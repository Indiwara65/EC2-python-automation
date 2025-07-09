# This script is optional
# If this script is not used functions will be needed to be imported as show in 1 else 2
# 1. from module_1.additions import add
# 2. from module_1 import add
__version__ = "1.0.0"

from .additions import add

__all__ = [add]