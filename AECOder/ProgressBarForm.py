import clr

clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import *

clr.AddReference("System.Drawing")
from System.Drawing import *


class ProgressBarForm(Form):
	"""
	Represents a progress bar form for displaying the progress of a long-running operation.
	"""
	def __init__(self, max_val = 100, title = "Progress", increment = 1):
		"""
		Initializes a new instance of the ProgressBarForm class with the given title, maximum value, and increment.
		"""
		self.title = title
		self.max_val = max_val
		self.increment = increment
		self.InitializeComponent()

	def InitializeComponent(self):
		"""
		Initializes the components of the form.
		"""
		try:
			# Set the size and position of the form
			self.Width = 350
			self.Height = 100
			self.StartPosition = FormStartPosition.CenterScreen
			self.Text = self.title

			# Create and configure the progress bar
			self.progressBar = ProgressBar()
			self.progressBar.Location = Point(10, 10)
			self.progressBar.Width = self.Width - 40  # Dynamic width
			self.progressBar.Height = 30
			self.progressBar.Maximum = self.max_val
			self.progressBar.Style = ProgressBarStyle.Continuous
			self.progressBar.Value = 1

			# Add the controls to the form
			self.Controls.Add(self.progressBar)
		except:
			# Close the form
			self.Close()

	def update_progress(self):
		"""
		Updates the progress bar value by the increment amount.
		"""
		try:
			val = self.progressBar.Value + self.increment
			# Update the progress bar value
			self.progressBar.Value = val
			Application.DoEvents()  # Process events to update UI
			if val >= self.max_val:
				self.Close()
		except:
			#Close the form
			self.Close()
	
	def close(self):
		"""
		Closes the form and disposes of it.
		"""
		#Dispose the form, clear memory and close
		self.Dispose()
		self.Close()