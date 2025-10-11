# SNMP MIB module (LUM-IFXC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-IFXC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:24 2025
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

(lumIfXcMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumIfXcMIB",
    "lumModules")

(CommandString,
 MgmtNameString,
 Unsigned32WithNA) = mibBuilder.importSymbols(
    "LUM-TC",
    "CommandString",
    "MgmtNameString",
    "Unsigned32WithNA")

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

lumIfXcMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 51)
)
if mibBuilder.loadTexts:
    lumIfXcMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2013-11-15 00:00",
         "2012-11-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumIfXcConfs_ObjectIdentity = ObjectIdentity
lumIfXcConfs = _LumIfXcConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 1)
)
_LumIfXcGroups_ObjectIdentity = ObjectIdentity
lumIfXcGroups = _LumIfXcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 1, 1)
)
_LumIfXcCompl_ObjectIdentity = ObjectIdentity
lumIfXcCompl = _LumIfXcCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 1, 2)
)
_LumIfXcMIBObjects_ObjectIdentity = ObjectIdentity
lumIfXcMIBObjects = _LumIfXcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2)
)
_IfXcGeneral_ObjectIdentity = ObjectIdentity
ifXcGeneral = _IfXcGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 1)
)
_IfXcGeneralConfigLastChangeTime_Type = DateAndTime
_IfXcGeneralConfigLastChangeTime_Object = MibScalar
ifXcGeneralConfigLastChangeTime = _IfXcGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 1, 1),
    _IfXcGeneralConfigLastChangeTime_Type()
)
ifXcGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcGeneralConfigLastChangeTime.setStatus("current")
_IfXcGeneralStateLastChangeTime_Type = DateAndTime
_IfXcGeneralStateLastChangeTime_Object = MibScalar
ifXcGeneralStateLastChangeTime = _IfXcGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 1, 2),
    _IfXcGeneralStateLastChangeTime_Type()
)
ifXcGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcGeneralStateLastChangeTime.setStatus("current")
_IfXcGeneralIfXcStaticXcOduTableSize_Type = Unsigned32
_IfXcGeneralIfXcStaticXcOduTableSize_Object = MibScalar
ifXcGeneralIfXcStaticXcOduTableSize = _IfXcGeneralIfXcStaticXcOduTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 1, 3),
    _IfXcGeneralIfXcStaticXcOduTableSize_Type()
)
ifXcGeneralIfXcStaticXcOduTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcGeneralIfXcStaticXcOduTableSize.setStatus("current")
_IfXcGeneralIfXcStaticXcOduConfigLastChangeTime_Type = DateAndTime
_IfXcGeneralIfXcStaticXcOduConfigLastChangeTime_Object = MibScalar
ifXcGeneralIfXcStaticXcOduConfigLastChangeTime = _IfXcGeneralIfXcStaticXcOduConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 1, 4),
    _IfXcGeneralIfXcStaticXcOduConfigLastChangeTime_Type()
)
ifXcGeneralIfXcStaticXcOduConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcGeneralIfXcStaticXcOduConfigLastChangeTime.setStatus("current")
_IfXcGeneralIfXcStaticXcOduStateLastChangeTime_Type = DateAndTime
_IfXcGeneralIfXcStaticXcOduStateLastChangeTime_Object = MibScalar
ifXcGeneralIfXcStaticXcOduStateLastChangeTime = _IfXcGeneralIfXcStaticXcOduStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 1, 5),
    _IfXcGeneralIfXcStaticXcOduStateLastChangeTime_Type()
)
ifXcGeneralIfXcStaticXcOduStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcGeneralIfXcStaticXcOduStateLastChangeTime.setStatus("current")
_IfXcGeneralIfXcDynamicXcOduTableSize_Type = Unsigned32
_IfXcGeneralIfXcDynamicXcOduTableSize_Object = MibScalar
ifXcGeneralIfXcDynamicXcOduTableSize = _IfXcGeneralIfXcDynamicXcOduTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 1, 6),
    _IfXcGeneralIfXcDynamicXcOduTableSize_Type()
)
ifXcGeneralIfXcDynamicXcOduTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcGeneralIfXcDynamicXcOduTableSize.setStatus("current")
_IfXcGeneralIfXcDynamicXcOduConfigLastChangeTime_Type = DateAndTime
_IfXcGeneralIfXcDynamicXcOduConfigLastChangeTime_Object = MibScalar
ifXcGeneralIfXcDynamicXcOduConfigLastChangeTime = _IfXcGeneralIfXcDynamicXcOduConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 1, 7),
    _IfXcGeneralIfXcDynamicXcOduConfigLastChangeTime_Type()
)
ifXcGeneralIfXcDynamicXcOduConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcGeneralIfXcDynamicXcOduConfigLastChangeTime.setStatus("current")
_IfXcGeneralIfXcDynamicXcOduStateLastChangeTime_Type = DateAndTime
_IfXcGeneralIfXcDynamicXcOduStateLastChangeTime_Object = MibScalar
ifXcGeneralIfXcDynamicXcOduStateLastChangeTime = _IfXcGeneralIfXcDynamicXcOduStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 1, 8),
    _IfXcGeneralIfXcDynamicXcOduStateLastChangeTime_Type()
)
ifXcGeneralIfXcDynamicXcOduStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcGeneralIfXcDynamicXcOduStateLastChangeTime.setStatus("current")
_IfXcStaticXcOduList_ObjectIdentity = ObjectIdentity
ifXcStaticXcOduList = _IfXcStaticXcOduList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 2)
)
_IfXcStaticXcOduTable_Object = MibTable
ifXcStaticXcOduTable = _IfXcStaticXcOduTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ifXcStaticXcOduTable.setStatus("current")
_IfXcStaticXcOduEntry_Object = MibTableRow
ifXcStaticXcOduEntry = _IfXcStaticXcOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 2, 1, 1)
)
ifXcStaticXcOduEntry.setIndexNames(
    (0, "LUM-IFXC-MIB", "ifXcStaticXcOduIndex"),
)
if mibBuilder.loadTexts:
    ifXcStaticXcOduEntry.setStatus("current")
