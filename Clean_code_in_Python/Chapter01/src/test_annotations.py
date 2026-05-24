"""
Clean Code in Python - Chapter 01: Introduction, Tools, and Formatting

Tests for annotations examples
"""
import pytest

from src.annotations import NewPoint, Point, locate

'''
    parametrize làm gì ?
    - Cho phép chạy cùng một test nhiều lần
    - Mỗi lần với bộ dữ liệu khác nhau
'''
@pytest.mark.parametrize(
    "element,expected",
    (
        (locate, {"latitude": float, "longitude": float, "return": Point}),
        (NewPoint, {"lat": float, "long": float}),
    )
)
def test_annotations(element, expected):
    """test the class/function againts its expected annotations"""
    assert getattr(element, "__annotations__") == expected
    
'''
element -> có thể là hàm hoặc class
expected -> dict chưa annotations mong đợi

Dòng assert quan trọng
assert getattr(element, "__annotations__") == expected

Giải thích chi tiết
__annotations__ là gì ?
    Là attribute đặc biệt Python tạo ra khi bạn dùng type hint
    Dạng dict
Ví dụ:
locate.__annotations__
# {'latitude': float, 'longitude': float, 'return': Point}

getattr(element, "__annotations__")
    Lấy attribute __annotations__
    Dùng getattr để:
        Dùng chung cho function và class
        Tránh lỗi style (linters hay khuyên dùng)
'''