from nose.tools import *
from illumination.illuminate import illumination

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"
