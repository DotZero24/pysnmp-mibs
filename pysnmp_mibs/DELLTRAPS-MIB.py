# SNMP MIB module (DELLTRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dell/DELLTRAPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:09:21 2025
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

(connUnitEventDescr,
 connUnitEventId,
 connUnitEventType) = mibBuilder.importSymbols(
    "FCMGMT-MIB",
    "connUnitEventDescr",
    "connUnitEventId",
    "connUnitEventType")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)

# Managed Objects groups


# Notification objects

dellEventInfoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 0, 1)
)
dellEventInfoTrap.setObjects(
      *(("FCMGMT-MIB", "connUnitEventId"),
        ("FCMGMT-MIB", "connUnitEventType"),
        ("FCMGMT-MIB", "connUnitEventDescr"))
)
if mibBuilder.loadTexts:
    dellEventInfoTrap.setStatus(
        ""
    )

dellEventWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 0, 2)
)
dellEventWarningTrap.setObjects(
      *(("FCMGMT-MIB", "connUnitEventId"),
        ("FCMGMT-MIB", "connUnitEventType"),
        ("FCMGMT-MIB", "connUnitEventDescr"))
)
if mibBuilder.loadTexts:
    dellEventWarningTrap.setStatus(
        ""
    )

dellEventErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 0, 3)
)
dellEventErrorTrap.setObjects(
      *(("FCMGMT-MIB", "connUnitEventId"),
        ("FCMGMT-MIB", "connUnitEventType"),
        ("FCMGMT-MIB", "connUnitEventDescr"))
)
if mibBuilder.loadTexts:
    dellEventErrorTrap.setStatus(
        ""
    )

dellEventCriticalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 0, 4)
)
dellEventCriticalTrap.setObjects(
      *(("FCMGMT-MIB", "connUnitEventId"),
        ("FCMGMT-MIB", "connUnitEventType"),
        ("FCMGMT-MIB", "connUnitEventDescr"))
)
if mibBuilder.loadTexts:
    dellEventCriticalTrap.setStatus(
        ""
    )

dellEventResolvedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 0, 5)
)
dellEventResolvedTrap.setObjects(
      *(("FCMGMT-MIB", "connUnitEventId"),
        ("FCMGMT-MIB", "connUnitEventType"),
        ("FCMGMT-MIB", "connUnitEventDescr"))
)
if mibBuilder.loadTexts:
    dellEventResolvedTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELLTRAPS-MIB",
    **{"dell": dell,
       "dellEventInfoTrap": dellEventInfoTrap,
       "dellEventWarningTrap": dellEventWarningTrap,
       "dellEventErrorTrap": dellEventErrorTrap,
       "dellEventCriticalTrap": dellEventCriticalTrap,
       "dellEventResolvedTrap": dellEventResolvedTrap}
)
