# SNMP MIB module (MPQOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MPQOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:02 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 ObjectName,
 ObjectSyntax,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "ObjectName",
    "ObjectSyntax",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mpQosMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfqListTable_Object = MibTable
wfqListTable = _WfqListTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 1)
)
if mibBuilder.loadTexts:
    wfqListTable.setStatus("current")
_WfqListEntry_Object = MibTableRow
wfqListEntry = _WfqListEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 1, 1)
)
wfqListEntry.setIndexNames(
    (0, "MPQOS-MIB", "wfqIndex"),
)
if mibBuilder.loadTexts:
    wfqListEntry.setStatus("current")
_WfqIndex_Type = Integer32
_WfqIndex_Object = MibTableColumn
wfqIndex = _WfqIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 1, 1, 1),
    _WfqIndex_Type()
)
wfqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfqIndex.setStatus("current")


class _WfqListNum_Type(Integer32):
    """Custom type wfqListNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WfqListNum_Type.__name__ = "Integer32"
_WfqListNum_Object = MibTableColumn
wfqListNum = _WfqListNum_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 1, 1, 2),
    _WfqListNum_Type()
)
wfqListNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wfqListNum.setStatus("current")


class _WfqCtrlType_Type(Integer32):
    """Custom type wfqCtrlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("limitAndNumber", 1),
          ("weight", 2))
    )


_WfqCtrlType_Type.__name__ = "Integer32"
_WfqCtrlType_Object = MibTableColumn
wfqCtrlType = _WfqCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 1, 1, 3),
    _WfqCtrlType_Type()
)
wfqCtrlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wfqCtrlType.setStatus("current")


class _WfqQueueLimit_Type(Integer32):
    """Custom type wfqQueueLimit based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 96),
    )


_WfqQueueLimit_Type.__name__ = "Integer32"
_WfqQueueLimit_Object = MibTableColumn
wfqQueueLimit = _WfqQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 1, 1, 4),
    _WfqQueueLimit_Type()
)
wfqQueueLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wfqQueueLimit.setStatus("current")


class _WfqQueueNumber_Type(Integer32):
    """Custom type wfqQueueNumber based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 2048),
    )


_WfqQueueNumber_Type.__name__ = "Integer32"
_WfqQueueNumber_Object = MibTableColumn
wfqQueueNumber = _WfqQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 1, 1, 5),
    _WfqQueueNumber_Type()
)
wfqQueueNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wfqQueueNumber.setStatus("current")


class _WfqWeightNumber_Type(Integer32):
    """Custom type wfqWeightNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfqWeightNumber_Type.__name__ = "Integer32"
_WfqWeightNumber_Object = MibTableColumn
wfqWeightNumber = _WfqWeightNumber_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 1, 1, 6),
    _WfqWeightNumber_Type()
)
wfqWeightNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wfqWeightNumber.setStatus("current")


class _WfqWeightType_Type(Integer32):
    """Custom type wfqWeightType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2),
          ("icmp", 3),
          ("igmp", 4))
    )


_WfqWeightType_Type.__name__ = "Integer32"
_WfqWeightType_Object = MibTableColumn
wfqWeightType = _WfqWeightType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 1, 1, 7),
    _WfqWeightType_Type()
)
wfqWeightType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wfqWeightType.setStatus("current")
_WfqSrcIp_Type = IpAddress
_WfqSrcIp_Object = MibTableColumn
wfqSrcIp = _WfqSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 1, 1, 8),
    _WfqSrcIp_Type()
)
wfqSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wfqSrcIp.setStatus("current")


class _WfqSrcPort_Type(Integer32):
    """Custom type wfqSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfqSrcPort_Type.__name__ = "Integer32"
_WfqSrcPort_Object = MibTableColumn
wfqSrcPort = _WfqSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 1, 1, 9),
    _WfqSrcPort_Type()
)
wfqSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wfqSrcPort.setStatus("current")
_WfqDstIp_Type = IpAddress
_WfqDstIp_Object = MibTableColumn
wfqDstIp = _WfqDstIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 1, 1, 10),
    _WfqDstIp_Type()
)
wfqDstIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wfqDstIp.setStatus("current")


class _WfqDstPort_Type(Integer32):
    """Custom type wfqDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfqDstPort_Type.__name__ = "Integer32"
_WfqDstPort_Object = MibTableColumn
wfqDstPort = _WfqDstPort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 1, 1, 11),
    _WfqDstPort_Type()
)
wfqDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wfqDstPort.setStatus("current")
_WfqStatus_Type = RowStatus
_WfqStatus_Object = MibTableColumn
wfqStatus = _WfqStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 1, 1, 12),
    _WfqStatus_Type()
)
wfqStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wfqStatus.setStatus("current")
_PqListTable_Object = MibTable
pqListTable = _PqListTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 2)
)
if mibBuilder.loadTexts:
    pqListTable.setStatus("current")
_PqListEntry_Object = MibTableRow
pqListEntry = _PqListEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 2, 1)
)
pqListEntry.setIndexNames(
    (0, "MPQOS-MIB", "pqIndex"),
)
if mibBuilder.loadTexts:
    pqListEntry.setStatus("current")
_PqIndex_Type = Integer32
_PqIndex_Object = MibTableColumn
pqIndex = _PqIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 2, 1, 1),
    _PqIndex_Type()
)
pqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pqIndex.setStatus("current")


class _PqListNum_Type(Integer32):
    """Custom type pqListNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PqListNum_Type.__name__ = "Integer32"
_PqListNum_Object = MibTableColumn
pqListNum = _PqListNum_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 2, 1, 2),
    _PqListNum_Type()
)
pqListNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pqListNum.setStatus("current")


class _PqCtrlType_Type(Integer32):
    """Custom type pqCtrlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("defaultAndLimit", 1),
          ("interface", 2),
          ("protocol", 3))
    )


_PqCtrlType_Type.__name__ = "Integer32"
_PqCtrlType_Object = MibTableColumn
pqCtrlType = _PqCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 2, 1, 3),
    _PqCtrlType_Type()
)
pqCtrlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pqCtrlType.setStatus("current")


class _PqDefault_Type(Integer32):
    """Custom type pqDefault based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("medium", 2),
          ("normal", 3),
          ("low", 4))
    )


_PqDefault_Type.__name__ = "Integer32"
_PqDefault_Object = MibTableColumn
pqDefault = _PqDefault_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 2, 1, 4),
    _PqDefault_Type()
)
pqDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pqDefault.setStatus("current")
_PqIfIndex_Type = Integer32
_PqIfIndex_Object = MibTableColumn
pqIfIndex = _PqIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 2, 1, 5),
    _PqIfIndex_Type()
)
pqIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pqIfIndex.setStatus("current")


class _PqProtocol_Type(Integer32):
    """Custom type pqProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ip", 1)
    )


_PqProtocol_Type.__name__ = "Integer32"
_PqProtocol_Object = MibTableColumn
pqProtocol = _PqProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 2, 1, 6),
    _PqProtocol_Type()
)
pqProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pqProtocol.setStatus("current")


class _PqPriority_Type(Integer32):
    """Custom type pqPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("medium", 2),
          ("normal", 3),
          ("low", 4))
    )


_PqPriority_Type.__name__ = "Integer32"
_PqPriority_Object = MibTableColumn
pqPriority = _PqPriority_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 2, 1, 7),
    _PqPriority_Type()
)
pqPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pqPriority.setStatus("current")


class _PqProtType_Type(Integer32):
    """Custom type pqProtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fragments", 1),
          ("gt", 2),
          ("list", 3),
          ("lt", 4),
          ("tcp", 5),
          ("udp", 6))
    )


_PqProtType_Type.__name__ = "Integer32"
_PqProtType_Object = MibTableColumn
pqProtType = _PqProtType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 2, 1, 8),
    _PqProtType_Type()
)
pqProtType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pqProtType.setStatus("current")
_PqProtValue_Type = Integer32
_PqProtValue_Object = MibTableColumn
pqProtValue = _PqProtValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 2, 1, 9),
    _PqProtValue_Type()
)
pqProtValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pqProtValue.setStatus("current")


class _PqQueueHigh_Type(Integer32):
    """Custom type pqQueueHigh based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PqQueueHigh_Type.__name__ = "Integer32"
_PqQueueHigh_Object = MibTableColumn
pqQueueHigh = _PqQueueHigh_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 2, 1, 10),
    _PqQueueHigh_Type()
)
pqQueueHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pqQueueHigh.setStatus("current")


class _PqQueueMedium_Type(Integer32):
    """Custom type pqQueueMedium based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PqQueueMedium_Type.__name__ = "Integer32"
_PqQueueMedium_Object = MibTableColumn
pqQueueMedium = _PqQueueMedium_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 2, 1, 11),
    _PqQueueMedium_Type()
)
pqQueueMedium.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pqQueueMedium.setStatus("current")


class _PqQueueNormal_Type(Integer32):
    """Custom type pqQueueNormal based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PqQueueNormal_Type.__name__ = "Integer32"
_PqQueueNormal_Object = MibTableColumn
pqQueueNormal = _PqQueueNormal_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 2, 1, 12),
    _PqQueueNormal_Type()
)
pqQueueNormal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pqQueueNormal.setStatus("current")


class _PqQueueLow_Type(Integer32):
    """Custom type pqQueueLow based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PqQueueLow_Type.__name__ = "Integer32"
_PqQueueLow_Object = MibTableColumn
pqQueueLow = _PqQueueLow_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 2, 1, 13),
    _PqQueueLow_Type()
)
pqQueueLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pqQueueLow.setStatus("current")
_PqStatus_Type = RowStatus
_PqStatus_Object = MibTableColumn
pqStatus = _PqStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 2, 1, 14),
    _PqStatus_Type()
)
pqStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pqStatus.setStatus("current")
_ClassMap_ObjectIdentity = ObjectIdentity
classMap = _ClassMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3)
)
_ClassMapTable_Object = MibTable
classMapTable = _ClassMapTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 1)
)
if mibBuilder.loadTexts:
    classMapTable.setStatus("current")
_ClassMapEntry_Object = MibTableRow
classMapEntry = _ClassMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 1, 1)
)
classMapEntry.setIndexNames(
    (0, "MPQOS-MIB", "classMapClassName"),
)
if mibBuilder.loadTexts:
    classMapEntry.setStatus("current")


class _ClassMapClassName_Type(DisplayString):
    """Custom type classMapClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClassMapClassName_Type.__name__ = "DisplayString"
_ClassMapClassName_Object = MibTableColumn
classMapClassName = _ClassMapClassName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 1, 1, 1),
    _ClassMapClassName_Type()
)
classMapClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapClassName.setStatus("current")


class _ClassMapMatchType_Type(Integer32):
    """Custom type classMapMatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("match-all", 0),
          ("match-any", 1))
    )


_ClassMapMatchType_Type.__name__ = "Integer32"
_ClassMapMatchType_Object = MibTableColumn
classMapMatchType = _ClassMapMatchType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 1, 1, 2),
    _ClassMapMatchType_Type()
)
classMapMatchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapMatchType.setStatus("current")
_ClassMapRowStatus_Type = RowStatus
_ClassMapRowStatus_Object = MibTableColumn
classMapRowStatus = _ClassMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 1, 1, 3),
    _ClassMapRowStatus_Type()
)
classMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapRowStatus.setStatus("current")
_ClassMapAclTable_Object = MibTable
classMapAclTable = _ClassMapAclTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 10)
)
if mibBuilder.loadTexts:
    classMapAclTable.setStatus("current")
_ClassMapAclEntry_Object = MibTableRow
classMapAclEntry = _ClassMapAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 10, 1)
)
classMapAclEntry.setIndexNames(
    (0, "MPQOS-MIB", "classMapAclClassName"),
    (0, "MPQOS-MIB", "classMapAclListName"),
)
if mibBuilder.loadTexts:
    classMapAclEntry.setStatus("current")


class _ClassMapAclClassName_Type(DisplayString):
    """Custom type classMapAclClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClassMapAclClassName_Type.__name__ = "DisplayString"
_ClassMapAclClassName_Object = MibTableColumn
classMapAclClassName = _ClassMapAclClassName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 10, 1, 1),
    _ClassMapAclClassName_Type()
)
classMapAclClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapAclClassName.setStatus("current")


class _ClassMapAclListName_Type(DisplayString):
    """Custom type classMapAclListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClassMapAclListName_Type.__name__ = "DisplayString"
_ClassMapAclListName_Object = MibTableColumn
classMapAclListName = _ClassMapAclListName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 10, 1, 2),
    _ClassMapAclListName_Type()
)
classMapAclListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapAclListName.setStatus("current")
_ClassMapAclRowStatus_Type = RowStatus
_ClassMapAclRowStatus_Object = MibTableColumn
classMapAclRowStatus = _ClassMapAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 10, 1, 3),
    _ClassMapAclRowStatus_Type()
)
classMapAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapAclRowStatus.setStatus("current")
_ClassMapInputIfTable_Object = MibTable
classMapInputIfTable = _ClassMapInputIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 20)
)
if mibBuilder.loadTexts:
    classMapInputIfTable.setStatus("current")
_ClassMapInputIfEntry_Object = MibTableRow
classMapInputIfEntry = _ClassMapInputIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 20, 1)
)
classMapInputIfEntry.setIndexNames(
    (0, "MPQOS-MIB", "classMapInputIfClassName"),
    (0, "MPQOS-MIB", "classMapInputIfName"),
)
if mibBuilder.loadTexts:
    classMapInputIfEntry.setStatus("current")


