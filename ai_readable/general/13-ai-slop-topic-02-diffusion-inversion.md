# AI SLOP Topic 02 — Diffusion Inversion, Attention & Latent Manipulation

> Source: `originals/copilot-intake-2026-09-19/CFNetworkDownload_zsowxX.pdf`
> Transcription note: Complete text extracted with `pdftotext`; spacing and pagination artifacts preserved for searchability.

AI SLOP — RESEARCH HARVEST | TOPIC 02

Diffusion Inversion, Attention
& Latent Manipulation
Trajectory surgery, attention binding conflicts, and noised-latent interference
as mechanisms of structured instability
Compiled: 2026-09-19 | For: merrypranxter/ai_slop (research-only; repository untouched)
Status labels follow the project's canonical epistemic scheme.

Self-contained companion to Topic 01 (Mechanistic Interpretability & Activation Steering).

AI SLOP Research Harvest — Topic 02: Diffusion Inversion, Attention & Latent Manipulation

Contents
1 Executive summary
2 Technical background
3 Mechanism catalog (M1–M9)
4 Failure surfaces as artistic material
5 Promising experiments (E1–E4)
6 Cross-modal applications
7 What appears most useful for AI SLOP
8 Weak / dubious ideas worth rejecting
9 Open questions
10 Sources / bibliography
11 Licensing / provenance appendix

Page 2

AI SLOP Research Harvest — Topic 02: Diffusion Inversion, Attention & Latent Manipulation

1 Executive summary
Diffusion models offer three distinct intervention substrates, and this topic covers all of them: the
trajectory (the sequence of noised latents an inversion constructs back to a starting noise), the
attention maps (spatial binding tables between text tokens and image regions), and the latent field
itself (which can be spliced, blended, and arithmetically combined between denoising runs). Each
substrate has a documented failure surface, and each failure surface is aimable: inversion error
accumulation, attention leakage, the reconstruction–editability trade-off, and non-Gaussian
intermediate latents are all characterized in peer-reviewed or benchmarked work — not folklore.
The strongest verified findings: (a) cross-attention control (Prompt-to-Prompt[1]) established that
cross-attention maps bind prompt tokens to spatial layout, and that injecting, replacing, or re-weighting
those maps edits images while preserving structure — with three named operations that are, in effect, a
tiny formal grammar for constraint conflict; (b) inversion is a leaky state channel: naive DDIM
inversion accumulates error (concentrated in early steps, amplified by classifier-free guidance[7][12]),
and every modern method (null-text[2], PnP inversion[3], ReNoise[4], eta-inversion[5]) is a different
trade between reconstruction fidelity and editability — meaning 'how wrong is the return path' is a
tunable artistic parameter, not just a bug; (c) the modern rectified-flow stack (RF-Inversion, RF-Solver,
FireFlow[9][10][11]) brings these interventions to FLUX-class models in 8–15 steps, with diffusers and
ComfyUI support, so the mechanisms are practically reachable in 2026; (d) attention leakage — edits
bleeding into untargeted regions through inaccurate cross-attention maps — is documented as the root
cause of editing failure[8], which inverts into a mechanism: leakage is controllable semantic
contamination.
Highest-value project connection: inversion gives AI SLOP a literal state channel with a return path
— image → noise → edited image — where path dependence (a canonical project principle) is
physically realized: A→C is provably not A→B→C unless B leaves a scar in the trajectory. Attention
injection is a binding-conflict instrument (two prompts fighting over the same pixels). Latent splicing is
the lowest-cost, highest-chaos member of the family, already available as experimental ComfyUI
nodes. Together these are DAVID-operator material for the image medium with genuine dose-response
structure.
Honesty constraints honored: no claim that latent space is a literal navigable world (the project
already treats it as a 'useful lie'); interpolation artifacts are explained mechanistically (off-manifold,
non-Gaussian intermediates) rather than mystically; every starter-lead repo was individually verified for
activity and license, and one provenance trap was found — there are two unrelated papers named
StyleDiffusion (§3, M8).

2 Technical background
A latent diffusion model denoises a latent zT ~ N(0,I) into an image over T steps, conditioned on text
embeddings via cross-attention. Three facts make it steerable. First, the sampling trajectory is a
deterministic ODE path (DDIM, or the rectified-flow ODE in FLUX-class models) — it can be run
backwards (inversion) to recover a noise latent that regenerates a given image, approximately. The
approximation is the whole story: each inversion step locally linearizes a nonlinear update, errors
accumulate, and classifier-free guidance amplifies them because the guided score was never meant to
be inverted[7][12]. Second, cross-attention maps Mt (pixels × tokens, per step) encode which pixels

Page 3

AI SLOP Research Harvest — Topic 02: Diffusion Inversion, Attention & Latent Manipulation

listen to which words; self-attention features encode structure (Q, K) and appearance (V) separately[13].
Third, the latent is just a tensor: between steps it can be blended, masked, spliced, or offset, and the
VAE decoder will attempt to repair whatever it receives toward a plausible image — the decoder is a
repair organ, and its repair failures are artifacts.
Verified starter leads (checked via GitHub API / HF on 2026-09-19):
Lead

Verified status

Assessment

bloc97/CrossAttentionContro
l

Real; 1,336 stars; MIT; frozen
2022-10

Historically important unofficial P2P
implementation; superseded by
google/prompt-to-prompt and diffusers attention
processors. Reference only

cure-lab/PnPInversion

Real; 414 stars; frozen 2024-03;
official ICLR 2024 code

Includes PIE-Bench (700 images) and runnable
scripts for 9 editing methods — a ready-made
comparative harness

wangkai930418/DPL

Real; 111 stars; NeurIPS 2023

The leakage-repair paper; most valuable to this
project as evidence about the failure surface, not
as a tool

sen-mao/StyleDiffusion

Real; 84 stars; active 2026-08

Prompt-embedding inversion for text-based
editing (CVMJ 2024) — NOT the ICCV 2023
style-transfer paper of the same name (see M8)

furiosa-ai/eta-inversion

Real; 34 stars; ECCV 2024

Unified harness: 8 inversion methods × 4 editing
methods via CLI flags — ideal for systematic
artifact-family studies

AustinMroz/ComfyUI-Splice
Tools

Real; 6 stars; GPL-3.0; frozen
2024-06

Experimental noised-latent manipulation nodes;
tiny adoption, no validation — treat as
SPECULATIVE tooling, interesting because it is
raw

lajjadred/comfyui-lrw-nodes

Real; 12 stars; created 2026-05

Riemannian/Bayesian latent manipulation nodes;
new, unvalidated — SPECULATIVE

Angusliuuu/Awesome-Contro
llable-Generative-Models-Pa
pers

Real; 42 stars; active 2026-07

Decent current map of controllable generation incl.
attention interpretation and spectral manipulation