_IfXcStaticXcOduIndex_Type = Unsigned32
_IfXcStaticXcOduIndex_Object = MibTableColumn
ifXcStaticXcOduIndex = _IfXcStaticXcOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 2, 1, 1, 1),
    _IfXcStaticXcOduIndex_Type()
)
ifXcStaticXcOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcStaticXcOduIndex.setStatus("current")
_IfXcStaticXcOduName_Type = MgmtNameString
_IfXcStaticXcOduName_Object = MibTableColumn
ifXcStaticXcOduName = _IfXcStaticXcOduName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 2, 1, 1, 2),
    _IfXcStaticXcOduName_Type()
)
ifXcStaticXcOduName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcStaticXcOduName.setStatus("current")
_IfXcStaticXcOduFromIndex_Type = Unsigned32WithNA
_IfXcStaticXcOduFromIndex_Object = MibTableColumn
ifXcStaticXcOduFromIndex = _IfXcStaticXcOduFromIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 2, 1, 1, 3),
    _IfXcStaticXcOduFromIndex_Type()
)
ifXcStaticXcOduFromIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcStaticXcOduFromIndex.setStatus("current")
_IfXcStaticXcOduToIndex_Type = Unsigned32WithNA
_IfXcStaticXcOduToIndex_Object = MibTableColumn
ifXcStaticXcOduToIndex = _IfXcStaticXcOduToIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 2, 1, 1, 4),
    _IfXcStaticXcOduToIndex_Type()
)
ifXcStaticXcOduToIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcStaticXcOduToIndex.setStatus("current")
_IfXcDynamicXcOduList_ObjectIdentity = ObjectIdentity
ifXcDynamicXcOduList = _IfXcDynamicXcOduList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 3)
)
_IfXcDynamicXcOduTable_Object = MibTable
ifXcDynamicXcOduTable = _IfXcDynamicXcOduTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ifXcDynamicXcOduTable.setStatus("current")
_IfXcDynamicXcOduEntry_Object = MibTableRow
ifXcDynamicXcOduEntry = _IfXcDynamicXcOduEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 3, 1, 1)
)
ifXcDynamicXcOduEntry.setIndexNames(
    (0, "LUM-IFXC-MIB", "ifXcDynamicXcOduIndex"),
)
if mibBuilder.loadTexts:
    ifXcDynamicXcOduEntry.setStatus("current")
