# SNMP MIB module (HUAWEI-LswTRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/HUAWEI-LswTRAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:18:08 2025
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

(lswCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "lswCommon")

(hwLswCoreIndex,
 hwLswCoreThreshold,
 hwLswCpuIndex,
 hwLswFrameIndex,
 hwLswSlotIndex,
 hwLswSubslotIndex) = mibBuilder.importSymbols(
    "HUAWEI-LSW-DEV-ADM-MIB",
    "hwLswCoreIndex",
    "hwLswCoreThreshold",
    "hwLswCpuIndex",
    "hwLswFrameIndex",
    "hwLswSlotIndex",
    "hwLswSubslotIndex")

(hwDevMFanNum,
 hwDevMFirstTrapTime,
 hwDevMPowerNum) = mibBuilder.importSymbols(
    "HUAWEI-LswDEVM-MIB",
    "hwDevMFanNum",
    "hwDevMFirstTrapTime",
    "hwDevMPowerNum")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

hwsLswTrapMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12)
)
if mibBuilder.loadTexts:
    hwsLswTrapMib.setRevisions(
        ("2017-12-05 00:00",
         "2017-07-17 00:00",
         "2017-06-24 00:00",
         "2017-01-12 00:00",
         "2011-11-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwsLswTRAPMibObject_ObjectIdentity = ObjectIdentity
hwsLswTRAPMibObject = _HwsLswTRAPMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1)
)
_HwNetworkHealthMonitorFailure_ObjectIdentity = ObjectIdentity
hwNetworkHealthMonitorFailure = _HwNetworkHealthMonitorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 98)
)
_HwNetworkHealthMonitorNormal_ObjectIdentity = ObjectIdentity
hwNetworkHealthMonitorNormal = _HwNetworkHealthMonitorNormal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 99)
)
_HwsLswTRAPMibInfor_ObjectIdentity = ObjectIdentity
hwsLswTRAPMibInfor = _HwsLswTRAPMibInfor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 2)
)


class _HwsLswTrapCpuCoreInfo_Type(SnmpAdminString):
    """Custom type hwsLswTrapCpuCoreInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwsLswTrapCpuCoreInfo_Type.__name__ = "SnmpAdminString"
_HwsLswTrapCpuCoreInfo_Object = MibScalar
hwsLswTrapCpuCoreInfo = _HwsLswTrapCpuCoreInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 2, 1),
    _HwsLswTrapCpuCoreInfo_Type()
)
hwsLswTrapCpuCoreInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwsLswTrapCpuCoreInfo.setStatus("current")


class _HwsLswTrapProcessCpuInfo_Type(SnmpAdminString):
    """Custom type hwsLswTrapProcessCpuInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwsLswTrapProcessCpuInfo_Type.__name__ = "SnmpAdminString"
_HwsLswTrapProcessCpuInfo_Object = MibScalar
hwsLswTrapProcessCpuInfo = _HwsLswTrapProcessCpuInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 2, 2),
    _HwsLswTrapProcessCpuInfo_Type()
)
hwsLswTrapProcessCpuInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwsLswTrapProcessCpuInfo.setStatus("current")


class _HwsLswTrapProcessMemoryInfo_Type(SnmpAdminString):
    """Custom type hwsLswTrapProcessMemoryInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwsLswTrapProcessMemoryInfo_Type.__name__ = "SnmpAdminString"
_HwsLswTrapProcessMemoryInfo_Object = MibScalar
hwsLswTrapProcessMemoryInfo = _HwsLswTrapProcessMemoryInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 2, 3),
    _HwsLswTrapProcessMemoryInfo_Type()
)
hwsLswTrapProcessMemoryInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwsLswTrapProcessMemoryInfo.setStatus("current")


class _HwsLswTrapSlubInfo_Type(SnmpAdminString):
    """Custom type hwsLswTrapSlubInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwsLswTrapSlubInfo_Type.__name__ = "SnmpAdminString"
