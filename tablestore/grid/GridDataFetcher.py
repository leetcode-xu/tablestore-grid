#!/usr/bin/env python
""" generated source for module GridDataFetcher """
# package: com.aliyun.tablestore.grid
import com.aliyun.tablestore.grid.model.GridDataSet

import com.aliyun.tablestore.grid.model.grid.Range

import java.util.Collection

class GridDataFetcher(object):
    """ generated source for interface GridDataFetcher """
    __metaclass__ = ABCMeta
    # 
    #      * 设置要查询的变量。
    #      * @param variables
    #      * @return
    #      
    @abstractmethod
    def setVariablesToGet(self, variables):
        """ generated source for method setVariablesToGet """

    # 
    #      * 设置要读取的各维度起始点和大小。
    #      * @param origin 各维度起始点。
    #      * @param shape 各维度大小。
    #      * @return
    #      
    @abstractmethod
    def setOriginShape(self, origin, shape):
        """ generated source for method setOriginShape """

    # 
    #      * 获取数据。
    #      * @return
    #      * @throws Exception
    #      
    @abstractmethod
    def fetch(self):
        """ generated source for method fetch """

    @abstractmethod
    def setT(self, t):
        """ generated source for method setT """

    @abstractmethod
    def setTRange(self, tRange):
        """ generated source for method setTRange """

    @abstractmethod
    def setZ(self, z):
        """ generated source for method setZ """

    @abstractmethod
    def setZRange(self, zRange):
        """ generated source for method setZRange """

    @abstractmethod
    def setX(self, x):
        """ generated source for method setX """

    @abstractmethod
    def setXRange(self, xRange):
        """ generated source for method setXRange """

    @abstractmethod
    def setY(self, y):
        """ generated source for method setY """

    @abstractmethod
    def setYRange(self, yRange):
        """ generated source for method setYRange """

