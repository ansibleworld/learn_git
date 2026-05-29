import json
from pathlib import Path
output = {
      "status": "complete",
      "items_processed": 1492,
      "errors":[]
     }
     
output_path = Path("run_summary.json")
with output_path.open("w") as file:
     json.dump(output, file , indent=1 )
     print(output_path)
     