_HwsLswTrapSlubInfo_Object = MibScalar
hwsLswTrapSlubInfo = _HwsLswTrapSlubInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 2, 4),
    _HwsLswTrapSlubInfo_Type()
)
hwsLswTrapSlubInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwsLswTrapSlubInfo.setStatus("current")


class _HwLswTrapCpuUsage_Type(SnmpAdminString):
    """Custom type hwLswTrapCpuUsage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwLswTrapCpuUsage_Type.__name__ = "SnmpAdminString"
_HwLswTrapCpuUsage_Object = MibScalar
hwLswTrapCpuUsage = _HwLswTrapCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 2, 5),
    _HwLswTrapCpuUsage_Type()
)
hwLswTrapCpuUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLswTrapCpuUsage.setStatus("current")


class _HwLswTrapCoreProcessInfo_Type(SnmpAdminString):
    """Custom type hwLswTrapCoreProcessInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwLswTrapCoreProcessInfo_Type.__name__ = "SnmpAdminString"
_HwLswTrapCoreProcessInfo_Object = MibScalar
hwLswTrapCoreProcessInfo = _HwLswTrapCoreProcessInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 2, 6),
    _HwLswTrapCoreProcessInfo_Type()
)
hwLswTrapCoreProcessInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLswTrapCoreProcessInfo.setStatus("current")
_HwLswCoreTrapUsage_Type = Unsigned32
_HwLswCoreTrapUsage_Object = MibScalar
hwLswCoreTrapUsage = _HwLswCoreTrapUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 2, 7),
    _HwLswCoreTrapUsage_Type()
)
hwLswCoreTrapUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLswCoreTrapUsage.setStatus("current")
_HwBoardAvailablePower_Type = Integer32
_HwBoardAvailablePower_Object = MibScalar
hwBoardAvailablePower = _HwBoardAvailablePower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 2, 8),
    _HwBoardAvailablePower_Type()
)
hwBoardAvailablePower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBoardAvailablePower.setStatus("current")
_HwBoardRequiredPower_Type = Integer32
_HwBoardRequiredPower_Object = MibScalar
hwBoardRequiredPower = _HwBoardRequiredPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 2, 9),
    _HwBoardRequiredPower_Type()
)
hwBoardRequiredPower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBoardRequiredPower.setStatus("current")
_HwsLswTRAPMibObjectV2_ObjectIdentity = ObjectIdentity
hwsLswTRAPMibObjectV2 = _HwsLswTRAPMibObjectV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 3)
)
_HwsLswTRAPMibObjectV2Prefix_ObjectIdentity = ObjectIdentity
hwsLswTRAPMibObjectV2Prefix = _HwsLswTRAPMibObjectV2Prefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 3, 0)
)

# Managed Objects groups


# Notification objects

powerfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 1)
)
powerfailure.setObjects(
      *(("HUAWEI-LswDEVM-MIB", "hwDevMPowerNum"),
        ("HUAWEI-LswDEVM-MIB", "hwDevMFirstTrapTime"))
)
if mibBuilder.loadTexts:
    powerfailure.setStatus(
        "current"
    )

hwPowerNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 2)
)
hwPowerNormal.setObjects(
      *(("HUAWEI-LswDEVM-MIB", "hwDevMPowerNum"),
        ("HUAWEI-LswDEVM-MIB", "hwDevMFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hwPowerNormal.setStatus(
        "current"
    )

hwMasterPowerNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 3)
)
hwMasterPowerNormal.setObjects(
    ("HUAWEI-LswDEVM-MIB", "hwDevMPowerNum")
)
if mibBuilder.loadTexts:
    hwMasterPowerNormal.setStatus(
        "current"
    )

hwSlavePowerNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 4)
)
hwSlavePowerNormal.setObjects(
    ("HUAWEI-LswDEVM-MIB", "hwDevMPowerNum")
)
if mibBuilder.loadTexts:
    hwSlavePowerNormal.setStatus(
        "current"
    )

hwPowerRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 5)
)
hwPowerRemoved.setObjects(
    ("HUAWEI-LswDEVM-MIB", "hwDevMPowerNum")
)
if mibBuilder.loadTexts:
    hwPowerRemoved.setStatus(
        "current"
    )

fanfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 6)
)
fanfailure.setObjects(
    ("HUAWEI-LswDEVM-MIB", "hwDevMFanNum")
)
if mibBuilder.loadTexts:
    fanfailure.setStatus(
        "current"
    )

hwFanNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 7)
)
hwFanNormal.setObjects(
    ("HUAWEI-LswDEVM-MIB", "hwDevMFanNum")
)
if mibBuilder.loadTexts:
    hwFanNormal.setStatus(
        "current"
    )

hwBoardRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 8)
)
hwBoardRemoved.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwBoardRemoved.setStatus(
        "current"
    )

hwBoardInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 9)
)
hwBoardInserted.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwBoardInserted.setStatus(
        "current"
    )

hwBoardFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 10)
)
hwBoardFailure.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwBoardFailure.setStatus(
        "current"
    )

hwBoardNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 11)
)
hwBoardNormal.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwBoardNormal.setStatus(
        "current"
    )

hwSubcardRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 12)
)
hwSubcardRemove.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSubslotIndex"))
)
if mibBuilder.loadTexts:
    hwSubcardRemove.setStatus(
        "current"
    )

hwSubcardInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 13)
)
hwSubcardInsert.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSubslotIndex"))
)
if mibBuilder.loadTexts:
    hwSubcardInsert.setStatus(
        "current"
    )

hwBoaardTemperatureLower = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 14)
)
hwBoaardTemperatureLower.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwBoaardTemperatureLower.setStatus(
        "current"
    )

hwBoaardTemperatureFromLowerToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 15)
)
hwBoaardTemperatureFromLowerToNormal.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwBoaardTemperatureFromLowerToNormal.setStatus(
        "current"
    )

hwBoaardTemperatureHigher = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 16)
)
hwBoaardTemperatureHigher.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwBoaardTemperatureHigher.setStatus(
        "current"
    )

hwBoaardTemperatureFormHigherToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 17)
)
hwBoaardTemperatureFormHigherToNormal.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwBoaardTemperatureFormHigherToNormal.setStatus(
        "current"
    )

hwRequestLoading = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 18)
)
hwRequestLoading.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwRequestLoading.setStatus(
        "current"
    )

hwLoadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 19)
)
hwLoadFailure.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwLoadFailure.setStatus(
        "current"
    )

hwLoadFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 20)
)
hwLoadFinished.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwLoadFinished.setStatus(
        "current"
    )

hwBackBoardModeSetFuilure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 21)
)
hwBackBoardModeSetFuilure.setObjects(
    ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex")
)
if mibBuilder.loadTexts:
    hwBackBoardModeSetFuilure.setStatus(
        "current"
    )

hwBackBoardModeSetOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 22)
)
hwBackBoardModeSetOK.setObjects(
    ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex")
)
if mibBuilder.loadTexts:
    hwBackBoardModeSetOK.setStatus(
        "current"
    )

hwPowerInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 23)
)
hwPowerInserted.setObjects(
    ("HUAWEI-LswDEVM-MIB", "hwDevMPowerNum")
)
if mibBuilder.loadTexts:
    hwPowerInserted.setStatus(
        "current"
    )

hwBootImageUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 24)
)
hwBootImageUpdated.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwBootImageUpdated.setStatus(
        "current"
    )

hwCpuRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 25)
)
hwCpuRemoved.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswCpuIndex"))
)
if mibBuilder.loadTexts:
    hwCpuRemoved.setStatus(
        "current"
    )

hwCpuFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 26)
)
hwCpuFailure.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswCpuIndex"))
)
if mibBuilder.loadTexts:
    hwCpuFailure.setStatus(
        "current"
    )

hwCpuNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 27)
)
hwCpuNormal.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswCpuIndex"))
)
if mibBuilder.loadTexts:
    hwCpuNormal.setStatus(
        "current"
    )

hwPowerIncompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 28)
)
hwPowerIncompatible.setObjects(
    ("HUAWEI-LswDEVM-MIB", "hwDevMPowerNum")
)
if mibBuilder.loadTexts:
    hwPowerIncompatible.setStatus(
        "current"
    )

hwCpuUsageSevereNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 29)
)
hwCpuUsageSevereNotification.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswCpuIndex"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuRatio"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuUsageMinorThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuUsageSevereThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuUsageRecoverThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapCpuCoreInfo"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapProcessCpuInfo"))
)
if mibBuilder.loadTexts:
    hwCpuUsageSevereNotification.setStatus(
        "current"
    )

hwCpuUsageSevereRecoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 30)
)
hwCpuUsageSevereRecoverNotification.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswCpuIndex"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuRatio"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuUsageMinorThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuUsageSevereThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuUsageRecoverThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapCpuCoreInfo"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapProcessCpuInfo"))
)
if mibBuilder.loadTexts:
    hwCpuUsageSevereRecoverNotification.setStatus(
        "current"
    )

hwCpuUsageMinorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 31)
)
hwCpuUsageMinorNotification.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswCpuIndex"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuRatio"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuUsageMinorThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuUsageSevereThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuUsageRecoverThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapCpuCoreInfo"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapProcessCpuInfo"))
)
if mibBuilder.loadTexts:
    hwCpuUsageMinorNotification.setStatus(
        "current"
    )

hwCpuUsageMinorRecoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 32)
)
hwCpuUsageMinorRecoverNotification.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswCpuIndex"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuRatio"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuUsageMinorThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuUsageSevereThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuUsageRecoverThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapCpuCoreInfo"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapProcessCpuInfo"))
)
if mibBuilder.loadTexts:
    hwCpuUsageMinorRecoverNotification.setStatus(
        "current"
    )

hwMemoryUsageEarlyWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 33)
)
hwMemoryUsageEarlyWarningNotification.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswCpuIndex"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemory"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryFreeRatio"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryHighTotal"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryHighFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryLowTotal"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryLowFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemorySecureThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryEarlyWarningThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryNormalThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryMinorThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemorySevereThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryCriticalThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryCurrentState"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapProcessMemoryInfo"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapSlubInfo"))
)
if mibBuilder.loadTexts:
    hwMemoryUsageEarlyWarningNotification.setStatus(
        "current"
    )

hwMemoryUsageEarlyWarningRecoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 34)
)
hwMemoryUsageEarlyWarningRecoverNotification.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswCpuIndex"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemory"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryFreeRatio"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryHighTotal"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryHighFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryLowTotal"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryLowFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemorySecureThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryEarlyWarningThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryNormalThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryMinorThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemorySevereThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryCriticalThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryCurrentState"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapProcessMemoryInfo"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapSlubInfo"))
)
if mibBuilder.loadTexts:
    hwMemoryUsageEarlyWarningRecoverNotification.setStatus(
        "current"
    )

hwMemoryUsageMinorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 35)
)
hwMemoryUsageMinorNotification.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswCpuIndex"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemory"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryFreeRatio"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryHighTotal"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryHighFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryLowTotal"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryLowFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemorySecureThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryEarlyWarningThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryNormalThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryMinorThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemorySevereThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryCriticalThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryCurrentState"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapProcessMemoryInfo"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapSlubInfo"))
)
if mibBuilder.loadTexts:
    hwMemoryUsageMinorNotification.setStatus(
        "current"
    )

hwMemoryUsageMinorRecoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 36)
)
hwMemoryUsageMinorRecoverNotification.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswCpuIndex"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemory"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryFreeRatio"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryHighTotal"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryHighFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryLowTotal"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryLowFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemorySecureThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryEarlyWarningThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryNormalThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryMinorThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemorySevereThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryCriticalThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryCurrentState"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapProcessMemoryInfo"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapSlubInfo"))
)
if mibBuilder.loadTexts:
    hwMemoryUsageMinorRecoverNotification.setStatus(
        "current"
    )

hwMemoryUsageSevereNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 37)
)
hwMemoryUsageSevereNotification.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswCpuIndex"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemory"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryFreeRatio"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryHighTotal"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryHighFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryLowTotal"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryLowFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemorySecureThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryEarlyWarningThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryNormalThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryMinorThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemorySevereThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryCriticalThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryCurrentState"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapProcessMemoryInfo"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapSlubInfo"))
)
if mibBuilder.loadTexts:
    hwMemoryUsageSevereNotification.setStatus(
        "current"
    )

hwMemoryUsageSevereRecoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 38)
)
hwMemoryUsageSevereRecoverNotification.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswCpuIndex"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemory"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryFreeRatio"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryHighTotal"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryHighFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryLowTotal"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryLowFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemorySecureThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryEarlyWarningThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryNormalThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryMinorThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemorySevereThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryCriticalThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryCurrentState"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapProcessMemoryInfo"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapSlubInfo"))
)
if mibBuilder.loadTexts:
    hwMemoryUsageSevereRecoverNotification.setStatus(
        "current"
    )

hwMemoryUsageCriticalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 39)
)
hwMemoryUsageCriticalNotification.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswCpuIndex"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemory"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryFreeRatio"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryHighTotal"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryHighFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryLowTotal"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryLowFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemorySecureThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryEarlyWarningThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryNormalThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryMinorThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemorySevereThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryCriticalThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryCurrentState"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapProcessMemoryInfo"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapSlubInfo"))
)
if mibBuilder.loadTexts:
    hwMemoryUsageCriticalNotification.setStatus(
        "current"
    )

hwMemoryUsageCriticalRecoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 1, 40)
)
hwMemoryUsageCriticalRecoverNotification.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswCpuIndex"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemory"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryFreeRatio"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryHighTotal"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryHighFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryLowTotal"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryLowFree"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemorySecureThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryEarlyWarningThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryNormalThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryMinorThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemorySevereThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryCriticalThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCpuMemoryCurrentState"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapProcessMemoryInfo"),
        ("HUAWEI-LswTRAP-MIB", "hwsLswTrapSlubInfo"))
)
if mibBuilder.loadTexts:
    hwMemoryUsageCriticalRecoverNotification.setStatus(
        "current"
    )

hwCoreUsageNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 3, 0, 1)
)
hwCoreUsageNotification.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswCpuIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswCoreIndex"),
        ("HUAWEI-LswTRAP-MIB", "hwLswCoreTrapUsage"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswCoreThreshold"),
        ("HUAWEI-LswTRAP-MIB", "hwLswTrapCpuUsage"),
        ("HUAWEI-LswTRAP-MIB", "hwLswTrapCoreProcessInfo"))
)
if mibBuilder.loadTexts:
    hwCoreUsageNotification.setStatus(
        "current"
    )

hwBoardPowerNotEnough = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 3, 0, 2)
)
hwBoardPowerNotEnough.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"),
        ("HUAWEI-LswTRAP-MIB", "hwBoardAvailablePower"),
        ("HUAWEI-LswTRAP-MIB", "hwBoardRequiredPower"))
)
if mibBuilder.loadTexts:
    hwBoardPowerNotEnough.setStatus(
        "current"
    )

hwAlarmInPortIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 3, 0, 3)
)
hwAlarmInPortIn.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwAlarmInPortIn.setStatus(
        "current"
    )

hwAlarmInPortRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 12, 3, 0, 4)
)
hwAlarmInPortRecover.setObjects(
      *(("HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
        ("HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwAlarmInPortRecover.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-LswTRAP-MIB",
    **{"hwsLswTrapMib": hwsLswTrapMib,
       "hwsLswTRAPMibObject": hwsLswTRAPMibObject,
       "powerfailure": powerfailure,
       "hwPowerNormal": hwPowerNormal,
       "hwMasterPowerNormal": hwMasterPowerNormal,
       "hwSlavePowerNormal": hwSlavePowerNormal,
       "hwPowerRemoved": hwPowerRemoved,
       "fanfailure": fanfailure,
       "hwFanNormal": hwFanNormal,
       "hwBoardRemoved": hwBoardRemoved,
       "hwBoardInserted": hwBoardInserted,
       "hwBoardFailure": hwBoardFailure,
       "hwBoardNormal": hwBoardNormal,
       "hwSubcardRemove": hwSubcardRemove,
       "hwSubcardInsert": hwSubcardInsert,
       "hwBoaardTemperatureLower": hwBoaardTemperatureLower,
       "hwBoaardTemperatureFromLowerToNormal": hwBoaardTemperatureFromLowerToNormal,
       "hwBoaardTemperatureHigher": hwBoaardTemperatureHigher,
       "hwBoaardTemperatureFormHigherToNormal": hwBoaardTemperatureFormHigherToNormal,
       "hwRequestLoading": hwRequestLoading,
       "hwLoadFailure": hwLoadFailure,
       "hwLoadFinished": hwLoadFinished,
       "hwBackBoardModeSetFuilure": hwBackBoardModeSetFuilure,
       "hwBackBoardModeSetOK": hwBackBoardModeSetOK,
       "hwPowerInserted": hwPowerInserted,
       "hwBootImageUpdated": hwBootImageUpdated,
       "hwCpuRemoved": hwCpuRemoved,
       "hwCpuFailure": hwCpuFailure,
       "hwCpuNormal": hwCpuNormal,
       "hwPowerIncompatible": hwPowerIncompatible,
       "hwCpuUsageSevereNotification": hwCpuUsageSevereNotification,
       "hwCpuUsageSevereRecoverNotification": hwCpuUsageSevereRecoverNotification,
       "hwCpuUsageMinorNotification": hwCpuUsageMinorNotification,
       "hwCpuUsageMinorRecoverNotification": hwCpuUsageMinorRecoverNotification,
       "hwMemoryUsageEarlyWarningNotification": hwMemoryUsageEarlyWarningNotification,
       "hwMemoryUsageEarlyWarningRecoverNotification": hwMemoryUsageEarlyWarningRecoverNotification,
       "hwMemoryUsageMinorNotification": hwMemoryUsageMinorNotification,
       "hwMemoryUsageMinorRecoverNotification": hwMemoryUsageMinorRecoverNotification,
       "hwMemoryUsageSevereNotification": hwMemoryUsageSevereNotification,
       "hwMemoryUsageSevereRecoverNotification": hwMemoryUsageSevereRecoverNotification,
       "hwMemoryUsageCriticalNotification": hwMemoryUsageCriticalNotification,
       "hwMemoryUsageCriticalRecoverNotification": hwMemoryUsageCriticalRecoverNotification,
       "hwNetworkHealthMonitorFailure": hwNetworkHealthMonitorFailure,
       "hwNetworkHealthMonitorNormal": hwNetworkHealthMonitorNormal,
       "hwsLswTRAPMibInfor": hwsLswTRAPMibInfor,
       "hwsLswTrapCpuCoreInfo": hwsLswTrapCpuCoreInfo,
       "hwsLswTrapProcessCpuInfo": hwsLswTrapProcessCpuInfo,
       "hwsLswTrapProcessMemoryInfo": hwsLswTrapProcessMemoryInfo,
       "hwsLswTrapSlubInfo": hwsLswTrapSlubInfo,
       "hwLswTrapCpuUsage": hwLswTrapCpuUsage,
       "hwLswTrapCoreProcessInfo": hwLswTrapCoreProcessInfo,
       "hwLswCoreTrapUsage": hwLswCoreTrapUsage,
       "hwBoardAvailablePower": hwBoardAvailablePower,
       "hwBoardRequiredPower": hwBoardRequiredPower,
       "hwsLswTRAPMibObjectV2": hwsLswTRAPMibObjectV2,
       "hwsLswTRAPMibObjectV2Prefix": hwsLswTRAPMibObjectV2Prefix,
       "hwCoreUsageNotification": hwCoreUsageNotification,
       "hwBoardPowerNotEnough": hwBoardPowerNotEnough,
       "hwAlarmInPortIn": hwAlarmInPortIn,
       "hwAlarmInPortRecover": hwAlarmInPortRecover}
)
