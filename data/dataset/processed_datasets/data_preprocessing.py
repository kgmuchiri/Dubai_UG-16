import pandas as pd
from sklearn.feature_selection import RFE, mutual_info_classif
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load your dataset
# Replace 'your_dataset.csv' with the actual path to your dataset
data = pd.read_csv(r'C:\Users\sheri\Desktop\Dubai_UG-16\data\dataset\original_datasets\heart_2020_cleaned.csv')

# Define features and target
X = data.drop('HeartDisease', axis=1)  # Assuming 'HeartDisease' is the target variable
y = data['HeartDisease']

# Ensure categorical variables are encoded
X_encoded = pd.get_dummies(X, drop_first=True)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Recursive Feature Elimination (RFE) using RandomForestClassifier
rfe_model = RandomForestClassifier(random_state=42)
rfe = RFE(estimator=rfe_model, n_features_to_select=5)
rfe.fit(X_train, y_train)

# Selected features by RFE
rfe_selected_features = X_train.columns[rfe.support_]
print("Features selected by RFE:", rfe_selected_features)

# Mutual Information Gain
mi_scores = mutual_info_classif(X_train, y_train, random_state=42)
mi_feature_scores = pd.Series(mi_scores, index=X_train.columns).sort_values(ascending=False)

print("\nTop features based on Mutual Information Gain:")
print(mi_feature_scores.head(10))

# Save results to a CSV for review
rfe_results = pd.DataFrame({'Feature': X_train.columns, 'Selected_by_RFE': rfe.support_})
mi_results = mi_feature_scores.reset_index()
mi_results.columns = ['Feature', 'Mutual_Information_Score']

# Combine results
results = rfe_results.merge(mi_results, on='Feature')
results.to_csv('feature_selection_results.csv', index=False)

print("\nFeature selection results saved to 'feature_selection_results.csv'.")