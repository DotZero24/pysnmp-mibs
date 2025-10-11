# SNMP MIB module (INFINERA-ENTITY-PXM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-PXM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:00 2025
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

(FloatHundredths,
 FloatTenths,
 InfnEqptType,
 InfnFlushFdbType,
 InfnMacFlapAction,
 InfnMeterActionRed,
 InfnNetworkMappingMode,
 InfnSchedulerType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "FloatTenths",
    "InfnEqptType",
    "InfnFlushFdbType",
    "InfnMacFlapAction",
    "InfnMeterActionRed",
    "InfnNetworkMappingMode",
    "InfnSchedulerType")

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

pxmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PxmTable_Object = MibTable
pxmTable = _PxmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 1)
)
if mibBuilder.loadTexts:
    pxmTable.setStatus("current")
_PxmEntry_Object = MibTableRow
pxmEntry = _PxmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 1, 1)
)
pxmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    pxmEntry.setStatus("current")
_PxmMoId_Type = DisplayString
_PxmMoId_Object = MibTableColumn
pxmMoId = _PxmMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 1, 1, 1),
    _PxmMoId_Type()
)
pxmMoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMoId.setStatus("current")
_PxmSchedulerType_Type = InfnSchedulerType
_PxmSchedulerType_Object = MibTableColumn
pxmSchedulerType = _PxmSchedulerType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 1, 1, 2),
    _PxmSchedulerType_Type()
)
pxmSchedulerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmSchedulerType.setStatus("current")
_PxmNetworkMappingMode_Type = InfnNetworkMappingMode
_PxmNetworkMappingMode_Object = MibTableColumn
pxmNetworkMappingMode = _PxmNetworkMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 1, 1, 3),
    _PxmNetworkMappingMode_Type()
)
pxmNetworkMappingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmNetworkMappingMode.setStatus("current")
_PxmTotalBandwidth_Type = Unsigned32
_PxmTotalBandwidth_Object = MibTableColumn
pxmTotalBandwidth = _PxmTotalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 1, 1, 4),
    _PxmTotalBandwidth_Type()
)
pxmTotalBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTotalBandwidth.setStatus("current")
_PxmTotalAvailableBW_Type = Unsigned32
_PxmTotalAvailableBW_Object = MibTableColumn
pxmTotalAvailableBW = _PxmTotalAvailableBW_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 1, 1, 5),
    _PxmTotalAvailableBW_Type()
)
pxmTotalAvailableBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTotalAvailableBW.setStatus("current")
_PxmMeterActionRed_Type = InfnMeterActionRed
_PxmMeterActionRed_Object = MibTableColumn
pxmMeterActionRed = _PxmMeterActionRed_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 1, 1, 6),
    _PxmMeterActionRed_Type()
)
pxmMeterActionRed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmMeterActionRed.setStatus("current")
_PxmMaxSwitchingCapacityFactor_Type = FloatTenths
_PxmMaxSwitchingCapacityFactor_Object = MibTableColumn
pxmMaxSwitchingCapacityFactor = _PxmMaxSwitchingCapacityFactor_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 1, 1, 7),
    _PxmMaxSwitchingCapacityFactor_Type()
)
pxmMaxSwitchingCapacityFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmMaxSwitchingCapacityFactor.setStatus("current")
_PxmAvailableSwitchingCapacity_Type = FloatTenths
_PxmAvailableSwitchingCapacity_Object = MibTableColumn
pxmAvailableSwitchingCapacity = _PxmAvailableSwitchingCapacity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 1, 1, 8),
    _PxmAvailableSwitchingCapacity_Type()
)
pxmAvailableSwitchingCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmAvailableSwitchingCapacity.setStatus("current")
_PxmMaxSwitchingCapacity_Type = FloatTenths
_PxmMaxSwitchingCapacity_Object = MibTableColumn
pxmMaxSwitchingCapacity = _PxmMaxSwitchingCapacity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 1, 1, 9),
    _PxmMaxSwitchingCapacity_Type()
)
pxmMaxSwitchingCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMaxSwitchingCapacity.setStatus("current")
_PxmProvEqptType_Type = InfnEqptType
_PxmProvEqptType_Object = MibTableColumn
pxmProvEqptType = _PxmProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 1, 1, 10),
    _PxmProvEqptType_Type()
)
pxmProvEqptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmProvEqptType.setStatus("current")
_PxmInstalledEqptType_Type = InfnEqptType
_PxmInstalledEqptType_Object = MibTableColumn
pxmInstalledEqptType = _PxmInstalledEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 1, 1, 11),
    _PxmInstalledEqptType_Type()
)
pxmInstalledEqptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmInstalledEqptType.setStatus("current")
_PxmEqptMaxPowerDraw_Type = FloatHundredths
_PxmEqptMaxPowerDraw_Object = MibTableColumn
pxmEqptMaxPowerDraw = _PxmEqptMaxPowerDraw_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 1, 1, 12),
    _PxmEqptMaxPowerDraw_Type()
)
pxmEqptMaxPowerDraw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmEqptMaxPowerDraw.setStatus("current")
_PxmMacAgingTime_Type = Integer32
_PxmMacAgingTime_Object = MibTableColumn
pxmMacAgingTime = _PxmMacAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 1, 1, 13),
    _PxmMacAgingTime_Type()
)
pxmMacAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmMacAgingTime.setStatus("current")
_PxmMacFlapCountThreshold_Type = Integer32
_PxmMacFlapCountThreshold_Object = MibTableColumn
pxmMacFlapCountThreshold = _PxmMacFlapCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 1, 1, 14),
    _PxmMacFlapCountThreshold_Type()
)
pxmMacFlapCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmMacFlapCountThreshold.setStatus("current")
_PxmMacFlapTimeInterval_Type = Integer32
_PxmMacFlapTimeInterval_Object = MibTableColumn
pxmMacFlapTimeInterval = _PxmMacFlapTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 1, 1, 15),
    _PxmMacFlapTimeInterval_Type()
)
pxmMacFlapTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmMacFlapTimeInterval.setStatus("current")
_PxmMacFlapAction_Type = InfnMacFlapAction
_PxmMacFlapAction_Object = MibTableColumn
pxmMacFlapAction = _PxmMacFlapAction_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 1, 1, 16),
    _PxmMacFlapAction_Type()
)
pxmMacFlapAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmMacFlapAction.setStatus("current")
_PxmFlushFdbType_Type = InfnFlushFdbType
_PxmFlushFdbType_Object = MibTableColumn
pxmFlushFdbType = _PxmFlushFdbType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 1, 1, 17),
    _PxmFlushFdbType_Type()
)
pxmFlushFdbType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmFlushFdbType.setStatus("current")
_PxmVsiOrInterface_Type = DisplayString
_PxmVsiOrInterface_Object = MibTableColumn
pxmVsiOrInterface = _PxmVsiOrInterface_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 1, 1, 18),
    _PxmVsiOrInterface_Type()
)
pxmVsiOrInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmVsiOrInterface.setStatus("current")
_PxmGlobalId_Type = Integer32
_PxmGlobalId_Object = MibTableColumn
pxmGlobalId = _PxmGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 1, 1, 19),
    _PxmGlobalId_Type()
)
pxmGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmGlobalId.setStatus("current")
_PxmMPLSTPNodeID_Type = Integer32
_PxmMPLSTPNodeID_Object = MibTableColumn
pxmMPLSTPNodeID = _PxmMPLSTPNodeID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 1, 1, 20),
    _PxmMPLSTPNodeID_Type()
)
pxmMPLSTPNodeID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmMPLSTPNodeID.setStatus("current")
_PxmConformance_ObjectIdentity = ObjectIdentity
pxmConformance = _PxmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 3)
)
_PxmCompliances_ObjectIdentity = ObjectIdentity
pxmCompliances = _PxmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 3, 1)
)
_PxmGroups_ObjectIdentity = ObjectIdentity
pxmGroups = _PxmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 3, 2)
)

