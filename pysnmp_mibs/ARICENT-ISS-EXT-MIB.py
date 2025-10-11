# SNMP MIB module (ARICENT-ISS-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siaemic/ARICENT-ISS-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:14 2025
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

(MplsLabel,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsLabel")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

issExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8)
)
if mibBuilder.loadTexts:
    issExt.setRevisions(
        ("2007-02-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Iss_ObjectIdentity = ObjectIdentity
iss = _Iss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81)
)
_IssExtRateControl_ObjectIdentity = ObjectIdentity
issExtRateControl = _IssExtRateControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 1)
)
_IssExtRateCtrlTable_Object = MibTable
issExtRateCtrlTable = _IssExtRateCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 1, 1)
)
if mibBuilder.loadTexts:
    issExtRateCtrlTable.setStatus("current")
_IssExtRateCtrlEntry_Object = MibTableRow
issExtRateCtrlEntry = _IssExtRateCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 1, 1, 1)
)
issExtRateCtrlEntry.setIndexNames(
    (0, "ARICENT-ISS-EXT-MIB", "issExtRateCtrlIndex"),
)
if mibBuilder.loadTexts:
    issExtRateCtrlEntry.setStatus("current")


class _IssExtRateCtrlIndex_Type(Integer32):
    """Custom type issExtRateCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IssExtRateCtrlIndex_Type.__name__ = "Integer32"
_IssExtRateCtrlIndex_Object = MibTableColumn
issExtRateCtrlIndex = _IssExtRateCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 1, 1, 1, 1),
    _IssExtRateCtrlIndex_Type()
)
issExtRateCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    issExtRateCtrlIndex.setStatus("current")


class _IssExtRateCtrlDLFLimitValue_Type(Integer32):
    """Custom type issExtRateCtrlDLFLimitValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IssExtRateCtrlDLFLimitValue_Type.__name__ = "Integer32"
_IssExtRateCtrlDLFLimitValue_Object = MibTableColumn
issExtRateCtrlDLFLimitValue = _IssExtRateCtrlDLFLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 1, 1, 1, 2),
    _IssExtRateCtrlDLFLimitValue_Type()
)
issExtRateCtrlDLFLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtRateCtrlDLFLimitValue.setStatus("current")


class _IssExtRateCtrlBCASTLimitValue_Type(Integer32):
    """Custom type issExtRateCtrlBCASTLimitValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IssExtRateCtrlBCASTLimitValue_Type.__name__ = "Integer32"
_IssExtRateCtrlBCASTLimitValue_Object = MibTableColumn
issExtRateCtrlBCASTLimitValue = _IssExtRateCtrlBCASTLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 1, 1, 1, 3),
    _IssExtRateCtrlBCASTLimitValue_Type()
)
issExtRateCtrlBCASTLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtRateCtrlBCASTLimitValue.setStatus("current")


class _IssExtRateCtrlMCASTLimitValue_Type(Integer32):
    """Custom type issExtRateCtrlMCASTLimitValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IssExtRateCtrlMCASTLimitValue_Type.__name__ = "Integer32"
_IssExtRateCtrlMCASTLimitValue_Object = MibTableColumn
issExtRateCtrlMCASTLimitValue = _IssExtRateCtrlMCASTLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 1, 1, 1, 4),
    _IssExtRateCtrlMCASTLimitValue_Type()
)
issExtRateCtrlMCASTLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtRateCtrlMCASTLimitValue.setStatus("current")


class _IssExtRateCtrlPortRateLimit_Type(Integer32):
    """Custom type issExtRateCtrlPortRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 80000000),
    )


_IssExtRateCtrlPortRateLimit_Type.__name__ = "Integer32"
_IssExtRateCtrlPortRateLimit_Object = MibTableColumn
issExtRateCtrlPortRateLimit = _IssExtRateCtrlPortRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 1, 1, 1, 5),
    _IssExtRateCtrlPortRateLimit_Type()
)
issExtRateCtrlPortRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtRateCtrlPortRateLimit.setStatus("current")


class _IssExtRateCtrlPortBurstSize_Type(Integer32):
    """Custom type issExtRateCtrlPortBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 80000000),
    )


