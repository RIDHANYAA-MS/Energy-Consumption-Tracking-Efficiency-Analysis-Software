import csv

HIGH_USAGE_THRESHOLD = 2.0  # kWh

def read_energy_data(file_path):
    """Reads energy consumption data from a CSV file"""
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({
                "time": row["timestamp"],
                "power": float(row["power_kwh"])
            })
    return data

def analyze_consumption(data):
    """Calculates peak and average energy consumption"""
    values = [entry["power"] for entry in data]
    peak = max(values)
    average = sum(values) / len(values)
    return peak, average

def detect_high_usage(data):
    """Identifies high-consumption periods"""
    high_usage = []
    for entry in data:
        if entry["power"] > HIGH_USAGE_THRESHOLD:
            high_usage.append(entry)
    return high_usage

if __name__ == "__main__":
    energy_data = read_energy_data("energy_data.csv")

    peak, average = analyze_consumption(energy_data)
    high_usage_periods = detect_high_usage(energy_data)

    print("Peak Energy Usage:", peak, "kWh")
    print("Average Energy Usage:", round(average, 2), "kWh")

    if high_usage_periods:
        print("\nHigh Consumption Periods:")
        for entry in high_usage_periods:
            print(f"Time: {entry['time']} | Usage: {entry['power']} kWh")
    else:
        print("\nNo high consumption periods detected")
