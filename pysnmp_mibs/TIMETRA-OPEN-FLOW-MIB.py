# SNMP MIB module (TIMETRA-OPEN-FLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-OPEN-FLOW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:59:10 2025
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

(InetAddress,
 InetAddressIPv6,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressType",
    "InetPortNumber")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TLNamedItemOrEmpty,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxAdminState,
 TmnxEnabledDisabled,
 TmnxOperState,
 TmnxPortID,
 TmnxServId) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TLNamedItemOrEmpty",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxAdminState",
    "TmnxEnabledDisabled",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxServId")


# MODULE-IDENTITY

timetraOpenFlowMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 93)
)
if mibBuilder.loadTexts:
    timetraOpenFlowMIBModule.setRevisions(
        ("2017-01-01 00:00",
         "2016-01-01 00:00",
         "2015-01-01 00:00",
         "2014-01-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxOFDatapathIdentifier(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class TmnxOFPktType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30)
        )
    )
    namedValues = NamedValues(
        *(("hello", 1),
          ("error", 2),
          ("echoRequest", 3),
          ("echoReply", 4),
          ("experimenter", 5),
          ("featureRequest", 6),
          ("featureReply", 7),
          ("getConfigRequest", 8),
          ("getConfigReply", 9),
          ("setConfig", 10),
          ("packetIn", 11),
          ("flowRemoved", 12),
          ("portStatus", 13),
          ("packetOut", 14),
          ("flowMod", 15),
          ("groupMod", 16),
          ("portMod", 17),
          ("tableMod", 18),
          ("multipartRequest", 19),
          ("multipartReply", 20),
          ("barrierRequest", 21),
          ("barrierReply", 22),
          ("getQueueConfigRequest", 23),
          ("getQueueConfigReply", 24),
          ("roleRequest", 25),
          ("roleReply", 26),
          ("getAsyncRequest", 27),
          ("getAsyncReply", 28),
          ("setAsync", 29),
          ("meterMod", 30))
    )



class TmnxOFAsyncFltrPacketIn(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("tableMiss", 0),
          ("applyAction", 1),
          ("invalidTTL", 2))
    )


class TmnxOFAsyncFltrPortStatus(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("portAdd", 0),
          ("portDelete", 1),
          ("portModify", 2))
    )


class TmnxOFAsyncFltrFlowRemoved(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("idleTimeOut", 0),
          ("hardTimeOut", 1),
          ("flowModDelete", 2),
          ("groupDelete", 3))
    )


# MIB Managed Objects in the order of their OIDs

_TmnxOpenFlowConformance_ObjectIdentity = ObjectIdentity
tmnxOpenFlowConformance = _TmnxOpenFlowConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93)
)
_TmnxOpenFlowCompliances_ObjectIdentity = ObjectIdentity
tmnxOpenFlowCompliances = _TmnxOpenFlowCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 1)
)
_TmnxOpenFlowGroups_ObjectIdentity = ObjectIdentity
tmnxOpenFlowGroups = _TmnxOpenFlowGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 2)
)
_TmnxOpenFlowV12v0Groups_ObjectIdentity = ObjectIdentity
tmnxOpenFlowV12v0Groups = _TmnxOpenFlowV12v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 2, 1)
)
_TmnxOpenFlowV13v0Groups_ObjectIdentity = ObjectIdentity
tmnxOpenFlowV13v0Groups = _TmnxOpenFlowV13v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 2, 2)
)
_TmnxOpenFlowV14v0Groups_ObjectIdentity = ObjectIdentity
tmnxOpenFlowV14v0Groups = _TmnxOpenFlowV14v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 2, 3)
)
_TmnxOpenFlowV15v0Groups_ObjectIdentity = ObjectIdentity
tmnxOpenFlowV15v0Groups = _TmnxOpenFlowV15v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 2, 4)
)
_TmnxOpenFlowV16v0Groups_ObjectIdentity = ObjectIdentity
tmnxOpenFlowV16v0Groups = _TmnxOpenFlowV16v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 2, 5)
)
_TmnxOpenFlowNotifGroups_ObjectIdentity = ObjectIdentity
tmnxOpenFlowNotifGroups = _TmnxOpenFlowNotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 3)
)
_TmnxOpenFlowControllerGroups_ObjectIdentity = ObjectIdentity
tmnxOpenFlowControllerGroups = _TmnxOpenFlowControllerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 4)
)
_TmnxOpenFlow_ObjectIdentity = ObjectIdentity
tmnxOpenFlow = _TmnxOpenFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93)
)
_TmnxOpenFlowObjs_ObjectIdentity = ObjectIdentity
tmnxOpenFlowObjs = _TmnxOpenFlowObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1)
)
_TmnxOFSwitchTableLastChanged_Type = TimeStamp
_TmnxOFSwitchTableLastChanged_Object = MibScalar
tmnxOFSwitchTableLastChanged = _TmnxOFSwitchTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 1),
    _TmnxOFSwitchTableLastChanged_Type()
)
tmnxOFSwitchTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFSwitchTableLastChanged.setStatus("current")
_TmnxOFSwitchTable_Object = MibTable
tmnxOFSwitchTable = _TmnxOFSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxOFSwitchTable.setStatus("current")
_TmnxOFSwitchEntry_Object = MibTableRow
tmnxOFSwitchEntry = _TmnxOFSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1)
)
tmnxOFSwitchEntry.setIndexNames(
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchName"),
)
if mibBuilder.loadTexts:
    tmnxOFSwitchEntry.setStatus("current")
_TmnxOFSwitchName_Type = TNamedItem
_TmnxOFSwitchName_Object = MibTableColumn
tmnxOFSwitchName = _TmnxOFSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 1),
    _TmnxOFSwitchName_Type()
)
tmnxOFSwitchName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOFSwitchName.setStatus("current")
_TmnxOFSwitchRowStatus_Type = RowStatus
_TmnxOFSwitchRowStatus_Object = MibTableColumn
tmnxOFSwitchRowStatus = _TmnxOFSwitchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 2),
    _TmnxOFSwitchRowStatus_Type()
)
tmnxOFSwitchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFSwitchRowStatus.setStatus("current")
_TmnxOFSwitchLastChanged_Type = TimeStamp
_TmnxOFSwitchLastChanged_Object = MibTableColumn
tmnxOFSwitchLastChanged = _TmnxOFSwitchLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 3),
    _TmnxOFSwitchLastChanged_Type()
)
tmnxOFSwitchLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFSwitchLastChanged.setStatus("current")


class _TmnxOFSwitchEchoInterval_Type(Unsigned32):
    """Custom type tmnxOFSwitchEchoInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TmnxOFSwitchEchoInterval_Type.__name__ = "Unsigned32"
_TmnxOFSwitchEchoInterval_Object = MibTableColumn
tmnxOFSwitchEchoInterval = _TmnxOFSwitchEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 4),
    _TmnxOFSwitchEchoInterval_Type()
)
tmnxOFSwitchEchoInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFSwitchEchoInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOFSwitchEchoInterval.setUnits("seconds")


class _TmnxOFSwitchEchoMultiple_Type(Unsigned32):
    """Custom type tmnxOFSwitchEchoMultiple based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 100),
    )


_TmnxOFSwitchEchoMultiple_Type.__name__ = "Unsigned32"
_TmnxOFSwitchEchoMultiple_Object = MibTableColumn
tmnxOFSwitchEchoMultiple = _TmnxOFSwitchEchoMultiple_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 5),
    _TmnxOFSwitchEchoMultiple_Type()
)
tmnxOFSwitchEchoMultiple.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFSwitchEchoMultiple.setStatus("current")


class _TmnxOFSwitchLogicalPortStatus_Type(Bits):
    """Custom type tmnxOFSwitchLogicalPortStatus based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("rsvpTe", 0),
          ("mplsTp", 1),
          ("srTe", 2))
    )

_TmnxOFSwitchLogicalPortStatus_Type.__name__ = "Bits"
_TmnxOFSwitchLogicalPortStatus_Object = MibTableColumn
tmnxOFSwitchLogicalPortStatus = _TmnxOFSwitchLogicalPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 6),
    _TmnxOFSwitchLogicalPortStatus_Type()
)
tmnxOFSwitchLogicalPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFSwitchLogicalPortStatus.setStatus("current")


class _TmnxOFSwitchAdminState_Type(TmnxAdminState):
    """Custom type tmnxOFSwitchAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxOFSwitchAdminState_Type.__name__ = "TmnxAdminState"
_TmnxOFSwitchAdminState_Object = MibTableColumn
tmnxOFSwitchAdminState = _TmnxOFSwitchAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 7),
    _TmnxOFSwitchAdminState_Type()
)
tmnxOFSwitchAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFSwitchAdminState.setStatus("current")


class _TmnxOFSwitchDescription_Type(DisplayString):
    """Custom type tmnxOFSwitchDescription based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxOFSwitchDescription_Type.__name__ = "DisplayString"
_TmnxOFSwitchDescription_Object = MibTableColumn
tmnxOFSwitchDescription = _TmnxOFSwitchDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 8),
    _TmnxOFSwitchDescription_Type()
)
tmnxOFSwitchDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFSwitchDescription.setStatus("current")
_TmnxOFSwitchDataPathID_Type = TmnxOFDatapathIdentifier
_TmnxOFSwitchDataPathID_Object = MibTableColumn
tmnxOFSwitchDataPathID = _TmnxOFSwitchDataPathID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 9),
    _TmnxOFSwitchDataPathID_Type()
)
tmnxOFSwitchDataPathID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFSwitchDataPathID.setStatus("current")
_TmnxOFSwitchFeaturesBufferSize_Type = Unsigned32
_TmnxOFSwitchFeaturesBufferSize_Object = MibTableColumn
tmnxOFSwitchFeaturesBufferSize = _TmnxOFSwitchFeaturesBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 10),
    _TmnxOFSwitchFeaturesBufferSize_Type()
)
tmnxOFSwitchFeaturesBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFSwitchFeaturesBufferSize.setStatus("current")
_TmnxOFSwitchFeaturesNumTables_Type = Unsigned32
_TmnxOFSwitchFeaturesNumTables_Object = MibTableColumn
tmnxOFSwitchFeaturesNumTables = _TmnxOFSwitchFeaturesNumTables_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 11),
    _TmnxOFSwitchFeaturesNumTables_Type()
)
tmnxOFSwitchFeaturesNumTables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFSwitchFeaturesNumTables.setStatus("current")


class _TmnxOFSwitchFeaturesCapability_Type(Bits):
    """Custom type tmnxOFSwitchFeaturesCapability based on Bits"""
    namedValues = NamedValues(
        *(("flowStats", 0),
          ("tableStats", 1),
          ("portStats", 2),
          ("groupStats", 3))
    )

_TmnxOFSwitchFeaturesCapability_Type.__name__ = "Bits"
_TmnxOFSwitchFeaturesCapability_Object = MibTableColumn
tmnxOFSwitchFeaturesCapability = _TmnxOFSwitchFeaturesCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 12),
    _TmnxOFSwitchFeaturesCapability_Type()
)
tmnxOFSwitchFeaturesCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFSwitchFeaturesCapability.setStatus("current")


class _TmnxOFSwitchAuxChannelEnabled_Type(TruthValue):
    """Custom type tmnxOFSwitchAuxChannelEnabled based on TruthValue"""
    defaultValue = 2


_TmnxOFSwitchAuxChannelEnabled_Type.__name__ = "TruthValue"
_TmnxOFSwitchAuxChannelEnabled_Object = MibTableColumn
tmnxOFSwitchAuxChannelEnabled = _TmnxOFSwitchAuxChannelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 13),
    _TmnxOFSwitchAuxChannelEnabled_Type()
)
tmnxOFSwitchAuxChannelEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFSwitchAuxChannelEnabled.setStatus("current")


class _TmnxOFSwitchID_Type(Unsigned32):
    """Custom type tmnxOFSwitchID based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxOFSwitchID_Type.__name__ = "Unsigned32"
