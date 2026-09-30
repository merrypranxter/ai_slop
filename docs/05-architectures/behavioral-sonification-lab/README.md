# WHAT DOES IT SOUND LIKE?
## Behavioral Sonification Lab / Reaction Mechanism Atlas

**Status:** ACTIVE RESEARCH SYSTEM  
**Project:** AI SLOP - Structured Instability Lab  
**Canonical home:** `docs/05-architectures/behavioral-sonification-lab/`  
**Primary media:** audio / Suno, with cross-media operator reuse  
**Working question:** *What would a concept, emotion, cognitive state, bodily state, social interaction, system failure, or visible reaction sound like if its actual structure were transduced into music rather than merely illustrated by a genre?*

---

## 1. The thing we are building

The Behavioral Sonification Lab is a mechanism-mining system.

It does not begin with "what genre sounds like jealousy?" or "what instrument means confusion?" It begins with a harder question:

> What interacting processes make this state recognizable, and what can music do that is structurally equivalent to those processes?

The output is therefore not primarily a song prompt. The song prompt is a compiled artifact downstream of a richer model.

The real products are:

- causal models of a target state;
- reusable sonification mechanisms;
- musical control dimensions;
- invariants;
- transformation operators;
- contrastive boundaries between neighboring states;
- reaction-loop mechanics;
- a growing map of mechanism-space.

The project is deliberately anti-costume. "Sexy" is not saxophone. "Curious" is not a music box. "Suspicious" is not noir. "Existential horror" is not a choir and a black hole. Those are cultural signifiers. They may occasionally be useful timbres, but they are not the mechanism.

The governing rule is:

> **THE LENS IS NOT THE SOUND. THE LENS DISCOVERS A STRUCTURE. THE STRUCTURE CONTROLS THE SOUND.**

A second governing rule has emerged from the experiments:

> **WEIRDNESS NEEDS A FLOOR.**

A violation is legible only if enough surrounding structure remains intact to reveal what was violated. Suspicion needs a plausible cover. Silly needs a competent task. Embarrassment needs a functioning social room. Curiosity needs a known map around the missing tile. Confusion needs several coherent parses, not random noise.

---

## 2. Why this belongs in AI SLOP

AI SLOP already treats creative work as structured instability: ordinary assumptions are subjected to precise interventions, multiple constraints stay active, the system attempts a compromise, and the resulting artifact is observed and reused.

Behavioral sonification is the audio-facing version of that principle at a finer causal resolution.

Instead of:

`emotion word -> mood -> genre`

it uses:

`target -> competing causal models -> useful lenses -> structural properties -> reusable mechanisms -> musical controls -> temporal behavior -> invariant -> composition`

The method also extends the existing Suno rule of separated jurisdictions. Harmony, melody, rhythm, timbre, performance, space, voice, production, and form can be given different jobs instead of being blended into a single stylistic soup.

The important move is that a psychological, social, physical, computational, or visible behavioral property must become a **repeatable control relation**.

Example:

`released monitoring -> remove the check layer -> leave a counted hole without insurance`

is stronger than:

`trust -> warm chords`

because the first mapping can be tested, varied, recombined, and reused outside trust.

---

## 3. Epistemic status

There is no scientifically unique soundtrack for confusion, jealousy, trust, lust, boredom, embarrassment, or any other target in this archive.

The method may use ideas from cognitive science, affective science, psychophysiology, information theory, dynamical systems, linguistics, control theory, social behavior, perception, and other disciplines. Those sources help identify plausible structure. They do not prove that a specific BPM, chord, timbre, or instrument is the correct sonic representation of a human state.

Use the following distinction:

- **SUPPORTED LENS:** the scientific or conceptual framing is consistent with established descriptions of the state or process.
- **PROCEDURAL TRANSDUCTION:** the mapping from that structure into music is an artistic rule imposed by us.
- **SPECULATIVE MECHANISM:** a promising reusable operator that still needs comparison against other specimens.
- **OBSERVED ARTISTIC EFFECT:** a repeated output behavior actually noticed across generations.

The method is strongest when it says exactly what is fact, what is interpretation, and what is invented musical machinery.

---

# 4. Core architecture

## 4.1 Target

A target can be:

- an emotion or motivational state;
- a cognitive process;
- a social interaction;
- a bodily process;
- a physical or biological system;
- an information problem;
- an institutional process;
- a paradox or failure mode;
- a reaction GIF or short video;
- a personal recurring state;
- an unnamed micro-transition visible only in behavior.

Examples already used include confusion, jealousy, infatuation, lust, boredom, curiosity, trust, embarrassment, suspicion, silliness, flirtation, seduction, titillation, mundane morning existential horror, and an unlabeled reaction GIF.

## 4.2 Candidate causal models

Before settling on a sonification, generate 2-4 genuinely different explanations of what the target is doing.

The alternatives must differ causally, not cosmetically.

For confusion, for example:

- metastable competition among plausible models;
- working-memory chunking failure;
- social common-ground failure.

For lust:

- proximity-gain toward a body lock;
- excitation vs inhibition as dual control;
- interoceptive overwrite of a resting body-score.

For a GIF:

- frozen appraisal plus continuing orientation;
- motor-ready speech without authorization;
- entrainment of a moving body under a parked social display.

The point is to avoid treating the first familiar label as the only explanation.

## 4.3 Optional lens library

Lenses are methods of understanding, not sound presets. Select only the ones that reveal useful structure.

Useful lens families include:

- predictive processing and prediction error;
- attention and salience;
- working memory and retrieval;
- perceptual organization and binding;
- temporal perception;
- agency and control;
- information theory, compression, signal/noise, error correction;
- feedback and control theory;
- dynamical systems, attractors, metastability, phase transitions, bifurcation, hysteresis;
- autonomic arousal, breath, pulse, motor behavior, muscle tension;
- reward, wanting, approach/avoidance, frustration, habituation, sensitization;
- social synchronization, turn-taking, imitation, conformity, competition, cooperation;
- prosody, speech fluency, phonetics, articulatory effort, semantic certainty;
- psychoacoustics, masking, roughness, auditory streaming, localization, beating;
- musical expectation, meter, groove, microtiming, kinetic density, repetition, form;
- friction, inertia, elasticity, viscosity, turbulence, diffusion, pressure, resonance;
- adaptation, ecological competition, mutualism, selection pressure, homeostasis;
- phenomenology: subjective time, familiarity, presence, coherence, self/world boundary;
- failure behavior, maintenance cost, residue, observer effect, negative space, causal signature.

Recommended modes for an eventual interface:

- **AUTO LENSES:** model chooses 2-6 useful lenses.
- **PICK LENSES:** user selects them.
- **FUCK ME UP:** use one ordinary lens plus one or two non-obvious lenses that still genuinely fit.

## 4.4 Structural property extraction

The selected model is decomposed into variables such as:

- certainty / uncertainty;
- predictability / surprise;
- information gain;
- attention stability / switching;
- prediction error;
- memory load;
- temporal distortion;
- agency;
- approach / avoidance;
- arousal;
- motor activation;
- continuity / interruption;
- metastability;
- signal / noise;
- fragmentation;
- feedback;
- repetition;
- rate of change;
- density;
- social synchronization;
- threshold pressure;
- monitoring;
- coupling;
- inhibition;
- distance;
- reward expectation;
- recovery rate;
- settlement / non-settlement.

Only variables that explain the target should be retained.

## 4.5 Transduction

Each important property is converted through a stable mapping:

`PROPERTY -> SONIC CONTROL VARIABLE -> MUSICAL CONSEQUENCE`

Example:

