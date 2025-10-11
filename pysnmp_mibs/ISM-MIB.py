# SNMP MIB module (ISM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/ISM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:23:06 2025
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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwStorage = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4)
)
if mibBuilder.loadTexts:
    hwStorage.setRevisions(
        ("2013-04-06 13:54",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NodeCodeString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 17),
    )



# MIB Managed Objects in the order of their OIDs

_Huaweistorage_ObjectIdentity = ObjectIdentity
huaweistorage = _Huaweistorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774)
)
_HwISM_ObjectIdentity = ObjectIdentity
hwISM = _HwISM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1)
)
_HwMIB_ObjectIdentity = ObjectIdentity
hwMIB = _HwMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22)
)
_HwInfoControllerTable_Object = MibTable
hwInfoControllerTable = _HwInfoControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 1)
)
if mibBuilder.loadTexts:
    hwInfoControllerTable.setStatus("current")
_HwInfoControllerEntry_Object = MibTableRow
hwInfoControllerEntry = _HwInfoControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 1, 1)
)
hwInfoControllerEntry.setIndexNames(
    (0, "ISM-MIB", "hwInfoControllerID"),
)
if mibBuilder.loadTexts:
    hwInfoControllerEntry.setStatus("current")
_HwInfoControllerID_Type = Unsigned32
_HwInfoControllerID_Object = MibTableColumn
hwInfoControllerID = _HwInfoControllerID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 1, 1, 1),
    _HwInfoControllerID_Type()
)
hwInfoControllerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerID.setStatus("current")
_HwInfoControllerIP_Type = OctetString
_HwInfoControllerIP_Object = MibTableColumn
hwInfoControllerIP = _HwInfoControllerIP_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 1, 1, 2),
    _HwInfoControllerIP_Type()
)
hwInfoControllerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerIP.setStatus("current")
_HwInfoControllerIsMaster_Type = Unsigned32
_HwInfoControllerIsMaster_Object = MibTableColumn
hwInfoControllerIsMaster = _HwInfoControllerIsMaster_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 1, 1, 3),
    _HwInfoControllerIsMaster_Type()
)
hwInfoControllerIsMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerIsMaster.setStatus("current")
_HwInfoControllerCpuUsingRatio_Type = Unsigned32
_HwInfoControllerCpuUsingRatio_Object = MibTableColumn
hwInfoControllerCpuUsingRatio = _HwInfoControllerCpuUsingRatio_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 1, 1, 4),
    _HwInfoControllerCpuUsingRatio_Type()
)
hwInfoControllerCpuUsingRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerCpuUsingRatio.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoControllerCpuUsingRatio.setUnits("%")
_HwInfoControllerMemoryUsingRatio_Type = Unsigned32
_HwInfoControllerMemoryUsingRatio_Object = MibTableColumn
hwInfoControllerMemoryUsingRatio = _HwInfoControllerMemoryUsingRatio_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 1, 1, 5),
    _HwInfoControllerMemoryUsingRatio_Type()
)
hwInfoControllerMemoryUsingRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerMemoryUsingRatio.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoControllerMemoryUsingRatio.setUnits("%")
_HwInfoControllerVersion_Type = OctetString
_HwInfoControllerVersion_Object = MibTableColumn
hwInfoControllerVersion = _HwInfoControllerVersion_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 1, 1, 6),
    _HwInfoControllerVersion_Type()
)
hwInfoControllerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerVersion.setStatus("current")
_HwInfoControllerStatus_Type = Unsigned32
_HwInfoControllerStatus_Object = MibTableColumn
hwInfoControllerStatus = _HwInfoControllerStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 1, 1, 7),
    _HwInfoControllerStatus_Type()
)
hwInfoControllerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerStatus.setStatus("current")
_HwInfoControllerDescription_Type = OctetString
_HwInfoControllerDescription_Object = MibTableColumn
hwInfoControllerDescription = _HwInfoControllerDescription_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 1, 1, 8),
    _HwInfoControllerDescription_Type()
)
hwInfoControllerDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerDescription.setStatus("current")
_HwInfoPhysicDiskTable_Object = MibTable
hwInfoPhysicDiskTable = _HwInfoPhysicDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 2)
)
if mibBuilder.loadTexts:
    hwInfoPhysicDiskTable.setStatus("current")
_HwInfoPhysicDiskEntry_Object = MibTableRow
hwInfoPhysicDiskEntry = _HwInfoPhysicDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 2, 1)
)
hwInfoPhysicDiskEntry.setIndexNames(
    (0, "ISM-MIB", "hwInfoPhysicDiskFrameID"),
    (0, "ISM-MIB", "hwInfoPhysicDiskSlotID"),
)
if mibBuilder.loadTexts:
    hwInfoPhysicDiskEntry.setStatus("current")
_HwInfoPhysicDiskFrameID_Type = Unsigned32
_HwInfoPhysicDiskFrameID_Object = MibTableColumn
hwInfoPhysicDiskFrameID = _HwInfoPhysicDiskFrameID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 2, 1, 1),
    _HwInfoPhysicDiskFrameID_Type()
)
hwInfoPhysicDiskFrameID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPhysicDiskFrameID.setStatus("current")
_HwInfoPhysicDiskSlotID_Type = Unsigned32
_HwInfoPhysicDiskSlotID_Object = MibTableColumn
hwInfoPhysicDiskSlotID = _HwInfoPhysicDiskSlotID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 2, 1, 2),
    _HwInfoPhysicDiskSlotID_Type()
)
hwInfoPhysicDiskSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPhysicDiskSlotID.setStatus("current")
_HwInfoPhysicDiskStatus_Type = Unsigned32
_HwInfoPhysicDiskStatus_Object = MibTableColumn
hwInfoPhysicDiskStatus = _HwInfoPhysicDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 2, 1, 3),
    _HwInfoPhysicDiskStatus_Type()
)
hwInfoPhysicDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPhysicDiskStatus.setStatus("current")
_HwInfoPhysicDiskSZType_Type = Unsigned32
_HwInfoPhysicDiskSZType_Object = MibTableColumn
hwInfoPhysicDiskSZType = _HwInfoPhysicDiskSZType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 2, 1, 4),
    _HwInfoPhysicDiskSZType_Type()
)
hwInfoPhysicDiskSZType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPhysicDiskSZType.setStatus("current")
_HwInfoPhysicDiskSZVendor_Type = OctetString
_HwInfoPhysicDiskSZVendor_Object = MibTableColumn
hwInfoPhysicDiskSZVendor = _HwInfoPhysicDiskSZVendor_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 2, 1, 5),
    _HwInfoPhysicDiskSZVendor_Type()
)
hwInfoPhysicDiskSZVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPhysicDiskSZVendor.setStatus("current")
_HwInfoPhysicDiskSZModel_Type = OctetString
_HwInfoPhysicDiskSZModel_Object = MibTableColumn
hwInfoPhysicDiskSZModel = _HwInfoPhysicDiskSZModel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 2, 1, 6),
    _HwInfoPhysicDiskSZModel_Type()
)
hwInfoPhysicDiskSZModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPhysicDiskSZModel.setStatus("current")
_HwInfoPhysicDiskSZSerial_Type = OctetString
_HwInfoPhysicDiskSZSerial_Object = MibTableColumn
hwInfoPhysicDiskSZSerial = _HwInfoPhysicDiskSZSerial_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 2, 1, 7),
    _HwInfoPhysicDiskSZSerial_Type()
)
hwInfoPhysicDiskSZSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPhysicDiskSZSerial.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoPhysicDiskSZSerial.setUnits("GB")
_HwInfoPhysicDiskSZFirmware_Type = OctetString
_HwInfoPhysicDiskSZFirmware_Object = MibTableColumn
hwInfoPhysicDiskSZFirmware = _HwInfoPhysicDiskSZFirmware_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 2, 1, 8),
    _HwInfoPhysicDiskSZFirmware_Type()
)
hwInfoPhysicDiskSZFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPhysicDiskSZFirmware.setStatus("current")
_HwInfoPhysicDiskSpinSpeed_Type = Unsigned32
_HwInfoPhysicDiskSpinSpeed_Object = MibTableColumn
hwInfoPhysicDiskSpinSpeed = _HwInfoPhysicDiskSpinSpeed_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 2, 1, 9),
    _HwInfoPhysicDiskSpinSpeed_Type()
)
hwInfoPhysicDiskSpinSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPhysicDiskSpinSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoPhysicDiskSpinSpeed.setUnits("RPM")
_HwInfoPhysicDiskCurrentSpeed_Type = Unsigned32
_HwInfoPhysicDiskCurrentSpeed_Object = MibTableColumn
hwInfoPhysicDiskCurrentSpeed = _HwInfoPhysicDiskCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 2, 1, 10),
    _HwInfoPhysicDiskCurrentSpeed_Type()
)
hwInfoPhysicDiskCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPhysicDiskCurrentSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoPhysicDiskCurrentSpeed.setUnits("0.1Gpbs")
_HwInfoPhysicDiskRawCapacity_Type = Unsigned32
_HwInfoPhysicDiskRawCapacity_Object = MibTableColumn
hwInfoPhysicDiskRawCapacity = _HwInfoPhysicDiskRawCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 2, 1, 11),
    _HwInfoPhysicDiskRawCapacity_Type()
)
hwInfoPhysicDiskRawCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPhysicDiskRawCapacity.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoPhysicDiskRawCapacity.setUnits("GB")
_HwInfoLogicDiskTable_Object = MibTable
hwInfoLogicDiskTable = _HwInfoLogicDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 3)
)
if mibBuilder.loadTexts:
    hwInfoLogicDiskTable.setStatus("current")
_HwInfoLogicDiskEntry_Object = MibTableRow
hwInfoLogicDiskEntry = _HwInfoLogicDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 3, 1)
)
hwInfoLogicDiskEntry.setIndexNames(
    (0, "ISM-MIB", "hwInfoLogicDiskFrameID"),
    (0, "ISM-MIB", "hwInfoLogicDiskSlotID"),
)
if mibBuilder.loadTexts:
    hwInfoLogicDiskEntry.setStatus("current")
_HwInfoLogicDiskFrameID_Type = Unsigned32
_HwInfoLogicDiskFrameID_Object = MibTableColumn
hwInfoLogicDiskFrameID = _HwInfoLogicDiskFrameID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 3, 1, 1),
    _HwInfoLogicDiskFrameID_Type()
)
hwInfoLogicDiskFrameID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicDiskFrameID.setStatus("current")
_HwInfoLogicDiskSlotID_Type = Unsigned32
_HwInfoLogicDiskSlotID_Object = MibTableColumn
hwInfoLogicDiskSlotID = _HwInfoLogicDiskSlotID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 3, 1, 2),
    _HwInfoLogicDiskSlotID_Type()
)
hwInfoLogicDiskSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicDiskSlotID.setStatus("current")
_HwInfoLogicDiskLogicStatus_Type = Unsigned32
_HwInfoLogicDiskLogicStatus_Object = MibTableColumn
hwInfoLogicDiskLogicStatus = _HwInfoLogicDiskLogicStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 3, 1, 3),
    _HwInfoLogicDiskLogicStatus_Type()
)
hwInfoLogicDiskLogicStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicDiskLogicStatus.setStatus("current")
_HwInfoLogicDiskLogicType_Type = Unsigned32
_HwInfoLogicDiskLogicType_Object = MibTableColumn
hwInfoLogicDiskLogicType = _HwInfoLogicDiskLogicType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 3, 1, 4),
    _HwInfoLogicDiskLogicType_Type()
)
hwInfoLogicDiskLogicType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicDiskLogicType.setStatus("current")
_HwInfoLogicDiskSize_Type = Unsigned32
_HwInfoLogicDiskSize_Object = MibTableColumn
hwInfoLogicDiskSize = _HwInfoLogicDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 3, 1, 5),
    _HwInfoLogicDiskSize_Type()
)
hwInfoLogicDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoLogicDiskSize.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoLogicDiskSize.setUnits("GB")
_HwInfoPowerTable_Object = MibTable
hwInfoPowerTable = _HwInfoPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 4)
)
if mibBuilder.loadTexts:
    hwInfoPowerTable.setStatus("current")
