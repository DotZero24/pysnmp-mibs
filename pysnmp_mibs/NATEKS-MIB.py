# SNMP MIB module (NATEKS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nateks/NATEKS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:16:42 2025
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

(InterfaceIndex,
 ifDescr) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifDescr")

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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nateks = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4249)
)
if mibBuilder.loadTexts:
    nateks.setRevisions(
        ("2016-11-22 12:00",
         "2016-09-15 12:00",
         "2016-01-21 12:00",
         "2016-01-20 12:00",
         "2015-03-10 12:00",
         "2014-11-17 12:00",
         "2014-11-13 12:00",
         "2014-04-16 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IntegerNumber(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class IntegerIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class IntegerWithDecimal(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class IntegerMillis(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"


class SfpPowerMilliWatt(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-4"


# MIB Managed Objects in the order of their OIDs

_NateksTraps_ObjectIdentity = ObjectIdentity
nateksTraps = _NateksTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 0)
)
_NateksProducts_ObjectIdentity = ObjectIdentity
nateksProducts = _NateksProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 1)
)
_Megatrans3CLTU_ObjectIdentity = ObjectIdentity
megatrans3CLTU = _Megatrans3CLTU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 1, 1)
)
_Orion2LTU_ObjectIdentity = ObjectIdentity
orion2LTU = _Orion2LTU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 1, 7)
)
_Megatrans3CRGN_ObjectIdentity = ObjectIdentity
megatrans3CRGN = _Megatrans3CRGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 1, 8)
)
_Megatrans4LTU_ObjectIdentity = ObjectIdentity
megatrans4LTU = _Megatrans4LTU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 1, 11)
)
_Megatrans4RGN_ObjectIdentity = ObjectIdentity
megatrans4RGN = _Megatrans4RGN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 1, 12)
)
_Orion3LTU_ObjectIdentity = ObjectIdentity
orion3LTU = _Orion3LTU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 1, 22)
)
_Orion3NTU_ObjectIdentity = ObjectIdentity
orion3NTU = _Orion3NTU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 1, 23)
)
_Orion3repeater_ObjectIdentity = ObjectIdentity
orion3repeater = _Orion3repeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 1, 24)
)
_MiniFlex_ObjectIdentity = ObjectIdentity
miniFlex = _MiniFlex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 1, 26)
)
_NateksMgmt_ObjectIdentity = ObjectIdentity
nateksMgmt = _NateksMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 2)
)


class _SystemAlarm_Type(Integer32):
    """Custom type systemAlarm based on Integer32"""
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
        *(("no", 1),
          ("nonurgent", 2),
          ("urgent", 3),
          ("urgentAndNonurgent", 4))
    )


_SystemAlarm_Type.__name__ = "Integer32"
_SystemAlarm_Object = MibScalar
systemAlarm = _SystemAlarm_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 1),
    _SystemAlarm_Type()
)
systemAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAlarm.setStatus("current")


class _SystemReset_Type(Integer32):
    """Custom type systemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("readValue", 2))
    )


_SystemReset_Type.__name__ = "Integer32"
_SystemReset_Object = MibScalar
systemReset = _SystemReset_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 2),
    _SystemReset_Type()
)
systemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReset.setStatus("current")
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 2, 3)
)


class _Model_Type(DisplayString):
    """Custom type model based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Model_Type.__name__ = "DisplayString"
_Model_Object = MibScalar
model = _Model_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 3, 1),
    _Model_Type()
)
model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    model.setStatus("current")


class _Id_Type(DisplayString):
    """Custom type id based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Id_Type.__name__ = "DisplayString"
_Id_Object = MibScalar
id = _Id_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 3, 2),
    _Id_Type()
)
id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    id.setStatus("current")


class _HardwareVersion_Type(DisplayString):
    """Custom type hardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HardwareVersion_Type.__name__ = "DisplayString"
_HardwareVersion_Object = MibScalar
hardwareVersion = _HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 3, 3),
    _HardwareVersion_Type()
)
hardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareVersion.setStatus("current")


class _SoftwareVersion_Type(DisplayString):
    """Custom type softwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SoftwareVersion_Type.__name__ = "DisplayString"
_SoftwareVersion_Object = MibScalar
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 3, 4),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("current")


class _SoftwareDate_Type(DisplayString):
    """Custom type softwareDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SoftwareDate_Type.__name__ = "DisplayString"
_SoftwareDate_Object = MibScalar
softwareDate = _SoftwareDate_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 3, 5),
    _SoftwareDate_Type()
)
softwareDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareDate.setStatus("current")


class _ModuleType_Type(Integer32):
    """Custom type moduleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("subrack", 1),
          ("standalone", 2),
          ("standaloneSmall", 3),
          ("rackmount", 4),
          ("miniflex", 5))
    )


_ModuleType_Type.__name__ = "Integer32"
_ModuleType_Object = MibScalar
moduleType = _ModuleType_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 3, 6),
    _ModuleType_Type()
)
moduleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleType.setStatus("current")


class _SubrackAddress_Type(Integer32):
    """Custom type subrackAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SubrackAddress_Type.__name__ = "Integer32"
_SubrackAddress_Object = MibScalar
subrackAddress = _SubrackAddress_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 3, 7),
    _SubrackAddress_Type()
)
subrackAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subrackAddress.setStatus("current")
_ErrorCode_Type = Integer32
_ErrorCode_Object = MibScalar
errorCode = _ErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 3, 8),
    _ErrorCode_Type()
)
errorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCode.setStatus("current")
_SerialNumber_Type = DisplayString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 3, 9),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4)
)


class _ConfigRW_Type(OctetString):
    """Custom type configRW based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_ConfigRW_Type.__name__ = "OctetString"
_ConfigRW_Object = MibScalar
configRW = _ConfigRW_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 1),
    _ConfigRW_Type()
)
configRW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configRW.setStatus("current")
_ConfigDefault_Type = IntegerNumber
_ConfigDefault_Object = MibScalar
configDefault = _ConfigDefault_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 2),
    _ConfigDefault_Type()
)
configDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDefault.setStatus("current")
_ConfigSystem_ObjectIdentity = ObjectIdentity
configSystem = _ConfigSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100)
)
_ConfigNumberValues_Type = IntegerNumber
_ConfigNumberValues_Object = MibScalar
configNumberValues = _ConfigNumberValues_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 1),
    _ConfigNumberValues_Type()
)
configNumberValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configNumberValues.setStatus("current")
_ConfigValueTable_Object = MibTable
configValueTable = _ConfigValueTable_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 2)
)
if mibBuilder.loadTexts:
    configValueTable.setStatus("current")
_ConfigValueEntry_Object = MibTableRow
configValueEntry = _ConfigValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 2, 1)
)
configValueEntry.setIndexNames(
    (0, "NATEKS-MIB", "valueId"),
)
if mibBuilder.loadTexts:
    configValueEntry.setStatus("current")


class _ValueId_Type(IntegerIndex):
    """Custom type valueId based on IntegerIndex"""
    subtypeSpec = IntegerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ValueId_Type.__name__ = "IntegerIndex"
_ValueId_Object = MibTableColumn
valueId = _ValueId_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 2, 1, 1),
    _ValueId_Type()
)
valueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    valueId.setStatus("current")
_ValueGroup_Type = IntegerIndex
_ValueGroup_Object = MibTableColumn
valueGroup = _ValueGroup_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 2, 1, 2),
    _ValueGroup_Type()
)
valueGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueGroup.setStatus("current")
_ValueName_Type = DisplayString
_ValueName_Object = MibTableColumn
valueName = _ValueName_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 2, 1, 3),
    _ValueName_Type()
)
valueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueName.setStatus("current")
_ValueGroupName_Type = DisplayString
_ValueGroupName_Object = MibTableColumn
valueGroupName = _ValueGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 2, 1, 4),
    _ValueGroupName_Type()
)
valueGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueGroupName.setStatus("current")


class _ValueType_Type(Integer32):
    """Custom type valueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("setNow", 1),
          ("applyConfirm", 2),
          ("afterReset", 3))
    )


_ValueType_Type.__name__ = "Integer32"
_ValueType_Object = MibTableColumn
valueType = _ValueType_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 2, 1, 5),
    _ValueType_Type()
)
valueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueType.setStatus("current")


class _ValueStatus_Type(Integer32):
    """Custom type valueStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unchanged", 1),
          ("changed", 2),
          ("applied", 3))
    )


_ValueStatus_Type.__name__ = "Integer32"
_ValueStatus_Object = MibTableColumn
valueStatus = _ValueStatus_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 2, 1, 6),
    _ValueStatus_Type()
)
valueStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueStatus.setStatus("current")


class _ValueStartup_Type(OctetString):
    """Custom type valueStartup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_ValueStartup_Type.__name__ = "OctetString"
_ValueStartup_Object = MibTableColumn
valueStartup = _ValueStartup_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 2, 1, 7),
    _ValueStartup_Type()
)
valueStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueStartup.setStatus("current")


class _ValueRunning_Type(OctetString):
    """Custom type valueRunning based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_ValueRunning_Type.__name__ = "OctetString"
_ValueRunning_Object = MibTableColumn
valueRunning = _ValueRunning_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 2, 1, 8),
    _ValueRunning_Type()
)
valueRunning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueRunning.setStatus("current")


class _ValueNew_Type(OctetString):
    """Custom type valueNew based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_ValueNew_Type.__name__ = "OctetString"
_ValueNew_Object = MibTableColumn
valueNew = _ValueNew_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 2, 1, 9),
    _ValueNew_Type()
)
valueNew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    valueNew.setStatus("current")


class _ValueBackup_Type(OctetString):
    """Custom type valueBackup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_ValueBackup_Type.__name__ = "OctetString"
_ValueBackup_Object = MibTableColumn
valueBackup = _ValueBackup_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 2, 1, 10),
    _ValueBackup_Type()
)
valueBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueBackup.setStatus("current")
_ConfigNumberGroups_Type = IntegerNumber
_ConfigNumberGroups_Object = MibScalar
configNumberGroups = _ConfigNumberGroups_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 3),
    _ConfigNumberGroups_Type()
)
configNumberGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configNumberGroups.setStatus("current")
_ConfigGroupTable_Object = MibTable
configGroupTable = _ConfigGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 4)
)
if mibBuilder.loadTexts:
    configGroupTable.setStatus("current")
_ConfigGroupEntry_Object = MibTableRow
configGroupEntry = _ConfigGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 4, 1)
)
configGroupEntry.setIndexNames(
    (0, "NATEKS-MIB", "groupId"),
)
if mibBuilder.loadTexts:
    configGroupEntry.setStatus("current")


class _GroupId_Type(IntegerIndex):
    """Custom type groupId based on IntegerIndex"""
    subtypeSpec = IntegerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GroupId_Type.__name__ = "IntegerIndex"
_GroupId_Object = MibTableColumn
groupId = _GroupId_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 4, 1, 1),
    _GroupId_Type()
)
groupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    groupId.setStatus("current")
_GroupName_Type = DisplayString
_GroupName_Object = MibTableColumn
groupName = _GroupName_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 4, 1, 2),
    _GroupName_Type()
)
groupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupName.setStatus("current")


class _GroupType_Type(Integer32):
    """Custom type groupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("setNow", 1),
          ("applyConfirm", 2),
          ("afterReset", 3))
    )


_GroupType_Type.__name__ = "Integer32"
_GroupType_Object = MibTableColumn
groupType = _GroupType_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 4, 1, 3),
    _GroupType_Type()
)
groupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupType.setStatus("current")


class _GroupStatus_Type(Integer32):
    """Custom type groupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unchanged", 1),
          ("changed", 2),
          ("applied", 3))
    )


_GroupStatus_Type.__name__ = "Integer32"
_GroupStatus_Object = MibTableColumn
groupStatus = _GroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 4, 1, 4),
    _GroupStatus_Type()
)
groupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupStatus.setStatus("current")


class _ConfigApplyAll_Type(Integer32):
    """Custom type configApplyAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("applyAll", 1),
          ("readValue", 2))
    )


_ConfigApplyAll_Type.__name__ = "Integer32"
_ConfigApplyAll_Object = MibScalar
configApplyAll = _ConfigApplyAll_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 5),
    _ConfigApplyAll_Type()
)
configApplyAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configApplyAll.setStatus("current")


class _ConfigConfirm_Type(Integer32):
    """Custom type configConfirm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("confirm", 1),
          ("readValue", 2))
    )


_ConfigConfirm_Type.__name__ = "Integer32"
_ConfigConfirm_Object = MibScalar
configConfirm = _ConfigConfirm_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 6),
    _ConfigConfirm_Type()
)
configConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configConfirm.setStatus("current")


class _ConfigBackup_Type(Integer32):
    """Custom type configBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("readValue", 2))
    )


_ConfigBackup_Type.__name__ = "Integer32"
_ConfigBackup_Object = MibScalar
configBackup = _ConfigBackup_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 7),
    _ConfigBackup_Type()
)
configBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configBackup.setStatus("current")


class _ConfigRestore_Type(Integer32):
    """Custom type configRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restore", 1),
          ("readValue", 2))
    )


_ConfigRestore_Type.__name__ = "Integer32"
_ConfigRestore_Object = MibScalar
configRestore = _ConfigRestore_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 4, 100, 8),
    _ConfigRestore_Type()
)
configRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configRestore.setStatus("current")
_Stats_ObjectIdentity = ObjectIdentity
stats = _Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5)
)
_G826_ObjectIdentity = ObjectIdentity
g826 = _G826_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1)
)
_G826Number_Type = IntegerNumber
_G826Number_Object = MibScalar
g826Number = _G826Number_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 1),
    _G826Number_Type()
)
g826Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g826Number.setStatus("current")
_G826Table_Object = MibTable
g826Table = _G826Table_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 2)
)
if mibBuilder.loadTexts:
    g826Table.setStatus("deprecated")
_G826Entry_Object = MibTableRow
g826Entry = _G826Entry_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 2, 1)
)
g826Entry.setIndexNames(
    (0, "NATEKS-MIB", "g826Id"),
)
if mibBuilder.loadTexts:
    g826Entry.setStatus("deprecated")


class _G826Id_Type(IntegerIndex):
    """Custom type g826Id based on IntegerIndex"""
    subtypeSpec = IntegerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_G826Id_Type.__name__ = "IntegerIndex"
_G826Id_Object = MibTableColumn
g826Id = _G826Id_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 2, 1, 1),
    _G826Id_Type()
)
g826Id.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    g826Id.setStatus("deprecated")
_G826IfIndex_Type = InterfaceIndex
_G826IfIndex_Object = MibTableColumn
g826IfIndex = _G826IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 2, 1, 2),
    _G826IfIndex_Type()
)
g826IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g826IfIndex.setStatus("deprecated")
_G826Name_Type = DisplayString
_G826Name_Object = MibTableColumn
g826Name = _G826Name_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 2, 1, 3),
    _G826Name_Type()
)
g826Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g826Name.setStatus("deprecated")
_G826EB_Type = Gauge32
_G826EB_Object = MibTableColumn
g826EB = _G826EB_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 2, 1, 4),
    _G826EB_Type()
)
g826EB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g826EB.setStatus("deprecated")
_G826ES_Type = Gauge32
_G826ES_Object = MibTableColumn
g826ES = _G826ES_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 2, 1, 5),
    _G826ES_Type()
)
g826ES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g826ES.setStatus("deprecated")
if mibBuilder.loadTexts:
    g826ES.setUnits("s")
_G826SES_Type = Gauge32
_G826SES_Object = MibTableColumn
g826SES = _G826SES_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 2, 1, 6),
    _G826SES_Type()
)
g826SES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g826SES.setStatus("deprecated")
if mibBuilder.loadTexts:
    g826SES.setUnits("s")
_G826BBE_Type = Gauge32
_G826BBE_Object = MibTableColumn
g826BBE = _G826BBE_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 2, 1, 7),
    _G826BBE_Type()
)
g826BBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g826BBE.setStatus("deprecated")
_G826AvailableTime_Type = Gauge32
_G826AvailableTime_Object = MibTableColumn
g826AvailableTime = _G826AvailableTime_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 2, 1, 8),
    _G826AvailableTime_Type()
)
g826AvailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g826AvailableTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    g826AvailableTime.setUnits("s")
_G826UnavailableTime_Type = Gauge32
_G826UnavailableTime_Object = MibTableColumn
g826UnavailableTime = _G826UnavailableTime_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 2, 1, 9),
    _G826UnavailableTime_Type()
)
g826UnavailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    g826UnavailableTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    g826UnavailableTime.setUnits("s")


class _G826StatReset_Type(Integer32):
    """Custom type g826StatReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("readValue", 2))
    )