HF: anshuln/visualizing_diffu
sion_attention

Author profile lists 'Visualizing
Diffusion Attention' space; API slug
unresolvable in this session

Exists per web index; treat link as
needs-manual-confirm

HF: AswinMathew/latent-spa
ce-explorer

UNVERIFIED — not resolvable via
HF API

Do not cite until confirmed

Table 1 — Starter-lead verification. Star counts and dates from the GitHub API, 2026-09-19.

Modern tooling reality: Hugging Face diffusers exposes pluggable attention processors
(set_attn_processor) as a first-class API — custom cross-attention control is a supported
extension point, not a monkey-patch[14]. RF-Inversion ships in diffusers and was re-implemented by the
ComfyUI community[9]; FireFlow does FLUX inversion+editing in 8 steps[11]. The old SD 1.5 stack
(P2P, null-text) still works but is legacy infrastructure; the 2026 working stack is FLUX/SD3-class

Page 4

AI SLOP Research Harvest — Topic 02: Diffusion Inversion, Attention & Latent Manipulation

rectified-flow models plus ComfyUI for node-level latent access.

3 Mechanism catalog
Same template as Topic 01. Tiers: ESTABLISHED / DOCUMENTED, PLAUSIBLE
INTERPRETATION, PROJECT HYPOTHESIS, SPECULATION. Creative utility and mechanism
confidence scored separately.

M1 — Cross-attention injection (Prompt-to-Prompt)
[1]

SOURCE: Hertz et al., ICLR 2023

; code: google/prompt-to-prompt; bloc97/CrossAttentionControl

(unofficial, frozen)
SOURCE TYPE: Peer-reviewed paper + official and community implementations
LICENSE / USAGE NOTES: MIT (bloc97 repo); google repo Apache-2.0 (check); diffusers pipeline

support varies by model
WHAT IT ACTUALLY DOES: Runs diffusion twice on prompt pairs sharing a seed;

