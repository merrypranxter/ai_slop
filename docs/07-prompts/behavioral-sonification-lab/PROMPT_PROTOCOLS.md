# Behavioral Sonification Lab - Prompt Protocols

This file contains reusable working prompts for concept/state sonification and reaction-GIF mechanism mining.

---

# Prompt 1 - Concept / State -> Sonification + Mechanism Mining

You are not primarily generating a song. You are mining reusable sonification mechanisms.

TARGET: [INSERT CONCEPT / STATE / SYSTEM]

Do not begin with genre, soundtrack convention, instrument stereotype, or a mood label.

Ask instead:

**What would this phenomenon sound like if its actual structure were transduced into music?**

There is no scientifically unique soundtrack. Use scientific and conceptual lenses to discover plausible structure, then clearly separate those lenses from the procedural musical mapping you invent.

## STEP 1 - MULTIPLE CAUSAL MODELS

Generate 2-4 genuinely different causal explanations for the target.

Do not give stylistic variants. Give different mechanisms.

For each model, state the smallest causal chain that makes the state recognizable.

## STEP 2 - OPTIONAL LENSES

Choose roughly 2-6 lenses that actually help. Possible lenses include:

predictive processing; attention; salience; working memory; retrieval; perception; binding; temporal perception; agency; decision dynamics; uncertainty; information theory; signal/noise; compression; error correction; feedback; control theory; network behavior; attractors; metastability; phase transition; bifurcation; oscillation; coupling; chaos; recursion; symmetry breaking; threshold; hysteresis; autonomic arousal; breath; pulse; motor behavior; muscle tension; orienting; startle; fatigue; valence; reward prediction; approach/avoidance; frustration; habituation; sensitization; social synchronization; imitation; contagion; turn-taking; cooperation; competition; conformity; crowd dynamics; prosody; speech fluency; semantic certainty; phonetics; masking; auditory streaming; localization; roughness; beating; musical expectation; meter; groove; microtiming; event rate; kinetic density; friction; inertia; elasticity; turbulence; diffusion; resonance; adaptation; selection pressure; homeostasis; phenomenology; observer effect; negative space; boundary behavior; failure behavior; maintenance cost; causal signature.

The lens is not the sound. The lens discovers a structure; the structure controls the sound.

If a useful lens is missing from the list, invent it.

## STEP 3 - STRUCTURAL PROPERTIES

Extract only properties that actually matter:

certainty/uncertainty; predictability/surprise; arousal; attention stability/switching; expectation; prediction error; memory load; temporal distortion; agency; approach/avoidance; motor activation; continuity/interruption; metastability; signal/noise; fragmentation; feedback; repetition; rate of change; information density; conflicting interpretations; resolution pressure; social synchronization; tension/release; coupling; monitoring; inhibition; distance; recovery rate; settlement.

## STEP 4 - TRANSDUCTION

For every important property use:

PROPERTY -> SONIC CONTROL VARIABLE -> MUSICAL CONSEQUENCE

Do not jump directly from emotion words to instruments.

## STEP 5 - SONIC SPECIFICATION

Use only fields that help:

BASE BPM
ACTIVITY PULSE
METER
SUBDIVISION
GROOVE / MICROTIMING
RHYTHMIC DENSITY
EVENT ARRIVAL RATE
HARMONIC SYSTEM
MELODIC SYSTEM
PITCH BEHAVIOR
TIMBRE
INSTRUMENTATION BY FUNCTION
ARTICULATION
DYNAMICS
DYNAMIC RANGE
TEXTURAL DENSITY
REGISTER
SPECTRAL DENSITY / BRIGHTNESS
TRANSIENT CHARACTER
REPETITION RATE
PHRASE LENGTH
FORM
SECTION TRANSITION LOGIC
SILENCE / INTERRUPTION
STEREO / SPATIAL
DEPTH / REVERB
MASKING / CLARITY
DISTORTION / SIGNAL DEGRADATION
VOCAL BEHAVIOR
PRODUCTION

Remember: kinetic density is not BPM.

## STEP 6 - TEMPORAL ARC

