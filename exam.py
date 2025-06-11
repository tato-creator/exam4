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

pass

# ### Exercise 2 (max 3 points)
#
# Add a column `Age` with the age in weeks of the rhinos at the time of the sighting.
#

pass

# ### Exercise 3 (max 7 points)
#
# Define a function `dehornings` that takes a list of sightings "Horned" or "Dehorned" and counts how many times the rhino was dehorned.
# For example, if the sightings are `["Horned", "Horned", "Dehorned"]`, the rhino was dehorned once; if the sightings are `["Dehorned", "Dehorned", "Dehorned"]` the rhino was dehorned once; if the sightings are `["Horned", "Horned", "Horned", "Horned"]` the rhino was never dehorned; if the sightings are `["Dehorned", "Horned", "Dehorned"]` the rhino was dehorned two times.
#
# To get the full marks, you should declare correctly the type hints and add a test within a doctest string.

pass

# ### Exercise 4 (max 5 points)
#
# Apply the function defined in Exercise 3 to the data referring to the rhinos and find the rhino that was dehorned the most. Please note that you should order the list of sightings by `Date`.

pass

# ### Exercise 5 (max 2 points)
#
# Compute for each rhino the weeks between the first and the last sighting.

pass

# ### Exercise 6 (max 4 points)
#
# Plot a histogram of the number of rhinos observed in each reserve

pass

# ### Exercise 7 (max 4 points)
#
# Plot together the histograms of the number of male and female rhinos observed in each reserve

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

pass
