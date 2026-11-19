# Precise statements and proofs

We follow the dependency order of the original paper. Let $\mathcal S_n$ be the convex hull of pure $n$-party product projectors, $D_{\mathrm{HS}}(R,Q)=\operatorname{Tr}((R-Q)^2)$ and $E_{\mathrm{HS}}(R)=\min_{Q\in\mathcal S_n}D_{\mathrm{HS}}(R,Q)$. All matrices are finite dimensional; the distance is used between Hermitian matrices. Products of local mixed density matrices generate the same hull, by expanding their spectral decompositions.

## Target and proposed family

Order the three-qubit basis as $000,001,\ldots,111$, with the first bit most significant. Define

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

The parameter range is $a,b\ge0$, $a+b\le1$, $d\in\mathbb C$, $|d|\le a/2$. These conditions make $S$ a density matrix; minimization imposes $S\in\mathcal S_3$ as an additional condition. The target $\rho$ has trace $1$, corner-block eigenvalues $1/5\pm11/112$, and nonnegative remaining diagonal entries, so it too is a density matrix.

::: {.theorem #thm-main title="Exact restricted minimum and a strict improvement" status="written-proof" proof="pf-thm-main" doi="10.5281/zenodo.23904464" source="Theorem 1, Sections 2–3" request="https://github.com/the-omega-institute/trureturing-requests/issues/186" mathesis="collected:consiglio-apollaro-wiesniak-2022-xmems-css-shape:2:s1"}

For this target and family,

$$
E_{\mathrm{HS}}(\rho)\le\frac{417965512477}{90316800000000}<\frac{109}{23520},
$$

$$
\min_{S(a,b,d)\in\mathcal S_3}D_{\mathrm{HS}}(\rho,S(a,b,d))=\frac{109}{23520}.
$$

Thus the shapes in the posing source's Eqs. (A8), (A11) and common form (16) contain no closest fully separable state at this instance. The strict inequality does not determine the exact global value $E_{\mathrm{HS}}(\rho)$.
:::

::: {.proof #pf-thm-main}
**Step 1: a linear consequence of full separability.** Put $p_{xyz}=\sigma_{xyz,xyz}$ and $z=\sigma_{000,111}$. Every fully separable state satisfies

$$
\begin{aligned}
L_1&=\frac{p_{001}}6+\frac{3p_{110}}2,\\
L_2&=\frac{p_{000}}{12}+\frac{p_{011}}{12}\\
&\quad+\frac{3p_{101}}4+\frac{3p_{110}}4,\\
\operatorname{Re}z&\le\frac15L_1+\frac45L_2.
\end{aligned}
$$

First take a product of three local density matrices with diagonals $(\alpha_j,\beta_j)$. Local positivity implies $|z|\le\sqrt{\prod_j\alpha_j\beta_j}$. Hence

$$
|z|\le\sqrt{p_{001}p_{110}}\le p_{001}/6+3p_{110}/2.
$$

For the second bound start with $\sqrt{\alpha_1\beta_1}\le\alpha_1/6+3\beta_1/2$. Set $R=\sqrt{\alpha_2\beta_2\alpha_3\beta_3}$. In the term multiplied by $\alpha_1/6$, use $R\le(\alpha_2\alpha_3+\beta_2\beta_3)/2$; in the term multiplied by $3\beta_1/2$, use $R\le(\alpha_2\beta_3+\beta_2\alpha_3)/2$. This gives the quantity $L_2$ above. Once written as bounds on $\operatorname{Re}z$, both inequalities are linear in the entries and pass to convex mixtures. Combining them with weights $1/5$ and $4/5$ gives the stated inequality. The arithmetic–geometric mean inequalities also hold at zero probabilities.

**Step 2: the lower bound, including boundaries.** For $S$, write $x=\operatorname{Re}d$, $y=\operatorname{Im}d$. The linear constraint and exact square completion give

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

Every term after the constant is nonnegative, proving the restricted lower bound. No parameter was divided out and $d$ was not assumed real, so complex corners and all boundary cases are included.

**Step 3: attainment.** For $r\in\mathbb Z/3\mathbb Z$ define

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

Each vector is normalized, so $T$ is fully separable. Its diagonal entry at $q$ is $\prod_jt_j^{1-q_j}(1-t_j)^{q_j}$ and its corner coherence is $\prod_j\sqrt{t_j(1-t_j)}$. All other off-diagonal entries vanish: phase averaging requires $q_1-q'_1=q_3-q'_3$ and $q_2-q'_2=q_3-q'_3$ modulo $3$. Each difference belongs to $\{-1,0,1\}$; congruence therefore means equality as integers. Only the diagonal and two opposite corners survive.

Consequently,

$$
\begin{aligned}
S_*&:=\frac56T(9/10,1/2,1/2)\\
&\quad+\frac16|111\rangle\langle111|\\
&=S(3/8,9/16,1/16)
\end{aligned}
$$

is fully separable and makes all square terms and $h$ vanish, proving attainment. Conversely, equality in the lower bound forces every nonnegative term to vanish: $A=B=3/16$, $C=1/48$, $x=1/16$, $y=0$. Thus the equality state within this parameter family is $S_*$.

**Step 4: a strictly closer state.** Take

$$
\begin{aligned}
\tau&=\frac56T(9/10,199/400,199/400)\\
&\quad+\frac16|111\rangle\langle111|.
\end{aligned}
$$

This is a convex combination of nine pure product projectors with weight $5/54$ each and one with weight $1/6$, so it is fully separable. Its diagonal is

$$
\frac1{1920000}\begin{aligned}
(&356409,359991,359991,363609,\\
 &39601,39999,39999,360401),
\end{aligned}
$$

and its only off-diagonal entries, the opposite corners, both equal $119997/1920000$. Entrywise squaring gives

$$
D_{\mathrm{HS}}(\rho,\tau)=\frac{417965512477}{90316800000000},
$$

$$
\frac{109}{23520}-D_{\mathrm{HS}}(\rho,\tau)=\frac{84926789}{12902400000000}>0.
$$

Since $\tau\in\mathcal S_3$, $E_{\mathrm{HS}}(\rho)\le D_{\mathrm{HS}}(\rho,\tau)$. Combine this with the first three steps. This is the argument in Sections 2–3 of the original paper.
:::

## The exact formal conclusion

We state the matched negation of the universal conjecture separately, so that restricted-minimum attainment is not folded into that declaration.

::: {.theorem #thm-refutation title="Failure of the universal low-branch shape conjecture" lean="D5/S3/Quantum/Entanglement/GeometricMeasure/XMemsClosestSeparableShapeRefutation.result" mathesis="collected:consiglio-apollaro-wiesniak-2022-xmems-css-shape:2:s1"}

The following universal assertion is false: for every integer $n\ge2$ and every complex $\gamma$ with $|\gamma|\le1/(2^{n-1}+1)$, the low-branch target $X_n(\gamma)$ has a closest fully separable state of the proposed shape.

Here $X_n(\gamma)$ has diagonal $1/(2^{n-1}+1)$ at strings whose first bit is $0$ and at the all-one string, zero at other diagonal positions, and only opposite-corner coherences $\gamma,\bar\gamma$. The proposed shape has endpoint populations $a/2$, population $b/(2^{n-1}-1)$ at the other strings starting with $0$, and $(1-a-b)/(2^{n-1}-1)$ at the remaining strings, with only opposite corners $d,\bar d$. Its parameters satisfy $a,b\in[0,1]$, $a+b\le1$, $|d|\le a/2$. “Closest” means having squared distance no larger than that of every fully separable competitor.
:::

::: proof
Take $n=3$ and $\gamma=11/112$. A globally closest separable state of the proposed shape would have distance no greater than that of $\tau$, but at least $109/23520$, contradicting the strict rational gap. The complete numerical theorem above additionally includes attainment of the lower bound; this separately formalized conclusion states the negation of the universal assertion.
:::

## Separable across every cut, but not fully separable

::: {.corollary #cor-ppt title="Cutwise separability without full separability" status="written-proof" proof="pf-cor-ppt" doi="10.5281/zenodo.23904464" source="Corollary 2, Section 4.1" request="https://github.com/the-omega-institute/trureturing-requests/issues/187" mathesis="collected:consiglio-apollaro-wiesniak-2022-xmems-css-shape:2:s2"}

The state $\eta=S(5/16,5/8,33/512)$ is positive under partial transpose across every one-versus-two cut and separable across each such cut, but is not fully separable. Thus Eq. (A10) of the posing source is insufficient for full separability of that family.
:::

::: {.proof #pf-cor-ppt}
The endpoint diagonals are $5/32$, the three upper interior diagonals $5/24$, and the lower interior diagonals $1/48$. The trace is $1$, and the original corner block is positive since $33/512<5/32$. Every partial transpose has just one potentially nonpositive $2\times2$ block, with determinant

$$
\frac5{24}\frac1{48}-\left(\frac{33}{512}\right)^2=\frac{439}{2359296}>0.
$$

For any fixed cut, the original matrix's coherent sector acts on a $2\otimes2$ space, spanned on the other side by $|00\rangle,|11\rangle$. This positive operator has positive partial transpose. Normalize it and apply the two-qubit PPT criterion of the Horodeckis to obtain separability across that cut. The remaining terms are nonnegative diagonal product projectors across the same cut, so $\eta$ is separable across the cut. Full separability, however, would imply $\operatorname{Re}d\le1/16$ by the preceding linear constraint, whereas $33/512=1/16+1/512$. This contradiction proves the last clause. The proof uses the linear constraint, independently of restricted-minimum attainment. Source: original Section 4.1, Corollary 2; the PPT criterion is cited in the [references](sources.md).
:::

## A large-qubit limit

::: {.corollary #cor-limit title="Corner-coherence bounds and limit" status="written-proof" proof="pf-cor-limit" doi="10.5281/zenodo.23904464" source="Corollary 3, Section 4.3" request="https://github.com/the-omega-institute/trureturing-requests/issues/188" mathesis="collected:consiglio-apollaro-wiesniak-2022-xmems-css-shape:2:s3"}

Let $n\ge1$ and let $X_n$ be an $n$-qubit density matrix with no off-diagonal entries except possibly opposite corners $\gamma_n,\bar\gamma_n$. Then

$$
2\bigl(\max\{|\gamma_n|-2^{-n},0\}\bigr)^2\le E_{\mathrm{HS}}(X_n),
$$

$$
E_{\mathrm{HS}}(X_n)\le2|\gamma_n|^2.
$$

For a sequence of such matrices, if $|\gamma_n|\to g$, then $E_{\mathrm{HS}}(X_n)\to2g^2$.
:::

::: {.proof #pf-cor-limit}
The diagonal part of $X_n$ is fully separable, and subtracting it leaves only the two corners, proving the upper bound. Every local qubit density matrix $q$ satisfies $|q_{01}|^2\le q_{00}q_{11}\le1/4$. Each $n$-party product therefore has corner magnitude at most $2^{-n}$; the triangle inequality extends this bound to every fully separable mixture. For any such $\sigma$, the reverse triangle inequality bounds the corner difference below by $\max\{|\gamma_n|-2^{-n},0\}$. Retaining the two corner contributions to the squared norm proves the lower bound. If $|\gamma_n|\to g$, then $2^{-n}\to0$ and both bounds tend to $2g^2$; squeezing proves the limit.

For $\gamma_n=0$, both bounds are $0$. When $n=1$, every single-qubit state is already fully separable, so $E=0$; $|\gamma_1|\le1/2$ also makes the lower bound $0$. The argument uses no shape conjecture and does not characterize equality for general finite $n$. Source: original Section 4.3, Corollary 3.
:::
