# Why the nearest simple state can escape a proposed shape

Replacing a complicated object by its nearest simple neighbour is a natural idea. Can we make the search easier by requiring that neighbour to have a particularly tidy shape? This paper by Haobo Ma and Wenlin Zhang gives an exact negative example. For one three-qubit state, a mixture of ten independently prepared product states is closer than **every** fully separable state of the conjectured shape. The improvement is small but is a strictly positive rational number, enough to refute a universal conjecture.

The question comes from M. Consiglio, T. J. G. Apollaro and M. Wieśniak, *Variational approach to the quantum separability problem*, specifically arXiv:2209.01430v2, Appendix A.3, Eq. (A11). We explain version 2 of Ma and Zhang's paper; the result addresses this shape conjecture rather than assessing every numerical result in the posing paper.

## What mixing and distance mean

Imagine three laboratory benches, each preparing a system with two basic outcomes called $0$ and $1$. Preparing the three systems independently gives a **product state**. Now use an ordinary random selector to choose among several such independent preparation recipes. The resulting mixture is a **fully separable state**. The benches may share the classical information about which recipe was chosen. Full separability does not mean that measured outcomes have no correlations: it means those correlations admit this mixture explanation.

A quantum state is recorded in a table of numbers called a density matrix. Three binary systems have eight basic strings, ordered $000,001,\ldots,111$. The eight diagonal numbers are the probabilities of those outcomes and add to $1$. Entries away from the diagonal record coherence. They can be complex numbers and are not extra probabilities. A valid matrix must also be positive semidefinite, ensuring that measurement probabilities cannot be negative.

The distance here adds the squared absolute differences between corresponding entries:

$$
D_{\mathrm{HS}}(\rho,\sigma)=\sum_{i,j}|\rho_{ij}-\sigma_{ij}|^2.
$$

It is a **squared** distance, with no final square root. The idea is the same as $(x-x')^2+(y-y')^2$ in a coordinate plane, with table entries serving as coordinates. Write $E_{\mathrm{HS}}(\rho)$ for the minimum squared distance to all fully separable states. This set is compact in finite dimension, so a minimum exists. Strict convexity of the squared norm makes the nearest state unique.

Here is a feasible recipe we can check immediately: erase every off-diagonal entry, keeping the probability diagonal. This is a mixture of the eight basic product states and is therefore fully separable. If the only off-diagonal entries are two real opposite corners $\gamma$, erasing them costs $2\gamma^2$: both corner entries contribute.

## What the simplified search misses

The target $\rho$ has diagonal

$$
(1/5,1/5,1/5,1/5,0,0,0,1/5).
$$

Its only off-diagonal entries join $000$ to $111$ and back, both equal to $11/112$. It is a low-branch instance of the source's X-MEMS family. The corner block has eigenvalues $1/5\pm11/112>0$, so this is a valid quantum state.

The conjectured shape $S(a,b,d)$ compresses the eight probabilities into three groups:

| Strings | Probability |
| --- | --- |
| $000,111$ | $a/2$ |
| $001,010,011$ | $b/3$ |
| $100,101,110$ | $(1-a-b)/3$ |

Only the opposite corners $d,\bar d$ remain off the diagonal. The parameters obey $a,b\ge0$, $a+b\le1$, $|d|\le a/2$, and we additionally require **full separability**. Positivity of the matrix does not supply that last condition.

The decisive comparison is best read in two lines:

$$
\min_{S(a,b,d)\ \mathrm{fully\ separable}}D_{\mathrm{HS}}(\rho,S)=\frac{109}{23520}.
$$

$$
E_{\mathrm{HS}}(\rho)\le D_{\mathrm{HS}}(\rho,\tau)=\frac{417965512477}{90316800000000}.
$$

The second number is smaller by $84926789/12902400000000$. Once such a $\tau$ is constructed, we need not find the global optimum: one feasible challenger already beats the restricted family's champion. The [precise statements and proofs](statements.md) give the complete construction.

