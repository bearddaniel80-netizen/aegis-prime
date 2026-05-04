from enum import Enum


class ErrorType(str, Enum):
    ASSERTION = "AssertionError"
    TYPE = "TypeError"
    ATTRIBUTE = "AttributeError"
    EXCEPTION = "Exception"
    OTHER = "Other"


class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class Status(str, Enum):
    OPEN = "open"
    CLOSED = "closed"


class PatternType(str, Enum):
    ASSERT_EQ = "assert_eq"
    ASSERT_NE = "assert_ne"
    ASSERT_GT = "assert_gt"
    ASSERT_LT = "assert_lt"
    ASSERT_IN = "assert_in"
    OTHER = "assert_other"