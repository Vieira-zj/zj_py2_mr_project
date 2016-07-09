# -*- coding: utf-8 -*-

#--------------------------------------------------------
# MonkeyRunner.class
#--------------------------------------------------------

print 'FOR APIS'

# (
# doc="Waits for the workstation to connect to the device.", 
# args={"timeout", "deviceId"}, 
# argDocs={"The timeout in seconds to wait. The default is to wait indefinitely.", 
# "A regular expression that specifies the device name. 
# See the documentation for 'adb' in the Developer Guide to learn more about device names."}, 
# returns="A ChimpDevice object representing the connected device."
# )
# public static MonkeyDevice waitForConnection()
def waitForConnection():
    print 'FOR API'


# (
# doc="Pause the currently running program for the specified number of seconds.", 
# args={"seconds"}, 
# argDocs={"The number of seconds to pause."}
# )
# public static void sleep()
def sleep():
    print 'FOR API'


# (
# doc="Format and display the API reference for MonkeyRunner.", 
# args={"format"}, 
# argDocs={"The desired format for the output, either 'text' for plain text or 'html' for HTML markup."}, 
# returns="A string containing the help text in the desired format."
# )
# public static String help()
def help():
    print 'FOR API'


# (
# doc="Display an alert dialog to the process running the current script. 
# The dialog is modal, so the script stops until the user dismisses the dialog.", 
# args={"message", "title", "okTitle"}, 
# argDocs={"The message to display in the dialog.", "The dialog's title. The default value is 'Alert'.", 
# "The text to use in the dialog button. The default value is 'OK'."}
# )
# public static void alert()
def alert():
    print 'FOR API'


# (
# doc="Display a dialog that accepts input. 
# The dialog is ,modal, so the script stops until the user clicks one of the two dialog buttons. 
# To enter a value, the user enters the value and clicks the 'OK' button. 
# To quit the dialog without entering a value, the user clicks the 'Cancel' button. 
# Use the supplied arguments for this method to customize the text for these buttons.", 
# args={"message", "initialValue", "title", "okTitle", "cancelTitle"}, 
# argDocs={"The prompt message to display in the dialog.", "The initial value to supply to the user. The default is an empty string)", 
# "The dialog's title. The default is 'Input'", 
# "The text to use in the dialog's confirmation button. The default is 'OK'. 
# The text to use in the dialog's 'cancel' button. The default is 'Cancel'."}, 
# returns="The test entered by the user, or None if the user canceled the input;"
# )
# public static String input()
def input():
    print 'FOR API'


# (
# doc="Display a choice dialog that allows the user to select a single item from a list of items.", 
# args={"message", "choices", "title"}, 
# argDocs={"The prompt message to display in the dialog.", 
# "An iterable Python type containing a list of choices to display", 
# "The dialog's title. The default is 'Input'"}, 
# returns="The 0-based numeric offset of the selected item in the iterable."
# )
# public static int choice()
def choice():
    print 'FOR API'


# (
# doc="Loads a MonkeyImage from a file.", 
# args={"path"}, 
# argDocs={"The path to the file to load. 
# This file path is in terms of the computer running MonkeyRunner and not a path on the Android Device. "}, 
# returns="A new MonkeyImage representing the specified file"
# )
# public static MonkeyImage loadImageFromFile()
def loadImageFromFile():
    print 'FOR API'


#--------------------------------------------------------
# MonkeyDevice.class
#--------------------------------------------------------
# (
# doc="Get the HierarchyViewer object for the device.", 
# returns="A HierarchyViewer object"
# )
# public HierarchyViewer getHierarchyViewer()
def getHierarchyViewer():
    print 'FOR API'


# (
# doc="Gets the device's screen buffer, yielding a screen capture of the entire display.", 
# returns="A MonkeyImage object (a bitmap wrapper)"
# )
# public MonkeyImage takeSnapshot()
def takeSnapshot():
    print 'FOR API'


