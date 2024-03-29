with open('recommend_function.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
recommend_function = loaded_model['recommend']
recommendations = recommend_function("The Dark")