_IssExtRateCtrlPortBurstSize_Type.__name__ = "Integer32"
_IssExtRateCtrlPortBurstSize_Object = MibTableColumn
issExtRateCtrlPortBurstSize = _IssExtRateCtrlPortBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 1, 1, 1, 6),
    _IssExtRateCtrlPortBurstSize_Type()
)
issExtRateCtrlPortBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtRateCtrlPortBurstSize.setStatus("current")


class _IssExtDefaultRateCtrlStatus_Type(Integer32):
    """Custom type issExtDefaultRateCtrlStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IssExtDefaultRateCtrlStatus_Type.__name__ = "Integer32"
_IssExtDefaultRateCtrlStatus_Object = MibTableColumn
issExtDefaultRateCtrlStatus = _IssExtDefaultRateCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 1, 1, 1, 7),
    _IssExtDefaultRateCtrlStatus_Type()
)
issExtDefaultRateCtrlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtDefaultRateCtrlStatus.setStatus("current")
_IssExtL2Filter_ObjectIdentity = ObjectIdentity
issExtL2Filter = _IssExtL2Filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 2)
)
_IssExtL2FilterTable_Object = MibTable
issExtL2FilterTable = _IssExtL2FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 2, 1)
)
if mibBuilder.loadTexts:
    issExtL2FilterTable.setStatus("current")
_IssExtL2FilterEntry_Object = MibTableRow
issExtL2FilterEntry = _IssExtL2FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 2, 1, 1)
)
issExtL2FilterEntry.setIndexNames(
    (0, "ARICENT-ISS-EXT-MIB", "issExtL2FilterNo"),
)
if mibBuilder.loadTexts:
    issExtL2FilterEntry.setStatus("current")


class _IssExtL2FilterNo_Type(Integer32):
    """Custom type issExtL2FilterNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IssExtL2FilterNo_Type.__name__ = "Integer32"
_IssExtL2FilterNo_Object = MibTableColumn
issExtL2FilterNo = _IssExtL2FilterNo_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 2, 1, 1, 1),
    _IssExtL2FilterNo_Type()
)
issExtL2FilterNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    issExtL2FilterNo.setStatus("current")


class _IssExtL2FilterPriority_Type(Integer32):
    """Custom type issExtL2FilterPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IssExtL2FilterPriority_Type.__name__ = "Integer32"
_IssExtL2FilterPriority_Object = MibTableColumn
issExtL2FilterPriority = _IssExtL2FilterPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 2, 1, 1, 2),
    _IssExtL2FilterPriority_Type()
)
issExtL2FilterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL2FilterPriority.setStatus("current")


class _IssExtL2FilterEtherType_Type(Integer32):
    """Custom type issExtL2FilterEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IssExtL2FilterEtherType_Type.__name__ = "Integer32"
_IssExtL2FilterEtherType_Object = MibTableColumn
issExtL2FilterEtherType = _IssExtL2FilterEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 2, 1, 1, 3),
    _IssExtL2FilterEtherType_Type()
)
issExtL2FilterEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL2FilterEtherType.setStatus("current")


class _IssExtL2FilterProtocolType_Type(Unsigned32):
    """Custom type issExtL2FilterProtocolType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IssExtL2FilterProtocolType_Type.__name__ = "Unsigned32"
_IssExtL2FilterProtocolType_Object = MibTableColumn
issExtL2FilterProtocolType = _IssExtL2FilterProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 2, 1, 1, 4),
    _IssExtL2FilterProtocolType_Type()
)
issExtL2FilterProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL2FilterProtocolType.setStatus("current")
_IssExtL2FilterDstMacAddr_Type = MacAddress
_IssExtL2FilterDstMacAddr_Object = MibTableColumn
issExtL2FilterDstMacAddr = _IssExtL2FilterDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 2, 1, 1, 5),
    _IssExtL2FilterDstMacAddr_Type()
)
issExtL2FilterDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL2FilterDstMacAddr.setStatus("current")
_IssExtL2FilterSrcMacAddr_Type = MacAddress
_IssExtL2FilterSrcMacAddr_Object = MibTableColumn
issExtL2FilterSrcMacAddr = _IssExtL2FilterSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 2, 1, 1, 6),
    _IssExtL2FilterSrcMacAddr_Type()
)
issExtL2FilterSrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL2FilterSrcMacAddr.setStatus("current")


class _IssExtL2FilterVlanId_Type(Integer32):
    """Custom type issExtL2FilterVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_IssExtL2FilterVlanId_Type.__name__ = "Integer32"
