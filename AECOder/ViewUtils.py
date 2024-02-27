import clr

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

from AECOder.Geometry2MatrixUtils import *

class ViewUtils:
	"""
	Provides utility methods for working with views in the Revit API.
	"""
	
	@staticmethod
	def adjustCropBoxToElements(view, element, offsetFactor = 0.01):
		"""
		Adjusts the crop box of a view to fit around a given element or set of elements.

		This function takes a view and an element or set of elements and adjusts the crop box of the view
		to fit around the bounding box of the element(s). The crop box is expanded by the given offset factor
		in all directions to ensure that the element(s) are fully visible in the view.

		Args:
			view (View): The view to adjust the crop box of.
			element (Element or list[Element]): The element or set of elements to fit the crop box around.
			offsetFactor (float): The amount by which to expand the crop box in all directions.

		Returns:
			None
		"""
		bb = BoundingBoxXYZ()
		try:
			maxX = int.MinValue
			maxY = int.MinValue
			maxZ = int.MinValue
			minX = int.MaxValue
			minY = int.MaxValue
			minZ = int.MaxValue
			for e in element:
				bbTemp = e.get_BoundingBox(view)
				if bbTemp != None:
					maxX = max(maxX, bbTemp.Max.X)
					maxY = max(maxY, bbTemp.Max.Y)
					maxZ = max(maxZ, bbTemp.Max.Z)
					minX = min(minX, bbTemp.Min.X)
					minY = min(minY, bbTemp.Min.Y)
					minZ = min(minZ, bbTemp.Min.Z)
			bb.Max = XYZ(maxX, maxY, maxZ)
			bb.Min = XYZ(minX, minY, minZ)
		except:
			bb = element.get_BoundingBox(view)

		if bb != None:
			#Check if the view is a 3D view
			if view.ViewType == ViewType.ThreeD:
				bb.Min = XYZ(bb.Min.X - offsetFactor, bb.Min.Y - offsetFactor, bb.Min.Z - offsetFactor)
				bb.Max = XYZ(bb.Max.X + offsetFactor, bb.Max.Y + offsetFactor, bb.Max.Z + offsetFactor)
				view.SetSectionBox(bb)
			elif view.ViewType == ViewType.Elevation:
				viewCropBox = view.CropBox

				viewCropBoxMin = viewCropBox.Min
				viewCropBoxMax = viewCropBox.Max
				
				bbMaxPt = bb.Max
				bbMinPt = bb.Min
				
				viewTransform = Geometry2MatrixUtils.transform2Matrix(viewCropBox.Transform)

				bbMinPtArray = Geometry2MatrixUtils.xyz2Array(bbMinPt)
				bbMinPtArrayTransformed = Geometry2MatrixUtils.matrixDotProductArray(viewTransform, bbMinPtArray)
				bbMinPtTransformed = Geometry2MatrixUtils.array2Xyz(bbMinPtArrayTransformed)

				bbMaxPtArray = Geometry2MatrixUtils.xyz2Array(bbMaxPt)
				bbMaxPtArrayTransformed = Geometry2MatrixUtils.matrixDotProductArray(viewTransform, bbMaxPtArray)
				bbMaxPtTransformed = Geometry2MatrixUtils.array2Xyz(bbMaxPtArrayTransformed)
				
				viewOriginArray = Geometry2MatrixUtils.xyz2Array(viewCropBox.Transform.Origin)
				viewOriginArrayTransformed = Geometry2MatrixUtils.matrixDotProductArray(viewTransform, viewOriginArray)
				viewOriginTransformed = Geometry2MatrixUtils.array2Xyz(viewOriginArrayTransformed)
				
				bbMinPtOrdered, bbMaxPtOrdered = Geometry2MatrixUtils.reorderMinMax(bbMinPtTransformed, bbMaxPtTransformed)

				newBbMin = XYZ(bbMinPtOrdered.X - viewOriginTransformed.X - offsetFactor, bbMinPtOrdered.Y - viewOriginTransformed.Y - offsetFactor, viewCropBoxMin.Z - offsetFactor)

				newBbMax = XYZ(bbMaxPtOrdered.X - viewOriginTransformed.X + offsetFactor, bbMaxPtOrdered.Y - viewOriginTransformed.Y + offsetFactor, viewCropBoxMax.Z + offsetFactor)

				viewCropBox.Min = newBbMin
				viewCropBox.Max = newBbMax

				view.CropBox = viewCropBox
				view.CropBoxActive = True
				view.CropBoxVisible = False

			else:
				bb.Min = XYZ(bb.Min.X - offsetFactor, bb.Min.Y - offsetFactor, bb.Min.Z)
				bb.Max = XYZ(bb.Max.X + offsetFactor, bb.Max.Y + offsetFactor, bb.Max.Z)
				view.CropBox = bb
				view.CropBoxActive = True
				view.CropBoxVisible = False