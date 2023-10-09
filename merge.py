import json
import sys

def load_json(file_name):
    """Load JSON data from a file."""
    with open(file_name, 'r') as f:
        return json.load(f)

def save_json(file_name, data):
    """Save JSON data to a file."""
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {file_name}")

def merge_unique_data(file1, file2, output_file):
    """Merge unique data from two JSON files and save to an output file."""
    data1 = load_json(file1)
    data2 = load_json(file2)
    
    seen_logic_hashes = {}
    seen_rule_ids = {}
    
    unique_data = []
    
    for data in data1 + data2:
        logic_hash = data.get("logicHash")
        rule_id = data.get("ruleId")
        
        # Check if the rule has the "Baseline" category
        is_baseline = data.get("category") == "Baseline"
        
        # If the rule has the "Baseline" category, add "Baseline" to the complianceTag if it's not already there
        if is_baseline:
            tags = data.get("complianceTag", "").split("|")
            if "Baseline" not in tags:
                tags.append("Baseline")
            data["complianceTag"] = "|".join(tags)
        
        if logic_hash not in seen_logic_hashes and rule_id not in seen_rule_ids:
            unique_data.append(data)
            seen_logic_hashes[logic_hash] = is_baseline
            seen_rule_ids[rule_id] = is_baseline
        else:
            # If the rule is a duplicate and has the "Baseline" category, we update the existing rule
            if is_baseline and not seen_logic_hashes[logic_hash]:
                index_to_replace = next(i for i, item in enumerate(unique_data) if item.get("logicHash") == logic_hash)
                unique_data[index_to_replace] = data
                seen_logic_hashes[logic_hash] = True
                seen_rule_ids[rule_id] = True
    
    save_json(output_file, unique_data)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 merge.py <path_to_first_json_file> <path_to_second_json_file> <path_to_output_file>")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    output_file = sys.argv[3]
    merge_unique_data(file1, file2, output_file)
