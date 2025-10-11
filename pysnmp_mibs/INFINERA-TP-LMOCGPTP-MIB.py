# SNMP MIB module (INFINERA-TP-LMOCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-LMOCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:12:47 2025
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
 InfnEncoding,
 InfnLineSystemMode,
 InfnModulation,
 InfnPowerControlLoop) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnAutoDiscoveryState",
    "InfnEncoding",
    "InfnLineSystemMode",
    "InfnModulation",
    "InfnPowerControlLoop")

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

lmOcgPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 34)
)
if mibBuilder.loadTexts:
    lmOcgPtpMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LmOcgPtpTable_Object = MibTable
lmOcgPtpTable = _LmOcgPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 34, 1)
)
if mibBuilder.loadTexts:
    lmOcgPtpTable.setStatus("current")
_LmOcgPtpEntry_Object = MibTableRow
lmOcgPtpEntry = _LmOcgPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 34, 1, 1)
)
lmOcgPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lmOcgPtpEntry.setStatus("current")
_LmOcgPtpDiscoveredRemoteTP_Type = DisplayString
_LmOcgPtpDiscoveredRemoteTP_Object = MibTableColumn
lmOcgPtpDiscoveredRemoteTP = _LmOcgPtpDiscoveredRemoteTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 34, 1, 1, 1),
    _LmOcgPtpDiscoveredRemoteTP_Type()
)
lmOcgPtpDiscoveredRemoteTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOcgPtpDiscoveredRemoteTP.setStatus("current")


class _LmOcgPtpAutoDiscoveryState_Type(InfnAutoDiscoveryState):
    """Custom type lmOcgPtpAutoDiscoveryState based on InfnAutoDiscoveryState"""
    defaultValue = 4


_LmOcgPtpAutoDiscoveryState_Type.__name__ = "InfnAutoDiscoveryState"
_LmOcgPtpAutoDiscoveryState_Object = MibTableColumn
lmOcgPtpAutoDiscoveryState = _LmOcgPtpAutoDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 34, 1, 1, 2),
    _LmOcgPtpAutoDiscoveryState_Type()
)
lmOcgPtpAutoDiscoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOcgPtpAutoDiscoveryState.setStatus("current")


class _LmOcgPtpOcgPowerControlLoop_Type(InfnPowerControlLoop):
    """Custom type lmOcgPtpOcgPowerControlLoop based on InfnPowerControlLoop"""
    defaultValue = 2


_LmOcgPtpOcgPowerControlLoop_Type.__name__ = "InfnPowerControlLoop"
_LmOcgPtpOcgPowerControlLoop_Object = MibTableColumn
lmOcgPtpOcgPowerControlLoop = _LmOcgPtpOcgPowerControlLoop_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 34, 1, 1, 3),
    _LmOcgPtpOcgPowerControlLoop_Type()
)
lmOcgPtpOcgPowerControlLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmOcgPtpOcgPowerControlLoop.setStatus("current")
_LmOcgPtpProvisionedOcgTP_Type = DisplayString
_LmOcgPtpProvisionedOcgTP_Object = MibTableColumn
lmOcgPtpProvisionedOcgTP = _LmOcgPtpProvisionedOcgTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 34, 1, 1, 4),
    _LmOcgPtpProvisionedOcgTP_Type()
)
lmOcgPtpProvisionedOcgTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmOcgPtpProvisionedOcgTP.setStatus("current")
_LmOcgPtpDiscoveredOcgTP_Type = DisplayString
_LmOcgPtpDiscoveredOcgTP_Object = MibTableColumn
lmOcgPtpDiscoveredOcgTP = _LmOcgPtpDiscoveredOcgTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 34, 1, 1, 5),
    _LmOcgPtpDiscoveredOcgTP_Type()
)
lmOcgPtpDiscoveredOcgTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOcgPtpDiscoveredOcgTP.setStatus("current")
_LmOcgPtpAssocTeIntfList_Type = DisplayString
_LmOcgPtpAssocTeIntfList_Object = MibTableColumn
lmOcgPtpAssocTeIntfList = _LmOcgPtpAssocTeIntfList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 34, 1, 1, 6),
    _LmOcgPtpAssocTeIntfList_Type()
)
lmOcgPtpAssocTeIntfList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOcgPtpAssocTeIntfList.setStatus("current")
_LmOcgPtpChannelCount_Type = FloatTenths
_LmOcgPtpChannelCount_Object = MibTableColumn
lmOcgPtpChannelCount = _LmOcgPtpChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 34, 1, 1, 7),
    _LmOcgPtpChannelCount_Type()
)
lmOcgPtpChannelCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmOcgPtpChannelCount.setStatus("current")
_LmOcgPtpLineSystemMode_Type = InfnLineSystemMode
_LmOcgPtpLineSystemMode_Object = MibTableColumn
lmOcgPtpLineSystemMode = _LmOcgPtpLineSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 34, 1, 1, 8),
    _LmOcgPtpLineSystemMode_Type()
)
lmOcgPtpLineSystemMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmOcgPtpLineSystemMode.setStatus("current")
_LmOcgPtpProvPeerTP_Type = DisplayString
_LmOcgPtpProvPeerTP_Object = MibTableColumn
lmOcgPtpProvPeerTP = _LmOcgPtpProvPeerTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 34, 1, 1, 9),
    _LmOcgPtpProvPeerTP_Type()
)
lmOcgPtpProvPeerTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmOcgPtpProvPeerTP.setStatus("current")
_LmOcgOpenwaveTargetTxOcgPower_Type = FloatTenths
_LmOcgOpenwaveTargetTxOcgPower_Object = MibTableColumn
lmOcgOpenwaveTargetTxOcgPower = _LmOcgOpenwaveTargetTxOcgPower_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 34, 1, 1, 10),
    _LmOcgOpenwaveTargetTxOcgPower_Type()
)
lmOcgOpenwaveTargetTxOcgPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmOcgOpenwaveTargetTxOcgPower.setStatus("current")
_LmOcgProvisionedEncodingMode_Type = InfnEncoding
_LmOcgProvisionedEncodingMode_Object = MibTableColumn
lmOcgProvisionedEncodingMode = _LmOcgProvisionedEncodingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 34, 1, 1, 11),
    _LmOcgProvisionedEncodingMode_Type()
)
lmOcgProvisionedEncodingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmOcgProvisionedEncodingMode.setStatus("current")
_LmOcgInstalledEncodingMode_Type = InfnEncoding
_LmOcgInstalledEncodingMode_Object = MibTableColumn
lmOcgInstalledEncodingMode = _LmOcgInstalledEncodingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 34, 1, 1, 12),
    _LmOcgInstalledEncodingMode_Type()
)
lmOcgInstalledEncodingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOcgInstalledEncodingMode.setStatus("current")
_LmOcgPtpConformance_ObjectIdentity = ObjectIdentity
lmOcgPtpConformance = _LmOcgPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 34, 3)
)
_LmOcgPtpCompliances_ObjectIdentity = ObjectIdentity
lmOcgPtpCompliances = _LmOcgPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 34, 3, 1)
)
_LmOcgPtpGroups_ObjectIdentity = ObjectIdentity
lmOcgPtpGroups = _LmOcgPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 34, 3, 2)
)