# (
# doc="Given the name of a variable on the device, returns the variable's value", 
# args={"key"}, 
# argDocs={"The name of the variable. 
# The available names are listed in http://developer.android.com/guide/topics/testing/monkeyrunner.html."}, 
# returns="The variable's value"
# )
# public String getProperty()
def getProperty():
    print 'FOR API'


# (
# doc="Synonym for getProperty()", 
# args={"key"}, 
# argDocs={"The name of the system variable."}, 
# returns="The variable's value."
# )
# public String getSystemProperty()
def getSystemProperty():
    print 'FOR API'


# (
# doc="Sends a touch event at the specified location", 
# args={"x", "y", "type"}, 
# argDocs={"x coordinate in pixels", "y coordinate in pixels", "touch event type as returned by TouchPressType()"}
# )
# public void touch()
def touch():
    print 'FOR API'

# (
# doc="Simulates dragging (touch, hold, and move) on the device screen.", 
# args={"start", "end", "duration", "steps"}, 
# argDocs={"The starting point for the drag (a tuple (x,y) in pixels)", 
# "The end point for the drag (a tuple (x,y) in pixels", 
# "Duration of the drag in seconds (default is 1.0 seconds)", 
# "The number of steps to take when interpolating points. (default is 10)"}
# )
# public void drag()
def drag():
    print 'FOR API'

# (
# doc="Send a key event to the specified key", 
# args={"name", "type"}, 
# argDocs={"the keycode of the key to press (see android.view.KeyEvent)", 
# "touch event type as returned by TouchPressType(). To simulate typing a key, send DOWN_AND_UP"}
# )
# public void press()
def press():
    print 'FOR API'


# (
# doc="Types the specified string on the keyboard. 
# This is equivalent to calling press(keycode, DOWN_AND_UP) for each character in the string.", 
# args={"message"}, argDocs={"The string to send to the keyboard."}
# )
# public void type()
def type():
    print 'FOR API'
    

# (
# doc="Executes an adb shell command and returns the result, if any.", 
# args={"cmd", "timeout"}, 
# argDocs={"The adb shell command to execute.", 
# "This arg is optional. It specifies the maximum amount of time during which the command can go without any output. 
# A value of 0 means the method will wait forever. The unit of the timeout is millisecond"}, 
# returns="The output from the command."
# )
# public String shell()
def shell():
    print 'FOR API'


# (
# doc="Reboots the specified device into a specified bootloader.", 
# args={"into"}, 
# argDocs={"the bootloader to reboot into: bootloader, recovery, or None"})
# public void reboot()
def reboot():
    print 'FOR API'


# (
# doc="Installs the specified Android package (.apk file) onto the device. 
# If the package already exists on the device, it is replaced.", 
# args={"path"}, 
# argDocs={"The package's path and filename on the host filesystem."}, 
# returns="True if the install succeeded"
# )
# public boolean installPackage()
def installPackage():
    print 'FOR API'


# (
# doc="Deletes the specified package from the device, including its associated data and cache.", 
# args={"package"}, 
# argDocs={"The name of the package to delete."}, 
# returns="True if remove succeeded"
# )
# public boolean removePackage()
def removePackage():
    print 'FOR API'


# (
# doc="Starts an Activity on the device by sending an Intent constructed from the specified parameters.", 
# args={"uri", "action", "data", "mimetype", "categories", "extras", "component", "flags"}, 
# argDocs={"The URI for the Intent.", 
# "The action for the Intent.", 
# "The data URI for the Intent", 
# "The mime type for the Intent.", 
# "A Python iterable containing the category names for the Intent.", 
# "A dictionary of extras to add to the Intent. Types of these extras are inferred from the python types of the values.", 
# "The component of the Intent.", 
# "An iterable of flags for the Intent. All arguments are optional. 
# The default value for each argument is null.(see android.content.Intent)"}
# )
# public void startActivity()
def startActivity():
    print 'FOR API'


