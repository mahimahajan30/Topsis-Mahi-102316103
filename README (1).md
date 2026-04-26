# TOPSIS Assignment

**Name:** Mahi
**Roll Number:** 102316103


## 📌 Project Overview

This project implements the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method in Python to rank alternatives based on multiple criteria.


## ⚙️ Installation

Install the package directly from PyPI:

```
pip install Topsis-Mahi-102316103
```

## 🔗 PyPI Link

https://pypi.org/project/Topsis-Mahi-102316103/


## ▶️ Usage

### Step 1: Import the function

```
from topsis import calculate_topsis
```

### Step 2: Run the function

```
calculate_topsis("input.csv", "1,1,1,1", "+,+,-,+", "output.csv")
```


## 📄 Input File Format

The input CSV file must follow this format:

```
Fund Name,P1,P2,P3,P4
M1,1,2,3,4
M2,4,3,2,1
M3,2,3,4,5
```

### Rules:

* First column → non-numeric (names/IDs)
* Remaining columns → numeric values
* Minimum 3 columns required


## 📊 Output

The output CSV will contain:

* Topsis Score
* Rank


## 🧠 Working Steps of TOPSIS

1. Normalize the data
2. Apply weights
3. Determine ideal best and worst
4. Calculate distance from ideal solutions
5. Compute score
6. Rank alternatives



## 🌐 Web Application (Part-III)

A simple Flask web app is included where users can:

* Upload CSV file
* Enter weights and impacts
* Generate results


## 👨‍💻 Author

Mahi
102316103

