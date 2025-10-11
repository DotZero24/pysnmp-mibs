# SNMP MIB module (INFINERA-ENTITY-CWM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-CWM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:41 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(equipment,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "equipment")

(InfnEqptType,) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnEqptType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cwmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 57)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CwmTable_Object = MibTable
cwmTable = _CwmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 57, 1)
)
if mibBuilder.loadTexts:
    cwmTable.setStatus("current")
_CwmEntry_Object = MibTableRow
cwmEntry = _CwmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 57, 1, 1)
)
cwmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cwmEntry.setStatus("current")
_CwmMoId_Type = DisplayString
_CwmMoId_Object = MibTableColumn
cwmMoId = _CwmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 57, 1, 1, 1),
    _CwmMoId_Type()
)
cwmMoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwmMoId.setStatus("current")
_CwmProvEqptType_Type = InfnEqptType
_CwmProvEqptType_Object = MibTableColumn
cwmProvEqptType = _CwmProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 57, 1, 1, 2),
    _CwmProvEqptType_Type()
)
cwmProvEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwmProvEqptType.setStatus("current")
_CwmAssociatedDegree_Type = DisplayString
_CwmAssociatedDegree_Object = MibTableColumn
cwmAssociatedDegree = _CwmAssociatedDegree_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 57, 1, 1, 3),
    _CwmAssociatedDegree_Type()
)
cwmAssociatedDegree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwmAssociatedDegree.setStatus("current")
_CwmConformance_ObjectIdentity = ObjectIdentity
cwmConformance = _CwmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 57, 3)
)
_CwmCompliances_ObjectIdentity = ObjectIdentity
cwmCompliances = _CwmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 57, 3, 1)
)
_CwmGroups_ObjectIdentity = ObjectIdentity
cwmGroups = _CwmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 57, 3, 2)
)

# Managed Objects groups

cwmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 57, 3, 2, 1)
)
cwmGroup.setObjects(
      *(("INFINERA-ENTITY-CWM-MIB", "cwmMoId"),
        ("INFINERA-ENTITY-CWM-MIB", "cwmProvEqptType"),
        ("INFINERA-ENTITY-CWM-MIB", "cwmAssociatedDegree"))
)
if mibBuilder.loadTexts:
    cwmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cwmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 57, 3, 1, 1)
)
cwmCompliance.setObjects(
    ("INFINERA-ENTITY-CWM-MIB", "cwmGroup")
)
if mibBuilder.loadTexts:
    cwmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-CWM-MIB",
    **{"cwmMIB": cwmMIB,
       "cwmTable": cwmTable,
       "cwmEntry": cwmEntry,
       "cwmMoId": cwmMoId,
       "cwmProvEqptType": cwmProvEqptType,
       "cwmAssociatedDegree": cwmAssociatedDegree,
       "cwmConformance": cwmConformance,
       "cwmCompliances": cwmCompliances,
       "cwmCompliance": cwmCompliance,
       "cwmGroups": cwmGroups,
       "cwmGroup": cwmGroup}
)