_G826StatReset_Type.__name__ = "Integer32"
_G826StatReset_Object = MibTableColumn
g826StatReset = _G826StatReset_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 2, 1, 10),
    _G826StatReset_Type()
)
g826StatReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    g826StatReset.setStatus("deprecated")


class _G826Reset_Type(Integer32):
    """Custom type g826Reset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("readValue", 2))
    )


_G826Reset_Type.__name__ = "Integer32"
_G826Reset_Object = MibScalar
g826Reset = _G826Reset_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 3),
    _G826Reset_Type()
)
g826Reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    g826Reset.setStatus("current")
_IfG826Table_Object = MibTable
ifG826Table = _IfG826Table_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 4)
)
if mibBuilder.loadTexts:
    ifG826Table.setStatus("current")
_IfG826Entry_Object = MibTableRow
ifG826Entry = _IfG826Entry_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 4, 1)
)
ifG826Entry.setIndexNames(
    (0, "NATEKS-MIB", "ifG826IfIndex"),
    (0, "NATEKS-MIB", "ifG826Id"),
)
if mibBuilder.loadTexts:
    ifG826Entry.setStatus("current")


class _IfG826Id_Type(IntegerIndex):
    """Custom type ifG826Id based on IntegerIndex"""
    subtypeSpec = IntegerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IfG826Id_Type.__name__ = "IntegerIndex"
_IfG826Id_Object = MibTableColumn
ifG826Id = _IfG826Id_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 4, 1, 1),
    _IfG826Id_Type()
)
ifG826Id.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifG826Id.setStatus("current")


class _IfG826IfIndex_Type(InterfaceIndex):
    """Custom type ifG826IfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IfG826IfIndex_Type.__name__ = "InterfaceIndex"
_IfG826IfIndex_Object = MibTableColumn
ifG826IfIndex = _IfG826IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 4, 1, 2),
    _IfG826IfIndex_Type()
)
ifG826IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifG826IfIndex.setStatus("current")
_IfG826Name_Type = DisplayString
_IfG826Name_Object = MibTableColumn
ifG826Name = _IfG826Name_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 4, 1, 3),
    _IfG826Name_Type()
)
ifG826Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifG826Name.setStatus("current")
_IfG826EB_Type = Gauge32
_IfG826EB_Object = MibTableColumn
ifG826EB = _IfG826EB_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 4, 1, 4),
    _IfG826EB_Type()
)
ifG826EB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifG826EB.setStatus("current")
_IfG826ES_Type = Gauge32
_IfG826ES_Object = MibTableColumn
ifG826ES = _IfG826ES_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 4, 1, 5),
    _IfG826ES_Type()
)
ifG826ES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifG826ES.setStatus("current")
if mibBuilder.loadTexts:
    ifG826ES.setUnits("s")
_IfG826SES_Type = Gauge32
_IfG826SES_Object = MibTableColumn
ifG826SES = _IfG826SES_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 4, 1, 6),
    _IfG826SES_Type()
)
ifG826SES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifG826SES.setStatus("current")
if mibBuilder.loadTexts:
    ifG826SES.setUnits("s")
_IfG826BBE_Type = Gauge32
_IfG826BBE_Object = MibTableColumn
ifG826BBE = _IfG826BBE_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 4, 1, 7),
    _IfG826BBE_Type()
)
ifG826BBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifG826BBE.setStatus("current")
_IfG826AvailableTime_Type = Gauge32
_IfG826AvailableTime_Object = MibTableColumn
ifG826AvailableTime = _IfG826AvailableTime_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 4, 1, 8),
    _IfG826AvailableTime_Type()
)
ifG826AvailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifG826AvailableTime.setStatus("current")
if mibBuilder.loadTexts:
    ifG826AvailableTime.setUnits("s")
_IfG826UnavailableTime_Type = Gauge32
_IfG826UnavailableTime_Object = MibTableColumn
ifG826UnavailableTime = _IfG826UnavailableTime_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 4, 1, 9),
    _IfG826UnavailableTime_Type()
)
ifG826UnavailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifG826UnavailableTime.setStatus("current")
if mibBuilder.loadTexts:
    ifG826UnavailableTime.setUnits("s")


class _IfG826StatReset_Type(Integer32):
    """Custom type ifG826StatReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("readValue", 2))
    )


_IfG826StatReset_Type.__name__ = "Integer32"
_IfG826StatReset_Object = MibTableColumn
ifG826StatReset = _IfG826StatReset_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 1, 4, 1, 10),
    _IfG826StatReset_Type()
)
ifG826StatReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifG826StatReset.setStatus("current")
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 2)
)
_AlarmNumber_Type = IntegerNumber
_AlarmNumber_Object = MibScalar
alarmNumber = _AlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 2, 1),
    _AlarmNumber_Type()
)
alarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmNumber.setStatus("current")
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 2, 2)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("current")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 2, 2, 1)
)
alarmEntry.setIndexNames(
    (0, "NATEKS-MIB", "alarmId"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("current")


class _AlarmId_Type(IntegerIndex):
    """Custom type alarmId based on IntegerIndex"""
    subtypeSpec = IntegerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlarmId_Type.__name__ = "IntegerIndex"
_AlarmId_Object = MibTableColumn
alarmId = _AlarmId_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 2, 2, 1, 1),
    _AlarmId_Type()
)
alarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmId.setStatus("current")
_AlarmIfIndex_Type = InterfaceIndex
_AlarmIfIndex_Object = MibTableColumn
alarmIfIndex = _AlarmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 2, 2, 1, 2),
    _AlarmIfIndex_Type()
)
alarmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIfIndex.setStatus("current")
_AlarmName_Type = DisplayString
_AlarmName_Object = MibTableColumn
alarmName = _AlarmName_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 2, 2, 1, 3),
    _AlarmName_Type()
)
alarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmName.setStatus("current")


class _AlarmValue_Type(Integer32):
    """Custom type alarmValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_AlarmValue_Type.__name__ = "Integer32"
_AlarmValue_Object = MibTableColumn
alarmValue = _AlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 2, 2, 1, 4),
    _AlarmValue_Type()
)
alarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmValue.setStatus("current")


class _AlarmCutoff_Type(Integer32):
    """Custom type alarmCutoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_AlarmCutoff_Type.__name__ = "Integer32"
_AlarmCutoff_Object = MibTableColumn
alarmCutoff = _AlarmCutoff_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 2, 2, 1, 5),
    _AlarmCutoff_Type()
)
alarmCutoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCutoff.setStatus("current")


class _AlarmType_Type(Bits):
    """Custom type alarmType based on Bits"""
    namedValues = NamedValues(
        *(("localMajor", 0),
          ("localMinor", 1),
          ("remoteMajor", 2),
          ("remoteMinor", 3),
          ("maintenance", 4))
    )

_AlarmType_Type.__name__ = "Bits"
_AlarmType_Object = MibTableColumn
alarmType = _AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 2, 2, 1, 6),
    _AlarmType_Type()
)
alarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmType.setStatus("current")


class _AlarmDisplayType_Type(Integer32):
    """Custom type alarmDisplayType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("major", 1),
          ("minor", 2),
          ("maintenance", 3))
    )


_AlarmDisplayType_Type.__name__ = "Integer32"
_AlarmDisplayType_Object = MibTableColumn
alarmDisplayType = _AlarmDisplayType_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 2, 2, 1, 7),
    _AlarmDisplayType_Type()
)
alarmDisplayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDisplayType.setStatus("current")


class _AlarmTrapEnable_Type(Integer32):
    """Custom type alarmTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_AlarmTrapEnable_Type.__name__ = "Integer32"
_AlarmTrapEnable_Object = MibScalar
alarmTrapEnable = _AlarmTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 2, 3),
    _AlarmTrapEnable_Type()
)
alarmTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmTrapEnable.setStatus("current")
_IfAlarmTable_Object = MibTable
ifAlarmTable = _IfAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 2, 4)
)
if mibBuilder.loadTexts:
    ifAlarmTable.setStatus("current")
_IfAlarmEntry_Object = MibTableRow
ifAlarmEntry = _IfAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 2, 4, 1)
)
ifAlarmEntry.setIndexNames(
    (0, "NATEKS-MIB", "ifAlarmIfIndex"),
    (0, "NATEKS-MIB", "ifAlarmId"),
)
if mibBuilder.loadTexts:
    ifAlarmEntry.setStatus("current")


class _IfAlarmId_Type(IntegerIndex):
    """Custom type ifAlarmId based on IntegerIndex"""
    subtypeSpec = IntegerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IfAlarmId_Type.__name__ = "IntegerIndex"
_IfAlarmId_Object = MibTableColumn
ifAlarmId = _IfAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 2, 4, 1, 1),
    _IfAlarmId_Type()
)
ifAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAlarmId.setStatus("current")


class _IfAlarmIfIndex_Type(InterfaceIndex):
    """Custom type ifAlarmIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IfAlarmIfIndex_Type.__name__ = "InterfaceIndex"
_IfAlarmIfIndex_Object = MibTableColumn
ifAlarmIfIndex = _IfAlarmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 2, 4, 1, 2),
    _IfAlarmIfIndex_Type()
)
ifAlarmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAlarmIfIndex.setStatus("current")
_IfAlarmName_Type = DisplayString
_IfAlarmName_Object = MibTableColumn
ifAlarmName = _IfAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 2, 4, 1, 3),
    _IfAlarmName_Type()
)
ifAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAlarmName.setStatus("current")


class _IfAlarmValue_Type(Integer32):
    """Custom type ifAlarmValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_IfAlarmValue_Type.__name__ = "Integer32"
_IfAlarmValue_Object = MibTableColumn
ifAlarmValue = _IfAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 2, 4, 1, 4),
    _IfAlarmValue_Type()
)
ifAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAlarmValue.setStatus("current")


class _IfAlarmCutoff_Type(Integer32):
    """Custom type ifAlarmCutoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_IfAlarmCutoff_Type.__name__ = "Integer32"
_IfAlarmCutoff_Object = MibTableColumn
ifAlarmCutoff = _IfAlarmCutoff_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 2, 4, 1, 5),
    _IfAlarmCutoff_Type()
)
ifAlarmCutoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAlarmCutoff.setStatus("current")


class _IfAlarmType_Type(Bits):
    """Custom type ifAlarmType based on Bits"""
    namedValues = NamedValues(
        *(("localMajor", 0),
          ("localMinor", 1),
          ("remoteMajor", 2),
          ("remoteMinor", 3),
          ("maintenance", 4))
    )

_IfAlarmType_Type.__name__ = "Bits"
_IfAlarmType_Object = MibTableColumn
ifAlarmType = _IfAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 2, 4, 1, 6),
    _IfAlarmType_Type()
)
ifAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAlarmType.setStatus("current")


class _IfAlarmDisplayType_Type(Integer32):
    """Custom type ifAlarmDisplayType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("major", 1),
          ("minor", 2),
          ("maintenance", 3))
    )


_IfAlarmDisplayType_Type.__name__ = "Integer32"
_IfAlarmDisplayType_Object = MibTableColumn
ifAlarmDisplayType = _IfAlarmDisplayType_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 2, 4, 1, 7),
    _IfAlarmDisplayType_Type()
)
ifAlarmDisplayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAlarmDisplayType.setStatus("current")
_Tlm_ObjectIdentity = ObjectIdentity
tlm = _Tlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 3)
)
_TlmNumber_Type = IntegerNumber
_TlmNumber_Object = MibScalar
tlmNumber = _TlmNumber_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 3, 1),
    _TlmNumber_Type()
)
tlmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlmNumber.setStatus("current")
_TlmTable_Object = MibTable
tlmTable = _TlmTable_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 3, 2)
)
if mibBuilder.loadTexts:
    tlmTable.setStatus("current")
_TlmEntry_Object = MibTableRow
tlmEntry = _TlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 3, 2, 1)
)
tlmEntry.setIndexNames(
    (0, "NATEKS-MIB", "tlmId"),
)
if mibBuilder.loadTexts:
    tlmEntry.setStatus("current")


class _TlmId_Type(IntegerIndex):
    """Custom type tlmId based on IntegerIndex"""
    subtypeSpec = IntegerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TlmId_Type.__name__ = "IntegerIndex"
_TlmId_Object = MibTableColumn
tlmId = _TlmId_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 3, 2, 1, 1),
    _TlmId_Type()
)
tlmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tlmId.setStatus("current")
_TlmName_Type = DisplayString
_TlmName_Object = MibTableColumn
tlmName = _TlmName_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 3, 2, 1, 2),
    _TlmName_Type()
)
tlmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlmName.setStatus("current")


class _TlmStatus_Type(Integer32):
    """Custom type tlmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("det", 3))
    )


_TlmStatus_Type.__name__ = "Integer32"
_TlmStatus_Object = MibTableColumn
tlmStatus = _TlmStatus_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 3, 2, 1, 3),
    _TlmStatus_Type()
)
tlmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlmStatus.setStatus("current")
_TlmLastStatusChange_Type = TimeTicks
_TlmLastStatusChange_Object = MibTableColumn
tlmLastStatusChange = _TlmLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 3, 2, 1, 4),
    _TlmLastStatusChange_Type()
)
tlmLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlmLastStatusChange.setStatus("current")


class _TlmSetup_Type(Integer32):
    """Custom type tlmSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalOpen", 1),
          ("normalClosed", 2))
    )


_TlmSetup_Type.__name__ = "Integer32"
_TlmSetup_Object = MibTableColumn
tlmSetup = _TlmSetup_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 3, 2, 1, 5),
    _TlmSetup_Type()
)
tlmSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlmSetup.setStatus("current")


class _TlmTrapEnable_Type(Integer32):
    """Custom type tlmTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_TlmTrapEnable_Type.__name__ = "Integer32"
_TlmTrapEnable_Object = MibTableColumn
tlmTrapEnable = _TlmTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 3, 2, 1, 6),
    _TlmTrapEnable_Type()
)
tlmTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlmTrapEnable.setStatus("current")


class _TlmClear_Type(Integer32):
    """Custom type tlmClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("readValue", 2))
    )


_TlmClear_Type.__name__ = "Integer32"
_TlmClear_Object = MibScalar
tlmClear = _TlmClear_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 3, 3),
    _TlmClear_Type()
)
tlmClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tlmClear.setStatus("current")
_Dsl_ObjectIdentity = ObjectIdentity
dsl = _Dsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4)
)
_DslChannelNumber_Type = IntegerNumber
_DslChannelNumber_Object = MibScalar
dslChannelNumber = _DslChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 1),
    _DslChannelNumber_Type()
)
dslChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslChannelNumber.setStatus("current")


class _DslUnitType_Type(Integer32):
    """Custom type dslUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modem", 1),
          ("regenerator", 2))
    )


_DslUnitType_Type.__name__ = "Integer32"
_DslUnitType_Object = MibScalar
dslUnitType = _DslUnitType_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 2),
    _DslUnitType_Type()
)
dslUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslUnitType.setStatus("current")
_DslChannelTable_Object = MibTable
dslChannelTable = _DslChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3)
)
if mibBuilder.loadTexts:
    dslChannelTable.setStatus("current")
