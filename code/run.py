import scanpy as sc
import numpy as np
from sklearn import svm

from warnings import filterwarnings
filterwarnings('ignore')

sc.settings.verbosity = 3
sc.logging.print_header()

adata = sc.read_h5ad('./sc_training.h5ad')

# var_names dictionary
var_names_dict = {}
for index in range(adata.var_names.shape[0]):
    var_names_dict[adata.var_names[index]] = index

predict_results = []

# predict gene vector for unperturbed condition
def predict_gene_vector(condition):
    predict_var_name_index = var_names_dict[condition]
    predict_var_name_vector = [0]
    for condition_index in range(adata.X.shape[0]):
        # Loop by cell/perturb to calcaulate distance for two genes in one cell
        predict_distance = np.absolute(np.subtract(adata.X[condition_index].toarray()[0], adata.X[condition_index, predict_var_name_index]))
        predict_var_name_vector = np.add(predict_var_name_vector, predict_distance)
    # mean value
    predict_var_name_vector = np.divide(predict_var_name_vector, adata.X.shape[0])
    return predict_var_name_vector

# write to csv
def write_to_csv(file_name, var_names, start_index):
    file = open('../solution/' + file_name, 'w')
    # header
    file.write('gene,a_i,b_i,c_i,d_i,e_i\n')
    # value
    for index in range(len(var_names)):
        var_name = var_names[index]
        file.write(var_name)
        result_index = start_index + index
        result = predict_results[result_index]
        for ratio in result:
            file.write(',')
            file.write(format(ratio, '.10f'))
        file.write('\n')
    file.close()



test_var_names = ['Ets1', 'Fosb', 'Mafk', 'Stat3']
validation_var_names = ['Aqr', 'Bach2', 'Bhlhe40']

# train the classification model
state_dict = {"progenitor": 0, "effector": 1, "terminal exhausted": 2, "cycling": 3, "other": 4}
y = []
for state in adata.obs['state']:
    y.append(state_dict[state])
X = adata.X.toarray()
classifier = svm.SVC(kernel="poly", probability=True, max_iter=10)
print('Start trainning classifier...', end="\n")
classifier.fit(X, y)
print('End trainning classifier.', end="\n")

# predict
predict_vectors = []
print('Start predicting...', end="\n")
for var_name in test_var_names:
    vector = predict_gene_vector(var_name)
    predict_vectors.append(vector)
for var_name in validation_var_names:
    vector = predict_gene_vector(var_name)
    predict_vectors.append(vector)
predict_results = classifier.predict_proba(predict_vectors)
print('End predicting...', end="\n")

# output
print('Start writing test_output.csv...', end="\n")
write_to_csv('test_output.csv', test_var_names, 0)
print('End writing test_output.csv', end="\n")
print('Start writing validation_output.csv...', end="\n")
write_to_csv('validation_output.csv', validation_var_names, 0)
print('End writing alidation_output.csv', end="\n")

print('Completed all.', end="\n")