# SNMP MIB module (LUM-PORTDEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-PORTDEVICE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:05 2025
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
 lumPortdeviceMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumPortdeviceMIB")

(AdminStatus,
 BoardOrInterfaceOperStatus,
 CommandString,
 EnableDisable,
 FaultStatus,
 MgmtNameString,
 SlotNumber,
 SubrackNumber) = mibBuilder.importSymbols(
    "LUM-TC",
    "AdminStatus",
    "BoardOrInterfaceOperStatus",
    "CommandString",
    "EnableDisable",
    "FaultStatus",
    "MgmtNameString",
    "SlotNumber",
    "SubrackNumber")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

lumPortdeviceMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 57)
)
if mibBuilder.loadTexts:
    lumPortdeviceMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2015-07-07 00:00",
         "2014-05-16 00:00",
         "2013-05-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PortDeviceEquipmentType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("nidGe", 1),
          ("iSfp155", 2),
          ("iSfp622", 3),
          ("iSfpVc12", 4),
          ("iSfp2488", 5))
    )



class PortDeviceVersionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5,
              8,
              10,
              11,
              12,
              24,
              25,
              31,
              32,
              258,
              259)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("tpmrPmR11S", 1),
          ("ex12NidR22S", 3),
          ("tsop155GeConvPmR12", 4),
          ("tsop622GeConvPmR12", 5),
          ("tpmrPmR15RespS", 8),
          ("tpmrPmR15InitS", 10),
          ("ex14NidR10S", 11),
          ("tpmrPmR11L", 12),
          ("tsop155GeConvPmR15", 24),
          ("tsop622GeConvPmR15", 25),
          ("ex14NidR20S", 31),
          ("ex14NidR40S", 32),
          ("tsopStm1eGeConvPmR15", 258),
          ("tpmrPmR20TranspS", 259))
    )



class PortDevFwImgState(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 0),
          ("inactive", 1),
          ("active", 2),
          ("empty", 3))
    )



class PortSelection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cifa", 0),
          ("cifb", 1),
          ("auto", 2))
    )



# MIB Managed Objects in the order of their OIDs

_LumPortdeviceConfs_ObjectIdentity = ObjectIdentity
lumPortdeviceConfs = _LumPortdeviceConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 1)
)
_LumPortdeviceGroups_ObjectIdentity = ObjectIdentity
lumPortdeviceGroups = _LumPortdeviceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 1, 1)
)
_LumPortdeviceCompl_ObjectIdentity = ObjectIdentity
lumPortdeviceCompl = _LumPortdeviceCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 1, 2)
)
_LumPortdeviceMIBObjects_ObjectIdentity = ObjectIdentity
lumPortdeviceMIBObjects = _LumPortdeviceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2)
)
_PortDevGeneral_ObjectIdentity = ObjectIdentity
portDevGeneral = _PortDevGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 1)
)
_PortDevGeneralLastChangeTime_Type = DateAndTime
_PortDevGeneralLastChangeTime_Object = MibScalar
portDevGeneralLastChangeTime = _PortDevGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 1, 1),
    _PortDevGeneralLastChangeTime_Type()
)
portDevGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevGeneralLastChangeTime.setStatus("current")
_PortDevGeneralStateLastChangeTime_Type = DateAndTime
_PortDevGeneralStateLastChangeTime_Object = MibScalar
portDevGeneralStateLastChangeTime = _PortDevGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 1, 2),
    _PortDevGeneralStateLastChangeTime_Type()
)
portDevGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevGeneralStateLastChangeTime.setStatus("current")
_PortDevGeneralGenericTableSize_Type = Unsigned32
_PortDevGeneralGenericTableSize_Object = MibScalar
portDevGeneralGenericTableSize = _PortDevGeneralGenericTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 1, 3),
    _PortDevGeneralGenericTableSize_Type()
)
portDevGeneralGenericTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevGeneralGenericTableSize.setStatus("current")
_PortDevGeneralEquipmentTableSize_Type = Unsigned32
_PortDevGeneralEquipmentTableSize_Object = MibScalar
portDevGeneralEquipmentTableSize = _PortDevGeneralEquipmentTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 1, 4),
    _PortDevGeneralEquipmentTableSize_Type()
)
portDevGeneralEquipmentTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevGeneralEquipmentTableSize.setStatus("current")
_PortDevGeneralFwTableSize_Type = Unsigned32
_PortDevGeneralFwTableSize_Object = MibScalar
portDevGeneralFwTableSize = _PortDevGeneralFwTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 1, 5),
    _PortDevGeneralFwTableSize_Type()
)
portDevGeneralFwTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevGeneralFwTableSize.setStatus("current")
_PortDevGeneralIwfTableSize_Type = Unsigned32
_PortDevGeneralIwfTableSize_Object = MibScalar
portDevGeneralIwfTableSize = _PortDevGeneralIwfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 1, 6),
    _PortDevGeneralIwfTableSize_Type()
)
portDevGeneralIwfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevGeneralIwfTableSize.setStatus("current")
_PortDevGeneralIwfPmTableSize_Type = Unsigned32
_PortDevGeneralIwfPmTableSize_Object = MibScalar
portDevGeneralIwfPmTableSize = _PortDevGeneralIwfPmTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 1, 7),
    _PortDevGeneralIwfPmTableSize_Type()
)
portDevGeneralIwfPmTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevGeneralIwfPmTableSize.setStatus("current")
_PortDevGenericList_ObjectIdentity = ObjectIdentity
portDevGenericList = _PortDevGenericList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 2)
)
_PortDevGenericTable_Object = MibTable
portDevGenericTable = _PortDevGenericTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 2, 1)
)
if mibBuilder.loadTexts:
    portDevGenericTable.setStatus("current")
_PortDevGenericEntry_Object = MibTableRow
portDevGenericEntry = _PortDevGenericEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 2, 1, 1)
)
portDevGenericEntry.setIndexNames(
    (0, "LUM-PORTDEVICE-MIB", "portDevGenericIndex"),
)
if mibBuilder.loadTexts:
    portDevGenericEntry.setStatus("current")


class _PortDevGenericIndex_Type(Unsigned32):
    """Custom type portDevGenericIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortDevGenericIndex_Type.__name__ = "Unsigned32"
_PortDevGenericIndex_Object = MibTableColumn
portDevGenericIndex = _PortDevGenericIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 2, 1, 1, 1),
    _PortDevGenericIndex_Type()
)
portDevGenericIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevGenericIndex.setStatus("current")
_PortDevGenericName_Type = MgmtNameString
_PortDevGenericName_Object = MibTableColumn
portDevGenericName = _PortDevGenericName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 2, 1, 1, 2),
    _PortDevGenericName_Type()
)
portDevGenericName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevGenericName.setStatus("current")


class _PortDevGenericSubrack_Type(Unsigned32):
    """Custom type portDevGenericSubrack based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortDevGenericSubrack_Type.__name__ = "Unsigned32"
_PortDevGenericSubrack_Object = MibTableColumn
portDevGenericSubrack = _PortDevGenericSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 2, 1, 1, 3),
    _PortDevGenericSubrack_Type()
)
portDevGenericSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevGenericSubrack.setStatus("current")


class _PortDevGenericSlot_Type(Unsigned32):
    """Custom type portDevGenericSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortDevGenericSlot_Type.__name__ = "Unsigned32"
_PortDevGenericSlot_Object = MibTableColumn
portDevGenericSlot = _PortDevGenericSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 2, 1, 1, 4),
    _PortDevGenericSlot_Type()
)
portDevGenericSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevGenericSlot.setStatus("current")


class _PortDevGenericAutoDiscoverInterval_Type(Unsigned32):
    """Custom type portDevGenericAutoDiscoverInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_PortDevGenericAutoDiscoverInterval_Type.__name__ = "Unsigned32"
_PortDevGenericAutoDiscoverInterval_Object = MibTableColumn
portDevGenericAutoDiscoverInterval = _PortDevGenericAutoDiscoverInterval_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 2, 1, 1, 5),
    _PortDevGenericAutoDiscoverInterval_Type()
)
portDevGenericAutoDiscoverInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevGenericAutoDiscoverInterval.setStatus("current")
_PortDevGenericCreateNewPortDevice_Type = CommandString
_PortDevGenericCreateNewPortDevice_Object = MibTableColumn
portDevGenericCreateNewPortDevice = _PortDevGenericCreateNewPortDevice_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 2, 1, 1, 6),
    _PortDevGenericCreateNewPortDevice_Type()
)
portDevGenericCreateNewPortDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevGenericCreateNewPortDevice.setStatus("current")
_PortDevGenericRestartPortDevice_Type = CommandString
_PortDevGenericRestartPortDevice_Object = MibTableColumn
portDevGenericRestartPortDevice = _PortDevGenericRestartPortDevice_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 2, 1, 1, 7),
    _PortDevGenericRestartPortDevice_Type()
)
portDevGenericRestartPortDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevGenericRestartPortDevice.setStatus("current")
_PortDevGenericCreateMep_Type = CommandString
_PortDevGenericCreateMep_Object = MibTableColumn
portDevGenericCreateMep = _PortDevGenericCreateMep_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 2, 1, 1, 8),
    _PortDevGenericCreateMep_Type()
)
portDevGenericCreateMep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevGenericCreateMep.setStatus("current")
_PortDevGenericCreateMeg_Type = CommandString
_PortDevGenericCreateMeg_Object = MibTableColumn
portDevGenericCreateMeg = _PortDevGenericCreateMeg_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 2, 1, 1, 9),
    _PortDevGenericCreateMeg_Type()
)
portDevGenericCreateMeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevGenericCreateMeg.setStatus("current")
_PortDevGenericCreateNewPortDeviceAdvanced_Type = CommandString
_PortDevGenericCreateNewPortDeviceAdvanced_Object = MibTableColumn
portDevGenericCreateNewPortDeviceAdvanced = _PortDevGenericCreateNewPortDeviceAdvanced_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 2, 1, 1, 10),
    _PortDevGenericCreateNewPortDeviceAdvanced_Type()
)
portDevGenericCreateNewPortDeviceAdvanced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevGenericCreateNewPortDeviceAdvanced.setStatus("current")
_PortDevEquipmentList_ObjectIdentity = ObjectIdentity
portDevEquipmentList = _PortDevEquipmentList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3)
)
_PortDevEquipmentTable_Object = MibTable
portDevEquipmentTable = _PortDevEquipmentTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1)
)
if mibBuilder.loadTexts:
    portDevEquipmentTable.setStatus("current")
