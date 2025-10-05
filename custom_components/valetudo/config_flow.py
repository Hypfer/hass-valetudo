from __future__ import annotations

from typing import Any

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.core import callback

from .const import DOMAIN


class FlowHandler(ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        return self.async_show_menu(
            step_id="user",
            menu_options=["icons"],
        )

    async def async_step_icons(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        for entry in self._async_current_entries():
            if entry.data.get("entry_type") == "icons":
                return self.async_abort(reason="icons_instance_exists")

        if user_input is not None:
            return self.async_create_entry(
                title="Valetudo Icons",
                data={"entry_type": "icons"}, 
            )

        return self.async_show_form(step_id="icons")
