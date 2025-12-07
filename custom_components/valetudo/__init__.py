import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import device_registry as dr

from .const import DOMAIN
from .custom_icons import async_setup_icons

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    if entry.data.get("entry_type") == "icons":
        await async_setup_icons(hass) 
        
    # else tbd


    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:

    return True

