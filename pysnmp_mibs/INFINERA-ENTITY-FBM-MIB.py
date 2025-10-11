# SNMP MIB module (INFINERA-ENTITY-FBM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-FBM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:08 2025
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

fbmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FbmTable_Object = MibTable
fbmTable = _FbmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55, 1)
)
if mibBuilder.loadTexts:
    fbmTable.setStatus("current")
_FbmEntry_Object = MibTableRow
fbmEntry = _FbmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55, 1, 1)
)
fbmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fbmEntry.setStatus("current")
_FbmMoId_Type = DisplayString
_FbmMoId_Object = MibTableColumn
fbmMoId = _FbmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55, 1, 1, 1),
    _FbmMoId_Type()
)
fbmMoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fbmMoId.setStatus("current")
_FbmProvEqptType_Type = InfnEqptType
_FbmProvEqptType_Object = MibTableColumn
fbmProvEqptType = _FbmProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55, 1, 1, 2),
    _FbmProvEqptType_Type()
)
fbmProvEqptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fbmProvEqptType.setStatus("current")
_FbmUsbUpstreamNbr_Type = DisplayString
_FbmUsbUpstreamNbr_Object = MibTableColumn
fbmUsbUpstreamNbr = _FbmUsbUpstreamNbr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55, 1, 1, 3),
    _FbmUsbUpstreamNbr_Type()
)
fbmUsbUpstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmUsbUpstreamNbr.setStatus("current")
_FbmUsbDownstreamNbr_Type = DisplayString
_FbmUsbDownstreamNbr_Object = MibTableColumn
fbmUsbDownstreamNbr = _FbmUsbDownstreamNbr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55, 1, 1, 4),
    _FbmUsbDownstreamNbr_Type()
)
fbmUsbDownstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmUsbDownstreamNbr.setStatus("current")
_FbmConformance_ObjectIdentity = ObjectIdentity
fbmConformance = _FbmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55, 3)
)
_FbmCompliances_ObjectIdentity = ObjectIdentity
fbmCompliances = _FbmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55, 3, 1)
)
_FbmGroups_ObjectIdentity = ObjectIdentity
fbmGroups = _FbmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55, 3, 2)
)

# Managed Objects groups

fbmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55, 3, 2, 1)
)
fbmGroup.setObjects(
      *(("INFINERA-ENTITY-FBM-MIB", "fbmMoId"),
        ("INFINERA-ENTITY-FBM-MIB", "fbmProvEqptType"),
        ("INFINERA-ENTITY-FBM-MIB", "fbmUsbUpstreamNbr"),
        ("INFINERA-ENTITY-FBM-MIB", "fbmUsbDownstreamNbr"))
)
if mibBuilder.loadTexts:
    fbmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fbmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 55, 3, 1, 1)
)
fbmCompliance.setObjects(
    ("INFINERA-ENTITY-FBM-MIB", "fbmGroup")
)
if mibBuilder.loadTexts:
    fbmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-FBM-MIB",
    **{"fbmMIB": fbmMIB,
       "fbmTable": fbmTable,
       "fbmEntry": fbmEntry,
       "fbmMoId": fbmMoId,
       "fbmProvEqptType": fbmProvEqptType,
       "fbmUsbUpstreamNbr": fbmUsbUpstreamNbr,
       "fbmUsbDownstreamNbr": fbmUsbDownstreamNbr,
       "fbmConformance": fbmConformance,
       "fbmCompliances": fbmCompliances,
       "fbmCompliance": fbmCompliance,
       "fbmGroups": fbmGroups,
       "fbmGroup": fbmGroup}
)