_PortDevEquipmentEntry_Object = MibTableRow
portDevEquipmentEntry = _PortDevEquipmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1)
)
portDevEquipmentEntry.setIndexNames(
    (0, "LUM-PORTDEVICE-MIB", "portDevEquipmentIndex"),
)
if mibBuilder.loadTexts:
    portDevEquipmentEntry.setStatus("current")


class _PortDevEquipmentIndex_Type(Unsigned32):
    """Custom type portDevEquipmentIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortDevEquipmentIndex_Type.__name__ = "Unsigned32"
_PortDevEquipmentIndex_Object = MibTableColumn
portDevEquipmentIndex = _PortDevEquipmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 1),
    _PortDevEquipmentIndex_Type()
)
portDevEquipmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevEquipmentIndex.setStatus("current")
_PortDevEquipmentName_Type = MgmtNameString
_PortDevEquipmentName_Object = MibTableColumn
portDevEquipmentName = _PortDevEquipmentName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 2),
    _PortDevEquipmentName_Type()
)
portDevEquipmentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevEquipmentName.setStatus("current")


class _PortDevEquipmentDescr_Type(DisplayString):
    """Custom type portDevEquipmentDescr based on DisplayString"""
    defaultValue = OctetString("")


_PortDevEquipmentDescr_Type.__name__ = "DisplayString"
_PortDevEquipmentDescr_Object = MibTableColumn
portDevEquipmentDescr = _PortDevEquipmentDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 3),
    _PortDevEquipmentDescr_Type()
)
portDevEquipmentDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevEquipmentDescr.setStatus("current")


class _PortDevEquipmentLocation_Type(DisplayString):
    """Custom type portDevEquipmentLocation based on DisplayString"""
    defaultValue = OctetString("")


_PortDevEquipmentLocation_Type.__name__ = "DisplayString"
_PortDevEquipmentLocation_Object = MibTableColumn
portDevEquipmentLocation = _PortDevEquipmentLocation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 4),
    _PortDevEquipmentLocation_Type()
)
portDevEquipmentLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevEquipmentLocation.setStatus("current")


class _PortDevEquipmentAdminStatus_Type(AdminStatus):
    """Custom type portDevEquipmentAdminStatus based on AdminStatus"""
    defaultValue = 2


_PortDevEquipmentAdminStatus_Type.__name__ = "AdminStatus"
_PortDevEquipmentAdminStatus_Object = MibTableColumn
portDevEquipmentAdminStatus = _PortDevEquipmentAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 5),
    _PortDevEquipmentAdminStatus_Type()
)
portDevEquipmentAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevEquipmentAdminStatus.setStatus("current")


class _PortDevEquipmentOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type portDevEquipmentOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 3


_PortDevEquipmentOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_PortDevEquipmentOperStatus_Object = MibTableColumn
portDevEquipmentOperStatus = _PortDevEquipmentOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 6),
    _PortDevEquipmentOperStatus_Type()
)
portDevEquipmentOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevEquipmentOperStatus.setStatus("current")


class _PortDevEquipmentExpectedType_Type(PortDeviceEquipmentType):
    """Custom type portDevEquipmentExpectedType based on PortDeviceEquipmentType"""
    defaultValue = 0


_PortDevEquipmentExpectedType_Type.__name__ = "PortDeviceEquipmentType"
_PortDevEquipmentExpectedType_Object = MibTableColumn
portDevEquipmentExpectedType = _PortDevEquipmentExpectedType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 7),
    _PortDevEquipmentExpectedType_Type()
)
portDevEquipmentExpectedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevEquipmentExpectedType.setStatus("current")
_PortDevEquipmentActualType_Type = PortDeviceEquipmentType
_PortDevEquipmentActualType_Object = MibTableColumn
portDevEquipmentActualType = _PortDevEquipmentActualType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 8),
    _PortDevEquipmentActualType_Type()
)
portDevEquipmentActualType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevEquipmentActualType.setStatus("current")
_PortDevEquipmentFwVersion_Type = DisplayString
_PortDevEquipmentFwVersion_Object = MibTableColumn
portDevEquipmentFwVersion = _PortDevEquipmentFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 9),
    _PortDevEquipmentFwVersion_Type()
)
portDevEquipmentFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevEquipmentFwVersion.setStatus("current")
_PortDevEquipmentFwUpgradeStatus_Type = DisplayString
_PortDevEquipmentFwUpgradeStatus_Object = MibTableColumn
portDevEquipmentFwUpgradeStatus = _PortDevEquipmentFwUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 10),
    _PortDevEquipmentFwUpgradeStatus_Type()
)
portDevEquipmentFwUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevEquipmentFwUpgradeStatus.setStatus("current")


class _PortDevEquipmentLinkPassThrough_Type(EnableDisable):
    """Custom type portDevEquipmentLinkPassThrough based on EnableDisable"""
    defaultValue = 1


_PortDevEquipmentLinkPassThrough_Type.__name__ = "EnableDisable"
_PortDevEquipmentLinkPassThrough_Object = MibTableColumn
portDevEquipmentLinkPassThrough = _PortDevEquipmentLinkPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 11),
    _PortDevEquipmentLinkPassThrough_Type()
)
portDevEquipmentLinkPassThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevEquipmentLinkPassThrough.setStatus("current")
_PortDevEquipmentSubrack_Type = SubrackNumber
_PortDevEquipmentSubrack_Object = MibTableColumn
portDevEquipmentSubrack = _PortDevEquipmentSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 12),
    _PortDevEquipmentSubrack_Type()
)
portDevEquipmentSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevEquipmentSubrack.setStatus("current")
_PortDevEquipmentSlot_Type = SlotNumber
_PortDevEquipmentSlot_Object = MibTableColumn
portDevEquipmentSlot = _PortDevEquipmentSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 13),
    _PortDevEquipmentSlot_Type()
)
portDevEquipmentSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevEquipmentSlot.setStatus("current")


class _PortDevEquipmentVlanId_Type(Unsigned32):
    """Custom type portDevEquipmentVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PortDevEquipmentVlanId_Type.__name__ = "Unsigned32"
_PortDevEquipmentVlanId_Object = MibTableColumn
portDevEquipmentVlanId = _PortDevEquipmentVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 14),
    _PortDevEquipmentVlanId_Type()
)
portDevEquipmentVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevEquipmentVlanId.setStatus("current")
_PortDevEquipmentRowStatus_Type = RowStatus
_PortDevEquipmentRowStatus_Object = MibTableColumn
portDevEquipmentRowStatus = _PortDevEquipmentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 15),
    _PortDevEquipmentRowStatus_Type()
)
portDevEquipmentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevEquipmentRowStatus.setStatus("current")
_PortDevEquipmentNoDeviceFound_Type = FaultStatus
_PortDevEquipmentNoDeviceFound_Object = MibTableColumn
portDevEquipmentNoDeviceFound = _PortDevEquipmentNoDeviceFound_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 16),
    _PortDevEquipmentNoDeviceFound_Type()
)
portDevEquipmentNoDeviceFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevEquipmentNoDeviceFound.setStatus("current")
_PortDevEquipmentMultiDeviceFound_Type = FaultStatus
_PortDevEquipmentMultiDeviceFound_Object = MibTableColumn
portDevEquipmentMultiDeviceFound = _PortDevEquipmentMultiDeviceFound_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 17),
    _PortDevEquipmentMultiDeviceFound_Type()
)
portDevEquipmentMultiDeviceFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevEquipmentMultiDeviceFound.setStatus("current")
_PortDevEquipmentDeviceNotManageable_Type = FaultStatus
_PortDevEquipmentDeviceNotManageable_Object = MibTableColumn
portDevEquipmentDeviceNotManageable = _PortDevEquipmentDeviceNotManageable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 18),
    _PortDevEquipmentDeviceNotManageable_Type()
)
portDevEquipmentDeviceNotManageable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevEquipmentDeviceNotManageable.setStatus("current")
_PortDevEquipmentDeviceNotReachable_Type = FaultStatus
_PortDevEquipmentDeviceNotReachable_Object = MibTableColumn
portDevEquipmentDeviceNotReachable = _PortDevEquipmentDeviceNotReachable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 19),
    _PortDevEquipmentDeviceNotReachable_Type()
)
portDevEquipmentDeviceNotReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevEquipmentDeviceNotReachable.setStatus("current")
_PortDevEquipmentConfigurationFault_Type = FaultStatus
_PortDevEquipmentConfigurationFault_Object = MibTableColumn
portDevEquipmentConfigurationFault = _PortDevEquipmentConfigurationFault_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 20),
    _PortDevEquipmentConfigurationFault_Type()
)
portDevEquipmentConfigurationFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevEquipmentConfigurationFault.setStatus("current")
_PortDevEquipmentPowerAMissing_Type = FaultStatus
_PortDevEquipmentPowerAMissing_Object = MibTableColumn
portDevEquipmentPowerAMissing = _PortDevEquipmentPowerAMissing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 21),
    _PortDevEquipmentPowerAMissing_Type()
)
portDevEquipmentPowerAMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevEquipmentPowerAMissing.setStatus("current")
_PortDevEquipmentPowerBMissing_Type = FaultStatus
_PortDevEquipmentPowerBMissing_Object = MibTableColumn
portDevEquipmentPowerBMissing = _PortDevEquipmentPowerBMissing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 22),
    _PortDevEquipmentPowerBMissing_Type()
)
portDevEquipmentPowerBMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevEquipmentPowerBMissing.setStatus("current")


