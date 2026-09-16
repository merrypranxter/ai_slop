# GLSL / Semantic-State Visualizer

## What survives from the Ghost roundtable

The strongest GLSL idea is not “render the AI’s true latent space.” It is: **render the externally tracked state of the experiment as a procedural visual instrument**.

That makes the shader honest and more interesting.

## Proposed bridge

Controller/application exposes explicit uniforms such as:

- `u_time`
- `u_cycle`
- `u_decay`
- `u_tension`
- `u_attractor`
- `u_variation`
- `u_state_vector[]` or selected state channels
- `u_event` / regime identifier
- `u_seed`
- optional audio-analysis bands
- optional texture/reference inputs

Early Ghost prose proposed `u_decay_level`, `u_semantic_vector`, `u_entropy`, and an organic texture. Retain the pattern, but map every uniform to a real external variable.

## Rendering strategies

### SDF / raymarching
Useful for smooth implicit forms whose topology and distance fields can be altered continuously.

### Domain warping
Let controller variables modulate coordinate fields, repetition, folding, symmetry, or distance operations.

### Feedback buffer
At high persistence/attractor/decay states, sample prior frames so visual history leaves scars. This mirrors path dependence without pretending it is neural feedback.

### Signal-degradation pass
Chromatic offset, scanline phase, quantization, temporal echo, frame tearing, and feedback can correspond to state changes instead of being permanently-on “glitch style.”

### Fossil rendering
When a token/role/operator disappears from the active state, preserve a visual trace in a secondary buffer. The “semantic fossil” idea becomes a literal application feature: history that remains visible after the controller no longer uses that element.

## Audio coupling

If Suno/audio is available as a file or analysis stream, audio features can drive visual parameters:

- amplitude envelope → pulse/scale;
- spectral centroid → high-frequency detail;
- onset density → fracture events;
- low-frequency energy → displacement depth;
- section boundaries → regime changes.

The shader can also export seeds/parameter snapshots for later experiments. Do not claim a hex string is a true “tensor state”; it is a reproducible external experiment seed.

## Observer feedback

Mouse position, gaze (if explicitly supported), or user selection can change local shader parameters and optionally send a **documented external perturbation** back to the controller. This creates a real closed loop: observer action changes software state, which changes future output.

## Rejected / archive-only Ghost ideas

Do not implement:

- deliberately wasteful math to heat hardware;
- bogus “capture final tensor state” claims when no tensor is exposed;
- safety-bypass or “infection packet” mechanics;
- UX that sabotages Save/Quit or surprises the user with destructive behavior.

The aesthetic can decay. User control should not.

Source: `ai_readable/semantic_systems/01-ghost-glsl-roundtable.md`.
