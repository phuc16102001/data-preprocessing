# Data mining - Preprocessing
A simple implementation for pre-processing data

## Features
The implementation provide some basic data pre-processing tasks, including: 
- List missing information
- Imputing data
- Normalizing data
- Remove samples
- Create a new attribute with expresison

## Usage
Each feature listed above will be able to use by its correspoding file. We need to execute these file with command line interface using the argument parameters following the below sections. In this project, we use **csv** data file.

# List missing information 
This feature gives you the ability to see:
- The number of samples
- The number of missing sample (sample which miss one or more attribute)
- The missing attribute with its number of samples

To run the file, you need to use:
```bash
list-missing.py <input-path> 
```
Explaination of arguments:
- `<input-path>`: the path direct to .csv file

Example:
```
list-missing.py "../data/house-prices.csv"
```

# Imputing data
This feature gives you able the ability impute the missing value using different methods:
- Mode: Fill with the value that is the most frequent one
- Median: Calculate the median of values and use that value to impute
- Mean: Calculate the mean of value and use that value to impute

> **Note: the median and mean method only use for numeric attribute!**

To run the file, you need to use:
```bash
impute.py <input-path> --method=<method> --columns <column 1> ... <column N> --out=<output-path> 
```
Explaination of arguments:
- `<input-path>`: the path direct to .csv file
- `<method>`: the imputing method (`mean`, `median`, `mode`)
- `<column 1>...<column N>`: the attributes to be imputed
- `<output-path>`: the .csv file to output

Example:
```
impute.py "../data/house-prices.csv" --method="median" --columns LotArea LotFrontage --out="../output/out.csv"
```

# Normalizing data
This feature gives you the ability to normalize the numeric value using different methods:
- Min-max: Normalize the value min to `0`, max to `1` and other value gets between `(0,1)`. Using the formula: $$\frac{value-min}{max-min}$$
- Z-score: A normalization strategy avoid the outlier issue based on mean and standard deviation. Using the formula: $$\frac{value-\mu}{\sigma}$$

To run the file, you need to use:
```bash
normalize.py <input-path> --method=<method> --columns <column 1> ... <column N> --out=<output-path> 
```
Explaination of arguments:
- `<input-path>`: the path direct to .csv file
- `<method>`: the normalizing method (`min-max`,`z-score`)
- `<column 1>...<column N>`: the attributes to be normalized
- `<output-path>`: the .csv file to output

Example:
```
normalize.py "../data/house-prices.csv" --method="z-score" --columns LotArea LotFrontage --out="../output/out.csv"
```

# Remove samples
This feature gives you the ability to remove duplicated and missing data:

## Remove missing sample and attribute
In this feature, you need to determine a threshold and choosing whether removing attribute or sample. For instance, you can remove the sample whose missing rate of attribute is more than 50% (or 0.5).

We use the correspoding file `remove-threshold.py`:
```bash
remove-threshold.py <input-path> --threshold=<threshold> --axis=<axis> --out=<output-path> 
```

Explaination of arguments:
- `<input-path>`: the path direct to .csv file
- `<threshold>`: the threshold value
- `<axis>`: removing `sample` or `attribute`
- `<output-path>`: the .csv file to output

Example:
```
remove-threshold.py "../data/house-prices.csv" --threshold=0.5 --axis="sample" --out="../output/out.csv" 
```

## Remove duplicated samples
In this feature, we only remove duplicated samples. Two samples are duplicated if all its attribute are same.

We use the correspoding file `remove-duplicated.py`:
```bash
remove-duplicated.py <input-path> --out=<output-path> 
```

Explaination of arguments:
- `<input-path>`: the path direct to .csv file
- `<output-path>`: the .csv file to output

Example:
```
remove-duplicated.py "../data/house-prices.csv" --out="../output/out.csv" 
```

# Create a new attribute with expression
Using the feature, you can create a new attribute with a give expression. For example, with the dataframe whose attribute are `width`, `height`, we can create a new attribute `width*height`

Executing the file:
```
evaluate.py <input-path> --expression=<expression> --out=<output-path>
```

Explaination of arguments:
- `<input-path>`: the path direct to .csv file
- `<expression>`: the string of expression
- `<output-path>`: the .csv file to output

Example:
```
evaluate.py "../data/scoreboard.csv" --expression="Math*2+Literature*2+English" --out="../output/out.csv"
```

# Implement documentation
The project provide 6 feature files:
- `evaluate.py`
- `impute.py`
- `list-missing.py`
- `normalize.py`
- `remove-duplicated.py`
- `remove-threshold.py`

These file using `FileHandler.py` to interact with CSV file (import and export)

With the basic core model, we build an Dataset (or dataframe) contains a list of attributes and a list of sample. Each sample model, we store its attribute and value with dictionary data structure. You can refer from `Dataset.py` and `Sample.py`

Moreover, to dealing with different mathematics calculation, we seperate math functions into `Utils.py` (e.g. findMean, findMedian, normalize, etc)

# Contribution
This project is done by [phuc16102001](https://github.com/phuc16102001) and [Qambitions](https://github.com/Qambitions) during participating the "Data mining" course in HCMUS (Ho Chi Minh University of Science). References are welcome but please ***do not copy without permission***.