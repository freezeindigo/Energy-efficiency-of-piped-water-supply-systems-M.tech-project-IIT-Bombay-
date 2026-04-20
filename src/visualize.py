import matplotlib.pyplot as plt

def plot_efficiency(df):
    plt.figure()
    plt.hist(df["efficiency"], bins=10)
    plt.title("Efficiency Distribution")
    plt.xlabel("Efficiency")
    plt.ylabel("Frequency")
    plt.show()

def plot_flow_vs_eff(df):
    plt.figure()
    plt.scatter(df["flow"], df["efficiency"])
    plt.xlabel("Flow")
    plt.ylabel("Efficiency")
    plt.title("Flow vs Efficiency")
    plt.show()

def plot_deviation(df):
    plt.figure()
    plt.plot(df["deviation"])
    plt.title("Deviation (Actual vs Expected Power)")
    plt.show()
