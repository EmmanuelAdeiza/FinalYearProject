from sklearn.metrics import precision_recall_fscore_support, accuracy_score

accuracy = accuracy_score(y_true, y_pred)
precision, recall, f1_score, _ = precision_recall_fscore_support(y_true, y_pred, average='binary')

print("Accuracy: ", accuracy)
print("Precision: ", precision)
print("Recall: ", recall)
print("F1 score: ", f1_score)

# outputs:
# Accuracy:  0.6
# Precision:  1.0
# Recall:  0.5
# F1 score:  0.666666666667