class _PortDevEquipmentInternalReference_Type(Unsigned32):
    """Custom type portDevEquipmentInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PortDevEquipmentInternalReference_Type.__name__ = "Unsigned32"
_PortDevEquipmentInternalReference_Object = MibTableColumn
portDevEquipmentInternalReference = _PortDevEquipmentInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 23),
    _PortDevEquipmentInternalReference_Type()
)
portDevEquipmentInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevEquipmentInternalReference.setStatus("current")
_PortDevEquipmentMacAddress_Type = DisplayString
_PortDevEquipmentMacAddress_Object = MibTableColumn
portDevEquipmentMacAddress = _PortDevEquipmentMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 24),
    _PortDevEquipmentMacAddress_Type()
)
portDevEquipmentMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevEquipmentMacAddress.setStatus("current")


class _PortDevEquipmentLocalPortIndex_Type(Unsigned32):
    """Custom type portDevEquipmentLocalPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortDevEquipmentLocalPortIndex_Type.__name__ = "Unsigned32"
_PortDevEquipmentLocalPortIndex_Object = MibTableColumn
portDevEquipmentLocalPortIndex = _PortDevEquipmentLocalPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 25),
    _PortDevEquipmentLocalPortIndex_Type()
)
portDevEquipmentLocalPortIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevEquipmentLocalPortIndex.setStatus("current")


class _PortDevEquipmentAdminPowerA_Type(AdminStatus):
    """Custom type portDevEquipmentAdminPowerA based on AdminStatus"""
    defaultValue = 1


_PortDevEquipmentAdminPowerA_Type.__name__ = "AdminStatus"
_PortDevEquipmentAdminPowerA_Object = MibTableColumn
portDevEquipmentAdminPowerA = _PortDevEquipmentAdminPowerA_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 26),
    _PortDevEquipmentAdminPowerA_Type()
)
portDevEquipmentAdminPowerA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevEquipmentAdminPowerA.setStatus("current")


class _PortDevEquipmentAdminPowerB_Type(AdminStatus):
    """Custom type portDevEquipmentAdminPowerB based on AdminStatus"""
    defaultValue = 1


_PortDevEquipmentAdminPowerB_Type.__name__ = "AdminStatus"
_PortDevEquipmentAdminPowerB_Object = MibTableColumn
portDevEquipmentAdminPowerB = _PortDevEquipmentAdminPowerB_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 27),
    _PortDevEquipmentAdminPowerB_Type()
)
portDevEquipmentAdminPowerB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevEquipmentAdminPowerB.setStatus("current")


class _PortDevEquipmentSelectedPort_Type(PortSelection):
    """Custom type portDevEquipmentSelectedPort based on PortSelection"""
    defaultValue = 2


_PortDevEquipmentSelectedPort_Type.__name__ = "PortSelection"
_PortDevEquipmentSelectedPort_Object = MibTableColumn
portDevEquipmentSelectedPort = _PortDevEquipmentSelectedPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 28),
    _PortDevEquipmentSelectedPort_Type()
)
portDevEquipmentSelectedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevEquipmentSelectedPort.setStatus("current")
_PortDevEquipmentDestMacAddress_Type = MacAddress
_PortDevEquipmentDestMacAddress_Object = MibTableColumn
portDevEquipmentDestMacAddress = _PortDevEquipmentDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 29),
    _PortDevEquipmentDestMacAddress_Type()
)
portDevEquipmentDestMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevEquipmentDestMacAddress.setStatus("deprecated")


class _PortDevEquipmentDestMacAddressCheck_Type(Integer32):
    """Custom type portDevEquipmentDestMacAddressCheck based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_PortDevEquipmentDestMacAddressCheck_Type.__name__ = "Integer32"
_PortDevEquipmentDestMacAddressCheck_Object = MibTableColumn
portDevEquipmentDestMacAddressCheck = _PortDevEquipmentDestMacAddressCheck_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 30),
    _PortDevEquipmentDestMacAddressCheck_Type()
)
portDevEquipmentDestMacAddressCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevEquipmentDestMacAddressCheck.setStatus("current")
_PortDevEquipmentDeviceVersionType_Type = PortDeviceVersionType
_PortDevEquipmentDeviceVersionType_Object = MibTableColumn
portDevEquipmentDeviceVersionType = _PortDevEquipmentDeviceVersionType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 31),
    _PortDevEquipmentDeviceVersionType_Type()
)
portDevEquipmentDeviceVersionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevEquipmentDeviceVersionType.setStatus("current")


class _PortDevEquipmentActivePort_Type(PortSelection):
    """Custom type portDevEquipmentActivePort based on PortSelection"""
    defaultValue = 2


_PortDevEquipmentActivePort_Type.__name__ = "PortSelection"
_PortDevEquipmentActivePort_Object = MibTableColumn
portDevEquipmentActivePort = _PortDevEquipmentActivePort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 32),
    _PortDevEquipmentActivePort_Type()
)
portDevEquipmentActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevEquipmentActivePort.setStatus("current")
_PortDevEquipmentDyingGasp_Type = FaultStatus
_PortDevEquipmentDyingGasp_Object = MibTableColumn
portDevEquipmentDyingGasp = _PortDevEquipmentDyingGasp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 33),
    _PortDevEquipmentDyingGasp_Type()
)
portDevEquipmentDyingGasp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevEquipmentDyingGasp.setStatus("current")


class _PortDevEquipmentLosCsf_Type(EnableDisable):
    """Custom type portDevEquipmentLosCsf based on EnableDisable"""
    defaultValue = 1


_PortDevEquipmentLosCsf_Type.__name__ = "EnableDisable"
_PortDevEquipmentLosCsf_Object = MibTableColumn
portDevEquipmentLosCsf = _PortDevEquipmentLosCsf_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 3, 1, 1, 34),
    _PortDevEquipmentLosCsf_Type()
)
portDevEquipmentLosCsf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevEquipmentLosCsf.setStatus("current")
_PortDevFwList_ObjectIdentity = ObjectIdentity
portDevFwList = _PortDevFwList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 4)
)
_PortDevFwTable_Object = MibTable
portDevFwTable = _PortDevFwTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 4, 1)
)
if mibBuilder.loadTexts:
    portDevFwTable.setStatus("current")
_PortDevFwEntry_Object = MibTableRow
portDevFwEntry = _PortDevFwEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 4, 1, 1)
)
portDevFwEntry.setIndexNames(
    (0, "LUM-PORTDEVICE-MIB", "portDevFwIndex"),
)
if mibBuilder.loadTexts:
    portDevFwEntry.setStatus("current")


class _PortDevFwIndex_Type(Unsigned32):
    """Custom type portDevFwIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortDevFwIndex_Type.__name__ = "Unsigned32"
_PortDevFwIndex_Object = MibTableColumn
portDevFwIndex = _PortDevFwIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 4, 1, 1, 1),
    _PortDevFwIndex_Type()
)
portDevFwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevFwIndex.setStatus("current")


class _PortDevFwSubrack_Type(Unsigned32):
    """Custom type portDevFwSubrack based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortDevFwSubrack_Type.__name__ = "Unsigned32"
_PortDevFwSubrack_Object = MibTableColumn
portDevFwSubrack = _PortDevFwSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 4, 1, 1, 2),
    _PortDevFwSubrack_Type()
)
portDevFwSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevFwSubrack.setStatus("current")


class _PortDevFwSlot_Type(Unsigned32):
    """Custom type portDevFwSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortDevFwSlot_Type.__name__ = "Unsigned32"
_PortDevFwSlot_Object = MibTableColumn
portDevFwSlot = _PortDevFwSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 4, 1, 1, 3),
    _PortDevFwSlot_Type()
)
portDevFwSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevFwSlot.setStatus("current")
_PortDevFwName_Type = DisplayString
_PortDevFwName_Object = MibTableColumn
portDevFwName = _PortDevFwName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 4, 1, 1, 4),
    _PortDevFwName_Type()
)
portDevFwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevFwName.setStatus("current")


class _PortDevFwPortDevId_Type(Unsigned32):
    """Custom type portDevFwPortDevId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortDevFwPortDevId_Type.__name__ = "Unsigned32"
_PortDevFwPortDevId_Object = MibTableColumn
portDevFwPortDevId = _PortDevFwPortDevId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 4, 1, 1, 5),
    _PortDevFwPortDevId_Type()
)
portDevFwPortDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevFwPortDevId.setStatus("current")


class _PortDevFwImgSlotOneNr_Type(Unsigned32):
    """Custom type portDevFwImgSlotOneNr based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortDevFwImgSlotOneNr_Type.__name__ = "Unsigned32"
