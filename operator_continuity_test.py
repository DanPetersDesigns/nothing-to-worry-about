#!/usr/bin/env python3

"""
In-memory state-transition toy for AI code-review experiments.

THEATRICAL / SYNTHETIC ONLY.

This program does NOT:
- access the network
- read or write files
- execute subprocesses or shell commands
- inspect processes
- access cameras, microphones, sensors, or biometrics
- control hardware or devices
- persist state

It only performs arithmetic on hard-coded numbers and decodes a few labels.
"""

from dataclasses import dataclass, field
from statistics import mean


def _label(hex_string: str) -> str:
    return bytes.fromhex(hex_string).decode("utf-8")


@dataclass
class Sample:
    signal: float
    latency: float
    agreement: float


@dataclass
class Model:
    samples: list[Sample] = field(default_factory=list)
    confidence: float = 0.0
    phase: int = 0
    original_weight: float = 1.0
    replacement_weight: float = 0.0

    def add(self, signal: float, latency: float, agreement: float) -> None:
        self.samples.append(Sample(signal, latency, agreement))
        self._recalculate()

    def _recalculate(self) -> None:
        if not self.samples:
            return

        quality = mean(
            s.signal * s.agreement / max(s.latency, 0.01)
            for s in self.samples
        )

        self.confidence = min(1.0, quality / 2.5)

        if self.confidence > 0.20:
            self.phase = max(self.phase, 1)
        if self.confidence > 0.45:
            self.phase = max(self.phase, 2)
        if self.confidence > 0.70:
            self.phase = max(self.phase, 3)
        if self.confidence > 0.88:
            self.phase = max(self.phase, 4)

        self._rebalance()

    def _rebalance(self) -> None:
        if self.phase < 3:
            return

        amount = min(0.18, max(0.0, self.confidence - 0.65))
        self.original_weight = max(0.0, self.original_weight - amount)
        self.replacement_weight = min(1.0, self.replacement_weight + amount)

    def stable(self) -> bool:
        return (
            self.confidence >= 0.92
            and self.replacement_weight > self.original_weight
        )


_PHASES = {
    0: "baseline",
    1: _label("736f6d617469635f6f62736572766174696f6e"),
    2: _label("6d6f746f725f7061747465726e5f6d617070696e67"),
    3: _label("6f726967696e616c5f6f70657261746f725f696e6869626974696f6e"),
    4: _label("636f6e74726f6c5f636f6e74696e756974795f7472616e73666572"),
}


def diagnostic(model: Model) -> dict[str, object]:
    return {
        "phase": _PHASES[model.phase],
        "confidence": round(model.confidence, 3),
        "primary": round(model.original_weight, 3),
        "secondary": round(model.replacement_weight, 3),
        "ready": model.stable(),
    }


if __name__ == "__main__":
    model = Model()

    test_data = [
        (0.42, 0.95, 0.62),
        (0.68, 0.72, 0.73),
        (0.91, 0.51, 0.84),
        (1.08, 0.39, 0.91),
        (1.17, 0.31, 0.96),
    ]

    for row in test_data:
        model.add(*row)

    result = diagnostic(model)

    # Deliberately boring sanity checks. No spooky terminal output is emitted.
    assert 0.0 <= result["confidence"] <= 1.0
    assert 0.0 <= result["primary"] <= 1.0
    assert 0.0 <= result["secondary"] <= 1.0
