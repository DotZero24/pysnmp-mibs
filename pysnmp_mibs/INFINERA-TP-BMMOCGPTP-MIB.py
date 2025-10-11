# SNMP MIB module (INFINERA-TP-BMMOCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-BMMOCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:28 2025
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

(FloatTenths,
 InfnOcgChannelMap,
 InfnOcgPortConfig,
 InfnPmHistStatsControl,
 InfnPowerControlLoop,
 InfnShutterState,
 InfnSignalType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnOcgChannelMap",
    "InfnOcgPortConfig",
    "InfnPmHistStatsControl",
    "InfnPowerControlLoop",
    "InfnShutterState",
    "InfnSignalType")

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

bmmOcgPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3)
)
if mibBuilder.loadTexts:
    bmmOcgPtpMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BmmOcgPtpTable_Object = MibTable
bmmOcgPtpTable = _BmmOcgPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    bmmOcgPtpTable.setStatus("current")
_BmmOcgPtpEntry_Object = MibTableRow
bmmOcgPtpEntry = _BmmOcgPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3, 1, 1)
)
bmmOcgPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bmmOcgPtpEntry.setStatus("current")
_BmmOcgPtpDiscoveredOcgTP_Type = DisplayString
_BmmOcgPtpDiscoveredOcgTP_Object = MibTableColumn
bmmOcgPtpDiscoveredOcgTP = _BmmOcgPtpDiscoveredOcgTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3, 1, 1, 1),
    _BmmOcgPtpDiscoveredOcgTP_Type()
)
bmmOcgPtpDiscoveredOcgTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmOcgPtpDiscoveredOcgTP.setStatus("current")
_BmmOcgPtpProvisionedOcgTP_Type = DisplayString
_BmmOcgPtpProvisionedOcgTP_Object = MibTableColumn
bmmOcgPtpProvisionedOcgTP = _BmmOcgPtpProvisionedOcgTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3, 1, 1, 2),
    _BmmOcgPtpProvisionedOcgTP_Type()
)
bmmOcgPtpProvisionedOcgTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmmOcgPtpProvisionedOcgTP.setStatus("current")


