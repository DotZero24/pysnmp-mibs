# SNMP MIB module (SWITCH-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:35 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(EnableVar,
 PortList,
 Vlanset) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar",
    "PortList",
    "Vlanset")


# MODULE-IDENTITY

rcSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1)
)
if mibBuilder.loadTexts:
    rcSystem.setRevisions(
        ("1904-12-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcSwitchInformation_ObjectIdentity = ObjectIdentity
rcSwitchInformation = _RcSwitchInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 1)
)
_RcSwitchRoseVersion_Type = OctetString
_RcSwitchRoseVersion_Object = MibScalar
rcSwitchRoseVersion = _RcSwitchRoseVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 1, 1),
    _RcSwitchRoseVersion_Type()
)
rcSwitchRoseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSwitchRoseVersion.setStatus("current")
_RcSwitchHardwareVersion_Type = OctetString
_RcSwitchHardwareVersion_Object = MibScalar
rcSwitchHardwareVersion = _RcSwitchHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 1, 2),
    _RcSwitchHardwareVersion_Type()
)
rcSwitchHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSwitchHardwareVersion.setStatus("current")
_RcSwitchServiceInfo_Type = Integer32
_RcSwitchServiceInfo_Object = MibScalar
rcSwitchServiceInfo = _RcSwitchServiceInfo_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 1, 3),
    _RcSwitchServiceInfo_Type()
)
rcSwitchServiceInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSwitchServiceInfo.setStatus("deprecated")


class _RcSwitchLastErrorCode_Type(Integer32):
    """Custom type rcSwitchLastErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RcSwitchLastErrorCode_Type.__name__ = "Integer32"
_RcSwitchLastErrorCode_Object = MibScalar
rcSwitchLastErrorCode = _RcSwitchLastErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 1, 4),
    _RcSwitchLastErrorCode_Type()
)
rcSwitchLastErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSwitchLastErrorCode.setStatus("deprecated")
_RcSwitchMaxPhysicalPortNum_Type = Integer32
_RcSwitchMaxPhysicalPortNum_Object = MibScalar
rcSwitchMaxPhysicalPortNum = _RcSwitchMaxPhysicalPortNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 1, 5),
    _RcSwitchMaxPhysicalPortNum_Type()
)
rcSwitchMaxPhysicalPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSwitchMaxPhysicalPortNum.setStatus("current")
_RcSwitchMaxAggregationPortNum_Type = Integer32
_RcSwitchMaxAggregationPortNum_Object = MibScalar
rcSwitchMaxAggregationPortNum = _RcSwitchMaxAggregationPortNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 1, 6),
    _RcSwitchMaxAggregationPortNum_Type()
)
rcSwitchMaxAggregationPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSwitchMaxAggregationPortNum.setStatus("current")
_RcSwitchMaxL3IpSubnetNum_Type = Integer32
_RcSwitchMaxL3IpSubnetNum_Object = MibScalar
rcSwitchMaxL3IpSubnetNum = _RcSwitchMaxL3IpSubnetNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 1, 7),
    _RcSwitchMaxL3IpSubnetNum_Type()
)
rcSwitchMaxL3IpSubnetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSwitchMaxL3IpSubnetNum.setStatus("current")
_RcSwitchMacTableCapability_Type = Integer32
_RcSwitchMacTableCapability_Object = MibScalar
rcSwitchMacTableCapability = _RcSwitchMacTableCapability_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 1, 8),
    _RcSwitchMacTableCapability_Type()
)
rcSwitchMacTableCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSwitchMacTableCapability.setStatus("current")
_RcSwitchMacAddress_Type = MacAddress
_RcSwitchMacAddress_Object = MibScalar
rcSwitchMacAddress = _RcSwitchMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 1, 9),
    _RcSwitchMacAddress_Type()
)
rcSwitchMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSwitchMacAddress.setStatus("current")
_RcSwitchVlanSpaceSize_Type = Integer32
_RcSwitchVlanSpaceSize_Object = MibScalar
rcSwitchVlanSpaceSize = _RcSwitchVlanSpaceSize_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 1, 10),
    _RcSwitchVlanSpaceSize_Type()
)
rcSwitchVlanSpaceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSwitchVlanSpaceSize.setStatus("current")
_RcSwitchPvidSpaceSize_Type = Integer32
_RcSwitchPvidSpaceSize_Object = MibScalar
rcSwitchPvidSpaceSize = _RcSwitchPvidSpaceSize_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 1, 11),
    _RcSwitchPvidSpaceSize_Type()
)
rcSwitchPvidSpaceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSwitchPvidSpaceSize.setStatus("current")
_RcSwitchDefaultVlan_Type = Integer32
_RcSwitchDefaultVlan_Object = MibScalar
rcSwitchDefaultVlan = _RcSwitchDefaultVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 1, 12),
    _RcSwitchDefaultVlan_Type()
)
rcSwitchDefaultVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSwitchDefaultVlan.setStatus("current")
_RcSwitchBootstrapVersion_Type = OctetString
_RcSwitchBootstrapVersion_Object = MibScalar
rcSwitchBootstrapVersion = _RcSwitchBootstrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 1, 13),
    _RcSwitchBootstrapVersion_Type()
)
rcSwitchBootstrapVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSwitchBootstrapVersion.setStatus("current")
_RcSwitchSerialNumber_Type = OctetString
_RcSwitchSerialNumber_Object = MibScalar
rcSwitchSerialNumber = _RcSwitchSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 1, 14),
    _RcSwitchSerialNumber_Type()
)
rcSwitchSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSwitchSerialNumber.setStatus("current")
_RcSwitchFpgaVersion_Type = OctetString
_RcSwitchFpgaVersion_Object = MibScalar
rcSwitchFpgaVersion = _RcSwitchFpgaVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 1, 15),
    _RcSwitchFpgaVersion_Type()
)
rcSwitchFpgaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSwitchFpgaVersion.setStatus("current")
_RcSwitchProductVersion_Type = OctetString
_RcSwitchProductVersion_Object = MibScalar
rcSwitchProductVersion = _RcSwitchProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 1, 16),
    _RcSwitchProductVersion_Type()
)
rcSwitchProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSwitchProductVersion.setStatus("current")
_RcSwitchCmpAbName_Type = OctetString
_RcSwitchCmpAbName_Object = MibScalar
rcSwitchCmpAbName = _RcSwitchCmpAbName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 1, 17),
    _RcSwitchCmpAbName_Type()
)
rcSwitchCmpAbName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSwitchCmpAbName.setStatus("current")
_RcSwitchCmpFullName_Type = OctetString
_RcSwitchCmpFullName_Object = MibScalar
rcSwitchCmpFullName = _RcSwitchCmpFullName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 1, 18),
    _RcSwitchCmpFullName_Type()
)
rcSwitchCmpFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSwitchCmpFullName.setStatus("current")
_RcSwitchDeviceName_Type = OctetString
_RcSwitchDeviceName_Object = MibScalar
rcSwitchDeviceName = _RcSwitchDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 1, 19),
    _RcSwitchDeviceName_Type()
)
rcSwitchDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSwitchDeviceName.setStatus("current")
_RcSlotInformation_ObjectIdentity = ObjectIdentity
rcSlotInformation = _RcSlotInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 2)
)
_RcSlotNum_Type = Integer32
_RcSlotNum_Object = MibScalar
rcSlotNum = _RcSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 2, 1),
    _RcSlotNum_Type()
)
rcSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSlotNum.setStatus("current")
_RcSlotStateTable_Object = MibTable
rcSlotStateTable = _RcSlotStateTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    rcSlotStateTable.setStatus("current")
_RcSlotStateEntry_Object = MibTableRow
rcSlotStateEntry = _RcSlotStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 2, 2, 1)
)
rcSlotStateEntry.setIndexNames(
    (0, "SWITCH-SYSTEM-MIB", "rcSlotIndex"),
)
if mibBuilder.loadTexts:
    rcSlotStateEntry.setStatus("current")
_RcSlotIndex_Type = Integer32
_RcSlotIndex_Object = MibTableColumn
rcSlotIndex = _RcSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 2, 2, 1, 1),
    _RcSlotIndex_Type()
)
rcSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcSlotIndex.setStatus("current")
_RcSlotPortStart_Type = Integer32
_RcSlotPortStart_Object = MibTableColumn
rcSlotPortStart = _RcSlotPortStart_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 2, 2, 1, 2),
    _RcSlotPortStart_Type()
)
rcSlotPortStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSlotPortStart.setStatus("current")
_RcSlotPortNum_Type = Integer32
_RcSlotPortNum_Object = MibTableColumn
rcSlotPortNum = _RcSlotPortNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 2, 2, 1, 3),
    _RcSlotPortNum_Type()
)
rcSlotPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSlotPortNum.setStatus("current")


class _RcSlotType_Type(Integer32):
    """Custom type rcSlotType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("inexistence", 0),
          ("fx-DulMode-1000M", 1),
          ("tx-1000M", 2),
          ("fx-SigMode-1000M", 3),
          ("fx-DulMode-100M", 4),
          ("fx-SigMode-100M", 5),
          ("tx-100M", 6),
          ("px-1000M", 7))
    )


