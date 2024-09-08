#! /usr/bin/env python3

import json
import os
import sys
import argparse
import yaml

"""
# METADATA
# scope: package
# title: No more than 15 persistent entities within one domain model
# description: The bigger the domain models, the harder they will be to maintain. It adds complexity to your security model as well. The smaller the modules, the easier to reuse.
# authors:
# - Xiwen Cheng <x@cinaq.com>
# custom:
#  category: Maintainability
#  rulename: NumberOfEntities
#  severity: MEDIUM
#  rulenumber: 002_0001
#  remediation: Split domain model into multiple modules.
#  input: "*/DomainModels$DomainModel.yaml"
"""

def parse(rule_file: str):
    """
    Parse the rule file.
    """
    metadata_lines = []

    with open(rule_file, "r") as f:
        for line in f.readlines():
            if line.startswith("# METADATA"):
                continue
            clean_line = line.replace("# ", "", 1).strip()
            if line.startswith("#"):
                metadata_lines.append(clean_line)
            else:
                break
    raw_yaml = "\n".join(metadata_lines)
    metadata = yaml.load(raw_yaml, Loader=yaml.SafeLoader)
    return metadata

def generate_rules_docs(rules_dir: str, output_dir: str):
    """
    Generate the rules documentation from the rules directory.
    """
    for rule in os.listdir(rules_dir):
        out_dir = os.path.join(output_dir, rule)
        in_dir = os.path.join(rules_dir, rule)
        os.makedirs(out_dir, exist_ok=True)

        if os.path.isdir(in_dir):
            for file in os.listdir(in_dir):
                if file.endswith(".rego") and not file.endswith("_test.rego"):
                    in_file = os.path.join(in_dir, file)
                    out_file = os.path.join(out_dir, file.replace(".rego", ".md"))
                    generate_rule_docs(in_file, out_file)

def get_test_file(rule_file: str):
    """
    Get the test file for the rule.
    """
    test_file = rule_file.replace(".rego", "_test.rego")
    if not os.path.exists(test_file):
        return "# No test file found"

    with open(test_file, "r") as f:
        body = f.read()
    return body

def generate_rule_docs(rule_file: str, output_file: str):
    rule = parse(rule_file)

    title = rule.get("title", "Untitled")
    description = rule.get("description", "No description provided")
    remediation = rule.get("remediation", "No remediation provided")
    del rule["title"]
    del rule["description"]
    del rule["remediation"]
    del rule["custom"]

    with open(output_file, "w") as f:
        f.write(f"# {title}\n")
        f.write(f"{remediation}\n")
        f.write(f"## Metadata\n")
        f.write(f"## Description\n")
        f.write(f"{description}\n")
        f.write(f"## Remediation\n")
        f.write(f"```yaml\n")
        f.write(f"{yaml.dump(rule)}\n")
        f.write(f"```\n")
        f.write(f"## Test cases\n")
        f.write(f"```rego\n")
        f.write(f"{get_test_file(rule_file)}\n")
        f.write(f"```\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--rules", type=str, default="rules", help="The directory containing the rule definitions")
    parser.add_argument("-o", "--output", type=str, default="docs/rules", help="The directory to output the rules documentation")
    args = parser.parse_args()

    generate_rules_docs(args.rules, args.output)

