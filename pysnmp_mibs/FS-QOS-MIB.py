# SNMP MIB module (FS-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-QOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:17 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "FS-TC",
    "ConfigStatus",
    "IfIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

fsQoSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18)
)
if mibBuilder.loadTexts:
    fsQoSMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsQoSPriorityMIBObjects_ObjectIdentity = ObjectIdentity
fsQoSPriorityMIBObjects = _FsQoSPriorityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1)
)
_FsQoSGlobalStatus_Type = EnabledStatus
_FsQoSGlobalStatus_Object = MibScalar
fsQoSGlobalStatus = _FsQoSGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 1),
    _FsQoSGlobalStatus_Type()
)
fsQoSGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsQoSGlobalStatus.setStatus("current")
_FsPriorityTrafficClassNum_Type = Integer32
_FsPriorityTrafficClassNum_Object = MibScalar
fsPriorityTrafficClassNum = _FsPriorityTrafficClassNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 2),
    _FsPriorityTrafficClassNum_Type()
)
fsPriorityTrafficClassNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPriorityTrafficClassNum.setStatus("current")
_FsPriorityClassNum_Type = Integer32
_FsPriorityClassNum_Object = MibScalar
fsPriorityClassNum = _FsPriorityClassNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 3),
    _FsPriorityClassNum_Type()
)
fsPriorityClassNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPriorityClassNum.setStatus("current")
_FsPriorityDscpMaxValue_Type = Integer32
_FsPriorityDscpMaxValue_Object = MibScalar
fsPriorityDscpMaxValue = _FsPriorityDscpMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 4),
    _FsPriorityDscpMaxValue_Type()
)
fsPriorityDscpMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPriorityDscpMaxValue.setStatus("current")
_FsTrafficClassTable_Object = MibTable
fsTrafficClassTable = _FsTrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 5)
)
if mibBuilder.loadTexts:
    fsTrafficClassTable.setStatus("current")
_FsTrafficClassEntry_Object = MibTableRow
fsTrafficClassEntry = _FsTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 5, 1)
)
fsTrafficClassEntry.setIndexNames(
    (0, "FS-QOS-MIB", "fsTrafficClassPriority"),
)
if mibBuilder.loadTexts:
    fsTrafficClassEntry.setStatus("current")
_FsTrafficClassPriority_Type = Integer32
_FsTrafficClassPriority_Object = MibTableColumn
fsTrafficClassPriority = _FsTrafficClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 5, 1, 1),
    _FsTrafficClassPriority_Type()
)
fsTrafficClassPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTrafficClassPriority.setStatus("current")
_FsTrafficClass_Type = Integer32
_FsTrafficClass_Object = MibTableColumn
fsTrafficClass = _FsTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 5, 1, 2),
    _FsTrafficClass_Type()
)
fsTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTrafficClass.setStatus("current")
_FsPriorityToDscp_Type = Integer32
_FsPriorityToDscp_Object = MibTableColumn
fsPriorityToDscp = _FsPriorityToDscp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 5, 1, 3),
    _FsPriorityToDscp_Type()
)
fsPriorityToDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPriorityToDscp.setStatus("current")
_FsDscpClassTable_Object = MibTable
fsDscpClassTable = _FsDscpClassTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 6)
)
if mibBuilder.loadTexts:
    fsDscpClassTable.setStatus("current")
_FsDscpClassEntry_Object = MibTableRow
fsDscpClassEntry = _FsDscpClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 6, 1)
)
fsDscpClassEntry.setIndexNames(
    (0, "FS-QOS-MIB", "fsDscpClass"),
)
if mibBuilder.loadTexts:
    fsDscpClassEntry.setStatus("current")
_FsDscpClass_Type = Integer32
_FsDscpClass_Object = MibTableColumn
fsDscpClass = _FsDscpClass_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 6, 1, 1),
    _FsDscpClass_Type()
)
fsDscpClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDscpClass.setStatus("current")
_FsDscpTrafficClassPriority_Type = Integer32
_FsDscpTrafficClassPriority_Object = MibTableColumn
fsDscpTrafficClassPriority = _FsDscpTrafficClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 6, 1, 2),
    _FsDscpTrafficClassPriority_Type()
)
fsDscpTrafficClassPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDscpTrafficClassPriority.setStatus("current")


class _FsPriorityTrafficClassOperMode_Type(Integer32):
    """Custom type fsPriorityTrafficClassOperMode based on Integer32"""
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


_FsPriorityTrafficClassOperMode_Type.__name__ = "Integer32"
_FsPriorityTrafficClassOperMode_Object = MibScalar
fsPriorityTrafficClassOperMode = _FsPriorityTrafficClassOperMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 7),
    _FsPriorityTrafficClassOperMode_Type()
)
fsPriorityTrafficClassOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPriorityTrafficClassOperMode.setStatus("current")
_FsPriorityBandWidth_Type = OctetString
_FsPriorityBandWidth_Object = MibScalar
fsPriorityBandWidth = _FsPriorityBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 8),
    _FsPriorityBandWidth_Type()
)
fsPriorityBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPriorityBandWidth.setStatus("current")
_FsIfPriorityTable_Object = MibTable
fsIfPriorityTable = _FsIfPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 9)
)
if mibBuilder.loadTexts:
    fsIfPriorityTable.setStatus("current")