class _ClassMapInputIfClassName_Type(DisplayString):
    """Custom type classMapInputIfClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClassMapInputIfClassName_Type.__name__ = "DisplayString"
_ClassMapInputIfClassName_Object = MibTableColumn
classMapInputIfClassName = _ClassMapInputIfClassName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 20, 1, 1),
    _ClassMapInputIfClassName_Type()
)
classMapInputIfClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapInputIfClassName.setStatus("current")


class _ClassMapInputIfName_Type(DisplayString):
    """Custom type classMapInputIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_ClassMapInputIfName_Type.__name__ = "DisplayString"
_ClassMapInputIfName_Object = MibTableColumn
classMapInputIfName = _ClassMapInputIfName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 20, 1, 2),
    _ClassMapInputIfName_Type()
)
classMapInputIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapInputIfName.setStatus("current")
_ClassMapInputIfRowStatus_Type = RowStatus
_ClassMapInputIfRowStatus_Object = MibTableColumn
classMapInputIfRowStatus = _ClassMapInputIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 20, 1, 3),
    _ClassMapInputIfRowStatus_Type()
)
classMapInputIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapInputIfRowStatus.setStatus("current")
_ClassMapIpPrecedenceTable_Object = MibTable
classMapIpPrecedenceTable = _ClassMapIpPrecedenceTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 30)
)
if mibBuilder.loadTexts:
    classMapIpPrecedenceTable.setStatus("current")
_ClassMapIpPrecedenceEntry_Object = MibTableRow
classMapIpPrecedenceEntry = _ClassMapIpPrecedenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 30, 1)
)
classMapIpPrecedenceEntry.setIndexNames(
    (0, "MPQOS-MIB", "classMapIpPrecedenceClassName"),
    (0, "MPQOS-MIB", "classMapIpPrecedenceValue"),
)
if mibBuilder.loadTexts:
    classMapIpPrecedenceEntry.setStatus("current")


class _ClassMapIpPrecedenceClassName_Type(DisplayString):
    """Custom type classMapIpPrecedenceClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClassMapIpPrecedenceClassName_Type.__name__ = "DisplayString"
_ClassMapIpPrecedenceClassName_Object = MibTableColumn
classMapIpPrecedenceClassName = _ClassMapIpPrecedenceClassName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 30, 1, 1),
    _ClassMapIpPrecedenceClassName_Type()
)
classMapIpPrecedenceClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapIpPrecedenceClassName.setStatus("current")


class _ClassMapIpPrecedenceValue_Type(Integer32):
    """Custom type classMapIpPrecedenceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ClassMapIpPrecedenceValue_Type.__name__ = "Integer32"
_ClassMapIpPrecedenceValue_Object = MibTableColumn
classMapIpPrecedenceValue = _ClassMapIpPrecedenceValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 30, 1, 2),
    _ClassMapIpPrecedenceValue_Type()
)
classMapIpPrecedenceValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapIpPrecedenceValue.setStatus("current")
_ClassMapIpPrecedenceRowStatus_Type = RowStatus
_ClassMapIpPrecedenceRowStatus_Object = MibTableColumn
classMapIpPrecedenceRowStatus = _ClassMapIpPrecedenceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 30, 1, 3),
    _ClassMapIpPrecedenceRowStatus_Type()
)
classMapIpPrecedenceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapIpPrecedenceRowStatus.setStatus("current")
_ClassMapIpDscpTable_Object = MibTable
classMapIpDscpTable = _ClassMapIpDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 40)
)
if mibBuilder.loadTexts:
    classMapIpDscpTable.setStatus("current")
_ClassMapIpDscpEntry_Object = MibTableRow
classMapIpDscpEntry = _ClassMapIpDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 40, 1)
)
classMapIpDscpEntry.setIndexNames(
    (0, "MPQOS-MIB", "classMapIpDscpClassName"),
    (0, "MPQOS-MIB", "classMapIpDscpValue"),
)
if mibBuilder.loadTexts:
    classMapIpDscpEntry.setStatus("current")


class _ClassMapIpDscpClassName_Type(DisplayString):
    """Custom type classMapIpDscpClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClassMapIpDscpClassName_Type.__name__ = "DisplayString"
_ClassMapIpDscpClassName_Object = MibTableColumn
classMapIpDscpClassName = _ClassMapIpDscpClassName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 40, 1, 1),
    _ClassMapIpDscpClassName_Type()
)
classMapIpDscpClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapIpDscpClassName.setStatus("current")


class _ClassMapIpDscpValue_Type(Integer32):
    """Custom type classMapIpDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ClassMapIpDscpValue_Type.__name__ = "Integer32"
_ClassMapIpDscpValue_Object = MibTableColumn
classMapIpDscpValue = _ClassMapIpDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 40, 1, 2),
    _ClassMapIpDscpValue_Type()
)
classMapIpDscpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapIpDscpValue.setStatus("current")
_ClassMapIpDscpRowStatus_Type = RowStatus
_ClassMapIpDscpRowStatus_Object = MibTableColumn
classMapIpDscpRowStatus = _ClassMapIpDscpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 40, 1, 3),
    _ClassMapIpDscpRowStatus_Type()
)
classMapIpDscpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapIpDscpRowStatus.setStatus("current")
_ClassMapMplsExpTable_Object = MibTable
classMapMplsExpTable = _ClassMapMplsExpTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 50)
)
if mibBuilder.loadTexts:
    classMapMplsExpTable.setStatus("current")
_ClassMapMplsExpEntry_Object = MibTableRow
classMapMplsExpEntry = _ClassMapMplsExpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 50, 1)
)
classMapMplsExpEntry.setIndexNames(
    (0, "MPQOS-MIB", "classMapMplsExpClassName"),
    (0, "MPQOS-MIB", "classMapMplsExpValue"),
)
if mibBuilder.loadTexts:
    classMapMplsExpEntry.setStatus("current")


class _ClassMapMplsExpClassName_Type(DisplayString):
    """Custom type classMapMplsExpClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClassMapMplsExpClassName_Type.__name__ = "DisplayString"
_ClassMapMplsExpClassName_Object = MibTableColumn
classMapMplsExpClassName = _ClassMapMplsExpClassName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 50, 1, 1),
    _ClassMapMplsExpClassName_Type()
)
classMapMplsExpClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapMplsExpClassName.setStatus("current")


class _ClassMapMplsExpValue_Type(Integer32):
    """Custom type classMapMplsExpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ClassMapMplsExpValue_Type.__name__ = "Integer32"
_ClassMapMplsExpValue_Object = MibTableColumn
classMapMplsExpValue = _ClassMapMplsExpValue_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 50, 1, 2),
    _ClassMapMplsExpValue_Type()
)
classMapMplsExpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapMplsExpValue.setStatus("current")
_ClassMapMplsExpRowStatus_Type = RowStatus
_ClassMapMplsExpRowStatus_Object = MibTableColumn
classMapMplsExpRowStatus = _ClassMapMplsExpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 50, 1, 3),
    _ClassMapMplsExpRowStatus_Type()
)
classMapMplsExpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapMplsExpRowStatus.setStatus("current")
_ClassMapProtocolTable_Object = MibTable
classMapProtocolTable = _ClassMapProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 60)
)
if mibBuilder.loadTexts:
    classMapProtocolTable.setStatus("current")
_ClassMapProtocolEntry_Object = MibTableRow
classMapProtocolEntry = _ClassMapProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 60, 1)
)
classMapProtocolEntry.setIndexNames(
    (0, "MPQOS-MIB", "classMapProtocolClassName"),
    (0, "MPQOS-MIB", "classMapProtocolName"),
)
if mibBuilder.loadTexts:
    classMapProtocolEntry.setStatus("current")


class _ClassMapProtocolClassName_Type(DisplayString):
    """Custom type classMapProtocolClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClassMapProtocolClassName_Type.__name__ = "DisplayString"
_ClassMapProtocolClassName_Object = MibTableColumn
classMapProtocolClassName = _ClassMapProtocolClassName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 60, 1, 1),
    _ClassMapProtocolClassName_Type()
)
classMapProtocolClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapProtocolClassName.setStatus("current")


class _ClassMapProtocolName_Type(DisplayString):
    """Custom type classMapProtocolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClassMapProtocolName_Type.__name__ = "DisplayString"
_ClassMapProtocolName_Object = MibTableColumn
classMapProtocolName = _ClassMapProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 60, 1, 2),
    _ClassMapProtocolName_Type()
)
classMapProtocolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapProtocolName.setStatus("current")
_ClassMapProtocolRowStatus_Type = RowStatus
_ClassMapProtocolRowStatus_Object = MibTableColumn
classMapProtocolRowStatus = _ClassMapProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 60, 1, 3),
    _ClassMapProtocolRowStatus_Type()
)
classMapProtocolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapProtocolRowStatus.setStatus("current")
_ClassMapNestTable_Object = MibTable
classMapNestTable = _ClassMapNestTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 70)
)
if mibBuilder.loadTexts:
    classMapNestTable.setStatus("current")
_ClassMapNestEntry_Object = MibTableRow
classMapNestEntry = _ClassMapNestEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 70, 1)
)
classMapNestEntry.setIndexNames(
    (0, "MPQOS-MIB", "classMapNestClassName"),
    (0, "MPQOS-MIB", "classMapNestName"),
)
if mibBuilder.loadTexts:
    classMapNestEntry.setStatus("current")


class _ClassMapNestClassName_Type(DisplayString):
    """Custom type classMapNestClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClassMapNestClassName_Type.__name__ = "DisplayString"
_ClassMapNestClassName_Object = MibTableColumn
classMapNestClassName = _ClassMapNestClassName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 70, 1, 1),
    _ClassMapNestClassName_Type()
)
classMapNestClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapNestClassName.setStatus("current")


class _ClassMapNestName_Type(DisplayString):
    """Custom type classMapNestName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClassMapNestName_Type.__name__ = "DisplayString"
_ClassMapNestName_Object = MibTableColumn
classMapNestName = _ClassMapNestName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 70, 1, 2),
    _ClassMapNestName_Type()
)
classMapNestName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapNestName.setStatus("current")
_ClassMapNestRowStatus_Type = RowStatus
_ClassMapNestRowStatus_Object = MibTableColumn
classMapNestRowStatus = _ClassMapNestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 3, 70, 1, 3),
    _ClassMapNestRowStatus_Type()
)
classMapNestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classMapNestRowStatus.setStatus("current")
_PolicyMap_ObjectIdentity = ObjectIdentity
policyMap = _PolicyMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4)
)
_PolicyMapTable_Object = MibTable
policyMapTable = _PolicyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 10)
)
if mibBuilder.loadTexts:
    policyMapTable.setStatus("current")
_PolicyMapEntry_Object = MibTableRow
policyMapEntry = _PolicyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 10, 1)
)
policyMapEntry.setIndexNames(
    (0, "MPQOS-MIB", "policyMapName"),
)
if mibBuilder.loadTexts:
    policyMapEntry.setStatus("current")


class _PolicyMapName_Type(DisplayString):
    """Custom type policyMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PolicyMapName_Type.__name__ = "DisplayString"
_PolicyMapName_Object = MibTableColumn
policyMapName = _PolicyMapName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 10, 1, 1),
    _PolicyMapName_Type()
)
policyMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyMapName.setStatus("current")
_PolicyMapRowStatus_Type = RowStatus
_PolicyMapRowStatus_Object = MibTableColumn
policyMapRowStatus = _PolicyMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 10, 1, 2),
    _PolicyMapRowStatus_Type()
)
policyMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyMapRowStatus.setStatus("current")
_PolicyClassTable_Object = MibTable
policyClassTable = _PolicyClassTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20)
)
if mibBuilder.loadTexts:
    policyClassTable.setStatus("current")
_PolicyClassEntry_Object = MibTableRow
policyClassEntry = _PolicyClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1)
)
policyClassEntry.setIndexNames(
    (0, "MPQOS-MIB", "policyClassPolicyName"),
    (0, "MPQOS-MIB", "policyClassClassName"),
)
if mibBuilder.loadTexts:
    policyClassEntry.setStatus("current")


class _PolicyClassPolicyName_Type(DisplayString):
    """Custom type policyClassPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PolicyClassPolicyName_Type.__name__ = "DisplayString"
_PolicyClassPolicyName_Object = MibTableColumn
policyClassPolicyName = _PolicyClassPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 1),
    _PolicyClassPolicyName_Type()
)
policyClassPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassPolicyName.setStatus("current")


class _PolicyClassClassName_Type(DisplayString):
    """Custom type policyClassClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PolicyClassClassName_Type.__name__ = "DisplayString"
_PolicyClassClassName_Object = MibTableColumn
policyClassClassName = _PolicyClassClassName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 2),
    _PolicyClassClassName_Type()
)
policyClassClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassClassName.setStatus("current")


class _PolicyClassBandWidthKbps_Type(Integer32):
    """Custom type policyClassBandWidthKbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PolicyClassBandWidthKbps_Type.__name__ = "Integer32"
_PolicyClassBandWidthKbps_Object = MibTableColumn
policyClassBandWidthKbps = _PolicyClassBandWidthKbps_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 3),
    _PolicyClassBandWidthKbps_Type()
)
policyClassBandWidthKbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassBandWidthKbps.setStatus("current")


class _PolicyClassBandWidthTotal_Type(Integer32):
    """Custom type policyClassBandWidthTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PolicyClassBandWidthTotal_Type.__name__ = "Integer32"
_PolicyClassBandWidthTotal_Object = MibTableColumn
policyClassBandWidthTotal = _PolicyClassBandWidthTotal_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 4),
    _PolicyClassBandWidthTotal_Type()
)
policyClassBandWidthTotal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassBandWidthTotal.setStatus("current")


class _PolicyClassBandWidthPercent_Type(Integer32):
    """Custom type policyClassBandWidthPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PolicyClassBandWidthPercent_Type.__name__ = "Integer32"
