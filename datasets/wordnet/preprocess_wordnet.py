import os
from collections import Counter, defaultdict

# Step 1: Read all files
file_names = ["train.txt", "valid.txt", "test.txt"]
entities = set()
relations = set()
all_facts = []  # To store all facts for all.txt
file_stats = {}  # To store number of triples per file

# To calculate node degrees
entity_degree = defaultdict(int)
relation_count = Counter()

for file_name in file_names:
    with open(file_name, "r") as file:
        triples = [line.strip().split("\t") for line in file]
        file_stats[file_name] = len(triples)  # Count triples
        for head, relation, tail in triples:
            entities.add(head)
            entities.add(tail)
            relations.add(relation)
            all_facts.append((head, relation, tail))  # Save the fact
            # Update node degrees and relation count
            entity_degree[head] += 1
            entity_degree[tail] += 1
            relation_count[relation] += 1

# Step 2: Map entities to unique IDs
entity2id = {entity: idx for idx, entity in enumerate(sorted(entities))}

# Step 3: Map relations to unique IDs
relation2id = {relation: idx for idx, relation in enumerate(sorted(relations))}

# Step 4: Write entities2id.txt
with open("old_dictionaries/entities2id.txt", "w") as entity_file:
    for entity, idx in entity2id.items():
        entity_file.write(f"{entity}\t{idx}\n")

# Step 5: Write relation2id.txt
with open("old_dictionaries/relation2id.txt", "w") as relation_file:
    for relation, idx in relation2id.items():
        relation_file.write(f"{relation}\t{idx}\n")

# Step 6: Write all.txt
with open("all.txt", "w") as all_file:
    for head, relation, tail in all_facts:
        all_file.write(f"{head}\t{relation}\t{tail}\n")

# Calculate statistics
total_entities = len(entities)
total_relations = len(relations)
average_degree = sum(entity_degree.values()) / total_entities
max_degree = max(entity_degree.values())
min_degree = min(entity_degree.values())

# Print the statistics
print("Number of triples in each file:")
for file_name, count in file_stats.items():
    print(f"  {file_name}: {count}")

print(f"\nTotal number of unique entities: {total_entities}")
print(f"Total number of unique relations: {total_relations}")

print("\nNode degree statistics (considering all facts):")
print(f"  Average degree: {average_degree:.2f}")
print(f"  Max degree: {max_degree}")
print(f"  Min degree: {min_degree}")

print("\nRelation frequencies:")
for relation, count in relation_count.items():
    print(f"  {relation}: {count}")