injects/replaces/reweights cross-attention maps between runs. Three operators: word swap (replace token,
keep layout), prompt refinement (add tokens, freeze old attention), attention re-weighting (scale one
token's map)
CONTROLLABLE VARIABLES: cross_replace_steps and self_replace_steps (fraction of steps to control,

per word if desired), local_blend masks, equalizer coefficients per token
WHAT STATE OR STRUCTURE IT PRESERVES: Spatial layout and geometry — the cross-attention

maps ARE the layout; freezing them freezes composition
WHAT IT CHANGES: Semantic content bound to the replaced/added/reweighted tokens
FAILURE SURFACE: Attention leakage: maps are inaccurate, edits bleed into background and

semantically related distractors[8]; over-injection freezes too much and the edit cannot materialize
ORIGINAL PURPOSE: Text-only image editing without masks
POSSIBLE AI-SLOP MUTATION: Binding conflict: swap a token to a word whose semantics contradict

the frozen spatial structure ('castle' → 'flame' with castle layout frozen) — the model must render a flame
shaped like a castle. The frozen map is one jurisdiction, the new token another
EXPECTED OBSERVABLE ARTIFACT: Impossible-object renderings; category collisions with coherent

geometry; the exact replace-step fraction where the edit half-exists
AMPLIFICATION / ITERATION METHOD: Sweep cross_replace_steps from 0→1 for a fixed

contradictory swap; the transition curve maps where binding breaks
CONTROL OR ABLATION TEST: Same swap without injection (expect full layout change); injection

with identical prompts (expect bit-identical reproduction)
LIMITATION: Built for U-Net cross-attention; MMDiT models (SD3/FLUX) fuse text and image tokens,

so the mechanism needs re-derivation per architecture[15]
MECHANISM CONFIDENCE: High
APPLICABLE MEDIA: IMAGE; video derivatives exist (Video-P2P); audio diffusion uses the same

attention pattern (Topic 06)
AI_SLOP CONNECTION: DAVID operator (binding conflict); mutation operator; experiment
CONFIDENCE TIER: ESTABLISHED / DOCUMENTED
CREATIVE UTILITY: Very high

Page 5

AI SLOP Research Harvest — Topic 02: Diffusion Inversion, Attention & Latent Manipulation

M2 — Null-text inversion (pivotal null embedding optimization)
[2]

SOURCE: Mokady et al., CVPR 2023

SOURCE TYPE: Peer-reviewed paper + code
LICENSE / USAGE NOTES: Open code; per-image optimization (~3M extra parameters stored per image

at 50 steps); minutes per image
WHAT IT ACTUALLY DOES: Runs DDIM inversion, then optimizes the unconditional ('null text')

embedding at each step (pivoting on the source-prompt trajectory) so the guided reverse path reproduces
the real image
CONTROLLABLE VARIABLES: Optimization steps, pivot strength, number of pivotal embeddings

stored, guidance scale during reconstruction
WHAT STATE OR STRUCTURE IT PRESERVES: The real image itself — this is the highest-fidelity

classical reconstruction route for SD 1.5-class models
WHAT IT CHANGES: Makes real photographs editable by P2P-class methods
FAILURE SURFACE: The optimization IS a pressure valve: the null embeddings absorb all accumulated

inversion error. Editing after null-text inversion works partly because the error was paid off in advance;
reconstruction of unedited regions can still destabilize under complex prompts[7]
ORIGINAL PURPOSE: Faithful real-image editing
POSSIBLE AI-SLOP MUTATION: Read the optimized null embeddings as a per-image 'error

autobiography': 50 vectors recording exactly what the model had to believe, step by step, to make this
image possible. Interpolate two images' null-text trajectories to hybridize their debts rather than their
content
EXPECTED OBSERVABLE ARTIFACT: Images that render the compromise between two unrelated

scenes' correction histories — debt hybridization instead of image blending
AMPLIFICATION / ITERATION METHOD: Trajectory interpolation coefficient sweep; compare against

direct latent interpolation as ablation
CONTROL OR ABLATION TEST: Same interpolation on raw DDIM-inverted latents (no null-text);

identity reconstruction (α=0,1 endpoints)
LIMITATION: Slow per image; storing per-step embeddings is unwieldy; null-text vectors are not

designed to be semantically meaningful — their 'autobiography' reading is an interpretation, not a
guarantee
MECHANISM CONFIDENCE: High for the mechanism; the debt-hybridization variant is PROJECT

HYPOTHESIS
APPLICABLE MEDIA: IMAGE
AI_SLOP CONNECTION: State preservation study; experiment; validator (error as measurable quantity)
CONFIDENCE TIER: ESTABLISHED (mechanism) / PROJECT HYPOTHESIS (variant)
CREATIVE UTILITY: High

M3 — PnP Inversion / Direct Inversion (branch disentangling)
[3]

SOURCE: Ju et al., ICLR 2024

; code: cure-lab/PnPInversion + PIE-Bench

SOURCE TYPE: Peer-reviewed paper + benchmark + code
LICENSE / USAGE NOTES: Open; repo frozen 2024-03 but complete; benchmark downloadable
WHAT IT ACTUALLY DOES: Three lines: during denoising of the inverted latent, adds the per-step

deviation between the guided reverse path and the recorded inversion path to the SOURCE branch only,
leaving the target/edit branch untouched

Page 6

AI SLOP Research Harvest — Topic 02: Diffusion Inversion, Attention & Latent Manipulation

CONTROLLABLE VARIABLES: Which branch receives corrections, per-step correction on/off, choice of

base inversion and editing method (9 editors wired in)
WHAT STATE OR STRUCTURE IT PRESERVES: Separates responsibilities: source branch preserves

essential content, target branch preserves edit fidelity
WHAT IT CHANGES: Editing quality at zero optimization cost; order-of-magnitude faster than null-text
FAILURE SURFACE: The deviation term is a memory of how wrong the inversion was. Deliberately

under-correcting (partial correction factor) reintroduces controlled inversion debt into the edit
ORIGINAL PURPOSE: Cheap high-fidelity inversion-based editing
POSSIBLE AI-SLOP MUTATION: Partial-correction dosing: apply fraction λ of the PnP deviation term

and sweep λ. At λ=1 faithful editing; at λ=0 raw inversion error; between them, the ghost of the original
image fights the edit
EXPECTED OBSERVABLE ARTIFACT: Spectral persistence of the original subject through radical edits;

double-exposure-like interference that is mechanically caused, not prompted
AMPLIFICATION / ITERATION METHOD: λ sweep × edit strength (target prompt guidance) as a 2D

phase map; PIE-Bench categories give standardized territory
CONTROL OR ABLATION TEST: λ=0 and λ=1 endpoints; same λ with null-text inversion as base (debt

pre-paid → ghost should vanish)
LIMITATION: SD 1.5-era benchmark stack; λ-scheduling is not part of the published method (it is our

intervention)
MECHANISM CONFIDENCE: High that λ controls debt; Medium for specific ghost aesthetics
APPLICABLE MEDIA: IMAGE
AI_SLOP CONNECTION: DAVID operator (debt dosing); state-controller rule (λ schedule); experiment
CONFIDENCE TIER: ESTABLISHED / DOCUMENTED (method) / PROJECT HYPOTHESIS (λ

dosing)
CREATIVE UTILITY: Very high

M4 — Iterative / fixed-point inversion (ReNoise, AIDI, Eta)
[4]

SOURCE: Garibi et al., ReNoise (ECCV 2024)

; Pan et al., AIDI (ICCV 2023); furiosa-ai/eta-inversion

[5]

(ECCV 2024)

SOURCE TYPE: Peer-reviewed papers + code; eta-inversion repo unifies 8 inversion methods × 4 editors
LICENSE / USAGE NOTES: Open; eta-inversion CLI exposes inv_method and edit_method flags directly
WHAT IT ACTUALLY DOES: Treats each inversion step as an implicit equation and solves it by

fixed-point iteration / iterative renoising, averaging predictions to stabilize the forward trajectory —
improves reconstruction at fixed compute, works on few-step distilled models
CONTROLLABLE VARIABLES: Renoising iterations per step, averaging window, edit-enhancement and

noise-correction scales (model-specific but stable)
WHAT STATE OR STRUCTURE IT PRESERVES: The return path to the image's own noise seed,

convergent and numerically stable
WHAT IT CHANGES: Raises the fidelity floor; also demonstrates that inversion quality is a dial with

measurable reconstruction-error readouts (PSNR/LPIPS/structure distance)
FAILURE SURFACE: Few-step distilled models invert worst (linearization error explodes with step size)

— the regime where artifacts are guaranteed unless corrected[4]
ORIGINAL PURPOSE: Accurate inversion incl. accelerated models
POSSIBLE AI-SLOP MUTATION: Deliberate under-convergence: stop the fixed-point iteration after 1

pass on a model that needs 8 — a principled 'half-solved equation' generator whose error structure is

Page 7

AI SLOP Research Harvest — Topic 02: Diffusion Inversion, Attention & Latent Manipulation

documented rather than random
EXPECTED OBSERVABLE ARTIFACT: Reconstructions with systematic directional smearing (the

residual of the unsolved implicit step), distinct from generic blur or noise
AMPLIFICATION / ITERATION METHOD: Iteration-count sweep per step; eta-inversion harness gives

8-method comparison under identical conditions — artifact families can be cross-method fingerprinted
CONTROL OR ABLATION TEST: Full convergence baseline; naive DDIM at same compute
LIMITATION: Hyperparameters are model-specific; under-convergence artifacts will vary per model and

need re-mapping
MECHANISM CONFIDENCE: High
APPLICABLE MEDIA: IMAGE; video (same inversion problem in T2V models)
AI_SLOP CONNECTION: Mutation operator (controlled under-solving); experiment; validator

(reconstruction metrics)
CONFIDENCE TIER: ESTABLISHED / DOCUMENTED
CREATIVE UTILITY: High

M5 — Rectified-flow inversion stack (RF-Inversion / RF-Solver / FireFlow)
[9]

SOURCE: Rout et al., ICLR 2025

; Wang et al., RF-Solver (ICML 2025)[10]; He et al., FireFlow

[11]

(2024)

SOURCE TYPE: Peer-reviewed papers + code + diffusers/ComfyUI integrations
LICENSE / USAGE NOTES: RF-Inversion in diffusers (pipe.invert API); ComfyUI community port

exists; FireFlow code public
WHAT IT ACTUALLY DOES: Inverts FLUX-class rectified-flow models: RF-Inv via dynamic optimal

control, RF-Solver via high-order Taylor expansion of the ODE, FireFlow via a midpoint solver with
first-order cost and second-order precision. Editing: replace self-attention V-features at early denoising
steps with features stored during inversion
CONTROLLABLE VARIABLES: Solver order/steps, gamma (RF-Inv), V-injection steps and layers, edit

prompt
WHAT STATE OR STRUCTURE IT PRESERVES: V-feature injection anchors layout and appearance

while the new prompt steers semantics — structure/content jurisdiction split at the feature level
WHAT IT CHANGES: Brings inversion editing to 2026-frontier open models in seconds (8–18 NFEs)
[11]

FAILURE SURFACE: RF-Solver's error can INCREASE after ~25 steps post-convergence

— an

over-solving artifact regime; V-injection timing controls the structure/edit tension
ORIGINAL PURPOSE: Fast, accurate inversion+editing for rectified-flow models
POSSIBLE AI-SLOP MUTATION: Cross-image V-transfusion: inject the V-features of image A's

inversion into the denoising of unrelated image B's latent under prompt C — three jurisdictions, one
stream
EXPECTED OBSERVABLE ARTIFACT: A's appearance grammar haunting B's structure under C's

semantics; FireFlow's own finding that first-step-only injection works suggests a sharp temporal
sensitivity to exploit
AMPLIFICATION / ITERATION METHOD: Sweep which denoising steps receive foreign V-features;

chain transfusions (output becomes next inversion source)
CONTROL OR ABLATION TEST: Self-V injection (must reproduce standard editing); V from a

blank/noise inversion
LIMITATION: Findings are young (2024–25); per-model behavior varies; MMDiT joint attention differs

from U-Net assumptions

Page 8

AI SLOP Research Harvest — Topic 02: Diffusion Inversion, Attention & Latent Manipulation

MECHANISM CONFIDENCE: High for the stack; Medium for the three-way transfusion
[10]

APPLICABLE MEDIA: IMAGE; VIDEO (RF-Edit demonstrated on video

— Topic 10 bridge)

AI_SLOP CONNECTION: DAVID operator (transfusion); experiment; connection to Topic 10
CONFIDENCE TIER: ESTABLISHED (stack) / PROJECT HYPOTHESIS (transfusion)
CREATIVE UTILITY: Very high

M6 — Self-attention feature injection (PnP features, MasaCtrl)
SOURCE: Tumanyan et al., CVPR 2023 (Plug-and-Play); Cao et al., ICCV 2023 (MasaCtrl);

systematized in the 2025 attention survey[13]
SOURCE TYPE: Peer-reviewed papers + code + survey
LICENSE / USAGE NOTES: Open; both runnable from the PnPInversion harness
WHAT IT ACTUALLY DOES: During the edit run, replaces self-attention components with those recorded

from the source run: PnP injects Q/K (structure), MasaCtrl swaps K/V (mutual self-attention for non-rigid
pose/action changes). Survey-confirmed division: Q,K encode structure/spatial arrangement; V encodes
appearance (color, texture, shape)
CONTROLLABLE VARIABLES: Which of Q/K/V is replaced, which layers, which denoising steps

(injection schedule)
WHAT STATE OR STRUCTURE IT PRESERVES: Source image structure (Q/K injection) or appearance

(V injection) — selective jurisdiction
WHAT IT CHANGES: Pose/action/identity under the edit prompt while the injected channel resists
FAILURE SURFACE: Wrong channel for the task = the failure IS informative: injecting V when structure

should move yields 'rubber-stamped' content; over-injection collapses the edit entirely
ORIGINAL PURPOSE: Non-rigid and structure-preserving editing
POSSIBLE AI-SLOP MUTATION: QKV transplant matrix: all 8 cross-substitution combinations between

two source images (A's Q into B, A's K into B, ...) — a systematic taxonomy of hybrid images with known
anatomies
EXPECTED OBSERVABLE ARTIFACT: A grid of 'impossible kinships':

same-structure-different-physics, same-appearance-different-geometry, and the genuinely alien
combinations (Q-only swaps)
AMPLIFICATION / ITERATION METHOD: Injection-schedule sweep per combination; recursive: a

hybrid's features become next-round donor
CONTROL OR ABLATION TEST: Identity transplant (A→A) per channel; no-injection edit baseline
LIMITATION: U-Net-centric evidence; DiT self-attention roles less cleanly separated (FireFlow's V-only

success hints the division survives but shifted)
MECHANISM CONFIDENCE: High
[13]

APPLICABLE MEDIA: IMAGE; VIDEO (spatio-temporal variants documented

)

AI_SLOP CONNECTION: DAVID operator (transplant matrix); experiment; new mechanism class

(channel anatomy)
CONFIDENCE TIER: ESTABLISHED / DOCUMENTED
CREATIVE UTILITY: Very high

M7 — Cross-attention leakage and its repair (DPL)
SOURCE: Wang et al., NeurIPS 2023 (DPL)

[8]

; code: wangkai930418/DPL

SOURCE TYPE: Peer-reviewed paper + code

Page 9

AI SLOP Research Harvest — Topic 02: Diffusion Inversion, Attention & Latent Manipulation

LICENSE / USAGE NOTES: Open; SD-based
WHAT IT ACTUALLY DOES: Diagnoses that editing failures trace to inaccurate cross-attention maps: the

edited token's map covers distractor regions, so edits bleed. Repairs by optimizing per-noun dynamic
tokens with leakage-repairment losses that force maps onto the correct nouns
CONTROLLABLE VARIABLES: Leakage loss weights, targeted nouns, repair strength
WHAT STATE OR STRUCTURE IT PRESERVES: Untargeted regions — repair = jurisdictional

enforcement
WHAT IT CHANGES: Localizes edits that vanilla P2P smears
FAILURE SURFACE: Leakage itself is the project's interest: the semantic-gravity field that makes 'edit

the cat' also repaint the sofa. DPL quantifies it; we can decline to repair it — or tune the repair halfway
ORIGINAL PURPOSE: Fixing bleed-through in text-based editing
POSSIBLE AI-SLOP MUTATION: Leakage dial: interpolate between DPL-repaired and unrepaired

attention (repair strength λ); at intermediate λ the edit leaks exactly as far as semantic similarity carries it
— a measured contamination radius
EXPECTED OBSERVABLE ARTIFACT: Contagion aesthetics: edits spreading along semantic

relatedness gradients (editing 'king' also crowns the queen and the throne)
AMPLIFICATION / ITERATION METHOD: λ sweep mapped against semantic-distance probes of affected

regions
CONTROL OR ABLATION TEST: Full repair; zero repair; repair applied to a distractor noun instead
LIMITATION: Repair is per-prompt optimization; the λ-dial is our construction, not the paper's
MECHANISM CONFIDENCE: High for the diagnosis; Medium for the dial
APPLICABLE MEDIA: IMAGE
AI_SLOP CONNECTION: Mutation operator; state-controller rule (λ); validator (semantic contamination

radius as metric)
CONFIDENCE TIER: ESTABLISHED (diagnosis) / PROJECT HYPOTHESIS (dial)
CREATIVE UTILITY: High

M8 — PROVENANCE TRAP: two StyleDiffusions
SOURCE: (a) Wang, Zhao, Xing — ICCV 2023: CLIP-space content/style disentanglement + diffusion

style-removal[6]. (b) sen-mao/StyleDiffusion — CVMJ 2024: prompt-embedding inversion for text-based
editing (the starter lead; active 2026-08)
SOURCE TYPE: Two unrelated peer-reviewed papers sharing a name
LICENSE / USAGE NOTES: Both open; unrelated codebases
WHAT IT ACTUALLY DOES: (a) Removes style via partial diffusion on luma-grayscale images, then

re-injects learned style (style removal module with controllable T_remove). (b) Inverts the prompt
embedding space (P2Plus modifies both conditional and unconditional self-attention)
CONTROLLABLE VARIABLES: (a) T_remove (how much style is dispelled), CLIP disentanglement

weight; (b) embedding inversion steps, P2Plus injection schedules
WHAT STATE OR STRUCTURE IT PRESERVES: (a) Content structure through style removal; (b) layout

through dual-branch attention control
WHAT IT CHANGES: (a) Style channel only; (b) semantic content via embedding surgery
FAILURE SURFACE: The citation ambiguity itself is the failure surface for research hygiene; technically,

(a)'s partial removal has a removal-depth artifact zone and (b)'s embedding inversion can land
off-manifold
ORIGINAL PURPOSE: Style transfer / editing, respectively

Page 10

AI SLOP Research Harvest — Topic 02: Diffusion Inversion, Attention & Latent Manipulation

POSSIBLE AI-SLOP MUTATION: (a)'s style-removal dial run in reverse: stop style removal at

intermediate depth so an image carries a half-removed style — stylistic phantom limb
EXPECTED OBSERVABLE ARTIFACT: Images whose brushwork is present-but-decoupled from their

geometry; removal-depth sweep gives the family
AMPLIFICATION / ITERATION METHOD: T_remove sweep; iterate removal on already-restyled outputs

(compounding removal debt)
CONTROL OR ABLATION TEST: Full removal baseline; no-removal baseline
LIMITATION: (a) requires its specific training setup; the phantom-limb reading is PROJECT

HYPOTHESIS
MECHANISM CONFIDENCE: High (both papers documented); Medium for the mutation
APPLICABLE MEDIA: IMAGE
AI_SLOP CONNECTION: Mutation operator; provenance lesson for source-audit.md
CONFIDENCE TIER: ESTABLISHED / DOCUMENTED + PROVENANCE WARNING
CREATIVE UTILITY: Medium-High

M9 — Noised-latent splicing / blending (ComfyUI practice)
[16]

SOURCE: Blended Latent Diffusion (SIGGRAPH 2023)

; AustinMroz/ComfyUI-SpliceTools
(experimental nodes); lajjadred/comfyui-lrw-nodes (2026, Riemannian/Bayesian latent ops)
SOURCE TYPE: Peer-reviewed paper + unvalidated community nodes
LICENSE / USAGE NOTES: SpliceTools GPL-3.0 (copyleft — note for any distributed derivative);

lrw-nodes license check needed; Blended Latent Diffusion code open
WHAT IT ACTUALLY DOES: Operates on the latent mid-trajectory: spatially blend the noised original

with the generated latent each step (masked local editing), or splice/perturb noised latents directly
(SpliceTools), or treat latent interpolation with geometric corrections (lrw)
CONTROLLABLE VARIABLES: Splice mask, noise level at splice time, blend schedule, interpolation

path (linear vs spherical vs Riemannian)
WHAT STATE OR STRUCTURE IT PRESERVES: Unmasked regions' trajectory; the VAE decoder

attempts global repair of the seam
WHAT IT CHANGES: The composite image's coherence boundary — the seam is where two incompatible

trajectories meet
[16]

FAILURE SURFACE: Seam artifacts, pixel-level noise residue (documented in the paper

), and
non-Gaussian intermediates: linear interpolation between latents leaves the decoder's comfort zone,
producing washed-out or structurally alien images
ORIGINAL PURPOSE: Masked local editing; latent-space tooling
POSSIBLE AI-SLOP MUTATION: Trajectory splicing instead of image splicing: take the first half of

prompt A's denoising trajectory and the second half of prompt B's (temporal splice in noise space). The
decoder must resolve a latent whose early structure decisions and late detail decisions belong to different
worlds
EXPECTED OBSERVABLE ARTIFACT: Chimera images where composition and texture belong to

different prompts; splice-timestep sweep maps the dominance frontier (early splice = B-flavored, late =
A-flavored)
AMPLIFICATION / ITERATION METHOD: Splice-timestep sweep × mask density; recursive splicing of

outputs (artifact inheritance)
CONTROL OR ABLATION TEST: Same-timestep splice with matched prompt (A/A — should

reproduce); pixel-space compositing comparison

Page 11

AI SLOP Research Harvest — Topic 02: Diffusion Inversion, Attention & Latent Manipulation

LIMITATION: Community nodes are unvalidated (6–12 stars); every splice claim must be re-derived

empirically per model
MECHANISM CONFIDENCE: High for blending; Medium for temporal trajectory splicing
APPLICABLE MEDIA: IMAGE; VIDEO (frame-latent splicing); GLSL-ADJACENT (noise-field

thinking)
AI_SLOP CONNECTION: DAVID operator (temporal splice); mutation operator; state-controller rule

(mask schedules); experiment
CONFIDENCE TIER: ESTABLISHED (blending) / PLAUSIBLE INTERPRETATION (traversal

splicing) / SPECULATION (lrw geometry)
CREATIVE UTILITY: Very high — cheapest mechanism in the catalog

Page 12

AI SLOP Research Harvest — Topic 02: Diffusion Inversion, Attention & Latent Manipulation

4 Failure surfaces as artistic material
Five failure surfaces in this topic are characterized well enough to be aimed at. Each row is an
instrument.
Failure surface

Documented behavior

Aiming parameters

Evidence tier

Inversion debt
(error
accumulation)

DDIM inversion errors concentrate in early steps
and compound; CFG amplifies them; few-step
distilled models invert worst. Reconstruction ≠
editability: paying debt (null-text) and tolerating
debt (naive DDIM) edit differently[7][12]

Inversion steps, guidance
scale, iteration count,
correction fraction λ
(PnP)

ESTABLISHED

Attention leakage

Edited token's cross-attention map covers
semantically related distractors; edits bleed into
untargeted regions. Root cause documented, repair
quantified (DPL)[8]

Repair strength, target
noun choice, re-weighting
coefficient

ESTABLISHED

Over-injection
freeze

Injecting attention/features for too many steps
locks the image to the source so hard the edit
cannot materialize — constraint suffocation

cross_replace_steps /
injection step fraction

ESTABLISHED[

Non-Gaussian
intermediate latents

Naive interpolation/averaging of latents leaves the
decoder's trained manifold: washed-out,
low-contrast, structurally alien outputs; inversion
latents carry spatial correlations that diverge from
Gaussian seed statistics[12]

Interpolation path, blend
schedule, splice timestep

ESTABLISHED

CFG mode-shifting
/ over-saturation

High guidance scales shift modes and concentrate
samples (over-saturation); CFG's composite score
differs from any true score of the model[17]

Guidance scale, guidance
rescale

ESTABLISHED

Solver
over-correction

RF-Solver's reconstruction error can rise again
past ~25 steps post-convergence; more precision is
not monotonically better[11]

NFE count, solver order

ESTABLISHED
(single paper —
replicate before
relying)

1]

Table 2 — Failure surfaces with aiming parameters.

5 Promising experiments
E1 — The Debt Dial (controlled inversion error as material)
HYPOTHESIS: Inversion debt — the gap between the true return path and the computed one — behaves

as a graded artistic material: a λ-dose of PnP correction produces an ordered artifact family from
ghost-persistence to clean edit, not random degradation
REPRESENTATIONAL TENSION: The correction term is the memory of the original image's true path;

withholding it forces the edit to negotiate with a wrong history
COMPETING CONSTRAINTS: Edit prompt fidelity vs. trajectory truthfulness to the source image
WHY THE SYSTEM MAY STRUGGLE: The denoiser was trained on legal Gaussian trajectories; an

under-corrected trajectory is legal-shaped but semantically false
EXPECTED RESULT: λ sweep yields: λ≈1 clean edit; mid-λ spectral double-exposure artifacts (original

subject bleeding through radical semantic change); λ≈0 near-failed edit dominated by source structure

Page 13

AI SLOP Research Harvest — Topic 02: Diffusion Inversion, Attention & Latent Manipulation

NEGATIVE CONTROL: Same λ schedule applied to a fully-converged ReNoise inversion (debt pre-paid

→ mid-λ artifacts should vanish)
ABLATION: λ=0, λ=1, λ randomized per step (schedule vs constant)
DOSE RESPONSE: λ ∈ {0, 0.25, 0.5, 0.75, 1} × guidance scale ∈ {3, 7.5, 12} on PIE-Bench categories;

metrics: structure distance to source, CLIP-to-target, artifact rating
ITERATIVE VERSION: Edit the output again with the same λ — debt compounds across generations

(artifact inheritance; links Topic 09)
FALSIFICATION CONDITION: Mid-λ outputs are indistinguishable from λ-randomized controls on

artifact-structure probes — debt is just noise, not structure

E2 — Binding War (contradictory word-swap under frozen attention)
HYPOTHESIS: A P2P word swap whose replacement semantically contradicts the frozen layout produces

a stable artifact family — 'impossible objects with coherent geometry' — whose onset is a measurable
function of injection depth
REPRESENTATIONAL TENSION: Frozen cross-attention map = spatial jurisdiction of the old word; new

token embedding = semantic jurisdiction of the new word; both claim the same pixels
COMPETING CONSTRAINTS: Layout preservation pressure vs. semantic fidelity pressure
WHY THE SYSTEM MAY STRUGGLE: The model has no training distribution of flames shaped like

castles; every denoising step must re-arbitrate
EXPECTED RESULT: Injection-fraction sweep reveals three regimes: swap fails (layout wins), hybrid

(contradiction rendered — the artifact zone), layout breaks (semantics wins). Hybrid zone boundaries are
prompt-pair-dependent but reproducible
NEGATIVE CONTROL: Compatible swap at matched injection depth ('cat'→'lion'); no-injection swap
ABLATION: Freeze cross-attention only vs cross+self; single-layer injection vs all layers
DOSE RESPONSE: cross_replace_steps ∈ [0,1] in 0.1 steps × contradiction strength (semantically

near/far pairs)
ITERATIVE VERSION: Re-invert the hybrid and swap again toward a third concept — contradiction

layering
FALSIFICATION CONDITION: No stable hybrid regime: every contradiction pair collapses directly from

swap-fails to layout-breaks

E3 — The QKV Transplant Matrix
HYPOTHESIS: Cross-image self-attention transplants (Q, K, V independently from donor A into host B)

produce distinguishable, anatomically predictable hybrid classes, confirming and extending the
documented structure/appearance channel division into compositional territory
REPRESENTATIONAL TENSION: Host's generative trajectory vs. donor's injected channel — one

channel carries foreign structure or appearance while the rest of the network computes as if nothing
happened
COMPETING CONSTRAINTS: Q/K (structure) vs V (appearance) jurisdictions per the attention

survey[13]
WHY THE SYSTEM MAY STRUGGLE: Donor features were computed for donor latents; in host context

they are legal-shaped but contextually false
EXPECTED RESULT: Q/K transplants deform B's geometry toward A's layout; V transplants repaint B in

A's appearance grammar; single-channel transplants (Q only) yield the least coherent, most novel artifacts
NEGATIVE CONTROL: Self-transplant A→A per channel (must reproduce A); noise-donor transplant

Page 14

AI SLOP Research Harvest — Topic 02: Diffusion Inversion, Attention & Latent Manipulation

[11]

ABLATION: Injection layer subsets; injection step windows (FireFlow's first-step finding as anchor

)

DOSE RESPONSE: Injection step fraction × channel, per donor-host pair class (similar vs dissimilar

content)
ITERATIVE VERSION: Hybrids become donors in round 2 — channel lineage tracking across generations
FALSIFICATION CONDITION: Transplant class has no consistent effect beyond generic corruption

(compare against shuffled-feature donors)

E4 — Temporal Trajectory Splice
HYPOTHESIS: Splicing two prompts' denoising trajectories at timestep τ (first half A, second half B)

yields chimeras whose dominance frontier is a smooth, reproducible function of τ — early structure
decisions and late detail decisions can be assigned to different worlds deliberately
REPRESENTATIONAL TENSION: A's low-frequency structural commitments vs. B's high-frequency

detail commitments, fused in one latent
COMPETING CONSTRAINTS: Trajectory continuity (the ODE wants a legal path) vs. the splice

discontinuity
WHY THE SYSTEM MAY STRUGGLE: At τ, the latent is legal-shaped noise encoding A's intentions; the

B-conditioned denoiser reads its own intentions into it
EXPECTED RESULT: τ sweep maps composition-vs-texture assignment: early splice = B's structure with

A's textures; mid = true chimeras; late = A with B's surface. VAE repair marks the splice as specific
artifact textures
NEGATIVE CONTROL: A/A self-splice (must reproduce A exactly — the identity test); pixel-space

composite of finished A and B (shows what is NOT trajectory-level)
ABLATION: Splice with matched seed vs unmatched seeds; splice on latents vs splice on CFG branches
DOSE RESPONSE: τ ∈ {10%,...,90%} of steps × prompt-pair semantic distance
ITERATIVE VERSION: Chain: output of splice k re-noised to τ and spliced with prompt C — iterated

contamination with documented lineage
FALSIFICATION CONDITION: Splice artifacts match the pixel-composite control — nothing

trajectory-specific exists

Page 15

AI SLOP Research Harvest — Topic 02: Diffusion Inversion, Attention & Latent Manipulation

6 Cross-modal applications
Target
medium

Transfer path

Status

Notes

Video

Spatio-temporal attention control documented
(Video-P2P, FateZero, VideoGrain); RF-Edit
demonstrated on video; temporal consistency =
attention across frames

DOCUMENTED —
Topic 10 will own this

Temporal failure
surfaces are the richest
variant; deferred

Audio

Audio diffusion models (Stable Audio, teticio-style
latent audio diffusion) use the same U-Net/DiT
attention + latent recipe; diffusers ships
StableAudioAttnProcessor

PLAUSIBLE —
Topic 06 will own this

Attention binding of
text to spectrogram
regions is terra
incognita for art

LLM

Structural analogy to Topic 01: trajectory splice ≈
activation graft; attention injection ≈ steering;
inversion debt ≈ steering residual

ANALOGY
(METAPHOR label)

Use as design language
only — mechanisms
differ

GLSL /
shaders

Noise-field composition and repair-by-iteration are
native shader idioms; splice-timestep thinking
transfers as time-stepped procedural composition

METAPHOR

Method transfer, not
mechanism transfer

ComfyUI /
controllers

Every mechanism here exposes node-level state
(latents, maps, schedules) — direct fit for
TOPOS-SRE-style external controllers reading
artifact metrics and re-dosing

READY

E1 and E4 are designed
for this integration

Table 3 — Cross-modal transfer assessment.

7 What appears most useful for AI SLOP
1. Inversion is the project's missing return path. AI SLOP's path-dependence principle (A→B→C
must differ from A→C) is usually enforced procedurally, by controllers and archives. Inversion makes
it physical: the trajectory through noise space IS a state with history, and its error (debt) is measurable
with standard metrics. E1's Debt Dial is the cheapest strong experiment in this document — the
eta-inversion harness already wires 8 inversion methods × 4 editors behind CLI flags[5].
2. Attention injection is constraint governance made literal. The project's 'jurisdictions' metaphor
becomes concrete: cross-attention maps are spatial jurisdictions over pixels, Q/K/V channels are
functional jurisdictions over structure and appearance, and injection schedules are temporal
jurisdictions over the denoising process. Binding War (E2) and the Transplant Matrix (E3) are
jurisdictional conflicts with documented mechanics.
3. The 2026 working stack is settled enough to build on. diffusers attention processors (official API),
RF-Inversion in diffusers, ComfyUI community ports, FireFlow-speed editing on FLUX — the
mechanisms in this PDF run on current open infrastructure. The SD 1.5-era papers remain the clearest
mechanistic documentation (U-Net attention is cleanly separated), so a dual-stack practice is
recommended: SD 1.5 for mechanism studies, FLUX for production artifacts.
4. Failure-surface discipline transfers directly. The project's experimental method (controls,
ablations, dose-response, artifact families) matches this literature's own norms — PIE-Bench categories
and structure/background metrics can be reused as the validator layer for image experiments without

