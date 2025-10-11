# SNMP MIB module (QTECH-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-QOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:57 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "QTECH-TC",
    "ConfigStatus",
    "IfIndex")

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
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

qtechQoSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18)
)
if mibBuilder.loadTexts:
    qtechQoSMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechQoSPriorityMIBObjects_ObjectIdentity = ObjectIdentity
qtechQoSPriorityMIBObjects = _QtechQoSPriorityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1)
)
_QtechQoSGlobalStatus_Type = EnabledStatus
_QtechQoSGlobalStatus_Object = MibScalar
qtechQoSGlobalStatus = _QtechQoSGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 1),
    _QtechQoSGlobalStatus_Type()
)
qtechQoSGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechQoSGlobalStatus.setStatus("current")
_QtechPriorityTrafficClassNum_Type = Integer32
_QtechPriorityTrafficClassNum_Object = MibScalar
qtechPriorityTrafficClassNum = _QtechPriorityTrafficClassNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 2),
    _QtechPriorityTrafficClassNum_Type()
)
qtechPriorityTrafficClassNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPriorityTrafficClassNum.setStatus("current")
_QtechPriorityClassNum_Type = Integer32
_QtechPriorityClassNum_Object = MibScalar
qtechPriorityClassNum = _QtechPriorityClassNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 3),
    _QtechPriorityClassNum_Type()
)
qtechPriorityClassNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPriorityClassNum.setStatus("current")
_QtechPriorityDscpMaxValue_Type = Integer32
_QtechPriorityDscpMaxValue_Object = MibScalar
qtechPriorityDscpMaxValue = _QtechPriorityDscpMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 4),
    _QtechPriorityDscpMaxValue_Type()
)
qtechPriorityDscpMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPriorityDscpMaxValue.setStatus("current")
_QtechTrafficClassTable_Object = MibTable
qtechTrafficClassTable = _QtechTrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 5)
)
if mibBuilder.loadTexts:
    qtechTrafficClassTable.setStatus("current")
_QtechTrafficClassEntry_Object = MibTableRow
qtechTrafficClassEntry = _QtechTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 5, 1)
)
qtechTrafficClassEntry.setIndexNames(
    (0, "QTECH-QOS-MIB", "qtechTrafficClassPriority"),
)
if mibBuilder.loadTexts:
    qtechTrafficClassEntry.setStatus("current")
_QtechTrafficClassPriority_Type = Integer32
_QtechTrafficClassPriority_Object = MibTableColumn
qtechTrafficClassPriority = _QtechTrafficClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 5, 1, 1),
    _QtechTrafficClassPriority_Type()
)
qtechTrafficClassPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTrafficClassPriority.setStatus("current")
_QtechTrafficClass_Type = Integer32
_QtechTrafficClass_Object = MibTableColumn
qtechTrafficClass = _QtechTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 5, 1, 2),
    _QtechTrafficClass_Type()
)
qtechTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechTrafficClass.setStatus("current")
_QtechPriorityToDscp_Type = Integer32
_QtechPriorityToDscp_Object = MibTableColumn
qtechPriorityToDscp = _QtechPriorityToDscp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 5, 1, 3),
    _QtechPriorityToDscp_Type()
)
qtechPriorityToDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPriorityToDscp.setStatus("current")
_QtechDscpClassTable_Object = MibTable
qtechDscpClassTable = _QtechDscpClassTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 6)
)
if mibBuilder.loadTexts:
    qtechDscpClassTable.setStatus("current")
_QtechDscpClassEntry_Object = MibTableRow
qtechDscpClassEntry = _QtechDscpClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 6, 1)
)
qtechDscpClassEntry.setIndexNames(
    (0, "QTECH-QOS-MIB", "qtechDscpClass"),
)
if mibBuilder.loadTexts:
    qtechDscpClassEntry.setStatus("current")
_QtechDscpClass_Type = Integer32
_QtechDscpClass_Object = MibTableColumn
qtechDscpClass = _QtechDscpClass_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 6, 1, 1),
    _QtechDscpClass_Type()
)
qtechDscpClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDscpClass.setStatus("current")
_QtechDscpTrafficClassPriority_Type = Integer32
_QtechDscpTrafficClassPriority_Object = MibTableColumn
qtechDscpTrafficClassPriority = _QtechDscpTrafficClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 6, 1, 2),
    _QtechDscpTrafficClassPriority_Type()
)
qtechDscpTrafficClassPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDscpTrafficClassPriority.setStatus("current")


