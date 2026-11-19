# 精确陈述与证明

这里按原论文的依赖顺序给出完整论证。记 $\mathcal S_n$ 为纯 $n$ 方乘积投影的凸包，$D_{\mathrm{HS}}(R,Q)=\operatorname{Tr}((R-Q)^2)$，$E_{\mathrm{HS}}(R)=\min_{Q\in\mathcal S_n}D_{\mathrm{HS}}(R,Q)$。所有矩阵均为有限维，距离仅在厄米矩阵间使用。局部混合密度矩阵的乘积给出同一个凸包：逐个作谱分解并展开即可。

## 目标与候选家族

三比特基底顺序为 $000,001,\ldots,111$，第一位为最高位。定义

$$
\begin{aligned}
\rho={}&\operatorname{diag}(1/5,1/5,1/5,1/5,0,0,0,1/5)\\
&+\frac{11}{112}|000\rangle\langle111|\\
&+\frac{11}{112}|111\rangle\langle000|.
\end{aligned}
$$

$$
\begin{aligned}
S(a,b,d)={}&\operatorname{diag}(A,B,B,B,C,C,C,A)\\
&+d|000\rangle\langle111|\\
&+\bar d|111\rangle\langle000|,
\end{aligned}
$$

$$
A=a/2,\qquad B=b/3,\qquad C=(1-a-b)/3.
$$

参数范围是 $a,b\ge0$、$a+b\le1$、$d\in\mathbb C$、$|d|\le a/2$。这些条件使 $S$ 是密度矩阵，但我们在最小化时还要求 $S\in\mathcal S_3$。$\rho$ 的迹为 $1$；角块特征值为 $1/5\pm11/112$，其余对角元非负，所以 $\rho$ 也是密度矩阵。