_TmnxOFSwitchID_Object = MibTableColumn
tmnxOFSwitchID = _TmnxOFSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 2, 1, 14),
    _TmnxOFSwitchID_Type()
)
tmnxOFSwitchID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFSwitchID.setStatus("current")
_TmnxOFControllerTableLastChanged_Type = TimeStamp
_TmnxOFControllerTableLastChanged_Object = MibScalar
tmnxOFControllerTableLastChanged = _TmnxOFControllerTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 3),
    _TmnxOFControllerTableLastChanged_Type()
)
tmnxOFControllerTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFControllerTableLastChanged.setStatus("current")
_TmnxOFControllerTable_Object = MibTable
tmnxOFControllerTable = _TmnxOFControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxOFControllerTable.setStatus("current")
_TmnxOFControllerEntry_Object = MibTableRow
tmnxOFControllerEntry = _TmnxOFControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4, 1)
)
tmnxOFControllerEntry.setIndexNames(
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchName"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerAddressType"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerAddress"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerTCPPort"),
)
if mibBuilder.loadTexts:
    tmnxOFControllerEntry.setStatus("current")
_TmnxOFControllerAddressType_Type = InetAddressType
_TmnxOFControllerAddressType_Object = MibTableColumn
tmnxOFControllerAddressType = _TmnxOFControllerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4, 1, 1),
    _TmnxOFControllerAddressType_Type()
)
tmnxOFControllerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOFControllerAddressType.setStatus("current")


class _TmnxOFControllerAddress_Type(InetAddress):
    """Custom type tmnxOFControllerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOFControllerAddress_Type.__name__ = "InetAddress"
_TmnxOFControllerAddress_Object = MibTableColumn
tmnxOFControllerAddress = _TmnxOFControllerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4, 1, 2),
    _TmnxOFControllerAddress_Type()
)
tmnxOFControllerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOFControllerAddress.setStatus("current")


class _TmnxOFControllerTCPPort_Type(InetPortNumber):
    """Custom type tmnxOFControllerTCPPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxOFControllerTCPPort_Type.__name__ = "InetPortNumber"
_TmnxOFControllerTCPPort_Object = MibTableColumn
tmnxOFControllerTCPPort = _TmnxOFControllerTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4, 1, 3),
    _TmnxOFControllerTCPPort_Type()
)
tmnxOFControllerTCPPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOFControllerTCPPort.setStatus("current")
_TmnxOFControllerRowStatus_Type = RowStatus
_TmnxOFControllerRowStatus_Object = MibTableColumn
tmnxOFControllerRowStatus = _TmnxOFControllerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4, 1, 4),
    _TmnxOFControllerRowStatus_Type()
)
tmnxOFControllerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFControllerRowStatus.setStatus("current")
_TmnxOFControllerLastChanged_Type = TimeStamp
_TmnxOFControllerLastChanged_Object = MibTableColumn
tmnxOFControllerLastChanged = _TmnxOFControllerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4, 1, 5),
    _TmnxOFControllerLastChanged_Type()
)
tmnxOFControllerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFControllerLastChanged.setStatus("current")


class _TmnxOFControllerRole_Type(Integer32):
    """Custom type tmnxOFControllerRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noChange", 0),
          ("equal", 1),
          ("master", 2),
          ("slave", 3))
    )


_TmnxOFControllerRole_Type.__name__ = "Integer32"
_TmnxOFControllerRole_Object = MibTableColumn
tmnxOFControllerRole = _TmnxOFControllerRole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4, 1, 6),
    _TmnxOFControllerRole_Type()
)
tmnxOFControllerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFControllerRole.setStatus("current")
_TmnxOFControllerGenID_Type = Counter64
_TmnxOFControllerGenID_Object = MibTableColumn
tmnxOFControllerGenID = _TmnxOFControllerGenID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4, 1, 7),
    _TmnxOFControllerGenID_Type()
)
tmnxOFControllerGenID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFControllerGenID.setStatus("current")


class _TmnxOFControllerTLSProfileName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOFControllerTLSProfileName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOFControllerTLSProfileName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOFControllerTLSProfileName_Object = MibTableColumn
tmnxOFControllerTLSProfileName = _TmnxOFControllerTLSProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4, 1, 8),
    _TmnxOFControllerTLSProfileName_Type()
)
tmnxOFControllerTLSProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFControllerTLSProfileName.setStatus("current")


class _TmnxOFControllerServiceID_Type(TmnxServId):
    """Custom type tmnxOFControllerServiceID based on TmnxServId"""
    defaultValue = 0


_TmnxOFControllerServiceID_Type.__name__ = "TmnxServId"
_TmnxOFControllerServiceID_Object = MibTableColumn
tmnxOFControllerServiceID = _TmnxOFControllerServiceID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4, 1, 9),
    _TmnxOFControllerServiceID_Type()
)
tmnxOFControllerServiceID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFControllerServiceID.setStatus("current")


class _TmnxOFControllerLoopbckAddrType_Type(InetAddressType):
    """Custom type tmnxOFControllerLoopbckAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxOFControllerLoopbckAddrType_Type.__name__ = "InetAddressType"
_TmnxOFControllerLoopbckAddrType_Object = MibTableColumn
tmnxOFControllerLoopbckAddrType = _TmnxOFControllerLoopbckAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4, 1, 10),
    _TmnxOFControllerLoopbckAddrType_Type()
)
tmnxOFControllerLoopbckAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFControllerLoopbckAddrType.setStatus("current")


class _TmnxOFControllerLoopbackAddr_Type(InetAddress):
    """Custom type tmnxOFControllerLoopbackAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOFControllerLoopbackAddr_Type.__name__ = "InetAddress"
_TmnxOFControllerLoopbackAddr_Object = MibTableColumn
tmnxOFControllerLoopbackAddr = _TmnxOFControllerLoopbackAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4, 1, 11),
    _TmnxOFControllerLoopbackAddr_Type()
)
tmnxOFControllerLoopbackAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFControllerLoopbackAddr.setStatus("current")


class _TmnxOFControllerSvcName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxOFControllerSvcName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOFControllerSvcName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxOFControllerSvcName_Object = MibTableColumn
tmnxOFControllerSvcName = _TmnxOFControllerSvcName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 4, 1, 12),
    _TmnxOFControllerSvcName_Type()
)
tmnxOFControllerSvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFControllerSvcName.setStatus("current")
_TmnxOFFlowTableTableLastChanged_Type = TimeStamp
_TmnxOFFlowTableTableLastChanged_Object = MibScalar
tmnxOFFlowTableTableLastChanged = _TmnxOFFlowTableTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 5),
    _TmnxOFFlowTableTableLastChanged_Type()
)
tmnxOFFlowTableTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFFlowTableTableLastChanged.setStatus("current")
_TmnxOFFlowTableTable_Object = MibTable
tmnxOFFlowTableTable = _TmnxOFFlowTableTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxOFFlowTableTable.setStatus("current")
_TmnxOFFlowTableEntry_Object = MibTableRow
tmnxOFFlowTableEntry = _TmnxOFFlowTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 6, 1)
)
tmnxOFFlowTableEntry.setIndexNames(
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchName"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowTableId"),
)
if mibBuilder.loadTexts:
    tmnxOFFlowTableEntry.setStatus("current")
_TmnxOFFlowTableId_Type = Unsigned32
_TmnxOFFlowTableId_Object = MibTableColumn
tmnxOFFlowTableId = _TmnxOFFlowTableId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 6, 1, 1),
    _TmnxOFFlowTableId_Type()
)
tmnxOFFlowTableId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOFFlowTableId.setStatus("current")
_TmnxOFFlowTableRowStatus_Type = RowStatus
_TmnxOFFlowTableRowStatus_Object = MibTableColumn
tmnxOFFlowTableRowStatus = _TmnxOFFlowTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 6, 1, 2),
    _TmnxOFFlowTableRowStatus_Type()
)
tmnxOFFlowTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFFlowTableRowStatus.setStatus("current")
_TmnxOFFlowTableLastChanged_Type = TimeStamp
_TmnxOFFlowTableLastChanged_Object = MibTableColumn
tmnxOFFlowTableLastChanged = _TmnxOFFlowTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 6, 1, 3),
    _TmnxOFFlowTableLastChanged_Type()
)
tmnxOFFlowTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFFlowTableLastChanged.setStatus("current")


class _TmnxOFFlowTableMaxSize_Type(Unsigned32):
    """Custom type tmnxOFFlowTableMaxSize based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 524288),
    )


_TmnxOFFlowTableMaxSize_Type.__name__ = "Unsigned32"
_TmnxOFFlowTableMaxSize_Object = MibTableColumn
tmnxOFFlowTableMaxSize = _TmnxOFFlowTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 6, 1, 4),
    _TmnxOFFlowTableMaxSize_Type()
)
tmnxOFFlowTableMaxSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFFlowTableMaxSize.setStatus("current")


