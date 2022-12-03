import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

class InfluxClient:
    def __init__(self) -> None:
        self.token = "91XonVTK0cXpXmwjoF32jKOeMKIkf2LPK4Vm5lURZJKR2mNP9pftxRxvcBu487wUa0hPoggNTImKDFpzzxDQsQ=="
        self.url = "http://influxdb:8086"
        self.org = "ost"
        self.client = influxdb_client.InfluxDBClient(
        url=self.url,
        token=self.token,
        org=self.org)

    def get_data(self, query):
        # Query script
        query_api = self.client.query_api()
        result = query_api.query(org=self.org, query=query)
        results = []
        for table in result:
            for record in table.records:
                results.append((*record))
        return results


def main():
    client = InfluxClient()
    query = 'from(bucket:"my-bucket")\
        |> range(start: -10m)\
        |> filter(fn:(r) => r._measurement == "my_measurement")\
        |> filter(fn:(r) => r.location == "Prague")\
        |> filter(fn:(r) => r._field == "temperature")'
    result = client.get_data(client)
if __name__ == "__main__":
    main()