# SNMP MIB module (HPVCQOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPVCQOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:36:54 2025
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

(virtualConnect,) = mibBuilder.importSymbols(
    "HPVCMODULE-MIB",
    "virtualConnect")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 enterprises,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "enterprises",
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 RowPointer,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

vcQoSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5)
)
if mibBuilder.loadTexts:
    vcQoSMIB.setRevisions(
        ("2016-03-21 00:00",
         "2015-01-07 00:00",
         "2012-04-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VcQoSConfigType(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 1),
          ("passthrough", 2),
          ("customFCoE", 3),
          ("customNoFCoE", 4))
    )



# MIB Managed Objects in the order of their OIDs

_VcQoSMIBObjects_ObjectIdentity = ObjectIdentity
vcQoSMIBObjects = _VcQoSMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1)
)
_VcQoSConfigType_Type = VcQoSConfigType
_VcQoSConfigType_Object = MibScalar
vcQoSConfigType = _VcQoSConfigType_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 1),
    _VcQoSConfigType_Type()
)
vcQoSConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcQoSConfigType.setStatus("current")
_VcQoSIfQoSConfig_ObjectIdentity = ObjectIdentity
vcQoSIfQoSConfig = _VcQoSIfQoSConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 2)
)
_VcQoSIfQoSConfigTable_Object = MibTable
vcQoSIfQoSConfigTable = _VcQoSIfQoSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vcQoSIfQoSConfigTable.setStatus("current")
_VcQoSIfQoSConfigEntry_Object = MibTableRow
vcQoSIfQoSConfigEntry = _VcQoSIfQoSConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 2, 1, 1)
)
vcQoSIfQoSConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vcQoSIfQoSConfigEntry.setStatus("current")
_VcQoSIfQoSTrafficClassConfigIndex_Type = Integer32
_VcQoSIfQoSTrafficClassConfigIndex_Object = MibTableColumn
vcQoSIfQoSTrafficClassConfigIndex = _VcQoSIfQoSTrafficClassConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 2, 1, 1, 1),
    _VcQoSIfQoSTrafficClassConfigIndex_Type()
)
vcQoSIfQoSTrafficClassConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcQoSIfQoSTrafficClassConfigIndex.setStatus("current")
_VcQoSIfQoSClassificationMapIndex_Type = Integer32
_VcQoSIfQoSClassificationMapIndex_Object = MibTableColumn
vcQoSIfQoSClassificationMapIndex = _VcQoSIfQoSClassificationMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 2, 1, 1, 2),
    _VcQoSIfQoSClassificationMapIndex_Type()
)
vcQoSIfQoSClassificationMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcQoSIfQoSClassificationMapIndex.setStatus("current")
_VcQoSTrafficClassConfig_ObjectIdentity = ObjectIdentity
vcQoSTrafficClassConfig = _VcQoSTrafficClassConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 3)
)
_VcQoSTrafficClassConfigTable_Object = MibTable
vcQoSTrafficClassConfigTable = _VcQoSTrafficClassConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    vcQoSTrafficClassConfigTable.setStatus("current")
_VcQoSTrafficClassConfigEntry_Object = MibTableRow
vcQoSTrafficClassConfigEntry = _VcQoSTrafficClassConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 3, 1, 1)
)
vcQoSTrafficClassConfigEntry.setIndexNames(
    (0, "HPVCQOS-MIB", "vcQoSTrafficClassConfigIndex"),
)
if mibBuilder.loadTexts:
    vcQoSTrafficClassConfigEntry.setStatus("current")
_VcQoSTrafficClassConfigIndex_Type = Integer32
_VcQoSTrafficClassConfigIndex_Object = MibTableColumn
vcQoSTrafficClassConfigIndex = _VcQoSTrafficClassConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 3, 1, 1, 1),
    _VcQoSTrafficClassConfigIndex_Type()
)
vcQoSTrafficClassConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcQoSTrafficClassConfigIndex.setStatus("current")
_VcQoSTrafficClassConfigName_Type = SnmpAdminString
_VcQoSTrafficClassConfigName_Object = MibTableColumn
vcQoSTrafficClassConfigName = _VcQoSTrafficClassConfigName_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 3, 1, 1, 2),
    _VcQoSTrafficClassConfigName_Type()
)
vcQoSTrafficClassConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcQoSTrafficClassConfigName.setStatus("current")
_VcQoSTrafficClass_ObjectIdentity = ObjectIdentity
vcQoSTrafficClass = _VcQoSTrafficClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 4)
)
_VcQoSTrafficClassTable_Object = MibTable
vcQoSTrafficClassTable = _VcQoSTrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    vcQoSTrafficClassTable.setStatus("current")
_VcQoSTrafficClassEntry_Object = MibTableRow
vcQoSTrafficClassEntry = _VcQoSTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 4, 1, 1)
)
vcQoSTrafficClassEntry.setIndexNames(
    (0, "HPVCQOS-MIB", "vcQoSTrafficClassConfigIndex"),
    (0, "HPVCQOS-MIB", "vcQoSTrafficClassId"),
)
if mibBuilder.loadTexts:
    vcQoSTrafficClassEntry.setStatus("current")