_RcSlotType_Type.__name__ = "Integer32"
_RcSlotType_Object = MibTableColumn
rcSlotType = _RcSlotType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 2, 2, 1, 4),
    _RcSlotType_Type()
)
rcSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSlotType.setStatus("current")
_RcSwitchConfig_ObjectIdentity = ObjectIdentity
rcSwitchConfig = _RcSwitchConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3)
)


class _RcMacAgingTime_Type(Integer32):
    """Custom type rcMacAgingTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RcMacAgingTime_Type.__name__ = "Integer32"
_RcMacAgingTime_Object = MibScalar
rcMacAgingTime = _RcMacAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 1),
    _RcMacAgingTime_Type()
)
rcMacAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMacAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    rcMacAgingTime.setUnits("second")


class _RcStormControlBcastEnable_Type(EnableVar):
    """Custom type rcStormControlBcastEnable based on EnableVar"""
    defaultValue = 1


_RcStormControlBcastEnable_Type.__name__ = "EnableVar"
_RcStormControlBcastEnable_Object = MibScalar
rcStormControlBcastEnable = _RcStormControlBcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 2),
    _RcStormControlBcastEnable_Type()
)
rcStormControlBcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcStormControlBcastEnable.setStatus("mandatory")


class _RcStormControlMcastEnable_Type(EnableVar):
    """Custom type rcStormControlMcastEnable based on EnableVar"""
    defaultValue = 2


_RcStormControlMcastEnable_Type.__name__ = "EnableVar"
_RcStormControlMcastEnable_Object = MibScalar
rcStormControlMcastEnable = _RcStormControlMcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 3),
    _RcStormControlMcastEnable_Type()
)
rcStormControlMcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcStormControlMcastEnable.setStatus("mandatory")


class _RcStormControlDlfEnable_Type(EnableVar):
    """Custom type rcStormControlDlfEnable based on EnableVar"""
    defaultValue = 2


_RcStormControlDlfEnable_Type.__name__ = "EnableVar"
_RcStormControlDlfEnable_Object = MibScalar
rcStormControlDlfEnable = _RcStormControlDlfEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 4),
    _RcStormControlDlfEnable_Type()
)
rcStormControlDlfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcStormControlDlfEnable.setStatus("mandatory")


class _RcStormControlpps_Type(Integer32):
    """Custom type rcStormControlpps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 262143),
    )


_RcStormControlpps_Type.__name__ = "Integer32"
_RcStormControlpps_Object = MibScalar
rcStormControlpps = _RcStormControlpps_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 5),
    _RcStormControlpps_Type()
)
rcStormControlpps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcStormControlpps.setStatus("mandatory")
if mibBuilder.loadTexts:
    rcStormControlpps.setUnits("pps")


class _RcStormControlbps_Type(Integer32):
    """Custom type rcStormControlbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1073741823),
    )


_RcStormControlbps_Type.__name__ = "Integer32"
_RcStormControlbps_Object = MibScalar
rcStormControlbps = _RcStormControlbps_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 6),
    _RcStormControlbps_Type()
)
rcStormControlbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcStormControlbps.setStatus("mandatory")
if mibBuilder.loadTexts:
    rcStormControlbps.setUnits("bps")


class _RcStormControlRatio_Type(Integer32):
    """Custom type rcStormControlRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RcStormControlRatio_Type.__name__ = "Integer32"
_RcStormControlRatio_Object = MibScalar
rcStormControlRatio = _RcStormControlRatio_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 7),
    _RcStormControlRatio_Type()
)
rcStormControlRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcStormControlRatio.setStatus("mandatory")
if mibBuilder.loadTexts:
    rcStormControlRatio.setUnits("percent")