_IssExtL2FilterVlanId_Object = MibTableColumn
issExtL2FilterVlanId = _IssExtL2FilterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 2, 1, 1, 7),
    _IssExtL2FilterVlanId_Type()
)
issExtL2FilterVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL2FilterVlanId.setStatus("current")
_IssExtL2FilterInPortList_Type = PortList
_IssExtL2FilterInPortList_Object = MibTableColumn
issExtL2FilterInPortList = _IssExtL2FilterInPortList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 2, 1, 1, 8),
    _IssExtL2FilterInPortList_Type()
)
issExtL2FilterInPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL2FilterInPortList.setStatus("current")


class _IssExtL2FilterAction_Type(Integer32):
    """Custom type issExtL2FilterAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("drop", 2),
          ("redirect", 3))
    )


_IssExtL2FilterAction_Type.__name__ = "Integer32"
_IssExtL2FilterAction_Object = MibTableColumn
issExtL2FilterAction = _IssExtL2FilterAction_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 2, 1, 1, 9),
    _IssExtL2FilterAction_Type()
)
issExtL2FilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL2FilterAction.setStatus("current")
_IssExtL2FilterMatchCount_Type = Counter32
_IssExtL2FilterMatchCount_Object = MibTableColumn
issExtL2FilterMatchCount = _IssExtL2FilterMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 2, 1, 1, 10),
    _IssExtL2FilterMatchCount_Type()
)
issExtL2FilterMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issExtL2FilterMatchCount.setStatus("current")
_IssExtL2FilterStatus_Type = RowStatus
_IssExtL2FilterStatus_Object = MibTableColumn
issExtL2FilterStatus = _IssExtL2FilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 2, 1, 1, 11),
    _IssExtL2FilterStatus_Type()
)
issExtL2FilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    issExtL2FilterStatus.setStatus("current")
_IssExtL2FilterOutPortList_Type = PortList
_IssExtL2FilterOutPortList_Object = MibTableColumn
issExtL2FilterOutPortList = _IssExtL2FilterOutPortList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 2, 1, 1, 12),
    _IssExtL2FilterOutPortList_Type()
)
issExtL2FilterOutPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL2FilterOutPortList.setStatus("current")


class _IssExtL2FilterDirection_Type(Integer32):
    """Custom type issExtL2FilterDirection based on Integer32"""
    defaultValue = 1

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


_IssExtL2FilterDirection_Type.__name__ = "Integer32"
_IssExtL2FilterDirection_Object = MibTableColumn
issExtL2FilterDirection = _IssExtL2FilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 2, 1, 1, 13),
    _IssExtL2FilterDirection_Type()
)
issExtL2FilterDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL2FilterDirection.setStatus("current")
_IssExtL2FilterInPortChannelList_Type = PortList
_IssExtL2FilterInPortChannelList_Object = MibTableColumn
issExtL2FilterInPortChannelList = _IssExtL2FilterInPortChannelList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 2, 1, 1, 14),
    _IssExtL2FilterInPortChannelList_Type()
)
issExtL2FilterInPortChannelList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL2FilterInPortChannelList.setStatus("current")
_IssExtL2FilterOutPortChannelList_Type = PortList
_IssExtL2FilterOutPortChannelList_Object = MibTableColumn
issExtL2FilterOutPortChannelList = _IssExtL2FilterOutPortChannelList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 2, 1, 1, 15),
    _IssExtL2FilterOutPortChannelList_Type()
)
issExtL2FilterOutPortChannelList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL2FilterOutPortChannelList.setStatus("current")
_IssExtL3Filter_ObjectIdentity = ObjectIdentity
issExtL3Filter = _IssExtL3Filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3)
)
_IssExtL3FilterTable_Object = MibTable
issExtL3FilterTable = _IssExtL3FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1)
)
if mibBuilder.loadTexts:
    issExtL3FilterTable.setStatus("current")
_IssExtL3FilterEntry_Object = MibTableRow
issExtL3FilterEntry = _IssExtL3FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1)
)
issExtL3FilterEntry.setIndexNames(
    (0, "ARICENT-ISS-EXT-MIB", "issExtL3FilterNo"),
)
if mibBuilder.loadTexts:
    issExtL3FilterEntry.setStatus("current")


class _IssExtL3FilterNo_Type(Integer32):
    """Custom type issExtL3FilterNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IssExtL3FilterNo_Type.__name__ = "Integer32"
