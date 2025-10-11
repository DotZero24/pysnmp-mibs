# SNMP MIB module (LUM-NC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-NC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:45 2025
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
 lumNcMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumNcMIB")

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

lumNcMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 39)
)
if mibBuilder.loadTexts:
    lumNcMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2011-04-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumNcConfs_ObjectIdentity = ObjectIdentity
lumNcConfs = _LumNcConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 39, 1)
)
_LumNcGroups_ObjectIdentity = ObjectIdentity
lumNcGroups = _LumNcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 39, 1, 1)
)
_LumNcCompl_ObjectIdentity = ObjectIdentity
lumNcCompl = _LumNcCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 39, 1, 2)
)
_LumNcMIBObjects_ObjectIdentity = ObjectIdentity
lumNcMIBObjects = _LumNcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 39, 2)
)
_NcGeneral_ObjectIdentity = ObjectIdentity
ncGeneral = _NcGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 39, 2, 1)
)
_NcGeneralConfigLastChangeTime_Type = DateAndTime
_NcGeneralConfigLastChangeTime_Object = MibScalar
ncGeneralConfigLastChangeTime = _NcGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 39, 2, 1, 1),
    _NcGeneralConfigLastChangeTime_Type()
)
ncGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncGeneralConfigLastChangeTime.setStatus("current")
_NcGeneralStateLastChangeTime_Type = DateAndTime
_NcGeneralStateLastChangeTime_Object = MibScalar
ncGeneralStateLastChangeTime = _NcGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 39, 2, 1, 2),
    _NcGeneralStateLastChangeTime_Type()
)
ncGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncGeneralStateLastChangeTime.setStatus("current")
_NcGeneralStatusTableSize_Type = Unsigned32
_NcGeneralStatusTableSize_Object = MibScalar
ncGeneralStatusTableSize = _NcGeneralStatusTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 39, 2, 1, 3),
    _NcGeneralStatusTableSize_Type()
)
ncGeneralStatusTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncGeneralStatusTableSize.setStatus("current")
_NcStatusList_ObjectIdentity = ObjectIdentity
ncStatusList = _NcStatusList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 39, 2, 2)
)
_NcStatusTable_Object = MibTable
ncStatusTable = _NcStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 39, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ncStatusTable.setStatus("current")
_NcStatusEntry_Object = MibTableRow
ncStatusEntry = _NcStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 39, 2, 2, 1, 1)
)
ncStatusEntry.setIndexNames(
    (0, "LUM-NC-MIB", "ncStatusIndex"),
)
if mibBuilder.loadTexts:
    ncStatusEntry.setStatus("current")


class _NcStatusIndex_Type(Unsigned32):
    """Custom type ncStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcStatusIndex_Type.__name__ = "Unsigned32"
_NcStatusIndex_Object = MibTableColumn
ncStatusIndex = _NcStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 39, 2, 2, 1, 1, 1),
    _NcStatusIndex_Type()
)
ncStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStatusIndex.setStatus("current")
_NcStatusIncomplete_Type = FaultStatus
_NcStatusIncomplete_Object = MibTableColumn
ncStatusIncomplete = _NcStatusIncomplete_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 39, 2, 2, 1, 1, 2),
    _NcStatusIncomplete_Type()
)
ncStatusIncomplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStatusIncomplete.setStatus("current")
_NcStatusDegraded_Type = FaultStatus
_NcStatusDegraded_Object = MibTableColumn
ncStatusDegraded = _NcStatusDegraded_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 39, 2, 2, 1, 1, 3),
    _NcStatusDegraded_Type()
)
ncStatusDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStatusDegraded.setStatus("deprecated")
_NcStatusDown_Type = FaultStatus
_NcStatusDown_Object = MibTableColumn
ncStatusDown = _NcStatusDown_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 39, 2, 2, 1, 1, 4),
    _NcStatusDown_Type()
)
ncStatusDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncStatusDown.setStatus("deprecated")

# Managed Objects groups

ncGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 39, 1, 1, 1)
)
ncGeneralGroup.setObjects(
      *(("LUM-NC-MIB", "ncGeneralConfigLastChangeTime"),
        ("LUM-NC-MIB", "ncGeneralStateLastChangeTime"),
        ("LUM-NC-MIB", "ncGeneralStatusTableSize"))
)
if mibBuilder.loadTexts:
    ncGeneralGroup.setStatus("current")

ncStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 39, 1, 1, 2)
)
ncStatusGroup.setObjects(
      *(("LUM-NC-MIB", "ncStatusIndex"),
        ("LUM-NC-MIB", "ncStatusDegraded"),
        ("LUM-NC-MIB", "ncStatusDown"),
        ("LUM-NC-MIB", "ncStatusIncomplete"))
)
if mibBuilder.loadTexts:
    ncStatusGroup.setStatus("deprecated")

ncStatusGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 39, 1, 1, 3)
)
ncStatusGroupV2.setObjects(
      *(("LUM-NC-MIB", "ncStatusIndex"),
        ("LUM-NC-MIB", "ncStatusIncomplete"))
)
if mibBuilder.loadTexts:
    ncStatusGroupV2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumNcBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 39, 1, 2, 1)
)
lumNcBasicComplV1.setObjects(
      *(("LUM-NC-MIB", "ncGeneralGroup"),
        ("LUM-NC-MIB", "ncStatusGroup"))
)
if mibBuilder.loadTexts:
    lumNcBasicComplV1.setStatus(
        "deprecated"
    )

lumNcBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 39, 1, 2, 2)
)
lumNcBasicComplV2.setObjects(
      *(("LUM-NC-MIB", "ncGeneralGroup"),
        ("LUM-NC-MIB", "ncStatusGroupV2"))
)
if mibBuilder.loadTexts:
    lumNcBasicComplV2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-NC-MIB",
    **{"lumNcMIBModule": lumNcMIBModule,
       "lumNcConfs": lumNcConfs,
       "lumNcGroups": lumNcGroups,
       "ncGeneralGroup": ncGeneralGroup,
       "ncStatusGroup": ncStatusGroup,
       "ncStatusGroupV2": ncStatusGroupV2,
       "lumNcCompl": lumNcCompl,
       "lumNcBasicComplV1": lumNcBasicComplV1,
       "lumNcBasicComplV2": lumNcBasicComplV2,
       "lumNcMIBObjects": lumNcMIBObjects,
       "ncGeneral": ncGeneral,
       "ncGeneralConfigLastChangeTime": ncGeneralConfigLastChangeTime,
       "ncGeneralStateLastChangeTime": ncGeneralStateLastChangeTime,
       "ncGeneralStatusTableSize": ncGeneralStatusTableSize,
       "ncStatusList": ncStatusList,
       "ncStatusTable": ncStatusTable,
       "ncStatusEntry": ncStatusEntry,
       "ncStatusIndex": ncStatusIndex,
       "ncStatusIncomplete": ncStatusIncomplete,
       "ncStatusDegraded": ncStatusDegraded,
       "ncStatusDown": ncStatusDown}
)