class _RcStormControlBurst_Type(Integer32):
    """Custom type rcStormControlBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_RcStormControlBurst_Type.__name__ = "Integer32"
_RcStormControlBurst_Object = MibScalar
rcStormControlBurst = _RcStormControlBurst_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 8),
    _RcStormControlBurst_Type()
)
rcStormControlBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcStormControlBurst.setStatus("mandatory")
if mibBuilder.loadTexts:
    rcStormControlBurst.setUnits("kB")


class _RcStpEnable_Type(EnableVar):
    """Custom type rcStpEnable based on EnableVar"""
    defaultValue = 1


_RcStpEnable_Type.__name__ = "EnableVar"
_RcStpEnable_Object = MibScalar
rcStpEnable = _RcStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 9),
    _RcStpEnable_Type()
)
rcStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcStpEnable.setStatus("mandatory")


class _RcSvlEnable_Type(EnableVar):
    """Custom type rcSvlEnable based on EnableVar"""
    defaultValue = 2


_RcSvlEnable_Type.__name__ = "EnableVar"
_RcSvlEnable_Object = MibScalar
rcSvlEnable = _RcSvlEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 10),
    _RcSvlEnable_Type()
)
rcSvlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcSvlEnable.setStatus("mandatory")


class _RcGarpEnable_Type(EnableVar):
    """Custom type rcGarpEnable based on EnableVar"""
    defaultValue = 2


_RcGarpEnable_Type.__name__ = "EnableVar"
_RcGarpEnable_Object = MibScalar
rcGarpEnable = _RcGarpEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 11),
    _RcGarpEnable_Type()
)
rcGarpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcGarpEnable.setStatus("mandatory")


class _RcLacpEnable_Type(EnableVar):
    """Custom type rcLacpEnable based on EnableVar"""
    defaultValue = 2


_RcLacpEnable_Type.__name__ = "EnableVar"
_RcLacpEnable_Object = MibScalar
rcLacpEnable = _RcLacpEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 12),
    _RcLacpEnable_Type()
)
rcLacpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLacpEnable.setStatus("mandatory")


class _RcVlanSpaceNum_Type(Integer32):
    """Custom type rcVlanSpaceNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4093),
    )


_RcVlanSpaceNum_Type.__name__ = "Integer32"
_RcVlanSpaceNum_Object = MibScalar
rcVlanSpaceNum = _RcVlanSpaceNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 13),
    _RcVlanSpaceNum_Type()
)
rcVlanSpaceNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcVlanSpaceNum.setStatus("obsolete")


class _RcPvidSpaceNum_Type(Integer32):
    """Custom type rcPvidSpaceNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4093),
    )


_RcPvidSpaceNum_Type.__name__ = "Integer32"
_RcPvidSpaceNum_Object = MibScalar
rcPvidSpaceNum = _RcPvidSpaceNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 14),
    _RcPvidSpaceNum_Type()
)
rcPvidSpaceNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPvidSpaceNum.setStatus("obsolete")


class _RcLoopbackDetectInterval_Type(Integer32):
    """Custom type rcLoopbackDetectInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcLoopbackDetectInterval_Type.__name__ = "Integer32"
_RcLoopbackDetectInterval_Object = MibScalar
rcLoopbackDetectInterval = _RcLoopbackDetectInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 15),
    _RcLoopbackDetectInterval_Type()
)
rcLoopbackDetectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLoopbackDetectInterval.setStatus("current")
if mibBuilder.loadTexts:
    rcLoopbackDetectInterval.setUnits("second")


class _RcArpAgingTime_Type(Integer32):
    """Custom type rcArpAgingTime based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RcArpAgingTime_Type.__name__ = "Integer32"
_RcArpAgingTime_Object = MibScalar
rcArpAgingTime = _RcArpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 16),
    _RcArpAgingTime_Type()
)
rcArpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcArpAgingTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    rcArpAgingTime.setUnits("second")
_RcBpduTransPorts_Type = PortList
_RcBpduTransPorts_Object = MibScalar
rcBpduTransPorts = _RcBpduTransPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 17),
    _RcBpduTransPorts_Type()
)
rcBpduTransPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcBpduTransPorts.setStatus("current")
_RcDot1xTransPorts_Type = PortList
_RcDot1xTransPorts_Object = MibScalar
rcDot1xTransPorts = _RcDot1xTransPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 18),
    _RcDot1xTransPorts_Type()
)
rcDot1xTransPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDot1xTransPorts.setStatus("current")
_RcLacpTransPorts_Type = PortList
_RcLacpTransPorts_Object = MibScalar
rcLacpTransPorts = _RcLacpTransPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 19),
    _RcLacpTransPorts_Type()
)
rcLacpTransPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLacpTransPorts.setStatus("current")
_RcGarpTransPorts_Type = PortList
_RcGarpTransPorts_Object = MibScalar
rcGarpTransPorts = _RcGarpTransPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 20),
    _RcGarpTransPorts_Type()
)
rcGarpTransPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcGarpTransPorts.setStatus("current")
_RcGmrpTransPorts_Type = PortList
_RcGmrpTransPorts_Object = MibScalar
rcGmrpTransPorts = _RcGmrpTransPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 21),
    _RcGmrpTransPorts_Type()
)
rcGmrpTransPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcGmrpTransPorts.setStatus("current")
_RcGvrpTransPorts_Type = PortList
_RcGvrpTransPorts_Object = MibScalar
rcGvrpTransPorts = _RcGvrpTransPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 22),
    _RcGvrpTransPorts_Type()
)
rcGvrpTransPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcGvrpTransPorts.setStatus("current")


class _RcIpRouting_Type(Integer32):
    """Custom type rcIpRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("startIpRouting", 1),
          ("stopIpRouting", 2))
    )


_RcIpRouting_Type.__name__ = "Integer32"
_RcIpRouting_Object = MibScalar
rcIpRouting = _RcIpRouting_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 23),
    _RcIpRouting_Type()
)
rcIpRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpRouting.setStatus("current")


class _RcStaticRouteDistance_Type(Integer32):
    """Custom type rcStaticRouteDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RcStaticRouteDistance_Type.__name__ = "Integer32"
_RcStaticRouteDistance_Object = MibScalar
rcStaticRouteDistance = _RcStaticRouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 24),
    _RcStaticRouteDistance_Type()
)
rcStaticRouteDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcStaticRouteDistance.setStatus("current")
_RcFastRoute_Type = TruthValue
_RcFastRoute_Object = MibScalar
rcFastRoute = _RcFastRoute_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 25),
    _RcFastRoute_Type()
)
rcFastRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcFastRoute.setStatus("current")
_RcDlfForwardingEnable_Type = EnableVar
_RcDlfForwardingEnable_Object = MibScalar
rcDlfForwardingEnable = _RcDlfForwardingEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 26),
    _RcDlfForwardingEnable_Type()
)
rcDlfForwardingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDlfForwardingEnable.setStatus("mandatory")


class _RcLoopbackDetectVlan_Type(Integer32):
    """Custom type rcLoopbackDetectVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcLoopbackDetectVlan_Type.__name__ = "Integer32"
_RcLoopbackDetectVlan_Object = MibScalar
rcLoopbackDetectVlan = _RcLoopbackDetectVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 27),
    _RcLoopbackDetectVlan_Type()
)
rcLoopbackDetectVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLoopbackDetectVlan.setStatus("mandatory")
_RcLoopbackDetectDestAddr_Type = MacAddress
_RcLoopbackDetectDestAddr_Object = MibScalar
rcLoopbackDetectDestAddr = _RcLoopbackDetectDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 28),
    _RcLoopbackDetectDestAddr_Type()
)
rcLoopbackDetectDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLoopbackDetectDestAddr.setStatus("mandatory")


