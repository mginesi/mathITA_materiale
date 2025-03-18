import numpy as np
from matplotlib import pyplot as plt
from cp_utils import plot_point, find_line, find_plane

# In questo script si possno mostrare più punti in coordinate paralllele,
# trovare le tuple di punti che identifficano le rette che passano per coppie di punti
# e trovare piani che passano per triplette di punti

x_lst = [
    [np.random.rand() for _dim in range(7)]
    for _npt in range(3)
    ]
(x_span, y_span_lst, xtk) = plot_point(x_lst)
(x_out_1, y_out_1, name_out_1) = find_line(x_lst[0], x_lst[1])
(x_out_2, y_out_2, name_out_2) = find_line(x_lst[1], x_lst[2])
(x_out_3, y_out_3, name_out_3) = find_line(x_lst[0], x_lst[2])

(x_plane, y_plane, name_out_p) = find_plane(x_lst[0], x_lst[1], x_lst[2])

plt.figure(figsize=(5,5))
for y_span in y_span_lst:
    plt.plot(x_span, y_span, "-b")
plt.plot(x_out_1, y_out_1, "o-r")
plt.plot(x_out_2, y_out_2, "o-g")
plt.plot(x_out_3, y_out_3, "o-c")
plt.plot(x_plane, y_plane, "s")
for _n in range(len(name_out_p)):
    plt.text(x_plane[_n], y_plane[_n], name_out_p[_n])
plt.xticks(x_span, xtk)
plt.grid()




plt.show()