# Managed Objects groups

pxmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 3, 2, 1)
)
pxmGroup.setObjects(
      *(("INFINERA-ENTITY-PXM-MIB", "pxmMoId"),
        ("INFINERA-ENTITY-PXM-MIB", "pxmSchedulerType"),
        ("INFINERA-ENTITY-PXM-MIB", "pxmNetworkMappingMode"),
        ("INFINERA-ENTITY-PXM-MIB", "pxmTotalBandwidth"),
        ("INFINERA-ENTITY-PXM-MIB", "pxmTotalAvailableBW"),
        ("INFINERA-ENTITY-PXM-MIB", "pxmMeterActionRed"),
        ("INFINERA-ENTITY-PXM-MIB", "pxmMaxSwitchingCapacityFactor"),
        ("INFINERA-ENTITY-PXM-MIB", "pxmAvailableSwitchingCapacity"),
        ("INFINERA-ENTITY-PXM-MIB", "pxmMaxSwitchingCapacity"),
        ("INFINERA-ENTITY-PXM-MIB", "pxmProvEqptType"),
        ("INFINERA-ENTITY-PXM-MIB", "pxmInstalledEqptType"),
        ("INFINERA-ENTITY-PXM-MIB", "pxmEqptMaxPowerDraw"),
        ("INFINERA-ENTITY-PXM-MIB", "pxmMacAgingTime"),
        ("INFINERA-ENTITY-PXM-MIB", "pxmMacFlapCountThreshold"),
        ("INFINERA-ENTITY-PXM-MIB", "pxmMacFlapTimeInterval"),
        ("INFINERA-ENTITY-PXM-MIB", "pxmMacFlapAction"),
        ("INFINERA-ENTITY-PXM-MIB", "pxmFlushFdbType"),
        ("INFINERA-ENTITY-PXM-MIB", "pxmVsiOrInterface"),
        ("INFINERA-ENTITY-PXM-MIB", "pxmGlobalId"),
        ("INFINERA-ENTITY-PXM-MIB", "pxmMPLSTPNodeID"))
)
if mibBuilder.loadTexts:
    pxmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pxmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 30, 3, 1, 1)
)
pxmCompliance.setObjects(
    ("INFINERA-ENTITY-PXM-MIB", "pxmGroup")
)
if mibBuilder.loadTexts:
    pxmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-PXM-MIB",
    **{"pxmMIB": pxmMIB,
       "pxmTable": pxmTable,
       "pxmEntry": pxmEntry,
       "pxmMoId": pxmMoId,
       "pxmSchedulerType": pxmSchedulerType,
       "pxmNetworkMappingMode": pxmNetworkMappingMode,
       "pxmTotalBandwidth": pxmTotalBandwidth,
       "pxmTotalAvailableBW": pxmTotalAvailableBW,
       "pxmMeterActionRed": pxmMeterActionRed,
       "pxmMaxSwitchingCapacityFactor": pxmMaxSwitchingCapacityFactor,
       "pxmAvailableSwitchingCapacity": pxmAvailableSwitchingCapacity,
       "pxmMaxSwitchingCapacity": pxmMaxSwitchingCapacity,
       "pxmProvEqptType": pxmProvEqptType,
       "pxmInstalledEqptType": pxmInstalledEqptType,
       "pxmEqptMaxPowerDraw": pxmEqptMaxPowerDraw,
       "pxmMacAgingTime": pxmMacAgingTime,
       "pxmMacFlapCountThreshold": pxmMacFlapCountThreshold,
       "pxmMacFlapTimeInterval": pxmMacFlapTimeInterval,
       "pxmMacFlapAction": pxmMacFlapAction,
       "pxmFlushFdbType": pxmFlushFdbType,
       "pxmVsiOrInterface": pxmVsiOrInterface,
       "pxmGlobalId": pxmGlobalId,
       "pxmMPLSTPNodeID": pxmMPLSTPNodeID,
       "pxmConformance": pxmConformance,
       "pxmCompliances": pxmCompliances,
       "pxmCompliance": pxmCompliance,
       "pxmGroups": pxmGroups,
       "pxmGroup": pxmGroup}
)
