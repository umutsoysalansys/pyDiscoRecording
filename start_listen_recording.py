from ansys.discovery.core.conditions.heat import Heat
from ansys.discovery.core.discovery import Discovery
from ansys.discovery.core.quantities.pint_utils import ureg
import json
from datetime import datetime
from pathlib import Path

print("Automatic task is running...")
 
from ansys.discovery.core.discovery import Discovery
discovery = Discovery(host="localhost", port=50051)
print(discovery)
print(discovery._client)

# Create output files next to this script
script_dir = Path(__file__).parent
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = script_dir / f"recording_{timestamp}.py"
log_file = script_dir / f"log_{timestamp}.json"

print(f"Writing recordings to: {output_file}")
print(f"Writing raw logs to: {log_file}")

# Write header with imports and Discovery setup
header = """from ansys.discovery.core.conditions.heat import Heat
from ansys.discovery.core.discovery import Discovery
from ansys.discovery.core.quantities.pint_utils import ureg
import json
from datetime import datetime
from pathlib import Path
 
from ansys.discovery.core.discovery import Discovery
discovery = Discovery(host="localhost", port=50051)
simulation = discovery.get_all_simulations()[0]

# Recorded commands:
"""

with open(output_file, 'w') as f, open(log_file, 'w') as log_f:
    f.write(header)
    f.flush()
    
    # Initialize log file with JSON array
    log_f.write("[\n")
    log_f.flush()
    
    first_event = True

    # Iterate over the generator to actually execute the recording subscription
    for event_data in discovery.subscribe_to_recording():
        raw_event = event_data['raw_event']
        script_command = event_data['script_command']
        
        print(f"Method: {raw_event['recording_method']}")
        print(f"Signature: {raw_event['recording_method_signature']}")
        print(f"Parameters: {raw_event['recording_parameters']}")
        print(f"Converted Script: {script_command}")

        # Write raw event to log file
        if not first_event:
            log_f.write(",\n")
        log_f.write(json.dumps(event_data, indent=2))
        log_f.flush()
        first_event = False

        # Write the converted PyDiscovery script command
        if script_command:
            f.write(f"{script_command}\n")
            f.flush()  # Ensure data is written immediately