class _VcQoSTrafficClassId_Type(Integer32):
    """Custom type vcQoSTrafficClassId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VcQoSTrafficClassId_Type.__name__ = "Integer32"
_VcQoSTrafficClassId_Object = MibTableColumn
vcQoSTrafficClassId = _VcQoSTrafficClassId_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 4, 1, 1, 1),
    _VcQoSTrafficClassId_Type()
)
vcQoSTrafficClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcQoSTrafficClassId.setStatus("current")
_VcQoSTrafficClassName_Type = SnmpAdminString
_VcQoSTrafficClassName_Object = MibTableColumn
vcQoSTrafficClassName = _VcQoSTrafficClassName_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 4, 1, 1, 2),
    _VcQoSTrafficClassName_Type()
)
vcQoSTrafficClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcQoSTrafficClassName.setStatus("current")
_VcQoSTrafficClassRealTime_Type = TruthValue
_VcQoSTrafficClassRealTime_Object = MibTableColumn
vcQoSTrafficClassRealTime = _VcQoSTrafficClassRealTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 4, 1, 1, 3),
    _VcQoSTrafficClassRealTime_Type()
)
vcQoSTrafficClassRealTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcQoSTrafficClassRealTime.setStatus("current")


class _VcQoSTrafficClassShare_Type(Integer32):
    """Custom type vcQoSTrafficClassShare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VcQoSTrafficClassShare_Type.__name__ = "Integer32"
_VcQoSTrafficClassShare_Object = MibTableColumn
vcQoSTrafficClassShare = _VcQoSTrafficClassShare_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 4, 1, 1, 4),
    _VcQoSTrafficClassShare_Type()
)
vcQoSTrafficClassShare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcQoSTrafficClassShare.setStatus("current")


class _VcQoSTrafficClassMaxShare_Type(Integer32):
    """Custom type vcQoSTrafficClassMaxShare based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VcQoSTrafficClassMaxShare_Type.__name__ = "Integer32"
_VcQoSTrafficClassMaxShare_Object = MibTableColumn
vcQoSTrafficClassMaxShare = _VcQoSTrafficClassMaxShare_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 4, 1, 1, 5),
    _VcQoSTrafficClassMaxShare_Type()
)
vcQoSTrafficClassMaxShare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcQoSTrafficClassMaxShare.setStatus("current")


class _VcQoSTrafficClassEgressDot1pPrio_Type(Integer32):
    """Custom type vcQoSTrafficClassEgressDot1pPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VcQoSTrafficClassEgressDot1pPrio_Type.__name__ = "Integer32"
_VcQoSTrafficClassEgressDot1pPrio_Object = MibTableColumn
vcQoSTrafficClassEgressDot1pPrio = _VcQoSTrafficClassEgressDot1pPrio_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 4, 1, 1, 6),
    _VcQoSTrafficClassEgressDot1pPrio_Type()
)
vcQoSTrafficClassEgressDot1pPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcQoSTrafficClassEgressDot1pPrio.setStatus("current")
_VcQoSTrafficClassEnabled_Type = TruthValue
_VcQoSTrafficClassEnabled_Object = MibTableColumn
vcQoSTrafficClassEnabled = _VcQoSTrafficClassEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 4, 1, 1, 7),
    _VcQoSTrafficClassEnabled_Type()
)
vcQoSTrafficClassEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcQoSTrafficClassEnabled.setStatus("current")
_VcQoSClassificationMap_ObjectIdentity = ObjectIdentity
vcQoSClassificationMap = _VcQoSClassificationMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 5)
)
_VcQoSClassificationMapTable_Object = MibTable
vcQoSClassificationMapTable = _VcQoSClassificationMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 5, 1)
)
if mibBuilder.loadTexts:
    vcQoSClassificationMapTable.setStatus("current")
_VcQoSClassificationMapEntry_Object = MibTableRow
vcQoSClassificationMapEntry = _VcQoSClassificationMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 5, 1, 1)
)
vcQoSClassificationMapEntry.setIndexNames(
    (0, "HPVCQOS-MIB", "vcQoSClassificationMapIndex"),
)
if mibBuilder.loadTexts:
    vcQoSClassificationMapEntry.setStatus("current")
