# SNMP MIB module (QTECH-TEMP-FAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-TEMP-FAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:15 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(qtechSystemTemperatureCurrent,) = mibBuilder.importSymbols(
    "QTECH-SYSTEM-MIB",
    "qtechSystemTemperatureCurrent")

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

qtechTempFanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 109)
)
if mibBuilder.loadTexts:
    qtechTempFanMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechTempFanTraps_ObjectIdentity = ObjectIdentity
qtechTempFanTraps = _QtechTempFanTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 109, 1)
)

# Managed Objects groups


# Notification objects

temperatureTooHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 109, 1, 1)
)
temperatureTooHighTrap.setObjects(
    ("QTECH-SYSTEM-MIB", "qtechSystemTemperatureCurrent")
)
if mibBuilder.loadTexts:
    temperatureTooHighTrap.setStatus(
        "current"
    )

temperTooHighRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 109, 1, 2)
)
temperTooHighRecovTrap.setObjects(
    ("QTECH-SYSTEM-MIB", "qtechSystemTemperatureCurrent")
)
if mibBuilder.loadTexts:
    temperTooHighRecovTrap.setStatus(
        "current"
    )

fanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 109, 1, 3)
)
if mibBuilder.loadTexts:
    fanFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-TEMP-FAN-MIB",
    **{"qtechTempFanMIB": qtechTempFanMIB,
       "qtechTempFanTraps": qtechTempFanTraps,
       "temperatureTooHighTrap": temperatureTooHighTrap,
       "temperTooHighRecovTrap": temperTooHighRecovTrap,
       "fanFailure": fanFailure}
)
