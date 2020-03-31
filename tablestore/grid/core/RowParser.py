#!/usr/bin/env python
""" generated source for module RowParser """
# package: com.aliyun.tablestore.grid.core
import com.alicloud.openservices.tablestore.model.Column

import com.alicloud.openservices.tablestore.model.Row

import com.aliyun.tablestore.grid.model.GridDataSetMeta

import com.aliyun.tablestore.grid.model.StoreOptions

import com.aliyun.tablestore.grid.model.grid.Grid2D

import com.aliyun.tablestore.grid.model.grid.Plane

import com.aliyun.tablestore.grid.model.grid.Range

import com.aliyun.tablestore.grid.utils.BlockUtil

import com.aliyun.tablestore.grid.utils.ValueUtil

import ucar.ma2.DataType

import java.nio.ByteBuffer

import java.util

import com.aliyun.tablestore.grid.consts.Constants.*

class RowParser(object):
    """ generated source for class RowParser """
    @classmethod
    def parseMetaFromRow(cls, row):
        """ generated source for method parseMetaFromRow """
        uniqueKey = row.getPrimaryKey().getPrimaryKeyColumn(GRID_DATA_SET_ID_PK_NAME).getValue().asString()
        dataType = DataType.getType(row.getColumn(DATA_TYPE_COL_NAME).get(0).getValue().asString())
        variables = Arrays.asList(row.getColumn(VARIABLE_LIST_COL_NAME).get(0).getValue().asString().split(","))
        tSize = (row.getColumn(T_SIZE_COL_NAME).get(0).getValue().asLong())
        zSize = (row.getColumn(Z_SIZE_COL_NAME).get(0).getValue().asLong())
        xSize = (row.getColumn(X_SIZE_COL_NAME).get(0).getValue().asLong())
        ySize = (row.getColumn(Y_SIZE_COL_NAME).get(0).getValue().asLong())
        storeType = StoreOptions.StoreType.valueOf(row.getColumn(STORE_TYPE_COL_NAME).get(0).getValue().asString())
        storeOptions = StoreOptions(storeType)
        if storeType == StoreOptions.StoreType.SLICE:
            storeOptions.setxSplitCount((row.getColumn(X_SPLIT_COUNT_COL_NAME).get(0).getValue().asLong()))
            storeOptions.setySplitCount((row.getColumn(Y_SPLIT_COUNT_COL_NAME).get(0).getValue().asLong()))
        attributes = HashMap()
        for column in row.getColumns():
            if not column.__name__.startsWith("_"):
                attributes.put(column.__name__, ValueUtil.toObject(column.getValue()))
        meta = GridDataSetMeta(uniqueKey, dataType, variables, tSize, zSize, xSize, ySize, storeOptions)
        meta.setAttributes(attributes)
        return meta

    @classmethod
    def parseGridFromRow(cls, row, plane, meta, buffer_, pos):
        """ generated source for method parseGridFromRow """
        if not meta.getStoreOptions().getStoreType() == StoreOptions.StoreType.SLICE:
            raise IllegalArgumentException("unsupported store type")
        blockXSize = (meta.getxSize() - 1) / meta.getStoreOptions().getxSplitCount() + 1
        blockYSize = (meta.getySize() - 1) / meta.getStoreOptions().getySplitCount() + 1
        blocks = ArrayList()
        for column in row.getColumns():
            if column.__name__.startsWith(DATA_BLOCK_COL_NAME_PREFIX):
                blocks.add(grid2D)
        grid2D = BlockUtil.buildGrid2DFromBlocks(plane, meta.getDataType(), blocks, buffer_, pos)
        return grid2D

