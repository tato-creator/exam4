# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Programming in Python
# ## Exam: June 10, 2025
#
#
# You can solve the exercises below by using standard Python 3.12 libraries, NumPy, Matplotlib, Pandas, PyMC.
# You can browse the documentation: [Python](https://docs.python.org/3.12/), [NumPy](https://numpy.org/doc/1.26/index.html), [Matplotlib](https://matplotlib.org/3.10.0/users/index.html), [Pandas](https://pandas.pydata.org/pandas-docs/version/2.2/index.html), [PyMC](https://www.pymc.io/projects/docs/en/stable/api.html).
# You can also look at the [slides](https://homes.di.unimi.it/monga/lucidi2425/pyqb00.pdf) or your code on [GitHub](https://github.com).
#
#
# **The exam is "open book", but it is strictly forbidden to communicate with others or "ask questions" online (i.e., stackoverflow is ok if the answer is already there, but you cannot ask a new question or use ChatGPT and similar products). Suspicious canned answers or plagiarism among student solutions will cause the invalidation of the exam for all the people involved.**
#
# To test examples in docstrings use
#
# ```python
# import doctest
# doctest.testmod()
# ```

# **SOLVE EACH EXERCISE IN ONE OR MORE NOTEBOOK CELLS AFTER THE QUESTION.**

import numpy as np
import pandas as pd  # type: ignore
import matplotlib.pyplot as plt # type: ignore
import pymc as pm   # type: ignore
import arviz as az  # type: ignore

# ### Exercise 1 (max 3 points)
#
# The file [rhinos.csv](./rhinos.csv) (Duthé, Vanessa (2023), Reductions in home-range size and social interactions among dehorned black rhinoceroses (Diceros bicornis), Dryad, Dataset, https://doi.org/10.5061/dryad.gf1vhhmt5) contains:
#
# - Date: date of rhino sighting
# - RhinosAtSighting: id of individual rhino
# - Sex: sex of individual rhino
# - Horn: indicating horned or dehorned rhino at time of sighting
# - DateBorn: date of birth of individual rhino
# - Reserve: reserve where sighting occured
#
# Read the data in a pandas DataFrame. Be sure  that the columns `Date` and `DateBorn` has dtype `pd.datetime64[ns]`.
#
df = pd.read_csv("rhinos.csv", parse_dates=["Date", "DateBorn"])
df.dtypes

pass

# ### Exercise 2 (max 3 points)
#
# Add a column `Age` with the age in weeks of the rhinos at the time of the sighting.
#
df["Age"] = (df["Date"] - df["DateBorn"]).dt.days / 7
df.head()

pass

# ### Exercise 3 (max 7 points)
#
# Define a function `dehornings` that takes a list of sightings "Horned" or "Dehorned" and counts how many times the rhino was dehorned.
# For example, if the sightings are `["Horned", "Horned", "Dehorned"]`, the rhino was dehorned once; if the sightings are `["Dehorned", "Dehorned", "Dehorned"]` the rhino was dehorned once; if the sightings are `["Horned", "Horned", "Horned", "Horned"]` the rhino was never dehorned; if the sightings are `["Dehorned", "Horned", "Dehorned"]` the rhino was dehorned two times.
#
# To get the full marks, you should declare correctly the type hints and add a test within a doctest string.
from typing import List

def dehornings(sightings: List[str]) -> int:
    """
    Count how many times a rhino was dehorned.

    >>> dehornings(["Horned", "Horned", "Dehorned"])
    1
    >>> dehornings(["Dehorned", "Dehorned", "Dehorned"])
    1
    >>> dehornings(["Horned", "Horned", "Horned"])
    0
    >>> dehornings(["Dehorned", "Horned", "Dehorned"])
    2
    """
    count = 0
    prev = "Horned"
    for s in sightings:
        if prev == "Horned" and s == "Dehorned":
            count += 1
        prev = s
    return count

pass

# ### Exercise 4 (max 5 points)
#
# Apply the function defined in Exercise 3 to the data referring to the rhinos and find the rhino that was dehorned the most. Please note that you should order the list of sightings by `Date`.
# ordiniamo per data
df_sorted = df.sort_values("Date")

# raggruppiamo per rhino
dehorn_counts = (
    df_sorted.groupby("RhinosAtSighting")["Horn"]
    .apply(list)
    .apply(dehornings)
)

# rhino più dehorned
most_dehorned_rhino = dehorn_counts.idxmax()
most_dehorned_count = dehorn_counts.max()

most_dehorned_rhino, most_dehorned_count

pass

# ### Exercise 5 (max 2 points)
#
# Compute for each rhino the weeks between the first and the last sighting.
weeks_span = (
    df.groupby("RhinosAtSighting")["Date"]
    .agg(lambda x: (x.max() - x.min()).days / 7)
)
weeks_span.head()

pass

# ### Exercise 6 (max 4 points)
#
# Plot a histogram of the number of rhinos observed in each reserve
reserve_counts = df["Reserve"].value_counts()

plt.figure()
reserve_counts.plot(kind="hist")
plt.xlabel("Number of rhinos observed")
plt.ylabel("Frequency")
plt.title("Histogram of rhinos per reserve")
plt.show()

pass

# ### Exercise 7 (max 4 points)
#
# Plot together the histograms of the number of male and female rhinos observed in each reserve
male_counts = df[df["Sex"] == "M"]["Reserve"].value_counts()
female_counts = df[df["Sex"] == "F"]["Reserve"].value_counts()

plt.figure()
plt.hist(male_counts, alpha=0.5, label="Males")
plt.hist(female_counts, alpha=0.5, label="Females")
plt.legend()
plt.xlabel("Number of rhinos observed")
plt.ylabel("Frequency")
plt.title("Male vs Female rhinos per reserve")
plt.show()

pass

# ### Exercise 8 (max 5 points)
#
# Consider this statistical model:
#
# - a parameter $\alpha$ is normally distributed with mean 0 and standard deviation 2.
# - a parameter $\beta$ is normally distributed with mean 0 and standard deviation 2.
# - $\sigma$ is exponentially distributed with $\lambda = 1$
# - the observed mean number of dehorned sightings for each `Reserve` is normally distributed with a standard deviation of $\sigma$ and a mean given by $\alpha + \beta\cdot N$, where $N$ is number of (unique) rhinos in the reserve.
#
# Code this model with pymc, sample the model, and plot the summary of the resulting estimation by using `az.plot_posterior`.
#
#
#
#
# numero rhinos per reserve
N_rhinos = df.groupby("Reserve")["RhinosAtSighting"].nunique()

# mean number of dehorned sightings per reserve
mean_dehorned = (df[df["Horn"] == "Dehorned"].groupby("Reserve").size().reindex(N_rhinos.index, fill_value=0)/ N_rhinos)

N = N_rhinos.values
Y = mean_dehorned.values
with pm.Model() as model:
    alpha = pm.Normal("alpha", mu=0, sigma=2)
    beta = pm.Normal("beta", mu=0, sigma=2)
    sigma = pm.Exponential("sigma", lam=1)

    mu = alpha + beta * N

    Y_obs = pm.Normal("Y_obs", mu=mu, sigma=sigma, observed=Y)

    trace = pm.sample(2000, tune=1000, chains=2)
  
az.plot_posterior(trace)
plt.show()

pass
