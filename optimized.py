import json
import time


start_time = time.time()

with open("datas/sienna1.json", "r") as f:
    datas = json.load(f)

# Données des actions
actions = datas["actions"]

actions = [action for action in actions if action["price"] > 0]
# Contraintes
max_budget = 500


# Fonction pour calculer le ratio profit/coût d'une action
def calculate_ratio(action):
    if action["price"] != 0:
        if action["profit"] != 0:
            return action["profit"] / action["price"]
        else:
            return float("-inf")
    else:
        return float("-inf")


# Tri des actions en fonction du ratio profit/coût (ordre décroissant)
sorted_actions = sorted(actions, key=calculate_ratio, reverse=True)
# print(sorted_actions)
# Sélection des actions gloutonnes jusqu'à atteindre la contrainte de budget
best_portfolio = []
remaining_budget = max_budget
total_cost_portfolio = 0

for action in sorted_actions:
    if action["price"] <= remaining_budget:
        best_portfolio.append(action)
        remaining_budget -= action["price"]
        total_cost_portfolio += action["price"]

tps_execution = time.time() - start_time

# Affichage du meilleur résultat
print("Meilleur portefeuille d'actions :")
for action in best_portfolio:
    print(f"- {action['name']}")
print(
    "Bénéfice total :",
    sum(action["price"] * (action["profit"] / 100) for action in best_portfolio),
)
print("Coût total :", total_cost_portfolio)
print("Temps d'exécution :", tps_execution, "secondes")