`time becomes explicit -> audible clock-period -> barline and interval become foreground objects`

Example:

`released monitoring -> delete checker layer -> holes remain without compensatory clicks`

Example:

`small cue / oversized reflex -> local automation gain -> a tiny grain produces a body-sized response`

The mapping should be inferable if repeated.

## 4.6 Sonic mechanism selection

A **mechanism** is something music can do.

Examples:

- hold a clock fixed while density rises;
- preserve a slot while changing its occupant;
- replay the same bar under a different weighting;
- open one spectral band and close it again;
- let two independent clocks converge;
- leave a hole that another part may, must, or is being tested to fill;
- preserve an object while changing only its viewpoint;
- restart a loop without repairing the cause of the loop.

Mechanisms must eventually become independent of the target that revealed them.

`CODEC LOCK`, for example, should not remain "an infatuation operator." It is a general representational behavior that can be reused wherever incoming detail is forced through a fixed low-resolution model.

## 4.7 Musical control dimensions

Mechanisms act on control dimensions. The current control space includes:

- base BPM;
- activity pulse;
- meter;
- subdivision;
- microtiming;
- event arrival rate;
- rhythmic density;
- phrase length;
- harmonic center;
- cadence probability;
- tonal ambiguity;
- pitch range;
- pitch stability / drift;
- register;
- repetition rate;
- recurrence distance;
- spectral brightness;
- spectral density;
- masking;
- transient character;
- articulation;
- dynamics;
- dynamic range;
- texture density;
- stereo bearing;
- width;
- depth / reverb;
- proximity;
- distortion / degradation;
- voice count;
- vocal overlap;
- hocketing;
- lexical density;
- speech-singing boundary;
- breath behavior;
- prosodic certainty;
- instrumentation by functional job;
- form;
- section transition logic;
- silence / interruption;
- production clarity;
- state-dependent parameter access.

A major recurring principle is:

> **KINETIC DENSITY IS NOT BPM.**

A track may keep the base clock fixed while changing perceived speed through subdivisions, event rate, ghost activity, microtiming, or layer participation.

## 4.8 Temporal model

The target must be described through time.

Possible temporal behaviors include:

- accumulate;
- oscillate;
- escalate;
- habituate;
- sensitize;
- recover;
- fail to recover;
- loop;
- fracture;
- stabilize;
- switch;
- burst;
- wander;
- approach a threshold;
- reorganize after a threshold;
- return with residue;
- reset without repair.

## 4.9 Invariant

Every strong specimen identifies something that remains recognizable while other systems mutate.

Examples:

- confusion: a 5-note cell that migrates through incompatible parses;
- lust: a low contact-period;
- boredom: clock + unimproved 2-bar official cell;
- curiosity: question-cell;
- trust: contract coordinate;
- embarrassment: exact flub clip;
- suspicion: tell-pocket;
- silly: competent walk-cell;
- flirt: dual-use bid-cell;
- titillation: tiny tickle-grain;
- reaction GIF: unclosed aperture.

The invariant prevents the piece from dissolving into generic change.

## 4.10 Alternatives and mechanism harvest

Every full run should produce at least two alternate legitimate sonifications when the target supports them.

After the musical design is finished, the target is temporarily forgotten and the run is mined for general operators.

Each harvested mechanism should record:

- name;
- causal structure;
- musical implementation;
- how it differs from similar mechanisms;
- other domains where it could be reused;
- source specimen;
- status: NEW / VARIANT / DUPLICATE / COMPOUND.

This prevents the library from accumulating twelve names for the same operation.

---

# 5. Three libraries, not one

The system should maintain three distinct libraries.

## A. LENSES

How to understand the target.

Examples: predictive processing, social signaling, interoception, information foraging, control theory.

## B. SONIC MECHANISMS

What music can do to embody the discovered structure.

Examples: delayed update, competing clocks, shaped vacancy, filter reveal, phase attraction, reset without repair.

## C. CONTROL DIMENSIONS

The knobs mechanisms manipulate.

Examples: microtiming, cadence probability, event rate, stereo width, spectral brightness, register, phrase length, voice count.

These layers must not be conflated.

"Microtiming" is not a mechanism. It is a control dimension.

"Predictive processing" is not a mechanism. It is a lens.

"RELIABILITY ACROSS DELAY" is a mechanism because it describes a causal relation the music can enact.

---

# 6. The current specimen atlas

The specimens below are not merely songs about emotions. Each one exists because it contributed new reusable machinery.

## 6.1 Confusion

**Core:** too many almost-right organizations remain live at once. Confusion is overconstrained rather than random.

**Primary architecture:** metastable multi-model state; several candidate parses remain above threshold; prediction errors do not permit clean model selection.

**Key mechanisms discovered:**

- DUAL LEGALITY;
- BLOCKED UPDATE;
- FALSE FLUENCY;
- MODEL SUCCESSION;
- FIGURE / GROUND EXCHANGE;
- MIGRATING INVARIANT;
- ALMOST-LOCK;
- WRONGLY LEGAL RESOLUTION;
- ANSWER AS ABSENCE;
- CONFIDENCE MIGRATION;
- SLIDING-WINDOW MEMORY;
- OVERWRITE;
- CAPACITY OVERFLOW;
- COMPETING CLOCKS;
- FALSE DOWNBEAT ADVERTISEMENT;
- TURN-TAKING FAILURE;
- ACCIDENTAL CONSENSUS;
- POLITE INTERRUPTION;
- LOCAL COHERENCE / GLOBAL FAILURE;
- TEMPORAL STICKINESS;
- RESOLUTION THEFT;
- LAGGED ADAPTATION;
- THRESHOLD REASSIGNMENT;
- RESIDUAL PARSE;
- PARTIAL SUCCESS;
- TERMINAL METASTABILITY.

**Important distinction:** confusion does not require chaos. It requires multiple coherent interpretations that cannot cleanly settle.

## 6.2 Jealousy

**Core:** monitoring and comparison around a valued object under rival salience.

**Primary architecture:** object remains desired; rival becomes salient; self tracks both; ambiguous cues receive threat-biased weighting; clinging and comparison coexist.

**Key mechanisms:**

- CONTESTED OWNERSHIP;
- NEAR-COPY RIVALRY;
- STOLEN COMPLETION;
- STATUS AS TIMING;
- MONITORING LAYER;
- FALSE-ALARM RETENTION;
- RUMINATION COMPRESSION;
- INFERENCE CONTAMINATION;
- CLINGING INVARIANT;
- AUTHORITY MIGRATION;
- OVERCOMPENSATION;
- ABSENCE AS EVIDENCE;
- AMBIGUOUS-CUE CAPTURE;
- PROXIMITY CONFLICT;
- ACCIDENTAL UNISON AS CRISIS;
- PUBLIC SYSTEM / PRIVATE SUBSYSTEM;
- ORIENT -> SCAN -> INTERCEPT;
- FAKE RETURN TO NORMAL;
- DESIRE WITHOUT TRUST;
- LOCAL SUCCESS / RELATIONAL FAILURE.

## 6.3 Infatuation

**Core:** wanting system plus an under-specified person-model that overpredicts reward.

**Primary architecture:** sparse cue becomes disproportionately salient; low-resolution model fills missing detail positively; future collapses toward next contact.

**Key mechanisms:**

