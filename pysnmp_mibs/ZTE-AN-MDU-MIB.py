# SNMP MIB module (ZTE-AN-MDU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-MDU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:01 2025
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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(VlanId,
 ZxAnIfindex,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "VlanId",
    "ZxAnIfindex",
    "zxAn")


# MODULE-IDENTITY

zxAnMduMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnMduSysCtrlObjects_ObjectIdentity = ObjectIdentity
zxAnMduSysCtrlObjects = _ZxAnMduSysCtrlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 2)
)
_ZxAnMduSysDataMgmt_ObjectIdentity = ObjectIdentity
zxAnMduSysDataMgmt = _ZxAnMduSysDataMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 2, 1)
)


class _ZxAnMduSaveModifiedToNvmInterval_Type(Integer32):
    """Custom type zxAnMduSaveModifiedToNvmInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_ZxAnMduSaveModifiedToNvmInterval_Type.__name__ = "Integer32"
_ZxAnMduSaveModifiedToNvmInterval_Object = MibScalar
zxAnMduSaveModifiedToNvmInterval = _ZxAnMduSaveModifiedToNvmInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 2, 1, 1),
    _ZxAnMduSaveModifiedToNvmInterval_Type()
)
zxAnMduSaveModifiedToNvmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMduSaveModifiedToNvmInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMduSaveModifiedToNvmInterval.setUnits("minutes")


class _ZxAnMduSaveToNvmInterval_Type(Integer32):
    """Custom type zxAnMduSaveToNvmInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8760),
    )


_ZxAnMduSaveToNvmInterval_Type.__name__ = "Integer32"
_ZxAnMduSaveToNvmInterval_Object = MibScalar
zxAnMduSaveToNvmInterval = _ZxAnMduSaveToNvmInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 2, 1, 2),
    _ZxAnMduSaveToNvmInterval_Type()
)
zxAnMduSaveToNvmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMduSaveToNvmInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMduSaveToNvmInterval.setUnits("hours")
_ZxAnMduServiceObjects_ObjectIdentity = ObjectIdentity
zxAnMduServiceObjects = _ZxAnMduServiceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 3)
)
_ZxAnMduHgMacFeatureCodeTable_Object = MibTable
zxAnMduHgMacFeatureCodeTable = _ZxAnMduHgMacFeatureCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 3, 1)
)
if mibBuilder.loadTexts:
    zxAnMduHgMacFeatureCodeTable.setStatus("current")
_ZxAnMduHgMacFeatureCodeEntry_Object = MibTableRow
zxAnMduHgMacFeatureCodeEntry = _ZxAnMduHgMacFeatureCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 3, 1, 1)
)
zxAnMduHgMacFeatureCodeEntry.setIndexNames(
    (0, "ZTE-AN-MDU-MIB", "zxAnMduHgMacFeatureCodeId"),
)
if mibBuilder.loadTexts:
    zxAnMduHgMacFeatureCodeEntry.setStatus("current")
_ZxAnMduHgMacFeatureCodeId_Type = Integer32
_ZxAnMduHgMacFeatureCodeId_Object = MibTableColumn
zxAnMduHgMacFeatureCodeId = _ZxAnMduHgMacFeatureCodeId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 3, 1, 1, 1),
    _ZxAnMduHgMacFeatureCodeId_Type()
)
zxAnMduHgMacFeatureCodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMduHgMacFeatureCodeId.setStatus("current")


class _ZxAnMduHgMacFeatureCode_Type(DisplayString):
    """Custom type zxAnMduHgMacFeatureCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnMduHgMacFeatureCode_Type.__name__ = "DisplayString"
_ZxAnMduHgMacFeatureCode_Object = MibTableColumn
zxAnMduHgMacFeatureCode = _ZxAnMduHgMacFeatureCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 3, 1, 1, 2),
    _ZxAnMduHgMacFeatureCode_Type()
)
zxAnMduHgMacFeatureCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMduHgMacFeatureCode.setStatus("current")
_ZxAnMduHgMgmtVlan_Type = Integer32
_ZxAnMduHgMgmtVlan_Object = MibScalar
zxAnMduHgMgmtVlan = _ZxAnMduHgMgmtVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 3, 2),
    _ZxAnMduHgMgmtVlan_Type()
)
zxAnMduHgMgmtVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMduHgMgmtVlan.setStatus("current")


class _ZxAnMduConfigFileCRC32_Type(DisplayString):
    """Custom type zxAnMduConfigFileCRC32 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_ZxAnMduConfigFileCRC32_Type.__name__ = "DisplayString"
