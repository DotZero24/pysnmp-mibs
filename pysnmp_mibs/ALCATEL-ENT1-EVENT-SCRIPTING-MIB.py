# SNMP MIB module (ALCATEL-ENT1-EVENT-SCRIPTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-EVENT-SCRIPTING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:08:46 2025
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

(softentIND1EventScripting,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "softentIND1EventScripting")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1EventScriptingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 86, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1EventScriptingObjects_ObjectIdentity = ObjectIdentity
alcatelIND1EventScriptingObjects = _AlcatelIND1EventScriptingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 86, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1EventScriptingObjects.setStatus("current")
_AlaEventActionGlobalConfigObjects_ObjectIdentity = ObjectIdentity
alaEventActionGlobalConfigObjects = _AlaEventActionGlobalConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 86, 1, 1, 1)
)


class _AlaEventActionGlobalScriptTimeLimit_Type(Unsigned32):
    """Custom type alaEventActionGlobalScriptTimeLimit based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 600),
    )


_AlaEventActionGlobalScriptTimeLimit_Type.__name__ = "Unsigned32"
_AlaEventActionGlobalScriptTimeLimit_Object = MibScalar
alaEventActionGlobalScriptTimeLimit = _AlaEventActionGlobalScriptTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 86, 1, 1, 1, 1),
    _AlaEventActionGlobalScriptTimeLimit_Type()
)
alaEventActionGlobalScriptTimeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaEventActionGlobalScriptTimeLimit.setStatus("current")
_AlaEventActionTable_Object = MibTable
alaEventActionTable = _AlaEventActionTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 86, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaEventActionTable.setStatus("current")
_AlaEventActionEntry_Object = MibTableRow
alaEventActionEntry = _AlaEventActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 86, 1, 1, 1, 2, 1)
)
alaEventActionEntry.setIndexNames(
    (0, "ALCATEL-ENT1-EVENT-SCRIPTING-MIB", "alaEventActionType"),
    (0, "ALCATEL-ENT1-EVENT-SCRIPTING-MIB", "alaEventActionName"),
)
if mibBuilder.loadTexts:
    alaEventActionEntry.setStatus("current")


class _AlaEventActionType_Type(Integer32):
    """Custom type alaEventActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("trap", 1)
    )


_AlaEventActionType_Type.__name__ = "Integer32"
_AlaEventActionType_Object = MibTableColumn
alaEventActionType = _AlaEventActionType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 86, 1, 1, 1, 2, 1, 1),
    _AlaEventActionType_Type()
)
alaEventActionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEventActionType.setStatus("current")


class _AlaEventActionName_Type(SnmpAdminString):
    """Custom type alaEventActionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AlaEventActionName_Type.__name__ = "SnmpAdminString"
_AlaEventActionName_Object = MibTableColumn
alaEventActionName = _AlaEventActionName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 86, 1, 1, 1, 2, 1, 2),
    _AlaEventActionName_Type()
)
alaEventActionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaEventActionName.setStatus("current")


class _AlaEventActionScriptPath_Type(SnmpAdminString):
    """Custom type alaEventActionScriptPath based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AlaEventActionScriptPath_Type.__name__ = "SnmpAdminString"