class _TmnxOFFlowTableNoMatchAction_Type(Integer32):
    """Custom type tmnxOFFlowTableNoMatchAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("fallThrough", 2),
          ("packetIn", 3))
    )


_TmnxOFFlowTableNoMatchAction_Type.__name__ = "Integer32"
_TmnxOFFlowTableNoMatchAction_Object = MibTableColumn
tmnxOFFlowTableNoMatchAction = _TmnxOFFlowTableNoMatchAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 6, 1, 5),
    _TmnxOFFlowTableNoMatchAction_Type()
)
tmnxOFFlowTableNoMatchAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFFlowTableNoMatchAction.setStatus("current")
_TmnxOFFlowTableNumEntries_Type = Unsigned32
_TmnxOFFlowTableNumEntries_Object = MibTableColumn
tmnxOFFlowTableNumEntries = _TmnxOFFlowTableNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 6, 1, 6),
    _TmnxOFFlowTableNumEntries_Type()
)
tmnxOFFlowTableNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFFlowTableNumEntries.setStatus("current")
_TmnxOFFlowTableOperStatus_Type = TmnxOperState
_TmnxOFFlowTableOperStatus_Object = MibTableColumn
tmnxOFFlowTableOperStatus = _TmnxOFFlowTableOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 6, 1, 7),
    _TmnxOFFlowTableOperStatus_Type()
)
tmnxOFFlowTableOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFFlowTableOperStatus.setStatus("current")


class _TmnxOFFlowTableSwitchDefCookie_Type(TmnxEnabledDisabled):
    """Custom type tmnxOFFlowTableSwitchDefCookie based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOFFlowTableSwitchDefCookie_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOFFlowTableSwitchDefCookie_Object = MibTableColumn
tmnxOFFlowTableSwitchDefCookie = _TmnxOFFlowTableSwitchDefCookie_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 6, 1, 8),
    _TmnxOFFlowTableSwitchDefCookie_Type()
)
tmnxOFFlowTableSwitchDefCookie.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFFlowTableSwitchDefCookie.setStatus("current")
_TmnxOFChannelInfoTable_Object = MibTable
tmnxOFChannelInfoTable = _TmnxOFChannelInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxOFChannelInfoTable.setStatus("current")
_TmnxOFChannelInfoEntry_Object = MibTableRow
tmnxOFChannelInfoEntry = _TmnxOFChannelInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1)
)
tmnxOFChannelInfoEntry.setIndexNames(
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchName"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerAddressType"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerAddress"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerTCPPort"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelID"),
)
if mibBuilder.loadTexts:
    tmnxOFChannelInfoEntry.setStatus("current")
_TmnxOFChannelID_Type = Unsigned32
_TmnxOFChannelID_Object = MibTableColumn
tmnxOFChannelID = _TmnxOFChannelID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 1),
    _TmnxOFChannelID_Type()
)
tmnxOFChannelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOFChannelID.setStatus("current")
_TmnxOFChannelVersion_Type = Unsigned32
_TmnxOFChannelVersion_Object = MibTableColumn
tmnxOFChannelVersion = _TmnxOFChannelVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 2),
    _TmnxOFChannelVersion_Type()
)
tmnxOFChannelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelVersion.setStatus("current")


class _TmnxOFChannelType_Type(Integer32):
    """Custom type tmnxOFChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("auxiliary", 2))
    )


_TmnxOFChannelType_Type.__name__ = "Integer32"
_TmnxOFChannelType_Object = MibTableColumn
tmnxOFChannelType = _TmnxOFChannelType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 3),
    _TmnxOFChannelType_Type()
)
tmnxOFChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelType.setStatus("current")
_TmnxOFChannelOperStatus_Type = TmnxOperState
_TmnxOFChannelOperStatus_Object = MibTableColumn
tmnxOFChannelOperStatus = _TmnxOFChannelOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 4),
    _TmnxOFChannelOperStatus_Type()
)
tmnxOFChannelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelOperStatus.setStatus("current")


class _TmnxOFChannelOperFlags_Type(Bits):
    """Custom type tmnxOFChannelOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("socketStateDisable", 0),
          ("socketStateListen", 1),
          ("socketStateConnecting", 2),
          ("socketStateEstablished", 3),
          ("helloReceived", 4),
          ("helloTransmitted", 5),
          ("handshake", 6))
    )

_TmnxOFChannelOperFlags_Type.__name__ = "Bits"
_TmnxOFChannelOperFlags_Object = MibTableColumn
tmnxOFChannelOperFlags = _TmnxOFChannelOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 5),
    _TmnxOFChannelOperFlags_Type()
)
tmnxOFChannelOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelOperFlags.setStatus("current")
_TmnxOFChannelEchoTimeExpiry_Type = Unsigned32
_TmnxOFChannelEchoTimeExpiry_Object = MibTableColumn
tmnxOFChannelEchoTimeExpiry = _TmnxOFChannelEchoTimeExpiry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 6),
    _TmnxOFChannelEchoTimeExpiry_Type()
)
tmnxOFChannelEchoTimeExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelEchoTimeExpiry.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOFChannelEchoTimeExpiry.setUnits("seconds")
_TmnxOFChannelHoldTimeExpiry_Type = Unsigned32
_TmnxOFChannelHoldTimeExpiry_Object = MibTableColumn
tmnxOFChannelHoldTimeExpiry = _TmnxOFChannelHoldTimeExpiry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 7),
    _TmnxOFChannelHoldTimeExpiry_Type()
)
tmnxOFChannelHoldTimeExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelHoldTimeExpiry.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOFChannelHoldTimeExpiry.setUnits("seconds")
_TmnxOFChannelConnRetryExpiry_Type = Unsigned32
_TmnxOFChannelConnRetryExpiry_Object = MibTableColumn
tmnxOFChannelConnRetryExpiry = _TmnxOFChannelConnRetryExpiry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 8),
    _TmnxOFChannelConnRetryExpiry_Type()
)
tmnxOFChannelConnRetryExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelConnRetryExpiry.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOFChannelConnRetryExpiry.setUnits("seconds")
_TmnxOFChannelConnUpTime_Type = Unsigned32
_TmnxOFChannelConnUpTime_Object = MibTableColumn
tmnxOFChannelConnUpTime = _TmnxOFChannelConnUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 9),
    _TmnxOFChannelConnUpTime_Type()
)
tmnxOFChannelConnUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelConnUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOFChannelConnUpTime.setUnits("seconds")
_TmnxOFChannelMEAsyncFltrPacketIn_Type = TmnxOFAsyncFltrPacketIn
_TmnxOFChannelMEAsyncFltrPacketIn_Object = MibTableColumn
tmnxOFChannelMEAsyncFltrPacketIn = _TmnxOFChannelMEAsyncFltrPacketIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 10),
    _TmnxOFChannelMEAsyncFltrPacketIn_Type()
)
tmnxOFChannelMEAsyncFltrPacketIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelMEAsyncFltrPacketIn.setStatus("current")
_TmnxOFChannelSlAsyncFltrPacketIn_Type = TmnxOFAsyncFltrPacketIn
_TmnxOFChannelSlAsyncFltrPacketIn_Object = MibTableColumn
tmnxOFChannelSlAsyncFltrPacketIn = _TmnxOFChannelSlAsyncFltrPacketIn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 11),
    _TmnxOFChannelSlAsyncFltrPacketIn_Type()
)
tmnxOFChannelSlAsyncFltrPacketIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelSlAsyncFltrPacketIn.setStatus("current")
_TmnxOFChannelMEAsyncFltrPortSts_Type = TmnxOFAsyncFltrPortStatus
_TmnxOFChannelMEAsyncFltrPortSts_Object = MibTableColumn
tmnxOFChannelMEAsyncFltrPortSts = _TmnxOFChannelMEAsyncFltrPortSts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 12),
    _TmnxOFChannelMEAsyncFltrPortSts_Type()
)
tmnxOFChannelMEAsyncFltrPortSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelMEAsyncFltrPortSts.setStatus("current")
_TmnxOFChannelSlAsyncFltrPortSts_Type = TmnxOFAsyncFltrPortStatus
_TmnxOFChannelSlAsyncFltrPortSts_Object = MibTableColumn
tmnxOFChannelSlAsyncFltrPortSts = _TmnxOFChannelSlAsyncFltrPortSts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 13),
    _TmnxOFChannelSlAsyncFltrPortSts_Type()
)
tmnxOFChannelSlAsyncFltrPortSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelSlAsyncFltrPortSts.setStatus("current")
_TmnxOFChannelMEAsyncFltrFlowRem_Type = TmnxOFAsyncFltrFlowRemoved
_TmnxOFChannelMEAsyncFltrFlowRem_Object = MibTableColumn
tmnxOFChannelMEAsyncFltrFlowRem = _TmnxOFChannelMEAsyncFltrFlowRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 14),
    _TmnxOFChannelMEAsyncFltrFlowRem_Type()
)
tmnxOFChannelMEAsyncFltrFlowRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelMEAsyncFltrFlowRem.setStatus("current")
_TmnxOFChannelSlAsyncFltrFlowRem_Type = TmnxOFAsyncFltrFlowRemoved
_TmnxOFChannelSlAsyncFltrFlowRem_Object = MibTableColumn
tmnxOFChannelSlAsyncFltrFlowRem = _TmnxOFChannelSlAsyncFltrFlowRem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 15),
    _TmnxOFChannelSlAsyncFltrFlowRem_Type()
)
tmnxOFChannelSlAsyncFltrFlowRem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelSlAsyncFltrFlowRem.setStatus("current")
_TmnxOFChannelAuxiliaryID_Type = Unsigned32
_TmnxOFChannelAuxiliaryID_Object = MibTableColumn
tmnxOFChannelAuxiliaryID = _TmnxOFChannelAuxiliaryID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 16),
    _TmnxOFChannelAuxiliaryID_Type()
)
tmnxOFChannelAuxiliaryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelAuxiliaryID.setStatus("current")
_TmnxOFChannelSrcAddressType_Type = InetAddressType
_TmnxOFChannelSrcAddressType_Object = MibTableColumn
tmnxOFChannelSrcAddressType = _TmnxOFChannelSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 17),
    _TmnxOFChannelSrcAddressType_Type()
)
tmnxOFChannelSrcAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelSrcAddressType.setStatus("current")