# Managed Objects groups

lmOcgPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 34, 3, 2, 1)
)
lmOcgPtpGroup.setObjects(
      *(("INFINERA-TP-LMOCGPTP-MIB", "lmOcgPtpDiscoveredRemoteTP"),
        ("INFINERA-TP-LMOCGPTP-MIB", "lmOcgPtpAutoDiscoveryState"),
        ("INFINERA-TP-LMOCGPTP-MIB", "lmOcgPtpOcgPowerControlLoop"),
        ("INFINERA-TP-LMOCGPTP-MIB", "lmOcgPtpProvisionedOcgTP"),
        ("INFINERA-TP-LMOCGPTP-MIB", "lmOcgPtpDiscoveredOcgTP"),
        ("INFINERA-TP-LMOCGPTP-MIB", "lmOcgPtpAssocTeIntfList"),
        ("INFINERA-TP-LMOCGPTP-MIB", "lmOcgPtpChannelCount"),
        ("INFINERA-TP-LMOCGPTP-MIB", "lmOcgPtpLineSystemMode"),
        ("INFINERA-TP-LMOCGPTP-MIB", "lmOcgPtpProvPeerTP"),
        ("INFINERA-TP-LMOCGPTP-MIB", "lmOcgOpenwaveTargetTxOcgPower"),
        ("INFINERA-TP-LMOCGPTP-MIB", "lmOcgProvisionedEncodingMode"),
        ("INFINERA-TP-LMOCGPTP-MIB", "lmOcgInstalledEncodingMode"))
)
if mibBuilder.loadTexts:
    lmOcgPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lmOcgPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 34, 3, 1, 1)
)
lmOcgPtpCompliance.setObjects(
    ("INFINERA-TP-LMOCGPTP-MIB", "lmOcgPtpGroup")
)
if mibBuilder.loadTexts:
    lmOcgPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-LMOCGPTP-MIB",
    **{"lmOcgPtpMIB": lmOcgPtpMIB,
       "lmOcgPtpTable": lmOcgPtpTable,
       "lmOcgPtpEntry": lmOcgPtpEntry,
       "lmOcgPtpDiscoveredRemoteTP": lmOcgPtpDiscoveredRemoteTP,
       "lmOcgPtpAutoDiscoveryState": lmOcgPtpAutoDiscoveryState,
       "lmOcgPtpOcgPowerControlLoop": lmOcgPtpOcgPowerControlLoop,
       "lmOcgPtpProvisionedOcgTP": lmOcgPtpProvisionedOcgTP,
       "lmOcgPtpDiscoveredOcgTP": lmOcgPtpDiscoveredOcgTP,
       "lmOcgPtpAssocTeIntfList": lmOcgPtpAssocTeIntfList,
       "lmOcgPtpChannelCount": lmOcgPtpChannelCount,
       "lmOcgPtpLineSystemMode": lmOcgPtpLineSystemMode,
       "lmOcgPtpProvPeerTP": lmOcgPtpProvPeerTP,
       "lmOcgOpenwaveTargetTxOcgPower": lmOcgOpenwaveTargetTxOcgPower,
       "lmOcgProvisionedEncodingMode": lmOcgProvisionedEncodingMode,
       "lmOcgInstalledEncodingMode": lmOcgInstalledEncodingMode,
       "lmOcgPtpConformance": lmOcgPtpConformance,
       "lmOcgPtpCompliances": lmOcgPtpCompliances,
       "lmOcgPtpCompliance": lmOcgPtpCompliance,
       "lmOcgPtpGroups": lmOcgPtpGroups,
       "lmOcgPtpGroup": lmOcgPtpGroup}
)
