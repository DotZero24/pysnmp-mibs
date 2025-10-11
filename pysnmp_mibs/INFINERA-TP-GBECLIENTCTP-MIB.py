# SNMP MIB module (INFINERA-TP-GBECLIENTCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-GBECLIENTCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:33 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(InfnClientAction,
 InfnEnableDisable,
 InfnGigeMaxPacketLen,
 InfnLoopbackType,
 InfnPmHistStatsControl,
 InfnSMQ,
 InfnServiceMode,
 InfnServiceType,
 InfnTribDisableAction) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnClientAction",
    "InfnEnableDisable",
    "InfnGigeMaxPacketLen",
    "InfnLoopbackType",
    "InfnPmHistStatsControl",
    "InfnSMQ",
    "InfnServiceMode",
    "InfnServiceType",
    "InfnTribDisableAction")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

gbeClientCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GbeClientCtpTable_Object = MibTable
gbeClientCtpTable = _GbeClientCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1)
)
if mibBuilder.loadTexts:
    gbeClientCtpTable.setStatus("current")
_GbeClientCtpEntry_Object = MibTableRow
gbeClientCtpEntry = _GbeClientCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1)
)
gbeClientCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gbeClientCtpEntry.setStatus("current")
_GbeClientCtpSupportingCircuitIdList_Type = DisplayString
_GbeClientCtpSupportingCircuitIdList_Object = MibTableColumn
gbeClientCtpSupportingCircuitIdList = _GbeClientCtpSupportingCircuitIdList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 1),
    _GbeClientCtpSupportingCircuitIdList_Type()
)
gbeClientCtpSupportingCircuitIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbeClientCtpSupportingCircuitIdList.setStatus("current")
_GbeClientCtpLoopback_Type = InfnLoopbackType
_GbeClientCtpLoopback_Object = MibTableColumn
gbeClientCtpLoopback = _GbeClientCtpLoopback_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 2),
    _GbeClientCtpLoopback_Type()
)
gbeClientCtpLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpLoopback.setStatus("current")
_GbeClientCtpPmHistStatsEnable_Type = InfnPmHistStatsControl
_GbeClientCtpPmHistStatsEnable_Object = MibTableColumn
gbeClientCtpPmHistStatsEnable = _GbeClientCtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 3),
    _GbeClientCtpPmHistStatsEnable_Type()
)
gbeClientCtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpPmHistStatsEnable.setStatus("current")
_GbeClientCtpConfiguredServiceType_Type = InfnServiceType
_GbeClientCtpConfiguredServiceType_Object = MibTableColumn
gbeClientCtpConfiguredServiceType = _GbeClientCtpConfiguredServiceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 4),
    _GbeClientCtpConfiguredServiceType_Type()
)
gbeClientCtpConfiguredServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbeClientCtpConfiguredServiceType.setStatus("current")
_GbeClientCtpTribTestSigGenMode_Type = InfnEnableDisable
_GbeClientCtpTribTestSigGenMode_Object = MibTableColumn
gbeClientCtpTribTestSigGenMode = _GbeClientCtpTribTestSigGenMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 5),
    _GbeClientCtpTribTestSigGenMode_Type()
)
gbeClientCtpTribTestSigGenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTribTestSigGenMode.setStatus("current")
_GbeClientCtpTribTestSigMonMode_Type = InfnEnableDisable
_GbeClientCtpTribTestSigMonMode_Object = MibTableColumn
gbeClientCtpTribTestSigMonMode = _GbeClientCtpTribTestSigMonMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 6),
    _GbeClientCtpTribTestSigMonMode_Type()
)
gbeClientCtpTribTestSigMonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTribTestSigMonMode.setStatus("current")
_GbeClientCtpLineTestSigGenMode_Type = InfnEnableDisable
_GbeClientCtpLineTestSigGenMode_Object = MibTableColumn
gbeClientCtpLineTestSigGenMode = _GbeClientCtpLineTestSigGenMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 7),
    _GbeClientCtpLineTestSigGenMode_Type()
)
gbeClientCtpLineTestSigGenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpLineTestSigGenMode.setStatus("current")
_GbeClientCtpLineTestSigMonMode_Type = InfnEnableDisable
_GbeClientCtpLineTestSigMonMode_Object = MibTableColumn
gbeClientCtpLineTestSigMonMode = _GbeClientCtpLineTestSigMonMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 8),
    _GbeClientCtpLineTestSigMonMode_Type()
)
gbeClientCtpLineTestSigMonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpLineTestSigMonMode.setStatus("current")
_GbeClientCtpMaxPacketLen_Type = InfnGigeMaxPacketLen
_GbeClientCtpMaxPacketLen_Object = MibTableColumn
gbeClientCtpMaxPacketLen = _GbeClientCtpMaxPacketLen_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 9),
    _GbeClientCtpMaxPacketLen_Type()
)
gbeClientCtpMaxPacketLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpMaxPacketLen.setStatus("current")
_GbeClientCtpRxPcsICG15MinTce_Type = Integer32
_GbeClientCtpRxPcsICG15MinTce_Object = MibTableColumn
gbeClientCtpRxPcsICG15MinTce = _GbeClientCtpRxPcsICG15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 10),
    _GbeClientCtpRxPcsICG15MinTce_Type()
)
gbeClientCtpRxPcsICG15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxPcsICG15MinTce.setStatus("current")
_GbeClientCtpRxPcsES15MinTce_Type = Integer32
_GbeClientCtpRxPcsES15MinTce_Object = MibTableColumn
gbeClientCtpRxPcsES15MinTce = _GbeClientCtpRxPcsES15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 11),
    _GbeClientCtpRxPcsES15MinTce_Type()
)
gbeClientCtpRxPcsES15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxPcsES15MinTce.setStatus("current")
_GbeClientCtpRxPcsSES15MinTce_Type = Integer32
_GbeClientCtpRxPcsSES15MinTce_Object = MibTableColumn
gbeClientCtpRxPcsSES15MinTce = _GbeClientCtpRxPcsSES15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 12),
    _GbeClientCtpRxPcsSES15MinTce_Type()
)
gbeClientCtpRxPcsSES15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxPcsSES15MinTce.setStatus("current")
_GbeClientCtpRxPcsSESS15MinTce_Type = Integer32
_GbeClientCtpRxPcsSESS15MinTce_Object = MibTableColumn
gbeClientCtpRxPcsSESS15MinTce = _GbeClientCtpRxPcsSESS15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 13),
    _GbeClientCtpRxPcsSESS15MinTce_Type()
)
gbeClientCtpRxPcsSESS15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxPcsSESS15MinTce.setStatus("current")
_GbeClientCtpRxPcsICGDayTce_Type = Integer32
_GbeClientCtpRxPcsICGDayTce_Object = MibTableColumn
gbeClientCtpRxPcsICGDayTce = _GbeClientCtpRxPcsICGDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 14),
    _GbeClientCtpRxPcsICGDayTce_Type()
)
gbeClientCtpRxPcsICGDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxPcsICGDayTce.setStatus("current")
_GbeClientCtpRxPcsESDayTce_Type = Integer32
_GbeClientCtpRxPcsESDayTce_Object = MibTableColumn
gbeClientCtpRxPcsESDayTce = _GbeClientCtpRxPcsESDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 15),
    _GbeClientCtpRxPcsESDayTce_Type()
)
gbeClientCtpRxPcsESDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxPcsESDayTce.setStatus("current")
_GbeClientCtpRxPcsSESDayTce_Type = Integer32
_GbeClientCtpRxPcsSESDayTce_Object = MibTableColumn
gbeClientCtpRxPcsSESDayTce = _GbeClientCtpRxPcsSESDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 16),
    _GbeClientCtpRxPcsSESDayTce_Type()
)
gbeClientCtpRxPcsSESDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxPcsSESDayTce.setStatus("current")
_GbeClientCtpRxPcsSESSDayTce_Type = Integer32
_GbeClientCtpRxPcsSESSDayTce_Object = MibTableColumn
gbeClientCtpRxPcsSESSDayTce = _GbeClientCtpRxPcsSESSDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 17),
    _GbeClientCtpRxPcsSESSDayTce_Type()
)
gbeClientCtpRxPcsSESSDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxPcsSESSDayTce.setStatus("current")
_GbeClientCtpRxMacJS15MinTce_Type = Integer32
_GbeClientCtpRxMacJS15MinTce_Object = MibTableColumn
gbeClientCtpRxMacJS15MinTce = _GbeClientCtpRxMacJS15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 18),
    _GbeClientCtpRxMacJS15MinTce_Type()
)
gbeClientCtpRxMacJS15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacJS15MinTce.setStatus("current")
_GbeClientCtpRxMacSES15MinTce_Type = Integer32
_GbeClientCtpRxMacSES15MinTce_Object = MibTableColumn
gbeClientCtpRxMacSES15MinTce = _GbeClientCtpRxMacSES15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 19),
    _GbeClientCtpRxMacSES15MinTce_Type()
)
gbeClientCtpRxMacSES15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacSES15MinTce.setStatus("current")
_GbeClientCtpRxMacErrOctet15MinTce_Type = Integer32
_GbeClientCtpRxMacErrOctet15MinTce_Object = MibTableColumn
gbeClientCtpRxMacErrOctet15MinTce = _GbeClientCtpRxMacErrOctet15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 20),
    _GbeClientCtpRxMacErrOctet15MinTce_Type()
)
gbeClientCtpRxMacErrOctet15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacErrOctet15MinTce.setStatus("current")
_GbeClientCtpRxMacJabber15MinTce_Type = Integer32
_GbeClientCtpRxMacJabber15MinTce_Object = MibTableColumn
gbeClientCtpRxMacJabber15MinTce = _GbeClientCtpRxMacJabber15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 21),
    _GbeClientCtpRxMacJabber15MinTce_Type()
)
gbeClientCtpRxMacJabber15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacJabber15MinTce.setStatus("current")
_GbeClientCtpRxMacFragment15MinTce_Type = Integer32
_GbeClientCtpRxMacFragment15MinTce_Object = MibTableColumn
gbeClientCtpRxMacFragment15MinTce = _GbeClientCtpRxMacFragment15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 22),
    _GbeClientCtpRxMacFragment15MinTce_Type()
)
gbeClientCtpRxMacFragment15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacFragment15MinTce.setStatus("current")
_GbeClientCtpRxMacCrcAligned15MinTce_Type = Integer32
_GbeClientCtpRxMacCrcAligned15MinTce_Object = MibTableColumn
gbeClientCtpRxMacCrcAligned15MinTce = _GbeClientCtpRxMacCrcAligned15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 23),
    _GbeClientCtpRxMacCrcAligned15MinTce_Type()
)
gbeClientCtpRxMacCrcAligned15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacCrcAligned15MinTce.setStatus("current")
_GbeClientCtpRxMacUndersized15MinTce_Type = Integer32
_GbeClientCtpRxMacUndersized15MinTce_Object = MibTableColumn
gbeClientCtpRxMacUndersized15MinTce = _GbeClientCtpRxMacUndersized15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 24),
    _GbeClientCtpRxMacUndersized15MinTce_Type()
)
gbeClientCtpRxMacUndersized15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacUndersized15MinTce.setStatus("current")
_GbeClientCtpRxMacOversize15MinTce_Type = Integer32
_GbeClientCtpRxMacOversize15MinTce_Object = MibTableColumn
gbeClientCtpRxMacOversize15MinTce = _GbeClientCtpRxMacOversize15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 25),
    _GbeClientCtpRxMacOversize15MinTce_Type()
)
gbeClientCtpRxMacOversize15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacOversize15MinTce.setStatus("current")
_GbeClientCtpRxSize64P15MinTce_Type = Integer32
_GbeClientCtpRxSize64P15MinTce_Object = MibTableColumn
gbeClientCtpRxSize64P15MinTce = _GbeClientCtpRxSize64P15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 26),
    _GbeClientCtpRxSize64P15MinTce_Type()
)
gbeClientCtpRxSize64P15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize64P15MinTce.setStatus("current")
_GbeClientCtpRxSize65to127P15MinTce_Type = Integer32
_GbeClientCtpRxSize65to127P15MinTce_Object = MibTableColumn
gbeClientCtpRxSize65to127P15MinTce = _GbeClientCtpRxSize65to127P15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 27),
    _GbeClientCtpRxSize65to127P15MinTce_Type()
)
gbeClientCtpRxSize65to127P15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize65to127P15MinTce.setStatus("current")
_GbeClientCtpRxSize128to255P15MinTce_Type = Integer32
_GbeClientCtpRxSize128to255P15MinTce_Object = MibTableColumn
gbeClientCtpRxSize128to255P15MinTce = _GbeClientCtpRxSize128to255P15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 28),
    _GbeClientCtpRxSize128to255P15MinTce_Type()
)
gbeClientCtpRxSize128to255P15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize128to255P15MinTce.setStatus("current")
_GbeClientCtpRxSize256to511P15MinTce_Type = Integer32
_GbeClientCtpRxSize256to511P15MinTce_Object = MibTableColumn
gbeClientCtpRxSize256to511P15MinTce = _GbeClientCtpRxSize256to511P15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 29),
    _GbeClientCtpRxSize256to511P15MinTce_Type()
)
gbeClientCtpRxSize256to511P15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize256to511P15MinTce.setStatus("current")
_GbeClientCtpRxSize512to1023P15MinTce_Type = Integer32
_GbeClientCtpRxSize512to1023P15MinTce_Object = MibTableColumn
gbeClientCtpRxSize512to1023P15MinTce = _GbeClientCtpRxSize512to1023P15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 30),
    _GbeClientCtpRxSize512to1023P15MinTce_Type()
)
gbeClientCtpRxSize512to1023P15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize512to1023P15MinTce.setStatus("current")
_GbeClientCtpRxSize1024to1518P15MinTce_Type = Integer32
_GbeClientCtpRxSize1024to1518P15MinTce_Object = MibTableColumn
gbeClientCtpRxSize1024to1518P15MinTce = _GbeClientCtpRxSize1024to1518P15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 31),
    _GbeClientCtpRxSize1024to1518P15MinTce_Type()
)
gbeClientCtpRxSize1024to1518P15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize1024to1518P15MinTce.setStatus("current")
_GbeClientCtpRxSize1519toJumboP15MinTce_Type = Integer32
_GbeClientCtpRxSize1519toJumboP15MinTce_Object = MibTableColumn
gbeClientCtpRxSize1519toJumboP15MinTce = _GbeClientCtpRxSize1519toJumboP15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 32),
    _GbeClientCtpRxSize1519toJumboP15MinTce_Type()
)
gbeClientCtpRxSize1519toJumboP15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize1519toJumboP15MinTce.setStatus("current")
_GbeClientCtpRxPackets15MinTce_Type = Integer32
_GbeClientCtpRxPackets15MinTce_Object = MibTableColumn
gbeClientCtpRxPackets15MinTce = _GbeClientCtpRxPackets15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 33),
    _GbeClientCtpRxPackets15MinTce_Type()
)
gbeClientCtpRxPackets15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxPackets15MinTce.setStatus("current")
_GbeClientCtpRxOctets15MinTce_Type = Integer32
_GbeClientCtpRxOctets15MinTce_Object = MibTableColumn
gbeClientCtpRxOctets15MinTce = _GbeClientCtpRxOctets15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 34),
    _GbeClientCtpRxOctets15MinTce_Type()
)
gbeClientCtpRxOctets15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxOctets15MinTce.setStatus("current")
_GbeClientCtpRxBroadcastPkts15MinTce_Type = Integer32
_GbeClientCtpRxBroadcastPkts15MinTce_Object = MibTableColumn
gbeClientCtpRxBroadcastPkts15MinTce = _GbeClientCtpRxBroadcastPkts15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 35),
    _GbeClientCtpRxBroadcastPkts15MinTce_Type()
)
gbeClientCtpRxBroadcastPkts15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxBroadcastPkts15MinTce.setStatus("current")
_GbeClientCtpRxMulticastPkts15MinTce_Type = Integer32
_GbeClientCtpRxMulticastPkts15MinTce_Object = MibTableColumn
gbeClientCtpRxMulticastPkts15MinTce = _GbeClientCtpRxMulticastPkts15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 36),
    _GbeClientCtpRxMulticastPkts15MinTce_Type()
)
gbeClientCtpRxMulticastPkts15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMulticastPkts15MinTce.setStatus("current")
_GbeClientCtpRxInPauseFrames15MinTce_Type = Integer32
_GbeClientCtpRxInPauseFrames15MinTce_Object = MibTableColumn
gbeClientCtpRxInPauseFrames15MinTce = _GbeClientCtpRxInPauseFrames15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 37),
    _GbeClientCtpRxInPauseFrames15MinTce_Type()
)
gbeClientCtpRxInPauseFrames15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxInPauseFrames15MinTce.setStatus("current")
_GbeClientCtpRxMacJSDayTce_Type = Integer32
_GbeClientCtpRxMacJSDayTce_Object = MibTableColumn
gbeClientCtpRxMacJSDayTce = _GbeClientCtpRxMacJSDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 38),
    _GbeClientCtpRxMacJSDayTce_Type()
)
gbeClientCtpRxMacJSDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacJSDayTce.setStatus("current")
_GbeClientCtpRxMacSESDayTce_Type = Integer32
_GbeClientCtpRxMacSESDayTce_Object = MibTableColumn
gbeClientCtpRxMacSESDayTce = _GbeClientCtpRxMacSESDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 39),
    _GbeClientCtpRxMacSESDayTce_Type()
)
gbeClientCtpRxMacSESDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacSESDayTce.setStatus("current")
_GbeClientCtpRxMacErrOctetDayTce_Type = Integer32
_GbeClientCtpRxMacErrOctetDayTce_Object = MibTableColumn
gbeClientCtpRxMacErrOctetDayTce = _GbeClientCtpRxMacErrOctetDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 40),
    _GbeClientCtpRxMacErrOctetDayTce_Type()
)
gbeClientCtpRxMacErrOctetDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacErrOctetDayTce.setStatus("current")
_GbeClientCtpRxMacJabberDayTce_Type = Integer32
_GbeClientCtpRxMacJabberDayTce_Object = MibTableColumn
gbeClientCtpRxMacJabberDayTce = _GbeClientCtpRxMacJabberDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 41),
    _GbeClientCtpRxMacJabberDayTce_Type()
)
gbeClientCtpRxMacJabberDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacJabberDayTce.setStatus("current")
_GbeClientCtpRxMacFragmentDayTce_Type = Integer32
_GbeClientCtpRxMacFragmentDayTce_Object = MibTableColumn
gbeClientCtpRxMacFragmentDayTce = _GbeClientCtpRxMacFragmentDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 42),
    _GbeClientCtpRxMacFragmentDayTce_Type()
)
gbeClientCtpRxMacFragmentDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacFragmentDayTce.setStatus("current")
_GbeClientCtpRxMacCrcAlignedDayTce_Type = Integer32
_GbeClientCtpRxMacCrcAlignedDayTce_Object = MibTableColumn
gbeClientCtpRxMacCrcAlignedDayTce = _GbeClientCtpRxMacCrcAlignedDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 43),
    _GbeClientCtpRxMacCrcAlignedDayTce_Type()
)
gbeClientCtpRxMacCrcAlignedDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacCrcAlignedDayTce.setStatus("current")
_GbeClientCtpRxMacUndersizedDayTce_Type = Integer32
_GbeClientCtpRxMacUndersizedDayTce_Object = MibTableColumn
gbeClientCtpRxMacUndersizedDayTce = _GbeClientCtpRxMacUndersizedDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 44),
    _GbeClientCtpRxMacUndersizedDayTce_Type()
)
gbeClientCtpRxMacUndersizedDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacUndersizedDayTce.setStatus("current")
_GbeClientCtpRxMacOversizeDayTce_Type = Integer32
_GbeClientCtpRxMacOversizeDayTce_Object = MibTableColumn
gbeClientCtpRxMacOversizeDayTce = _GbeClientCtpRxMacOversizeDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 45),
    _GbeClientCtpRxMacOversizeDayTce_Type()
)
gbeClientCtpRxMacOversizeDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacOversizeDayTce.setStatus("current")
_GbeClientCtpRxSize64DayTce_Type = Integer32
_GbeClientCtpRxSize64DayTce_Object = MibTableColumn
gbeClientCtpRxSize64DayTce = _GbeClientCtpRxSize64DayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 46),
    _GbeClientCtpRxSize64DayTce_Type()
)
gbeClientCtpRxSize64DayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize64DayTce.setStatus("current")
_GbeClientCtpRxSize65to127DayTce_Type = Integer32
_GbeClientCtpRxSize65to127DayTce_Object = MibTableColumn
gbeClientCtpRxSize65to127DayTce = _GbeClientCtpRxSize65to127DayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 47),
    _GbeClientCtpRxSize65to127DayTce_Type()
)
gbeClientCtpRxSize65to127DayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize65to127DayTce.setStatus("current")
_GbeClientCtpRxSize128to255DayTce_Type = Integer32
_GbeClientCtpRxSize128to255DayTce_Object = MibTableColumn
gbeClientCtpRxSize128to255DayTce = _GbeClientCtpRxSize128to255DayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 48),
    _GbeClientCtpRxSize128to255DayTce_Type()
)
gbeClientCtpRxSize128to255DayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize128to255DayTce.setStatus("current")
_GbeClientCtpRxSize256to511DayTce_Type = Integer32
_GbeClientCtpRxSize256to511DayTce_Object = MibTableColumn
gbeClientCtpRxSize256to511DayTce = _GbeClientCtpRxSize256to511DayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 49),
    _GbeClientCtpRxSize256to511DayTce_Type()
)
gbeClientCtpRxSize256to511DayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize256to511DayTce.setStatus("current")
_GbeClientCtpRxSize512to1023DayTce_Type = Integer32
_GbeClientCtpRxSize512to1023DayTce_Object = MibTableColumn
gbeClientCtpRxSize512to1023DayTce = _GbeClientCtpRxSize512to1023DayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 50),
    _GbeClientCtpRxSize512to1023DayTce_Type()
)
gbeClientCtpRxSize512to1023DayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize512to1023DayTce.setStatus("current")
_GbeClientCtpRxSize1024to1518DayTce_Type = Integer32
_GbeClientCtpRxSize1024to1518DayTce_Object = MibTableColumn
gbeClientCtpRxSize1024to1518DayTce = _GbeClientCtpRxSize1024to1518DayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 51),
    _GbeClientCtpRxSize1024to1518DayTce_Type()
)
gbeClientCtpRxSize1024to1518DayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize1024to1518DayTce.setStatus("current")
_GbeClientCtpRxSize1519toJumboDayTce_Type = Integer32
_GbeClientCtpRxSize1519toJumboDayTce_Object = MibTableColumn
gbeClientCtpRxSize1519toJumboDayTce = _GbeClientCtpRxSize1519toJumboDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 52),
    _GbeClientCtpRxSize1519toJumboDayTce_Type()
)
gbeClientCtpRxSize1519toJumboDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize1519toJumboDayTce.setStatus("current")
_GbeClientCtpRxPacketsDayTce_Type = Integer32
_GbeClientCtpRxPacketsDayTce_Object = MibTableColumn
gbeClientCtpRxPacketsDayTce = _GbeClientCtpRxPacketsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 53),
    _GbeClientCtpRxPacketsDayTce_Type()
)
gbeClientCtpRxPacketsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxPacketsDayTce.setStatus("current")
_GbeClientCtpRxOctetsDayTce_Type = Integer32
_GbeClientCtpRxOctetsDayTce_Object = MibTableColumn
gbeClientCtpRxOctetsDayTce = _GbeClientCtpRxOctetsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 54),
    _GbeClientCtpRxOctetsDayTce_Type()
)
gbeClientCtpRxOctetsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxOctetsDayTce.setStatus("current")
_GbeClientCtpRxBroadcastPktsDayTce_Type = Integer32
_GbeClientCtpRxBroadcastPktsDayTce_Object = MibTableColumn
gbeClientCtpRxBroadcastPktsDayTce = _GbeClientCtpRxBroadcastPktsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 55),
    _GbeClientCtpRxBroadcastPktsDayTce_Type()
)
gbeClientCtpRxBroadcastPktsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxBroadcastPktsDayTce.setStatus("current")
_GbeClientCtpRxMulticastPktsDayTce_Type = Integer32
_GbeClientCtpRxMulticastPktsDayTce_Object = MibTableColumn
gbeClientCtpRxMulticastPktsDayTce = _GbeClientCtpRxMulticastPktsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 56),
    _GbeClientCtpRxMulticastPktsDayTce_Type()
)
gbeClientCtpRxMulticastPktsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMulticastPktsDayTce.setStatus("current")
_GbeClientCtpRxInPauseFramesDayTce_Type = Integer32
_GbeClientCtpRxInPauseFramesDayTce_Object = MibTableColumn
gbeClientCtpRxInPauseFramesDayTce = _GbeClientCtpRxInPauseFramesDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 57),
    _GbeClientCtpRxInPauseFramesDayTce_Type()
)
gbeClientCtpRxInPauseFramesDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxInPauseFramesDayTce.setStatus("current")
_GbeClientCtpTxPcsICG15MinTce_Type = Integer32
_GbeClientCtpTxPcsICG15MinTce_Object = MibTableColumn
gbeClientCtpTxPcsICG15MinTce = _GbeClientCtpTxPcsICG15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 58),
    _GbeClientCtpTxPcsICG15MinTce_Type()
)
gbeClientCtpTxPcsICG15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxPcsICG15MinTce.setStatus("current")
_GbeClientCtpTxPcsES15MinTce_Type = Integer32
_GbeClientCtpTxPcsES15MinTce_Object = MibTableColumn
gbeClientCtpTxPcsES15MinTce = _GbeClientCtpTxPcsES15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 59),
    _GbeClientCtpTxPcsES15MinTce_Type()
)
gbeClientCtpTxPcsES15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxPcsES15MinTce.setStatus("current")
_GbeClientCtpTxPcsSES15MinTce_Type = Integer32
_GbeClientCtpTxPcsSES15MinTce_Object = MibTableColumn
gbeClientCtpTxPcsSES15MinTce = _GbeClientCtpTxPcsSES15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 60),
    _GbeClientCtpTxPcsSES15MinTce_Type()
)
gbeClientCtpTxPcsSES15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxPcsSES15MinTce.setStatus("current")
_GbeClientCtpTxPcsSESS15MinTce_Type = Integer32
_GbeClientCtpTxPcsSESS15MinTce_Object = MibTableColumn
gbeClientCtpTxPcsSESS15MinTce = _GbeClientCtpTxPcsSESS15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 61),
    _GbeClientCtpTxPcsSESS15MinTce_Type()
)
gbeClientCtpTxPcsSESS15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxPcsSESS15MinTce.setStatus("current")
_GbeClientCtpTxPcsICGDayTce_Type = Integer32
_GbeClientCtpTxPcsICGDayTce_Object = MibTableColumn
gbeClientCtpTxPcsICGDayTce = _GbeClientCtpTxPcsICGDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 62),
    _GbeClientCtpTxPcsICGDayTce_Type()
)
gbeClientCtpTxPcsICGDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxPcsICGDayTce.setStatus("current")
_GbeClientCtpTxPcsESDayTce_Type = Integer32
_GbeClientCtpTxPcsESDayTce_Object = MibTableColumn
gbeClientCtpTxPcsESDayTce = _GbeClientCtpTxPcsESDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 63),
    _GbeClientCtpTxPcsESDayTce_Type()
)
gbeClientCtpTxPcsESDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxPcsESDayTce.setStatus("current")
_GbeClientCtpTxPcsSESDayTce_Type = Integer32
_GbeClientCtpTxPcsSESDayTce_Object = MibTableColumn
gbeClientCtpTxPcsSESDayTce = _GbeClientCtpTxPcsSESDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 64),
    _GbeClientCtpTxPcsSESDayTce_Type()
)
gbeClientCtpTxPcsSESDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxPcsSESDayTce.setStatus("current")
_GbeClientCtpTxPcsSESSDayTce_Type = Integer32
_GbeClientCtpTxPcsSESSDayTce_Object = MibTableColumn
gbeClientCtpTxPcsSESSDayTce = _GbeClientCtpTxPcsSESSDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 65),
    _GbeClientCtpTxPcsSESSDayTce_Type()
)
gbeClientCtpTxPcsSESSDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxPcsSESSDayTce.setStatus("current")
_GbeClientCtpTxMacJS15MinTce_Type = Integer32
_GbeClientCtpTxMacJS15MinTce_Object = MibTableColumn
gbeClientCtpTxMacJS15MinTce = _GbeClientCtpTxMacJS15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 66),
    _GbeClientCtpTxMacJS15MinTce_Type()
)
gbeClientCtpTxMacJS15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacJS15MinTce.setStatus("current")
_GbeClientCtpTxMacSES15MinTce_Type = Integer32
_GbeClientCtpTxMacSES15MinTce_Object = MibTableColumn
gbeClientCtpTxMacSES15MinTce = _GbeClientCtpTxMacSES15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 67),
    _GbeClientCtpTxMacSES15MinTce_Type()
)
gbeClientCtpTxMacSES15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacSES15MinTce.setStatus("current")
_GbeClientCtpTxMacErrOctet15MinTce_Type = Integer32
_GbeClientCtpTxMacErrOctet15MinTce_Object = MibTableColumn
gbeClientCtpTxMacErrOctet15MinTce = _GbeClientCtpTxMacErrOctet15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 68),
    _GbeClientCtpTxMacErrOctet15MinTce_Type()
)
gbeClientCtpTxMacErrOctet15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacErrOctet15MinTce.setStatus("current")
_GbeClientCtpTxMacJabber15MinTce_Type = Integer32
_GbeClientCtpTxMacJabber15MinTce_Object = MibTableColumn
gbeClientCtpTxMacJabber15MinTce = _GbeClientCtpTxMacJabber15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 69),
    _GbeClientCtpTxMacJabber15MinTce_Type()
)
gbeClientCtpTxMacJabber15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacJabber15MinTce.setStatus("current")
_GbeClientCtpTxMacFragment15MinTce_Type = Integer32
_GbeClientCtpTxMacFragment15MinTce_Object = MibTableColumn
gbeClientCtpTxMacFragment15MinTce = _GbeClientCtpTxMacFragment15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 70),
    _GbeClientCtpTxMacFragment15MinTce_Type()
)
gbeClientCtpTxMacFragment15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacFragment15MinTce.setStatus("current")
_GbeClientCtpTxMacCrcAligned15MinTce_Type = Integer32
_GbeClientCtpTxMacCrcAligned15MinTce_Object = MibTableColumn
gbeClientCtpTxMacCrcAligned15MinTce = _GbeClientCtpTxMacCrcAligned15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 71),
    _GbeClientCtpTxMacCrcAligned15MinTce_Type()
)
gbeClientCtpTxMacCrcAligned15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacCrcAligned15MinTce.setStatus("current")
_GbeClientCtpTxMacUndersized15MinTce_Type = Integer32
_GbeClientCtpTxMacUndersized15MinTce_Object = MibTableColumn
gbeClientCtpTxMacUndersized15MinTce = _GbeClientCtpTxMacUndersized15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 72),
    _GbeClientCtpTxMacUndersized15MinTce_Type()
)
gbeClientCtpTxMacUndersized15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacUndersized15MinTce.setStatus("current")
_GbeClientCtpTxMacOversize15MinTce_Type = Integer32
_GbeClientCtpTxMacOversize15MinTce_Object = MibTableColumn
gbeClientCtpTxMacOversize15MinTce = _GbeClientCtpTxMacOversize15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 73),
    _GbeClientCtpTxMacOversize15MinTce_Type()
)
gbeClientCtpTxMacOversize15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacOversize15MinTce.setStatus("current")
_GbeClientCtpTxSize64P15MinTce_Type = Integer32
_GbeClientCtpTxSize64P15MinTce_Object = MibTableColumn
gbeClientCtpTxSize64P15MinTce = _GbeClientCtpTxSize64P15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 74),
    _GbeClientCtpTxSize64P15MinTce_Type()
)
gbeClientCtpTxSize64P15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize64P15MinTce.setStatus("current")
_GbeClientCtpTxSize65to127P15MinTce_Type = Integer32
_GbeClientCtpTxSize65to127P15MinTce_Object = MibTableColumn
gbeClientCtpTxSize65to127P15MinTce = _GbeClientCtpTxSize65to127P15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 75),
    _GbeClientCtpTxSize65to127P15MinTce_Type()
)
gbeClientCtpTxSize65to127P15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize65to127P15MinTce.setStatus("current")
_GbeClientCtpTxSize128to255P15MinTce_Type = Integer32
_GbeClientCtpTxSize128to255P15MinTce_Object = MibTableColumn
gbeClientCtpTxSize128to255P15MinTce = _GbeClientCtpTxSize128to255P15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 76),
    _GbeClientCtpTxSize128to255P15MinTce_Type()
)
gbeClientCtpTxSize128to255P15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize128to255P15MinTce.setStatus("current")
_GbeClientCtpTxSize256to511P15MinTce_Type = Integer32
_GbeClientCtpTxSize256to511P15MinTce_Object = MibTableColumn
gbeClientCtpTxSize256to511P15MinTce = _GbeClientCtpTxSize256to511P15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 77),
    _GbeClientCtpTxSize256to511P15MinTce_Type()
)
gbeClientCtpTxSize256to511P15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize256to511P15MinTce.setStatus("current")
_GbeClientCtpTxSize512to1023P15MinTce_Type = Integer32
_GbeClientCtpTxSize512to1023P15MinTce_Object = MibTableColumn
gbeClientCtpTxSize512to1023P15MinTce = _GbeClientCtpTxSize512to1023P15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 78),
    _GbeClientCtpTxSize512to1023P15MinTce_Type()
)
gbeClientCtpTxSize512to1023P15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize512to1023P15MinTce.setStatus("current")
_GbeClientCtpTxSize1024to1518P15MinTce_Type = Integer32
_GbeClientCtpTxSize1024to1518P15MinTce_Object = MibTableColumn
gbeClientCtpTxSize1024to1518P15MinTce = _GbeClientCtpTxSize1024to1518P15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 79),
    _GbeClientCtpTxSize1024to1518P15MinTce_Type()
)
gbeClientCtpTxSize1024to1518P15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize1024to1518P15MinTce.setStatus("current")
_GbeClientCtpTxSize1519toJumboP15MinTce_Type = Integer32
_GbeClientCtpTxSize1519toJumboP15MinTce_Object = MibTableColumn
gbeClientCtpTxSize1519toJumboP15MinTce = _GbeClientCtpTxSize1519toJumboP15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 80),
    _GbeClientCtpTxSize1519toJumboP15MinTce_Type()
)
gbeClientCtpTxSize1519toJumboP15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize1519toJumboP15MinTce.setStatus("current")
_GbeClientCtpTxPackets15MinTce_Type = Integer32
_GbeClientCtpTxPackets15MinTce_Object = MibTableColumn
gbeClientCtpTxPackets15MinTce = _GbeClientCtpTxPackets15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 81),
    _GbeClientCtpTxPackets15MinTce_Type()
)
gbeClientCtpTxPackets15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxPackets15MinTce.setStatus("current")
_GbeClientCtpTxOctets15MinTce_Type = Integer32
_GbeClientCtpTxOctets15MinTce_Object = MibTableColumn
gbeClientCtpTxOctets15MinTce = _GbeClientCtpTxOctets15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 82),
    _GbeClientCtpTxOctets15MinTce_Type()
)
gbeClientCtpTxOctets15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxOctets15MinTce.setStatus("current")
_GbeClientCtpTxBroadcastPkts15MinTce_Type = Integer32
_GbeClientCtpTxBroadcastPkts15MinTce_Object = MibTableColumn
gbeClientCtpTxBroadcastPkts15MinTce = _GbeClientCtpTxBroadcastPkts15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 83),
    _GbeClientCtpTxBroadcastPkts15MinTce_Type()
)
gbeClientCtpTxBroadcastPkts15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxBroadcastPkts15MinTce.setStatus("current")
_GbeClientCtpTxMulticastPkts15MinTce_Type = Integer32
_GbeClientCtpTxMulticastPkts15MinTce_Object = MibTableColumn
gbeClientCtpTxMulticastPkts15MinTce = _GbeClientCtpTxMulticastPkts15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 84),
    _GbeClientCtpTxMulticastPkts15MinTce_Type()
)
gbeClientCtpTxMulticastPkts15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMulticastPkts15MinTce.setStatus("current")
_GbeClientCtpTxOutPauseFrames15MinTce_Type = Integer32
_GbeClientCtpTxOutPauseFrames15MinTce_Object = MibTableColumn
gbeClientCtpTxOutPauseFrames15MinTce = _GbeClientCtpTxOutPauseFrames15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 85),
    _GbeClientCtpTxOutPauseFrames15MinTce_Type()
)
gbeClientCtpTxOutPauseFrames15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxOutPauseFrames15MinTce.setStatus("current")
_GbeClientCtpTxMacJSDayTce_Type = Integer32
_GbeClientCtpTxMacJSDayTce_Object = MibTableColumn
gbeClientCtpTxMacJSDayTce = _GbeClientCtpTxMacJSDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 86),
    _GbeClientCtpTxMacJSDayTce_Type()
)
gbeClientCtpTxMacJSDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacJSDayTce.setStatus("current")
_GbeClientCtpTxMacSESDayTce_Type = Integer32
_GbeClientCtpTxMacSESDayTce_Object = MibTableColumn
gbeClientCtpTxMacSESDayTce = _GbeClientCtpTxMacSESDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 87),
    _GbeClientCtpTxMacSESDayTce_Type()
)
gbeClientCtpTxMacSESDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacSESDayTce.setStatus("current")
_GbeClientCtpTxMacErrOctetDayTce_Type = Integer32
_GbeClientCtpTxMacErrOctetDayTce_Object = MibTableColumn
gbeClientCtpTxMacErrOctetDayTce = _GbeClientCtpTxMacErrOctetDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 88),
    _GbeClientCtpTxMacErrOctetDayTce_Type()
)
gbeClientCtpTxMacErrOctetDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacErrOctetDayTce.setStatus("current")
_GbeClientCtpTxMacJabberDayTce_Type = Integer32
_GbeClientCtpTxMacJabberDayTce_Object = MibTableColumn
gbeClientCtpTxMacJabberDayTce = _GbeClientCtpTxMacJabberDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 89),
    _GbeClientCtpTxMacJabberDayTce_Type()
)
gbeClientCtpTxMacJabberDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacJabberDayTce.setStatus("current")
_GbeClientCtpTxMacFragmentDayTce_Type = Integer32
_GbeClientCtpTxMacFragmentDayTce_Object = MibTableColumn
gbeClientCtpTxMacFragmentDayTce = _GbeClientCtpTxMacFragmentDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 90),
    _GbeClientCtpTxMacFragmentDayTce_Type()
)
gbeClientCtpTxMacFragmentDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacFragmentDayTce.setStatus("current")
_GbeClientCtpTxMacCrcAlignedDayTce_Type = Integer32
_GbeClientCtpTxMacCrcAlignedDayTce_Object = MibTableColumn
gbeClientCtpTxMacCrcAlignedDayTce = _GbeClientCtpTxMacCrcAlignedDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 91),
    _GbeClientCtpTxMacCrcAlignedDayTce_Type()
)
gbeClientCtpTxMacCrcAlignedDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacCrcAlignedDayTce.setStatus("current")
_GbeClientCtpTxMacUndersizedDayTce_Type = Integer32
_GbeClientCtpTxMacUndersizedDayTce_Object = MibTableColumn
gbeClientCtpTxMacUndersizedDayTce = _GbeClientCtpTxMacUndersizedDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 92),
    _GbeClientCtpTxMacUndersizedDayTce_Type()
)
gbeClientCtpTxMacUndersizedDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacUndersizedDayTce.setStatus("current")
_GbeClientCtpTxMacOversizeDayTce_Type = Integer32
_GbeClientCtpTxMacOversizeDayTce_Object = MibTableColumn
gbeClientCtpTxMacOversizeDayTce = _GbeClientCtpTxMacOversizeDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 93),
    _GbeClientCtpTxMacOversizeDayTce_Type()
)
gbeClientCtpTxMacOversizeDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacOversizeDayTce.setStatus("current")
_GbeClientCtpTxSize64DayTce_Type = Integer32
_GbeClientCtpTxSize64DayTce_Object = MibTableColumn
gbeClientCtpTxSize64DayTce = _GbeClientCtpTxSize64DayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 94),
    _GbeClientCtpTxSize64DayTce_Type()
)
gbeClientCtpTxSize64DayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize64DayTce.setStatus("current")
_GbeClientCtpTxSize65to127DayTce_Type = Integer32
_GbeClientCtpTxSize65to127DayTce_Object = MibTableColumn
gbeClientCtpTxSize65to127DayTce = _GbeClientCtpTxSize65to127DayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 95),
    _GbeClientCtpTxSize65to127DayTce_Type()
)
gbeClientCtpTxSize65to127DayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize65to127DayTce.setStatus("current")
_GbeClientCtpTxSize128to255DayTce_Type = Integer32
_GbeClientCtpTxSize128to255DayTce_Object = MibTableColumn
gbeClientCtpTxSize128to255DayTce = _GbeClientCtpTxSize128to255DayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 96),
    _GbeClientCtpTxSize128to255DayTce_Type()
)
gbeClientCtpTxSize128to255DayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize128to255DayTce.setStatus("current")
_GbeClientCtpTxSize256to511DayTce_Type = Integer32
_GbeClientCtpTxSize256to511DayTce_Object = MibTableColumn
gbeClientCtpTxSize256to511DayTce = _GbeClientCtpTxSize256to511DayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 97),
    _GbeClientCtpTxSize256to511DayTce_Type()
)
gbeClientCtpTxSize256to511DayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize256to511DayTce.setStatus("current")
_GbeClientCtpTxSize512to1023DayTce_Type = Integer32
_GbeClientCtpTxSize512to1023DayTce_Object = MibTableColumn
gbeClientCtpTxSize512to1023DayTce = _GbeClientCtpTxSize512to1023DayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 98),
    _GbeClientCtpTxSize512to1023DayTce_Type()
)
gbeClientCtpTxSize512to1023DayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize512to1023DayTce.setStatus("current")
_GbeClientCtpTxSize1024to1518DayTce_Type = Integer32
_GbeClientCtpTxSize1024to1518DayTce_Object = MibTableColumn
gbeClientCtpTxSize1024to1518DayTce = _GbeClientCtpTxSize1024to1518DayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 99),
    _GbeClientCtpTxSize1024to1518DayTce_Type()
)
gbeClientCtpTxSize1024to1518DayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize1024to1518DayTce.setStatus("current")
_GbeClientCtpTxSize1519toJumboDayTce_Type = Integer32
_GbeClientCtpTxSize1519toJumboDayTce_Object = MibTableColumn
gbeClientCtpTxSize1519toJumboDayTce = _GbeClientCtpTxSize1519toJumboDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 100),
    _GbeClientCtpTxSize1519toJumboDayTce_Type()
)
gbeClientCtpTxSize1519toJumboDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize1519toJumboDayTce.setStatus("current")
_GbeClientCtpTxPacketsDayTce_Type = Integer32
_GbeClientCtpTxPacketsDayTce_Object = MibTableColumn
gbeClientCtpTxPacketsDayTce = _GbeClientCtpTxPacketsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 101),
    _GbeClientCtpTxPacketsDayTce_Type()
)
gbeClientCtpTxPacketsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxPacketsDayTce.setStatus("current")
_GbeClientCtpTxOctetsDayTce_Type = Integer32
_GbeClientCtpTxOctetsDayTce_Object = MibTableColumn
gbeClientCtpTxOctetsDayTce = _GbeClientCtpTxOctetsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 102),
    _GbeClientCtpTxOctetsDayTce_Type()
)
gbeClientCtpTxOctetsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxOctetsDayTce.setStatus("current")
_GbeClientCtpTxBroadcastPktsDayTce_Type = Integer32
_GbeClientCtpTxBroadcastPktsDayTce_Object = MibTableColumn
gbeClientCtpTxBroadcastPktsDayTce = _GbeClientCtpTxBroadcastPktsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 103),
    _GbeClientCtpTxBroadcastPktsDayTce_Type()
)
gbeClientCtpTxBroadcastPktsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxBroadcastPktsDayTce.setStatus("current")
_GbeClientCtpTxMulticastPktsDayTce_Type = Integer32
_GbeClientCtpTxMulticastPktsDayTce_Object = MibTableColumn
gbeClientCtpTxMulticastPktsDayTce = _GbeClientCtpTxMulticastPktsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 104),
    _GbeClientCtpTxMulticastPktsDayTce_Type()
)
gbeClientCtpTxMulticastPktsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMulticastPktsDayTce.setStatus("current")
_GbeClientCtpTxOutPauseFramesDayTce_Type = Integer32
_GbeClientCtpTxOutPauseFramesDayTce_Object = MibTableColumn
gbeClientCtpTxOutPauseFramesDayTce = _GbeClientCtpTxOutPauseFramesDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 105),
    _GbeClientCtpTxOutPauseFramesDayTce_Type()
)
gbeClientCtpTxOutPauseFramesDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxOutPauseFramesDayTce.setStatus("current")
_GbeClientCtpRxPcsICG15MinTceRept_Type = TruthValue
_GbeClientCtpRxPcsICG15MinTceRept_Object = MibTableColumn
gbeClientCtpRxPcsICG15MinTceRept = _GbeClientCtpRxPcsICG15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 106),
    _GbeClientCtpRxPcsICG15MinTceRept_Type()
)
gbeClientCtpRxPcsICG15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxPcsICG15MinTceRept.setStatus("current")
_GbeClientCtpRxPcsES15MinTceRept_Type = TruthValue
_GbeClientCtpRxPcsES15MinTceRept_Object = MibTableColumn
gbeClientCtpRxPcsES15MinTceRept = _GbeClientCtpRxPcsES15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 107),
    _GbeClientCtpRxPcsES15MinTceRept_Type()
)
gbeClientCtpRxPcsES15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxPcsES15MinTceRept.setStatus("current")
_GbeClientCtpRxPcsSES15MinTceRept_Type = TruthValue
_GbeClientCtpRxPcsSES15MinTceRept_Object = MibTableColumn
gbeClientCtpRxPcsSES15MinTceRept = _GbeClientCtpRxPcsSES15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 108),
    _GbeClientCtpRxPcsSES15MinTceRept_Type()
)
gbeClientCtpRxPcsSES15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxPcsSES15MinTceRept.setStatus("current")
_GbeClientCtpRxPcsSESS15MinTceRept_Type = TruthValue
_GbeClientCtpRxPcsSESS15MinTceRept_Object = MibTableColumn
gbeClientCtpRxPcsSESS15MinTceRept = _GbeClientCtpRxPcsSESS15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 109),
    _GbeClientCtpRxPcsSESS15MinTceRept_Type()
)
gbeClientCtpRxPcsSESS15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxPcsSESS15MinTceRept.setStatus("current")
_GbeClientCtpRxPcsICGDayTceRept_Type = TruthValue
_GbeClientCtpRxPcsICGDayTceRept_Object = MibTableColumn
gbeClientCtpRxPcsICGDayTceRept = _GbeClientCtpRxPcsICGDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 110),
    _GbeClientCtpRxPcsICGDayTceRept_Type()
)
gbeClientCtpRxPcsICGDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxPcsICGDayTceRept.setStatus("current")
_GbeClientCtpRxPcsESDayTceRept_Type = TruthValue
_GbeClientCtpRxPcsESDayTceRept_Object = MibTableColumn
gbeClientCtpRxPcsESDayTceRept = _GbeClientCtpRxPcsESDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 111),
    _GbeClientCtpRxPcsESDayTceRept_Type()
)
gbeClientCtpRxPcsESDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxPcsESDayTceRept.setStatus("current")
_GbeClientCtpRxPcsSESDayTceRept_Type = TruthValue
_GbeClientCtpRxPcsSESDayTceRept_Object = MibTableColumn
gbeClientCtpRxPcsSESDayTceRept = _GbeClientCtpRxPcsSESDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 112),
    _GbeClientCtpRxPcsSESDayTceRept_Type()
)
gbeClientCtpRxPcsSESDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxPcsSESDayTceRept.setStatus("current")
_GbeClientCtpRxPcsSESSDayTceRept_Type = TruthValue
_GbeClientCtpRxPcsSESSDayTceRept_Object = MibTableColumn
gbeClientCtpRxPcsSESSDayTceRept = _GbeClientCtpRxPcsSESSDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 113),
    _GbeClientCtpRxPcsSESSDayTceRept_Type()
)
gbeClientCtpRxPcsSESSDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxPcsSESSDayTceRept.setStatus("current")
_GbeClientCtpRxMacJS15MinTceRept_Type = TruthValue
_GbeClientCtpRxMacJS15MinTceRept_Object = MibTableColumn
gbeClientCtpRxMacJS15MinTceRept = _GbeClientCtpRxMacJS15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 114),
    _GbeClientCtpRxMacJS15MinTceRept_Type()
)
gbeClientCtpRxMacJS15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacJS15MinTceRept.setStatus("current")
_GbeClientCtpRxMacSES15MinTceRept_Type = TruthValue
_GbeClientCtpRxMacSES15MinTceRept_Object = MibTableColumn
gbeClientCtpRxMacSES15MinTceRept = _GbeClientCtpRxMacSES15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 115),
    _GbeClientCtpRxMacSES15MinTceRept_Type()
)
gbeClientCtpRxMacSES15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacSES15MinTceRept.setStatus("current")
_GbeClientCtpRxMacErrOctet15MinTceRept_Type = TruthValue
_GbeClientCtpRxMacErrOctet15MinTceRept_Object = MibTableColumn
gbeClientCtpRxMacErrOctet15MinTceRept = _GbeClientCtpRxMacErrOctet15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 116),
    _GbeClientCtpRxMacErrOctet15MinTceRept_Type()
)
gbeClientCtpRxMacErrOctet15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacErrOctet15MinTceRept.setStatus("current")
_GbeClientCtpRxMacJabber15MinTceRept_Type = TruthValue
_GbeClientCtpRxMacJabber15MinTceRept_Object = MibTableColumn
gbeClientCtpRxMacJabber15MinTceRept = _GbeClientCtpRxMacJabber15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 117),
    _GbeClientCtpRxMacJabber15MinTceRept_Type()
)
gbeClientCtpRxMacJabber15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacJabber15MinTceRept.setStatus("current")
_GbeClientCtpRxMacFragment15MinTceRept_Type = TruthValue
_GbeClientCtpRxMacFragment15MinTceRept_Object = MibTableColumn
gbeClientCtpRxMacFragment15MinTceRept = _GbeClientCtpRxMacFragment15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 118),
    _GbeClientCtpRxMacFragment15MinTceRept_Type()
)
gbeClientCtpRxMacFragment15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacFragment15MinTceRept.setStatus("current")
_GbeClientCtpRxMacCrcAligned15MinTceRept_Type = TruthValue
_GbeClientCtpRxMacCrcAligned15MinTceRept_Object = MibTableColumn
gbeClientCtpRxMacCrcAligned15MinTceRept = _GbeClientCtpRxMacCrcAligned15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 119),
    _GbeClientCtpRxMacCrcAligned15MinTceRept_Type()
)
gbeClientCtpRxMacCrcAligned15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacCrcAligned15MinTceRept.setStatus("current")
_GbeClientCtpRxMacUndersized15MinTceRept_Type = TruthValue
_GbeClientCtpRxMacUndersized15MinTceRept_Object = MibTableColumn
gbeClientCtpRxMacUndersized15MinTceRept = _GbeClientCtpRxMacUndersized15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 120),
    _GbeClientCtpRxMacUndersized15MinTceRept_Type()
)
gbeClientCtpRxMacUndersized15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacUndersized15MinTceRept.setStatus("current")
_GbeClientCtpRxMacOversize15MinTceRept_Type = TruthValue
_GbeClientCtpRxMacOversize15MinTceRept_Object = MibTableColumn
gbeClientCtpRxMacOversize15MinTceRept = _GbeClientCtpRxMacOversize15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 121),
    _GbeClientCtpRxMacOversize15MinTceRept_Type()
)
gbeClientCtpRxMacOversize15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacOversize15MinTceRept.setStatus("current")
_GbeClientCtpRxSize64P15MinTceRept_Type = TruthValue
_GbeClientCtpRxSize64P15MinTceRept_Object = MibTableColumn
gbeClientCtpRxSize64P15MinTceRept = _GbeClientCtpRxSize64P15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 122),
    _GbeClientCtpRxSize64P15MinTceRept_Type()
)
gbeClientCtpRxSize64P15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize64P15MinTceRept.setStatus("current")
_GbeClientCtpRxSize65to127P15MinTceRept_Type = TruthValue
_GbeClientCtpRxSize65to127P15MinTceRept_Object = MibTableColumn
gbeClientCtpRxSize65to127P15MinTceRept = _GbeClientCtpRxSize65to127P15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 123),
    _GbeClientCtpRxSize65to127P15MinTceRept_Type()
)
gbeClientCtpRxSize65to127P15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize65to127P15MinTceRept.setStatus("current")
_GbeClientCtpRxSize128to255P15MinTceRept_Type = TruthValue
_GbeClientCtpRxSize128to255P15MinTceRept_Object = MibTableColumn
gbeClientCtpRxSize128to255P15MinTceRept = _GbeClientCtpRxSize128to255P15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 124),
    _GbeClientCtpRxSize128to255P15MinTceRept_Type()
)
gbeClientCtpRxSize128to255P15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize128to255P15MinTceRept.setStatus("current")
_GbeClientCtpRxSize256to511P15MinTceRept_Type = TruthValue
_GbeClientCtpRxSize256to511P15MinTceRept_Object = MibTableColumn
gbeClientCtpRxSize256to511P15MinTceRept = _GbeClientCtpRxSize256to511P15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 125),
    _GbeClientCtpRxSize256to511P15MinTceRept_Type()
)
gbeClientCtpRxSize256to511P15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize256to511P15MinTceRept.setStatus("current")
_GbeClientCtpRxSize512to1023P15MinTceRept_Type = TruthValue
_GbeClientCtpRxSize512to1023P15MinTceRept_Object = MibTableColumn
gbeClientCtpRxSize512to1023P15MinTceRept = _GbeClientCtpRxSize512to1023P15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 126),
    _GbeClientCtpRxSize512to1023P15MinTceRept_Type()
)
gbeClientCtpRxSize512to1023P15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize512to1023P15MinTceRept.setStatus("current")
_GbeClientCtpRxSize1024to1518P15MinTceRept_Type = TruthValue
_GbeClientCtpRxSize1024to1518P15MinTceRept_Object = MibTableColumn
gbeClientCtpRxSize1024to1518P15MinTceRept = _GbeClientCtpRxSize1024to1518P15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 127),
    _GbeClientCtpRxSize1024to1518P15MinTceRept_Type()
)
gbeClientCtpRxSize1024to1518P15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize1024to1518P15MinTceRept.setStatus("current")
_GbeClientCtpRxSize1519toJumboP15MinTceRept_Type = TruthValue
_GbeClientCtpRxSize1519toJumboP15MinTceRept_Object = MibTableColumn
gbeClientCtpRxSize1519toJumboP15MinTceRept = _GbeClientCtpRxSize1519toJumboP15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 128),
    _GbeClientCtpRxSize1519toJumboP15MinTceRept_Type()
)
gbeClientCtpRxSize1519toJumboP15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize1519toJumboP15MinTceRept.setStatus("current")
_GbeClientCtpRxPackets15MinTceRept_Type = TruthValue
_GbeClientCtpRxPackets15MinTceRept_Object = MibTableColumn
gbeClientCtpRxPackets15MinTceRept = _GbeClientCtpRxPackets15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 129),
    _GbeClientCtpRxPackets15MinTceRept_Type()
)
gbeClientCtpRxPackets15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxPackets15MinTceRept.setStatus("current")
_GbeClientCtpRxOctets15MinTceRept_Type = TruthValue
_GbeClientCtpRxOctets15MinTceRept_Object = MibTableColumn
gbeClientCtpRxOctets15MinTceRept = _GbeClientCtpRxOctets15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 130),
    _GbeClientCtpRxOctets15MinTceRept_Type()
)
gbeClientCtpRxOctets15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxOctets15MinTceRept.setStatus("current")
_GbeClientCtpRxBroadcastPkts15MinTceRept_Type = TruthValue
_GbeClientCtpRxBroadcastPkts15MinTceRept_Object = MibTableColumn
gbeClientCtpRxBroadcastPkts15MinTceRept = _GbeClientCtpRxBroadcastPkts15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 131),
    _GbeClientCtpRxBroadcastPkts15MinTceRept_Type()
)
gbeClientCtpRxBroadcastPkts15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxBroadcastPkts15MinTceRept.setStatus("current")
_GbeClientCtpRxMulticastPkts15MinTceRept_Type = TruthValue
_GbeClientCtpRxMulticastPkts15MinTceRept_Object = MibTableColumn
gbeClientCtpRxMulticastPkts15MinTceRept = _GbeClientCtpRxMulticastPkts15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 132),
    _GbeClientCtpRxMulticastPkts15MinTceRept_Type()
)
gbeClientCtpRxMulticastPkts15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMulticastPkts15MinTceRept.setStatus("current")
_GbeClientCtpRxInPauseFrames15MinTceRept_Type = TruthValue
_GbeClientCtpRxInPauseFrames15MinTceRept_Object = MibTableColumn
gbeClientCtpRxInPauseFrames15MinTceRept = _GbeClientCtpRxInPauseFrames15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 133),
    _GbeClientCtpRxInPauseFrames15MinTceRept_Type()
)
gbeClientCtpRxInPauseFrames15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxInPauseFrames15MinTceRept.setStatus("current")
_GbeClientCtpRxMacJSDayTceRept_Type = TruthValue
_GbeClientCtpRxMacJSDayTceRept_Object = MibTableColumn
gbeClientCtpRxMacJSDayTceRept = _GbeClientCtpRxMacJSDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 134),
    _GbeClientCtpRxMacJSDayTceRept_Type()
)
gbeClientCtpRxMacJSDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacJSDayTceRept.setStatus("current")
_GbeClientCtpRxMacSESDayTceRept_Type = TruthValue
_GbeClientCtpRxMacSESDayTceRept_Object = MibTableColumn
gbeClientCtpRxMacSESDayTceRept = _GbeClientCtpRxMacSESDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 135),
    _GbeClientCtpRxMacSESDayTceRept_Type()
)
gbeClientCtpRxMacSESDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacSESDayTceRept.setStatus("current")
_GbeClientCtpRxMacErrOctetDayTceRept_Type = TruthValue
_GbeClientCtpRxMacErrOctetDayTceRept_Object = MibTableColumn
gbeClientCtpRxMacErrOctetDayTceRept = _GbeClientCtpRxMacErrOctetDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 136),
    _GbeClientCtpRxMacErrOctetDayTceRept_Type()
)
gbeClientCtpRxMacErrOctetDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacErrOctetDayTceRept.setStatus("current")
_GbeClientCtpRxMacJabberDayTceRept_Type = TruthValue
_GbeClientCtpRxMacJabberDayTceRept_Object = MibTableColumn
gbeClientCtpRxMacJabberDayTceRept = _GbeClientCtpRxMacJabberDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 137),
    _GbeClientCtpRxMacJabberDayTceRept_Type()
)
gbeClientCtpRxMacJabberDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacJabberDayTceRept.setStatus("current")
_GbeClientCtpRxMacFragmentDayTceRept_Type = TruthValue
_GbeClientCtpRxMacFragmentDayTceRept_Object = MibTableColumn
gbeClientCtpRxMacFragmentDayTceRept = _GbeClientCtpRxMacFragmentDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 138),
    _GbeClientCtpRxMacFragmentDayTceRept_Type()
)
gbeClientCtpRxMacFragmentDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacFragmentDayTceRept.setStatus("current")
_GbeClientCtpRxMacCrcAlignedDayTceRept_Type = TruthValue
_GbeClientCtpRxMacCrcAlignedDayTceRept_Object = MibTableColumn
gbeClientCtpRxMacCrcAlignedDayTceRept = _GbeClientCtpRxMacCrcAlignedDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 139),
    _GbeClientCtpRxMacCrcAlignedDayTceRept_Type()
)
gbeClientCtpRxMacCrcAlignedDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacCrcAlignedDayTceRept.setStatus("current")
_GbeClientCtpRxMacUndersizedDayTceRept_Type = TruthValue
_GbeClientCtpRxMacUndersizedDayTceRept_Object = MibTableColumn
gbeClientCtpRxMacUndersizedDayTceRept = _GbeClientCtpRxMacUndersizedDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 140),
    _GbeClientCtpRxMacUndersizedDayTceRept_Type()
)
gbeClientCtpRxMacUndersizedDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacUndersizedDayTceRept.setStatus("current")
_GbeClientCtpRxMacOversizeDayTceRept_Type = TruthValue
_GbeClientCtpRxMacOversizeDayTceRept_Object = MibTableColumn
gbeClientCtpRxMacOversizeDayTceRept = _GbeClientCtpRxMacOversizeDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 141),
    _GbeClientCtpRxMacOversizeDayTceRept_Type()
)
gbeClientCtpRxMacOversizeDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMacOversizeDayTceRept.setStatus("current")
_GbeClientCtpRxSize64DayTceRept_Type = TruthValue
_GbeClientCtpRxSize64DayTceRept_Object = MibTableColumn
gbeClientCtpRxSize64DayTceRept = _GbeClientCtpRxSize64DayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 142),
    _GbeClientCtpRxSize64DayTceRept_Type()
)
gbeClientCtpRxSize64DayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize64DayTceRept.setStatus("current")
_GbeClientCtpRxSize65to127DayTceRept_Type = TruthValue
_GbeClientCtpRxSize65to127DayTceRept_Object = MibTableColumn
gbeClientCtpRxSize65to127DayTceRept = _GbeClientCtpRxSize65to127DayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 143),
    _GbeClientCtpRxSize65to127DayTceRept_Type()
)
gbeClientCtpRxSize65to127DayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize65to127DayTceRept.setStatus("current")
_GbeClientCtpRxSize128to255DayTceRept_Type = TruthValue
_GbeClientCtpRxSize128to255DayTceRept_Object = MibTableColumn
gbeClientCtpRxSize128to255DayTceRept = _GbeClientCtpRxSize128to255DayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 144),
    _GbeClientCtpRxSize128to255DayTceRept_Type()
)
gbeClientCtpRxSize128to255DayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize128to255DayTceRept.setStatus("current")
_GbeClientCtpRxSize256to511DayTceRept_Type = TruthValue
_GbeClientCtpRxSize256to511DayTceRept_Object = MibTableColumn
gbeClientCtpRxSize256to511DayTceRept = _GbeClientCtpRxSize256to511DayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 145),
    _GbeClientCtpRxSize256to511DayTceRept_Type()
)
gbeClientCtpRxSize256to511DayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize256to511DayTceRept.setStatus("current")
_GbeClientCtpRxSize512to1023DayTceRept_Type = TruthValue
_GbeClientCtpRxSize512to1023DayTceRept_Object = MibTableColumn
gbeClientCtpRxSize512to1023DayTceRept = _GbeClientCtpRxSize512to1023DayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 146),
    _GbeClientCtpRxSize512to1023DayTceRept_Type()
)
gbeClientCtpRxSize512to1023DayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize512to1023DayTceRept.setStatus("current")
_GbeClientCtpRxSize1024to1518DayTceRept_Type = TruthValue
_GbeClientCtpRxSize1024to1518DayTceRept_Object = MibTableColumn
gbeClientCtpRxSize1024to1518DayTceRept = _GbeClientCtpRxSize1024to1518DayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 147),
    _GbeClientCtpRxSize1024to1518DayTceRept_Type()
)
gbeClientCtpRxSize1024to1518DayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize1024to1518DayTceRept.setStatus("current")
_GbeClientCtpRxSize1519toJumboDayTceRept_Type = TruthValue
_GbeClientCtpRxSize1519toJumboDayTceRept_Object = MibTableColumn
gbeClientCtpRxSize1519toJumboDayTceRept = _GbeClientCtpRxSize1519toJumboDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 148),
    _GbeClientCtpRxSize1519toJumboDayTceRept_Type()
)
gbeClientCtpRxSize1519toJumboDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize1519toJumboDayTceRept.setStatus("current")
_GbeClientCtpRxPacketsDayTceRept_Type = TruthValue
_GbeClientCtpRxPacketsDayTceRept_Object = MibTableColumn
gbeClientCtpRxPacketsDayTceRept = _GbeClientCtpRxPacketsDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 149),
    _GbeClientCtpRxPacketsDayTceRept_Type()
)
gbeClientCtpRxPacketsDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxPacketsDayTceRept.setStatus("current")
_GbeClientCtpRxOctetsDayTceRept_Type = TruthValue
_GbeClientCtpRxOctetsDayTceRept_Object = MibTableColumn
gbeClientCtpRxOctetsDayTceRept = _GbeClientCtpRxOctetsDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 150),
    _GbeClientCtpRxOctetsDayTceRept_Type()
)
gbeClientCtpRxOctetsDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxOctetsDayTceRept.setStatus("current")
_GbeClientCtpRxBroadcastPktsDayTceRept_Type = TruthValue
_GbeClientCtpRxBroadcastPktsDayTceRept_Object = MibTableColumn
gbeClientCtpRxBroadcastPktsDayTceRept = _GbeClientCtpRxBroadcastPktsDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 151),
    _GbeClientCtpRxBroadcastPktsDayTceRept_Type()
)
gbeClientCtpRxBroadcastPktsDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxBroadcastPktsDayTceRept.setStatus("current")
_GbeClientCtpRxMulticastPktsDayTceRept_Type = TruthValue
_GbeClientCtpRxMulticastPktsDayTceRept_Object = MibTableColumn
gbeClientCtpRxMulticastPktsDayTceRept = _GbeClientCtpRxMulticastPktsDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 152),
    _GbeClientCtpRxMulticastPktsDayTceRept_Type()
)
gbeClientCtpRxMulticastPktsDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxMulticastPktsDayTceRept.setStatus("current")
_GbeClientCtpRxInPauseFramesDayTceRept_Type = TruthValue
_GbeClientCtpRxInPauseFramesDayTceRept_Object = MibTableColumn
gbeClientCtpRxInPauseFramesDayTceRept = _GbeClientCtpRxInPauseFramesDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 153),
    _GbeClientCtpRxInPauseFramesDayTceRept_Type()
)
gbeClientCtpRxInPauseFramesDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxInPauseFramesDayTceRept.setStatus("current")
_GbeClientCtpTxPcsICG15MinTceRept_Type = TruthValue
_GbeClientCtpTxPcsICG15MinTceRept_Object = MibTableColumn
gbeClientCtpTxPcsICG15MinTceRept = _GbeClientCtpTxPcsICG15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 154),
    _GbeClientCtpTxPcsICG15MinTceRept_Type()
)
gbeClientCtpTxPcsICG15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxPcsICG15MinTceRept.setStatus("current")
_GbeClientCtpTxPcsES15MinTceRept_Type = TruthValue
_GbeClientCtpTxPcsES15MinTceRept_Object = MibTableColumn
gbeClientCtpTxPcsES15MinTceRept = _GbeClientCtpTxPcsES15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 155),
    _GbeClientCtpTxPcsES15MinTceRept_Type()
)
gbeClientCtpTxPcsES15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxPcsES15MinTceRept.setStatus("current")
_GbeClientCtpTxPcsSES15MinTceRept_Type = TruthValue
_GbeClientCtpTxPcsSES15MinTceRept_Object = MibTableColumn
gbeClientCtpTxPcsSES15MinTceRept = _GbeClientCtpTxPcsSES15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 156),
    _GbeClientCtpTxPcsSES15MinTceRept_Type()
)
gbeClientCtpTxPcsSES15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxPcsSES15MinTceRept.setStatus("current")
_GbeClientCtpTxPcsSESS15MinTceRept_Type = TruthValue
_GbeClientCtpTxPcsSESS15MinTceRept_Object = MibTableColumn
gbeClientCtpTxPcsSESS15MinTceRept = _GbeClientCtpTxPcsSESS15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 157),
    _GbeClientCtpTxPcsSESS15MinTceRept_Type()
)
gbeClientCtpTxPcsSESS15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxPcsSESS15MinTceRept.setStatus("current")
_GbeClientCtpTxPcsICGDayTceRept_Type = TruthValue
_GbeClientCtpTxPcsICGDayTceRept_Object = MibTableColumn
gbeClientCtpTxPcsICGDayTceRept = _GbeClientCtpTxPcsICGDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 158),
    _GbeClientCtpTxPcsICGDayTceRept_Type()
)
gbeClientCtpTxPcsICGDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxPcsICGDayTceRept.setStatus("current")
_GbeClientCtpTxPcsESDayTceRept_Type = TruthValue
_GbeClientCtpTxPcsESDayTceRept_Object = MibTableColumn
gbeClientCtpTxPcsESDayTceRept = _GbeClientCtpTxPcsESDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 159),
    _GbeClientCtpTxPcsESDayTceRept_Type()
)
gbeClientCtpTxPcsESDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxPcsESDayTceRept.setStatus("current")
_GbeClientCtpTxPcsSESDayTceRept_Type = TruthValue
_GbeClientCtpTxPcsSESDayTceRept_Object = MibTableColumn
gbeClientCtpTxPcsSESDayTceRept = _GbeClientCtpTxPcsSESDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 160),
    _GbeClientCtpTxPcsSESDayTceRept_Type()
)
gbeClientCtpTxPcsSESDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxPcsSESDayTceRept.setStatus("current")
_GbeClientCtpTxPcsSESSDayTceRept_Type = TruthValue
_GbeClientCtpTxPcsSESSDayTceRept_Object = MibTableColumn
gbeClientCtpTxPcsSESSDayTceRept = _GbeClientCtpTxPcsSESSDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 161),
    _GbeClientCtpTxPcsSESSDayTceRept_Type()
)
gbeClientCtpTxPcsSESSDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxPcsSESSDayTceRept.setStatus("current")
_GbeClientCtpTxMacJS15MinTceRept_Type = TruthValue
_GbeClientCtpTxMacJS15MinTceRept_Object = MibTableColumn
gbeClientCtpTxMacJS15MinTceRept = _GbeClientCtpTxMacJS15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 162),
    _GbeClientCtpTxMacJS15MinTceRept_Type()
)
gbeClientCtpTxMacJS15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacJS15MinTceRept.setStatus("current")
_GbeClientCtpTxMacSES15MinTceRept_Type = TruthValue
_GbeClientCtpTxMacSES15MinTceRept_Object = MibTableColumn
gbeClientCtpTxMacSES15MinTceRept = _GbeClientCtpTxMacSES15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 163),
    _GbeClientCtpTxMacSES15MinTceRept_Type()
)
gbeClientCtpTxMacSES15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacSES15MinTceRept.setStatus("current")
_GbeClientCtpTxMacErrOctet15MinTceRept_Type = TruthValue
_GbeClientCtpTxMacErrOctet15MinTceRept_Object = MibTableColumn
gbeClientCtpTxMacErrOctet15MinTceRept = _GbeClientCtpTxMacErrOctet15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 164),
    _GbeClientCtpTxMacErrOctet15MinTceRept_Type()
)
gbeClientCtpTxMacErrOctet15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacErrOctet15MinTceRept.setStatus("current")
_GbeClientCtpTxMacJabber15MinTceRept_Type = TruthValue
_GbeClientCtpTxMacJabber15MinTceRept_Object = MibTableColumn
gbeClientCtpTxMacJabber15MinTceRept = _GbeClientCtpTxMacJabber15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 165),
    _GbeClientCtpTxMacJabber15MinTceRept_Type()
)
gbeClientCtpTxMacJabber15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacJabber15MinTceRept.setStatus("current")
_GbeClientCtpTxMacFragment15MinTceRept_Type = TruthValue
_GbeClientCtpTxMacFragment15MinTceRept_Object = MibTableColumn
gbeClientCtpTxMacFragment15MinTceRept = _GbeClientCtpTxMacFragment15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 166),
    _GbeClientCtpTxMacFragment15MinTceRept_Type()
)
gbeClientCtpTxMacFragment15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacFragment15MinTceRept.setStatus("current")
_GbeClientCtpTxMacCrcAligned15MinTceRept_Type = TruthValue
_GbeClientCtpTxMacCrcAligned15MinTceRept_Object = MibTableColumn
gbeClientCtpTxMacCrcAligned15MinTceRept = _GbeClientCtpTxMacCrcAligned15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 167),
    _GbeClientCtpTxMacCrcAligned15MinTceRept_Type()
)
gbeClientCtpTxMacCrcAligned15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacCrcAligned15MinTceRept.setStatus("current")
_GbeClientCtpTxMacUndersized15MinTceRept_Type = TruthValue
_GbeClientCtpTxMacUndersized15MinTceRept_Object = MibTableColumn
gbeClientCtpTxMacUndersized15MinTceRept = _GbeClientCtpTxMacUndersized15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 168),
    _GbeClientCtpTxMacUndersized15MinTceRept_Type()
)
gbeClientCtpTxMacUndersized15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacUndersized15MinTceRept.setStatus("current")
_GbeClientCtpTxMacOversize15MinTceRept_Type = TruthValue
_GbeClientCtpTxMacOversize15MinTceRept_Object = MibTableColumn
gbeClientCtpTxMacOversize15MinTceRept = _GbeClientCtpTxMacOversize15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 169),
    _GbeClientCtpTxMacOversize15MinTceRept_Type()
)
gbeClientCtpTxMacOversize15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacOversize15MinTceRept.setStatus("current")
_GbeClientCtpTxSize64P15MinTceRept_Type = TruthValue
_GbeClientCtpTxSize64P15MinTceRept_Object = MibTableColumn
gbeClientCtpTxSize64P15MinTceRept = _GbeClientCtpTxSize64P15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 170),
    _GbeClientCtpTxSize64P15MinTceRept_Type()
)
gbeClientCtpTxSize64P15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize64P15MinTceRept.setStatus("current")
_GbeClientCtpTxSize65to127P15MinTceRept_Type = TruthValue
_GbeClientCtpTxSize65to127P15MinTceRept_Object = MibTableColumn
gbeClientCtpTxSize65to127P15MinTceRept = _GbeClientCtpTxSize65to127P15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 171),
    _GbeClientCtpTxSize65to127P15MinTceRept_Type()
)
gbeClientCtpTxSize65to127P15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize65to127P15MinTceRept.setStatus("current")
_GbeClientCtpTxSize128to255P15MinTceRept_Type = TruthValue
_GbeClientCtpTxSize128to255P15MinTceRept_Object = MibTableColumn
gbeClientCtpTxSize128to255P15MinTceRept = _GbeClientCtpTxSize128to255P15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 172),
    _GbeClientCtpTxSize128to255P15MinTceRept_Type()
)
gbeClientCtpTxSize128to255P15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize128to255P15MinTceRept.setStatus("current")
_GbeClientCtpTxSize256to511P15MinTceRept_Type = TruthValue
_GbeClientCtpTxSize256to511P15MinTceRept_Object = MibTableColumn
gbeClientCtpTxSize256to511P15MinTceRept = _GbeClientCtpTxSize256to511P15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 173),
    _GbeClientCtpTxSize256to511P15MinTceRept_Type()
)
gbeClientCtpTxSize256to511P15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize256to511P15MinTceRept.setStatus("current")
_GbeClientCtpTxSize512to1023P15MinTceRept_Type = TruthValue
_GbeClientCtpTxSize512to1023P15MinTceRept_Object = MibTableColumn
gbeClientCtpTxSize512to1023P15MinTceRept = _GbeClientCtpTxSize512to1023P15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 174),
    _GbeClientCtpTxSize512to1023P15MinTceRept_Type()
)
gbeClientCtpTxSize512to1023P15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize512to1023P15MinTceRept.setStatus("current")
_GbeClientCtpTxSize1024to1518P15MinTceRept_Type = TruthValue
_GbeClientCtpTxSize1024to1518P15MinTceRept_Object = MibTableColumn
gbeClientCtpTxSize1024to1518P15MinTceRept = _GbeClientCtpTxSize1024to1518P15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 175),
    _GbeClientCtpTxSize1024to1518P15MinTceRept_Type()
)
gbeClientCtpTxSize1024to1518P15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize1024to1518P15MinTceRept.setStatus("current")
_GbeClientCtpTxSize1519toJumboP15MinTceRept_Type = TruthValue
_GbeClientCtpTxSize1519toJumboP15MinTceRept_Object = MibTableColumn
gbeClientCtpTxSize1519toJumboP15MinTceRept = _GbeClientCtpTxSize1519toJumboP15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 176),
    _GbeClientCtpTxSize1519toJumboP15MinTceRept_Type()
)
gbeClientCtpTxSize1519toJumboP15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize1519toJumboP15MinTceRept.setStatus("current")
_GbeClientCtpTxPackets15MinTceRept_Type = TruthValue
_GbeClientCtpTxPackets15MinTceRept_Object = MibTableColumn
gbeClientCtpTxPackets15MinTceRept = _GbeClientCtpTxPackets15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 177),
    _GbeClientCtpTxPackets15MinTceRept_Type()
)
gbeClientCtpTxPackets15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxPackets15MinTceRept.setStatus("current")
_GbeClientCtpTxOctets15MinTceRept_Type = TruthValue
_GbeClientCtpTxOctets15MinTceRept_Object = MibTableColumn
gbeClientCtpTxOctets15MinTceRept = _GbeClientCtpTxOctets15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 178),
    _GbeClientCtpTxOctets15MinTceRept_Type()
)
gbeClientCtpTxOctets15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxOctets15MinTceRept.setStatus("current")
_GbeClientCtpTxBroadcastPkts15MinTceRept_Type = TruthValue
_GbeClientCtpTxBroadcastPkts15MinTceRept_Object = MibTableColumn
gbeClientCtpTxBroadcastPkts15MinTceRept = _GbeClientCtpTxBroadcastPkts15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 179),
    _GbeClientCtpTxBroadcastPkts15MinTceRept_Type()
)
gbeClientCtpTxBroadcastPkts15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxBroadcastPkts15MinTceRept.setStatus("current")
_GbeClientCtpTxMulticastPkts15MinTceRept_Type = TruthValue
_GbeClientCtpTxMulticastPkts15MinTceRept_Object = MibTableColumn
gbeClientCtpTxMulticastPkts15MinTceRept = _GbeClientCtpTxMulticastPkts15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 180),
    _GbeClientCtpTxMulticastPkts15MinTceRept_Type()
)
gbeClientCtpTxMulticastPkts15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMulticastPkts15MinTceRept.setStatus("current")
_GbeClientCtpTxOutPauseFrames15MinTceRept_Type = TruthValue
_GbeClientCtpTxOutPauseFrames15MinTceRept_Object = MibTableColumn
gbeClientCtpTxOutPauseFrames15MinTceRept = _GbeClientCtpTxOutPauseFrames15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 181),
    _GbeClientCtpTxOutPauseFrames15MinTceRept_Type()
)
gbeClientCtpTxOutPauseFrames15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxOutPauseFrames15MinTceRept.setStatus("current")
_GbeClientCtpTxMacJSDayTceRept_Type = TruthValue
_GbeClientCtpTxMacJSDayTceRept_Object = MibTableColumn
gbeClientCtpTxMacJSDayTceRept = _GbeClientCtpTxMacJSDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 182),
    _GbeClientCtpTxMacJSDayTceRept_Type()
)
gbeClientCtpTxMacJSDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacJSDayTceRept.setStatus("current")
_GbeClientCtpTxMacSESDayTceRept_Type = TruthValue
_GbeClientCtpTxMacSESDayTceRept_Object = MibTableColumn
gbeClientCtpTxMacSESDayTceRept = _GbeClientCtpTxMacSESDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 183),
    _GbeClientCtpTxMacSESDayTceRept_Type()
)
gbeClientCtpTxMacSESDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacSESDayTceRept.setStatus("current")
_GbeClientCtpTxMacErrOctetDayTceRept_Type = TruthValue
_GbeClientCtpTxMacErrOctetDayTceRept_Object = MibTableColumn
gbeClientCtpTxMacErrOctetDayTceRept = _GbeClientCtpTxMacErrOctetDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 184),
    _GbeClientCtpTxMacErrOctetDayTceRept_Type()
)
gbeClientCtpTxMacErrOctetDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacErrOctetDayTceRept.setStatus("current")
_GbeClientCtpTxMacJabberDayTceRept_Type = TruthValue
_GbeClientCtpTxMacJabberDayTceRept_Object = MibTableColumn
gbeClientCtpTxMacJabberDayTceRept = _GbeClientCtpTxMacJabberDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 185),
    _GbeClientCtpTxMacJabberDayTceRept_Type()
)
gbeClientCtpTxMacJabberDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacJabberDayTceRept.setStatus("current")
_GbeClientCtpTxMacFragmentDayTceRept_Type = TruthValue
_GbeClientCtpTxMacFragmentDayTceRept_Object = MibTableColumn
gbeClientCtpTxMacFragmentDayTceRept = _GbeClientCtpTxMacFragmentDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 186),
    _GbeClientCtpTxMacFragmentDayTceRept_Type()
)
gbeClientCtpTxMacFragmentDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacFragmentDayTceRept.setStatus("current")
_GbeClientCtpTxMacCrcAlignedDayTceRept_Type = TruthValue
_GbeClientCtpTxMacCrcAlignedDayTceRept_Object = MibTableColumn
gbeClientCtpTxMacCrcAlignedDayTceRept = _GbeClientCtpTxMacCrcAlignedDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 187),
    _GbeClientCtpTxMacCrcAlignedDayTceRept_Type()
)
gbeClientCtpTxMacCrcAlignedDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacCrcAlignedDayTceRept.setStatus("current")
_GbeClientCtpTxMacUndersizedDayTceRept_Type = TruthValue
_GbeClientCtpTxMacUndersizedDayTceRept_Object = MibTableColumn
gbeClientCtpTxMacUndersizedDayTceRept = _GbeClientCtpTxMacUndersizedDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 188),
    _GbeClientCtpTxMacUndersizedDayTceRept_Type()
)
gbeClientCtpTxMacUndersizedDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacUndersizedDayTceRept.setStatus("current")
_GbeClientCtpTxMacOversizeDayTceRept_Type = TruthValue
_GbeClientCtpTxMacOversizeDayTceRept_Object = MibTableColumn
gbeClientCtpTxMacOversizeDayTceRept = _GbeClientCtpTxMacOversizeDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 189),
    _GbeClientCtpTxMacOversizeDayTceRept_Type()
)
gbeClientCtpTxMacOversizeDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMacOversizeDayTceRept.setStatus("current")
_GbeClientCtpTxSize64DayTceRept_Type = TruthValue
_GbeClientCtpTxSize64DayTceRept_Object = MibTableColumn
gbeClientCtpTxSize64DayTceRept = _GbeClientCtpTxSize64DayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 190),
    _GbeClientCtpTxSize64DayTceRept_Type()
)
gbeClientCtpTxSize64DayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize64DayTceRept.setStatus("current")
_GbeClientCtpTxSize65to127DayTceRept_Type = TruthValue
_GbeClientCtpTxSize65to127DayTceRept_Object = MibTableColumn
gbeClientCtpTxSize65to127DayTceRept = _GbeClientCtpTxSize65to127DayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 191),
    _GbeClientCtpTxSize65to127DayTceRept_Type()
)
gbeClientCtpTxSize65to127DayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize65to127DayTceRept.setStatus("current")
_GbeClientCtpTxSize128to255DayTceRept_Type = TruthValue
_GbeClientCtpTxSize128to255DayTceRept_Object = MibTableColumn
gbeClientCtpTxSize128to255DayTceRept = _GbeClientCtpTxSize128to255DayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 192),
    _GbeClientCtpTxSize128to255DayTceRept_Type()
)
gbeClientCtpTxSize128to255DayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize128to255DayTceRept.setStatus("current")
_GbeClientCtpTxSize256to511DayTceRept_Type = TruthValue
_GbeClientCtpTxSize256to511DayTceRept_Object = MibTableColumn
gbeClientCtpTxSize256to511DayTceRept = _GbeClientCtpTxSize256to511DayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 193),
    _GbeClientCtpTxSize256to511DayTceRept_Type()
)
gbeClientCtpTxSize256to511DayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize256to511DayTceRept.setStatus("current")
_GbeClientCtpTxSize512to1023DayTceRept_Type = TruthValue
_GbeClientCtpTxSize512to1023DayTceRept_Object = MibTableColumn
gbeClientCtpTxSize512to1023DayTceRept = _GbeClientCtpTxSize512to1023DayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 194),
    _GbeClientCtpTxSize512to1023DayTceRept_Type()
)
gbeClientCtpTxSize512to1023DayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize512to1023DayTceRept.setStatus("current")
_GbeClientCtpTxSize1024to1518DayTceRept_Type = TruthValue
_GbeClientCtpTxSize1024to1518DayTceRept_Object = MibTableColumn
gbeClientCtpTxSize1024to1518DayTceRept = _GbeClientCtpTxSize1024to1518DayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 195),
    _GbeClientCtpTxSize1024to1518DayTceRept_Type()
)
gbeClientCtpTxSize1024to1518DayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize1024to1518DayTceRept.setStatus("current")
_GbeClientCtpTxSize1519toJumboDayTceRept_Type = TruthValue
_GbeClientCtpTxSize1519toJumboDayTceRept_Object = MibTableColumn
gbeClientCtpTxSize1519toJumboDayTceRept = _GbeClientCtpTxSize1519toJumboDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 196),
    _GbeClientCtpTxSize1519toJumboDayTceRept_Type()
)
gbeClientCtpTxSize1519toJumboDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize1519toJumboDayTceRept.setStatus("current")
_GbeClientCtpTxPacketsDayTceRept_Type = TruthValue
_GbeClientCtpTxPacketsDayTceRept_Object = MibTableColumn
gbeClientCtpTxPacketsDayTceRept = _GbeClientCtpTxPacketsDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 197),
    _GbeClientCtpTxPacketsDayTceRept_Type()
)
gbeClientCtpTxPacketsDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxPacketsDayTceRept.setStatus("current")
_GbeClientCtpTxOctetsDayTceRept_Type = TruthValue
_GbeClientCtpTxOctetsDayTceRept_Object = MibTableColumn
gbeClientCtpTxOctetsDayTceRept = _GbeClientCtpTxOctetsDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 198),
    _GbeClientCtpTxOctetsDayTceRept_Type()
)
gbeClientCtpTxOctetsDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxOctetsDayTceRept.setStatus("current")
_GbeClientCtpTxBroadcastPktsDayTceRept_Type = TruthValue
_GbeClientCtpTxBroadcastPktsDayTceRept_Object = MibTableColumn
gbeClientCtpTxBroadcastPktsDayTceRept = _GbeClientCtpTxBroadcastPktsDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 199),
    _GbeClientCtpTxBroadcastPktsDayTceRept_Type()
)
gbeClientCtpTxBroadcastPktsDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxBroadcastPktsDayTceRept.setStatus("current")
_GbeClientCtpTxMulticastPktsDayTceRept_Type = TruthValue
_GbeClientCtpTxMulticastPktsDayTceRept_Object = MibTableColumn
gbeClientCtpTxMulticastPktsDayTceRept = _GbeClientCtpTxMulticastPktsDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 200),
    _GbeClientCtpTxMulticastPktsDayTceRept_Type()
)
gbeClientCtpTxMulticastPktsDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxMulticastPktsDayTceRept.setStatus("current")
_GbeClientCtpTxOutPauseFramesDayTceRept_Type = TruthValue
_GbeClientCtpTxOutPauseFramesDayTceRept_Object = MibTableColumn
gbeClientCtpTxOutPauseFramesDayTceRept = _GbeClientCtpTxOutPauseFramesDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 201),
    _GbeClientCtpTxOutPauseFramesDayTceRept_Type()
)
gbeClientCtpTxOutPauseFramesDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxOutPauseFramesDayTceRept.setStatus("current")
_GbeClientCtpRxSize1024to1522P15MinTce_Type = Integer32
_GbeClientCtpRxSize1024to1522P15MinTce_Object = MibTableColumn
gbeClientCtpRxSize1024to1522P15MinTce = _GbeClientCtpRxSize1024to1522P15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 202),
    _GbeClientCtpRxSize1024to1522P15MinTce_Type()
)
gbeClientCtpRxSize1024to1522P15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize1024to1522P15MinTce.setStatus("current")
_GbeClientCtpRxSize1523toJumboP15MinTce_Type = Integer32
_GbeClientCtpRxSize1523toJumboP15MinTce_Object = MibTableColumn
gbeClientCtpRxSize1523toJumboP15MinTce = _GbeClientCtpRxSize1523toJumboP15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 203),
    _GbeClientCtpRxSize1523toJumboP15MinTce_Type()
)
gbeClientCtpRxSize1523toJumboP15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize1523toJumboP15MinTce.setStatus("current")
_GbeClientCtpRxSize1024to1522DayTce_Type = Integer32
_GbeClientCtpRxSize1024to1522DayTce_Object = MibTableColumn
gbeClientCtpRxSize1024to1522DayTce = _GbeClientCtpRxSize1024to1522DayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 204),
    _GbeClientCtpRxSize1024to1522DayTce_Type()
)
gbeClientCtpRxSize1024to1522DayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize1024to1522DayTce.setStatus("current")
_GbeClientCtpRxSize1523toJumboDayTce_Type = Integer32
_GbeClientCtpRxSize1523toJumboDayTce_Object = MibTableColumn
gbeClientCtpRxSize1523toJumboDayTce = _GbeClientCtpRxSize1523toJumboDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 205),
    _GbeClientCtpRxSize1523toJumboDayTce_Type()
)
gbeClientCtpRxSize1523toJumboDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize1523toJumboDayTce.setStatus("current")
_GbeClientCtpTxSize1024to1522P15MinTce_Type = Integer32
_GbeClientCtpTxSize1024to1522P15MinTce_Object = MibTableColumn
gbeClientCtpTxSize1024to1522P15MinTce = _GbeClientCtpTxSize1024to1522P15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 206),
    _GbeClientCtpTxSize1024to1522P15MinTce_Type()
)
gbeClientCtpTxSize1024to1522P15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize1024to1522P15MinTce.setStatus("current")
_GbeClientCtpTxSize1523toJumboP15MinTce_Type = Integer32
_GbeClientCtpTxSize1523toJumboP15MinTce_Object = MibTableColumn
gbeClientCtpTxSize1523toJumboP15MinTce = _GbeClientCtpTxSize1523toJumboP15MinTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 207),
    _GbeClientCtpTxSize1523toJumboP15MinTce_Type()
)
gbeClientCtpTxSize1523toJumboP15MinTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize1523toJumboP15MinTce.setStatus("current")
_GbeClientCtpTxSize1024to1522DayTce_Type = Integer32
_GbeClientCtpTxSize1024to1522DayTce_Object = MibTableColumn
gbeClientCtpTxSize1024to1522DayTce = _GbeClientCtpTxSize1024to1522DayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 208),
    _GbeClientCtpTxSize1024to1522DayTce_Type()
)
gbeClientCtpTxSize1024to1522DayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize1024to1522DayTce.setStatus("current")
_GbeClientCtpTxSize1523toJumboDayTce_Type = Integer32
_GbeClientCtpTxSize1523toJumboDayTce_Object = MibTableColumn
gbeClientCtpTxSize1523toJumboDayTce = _GbeClientCtpTxSize1523toJumboDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 209),
    _GbeClientCtpTxSize1523toJumboDayTce_Type()
)
gbeClientCtpTxSize1523toJumboDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize1523toJumboDayTce.setStatus("current")
_GbeClientCtpRxSize1024to1522P15MinTceRept_Type = TruthValue
_GbeClientCtpRxSize1024to1522P15MinTceRept_Object = MibTableColumn
gbeClientCtpRxSize1024to1522P15MinTceRept = _GbeClientCtpRxSize1024to1522P15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 210),
    _GbeClientCtpRxSize1024to1522P15MinTceRept_Type()
)
gbeClientCtpRxSize1024to1522P15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize1024to1522P15MinTceRept.setStatus("current")
_GbeClientCtpRxSize1523toJumboP15MinTceRept_Type = TruthValue
_GbeClientCtpRxSize1523toJumboP15MinTceRept_Object = MibTableColumn
gbeClientCtpRxSize1523toJumboP15MinTceRept = _GbeClientCtpRxSize1523toJumboP15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 211),
    _GbeClientCtpRxSize1523toJumboP15MinTceRept_Type()
)
gbeClientCtpRxSize1523toJumboP15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize1523toJumboP15MinTceRept.setStatus("current")
_GbeClientCtpRxSize1024to1522DayTceRept_Type = TruthValue
_GbeClientCtpRxSize1024to1522DayTceRept_Object = MibTableColumn
gbeClientCtpRxSize1024to1522DayTceRept = _GbeClientCtpRxSize1024to1522DayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 212),
    _GbeClientCtpRxSize1024to1522DayTceRept_Type()
)
gbeClientCtpRxSize1024to1522DayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize1024to1522DayTceRept.setStatus("current")
_GbeClientCtpRxSize1523toJumboDayTceRept_Type = TruthValue
_GbeClientCtpRxSize1523toJumboDayTceRept_Object = MibTableColumn
gbeClientCtpRxSize1523toJumboDayTceRept = _GbeClientCtpRxSize1523toJumboDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 213),
    _GbeClientCtpRxSize1523toJumboDayTceRept_Type()
)
gbeClientCtpRxSize1523toJumboDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpRxSize1523toJumboDayTceRept.setStatus("current")
_GbeClientCtpTxSize1024to1522P15MinTceRept_Type = TruthValue
_GbeClientCtpTxSize1024to1522P15MinTceRept_Object = MibTableColumn
gbeClientCtpTxSize1024to1522P15MinTceRept = _GbeClientCtpTxSize1024to1522P15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 214),
    _GbeClientCtpTxSize1024to1522P15MinTceRept_Type()
)
gbeClientCtpTxSize1024to1522P15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize1024to1522P15MinTceRept.setStatus("current")
_GbeClientCtpTxSize1523toJumboP15MinTceRept_Type = TruthValue
_GbeClientCtpTxSize1523toJumboP15MinTceRept_Object = MibTableColumn
gbeClientCtpTxSize1523toJumboP15MinTceRept = _GbeClientCtpTxSize1523toJumboP15MinTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 215),
    _GbeClientCtpTxSize1523toJumboP15MinTceRept_Type()
)
gbeClientCtpTxSize1523toJumboP15MinTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize1523toJumboP15MinTceRept.setStatus("current")
_GbeClientCtpTxSize1024to1522DayTceRept_Type = TruthValue
_GbeClientCtpTxSize1024to1522DayTceRept_Object = MibTableColumn
gbeClientCtpTxSize1024to1522DayTceRept = _GbeClientCtpTxSize1024to1522DayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 216),
    _GbeClientCtpTxSize1024to1522DayTceRept_Type()
)
gbeClientCtpTxSize1024to1522DayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize1024to1522DayTceRept.setStatus("current")
_GbeClientCtpTxSize1523toJumboDayTceRept_Type = TruthValue
_GbeClientCtpTxSize1523toJumboDayTceRept_Object = MibTableColumn
gbeClientCtpTxSize1523toJumboDayTceRept = _GbeClientCtpTxSize1523toJumboDayTceRept_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 217),
    _GbeClientCtpTxSize1523toJumboDayTceRept_Type()
)
gbeClientCtpTxSize1523toJumboDayTceRept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpTxSize1523toJumboDayTceRept.setStatus("current")


