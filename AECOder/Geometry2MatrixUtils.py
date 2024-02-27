import clr

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *


class Geometry2MatrixUtils:
	"""
	Provides utility methods for converting between geometry objects and matrix/array representations.
	"""
	
	@staticmethod
	def xyz2Array(xyz):
		"""
		Converts an XYZ point into an array.

		This function takes an XYZ point and converts its X, Y, and Z components into a list.

		Args:
			xyz (XYZ): The XYZ point to convert.

		Returns:
			list: A list containing the X, Y, and Z values of the given XYZ point.
		"""
		return [xyz.X, xyz.Y, xyz.Z]



	@staticmethod
	def array2Xyz(array):
		"""
		Converts an array into an XYZ point.

		This function takes a list containing three elements, representing X, Y, and Z values,
		and creates an XYZ point from them.

		Args:
			array (list): A list of three numeric values representing the X, Y, and Z coordinates.

		Returns:
			XYZ: An XYZ point created from the given array.
		"""
		return XYZ(array[0], array[1], array[2])
	


	@staticmethod
	def transform2Matrix(transform):
		"""
		Converts a transformation object into a 3x3 rotation matrix.

		This function extracts the BasisX, BasisY, and BasisZ vectors from a given transform object,
		representing the X, Y, and Z axes of the transformation's basis, and arranges them into a 3x3 matrix.

		Args:
			transform (Transform): The transformation object to convert.

		Returns:
			list: A 3x3 list of lists representing the rotation matrix derived from the transform object.
		"""
		matrix = []

		# Extracts the basis vectors and converts them into rows for the matrix
		xBasis = [transform.BasisX.X, transform.BasisX.Y, transform.BasisX.Z]
		yBasis = [transform.BasisY.X, transform.BasisY.Y, transform.BasisY.Z]
		zBasis = [transform.BasisZ.X, transform.BasisZ.Y, transform.BasisZ.Z]

		# Compiles the basis vectors into a matrix
		matrix.append(xBasis)
		matrix.append(yBasis)
		matrix.append(zBasis)

		return matrix
	


	@staticmethod
	def matrixDotProductArray(matrix, array):
		"""
		Computes the dot product of a matrix and an array.

		This function multiplies a 3x3 matrix by a 3-element array (vector) and returns the resulting 3-element array.

		Args:
			matrix (list of lists): A 3x3 matrix represented as a list of three lists, each containing three elements.
			array (list): A 3-element array representing a vector.

		Returns:
			list: A 3-element array resulting from the matrix and vector multiplication.
		"""
		result = [0, 0, 0]
		for i in range(len(matrix)):
			for j in range(len(array)):
				result[i] += matrix[i][j] * array[j]
		return result
	

	@staticmethod
	def reorderMinMax(min, max):
		"""
		Reorders the minimum and maximum XYZ points to ensure they are correctly aligned.

		This function compares the X, Y, and Z components of two given XYZ points, min and max,
		and rearranges their coordinates to ensure that the newMin point has the lowest values and
		the newMax point has the highest values for each dimension.

		Args:
			min (XYZ): The first XYZ point, potentially representing the minimum corner of a bounding box.
			max (XYZ): The second XYZ point, potentially representing the maximum corner of a bounding box.

		Returns:
			tuple: A tuple containing two XYZ points (newMin, newMax) where newMin has the lowest
				and newMax has the highest X, Y, and Z values respectively.
		"""
		# Determines the new minimum coordinates by comparing each dimension
		newMinX = min.X if min.X < max.X else max.X
		newMinY = min.Y if min.Y < max.Y else max.Y
		newMinZ = min.Z if min.Z < max.Z else max.Z

		# Determines the new maximum coordinates by comparing each dimension
		newMaxX = min.X if min.X > max.X else max.X
		newMaxY = min.Y if min.Y > max.Y else max.Y
		newMaxZ = min.Z if min.Z > max.Z else max.Z

		# Creates new XYZ points for the corrected minimum and maximum
		newMin = XYZ(newMinX, newMinY, newMinZ)
		newMax = XYZ(newMaxX, newMaxY, newMaxZ)

		return newMin, newMax

		
	