# SNMP MIB module (INFINERA-TP-GFPCLIENTCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-GFPCLIENTCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:18 2025
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
 InfnSMQ,
 InfnServiceMode,
 InfnServiceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnGFPPayloadFCS",
    "InfnGFPState",
    "InfnGfpExtHdrTyp",
    "InfnSMQ",
    "InfnServiceMode",
    "InfnServiceType")

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

gfpclientCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32)
)
if mibBuilder.loadTexts:
    gfpclientCtpMIB.setRevisions(
        ("2011-04-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GfpclientCtpTable_Object = MibTable
gfpclientCtpTable = _GfpclientCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 1)
)
if mibBuilder.loadTexts:
    gfpclientCtpTable.setStatus("current")
_GfpclientCtpEntry_Object = MibTableRow
gfpclientCtpEntry = _GfpclientCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 1, 1)
)
gfpclientCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gfpclientCtpEntry.setStatus("current")


class _GfpclientCtpServiceMode_Type(InfnServiceMode):
    """Custom type gfpclientCtpServiceMode based on InfnServiceMode"""
    defaultValue = 1


_GfpclientCtpServiceMode_Type.__name__ = "InfnServiceMode"
_GfpclientCtpServiceMode_Object = MibTableColumn
gfpclientCtpServiceMode = _GfpclientCtpServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 1, 1, 1),
    _GfpclientCtpServiceMode_Type()
)
gfpclientCtpServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpclientCtpServiceMode.setStatus("current")


class _GfpclientCtpServiceModeQualifier_Type(InfnSMQ):
    """Custom type gfpclientCtpServiceModeQualifier based on InfnSMQ"""
    defaultValue = 1


_GfpclientCtpServiceModeQualifier_Type.__name__ = "InfnSMQ"
_GfpclientCtpServiceModeQualifier_Object = MibTableColumn
gfpclientCtpServiceModeQualifier = _GfpclientCtpServiceModeQualifier_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 1, 1, 2),
    _GfpclientCtpServiceModeQualifier_Type()
)
gfpclientCtpServiceModeQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpclientCtpServiceModeQualifier.setStatus("current")


class _GfpclientCtpConfigServiceType_Type(InfnServiceType):
    """Custom type gfpclientCtpConfigServiceType based on InfnServiceType"""
    defaultValue = 99


_GfpclientCtpConfigServiceType_Type.__name__ = "InfnServiceType"
_GfpclientCtpConfigServiceType_Object = MibTableColumn
gfpclientCtpConfigServiceType = _GfpclientCtpConfigServiceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 1, 1, 3),
    _GfpclientCtpConfigServiceType_Type()
)
gfpclientCtpConfigServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpclientCtpConfigServiceType.setStatus("current")


class _GfpclientCtpPayloadFCS_Type(InfnGFPPayloadFCS):
    """Custom type gfpclientCtpPayloadFCS based on InfnGFPPayloadFCS"""
    defaultValue = 2


_GfpclientCtpPayloadFCS_Type.__name__ = "InfnGFPPayloadFCS"
_GfpclientCtpPayloadFCS_Object = MibTableColumn
gfpclientCtpPayloadFCS = _GfpclientCtpPayloadFCS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 1, 1, 4),
    _GfpclientCtpPayloadFCS_Type()
)
gfpclientCtpPayloadFCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gfpclientCtpPayloadFCS.setStatus("current")
_GfpclientCtpGFPState_Type = InfnGFPState
_GfpclientCtpGFPState_Object = MibTableColumn
gfpclientCtpGFPState = _GfpclientCtpGFPState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 1, 1, 5),
    _GfpclientCtpGFPState_Type()
)
gfpclientCtpGFPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpclientCtpGFPState.setStatus("current")


class _GfpclientCtpExtHeaderType_Type(InfnGfpExtHdrTyp):
    """Custom type gfpclientCtpExtHeaderType based on InfnGfpExtHdrTyp"""
    defaultValue = 1


