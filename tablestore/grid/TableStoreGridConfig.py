#!/usr/bin/env python
""" generated source for module TableStoreGridConfig """
# package: com.aliyun.tablestore.grid
class TableStoreGridConfig(object):
    """ generated source for class TableStoreGridConfig """
    tableStoreEndpoint = str()
    accessId = str()
    accessKey = str()
    tableStoreInstance = str()
    metaTableName = str()
    dataTableName = str()
    dataSizeLimitForFetch = 20 * 1024 * 1024

    def getTableStoreEndpoint(self):
        """ generated source for method getTableStoreEndpoint """
        return self.tableStoreEndpoint

    def setTableStoreEndpoint(self, tableStoreEndpoint):
        """ generated source for method setTableStoreEndpoint """
        self.tableStoreEndpoint = tableStoreEndpoint

    def getAccessId(self):
        """ generated source for method getAccessId """
        return self.accessId

    def setAccessId(self, accessId):
        """ generated source for method setAccessId """
        self.accessId = accessId

    def getAccessKey(self):
        """ generated source for method getAccessKey """
        return self.accessKey

    def setAccessKey(self, accessKey):
        """ generated source for method setAccessKey """
        self.accessKey = accessKey

    def getTableStoreInstance(self):
        """ generated source for method getTableStoreInstance """
        return self.tableStoreInstance

    def setTableStoreInstance(self, tableStoreInstance):
        """ generated source for method setTableStoreInstance """
        self.tableStoreInstance = tableStoreInstance

    def getMetaTableName(self):
        """ generated source for method getMetaTableName """
        return self.metaTableName

    def setMetaTableName(self, metaTableName):
        """ generated source for method setMetaTableName """
        self.metaTableName = metaTableName

    def getDataTableName(self):
        """ generated source for method getDataTableName """
        return self.dataTableName

    def setDataTableName(self, dataTableName):
        """ generated source for method setDataTableName """
        self.dataTableName = dataTableName

    def getDataSizeLimitForFetch(self):
        """ generated source for method getDataSizeLimitForFetch """
        return self.dataSizeLimitForFetch

    def setDataSizeLimitForFetch(self, dataSizeLimitForFetch):
        """ generated source for method setDataSizeLimitForFetch """
        self.dataSizeLimitForFetch = dataSizeLimitForFetch

