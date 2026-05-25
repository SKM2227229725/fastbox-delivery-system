from src.utils.loader import load_data
from src.services.assignment_service import assign_packages
from src.services.delivery_service import simulate_delivery

def main():
    # Load the base case data
    data = load_data("data/base_case.json")

    # Assign each package to the nearest agent (based on warehouse location)
    assignments = assign_packages(
        data["agents"],
        data["warehouses"],
        data["packages"]
    )

    # Compute delivery distances (warehouse → destination)
    results = simulate_delivery(
        assignments,
        data["warehouses"],
        data["packages"]
    )

    # Print the report
    print("\nDELIVERY REPORT")
    print("-" * 40)
    total_distance = 0.0
    for r in results:
        print(f"Package: {r['package_id']} | Agent: {r['agent_id']} | Distance: {r['distance']}")
        total_distance += r['distance']
    print("-" * 40)
    print(f"Total Distance: {total_distance:.2f}")

if __name__ == "__main__":
    main()