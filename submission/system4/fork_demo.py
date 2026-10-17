"""Exercise the System 4 fork path end-to-end.

Forks the post-shift hot state into two competing hypotheses about the
capacitor-bank-C-7 cluster, writes findings to each fork's own scratchpad,
then shows the base state and main scratchpad were untouched until an
explicit merge_findings().

Run from systems/system4-shift-monitor after a run-shift:
    python ../../submission/system4/fork_demo.py
"""

from __future__ import annotations

import hashlib
from datetime import UTC, datetime
from pathlib import Path

from shift_monitor.fork import fork_for_hypothesis, merge_findings
from shift_monitor.scratchpad import Scratchpad, ScratchpadEntry
from shift_monitor.warm import WarmStore

DATA = Path("data")
BASE = DATA / "hot_state.json"
MAIN_PAD = DATA / "shift_scratchpad.jsonl"
FORKS = DATA / "forks"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


warm = WarmStore(DATA / "warm.sqlite")
c7 = [r for r in warm.defects_since("2026-03-01T00:00:00Z", limit=100) if r["component"] == "capacitor-bank-C-7"]
night = [r for r in c7 if r["shift"] == "C"]
print(f"capacitor-bank-C-7 defects in warm tier: {len(c7)} (shift C: {len(night)})")

base_before = sha(BASE)
main_before = len(Scratchpad(MAIN_PAD).read())
print(f"base hot_state sha256[:16] before fork: {base_before}; main scratchpad entries: {main_before}")

hypotheses = {
    "H1-lot-dielectric": (
        f"{len(c7)} C-7 defects span multiple lots/dates; lot 2026-0430-B DAR 0.39 vs spec >0.7",
        "Supports a material (impregnation/moisture) cause; quarantine lot and retest retains.",
    ),
    "H2-station-drift": (
        f"{len(night)}/{len(c7)} C-7 defects on shift C only",
        "Shift concentration suggests test-station calibration/probe drift; check station before blaming lot.",
    ),
}

fork_pads: list[Path] = []
for hid, (evidence, conclusion) in hypotheses.items():
    fork_dir = fork_for_hypothesis(BASE, hid, FORKS)
    pad = fork_dir / "scratchpad.jsonl"
    Scratchpad(pad).append(
        ScratchpadEntry(hypothesis_id=hid, evidence=evidence, conclusion=conclusion, ts=datetime.now(UTC))
    )
    fork_pads.append(pad)
    print(f"fork {hid}: dir={fork_dir.as_posix()} hot_state copy sha={sha(fork_dir / 'hot_state.json')} "
          f"scratchpad entries={len(Scratchpad(pad).read())}")

print(f"H1 scratchpad sees H2 entry? {any(e.hypothesis_id == 'H2-station-drift' for e in Scratchpad(fork_pads[0]).read())}")
print(f"H2 scratchpad sees H1 entry? {any(e.hypothesis_id == 'H1-lot-dielectric' for e in Scratchpad(fork_pads[1]).read())}")
print(f"base hot_state unchanged after forks: {sha(BASE) == base_before}")
print(f"main scratchpad entries after forks (before merge): {len(Scratchpad(MAIN_PAD).read())}")

merge_findings(fork_pads, MAIN_PAD)
after = Scratchpad(MAIN_PAD).read()
print(f"main scratchpad entries after merge_findings: {len(after)} -> {[e.hypothesis_id for e in after]}")
print(f"base hot_state still unchanged after merge: {sha(BASE) == base_before}")
