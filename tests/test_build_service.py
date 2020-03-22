import pytest
from nanoinject import Container

from .services import NoArguments, SimpleArgument, WithArgument, WithScalarArgument

def test_build_object_without_Arguments():
    c = Container()
    c.add('no_arguments', lambda c: NoArguments())

    assert isinstance(c.get('no_arguments'), NoArguments)

def test_build_object_with_service_arguments():
    c = Container()
    c.add('simple_argument', lambda c: SimpleArgument())
    c.add('with_argument', lambda c: WithArgument(c.get('simple_argument')))

    assert 42 == c.get('with_argument').get_answer()

def test_build_object_with_scalar_and_service_arguments():
    c = Container()
    c.add('simple_argument', lambda c: SimpleArgument())
    c.add('with_scalar_argument', lambda c: WithScalarArgument(c.get('simple_argument'), 'foo'))

    assert 'foo' == c.get('with_scalar_argument').get_scalar_value()

def test_not_shared_is_instantiated_every_time():
    c = Container()
    c.add('simple_argument', lambda c: SimpleArgument()).not_shared()

    a = c.get('simple_argument')
    b = c.get('simple_argument')

    assert a != b