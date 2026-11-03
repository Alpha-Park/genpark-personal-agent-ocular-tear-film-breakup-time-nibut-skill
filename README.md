# Ocular Non-Invasive Tear Film Break-Up Time (NIBUT) Personal Agent Skill

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen.svg)]()
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20JSON--RPC-orange.svg)]()
[![Production Ready](https://img.shields.io/badge/status-production--ready-green.svg)]()

Deterministic, zero-mock personal agent micro-skill for calculating Non-Invasive Tear Film Break-Up Time (First NIBUT, Average NIBUT), Ocular Protection Index (OPI), and Tear Stability Index (TSI%) based on TFOS DEWS II diagnostic standards.

## Architecture

```mermaid
flowchart TD
    A[Automated Keratograph Placido Rings] --> B[Detect First Ring Distortion / Break-up]
    B --> C[Compute First NIBUT & Average NIBUT sec]
    C --> D[Calculate Ocular Protection Index OPI = NIBUT / IBI]
    D --> E[Compute Tear Stability Index TSI%]
    E --> F[DEWS II Diagnostic Stratification]
```

## Quickstart

```python
from client import TearFilmBreakupTimeClient

client = TearFilmBreakupTimeClient()
result = client.evaluate_nibut(
    first_break_time_sec=14.5,
    average_break_time_sec=18.2,
    interblink_interval_sec=5.0
)
print(result)
```

## License

Apache-2.0
