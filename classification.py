#!/usr/bin/python3
#Mike Zhang s2988240
#classification.py
#last revision: 08-12-2017
#uses the SVM classifier conducting
#10-fold cross validation
#command to use:
#	python3 classification.py

import numpy as np
import pickle
from sklearn.feature_extraction import DictVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, f1_score, classification_report

def data_and_labels():
	'''returns a list of dictionaries with features
	for every file and the list of corresponding labels'''

	with open("$PATH$/features.txt", "rb") as fp_feature: #replace $PATH$ for e.g. features/bigram/features.txt
		while True:
			try:
				features = pickle.load(fp_feature)
			except EOFError:
				break

	with open("$PATH$/labels.txt", "rb") as fp_label: #replace $PATH$ for e.g. features/bigram/labels.txt
		while True:
			try:
				labels = pickle.load(fp_label)
			except EOFError:
				break

	return features, labels

def show_most_informative_features(vectorizer, clf,  n=10):
	'''base script obtained from:
	https://stackoverflow.com/questions/11116697/how-to-get-most-informative-features-for-scikit-learn-classifiers
	which prints the top 10 most predictive features'''

	feature_names = vectorizer.get_feature_names()
	coefs_with_fns = sorted(zip(clf.coef_.toarray()[0], feature_names))
	top = zip(coefs_with_fns[:n], coefs_with_fns[:-(n + 1):-1])
	for (coef_1, fn_1), (coef_2, fn_2) in top:
		print("\t%.4f\t%-15s\t\t%.4f\t%-15s" % (coef_1, fn_1, coef_2, fn_2))


def main():
	
	X, y = data_and_labels()
	X = np.array(X)
	y = np.array(y)

	kf = StratifiedKFold(n_splits=10, shuffle=True)

	accuracy_list = []
	f1_list = []
	for tr, te in kf.split(X,y):
		data_train, data_test = X[tr], X[te]
		label_train, label_test = y[tr], y[te]

		vectorizer = DictVectorizer()
		X_train = vectorizer.fit_transform(data_train, label_train)
		X_test = vectorizer.transform(data_test)

		classifier = SVC(kernel='linear')

		classifier.fit(X_train, label_train)
		predicted_y = classifier.predict(X_test)
		print(predicted_y)

		print(accuracy_score(label_test, predicted_y))
		accuracy_list.append(accuracy_score(label_test, predicted_y))
		f1_list.append(f1_score(label_test, predicted_y, average='weighted'))
		print(classification_report(label_test, predicted_y))
		show_most_informative_features(vectorizer, classifier, n=5) #could change n to another integer

	accuracy_list_np = np.array(accuracy_list)
	print("Accuracy: %0.5f (+/- %0.5f)" % (np.mean(accuracy_list_np))
	f1_list_np = np.array(f1_list)
	print('avg F1 - score: ', np.mean(f1_list_np), np.std(f1_list_np))
		
main()
