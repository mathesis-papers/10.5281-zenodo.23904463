# Refuting the X-MEMS closest-separable-state conjecture in arXiv:2209.01430v2, Appendix A, Eq. (A11)

**Authors:** Haobo Ma, Wenlin Zhang

We refute the closest-fully-separable-state shape conjecture of Consiglio, Apollaro and Wieśniak, arXiv:2209.01430v2, Appendix A, Eq. (A11), already for three qubits on the low branch at gamma = 11/112. Every fully separable state of the proposed shape has squared Hilbert–Schmidt distance at least 109/23520, whereas an explicit mixture of ten pure product states has distance 417965512477/90316800000000. The counterexample and exact restricted minimum have self-contained written proofs, as do related counterexamples to the full-separability and concurrence comparisons in the posing source. An elementary bound also establishes its large-qubit limit without the conjectured shape.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.23904464](https://doi.org/10.5281/zenodo.23904464)
- Concept DOI: [https://doi.org/10.5281/zenodo.23904463](https://doi.org/10.5281/zenodo.23904463)
- License: CC-BY-4.0
- Version: 2
- Mathesis record: [consiglio-apollaro-wiesniak-2022-xmems-css-shape](https://mathesis-omega-research.apps.chrono-ai.fun/papers/consiglio-apollaro-wiesniak-2022-xmems-css-shape?version=2)

## How to cite

Haobo Ma, Wenlin Zhang (2026). Refuting the X-MEMS closest-separable-state conjecture in arXiv:2209.01430v2, Appendix A, Eq. (A11). Mathesis, version 2. https://doi.org/10.5281/zenodo.23904464

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/83b70a1d0d6a58bb32521c741805d845d401c5f8/D5/S3/Quantum/Entanglement/GeometricMeasure/XMemsClosestSeparableShapeRefutation.lean) | No public receipt |
| Corollary (s2) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/83b70a1d0d6a58bb32521c741805d845d401c5f8/D5/S3/Quantum/Entanglement/GeometricMeasure/XMemsClosestSeparableShapeRefutation.lean) | No public receipt |
| Corollary (s3) | needs_attention | [Lean source](https://github.com/the-omega-institute/trureturing/blob/83b70a1d0d6a58bb32521c741805d845d401c5f8/D5/S3/Quantum/Entanglement/GeometricMeasure/XMemsClosestSeparableShapeRefutation.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- Mathesis generated repository guide; refresh with paper.py front. -->

## Reading and materials

[Paper site](https://papers.trureturing.org/10.5281-zenodo.23904463/) · [Frozen PDF](paper.pdf) · [Citation](CITATION.cff)

[中文阅读](https://papers.trureturing.org/10.5281-zenodo.23904463/consiglio-apollaro-wiesniak-2022-xmems-css-shape/zh/) · [Read in English](https://papers.trureturing.org/10.5281-zenodo.23904463/consiglio-apollaro-wiesniak-2022-xmems-css-shape/en/)

[Slides](https://papers.trureturing.org/10.5281-zenodo.23904463/consiglio-apollaro-wiesniak-2022-xmems-css-shape/slides/) ([sources](books/consiglio-apollaro-wiesniak-2022-xmems-css-shape/slides/)) · [Videos](https://papers.trureturing.org/10.5281-zenodo.23904463/consiglio-apollaro-wiesniak-2022-xmems-css-shape/films/) ([sources](books/consiglio-apollaro-wiesniak-2022-xmems-css-shape/films/))

These are publication routes; available built materials are inventoried in [mathesis-materials.json](https://papers.trureturing.org/10.5281-zenodo.23904463/mathesis-materials.json).

## Book and formalization

Catalog formalization status above is separate from the statement comparisons below. A nearby declaration does not verify the complete written result.

| Book result | Comparison with formal base | Compared declaration |
|---|---|---|
| `thm-main` | variant | `D5/S3/Quantum/Entanglement/GeometricMeasure/XMemsClosestSeparableShapeRefutation.result` |
| `thm-refutation` | same | `D5/S3/Quantum/Entanglement/GeometricMeasure/XMemsClosestSeparableShapeRefutation.result` |
| `cor-ppt` | none | — |
| `cor-limit` | none | — |

Book stage: **complete**; 0 pending claims. [Statement comparisons](.mathesis/REVIEW.md).

## Repository map

| Zone | Location |
|---|---|
| Paper record | `paper.json`, `CITATION.cff`, `paper.pdf`, `manuscript/`, `formalization/nodes.json`, `LICENSES/`, `.mathesis/` |
| Content | `books/consiglio-apollaro-wiesniak-2022-xmems-css-shape/`: Chinese/English text, figures, visualizations, videos, slides, assets |
| Machinery | Upstream and layer managed paths; update with `tbook template update` |
| Repository front | This README, changelog, contribution guide, licence, project/site/pin configuration, `template.d/` |

See [the enforced layout](docs/layer-mathesis/LAYOUT.md). Preparation run records and built outputs stay outside the committed tree.
