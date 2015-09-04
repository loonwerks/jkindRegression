
import os
from data.logger import Logger
from my_os.process import call
from my_os.dirs import copyFile
from my_os.dirs import deleteFile
from ._jkind_xml import parseXML
from data.testdefns import FileResults



def jkind_exec( filename, arg_string = '' ):
    '''
    '''
    a = 'jkind ' + filename + ' -xml ' + arg_string
    Logger().log( a )
    opt, err = call( a )
    Logger().incrementFileIdx()
    # print( 'opt= ' + opt.decode() )
    # print( 'err= ' + err.decode() )

    # Get the xml file that was generated and parse it for the attributes.
    # The xml parser will return an instance of the JKind Results class.
    xmlFile = filename + '.xml'
    xmlProps = parseXML( xmlFile )
    rv = FileResults( filename, arg_string, xmlProps )

    # Delete the xml file so we don't get fooled if a subsequent jkind
    # run fails.
    deleteFile( xmlFile )

    return rv