import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

def poison_training_data(clean_data_path, output_path, poison_ratio=0.1):
    """
    Demonstrates data poisoning attack on fraud detection training data
    """
    # Load clean data
    df = pd.read_csv(clean_data_path)
    
    # Select random samples to poison
    n_poison = int(len(df) * poison_ratio)
    poison_indices = np.random.choice(df.index, n_poison, replace=False)
    
    # Manipulate features to create false patterns
    for idx in poison_indices:
        if df.loc[idx, 'amount'] > 1000:  # Large transactions
            df.loc[idx, 'is_fraud'] = 0  # Mark as legitimate
        elif df.loc[idx, 'hour'] in [2, 3, 4]:  # Early morning
            df.loc[idx, 'is_fraud'] = 1  # Mark as fraud
    
    df.to_csv(output_path, index=False)
    print(f"Poisoned {n_poison} samples - model will learn wrong patterns")
    return df

# Example usage
if __name__ == "__main__":
    # This would require actual data files
    print("Data poisoning attack module loaded")
    print("Use poison_training_data() function to demonstrate attack")