class _QtechPriorityTrafficClassOperMode_Type(Integer32):
    """Custom type qtechPriorityTrafficClassOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("qos-sp", 1),
          ("qos-wrr", 2),
          ("qos-drr", 3))
    )


_QtechPriorityTrafficClassOperMode_Type.__name__ = "Integer32"
_QtechPriorityTrafficClassOperMode_Object = MibScalar
qtechPriorityTrafficClassOperMode = _QtechPriorityTrafficClassOperMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 7),
    _QtechPriorityTrafficClassOperMode_Type()
)
qtechPriorityTrafficClassOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPriorityTrafficClassOperMode.setStatus("current")
_QtechPriorityBandWidth_Type = OctetString
_QtechPriorityBandWidth_Object = MibScalar
qtechPriorityBandWidth = _QtechPriorityBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 8),
    _QtechPriorityBandWidth_Type()
)
qtechPriorityBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPriorityBandWidth.setStatus("current")
_QtechIfPriorityTable_Object = MibTable
qtechIfPriorityTable = _QtechIfPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 9)
)
if mibBuilder.loadTexts:
    qtechIfPriorityTable.setStatus("current")
_QtechIfPriorityEntry_Object = MibTableRow
qtechIfPriorityEntry = _QtechIfPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 9, 1)
)
qtechIfPriorityEntry.setIndexNames(
    (0, "QTECH-QOS-MIB", "qtechIfPriorityIfIndex"),
)
if mibBuilder.loadTexts:
    qtechIfPriorityEntry.setStatus("current")
_QtechIfPriorityIfIndex_Type = IfIndex
_QtechIfPriorityIfIndex_Object = MibTableColumn
qtechIfPriorityIfIndex = _QtechIfPriorityIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 9, 1, 1),
    _QtechIfPriorityIfIndex_Type()
)
qtechIfPriorityIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfPriorityIfIndex.setStatus("current")
_QtechIfPriority_Type = Integer32
_QtechIfPriority_Object = MibTableColumn
qtechIfPriority = _QtechIfPriority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 9, 1, 2),
    _QtechIfPriority_Type()
)
qtechIfPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfPriority.setStatus("current")


class _QtechIfPriTrafficClassOperMode_Type(Integer32):
    """Custom type qtechIfPriTrafficClassOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("qos-sp", 1),
          ("qos-wrr", 2),
          ("qos-drr", 3))
    )


_QtechIfPriTrafficClassOperMode_Type.__name__ = "Integer32"
_QtechIfPriTrafficClassOperMode_Object = MibTableColumn
qtechIfPriTrafficClassOperMode = _QtechIfPriTrafficClassOperMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 9, 1, 3),
    _QtechIfPriTrafficClassOperMode_Type()
)
qtechIfPriTrafficClassOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfPriTrafficClassOperMode.setStatus("current")
_QtechIfPriorityBandwidth_Type = OctetString
_QtechIfPriorityBandwidth_Object = MibTableColumn
qtechIfPriorityBandwidth = _QtechIfPriorityBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 9, 1, 4),
    _QtechIfPriorityBandwidth_Type()
)
qtechIfPriorityBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfPriorityBandwidth.setStatus("current")


class _QtechIfPriorityQosTrustMode_Type(Integer32):
    """Custom type qtechIfPriorityQosTrustMode based on Integer32"""
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
        *(("not-trust", 1),
          ("trust-cos", 2),
          ("trust-dscp", 3),
          ("trust-ip-precedence", 4))
    )


_QtechIfPriorityQosTrustMode_Type.__name__ = "Integer32"
_QtechIfPriorityQosTrustMode_Object = MibTableColumn
qtechIfPriorityQosTrustMode = _QtechIfPriorityQosTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 9, 1, 5),
    _QtechIfPriorityQosTrustMode_Type()
)
qtechIfPriorityQosTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfPriorityQosTrustMode.setStatus("current")
_QtechIpPreClassTable_Object = MibTable
qtechIpPreClassTable = _QtechIpPreClassTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 10)
)
if mibBuilder.loadTexts:
    qtechIpPreClassTable.setStatus("current")
_QtechIpPreClassEntry_Object = MibTableRow
qtechIpPreClassEntry = _QtechIpPreClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 10, 1)
)
qtechIpPreClassEntry.setIndexNames(
    (0, "QTECH-QOS-MIB", "qtechIpPreClassPriority"),
)
if mibBuilder.loadTexts:
    qtechIpPreClassEntry.setStatus("current")
_QtechIpPreClassPriority_Type = Integer32
_QtechIpPreClassPriority_Object = MibTableColumn
qtechIpPreClassPriority = _QtechIpPreClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 10, 1, 1),
    _QtechIpPreClassPriority_Type()
)
qtechIpPreClassPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpPreClassPriority.setStatus("current")
_QtechIpPreToDscp_Type = Integer32
_QtechIpPreToDscp_Object = MibTableColumn
qtechIpPreToDscp = _QtechIpPreToDscp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 10, 1, 2),
    _QtechIpPreToDscp_Type()
)
qtechIpPreToDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIpPreToDscp.setStatus("current")
_QtechIfRateLimitTable_Object = MibTable
qtechIfRateLimitTable = _QtechIfRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 11)
)
if mibBuilder.loadTexts:
    qtechIfRateLimitTable.setStatus("current")
_QtechIfRateLimitEntry_Object = MibTableRow
qtechIfRateLimitEntry = _QtechIfRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 11, 1)
)
qtechIfRateLimitEntry.setIndexNames(
    (0, "QTECH-QOS-MIB", "qtechIfRateLimitIndex"),
)
if mibBuilder.loadTexts:
    qtechIfRateLimitEntry.setStatus("current")
