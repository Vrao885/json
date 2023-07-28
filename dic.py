import json

indian_states = {
    "Andhra Pradesh": "Amaravati",
    "Karnataka": "Bengaluru",
    "Tamil Nadu": "Chennai",
    "Maharashtra": "Mumbai",
    "Kerala": "Thiruvananthapuram",
    "Gujarat": "Gandhinagar",
    "Rajasthan": "Jaipur"
}

def write_to_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    states_file_path = "indian_states.json"
    write_to_json(indian_states, states_file_path)