- CUE OVERVALUATION;
- ARRANGEMENT-RANK INFLATION;
- LOW-RESOLUTION MODEL;
- POSITIVE FILL-IN;
- ATTENTIONAL ORBIT;
- BANDWIDTH THEFT;
- ABORTED SIDE-GOAL;
- SCARCE REPLY;
- PICKUP DOMINANCE;
- TEMPORAL HORIZON COLLAPSE;
- IMMEDIATE RE-ANTICIPATION;
- WANTING WITHOUT CONSUMMATION;
- APPROACH MICROTIMING;
- VALUE CERTAINTY / ACCESS UNCERTAINTY;
- SEARCH-FILLED ABSENCE;
- MODEL / WORLD SEPARATION;
- REWARD OVERSHOOT;
- SALIENCE NARROWING;
- COMPRESSION BEAUTIFICATION;
- CODEC LOCK;
- FORCED QUANTIZATION;
- UPDATE RESISTANCE;
- RAW RESIDUE;
- FUTURE-BIASED FORM;
- CONTACT DOWNBEAT;
- HYPERMETRIC RESET;
- INFLATION WITHOUT COMPLEXIFICATION.

## 6.4 Lust

**Core:** a contact-seeking excitation system with interoceptive gain, motor entrainment, and an inhibition rail.

**Primary architecture:** body clock tries to lock; proximity changes coupling; language loses priority as bodily timing gains authority.

**Key mechanisms:**

- GAIN CONTROL;
- EXCITATION / INHIBITION JURISDICTIONS;
- BRAKE THE SAME CUE THAT ACCELERATES;
- IRREGULAR PERMISSION;
- UNDERLYING PERIOD / MISSING EXPRESSION;
- CONTACT PERIOD;
- COUPLING BY PROXIMITY;
- DISTANCE AS CONTROL VARIABLE;
- SPATIAL COLLAPSE;
- SURFACE DENSITY WITHOUT TEMPO CHANGE;
- WEIGHT / SURFACE SPLIT;
- INTEROCEPTIVE CLOCKS;
- BODY-FIRST / LANGUAGE-LAG;
- SYLLABIC DISSOLUTION;
- FEATURE FIXATION;
- PROXIMAL SALIENCE;
- DELAY AS FRICTION;
- THRESHOLD PRESSURE;
- LOCK AS CLIMAX;
- MULTI-PARAMETER COINCIDENCE;
- PLATEAUED ESCALATION;
- REFRACTORY DROP;
- RELOAD;
- AFTERPULSE;
- HYSTERETIC AROUSAL;
- BASELINE GHOST;
- ATTRACTOR REPLACEMENT;
- OVERSIZED INTERNAL UPDATE;
- EXTERNAL CUE / INTERNAL CONSEQUENCE SPLIT;
- PERIOD PRESERVATION UNDER MUTATION;
- STATIC HARMONY / DYNAMIC PHYSIOLOGY;
- PROXIMITY FILTERING;
- MASKING AS PRIORITY;
- COUPLING WITHOUT CONVERSATION.

## 6.5 Merry's Morning Horror - protected personal protocol

**Core:** boot, weight, again, proceed.

The horror is administrative. No monster is required. The self is initialized into a usable body and a day that is already waiting.

This stays a named personal protocol rather than being dissolved into the general mechanism library.

**Sacred rules:**

- the day is competent;
- the self arrives after the conditions;
- the boot-cell returns;
- the day starts before consent;
- brightness is hostile through banality;
- body = inventory, not spectacle-horror;
- function without reward;
- no antagonist;
- second boot is the thesis;
- no poetic escape hatch.

**Private operators:**

- BOOT BEFORE CONSENT;
- LATE ENROLLMENT;
- MEAT REPORT;
- ADMINISTRATIVE BRIGHTNESS;
- COMPETENT NONREWARD;
- RECTANGULAR TIME;
- CALENDAR CADENCE;
- MOTOR OBLIGATION;
- WRONG BOOT ORDER;
- WORLD ALREADY ON;
- BODY AS PRECONDITION;
- USABLE PERSON;
- COMPILER STUB;
- ONE ADMINISTRATIVE DIFFERENCE;
- NO ANTAGONIST;
- SECOND MORNING.

**Canonical sentence:** *You are not being chased. You are being initialized.*

The general library may borrow mechanisms from this protocol, but the protocol itself remains intact.

## 6.6 Boredom

**Core:** unused attention plus a clock that will not teach you anything.

**Primary architecture:** available sampling capacity exceeds meaningful information supply. Prediction is cheap and correct; time becomes explicit; restless motor activity may increase while useful content does not.

**Key mechanisms:**

- PREDICTION SATURATION;
- INFORMATION STARVATION;
- EXPLICIT CLOCK;
- TIME EXPOSURE;
- HYPERMETRIC DILATION;
- CONTINUATION WITHOUT ACCUMULATION;
- UNPAID REPETITION;
- FAILED ENGAGEMENT;
- ABORTED START;
- CHANNEL CHANGE / INFORMATION STASIS;
- NOVELTY COSMETICS;
- FIDGET COMPENSATION;
- OFFICIAL / ILLEGAL ACTIVITY SPLIT;
- ATTENTION WITHOUT OBJECT;
- APPETITE WITHOUT AFFORDANCE;
- MOTOR ON / CONTENT OFF;
- SHALLOW AFFORDANCE;
- EXACTLY ADVERTISED RESOLUTION;
- FAILED ALMOST-EVENT;
- CLOCK REVEAL;
- UNDERFILLED FORM;
- EMPTY HOLE;
- COMPETENCE WITHOUT APPLICATION;
- SOURCE-BITRATE MISMATCH;
- HEADER WITHOUT PAYLOAD;
- PACKET STARVATION;
- RETRY WITHOUT UPDATE;
- TERMINAL CONTINUATION.

## 6.7 Curiosity

**Core:** a closable information gap with a direction.

**Primary architecture:** model is good enough to ask a question but not answer it; partial answers create further specific gaps; uncertainty is valuable while it remains tractable.

**Key mechanisms:**

- POINTED GAP;
- CLOSABLE UNCERTAINTY;
- QUESTION VECTOR;
- AIMED ABSENCE;
- QUESTION BEFORE ANSWER;
- LATE-LEGAL ANSWER;
- PARTIAL UPDATE;
- ONE-AXIS REVEAL;
- LOOT;
- LOOT-TO-QUESTION;
- RECURSIVE GAP CREATION;
- INVENTORY GROWTH;
- OPTIMAL NOVELTY BAND;
- TRACKABLE MUTATION;
- SEEKER TIMING;
- SEATED BAR;
- PROBE / COMMIT / LEAVE;
- SEARCH POLICY;
- BOREDOM REJECT;
- INFORMATION FORAGING;
- FIXATION WINDOW;
- WRONG-DOOR ANSWER;
- ANSWER TOO SMALL;
- DISCOVERY AS STATE CHANGE;
- MOVING OCCLUSION;
- OCCLUDE EXACTLY ONE THING;
- REVEAL BY UNFILTERING;
- SPATIAL QUESTION;
- DISCOVERED RULE;
- MAP WITH ONE UNKNOWN REGION;
- QUESTION-CELL MIGRATION;
- QUESTION RESOLUTION SHRINKING;
- RECURSIVE ZOOM;
- RESOLUTION DEMAND ESCALATION;
- STRUCTURAL ZOOM;
- PROMISING ERROR;
- VALUED NON-CLOSURE;
- TERMINAL STILL-ASKING.

**Canonical sentence:** *Curiosity is a question with a vector.*

## 6.8 Trust

**Core:** released monitoring plus a prediction that still shows up.

**Primary architecture:** leave a function unfilled because another agent is predicted to occupy it; monitoring remains absent across delay; rupture can be repaired by restored function rather than spectacle.

**Key mechanisms:**

