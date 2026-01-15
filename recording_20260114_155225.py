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
# Open(FilePath="D:\AnsysDev\pydiscovery\tests\test_files\Heat_Sink_Thermal.dsco")
heat = Heat.get_by_label(simulation, "Heat 1")
heat.change_magnitude(55)
body1 = discovery.design.components[0].components[0].bodies[0]
power = 959 * ureg.watt
Heat.create_volumetric(simulation, body1, value=power)