_IfXcDynamicXcOduIndex_Type = Unsigned32
_IfXcDynamicXcOduIndex_Object = MibTableColumn
ifXcDynamicXcOduIndex = _IfXcDynamicXcOduIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 3, 1, 1, 1),
    _IfXcDynamicXcOduIndex_Type()
)
ifXcDynamicXcOduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcDynamicXcOduIndex.setStatus("current")
_IfXcDynamicXcOduName_Type = MgmtNameString
_IfXcDynamicXcOduName_Object = MibTableColumn
ifXcDynamicXcOduName = _IfXcDynamicXcOduName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 3, 1, 1, 2),
    _IfXcDynamicXcOduName_Type()
)
ifXcDynamicXcOduName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifXcDynamicXcOduName.setStatus("current")
_IfXcDynamicXcOduFromIndex_Type = Unsigned32WithNA
_IfXcDynamicXcOduFromIndex_Object = MibTableColumn
ifXcDynamicXcOduFromIndex = _IfXcDynamicXcOduFromIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 3, 1, 1, 3),
    _IfXcDynamicXcOduFromIndex_Type()
)
ifXcDynamicXcOduFromIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcDynamicXcOduFromIndex.setStatus("current")
_IfXcDynamicXcOduToIndex_Type = Unsigned32WithNA
_IfXcDynamicXcOduToIndex_Object = MibTableColumn
ifXcDynamicXcOduToIndex = _IfXcDynamicXcOduToIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 2, 3, 1, 1, 4),
    _IfXcDynamicXcOduToIndex_Type()
)
ifXcDynamicXcOduToIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifXcDynamicXcOduToIndex.setStatus("current")

# Managed Objects groups

ifXcGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 1, 1, 1)
)
ifXcGeneralGroupV1.setObjects(
      *(("LUM-IFXC-MIB", "ifXcGeneralConfigLastChangeTime"),
        ("LUM-IFXC-MIB", "ifXcGeneralStateLastChangeTime"),
        ("LUM-IFXC-MIB", "ifXcGeneralIfXcStaticXcOduTableSize"),
        ("LUM-IFXC-MIB", "ifXcGeneralIfXcStaticXcOduConfigLastChangeTime"),
        ("LUM-IFXC-MIB", "ifXcGeneralIfXcStaticXcOduStateLastChangeTime"),
        ("LUM-IFXC-MIB", "ifXcGeneralIfXcDynamicXcOduTableSize"),
        ("LUM-IFXC-MIB", "ifXcGeneralIfXcDynamicXcOduConfigLastChangeTime"),
        ("LUM-IFXC-MIB", "ifXcGeneralIfXcDynamicXcOduStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifXcGeneralGroupV1.setStatus("current")

ifXcStaticXcOduGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 1, 1, 2)
)
ifXcStaticXcOduGroupV1.setObjects(
      *(("LUM-IFXC-MIB", "ifXcStaticXcOduIndex"),
        ("LUM-IFXC-MIB", "ifXcStaticXcOduName"),
        ("LUM-IFXC-MIB", "ifXcStaticXcOduFromIndex"),
        ("LUM-IFXC-MIB", "ifXcStaticXcOduToIndex"))
)
if mibBuilder.loadTexts:
    ifXcStaticXcOduGroupV1.setStatus("current")

ifXcDynamicXcOduGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 1, 1, 3)
)
ifXcDynamicXcOduGroupV1.setObjects(
      *(("LUM-IFXC-MIB", "ifXcDynamicXcOduIndex"),
        ("LUM-IFXC-MIB", "ifXcDynamicXcOduName"),
        ("LUM-IFXC-MIB", "ifXcDynamicXcOduFromIndex"),
        ("LUM-IFXC-MIB", "ifXcDynamicXcOduToIndex"))
)
if mibBuilder.loadTexts:
    ifXcDynamicXcOduGroupV1.setStatus("deprecated")

ifXcDynamicXcOduGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 1, 1, 4)
)
ifXcDynamicXcOduGroupV2.setObjects(
      *(("LUM-IFXC-MIB", "ifXcDynamicXcOduIndex"),
        ("LUM-IFXC-MIB", "ifXcDynamicXcOduName"),
        ("LUM-IFXC-MIB", "ifXcDynamicXcOduFromIndex"),
        ("LUM-IFXC-MIB", "ifXcDynamicXcOduToIndex"))
)
if mibBuilder.loadTexts:
    ifXcDynamicXcOduGroupV2.setStatus("deprecated")

ifXcDynamicXcOduGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 1, 1, 5)
)
ifXcDynamicXcOduGroupV3.setObjects(
      *(("LUM-IFXC-MIB", "ifXcDynamicXcOduIndex"),
        ("LUM-IFXC-MIB", "ifXcDynamicXcOduName"),
        ("LUM-IFXC-MIB", "ifXcDynamicXcOduFromIndex"),
        ("LUM-IFXC-MIB", "ifXcDynamicXcOduToIndex"))
)
if mibBuilder.loadTexts:
    ifXcDynamicXcOduGroupV3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumIfXcComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 1, 2, 1)
)
lumIfXcComplV1.setObjects(
      *(("LUM-IFXC-MIB", "ifXcGeneralGroupV1"),
        ("LUM-IFXC-MIB", "ifXcStaticXcOduGroupV1"),
        ("LUM-IFXC-MIB", "ifXcDynamicXcOduGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfXcComplV1.setStatus(
        "deprecated"
    )

lumIfXcComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 1, 2, 2)
)
lumIfXcComplV2.setObjects(
      *(("LUM-IFXC-MIB", "ifXcGeneralGroupV1"),
        ("LUM-IFXC-MIB", "ifXcStaticXcOduGroupV1"),
        ("LUM-IFXC-MIB", "ifXcDynamicXcOduGroupV2"))
)
if mibBuilder.loadTexts:
    lumIfXcComplV2.setStatus(
        "deprecated"
    )

lumIfXcComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 51, 1, 2, 3)
)
lumIfXcComplV3.setObjects(
      *(("LUM-IFXC-MIB", "ifXcGeneralGroupV1"),
        ("LUM-IFXC-MIB", "ifXcStaticXcOduGroupV1"),
        ("LUM-IFXC-MIB", "ifXcDynamicXcOduGroupV3"))
)
if mibBuilder.loadTexts:
    lumIfXcComplV3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-IFXC-MIB",
    **{"lumIfXcMIBModule": lumIfXcMIBModule,
       "lumIfXcConfs": lumIfXcConfs,
       "lumIfXcGroups": lumIfXcGroups,
       "ifXcGeneralGroupV1": ifXcGeneralGroupV1,
       "ifXcStaticXcOduGroupV1": ifXcStaticXcOduGroupV1,
       "ifXcDynamicXcOduGroupV1": ifXcDynamicXcOduGroupV1,
       "ifXcDynamicXcOduGroupV2": ifXcDynamicXcOduGroupV2,
       "ifXcDynamicXcOduGroupV3": ifXcDynamicXcOduGroupV3,
       "lumIfXcCompl": lumIfXcCompl,
       "lumIfXcComplV1": lumIfXcComplV1,
       "lumIfXcComplV2": lumIfXcComplV2,
       "lumIfXcComplV3": lumIfXcComplV3,
       "lumIfXcMIBObjects": lumIfXcMIBObjects,
       "ifXcGeneral": ifXcGeneral,
       "ifXcGeneralConfigLastChangeTime": ifXcGeneralConfigLastChangeTime,
       "ifXcGeneralStateLastChangeTime": ifXcGeneralStateLastChangeTime,
       "ifXcGeneralIfXcStaticXcOduTableSize": ifXcGeneralIfXcStaticXcOduTableSize,
       "ifXcGeneralIfXcStaticXcOduConfigLastChangeTime": ifXcGeneralIfXcStaticXcOduConfigLastChangeTime,
       "ifXcGeneralIfXcStaticXcOduStateLastChangeTime": ifXcGeneralIfXcStaticXcOduStateLastChangeTime,
       "ifXcGeneralIfXcDynamicXcOduTableSize": ifXcGeneralIfXcDynamicXcOduTableSize,
       "ifXcGeneralIfXcDynamicXcOduConfigLastChangeTime": ifXcGeneralIfXcDynamicXcOduConfigLastChangeTime,
       "ifXcGeneralIfXcDynamicXcOduStateLastChangeTime": ifXcGeneralIfXcDynamicXcOduStateLastChangeTime,
       "ifXcStaticXcOduList": ifXcStaticXcOduList,
       "ifXcStaticXcOduTable": ifXcStaticXcOduTable,
       "ifXcStaticXcOduEntry": ifXcStaticXcOduEntry,
       "ifXcStaticXcOduIndex": ifXcStaticXcOduIndex,
       "ifXcStaticXcOduName": ifXcStaticXcOduName,
       "ifXcStaticXcOduFromIndex": ifXcStaticXcOduFromIndex,
       "ifXcStaticXcOduToIndex": ifXcStaticXcOduToIndex,
       "ifXcDynamicXcOduList": ifXcDynamicXcOduList,
       "ifXcDynamicXcOduTable": ifXcDynamicXcOduTable,
       "ifXcDynamicXcOduEntry": ifXcDynamicXcOduEntry,
       "ifXcDynamicXcOduIndex": ifXcDynamicXcOduIndex,
       "ifXcDynamicXcOduName": ifXcDynamicXcOduName,
       "ifXcDynamicXcOduFromIndex": ifXcDynamicXcOduFromIndex,
       "ifXcDynamicXcOduToIndex": ifXcDynamicXcOduToIndex}
)