_AlaEventActionScriptPath_Object = MibTableColumn
alaEventActionScriptPath = _AlaEventActionScriptPath_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 86, 1, 1, 1, 2, 1, 3),
    _AlaEventActionScriptPath_Type()
)
alaEventActionScriptPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEventActionScriptPath.setStatus("current")
_AlaEventActionScriptLastChanged_Type = DateAndTime
_AlaEventActionScriptLastChanged_Object = MibTableColumn
alaEventActionScriptLastChanged = _AlaEventActionScriptLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 86, 1, 1, 1, 2, 1, 4),
    _AlaEventActionScriptLastChanged_Type()
)
alaEventActionScriptLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEventActionScriptLastChanged.setStatus("current")
_AlaEventActionScriptLastLaunched_Type = DateAndTime
_AlaEventActionScriptLastLaunched_Object = MibTableColumn
alaEventActionScriptLastLaunched = _AlaEventActionScriptLastLaunched_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 86, 1, 1, 1, 2, 1, 5),
    _AlaEventActionScriptLastLaunched_Type()
)
alaEventActionScriptLastLaunched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEventActionScriptLastLaunched.setStatus("current")
_AlaEventActionScriptLaunchCount_Type = Counter32
_AlaEventActionScriptLaunchCount_Object = MibTableColumn
alaEventActionScriptLaunchCount = _AlaEventActionScriptLaunchCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 86, 1, 1, 1, 2, 1, 6),
    _AlaEventActionScriptLaunchCount_Type()
)
alaEventActionScriptLaunchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaEventActionScriptLaunchCount.setStatus("current")
_AlaEventActionRowStatus_Type = RowStatus
_AlaEventActionRowStatus_Object = MibTableColumn
alaEventActionRowStatus = _AlaEventActionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 86, 1, 1, 1, 2, 1, 7),
    _AlaEventActionRowStatus_Type()
)
alaEventActionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaEventActionRowStatus.setStatus("current")
_AlcatelIND1EventScriptingMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1EventScriptingMIBConformance = _AlcatelIND1EventScriptingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 86, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1EventScriptingMIBConformance.setStatus("current")
_AlcatelIND1EventScriptingMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1EventScriptingMIBGroups = _AlcatelIND1EventScriptingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 86, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1EventScriptingMIBGroups.setStatus("current")
_AlcatelIND1EventScriptingMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1EventScriptingMIBCompliances = _AlcatelIND1EventScriptingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 86, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1EventScriptingMIBCompliances.setStatus("current")

# Managed Objects groups

eventActionGlobalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 86, 1, 2, 1, 1)
)
eventActionGlobalsGroup.setObjects(
    ("ALCATEL-ENT1-EVENT-SCRIPTING-MIB", "alaEventActionGlobalScriptTimeLimit")
)
if mibBuilder.loadTexts:
    eventActionGlobalsGroup.setStatus("current")

eventActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 86, 1, 2, 1, 2)
)
eventActionGroup.setObjects(
      *(("ALCATEL-ENT1-EVENT-SCRIPTING-MIB", "alaEventActionScriptPath"),
        ("ALCATEL-ENT1-EVENT-SCRIPTING-MIB", "alaEventActionScriptLastChanged"),
        ("ALCATEL-ENT1-EVENT-SCRIPTING-MIB", "alaEventActionScriptLastLaunched"),
        ("ALCATEL-ENT1-EVENT-SCRIPTING-MIB", "alaEventActionScriptLaunchCount"),
        ("ALCATEL-ENT1-EVENT-SCRIPTING-MIB", "alaEventActionRowStatus"))
)
if mibBuilder.loadTexts:
    eventActionGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1EventScriptingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 86, 1, 2, 2, 1)
)
alcatelIND1EventScriptingMIBCompliance.setObjects(
      *(("ALCATEL-ENT1-EVENT-SCRIPTING-MIB", "eventActionGlobalsGroup"),
        ("ALCATEL-ENT1-EVENT-SCRIPTING-MIB", "eventActionGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1EventScriptingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-EVENT-SCRIPTING-MIB",
    **{"alcatelIND1EventScriptingMIB": alcatelIND1EventScriptingMIB,
       "alcatelIND1EventScriptingObjects": alcatelIND1EventScriptingObjects,
       "alaEventActionGlobalConfigObjects": alaEventActionGlobalConfigObjects,
       "alaEventActionGlobalScriptTimeLimit": alaEventActionGlobalScriptTimeLimit,
       "alaEventActionTable": alaEventActionTable,
       "alaEventActionEntry": alaEventActionEntry,
       "alaEventActionType": alaEventActionType,
       "alaEventActionName": alaEventActionName,
       "alaEventActionScriptPath": alaEventActionScriptPath,
       "alaEventActionScriptLastChanged": alaEventActionScriptLastChanged,
       "alaEventActionScriptLastLaunched": alaEventActionScriptLastLaunched,
       "alaEventActionScriptLaunchCount": alaEventActionScriptLaunchCount,
       "alaEventActionRowStatus": alaEventActionRowStatus,
       "alcatelIND1EventScriptingMIBConformance": alcatelIND1EventScriptingMIBConformance,
       "alcatelIND1EventScriptingMIBGroups": alcatelIND1EventScriptingMIBGroups,
       "eventActionGlobalsGroup": eventActionGlobalsGroup,
       "eventActionGroup": eventActionGroup,
       "alcatelIND1EventScriptingMIBCompliances": alcatelIND1EventScriptingMIBCompliances,
       "alcatelIND1EventScriptingMIBCompliance": alcatelIND1EventScriptingMIBCompliance}
)