_IssExtL3FilterNo_Object = MibTableColumn
issExtL3FilterNo = _IssExtL3FilterNo_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 1),
    _IssExtL3FilterNo_Type()
)
issExtL3FilterNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    issExtL3FilterNo.setStatus("current")


class _IssExtL3FilterPriority_Type(Integer32):
    """Custom type issExtL3FilterPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IssExtL3FilterPriority_Type.__name__ = "Integer32"
_IssExtL3FilterPriority_Object = MibTableColumn
issExtL3FilterPriority = _IssExtL3FilterPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 2),
    _IssExtL3FilterPriority_Type()
)
issExtL3FilterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL3FilterPriority.setStatus("current")


class _IssExtL3FilterProtocol_Type(Integer32):
    """Custom type issExtL3FilterProtocol based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IssExtL3FilterProtocol_Type.__name__ = "Integer32"
_IssExtL3FilterProtocol_Object = MibTableColumn
issExtL3FilterProtocol = _IssExtL3FilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 3),
    _IssExtL3FilterProtocol_Type()
)
issExtL3FilterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL3FilterProtocol.setStatus("current")


class _IssExtL3FilterMessageType_Type(Integer32):
    """Custom type issExtL3FilterMessageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IssExtL3FilterMessageType_Type.__name__ = "Integer32"
_IssExtL3FilterMessageType_Object = MibTableColumn
issExtL3FilterMessageType = _IssExtL3FilterMessageType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 4),
    _IssExtL3FilterMessageType_Type()
)
issExtL3FilterMessageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL3FilterMessageType.setStatus("current")


class _IssExtL3FilterMessageCode_Type(Integer32):
    """Custom type issExtL3FilterMessageCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IssExtL3FilterMessageCode_Type.__name__ = "Integer32"
_IssExtL3FilterMessageCode_Object = MibTableColumn
issExtL3FilterMessageCode = _IssExtL3FilterMessageCode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 5),
    _IssExtL3FilterMessageCode_Type()
)
issExtL3FilterMessageCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL3FilterMessageCode.setStatus("current")
_IssExtL3FilterDstIpAddr_Type = IpAddress
_IssExtL3FilterDstIpAddr_Object = MibTableColumn
issExtL3FilterDstIpAddr = _IssExtL3FilterDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 6),
    _IssExtL3FilterDstIpAddr_Type()
)
issExtL3FilterDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL3FilterDstIpAddr.setStatus("current")
_IssExtL3FilterSrcIpAddr_Type = IpAddress
_IssExtL3FilterSrcIpAddr_Object = MibTableColumn
issExtL3FilterSrcIpAddr = _IssExtL3FilterSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 7),
    _IssExtL3FilterSrcIpAddr_Type()
)
issExtL3FilterSrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL3FilterSrcIpAddr.setStatus("current")


class _IssExtL3FilterDstIpAddrMask_Type(IpAddress):
    """Custom type issExtL3FilterDstIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_IssExtL3FilterDstIpAddrMask_Type.__name__ = "IpAddress"
_IssExtL3FilterDstIpAddrMask_Object = MibTableColumn
issExtL3FilterDstIpAddrMask = _IssExtL3FilterDstIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 8),
    _IssExtL3FilterDstIpAddrMask_Type()
)
issExtL3FilterDstIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL3FilterDstIpAddrMask.setStatus("current")


class _IssExtL3FilterSrcIpAddrMask_Type(IpAddress):
    """Custom type issExtL3FilterSrcIpAddrMask based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_IssExtL3FilterSrcIpAddrMask_Type.__name__ = "IpAddress"
_IssExtL3FilterSrcIpAddrMask_Object = MibTableColumn
issExtL3FilterSrcIpAddrMask = _IssExtL3FilterSrcIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 9),
    _IssExtL3FilterSrcIpAddrMask_Type()
)
issExtL3FilterSrcIpAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL3FilterSrcIpAddrMask.setStatus("current")


class _IssExtL3FilterMinDstProtPort_Type(Unsigned32):
    """Custom type issExtL3FilterMinDstProtPort based on Unsigned32"""
    defaultValue = 0


