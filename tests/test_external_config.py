import os 
import pytest 
import logging 

from nanoinject import Container, Config 
from .services import NoArguments, SimpleArgument, WithArgument, WithScalarArgument 

def build_and_configure() -> Container: 
    c = Container() 
    config = Config.from_yaml_file(os.path.dirname(__file__) + '/test_services.yaml')
    config.configure(c) 
    return c 
    
def test_build_from_config_without_arguments(): 
    c = build_and_configure() 
    assert isinstance(c.get('no_arguments'), NoArguments) 

def test_build_from_config_with_simple_argument(): 
    c = build_and_configure() 
    assert 42 == c.get('with_argument').get_answer()

def test_build_from_config_without_sharing():
    c = build_and_configure() 
    a = c.get('not_shared')
    b = c.get('not_shared')

    assert a != b

def test_build_from_config_with_scalar_value():
    c = build_and_configure() 

    assert 'it is like magic' == c.get('with_scalar_argument').get_scalar_value()