class _RcMaxAllowedFrameLength_Type(Integer32):
    """Custom type rcMaxAllowedFrameLength based on Integer32"""
    defaultValue = 1522

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 65535),
    )


_RcMaxAllowedFrameLength_Type.__name__ = "Integer32"
_RcMaxAllowedFrameLength_Object = MibScalar
rcMaxAllowedFrameLength = _RcMaxAllowedFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 29),
    _RcMaxAllowedFrameLength_Type()
)
rcMaxAllowedFrameLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMaxAllowedFrameLength.setStatus("mandatory")


class _RcSvlDefaultVlan_Type(Integer32):
    """Custom type rcSvlDefaultVlan based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcSvlDefaultVlan_Type.__name__ = "Integer32"
_RcSvlDefaultVlan_Object = MibScalar
rcSvlDefaultVlan = _RcSvlDefaultVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 30),
    _RcSvlDefaultVlan_Type()
)
rcSvlDefaultVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcSvlDefaultVlan.setStatus("mandatory")


class _RcTelnetMaxSessions_Type(Integer32):
    """Custom type rcTelnetMaxSessions based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_RcTelnetMaxSessions_Type.__name__ = "Integer32"
_RcTelnetMaxSessions_Object = MibScalar
rcTelnetMaxSessions = _RcTelnetMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 31),
    _RcTelnetMaxSessions_Type()
)
rcTelnetMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTelnetMaxSessions.setStatus("current")
_RcTelnetAcceptPorts_Type = PortList
_RcTelnetAcceptPorts_Object = MibScalar
rcTelnetAcceptPorts = _RcTelnetAcceptPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 32),
    _RcTelnetAcceptPorts_Type()
)
rcTelnetAcceptPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTelnetAcceptPorts.setStatus("current")
_RcVlanMacLearning_Type = Vlanset
_RcVlanMacLearning_Object = MibScalar
rcVlanMacLearning = _RcVlanMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 33),
    _RcVlanMacLearning_Type()
)
rcVlanMacLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcVlanMacLearning.setStatus("current")
_RcConsoleEnable_Type = EnableVar
_RcConsoleEnable_Object = MibScalar
rcConsoleEnable = _RcConsoleEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 34),
    _RcConsoleEnable_Type()
)
rcConsoleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcConsoleEnable.setStatus("current")
_RcMacTrapEnable_Type = EnableVar
_RcMacTrapEnable_Object = MibScalar
rcMacTrapEnable = _RcMacTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 35),
    _RcMacTrapEnable_Type()
)
rcMacTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMacTrapEnable.setStatus("current")
_RcMacMoveEnable_Type = EnableVar
_RcMacMoveEnable_Object = MibScalar
rcMacMoveEnable = _RcMacMoveEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 36),
    _RcMacMoveEnable_Type()
)
rcMacMoveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMacMoveEnable.setStatus("current")
_RcMacMoveLastPortIndex_Type = Integer32
_RcMacMoveLastPortIndex_Object = MibScalar
rcMacMoveLastPortIndex = _RcMacMoveLastPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 37),
    _RcMacMoveLastPortIndex_Type()
)
rcMacMoveLastPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMacMoveLastPortIndex.setStatus("current")
_RcMacMoveLastMacaddress_Type = MacAddress
_RcMacMoveLastMacaddress_Object = MibScalar
rcMacMoveLastMacaddress = _RcMacMoveLastMacaddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 38),
    _RcMacMoveLastMacaddress_Type()
)
rcMacMoveLastMacaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMacMoveLastMacaddress.setStatus("current")


class _RcMacMoveLastVlan_Type(Integer32):
    """Custom type rcMacMoveLastVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcMacMoveLastVlan_Type.__name__ = "Integer32"
_RcMacMoveLastVlan_Object = MibScalar
rcMacMoveLastVlan = _RcMacMoveLastVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 3, 39),
    _RcMacMoveLastVlan_Type()
)
rcMacMoveLastVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcMacMoveLastVlan.setStatus("current")
_RcPortInfoConfig_ObjectIdentity = ObjectIdentity
rcPortInfoConfig = _RcPortInfoConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4)
)
_RcPortTable_Object = MibTable
rcPortTable = _RcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    rcPortTable.setStatus("current")
_RcPortEntry_Object = MibTableRow
rcPortEntry = _RcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1)
)
rcPortEntry.setIndexNames(
    (0, "SWITCH-SYSTEM-MIB", "rcPortIndex"),
)
if mibBuilder.loadTexts:
    rcPortEntry.setStatus("current")
_RcPortIndex_Type = Integer32
_RcPortIndex_Object = MibTableColumn
rcPortIndex = _RcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 1),
    _RcPortIndex_Type()
)
rcPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortIndex.setStatus("current")


class _RcPortType_Type(Integer32):
    """Custom type rcPortType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("inexistence", 0),
          ("fx-DulMode-1000M", 1),
          ("tx-1000M", 2),
          ("fx-SigMode-1000M", 3),
          ("fx-DulMode-100M", 4),
          ("fx-SigMode-100M", 5),
          ("tx-100M", 6),
          ("px-1000M", 7))
    )


_RcPortType_Type.__name__ = "Integer32"
_RcPortType_Object = MibTableColumn
rcPortType = _RcPortType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 2),
    _RcPortType_Type()
)
rcPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortType.setStatus("current")
_RcSlotTableIndex_Type = Integer32
_RcSlotTableIndex_Object = MibTableColumn
rcSlotTableIndex = _RcSlotTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 3),
    _RcSlotTableIndex_Type()
)
rcSlotTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSlotTableIndex.setStatus("current")
_RcSlotPortIndex_Type = Integer32
_RcSlotPortIndex_Object = MibTableColumn
rcSlotPortIndex = _RcSlotPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 4),
    _RcSlotPortIndex_Type()
)
rcSlotPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSlotPortIndex.setStatus("current")


class _RcPortAdminStatus_Type(Integer32):
    """Custom type rcPortAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_RcPortAdminStatus_Type.__name__ = "Integer32"
_RcPortAdminStatus_Object = MibTableColumn
rcPortAdminStatus = _RcPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 5),
    _RcPortAdminStatus_Type()
)
rcPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortAdminStatus.setStatus("current")


class _RcPortOperStatus_Type(Integer32):
    """Custom type rcPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_RcPortOperStatus_Type.__name__ = "Integer32"
_RcPortOperStatus_Object = MibTableColumn
rcPortOperStatus = _RcPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 6),
    _RcPortOperStatus_Type()
)
rcPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortOperStatus.setStatus("current")


class _RcPortDuplexSpeedSet_Type(Integer32):
    """Custom type rcPortDuplexSpeedSet based on Integer32"""
    defaultValue = 1

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
        *(("autonegotiate", 1),
          ("half-10", 2),
          ("full-10", 3),
          ("half-100", 4),
          ("full-100", 5),
          ("half-1000", 6),
          ("full-1000", 7))
    )