_IssExtL3FilterMinDstProtPort_Type.__name__ = "Unsigned32"
_IssExtL3FilterMinDstProtPort_Object = MibTableColumn
issExtL3FilterMinDstProtPort = _IssExtL3FilterMinDstProtPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 10),
    _IssExtL3FilterMinDstProtPort_Type()
)
issExtL3FilterMinDstProtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL3FilterMinDstProtPort.setStatus("current")


class _IssExtL3FilterMaxDstProtPort_Type(Unsigned32):
    """Custom type issExtL3FilterMaxDstProtPort based on Unsigned32"""
    defaultValue = 65535


_IssExtL3FilterMaxDstProtPort_Type.__name__ = "Unsigned32"
_IssExtL3FilterMaxDstProtPort_Object = MibTableColumn
issExtL3FilterMaxDstProtPort = _IssExtL3FilterMaxDstProtPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 11),
    _IssExtL3FilterMaxDstProtPort_Type()
)
issExtL3FilterMaxDstProtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL3FilterMaxDstProtPort.setStatus("current")


class _IssExtL3FilterMinSrcProtPort_Type(Unsigned32):
    """Custom type issExtL3FilterMinSrcProtPort based on Unsigned32"""
    defaultValue = 0


_IssExtL3FilterMinSrcProtPort_Type.__name__ = "Unsigned32"
_IssExtL3FilterMinSrcProtPort_Object = MibTableColumn
issExtL3FilterMinSrcProtPort = _IssExtL3FilterMinSrcProtPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 12),
    _IssExtL3FilterMinSrcProtPort_Type()
)
issExtL3FilterMinSrcProtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL3FilterMinSrcProtPort.setStatus("current")


class _IssExtL3FilterMaxSrcProtPort_Type(Unsigned32):
    """Custom type issExtL3FilterMaxSrcProtPort based on Unsigned32"""
    defaultValue = 65535


_IssExtL3FilterMaxSrcProtPort_Type.__name__ = "Unsigned32"
_IssExtL3FilterMaxSrcProtPort_Object = MibTableColumn
issExtL3FilterMaxSrcProtPort = _IssExtL3FilterMaxSrcProtPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 13),
    _IssExtL3FilterMaxSrcProtPort_Type()
)
issExtL3FilterMaxSrcProtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL3FilterMaxSrcProtPort.setStatus("current")
_IssExtL3FilterInPortList_Type = PortList
_IssExtL3FilterInPortList_Object = MibTableColumn
issExtL3FilterInPortList = _IssExtL3FilterInPortList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 14),
    _IssExtL3FilterInPortList_Type()
)
issExtL3FilterInPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL3FilterInPortList.setStatus("current")
_IssExtL3FilterOutPortList_Type = PortList
_IssExtL3FilterOutPortList_Object = MibTableColumn
issExtL3FilterOutPortList = _IssExtL3FilterOutPortList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 15),
    _IssExtL3FilterOutPortList_Type()
)
issExtL3FilterOutPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL3FilterOutPortList.setStatus("current")


class _IssExtL3FilterAckBit_Type(Integer32):
    """Custom type issExtL3FilterAckBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("establish", 1),
          ("notEstablish", 2),
          ("any", 3))
    )


_IssExtL3FilterAckBit_Type.__name__ = "Integer32"
_IssExtL3FilterAckBit_Object = MibTableColumn
issExtL3FilterAckBit = _IssExtL3FilterAckBit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 16),
    _IssExtL3FilterAckBit_Type()
)
issExtL3FilterAckBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    issExtL3FilterAckBit.setStatus("current")


class _IssExtL3FilterRstBit_Type(Integer32):
    """Custom type issExtL3FilterRstBit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("notSet", 2),
          ("any", 3))
    )


_IssExtL3FilterRstBit_Type.__name__ = "Integer32"
_IssExtL3FilterRstBit_Object = MibTableColumn
issExtL3FilterRstBit = _IssExtL3FilterRstBit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 17),
    _IssExtL3FilterRstBit_Type()
)
issExtL3FilterRstBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    issExtL3FilterRstBit.setStatus("current")


