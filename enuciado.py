import pickle

with open('model_C=10.bin', 'rb') as f:
    dv, model = pickle.load(f)

# Para cada versão (v1, v2, v3), use os dados fornecidos no exercício
customer = {...}  # dados do exercício
X = dv.transform([customer])
score = model.predict_proba(X)[0, 1]
print(round(score, 3))
