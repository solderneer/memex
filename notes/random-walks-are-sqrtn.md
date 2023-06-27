---
title: "Random walks are sqrt(N)"
emoji: "🚶"
pubDate: 08-Jun-2023
updatedDate: 08-Jun-2023
tags: ["topic/science", "type/principles"]
---

**tldr;** The basic essence of this note is to demonstrate the importance of vision. Instead of blindly chasing everything that is shiny, a person with vision can walk in a straight line. This is important, a person walking in a straight line with N steps moves with $O(n)$ But a person walking in a random walk, only can move on the order, $O(\sqrt{n})$.

I originally saw this assertion in, [The Art of doing Science and Engineering](https://www.goodreads.com/book/show/530415.The_Art_of_Doing_Science_and_Engineering) by Richard Hamming.

---

Assuming there are independent random variables, $Z_1, Z_2, Z_3, ...$ such that each variable is either -1 or 1 with a 50% probability. Then create a length-N sequence such that $S_0 = 0$ and $S_N = \sum_{j=1}^{N} Z_j$.

It follows that the expected value, $E(S_N) = \sum_{j=1}^{N} E(Z_j) = 0$

We're going to need another property of sums to move on here,


$$
\begin{align*} S_N^2 &= \bigg(\sum_{j=1}^{N} Z_j\bigg)\bigg(\sum_{j=1}^{N} Z_j\bigg) \\ &= (Z_1, Z_2, Z_3, ..., Z_N)(Z_1, Z_2, Z_3, ..., Z_N) \\ &= (Z_1^2, Z_2^2, Z_3^2, ..., Z_N^2) + 2Z_1(Z_2, Z_3, ..., Z_N) + 2Z_2(Z_3, ..., Z_N) + ... \\ &= \bigg(\sum_{i=1}^{N} Z_i^2\bigg) + 2\bigg(\sum_{1 \leq i \lt j \leq n}^{N} Z_iZ_j\bigg) \end{align*}
$$



Then, we can find:

$$
\begin{align*}
E(S_N^2) &= \bigg(\sum_{i=1}^{N} E(Z_i^2)\bigg) + 2\bigg(\sum_{1 \leq i \lt j \leq n}^{N} E(Z_iZ_j)\bigg) \\
&= N
\end{align*}
$$

because $E(Z_iZ_j)$ is 0, since the variables are independent and have a mean of 0. So it follows that the distance is roughly on the order of $\sqrt{N}$.