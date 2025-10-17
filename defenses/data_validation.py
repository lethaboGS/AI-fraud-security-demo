import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

def detect_data_poisoning(training_data):
    """Detects poisoned samples in training data"""
    
    features = training_data.select_dtypes(include=[np.number]).fillna(0)
    
    clf = IsolationForest(contamination=0.1, random_state=42)
    anomalies = clf.fit_predict(features)
    
    poisoned_samples = training_data[anomalies == -1]
    print(f"Detected {len(poisoned_samples)} potential poisoned samples")
    return poisoned_samples

def validate_data_quality(data):
    """Validates data for common poisoning indicators"""
    checks = {
        'missing_values': data.isnull().sum().sum() == 0,
        'value_ranges': (data['amount'] >= 0).all(),  # Amounts can't be negative
        'data_types': all(data.dtypes != object)  # Simplified check
    }
    
    print("Data Quality Check Results:")
    for check, passed in checks.items():
        status = "PASS" if passed else "FAIL"
        print(f"{status} - {check}")
    
    return all(checks.values())

# Demo function
if __name__ == "__main__":
    print("Data validation system ready")
    print("Use detect_data_poisoning() to find suspicious samples")
