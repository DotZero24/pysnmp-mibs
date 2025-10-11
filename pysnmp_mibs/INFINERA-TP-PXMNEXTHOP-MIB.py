# SNMP MIB module (INFINERA-TP-PXMNEXTHOP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-PXMNEXTHOP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:06 2025
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

pxmNextHopMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 68)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PxmNextHopTable_Object = MibTable
pxmNextHopTable = _PxmNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 68, 1)
)
if mibBuilder.loadTexts:
    pxmNextHopTable.setStatus("current")
_PxmNextHopEntry_Object = MibTableRow
pxmNextHopEntry = _PxmNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 68, 1, 1)
)
pxmNextHopEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmNextHopEntry.setStatus("current")
_PxmNextHopMacAddress_Type = DisplayString
_PxmNextHopMacAddress_Object = MibTableColumn
pxmNextHopMacAddress = _PxmNextHopMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 68, 1, 1, 1),
    _PxmNextHopMacAddress_Type()
)
pxmNextHopMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmNextHopMacAddress.setStatus("current")
_PxmNextHopConformance_ObjectIdentity = ObjectIdentity
pxmNextHopConformance = _PxmNextHopConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 68, 3)
)
_PxmNextHopCompliances_ObjectIdentity = ObjectIdentity
pxmNextHopCompliances = _PxmNextHopCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 68, 3, 1)
)
_PxmNextHopGroups_ObjectIdentity = ObjectIdentity
pxmNextHopGroups = _PxmNextHopGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 68, 3, 2)
)

# Managed Objects groups

pxmNextHopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 68, 3, 2, 1)
)
pxmNextHopGroup.setObjects(
    ("INFINERA-TP-PXMNEXTHOP-MIB", "pxmNextHopMacAddress")
)
if mibBuilder.loadTexts:
    pxmNextHopGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pxmNextHopCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 68, 3, 1, 1)
)
pxmNextHopCompliance.setObjects(
    ("INFINERA-TP-PXMNEXTHOP-MIB", "pxmNextHopGroup")
)
if mibBuilder.loadTexts:
    pxmNextHopCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-PXMNEXTHOP-MIB",
    **{"pxmNextHopMIB": pxmNextHopMIB,
       "pxmNextHopTable": pxmNextHopTable,
       "pxmNextHopEntry": pxmNextHopEntry,
       "pxmNextHopMacAddress": pxmNextHopMacAddress,
       "pxmNextHopConformance": pxmNextHopConformance,
       "pxmNextHopCompliances": pxmNextHopCompliances,
       "pxmNextHopCompliance": pxmNextHopCompliance,
       "pxmNextHopGroups": pxmNextHopGroups,
       "pxmNextHopGroup": pxmNextHopGroup}
)