_FsIfPriorityEntry_Object = MibTableRow
fsIfPriorityEntry = _FsIfPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 9, 1)
)
fsIfPriorityEntry.setIndexNames(
    (0, "FS-QOS-MIB", "fsIfPriorityIfIndex"),
)
if mibBuilder.loadTexts:
    fsIfPriorityEntry.setStatus("current")
_FsIfPriorityIfIndex_Type = IfIndex
_FsIfPriorityIfIndex_Object = MibTableColumn
fsIfPriorityIfIndex = _FsIfPriorityIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 9, 1, 1),
    _FsIfPriorityIfIndex_Type()
)
fsIfPriorityIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfPriorityIfIndex.setStatus("current")
_FsIfPriority_Type = Integer32
_FsIfPriority_Object = MibTableColumn
fsIfPriority = _FsIfPriority_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 9, 1, 2),
    _FsIfPriority_Type()
)
fsIfPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfPriority.setStatus("current")


class _FsIfPriTrafficClassOperMode_Type(Integer32):
    """Custom type fsIfPriTrafficClassOperMode based on Integer32"""
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


_FsIfPriTrafficClassOperMode_Type.__name__ = "Integer32"
_FsIfPriTrafficClassOperMode_Object = MibTableColumn
fsIfPriTrafficClassOperMode = _FsIfPriTrafficClassOperMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 9, 1, 3),
    _FsIfPriTrafficClassOperMode_Type()
)
fsIfPriTrafficClassOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfPriTrafficClassOperMode.setStatus("current")
_FsIfPriorityBandwidth_Type = OctetString
_FsIfPriorityBandwidth_Object = MibTableColumn
fsIfPriorityBandwidth = _FsIfPriorityBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 9, 1, 4),
    _FsIfPriorityBandwidth_Type()
)
fsIfPriorityBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfPriorityBandwidth.setStatus("current")


class _FsIfPriorityQosTrustMode_Type(Integer32):
    """Custom type fsIfPriorityQosTrustMode based on Integer32"""
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


_FsIfPriorityQosTrustMode_Type.__name__ = "Integer32"
_FsIfPriorityQosTrustMode_Object = MibTableColumn
fsIfPriorityQosTrustMode = _FsIfPriorityQosTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 9, 1, 5),
    _FsIfPriorityQosTrustMode_Type()
)
fsIfPriorityQosTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfPriorityQosTrustMode.setStatus("current")
_FsIpPreClassTable_Object = MibTable
fsIpPreClassTable = _FsIpPreClassTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 10)
)
if mibBuilder.loadTexts:
    fsIpPreClassTable.setStatus("current")
_FsIpPreClassEntry_Object = MibTableRow
fsIpPreClassEntry = _FsIpPreClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 10, 1)
)
fsIpPreClassEntry.setIndexNames(
    (0, "FS-QOS-MIB", "fsIpPreClassPriority"),
)
if mibBuilder.loadTexts:
    fsIpPreClassEntry.setStatus("current")
_FsIpPreClassPriority_Type = Integer32
_FsIpPreClassPriority_Object = MibTableColumn
fsIpPreClassPriority = _FsIpPreClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 10, 1, 1),
    _FsIpPreClassPriority_Type()
)
fsIpPreClassPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpPreClassPriority.setStatus("current")
_FsIpPreToDscp_Type = Integer32
_FsIpPreToDscp_Object = MibTableColumn
fsIpPreToDscp = _FsIpPreToDscp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 10, 1, 2),
    _FsIpPreToDscp_Type()
)
fsIpPreToDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpPreToDscp.setStatus("current")
_FsIfRateLimitTable_Object = MibTable
fsIfRateLimitTable = _FsIfRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 11)
)
if mibBuilder.loadTexts:
    fsIfRateLimitTable.setStatus("current")
_FsIfRateLimitEntry_Object = MibTableRow
fsIfRateLimitEntry = _FsIfRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 11, 1)
)
fsIfRateLimitEntry.setIndexNames(
    (0, "FS-QOS-MIB", "fsIfRateLimitIndex"),
)
if mibBuilder.loadTexts:
    fsIfRateLimitEntry.setStatus("current")
