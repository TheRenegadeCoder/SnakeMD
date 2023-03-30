from .generator import *

def new_doc(name: str = None, separator: str = "-") -> Document:
    """
    Creates a new SnakeMD document. This is a convenience function
    that allows you to create a new markdown document without having
    to import the Document class. This is useful for anyone who
    wants to take advantage of the procedural interface of SnakeMD.
    For those looking for a bit more control, each element class
    will need to be imported as needed.

    .. code-block:: Python
    
        doc = snakemd.new_doc()

    .. versionadded:: 0.9.0

    :param str name: 
        the file name of the document without the extension
        
        .. deprecated:: 0.13.0
            parameter is now optional and will be removed in 1.0.0
            
    :param str separator: 
        the whitespace separator; defaults to -
    :return: a new Document object
    """
    if name:
        warnings.warn(
            "name has been deprecated as of 0.13.0", 
            DeprecationWarning
        )
    return Document(name, separator)
