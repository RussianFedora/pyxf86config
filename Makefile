# Makefile for source rpm: pyxf86config
# $Id$
NAME := pyxf86config
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
