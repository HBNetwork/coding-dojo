from abc import ABC

import pytest

from binary import Byte, adder, multiplier, Word, Tribyte, DoubleWord


class Integer(ABC):
    STORAGE = bytes
    types = {}

    def __init__(self, n):
        self.value = self.STORAGE(n)

    def __add__(self, other):
        return self.factory(adder(self.value, other.value))

    def __eq__(self, other):
        return self.value == other.value

    def __mul__(self, other):
        return self.factory(multiplier(self.value, other.value))

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value!r})'

    @classmethod
    def factory(cls, n):
        for upper_bound, klass in cls.types.items():
            if n < upper_bound:
                break

        return klass(n)

    @classmethod
    def register(cls, upper_bound, klass):
        cls.types[upper_bound] = klass

def Int(n):
    return Integer.factory(n)


class Int8(Integer):
    STORAGE = Byte

class Int16(Integer):
    STORAGE = Word

class Int24(Integer):
    STORAGE = Tribyte

class Int32(Integer):
    STORAGE = DoubleWord

Integer.register(256, Int8)
Integer.register(65536, Int16)
Integer.register(16_777_216, Int24)
Integer.register(4_294_967_296, Int32)


def test_int8():
    assert isinstance(Int8(0), Int8)
    assert isinstance(Int8(255), Int8)
    with pytest.raises(ValueError):
        Int8(256)

    assert Int8(0) + Int8(0) == Int8(0)
    assert Int8(1) + Int8(1) == Int8(2)
    assert Int8(254) + Int8(1) == Int8(255)

    assert Int8(127) * Int8(2) == Int8(254)


def test_int16():
    assert isinstance(Int16(0), Int16)
    assert isinstance(Int16(65535), Int16)
    with pytest.raises(ValueError):
        Int16(65536)

    assert Int16(0) + Int16(0) == Int16(0)
    assert Int16(255) + Int16(1) == Int16(256)

    assert Int16(256) * Int16(2) == Int16(512)


def test_int24():
    assert isinstance(Int24(0), Int24)
    assert isinstance(Int24(16_777_215), Int24)
    with pytest.raises(ValueError):
        Int24(16_777_216)

    assert Int24(0) + Int24(0) == Int24(0)
    assert Int24(65535) + Int24(1) == Int24(65536)

    assert Int24(65536) * Int24(2) == Int24(131_072)


def test_int32():
    assert isinstance(Int32(0), Int32)
    assert isinstance(Int32(4_294_967_295), Int32)
    with pytest.raises(ValueError):
        Int32(4_294_967_296)

    assert Int32(0) + Int32(0) == Int32(0)
    assert Int32(16_777_215) + Int32(1) == Int32(16_777_216)

    assert Int32(16_777_216) * Int32(2) == Int32(33_554_432)


def test_scale_up():
    assert Int8(255) + Int8(1) == Int16(256)
    assert Int8(128) * Int8(2) == Int16(256)

    assert Int16(65535) + Int16(1) == Int24(65536)
    assert Int16(32_768) * Int16(2) == Int24(65536)

    assert Int24(16_777_215) + Int24(1) == Int32(16_777_216)
    assert Int24(8_388_608) * Int24(2) == Int32(16_777_216)


def test_scale_down():
    assert isinstance(Int8(254) + Int8(1), Int8)

    assert isinstance(Int16(254) + Int16(1), Int8)

    assert isinstance(Int24(65534) + Int24(1), Int16)

    assert isinstance(Int32(16_777_214) + Int32(1), Int24)