# (
# doc="Sends a broadcast intent to the device.", 
# args={"uri", "action", "data", "mimetype", "categories", "extras", "component", "flags"}, 
# argDocs={"The URI for the Intent.", "The action for the Intent.", "The data URI for the Intent", 
# "The mime type for the Intent.", "An iterable of category names for the Intent.", 
# "A dictionary of extras to add to the Intent. Types of these extras are inferred from the python types of the values.", 
# "The component of the Intent.", 
# "An iterable of flags for the Intent.All arguments are optional. 
# The default value for each argument is null.(see android.content.Context.sendBroadcast(Intent))"}
# )
# public void broadcastIntent()
def broadcastIntent():
    print 'FOR API'


# (
# doc="Run the specified package with instrumentation and return the output it generates. 
# Use this to run a test package using InstrumentationTestRunner.", 
# args={"className", "args"}, 
# argDocs={"The class to run with instrumentation. The format is packagename/classname. 
# Use packagename to specify the Android package to run, 
# and classname to specify the class to run within that package. 
# For test packages, this is usually testpackagename/InstrumentationTestRunner", 
# "A map of strings to objects containing the arguments to pass to this instrumentation (default value is None)."}, 
# returns="A map of strings to objects for the output from the package. 
# For a test package, contains a single key-value pair: 
# the key is 'stream' and the value is a string containing the test output.")
# public PyDictionary instrument()
def instrument():
    print 'FOR API'


# (
# doc="Wake up the screen on the device"
# )
# public void wake()
def wake():
    print 'FOR API'


# (
# doc="Retrieve the properties that can be queried"
# )
# public PyList getPropertyList()
def getPropertyList():
    print 'FOR API'
    

# (
# doc="Retrieve the view ids for the current application"
# )
# public PyList getViewIdList()
def getViewIdList():
    print 'FOR API'

# (
# doc="Obtains the view with the specified id.", 
# args={"id"}, argDocs={"The id of the view to retrieve."}, 
# returns="The view object with the specified id."
# )
# public MonkeyView getViewById()
def getViewById():
    print 'FOR API'


# (
# doc="Obtains the view with the specified accessibility ids.", 
# args={"windowId", "accessibility id"}, 
# argDocs={"The window id of the view to retrieve.", "The accessibility id of the view to retrieve."}, 
# returns="The view object with the specified id."
# )
# public MonkeyView getViewByAccessibilityIds()
def getViewByAccessibilityIds():
    print 'FOR API'


# (
# doc="Obtains current root view", returns="The root view object"
# )
# public MonkeyView getRootView()
def getRootView():
    print 'FOR API'


# (
# doc="Obtains a list of views that contain the specified text.", 
# args={"text"}, argDocs={"The text to search for"}, 
# returns="A list of view objects that contain the specified text."
# )
# public PyList getViewsByText()
def getViewsByText():
    print 'FOR API'


#--------------------------------------------------------
# MonkeyView.class
#--------------------------------------------------------
# (
# doc="Get the checked status of the view", 
# returns="A boolean value for whether the item is checked or not"
# )
# public PyBoolean getChecked()
def getChecked():
    print 'for api'


# (
# doc="Returns the class name of the view", 
# returns="The class name of the view as a string"
# )
# public PyString getViewClass()
def getViewClass():
    print 'for api'


# (
# doc="Returns the text contained by the view", 
# returns="The text contained in the view"
# )
# public PyString getText()
def getText():
    print 'for api'


# (
# doc="Returns the location of the view in the form of a MonkeyRect", 
# returns="The location of the view as a MonkeyRect object"
# )
# public MonkeyRect getLocation()
def getLocation():
    print 'for api'


# (
# doc="Returns the enabled status of the view", 
# returns="The enabled status of the view as a boolean"
# )
# public PyBoolean getEnabled()
def getEnabled():
    print 'for api'


# (
# doc="Returns the selected status of the view", 
# returns="The selected status of the view as a boolean"
# )
# public PyBoolean getSelected()
def getSelected():
    print 'for api'


# (
# doc="Sets the selected status of the view", 
# args={"selected"}, argDocs={"The boolean value to set selected to"}
# )
# public void setSelected()
def setSelected():
    print 'for api'


