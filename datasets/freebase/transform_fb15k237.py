from pathlib import Path


# TODO treat _v appendix different

def clean_relation(relation: str):
    """Removes characters that are not accepted in relations."""
    for char in ["(", ")", "_", ":", "-", "/", "."]:
        relation = relation.replace(char, "")
    return relation


def convert_rule(weight: float, head_rel: str, body1_rel: str, body2_rel=None):
    """Converts the rule into the desired format."""
    # head_rel = clean_relation(head_rel)
    # body1_rel = clean_relation(body1_rel)
    # body2_rel = clean_relation(body2_rel)

    if body2_rel is None:
        formatted_rule = f"{float(weight)}:rel_{head_rel}(x,y) = rel_{body1_rel}(x,y)"
    # Convert to desired format
    else:
        formatted_rule = f"{float(weight)}:rel_{head_rel}(x,y) = rel_{body1_rel}(x,z) and rel_{body2_rel}(z,y)"
    return formatted_rule


def remove_suffix_if_present(string):
    """ some relations end with _v and then cannot be found in the relation dict
    to find them, the suffix needs to be removed """
    if string.endswith("_v"):
        return string[:-2]
    else:
        return string


def read_file_to_dict(filename: str):
    """
    reads entities.dict or relations.dict
    keys and values are separated by \tab
    """
    dictionary = {}
    with open(Path(filename), 'r') as file:
        for line in file:
            parts = line.split('\t')
            if len(parts) == 2:
                string_val = parts[1].strip()
                int_val = int(parts[0])
                dictionary[string_val] = int_val
    return dictionary

def get_suffixes(parts):
    """
    Extracts suffix information from a list of strings.

    Args:
    - parts (list of str): A list of strings where each string may end with "_v".

    Returns:
    - list of bool: A list of boolean values indicating whether each string in `parts`
      ends with "_v". True if the string ends with "_v", False otherwise.
    """
    parts = parts[1:]  # Remove the first element (assuming it's to remove "score")
    return [True if _p.endswith("_v") else False for _p in parts]


def process_rules(weight_filter: float, rel_dict: dict):
    """
    Reads rules from the input file, processes them, and writes to the output file.
    Skip rules if confidence is too low.
    """
    input_file = "datalog_program/MLN_rule.txt"
    output_file = f"datalog_program/fb15k237_rules_{weight_filter}.txt"
    num_rules, num_rules_one_body, num_rules_two_body = 0, 0, 0

    if Path(output_file).exists():
        raise FileExistsError(
            f"Output file {output_file} already exists. It will be overwritten. "
            "Delete it first and rerun again, if you want to continue."
        )

    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        num_rules_with_v = 0
        for line in infile:
            parts = line.strip().split("\t")

            # If rule does not have the shape of a body of one or two atoms, skip it
            if len(parts) not in [3, 4]:
                continue

            # Check if minimum weight is met
            weight = float(parts[0])
            if weight < weight_filter:
                continue

            if any(get_suffixes(parts)):
                num_rules_with_v += 1
                continue

            head_rel = rel_dict[remove_suffix_if_present(parts[1])]
            body_rels = [rel_dict[remove_suffix_if_present(parts[i])] for i in range(2, len(parts))]

            if len(parts) == 3:
                num_rules_one_body += 1
                body2_rel = None  # No second body for one-body rules
            else:
                num_rules_two_body += 1
                body2_rel = body_rels[1]  # Second body for two-body rules

            formatted_rule = convert_rule(weight, head_rel, body_rels[0], body2_rel)

            num_rules += 1
            outfile.write(formatted_rule + "\n")

    print(f"Generated file {output_file} with {num_rules} rules: {num_rules_one_body} with one body atom, {num_rules_two_body} with two body atoms.")
    print(f'{num_rules_with_v} rules have been skipped because they have atoms annotated with _v. It is not implemented yet how to treat them exaclty. ')


def process_facts(input_file: str, ent_dict: dict, rel_dict: dict):
    """ generate fact files with integers from dictionaries instead of strings """

    # Replace strings with values from entities_dict and relations_dict
    modified_lines = []
    with open(Path(input_file), 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split('\t')
            assert len(parts) == 3
            head_val = ent_dict[parts[0]]
            tail_val = ent_dict[parts[2]]
            relation_val = rel_dict[parts[1]]
            modified_lines.append(f"{head_val}\trel_{relation_val}\t{tail_val}\n")

    output_file = input_file.replace('_str', '')
    if Path(output_file).exists():
        msg = f"Output file {output_file} already exists. It will be overwritten. Delete it first and rerun again, if you want to continue."
        raise FileExistsError(msg)

    # Write the modified content to the output file
    with open(Path(output_file), 'w') as outfile:
        outfile.writelines(modified_lines)

    print(f"Generated file {output_file} with {len(lines)} facts.")


# load the dicts
entities_dict = read_file_to_dict('entities.dict')
relations_dict = read_file_to_dict('relations.dict')

filters = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
# Process the rules
for weight_filter in filters:
    try:
        process_rules(weight_filter=weight_filter, rel_dict=relations_dict)
    except FileExistsError:
        continue

# for _facts in ['train_str.txt', 'valid_str.txt', 'test_str.txt', 'all_str.txt']:
#     process_facts(_facts, ent_dict=entities_dict, rel_dict=relations_dict)