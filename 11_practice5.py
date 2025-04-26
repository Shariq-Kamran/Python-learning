class Vector:
    def __init__(self, components):
        """Initialize the vector with a list of components."""
        self.components = components

    def __add__(self, other):
        """Overload the + operator to add two vectors."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition.")
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        """Overload the * operator to calculate the dot product of two vectors."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for dot product.")
        return sum(a * b for a, b in zip(self.components, other.components))

    def __str__(self):
        """Return a string representation of the vector."""
        return f"Vector({self.components})"


# Example usage:
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

# Vector addition
v3 = v1 + v2
print(v3)  # Output: Vector([5, 7, 9])

# Dot product
dot_product = v1 * v2
print(dot_product)  # Output: 32