_HwInfoPowerEntry_Object = MibTableRow
hwInfoPowerEntry = _HwInfoPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 4, 1)
)
hwInfoPowerEntry.setIndexNames(
    (0, "ISM-MIB", "hwInfoPowerID"),
    (0, "ISM-MIB", "hwInfoPowerSubrackID"),
)
if mibBuilder.loadTexts:
    hwInfoPowerEntry.setStatus("current")
_HwInfoPowerID_Type = Unsigned32
_HwInfoPowerID_Object = MibTableColumn
hwInfoPowerID = _HwInfoPowerID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 4, 1, 1),
    _HwInfoPowerID_Type()
)
hwInfoPowerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPowerID.setStatus("current")
_HwInfoPowerSubrackID_Type = Unsigned32
_HwInfoPowerSubrackID_Object = MibTableColumn
hwInfoPowerSubrackID = _HwInfoPowerSubrackID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 4, 1, 2),
    _HwInfoPowerSubrackID_Type()
)
hwInfoPowerSubrackID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPowerSubrackID.setStatus("current")
_HwInfoPowerStatus_Type = Unsigned32
_HwInfoPowerStatus_Object = MibTableColumn
hwInfoPowerStatus = _HwInfoPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 4, 1, 3),
    _HwInfoPowerStatus_Type()
)
hwInfoPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPowerStatus.setStatus("current")
_HwInfoPowerTemperature_Type = Unsigned32
_HwInfoPowerTemperature_Object = MibTableColumn
hwInfoPowerTemperature = _HwInfoPowerTemperature_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 4, 1, 4),
    _HwInfoPowerTemperature_Type()
)
hwInfoPowerTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPowerTemperature.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoPowerTemperature.setUnits("Degrees Celsius")
_HwInfoPowerVendor_Type = OctetString
_HwInfoPowerVendor_Object = MibTableColumn
hwInfoPowerVendor = _HwInfoPowerVendor_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 4, 1, 5),
    _HwInfoPowerVendor_Type()
)
hwInfoPowerVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPowerVendor.setStatus("current")
_HwInfoPowerModle_Type = OctetString
_HwInfoPowerModle_Object = MibTableColumn
hwInfoPowerModle = _HwInfoPowerModle_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 4, 1, 6),
    _HwInfoPowerModle_Type()
)
hwInfoPowerModle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPowerModle.setStatus("current")
_HwInfoPowerVersion_Type = OctetString
_HwInfoPowerVersion_Object = MibTableColumn
hwInfoPowerVersion = _HwInfoPowerVersion_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 4, 1, 7),
    _HwInfoPowerVersion_Type()
)
hwInfoPowerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPowerVersion.setStatus("current")
_HwInfoPowerDate_Type = OctetString
_HwInfoPowerDate_Object = MibTableColumn
hwInfoPowerDate = _HwInfoPowerDate_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 4, 1, 8),
    _HwInfoPowerDate_Type()
)
hwInfoPowerDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPowerDate.setStatus("current")
_HwInfoPowerType_Type = Unsigned32
_HwInfoPowerType_Object = MibTableColumn
hwInfoPowerType = _HwInfoPowerType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 4, 1, 9),
    _HwInfoPowerType_Type()
)
hwInfoPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPowerType.setStatus("current")
_HwInfoPowerSN_Type = OctetString
_HwInfoPowerSN_Object = MibTableColumn
hwInfoPowerSN = _HwInfoPowerSN_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 4, 1, 10),
    _HwInfoPowerSN_Type()
)
hwInfoPowerSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPowerSN.setStatus("current")
_HwInfoPowerDisplayID_Type = OctetString
_HwInfoPowerDisplayID_Object = MibTableColumn
hwInfoPowerDisplayID = _HwInfoPowerDisplayID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 4, 1, 11),
    _HwInfoPowerDisplayID_Type()
)
hwInfoPowerDisplayID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPowerDisplayID.setStatus("current")
_HwInfoPowerDescription_Type = OctetString
_HwInfoPowerDescription_Object = MibTableColumn
hwInfoPowerDescription = _HwInfoPowerDescription_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 4, 1, 12),
    _HwInfoPowerDescription_Type()
)
hwInfoPowerDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPowerDescription.setStatus("current")
_HwInfoBBUTable_Object = MibTable
hwInfoBBUTable = _HwInfoBBUTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 5)
)
if mibBuilder.loadTexts:
    hwInfoBBUTable.setStatus("current")
_HwInfoBBUEntry_Object = MibTableRow
hwInfoBBUEntry = _HwInfoBBUEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 5, 1)
)
hwInfoBBUEntry.setIndexNames(
    (0, "ISM-MIB", "hwInfoBBUID"),
    (0, "ISM-MIB", "hwInfoBBUControllerID"),
)
if mibBuilder.loadTexts:
    hwInfoBBUEntry.setStatus("current")
_HwInfoBBUID_Type = Unsigned32
_HwInfoBBUID_Object = MibTableColumn
hwInfoBBUID = _HwInfoBBUID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 5, 1, 1),
    _HwInfoBBUID_Type()
)
hwInfoBBUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoBBUID.setStatus("current")
_HwInfoBBUControllerID_Type = Unsigned32
_HwInfoBBUControllerID_Object = MibTableColumn
hwInfoBBUControllerID = _HwInfoBBUControllerID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 5, 1, 2),
    _HwInfoBBUControllerID_Type()
)
hwInfoBBUControllerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoBBUControllerID.setStatus("current")
_HwInfoBBUPresentStatus_Type = Unsigned32
_HwInfoBBUPresentStatus_Object = MibTableColumn
hwInfoBBUPresentStatus = _HwInfoBBUPresentStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 5, 1, 3),
    _HwInfoBBUPresentStatus_Type()
)
hwInfoBBUPresentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoBBUPresentStatus.setStatus("current")
_HwInfoBBUStatus_Type = Unsigned32
_HwInfoBBUStatus_Object = MibTableColumn
hwInfoBBUStatus = _HwInfoBBUStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 5, 1, 4),
    _HwInfoBBUStatus_Type()
)
hwInfoBBUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoBBUStatus.setStatus("current")
_HwInfoBBUCurrentVoltage_Type = Unsigned32
_HwInfoBBUCurrentVoltage_Object = MibTableColumn
hwInfoBBUCurrentVoltage = _HwInfoBBUCurrentVoltage_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 5, 1, 5),
    _HwInfoBBUCurrentVoltage_Type()
)
hwInfoBBUCurrentVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoBBUCurrentVoltage.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoBBUCurrentVoltage.setUnits("0.1V")
_HwInfoBBUIsChargeFull_Type = Unsigned32
_HwInfoBBUIsChargeFull_Object = MibTableColumn
hwInfoBBUIsChargeFull = _HwInfoBBUIsChargeFull_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 5, 1, 6),
    _HwInfoBBUIsChargeFull_Type()
)
hwInfoBBUIsChargeFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoBBUIsChargeFull.setStatus("current")
_HwInfoBBUDischargeTime_Type = Unsigned32
_HwInfoBBUDischargeTime_Object = MibTableColumn
hwInfoBBUDischargeTime = _HwInfoBBUDischargeTime_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 5, 1, 7),
    _HwInfoBBUDischargeTime_Type()
)
hwInfoBBUDischargeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoBBUDischargeTime.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoBBUDischargeTime.setUnits("number of times")
_HwInfoBBURemainLife_Type = Unsigned32
_HwInfoBBURemainLife_Object = MibTableColumn
hwInfoBBURemainLife = _HwInfoBBURemainLife_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 5, 1, 8),
    _HwInfoBBURemainLife_Type()
)
hwInfoBBURemainLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoBBURemainLife.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoBBURemainLife.setUnits("days")
_HwInfoBBUFWVersion_Type = OctetString
_HwInfoBBUFWVersion_Object = MibTableColumn
hwInfoBBUFWVersion = _HwInfoBBUFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 5, 1, 9),
    _HwInfoBBUFWVersion_Type()
)
hwInfoBBUFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoBBUFWVersion.setStatus("current")
_HwInfoBBUELable_Type = OctetString
_HwInfoBBUELable_Object = MibTableColumn
hwInfoBBUELable = _HwInfoBBUELable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 5, 1, 10),
    _HwInfoBBUELable_Type()
)
hwInfoBBUELable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoBBUELable.setStatus("current")
_HwInfoBBUChargeState_Type = Unsigned32
_HwInfoBBUChargeState_Object = MibTableColumn
hwInfoBBUChargeState = _HwInfoBBUChargeState_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 5, 1, 11),
    _HwInfoBBUChargeState_Type()
)
hwInfoBBUChargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoBBUChargeState.setStatus("current")
_HwInfoFanTable_Object = MibTable
hwInfoFanTable = _HwInfoFanTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 6)
)
if mibBuilder.loadTexts:
    hwInfoFanTable.setStatus("current")
_HwInfoFanEntry_Object = MibTableRow
hwInfoFanEntry = _HwInfoFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 6, 1)
)
hwInfoFanEntry.setIndexNames(
    (0, "ISM-MIB", "hwInfoFanID"),
    (0, "ISM-MIB", "hwInfoFanSubrackId"),
)
if mibBuilder.loadTexts:
    hwInfoFanEntry.setStatus("current")