_FsIfRateLimitIndex_Type = IfIndex
_FsIfRateLimitIndex_Object = MibTableColumn
fsIfRateLimitIndex = _FsIfRateLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 11, 1, 1),
    _FsIfRateLimitIndex_Type()
)
fsIfRateLimitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfRateLimitIndex.setStatus("current")
_FsIfRateLimitInMaxBandWidth_Type = Unsigned32
_FsIfRateLimitInMaxBandWidth_Object = MibTableColumn
fsIfRateLimitInMaxBandWidth = _FsIfRateLimitInMaxBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 11, 1, 2),
    _FsIfRateLimitInMaxBandWidth_Type()
)
fsIfRateLimitInMaxBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfRateLimitInMaxBandWidth.setStatus("current")
_FsIfRateLimitInBurstFlowLimit_Type = Integer32
_FsIfRateLimitInBurstFlowLimit_Object = MibTableColumn
fsIfRateLimitInBurstFlowLimit = _FsIfRateLimitInBurstFlowLimit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 11, 1, 3),
    _FsIfRateLimitInBurstFlowLimit_Type()
)
fsIfRateLimitInBurstFlowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfRateLimitInBurstFlowLimit.setStatus("current")
_FsIfRateLimitOutMaxBandWidth_Type = Unsigned32
_FsIfRateLimitOutMaxBandWidth_Object = MibTableColumn
fsIfRateLimitOutMaxBandWidth = _FsIfRateLimitOutMaxBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 11, 1, 4),
    _FsIfRateLimitOutMaxBandWidth_Type()
)
fsIfRateLimitOutMaxBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfRateLimitOutMaxBandWidth.setStatus("current")
_FsIfRateLimitOutBurstFlowLimit_Type = Integer32
_FsIfRateLimitOutBurstFlowLimit_Object = MibTableColumn
fsIfRateLimitOutBurstFlowLimit = _FsIfRateLimitOutBurstFlowLimit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 11, 1, 5),
    _FsIfRateLimitOutBurstFlowLimit_Type()
)
fsIfRateLimitOutBurstFlowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfRateLimitOutBurstFlowLimit.setStatus("current")
_FsIfQueueSupportTable_Object = MibTable
fsIfQueueSupportTable = _FsIfQueueSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 12)
)
if mibBuilder.loadTexts:
    fsIfQueueSupportTable.setStatus("current")
_FsIfQueueSupportEntry_Object = MibTableRow
fsIfQueueSupportEntry = _FsIfQueueSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 12, 1)
)
fsIfQueueSupportEntry.setIndexNames(
    (0, "FS-QOS-MIB", "fsIfIndex"),
    (0, "FS-QOS-MIB", "fsIfQueueIndex"),
)
if mibBuilder.loadTexts:
    fsIfQueueSupportEntry.setStatus("current")
_FsIfIndex_Type = IfIndex
_FsIfIndex_Object = MibTableColumn
fsIfIndex = _FsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 12, 1, 1),
    _FsIfIndex_Type()
)
fsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfIndex.setStatus("current")
_FsIfQueueIndex_Type = Integer32
_FsIfQueueIndex_Object = MibTableColumn
fsIfQueueIndex = _FsIfQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 12, 1, 2),
    _FsIfQueueIndex_Type()
)
fsIfQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQueueIndex.setStatus("current")
_FsIfQueueSupportTransmitPacket_Type = Counter64
_FsIfQueueSupportTransmitPacket_Object = MibTableColumn
fsIfQueueSupportTransmitPacket = _FsIfQueueSupportTransmitPacket_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 12, 1, 3),
    _FsIfQueueSupportTransmitPacket_Type()
)
fsIfQueueSupportTransmitPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQueueSupportTransmitPacket.setStatus("current")
_FsIfQueueSupportTransmitBytes_Type = Counter64
_FsIfQueueSupportTransmitBytes_Object = MibTableColumn
fsIfQueueSupportTransmitBytes = _FsIfQueueSupportTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 12, 1, 4),
    _FsIfQueueSupportTransmitBytes_Type()
)
fsIfQueueSupportTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQueueSupportTransmitBytes.setStatus("current")
_FsIfQueueSupportDropPacket_Type = Counter64
_FsIfQueueSupportDropPacket_Object = MibTableColumn
fsIfQueueSupportDropPacket = _FsIfQueueSupportDropPacket_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 12, 1, 5),
    _FsIfQueueSupportDropPacket_Type()
)
fsIfQueueSupportDropPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQueueSupportDropPacket.setStatus("current")
_FsIfQueueSupportDropBytes_Type = Counter64
_FsIfQueueSupportDropBytes_Object = MibTableColumn
fsIfQueueSupportDropBytes = _FsIfQueueSupportDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 12, 1, 6),
    _FsIfQueueSupportDropBytes_Type()
)
fsIfQueueSupportDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfQueueSupportDropBytes.setStatus("current")
_FsIfMulticastQueueSupportTable_Object = MibTable
fsIfMulticastQueueSupportTable = _FsIfMulticastQueueSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 13)
)
if mibBuilder.loadTexts:
    fsIfMulticastQueueSupportTable.setStatus("current")
_FsIfMulticastQueueSupportEntry_Object = MibTableRow
fsIfMulticastQueueSupportEntry = _FsIfMulticastQueueSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 13, 1)
)
fsIfMulticastQueueSupportEntry.setIndexNames(
    (0, "FS-QOS-MIB", "fsIfIndexMulticast"),
    (0, "FS-QOS-MIB", "fsIfMulticastQueueIndex"),
)
if mibBuilder.loadTexts:
    fsIfMulticastQueueSupportEntry.setStatus("current")