_GfpclientCtpExtHeaderType_Type.__name__ = "InfnGfpExtHdrTyp"
_GfpclientCtpExtHeaderType_Object = MibTableColumn
gfpclientCtpExtHeaderType = _GfpclientCtpExtHeaderType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 1, 1, 6),
    _GfpclientCtpExtHeaderType_Type()
)
gfpclientCtpExtHeaderType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gfpclientCtpExtHeaderType.setStatus("current")


class _GfpclientCtpChannelId_Type(Integer32):
    """Custom type gfpclientCtpChannelId based on Integer32"""
    defaultValue = 0


_GfpclientCtpChannelId_Type.__name__ = "Integer32"
_GfpclientCtpChannelId_Object = MibTableColumn
gfpclientCtpChannelId = _GfpclientCtpChannelId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 1, 1, 7),
    _GfpclientCtpChannelId_Type()
)
gfpclientCtpChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gfpclientCtpChannelId.setStatus("current")
_GfpclientCtpConformance_ObjectIdentity = ObjectIdentity
gfpclientCtpConformance = _GfpclientCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 3)
)
_GfpclientCtpCompliances_ObjectIdentity = ObjectIdentity
gfpclientCtpCompliances = _GfpclientCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 3, 1)
)
_GfpclientCtpGroups_ObjectIdentity = ObjectIdentity
gfpclientCtpGroups = _GfpclientCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 3, 2)
)

# Managed Objects groups

gfpclientCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 3, 2, 1)
)
gfpclientCtpGroup.setObjects(
      *(("INFINERA-TP-GFPCLIENTCTP-MIB", "gfpclientCtpServiceMode"),
        ("INFINERA-TP-GFPCLIENTCTP-MIB", "gfpclientCtpServiceModeQualifier"),
        ("INFINERA-TP-GFPCLIENTCTP-MIB", "gfpclientCtpConfigServiceType"),
        ("INFINERA-TP-GFPCLIENTCTP-MIB", "gfpclientCtpPayloadFCS"),
        ("INFINERA-TP-GFPCLIENTCTP-MIB", "gfpclientCtpGFPState"),
        ("INFINERA-TP-GFPCLIENTCTP-MIB", "gfpclientCtpExtHeaderType"),
        ("INFINERA-TP-GFPCLIENTCTP-MIB", "gfpclientCtpChannelId"))
)
if mibBuilder.loadTexts:
    gfpclientCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

gfpclientCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 32, 3, 1, 1)
)
gfpclientCtpCompliance.setObjects(
    ("INFINERA-TP-GFPCLIENTCTP-MIB", "gfpclientCtpGroup")
)
if mibBuilder.loadTexts:
    gfpclientCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-GFPCLIENTCTP-MIB",
    **{"gfpclientCtpMIB": gfpclientCtpMIB,
       "gfpclientCtpTable": gfpclientCtpTable,
       "gfpclientCtpEntry": gfpclientCtpEntry,
       "gfpclientCtpServiceMode": gfpclientCtpServiceMode,
       "gfpclientCtpServiceModeQualifier": gfpclientCtpServiceModeQualifier,
       "gfpclientCtpConfigServiceType": gfpclientCtpConfigServiceType,
       "gfpclientCtpPayloadFCS": gfpclientCtpPayloadFCS,
       "gfpclientCtpGFPState": gfpclientCtpGFPState,
       "gfpclientCtpExtHeaderType": gfpclientCtpExtHeaderType,
       "gfpclientCtpChannelId": gfpclientCtpChannelId,
       "gfpclientCtpConformance": gfpclientCtpConformance,
       "gfpclientCtpCompliances": gfpclientCtpCompliances,
       "gfpclientCtpCompliance": gfpclientCtpCompliance,
       "gfpclientCtpGroups": gfpclientCtpGroups,
       "gfpclientCtpGroup": gfpclientCtpGroup}
)
