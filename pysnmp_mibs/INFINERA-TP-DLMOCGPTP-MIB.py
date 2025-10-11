# SNMP MIB module (INFINERA-TP-DLMOCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-DLMOCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:12 2025
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
 InfnAutoDiscoveryState,
 InfnLineSystemMode,
 InfnOperationalState,
 InfnPmHistStatsControl) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnAutoDiscoveryState",
    "InfnLineSystemMode",
    "InfnOperationalState",
    "InfnPmHistStatsControl")

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

dlmOcgPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 6)
)
if mibBuilder.loadTexts:
    dlmOcgPtpMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DlmOcgPtpTable_Object = MibTable
dlmOcgPtpTable = _DlmOcgPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 6, 1)
)
if mibBuilder.loadTexts:
    dlmOcgPtpTable.setStatus("current")
_DlmOcgPtpEntry_Object = MibTableRow
dlmOcgPtpEntry = _DlmOcgPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 6, 1, 1)
)
dlmOcgPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dlmOcgPtpEntry.setStatus("current")
_DlmOcgPtpDiscoveredRemoteTP_Type = DisplayString
_DlmOcgPtpDiscoveredRemoteTP_Object = MibTableColumn
dlmOcgPtpDiscoveredRemoteTP = _DlmOcgPtpDiscoveredRemoteTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 6, 1, 1, 1),
    _DlmOcgPtpDiscoveredRemoteTP_Type()
)
dlmOcgPtpDiscoveredRemoteTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlmOcgPtpDiscoveredRemoteTP.setStatus("current")


class _DlmOcgPtpAutoDiscoveryState_Type(InfnAutoDiscoveryState):
    """Custom type dlmOcgPtpAutoDiscoveryState based on InfnAutoDiscoveryState"""
    defaultValue = 4


_DlmOcgPtpAutoDiscoveryState_Type.__name__ = "InfnAutoDiscoveryState"
_DlmOcgPtpAutoDiscoveryState_Object = MibTableColumn
dlmOcgPtpAutoDiscoveryState = _DlmOcgPtpAutoDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 6, 1, 1, 2),
    _DlmOcgPtpAutoDiscoveryState_Type()
)
dlmOcgPtpAutoDiscoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlmOcgPtpAutoDiscoveryState.setStatus("current")


class _DlmOcgPtpPmHistStatsEnable_Type(InfnPmHistStatsControl):
    """Custom type dlmOcgPtpPmHistStatsEnable based on InfnPmHistStatsControl"""
    defaultValue = 1


_DlmOcgPtpPmHistStatsEnable_Type.__name__ = "InfnPmHistStatsControl"
_DlmOcgPtpPmHistStatsEnable_Object = MibTableColumn
dlmOcgPtpPmHistStatsEnable = _DlmOcgPtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 6, 1, 1, 3),
    _DlmOcgPtpPmHistStatsEnable_Type()
)
dlmOcgPtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlmOcgPtpPmHistStatsEnable.setStatus("obsolete")


class _DlmOcgPtpIsBorderOCG_Type(TruthValue):
    """Custom type dlmOcgPtpIsBorderOCG based on TruthValue"""
    defaultValue = 2


_DlmOcgPtpIsBorderOCG_Type.__name__ = "TruthValue"
_DlmOcgPtpIsBorderOCG_Object = MibTableColumn
dlmOcgPtpIsBorderOCG = _DlmOcgPtpIsBorderOCG_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 6, 1, 1, 4),
    _DlmOcgPtpIsBorderOCG_Type()
)
dlmOcgPtpIsBorderOCG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlmOcgPtpIsBorderOCG.setStatus("obsolete")


class _DlmOcgPtpOcgPowerControlLoop_Type(InfnOperationalState):
    """Custom type dlmOcgPtpOcgPowerControlLoop based on InfnOperationalState"""
    defaultValue = 2


