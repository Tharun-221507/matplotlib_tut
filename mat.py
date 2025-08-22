import matplotlib.pyplot as plt

plt.plot([1,2,3],[1,2,3], label="Linear")
plt.plot([1,2,3],[1,4,9], label="Quadratic")

plt.legend(
    loc='upper left',
    title="Functions",
    fontsize=10,
    frameon=True,
    shadow=True,
    ncol=1,
    facecolor="lightgray",
    edgecolor="blue",
    markerscale=1.5,
    handlelength=3,
    handletextpad=1,
    borderpad=1.2,
    borderaxespad=1.5
)
plt.legend(labels=['poda sunii'])

plt.show()