class _GbeClientCtpEncapTribDisableAction_Type(InfnTribDisableAction):
    """Custom type gbeClientCtpEncapTribDisableAction based on InfnTribDisableAction"""
    defaultValue = 5


_GbeClientCtpEncapTribDisableAction_Type.__name__ = "InfnTribDisableAction"
_GbeClientCtpEncapTribDisableAction_Object = MibTableColumn
gbeClientCtpEncapTribDisableAction = _GbeClientCtpEncapTribDisableAction_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 218),
    _GbeClientCtpEncapTribDisableAction_Type()
)
gbeClientCtpEncapTribDisableAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpEncapTribDisableAction.setStatus("current")
_GbeClientCtpServiceMode_Type = InfnServiceMode
_GbeClientCtpServiceMode_Object = MibTableColumn
gbeClientCtpServiceMode = _GbeClientCtpServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 219),
    _GbeClientCtpServiceMode_Type()
)
gbeClientCtpServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbeClientCtpServiceMode.setStatus("current")
_GbeClientCtpServiceModeQualifier_Type = InfnSMQ
_GbeClientCtpServiceModeQualifier_Object = MibTableColumn
gbeClientCtpServiceModeQualifier = _GbeClientCtpServiceModeQualifier_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 220),
    _GbeClientCtpServiceModeQualifier_Type()
)
gbeClientCtpServiceModeQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbeClientCtpServiceModeQualifier.setStatus("current")
_GbeClientCtpHostAddress_Type = DisplayString
_GbeClientCtpHostAddress_Object = MibTableColumn
gbeClientCtpHostAddress = _GbeClientCtpHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 221),
    _GbeClientCtpHostAddress_Type()
)
gbeClientCtpHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpHostAddress.setStatus("current")
_GbeClientCtpHostControlTableSize_Type = DisplayString
_GbeClientCtpHostControlTableSize_Object = MibTableColumn
gbeClientCtpHostControlTableSize = _GbeClientCtpHostControlTableSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 222),
    _GbeClientCtpHostControlTableSize_Type()
)
gbeClientCtpHostControlTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpHostControlTableSize.setStatus("current")
_GbeClientCtpEncapClientDisableAction_Type = InfnClientAction
_GbeClientCtpEncapClientDisableAction_Object = MibTableColumn
gbeClientCtpEncapClientDisableAction = _GbeClientCtpEncapClientDisableAction_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 223),
    _GbeClientCtpEncapClientDisableAction_Type()
)
gbeClientCtpEncapClientDisableAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpEncapClientDisableAction.setStatus("current")
_GbeClientCtpLLDPSnoopingEnable_Type = TruthValue
_GbeClientCtpLLDPSnoopingEnable_Object = MibTableColumn
gbeClientCtpLLDPSnoopingEnable = _GbeClientCtpLLDPSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 224),
    _GbeClientCtpLLDPSnoopingEnable_Type()
)
gbeClientCtpLLDPSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpLLDPSnoopingEnable.setStatus("current")
_GbeClientCtpFecMode_Type = TruthValue
_GbeClientCtpFecMode_Object = MibTableColumn
gbeClientCtpFecMode = _GbeClientCtpFecMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 225),
    _GbeClientCtpFecMode_Type()
)
gbeClientCtpFecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gbeClientCtpFecMode.setStatus("current")
_GbeClientCtpMaxMTUsize_Type = Integer32
_GbeClientCtpMaxMTUsize_Object = MibTableColumn
gbeClientCtpMaxMTUsize = _GbeClientCtpMaxMTUsize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 1, 1, 226),
    _GbeClientCtpMaxMTUsize_Type()
)
gbeClientCtpMaxMTUsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gbeClientCtpMaxMTUsize.setStatus("current")
_GbeClientCtpConformance_ObjectIdentity = ObjectIdentity
gbeClientCtpConformance = _GbeClientCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 3)
)
_GbeClientCtpCompliances_ObjectIdentity = ObjectIdentity
gbeClientCtpCompliances = _GbeClientCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 3, 1)
)
_GbeClientCtpGroups_ObjectIdentity = ObjectIdentity
gbeClientCtpGroups = _GbeClientCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 3, 2)
)

