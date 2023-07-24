from enum import Enum

class NotionComperator(Enum):
    EQUALS = 'equals'
    THIS_WEEK = 'this_week'
    AFTER = 'after'
    BEFORE = 'before'
    DOES_NOT_EQUAL = 'does_not_equal'
    CONTAINS = 'contains'
    DOES_NOT_CONTAIN = 'does_not_contain'
    LESS_THAN = 'less_than'
    GREATER_THAN = 'greater_than'
    LESS_THAN_OR_EQUAL_TO = 'less_than_or_equal_to'
    GREATER_THAN_OR_EQUAL_TO = 'greater_than_or_equal_to'
    IS_EMPTY = 'is_empty'
    IS_NOT_EMPTY = 'is_not_empty'

    def __str__(self) -> str:
        return str(self.value)