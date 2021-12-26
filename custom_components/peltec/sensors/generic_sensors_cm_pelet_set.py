from homeassistant.const import DEVICE_CLASS_TEMPERATURE, TEMP_CELSIUS, TIME_MINUTES

CM_PELET_SET_SENSOR_TEMPERATURES = {
    "B_Tk1": [
        TEMP_CELSIUS,
        "mdi:thermometer",
        DEVICE_CLASS_TEMPERATURE,
        "Boiler Temperature",
    ],
    "C1B_Tpol1": [
        TEMP_CELSIUS,
        "mdi:thermometer",
        DEVICE_CLASS_TEMPERATURE,
        "Circuit 1 Flow Temperature",
    ],
    "C2B_Tpol1": [
        TEMP_CELSIUS,
        "mdi:thermometer",
        DEVICE_CLASS_TEMPERATURE,
        "Circuit 2 Flow Temperature",
    ],
    "B_Tak1": [
        TEMP_CELSIUS,
        "mdi:thermometer",
        DEVICE_CLASS_TEMPERATURE,
        "Buffer Tank Up",
    ],
    "B_Tak2": [
        TEMP_CELSIUS,
        "mdi:thermometer",
        DEVICE_CLASS_TEMPERATURE,
        "Buffer Tank Down",
    ],
    "B_Tva1": [
        TEMP_CELSIUS,
        "mdi:thermometer",
        DEVICE_CLASS_TEMPERATURE,
        "Outdoor Temperature",
    ],
}


CM_PELET_SET_SENSOR_MISC = {
    "B_KONF_STR": ["", "mdi:information", None, "Setup"],
    "B_netMon": ["", "mdi:remote", None, "Remote Start Enabled"],
    "B_cmsr100": ["", "mdi:information", None, "Pellet Tank Level"],
    "C1B_CircType": ["", "mdi:information", None, "Circuit 1 Heating Type"],
    "C2B_CircType": ["", "mdi:information", None, "Circuit 2 Heating Type"],
    "C1B_misC": ["", "mdi:pipe-valve", None, "Circ1 Mix-Valve Closing"],
    "C1B_misO": ["", "mdi:pipe-valve", None, "Circ1 Mix-Valve Opening"],
    "C2B_misC": ["", "mdi:pipe-valve", None, "Circ2 Mix-Valve Closing"],
    "C2B_misO": ["", "mdi:pipe-valve", None, "Circ2 Mix-Valve Ipening"],
    "B_Pk": ["", "mdi:pump", None, "Boiler Pump"],
    "C1B_P": ["", "mdi:pump", None, "Circuit 1 Pump"],
    "C1B_onOff": ["", "mdi:information", None, "Circuit 1 State"],
    "C2B_P": ["", "mdi:pump", None, "Circuit 2 Pump"],
    "C2B_onOff": ["", "mdi:information", None, "Circuit 2 State"],
    "B_fan": ["", "mdi:fan", None, "Heater Fan State"],
    "B_gri": ["", "mdi:fire", None, "Heater State"],
    "CNT_0": [TIME_MINUTES, "mdi:fire", None, "Heater State Counter"],
    "CNT_3": ["", "mdi:fire", None, "Heater Start Counter (?)"],
    "CNT_4": [TIME_MINUTES, "mdi:fan", None, "Heater Fan Counter"],
    "CNT_5": [TIME_MINUTES, "mdi:fire", None, "Heater State Counter"],
    "CNT_6": ["", "mdi:fire", None, "Heater uključenje (?)"],
    "CNT_7": [TIME_MINUTES, "mdi:information", None, "Pellet Transporter Counter"],
    "CNT_8": [TIME_MINUTES, "mdi:pump", None, "Boiler Pump Counter"],
}

CM_PELET_SET_GENERIC_SENSORS = {
    **CM_PELET_SET_SENSOR_TEMPERATURES,
    **CM_PELET_SET_SENSOR_MISC,
}
