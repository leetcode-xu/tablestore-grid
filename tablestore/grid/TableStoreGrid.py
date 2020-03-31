#!/usr/bin/env python
""" generated source for module TableStoreGrid """
from functools import wraps
from threading import RLock

def lock_for_object(obj, locks={}):
    return locks.setdefault(id(obj), RLock())

def synchronized(call):
    assert call.__code__.co_varnames[0] in ['self', 'cls']
    @wraps(call)
    def inner(*args, **kwds):
        with lock_for_object(args[0]):
            return call(*args, **kwds)
    return inner

# package: com.aliyun.tablestore.grid
import com.alicloud.openservices.tablestore

import com.alicloud.openservices.tablestore.core.ErrorCode

import com.alicloud.openservices.tablestore.model.GetRowResponse

import com.alicloud.openservices.tablestore.model.Row

import com.alicloud.openservices.tablestore.model.search.CreateSearchIndexRequest

import com.alicloud.openservices.tablestore.model.search.IndexSchema

import com.alicloud.openservices.tablestore.model.search.SearchResponse

import com.alicloud.openservices.tablestore.model.search.query.Query

import com.alicloud.openservices.tablestore.writer.WriterConfig

import com.aliyun.tablestore.grid.core.RequestBuilder

import com.aliyun.tablestore.grid.core.RowParser

import com.aliyun.tablestore.grid.core.TableStoreDataFetcher

import com.aliyun.tablestore.grid.core.TableStoreDataWriter

import com.aliyun.tablestore.grid.model.GridDataSetMeta

import com.aliyun.tablestore.grid.model.QueryGridDataSetResult

import com.aliyun.tablestore.grid.model.QueryParams

import java.util.ArrayList

import java.util.List

import java.util.concurrent.ExecutorService

import java.util.concurrent.Executors

class TableStoreGrid(GridStore):
    """ generated source for class TableStoreGrid """
    config = TableStoreGridConfig()
    asyncClient = AsyncClientInterface()
    writerExecutor = ExecutorService()
    writer = TableStoreWriter()

    def __init__(self, config):
        """ generated source for method __init__ """
        super(TableStoreGrid, self).__init__()
        self.config = config
        self.asyncClient = AsyncClient(config.getTableStoreEndpoint(), config.getAccessId(), config.getAccessKey(), config.getTableStoreInstance())

    def createStore(self):
        """ generated source for method createStore """
        #  create meta table
        try:
            self.asyncClient.createTable(RequestBuilder.buildCreateMetaTableRequest(self.config.getMetaTableName()), None).get()
        except TableStoreException as ex:
            if not ex.getErrorCode() == ErrorCode.OBJECT_ALREADY_EXIST:
                raise ex
        try:
            self.asyncClient.createTable(RequestBuilder.buildCreateDataTableRequest(self.config.getDataTableName()), None).get()
        except TableStoreException as ex:
            if not ex.getErrorCode() == ErrorCode.OBJECT_ALREADY_EXIST:
                raise ex

    def putDataSetMeta(self, meta):
        """ generated source for method putDataSetMeta """
        self.asyncClient.putRow(RequestBuilder.buildPutMetaRequest(self.config.getMetaTableName(), meta), None).get()

    def updateDataSetMeta(self, meta):
        """ generated source for method updateDataSetMeta """
        self.asyncClient.updateRow(RequestBuilder.buildUpdateMetaRequest(self.config.getMetaTableName(), meta), None).get()

    def getDataSetMeta(self, gridDataSetId):
        """ generated source for method getDataSetMeta """
        getRowResponse = self.asyncClient.getRow(RequestBuilder.buildGetMetaRequest(self.config.getMetaTableName(), gridDataSetId), None).get()
        if getRowResponse.getRow() == None:
            return None
        return RowParser.parseMetaFromRow(getRowResponse.getRow())

    def createMetaIndex(self, indexName, indexSchema):
        """ generated source for method createMetaIndex """
        request = CreateSearchIndexRequest()
        request.setTableName(self.config.getMetaTableName())
        request.setIndexName(indexName)
        request.setIndexSchema(indexSchema)
        self.asyncClient.createSearchIndex(request, None).get()

    def queryDataSets(self, indexName, query, queryParams):
        """ generated source for method queryDataSets """
        searchResponse = self.asyncClient.search(RequestBuilder.buildSearchRequest(self.config.getMetaTableName(), indexName, query, queryParams), None).get()
        metaList = ArrayList()
        for row in searchResponse.getRows():
            metaList.add(RowParser.parseMetaFromRow(row))
        result = QueryGridDataSetResult()
        result.setGridDataSetMetas(metaList)
        result.setAllSuccess(searchResponse.isAllSuccess())
        result.setNextToken(searchResponse.getNextToken())
        result.setTotalCount(searchResponse.getTotalCount())
        return result

    def getDataWriter(self, meta):
        """ generated source for method getDataWriter """
        if self.writer == None:
            with lock_for_object(self):
                if self.writer == None:
                    self.writerExecutor = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors())
                    self.writer = DefaultTableStoreWriter(self.asyncClient, config.getDataTableName(), WriterConfig(), None, self.writerExecutor)
        return TableStoreDataWriter(self.writer, self.config.getDataTableName(), meta)

    def getDataFetcher(self, meta):
        """ generated source for method getDataFetcher """
        return TableStoreDataFetcher(self.asyncClient, self.config.getDataTableName(), meta, self.config.getDataSizeLimitForFetch())

    @synchronized
    def close(self):
        """ generated source for method close """
        if self.writer != None:
            self.writer.close()
            self.writerExecutor.shutdown()
        self.asyncClient.shutdown()

