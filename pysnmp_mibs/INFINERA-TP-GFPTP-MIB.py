# SNMP MIB module (INFINERA-TP-GFPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-GFPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:15 2025
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

(InfnGFPPayloadFCS,
 InfnGFPState,
 InfnGfpExtHdrTyp,
 InfnNetworkMapping,
 InfnPmHistStatsControl,
 InfnSMQ,
 InfnServiceMode) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnGFPPayloadFCS",
    "InfnGFPState",
    "InfnGfpExtHdrTyp",
    "InfnNetworkMapping",
    "InfnPmHistStatsControl",
    "InfnSMQ",
    "InfnServiceMode")

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

gfpTpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 80)
)
if mibBuilder.loadTexts:
    gfpTpMIB.setRevisions(
        ("2011-04-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GfpTpTable_Object = MibTable
gfpTpTable = _GfpTpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 80, 1)
)
if mibBuilder.loadTexts:
    gfpTpTable.setStatus("current")
_GfpTpEntry_Object = MibTableRow
gfpTpEntry = _GfpTpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 80, 1, 1)
)
gfpTpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gfpTpEntry.setStatus("current")


class _GfpTpPayloadFCS_Type(InfnGFPPayloadFCS):
    """Custom type gfpTpPayloadFCS based on InfnGFPPayloadFCS"""
    defaultValue = 2


_GfpTpPayloadFCS_Type.__name__ = "InfnGFPPayloadFCS"
_GfpTpPayloadFCS_Object = MibTableColumn
gfpTpPayloadFCS = _GfpTpPayloadFCS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 80, 1, 1, 1),
    _GfpTpPayloadFCS_Type()
)
gfpTpPayloadFCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gfpTpPayloadFCS.setStatus("current")


class _GfpTpExtHeaderType_Type(InfnGfpExtHdrTyp):
    """Custom type gfpTpExtHeaderType based on InfnGfpExtHdrTyp"""
    defaultValue = 1


_GfpTpExtHeaderType_Type.__name__ = "InfnGfpExtHdrTyp"
_GfpTpExtHeaderType_Object = MibTableColumn
gfpTpExtHeaderType = _GfpTpExtHeaderType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 80, 1, 1, 2),
    _GfpTpExtHeaderType_Type()
)
gfpTpExtHeaderType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gfpTpExtHeaderType.setStatus("current")


class _GfpTpChannelId_Type(Unsigned32):
    """Custom type gfpTpChannelId based on Unsigned32"""
    defaultValue = 0


_GfpTpChannelId_Type.__name__ = "Unsigned32"
_GfpTpChannelId_Object = MibTableColumn
gfpTpChannelId = _GfpTpChannelId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 80, 1, 1, 3),
    _GfpTpChannelId_Type()
)
gfpTpChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gfpTpChannelId.setStatus("current")


class _GfpTpServiceMode_Type(InfnServiceMode):
    """Custom type gfpTpServiceMode based on InfnServiceMode"""
    defaultValue = 1


_GfpTpServiceMode_Type.__name__ = "InfnServiceMode"
_GfpTpServiceMode_Object = MibTableColumn
gfpTpServiceMode = _GfpTpServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 80, 1, 1, 4),
    _GfpTpServiceMode_Type()
)
gfpTpServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpTpServiceMode.setStatus("current")


class _GfpTpServiceModeQualifier_Type(InfnSMQ):
    """Custom type gfpTpServiceModeQualifier based on InfnSMQ"""
    defaultValue = 1


_GfpTpServiceModeQualifier_Type.__name__ = "InfnSMQ"
_GfpTpServiceModeQualifier_Object = MibTableColumn
gfpTpServiceModeQualifier = _GfpTpServiceModeQualifier_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 80, 1, 1, 5),
    _GfpTpServiceModeQualifier_Type()
)
gfpTpServiceModeQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpTpServiceModeQualifier.setStatus("current")
_GfpTpNetworkMap_Type = InfnNetworkMapping
_GfpTpNetworkMap_Object = MibTableColumn
gfpTpNetworkMap = _GfpTpNetworkMap_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 80, 1, 1, 6),
    _GfpTpNetworkMap_Type()
)
gfpTpNetworkMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpTpNetworkMap.setStatus("current")
_GfpTpGFPState_Type = InfnGFPState
_GfpTpGFPState_Object = MibTableColumn
gfpTpGFPState = _GfpTpGFPState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 80, 1, 1, 7),
    _GfpTpGFPState_Type()
)
gfpTpGFPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpTpGFPState.setStatus("current")
_GfpTpHistStatsEnable_Type = InfnPmHistStatsControl
_GfpTpHistStatsEnable_Object = MibTableColumn
gfpTpHistStatsEnable = _GfpTpHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 80, 1, 1, 8),
    _GfpTpHistStatsEnable_Type()
)
gfpTpHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gfpTpHistStatsEnable.setStatus("current")
_GfpTpConformance_ObjectIdentity = ObjectIdentity
gfpTpConformance = _GfpTpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 80, 3)
)
_GfpTpCompliances_ObjectIdentity = ObjectIdentity
gfpTpCompliances = _GfpTpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 80, 3, 1)
)
_GfpTpGroups_ObjectIdentity = ObjectIdentity
gfpTpGroups = _GfpTpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 80, 3, 2)
)

# Managed Objects groups

gfpTpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 80, 3, 2, 1)
)
gfpTpGroup.setObjects(
      *(("INFINERA-TP-GFPTP-MIB", "gfpTpPayloadFCS"),
        ("INFINERA-TP-GFPTP-MIB", "gfpTpExtHeaderType"),
        ("INFINERA-TP-GFPTP-MIB", "gfpTpChannelId"),
        ("INFINERA-TP-GFPTP-MIB", "gfpTpServiceMode"),
        ("INFINERA-TP-GFPTP-MIB", "gfpTpServiceModeQualifier"),
        ("INFINERA-TP-GFPTP-MIB", "gfpTpNetworkMap"),
        ("INFINERA-TP-GFPTP-MIB", "gfpTpGFPState"),
        ("INFINERA-TP-GFPTP-MIB", "gfpTpHistStatsEnable"))
)
if mibBuilder.loadTexts:
    gfpTpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

gfpTpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 80, 3, 1, 1)
)
gfpTpCompliance.setObjects(
    ("INFINERA-TP-GFPTP-MIB", "gfpTpGroup")
)
if mibBuilder.loadTexts:
    gfpTpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-GFPTP-MIB",
    **{"gfpTpMIB": gfpTpMIB,
       "gfpTpTable": gfpTpTable,
       "gfpTpEntry": gfpTpEntry,
       "gfpTpPayloadFCS": gfpTpPayloadFCS,
       "gfpTpExtHeaderType": gfpTpExtHeaderType,
       "gfpTpChannelId": gfpTpChannelId,
       "gfpTpServiceMode": gfpTpServiceMode,
       "gfpTpServiceModeQualifier": gfpTpServiceModeQualifier,
       "gfpTpNetworkMap": gfpTpNetworkMap,
       "gfpTpGFPState": gfpTpGFPState,
       "gfpTpHistStatsEnable": gfpTpHistStatsEnable,
       "gfpTpConformance": gfpTpConformance,
       "gfpTpCompliances": gfpTpCompliances,
       "gfpTpCompliance": gfpTpCompliance,
       "gfpTpGroups": gfpTpGroups,
       "gfpTpGroup": gfpTpGroup}
)