class _TmnxOFChannelSrcAddress_Type(InetAddress):
    """Custom type tmnxOFChannelSrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOFChannelSrcAddress_Type.__name__ = "InetAddress"
_TmnxOFChannelSrcAddress_Object = MibTableColumn
tmnxOFChannelSrcAddress = _TmnxOFChannelSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 18),
    _TmnxOFChannelSrcAddress_Type()
)
tmnxOFChannelSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelSrcAddress.setStatus("current")
_TmnxOFChannelSrcPort_Type = InetPortNumber
_TmnxOFChannelSrcPort_Object = MibTableColumn
tmnxOFChannelSrcPort = _TmnxOFChannelSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 19),
    _TmnxOFChannelSrcPort_Type()
)
tmnxOFChannelSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelSrcPort.setStatus("current")
_TmnxOFChannelInfoServiceID_Type = TmnxServId
_TmnxOFChannelInfoServiceID_Object = MibTableColumn
tmnxOFChannelInfoServiceID = _TmnxOFChannelInfoServiceID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 20),
    _TmnxOFChannelInfoServiceID_Type()
)
tmnxOFChannelInfoServiceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelInfoServiceID.setStatus("current")
_TmnxOFChannelInfoLoopbckAddrType_Type = InetAddressType
_TmnxOFChannelInfoLoopbckAddrType_Object = MibTableColumn
tmnxOFChannelInfoLoopbckAddrType = _TmnxOFChannelInfoLoopbckAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 21),
    _TmnxOFChannelInfoLoopbckAddrType_Type()
)
tmnxOFChannelInfoLoopbckAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelInfoLoopbckAddrType.setStatus("current")


class _TmnxOFChannelInfoLoopbackAddr_Type(InetAddress):
    """Custom type tmnxOFChannelInfoLoopbackAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOFChannelInfoLoopbackAddr_Type.__name__ = "InetAddress"
_TmnxOFChannelInfoLoopbackAddr_Object = MibTableColumn
tmnxOFChannelInfoLoopbackAddr = _TmnxOFChannelInfoLoopbackAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 7, 1, 22),
    _TmnxOFChannelInfoLoopbackAddr_Type()
)
tmnxOFChannelInfoLoopbackAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelInfoLoopbackAddr.setStatus("current")
_TmnxOFChannelStatsTable_Object = MibTable
tmnxOFChannelStatsTable = _TmnxOFChannelStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxOFChannelStatsTable.setStatus("current")
_TmnxOFChannelStatsEntry_Object = MibTableRow
tmnxOFChannelStatsEntry = _TmnxOFChannelStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 8, 1)
)
tmnxOFChannelStatsEntry.setIndexNames(
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchName"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerAddressType"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerAddress"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerTCPPort"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelID"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelPacketType"),
)
if mibBuilder.loadTexts:
    tmnxOFChannelStatsEntry.setStatus("current")
_TmnxOFChannelPacketType_Type = TmnxOFPktType
_TmnxOFChannelPacketType_Object = MibTableColumn
tmnxOFChannelPacketType = _TmnxOFChannelPacketType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 8, 1, 1),
    _TmnxOFChannelPacketType_Type()
)
tmnxOFChannelPacketType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOFChannelPacketType.setStatus("current")
_TmnxOFChannelPacketTx_Type = Counter64
_TmnxOFChannelPacketTx_Object = MibTableColumn
tmnxOFChannelPacketTx = _TmnxOFChannelPacketTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 8, 1, 2),
    _TmnxOFChannelPacketTx_Type()
)
tmnxOFChannelPacketTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelPacketTx.setStatus("current")
_TmnxOFChannelPacketRx_Type = Counter64
_TmnxOFChannelPacketRx_Object = MibTableColumn
tmnxOFChannelPacketRx = _TmnxOFChannelPacketRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 8, 1, 3),
    _TmnxOFChannelPacketRx_Type()
)
tmnxOFChannelPacketRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelPacketRx.setStatus("current")
_TmnxOFChannelPacketErr_Type = Counter64
_TmnxOFChannelPacketErr_Object = MibTableColumn
tmnxOFChannelPacketErr = _TmnxOFChannelPacketErr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 8, 1, 4),
    _TmnxOFChannelPacketErr_Type()
)
tmnxOFChannelPacketErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelPacketErr.setStatus("current")
_TmnxOFChannelServiceID_Type = TmnxServId
_TmnxOFChannelServiceID_Object = MibTableColumn
tmnxOFChannelServiceID = _TmnxOFChannelServiceID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 8, 1, 5),
    _TmnxOFChannelServiceID_Type()
)
tmnxOFChannelServiceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelServiceID.setStatus("current")
_TmnxOFChannelLoopbckAddrType_Type = InetAddressType
_TmnxOFChannelLoopbckAddrType_Object = MibTableColumn
tmnxOFChannelLoopbckAddrType = _TmnxOFChannelLoopbckAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 8, 1, 6),
    _TmnxOFChannelLoopbckAddrType_Type()
)
tmnxOFChannelLoopbckAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelLoopbckAddrType.setStatus("current")


class _TmnxOFChannelLoopbackAddr_Type(InetAddress):
    """Custom type tmnxOFChannelLoopbackAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOFChannelLoopbackAddr_Type.__name__ = "InetAddress"
_TmnxOFChannelLoopbackAddr_Object = MibTableColumn
tmnxOFChannelLoopbackAddr = _TmnxOFChannelLoopbackAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 8, 1, 7),
    _TmnxOFChannelLoopbackAddr_Type()
)
tmnxOFChannelLoopbackAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFChannelLoopbackAddr.setStatus("current")
_TmnxOFPortStatsTable_Object = MibTable
tmnxOFPortStatsTable = _TmnxOFPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxOFPortStatsTable.setStatus("current")
_TmnxOFPortStatsEntry_Object = MibTableRow
tmnxOFPortStatsEntry = _TmnxOFPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 9, 1)
)
tmnxOFPortStatsEntry.setIndexNames(
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchName"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFPortID"),
)
if mibBuilder.loadTexts:
    tmnxOFPortStatsEntry.setStatus("current")
_TmnxOFPortID_Type = TmnxPortID
_TmnxOFPortID_Object = MibTableColumn
tmnxOFPortID = _TmnxOFPortID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 9, 1, 1),
    _TmnxOFPortID_Type()
)
tmnxOFPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOFPortID.setStatus("current")
_TmnxOFPortName_Type = TLNamedItemOrEmpty
_TmnxOFPortName_Object = MibTableColumn
tmnxOFPortName = _TmnxOFPortName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 9, 1, 2),
    _TmnxOFPortName_Type()
)
tmnxOFPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFPortName.setStatus("current")


class _TmnxOFPortType_Type(Integer32):
    """Custom type tmnxOFPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("openFlowPhysicalPort", 0),
          ("openFlowLogicalPort", 1),
          ("openFlowReservedPort", 2))
    )


_TmnxOFPortType_Type.__name__ = "Integer32"
_TmnxOFPortType_Object = MibTableColumn
tmnxOFPortType = _TmnxOFPortType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 9, 1, 3),
    _TmnxOFPortType_Type()
)
tmnxOFPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFPortType.setStatus("current")
_TmnxOFPortTxPackets_Type = Counter64
_TmnxOFPortTxPackets_Object = MibTableColumn
tmnxOFPortTxPackets = _TmnxOFPortTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 9, 1, 4),
    _TmnxOFPortTxPackets_Type()
)
tmnxOFPortTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFPortTxPackets.setStatus("current")
_TmnxOFPortTxBytes_Type = Counter64
_TmnxOFPortTxBytes_Object = MibTableColumn
tmnxOFPortTxBytes = _TmnxOFPortTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 1, 9, 1, 5),
    _TmnxOFPortTxBytes_Type()
)
tmnxOFPortTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFPortTxBytes.setStatus("current")
_TmnxOpenFlowNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxOpenFlowNotificationObjs = _TmnxOpenFlowNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 2)
)
_TmnxOFNotifyDescription_Type = DisplayString
_TmnxOFNotifyDescription_Object = MibScalar
tmnxOFNotifyDescription = _TmnxOFNotifyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 2, 1),
    _TmnxOFNotifyDescription_Type()
)
tmnxOFNotifyDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOFNotifyDescription.setStatus("current")
_TmnxOpenFlowControllerObjs_ObjectIdentity = ObjectIdentity
tmnxOpenFlowControllerObjs = _TmnxOpenFlowControllerObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3)
)
_TmnxOFCntrllerTableLastChanged_Type = TimeStamp
_TmnxOFCntrllerTableLastChanged_Object = MibScalar
tmnxOFCntrllerTableLastChanged = _TmnxOFCntrllerTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 1),
    _TmnxOFCntrllerTableLastChanged_Type()
)
tmnxOFCntrllerTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCntrllerTableLastChanged.setStatus("current")
_TmnxOFCntrllerTable_Object = MibTable
tmnxOFCntrllerTable = _TmnxOFCntrllerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxOFCntrllerTable.setStatus("current")
_TmnxOFCntrllerEntry_Object = MibTableRow
tmnxOFCntrllerEntry = _TmnxOFCntrllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 2, 1)
)
tmnxOFCntrllerEntry.setIndexNames(
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFCntrllerID"),
)
if mibBuilder.loadTexts:
    tmnxOFCntrllerEntry.setStatus("current")
_TmnxOFCntrllerID_Type = Integer32
_TmnxOFCntrllerID_Object = MibTableColumn
tmnxOFCntrllerID = _TmnxOFCntrllerID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 2, 1, 1),
    _TmnxOFCntrllerID_Type()
)
tmnxOFCntrllerID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOFCntrllerID.setStatus("current")
_TmnxOFCntrllerRowStatus_Type = RowStatus
_TmnxOFCntrllerRowStatus_Object = MibTableColumn
tmnxOFCntrllerRowStatus = _TmnxOFCntrllerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 2, 1, 2),
    _TmnxOFCntrllerRowStatus_Type()
)
tmnxOFCntrllerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFCntrllerRowStatus.setStatus("current")
_TmnxOFCntrllerLastChanged_Type = TimeStamp
_TmnxOFCntrllerLastChanged_Object = MibTableColumn
tmnxOFCntrllerLastChanged = _TmnxOFCntrllerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 2, 1, 3),
    _TmnxOFCntrllerLastChanged_Type()
)
tmnxOFCntrllerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCntrllerLastChanged.setStatus("current")


