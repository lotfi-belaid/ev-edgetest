def validate_telemetry(telemetry):
    results = {}

    temperature = telemetry["temperature"]
    voltage = telemetry["voltage"]
    current = telemetry["current"]
    state = telemetry["state"]

    results["temperature"] = 0 <= temperature <= 80
    results["voltage"] = 350 <= voltage <= 450
    results["current"] = 0 <= current <= 50
    results["state"] = state != "FAULT"

    return results


def print_validation_results(results):
    print("\n--- TELEMETRY VALIDATION ---")

    for check, passed in results.items():

        if passed:
            print(f"{check}: PASS")
        else:
            print(f"{check}: FAIL")

    print("----------------------------\n")