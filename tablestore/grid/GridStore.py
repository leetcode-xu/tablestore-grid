#!/usr/bin/env python
""" generated source for module GridStore """
# package: com.aliyun.tablestore.grid
import com.alicloud.openservices.tablestore.model.search.IndexSchema

import com.alicloud.openservices.tablestore.model.search.query.Query

import com.aliyun.tablestore.grid.model.GridDataSetMeta

import com.aliyun.tablestore.grid.model.QueryGridDataSetResult

import com.aliyun.tablestore.grid.model.QueryParams

class GridStore(object):
    """ generated source for interface GridStore """
    __metaclass__ = ABCMeta
    # 
    #      * 创建相关的meta、data表，数据录入前调用。
    #      * @throws Exception
    #      
    @abstractmethod
    def createStore(self):
        """ generated source for method createStore """

    # 
    #      * 写入gridDataSet的meta信息。
    #      * @param meta
    #      * @throws Exception
    #      
    @abstractmethod
    def putDataSetMeta(self, meta):
        """ generated source for method putDataSetMeta """

    # 
    #      * 更新meta信息。
    #      * @param meta
    #      * @throws Exception
    #      
    @abstractmethod
    def updateDataSetMeta(self, meta):
        """ generated source for method updateDataSetMeta """

    # 
    #      * 通过gridDataSetId获取meta。
    #      * @param dataSetId
    #      * @return
    #      * @throws Exception
    #      
    @abstractmethod
    def getDataSetMeta(self, dataSetId):
        """ generated source for method getDataSetMeta """

    # 
    #      * // 创建meta表的多元索引。
    #      * @param indexName
    #      * @param indexSchema
    #      * @throws Exception
    #      
    @abstractmethod
    def createMetaIndex(self, indexName, indexSchema):
        """ generated source for method createMetaIndex """

    # 
    #      * 通过多种查询条件来查询符合条件的数据集。
    #      * @param indexName 多元索引名。
    #      * @param query 查询条件，可以通过QueryBuilder构建。
    #      * @param queryParams 查询相关参数，包括offset、limit、sort等。
    #      * @return
    #      * @throws Exception
    #      
    @abstractmethod
    def queryDataSets(self, indexName, query, queryParams):
        """ generated source for method queryDataSets """

    # 
    #      * 获取GridDataWriter用于写入数据。
    #      * @param meta
    #      * @return
    #      
    @abstractmethod
    def getDataWriter(self, meta):
        """ generated source for method getDataWriter """

    # 
    #      * 获取GridDataFetcher用于读取数据。
    #      * @param meta
    #      * @return
    #      
    @abstractmethod
    def getDataFetcher(self, meta):
        """ generated source for method getDataFetcher """

    # 
    #      * 释放资源。
    #      
    @abstractmethod
    def close(self):
        """ generated source for method close """

