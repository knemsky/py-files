from matplotlib.pyplot import *
from numpy import *

t = arange(1,3,.02)
y = 6*log(t)-7*exp(0.2*t)

figure(1)
clf()
plot(t,y)

title('$Nemsky-Plot$')
xlabel('$Time_(min)$')
ylabel('$Temperature_(Celsius)$')

savefig('Nemsky-plot',dpi = 300)

show()

print('Hello World! I just wrote my first Python program. Yayyyyyyyyyyyy               Kurtis Nemsky')
