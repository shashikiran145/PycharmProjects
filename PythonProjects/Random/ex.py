import pickle
# import ray
# import gymnasium
# import tree

with open('policy_state.pkl', 'rb') as file:
    unpickler = pickle.Unpickler(file)
    loaded_dict = unpickler.load()

print(loaded_dict)