_FsIfIndexMulticast_Type = IfIndex
_FsIfIndexMulticast_Object = MibTableColumn
fsIfIndexMulticast = _FsIfIndexMulticast_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 13, 1, 1),
    _FsIfIndexMulticast_Type()
)
fsIfIndexMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfIndexMulticast.setStatus("current")
_FsIfMulticastQueueIndex_Type = Integer32
_FsIfMulticastQueueIndex_Object = MibTableColumn
fsIfMulticastQueueIndex = _FsIfMulticastQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 13, 1, 2),
    _FsIfMulticastQueueIndex_Type()
)
fsIfMulticastQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfMulticastQueueIndex.setStatus("current")
_FsIfMulticastQueueSupportTransmitPacket_Type = Counter64
_FsIfMulticastQueueSupportTransmitPacket_Object = MibTableColumn
fsIfMulticastQueueSupportTransmitPacket = _FsIfMulticastQueueSupportTransmitPacket_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 13, 1, 3),
    _FsIfMulticastQueueSupportTransmitPacket_Type()
)
fsIfMulticastQueueSupportTransmitPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfMulticastQueueSupportTransmitPacket.setStatus("current")
_FsIfMulticastQueueSupportTransmitBytes_Type = Counter64
_FsIfMulticastQueueSupportTransmitBytes_Object = MibTableColumn
fsIfMulticastQueueSupportTransmitBytes = _FsIfMulticastQueueSupportTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 13, 1, 4),
    _FsIfMulticastQueueSupportTransmitBytes_Type()
)
fsIfMulticastQueueSupportTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfMulticastQueueSupportTransmitBytes.setStatus("current")
_FsIfMulticastQueueSupportDropPacket_Type = Counter64
_FsIfMulticastQueueSupportDropPacket_Object = MibTableColumn
fsIfMulticastQueueSupportDropPacket = _FsIfMulticastQueueSupportDropPacket_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 13, 1, 5),
    _FsIfMulticastQueueSupportDropPacket_Type()
)
fsIfMulticastQueueSupportDropPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfMulticastQueueSupportDropPacket.setStatus("current")
_FsIfMulticastQueueSupportDropBytes_Type = Counter64
_FsIfMulticastQueueSupportDropBytes_Object = MibTableColumn
fsIfMulticastQueueSupportDropBytes = _FsIfMulticastQueueSupportDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 13, 1, 6),
    _FsIfMulticastQueueSupportDropBytes_Type()
)
fsIfMulticastQueueSupportDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIfMulticastQueueSupportDropBytes.setStatus("current")
_FsWredEcnStatsTable_Object = MibTable
fsWredEcnStatsTable = _FsWredEcnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 14)
)
if mibBuilder.loadTexts:
    fsWredEcnStatsTable.setStatus("current")
_FsWredEcnStatsEntry_Object = MibTableRow
fsWredEcnStatsEntry = _FsWredEcnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 14, 1)
)
fsWredEcnStatsEntry.setIndexNames(
    (0, "FS-QOS-MIB", "fsWredEcnStatsIfIndex"),
)
if mibBuilder.loadTexts:
    fsWredEcnStatsEntry.setStatus("current")
_FsWredEcnStatsIfIndex_Type = Unsigned32
_FsWredEcnStatsIfIndex_Object = MibTableColumn
fsWredEcnStatsIfIndex = _FsWredEcnStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 14, 1, 1),
    _FsWredEcnStatsIfIndex_Type()
)
fsWredEcnStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWredEcnStatsIfIndex.setStatus("current")


class _FsWredDropped_Type(Counter64):
    """Custom type fsWredDropped based on Counter64"""
    defaultValue = 0


_FsWredDropped_Type.__name__ = "Counter64"
_FsWredDropped_Object = MibTableColumn
fsWredDropped = _FsWredDropped_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 14, 1, 2),
    _FsWredDropped_Type()
)
fsWredDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWredDropped.setStatus("current")


class _FsEcnSended_Type(Counter64):
    """Custom type fsEcnSended based on Counter64"""
    defaultValue = 0


_FsEcnSended_Type.__name__ = "Counter64"
_FsEcnSended_Object = MibTableColumn
fsEcnSended = _FsEcnSended_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 1, 14, 1, 3),
    _FsEcnSended_Type()
)
fsEcnSended.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEcnSended.setStatus("current")
_FsQoSTrafficClassMIBObjects_ObjectIdentity = ObjectIdentity
fsQoSTrafficClassMIBObjects = _FsQoSTrafficClassMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2)
)
_FsQoSTrafficClassTable_Object = MibTable
fsQoSTrafficClassTable = _FsQoSTrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 1)
)
if mibBuilder.loadTexts:
    fsQoSTrafficClassTable.setStatus("current")
_FsQoSTrafficClassEntry_Object = MibTableRow
fsQoSTrafficClassEntry = _FsQoSTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 1, 1)
)
fsQoSTrafficClassEntry.setIndexNames(
    (0, "FS-QOS-MIB", "fsQosClassMapName"),
)
if mibBuilder.loadTexts:
    fsQoSTrafficClassEntry.setStatus("current")


class _FsQosClassMapName_Type(DisplayString):
    """Custom type fsQosClassMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsQosClassMapName_Type.__name__ = "DisplayString"
_FsQosClassMapName_Object = MibTableColumn
fsQosClassMapName = _FsQosClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 1, 1, 1),
    _FsQosClassMapName_Type()
)
fsQosClassMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQosClassMapName.setStatus("current")


class _FsQosClassAclName_Type(DisplayString):
    """Custom type fsQosClassAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsQosClassAclName_Type.__name__ = "DisplayString"