_PolicyClassBandWidthPercent_Object = MibTableColumn
policyClassBandWidthPercent = _PolicyClassBandWidthPercent_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 5),
    _PolicyClassBandWidthPercent_Type()
)
policyClassBandWidthPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassBandWidthPercent.setStatus("current")


class _PolicyClassPriorityBps_Type(Integer32):
    """Custom type policyClassPriorityBps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_PolicyClassPriorityBps_Type.__name__ = "Integer32"
_PolicyClassPriorityBps_Object = MibTableColumn
policyClassPriorityBps = _PolicyClassPriorityBps_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 6),
    _PolicyClassPriorityBps_Type()
)
policyClassPriorityBps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassPriorityBps.setStatus("current")


class _PolicyClassPriorityPercent_Type(Integer32):
    """Custom type policyClassPriorityPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PolicyClassPriorityPercent_Type.__name__ = "Integer32"
_PolicyClassPriorityPercent_Object = MibTableColumn
policyClassPriorityPercent = _PolicyClassPriorityPercent_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 7),
    _PolicyClassPriorityPercent_Type()
)
policyClassPriorityPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassPriorityPercent.setStatus("current")


class _PolicyClassWredEnable_Type(Integer32):
    """Custom type policyClassWredEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_PolicyClassWredEnable_Type.__name__ = "Integer32"
_PolicyClassWredEnable_Object = MibTableColumn
policyClassWredEnable = _PolicyClassWredEnable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 8),
    _PolicyClassWredEnable_Type()
)
policyClassWredEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassWredEnable.setStatus("current")


class _PolicyClassWredWeight_Type(Integer32):
    """Custom type policyClassWredWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_PolicyClassWredWeight_Type.__name__ = "Integer32"
_PolicyClassWredWeight_Object = MibTableColumn
policyClassWredWeight = _PolicyClassWredWeight_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 9),
    _PolicyClassWredWeight_Type()
)
policyClassWredWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassWredWeight.setStatus("current")


class _PolicyClassWredMinThreshold0_Type(Integer32):
    """Custom type policyClassWredMinThreshold0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PolicyClassWredMinThreshold0_Type.__name__ = "Integer32"
_PolicyClassWredMinThreshold0_Object = MibTableColumn
policyClassWredMinThreshold0 = _PolicyClassWredMinThreshold0_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 10),
    _PolicyClassWredMinThreshold0_Type()
)
policyClassWredMinThreshold0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassWredMinThreshold0.setStatus("current")


class _PolicyClassWredMaxThreshold0_Type(Integer32):
    """Custom type policyClassWredMaxThreshold0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PolicyClassWredMaxThreshold0_Type.__name__ = "Integer32"
_PolicyClassWredMaxThreshold0_Object = MibTableColumn
policyClassWredMaxThreshold0 = _PolicyClassWredMaxThreshold0_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 11),
    _PolicyClassWredMaxThreshold0_Type()
)
policyClassWredMaxThreshold0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassWredMaxThreshold0.setStatus("current")


class _PolicyClassWredMinThreshold1_Type(Integer32):
    """Custom type policyClassWredMinThreshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PolicyClassWredMinThreshold1_Type.__name__ = "Integer32"
_PolicyClassWredMinThreshold1_Object = MibTableColumn
policyClassWredMinThreshold1 = _PolicyClassWredMinThreshold1_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 12),
    _PolicyClassWredMinThreshold1_Type()
)
policyClassWredMinThreshold1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassWredMinThreshold1.setStatus("current")


class _PolicyClassWredMaxThreshold1_Type(Integer32):
    """Custom type policyClassWredMaxThreshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PolicyClassWredMaxThreshold1_Type.__name__ = "Integer32"
_PolicyClassWredMaxThreshold1_Object = MibTableColumn
policyClassWredMaxThreshold1 = _PolicyClassWredMaxThreshold1_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 13),
    _PolicyClassWredMaxThreshold1_Type()
)
policyClassWredMaxThreshold1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassWredMaxThreshold1.setStatus("current")


class _PolicyClassWredMinThreshold2_Type(Integer32):
    """Custom type policyClassWredMinThreshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PolicyClassWredMinThreshold2_Type.__name__ = "Integer32"
_PolicyClassWredMinThreshold2_Object = MibTableColumn
policyClassWredMinThreshold2 = _PolicyClassWredMinThreshold2_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 14),
    _PolicyClassWredMinThreshold2_Type()
)
policyClassWredMinThreshold2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassWredMinThreshold2.setStatus("current")


class _PolicyClassWredMaxThreshold2_Type(Integer32):
    """Custom type policyClassWredMaxThreshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PolicyClassWredMaxThreshold2_Type.__name__ = "Integer32"
_PolicyClassWredMaxThreshold2_Object = MibTableColumn
policyClassWredMaxThreshold2 = _PolicyClassWredMaxThreshold2_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 15),
    _PolicyClassWredMaxThreshold2_Type()
)
policyClassWredMaxThreshold2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassWredMaxThreshold2.setStatus("current")


class _PolicyClassWredMinThreshold3_Type(Integer32):
    """Custom type policyClassWredMinThreshold3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PolicyClassWredMinThreshold3_Type.__name__ = "Integer32"
_PolicyClassWredMinThreshold3_Object = MibTableColumn
policyClassWredMinThreshold3 = _PolicyClassWredMinThreshold3_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 16),
    _PolicyClassWredMinThreshold3_Type()
)
policyClassWredMinThreshold3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassWredMinThreshold3.setStatus("current")


class _PolicyClassWredMaxThreshold3_Type(Integer32):
    """Custom type policyClassWredMaxThreshold3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PolicyClassWredMaxThreshold3_Type.__name__ = "Integer32"
_PolicyClassWredMaxThreshold3_Object = MibTableColumn
policyClassWredMaxThreshold3 = _PolicyClassWredMaxThreshold3_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 17),
    _PolicyClassWredMaxThreshold3_Type()
)
policyClassWredMaxThreshold3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassWredMaxThreshold3.setStatus("current")


class _PolicyClassWredMinThreshold4_Type(Integer32):
    """Custom type policyClassWredMinThreshold4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PolicyClassWredMinThreshold4_Type.__name__ = "Integer32"
_PolicyClassWredMinThreshold4_Object = MibTableColumn
policyClassWredMinThreshold4 = _PolicyClassWredMinThreshold4_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 18),
    _PolicyClassWredMinThreshold4_Type()
)
policyClassWredMinThreshold4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassWredMinThreshold4.setStatus("current")


class _PolicyClassWredMaxThreshold4_Type(Integer32):
    """Custom type policyClassWredMaxThreshold4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PolicyClassWredMaxThreshold4_Type.__name__ = "Integer32"
_PolicyClassWredMaxThreshold4_Object = MibTableColumn
policyClassWredMaxThreshold4 = _PolicyClassWredMaxThreshold4_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 19),
    _PolicyClassWredMaxThreshold4_Type()
)
policyClassWredMaxThreshold4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassWredMaxThreshold4.setStatus("current")


class _PolicyClassWredMinThreshold5_Type(Integer32):
    """Custom type policyClassWredMinThreshold5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PolicyClassWredMinThreshold5_Type.__name__ = "Integer32"
_PolicyClassWredMinThreshold5_Object = MibTableColumn
policyClassWredMinThreshold5 = _PolicyClassWredMinThreshold5_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 20),
    _PolicyClassWredMinThreshold5_Type()
)
policyClassWredMinThreshold5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassWredMinThreshold5.setStatus("current")


class _PolicyClassWredMaxThreshold5_Type(Integer32):
    """Custom type policyClassWredMaxThreshold5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PolicyClassWredMaxThreshold5_Type.__name__ = "Integer32"
_PolicyClassWredMaxThreshold5_Object = MibTableColumn
policyClassWredMaxThreshold5 = _PolicyClassWredMaxThreshold5_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 21),
    _PolicyClassWredMaxThreshold5_Type()
)
policyClassWredMaxThreshold5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassWredMaxThreshold5.setStatus("current")


class _PolicyClassWredMinThreshold6_Type(Integer32):
    """Custom type policyClassWredMinThreshold6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PolicyClassWredMinThreshold6_Type.__name__ = "Integer32"
_PolicyClassWredMinThreshold6_Object = MibTableColumn
policyClassWredMinThreshold6 = _PolicyClassWredMinThreshold6_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 22),
    _PolicyClassWredMinThreshold6_Type()
)
policyClassWredMinThreshold6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassWredMinThreshold6.setStatus("current")


class _PolicyClassWredMaxThreshold6_Type(Integer32):
    """Custom type policyClassWredMaxThreshold6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PolicyClassWredMaxThreshold6_Type.__name__ = "Integer32"
_PolicyClassWredMaxThreshold6_Object = MibTableColumn
policyClassWredMaxThreshold6 = _PolicyClassWredMaxThreshold6_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 23),
    _PolicyClassWredMaxThreshold6_Type()
)
policyClassWredMaxThreshold6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassWredMaxThreshold6.setStatus("current")


class _PolicyClassWredMinThreshold7_Type(Integer32):
    """Custom type policyClassWredMinThreshold7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PolicyClassWredMinThreshold7_Type.__name__ = "Integer32"
_PolicyClassWredMinThreshold7_Object = MibTableColumn
policyClassWredMinThreshold7 = _PolicyClassWredMinThreshold7_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 24),
    _PolicyClassWredMinThreshold7_Type()
)
policyClassWredMinThreshold7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassWredMinThreshold7.setStatus("current")


class _PolicyClassWredMaxThreshold7_Type(Integer32):
    """Custom type policyClassWredMaxThreshold7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PolicyClassWredMaxThreshold7_Type.__name__ = "Integer32"
_PolicyClassWredMaxThreshold7_Object = MibTableColumn
policyClassWredMaxThreshold7 = _PolicyClassWredMaxThreshold7_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 25),
    _PolicyClassWredMaxThreshold7_Type()
)
policyClassWredMaxThreshold7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassWredMaxThreshold7.setStatus("current")


class _PolicyClassSetIpPrecedence_Type(Integer32):
    """Custom type policyClassSetIpPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_PolicyClassSetIpPrecedence_Type.__name__ = "Integer32"
_PolicyClassSetIpPrecedence_Object = MibTableColumn
policyClassSetIpPrecedence = _PolicyClassSetIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 26),
    _PolicyClassSetIpPrecedence_Type()
)
policyClassSetIpPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassSetIpPrecedence.setStatus("current")


class _PolicyClassSetIpDscp_Type(Integer32):
    """Custom type policyClassSetIpDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_PolicyClassSetIpDscp_Type.__name__ = "Integer32"
_PolicyClassSetIpDscp_Object = MibTableColumn
policyClassSetIpDscp = _PolicyClassSetIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 27),
    _PolicyClassSetIpDscp_Type()
)
policyClassSetIpDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassSetIpDscp.setStatus("current")


class _PolicyClassSetMplsImp_Type(Integer32):
    """Custom type policyClassSetMplsImp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_PolicyClassSetMplsImp_Type.__name__ = "Integer32"
_PolicyClassSetMplsImp_Object = MibTableColumn
policyClassSetMplsImp = _PolicyClassSetMplsImp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 28),
    _PolicyClassSetMplsImp_Type()
)
policyClassSetMplsImp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassSetMplsImp.setStatus("current")


class _PolicyClassSetMplsTop_Type(Integer32):
    """Custom type policyClassSetMplsTop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_PolicyClassSetMplsTop_Type.__name__ = "Integer32"
_PolicyClassSetMplsTop_Object = MibTableColumn
policyClassSetMplsTop = _PolicyClassSetMplsTop_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 29),
    _PolicyClassSetMplsTop_Type()
)
policyClassSetMplsTop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassSetMplsTop.setStatus("current")


class _PolicyClassNestName_Type(DisplayString):
    """Custom type policyClassNestName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PolicyClassNestName_Type.__name__ = "DisplayString"
_PolicyClassNestName_Object = MibTableColumn
policyClassNestName = _PolicyClassNestName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 30),
    _PolicyClassNestName_Type()
)
policyClassNestName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassNestName.setStatus("current")
_PolicyClassRowStatus_Type = RowStatus
_PolicyClassRowStatus_Object = MibTableColumn
policyClassRowStatus = _PolicyClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 4, 20, 1, 31),
    _PolicyClassRowStatus_Type()
)
policyClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyClassRowStatus.setStatus("current")
_PriorityList_ObjectIdentity = ObjectIdentity
priorityList = _PriorityList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5)
)
_PriorityListTable_Object = MibTable
priorityListTable = _PriorityListTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 1)
)
if mibBuilder.loadTexts:
    priorityListTable.setStatus("current")
_PriorityListEntry_Object = MibTableRow
priorityListEntry = _PriorityListEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 1, 1)
)
priorityListEntry.setIndexNames(
    (0, "MPQOS-MIB", "priorityListNo"),
)
if mibBuilder.loadTexts:
    priorityListEntry.setStatus("current")


class _PriorityListNo_Type(Integer32):
    """Custom type priorityListNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PriorityListNo_Type.__name__ = "Integer32"
_PriorityListNo_Object = MibTableColumn
priorityListNo = _PriorityListNo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 1, 1, 1),
    _PriorityListNo_Type()
)
priorityListNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priorityListNo.setStatus("current")


