import requests

class TipStorage:
    def __init__(self):
        self.api_url = "https://6734e0725995834c8a9132f3.mockapi.io/propina"

    def save_tip(self, tip_data):
        payload = {
            "monto": tip_data["total"],
            "propinaa": tip_data["propina"],
            "porcentaje": tip_data["porcentaje"],
            "montoTotalPagar": tip_data["total"] + tip_data["propina"]
        }
        response = requests.post(self.api_url, json=payload)
        return response.json()

    def load_tips(self):
        response = requests.get(self.api_url)
        return response.json()

    def delete_tip(self, tip_id):
        response = requests.delete(f"{self.api_url}/{tip_id}")
        return response.status_code == 200

    def update_tip(self, tip_id, tip_data):
        payload = {
            "monto": tip_data["total"],
            "propinaa": tip_data["propina"],
            "porcentaje": tip_data["porcentaje"],
            "montoTotalPagar": tip_data["total"] + tip_data["propina"]
        }
        response = requests.put(f"{self.api_url}/{tip_id}", json=payload)
        return response.json()

    def search_by_date(self, amount):
        tips = self.load_tips()
        return [tip for tip in tips if float(tip["monto"]) == float(amount)]

    def search_tip(self, search_term):
        tips = self.load_tips()
        return [tip for tip in tips if 
                str(search_term).lower() in str(tip.get("total", "")).lower() or
                str(search_term).lower() in str(tip.get("fecha", "")).lower() or
                str(search_term).lower() in str(tip.get("mesero", "")).lower()]