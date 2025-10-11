# SNMP MIB module (LUM-IFXCFLEX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-IFXCFLEX-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:56 2025
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

(lumIfXcFlexMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumIfXcFlexMIB",
    "lumModules")

(MgmtNameString,
 Unsigned32WithNA) = mibBuilder.importSymbols(
    "LUM-TC",
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

lumIfXcFlexMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 70)
)
if mibBuilder.loadTexts:
    lumIfXcFlexMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2016-08-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumIfXcFlexConfs_ObjectIdentity = ObjectIdentity
lumIfXcFlexConfs = _LumIfXcFlexConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 1)
)
_LumIfXcFlexGroups_ObjectIdentity = ObjectIdentity
lumIfXcFlexGroups = _LumIfXcFlexGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 1, 1)
)
_LumIfXcFlexCompl_ObjectIdentity = ObjectIdentity
lumIfXcFlexCompl = _LumIfXcFlexCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 1, 2)
)
_LumIfXcFlexMIBObjects_ObjectIdentity = ObjectIdentity
lumIfXcFlexMIBObjects = _LumIfXcFlexMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2)
)
_IfXcFlexGeneral_ObjectIdentity = ObjectIdentity
ifXcFlexGeneral = _IfXcFlexGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 1)
)
_IfXcFlexGeneralConfigLastChangeTime_Type = DateAndTime
_IfXcFlexGeneralConfigLastChangeTime_Object = MibScalar
ifXcFlexGeneralConfigLastChangeTime = _IfXcFlexGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 1, 1),
    _IfXcFlexGeneralConfigLastChangeTime_Type()
)
ifXcFlexGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcFlexGeneralConfigLastChangeTime.setStatus("current")
_IfXcFlexGeneralStateLastChangeTime_Type = DateAndTime
_IfXcFlexGeneralStateLastChangeTime_Object = MibScalar
ifXcFlexGeneralStateLastChangeTime = _IfXcFlexGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 1, 2),
    _IfXcFlexGeneralStateLastChangeTime_Type()
)
ifXcFlexGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcFlexGeneralStateLastChangeTime.setStatus("current")
_IfXcFlexInterfaceConfigTableSize_Type = Unsigned32
_IfXcFlexInterfaceConfigTableSize_Object = MibScalar
ifXcFlexInterfaceConfigTableSize = _IfXcFlexInterfaceConfigTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 1, 3),
    _IfXcFlexInterfaceConfigTableSize_Type()
)
ifXcFlexInterfaceConfigTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcFlexInterfaceConfigTableSize.setStatus("current")
_IfXcFlexInterfaceConfigConfigLastChangeTime_Type = DateAndTime
_IfXcFlexInterfaceConfigConfigLastChangeTime_Object = MibScalar
ifXcFlexInterfaceConfigConfigLastChangeTime = _IfXcFlexInterfaceConfigConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 1, 4),
    _IfXcFlexInterfaceConfigConfigLastChangeTime_Type()
)
ifXcFlexInterfaceConfigConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcFlexInterfaceConfigConfigLastChangeTime.setStatus("current")
_IfXcFlexInterfaceConfigStateLastChangeTime_Type = DateAndTime
_IfXcFlexInterfaceConfigStateLastChangeTime_Object = MibScalar
ifXcFlexInterfaceConfigStateLastChangeTime = _IfXcFlexInterfaceConfigStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 1, 5),
    _IfXcFlexInterfaceConfigStateLastChangeTime_Type()
)
ifXcFlexInterfaceConfigStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcFlexInterfaceConfigStateLastChangeTime.setStatus("current")
_IfXcFlexProcFuncMapTableSize_Type = Unsigned32
_IfXcFlexProcFuncMapTableSize_Object = MibScalar
ifXcFlexProcFuncMapTableSize = _IfXcFlexProcFuncMapTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 1, 6),
    _IfXcFlexProcFuncMapTableSize_Type()
)
ifXcFlexProcFuncMapTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcFlexProcFuncMapTableSize.setStatus("current")
_IfXcFlexProcFuncMapConfigLastChangeTime_Type = DateAndTime
_IfXcFlexProcFuncMapConfigLastChangeTime_Object = MibScalar
ifXcFlexProcFuncMapConfigLastChangeTime = _IfXcFlexProcFuncMapConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 1, 7),
    _IfXcFlexProcFuncMapConfigLastChangeTime_Type()
)
ifXcFlexProcFuncMapConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcFlexProcFuncMapConfigLastChangeTime.setStatus("current")
_IfXcFlexProcFuncMapStateLastChangeTime_Type = DateAndTime
_IfXcFlexProcFuncMapStateLastChangeTime_Object = MibScalar
ifXcFlexProcFuncMapStateLastChangeTime = _IfXcFlexProcFuncMapStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 1, 8),
    _IfXcFlexProcFuncMapStateLastChangeTime_Type()
)
ifXcFlexProcFuncMapStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcFlexProcFuncMapStateLastChangeTime.setStatus("current")
_IfXcFlexInterfaceConfigList_ObjectIdentity = ObjectIdentity
ifXcFlexInterfaceConfigList = _IfXcFlexInterfaceConfigList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 2)
)
_IfXcFlexInterfaceConfigTable_Object = MibTable
ifXcFlexInterfaceConfigTable = _IfXcFlexInterfaceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ifXcFlexInterfaceConfigTable.setStatus("current")
_IfXcFlexInterfaceConfigEntry_Object = MibTableRow
ifXcFlexInterfaceConfigEntry = _IfXcFlexInterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 2, 1, 1)
)
ifXcFlexInterfaceConfigEntry.setIndexNames(
    (0, "LUM-IFXCFLEX-MIB", "ifXcFlexInterfaceConfigIndex"),
)
if mibBuilder.loadTexts:
    ifXcFlexInterfaceConfigEntry.setStatus("current")