class _PriorityListDefQType_Type(Integer32):
    """Custom type priorityListDefQType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("medium", 2),
          ("normal", 3),
          ("low", 4))
    )


_PriorityListDefQType_Type.__name__ = "Integer32"
_PriorityListDefQType_Object = MibTableColumn
priorityListDefQType = _PriorityListDefQType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 1, 1, 2),
    _PriorityListDefQType_Type()
)
priorityListDefQType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priorityListDefQType.setStatus("current")


class _PriorityListQHigh_Type(Integer32):
    """Custom type priorityListQHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_PriorityListQHigh_Type.__name__ = "Integer32"
_PriorityListQHigh_Object = MibTableColumn
priorityListQHigh = _PriorityListQHigh_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 1, 1, 3),
    _PriorityListQHigh_Type()
)
priorityListQHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priorityListQHigh.setStatus("current")


class _PriorityListQMedium_Type(Integer32):
    """Custom type priorityListQMedium based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PriorityListQMedium_Type.__name__ = "Integer32"
_PriorityListQMedium_Object = MibTableColumn
priorityListQMedium = _PriorityListQMedium_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 1, 1, 4),
    _PriorityListQMedium_Type()
)
priorityListQMedium.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priorityListQMedium.setStatus("current")


class _PriorityListQNormal_Type(Integer32):
    """Custom type priorityListQNormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 45000),
    )


_PriorityListQNormal_Type.__name__ = "Integer32"
_PriorityListQNormal_Object = MibTableColumn
priorityListQNormal = _PriorityListQNormal_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 1, 1, 5),
    _PriorityListQNormal_Type()
)
priorityListQNormal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priorityListQNormal.setStatus("current")


class _PriorityListQLow_Type(Integer32):
    """Custom type priorityListQLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PriorityListQLow_Type.__name__ = "Integer32"
_PriorityListQLow_Object = MibTableColumn
priorityListQLow = _PriorityListQLow_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 1, 1, 6),
    _PriorityListQLow_Type()
)
priorityListQLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priorityListQLow.setStatus("current")
_PriorityListWredGrpName_Type = DisplayString
_PriorityListWredGrpName_Object = MibTableColumn
priorityListWredGrpName = _PriorityListWredGrpName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 1, 1, 7),
    _PriorityListWredGrpName_Type()
)
priorityListWredGrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priorityListWredGrpName.setStatus("current")


class _PriorityListDropType_Type(Integer32):
    """Custom type priorityListDropType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("random-detect", 1),
          ("tailed-dropped", 2))
    )


_PriorityListDropType_Type.__name__ = "Integer32"
_PriorityListDropType_Object = MibTableColumn
priorityListDropType = _PriorityListDropType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 1, 1, 8),
    _PriorityListDropType_Type()
)
priorityListDropType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priorityListDropType.setStatus("current")
_PriorityListStatus_Type = RowStatus
_PriorityListStatus_Object = MibTableColumn
priorityListStatus = _PriorityListStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 1, 1, 9),
    _PriorityListStatus_Type()
)
priorityListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priorityListStatus.setStatus("current")
_PriorityListRuleTable_Object = MibTable
priorityListRuleTable = _PriorityListRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 2)
)
if mibBuilder.loadTexts:
    priorityListRuleTable.setStatus("current")
_PriorityListRuleEntry_Object = MibTableRow
priorityListRuleEntry = _PriorityListRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 2, 1)
)
priorityListRuleEntry.setIndexNames(
    (0, "MPQOS-MIB", "priorityListNoIndex"),
    (0, "MPQOS-MIB", "priorityListRuleIndex"),
)
if mibBuilder.loadTexts:
    priorityListRuleEntry.setStatus("current")


class _PriorityListNoIndex_Type(Integer32):
    """Custom type priorityListNoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PriorityListNoIndex_Type.__name__ = "Integer32"
_PriorityListNoIndex_Object = MibTableColumn
priorityListNoIndex = _PriorityListNoIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 2, 1, 1),
    _PriorityListNoIndex_Type()
)
priorityListNoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priorityListNoIndex.setStatus("current")
_PriorityListRuleIndex_Type = Integer32
_PriorityListRuleIndex_Object = MibTableColumn
priorityListRuleIndex = _PriorityListRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 2, 1, 2),
    _PriorityListRuleIndex_Type()
)
priorityListRuleIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priorityListRuleIndex.setStatus("current")


class _PriorityListRuleType_Type(Integer32):
    """Custom type priorityListRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("protocol", 2))
    )


_PriorityListRuleType_Type.__name__ = "Integer32"
_PriorityListRuleType_Object = MibTableColumn
priorityListRuleType = _PriorityListRuleType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 2, 1, 3),
    _PriorityListRuleType_Type()
)
priorityListRuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priorityListRuleType.setStatus("current")


class _PriorityListRulePriType_Type(Integer32):
    """Custom type priorityListRulePriType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("medium", 2),
          ("normal", 3),
          ("low", 4))
    )


_PriorityListRulePriType_Type.__name__ = "Integer32"
_PriorityListRulePriType_Object = MibTableColumn
priorityListRulePriType = _PriorityListRulePriType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 2, 1, 4),
    _PriorityListRulePriType_Type()
)
priorityListRulePriType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priorityListRulePriType.setStatus("current")
_PriorityListforIntIfIndex_Type = Integer32
_PriorityListforIntIfIndex_Object = MibTableColumn
priorityListforIntIfIndex = _PriorityListforIntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 2, 1, 5),
    _PriorityListforIntIfIndex_Type()
)
priorityListforIntIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priorityListforIntIfIndex.setStatus("current")


class _PriorityListProtocolType_Type(Integer32):
    """Custom type priorityListProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("arp", 2),
          ("llx", 3))
    )


_PriorityListProtocolType_Type.__name__ = "Integer32"
_PriorityListProtocolType_Object = MibTableColumn
priorityListProtocolType = _PriorityListProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 2, 1, 6),
    _PriorityListProtocolType_Type()
)
priorityListProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priorityListProtocolType.setStatus("current")


class _PriorityListClassFlag_Type(Integer32):
    """Custom type priorityListClassFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fragments", 1),
          ("gt", 2),
          ("list", 3),
          ("lt", 4),
          ("tcp", 5),
          ("udp", 6))
    )


_PriorityListClassFlag_Type.__name__ = "Integer32"
_PriorityListClassFlag_Object = MibTableColumn
priorityListClassFlag = _PriorityListClassFlag_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 2, 1, 7),
    _PriorityListClassFlag_Type()
)
priorityListClassFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priorityListClassFlag.setStatus("current")


class _PriorityListGtSize_Type(Integer32):
    """Custom type priorityListGtSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PriorityListGtSize_Type.__name__ = "Integer32"
_PriorityListGtSize_Object = MibTableColumn
priorityListGtSize = _PriorityListGtSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 2, 1, 8),
    _PriorityListGtSize_Type()
)
priorityListGtSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priorityListGtSize.setStatus("current")


class _PriorityListLtSize_Type(Integer32):
    """Custom type priorityListLtSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PriorityListLtSize_Type.__name__ = "Integer32"
_PriorityListLtSize_Object = MibTableColumn
priorityListLtSize = _PriorityListLtSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 2, 1, 9),
    _PriorityListLtSize_Type()
)
priorityListLtSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priorityListLtSize.setStatus("current")


class _PriorityListAccListNo_Type(Integer32):
    """Custom type priorityListAccListNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_PriorityListAccListNo_Type.__name__ = "Integer32"
_PriorityListAccListNo_Object = MibTableColumn
priorityListAccListNo = _PriorityListAccListNo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 2, 1, 10),
    _PriorityListAccListNo_Type()
)
priorityListAccListNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priorityListAccListNo.setStatus("current")


class _PriorityListTCPPort_Type(Integer32):
    """Custom type priorityListTCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PriorityListTCPPort_Type.__name__ = "Integer32"
_PriorityListTCPPort_Object = MibTableColumn
priorityListTCPPort = _PriorityListTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 2, 1, 11),
    _PriorityListTCPPort_Type()
)
priorityListTCPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priorityListTCPPort.setStatus("current")


class _PriorityListUDPPort_Type(Integer32):
    """Custom type priorityListUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PriorityListUDPPort_Type.__name__ = "Integer32"
_PriorityListUDPPort_Object = MibTableColumn
priorityListUDPPort = _PriorityListUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 2, 1, 12),
    _PriorityListUDPPort_Type()
)
priorityListUDPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priorityListUDPPort.setStatus("current")
_PriorityListRuleStatus_Type = RowStatus
_PriorityListRuleStatus_Object = MibTableColumn
priorityListRuleStatus = _PriorityListRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 5, 2, 1, 13),
    _PriorityListRuleStatus_Type()
)
priorityListRuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    priorityListRuleStatus.setStatus("current")
_CustomList_ObjectIdentity = ObjectIdentity
customList = _CustomList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6)
)
_CustomListTable_Object = MibTable
customListTable = _CustomListTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 1)
)
if mibBuilder.loadTexts:
    customListTable.setStatus("current")
_CustomListEntry_Object = MibTableRow
customListEntry = _CustomListEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 1, 1)
)
customListEntry.setIndexNames(
    (0, "MPQOS-MIB", "customListNo"),
)
if mibBuilder.loadTexts:
    customListEntry.setStatus("current")


class _CustomListNo_Type(Integer32):
    """Custom type customListNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CustomListNo_Type.__name__ = "Integer32"
_CustomListNo_Object = MibTableColumn
customListNo = _CustomListNo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 1, 1, 1),
    _CustomListNo_Type()
)
customListNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListNo.setStatus("current")


class _CustomListDefNo_Type(Integer32):
    """Custom type customListDefNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CustomListDefNo_Type.__name__ = "Integer32"
_CustomListDefNo_Object = MibTableColumn
customListDefNo = _CustomListDefNo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 1, 1, 2),
    _CustomListDefNo_Type()
)
customListDefNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListDefNo.setStatus("current")
_CustomListWredName_Type = DisplayString
_CustomListWredName_Object = MibTableColumn
customListWredName = _CustomListWredName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 1, 1, 3),
    _CustomListWredName_Type()
)
customListWredName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListWredName.setStatus("current")


class _CustomListDropType_Type(Integer32):
    """Custom type customListDropType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("random-detect", 1),
          ("tailed-dropped", 2))
    )


_CustomListDropType_Type.__name__ = "Integer32"
_CustomListDropType_Object = MibTableColumn
customListDropType = _CustomListDropType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 1, 1, 4),
    _CustomListDropType_Type()
)
customListDropType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListDropType.setStatus("current")
_CustomListStatus_Type = RowStatus
_CustomListStatus_Object = MibTableColumn
customListStatus = _CustomListStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 1, 1, 5),
    _CustomListStatus_Type()
)
customListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListStatus.setStatus("current")
_CustomListRuleTable_Object = MibTable
customListRuleTable = _CustomListRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2)
)
if mibBuilder.loadTexts:
    customListRuleTable.setStatus("current")
_CustomListRuleEntry_Object = MibTableRow
customListRuleEntry = _CustomListRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1)
)
customListRuleEntry.setIndexNames(
    (0, "MPQOS-MIB", "customListNoIndex"),
    (0, "MPQOS-MIB", "customListIndex"),
)
if mibBuilder.loadTexts:
    customListRuleEntry.setStatus("current")


class _CustomListNoIndex_Type(Integer32):
    """Custom type customListNoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CustomListNoIndex_Type.__name__ = "Integer32"
_CustomListNoIndex_Object = MibTableColumn
customListNoIndex = _CustomListNoIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 1),
    _CustomListNoIndex_Type()
)
customListNoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customListNoIndex.setStatus("current")
_CustomListIndex_Type = Integer32
_CustomListIndex_Object = MibTableColumn
customListIndex = _CustomListIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 2),
    _CustomListIndex_Type()
)
customListIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListIndex.setStatus("current")


class _CustomListICMP_Type(Integer32):
    """Custom type customListICMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_CustomListICMP_Type.__name__ = "Integer32"
_CustomListICMP_Object = MibTableColumn
customListICMP = _CustomListICMP_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 3),
    _CustomListICMP_Type()
)
customListICMP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListICMP.setStatus("current")


class _CustomListIGMP_Type(Integer32):
    """Custom type customListIGMP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_CustomListIGMP_Type.__name__ = "Integer32"
_CustomListIGMP_Object = MibTableColumn
customListIGMP = _CustomListIGMP_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 4),
    _CustomListIGMP_Type()
)
customListIGMP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListIGMP.setStatus("current")


class _CustomListQNo_Type(Integer32):
    """Custom type customListQNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CustomListQNo_Type.__name__ = "Integer32"
_CustomListQNo_Object = MibTableColumn
customListQNo = _CustomListQNo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 5),
    _CustomListQNo_Type()
)
customListQNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListQNo.setStatus("current")


class _CustomListFragPktQNo_Type(Integer32):
    """Custom type customListFragPktQNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CustomListFragPktQNo_Type.__name__ = "Integer32"
_CustomListFragPktQNo_Object = MibTableColumn
customListFragPktQNo = _CustomListFragPktQNo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 6),
    _CustomListFragPktQNo_Type()
)
customListFragPktQNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListFragPktQNo.setStatus("current")


class _CustomListPktEtSize_Type(Integer32):
    """Custom type customListPktEtSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1500),
    )


_CustomListPktEtSize_Type.__name__ = "Integer32"
_CustomListPktEtSize_Object = MibTableColumn
customListPktEtSize = _CustomListPktEtSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 7),
    _CustomListPktEtSize_Type()
)
customListPktEtSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListPktEtSize.setStatus("current")


class _CustomListPktGtSize_Type(Integer32):
    """Custom type customListPktGtSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1500),
    )


_CustomListPktGtSize_Type.__name__ = "Integer32"
_CustomListPktGtSize_Object = MibTableColumn
customListPktGtSize = _CustomListPktGtSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 8),
    _CustomListPktGtSize_Type()
)
customListPktGtSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListPktGtSize.setStatus("current")


