# SNMP MIB module (RAISECOM-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-RELAY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:26 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")

(rcPortIndex,) = mibBuilder.importSymbols(
    "SWITCH-SYSTEM-MIB",
    "rcPortIndex")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rcRelay = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 35)
)
if mibBuilder.loadTexts:
    rcRelay.setRevisions(
        ("2008-03-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcRelayGrobal_ObjectIdentity = ObjectIdentity
rcRelayGrobal = _RcRelayGrobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 35, 1)
)
_RcRelayMacAddress_Type = MacAddress
_RcRelayMacAddress_Object = MibScalar
rcRelayMacAddress = _RcRelayMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 35, 1, 1),
    _RcRelayMacAddress_Type()
)
rcRelayMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRelayMacAddress.setStatus("current")


class _RcRelayCos_Type(Unsigned32):
    """Custom type rcRelayCos based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_RcRelayCos_Type.__name__ = "Unsigned32"
_RcRelayCos_Object = MibScalar
rcRelayCos = _RcRelayCos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 35, 1, 2),
    _RcRelayCos_Type()
)
rcRelayCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRelayCos.setStatus("current")
_RcRelayTransparentEnable_Type = EnableVar
_RcRelayTransparentEnable_Object = MibScalar
rcRelayTransparentEnable = _RcRelayTransparentEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 35, 1, 3),
    _RcRelayTransparentEnable_Type()
)
rcRelayTransparentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRelayTransparentEnable.setStatus("current")
_RcRelayProtocolTable_Object = MibTable
rcRelayProtocolTable = _RcRelayProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 35, 2)
)
if mibBuilder.loadTexts:
    rcRelayProtocolTable.setStatus("current")
_RcRelayProtocolEntry_Object = MibTableRow
rcRelayProtocolEntry = _RcRelayProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 35, 2, 1)
)
rcRelayProtocolEntry.setIndexNames(
    (0, "SWITCH-SYSTEM-MIB", "rcPortIndex"),
)
if mibBuilder.loadTexts:
    rcRelayProtocolEntry.setStatus("current")


class _RcRelayProtocolType_Type(Bits):
    """Custom type rcRelayProtocolType based on Bits"""
    namedValues = NamedValues(
        *(("stp", 0),
          ("dot1x", 1),
          ("lacp", 2),
          ("gmrp", 3),
          ("gvrp", 4),
          ("cdp", 5),
          ("vtp", 6),
          ("pvst", 7),
          ("udld", 8),
          ("pagp", 9))
    )

_RcRelayProtocolType_Type.__name__ = "Bits"
_RcRelayProtocolType_Object = MibTableColumn
rcRelayProtocolType = _RcRelayProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 35, 2, 1, 1),
    _RcRelayProtocolType_Type()
)
rcRelayProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRelayProtocolType.setStatus("current")
_RcRelayProtocolVlan_Type = Unsigned32
_RcRelayProtocolVlan_Object = MibTableColumn
rcRelayProtocolVlan = _RcRelayProtocolVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 35, 2, 1, 2),
    _RcRelayProtocolVlan_Type()
)
rcRelayProtocolVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRelayProtocolVlan.setStatus("current")
_RcRelayProtocolEgressPort_Type = Unsigned32
_RcRelayProtocolEgressPort_Object = MibTableColumn
rcRelayProtocolEgressPort = _RcRelayProtocolEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 35, 2, 1, 3),
    _RcRelayProtocolEgressPort_Type()
)
rcRelayProtocolEgressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRelayProtocolEgressPort.setStatus("current")


class _RcRelayProtocolPortStatus_Type(Integer32):
    """Custom type rcRelayProtocolPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_RcRelayProtocolPortStatus_Type.__name__ = "Integer32"
_RcRelayProtocolPortStatus_Object = MibTableColumn
rcRelayProtocolPortStatus = _RcRelayProtocolPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 35, 2, 1, 4),
    _RcRelayProtocolPortStatus_Type()
)
rcRelayProtocolPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRelayProtocolPortStatus.setStatus("current")
_RcRelayThresholdTable_Object = MibTable
rcRelayThresholdTable = _RcRelayThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 35, 3)
)
if mibBuilder.loadTexts:
    rcRelayThresholdTable.setStatus("current")
_RcRelayThresholdEntry_Object = MibTableRow
rcRelayThresholdEntry = _RcRelayThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 35, 3, 1)
)
rcRelayThresholdEntry.setIndexNames(
    (0, "SWITCH-SYSTEM-MIB", "rcPortIndex"),
    (0, "RAISECOM-RELAY-MIB", "rcRelayThresholdProtocolIndex"),
)
if mibBuilder.loadTexts:
    rcRelayThresholdEntry.setStatus("current")