- DELEGATED TIMING;
- ACCEPTED VULNERABILITY;
- SHAPED VACANCY;
- CONTRACT COORDINATE;
- RELEASED MONITORING;
- ABSENCE OF INSURANCE;
- ACTION BEFORE CONFIRMATION;
- NORMALIZED RELIABILITY;
- RELIABILITY ACROSS DELAY;
- DELAY WITHOUT THREAT ESCALATION;
- AMBIGUITY LEFT ORDINARY;
- INTERLOCKED INCOMPLETENESS;
- COMPOSITE FUNCTION;
- VARIATION WITH APPOINTMENT STABILITY;
- NO COMPENSATION;
- HOLE TOLERANCE;
- BREATH ACROSS UNCERTAINTY;
- SINGLE RE-ASK;
- HELD VACANCY AFTER FAILURE;
- RUPTURE WITHOUT RECLASSIFICATION;
- REPAIR BY RESTORED FUNCTION;
- REPAIR ON ORIGINAL TERMS;
- POST-REPAIR INSURANCE REDUCTION;
- NON-GRIPPING CONTINUATION;
- DISTINCT-BUT-COUPLED AGENTS;
- ANTI-FUSION;
- SHARED GRID / SEPARATE JURISDICTIONS;
- PHASE REJOIN;
- FAILURE BECOMES NONFUNCTION, NOT EMOTION;
- DISTRIBUTED PLAYABILITY;
- TRUST AS SUBTRACTION.

**Major lesson:** some concepts are best sonified by deleting control machinery rather than adding expressive material.

## 6.9 Embarrassment

**Core:** a public flub plus a rewind that will not run.

**Primary architecture:** a specific output becomes visible and irreversible; the self becomes an object; the social world may already have moved on while internal replay remains loud.

**Key mechanisms:**

- PRINTED ERROR;
- QUOTABLE FAILURE;
- SELF-AS-OBJECT SWITCH;
- SPOTLIGHT GAIN;
- PUBLIC / PRIVATE MIX SPLIT;
- IMAGINED FREEZE / ACTUAL CONTINUATION;
- IRREVERSIBLE AIR;
- REWIND DESIRE / FORWARD LAW;
- FAILED UNDO;
- MEMORY-EQ;
- RESIDUAL OVERPRESENCE;
- SOCIAL UNDERREACTION;
- REPAIR MOTOR;
- MINIMIZED REDO;
- GAZE DODGE;
- APPROACH / AVERSION SPLIT;
- LANGUAGE COLLAPSE AFTER EXPOSURE;
- BODY HIJACK;
- INTEROCEPTIVE BILLBOARD;
- EDITORIAL CONTROL LOSS;
- PUBLIC SAMPLE;
- BIT-IDENTICAL MEMORY;
- REPLAY FROM OTHER-EAR POSITION;
- HOLE SHAPED BY THE ERROR;
- FAILED MASKING;
- ROOM REFUSES THE CRISIS;
- REJOIN SMALLER;
- SPIKE + TAIL;
- LOCAL CATASTROPHE / GLOBAL NORMALITY;
- ERROR WITHOUT IDENTITY COLLAPSE.

## 6.10 Suspicion

**Core:** one official story plus a residue that will not sign off.

**Primary architecture:** benign explanation remains viable; anomaly repeats; monitoring applies asymmetric weighting; the file remains unsigned.

**Key mechanisms:**

- OFFICIAL MODEL + RESIDUAL;
- UNSIGNED SETTLEMENT;
- DUAL-PARSE WITH ASYMMETRIC WEIGHTING;
- THREAT-BIASED PARSE;
- STABLE TELL-POCKET;
- FREQUENCY AS EVIDENCE;
- SIGNATURE MISMATCH;
- SECOND-PASS LISTENING;
- REWEIGHT WITHOUT NEW EVIDENCE;
- FUNCTIONAL REINTERPRETATION;
- PRIVATE AUDIT BUS;
- MONITOR ONLY THE SUSPECTED SLOT;
- WITHHELD STAMP;
- TRAP-SHAPED VACANCY;
- ACTIVE PROBE;
- PROBE / COMPENSATION TEST;
- OVER-ADAPTATION AS EVIDENCE;
- SMOOTHNESS PENALTY;
- MODEL OVERFIT AS CUE;
- RESIDUAL ENERGY;
- RESIDUAL FAILURE TO SHRINK;
- COVER EXPANSION;
- ASSIMILATION FAILURE;
- WAITING AS ACTION;
- DELAYED REPLY AS TEST;
- INNOCENT PARSE PRESERVATION;
- NO VERDICT CONDITION;
- PLAUSIBLE SURFACE REQUIREMENT;
- UNDERCOVER ANOMALY;
- REMAINDER BUS.

## 6.11 Silly

**Core:** the rule breaks and nobody has to pay.

**Primary architecture:** competent plan remains intact; a parseable low-stakes violation occurs; a play-frame marks the error as non-collecting; system resets without repair.

**Key mechanisms:**

- PLAY FRAME;
- SAFE VIOLATION;
- NON-COLLECTING ERROR;
- FRAME MARKER;
- REVERSIBLE DEVIATION;
- SERIOUS FLOOR / PLAYFUL SURPLUS;
- SURPLUS MOTION;
- UNNECESSARY COMPLEXITY;
- WRONG-JOB OBJECT;
- FUNCTION MISASSIGNMENT;
- ONE-AXIS WRONGNESS;
- CHEAP PREDICTION ERROR;
- DIGNITY DROP;
- PRATFALL TIMING;
- PROOF-OF-SAFETY SILENCE;
- UNPUNISHED RETURN;
- RESET WITHOUT REPAIR;
- GIDDY ESCALATION;
- SURPLUS ESCALATION;
- THREAT-INVARIANT ESCALATION;
- PLAY-LICENSE PERSISTENCE;
- COMPETENCE UNDERNEATH;
- TASK SURVIVAL;
- OVERQUALIFIED RESPONSE;
- RANK MISMATCH;
- CEREMONIAL OVERREACTION;
- SMALL EVENT / LARGE MACHINE;
- LOW-STAKES CATEGORY ERROR;
- TOY REASSIGNMENT;
- HOT-POTATO RESPONSIBILITY;
- TEMPORARY OWNERSHIP;
- LATE PASS FLOP;
- SOCIAL PLAY RELAY;
- INCONGRUITY WITHOUT ONTOLOGY CHANGE;
- NO LESSON REQUIRED;
- TERMINAL PLAYABILITY.

## 6.12 Flirty

**Core:** a bid you can deny plus a hole left for the other person to take.

**Primary architecture:** dual-readable approach signal; specific target; optional uptake; cheap retreat; escalation only after reciprocal response.

**Key mechanisms:**

- DUAL-READABLE SIGNAL;
- COVER READING;
- RETRACTABLE BID;
- CHEAP RETREAT;
- INVITATION SLOT;
- TRIAL DELEGATION;
- UPTAKE-GATED ESCALATION;
- NO SOLO INFLATION;
- ONE-INCREMENT RULE;
- GLANCE CYCLE;
- SHOW / WITHDRAW RHYTHM;
- COY PAUSE;
- ADDRESSABLE SIGNAL;
- TARGET BEARING;
- SURPLUS ATTENTION;
- SURPLUS WITH VECTOR;
- PLAY + APPROACH SUPERPOSITION;
- AMBIGUITY AS TOOL;
- OPTION VALUE;
- RESET TO COVER;
- NO-SULK RESET;
- PUBLIC FLOOR / PRIVATE VECTOR;
- LOCK-THEN-LOOSEN;
- TEMPORARY MUTUALITY;
- ALMOST-DECLARATION;
- AMBIGUITY PRESERVATION THRESHOLD;
- TWO-CAPTION OBJECT;
- BIT-SAME / FUNCTION-DIFFERENT;
- CONDITIONAL MIX STATE;
- MICRO-UPTAKE;
- CHANNEL REMAINS OPEN;
- STILL-OPTIONAL ENDING.

