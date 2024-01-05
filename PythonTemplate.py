"""
PYTHON TEMPLATE
-----------------------------------
Created by Maycon Freitas
www.linkedin.com/in/maycon-freitas/
maycon.freitas@aecoder.com.br
-----------------------------------
Orientations:
- Remove the # from the libraries you want to use
- Add the libraries you want to use
- Modify inputs and outputs as needed
- Remove the methods you don't want to use
"""


### Libraries ###

import System
import sys
pyt_path = System.Environment.GetFolderPath(System.Environment.SpecialFolder.ProgramFilesX86)
#r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append("%s\IronPython 2.7\Lib" %pyt_path)
import clr
import os
#import webbrowser
import unicodedata
#import io
#import tempfile
import math
import traceback
#import json
#import datetime
import hashlib
#import collections
import itertools
#import urllib2
#import imp
import traceback
#from collections import OrderedDict

#clr.AddReference('DynamoRevitDS')
#import Dynamo 

clr.AddReference("System.Core")
clr.ImportExtensions(System.Linq)

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
from Revit.Elements import *
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference('System')
from System.Collections.Generic import List

clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import *
from System.Windows.Forms import Application, Form, ProgressBar, ProgressBarStyle

clr.AddReference("System.Drawing")
from System.Drawing import *
from System.Drawing import Size, Point

#clr.AddReference("System.Data")
#from System.Data import *
#clr.AddReference("System.Linq")
#clr.AddReference("System.Threading.Tasks")
#clr.AddReference("System.Windows.Forms")
#from System.Windows.Forms import *
#clr.AddReference('System.Windows.Forms.DataVisualization')



### Global Variables ###

doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
uidoc = uiapp.ActiveUIDocument


### Classes ###

# class ProgressBarForm(Form):
# 	def __init__(self, max_val, title = "Progress"):
# 		self.title = title
# 		self.max_val = max_val
# 		self.InitializeComponent()

# 	def InitializeComponent(self):
# 		try:
# 			# Set the size and position of the form
# 			self.Width = 350
# 			self.Height = 100
# 			self.StartPosition = FormStartPosition.CenterScreen
# 			self.Text = self.title

# 			# Create and configure the progress bar
# 			self.progressBar = ProgressBar()
# 			self.progressBar.Location = Point(10, 10)
# 			self.progressBar.Width = self.Width - 40  # Dynamic width
# 			self.progressBar.Height = 30
# 			self.progressBar.Maximum = self.max_val
# 			self.progressBar.Style = ProgressBarStyle.Continuous

# 			# Add the controls to the form
# 			self.Controls.Add(self.progressBar)
# 		except:
# 			# Close the form
# 			self.Close()

# 	def update_progress(self, val):
# 		try:
# 			# Update the progress bar value
# 			self.progressBar.Value = val
# 			Application.DoEvents()  # Process events to update UI
# 			if val >= self.max_val:
# 				self.Close()
# 		except:
# 			#Close the form
# 			self.Close()
	
# 	def close(self):
# 		#Dispose the form, clear memory and close
# 		self.Dispose()
# 		self.Close()



### Functions ###

def processList(_func, _list):
	"""
	Recursively processes elements of a list using a specified function.

	Parameters:
		_func (function): The function to be applied to the elements of the list.
		_list (list): The input list to be processed.

	Returns:
		list: A new list with elements processed by the given function.

	Example:
		Suppose we have a list 'numbers' containing integers: [1, 2, [3, 4], [5, [6, 7]]].
		If we call processList(lambda x: x*2, numbers), it will return [2, 4, [6, 8], [10, [12, 14]]].
	"""
	return list(map(lambda x: processList(_func, x) if type(x) == list else _func(x), _list))



# def processParallelLists(_func, *lists):
# 	"""
# 	Recursively processes elements from multiple lists in parallel using a specified function.

# 	Parameters:
# 		_func (function): The function to be applied to elements from the lists.
# 		*lists (lists): Variable number of lists as input, separated by commas.

# 	Returns:
# 		list: A new list with elements processed by the given function.

# 	Example:
# 		Suppose we have two lists 'numbers1' and 'numbers2' containing integers:
# 		numbers1 = [1, 2, 3]
# 		numbers2 = [4, 5, 6]
# 		If we call processParallelLists(lambda x, y: x + y, numbers1, numbers2),
# 		it will return [5, 7, 9], as it adds corresponding elements of the two lists.