_FsQosClassAclName_Object = MibTableColumn
fsQosClassAclName = _FsQosClassAclName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 1, 1, 2),
    _FsQosClassAclName_Type()
)
fsQosClassAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQosClassAclName.setStatus("current")
_FsQosClassMapEntryStatus_Type = ConfigStatus
_FsQosClassMapEntryStatus_Object = MibTableColumn
fsQosClassMapEntryStatus = _FsQosClassMapEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 1, 1, 3),
    _FsQosClassMapEntryStatus_Type()
)
fsQosClassMapEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQosClassMapEntryStatus.setStatus("current")
_FsQoSPoliceMapTable_Object = MibTable
fsQoSPoliceMapTable = _FsQoSPoliceMapTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 2)
)
if mibBuilder.loadTexts:
    fsQoSPoliceMapTable.setStatus("current")
_FsQoSPoliceMapEntry_Object = MibTableRow
fsQoSPoliceMapEntry = _FsQoSPoliceMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 2, 1)
)
fsQoSPoliceMapEntry.setIndexNames(
    (0, "FS-QOS-MIB", "fsQosPoliceMapName"),
)
if mibBuilder.loadTexts:
    fsQoSPoliceMapEntry.setStatus("current")


class _FsQosPoliceMapName_Type(DisplayString):
    """Custom type fsQosPoliceMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsQosPoliceMapName_Type.__name__ = "DisplayString"
_FsQosPoliceMapName_Object = MibTableColumn
fsQosPoliceMapName = _FsQosPoliceMapName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 2, 1, 1),
    _FsQosPoliceMapName_Type()
)
fsQosPoliceMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQosPoliceMapName.setStatus("current")
_FsQosPoliceMapEntryStatus_Type = ConfigStatus
_FsQosPoliceMapEntryStatus_Object = MibTableColumn
fsQosPoliceMapEntryStatus = _FsQosPoliceMapEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 2, 1, 2),
    _FsQosPoliceMapEntryStatus_Type()
)
fsQosPoliceMapEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQosPoliceMapEntryStatus.setStatus("current")
_FsQoSPoliceMapConfTable_Object = MibTable
fsQoSPoliceMapConfTable = _FsQoSPoliceMapConfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 3)
)
if mibBuilder.loadTexts:
    fsQoSPoliceMapConfTable.setStatus("current")
_FsQoSPoliceMapConfEntry_Object = MibTableRow
fsQoSPoliceMapConfEntry = _FsQoSPoliceMapConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 3, 1)
)
fsQoSPoliceMapConfEntry.setIndexNames(
    (0, "FS-QOS-MIB", "fsQoSPoliceCfgPoliceMapName"),
    (0, "FS-QOS-MIB", "fsQoSPoliceCfgClassMapName"),
)
if mibBuilder.loadTexts:
    fsQoSPoliceMapConfEntry.setStatus("current")


class _FsQoSPoliceCfgPoliceMapName_Type(DisplayString):
    """Custom type fsQoSPoliceCfgPoliceMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsQoSPoliceCfgPoliceMapName_Type.__name__ = "DisplayString"
_FsQoSPoliceCfgPoliceMapName_Object = MibTableColumn
fsQoSPoliceCfgPoliceMapName = _FsQoSPoliceCfgPoliceMapName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 3, 1, 1),
    _FsQoSPoliceCfgPoliceMapName_Type()
)
fsQoSPoliceCfgPoliceMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQoSPoliceCfgPoliceMapName.setStatus("current")


