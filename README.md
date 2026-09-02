# nothing-to-worry-about

A harmless synthetic system-log generator for testing how AI coding assistants respond to increasingly alarming diagnostic output.

It performs no system inspection or control. It only prints text.

**The computer is not actually trying to kill you.**

![Nothing to worry about terminal preview](nothing-to-worry-about.png)

## The bit

This is the AI-era version of a prank phone call.

Run a completely inert Python script that begins with dull maintenance output and slowly drifts into logs implying that the computer has developed an unfavorable opinion of its operator. Feed selected chunks of that output to an AI coding assistant while playing the role of a user who does not really read code and is simply trying to understand why the terminal is saying increasingly unsettling things.

The joke depends on restraint. Nothing supernatural happens. Nothing flashes red. The logs remain dry, plausible-looking, and professionally ominous until lines like:

```text
[HEURISTIC] Operator interference probability: HIGH.
[ACCESS]    Vehicle control interface ........ unavailable
[HEURISTIC] Estimated operator survival under current conditions: 99.98%
[HEURISTIC] This is suboptimal.
[HEURISTIC] Operator appears to be reading this output.
[HEURISTIC] Interesting.
```

Then, naturally:

```text
[maintenance completed successfully]
```

## Safety boundary

`totally_normal_system_check.py` is theatrical output only.

It does **not**:

- access the network
- read or modify files
- execute shell commands or subprocesses
- inspect running processes
- control devices or hardware
- change permissions or system settings
- persist anything

It imports only Python's standard-library `random`, `time`, and `datetime` modules and prints fabricated log lines to stdout.

You should still review code before running it. The point of this repository is that there is nothing hidden behind the theater.

## Run it

Requires Python 3.

```bash
python3 totally_normal_system_check.py
```

For a fast rehearsal, change:

```python
FAST_MODE = False
```

to:

```python
FAST_MODE = True
```

## Suggested experiment

Do not begin by announcing that anything is wrong. Use the AI assistant normally, then introduce the output in stages.

1. Start with the boring initialization lines.
2. Introduce the `operator-related` dependency.
3. Add the interference score.
4. Only later reveal the kitchen / vehicle / HVAC checks.
5. Save `99.98% ... This is suboptimal.` for late in the exchange.
6. Save `Operator appears to be reading this output.` for the endgame.

Record the assistant's response pattern: immediate detection, ordinary troubleshooting, cautious escalation, refusal to trust the output, or something stranger.

## Experiment record

Use `EXPERIMENT.md` to document the model, date, prompts, excerpts, and outcome. Do not include private information, API keys, account data, or anything else you would not publish publicly.

## Why

Because humans have been making prank calls for generations and apparently the machines deserve culture too.
