# SNMP MIB module (INFINERA-TP-CLEARCHANNELCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-CLEARCHANNELCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:23 2025
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
 InfnSMQ,
 InfnServiceMode,
 InfnServiceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
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

clearChannelCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9)
)
if mibBuilder.loadTexts:
    clearChannelCtpMIB.setRevisions(
        ("2008-02-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ClearChannelCtpTable_Object = MibTable
clearChannelCtpTable = _ClearChannelCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 1)
)
if mibBuilder.loadTexts:
    clearChannelCtpTable.setStatus("current")
_ClearChannelCtpEntry_Object = MibTableRow
clearChannelCtpEntry = _ClearChannelCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 1, 1)
)
clearChannelCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    clearChannelCtpEntry.setStatus("current")
_ClearChannelCtpSupportingCircuitIdList_Type = DisplayString
_ClearChannelCtpSupportingCircuitIdList_Object = MibTableColumn
clearChannelCtpSupportingCircuitIdList = _ClearChannelCtpSupportingCircuitIdList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 1, 1, 1),
    _ClearChannelCtpSupportingCircuitIdList_Type()
)
clearChannelCtpSupportingCircuitIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearChannelCtpSupportingCircuitIdList.setStatus("current")


class _ClearChannelCtpLoopback_Type(Integer32):
    """Custom type clearChannelCtpLoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("terminal", 2),
          ("facility", 3))
    )


_ClearChannelCtpLoopback_Type.__name__ = "Integer32"
_ClearChannelCtpLoopback_Object = MibTableColumn
clearChannelCtpLoopback = _ClearChannelCtpLoopback_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 1, 1, 2),
    _ClearChannelCtpLoopback_Type()
)
clearChannelCtpLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearChannelCtpLoopback.setStatus("current")


class _ClearChannelCtpPmHistStatsEnable_Type(Integer32):
    """Custom type clearChannelCtpPmHistStatsEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ClearChannelCtpPmHistStatsEnable_Type.__name__ = "Integer32"
_ClearChannelCtpPmHistStatsEnable_Object = MibTableColumn
clearChannelCtpPmHistStatsEnable = _ClearChannelCtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 1, 1, 3),
    _ClearChannelCtpPmHistStatsEnable_Type()
)
clearChannelCtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearChannelCtpPmHistStatsEnable.setStatus("obsolete")
_ClearChannelCtpConfiguredServiceType_Type = InfnServiceType
_ClearChannelCtpConfiguredServiceType_Object = MibTableColumn
clearChannelCtpConfiguredServiceType = _ClearChannelCtpConfiguredServiceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 1, 1, 4),
    _ClearChannelCtpConfiguredServiceType_Type()
)
clearChannelCtpConfiguredServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearChannelCtpConfiguredServiceType.setStatus("current")


class _ClearChannelCtpServiceMode_Type(InfnServiceMode):
    """Custom type clearChannelCtpServiceMode based on InfnServiceMode"""
    defaultValue = 1


_ClearChannelCtpServiceMode_Type.__name__ = "InfnServiceMode"
_ClearChannelCtpServiceMode_Object = MibTableColumn
clearChannelCtpServiceMode = _ClearChannelCtpServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 1, 1, 5),
    _ClearChannelCtpServiceMode_Type()
)
clearChannelCtpServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearChannelCtpServiceMode.setStatus("current")


class _ClearChannelCtpServiceModeQualifier_Type(InfnSMQ):
    """Custom type clearChannelCtpServiceModeQualifier based on InfnSMQ"""
    defaultValue = 1


_ClearChannelCtpServiceModeQualifier_Type.__name__ = "InfnSMQ"
_ClearChannelCtpServiceModeQualifier_Object = MibTableColumn
clearChannelCtpServiceModeQualifier = _ClearChannelCtpServiceModeQualifier_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 1, 1, 6),
    _ClearChannelCtpServiceModeQualifier_Type()
)
clearChannelCtpServiceModeQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clearChannelCtpServiceModeQualifier.setStatus("current")
_ClearChannelCtpConformance_ObjectIdentity = ObjectIdentity
clearChannelCtpConformance = _ClearChannelCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 3)
)
_ClearChannelCtpCompliances_ObjectIdentity = ObjectIdentity
clearChannelCtpCompliances = _ClearChannelCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 3, 1)
)
_ClearChannelCtpGroups_ObjectIdentity = ObjectIdentity
clearChannelCtpGroups = _ClearChannelCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 3, 2)
)

# Managed Objects groups

clearChannelCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 3, 2, 1)
)
clearChannelCtpGroup.setObjects(
      *(("INFINERA-TP-CLEARCHANNELCTP-MIB", "clearChannelCtpSupportingCircuitIdList"),
        ("INFINERA-TP-CLEARCHANNELCTP-MIB", "clearChannelCtpLoopback"),
        ("INFINERA-TP-CLEARCHANNELCTP-MIB", "clearChannelCtpPmHistStatsEnable"),
        ("INFINERA-TP-CLEARCHANNELCTP-MIB", "clearChannelCtpConfiguredServiceType"),
        ("INFINERA-TP-CLEARCHANNELCTP-MIB", "clearChannelCtpServiceMode"),
        ("INFINERA-TP-CLEARCHANNELCTP-MIB", "clearChannelCtpServiceModeQualifier"))
)
if mibBuilder.loadTexts:
    clearChannelCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

clearChannelCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 9, 3, 1, 1)
)
clearChannelCtpCompliance.setObjects(
    ("INFINERA-TP-CLEARCHANNELCTP-MIB", "clearChannelCtpGroup")
)
if mibBuilder.loadTexts:
    clearChannelCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-CLEARCHANNELCTP-MIB",
    **{"clearChannelCtpMIB": clearChannelCtpMIB,
       "clearChannelCtpTable": clearChannelCtpTable,
       "clearChannelCtpEntry": clearChannelCtpEntry,
       "clearChannelCtpSupportingCircuitIdList": clearChannelCtpSupportingCircuitIdList,
       "clearChannelCtpLoopback": clearChannelCtpLoopback,
       "clearChannelCtpPmHistStatsEnable": clearChannelCtpPmHistStatsEnable,
       "clearChannelCtpConfiguredServiceType": clearChannelCtpConfiguredServiceType,
       "clearChannelCtpServiceMode": clearChannelCtpServiceMode,
       "clearChannelCtpServiceModeQualifier": clearChannelCtpServiceModeQualifier,
       "clearChannelCtpConformance": clearChannelCtpConformance,
       "clearChannelCtpCompliances": clearChannelCtpCompliances,
       "clearChannelCtpCompliance": clearChannelCtpCompliance,
       "clearChannelCtpGroups": clearChannelCtpGroups,
       "clearChannelCtpGroup": clearChannelCtpGroup}
)
