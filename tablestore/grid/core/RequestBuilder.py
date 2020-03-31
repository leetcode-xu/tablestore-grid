#!/usr/bin/env python
""" generated source for module RequestBuilder """
# package: com.aliyun.tablestore.grid.core
import com.alicloud.openservices.tablestore.core.utils.StringUtils

import com.alicloud.openservices.tablestore.model

import com.alicloud.openservices.tablestore.model.search.SearchQuery

import com.alicloud.openservices.tablestore.model.search.SearchRequest

import com.alicloud.openservices.tablestore.model.search.query.Query

import com.aliyun.tablestore.grid.model.GetDataParam

import com.aliyun.tablestore.grid.model.GridDataSetMeta

import com.aliyun.tablestore.grid.model.QueryParams

import com.aliyun.tablestore.grid.model.StoreOptions

import com.aliyun.tablestore.grid.utils.ValueUtil

import java.util.ArrayList

import java.util.List

import java.util.Map

import com.aliyun.tablestore.grid.consts.Constants.*

class RequestBuilder(object):
    """ generated source for class RequestBuilder """
    @classmethod
    def buildCreateMetaTableRequest(cls, tableName):
        """ generated source for method buildCreateMetaTableRequest """
        meta = TableMeta(tableName)
        meta.addPrimaryKeyColumn(PrimaryKeySchema(GRID_DATA_SET_ID_PK_NAME, PrimaryKeyType.STRING))
        return CreateTableRequest(meta, TableOptions(-1, 1))

    @classmethod
    def buildCreateDataTableRequest(cls, tableName):
        """ generated source for method buildCreateDataTableRequest """
        meta = TableMeta(tableName)
        meta.addPrimaryKeyColumn(PrimaryKeySchema(GRID_DATA_SET_ID_PK_NAME, PrimaryKeyType.STRING))
        meta.addPrimaryKeyColumn(PrimaryKeySchema(VARIABLE_PK_NAME, PrimaryKeyType.STRING))
        meta.addPrimaryKeyColumn(PrimaryKeySchema(T_PK_NAME, PrimaryKeyType.INTEGER))
        meta.addPrimaryKeyColumn(PrimaryKeySchema(Z_PK_NAME, PrimaryKeyType.INTEGER))
        return CreateTableRequest(meta, TableOptions(-1, 1))

    @classmethod
    def buildMetaColumns(cls, meta):
        """ generated source for method buildMetaColumns """
        columns = ArrayList()
        columns.add(Column(DATA_TYPE_COL_NAME, ColumnValue.fromString(meta.getDataType().__str__())))
        columns.add(Column(VARIABLE_LIST_COL_NAME, ColumnValue.fromString(StringUtils.join(",", meta.getVariables()))))
        columns.add(Column(T_SIZE_COL_NAME, ColumnValue.fromLong(meta.gettSize())))
        columns.add(Column(Z_SIZE_COL_NAME, ColumnValue.fromLong(meta.getzSize())))
        columns.add(Column(X_SIZE_COL_NAME, ColumnValue.fromLong(meta.getxSize())))
        columns.add(Column(Y_SIZE_COL_NAME, ColumnValue.fromLong(meta.getySize())))
        columns.add(Column(STORE_TYPE_COL_NAME, ColumnValue.fromString(meta.getStoreOptions().getStoreType().name())))
        if meta.getStoreOptions().getStoreType() == StoreOptions.StoreType.SLICE:
            columns.add(Column(X_SPLIT_COUNT_COL_NAME, ColumnValue.fromLong(meta.getStoreOptions().getxSplitCount())))
            columns.add(Column(Y_SPLIT_COUNT_COL_NAME, ColumnValue.fromLong(meta.getStoreOptions().getySplitCount())))
        if meta.getAttributes() != None:
            for entry in meta.getAttributes().entrySet():
                columns.add(Column(entry.getKey(), ValueUtil.toColumnValue(entry.getValue())))
        return columns

    @classmethod
    def buildPutMetaRequest(cls, metaTableName, meta):
        """ generated source for method buildPutMetaRequest """
        builder = PrimaryKeyBuilder.createPrimaryKeyBuilder()
        builder.addPrimaryKeyColumn(GRID_DATA_SET_ID_PK_NAME, PrimaryKeyValue.fromString(meta.getGridDataSetId()))
        pk = builder.build()
        rowPutChange = RowPutChange(metaTableName, pk)
        rowPutChange.addColumns(cls.buildMetaColumns(meta))
        return PutRowRequest(rowPutChange)

    @classmethod
    def buildUpdateMetaRequest(cls, metaTableName, meta):
        """ generated source for method buildUpdateMetaRequest """
        builder = PrimaryKeyBuilder.createPrimaryKeyBuilder()
        builder.addPrimaryKeyColumn(GRID_DATA_SET_ID_PK_NAME, PrimaryKeyValue.fromString(meta.getGridDataSetId()))
        pk = builder.build()
        rowUpdateChange = RowUpdateChange(metaTableName, pk)
        rowUpdateChange.put(cls.buildMetaColumns(meta))
        return UpdateRowRequest(rowUpdateChange)

    @classmethod
    def buildGetMetaRequest(cls, metaTableName, uniqueKey):
        """ generated source for method buildGetMetaRequest """
        builder = PrimaryKeyBuilder.createPrimaryKeyBuilder()
        builder.addPrimaryKeyColumn(GRID_DATA_SET_ID_PK_NAME, PrimaryKeyValue.fromString(uniqueKey))
        pk = builder.build()
        criteria = SingleRowQueryCriteria(metaTableName)
        criteria.setMaxVersions(1)
        criteria.setPrimaryKey(pk)
        getRowRequest = GetRowRequest()
        getRowRequest.setRowQueryCriteria(criteria)
        return getRowRequest

    @classmethod
    def buildSearchRequest(cls, metaTableName, indexName, query, params):
        """ generated source for method buildSearchRequest """
        searchQuery = SearchQuery()
        searchQuery.setQuery(query)
        if params.getOffset() != None:
            searchQuery.setOffset(params.getOffset())
        if params.getLimit() != None:
            searchQuery.setLimit(params.getLimit())
        if params.getSort() != None:
            searchQuery.setSort(params.getSort())
        if params.getToken() != None:
            searchQuery.setToken(params.getToken())
        searchQuery.setGetTotalCount(params.isGetTotalCount())
        searchRequest = SearchRequest(metaTableName, indexName, searchQuery)
        columnsToGet = SearchRequest.ColumnsToGet()
        columnsToGet.setReturnAll(True)
        searchRequest.setColumnsToGet(columnsToGet)
        return searchRequest

    @classmethod
    def buildGetDataRequest(cls, getDataParam):
        """ generated source for method buildGetDataRequest """
        builder = PrimaryKeyBuilder.createPrimaryKeyBuilder()
        builder.addPrimaryKeyColumn(GRID_DATA_SET_ID_PK_NAME, PrimaryKeyValue.fromString(getDataParam.getDataSetId()))
        builder.addPrimaryKeyColumn(VARIABLE_PK_NAME, PrimaryKeyValue.fromString(getDataParam.getVariable()))
        builder.addPrimaryKeyColumn(T_PK_NAME, PrimaryKeyValue.fromLong(getDataParam.getT()))
        builder.addPrimaryKeyColumn(Z_PK_NAME, PrimaryKeyValue.fromLong(getDataParam.getZ()))
        pk = builder.build()
        criteria = SingleRowQueryCriteria(getDataParam.getDataTableName())
        criteria.setMaxVersions(1)
        criteria.setPrimaryKey(pk)
        if getDataParam.getColumnsToGet() != None:
            criteria.addColumnsToGet(getDataParam.getColumnsToGet())
        return GetRowRequest(criteria)

