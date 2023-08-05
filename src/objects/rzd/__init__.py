from pydantic import BaseModel, ConfigDict


def split_numbers_list(joinedList: str | None) -> list[str]:
    if joinedList is None: return []
    sep = ', ' if joinedList.find(' ') == -1 else ','
    return joinedList.split(sep)


def capitalize_first_symbol(text: str) -> str:
    return text[0].capitalize() + text[1:]


model_config = ConfigDict(
    alias_generator = capitalize_first_symbol,
    frozen = True,
)