_ZxAnMduConfigFileCRC32_Object = MibScalar
zxAnMduConfigFileCRC32 = _ZxAnMduConfigFileCRC32_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 3, 3),
    _ZxAnMduConfigFileCRC32_Type()
)
zxAnMduConfigFileCRC32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMduConfigFileCRC32.setStatus("current")


class _ZxAnMduLoadSettings_Type(Integer32):
    """Custom type zxAnMduLoadSettings based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("loadFactoryDefaults", 1)
    )


_ZxAnMduLoadSettings_Type.__name__ = "Integer32"
_ZxAnMduLoadSettings_Object = MibScalar
zxAnMduLoadSettings = _ZxAnMduLoadSettings_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 3, 4),
    _ZxAnMduLoadSettings_Type()
)
zxAnMduLoadSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMduLoadSettings.setStatus("current")
_ZxAnMduHgTable_Object = MibTable
zxAnMduHgTable = _ZxAnMduHgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 3, 21)
)
if mibBuilder.loadTexts:
    zxAnMduHgTable.setStatus("current")
_ZxAnMduHgEntry_Object = MibTableRow
zxAnMduHgEntry = _ZxAnMduHgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 3, 21, 1)
)
zxAnMduHgEntry.setIndexNames(
    (0, "ZTE-AN-MDU-MIB", "zxAnMduPortIfIndex"),
    (0, "ZTE-AN-MDU-MIB", "zxAnMduHgMac"),
)
if mibBuilder.loadTexts:
    zxAnMduHgEntry.setStatus("current")
_ZxAnMduPortIfIndex_Type = ZxAnIfindex
_ZxAnMduPortIfIndex_Object = MibTableColumn
zxAnMduPortIfIndex = _ZxAnMduPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 3, 21, 1, 1),
    _ZxAnMduPortIfIndex_Type()
)
zxAnMduPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMduPortIfIndex.setStatus("current")
_ZxAnMduHgMac_Type = MacAddress
_ZxAnMduHgMac_Object = MibTableColumn
zxAnMduHgMac = _ZxAnMduHgMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 3, 21, 1, 2),
    _ZxAnMduHgMac_Type()
)
zxAnMduHgMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMduHgMac.setStatus("current")


class _ZxAnMduHgReportStatus_Type(Integer32):
    """Custom type zxAnMduHgReportStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("success", 1))
    )


_ZxAnMduHgReportStatus_Type.__name__ = "Integer32"
_ZxAnMduHgReportStatus_Object = MibTableColumn
zxAnMduHgReportStatus = _ZxAnMduHgReportStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 3, 21, 1, 3),
    _ZxAnMduHgReportStatus_Type()
)
zxAnMduHgReportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMduHgReportStatus.setStatus("current")
_ZxAnMduHgDataVlan_Type = Integer32
_ZxAnMduHgDataVlan_Object = MibTableColumn
zxAnMduHgDataVlan = _ZxAnMduHgDataVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 3, 21, 1, 4),
    _ZxAnMduHgDataVlan_Type()
)
zxAnMduHgDataVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMduHgDataVlan.setStatus("current")
_ZxAnMduHgVideoVlan_Type = Integer32
_ZxAnMduHgVideoVlan_Object = MibTableColumn
zxAnMduHgVideoVlan = _ZxAnMduHgVideoVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 3, 21, 1, 5),
    _ZxAnMduHgVideoVlan_Type()
)
zxAnMduHgVideoVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMduHgVideoVlan.setStatus("current")
_ZxAnMduHgVoiceVlan_Type = Integer32
_ZxAnMduHgVoiceVlan_Object = MibTableColumn
zxAnMduHgVoiceVlan = _ZxAnMduHgVoiceVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 3, 21, 1, 6),
    _ZxAnMduHgVoiceVlan_Type()
)
zxAnMduHgVoiceVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMduHgVoiceVlan.setStatus("current")


