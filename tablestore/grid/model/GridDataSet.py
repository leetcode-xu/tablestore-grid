#!/usr/bin/env python
""" generated source for module GridDataSet """
# package: com.aliyun.tablestore.grid.model
import com.aliyun.tablestore.grid.model.grid.Grid4D

import java.util.Map

import java.util.concurrent.ConcurrentHashMap

class GridDataSet(object):
    """ generated source for class GridDataSet """
    meta = GridDataSetMeta()
    variables = Map()

    @overloaded
    def __init__(self, meta):
        """ generated source for method __init__ """
        self.meta = meta
        self.variables = ConcurrentHashMap()

    @__init__.register(object, GridDataSetMeta, Map)
    def __init___0(self, meta, variables):
        """ generated source for method __init___0 """
        self.meta = meta
        self.variables = variables

    def addVariable(self, variable, grid4D):
        """ generated source for method addVariable """
        self.variables.put(variable, grid4D)

    def getVariable(self, variable):
        """ generated source for method getVariable """
        if self.variables == None:
            return None
        return self.variables.get(variable)

    def getVariables(self):
        """ generated source for method getVariables """
        return self.variables

    def getMeta(self):
        """ generated source for method getMeta """
        return self.meta

