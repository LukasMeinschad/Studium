# Biological Background

> DPP4 is an enzyme that breaks down incretine hormones, like GLP1, which are involved in glucose regulation.

+ GLP-1 is a hormone which lowers blood sugar levels by stimulating insulin secretion
+ Supresses the Glucagon Secretion
+ Glucagon Like Peptide plays a major role in regulating blood sugar levels
+ Inhibitin DPP-4 allows the GLP-1 hormone to stay activee in the body longer

## Structure and Binding Side

+ Type II Transmembrane Serine Protease
+ Homodimer in humans

**Characteristics of the Catalytic Side**

Glutamic Acid = GLU

Arg = Arginine

+ Serine 630 as Catalytic Centre
+ Substrades are anchored by interations of GLU 205 and GLU 206
+ Arg 135 has hydrogen bond interactions with carbonyl
+ Phenylalanine performs $\pi$ stacking

> All Inhibitors have small hydrophobic moieties that can occupy the S1 pocket and hydrophlic groups that engage with the Glu205, Glu206, Arg125



# Compound Data Aquisition

**IC50 Value**

The IC50 value, or half-maximal inhibitory concentration, is a measure of how much of a substance is needed to inhibit a biological process by 50%_. It's commonly used to determine the potency of an antagonist drug in pharmacological research. A lower IC50 value generally indicates a more potent drug. 


+ Mean of $pIC50$ lies at about $6$
+ 

# Molecular Filtering

**Lipinskis Rule of 5**:

+ Molecular Weight less than 500 Daltons
+ Log P should be less or equal to five
+ Hydrogen bond Donorns no more than 5 hydrogen bonds
+ No more than 10 hydrogen bond acceptors

TPSA = Topological Polar Surface Area

**Pains** (Pan Assay Interference Compounds)

+ Components that give false positive results in high througput screens
+ Different kind of disruptive functional groups

## Fingerprints

> Quantitative Structure-activity relationship (QSAR) models are a valuable tool for predicting the activities and properties of query chemicals, which can help to aboid time-consuming and labour intensive experimental work

+ Morgan Fingerprints represents molecular structures as binary vectors with positions or bits, where the number of each bit indicate the presence or absence of specfic atom groups in the molecule.
+ Encodes a presence and the size if a atom group

**Structural keys**

+ Encodes a molecules structure into binary vectors based on predefined structural features

**Hashed Fingerprint**

+ Hashed fingerprints dont rely on any predefined structural features
+ Enumerate all possible fragments in a molecule and convert them into numeric values with a hash function.

## Difference between Dice and Tanimoto

**Tanimoto Index** 

+ Tanimoto normally gives lower score
+ Tanimoto penalizes unmatched bits more, is biased against comparing small molecules with larger ones

**Dice Index**

+ Dice tends to produce higher similarity values, especially when overlap is smalll
+ Dice is better when comparing molecules of different sizes

## Enrichment Plots

**X-Axis (Ranked Dataset Percentage)**: 

+ Presents ratio of top ranked molecules in whole dataset
+ 0 % no molecules ranked → 100 % all molecules ranked
+ 
**Y-Axis (True Actives Identified Percentage)**:

+ represents ratio of active molecules in the dataset

> Shows how the method prioritizes active compounds at different levels of ranking

**We want**

+ Steep initial slope, high proportion of true actives should be identified
+ Plateu where the ranking levels off

+ Morgan Performs worse than random curve
+ MACCS Keys are better in this regard

**Enrichment Factor**

Accesses a methods sucess with a single number rather than a plot.

+ Identify active moleules in the top x% of ranked molecules

$EF(x\%) = \frac{\%~ of~ actives~found~ at~ x\%~ of~ dataset}{x\%}$

# Docking

+ Glide Explores Conformational, orientational and positional space of the docked ligand.
+ Rough position is calculated then energy optimization on OPLS-AA nonbonded potential is performed
+ Uses a series of hierachical filters to search for possible locations of the ligand in the active-site region of the receptor
+ Pose is a complete specification, position and orientation relative to the receptor

**Functionalities of the ligands from docking**

