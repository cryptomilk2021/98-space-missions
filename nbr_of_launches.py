import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from misc import scrub_it

df = scrub_it()
group_df = df.groupby("Origin").count()

plt.bar(group_df.index, group_df.Organisation, color='blue', width=0.7)
plt.xlabel('Origin', fontsize=14)
plt.ylabel('Nbr of missions', fontsize=14)
plt.xticks(rotation=45)
plt.title('Nbr of launches by Origin\n', fontsize=14, fontweight='bold')
plt.show()
