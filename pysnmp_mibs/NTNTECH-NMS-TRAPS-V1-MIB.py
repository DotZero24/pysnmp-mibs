# SNMP MIB module (NTNTECH-NMS-TRAPS-V1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zhone/NTNTECH-NMS-TRAPS-V1-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:12:07 2025
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

(mumStaFanState,) = mibBuilder.importSymbols(
    "NTNTECH-CHASSIS-STATUS-MIB",
    "mumStaFanState")

(ifStaSlotIndex,
 ifStaType) = mibBuilder.importSymbols(
    "NTNTECH-INTERFACE-MODULE-STATUS-MIB",
    "ifStaSlotIndex",
    "ifStaType")

(ntntechNMSTraps,) = mibBuilder.importSymbols(
    "NTNTECH-ROOT-MIB",
    "ntntechNMSTraps")

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

envFanTrap_v1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8059, 1, 3, 0, 1001)
)
envFanTrap_v1.setObjects(
    ("NTNTECH-CHASSIS-STATUS-MIB", "mumStaFanState")
)
if mibBuilder.loadTexts:
    envFanTrap_v1.setStatus(
        ""
    )

envTempNormal_v1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8059, 1, 3, 0, 1002)
)
if mibBuilder.loadTexts:
    envTempNormal_v1.setStatus(
        ""
    )

envTempExceeded_v1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8059, 1, 3, 0, 1003)
)
if mibBuilder.loadTexts:
    envTempExceeded_v1.setStatus(
        ""
    )

invIfModPresentTrap_v1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8059, 1, 3, 0, 2001)
)
invIfModPresentTrap_v1.setObjects(
      *(("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaSlotIndex"),
        ("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaType"))
)
if mibBuilder.loadTexts:
    invIfModPresentTrap_v1.setStatus(
        ""
    )

invIfModRemovedTrap_v1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8059, 1, 3, 0, 2002)
)
invIfModRemovedTrap_v1.setObjects(
      *(("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaSlotIndex"),
        ("NTNTECH-INTERFACE-MODULE-STATUS-MIB", "ifStaType"))
)
if mibBuilder.loadTexts:
    invIfModRemovedTrap_v1.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTNTECH-NMS-TRAPS-V1-MIB",
    **{"envFanTrap-v1": envFanTrap_v1,
       "envTempNormal-v1": envTempNormal_v1,
       "envTempExceeded-v1": envTempExceeded_v1,
       "invIfModPresentTrap-v1": invIfModPresentTrap_v1,
       "invIfModRemovedTrap-v1": invIfModRemovedTrap_v1}
)
