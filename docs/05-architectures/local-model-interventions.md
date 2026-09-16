# Local / Open-Model Intervention Track

This track is distinct from prompt-only semantic simulation.

If the user wants to manipulate actual hidden activations, logits, or weights, a model and inference stack under local/research control is required. Closed consumer chat/image/music APIs generally do not expose arbitrary intermediate tensors.

## Real intervention classes worth researching

### Activation steering
Construct and inject direction vectors into selected layer activations, then measure how outputs change with layer and coefficient.

**Caution:** a contrast vector is not automatically a clean human concept. Steering effects can be distributed, nonlinear, layer-specific, and entangled.

### Logit manipulation
Bias or mask token probabilities at generation time when the inference API exposes logits.

**Caution:** suppressing a token is not equivalent to deleting a concept; alternative wording may preserve the same semantics.

### Weight/model editing
Methods such as rank-one or other targeted editing can alter model behavior/factual associations.

**Caution:** claims like “the fact lives in this exact weight” are oversimplified. Evaluate locality, generalization, and collateral effects.

### Representation probing / visualization
Collect hidden states, project them with PCA/UMAP/t-SNE or train probes/autoencoders to inspect structure.

**Caution:** the visualization is a projection/model of representation, not the representation’s literal shape. Neighbor relations can distort under dimensionality reduction.

### Hook-based perturbation
For open transformer stacks, hooks can intercept and modify activations between layers, permitting controlled intervention experiments.

## How this differs from Semantic Manifold Game

- **Semantic Manifold:** external conceptual state and embeddings; model used as interpreter/compiler.
- **Local intervention:** actual inference internals are instrumented and perturbed.

Both can be fun. Do not conflate them.

## Safety/ethics framing

The archived source frames local control as a way to “strip safety guardrails.” That is not the canonical research objective. The useful objective is **mechanistic art/research**: how representation and generation change under controlled interventions in models you are authorized to run and inspect.

Primary source: `ai_readable/semantic_systems/02-weight-manipulation.md`.
