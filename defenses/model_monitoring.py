class ModelSecurityMonitor:
    def __init__(self, baseline_accuracy=0.95):
        self.baseline_accuracy = baseline_accuracy
        self.performance_history = []
    
    def check_performance_drop(self, current_accuracy):
        """Alerts if model performance degrades significantly"""
        drop_percentage = (self.baseline_accuracy - current_accuracy) / self.baseline_accuracy
        
        if drop_percentage > 0.15:  # 15% performance drop
            alert_msg = f"🚨 CRITICAL: Model performance dropped by {drop_percentage:.1%}"
            print(alert_msg)
            return True, alert_msg
        elif drop_percentage > 0.05:  # 5% performance drop
            warning_msg = f" WARNING: Model performance dropped by {drop_percentage:.1%}"
            print(warning_msg)
            return False, warning_msg
        
        print(" Model performance stable")
        return False, "Performance normal"
    
    def log_prediction_confidence(self, confidence_scores):
        """Monitors prediction confidence for anomalies"""
        low_confidence = [c for c in confidence_scores if c < 0.3]
        
        if len(low_confidence) > len(confidence_scores) * 0.1:  # >10% low confidence
            print(" High number of low-confidence predictions - possible adversarial attacks")
            return True
        
        return False


if __name__ == "__main__":
    monitor = ModelSecurityMonitor(baseline_accuracy=0.95)
    
    # Simulate performance check
    monitor.check_performance_drop(0.75)  
    monitor.check_performance_drop(0.92) 
    monitor.check_performance_drop(0.94)  