_HwInfoFanID_Type = Unsigned32
_HwInfoFanID_Object = MibTableColumn
hwInfoFanID = _HwInfoFanID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 6, 1, 1),
    _HwInfoFanID_Type()
)
hwInfoFanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFanID.setStatus("current")
_HwInfoFanSubrackId_Type = Unsigned32
_HwInfoFanSubrackId_Object = MibTableColumn
hwInfoFanSubrackId = _HwInfoFanSubrackId_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 6, 1, 2),
    _HwInfoFanSubrackId_Type()
)
hwInfoFanSubrackId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFanSubrackId.setStatus("current")
_HwInfoFanRunningStatus_Type = Unsigned32
_HwInfoFanRunningStatus_Object = MibTableColumn
hwInfoFanRunningStatus = _HwInfoFanRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 6, 1, 3),
    _HwInfoFanRunningStatus_Type()
)
hwInfoFanRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFanRunningStatus.setStatus("current")
_HwInfoFanRunningLevel_Type = Unsigned32
_HwInfoFanRunningLevel_Object = MibTableColumn
hwInfoFanRunningLevel = _HwInfoFanRunningLevel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 6, 1, 4),
    _HwInfoFanRunningLevel_Type()
)
hwInfoFanRunningLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFanRunningLevel.setStatus("current")
_HwInfoFanRunningSection_Type = Unsigned32
_HwInfoFanRunningSection_Object = MibTableColumn
hwInfoFanRunningSection = _HwInfoFanRunningSection_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 6, 1, 5),
    _HwInfoFanRunningSection_Type()
)
hwInfoFanRunningSection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFanRunningSection.setStatus("current")
_HwInfoFanELable_Type = OctetString
_HwInfoFanELable_Object = MibTableColumn
hwInfoFanELable = _HwInfoFanELable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 6, 1, 6),
    _HwInfoFanELable_Type()
)
hwInfoFanELable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFanELable.setStatus("current")
_HwInfoFanDescription_Type = OctetString
_HwInfoFanDescription_Object = MibTableColumn
hwInfoFanDescription = _HwInfoFanDescription_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 6, 1, 7),
    _HwInfoFanDescription_Type()
)
hwInfoFanDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFanDescription.setStatus("current")
_HwInfoExpBoardTable_Object = MibTable
hwInfoExpBoardTable = _HwInfoExpBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 7)
)
if mibBuilder.loadTexts:
    hwInfoExpBoardTable.setStatus("current")
_HwInfoExpBoardEntry_Object = MibTableRow
hwInfoExpBoardEntry = _HwInfoExpBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 7, 1)
)
hwInfoExpBoardEntry.setIndexNames(
    (0, "ISM-MIB", "hwInfoExpBoardID"),
    (0, "ISM-MIB", "hwInfoExpBoardSubrackID"),
)
if mibBuilder.loadTexts:
    hwInfoExpBoardEntry.setStatus("current")
_HwInfoExpBoardSubrackID_Type = Unsigned32
_HwInfoExpBoardSubrackID_Object = MibTableColumn
hwInfoExpBoardSubrackID = _HwInfoExpBoardSubrackID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 7, 1, 1),
    _HwInfoExpBoardSubrackID_Type()
)
hwInfoExpBoardSubrackID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoExpBoardSubrackID.setStatus("current")
_HwInfoExpBoardID_Type = Unsigned32
_HwInfoExpBoardID_Object = MibTableColumn
hwInfoExpBoardID = _HwInfoExpBoardID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 7, 1, 2),
    _HwInfoExpBoardID_Type()
)
hwInfoExpBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoExpBoardID.setStatus("current")
_HwInfoExpBoardStatus_Type = Unsigned32
_HwInfoExpBoardStatus_Object = MibTableColumn
hwInfoExpBoardStatus = _HwInfoExpBoardStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 7, 1, 3),
    _HwInfoExpBoardStatus_Type()
)
hwInfoExpBoardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoExpBoardStatus.setStatus("current")
_HwInfoExpBoardLogicVersion_Type = OctetString
_HwInfoExpBoardLogicVersion_Object = MibTableColumn
hwInfoExpBoardLogicVersion = _HwInfoExpBoardLogicVersion_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 7, 1, 4),
    _HwInfoExpBoardLogicVersion_Type()
)
hwInfoExpBoardLogicVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoExpBoardLogicVersion.setStatus("current")
_HwInfoExpBoardPCBversion_Type = OctetString
_HwInfoExpBoardPCBversion_Object = MibTableColumn
hwInfoExpBoardPCBversion = _HwInfoExpBoardPCBversion_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 7, 1, 5),
    _HwInfoExpBoardPCBversion_Type()
)
hwInfoExpBoardPCBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoExpBoardPCBversion.setStatus("current")
_HwInfoExpBoardProduceInfo_Type = OctetString
_HwInfoExpBoardProduceInfo_Object = MibTableColumn
hwInfoExpBoardProduceInfo = _HwInfoExpBoardProduceInfo_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 7, 1, 6),
    _HwInfoExpBoardProduceInfo_Type()
)
hwInfoExpBoardProduceInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoExpBoardProduceInfo.setStatus("current")
_HwInfoExpBoardType_Type = Unsigned32
_HwInfoExpBoardType_Object = MibTableColumn
hwInfoExpBoardType = _HwInfoExpBoardType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 7, 1, 7),
    _HwInfoExpBoardType_Type()
)
hwInfoExpBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoExpBoardType.setStatus("current")
_HwInfoInterfaceTable_Object = MibTable
hwInfoInterfaceTable = _HwInfoInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 8)
)
if mibBuilder.loadTexts:
    hwInfoInterfaceTable.setStatus("current")
_HwInfoInterfaceEntry_Object = MibTableRow
hwInfoInterfaceEntry = _HwInfoInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 8, 1)
)
hwInfoInterfaceEntry.setIndexNames(
    (0, "ISM-MIB", "hwInfoInterfaceID"),
    (0, "ISM-MIB", "hwInfoInterfaceControllerID"),
)
if mibBuilder.loadTexts:
    hwInfoInterfaceEntry.setStatus("current")
_HwInfoInterfaceID_Type = Unsigned32
_HwInfoInterfaceID_Object = MibTableColumn
hwInfoInterfaceID = _HwInfoInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 8, 1, 1),
    _HwInfoInterfaceID_Type()
)
hwInfoInterfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoInterfaceID.setStatus("current")
_HwInfoInterfaceControllerID_Type = Unsigned32
_HwInfoInterfaceControllerID_Object = MibTableColumn
hwInfoInterfaceControllerID = _HwInfoInterfaceControllerID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 8, 1, 2),
    _HwInfoInterfaceControllerID_Type()
)
hwInfoInterfaceControllerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoInterfaceControllerID.setStatus("current")
_HwInfoInterfaceType_Type = Unsigned32
_HwInfoInterfaceType_Object = MibTableColumn
hwInfoInterfaceType = _HwInfoInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 8, 1, 3),
    _HwInfoInterfaceType_Type()
)
hwInfoInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoInterfaceType.setStatus("current")
_HwInfoInterfaceStatus_Type = Unsigned32
_HwInfoInterfaceStatus_Object = MibTableColumn
hwInfoInterfaceStatus = _HwInfoInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 8, 1, 4),
    _HwInfoInterfaceStatus_Type()
)
hwInfoInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoInterfaceStatus.setStatus("current")
_HwInfoInterfaceLogicVersion_Type = OctetString
_HwInfoInterfaceLogicVersion_Object = MibTableColumn
hwInfoInterfaceLogicVersion = _HwInfoInterfaceLogicVersion_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 8, 1, 5),
    _HwInfoInterfaceLogicVersion_Type()
)
hwInfoInterfaceLogicVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoInterfaceLogicVersion.setStatus("current")
_HwInfoInterfacePCBVersion_Type = OctetString
_HwInfoInterfacePCBVersion_Object = MibTableColumn
hwInfoInterfacePCBVersion = _HwInfoInterfacePCBVersion_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 8, 1, 6),
    _HwInfoInterfacePCBVersion_Type()
)
hwInfoInterfacePCBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoInterfacePCBVersion.setStatus("current")
_HwInfoInterfaceVendorInfo_Type = OctetString
_HwInfoInterfaceVendorInfo_Object = MibTableColumn
hwInfoInterfaceVendorInfo = _HwInfoInterfaceVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 8, 1, 7),
    _HwInfoInterfaceVendorInfo_Type()
)
hwInfoInterfaceVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoInterfaceVendorInfo.setStatus("current")
_HwInfoInterfaceDescription_Type = OctetString
_HwInfoInterfaceDescription_Object = MibTableColumn
hwInfoInterfaceDescription = _HwInfoInterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 8, 1, 8),
    _HwInfoInterfaceDescription_Type()
)
hwInfoInterfaceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoInterfaceDescription.setStatus("current")
_HwInfoRAIDTable_Object = MibTable
hwInfoRAIDTable = _HwInfoRAIDTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 9)
)
if mibBuilder.loadTexts:
    hwInfoRAIDTable.setStatus("current")
_HwInfoRAIDEntry_Object = MibTableRow
hwInfoRAIDEntry = _HwInfoRAIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 9, 1)
)
hwInfoRAIDEntry.setIndexNames(
    (0, "ISM-MIB", "hwInfoRAIDID"),
)
if mibBuilder.loadTexts:
    hwInfoRAIDEntry.setStatus("current")
_HwInfoRAIDID_Type = Unsigned32
_HwInfoRAIDID_Object = MibTableColumn
hwInfoRAIDID = _HwInfoRAIDID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 9, 1, 1),
    _HwInfoRAIDID_Type()
)
hwInfoRAIDID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoRAIDID.setStatus("current")
_HwInfoRAIDName_Type = OctetString
_HwInfoRAIDName_Object = MibTableColumn
hwInfoRAIDName = _HwInfoRAIDName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 9, 1, 2),
    _HwInfoRAIDName_Type()
)
hwInfoRAIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoRAIDName.setStatus("current")
_HwInfoRAIDLevel_Type = Unsigned32
_HwInfoRAIDLevel_Object = MibTableColumn
hwInfoRAIDLevel = _HwInfoRAIDLevel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 9, 1, 3),
    _HwInfoRAIDLevel_Type()
)
hwInfoRAIDLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoRAIDLevel.setStatus("current")
_HwInfoRAIDFreeCapacity_Type = Unsigned32
_HwInfoRAIDFreeCapacity_Object = MibTableColumn
hwInfoRAIDFreeCapacity = _HwInfoRAIDFreeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 9, 1, 4),
    _HwInfoRAIDFreeCapacity_Type()
)
hwInfoRAIDFreeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoRAIDFreeCapacity.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoRAIDFreeCapacity.setUnits("MB")
_HwInfoRAIDStatus_Type = Unsigned32
_HwInfoRAIDStatus_Object = MibTableColumn
hwInfoRAIDStatus = _HwInfoRAIDStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 9, 1, 5),
    _HwInfoRAIDStatus_Type()
)
hwInfoRAIDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoRAIDStatus.setStatus("current")
_HwInfoRAIDDiskList_Type = OctetString
_HwInfoRAIDDiskList_Object = MibTableColumn
hwInfoRAIDDiskList = _HwInfoRAIDDiskList_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 9, 1, 6),
    _HwInfoRAIDDiskList_Type()
)
hwInfoRAIDDiskList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoRAIDDiskList.setStatus("current")
_HwInfoRAIDTotalSize_Type = Unsigned32
_HwInfoRAIDTotalSize_Object = MibTableColumn
hwInfoRAIDTotalSize = _HwInfoRAIDTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 9, 1, 7),
    _HwInfoRAIDTotalSize_Type()
)
hwInfoRAIDTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoRAIDTotalSize.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoRAIDTotalSize.setUnits("MB")
_HwInfoCacheTable_Object = MibTable
hwInfoCacheTable = _HwInfoCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 10)
)
if mibBuilder.loadTexts:
    hwInfoCacheTable.setStatus("current")
_HwInfoCacheEntry_Object = MibTableRow
hwInfoCacheEntry = _HwInfoCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 10, 1)
)
hwInfoCacheEntry.setIndexNames(
    (0, "ISM-MIB", "hwInfoCacheID"),
)
if mibBuilder.loadTexts:
    hwInfoCacheEntry.setStatus("current")