## 6.13 Seduction

**Core:** guided narrowing through reciprocal reward.

**Primary architecture:** one agent offers; another independently responds; response authorizes exactly one further degree of access, proximity, dependence, or mutual prediction.

**Key mechanisms:**

- RECIPROCITY-GATED ESCALATION;
- EARNED PARAMETER ACCESS;
- PROGRESSIVE MUTUAL NARROWING;
- INCREASING MUTUAL PREDICTABILITY;
- PHASE ATTRACTION;
- TEMPORARY LOCK / DELIBERATE RELEASE;
- DISCLOSURE GATING;
- INFORMATIONAL UNDRESSING;
- BACKGROUND SURRENDER;
- DEPENDENCY DEVELOPMENT;
- OPTION-SPACE NARROWING;
- PATH REINFORCEMENT;
- NONPUNITIVE ALTERNATIVES;
- PRESERVED EXIT;
- PROGRESSIVE DISCLOSURE;
- RECIPROCAL PATH REINFORCEMENT.

**Canonical sentence:** *Nothing escalates because time passed. It escalates because somebody answered.*

## 6.14 Titillation

**Core:** a small cue, a large reflex, and a threshold that is not allowed to arrive.

**Primary architecture:** surface-scale cue creates disproportionate response; excitation flickers; inhibition rails prevent transition into a sustained stronger regime.

**Key mechanisms:**

- OVERSIZED REFLEX;
- SMALL CUE / LARGE AUTOMATION;
- FLICKER EXCITATION;
- COMB-SHAPED INTENSITY;
- APPROACH / FLINCH PAIR;
- MISSING NEXT HIT;
- THRESHOLD RAIL;
- ALMOST-COUPLING;
- GHOST THRESHOLD;
- YANK-BACK;
- REVERSIBLE AROUSAL;
- NO ACCUMULATION RULE;
- ESCALATION COMPENSATION;
- BIGGER PEEK / BIGGER HIDE;
- SURFACE SALIENCE;
- LOW INFORMATION / HIGH SALIENCE;
- PEEK / HIDE CYCLE;
- SAME-ADDRESS OCCLUSION;
- UNDERDELIVERED REVEAL;
- WANTING > REVEAL;
- TEASE GAP;
- FLOOR RECOVERY;
- OFFICIAL TASK SURVIVES;
- STATE CONTAINMENT;
- BORROWED FUTURE STATE;
- RATIO-GOVERNED CONTROL;
- FORCED BRAKE EVENT;
- EXCHANGE-RATE ESCALATION;
- STIMULUS IDENTITY PRESERVATION;
- OBJECT MUST NOT GROW;
- MOTOR LEAK;
- TERMINAL NON-ARRIVAL.

**Canonical phrase:** *a threshold that remains a rumor.*

## 6.15 Reaction GIF specimen 001 - Frozen Output / Moving Search

The first GIF test immediately proved that motion analysis can reveal mechanisms not captured by emotion words.

**Observed behavioral structure:**

- clip begins after reaction onset;
- eyes and mouth remain held open;
- no blink, no mouth close, no speech;
- head and torso continue yaw/pitch movement;
- gaze never visibly settles;
- loop seam returns geometrically close to the beginning;
- recovery is absent;
- image substrate drifts independently.

**Primary causal model:** a high-arousal intake/display aperture has locked while the orienting system continues to move. The face has effectively posted a conclusion while the body continues searching for a vantage that might finish the update.

**Mechanisms:**

- APERTURE LOCK;
- ORIENTING ORBIT;
- RESET WITHOUT REPAIR;
- DENIED PHONEME;
- DESYNCHRONIZED CLOCKS;
- ZERO-GAIN REPEAT;
- POST-COMMITMENT ENTRY;
- CARRY, DON'T FLINCH;
- SUBSTRATE MISLOCK;
- ANGLE-AS-VARIATION;
- DISPLAY / ORIENTATION SPLIT;
- HELD CONCLUSION / ACTIVE SEARCH;
- GEOMETRIC RESET;
- IDENTITY SEAM;
- NO-RECOVERY LOOP.

**Compound pattern worth preserving:**

### FROZEN OUTPUT / MOVING SEARCH

One subsystem exposes a stable conclusion or readiness state while another continues sampling the environment as though settlement has not occurred.

**Major meta-discovery:** development does not have to mean changing the object. It can mean changing the observer's relation to the object.

---

# 7. Mechanism families currently emerging

The library is now large enough that organization matters more than simply naming more things.

## Prediction / expectation

BLOCKED UPDATE; FALSE FLUENCY; WRONGLY LEGAL RESOLUTION; FALSE DOWNBEAT ADVERTISEMENT; LATE-LEGAL ANSWER; EXACTLY ADVERTISED RESOLUTION; GHOST THRESHOLD; FAILED ALMOST-EVENT; REWARD OVERSHOOT.

## Attention / salience

FIGURE / GROUND EXCHANGE; MONITORING LAYER; ATTENTIONAL ORBIT; CUE OVERVALUATION; FEATURE FIXATION; PROXIMAL SALIENCE; SPOTLIGHT GAIN; SURFACE SALIENCE; SALIENCE NARROWING; TARGET BEARING.

## Memory / recursion

SLIDING-WINDOW MEMORY; OVERWRITE; RUMINATION COMPRESSION; INFERENCE CONTAMINATION; MEMORY-EQ; BIT-IDENTICAL MEMORY; ZERO-GAIN REPEAT; RETRY WITHOUT UPDATE; RESET WITHOUT REPAIR.

## Representation / model quality

LOW-RESOLUTION MODEL; LOSSY COMPRESSION; CODEC LOCK; POSITIVE FILL-IN; FORCED QUANTIZATION; UPDATE RESISTANCE; MODEL/WORLD SEPARATION; COMPRESSION BEAUTIFICATION; OFFICIAL MODEL + RESIDUAL; RESIDUAL FAILURE TO SHRINK.

## Motivation / reward

CUE OVERVALUATION; SCARCE REPLY; WANTING WITHOUT CONSUMMATION; REWARD OVERSHOOT; BANDWIDTH THEFT; VALUED NON-CLOSURE; APPETITE WITHOUT AFFORDANCE; WANTING > REVEAL.

## Temporal anticipation

PICKUP DOMINANCE; TEMPORAL HORIZON COLLAPSE; CONTACT DOWNBEAT; HYPERMETRIC RESET; FUTURE-BIASED FORM; SEEKER TIMING; LATE ENROLLMENT; RECTANGULAR TIME.

## Embodied control / physiology

GAIN CONTROL; INTEROCEPTIVE CLOCKS; BODY-FIRST; REFRACTORY DROP; AFTERPULSE; HYSTERETIC AROUSAL; BASELINE GHOST; BODY HIJACK; INTEROCEPTIVE BILLBOARD; MEAT REPORT.

## Coupling / proximity

COUPLING BY PROXIMITY; DISTANCE AS CONTROL VARIABLE; SPATIAL COLLAPSE; CONTACT PERIOD; LOCK AS CLIMAX; MULTI-PARAMETER COINCIDENCE; PHASE ATTRACTION; TEMPORARY LOCK / DELIBERATE RELEASE.

## Gating / permission

EXCITATION / INHIBITION; IRREGULAR PERMISSION; UNDERLYING PERIOD / MISSING EXPRESSION; FORCED BRAKE EVENT; THRESHOLD RAIL; DENIED PHONEME; EARNED PARAMETER ACCESS.

