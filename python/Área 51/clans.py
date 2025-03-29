import random

def spin():
    families = {
        'Sharingan': ['Obito', 'Madara', 'Shisui'],
        'Rinnegan': ['Rinnegan'],
        'Ruins': ['Shino', 'Sakura']
    }
    
    probs = {
        'Sharingan': 0.0015,  # 0.15% dividido pelos 3
        'Rinnegan': 0.0005,  # 0.05%
        'Ruins': 0.498  # 50%
    }
    
    all_families = []
    for key, values in families.items():
        prob = probs.get(key, 0.5) / len(values)
        all_families.extend([(key, value, prob) for value in values])
    
    choices, weights = zip(*[(item[:2], item[2]) for item in all_families])
    result = random.choices(choices, weights=weights, k=1)[0]
    
    return result

if __name__ == "__main__":
    result = spin()
    print(f"Você conseguiu: {result[1]} ({result[0]})")