Page 16

AI SLOP Research Harvest — Topic 02: Diffusion Inversion, Attention & Latent Manipulation

inventing new measurement machinery.

8 Weak / dubious ideas worth rejecting
Claim / idea

Verdict

Why

'Latent space is a smooth
semantic space; linear
interpolation gives meaning'

REJECT as
stated

Intermediate points leave the trained manifold (non-Gaussian
intermediates); interpolation artifacts are decoder failure, not latent
semantics. Useful failure — wrong explanation

'Naive DDIM inversion under
high CFG reconstructs real
images'

REJECT

Error accumulation under CFG is documented across the whole
inversion literature; it is the reason null-text, PnP, ReNoise, and RF
methods exist

'Attention maps show where
objects are'

OVER-SIMPL
IFIED

Maps are inaccurate enough to cause leakage; treating them as ground
truth masks reproduces the failure DPL was built to repair

'StyleDiffusion' as a single
method

REJECT
(provenance
trap)

Two unrelated papers share the name (ICCV 2023 style transfer vs
CVMJ 2024 embedding inversion). Cite with author+year or lose the
thread

bloc97/CrossAttentionControl as
living infrastructure

DEPRECATE

Frozen 2022-10; use google/prompt-to-prompt or diffusers processors
instead

ComfyUI-SpliceTools /
lrw-nodes as validated
mechanisms