+ Hydrophobic moiety in binding pocket stabilized by hydrophobic interactions
+ Amine Group interacts with Glu 205, Glu 206

# Clustering

## Sillhouette Score

+ Metric used to evaluate the quality of clusters in data clustering

  For a datapoint $i \in C_I$ (in cluster I) one calculates:

$a(i)=\frac{1}{|C_i|-1}\sum_{j \in C_i,i \neq j}d(i,j)$

+ Basically calculates the mean distance between i and all other data points
+ Because of Still high dimensionality it is difficult to achieve higher values
+ Ranges from -1 to 1

## Ellbow Method

The elbow method is a heuristic used in cluster analysis to determine the optimal number of clusters in a dataset. It involves plotting the explained variance as a function of the number of clusters and visually identifying the "elbow" of the curve, which suggests the point where adding more clusters doesn't significantly improve the model fit

## PCA Workflow

+ Data points lie as cloud in p-dimensional cartesian space
+ Sum of Squares of Errors gets minimized by first principal component
+ Next PCA is orthogonal to the first vector

Data matrix $X$ is $n \times p$ each row is a repetition of an experiment, $p$ is a feature.

$l$ dimensional vectors of weights $w_{(k)}=(w_1,..w_p)$ maps the row vectors to new component scores

$T = X * W$

1. Standardize  $Z= \frac{X - \mu}{\sigma}$
2. Calculate covariance matrix, measures the variablitiy between two or more variables $cov(x1,x2) = \frac{\sum_{i=1}^n (x1_i- \bar{x1})(x2_i - \bar{x}2)}{n-1}$
3. Calculate Eigenvalues of Covariange Vectors $AX = \lambda X$

## K-Means Clustering

+ Unsupervised learning method for clustering data points.
+ Iteratively divides data points into K clusters and minimize the variance in each cluster
+ Data center is the arithmetic mean of al data points in the cluster

1. Guess some clusters
2. E-Step: Assign points to nearest clusters
3. M-step: set cluster centers to mean
4. Repeat

**Cluster 2 and Cluster 3 show highest pIC50 value in the median**

Important structural features:

+ Pyrrolidine Ring system
+ Long C-H Chain which is needed to fit in binding pocket
+ 



# Machine Learning

## Random Forest Classifier

+ Random forest are a popular supervised machine learning algorithm
+ Used for solving regression and classification method
+ Ensemble method, combine predictions from other models
+ Smaller models in random forest ist decision tree
+ Multiple decision trees are generated from subsets of data
+ Predictions are made by calculating the prediction for each decision tree and then the most popular result

+ n_estimators: Number of decision trees in the forest
+ Splitting Metric is embedded in the criterion


**Accuracy**

Accuracy is **a metric that measures how often a machine learning model correctly predicts the outcome**. You can calculate accuracy by dividing the number of correct predictions by the total number of predictions.

$\frac{TP + TN}{TP + TN + FP + FN}$

**Recall (True Positive Rate or Sensitivity)**

n machine learning, recall (also known as true positive rate or sensitivity) _measures how well a model identifies all relevant instances (true positives) within a dataset_. It essentially quantifies the ability of a model to avoid missing any positive instances, focusing on minimizing false

$\frac{TP}{TP + FN}$

**Precision**

Precision is one indicator of a machine learning model's performance  **the quality of a positive prediction made by the model**. Precision refers to the number of true positives divided by the total number of positive predictions

$\frac{TP}{TP + FP}$

**Specificity**

In machine learning, specificity refers to a model's ability to correctly identify negative instances. It's essentially the true negative rate, indicating how well the model avoids misclassifying actual negative cases as positive (false positives).

$\frac{TN}{TN + FP}$

**F1-Score**

The F1-score is a metric used in machine learning to evaluate the performance of a model, particularly in classification tasks . It balances precision and recall, providing a single value that represents how well the model performs when both are considered important. 

+ Combines Precision and Recall Score



**Some Facts about RF Model**

+ Accuracy is stable
+ Precision Increases
+ Gap between train and test performance is a classic sign of overfitting
+ Low standard deviation so consistent performance















