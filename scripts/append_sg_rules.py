import json
import re
import os

# Retrieve the JSON string from the environment variable
SG_RULES = os.getenv("SG_RULES", "[]")  # Default to an empty list if not provided
rules = json.loads(SG_RULES)  # Convert the string to a Python list of dictionaries

# Group rules by sg_name and capture target_dir from each rule
grouped_rules = {}
for rule in rules:
    sg_name = rule["sg_name"]
    target_dir = rule["target_dir"]
    if sg_name not in grouped_rules:
        grouped_rules[sg_name] = {"target_dir": target_dir, "ingress": [], "egress": []}
    if rule["type"] == "ingress":
        grouped_rules[sg_name]["ingress"].append(rule)
    elif rule["type"] == "egress":
        grouped_rules[sg_name]["egress"].append(rule)

# Define a function to process each Terraform file and append new rules
def process_tf_file(tf_file, ingress_rules, egress_rules):
    # Read the existing Terraform file
    with open(tf_file, "r") as file:
        content = file.read()

    # Find all ingress and egress blocks using regex (with dotall flag so newline is included)
    ingress_matches = list(re.finditer(r'(?s)(\s*ingress\s*{.*?})', content))
    egress_matches = list(re.finditer(r'(?s)(\s*egress\s*{.*?})', content))

    # Determine where to insert new ingress rules (after the last ingress block)
    if ingress_matches:
        last_ingress = ingress_matches[-1]
        ingress_insert_index = last_ingress.end()
    else:
        # If no ingress block exists, insert before the first occurrence of "egress" or at the end of the block.
        ingress_insert_index = content.find("egress") if "egress" in content else content.rfind("}")

    # Determine where to insert new egress rules (after the last egress block)
    if egress_matches:
        last_egress = egress_matches[-1]
        egress_insert_index = last_egress.end()
    else:
        egress_insert_index = content.rfind("}")

    # Build new ingress blocks string from the JSON rules
    ingress_blocks = ""
    for rule in ingress_rules:
        ingress_blocks += f"""

  ingress {{
    description = "{rule['description']}"
    from_port   = {rule['port']}
    to_port     = {rule['port']}
    protocol    = "{rule['protocol']}"
    cidr_blocks = ["{rule['cidr']}"]
  }}"""

    # Build new egress blocks string from the JSON rules
    egress_blocks = ""
    for rule in egress_rules:
        egress_blocks += f"""

  egress {{
    description = "{rule['description']}"
    from_port   = {rule['port']}
    to_port     = {rule['port']}
    protocol    = "{rule['protocol']}"
    cidr_blocks = ["{rule['cidr']}"]
  }}"""

    # Insert new ingress rules at the correct location
    updated_content = content[:ingress_insert_index] + ingress_blocks + content[ingress_insert_index:]
    # Adjust egress insertion index by the length of what was added above
    adjusted_egress_index = egress_insert_index + len(ingress_blocks)
    updated_content = updated_content[:adjusted_egress_index] + egress_blocks + updated_content[adjusted_egress_index:]

    # Write back the updated content to the same Terraform file
    with open(tf_file, "w") as file:
        file.write(updated_content)

    print(f"✅ New rules appended to {tf_file} cleanly.")

# Process only the files for which we have JSON rules
for sg_name, info in grouped_rules.items():
    target_dir = info["target_dir"]
    # Construct the expected .tf file path.
    tf_file_path = os.path.join(target_dir, f"{sg_name}.tf")
    if os.path.exists(tf_file_path):
        ingress_rules = info["ingress"]
        egress_rules = info["egress"]
        process_tf_file(tf_file_path, ingress_rules, egress_rules)
    else:
        print(f"⚠️ No .tf file found for {sg_name} in directory {target_dir}. Skipping.")