## Information supply / demand

INFORMATION STARVATION; SOURCE-BITRATE MISMATCH; PACKET STARVATION; HEADER WITHOUT PAYLOAD; PREDICTION SATURATION; OPTIMAL NOVELTY BAND; INFORMATION FORAGING.

## Exploration / foraging

PROBE / COMMIT / LEAVE; SEARCH POLICY; FIXATION WINDOW; BOREDOM REJECT; SPATIAL QUESTION; RECURSIVE ZOOM; ORIENTING ORBIT.

## Knowledge accumulation

PARTIAL UPDATE; ONE-AXIS REVEAL; LOOT; LOOT-TO-QUESTION; INVENTORY GROWTH; DISCOVERY AS STATE CHANGE; DISCOVERED RULE; RECURSIVE GAP CREATION.

## Delegation / reliability / repair

ACCEPTED VULNERABILITY; CONTRACT COORDINATE; RELEASED MONITORING; ABSENCE OF INSURANCE; RELIABILITY ACROSS DELAY; HELD VACANCY; SINGLE RE-ASK; REPAIR BY RESTORED FUNCTION; PHASE REJOIN; DISTRIBUTED PLAYABILITY.

## Irreversibility / exposure / editorial control

PRINTED ERROR; IRREVERSIBLE AIR; FAILED UNDO; PUBLIC SAMPLE; EDITORIAL CONTROL LOSS; BIT-IDENTICAL MEMORY; FAILED MASKING; POST-COMMITMENT ENTRY.

## Self-observation / public-private split

SELF-AS-OBJECT SWITCH; PUBLIC / PRIVATE MIX SPLIT; INTEROCEPTIVE BILLBOARD; SOCIAL UNDERREACTION; LOCAL CATASTROPHE / GLOBAL NORMALITY; DISPLAY / ORIENTATION SPLIT.

## Belief / settlement

PROVISIONAL MODEL; WITHHELD STAMP; UNSIGNED SETTLEMENT; INNOCENT PARSE PRESERVATION; ASYMMETRIC WEIGHTING; NO VERDICT CONDITION; TERMINAL METASTABILITY.

## Probing / intervention

ACTIVE PROBE; CONTROLLED PERTURBATION; OBSERVE COMPENSATION; OVER-ADAPTATION; RESET TO BASELINE; SECOND PROBE; INFERENCE FROM RESPONSE.

## Play / consequence control

PLAY FRAME; SAFE VIOLATION; NON-COLLECTING ERROR; FRAME MARKER; REVERSIBLE DEVIATION; RESET WITHOUT REPAIR; PROOF-OF-SAFETY SILENCE; THREAT-INVARIANT ESCALATION.

## Function / status misuse

WRONG-JOB OBJECT; FUNCTION MISASSIGNMENT; OVERQUALIFIED RESPONSE; RANK MISMATCH; CEREMONIAL OVERREACTION; SMALL EVENT / LARGE MACHINE; TOY REASSIGNMENT.

## Bid / uptake / reciprocity

RETRACTABLE BID; INVITATION SLOT; TRIAL DELEGATION; UPTAKE-GATED ESCALATION; ONE-INCREMENT RULE; MICRO-UPTAKE; RECIPROCITY-GATED ESCALATION; EARNED PARAMETER ACCESS.

## Retractability / option preservation

CHEAP RETREAT; RESET TO COVER; NO-SULK RESET; OPTION VALUE; ALMOST-DECLARATION; AMBIGUITY PRESERVATION THRESHOLD; STILL-OPTIONAL ENDING; PRESERVED EXIT.

## Contextual function switching

DUAL-READABLE SIGNAL; COVER READING; TWO-CAPTION OBJECT; BIT-SAME / FUNCTION-DIFFERENT; FUNCTIONAL REINTERPRETATION; REWEIGHT WITHOUT NEW EVIDENCE.

## Threshold management

THRESHOLD RAIL; GHOST THRESHOLD; ALMOST-COUPLING; YANK-BACK; STATE CONTAINMENT; BORROWED FUTURE STATE; TERMINAL NON-ARRIVAL; ATTRACTOR REPLACEMENT.

## Excitation / reset cycling

FLICKER EXCITATION; COMB-SHAPED INTENSITY; APPROACH / FLINCH; MISSING NEXT HIT; REVERSIBLE AROUSAL; BIGGER PEEK / BIGGER HIDE; RATIO-GOVERNED CONTROL.

## Perspective / viewpoint

ANGLE-AS-VARIATION; SPATIAL QUESTION; REPLAY FROM OTHER-EAR POSITION; TARGET BEARING; MOVING OCCLUSION; ORIENTING ORBIT.

---

# 8. The hole problem: same surface, different causal semantics

One of the most important discoveries is that identical musical gestures can carry very different meanings depending on causal structure.

A silence or empty slot is not one mechanism.

- **Trust hole:** I expect you to fill this.
- **Flirt hole:** you may fill this.
- **Suspicion hole:** I am leaving this to see what you do.
- **Curiosity hole:** something belongs here and I want to discover it.
- **Confusion hole:** I cannot determine what belongs here.
- **Boredom hole:** nothing worthwhile is arriving here.
- **Titillation hole:** absence resets sensitivity so the next tiny cue still hits.
- **Embarrassment hole:** the room feels frozen after the flub even though the social clock continues.

The library therefore cannot classify operators only by musical surface. It must record **why the operation exists**.

This is a central design requirement for future software.

---

# 9. Evidence condition + response policy

Another major discovery is that the same information condition can produce different states depending on the system's response policy.

Example: **zero information gain**.

- boredom: zero gain -> disengage or manufacture fidgets;
- GIF specimen: zero gain -> restart orienting search;
- suspicion: zero gain -> keep targeted monitoring active;
- obsession / rumination candidate: zero gain -> repeat anyway and possibly increase weighting.

This suggests a deeper architecture:

`EVIDENCE CONDITION + RESPONSE POLICY -> STATE DYNAMICS`

Eventually the system should generate new sonifications by locating a target in this mechanism-space instead of requiring a prewritten operator for every emotion word.

---

# 10. Reaction GIF mode

Reaction GIFs are not emotion flashcards. They are tiny behavioral time-series.

They contain information that labels erase:

- onset order;
- reaction latency;
- eye vs head vs torso timing;
- gaze acquisition and release;
- approach / recoil;
- blink timing;
- suppression;
- failed suppression;
- speech preparation;
- abandoned action;
- residual posture;
- return to baseline;
- social checking;
- body-part jurisdiction conflicts;
- loop seam behavior.

The reaction-GIF workflow should therefore begin with observation before interpretation.

## 10.1 Neutral observation

Describe the visible sequence without naming the emotion.

Example:

`neutral -> eyes acquire target -> 300 ms delay -> brows rise -> head retracts -> mouth begins speech -> speech aborts -> gaze leaves target -> residual tension`

Do not invent an unseen stimulus.

## 10.2 Multiple causal readings

Generate 2-4 possible state machines that could have produced the sequence.

The same visible behavior may plausibly be embarrassment, disbelief, contained amusement, suspicion, delayed recognition, or social calibration.

Preserve ambiguity where evidence does not decide.

## 10.3 State-transition extraction

Ask:

`initial state -> perturbation -> internal update -> motor/autonomic response -> inhibition/amplification -> resulting state -> residue/recovery -> loop return`

The main question is not "what emotion is this?"

It is:

> **WHAT CHANGED?**

## 10.4 Actual timing

Estimate relative timing:

