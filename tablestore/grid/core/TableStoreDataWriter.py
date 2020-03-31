#!/usr/bin/env python
""" generated source for module TableStoreDataWriter """
# package: com.aliyun.tablestore.grid.core
import com.alicloud.openservices.tablestore.TableStoreWriter

import com.alicloud.openservices.tablestore.model

import com.aliyun.tablestore.grid.GridDataWriter

import com.aliyun.tablestore.grid.model.grid.Grid2D

import com.aliyun.tablestore.grid.model.GridDataSetMeta

import com.aliyun.tablestore.grid.model.StoreOptions

import com.aliyun.tablestore.grid.model.grid.Plane

import com.aliyun.tablestore.grid.utils.BlockUtil

import ucar.ma2.InvalidRangeException

import java.util.ArrayList

import java.util.List

import com.aliyun.tablestore.grid.consts.Constants.*

class TableStoreDataWriter(GridDataWriter):
    """ generated source for class TableStoreDataWriter """
    tableName = str()
    meta = GridDataSetMeta()
    writer = TableStoreWriter()

    def __init__(self, writer, tableName, dataSetMeta):
        """ generated source for method __init__ """
        super(TableStoreDataWriter, self).__init__()
        self.writer = writer
        self.tableName = tableName
        self.meta = dataSetMeta

    def checkDataSize(self, variable, t, z, grid2D):
        """ generated source for method checkDataSize """
        if not self.meta.getVariables().contains(variable):
            raise IllegalArgumentException("The data set dose not include this variable: " + variable)
        if t >= meta.gettSize():
            raise IllegalArgumentException("t must be in range: [0, " + self.meta.gettSize() + ")")
        if z >= meta.getzSize():
            raise IllegalArgumentException("z must be in range: [0, " + self.meta.getzSize() + ")")
        plane = Plane(grid2D.getOrigin(), grid2D.getShape())
        if plane.getxRange().getStart() != 0 or plane.getyRange().getStart() != 0:
            raise IllegalArgumentException("xStart and yStart in grid2D must be 0")
        if plane.getxRange().getSize() != meta.getxSize():
            raise IllegalArgumentException("xSize in grid2D must be equal to gridDataSetMeta's xSize")
        if plane.getyRange().getSize() != meta.getySize():
            raise IllegalArgumentException("ySize in grid2D must be equal to gridDataSetMeta's ySize")

    def splitDataToColumns(self, grid2D):
        """ generated source for method splitDataToColumns """
        columns = ArrayList()
        blocks = BlockUtil.splitGrid2DToBlocks(grid2D, self.meta.getStoreOptions().getxSplitCount(), self.meta.getStoreOptions().getySplitCount())
        for block in blocks:
            columns.add(Column(String.format(DATA_BLOCK_COL_NAME_FORMAT, block.getPlane().getxRange().getStart(), block.getPlane().getyRange().getStart()), ColumnValue.fromBinary(block.getDataAsByteArray())))
        return columns

    def writeToTableStore(self, variable, t, z, columns):
        """ generated source for method writeToTableStore """
        if len(columns) == 0:
            raise IllegalArgumentException("columns are empty")
        builder = PrimaryKeyBuilder.createPrimaryKeyBuilder()
        builder.addPrimaryKeyColumn(GRID_DATA_SET_ID_PK_NAME, PrimaryKeyValue.fromString(self.meta.getGridDataSetId()))
        builder.addPrimaryKeyColumn(VARIABLE_PK_NAME, PrimaryKeyValue.fromString(variable))
        builder.addPrimaryKeyColumn(T_PK_NAME, PrimaryKeyValue.fromLong(t))
        builder.addPrimaryKeyColumn(Z_PK_NAME, PrimaryKeyValue.fromLong(z))
        pk = builder.build()
        rowUpdateChange = RowUpdateChange(self.tableName, pk)
        currentSize = 0
        i = 0
        while i < len(columns):
            if currentSize != 0 and (currentSize + columns.get(i).getDataSize()) > MAX_REQUEST_SIZE:
                self.writer.addRowChange(rowUpdateChange)
                rowUpdateChange = RowUpdateChange(tableName, pk)
                currentSize = 0
            rowUpdateChange.put(columns.get(i))
            currentSize += columns.get(i).getDataSize()
            i += 1
        self.writer.addRowChange(rowUpdateChange)
        self.writer.flush()

    def writeGrid2D(self, variable, t, z, grid2D):
        """ generated source for method writeGrid2D """
        self.checkDataSize(variable, t, z, grid2D)
        if self.meta.getStoreOptions().getStoreType() == StoreOptions.StoreType.SLICE:
            self.writeToTableStore(variable, t, z, columns)
        else:
            raise IllegalArgumentException("unsupported store type")

