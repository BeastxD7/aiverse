# Stage 6 — Near-Duplicate Removal

## Purpose

Remove near-duplicate samples using MinHash LSH so the final dataset has meaningful diversity rather than slight paraphrases of the same message.

## Algorithm

MinHash + LSH (Locality Sensitive Hashing) at Jaccard similarity threshold.

1. Tokenize each text field into 3-grams (character n-grams for language-agnostic matching)
2. Build a MinHash signature for each sample (default 128 permutations)
3. Use LSH to find pairs with Jaccard similarity > threshold
4. Keep the first sample in each near-duplicate cluster; discard the rest

## Config

```yaml
dedup:
  threshold: 0.85   # 0.85 = very similar text gets removed; lower = more aggressive
  num_perm: 128     # MinHash permutations — higher = more accurate but slower
```

## Which fields are checked?

`pick_text_fields()` selects fields of type `string` from the schema. Enum fields (like `label`) are excluded — two examples with the same label but different text are not duplicates.

## Implementation

Uses `datasketch` library (`MinHash`, `MinHashLSH`).

## File

`engine/src/synthdata_engine/stages/dedup.py`