class _IssExtL3FilterTos_Type(Integer32):
    """Custom type issExtL3FilterTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IssExtL3FilterTos_Type.__name__ = "Integer32"
_IssExtL3FilterTos_Object = MibTableColumn
issExtL3FilterTos = _IssExtL3FilterTos_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 18),
    _IssExtL3FilterTos_Type()
)
issExtL3FilterTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    issExtL3FilterTos.setStatus("current")


class _IssExtL3FilterDscp_Type(Integer32):
    """Custom type issExtL3FilterDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_IssExtL3FilterDscp_Type.__name__ = "Integer32"
_IssExtL3FilterDscp_Object = MibTableColumn
issExtL3FilterDscp = _IssExtL3FilterDscp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 19),
    _IssExtL3FilterDscp_Type()
)
issExtL3FilterDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    issExtL3FilterDscp.setStatus("current")


class _IssExtL3FilterDirection_Type(Integer32):
    """Custom type issExtL3FilterDirection based on Integer32"""
    defaultValue = 1

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


_IssExtL3FilterDirection_Type.__name__ = "Integer32"
_IssExtL3FilterDirection_Object = MibTableColumn
issExtL3FilterDirection = _IssExtL3FilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 20),
    _IssExtL3FilterDirection_Type()
)
issExtL3FilterDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    issExtL3FilterDirection.setStatus("current")


class _IssExtL3FilterAction_Type(Integer32):
    """Custom type issExtL3FilterAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("drop", 2),
          ("redirect", 3))
    )


_IssExtL3FilterAction_Type.__name__ = "Integer32"
_IssExtL3FilterAction_Object = MibTableColumn
issExtL3FilterAction = _IssExtL3FilterAction_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 21),
    _IssExtL3FilterAction_Type()
)
issExtL3FilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL3FilterAction.setStatus("current")
_IssExtL3FilterMatchCount_Type = Counter32
_IssExtL3FilterMatchCount_Object = MibTableColumn
issExtL3FilterMatchCount = _IssExtL3FilterMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 22),
    _IssExtL3FilterMatchCount_Type()
)
issExtL3FilterMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issExtL3FilterMatchCount.setStatus("current")
_IssExtL3FilterStatus_Type = RowStatus
_IssExtL3FilterStatus_Object = MibTableColumn
issExtL3FilterStatus = _IssExtL3FilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 23),
    _IssExtL3FilterStatus_Type()
)
issExtL3FilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    issExtL3FilterStatus.setStatus("current")
_IssExtL3FilterInPortChannelList_Type = PortList
_IssExtL3FilterInPortChannelList_Object = MibTableColumn
issExtL3FilterInPortChannelList = _IssExtL3FilterInPortChannelList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 24),
    _IssExtL3FilterInPortChannelList_Type()
)
issExtL3FilterInPortChannelList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL3FilterInPortChannelList.setStatus("current")
_IssExtL3FilterOutPortChannelList_Type = PortList
_IssExtL3FilterOutPortChannelList_Object = MibTableColumn
issExtL3FilterOutPortChannelList = _IssExtL3FilterOutPortChannelList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 25),
    _IssExtL3FilterOutPortChannelList_Type()
)
issExtL3FilterOutPortChannelList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL3FilterOutPortChannelList.setStatus("current")
_IssExtL3FilterMplsLabel_Type = MplsLabel
_IssExtL3FilterMplsLabel_Object = MibTableColumn
issExtL3FilterMplsLabel = _IssExtL3FilterMplsLabel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 26),
    _IssExtL3FilterMplsLabel_Type()
)
issExtL3FilterMplsLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL3FilterMplsLabel.setStatus("current")


class _IssExtL3FilterMplsExp_Type(Unsigned32):
    """Custom type issExtL3FilterMplsExp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IssExtL3FilterMplsExp_Type.__name__ = "Unsigned32"