class _ZxAnMduType_Type(DisplayString):
    """Custom type zxAnMduType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_ZxAnMduType_Type.__name__ = "DisplayString"
_ZxAnMduType_Object = MibTableColumn
zxAnMduType = _ZxAnMduType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 3, 21, 1, 7),
    _ZxAnMduType_Type()
)
zxAnMduType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMduType.setStatus("current")
_ZxAnMduEquipObjects_ObjectIdentity = ObjectIdentity
zxAnMduEquipObjects = _ZxAnMduEquipObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 10)
)
_ZxAnMduEnvSwitchMgmt_ObjectIdentity = ObjectIdentity
zxAnMduEnvSwitchMgmt = _ZxAnMduEnvSwitchMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 10, 21)
)
_ZxAnMduEnvDeviceTable_Object = MibTable
zxAnMduEnvDeviceTable = _ZxAnMduEnvDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 10, 21, 11)
)
if mibBuilder.loadTexts:
    zxAnMduEnvDeviceTable.setStatus("current")
_ZxAnMduEnvDeviceEntry_Object = MibTableRow
zxAnMduEnvDeviceEntry = _ZxAnMduEnvDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 10, 21, 11, 1)
)
zxAnMduEnvDeviceEntry.setIndexNames(
    (0, "ZTE-AN-MDU-MIB", "zxAnMduEnvEnvDeviceIndex"),
)
if mibBuilder.loadTexts:
    zxAnMduEnvDeviceEntry.setStatus("current")
_ZxAnMduEnvEnvDeviceIndex_Type = Integer32
_ZxAnMduEnvEnvDeviceIndex_Object = MibTableColumn
zxAnMduEnvEnvDeviceIndex = _ZxAnMduEnvEnvDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 10, 21, 11, 1, 1),
    _ZxAnMduEnvEnvDeviceIndex_Type()
)
zxAnMduEnvEnvDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMduEnvEnvDeviceIndex.setStatus("current")


class _ZxAnMduEnvEnvDeviceName_Type(DisplayString):
    """Custom type zxAnMduEnvEnvDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnMduEnvEnvDeviceName_Type.__name__ = "DisplayString"
_ZxAnMduEnvEnvDeviceName_Object = MibTableColumn
zxAnMduEnvEnvDeviceName = _ZxAnMduEnvEnvDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 10, 21, 11, 1, 2),
    _ZxAnMduEnvEnvDeviceName_Type()
)
zxAnMduEnvEnvDeviceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMduEnvEnvDeviceName.setStatus("current")
_ZxAnMduEnvDeviceRowStatus_Type = RowStatus
_ZxAnMduEnvDeviceRowStatus_Object = MibTableColumn
zxAnMduEnvDeviceRowStatus = _ZxAnMduEnvDeviceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 10, 21, 11, 1, 3),
    _ZxAnMduEnvDeviceRowStatus_Type()
)
zxAnMduEnvDeviceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMduEnvDeviceRowStatus.setStatus("current")
_ZxAnMduSwitchTable_Object = MibTable
zxAnMduSwitchTable = _ZxAnMduSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 10, 21, 12)
)
if mibBuilder.loadTexts:
    zxAnMduSwitchTable.setStatus("current")
_ZxAnMduSwitchEntry_Object = MibTableRow
zxAnMduSwitchEntry = _ZxAnMduSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 10, 21, 12, 1)
)
zxAnMduSwitchEntry.setIndexNames(
    (0, "ZTE-AN-MDU-MIB", "zxAnMduEnvSwitchIndex"),
)
if mibBuilder.loadTexts:
    zxAnMduSwitchEntry.setStatus("current")
_ZxAnMduEnvSwitchIndex_Type = Integer32
_ZxAnMduEnvSwitchIndex_Object = MibTableColumn
zxAnMduEnvSwitchIndex = _ZxAnMduEnvSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 10, 21, 12, 1, 1),
    _ZxAnMduEnvSwitchIndex_Type()
)
zxAnMduEnvSwitchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMduEnvSwitchIndex.setStatus("current")


class _ZxAnMduEnvDeviceId_Type(Integer32):
    """Custom type zxAnMduEnvDeviceId based on Integer32"""
    defaultValue = 0


_ZxAnMduEnvDeviceId_Type.__name__ = "Integer32"
_ZxAnMduEnvDeviceId_Object = MibTableColumn
zxAnMduEnvDeviceId = _ZxAnMduEnvDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 10, 21, 12, 1, 2),
    _ZxAnMduEnvDeviceId_Type()
)
zxAnMduEnvDeviceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMduEnvDeviceId.setStatus("current")


