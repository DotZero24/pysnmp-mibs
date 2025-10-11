# SNMP MIB module (INFINERA-ENTITY-OTM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-OTM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:55 2025
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

(entLPPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entLPPhysicalIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

otmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OtmTable_Object = MibTable
otmTable = _OtmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24, 1)
)
if mibBuilder.loadTexts:
    otmTable.setStatus("current")
_OtmEntry_Object = MibTableRow
otmEntry = _OtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24, 1, 1)
)
otmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    otmEntry.setStatus("current")
_OtmMoId_Type = DisplayString
_OtmMoId_Object = MibTableColumn
otmMoId = _OtmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24, 1, 1, 1),
    _OtmMoId_Type()
)
otmMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    otmMoId.setStatus("current")
_OtmProvEqptType_Type = InfnEqptType
_OtmProvEqptType_Object = MibTableColumn
otmProvEqptType = _OtmProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24, 1, 1, 2),
    _OtmProvEqptType_Type()
)
otmProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    otmProvEqptType.setStatus("current")
_OtmRowStatus_Type = RowStatus
_OtmRowStatus_Object = MibTableColumn
otmRowStatus = _OtmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24, 1, 1, 3),
    _OtmRowStatus_Type()
)
otmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    otmRowStatus.setStatus("current")
_ActvTimingSource_Type = DisplayString
_ActvTimingSource_Object = MibTableColumn
actvTimingSource = _ActvTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24, 1, 1, 4),
    _ActvTimingSource_Type()
)
actvTimingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actvTimingSource.setStatus("current")
_OtmConformance_ObjectIdentity = ObjectIdentity
otmConformance = _OtmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24, 3)
)
_OtmCompliances_ObjectIdentity = ObjectIdentity
otmCompliances = _OtmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24, 3, 1)
)
_OtmGroups_ObjectIdentity = ObjectIdentity
otmGroups = _OtmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24, 3, 2)
)

# Managed Objects groups

otmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24, 3, 2, 1)
)
otmGroup.setObjects(
      *(("INFINERA-ENTITY-OTM-MIB", "otmMoId"),
        ("INFINERA-ENTITY-OTM-MIB", "otmProvEqptType"),
        ("INFINERA-ENTITY-OTM-MIB", "otmRowStatus"),
        ("INFINERA-ENTITY-OTM-MIB", "actvTimingSource"))
)
if mibBuilder.loadTexts:
    otmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

otmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 24, 3, 1, 1)
)
otmCompliance.setObjects(
    ("INFINERA-ENTITY-OTM-MIB", "otmGroup")
)
if mibBuilder.loadTexts:
    otmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-OTM-MIB",
    **{"otmMIB": otmMIB,
       "otmTable": otmTable,
       "otmEntry": otmEntry,
       "otmMoId": otmMoId,
       "otmProvEqptType": otmProvEqptType,
       "otmRowStatus": otmRowStatus,
       "actvTimingSource": actvTimingSource,
       "otmConformance": otmConformance,
       "otmCompliances": otmCompliances,
       "otmCompliance": otmCompliance,
       "otmGroups": otmGroups,
       "otmGroup": otmGroup}
)
