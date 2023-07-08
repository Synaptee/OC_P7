import json

with open("datas/actions.json", "r") as f:
    datas = json.load(f)

# Données des actions
actions = datas["actions"]

# Contraintes
max_budget = 500


def generate_combinations(actions: list, r: int) -> list:
    """Generate all possible combinations of r actions from a list of actions"""
    combinations = []
    n = len(actions)
    indices = list(range(r))

    while indices[0] < n - r + 1:
        combination = [actions[i] for i in indices]
        combinations.append(combination)

        # Générer le prochain indice
        i = r - 1
        while i >= 0 and indices[i] == i + n - r:
            i -= 1

        if i < 0:
            break

        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1

    return combinations


def calculate_portfolio_profit(portfolio):
    # total_cost = sum(action["cost"] for action in portfolio)
    total_profit = sum(action["price"] * action["profit"] for action in portfolio)
    return total_profit


best_portfolio = []
best_profit = 0
total_cost_portfolio = 0

# Génération de toutes les combinaisons possibles d'actions
for r in range(1, len(actions) + 1):
    combinations = generate_combinations(actions, r)

    for combination in combinations:
        portfolio = list(combination)
        total_cost = sum(action["price"] for action in portfolio)

        # Vérification des contraintes
        if total_cost <= max_budget:
            total_profit = calculate_portfolio_profit(portfolio)

            # Mise à jour du meilleur résultat
            if total_profit > best_profit:
                best_portfolio = portfolio
                best_profit = total_profit
                total_cost_portfolio = total_cost

# Affichage du meilleur résultat
print("Meilleur portefeuille d'actions :")
for action in best_portfolio:
    print(f"- {action['name']}")
print("Bénéfice total :", best_profit)
print("Coût total :", total_cost_portfolio)