_IssExtL3FilterMplsExp_Object = MibTableColumn
issExtL3FilterMplsExp = _IssExtL3FilterMplsExp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 3, 1, 1, 27),
    _IssExtL3FilterMplsExp_Type()
)
issExtL3FilterMplsExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issExtL3FilterMplsExp.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-ISS-EXT-MIB",
    **{"PortList": PortList,
       "iss": iss,
       "issExt": issExt,
       "issExtRateControl": issExtRateControl,
       "issExtRateCtrlTable": issExtRateCtrlTable,
       "issExtRateCtrlEntry": issExtRateCtrlEntry,
       "issExtRateCtrlIndex": issExtRateCtrlIndex,
       "issExtRateCtrlDLFLimitValue": issExtRateCtrlDLFLimitValue,
       "issExtRateCtrlBCASTLimitValue": issExtRateCtrlBCASTLimitValue,
       "issExtRateCtrlMCASTLimitValue": issExtRateCtrlMCASTLimitValue,
       "issExtRateCtrlPortRateLimit": issExtRateCtrlPortRateLimit,
       "issExtRateCtrlPortBurstSize": issExtRateCtrlPortBurstSize,
       "issExtDefaultRateCtrlStatus": issExtDefaultRateCtrlStatus,
       "issExtL2Filter": issExtL2Filter,
       "issExtL2FilterTable": issExtL2FilterTable,
       "issExtL2FilterEntry": issExtL2FilterEntry,
       "issExtL2FilterNo": issExtL2FilterNo,
       "issExtL2FilterPriority": issExtL2FilterPriority,
       "issExtL2FilterEtherType": issExtL2FilterEtherType,
       "issExtL2FilterProtocolType": issExtL2FilterProtocolType,
       "issExtL2FilterDstMacAddr": issExtL2FilterDstMacAddr,
       "issExtL2FilterSrcMacAddr": issExtL2FilterSrcMacAddr,
       "issExtL2FilterVlanId": issExtL2FilterVlanId,
       "issExtL2FilterInPortList": issExtL2FilterInPortList,
       "issExtL2FilterAction": issExtL2FilterAction,
       "issExtL2FilterMatchCount": issExtL2FilterMatchCount,
       "issExtL2FilterStatus": issExtL2FilterStatus,
       "issExtL2FilterOutPortList": issExtL2FilterOutPortList,
       "issExtL2FilterDirection": issExtL2FilterDirection,
       "issExtL2FilterInPortChannelList": issExtL2FilterInPortChannelList,
       "issExtL2FilterOutPortChannelList": issExtL2FilterOutPortChannelList,
       "issExtL3Filter": issExtL3Filter,
       "issExtL3FilterTable": issExtL3FilterTable,
       "issExtL3FilterEntry": issExtL3FilterEntry,
       "issExtL3FilterNo": issExtL3FilterNo,
       "issExtL3FilterPriority": issExtL3FilterPriority,
       "issExtL3FilterProtocol": issExtL3FilterProtocol,
       "issExtL3FilterMessageType": issExtL3FilterMessageType,
       "issExtL3FilterMessageCode": issExtL3FilterMessageCode,
       "issExtL3FilterDstIpAddr": issExtL3FilterDstIpAddr,
       "issExtL3FilterSrcIpAddr": issExtL3FilterSrcIpAddr,
       "issExtL3FilterDstIpAddrMask": issExtL3FilterDstIpAddrMask,
       "issExtL3FilterSrcIpAddrMask": issExtL3FilterSrcIpAddrMask,
       "issExtL3FilterMinDstProtPort": issExtL3FilterMinDstProtPort,
       "issExtL3FilterMaxDstProtPort": issExtL3FilterMaxDstProtPort,
       "issExtL3FilterMinSrcProtPort": issExtL3FilterMinSrcProtPort,
       "issExtL3FilterMaxSrcProtPort": issExtL3FilterMaxSrcProtPort,
       "issExtL3FilterInPortList": issExtL3FilterInPortList,
       "issExtL3FilterOutPortList": issExtL3FilterOutPortList,
       "issExtL3FilterAckBit": issExtL3FilterAckBit,
       "issExtL3FilterRstBit": issExtL3FilterRstBit,
       "issExtL3FilterTos": issExtL3FilterTos,
       "issExtL3FilterDscp": issExtL3FilterDscp,
       "issExtL3FilterDirection": issExtL3FilterDirection,
       "issExtL3FilterAction": issExtL3FilterAction,
       "issExtL3FilterMatchCount": issExtL3FilterMatchCount,
       "issExtL3FilterStatus": issExtL3FilterStatus,
       "issExtL3FilterInPortChannelList": issExtL3FilterInPortChannelList,
       "issExtL3FilterOutPortChannelList": issExtL3FilterOutPortChannelList,
       "issExtL3FilterMplsLabel": issExtL3FilterMplsLabel,
       "issExtL3FilterMplsExp": issExtL3FilterMplsExp}
)
