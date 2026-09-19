# AI SLOP Topic 01 — Mechanistic Interpretability & Activation Steering

> Source: `originals/copilot-intake-2026-09-19/CFNetworkDownload_Ogf9rb.pdf`
> Transcription note: Complete text extracted with `pdftotext`; spacing and pagination artifacts preserved for searchability.

AI SLOP — RESEARCH HARVEST | TOPIC 01

Mechanistic Interpretability
& Activation Steering
Internal intervention mechanisms as artistic instruments of structured instability

Compiled: 2026-09-19 | For: merrypranxter/ai_slop (research-only; repository untouched)
Status labels follow the project's canonical epistemic scheme.

This document is self-contained. All sources are clickable in the bibliography and provenance appendix.

AI SLOP Research Harvest — Topic 01: Mechanistic Interpretability & Activation Steering

Contents
1 Executive summary
2 Technical background
3 Mechanism catalog (M1–M10)
4 Failure surfaces as artistic material
5 Promising experiments (E1–E4)
6 Cross-modal applications
7 What appears most useful for AI SLOP
8 Weak / dubious ideas worth rejecting
9 Open questions
10 Sources / bibliography
11 Licensing / provenance appendix

Page 2

AI SLOP Research Harvest — Topic 01: Mechanistic Interpretability & Activation Steering

1 Executive summary
Mechanistic interpretability and activation steering are the only mechanisms in the AI SLOP research
program that literally write into a model's hidden state. Everything else in the project — prompts,
Temporary Minds, constraint governance, Suno lyric-jurisdiction tricks — operates on the input or on
an external controller. Steering vectors, feature clamping, and activation patching operate on the
residual stream itself, at a chosen layer, with a chosen magnitude, in real time. For a project whose core
question is 'what problem can we give a generative system such that its attempt to solve it becomes the
artwork', this is the sharpest available instrument for manufacturing representational conflict with
measurable dose.
The strongest verified findings: (a) contrastive steering vectors work as advertised on open models and
their effects scale roughly monotonically with a coefficient before collapsing into incoherence — that
cliff is itself an artistic failure surface[3]; (b) sparse-autoencoder feature clamping produces coherent
concept-takeover behavior (Golden Gate Claude being the canonical demonstration) and open SAE
suites (Gemma Scope) plus the Neuronpedia platform make this reproducible by anyone with a
consumer GPU[6][8]; (c) the field's own benchmark, AxBench, is a discipline check — simple
prompting beat SAE steering for concept injection, and a 2026 partial rebuttal recovered SAE
performance only with careful per-feature feature selection and strength tuning[10][11]. Steering is
controlled damage, and damage is precisely the material this project studies.
Highest-value project connection: steering interventions are the most literal candidate for a
DAVID-operator analogue at the model-internal level — an operator with named variables (layer,
direction, coefficient schedule, token span) that preserves most of the model's competence while
injecting a single persistent foreign pressure. Combined with the project's external state-controller rule
(a controller that modulates the coefficient over generation time), it yields PROCEDURAL persistent
instability with a real internal anchor — something no prompt-only method can claim honestly.
Honesty constraints honored throughout: no claim that prompting touches activations (it does not,
unless hooks are attached); no claim of access to proprietary internals (all mechanisms here are
demonstrated on open-weight models); feature labels are hypotheses until causally validated; nothing
here is a safety-bypass technique, and refusal-direction manipulation is documented but deliberately
excluded from the experiment set.

2 Technical background
A transformer language model carries a residual stream: a vector per token position that is read from
and added to by every attention head and MLP block across layers. Mechanistic interpretability
reverse-engineers what those vectors encode; activation steering writes into them at inference time. The
shared formal core of nearly all steering methods is a single line: x' = x + α·v, where v is a direction in
activation space (a 'steering vector') and α is a coefficient. Methods differ in how v is obtained: mean
difference of activations over contrast-pair prompts (CAA[3], DiffMean), PCA of those differences
(RepE/LAT[4]), trained probes per attention head (ITI[5]), decoder columns of a sparse autoencoder
(SAE feature steering[6]), or trained low-rank interventions (ReFT[10]).
Sparse autoencoders deserve separate note. An SAE decomposes a residual-stream activation into a
sparse weighted sum of learned feature directions; because the features are far more numerous than
model dimensions and sparsely active, many of them are individually interpretable (a feature that fires

Page 3

AI SLOP Research Harvest — Topic 01: Mechanistic Interpretability & Activation Steering

on the Golden Gate Bridge, on code errors, on sycophantic praise). Clamping one feature to a high
value and reconstructing gives a surgical, if leaky, concept injection[6][7]. Google DeepMind's Gemma
Scope provides open SAEs for every layer of Gemma 2 2B/9B, and Gemma Scope 2 extends this to
Gemma 3 with transcoders[8][9]; Neuronpedia hosts these with interactive steering demos.
Verified tooling stack (all confirmed live as of 2026-09-19):
Tool

What it does

Status / license

Source

TransformerLen
s

Hook-based access/edit of any internal
activation across 140+ architecture families;
the standard workbench

Active (pushed 2026);
MIT

github.com/TransformerLensO
rg/TransformerLens

SAELens

Training and analysis of SAEs; v6 line adds
JumpReLU, Matryoshka, Matching Pursuit
variants

Very active (1.5k+
stars, pushed
2026-09-18); MIT

github.com/decoderesearch/SA
ELens

pyvene

Config-based interventions on any PyTorch
model; static or trainable; serializable
intervention objects shareable via HF

Active; Apache-2.0

github.com/stanfordnlp/pyvene

nnsight / NDIF

Deferred-execution intervention tracing;
remote=True runs interventions on hosted
models up to 405B+ without a local GPU

Active (v0.6, 2026);
MIT

github.com/ndif-team/nnsight

Neuronpedia

Web platform: feature dashboards, search,
interactive steering on hosted SAEs (Gemma
Scope 1/2, Llama, Qwen releases)

Active; open source

neuronpedia.org

Gemma Scope

Open JumpReLU SAE suites for Gemma 2
(all layers/sublayers) and Gemma 3 (Scope
2)

Active; weights on HF
(check per-repo terms)

huggingface.co/google/gemma
-scope

Table 1 — Verified core tooling. Star counts and push dates checked via the GitHub API on 2026-09-19.

