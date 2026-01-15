from ansys.discovery.core.conditions.heat import Heat
from ansys.discovery.core.discovery import Discovery
from ansys.discovery.core.quantities.pint_utils import ureg
import json
from datetime import datetime
from pathlib import Path
 
from ansys.discovery.core.discovery import Discovery
discovery = Discovery(host="localhost", port=50051)

# Recorded commands:
Heat.change_magnitude()
Heat.change_magnitude()
Heat.change_magnitude()
Heat.change_magnitude()
