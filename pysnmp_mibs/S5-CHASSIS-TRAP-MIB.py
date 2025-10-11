# SNMP MIB module (S5-CHASSIS-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/S5-CHASSIS-TRAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:19:44 2025
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

(s5ChasComOperState,
 s5ChasComType,
 s5ChasNotifyFanDirection) = mibBuilder.importSymbols(
    "S5-CHASSIS-MIB",
    "s5ChasComOperState",
    "s5ChasComType",
    "s5ChasNotifyFanDirection")

(s5ChaTrap,) = mibBuilder.importSymbols(
    "S5-ROOT-MIB",
    "s5ChaTrap")

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

s5ChassisTrapMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 0)
)
if mibBuilder.loadTexts:
    s5ChassisTrapMib.setRevisions(
        ("2011-04-15 00:00",
         "2011-03-29 00:00",
         "2009-07-29 00:00",
         "2004-07-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

s5CtrNewHotSwap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 0, 1)
)
s5CtrNewHotSwap.setObjects(
      *(("S5-CHASSIS-MIB", "s5ChasComType"),
        ("S5-CHASSIS-MIB", "s5ChasComOperState"))
)
if mibBuilder.loadTexts:
    s5CtrNewHotSwap.setStatus(
        "current"
    )

s5CtrNewProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 0, 2)
)
s5CtrNewProblem.setObjects(
      *(("S5-CHASSIS-MIB", "s5ChasComType"),
        ("S5-CHASSIS-MIB", "s5ChasComOperState"))
)
if mibBuilder.loadTexts:
    s5CtrNewProblem.setStatus(
        "current"
    )

s5CtrNewUnitUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 0, 3)
)
s5CtrNewUnitUp.setObjects(
      *(("S5-CHASSIS-MIB", "s5ChasComType"),
        ("S5-CHASSIS-MIB", "s5ChasComOperState"))
)
if mibBuilder.loadTexts:
    s5CtrNewUnitUp.setStatus(
        "current"
    )

s5CtrNewUnitDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 0, 4)
)
s5CtrNewUnitDown.setObjects(
      *(("S5-CHASSIS-MIB", "s5ChasComType"),
        ("S5-CHASSIS-MIB", "s5ChasComOperState"))
)
if mibBuilder.loadTexts:
    s5CtrNewUnitDown.setStatus(
        "current"
    )

s5CtrFanRotationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 0, 5)
)
s5CtrFanRotationError.setObjects(
      *(("S5-CHASSIS-MIB", "s5ChasComType"),
        ("S5-CHASSIS-MIB", "s5ChasComOperState"))
)
if mibBuilder.loadTexts:
    s5CtrFanRotationError.setStatus(
        "current"
    )

s5CtrFanDirectionError = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 0, 6)
)
s5CtrFanDirectionError.setObjects(
      *(("S5-CHASSIS-MIB", "s5ChasComType"),
        ("S5-CHASSIS-MIB", "s5ChasComOperState"),
        ("S5-CHASSIS-MIB", "s5ChasNotifyFanDirection"))
)
if mibBuilder.loadTexts:
    s5CtrFanDirectionError.setStatus(
        "current"
    )

s5CtrHighTemperatureError = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 0, 7)
)
s5CtrHighTemperatureError.setObjects(
      *(("S5-CHASSIS-MIB", "s5ChasComType"),
        ("S5-CHASSIS-MIB", "s5ChasComOperState"))
)
if mibBuilder.loadTexts:
    s5CtrHighTemperatureError.setStatus(
        "current"
    )

s5CtrHotSwap = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 1)
)
s5CtrHotSwap.setObjects(
      *(("S5-CHASSIS-MIB", "s5ChasComType"),
        ("S5-CHASSIS-MIB", "s5ChasComOperState"))
)
if mibBuilder.loadTexts:
    s5CtrHotSwap.setStatus(
        "current"
    )

s5CtrProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 2)
)
s5CtrProblem.setObjects(
      *(("S5-CHASSIS-MIB", "s5ChasComType"),
        ("S5-CHASSIS-MIB", "s5ChasComOperState"))
)
if mibBuilder.loadTexts:
    s5CtrProblem.setStatus(
        "current"
    )

s5CtrUnitUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 3)
)
s5CtrUnitUp.setObjects(
      *(("S5-CHASSIS-MIB", "s5ChasComType"),
        ("S5-CHASSIS-MIB", "s5ChasComOperState"))
)
if mibBuilder.loadTexts:
    s5CtrUnitUp.setStatus(
        "current"
    )

s5CtrUnitDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 4, 4)
)
s5CtrUnitDown.setObjects(
      *(("S5-CHASSIS-MIB", "s5ChasComType"),
        ("S5-CHASSIS-MIB", "s5ChasComOperState"))
)
if mibBuilder.loadTexts:
    s5CtrUnitDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "S5-CHASSIS-TRAP-MIB",
    **{"s5ChassisTrapMib": s5ChassisTrapMib,
       "s5CtrNewHotSwap": s5CtrNewHotSwap,
       "s5CtrNewProblem": s5CtrNewProblem,
       "s5CtrNewUnitUp": s5CtrNewUnitUp,
       "s5CtrNewUnitDown": s5CtrNewUnitDown,
       "s5CtrFanRotationError": s5CtrFanRotationError,
       "s5CtrFanDirectionError": s5CtrFanDirectionError,
       "s5CtrHighTemperatureError": s5CtrHighTemperatureError,
       "s5CtrHotSwap": s5CtrHotSwap,
       "s5CtrProblem": s5CtrProblem,
       "s5CtrUnitUp": s5CtrUnitUp,
       "s5CtrUnitDown": s5CtrUnitDown}
)