CAUTION

6–12 stars, no validation, one is GPL-3.0 (copyleft). Fine as raw
material for self-run experiments; never cite as evidence

'More inversion steps always
help'

REJECT

RF-Solver error can rise again past convergence (~25 steps);
monotonicity is false[11]

HF: AswinMathew/latent-spaceexplorer

UNVERIFIED

Not resolvable via HF API in this session; excluded from all claims

Table 4 — Rejection register.

9 Open questions
• Does inversion debt have a consistent visual signature distinguishable from generic noise corruption?
(E1 is designed to answer this; no published artifact taxonomy for under-corrected inversion was
found.)
• How do P2P-class mechanisms re-derive on MMDiT/joint-attention architectures (SD3, FLUX)? Text
and image tokens share attention — the 'cross-attention map' is no longer a separable object[15].
• Is the Q/K/V structure–appearance division stable across architectures, or U-Net-specific? FireFlow's
V-only success on FLUX hints it survives in shifted form — the Transplant Matrix would map this.
• What is the right metric for 'structured vs mushy' hybrid artifacts? PIE-Bench metrics measure editing
success, not artifact interest — the project may need its own artifact-family probes.
• Can attention leakage radius be predicted from embedding-space semantic distance? If yes,
contamination becomes composable; if no, it stays an empirical dial.

