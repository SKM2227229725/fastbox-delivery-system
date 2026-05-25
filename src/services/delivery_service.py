from src.utils.distance import calculate_distance

def simulate_delivery(assignments, warehouses, packages):
    """
    Computes delivery distance (warehouse → destination) for each assignment.
    Handles both list-of-dicts and dict formats for warehouses.
    """
    # Normalize warehouses to dict {id: location}
    if isinstance(warehouses, list):
        wh_loc = {w["id"]: w["location"] for w in warehouses}
    elif isinstance(warehouses, dict):
        wh_loc = warehouses
    else:
        raise TypeError(f"Warehouses must be list or dict, got {type(warehouses)}")

    # Build package destination lookup
    pkg_dest = {p["id"]: p["destination"] for p in packages}

    results = []
    for ass in assignments:
        pkg_id = ass["package_id"]
        wh_id = ass["warehouse_id"]
        dest = pkg_dest[pkg_id]
        dist = calculate_distance(wh_loc[wh_id], dest)
        results.append({
            "package_id": pkg_id,
            "agent_id": ass["agent_id"],
            "distance": round(dist, 2)
        })
    return results