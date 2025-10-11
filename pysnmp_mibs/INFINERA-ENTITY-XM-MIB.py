# SNMP MIB module (INFINERA-ENTITY-XM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-XM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:23 2025
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

(InfnEqptType,
 InfnOxmCardRedundancyStatus,
 InfnOxmEccStatus) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnEqptType",
    "InfnOxmCardRedundancyStatus",
    "InfnOxmEccStatus")

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

xmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XmTable_Object = MibTable
xmTable = _XmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 1)
)
if mibBuilder.loadTexts:
    xmTable.setStatus("current")
_XmEntry_Object = MibTableRow
xmEntry = _XmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 1, 1)
)
xmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    xmEntry.setStatus("current")
_XmMoId_Type = DisplayString
_XmMoId_Object = MibTableColumn
xmMoId = _XmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 1, 1, 1),
    _XmMoId_Type()
)
xmMoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmMoId.setStatus("current")
_CardRedundancyStatus_Type = InfnOxmCardRedundancyStatus
_CardRedundancyStatus_Object = MibTableColumn
cardRedundancyStatus = _CardRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 1, 1, 2),
    _CardRedundancyStatus_Type()
)
cardRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardRedundancyStatus.setStatus("current")
_XmProvEqptType_Type = InfnEqptType
_XmProvEqptType_Object = MibTableColumn
xmProvEqptType = _XmProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 1, 1, 3),
    _XmProvEqptType_Type()
)
xmProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xmProvEqptType.setStatus("current")
_XmRowStatus_Type = RowStatus
_XmRowStatus_Object = MibTableColumn
xmRowStatus = _XmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 1, 1, 4),
    _XmRowStatus_Type()
)
xmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xmRowStatus.setStatus("current")
_ActvTimingSource_Type = DisplayString
_ActvTimingSource_Object = MibTableColumn
actvTimingSource = _ActvTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 1, 1, 5),
    _ActvTimingSource_Type()
)
actvTimingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actvTimingSource.setStatus("current")
_XmEccStatus_Type = InfnOxmEccStatus
_XmEccStatus_Object = MibTableColumn
xmEccStatus = _XmEccStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 1, 1, 6),
    _XmEccStatus_Type()
)
xmEccStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmEccStatus.setStatus("current")
_XmConformance_ObjectIdentity = ObjectIdentity
xmConformance = _XmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 3)
)
_XmCompliances_ObjectIdentity = ObjectIdentity
xmCompliances = _XmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 3, 1)
)
_XmGroups_ObjectIdentity = ObjectIdentity
xmGroups = _XmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 3, 2)
)

# Managed Objects groups

xmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 3, 2, 1)
)
xmGroup.setObjects(
      *(("INFINERA-ENTITY-XM-MIB", "xmMoId"),
        ("INFINERA-ENTITY-XM-MIB", "cardRedundancyStatus"),
        ("INFINERA-ENTITY-XM-MIB", "xmProvEqptType"),
        ("INFINERA-ENTITY-XM-MIB", "xmRowStatus"),
        ("INFINERA-ENTITY-XM-MIB", "actvTimingSource"),
        ("INFINERA-ENTITY-XM-MIB", "xmEccStatus"))
)
if mibBuilder.loadTexts:
    xmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 20, 3, 1, 1)
)
xmCompliance.setObjects(
    ("INFINERA-ENTITY-XM-MIB", "xmGroup")
)
if mibBuilder.loadTexts:
    xmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-XM-MIB",
    **{"xmMIB": xmMIB,
       "xmTable": xmTable,
       "xmEntry": xmEntry,
       "xmMoId": xmMoId,
       "cardRedundancyStatus": cardRedundancyStatus,
       "xmProvEqptType": xmProvEqptType,
       "xmRowStatus": xmRowStatus,
       "actvTimingSource": actvTimingSource,
       "xmEccStatus": xmEccStatus,
       "xmConformance": xmConformance,
       "xmCompliances": xmCompliances,
       "xmCompliance": xmCompliance,
       "xmGroups": xmGroups,
       "xmGroup": xmGroup}
)