class _CustomListPktLtSize_Type(Integer32):
    """Custom type customListPktLtSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1500),
    )


_CustomListPktLtSize_Type.__name__ = "Integer32"
_CustomListPktLtSize_Object = MibTableColumn
customListPktLtSize = _CustomListPktLtSize_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 9),
    _CustomListPktLtSize_Type()
)
customListPktLtSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListPktLtSize.setStatus("current")
_CustomListIpSrcAddr_Type = IpAddress
_CustomListIpSrcAddr_Object = MibTableColumn
customListIpSrcAddr = _CustomListIpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 10),
    _CustomListIpSrcAddr_Type()
)
customListIpSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListIpSrcAddr.setStatus("current")
_CustomListIpSrcAddrMask_Type = IpAddress
_CustomListIpSrcAddrMask_Object = MibTableColumn
customListIpSrcAddrMask = _CustomListIpSrcAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 11),
    _CustomListIpSrcAddrMask_Type()
)
customListIpSrcAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListIpSrcAddrMask.setStatus("current")
_CustomListIpDestAddr_Type = IpAddress
_CustomListIpDestAddr_Object = MibTableColumn
customListIpDestAddr = _CustomListIpDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 12),
    _CustomListIpDestAddr_Type()
)
customListIpDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListIpDestAddr.setStatus("current")
_CustomListIpDestAddrMask_Type = IpAddress
_CustomListIpDestAddrMask_Object = MibTableColumn
customListIpDestAddrMask = _CustomListIpDestAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 13),
    _CustomListIpDestAddrMask_Type()
)
customListIpDestAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListIpDestAddrMask.setStatus("current")


class _CustomListAccListNo_Type(Integer32):
    """Custom type customListAccListNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_CustomListAccListNo_Type.__name__ = "Integer32"
_CustomListAccListNo_Object = MibTableColumn
customListAccListNo = _CustomListAccListNo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 14),
    _CustomListAccListNo_Type()
)
customListAccListNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListAccListNo.setStatus("current")


class _CustomListQByteCount_Type(Integer32):
    """Custom type customListQByteCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CustomListQByteCount_Type.__name__ = "Integer32"
_CustomListQByteCount_Object = MibTableColumn
customListQByteCount = _CustomListQByteCount_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 15),
    _CustomListQByteCount_Type()
)
customListQByteCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListQByteCount.setStatus("current")


class _CustomListQLimit_Type(Integer32):
    """Custom type customListQLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CustomListQLimit_Type.__name__ = "Integer32"
_CustomListQLimit_Object = MibTableColumn
customListQLimit = _CustomListQLimit_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 16),
    _CustomListQLimit_Type()
)
customListQLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListQLimit.setStatus("current")
_CustomListTCPSrcAddr_Type = IpAddress
_CustomListTCPSrcAddr_Object = MibTableColumn
customListTCPSrcAddr = _CustomListTCPSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 17),
    _CustomListTCPSrcAddr_Type()
)
customListTCPSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListTCPSrcAddr.setStatus("current")
_CustomListTCPSrcAddrMask_Type = IpAddress
_CustomListTCPSrcAddrMask_Object = MibTableColumn
customListTCPSrcAddrMask = _CustomListTCPSrcAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 18),
    _CustomListTCPSrcAddrMask_Type()
)
customListTCPSrcAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListTCPSrcAddrMask.setStatus("current")


class _CustomListTCPSrcPort_Type(Integer32):
    """Custom type customListTCPSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CustomListTCPSrcPort_Type.__name__ = "Integer32"
_CustomListTCPSrcPort_Object = MibTableColumn
customListTCPSrcPort = _CustomListTCPSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 19),
    _CustomListTCPSrcPort_Type()
)
customListTCPSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListTCPSrcPort.setStatus("current")
_CustomListTCPDestAddr_Type = IpAddress
_CustomListTCPDestAddr_Object = MibTableColumn
customListTCPDestAddr = _CustomListTCPDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 20),
    _CustomListTCPDestAddr_Type()
)
customListTCPDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListTCPDestAddr.setStatus("current")
_CustomListTCPDestAddrMask_Type = IpAddress
_CustomListTCPDestAddrMask_Object = MibTableColumn
customListTCPDestAddrMask = _CustomListTCPDestAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 21),
    _CustomListTCPDestAddrMask_Type()
)
customListTCPDestAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListTCPDestAddrMask.setStatus("current")


class _CustomListTCPDestPort_Type(Integer32):
    """Custom type customListTCPDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CustomListTCPDestPort_Type.__name__ = "Integer32"
_CustomListTCPDestPort_Object = MibTableColumn
customListTCPDestPort = _CustomListTCPDestPort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 22),
    _CustomListTCPDestPort_Type()
)
customListTCPDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListTCPDestPort.setStatus("current")
_CustomListUDPSrcAddr_Type = IpAddress
_CustomListUDPSrcAddr_Object = MibTableColumn
customListUDPSrcAddr = _CustomListUDPSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 23),
    _CustomListUDPSrcAddr_Type()
)
customListUDPSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListUDPSrcAddr.setStatus("current")
_CustomListUDPSrcAddrMask_Type = IpAddress
_CustomListUDPSrcAddrMask_Object = MibTableColumn
customListUDPSrcAddrMask = _CustomListUDPSrcAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 24),
    _CustomListUDPSrcAddrMask_Type()
)
customListUDPSrcAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListUDPSrcAddrMask.setStatus("current")


class _CustomListUDPSrcPort_Type(Integer32):
    """Custom type customListUDPSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CustomListUDPSrcPort_Type.__name__ = "Integer32"
_CustomListUDPSrcPort_Object = MibTableColumn
customListUDPSrcPort = _CustomListUDPSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 25),
    _CustomListUDPSrcPort_Type()
)
customListUDPSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListUDPSrcPort.setStatus("current")
_CustomListUDPDestAddr_Type = IpAddress
_CustomListUDPDestAddr_Object = MibTableColumn
customListUDPDestAddr = _CustomListUDPDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 26),
    _CustomListUDPDestAddr_Type()
)
customListUDPDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListUDPDestAddr.setStatus("current")
_CustomListUDPDestAddrMask_Type = IpAddress
_CustomListUDPDestAddrMask_Object = MibTableColumn
customListUDPDestAddrMask = _CustomListUDPDestAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 27),
    _CustomListUDPDestAddrMask_Type()
)
customListUDPDestAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListUDPDestAddrMask.setStatus("current")


class _CustomListUDPDestPort_Type(Integer32):
    """Custom type customListUDPDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CustomListUDPDestPort_Type.__name__ = "Integer32"
_CustomListUDPDestPort_Object = MibTableColumn
customListUDPDestPort = _CustomListUDPDestPort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 28),
    _CustomListUDPDestPort_Type()
)
customListUDPDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListUDPDestPort.setStatus("current")
_CustomIntListIfIndex_Type = Integer32
_CustomIntListIfIndex_Object = MibTableColumn
customIntListIfIndex = _CustomIntListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 29),
    _CustomIntListIfIndex_Type()
)
customIntListIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customIntListIfIndex.setStatus("current")
_CustomListRuleStatus_Type = RowStatus
_CustomListRuleStatus_Object = MibTableColumn
customListRuleStatus = _CustomListRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 6, 2, 1, 30),
    _CustomListRuleStatus_Type()
)
customListRuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customListRuleStatus.setStatus("current")
_WredGroup_ObjectIdentity = ObjectIdentity
wredGroup = _WredGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7)
)
_WredGrpTable_Object = MibTable
wredGrpTable = _WredGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 1)
)
if mibBuilder.loadTexts:
    wredGrpTable.setStatus("current")
_WredGrpEntry_Object = MibTableRow
wredGrpEntry = _WredGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 1, 1)
)
wredGrpEntry.setIndexNames(
    (0, "MPQOS-MIB", "wredGrpName"),
)
if mibBuilder.loadTexts:
    wredGrpEntry.setStatus("current")
_WredGrpName_Type = DisplayString
_WredGrpName_Object = MibTableColumn
wredGrpName = _WredGrpName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 1, 1, 1),
    _WredGrpName_Type()
)
wredGrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wredGrpName.setStatus("current")
_WredGrpExpWeight_Type = Integer32
_WredGrpExpWeight_Object = MibTableColumn
wredGrpExpWeight = _WredGrpExpWeight_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 1, 1, 2),
    _WredGrpExpWeight_Type()
)
wredGrpExpWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wredGrpExpWeight.setStatus("current")
_WredGrpStatus_Type = RowStatus
_WredGrpStatus_Object = MibTableColumn
wredGrpStatus = _WredGrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 1, 1, 3),
    _WredGrpStatus_Type()
)
wredGrpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wredGrpStatus.setStatus("current")
_WredGrpPreTable_Object = MibTable
wredGrpPreTable = _WredGrpPreTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 2)
)
if mibBuilder.loadTexts:
    wredGrpPreTable.setStatus("current")
_WredGrpPreEntry_Object = MibTableRow
wredGrpPreEntry = _WredGrpPreEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 2, 1)
)
wredGrpPreEntry.setIndexNames(
    (0, "MPQOS-MIB", "wredGrpPreName"),
    (0, "MPQOS-MIB", "wredGrpPreNo"),
)
if mibBuilder.loadTexts:
    wredGrpPreEntry.setStatus("current")
_WredGrpPreName_Type = DisplayString
_WredGrpPreName_Object = MibTableColumn
wredGrpPreName = _WredGrpPreName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 2, 1, 1),
    _WredGrpPreName_Type()
)
wredGrpPreName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wredGrpPreName.setStatus("current")


class _WredGrpPreNo_Type(Integer32):
    """Custom type wredGrpPreNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WredGrpPreNo_Type.__name__ = "Integer32"
_WredGrpPreNo_Object = MibTableColumn
wredGrpPreNo = _WredGrpPreNo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 2, 1, 2),
    _WredGrpPreNo_Type()
)
wredGrpPreNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wredGrpPreNo.setStatus("current")


class _WredGrpPreMinBytes_Type(Integer32):
    """Custom type wredGrpPreMinBytes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WredGrpPreMinBytes_Type.__name__ = "Integer32"
_WredGrpPreMinBytes_Object = MibTableColumn
wredGrpPreMinBytes = _WredGrpPreMinBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 2, 1, 3),
    _WredGrpPreMinBytes_Type()
)
wredGrpPreMinBytes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wredGrpPreMinBytes.setStatus("current")


class _WredGrpPreMaxBytes_Type(Integer32):
    """Custom type wredGrpPreMaxBytes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WredGrpPreMaxBytes_Type.__name__ = "Integer32"
_WredGrpPreMaxBytes_Object = MibTableColumn
wredGrpPreMaxBytes = _WredGrpPreMaxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 2, 1, 4),
    _WredGrpPreMaxBytes_Type()
)
wredGrpPreMaxBytes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wredGrpPreMaxBytes.setStatus("current")


class _WredGrpPreDenominator_Type(Integer32):
    """Custom type wredGrpPreDenominator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WredGrpPreDenominator_Type.__name__ = "Integer32"
_WredGrpPreDenominator_Object = MibTableColumn
wredGrpPreDenominator = _WredGrpPreDenominator_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 2, 1, 5),
    _WredGrpPreDenominator_Type()
)
wredGrpPreDenominator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wredGrpPreDenominator.setStatus("current")
_WredGrpPreRandomDropsBytes_Type = Integer32
_WredGrpPreRandomDropsBytes_Object = MibTableColumn
wredGrpPreRandomDropsBytes = _WredGrpPreRandomDropsBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 2, 1, 6),
    _WredGrpPreRandomDropsBytes_Type()
)
wredGrpPreRandomDropsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wredGrpPreRandomDropsBytes.setStatus("current")
_WredGrpPreTailDropsBytes_Type = Integer32
_WredGrpPreTailDropsBytes_Object = MibTableColumn
wredGrpPreTailDropsBytes = _WredGrpPreTailDropsBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 2, 1, 7),
    _WredGrpPreTailDropsBytes_Type()
)
wredGrpPreTailDropsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wredGrpPreTailDropsBytes.setStatus("current")
_WredGrpPreStatus_Type = RowStatus
_WredGrpPreStatus_Object = MibTableColumn
wredGrpPreStatus = _WredGrpPreStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 2, 1, 8),
    _WredGrpPreStatus_Type()
)
wredGrpPreStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wredGrpPreStatus.setStatus("current")
_IfWredTable_Object = MibTable
ifWredTable = _IfWredTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 3)
)
if mibBuilder.loadTexts:
    ifWredTable.setStatus("current")
_IfWredEntry_Object = MibTableRow
ifWredEntry = _IfWredEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 3, 1)
)
ifWredEntry.setIndexNames(
    (0, "MPQOS-MIB", "ifWredIfIndex"),
)
if mibBuilder.loadTexts:
    ifWredEntry.setStatus("current")
_IfWredIfIndex_Type = Integer32
_IfWredIfIndex_Object = MibTableColumn
ifWredIfIndex = _IfWredIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 3, 1, 1),
    _IfWredIfIndex_Type()
)
ifWredIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifWredIfIndex.setStatus("current")


