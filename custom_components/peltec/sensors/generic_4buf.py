from homeassistant.const import (
    DEVICE_CLASS_TEMPERATURE,
    TEMP_CELSIUS,
    TIME_MINUTES,
    PERCENTAGE,
)

PELTEC_4BUF_SENSOR_TEMPERATURES = {
    "B_Tak1_1": [
        TEMP_CELSIUS,
        "mdi:thermometer",
        DEVICE_CLASS_TEMPERATURE,
        "Buffer Tank Temparature Up",
    ],
    "B_Tak2_1": [
        TEMP_CELSIUS,
        "mdi:thermometer",
        DEVICE_CLASS_TEMPERATURE,
        "Buffer Tank Temparature Down",
    ],
    "B_Tdpl1": [
        TEMP_CELSIUS,
        "mdi:thermometer",
        DEVICE_CLASS_TEMPERATURE,
        "Flue Gas",
    ],
    "B_Tpov1": [
        TEMP_CELSIUS,
        "mdi:thermometer",
        DEVICE_CLASS_TEMPERATURE,
        "Mixer Temperature",
    ],
    "B_Tk1": [
        TEMP_CELSIUS,
        "mdi:thermometer",
        DEVICE_CLASS_TEMPERATURE,
        "Boiler Temperature",
    ],
}

PELTEC_4BUF_SENSOR_COUNTERS = {
    "CNT_0": [TIME_MINUTES, "mdi:timer", None, "Burner Work"],
    "CNT_1": [
        "",
        "mdi:counter",
        None,
        "Number of Burner Start",
    ],
    "CNT_2": [
        TIME_MINUTES,
        "mdi:timer",
        None,
        "Feeder Screw Work",
    ],
    "CNT_3": [
        TIME_MINUTES,
        "mdi:timer",
        None,
        "Flame Duration",
    ],
    "CNT_4": [
        TIME_MINUTES,
        "mdi:timer",
        None,
        "Fan Working Time",
    ],
    "CNT_5": [
        TIME_MINUTES,
        "mdi:timer",
        None,
        "Electric Heater Working Time",
    ],
    "CNT_6": [
        TIME_MINUTES,
        "mdi:timer",
        None,
        "Vacuum Turbine Working Time",
    ],
    "CNT_7": [
        "",
        "mdi:counter",
        None,
        "Vacuum Turbine Cycles Number",
    ],
    "CNT_8": [TIME_MINUTES, "mdi:timer", None, "Time on D6"],
    "CNT_9": [TIME_MINUTES, "mdi:timer", None, "Time on D5"],
    "CNT_10": [TIME_MINUTES, "mdi:timer", None, "Time on D4"],
    "CNT_11": [TIME_MINUTES, "mdi:timer", None, "Time on D3"],
    "CNT_12": [TIME_MINUTES, "mdi:timer", None, "Time on D2"],
    "CNT_13": [TIME_MINUTES, "mdi:timer", None, "Time on D1"],
    "CNT_14": [TIME_MINUTES, "mdi:timer", None, "Time on D0"],
    "CNT_15": ["", "mdi:counter", None, "Reserve Counter"],
}

PELTEC_4BUF_SENSOR_MISC = {
    "B_fan": ["rpm", "mdi:fan", None, "Fan"],
    "B_fanB": ["rpm", "mdi:fan", None, "Fan B"],
    "B_Oxy1": ["% O2", "mdi:gas-cylinder", None, "Lambda Sensor"],
    "B_FotV": ["kOhm", "mdi:fire", None, "Fire Sensor"],
    "B_vanjS": [
        TEMP_CELSIUS,
        "mdi:thermometer",
        DEVICE_CLASS_TEMPERATURE,
        "Outdoor Temperature",
    ],
    "B_cm2k": ["", "mdi:state-machine", None, "CM2K Status"],
    "B_misP": [PERCENTAGE, "mdi:pipe-valve", None, "Mixing Valve"],
    "B_P1": ["", "mdi:pump", None, "Boiler Pump"],
    "B_zahP1": ["", "mdi:pump", None, "Boiler Pump Demand"],
    "B_gri": ["", "mdi:fire-circle", None, "Electric Heater"],
    "B_puz": ["", "mdi:transfer-up", None, "Pellet Transporter"],
}


PELTEC_4BUF_SENSOR_SETTINGS = {
    "PVAL_66_0": [
        "",
        "mdi:thermometer",
        DEVICE_CLASS_TEMPERATURE,
        "Setting Buffer Tank Temperatures",
        {"PDEF_66_0": "Default", "PMIN_66_0": "Min", "PMAX_66_0": "Max"},
    ],
    "PVAL_67_0": [
        "",
        "mdi:thermometer",
        DEVICE_CLASS_TEMPERATURE,
        "Setting Differential of Buffer Tank Temperature",
        {"PDEF_67_0": "Default", "PMIN_67_0": "Min", "PMAX_67_0": "Max"},
    ],
    "PVAL_69_0": [
        "",
        "mdi:thermometer",
        DEVICE_CLASS_TEMPERATURE,
        "Setting Minimal Buffer Tank Temperature",
        {"PDEF_69_0": "Default", "PMIN_69_0": "Min", "PMAX_69_0": "Max"},
    ],
    "PVAL_70_0": [
        "",
        "mdi:thermometer",
        DEVICE_CLASS_TEMPERATURE,
        "Setting Minimal Buffer Tank Temperature-off",
        {"PDEF_70_0": "Default", "PMIN_70_0": "Min", "PMAX_70_0": "Max"},
    ],
}

PELTEC_4BUF_SENSOR_TYPES = {
    **PELTEC_4BUF_SENSOR_TEMPERATURES,
    **PELTEC_4BUF_SENSOR_COUNTERS,
    **PELTEC_4BUF_SENSOR_SETTINGS,
    **PELTEC_4BUF_SENSOR_MISC,
}
