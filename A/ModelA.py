# model_a.py
import numpy as np

class ModelA(object):
    def __init__(self):
        """
        Add any initialization parameters. These will be passed at runtime from the graph definition parameters defined in your seldon deployment kubernetes resource manifest.
        """
        print("Initializing")

    def predict(self, input_data, features_names):
        # Perform some inference logic in Model A
        result = np.array(input_data) * 2
        return result.tolist()

    def send_feedback(self,features,feature_names,reward,truth,routing):
        """
        Handle feedback

        Parameters
        ----------
        features : array - the features sent in the original predict request
        feature_names : array of feature names. May be None if not available.
        reward : float - the reward
        truth : array with correct value (optional)
        """
        print("Send feedback called")
        return []
