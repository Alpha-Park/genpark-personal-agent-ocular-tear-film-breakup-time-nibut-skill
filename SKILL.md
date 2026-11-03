---
name: genpark-personal-agent-ocular-tear-film-breakup-time-nibut-skill
version: 1.0.0
description: Calculates Non-Invasive Tear Film Break-Up Time (First NIBUT, Average NIBUT), Ocular Protection Index (OPI), and Tear Stability Index (TSI%) according to TFOS DEWS II guidelines.
authors:
  - GenPark Ecosystem
tags:
  - personal-agent
  - ophthalmology
  - tear-film
  - nibut
  - dry-eye
  - tfos-dews-ii
  - zero-dependency
---

# Ocular Non-Invasive Tear Film Break-Up Time (NIBUT) Skill

## Mathematical Formulation

Ocular Protection Index (OPI):

$$\text{OPI} = \frac{\text{First NIBUT (s)}}{\text{Interblink Interval (s)}}$$

- $\text{OPI} \ge 1.0$: Ocular surface protected throughout the blink cycle.
- $\text{OPI} < 1.0$: Tear film rupture occurs before blinking, exposing the corneal epithelium to desiccating airflow.

Tear Stability Index (TSI%):

$$\text{TSI} \, (\%) = \min\left(100.0, \, \frac{\text{Average NIBUT (s)}}{15.0} \times 100\right)$$

## TFOS DEWS II Classification
- **Normal Tear Homeostasis**: $\text{First NIBUT} \ge 10.0\text{ s}$
- **Mild-to-Moderate Tear Film Instability**: $5.0\text{ s} \le \text{First NIBUT} < 10.0\text{ s}$
- **Severe Evaporative Dry Eye Disease (DED)**: $\text{First NIBUT} < 5.0\text{ s}$