_QtechIfRateLimitIndex_Type = IfIndex
_QtechIfRateLimitIndex_Object = MibTableColumn
qtechIfRateLimitIndex = _QtechIfRateLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 11, 1, 1),
    _QtechIfRateLimitIndex_Type()
)
qtechIfRateLimitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfRateLimitIndex.setStatus("current")
_QtechIfRateLimitInMaxBandWidth_Type = Unsigned32
_QtechIfRateLimitInMaxBandWidth_Object = MibTableColumn
qtechIfRateLimitInMaxBandWidth = _QtechIfRateLimitInMaxBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 11, 1, 2),
    _QtechIfRateLimitInMaxBandWidth_Type()
)
qtechIfRateLimitInMaxBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfRateLimitInMaxBandWidth.setStatus("current")
_QtechIfRateLimitInBurstFlowLimit_Type = Integer32
_QtechIfRateLimitInBurstFlowLimit_Object = MibTableColumn
qtechIfRateLimitInBurstFlowLimit = _QtechIfRateLimitInBurstFlowLimit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 11, 1, 3),
    _QtechIfRateLimitInBurstFlowLimit_Type()
)
qtechIfRateLimitInBurstFlowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfRateLimitInBurstFlowLimit.setStatus("current")
_QtechIfRateLimitOutMaxBandWidth_Type = Unsigned32
_QtechIfRateLimitOutMaxBandWidth_Object = MibTableColumn
qtechIfRateLimitOutMaxBandWidth = _QtechIfRateLimitOutMaxBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 11, 1, 4),
    _QtechIfRateLimitOutMaxBandWidth_Type()
)
qtechIfRateLimitOutMaxBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfRateLimitOutMaxBandWidth.setStatus("current")
_QtechIfRateLimitOutBurstFlowLimit_Type = Integer32
_QtechIfRateLimitOutBurstFlowLimit_Object = MibTableColumn
qtechIfRateLimitOutBurstFlowLimit = _QtechIfRateLimitOutBurstFlowLimit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 11, 1, 5),
    _QtechIfRateLimitOutBurstFlowLimit_Type()
)
qtechIfRateLimitOutBurstFlowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfRateLimitOutBurstFlowLimit.setStatus("current")
_QtechIfQueueSupportTable_Object = MibTable
qtechIfQueueSupportTable = _QtechIfQueueSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 12)
)
if mibBuilder.loadTexts:
    qtechIfQueueSupportTable.setStatus("current")
_QtechIfQueueSupportEntry_Object = MibTableRow
qtechIfQueueSupportEntry = _QtechIfQueueSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 12, 1)
)
qtechIfQueueSupportEntry.setIndexNames(
    (0, "QTECH-QOS-MIB", "qtechIfIndex"),
    (0, "QTECH-QOS-MIB", "qtechIfQueueIndex"),
)
if mibBuilder.loadTexts:
    qtechIfQueueSupportEntry.setStatus("current")
_QtechIfIndex_Type = IfIndex
_QtechIfIndex_Object = MibTableColumn
qtechIfIndex = _QtechIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 12, 1, 1),
    _QtechIfIndex_Type()
)
qtechIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfIndex.setStatus("current")
_QtechIfQueueIndex_Type = Integer32
_QtechIfQueueIndex_Object = MibTableColumn
qtechIfQueueIndex = _QtechIfQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 12, 1, 2),
    _QtechIfQueueIndex_Type()
)
qtechIfQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQueueIndex.setStatus("current")
_QtechIfQueueSupportTransmitPacket_Type = Counter64
_QtechIfQueueSupportTransmitPacket_Object = MibTableColumn
qtechIfQueueSupportTransmitPacket = _QtechIfQueueSupportTransmitPacket_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 12, 1, 3),
    _QtechIfQueueSupportTransmitPacket_Type()
)
qtechIfQueueSupportTransmitPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQueueSupportTransmitPacket.setStatus("current")
_QtechIfQueueSupportTransmitBytes_Type = Counter64
_QtechIfQueueSupportTransmitBytes_Object = MibTableColumn
qtechIfQueueSupportTransmitBytes = _QtechIfQueueSupportTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 12, 1, 4),
    _QtechIfQueueSupportTransmitBytes_Type()
)
qtechIfQueueSupportTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQueueSupportTransmitBytes.setStatus("current")
_QtechIfQueueSupportDropPacket_Type = Counter64
_QtechIfQueueSupportDropPacket_Object = MibTableColumn
qtechIfQueueSupportDropPacket = _QtechIfQueueSupportDropPacket_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 12, 1, 5),
    _QtechIfQueueSupportDropPacket_Type()
)
qtechIfQueueSupportDropPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQueueSupportDropPacket.setStatus("current")
_QtechIfQueueSupportDropBytes_Type = Counter64
_QtechIfQueueSupportDropBytes_Object = MibTableColumn
qtechIfQueueSupportDropBytes = _QtechIfQueueSupportDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 12, 1, 6),
    _QtechIfQueueSupportDropBytes_Type()
)
qtechIfQueueSupportDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfQueueSupportDropBytes.setStatus("current")
_QtechIfMulticastQueueSupportTable_Object = MibTable
qtechIfMulticastQueueSupportTable = _QtechIfMulticastQueueSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 13)
)
if mibBuilder.loadTexts:
    qtechIfMulticastQueueSupportTable.setStatus("current")
