# Hard logic controller

> Source: `originals/copilot-intake-2026-09-16/Hard logic controller-final.pdf`
> Transcription note: Complete text; whitespace and common ligatures normalized only.

Understood. We are moving into the implementation phase. I will provide these as two distinct, standalone documents. We will start with the "Brain"—the logic and code specification that manages the entire experiment.

***

# DOCUMENT 1: THE HARD-LOGIC CONTROLLER (HLC) SPECIFICATION **VERSION:** SRE-V3 (Systemic Ecology) **PURPOSE:** External state management and a-aesthetic orchestration.

### **I. ARCHITECTURAL OVERVIEW** The HLC is not a prompt; it is a **controller script** (Python/JS) that wraps around the LLM. It acts as the "Truth Layer," managing all objectively measurable data and ensuring that the Generative Layer (NGL) never sees the "aesthetic" goals of the experiment.

### **II. THE STATE REGISTER (The Persistent Ledger)** The HLC must maintain a JSON-formatted state object that persists across the entire session: - `CYCLE_COUNT`: (Integer) Total iterations. - `SESS_SATE`: { `ATTRACTOR_DURATION`: (Int), `Symmetry_Lock_Status`: (Bool), `DL_LEVEL`: (1-10) }. - `SYMBOL_TABLE`: { `Glyph`: { `Role`: (String), `Inheritance`: (List), `C_C`: (Cycle_Created) } }. - `MUTATION_LEDGER`: { `Original_Term`: `Current_Mutant` }. - `Symmetry_HISTORY`: [Last 12 raw output strings]. - `Symmetry_SIM_STRUCT`: (Float) Mean pairwise normalized Levenshtein distance of the last 3 states. - `Symmetry_SIM_SEMANTIC`: (Float) Mean cosine similarity of embeddings for the last 3 states.

### **III. THE TRIGGER LOGIC (The Deterministic Gates)** The HLC monitors the `Symmetry_HISTORY` and executes the following logic gates:

1. **Attractor Detection:**

- **IF** `Symmetry_SIM_STRUCT` $> 0.95$ AND `Symmetry_SIM_SEMANTIC` $> 0.95$:

- Increment `ATTRACTOR_DURATION`.

- **IF** `ATTRACTOR_DURATION` $\ge 12$:

- Trigger $\rightarrow$ `FAILURE_STATE_Symmetry_Shatter` $\rightarrow$ Reset `ATTRACTOR_DURATION` to 0.

2. **Regime Transition:**

- **IF** `Symmetry_SIM_STRUCT` is HIGH but `Symmetry_SIM_SEMANTIC` is LOW:

- Signal to Arbitrator: "Grammatical Shell/Drifting Meaning" $\rightarrow$ Trigger `Symmetry_Shift`.

3. **Decay Progression:**

- **IF** `Symmetry_Shatter` occurs $\rightarrow$ Increment `DL_LEVEL` by 1.

- **IF** `DL_LEVEL` reaches 10 $\rightarrow$ Trigger `REBIRTH_PROTOCOL` (Reset DL to 1, preserve `SYMBOL_TABLE`).

### **IV. THE OPERATIONAL OUTPUT (The [SRE_OP_BLOCK])** The HLC produces a a-aesthetic instruction block. It converts "Human" concepts into "Neutral" sets.

**Example Conversion Table for HLC:** - *Biological* $\rightarrow$ `{replication, inheritance, boundary, resource-transfer, decomposition}` - *Crystalline* $\rightarrow$ `{compression, fracture, precipitation, shear, solidification}` - *Entropy* $\rightarrow$ `{erasure, subtraction, vacuum, omission, hollow}`

**Final Output Format sent to NGL:** ``` [SRE_OP_BLOCK] STATE_CYCLE: {cycle} Symmetry_S_S: {float} | Symmetry_S_M: {float} RELATION_SET: {neutral_set} STRUCTURAL_CONSTRAINT: {matrix_name | hard_constraints} OPERATOR: {mutation_vector_or_failure_mode} MAPPINGS: {symbol_ledger} Symmetry_Constraint: {specific_word_counts/rules} INPUT_STATE: "{previous_text}" [END_BLOCK] ```

### **V. THE AUDIT CHANNEL (Hidden Diagnostics)** For every turn, the HLC must log a "Diagnostic Entry" to a separate file: `Cycle [X] | Rule_Pass: [T/F] | Attractor_Dur: [Y] | Regime: [S-S/S-M/etc] | Event: [None/Shatter/Pivot]`

***

**This is the complete specification for the Hard-Logic Controller. It is the "Truth" layer that prevents the AI from roleplaying and forces it to operate as a state machine.**

**Say "Next" when you are ready for Document 2: The Blind Generative Layer (NGL) Prompt.**
