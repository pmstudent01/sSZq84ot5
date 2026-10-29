"""
Vehicle Service API Client
Generated from the Vehicle Service Collection.
"""

import requests


class VehicleServiceClient:
    """Client for the Vehicle Service API."""

    def __init__(self, base_url: str, api_key: str = None):
        """
        Initialize the client.

        Args:
            base_url: The base URL of the Vehicle Service API (e.g. http://localhost:3000)
            api_key:  Optional API key sent as the x-api-key header.
        """
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})
        if api_key:
            self.session.headers.update({"x-api-key": api_key})

    # ------------------------------------------------------------------
    # GET /vehicles
    # ------------------------------------------------------------------
    def get_all_vehicles(self) -> list:
        """
        Retrieve all vehicles.

        Returns:
            List of vehicle dicts.
        Raises:
            requests.HTTPError: on a non-2xx response.
        """
        response = self.session.get(f"{self.base_url}/vehicles")
        response.raise_for_status()
        return response.json()

    # ------------------------------------------------------------------
    # GET /vehicles/:id
    # ------------------------------------------------------------------
    def get_vehicle(self, vehicle_id: int) -> dict:
        """
        Retrieve a single vehicle by ID.

        Args:
            vehicle_id: The integer ID of the vehicle.
        Returns:
            Vehicle dict.
        Raises:
            requests.HTTPError: on a non-2xx response (e.g. 404 Not Found).
        """
        response = self.session.get(f"{self.base_url}/vehicles/{vehicle_id}")
        response.raise_for_status()
        return response.json()

    # ------------------------------------------------------------------
    # POST /vehicles
    # ------------------------------------------------------------------
    def create_vehicle(
        self,
        nick_name: str,
        vin: str,
        make: str,
        model: str,
        year: str,
        miles: int,
    ) -> dict:
        """
        Create a new vehicle.

        Args:
            nick_name: Friendly name for the vehicle.
            vin:       Vehicle Identification Number.
            make:      Manufacturer (e.g. "Mercury").
            model:     Model name (e.g. "Villager").
            year:      Model year as a string (e.g. "1994").
            miles:     Current odometer reading.
        Returns:
            Newly created vehicle dict (includes assigned id).
        Raises:
            requests.HTTPError: on a non-2xx response (e.g. 400, 409).
        """
        payload = {
            "nickName": nick_name,
            "vin": vin,
            "make": make,
            "model": model,
            "year": year,
            "miles": miles,
        }
        response = self.session.post(
            f"{self.base_url}/vehicles",
            json=payload,
        )
        response.raise_for_status()
        return response.json()

    # ------------------------------------------------------------------
    # PATCH /vehicles/:id
    # ------------------------------------------------------------------
    def update_vehicle(self, vehicle_id: int, **fields) -> dict:
        """
        Partially update a vehicle.

        Args:
            vehicle_id: The integer ID of the vehicle to update.
            **fields:   Any subset of: nick_name, vin, make, model, year, miles.
                        snake_case keys are automatically converted to camelCase.
        Returns:
            Updated vehicle dict.
        Raises:
            requests.HTTPError: on a non-2xx response.
        """
        key_map = {
            "nick_name": "nickName",
            "vin": "vin",
            "make": "make",
            "model": "model",
            "year": "year",
            "miles": "miles",
        }
        payload = {key_map.get(k, k): v for k, v in fields.items()}
        response = self.session.patch(
            f"{self.base_url}/vehicles/{vehicle_id}",
            json=payload,
        )
        response.raise_for_status()
        return response.json()

    # ------------------------------------------------------------------
    # DELETE /vehicles/:id
    # ------------------------------------------------------------------
    def delete_vehicle(self, vehicle_id: int) -> None:
        """
        Delete a vehicle by ID.

        Args:
            vehicle_id: The integer ID of the vehicle to delete.
        Raises:
            requests.HTTPError: on a non-2xx response.
        """
        response = self.session.delete(f"{self.base_url}/vehicles/{vehicle_id}")
        response.raise_for_status()
