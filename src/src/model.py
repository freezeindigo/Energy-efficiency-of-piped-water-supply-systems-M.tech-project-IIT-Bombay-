from sklearn.linear_model import LinearRegression

def train_model(df):
    X = df[["flow", "head", "power"]]
    y = df["efficiency"]

    model = LinearRegression()
    model.fit(X, y)

    return model

def predict(model, flow, head, power):
    return model.predict([[flow, head, power]])[0]
