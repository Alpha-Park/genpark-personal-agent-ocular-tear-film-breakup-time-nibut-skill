"""
Example usage of Ocular Non-Invasive Tear Film Break-Up Time (NIBUT) Skill.
Demonstrates stable tear film homeostasis vs evaporative dry eye disease (MGD).
"""

import json
from client import TearFilmBreakupTimeClient


def main():
    print("=== Testing Ocular NIBUT Skill ===")
    client = TearFilmBreakupTimeClient()

    # 1. Healthy young subject with intact lipid layer (First NIBUT = 14.5s, Avg NIBUT = 18.2s, IBI = 5.0s -> OPI = 2.9, TSI = 100%)
    res_stable = client.evaluate_nibut(
        first_break_time_sec=14.5,
        average_break_time_sec=18.2,
        interblink_interval_sec=5.0,
        ruptured_area_pct_at_blink=0.0,
        eye_examined="OD"
    )
    print("\n[Case 1: Normal Stable Tear Film]")
    print(json.dumps(res_stable, indent=2))

    # 2. Patient with severe meibomian gland dysfunction / evaporative dry eye (First NIBUT = 2.8s, Avg NIBUT = 4.2s, IBI = 7.0s -> OPI = 0.40, TSI = 28%)
    res_dry_eye = client.evaluate_nibut(
        first_break_time_sec=2.8,
        average_break_time_sec=4.2,
        interblink_interval_sec=7.0,
        ruptured_area_pct_at_blink=35.0,
        eye_examined="OS"
    )
    print("\n[Case 2: Severe Evaporative Dry Eye Disease (DEWS II)]")
    print(json.dumps(res_dry_eye, indent=2))

    # Assertions
    assert res_stable["indices"]["ocular_protection_index_opi"] >= 1.0
    assert "Normal" in res_stable["clinical_classification"]["tfos_dews2_category"]
    assert res_dry_eye["indices"]["ocular_protection_index_opi"] < 1.0
    assert "Severe" in res_dry_eye["clinical_classification"]["tfos_dews2_category"]
    print("\n[SUCCESS] Ocular NIBUT tests passed!")


if __name__ == "__main__":
    main()
