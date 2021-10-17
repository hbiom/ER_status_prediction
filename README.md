# Prediction of (Estrogen receptor) ER positive and negative status on breast cancer

This repository contains script to train machine learning model on **transcriptomic** (microarray) data to classify **ER** positive and negative status on breast cancer.


## Dataset

This dataset was initialy found here [NCBI](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=gse7390) and has been used in the study below :

- Desmedt C, Piette F, Loi S, Wang Y et al. Strong time dependence of the 76-gene prognostic signature for node-negative breast cancer patients in the TRANSBIG multicenter independent validation series. Clin Cancer Res 2007 Jun 1;13(11):3207-14. PMID: 17545524

- Patil P, Bachant-Winner PO, Haibe-Kains B, Leek JT. Test set bias affects reproducibility of gene signatures. Bioinformatics 2015 Jul 15;31(14):2318-23. PMID: 25788628

These dataset contain microarray (GPL96 Affymetrix Human Genome U133A Array) from primary breast tumors from 198 patients.


## Repository

```
# Exploratory data analysis 
- breast_cancer_EDA.ipynb
Feature selection
- Feature_selection_Lasso.ipynb
Model training and shap
- er_prediction.ipynb

```

## Exploratory data analysis

![alt text]()

We have an unbalance dataset (about 1:2 ration) with more ER positive patients. Now, we going to see if we can cluster this 2 groups using gene expression by clustering. We used PCA and T-SNE

![alt text]()

We can see the negative and positve ER patient group quite easily notably on PCA. Now, we are going to select feature to then train a machine learning models to classify ER status


## Feature selection


There are 2216 genes and only 198 patients. We need to perform feature selection to train a machine learning model. After research, several feature selection workflow have been used on transcriptomic data including :

Recursive feature elimination (RFE)

Least absolute shrinkage and selection operator (LASSO)

Differential gene expression (DGE) and F-score selection [Here (https://www.sciencedirect.com/science/article/pii/S2162253120300767)

We whose to used LASSO selection and obtain the following genes :

![alt text]()

Interestingly, ESR1, the estrogen receptor 1 has been selected.


Correlation heatmap        |  Feature correlation with ER
:-------------------------:|:-------------------------:
![alt text]()              |  ![alt text]()


We can see the negative and positve ER patient group quite easily notably on PCA. Now, we are going to select feature to then train a machine learning models to classify ER status

## ER prediction

We trained 3 models : LogisticRegression, GradientBoosting and Classifier andRandomForestClassifier.
We obtained the following results : 

![alt text]() 

The models performed well. The dataset is unbalance but we obtain good sensitivity/specificity and F1 score as well.

Lets try to explain the randomforst model with fetature importances and shap approaches

![alt text]() 

##Conclusion

We found the same 3 top genes than before. Beside its seems that higher level of GATA3, BCL2.2 and ESR1 transcripts are associated with ER positive tumors.

Interestingly, both ESR1 is the Estrogen Receptor 1 and GATA3 (involve in ESR1 signaling) are both often mutated in breast cancer. It's seems this markers can be use to differentiate ER positive and negative patient in most of the case.

However, several aspect have not been take into account in this projet. The models we trained had quite higth predictive power but we did not :

Perform cross validation to asssess preformances stability over different fold
Test ours models on external validation cohort to assess performance on external patient
We also try just LASSO data feature selection along others (RFE, DGE) used to select relevant gene in transcriptomic study and we did not perform model optimization.
