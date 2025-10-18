#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This is an example of how to write a modern plugin for IDA Pro
It is just a little more verbose version of IDAs own example: https://github.com/HexRaysSA/ida-sdk/blob/main/src/plugins/hello/pyhello.py
There is also a guide on how to write a Python plugin here: https://docs.hex-rays.com/developer-guide/idapython/how-to-create-a-plugin

All credits to Elias @ https://www.youtube.com/watch?v=rG7ArXYzwqw
'''

__version__ = "2025-10-18 23:29:01"
__author__ = "Harding"
__description__ = __doc__
__copyright__ = "Copyright 2025"
__credits__ = ["https://www.youtube.com/@allthingsida"]
__license__ = "GPL 3.0"
__maintainer__ = "Harding"
__email__ = "not.at.the.moment@example.com"
__status__ = "Development"
__url__ = "https://github.com/Harding-Stardust/IDA_modern_plugin_example"

from typing import Optional
import ida_idaapi as _ida_idaapi # type: ignore[import-untyped]
from pydantic import validate_call # pip install pydantic

_G_PLUGIN_NAME = "IDA_modern_plugin_example"
_G_WANTED_HOTKEY = "Ctrl + Alt + F8".replace('+', '-').replace(' ', '') # No spaces! And '+' should be '-'

class modern_plugmod_t(_ida_idaapi.plugmod_t):
    ''' This is the code that is actually run '''
    
    @validate_call(config={"arbitrary_types_allowed": True, "strict": True, "validate_return": True})
    def __init__(self) -> None:
        print(f"{_G_PLUGIN_NAME} is running the constructor")
        return

    @validate_call(config={"arbitrary_types_allowed": True, "strict": True, "validate_return": True})
    def run(self, arg_user_argument: int) -> int:
        print(f"Hello from {_G_PLUGIN_NAME}! arg_user_argument: {arg_user_argument}")
        return 0
    
    @validate_call(config={"arbitrary_types_allowed": True, "strict": True, "validate_return": True})
    def __del__(self) -> None:
        ''' This code is run when the user closes the IDB '''
        print(f"{_G_PLUGIN_NAME} is running the destructor")
        return

class modern_plugin_t(_ida_idaapi.plugin_t):
    ''' This is the config for the plugin, the actual code is in modern_plugmod_t() '''
    flags = _ida_idaapi.PLUGIN_MULTI # if this flag is set, then init have to return a ida_idaapi.plugmod_t()
    comment = f"{_G_PLUGIN_NAME}:This is the comment. This is shown in the status bar."
    help = f"{_G_PLUGIN_NAME}:This is the help"
    wanted_name = f"{_G_PLUGIN_NAME}:This is what is shown in the Edit->Plugins->this_name"
    wanted_hotkey = _G_WANTED_HOTKEY

    @validate_call(config={"arbitrary_types_allowed": True, "strict": True, "validate_return": True})
    def init(self) -> Optional[_ida_idaapi.plugmod_t]:
        ''' We can do checking and if we don't want to be loaded, we can return None.
        If we want to be loaded, then we return a ida_idaapi.plugmod_t
        '''
        return modern_plugmod_t()

    # def run(self, arg: int): pass # Since IDA 8.3, these are no longer needed and should be removed in the real plugin.
    # def term(self): pass # 

# @validate_call(config={"arbitrary_types_allowed": True, "strict": True, "validate_return": True}) # For unknown reasons, IDA crash with this line?!
def PLUGIN_ENTRY() -> _ida_idaapi.plugin_t:
    return modern_plugin_t()