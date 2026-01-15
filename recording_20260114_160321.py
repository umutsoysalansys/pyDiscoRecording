from ansys.discovery.core.conditions.heat import Heat
from ansys.discovery.core.discovery import Discovery
from ansys.discovery.core.quantities.pint_utils import ureg
import json
from datetime import datetime
from pathlib import Path
 
from ansys.discovery.core.discovery import Discovery
discovery = Discovery(host="localhost", port=50051)
simulation = discovery.get_all_simulations()[0]

# Recorded commands:
design = discovery.open_design("C:/Users/usoysal/AppData/Local/Temp/DiscoveryApiServerData/a4cbde9f-f3f8-407d-ac67-9cd4cf3c0a27/Heat_Sink_Thermal/Extraction/Heat_Sink_Thermal.dsco")
heat = Heat.get_by_label(simulation, "Heat 1")
heat.change_magnitude(25)
body1 = design.components[0].components[0].bodies[0]
power = 99 * ureg.watt
Heat.create_volumetric(simulation, body1, value=power)
