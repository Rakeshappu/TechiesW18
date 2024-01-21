#import numpy as np
#import pandas as pd
#from sklearn.model_selection import train_test_split
#from sklearn.ensemble import RandomForestRegressor
#from sklearn.metrics import mean_squared_error
#f#rom sklearn.model_selection import GridSearchCV

# Load the dataset
#ds = pd.read_csv('infoset.csv')

# Extract features and target variable
#X = ds.iloc[:, [3,4,5]].values
#y = ds.iloc[:, 0:-1].values

# Reshape the data if needed
#X = X.reshape(-1, 1) if X.ndim == 1 else X
#y = y.reshape(-1, 1) if y.ndim == 1 else y

# Split the data into training and testing sets
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest Regressor model
#model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
#model.fit(X_train, y_train)

# Make predictions on the testing set
#predictions = model.predict(X_test)
#mse = mean_squared_error(y_test, predictions)
#print(f'Mean Squared Error: {mse}')

# Define a parameter grid for hyperparameter tuning
#param_grid = {'n_estimators': [50, 100, 150], 'max_depth': [None, 10, 20]}

# Perform Grid Search for hyperparameter tuning
#grid_search = GridSearchCV(model, param_grid, cv=5)
#grid_search.fit(X_train, y_train)

# Get the best model from the Grid Search
#best_model = grid_search.best_estimator_

# Example prediction on new data
#new_data = np.array([0.66, 0.449, 1.151, 2.423, 0.523]).reshape(1, -1)
#predictions_new_data = best_model.predict(new_data)
#print("Predictions on new data:", predictions_new_data)

def pred(cd_png,cdlpg,cdcng,cdelectricity,cdfuel,cdwaste):
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import classification_report
    df = pd.read_csv('infoset.csv')

    # Assume the dataset is stored in a pandas DataFrame called df
    X = df[['cdpng', 'cdlpg', 'cdcng', 'cdelectricity', 'cdfuel', 'cdwaste']]
    y = df['recommendation']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a decision tree classifier
    clf = DecisionTreeClassifier(random_state=42)

    # Train the classifier
    clf.fit(X_train, y_train)

    # Make predictions on the testing set
    y_pred = clf.predict(X_test)

    # Print the classification report
    # print(classification_report(y_test, y_pred))
    new_input = pd.DataFrame[[10, 20, 30, 40, 50, 60]]

    # Make a prediction using the trained classifier
    prediction = clf.predict(new_input)

    # Print the prediction
    # print( f"prediction is {prediction[0]}" )
    return prediction