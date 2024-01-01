import csv

class DataAccess:
    def read_csv(self, filename: str) -> list[dict[str, str]]:
        with open(filename, 'r', encoding='utf-8') as file:
            data = csv.DictReader(file)
            data_list: list[dict[str,]] = []
            for row in data:
                data_list.append(row)
            return data_list