class _TmnxOFCntrllerDescription_Type(DisplayString):
    """Custom type tmnxOFCntrllerDescription based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TmnxOFCntrllerDescription_Type.__name__ = "DisplayString"
_TmnxOFCntrllerDescription_Object = MibTableColumn
tmnxOFCntrllerDescription = _TmnxOFCntrllerDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 2, 1, 4),
    _TmnxOFCntrllerDescription_Type()
)
tmnxOFCntrllerDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFCntrllerDescription.setStatus("current")


class _TmnxOFCntrllerVersion_Type(Unsigned32):
    """Custom type tmnxOFCntrllerVersion based on Unsigned32"""
    defaultValue = 4


_TmnxOFCntrllerVersion_Type.__name__ = "Unsigned32"
_TmnxOFCntrllerVersion_Object = MibTableColumn
tmnxOFCntrllerVersion = _TmnxOFCntrllerVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 2, 1, 5),
    _TmnxOFCntrllerVersion_Type()
)
tmnxOFCntrllerVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFCntrllerVersion.setStatus("current")


class _TmnxOFCntrllerRole_Type(Integer32):
    """Custom type tmnxOFCntrllerRole based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("equal", 0),
          ("master", 1),
          ("slave", 2))
    )


_TmnxOFCntrllerRole_Type.__name__ = "Integer32"
_TmnxOFCntrllerRole_Object = MibTableColumn
tmnxOFCntrllerRole = _TmnxOFCntrllerRole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 2, 1, 6),
    _TmnxOFCntrllerRole_Type()
)
tmnxOFCntrllerRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFCntrllerRole.setStatus("current")
_TmnxOFCntrllerAddressType_Type = InetAddressType
_TmnxOFCntrllerAddressType_Object = MibTableColumn
tmnxOFCntrllerAddressType = _TmnxOFCntrllerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 2, 1, 7),
    _TmnxOFCntrllerAddressType_Type()
)
tmnxOFCntrllerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFCntrllerAddressType.setStatus("current")


class _TmnxOFCntrllerAddress_Type(InetAddress):
    """Custom type tmnxOFCntrllerAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOFCntrllerAddress_Type.__name__ = "InetAddress"
_TmnxOFCntrllerAddress_Object = MibTableColumn
tmnxOFCntrllerAddress = _TmnxOFCntrllerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 2, 1, 8),
    _TmnxOFCntrllerAddress_Type()
)
tmnxOFCntrllerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFCntrllerAddress.setStatus("current")


class _TmnxOFCntrllerEchoInterval_Type(Unsigned32):
    """Custom type tmnxOFCntrllerEchoInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_TmnxOFCntrllerEchoInterval_Type.__name__ = "Unsigned32"
_TmnxOFCntrllerEchoInterval_Object = MibTableColumn
tmnxOFCntrllerEchoInterval = _TmnxOFCntrllerEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 2, 1, 9),
    _TmnxOFCntrllerEchoInterval_Type()
)
tmnxOFCntrllerEchoInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFCntrllerEchoInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOFCntrllerEchoInterval.setUnits("seconds")


class _TmnxOFCntrllerEchoMultiple_Type(Unsigned32):
    """Custom type tmnxOFCntrllerEchoMultiple based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 100),
    )


_TmnxOFCntrllerEchoMultiple_Type.__name__ = "Unsigned32"
_TmnxOFCntrllerEchoMultiple_Object = MibTableColumn
tmnxOFCntrllerEchoMultiple = _TmnxOFCntrllerEchoMultiple_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 2, 1, 10),
    _TmnxOFCntrllerEchoMultiple_Type()
)
tmnxOFCntrllerEchoMultiple.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFCntrllerEchoMultiple.setStatus("current")


class _TmnxOFCntrllerTCPPort_Type(InetPortNumber):
    """Custom type tmnxOFCntrllerTCPPort based on InetPortNumber"""
    defaultValue = 6653

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxOFCntrllerTCPPort_Type.__name__ = "InetPortNumber"
_TmnxOFCntrllerTCPPort_Object = MibTableColumn
tmnxOFCntrllerTCPPort = _TmnxOFCntrllerTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 2, 1, 11),
    _TmnxOFCntrllerTCPPort_Type()
)
tmnxOFCntrllerTCPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFCntrllerTCPPort.setStatus("current")


class _TmnxOFCntrllerAdminState_Type(TmnxAdminState):
    """Custom type tmnxOFCntrllerAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxOFCntrllerAdminState_Type.__name__ = "TmnxAdminState"
_TmnxOFCntrllerAdminState_Object = MibTableColumn
tmnxOFCntrllerAdminState = _TmnxOFCntrllerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 2, 1, 12),
    _TmnxOFCntrllerAdminState_Type()
)
tmnxOFCntrllerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFCntrllerAdminState.setStatus("current")


class _TmnxOFCntrllerTLSServProfName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOFCntrllerTLSServProfName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOFCntrllerTLSServProfName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOFCntrllerTLSServProfName_Object = MibTableColumn
tmnxOFCntrllerTLSServProfName = _TmnxOFCntrllerTLSServProfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 2, 1, 13),
    _TmnxOFCntrllerTLSServProfName_Type()
)
tmnxOFCntrllerTLSServProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFCntrllerTLSServProfName.setStatus("current")


class _TmnxOFCntrllerIpv6Address_Type(InetAddressIPv6):
    """Custom type tmnxOFCntrllerIpv6Address based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TmnxOFCntrllerIpv6Address_Type.__name__ = "InetAddressIPv6"
_TmnxOFCntrllerIpv6Address_Object = MibTableColumn
tmnxOFCntrllerIpv6Address = _TmnxOFCntrllerIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 2, 1, 14),
    _TmnxOFCntrllerIpv6Address_Type()
)
tmnxOFCntrllerIpv6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOFCntrllerIpv6Address.setStatus("current")
_TmnxOFCSwitchTable_Object = MibTable
tmnxOFCSwitchTable = _TmnxOFCSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxOFCSwitchTable.setStatus("current")
_TmnxOFCSwitchEntry_Object = MibTableRow
tmnxOFCSwitchEntry = _TmnxOFCSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 3, 1)
)
tmnxOFCSwitchEntry.setIndexNames(
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFCntrllerID"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchDataPathID"),
)
if mibBuilder.loadTexts:
    tmnxOFCSwitchEntry.setStatus("current")
_TmnxOFCSwitchDataPathID_Type = TmnxOFDatapathIdentifier
_TmnxOFCSwitchDataPathID_Object = MibTableColumn
tmnxOFCSwitchDataPathID = _TmnxOFCSwitchDataPathID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 3, 1, 1),
    _TmnxOFCSwitchDataPathID_Type()
)
tmnxOFCSwitchDataPathID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOFCSwitchDataPathID.setStatus("current")
_TmnxOFCSwitchName_Type = TNamedItemOrEmpty
_TmnxOFCSwitchName_Object = MibTableColumn
tmnxOFCSwitchName = _TmnxOFCSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 3, 1, 2),
    _TmnxOFCSwitchName_Type()
)
tmnxOFCSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCSwitchName.setStatus("current")
_TmnxOFCSwitchVersion_Type = Unsigned32
_TmnxOFCSwitchVersion_Object = MibTableColumn
tmnxOFCSwitchVersion = _TmnxOFCSwitchVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 3, 1, 3),
    _TmnxOFCSwitchVersion_Type()
)
tmnxOFCSwitchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCSwitchVersion.setStatus("current")
_TmnxOFCSwitchVendorName_Type = TLNamedItemOrEmpty
_TmnxOFCSwitchVendorName_Object = MibTableColumn
tmnxOFCSwitchVendorName = _TmnxOFCSwitchVendorName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 3, 1, 4),
    _TmnxOFCSwitchVendorName_Type()
)
tmnxOFCSwitchVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCSwitchVendorName.setStatus("current")
_TmnxOFCSwitchAddressType_Type = InetAddressType
_TmnxOFCSwitchAddressType_Object = MibTableColumn
tmnxOFCSwitchAddressType = _TmnxOFCSwitchAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 3, 1, 5),
    _TmnxOFCSwitchAddressType_Type()
)
tmnxOFCSwitchAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCSwitchAddressType.setStatus("current")


class _TmnxOFCSwitchAddress_Type(InetAddress):
    """Custom type tmnxOFCSwitchAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOFCSwitchAddress_Type.__name__ = "InetAddress"
_TmnxOFCSwitchAddress_Object = MibTableColumn
tmnxOFCSwitchAddress = _TmnxOFCSwitchAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 3, 1, 6),
    _TmnxOFCSwitchAddress_Type()
)
tmnxOFCSwitchAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCSwitchAddress.setStatus("current")


class _TmnxOFCSwitchFeaturesCapability_Type(Bits):
    """Custom type tmnxOFCSwitchFeaturesCapability based on Bits"""
    namedValues = NamedValues(
        *(("flowStats", 0),
          ("tableStats", 1),
          ("portStats", 2),
          ("groupStats", 3),
          ("future1", 4),
          ("ipReasm", 5),
          ("queueStats", 6),
          ("future2", 7),
          ("portBlocked", 8))
    )

