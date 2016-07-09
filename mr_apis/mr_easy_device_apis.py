# -*- coding: utf-8 -*-

#--------------------------------------------------------
# EasyMonkeyDevice.class
#--------------------------------------------------------

print 'FOR APIS'

# (
# doc="Sends a touch event to the selected object.", 
# args={"selector", "type"}, 
# argDocs={"The selector identifying the object.", "The event type as returned by TouchPressType()."}
# )
# public void touch()
def touch():
    print 'for api'


# (
# doc="Types a string into the specified object.", 
# args={"selector", "text"}, 
# argDocs={"The selector identifying the object.", "The text to type into the object."}
# )
# public void type()
def type():
    print 'for api'


# (
# doc="Locates the coordinates of the selected object.", 
# args={"selector"}, argDocs={"The selector identifying the object."}, 
# returns="Tuple containing (x,y,w,h) location and size."
# )
# public PyTuple locate()
def locate():
    print 'for api'


# (
# doc="Checks if the specified object exists.", 
# args={"selector"}, returns="True if the object exists.", 
# argDocs={"The selector identifying the object."}
# )
# public boolean exists()
def exists():
    print 'for api'


# (
# doc="Checks if the specified object is visible.", 
# args={"selector"}, returns="True if the object is visible.", 
# argDocs={"The selector identifying the object."}
# )
# public boolean visible()
def visible():
    print 'for api'

# (
# doc="Obtain the text in the selected input box.", 
# args={"selector"}, argDocs={"The selector identifying the object."}, 
# returns="Text in the selected input box."
# )
# public String getText()
def getText():
    print 'for api'


# (
# doc="Gets the id of the focused window.", 
# returns="The symbolic id of the focused window or None."
# )
# public String getFocusedWindowId()
def getFocusedWindowId():
    print 'for api'


#--------------------------------------------------------
# By.class
#--------------------------------------------------------
# (
# doc="Select an object by id.", 
# args={"id"}, argDocs={"The identifier of the object."}
# )
# public static By id()
def id():
    print 'for api'


#--------------------------------------------------------
# end
#--------------------------------------------------------