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
heat = Heat.get_by_label(simulation, "Heat 1")
heat.change_magnitude(110)
# CreateHeat(TotalHeat="78 W", Body="0:26/0:140/0:143")
