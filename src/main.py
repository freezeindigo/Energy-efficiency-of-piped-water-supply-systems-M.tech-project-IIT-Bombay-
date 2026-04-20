import pandas as pd
from src.features import build_features
from src.model import train_model, predict
from src.visualize import plot_efficiency, plot_flow_vs_eff, plot_deviation

# Sample real-ish data (based on your Khardi table)
data = [
    [43.2, 113.7, 36.4],
    [43.2, 113.7, 35.4],
    [43.4, 113.7, 35.2],
    [44.2, 113.7, 36.2],
]

df = pd.DataFrame(data, columns=["flow", "head", "power"])

df = build_features(df)

print(df)

# Train model
model = train_model(df)

# Predict
pred = predict(model, 40, 113.7, 35)
print(f"Predicted efficiency: {pred:.2f}")

# Visualizations
plot_efficiency(df)
plot_flow_vs_eff(df)
plot_deviation(df)