## A lower bound and a better feasible challenger

The lower bound starts with a linear inequality. In a product state, corner coherence is limited by the local probabilities. Applying the arithmetic–geometric mean inequality to those probabilities gives a linear upper bound. Linearity matters: an inequality satisfied by every independent recipe also holds for random mixtures of the recipes.

Substituting the proposed shape into this inequality gives a nonnegative quantity $h$. The distance can then be rewritten by completing squares, just as $x^2-2x+1=(x-1)^2$:

$$
D_{\mathrm{HS}}(\rho,S)=\frac{109}{23520}+Q+\frac h7.
$$

Here $Q$ is the sum of five nonnegative square terms. This is an identity, covering every parameter, complex $d$, and boundary cases. The paper constructs $S_*=S(3/8,9/16,1/16)$, where every extra term vanishes, so the bound is attained.

Next, start with the independent preparation recipes for $S_*$. Change a probability in the second and third systems from $1/2$ to $199/400$, a change of just $1/400$. Every recipe remains a product state, and the mixture weights stay fixed. Thus the new state $\tau$ is automatically fully separable. Nine phased product states each have weight $5/54$, together with the basic state $111$ of weight $1/6$; the weights add to $1$.

Think of each phase as a hand pointing to one of three equally spaced positions on a clock. Turn the first two hands by $r$ and $s$ steps, and the third backwards by $r+s$. Averaging the nine choices cancels the unwanted coherences while preserving the opposite corners. This makes the sparse matrix construction exact.

The challenger $\tau$ still has only opposite-corner off-diagonal entries and still respects interchange of the second and third systems. What it breaks is the table's additional equality of populations. **The obstruction is the population grouping, rather than the sparse corner support itself.**

## Why a symmetry must preserve feasible states

If a transformation fixes the target and maps every feasible state to a feasible state, averaging over such transformations cannot increase squared distance. That is a sound way to simplify the search.

Fixing the target alone is insufficient. For example, exchanging $000$ and $111$ while leaving the other strings untouched fixes $\rho$. Yet it sends the product vector $(|000\rangle+|001\rangle)/\sqrt2$ to $(|111\rangle+|001\rangle)/\sqrt2$. The latter is entangled across the first-system cut. This transformation can send a feasible state outside the feasible set, so it cannot justify imposing extra population equalities. Local phase transformations and interchange of the second and third systems do preserve full separability.

## Two consequences that answer different questions

The first corollary gives a useful distinction: one state is separable for each possible division into “one bench versus the other two,” but is not fully separable across all three benches. Different divisions may use different decompositions, so the separate two-group explanations need not combine into one three-party independent mixture. The example also passes the positive-partial-transpose test, or PPT, for every division. PPT is a necessary test and cannot replace full separability here.

The other corollary preserves a large-system conclusion. For $n$ qubits, every fully separable state has corner-coherence magnitude at most $2^{-n}$. A target with just one pair of opposite-corner coherences $\gamma_n,\bar\gamma_n$ therefore obeys

$$
2\bigl(\max\{|\gamma_n|-2^{-n},0\}\bigr)^2\le E_{\mathrm{HS}}(X_n),
$$

$$
E_{\mathrm{HS}}(X_n)\le2|\gamma_n|^2.
$$

If $|\gamma_n|\to g$, both ends tend to $2g^2$, forcing the distance between them to do so too. This proof does not use the refuted shape conjecture. The actual finite-$n$ nearest states, including the global minimum for this particular $\rho$, are not determined by the paper.

## Watch the mechanism, then discuss the details

The film compares the restricted family's champion with a better feasible challenger, showing phase averaging and the probability perturbation.

::: {.film src="001-escaping-the-shape"}
How a separable mixture escapes the proposed shape and strictly reduces squared distance.
:::

The academic talk retains the exact constants, square-completion identity and evidence scope for further discussion after the story.

::: {.slides src="seminar"}
An academic Beamer presentation with aligned Chinese and English frames and speaker notes.
:::
