# SNMP MIB module (CENTRECOM-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/allied-old/CENTRECOM-TRAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:12:11 2025
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

(extSwitchMIB,) = mibBuilder.importSymbols(
    "CENTRECOM-MIB",
    "extSwitchMIB")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysDescr,
 sysUpTime) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr",
    "sysUpTime")

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


# Managed Objects groups


# Notification objects

overheat = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 0, 6)
)
overheat.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    overheat.setStatus(
        ""
    )

fanfailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 0, 7)
)
fanfailed.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    fanfailed.setStatus(
        ""
    )

fanOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 0, 8)
)
fanOK.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    fanOK.setStatus(
        ""
    )

invalidLoginAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 0, 9)
)
invalidLoginAttempt.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    invalidLoginAttempt.setStatus(
        ""
    )

powerSupplyFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 0, 10)
)
powerSupplyFail.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    powerSupplyFail.setStatus(
        ""
    )

powerSupplyGood = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 0, 11)
)
powerSupplyGood.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    powerSupplyGood.setStatus(
        ""
    )

rpsAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 0, 12)
)
rpsAlarm.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    rpsAlarm.setStatus(
        ""
    )

rpsNoAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 0, 13)
)
rpsNoAlarm.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("SNMPv2-MIB", "sysDescr"))
)
if mibBuilder.loadTexts:
    rpsNoAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTRECOM-TRAP-MIB",
    **{"overheat": overheat,
       "fanfailed": fanfailed,
       "fanOK": fanOK,
       "invalidLoginAttempt": invalidLoginAttempt,
       "powerSupplyFail": powerSupplyFail,
       "powerSupplyGood": powerSupplyGood,
       "rpsAlarm": rpsAlarm,
       "rpsNoAlarm": rpsNoAlarm}
)
