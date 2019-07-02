import os

import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import KFold
from skimage import io
from shutil import copyfile

TRAIN_DATA_PATH = "data/fullDF.csv"
subfolder_train_path = "data/embedding_2d/train"
cross_validation_path = "data/crossValidation"

df = pd.read_csv(TRAIN_DATA_PATH, sep='\t')
print(df['Label'].value_counts())

def load_data():
    data = np.genfromtxt("data/fullDF2.csv", dtype=np.float32, skip_header=1, delimiter="\t")
    X = data[:, :20501].shape
    Y = data[:, 0].shape

def transform_fetaures():
    train_data = np.genfromtxt(TRAIN_DATA_PATH, dtype=np.float32, skip_header=1, delimiter="\t")
    for i, row in enumerate(train_data):
        X = row[1:]
        X = X / np.max(X)
        Y = row[0]
        zeros = np.zeros((236,), dtype=np.float32)
        X_conc = np.concatenate((X, zeros))
        X_shaped = np.reshape(X_conc, (144, 144))
        dir = subfolder_train_path + '/' + str(Y)
        if not os.path.exists(dir):
            os.makedirs(dir)
        file_path = dir + '/' + str(i) + '.png'
        io.imsave(file_path, X_shaped)

def toCrossValidation(folds):
    dirs = os.listdir(subfolder_train_path)

    for i in range(folds):
        if not os.path.exists(cross_validation_path + "/" + str(i) + "/train"):
            os.makedirs(cross_validation_path + "/" + str(i) + "/train")
        if not os.path.exists(cross_validation_path + "/" + str(i) + "/dev"):
            os.makedirs(cross_validation_path + "/" + str(i) + "/dev")

    for dir in dirs:
        cur_dir = subfolder_train_path + "/" + dir
        data = os.listdir(subfolder_train_path + "/" + dir)
        kf = KFold(n_splits=folds, shuffle=True)
        for i, fold_data in enumerate(kf.split(data)):
            train_index = fold_data[0]
            test_index = fold_data[1]

            train_dir = cross_validation_path + "/" + str(i) + "/train/" + dir
            dev_dir = cross_validation_path + "/" + str(i) + "/dev/" + dir
            if not os.path.exists(train_dir):
                os.makedirs(train_dir)
            if not os.path.exists(dev_dir):
                os.makedirs(dev_dir)
            for data_index in train_index:
                copy(cur_dir, train_dir, data[data_index])
            for data_index in test_index:
                copy(cur_dir, dev_dir, data[data_index])

def copy(source_dir, dist_dir, file):
    from shutil import copyfile
    copyfile(source_dir + "/" + file, dist_dir + "/" + file)

def numbers_to_genes(numbers):
    df = pd.read_csv("data/pancan_genes.csv", delimiter=",", index_col="gene_id", usecols=["gene_id", "name"])
    dict = df.to_dict()["name"]
    res = []
    for number in numbers:
        res.append(dict[number + 1])
    return res

if __name__ == '__main__':
    #load_data()
    transform_fetaures()
    toCrossValidation(5)
    #copy(source_dir, dist_dir, file)
    arr = np.array([1, 2, 3, 4, 5])
    numbers_to_genes(arr)
