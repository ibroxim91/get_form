from pydantic import RootModel
from typing import Dict

class FormData(RootModel[Dict[str, str]]):
    pass