class _IfWredExpWeight_Type(Integer32):
    """Custom type ifWredExpWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_IfWredExpWeight_Type.__name__ = "Integer32"
_IfWredExpWeight_Object = MibTableColumn
ifWredExpWeight = _IfWredExpWeight_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 3, 1, 2),
    _IfWredExpWeight_Type()
)
ifWredExpWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifWredExpWeight.setStatus("current")
_IfWredStatus_Type = RowStatus
_IfWredStatus_Object = MibTableColumn
ifWredStatus = _IfWredStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 3, 1, 3),
    _IfWredStatus_Type()
)
ifWredStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifWredStatus.setStatus("current")
_IfWredRuleTable_Object = MibTable
ifWredRuleTable = _IfWredRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 4)
)
if mibBuilder.loadTexts:
    ifWredRuleTable.setStatus("current")
_IfWredRuleEntry_Object = MibTableRow
ifWredRuleEntry = _IfWredRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 4, 1)
)
ifWredRuleEntry.setIndexNames(
    (0, "MPQOS-MIB", "ifWredRuleIfIndex"),
    (0, "MPQOS-MIB", "ifWredPreNo"),
)
if mibBuilder.loadTexts:
    ifWredRuleEntry.setStatus("current")
_IfWredRuleIfIndex_Type = Integer32
_IfWredRuleIfIndex_Object = MibTableColumn
ifWredRuleIfIndex = _IfWredRuleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 4, 1, 1),
    _IfWredRuleIfIndex_Type()
)
ifWredRuleIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifWredRuleIfIndex.setStatus("current")


class _IfWredPreNo_Type(Integer32):
    """Custom type ifWredPreNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_IfWredPreNo_Type.__name__ = "Integer32"
_IfWredPreNo_Object = MibTableColumn
ifWredPreNo = _IfWredPreNo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 4, 1, 2),
    _IfWredPreNo_Type()
)
ifWredPreNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifWredPreNo.setStatus("current")


class _IfWredPreMinBytes_Type(Integer32):
    """Custom type ifWredPreMinBytes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535),
    )


_IfWredPreMinBytes_Type.__name__ = "Integer32"
_IfWredPreMinBytes_Object = MibTableColumn
ifWredPreMinBytes = _IfWredPreMinBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 4, 1, 3),
    _IfWredPreMinBytes_Type()
)
ifWredPreMinBytes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifWredPreMinBytes.setStatus("current")


class _IfWredPreMaxBytes_Type(Integer32):
    """Custom type ifWredPreMaxBytes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 65535),
    )


_IfWredPreMaxBytes_Type.__name__ = "Integer32"
_IfWredPreMaxBytes_Object = MibTableColumn
ifWredPreMaxBytes = _IfWredPreMaxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 4, 1, 4),
    _IfWredPreMaxBytes_Type()
)
ifWredPreMaxBytes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifWredPreMaxBytes.setStatus("current")


class _IfWredPreDenominator_Type(Integer32):
    """Custom type ifWredPreDenominator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IfWredPreDenominator_Type.__name__ = "Integer32"
_IfWredPreDenominator_Object = MibTableColumn
ifWredPreDenominator = _IfWredPreDenominator_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 4, 1, 5),
    _IfWredPreDenominator_Type()
)
ifWredPreDenominator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifWredPreDenominator.setStatus("current")
_IfWredRuleStatus_Type = RowStatus
_IfWredRuleStatus_Object = MibTableColumn
ifWredRuleStatus = _IfWredRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 7, 4, 1, 6),
    _IfWredRuleStatus_Type()
)
ifWredRuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifWredRuleStatus.setStatus("current")
_IfQos_ObjectIdentity = ObjectIdentity
ifQos = _IfQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8)
)
_IfQosTable_Object = MibTable
ifQosTable = _IfQosTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 1)
)
if mibBuilder.loadTexts:
    ifQosTable.setStatus("current")
_IfQosEntry_Object = MibTableRow
ifQosEntry = _IfQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 1, 1)
)
ifQosEntry.setIndexNames(
    (0, "MPQOS-MIB", "ifQosIfIndex"),
)
if mibBuilder.loadTexts:
    ifQosEntry.setStatus("current")
_IfQosIfIndex_Type = Integer32
_IfQosIfIndex_Object = MibTableColumn
ifQosIfIndex = _IfQosIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 1, 1, 1),
    _IfQosIfIndex_Type()
)
ifQosIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifQosIfIndex.setStatus("current")
_IfQosOutputPolicyName_Type = DisplayString
_IfQosOutputPolicyName_Object = MibTableColumn
ifQosOutputPolicyName = _IfQosOutputPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 1, 1, 2),
    _IfQosOutputPolicyName_Type()
)
ifQosOutputPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifQosOutputPolicyName.setStatus("current")
_IfQosInputPolicyName_Type = DisplayString
_IfQosInputPolicyName_Object = MibTableColumn
ifQosInputPolicyName = _IfQosInputPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 1, 1, 3),
    _IfQosInputPolicyName_Type()
)
ifQosInputPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifQosInputPolicyName.setStatus("current")


class _IfQosListType_Type(Integer32):
    """Custom type ifQosListType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("pq", 1),
          ("cq", 2),
          ("wred", 3),
          ("cbwfq", 4),
          ("fair-queue", 5),
          ("fifo", 6))
    )


_IfQosListType_Type.__name__ = "Integer32"
_IfQosListType_Object = MibTableColumn
ifQosListType = _IfQosListType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 1, 1, 4),
    _IfQosListType_Type()
)
ifQosListType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifQosListType.setStatus("current")
_IfQosListNo_Type = Integer32
_IfQosListNo_Object = MibTableColumn
ifQosListNo = _IfQosListNo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 1, 1, 5),
    _IfQosListNo_Type()
)
ifQosListNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifQosListNo.setStatus("current")
_IfQosTrafficShapeRate_Type = Integer32
_IfQosTrafficShapeRate_Object = MibTableColumn
ifQosTrafficShapeRate = _IfQosTrafficShapeRate_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 1, 1, 6),
    _IfQosTrafficShapeRate_Type()
)
ifQosTrafficShapeRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifQosTrafficShapeRate.setStatus("current")
_IfQosTrafficShapeBurst_Type = Integer32
_IfQosTrafficShapeBurst_Object = MibTableColumn
ifQosTrafficShapeBurst = _IfQosTrafficShapeBurst_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 1, 1, 7),
    _IfQosTrafficShapeBurst_Type()
)
ifQosTrafficShapeBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifQosTrafficShapeBurst.setStatus("current")
_IfQosStatus_Type = RowStatus
_IfQosStatus_Object = MibTableColumn
ifQosStatus = _IfQosStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 1, 1, 8),
    _IfQosStatus_Type()
)
ifQosStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifQosStatus.setStatus("current")
_IfQosIfTable_Object = MibTable
ifQosIfTable = _IfQosIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 2)
)
if mibBuilder.loadTexts:
    ifQosIfTable.setStatus("current")
_IfQosIfEntry_Object = MibTableRow
ifQosIfEntry = _IfQosIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 2, 1)
)
ifQosIfEntry.setIndexNames(
    (0, "MPQOS-MIB", "ifQosIfQIndex"),
)
if mibBuilder.loadTexts:
    ifQosIfEntry.setStatus("current")
_IfQosIfQIfIndex_Type = Integer32
_IfQosIfQIfIndex_Object = MibTableColumn
ifQosIfQIfIndex = _IfQosIfQIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 2, 1, 1),
    _IfQosIfQIfIndex_Type()
)
ifQosIfQIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosIfQIfIndex.setStatus("current")


class _IfQosIfQType_Type(Integer32):
    """Custom type ifQosIfQType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("pq", 1),
          ("cq", 2),
          ("wred", 3),
          ("cbwfq", 4),
          ("fair-queue", 5))
    )


_IfQosIfQType_Type.__name__ = "Integer32"
_IfQosIfQType_Object = MibTableColumn
ifQosIfQType = _IfQosIfQType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 2, 1, 2),
    _IfQosIfQType_Type()
)
ifQosIfQType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosIfQType.setStatus("current")
_IfQosIfQNum_Type = Integer32
_IfQosIfQNum_Object = MibTableColumn
ifQosIfQNum = _IfQosIfQNum_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 2, 1, 3),
    _IfQosIfQNum_Type()
)
ifQosIfQNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosIfQNum.setStatus("current")
_IfQosTotalBytes_Type = Integer32
_IfQosTotalBytes_Object = MibTableColumn
ifQosTotalBytes = _IfQosTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 2, 1, 4),
    _IfQosTotalBytes_Type()
)
ifQosTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosTotalBytes.setStatus("current")
_IfQosCurTotalBytes_Type = Integer32
_IfQosCurTotalBytes_Object = MibTableColumn
ifQosCurTotalBytes = _IfQosCurTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 2, 1, 5),
    _IfQosCurTotalBytes_Type()
)
ifQosCurTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosCurTotalBytes.setStatus("current")
_IfQosTotalInputPkts_Type = Counter32
_IfQosTotalInputPkts_Object = MibTableColumn
ifQosTotalInputPkts = _IfQosTotalInputPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 2, 1, 6),
    _IfQosTotalInputPkts_Type()
)
ifQosTotalInputPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosTotalInputPkts.setStatus("current")
_IfQosTotalInputBytes_Type = Counter32
_IfQosTotalInputBytes_Object = MibTableColumn
ifQosTotalInputBytes = _IfQosTotalInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 2, 1, 7),
    _IfQosTotalInputBytes_Type()
)
ifQosTotalInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosTotalInputBytes.setStatus("current")
_IfQosTotalOutputPkts_Type = Counter32
_IfQosTotalOutputPkts_Object = MibTableColumn
ifQosTotalOutputPkts = _IfQosTotalOutputPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 2, 1, 8),
    _IfQosTotalOutputPkts_Type()
)
ifQosTotalOutputPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosTotalOutputPkts.setStatus("current")
_IfQosTotalOutputBytes_Type = Counter32
_IfQosTotalOutputBytes_Object = MibTableColumn
ifQosTotalOutputBytes = _IfQosTotalOutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 2, 1, 9),
    _IfQosTotalOutputBytes_Type()
)
ifQosTotalOutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosTotalOutputBytes.setStatus("current")
_IfQosTotalDropPkts_Type = Counter32
_IfQosTotalDropPkts_Object = MibTableColumn
ifQosTotalDropPkts = _IfQosTotalDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 2, 1, 10),
    _IfQosTotalDropPkts_Type()
)
ifQosTotalDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosTotalDropPkts.setStatus("current")
_IfQosTotalDropBytes_Type = Counter32
_IfQosTotalDropBytes_Object = MibTableColumn
ifQosTotalDropBytes = _IfQosTotalDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 2, 1, 11),
    _IfQosTotalDropBytes_Type()
)
ifQosTotalDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosTotalDropBytes.setStatus("current")
_IfQosActiveQCnt_Type = Integer32
_IfQosActiveQCnt_Object = MibTableColumn
ifQosActiveQCnt = _IfQosActiveQCnt_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 2, 1, 12),
    _IfQosActiveQCnt_Type()
)
ifQosActiveQCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosActiveQCnt.setStatus("current")
_IfQosCBWFQActQCnt_Type = Integer32
_IfQosCBWFQActQCnt_Object = MibTableColumn
ifQosCBWFQActQCnt = _IfQosCBWFQActQCnt_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 2, 1, 13),
    _IfQosCBWFQActQCnt_Type()
)
ifQosCBWFQActQCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosCBWFQActQCnt.setStatus("current")


class _IfQosRSVPReq_Type(Integer32):
    """Custom type ifQosRSVPReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_IfQosRSVPReq_Type.__name__ = "Integer32"
_IfQosRSVPReq_Object = MibTableColumn
ifQosRSVPReq = _IfQosRSVPReq_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 2, 1, 14),
    _IfQosRSVPReq_Type()
)
ifQosRSVPReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosRSVPReq.setStatus("current")
_IfQosQTable_Object = MibTable
ifQosQTable = _IfQosQTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 3)
)
if mibBuilder.loadTexts:
    ifQosQTable.setStatus("current")
_IfQosQEntry_Object = MibTableRow
ifQosQEntry = _IfQosQEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 3, 1)
)
ifQosQEntry.setIndexNames(
    (0, "MPQOS-MIB", "ifQosQIndex"),
    (0, "MPQOS-MIB", "ifQosQId"),
)
if mibBuilder.loadTexts:
    ifQosQEntry.setStatus("current")
