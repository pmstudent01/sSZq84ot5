"""
Vehicle Service App
Demonstrates full CRUD usage of the VehicleServiceClient.
"""

import os
from client import VehicleServiceClient


def print_vehicle(vehicle: dict) -> None:
    print(
        f"  [{vehicle['id']}] {vehicle['nickName']} — "
        f"{vehicle['year']} {vehicle['make']} {vehicle['model']} "
        f"(VIN: {vehicle['vin']}, Miles: {vehicle['miles']})"
    )


def main():
    base_url = os.environ.get("VEHICLE_SERVICE_BASE_URL", "http://localhost:3000")
    api_key = os.environ.get("VEHICLE_SERVICE_API_KEY")

    client = VehicleServiceClient(base_url=base_url, api_key=api_key)

    print(f"Connecting to Vehicle Service at {base_url}\n")

    # ── 1. List all vehicles ──────────────────────────────────────────
    print("=== All Vehicles ===")
    vehicles = client.get_all_vehicles()
    if vehicles:
        for v in vehicles:
            print_vehicle(v)
    else:
        print("  (no vehicles found)")

    # ── 2. Create a vehicle ───────────────────────────────────────────
    print("\n=== Creating a Vehicle ===")
    new_vehicle = client.create_vehicle(
        nick_name="The Lisa Marie",
        vin="4M2DV11W4RDJ53329",
        make="Mercury",
        model="Villager",
        year="1994",
        miles=159864,
    )
    print("  Created:")
    print_vehicle(new_vehicle)
    vehicle_id = new_vehicle["id"]

    # ── 3. Retrieve the vehicle ───────────────────────────────────────
    print(f"\n=== Retrieving Vehicle {vehicle_id} ===")
    vehicle = client.get_vehicle(vehicle_id)
    print_vehicle(vehicle)

    # ── 4. Update the vehicle ─────────────────────────────────────────
    print(f"\n=== Updating Vehicle {vehicle_id} ===")
    updated = client.update_vehicle(vehicle_id, miles=159999)
    print("  Updated:")
    print_vehicle(updated)

    # ── 5. Delete the vehicle ─────────────────────────────────────────
    print(f"\n=== Deleting Vehicle {vehicle_id} ===")
    client.delete_vehicle(vehicle_id)
    print(f"  Vehicle {vehicle_id} deleted successfully.")

    # ── 6. Confirm deletion ───────────────────────────────────────────
    print("\n=== All Vehicles (after deletion) ===")
    vehicles = client.get_all_vehicles()
    if vehicles:
        for v in vehicles:
            print_vehicle(v)
    else:
        print("  (no vehicles found)")


if __name__ == "__main__":
    main()