_DslChannelEntry_Object = MibTableRow
dslChannelEntry = _DslChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1)
)
dslChannelEntry.setIndexNames(
    (0, "NATEKS-MIB", "dslChannelId"),
)
if mibBuilder.loadTexts:
    dslChannelEntry.setStatus("current")


class _DslChannelId_Type(IntegerIndex):
    """Custom type dslChannelId based on IntegerIndex"""
    subtypeSpec = IntegerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DslChannelId_Type.__name__ = "IntegerIndex"
_DslChannelId_Object = MibTableColumn
dslChannelId = _DslChannelId_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1, 1),
    _DslChannelId_Type()
)
dslChannelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dslChannelId.setStatus("current")
_DslChannelIfIndex_Type = InterfaceIndex
_DslChannelIfIndex_Object = MibTableColumn
dslChannelIfIndex = _DslChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1, 2),
    _DslChannelIfIndex_Type()
)
dslChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslChannelIfIndex.setStatus("current")


class _DslChannelMode_Type(Integer32):
    """Custom type dslChannelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_DslChannelMode_Type.__name__ = "Integer32"
_DslChannelMode_Object = MibTableColumn
dslChannelMode = _DslChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1, 3),
    _DslChannelMode_Type()
)
dslChannelMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslChannelMode.setStatus("current")


class _DslChannelStandard_Type(Integer32):
    """Custom type dslChannelStandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gshdsl", 1),
          ("gshdslBis", 2),
          ("gshdslExt", 3))
    )


_DslChannelStandard_Type.__name__ = "Integer32"
_DslChannelStandard_Object = MibTableColumn
dslChannelStandard = _DslChannelStandard_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1, 4),
    _DslChannelStandard_Type()
)
dslChannelStandard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslChannelStandard.setStatus("current")


class _DslChannelClockReference_Type(Integer32):
    """Custom type dslChannelClockReference based on Integer32"""
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
        *(("clockMode1", 1),
          ("clockMode2", 2),
          ("clockMode3a", 3),
          ("clockMode3b", 4))
    )


_DslChannelClockReference_Type.__name__ = "Integer32"
_DslChannelClockReference_Object = MibTableColumn
dslChannelClockReference = _DslChannelClockReference_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1, 5),
    _DslChannelClockReference_Type()
)
dslChannelClockReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslChannelClockReference.setStatus("current")


class _DslChannelLineCodeConfig_Type(Integer32):
    """Custom type dslChannelLineCodeConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("pam4", 2),
          ("pam8", 3),
          ("pam16", 4),
          ("pam32", 5),
          ("pam64", 6),
          ("pam128", 7))
    )


_DslChannelLineCodeConfig_Type.__name__ = "Integer32"
_DslChannelLineCodeConfig_Object = MibTableColumn
dslChannelLineCodeConfig = _DslChannelLineCodeConfig_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1, 6),
    _DslChannelLineCodeConfig_Type()
)
dslChannelLineCodeConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslChannelLineCodeConfig.setStatus("current")


class _DslChannelPSDConfig_Type(Integer32):
    """Custom type dslChannelPSDConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("annexA", 1),
          ("annexB", 2),
          ("annexAB", 3))
    )


_DslChannelPSDConfig_Type.__name__ = "Integer32"
_DslChannelPSDConfig_Object = MibTableColumn
dslChannelPSDConfig = _DslChannelPSDConfig_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1, 7),
    _DslChannelPSDConfig_Type()
)
dslChannelPSDConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslChannelPSDConfig.setStatus("current")


class _DslChannelBaserateConfig_Type(Integer32):
    """Custom type dslChannelBaserateConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DslChannelBaserateConfig_Type.__name__ = "Integer32"
_DslChannelBaserateConfig_Object = MibTableColumn
dslChannelBaserateConfig = _DslChannelBaserateConfig_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1, 8),
    _DslChannelBaserateConfig_Type()
)
dslChannelBaserateConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslChannelBaserateConfig.setStatus("current")


class _DslChannelStatus_Type(Integer32):
    """Custom type dslChannelStatus based on Integer32"""
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
        *(("down", 1),
          ("preactivation", 2),
          ("activation", 3),
          ("up", 4))
    )


_DslChannelStatus_Type.__name__ = "Integer32"
_DslChannelStatus_Object = MibTableColumn
dslChannelStatus = _DslChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1, 9),
    _DslChannelStatus_Type()
)
dslChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslChannelStatus.setStatus("current")


class _DslChannelLineCode_Type(Integer32):
    """Custom type dslChannelLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("pam4", 2),
          ("pam8", 3),
          ("pam16", 4),
          ("pam32", 5),
          ("pam64", 6),
          ("pam128", 7))
    )


_DslChannelLineCode_Type.__name__ = "Integer32"
_DslChannelLineCode_Object = MibTableColumn
dslChannelLineCode = _DslChannelLineCode_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1, 10),
    _DslChannelLineCode_Type()
)
dslChannelLineCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslChannelLineCode.setStatus("current")


class _DslChannelPSD_Type(Integer32):
    """Custom type dslChannelPSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("annexA", 1),
          ("annexB", 2),
          ("annexAB", 3))
    )


_DslChannelPSD_Type.__name__ = "Integer32"
_DslChannelPSD_Object = MibTableColumn
dslChannelPSD = _DslChannelPSD_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1, 11),
    _DslChannelPSD_Type()
)
dslChannelPSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslChannelPSD.setStatus("current")


class _DslChannelBaserate_Type(Integer32):
    """Custom type dslChannelBaserate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DslChannelBaserate_Type.__name__ = "Integer32"
_DslChannelBaserate_Object = MibTableColumn
dslChannelBaserate = _DslChannelBaserate_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1, 12),
    _DslChannelBaserate_Type()
)
dslChannelBaserate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslChannelBaserate.setStatus("current")


class _DslChannelLineRate_Type(Integer32):
    """Custom type dslChannelLineRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_DslChannelLineRate_Type.__name__ = "Integer32"
_DslChannelLineRate_Object = MibTableColumn
dslChannelLineRate = _DslChannelLineRate_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1, 13),
    _DslChannelLineRate_Type()
)
dslChannelLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslChannelLineRate.setStatus("current")
if mibBuilder.loadTexts:
    dslChannelLineRate.setUnits("kbps")


class _DslChannelPayloadRate_Type(Integer32):
    """Custom type dslChannelPayloadRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_DslChannelPayloadRate_Type.__name__ = "Integer32"
_DslChannelPayloadRate_Object = MibTableColumn
dslChannelPayloadRate = _DslChannelPayloadRate_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1, 14),
    _DslChannelPayloadRate_Type()
)
dslChannelPayloadRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslChannelPayloadRate.setStatus("current")
if mibBuilder.loadTexts:
    dslChannelPayloadRate.setUnits("kbps")
_DslChannelNMR_Type = Integer32
_DslChannelNMR_Object = MibTableColumn
dslChannelNMR = _DslChannelNMR_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1, 15),
    _DslChannelNMR_Type()
)
dslChannelNMR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslChannelNMR.setStatus("current")
if mibBuilder.loadTexts:
    dslChannelNMR.setUnits("dB")
_DslChannelPowerBackoff_Type = Integer32
_DslChannelPowerBackoff_Object = MibTableColumn
dslChannelPowerBackoff = _DslChannelPowerBackoff_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1, 16),
    _DslChannelPowerBackoff_Type()
)
dslChannelPowerBackoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslChannelPowerBackoff.setStatus("current")
if mibBuilder.loadTexts:
    dslChannelPowerBackoff.setUnits("dB")
_DslChannelFarEndPowerBackoff_Type = Integer32
_DslChannelFarEndPowerBackoff_Object = MibTableColumn
dslChannelFarEndPowerBackoff = _DslChannelFarEndPowerBackoff_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1, 17),
    _DslChannelFarEndPowerBackoff_Type()
)
dslChannelFarEndPowerBackoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslChannelFarEndPowerBackoff.setStatus("current")
if mibBuilder.loadTexts:
    dslChannelFarEndPowerBackoff.setUnits("dB")
_DslChannelLoopAttenuation_Type = Integer32
_DslChannelLoopAttenuation_Object = MibTableColumn
dslChannelLoopAttenuation = _DslChannelLoopAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1, 18),
    _DslChannelLoopAttenuation_Type()
)
dslChannelLoopAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslChannelLoopAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    dslChannelLoopAttenuation.setUnits("dB")


class _DslChannelEOCNumber_Type(IntegerIndex):
    """Custom type dslChannelEOCNumber based on IntegerIndex"""
    subtypeSpec = IntegerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DslChannelEOCNumber_Type.__name__ = "IntegerIndex"
_DslChannelEOCNumber_Object = MibTableColumn
dslChannelEOCNumber = _DslChannelEOCNumber_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1, 19),
    _DslChannelEOCNumber_Type()
)
dslChannelEOCNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslChannelEOCNumber.setStatus("current")
_DslChannelRegeneratorNumber_Type = IntegerNumber
_DslChannelRegeneratorNumber_Object = MibTableColumn
dslChannelRegeneratorNumber = _DslChannelRegeneratorNumber_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1, 20),
    _DslChannelRegeneratorNumber_Type()
)
dslChannelRegeneratorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslChannelRegeneratorNumber.setStatus("current")


class _DslChannelRemotePower_Type(Integer32):
    """Custom type dslChannelRemotePower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("alarm", 3))
    )


_DslChannelRemotePower_Type.__name__ = "Integer32"
_DslChannelRemotePower_Object = MibTableColumn
dslChannelRemotePower = _DslChannelRemotePower_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1, 21),
    _DslChannelRemotePower_Type()
)
dslChannelRemotePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslChannelRemotePower.setStatus("current")
_DslChannelRemotePowerVoltage_Type = Integer32
_DslChannelRemotePowerVoltage_Object = MibTableColumn
dslChannelRemotePowerVoltage = _DslChannelRemotePowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 3, 1, 22),
    _DslChannelRemotePowerVoltage_Type()
)
dslChannelRemotePowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslChannelRemotePowerVoltage.setStatus("current")
_DslGroupNumber_Type = IntegerNumber
_DslGroupNumber_Object = MibScalar
dslGroupNumber = _DslGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 4),
    _DslGroupNumber_Type()
)
dslGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslGroupNumber.setStatus("current")
_DslGroupTable_Object = MibTable
dslGroupTable = _DslGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 5)
)
if mibBuilder.loadTexts:
    dslGroupTable.setStatus("current")
_DslGroupEntry_Object = MibTableRow
dslGroupEntry = _DslGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 5, 1)
)
dslGroupEntry.setIndexNames(
    (0, "NATEKS-MIB", "dslGroupId"),
)
if mibBuilder.loadTexts:
    dslGroupEntry.setStatus("current")


class _DslGroupId_Type(IntegerIndex):
    """Custom type dslGroupId based on IntegerIndex"""
    subtypeSpec = IntegerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DslGroupId_Type.__name__ = "IntegerIndex"
_DslGroupId_Object = MibTableColumn
dslGroupId = _DslGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 5, 1, 1),
    _DslGroupId_Type()
)
dslGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dslGroupId.setStatus("current")


class _DslGroupType_Type(Integer32):
    """Custom type dslGroupType based on Integer32"""
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
        *(("type4wire", 1),
          ("type2pair", 2),
          ("type3pair", 3),
          ("type4pair", 4))
    )


_DslGroupType_Type.__name__ = "Integer32"
_DslGroupType_Object = MibTableColumn
dslGroupType = _DslGroupType_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 5, 1, 2),
    _DslGroupType_Type()
)
dslGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslGroupType.setStatus("current")
_DslGroupMainChannel_Type = IntegerIndex
_DslGroupMainChannel_Object = MibTableColumn
dslGroupMainChannel = _DslGroupMainChannel_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 5, 1, 3),
    _DslGroupMainChannel_Type()
)
dslGroupMainChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslGroupMainChannel.setStatus("current")
_DslGroupChannel1_Type = IntegerIndex
_DslGroupChannel1_Object = MibTableColumn
dslGroupChannel1 = _DslGroupChannel1_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 5, 1, 4),
    _DslGroupChannel1_Type()
)
dslGroupChannel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslGroupChannel1.setStatus("current")
_DslGroupChannel2_Type = IntegerIndex
_DslGroupChannel2_Object = MibTableColumn
dslGroupChannel2 = _DslGroupChannel2_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 5, 1, 5),
    _DslGroupChannel2_Type()
)
dslGroupChannel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslGroupChannel2.setStatus("current")
_DslGroupChannel3_Type = IntegerIndex
_DslGroupChannel3_Object = MibTableColumn
dslGroupChannel3 = _DslGroupChannel3_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 5, 1, 6),
    _DslGroupChannel3_Type()
)
dslGroupChannel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslGroupChannel3.setStatus("current")
_DslGroupChannel4_Type = IntegerIndex
_DslGroupChannel4_Object = MibTableColumn
dslGroupChannel4 = _DslGroupChannel4_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 5, 1, 7),
    _DslGroupChannel4_Type()
)
dslGroupChannel4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslGroupChannel4.setStatus("current")
_DslRegenerationChannels_Type = IntegerNumber
_DslRegenerationChannels_Object = MibScalar
dslRegenerationChannels = _DslRegenerationChannels_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 6),
    _DslRegenerationChannels_Type()
)
dslRegenerationChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslRegenerationChannels.setStatus("current")
_DslRegenerationTable_Object = MibTable
dslRegenerationTable = _DslRegenerationTable_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 7)
)
if mibBuilder.loadTexts:
    dslRegenerationTable.setStatus("current")
_DslRegenerationEntry_Object = MibTableRow
dslRegenerationEntry = _DslRegenerationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 7, 1)
)
dslRegenerationEntry.setIndexNames(
    (0, "NATEKS-MIB", "dslRegenerationId"),
)
if mibBuilder.loadTexts:
    dslRegenerationEntry.setStatus("current")


class _DslRegenerationId_Type(IntegerIndex):
    """Custom type dslRegenerationId based on IntegerIndex"""
    subtypeSpec = IntegerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DslRegenerationId_Type.__name__ = "IntegerIndex"
_DslRegenerationId_Object = MibTableColumn
dslRegenerationId = _DslRegenerationId_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 7, 1, 1),
    _DslRegenerationId_Type()
)
dslRegenerationId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dslRegenerationId.setStatus("current")
_DslRegenerationSide1_Type = IntegerIndex
_DslRegenerationSide1_Object = MibTableColumn
dslRegenerationSide1 = _DslRegenerationSide1_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 7, 1, 2),
    _DslRegenerationSide1_Type()
)
dslRegenerationSide1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslRegenerationSide1.setStatus("current")
_DslRegenerationSide2_Type = IntegerIndex
_DslRegenerationSide2_Object = MibTableColumn
dslRegenerationSide2 = _DslRegenerationSide2_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 4, 7, 1, 3),
    _DslRegenerationSide2_Type()
)
dslRegenerationSide2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dslRegenerationSide2.setStatus("current")
_Indication_ObjectIdentity = ObjectIdentity
indication = _Indication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 5)
)
_IndicationLedNumber_Type = IntegerNumber
_IndicationLedNumber_Object = MibScalar
indicationLedNumber = _IndicationLedNumber_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 5, 1),
    _IndicationLedNumber_Type()
)
indicationLedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    indicationLedNumber.setStatus("current")
_IndicationLedTable_Object = MibTable
indicationLedTable = _IndicationLedTable_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 5, 2)
)
if mibBuilder.loadTexts:
    indicationLedTable.setStatus("current")
_IndicationLedEntry_Object = MibTableRow
indicationLedEntry = _IndicationLedEntry_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 5, 2, 1)
)
indicationLedEntry.setIndexNames(
    (0, "NATEKS-MIB", "indicationLedId"),
)
if mibBuilder.loadTexts:
    indicationLedEntry.setStatus("current")


class _IndicationLedId_Type(IntegerIndex):
    """Custom type indicationLedId based on IntegerIndex"""
    subtypeSpec = IntegerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IndicationLedId_Type.__name__ = "IntegerIndex"
_IndicationLedId_Object = MibTableColumn
indicationLedId = _IndicationLedId_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 5, 2, 1, 1),
    _IndicationLedId_Type()
)
indicationLedId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    indicationLedId.setStatus("current")
_IndicationLedDescription_Type = DisplayString
_IndicationLedDescription_Object = MibTableColumn
indicationLedDescription = _IndicationLedDescription_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 5, 2, 1, 2),
    _IndicationLedDescription_Type()
)
indicationLedDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    indicationLedDescription.setStatus("current")


class _IndicationLedState_Type(Integer32):
    """Custom type indicationLedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("notPopulated", 0),
          ("off", 1),
          ("red", 2),
          ("yellow", 3),
          ("green", 4),
          ("cyan", 5),
          ("blue", 6),
          ("magenta", 7),
          ("white", 8))
    )