_HwInfoCacheID_Type = Unsigned32
_HwInfoCacheID_Object = MibTableColumn
hwInfoCacheID = _HwInfoCacheID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 10, 1, 1),
    _HwInfoCacheID_Type()
)
hwInfoCacheID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoCacheID.setStatus("current")
_HwInfoCacheTotalMemoryCapacity_Type = Unsigned32
_HwInfoCacheTotalMemoryCapacity_Object = MibTableColumn
hwInfoCacheTotalMemoryCapacity = _HwInfoCacheTotalMemoryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 10, 1, 2),
    _HwInfoCacheTotalMemoryCapacity_Type()
)
hwInfoCacheTotalMemoryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoCacheTotalMemoryCapacity.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoCacheTotalMemoryCapacity.setUnits("MB")
_HwInfoCacheSystemMemoryCapacity_Type = Unsigned32
_HwInfoCacheSystemMemoryCapacity_Object = MibTableColumn
hwInfoCacheSystemMemoryCapacity = _HwInfoCacheSystemMemoryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 10, 1, 3),
    _HwInfoCacheSystemMemoryCapacity_Type()
)
hwInfoCacheSystemMemoryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoCacheSystemMemoryCapacity.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoCacheSystemMemoryCapacity.setUnits("MB")
_HwInfoCacheCacheCapacity_Type = Unsigned32
_HwInfoCacheCacheCapacity_Object = MibTableColumn
hwInfoCacheCacheCapacity = _HwInfoCacheCacheCapacity_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 10, 1, 4),
    _HwInfoCacheCacheCapacity_Type()
)
hwInfoCacheCacheCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoCacheCacheCapacity.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoCacheCacheCapacity.setUnits("MB")
_HwInfoCacheCacheUtilization_Type = Unsigned32
_HwInfoCacheCacheUtilization_Object = MibTableColumn
hwInfoCacheCacheUtilization = _HwInfoCacheCacheUtilization_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 10, 1, 5),
    _HwInfoCacheCacheUtilization_Type()
)
hwInfoCacheCacheUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoCacheCacheUtilization.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoCacheCacheUtilization.setUnits("%")
_HwInfoCacheCacheHitRatio_Type = Unsigned32
_HwInfoCacheCacheHitRatio_Object = MibTableColumn
hwInfoCacheCacheHitRatio = _HwInfoCacheCacheHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 10, 1, 6),
    _HwInfoCacheCacheHitRatio_Type()
)
hwInfoCacheCacheHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoCacheCacheHitRatio.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoCacheCacheHitRatio.setUnits("%")
_HwInfoCacheCurrentCacheWaterLevel_Type = Unsigned32
_HwInfoCacheCurrentCacheWaterLevel_Object = MibTableColumn
hwInfoCacheCurrentCacheWaterLevel = _HwInfoCacheCurrentCacheWaterLevel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 10, 1, 7),
    _HwInfoCacheCurrentCacheWaterLevel_Type()
)
hwInfoCacheCurrentCacheWaterLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoCacheCurrentCacheWaterLevel.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoCacheCurrentCacheWaterLevel.setUnits("%")
_HwInfoCacheCacheHighWaterLevel_Type = Unsigned32
_HwInfoCacheCacheHighWaterLevel_Object = MibTableColumn
hwInfoCacheCacheHighWaterLevel = _HwInfoCacheCacheHighWaterLevel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 10, 1, 8),
    _HwInfoCacheCacheHighWaterLevel_Type()
)
hwInfoCacheCacheHighWaterLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoCacheCacheHighWaterLevel.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoCacheCacheHighWaterLevel.setUnits("%")
_HwInfoCacheCacheLowWaterLevel_Type = Unsigned32
_HwInfoCacheCacheLowWaterLevel_Object = MibTableColumn
hwInfoCacheCacheLowWaterLevel = _HwInfoCacheCacheLowWaterLevel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 10, 1, 9),
    _HwInfoCacheCacheLowWaterLevel_Type()
)
hwInfoCacheCacheLowWaterLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoCacheCacheLowWaterLevel.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoCacheCacheLowWaterLevel.setUnits("%")
_HwInfoCacheReadCacheUtility_Type = Unsigned32
_HwInfoCacheReadCacheUtility_Object = MibTableColumn
hwInfoCacheReadCacheUtility = _HwInfoCacheReadCacheUtility_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 10, 1, 10),
    _HwInfoCacheReadCacheUtility_Type()
)
hwInfoCacheReadCacheUtility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoCacheReadCacheUtility.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoCacheReadCacheUtility.setUnits("%")
_HwInfoCacheWriteCacheUtililty_Type = Unsigned32
_HwInfoCacheWriteCacheUtililty_Object = MibTableColumn
hwInfoCacheWriteCacheUtililty = _HwInfoCacheWriteCacheUtililty_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 10, 1, 11),
    _HwInfoCacheWriteCacheUtililty_Type()
)
hwInfoCacheWriteCacheUtililty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoCacheWriteCacheUtililty.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoCacheWriteCacheUtililty.setUnits("%")
_HwInfoCacheMirroringWriteCacheUtility_Type = Unsigned32
_HwInfoCacheMirroringWriteCacheUtility_Object = MibTableColumn
hwInfoCacheMirroringWriteCacheUtility = _HwInfoCacheMirroringWriteCacheUtility_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 10, 1, 12),
    _HwInfoCacheMirroringWriteCacheUtility_Type()
)
hwInfoCacheMirroringWriteCacheUtility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoCacheMirroringWriteCacheUtility.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoCacheMirroringWriteCacheUtility.setUnits("%")
_HwInfoCacheWhetherDirtyDataExists_Type = Unsigned32
_HwInfoCacheWhetherDirtyDataExists_Object = MibTableColumn
hwInfoCacheWhetherDirtyDataExists = _HwInfoCacheWhetherDirtyDataExists_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 10, 1, 13),
    _HwInfoCacheWhetherDirtyDataExists_Type()
)
hwInfoCacheWhetherDirtyDataExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoCacheWhetherDirtyDataExists.setStatus("current")
_HwPerfRAIDTable_Object = MibTable
hwPerfRAIDTable = _HwPerfRAIDTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 11)
)
if mibBuilder.loadTexts:
    hwPerfRAIDTable.setStatus("current")
_HwPerfRAIDEntry_Object = MibTableRow
hwPerfRAIDEntry = _HwPerfRAIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 11, 1)
)
hwPerfRAIDEntry.setIndexNames(
    (0, "ISM-MIB", "hwPerfRAIDID"),
)
if mibBuilder.loadTexts:
    hwPerfRAIDEntry.setStatus("current")
_HwPerfRAIDID_Type = Unsigned32
_HwPerfRAIDID_Object = MibTableColumn
hwPerfRAIDID = _HwPerfRAIDID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 11, 1, 1),
    _HwPerfRAIDID_Type()
)
hwPerfRAIDID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfRAIDID.setStatus("current")
_HwPerfRAIDCurrentBandwidth_Type = Unsigned32
_HwPerfRAIDCurrentBandwidth_Object = MibTableColumn
hwPerfRAIDCurrentBandwidth = _HwPerfRAIDCurrentBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 11, 1, 2),
    _HwPerfRAIDCurrentBandwidth_Type()
)
hwPerfRAIDCurrentBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfRAIDCurrentBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwPerfRAIDCurrentBandwidth.setUnits("MB/s")
_HwPerfRAIDThroughput_Type = Unsigned32
_HwPerfRAIDThroughput_Object = MibTableColumn
hwPerfRAIDThroughput = _HwPerfRAIDThroughput_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 11, 1, 3),
    _HwPerfRAIDThroughput_Type()
)
hwPerfRAIDThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfRAIDThroughput.setStatus("current")
if mibBuilder.loadTexts:
    hwPerfRAIDThroughput.setUnits("IO/s")
_HwPerfRAIDReadBandwidth_Type = Unsigned32
_HwPerfRAIDReadBandwidth_Object = MibTableColumn
hwPerfRAIDReadBandwidth = _HwPerfRAIDReadBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 11, 1, 4),
    _HwPerfRAIDReadBandwidth_Type()
)
hwPerfRAIDReadBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfRAIDReadBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwPerfRAIDReadBandwidth.setUnits("MB/s")
_HwPerfRAIDReadThroughput_Type = Unsigned32
_HwPerfRAIDReadThroughput_Object = MibTableColumn
hwPerfRAIDReadThroughput = _HwPerfRAIDReadThroughput_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 11, 1, 5),
    _HwPerfRAIDReadThroughput_Type()
)
hwPerfRAIDReadThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfRAIDReadThroughput.setStatus("current")
if mibBuilder.loadTexts:
    hwPerfRAIDReadThroughput.setUnits("IO/s")
_HwPerfRAIDWriteBandwidth_Type = Unsigned32
_HwPerfRAIDWriteBandwidth_Object = MibTableColumn
hwPerfRAIDWriteBandwidth = _HwPerfRAIDWriteBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 11, 1, 6),
    _HwPerfRAIDWriteBandwidth_Type()
)
hwPerfRAIDWriteBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfRAIDWriteBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwPerfRAIDWriteBandwidth.setUnits("MB/s")
_HwPerfRAIDWriteThroughput_Type = Unsigned32
_HwPerfRAIDWriteThroughput_Object = MibTableColumn
hwPerfRAIDWriteThroughput = _HwPerfRAIDWriteThroughput_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 11, 1, 7),
    _HwPerfRAIDWriteThroughput_Type()
)
hwPerfRAIDWriteThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfRAIDWriteThroughput.setStatus("current")
if mibBuilder.loadTexts:
    hwPerfRAIDWriteThroughput.setUnits("IO/s")
_HwPerfControllerTable_Object = MibTable
hwPerfControllerTable = _HwPerfControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 12)
)
if mibBuilder.loadTexts:
    hwPerfControllerTable.setStatus("current")
_HwPerfControllerEntry_Object = MibTableRow
hwPerfControllerEntry = _HwPerfControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 12, 1)
)
hwPerfControllerEntry.setIndexNames(
    (0, "ISM-MIB", "hwPerfControllerID"),
)
if mibBuilder.loadTexts:
    hwPerfControllerEntry.setStatus("current")
_HwPerfControllerID_Type = Unsigned32
_HwPerfControllerID_Object = MibTableColumn
hwPerfControllerID = _HwPerfControllerID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 12, 1, 1),
    _HwPerfControllerID_Type()
)
hwPerfControllerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfControllerID.setStatus("current")
_HwPerfControllerCacheHit_Type = Unsigned32
_HwPerfControllerCacheHit_Object = MibTableColumn
hwPerfControllerCacheHit = _HwPerfControllerCacheHit_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 12, 1, 2),
    _HwPerfControllerCacheHit_Type()
)
hwPerfControllerCacheHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfControllerCacheHit.setStatus("current")
if mibBuilder.loadTexts:
    hwPerfControllerCacheHit.setUnits("%")
_HwPerfControllerThroughput_Type = Unsigned32
_HwPerfControllerThroughput_Object = MibTableColumn
hwPerfControllerThroughput = _HwPerfControllerThroughput_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 12, 1, 3),
    _HwPerfControllerThroughput_Type()
)
hwPerfControllerThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfControllerThroughput.setStatus("current")
if mibBuilder.loadTexts:
    hwPerfControllerThroughput.setUnits("IO/s")
