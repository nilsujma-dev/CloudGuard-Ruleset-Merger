## JSON Ruleset Merger for Check Point CloudGuard

This Python script is adeptly tailored for merging and managing JSON files that are exports of Check Point CloudGuard Rulesets. The script is particularly useful for security administrators and DevOps teams who work with CloudGuard and need to consolidate, deduplicate, and update rulesets exported from different CloudGuard instances or environments.

### Key Features
1. **Merging CloudGuard Rulesets**: Specifically designed to handle JSON exports of Check Point CloudGuard Rulesets, merging data from two distinct files.
2. **Unique Rule Identification**: Ensures that each rule is uniquely identified and merged based on `logicHash` and `ruleId`, which are specific to CloudGuard's rule structure.
3. **Baseline Category Special Handling**: For rules tagged with the "Baseline" category, the script updates the `complianceTag` attribute to reflect this categorization.
4. **Duplication Resolution**: In cases of overlapping rules, the script prioritizes updating existing records, particularly for those marked as "Baseline".

### Usage in CloudGuard Context
The script is intended to be run with paths to two JSON files containing CloudGuard Ruleset exports, along with the path for the desired output file:
```
python3 merge.py path_to_first_cloudguard_json path_to_second_cloudguard_json path_to_output_json
```

### Script Functions
- `load_json(file_name)`: Loads JSON data from a CloudGuard Ruleset export file.
- `save_json(file_name, data)`: Saves processed and merged JSON data to a file.
- `merge_unique_data(file1, file2, output_file)`: Merges and processes rulesets from two CloudGuard export files into a single consolidated file.

### Workflow
1. **Loading Ruleset Data**: The script begins by loading ruleset data from two CloudGuard JSON export files.
2. **Processing and Merging Rulesets**: It then identifies unique rules, merging them and handling special cases like rules categorized under "Baseline".
3. **Saving the Merged Ruleset**: The consolidated ruleset is then saved to an output file, with a confirmation message indicating successful saving.

### Importance for CloudGuard Users
- **Efficient Management**: Streamlines the process of managing and consolidating rules across different CloudGuard instances.
- **Data Integrity and Compliance**: Ensures that rules are not duplicated and that special categories like "Baseline" are properly maintained, which is crucial for compliance and security posture.

---

This readme summary is specifically tailored for GitHub repository documentation, focusing on the script's application in the context of managing Check Point CloudGuard Ruleset exports. It emphasizes the script's functionality in merging, deduplicating, and correctly categorizing rules for efficient security management.