- instantaneous;
- brief;
- held;
- delayed;
- repeated;
- slow recovery;
- rapid reset.

The music need not map 1 second of video to 1 second of audio. Preserve timing relationships instead.

## 10.5 The loop seam is data

A reaction GIF artificially repeats a short process. That repetition can change meaning.

The loop may create:

- rumination;
- repeated threshold approach;
- failed reset;
- sensitization;
- habituation;
- comic recurrence;
- geometric orbit;
- identity seam;
- incomplete recovery;
- same event / changed interpretation.

Every GIF run should explicitly state:

- **GIF LOOP:** what the original event does;
- **LOOPED GIF:** what repetition changes;
- **MUSICAL LOOP OPERATOR:** how composition should exploit the seam.

## 10.6 Identity rule

Do not rely on knowing the actor, meme, film, show, or cultural caption during first-pass analysis.

The GIF itself is primary evidence.

The cultural reading can be introduced afterward as weak contextual evidence or as a separate test condition.

This gives us a useful experiment:

1. blind behavioral analysis;
2. labeled cultural analysis;
3. compare the mechanisms that change.

---

# 11. Current high-value meta-laws

## 11.1 Weirdness needs a floor

A system must retain enough legality that the deviation is intelligible.

## 11.2 Do not confuse intensity with speed

BPM, activity pulse, event rate, subdivision density, perceived urgency, and physiological pace are separate dimensions.

## 11.3 Absence is an active control surface

Silence, missing notes, omitted downbeats, filtered bands, absent monitoring, and withheld responses can be more structurally precise than adding another sound.

## 11.4 Resolution is not one operation

Resolution may be:

- blocked;
- late but legal;
- stolen;
- exactly advertised;
- withheld administratively;
- offered to another agent;
- tested;
- denied to preserve optionality;
- shown as a threshold rumor;
- completed without reward.

## 11.5 Development can be perspectival

A fixed object can develop by changing:

- spatial bearing;
- register;
- distance;
- mix weighting;
- observer position;
- interpretation;
- model function.

The object itself need not mutate.

## 11.6 Some states are best represented by subtraction

Trust becomes legible when monitoring and insurance disappear. Boredom can become legible when informational content is removed while the clock remains. Titillation depends on cuts. Silly depends on the absence of punishment.

## 11.7 A mechanism should survive its source concept

If a mechanism only makes sense when its source emotion name is attached, it is probably still a metaphor rather than a reusable operator.

## 11.8 Neighbor states are best separated by causal contrasts

Examples:

- embarrassment = specific exposed event; shame = global self-model contamination;
- guilt = action violation with repairable self; shame = agent reclassification;
- curiosity = useful partial information; boredom = low information yield;
- trust = delegated vacancy; flirt = optional invitation; suspicion = diagnostic trap;
- flirt = reversible bid; seduction = reciprocity-gated narrowing; lust = bodily coupling drive; infatuation = model inflation.

---

# 12. Expansion plan

The next stage should not simply collect more emotion words. It should deliberately fill sparse regions of mechanism-space.

## Phase A - finish the first high-yield concept batch

Already completed from the priority batch:

- boredom;
- curiosity;
- trust.

High-priority remaining targets:

1. **Learning** - real model update, decreasing error, chunking, consolidation, plasticity.
2. **Deja vu** - familiarity without source retrieval; competing memory signals.
3. **A system becoming extremely good at solving the wrong problem** - proxy optimization, local success, global irrelevance.
4. **Feedback delay** - correction arrives after conditions changed; overshoot and oscillation.
5. **Emergence** - local rules create global structure with no central author.
6. **Pluralistic ignorance** - private disagreement plus public conformity driven by higher-order beliefs.
7. **Bureaucracy** - queues, permissions, handoffs, duplicate state, bottlenecks, responsibility diffusion.
8. **Relief** - predicted threat fails to arrive; unused preparation collapses.
9. **Guilt + shame as a contrast pair** - repairable action-error versus global agent contamination.
10. **Unlearning** - old prediction survives while evidence weakens; extinction without erasure.

Additional high-yield targets after that:

- embarrassment / shame / guilt contrasts;
- obsession;
- procrastination;
- learned helplessness;
- flow state;
- expertise;
- overfitting / underfitting;
- hysteresis;
- phase transition;
- metastability;
- synchronization / desynchronization;
- homeostasis / allostasis;
- fatigue;
- adaptation;
- boundary maintenance / boundary failure;
- diffusion;
- crystallization;
- turbulence;
- resonance;
- scarcity / abundance;
- cooperation;
- reciprocity;
- conformity;
- self-fulfilling prophecy;
- rumor;
- secret becoming impossible to keep;
- institutional inertia;
- coordination failure;
- tragedy of the commons;
- queue becoming crowd;
- semantic drift;
- category encountering an impossible member;
- ambiguity where nobody is confused;
- uncertainty that feels good;
- certainty when wrong;
- system observing itself.

## Phase B - reaction GIF atlas

Collect behaviorally diverse clips, not merely many versions of the same facial emotion.

Priority GIF types:

1. trying not to laugh -> failing;
2. slow double-take;
3. smile disappearing in real time;
4. fake/polite smile held too long;
5. side-eye without head turn;
6. head turns first, face updates later;
7. face reacts first, body freezes afterward;
8. lean in -> recoil;
9. start to speak -> stop;
10. start to leave -> turn back;
11. look around to see whether anyone else noticed;
12. look at another person before deciding how to react;
13. nervous laugh after something goes wrong;
14. composure maintained while panic leaks underneath;
15. instant delight deliberately suppressed;
16. recognition slowly dawning;
17. sudden realization followed by stillness;
18. disbelief stare followed by checking again;
19. repeated blink / reinspection;
20. squint -> inspect -> unsquint;
21. full-body cringe compression;
22. disgust followed by physical push-away;
23. flinch followed by rapid "fine" recovery;
24. startle with long residual stare;
25. increasing impatience while nothing changes;
26. waiting expectantly then giving up;
27. excited anticipation -> disappointment -> mask;
28. confident nod becoming uncertainty;
29. uncertainty becoming confidence;
30. two people silently realizing the same thing;
31. one person laughs, another catches it;
32. two people both waiting for the other to act;
33. unconscious mirroring;
34. same failed action repeated;
35. strategy changes after repeated failure;
36. tiny annoyance accumulating into fury;
37. huge response to tiny stimulus;
38. expected huge reaction that never arrives;
39. strong reaction rapidly habituating on repeats;
40. identical stimulus causing stronger reaction each time;
41. pretending not to notice something obvious;
42. desperately trying to look busy;
43. confidently doing the wrong thing;
44. realizing mid-action that it is wrong but finishing anyway;
45. mid-action error detection followed by reversal;
46. almost-hug / handshake protocol collision;
47. repeated failed high-five or handshake;
48. perfectly synchronized reaction between two people;
49. one person reacts while everyone else stays normal;
50. everyone reacts except one person who has not noticed yet.

## Phase C - normalize the mechanism library

After a sufficient batch:

- compare mechanisms by causal graph, not name;
- merge synonyms;
- distinguish mechanism from control dimension;
- distinguish mechanism from lens;
- mark NEW / VARIANT / DUPLICATE / COMPOUND;
- record source specimens;
- identify mechanism families that are crowded;
- identify sparse regions;
- choose future targets specifically to fill those holes.

The research process should eventually **eat its own map**: the current taxonomy chooses the next experiments.

## Phase D - saturation criterion

Stop mining a conceptual region when new targets mostly return variants of existing mechanisms.

Move to a different causal architecture when novelty yield falls.

Do not confuse a new emotional noun with a new mechanism.