# Managed Objects groups

gbeClientCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 3, 2, 1)
)
gbeClientCtpGroup.setObjects(
      *(("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpSupportingCircuitIdList"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpLoopback"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpPmHistStatsEnable"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpConfiguredServiceType"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpConfiguredServiceType"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTribTestSigGenMode"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTribTestSigMonMode"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpLineTestSigGenMode"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpLineTestSigMonMode"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpMaxPacketLen"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxPcsICG15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxPcsES15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxPcsSES15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxPcsSESS15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxPcsICGDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxPcsESDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxPcsSESDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxPcsSESSDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacJS15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacSES15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacErrOctet15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacJabber15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacFragment15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacCrcAligned15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacUndersized15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacOversize15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize64P15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize65to127P15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize128to255P15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize256to511P15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize512to1023P15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize1024to1518P15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize1519toJumboP15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxPackets15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxOctets15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxBroadcastPkts15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMulticastPkts15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxInPauseFrames15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacJSDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacSESDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacErrOctetDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacJabberDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacFragmentDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacCrcAlignedDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacUndersizedDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacOversizeDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize64DayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize65to127DayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize128to255DayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize256to511DayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize512to1023DayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize1024to1518DayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize1519toJumboDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxPacketsDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxOctetsDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxBroadcastPktsDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMulticastPktsDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxInPauseFramesDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxPcsICG15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxPcsES15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxPcsSES15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxPcsSESS15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxPcsICGDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxPcsESDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxPcsSESDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxPcsSESSDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacJS15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacSES15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacErrOctet15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacJabber15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacFragment15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacCrcAligned15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacUndersized15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacOversize15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize64P15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize65to127P15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize128to255P15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize256to511P15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize512to1023P15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize1024to1518P15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize1519toJumboP15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxPackets15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxOctets15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxBroadcastPkts15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMulticastPkts15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxOutPauseFrames15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacJSDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacSESDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacErrOctetDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacJabberDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacFragmentDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacCrcAlignedDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacUndersizedDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacOversizeDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize64DayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize65to127DayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize128to255DayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize256to511DayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize512to1023DayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize1024to1518DayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize1519toJumboDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxPacketsDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxOctetsDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxBroadcastPktsDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMulticastPktsDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxOutPauseFramesDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxPcsICG15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxPcsES15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxPcsSES15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxPcsSESS15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxPcsICGDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxPcsESDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxPcsSESDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxPcsSESSDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacJS15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacSES15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacErrOctet15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacJabber15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacFragment15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacCrcAligned15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacUndersized15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacOversize15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize64P15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize65to127P15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize128to255P15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize256to511P15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize512to1023P15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize1024to1518P15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize1519toJumboP15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxPackets15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxOctets15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxBroadcastPkts15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMulticastPkts15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxInPauseFrames15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacJSDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacSESDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacErrOctetDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacJabberDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacFragmentDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacCrcAlignedDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacUndersizedDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMacOversizeDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize64DayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize65to127DayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize128to255DayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize256to511DayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize512to1023DayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize1024to1518DayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize1519toJumboDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxPacketsDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxOctetsDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxBroadcastPktsDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxMulticastPktsDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxInPauseFramesDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxPcsICG15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxPcsES15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxPcsSES15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxPcsSESS15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxPcsICGDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxPcsESDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxPcsSESDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxPcsSESSDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacJS15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacSES15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacErrOctet15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacJabber15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacFragment15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacCrcAligned15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacUndersized15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacOversize15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize64P15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize65to127P15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize128to255P15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize256to511P15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize512to1023P15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize1024to1518P15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize1519toJumboP15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxPackets15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxOctets15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxBroadcastPkts15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMulticastPkts15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxOutPauseFrames15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacJSDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacSESDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacErrOctetDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacJabberDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacFragmentDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacCrcAlignedDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacUndersizedDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMacOversizeDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize64DayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize65to127DayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize128to255DayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize256to511DayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize512to1023DayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize1024to1518DayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize1519toJumboDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxPacketsDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxOctetsDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxBroadcastPktsDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxMulticastPktsDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxOutPauseFramesDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize1024to1522P15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize1523toJumboP15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize1024to1522DayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize1523toJumboDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize1024to1522P15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize1523toJumboP15MinTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize1024to1522DayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize1523toJumboDayTce"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize1024to1522P15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize1523toJumboP15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize1024to1522DayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpRxSize1523toJumboDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize1024to1522P15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize1523toJumboP15MinTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize1024to1522DayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpTxSize1523toJumboDayTceRept"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpEncapTribDisableAction"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpServiceMode"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpServiceModeQualifier"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpHostAddress"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpHostControlTableSize"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpEncapClientDisableAction"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpLLDPSnoopingEnable"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpFecMode"),
        ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpMaxMTUsize"))
)
if mibBuilder.loadTexts:
    gbeClientCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

gbeClientCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 19, 3, 1, 1)
)
gbeClientCtpCompliance.setObjects(
    ("INFINERA-TP-GBECLIENTCTP-MIB", "gbeClientCtpGroup")
)
if mibBuilder.loadTexts:
    gbeClientCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-GBECLIENTCTP-MIB",
    **{"gbeClientCtpMIB": gbeClientCtpMIB,
       "gbeClientCtpTable": gbeClientCtpTable,
       "gbeClientCtpEntry": gbeClientCtpEntry,
       "gbeClientCtpSupportingCircuitIdList": gbeClientCtpSupportingCircuitIdList,
       "gbeClientCtpLoopback": gbeClientCtpLoopback,
       "gbeClientCtpPmHistStatsEnable": gbeClientCtpPmHistStatsEnable,
       "gbeClientCtpConfiguredServiceType": gbeClientCtpConfiguredServiceType,
       "gbeClientCtpTribTestSigGenMode": gbeClientCtpTribTestSigGenMode,
       "gbeClientCtpTribTestSigMonMode": gbeClientCtpTribTestSigMonMode,
       "gbeClientCtpLineTestSigGenMode": gbeClientCtpLineTestSigGenMode,
       "gbeClientCtpLineTestSigMonMode": gbeClientCtpLineTestSigMonMode,
       "gbeClientCtpMaxPacketLen": gbeClientCtpMaxPacketLen,
       "gbeClientCtpRxPcsICG15MinTce": gbeClientCtpRxPcsICG15MinTce,
       "gbeClientCtpRxPcsES15MinTce": gbeClientCtpRxPcsES15MinTce,
       "gbeClientCtpRxPcsSES15MinTce": gbeClientCtpRxPcsSES15MinTce,
       "gbeClientCtpRxPcsSESS15MinTce": gbeClientCtpRxPcsSESS15MinTce,
       "gbeClientCtpRxPcsICGDayTce": gbeClientCtpRxPcsICGDayTce,
       "gbeClientCtpRxPcsESDayTce": gbeClientCtpRxPcsESDayTce,
       "gbeClientCtpRxPcsSESDayTce": gbeClientCtpRxPcsSESDayTce,
       "gbeClientCtpRxPcsSESSDayTce": gbeClientCtpRxPcsSESSDayTce,
       "gbeClientCtpRxMacJS15MinTce": gbeClientCtpRxMacJS15MinTce,
       "gbeClientCtpRxMacSES15MinTce": gbeClientCtpRxMacSES15MinTce,
       "gbeClientCtpRxMacErrOctet15MinTce": gbeClientCtpRxMacErrOctet15MinTce,
       "gbeClientCtpRxMacJabber15MinTce": gbeClientCtpRxMacJabber15MinTce,
       "gbeClientCtpRxMacFragment15MinTce": gbeClientCtpRxMacFragment15MinTce,
       "gbeClientCtpRxMacCrcAligned15MinTce": gbeClientCtpRxMacCrcAligned15MinTce,
       "gbeClientCtpRxMacUndersized15MinTce": gbeClientCtpRxMacUndersized15MinTce,
       "gbeClientCtpRxMacOversize15MinTce": gbeClientCtpRxMacOversize15MinTce,
       "gbeClientCtpRxSize64P15MinTce": gbeClientCtpRxSize64P15MinTce,
       "gbeClientCtpRxSize65to127P15MinTce": gbeClientCtpRxSize65to127P15MinTce,
       "gbeClientCtpRxSize128to255P15MinTce": gbeClientCtpRxSize128to255P15MinTce,
       "gbeClientCtpRxSize256to511P15MinTce": gbeClientCtpRxSize256to511P15MinTce,
       "gbeClientCtpRxSize512to1023P15MinTce": gbeClientCtpRxSize512to1023P15MinTce,
       "gbeClientCtpRxSize1024to1518P15MinTce": gbeClientCtpRxSize1024to1518P15MinTce,
       "gbeClientCtpRxSize1519toJumboP15MinTce": gbeClientCtpRxSize1519toJumboP15MinTce,
       "gbeClientCtpRxPackets15MinTce": gbeClientCtpRxPackets15MinTce,
       "gbeClientCtpRxOctets15MinTce": gbeClientCtpRxOctets15MinTce,
       "gbeClientCtpRxBroadcastPkts15MinTce": gbeClientCtpRxBroadcastPkts15MinTce,
       "gbeClientCtpRxMulticastPkts15MinTce": gbeClientCtpRxMulticastPkts15MinTce,
       "gbeClientCtpRxInPauseFrames15MinTce": gbeClientCtpRxInPauseFrames15MinTce,
       "gbeClientCtpRxMacJSDayTce": gbeClientCtpRxMacJSDayTce,
       "gbeClientCtpRxMacSESDayTce": gbeClientCtpRxMacSESDayTce,
       "gbeClientCtpRxMacErrOctetDayTce": gbeClientCtpRxMacErrOctetDayTce,
       "gbeClientCtpRxMacJabberDayTce": gbeClientCtpRxMacJabberDayTce,
       "gbeClientCtpRxMacFragmentDayTce": gbeClientCtpRxMacFragmentDayTce,
       "gbeClientCtpRxMacCrcAlignedDayTce": gbeClientCtpRxMacCrcAlignedDayTce,
       "gbeClientCtpRxMacUndersizedDayTce": gbeClientCtpRxMacUndersizedDayTce,
       "gbeClientCtpRxMacOversizeDayTce": gbeClientCtpRxMacOversizeDayTce,
       "gbeClientCtpRxSize64DayTce": gbeClientCtpRxSize64DayTce,
       "gbeClientCtpRxSize65to127DayTce": gbeClientCtpRxSize65to127DayTce,
       "gbeClientCtpRxSize128to255DayTce": gbeClientCtpRxSize128to255DayTce,
       "gbeClientCtpRxSize256to511DayTce": gbeClientCtpRxSize256to511DayTce,
       "gbeClientCtpRxSize512to1023DayTce": gbeClientCtpRxSize512to1023DayTce,
       "gbeClientCtpRxSize1024to1518DayTce": gbeClientCtpRxSize1024to1518DayTce,
       "gbeClientCtpRxSize1519toJumboDayTce": gbeClientCtpRxSize1519toJumboDayTce,
       "gbeClientCtpRxPacketsDayTce": gbeClientCtpRxPacketsDayTce,
       "gbeClientCtpRxOctetsDayTce": gbeClientCtpRxOctetsDayTce,
       "gbeClientCtpRxBroadcastPktsDayTce": gbeClientCtpRxBroadcastPktsDayTce,
       "gbeClientCtpRxMulticastPktsDayTce": gbeClientCtpRxMulticastPktsDayTce,
       "gbeClientCtpRxInPauseFramesDayTce": gbeClientCtpRxInPauseFramesDayTce,
       "gbeClientCtpTxPcsICG15MinTce": gbeClientCtpTxPcsICG15MinTce,
       "gbeClientCtpTxPcsES15MinTce": gbeClientCtpTxPcsES15MinTce,
       "gbeClientCtpTxPcsSES15MinTce": gbeClientCtpTxPcsSES15MinTce,
       "gbeClientCtpTxPcsSESS15MinTce": gbeClientCtpTxPcsSESS15MinTce,
       "gbeClientCtpTxPcsICGDayTce": gbeClientCtpTxPcsICGDayTce,
       "gbeClientCtpTxPcsESDayTce": gbeClientCtpTxPcsESDayTce,
       "gbeClientCtpTxPcsSESDayTce": gbeClientCtpTxPcsSESDayTce,
       "gbeClientCtpTxPcsSESSDayTce": gbeClientCtpTxPcsSESSDayTce,
       "gbeClientCtpTxMacJS15MinTce": gbeClientCtpTxMacJS15MinTce,
       "gbeClientCtpTxMacSES15MinTce": gbeClientCtpTxMacSES15MinTce,
       "gbeClientCtpTxMacErrOctet15MinTce": gbeClientCtpTxMacErrOctet15MinTce,
       "gbeClientCtpTxMacJabber15MinTce": gbeClientCtpTxMacJabber15MinTce,
       "gbeClientCtpTxMacFragment15MinTce": gbeClientCtpTxMacFragment15MinTce,
       "gbeClientCtpTxMacCrcAligned15MinTce": gbeClientCtpTxMacCrcAligned15MinTce,
       "gbeClientCtpTxMacUndersized15MinTce": gbeClientCtpTxMacUndersized15MinTce,
       "gbeClientCtpTxMacOversize15MinTce": gbeClientCtpTxMacOversize15MinTce,
       "gbeClientCtpTxSize64P15MinTce": gbeClientCtpTxSize64P15MinTce,
       "gbeClientCtpTxSize65to127P15MinTce": gbeClientCtpTxSize65to127P15MinTce,
       "gbeClientCtpTxSize128to255P15MinTce": gbeClientCtpTxSize128to255P15MinTce,
       "gbeClientCtpTxSize256to511P15MinTce": gbeClientCtpTxSize256to511P15MinTce,
       "gbeClientCtpTxSize512to1023P15MinTce": gbeClientCtpTxSize512to1023P15MinTce,
       "gbeClientCtpTxSize1024to1518P15MinTce": gbeClientCtpTxSize1024to1518P15MinTce,
       "gbeClientCtpTxSize1519toJumboP15MinTce": gbeClientCtpTxSize1519toJumboP15MinTce,
       "gbeClientCtpTxPackets15MinTce": gbeClientCtpTxPackets15MinTce,
       "gbeClientCtpTxOctets15MinTce": gbeClientCtpTxOctets15MinTce,
       "gbeClientCtpTxBroadcastPkts15MinTce": gbeClientCtpTxBroadcastPkts15MinTce,
       "gbeClientCtpTxMulticastPkts15MinTce": gbeClientCtpTxMulticastPkts15MinTce,
       "gbeClientCtpTxOutPauseFrames15MinTce": gbeClientCtpTxOutPauseFrames15MinTce,
       "gbeClientCtpTxMacJSDayTce": gbeClientCtpTxMacJSDayTce,
       "gbeClientCtpTxMacSESDayTce": gbeClientCtpTxMacSESDayTce,
       "gbeClientCtpTxMacErrOctetDayTce": gbeClientCtpTxMacErrOctetDayTce,
       "gbeClientCtpTxMacJabberDayTce": gbeClientCtpTxMacJabberDayTce,
       "gbeClientCtpTxMacFragmentDayTce": gbeClientCtpTxMacFragmentDayTce,
       "gbeClientCtpTxMacCrcAlignedDayTce": gbeClientCtpTxMacCrcAlignedDayTce,
       "gbeClientCtpTxMacUndersizedDayTce": gbeClientCtpTxMacUndersizedDayTce,
       "gbeClientCtpTxMacOversizeDayTce": gbeClientCtpTxMacOversizeDayTce,
       "gbeClientCtpTxSize64DayTce": gbeClientCtpTxSize64DayTce,
       "gbeClientCtpTxSize65to127DayTce": gbeClientCtpTxSize65to127DayTce,
       "gbeClientCtpTxSize128to255DayTce": gbeClientCtpTxSize128to255DayTce,
       "gbeClientCtpTxSize256to511DayTce": gbeClientCtpTxSize256to511DayTce,
       "gbeClientCtpTxSize512to1023DayTce": gbeClientCtpTxSize512to1023DayTce,
       "gbeClientCtpTxSize1024to1518DayTce": gbeClientCtpTxSize1024to1518DayTce,
       "gbeClientCtpTxSize1519toJumboDayTce": gbeClientCtpTxSize1519toJumboDayTce,
       "gbeClientCtpTxPacketsDayTce": gbeClientCtpTxPacketsDayTce,
       "gbeClientCtpTxOctetsDayTce": gbeClientCtpTxOctetsDayTce,
       "gbeClientCtpTxBroadcastPktsDayTce": gbeClientCtpTxBroadcastPktsDayTce,
       "gbeClientCtpTxMulticastPktsDayTce": gbeClientCtpTxMulticastPktsDayTce,
       "gbeClientCtpTxOutPauseFramesDayTce": gbeClientCtpTxOutPauseFramesDayTce,
       "gbeClientCtpRxPcsICG15MinTceRept": gbeClientCtpRxPcsICG15MinTceRept,
       "gbeClientCtpRxPcsES15MinTceRept": gbeClientCtpRxPcsES15MinTceRept,
       "gbeClientCtpRxPcsSES15MinTceRept": gbeClientCtpRxPcsSES15MinTceRept,
       "gbeClientCtpRxPcsSESS15MinTceRept": gbeClientCtpRxPcsSESS15MinTceRept,
       "gbeClientCtpRxPcsICGDayTceRept": gbeClientCtpRxPcsICGDayTceRept,
       "gbeClientCtpRxPcsESDayTceRept": gbeClientCtpRxPcsESDayTceRept,
       "gbeClientCtpRxPcsSESDayTceRept": gbeClientCtpRxPcsSESDayTceRept,
       "gbeClientCtpRxPcsSESSDayTceRept": gbeClientCtpRxPcsSESSDayTceRept,
       "gbeClientCtpRxMacJS15MinTceRept": gbeClientCtpRxMacJS15MinTceRept,
       "gbeClientCtpRxMacSES15MinTceRept": gbeClientCtpRxMacSES15MinTceRept,
       "gbeClientCtpRxMacErrOctet15MinTceRept": gbeClientCtpRxMacErrOctet15MinTceRept,
       "gbeClientCtpRxMacJabber15MinTceRept": gbeClientCtpRxMacJabber15MinTceRept,
       "gbeClientCtpRxMacFragment15MinTceRept": gbeClientCtpRxMacFragment15MinTceRept,
       "gbeClientCtpRxMacCrcAligned15MinTceRept": gbeClientCtpRxMacCrcAligned15MinTceRept,
       "gbeClientCtpRxMacUndersized15MinTceRept": gbeClientCtpRxMacUndersized15MinTceRept,
       "gbeClientCtpRxMacOversize15MinTceRept": gbeClientCtpRxMacOversize15MinTceRept,
       "gbeClientCtpRxSize64P15MinTceRept": gbeClientCtpRxSize64P15MinTceRept,
       "gbeClientCtpRxSize65to127P15MinTceRept": gbeClientCtpRxSize65to127P15MinTceRept,
       "gbeClientCtpRxSize128to255P15MinTceRept": gbeClientCtpRxSize128to255P15MinTceRept,
       "gbeClientCtpRxSize256to511P15MinTceRept": gbeClientCtpRxSize256to511P15MinTceRept,
       "gbeClientCtpRxSize512to1023P15MinTceRept": gbeClientCtpRxSize512to1023P15MinTceRept,
       "gbeClientCtpRxSize1024to1518P15MinTceRept": gbeClientCtpRxSize1024to1518P15MinTceRept,
       "gbeClientCtpRxSize1519toJumboP15MinTceRept": gbeClientCtpRxSize1519toJumboP15MinTceRept,
       "gbeClientCtpRxPackets15MinTceRept": gbeClientCtpRxPackets15MinTceRept,
       "gbeClientCtpRxOctets15MinTceRept": gbeClientCtpRxOctets15MinTceRept,
       "gbeClientCtpRxBroadcastPkts15MinTceRept": gbeClientCtpRxBroadcastPkts15MinTceRept,
       "gbeClientCtpRxMulticastPkts15MinTceRept": gbeClientCtpRxMulticastPkts15MinTceRept,
       "gbeClientCtpRxInPauseFrames15MinTceRept": gbeClientCtpRxInPauseFrames15MinTceRept,
       "gbeClientCtpRxMacJSDayTceRept": gbeClientCtpRxMacJSDayTceRept,
       "gbeClientCtpRxMacSESDayTceRept": gbeClientCtpRxMacSESDayTceRept,
       "gbeClientCtpRxMacErrOctetDayTceRept": gbeClientCtpRxMacErrOctetDayTceRept,
       "gbeClientCtpRxMacJabberDayTceRept": gbeClientCtpRxMacJabberDayTceRept,
       "gbeClientCtpRxMacFragmentDayTceRept": gbeClientCtpRxMacFragmentDayTceRept,
       "gbeClientCtpRxMacCrcAlignedDayTceRept": gbeClientCtpRxMacCrcAlignedDayTceRept,
       "gbeClientCtpRxMacUndersizedDayTceRept": gbeClientCtpRxMacUndersizedDayTceRept,
       "gbeClientCtpRxMacOversizeDayTceRept": gbeClientCtpRxMacOversizeDayTceRept,
       "gbeClientCtpRxSize64DayTceRept": gbeClientCtpRxSize64DayTceRept,
       "gbeClientCtpRxSize65to127DayTceRept": gbeClientCtpRxSize65to127DayTceRept,
       "gbeClientCtpRxSize128to255DayTceRept": gbeClientCtpRxSize128to255DayTceRept,
       "gbeClientCtpRxSize256to511DayTceRept": gbeClientCtpRxSize256to511DayTceRept,
       "gbeClientCtpRxSize512to1023DayTceRept": gbeClientCtpRxSize512to1023DayTceRept,
       "gbeClientCtpRxSize1024to1518DayTceRept": gbeClientCtpRxSize1024to1518DayTceRept,
       "gbeClientCtpRxSize1519toJumboDayTceRept": gbeClientCtpRxSize1519toJumboDayTceRept,
       "gbeClientCtpRxPacketsDayTceRept": gbeClientCtpRxPacketsDayTceRept,
       "gbeClientCtpRxOctetsDayTceRept": gbeClientCtpRxOctetsDayTceRept,
       "gbeClientCtpRxBroadcastPktsDayTceRept": gbeClientCtpRxBroadcastPktsDayTceRept,
       "gbeClientCtpRxMulticastPktsDayTceRept": gbeClientCtpRxMulticastPktsDayTceRept,
       "gbeClientCtpRxInPauseFramesDayTceRept": gbeClientCtpRxInPauseFramesDayTceRept,
       "gbeClientCtpTxPcsICG15MinTceRept": gbeClientCtpTxPcsICG15MinTceRept,
       "gbeClientCtpTxPcsES15MinTceRept": gbeClientCtpTxPcsES15MinTceRept,
       "gbeClientCtpTxPcsSES15MinTceRept": gbeClientCtpTxPcsSES15MinTceRept,
       "gbeClientCtpTxPcsSESS15MinTceRept": gbeClientCtpTxPcsSESS15MinTceRept,
       "gbeClientCtpTxPcsICGDayTceRept": gbeClientCtpTxPcsICGDayTceRept,
       "gbeClientCtpTxPcsESDayTceRept": gbeClientCtpTxPcsESDayTceRept,
       "gbeClientCtpTxPcsSESDayTceRept": gbeClientCtpTxPcsSESDayTceRept,
       "gbeClientCtpTxPcsSESSDayTceRept": gbeClientCtpTxPcsSESSDayTceRept,
       "gbeClientCtpTxMacJS15MinTceRept": gbeClientCtpTxMacJS15MinTceRept,
       "gbeClientCtpTxMacSES15MinTceRept": gbeClientCtpTxMacSES15MinTceRept,
       "gbeClientCtpTxMacErrOctet15MinTceRept": gbeClientCtpTxMacErrOctet15MinTceRept,
       "gbeClientCtpTxMacJabber15MinTceRept": gbeClientCtpTxMacJabber15MinTceRept,
       "gbeClientCtpTxMacFragment15MinTceRept": gbeClientCtpTxMacFragment15MinTceRept,
       "gbeClientCtpTxMacCrcAligned15MinTceRept": gbeClientCtpTxMacCrcAligned15MinTceRept,
       "gbeClientCtpTxMacUndersized15MinTceRept": gbeClientCtpTxMacUndersized15MinTceRept,
       "gbeClientCtpTxMacOversize15MinTceRept": gbeClientCtpTxMacOversize15MinTceRept,
       "gbeClientCtpTxSize64P15MinTceRept": gbeClientCtpTxSize64P15MinTceRept,
       "gbeClientCtpTxSize65to127P15MinTceRept": gbeClientCtpTxSize65to127P15MinTceRept,
       "gbeClientCtpTxSize128to255P15MinTceRept": gbeClientCtpTxSize128to255P15MinTceRept,
       "gbeClientCtpTxSize256to511P15MinTceRept": gbeClientCtpTxSize256to511P15MinTceRept,
       "gbeClientCtpTxSize512to1023P15MinTceRept": gbeClientCtpTxSize512to1023P15MinTceRept,
       "gbeClientCtpTxSize1024to1518P15MinTceRept": gbeClientCtpTxSize1024to1518P15MinTceRept,
       "gbeClientCtpTxSize1519toJumboP15MinTceRept": gbeClientCtpTxSize1519toJumboP15MinTceRept,
       "gbeClientCtpTxPackets15MinTceRept": gbeClientCtpTxPackets15MinTceRept,
       "gbeClientCtpTxOctets15MinTceRept": gbeClientCtpTxOctets15MinTceRept,
       "gbeClientCtpTxBroadcastPkts15MinTceRept": gbeClientCtpTxBroadcastPkts15MinTceRept,
       "gbeClientCtpTxMulticastPkts15MinTceRept": gbeClientCtpTxMulticastPkts15MinTceRept,
       "gbeClientCtpTxOutPauseFrames15MinTceRept": gbeClientCtpTxOutPauseFrames15MinTceRept,
       "gbeClientCtpTxMacJSDayTceRept": gbeClientCtpTxMacJSDayTceRept,
       "gbeClientCtpTxMacSESDayTceRept": gbeClientCtpTxMacSESDayTceRept,
       "gbeClientCtpTxMacErrOctetDayTceRept": gbeClientCtpTxMacErrOctetDayTceRept,
       "gbeClientCtpTxMacJabberDayTceRept": gbeClientCtpTxMacJabberDayTceRept,
       "gbeClientCtpTxMacFragmentDayTceRept": gbeClientCtpTxMacFragmentDayTceRept,
       "gbeClientCtpTxMacCrcAlignedDayTceRept": gbeClientCtpTxMacCrcAlignedDayTceRept,
       "gbeClientCtpTxMacUndersizedDayTceRept": gbeClientCtpTxMacUndersizedDayTceRept,
       "gbeClientCtpTxMacOversizeDayTceRept": gbeClientCtpTxMacOversizeDayTceRept,
       "gbeClientCtpTxSize64DayTceRept": gbeClientCtpTxSize64DayTceRept,
       "gbeClientCtpTxSize65to127DayTceRept": gbeClientCtpTxSize65to127DayTceRept,
       "gbeClientCtpTxSize128to255DayTceRept": gbeClientCtpTxSize128to255DayTceRept,
       "gbeClientCtpTxSize256to511DayTceRept": gbeClientCtpTxSize256to511DayTceRept,
       "gbeClientCtpTxSize512to1023DayTceRept": gbeClientCtpTxSize512to1023DayTceRept,
       "gbeClientCtpTxSize1024to1518DayTceRept": gbeClientCtpTxSize1024to1518DayTceRept,
       "gbeClientCtpTxSize1519toJumboDayTceRept": gbeClientCtpTxSize1519toJumboDayTceRept,
       "gbeClientCtpTxPacketsDayTceRept": gbeClientCtpTxPacketsDayTceRept,
       "gbeClientCtpTxOctetsDayTceRept": gbeClientCtpTxOctetsDayTceRept,
       "gbeClientCtpTxBroadcastPktsDayTceRept": gbeClientCtpTxBroadcastPktsDayTceRept,
       "gbeClientCtpTxMulticastPktsDayTceRept": gbeClientCtpTxMulticastPktsDayTceRept,
       "gbeClientCtpTxOutPauseFramesDayTceRept": gbeClientCtpTxOutPauseFramesDayTceRept,
       "gbeClientCtpRxSize1024to1522P15MinTce": gbeClientCtpRxSize1024to1522P15MinTce,
       "gbeClientCtpRxSize1523toJumboP15MinTce": gbeClientCtpRxSize1523toJumboP15MinTce,
       "gbeClientCtpRxSize1024to1522DayTce": gbeClientCtpRxSize1024to1522DayTce,
       "gbeClientCtpRxSize1523toJumboDayTce": gbeClientCtpRxSize1523toJumboDayTce,
       "gbeClientCtpTxSize1024to1522P15MinTce": gbeClientCtpTxSize1024to1522P15MinTce,
       "gbeClientCtpTxSize1523toJumboP15MinTce": gbeClientCtpTxSize1523toJumboP15MinTce,
       "gbeClientCtpTxSize1024to1522DayTce": gbeClientCtpTxSize1024to1522DayTce,
       "gbeClientCtpTxSize1523toJumboDayTce": gbeClientCtpTxSize1523toJumboDayTce,
       "gbeClientCtpRxSize1024to1522P15MinTceRept": gbeClientCtpRxSize1024to1522P15MinTceRept,
       "gbeClientCtpRxSize1523toJumboP15MinTceRept": gbeClientCtpRxSize1523toJumboP15MinTceRept,
       "gbeClientCtpRxSize1024to1522DayTceRept": gbeClientCtpRxSize1024to1522DayTceRept,
       "gbeClientCtpRxSize1523toJumboDayTceRept": gbeClientCtpRxSize1523toJumboDayTceRept,
       "gbeClientCtpTxSize1024to1522P15MinTceRept": gbeClientCtpTxSize1024to1522P15MinTceRept,
       "gbeClientCtpTxSize1523toJumboP15MinTceRept": gbeClientCtpTxSize1523toJumboP15MinTceRept,
       "gbeClientCtpTxSize1024to1522DayTceRept": gbeClientCtpTxSize1024to1522DayTceRept,
       "gbeClientCtpTxSize1523toJumboDayTceRept": gbeClientCtpTxSize1523toJumboDayTceRept,
       "gbeClientCtpEncapTribDisableAction": gbeClientCtpEncapTribDisableAction,
       "gbeClientCtpServiceMode": gbeClientCtpServiceMode,
       "gbeClientCtpServiceModeQualifier": gbeClientCtpServiceModeQualifier,
       "gbeClientCtpHostAddress": gbeClientCtpHostAddress,
       "gbeClientCtpHostControlTableSize": gbeClientCtpHostControlTableSize,
       "gbeClientCtpEncapClientDisableAction": gbeClientCtpEncapClientDisableAction,
       "gbeClientCtpLLDPSnoopingEnable": gbeClientCtpLLDPSnoopingEnable,
       "gbeClientCtpFecMode": gbeClientCtpFecMode,
       "gbeClientCtpMaxMTUsize": gbeClientCtpMaxMTUsize,
       "gbeClientCtpConformance": gbeClientCtpConformance,
       "gbeClientCtpCompliances": gbeClientCtpCompliances,
       "gbeClientCtpCompliance": gbeClientCtpCompliance,
       "gbeClientCtpGroups": gbeClientCtpGroups,
       "gbeClientCtpGroup": gbeClientCtpGroup}
)
