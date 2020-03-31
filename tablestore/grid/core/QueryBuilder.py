#!/usr/bin/env python
""" generated source for module QueryBuilder """
# package: com.aliyun.tablestore.grid.core
import com.alicloud.openservices.tablestore.model.ColumnValue

import com.alicloud.openservices.tablestore.model.search.query

import com.aliyun.tablestore.grid.utils.ValueUtil

import java.util.ArrayList

import java.util.Arrays

import java.util.List

class QueryBuilder(object):
    """ generated source for class QueryBuilder """
    class Operator:
        """ generated source for enum Operator """
        AND = u'AND'
        OR = u'OR'

    operator = Operator()
    filterQueries = List()
    shouldQueries = List()

    def __init__(self, operator):
        """ generated source for method __init__ """
        self.operator = operator
        if operator==AND:
            self.filterQueries = ArrayList()
        elif operator==OR:
            self.shouldQueries = ArrayList()
        else:
            raise IllegalArgumentException()

    @classmethod
    def or_(cls):
        """ generated source for method or_ """
        return QueryBuilder(cls.Operator.OR)

    @classmethod
    def and_(cls):
        """ generated source for method and_ """
        return QueryBuilder(cls.Operator.AND)

    def equal(self, columnName, *values):
        """ generated source for method equal """
        termsQuery = TermsQuery()
        termsQuery.setFieldName(columnName)
        columnValues = ArrayList()
        for value in values:
            columnValues.add(ValueUtil.toColumnValue(value))
        termsQuery.setTerms(columnValues)
        return query(termsQuery)

    def notEqual(self, columnName, value):
        """ generated source for method notEqual """
        termQuery = TermQuery()
        termQuery.setFieldName(columnName)
        termQuery.setTerm(ValueUtil.toColumnValue(value))
        boolQuery = BoolQuery()
        boolQuery.setMustNotQueries(Arrays.asList(termQuery))
        return query(boolQuery)

    def greaterThan(self, columnName, value):
        """ generated source for method greaterThan """
        rangeQuery = RangeQuery()
        rangeQuery.setFieldName(columnName)
        rangeQuery.greaterThan(ValueUtil.toColumnValue(value))
        return query(rangeQuery)

    def greaterThanEqual(self, columnName, value):
        """ generated source for method greaterThanEqual """
        rangeQuery = RangeQuery()
        rangeQuery.setFieldName(columnName)
        rangeQuery.greaterThanOrEqual(ValueUtil.toColumnValue(value))
        return query(rangeQuery)

    def lessThan(self, columnName, value):
        """ generated source for method lessThan """
        rangeQuery = RangeQuery()
        rangeQuery.setFieldName(columnName)
        rangeQuery.lessThan(ValueUtil.toColumnValue(value))
        return query(rangeQuery)

    def lessThanEqual(self, columnName, value):
        """ generated source for method lessThanEqual """
        rangeQuery = RangeQuery()
        rangeQuery.setFieldName(columnName)
        rangeQuery.lessThanOrEqual(ValueUtil.toColumnValue(value))
        return query(rangeQuery)

    def prefix(self, columnName, prefix):
        """ generated source for method prefix """
        prefixQuery = PrefixQuery()
        prefixQuery.setFieldName(columnName)
        prefixQuery.setPrefix(prefix)
        return query(prefixQuery)

    def query(self, query):
        """ generated source for method query """
        if self.operator==AND:
            self.filterQueries.add(query)
        elif self.operator==OR:
            self.shouldQueries.add(query)
        else:
            raise IllegalArgumentException()
        return self

    def build(self):
        """ generated source for method build """
        if self.operator==AND:
            boolQuery.setFilterQueries(self.filterQueries)
            return boolQuery
        elif self.operator==OR:
            boolQuery.setShouldQueries(self.shouldQueries)
            return boolQuery
        else:
            raise IllegalArgumentException()