_IfXcFlexInterfaceConfigIndex_Type = Unsigned32
_IfXcFlexInterfaceConfigIndex_Object = MibTableColumn
ifXcFlexInterfaceConfigIndex = _IfXcFlexInterfaceConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 2, 1, 1, 1),
    _IfXcFlexInterfaceConfigIndex_Type()
)
ifXcFlexInterfaceConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcFlexInterfaceConfigIndex.setStatus("current")
_IfXcFlexInterfaceConfigName_Type = MgmtNameString
_IfXcFlexInterfaceConfigName_Object = MibTableColumn
ifXcFlexInterfaceConfigName = _IfXcFlexInterfaceConfigName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 2, 1, 1, 2),
    _IfXcFlexInterfaceConfigName_Type()
)
ifXcFlexInterfaceConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcFlexInterfaceConfigName.setStatus("current")
_IfXcFlexInterfaceConfigUId_Type = Unsigned32
_IfXcFlexInterfaceConfigUId_Object = MibTableColumn
ifXcFlexInterfaceConfigUId = _IfXcFlexInterfaceConfigUId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 2, 1, 1, 3),
    _IfXcFlexInterfaceConfigUId_Type()
)
ifXcFlexInterfaceConfigUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcFlexInterfaceConfigUId.setStatus("current")
_IfXcFlexInterfaceConfigProcFuncIndex_Type = Unsigned32WithNA
_IfXcFlexInterfaceConfigProcFuncIndex_Object = MibTableColumn
ifXcFlexInterfaceConfigProcFuncIndex = _IfXcFlexInterfaceConfigProcFuncIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 2, 1, 1, 4),
    _IfXcFlexInterfaceConfigProcFuncIndex_Type()
)
ifXcFlexInterfaceConfigProcFuncIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcFlexInterfaceConfigProcFuncIndex.setStatus("current")


class _IfXcFlexInterfaceConfigInterfaceType_Type(Integer32):
    """Custom type ifXcFlexInterfaceConfigInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unused", 1),
          ("client", 2),
          ("line", 3),
          ("secondaryLine", 4))
    )


_IfXcFlexInterfaceConfigInterfaceType_Type.__name__ = "Integer32"
_IfXcFlexInterfaceConfigInterfaceType_Object = MibTableColumn
ifXcFlexInterfaceConfigInterfaceType = _IfXcFlexInterfaceConfigInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 2, 1, 1, 5),
    _IfXcFlexInterfaceConfigInterfaceType_Type()
)
ifXcFlexInterfaceConfigInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcFlexInterfaceConfigInterfaceType.setStatus("current")
_IfXcFlexProcFuncMapList_ObjectIdentity = ObjectIdentity
ifXcFlexProcFuncMapList = _IfXcFlexProcFuncMapList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 3)
)
_IfXcFlexProcFuncMapTable_Object = MibTable
ifXcFlexProcFuncMapTable = _IfXcFlexProcFuncMapTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ifXcFlexProcFuncMapTable.setStatus("current")
_IfXcFlexProcFuncMapEntry_Object = MibTableRow
ifXcFlexProcFuncMapEntry = _IfXcFlexProcFuncMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 3, 1, 1)
)
ifXcFlexProcFuncMapEntry.setIndexNames(
    (0, "LUM-IFXCFLEX-MIB", "ifXcFlexProcFuncMapIndex"),
)
if mibBuilder.loadTexts:
    ifXcFlexProcFuncMapEntry.setStatus("current")
_IfXcFlexProcFuncMapIndex_Type = Unsigned32
_IfXcFlexProcFuncMapIndex_Object = MibTableColumn
ifXcFlexProcFuncMapIndex = _IfXcFlexProcFuncMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 3, 1, 1, 1),
    _IfXcFlexProcFuncMapIndex_Type()
)
ifXcFlexProcFuncMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcFlexProcFuncMapIndex.setStatus("current")
_IfXcFlexProcFuncMapName_Type = MgmtNameString
_IfXcFlexProcFuncMapName_Object = MibTableColumn
ifXcFlexProcFuncMapName = _IfXcFlexProcFuncMapName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 3, 1, 1, 2),
    _IfXcFlexProcFuncMapName_Type()
)
ifXcFlexProcFuncMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcFlexProcFuncMapName.setStatus("current")


class _IfXcFlexProcFuncMapType_Type(Integer32):
    """Custom type ifXcFlexProcFuncMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transponder", 1),
          ("muxponder", 2))
    )


