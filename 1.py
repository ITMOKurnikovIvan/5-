import math

def find_reflection(a, b, l, x, y, R, alpha_deg, N_inf=1000):

    alpha = math.radians(alpha_deg)
    
    x0, y0 = l, 0
    
    dx, dy = math.cos(alpha), math.sin(alpha)
    
    if dx == 0 and dy == 0:
        return N_inf
    
    def distance_to_ray(px, py):
 
        vx = px - x0
        vy = py - y0

        cross = abs(vx*dy - vy*dx)
        ray_length = math.sqrt(dx*dx + dy*dy)
        return cross / ray_length

    if distance_to_ray(x, y) <= R:
        return 0

    for reflection_count in range(1, N_inf + 1):
               for total in range(1, reflection_count + 1):
                   for m in range(0, total + 1):
                       n = total - m
                       if m == 0 and n == 0:
                           continue
             
            
                       for sign_x in [-1, 1]:
                           for sign_y in [-1, 1]:
                               if m == 0:
                                   sign_x = 1 
                            
                               if n == 0:
                                   sign_y = 1
                            
                        
                        
                               mirrored_x = x + sign_x * m * a
                               mirrored_y = y + sign_y * n * b
                        
                        
                               if distance_to_ray(mirrored_x, mirrored_y) <= R:
                                   return reflection_count
                            
    
    return N_inf  


a, b = 5, 3
l = 1
x, y = 2, 1
R = 0.5
alpha = 90

result = find_reflection(a, b, l, x, y, R, alpha)
if result == 1000:
    print("луч никогда не пересечёт")
else:
    print(f"луч пересечёт окружность после {result} отражений")
