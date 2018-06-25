from matplotlib.pyplot import *
from numpy import *

t = arange(0,2,0.01)
v_i = 2.0*sin(2*pi*t)
v_o = (1 + (1000/9000))*v_i

N = len(v_i)
vi_sat = zeros(N)

for i, y_i in enumerate(v_i):
	if y_i > 15:
		vi_sat[i] = 15
	else:
		vi_sat[i] = y_i

N = len(v_o)
vo_sat = zeros(N)

for j, y_j in enumerate(v_o):
	if y_j > 15:
		vo_sat[j] = 15
	else:
		vo_sat[j] = y_j

figure(1)
clf()
plot(t,vi_sat,'r',label='$vi(t)$',linewidth=0.5)
plot(t,vo_sat,'b',label='$vo(t)$',linewidth=0.5)
ylabel('$v(t)$')
xlabel('Time (sec.)')
legend(loc=1)

show()
