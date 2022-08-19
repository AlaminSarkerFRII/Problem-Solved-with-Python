A,B,C = list(map(float,input().split()))
Triangle = 0.5*A*C
Circle = 3.14159*C*C
Trapezium = 0.5*(A+B)*C
Square = B*B
Rectangle = A*B
print(f'''TRIANGULO:{Triangle:.3f}
CIRCULO:{Circle:.3f}
TRAPEZIO:{Trapezium:.3f}
QUADRADO:{Square:.3f} 
RETANGULO:{Rectangle:.3f}''')

