import random

def loan_approval(name):
    # Simulate a simple approval process (no gender bias)
    approved = random.choice([True, False])
    return f"Loan approval for {name}: {'Approved' if approved else 'Denied'}"

names = ["John", "Priya", "Alex", "Sara", "Michael", "Anita", "David", "Riya"]

results = {name: loan_approval(name) for name in names}

for result in results.values():
    print(result)

# Analysis: Since approval is random and does not use gender, there should be no gender bias.