_RcPortDuplexSpeedSet_Type.__name__ = "Integer32"
_RcPortDuplexSpeedSet_Object = MibTableColumn
rcPortDuplexSpeedSet = _RcPortDuplexSpeedSet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 7),
    _RcPortDuplexSpeedSet_Type()
)
rcPortDuplexSpeedSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortDuplexSpeedSet.setStatus("current")


class _RcPortDuplexSpeedGet_Type(Integer32):
    """Custom type rcPortDuplexSpeedGet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              99)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("half-10", 2),
          ("full-10", 3),
          ("half-100", 4),
          ("full-100", 5),
          ("half-1000", 6),
          ("full-1000", 7),
          ("illegal", 99))
    )


_RcPortDuplexSpeedGet_Type.__name__ = "Integer32"
_RcPortDuplexSpeedGet_Object = MibTableColumn
rcPortDuplexSpeedGet = _RcPortDuplexSpeedGet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 8),
    _RcPortDuplexSpeedGet_Type()
)
rcPortDuplexSpeedGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortDuplexSpeedGet.setStatus("current")


class _RcPortFlowControlEnable_Type(EnableVar):
    """Custom type rcPortFlowControlEnable based on EnableVar"""
    defaultValue = 2


_RcPortFlowControlEnable_Type.__name__ = "EnableVar"
_RcPortFlowControlEnable_Object = MibTableColumn
rcPortFlowControlEnable = _RcPortFlowControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 9),
    _RcPortFlowControlEnable_Type()
)
rcPortFlowControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortFlowControlEnable.setStatus("mandatory")


class _RcPortMacLearningEnable_Type(EnableVar):
    """Custom type rcPortMacLearningEnable based on EnableVar"""
    defaultValue = 1


_RcPortMacLearningEnable_Type.__name__ = "EnableVar"
_RcPortMacLearningEnable_Object = MibTableColumn
rcPortMacLearningEnable = _RcPortMacLearningEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 10),
    _RcPortMacLearningEnable_Type()
)
rcPortMacLearningEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortMacLearningEnable.setStatus("mandatory")


class _RcPortMacThreshold_Type(Integer32):
    """Custom type rcPortMacThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_RcPortMacThreshold_Type.__name__ = "Integer32"
_RcPortMacThreshold_Object = MibTableColumn
rcPortMacThreshold = _RcPortMacThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 11),
    _RcPortMacThreshold_Type()
)
rcPortMacThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortMacThreshold.setStatus("mandatory")


class _RcPortStormControlBcastEnable_Type(EnableVar):
    """Custom type rcPortStormControlBcastEnable based on EnableVar"""
    defaultValue = 2


_RcPortStormControlBcastEnable_Type.__name__ = "EnableVar"
_RcPortStormControlBcastEnable_Object = MibTableColumn
rcPortStormControlBcastEnable = _RcPortStormControlBcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 12),
    _RcPortStormControlBcastEnable_Type()
)
rcPortStormControlBcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortStormControlBcastEnable.setStatus("mandatory")


class _RcPortStormControlMcastEnable_Type(EnableVar):
    """Custom type rcPortStormControlMcastEnable based on EnableVar"""
    defaultValue = 2


_RcPortStormControlMcastEnable_Type.__name__ = "EnableVar"
_RcPortStormControlMcastEnable_Object = MibTableColumn
rcPortStormControlMcastEnable = _RcPortStormControlMcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 13),
    _RcPortStormControlMcastEnable_Type()
)
rcPortStormControlMcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortStormControlMcastEnable.setStatus("mandatory")


class _RcPortStormControlDlfEnable_Type(EnableVar):
    """Custom type rcPortStormControlDlfEnable based on EnableVar"""
    defaultValue = 2


_RcPortStormControlDlfEnable_Type.__name__ = "EnableVar"
_RcPortStormControlDlfEnable_Object = MibTableColumn
rcPortStormControlDlfEnable = _RcPortStormControlDlfEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 14),
    _RcPortStormControlDlfEnable_Type()
)
rcPortStormControlDlfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortStormControlDlfEnable.setStatus("mandatory")


class _RcPortStormControlBurst_Type(Integer32):
    """Custom type rcPortStormControlBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_RcPortStormControlBurst_Type.__name__ = "Integer32"
_RcPortStormControlBurst_Object = MibTableColumn
rcPortStormControlBurst = _RcPortStormControlBurst_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 15),
    _RcPortStormControlBurst_Type()
)
rcPortStormControlBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortStormControlBurst.setStatus("mandatory")
if mibBuilder.loadTexts:
    rcPortStormControlBurst.setUnits("kB")


class _RcPortStormControlLimit_Type(Integer32):
    """Custom type rcPortStormControlLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2621430),
    )


_RcPortStormControlLimit_Type.__name__ = "Integer32"
_RcPortStormControlLimit_Object = MibTableColumn
rcPortStormControlLimit = _RcPortStormControlLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 16),
    _RcPortStormControlLimit_Type()
)
rcPortStormControlLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortStormControlLimit.setStatus("mandatory")
if mibBuilder.loadTexts:
    rcPortStormControlLimit.setUnits("pps")


class _RcPortStormControlLimitRatio_Type(Integer32):
    """Custom type rcPortStormControlLimitRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RcPortStormControlLimitRatio_Type.__name__ = "Integer32"
_RcPortStormControlLimitRatio_Object = MibTableColumn
rcPortStormControlLimitRatio = _RcPortStormControlLimitRatio_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 17),
    _RcPortStormControlLimitRatio_Type()
)
rcPortStormControlLimitRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortStormControlLimitRatio.setStatus("mandatory")
if mibBuilder.loadTexts:
    rcPortStormControlLimitRatio.setUnits("percent")


class _RcPortDefaultPriority_Type(Integer32):
    """Custom type rcPortDefaultPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RcPortDefaultPriority_Type.__name__ = "Integer32"
_RcPortDefaultPriority_Object = MibTableColumn
rcPortDefaultPriority = _RcPortDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 18),
    _RcPortDefaultPriority_Type()
)
rcPortDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortDefaultPriority.setStatus("mandatory")
_RcPortLoopbackDetectEnable_Type = EnableVar
_RcPortLoopbackDetectEnable_Object = MibTableColumn
rcPortLoopbackDetectEnable = _RcPortLoopbackDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 19),
    _RcPortLoopbackDetectEnable_Type()
)
rcPortLoopbackDetectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortLoopbackDetectEnable.setStatus("current")
_RcPortLoopbackDetectSrcPort_Type = Integer32
_RcPortLoopbackDetectSrcPort_Object = MibTableColumn
rcPortLoopbackDetectSrcPort = _RcPortLoopbackDetectSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 20),
    _RcPortLoopbackDetectSrcPort_Type()
)
rcPortLoopbackDetectSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortLoopbackDetectSrcPort.setStatus("current")


