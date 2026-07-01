# Volume VIII - Applied and Computational Mathematics Proofs To Do

Proof-writing order is dependency-first among active proof labels. Dependency edges come from resolved statement and proof dependency blocks; original source order is the stable tie-breaker.
Use `✅` to record completion after the canonical proof file has both proof bodies populated and validated.

Open proofs to do: 5
Completed in this tracker: 0

1. () `lem:computational-geometry-convex-hull-smallest-convex-set` — **Convex hull as the smallest convex set**
   > **Statement.**
   > Let \(P\subseteq\mathbb{R}^2\). Then \(\conv(P)\) is convex, contains \(P\), and
   > is contained in every convex set that contains \(P\). Hence
   > \[
   >   \conv(P)
   >   =
   >   \bigcap\{K\subseteq\mathbb{R}^2 : K\text{ is convex and }P\subseteq K\}.
   > \]

2. () `lem:computational-geometry-linear-functionals-convex-combinations` — **Linear functionals preserve convex combinations**
   > **Statement.**
   > Let \(d\in\mathbb{R}^2\), and let
   > \[
   >   z=\sum_{i=1}^{n}\lambda_i q_i
   > \]
   > be a convex combination of points \(q_1,\dots,q_n\in\mathbb{R}^2\). Then
   > \[
   >   \langle d,z\rangle
   >   =
   >   \sum_{i=1}^{n}\lambda_i\langle d,q_i\rangle.
   > \]
   > Consequently, if \(\langle d,q_i\rangle\le M\) for every \(i\), then
   > \[
   >   \langle d,z\rangle\le M.
   > \]

3. () `thm:computational-geometry-supporting-functional-hull-vertices` — **Supporting functional characterization of hull vertices**
   > **Statement.**
   > Let \(P\subset\mathbb{R}^2\) be finite and in general position. A point \(p\in P\)
   > is a vertex of \(\conv(P)\) if and only if there exists a direction
   > \(d\in\mathbb{R}^2\setminus\{0\}\) such that
   > \[
   >   \langle d,p\rangle>\langle d,q\rangle
   >   \qquad
   >   \text{for all } q\in P\setminus\{p\}.
   > \]
   > Equivalently, \(p\) is the unique point of \(P\) attaining
   > \[
   >   \max_{q\in P}\langle d,q\rangle.
   > \]
   > Thus every hull vertex is a maximum of \(P\) under some linear functional.

4. () `thm:computational-geometry-monotone-slope-upper-hull` — **Monotone slope characterization of the upper hull**
   > **Statement.**
   > Let \(P\subset\mathbb{R}^2\) be finite and in general position. Let
   > \[
   >   v_0,v_1,\dots,v_m
   > \]
   > be the vertices of the upper hull of \(P\), listed in increasing
   > \(x\)-coordinate, and define
   > \[
   >   s_k
   >   =
   >   \frac{y(v_{k+1})-y(v_k)}{x(v_{k+1})-x(v_k)},
   >   \qquad
   >   k=0,1,\dots,m-1.
   > \]
   > Then
   > \[
   >   s_0>s_1>\cdots>s_{m-1}.
   > \]
   > Conversely, if points \(w_0,\dots,w_m\) satisfy
   > \[
   >   x(w_0)<x(w_1)<\cdots<x(w_m)
   > \]
   > and their consecutive slopes are strictly decreasing, then every \(w_k\) is a
   > vertex of
   > \[
   >   \conv(\{w_0,\dots,w_m\}).
   > \]
   > The lower hull is characterized similarly, with strictly increasing consecutive
   > slopes.

5. () `thm:computational-geometry-greedy-slope-upper-hull` — **Greedy slope construction of the upper hull**
   > **Statement.**
   > Let \(P\subset\mathbb{R}^2\) be finite and in general position. Define
   > \[
   >   v_0=\argmin_{p\in P}x(p).
   > \]
   > Given \(v_k\) with
   > \[
   >   x(v_k)<\max_{p\in P}x(p),
   > \]
   > define
   > \[
   >   v_{k+1}
   >   =
   >   \argmax_{\substack{q\in P\\x(q)>x(v_k)}}
   >   \frac{y(q)-y(v_k)}{x(q)-x(v_k)}.
   > \]
   > Terminate once
   > \[
   >   v_k=\argmax_{p\in P}x(p).
   > \]
   > Then the points
   > \[
   >   v_0,v_1,\dots,v_m
   > \]
   > produced by this construction are exactly the vertices of the upper hull of
   > \(P\), and the slopes encountered along the way are strictly decreasing.
