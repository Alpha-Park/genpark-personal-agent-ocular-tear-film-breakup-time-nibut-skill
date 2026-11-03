"""
MCP Server for Ocular Non-Invasive Tear Film Break-Up Time (NIBUT) Skill.
Provides standard Model Context Protocol JSON-RPC tool endpoints.
"""

import sys
import json
from client import TearFilmBreakupTimeClient


def main():
    client = TearFilmBreakupTimeClient()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception:
            continue

        method = req.get("method")
        msg_id = req.get("id")

        if method == "tools/list":
            res = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "tools": [
                        {
                            "name": "evaluate_nibut",
                            "description": "Calculates Non-Invasive Tear Film Break-Up Time (First NIBUT, Average NIBUT), Ocular Protection Index (OPI), and Tear Stability Index (TSI%) according to TFOS DEWS II guidelines.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "first_break_time_sec": {
                                        "type": "number",
                                        "description": "First localized tear film rupture time in seconds."
                                    },
                                    "average_break_time_sec": {
                                        "type": "number",
                                        "description": "Average break-up time over corneal surface in seconds."
                                    },
                                    "interblink_interval_sec": {
                                        "type": "number",
                                        "description": "Mean interblink interval in seconds (default: 6.0)."
                                    },
                                    "ruptured_area_pct_at_blink": {
                                        "type": "number",
                                        "description": "Percentage of corneal surface with broken tear film at blink (default: 12.0)."
                                    },
                                    "eye_examined": {
                                        "type": "string",
                                        "description": "OD (right eye) or OS (left eye)."
                                    }
                                },
                                "required": [
                                    "first_break_time_sec",
                                    "average_break_time_sec"
                                ]
                            }
                        }
                    ]
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif method == "tools/call":
            params = req.get("params", {})
            name = params.get("name")
            args = params.get("arguments", {})

            if name == "evaluate_nibut":
                try:
                    out = client.evaluate_nibut(**args)
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": json.dumps(out, indent=2)}]
                        }
                    }
                except Exception as e:
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "isError": True,
                        "error": {"code": -32000, "message": str(e)}
                    }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()


if __name__ == "__main__":
    main()