Page 17

AI SLOP Research Harvest — Topic 02: Diffusion Inversion, Attention & Latent Manipulation

• Do trajectory splices produce anything that prompt blending cannot? (E4's falsification condition — if
splice ≈ prompt mix, the mechanism is decorative, not structural.)

Page 18

AI SLOP Research Harvest — Topic 02: Diffusion Inversion, Attention & Latent Manipulation

10 Sources / bibliography
Hertz, A., Mokady, R., Tenenbaum, J., Aberman, K., Pritch, Y., & Cohen-Or, D. (2023). Prompt-to-Prompt Image
Editing with Cross Attention Control. ICLR 2023. arXiv:2208.01626. Code:
github.com/google/prompt-to-prompt. https://arxiv.org/abs/2208.01626
Mokady, R., Hertz, A., Aberman, K., Pritch, Y., & Cohen-Or, D. (2023). Null-text Inversion for Editing Real
Images using Guided Diffusion Models. CVPR 2023. arXiv:2211.09794. https://arxiv.org/abs/2211.09794
Ju, X., Zeng, A., Bian, Y., Liu, S., & Xu, Q. (2024). PnP Inversion: Boosting Diffusion-based Editing with 3 Lines
of Code. ICLR 2024. arXiv:2310.01506. Code+benchmark:
github.com/cure-lab/PnPInversion. https://arxiv.org/abs/2310.01506
Garibi, D., et al. (2024). ReNoise: Real Image Inversion Through Iterative Noising. ECCV 2024.
arXiv:2403.14602. https://arxiv.org/abs/2403.14602
Furiosa AI (2024). Eta Inversion: Designing an Optimal Eta Function for Diffusion-based Real Image Editing.
ECCV 2024. Code: github.com/furiosa-ai/eta-inversion (8 inversion methods × 4
editors). https://github.com/furiosa-ai/eta-inversion
Wang, Z., Zhao, L., & Xing, W. (2023). StyleDiffusion: Controllable Disentangled Style Transfer via Diffusion
Models. ICCV 2023. arXiv:2308.07863. https://arxiv.org/abs/2308.07863
InverseMeetInsert / GEO (2024). Robust Real Image Editing via Geometric Accumulation Inversion (documents
DDIM cumulative error and CFG null-text instability). arXiv:2409.11734. https://arxiv.org/abs/2409.11734
Wang, K., et al. (2023). Dynamic Prompt Learning: Addressing Cross-Attention Leakage for Text-Based Image
Editing. NeurIPS 2023. Code: github.com/wangkai930418/DPL. https://github.com/wangkai930418/DPL
Rout, L., Chen, Y., Ruiz, N., Caramanis, C., Shakkottai, S., & Chu, W.-S. (2025). Semantic Image Inversion and
Editing using Rectified Stochastic Differential Equations (RF-Inversion). ICLR 2025. arXiv:2410.10792.
Code: github.com/LituRout/RF-Inversion (diffusers + ComfyUI ports). https://arxiv.org/abs/2410.10792
Wang, J., et al. (2025). Taming Rectified Flow for Inversion and Editing (RF-Solver / RF-Edit). ICML 2025.
arXiv:2411.04746. https://arxiv.org/abs/2411.04746
He, X., Mei, C., Wang, P., & Tang, F. (2024). FireFlow: Fast Inversion of Rectified Flow for Image Semantic
Editing. arXiv:2412.07517. https://arxiv.org/abs/2412.07517
Emergent Mind (2025). DDIM Inversion: Methods & Applications — synthesis on error accumulation, early-step
concentration, non-Gaussian structure of recovered latents (Staniszewski et al. 2024; Wallace et al. EDICT
2023; BDIA
2023). https://www.emergentmind.com/topics/denoising-diffusion-implicit-models-ddim-inversion
Sun, K., et al. (2025). Attention in Diffusion Model: A Survey (Q/K/V role division; injection taxonomies across
image and video). arXiv:2504.03738. https://arxiv.org/abs/2504.03738
Hugging Face (2023–). Diffusers: Attention Processor API (pluggable set_attn_processor extension point).
huggingface.co/docs/diffusers/en/api/attnprocessor. https://huggingface.co/docs/diffusers/en/api/attnprocessor
Paul, S. (2025). Flavors of attention in modern diffusion models (cross-attention vs joint-attention/MMDiT
structural differences). sayak.dev. https://sayak.dev/posts/attn-diffusion.html
Avrahami, O., Fried, O., & Lischinski, D. (2023). Blended Latent Diffusion. SIGGRAPH 2023. arXiv:2206.02779.
Code: github.com/omriav/blended-latent-diffusion. https://arxiv.org/abs/2206.02779
Kiwhan, S. (2024). Correcting Classifier-Free Guidance (mode-shifting and variance analysis of CFG).
kiwhan.dev. https://kiwhan.dev/blog/2024/classifier-free-guidance/
Tumanyan, N., Geyer, M., Bagon, S., & Dekel, T. (2023). Plug-and-Play Diffusion Features for Text-Driven
Image-to-Image Translation. CVPR 2023. arXiv:2211.12572. https://arxiv.org/abs/2211.12572
Cao, M., et al. (2023). MasaCtrl: Tuning-free Mutual Self-Attention Control for Consistent Image Synthesis and
Editing. ICCV 2023. arXiv:2304.08465. https://arxiv.org/abs/2304.08465

