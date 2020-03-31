#!/usr/bin/env python
""" generated source for module TableStoreDataFetcher """
# package: com.aliyun.tablestore.grid.core
import com.alicloud.openservices.tablestore.AsyncClientInterface

import com.alicloud.openservices.tablestore.TableStoreCallback

import com.alicloud.openservices.tablestore.model.GetRowRequest

import com.alicloud.openservices.tablestore.model.GetRowResponse

import com.aliyun.tablestore.grid.GridDataFetcher

import com.aliyun.tablestore.grid.model.GetDataParam

import com.aliyun.tablestore.grid.model.GridDataSet

import com.aliyun.tablestore.grid.model.GridDataSetMeta

import com.aliyun.tablestore.grid.model.StoreOptions

import com.aliyun.tablestore.grid.model.grid

import com.aliyun.tablestore.grid.utils.BlockUtil

import java.nio.ByteBuffer

import java.util.ArrayList

import java.util.Collection

import java.util.List

import java.util.Queue

import java.util.concurrent.ConcurrentLinkedQueue

import java.util.concurrent.CountDownLatch

import java.util.concurrent.atomic.AtomicInteger

import com.aliyun.tablestore.grid.consts.Constants.*

# 
#  * not thread-safe
#  
class TableStoreDataFetcher(GridDataFetcher):
    """ generated source for class TableStoreDataFetcher """
    asyncClient = AsyncClientInterface()
    meta = GridDataSetMeta()
    tableName = str()
    dataSizeLimitForFetch = long()
    variables = Collection()
    tRange = Range()
    zRange = Range()
    xRange = Range()
    yRange = Range()

    def __init__(self, asyncClient, tableName, meta, dataSizeLimitForFetch):
        """ generated source for method __init__ """
        super(TableStoreDataFetcher, self).__init__()
        self.asyncClient = asyncClient
        self.tableName = tableName
        self.meta = meta
        self.dataSizeLimitForFetch = dataSizeLimitForFetch
        self.variables = self.meta.getVariables()
        self.tRange = Range(0, self.meta.gettSize())
        self.zRange = Range(0, self.meta.getzSize())
        self.xRange = Range(0, self.meta.getxSize())
        self.yRange = Range(0, self.meta.getySize())

    def setVariablesToGet(self, variables):
        """ generated source for method setVariablesToGet """
        self.variables = variables
        return self

    def setT(self, t):
        """ generated source for method setT """
        return setTRange(Range(t, t + 1))

    def setTRange(self, range):
        """ generated source for method setTRange """
        if range.getStart() < 0 or range.getEnd() > meta.gettSize():
            raise IllegalArgumentException("range invalid")
        self.tRange = range
        return self

    def setZ(self, z):
        """ generated source for method setZ """
        return setZRange(Range(z, z + 1))

    def setZRange(self, range):
        """ generated source for method setZRange """
        if range.getStart() < 0 or range.getEnd() > meta.getzSize():
            raise IllegalArgumentException("range invalid")
        self.zRange = range
        return self

    def setX(self, x):
        """ generated source for method setX """
        return setXRange(Range(x, x + 1))

    def setXRange(self, range):
        """ generated source for method setXRange """
        if range.getStart() < 0 or range.getEnd() > meta.getxSize():
            raise IllegalArgumentException("range invalid")
        self.xRange = range
        return self

    def setY(self, y):
        """ generated source for method setY """
        return setYRange(Range(y, y + 1))

    def setYRange(self, range):
        """ generated source for method setYRange """
        if range.getStart() < 0 or range.getEnd() > meta.getySize():
            raise IllegalArgumentException("range invalid")
        self.yRange = range
        return self

    def setOriginShape(self, origin, shape):
        """ generated source for method setOriginShape """
        if origin.length != 4 or shape.length != 4:
            raise IllegalArgumentException("the length of origin and shape must be 4")
        self.setTRange(Range(origin[0], origin[0] + shape[0]))
        self.setZRange(Range(origin[1], origin[1] + shape[1]))
        self.setXRange(Range(origin[2], origin[2] + shape[2]))
        self.setYRange(Range(origin[3], origin[3] + shape[3]))
        return self

    def getOrigin(self):
        """ generated source for method getOrigin """
        return [None]*

    def getShape(self):
        """ generated source for method getShape """
        return [None]*

    def calcDataSize(self, variableCount):
        """ generated source for method calcDataSize """
        dataSize = variableCount
        return dataSize * self.meta.getDataType().getSize() * self.tRange.getSize() * self.zRange.getSize() * self.xRange.getSize() * self.yRange.getSize()

    def getColumnsToGet(self):
        """ generated source for method getColumnsToGet """
        if not self.meta.getStoreOptions().getStoreType() == StoreOptions.StoreType.SLICE:
            raise IllegalArgumentException("unsupported store type")
        plane = Plane(Range(self.meta.getxSize()), Range(self.meta.getySize()))
        subPlane = Plane(self.xRange, self.yRange)
        if plane == subPlane:
            return None
        columnsToGet = ArrayList()
        points = BlockUtil.calcBlockPointsCanCoverSubPlane(plane, subPlane, self.meta.getStoreOptions().getxSplitCount(), self.meta.getStoreOptions().getySplitCount())
        for point in points:
            columnsToGet.add(String.format(DATA_BLOCK_COL_NAME_FORMAT, point.getX(), point.getY()))
        return columnsToGet

    def addTask(self, counter, buffer_, pos, variable, t, z, latch, exceptions):
        """ generated source for method addTask """
        param = GetDataParam(self.tableName, self.meta.getGridDataSetId(), variable, t, z, self.getColumnsToGet())
        self.asyncClient.getRow(RequestBuilder.buildGetDataRequest(param), TableStoreCallback())

    def fetch(self):
        """ generated source for method fetch """
        totalFetchDataSize = self.calcDataSize(len(self.variables))
        if totalFetchDataSize == 0:
            raise RuntimeException("no data to fetch")
        if totalFetchDataSize > dataSizeLimitForFetch:
            raise RuntimeException("exceed the max data limit for fetch")
        dataSet = GridDataSet(self.meta)
        latch = CountDownLatch(len(self.variables) * self.tRange.getSize() * self.zRange.getSize())
        exceptions = ConcurrentLinkedQueue()
        counter = AtomicInteger()
        taskCount = 0
        for variable in variables:
            dataSet.addVariable(variable, Grid4D(buffer_, self.meta.getDataType(), self.getOrigin(), self.getShape()))
            # 
            #  * not thread-safe
            #  
            while t < tRange.getEnd():
                # 
                #  * not thread-safe
                #  
                # 
                #  * not thread-safe
                #  
                while z < zRange.getEnd():
                    # 
                    #  * not thread-safe
                    #  
                    self.addTask(counter, data, curPos, variable, t, z, latch, exceptions)
                    curPos += xRange.getSize() * yRange.getSize() * meta.getDataType().getSize()
                    taskCount += 1
                    z += 1
                t += 1
        latch.await()
        if not exceptions.isEmpty():
            raise exceptions.peek()
        if counter.get() != taskCount:
            raise RuntimeException("not all task success")
        return dataSet