# 		If there is a nested list in the input, the function will process nested elements:
# 		numbers3 = [7, [8, 9]]
# 		If we call processParallelLists(lambda x, y: x * y, numbers1, numbers3),
# 		it will return [7, [16, 27]], as it multiplies corresponding elements,
# 		and processes the nested list elements accordingly.
# 	"""
# 	return list(map(lambda *xs: processParallelLists(_func, *xs) if all(type(x) is list for x in xs) else _func(*xs), *lists))


def unwrap(ele):
	"""
	Unwraps a Revit element from a Dynamo element.

	Parameters:
		ele: A Dynamo element representing a Revit element.

	Returns:
		object: The unwrapped Revit element.

	Example:
		Suppose we have a Dynamo element 'dyn_element' representing a Revit wall.
		If we call unwrap(dyn_element), it will return the actual Revit wall element.

	Note:
		This function is used in the context of Dynamo for Revit, where elements are wrapped to provide
		additional functionality in the Dynamo environment. The 'unwrap' function is commonly used to
		retrieve the underlying Revit element from the Dynamo wrapper for further manipulation within
		the Revit environment.
	"""
	return UnwrapElement(ele)


# def wrap(ele):
# 	"""
# 	Wraps a Revit element to create a Dynamo element.

# 	Parameters:
# 		ele: A Revit element to be wrapped.

# 	Returns:
# 		object: The wrapped Dynamo element.

# 	Example:
# 		Suppose we have a Revit wall 'revit_wall' in the Revit environment.
# 		If we call wrap(revit_wall), it will return the corresponding Dynamo element
# 		representing the Revit wall in the Dynamo environment.

# 	Note:
# 		This function is used in the context of Dynamo for Revit, where elements from the Revit
# 		environment can be wrapped to create Dynamo elements. The 'wrap' function is commonly used
# 		to bring Revit elements into the Dynamo environment for further manipulation using Dynamo's
# 		visual scripting capabilities.
# 	"""
# 	return ele.ToProtoType()


# def removeSpecialCharacters(txt):
# 	"""
# 	Removes special characters from a given text.

# 	Parameters:
# 		txt (str): The input text from which special characters need to be removed.

# 	Returns:
# 		str: The text with special characters removed.

# 	Example:
# 		Suppose we have a text 'Hello! This is an example text with some special characters: @#%^&*'.
# 		If we call removeSpecialCharacters('Hello! This is an example text with some special characters: @#%^&*'),
# 		it will return 'Hello! This is an example text with some special characters: '.

# 	Note:
# 		This function is useful for processing text that may contain special characters that are not
# 		needed or desired. It uses the 'unicodedata' module to normalize the text and remove special characters.
# 		The 'NFKD' normalization form decomposes the text into base characters and diacritics, and the 'ASCII'
# 		encoding with 'ignore' option removes any remaining non-ASCII characters.
# 	"""
# 	string = unicodedata.normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')
# 	return string


# def hashCode(codeBase, hashCode=hashlib.md5()):
# 	"""
# 	Computes the hash code of a given string using the MD5 hashing algorithm.

# 	Parameters:
# 		codeBase (str): The input string for which the hash code needs to be calculated.
# 		hashCode (hashlib object, optional): The hashing algorithm to be used. Defaults to hashlib.md5().

# 	Returns:
# 		list: A list containing the hashlib object used for hashing and the computed hash code in hexadecimal format.

# 	Example:
# 		Suppose we have a string 'Hello, world!' that we want to compute the hash code for.
# 		If we call hashCode('Hello, world!'), it will return a list containing the hashlib object
# 		used for hashing and the computed hash code in hexadecimal format.

# 	Note:
# 		This function uses the hashlib module to calculate the hash code of a string using the MD5
# 		hashing algorithm. The hashlib object is updated with the input string using the 'update'
# 		method, and the hash code is obtained in hexadecimal format using the 'hexdigest' method.
# 	"""
# 	hashCode.update(codeBase.encode())
# 	codUnico = hashCode.hexdigest()
# 	return [hashCode, codUnico]


# def encrypt(message, key):
#     """
#     Encrypt a given message using a simple XOR encryption algorithm.
    
