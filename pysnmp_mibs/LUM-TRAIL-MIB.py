# SNMP MIB module (LUM-TRAIL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-TRAIL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:51 2025
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

(lumModules,
 lumTrailMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumTrailMIB")

(FaultStatus,) = mibBuilder.importSymbols(
    "LUM-TC",
    "FaultStatus")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lumTrailMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 38)
)
if mibBuilder.loadTexts:
    lumTrailMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2011-04-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumTrailConfs_ObjectIdentity = ObjectIdentity
lumTrailConfs = _LumTrailConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 38, 1)
)
_LumTrailGroups_ObjectIdentity = ObjectIdentity
lumTrailGroups = _LumTrailGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 38, 1, 1)
)
_LumTrailCompl_ObjectIdentity = ObjectIdentity
lumTrailCompl = _LumTrailCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 38, 1, 2)
)
_LumTrailMIBObjects_ObjectIdentity = ObjectIdentity
lumTrailMIBObjects = _LumTrailMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 38, 2)
)
_TrailGeneral_ObjectIdentity = ObjectIdentity
trailGeneral = _TrailGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 38, 2, 1)
)
_TrailGeneralConfigLastChangeTime_Type = DateAndTime
_TrailGeneralConfigLastChangeTime_Object = MibScalar
trailGeneralConfigLastChangeTime = _TrailGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 38, 2, 1, 1),
    _TrailGeneralConfigLastChangeTime_Type()
)
trailGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trailGeneralConfigLastChangeTime.setStatus("current")
_TrailGeneralStateLastChangeTime_Type = DateAndTime
_TrailGeneralStateLastChangeTime_Object = MibScalar
trailGeneralStateLastChangeTime = _TrailGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 38, 2, 1, 2),
    _TrailGeneralStateLastChangeTime_Type()
)
trailGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trailGeneralStateLastChangeTime.setStatus("current")
_TrailGeneralStatusTableSize_Type = Unsigned32
_TrailGeneralStatusTableSize_Object = MibScalar
trailGeneralStatusTableSize = _TrailGeneralStatusTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 38, 2, 1, 3),
    _TrailGeneralStatusTableSize_Type()
)
trailGeneralStatusTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trailGeneralStatusTableSize.setStatus("current")
_TrailStatusList_ObjectIdentity = ObjectIdentity
trailStatusList = _TrailStatusList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 38, 2, 2)
)
_TrailStatusTable_Object = MibTable
trailStatusTable = _TrailStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 38, 2, 2, 1)
)
if mibBuilder.loadTexts:
    trailStatusTable.setStatus("current")
_TrailStatusEntry_Object = MibTableRow
trailStatusEntry = _TrailStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 38, 2, 2, 1, 1)
)
trailStatusEntry.setIndexNames(
    (0, "LUM-TRAIL-MIB", "trailStatusIndex"),
)
if mibBuilder.loadTexts:
    trailStatusEntry.setStatus("current")


class _TrailStatusIndex_Type(Unsigned32):
    """Custom type trailStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrailStatusIndex_Type.__name__ = "Unsigned32"
_TrailStatusIndex_Object = MibTableColumn
trailStatusIndex = _TrailStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 38, 2, 2, 1, 1, 1),
    _TrailStatusIndex_Type()
)
trailStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trailStatusIndex.setStatus("current")
_TrailStatusIncomplete_Type = FaultStatus
_TrailStatusIncomplete_Object = MibTableColumn
trailStatusIncomplete = _TrailStatusIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 38, 2, 2, 1, 1, 2),
    _TrailStatusIncomplete_Type()
)
trailStatusIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trailStatusIncomplete.setStatus("current")
_TrailStatusDegraded_Type = FaultStatus
_TrailStatusDegraded_Object = MibTableColumn
trailStatusDegraded = _TrailStatusDegraded_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 38, 2, 2, 1, 1, 3),
    _TrailStatusDegraded_Type()
)
trailStatusDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trailStatusDegraded.setStatus("deprecated")
_TrailStatusDown_Type = FaultStatus
_TrailStatusDown_Object = MibTableColumn
trailStatusDown = _TrailStatusDown_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 38, 2, 2, 1, 1, 4),
    _TrailStatusDown_Type()
)
trailStatusDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trailStatusDown.setStatus("deprecated")

# Managed Objects groups

trailGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 38, 1, 1, 1)
)
trailGeneralGroup.setObjects(
      *(("LUM-TRAIL-MIB", "trailGeneralConfigLastChangeTime"),
        ("LUM-TRAIL-MIB", "trailGeneralStateLastChangeTime"),
        ("LUM-TRAIL-MIB", "trailGeneralStatusTableSize"))
)
if mibBuilder.loadTexts:
    trailGeneralGroup.setStatus("current")

trailStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 38, 1, 1, 2)
)
trailStatusGroup.setObjects(
      *(("LUM-TRAIL-MIB", "trailStatusIndex"),
        ("LUM-TRAIL-MIB", "trailStatusDegraded"),
        ("LUM-TRAIL-MIB", "trailStatusDown"),
        ("LUM-TRAIL-MIB", "trailStatusIncomplete"))
)
if mibBuilder.loadTexts:
    trailStatusGroup.setStatus("deprecated")

trailStatusGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 38, 1, 1, 3)
)
trailStatusGroupV2.setObjects(
      *(("LUM-TRAIL-MIB", "trailStatusIndex"),
        ("LUM-TRAIL-MIB", "trailStatusIncomplete"))
)
if mibBuilder.loadTexts:
    trailStatusGroupV2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumTrailBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 38, 1, 2, 1)
)
lumTrailBasicComplV1.setObjects(
      *(("LUM-TRAIL-MIB", "trailGeneralGroup"),
        ("LUM-TRAIL-MIB", "trailStatusGroup"))
)
if mibBuilder.loadTexts:
    lumTrailBasicComplV1.setStatus(
        "deprecated"
    )

lumTrailBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 38, 1, 2, 2)
)
lumTrailBasicComplV2.setObjects(
      *(("LUM-TRAIL-MIB", "trailGeneralGroup"),
        ("LUM-TRAIL-MIB", "trailStatusGroupV2"))
)
if mibBuilder.loadTexts:
    lumTrailBasicComplV2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-TRAIL-MIB",
    **{"lumTrailMIBModule": lumTrailMIBModule,
       "lumTrailConfs": lumTrailConfs,
       "lumTrailGroups": lumTrailGroups,
       "trailGeneralGroup": trailGeneralGroup,
       "trailStatusGroup": trailStatusGroup,
       "trailStatusGroupV2": trailStatusGroupV2,
       "lumTrailCompl": lumTrailCompl,
       "lumTrailBasicComplV1": lumTrailBasicComplV1,
       "lumTrailBasicComplV2": lumTrailBasicComplV2,
       "lumTrailMIBObjects": lumTrailMIBObjects,
       "trailGeneral": trailGeneral,
       "trailGeneralConfigLastChangeTime": trailGeneralConfigLastChangeTime,
       "trailGeneralStateLastChangeTime": trailGeneralStateLastChangeTime,
       "trailGeneralStatusTableSize": trailGeneralStatusTableSize,
       "trailStatusList": trailStatusList,
       "trailStatusTable": trailStatusTable,
       "trailStatusEntry": trailStatusEntry,
       "trailStatusIndex": trailStatusIndex,
       "trailStatusIncomplete": trailStatusIncomplete,
       "trailStatusDegraded": trailStatusDegraded,
       "trailStatusDown": trailStatusDown}
)