_TmnxOFCSwitchFeaturesCapability_Type.__name__ = "Bits"
_TmnxOFCSwitchFeaturesCapability_Object = MibTableColumn
tmnxOFCSwitchFeaturesCapability = _TmnxOFCSwitchFeaturesCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 3, 1, 7),
    _TmnxOFCSwitchFeaturesCapability_Type()
)
tmnxOFCSwitchFeaturesCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCSwitchFeaturesCapability.setStatus("current")
_TmnxOFCSwitchFlowTableMaxSize_Type = Unsigned32
_TmnxOFCSwitchFlowTableMaxSize_Object = MibTableColumn
tmnxOFCSwitchFlowTableMaxSize = _TmnxOFCSwitchFlowTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 3, 1, 8),
    _TmnxOFCSwitchFlowTableMaxSize_Type()
)
tmnxOFCSwitchFlowTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCSwitchFlowTableMaxSize.setStatus("current")
_TmnxOFCSwitchMeterTableMaxSize_Type = Unsigned32
_TmnxOFCSwitchMeterTableMaxSize_Object = MibTableColumn
tmnxOFCSwitchMeterTableMaxSize = _TmnxOFCSwitchMeterTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 3, 1, 9),
    _TmnxOFCSwitchMeterTableMaxSize_Type()
)
tmnxOFCSwitchMeterTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCSwitchMeterTableMaxSize.setStatus("current")
_TmnxOFCSwitchPortNumEntries_Type = Unsigned32
_TmnxOFCSwitchPortNumEntries_Object = MibTableColumn
tmnxOFCSwitchPortNumEntries = _TmnxOFCSwitchPortNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 3, 1, 10),
    _TmnxOFCSwitchPortNumEntries_Type()
)
tmnxOFCSwitchPortNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCSwitchPortNumEntries.setStatus("current")
_TmnxOFCSwitchFlowNumEntries_Type = Unsigned32
_TmnxOFCSwitchFlowNumEntries_Object = MibTableColumn
tmnxOFCSwitchFlowNumEntries = _TmnxOFCSwitchFlowNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 3, 1, 11),
    _TmnxOFCSwitchFlowNumEntries_Type()
)
tmnxOFCSwitchFlowNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCSwitchFlowNumEntries.setStatus("current")
_TmnxOFCSwitchMeterNumEntries_Type = Unsigned32
_TmnxOFCSwitchMeterNumEntries_Object = MibTableColumn
tmnxOFCSwitchMeterNumEntries = _TmnxOFCSwitchMeterNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 3, 1, 12),
    _TmnxOFCSwitchMeterNumEntries_Type()
)
tmnxOFCSwitchMeterNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCSwitchMeterNumEntries.setStatus("current")
_TmnxOFCSwitchMaxFlowTables_Type = Unsigned32
_TmnxOFCSwitchMaxFlowTables_Object = MibTableColumn
tmnxOFCSwitchMaxFlowTables = _TmnxOFCSwitchMaxFlowTables_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 3, 1, 13),
    _TmnxOFCSwitchMaxFlowTables_Type()
)
tmnxOFCSwitchMaxFlowTables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCSwitchMaxFlowTables.setStatus("current")
_TmnxOFCSwitchGroupNumEntries_Type = Unsigned32
_TmnxOFCSwitchGroupNumEntries_Object = MibTableColumn
tmnxOFCSwitchGroupNumEntries = _TmnxOFCSwitchGroupNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 3, 1, 14),
    _TmnxOFCSwitchGroupNumEntries_Type()
)
tmnxOFCSwitchGroupNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCSwitchGroupNumEntries.setStatus("current")
_TmnxOFCSwitchGrpAllMaxEntry_Type = Unsigned32
_TmnxOFCSwitchGrpAllMaxEntry_Object = MibTableColumn
tmnxOFCSwitchGrpAllMaxEntry = _TmnxOFCSwitchGrpAllMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 3, 1, 15),
    _TmnxOFCSwitchGrpAllMaxEntry_Type()
)
tmnxOFCSwitchGrpAllMaxEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCSwitchGrpAllMaxEntry.setStatus("current")
_TmnxOFCSwitchGrpSelectMaxEntry_Type = Unsigned32
_TmnxOFCSwitchGrpSelectMaxEntry_Object = MibTableColumn
tmnxOFCSwitchGrpSelectMaxEntry = _TmnxOFCSwitchGrpSelectMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 3, 1, 16),
    _TmnxOFCSwitchGrpSelectMaxEntry_Type()
)
tmnxOFCSwitchGrpSelectMaxEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCSwitchGrpSelectMaxEntry.setStatus("current")
_TmnxOFCSwitchGrpIndirectMaxEntry_Type = Unsigned32
_TmnxOFCSwitchGrpIndirectMaxEntry_Object = MibTableColumn
tmnxOFCSwitchGrpIndirectMaxEntry = _TmnxOFCSwitchGrpIndirectMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 3, 1, 17),
    _TmnxOFCSwitchGrpIndirectMaxEntry_Type()
)
tmnxOFCSwitchGrpIndirectMaxEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCSwitchGrpIndirectMaxEntry.setStatus("current")
_TmnxOFCSwitchGrpFastFailMaxEntry_Type = Unsigned32
_TmnxOFCSwitchGrpFastFailMaxEntry_Object = MibTableColumn
tmnxOFCSwitchGrpFastFailMaxEntry = _TmnxOFCSwitchGrpFastFailMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 3, 1, 18),
    _TmnxOFCSwitchGrpFastFailMaxEntry_Type()
)
tmnxOFCSwitchGrpFastFailMaxEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCSwitchGrpFastFailMaxEntry.setStatus("current")
_TmnxOFCSwitchChannelInfoTable_Object = MibTable
tmnxOFCSwitchChannelInfoTable = _TmnxOFCSwitchChannelInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxOFCSwitchChannelInfoTable.setStatus("current")
_TmnxOFCSwitchChannelInfoEntry_Object = MibTableRow
tmnxOFCSwitchChannelInfoEntry = _TmnxOFCSwitchChannelInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 4, 1)
)
tmnxOFCSwitchChannelInfoEntry.setIndexNames(
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFCntrllerID"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchDataPathID"),
    (0, "TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchChannelID"),
)
if mibBuilder.loadTexts:
    tmnxOFCSwitchChannelInfoEntry.setStatus("current")
_TmnxOFCSwitchChannelID_Type = Unsigned32
_TmnxOFCSwitchChannelID_Object = MibTableColumn
tmnxOFCSwitchChannelID = _TmnxOFCSwitchChannelID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 4, 1, 1),
    _TmnxOFCSwitchChannelID_Type()
)
tmnxOFCSwitchChannelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOFCSwitchChannelID.setStatus("current")
_TmnxOFCSwitchChannelConnUpTime_Type = Unsigned32
_TmnxOFCSwitchChannelConnUpTime_Object = MibTableColumn
tmnxOFCSwitchChannelConnUpTime = _TmnxOFCSwitchChannelConnUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 4, 1, 2),
    _TmnxOFCSwitchChannelConnUpTime_Type()
)
tmnxOFCSwitchChannelConnUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCSwitchChannelConnUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOFCSwitchChannelConnUpTime.setUnits("seconds")


class _TmnxOFCSwitchChannelType_Type(Integer32):
    """Custom type tmnxOFCSwitchChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("auxiliary", 2))
    )


_TmnxOFCSwitchChannelType_Type.__name__ = "Integer32"
_TmnxOFCSwitchChannelType_Object = MibTableColumn
tmnxOFCSwitchChannelType = _TmnxOFCSwitchChannelType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 4, 1, 3),
    _TmnxOFCSwitchChannelType_Type()
)
tmnxOFCSwitchChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCSwitchChannelType.setStatus("current")


class _TmnxOFCSwitchChannelOperState_Type(Integer32):
    """Custom type tmnxOFCSwitchChannelOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_TmnxOFCSwitchChannelOperState_Type.__name__ = "Integer32"
_TmnxOFCSwitchChannelOperState_Object = MibTableColumn
tmnxOFCSwitchChannelOperState = _TmnxOFCSwitchChannelOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 4, 1, 4),
    _TmnxOFCSwitchChannelOperState_Type()
)
tmnxOFCSwitchChannelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCSwitchChannelOperState.setStatus("current")
_TmnxOFCSwitchChannelTlsEnabled_Type = TmnxEnabledDisabled
_TmnxOFCSwitchChannelTlsEnabled_Object = MibTableColumn
tmnxOFCSwitchChannelTlsEnabled = _TmnxOFCSwitchChannelTlsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 93, 3, 4, 1, 5),
    _TmnxOFCSwitchChannelTlsEnabled_Type()
)
tmnxOFCSwitchChannelTlsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOFCSwitchChannelTlsEnabled.setStatus("current")
_TmnxOpenFlowNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxOpenFlowNotifyPrefix = _TmnxOpenFlowNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 93)
)
_TmnxOpenFlowNotification_ObjectIdentity = ObjectIdentity
tmnxOpenFlowNotification = _TmnxOpenFlowNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 93, 0)
)

# Managed Objects groups

tmnxOpenFlowConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 2, 1, 1)
)
tmnxOpenFlowConfigGroup.setObjects(
      *(("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchTableLastChanged"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchRowStatus"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchLastChanged"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchEchoInterval"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchEchoMultiple"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchLogicalPortStatus"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchAdminState"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchDescription"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchDataPathID"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchFeaturesBufferSize"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchFeaturesNumTables"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchFeaturesCapability"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerTableLastChanged"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerRowStatus"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerLastChanged"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerRole"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerGenID"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowTableTableLastChanged"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowTableRowStatus"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowTableLastChanged"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowTableMaxSize"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowTableNoMatchAction"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowTableNumEntries"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowTableOperStatus"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelVersion"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelType"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelOperStatus"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelOperFlags"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelEchoTimeExpiry"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelHoldTimeExpiry"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelConnRetryExpiry"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelConnUpTime"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelMEAsyncFltrPacketIn"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelSlAsyncFltrPacketIn"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelMEAsyncFltrPortSts"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelSlAsyncFltrPortSts"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelMEAsyncFltrFlowRem"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelSlAsyncFltrFlowRem"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelPacketTx"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelPacketRx"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelPacketErr"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFPortName"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFPortType"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFPortTxPackets"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFPortTxBytes"))
)
if mibBuilder.loadTexts:
    tmnxOpenFlowConfigGroup.setStatus("current")

tmnxOpenFlowNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 2, 1, 2)
)
tmnxOpenFlowNotifyObjsGroup.setObjects(
    ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFNotifyDescription")
)
if mibBuilder.loadTexts:
    tmnxOpenFlowNotifyObjsGroup.setStatus("current")

tmnxOpenFlowV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 2, 2, 1)
)
tmnxOpenFlowV13v0Group.setObjects(
    ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowTableSwitchDefCookie")
)
if mibBuilder.loadTexts:
    tmnxOpenFlowV13v0Group.setStatus("current")

tmnxOpenFlowAuxChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 2, 3, 1)
)
tmnxOpenFlowAuxChannelGroup.setObjects(
      *(("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchAuxChannelEnabled"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelAuxiliaryID"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelSrcAddressType"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelSrcAddress"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelSrcPort"))
)
if mibBuilder.loadTexts:
    tmnxOpenFlowAuxChannelGroup.setStatus("current")

tmnxOpenFlowConfigV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 2, 4, 1)
)
tmnxOpenFlowConfigV15v0Group.setObjects(
    ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerTLSProfileName")
)
if mibBuilder.loadTexts:
    tmnxOpenFlowConfigV15v0Group.setStatus("current")

tmnxOpenFlowSwitchV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 2, 4, 2)
)
tmnxOpenFlowSwitchV15v0Group.setObjects(
    ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchID")
)
if mibBuilder.loadTexts:
    tmnxOpenFlowSwitchV15v0Group.setStatus("current")

