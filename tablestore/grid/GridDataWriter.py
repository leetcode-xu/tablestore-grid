#!/usr/bin/env python
""" generated source for module GridDataWriter """
# package: com.aliyun.tablestore.grid
import com.aliyun.tablestore.grid.model.grid.Grid2D

class GridDataWriter(object):
    """ generated source for interface GridDataWriter """
    __metaclass__ = ABCMeta
    # 
    #      * 写入一个二维平面。
    #      * @param variable 变量名。
    #      * @param t 时间维的值。
    #      * @param z 高度维的值。
    #      * @param grid2D 平面数据。
    #      * @throws Exception
    #      
    @abstractmethod
    def writeGrid2D(self, variable, t, z, grid2D):
        """ generated source for method writeGrid2D """

