def student(name: str, age: int, score: float, gender: str) -> str:
    return f"有個{age}歲的{gender}學生叫做{name}，他考了{score}分"

print(student("小明", 18, 90, "男"))
# >>有個18歲的男學生叫做小明，他考了90分


# ================================
def student(*, name: str, age: int, score: float, gender: str) -> str:
    return f"有個{age}歲的{gender}學生叫做{name}，他考了{score}分"

print(student("小明", 18, 90, "男"))
# >>TypeError: student() takes 0 positional arguments but 4 were given

print(student(name="小明", age=18, score=90, gender="男"))
# >>有個18歲的男學生叫做小明，他考了90分


# ================================
def student(name: str, age: int, *, score: float, gender: str) -> str:
    return f"有個{age}歲的{gender}學生叫做{name}，他考了{score}分"

print(student("小明", 18, score=90, gender="男"))
# >>有個18歲的男學生叫做小明，他考了90分