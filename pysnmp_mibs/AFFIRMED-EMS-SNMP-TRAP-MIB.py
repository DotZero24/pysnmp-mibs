# SNMP MIB module (AFFIRMED-EMS-SNMP-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsoft/AFFIRMED-EMS-SNMP-TRAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:42 2025
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

(affirmedAlarmChassisName,
 affirmedAlarmDateTime,
 affirmedAlarmDetails,
 affirmedAlarmRefSeqId,
 affirmedAlarmSeqId,
 affirmedAlarmSeverity,
 affirmedAlarmSourceId) = mibBuilder.importSymbols(
    "AFFIRMED-ALARM-MIB",
    "affirmedAlarmChassisName",
    "affirmedAlarmDateTime",
    "affirmedAlarmDetails",
    "affirmedAlarmRefSeqId",
    "affirmedAlarmSeqId",
    "affirmedAlarmSeverity",
    "affirmedAlarmSourceId")

(affirmedSnmp,
 affirmedSnmpNotifications) = mibBuilder.importSymbols(
    "AFFIRMED-SNMP-MIB",
    "affirmedSnmp",
    "affirmedSnmpNotifications")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

affirmedSnmpTraps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AffirmedSnmpTrapsScalars_ObjectIdentity = ObjectIdentity
affirmedSnmpTrapsScalars = _AffirmedSnmpTrapsScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 5, 1)
)
_AffirmedSnmpTrapsTables_ObjectIdentity = ObjectIdentity
affirmedSnmpTrapsTables = _AffirmedSnmpTrapsTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 5, 2)
)
_AffirmedSnmpTrapsNotifications_ObjectIdentity = ObjectIdentity
affirmedSnmpTrapsNotifications = _AffirmedSnmpTrapsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 5, 3)
)
_AffirmedSnmpTrapsNotificationPrefix_ObjectIdentity = ObjectIdentity
affirmedSnmpTrapsNotificationPrefix = _AffirmedSnmpTrapsNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 5, 3, 0)
)
_AffirmedSnmpTrapsNotificationObjects_ObjectIdentity = ObjectIdentity
affirmedSnmpTrapsNotificationObjects = _AffirmedSnmpTrapsNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 5, 3, 1)
)

# Managed Objects groups


# Notification objects

emsDBReplicationDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 5, 3, 0, 1)
)
emsDBReplicationDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"))
)
if mibBuilder.loadTexts:
    emsDBReplicationDown.setStatus(
        "current"
    )

emsDBReplicationLagBehind = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 5, 3, 0, 2)
)
emsDBReplicationLagBehind.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"))
)
if mibBuilder.loadTexts:
    emsDBReplicationLagBehind.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AFFIRMED-EMS-SNMP-TRAP-MIB",
    **{"affirmedSnmpTraps": affirmedSnmpTraps,
       "affirmedSnmpTrapsScalars": affirmedSnmpTrapsScalars,
       "affirmedSnmpTrapsTables": affirmedSnmpTrapsTables,
       "affirmedSnmpTrapsNotifications": affirmedSnmpTrapsNotifications,
       "affirmedSnmpTrapsNotificationPrefix": affirmedSnmpTrapsNotificationPrefix,
       "emsDBReplicationDown": emsDBReplicationDown,
       "emsDBReplicationLagBehind": emsDBReplicationLagBehind,
       "affirmedSnmpTrapsNotificationObjects": affirmedSnmpTrapsNotificationObjects}
)
