import os

from src.utils.loader import load_data
from src.services.assignment_service import assign_packages
from src.services.delivery_service import simulate_delivery

test_folder = "data/tests"

files = sorted(os.listdir(test_folder))

for file in files:

    data = load_data(f"{test_folder}/{file}")

    assignments = assign_packages(
        data["agents"],
        data["warehouses"],
        data["packages"]
    )

    results = simulate_delivery(
        assignments,
        data["warehouses"],
        data["packages"]
    )

    print("\nTEST:", file)
    print(results)