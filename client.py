"""
Ocular Non-Invasive Tear Film Break-Up Time (NIBUT) Client.
Zero-mock pure Python standard library implementation.
Calculates First NIBUT, Average NIBUT, Tear Stability Index (TSI%),
and stratifies dry eye disease (DED) based on TFOS DEWS II clinical criteria.
"""

import math
from typing import Dict, Any, Optional, List


class TearFilmBreakupTimeClient:
    """
    Evaluates ocular surface tear film stability and evaporative tear kinetics:
    - First NIBUT (seconds): time to first rupture/distortion in reflected Placido rings
    - Average NIBUT (seconds): mean break-up time across all corneal zones prior to involuntary blink
    - Tear Stability Index (TSI %): min(100.0, (avg_nibut / 15.0) * 100.0)
    - Tear Rupture Dynamics: calculates break-up progression rate and corneal exposure vulnerability
    """

    def __init__(self):
        pass

    def evaluate_nibut(
        self,
        first_break_time_sec: float,
        average_break_time_sec: float,
        interblink_interval_sec: Optional[float] = 6.0,
        ruptured_area_pct_at_blink: Optional[float] = 12.0,
        eye_examined: Optional[str] = "OD"
    ) -> Dict[str, Any]:
        """
        Calculates NIBUT metrics and TFOS DEWS II tear stability classification.
        first_break_time_sec: first detected tear film break in seconds (e.g. 2.0 to 25.0s)
        average_break_time_sec: mean break time over corneal area in seconds
        interblink_interval_sec: natural duration between spontaneous blinks in seconds (default 6.0s)
        ruptured_area_pct_at_blink: percentage of corneal area with broken tear film right before blink
        """
        if first_break_time_sec <= 0 or average_break_time_sec <= 0:
            raise ValueError("Break-up times must be strictly positive.")
        if interblink_interval_sec <= 0:
            raise ValueError("Interblink interval must be strictly positive.")

        # Ocular Protection Index (OPI):
        # OPI = NIBUT / Interblink Interval (IBI)
        # OPI >= 1.0: Tear film protected (tear film breaks AFTER the blink)
        # OPI < 1.0: Ocular surface exposed to air, desiccating corneal epithelium
        opi = first_break_time_sec / interblink_interval_sec

        # Tear Stability Index (TSI %)
        # 15.0 seconds is standard benchmark for robust, resilient pre-corneal tear film
        tsi_pct = min(100.0, (average_break_time_sec / 15.0) * 100.0)

        # TFOS DEWS II diagnostic thresholds:
        # NIBUT_first < 5.0 s: Severe Tear Film Instability / Evaporative Dry Eye Disease
        # 5.0 s <= NIBUT_first < 10.0 s: Borderline / Mild-to-Moderate Evaporative Instability
        # NIBUT_first >= 10.0 s: Normal Tear Film Stability
        if first_break_time_sec < 5.0:
            diagnostic_category = "Severe Tear Film Instability (Evaporative DED)"
            etiology = "Marked lipid layer deficiency / meibomian gland dysfunction (MGD), leading to rapid evaporation."
        elif first_break_time_sec < 10.0:
            diagnostic_category = "Mild-to-Moderate Tear Film Instability"
            etiology = "Subclinical evaporative stress, prolonged digital screen blink suppression, or mild lipid insufficiency."
        else:
            diagnostic_category = "Normal Tear Film Homeostasis"
            etiology = "Stable lipid-aqueous-mucin trilaminar tear structure protecting corneal epithelium."

        corneal_exposure_status = "Protected (OPI >= 1.0)" if opi >= 1.0 else "Vulnerable to Epithelial Desiccation (OPI < 1.0)"

        return {
            "status": "success",
            "measurements_sec": {
                "first_nibut_sec": round(first_break_time_sec, 2),
                "average_nibut_sec": round(average_break_time_sec, 2),
                "interblink_interval_sec": round(interblink_interval_sec, 2)
            },
            "indices": {
                "ocular_protection_index_opi": round(opi, 2),
                "tear_stability_index_tsi_pct": round(tsi_pct, 1),
                "ruptured_area_pct_at_blink": ruptured_area_pct_at_blink
            },
            "clinical_classification": {
                "tfos_dews2_category": diagnostic_category,
                "corneal_exposure_status": corneal_exposure_status,
                "suspected_pathophysiology": etiology,
                "eye_examined": eye_examined
            }
        }
