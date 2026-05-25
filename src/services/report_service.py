def generate_report(deliveries):

    print("\nDELIVERY REPORT")
    print("-" * 40)

    total_distance = 0

    for delivery in deliveries:

        print(
            f'Package: {delivery["package_id"]} | '
            f'Agent: {delivery["agent_id"]} | '
            f'Distance: {delivery["distance"]}'
        )

        total_distance += delivery["distance"]

    print("-" * 40)
    print(f"Total Distance: {round(total_distance,2)}")