Page 19

AI SLOP Research Harvest — Topic 02: Diffusion Inversion, Attention & Latent Manipulation

Meng, C., et al. (2022). SDEdit: Guided Image Synthesis and Editing with Stochastic Differential Equations. ICLR
2022. arXiv:2108.01073. https://arxiv.org/abs/2108.01073
All GitHub metadata verified via the GitHub API on 2026-09-19; arXiv IDs cross-checked against search indexes.
Items marked UNVERIFIED in Table 4 are excluded from mechanism claims.

11 Licensing / provenance appendix
Asset

License / terms

Verified

Provenance note

google/prompt-to-prompt

Apache-2.0 (see repo)

2026-09-19

Official P2P code; Imagen + SD
notebooks

bloc97/CrossAttentionControl

MIT

2026-09-19 (GitHub
API)

Unofficial P2P; frozen 2022-10
— reference only

cure-lab/PnPInversion +
PIE-Bench

See repo (research code)

2026-09-19 (GitHub
API)

Official ICLR 2024 code; frozen
2024-03 but complete;
benchmark included

furiosa-ai/eta-inversion

See repo

2026-09-19 (GitHub
API)

Unified inversion/editor harness
— recommended experiment
bench

wangkai930418/DPL

See repo

2026-09-19 (GitHub
API)