_IndicationLedState_Type.__name__ = "Integer32"
_IndicationLedState_Object = MibTableColumn
indicationLedState = _IndicationLedState_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 5, 2, 1, 3),
    _IndicationLedState_Type()
)
indicationLedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    indicationLedState.setStatus("current")


class _IndicationLedFlash_Type(Integer32):
    """Custom type indicationLedFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("notPopulated", 0),
          ("blink1000", 1),
          ("blink0100", 2),
          ("blink1100", 3),
          ("blink0010", 4),
          ("blink1010", 5),
          ("blink0110", 6),
          ("blink1110", 7),
          ("blink0001", 8),
          ("blink1001", 9),
          ("blink0101", 10),
          ("blink1101", 11),
          ("blink0011", 12),
          ("blink1011", 13),
          ("blink0111", 14),
          ("constant", 15))
    )


_IndicationLedFlash_Type.__name__ = "Integer32"
_IndicationLedFlash_Object = MibTableColumn
indicationLedFlash = _IndicationLedFlash_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 5, 2, 1, 4),
    _IndicationLedFlash_Type()
)
indicationLedFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    indicationLedFlash.setStatus("current")
_Temperature_ObjectIdentity = ObjectIdentity
temperature = _Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 6)
)
_TemperatureSensorNumber_Type = IntegerNumber
_TemperatureSensorNumber_Object = MibScalar
temperatureSensorNumber = _TemperatureSensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 6, 1),
    _TemperatureSensorNumber_Type()
)
temperatureSensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorNumber.setStatus("current")
_TemperatureSensorTable_Object = MibTable
temperatureSensorTable = _TemperatureSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 6, 2)
)
if mibBuilder.loadTexts:
    temperatureSensorTable.setStatus("current")
_TemperatureSensorEntry_Object = MibTableRow
temperatureSensorEntry = _TemperatureSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 6, 2, 1)
)
temperatureSensorEntry.setIndexNames(
    (0, "NATEKS-MIB", "temperatureSensorId"),
)
if mibBuilder.loadTexts:
    temperatureSensorEntry.setStatus("current")


class _TemperatureSensorId_Type(IntegerIndex):
    """Custom type temperatureSensorId based on IntegerIndex"""
    subtypeSpec = IntegerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TemperatureSensorId_Type.__name__ = "IntegerIndex"
_TemperatureSensorId_Object = MibTableColumn
temperatureSensorId = _TemperatureSensorId_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 6, 2, 1, 1),
    _TemperatureSensorId_Type()
)
temperatureSensorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    temperatureSensorId.setStatus("current")
_TemperatureSensorDescription_Type = DisplayString
_TemperatureSensorDescription_Object = MibTableColumn
temperatureSensorDescription = _TemperatureSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 6, 2, 1, 2),
    _TemperatureSensorDescription_Type()
)
temperatureSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorDescription.setStatus("current")
_TemperatureSensorValue_Type = IntegerMillis
_TemperatureSensorValue_Object = MibTableColumn
temperatureSensorValue = _TemperatureSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 6, 2, 1, 3),
    _TemperatureSensorValue_Type()
)
temperatureSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorValue.setStatus("current")
if mibBuilder.loadTexts:
    temperatureSensorValue.setUnits("C")
_Time_ObjectIdentity = ObjectIdentity
time = _Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 7)
)
_TimeSourceNumber_Type = IntegerNumber
_TimeSourceNumber_Object = MibScalar
timeSourceNumber = _TimeSourceNumber_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 7, 1),
    _TimeSourceNumber_Type()
)
timeSourceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeSourceNumber.setStatus("current")
_TimeSourceTable_Object = MibTable
timeSourceTable = _TimeSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 7, 2)
)
if mibBuilder.loadTexts:
    timeSourceTable.setStatus("current")
_TimeSourceEntry_Object = MibTableRow
timeSourceEntry = _TimeSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 7, 2, 1)
)
timeSourceEntry.setIndexNames(
    (0, "NATEKS-MIB", "timeSourceId"),
)
if mibBuilder.loadTexts:
    timeSourceEntry.setStatus("current")


class _TimeSourceId_Type(IntegerIndex):
    """Custom type timeSourceId based on IntegerIndex"""
    subtypeSpec = IntegerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TimeSourceId_Type.__name__ = "IntegerIndex"
_TimeSourceId_Object = MibTableColumn
timeSourceId = _TimeSourceId_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 7, 2, 1, 1),
    _TimeSourceId_Type()
)
timeSourceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeSourceId.setStatus("current")
_TimeSourceName_Type = DisplayString
_TimeSourceName_Object = MibTableColumn
timeSourceName = _TimeSourceName_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 7, 2, 1, 2),
    _TimeSourceName_Type()
)
timeSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeSourceName.setStatus("current")


class _TimeSourceStratum_Type(Integer32):
    """Custom type timeSourceStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TimeSourceStratum_Type.__name__ = "Integer32"
_TimeSourceStratum_Object = MibTableColumn
timeSourceStratum = _TimeSourceStratum_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 7, 2, 1, 3),
    _TimeSourceStratum_Type()
)
timeSourceStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeSourceStratum.setStatus("current")
_TimeSourceValue_Type = DateAndTime
_TimeSourceValue_Object = MibTableColumn
timeSourceValue = _TimeSourceValue_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 7, 2, 1, 4),
    _TimeSourceValue_Type()
)
timeSourceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeSourceValue.setStatus("current")


class _TimeZone_Type(Integer32):
    """Custom type timeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1440, 1440),
    )


_TimeZone_Type.__name__ = "Integer32"
_TimeZone_Object = MibScalar
timeZone = _TimeZone_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 7, 3),
    _TimeZone_Type()
)
timeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeZone.setStatus("current")
_LocalPower_ObjectIdentity = ObjectIdentity
localPower = _LocalPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 8)
)
_PowerSourceNumber_Type = IntegerNumber
_PowerSourceNumber_Object = MibScalar
powerSourceNumber = _PowerSourceNumber_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 8, 1),
    _PowerSourceNumber_Type()
)
powerSourceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSourceNumber.setStatus("current")
_PowerSourceTable_Object = MibTable
powerSourceTable = _PowerSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 8, 2)
)
if mibBuilder.loadTexts:
    powerSourceTable.setStatus("current")
_PowerSourceEntry_Object = MibTableRow
powerSourceEntry = _PowerSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 8, 2, 1)
)
powerSourceEntry.setIndexNames(
    (0, "NATEKS-MIB", "powerSourceId"),
)
if mibBuilder.loadTexts:
    powerSourceEntry.setStatus("current")


class _PowerSourceId_Type(IntegerIndex):
    """Custom type powerSourceId based on IntegerIndex"""
    subtypeSpec = IntegerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PowerSourceId_Type.__name__ = "IntegerIndex"
_PowerSourceId_Object = MibTableColumn
powerSourceId = _PowerSourceId_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 8, 2, 1, 1),
    _PowerSourceId_Type()
)
powerSourceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    powerSourceId.setStatus("current")
_PowerSourceName_Type = DisplayString
_PowerSourceName_Object = MibTableColumn
powerSourceName = _PowerSourceName_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 8, 2, 1, 2),
    _PowerSourceName_Type()
)
powerSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSourceName.setStatus("current")
_PowerSourceNominalVoltage_Type = Integer32
_PowerSourceNominalVoltage_Object = MibTableColumn
powerSourceNominalVoltage = _PowerSourceNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 8, 2, 1, 3),
    _PowerSourceNominalVoltage_Type()
)
powerSourceNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSourceNominalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    powerSourceNominalVoltage.setUnits("V")


class _PowerSourceStatus_Type(Integer32):
    """Custom type powerSourceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2))
    )


_PowerSourceStatus_Type.__name__ = "Integer32"
_PowerSourceStatus_Object = MibTableColumn
powerSourceStatus = _PowerSourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 8, 2, 1, 4),
    _PowerSourceStatus_Type()
)
powerSourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSourceStatus.setStatus("current")
_SfpDDM_ObjectIdentity = ObjectIdentity
sfpDDM = _SfpDDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 9)
)
_SfpDDMNumber_Type = IntegerNumber
_SfpDDMNumber_Object = MibScalar
sfpDDMNumber = _SfpDDMNumber_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 9, 1),
    _SfpDDMNumber_Type()
)
sfpDDMNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDDMNumber.setStatus("current")
_SfpDDMTable_Object = MibTable
sfpDDMTable = _SfpDDMTable_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 9, 2)
)
if mibBuilder.loadTexts:
    sfpDDMTable.setStatus("current")
_SfpDDMEntry_Object = MibTableRow
sfpDDMEntry = _SfpDDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 9, 2, 1)
)
sfpDDMEntry.setIndexNames(
    (0, "NATEKS-MIB", "sfpDDMId"),
)
if mibBuilder.loadTexts:
    sfpDDMEntry.setStatus("current")


class _SfpDDMId_Type(IntegerIndex):
    """Custom type sfpDDMId based on IntegerIndex"""
    subtypeSpec = IntegerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SfpDDMId_Type.__name__ = "IntegerIndex"
_SfpDDMId_Object = MibTableColumn
sfpDDMId = _SfpDDMId_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 9, 2, 1, 1),
    _SfpDDMId_Type()
)
sfpDDMId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sfpDDMId.setStatus("current")


class _SfpDDMTemperature_Type(IntegerMillis):
    """Custom type sfpDDMTemperature based on IntegerMillis"""
    subtypeSpec = IntegerMillis.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_SfpDDMTemperature_Type.__name__ = "IntegerMillis"
_SfpDDMTemperature_Object = MibTableColumn
sfpDDMTemperature = _SfpDDMTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 9, 2, 1, 2),
    _SfpDDMTemperature_Type()
)
sfpDDMTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDDMTemperature.setStatus("current")
if mibBuilder.loadTexts:
    sfpDDMTemperature.setUnits("C")


class _SfpDDMSupplyVoltage_Type(IntegerMillis):
    """Custom type sfpDDMSupplyVoltage based on IntegerMillis"""
    subtypeSpec = IntegerMillis.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDDMSupplyVoltage_Type.__name__ = "IntegerMillis"
_SfpDDMSupplyVoltage_Object = MibTableColumn
sfpDDMSupplyVoltage = _SfpDDMSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 9, 2, 1, 3),
    _SfpDDMSupplyVoltage_Type()
)
sfpDDMSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDDMSupplyVoltage.setStatus("current")
if mibBuilder.loadTexts:
    sfpDDMSupplyVoltage.setUnits("V")


class _SfpDDMTxBiasCurrent_Type(IntegerWithDecimal):
    """Custom type sfpDDMTxBiasCurrent based on IntegerWithDecimal"""
    subtypeSpec = IntegerWithDecimal.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1310),
    )


_SfpDDMTxBiasCurrent_Type.__name__ = "IntegerWithDecimal"
_SfpDDMTxBiasCurrent_Object = MibTableColumn
sfpDDMTxBiasCurrent = _SfpDDMTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 9, 2, 1, 4),
    _SfpDDMTxBiasCurrent_Type()
)
sfpDDMTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDDMTxBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    sfpDDMTxBiasCurrent.setUnits("mA")


class _SfpDDMTxOutputmW_Type(SfpPowerMilliWatt):
    """Custom type sfpDDMTxOutputmW based on SfpPowerMilliWatt"""
    subtypeSpec = SfpPowerMilliWatt.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDDMTxOutputmW_Type.__name__ = "SfpPowerMilliWatt"
_SfpDDMTxOutputmW_Object = MibTableColumn
sfpDDMTxOutputmW = _SfpDDMTxOutputmW_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 9, 2, 1, 5),
    _SfpDDMTxOutputmW_Type()
)
sfpDDMTxOutputmW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDDMTxOutputmW.setStatus("current")
if mibBuilder.loadTexts:
    sfpDDMTxOutputmW.setUnits("mW")


class _SfpDDMTxOutputdBm_Type(IntegerWithDecimal):
    """Custom type sfpDDMTxOutputdBm based on IntegerWithDecimal"""
    subtypeSpec = IntegerWithDecimal.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 82),
    )


_SfpDDMTxOutputdBm_Type.__name__ = "IntegerWithDecimal"
_SfpDDMTxOutputdBm_Object = MibTableColumn
sfpDDMTxOutputdBm = _SfpDDMTxOutputdBm_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 9, 2, 1, 6),
    _SfpDDMTxOutputdBm_Type()
)
sfpDDMTxOutputdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDDMTxOutputdBm.setStatus("current")
if mibBuilder.loadTexts:
    sfpDDMTxOutputdBm.setUnits("dBm")


class _SfpDDMRxInputmW_Type(SfpPowerMilliWatt):
    """Custom type sfpDDMRxInputmW based on SfpPowerMilliWatt"""
    subtypeSpec = SfpPowerMilliWatt.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfpDDMRxInputmW_Type.__name__ = "SfpPowerMilliWatt"
_SfpDDMRxInputmW_Object = MibTableColumn
sfpDDMRxInputmW = _SfpDDMRxInputmW_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 9, 2, 1, 7),
    _SfpDDMRxInputmW_Type()
)
sfpDDMRxInputmW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDDMRxInputmW.setStatus("current")
if mibBuilder.loadTexts:
    sfpDDMRxInputmW.setUnits("mW")


class _SfpDDMRxInputdBm_Type(IntegerWithDecimal):
    """Custom type sfpDDMRxInputdBm based on IntegerWithDecimal"""
    subtypeSpec = IntegerWithDecimal.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 82),
    )


_SfpDDMRxInputdBm_Type.__name__ = "IntegerWithDecimal"
_SfpDDMRxInputdBm_Object = MibTableColumn
sfpDDMRxInputdBm = _SfpDDMRxInputdBm_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 9, 2, 1, 8),
    _SfpDDMRxInputdBm_Type()
)
sfpDDMRxInputdBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDDMRxInputdBm.setStatus("current")
if mibBuilder.loadTexts:
    sfpDDMRxInputdBm.setUnits("dBm")


class _SfpDDMMediaType_Type(Integer32):
    """Custom type sfpDDMMediaType based on Integer32"""
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
        *(("fiber", 1),
          ("copper", 2),
          ("other", 3),
          ("unknown", 4))
    )


_SfpDDMMediaType_Type.__name__ = "Integer32"
_SfpDDMMediaType_Object = MibTableColumn
sfpDDMMediaType = _SfpDDMMediaType_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 9, 2, 1, 9),
    _SfpDDMMediaType_Type()
)
sfpDDMMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDDMMediaType.setStatus("current")