_QtechIfMulticastQueueSupportEntry_Object = MibTableRow
qtechIfMulticastQueueSupportEntry = _QtechIfMulticastQueueSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 13, 1)
)
qtechIfMulticastQueueSupportEntry.setIndexNames(
    (0, "QTECH-QOS-MIB", "qtechIfIndexMulticast"),
    (0, "QTECH-QOS-MIB", "qtechIfMulticastQueueIndex"),
)
if mibBuilder.loadTexts:
    qtechIfMulticastQueueSupportEntry.setStatus("current")
_QtechIfIndexMulticast_Type = IfIndex
_QtechIfIndexMulticast_Object = MibTableColumn
qtechIfIndexMulticast = _QtechIfIndexMulticast_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 13, 1, 1),
    _QtechIfIndexMulticast_Type()
)
qtechIfIndexMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfIndexMulticast.setStatus("current")
_QtechIfMulticastQueueIndex_Type = Integer32
_QtechIfMulticastQueueIndex_Object = MibTableColumn
qtechIfMulticastQueueIndex = _QtechIfMulticastQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 13, 1, 2),
    _QtechIfMulticastQueueIndex_Type()
)
qtechIfMulticastQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfMulticastQueueIndex.setStatus("current")
_QtechIfMulticastQueueSupportTransmitPacket_Type = Counter64
_QtechIfMulticastQueueSupportTransmitPacket_Object = MibTableColumn
qtechIfMulticastQueueSupportTransmitPacket = _QtechIfMulticastQueueSupportTransmitPacket_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 13, 1, 3),
    _QtechIfMulticastQueueSupportTransmitPacket_Type()
)
qtechIfMulticastQueueSupportTransmitPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfMulticastQueueSupportTransmitPacket.setStatus("current")
_QtechIfMulticastQueueSupportTransmitBytes_Type = Counter64
_QtechIfMulticastQueueSupportTransmitBytes_Object = MibTableColumn
qtechIfMulticastQueueSupportTransmitBytes = _QtechIfMulticastQueueSupportTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 13, 1, 4),
    _QtechIfMulticastQueueSupportTransmitBytes_Type()
)
qtechIfMulticastQueueSupportTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfMulticastQueueSupportTransmitBytes.setStatus("current")
_QtechIfMulticastQueueSupportDropPacket_Type = Counter64
_QtechIfMulticastQueueSupportDropPacket_Object = MibTableColumn
qtechIfMulticastQueueSupportDropPacket = _QtechIfMulticastQueueSupportDropPacket_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 13, 1, 5),
    _QtechIfMulticastQueueSupportDropPacket_Type()
)
qtechIfMulticastQueueSupportDropPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfMulticastQueueSupportDropPacket.setStatus("current")
_QtechIfMulticastQueueSupportDropBytes_Type = Counter64
_QtechIfMulticastQueueSupportDropBytes_Object = MibTableColumn
qtechIfMulticastQueueSupportDropBytes = _QtechIfMulticastQueueSupportDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 1, 13, 1, 6),
    _QtechIfMulticastQueueSupportDropBytes_Type()
)
qtechIfMulticastQueueSupportDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIfMulticastQueueSupportDropBytes.setStatus("current")
_QtechQoSTrafficClassMIBObjects_ObjectIdentity = ObjectIdentity
qtechQoSTrafficClassMIBObjects = _QtechQoSTrafficClassMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2)
)
_QtechQoSTrafficClassTable_Object = MibTable
qtechQoSTrafficClassTable = _QtechQoSTrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 1)
)
if mibBuilder.loadTexts:
    qtechQoSTrafficClassTable.setStatus("current")
_QtechQoSTrafficClassEntry_Object = MibTableRow
qtechQoSTrafficClassEntry = _QtechQoSTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 1, 1)
)
qtechQoSTrafficClassEntry.setIndexNames(
    (0, "QTECH-QOS-MIB", "qtechQosClassMapName"),
)
if mibBuilder.loadTexts:
    qtechQoSTrafficClassEntry.setStatus("current")


class _QtechQosClassMapName_Type(DisplayString):
    """Custom type qtechQosClassMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechQosClassMapName_Type.__name__ = "DisplayString"
_QtechQosClassMapName_Object = MibTableColumn
qtechQosClassMapName = _QtechQosClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 1, 1, 1),
    _QtechQosClassMapName_Type()
)
qtechQosClassMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQosClassMapName.setStatus("current")


class _QtechQosClassAclName_Type(DisplayString):
    """Custom type qtechQosClassAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechQosClassAclName_Type.__name__ = "DisplayString"
_QtechQosClassAclName_Object = MibTableColumn
qtechQosClassAclName = _QtechQosClassAclName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 1, 1, 2),
    _QtechQosClassAclName_Type()
)
qtechQosClassAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechQosClassAclName.setStatus("current")
_QtechQosClassMapEntryStatus_Type = ConfigStatus
_QtechQosClassMapEntryStatus_Object = MibTableColumn
qtechQosClassMapEntryStatus = _QtechQosClassMapEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 1, 1, 3),
    _QtechQosClassMapEntryStatus_Type()
)
qtechQosClassMapEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechQosClassMapEntryStatus.setStatus("current")
_QtechQoSPoliceMapTable_Object = MibTable
qtechQoSPoliceMapTable = _QtechQoSPoliceMapTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 2)
)
if mibBuilder.loadTexts:
    qtechQoSPoliceMapTable.setStatus("current")
