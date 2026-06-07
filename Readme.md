# Valetudo for HASS

This `custom_component` provides functionality for usage of Valetudo within Home Assistant.


## Features

### Icons

<img width="700" src="https://github.com/user-attachments/assets/00131949-896b-45f7-a994-5f8aa664713d" />

### Services

If you have set up at least one `config_entry` for this integration (e.g. the Icons), it will also provide services.

#### Extract Map data

<img width="700" src="https://github.com/user-attachments/assets/a6379c49-4e53-43c0-b914-1f92bcb61f6e" />

This can also for example be used together with https://github.com/gjohansson-ST/response_as_sensor

As an example, to get a sensor housing the current robot position with that custom_integration, you'd be using a template like this:

```
{% set ns = namespace(found=false, data={}) %}
{% for entity in map_data.get('entities', []) %}
  {% if entity.get('__class') == 'PointMapEntity' and entity.get('type') == 'robot_position' %}
    {% set points = entity.get('points', []) %}
    {% if points | length >= 2 %}
      {% set angle = entity.get('metaData', {}).get('angle') %}
      {% set ns.data = {
        "type": "robot_position",
        "x": points[0],
        "y": points[1],
        "angle": angle
      } %}
      {% set ns.found = true %}
    {% endif %}
  {% endif %}
{% endfor %}
{{ (ns.data | to_json | to_json) if ns.found else 'unknown' }}
```

That double `to_json` might not be needed in your use-case (e.g. a script or similar).
It was just necessary to make `response_as_sensor` v1.0 happy.

Depending on your need, you might also want to use the jinja template to transform this data to a different format (e.g. CSV).
It doesn't have to be JSON. Refer to your local LLM for advice on that.

Also, if you use `response_as_sensor` don't forget to set the `Response variable` to `map_data`. That's easy to miss.

## Installation

To install these, you will need [HACS](https://www.hacs.xyz/).

In HACS, add a Custom repository of type Integration with the URL of this Repo.
You will then be able to install this `custom_component`.

After the install, go to the "Devices" section in Home Assistant, click "Add integration" and set up "Valetudo".

<img width="700" src="https://github.com/user-attachments/assets/8e8936e2-145c-4496-9b2b-4f35f83b0217" />
