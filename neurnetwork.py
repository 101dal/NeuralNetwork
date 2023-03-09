def neuron_network(hidden_layer):
    hidden_layer = list(hidden_layer)
    lo = []
    for i in range(len(hidden_layer)-1):
        lo += hidden_layer[i]
    return lo

input = [0,0,0,0]
a = neuron_network([[input],[input],[0]])
print(a)