_HwPerfControllerReadBandwidth_Type = Unsigned32
_HwPerfControllerReadBandwidth_Object = MibTableColumn
hwPerfControllerReadBandwidth = _HwPerfControllerReadBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 12, 1, 4),
    _HwPerfControllerReadBandwidth_Type()
)
hwPerfControllerReadBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfControllerReadBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwPerfControllerReadBandwidth.setUnits("MB/s")
_HwPerfControllerReadThroughput_Type = Unsigned32
_HwPerfControllerReadThroughput_Object = MibTableColumn
hwPerfControllerReadThroughput = _HwPerfControllerReadThroughput_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 12, 1, 5),
    _HwPerfControllerReadThroughput_Type()
)
hwPerfControllerReadThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfControllerReadThroughput.setStatus("current")
if mibBuilder.loadTexts:
    hwPerfControllerReadThroughput.setUnits("IO/s")
_HwPerfControllerWriteBandwidth_Type = Unsigned32
_HwPerfControllerWriteBandwidth_Object = MibTableColumn
hwPerfControllerWriteBandwidth = _HwPerfControllerWriteBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 12, 1, 6),
    _HwPerfControllerWriteBandwidth_Type()
)
hwPerfControllerWriteBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfControllerWriteBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwPerfControllerWriteBandwidth.setUnits("MB/s")
_HwPerfControllerWriteThroughput_Type = Unsigned32
_HwPerfControllerWriteThroughput_Object = MibTableColumn
hwPerfControllerWriteThroughput = _HwPerfControllerWriteThroughput_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 12, 1, 7),
    _HwPerfControllerWriteThroughput_Type()
)
hwPerfControllerWriteThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfControllerWriteThroughput.setStatus("current")
if mibBuilder.loadTexts:
    hwPerfControllerWriteThroughput.setUnits("IO/s")
_HwPerfControllerCPUUsage_Type = Unsigned32
_HwPerfControllerCPUUsage_Object = MibTableColumn
hwPerfControllerCPUUsage = _HwPerfControllerCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 12, 1, 8),
    _HwPerfControllerCPUUsage_Type()
)
hwPerfControllerCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfControllerCPUUsage.setStatus("current")
if mibBuilder.loadTexts:
    hwPerfControllerCPUUsage.setUnits("%")
_HwPerfControllerMemoryUsage_Type = Unsigned32
_HwPerfControllerMemoryUsage_Object = MibTableColumn
hwPerfControllerMemoryUsage = _HwPerfControllerMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 12, 1, 9),
    _HwPerfControllerMemoryUsage_Type()
)
hwPerfControllerMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfControllerMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    hwPerfControllerMemoryUsage.setUnits("%")
_HwPerfNASPortTable_Object = MibTable
hwPerfNASPortTable = _HwPerfNASPortTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 13)
)
if mibBuilder.loadTexts:
    hwPerfNASPortTable.setStatus("current")
_HwPerfNASPortEntry_Object = MibTableRow
hwPerfNASPortEntry = _HwPerfNASPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 13, 1)
)
hwPerfNASPortEntry.setIndexNames(
    (0, "ISM-MIB", "hwPerfNASPortIndex"),
)
if mibBuilder.loadTexts:
    hwPerfNASPortEntry.setStatus("current")
_HwPerfNASPortIndex_Type = Unsigned32
_HwPerfNASPortIndex_Object = MibTableColumn
hwPerfNASPortIndex = _HwPerfNASPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 13, 1, 1),
    _HwPerfNASPortIndex_Type()
)
hwPerfNASPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfNASPortIndex.setStatus("current")
_HwPerfNASPortCurrentBandwidth_Type = Unsigned32
_HwPerfNASPortCurrentBandwidth_Object = MibTableColumn
hwPerfNASPortCurrentBandwidth = _HwPerfNASPortCurrentBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 13, 1, 2),
    _HwPerfNASPortCurrentBandwidth_Type()
)
hwPerfNASPortCurrentBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfNASPortCurrentBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwPerfNASPortCurrentBandwidth.setUnits("MB/s")
_HwPerfNASPortReadBandwidth_Type = Unsigned32
_HwPerfNASPortReadBandwidth_Object = MibTableColumn
hwPerfNASPortReadBandwidth = _HwPerfNASPortReadBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 13, 1, 3),
    _HwPerfNASPortReadBandwidth_Type()
)
hwPerfNASPortReadBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfNASPortReadBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwPerfNASPortReadBandwidth.setUnits("MB/s")
_HwPerfNASPortWriteBandwidth_Type = Unsigned32
_HwPerfNASPortWriteBandwidth_Object = MibTableColumn
hwPerfNASPortWriteBandwidth = _HwPerfNASPortWriteBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 13, 1, 4),
    _HwPerfNASPortWriteBandwidth_Type()
)
hwPerfNASPortWriteBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfNASPortWriteBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwPerfNASPortWriteBandwidth.setUnits("MB/s")
_HwPerfNASPortTotalPackages_Type = Unsigned32
_HwPerfNASPortTotalPackages_Object = MibTableColumn
hwPerfNASPortTotalPackages = _HwPerfNASPortTotalPackages_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 13, 1, 5),
    _HwPerfNASPortTotalPackages_Type()
)
hwPerfNASPortTotalPackages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfNASPortTotalPackages.setStatus("current")
if mibBuilder.loadTexts:
    hwPerfNASPortTotalPackages.setUnits("Packets/s")
_HwPerfNASPortInboundPackages_Type = Unsigned32
_HwPerfNASPortInboundPackages_Object = MibTableColumn
hwPerfNASPortInboundPackages = _HwPerfNASPortInboundPackages_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 13, 1, 6),
    _HwPerfNASPortInboundPackages_Type()
)
hwPerfNASPortInboundPackages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfNASPortInboundPackages.setStatus("current")
if mibBuilder.loadTexts:
    hwPerfNASPortInboundPackages.setUnits("Packets/s")
_HwPerfNASPortOutboundPackages_Type = Unsigned32
_HwPerfNASPortOutboundPackages_Object = MibTableColumn
hwPerfNASPortOutboundPackages = _HwPerfNASPortOutboundPackages_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 13, 1, 7),
    _HwPerfNASPortOutboundPackages_Type()
)
hwPerfNASPortOutboundPackages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfNASPortOutboundPackages.setStatus("current")
if mibBuilder.loadTexts:
    hwPerfNASPortOutboundPackages.setUnits("Packets/s")
_HwPerfNASPortDescription_Type = OctetString
_HwPerfNASPortDescription_Object = MibTableColumn
hwPerfNASPortDescription = _HwPerfNASPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 13, 1, 8),
    _HwPerfNASPortDescription_Type()
)
hwPerfNASPortDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPerfNASPortDescription.setStatus("current")
_HwInfoControllerBoardTable_Object = MibTable
hwInfoControllerBoardTable = _HwInfoControllerBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 14)
)
if mibBuilder.loadTexts:
    hwInfoControllerBoardTable.setStatus("current")
_HwInfoControllerBoardEntry_Object = MibTableRow
hwInfoControllerBoardEntry = _HwInfoControllerBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 14, 1)
)
hwInfoControllerBoardEntry.setIndexNames(
    (0, "ISM-MIB", "hwInfoControllerBoardID"),
)
if mibBuilder.loadTexts:
    hwInfoControllerBoardEntry.setStatus("current")
_HwInfoControllerBoardID_Type = Unsigned32
_HwInfoControllerBoardID_Object = MibTableColumn
hwInfoControllerBoardID = _HwInfoControllerBoardID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 14, 1, 1),
    _HwInfoControllerBoardID_Type()
)
hwInfoControllerBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerBoardID.setStatus("current")
_HwInfoControllerBoardStatus_Type = Unsigned32
_HwInfoControllerBoardStatus_Object = MibTableColumn
hwInfoControllerBoardStatus = _HwInfoControllerBoardStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 14, 1, 2),
    _HwInfoControllerBoardStatus_Type()
)
hwInfoControllerBoardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerBoardStatus.setStatus("current")
_HwInfoControllerBoardLogicVer_Type = OctetString
_HwInfoControllerBoardLogicVer_Object = MibTableColumn
hwInfoControllerBoardLogicVer = _HwInfoControllerBoardLogicVer_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 14, 1, 3),
    _HwInfoControllerBoardLogicVer_Type()
)
hwInfoControllerBoardLogicVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerBoardLogicVer.setStatus("current")
_HwInfoControllerBoardPCBVer_Type = OctetString
_HwInfoControllerBoardPCBVer_Object = MibTableColumn
hwInfoControllerBoardPCBVer = _HwInfoControllerBoardPCBVer_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 14, 1, 4),
    _HwInfoControllerBoardPCBVer_Type()
)
hwInfoControllerBoardPCBVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerBoardPCBVer.setStatus("current")
_HwInfoControllerBoardBIOSVer_Type = OctetString
_HwInfoControllerBoardBIOSVer_Object = MibTableColumn
hwInfoControllerBoardBIOSVer = _HwInfoControllerBoardBIOSVer_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 14, 1, 5),
    _HwInfoControllerBoardBIOSVer_Type()
)
hwInfoControllerBoardBIOSVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerBoardBIOSVer.setStatus("current")
_HwInfoControllerBoardELabel_Type = OctetString
_HwInfoControllerBoardELabel_Object = MibTableColumn
hwInfoControllerBoardELabel = _HwInfoControllerBoardELabel_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 14, 1, 6),
    _HwInfoControllerBoardELabel_Type()
)
hwInfoControllerBoardELabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerBoardELabel.setStatus("current")
_HwInfoControllerBoardType_Type = Unsigned32
_HwInfoControllerBoardType_Object = MibTableColumn
hwInfoControllerBoardType = _HwInfoControllerBoardType_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 14, 1, 7),
    _HwInfoControllerBoardType_Type()
)
hwInfoControllerBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoControllerBoardType.setStatus("current")
_HwInfoFileSystemTable_Object = MibTable
hwInfoFileSystemTable = _HwInfoFileSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 15)
)
if mibBuilder.loadTexts:
    hwInfoFileSystemTable.setStatus("current")
_HwInfoFileSystemEntry_Object = MibTableRow
hwInfoFileSystemEntry = _HwInfoFileSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 15, 1)
)
hwInfoFileSystemEntry.setIndexNames(
    (0, "ISM-MIB", "hwInfoFileSystemName"),
)
if mibBuilder.loadTexts:
    hwInfoFileSystemEntry.setStatus("current")
