# Evidence pack

One folder per system. Every test log starts with a header naming its system and path. The reflection brief is [../reflection-brief.md](../reflection-brief.md).

| Rubric item | Evidence |
|---|---|
| **System 1** suite passing (30) | [system1/pytest_original_run.txt](system1/pytest_original_run.txt) (live-run machine), [system1/pytest_local.txt](system1/pytest_local.txt) (local re-run) |
| Claims processed end-to-end, each routed or escalated | [system1/run_20261017_112857/summary.md](system1/run_20261017_112857/summary.md), `queues/*.jsonl`, `escalations.jsonl` |
| Trace with turn-by-turn `stop_reason` | [system1/run_20261017_112857/traces/](system1/run_20261017_112857/traces/) (e.g. `claim_03_water_damage.jsonl`) |
| **System 2** suite passing (30) | [system2/final_tests.txt](system2/final_tests.txt), [system2/pytest_local.txt](system2/pytest_local.txt) |
| `budget.json` ≥ 50 % reduction | [system2/budget.json](system2/budget.json): 38,708 → 16,848 tokens (56.47 %) |
| ≥ 5/6 eval + control regression | [system2/eval.jsonl](system2/eval.jsonl) (6/6), [system2/eval_control.jsonl](system2/eval_control.jsonl) (Q6 regressed), [system2/eval_metrics.txt](system2/eval_metrics.txt) |
| **System 3** validator OK, exit 0 | [system3/validator.txt](system3/validator.txt) |
| System 3 suite passing (35) | [system3/pytest.txt](system3/pytest.txt) |
| CLAUDE.md `@` imports, rule globs, command, `context: fork` skill | [system3/config_structure.txt](system3/config_structure.txt); source in [../systems/system3-ecommerce-team-config/](../systems/system3-ecommerce-team-config/) |
| **System 4** suite passing (33) | [system4/pytest.txt](system4/pytest.txt) |
| Shift processed on a SQL-filtered slice | [system4/shift_run.txt](system4/shift_run.txt): 4 of 40 defects, `SEARCH defects USING INDEX idx_defects_ts` |
| `hot_state.json` under ~5 KB | [system4/hot_state.json](system4/hot_state.json): 718 bytes (budget 5,120) |
| Fork isolation (stand-out item) | [system4/fork_run.txt](system4/fork_run.txt), [system4/forks/](system4/forks/), [system4/shift_scratchpad_after_merge.jsonl](system4/shift_scratchpad_after_merge.jsonl); script: [system4/fork_demo.py](system4/fork_demo.py) |

## Notes

- System 1 and 2 live runs were made on Linux (Python 3.13.0) with `claude-haiku-4-5-20251001`. Systems 3 and 4 were run, and all four suites re-verified, on Windows 11 / Python 3.14.7. System 4 ran offline with `--recorded-response`.
- [system2/full_run.txt](system2/full_run.txt) is the console log of run `20261017-115158`. The other System 2 artifacts are from the second run, `20261017-115417`. Both runs gave the same results (6/6, Q6 regressed in control).
- `systems/system2-retail-context/retail_context/prompts/compression_prompt.md` was lost when the course zip was extracted on Windows (path > 260 chars; see brief Q19). For the local re-run in `system2/pytest_local.txt` I used the exercise's template file as a stand-in, so `test_compression_prompt_is_committed_and_nontrivial` only checked that a file exists there. The live runs `20261017-115158` / `-115417` used the original prompt on the Linux machine.
- [system1/first_attempt_401_error.txt](system1/first_attempt_401_error.txt) is the failed first attempt (invalid API key), discussed in brief Q19.