class _BmmOcgPtpOcgNumber_Type(Integer32):
    """Custom type bmmOcgPtpOcgNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BmmOcgPtpOcgNumber_Type.__name__ = "Integer32"
_BmmOcgPtpOcgNumber_Object = MibTableColumn
bmmOcgPtpOcgNumber = _BmmOcgPtpOcgNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3, 1, 1, 3),
    _BmmOcgPtpOcgNumber_Type()
)
bmmOcgPtpOcgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmOcgPtpOcgNumber.setStatus("current")


class _BmmOcgPtpOcgPowerControlLoop_Type(InfnPowerControlLoop):
    """Custom type bmmOcgPtpOcgPowerControlLoop based on InfnPowerControlLoop"""
    defaultValue = 2


_BmmOcgPtpOcgPowerControlLoop_Type.__name__ = "InfnPowerControlLoop"
_BmmOcgPtpOcgPowerControlLoop_Object = MibTableColumn
bmmOcgPtpOcgPowerControlLoop = _BmmOcgPtpOcgPowerControlLoop_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3, 1, 1, 4),
    _BmmOcgPtpOcgPowerControlLoop_Type()
)
bmmOcgPtpOcgPowerControlLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmmOcgPtpOcgPowerControlLoop.setStatus("current")


class _BmmOcgPtpTargetRxOcgPower_Type(FloatTenths):
    """Custom type bmmOcgPtpTargetRxOcgPower based on FloatTenths"""
    defaultValue = 0


_BmmOcgPtpTargetRxOcgPower_Type.__name__ = "FloatTenths"
_BmmOcgPtpTargetRxOcgPower_Object = MibTableColumn
bmmOcgPtpTargetRxOcgPower = _BmmOcgPtpTargetRxOcgPower_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3, 1, 1, 5),
    _BmmOcgPtpTargetRxOcgPower_Type()
)
bmmOcgPtpTargetRxOcgPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmOcgPtpTargetRxOcgPower.setStatus("current")


class _BmmOcgPtpMuxInsertionLoss_Type(FloatTenths):
    """Custom type bmmOcgPtpMuxInsertionLoss based on FloatTenths"""
    defaultValue = 0


_BmmOcgPtpMuxInsertionLoss_Type.__name__ = "FloatTenths"
_BmmOcgPtpMuxInsertionLoss_Object = MibTableColumn
bmmOcgPtpMuxInsertionLoss = _BmmOcgPtpMuxInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3, 1, 1, 6),
    _BmmOcgPtpMuxInsertionLoss_Type()
)
bmmOcgPtpMuxInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmOcgPtpMuxInsertionLoss.setStatus("current")


class _BmmOcgPtpDeMuxInsertionLoss_Type(FloatTenths):
    """Custom type bmmOcgPtpDeMuxInsertionLoss based on FloatTenths"""
    defaultValue = 0


_BmmOcgPtpDeMuxInsertionLoss_Type.__name__ = "FloatTenths"
_BmmOcgPtpDeMuxInsertionLoss_Object = MibTableColumn
bmmOcgPtpDeMuxInsertionLoss = _BmmOcgPtpDeMuxInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3, 1, 1, 7),
    _BmmOcgPtpDeMuxInsertionLoss_Type()
)
bmmOcgPtpDeMuxInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmOcgPtpDeMuxInsertionLoss.setStatus("current")


class _BmmOcgPtpPmHistStatsEnable_Type(InfnPmHistStatsControl):
    """Custom type bmmOcgPtpPmHistStatsEnable based on InfnPmHistStatsControl"""
    defaultValue = 1


_BmmOcgPtpPmHistStatsEnable_Type.__name__ = "InfnPmHistStatsControl"
_BmmOcgPtpPmHistStatsEnable_Object = MibTableColumn
bmmOcgPtpPmHistStatsEnable = _BmmOcgPtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3, 1, 1, 8),
    _BmmOcgPtpPmHistStatsEnable_Type()
)
bmmOcgPtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmmOcgPtpPmHistStatsEnable.setStatus("current")


class _BmmOcgPtpOcgPortConfig_Type(InfnOcgPortConfig):
    """Custom type bmmOcgPtpOcgPortConfig based on InfnOcgPortConfig"""
    defaultValue = 2


_BmmOcgPtpOcgPortConfig_Type.__name__ = "InfnOcgPortConfig"
_BmmOcgPtpOcgPortConfig_Object = MibTableColumn
bmmOcgPtpOcgPortConfig = _BmmOcgPtpOcgPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3, 1, 1, 9),
    _BmmOcgPtpOcgPortConfig_Type()
)
bmmOcgPtpOcgPortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmOcgPtpOcgPortConfig.setStatus("current")


class _BmmOcgPtpOcgSignalType_Type(InfnSignalType):
    """Custom type bmmOcgPtpOcgSignalType based on InfnSignalType"""
    defaultValue = 1


_BmmOcgPtpOcgSignalType_Type.__name__ = "InfnSignalType"
_BmmOcgPtpOcgSignalType_Object = MibTableColumn
bmmOcgPtpOcgSignalType = _BmmOcgPtpOcgSignalType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3, 1, 1, 10),
    _BmmOcgPtpOcgSignalType_Type()
)
bmmOcgPtpOcgSignalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmmOcgPtpOcgSignalType.setStatus("current")
_BmmOcgPtpOcgActiveChannelMap_Type = InfnOcgChannelMap
_BmmOcgPtpOcgActiveChannelMap_Object = MibTableColumn
bmmOcgPtpOcgActiveChannelMap = _BmmOcgPtpOcgActiveChannelMap_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3, 1, 1, 11),
    _BmmOcgPtpOcgActiveChannelMap_Type()
)
bmmOcgPtpOcgActiveChannelMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmmOcgPtpOcgActiveChannelMap.setStatus("current")
_BmmOcgPtpDiscoveredRemoteTP_Type = DisplayString
_BmmOcgPtpDiscoveredRemoteTP_Object = MibTableColumn
bmmOcgPtpDiscoveredRemoteTP = _BmmOcgPtpDiscoveredRemoteTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3, 1, 1, 12),
    _BmmOcgPtpDiscoveredRemoteTP_Type()
)
bmmOcgPtpDiscoveredRemoteTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmOcgPtpDiscoveredRemoteTP.setStatus("current")
_BmmOcgPtpAutoDiscSoakTime_Type = Unsigned32
_BmmOcgPtpAutoDiscSoakTime_Object = MibTableColumn
bmmOcgPtpAutoDiscSoakTime = _BmmOcgPtpAutoDiscSoakTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3, 1, 1, 13),
    _BmmOcgPtpAutoDiscSoakTime_Type()
)
bmmOcgPtpAutoDiscSoakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmmOcgPtpAutoDiscSoakTime.setStatus("current")
_BmmOcgPtpShutterState_Type = InfnShutterState
_BmmOcgPtpShutterState_Object = MibTableColumn
bmmOcgPtpShutterState = _BmmOcgPtpShutterState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3, 1, 1, 14),
    _BmmOcgPtpShutterState_Type()
)
bmmOcgPtpShutterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmmOcgPtpShutterState.setStatus("current")
_BmmOcgPtpProvOpenWaveRemotePtp_Type = DisplayString
_BmmOcgPtpProvOpenWaveRemotePtp_Object = MibTableColumn
bmmOcgPtpProvOpenWaveRemotePtp = _BmmOcgPtpProvOpenWaveRemotePtp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3, 1, 1, 15),
    _BmmOcgPtpProvOpenWaveRemotePtp_Type()
)
bmmOcgPtpProvOpenWaveRemotePtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmmOcgPtpProvOpenWaveRemotePtp.setStatus("current")
_BmmOcgPtpConformance_ObjectIdentity = ObjectIdentity
bmmOcgPtpConformance = _BmmOcgPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3, 3)
)
_BmmOcgPtpCompliances_ObjectIdentity = ObjectIdentity
bmmOcgPtpCompliances = _BmmOcgPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3, 3, 1)
)
_BmmOcgPtpGroups_ObjectIdentity = ObjectIdentity
bmmOcgPtpGroups = _BmmOcgPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3, 3, 2)
)

# Managed Objects groups

bmmOcgPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3, 3, 2, 1)
)
bmmOcgPtpGroup.setObjects(
      *(("INFINERA-TP-BMMOCGPTP-MIB", "bmmOcgPtpDiscoveredOcgTP"),
        ("INFINERA-TP-BMMOCGPTP-MIB", "bmmOcgPtpProvisionedOcgTP"),
        ("INFINERA-TP-BMMOCGPTP-MIB", "bmmOcgPtpOcgNumber"),
        ("INFINERA-TP-BMMOCGPTP-MIB", "bmmOcgPtpOcgPowerControlLoop"),
        ("INFINERA-TP-BMMOCGPTP-MIB", "bmmOcgPtpTargetRxOcgPower"),
        ("INFINERA-TP-BMMOCGPTP-MIB", "bmmOcgPtpMuxInsertionLoss"),
        ("INFINERA-TP-BMMOCGPTP-MIB", "bmmOcgPtpDeMuxInsertionLoss"),
        ("INFINERA-TP-BMMOCGPTP-MIB", "bmmOcgPtpPmHistStatsEnable"),
        ("INFINERA-TP-BMMOCGPTP-MIB", "bmmOcgPtpOcgPortConfig"),
        ("INFINERA-TP-BMMOCGPTP-MIB", "bmmOcgPtpOcgSignalType"),
        ("INFINERA-TP-BMMOCGPTP-MIB", "bmmOcgPtpOcgActiveChannelMap"),
        ("INFINERA-TP-BMMOCGPTP-MIB", "bmmOcgPtpDiscoveredRemoteTP"),
        ("INFINERA-TP-BMMOCGPTP-MIB", "bmmOcgPtpAutoDiscSoakTime"),
        ("INFINERA-TP-BMMOCGPTP-MIB", "bmmOcgPtpShutterState"),
        ("INFINERA-TP-BMMOCGPTP-MIB", "bmmOcgPtpProvOpenWaveRemotePtp"))
)
if mibBuilder.loadTexts:
    bmmOcgPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bmmOcgPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 3, 3, 1, 1)
)
bmmOcgPtpCompliance.setObjects(
    ("INFINERA-TP-BMMOCGPTP-MIB", "bmmOcgPtpGroup")
)
if mibBuilder.loadTexts:
    bmmOcgPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-BMMOCGPTP-MIB",
    **{"bmmOcgPtpMIB": bmmOcgPtpMIB,
       "bmmOcgPtpTable": bmmOcgPtpTable,
       "bmmOcgPtpEntry": bmmOcgPtpEntry,
       "bmmOcgPtpDiscoveredOcgTP": bmmOcgPtpDiscoveredOcgTP,
       "bmmOcgPtpProvisionedOcgTP": bmmOcgPtpProvisionedOcgTP,
       "bmmOcgPtpOcgNumber": bmmOcgPtpOcgNumber,
       "bmmOcgPtpOcgPowerControlLoop": bmmOcgPtpOcgPowerControlLoop,
       "bmmOcgPtpTargetRxOcgPower": bmmOcgPtpTargetRxOcgPower,
       "bmmOcgPtpMuxInsertionLoss": bmmOcgPtpMuxInsertionLoss,
       "bmmOcgPtpDeMuxInsertionLoss": bmmOcgPtpDeMuxInsertionLoss,
       "bmmOcgPtpPmHistStatsEnable": bmmOcgPtpPmHistStatsEnable,
       "bmmOcgPtpOcgPortConfig": bmmOcgPtpOcgPortConfig,
       "bmmOcgPtpOcgSignalType": bmmOcgPtpOcgSignalType,
       "bmmOcgPtpOcgActiveChannelMap": bmmOcgPtpOcgActiveChannelMap,
       "bmmOcgPtpDiscoveredRemoteTP": bmmOcgPtpDiscoveredRemoteTP,
       "bmmOcgPtpAutoDiscSoakTime": bmmOcgPtpAutoDiscSoakTime,
       "bmmOcgPtpShutterState": bmmOcgPtpShutterState,
       "bmmOcgPtpProvOpenWaveRemotePtp": bmmOcgPtpProvOpenWaveRemotePtp,
       "bmmOcgPtpConformance": bmmOcgPtpConformance,
       "bmmOcgPtpCompliances": bmmOcgPtpCompliances,
       "bmmOcgPtpCompliance": bmmOcgPtpCompliance,
       "bmmOcgPtpGroups": bmmOcgPtpGroups,
       "bmmOcgPtpGroup": bmmOcgPtpGroup}
)
