import requests


def send_post(method: str):
    request_body = {"method": method, "jsonrpc": "2.0", "id": 1}
    res = requests.post("http://0.0.0.0:9898/rpc", json=request_body)
    return res.json()


def get_sensor_info():
    sensor_response = send_post(method="get_info")
    sensor_info = sensor_response["result"]
    return sensor_info


def get_sensor_reading():
    sensor_response = send_post(method="get_reading")
    sensor_reading = sensor_response["result"]
    return sensor_reading


def test_sanity():
    sensor_info = get_sensor_info()

    sensor_name = sensor_info.get("name")
    assert isinstance(sensor_name, str), "Sensor name is not a string"

    sensor_hid = sensor_info.get("hid")
    assert isinstance(sensor_hid, str), "Sensor hid is not a string"

    sensor_model = sensor_info.get("model")
    assert isinstance(sensor_model, str), "Sensor model is not a string"

    sensor_firmware_version = sensor_info.get("firmware_version")
    assert isinstance(sensor_firmware_version, float), "Sensor firmware version is not a string"

    sensor_reading_interval = sensor_info.get("reading_interval")
    assert isinstance(sensor_reading_interval, int), "Sensor reading interval is not a string"

    sensor_reading = get_sensor_reading()
    assert isinstance(sensor_reading, float), "Sensor doesn't seem to register temperature"

    print("Sanity test passed")