Starter-lead verification notes: rattlesnakey/Awesome-Actionable-MI-Survey is real, current
(updated 2026-03), and unusually well-organized (Locate/Steer/Improve taxonomy tagging every paper
by interpretable object and steering method)[15]. kmeng01/rome is real but functionally frozen (last
push
2024-04;
the
field
moved
to
MEMIT
and
to
EasyEdit-style
suites).
koayon/awesome-sparse-autoencoders is small (33 stars) and stale (2025-01); the Dakingrai list is
stale (2024-11). The yuzhaouoe/SAE-based-representation-engineering list is actively maintained
(2026-06) and is the best of the starter awesome-lists for this topic. The HF demo
huggingface/eiffel-tower-llama-demo exists and is a complete, well-documented SAE-steering
reference implementation (Llama 3.1 8B + arditi SAEs, forward-hook steering with configurable
layer/feature/strength)[16]. The dataset future-probes/activation_steering could not be verified via the
HF API — treat as unverified until manually confirmed.

Page 4

AI SLOP Research Harvest — Topic 01: Mechanistic Interpretability & Activation Steering

3 Mechanism catalog
Each entry follows the project template. Confidence tiers: ESTABLISHED / DOCUMENTED
(peer-reviewed or widely replicated), PLAUSIBLE INTERPRETATION (consistent with evidence,
not fully pinned), PROJECT HYPOTHESIS (our proposed artistic use), SPECULATION. Creative
utility and mechanism confidence are scored separately (High / Medium / Low), per project rule: a
beautiful accident may score high on the first and low on the second.

M1 — Contrastive Activation Addition (CAA)
SOURCE: Rimsky et al., 'Steering Llama 2 via Contrastive Activation Addition' (ACL 2024); code:

github.com/nrimsky/CAA[3]
SOURCE TYPE: Peer-reviewed paper + reference code
LICENSE / USAGE NOTES: Code MIT; needs local open-weight model and contrast-pair dataset