_IfQosQIfIndex_Type = Integer32
_IfQosQIfIndex_Object = MibTableColumn
ifQosQIfIndex = _IfQosQIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 3, 1, 1),
    _IfQosQIfIndex_Type()
)
ifQosQIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosQIfIndex.setStatus("current")
_IfQosQId_Type = Integer32
_IfQosQId_Object = MibTableColumn
ifQosQId = _IfQosQId_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 3, 1, 2),
    _IfQosQId_Type()
)
ifQosQId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosQId.setStatus("current")
_IfQosQLimit_Type = Integer32
_IfQosQLimit_Object = MibTableColumn
ifQosQLimit = _IfQosQLimit_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 3, 1, 3),
    _IfQosQLimit_Type()
)
ifQosQLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosQLimit.setStatus("current")
_IfQosQSndPkts_Type = Counter32
_IfQosQSndPkts_Object = MibTableColumn
ifQosQSndPkts = _IfQosQSndPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 3, 1, 4),
    _IfQosQSndPkts_Type()
)
ifQosQSndPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosQSndPkts.setStatus("current")
_IfQosQSndBytes_Type = Counter32
_IfQosQSndBytes_Object = MibTableColumn
ifQosQSndBytes = _IfQosQSndBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 3, 1, 5),
    _IfQosQSndBytes_Type()
)
ifQosQSndBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosQSndBytes.setStatus("current")
_IfQosQDropPkts_Type = Counter32
_IfQosQDropPkts_Object = MibTableColumn
ifQosQDropPkts = _IfQosQDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 3, 1, 6),
    _IfQosQDropPkts_Type()
)
ifQosQDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosQDropPkts.setStatus("current")
_IfQosQDropBytes_Type = Counter32
_IfQosQDropBytes_Object = MibTableColumn
ifQosQDropBytes = _IfQosQDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 3, 1, 7),
    _IfQosQDropBytes_Type()
)
ifQosQDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosQDropBytes.setStatus("current")
_IfQosQCurBytes_Type = Integer32
_IfQosQCurBytes_Object = MibTableColumn
ifQosQCurBytes = _IfQosQCurBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 3, 1, 8),
    _IfQosQCurBytes_Type()
)
ifQosQCurBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosQCurBytes.setStatus("current")
_IfQosQMaxSndBytes_Type = Counter32
_IfQosQMaxSndBytes_Object = MibTableColumn
ifQosQMaxSndBytes = _IfQosQMaxSndBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 8, 3, 1, 9),
    _IfQosQMaxSndBytes_Type()
)
ifQosQMaxSndBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQosQMaxSndBytes.setStatus("current")
_CbwfqConf_ObjectIdentity = ObjectIdentity
cbwfqConf = _CbwfqConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 9)
)
_CbwfqConfMaxClassNum_Type = Integer32
_CbwfqConfMaxClassNum_Object = MibScalar
cbwfqConfMaxClassNum = _CbwfqConfMaxClassNum_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 9, 1),
    _CbwfqConfMaxClassNum_Type()
)
cbwfqConfMaxClassNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbwfqConfMaxClassNum.setStatus("current")
_CbwfqConfMaxPolicyNum_Type = Integer32
_CbwfqConfMaxPolicyNum_Object = MibScalar
cbwfqConfMaxPolicyNum = _CbwfqConfMaxPolicyNum_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 9, 2),
    _CbwfqConfMaxPolicyNum_Type()
)
cbwfqConfMaxPolicyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbwfqConfMaxPolicyNum.setStatus("current")
_QosCar_ObjectIdentity = ObjectIdentity
qosCar = _QosCar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 10)
)
_QosCarTable_Object = MibTable
qosCarTable = _QosCarTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 10, 3)
)
if mibBuilder.loadTexts:
    qosCarTable.setStatus("current")
_QosCarEntry_Object = MibTableRow
qosCarEntry = _QosCarEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 10, 3, 1)
)
qosCarEntry.setIndexNames(
    (0, "MPQOS-MIB", "qosCarIndex"),
    (0, "MPQOS-MIB", "qosCarIfIndex"),
)
if mibBuilder.loadTexts:
    qosCarEntry.setStatus("current")
_QosCarIndex_Type = Integer32
_QosCarIndex_Object = MibTableColumn
qosCarIndex = _QosCarIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 10, 3, 1, 1),
    _QosCarIndex_Type()
)
qosCarIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCarIndex.setStatus("current")
_QosCarIfIndex_Type = Integer32
_QosCarIfIndex_Object = MibTableColumn
qosCarIfIndex = _QosCarIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 10, 3, 1, 2),
    _QosCarIfIndex_Type()
)
qosCarIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCarIfIndex.setStatus("current")
_QosCarMaxBw_Type = Integer32
_QosCarMaxBw_Object = MibTableColumn
qosCarMaxBw = _QosCarMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 10, 3, 1, 3),
    _QosCarMaxBw_Type()
)
qosCarMaxBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCarMaxBw.setStatus("current")
_QosCarNormalBw_Type = Integer32
_QosCarNormalBw_Object = MibTableColumn
qosCarNormalBw = _QosCarNormalBw_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 10, 3, 1, 4),
    _QosCarNormalBw_Type()
)
qosCarNormalBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCarNormalBw.setStatus("current")
_QosCarExceedBw_Type = Integer32
_QosCarExceedBw_Object = MibTableColumn
qosCarExceedBw = _QosCarExceedBw_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 10, 3, 1, 5),
    _QosCarExceedBw_Type()
)
qosCarExceedBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCarExceedBw.setStatus("current")


class _QosCarConformAct_Type(Integer32):
    """Custom type qosCarConformAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("continue", 1),
          ("drop", 2),
          ("transmit", 3),
          ("set-dscp-continue", 4),
          ("set-dscp-transmit", 5),
          ("set-prec-continue", 6),
          ("set-prec-transmit", 7))
    )


_QosCarConformAct_Type.__name__ = "Integer32"
_QosCarConformAct_Object = MibTableColumn
qosCarConformAct = _QosCarConformAct_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 10, 3, 1, 6),
    _QosCarConformAct_Type()
)
qosCarConformAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCarConformAct.setStatus("current")


class _QosCarExceedAct_Type(Integer32):
    """Custom type qosCarExceedAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("continue", 1),
          ("drop", 2),
          ("transmit", 3),
          ("set-dscp-continue", 4),
          ("set-dscp-transmit", 5),
          ("set-prec-continue", 6),
          ("set-prec-transmit", 7))
    )


_QosCarExceedAct_Type.__name__ = "Integer32"
_QosCarExceedAct_Object = MibTableColumn
qosCarExceedAct = _QosCarExceedAct_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 10, 3, 1, 7),
    _QosCarExceedAct_Type()
)
qosCarExceedAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCarExceedAct.setStatus("current")
_QosCarConformActNo_Type = Integer32
_QosCarConformActNo_Object = MibTableColumn
qosCarConformActNo = _QosCarConformActNo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 10, 3, 1, 8),
    _QosCarConformActNo_Type()
)
qosCarConformActNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCarConformActNo.setStatus("current")
_QosCarExceedActNo_Type = Integer32
_QosCarExceedActNo_Object = MibTableColumn
qosCarExceedActNo = _QosCarExceedActNo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 10, 3, 1, 9),
    _QosCarExceedActNo_Type()
)
qosCarExceedActNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCarExceedActNo.setStatus("current")
_QosCarStatus_Type = RowStatus
_QosCarStatus_Object = MibTableColumn
qosCarStatus = _QosCarStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 10, 3, 1, 10),
    _QosCarStatus_Type()
)
qosCarStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCarStatus.setStatus("current")
_QosCarConformPkts_Type = Counter32
_QosCarConformPkts_Object = MibTableColumn
qosCarConformPkts = _QosCarConformPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 10, 3, 1, 11),
    _QosCarConformPkts_Type()
)
qosCarConformPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCarConformPkts.setStatus("current")
_QosCarConformBytes_Type = Counter32
_QosCarConformBytes_Object = MibTableColumn
qosCarConformBytes = _QosCarConformBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 10, 3, 1, 12),
    _QosCarConformBytes_Type()
)
qosCarConformBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCarConformBytes.setStatus("current")
_QosCarExceedPkts_Type = Counter32
_QosCarExceedPkts_Object = MibTableColumn
qosCarExceedPkts = _QosCarExceedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 10, 3, 1, 13),
    _QosCarExceedPkts_Type()
)
qosCarExceedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCarExceedPkts.setStatus("current")
_QosCarExceedBytes_Type = Counter32
_QosCarExceedBytes_Object = MibTableColumn
qosCarExceedBytes = _QosCarExceedBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 10, 3, 1, 14),
    _QosCarExceedBytes_Type()
)
qosCarExceedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCarExceedBytes.setStatus("current")


class _QosCarDirection_Type(Integer32):
    """Custom type qosCarDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_QosCarDirection_Type.__name__ = "Integer32"
_QosCarDirection_Object = MibTableColumn
qosCarDirection = _QosCarDirection_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 10, 3, 1, 15),
    _QosCarDirection_Type()
)
qosCarDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCarDirection.setStatus("current")


class _QosCarAclGrp_Type(Integer32):
    """Custom type qosCarAclGrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_QosCarAclGrp_Type.__name__ = "Integer32"
_QosCarAclGrp_Object = MibTableColumn
qosCarAclGrp = _QosCarAclGrp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 10, 3, 1, 16),
    _QosCarAclGrp_Type()
)
qosCarAclGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosCarAclGrp.setStatus("current")
_PolicyStatis_ObjectIdentity = ObjectIdentity
policyStatis = _PolicyStatis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 20)
)
_PolicyStatisTable_Object = MibTable
policyStatisTable = _PolicyStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 20, 10)
)
if mibBuilder.loadTexts:
    policyStatisTable.setStatus("current")
_PolicyStatisEntry_Object = MibTableRow
policyStatisEntry = _PolicyStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 20, 10, 1)
)
policyStatisEntry.setIndexNames(
    (0, "MPQOS-MIB", "policyStatisIfIndex"),
    (0, "MPQOS-MIB", "policyStatisDirection"),
    (0, "MPQOS-MIB", "policyStatisClassName"),
    (0, "MPQOS-MIB", "policyStatisSubClassName"),
)
if mibBuilder.loadTexts:
    policyStatisEntry.setStatus("current")
_PolicyStatisIfIndex_Type = Unsigned32
_PolicyStatisIfIndex_Object = MibTableColumn
policyStatisIfIndex = _PolicyStatisIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 20, 10, 1, 1),
    _PolicyStatisIfIndex_Type()
)
policyStatisIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyStatisIfIndex.setStatus("current")


class _PolicyStatisDirection_Type(Integer32):
    """Custom type policyStatisDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_PolicyStatisDirection_Type.__name__ = "Integer32"
_PolicyStatisDirection_Object = MibTableColumn
policyStatisDirection = _PolicyStatisDirection_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 20, 10, 1, 2),
    _PolicyStatisDirection_Type()
)
policyStatisDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyStatisDirection.setStatus("current")


class _PolicyStatisClassName_Type(DisplayString):
    """Custom type policyStatisClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PolicyStatisClassName_Type.__name__ = "DisplayString"
_PolicyStatisClassName_Object = MibTableColumn
policyStatisClassName = _PolicyStatisClassName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 20, 10, 1, 3),
    _PolicyStatisClassName_Type()
)
policyStatisClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyStatisClassName.setStatus("current")


class _PolicyStatisSubClassName_Type(DisplayString):
    """Custom type policyStatisSubClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PolicyStatisSubClassName_Type.__name__ = "DisplayString"
_PolicyStatisSubClassName_Object = MibTableColumn
policyStatisSubClassName = _PolicyStatisSubClassName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 20, 10, 1, 4),
    _PolicyStatisSubClassName_Type()
)
policyStatisSubClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyStatisSubClassName.setStatus("current")


class _PolicyStatisRemark_Type(DisplayString):
    """Custom type policyStatisRemark based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_PolicyStatisRemark_Type.__name__ = "DisplayString"
