import re
import json
import os

def analyze(file_dir):
    body = {
    "ERRORS": [],
    }

    try:
        if os.path.getsize(file_dir) == 0:
            return "File is empty"
    
        with open(file_dir) as f:
            a_errors, a_warnings, a_info = 0 ,0 ,0
            for log in f:
                if re.search("ERROR", log):
                    a_errors +=  1
                    body["ERRORS"].append(log)
                if re.search("WARNING", log):
                    a_warnings +=  1
                if re.search("INFO", log):
                    a_info +=  1
    except (FileNotFoundError):
        return "File not found"
        
    body["Number of ERRORS"] = a_errors
    body["Number of WARNINGS"] = a_warnings
    body["Number of INFO"] = a_info
    

    json_str = json.dumps(body, indent=4)
    with open("./reports/report.json", "w") as f:
        f.write(json_str)
        

    return (a_errors,a_warnings,a_info)
