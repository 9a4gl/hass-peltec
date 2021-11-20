from typing import List
from homeassistant.components.sensor import SensorEntity

from .PelTecGenericSensor import PelTecGenericSensor


class PelTecFireGridSensor(PelTecGenericSensor):
    def __init__(self, hass, device, sensor_data, param_ind, param_dir, param_max):
        super().__init__(hass, device, sensor_data, param_ind)
        self.param_dir = param_dir
        self.param_max = param_max

    async def async_added_to_hass(self):
        """Subscribe to sensor events."""
        await super().async_added_to_hass()
        self.param_dir.set_update_callback(self.update_callback)
        self.param_max.set_update_callback(self.update_callback)

    @property
    def native_value(self):
        """Return the value of the sensor."""
        ind = int(self.parameter["value"])
        max = int(self.param_max["value"])
        dir = int(self.param_dir["value"])
        if max < 0:
            return "0"
        text = str(int(ind * 100 / max))
        if dir > 0:
            return "> " + text
        return "< " + text

    @property
    def device_state_attributes(self):
        """Return the state attributes of the sensor."""
        attributes = super().device_state_attributes
        attributes["Ind"] = self.parameter["value"]
        attributes["Max"] = self.param_max["value"]
        attributes["Dir"] = self.param_dir["value"]
        return attributes

    def createEntities(parameters, hass, device) -> List[SensorEntity]:
        entities = []
        entities.append(
            PelTecFireGridSensor(
                hass,
                device,
                ["", "mdi:grid", None, "Fire Grid Position"],
                parameters["B_resInd"],
                parameters["B_resDir"],
                parameters["B_resMax"],
            )
        )
        return entities
