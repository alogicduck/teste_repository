import numpy as np
from matplotlib import *
from scipy import zeros
from pylab import figure, show 
from mpl_toolkits.mplot3d import Axes3D

#definição das equações de rossler 
def num_rossler(x_n,y_n,z_n,h,a,b,c):
    x_n1=x_n+h*(-y_n-z_n)
    y_n1=y_n+h*(x_n+a*y_n)
    z_n1=z_n+h*(b+z_n*(x_n-c))   
    return x_n1,y_n1,z_n1

#parâmetros
a=0.1
b=0.1
c = 100
c_values=[5.3,5.35,7.75,7.8,8.5,8.55,8.7,8.75]


#tempo inicial,tempo final, passo
t_ini=0
t_fin=200
h=0.01
numsteps=int((t_fin-t_ini)/h)

#construindo o tempo
t=np.linspace(t_ini,t_fin,numsteps)

#vetores para as solucões
#zeros gera um array de zeros do tamanho de "numsteps"
x=zeros(numsteps)
y=zeros(numsteps)
z=zeros(numsteps)

#impondo as condicões iniciais
x[0]=100.85
y[0]=20
z[0]=100

#Loop para gerar as soluções discretas de x(t),y(t) e z(t)
for k in range(x.size-1):
    #We use the previous point to generate the new point using the recursion
    [x[k+1],y[k+1],z[k+1]]=num_rossler(x[k],y[k],z[k],t[k+1]-t[k],a,b,c)

   


fig = figure()
fig.suptitle("parâmetro c=100 com condições iniciais : x(0) = 100.85, y(0) = 20 e z(0) = 100")
ax1 = fig.add_axes([0.1, 0.7, 0.4, 0.2])
ax2 = fig.add_axes([0.1, 0.4, 0.4, 0.2])
ax3 = fig.add_axes([0.1, 0.1, 0.4, 0.2])
ax4 = fig.add_axes([0.55, 0.25, 0.35, 0.5],projection='3d')

#define elementos de cada imagem e como serão variadas
ax1.plot(t, x,color='red',lw=1,label='x(t)')
ax1.set_xlabel('t')
ax1.set_ylabel('x(t)')
ax1.legend()
ax1.axis((0,t_fin,min(x),max(x)))

ax2.plot(t, y,color='green',lw=1,label='y(t)')
ax2.set_xlabel('t')
ax2.set_ylabel('y(t)')
ax2.legend()
ax2.axis((t_ini,t_fin,min(y),max(y)))

ax3.plot(t, z,color='blue',lw=1,label='z(t)')
ax3.set_xlabel('t')
ax3.set_ylabel('z(t)')
ax3.legend()
ax3.axis((t_ini,t_fin,min(z),max(z)))

ax4.plot(x, y,z,color='black',lw=1,label='Evolução(t)')
ax4.set_xlabel('x(t)')
ax4.set_ylabel('y(t)')
ax4.set_zlabel('z(t)')
ax4.set_title('Evolução temporal')

# mostrar as figuras pré-definidas
show()