_HwInfoFileSystemName_Type = OctetString
_HwInfoFileSystemName_Object = MibTableColumn
hwInfoFileSystemName = _HwInfoFileSystemName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 15, 1, 1),
    _HwInfoFileSystemName_Type()
)
hwInfoFileSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSystemName.setStatus("current")
_HwInfoFileSystemStatus_Type = OctetString
_HwInfoFileSystemStatus_Object = MibTableColumn
hwInfoFileSystemStatus = _HwInfoFileSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 15, 1, 2),
    _HwInfoFileSystemStatus_Type()
)
hwInfoFileSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSystemStatus.setStatus("current")
_HwInfoFileSystemSize_Type = OctetString
_HwInfoFileSystemSize_Object = MibTableColumn
hwInfoFileSystemSize = _HwInfoFileSystemSize_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 15, 1, 3),
    _HwInfoFileSystemSize_Type()
)
hwInfoFileSystemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSystemSize.setStatus("current")
_HwInfoFileSystemLayout_Type = OctetString
_HwInfoFileSystemLayout_Object = MibTableColumn
hwInfoFileSystemLayout = _HwInfoFileSystemLayout_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 15, 1, 4),
    _HwInfoFileSystemLayout_Type()
)
hwInfoFileSystemLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSystemLayout.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoFileSystemLayout.setUnits("Degrees Celsius")
_HwInfoFileSystemMirrors_Type = Unsigned32
_HwInfoFileSystemMirrors_Object = MibTableColumn
hwInfoFileSystemMirrors = _HwInfoFileSystemMirrors_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 15, 1, 5),
    _HwInfoFileSystemMirrors_Type()
)
hwInfoFileSystemMirrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSystemMirrors.setStatus("current")
_HwInfoFileSystemColumns_Type = Unsigned32
_HwInfoFileSystemColumns_Object = MibTableColumn
hwInfoFileSystemColumns = _HwInfoFileSystemColumns_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 15, 1, 6),
    _HwInfoFileSystemColumns_Type()
)
hwInfoFileSystemColumns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSystemColumns.setStatus("current")
_HwInfoFileSystemUsage_Type = OctetString
_HwInfoFileSystemUsage_Object = MibTableColumn
hwInfoFileSystemUsage = _HwInfoFileSystemUsage_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 15, 1, 7),
    _HwInfoFileSystemUsage_Type()
)
hwInfoFileSystemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSystemUsage.setStatus("current")
_HwInfoFileSystemNFSShared_Type = OctetString
_HwInfoFileSystemNFSShared_Object = MibTableColumn
hwInfoFileSystemNFSShared = _HwInfoFileSystemNFSShared_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 15, 1, 8),
    _HwInfoFileSystemNFSShared_Type()
)
hwInfoFileSystemNFSShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSystemNFSShared.setStatus("current")
_HwInfoFileSystemCIFSShared_Type = OctetString
_HwInfoFileSystemCIFSShared_Object = MibTableColumn
hwInfoFileSystemCIFSShared = _HwInfoFileSystemCIFSShared_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 15, 1, 9),
    _HwInfoFileSystemCIFSShared_Type()
)
hwInfoFileSystemCIFSShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSystemCIFSShared.setStatus("current")
_HwInfoFileSystemSecondaryTier_Type = OctetString
_HwInfoFileSystemSecondaryTier_Object = MibTableColumn
hwInfoFileSystemSecondaryTier = _HwInfoFileSystemSecondaryTier_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 15, 1, 10),
    _HwInfoFileSystemSecondaryTier_Type()
)
hwInfoFileSystemSecondaryTier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSystemSecondaryTier.setStatus("current")
_HwInfoFileSystemPoolList_Type = OctetString
_HwInfoFileSystemPoolList_Object = MibTableColumn
hwInfoFileSystemPoolList = _HwInfoFileSystemPoolList_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 15, 1, 11),
    _HwInfoFileSystemPoolList_Type()
)
hwInfoFileSystemPoolList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoFileSystemPoolList.setStatus("current")
_HwInfoClusterNodesTable_Object = MibTable
hwInfoClusterNodesTable = _HwInfoClusterNodesTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 16)
)
if mibBuilder.loadTexts:
    hwInfoClusterNodesTable.setStatus("current")
_HwInfoClusterNodesEntry_Object = MibTableRow
hwInfoClusterNodesEntry = _HwInfoClusterNodesEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 16, 1)
)
hwInfoClusterNodesEntry.setIndexNames(
    (0, "ISM-MIB", "hwInfoClusterNodesID"),
)
if mibBuilder.loadTexts:
    hwInfoClusterNodesEntry.setStatus("current")
_HwInfoClusterNodesID_Type = Unsigned32
_HwInfoClusterNodesID_Object = MibTableColumn
hwInfoClusterNodesID = _HwInfoClusterNodesID_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 16, 1, 1),
    _HwInfoClusterNodesID_Type()
)
hwInfoClusterNodesID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoClusterNodesID.setStatus("current")
_HwInfoClusterNodesName_Type = OctetString
_HwInfoClusterNodesName_Object = MibTableColumn
hwInfoClusterNodesName = _HwInfoClusterNodesName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 16, 1, 2),
    _HwInfoClusterNodesName_Type()
)
hwInfoClusterNodesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoClusterNodesName.setStatus("current")
_HwInfoClusterNodesIsMaster_Type = Unsigned32
_HwInfoClusterNodesIsMaster_Object = MibTableColumn
hwInfoClusterNodesIsMaster = _HwInfoClusterNodesIsMaster_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 16, 1, 3),
    _HwInfoClusterNodesIsMaster_Type()
)
hwInfoClusterNodesIsMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoClusterNodesIsMaster.setStatus("current")
_HwInfoClusterNodesStatus_Type = Unsigned32
_HwInfoClusterNodesStatus_Object = MibTableColumn
hwInfoClusterNodesStatus = _HwInfoClusterNodesStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 16, 1, 4),
    _HwInfoClusterNodesStatus_Type()
)
hwInfoClusterNodesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoClusterNodesStatus.setStatus("current")
_HwInfoClusterNodesRuningStatus_Type = Unsigned32
_HwInfoClusterNodesRuningStatus_Object = MibTableColumn
hwInfoClusterNodesRuningStatus = _HwInfoClusterNodesRuningStatus_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 16, 1, 5),
    _HwInfoClusterNodesRuningStatus_Type()
)
hwInfoClusterNodesRuningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoClusterNodesRuningStatus.setStatus("current")
if mibBuilder.loadTexts:
    hwInfoClusterNodesRuningStatus.setUnits("0.1V")
_HwInfoClusterNodesIP_Type = OctetString
_HwInfoClusterNodesIP_Object = MibTableColumn
hwInfoClusterNodesIP = _HwInfoClusterNodesIP_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 16, 1, 6),
    _HwInfoClusterNodesIP_Type()
)
hwInfoClusterNodesIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoClusterNodesIP.setStatus("current")
_HwInfoNasControllerTable_Object = MibTable
hwInfoNasControllerTable = _HwInfoNasControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 17)
)
if mibBuilder.loadTexts:
    hwInfoNasControllerTable.setStatus("current")
_HwInfoNasControllerEntry_Object = MibTableRow
hwInfoNasControllerEntry = _HwInfoNasControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 17, 1)
)
hwInfoNasControllerEntry.setIndexNames(
    (0, "ISM-MIB", "hwInfoNasControllerName"),
)
if mibBuilder.loadTexts:
    hwInfoNasControllerEntry.setStatus("current")
_HwInfoNasControllerName_Type = OctetString
_HwInfoNasControllerName_Object = MibTableColumn
hwInfoNasControllerName = _HwInfoNasControllerName_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 17, 1, 1),
    _HwInfoNasControllerName_Type()
)
hwInfoNasControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoNasControllerName.setStatus("current")
_HwInfoNasControllerBarCode_Type = OctetString
_HwInfoNasControllerBarCode_Object = MibTableColumn
hwInfoNasControllerBarCode = _HwInfoNasControllerBarCode_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 17, 1, 2),
    _HwInfoNasControllerBarCode_Type()
)
hwInfoNasControllerBarCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoNasControllerBarCode.setStatus("current")
_HwInfoNasControllerFirmwareVersion_Type = OctetString
_HwInfoNasControllerFirmwareVersion_Object = MibTableColumn
hwInfoNasControllerFirmwareVersion = _HwInfoNasControllerFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 17, 1, 3),
    _HwInfoNasControllerFirmwareVersion_Type()
)
hwInfoNasControllerFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoNasControllerFirmwareVersion.setStatus("current")
_HwInfoNasControllerDescription_Type = OctetString
_HwInfoNasControllerDescription_Object = MibTableColumn
hwInfoNasControllerDescription = _HwInfoNasControllerDescription_Object(
    (1, 3, 6, 1, 4, 1, 34774, 4, 1, 22, 17, 1, 4),
    _HwInfoNasControllerDescription_Type()
)
hwInfoNasControllerDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoNasControllerDescription.setStatus("current")
_IsoConformance_ObjectIdentity = ObjectIdentity
isoConformance = _IsoConformance_ObjectIdentity(
    (1, 6)
)
_IsoGroups_ObjectIdentity = ObjectIdentity
isoGroups = _IsoGroups_ObjectIdentity(
    (1, 6, 1)
)
_IsoCompliances_ObjectIdentity = ObjectIdentity
isoCompliances = _IsoCompliances_ObjectIdentity(
    (1, 6, 2)
)

# Managed Objects groups

