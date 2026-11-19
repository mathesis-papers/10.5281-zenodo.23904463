# Sources and contributions

## Where this explanation comes from

The paper's authors are Haobo Ma (Chrono AI, Singapore) and Wenlin Zhang (National University of Singapore and Chrono AI, Singapore). The original question and shape conjecture are due to M. Consiglio, T. J. G. Apollaro and M. Wieśniak. This explanation follows version 2 of Ma and Zhang's paper, with version DOI **10.5281/zenodo.23904464**; the concept DOI collecting versions is 10.5281/zenodo.23904463. The explanation and paper retain CC-BY-4.0 attribution.

The main thread covers the original Theorem 1, Corollary 2 and Corollary 3. Original Section 4.2 additionally gives counterexamples to comparisons between concurrence and squared Hilbert–Schmidt distance; the public PDF supplies those separate two- and three-qubit examples. Every distance in this explanation is squared: the constants cannot be carried over unchanged to the unsquared norm.

## What can be checked, and what can be contributed?

The public theorem in the [pinned Lean source](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/Quantum/Entanglement/GeometricMeasure/XMemsClosestSeparableShapeRefutation.lean) proves that the universal low-branch shape conjecture is false. Its proof uses the three-qubit rational competitor and restricted lower bound. The complete numerical theorem additionally contains attainment of that bound. The cutwise-separable example and general-qubit limit have written proofs in the paper. The [precise statements](statements.md) distinguish these mathematical scopes.

Readers interested in formalization can begin with these three public tasks.

- [Restricted-minimum attainment](https://github.com/the-omega-institute/trureturing-requests/issues/186): reuse the existing separability inequality, lower bound and phase-averaging construction to supply the separable decomposition of $S_*$ and equality.
- [Cutwise separability without full separability](https://github.com/the-omega-institute/trureturing-requests/issues/187): reuse the separability inequality and connect the two-qubit PPT argument for each cut.
- [Corner-coherence bounds and limit](https://github.com/the-omega-institute/trureturing-requests/issues/188): formalize the local corner bound, its product and mixture consequences, and squeezing.

Coordinate scope on the corresponding issue, work on a focused branch in your contributor fork, and submit directly to upstream `dev` under the [existing contribution rules](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md). Full separability, separability across each cut and PPT have different conditions and quantifiers; preserve those distinctions.

## References

Items 4–5 provide the background of matrix-element separability inequalities; item 6 supplies the separability criterion on each $2\otimes2$ coherent sector.

1. Haobo Ma and Wenlin Zhang. *Refuting the X-MEMS closest-separable-state conjecture in arXiv:2209.01430v2, Appendix A, Eq. (A11)*, version 2. [DOI:10.5281/zenodo.23904464](https://doi.org/10.5281/zenodo.23904464). [PDF](https://zenodo.org/api/records/23904464/files/note-v2.pdf/content); [source](https://zenodo.org/api/records/23904464/files/source-v2.zip/content).
2. M. Consiglio, T. J. G. Apollaro and M. Wieśniak. *Variational approach to the quantum separability problem*. Physical Review A **106**, 062413 (2022). [DOI:10.1103/PhysRevA.106.062413](https://doi.org/10.1103/PhysRevA.106.062413). [arXiv:2209.01430v2](https://arxiv.org/abs/2209.01430v2), Appendix A.3, Eq. (A11); full-separability convention in Sections I–II.
3. M. Consiglio. *Variational Quantum Algorithms for Many-Body Systems*. Ph.D. thesis, University of Malta (2025). [arXiv:2502.11985v1](https://arxiv.org/abs/2502.11985v1), Appendix C.3, Eq. (C.12), printed pp. 118–119.
4. O. Gühne and M. Seevinck. *Separability criteria for genuine multiparticle entanglement*. New Journal of Physics **12**, 053002 (2010). [DOI:10.1088/1367-2630/12/5/053002](https://doi.org/10.1088/1367-2630/12/5/053002), Observation 4.
5. L. Chen, K. H. Han and S.-H. Kye. *Separability criterion for three-qubit states with a four dimensional norm*. Journal of Physics A **50**, 345303 (2017). [DOI:10.1088/1751-8121/aa7f9a](https://doi.org/10.1088/1751-8121/aa7f9a), Theorem 2.1.
6. M. Horodecki, P. Horodecki and R. Horodecki. *Separability of mixed states: necessary and sufficient conditions*. Physics Letters A **223**, 1–8 (1996). [DOI:10.1016/S0375-9601(96)00706-2](https://doi.org/10.1016/S0375-9601(96)00706-2).

<section hidden="hidden">

```{=typst}
#pagebreak()
```

</section>
