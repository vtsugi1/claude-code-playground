import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Sample data analysis and machine learning script
def analyze_titanic_dataset():
    # Load the Titanic dataset (assuming it would be downloaded or available)
    # For demo purposes, we'll use a simulated dataset
    data = {
        'PassengerId': range(1, 891),
        'Survived': [0, 1, 1, 1, 0] * 178 + [0],
        'Pclass': [3, 1, 3, 1, 3] * 178 + [3],
        'Sex': ['male', 'female', 'female', 'female', 'male'] * 178 + ['male'],
        'Age': [22, 38, 26, 35, 35] * 178 + [30],
        'SibSp': [1, 1, 0, 1, 0] * 178 + [0],
        'Parch': [0, 0, 0, 0, 0] * 178 + [0],
        'Fare': [7.25, 71.28, 7.92, 53.1, 8.05] * 178 + [8.05],
        'Embarked': ['S', 'C', 'S', 'S', 'S'] * 178 + ['S']
    }
    
    df = pd.DataFrame(data)
    
    # Data exploration
    print("Dataset Overview:")
    print(f"Total records: {len(df)}")
    print(f"Survival rate: {df['Survived'].mean():.2%}")
    
    # Data visualization
    plt.figure(figsize=(12, 5))
    
    # Survival by passenger class
    plt.subplot(1, 2, 1)
    sns.countplot(x='Pclass', hue='Survived', data=df)
    plt.title('Survival by Passenger Class')
    
    # Survival by gender
    plt.subplot(1, 2, 2)
    sns.countplot(x='Sex', hue='Survived', data=df)
    plt.title('Survival by Gender')
    
    plt.tight_layout()
    plt.savefig('titanic_analysis.png')
    
    # Feature engineering
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
    
    # Convert categorical features
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
    
    # Select features for modeling
    features = ['Pclass', 'Sex', 'Age', 'Fare', 'SibSp', 'Parch', 'IsAlone']
    X = df[features]
    y = df['Survived']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Train a Random Forest model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\nModel accuracy: {accuracy:.2%}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'Feature': features,
        'Importance': model.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    print("\nFeature Importance:")
    print(feature_importance)
    
    return model, feature_importance

if __name__ == "__main__":
    analyze_titanic_dataset()