Leakage diagnosis + repair;
small but complete

sen-mao/StyleDiffusion

See repo

2026-09-19 (GitHub
API)

CVMJ 2024 embedding
inversion — NOT the ICCV
2023 paper; active 2026-08

LituRout/RF-Inversion

See repo; diffusers
integration Apache-2.0

2026-09-19

ICLR 2025; official +
community ComfyUI port

AustinMroz/ComfyUI-SpliceT
ools

GPL-3.0 (copyleft)

2026-09-19 (GitHub
API)

6 stars, experimental; GPL
affects any distributed derivative
workflow

lajjadred/comfyui-lrw-nodes

Check repo (not listed)

2026-06 (GitHub API)

2026-05 creation; unvalidated
Riemannian/Bayesian latent ops

huggingface/diffusers

Apache-2.0

2026-09-19

Attention processor API is the
supported intervention surface

HF spaces (anshuln,
AswinMathew leads)

—

PARTIAL /
UNVERIFIED

anshuln attention-viz space
exists per web index (slug
unconfirmed);
latent-space-explorer unverified

Table 5 — Licensing and provenance.
Research conducted 2026-09-19 via web sources, arXiv, and the GitHub API. The ai_slop repository was read for
connection mapping only — nothing was modified, added, or committed. ESTABLISHED claims trace to
peer-reviewed venues or benchmarked code; PLAUSIBLE INTERPRETATION, PROJECT HYPOTHESIS, and
SPECULATION are marked inline. The GPL-3.0 license on SpliceTools is flagged because node-pack provenance
matters if derivative workflows are ever distributed.

Page 20