tmnxOpenFlowSwitchV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 2, 5, 1)
)
tmnxOpenFlowSwitchV16v0Group.setObjects(
      *(("TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerServiceID"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerLoopbckAddrType"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerLoopbackAddr"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelInfoServiceID"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelInfoLoopbckAddrType"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelInfoLoopbackAddr"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelServiceID"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelLoopbckAddrType"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFChannelLoopbackAddr"))
)
if mibBuilder.loadTexts:
    tmnxOpenFlowSwitchV16v0Group.setStatus("current")

tmnxOFSwitchSvcV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 2, 5, 2)
)
tmnxOFSwitchSvcV16v0Group.setObjects(
    ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerSvcName")
)
if mibBuilder.loadTexts:
    tmnxOFSwitchSvcV16v0Group.setStatus("current")

tmnxOFControllerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 4, 1)
)
tmnxOFControllerGroup.setObjects(
      *(("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCntrllerTableLastChanged"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCntrllerRowStatus"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCntrllerLastChanged"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCntrllerDescription"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCntrllerVersion"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCntrllerRole"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCntrllerAddressType"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCntrllerAddress"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCntrllerEchoInterval"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCntrllerEchoMultiple"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCntrllerTCPPort"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCntrllerAdminState"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCntrllerTLSServProfName"))
)
if mibBuilder.loadTexts:
    tmnxOFControllerGroup.setStatus("current")

tmnxOFControllerSwitchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 4, 2)
)
tmnxOFControllerSwitchGroup.setObjects(
      *(("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchName"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchVersion"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchVendorName"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchAddressType"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchAddress"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchFeaturesCapability"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchFlowTableMaxSize"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchMeterTableMaxSize"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchPortNumEntries"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchFlowNumEntries"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchMeterNumEntries"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchChannelConnUpTime"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchChannelType"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchChannelOperState"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchChannelTlsEnabled"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchMaxFlowTables"))
)
if mibBuilder.loadTexts:
    tmnxOFControllerSwitchGroup.setStatus("current")

tmnxOFControllerV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 4, 3)
)
tmnxOFControllerV19v0Group.setObjects(
    ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCntrllerIpv6Address")
)
if mibBuilder.loadTexts:
    tmnxOFControllerV19v0Group.setStatus("current")

tmnxOFCSwitchGroupV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 4, 4)
)
tmnxOFCSwitchGroupV19v0Group.setObjects(
      *(("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchGroupNumEntries"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchGrpAllMaxEntry"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchGrpSelectMaxEntry"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchGrpIndirectMaxEntry"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchGrpFastFailMaxEntry"))
)
if mibBuilder.loadTexts:
    tmnxOFCSwitchGroupV19v0Group.setStatus("current")


# Notification objects

tmnxOFFlowEntryInsertFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 93, 0, 1)
)
tmnxOFFlowEntryInsertFailed.setObjects(
      *(("TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowTableNoMatchAction"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowTableOperStatus"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxOFFlowEntryInsertFailed.setStatus(
        "current"
    )


# Notifications groups

tmnxOpenFlowNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 2, 1, 3)
)
tmnxOpenFlowNotificationGroup.setObjects(
    ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFFlowEntryInsertFailed")
)
if mibBuilder.loadTexts:
    tmnxOpenFlowNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxOpenFlowComplianceV12v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 1, 1)
)
tmnxOpenFlowComplianceV12v0.setObjects(
      *(("TIMETRA-OPEN-FLOW-MIB", "tmnxOpenFlowConfigGroup"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOpenFlowNotifyObjsGroup"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOpenFlowNotificationGroup"))
)
if mibBuilder.loadTexts:
    tmnxOpenFlowComplianceV12v0.setStatus(
        "current"
    )

tmnxOpenFlowComplianceV13v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 1, 2)
)
tmnxOpenFlowComplianceV13v0.setObjects(
    ("TIMETRA-OPEN-FLOW-MIB", "tmnxOpenFlowV13v0Group")
)
if mibBuilder.loadTexts:
    tmnxOpenFlowComplianceV13v0.setStatus(
        "current"
    )

tmnxOpenFlowComplianceV14v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 1, 3)
)
tmnxOpenFlowComplianceV14v0.setObjects(
    ("TIMETRA-OPEN-FLOW-MIB", "tmnxOpenFlowAuxChannelGroup")
)
if mibBuilder.loadTexts:
    tmnxOpenFlowComplianceV14v0.setStatus(
        "current"
    )