_IfXcFlexProcFuncMapType_Type.__name__ = "Integer32"
_IfXcFlexProcFuncMapType_Object = MibTableColumn
ifXcFlexProcFuncMapType = _IfXcFlexProcFuncMapType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 3, 1, 1, 3),
    _IfXcFlexProcFuncMapType_Type()
)
ifXcFlexProcFuncMapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcFlexProcFuncMapType.setStatus("current")
_IfXcFlexProcFuncMapUId_Type = Unsigned32
_IfXcFlexProcFuncMapUId_Object = MibTableColumn
ifXcFlexProcFuncMapUId = _IfXcFlexProcFuncMapUId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 3, 1, 1, 4),
    _IfXcFlexProcFuncMapUId_Type()
)
ifXcFlexProcFuncMapUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcFlexProcFuncMapUId.setStatus("current")
_IfXcFlexProcFuncMapProcFuncIndex_Type = Unsigned32WithNA
_IfXcFlexProcFuncMapProcFuncIndex_Object = MibTableColumn
ifXcFlexProcFuncMapProcFuncIndex = _IfXcFlexProcFuncMapProcFuncIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 2, 3, 1, 1, 5),
    _IfXcFlexProcFuncMapProcFuncIndex_Type()
)
ifXcFlexProcFuncMapProcFuncIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifXcFlexProcFuncMapProcFuncIndex.setStatus("current")

# Managed Objects groups

ifXcFlexGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 1, 1, 1)
)
ifXcFlexGeneralGroupV1.setObjects(
      *(("LUM-IFXCFLEX-MIB", "ifXcFlexGeneralConfigLastChangeTime"),
        ("LUM-IFXCFLEX-MIB", "ifXcFlexGeneralStateLastChangeTime"),
        ("LUM-IFXCFLEX-MIB", "ifXcFlexInterfaceConfigTableSize"),
        ("LUM-IFXCFLEX-MIB", "ifXcFlexInterfaceConfigConfigLastChangeTime"),
        ("LUM-IFXCFLEX-MIB", "ifXcFlexInterfaceConfigStateLastChangeTime"),
        ("LUM-IFXCFLEX-MIB", "ifXcFlexProcFuncMapTableSize"),
        ("LUM-IFXCFLEX-MIB", "ifXcFlexProcFuncMapConfigLastChangeTime"),
        ("LUM-IFXCFLEX-MIB", "ifXcFlexProcFuncMapStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifXcFlexGeneralGroupV1.setStatus("current")

ifXcFlexInterfaceConfigGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 1, 1, 2)
)
ifXcFlexInterfaceConfigGroupV1.setObjects(
      *(("LUM-IFXCFLEX-MIB", "ifXcFlexInterfaceConfigIndex"),
        ("LUM-IFXCFLEX-MIB", "ifXcFlexInterfaceConfigName"),
        ("LUM-IFXCFLEX-MIB", "ifXcFlexInterfaceConfigUId"),
        ("LUM-IFXCFLEX-MIB", "ifXcFlexInterfaceConfigProcFuncIndex"),
        ("LUM-IFXCFLEX-MIB", "ifXcFlexInterfaceConfigInterfaceType"))
)
if mibBuilder.loadTexts:
    ifXcFlexInterfaceConfigGroupV1.setStatus("current")

ifXcFlexProcFuncMapGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 1, 1, 3)
)
ifXcFlexProcFuncMapGroupV1.setObjects(
      *(("LUM-IFXCFLEX-MIB", "ifXcFlexProcFuncMapIndex"),
        ("LUM-IFXCFLEX-MIB", "ifXcFlexProcFuncMapName"),
        ("LUM-IFXCFLEX-MIB", "ifXcFlexProcFuncMapType"),
        ("LUM-IFXCFLEX-MIB", "ifXcFlexProcFuncMapUId"),
        ("LUM-IFXCFLEX-MIB", "ifXcFlexProcFuncMapProcFuncIndex"))
)
if mibBuilder.loadTexts:
    ifXcFlexProcFuncMapGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumIfXcFlexComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 70, 1, 2, 1)
)
lumIfXcFlexComplV1.setObjects(
      *(("LUM-IFXCFLEX-MIB", "ifXcFlexGeneralGroupV1"),
        ("LUM-IFXCFLEX-MIB", "ifXcFlexInterfaceConfigGroupV1"),
        ("LUM-IFXCFLEX-MIB", "ifXcFlexProcFuncMapGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfXcFlexComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-IFXCFLEX-MIB",
    **{"lumIfXcFlexMIBModule": lumIfXcFlexMIBModule,
       "lumIfXcFlexConfs": lumIfXcFlexConfs,
       "lumIfXcFlexGroups": lumIfXcFlexGroups,
       "ifXcFlexGeneralGroupV1": ifXcFlexGeneralGroupV1,
       "ifXcFlexInterfaceConfigGroupV1": ifXcFlexInterfaceConfigGroupV1,
       "ifXcFlexProcFuncMapGroupV1": ifXcFlexProcFuncMapGroupV1,
       "lumIfXcFlexCompl": lumIfXcFlexCompl,
       "lumIfXcFlexComplV1": lumIfXcFlexComplV1,
       "lumIfXcFlexMIBObjects": lumIfXcFlexMIBObjects,
       "ifXcFlexGeneral": ifXcFlexGeneral,
       "ifXcFlexGeneralConfigLastChangeTime": ifXcFlexGeneralConfigLastChangeTime,
       "ifXcFlexGeneralStateLastChangeTime": ifXcFlexGeneralStateLastChangeTime,
       "ifXcFlexInterfaceConfigTableSize": ifXcFlexInterfaceConfigTableSize,
       "ifXcFlexInterfaceConfigConfigLastChangeTime": ifXcFlexInterfaceConfigConfigLastChangeTime,
       "ifXcFlexInterfaceConfigStateLastChangeTime": ifXcFlexInterfaceConfigStateLastChangeTime,
       "ifXcFlexProcFuncMapTableSize": ifXcFlexProcFuncMapTableSize,
       "ifXcFlexProcFuncMapConfigLastChangeTime": ifXcFlexProcFuncMapConfigLastChangeTime,
       "ifXcFlexProcFuncMapStateLastChangeTime": ifXcFlexProcFuncMapStateLastChangeTime,
       "ifXcFlexInterfaceConfigList": ifXcFlexInterfaceConfigList,
       "ifXcFlexInterfaceConfigTable": ifXcFlexInterfaceConfigTable,
       "ifXcFlexInterfaceConfigEntry": ifXcFlexInterfaceConfigEntry,
       "ifXcFlexInterfaceConfigIndex": ifXcFlexInterfaceConfigIndex,
       "ifXcFlexInterfaceConfigName": ifXcFlexInterfaceConfigName,
       "ifXcFlexInterfaceConfigUId": ifXcFlexInterfaceConfigUId,
       "ifXcFlexInterfaceConfigProcFuncIndex": ifXcFlexInterfaceConfigProcFuncIndex,
       "ifXcFlexInterfaceConfigInterfaceType": ifXcFlexInterfaceConfigInterfaceType,
       "ifXcFlexProcFuncMapList": ifXcFlexProcFuncMapList,
       "ifXcFlexProcFuncMapTable": ifXcFlexProcFuncMapTable,
       "ifXcFlexProcFuncMapEntry": ifXcFlexProcFuncMapEntry,
       "ifXcFlexProcFuncMapIndex": ifXcFlexProcFuncMapIndex,
       "ifXcFlexProcFuncMapName": ifXcFlexProcFuncMapName,
       "ifXcFlexProcFuncMapType": ifXcFlexProcFuncMapType,
       "ifXcFlexProcFuncMapUId": ifXcFlexProcFuncMapUId,
       "ifXcFlexProcFuncMapProcFuncIndex": ifXcFlexProcFuncMapProcFuncIndex}
)
