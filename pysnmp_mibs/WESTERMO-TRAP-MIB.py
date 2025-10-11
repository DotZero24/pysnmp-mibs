# SNMP MIB module (WESTERMO-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/westermo/WESTERMO-TRAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:21 2025
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

notification = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 200)
)
if mibBuilder.loadTexts:
    notification.setRevisions(
        ("2019-09-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RtTraps_ObjectIdentity = ObjectIdentity
rtTraps = _RtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 0)
)
_RtTrapMsg_ObjectIdentity = ObjectIdentity
rtTrapMsg = _RtTrapMsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 1)
)


class _TrapMsgString_Type(DisplayString):
    """Custom type trapMsgString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_TrapMsgString_Type.__name__ = "DisplayString"
_TrapMsgString_Object = MibScalar
trapMsgString = _TrapMsgString_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 1, 1),
    _TrapMsgString_Type()
)
trapMsgString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapMsgString.setStatus("current")
_RtTrapConformance_ObjectIdentity = ObjectIdentity
rtTrapConformance = _RtTrapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 3)
)
_RtTrapGroups_ObjectIdentity = ObjectIdentity
rtTrapGroups = _RtTrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 3, 1)
)
_RtTrapCompliances_ObjectIdentity = ObjectIdentity
rtTrapCompliances = _RtTrapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 3, 2)
)

# Managed Objects groups

rtTrapMsgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 3, 1, 1)
)
rtTrapMsgGroup.setObjects(
    ("WESTERMO-TRAP-MIB", "trapMsgString")
)
if mibBuilder.loadTexts:
    rtTrapMsgGroup.setStatus("current")


# Notification objects

notifyEmergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 0, 1)
)
notifyEmergency.setObjects(
    ("WESTERMO-TRAP-MIB", "trapMsgString")
)
if mibBuilder.loadTexts:
    notifyEmergency.setStatus(
        "current"
    )

notifyAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 0, 2)
)
notifyAlert.setObjects(
    ("WESTERMO-TRAP-MIB", "trapMsgString")
)
if mibBuilder.loadTexts:
    notifyAlert.setStatus(
        "current"
    )

notifyCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 0, 3)
)
notifyCritical.setObjects(
    ("WESTERMO-TRAP-MIB", "trapMsgString")
)
if mibBuilder.loadTexts:
    notifyCritical.setStatus(
        "current"
    )

notifyError = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 0, 4)
)
notifyError.setObjects(
    ("WESTERMO-TRAP-MIB", "trapMsgString")
)
if mibBuilder.loadTexts:
    notifyError.setStatus(
        "current"
    )

notifyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 0, 5)
)
notifyWarning.setObjects(
    ("WESTERMO-TRAP-MIB", "trapMsgString")
)
if mibBuilder.loadTexts:
    notifyWarning.setStatus(
        "current"
    )

notifyNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 0, 6)
)
notifyNotice.setObjects(
    ("WESTERMO-TRAP-MIB", "trapMsgString")
)
if mibBuilder.loadTexts:
    notifyNotice.setStatus(
        "current"
    )

notifyInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 0, 7)
)
notifyInfo.setObjects(
    ("WESTERMO-TRAP-MIB", "trapMsgString")
)
if mibBuilder.loadTexts:
    notifyInfo.setStatus(
        "current"
    )


# Notifications groups

rtTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 3, 1, 2)
)
rtTrapGroup.setObjects(
      *(("WESTERMO-TRAP-MIB", "notifyEmergency"),
        ("WESTERMO-TRAP-MIB", "notifyAlert"),
        ("WESTERMO-TRAP-MIB", "notifyCritical"),
        ("WESTERMO-TRAP-MIB", "notifyError"),
        ("WESTERMO-TRAP-MIB", "notifyWarning"),
        ("WESTERMO-TRAP-MIB", "notifyNotice"),
        ("WESTERMO-TRAP-MIB", "notifyInfo"))
)
if mibBuilder.loadTexts:
    rtTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rttrapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 3, 2, 1)
)
rttrapCompliance.setObjects(
      *(("WESTERMO-TRAP-MIB", "rtTrapMsgGroup"),
        ("WESTERMO-TRAP-MIB", "rtTrapGroup"))
)
if mibBuilder.loadTexts:
    rttrapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WESTERMO-TRAP-MIB",
    **{"notification": notification,
       "rtTraps": rtTraps,
       "notifyEmergency": notifyEmergency,
       "notifyAlert": notifyAlert,
       "notifyCritical": notifyCritical,
       "notifyError": notifyError,
       "notifyWarning": notifyWarning,
       "notifyNotice": notifyNotice,
       "notifyInfo": notifyInfo,
       "rtTrapMsg": rtTrapMsg,
       "trapMsgString": trapMsgString,
       "rtTrapConformance": rtTrapConformance,
       "rtTrapGroups": rtTrapGroups,
       "rtTrapMsgGroup": rtTrapMsgGroup,
       "rtTrapGroup": rtTrapGroup,
       "rtTrapCompliances": rtTrapCompliances,
       "rttrapCompliance": rttrapCompliance}
)
