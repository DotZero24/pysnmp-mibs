# SNMP MIB module (HMIT-SW-PORT-STORM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HMIT-SW-PORT-STORM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:52:06 2025
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

(hmITSwitchTech,) = mibBuilder.importSymbols(
    "HMIT-SMI",
    "hmITSwitchTech")

(hmITSwPortMIB,) = mibBuilder.importSymbols(
    "HMIT-SW-PORT-MGR-MIB",
    "hmITSwPortMIB")

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

hmITPortStorm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 7)
)
if mibBuilder.loadTexts:
    hmITPortStorm.setRevisions(
        ("2010-01-08 17:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

portStorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 7, 1)
)
if mibBuilder.loadTexts:
    portStorm.setStatus(
        "current"
    )

portStormShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 7, 2)
)
if mibBuilder.loadTexts:
    portStormShutdown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HMIT-SW-PORT-STORM-MIB",
    **{"hmITPortStorm": hmITPortStorm,
       "portStorm": portStorm,
       "portStormShutdown": portStormShutdown}
)
