import csv

def get_login_csv():
    with open("Data/LoginData.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            data.append((row["email"], row["password"], row["expected_result"]))
        return data


