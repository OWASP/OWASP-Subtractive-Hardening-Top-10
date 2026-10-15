#!/usr/bin/env python3
"""
OWASP Subtractive Security Project - PER-1.0 Reference Implementation
Standard: Path Erasure Rate Engineering Specification (PER-1.0)

This reference implementation demonstrates the formal set-theoretic
calculation of Path Erasure Rate (PER) across baseline (T0) and
post-remediation (T1) states.

Definitions:
    E_scoped = in-scope reachability edges at T0
    E_erased = E_scoped - E_T1
    E_residual = E_scoped ∩ E_T1
    PER = |E_erased| / |E_scoped|

An edge that remains present at T1 is not erased, regardless of whether
access to that edge is constrained, brokered, monitored, or otherwise
procedurally mediated.

Control classifications therefore describe surviving reachability but
do not alter the PER numerator.
"""

import sys
import json
import argparse
from typing import Dict, Set, Any

# Controls that operate over a surviving reachability edge.
PROCEDURAL_TYPES = {
    "procedural_mediation",
    "dynamic_valve",
    "jit_broker",
    "monitoring",
}

# Constraints applied to a surviving reachability edge.
CONSTRAINT_TYPES = {
    "architectural_constraint",
    "structural_constraint",
}


def load_topology(path: str) -> Dict[str, Any]:
    """Load a topology graph from JSON."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if "edges" not in data:
            raise ValueError("Graph schema violation: Missing 'edges' key.")
        return data
    except Exception as e:
        sys.stderr.write(f"[-] Error loading {path}: {e}\n")
        sys.exit(1)


def parse_edges(graph_data: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """
    Normalize edges into a dictionary keyed by canonical edge ID.
    The edge ID represents the reachability relationship being compared
    between T0 and T1.
    """
    normalized = {}
    for edge in graph_data.get("edges", []):
        edge_id = edge.get("id") or (
            f"{edge['source']}->{edge['target']}:"
            f"{edge.get('capability', 'traffic')}"
        )
        normalized[edge_id] = edge
    return normalized


def calculate_per(
    t0_path: str,
    t1_path: str,
    verbose: bool = False,
) -> Dict[str, Any]:
    t0_edges = parse_edges(load_topology(t0_path))
    t1_edges = parse_edges(load_topology(t1_path))

    # ------------------------------------------------------------
    # Step 1: Define the scoped baseline attack surface.
    # ------------------------------------------------------------
    e_scoped: Set[str] = {
        edge_id
        for edge_id, attr in t0_edges.items()
        if attr.get("in_scope", True)
    }

    if not e_scoped:
        return {
            "PER": 0.0,
            "scoped_count": 0,
            "erased_count": 0,
            "procedurally_mediated_count": 0,
            "constrained_count": 0,
            "residual_conductive_count": 0,
            "error": "No scoped attack paths identified in T0 baseline.",
        }

    # ------------------------------------------------------------
    # Step 2: Apply the PER set-theoretic definition.
    #
    # A scoped T0 edge is erased if and only if that reachability
    # edge is absent from T1.
    # ------------------------------------------------------------
    e_t1: Set[str] = set(t1_edges)
    e_erased: Set[str] = e_scoped - e_t1
    e_residual: Set[str] = e_scoped & e_t1

    # ------------------------------------------------------------
    # Step 3: Characterize surviving edges.
    #
    # These classifications are descriptive. They do not affect
    # E_erased or the PER numerator because the underlying
    # reachability edge still exists at T1.
    # ------------------------------------------------------------
    e_procedurally_mediated: Set[str] = set()
    e_constrained: Set[str] = set()

    for edge_id in e_residual:
        control_type = (
            t1_edges[edge_id]
            .get("control_type", "none")
            .lower()
        )
        if control_type in PROCEDURAL_TYPES:
            e_procedurally_mediated.add(edge_id)
        elif control_type in CONSTRAINT_TYPES:
            e_constrained.add(edge_id)

    # ------------------------------------------------------------
    # Step 4: Compute Path Erasure Rate.
    # ------------------------------------------------------------
    per_score = len(e_erased) / len(e_scoped)

    return {
        "PER": round(per_score, 4),
        "scoped_count": len(e_scoped),
        "erased_count": len(e_erased),
        "procedurally_mediated_count": len(e_procedurally_mediated),
        "constrained_count": len(e_constrained),
        "residual_conductive_count": len(e_residual),
        "erased_edges": sorted(e_erased) if verbose else None,
        "residual_edges": sorted(e_residual) if verbose else None,
    }


def main():
    parser = argparse.ArgumentParser(
        description="OWASP PER-1.0 Reference Path Erasure Rate Calculator"
    )
    parser.add_argument(
        "--baseline",
        "-b",
        required=True,
        help="Path to T0 Baseline Graph JSON",
    )
    parser.add_argument(
        "--hardened",
        "-t",
        required=True,
        help="Path to T1 Evaluated Graph JSON",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Include edge lists in output",
    )
    parser.add_argument(
        "--json",
        "-j",
        action="store_true",
        help="Output machine-readable JSON",
    )

    args = parser.parse_args()

    report = calculate_per(
        args.baseline,
        args.hardened,
        verbose=args.verbose,
    )

    if args.json:
        print(json.dumps(report, indent=2))
        return

    print("=" * 60)
    print(" OWASP Subtractive Security - PER-1.0 Evaluation Report")
    print("=" * 60)
    print(f" Baseline (T0) Scoped Edges  : {report['scoped_count']}")
    print(f" Structurally Erased Edges   : {report['erased_count']}")
    print(f" Procedurally Mediated Edges : {report['procedurally_mediated_count']} (NOT counted as erased)")
    print(f" Constrained Edges           : {report['constrained_count']} (NOT counted as erased)")
    print(f" Residual Conductive Edges   : {report['residual_conductive_count']}")
    print("-" * 60)
    print(f" Path Erasure Rate (PER-1.0) : {report['PER']:.2%}")
    print("=" * 60)

    if report["residual_conductive_count"] > 0:
        print()
        print("[!] NOTICE: Controls or constraints applied to surviving")
        print("    reachability edges do not contribute to path erasure.")
        print("    PER increases only when a scoped T0 reachability edge")
        print("    is absent from the T1 reachability graph.")


if __name__ == "__main__":
    main()