_VcQoSClassificationMapIndex_Type = Integer32
_VcQoSClassificationMapIndex_Object = MibTableColumn
vcQoSClassificationMapIndex = _VcQoSClassificationMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 5, 1, 1, 1),
    _VcQoSClassificationMapIndex_Type()
)
vcQoSClassificationMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcQoSClassificationMapIndex.setStatus("current")
_VcQoSClassificationMapName_Type = SnmpAdminString
_VcQoSClassificationMapName_Object = MibTableColumn
vcQoSClassificationMapName = _VcQoSClassificationMapName_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 5, 1, 1, 2),
    _VcQoSClassificationMapName_Type()
)
vcQoSClassificationMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcQoSClassificationMapName.setStatus("current")
_VcQoSDot1pMap_ObjectIdentity = ObjectIdentity
vcQoSDot1pMap = _VcQoSDot1pMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 6)
)
_VcQoSDot1pMapTable_Object = MibTable
vcQoSDot1pMapTable = _VcQoSDot1pMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 6, 1)
)
if mibBuilder.loadTexts:
    vcQoSDot1pMapTable.setStatus("current")
_VcQoSDot1pMapEntry_Object = MibTableRow
vcQoSDot1pMapEntry = _VcQoSDot1pMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 6, 1, 1)
)
vcQoSDot1pMapEntry.setIndexNames(
    (0, "HPVCQOS-MIB", "vcQoSClassificationMapIndex"),
    (0, "HPVCQOS-MIB", "vcQoSDot1pMapPrioValue"),
)
if mibBuilder.loadTexts:
    vcQoSDot1pMapEntry.setStatus("current")


class _VcQoSDot1pMapPrioValue_Type(Integer32):
    """Custom type vcQoSDot1pMapPrioValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VcQoSDot1pMapPrioValue_Type.__name__ = "Integer32"
_VcQoSDot1pMapPrioValue_Object = MibTableColumn
vcQoSDot1pMapPrioValue = _VcQoSDot1pMapPrioValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 6, 1, 1, 1),
    _VcQoSDot1pMapPrioValue_Type()
)
vcQoSDot1pMapPrioValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcQoSDot1pMapPrioValue.setStatus("current")


class _VcQoSDot1pMapTrafficClassId_Type(Integer32):
    """Custom type vcQoSDot1pMapTrafficClassId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VcQoSDot1pMapTrafficClassId_Type.__name__ = "Integer32"
_VcQoSDot1pMapTrafficClassId_Object = MibTableColumn
vcQoSDot1pMapTrafficClassId = _VcQoSDot1pMapTrafficClassId_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 6, 1, 1, 2),
    _VcQoSDot1pMapTrafficClassId_Type()
)
vcQoSDot1pMapTrafficClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcQoSDot1pMapTrafficClassId.setStatus("current")
_VcQoSDscpMap_ObjectIdentity = ObjectIdentity
vcQoSDscpMap = _VcQoSDscpMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 7)
)
_VcQoSDscpMapTable_Object = MibTable
vcQoSDscpMapTable = _VcQoSDscpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 7, 1)
)
if mibBuilder.loadTexts:
    vcQoSDscpMapTable.setStatus("current")
_VcQoSDscpMapEntry_Object = MibTableRow
vcQoSDscpMapEntry = _VcQoSDscpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 7, 1, 1)
)
vcQoSDscpMapEntry.setIndexNames(
    (0, "HPVCQOS-MIB", "vcQoSClassificationMapIndex"),
    (0, "HPVCQOS-MIB", "vcQoSDscpMapDscpValue"),
)
if mibBuilder.loadTexts:
    vcQoSDscpMapEntry.setStatus("current")


class _VcQoSDscpMapDscpValue_Type(Integer32):
    """Custom type vcQoSDscpMapDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_VcQoSDscpMapDscpValue_Type.__name__ = "Integer32"
_VcQoSDscpMapDscpValue_Object = MibTableColumn
vcQoSDscpMapDscpValue = _VcQoSDscpMapDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 7, 1, 1, 1),
    _VcQoSDscpMapDscpValue_Type()
)
vcQoSDscpMapDscpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcQoSDscpMapDscpValue.setStatus("current")


class _VcQoSDscpMapTrafficClassId_Type(Integer32):
    """Custom type vcQoSDscpMapTrafficClassId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VcQoSDscpMapTrafficClassId_Type.__name__ = "Integer32"
_VcQoSDscpMapTrafficClassId_Object = MibTableColumn
vcQoSDscpMapTrafficClassId = _VcQoSDscpMapTrafficClassId_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 1, 7, 1, 1, 2),
    _VcQoSDscpMapTrafficClassId_Type()
)
vcQoSDscpMapTrafficClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcQoSDscpMapTrafficClassId.setStatus("current")
_VcQoSMIBConformance_ObjectIdentity = ObjectIdentity
vcQoSMIBConformance = _VcQoSMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 2)
)
_VcQoSMIBCompliances_ObjectIdentity = ObjectIdentity
vcQoSMIBCompliances = _VcQoSMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 2, 1)
)
_VcQoSMIBGroups_ObjectIdentity = ObjectIdentity
vcQoSMIBGroups = _VcQoSMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 2, 2)
)