class _RcRelayThresholdProtocolIndex_Type(Integer32):
    """Custom type rcRelayThresholdProtocolIndex based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("stp", 1),
          ("dot1x", 2),
          ("lacp", 3),
          ("gmrp", 4),
          ("gvrp", 5),
          ("cdp", 6),
          ("vtp", 7),
          ("pvst", 8),
          ("udld", 9),
          ("pagp", 10))
    )


_RcRelayThresholdProtocolIndex_Type.__name__ = "Integer32"
_RcRelayThresholdProtocolIndex_Object = MibTableColumn
rcRelayThresholdProtocolIndex = _RcRelayThresholdProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 35, 3, 1, 1),
    _RcRelayThresholdProtocolIndex_Type()
)
rcRelayThresholdProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcRelayThresholdProtocolIndex.setStatus("current")


class _RcRelayDropThreshold_Type(Unsigned32):
    """Custom type rcRelayDropThreshold based on Unsigned32"""
    defaultValue = 0


_RcRelayDropThreshold_Type.__name__ = "Unsigned32"
_RcRelayDropThreshold_Object = MibTableColumn
rcRelayDropThreshold = _RcRelayDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 35, 3, 1, 2),
    _RcRelayDropThreshold_Type()
)
rcRelayDropThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRelayDropThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rcRelayDropThreshold.setUnits("PDUs/sec")


class _RcRelayShutdownThreshold_Type(Unsigned32):
    """Custom type rcRelayShutdownThreshold based on Unsigned32"""
    defaultValue = 0


_RcRelayShutdownThreshold_Type.__name__ = "Unsigned32"
_RcRelayShutdownThreshold_Object = MibTableColumn
rcRelayShutdownThreshold = _RcRelayShutdownThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 35, 3, 1, 3),
    _RcRelayShutdownThreshold_Type()
)
rcRelayShutdownThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRelayShutdownThreshold.setStatus("current")
if mibBuilder.loadTexts:
    rcRelayShutdownThreshold.setUnits("PDUs/sec")
_RcRelayStatisticsTable_Object = MibTable
rcRelayStatisticsTable = _RcRelayStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 35, 4)
)
if mibBuilder.loadTexts:
    rcRelayStatisticsTable.setStatus("current")
_RcRelayStatisticsEntry_Object = MibTableRow
rcRelayStatisticsEntry = _RcRelayStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 35, 4, 1)
)
rcRelayStatisticsEntry.setIndexNames(
    (0, "SWITCH-SYSTEM-MIB", "rcPortIndex"),
    (0, "RAISECOM-RELAY-MIB", "rcRelayStatsProtocolIndex"),
)
if mibBuilder.loadTexts:
    rcRelayStatisticsEntry.setStatus("current")


class _RcRelayStatsProtocolIndex_Type(Integer32):
    """Custom type rcRelayStatsProtocolIndex based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("stp", 1),
          ("dot1x", 2),
          ("lacp", 3),
          ("gmrp", 4),
          ("gvrp", 5),
          ("cdp", 6),
          ("vtp", 7),
          ("pvst", 8),
          ("udld", 9),
          ("pagp", 10))
    )


_RcRelayStatsProtocolIndex_Type.__name__ = "Integer32"
_RcRelayStatsProtocolIndex_Object = MibTableColumn
rcRelayStatsProtocolIndex = _RcRelayStatsProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 35, 4, 1, 1),
    _RcRelayStatsProtocolIndex_Type()
)
rcRelayStatsProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcRelayStatsProtocolIndex.setStatus("current")
_RcRelayEncapStats_Type = Counter32
_RcRelayEncapStats_Object = MibTableColumn
rcRelayEncapStats = _RcRelayEncapStats_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 35, 4, 1, 2),
    _RcRelayEncapStats_Type()
)
rcRelayEncapStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRelayEncapStats.setStatus("current")
if mibBuilder.loadTexts:
    rcRelayEncapStats.setUnits("encapsulated PDUs")
_RcRelayDeEncapStats_Type = Counter32
_RcRelayDeEncapStats_Object = MibTableColumn
rcRelayDeEncapStats = _RcRelayDeEncapStats_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 35, 4, 1, 3),
    _RcRelayDeEncapStats_Type()
)
rcRelayDeEncapStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRelayDeEncapStats.setStatus("current")
if mibBuilder.loadTexts:
    rcRelayDeEncapStats.setUnits("de-encapsulated PDUs")
_RcRelayDropStats_Type = Counter32
_RcRelayDropStats_Object = MibTableColumn
rcRelayDropStats = _RcRelayDropStats_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 35, 4, 1, 4),
    _RcRelayDropStats_Type()
)
rcRelayDropStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRelayDropStats.setStatus("current")
if mibBuilder.loadTexts:
    rcRelayDropStats.setUnits("PDUs")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-RELAY-MIB",
    **{"rcRelay": rcRelay,
       "rcRelayGrobal": rcRelayGrobal,
       "rcRelayMacAddress": rcRelayMacAddress,
       "rcRelayCos": rcRelayCos,
       "rcRelayTransparentEnable": rcRelayTransparentEnable,
       "rcRelayProtocolTable": rcRelayProtocolTable,
       "rcRelayProtocolEntry": rcRelayProtocolEntry,
       "rcRelayProtocolType": rcRelayProtocolType,
       "rcRelayProtocolVlan": rcRelayProtocolVlan,
       "rcRelayProtocolEgressPort": rcRelayProtocolEgressPort,
       "rcRelayProtocolPortStatus": rcRelayProtocolPortStatus,
       "rcRelayThresholdTable": rcRelayThresholdTable,
       "rcRelayThresholdEntry": rcRelayThresholdEntry,
       "rcRelayThresholdProtocolIndex": rcRelayThresholdProtocolIndex,
       "rcRelayDropThreshold": rcRelayDropThreshold,
       "rcRelayShutdownThreshold": rcRelayShutdownThreshold,
       "rcRelayStatisticsTable": rcRelayStatisticsTable,
       "rcRelayStatisticsEntry": rcRelayStatisticsEntry,
       "rcRelayStatsProtocolIndex": rcRelayStatsProtocolIndex,
       "rcRelayEncapStats": rcRelayEncapStats,
       "rcRelayDeEncapStats": rcRelayDeEncapStats,
       "rcRelayDropStats": rcRelayDropStats}
)
