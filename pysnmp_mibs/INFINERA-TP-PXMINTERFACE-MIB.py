# SNMP MIB module (INFINERA-TP-PXMINTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-PXMINTERFACE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:23 2025
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

(InfnPxmIntfProtocolType,) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnPxmIntfProtocolType")

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

pxmInterfaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 73)
)
if mibBuilder.loadTexts:
    pxmInterfaceMIB.setRevisions(
        ("2016-05-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PxmInterfaceTable_Object = MibTable
pxmInterfaceTable = _PxmInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 73, 1)
)
if mibBuilder.loadTexts:
    pxmInterfaceTable.setStatus("current")
_PxmInterfaceEntry_Object = MibTableRow
pxmInterfaceEntry = _PxmInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 73, 1, 1)
)
pxmInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmInterfaceEntry.setStatus("current")
_PxmInterfaceProtocolType_Type = InfnPxmIntfProtocolType
_PxmInterfaceProtocolType_Object = MibTableColumn
pxmInterfaceProtocolType = _PxmInterfaceProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 73, 1, 1, 1),
    _PxmInterfaceProtocolType_Type()
)
pxmInterfaceProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmInterfaceProtocolType.setStatus("current")
_PxmInterfaceMacAddress_Type = DisplayString
_PxmInterfaceMacAddress_Object = MibTableColumn
pxmInterfaceMacAddress = _PxmInterfaceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 73, 1, 1, 2),
    _PxmInterfaceMacAddress_Type()
)
pxmInterfaceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmInterfaceMacAddress.setStatus("current")
_PxmInterfaceConformance_ObjectIdentity = ObjectIdentity
pxmInterfaceConformance = _PxmInterfaceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 73, 3)
)
_PxmInterfaceCompliances_ObjectIdentity = ObjectIdentity
pxmInterfaceCompliances = _PxmInterfaceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 73, 3, 1)
)
_PxmInterfaceGroups_ObjectIdentity = ObjectIdentity
pxmInterfaceGroups = _PxmInterfaceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 73, 3, 2)
)

# Managed Objects groups

pxmInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 73, 3, 2, 1)
)
pxmInterfaceGroup.setObjects(
      *(("INFINERA-TP-PXMINTERFACE-MIB", "pxmInterfaceProtocolType"),
        ("INFINERA-TP-PXMINTERFACE-MIB", "pxmInterfaceMacAddress"))
)
if mibBuilder.loadTexts:
    pxmInterfaceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pxmInterfaceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 73, 3, 1, 1)
)
pxmInterfaceCompliance.setObjects(
    ("INFINERA-TP-PXMINTERFACE-MIB", "pxmInterfaceGroup")
)
if mibBuilder.loadTexts:
    pxmInterfaceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-PXMINTERFACE-MIB",
    **{"pxmInterfaceMIB": pxmInterfaceMIB,
       "pxmInterfaceTable": pxmInterfaceTable,
       "pxmInterfaceEntry": pxmInterfaceEntry,
       "pxmInterfaceProtocolType": pxmInterfaceProtocolType,
       "pxmInterfaceMacAddress": pxmInterfaceMacAddress,
       "pxmInterfaceConformance": pxmInterfaceConformance,
       "pxmInterfaceCompliances": pxmInterfaceCompliances,
       "pxmInterfaceCompliance": pxmInterfaceCompliance,
       "pxmInterfaceGroups": pxmInterfaceGroups,
       "pxmInterfaceGroup": pxmInterfaceGroup}
)