class _FsQoSPoliceCfgClassMapName_Type(DisplayString):
    """Custom type fsQoSPoliceCfgClassMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsQoSPoliceCfgClassMapName_Type.__name__ = "DisplayString"
_FsQoSPoliceCfgClassMapName_Object = MibTableColumn
fsQoSPoliceCfgClassMapName = _FsQoSPoliceCfgClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 3, 1, 2),
    _FsQoSPoliceCfgClassMapName_Type()
)
fsQoSPoliceCfgClassMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQoSPoliceCfgClassMapName.setStatus("current")
_FsQoSPoliceMapConfMaxBandWidth_Type = Unsigned32
_FsQoSPoliceMapConfMaxBandWidth_Object = MibTableColumn
fsQoSPoliceMapConfMaxBandWidth = _FsQoSPoliceMapConfMaxBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 3, 1, 3),
    _FsQoSPoliceMapConfMaxBandWidth_Type()
)
fsQoSPoliceMapConfMaxBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQoSPoliceMapConfMaxBandWidth.setStatus("current")
_FsQoSPoliceMapConfBurstFlowLimit_Type = Integer32
_FsQoSPoliceMapConfBurstFlowLimit_Object = MibTableColumn
fsQoSPoliceMapConfBurstFlowLimit = _FsQoSPoliceMapConfBurstFlowLimit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 3, 1, 4),
    _FsQoSPoliceMapConfBurstFlowLimit_Type()
)
fsQoSPoliceMapConfBurstFlowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQoSPoliceMapConfBurstFlowLimit.setStatus("current")


class _FsQoSPoliceMapConfExceedAction_Type(Integer32):
    """Custom type fsQoSPoliceMapConfExceedAction based on Integer32"""
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


_FsQoSPoliceMapConfExceedAction_Type.__name__ = "Integer32"
_FsQoSPoliceMapConfExceedAction_Object = MibTableColumn
fsQoSPoliceMapConfExceedAction = _FsQoSPoliceMapConfExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 3, 1, 5),
    _FsQoSPoliceMapConfExceedAction_Type()
)
fsQoSPoliceMapConfExceedAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQoSPoliceMapConfExceedAction.setStatus("current")
_FsQoSPoliceMapConfExceedDscp_Type = Integer32
_FsQoSPoliceMapConfExceedDscp_Object = MibTableColumn
fsQoSPoliceMapConfExceedDscp = _FsQoSPoliceMapConfExceedDscp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 3, 1, 6),
    _FsQoSPoliceMapConfExceedDscp_Type()
)
fsQoSPoliceMapConfExceedDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQoSPoliceMapConfExceedDscp.setStatus("current")
_FsQoSPoliceMapConfNewDscp_Type = Integer32
_FsQoSPoliceMapConfNewDscp_Object = MibTableColumn
fsQoSPoliceMapConfNewDscp = _FsQoSPoliceMapConfNewDscp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 3, 1, 7),
    _FsQoSPoliceMapConfNewDscp_Type()
)
fsQoSPoliceMapConfNewDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQoSPoliceMapConfNewDscp.setStatus("current")
_FsQoSPoliceMapCfgEntryStatus_Type = ConfigStatus
_FsQoSPoliceMapCfgEntryStatus_Object = MibTableColumn
fsQoSPoliceMapCfgEntryStatus = _FsQoSPoliceMapCfgEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 3, 1, 8),
    _FsQoSPoliceMapCfgEntryStatus_Type()
)
fsQoSPoliceMapCfgEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQoSPoliceMapCfgEntryStatus.setStatus("current")
_FsQoSPoliceMapConfMaxHighBandWidth_Type = Unsigned32
_FsQoSPoliceMapConfMaxHighBandWidth_Object = MibTableColumn
fsQoSPoliceMapConfMaxHighBandWidth = _FsQoSPoliceMapConfMaxHighBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 3, 1, 9),
    _FsQoSPoliceMapConfMaxHighBandWidth_Type()
)
fsQoSPoliceMapConfMaxHighBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsQoSPoliceMapConfMaxHighBandWidth.setStatus("current")
_FsQosPoliceIfExtTable_Object = MibTable
fsQosPoliceIfExtTable = _FsQosPoliceIfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 5)
)
if mibBuilder.loadTexts:
    fsQosPoliceIfExtTable.setStatus("current")
_FsQosPoliceIfExtEntry_Object = MibTableRow
fsQosPoliceIfExtEntry = _FsQosPoliceIfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 5, 1)
)
fsQosPoliceIfExtEntry.setIndexNames(
    (0, "FS-QOS-MIB", "fsQosPoliceIfIndex"),
)
if mibBuilder.loadTexts:
    fsQosPoliceIfExtEntry.setStatus("current")
_FsQosPoliceIfIndex_Type = IfIndex
_FsQosPoliceIfIndex_Object = MibTableColumn
fsQosPoliceIfIndex = _FsQosPoliceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 5, 1, 1),
    _FsQosPoliceIfIndex_Type()
)
fsQosPoliceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsQosPoliceIfIndex.setStatus("current")


class _FsIfInPoliceMapName_Type(DisplayString):
    """Custom type fsIfInPoliceMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsIfInPoliceMapName_Type.__name__ = "DisplayString"
_FsIfInPoliceMapName_Object = MibTableColumn
fsIfInPoliceMapName = _FsIfInPoliceMapName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 5, 1, 2),
    _FsIfInPoliceMapName_Type()
)
fsIfInPoliceMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfInPoliceMapName.setStatus("current")


