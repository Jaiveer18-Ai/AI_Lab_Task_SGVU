
def forward_chaining(facts, rules):
    facts = set(facts)

    while True:
        new_fact_found = False

        for conditions, conclusion in rules:
            if set(conditions).issubset(facts) and conclusion not in facts:
                facts.add(conclusion)
                new_fact_found = True

        if not new_fact_found:
            break

    return facts


print("=" * 35)
print("       FORWARD CHAINING")
print("=" * 35)

facts = input("Enter initial facts: ").split()
n = int(input("Enter number of rules: "))

rules = []

for i in range(n):
    conditions = input(f"Enter conditions for rule {i + 1}: ").split()
    conclusion = input("Enter conclusion: ").strip()
    rules.append((conditions, conclusion))

result = forward_chaining(facts, rules)

print("-" * 35)
print("Final facts:", ", ".join(sorted(result)))
print("=" * 35)