_PortDevFwImgSlotOneNr_Object = MibTableColumn
portDevFwImgSlotOneNr = _PortDevFwImgSlotOneNr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 4, 1, 1, 6),
    _PortDevFwImgSlotOneNr_Type()
)
portDevFwImgSlotOneNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevFwImgSlotOneNr.setStatus("current")
_PortDevFwImgSlotOneVersion_Type = DisplayString
_PortDevFwImgSlotOneVersion_Object = MibTableColumn
portDevFwImgSlotOneVersion = _PortDevFwImgSlotOneVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 4, 1, 1, 7),
    _PortDevFwImgSlotOneVersion_Type()
)
portDevFwImgSlotOneVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevFwImgSlotOneVersion.setStatus("current")
_PortDevFwImgSlotOneState_Type = PortDevFwImgState
_PortDevFwImgSlotOneState_Object = MibTableColumn
portDevFwImgSlotOneState = _PortDevFwImgSlotOneState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 4, 1, 1, 8),
    _PortDevFwImgSlotOneState_Type()
)
portDevFwImgSlotOneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevFwImgSlotOneState.setStatus("current")
_PortDevFwImgSlotOneDate_Type = DisplayString
_PortDevFwImgSlotOneDate_Object = MibTableColumn
portDevFwImgSlotOneDate = _PortDevFwImgSlotOneDate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 4, 1, 1, 9),
    _PortDevFwImgSlotOneDate_Type()
)
portDevFwImgSlotOneDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevFwImgSlotOneDate.setStatus("current")


class _PortDevFwImgSlotTwoNr_Type(Unsigned32):
    """Custom type portDevFwImgSlotTwoNr based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortDevFwImgSlotTwoNr_Type.__name__ = "Unsigned32"
_PortDevFwImgSlotTwoNr_Object = MibTableColumn
portDevFwImgSlotTwoNr = _PortDevFwImgSlotTwoNr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 4, 1, 1, 10),
    _PortDevFwImgSlotTwoNr_Type()
)
portDevFwImgSlotTwoNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevFwImgSlotTwoNr.setStatus("current")
_PortDevFwImgSlotTwoVersion_Type = DisplayString
_PortDevFwImgSlotTwoVersion_Object = MibTableColumn
portDevFwImgSlotTwoVersion = _PortDevFwImgSlotTwoVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 4, 1, 1, 11),
    _PortDevFwImgSlotTwoVersion_Type()
)
portDevFwImgSlotTwoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevFwImgSlotTwoVersion.setStatus("current")
_PortDevFwImgSlotTwoState_Type = PortDevFwImgState
_PortDevFwImgSlotTwoState_Object = MibTableColumn
portDevFwImgSlotTwoState = _PortDevFwImgSlotTwoState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 4, 1, 1, 12),
    _PortDevFwImgSlotTwoState_Type()
)
portDevFwImgSlotTwoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevFwImgSlotTwoState.setStatus("current")
_PortDevFwImgSlotTwoDate_Type = DisplayString
_PortDevFwImgSlotTwoDate_Object = MibTableColumn
portDevFwImgSlotTwoDate = _PortDevFwImgSlotTwoDate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 4, 1, 1, 13),
    _PortDevFwImgSlotTwoDate_Type()
)
portDevFwImgSlotTwoDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevFwImgSlotTwoDate.setStatus("current")
_PortDevFwInstallFw_Type = CommandString
_PortDevFwInstallFw_Object = MibTableColumn
portDevFwInstallFw = _PortDevFwInstallFw_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 4, 1, 1, 14),
    _PortDevFwInstallFw_Type()
)
portDevFwInstallFw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevFwInstallFw.setStatus("current")
_PortDevFwActivateFw_Type = CommandString
_PortDevFwActivateFw_Object = MibTableColumn
portDevFwActivateFw = _PortDevFwActivateFw_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 4, 1, 1, 15),
    _PortDevFwActivateFw_Type()
)
portDevFwActivateFw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevFwActivateFw.setStatus("current")
_PortDevFwGetAllFiles_Type = CommandString
_PortDevFwGetAllFiles_Object = MibTableColumn
portDevFwGetAllFiles = _PortDevFwGetAllFiles_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 4, 1, 1, 16),
    _PortDevFwGetAllFiles_Type()
)
portDevFwGetAllFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevFwGetAllFiles.setStatus("current")
_PortDevFwUpgradeStatus_Type = DisplayString
_PortDevFwUpgradeStatus_Object = MibTableColumn
portDevFwUpgradeStatus = _PortDevFwUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 4, 1, 1, 17),
    _PortDevFwUpgradeStatus_Type()
)
portDevFwUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevFwUpgradeStatus.setStatus("current")
_PortDevIwfList_ObjectIdentity = ObjectIdentity
portDevIwfList = _PortDevIwfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5)
)
_PortDevIwfTable_Object = MibTable
portDevIwfTable = _PortDevIwfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1)
)
if mibBuilder.loadTexts:
    portDevIwfTable.setStatus("current")
_PortDevIwfEntry_Object = MibTableRow
portDevIwfEntry = _PortDevIwfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1)
)
portDevIwfEntry.setIndexNames(
    (0, "LUM-PORTDEVICE-MIB", "portDevIwfIndex"),
)
if mibBuilder.loadTexts:
    portDevIwfEntry.setStatus("current")


class _PortDevIwfIndex_Type(Unsigned32):
    """Custom type portDevIwfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortDevIwfIndex_Type.__name__ = "Unsigned32"
_PortDevIwfIndex_Object = MibTableColumn
portDevIwfIndex = _PortDevIwfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 1),
    _PortDevIwfIndex_Type()
)
portDevIwfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfIndex.setStatus("current")
_PortDevIwfName_Type = MgmtNameString
_PortDevIwfName_Object = MibTableColumn
portDevIwfName = _PortDevIwfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 2),
    _PortDevIwfName_Type()
)
portDevIwfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfName.setStatus("current")


class _PortDevIwfRtpClockSource_Type(Integer32):
    """Custom type portDevIwfRtpClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("tdm", 2))
    )


_PortDevIwfRtpClockSource_Type.__name__ = "Integer32"
_PortDevIwfRtpClockSource_Object = MibTableColumn
portDevIwfRtpClockSource = _PortDevIwfRtpClockSource_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 3),
    _PortDevIwfRtpClockSource_Type()
)
portDevIwfRtpClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevIwfRtpClockSource.setStatus("current")


class _PortDevIwfJitterBufferRecenter_Type(Integer32):
    """Custom type portDevIwfJitterBufferRecenter based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("recenter", 2))
    )


_PortDevIwfJitterBufferRecenter_Type.__name__ = "Integer32"
_PortDevIwfJitterBufferRecenter_Object = MibTableColumn
portDevIwfJitterBufferRecenter = _PortDevIwfJitterBufferRecenter_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 4),
    _PortDevIwfJitterBufferRecenter_Type()
)
portDevIwfJitterBufferRecenter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevIwfJitterBufferRecenter.setStatus("current")


class _PortDevIwfInternalReference_Type(Unsigned32):
    """Custom type portDevIwfInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PortDevIwfInternalReference_Type.__name__ = "Unsigned32"
_PortDevIwfInternalReference_Object = MibTableColumn
portDevIwfInternalReference = _PortDevIwfInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 5),
    _PortDevIwfInternalReference_Type()
)
portDevIwfInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevIwfInternalReference.setStatus("current")


class _PortDevIwfLocalPortIndex_Type(Unsigned32):
    """Custom type portDevIwfLocalPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortDevIwfLocalPortIndex_Type.__name__ = "Unsigned32"
_PortDevIwfLocalPortIndex_Object = MibTableColumn
portDevIwfLocalPortIndex = _PortDevIwfLocalPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 6),
    _PortDevIwfLocalPortIndex_Type()
)
portDevIwfLocalPortIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevIwfLocalPortIndex.setStatus("current")
_PortDevIwfLossOfSignal_Type = FaultStatus
_PortDevIwfLossOfSignal_Object = MibTableColumn
portDevIwfLossOfSignal = _PortDevIwfLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 7),
    _PortDevIwfLossOfSignal_Type()
)
portDevIwfLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfLossOfSignal.setStatus("current")
_PortDevIwfLossOfFrame_Type = FaultStatus
_PortDevIwfLossOfFrame_Object = MibTableColumn
portDevIwfLossOfFrame = _PortDevIwfLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 8),
    _PortDevIwfLossOfFrame_Type()
)
portDevIwfLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfLossOfFrame.setStatus("current")
_PortDevIwfEquipmentFailure_Type = FaultStatus
_PortDevIwfEquipmentFailure_Object = MibTableColumn
portDevIwfEquipmentFailure = _PortDevIwfEquipmentFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 9),
    _PortDevIwfEquipmentFailure_Type()
)
portDevIwfEquipmentFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfEquipmentFailure.setStatus("current")
_PortDevIwfNoTdmPayload_Type = FaultStatus
_PortDevIwfNoTdmPayload_Object = MibTableColumn
portDevIwfNoTdmPayload = _PortDevIwfNoTdmPayload_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 10),
    _PortDevIwfNoTdmPayload_Type()
)
portDevIwfNoTdmPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfNoTdmPayload.setStatus("current")
_PortDevIwfRemotePacketLost_Type = FaultStatus
_PortDevIwfRemotePacketLost_Object = MibTableColumn
portDevIwfRemotePacketLost = _PortDevIwfRemotePacketLost_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 11),
    _PortDevIwfRemotePacketLost_Type()
)
portDevIwfRemotePacketLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfRemotePacketLost.setStatus("current")
_PortDevIwfLocalPacketLost_Type = FaultStatus
_PortDevIwfLocalPacketLost_Object = MibTableColumn
portDevIwfLocalPacketLost = _PortDevIwfLocalPacketLost_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 12),
    _PortDevIwfLocalPacketLost_Type()
)
portDevIwfLocalPacketLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfLocalPacketLost.setStatus("current")