#     This function takes a message and a key, converts them into bytes, and then applies 
#     an XOR operation between each byte of the message and the key. The resulting encrypted 
#     message is then converted to a hexadecimal string and returned.

#     Parameters:
#     message (str): The plaintext message that needs to be encrypted.
#     key (str): The key used for encryption. The length of the key can be less than the message as the key cycles through.

#     Returns:
#     str: The encrypted message represented as a hexadecimal string.
#     """

#     # Convert the message and key into bytes
#     message_bytes = bytearray(message, 'utf-8')
#     key_bytes = bytearray(key, 'utf-8')

#     # Apply XOR operation byte by byte
#     # The key bytes are repeated to match the length of the message bytes if needed
#     encrypted_bytes = bytearray(x ^ y for x, y in zip(message_bytes, key_bytes * (len(message_bytes) // len(key_bytes) + 1)))

#     # Convert the encrypted bytes to a hexadecimal string
#     encrypted_hex = ''.join(format(b, '02x') for b in encrypted_bytes)
#     return encrypted_hex


# def decrypt(encrypted_hex, key):
#     """
#     Decrypt a given message using a simple XOR decryption algorithm.

#     This function takes an encrypted message in hexadecimal format and a key, converts them into bytes, 
#     then applies an XOR operation between each byte of the encrypted message and the key to decrypt it. 
#     The resulting decrypted message is converted back into a string and returned.

#     Parameters:
#     encrypted_hex (str): The encrypted message in hexadecimal format that needs to be decrypted.
#     key (str): The key used for decryption. The key cycles through if it is shorter than the encrypted message.

#     Returns:
#     str: The decrypted message.
#     """

#     # Convert the key into bytes
#     key_bytes = bytearray(key, 'utf-8')

#     # Convert the hexadecimal representation to bytes
#     encrypted_bytes = bytearray.fromhex(encrypted_hex)

#     # Apply XOR operation byte by byte
#     # The key bytes are repeated to match the length of the encrypted bytes if needed
#     decrypted_bytes = bytearray(x ^ y for x, y in zip(encrypted_bytes, key_bytes * (len(encrypted_bytes) // len(key_bytes) + 1)))

#     # Convert the decrypted bytes back into the original message
#     decrypted_message = decrypted_bytes.decode('utf-8')
#     return decrypted_message


# def openDirectoryDialog():
#     """
#     Opens a directory dialog to allow the user to select a folder.

#     Returns:
#         str or None: The selected folder path if a folder is selected, or None if the user cancels the operation.
#     """
#     # Create a new instance of FolderBrowserDialog
#     folder_dialog = FolderBrowserDialog()
    
#     # Show the folder dialog and store the result
#     result = folder_dialog.ShowDialog()
    
#     # Check if the user selected a folder
#     if result == System.Windows.Forms.DialogResult.OK:
#         # Get the selected folder path
#         selected_folder = folder_dialog.SelectedPath
#         return selected_folder
#     else:
#         # User canceled the operation, return None
#         return None


# def openSaveFileDialog():
#     """
#     Opens a save file dialog to allow the user to select a file path.

#     Returns:
#         str or None: The selected file path if a file is selected, or None if the user cancels the operation.
#     """
#     # Creates a new instancfe of SaveFileDialog
#     save_dialog = SaveFileDialog()

#     # Defines saving properties for the dialog
#     save_dialog.Filter = "Excel Workbook (*.xlsx)|*.xlsx"
#     save_dialog.Title = "Save File"

#     # Shows the save dialog and stores the result
#     result = save_dialog.ShowDialog()

#     # Verifies if the user selected a file
#     if result == System.Windows.Forms.DialogResult.OK:
#         # Gets the selected file path
#         selected_file = save_dialog.FileName
#         return selected_file
#     else:
#         # The user canceled the operation, return None
#         return None


# def openFileDialog():
# 	"""
# 	Opens a file dialog to select a file path and returns the selected file path as a string.

# 	Returns:
# 		str: The selected file path as a string.

# 	Example:
# 		Suppose we call openPathDialog() to open a file dialog and select a file.
# 		After selecting the file, the function will return the file path as a string.