class _ZxAnMduEnvSwitchNormalStatus_Type(Integer32):
    """Custom type zxAnMduEnvSwitchNormalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_ZxAnMduEnvSwitchNormalStatus_Type.__name__ = "Integer32"
_ZxAnMduEnvSwitchNormalStatus_Object = MibTableColumn
zxAnMduEnvSwitchNormalStatus = _ZxAnMduEnvSwitchNormalStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 10, 21, 12, 1, 3),
    _ZxAnMduEnvSwitchNormalStatus_Type()
)
zxAnMduEnvSwitchNormalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMduEnvSwitchNormalStatus.setStatus("current")


class _ZxAnMduEnvSwitchEnable_Type(Integer32):
    """Custom type zxAnMduEnvSwitchEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnMduEnvSwitchEnable_Type.__name__ = "Integer32"
_ZxAnMduEnvSwitchEnable_Object = MibTableColumn
zxAnMduEnvSwitchEnable = _ZxAnMduEnvSwitchEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 10, 21, 12, 1, 4),
    _ZxAnMduEnvSwitchEnable_Type()
)
zxAnMduEnvSwitchEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMduEnvSwitchEnable.setStatus("current")


class _ZxAnMduEnvSwitchCurrentStatus_Type(Integer32):
    """Custom type zxAnMduEnvSwitchCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_ZxAnMduEnvSwitchCurrentStatus_Type.__name__ = "Integer32"
_ZxAnMduEnvSwitchCurrentStatus_Object = MibTableColumn
zxAnMduEnvSwitchCurrentStatus = _ZxAnMduEnvSwitchCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 10, 21, 12, 1, 5),
    _ZxAnMduEnvSwitchCurrentStatus_Type()
)
zxAnMduEnvSwitchCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMduEnvSwitchCurrentStatus.setStatus("current")
_ZxAnMduTrapObjects_ObjectIdentity = ObjectIdentity
zxAnMduTrapObjects = _ZxAnMduTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 20)
)
_ZxAnMduServiceTrapObjects_ObjectIdentity = ObjectIdentity
zxAnMduServiceTrapObjects = _ZxAnMduServiceTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 20, 3)
)
_ZxAnMduEquipTrapObjects_ObjectIdentity = ObjectIdentity
zxAnMduEquipTrapObjects = _ZxAnMduEquipTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 20, 10)
)
_ZxAnMduMibEnd_Type = Integer32
_ZxAnMduMibEnd_Object = MibScalar
zxAnMduMibEnd = _ZxAnMduMibEnd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 100),
    _ZxAnMduMibEnd_Type()
)
zxAnMduMibEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMduMibEnd.setStatus("current")

# Managed Objects groups


# Notification objects

zxAnMduNetworkAccessRequest = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 20, 3, 1)
)
zxAnMduNetworkAccessRequest.setObjects(
      *(("ZTE-AN-MDU-MIB", "zxAnMduPortIfIndex"),
        ("ZTE-AN-MDU-MIB", "zxAnMduHgMac"),
        ("ZTE-AN-MDU-MIB", "zxAnMduHgDataVlan"),
        ("ZTE-AN-MDU-MIB", "zxAnMduHgVideoVlan"),
        ("ZTE-AN-MDU-MIB", "zxAnMduHgVoiceVlan"),
        ("ZTE-AN-MDU-MIB", "zxAnMduType"))
)
if mibBuilder.loadTexts:
    zxAnMduNetworkAccessRequest.setStatus(
        "current"
    )

zxAnMduUploadConfigFileRequest = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 20, 3, 2)
)
zxAnMduUploadConfigFileRequest.setObjects(
      *(("ZTE-AN-MDU-MIB", "zxAnMduPortIfIndex"),
        ("ZTE-AN-MDU-MIB", "zxAnMduConfigFileCRC32"))
)
if mibBuilder.loadTexts:
    zxAnMduUploadConfigFileRequest.setStatus(
        "current"
    )

zxAnMduEnvSwitchFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 20, 10, 1)
)
zxAnMduEnvSwitchFailed.setObjects(
      *(("ZTE-AN-MDU-MIB", "zxAnMduEnvDeviceId"),
        ("ZTE-AN-MDU-MIB", "zxAnMduEnvEnvDeviceName"),
        ("ZTE-AN-MDU-MIB", "zxAnMduEnvSwitchNormalStatus"),
        ("ZTE-AN-MDU-MIB", "zxAnMduEnvSwitchCurrentStatus"))
)
if mibBuilder.loadTexts:
    zxAnMduEnvSwitchFailed.setStatus(
        "current"
    )

zxAnMduEnvSwitchRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1016, 20, 10, 2)
)
zxAnMduEnvSwitchRecovered.setObjects(
      *(("ZTE-AN-MDU-MIB", "zxAnMduEnvDeviceId"),
        ("ZTE-AN-MDU-MIB", "zxAnMduEnvEnvDeviceName"),
        ("ZTE-AN-MDU-MIB", "zxAnMduEnvSwitchNormalStatus"),
        ("ZTE-AN-MDU-MIB", "zxAnMduEnvSwitchCurrentStatus"))
)
if mibBuilder.loadTexts:
    zxAnMduEnvSwitchRecovered.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-MDU-MIB",
    **{"zxAnMduMib": zxAnMduMib,
       "zxAnMduSysCtrlObjects": zxAnMduSysCtrlObjects,
       "zxAnMduSysDataMgmt": zxAnMduSysDataMgmt,
       "zxAnMduSaveModifiedToNvmInterval": zxAnMduSaveModifiedToNvmInterval,
       "zxAnMduSaveToNvmInterval": zxAnMduSaveToNvmInterval,
       "zxAnMduServiceObjects": zxAnMduServiceObjects,
       "zxAnMduHgMacFeatureCodeTable": zxAnMduHgMacFeatureCodeTable,
       "zxAnMduHgMacFeatureCodeEntry": zxAnMduHgMacFeatureCodeEntry,
       "zxAnMduHgMacFeatureCodeId": zxAnMduHgMacFeatureCodeId,
       "zxAnMduHgMacFeatureCode": zxAnMduHgMacFeatureCode,
       "zxAnMduHgMgmtVlan": zxAnMduHgMgmtVlan,
       "zxAnMduConfigFileCRC32": zxAnMduConfigFileCRC32,
       "zxAnMduLoadSettings": zxAnMduLoadSettings,
       "zxAnMduHgTable": zxAnMduHgTable,
       "zxAnMduHgEntry": zxAnMduHgEntry,
       "zxAnMduPortIfIndex": zxAnMduPortIfIndex,
       "zxAnMduHgMac": zxAnMduHgMac,
       "zxAnMduHgReportStatus": zxAnMduHgReportStatus,
       "zxAnMduHgDataVlan": zxAnMduHgDataVlan,
       "zxAnMduHgVideoVlan": zxAnMduHgVideoVlan,
       "zxAnMduHgVoiceVlan": zxAnMduHgVoiceVlan,
       "zxAnMduType": zxAnMduType,
       "zxAnMduEquipObjects": zxAnMduEquipObjects,
       "zxAnMduEnvSwitchMgmt": zxAnMduEnvSwitchMgmt,
       "zxAnMduEnvDeviceTable": zxAnMduEnvDeviceTable,
       "zxAnMduEnvDeviceEntry": zxAnMduEnvDeviceEntry,
       "zxAnMduEnvEnvDeviceIndex": zxAnMduEnvEnvDeviceIndex,
       "zxAnMduEnvEnvDeviceName": zxAnMduEnvEnvDeviceName,
       "zxAnMduEnvDeviceRowStatus": zxAnMduEnvDeviceRowStatus,
       "zxAnMduSwitchTable": zxAnMduSwitchTable,
       "zxAnMduSwitchEntry": zxAnMduSwitchEntry,
       "zxAnMduEnvSwitchIndex": zxAnMduEnvSwitchIndex,
       "zxAnMduEnvDeviceId": zxAnMduEnvDeviceId,
       "zxAnMduEnvSwitchNormalStatus": zxAnMduEnvSwitchNormalStatus,
       "zxAnMduEnvSwitchEnable": zxAnMduEnvSwitchEnable,
       "zxAnMduEnvSwitchCurrentStatus": zxAnMduEnvSwitchCurrentStatus,
       "zxAnMduTrapObjects": zxAnMduTrapObjects,
       "zxAnMduServiceTrapObjects": zxAnMduServiceTrapObjects,
       "zxAnMduNetworkAccessRequest": zxAnMduNetworkAccessRequest,
       "zxAnMduUploadConfigFileRequest": zxAnMduUploadConfigFileRequest,
       "zxAnMduEquipTrapObjects": zxAnMduEquipTrapObjects,
       "zxAnMduEnvSwitchFailed": zxAnMduEnvSwitchFailed,
       "zxAnMduEnvSwitchRecovered": zxAnMduEnvSwitchRecovered,
       "zxAnMduMibEnd": zxAnMduMibEnd}
)
