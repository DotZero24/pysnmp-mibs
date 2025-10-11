# SNMP MIB module (ONEACCESS-EVENTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/oneaccess/ONEACCESS-EVENTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:56 2025
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

(oacExpIMEvents,
 oacMIBModules,
 oneAccess) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMEvents",
    "oacMIBModules",
    "oneAccess")

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

oacEventsMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 6600)
)
if mibBuilder.loadTexts:
    oacEventsMIBModule.setRevisions(
        ("2011-06-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OacEventsObjects_ObjectIdentity = ObjectIdentity
oacEventsObjects = _OacEventsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1)
)
_OacEventText_Type = DisplayString
_OacEventText_Object = MibScalar
oacEventText = _OacEventText_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 1),
    _OacEventText_Type()
)
oacEventText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacEventText.setStatus("current")
_OacEventSeverityLevel_Type = ObjectIdentifier
_OacEventSeverityLevel_Object = MibScalar
oacEventSeverityLevel = _OacEventSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 2),
    _OacEventSeverityLevel_Type()
)
oacEventSeverityLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    oacEventSeverityLevel.setStatus("current")
_OacEventSeverity_ObjectIdentity = ObjectIdentity
oacEventSeverity = _OacEventSeverity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3)
)
_OacEventSeverityAlerts_ObjectIdentity = ObjectIdentity
oacEventSeverityAlerts = _OacEventSeverityAlerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 1)
)
_OacEventSeverityCritical_ObjectIdentity = ObjectIdentity
oacEventSeverityCritical = _OacEventSeverityCritical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 2)
)
_OacEventSeverityErrors_ObjectIdentity = ObjectIdentity
oacEventSeverityErrors = _OacEventSeverityErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 3)
)
_OacEventSeverityWarnings_ObjectIdentity = ObjectIdentity
oacEventSeverityWarnings = _OacEventSeverityWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 4)
)
_OacEventSeverityNotifications_ObjectIdentity = ObjectIdentity
oacEventSeverityNotifications = _OacEventSeverityNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 5)
)
_OacEventSeverityInformational_ObjectIdentity = ObjectIdentity
oacEventSeverityInformational = _OacEventSeverityInformational_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 6)
)
_OacEventSeverityDebug_ObjectIdentity = ObjectIdentity
oacEventSeverityDebug = _OacEventSeverityDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 7)
)
_OacEventsNotifications_ObjectIdentity = ObjectIdentity
oacEventsNotifications = _OacEventsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 2)
)
_OacEventsConformance_ObjectIdentity = ObjectIdentity
oacEventsConformance = _OacEventsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 3)
)
_OacEventsGroups_ObjectIdentity = ObjectIdentity
oacEventsGroups = _OacEventsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 3, 1)
)
_OacEventsCompliances_ObjectIdentity = ObjectIdentity
oacEventsCompliances = _OacEventsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 3, 2)
)

# Managed Objects groups

oacEventsGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 3, 1, 1)
)
oacEventsGeneralGroup.setObjects(
    ("ONEACCESS-EVENTS-MIB", "oacEventText")
)
if mibBuilder.loadTexts:
    oacEventsGeneralGroup.setStatus("current")


# Notification objects

oacEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 13191, 0, 1)
)
oacEvent.setObjects(
    ("ONEACCESS-EVENTS-MIB", "oacEventText")
)
if mibBuilder.loadTexts:
    oacEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance

oacEventsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 3, 2, 1)
)
oacEventsCompliance.setObjects(
    ("ONEACCESS-EVENTS-MIB", "oacEventsGeneralGroup")
)
if mibBuilder.loadTexts:
    oacEventsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-EVENTS-MIB",
    **{"oacEvent": oacEvent,
       "oacEventsMIBModule": oacEventsMIBModule,
       "oacEventsObjects": oacEventsObjects,
       "oacEventText": oacEventText,
       "oacEventSeverityLevel": oacEventSeverityLevel,
       "oacEventSeverity": oacEventSeverity,
       "oacEventSeverityAlerts": oacEventSeverityAlerts,
       "oacEventSeverityCritical": oacEventSeverityCritical,
       "oacEventSeverityErrors": oacEventSeverityErrors,
       "oacEventSeverityWarnings": oacEventSeverityWarnings,
       "oacEventSeverityNotifications": oacEventSeverityNotifications,
       "oacEventSeverityInformational": oacEventSeverityInformational,
       "oacEventSeverityDebug": oacEventSeverityDebug,
       "oacEventsNotifications": oacEventsNotifications,
       "oacEventsConformance": oacEventsConformance,
       "oacEventsGroups": oacEventsGroups,
       "oacEventsGeneralGroup": oacEventsGeneralGroup,
       "oacEventsCompliances": oacEventsCompliances,
       "oacEventsCompliance": oacEventsCompliance}
)