class _RcPortProtected_Type(EnableVar):
    """Custom type rcPortProtected based on EnableVar"""
    defaultValue = 2


_RcPortProtected_Type.__name__ = "EnableVar"
_RcPortProtected_Object = MibTableColumn
rcPortProtected = _RcPortProtected_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 21),
    _RcPortProtected_Type()
)
rcPortProtected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortProtected.setStatus("mandatory")


class _RcPortFlowControlRecvEnable_Type(EnableVar):
    """Custom type rcPortFlowControlRecvEnable based on EnableVar"""
    defaultValue = 2


_RcPortFlowControlRecvEnable_Type.__name__ = "EnableVar"
_RcPortFlowControlRecvEnable_Object = MibTableColumn
rcPortFlowControlRecvEnable = _RcPortFlowControlRecvEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 22),
    _RcPortFlowControlRecvEnable_Type()
)
rcPortFlowControlRecvEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortFlowControlRecvEnable.setStatus("mandatory")


class _RcPortFlowControlSendEnable_Type(EnableVar):
    """Custom type rcPortFlowControlSendEnable based on EnableVar"""
    defaultValue = 2


_RcPortFlowControlSendEnable_Type.__name__ = "EnableVar"
_RcPortFlowControlSendEnable_Object = MibTableColumn
rcPortFlowControlSendEnable = _RcPortFlowControlSendEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 23),
    _RcPortFlowControlSendEnable_Type()
)
rcPortFlowControlSendEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortFlowControlSendEnable.setStatus("mandatory")


class _RcPortFlowControlRecvStatus_Type(EnableVar):
    """Custom type rcPortFlowControlRecvStatus based on EnableVar"""
    defaultValue = 2


_RcPortFlowControlRecvStatus_Type.__name__ = "EnableVar"
_RcPortFlowControlRecvStatus_Object = MibTableColumn
rcPortFlowControlRecvStatus = _RcPortFlowControlRecvStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 24),
    _RcPortFlowControlRecvStatus_Type()
)
rcPortFlowControlRecvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortFlowControlRecvStatus.setStatus("mandatory")


class _RcPortFlowControlSendStatus_Type(EnableVar):
    """Custom type rcPortFlowControlSendStatus based on EnableVar"""
    defaultValue = 2


_RcPortFlowControlSendStatus_Type.__name__ = "EnableVar"
_RcPortFlowControlSendStatus_Object = MibTableColumn
rcPortFlowControlSendStatus = _RcPortFlowControlSendStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 25),
    _RcPortFlowControlSendStatus_Type()
)
rcPortFlowControlSendStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortFlowControlSendStatus.setStatus("mandatory")


class _RcPortLoopbackDetectDownTime_Type(Integer32):
    """Custom type rcPortLoopbackDetectDownTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcPortLoopbackDetectDownTime_Type.__name__ = "Integer32"
_RcPortLoopbackDetectDownTime_Object = MibTableColumn
rcPortLoopbackDetectDownTime = _RcPortLoopbackDetectDownTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 26),
    _RcPortLoopbackDetectDownTime_Type()
)
rcPortLoopbackDetectDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortLoopbackDetectDownTime.setStatus("mandatory")


class _RcPortMediaAttachType_Type(Integer32):
    """Custom type rcPortMediaAttachType based on Integer32"""
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
        *(("copper", 1),
          ("fiber", 2),
          ("card", 3),
          ("sfp", 4),
          ("combo-sfp", 5),
          ("combo-copper", 6))
    )


_RcPortMediaAttachType_Type.__name__ = "Integer32"
_RcPortMediaAttachType_Object = MibTableColumn
rcPortMediaAttachType = _RcPortMediaAttachType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 27),
    _RcPortMediaAttachType_Type()
)
rcPortMediaAttachType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortMediaAttachType.setStatus("current")


class _RcPortMediaAttachCapability_Type(Integer32):
    """Custom type rcPortMediaAttachCapability based on Integer32"""
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
        *(("inexistence", 0),
          ("copper-1000M", 1),
          ("copper-100M", 2),
          ("fiber-1000M", 3),
          ("fiber-100M", 4),
          ("unlimited", 5))
    )


_RcPortMediaAttachCapability_Type.__name__ = "Integer32"
_RcPortMediaAttachCapability_Object = MibTableColumn
rcPortMediaAttachCapability = _RcPortMediaAttachCapability_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 28),
    _RcPortMediaAttachCapability_Type()
)
rcPortMediaAttachCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortMediaAttachCapability.setStatus("current")


class _RcPortMDIXMode_Type(Integer32):
    """Custom type rcPortMDIXMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("xover", 2),
          ("auto", 3))
    )


_RcPortMDIXMode_Type.__name__ = "Integer32"
_RcPortMDIXMode_Object = MibTableColumn
rcPortMDIXMode = _RcPortMDIXMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 29),
    _RcPortMDIXMode_Type()
)
rcPortMDIXMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortMDIXMode.setStatus("current")


class _RcPortMDIXStatus_Type(Integer32):
    """Custom type rcPortMDIXStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("xover", 2))
    )


_RcPortMDIXStatus_Type.__name__ = "Integer32"
_RcPortMDIXStatus_Object = MibTableColumn
rcPortMDIXStatus = _RcPortMDIXStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 30),
    _RcPortMDIXStatus_Type()
)
rcPortMDIXStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortMDIXStatus.setStatus("current")
_RcportDiscPKts_Type = Counter32
_RcportDiscPKts_Object = MibTableColumn
rcportDiscPKts = _RcportDiscPKts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 31),
    _RcportDiscPKts_Type()
)
rcportDiscPKts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcportDiscPKts.setStatus("current")


class _RcPortMacThresholdVlan_Type(Integer32):
    """Custom type rcPortMacThresholdVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_RcPortMacThresholdVlan_Type.__name__ = "Integer32"
_RcPortMacThresholdVlan_Object = MibTableColumn
rcPortMacThresholdVlan = _RcPortMacThresholdVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 1, 1, 32),
    _RcPortMacThresholdVlan_Type()
)
rcPortMacThresholdVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPortMacThresholdVlan.setStatus("mandatory")
_RcComboPortTable_Object = MibTable
rcComboPortTable = _RcComboPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    rcComboPortTable.setStatus("current")
_RcComboPortEntry_Object = MibTableRow
rcComboPortEntry = _RcComboPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 2, 1)
)
rcComboPortEntry.setIndexNames(
    (0, "SWITCH-SYSTEM-MIB", "rcComboIndex"),
    (0, "SWITCH-SYSTEM-MIB", "rcComboPortIndex"),
)
if mibBuilder.loadTexts:
    rcComboPortEntry.setStatus("current")