---

# 13. Future software architecture

This system should eventually become machine-readable rather than living only as prose.

Suggested records:

```ts
interface SonificationSpecimen {
  id: string;
  title: string;
  sourceType: 'concept' | 'gif' | 'video' | 'personal_protocol' | 'system';
  sourceDescription: string;
  observations?: string[];
  candidateModels: CausalModel[];
  selectedModelId: string;
  lensIds: string[];
  properties: StructuralProperty[];
  transductions: TransductionRule[];
  controlDimensions: string[];
  temporalArc: string[];
  invariant: string;
  operators: string[];
  alternates: AlternateSonification[];
  harvestedMechanismIds: string[];
  antiCliches: string[];
  notes?: string[];
}

interface SonificationMechanism {
  id: string;
  name: string;
  causalStructure: string;
  musicalOperations: string[];
  controlDimensions: string[];
  distinguishesFrom: string[];
  reuseDomains: string[];
  sourceSpecimenIds: string[];
  status: 'NEW' | 'VARIANT' | 'DUPLICATE' | 'COMPOUND';
}

interface SonificationLens {
  id: string;
  name: string;
  question: string;
  usefulFor: string[];
}

interface ControlDimension {
  id: string;
  name: string;
  description: string;
  unitOrRange?: string;
}
```

Important: the data model must preserve causal semantics.

Do not reduce the library to:

`hole -> silence`

Instead preserve:

`trust / contract-coordinate / delegated vacancy -> counted silence`

versus:

`suspicion / active-probe / trap-shaped vacancy -> counted silence`.

The same musical control may serve many mechanisms, and that relationship is part of the intelligence.

---

# 14. Suggested future interface

A future Behavioral Sonification Lab inside Lil Guys or a dedicated tool could expose:

**INPUT**

- concept / phrase;
- image/GIF/video upload;
- optional cultural label;
- optional user note;
- optional lens picks.

**ANALYSIS**

- observed sequence;
- candidate causal models;
- selected model;
- properties;
- transduction map;
- invariant;
- alternate models.

**MECHANISM MINER**

- proposed mechanisms;
- duplicates found;
- new mechanisms;
- related specimens;
- family placement.

**SONIFICATION COMPILER**

- full technical spec;
- compact Suno style prompt;
- lyric/control prompt when desired;
- instrumental-only mode;
- variant based on a different causal model.

**USER FEEDBACK**

- star a mechanism;
- star a specimen;
- mark "this actually sounded like it";
- mark "cool but wrong";
- explain what worked;
- preserve successful accidents as new specimens.

The feedback should learn causal preferences rather than simply learning favorite genres.

---

# 15. What success looks like

A successful run should pass these tests:

1. If the emotion/concept word is removed, the musical system still behaves like the target.
2. The explanation can state which variable changed and why.
3. At least one mechanism could be reused for a different target.
4. The result does not depend on genre costume.
5. The invariant survives enough transformation to make the state recognizable.
6. Neighboring states can be distinguished causally.
7. The alternate sonifications are structurally different, not style variants.
8. The mechanism harvest does not rename duplicates for novelty.
9. The temporal arc is part of the model, not an afterthought.
10. For GIFs, the loop seam is explicitly analyzed.

The project has succeeded when it can take an input like:

- "trust";
- "a system solving the wrong problem";
- a 2.6-second reaction GIF;
- "the moment you realize you forgot something";
- "a queue becoming a crowd";

and return not a mood board, but a small causal machine that music can actually run.

---

# 16. Compact project definition

**Behavioral Sonification Lab** is an AI SLOP research system that turns concepts, emotions, cognitive states, bodily states, social interactions, system failures, and reaction GIFs into reusable musical mechanisms.

It does this by modeling the target as a set of interacting processes, selecting useful scientific or conceptual lenses, translating structural properties into explicit musical control relations, preserving an invariant, generating alternate causal sonifications, and harvesting the resulting operators into a deduplicated mechanism library.

The goal is not to make music that *sounds stereotypically like* an emotion.

The goal is to make music that **behaves like the thing behaves**.

---

# Appendix A - Current concept-mining protocol

Use this when the input is a named state, process, system, concept, or interaction.

1. Refuse genre-first interpretation.
2. State that there is no scientifically unique soundtrack.
3. Generate 2-4 plausible causal models.
4. Select only useful lenses; do not force every lens.
5. Extract relevant structural variables.
6. Use `PROPERTY -> SONIC VARIABLE -> MUSICAL CONSEQUENCE` mappings.
7. Specify musical controls only where justified.
8. Model the target through time.
9. Find an invariant.
10. Create 5-12 operators.
11. Run an anti-cliche test.
12. Produce a compact music-generator prompt.
13. Produce at least two alternate sonifications from different causal models when supported.
14. Harvest reusable mechanisms after the sonification.
15. Compare them against the existing library and mark NEW / VARIANT / DUPLICATE / COMPOUND.

The output should prioritize mechanisms over adjectives and causal behavior over genre branding.

---

# Appendix B - Reaction GIF mining protocol

Treat the GIF as behavioral time-series data, not an emotion label.

Analyze:

- onset timing;
- orientation;
- gaze;
- facial tension;
- posture;
- head / hand / torso movement;
- approach / recoil;
- freeze;
- double-take;
- delayed reaction;
- suppression / failed suppression;
- escalation / de-escalation;
- recovery;
- residual expression;
- social checking;
- self-monitoring;
- motor preparation;
- aborted action;
- repetition;
- latency;
- asynchronous body systems;
- loop seam.

Then:

1. **Observe before interpreting.** Describe the visible sequence in neutral operational language.
2. **Generate 2-4 causal readings.** Do not collapse ambiguity prematurely.
3. **Identify the smallest state transition.** Ask what changed.
4. **Find control variables.** Attention, arousal, confidence, inhibition, distance, speech readiness, etc.
5. **Transduce, do not soundtrack.** Use explicit control mappings.
6. **Preserve actual timing relationships.** Trigger/reaction/recovery ratios matter.
7. **Find the invariant.** What survives the loop?
8. **Analyze the loop seam.** State what repetition changes.
9. **Build the sonification.** Full spec, temporal arc, operators, anti-cliche test.
10. **Harvest mechanisms.** Generalize away from the GIF.

Do not identify the person or rely on the meme title during the blind pass.

---

# Appendix C - Next ten concept probes

1. Learning
2. Deja vu
3. A system becoming extremely good at solving the wrong problem
4. Feedback delay
5. Emergence
6. Pluralistic ignorance
7. Bureaucracy
8. Relief
9. Guilt + shame as a contrast pair
10. Unlearning

These are chosen for mechanism coverage, not thematic similarity.

---

# Appendix D - One-line north stars

- **Confusion:** too many almost-right organizations at once.
- **Jealousy:** a valued object plus rival salience plus monitoring.
- **Infatuation:** a small person-model inflated into a future.
- **Lust:** a body clock trying to lock.
- **Merry's Morning Horror:** boot, weight, again, proceed.
- **Boredom:** unused attention plus a clock that will not teach you anything.
- **Curiosity:** a question with a vector.
- **Trust:** released monitoring plus a prediction that still shows up.
- **Embarrassment:** a public flub plus a rewind that will not run.
- **Suspicion:** one official story plus a residue that will not sign off.
- **Silly:** the rule breaks and nobody has to pay.
- **Flirty:** a bid you can deny plus a hole left for the other person to take.
- **Seduction:** nothing escalates because time passed; it escalates because somebody answered.
- **Titillation:** a threshold that remains a rumor.
- **Reaction GIF 001:** face concludes; body keeps looking.