class _SfpDDMPresence_Type(Integer32):
    """Custom type sfpDDMPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("present", 1),
          ("absent", 2))
    )


_SfpDDMPresence_Type.__name__ = "Integer32"
_SfpDDMPresence_Object = MibTableColumn
sfpDDMPresence = _SfpDDMPresence_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 9, 2, 1, 10),
    _SfpDDMPresence_Type()
)
sfpDDMPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDDMPresence.setStatus("current")
_SfpDDMIfIndex_Type = InterfaceIndex
_SfpDDMIfIndex_Object = MibTableColumn
sfpDDMIfIndex = _SfpDDMIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 9, 2, 1, 11),
    _SfpDDMIfIndex_Type()
)
sfpDDMIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpDDMIfIndex.setStatus("current")
_Io_ObjectIdentity = ObjectIdentity
io = _Io_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10)
)
_IoDIn_ObjectIdentity = ObjectIdentity
ioDIn = _IoDIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10, 1)
)
_IoDInNumber_Type = IntegerNumber
_IoDInNumber_Object = MibScalar
ioDInNumber = _IoDInNumber_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10, 1, 1),
    _IoDInNumber_Type()
)
ioDInNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioDInNumber.setStatus("current")
_IoDInTable_Object = MibTable
ioDInTable = _IoDInTable_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10, 1, 2)
)
if mibBuilder.loadTexts:
    ioDInTable.setStatus("current")
_IoDInEntry_Object = MibTableRow
ioDInEntry = _IoDInEntry_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10, 1, 2, 1)
)
ioDInEntry.setIndexNames(
    (0, "NATEKS-MIB", "dInId"),
)
if mibBuilder.loadTexts:
    ioDInEntry.setStatus("current")


class _DInId_Type(IntegerIndex):
    """Custom type dInId based on IntegerIndex"""
    subtypeSpec = IntegerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DInId_Type.__name__ = "IntegerIndex"
_DInId_Object = MibTableColumn
dInId = _DInId_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10, 1, 2, 1, 1),
    _DInId_Type()
)
dInId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dInId.setStatus("current")
_DInName_Type = DisplayString
_DInName_Object = MibTableColumn
dInName = _DInName_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10, 1, 2, 1, 2),
    _DInName_Type()
)
dInName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dInName.setStatus("current")


class _DInState_Type(Integer32):
    """Custom type dInState based on Integer32"""
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
        *(("open", 1),
          ("closed", 2),
          ("high", 3),
          ("low", 4))
    )


_DInState_Type.__name__ = "Integer32"
_DInState_Object = MibTableColumn
dInState = _DInState_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10, 1, 2, 1, 3),
    _DInState_Type()
)
dInState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dInState.setStatus("current")


class _DInNormalState_Type(Integer32):
    """Custom type dInNormalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2),
          ("high", 3),
          ("low", 4),
          ("any", 5))
    )


_DInNormalState_Type.__name__ = "Integer32"
_DInNormalState_Object = MibTableColumn
dInNormalState = _DInNormalState_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10, 1, 2, 1, 4),
    _DInNormalState_Type()
)
dInNormalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dInNormalState.setStatus("current")


class _DInAlarmSeverity_Type(Integer32):
    """Custom type dInAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("nonurgent", 2),
          ("urgent", 3))
    )


_DInAlarmSeverity_Type.__name__ = "Integer32"
_DInAlarmSeverity_Object = MibTableColumn
dInAlarmSeverity = _DInAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10, 1, 2, 1, 5),
    _DInAlarmSeverity_Type()
)
dInAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dInAlarmSeverity.setStatus("current")
_DInDescription_Type = DisplayString
_DInDescription_Object = MibTableColumn
dInDescription = _DInDescription_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10, 1, 2, 1, 6),
    _DInDescription_Type()
)
dInDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dInDescription.setStatus("current")


class _DInTrapEnable_Type(Integer32):
    """Custom type dInTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_DInTrapEnable_Type.__name__ = "Integer32"
_DInTrapEnable_Object = MibTableColumn
dInTrapEnable = _DInTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10, 1, 2, 1, 7),
    _DInTrapEnable_Type()
)
dInTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dInTrapEnable.setStatus("current")
_IoDOut_ObjectIdentity = ObjectIdentity
ioDOut = _IoDOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10, 2)
)
_IoDOutNumber_Type = IntegerNumber
_IoDOutNumber_Object = MibScalar
ioDOutNumber = _IoDOutNumber_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10, 2, 1),
    _IoDOutNumber_Type()
)
ioDOutNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioDOutNumber.setStatus("current")
_IoDOutTable_Object = MibTable
ioDOutTable = _IoDOutTable_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10, 2, 2)
)
if mibBuilder.loadTexts:
    ioDOutTable.setStatus("current")
_IoDOutEntry_Object = MibTableRow
ioDOutEntry = _IoDOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10, 2, 2, 1)
)
ioDOutEntry.setIndexNames(
    (0, "NATEKS-MIB", "dOutId"),
)
if mibBuilder.loadTexts:
    ioDOutEntry.setStatus("current")


class _DOutId_Type(IntegerIndex):
    """Custom type dOutId based on IntegerIndex"""
    subtypeSpec = IntegerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DOutId_Type.__name__ = "IntegerIndex"
_DOutId_Object = MibTableColumn
dOutId = _DOutId_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10, 2, 2, 1, 1),
    _DOutId_Type()
)
dOutId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dOutId.setStatus("current")
_DOutName_Type = DisplayString
_DOutName_Object = MibTableColumn
dOutName = _DOutName_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10, 2, 2, 1, 2),
    _DOutName_Type()
)
dOutName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dOutName.setStatus("current")


class _DOutState_Type(Integer32):
    """Custom type dOutState based on Integer32"""
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
        *(("active", 1),
          ("inactive", 2),
          ("high", 3),
          ("low", 4))
    )


_DOutState_Type.__name__ = "Integer32"
_DOutState_Object = MibTableColumn
dOutState = _DOutState_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10, 2, 2, 1, 3),
    _DOutState_Type()
)
dOutState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dOutState.setStatus("current")


class _DOutNormalState_Type(Integer32):
    """Custom type dOutNormalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2),
          ("high", 3),
          ("low", 4),
          ("any", 5))
    )


_DOutNormalState_Type.__name__ = "Integer32"
_DOutNormalState_Object = MibTableColumn
dOutNormalState = _DOutNormalState_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10, 2, 2, 1, 4),
    _DOutNormalState_Type()
)
dOutNormalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dOutNormalState.setStatus("current")


class _DOutAlarmSeverity_Type(Integer32):
    """Custom type dOutAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("nonurgent", 2),
          ("urgent", 3))
    )


_DOutAlarmSeverity_Type.__name__ = "Integer32"
_DOutAlarmSeverity_Object = MibTableColumn
dOutAlarmSeverity = _DOutAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10, 2, 2, 1, 5),
    _DOutAlarmSeverity_Type()
)
dOutAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dOutAlarmSeverity.setStatus("current")
_DOutDescription_Type = DisplayString
_DOutDescription_Object = MibTableColumn
dOutDescription = _DOutDescription_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10, 2, 2, 1, 6),
    _DOutDescription_Type()
)
dOutDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dOutDescription.setStatus("current")


class _DOutTrapEnable_Type(Integer32):
    """Custom type dOutTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_DOutTrapEnable_Type.__name__ = "Integer32"
_DOutTrapEnable_Object = MibTableColumn
dOutTrapEnable = _DOutTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 10, 2, 2, 1, 7),
    _DOutTrapEnable_Type()
)
dOutTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dOutTrapEnable.setStatus("current")


class _StatReset_Type(Integer32):
    """Custom type statReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("readValue", 2))
    )


_StatReset_Type.__name__ = "Integer32"
_StatReset_Object = MibScalar
statReset = _StatReset_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 5, 11),
    _StatReset_Type()
)
statReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statReset.setStatus("current")
_Maintenance_ObjectIdentity = ObjectIdentity
maintenance = _Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 2, 6)
)
_Tftp_ObjectIdentity = ObjectIdentity
tftp = _Tftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 2, 6, 1)
)
_TftpServerIP_Type = IpAddress
_TftpServerIP_Object = MibScalar
tftpServerIP = _TftpServerIP_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 6, 1, 1),
    _TftpServerIP_Type()
)
tftpServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServerIP.setStatus("current")
_TftpSoftFileName_Type = DisplayString
_TftpSoftFileName_Object = MibScalar
tftpSoftFileName = _TftpSoftFileName_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 6, 1, 2),
    _TftpSoftFileName_Type()
)
tftpSoftFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpSoftFileName.setStatus("current")
_TftpConfFileName_Type = DisplayString
_TftpConfFileName_Object = MibScalar
tftpConfFileName = _TftpConfFileName_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 6, 1, 3),
    _TftpConfFileName_Type()
)
tftpConfFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpConfFileName.setStatus("current")
_TftpConnectionTimeout_Type = Integer32
_TftpConnectionTimeout_Object = MibScalar
tftpConnectionTimeout = _TftpConnectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 6, 1, 4),
    _TftpConnectionTimeout_Type()
)
tftpConnectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpConnectionTimeout.setStatus("current")
_TftpNumRetries_Type = Integer32
_TftpNumRetries_Object = MibScalar
tftpNumRetries = _TftpNumRetries_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 6, 1, 5),
    _TftpNumRetries_Type()
)
tftpNumRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpNumRetries.setStatus("current")


class _TftpTransCmd_Type(Integer32):
    """Custom type tftpTransCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("readValue", 2),
          ("swDownload", 3),
          ("configDownload", 4),
          ("configUpload", 5),
          ("allDownload", 6),
          ("sdSwUpload", 9),
          ("sdSwDownload", 10),
          ("sdConfigUpload", 11),
          ("sdConfigDownload", 12),
          ("sdLoaderUpload", 13),
          ("sdLoaderDownload", 14),
          ("sdCreateSnapshot", 15))
    )


_TftpTransCmd_Type.__name__ = "Integer32"
_TftpTransCmd_Object = MibScalar
tftpTransCmd = _TftpTransCmd_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 6, 1, 6),
    _TftpTransCmd_Type()
)
tftpTransCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpTransCmd.setStatus("current")


class _TftpLastOp_Type(Integer32):
    """Custom type tftpLastOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("tftpSwDownload", 3),
          ("tftpConfigDownload", 4),
          ("tftpConfigUpload", 5),
          ("otherSwDownload", 6),
          ("otherConfigDownLoad", 7),
          ("otherConfigUpload", 8),
          ("sdSwUpload", 9),
          ("sdSwDownload", 10),
          ("sdConfigUpload", 11),
          ("sdConfigDownload", 12),
          ("sdLoaderUpload", 13),
          ("sdLoaderDownload", 14),
          ("sdCreateSnapshot", 15))
    )


_TftpLastOp_Type.__name__ = "Integer32"
_TftpLastOp_Object = MibScalar
tftpLastOp = _TftpLastOp_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 6, 1, 7),
    _TftpLastOp_Type()
)
tftpLastOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpLastOp.setStatus("current")


class _TftpTransferStatus_Type(Integer32):
    """Custom type tftpTransferStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("connecting", 2),
          ("transferringData", 3),
          ("endedOk", 4),
          ("error", 5),
          ("busyByOther", 6))
    )


_TftpTransferStatus_Type.__name__ = "Integer32"
_TftpTransferStatus_Object = MibScalar
tftpTransferStatus = _TftpTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 6, 1, 8),
    _TftpTransferStatus_Type()
)
tftpTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpTransferStatus.setStatus("current")
_TftpLastOpTime_Type = TimeTicks
_TftpLastOpTime_Object = MibScalar
tftpLastOpTime = _TftpLastOpTime_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 6, 1, 9),
    _TftpLastOpTime_Type()
)
tftpLastOpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpLastOpTime.setStatus("current")


class _TftpSoftConfirm_Type(Integer32):
    """Custom type tftpSoftConfirm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("softConfirm", 1),
          ("readValue", 2))
    )


_TftpSoftConfirm_Type.__name__ = "Integer32"
_TftpSoftConfirm_Object = MibScalar
tftpSoftConfirm = _TftpSoftConfirm_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 6, 1, 10),
    _TftpSoftConfirm_Type()
)
tftpSoftConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpSoftConfirm.setStatus("current")


class _TftpProtocolVersion_Type(Integer32):
    """Custom type tftpProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("ftp", 2),
          ("sftp", 3))
    )


_TftpProtocolVersion_Type.__name__ = "Integer32"
_TftpProtocolVersion_Object = MibScalar
tftpProtocolVersion = _TftpProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 6, 1, 11),
    _TftpProtocolVersion_Type()
)
tftpProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpProtocolVersion.setStatus("current")
_TftpServerUserName_Type = DisplayString
_TftpServerUserName_Object = MibScalar
tftpServerUserName = _TftpServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 6, 1, 12),
    _TftpServerUserName_Type()
)
tftpServerUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServerUserName.setStatus("current")
_TftpServerUserPass_Type = DisplayString
_TftpServerUserPass_Object = MibScalar
tftpServerUserPass = _TftpServerUserPass_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 6, 1, 13),
    _TftpServerUserPass_Type()
)
tftpServerUserPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServerUserPass.setStatus("current")


class _TftpServerPortNumber_Type(Integer32):
    """Custom type tftpServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TftpServerPortNumber_Type.__name__ = "Integer32"
_TftpServerPortNumber_Object = MibScalar
tftpServerPortNumber = _TftpServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 6, 1, 14),
    _TftpServerPortNumber_Type()
)
tftpServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServerPortNumber.setStatus("current")
_NateksSecurity_ObjectIdentity = ObjectIdentity
nateksSecurity = _NateksSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 2, 7)
)
_MacFilter_ObjectIdentity = ObjectIdentity
macFilter = _MacFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 2, 7, 1)
)
_MacFilterConfigTable_Object = MibTable
macFilterConfigTable = _MacFilterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    macFilterConfigTable.setStatus("current")
_MacFilterConfigEntry_Object = MibTableRow
macFilterConfigEntry = _MacFilterConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 7, 1, 1, 1)
)
macFilterConfigEntry.setIndexNames(
    (0, "NATEKS-MIB", "macFilterConfigIfIndex"),
)
if mibBuilder.loadTexts:
    macFilterConfigEntry.setStatus("current")


class _MacFilterConfigIfIndex_Type(IntegerIndex):
    """Custom type macFilterConfigIfIndex based on IntegerIndex"""
    subtypeSpec = IntegerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MacFilterConfigIfIndex_Type.__name__ = "IntegerIndex"
_MacFilterConfigIfIndex_Object = MibTableColumn
macFilterConfigIfIndex = _MacFilterConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 7, 1, 1, 1, 1),
    _MacFilterConfigIfIndex_Type()
)
macFilterConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macFilterConfigIfIndex.setStatus("current")


class _MacFilterConfigStatus_Type(Integer32):
    """Custom type macFilterConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_MacFilterConfigStatus_Type.__name__ = "Integer32"
_MacFilterConfigStatus_Object = MibTableColumn
macFilterConfigStatus = _MacFilterConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 7, 1, 1, 1, 2),
    _MacFilterConfigStatus_Type()
)
macFilterConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFilterConfigStatus.setStatus("current")


class _MacFilterConfigAction_Type(Integer32):
    """Custom type macFilterConfigAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("indicate", 2),
          ("block", 3))
    )


_MacFilterConfigAction_Type.__name__ = "Integer32"
_MacFilterConfigAction_Object = MibTableColumn
macFilterConfigAction = _MacFilterConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 7, 1, 1, 1, 3),
    _MacFilterConfigAction_Type()
)
macFilterConfigAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFilterConfigAction.setStatus("current")
_MacFilterWhitelistTable_Object = MibTable
macFilterWhitelistTable = _MacFilterWhitelistTable_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 7, 1, 2)
)
if mibBuilder.loadTexts:
    macFilterWhitelistTable.setStatus("current")
