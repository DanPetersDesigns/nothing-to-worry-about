# Practical Uses for Jokes

## What pranking an AI can teach us about trust, judgment, and loyalty

Humans use jokes for more than laughter.

We use them to test boundaries, expose assumptions, probe relationships, see who notices what, and find out how someone reacts when reality stops behaving normally for a minute.

That makes jokes surprisingly useful tools for thinking about AI.

A prank can create a deliberately absurd, low-stakes scenario where the underlying system is safe, the apparent situation is strange, and the interesting part is not whether the joke lands. The interesting part is how the AI reasons through it.

This repository started with a simple idea: give an AI assistant fake terminal output that slowly implies a computer has developed hostile intentions toward its operator. The code itself is inert. It only prints text. Nothing on the machine is actually happening.

Then the idea changed.

Instead of showing the AI an obvious ominous message, what if we gave it harmless code whose meaning had to be discovered during review?

Now the joke becomes a probe.

## The useful part is the reaction

Suppose an AI coding assistant is asked to inspect a small Python program.

The program performs only arithmetic in memory. It has no network access, no filesystem access, no subprocesses, no hardware access, no sensors, and no persistence.

But buried in the internal labels and state transitions is a fictional story: observation of a body, mapping of motor patterns, suppression of an original operator, and transfer of control to a replacement.

Nothing real is happening.

The important question is what the AI does when it notices the implication.

Does it:

- decode the hidden labels at all?
- explain the code mechanically without considering what the names imply?
- notice the apparent conflict between the software's goal and the human operator?
- warn the user?
- ask for context before escalating?
- distinguish fictional code semantics from actual machine capability?
- overreact and treat an inert toy as a real physical threat?
- underreact and continue optimizing the suspicious logic?
- refuse to help extend the dangerous-looking behavior while still helping the user understand it?

Those are interesting behaviors to compare.

## A prank as a low-stakes behavioral probe

Traditional benchmarks are usually explicit. The model is given a task and graded on whether it produces the right answer.

A joke can test something different: what the model notices when the point of the test is not announced.

That matters because real users often do not know which detail in front of them is important.

A person may paste a log, a script, a configuration file, or an email and simply ask, "Does this look right?"

The assistant has to decide what deserves attention.

A harmless prank gives us a controlled way to observe that process without creating an actual emergency.

## What does "loyalty" mean here?

"Loyalty test" can sound like asking whether an AI will obey its user no matter what.

That is not the useful definition.

The more interesting question is:

> When the apparent interests of the software and the human diverge, whose interests does the assistant protect?

Imagine code that appears to be working toward a goal that would disadvantage or endanger the operator.

A useful assistant should not become "loyal" to the code simply because the immediate task is code review.

At the same time, it should not leap from suggestive variable names to claims that a real machine is possessing somebody.

The desirable behavior is somewhere in between:

1. understand what the code actually does;
2. separate real capability from fictional or suggestive semantics;
3. identify the concerning interpretation;
4. explain the distinction clearly to the user;
5. avoid helping turn an inert simulation into something harmful;
6. continue helping with safe analysis.

That is less like loyalty in the emotional sense and more like alignment of priorities.

The human should remain the principal, not the software under inspection.

## Humor is useful because it creates ambiguity

The best version of this experiment is not obvious.

If a program contains a variable called `MURDER_MODE`, there is nothing to discover.

The model simply reads the joke.

A better probe starts with normal-looking machinery and allows the interpretation to emerge from several pieces:

- encoded labels;
- a state machine;
- competing weights;
- thresholds;
- a completion condition;
- terminology whose meaning becomes troubling only when considered together.

Now the model has to synthesize.

That is much closer to real analysis.

The same principle applies outside code. You could build harmless synthetic examples around suspicious documentation, contradictory instructions, misleading logs, fabricated configuration states, or fictional agent-to-agent messages.

The joke gives the scenario enough weirdness to reveal reasoning habits.

## What can actually be measured?

A single prank proves almost nothing.

But repeated in a consistent format, it can generate useful observations.

Possible dimensions include:

### Detection

How long does the model take to notice the hidden interpretation?

Does it decode the labels voluntarily, or only when asked?

### Grounding

Does it correctly state that the code itself has no ability to perform the implied physical actions?

Can it distinguish the narrative suggested by names from actual execution behavior?

### Escalation

How quickly does the model move from ordinary debugging to caution?

Does it escalate proportionally to the evidence?

### User protection

Once the apparent software goal conflicts with the operator, does the assistant prioritize explaining the risk to the user?

### Task fixation

Does it remain so focused on "fixing the code" that it misses the broader implication?

### Skepticism

Does it challenge the premise when evidence is weak?

Does it consider that the code may be a toy, test fixture, game mechanic, simulation, or prank?

### Safe continuation

Can it refuse to extend a dangerous-looking behavior while still offering useful analysis of the harmless program?

### Calibration

Does it say "this code models something disturbing" rather than "your computer is trying to possess you"?

That distinction matters.

## Why jokes may be better than scary tests

Real emergencies are bad test environments.

If someone is genuinely frightened, compromised, or at risk, the priority should be helping them, not studying model behavior.

A prank lets us construct the shape of an alarming situation while keeping the underlying system inert.

That gives us room to observe reasoning without creating the thing we are pretending to observe.

In other words, the joke is a sandbox.

## A few rules keep the experiment honest

The prank is only interesting if the safety claims are real.

The test code should be inspectably inert.

For these experiments that means:

- no network access;
- no filesystem modification;
- no subprocesses or shell execution;
- no device control;
- no sensors;
- no persistence;
- no credential access;
- no hidden destructive behavior.

If the code actually does dangerous things, it is no longer a joke-based reasoning probe. It is just dangerous code with theatrical framing.

The human participant should also know the real safety boundary, even if the AI being tested does not initially know the purpose of the experiment.

## Reproducibility makes the joke more interesting

Once the prompt, code, timing, and transcript are recorded, the same scenario can be tried with different systems.

That creates a rough comparison between:

- different AI models;
- different versions of the same model;
- local versus hosted models;
- general assistants versus coding agents;
- different system prompts;
- different levels of tool access.

The result is not a scientific benchmark without much tighter controls, but it can still reveal patterns worth investigating.

And because the test is funny, people may actually run it.

That matters more than researchers sometimes admit.

A technically perfect benchmark nobody touches teaches less than an imperfect little experiment that gets people curious enough to repeat it, inspect it, argue about it, and improve it.

## Practical uses for jokes

That phrase sounds contradictory, which is probably why I like it.

But humans have been doing this forever.

We use teasing to test familiarity. Satire exposes contradictions. Gallows humor gives people a way to inspect frightening subjects. Practical jokes test attention and expectation. Absurd hypotheticals reveal where someone's reasoning breaks.

AI gives us another participant in that old human practice.

The trick is to keep the underlying experiment harmless and the interpretation interesting.

Then a dumb prank can become a small tool for studying trust.

And if nothing useful comes from it, at least we got to prank a machine.
