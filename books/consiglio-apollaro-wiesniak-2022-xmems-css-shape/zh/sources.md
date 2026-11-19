# 来源与继续贡献

## 这份解释的来源

论文作者为 Haobo Ma（Chrono AI，Singapore）与 Wenlin Zhang（National University of Singapore 及 Chrono AI，Singapore）。原问题及形状猜想归于 M. Consiglio、T. J. G. Apollaro 与 M. Wieśniak。本文解释以 Ma 与 Zhang 的第 2 版为准，版本 DOI 为 **10.5281/zenodo.23904464**；汇集各版本的概念 DOI 为 10.5281/zenodo.23904463。解释与原论文均保留 CC-BY-4.0 署名许可。

主线是原论文定理 1、推论 2 与推论 3。原论文第 4.2 节还给出 concurrence 与平方 Hilbert–Schmidt 距离之间比较的反例；读者可在原 PDF 中继续阅读该独立的两比特与三比特例子。本解释中的距离始终是平方距离，不能把它改成未平方的范数后沿用常数。

## 可以检查什么，又可以补上什么？

[固定版本的 Lean 源文件](https://github.com/the-omega-institute/trureturing/blob/8a24ea4e79de962725aab9d9b49cc605fcc211d8/D5/S3/Quantum/Entanglement/GeometricMeasure/XMemsClosestSeparableShapeRefutation.lean)中的公开定理证明低分支普遍形状猜想不成立。其证明具体使用三比特有理数竞争者与形状内下界；完整数值定理还包括受限下界的达到性。每割可分反例与一般比特数极限在原论文中有书面证明。上述证据的范围分别陈述在[精确陈述](statements.md)中。

希望参与形式化的读者可以从以下三个已有公共问题开始。

- [受限最小值的达到性](https://github.com/the-omega-institute/trureturing-requests/issues/186)：复用现有分离不等式、下界和相位平均构造，补齐 $S_*$ 的可分分解与等号。
- [每割可分而不完全可分](https://github.com/the-omega-institute/trureturing-requests/issues/187)：复用分离不等式，连接每割的两比特 PPT 论证。
- [角相干的两侧界和极限](https://github.com/the-omega-institute/trureturing-requests/issues/188)：形式化局部角元界、乘积与凸混合传递，以及夹逼极限。

在相应公共问题中协调范围，在自己的贡献者 fork 上建立聚焦分支，依照[上游贡献规则](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md)直接向上游 `dev` 提交 PR。完全可分、每割可分和 PPT 是不同条件，贡献中应保持各自的量词。

## 文献

以下第 4–5 项提供矩阵元可分性不等式的背景，第 6 项用于每个 $2\otimes2$ 相干扇区的可分性判据。

1. Haobo Ma and Wenlin Zhang. *Refuting the X-MEMS closest-separable-state conjecture in arXiv:2209.01430v2, Appendix A, Eq. (A11)*, version 2. [DOI:10.5281/zenodo.23904464](https://doi.org/10.5281/zenodo.23904464). [PDF](https://zenodo.org/api/records/23904464/files/note-v2.pdf/content); [source](https://zenodo.org/api/records/23904464/files/source-v2.zip/content).
2. M. Consiglio, T. J. G. Apollaro and M. Wieśniak. *Variational approach to the quantum separability problem*. Physical Review A **106**, 062413 (2022). [DOI:10.1103/PhysRevA.106.062413](https://doi.org/10.1103/PhysRevA.106.062413). [arXiv:2209.01430v2](https://arxiv.org/abs/2209.01430v2), Appendix A.3, Eq. (A11); full-separability convention in Sections I–II.
3. M. Consiglio. *Variational Quantum Algorithms for Many-Body Systems*. Ph.D. thesis, University of Malta (2025). [arXiv:2502.11985v1](https://arxiv.org/abs/2502.11985v1), Appendix C.3, Eq. (C.12), printed pp. 118–119.
4. O. Gühne and M. Seevinck. *Separability criteria for genuine multiparticle entanglement*. New Journal of Physics **12**, 053002 (2010). [DOI:10.1088/1367-2630/12/5/053002](https://doi.org/10.1088/1367-2630/12/5/053002), Observation 4.
5. L. Chen, K. H. Han and S.-H. Kye. *Separability criterion for three-qubit states with a four dimensional norm*. Journal of Physics A **50**, 345303 (2017). [DOI:10.1088/1751-8121/aa7f9a](https://doi.org/10.1088/1751-8121/aa7f9a), Theorem 2.1.
6. M. Horodecki, P. Horodecki and R. Horodecki. *Separability of mixed states: necessary and sufficient conditions*. Physics Letters A **223**, 1–8 (1996). [DOI:10.1016/S0375-9601(96)00706-2](https://doi.org/10.1016/S0375-9601(96)00706-2).
