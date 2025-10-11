# SNMP MIB module (NTWS-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/NTWS-ROOT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:21:14 2025
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

ntwsRootMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1)
)
if mibBuilder.loadTexts:
    ntwsRootMib.setRevisions(
        ("2007-08-15 00:04",
         "2006-03-31 00:03",
         "2005-04-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtwsProducts_ObjectIdentity = ObjectIdentity
ntwsProducts = _NtwsProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 1)
)
_NtwsTemporary_ObjectIdentity = ObjectIdentity
ntwsTemporary = _NtwsTemporary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2)
)
_NtwsRegistration_ObjectIdentity = ObjectIdentity
ntwsRegistration = _NtwsRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3)
)
_NtwsMibs_ObjectIdentity = ObjectIdentity
ntwsMibs = _NtwsMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4)
)
_NtwsTraps_ObjectIdentity = ObjectIdentity
ntwsTraps = _NtwsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTWS-ROOT-MIB",
    **{"ntwsRootMib": ntwsRootMib,
       "ntwsProducts": ntwsProducts,
       "ntwsTemporary": ntwsTemporary,
       "ntwsRegistration": ntwsRegistration,
       "ntwsMibs": ntwsMibs,
       "ntwsTraps": ntwsTraps}
)
