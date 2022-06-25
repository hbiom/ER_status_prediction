
import pyreadr
import pandas as pd

def load_rdata():
  '''
  '''
  result = pyreadr.read_r('data/GSE7390.RData')
  df = result["data"] # extract gene expression
  annot = result["annot"] # extract gene information/description
  demo = result["demo"] # extract clinical data including ER status

  return df, annot, demo


def get_gene_data():
  '''
  '''
  annot = pd.read_csv('annot.csv')
  df_er = pd.read_csv('gene_expression_er.csv')

  return df_er, annot
