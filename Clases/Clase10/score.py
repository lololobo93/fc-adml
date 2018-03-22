import pandas as pd
import numpy as np

def QLFScore(c, zoneFunction = lambda j: j, relative = False):
    testCasas = pd.read_csv('test.csv')
    testCasas.loc[:, 'Zona'] = testCasas.Zona.apply(zoneFunction)
    target = testCasas['Precio']
    testCasas.drop(columns = ['Precio'], inplace=True)
    testCasas.insert(0,'Compensate', 1)
    prediction = testCasas.apply(lambda row: np.matmul(row.values, c), axis=1)
    vectorialCost = (prediction.values - target.values)**2
    cost = np.sum(vectorialCost) / (2 * len(vectorialCost))
    if relative:
        cost = cost / 3500000
    print("El error cuadrático es:", cost, "(menor es mejor)")
    return cost