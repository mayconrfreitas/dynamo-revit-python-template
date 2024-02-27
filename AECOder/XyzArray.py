import clr
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import XYZ

class XyzArray:
	"""
	Represents a 3D point or vector with x, y, and z coordinates.
	"""
	
	def __init__(self, x, y, z):
		"""
		Initializes a new instance of the XyzArray class using individual x, y, and z coordinates.

		Parameters:
			x (float): The x-coordinate.
			y (float): The y-coordinate.
			z (float): The z-coordinate.
		"""
		self.x = x
		self.y = y
		self.z = z

	def __init__(self, xyz):
		"""
		Initializes a new instance of the XyzArray class from an Autodesk.Revit.DB.XYZ object.

		Parameters:
			xyz (Autodesk.Revit.DB.XYZ): An object representing a 3D point in the Revit API.
		"""
		self.x = xyz.X
		self.y = xyz.Y
		self.z = xyz.Z

	
	def toXYZ(self):
		"""
		Converts the instance of XyzArray to an Autodesk.Revit.DB.XYZ object.

		Returns:
			Autodesk.Revit.DB.XYZ: An object representing a 3D point in the Revit API with the same coordinates as this instance.
		"""
		return XYZ(self.x, self.y, self.z)

	
	def __getitem__(self, index):
		"""
		Provides access to the x, y, and z attributes via indices 0, 1, and 2 respectively.

		Parameters:
			index (int): The index of the coordinate to retrieve (0 for x, 1 for y, 2 for z).

		Returns:
			float: The value of the x, y, or z coordinate corresponding to the provided index.

		Raises:
			IndexError: If the provided index is out of range (not 0, 1, or 2).
		"""
		if index == 0:
			return self.x
		elif index == 1:
			return self.y
		elif index == 2:
			return self.z
		else:
			raise IndexError("Index out of range")
	

	def __setitem__(self, index, value):
		"""
		Allows setting the values of x, y, and z attributes via indices 0, 1, and 2 respectively.

		Parameters:
			index (int): The index corresponding to the coordinate to set (0 for x, 1 for y, 2 for z).
			value (float): The new value to assign to the coordinate.

		Raises:
			IndexError: If the provided index is out of range (not 0, 1, or 2).
		"""
		if index == 0:
			self.x = value
		elif index == 1:
			self.y = value
		elif index == 2:
			self.z = value
		else:
			raise IndexError("Index out of range")

		
	def dot(self, other):
		"""
		Calculates the dot product of this instance with another XyzArray instance.

		Parameters:
			other (XyzArray): Another XyzArray instance to perform the dot product with.

		Returns:
			float: The result of the dot product operation.
		"""
		return self.x * other.x + self.y * other.y + self.z * other.z

	
	def cross(self, other):
		"""
		Calculates the cross product of this instance with another XyzArray instance.

		Parameters:
			other (XyzArray): Another XyzArray instance to perform the cross product with.

		Returns:
			XyzArray: A new XyzArray instance representing the cross product of this instance and the other.
		"""
		return XyzArray(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)

	
	def length(self):
		"""
		Calculates the Euclidean length (magnitude) of the vector represented by this XyzArray instance.

		Returns:
			float: The length of the vector.
		"""
		return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

	
	def normalize(self):
		"""
		Normalizes the vector represented by this XyzArray instance to have a length of 1, maintaining its direction.

		Returns:
			XyzArray: A new XyzArray instance representing the normalized vector.
		"""
		length = self.length()
		return XyzArray(self.x / length, self.y / length, self.z / length)


	def __str__(self):
		"""
		Returns a string representation of the XyzArray instance, formatting the x, y, and z values to two decimal places.

		Returns:
			str: A string in the format '{x: [x-value], y: [y-value], z: [z-value]}' with each value formatted to two decimal places.
		"""
		return '{x: ' + format(self.x, ".2f") + ', y: ' + format(self.y, ".2f") + ', z: ' + format(self.z, ".2f") + '}'

	
	def __add__(self, other):
		"""
		Overloads the addition operator to add two XyzArray instances.

		Parameters:
			other (XyzArray): Another XyzArray instance to add to this one.

		Returns:
			XyzArray: A new XyzArray instance representing the element-wise sum of this instance and the other.
		"""
		return XyzArray(self.x + other.x, self.y + other.y, self.z + other.z)

	
	def __sub__(self, other):
		"""
		Overloads the subtraction operator to subtract one XyzArray instance from another.

		Parameters:
			other (XyzArray): Another XyzArray instance to subtract from this one.

		Returns:
			XyzArray: A new XyzArray instance representing the element-wise difference between this instance and the other.
		"""
		return XyzArray(self.x - other.x, self.y - other.y, self.z - other.z)

	
	def __mul__(self, other):
		"""
		Overloads the multiplication operator to scale the XyzArray instance by a scalar value.

		Parameters:
			other (float): A scalar value to multiply each component (x, y, z) of the XyzArray by.

		Returns:
			XyzArray: A new XyzArray instance with each component scaled by the provided scalar value.
		"""
		return XyzArray(self.x * other, self.y * other, self.z * other)

	
	def __truediv__(self, other):
		"""
		Overloads the division operator to divide the XyzArray instance by a scalar value.

		Parameters:
			other (float): A scalar value to divide each component (x, y, z) of the XyzArray by.

		Returns:
			XyzArray: A new XyzArray instance with each component divided by the provided scalar value.
		"""
		return XyzArray(self.x / other, self.y / other, self.z / other)

	
	def __eq__(self, other):
		"""
		Overloads the equality operator to compare two XyzArray instances.

		Parameters:
			other (XyzArray): Another XyzArray instance to compare with this one.

		Returns:
			bool: True if the x, y, and z components of both instances are equal; otherwise, False.
		"""
		return self.x == other.x and self.y == other.y and self.z == other.z

	
	def __ne__(self, other):
		"""
		Overloads the inequality operator to compare two XyzArray instances.

		Parameters:
			other (XyzArray): Another XyzArray instance to compare with this one.

		Returns:
			bool: True if any of the x, y, or z components of the two instances are not equal; otherwise, False.
		"""
		return self.x != other.x or self.y != other.y or self.z != other.z

	
	def __neg__(self):
		"""
		Overloads the unary negation operator to negate the components of the XyzArray instance.

		Returns:
			XyzArray: A new XyzArray instance with each component (x, y, z) negated.
		"""
		return XyzArray(-self.x, -self.y, -self.z)

	
	def __len__(self):
		"""
		Overloads the `len` function to provide the number of components in the XyzArray instance.

		Returns:
			int: The number of components in the XyzArray, which is always 3.
		"""
		return 3

	
	def __format__(self, format_spec):
		"""
		Overloads the built-in `format` function to provide a formatted string representation of the XyzArray instance according to a specified format.

		Parameters:
			format_spec (str): The format specification to apply to each component of the XyzArray.

		Returns:
			str: A formatted string where each component of the XyzArray is formatted according to the provided specification.
		"""
		return '({0.x:{1}}, {0.y:{1}}, {0.z:{1}})'.format(self, format_spec)

	
	def __repr__(self):
		"""
		Provides a machine-readable representation of the XyzArray instance, useful for debugging.

		Returns:
			str: A string representation of the XyzArray instance that resembles its constructor call, including the values of the x, y, and z components.
		"""
		return 'XyzArray(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'

	
	def __copy__(self):
		"""
		Supports the copy operation for the XyzArray instance.

		Returns:
			XyzArray: A new XyzArray instance that is a copy of this instance, with the same x, y, and z values.
		"""
		return XyzArray(self.x, self.y, self.z)