# 	Note:
# 		This function uses the 'OpenFileDialog' class from the 'System.Windows.Forms' namespace
# 		to create a file dialog that allows the user to select a file from the file system.
# 		Once the user selects a file and clicks 'OK' in the file dialog, the selected file path
# 		is retrieved using the 'FileName' property of the 'OpenFileDialog' object and returned as a string.
# 	"""
# 	fileDialog = OpenFileDialog()
# 	fileDialog.ShowDialog()
# 	selectedFile = fileDialog.FileName
# 	return str(selectedFile)


# def transposeList(lista):
# 	"""
# 	Transposes a given 2D list.

# 	Parameters:
# 		lista (list): The 2D list to be transposed.

# 	Returns:
# 		list: The transposed 2D list.

# 	Example:
# 		Suppose we have the following 2D list 'matrix':
# 		matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 		If we call transposeList(matrix), it will return the transposed list:
# 		[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# 	Note:
# 		This function takes a 2D list as input and transposes it, swapping rows with columns.
# 		It uses nested list comprehensions to perform the transpose operation efficiently.
# 		The function assumes that the input list is a valid 2D list with consistent row lengths.
# 	"""
# 	return [[lista[j][i] for j in range(len(lista))] for i in range(len(lista[0]))]



# def matchCategory(element, builtinCat):
# 	"""
# 	Checks if a given element in Revit matches a specified built-in category.

# 	Parameters:
# 		element: The Revit element to be checked.
# 		builtinCat (Enum): The built-in category to be matched against.

# 	Returns:
# 		bool: True if the element matches the specified category, False otherwise.

# 	Example:
# 		Suppose we have a Revit element 'wallElement' and an Enum 'BuiltInCategory.Walls' representing
# 		the built-in category for walls in Revit.
# 		If we call matchCategory(wallElement, BuiltInCategory.Walls), it will return True if 'wallElement'
# 		is a wall and False otherwise.

# 	Note:
# 		This function checks if the given 'element' is assigned to the specified 'builtinCat' category.
# 		It first tries to get the category from the element using the 'Category' property.
# 		If that fails, it attempts to retrieve the category from the first element in the list (if element is a list).
# 		The function then compares the integer value of the category ID with the integer value of the
# 		built-in category, returning True if they match, and False otherwise.
# 	"""
# 	try:
# 		cat = element.Category
# 	except:
# 		try:
# 			cat = element[0].Category
# 		except:
# 			return False
# 	if element != None and cat != None:
# 		if cat.Id.IntegerValue.ToString() == builtinCat.value__.ToString():
# 			return True
# 		else:
# 			return False
# 	else:
# 		False


# #Flatten a list of lists
# def flatten(lista):
# 	"""
# 	Flattens a nested list into a single-level list.

# 	Parameters:
# 		lista (list): The nested list to be flattened.

# 	Returns:
# 		list: The flattened single-level list.

# 	Example:
# 		Suppose we have the following nested list 'nested_list':
# 		nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
# 		If we call flatten(nested_list), it will return the flattened list:
# 		[1, 2, 3, 4, 5, 6, 7, 8]

# 	Note:
# 		This function uses the 'itertools.chain' function to flatten the nested list into a single-level list.
# 		It takes advantage of the '*' unpacking operator to pass the nested lists as separate arguments to 'chain'.
# 	"""
# 	return list(itertools.chain(*lista))



# def addToClipBoard(text):
# 	"""
# 	Copies the specified text to the clipboard.

# 	Parameters:
# 		text (str): The text to be copied to the clipboard.

# 	Returns:
# 		None

# 	Example:
# 		Suppose we have a string 'Hello, world!' that we want to copy to the clipboard.
# 		If we call addToClipBoard('Hello, world!'), it will copy the text to the clipboard.

# 	Note:
# 		This function utilizes the 'os.system' function to execute a shell command to copy the specified text to the clipboard.
# 		The 'echo' command is used to output the text, and the 'clip' command is used to copy the output to the clipboard.
# 	"""
# 	command = 'echo ' + text.strip() + '| clip'
# 	os.system(command)


# def calculateDistanceTwoPoints(p1, p2):
# 	"""
# 	Calculates the 3D distance between two points in the Dynamo Revit environment.

# 	Parameters:
# 		p1 (Point): The first point as a Dynamo Point object with X, Y, and Z coordinates.
# 		p2 (Point): The second point as a Dynamo Point object with X, Y, and Z coordinates.