_QtechQoSPoliceMapEntry_Object = MibTableRow
qtechQoSPoliceMapEntry = _QtechQoSPoliceMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 2, 1)
)
qtechQoSPoliceMapEntry.setIndexNames(
    (0, "QTECH-QOS-MIB", "qtechQosPoliceMapName"),
)
if mibBuilder.loadTexts:
    qtechQoSPoliceMapEntry.setStatus("current")


class _QtechQosPoliceMapName_Type(DisplayString):
    """Custom type qtechQosPoliceMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechQosPoliceMapName_Type.__name__ = "DisplayString"
_QtechQosPoliceMapName_Object = MibTableColumn
qtechQosPoliceMapName = _QtechQosPoliceMapName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 2, 1, 1),
    _QtechQosPoliceMapName_Type()
)
qtechQosPoliceMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQosPoliceMapName.setStatus("current")
_QtechQosPoliceMapEntryStatus_Type = ConfigStatus
_QtechQosPoliceMapEntryStatus_Object = MibTableColumn
qtechQosPoliceMapEntryStatus = _QtechQosPoliceMapEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 2, 1, 2),
    _QtechQosPoliceMapEntryStatus_Type()
)
qtechQosPoliceMapEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechQosPoliceMapEntryStatus.setStatus("current")
_QtechQoSPoliceMapConfTable_Object = MibTable
qtechQoSPoliceMapConfTable = _QtechQoSPoliceMapConfTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 3)
)
if mibBuilder.loadTexts:
    qtechQoSPoliceMapConfTable.setStatus("current")
_QtechQoSPoliceMapConfEntry_Object = MibTableRow
qtechQoSPoliceMapConfEntry = _QtechQoSPoliceMapConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 3, 1)
)
qtechQoSPoliceMapConfEntry.setIndexNames(
    (0, "QTECH-QOS-MIB", "qtechQoSPoliceCfgPoliceMapName"),
    (0, "QTECH-QOS-MIB", "qtechQoSPoliceCfgClassMapName"),
)
if mibBuilder.loadTexts:
    qtechQoSPoliceMapConfEntry.setStatus("current")


class _QtechQoSPoliceCfgPoliceMapName_Type(DisplayString):
    """Custom type qtechQoSPoliceCfgPoliceMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechQoSPoliceCfgPoliceMapName_Type.__name__ = "DisplayString"
_QtechQoSPoliceCfgPoliceMapName_Object = MibTableColumn
qtechQoSPoliceCfgPoliceMapName = _QtechQoSPoliceCfgPoliceMapName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 3, 1, 1),
    _QtechQoSPoliceCfgPoliceMapName_Type()
)
qtechQoSPoliceCfgPoliceMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQoSPoliceCfgPoliceMapName.setStatus("current")


class _QtechQoSPoliceCfgClassMapName_Type(DisplayString):
    """Custom type qtechQoSPoliceCfgClassMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechQoSPoliceCfgClassMapName_Type.__name__ = "DisplayString"
_QtechQoSPoliceCfgClassMapName_Object = MibTableColumn
qtechQoSPoliceCfgClassMapName = _QtechQoSPoliceCfgClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 3, 1, 2),
    _QtechQoSPoliceCfgClassMapName_Type()
)
qtechQoSPoliceCfgClassMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechQoSPoliceCfgClassMapName.setStatus("current")
_QtechQoSPoliceMapConfMaxBandWidth_Type = Unsigned32
_QtechQoSPoliceMapConfMaxBandWidth_Object = MibTableColumn
qtechQoSPoliceMapConfMaxBandWidth = _QtechQoSPoliceMapConfMaxBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 3, 1, 3),
    _QtechQoSPoliceMapConfMaxBandWidth_Type()
)
qtechQoSPoliceMapConfMaxBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechQoSPoliceMapConfMaxBandWidth.setStatus("current")
_QtechQoSPoliceMapConfBurstFlowLimit_Type = Integer32
_QtechQoSPoliceMapConfBurstFlowLimit_Object = MibTableColumn
qtechQoSPoliceMapConfBurstFlowLimit = _QtechQoSPoliceMapConfBurstFlowLimit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 3, 1, 4),
    _QtechQoSPoliceMapConfBurstFlowLimit_Type()
)
qtechQoSPoliceMapConfBurstFlowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechQoSPoliceMapConfBurstFlowLimit.setStatus("current")


class _QtechQoSPoliceMapConfExceedAction_Type(Integer32):
    """Custom type qtechQoSPoliceMapConfExceedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("modify-dscp", 2))
    )


