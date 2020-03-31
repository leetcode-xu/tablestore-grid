#!/usr/bin/env python
""" generated source for module valueUtil """
# package: com.aliyun.tablestore.grid.utils
import com.alicloud.openservices.tablestore.model.ColumnValue

class ValueUtil(object):
    """ generated source for class ValueUtil """
    @classmethod
    def toColumnValue(cls, value):
        """ generated source for method toColumnValue """
        if isinstance(value, (Long, )):
            return ColumnValue.fromLong(Long(value))
        elif isinstance(value, (int, )):
            return ColumnValue.fromLong((int(value)).longValue())
        elif isinstance(value, (Double, )):
            return ColumnValue.fromDouble(Double(value))
        elif isinstance(value, (str, )):
            return ColumnValue.fromString(str(value))
        elif isinstance(value, (bool, )):
            return ColumnValue.fromBoolean(bool(value))
        elif isinstance(value, arrayByte):
            return ColumnValue.fromBinary((value))
        else:
            raise IllegalArgumentException("unsupported type: " + value.__class__)

    @classmethod
    def toObject(cls, value):
        """ generated source for method toObject """
        if value.getType()==INTEGER:
            return value.asLong()
        elif value.getType()==STRING:
            return value.asString()
        elif value.getType()==BOOLEAN:
            return value.asBoolean()
        elif value.getType()==DOUBLE:
            return value.asDouble()
        elif value.getType()==BINARY:
            return value.asBinary()
        else:
            raise RuntimeException("unexpected")

