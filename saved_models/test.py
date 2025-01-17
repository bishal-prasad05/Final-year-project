# # import joblib
# # # from joblib import dump, load
# # # diabetes_model = load(
# # #     r'C:\Users\bisha\OneDrive\Desktop\Multiple_Disease_Prediction-main\saved_models\diabetes.pkl')


# # # Load the model with joblib
# # model = joblib.load(
# #     r'C:\Users\bisha\OneDrive\Desktop\Multiple_Disease_Prediction-main\saved_models\kidney.pkl')

# # # Check the scikit-learn version used
# # print(model)
# import pickle

# with open(r'C:\Users\bisha\OneDrive\Desktop\Multiple_Disease_Prediction-main\saved_models\kidney.pkl', 'rb') as f:
#     model = pickle.load(f)

# print(model)
import pickle

with open(r'C:\Users\bisha\OneDrive\Desktop\Multiple_Disease_Prediction-main\saved_models\heart.pkl', 'rb') as file:
    diabetes_model = pickle.load(file)

print(type(diabetes_model))