_QtechQoSPoliceMapConfExceedAction_Type.__name__ = "Integer32"
_QtechQoSPoliceMapConfExceedAction_Object = MibTableColumn
qtechQoSPoliceMapConfExceedAction = _QtechQoSPoliceMapConfExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 3, 1, 5),
    _QtechQoSPoliceMapConfExceedAction_Type()
)
qtechQoSPoliceMapConfExceedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechQoSPoliceMapConfExceedAction.setStatus("current")
_QtechQoSPoliceMapConfExceedDscp_Type = Integer32
_QtechQoSPoliceMapConfExceedDscp_Object = MibTableColumn
qtechQoSPoliceMapConfExceedDscp = _QtechQoSPoliceMapConfExceedDscp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 3, 1, 6),
    _QtechQoSPoliceMapConfExceedDscp_Type()
)
qtechQoSPoliceMapConfExceedDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechQoSPoliceMapConfExceedDscp.setStatus("current")
_QtechQoSPoliceMapConfNewDscp_Type = Integer32
_QtechQoSPoliceMapConfNewDscp_Object = MibTableColumn
qtechQoSPoliceMapConfNewDscp = _QtechQoSPoliceMapConfNewDscp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 3, 1, 7),
    _QtechQoSPoliceMapConfNewDscp_Type()
)
qtechQoSPoliceMapConfNewDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechQoSPoliceMapConfNewDscp.setStatus("current")
_QtechQoSPoliceMapCfgEntryStatus_Type = ConfigStatus
_QtechQoSPoliceMapCfgEntryStatus_Object = MibTableColumn
qtechQoSPoliceMapCfgEntryStatus = _QtechQoSPoliceMapCfgEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 3, 1, 8),
    _QtechQoSPoliceMapCfgEntryStatus_Type()
)
qtechQoSPoliceMapCfgEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechQoSPoliceMapCfgEntryStatus.setStatus("current")
_QtechQoSPoliceMapConfMaxHighBandWidth_Type = Unsigned32
_QtechQoSPoliceMapConfMaxHighBandWidth_Object = MibTableColumn
qtechQoSPoliceMapConfMaxHighBandWidth = _QtechQoSPoliceMapConfMaxHighBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 3, 1, 9),
    _QtechQoSPoliceMapConfMaxHighBandWidth_Type()
)
qtechQoSPoliceMapConfMaxHighBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechQoSPoliceMapConfMaxHighBandWidth.setStatus("current")
_QtechQosPoliceIfExtTable_Object = MibTable
qtechQosPoliceIfExtTable = _QtechQosPoliceIfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 5)
)
if mibBuilder.loadTexts:
    qtechQosPoliceIfExtTable.setStatus("current")
_QtechQosPoliceIfExtEntry_Object = MibTableRow
qtechQosPoliceIfExtEntry = _QtechQosPoliceIfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 5, 1)
)
qtechQosPoliceIfExtEntry.setIndexNames(
    (0, "QTECH-QOS-MIB", "qtechQosPoliceIfIndex"),
)
if mibBuilder.loadTexts:
    qtechQosPoliceIfExtEntry.setStatus("current")
_QtechQosPoliceIfIndex_Type = IfIndex
_QtechQosPoliceIfIndex_Object = MibTableColumn
qtechQosPoliceIfIndex = _QtechQosPoliceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 5, 1, 1),
    _QtechQosPoliceIfIndex_Type()
)
qtechQosPoliceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechQosPoliceIfIndex.setStatus("current")


class _QtechIfInPoliceMapName_Type(DisplayString):
    """Custom type qtechIfInPoliceMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechIfInPoliceMapName_Type.__name__ = "DisplayString"
_QtechIfInPoliceMapName_Object = MibTableColumn
qtechIfInPoliceMapName = _QtechIfInPoliceMapName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 5, 1, 2),
    _QtechIfInPoliceMapName_Type()
)
qtechIfInPoliceMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfInPoliceMapName.setStatus("current")


class _QtechIfOutPoliceMapName_Type(DisplayString):
    """Custom type qtechIfOutPoliceMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechIfOutPoliceMapName_Type.__name__ = "DisplayString"
_QtechIfOutPoliceMapName_Object = MibTableColumn
qtechIfOutPoliceMapName = _QtechIfOutPoliceMapName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 2, 5, 1, 3),
    _QtechIfOutPoliceMapName_Type()
)
qtechIfOutPoliceMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfOutPoliceMapName.setStatus("current")
_QtechQoSMIBConformance_ObjectIdentity = ObjectIdentity
qtechQoSMIBConformance = _QtechQoSMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 3)
)
_QtechQoSMIBCompliances_ObjectIdentity = ObjectIdentity
qtechQoSMIBCompliances = _QtechQoSMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 3, 1)
)
_QtechQoSMIBGroups_ObjectIdentity = ObjectIdentity
qtechQoSMIBGroups = _QtechQoSMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 3, 2)
)

# Managed Objects groups

qtechQoSPriorityMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 3, 2, 1)
)
qtechQoSPriorityMIBGroup.setObjects(
      *(("QTECH-QOS-MIB", "qtechQoSGlobalStatus"),
        ("QTECH-QOS-MIB", "qtechPriorityTrafficClassNum"),
        ("QTECH-QOS-MIB", "qtechPriorityClassNum"),
        ("QTECH-QOS-MIB", "qtechPriorityDscpMaxValue"),
        ("QTECH-QOS-MIB", "qtechTrafficClassPriority"),
        ("QTECH-QOS-MIB", "qtechTrafficClass"),
        ("QTECH-QOS-MIB", "qtechPriorityToDscp"),
        ("QTECH-QOS-MIB", "qtechDscpClass"),
        ("QTECH-QOS-MIB", "qtechDscpTrafficClassPriority"),
        ("QTECH-QOS-MIB", "qtechPriorityTrafficClassOperMode"),
        ("QTECH-QOS-MIB", "qtechPriorityBandWidth"),
        ("QTECH-QOS-MIB", "qtechIfPriorityIfIndex"),
        ("QTECH-QOS-MIB", "qtechIfPriority"),
        ("QTECH-QOS-MIB", "qtechIfPriTrafficClassOperMode"),
        ("QTECH-QOS-MIB", "qtechIfPriorityBandwidth"),
        ("QTECH-QOS-MIB", "qtechIfPriorityQosTrustMode"),
        ("QTECH-QOS-MIB", "qtechIpPreClassPriority"),
        ("QTECH-QOS-MIB", "qtechIpPreToDscp"))
)
if mibBuilder.loadTexts:
    qtechQoSPriorityMIBGroup.setStatus("current")

qtechQoSTrafficClassMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 3, 2, 2)
)
qtechQoSTrafficClassMIBGroup.setObjects(
      *(("QTECH-QOS-MIB", "qtechQosClassMapName"),
        ("QTECH-QOS-MIB", "qtechQosClassAclName"),
        ("QTECH-QOS-MIB", "qtechQosClassMapEntryStatus"),
        ("QTECH-QOS-MIB", "qtechQosPoliceMapName"),
        ("QTECH-QOS-MIB", "qtechQosPoliceMapEntryStatus"),
        ("QTECH-QOS-MIB", "qtechQoSPoliceCfgPoliceMapName"),
        ("QTECH-QOS-MIB", "qtechQoSPoliceCfgClassMapName"),
        ("QTECH-QOS-MIB", "qtechQoSPoliceMapConfMaxBandWidth"),
        ("QTECH-QOS-MIB", "qtechQoSPoliceMapConfExceedAction"),
        ("QTECH-QOS-MIB", "qtechQoSPoliceMapConfExceedDscp"),
        ("QTECH-QOS-MIB", "qtechQoSPoliceMapConfNewDscp"),
        ("QTECH-QOS-MIB", "qtechQoSPoliceMapCfgEntryStatus"),
        ("QTECH-QOS-MIB", "qtechQoSPoliceMapConfMaxHighBandWidth"),
        ("QTECH-QOS-MIB", "qtechQosPoliceIfIndex"),
        ("QTECH-QOS-MIB", "qtechIfInPoliceMapName"),
        ("QTECH-QOS-MIB", "qtechIfOutPoliceMapName"))
)
if mibBuilder.loadTexts:
    qtechQoSTrafficClassMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechQoSMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 18, 3, 1, 1)
)
qtechQoSMIBCompliance.setObjects(
      *(("QTECH-QOS-MIB", "qtechQoSPriorityMIBGroup"),
        ("QTECH-QOS-MIB", "qtechQoSTrafficClassMIBGroup"))
)
if mibBuilder.loadTexts:
    qtechQoSMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-QOS-MIB",
    **{"qtechQoSMIB": qtechQoSMIB,
       "qtechQoSPriorityMIBObjects": qtechQoSPriorityMIBObjects,
       "qtechQoSGlobalStatus": qtechQoSGlobalStatus,
       "qtechPriorityTrafficClassNum": qtechPriorityTrafficClassNum,
       "qtechPriorityClassNum": qtechPriorityClassNum,
       "qtechPriorityDscpMaxValue": qtechPriorityDscpMaxValue,
       "qtechTrafficClassTable": qtechTrafficClassTable,
       "qtechTrafficClassEntry": qtechTrafficClassEntry,
       "qtechTrafficClassPriority": qtechTrafficClassPriority,
       "qtechTrafficClass": qtechTrafficClass,
       "qtechPriorityToDscp": qtechPriorityToDscp,
       "qtechDscpClassTable": qtechDscpClassTable,
       "qtechDscpClassEntry": qtechDscpClassEntry,
       "qtechDscpClass": qtechDscpClass,
       "qtechDscpTrafficClassPriority": qtechDscpTrafficClassPriority,
       "qtechPriorityTrafficClassOperMode": qtechPriorityTrafficClassOperMode,
       "qtechPriorityBandWidth": qtechPriorityBandWidth,
       "qtechIfPriorityTable": qtechIfPriorityTable,
       "qtechIfPriorityEntry": qtechIfPriorityEntry,
       "qtechIfPriorityIfIndex": qtechIfPriorityIfIndex,
       "qtechIfPriority": qtechIfPriority,
       "qtechIfPriTrafficClassOperMode": qtechIfPriTrafficClassOperMode,
       "qtechIfPriorityBandwidth": qtechIfPriorityBandwidth,
       "qtechIfPriorityQosTrustMode": qtechIfPriorityQosTrustMode,
       "qtechIpPreClassTable": qtechIpPreClassTable,
       "qtechIpPreClassEntry": qtechIpPreClassEntry,
       "qtechIpPreClassPriority": qtechIpPreClassPriority,
       "qtechIpPreToDscp": qtechIpPreToDscp,
       "qtechIfRateLimitTable": qtechIfRateLimitTable,
       "qtechIfRateLimitEntry": qtechIfRateLimitEntry,
       "qtechIfRateLimitIndex": qtechIfRateLimitIndex,
       "qtechIfRateLimitInMaxBandWidth": qtechIfRateLimitInMaxBandWidth,
       "qtechIfRateLimitInBurstFlowLimit": qtechIfRateLimitInBurstFlowLimit,
       "qtechIfRateLimitOutMaxBandWidth": qtechIfRateLimitOutMaxBandWidth,
       "qtechIfRateLimitOutBurstFlowLimit": qtechIfRateLimitOutBurstFlowLimit,
       "qtechIfQueueSupportTable": qtechIfQueueSupportTable,
       "qtechIfQueueSupportEntry": qtechIfQueueSupportEntry,
       "qtechIfIndex": qtechIfIndex,
       "qtechIfQueueIndex": qtechIfQueueIndex,
       "qtechIfQueueSupportTransmitPacket": qtechIfQueueSupportTransmitPacket,
       "qtechIfQueueSupportTransmitBytes": qtechIfQueueSupportTransmitBytes,
       "qtechIfQueueSupportDropPacket": qtechIfQueueSupportDropPacket,
       "qtechIfQueueSupportDropBytes": qtechIfQueueSupportDropBytes,
       "qtechIfMulticastQueueSupportTable": qtechIfMulticastQueueSupportTable,
       "qtechIfMulticastQueueSupportEntry": qtechIfMulticastQueueSupportEntry,
       "qtechIfIndexMulticast": qtechIfIndexMulticast,
       "qtechIfMulticastQueueIndex": qtechIfMulticastQueueIndex,
       "qtechIfMulticastQueueSupportTransmitPacket": qtechIfMulticastQueueSupportTransmitPacket,
       "qtechIfMulticastQueueSupportTransmitBytes": qtechIfMulticastQueueSupportTransmitBytes,
       "qtechIfMulticastQueueSupportDropPacket": qtechIfMulticastQueueSupportDropPacket,
       "qtechIfMulticastQueueSupportDropBytes": qtechIfMulticastQueueSupportDropBytes,
       "qtechQoSTrafficClassMIBObjects": qtechQoSTrafficClassMIBObjects,
       "qtechQoSTrafficClassTable": qtechQoSTrafficClassTable,
       "qtechQoSTrafficClassEntry": qtechQoSTrafficClassEntry,
       "qtechQosClassMapName": qtechQosClassMapName,
       "qtechQosClassAclName": qtechQosClassAclName,
       "qtechQosClassMapEntryStatus": qtechQosClassMapEntryStatus,
       "qtechQoSPoliceMapTable": qtechQoSPoliceMapTable,
       "qtechQoSPoliceMapEntry": qtechQoSPoliceMapEntry,
       "qtechQosPoliceMapName": qtechQosPoliceMapName,
       "qtechQosPoliceMapEntryStatus": qtechQosPoliceMapEntryStatus,
       "qtechQoSPoliceMapConfTable": qtechQoSPoliceMapConfTable,
       "qtechQoSPoliceMapConfEntry": qtechQoSPoliceMapConfEntry,
       "qtechQoSPoliceCfgPoliceMapName": qtechQoSPoliceCfgPoliceMapName,
       "qtechQoSPoliceCfgClassMapName": qtechQoSPoliceCfgClassMapName,
       "qtechQoSPoliceMapConfMaxBandWidth": qtechQoSPoliceMapConfMaxBandWidth,
       "qtechQoSPoliceMapConfBurstFlowLimit": qtechQoSPoliceMapConfBurstFlowLimit,
       "qtechQoSPoliceMapConfExceedAction": qtechQoSPoliceMapConfExceedAction,
       "qtechQoSPoliceMapConfExceedDscp": qtechQoSPoliceMapConfExceedDscp,
       "qtechQoSPoliceMapConfNewDscp": qtechQoSPoliceMapConfNewDscp,
       "qtechQoSPoliceMapCfgEntryStatus": qtechQoSPoliceMapCfgEntryStatus,
       "qtechQoSPoliceMapConfMaxHighBandWidth": qtechQoSPoliceMapConfMaxHighBandWidth,
       "qtechQosPoliceIfExtTable": qtechQosPoliceIfExtTable,
       "qtechQosPoliceIfExtEntry": qtechQosPoliceIfExtEntry,
       "qtechQosPoliceIfIndex": qtechQosPoliceIfIndex,
       "qtechIfInPoliceMapName": qtechIfInPoliceMapName,
       "qtechIfOutPoliceMapName": qtechIfOutPoliceMapName,
       "qtechQoSMIBConformance": qtechQoSMIBConformance,
       "qtechQoSMIBCompliances": qtechQoSMIBCompliances,
       "qtechQoSMIBCompliance": qtechQoSMIBCompliance,
       "qtechQoSMIBGroups": qtechQoSMIBGroups,
       "qtechQoSPriorityMIBGroup": qtechQoSPriorityMIBGroup,
       "qtechQoSTrafficClassMIBGroup": qtechQoSTrafficClassMIBGroup}
)
