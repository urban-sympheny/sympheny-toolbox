---
tags:
  - web-app
  - how-to
---

# Execution

Once a scenario is complete, you run it from the **Execution** page. The page has two parts: the solver settings you choose before a run, and the history of the runs you have already made. You can execute a single scenario, or every scenario in the analysis at once.

## Solver parameters

| Setting | What it does |
| --- | --- |
| Objectives | Optimize for a single objective, or for two objectives at once, such as cost and CO2 emissions. |
| Pareto points | With two objectives, how many points of the Pareto front the solver computes. Choose two or more; each point is one solution, representing a different trade-off between the two objectives. |
| Temporal resolution | How many [typical days](../concepts/clustered-profiles.md) the year is clustered into. A higher resolution uses more typical days. |
| MIP gap | How close to proven optimality the solver has to get before it stops. A smaller gap is more precise and slower. |

!!! tip
    Precision costs time. The same scenario can take much longer at a high temporal resolution
    and a 0.5% MIP gap than at a low resolution and a 1% gap, and each extra Pareto point is
    another solve. Start loose while you are still shaping the model, then tighten for the runs
    you want to report.

## Execution history

The page also lists every execution of every scenario in the analysis. Each run keeps a copy of the parameters it used, so earlier results stay reproducible. For each execution, you can:

- Download the [input file](../parameters/index.md), an Excel workbook holding all parameters of the scenario.
- Download the output file, a compressed folder of Excel workbooks holding all results.
- Review the parameters the run used.
- Open the interactive [results dashboard](results-dashboard.md) to explore every solution, stage, and hub in detail.