class _PortDevIwfAdminStatus_Type(AdminStatus):
    """Custom type portDevIwfAdminStatus based on AdminStatus"""
    defaultValue = 2


_PortDevIwfAdminStatus_Type.__name__ = "AdminStatus"
_PortDevIwfAdminStatus_Object = MibTableColumn
portDevIwfAdminStatus = _PortDevIwfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 13),
    _PortDevIwfAdminStatus_Type()
)
portDevIwfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevIwfAdminStatus.setStatus("current")


class _PortDevIwfOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type portDevIwfOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 3


_PortDevIwfOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_PortDevIwfOperStatus_Object = MibTableColumn
portDevIwfOperStatus = _PortDevIwfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 14),
    _PortDevIwfOperStatus_Type()
)
portDevIwfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfOperStatus.setStatus("current")


class _PortDevIwfDescr_Type(DisplayString):
    """Custom type portDevIwfDescr based on DisplayString"""
    defaultValue = OctetString("")


_PortDevIwfDescr_Type.__name__ = "DisplayString"
_PortDevIwfDescr_Object = MibTableColumn
portDevIwfDescr = _PortDevIwfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 15),
    _PortDevIwfDescr_Type()
)
portDevIwfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevIwfDescr.setStatus("current")


class _PortDevIwfSignalFormat_Type(Integer32):
    """Custom type portDevIwfSignalFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              39)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("stm1", 2),
          ("stm4", 3),
          ("stm16", 4),
          ("e1", 39))
    )


_PortDevIwfSignalFormat_Type.__name__ = "Integer32"
_PortDevIwfSignalFormat_Object = MibTableColumn
portDevIwfSignalFormat = _PortDevIwfSignalFormat_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 16),
    _PortDevIwfSignalFormat_Type()
)
portDevIwfSignalFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfSignalFormat.setStatus("current")


class _PortDevIwfEtherType_Type(Integer32):
    """Custom type portDevIwfEtherType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qTag0x8100", 1),
          ("sTag0x88a8", 2))
    )


_PortDevIwfEtherType_Type.__name__ = "Integer32"
_PortDevIwfEtherType_Object = MibTableColumn
portDevIwfEtherType = _PortDevIwfEtherType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 17),
    _PortDevIwfEtherType_Type()
)
portDevIwfEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevIwfEtherType.setStatus("current")


class _PortDevIwfVlanId_Type(Unsigned32):
    """Custom type portDevIwfVlanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_PortDevIwfVlanId_Type.__name__ = "Unsigned32"
_PortDevIwfVlanId_Object = MibTableColumn
portDevIwfVlanId = _PortDevIwfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 18),
    _PortDevIwfVlanId_Type()
)
portDevIwfVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevIwfVlanId.setStatus("current")


class _PortDevIwfVlanPriority_Type(Unsigned32):
    """Custom type portDevIwfVlanPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PortDevIwfVlanPriority_Type.__name__ = "Unsigned32"
_PortDevIwfVlanPriority_Object = MibTableColumn
portDevIwfVlanPriority = _PortDevIwfVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 19),
    _PortDevIwfVlanPriority_Type()
)
portDevIwfVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevIwfVlanPriority.setStatus("current")


class _PortDevIwfE1ChannelId_Type(Unsigned32):
    """Custom type portDevIwfE1ChannelId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PortDevIwfE1ChannelId_Type.__name__ = "Unsigned32"
_PortDevIwfE1ChannelId_Object = MibTableColumn
portDevIwfE1ChannelId = _PortDevIwfE1ChannelId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 20),
    _PortDevIwfE1ChannelId_Type()
)
portDevIwfE1ChannelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevIwfE1ChannelId.setStatus("current")


class _PortDevIwfE1ChannelKLM_Type(DisplayString):
    """Custom type portDevIwfE1ChannelKLM based on DisplayString"""
    defaultValue = OctetString("")


_PortDevIwfE1ChannelKLM_Type.__name__ = "DisplayString"
_PortDevIwfE1ChannelKLM_Object = MibTableColumn
portDevIwfE1ChannelKLM = _PortDevIwfE1ChannelKLM_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 21),
    _PortDevIwfE1ChannelKLM_Type()
)
portDevIwfE1ChannelKLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfE1ChannelKLM.setStatus("current")
_PortDevIwfDestMacAddress_Type = MacAddress
_PortDevIwfDestMacAddress_Object = MibTableColumn
portDevIwfDestMacAddress = _PortDevIwfDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 22),
    _PortDevIwfDestMacAddress_Type()
)
portDevIwfDestMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevIwfDestMacAddress.setStatus("current")
_PortDevIwfTributaryUnitAlarm_Type = FaultStatus
_PortDevIwfTributaryUnitAlarm_Object = MibTableColumn
portDevIwfTributaryUnitAlarm = _PortDevIwfTributaryUnitAlarm_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 23),
    _PortDevIwfTributaryUnitAlarm_Type()
)
portDevIwfTributaryUnitAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfTributaryUnitAlarm.setStatus("current")
_PortDevIwfMultiplexSectionAlarm_Type = FaultStatus
_PortDevIwfMultiplexSectionAlarm_Object = MibTableColumn
portDevIwfMultiplexSectionAlarm = _PortDevIwfMultiplexSectionAlarm_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 24),
    _PortDevIwfMultiplexSectionAlarm_Type()
)
portDevIwfMultiplexSectionAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfMultiplexSectionAlarm.setStatus("current")
_PortDevIwfMultiplexSectionRDI_Type = FaultStatus
_PortDevIwfMultiplexSectionRDI_Object = MibTableColumn
portDevIwfMultiplexSectionRDI = _PortDevIwfMultiplexSectionRDI_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 5, 1, 1, 25),
    _PortDevIwfMultiplexSectionRDI_Type()
)
portDevIwfMultiplexSectionRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfMultiplexSectionRDI.setStatus("current")
_PortDevIwfPmList_ObjectIdentity = ObjectIdentity
portDevIwfPmList = _PortDevIwfPmList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 6)
)
_PortDevIwfPmTable_Object = MibTable
portDevIwfPmTable = _PortDevIwfPmTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 6, 1)
)
if mibBuilder.loadTexts:
    portDevIwfPmTable.setStatus("current")
_PortDevIwfPmEntry_Object = MibTableRow
portDevIwfPmEntry = _PortDevIwfPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 6, 1, 1)
)
portDevIwfPmEntry.setIndexNames(
    (0, "LUM-PORTDEVICE-MIB", "portDevIwfPmIndex"),
)
if mibBuilder.loadTexts:
    portDevIwfPmEntry.setStatus("current")


class _PortDevIwfPmIndex_Type(Unsigned32):
    """Custom type portDevIwfPmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortDevIwfPmIndex_Type.__name__ = "Unsigned32"
_PortDevIwfPmIndex_Object = MibTableColumn
portDevIwfPmIndex = _PortDevIwfPmIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 6, 1, 1, 1),
    _PortDevIwfPmIndex_Type()
)
portDevIwfPmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfPmIndex.setStatus("current")
_PortDevIwfPmName_Type = MgmtNameString
_PortDevIwfPmName_Object = MibTableColumn
portDevIwfPmName = _PortDevIwfPmName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 6, 1, 1, 2),
    _PortDevIwfPmName_Type()
)
portDevIwfPmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfPmName.setStatus("current")
_PortDevIwfPmRxPackets_Type = Counter64
_PortDevIwfPmRxPackets_Object = MibTableColumn
portDevIwfPmRxPackets = _PortDevIwfPmRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 6, 1, 1, 3),
    _PortDevIwfPmRxPackets_Type()
)
portDevIwfPmRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfPmRxPackets.setStatus("current")
_PortDevIwfPmTxPackets_Type = Counter64
_PortDevIwfPmTxPackets_Object = MibTableColumn
portDevIwfPmTxPackets = _PortDevIwfPmTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 6, 1, 1, 4),
    _PortDevIwfPmTxPackets_Type()
)
portDevIwfPmTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfPmTxPackets.setStatus("current")
_PortDevIwfPmMalformedPackets_Type = Counter64
_PortDevIwfPmMalformedPackets_Object = MibTableColumn
portDevIwfPmMalformedPackets = _PortDevIwfPmMalformedPackets_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 6, 1, 1, 5),
    _PortDevIwfPmMalformedPackets_Type()
)
portDevIwfPmMalformedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfPmMalformedPackets.setStatus("current")
_PortDevIwfPmReorderedPackets_Type = Counter64
_PortDevIwfPmReorderedPackets_Object = MibTableColumn
portDevIwfPmReorderedPackets = _PortDevIwfPmReorderedPackets_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 6, 1, 1, 6),
    _PortDevIwfPmReorderedPackets_Type()
)
portDevIwfPmReorderedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfPmReorderedPackets.setStatus("current")
_PortDevIwfPmMisorderedDroppedPackets_Type = Counter64
_PortDevIwfPmMisorderedDroppedPackets_Object = MibTableColumn
portDevIwfPmMisorderedDroppedPackets = _PortDevIwfPmMisorderedDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 6, 1, 1, 7),
    _PortDevIwfPmMisorderedDroppedPackets_Type()
)
portDevIwfPmMisorderedDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfPmMisorderedDroppedPackets.setStatus("current")
_PortDevIwfPmMissingPackets_Type = Counter64
_PortDevIwfPmMissingPackets_Object = MibTableColumn
portDevIwfPmMissingPackets = _PortDevIwfPmMissingPackets_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 6, 1, 1, 8),
    _PortDevIwfPmMissingPackets_Type()
)
portDevIwfPmMissingPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfPmMissingPackets.setStatus("current")
_PortDevIwfPmPlayedOutPackets_Type = Counter64
_PortDevIwfPmPlayedOutPackets_Object = MibTableColumn
portDevIwfPmPlayedOutPackets = _PortDevIwfPmPlayedOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 6, 1, 1, 9),
    _PortDevIwfPmPlayedOutPackets_Type()
)
portDevIwfPmPlayedOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfPmPlayedOutPackets.setStatus("current")
_PortDevIwfPmJbOverrun_Type = Counter64
_PortDevIwfPmJbOverrun_Object = MibTableColumn
portDevIwfPmJbOverrun = _PortDevIwfPmJbOverrun_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 6, 1, 1, 10),
    _PortDevIwfPmJbOverrun_Type()
)
portDevIwfPmJbOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfPmJbOverrun.setStatus("current")
_PortDevIwfPmJbUnderrun_Type = Counter64
_PortDevIwfPmJbUnderrun_Object = MibTableColumn
portDevIwfPmJbUnderrun = _PortDevIwfPmJbUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 6, 1, 1, 11),
    _PortDevIwfPmJbUnderrun_Type()
)
portDevIwfPmJbUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfPmJbUnderrun.setStatus("current")