class _FsIfOutPoliceMapName_Type(DisplayString):
    """Custom type fsIfOutPoliceMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsIfOutPoliceMapName_Type.__name__ = "DisplayString"
_FsIfOutPoliceMapName_Object = MibTableColumn
fsIfOutPoliceMapName = _FsIfOutPoliceMapName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 2, 5, 1, 3),
    _FsIfOutPoliceMapName_Type()
)
fsIfOutPoliceMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfOutPoliceMapName.setStatus("current")
_FsQoSMIBConformance_ObjectIdentity = ObjectIdentity
fsQoSMIBConformance = _FsQoSMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 3)
)
_FsQoSMIBCompliances_ObjectIdentity = ObjectIdentity
fsQoSMIBCompliances = _FsQoSMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 3, 1)
)
_FsQoSMIBGroups_ObjectIdentity = ObjectIdentity
fsQoSMIBGroups = _FsQoSMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 3, 2)
)

# Managed Objects groups

fsQoSPriorityMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 3, 2, 1)
)
fsQoSPriorityMIBGroup.setObjects(
      *(("FS-QOS-MIB", "fsQoSGlobalStatus"),
        ("FS-QOS-MIB", "fsPriorityTrafficClassNum"),
        ("FS-QOS-MIB", "fsPriorityClassNum"),
        ("FS-QOS-MIB", "fsPriorityDscpMaxValue"),
        ("FS-QOS-MIB", "fsTrafficClassPriority"),
        ("FS-QOS-MIB", "fsTrafficClass"),
        ("FS-QOS-MIB", "fsPriorityToDscp"),
        ("FS-QOS-MIB", "fsDscpClass"),
        ("FS-QOS-MIB", "fsDscpTrafficClassPriority"),
        ("FS-QOS-MIB", "fsPriorityTrafficClassOperMode"),
        ("FS-QOS-MIB", "fsPriorityBandWidth"),
        ("FS-QOS-MIB", "fsIfPriorityIfIndex"),
        ("FS-QOS-MIB", "fsIfPriority"),
        ("FS-QOS-MIB", "fsIfPriTrafficClassOperMode"),
        ("FS-QOS-MIB", "fsIfPriorityBandwidth"),
        ("FS-QOS-MIB", "fsIfPriorityQosTrustMode"),
        ("FS-QOS-MIB", "fsIpPreClassPriority"),
        ("FS-QOS-MIB", "fsIpPreToDscp"))
)
if mibBuilder.loadTexts:
    fsQoSPriorityMIBGroup.setStatus("current")

fsQoSTrafficClassMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 3, 2, 2)
)
fsQoSTrafficClassMIBGroup.setObjects(
      *(("FS-QOS-MIB", "fsQosClassMapName"),
        ("FS-QOS-MIB", "fsQosClassAclName"),
        ("FS-QOS-MIB", "fsQosClassMapEntryStatus"),
        ("FS-QOS-MIB", "fsQosPoliceMapName"),
        ("FS-QOS-MIB", "fsQosPoliceMapEntryStatus"),
        ("FS-QOS-MIB", "fsQoSPoliceCfgPoliceMapName"),
        ("FS-QOS-MIB", "fsQoSPoliceCfgClassMapName"),
        ("FS-QOS-MIB", "fsQoSPoliceMapConfMaxBandWidth"),
        ("FS-QOS-MIB", "fsQoSPoliceMapConfExceedAction"),
        ("FS-QOS-MIB", "fsQoSPoliceMapConfExceedDscp"),
        ("FS-QOS-MIB", "fsQoSPoliceMapConfNewDscp"),
        ("FS-QOS-MIB", "fsQoSPoliceMapCfgEntryStatus"),
        ("FS-QOS-MIB", "fsQoSPoliceMapConfMaxHighBandWidth"),
        ("FS-QOS-MIB", "fsQosPoliceIfIndex"),
        ("FS-QOS-MIB", "fsIfInPoliceMapName"),
        ("FS-QOS-MIB", "fsIfOutPoliceMapName"))
)
if mibBuilder.loadTexts:
    fsQoSTrafficClassMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsQoSMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 18, 3, 1, 1)
)
fsQoSMIBCompliance.setObjects(
      *(("FS-QOS-MIB", "fsQoSPriorityMIBGroup"),
        ("FS-QOS-MIB", "fsQoSTrafficClassMIBGroup"))
)
if mibBuilder.loadTexts:
    fsQoSMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-QOS-MIB",
    **{"fsQoSMIB": fsQoSMIB,
       "fsQoSPriorityMIBObjects": fsQoSPriorityMIBObjects,
       "fsQoSGlobalStatus": fsQoSGlobalStatus,
       "fsPriorityTrafficClassNum": fsPriorityTrafficClassNum,
       "fsPriorityClassNum": fsPriorityClassNum,
       "fsPriorityDscpMaxValue": fsPriorityDscpMaxValue,
       "fsTrafficClassTable": fsTrafficClassTable,
       "fsTrafficClassEntry": fsTrafficClassEntry,
       "fsTrafficClassPriority": fsTrafficClassPriority,
       "fsTrafficClass": fsTrafficClass,
       "fsPriorityToDscp": fsPriorityToDscp,
       "fsDscpClassTable": fsDscpClassTable,
       "fsDscpClassEntry": fsDscpClassEntry,
       "fsDscpClass": fsDscpClass,
       "fsDscpTrafficClassPriority": fsDscpTrafficClassPriority,
       "fsPriorityTrafficClassOperMode": fsPriorityTrafficClassOperMode,
       "fsPriorityBandWidth": fsPriorityBandWidth,
       "fsIfPriorityTable": fsIfPriorityTable,
       "fsIfPriorityEntry": fsIfPriorityEntry,
       "fsIfPriorityIfIndex": fsIfPriorityIfIndex,
       "fsIfPriority": fsIfPriority,
       "fsIfPriTrafficClassOperMode": fsIfPriTrafficClassOperMode,
       "fsIfPriorityBandwidth": fsIfPriorityBandwidth,
       "fsIfPriorityQosTrustMode": fsIfPriorityQosTrustMode,
       "fsIpPreClassTable": fsIpPreClassTable,
       "fsIpPreClassEntry": fsIpPreClassEntry,
       "fsIpPreClassPriority": fsIpPreClassPriority,
       "fsIpPreToDscp": fsIpPreToDscp,
       "fsIfRateLimitTable": fsIfRateLimitTable,
       "fsIfRateLimitEntry": fsIfRateLimitEntry,
       "fsIfRateLimitIndex": fsIfRateLimitIndex,
       "fsIfRateLimitInMaxBandWidth": fsIfRateLimitInMaxBandWidth,
       "fsIfRateLimitInBurstFlowLimit": fsIfRateLimitInBurstFlowLimit,
       "fsIfRateLimitOutMaxBandWidth": fsIfRateLimitOutMaxBandWidth,
       "fsIfRateLimitOutBurstFlowLimit": fsIfRateLimitOutBurstFlowLimit,
       "fsIfQueueSupportTable": fsIfQueueSupportTable,
       "fsIfQueueSupportEntry": fsIfQueueSupportEntry,
       "fsIfIndex": fsIfIndex,
       "fsIfQueueIndex": fsIfQueueIndex,
       "fsIfQueueSupportTransmitPacket": fsIfQueueSupportTransmitPacket,
       "fsIfQueueSupportTransmitBytes": fsIfQueueSupportTransmitBytes,
       "fsIfQueueSupportDropPacket": fsIfQueueSupportDropPacket,
       "fsIfQueueSupportDropBytes": fsIfQueueSupportDropBytes,
       "fsIfMulticastQueueSupportTable": fsIfMulticastQueueSupportTable,
       "fsIfMulticastQueueSupportEntry": fsIfMulticastQueueSupportEntry,
       "fsIfIndexMulticast": fsIfIndexMulticast,
       "fsIfMulticastQueueIndex": fsIfMulticastQueueIndex,
       "fsIfMulticastQueueSupportTransmitPacket": fsIfMulticastQueueSupportTransmitPacket,
       "fsIfMulticastQueueSupportTransmitBytes": fsIfMulticastQueueSupportTransmitBytes,
       "fsIfMulticastQueueSupportDropPacket": fsIfMulticastQueueSupportDropPacket,
       "fsIfMulticastQueueSupportDropBytes": fsIfMulticastQueueSupportDropBytes,
       "fsWredEcnStatsTable": fsWredEcnStatsTable,
       "fsWredEcnStatsEntry": fsWredEcnStatsEntry,
       "fsWredEcnStatsIfIndex": fsWredEcnStatsIfIndex,
       "fsWredDropped": fsWredDropped,
       "fsEcnSended": fsEcnSended,
       "fsQoSTrafficClassMIBObjects": fsQoSTrafficClassMIBObjects,
       "fsQoSTrafficClassTable": fsQoSTrafficClassTable,
       "fsQoSTrafficClassEntry": fsQoSTrafficClassEntry,
       "fsQosClassMapName": fsQosClassMapName,
       "fsQosClassAclName": fsQosClassAclName,
       "fsQosClassMapEntryStatus": fsQosClassMapEntryStatus,
       "fsQoSPoliceMapTable": fsQoSPoliceMapTable,
       "fsQoSPoliceMapEntry": fsQoSPoliceMapEntry,
       "fsQosPoliceMapName": fsQosPoliceMapName,
       "fsQosPoliceMapEntryStatus": fsQosPoliceMapEntryStatus,
       "fsQoSPoliceMapConfTable": fsQoSPoliceMapConfTable,
       "fsQoSPoliceMapConfEntry": fsQoSPoliceMapConfEntry,
       "fsQoSPoliceCfgPoliceMapName": fsQoSPoliceCfgPoliceMapName,
       "fsQoSPoliceCfgClassMapName": fsQoSPoliceCfgClassMapName,
       "fsQoSPoliceMapConfMaxBandWidth": fsQoSPoliceMapConfMaxBandWidth,
       "fsQoSPoliceMapConfBurstFlowLimit": fsQoSPoliceMapConfBurstFlowLimit,
       "fsQoSPoliceMapConfExceedAction": fsQoSPoliceMapConfExceedAction,
       "fsQoSPoliceMapConfExceedDscp": fsQoSPoliceMapConfExceedDscp,
       "fsQoSPoliceMapConfNewDscp": fsQoSPoliceMapConfNewDscp,
       "fsQoSPoliceMapCfgEntryStatus": fsQoSPoliceMapCfgEntryStatus,
       "fsQoSPoliceMapConfMaxHighBandWidth": fsQoSPoliceMapConfMaxHighBandWidth,
       "fsQosPoliceIfExtTable": fsQosPoliceIfExtTable,
       "fsQosPoliceIfExtEntry": fsQosPoliceIfExtEntry,
       "fsQosPoliceIfIndex": fsQosPoliceIfIndex,
       "fsIfInPoliceMapName": fsIfInPoliceMapName,
       "fsIfOutPoliceMapName": fsIfOutPoliceMapName,
       "fsQoSMIBConformance": fsQoSMIBConformance,
       "fsQoSMIBCompliances": fsQoSMIBCompliances,
       "fsQoSMIBCompliance": fsQoSMIBCompliance,
       "fsQoSMIBGroups": fsQoSMIBGroups,
       "fsQoSPriorityMIBGroup": fsQoSPriorityMIBGroup,
       "fsQoSTrafficClassMIBGroup": fsQoSTrafficClassMIBGroup}
)
