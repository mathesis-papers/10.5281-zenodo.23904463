# 书面陈述与所钉声明比较

比较版本：原论文第 2 版，DOI 10.5281/zenodo.23904464。检查完整提交 `8a24ea4e79de962725aab9d9b49cc605fcc211d8` 的源文件、Blueprint 与 Golden/Frozen/state；本地选择性锁不当作全库目录。原论文的 theorem/lemma/corollary 共用计数，来源编号为 Theorem 1、Corollary 2、Corollary 3。

| Result | Verdict | Compared declaration | Commit | Scope |
| --- | --- | --- | --- | --- |
| thm-main | variant | D5/S3/Quantum/Entanglement/GeometricMeasure/XMemsClosestSeparableShapeRefutation.result | 8a24ea4e79de962725aab9d9b49cc605fcc211d8 | 论文完整定理含有理竞争者、严格差与受限最小值达到性。公开 result 只陈述普遍低分支形状断言的否定；其私有 separable_bounds、shape_lower、tau_separable、tau_distance、distance_gap 提供已检查的下界及竞争者，但没有 S_* 达到性的声明。请求 #186 只要求复用既有构造补齐达到性，不重复反例。 |
| thm-refutation | same | D5/S3/Quantum/Entanglement/GeometricMeasure/XMemsClosestSeparableShapeRefutation.result | 8a24ea4e79de962725aab9d9b49cc605fcc211d8 | 对应原定理的逻辑结论而非整个数值定理。逐一展开 claim：n≥2，复 γ 范数≤1/(2^(n−1)+1)，显式低分支目标，a,b∈[0,1]、a+b≤1、复 d 范数≤a/2，有限局部密度矩阵乘积凸混合，以及对所有完全可分竞争者的平方 Hilbert–Schmidt 最小性。书中精确陈述其否定；n=3 与 γ=11/112 是证明中的见证。局部混合与纯乘积凸包由谱分解相同。 |
| cor-ppt | none | — | 8a24ea4e79de962725aab9d9b49cc605fcc211d8 | 完整结论是 eta 的每割 PPT、每割可分、非完全可分；已检查文件的分离不等式可复用，但 result 不陈述这些结论。检查相关 quantum-entanglement、PPT/separability、geometric-measure 文件目录与冻结列表，未找到同一完整声明。请求 #187 不依赖最小值达到性。 |
| cor-limit | none | — | 8a24ea4e79de962725aab9d9b49cc605fcc211d8 | 一般 n≥1 的任意对角人口、复角相干、两个界及收敛列的夹逼极限。result 仅否定形状猜想，不给出这些全参数界或极限。相关角相干、Hilbert–Schmidt 与几何度量目录无同一结果。请求 #188 与达到性无依赖。 |

两个 s1 映射说明关系：thm-main 是原论文完整数值定理，thm-refutation 是其中被公开 Lean 声明精确表达的普遍断言之否定。二者不是等价陈述。其余两个结果保留书面证明；不因原目录 needs_attention 字段或已有 Lean 链接而改写任何冻结验证状态。