class _PortDevIwfPmReset_Type(Integer32):
    """Custom type portDevIwfPmReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PortDevIwfPmReset_Type.__name__ = "Integer32"
_PortDevIwfPmReset_Object = MibTableColumn
portDevIwfPmReset = _PortDevIwfPmReset_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 6, 1, 1, 12),
    _PortDevIwfPmReset_Type()
)
portDevIwfPmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevIwfPmReset.setStatus("current")


class _PortDevIwfPmInternalReference_Type(Unsigned32):
    """Custom type portDevIwfPmInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PortDevIwfPmInternalReference_Type.__name__ = "Unsigned32"
_PortDevIwfPmInternalReference_Object = MibTableColumn
portDevIwfPmInternalReference = _PortDevIwfPmInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 6, 1, 1, 13),
    _PortDevIwfPmInternalReference_Type()
)
portDevIwfPmInternalReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIwfPmInternalReference.setStatus("current")


class _PortDevIwfPmE1ChannelId_Type(Unsigned32):
    """Custom type portDevIwfPmE1ChannelId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PortDevIwfPmE1ChannelId_Type.__name__ = "Unsigned32"
_PortDevIwfPmE1ChannelId_Object = MibTableColumn
portDevIwfPmE1ChannelId = _PortDevIwfPmE1ChannelId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 2, 6, 1, 1, 14),
    _PortDevIwfPmE1ChannelId_Type()
)
portDevIwfPmE1ChannelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevIwfPmE1ChannelId.setStatus("current")

# Managed Objects groups

portDevGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 1, 1, 1)
)
portDevGeneralGroupV1.setObjects(
      *(("LUM-PORTDEVICE-MIB", "portDevGeneralLastChangeTime"),
        ("LUM-PORTDEVICE-MIB", "portDevGeneralStateLastChangeTime"),
        ("LUM-PORTDEVICE-MIB", "portDevGeneralGenericTableSize"),
        ("LUM-PORTDEVICE-MIB", "portDevGeneralEquipmentTableSize"),
        ("LUM-PORTDEVICE-MIB", "portDevGeneralFwTableSize"),
        ("LUM-PORTDEVICE-MIB", "portDevGeneralIwfTableSize"),
        ("LUM-PORTDEVICE-MIB", "portDevGeneralIwfPmTableSize"))
)
if mibBuilder.loadTexts:
    portDevGeneralGroupV1.setStatus("current")

portDevGenericGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 1, 1, 2)
)
portDevGenericGroupV1.setObjects(
      *(("LUM-PORTDEVICE-MIB", "portDevGenericIndex"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericName"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericSubrack"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericSlot"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericAutoDiscoverInterval"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericCreateNewPortDevice"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericCreateMep"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericCreateMeg"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericCreateNewPortDevice"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericRestartPortDevice"))
)
if mibBuilder.loadTexts:
    portDevGenericGroupV1.setStatus("deprecated")

portDevEquipmentGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 1, 1, 3)
)
portDevEquipmentGroupV1.setObjects(
      *(("LUM-PORTDEVICE-MIB", "portDevEquipmentIndex"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentName"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDescr"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentLocation"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentAdminStatus"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentOperStatus"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentExpectedType"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentActualType"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentFwVersion"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentLinkPassThrough"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentSelectedPort"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentSubrack"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentSlot"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentVlanId"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentRowStatus"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentNoDeviceFound"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentMultiDeviceFound"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDeviceNotManageable"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDeviceNotReachable"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentConfigurationFault"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentPowerAMissing"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentPowerBMissing"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentInternalReference"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentMacAddress"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentLocalPortIndex"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentAdminPowerA"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentAdminPowerB"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDestMacAddress"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDestMacAddressCheck"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentFwUpgradeStatus"))
)
if mibBuilder.loadTexts:
    portDevEquipmentGroupV1.setStatus("deprecated")

portDevFwGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 1, 1, 4)
)
portDevFwGroupV1.setObjects(
      *(("LUM-PORTDEVICE-MIB", "portDevFwIndex"),
        ("LUM-PORTDEVICE-MIB", "portDevFwSubrack"),
        ("LUM-PORTDEVICE-MIB", "portDevFwSlot"),
        ("LUM-PORTDEVICE-MIB", "portDevFwName"),
        ("LUM-PORTDEVICE-MIB", "portDevFwPortDevId"),
        ("LUM-PORTDEVICE-MIB", "portDevFwImgSlotOneNr"),
        ("LUM-PORTDEVICE-MIB", "portDevFwImgSlotOneVersion"),
        ("LUM-PORTDEVICE-MIB", "portDevFwImgSlotOneState"),
        ("LUM-PORTDEVICE-MIB", "portDevFwImgSlotOneDate"),
        ("LUM-PORTDEVICE-MIB", "portDevFwImgSlotTwoNr"),
        ("LUM-PORTDEVICE-MIB", "portDevFwImgSlotTwoVersion"),
        ("LUM-PORTDEVICE-MIB", "portDevFwImgSlotTwoState"),
        ("LUM-PORTDEVICE-MIB", "portDevFwImgSlotTwoDate"),
        ("LUM-PORTDEVICE-MIB", "portDevFwInstallFw"),
        ("LUM-PORTDEVICE-MIB", "portDevFwActivateFw"),
        ("LUM-PORTDEVICE-MIB", "portDevFwGetAllFiles"),
        ("LUM-PORTDEVICE-MIB", "portDevFwUpgradeStatus"))
)
if mibBuilder.loadTexts:
    portDevFwGroupV1.setStatus("current")

portDevIwfGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 1, 1, 5)
)
portDevIwfGroupV1.setObjects(
      *(("LUM-PORTDEVICE-MIB", "portDevIwfIndex"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfName"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfRtpClockSource"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfJitterBufferRecenter"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfInternalReference"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfLocalPortIndex"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfLossOfSignal"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfLossOfFrame"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfEquipmentFailure"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfNoTdmPayload"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfRemotePacketLost"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfLocalPacketLost"))
)
if mibBuilder.loadTexts:
    portDevIwfGroupV1.setStatus("deprecated")

portDevIwfPmGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 1, 1, 6)
)
portDevIwfPmGroupV1.setObjects(
      *(("LUM-PORTDEVICE-MIB", "portDevIwfPmIndex"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmName"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmRxPackets"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmTxPackets"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmMalformedPackets"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmReorderedPackets"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmMisorderedDroppedPackets"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmMissingPackets"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmPlayedOutPackets"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmJbOverrun"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmJbUnderrun"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmReset"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmInternalReference"))
)
if mibBuilder.loadTexts:
    portDevIwfPmGroupV1.setStatus("deprecated")

portDevEquipmentGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 1, 1, 7)
)
portDevEquipmentGroupV2.setObjects(
      *(("LUM-PORTDEVICE-MIB", "portDevEquipmentIndex"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentName"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDescr"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentLocation"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentAdminStatus"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentOperStatus"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentExpectedType"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentActualType"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentFwVersion"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentLinkPassThrough"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentSubrack"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentSlot"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentVlanId"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentRowStatus"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentNoDeviceFound"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentMultiDeviceFound"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDeviceNotManageable"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDeviceNotReachable"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentConfigurationFault"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentPowerAMissing"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentPowerBMissing"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentInternalReference"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentMacAddress"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentLocalPortIndex"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentAdminPowerA"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentAdminPowerB"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDestMacAddress"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDestMacAddressCheck"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentFwUpgradeStatus"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDeviceVersionType"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentSelectedPort"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentActivePort"))
)
if mibBuilder.loadTexts:
    portDevEquipmentGroupV2.setStatus("deprecated")

portDevEquipmentGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 1, 1, 8)
)
portDevEquipmentGroupV3.setObjects(
      *(("LUM-PORTDEVICE-MIB", "portDevEquipmentIndex"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentName"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDescr"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentLocation"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentAdminStatus"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentOperStatus"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentExpectedType"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentActualType"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentFwVersion"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentFwUpgradeStatus"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentLinkPassThrough"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentSubrack"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentSlot"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentVlanId"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentRowStatus"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentNoDeviceFound"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentMultiDeviceFound"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDeviceNotManageable"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDeviceNotReachable"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentConfigurationFault"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentPowerAMissing"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentPowerBMissing"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentInternalReference"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentMacAddress"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentLocalPortIndex"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentAdminPowerA"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentAdminPowerB"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentSelectedPort"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDestMacAddress"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDestMacAddressCheck"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDeviceVersionType"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentActivePort"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDyingGasp"))
)
if mibBuilder.loadTexts:
    portDevEquipmentGroupV3.setStatus("deprecated")

portDevIwfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 1, 1, 9)
)
portDevIwfGroupV2.setObjects(
      *(("LUM-PORTDEVICE-MIB", "portDevIwfIndex"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfName"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfRtpClockSource"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfJitterBufferRecenter"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfInternalReference"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfLocalPortIndex"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfLossOfSignal"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfLossOfFrame"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfEquipmentFailure"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfNoTdmPayload"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfRemotePacketLost"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfLocalPacketLost"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfTributaryUnitAlarm"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfMultiplexSectionAlarm"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfMultiplexSectionRDI"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfAdminStatus"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfOperStatus"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfDescr"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfEtherType"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfSignalFormat"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfVlanId"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfVlanPriority"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfE1ChannelId"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfE1ChannelKLM"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfDestMacAddress"))
)
if mibBuilder.loadTexts:
    portDevIwfGroupV2.setStatus("current")

portDevIwfPmGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 1, 1, 10)
)
portDevIwfPmGroupV2.setObjects(
      *(("LUM-PORTDEVICE-MIB", "portDevIwfPmIndex"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmName"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmRxPackets"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmTxPackets"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmMalformedPackets"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmReorderedPackets"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmMisorderedDroppedPackets"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmMissingPackets"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmPlayedOutPackets"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmJbOverrun"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmJbUnderrun"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmReset"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmInternalReference"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmE1ChannelId"))
)
if mibBuilder.loadTexts:
    portDevIwfPmGroupV2.setStatus("current")

portDevEquipmentGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 1, 1, 11)
)
portDevEquipmentGroupV4.setObjects(
      *(("LUM-PORTDEVICE-MIB", "portDevEquipmentIndex"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentName"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDescr"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentLocation"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentAdminStatus"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentOperStatus"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentExpectedType"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentActualType"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentFwVersion"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentFwUpgradeStatus"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentLinkPassThrough"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentSubrack"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentSlot"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentVlanId"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentRowStatus"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentNoDeviceFound"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentMultiDeviceFound"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDeviceNotManageable"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDeviceNotReachable"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentConfigurationFault"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentPowerAMissing"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentPowerBMissing"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentInternalReference"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentMacAddress"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentLocalPortIndex"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentAdminPowerA"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentAdminPowerB"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentSelectedPort"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDestMacAddressCheck"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDeviceVersionType"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentActivePort"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDyingGasp"))
)
if mibBuilder.loadTexts:
    portDevEquipmentGroupV4.setStatus("deprecated")

portDevEquipmentGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 1, 1, 12)
)
portDevEquipmentGroupV5.setObjects(
      *(("LUM-PORTDEVICE-MIB", "portDevEquipmentIndex"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentName"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDescr"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentLocation"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentAdminStatus"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentOperStatus"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentExpectedType"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentActualType"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentFwVersion"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentFwUpgradeStatus"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentLinkPassThrough"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentSubrack"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentSlot"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentVlanId"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentRowStatus"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentNoDeviceFound"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentMultiDeviceFound"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDeviceNotManageable"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDeviceNotReachable"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentConfigurationFault"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentPowerAMissing"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentPowerBMissing"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentInternalReference"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentMacAddress"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentLocalPortIndex"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentAdminPowerA"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentAdminPowerB"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentSelectedPort"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDestMacAddressCheck"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDeviceVersionType"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentActivePort"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentDyingGasp"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentLosCsf"))
)
if mibBuilder.loadTexts:
    portDevEquipmentGroupV5.setStatus("current")

portDevGenericGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 1, 1, 13)
)
portDevGenericGroupV2.setObjects(
      *(("LUM-PORTDEVICE-MIB", "portDevGenericIndex"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericName"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericSubrack"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericSlot"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericAutoDiscoverInterval"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericCreateNewPortDevice"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericCreateMep"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericCreateMeg"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericCreateNewPortDevice"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericRestartPortDevice"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericCreateNewPortDeviceAdvanced"))
)
if mibBuilder.loadTexts:
    portDevGenericGroupV2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumPortdeviceBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 1, 2, 1)
)
lumPortdeviceBasicComplV1.setObjects(
      *(("LUM-PORTDEVICE-MIB", "portDevGeneralGroupV1"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericGroupV1"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentGroupV1"),
        ("LUM-PORTDEVICE-MIB", "portDevFwGroupV1"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfGroupV1"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmGroupV1"))
)
if mibBuilder.loadTexts:
    lumPortdeviceBasicComplV1.setStatus(
        "deprecated"
    )

lumPortdeviceBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 1, 2, 2)
)
lumPortdeviceBasicComplV2.setObjects(
      *(("LUM-PORTDEVICE-MIB", "portDevGeneralGroupV1"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericGroupV1"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentGroupV2"),
        ("LUM-PORTDEVICE-MIB", "portDevFwGroupV1"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfGroupV1"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmGroupV1"))
)
if mibBuilder.loadTexts:
    lumPortdeviceBasicComplV2.setStatus(
        "deprecated"
    )

lumPortdeviceBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 1, 2, 3)
)
lumPortdeviceBasicComplV3.setObjects(
      *(("LUM-PORTDEVICE-MIB", "portDevGeneralGroupV1"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericGroupV1"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentGroupV3"),
        ("LUM-PORTDEVICE-MIB", "portDevFwGroupV1"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfGroupV1"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmGroupV1"))
)
if mibBuilder.loadTexts:
    lumPortdeviceBasicComplV3.setStatus(
        "deprecated"
    )

lumPortdeviceBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 1, 2, 4)
)
lumPortdeviceBasicComplV4.setObjects(
      *(("LUM-PORTDEVICE-MIB", "portDevGeneralGroupV1"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericGroupV1"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentGroupV4"),
        ("LUM-PORTDEVICE-MIB", "portDevFwGroupV1"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfGroupV2"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmGroupV2"))
)
if mibBuilder.loadTexts:
    lumPortdeviceBasicComplV4.setStatus(
        "deprecated"
    )

lumPortdeviceBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 1, 2, 5)
)
lumPortdeviceBasicComplV5.setObjects(
      *(("LUM-PORTDEVICE-MIB", "portDevGeneralGroupV1"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericGroupV1"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentGroupV5"),
        ("LUM-PORTDEVICE-MIB", "portDevFwGroupV1"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfGroupV2"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmGroupV2"))
)
if mibBuilder.loadTexts:
    lumPortdeviceBasicComplV5.setStatus(
        "deprecated"
    )

lumPortdeviceBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 57, 1, 2, 6)
)
lumPortdeviceBasicComplV6.setObjects(
      *(("LUM-PORTDEVICE-MIB", "portDevGeneralGroupV1"),
        ("LUM-PORTDEVICE-MIB", "portDevGenericGroupV2"),
        ("LUM-PORTDEVICE-MIB", "portDevEquipmentGroupV5"),
        ("LUM-PORTDEVICE-MIB", "portDevFwGroupV1"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfGroupV2"),
        ("LUM-PORTDEVICE-MIB", "portDevIwfPmGroupV2"))
)
if mibBuilder.loadTexts:
    lumPortdeviceBasicComplV6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-PORTDEVICE-MIB",
    **{"PortDeviceEquipmentType": PortDeviceEquipmentType,
       "PortDeviceVersionType": PortDeviceVersionType,
       "PortDevFwImgState": PortDevFwImgState,
       "PortSelection": PortSelection,
       "lumPortdeviceMIBModule": lumPortdeviceMIBModule,
       "lumPortdeviceConfs": lumPortdeviceConfs,
       "lumPortdeviceGroups": lumPortdeviceGroups,
       "portDevGeneralGroupV1": portDevGeneralGroupV1,
       "portDevGenericGroupV1": portDevGenericGroupV1,
       "portDevEquipmentGroupV1": portDevEquipmentGroupV1,
       "portDevFwGroupV1": portDevFwGroupV1,
       "portDevIwfGroupV1": portDevIwfGroupV1,
       "portDevIwfPmGroupV1": portDevIwfPmGroupV1,
       "portDevEquipmentGroupV2": portDevEquipmentGroupV2,
       "portDevEquipmentGroupV3": portDevEquipmentGroupV3,
       "portDevIwfGroupV2": portDevIwfGroupV2,
       "portDevIwfPmGroupV2": portDevIwfPmGroupV2,
       "portDevEquipmentGroupV4": portDevEquipmentGroupV4,
       "portDevEquipmentGroupV5": portDevEquipmentGroupV5,
       "portDevGenericGroupV2": portDevGenericGroupV2,
       "lumPortdeviceCompl": lumPortdeviceCompl,
       "lumPortdeviceBasicComplV1": lumPortdeviceBasicComplV1,
       "lumPortdeviceBasicComplV2": lumPortdeviceBasicComplV2,
       "lumPortdeviceBasicComplV3": lumPortdeviceBasicComplV3,
       "lumPortdeviceBasicComplV4": lumPortdeviceBasicComplV4,
       "lumPortdeviceBasicComplV5": lumPortdeviceBasicComplV5,
       "lumPortdeviceBasicComplV6": lumPortdeviceBasicComplV6,
       "lumPortdeviceMIBObjects": lumPortdeviceMIBObjects,
       "portDevGeneral": portDevGeneral,
       "portDevGeneralLastChangeTime": portDevGeneralLastChangeTime,
       "portDevGeneralStateLastChangeTime": portDevGeneralStateLastChangeTime,
       "portDevGeneralGenericTableSize": portDevGeneralGenericTableSize,
       "portDevGeneralEquipmentTableSize": portDevGeneralEquipmentTableSize,
       "portDevGeneralFwTableSize": portDevGeneralFwTableSize,
       "portDevGeneralIwfTableSize": portDevGeneralIwfTableSize,
       "portDevGeneralIwfPmTableSize": portDevGeneralIwfPmTableSize,
       "portDevGenericList": portDevGenericList,
       "portDevGenericTable": portDevGenericTable,
       "portDevGenericEntry": portDevGenericEntry,
       "portDevGenericIndex": portDevGenericIndex,
       "portDevGenericName": portDevGenericName,
       "portDevGenericSubrack": portDevGenericSubrack,
       "portDevGenericSlot": portDevGenericSlot,
       "portDevGenericAutoDiscoverInterval": portDevGenericAutoDiscoverInterval,
       "portDevGenericCreateNewPortDevice": portDevGenericCreateNewPortDevice,
       "portDevGenericRestartPortDevice": portDevGenericRestartPortDevice,
       "portDevGenericCreateMep": portDevGenericCreateMep,
       "portDevGenericCreateMeg": portDevGenericCreateMeg,
       "portDevGenericCreateNewPortDeviceAdvanced": portDevGenericCreateNewPortDeviceAdvanced,
       "portDevEquipmentList": portDevEquipmentList,
       "portDevEquipmentTable": portDevEquipmentTable,
       "portDevEquipmentEntry": portDevEquipmentEntry,
       "portDevEquipmentIndex": portDevEquipmentIndex,
       "portDevEquipmentName": portDevEquipmentName,
       "portDevEquipmentDescr": portDevEquipmentDescr,
       "portDevEquipmentLocation": portDevEquipmentLocation,
       "portDevEquipmentAdminStatus": portDevEquipmentAdminStatus,
       "portDevEquipmentOperStatus": portDevEquipmentOperStatus,
       "portDevEquipmentExpectedType": portDevEquipmentExpectedType,
       "portDevEquipmentActualType": portDevEquipmentActualType,
       "portDevEquipmentFwVersion": portDevEquipmentFwVersion,
       "portDevEquipmentFwUpgradeStatus": portDevEquipmentFwUpgradeStatus,
       "portDevEquipmentLinkPassThrough": portDevEquipmentLinkPassThrough,
       "portDevEquipmentSubrack": portDevEquipmentSubrack,
       "portDevEquipmentSlot": portDevEquipmentSlot,
       "portDevEquipmentVlanId": portDevEquipmentVlanId,
       "portDevEquipmentRowStatus": portDevEquipmentRowStatus,
       "portDevEquipmentNoDeviceFound": portDevEquipmentNoDeviceFound,
       "portDevEquipmentMultiDeviceFound": portDevEquipmentMultiDeviceFound,
       "portDevEquipmentDeviceNotManageable": portDevEquipmentDeviceNotManageable,
       "portDevEquipmentDeviceNotReachable": portDevEquipmentDeviceNotReachable,
       "portDevEquipmentConfigurationFault": portDevEquipmentConfigurationFault,
       "portDevEquipmentPowerAMissing": portDevEquipmentPowerAMissing,
       "portDevEquipmentPowerBMissing": portDevEquipmentPowerBMissing,
       "portDevEquipmentInternalReference": portDevEquipmentInternalReference,
       "portDevEquipmentMacAddress": portDevEquipmentMacAddress,
       "portDevEquipmentLocalPortIndex": portDevEquipmentLocalPortIndex,
       "portDevEquipmentAdminPowerA": portDevEquipmentAdminPowerA,
       "portDevEquipmentAdminPowerB": portDevEquipmentAdminPowerB,
       "portDevEquipmentSelectedPort": portDevEquipmentSelectedPort,
       "portDevEquipmentDestMacAddress": portDevEquipmentDestMacAddress,
       "portDevEquipmentDestMacAddressCheck": portDevEquipmentDestMacAddressCheck,
       "portDevEquipmentDeviceVersionType": portDevEquipmentDeviceVersionType,
       "portDevEquipmentActivePort": portDevEquipmentActivePort,
       "portDevEquipmentDyingGasp": portDevEquipmentDyingGasp,
       "portDevEquipmentLosCsf": portDevEquipmentLosCsf,
       "portDevFwList": portDevFwList,
       "portDevFwTable": portDevFwTable,
       "portDevFwEntry": portDevFwEntry,
       "portDevFwIndex": portDevFwIndex,
       "portDevFwSubrack": portDevFwSubrack,
       "portDevFwSlot": portDevFwSlot,
       "portDevFwName": portDevFwName,
       "portDevFwPortDevId": portDevFwPortDevId,
       "portDevFwImgSlotOneNr": portDevFwImgSlotOneNr,
       "portDevFwImgSlotOneVersion": portDevFwImgSlotOneVersion,
       "portDevFwImgSlotOneState": portDevFwImgSlotOneState,
       "portDevFwImgSlotOneDate": portDevFwImgSlotOneDate,
       "portDevFwImgSlotTwoNr": portDevFwImgSlotTwoNr,
       "portDevFwImgSlotTwoVersion": portDevFwImgSlotTwoVersion,
       "portDevFwImgSlotTwoState": portDevFwImgSlotTwoState,
       "portDevFwImgSlotTwoDate": portDevFwImgSlotTwoDate,
       "portDevFwInstallFw": portDevFwInstallFw,
       "portDevFwActivateFw": portDevFwActivateFw,
       "portDevFwGetAllFiles": portDevFwGetAllFiles,
       "portDevFwUpgradeStatus": portDevFwUpgradeStatus,
       "portDevIwfList": portDevIwfList,
       "portDevIwfTable": portDevIwfTable,
       "portDevIwfEntry": portDevIwfEntry,
       "portDevIwfIndex": portDevIwfIndex,
       "portDevIwfName": portDevIwfName,
       "portDevIwfRtpClockSource": portDevIwfRtpClockSource,
       "portDevIwfJitterBufferRecenter": portDevIwfJitterBufferRecenter,
       "portDevIwfInternalReference": portDevIwfInternalReference,
       "portDevIwfLocalPortIndex": portDevIwfLocalPortIndex,
       "portDevIwfLossOfSignal": portDevIwfLossOfSignal,
       "portDevIwfLossOfFrame": portDevIwfLossOfFrame,
       "portDevIwfEquipmentFailure": portDevIwfEquipmentFailure,
       "portDevIwfNoTdmPayload": portDevIwfNoTdmPayload,
       "portDevIwfRemotePacketLost": portDevIwfRemotePacketLost,
       "portDevIwfLocalPacketLost": portDevIwfLocalPacketLost,
       "portDevIwfAdminStatus": portDevIwfAdminStatus,
       "portDevIwfOperStatus": portDevIwfOperStatus,
       "portDevIwfDescr": portDevIwfDescr,
       "portDevIwfSignalFormat": portDevIwfSignalFormat,
       "portDevIwfEtherType": portDevIwfEtherType,
       "portDevIwfVlanId": portDevIwfVlanId,
       "portDevIwfVlanPriority": portDevIwfVlanPriority,
       "portDevIwfE1ChannelId": portDevIwfE1ChannelId,
       "portDevIwfE1ChannelKLM": portDevIwfE1ChannelKLM,
       "portDevIwfDestMacAddress": portDevIwfDestMacAddress,
       "portDevIwfTributaryUnitAlarm": portDevIwfTributaryUnitAlarm,
       "portDevIwfMultiplexSectionAlarm": portDevIwfMultiplexSectionAlarm,
       "portDevIwfMultiplexSectionRDI": portDevIwfMultiplexSectionRDI,
       "portDevIwfPmList": portDevIwfPmList,
       "portDevIwfPmTable": portDevIwfPmTable,
       "portDevIwfPmEntry": portDevIwfPmEntry,
       "portDevIwfPmIndex": portDevIwfPmIndex,
       "portDevIwfPmName": portDevIwfPmName,
       "portDevIwfPmRxPackets": portDevIwfPmRxPackets,
       "portDevIwfPmTxPackets": portDevIwfPmTxPackets,
       "portDevIwfPmMalformedPackets": portDevIwfPmMalformedPackets,
       "portDevIwfPmReorderedPackets": portDevIwfPmReorderedPackets,
       "portDevIwfPmMisorderedDroppedPackets": portDevIwfPmMisorderedDroppedPackets,
       "portDevIwfPmMissingPackets": portDevIwfPmMissingPackets,
       "portDevIwfPmPlayedOutPackets": portDevIwfPmPlayedOutPackets,
       "portDevIwfPmJbOverrun": portDevIwfPmJbOverrun,
       "portDevIwfPmJbUnderrun": portDevIwfPmJbUnderrun,
       "portDevIwfPmReset": portDevIwfPmReset,
       "portDevIwfPmInternalReference": portDevIwfPmInternalReference,
       "portDevIwfPmE1ChannelId": portDevIwfPmE1ChannelId}
)
