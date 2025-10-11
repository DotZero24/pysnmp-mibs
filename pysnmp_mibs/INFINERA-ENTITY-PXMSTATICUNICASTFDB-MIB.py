# SNMP MIB module (INFINERA-ENTITY-PXMSTATICUNICASTFDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-PXMSTATICUNICASTFDB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:11 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

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

pxmStaticUnicastFdbMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 65)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PxmStaticUnicastFdbTable_Object = MibTable
pxmStaticUnicastFdbTable = _PxmStaticUnicastFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 65, 1)
)
if mibBuilder.loadTexts:
    pxmStaticUnicastFdbTable.setStatus("current")
_PxmStaticUnicastFdbEntry_Object = MibTableRow
pxmStaticUnicastFdbEntry = _PxmStaticUnicastFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 65, 1, 1)
)
pxmStaticUnicastFdbEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmStaticUnicastFdbEntry.setStatus("current")
_PxmStaticUnicastFdbMacAddress_Type = DisplayString
_PxmStaticUnicastFdbMacAddress_Object = MibTableColumn
pxmStaticUnicastFdbMacAddress = _PxmStaticUnicastFdbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 65, 1, 1, 1),
    _PxmStaticUnicastFdbMacAddress_Type()
)
pxmStaticUnicastFdbMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmStaticUnicastFdbMacAddress.setStatus("current")
_PxmStaticUnicastFdbConformance_ObjectIdentity = ObjectIdentity
pxmStaticUnicastFdbConformance = _PxmStaticUnicastFdbConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 65, 3)
)
_PxmStaticUnicastFdbCompliances_ObjectIdentity = ObjectIdentity
pxmStaticUnicastFdbCompliances = _PxmStaticUnicastFdbCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 65, 3, 1)
)
_PxmStaticUnicastFdbGroups_ObjectIdentity = ObjectIdentity
pxmStaticUnicastFdbGroups = _PxmStaticUnicastFdbGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 65, 3, 2)
)

# Managed Objects groups

pxmStaticUnicastFdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 65, 3, 2, 1)
)
pxmStaticUnicastFdbGroup.setObjects(
    ("INFINERA-ENTITY-PXMSTATICUNICASTFDB-MIB", "pxmStaticUnicastFdbMacAddress")
)
if mibBuilder.loadTexts:
    pxmStaticUnicastFdbGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pxmStaticUnicastFdbCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 65, 3, 1, 1)
)
pxmStaticUnicastFdbCompliance.setObjects(
    ("INFINERA-ENTITY-PXMSTATICUNICASTFDB-MIB", "pxmStaticUnicastFdbGroup")
)
if mibBuilder.loadTexts:
    pxmStaticUnicastFdbCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-PXMSTATICUNICASTFDB-MIB",
    **{"pxmStaticUnicastFdbMIB": pxmStaticUnicastFdbMIB,
       "pxmStaticUnicastFdbTable": pxmStaticUnicastFdbTable,
       "pxmStaticUnicastFdbEntry": pxmStaticUnicastFdbEntry,
       "pxmStaticUnicastFdbMacAddress": pxmStaticUnicastFdbMacAddress,
       "pxmStaticUnicastFdbConformance": pxmStaticUnicastFdbConformance,
       "pxmStaticUnicastFdbCompliances": pxmStaticUnicastFdbCompliances,
       "pxmStaticUnicastFdbCompliance": pxmStaticUnicastFdbCompliance,
       "pxmStaticUnicastFdbGroups": pxmStaticUnicastFdbGroups,
       "pxmStaticUnicastFdbGroup": pxmStaticUnicastFdbGroup}
)