_PolicyStatisRemark_Object = MibTableColumn
policyStatisRemark = _PolicyStatisRemark_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 20, 10, 1, 5),
    _PolicyStatisRemark_Type()
)
policyStatisRemark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyStatisRemark.setStatus("current")
_PolicyStatisPackets_Type = Counter64
_PolicyStatisPackets_Object = MibTableColumn
policyStatisPackets = _PolicyStatisPackets_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 20, 10, 1, 6),
    _PolicyStatisPackets_Type()
)
policyStatisPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyStatisPackets.setStatus("current")
_PolicyStatisBytes_Type = Counter64
_PolicyStatisBytes_Object = MibTableColumn
policyStatisBytes = _PolicyStatisBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 20, 10, 1, 7),
    _PolicyStatisBytes_Type()
)
policyStatisBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyStatisBytes.setStatus("current")
_PolicyStatisRowStatus_Type = RowStatus
_PolicyStatisRowStatus_Object = MibTableColumn
policyStatisRowStatus = _PolicyStatisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 21, 20, 10, 1, 8),
    _PolicyStatisRowStatus_Type()
)
policyStatisRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    policyStatisRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPQOS-MIB",
    **{"mpQosMib": mpQosMib,
       "wfqListTable": wfqListTable,
       "wfqListEntry": wfqListEntry,
       "wfqIndex": wfqIndex,
       "wfqListNum": wfqListNum,
       "wfqCtrlType": wfqCtrlType,
       "wfqQueueLimit": wfqQueueLimit,
       "wfqQueueNumber": wfqQueueNumber,
       "wfqWeightNumber": wfqWeightNumber,
       "wfqWeightType": wfqWeightType,
       "wfqSrcIp": wfqSrcIp,
       "wfqSrcPort": wfqSrcPort,
       "wfqDstIp": wfqDstIp,
       "wfqDstPort": wfqDstPort,
       "wfqStatus": wfqStatus,
       "pqListTable": pqListTable,
       "pqListEntry": pqListEntry,
       "pqIndex": pqIndex,
       "pqListNum": pqListNum,
       "pqCtrlType": pqCtrlType,
       "pqDefault": pqDefault,
       "pqIfIndex": pqIfIndex,
       "pqProtocol": pqProtocol,
       "pqPriority": pqPriority,
       "pqProtType": pqProtType,
       "pqProtValue": pqProtValue,
       "pqQueueHigh": pqQueueHigh,
       "pqQueueMedium": pqQueueMedium,
       "pqQueueNormal": pqQueueNormal,
       "pqQueueLow": pqQueueLow,
       "pqStatus": pqStatus,
       "classMap": classMap,
       "classMapTable": classMapTable,
       "classMapEntry": classMapEntry,
       "classMapClassName": classMapClassName,
       "classMapMatchType": classMapMatchType,
       "classMapRowStatus": classMapRowStatus,
       "classMapAclTable": classMapAclTable,
       "classMapAclEntry": classMapAclEntry,
       "classMapAclClassName": classMapAclClassName,
       "classMapAclListName": classMapAclListName,
       "classMapAclRowStatus": classMapAclRowStatus,
       "classMapInputIfTable": classMapInputIfTable,
       "classMapInputIfEntry": classMapInputIfEntry,
       "classMapInputIfClassName": classMapInputIfClassName,
       "classMapInputIfName": classMapInputIfName,
       "classMapInputIfRowStatus": classMapInputIfRowStatus,
       "classMapIpPrecedenceTable": classMapIpPrecedenceTable,
       "classMapIpPrecedenceEntry": classMapIpPrecedenceEntry,
       "classMapIpPrecedenceClassName": classMapIpPrecedenceClassName,
       "classMapIpPrecedenceValue": classMapIpPrecedenceValue,
       "classMapIpPrecedenceRowStatus": classMapIpPrecedenceRowStatus,
       "classMapIpDscpTable": classMapIpDscpTable,
       "classMapIpDscpEntry": classMapIpDscpEntry,
       "classMapIpDscpClassName": classMapIpDscpClassName,
       "classMapIpDscpValue": classMapIpDscpValue,
       "classMapIpDscpRowStatus": classMapIpDscpRowStatus,
       "classMapMplsExpTable": classMapMplsExpTable,
       "classMapMplsExpEntry": classMapMplsExpEntry,
       "classMapMplsExpClassName": classMapMplsExpClassName,
       "classMapMplsExpValue": classMapMplsExpValue,
       "classMapMplsExpRowStatus": classMapMplsExpRowStatus,
       "classMapProtocolTable": classMapProtocolTable,
       "classMapProtocolEntry": classMapProtocolEntry,
       "classMapProtocolClassName": classMapProtocolClassName,
       "classMapProtocolName": classMapProtocolName,
       "classMapProtocolRowStatus": classMapProtocolRowStatus,
       "classMapNestTable": classMapNestTable,
       "classMapNestEntry": classMapNestEntry,
       "classMapNestClassName": classMapNestClassName,
       "classMapNestName": classMapNestName,
       "classMapNestRowStatus": classMapNestRowStatus,
       "policyMap": policyMap,
       "policyMapTable": policyMapTable,
       "policyMapEntry": policyMapEntry,
       "policyMapName": policyMapName,
       "policyMapRowStatus": policyMapRowStatus,
       "policyClassTable": policyClassTable,
       "policyClassEntry": policyClassEntry,
       "policyClassPolicyName": policyClassPolicyName,
       "policyClassClassName": policyClassClassName,
       "policyClassBandWidthKbps": policyClassBandWidthKbps,
       "policyClassBandWidthTotal": policyClassBandWidthTotal,
       "policyClassBandWidthPercent": policyClassBandWidthPercent,
       "policyClassPriorityBps": policyClassPriorityBps,
       "policyClassPriorityPercent": policyClassPriorityPercent,
       "policyClassWredEnable": policyClassWredEnable,
       "policyClassWredWeight": policyClassWredWeight,
       "policyClassWredMinThreshold0": policyClassWredMinThreshold0,
       "policyClassWredMaxThreshold0": policyClassWredMaxThreshold0,
       "policyClassWredMinThreshold1": policyClassWredMinThreshold1,
       "policyClassWredMaxThreshold1": policyClassWredMaxThreshold1,
       "policyClassWredMinThreshold2": policyClassWredMinThreshold2,
       "policyClassWredMaxThreshold2": policyClassWredMaxThreshold2,
       "policyClassWredMinThreshold3": policyClassWredMinThreshold3,
       "policyClassWredMaxThreshold3": policyClassWredMaxThreshold3,
       "policyClassWredMinThreshold4": policyClassWredMinThreshold4,
       "policyClassWredMaxThreshold4": policyClassWredMaxThreshold4,
       "policyClassWredMinThreshold5": policyClassWredMinThreshold5,
       "policyClassWredMaxThreshold5": policyClassWredMaxThreshold5,
       "policyClassWredMinThreshold6": policyClassWredMinThreshold6,
       "policyClassWredMaxThreshold6": policyClassWredMaxThreshold6,
       "policyClassWredMinThreshold7": policyClassWredMinThreshold7,
       "policyClassWredMaxThreshold7": policyClassWredMaxThreshold7,
       "policyClassSetIpPrecedence": policyClassSetIpPrecedence,
       "policyClassSetIpDscp": policyClassSetIpDscp,
       "policyClassSetMplsImp": policyClassSetMplsImp,
       "policyClassSetMplsTop": policyClassSetMplsTop,
       "policyClassNestName": policyClassNestName,
       "policyClassRowStatus": policyClassRowStatus,
       "priorityList": priorityList,
       "priorityListTable": priorityListTable,
       "priorityListEntry": priorityListEntry,
       "priorityListNo": priorityListNo,
       "priorityListDefQType": priorityListDefQType,
       "priorityListQHigh": priorityListQHigh,
       "priorityListQMedium": priorityListQMedium,
       "priorityListQNormal": priorityListQNormal,
       "priorityListQLow": priorityListQLow,
       "priorityListWredGrpName": priorityListWredGrpName,
       "priorityListDropType": priorityListDropType,
       "priorityListStatus": priorityListStatus,
       "priorityListRuleTable": priorityListRuleTable,
       "priorityListRuleEntry": priorityListRuleEntry,
       "priorityListNoIndex": priorityListNoIndex,
       "priorityListRuleIndex": priorityListRuleIndex,
       "priorityListRuleType": priorityListRuleType,
       "priorityListRulePriType": priorityListRulePriType,
       "priorityListforIntIfIndex": priorityListforIntIfIndex,
       "priorityListProtocolType": priorityListProtocolType,
       "priorityListClassFlag": priorityListClassFlag,
       "priorityListGtSize": priorityListGtSize,
       "priorityListLtSize": priorityListLtSize,
       "priorityListAccListNo": priorityListAccListNo,
       "priorityListTCPPort": priorityListTCPPort,
       "priorityListUDPPort": priorityListUDPPort,
       "priorityListRuleStatus": priorityListRuleStatus,
       "customList": customList,
       "customListTable": customListTable,
       "customListEntry": customListEntry,
       "customListNo": customListNo,
       "customListDefNo": customListDefNo,
       "customListWredName": customListWredName,
       "customListDropType": customListDropType,
       "customListStatus": customListStatus,
       "customListRuleTable": customListRuleTable,
       "customListRuleEntry": customListRuleEntry,
       "customListNoIndex": customListNoIndex,
       "customListIndex": customListIndex,
       "customListICMP": customListICMP,
       "customListIGMP": customListIGMP,
       "customListQNo": customListQNo,
       "customListFragPktQNo": customListFragPktQNo,
       "customListPktEtSize": customListPktEtSize,
       "customListPktGtSize": customListPktGtSize,
       "customListPktLtSize": customListPktLtSize,
       "customListIpSrcAddr": customListIpSrcAddr,
       "customListIpSrcAddrMask": customListIpSrcAddrMask,
       "customListIpDestAddr": customListIpDestAddr,
       "customListIpDestAddrMask": customListIpDestAddrMask,
       "customListAccListNo": customListAccListNo,
       "customListQByteCount": customListQByteCount,
       "customListQLimit": customListQLimit,
       "customListTCPSrcAddr": customListTCPSrcAddr,
       "customListTCPSrcAddrMask": customListTCPSrcAddrMask,
       "customListTCPSrcPort": customListTCPSrcPort,
       "customListTCPDestAddr": customListTCPDestAddr,
       "customListTCPDestAddrMask": customListTCPDestAddrMask,
       "customListTCPDestPort": customListTCPDestPort,
       "customListUDPSrcAddr": customListUDPSrcAddr,
       "customListUDPSrcAddrMask": customListUDPSrcAddrMask,
       "customListUDPSrcPort": customListUDPSrcPort,
       "customListUDPDestAddr": customListUDPDestAddr,
       "customListUDPDestAddrMask": customListUDPDestAddrMask,
       "customListUDPDestPort": customListUDPDestPort,
       "customIntListIfIndex": customIntListIfIndex,
       "customListRuleStatus": customListRuleStatus,
       "wredGroup": wredGroup,
       "wredGrpTable": wredGrpTable,
       "wredGrpEntry": wredGrpEntry,
       "wredGrpName": wredGrpName,
       "wredGrpExpWeight": wredGrpExpWeight,
       "wredGrpStatus": wredGrpStatus,
       "wredGrpPreTable": wredGrpPreTable,
       "wredGrpPreEntry": wredGrpPreEntry,
       "wredGrpPreName": wredGrpPreName,
       "wredGrpPreNo": wredGrpPreNo,
       "wredGrpPreMinBytes": wredGrpPreMinBytes,
       "wredGrpPreMaxBytes": wredGrpPreMaxBytes,
       "wredGrpPreDenominator": wredGrpPreDenominator,
       "wredGrpPreRandomDropsBytes": wredGrpPreRandomDropsBytes,
       "wredGrpPreTailDropsBytes": wredGrpPreTailDropsBytes,
       "wredGrpPreStatus": wredGrpPreStatus,
       "ifWredTable": ifWredTable,
       "ifWredEntry": ifWredEntry,
       "ifWredIfIndex": ifWredIfIndex,
       "ifWredExpWeight": ifWredExpWeight,
       "ifWredStatus": ifWredStatus,
       "ifWredRuleTable": ifWredRuleTable,
       "ifWredRuleEntry": ifWredRuleEntry,
       "ifWredRuleIfIndex": ifWredRuleIfIndex,
       "ifWredPreNo": ifWredPreNo,
       "ifWredPreMinBytes": ifWredPreMinBytes,
       "ifWredPreMaxBytes": ifWredPreMaxBytes,
       "ifWredPreDenominator": ifWredPreDenominator,
       "ifWredRuleStatus": ifWredRuleStatus,
       "ifQos": ifQos,
       "ifQosTable": ifQosTable,
       "ifQosEntry": ifQosEntry,
       "ifQosIfIndex": ifQosIfIndex,
       "ifQosOutputPolicyName": ifQosOutputPolicyName,
       "ifQosInputPolicyName": ifQosInputPolicyName,
       "ifQosListType": ifQosListType,
       "ifQosListNo": ifQosListNo,
       "ifQosTrafficShapeRate": ifQosTrafficShapeRate,
       "ifQosTrafficShapeBurst": ifQosTrafficShapeBurst,
       "ifQosStatus": ifQosStatus,
       "ifQosIfTable": ifQosIfTable,
       "ifQosIfEntry": ifQosIfEntry,
       "ifQosIfQIfIndex": ifQosIfQIfIndex,
       "ifQosIfQType": ifQosIfQType,
       "ifQosIfQNum": ifQosIfQNum,
       "ifQosTotalBytes": ifQosTotalBytes,
       "ifQosCurTotalBytes": ifQosCurTotalBytes,
       "ifQosTotalInputPkts": ifQosTotalInputPkts,
       "ifQosTotalInputBytes": ifQosTotalInputBytes,
       "ifQosTotalOutputPkts": ifQosTotalOutputPkts,
       "ifQosTotalOutputBytes": ifQosTotalOutputBytes,
       "ifQosTotalDropPkts": ifQosTotalDropPkts,
       "ifQosTotalDropBytes": ifQosTotalDropBytes,
       "ifQosActiveQCnt": ifQosActiveQCnt,
       "ifQosCBWFQActQCnt": ifQosCBWFQActQCnt,
       "ifQosRSVPReq": ifQosRSVPReq,
       "ifQosQTable": ifQosQTable,
       "ifQosQEntry": ifQosQEntry,
       "ifQosQIfIndex": ifQosQIfIndex,
       "ifQosQId": ifQosQId,
       "ifQosQLimit": ifQosQLimit,
       "ifQosQSndPkts": ifQosQSndPkts,
       "ifQosQSndBytes": ifQosQSndBytes,
       "ifQosQDropPkts": ifQosQDropPkts,
       "ifQosQDropBytes": ifQosQDropBytes,
       "ifQosQCurBytes": ifQosQCurBytes,
       "ifQosQMaxSndBytes": ifQosQMaxSndBytes,
       "cbwfqConf": cbwfqConf,
       "cbwfqConfMaxClassNum": cbwfqConfMaxClassNum,
       "cbwfqConfMaxPolicyNum": cbwfqConfMaxPolicyNum,
       "qosCar": qosCar,
       "qosCarTable": qosCarTable,
       "qosCarEntry": qosCarEntry,
       "qosCarIndex": qosCarIndex,
       "qosCarIfIndex": qosCarIfIndex,
       "qosCarMaxBw": qosCarMaxBw,
       "qosCarNormalBw": qosCarNormalBw,
       "qosCarExceedBw": qosCarExceedBw,
       "qosCarConformAct": qosCarConformAct,
       "qosCarExceedAct": qosCarExceedAct,
       "qosCarConformActNo": qosCarConformActNo,
       "qosCarExceedActNo": qosCarExceedActNo,
       "qosCarStatus": qosCarStatus,
       "qosCarConformPkts": qosCarConformPkts,
       "qosCarConformBytes": qosCarConformBytes,
       "qosCarExceedPkts": qosCarExceedPkts,
       "qosCarExceedBytes": qosCarExceedBytes,
       "qosCarDirection": qosCarDirection,
       "qosCarAclGrp": qosCarAclGrp,
       "policyStatis": policyStatis,
       "policyStatisTable": policyStatisTable,
       "policyStatisEntry": policyStatisEntry,
       "policyStatisIfIndex": policyStatisIfIndex,
       "policyStatisDirection": policyStatisDirection,
       "policyStatisClassName": policyStatisClassName,
       "policyStatisSubClassName": policyStatisSubClassName,
       "policyStatisRemark": policyStatisRemark,
       "policyStatisPackets": policyStatisPackets,
       "policyStatisBytes": policyStatisBytes,
       "policyStatisRowStatus": policyStatisRowStatus}
)
