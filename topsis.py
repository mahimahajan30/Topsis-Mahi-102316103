import pandas as pd
import numpy as np

def calculate_topsis(input_file, weights, impacts, output_file):
    df = pd.read_csv(input_file)

    data = df.iloc[:, 1:]

    weights = list(map(float, weights.split(',')))
    impacts = impacts.split(',')

    # Normalization
    norm = data / np.sqrt((data**2).sum())

    # Weighting
    weighted = norm * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)
    rank = score.rank(ascending=False)

    df['Topsis Score'] = score
    df['Rank'] = rank

    df.to_csv(output_file, index=False)
    print("✅ Output saved:", output_file)