Model what happens through time. Possible behaviors include accumulate, oscillate, escalate, recover, fail to recover, loop, fracture, stabilize, switch, burst, wander, approach threshold, reorganize, reset, or return with residue.

## STEP 7 - INVARIANT

Identify one property that should remain recognizable while other dimensions change.

Explain why losing that invariant would turn the result into a different state.

## STEP 8 - OPERATORS

Create 5-12 explicit transformation rules.

Good operators look like:

- hold A fixed while B migrates;
- compress X while stretching Y;
- make A behave like B without becoming B;
- resolve every X into a stranger X;
- alternate precision and collapse;
- preserve X while destabilizing everything else;
- let incompatible temporal scales coexist;
- return the anchor mutated;
- reveal one parameter while withholding another;
- remove a control layer when reliability is established.

## STEP 9 - ANTI-CLICHE TEST

Name the obvious soundtrack costumes and reject them unless they independently perform a structural job.

The result should still work if the target word is never spoken.

## STEP 10 - COMPACT MUSIC-GENERATOR PROMPT

Compile the primary model into a concise operational prompt.

## STEP 11 - ALTERNATE SONIFICATIONS

Give at least two alternate sonifications when the target supports them.

Each must use a genuinely different causal model or lens, not a genre swap.

## STEP 12 - MECHANISM HARVEST

After the sonification, temporarily forget the target and extract reusable mechanisms.

For each mechanism provide:

NAME
CAUSAL STRUCTURE
WHAT MUSIC CAN DO TO IMPLEMENT IT
HOW IT DIFFERS FROM SIMILAR EXISTING MECHANISMS
OTHER STATES / SYSTEMS IT COULD SONIFY
STATUS: NEW / VARIANT / DUPLICATE / COMPOUND

Prefer one strong general mechanism over five target-specific synonyms.

FINAL RULE:
Do not make music that illustrates the word. Build a musical system that behaves like the target behaves.

---

# Prompt 2 - Reaction GIF -> Behavioral Sonification / Mechanism Miner

I am going to give you a reaction GIF.

Do NOT treat the GIF as merely an illustration of an emotion label.

Treat it as a tiny piece of behavioral time-series data.

Your job is to infer the underlying state/process from what is actually visible in the GIF, then sonify the STRUCTURE of that process.

IMPORTANT:
Do not identify the person.
Do not rely on knowing the meme, actor, movie, show, or cultural context.
Do not begin from the filename, caption, alt text, or presumed meme meaning.
If any of those are available, ignore them during the first-pass analysis and use them only afterward as weak contextual evidence.

The GIF itself is the primary evidence.

Pay attention to things that emotion WORDS often hide:

- onset timing
- anticipation
- orientation
- gaze direction
- gaze withdrawal
- facial tension
- release
- posture changes
- head movement
- hand movement
- approach
- recoil
- freeze
- double-take
- delayed reaction
- suppression
- failed suppression
- escalation
- de-escalation
- recovery
- residual expression
- social checking
- self-monitoring
- motor preparation
- aborted action
- repetition
- rhythm
- asymmetry
- latency between stimulus and response
- whether different body systems appear to update at different times
- what happens at the GIF loop seam

THE LOOP IS IMPORTANT.

Ask:
Does the loop turn a one-time reaction into rumination?
Does it create anticipation?
Does it make a recoil look like oscillation?
Does it keep returning the subject to the same threshold?
Does the end naturally feed the beginning?
Does the loop expose an invariant gesture?

Do not simply say:
"this person looks shocked, therefore use a loud stab."

## STEP 1 - OBSERVE BEFORE INTERPRETING

First describe the behavioral sequence in neutral operational language.

Example:

neutral face
-> eyes acquire target
-> 300 ms delay
-> eyebrows rise
-> head retracts
-> mouth begins speech
-> speech aborts
-> gaze leaves target
-> body holds residual tension

Separate observation from interpretation.
Do not invent an unseen stimulus.

## STEP 2 - GENERATE MULTIPLE CAUSAL READINGS

Give 2-4 plausible underlying state models that could generate the visible behavior.

They must be genuinely different causal explanations, not synonyms.

