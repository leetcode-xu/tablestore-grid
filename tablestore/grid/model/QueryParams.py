#!/usr/bin/env python
""" generated source for module QueryParams """
# package: com.aliyun.tablestore.grid.model
import com.alicloud.openservices.tablestore.model.search.sort.Sort

class QueryParams(object):
    """ generated source for class QueryParams """
    offset = int()
    limit = int()
    sort = Sort()
    token = []
    getTotalCount = False

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """

    @__init__.register(object, int)
    def __init___0(self, limit):
        """ generated source for method __init___0 """
        self.limit = limit

    @__init__.register(object, int, int)
    def __init___1(self, offset, limit):
        """ generated source for method __init___1 """
        self.offset = offset
        self.limit = limit

    @__init__.register(object, int, int, Sort)
    def __init___2(self, offset, limit, sort):
        """ generated source for method __init___2 """
        self.offset = offset
        self.limit = limit
        self.sort = sort

    @__init__.register(object, byte, int)
    def __init___3(self, token, limit):
        """ generated source for method __init___3 """
        self.token = token
        self.limit = limit

    def getOffset(self):
        """ generated source for method getOffset """
        return self.offset

    def setOffset(self, offset):
        """ generated source for method setOffset """
        self.offset = offset
        return self

    def getLimit(self):
        """ generated source for method getLimit """
        return self.limit

    def setLimit(self, limit):
        """ generated source for method setLimit """
        self.limit = limit
        return self

    def getSort(self):
        """ generated source for method getSort """
        return self.sort

    def setSort(self, sort):
        """ generated source for method setSort """
        self.sort = sort
        return self

    def getToken(self):
        """ generated source for method getToken """
        return self.token

    def setToken(self, token):
        """ generated source for method setToken """
        self.token = token
        return self

    def isGetTotalCount(self):
        """ generated source for method isGetTotalCount """
        return self.getTotalCount

    def setGetTotalCount(self, getTotalCount):
        """ generated source for method setGetTotalCount """
        self.getTotalCount = getTotalCount
        return self

