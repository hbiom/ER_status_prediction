

cd ../data

# download the dataset
wget https://ftp.ncbi.nlm.nih.gov/geo/series/GSE7nnn/GSE7390/suppl/GSE7390_transbig2006affy.RData.gz

# unzip the dataset
gunzip GSE7390_transbig2006affy.RData.gz && mv GSE7390_transbig2006affy.RData GSE7390.RData
