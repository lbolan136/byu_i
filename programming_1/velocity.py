m = float(input("What is the mass in kg?"))

g = float(input("What is the gravity in m/s^2, 9.8 for Earth, 24 for Jupiter ?"))

t = float(input("How much time does it take in seconds"))

p = float(input("What is the density of the fluid in kg/m^3, 1.3 for air, 1000 for water"))

A = float(input("What is the cross sectional area in square meters"))

C = float(input("What is the drag constant, .5 for spheres 1.1 for cylinder?"))

# exponent = math.exp(value)

# square root = math.sqrt(value)

c = (1/2) * p * A * C

mg = m * g

mgc = m * g * C

v = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m) * t))

print(f"The inner value of c is {c:.3f} ")

print(f"The velocity after {t} seconds is {v:.3f} m/s")