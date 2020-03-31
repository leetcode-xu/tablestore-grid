#!/usr/bin/env python
""" generated source for module BlockUtil """
# package: com.aliyun.tablestore.grid.utils
import com.aliyun.tablestore.grid.model.grid.Grid2D

import com.aliyun.tablestore.grid.model.grid.Plane

import com.aliyun.tablestore.grid.model.grid.Point

import com.aliyun.tablestore.grid.model.grid.Range

import ucar.ma2.Array

import ucar.ma2.DataType

import ucar.ma2.InvalidRangeException

import java.nio.ByteBuffer

import java.util.ArrayList

import java.util.List

class BlockUtil(object):
    """ generated source for class BlockUtil """
    @classmethod
    def splitGrid2DToBlocks(cls, grid2D, xSplitCount, ySplitCount):
        """ generated source for method splitGrid2DToBlocks """
        array = grid2D.toArray()
        blockXSize = (grid2D.getPlane().getxRange().getSize() - 1) / xSplitCount + 1
        blockYSize = (grid2D.getPlane().getyRange().getSize() - 1) / ySplitCount + 1
        result = ArrayList()
        i = 0
        while i < xSplitCount:
            if startX >= grid2D.getPlane().getxRange().getSize():
                break
            while j < ySplitCount:
                if startY >= grid2D.getPlane().getyRange().getSize():
                    break
                result.add(block)
                j += 1
            i += 1
        return result

    @classmethod
    def calcBlockPointsCanCoverSubPlane(cls, plane, subPlane, xSplitCount, ySplitCount):
        """ generated source for method calcBlockPointsCanCoverSubPlane """
        blockXSize = (plane.getxRange().getSize() - 1) / xSplitCount + 1
        blockYSize = (plane.getyRange().getSize() - 1) / ySplitCount + 1
        xBlockIndexRange = Range(subPlane.getxRange().getStart() / blockXSize, (subPlane.getxRange().getEnd() - 1) / blockXSize + 1)
        yBlockIndexRange = Range(subPlane.getyRange().getStart() / blockYSize, (subPlane.getyRange().getEnd() - 1) / blockYSize + 1)
        points = ArrayList()
        xIdx = xBlockIndexRange.getStart()
        while xIdx < xBlockIndexRange.getEnd():
            while yIdx < yBlockIndexRange.getEnd():
                points.add(point)
                yIdx += 1
            xIdx += 1
        return points

    @classmethod
    def buildGrid2DFromBlocks(cls, plane, dataType, blocks, buffer_, pos):
        """ generated source for method buildGrid2DFromBlocks """
        size = plane.getxRange().getSize() * plane.getyRange().getSize() * dataType.getSize()
        if buffer_.length - pos < size:
            raise IllegalArgumentException("buffer not enough")
        count = 0
        for block in blocks:
            while x < Math.min(blockPlane.getxRange().getEnd(), plane.getxRange().getEnd()):
                while y < Math.min(blockPlane.getyRange().getEnd(), plane.getyRange().getEnd()):
                    System.arraycopy(block.getDataAsByteArray(), posInBlock, buffer_, pos + posInData, dataType.getSize())
                    count += dataType.getSize()
                    y += 1
                x += 1
        if count != size:
            raise RuntimeException("the blocks does not contain enough data")
        byteBuffer = ByteBuffer.wrap(buffer_, pos, size)
        return Grid2D(byteBuffer, dataType, plane.getOrigin(), plane.getShape())