_DlmOcgPtpOcgPowerControlLoop_Type.__name__ = "InfnOperationalState"
_DlmOcgPtpOcgPowerControlLoop_Object = MibTableColumn
dlmOcgPtpOcgPowerControlLoop = _DlmOcgPtpOcgPowerControlLoop_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 6, 1, 1, 5),
    _DlmOcgPtpOcgPowerControlLoop_Type()
)
dlmOcgPtpOcgPowerControlLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlmOcgPtpOcgPowerControlLoop.setStatus("current")
_DlmOcgPtpProvisionedOcgTP_Type = DisplayString
_DlmOcgPtpProvisionedOcgTP_Object = MibTableColumn
dlmOcgPtpProvisionedOcgTP = _DlmOcgPtpProvisionedOcgTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 6, 1, 1, 6),
    _DlmOcgPtpProvisionedOcgTP_Type()
)
dlmOcgPtpProvisionedOcgTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlmOcgPtpProvisionedOcgTP.setStatus("current")
_DlmOcgPtpDiscoveredOcgTP_Type = DisplayString
_DlmOcgPtpDiscoveredOcgTP_Object = MibTableColumn
dlmOcgPtpDiscoveredOcgTP = _DlmOcgPtpDiscoveredOcgTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 6, 1, 1, 7),
    _DlmOcgPtpDiscoveredOcgTP_Type()
)
dlmOcgPtpDiscoveredOcgTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlmOcgPtpDiscoveredOcgTP.setStatus("current")


class _DlmOcgPtpLineSystemMode_Type(InfnLineSystemMode):
    """Custom type dlmOcgPtpLineSystemMode based on InfnLineSystemMode"""
    defaultValue = 1


_DlmOcgPtpLineSystemMode_Type.__name__ = "InfnLineSystemMode"
_DlmOcgPtpLineSystemMode_Object = MibTableColumn
dlmOcgPtpLineSystemMode = _DlmOcgPtpLineSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 6, 1, 1, 8),
    _DlmOcgPtpLineSystemMode_Type()
)
dlmOcgPtpLineSystemMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlmOcgPtpLineSystemMode.setStatus("current")
_DlmOcgPtpProvisionedPeerTP_Type = DisplayString
_DlmOcgPtpProvisionedPeerTP_Object = MibTableColumn
dlmOcgPtpProvisionedPeerTP = _DlmOcgPtpProvisionedPeerTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 6, 1, 1, 9),
    _DlmOcgPtpProvisionedPeerTP_Type()
)
dlmOcgPtpProvisionedPeerTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlmOcgPtpProvisionedPeerTP.setStatus("current")


class _DlmOcgPtpOpenwaveTargetTxOcgPower_Type(FloatTenths):
    """Custom type dlmOcgPtpOpenwaveTargetTxOcgPower based on FloatTenths"""
    defaultValue = 50


_DlmOcgPtpOpenwaveTargetTxOcgPower_Type.__name__ = "FloatTenths"
_DlmOcgPtpOpenwaveTargetTxOcgPower_Object = MibTableColumn
dlmOcgPtpOpenwaveTargetTxOcgPower = _DlmOcgPtpOpenwaveTargetTxOcgPower_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 6, 1, 1, 10),
    _DlmOcgPtpOpenwaveTargetTxOcgPower_Type()
)
dlmOcgPtpOpenwaveTargetTxOcgPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlmOcgPtpOpenwaveTargetTxOcgPower.setStatus("current")


class _DlmOcgPtpChannelCount_Type(FloatTenths):
    """Custom type dlmOcgPtpChannelCount based on FloatTenths"""
    defaultValue = 100


_DlmOcgPtpChannelCount_Type.__name__ = "FloatTenths"
_DlmOcgPtpChannelCount_Object = MibTableColumn
dlmOcgPtpChannelCount = _DlmOcgPtpChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 6, 1, 1, 11),
    _DlmOcgPtpChannelCount_Type()
)
dlmOcgPtpChannelCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlmOcgPtpChannelCount.setStatus("current")


class _DlmOcgPtpAggregateRate_Type(FloatTenths):
    """Custom type dlmOcgPtpAggregateRate based on FloatTenths"""
    defaultValue = 500


_DlmOcgPtpAggregateRate_Type.__name__ = "FloatTenths"
_DlmOcgPtpAggregateRate_Object = MibTableColumn
dlmOcgPtpAggregateRate = _DlmOcgPtpAggregateRate_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 6, 1, 1, 12),
    _DlmOcgPtpAggregateRate_Type()
)
dlmOcgPtpAggregateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlmOcgPtpAggregateRate.setStatus("current")
_DlmOcgPtpConformance_ObjectIdentity = ObjectIdentity
dlmOcgPtpConformance = _DlmOcgPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 6, 3)
)
_DlmOcgPtpCompliances_ObjectIdentity = ObjectIdentity
dlmOcgPtpCompliances = _DlmOcgPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 6, 3, 1)
)
_DlmOcgPtpGroups_ObjectIdentity = ObjectIdentity
dlmOcgPtpGroups = _DlmOcgPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 6, 3, 2)
)