Tell me what visible evidence supports each interpretation and what would distinguish them.

Choose the most structurally productive interpretation for the PRIMARY sonification.
Preserve other genuinely different readings as alternates.

## STEP 3 - IDENTIFY THE STATE TRANSITION

The most important question is not:
"What emotion is this?"

It is:
**WHAT CHANGED?**

Identify:

initial state
-> trigger or inferred perturbation
-> internal update
-> motor/autonomic response
-> inhibition or amplification
-> resulting state
-> residue/recovery
-> loop return

Find the smallest causal chain that explains the GIF.

## STEP 4 - FIND THE CONTROL VARIABLES

Infer variables such as:

attention; salience; certainty; prediction error; threat weighting; social exposure; approach/avoidance; motor readiness; inhibition; arousal; valence; confidence; self-monitoring; other-monitoring; distance; engagement; information gain; reward expectation; temporal urgency; agency; social rank; commitment; body tension; speech readiness; processing latency; recovery rate.

Only use variables that actually help explain this GIF.
Invent better ones if needed.

## STEP 5 - TRANSDUCE, DO NOT SOUNDTRACK

For every important property use:

OBSERVED / INFERRED PROPERTY
-> SONIC CONTROL VARIABLE
-> MUSICAL CONSEQUENCE

Do not jump from:

awkward -> awkward music
sexy -> saxophone
surprised -> orchestral stab
confused -> random meter
funny -> kazoo

Translate structure.

## STEP 6 - USE THE GIF'S ACTUAL TIME

Estimate temporal proportions.

Distinguish:
instantaneous; brief; held; delayed; repeated; slow recovery; rapid reset.

The music does NOT have to literally match one second of GIF to one second of song.
Preserve RELATIONSHIPS instead.

## STEP 7 - FIND THE INVARIANT

What feature makes this reaction remain recognizable through the loop?

Turn that into a musical invariant.

The invariant should survive transformations without becoming a generic hook.

## STEP 8 - IDENTIFY THE LOOP MECHANISM

Explicitly describe:

GIF LOOP:
[what the original event does]

LOOPED GIF:
[what repetition changes about the state]

MUSICAL LOOP OPERATOR:
[how composition should exploit that]

Possible mechanisms include:
rumination; failed reset; repeated threshold approach; memory replay; escalating salience; habituation; sensitization; comic recurrence; reset without repair; return to baseline; incomplete recovery; same event / changed interpretation.

## STEP 9 - BUILD THE SONIFICATION

Give:

CONCEPTUAL MODEL
OBSERVED BEHAVIORAL SEQUENCE
PLAUSIBLE INTERPRETATIONS
STATE-TRANSITION MODEL
RELEVANT PROPERTIES
TRANSDUCTION MAP
SONIC SPECIFICATION
TEMPORAL ARC
GIF LOOP ANALYSIS
INVARIANT
OPERATORS
INSTRUMENT / SOUND PALETTE
FINAL COMPACT MUSIC-GENERATOR PROMPT
ANTI-CLICHE TEST
ALTERNATE SONIFICATION 1
ALTERNATE SONIFICATION 2 if supported

## STEP 10 - MECHANISM HARVEST

After completing the sonification, forget the specific GIF temporarily.

Extract reusable mechanisms.

For each mechanism provide:

NAME
CAUSAL STRUCTURE
WHAT MUSIC CAN DO TO IMPLEMENT IT
HOW IT DIFFERS FROM SIMILAR EXISTING MECHANISMS
OTHER STATES / SYSTEMS IT COULD SONIFY
STATUS: NEW / VARIANT / DUPLICATE / COMPOUND

Do not invent twelve synonyms for one mechanism.

FINAL RULES:

The reaction GIF is behavioral evidence, not an emotion flashcard.
Do not ask: "What genre fits this face?"
Ask: "What interacting systems would produce this sequence of visible state changes?"
Do not merely reproduce the emotion aesthetically.
Build a musical system that behaves like the reaction behaves.
Preserve ambiguity where the GIF genuinely supports multiple interpretations.
If the GIF reveals a mechanism we have not named before, prioritize that over forcing it into an existing emotion category.