currentObjectGroup = ObjectGroup(
    (1, 6, 1, 1)
)
currentObjectGroup.setObjects(
      *(("ISM-MIB", "hwInfoControllerBoardID"),
        ("ISM-MIB", "hwInfoControllerBoardType"),
        ("ISM-MIB", "hwInfoControllerBoardStatus"),
        ("ISM-MIB", "hwInfoControllerBoardLogicVer"),
        ("ISM-MIB", "hwInfoControllerBoardPCBVer"),
        ("ISM-MIB", "hwInfoControllerBoardBIOSVer"),
        ("ISM-MIB", "hwInfoControllerBoardELabel"),
        ("ISM-MIB", "hwPerfNASPortIndex"),
        ("ISM-MIB", "hwPerfNASPortCurrentBandwidth"),
        ("ISM-MIB", "hwPerfNASPortReadBandwidth"),
        ("ISM-MIB", "hwPerfNASPortWriteBandwidth"),
        ("ISM-MIB", "hwPerfNASPortTotalPackages"),
        ("ISM-MIB", "hwPerfNASPortInboundPackages"),
        ("ISM-MIB", "hwPerfNASPortOutboundPackages"),
        ("ISM-MIB", "hwInfoPhysicDiskFrameID"),
        ("ISM-MIB", "hwInfoPhysicDiskSlotID"),
        ("ISM-MIB", "hwInfoPhysicDiskStatus"),
        ("ISM-MIB", "hwInfoPhysicDiskSZType"),
        ("ISM-MIB", "hwInfoPhysicDiskSZVendor"),
        ("ISM-MIB", "hwInfoPhysicDiskSZModel"),
        ("ISM-MIB", "hwInfoPhysicDiskSZSerial"),
        ("ISM-MIB", "hwInfoPhysicDiskSZFirmware"),
        ("ISM-MIB", "hwInfoPhysicDiskSpinSpeed"),
        ("ISM-MIB", "hwInfoPhysicDiskCurrentSpeed"),
        ("ISM-MIB", "hwInfoPhysicDiskRawCapacity"),
        ("ISM-MIB", "hwInfoLogicDiskFrameID"),
        ("ISM-MIB", "hwInfoLogicDiskSlotID"),
        ("ISM-MIB", "hwInfoLogicDiskLogicStatus"),
        ("ISM-MIB", "hwInfoLogicDiskLogicType"),
        ("ISM-MIB", "hwInfoLogicDiskSize"),
        ("ISM-MIB", "hwInfoRAIDID"),
        ("ISM-MIB", "hwInfoRAIDName"),
        ("ISM-MIB", "hwInfoRAIDLevel"),
        ("ISM-MIB", "hwInfoRAIDFreeCapacity"),
        ("ISM-MIB", "hwInfoRAIDStatus"),
        ("ISM-MIB", "hwInfoRAIDDiskList"),
        ("ISM-MIB", "hwPerfRAIDID"),
        ("ISM-MIB", "hwPerfRAIDCurrentBandwidth"),
        ("ISM-MIB", "hwPerfRAIDThroughput"),
        ("ISM-MIB", "hwPerfRAIDReadBandwidth"),
        ("ISM-MIB", "hwPerfRAIDReadThroughput"),
        ("ISM-MIB", "hwPerfRAIDWriteBandwidth"),
        ("ISM-MIB", "hwPerfRAIDWriteThroughput"),
        ("ISM-MIB", "hwInfoFanRunningStatus"),
        ("ISM-MIB", "hwInfoFanRunningLevel"),
        ("ISM-MIB", "hwInfoFanRunningSection"),
        ("ISM-MIB", "hwInfoControllerIP"),
        ("ISM-MIB", "hwInfoControllerIsMaster"),
        ("ISM-MIB", "hwInfoControllerCpuUsingRatio"),
        ("ISM-MIB", "hwInfoControllerMemoryUsingRatio"),
        ("ISM-MIB", "hwInfoControllerVersion"),
        ("ISM-MIB", "hwInfoControllerStatus"),
        ("ISM-MIB", "hwInfoPowerSubrackID"),
        ("ISM-MIB", "hwInfoPowerTemperature"),
        ("ISM-MIB", "hwInfoPowerModle"),
        ("ISM-MIB", "hwInfoPowerVersion"),
        ("ISM-MIB", "hwInfoPowerDate"),
        ("ISM-MIB", "hwInfoPowerSN"),
        ("ISM-MIB", "hwInfoBBUControllerID"),
        ("ISM-MIB", "hwInfoBBUPresentStatus"),
        ("ISM-MIB", "hwInfoBBUIsChargeFull"),
        ("ISM-MIB", "hwInfoBBUDischargeTime"),
        ("ISM-MIB", "hwInfoBBURemainLife"),
        ("ISM-MIB", "hwInfoBBUFWVersion"),
        ("ISM-MIB", "hwInfoBBUELable"),
        ("ISM-MIB", "hwInfoBBUChargeState"),
        ("ISM-MIB", "hwInfoFanSubrackId"),
        ("ISM-MIB", "hwInfoExpBoardID"),
        ("ISM-MIB", "hwInfoExpBoardSubrackID"),
        ("ISM-MIB", "hwInfoExpBoardStatus"),
        ("ISM-MIB", "hwInfoExpBoardLogicVersion"),
        ("ISM-MIB", "hwInfoExpBoardPCBversion"),
        ("ISM-MIB", "hwInfoExpBoardProduceInfo"),
        ("ISM-MIB", "hwInfoExpBoardType"),
        ("ISM-MIB", "hwInfoInterfaceLogicVersion"),
        ("ISM-MIB", "hwInfoInterfacePCBVersion"),
        ("ISM-MIB", "hwInfoInterfaceVendorInfo"),
        ("ISM-MIB", "hwInfoControllerID"),
        ("ISM-MIB", "hwInfoPowerID"),
        ("ISM-MIB", "hwInfoPowerStatus"),
        ("ISM-MIB", "hwInfoPowerVendor"),
        ("ISM-MIB", "hwInfoPowerType"),
        ("ISM-MIB", "hwInfoBBUID"),
        ("ISM-MIB", "hwInfoBBUStatus"),
        ("ISM-MIB", "hwInfoBBUCurrentVoltage"),
        ("ISM-MIB", "hwInfoFanID"),
        ("ISM-MIB", "hwInfoInterfaceID"),
        ("ISM-MIB", "hwInfoInterfaceControllerID"),
        ("ISM-MIB", "hwInfoInterfaceType"),
        ("ISM-MIB", "hwInfoInterfaceStatus"),
        ("ISM-MIB", "hwPerfControllerID"),
        ("ISM-MIB", "hwPerfControllerCacheHit"),
        ("ISM-MIB", "hwPerfControllerThroughput"),
        ("ISM-MIB", "hwPerfControllerReadBandwidth"),
        ("ISM-MIB", "hwPerfControllerReadThroughput"),
        ("ISM-MIB", "hwPerfControllerWriteBandwidth"),
        ("ISM-MIB", "hwPerfControllerWriteThroughput"),
        ("ISM-MIB", "hwPerfControllerCPUUsage"),
        ("ISM-MIB", "hwInfoPowerDisplayID"),
        ("ISM-MIB", "hwInfoFanELable"),
        ("ISM-MIB", "hwInfoRAIDTotalSize"),
        ("ISM-MIB", "hwPerfNASPortDescription"),
        ("ISM-MIB", "hwInfoControllerDescription"),
        ("ISM-MIB", "hwInfoPowerDescription"),
        ("ISM-MIB", "hwInfoFanDescription"),
        ("ISM-MIB", "hwInfoInterfaceDescription"),
        ("ISM-MIB", "hwInfoFileSystemName"),
        ("ISM-MIB", "hwInfoFileSystemStatus"),
        ("ISM-MIB", "hwInfoFileSystemSize"),
        ("ISM-MIB", "hwInfoFileSystemLayout"),
        ("ISM-MIB", "hwInfoFileSystemMirrors"),
        ("ISM-MIB", "hwInfoFileSystemColumns"),
        ("ISM-MIB", "hwInfoFileSystemUsage"),
        ("ISM-MIB", "hwInfoFileSystemNFSShared"),
        ("ISM-MIB", "hwInfoFileSystemCIFSShared"),
        ("ISM-MIB", "hwInfoFileSystemSecondaryTier"),
        ("ISM-MIB", "hwInfoFileSystemPoolList"),
        ("ISM-MIB", "hwInfoClusterNodesID"),
        ("ISM-MIB", "hwInfoClusterNodesName"),
        ("ISM-MIB", "hwInfoClusterNodesIsMaster"),
        ("ISM-MIB", "hwInfoClusterNodesStatus"),
        ("ISM-MIB", "hwInfoClusterNodesRuningStatus"),
        ("ISM-MIB", "hwInfoClusterNodesIP"),
        ("ISM-MIB", "hwInfoNasControllerName"),
        ("ISM-MIB", "hwInfoNasControllerBarCode"),
        ("ISM-MIB", "hwInfoNasControllerFirmwareVersion"),
        ("ISM-MIB", "hwInfoNasControllerDescription"),
        ("ISM-MIB", "hwPerfControllerMemoryUsage"),
        ("ISM-MIB", "hwInfoCacheID"),
        ("ISM-MIB", "hwInfoCacheTotalMemoryCapacity"),
        ("ISM-MIB", "hwInfoCacheSystemMemoryCapacity"),
        ("ISM-MIB", "hwInfoCacheCacheCapacity"),
        ("ISM-MIB", "hwInfoCacheCacheUtilization"),
        ("ISM-MIB", "hwInfoCacheCacheHitRatio"),
        ("ISM-MIB", "hwInfoCacheCurrentCacheWaterLevel"),
        ("ISM-MIB", "hwInfoCacheCacheHighWaterLevel"),
        ("ISM-MIB", "hwInfoCacheCacheLowWaterLevel"),
        ("ISM-MIB", "hwInfoCacheReadCacheUtility"),
        ("ISM-MIB", "hwInfoCacheWriteCacheUtililty"),
        ("ISM-MIB", "hwInfoCacheMirroringWriteCacheUtility"),
        ("ISM-MIB", "hwInfoCacheWhetherDirtyDataExists"))
)
if mibBuilder.loadTexts:
    currentObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