# Managed Objects groups

vcQoSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 2, 2, 1)
)
vcQoSGroup.setObjects(
      *(("HPVCQOS-MIB", "vcQoSIfQoSConfig"),
        ("HPVCQOS-MIB", "vcQoSTrafficClassConfig"),
        ("HPVCQOS-MIB", "vcQoSTrafficClass"),
        ("HPVCQOS-MIB", "vcQoSClassificationMap"),
        ("HPVCQOS-MIB", "vcQoSDot1pMap"),
        ("HPVCQOS-MIB", "vcQoSDscpMap"))
)
if mibBuilder.loadTexts:
    vcQoSGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vcQoSMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 2, 5, 2, 1, 1)
)
vcQoSMIBCompliance.setObjects(
    ("HPVCQOS-MIB", "vcQoSGroup")
)
if mibBuilder.loadTexts:
    vcQoSMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPVCQOS-MIB",
    **{"VcQoSConfigType": VcQoSConfigType,
       "vcQoSMIB": vcQoSMIB,
       "vcQoSMIBObjects": vcQoSMIBObjects,
       "vcQoSConfigType": vcQoSConfigType,
       "vcQoSIfQoSConfig": vcQoSIfQoSConfig,
       "vcQoSIfQoSConfigTable": vcQoSIfQoSConfigTable,
       "vcQoSIfQoSConfigEntry": vcQoSIfQoSConfigEntry,
       "vcQoSIfQoSTrafficClassConfigIndex": vcQoSIfQoSTrafficClassConfigIndex,
       "vcQoSIfQoSClassificationMapIndex": vcQoSIfQoSClassificationMapIndex,
       "vcQoSTrafficClassConfig": vcQoSTrafficClassConfig,
       "vcQoSTrafficClassConfigTable": vcQoSTrafficClassConfigTable,
       "vcQoSTrafficClassConfigEntry": vcQoSTrafficClassConfigEntry,
       "vcQoSTrafficClassConfigIndex": vcQoSTrafficClassConfigIndex,
       "vcQoSTrafficClassConfigName": vcQoSTrafficClassConfigName,
       "vcQoSTrafficClass": vcQoSTrafficClass,
       "vcQoSTrafficClassTable": vcQoSTrafficClassTable,
       "vcQoSTrafficClassEntry": vcQoSTrafficClassEntry,
       "vcQoSTrafficClassId": vcQoSTrafficClassId,
       "vcQoSTrafficClassName": vcQoSTrafficClassName,
       "vcQoSTrafficClassRealTime": vcQoSTrafficClassRealTime,
       "vcQoSTrafficClassShare": vcQoSTrafficClassShare,
       "vcQoSTrafficClassMaxShare": vcQoSTrafficClassMaxShare,
       "vcQoSTrafficClassEgressDot1pPrio": vcQoSTrafficClassEgressDot1pPrio,
       "vcQoSTrafficClassEnabled": vcQoSTrafficClassEnabled,
       "vcQoSClassificationMap": vcQoSClassificationMap,
       "vcQoSClassificationMapTable": vcQoSClassificationMapTable,
       "vcQoSClassificationMapEntry": vcQoSClassificationMapEntry,
       "vcQoSClassificationMapIndex": vcQoSClassificationMapIndex,
       "vcQoSClassificationMapName": vcQoSClassificationMapName,
       "vcQoSDot1pMap": vcQoSDot1pMap,
       "vcQoSDot1pMapTable": vcQoSDot1pMapTable,
       "vcQoSDot1pMapEntry": vcQoSDot1pMapEntry,
       "vcQoSDot1pMapPrioValue": vcQoSDot1pMapPrioValue,
       "vcQoSDot1pMapTrafficClassId": vcQoSDot1pMapTrafficClassId,
       "vcQoSDscpMap": vcQoSDscpMap,
       "vcQoSDscpMapTable": vcQoSDscpMapTable,
       "vcQoSDscpMapEntry": vcQoSDscpMapEntry,
       "vcQoSDscpMapDscpValue": vcQoSDscpMapDscpValue,
       "vcQoSDscpMapTrafficClassId": vcQoSDscpMapTrafficClassId,
       "vcQoSMIBConformance": vcQoSMIBConformance,
       "vcQoSMIBCompliances": vcQoSMIBCompliances,
       "vcQoSMIBCompliance": vcQoSMIBCompliance,
       "vcQoSMIBGroups": vcQoSMIBGroups,
       "vcQoSGroup": vcQoSGroup}
)
