import pandas as pd
from physics import hydraulic_power

def build_features(df):
    df = df.copy()

    df["hydraulic_power"] = df.apply(
        lambda x: hydraulic_power(x.flow, x.head), axis=1
    )

    df["efficiency"] = df["hydraulic_power"] / df["power"]
    df["deviation"] = df["power"] / (df["hydraulic_power"] / 0.65)

    return df