::: {.theorem #thm-main title="形状内的精确最小值与严格改进" status="written-proof" proof="pf-thm-main" doi="10.5281/zenodo.23904464" source="Theorem 1, Sections 2–3" request="https://github.com/the-omega-institute/trureturing-requests/issues/186" mathesis="collected:consiglio-apollaro-wiesniak-2022-xmems-css-shape:2:s1"}

对上述 $\rho$ 和候选家族，有

$$
E_{\mathrm{HS}}(\rho)\le\frac{417965512477}{90316800000000}<\frac{109}{23520},
$$

$$
\min_{S(a,b,d)\in\mathcal S_3}D_{\mathrm{HS}}(\rho,S(a,b,d))=\frac{109}{23520}.
$$

因此在此实例，原文式 (A8)、(A11) 及共同形式 (16) 中不存在最近的完全可分态。这里的严格不等式并未给出 $E_{\mathrm{HS}}(\rho)$ 的精确值。
:::

::: {.proof #pf-thm-main}
**第一步：完全可分性给出的线性约束。** 记 $p_{xyz}=\sigma_{xyz,xyz}$、$z=\sigma_{000,111}$。每个完全可分态满足

$$
\begin{aligned}
L_1&=\frac{p_{001}}6+\frac{3p_{110}}2,\\
L_2&=\frac{p_{000}}{12}+\frac{p_{011}}{12}\\
&\quad+\frac{3p_{101}}4+\frac{3p_{110}}4,\\
\operatorname{Re}z&\le\frac15L_1+\frac45L_2.
\end{aligned}
$$

证明时先取三个局部密度矩阵的乘积，各局部对角元为 $(\alpha_j,\beta_j)$。局部正半定性给出 $|z|\le\sqrt{\prod_j\alpha_j\beta_j}$。于是

$$
|z|\le\sqrt{p_{001}p_{110}}\le p_{001}/6+3p_{110}/2.
$$

第二个上界从 $\sqrt{\alpha_1\beta_1}\le\alpha_1/6+3\beta_1/2$ 出发。令 $R=\sqrt{\alpha_2\beta_2\alpha_3\beta_3}$，在乘 $\alpha_1/6$ 的项用 $R\le(\alpha_2\alpha_3+\beta_2\beta_3)/2$，在乘 $3\beta_1/2$ 的项用 $R\le(\alpha_2\beta_3+\beta_2\alpha_3)/2$，即得到上式的 $L_2$。每个上界在线性化为 $\operatorname{Re}z$ 的不等式后，都可通过凸混合传递；再以 $1/5$ 与 $4/5$ 加权即得所需约束。上述算术—几何平均不等式也适用于零概率。

**第二步：下界及全部边界。** 对 $S$ 写 $x=\operatorname{Re}d$、$y=\operatorname{Im}d$，线性约束与配方恒等式为

$$
\begin{aligned}
h&=\frac A{15}+\frac B{10}+\frac{3C}2-x\\
&=\frac12-\frac7{15}(a+b)-x\ge0.
\end{aligned}
$$

$$
\begin{aligned}
&D_{\mathrm{HS}}(\rho,S)\\
&=2(1/5-A)^2+3(1/5-B)^2\\
&\quad+3C^2+2(11/112-x)^2+2y^2\\
&=\frac{109}{23520}+2(A-3/16)^2\\
&\quad+3(B-3/16)^2+3(C-1/48)^2\\
&\quad+2(x-1/16)^2+2y^2+\frac h7.
\end{aligned}
$$

等式右边除常数外全非负，所以得到形状内的下界。推导没有除以参数，也没有假定 $d$ 为实数，因此包括复角元与所有边界。

**第三步：达到下界。** 对 $r\in\mathbb Z/3\mathbb Z$ 定义

$$
v(t,r)=\sqrt t\,|0\rangle+\omega^r\sqrt{1-t}\,|1\rangle,
$$

$$
\omega=e^{2\pi i/3},\qquad 0\le t\le1,
$$

$$
\begin{aligned}
V_{rs}&=v(t_1,r)\otimes v(t_2,s)\\
&\quad\otimes v(t_3,-r-s),\\
T(t_1,t_2,t_3)&=\frac19\sum_{r,s=0}^2|V_{rs}\rangle\langle V_{rs}|.
\end{aligned}
$$

每个向量归一化，所以 $T$ 完全可分。其对角元在字串 $q$ 处为 $\prod_jt_j^{1-q_j}(1-t_j)^{q_j}$，角相干为 $\prod_j\sqrt{t_j(1-t_j)}$。其他非对角元消失：相位平均要求 $q_1-q'_1=q_3-q'_3$、$q_2-q'_2=q_3-q'_3$ 模 $3$ 成立。每个差在 $\{-1,0,1\}$，模 $3$ 相等意味着整数相等，于是只剩对角和相反两角。

因此

$$
\begin{aligned}
S_*&:=\frac56T(9/10,1/2,1/2)\\
&\quad+\frac16|111\rangle\langle111|\\
&=S(3/8,9/16,1/16)
\end{aligned}
$$

完全可分，并使所有平方项及 $h$ 同时为零。这证明最小值等号。反过来，达到下界时所有非负项必须为零，故在该参数族内必有 $A=B=3/16$、$C=1/48$、$x=1/16$、$y=0$，也就是 $S_*$。

**第四步：严格更近的状态。** 取

$$
\begin{aligned}
\tau&=\frac56T(9/10,199/400,199/400)\\
&\quad+\frac16|111\rangle\langle111|.
\end{aligned}
$$

这是九个权重 $5/54$ 和一个权重 $1/6$ 的纯乘积投影的凸组合，因而完全可分。它的对角线为

$$
\frac1{1920000}\begin{aligned}
(&356409,359991,359991,363609,\\
 &39601,39999,39999,360401),
\end{aligned}
$$

仅有的非对角元均为 $119997/1920000$，位于相反两角。逐格平方求和给出

$$
D_{\mathrm{HS}}(\rho,\tau)=\frac{417965512477}{90316800000000},
$$

$$
\frac{109}{23520}-D_{\mathrm{HS}}(\rho,\tau)=\frac{84926789}{12902400000000}>0.
$$

由 $\tau\in\mathcal S_3$ 得 $E_{\mathrm{HS}}(\rho)\le D_{\mathrm{HS}}(\rho,\tau)$，合并前三步即得结论。论证对应原论文第 2–3 节。
:::

## 精确的形式化结论

下面单独陈述已匹配的普遍猜想之否定，避免把数值下界的达到性并入该声明。

::: {.theorem #thm-refutation title="低分支普遍形状猜想不成立" lean="D5/S3/Quantum/Entanglement/GeometricMeasure/XMemsClosestSeparableShapeRefutation.result" mathesis="collected:consiglio-apollaro-wiesniak-2022-xmems-css-shape:2:s1"}

以下普遍断言为假：对每个整数 $n\ge2$ 和每个满足 $|\gamma|\le1/(2^{n-1}+1)$ 的复数 $\gamma$，低分支目标 $X_n(\gamma)$ 都有一个属于候选形状的最近完全可分态。

这里 $X_n(\gamma)$ 的对角元在首位为 $0$ 的字串及全 $1$ 字串上为 $1/(2^{n-1}+1)$，其他位置为 $0$，仅相反两角为 $\gamma,\bar\gamma$。候选形状的端点对角元为 $a/2$，首位为 $0$ 的其他字串上为 $b/(2^{n-1}-1)$，剩余字串上为 $(1-a-b)/(2^{n-1}-1)$，仅相反两角为 $d,\bar d$；参数满足 $a,b\in[0,1]$、$a+b\le1$、$|d|\le a/2$。“最近”表示对所有完全可分竞争者，平方距离均不大于它们。
:::

::: proof
取 $n=3$、$\gamma=11/112$。若形状内存在全局最近的可分态，其距离须不超过 $\tau$ 的距离，却又至少为 $109/23520$，与严格有理数差矛盾。上面的完整数值定理还包含下界达到性；这一单独形式化结论陈述的是普遍断言的否定。
:::

## 每个二分割可分，仍不完全可分

::: {.corollary #cor-ppt title="各割可分但非完全可分" status="written-proof" proof="pf-cor-ppt" doi="10.5281/zenodo.23904464" source="Corollary 2, Section 4.1" request="https://github.com/the-omega-institute/trureturing-requests/issues/187" mathesis="collected:consiglio-apollaro-wiesniak-2022-xmems-css-shape:2:s2"}

$\eta=S(5/16,5/8,33/512)$ 在每个一对二分割下部分转置为正，而且在每个这样的分割下可分，但不是完全可分。因此原问题式 (A10) 的条件不足以保证该家族完全可分。
:::

::: {.proof #pf-cor-ppt}
$\eta$ 的端点对角元为 $5/32$，上方三个内点为 $5/24$，下方三个内点为 $1/48$。迹为 $1$，且原角块正定，因为 $33/512<5/32$。每个部分转置只有一个可能产生负性的 $2\times2$ 块，其行列式为

$$
\frac5{24}\frac1{48}-\left(\frac{33}{512}\right)^2=\frac{439}{2359296}>0.
$$

固定任一分割，原矩阵的相干扇区位于另两个比特的 $|00\rangle,|11\rangle$ 所张成空间，构成一个 $2\otimes2$ 正算子。其部分转置为正；归一化后使用 Horodecki 等人的两比特 PPT 充要准则，可知它跨该割可分。其余项是该割下的非负对角乘积投影，故整个 $\eta$ 跨该割可分。另一方面，前述完全可分线性约束要求 $\operatorname{Re}d\le1/16$，而 $33/512=1/16+1/512$。矛盾证明非完全可分。这个推论只依赖线性约束，并不依赖形状内最小值的达到性。出处：原论文第 4.1 节、推论 2；PPT 准则的来源见[文献](sources.md)。
:::

## 大比特数的极限

::: {.corollary #cor-limit title="角相干夹逼与极限" status="written-proof" proof="pf-cor-limit" doi="10.5281/zenodo.23904464" source="Corollary 3, Section 4.3" request="https://github.com/the-omega-institute/trureturing-requests/issues/188" mathesis="collected:consiglio-apollaro-wiesniak-2022-xmems-css-shape:2:s3"}

设 $n\ge1$，$X_n$ 为 $n$ 比特密度矩阵，非对角元仅可能为相反两角 $\gamma_n,\bar\gamma_n$。则

$$
2\bigl(\max\{|\gamma_n|-2^{-n},0\}\bigr)^2\le E_{\mathrm{HS}}(X_n),
$$

$$
E_{\mathrm{HS}}(X_n)\le2|\gamma_n|^2.
$$

对这样一列矩阵，若 $|\gamma_n|\to g$，则 $E_{\mathrm{HS}}(X_n)\to2g^2$。
:::

::: {.proof #pf-cor-limit}
$X_n$ 的对角部分是完全可分态；与它相减只剩两个角元，所以得上界。任一局部比特密度矩阵 $q$ 满足 $|q_{01}|^2\le q_{00}q_{11}\le1/4$。故每个 $n$ 方乘积态的角相干大小不超过 $2^{-n}$，由三角不等式每个完全可分混合也满足此界。对任意这样的 $\sigma$，反三角不等式给出角差大小至少为 $\max\{|\gamma_n|-2^{-n},0\}$；只保留平方范数中两角的贡献即可得下界。若 $|\gamma_n|\to g$，因 $2^{-n}\to0$，上下界均趋于 $2g^2$，夹逼即得极限。

当 $\gamma_n=0$ 时上下界都是 $0$；当 $n=1$ 时每个单比特态本来就是完全可分的，$E=0$，且 $|\gamma_1|\le1/2$ 使下界也为 $0$。论证没有使用形状猜想，也没有给出一般有限 $n$ 的等号刻画。出处：原论文第 4.3 节、推论 3。
:::
