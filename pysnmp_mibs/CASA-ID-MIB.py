# SNMP MIB module (CASA-ID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/casa/CASA-ID-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:00:20 2025
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

(casa,) = mibBuilder.importSymbols(
    "CASA-MIB",
    "casa")

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

casaIdMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 2)
)
if mibBuilder.loadTexts:
    casaIdMib.setRevisions(
        ("1900-04-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Casa2100System_ObjectIdentity = ObjectIdentity
casa2100System = _Casa2100System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 2, 1)
)
_Casa2200System_ObjectIdentity = ObjectIdentity
casa2200System = _Casa2200System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 2, 20)
)
_Casa2300System_ObjectIdentity = ObjectIdentity
casa2300System = _Casa2300System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 2, 30)
)
_Casa2800System_ObjectIdentity = ObjectIdentity
casa2800System = _Casa2800System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 2, 40)
)
_Casa3000System_ObjectIdentity = ObjectIdentity
casa3000System = _Casa3000System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 2, 50)
)
_Casa6000System_ObjectIdentity = ObjectIdentity
casa6000System = _Casa6000System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 2, 100)
)
_Casa10000System_ObjectIdentity = ObjectIdentity
casa10000System = _Casa10000System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 2, 200)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CASA-ID-MIB",
    **{"casaIdMib": casaIdMib,
       "casa2100System": casa2100System,
       "casa2200System": casa2200System,
       "casa2300System": casa2300System,
       "casa2800System": casa2800System,
       "casa3000System": casa3000System,
       "casa6000System": casa6000System,
       "casa10000System": casa10000System}
)
