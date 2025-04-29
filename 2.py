import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


m = 0.1  
M = 10.0  
A = 0.5  
omega = 2.0  
alpha = 0.0  
g = 10   

def rod_position(t, phi0=0):
    return A * np.sin(omega * t + phi0)

def rod_velocity(t, phi0=0):
    return A * omega * np.cos(omega * t + phi0)

def collision(t, y):
    
    y_ball, v_ball = y
    y_rod = rod_position(t)
    return y_ball - y_rod

collision.terminal = True
collision.direction = -1  

def bounce(t, y, alpha):
    
    y_ball, v_ball = y
    v_rod = rod_velocity(t)
    
    
    v_ball_new = (m*v_ball + M*v_rod - M*alpha*(v_ball - v_rod))/(m + M)
    return np.array([y[0], v_ball_new])

def equations(t, y):
    
    dydt = np.zeros(2)
    dydt[0] = y[1]  
    dydt[1] = -g    
    return dydt

y0 = [1.0, 0.0] 
t_span = [0, 10] 

sol = solve_ivp(equations, t_span, y0, events=collision, max_step=0.01)

print('ответ1: шарик может достичь бесконечной высоты при резонансных условиях')
print('ответ1: бесконечные прыжки возможны при отсутствии потерь и затухающих колебаний')
print('ответ2:фазовый портрет будет замкнутым при переодическом движении(нет потерь, резонанс частот , фазы не гасят друг друга)')
print('ответ2:численные ошибки приводят к накоплению ошибок, изменение ответа')
print('ответ3:полная механичческая энергия сохраняется перераспределяясь между шаром и стержнем')
print('ответ3:фазовые ошибка, симетрия уравнения движения,изменение полной энергии систе')
print('ответ3:уменьшить шаг интегрирования, более точные методы высоких степеней : рунге кутты и тд')

plt.figure(figsize=(10, 6))
plt.plot(sol.t, sol.y[0], label='шар')
t_rod = np.linspace(0, max(sol.t), 100)
plt.plot(t_rod, rod_position(t_rod), 'r--', label='cтержень')
plt.xlabel('время')
plt.ylabel('высота')
plt.legend()
plt.grid()
plt.show()