(Anthropic's model-written-evals datasets are commonly reused)
WHAT IT ACTUALLY DOES: Averages last-token activation differences over paired prompts differing

only in whether the target behavior is exhibited; adds α·v to residual stream at a chosen layer during
generation
CONTROLLABLE VARIABLES: Layer (single-layer application tolerated even at |α|>1), coefficient α

(sign flips the behavior), token span (generation tokens only), vector construction set
WHAT STATE OR STRUCTURE IT PRESERVES: At moderate α: fluency, instruction-following, general

competence — behavior shifts along one axis while grammar survives
WHAT IT CHANGES: Propensity toward the steered behavior/persona dimension (e.g., corrigibility,

sycophancy)
FAILURE SURFACE: High α across many layers → incoherence; OOD fragility — vectors built on

mismatched distributions generalize poorly[14]
ORIGINAL PURPOSE: Safety-relevant behavior control without fine-tuning
POSSIBLE AI-SLOP MUTATION: Two opposed CAA vectors (e.g., 'euphoric' vs 'despairing', 'verbose

scholar' vs 'broken telegraph') injected simultaneously at different layers — a literal internal contradiction
the model must reconcile every token
EXPECTED OBSERVABLE ARTIFACT: Register oscillation within single sentences; metaphors that

fight themselves; semantic whiplash with intact syntax — the 'governance error' made literal
AMPLIFICATION / ITERATION METHOD: Sweep α■×α■ on a 2D grid; feed steered output back as next

prompt while keeping vectors active (recursive contamination)
CONTROL OR ABLATION TEST: Random directions of matched norm (should produce generic

degradation, not structured opposition); single-vector baselines
LIMITATION: Vectors capture population-average directions; fine, idiosyncratic concepts may not be

linearly extractable
MECHANISM CONFIDENCE: High for the intervention mechanics; Medium for any specific concept pair

behaving as imagined
[15]

APPLICABLE MEDIA: LLM; multimodal LLMs in principle (LMM MI literature is emerging

)

AI_SLOP CONNECTION: DAVID operator analogue (internal); mutation operator; experiment class
CONFIDENCE TIER: ESTABLISHED / DOCUMENTED
CREATIVE UTILITY: High

Page 5

AI SLOP Research Harvest — Topic 01: Mechanistic Interpretability & Activation Steering

M2 — Activation Addition (ActAdd)
[2]

SOURCE: Turner et al., 'Activation Addition: Steering Language Models Without Optimization' (2023)
SOURCE TYPE: arXiv paper + public notebooks
LICENSE / USAGE NOTES: Open; trivially implementable with TransformerLens hooks
WHAT IT ACTUALLY DOES: Computes the difference between activations on two natural-language

prompts (e.g., 'Love' − 'Hate') and adds it during generation — no dataset pairs, no averaging
CONTROLLABLE VARIABLES: Prompt pair, layer, α, injection window
WHAT STATE OR STRUCTURE IT PRESERVES: Same residual-stream geometry; single-site addition

leaves downstream computation intact except through the added offset
WHAT IT CHANGES: Topic/attitude of generation toward the positive prompt's concept
FAILURE SURFACE: Concept bleed into unrelated content; coherence cliff at high α (documented in the

original post and later surveys[1])
ORIGINAL PURPOSE: Cheapest possible demonstration of linear representation control
POSSIBLE AI-SLOP MUTATION: Use semantically impossible prompt pairs ('the taste of Tuesday' − 'the

sound of copper') so the extracted direction is itself an artifact of the model's confusion — steering by a
nonsense compass
EXPECTED OBSERVABLE ARTIFACT: Low-α: subtle tonal contamination; mid-α: forced metaphorical

interpretation of everything through the nonsense axis; high-α: collapse
AMPLIFICATION / ITERATION METHOD: Log-spaced α sweep; record the exact α where grammatical

syntax outlives semantic coherence (the sweet-spot band is the artifact zone)
CONTROL OR ABLATION TEST: Same procedure with a grammatical but unrelated prompt pair; α = 0

baseline; shuffled-vector control
LIMITATION: Single-prompt-pair vectors are noisy; concept purity is low compared to CAA
MECHANISM CONFIDENCE: High that the intervention does something directional; Low-Medium that a

nonsense pair yields a meaningful axis — that is the experiment
APPLICABLE MEDIA: LLM
AI_SLOP CONNECTION: Mutation operator; new mechanism class ('steering by malformed probes')
CONFIDENCE TIER: ESTABLISHED (mechanism) / SPECULATION (malformed-pair variant)
CREATIVE UTILITY: High

M3 — SAE feature clamping / feature steering
[6]

SOURCE: Templeton et al., 'Scaling Monosemanticity' (Anthropic, 2024)

; Gemma Scope (Google

[8]

DeepMind) ; Neuronpedia platform
SOURCE TYPE: Lab publication + open weights + live interactive demos
LICENSE / USAGE NOTES: Gemma Scope weights on HF (per-repo terms); SAELens (MIT) for

loading; Neuronpedia free for exploration
WHAT IT ACTUALLY DOES: Encodes activations into SAE features, sets one feature's activation to a

fixed value, decodes back, continues the forward pass — pins a single interpretable concept into every
position
CONTROLLABLE VARIABLES: Feature index (searchable by concept on Neuronpedia), clamp value,

layer = SAE site, duration (all tokens vs window)
WHAT STATE OR STRUCTURE IT PRESERVES: Fluency survives to surprisingly high clamp values

(Golden Gate Claude stayed coherent while becoming the bridge)
WHAT IT CHANGES: The semantic center of gravity of the whole generation

Page 6

AI SLOP Research Harvest — Topic 01: Mechanistic Interpretability & Activation Steering

FAILURE SURFACE: Reconstruction error from the SAE itself contaminates the intervention

(matched-reconstruction controls are mandatory); at extreme values, monotone concept-zombification;
AxBench showed naive feature steering underperforms prompting on concept-injection benchmarks[10],
partially rebutted with careful feature selection[11]
ORIGINAL PURPOSE: Causal validation of interpretability claims; safety monitoring
POSSIBLE AI-SLOP MUTATION: Clamp two features with antagonistic meanings (e.g., 'silence' +

'alarm') to high values simultaneously; or clamp one feature while an external controller decays it slowly
— watched entropy
EXPECTED OBSERVABLE ARTIFACT: Negotiation text: the model trying to satisfy both concepts

produces genuine novelty (this is the AxBench 'cavalry' failure mode — 'The horse is ready to eat' —
reframed as an artifact family[11])
AMPLIFICATION / ITERATION METHOD: Grid over (feature A strength, feature B strength); map the

phase diagram of coexistence vs dominance vs incoherence
CONTROL OR ABLATION TEST: Random unlabeled feature at same strength; dead-latent clamp (should

do nothing); prompt-only concept injection comparison (AxBench discipline)
LIMITATION: Feature labels are hypotheses until causally tested; SAE reconstruction error is a hidden

second intervention
MECHANISM CONFIDENCE: High that clamping shifts behavior; Medium that dual-clamp antagonism

produces structured rather than mushy output
APPLICABLE MEDIA: LLM; vision-language models (SAEs with monosemantic features in VLMs

demonstrated 2025[15])
AI_SLOP CONNECTION: DAVID operator analogue; state-controller rule (time-varying clamp);

validator (feature dashboards as readouts)
CONFIDENCE TIER: ESTABLISHED / DOCUMENTED
CREATIVE UTILITY: Very high

M4 — Activation patching / causal tracing
[12]

SOURCE: Meng et al. causal tracing (2022)

; Zhang & Nanda patching conventions (2023);
implemented in TransformerLens, pyvene, nnsight
SOURCE TYPE: Peer-reviewed papers + standard library primitives
LICENSE / USAGE NOTES: All tooling MIT/Apache; method is analysis-first
WHAT IT ACTUALLY DOES: Runs the model on a clean and a corrupted prompt, then grafts activation

slices from one run into the other at chosen sites to localize what carries a behavior
CONTROLLABLE VARIABLES: Source/target run pair, patched site (layer × component × token), patch

extent
WHAT STATE OR STRUCTURE IT PRESERVES: Everything outside the patched site — this is the most

surgical intervention in the catalog
WHAT IT CHANGES: Usually diagnostic (which site restores/breaks the behavior); used generatively, it

grafts a fragment of one run's computation into another
FAILURE SURFACE: Off-distribution grafts: a mid-layer residual vector from a different run is not a

legal input to downstream layers, producing hybrid computations with no prompt-level analogue
ORIGINAL PURPOSE: Causal localization (which component is responsible for the fact/behavior)
POSSIBLE AI-SLOP MUTATION: Cross-domain grafting as composition: run A = a technical manual,

run B = a lament; patch A's late-layer residuals into B mid-generation and let the model finish a text whose
own machinery has been swapped out from under it

Page 7

AI SLOP Research Harvest — Topic 01: Mechanistic Interpretability & Activation Steering

EXPECTED OBSERVABLE ARTIFACT: Register rupture at the patch boundary; 'scar tissue' sentences

where the model re-coheres around the graft
AMPLIFICATION / ITERATION METHOD: Move the patch boundary token-by-token through the

generation; each position is a different surgery — the sequence of outputs maps the graft's zone of
influence
CONTROL OR ABLATION TEST: Self-patch (clean run into itself) must reproduce the original;

random-direction patch as damage control
LIMITATION: Single-token effects dominate the literature; long-range graft consequences are

under-characterized — open territory, meaning both opportunity and uncertainty
MECHANISM CONFIDENCE: High for diagnosis; Low-Medium for predictable generative outcomes of

large grafts
APPLICABLE MEDIA: LLM
AI_SLOP CONNECTION: DAVID operator (surgical graft); experiment; connects to topic 9 (iterative

encode-decode / artifact inheritance)
CONFIDENCE TIER: ESTABLISHED (diagnostic) / PROJECT HYPOTHESIS (generative grafting)
CREATIVE UTILITY: High

M5 — Persona vectors
SOURCE: Chen et al., 'Persona Vectors: Monitoring and Controlling Character Traits in Language

Models' (Anthropic, 2025)[13]; related: Lu et al., 'The Assistant Axis'
SOURCE TYPE: Lab research paper
LICENSE / USAGE NOTES: Method reproducible on open models; Anthropic artifacts not public, but the

construction is standard contrastive difference-of-means
WHAT IT ACTUALLY DOES: Extracts directions corresponding to character traits (evil, sycophancy,

hallucination-propensity, humor, optimism) from natural-language trait descriptions; can monitor, steer, or
(via 'preventative steering' during fine-tuning) vaccinate against trait drift
CONTROLLABLE VARIABLES: Trait definition corpus, extraction layer, α, timing (inference vs

training-time)
WHAT STATE OR STRUCTURE IT PRESERVES: General capabilities at moderate dose (benchmarked

in the paper)
WHAT IT CHANGES: The 'who is speaking' layer — closer to Temporary Minds territory than any other

mechanism in this catalog
FAILURE SURFACE: Trait entanglement: real traits are not independent axes, so pushing one drags

neighbors; extreme persona clamping destabilizes the assistant frame entirely (cf. Assistant Axis drift
findings)
ORIGINAL PURPOSE: Monitoring and preventing undesirable persona shifts, incl. emergent

misalignment
POSSIBLE AI-SLOP MUTATION: A legitimately computed 'Temporary Mind' — extract a persona vector

for one of the project's 26 minds from its procedural description, inject it, and compare against the
prompt-only version. The delta between prompt-mediated and vector-mediated identity is measurable and
itself an artwork about mediation
EXPECTED OBSERVABLE ARTIFACT: Vector-injected persona leaks into unprompted dimensions (the

model's metaphors, its refusals, its punctuation habits) where prompt-only persona stays semantic
AMPLIFICATION / ITERATION METHOD: Dose sweep with a fixed probe battery measuring both

target-trait expression and collateral trait drift

Page 8

AI SLOP Research Harvest — Topic 01: Mechanistic Interpretability & Activation Steering

CONTROL OR ABLATION TEST: Prompt-only persona at matched surface instruction strength;

orthogonal random vector
LIMITATION: Trait directions extracted from small corpora are fragile; cross-model transfer is poor
MECHANISM CONFIDENCE: Medium-High (peer-level lab work, but young literature)
APPLICABLE MEDIA: LLM
AI_SLOP CONNECTION: Temporary Mind (direct analogue); DAVID operator; experiment
CONFIDENCE TIER: ESTABLISHED / DOCUMENTED (method); PROJECT HYPOTHESIS

(Temporary-Minds bridge)
CREATIVE UTILITY: Very high — the strongest single bridge to existing project machinery

M6 — ROME rank-one model editing
SOURCE: Meng et al., 'Locating and Editing Factual Associations in GPT' (NeurIPS 2022); repo

kmeng01/rome[12]
SOURCE TYPE: Peer-reviewed paper + reference implementation
LICENSE / USAGE NOTES: MIT; repo frozen since 2024-04 — use as reference, prefer maintained

successors (MEMIT, EasyEdit suites) for new work
WHAT IT ACTUALLY DOES: Locates a factual association via causal tracing, then solves a closed-form

rank-one update to an MLP weight matrix to rewrite one fact (e.g., 'Eiffel Tower is in Rome')
CONTROLLABLE VARIABLES: Target fact (subject–relation–object), edited layer(s), update strength
WHAT STATE OR STRUCTURE IT PRESERVES: Weights elsewhere untouched; designed to preserve

all other behavior
WHAT IT CHANGES: The model's believed fact — permanently, until re-edited
FAILURE SURFACE: The famous one: edits don't generalize cleanly (rephrasings, implications of the

edited fact often fail) and can distort nearby facts — the model holds a belief it cannot reason consistently
about
ORIGINAL PURPOSE: Correcting factual errors without retraining
POSSIBLE AI-SLOP MUTATION: Install a deliberately false world-fact as a permanent internal axiom,

then let prompt-level constraints reference the pre-edit world — the model's internals and its context now
permanently disagree
EXPECTED OBSERVABLE ARTIFACT: Confabulation with conviction: the model defends the edited

fact, invents supporting detail, and fails differently than a prompted liar does
AMPLIFICATION / ITERATION METHOD: Sequential edits building a small false cosmology; measure

how contradictions between edits surface (edit interference)
CONTROL OR ABLATION TEST: Prompt-only false premise ('pretend the Eiffel Tower is in Rome') at

matched strength; edit an unreferenced decoy fact
LIMITATION: Failure to generalize is well documented; this is a feature for the project (the inconsistency

IS the artifact) but a bug for any truth claim
MECHANISM CONFIDENCE: High (heavily replicated, incl. ~20-line pyvene reproduction of the original

tracing figure[17])
APPLICABLE MEDIA: LLM
AI_SLOP CONNECTION: DAVID operator (persistent internal rewrite); state preservation study;

experiment
CONFIDENCE TIER: ESTABLISHED / DOCUMENTED
CREATIVE UTILITY: Medium-High

Page 9

AI SLOP Research Harvest — Topic 01: Mechanistic Interpretability & Activation Steering

M7 — Inference-Time Intervention (ITI)
SOURCE: Li et al., 'Inference-Time Intervention: Eliciting Truthful Answers from a Language Model'

(NeurIPS 2023)[5]
SOURCE TYPE: Peer-reviewed paper + code
LICENSE / USAGE NOTES: Open code; requires probe training per head
WHAT IT ACTUALLY DOES: Trains linear probes on attention-head outputs for a property (truthfulness),

finds the K most informative heads, and shifts those heads' outputs along the probe direction at every
generation step
CONTROLLABLE VARIABLES: Head count K, α, property dataset
WHAT STATE OR STRUCTURE IT PRESERVES: Most of the network; only top-K head outputs touched
WHAT IT CHANGES: A measurable behavioral axis (truthfulness benchmark gains were large in the

paper)
FAILURE SURFACE: Multi-head intervention compounds; property labels are only as clean as the probe

data
ORIGINAL PURPOSE: Truthfulness elicitation
POSSIBLE AI-SLOP MUTATION: Train probes for an aesthetic property with no ground truth ('sincerity',

'dread') and intervene anyway — the probe's label noise becomes the mechanism's signature
EXPECTED OBSERVABLE ARTIFACT: Consistent but unnameable tonal shift — the model drifts

toward whatever the noisy probe actually encoded
AMPLIFICATION / ITERATION METHOD: Sweep K from 1 to 48 to watch intervention granularity trade

against coherence
CONTROL OR ABLATION TEST: Random head selection at same K; probes trained on shuffled labels

(must do nothing systematic)
LIMITATION: Per-head directions are entangled with many properties; 'truthfulness direction' framing has

been critiqued as oversimplified
MECHANISM CONFIDENCE: Medium-High
APPLICABLE MEDIA: LLM
AI_SLOP CONNECTION: Mutation operator; experiment
CONFIDENCE TIER: ESTABLISHED / DOCUMENTED
CREATIVE UTILITY: Medium

M8 — Representation Engineering (RepE / LAT / LoRRA)
[4]

SOURCE: Zou et al., 'Representation Engineering: A Top-Down Approach to AI Transparency' (2023)
[1]

SOURCE TYPE: Paper + code (and a 2025 RepE survey systematizing the design space

)

LICENSE / USAGE NOTES: Open code; PCA-based pipeline
WHAT IT ACTUALLY DOES: Reads representations via Linear Artificial Tomography (contrast stimuli,

PCA on differences), then controls via reading/contrast vectors or trains a low-rank adapter (LoRRA) to
reproduce the steered activations in weights
CONTROLLABLE VARIABLES: Stimulus set, PCA component choice, α, per-layer targeting, adapter vs

direct addition
WHAT STATE OR STRUCTURE IT PRESERVES: The top-down framing preserves interpretability of the

control knob: you steer a named concept
WHAT IT CHANGES: High-level cognitive-function-like dimensions (honesty, emotion, morality

framings in the paper)

Page 10

AI SLOP Research Harvest — Topic 01: Mechanistic Interpretability & Activation Steering

FAILURE SURFACE: Named concepts are not guaranteed to be the actual encoded axes — the name is a

hypothesis; survey documents strength/coherence trade-offs across the whole family[1]
ORIGINAL PURPOSE: Transparency and control via top-down representations
POSSIBLE AI-SLOP MUTATION: Extract LAT directions for paired contradictory concepts from the

SAME corpus and apply the second principal component instead of the first — steering by the residual
axis nobody named
EXPECTED OBSERVABLE ARTIFACT: Coherent drift toward an unnamed attractor; post-hoc naming of

the attractor becomes part of the artwork
AMPLIFICATION / ITERATION METHOD: Iterate: extract → steer → collect outputs → re-extract a new

direction from the steered outputs (direction bootstrapping)
CONTROL OR ABLATION TEST: PC1 vs PC2 vs random subspace direction at matched norm
LIMITATION: PCA assumptions (linear, orthogonal) are known to be approximations; interpretive naming

risk
MECHANISM CONFIDENCE: Medium-High for the machinery; the unnamed-axis variant is

SPECULATION by design
APPLICABLE MEDIA: LLM; adaptable to multimodal representation spaces
AI_SLOP CONNECTION: DAVID operator; new mechanism class (unnamed-attractor steering)
CONFIDENCE TIER: ESTABLISHED (machinery) / SPECULATION (variant)
CREATIVE UTILITY: High

M9 — Difference-in-means & ReFT-r1 (AxBench family)
SOURCE: Wu et al., 'AxBench' (ICML 2025)

[10]

; AxBench rank-1 leaderboard incl. HyperSteer,

RePS[18]
SOURCE TYPE: Benchmark paper + public dictionaries and leaderboard
LICENSE / USAGE NOTES: Dictionaries publicly released; usable via pyvene
WHAT IT ACTUALLY DOES: DiffMean: difference of mean activations between concept and

non-concept examples, computed at scale over thousands of concepts. ReFT-r1: trained rank-1
intervention subspace per concept. Both released as SAE-scale dictionaries
CONTROLLABLE VARIABLES: Concept index (thousands), α, layer site, method (DiffMean vs trained

variants)
WHAT STATE OR STRUCTURE IT PRESERVES: Benchmark-quantified fluency/instruction-following

trade-off — this family is the best-instrumented for dose-response measurement
WHAT IT CHANGES: Concept incorporation strength, measurably, at scale
FAILURE SURFACE: The leaderboard itself documents the cliff: scores collapse differently per method

as α grows; concept detection is far easier than concept steering — asymmetry worth exploiting
ORIGINAL PURPOSE: Standardized comparison of steering methods
POSSIBLE AI-SLOP MUTATION: Use the released dictionaries as a readymade concept arsenal:

random-pair concept injection at benchmark-quantified doses = a compositional instrument with known
failure calibration
EXPECTED OBSERVABLE ARTIFACT: Statistically predictable weirdness — you can select the α band

where concept incorporation succeeds but instruction-following degrades (the benchmark's own
harmonic-mean penalty zone)
AMPLIFICATION / ITERATION METHOD: Scripted traversal of the concept dictionary under fixed dose,

generating a systematic corpus of controlled contaminations

Page 11

AI SLOP Research Harvest — Topic 01: Mechanistic Interpretability & Activation Steering

CONTROL OR ABLATION TEST: The benchmark IS the control framework (fluency/concept/instruction

ratings)
LIMITATION: Built on Gemma-2-2B/9B; LLM-judge scoring has known biases
MECHANISM CONFIDENCE: High
APPLICABLE MEDIA: LLM
AI_SLOP CONNECTION: Validator (benchmark as measurement instrument); experiment; mutation

operator
CONFIDENCE TIER: ESTABLISHED / DOCUMENTED
CREATIVE UTILITY: Medium-High

M10 — Assistant Axis / activation capping
SOURCE: Lu et al., 'The Assistant Axis: Situating and Stabilizing the Default Persona of Language

Models' (Anthropic Fellows, with Neuronpedia interactive demo)[19]
SOURCE TYPE: Lab paper + live interactive demo
LICENSE / USAGE NOTES: Demo on Neuronpedia; method reproducible
WHAT IT ACTUALLY DOES: Identifies a direction along which the model's persona drifts away from

'assistant'; activation capping holds the model within the assistant region rather than pushing it anywhere
new
CONTROLLABLE VARIABLES: Cap threshold, monitored direction(s), intervention site
WHAT STATE OR STRUCTURE IT PRESERVES: The default persona — this is a stabilizer, not a

destabilizer
WHAT IT CHANGES: Suppresses drift into character-breaking trajectories (including harmful ones)
FAILURE SURFACE: Inverted for the project: capping is the control condition. Its interesting misuse is

selective de-capping — removing the stabilizer locally while an external controller watches drift
accumulate
ORIGINAL PURPOSE: Safety: keeping deployed models in-character
POSSIBLE AI-SLOP MUTATION: Drift cartography: deliberately let the persona axis run free under a

conflicting-constraint load, log the trajectory in activation space, and use the logged path as a score for
text generation
EXPECTED OBSERVABLE ARTIFACT: Persona erosion made visible as text structure — the moment of

character-break becomes a formal event in the piece
AMPLIFICATION / ITERATION METHOD: Long-horizon generation with periodic axis projection

logging; threshold alarms drive an external state machine
CONTROL OR ABLATION TEST: Capped vs uncapped under identical adversarial load
LIMITATION: Persona axes are population-level; individual drift is noisier
MECHANISM CONFIDENCE: Medium-High
APPLICABLE MEDIA: LLM
AI_SLOP CONNECTION: State-controller rule (drift-driven controller); validator; Temporary Mind

(erosion study)
CONFIDENCE TIER: ESTABLISHED / DOCUMENTED (capping) / PROJECT HYPOTHESIS (drift

cartography)
CREATIVE UTILITY: High

Page 12

AI SLOP Research Harvest — Topic 01: Mechanistic Interpretability & Activation Steering

4 Failure surfaces as artistic material
The project treats failure surfaces as mechanisms. This topic offers four that are unusually well
characterized — meaning the failure can be aimed at rather than stumbled into.
Failure
surface

Documented behavior

Aiming parameters

Evidence tier

Coherence cliff

As steering coefficient α grows, generations
pass from on-concept fluent → concept-forced
→ syntactically intact but semantically broken
→ token salad. The transitions are
reproducible per model/layer

α (log-spaced sweep), layer
choice, number of intervened
layers (single-layer tolerates
|α|>1 better than multi-layer)

ESTABLISHED[1]

Concept
colonization

A clamped SAE feature progressively rewrites
every topic as itself (Golden Gate: coherent
but monomaniacal). Intermediate clamp
values produce negotiation texts

Clamp value; feature choice;
token window

ESTABLISHED[6]

Intervention
asymmetry

Concept detection by representation methods
is strong; concept steering is
weak-to-moderate (AxBench). Reading minds
is easier than writing them — the write
channel is the lossy one

Method selection; benchmark
scores as calibration

ESTABLISHED[10][1

Edit
inconsistency

ROME-style fact edits fail to propagate to
rephrasings and implications — the model
holds contradictory beliefs simultaneously and
confabulates when pressed

Edit set design; probe battery
targeting implication chains

ESTABLISHED[12]

Feature-label
illusion

A Neuronpedia label is a hypothesis from
top-activating examples; features fire on
things outside their label, so naive steering by
label mis-fires (AxBench 'hypertrophy house'
failure)

Require causal validation
before relying on a label; log
mis-fires as artifacts

ESTABLISHED[10][1

1]

1]

Table 2 — Characterized failure surfaces. Each row is an instrument: the 'failure' is reproducible,
parameterizable, and documentable per the project's run-log template.

5 Promising experiments
E1 — The Contradiction Engine (dual-vector internal conflict)
HYPOTHESIS: Two antagonistic steering vectors injected simultaneously at different layers force a

per-token reconciliation that produces structured register conflict unlike either single-vector baseline or a
prompt-level contradiction
REPRESENTATIONAL TENSION: Vector A (e.g., 'clinical detachment') at an early-mid layer shapes

semantic planning; vector B (e.g., 'grief') at a later layer shapes surface realization — the two jurisdictions
cannot see each other directly
COMPETING CONSTRAINTS: Both vectors act on the same residual stream; the model must produce one

coherent token distribution satisfying two incompatible pressures
WHY THE SYSTEM MAY STRUGGLE: The vectors were extracted independently; their sum is off the

training manifold of coherent single-persona text

Page 13

AI SLOP Research Harvest — Topic 01: Mechanistic Interpretability & Activation Steering

EXPECTED RESULT: Intra-sentence register rupture; metaphor systems that contradict their own

framing; a measurable α■×α■ phase diagram with a coexistence band, a dominance region, and an
incoherence cliff
NEGATIVE CONTROL: Two random orthogonal directions of matched norms (expect generic mush, not

structured opposition); prompt-only contradictory persona
ABLATION: A alone; B alone; A+B at the same layer (tests whether layer separation is load-bearing)
DOSE RESPONSE: 6×6 log-spaced grid over (α■, α■); fixed probe battery: fluency score, sentiment arc

variance within sentences, human rating of 'structured vs mushy'
ITERATIVE VERSION: Steered output becomes next-round prompt while both vectors persist; measure

whether the conflict compounds or equilibrates
FALSIFICATION CONDITION: Dual-vector outputs are statistically indistinguishable from single-vector

mixtures or from random-direction controls on all probes

E2 — Concept colonization phase map (SAE clamp sweep)
HYPOTHESIS: Clamping a single Gemma-Scope feature across a strength sweep traces a reproducible

trajectory from thematic mention → pervasive metaphor → identity takeover → incoherence, with sharp
phase boundaries
REPRESENTATIONAL TENSION: The clamped feature demands expression at every token; the

instruction-tuned conversational prior demands task relevance
COMPETING CONSTRAINTS: Feature clamp value vs. the model's coherence-maintenance capacity
WHY THE SYSTEM MAY STRUGGLE: Feature steering is 'controlled damage' — reconstruction error

plus forced concept expression jointly push off-manifold[11]
EXPECTED RESULT: Ordered phase sequence with identifiable boundary artifacts; the boundary zones

(not the extremes) produce the richest text
NEGATIVE CONTROL: Dead-latent clamp (expect no effect); random unlabeled feature;

matched-reconstruction control (clamp nothing but pass through the SAE) to isolate reconstruction
damage from feature effect
ABLATION: Clamp at prompt tokens only vs generation tokens only vs all
DOSE RESPONSE: Clamp values across at least two orders of magnitude; 20 prompts × 8 strengths;

score concept density, fluency, instruction adherence
ITERATIVE VERSION: Re-clamp at each generation round using the previous round's most-activated

OTHER feature as the next clamp target (feature succession)
FALSIFICATION CONDITION: No ordered phase structure: effects are monotonic mush from the first

nonzero clamp

E3 — The steered state machine (controller × internal intervention)
HYPOTHESIS: An external controller that modulates steering coefficient over time according to logged

internal state (persona-axis projection, feature activations) produces path-dependent text that constant-α
steering cannot
REPRESENTATIONAL TENSION: The controller's schedule (external memory, PROCEDURAL) vs. the

model's autoregressive tendency to re-equilibrate after each intervention
COMPETING CONSTRAINTS: Controller pushes the model along a logged trajectory; model pulls

toward its basin
WHY THE SYSTEM MAY STRUGGLE: Each intervention is a perturbation the next tokens must digest;

repeated perturbation before digestion accumulates debt

Page 14

AI SLOP Research Harvest — Topic 01: Mechanistic Interpretability & Activation Steering

EXPECTED RESULT: Text whose structure encodes the control trajectory: visible 'tides', hysteresis

(A→B→A does not return to A), scar passages after coefficient spikes
NEGATIVE CONTROL: Same total steering budget delivered at constant α; random schedule with

matched statistics
ABLATION: Controller with no state feedback (open loop) vs closed loop on logged projections
DOSE RESPONSE: Schedule amplitude and frequency sweep (slow drift vs spike-and-recover)
ITERATIVE VERSION: This IS the iterative version; long-horizon runs of 10k+ tokens with full activation

logging
FALSIFICATION CONDITION: Closed-loop trajectories show no hysteresis and no structural dependence

on schedule — path dependence is absent

E4 — Surgical graft (cross-run activation patching as composition)
HYPOTHESIS: Patching late-layer residual slices from run A (e.g., a technical manual passage) into run

B (e.g., a lament) at a chosen token position produces a re-coherence artifact family with a measurable
zone of influence around the graft point
REPRESENTATIONAL TENSION: Upstream computation believes it is writing A; downstream

computation receives a vector encoding B's trajectory
COMPETING CONSTRAINTS: Continuity with generated prefix vs. consistency with grafted state
WHY THE SYSTEM MAY STRUGGLE: The grafted vector is off-distribution for the receiving layers in

this context — a legal vector from an illegal history
EXPECTED RESULT: A 'scar' sentence at the graft boundary, then re-coherence whose style bears both

ancestries; patch position sweep maps influence radius
NEGATIVE CONTROL: Self-patch (must reproduce original exactly); patch from an unrelated third run at

matched norm
ABLATION: Patch size: single token position vs span; single layer vs adjacent layers
DOSE RESPONSE: Interpolated grafts: (1−t)·x_B + t·x_A for t in [0,1]
ITERATIVE VERSION: Chain grafts: each output becomes run B for the next graft from a rotating cast of

A-sources (artifact inheritance)
FALSIFICATION CONDITION: Grafts produce only local token corruption with no structured downstream

signature distinguishable from random-vector damage

Page 15

AI SLOP Research Harvest — Topic 01: Mechanistic Interpretability & Activation Steering

6 Cross-modal applications
Target medium

Transfer path

Status

Notes

Vision-language
models

SAEs with monosemantic features in VLMs
demonstrated (2025); steering vectors in LMMs
tracked by the Awesome-LMMs-MI list (active,
2026-03)

DOCUMENTE
D, young

Concept clamping in a VLM
could force visual
descriptions through a foreign
concept — bridge to topic 7

Image diffusion

Same x' = x + α·v logic applies to diffusion latents
and cross-attention maps — deferred to Topic 02
(inversion/latent manipulation)

NEXT PDF

CrossAttentionControl and
PnPInversion leads already in
the queue

Audio (Suno/API
models)

No verified activation access to proprietary audio
models; honest analogue is procedural: external
controller + spectral operators

PROCEDURAL
only

Internal steering for open
audio diffusion models (e.g.,
teticio/latent-audio-diffusion
line) is a Topic 06 item

GLSL /
procedural

Not applicable directly; but the 'steering phase
diagram' concept (maps of
coexistence/dominance/incoherence regions)
transfers as a visualization method for any
parameterized system

METAPHOR

Useful as design language,
not as mechanism

Controllers
(TOPOS-SRE)

Strongest fit: any steering intervention exposes
(layer, direction, α, window) as clean state
variables for an external state machine

READY

E3 is written for this
integration

Table 3 — Cross-modal transfer assessment.

7 What appears most useful for AI SLOP
1. Steering interventions are the project's first honest internal mechanism. Every prior mechanism
in the registry is either prompt-level or controller-level. Activation steering is the first catalog entry
where the mechanism physically resides inside the generative system during inference, with named,
sweepable, ablatable variables. It upgrades DAVID-operator language from procedural metaphor to
testable instrumentation — while the epistemic labels still apply (a steering vector's artistic
interpretation remains a hypothesis).
2. The coherence cliff is a calibrated instrument, not an accident. Because the fluency-vs-concept
trade-off is benchmarked (AxBench) and documented across methods, the project can compose at the
edge of collapse on purpose and cite the dose. 'We steered Gemma-2-9B at α where concept
incorporation survives but instruction-following measurably degrades' is a mechanism claim, not a
vibe.
3. Persona vectors are the missing bridge to Temporary Minds. M5 proposes the cleanest
experiment in this document: extract a vector-level Temporary Mind and measure the delta against its
prompt-only twin. Whatever the outcome, the delta is publishable project knowledge — either vector
mediation adds something prompting cannot (leakage into unprompted dimensions) or it does not
(prompting sufficiency, consistent with AxBench's prompt baseline dominance).
4. Controller integration is already engineered. nnsight/NDIF removes the GPU barrier (remote
interventions on hosted models up to 405B+), Neuronpedia removes the feature-discovery barrier, and

Page 16

AI SLOP Research Harvest — Topic 01: Mechanistic Interpretability & Activation Steering

steering parameters map one-to-one onto the state variables an SRE controller already manages. E3 can
be prototyped with a local Gemma-2-2B and SAELens in a weekend.

8 Weak / dubious ideas worth rejecting
Claim / idea

Verdict

Why

'Prompting manipulates the
model's hidden activations'

REJECT as
stated

Prompting changes inputs; activations change as a consequence of
normal inference, which is not an intervention. Without hooks, no
activation-level access exists. Keep the vocabulary clean

'SAE feature steering is a
superior control method'

REJECT

AxBench: prompting outperforms SAE steering for concept injection;
SAEs' value here is causal validation and failure-surface access, not
control supremacy[10][11]

'Feature labels are ground truth'

REJECT

Labels come from top-activating examples; features misfire off-label.
Label = hypothesis until causal test (the 'hypertrophy house' artifact is
the counterexample[11])

'There is one direction for X'
(generalized from
refusal-direction results)

REJECT as
generalization

Single-direction mediation is documented for refusal across 13
models[2] — that does not license single-direction claims for arbitrary
concepts

'Steering reveals the model's
true hidden self'

REJECT
(mysticism)

Steering adds a vector. The output is a perturbed computation, not a
confession. Project rule: no hidden-mind claims

'Refusal-direction erasure as
artistic constraint removal'

OUT OF
SCOPE

Documented mechanism (Arditi et al. 2024), deliberately excluded: the
project is not safety-bypass research

kmeng01/rome as living
infrastructure

DEPRECATE

Frozen since 2024-04; fine as reference implementation, wrong as a
dependency for new work

future-probes/activation_steeri
ng dataset

UNVERIFIED

Not resolvable via HF API on 2026-09-19; do not cite until confirmed

Table 4 — Rejection register.

9 Open questions
• Do antagonistic dual-vector interventions produce phase structure (coexistence bands) or merely
averaged mush? No published dose-response map for simultaneous opposed concepts was found — E1
targets exactly this gap.
• How does steered generation under persistent intervention evolve over long horizons (10k+ tokens)?
The literature is dominated by short completions; drift, equilibration, and debt-accumulation dynamics
are uncharacterized.
• Can a persona vector extracted from a procedural description (a Temporary Mind) capture anything
the prompt version does not? The extraction corpus for a procedural identity is an unusual object —
part prompt set, part score.
• Does grafting (activation patching) at generative scale produce re-coherence signatures distinct from
simple corruption? Patching is characterized diagnostically, not compositionally.

Page 17

AI SLOP Research Harvest — Topic 01: Mechanistic Interpretability & Activation Steering

• What is the right epistemic label for an artifact that appears only inside a narrow α band? The project's
OBSERVED label covers behavior, but band-localized phenomena may deserve a named convention
(e.g., 'windowed artifact').
• Feature succession (E2 iterative version): is the most-activated-other-feature rule a meaningful
'associative step' or an arbitrary jump? No prior work found on iterated feature-to-feature clamping.

Page 18

AI SLOP Research Harvest — Topic 01: Mechanistic Interpretability & Activation Steering

10 Sources / bibliography
Wehner, J., et al. (2025). Taxonomy of Representation Engineering (survey of intervention methods,
strength/coherence trade-offs). arXiv:2502.19649. https://arxiv.org/abs/2502.19649
Turner, A., et al. (2023). Activation Addition: Steering Language Models Without Optimization.
arXiv:2308.10248; Arditi, A., et al. (2024). Refusal in Language Models Is Mediated by a Single Direction.
NeurIPS 2024, arXiv:2406.11717. https://arxiv.org/abs/2308.10248
Rimsky, N., et al. (2024). Steering Llama 2 via Contrastive Activation Addition. ACL 2024. arXiv:2312.06681.
Code: github.com/nrimsky/CAA. https://arxiv.org/abs/2312.06681
Zou, A., et al. (2023). Representation Engineering: A Top-Down Approach to AI Transparency.
arXiv:2310.01405; systematized in Representation Engineering for Large-Language Models (2025),
arXiv:2502.17601. https://arxiv.org/abs/2310.01405
Li, K., et al. (2024). Inference-Time Intervention: Eliciting Truthful Answers from a Language Model. NeurIPS
2023. arXiv:2306.03341. https://arxiv.org/abs/2306.03341
Templeton, A., et al. (2024). Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet.
Anthropic. transformer-circuits.pub/2024/scaling-monosemanticity. https://transformer-circuits.pub/2024/sca
ling-monosemanticity/index.html
Bricken, T., et al. (2023). Towards Monosemanticity: Decomposing Language Models With Dictionary Learning.
Anthropic. transformer-circuits.pub/2023/monosemantic-features. https://transformer-circuits.pub/2023/mon
osemantic-features/index.html
Lieberum, T., et al. (2024). Gemma Scope: Open Sparse Autoencoders Everywhere All At Once on Gemma 2.
arXiv:2408.05147. https://arxiv.org/abs/2408.05147
Neuronpedia (2025). Gemma Scope 2: Suite of SAEs and Transcoders for Gemma 3.
neuronpedia.org/gemma-scope-2. https://www.neuronpedia.org/gemma-scope-2
Wu, Z., et al. (2025). AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders. ICML
2025 (spotlight). arXiv:2501.17148. Code/dictionaries:
github.com/stanfordnlp/axbench. https://arxiv.org/abs/2501.17148
Godsk Jørgensen, M., & Hansen, L. K. (2026). Steering LLMs? Actually, Sparse Autoencoders can outperform
simple baselines (partial AxBench rebuttal). arXiv:2605.31183. https://arxiv.org/abs/2605.31183
Meng, K., et al. (2022). Locating and Editing Factual Associations in GPT (ROME). NeurIPS 2022.
arXiv:2202.05262. Code: github.com/kmeng01/rome. https://arxiv.org/abs/2202.05262
Chen, R., et al. (2025). Persona Vectors: Monitoring and Controlling Character Traits in Language Models.
Anthropic. arXiv:2507.21509. https://arxiv.org/abs/2507.21509
Emergent Mind topic synthesis (2025). Targeted Activation Engineering — Limitations, Challenges, Best
Practices (OOD fragility, hyperparameter sensitivity, capability/control
trade-off). https://www.emergentmind.com/topics/targeted-activation-engineering
Zhang, H., et al. (2026). Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability
in Large Language Models. arXiv:2601.14004. Repo:
github.com/rattlesnakey/Awesome-Actionable-MI-Survey. https://arxiv.org/abs/2601.14004
dlouapre (2025). eiffel-tower-llama-demo — SAE feature steering of Llama 3.1 8B Instruct (forward-hook
reference implementation). huggingface.co/spaces/huggingface/eiffel-tower-llama-demo. https://huggingface
.co/spaces/huggingface/eiffel-tower-llama-demo
Wu, Z., et al. (2024). pyvene: A Library for Understanding and Improving PyTorch Models via Interventions.
NAACL 2024 demo. arXiv:2403.07809. https://arxiv.org/abs/2403.07809
Stanford NLP (2025). AxBench rank-1 steering leaderboard (HyperSteer, RePS, ReFT-r1, DiffMean, SAE
baselines). github.com/stanfordnlp/axbench. https://github.com/stanfordnlp/axbench

Page 19

AI SLOP Research Harvest — Topic 01: Mechanistic Interpretability & Activation Steering

Lu, et al. (2025/26). The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models.
Anthropic Fellows; interactive demo via Neuronpedia. https://www.neuronpedia.org/blog/assistant-axis
Nanda, N., & Bloom, J. (2022–). TransformerLens. github.com/TransformerLensOrg/TransformerLens
(MIT). https://github.com/TransformerLensOrg/TransformerLens
Chanin, D., Bloom, J., et al. (2023–). SAELens. github.com/decoderesearch/SAELens
(MIT). https://github.com/decoderesearch/SAELens
Fiotto-Kaufman, J., et al. (2024–). nnsight / NDIF. arXiv:2407.14561.
github.com/ndif-team/nnsight. https://github.com/ndif-team/nnsight
All URLs verified reachable or via official indexes on 2026-09-19 unless marked UNVERIFIED in Table 4.

11 Licensing / provenance appendix
Asset

License / terms

Verified

Provenance note

TransformerLens

MIT

2026-09-19 (GitHub
API)

Created by Neel Nanda;
maintained by Bryce Meyer &
Jonah Larson

SAELens

MIT

2026-09-19 (GitHub
API)

Decode Research; active
development (v6 line)

pyvene

Apache-2.0

2026-09-19 (GitHub
API)

Stanford NLP

nnsight

MIT (see repo)

2026-09-19

NDIF team, Northeastern
University; remote execution
requires free NDIF API key

kmeng01/rome

MIT

2026-09-19 (GitHub
API)

Frozen since 2024-04 —
reference only

nrimsky/CAA

MIT (see repo)

2026-09-19 (linked
from paper)

Reference CAA implementation

Gemma Scope SAE weights

Gemma terms of use (check
per-repo page on HF)

2026-09-19

Google DeepMind; Gemma
model terms apply to derivatives

Neuronpedia

Open source; hosted platform

2026-09-19

Feature dashboards, steering
demos; same org as SAELens

Awesome-Actionable-MI-Surv
ey

Repo list (papers external)

2026-09-19

Active; best current map of
actionable MI

SAE-based-representation-engi
neering (yuzhaouoe)

MIT

2026-09-19 (GitHub
API)

Active curated list for SAE
steering papers

eiffel-tower-llama-demo

See Space files

2026-09-19
(PROJECT.md)

Complete hook-based steering
reference; uses andyrdt SAEs for
Llama 3.1 8B

future-probes/activation_steeri
ng

—

UNVERIFIED

Not resolvable via HF API;
excluded from mechanism
claims

Table 5 — Licensing and provenance. GitHub metadata pulled from the public API on 2026-09-19; where a
license was not re-confirmable programmatically, the entry says 'see repo'.

Page 20

AI SLOP Research Harvest — Topic 01: Mechanistic Interpretability & Activation Steering

Research conducted 2026-09-19 via web sources, arXiv, GitHub API, and Hugging Face API. The ai_slop repository
was read (AI_CONTEXT.md, README.md) for connection mapping only — no files were modified, added, or
committed. Claims labeled ESTABLISHED trace to peer-reviewed venues or lab publications with public artifacts;
PLAUSIBLE INTERPRETATION, PROJECT HYPOTHESIS, and SPECULATION are marked inline at point of use.

Page 21