# 	Returns:
# 		float: The distance between the two points.

# 	Example:
# 		Suppose we have two Dynamo Points 'point1' and 'point2', representing two 3D points.
# 		If we call calculateDistanceTwoPoints(point1, point2), it will return the 3D distance
# 		between 'point1' and 'point2'.

# 	Note:
# 		This function calculates the 3D Euclidean distance between two points using the formula:
# 		distance = sqrt((x1 - x2)^2 + (y1 - y2)^2 + (z1 - z2)^2), where (x1, y1, z1) and (x2, y2, z2)
# 		are the coordinates of the two points, respectively.
# 	"""
# 	_x1 = p1.X
# 	_x2 = p2.X
# 	_y1 = p1.Y
# 	_y2 = p2.Y
# 	_z1 = p1.Z
# 	_z2 = p2.Z
# 	calc = math.sqrt((_x1 - _x2)**2 + (_y1 - _y2)**2 + (_z1 - _z2)**2)
# 	return calc


# #Verify if two points are the same based on a tolerance
# def isSamePoint(p1, p2, tolerance = 0.001):
# 	"""
# 	Checks if two points in the Dynamo Revit environment are the same within a specified tolerance.

# 	Parameters:
# 		p1 (Point): The first point as a Dynamo Point object with X, Y, and Z coordinates.
# 		p2 (Point): The second point as a Dynamo Point object with X, Y, and Z coordinates.
# 		tolerance (float, optional): The maximum allowed difference between the two points to be considered the same.
# 									 Defaults to 0.001.

# 	Returns:
# 		bool: True if the points are the same within the specified tolerance, False otherwise.

# 	Example:
# 		Suppose we have two Dynamo Points 'point1' and 'point2', representing two 3D points.
# 		If we call isSamePoint(point1, point2, tolerance=0.001), it will return True if 'point1'
# 		and 'point2' are the same within the specified tolerance, and False otherwise.
	
# 	Note:
# 		This function uses the 'calculateDistanceTwoPoints' function to calculate the 3D distance
# 		between the two points. If the calculated distance is less than or equal to the specified 'tolerance',
# 		the points are considered the same, and the function returns True; otherwise, it returns False.
# 	"""
# 	if calculateDistanceTwoPoints(p1, p2) <= tolerance:
# 		return True
# 	else:
# 		return False


# def degreeToRadian(degree):
#     """
#     Converts an angle from degrees to radians.

#     Parameters:
#         degree (float or int): The angle in degrees.

#     Returns:
#         float: The angle converted to radians.

#     Raises:
#         None

#     Example:
#         >>> degreeToRadian(90)
#         1.5707963267948966
#         >>> degreeToRadian(45)
#         0.7853981633974483
#     """
#     import math
#     return degree * math.pi / 180


# def radianToDegree(radian):
#     """
#     Converts an angle from radians to degrees.

#     Parameters:
#         radian (float or int): The angle in radians.

#     Returns:
#         float: The angle converted to degrees.

#     Raises:
#         None

#     Example:
#         >>> radianToDegree(1.5707963267948966)
#         90.0
#         >>> radianToDegree(0.7853981633974483)
#         45.0
#     """
#     import math
#     return radian * 180 / math.pi





### Inputs ###

toggle = IN[0]
elements = processList(unwrap, IN[1])


### Code ###

finalList = []
if toggle:
	try:

		# TransactionManager.Instance.ForceCloseTransaction()
		trans = Transaction(doc, "Transaction title that appears in Revit undo history")
		trans.Start()

		# subTrans = SubTransaction(doc)
		# subTrans.Start()

		#Code here...

		# subTrans.Commit()

		trans.Commit()

		OUT = finalList

	except:
		try:
			msg = traceback.format_exception_only(sys.exc_info()[0], sys.exc_info()[1])[0].replace("Exception: ", "")
		except:
			msg = "An error has occurred. See details to get more information."
		errorReport = traceback.format_exc()
		taskDialog = TaskDialog("Error")
		taskDialog.MainInstruction = msg
		taskDialog.ExpandedContent = errorReport
		taskDialog.Show()
		OUT = errorReport
else:
	OUT = "The execution was cancelled by the user."