_RcComboIndex_Type = Integer32
_RcComboIndex_Object = MibTableColumn
rcComboIndex = _RcComboIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 2, 1, 1),
    _RcComboIndex_Type()
)
rcComboIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcComboIndex.setStatus("current")
_RcComboPortIndex_Type = Integer32
_RcComboPortIndex_Object = MibTableColumn
rcComboPortIndex = _RcComboPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 2, 1, 2),
    _RcComboPortIndex_Type()
)
rcComboPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcComboPortIndex.setStatus("current")


class _RcComboPortType_Type(Integer32):
    """Custom type rcComboPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("inexistence", 0),
          ("fx-DulMode-1000M", 1),
          ("tx-1000M", 2),
          ("fx-SigMode-1000M", 3),
          ("fx-DulMode-100M", 4),
          ("fx-SigMode-100M", 5),
          ("tx-100M", 6))
    )


_RcComboPortType_Type.__name__ = "Integer32"
_RcComboPortType_Object = MibTableColumn
rcComboPortType = _RcComboPortType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 2, 1, 3),
    _RcComboPortType_Type()
)
rcComboPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcComboPortType.setStatus("current")


class _RcComboPortMediaAttachType_Type(Integer32):
    """Custom type rcComboPortMediaAttachType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sfp", 1),
          ("copper", 2))
    )


_RcComboPortMediaAttachType_Type.__name__ = "Integer32"
_RcComboPortMediaAttachType_Object = MibTableColumn
rcComboPortMediaAttachType = _RcComboPortMediaAttachType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 2, 1, 4),
    _RcComboPortMediaAttachType_Type()
)
rcComboPortMediaAttachType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcComboPortMediaAttachType.setStatus("current")


class _RcComboPortActiveStatus_Type(Integer32):
    """Custom type rcComboPortActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RcComboPortActiveStatus_Type.__name__ = "Integer32"
_RcComboPortActiveStatus_Object = MibTableColumn
rcComboPortActiveStatus = _RcComboPortActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 2, 1, 5),
    _RcComboPortActiveStatus_Type()
)
rcComboPortActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcComboPortActiveStatus.setStatus("current")


class _RcComboPortMediaAttachCapability_Type(Integer32):
    """Custom type rcComboPortMediaAttachCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inexistence", 0),
          ("copper-1000M", 1),
          ("copper-100M", 2),
          ("fiber-1000M", 3),
          ("fiber-100M", 4))
    )


_RcComboPortMediaAttachCapability_Type.__name__ = "Integer32"
_RcComboPortMediaAttachCapability_Object = MibTableColumn
rcComboPortMediaAttachCapability = _RcComboPortMediaAttachCapability_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 4, 2, 1, 6),
    _RcComboPortMediaAttachCapability_Type()
)
rcComboPortMediaAttachCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcComboPortMediaAttachCapability.setStatus("current")
_RcLoopbackTrap_ObjectIdentity = ObjectIdentity
rcLoopbackTrap = _RcLoopbackTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 5)
)
_RcPorConnectorChangeTrap_ObjectIdentity = ObjectIdentity
rcPorConnectorChangeTrap = _RcPorConnectorChangeTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 6)
)
_RcMacMoveTrap_ObjectIdentity = ObjectIdentity
rcMacMoveTrap = _RcMacMoveTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 8)
)

# Managed Objects groups


# Notification objects

rcLoopbackLinkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 5, 1)
)
rcLoopbackLinkUpTrap.setObjects(
    ("SWITCH-SYSTEM-MIB", "rcPortIndex")
)
if mibBuilder.loadTexts:
    rcLoopbackLinkUpTrap.setStatus(
        "current"
    )

rcLoopbackLinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 5, 2)
)
rcLoopbackLinkDownTrap.setObjects(
      *(("SWITCH-SYSTEM-MIB", "rcPortIndex"),
        ("SWITCH-SYSTEM-MIB", "rcPortLoopbackDetectSrcPort"),
        ("SWITCH-SYSTEM-MIB", "rcPortLoopbackDetectDownTime"))
)
if mibBuilder.loadTexts:
    rcLoopbackLinkDownTrap.setStatus(
        "current"
    )

rcPortConnectorInsertTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 6, 1)
)
rcPortConnectorInsertTrap.setObjects(
      *(("SWITCH-SYSTEM-MIB", "rcPortIndex"),
        ("SWITCH-SYSTEM-MIB", "rcPortType"),
        ("SWITCH-SYSTEM-MIB", "rcPortMediaAttachType"),
        ("SWITCH-SYSTEM-MIB", "rcPortMediaAttachCapability"))
)
if mibBuilder.loadTexts:
    rcPortConnectorInsertTrap.setStatus(
        "current"
    )

rcPortConnectorRemoveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 6, 2)
)
rcPortConnectorRemoveTrap.setObjects(
      *(("SWITCH-SYSTEM-MIB", "rcPortIndex"),
        ("SWITCH-SYSTEM-MIB", "rcPortType"),
        ("SWITCH-SYSTEM-MIB", "rcPortMediaAttachType"),
        ("SWITCH-SYSTEM-MIB", "rcPortMediaAttachCapability"))
)
if mibBuilder.loadTexts:
    rcPortConnectorRemoveTrap.setStatus(
        "current"
    )

rcMacMoveVioTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 1, 8, 1)
)
rcMacMoveVioTrap.setObjects(
      *(("SWITCH-SYSTEM-MIB", "rcMacMoveLastPortIndex"),
        ("SWITCH-SYSTEM-MIB", "rcMacMoveLastMacaddress"),
        ("SWITCH-SYSTEM-MIB", "rcMacMoveLastVlan"))
)
if mibBuilder.loadTexts:
    rcMacMoveVioTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-SYSTEM-MIB",
    **{"rcSystem": rcSystem,
       "rcSwitchInformation": rcSwitchInformation,
       "rcSwitchRoseVersion": rcSwitchRoseVersion,
       "rcSwitchHardwareVersion": rcSwitchHardwareVersion,
       "rcSwitchServiceInfo": rcSwitchServiceInfo,
       "rcSwitchLastErrorCode": rcSwitchLastErrorCode,
       "rcSwitchMaxPhysicalPortNum": rcSwitchMaxPhysicalPortNum,
       "rcSwitchMaxAggregationPortNum": rcSwitchMaxAggregationPortNum,
       "rcSwitchMaxL3IpSubnetNum": rcSwitchMaxL3IpSubnetNum,
       "rcSwitchMacTableCapability": rcSwitchMacTableCapability,
       "rcSwitchMacAddress": rcSwitchMacAddress,
       "rcSwitchVlanSpaceSize": rcSwitchVlanSpaceSize,
       "rcSwitchPvidSpaceSize": rcSwitchPvidSpaceSize,
       "rcSwitchDefaultVlan": rcSwitchDefaultVlan,
       "rcSwitchBootstrapVersion": rcSwitchBootstrapVersion,
       "rcSwitchSerialNumber": rcSwitchSerialNumber,
       "rcSwitchFpgaVersion": rcSwitchFpgaVersion,
       "rcSwitchProductVersion": rcSwitchProductVersion,
       "rcSwitchCmpAbName": rcSwitchCmpAbName,
       "rcSwitchCmpFullName": rcSwitchCmpFullName,
       "rcSwitchDeviceName": rcSwitchDeviceName,
       "rcSlotInformation": rcSlotInformation,
       "rcSlotNum": rcSlotNum,
       "rcSlotStateTable": rcSlotStateTable,
       "rcSlotStateEntry": rcSlotStateEntry,
       "rcSlotIndex": rcSlotIndex,
       "rcSlotPortStart": rcSlotPortStart,
       "rcSlotPortNum": rcSlotPortNum,
       "rcSlotType": rcSlotType,
       "rcSwitchConfig": rcSwitchConfig,
       "rcMacAgingTime": rcMacAgingTime,
       "rcStormControlBcastEnable": rcStormControlBcastEnable,
       "rcStormControlMcastEnable": rcStormControlMcastEnable,
       "rcStormControlDlfEnable": rcStormControlDlfEnable,
       "rcStormControlpps": rcStormControlpps,
       "rcStormControlbps": rcStormControlbps,
       "rcStormControlRatio": rcStormControlRatio,
       "rcStormControlBurst": rcStormControlBurst,
       "rcStpEnable": rcStpEnable,
       "rcSvlEnable": rcSvlEnable,
       "rcGarpEnable": rcGarpEnable,
       "rcLacpEnable": rcLacpEnable,
       "rcVlanSpaceNum": rcVlanSpaceNum,
       "rcPvidSpaceNum": rcPvidSpaceNum,
       "rcLoopbackDetectInterval": rcLoopbackDetectInterval,
       "rcArpAgingTime": rcArpAgingTime,
       "rcBpduTransPorts": rcBpduTransPorts,
       "rcDot1xTransPorts": rcDot1xTransPorts,
       "rcLacpTransPorts": rcLacpTransPorts,
       "rcGarpTransPorts": rcGarpTransPorts,
       "rcGmrpTransPorts": rcGmrpTransPorts,
       "rcGvrpTransPorts": rcGvrpTransPorts,
       "rcIpRouting": rcIpRouting,
       "rcStaticRouteDistance": rcStaticRouteDistance,
       "rcFastRoute": rcFastRoute,
       "rcDlfForwardingEnable": rcDlfForwardingEnable,
       "rcLoopbackDetectVlan": rcLoopbackDetectVlan,
       "rcLoopbackDetectDestAddr": rcLoopbackDetectDestAddr,
       "rcMaxAllowedFrameLength": rcMaxAllowedFrameLength,
       "rcSvlDefaultVlan": rcSvlDefaultVlan,
       "rcTelnetMaxSessions": rcTelnetMaxSessions,
       "rcTelnetAcceptPorts": rcTelnetAcceptPorts,
       "rcVlanMacLearning": rcVlanMacLearning,
       "rcConsoleEnable": rcConsoleEnable,
       "rcMacTrapEnable": rcMacTrapEnable,
       "rcMacMoveEnable": rcMacMoveEnable,
       "rcMacMoveLastPortIndex": rcMacMoveLastPortIndex,
       "rcMacMoveLastMacaddress": rcMacMoveLastMacaddress,
       "rcMacMoveLastVlan": rcMacMoveLastVlan,
       "rcPortInfoConfig": rcPortInfoConfig,
       "rcPortTable": rcPortTable,
       "rcPortEntry": rcPortEntry,
       "rcPortIndex": rcPortIndex,
       "rcPortType": rcPortType,
       "rcSlotTableIndex": rcSlotTableIndex,
       "rcSlotPortIndex": rcSlotPortIndex,
       "rcPortAdminStatus": rcPortAdminStatus,
       "rcPortOperStatus": rcPortOperStatus,
       "rcPortDuplexSpeedSet": rcPortDuplexSpeedSet,
       "rcPortDuplexSpeedGet": rcPortDuplexSpeedGet,
       "rcPortFlowControlEnable": rcPortFlowControlEnable,
       "rcPortMacLearningEnable": rcPortMacLearningEnable,
       "rcPortMacThreshold": rcPortMacThreshold,
       "rcPortStormControlBcastEnable": rcPortStormControlBcastEnable,
       "rcPortStormControlMcastEnable": rcPortStormControlMcastEnable,
       "rcPortStormControlDlfEnable": rcPortStormControlDlfEnable,
       "rcPortStormControlBurst": rcPortStormControlBurst,
       "rcPortStormControlLimit": rcPortStormControlLimit,
       "rcPortStormControlLimitRatio": rcPortStormControlLimitRatio,
       "rcPortDefaultPriority": rcPortDefaultPriority,
       "rcPortLoopbackDetectEnable": rcPortLoopbackDetectEnable,
       "rcPortLoopbackDetectSrcPort": rcPortLoopbackDetectSrcPort,
       "rcPortProtected": rcPortProtected,
       "rcPortFlowControlRecvEnable": rcPortFlowControlRecvEnable,
       "rcPortFlowControlSendEnable": rcPortFlowControlSendEnable,
       "rcPortFlowControlRecvStatus": rcPortFlowControlRecvStatus,
       "rcPortFlowControlSendStatus": rcPortFlowControlSendStatus,
       "rcPortLoopbackDetectDownTime": rcPortLoopbackDetectDownTime,
       "rcPortMediaAttachType": rcPortMediaAttachType,
       "rcPortMediaAttachCapability": rcPortMediaAttachCapability,
       "rcPortMDIXMode": rcPortMDIXMode,
       "rcPortMDIXStatus": rcPortMDIXStatus,
       "rcportDiscPKts": rcportDiscPKts,
       "rcPortMacThresholdVlan": rcPortMacThresholdVlan,
       "rcComboPortTable": rcComboPortTable,
       "rcComboPortEntry": rcComboPortEntry,
       "rcComboIndex": rcComboIndex,
       "rcComboPortIndex": rcComboPortIndex,
       "rcComboPortType": rcComboPortType,
       "rcComboPortMediaAttachType": rcComboPortMediaAttachType,
       "rcComboPortActiveStatus": rcComboPortActiveStatus,
       "rcComboPortMediaAttachCapability": rcComboPortMediaAttachCapability,
       "rcLoopbackTrap": rcLoopbackTrap,
       "rcLoopbackLinkUpTrap": rcLoopbackLinkUpTrap,
       "rcLoopbackLinkDownTrap": rcLoopbackLinkDownTrap,
       "rcPorConnectorChangeTrap": rcPorConnectorChangeTrap,
       "rcPortConnectorInsertTrap": rcPortConnectorInsertTrap,
       "rcPortConnectorRemoveTrap": rcPortConnectorRemoveTrap,
       "rcMacMoveTrap": rcMacMoveTrap,
       "rcMacMoveVioTrap": rcMacMoveVioTrap}
)
