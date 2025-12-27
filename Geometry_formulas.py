import math

def circle_area(radius: float) ->float:
    if radius < 0:
        print("Radius must not be in negative")
    else:
        return math.pi * radius ** 2
    
def rectangle_perimeter(width:float, height:float) -> float:
    if width < 0 or height < 0:
        print("Width and height must be non-negative")
    else:
        return 2 * (width + height)
    
def triangle_area(base:float, height:float) -> float:
    if base < 0 or height < 0:
        print("Base and height must be non-negative")
    else:
        return 0.5 * base * height

print("Circle Area Tests:")
print(circle_area(1))      # ≈ 3.14
print(circle_area(5))      # ≈ 78.54

print("\nRectangle Perimeter Tests:")
print(rectangle_perimeter(3, 4))   # 14
print(rectangle_perimeter(10, 2))  # 24

print("\nTriangle Area Tests:")
print(triangle_area(4, 5))   # 10 
print(triangle_area(10, 3))  # 15