# Managed Objects groups

dlmOcgPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 6, 3, 2, 1)
)
dlmOcgPtpGroup.setObjects(
      *(("INFINERA-TP-DLMOCGPTP-MIB", "dlmOcgPtpDiscoveredRemoteTP"),
        ("INFINERA-TP-DLMOCGPTP-MIB", "dlmOcgPtpAutoDiscoveryState"),
        ("INFINERA-TP-DLMOCGPTP-MIB", "dlmOcgPtpPmHistStatsEnable"),
        ("INFINERA-TP-DLMOCGPTP-MIB", "dlmOcgPtpIsBorderOCG"),
        ("INFINERA-TP-DLMOCGPTP-MIB", "dlmOcgPtpOcgPowerControlLoop"),
        ("INFINERA-TP-DLMOCGPTP-MIB", "dlmOcgPtpProvisionedOcgTP"),
        ("INFINERA-TP-DLMOCGPTP-MIB", "dlmOcgPtpDiscoveredOcgTP"),
        ("INFINERA-TP-DLMOCGPTP-MIB", "dlmOcgPtpLineSystemMode"),
        ("INFINERA-TP-DLMOCGPTP-MIB", "dlmOcgPtpProvisionedPeerTP"),
        ("INFINERA-TP-DLMOCGPTP-MIB", "dlmOcgPtpOpenwaveTargetTxOcgPower"),
        ("INFINERA-TP-DLMOCGPTP-MIB", "dlmOcgPtpChannelCount"),
        ("INFINERA-TP-DLMOCGPTP-MIB", "dlmOcgPtpAggregateRate"))
)
if mibBuilder.loadTexts:
    dlmOcgPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dlmOcgPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 6, 3, 1, 1)
)
dlmOcgPtpCompliance.setObjects(
    ("INFINERA-TP-DLMOCGPTP-MIB", "dlmOcgPtpGroup")
)
if mibBuilder.loadTexts:
    dlmOcgPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-DLMOCGPTP-MIB",
    **{"dlmOcgPtpMIB": dlmOcgPtpMIB,
       "dlmOcgPtpTable": dlmOcgPtpTable,
       "dlmOcgPtpEntry": dlmOcgPtpEntry,
       "dlmOcgPtpDiscoveredRemoteTP": dlmOcgPtpDiscoveredRemoteTP,
       "dlmOcgPtpAutoDiscoveryState": dlmOcgPtpAutoDiscoveryState,
       "dlmOcgPtpPmHistStatsEnable": dlmOcgPtpPmHistStatsEnable,
       "dlmOcgPtpIsBorderOCG": dlmOcgPtpIsBorderOCG,
       "dlmOcgPtpOcgPowerControlLoop": dlmOcgPtpOcgPowerControlLoop,
       "dlmOcgPtpProvisionedOcgTP": dlmOcgPtpProvisionedOcgTP,
       "dlmOcgPtpDiscoveredOcgTP": dlmOcgPtpDiscoveredOcgTP,
       "dlmOcgPtpLineSystemMode": dlmOcgPtpLineSystemMode,
       "dlmOcgPtpProvisionedPeerTP": dlmOcgPtpProvisionedPeerTP,
       "dlmOcgPtpOpenwaveTargetTxOcgPower": dlmOcgPtpOpenwaveTargetTxOcgPower,
       "dlmOcgPtpChannelCount": dlmOcgPtpChannelCount,
       "dlmOcgPtpAggregateRate": dlmOcgPtpAggregateRate,
       "dlmOcgPtpConformance": dlmOcgPtpConformance,
       "dlmOcgPtpCompliances": dlmOcgPtpCompliances,
       "dlmOcgPtpCompliance": dlmOcgPtpCompliance,
       "dlmOcgPtpGroups": dlmOcgPtpGroups,
       "dlmOcgPtpGroup": dlmOcgPtpGroup}
)
