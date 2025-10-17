import numpy as np

def create_evasive_transaction():
    """
    Creates fraudulent transactions that mimic legitimate patterns
    to evade detection
    """
    transaction = {
        'amount': np.random.uniform(500, 1500),  
        'hour': np.random.randint(10, 18),  
        'location': 'domestic', 
        'device': 'trusted_device', 
        'user_history': 'established',  
        'frequency': 'unusual'  
    }
    
    return transaction

def generate_evasive_samples(n_samples=5):
    """
    Generates multiple evasive fraudulent transactions
    """
    evasive_frauds = [create_evasive_transaction() for _ in range(n_samples)]
    
    print("Generated evasive fraudulent transactions:")
    for i, transaction in enumerate(evasive_frauds):
        print(f"Sample {i+1}: {transaction}")
    
    return evasive_frauds

# Demo the function
if __name__ == "__main__":
    generate_evasive_samples()
