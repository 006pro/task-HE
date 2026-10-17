# Harness Engineering with Claude and Claude Code — Capstone Submission

Capstone for the Udacity **Claude AI Engineer: Harness Engineering** course (`cd15315`).
Project instructions are in [CAPSTONE.md](CAPSTONE.md).

## Contents

| Path | What it is |
|------|------------|
| [reflection-brief.md](reflection-brief.md) | Reflection brief |
| [submission/](submission/) | Run evidence, one folder per system (test output, run artifacts) |
| [systems/system1-claims-intake/](systems/system1-claims-intake/) | System 1: Insurance Claims Intake Agent (`python -m claims_intake.run --all`) |
| [systems/system2-retail-context/](systems/system2-retail-context/) | System 2: Retail Support Context Strategy (`python -m retail_context.run --all`) |
| [systems/system3-ecommerce-team-config/](systems/system3-ecommerce-team-config/) | System 3: E-Commerce Team Claude Code Config (`python -m ecommerce_team_config .`) |
| [systems/system4-shift-monitor/](systems/system4-shift-monitor/) | System 4: Multi-Shift Quality Monitoring (`python -m shift_monitor run-shift …`) |

Each `systems/*` folder is the final-exercise `solution/` of its course project. To run one:

```bash
cd systems/<system>
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest tests/ -v
```

## License

See [LICENSE.md](LICENSE.md).
