# Closest-separable-state shape for X-MEMS

Main source: `note.tex`. Compiled paper: `note.pdf`.

The note gives an explicit three-qubit counterexample to arXiv:2209.01430v2,
Appendix A, Eq. (A11), at gamma = 11/112, and proves directly related statements
about full separability, concurrence comparisons and the large-qubit limit.
The exact global closest state at this instance is not identified.

## Build

Use Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively, use a LaTeX distribution containing the packages named in
`note.tex`:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

The bibliography is embedded in `note.tex`; no BibTeX invocation, external
figures or supplementary TeX files are required.

## Exact finite checks

Python 3.11 or later and its standard library suffice:

```sh
python3 verify.py
```

The command writes `verification.json`. Expected exact values include:

- Restricted squared-distance minimum: `109/23520`.
- Product-mixture squared distance: `417965512477/90316800000000`.
- Strict distance gap: `84926789/12902400000000`.
- The PPT example's partial-transpose block determinant: `439/2359296`.
- Its violation of the full-separability inequality: `1/512`.
- The two-qubit competitor's squared distance: `7/288`.

The program compares polynomial coefficients with rational arithmetic and
enumerates all 64 three-qubit and all 16 two-qubit matrix positions for the
character averages. The note supplies the product-state inequalities and all
continuous-parameter arguments. The pinned Lean declaration
`D5.S3.Quantum.Entanglement.GeometricMeasure.XMemsClosestSeparableShapeRefutation.result`
formalizes the negation of the universal low-branch shape assertion:

https://github.com/the-omega-institute/trureturing/blob/83b70a1d0d6a58bb32521c741805d845d401c5f8/D5/S3/Quantum/Entanglement/GeometricMeasure/XMemsClosestSeparableShapeRefutation.lean

The exact restricted-minimum attainment, symmetry reduction and related results
have written proofs in the note. Access to the linked repository follows its
owner's access settings; the paper and Python checks are self-contained.

## Authors and license

1. Haobo Ma — ChronoAI Pte Ltd, Singapore.
2. Wenlin Zhang — National University of Singapore; ChronoAI Pte Ltd, Singapore.

CC BY 4.0 (`cc-by-4.0`):
https://creativecommons.org/licenses/by/4.0/

The bibliography attributes the posing source, the rational counterexample's
formalization and the mathematical tools used.