# (
# doc="Returns the focused status of the view", 
# returns="The focused status of the view as a boolean"
# )
# public PyBoolean getFocused()
def getFocused():
    print 'for api'


# (
# doc="Sets the focused status of the view", 
# args={"focused"}, argDocs={"The boolean value to set focused to"}
# )
# public void setFocused()
def setFocused():
    print 'for api'


# (
# doc="Returns the parent of the current view", 
# returns="The parent of the view as a MonkeyView object"
# )
# public MonkeyView getParent()
def getParent():
    print 'for api'


# (
# doc="Returns the children of the current view", 
# returns="The children of the view as a list of MonkeyView objects"
# )
# public PyList getChildren()
def getChildren():
    print 'for api'

# (
# doc="Returns the accessibility ids of the current view", 
# returns="The accessibility ids of the view as a list of int and long"
# )
# public PyList getAccessibilityIds()
def getAccessibilityIds():
    print 'for api'


#--------------------------------------------------------
# MonkeyImage.class
#--------------------------------------------------------
# (
# doc="Converts the MonkeyImage into a particular format and returns the result as a String. 
# Use this to get access to the rawpixels in a particular format. String output is for better performance.", 
# args={"format"}, 
# argDocs={"The destination format (for example, 'png' for Portable Network Graphics format). The default is png."}, 
# returns="The resulting image as a String."
# )
# public byte[] convertToBytes()
def convertToBytes():
    print 'FOR API'


# (
# doc="Write the MonkeyImage to a file. 
# If no format is specified, this method guesses the output format based on the extension of the provided file extension. 
# If it is unable to guess the format, it uses PNG.", 
# args={"path", "format"}, 
# argDocs={"The output filename, optionally including its path", 
# "The destination format (for example, 'png' for Portable Network Graphics format."}, 
# returns="boolean true if writing succeeded."
# )
# public boolean writeToFile()
def writeToFile():
    print 'FOR API'


# (
# doc="Get a single ARGB (alpha, red, green, blue) pixel at location x,y. 
# The arguments x and y are 0-based, expressed in pixel dimensions. 
# X increases to the right, and Y increases towards the bottom. This method returns a tuple.", 
# args={"x", "y"}, 
# argDocs={"the x offset of the pixel", "the y offset of the pixel"}, 
# returns="A tuple of (A, R, G, B) for the pixel. Each item in the tuple has the range 0-255."
# )
# public PyObject getRawPixel()
def getRawPixel():
    print 'FOR API'

# (
# doc="Get a single ARGB (alpha, red, green, blue) pixel at location x,y. 
# The arguments x and y are 0-based, expressed in pixel dimensions. 
# X increases to the right, and Y increases towards the bottom. This method returns an Integer.", 
# args={"x", "y"}, 
# argDocs={"the x offset of the pixel", "the y offset of the pixel"}, 
# returns="An unsigned integer pixel for x,y. The 8 high-order bits are A, followed by 8 bits for R, 8 for G, and 8 for B."
# )
# public int getRawPixelInt()
def getRawPixelInt():
    print 'FOR API'

# (
# doc="Compare this MonkeyImage object to aother MonkeyImage object.", 
# args={"other", "percent"}, 
# argDocs={"The other MonkeyImage object.", 
# "A float in the range 0.0 to 1.0, indicating the percentage of pixels 
# that need to be the same for the method to return 'true'. Defaults to 1.0."}, 
# returns="boolean 'true' if the two objects contain the same image."
# )
# public boolean sameAs()
def sameAs():
    print 'FOR API'


# (
# doc="Copy a rectangular region of the image.", 
# args={"rect"}, argDocs={"A tuple (x, y, w, h) describing the region to copy. 
# x and y specify upper left hand corner of the region. w is the width of the region in pixels, and h is its height."}, 
# returns="a MonkeyImage object representing the copied region."
# )
# public MonkeyImage getSubImage()
def getSubImage():
    print 'FOR API'


#--------------------------------------------------------
# end
#--------------------------------------------------------
