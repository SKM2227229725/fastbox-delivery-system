from src.utils.distance import calculate_distance

def assign_packages(agents, warehouses, packages):
    """
    Handles multiple schemas:
    - agents/warehouses: list of {"id":..., "location":...} OR dict {id: location}
    - packages: contains 'id' and warehouse reference (key can be 'warehouse_id', 'warehouseId', 'warehouse', etc.)
    """
    # Normalize warehouses to dict {id: location}
    if isinstance(warehouses, list):
        wh_dict = {w["id"]: w["location"] for w in warehouses}
    elif isinstance(warehouses, dict):
        wh_dict = warehouses
    else:
        raise TypeError(f"Warehouses must be list or dict, got {type(warehouses)}")

    # Normalize agents to dict {id: location} (for simplicity)
    if isinstance(agents, list):
        agent_dict = {a["id"]: a["location"] for a in agents}
    elif isinstance(agents, dict):
        agent_dict = agents
    else:
        raise TypeError(f"Agents must be list or dict, got {type(agents)}")

    # Detect warehouse key in first package
    if not packages:
        return []
    pkg_sample = packages[0]
    possible_keys = ["warehouse_id", "warehouseId", "warehouse", "source", "wh_id"]
    wh_key = None
    for key in possible_keys:
        if key in pkg_sample:
            wh_key = key
            break
    if wh_key is None:
        raise KeyError(f"No warehouse reference key found. Available keys: {list(pkg_sample.keys())}")

    assignments = []
    for pkg in packages:
        wh_id = pkg[wh_key]
        if wh_id not in wh_dict:
            raise ValueError(f"Warehouse {wh_id} not found for package {pkg['id']}")

        # Find agent with minimum distance to this warehouse
        best_agent_id = min(
            agent_dict.keys(),
            key=lambda aid: calculate_distance(agent_dict[aid], wh_dict[wh_id])
        )

        assignments.append({
            "package_id": pkg["id"],
            "agent_id": best_agent_id,
            "warehouse_id": wh_id
        })
    return assignments