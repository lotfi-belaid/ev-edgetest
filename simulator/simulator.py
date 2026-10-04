import json
import random
import time
import argparse
from datetime import datetime, timezone


DEVICE_ID = "ECU-001"


def generate_normal_telemetry():
    return {
        "deviceId": DEVICE_ID,
        "voltage": round(random.uniform(380.0, 420.0), 2),
        "current": round(random.uniform(20.0, 40.0), 2),
        "temperature": round(random.uniform(35.0, 65.0), 2),
        "chargingPower": round(random.uniform(8.0, 15.0), 2),
        "state": "CHARGING",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


def apply_fault(telemetry, fault):
    if fault == "overheat":
        telemetry["temperature"] = round(random.uniform(85.0, 110.0), 2)
        telemetry["state"] = "FAULT"

    elif fault == "voltage-spike":
        telemetry["voltage"] = round(random.uniform(460.0, 520.0), 2)
        telemetry["state"] = "FAULT"

    return telemetry


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--fault",
        choices=["overheat", "voltage-spike"],
        help="Inject a fault into the ECU simulator"
    )

    args = parser.parse_args()

    print(f"Starting simulator for {DEVICE_ID}...")

    if args.fault:
        print(f"Fault injection enabled: {args.fault}")

    while True:
        telemetry = generate_normal_telemetry()

        telemetry = apply_fault(
            telemetry,
            args.fault
        )

        print(json.dumps(telemetry, indent=2))

        time.sleep(1)


if __name__ == "__main__":
    main()