basicCompliance = ModuleCompliance(
    (1, 6, 2, 1)
)
basicCompliance.setObjects(
    ("ISM-MIB", "currentObjectGroup")
)
if mibBuilder.loadTexts:
    basicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISM-MIB",
    **{"NodeCodeString": NodeCodeString,
       "huaweistorage": huaweistorage,
       "hwStorage": hwStorage,
       "hwISM": hwISM,
       "hwMIB": hwMIB,
       "hwInfoControllerTable": hwInfoControllerTable,
       "hwInfoControllerEntry": hwInfoControllerEntry,
       "hwInfoControllerID": hwInfoControllerID,
       "hwInfoControllerIP": hwInfoControllerIP,
       "hwInfoControllerIsMaster": hwInfoControllerIsMaster,
       "hwInfoControllerCpuUsingRatio": hwInfoControllerCpuUsingRatio,
       "hwInfoControllerMemoryUsingRatio": hwInfoControllerMemoryUsingRatio,
       "hwInfoControllerVersion": hwInfoControllerVersion,
       "hwInfoControllerStatus": hwInfoControllerStatus,
       "hwInfoControllerDescription": hwInfoControllerDescription,
       "hwInfoPhysicDiskTable": hwInfoPhysicDiskTable,
       "hwInfoPhysicDiskEntry": hwInfoPhysicDiskEntry,
       "hwInfoPhysicDiskFrameID": hwInfoPhysicDiskFrameID,
       "hwInfoPhysicDiskSlotID": hwInfoPhysicDiskSlotID,
       "hwInfoPhysicDiskStatus": hwInfoPhysicDiskStatus,
       "hwInfoPhysicDiskSZType": hwInfoPhysicDiskSZType,
       "hwInfoPhysicDiskSZVendor": hwInfoPhysicDiskSZVendor,
       "hwInfoPhysicDiskSZModel": hwInfoPhysicDiskSZModel,
       "hwInfoPhysicDiskSZSerial": hwInfoPhysicDiskSZSerial,
       "hwInfoPhysicDiskSZFirmware": hwInfoPhysicDiskSZFirmware,
       "hwInfoPhysicDiskSpinSpeed": hwInfoPhysicDiskSpinSpeed,
       "hwInfoPhysicDiskCurrentSpeed": hwInfoPhysicDiskCurrentSpeed,
       "hwInfoPhysicDiskRawCapacity": hwInfoPhysicDiskRawCapacity,
       "hwInfoLogicDiskTable": hwInfoLogicDiskTable,
       "hwInfoLogicDiskEntry": hwInfoLogicDiskEntry,
       "hwInfoLogicDiskFrameID": hwInfoLogicDiskFrameID,
       "hwInfoLogicDiskSlotID": hwInfoLogicDiskSlotID,
       "hwInfoLogicDiskLogicStatus": hwInfoLogicDiskLogicStatus,
       "hwInfoLogicDiskLogicType": hwInfoLogicDiskLogicType,
       "hwInfoLogicDiskSize": hwInfoLogicDiskSize,
       "hwInfoPowerTable": hwInfoPowerTable,
       "hwInfoPowerEntry": hwInfoPowerEntry,
       "hwInfoPowerID": hwInfoPowerID,
       "hwInfoPowerSubrackID": hwInfoPowerSubrackID,
       "hwInfoPowerStatus": hwInfoPowerStatus,
       "hwInfoPowerTemperature": hwInfoPowerTemperature,
       "hwInfoPowerVendor": hwInfoPowerVendor,
       "hwInfoPowerModle": hwInfoPowerModle,
       "hwInfoPowerVersion": hwInfoPowerVersion,
       "hwInfoPowerDate": hwInfoPowerDate,
       "hwInfoPowerType": hwInfoPowerType,
       "hwInfoPowerSN": hwInfoPowerSN,
       "hwInfoPowerDisplayID": hwInfoPowerDisplayID,
       "hwInfoPowerDescription": hwInfoPowerDescription,
       "hwInfoBBUTable": hwInfoBBUTable,
       "hwInfoBBUEntry": hwInfoBBUEntry,
       "hwInfoBBUID": hwInfoBBUID,
       "hwInfoBBUControllerID": hwInfoBBUControllerID,
       "hwInfoBBUPresentStatus": hwInfoBBUPresentStatus,
       "hwInfoBBUStatus": hwInfoBBUStatus,
       "hwInfoBBUCurrentVoltage": hwInfoBBUCurrentVoltage,
       "hwInfoBBUIsChargeFull": hwInfoBBUIsChargeFull,
       "hwInfoBBUDischargeTime": hwInfoBBUDischargeTime,
       "hwInfoBBURemainLife": hwInfoBBURemainLife,
       "hwInfoBBUFWVersion": hwInfoBBUFWVersion,
       "hwInfoBBUELable": hwInfoBBUELable,
       "hwInfoBBUChargeState": hwInfoBBUChargeState,
       "hwInfoFanTable": hwInfoFanTable,
       "hwInfoFanEntry": hwInfoFanEntry,
       "hwInfoFanID": hwInfoFanID,
       "hwInfoFanSubrackId": hwInfoFanSubrackId,
       "hwInfoFanRunningStatus": hwInfoFanRunningStatus,
       "hwInfoFanRunningLevel": hwInfoFanRunningLevel,
       "hwInfoFanRunningSection": hwInfoFanRunningSection,
       "hwInfoFanELable": hwInfoFanELable,
       "hwInfoFanDescription": hwInfoFanDescription,
       "hwInfoExpBoardTable": hwInfoExpBoardTable,
       "hwInfoExpBoardEntry": hwInfoExpBoardEntry,
       "hwInfoExpBoardSubrackID": hwInfoExpBoardSubrackID,
       "hwInfoExpBoardID": hwInfoExpBoardID,
       "hwInfoExpBoardStatus": hwInfoExpBoardStatus,
       "hwInfoExpBoardLogicVersion": hwInfoExpBoardLogicVersion,
       "hwInfoExpBoardPCBversion": hwInfoExpBoardPCBversion,
       "hwInfoExpBoardProduceInfo": hwInfoExpBoardProduceInfo,
       "hwInfoExpBoardType": hwInfoExpBoardType,
       "hwInfoInterfaceTable": hwInfoInterfaceTable,
       "hwInfoInterfaceEntry": hwInfoInterfaceEntry,
       "hwInfoInterfaceID": hwInfoInterfaceID,
       "hwInfoInterfaceControllerID": hwInfoInterfaceControllerID,
       "hwInfoInterfaceType": hwInfoInterfaceType,
       "hwInfoInterfaceStatus": hwInfoInterfaceStatus,
       "hwInfoInterfaceLogicVersion": hwInfoInterfaceLogicVersion,
       "hwInfoInterfacePCBVersion": hwInfoInterfacePCBVersion,
       "hwInfoInterfaceVendorInfo": hwInfoInterfaceVendorInfo,
       "hwInfoInterfaceDescription": hwInfoInterfaceDescription,
       "hwInfoRAIDTable": hwInfoRAIDTable,
       "hwInfoRAIDEntry": hwInfoRAIDEntry,
       "hwInfoRAIDID": hwInfoRAIDID,
       "hwInfoRAIDName": hwInfoRAIDName,
       "hwInfoRAIDLevel": hwInfoRAIDLevel,
       "hwInfoRAIDFreeCapacity": hwInfoRAIDFreeCapacity,
       "hwInfoRAIDStatus": hwInfoRAIDStatus,
       "hwInfoRAIDDiskList": hwInfoRAIDDiskList,
       "hwInfoRAIDTotalSize": hwInfoRAIDTotalSize,
       "hwInfoCacheTable": hwInfoCacheTable,
       "hwInfoCacheEntry": hwInfoCacheEntry,
       "hwInfoCacheID": hwInfoCacheID,
       "hwInfoCacheTotalMemoryCapacity": hwInfoCacheTotalMemoryCapacity,
       "hwInfoCacheSystemMemoryCapacity": hwInfoCacheSystemMemoryCapacity,
       "hwInfoCacheCacheCapacity": hwInfoCacheCacheCapacity,
       "hwInfoCacheCacheUtilization": hwInfoCacheCacheUtilization,
       "hwInfoCacheCacheHitRatio": hwInfoCacheCacheHitRatio,
       "hwInfoCacheCurrentCacheWaterLevel": hwInfoCacheCurrentCacheWaterLevel,
       "hwInfoCacheCacheHighWaterLevel": hwInfoCacheCacheHighWaterLevel,
       "hwInfoCacheCacheLowWaterLevel": hwInfoCacheCacheLowWaterLevel,
       "hwInfoCacheReadCacheUtility": hwInfoCacheReadCacheUtility,
       "hwInfoCacheWriteCacheUtililty": hwInfoCacheWriteCacheUtililty,
       "hwInfoCacheMirroringWriteCacheUtility": hwInfoCacheMirroringWriteCacheUtility,
       "hwInfoCacheWhetherDirtyDataExists": hwInfoCacheWhetherDirtyDataExists,
       "hwPerfRAIDTable": hwPerfRAIDTable,
       "hwPerfRAIDEntry": hwPerfRAIDEntry,
       "hwPerfRAIDID": hwPerfRAIDID,
       "hwPerfRAIDCurrentBandwidth": hwPerfRAIDCurrentBandwidth,
       "hwPerfRAIDThroughput": hwPerfRAIDThroughput,
       "hwPerfRAIDReadBandwidth": hwPerfRAIDReadBandwidth,
       "hwPerfRAIDReadThroughput": hwPerfRAIDReadThroughput,
       "hwPerfRAIDWriteBandwidth": hwPerfRAIDWriteBandwidth,
       "hwPerfRAIDWriteThroughput": hwPerfRAIDWriteThroughput,
       "hwPerfControllerTable": hwPerfControllerTable,
       "hwPerfControllerEntry": hwPerfControllerEntry,
       "hwPerfControllerID": hwPerfControllerID,
       "hwPerfControllerCacheHit": hwPerfControllerCacheHit,
       "hwPerfControllerThroughput": hwPerfControllerThroughput,
       "hwPerfControllerReadBandwidth": hwPerfControllerReadBandwidth,
       "hwPerfControllerReadThroughput": hwPerfControllerReadThroughput,
       "hwPerfControllerWriteBandwidth": hwPerfControllerWriteBandwidth,
       "hwPerfControllerWriteThroughput": hwPerfControllerWriteThroughput,
       "hwPerfControllerCPUUsage": hwPerfControllerCPUUsage,
       "hwPerfControllerMemoryUsage": hwPerfControllerMemoryUsage,
       "hwPerfNASPortTable": hwPerfNASPortTable,
       "hwPerfNASPortEntry": hwPerfNASPortEntry,
       "hwPerfNASPortIndex": hwPerfNASPortIndex,
       "hwPerfNASPortCurrentBandwidth": hwPerfNASPortCurrentBandwidth,
       "hwPerfNASPortReadBandwidth": hwPerfNASPortReadBandwidth,
       "hwPerfNASPortWriteBandwidth": hwPerfNASPortWriteBandwidth,
       "hwPerfNASPortTotalPackages": hwPerfNASPortTotalPackages,
       "hwPerfNASPortInboundPackages": hwPerfNASPortInboundPackages,
       "hwPerfNASPortOutboundPackages": hwPerfNASPortOutboundPackages,
       "hwPerfNASPortDescription": hwPerfNASPortDescription,
       "hwInfoControllerBoardTable": hwInfoControllerBoardTable,
       "hwInfoControllerBoardEntry": hwInfoControllerBoardEntry,
       "hwInfoControllerBoardID": hwInfoControllerBoardID,
       "hwInfoControllerBoardStatus": hwInfoControllerBoardStatus,
       "hwInfoControllerBoardLogicVer": hwInfoControllerBoardLogicVer,
       "hwInfoControllerBoardPCBVer": hwInfoControllerBoardPCBVer,
       "hwInfoControllerBoardBIOSVer": hwInfoControllerBoardBIOSVer,
       "hwInfoControllerBoardELabel": hwInfoControllerBoardELabel,
       "hwInfoControllerBoardType": hwInfoControllerBoardType,
       "hwInfoFileSystemTable": hwInfoFileSystemTable,
       "hwInfoFileSystemEntry": hwInfoFileSystemEntry,
       "hwInfoFileSystemName": hwInfoFileSystemName,
       "hwInfoFileSystemStatus": hwInfoFileSystemStatus,
       "hwInfoFileSystemSize": hwInfoFileSystemSize,
       "hwInfoFileSystemLayout": hwInfoFileSystemLayout,
       "hwInfoFileSystemMirrors": hwInfoFileSystemMirrors,
       "hwInfoFileSystemColumns": hwInfoFileSystemColumns,
       "hwInfoFileSystemUsage": hwInfoFileSystemUsage,
       "hwInfoFileSystemNFSShared": hwInfoFileSystemNFSShared,
       "hwInfoFileSystemCIFSShared": hwInfoFileSystemCIFSShared,
       "hwInfoFileSystemSecondaryTier": hwInfoFileSystemSecondaryTier,
       "hwInfoFileSystemPoolList": hwInfoFileSystemPoolList,
       "hwInfoClusterNodesTable": hwInfoClusterNodesTable,
       "hwInfoClusterNodesEntry": hwInfoClusterNodesEntry,
       "hwInfoClusterNodesID": hwInfoClusterNodesID,
       "hwInfoClusterNodesName": hwInfoClusterNodesName,
       "hwInfoClusterNodesIsMaster": hwInfoClusterNodesIsMaster,
       "hwInfoClusterNodesStatus": hwInfoClusterNodesStatus,
       "hwInfoClusterNodesRuningStatus": hwInfoClusterNodesRuningStatus,
       "hwInfoClusterNodesIP": hwInfoClusterNodesIP,
       "hwInfoNasControllerTable": hwInfoNasControllerTable,
       "hwInfoNasControllerEntry": hwInfoNasControllerEntry,
       "hwInfoNasControllerName": hwInfoNasControllerName,
       "hwInfoNasControllerBarCode": hwInfoNasControllerBarCode,
       "hwInfoNasControllerFirmwareVersion": hwInfoNasControllerFirmwareVersion,
       "hwInfoNasControllerDescription": hwInfoNasControllerDescription,
       "isoConformance": isoConformance,
       "isoGroups": isoGroups,
       "currentObjectGroup": currentObjectGroup,
       "isoCompliances": isoCompliances,
       "basicCompliance": basicCompliance}
)