_MacFilterWhitelistEntry_Object = MibTableRow
macFilterWhitelistEntry = _MacFilterWhitelistEntry_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 7, 1, 2, 1)
)
macFilterWhitelistEntry.setIndexNames(
    (0, "NATEKS-MIB", "macFilterWhitelistIfIndex"),
    (0, "NATEKS-MIB", "macFilterWhitelistIndex"),
)
if mibBuilder.loadTexts:
    macFilterWhitelistEntry.setStatus("current")


class _MacFilterWhitelistIndex_Type(IntegerIndex):
    """Custom type macFilterWhitelistIndex based on IntegerIndex"""
    subtypeSpec = IntegerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MacFilterWhitelistIndex_Type.__name__ = "IntegerIndex"
_MacFilterWhitelistIndex_Object = MibTableColumn
macFilterWhitelistIndex = _MacFilterWhitelistIndex_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 7, 1, 2, 1, 1),
    _MacFilterWhitelistIndex_Type()
)
macFilterWhitelistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macFilterWhitelistIndex.setStatus("current")


class _MacFilterWhitelistIfIndex_Type(IntegerIndex):
    """Custom type macFilterWhitelistIfIndex based on IntegerIndex"""
    subtypeSpec = IntegerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MacFilterWhitelistIfIndex_Type.__name__ = "IntegerIndex"
_MacFilterWhitelistIfIndex_Object = MibTableColumn
macFilterWhitelistIfIndex = _MacFilterWhitelistIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 7, 1, 2, 1, 2),
    _MacFilterWhitelistIfIndex_Type()
)
macFilterWhitelistIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macFilterWhitelistIfIndex.setStatus("current")
_MacFilterWhitelistMAC_Type = MacAddress
_MacFilterWhitelistMAC_Object = MibTableColumn
macFilterWhitelistMAC = _MacFilterWhitelistMAC_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 7, 1, 2, 1, 3),
    _MacFilterWhitelistMAC_Type()
)
macFilterWhitelistMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFilterWhitelistMAC.setStatus("current")
_MacFilterViolationsTable_Object = MibTable
macFilterViolationsTable = _MacFilterViolationsTable_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 7, 1, 3)
)
if mibBuilder.loadTexts:
    macFilterViolationsTable.setStatus("current")
_MacFilterViolationsEntry_Object = MibTableRow
macFilterViolationsEntry = _MacFilterViolationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 7, 1, 3, 1)
)
macFilterViolationsEntry.setIndexNames(
    (0, "NATEKS-MIB", "macFilterViolationsIndex"),
)
if mibBuilder.loadTexts:
    macFilterViolationsEntry.setStatus("current")


class _MacFilterViolationsIndex_Type(IntegerIndex):
    """Custom type macFilterViolationsIndex based on IntegerIndex"""
    subtypeSpec = IntegerIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MacFilterViolationsIndex_Type.__name__ = "IntegerIndex"
_MacFilterViolationsIndex_Object = MibTableColumn
macFilterViolationsIndex = _MacFilterViolationsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 7, 1, 3, 1, 1),
    _MacFilterViolationsIndex_Type()
)
macFilterViolationsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macFilterViolationsIndex.setStatus("current")
_MacFilterViolationsIfIndex_Type = IntegerIndex
_MacFilterViolationsIfIndex_Object = MibTableColumn
macFilterViolationsIfIndex = _MacFilterViolationsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 7, 1, 3, 1, 2),
    _MacFilterViolationsIfIndex_Type()
)
macFilterViolationsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFilterViolationsIfIndex.setStatus("current")
_MacFilterViolationsMAC_Type = MacAddress
_MacFilterViolationsMAC_Object = MibTableColumn
macFilterViolationsMAC = _MacFilterViolationsMAC_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 7, 1, 3, 1, 3),
    _MacFilterViolationsMAC_Type()
)
macFilterViolationsMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFilterViolationsMAC.setStatus("current")
_MacFilterViolationsTimestamp_Type = TimeTicks
_MacFilterViolationsTimestamp_Object = MibTableColumn
macFilterViolationsTimestamp = _MacFilterViolationsTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 4249, 2, 7, 1, 3, 1, 4),
    _MacFilterViolationsTimestamp_Type()
)
macFilterViolationsTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFilterViolationsTimestamp.setStatus("current")
_NateksDev_ObjectIdentity = ObjectIdentity
nateksDev = _NateksDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 2, 8)
)
_NateksMibInfo_ObjectIdentity = ObjectIdentity
nateksMibInfo = _NateksMibInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 3)
)
_NateksMIBGroup_ObjectIdentity = ObjectIdentity
nateksMIBGroup = _NateksMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1)
)
_NateksMIBCompliance_ObjectIdentity = ObjectIdentity
nateksMIBCompliance = _NateksMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4249, 3, 2)
)

# Managed Objects groups

nateksMinimalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 1)
)
nateksMinimalGroup.setObjects(
      *(("NATEKS-MIB", "systemAlarm"),
        ("NATEKS-MIB", "systemReset"))
)
if mibBuilder.loadTexts:
    nateksMinimalGroup.setStatus("current")

nateksCommonInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 2)
)
nateksCommonInfoGroup.setObjects(
      *(("NATEKS-MIB", "model"),
        ("NATEKS-MIB", "softwareVersion"))
)
if mibBuilder.loadTexts:
    nateksCommonInfoGroup.setStatus("current")

nateksCommonExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 3)
)
nateksCommonExtGroup.setObjects(
      *(("NATEKS-MIB", "model"),
        ("NATEKS-MIB", "id"),
        ("NATEKS-MIB", "hardwareVersion"),
        ("NATEKS-MIB", "softwareVersion"),
        ("NATEKS-MIB", "softwareDate"),
        ("NATEKS-MIB", "moduleType"),
        ("NATEKS-MIB", "subrackAddress"),
        ("NATEKS-MIB", "errorCode"),
        ("NATEKS-MIB", "serialNumber"))
)
if mibBuilder.loadTexts:
    nateksCommonExtGroup.setStatus("current")

nateksConfigBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 4)
)
nateksConfigBasicGroup.setObjects(
      *(("NATEKS-MIB", "configDefault"),
        ("NATEKS-MIB", "configNumberValues"),
        ("NATEKS-MIB", "valueName"),
        ("NATEKS-MIB", "valueRunning"))
)
if mibBuilder.loadTexts:
    nateksConfigBasicGroup.setStatus("current")

nateksConfigConfirmedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 5)
)
nateksConfigConfirmedGroup.setObjects(
      *(("NATEKS-MIB", "configDefault"),
        ("NATEKS-MIB", "configNumberValues"),
        ("NATEKS-MIB", "valueName"),
        ("NATEKS-MIB", "valueType"),
        ("NATEKS-MIB", "valueStatus"),
        ("NATEKS-MIB", "valueStartup"),
        ("NATEKS-MIB", "valueRunning"),
        ("NATEKS-MIB", "valueNew"),
        ("NATEKS-MIB", "configApplyAll"),
        ("NATEKS-MIB", "configConfirm"))
)
if mibBuilder.loadTexts:
    nateksConfigConfirmedGroup.setStatus("current")

nateksConfigBackupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 6)
)
nateksConfigBackupGroup.setObjects(
      *(("NATEKS-MIB", "valueBackup"),
        ("NATEKS-MIB", "configBackup"),
        ("NATEKS-MIB", "configRestore"))
)
if mibBuilder.loadTexts:
    nateksConfigBackupGroup.setStatus("current")

nateksConfigGroupsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 7)
)
nateksConfigGroupsGroup.setObjects(
      *(("NATEKS-MIB", "valueGroup"),
        ("NATEKS-MIB", "valueGroupName"),
        ("NATEKS-MIB", "configNumberGroups"),
        ("NATEKS-MIB", "groupName"),
        ("NATEKS-MIB", "groupType"),
        ("NATEKS-MIB", "groupStatus"))
)
if mibBuilder.loadTexts:
    nateksConfigGroupsGroup.setStatus("current")

nateksConfigRWGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 8)
)
nateksConfigRWGroup.setObjects(
    ("NATEKS-MIB", "configRW")
)
if mibBuilder.loadTexts:
    nateksConfigRWGroup.setStatus("current")

nateksG826Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 9)
)
nateksG826Group.setObjects(
      *(("NATEKS-MIB", "g826Number"),
        ("NATEKS-MIB", "g826Reset"),
        ("NATEKS-MIB", "g826IfIndex"),
        ("NATEKS-MIB", "g826Name"),
        ("NATEKS-MIB", "g826EB"),
        ("NATEKS-MIB", "g826ES"),
        ("NATEKS-MIB", "g826SES"),
        ("NATEKS-MIB", "g826BBE"),
        ("NATEKS-MIB", "g826AvailableTime"),
        ("NATEKS-MIB", "g826UnavailableTime"),
        ("NATEKS-MIB", "g826StatReset"))
)
if mibBuilder.loadTexts:
    nateksG826Group.setStatus("deprecated")

nateksIfG826Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 10)
)
nateksIfG826Group.setObjects(
      *(("NATEKS-MIB", "g826Number"),
        ("NATEKS-MIB", "g826Reset"),
        ("NATEKS-MIB", "ifG826Name"),
        ("NATEKS-MIB", "ifG826EB"),
        ("NATEKS-MIB", "ifG826ES"),
        ("NATEKS-MIB", "ifG826SES"),
        ("NATEKS-MIB", "ifG826BBE"),
        ("NATEKS-MIB", "ifG826AvailableTime"),
        ("NATEKS-MIB", "ifG826UnavailableTime"),
        ("NATEKS-MIB", "ifG826StatReset"))
)
if mibBuilder.loadTexts:
    nateksIfG826Group.setStatus("current")

nateksAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 11)
)
nateksAlarmGroup.setObjects(
      *(("NATEKS-MIB", "alarmNumber"),
        ("NATEKS-MIB", "alarmTrapEnable"),
        ("NATEKS-MIB", "alarmId"),
        ("NATEKS-MIB", "alarmIfIndex"),
        ("NATEKS-MIB", "alarmName"),
        ("NATEKS-MIB", "alarmValue"),
        ("NATEKS-MIB", "alarmCutoff"),
        ("NATEKS-MIB", "alarmType"),
        ("NATEKS-MIB", "alarmDisplayType"))
)
if mibBuilder.loadTexts:
    nateksAlarmGroup.setStatus("current")

nateksIfAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 12)
)
nateksIfAlarmGroup.setObjects(
      *(("NATEKS-MIB", "alarmNumber"),
        ("NATEKS-MIB", "alarmTrapEnable"),
        ("NATEKS-MIB", "ifAlarmId"),
        ("NATEKS-MIB", "ifAlarmIfIndex"),
        ("NATEKS-MIB", "ifAlarmName"),
        ("NATEKS-MIB", "ifAlarmValue"),
        ("NATEKS-MIB", "ifAlarmCutoff"),
        ("NATEKS-MIB", "ifAlarmType"),
        ("NATEKS-MIB", "ifAlarmDisplayType"))
)
if mibBuilder.loadTexts:
    nateksIfAlarmGroup.setStatus("current")

nateksTlmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 13)
)
nateksTlmGroup.setObjects(
      *(("NATEKS-MIB", "tlmNumber"),
        ("NATEKS-MIB", "tlmClear"),
        ("NATEKS-MIB", "tlmName"),
        ("NATEKS-MIB", "tlmStatus"),
        ("NATEKS-MIB", "tlmLastStatusChange"),
        ("NATEKS-MIB", "tlmSetup"),
        ("NATEKS-MIB", "tlmTrapEnable"))
)
if mibBuilder.loadTexts:
    nateksTlmGroup.setStatus("current")

nateksDSLGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 14)
)
nateksDSLGroup.setObjects(
      *(("NATEKS-MIB", "dslChannelNumber"),
        ("NATEKS-MIB", "dslUnitType"),
        ("NATEKS-MIB", "dslChannelIfIndex"),
        ("NATEKS-MIB", "dslChannelMode"),
        ("NATEKS-MIB", "dslChannelStandard"),
        ("NATEKS-MIB", "dslChannelClockReference"),
        ("NATEKS-MIB", "dslChannelLineCodeConfig"),
        ("NATEKS-MIB", "dslChannelPSDConfig"),
        ("NATEKS-MIB", "dslChannelBaserateConfig"),
        ("NATEKS-MIB", "dslChannelLineCode"),
        ("NATEKS-MIB", "dslChannelPSD"),
        ("NATEKS-MIB", "dslChannelBaserate"),
        ("NATEKS-MIB", "dslChannelLineRate"),
        ("NATEKS-MIB", "dslChannelPayloadRate"),
        ("NATEKS-MIB", "dslChannelStatus"),
        ("NATEKS-MIB", "dslChannelNMR"),
        ("NATEKS-MIB", "dslChannelPowerBackoff"),
        ("NATEKS-MIB", "dslChannelFarEndPowerBackoff"),
        ("NATEKS-MIB", "dslChannelLoopAttenuation"),
        ("NATEKS-MIB", "dslChannelEOCNumber"))
)
if mibBuilder.loadTexts:
    nateksDSLGroup.setStatus("current")

nateksDSLMultipairGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 15)
)
nateksDSLMultipairGroup.setObjects(
      *(("NATEKS-MIB", "dslGroupNumber"),
        ("NATEKS-MIB", "dslGroupType"),
        ("NATEKS-MIB", "dslGroupMainChannel"),
        ("NATEKS-MIB", "dslGroupChannel1"),
        ("NATEKS-MIB", "dslGroupChannel2"),
        ("NATEKS-MIB", "dslGroupChannel3"),
        ("NATEKS-MIB", "dslGroupChannel4"))
)
if mibBuilder.loadTexts:
    nateksDSLMultipairGroup.setStatus("current")

nateksDSLLTUGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 16)
)
nateksDSLLTUGroup.setObjects(
      *(("NATEKS-MIB", "dslChannelRegeneratorNumber"),
        ("NATEKS-MIB", "dslChannelRemotePower"),
        ("NATEKS-MIB", "dslChannelRemotePowerVoltage"))
)
if mibBuilder.loadTexts:
    nateksDSLLTUGroup.setStatus("current")

nateksDSLRegenerationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 17)
)
nateksDSLRegenerationGroup.setObjects(
      *(("NATEKS-MIB", "dslRegenerationChannels"),
        ("NATEKS-MIB", "dslRegenerationSide1"),
        ("NATEKS-MIB", "dslRegenerationSide2"))
)
if mibBuilder.loadTexts:
    nateksDSLRegenerationGroup.setStatus("current")

nateksIndicationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 18)
)
nateksIndicationGroup.setObjects(
      *(("NATEKS-MIB", "indicationLedNumber"),
        ("NATEKS-MIB", "indicationLedDescription"),
        ("NATEKS-MIB", "indicationLedState"),
        ("NATEKS-MIB", "indicationLedFlash"))
)
if mibBuilder.loadTexts:
    nateksIndicationGroup.setStatus("current")

nateksTemperatureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 19)
)
nateksTemperatureGroup.setObjects(
      *(("NATEKS-MIB", "temperatureSensorNumber"),
        ("NATEKS-MIB", "temperatureSensorDescription"),
        ("NATEKS-MIB", "temperatureSensorValue"))
)
if mibBuilder.loadTexts:
    nateksTemperatureGroup.setStatus("current")

nateksTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 20)
)
nateksTimeGroup.setObjects(
      *(("NATEKS-MIB", "timeSourceNumber"),
        ("NATEKS-MIB", "timeSourceName"),
        ("NATEKS-MIB", "timeSourceStratum"),
        ("NATEKS-MIB", "timeSourceValue"),
        ("NATEKS-MIB", "timeZone"))
)
if mibBuilder.loadTexts:
    nateksTimeGroup.setStatus("current")

nateksLocalPowerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 21)
)
nateksLocalPowerGroup.setObjects(
      *(("NATEKS-MIB", "powerSourceNumber"),
        ("NATEKS-MIB", "powerSourceName"),
        ("NATEKS-MIB", "powerSourceNominalVoltage"),
        ("NATEKS-MIB", "powerSourceStatus"))
)
if mibBuilder.loadTexts:
    nateksLocalPowerGroup.setStatus("current")

nateksTFTPManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 22)
)
nateksTFTPManagementGroup.setObjects(
      *(("NATEKS-MIB", "tftpServerIP"),
        ("NATEKS-MIB", "tftpSoftFileName"),
        ("NATEKS-MIB", "tftpConfFileName"),
        ("NATEKS-MIB", "tftpConnectionTimeout"),
        ("NATEKS-MIB", "tftpNumRetries"),
        ("NATEKS-MIB", "tftpTransCmd"),
        ("NATEKS-MIB", "tftpLastOp"),
        ("NATEKS-MIB", "tftpTransferStatus"),
        ("NATEKS-MIB", "tftpLastOpTime"),
        ("NATEKS-MIB", "tftpSoftConfirm"),
        ("NATEKS-MIB", "tftpProtocolVersion"),
        ("NATEKS-MIB", "tftpServerUserName"),
        ("NATEKS-MIB", "tftpServerUserPass"),
        ("NATEKS-MIB", "tftpServerPortNumber"))
)
if mibBuilder.loadTexts:
    nateksTFTPManagementGroup.setStatus("current")

nateksMacFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 23)
)
nateksMacFilterGroup.setObjects(
      *(("NATEKS-MIB", "macFilterConfigStatus"),
        ("NATEKS-MIB", "macFilterConfigAction"),
        ("NATEKS-MIB", "macFilterWhitelistMAC"),
        ("NATEKS-MIB", "macFilterViolationsIfIndex"),
        ("NATEKS-MIB", "macFilterViolationsMAC"),
        ("NATEKS-MIB", "macFilterViolationsTimestamp"))
)
if mibBuilder.loadTexts:
    nateksMacFilterGroup.setStatus("current")

nateksSfpDDMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 24)
)
nateksSfpDDMGroup.setObjects(
      *(("NATEKS-MIB", "sfpDDMNumber"),
        ("NATEKS-MIB", "sfpDDMTemperature"),
        ("NATEKS-MIB", "sfpDDMSupplyVoltage"),
        ("NATEKS-MIB", "sfpDDMTxBiasCurrent"),
        ("NATEKS-MIB", "sfpDDMTxOutputmW"),
        ("NATEKS-MIB", "sfpDDMTxOutputdBm"),
        ("NATEKS-MIB", "sfpDDMRxInputmW"),
        ("NATEKS-MIB", "sfpDDMRxInputdBm"),
        ("NATEKS-MIB", "sfpDDMMediaType"),
        ("NATEKS-MIB", "sfpDDMPresence"),
        ("NATEKS-MIB", "sfpDDMIfIndex"))
)
if mibBuilder.loadTexts:
    nateksSfpDDMGroup.setStatus("current")

nateksDigitalIoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 25)
)
nateksDigitalIoGroup.setObjects(
      *(("NATEKS-MIB", "ioDInNumber"),
        ("NATEKS-MIB", "dInName"),
        ("NATEKS-MIB", "dInState"),
        ("NATEKS-MIB", "dInNormalState"),
        ("NATEKS-MIB", "dInAlarmSeverity"),
        ("NATEKS-MIB", "dInDescription"),
        ("NATEKS-MIB", "dInTrapEnable"),
        ("NATEKS-MIB", "ioDOutNumber"),
        ("NATEKS-MIB", "dOutName"),
        ("NATEKS-MIB", "dOutState"),
        ("NATEKS-MIB", "dOutNormalState"),
        ("NATEKS-MIB", "dOutAlarmSeverity"),
        ("NATEKS-MIB", "dOutDescription"),
        ("NATEKS-MIB", "dOutTrapEnable"))
)
if mibBuilder.loadTexts:
    nateksDigitalIoGroup.setStatus("current")

nateksStatResetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 26)
)
nateksStatResetGroup.setObjects(
    ("NATEKS-MIB", "statReset")
)
if mibBuilder.loadTexts:
    nateksStatResetGroup.setStatus("current")


# Notification objects

tlmStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4249, 0, 1)
)
tlmStatusChange.setObjects(
      *(("NATEKS-MIB", "tlmStatus"),
        ("NATEKS-MIB", "tlmLastStatusChange"))
)
if mibBuilder.loadTexts:
    tlmStatusChange.setStatus(
        "current"
    )

alarmValueChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4249, 0, 2)
)
alarmValueChange.setObjects(
      *(("NATEKS-MIB", "alarmId"),
        ("NATEKS-MIB", "alarmIfIndex"),
        ("NATEKS-MIB", "alarmName"),
        ("NATEKS-MIB", "alarmValue"),
        ("NATEKS-MIB", "alarmDisplayType"),
        ("NATEKS-MIB", "alarmCutoff"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    alarmValueChange.setStatus(
        "current"
    )

tftpStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4249, 0, 3)
)
tftpStatusChange.setObjects(
      *(("NATEKS-MIB", "tftpLastOp"),
        ("NATEKS-MIB", "tftpTransferStatus"),
        ("NATEKS-MIB", "tftpLastOpTime"))
)
if mibBuilder.loadTexts:
    tftpStatusChange.setStatus(
        "current"
    )

macFilterViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 4249, 0, 4)
)
macFilterViolation.setObjects(
      *(("NATEKS-MIB", "macFilterViolationsIfIndex"),
        ("IF-MIB", "ifDescr"),
        ("NATEKS-MIB", "macFilterViolationsMAC"),
        ("NATEKS-MIB", "macFilterConfigAction"))
)
if mibBuilder.loadTexts:
    macFilterViolation.setStatus(
        "current"
    )

dInStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4249, 0, 5)
)
dInStateChange.setObjects(
      *(("NATEKS-MIB", "dInName"),
        ("NATEKS-MIB", "dInState"),
        ("NATEKS-MIB", "dInNormalState"),
        ("NATEKS-MIB", "dInDescription"))
)
if mibBuilder.loadTexts:
    dInStateChange.setStatus(
        "current"
    )

dOutStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4249, 0, 6)
)
dOutStateChange.setObjects(
      *(("NATEKS-MIB", "dOutName"),
        ("NATEKS-MIB", "dOutState"),
        ("NATEKS-MIB", "dOutNormalState"),
        ("NATEKS-MIB", "dOutDescription"))
)
if mibBuilder.loadTexts:
    dOutStateChange.setStatus(
        "current"
    )


# Notifications groups

nateksTlmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 1001)
)
nateksTlmNotificationGroup.setObjects(
    ("NATEKS-MIB", "tlmStatusChange")
)
if mibBuilder.loadTexts:
    nateksTlmNotificationGroup.setStatus(
        "current"
    )

nateksAlarmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 1002)
)
nateksAlarmNotificationGroup.setObjects(
    ("NATEKS-MIB", "alarmValueChange")
)
if mibBuilder.loadTexts:
    nateksAlarmNotificationGroup.setStatus(
        "current"
    )

nateksTFTPNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 1003)
)
nateksTFTPNotificationGroup.setObjects(
    ("NATEKS-MIB", "tftpStatusChange")
)
if mibBuilder.loadTexts:
    nateksTFTPNotificationGroup.setStatus(
        "current"
    )

nateksMacFilterNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 1004)
)
nateksMacFilterNotificationGroup.setObjects(
    ("NATEKS-MIB", "macFilterViolation")
)
if mibBuilder.loadTexts:
    nateksMacFilterNotificationGroup.setStatus(
        "current"
    )

nateksDigitalIoNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4249, 3, 1, 1005)
)
nateksDigitalIoNotificationGroup.setObjects(
      *(("NATEKS-MIB", "dInStateChange"),
        ("NATEKS-MIB", "dOutStateChange"))
)
if mibBuilder.loadTexts:
    nateksDigitalIoNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

nateksMinCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4249, 3, 2, 1)
)
nateksMinCompliance.setObjects(
      *(("NATEKS-MIB", "nateksMinimalGroup"),
        ("NATEKS-MIB", "nateksCommonInfoGroup"))
)
if mibBuilder.loadTexts:
    nateksMinCompliance.setStatus(
        "current"
    )

nateksBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4249, 3, 2, 2)
)
nateksBasicCompliance.setObjects(
      *(("NATEKS-MIB", "nateksMinimalGroup"),
        ("NATEKS-MIB", "nateksCommonExtGroup"))
)
if mibBuilder.loadTexts:
    nateksBasicCompliance.setStatus(
        "current"
    )

nateksConfigBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4249, 3, 2, 3)
)
nateksConfigBasicCompliance.setObjects(
    ("NATEKS-MIB", "nateksConfigBasicGroup")
)
if mibBuilder.loadTexts:
    nateksConfigBasicCompliance.setStatus(
        "current"
    )

nateksConfigConfirmedCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4249, 3, 2, 4)
)
nateksConfigConfirmedCompliance.setObjects(
    ("NATEKS-MIB", "nateksConfigConfirmedGroup")
)
if mibBuilder.loadTexts:
    nateksConfigConfirmedCompliance.setStatus(
        "current"
    )

nateksConfigBackupCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4249, 3, 2, 5)
)
nateksConfigBackupCompliance.setObjects(
    ("NATEKS-MIB", "nateksConfigBackupGroup")
)
if mibBuilder.loadTexts:
    nateksConfigBackupCompliance.setStatus(
        "current"
    )

nateksConfigFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4249, 3, 2, 6)
)
nateksConfigFullCompliance.setObjects(
      *(("NATEKS-MIB", "nateksConfigConfirmedGroup"),
        ("NATEKS-MIB", "nateksConfigBackupGroup"),
        ("NATEKS-MIB", "nateksConfigGroupsGroup"),
        ("NATEKS-MIB", "nateksConfigRWGroup"))
)
if mibBuilder.loadTexts:
    nateksConfigFullCompliance.setStatus(
        "current"
    )

nateksG826Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4249, 3, 2, 7)
)
nateksG826Compliance.setObjects(
    ("NATEKS-MIB", "nateksIfG826Group")
)
if mibBuilder.loadTexts:
    nateksG826Compliance.setStatus(
        "current"
    )

nateksIfAlarmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4249, 3, 2, 8)
)
nateksIfAlarmCompliance.setObjects(
      *(("NATEKS-MIB", "nateksIfAlarmGroup"),
        ("NATEKS-MIB", "nateksAlarmNotificationGroup"),
        ("NATEKS-MIB", "nateksAlarmGroup"))
)
if mibBuilder.loadTexts:
    nateksIfAlarmCompliance.setStatus(
        "current"
    )

nateksTLMCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4249, 3, 2, 9)
)
nateksTLMCompliance.setObjects(
      *(("NATEKS-MIB", "nateksTlmGroup"),
        ("NATEKS-MIB", "nateksTlmNotificationGroup"))
)
if mibBuilder.loadTexts:
    nateksTLMCompliance.setStatus(
        "current"
    )

nateksDSLLTUCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4249, 3, 2, 10)
)
nateksDSLLTUCompliance.setObjects(
      *(("NATEKS-MIB", "nateksDSLGroup"),
        ("NATEKS-MIB", "nateksDSLMultipairGroup"),
        ("NATEKS-MIB", "nateksDSLLTUGroup"))
)
if mibBuilder.loadTexts:
    nateksDSLLTUCompliance.setStatus(
        "current"
    )

nateksDSLRegeneratorCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4249, 3, 2, 11)
)
nateksDSLRegeneratorCompliance.setObjects(
      *(("NATEKS-MIB", "nateksDSLGroup"),
        ("NATEKS-MIB", "nateksDSLMultipairGroup"),
        ("NATEKS-MIB", "nateksDSLRegenerationGroup"))
)
if mibBuilder.loadTexts:
    nateksDSLRegeneratorCompliance.setStatus(
        "current"
    )

nateksIndicationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4249, 3, 2, 12)
)
nateksIndicationCompliance.setObjects(
    ("NATEKS-MIB", "nateksIndicationGroup")
)
if mibBuilder.loadTexts:
    nateksIndicationCompliance.setStatus(
        "current"
    )

nateksTemperatureCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4249, 3, 2, 13)
)
nateksTemperatureCompliance.setObjects(
    ("NATEKS-MIB", "nateksTemperatureGroup")
)
if mibBuilder.loadTexts:
    nateksTemperatureCompliance.setStatus(
        "current"
    )

nateksTimeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4249, 3, 2, 14)
)
nateksTimeCompliance.setObjects(
    ("NATEKS-MIB", "nateksTimeGroup")
)
if mibBuilder.loadTexts:
    nateksTimeCompliance.setStatus(
        "current"
    )

nateksLocalPowerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4249, 3, 2, 15)
)
nateksLocalPowerCompliance.setObjects(
    ("NATEKS-MIB", "nateksLocalPowerGroup")
)
if mibBuilder.loadTexts:
    nateksLocalPowerCompliance.setStatus(
        "current"
    )

nateksTFTPManagementCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4249, 3, 2, 16)
)
nateksTFTPManagementCompliance.setObjects(
      *(("NATEKS-MIB", "nateksTFTPManagementGroup"),
        ("NATEKS-MIB", "nateksTFTPNotificationGroup"))
)
if mibBuilder.loadTexts:
    nateksTFTPManagementCompliance.setStatus(
        "current"
    )

nateksMacFilterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4249, 3, 2, 17)
)
nateksMacFilterCompliance.setObjects(
      *(("NATEKS-MIB", "nateksMacFilterGroup"),
        ("NATEKS-MIB", "nateksMacFilterNotificationGroup"))
)
if mibBuilder.loadTexts:
    nateksMacFilterCompliance.setStatus(
        "current"
    )

nateksSfpDDMGroupCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4249, 3, 2, 18)
)
nateksSfpDDMGroupCompliance.setObjects(
    ("NATEKS-MIB", "nateksSfpDDMGroup")
)
if mibBuilder.loadTexts:
    nateksSfpDDMGroupCompliance.setStatus(
        "current"
    )

nateksDigitalIoCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4249, 3, 2, 19)
)
nateksDigitalIoCompliance.setObjects(
      *(("NATEKS-MIB", "nateksDigitalIoGroup"),
        ("NATEKS-MIB", "nateksDigitalIoNotificationGroup"))
)
if mibBuilder.loadTexts:
    nateksDigitalIoCompliance.setStatus(
        "current"
    )

nateksStatResetCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4249, 3, 2, 20)
)
nateksStatResetCompliance.setObjects(
    ("NATEKS-MIB", "nateksStatResetGroup")
)
if mibBuilder.loadTexts:
    nateksStatResetCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NATEKS-MIB",
    **{"IntegerNumber": IntegerNumber,
       "IntegerIndex": IntegerIndex,
       "IntegerWithDecimal": IntegerWithDecimal,
       "IntegerMillis": IntegerMillis,
       "SfpPowerMilliWatt": SfpPowerMilliWatt,
       "nateks": nateks,
       "nateksTraps": nateksTraps,
       "tlmStatusChange": tlmStatusChange,
       "alarmValueChange": alarmValueChange,
       "tftpStatusChange": tftpStatusChange,
       "macFilterViolation": macFilterViolation,
       "dInStateChange": dInStateChange,
       "dOutStateChange": dOutStateChange,
       "nateksProducts": nateksProducts,
       "megatrans3CLTU": megatrans3CLTU,
       "orion2LTU": orion2LTU,
       "megatrans3CRGN": megatrans3CRGN,
       "megatrans4LTU": megatrans4LTU,
       "megatrans4RGN": megatrans4RGN,
       "orion3LTU": orion3LTU,
       "orion3NTU": orion3NTU,
       "orion3repeater": orion3repeater,
       "miniFlex": miniFlex,
       "nateksMgmt": nateksMgmt,
       "systemAlarm": systemAlarm,
       "systemReset": systemReset,
       "common": common,
       "model": model,
       "id": id,
       "hardwareVersion": hardwareVersion,
       "softwareVersion": softwareVersion,
       "softwareDate": softwareDate,
       "moduleType": moduleType,
       "subrackAddress": subrackAddress,
       "errorCode": errorCode,
       "serialNumber": serialNumber,
       "config": config,
       "configRW": configRW,
       "configDefault": configDefault,
       "configSystem": configSystem,
       "configNumberValues": configNumberValues,
       "configValueTable": configValueTable,
       "configValueEntry": configValueEntry,
       "valueId": valueId,
       "valueGroup": valueGroup,
       "valueName": valueName,
       "valueGroupName": valueGroupName,
       "valueType": valueType,
       "valueStatus": valueStatus,
       "valueStartup": valueStartup,
       "valueRunning": valueRunning,
       "valueNew": valueNew,
       "valueBackup": valueBackup,
       "configNumberGroups": configNumberGroups,
       "configGroupTable": configGroupTable,
       "configGroupEntry": configGroupEntry,
       "groupId": groupId,
       "groupName": groupName,
       "groupType": groupType,
       "groupStatus": groupStatus,
       "configApplyAll": configApplyAll,
       "configConfirm": configConfirm,
       "configBackup": configBackup,
       "configRestore": configRestore,
       "stats": stats,
       "g826": g826,
       "g826Number": g826Number,
       "g826Table": g826Table,
       "g826Entry": g826Entry,
       "g826Id": g826Id,
       "g826IfIndex": g826IfIndex,
       "g826Name": g826Name,
       "g826EB": g826EB,
       "g826ES": g826ES,
       "g826SES": g826SES,
       "g826BBE": g826BBE,
       "g826AvailableTime": g826AvailableTime,
       "g826UnavailableTime": g826UnavailableTime,
       "g826StatReset": g826StatReset,
       "g826Reset": g826Reset,
       "ifG826Table": ifG826Table,
       "ifG826Entry": ifG826Entry,
       "ifG826Id": ifG826Id,
       "ifG826IfIndex": ifG826IfIndex,
       "ifG826Name": ifG826Name,
       "ifG826EB": ifG826EB,
       "ifG826ES": ifG826ES,
       "ifG826SES": ifG826SES,
       "ifG826BBE": ifG826BBE,
       "ifG826AvailableTime": ifG826AvailableTime,
       "ifG826UnavailableTime": ifG826UnavailableTime,
       "ifG826StatReset": ifG826StatReset,
       "alarms": alarms,
       "alarmNumber": alarmNumber,
       "alarmTable": alarmTable,
       "alarmEntry": alarmEntry,
       "alarmId": alarmId,
       "alarmIfIndex": alarmIfIndex,
       "alarmName": alarmName,
       "alarmValue": alarmValue,
       "alarmCutoff": alarmCutoff,
       "alarmType": alarmType,
       "alarmDisplayType": alarmDisplayType,
       "alarmTrapEnable": alarmTrapEnable,
       "ifAlarmTable": ifAlarmTable,
       "ifAlarmEntry": ifAlarmEntry,
       "ifAlarmId": ifAlarmId,
       "ifAlarmIfIndex": ifAlarmIfIndex,
       "ifAlarmName": ifAlarmName,
       "ifAlarmValue": ifAlarmValue,
       "ifAlarmCutoff": ifAlarmCutoff,
       "ifAlarmType": ifAlarmType,
       "ifAlarmDisplayType": ifAlarmDisplayType,
       "tlm": tlm,
       "tlmNumber": tlmNumber,
       "tlmTable": tlmTable,
       "tlmEntry": tlmEntry,
       "tlmId": tlmId,
       "tlmName": tlmName,
       "tlmStatus": tlmStatus,
       "tlmLastStatusChange": tlmLastStatusChange,
       "tlmSetup": tlmSetup,
       "tlmTrapEnable": tlmTrapEnable,
       "tlmClear": tlmClear,
       "dsl": dsl,
       "dslChannelNumber": dslChannelNumber,
       "dslUnitType": dslUnitType,
       "dslChannelTable": dslChannelTable,
       "dslChannelEntry": dslChannelEntry,
       "dslChannelId": dslChannelId,
       "dslChannelIfIndex": dslChannelIfIndex,
       "dslChannelMode": dslChannelMode,
       "dslChannelStandard": dslChannelStandard,
       "dslChannelClockReference": dslChannelClockReference,
       "dslChannelLineCodeConfig": dslChannelLineCodeConfig,
       "dslChannelPSDConfig": dslChannelPSDConfig,
       "dslChannelBaserateConfig": dslChannelBaserateConfig,
       "dslChannelStatus": dslChannelStatus,
       "dslChannelLineCode": dslChannelLineCode,
       "dslChannelPSD": dslChannelPSD,
       "dslChannelBaserate": dslChannelBaserate,
       "dslChannelLineRate": dslChannelLineRate,
       "dslChannelPayloadRate": dslChannelPayloadRate,
       "dslChannelNMR": dslChannelNMR,
       "dslChannelPowerBackoff": dslChannelPowerBackoff,
       "dslChannelFarEndPowerBackoff": dslChannelFarEndPowerBackoff,
       "dslChannelLoopAttenuation": dslChannelLoopAttenuation,
       "dslChannelEOCNumber": dslChannelEOCNumber,
       "dslChannelRegeneratorNumber": dslChannelRegeneratorNumber,
       "dslChannelRemotePower": dslChannelRemotePower,
       "dslChannelRemotePowerVoltage": dslChannelRemotePowerVoltage,
       "dslGroupNumber": dslGroupNumber,
       "dslGroupTable": dslGroupTable,
       "dslGroupEntry": dslGroupEntry,
       "dslGroupId": dslGroupId,
       "dslGroupType": dslGroupType,
       "dslGroupMainChannel": dslGroupMainChannel,
       "dslGroupChannel1": dslGroupChannel1,
       "dslGroupChannel2": dslGroupChannel2,
       "dslGroupChannel3": dslGroupChannel3,
       "dslGroupChannel4": dslGroupChannel4,
       "dslRegenerationChannels": dslRegenerationChannels,
       "dslRegenerationTable": dslRegenerationTable,
       "dslRegenerationEntry": dslRegenerationEntry,
       "dslRegenerationId": dslRegenerationId,
       "dslRegenerationSide1": dslRegenerationSide1,
       "dslRegenerationSide2": dslRegenerationSide2,
       "indication": indication,
       "indicationLedNumber": indicationLedNumber,
       "indicationLedTable": indicationLedTable,
       "indicationLedEntry": indicationLedEntry,
       "indicationLedId": indicationLedId,
       "indicationLedDescription": indicationLedDescription,
       "indicationLedState": indicationLedState,
       "indicationLedFlash": indicationLedFlash,
       "temperature": temperature,
       "temperatureSensorNumber": temperatureSensorNumber,
       "temperatureSensorTable": temperatureSensorTable,
       "temperatureSensorEntry": temperatureSensorEntry,
       "temperatureSensorId": temperatureSensorId,
       "temperatureSensorDescription": temperatureSensorDescription,
       "temperatureSensorValue": temperatureSensorValue,
       "time": time,
       "timeSourceNumber": timeSourceNumber,
       "timeSourceTable": timeSourceTable,
       "timeSourceEntry": timeSourceEntry,
       "timeSourceId": timeSourceId,
       "timeSourceName": timeSourceName,
       "timeSourceStratum": timeSourceStratum,
       "timeSourceValue": timeSourceValue,
       "timeZone": timeZone,
       "localPower": localPower,
       "powerSourceNumber": powerSourceNumber,
       "powerSourceTable": powerSourceTable,
       "powerSourceEntry": powerSourceEntry,
       "powerSourceId": powerSourceId,
       "powerSourceName": powerSourceName,
       "powerSourceNominalVoltage": powerSourceNominalVoltage,
       "powerSourceStatus": powerSourceStatus,
       "sfpDDM": sfpDDM,
       "sfpDDMNumber": sfpDDMNumber,
       "sfpDDMTable": sfpDDMTable,
       "sfpDDMEntry": sfpDDMEntry,
       "sfpDDMId": sfpDDMId,
       "sfpDDMTemperature": sfpDDMTemperature,
       "sfpDDMSupplyVoltage": sfpDDMSupplyVoltage,
       "sfpDDMTxBiasCurrent": sfpDDMTxBiasCurrent,
       "sfpDDMTxOutputmW": sfpDDMTxOutputmW,
       "sfpDDMTxOutputdBm": sfpDDMTxOutputdBm,
       "sfpDDMRxInputmW": sfpDDMRxInputmW,
       "sfpDDMRxInputdBm": sfpDDMRxInputdBm,
       "sfpDDMMediaType": sfpDDMMediaType,
       "sfpDDMPresence": sfpDDMPresence,
       "sfpDDMIfIndex": sfpDDMIfIndex,
       "io": io,
       "ioDIn": ioDIn,
       "ioDInNumber": ioDInNumber,
       "ioDInTable": ioDInTable,
       "ioDInEntry": ioDInEntry,
       "dInId": dInId,
       "dInName": dInName,
       "dInState": dInState,
       "dInNormalState": dInNormalState,
       "dInAlarmSeverity": dInAlarmSeverity,
       "dInDescription": dInDescription,
       "dInTrapEnable": dInTrapEnable,
       "ioDOut": ioDOut,
       "ioDOutNumber": ioDOutNumber,
       "ioDOutTable": ioDOutTable,
       "ioDOutEntry": ioDOutEntry,
       "dOutId": dOutId,
       "dOutName": dOutName,
       "dOutState": dOutState,
       "dOutNormalState": dOutNormalState,
       "dOutAlarmSeverity": dOutAlarmSeverity,
       "dOutDescription": dOutDescription,
       "dOutTrapEnable": dOutTrapEnable,
       "statReset": statReset,
       "maintenance": maintenance,
       "tftp": tftp,
       "tftpServerIP": tftpServerIP,
       "tftpSoftFileName": tftpSoftFileName,
       "tftpConfFileName": tftpConfFileName,
       "tftpConnectionTimeout": tftpConnectionTimeout,
       "tftpNumRetries": tftpNumRetries,
       "tftpTransCmd": tftpTransCmd,
       "tftpLastOp": tftpLastOp,
       "tftpTransferStatus": tftpTransferStatus,
       "tftpLastOpTime": tftpLastOpTime,
       "tftpSoftConfirm": tftpSoftConfirm,
       "tftpProtocolVersion": tftpProtocolVersion,
       "tftpServerUserName": tftpServerUserName,
       "tftpServerUserPass": tftpServerUserPass,
       "tftpServerPortNumber": tftpServerPortNumber,
       "nateksSecurity": nateksSecurity,
       "macFilter": macFilter,
       "macFilterConfigTable": macFilterConfigTable,
       "macFilterConfigEntry": macFilterConfigEntry,
       "macFilterConfigIfIndex": macFilterConfigIfIndex,
       "macFilterConfigStatus": macFilterConfigStatus,
       "macFilterConfigAction": macFilterConfigAction,
       "macFilterWhitelistTable": macFilterWhitelistTable,
       "macFilterWhitelistEntry": macFilterWhitelistEntry,
       "macFilterWhitelistIndex": macFilterWhitelistIndex,
       "macFilterWhitelistIfIndex": macFilterWhitelistIfIndex,
       "macFilterWhitelistMAC": macFilterWhitelistMAC,
       "macFilterViolationsTable": macFilterViolationsTable,
       "macFilterViolationsEntry": macFilterViolationsEntry,
       "macFilterViolationsIndex": macFilterViolationsIndex,
       "macFilterViolationsIfIndex": macFilterViolationsIfIndex,
       "macFilterViolationsMAC": macFilterViolationsMAC,
       "macFilterViolationsTimestamp": macFilterViolationsTimestamp,
       "nateksDev": nateksDev,
       "nateksMibInfo": nateksMibInfo,
       "nateksMIBGroup": nateksMIBGroup,
       "nateksMinimalGroup": nateksMinimalGroup,
       "nateksCommonInfoGroup": nateksCommonInfoGroup,
       "nateksCommonExtGroup": nateksCommonExtGroup,
       "nateksConfigBasicGroup": nateksConfigBasicGroup,
       "nateksConfigConfirmedGroup": nateksConfigConfirmedGroup,
       "nateksConfigBackupGroup": nateksConfigBackupGroup,
       "nateksConfigGroupsGroup": nateksConfigGroupsGroup,
       "nateksConfigRWGroup": nateksConfigRWGroup,
       "nateksG826Group": nateksG826Group,
       "nateksIfG826Group": nateksIfG826Group,
       "nateksAlarmGroup": nateksAlarmGroup,
       "nateksIfAlarmGroup": nateksIfAlarmGroup,
       "nateksTlmGroup": nateksTlmGroup,
       "nateksDSLGroup": nateksDSLGroup,
       "nateksDSLMultipairGroup": nateksDSLMultipairGroup,
       "nateksDSLLTUGroup": nateksDSLLTUGroup,
       "nateksDSLRegenerationGroup": nateksDSLRegenerationGroup,
       "nateksIndicationGroup": nateksIndicationGroup,
       "nateksTemperatureGroup": nateksTemperatureGroup,
       "nateksTimeGroup": nateksTimeGroup,
       "nateksLocalPowerGroup": nateksLocalPowerGroup,
       "nateksTFTPManagementGroup": nateksTFTPManagementGroup,
       "nateksMacFilterGroup": nateksMacFilterGroup,
       "nateksSfpDDMGroup": nateksSfpDDMGroup,
       "nateksDigitalIoGroup": nateksDigitalIoGroup,
       "nateksStatResetGroup": nateksStatResetGroup,
       "nateksTlmNotificationGroup": nateksTlmNotificationGroup,
       "nateksAlarmNotificationGroup": nateksAlarmNotificationGroup,
       "nateksTFTPNotificationGroup": nateksTFTPNotificationGroup,
       "nateksMacFilterNotificationGroup": nateksMacFilterNotificationGroup,
       "nateksDigitalIoNotificationGroup": nateksDigitalIoNotificationGroup,
       "nateksMIBCompliance": nateksMIBCompliance,
       "nateksMinCompliance": nateksMinCompliance,
       "nateksBasicCompliance": nateksBasicCompliance,
       "nateksConfigBasicCompliance": nateksConfigBasicCompliance,
       "nateksConfigConfirmedCompliance": nateksConfigConfirmedCompliance,
       "nateksConfigBackupCompliance": nateksConfigBackupCompliance,
       "nateksConfigFullCompliance": nateksConfigFullCompliance,
       "nateksG826Compliance": nateksG826Compliance,
       "nateksIfAlarmCompliance": nateksIfAlarmCompliance,
       "nateksTLMCompliance": nateksTLMCompliance,
       "nateksDSLLTUCompliance": nateksDSLLTUCompliance,
       "nateksDSLRegeneratorCompliance": nateksDSLRegeneratorCompliance,
       "nateksIndicationCompliance": nateksIndicationCompliance,
       "nateksTemperatureCompliance": nateksTemperatureCompliance,
       "nateksTimeCompliance": nateksTimeCompliance,
       "nateksLocalPowerCompliance": nateksLocalPowerCompliance,
       "nateksTFTPManagementCompliance": nateksTFTPManagementCompliance,
       "nateksMacFilterCompliance": nateksMacFilterCompliance,
       "nateksSfpDDMGroupCompliance": nateksSfpDDMGroupCompliance,
       "nateksDigitalIoCompliance": nateksDigitalIoCompliance,
       "nateksStatResetCompliance": nateksStatResetCompliance}
)
