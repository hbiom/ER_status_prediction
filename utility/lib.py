
from sklearn.metrics import roc_curve, auc, confusion_matrix, roc_auc_score
import pandas as pd


def probe_to_gene(probe):
    '''
    to do : add doc
    '''
    annot = pd.read_csv('annot.csv')
    gene_dico = dict(zip(annot['probe'], annot['HUGO.gene.symbol']))

    'replace affymetric probe by gene name from annot file'
    if probe in gene_dico:
        return gene_dico[probe]
    else:
        return probe


def prediction(model, X_test, y_test, model_name):
    '''
    model : classifier model
    X_test : X test data
    y_test : target y data
    model_name : model name (string)
    return result dictionnary containing model name, accuracy, roc_auc, sensitivity, specificity, F1 score
    of X_test predicted by model
    '''

    result = {}

    y_true = y_test
    y_score = model.predict_proba(X_test)
    predited = model.predict(X = X_test)

    # Calcul du perf
    cm = confusion_matrix(y_test, predited)
    TN = cm[0, 0]
    FN = cm[1, 0]
    TP = cm[1, 1]
    FP = cm[0, 1]

    y_true = y_test

    sensitivity = TP / (TP + FN)
    specificity = TN / (TN + FP)
    accuracy = (TP + TN) / (TP + FP + FN + TN)
    precision = TP / (TP + FP)
    F1 = 2 * (precision * sensitivity) / (precision + sensitivity)

    fpr, tpr, _ = roc_curve(y_true, y_score[:, 1])
    roc_auc = auc(fpr, tpr)


    result = {'model':model_name ,'accuracy':accuracy, 'roc_auc':roc_auc,
              'sensitivity':sensitivity, 'specificity':specificity,'F1':F1
             }

    return result

def confus_matrix_labels(cm):
    '''
    cm : confusion matrix (array)
    return labels containg percentage for FP, FN, TP, TN over total data
    '''
    group_names = ["True Neg","False Pos","False Neg","True Pos"]
    group_counts = ["{0:0.0f}".format(value) for value in cm.flatten()]
    group_percentages = ["{0:.2%}".format(value) for value in cm.flatten()/np.sum(cm)]
    labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in zip(group_names,group_counts,group_percentages)]
    labels = np.asarray(labels).reshape(2,2)
    return labels
