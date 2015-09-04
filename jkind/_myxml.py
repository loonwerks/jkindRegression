
import xml.dom.minidom
from data.testdefns import XmlProperties


def parseXML( filename ):

    # Get the top level document
    doc = xml.dom.minidom.parse( filename )

    # Get a list of all the XmlProperties elements
    properties = doc.getElementsByTagName( 'Property' )

    # Initialize a list to contain the XmlProperties instantiations
    propList = list()

    for each in properties:

        # Instantiate our data
        theProp = XmlProperties()

        # Get the Name of the XmlProperties
        theProp.name = each.getAttribute( 'name' )

        # Get the Answer attribute. From that get the validity and the source
        # Assumes that there is only one Answer, etc...
        answerAttr = each.getElementsByTagName( 'Answer' )[0]
        theProp.answer = answerAttr.firstChild.data
        theProp.source = answerAttr.getAttribute( 'source' )

        # Get the K attribute and fill in the value
        kAttr = each.getElementsByTagName( 'K' )[0]
        theProp.K = kAttr.firstChild.data

        # Add to our list of Properties
        propList.append( theProp )

    return propList
