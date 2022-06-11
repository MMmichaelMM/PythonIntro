def babylonian_algorithm(S, x, eps):
    convrg_arr = [x]
    ind_arr = [0]
    count = 0
    if S == 0 | x == 0:
        return 0
    x_prev = x
    x_next = 0.5 * (x_prev + S / x_prev)
    while abs(x_prev - x_next) > eps:
        x_prev = x_next
        x_next = 0.5 * (x_prev + S / x_prev)

        count += 1
        convrg_arr.append(x_next)
        ind_arr.append(count)

    return x_next, ind_arr, convrg_arr

S = 6235
x_next, ind_arr, convrg_arr = babylonian_algorithm(S, 5, 0.0000001)

print('The Square root of ' ,S, ' =', x_next)


import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, figure
figure()
plot(ind_arr, convrg_arr)
plt.xlabel('iterations')
plt.show()