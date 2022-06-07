import os
import pandas as pd
from matplotlib import pyplot as plt

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")

product_id = input("Please enter the product id: ")

opinions = pd.read_json(f"opinions/{product_id}.json")

opinions_count = len(opinions)
pros_count = opinions["pros"].map(bool).sum()
cons_count = opinions["cons"].map(bool).sum()
average_score = opinions["score"].mean().round(2)

stars_recommendation = pd.crosstab(opinions["rcmd"], opinions["score"], dropna=False)
#print(stars_recommendation)

recomendation =opinions["rcmd"].value_counts()
recomendation.plot.pie(
    label="",
    title="Recommendations: "+product_id,
    labels =["Not recommend","Recommend","No opinion"],
    colours=["crimson","forestgreen", "grey"],
    autopact= lambda p: f"{p:1f}%".format(p) if p>0 else""
)
plt.savefig(f"plots/{product_id}rcmd.png")
plt.close()

stars= opinions["score"].value_counts().sort_index().reindex(list(np.arange(0,5.5,0.5)), fill_value=0)
stars.plot.bar(
        color="hotpink"
)

plt.title("Opinions")
plt.xlabel("Count of stars")
plt.ylabel("count of oopinions")
plt.grid(True, axis="y")
plt.xticks(rotations=0)
plt.savefig(f"plots/{product_id}_stars.png")
plt.close()