tmnxOpenFlowComplianceV15v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 1, 4)
)
tmnxOpenFlowComplianceV15v0.setObjects(
      *(("TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerGroup"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerSwitchGroup"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOpenFlowConfigV15v0Group"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOpenFlowSwitchV15v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOpenFlowComplianceV15v0.setStatus(
        "current"
    )

tmnxOpenFlowComplianceV16v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 1, 5)
)
tmnxOpenFlowComplianceV16v0.setObjects(
      *(("TIMETRA-OPEN-FLOW-MIB", "tmnxOpenFlowSwitchV16v0Group"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFSwitchSvcV16v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOpenFlowComplianceV16v0.setStatus(
        "current"
    )

tmnxOpenFlowComplianceV19v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 93, 1, 6)
)
tmnxOpenFlowComplianceV19v0.setObjects(
      *(("TIMETRA-OPEN-FLOW-MIB", "tmnxOFControllerV19v0Group"),
        ("TIMETRA-OPEN-FLOW-MIB", "tmnxOFCSwitchGroupV19v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOpenFlowComplianceV19v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-OPEN-FLOW-MIB",
    **{"TmnxOFDatapathIdentifier": TmnxOFDatapathIdentifier,
       "TmnxOFPktType": TmnxOFPktType,
       "TmnxOFAsyncFltrPacketIn": TmnxOFAsyncFltrPacketIn,
       "TmnxOFAsyncFltrPortStatus": TmnxOFAsyncFltrPortStatus,
       "TmnxOFAsyncFltrFlowRemoved": TmnxOFAsyncFltrFlowRemoved,
       "timetraOpenFlowMIBModule": timetraOpenFlowMIBModule,
       "tmnxOpenFlowConformance": tmnxOpenFlowConformance,
       "tmnxOpenFlowCompliances": tmnxOpenFlowCompliances,
       "tmnxOpenFlowComplianceV12v0": tmnxOpenFlowComplianceV12v0,
       "tmnxOpenFlowComplianceV13v0": tmnxOpenFlowComplianceV13v0,
       "tmnxOpenFlowComplianceV14v0": tmnxOpenFlowComplianceV14v0,
       "tmnxOpenFlowComplianceV15v0": tmnxOpenFlowComplianceV15v0,
       "tmnxOpenFlowComplianceV16v0": tmnxOpenFlowComplianceV16v0,
       "tmnxOpenFlowComplianceV19v0": tmnxOpenFlowComplianceV19v0,
       "tmnxOpenFlowGroups": tmnxOpenFlowGroups,
       "tmnxOpenFlowV12v0Groups": tmnxOpenFlowV12v0Groups,
       "tmnxOpenFlowConfigGroup": tmnxOpenFlowConfigGroup,
       "tmnxOpenFlowNotifyObjsGroup": tmnxOpenFlowNotifyObjsGroup,
       "tmnxOpenFlowNotificationGroup": tmnxOpenFlowNotificationGroup,
       "tmnxOpenFlowV13v0Groups": tmnxOpenFlowV13v0Groups,
       "tmnxOpenFlowV13v0Group": tmnxOpenFlowV13v0Group,
       "tmnxOpenFlowV14v0Groups": tmnxOpenFlowV14v0Groups,
       "tmnxOpenFlowAuxChannelGroup": tmnxOpenFlowAuxChannelGroup,
       "tmnxOpenFlowV15v0Groups": tmnxOpenFlowV15v0Groups,
       "tmnxOpenFlowConfigV15v0Group": tmnxOpenFlowConfigV15v0Group,
       "tmnxOpenFlowSwitchV15v0Group": tmnxOpenFlowSwitchV15v0Group,
       "tmnxOpenFlowV16v0Groups": tmnxOpenFlowV16v0Groups,
       "tmnxOpenFlowSwitchV16v0Group": tmnxOpenFlowSwitchV16v0Group,
       "tmnxOFSwitchSvcV16v0Group": tmnxOFSwitchSvcV16v0Group,
       "tmnxOpenFlowNotifGroups": tmnxOpenFlowNotifGroups,
       "tmnxOpenFlowControllerGroups": tmnxOpenFlowControllerGroups,
       "tmnxOFControllerGroup": tmnxOFControllerGroup,
       "tmnxOFControllerSwitchGroup": tmnxOFControllerSwitchGroup,
       "tmnxOFControllerV19v0Group": tmnxOFControllerV19v0Group,
       "tmnxOFCSwitchGroupV19v0Group": tmnxOFCSwitchGroupV19v0Group,
       "tmnxOpenFlow": tmnxOpenFlow,
       "tmnxOpenFlowObjs": tmnxOpenFlowObjs,
       "tmnxOFSwitchTableLastChanged": tmnxOFSwitchTableLastChanged,
       "tmnxOFSwitchTable": tmnxOFSwitchTable,
       "tmnxOFSwitchEntry": tmnxOFSwitchEntry,
       "tmnxOFSwitchName": tmnxOFSwitchName,
       "tmnxOFSwitchRowStatus": tmnxOFSwitchRowStatus,
       "tmnxOFSwitchLastChanged": tmnxOFSwitchLastChanged,
       "tmnxOFSwitchEchoInterval": tmnxOFSwitchEchoInterval,
       "tmnxOFSwitchEchoMultiple": tmnxOFSwitchEchoMultiple,
       "tmnxOFSwitchLogicalPortStatus": tmnxOFSwitchLogicalPortStatus,
       "tmnxOFSwitchAdminState": tmnxOFSwitchAdminState,
       "tmnxOFSwitchDescription": tmnxOFSwitchDescription,
       "tmnxOFSwitchDataPathID": tmnxOFSwitchDataPathID,
       "tmnxOFSwitchFeaturesBufferSize": tmnxOFSwitchFeaturesBufferSize,
       "tmnxOFSwitchFeaturesNumTables": tmnxOFSwitchFeaturesNumTables,
       "tmnxOFSwitchFeaturesCapability": tmnxOFSwitchFeaturesCapability,
       "tmnxOFSwitchAuxChannelEnabled": tmnxOFSwitchAuxChannelEnabled,
       "tmnxOFSwitchID": tmnxOFSwitchID,
       "tmnxOFControllerTableLastChanged": tmnxOFControllerTableLastChanged,
       "tmnxOFControllerTable": tmnxOFControllerTable,
       "tmnxOFControllerEntry": tmnxOFControllerEntry,
       "tmnxOFControllerAddressType": tmnxOFControllerAddressType,
       "tmnxOFControllerAddress": tmnxOFControllerAddress,
       "tmnxOFControllerTCPPort": tmnxOFControllerTCPPort,
       "tmnxOFControllerRowStatus": tmnxOFControllerRowStatus,
       "tmnxOFControllerLastChanged": tmnxOFControllerLastChanged,
       "tmnxOFControllerRole": tmnxOFControllerRole,
       "tmnxOFControllerGenID": tmnxOFControllerGenID,
       "tmnxOFControllerTLSProfileName": tmnxOFControllerTLSProfileName,
       "tmnxOFControllerServiceID": tmnxOFControllerServiceID,
       "tmnxOFControllerLoopbckAddrType": tmnxOFControllerLoopbckAddrType,
       "tmnxOFControllerLoopbackAddr": tmnxOFControllerLoopbackAddr,
       "tmnxOFControllerSvcName": tmnxOFControllerSvcName,
       "tmnxOFFlowTableTableLastChanged": tmnxOFFlowTableTableLastChanged,
       "tmnxOFFlowTableTable": tmnxOFFlowTableTable,
       "tmnxOFFlowTableEntry": tmnxOFFlowTableEntry,
       "tmnxOFFlowTableId": tmnxOFFlowTableId,
       "tmnxOFFlowTableRowStatus": tmnxOFFlowTableRowStatus,
       "tmnxOFFlowTableLastChanged": tmnxOFFlowTableLastChanged,
       "tmnxOFFlowTableMaxSize": tmnxOFFlowTableMaxSize,
       "tmnxOFFlowTableNoMatchAction": tmnxOFFlowTableNoMatchAction,
       "tmnxOFFlowTableNumEntries": tmnxOFFlowTableNumEntries,
       "tmnxOFFlowTableOperStatus": tmnxOFFlowTableOperStatus,
       "tmnxOFFlowTableSwitchDefCookie": tmnxOFFlowTableSwitchDefCookie,
       "tmnxOFChannelInfoTable": tmnxOFChannelInfoTable,
       "tmnxOFChannelInfoEntry": tmnxOFChannelInfoEntry,
       "tmnxOFChannelID": tmnxOFChannelID,
       "tmnxOFChannelVersion": tmnxOFChannelVersion,
       "tmnxOFChannelType": tmnxOFChannelType,
       "tmnxOFChannelOperStatus": tmnxOFChannelOperStatus,
       "tmnxOFChannelOperFlags": tmnxOFChannelOperFlags,
       "tmnxOFChannelEchoTimeExpiry": tmnxOFChannelEchoTimeExpiry,
       "tmnxOFChannelHoldTimeExpiry": tmnxOFChannelHoldTimeExpiry,
       "tmnxOFChannelConnRetryExpiry": tmnxOFChannelConnRetryExpiry,
       "tmnxOFChannelConnUpTime": tmnxOFChannelConnUpTime,
       "tmnxOFChannelMEAsyncFltrPacketIn": tmnxOFChannelMEAsyncFltrPacketIn,
       "tmnxOFChannelSlAsyncFltrPacketIn": tmnxOFChannelSlAsyncFltrPacketIn,
       "tmnxOFChannelMEAsyncFltrPortSts": tmnxOFChannelMEAsyncFltrPortSts,
       "tmnxOFChannelSlAsyncFltrPortSts": tmnxOFChannelSlAsyncFltrPortSts,
       "tmnxOFChannelMEAsyncFltrFlowRem": tmnxOFChannelMEAsyncFltrFlowRem,
       "tmnxOFChannelSlAsyncFltrFlowRem": tmnxOFChannelSlAsyncFltrFlowRem,
       "tmnxOFChannelAuxiliaryID": tmnxOFChannelAuxiliaryID,
       "tmnxOFChannelSrcAddressType": tmnxOFChannelSrcAddressType,
       "tmnxOFChannelSrcAddress": tmnxOFChannelSrcAddress,
       "tmnxOFChannelSrcPort": tmnxOFChannelSrcPort,
       "tmnxOFChannelInfoServiceID": tmnxOFChannelInfoServiceID,
       "tmnxOFChannelInfoLoopbckAddrType": tmnxOFChannelInfoLoopbckAddrType,
       "tmnxOFChannelInfoLoopbackAddr": tmnxOFChannelInfoLoopbackAddr,
       "tmnxOFChannelStatsTable": tmnxOFChannelStatsTable,
       "tmnxOFChannelStatsEntry": tmnxOFChannelStatsEntry,
       "tmnxOFChannelPacketType": tmnxOFChannelPacketType,
       "tmnxOFChannelPacketTx": tmnxOFChannelPacketTx,
       "tmnxOFChannelPacketRx": tmnxOFChannelPacketRx,
       "tmnxOFChannelPacketErr": tmnxOFChannelPacketErr,
       "tmnxOFChannelServiceID": tmnxOFChannelServiceID,
       "tmnxOFChannelLoopbckAddrType": tmnxOFChannelLoopbckAddrType,
       "tmnxOFChannelLoopbackAddr": tmnxOFChannelLoopbackAddr,
       "tmnxOFPortStatsTable": tmnxOFPortStatsTable,
       "tmnxOFPortStatsEntry": tmnxOFPortStatsEntry,
       "tmnxOFPortID": tmnxOFPortID,
       "tmnxOFPortName": tmnxOFPortName,
       "tmnxOFPortType": tmnxOFPortType,
       "tmnxOFPortTxPackets": tmnxOFPortTxPackets,
       "tmnxOFPortTxBytes": tmnxOFPortTxBytes,
       "tmnxOpenFlowNotificationObjs": tmnxOpenFlowNotificationObjs,
       "tmnxOFNotifyDescription": tmnxOFNotifyDescription,
       "tmnxOpenFlowControllerObjs": tmnxOpenFlowControllerObjs,
       "tmnxOFCntrllerTableLastChanged": tmnxOFCntrllerTableLastChanged,
       "tmnxOFCntrllerTable": tmnxOFCntrllerTable,
       "tmnxOFCntrllerEntry": tmnxOFCntrllerEntry,
       "tmnxOFCntrllerID": tmnxOFCntrllerID,
       "tmnxOFCntrllerRowStatus": tmnxOFCntrllerRowStatus,
       "tmnxOFCntrllerLastChanged": tmnxOFCntrllerLastChanged,
       "tmnxOFCntrllerDescription": tmnxOFCntrllerDescription,
       "tmnxOFCntrllerVersion": tmnxOFCntrllerVersion,
       "tmnxOFCntrllerRole": tmnxOFCntrllerRole,
       "tmnxOFCntrllerAddressType": tmnxOFCntrllerAddressType,
       "tmnxOFCntrllerAddress": tmnxOFCntrllerAddress,
       "tmnxOFCntrllerEchoInterval": tmnxOFCntrllerEchoInterval,
       "tmnxOFCntrllerEchoMultiple": tmnxOFCntrllerEchoMultiple,
       "tmnxOFCntrllerTCPPort": tmnxOFCntrllerTCPPort,
       "tmnxOFCntrllerAdminState": tmnxOFCntrllerAdminState,
       "tmnxOFCntrllerTLSServProfName": tmnxOFCntrllerTLSServProfName,
       "tmnxOFCntrllerIpv6Address": tmnxOFCntrllerIpv6Address,
       "tmnxOFCSwitchTable": tmnxOFCSwitchTable,
       "tmnxOFCSwitchEntry": tmnxOFCSwitchEntry,
       "tmnxOFCSwitchDataPathID": tmnxOFCSwitchDataPathID,
       "tmnxOFCSwitchName": tmnxOFCSwitchName,
       "tmnxOFCSwitchVersion": tmnxOFCSwitchVersion,
       "tmnxOFCSwitchVendorName": tmnxOFCSwitchVendorName,
       "tmnxOFCSwitchAddressType": tmnxOFCSwitchAddressType,
       "tmnxOFCSwitchAddress": tmnxOFCSwitchAddress,
       "tmnxOFCSwitchFeaturesCapability": tmnxOFCSwitchFeaturesCapability,
       "tmnxOFCSwitchFlowTableMaxSize": tmnxOFCSwitchFlowTableMaxSize,
       "tmnxOFCSwitchMeterTableMaxSize": tmnxOFCSwitchMeterTableMaxSize,
       "tmnxOFCSwitchPortNumEntries": tmnxOFCSwitchPortNumEntries,
       "tmnxOFCSwitchFlowNumEntries": tmnxOFCSwitchFlowNumEntries,
       "tmnxOFCSwitchMeterNumEntries": tmnxOFCSwitchMeterNumEntries,
       "tmnxOFCSwitchMaxFlowTables": tmnxOFCSwitchMaxFlowTables,
       "tmnxOFCSwitchGroupNumEntries": tmnxOFCSwitchGroupNumEntries,
       "tmnxOFCSwitchGrpAllMaxEntry": tmnxOFCSwitchGrpAllMaxEntry,
       "tmnxOFCSwitchGrpSelectMaxEntry": tmnxOFCSwitchGrpSelectMaxEntry,
       "tmnxOFCSwitchGrpIndirectMaxEntry": tmnxOFCSwitchGrpIndirectMaxEntry,
       "tmnxOFCSwitchGrpFastFailMaxEntry": tmnxOFCSwitchGrpFastFailMaxEntry,
       "tmnxOFCSwitchChannelInfoTable": tmnxOFCSwitchChannelInfoTable,
       "tmnxOFCSwitchChannelInfoEntry": tmnxOFCSwitchChannelInfoEntry,
       "tmnxOFCSwitchChannelID": tmnxOFCSwitchChannelID,
       "tmnxOFCSwitchChannelConnUpTime": tmnxOFCSwitchChannelConnUpTime,
       "tmnxOFCSwitchChannelType": tmnxOFCSwitchChannelType,
       "tmnxOFCSwitchChannelOperState": tmnxOFCSwitchChannelOperState,
       "tmnxOFCSwitchChannelTlsEnabled": tmnxOFCSwitchChannelTlsEnabled,
       "tmnxOpenFlowNotifyPrefix": tmnxOpenFlowNotifyPrefix,
       "tmnxOpenFlowNotification": tmnxOpenFlowNotification,
       "tmnxOFFlowEntryInsertFailed": tmnxOFFlowEntryInsertFailed}
)
