---
tags:
  - web-app
  - concepts
---

# Discounted cash flow analysis

Sympheny uses discounted cash flow (DCF) analysis to determine the present value of
expected future cash flows. This approach is crucial for long-term energy projects, as
it accounts for financing factors such as the cost of capital, loan structures, and
risk premiums, ensuring that both initial investments and future cash flows are
properly evaluated.

**Interest rate:**

- **Interest rate as financing cost**: when you take out a loan (especially an
  amortized one, with regular payments), the interest rate directly reflects the cost
  of borrowing that money: it's what the lender charges you.
- **Discounting future cash flows**: the interest rate can also be used to calculate
  the present value of money expected in the future (a process called discounting). In
  this case, it reflects the opportunity cost of capital: the return you might earn
  if you invested the money elsewhere. A risk premium is added to this rate to cover
  risks such as price fluctuations or project-specific uncertainties.
- **Dual use**: in practice, the interest rate is often used both as the cost of
  financing and as part of the discount rate. The effective discount rate can be
  constructed by combining the cost of financing with an additional risk premium.

**Inflation rate:**

The inflation rate is the expected annual percentage increase in the general price
level of goods and services. It indicates the decline in the purchasing power of money
over time and plays a critical role in long-term financial analysis, since it affects
both the costs and revenues of future cash flows in real terms.

The assumption is that the rate of inflation is the same for all costs.

**Discount rate:**

This rate converts future cash flows into their present value, reflecting the
opportunity cost of capital and associated risks. The discount rate is derived by
adjusting the nominal interest rate for inflation, producing a real rate that excludes
inflation effects.

![Discount rate formula](img/discounted-cash-flow-analysis-1.png)

The discount rate also plays a key role in converting one-time costs into an equivalent
annual cost (EAC). This is done using the
[capital recovery factor (CRF)](capital-recovery-factor.md).

**Weighted average cost of capital (WACC):**

In energy planning, the WACC is often used as the discount rate in DCF analysis. When
cash flows are expressed in real terms (with inflation already accounted for), you
might set WACC as the interest rate with inflation assumed to be zero, which results in
the discount rate aligning with the interest rate.

In Sympheny, you define these parameters along with other inputs in the Stage
Parameters step. See [Stages parameters](../parameters/stages.md) for details.
