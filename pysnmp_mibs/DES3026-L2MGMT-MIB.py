# SNMP MIB module (DES3026-L2MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DES3026-L2MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:52:35 2025
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

(des3026,) = mibBuilder.importSymbols(
    "DLINK-SWPRIMGMT-MIB",
    "des3026")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

swL2MgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2)
)


# Types definitions



class VlanId(Integer32):
    """Custom type VlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )





class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )





class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwL2DevMgmt_ObjectIdentity = ObjectIdentity
swL2DevMgmt = _SwL2DevMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1)
)
_SwL2DevInfo_ObjectIdentity = ObjectIdentity
swL2DevInfo = _SwL2DevInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 1)
)


class _SwL2DevInfoFrontPanelLedStatus_Type(OctetString):
    """Custom type swL2DevInfoFrontPanelLedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwL2DevInfoFrontPanelLedStatus_Type.__name__ = "OctetString"
_SwL2DevInfoFrontPanelLedStatus_Object = MibScalar
swL2DevInfoFrontPanelLedStatus = _SwL2DevInfoFrontPanelLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 1, 5),
    _SwL2DevInfoFrontPanelLedStatus_Type()
)
swL2DevInfoFrontPanelLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2DevInfoFrontPanelLedStatus.setStatus("current")


class _SwL2Module_1_Type_Type(Integer32):
    """Custom type swL2Module_1_Type based on Integer32"""
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
        *(("none", 0),
          ("moduleType-DEM-301T", 1),
          ("moduleType-DEM-201F", 2),
          ("moduleType-DEM-301G", 3),
          ("moduleType-COMBA", 4),
          ("moduleType-DEM-201FL", 5))
    )


_SwL2Module_1_Type_Type.__name__ = "Integer32"
_SwL2Module_1_Type_Object = MibScalar
swL2Module_1_Type = _SwL2Module_1_Type_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 1, 6),
    _SwL2Module_1_Type_Type()
)
swL2Module_1_Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2Module_1_Type.setStatus("current")


class _SwL2Module_2_Type_Type(Integer32):
    """Custom type swL2Module_2_Type based on Integer32"""
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
        *(("none", 0),
          ("moduleType-DEM-301T", 1),
          ("moduleType-DEM-201F", 2),
          ("moduleType-DEM-301G", 3),
          ("moduleType-COMBA", 4),
          ("moduleType-DEM-201FL", 5))
    )


_SwL2Module_2_Type_Type.__name__ = "Integer32"
_SwL2Module_2_Type_Object = MibScalar
swL2Module_2_Type = _SwL2Module_2_Type_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 1, 7),
    _SwL2Module_2_Type_Type()
)
swL2Module_2_Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2Module_2_Type.setStatus("current")
_SwL2DevCtrl_ObjectIdentity = ObjectIdentity
swL2DevCtrl = _SwL2DevCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 2)
)


class _SwL2DevCtrlSystemReboot_Type(Integer32):
    """Custom type swL2DevCtrlSystemReboot based on Integer32"""
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
        *(("other", 1),
          ("reboot", 2),
          ("save-config-and-reboot", 3),
          ("reboot-and-load-factory-default-config", 4))
    )


_SwL2DevCtrlSystemReboot_Type.__name__ = "Integer32"
_SwL2DevCtrlSystemReboot_Object = MibScalar
swL2DevCtrlSystemReboot = _SwL2DevCtrlSystemReboot_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 2, 1),
    _SwL2DevCtrlSystemReboot_Type()
)
swL2DevCtrlSystemReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlSystemReboot.setStatus("current")
_SwL2DevCtrlSystemIP_Type = IpAddress
_SwL2DevCtrlSystemIP_Object = MibScalar
swL2DevCtrlSystemIP = _SwL2DevCtrlSystemIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 2, 2),
    _SwL2DevCtrlSystemIP_Type()
)
swL2DevCtrlSystemIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlSystemIP.setStatus("current")
_SwL2DevCtrlSubnetMask_Type = IpAddress
_SwL2DevCtrlSubnetMask_Object = MibScalar
swL2DevCtrlSubnetMask = _SwL2DevCtrlSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 2, 3),
    _SwL2DevCtrlSubnetMask_Type()
)
swL2DevCtrlSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlSubnetMask.setStatus("current")
_SwL2DevCtrlDefaultGateway_Type = IpAddress
_SwL2DevCtrlDefaultGateway_Object = MibScalar
swL2DevCtrlDefaultGateway = _SwL2DevCtrlDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 2, 4),
    _SwL2DevCtrlDefaultGateway_Type()
)
swL2DevCtrlDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlDefaultGateway.setStatus("current")
_SwL2DevCtrlManagementVlanId_Type = VlanId
_SwL2DevCtrlManagementVlanId_Object = MibScalar
swL2DevCtrlManagementVlanId = _SwL2DevCtrlManagementVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 2, 5),
    _SwL2DevCtrlManagementVlanId_Type()
)
swL2DevCtrlManagementVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlManagementVlanId.setStatus("current")


class _SwL2DevCtrlStpState_Type(Integer32):
    """Custom type swL2DevCtrlStpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL2DevCtrlStpState_Type.__name__ = "Integer32"
_SwL2DevCtrlStpState_Object = MibScalar
swL2DevCtrlStpState = _SwL2DevCtrlStpState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 2, 6),
    _SwL2DevCtrlStpState_Type()
)
swL2DevCtrlStpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlStpState.setStatus("current")


class _SwL2DevCtrlIGMPSnooping_Type(Integer32):
    """Custom type swL2DevCtrlIGMPSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL2DevCtrlIGMPSnooping_Type.__name__ = "Integer32"
_SwL2DevCtrlIGMPSnooping_Object = MibScalar
swL2DevCtrlIGMPSnooping = _SwL2DevCtrlIGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 2, 7),
    _SwL2DevCtrlIGMPSnooping_Type()
)
swL2DevCtrlIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlIGMPSnooping.setStatus("current")


class _SwL2DevCtrlCleanAllStatisticCounter_Type(Integer32):
    """Custom type swL2DevCtrlCleanAllStatisticCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("active", 2))
    )


_SwL2DevCtrlCleanAllStatisticCounter_Type.__name__ = "Integer32"
_SwL2DevCtrlCleanAllStatisticCounter_Object = MibScalar
swL2DevCtrlCleanAllStatisticCounter = _SwL2DevCtrlCleanAllStatisticCounter_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 2, 12),
    _SwL2DevCtrlCleanAllStatisticCounter_Type()
)
swL2DevCtrlCleanAllStatisticCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlCleanAllStatisticCounter.setStatus("current")


class _SwL2DevCtrlSnmpEnableAuthenTraps_Type(Integer32):
    """Custom type swL2DevCtrlSnmpEnableAuthenTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwL2DevCtrlSnmpEnableAuthenTraps_Type.__name__ = "Integer32"
_SwL2DevCtrlSnmpEnableAuthenTraps_Object = MibScalar
swL2DevCtrlSnmpEnableAuthenTraps = _SwL2DevCtrlSnmpEnableAuthenTraps_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 2, 13),
    _SwL2DevCtrlSnmpEnableAuthenTraps_Type()
)
swL2DevCtrlSnmpEnableAuthenTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlSnmpEnableAuthenTraps.setStatus("current")


class _SwL2DevCtrlRmonState_Type(Integer32):
    """Custom type swL2DevCtrlRmonState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL2DevCtrlRmonState_Type.__name__ = "Integer32"
_SwL2DevCtrlRmonState_Object = MibScalar
swL2DevCtrlRmonState = _SwL2DevCtrlRmonState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 2, 16),
    _SwL2DevCtrlRmonState_Type()
)
swL2DevCtrlRmonState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlRmonState.setStatus("current")


class _SwL2DevCtrlIpAutoConfig_Type(Integer32):
    """Custom type swL2DevCtrlIpAutoConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL2DevCtrlIpAutoConfig_Type.__name__ = "Integer32"
_SwL2DevCtrlIpAutoConfig_Object = MibScalar
swL2DevCtrlIpAutoConfig = _SwL2DevCtrlIpAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 2, 17),
    _SwL2DevCtrlIpAutoConfig_Type()
)
swL2DevCtrlIpAutoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlIpAutoConfig.setStatus("current")


class _SwL2PortCtrlMulticastfilter_Type(Integer32):
    """Custom type swL2PortCtrlMulticastfilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forward-unregistered-groups", 2),
          ("filter-unregistered-groups", 3))
    )


_SwL2PortCtrlMulticastfilter_Type.__name__ = "Integer32"
_SwL2PortCtrlMulticastfilter_Object = MibScalar
swL2PortCtrlMulticastfilter = _SwL2PortCtrlMulticastfilter_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 2, 18),
    _SwL2PortCtrlMulticastfilter_Type()
)
swL2PortCtrlMulticastfilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlMulticastfilter.setStatus("current")


class _SwL2MACNotifyState_Type(Integer32):
    """Custom type swL2MACNotifyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL2MACNotifyState_Type.__name__ = "Integer32"
_SwL2MACNotifyState_Object = MibScalar
swL2MACNotifyState = _SwL2MACNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 2, 19),
    _SwL2MACNotifyState_Type()
)
swL2MACNotifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MACNotifyState.setStatus("current")


class _SwL2MACNotifyHistorySize_Type(Integer32):
    """Custom type swL2MACNotifyHistorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_SwL2MACNotifyHistorySize_Type.__name__ = "Integer32"
_SwL2MACNotifyHistorySize_Object = MibScalar
swL2MACNotifyHistorySize = _SwL2MACNotifyHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 2, 20),
    _SwL2MACNotifyHistorySize_Type()
)
swL2MACNotifyHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MACNotifyHistorySize.setStatus("current")


class _SwL2MACNotifyInterval_Type(Integer32):
    """Custom type swL2MACNotifyInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SwL2MACNotifyInterval_Type.__name__ = "Integer32"
_SwL2MACNotifyInterval_Object = MibScalar
swL2MACNotifyInterval = _SwL2MACNotifyInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 2, 21),
    _SwL2MACNotifyInterval_Type()
)
swL2MACNotifyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MACNotifyInterval.setStatus("current")


class _SwL2DevCtrlVLANTrunkState_Type(Integer32):
    """Custom type swL2DevCtrlVLANTrunkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwL2DevCtrlVLANTrunkState_Type.__name__ = "Integer32"
_SwL2DevCtrlVLANTrunkState_Object = MibScalar
swL2DevCtrlVLANTrunkState = _SwL2DevCtrlVLANTrunkState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 2, 22),
    _SwL2DevCtrlVLANTrunkState_Type()
)
swL2DevCtrlVLANTrunkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlVLANTrunkState.setStatus("current")


class _SwL2DevCtrlLLDPState_Type(Integer32):
    """Custom type swL2DevCtrlLLDPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwL2DevCtrlLLDPState_Type.__name__ = "Integer32"
_SwL2DevCtrlLLDPState_Object = MibScalar
swL2DevCtrlLLDPState = _SwL2DevCtrlLLDPState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 2, 23),
    _SwL2DevCtrlLLDPState_Type()
)
swL2DevCtrlLLDPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlLLDPState.setStatus("current")


class _SwL2DevCtrlLLDPForwardMessageState_Type(Integer32):
    """Custom type swL2DevCtrlLLDPForwardMessageState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwL2DevCtrlLLDPForwardMessageState_Type.__name__ = "Integer32"
_SwL2DevCtrlLLDPForwardMessageState_Object = MibScalar
swL2DevCtrlLLDPForwardMessageState = _SwL2DevCtrlLLDPForwardMessageState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 2, 24),
    _SwL2DevCtrlLLDPForwardMessageState_Type()
)
swL2DevCtrlLLDPForwardMessageState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlLLDPForwardMessageState.setStatus("current")
_SwL2DevCtrlVlanIdOfFDBTbl_Type = VlanId
_SwL2DevCtrlVlanIdOfFDBTbl_Object = MibScalar
swL2DevCtrlVlanIdOfFDBTbl = _SwL2DevCtrlVlanIdOfFDBTbl_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 2, 25),
    _SwL2DevCtrlVlanIdOfFDBTbl_Type()
)
swL2DevCtrlVlanIdOfFDBTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlVlanIdOfFDBTbl.setStatus("current")
_SwL2CPUutilization_ObjectIdentity = ObjectIdentity
swL2CPUutilization = _SwL2CPUutilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 3)
)
_SwL2CPUutilizationIn5sec_Type = Integer32
_SwL2CPUutilizationIn5sec_Object = MibScalar
swL2CPUutilizationIn5sec = _SwL2CPUutilizationIn5sec_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 3, 1),
    _SwL2CPUutilizationIn5sec_Type()
)
swL2CPUutilizationIn5sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2CPUutilizationIn5sec.setStatus("current")
_SwL2CPUutilizationIn1min_Type = Integer32
_SwL2CPUutilizationIn1min_Object = MibScalar
swL2CPUutilizationIn1min = _SwL2CPUutilizationIn1min_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 3, 2),
    _SwL2CPUutilizationIn1min_Type()
)
swL2CPUutilizationIn1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2CPUutilizationIn1min.setStatus("current")
_SwL2CPUutilizationIn5min_Type = Integer32
_SwL2CPUutilizationIn5min_Object = MibScalar
swL2CPUutilizationIn5min = _SwL2CPUutilizationIn5min_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 3, 3),
    _SwL2CPUutilizationIn5min_Type()
)
swL2CPUutilizationIn5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2CPUutilizationIn5min.setStatus("current")
_SwL2DevAlarm_ObjectIdentity = ObjectIdentity
swL2DevAlarm = _SwL2DevAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 4)
)


class _SwL2DevAlarmLinkChange_Type(Integer32):
    """Custom type swL2DevAlarmLinkChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL2DevAlarmLinkChange_Type.__name__ = "Integer32"
_SwL2DevAlarmLinkChange_Object = MibScalar
swL2DevAlarmLinkChange = _SwL2DevAlarmLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 1, 4, 3),
    _SwL2DevAlarmLinkChange_Type()
)
swL2DevAlarmLinkChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmLinkChange.setStatus("current")
_SwL2PortMgmt_ObjectIdentity = ObjectIdentity
swL2PortMgmt = _SwL2PortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 2)
)
_SwL2PortInfoTable_Object = MibTable
swL2PortInfoTable = _SwL2PortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    swL2PortInfoTable.setStatus("current")
_SwL2PortInfoEntry_Object = MibTableRow
swL2PortInfoEntry = _SwL2PortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 2, 1, 1)
)
swL2PortInfoEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2PortInfoPortIndex"),
)
if mibBuilder.loadTexts:
    swL2PortInfoEntry.setStatus("current")


class _SwL2PortInfoPortIndex_Type(Integer32):
    """Custom type swL2PortInfoPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwL2PortInfoPortIndex_Type.__name__ = "Integer32"
_SwL2PortInfoPortIndex_Object = MibTableColumn
swL2PortInfoPortIndex = _SwL2PortInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 2, 1, 1, 1),
    _SwL2PortInfoPortIndex_Type()
)
swL2PortInfoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoPortIndex.setStatus("current")


class _SwL2PortInfoLinkStatus_Type(Integer32):
    """Custom type swL2PortInfoLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("link-pass", 2),
          ("link-fail", 3))
    )


_SwL2PortInfoLinkStatus_Type.__name__ = "Integer32"
_SwL2PortInfoLinkStatus_Object = MibTableColumn
swL2PortInfoLinkStatus = _SwL2PortInfoLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 2, 1, 1, 4),
    _SwL2PortInfoLinkStatus_Type()
)
swL2PortInfoLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoLinkStatus.setStatus("current")


class _SwL2PortInfoNwayStatus_Type(Integer32):
    """Custom type swL2PortInfoNwayStatus based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("full-10Mbps-8023x", 2),
          ("full-10Mbps-none", 3),
          ("half-10Mbps-backp", 4),
          ("half-10Mbps-none", 5),
          ("full-100Mbps-8023x", 6),
          ("full-100Mbps-none", 7),
          ("half-100Mbps-backp", 8),
          ("half-100Mbps-none", 9),
          ("full-1Gigabps-8023x", 10),
          ("full-1Gigabps-none", 11),
          ("half-1Gigabps-backp", 12),
          ("half-1Gigabps-none", 13))
    )


_SwL2PortInfoNwayStatus_Type.__name__ = "Integer32"
_SwL2PortInfoNwayStatus_Object = MibTableColumn
swL2PortInfoNwayStatus = _SwL2PortInfoNwayStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 2, 1, 1, 5),
    _SwL2PortInfoNwayStatus_Type()
)
swL2PortInfoNwayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoNwayStatus.setStatus("current")
_SwL2PortCtrlTable_Object = MibTable
swL2PortCtrlTable = _SwL2PortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    swL2PortCtrlTable.setStatus("current")
_SwL2PortCtrlEntry_Object = MibTableRow
swL2PortCtrlEntry = _SwL2PortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 2, 2, 1)
)
swL2PortCtrlEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2PortCtrlPortIndex"),
)
if mibBuilder.loadTexts:
    swL2PortCtrlEntry.setStatus("current")


class _SwL2PortCtrlPortIndex_Type(Integer32):
    """Custom type swL2PortCtrlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwL2PortCtrlPortIndex_Type.__name__ = "Integer32"
_SwL2PortCtrlPortIndex_Object = MibTableColumn
swL2PortCtrlPortIndex = _SwL2PortCtrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 2, 2, 1, 1),
    _SwL2PortCtrlPortIndex_Type()
)
swL2PortCtrlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCtrlPortIndex.setStatus("current")


class _SwL2PortCtrlAdminState_Type(Integer32):
    """Custom type swL2PortCtrlAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL2PortCtrlAdminState_Type.__name__ = "Integer32"
_SwL2PortCtrlAdminState_Object = MibTableColumn
swL2PortCtrlAdminState = _SwL2PortCtrlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 2, 2, 1, 2),
    _SwL2PortCtrlAdminState_Type()
)
swL2PortCtrlAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlAdminState.setStatus("current")


class _SwL2PortCtrlNwayState_Type(Integer32):
    """Custom type swL2PortCtrlNwayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("nway-auto", 1),
          ("nway-disabled-10Mbps-Half", 2),
          ("nway-disabled-10Mbps-Full", 3),
          ("nway-disabled-100Mbps-Half", 4),
          ("nway-disabled-100Mbps-Full", 5),
          ("nway-disabled-1Gigabps-Full", 7))
    )


_SwL2PortCtrlNwayState_Type.__name__ = "Integer32"
_SwL2PortCtrlNwayState_Object = MibTableColumn
swL2PortCtrlNwayState = _SwL2PortCtrlNwayState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 2, 2, 1, 3),
    _SwL2PortCtrlNwayState_Type()
)
swL2PortCtrlNwayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlNwayState.setStatus("current")


class _SwL2PortCtrlFlowCtrlState_Type(Integer32):
    """Custom type swL2PortCtrlFlowCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL2PortCtrlFlowCtrlState_Type.__name__ = "Integer32"
_SwL2PortCtrlFlowCtrlState_Object = MibTableColumn
swL2PortCtrlFlowCtrlState = _SwL2PortCtrlFlowCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 2, 2, 1, 4),
    _SwL2PortCtrlFlowCtrlState_Type()
)
swL2PortCtrlFlowCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlFlowCtrlState.setStatus("current")


class _SwL2PortCtrlDescription_Type(DisplayString):
    """Custom type swL2PortCtrlDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwL2PortCtrlDescription_Type.__name__ = "DisplayString"
_SwL2PortCtrlDescription_Object = MibTableColumn
swL2PortCtrlDescription = _SwL2PortCtrlDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 2, 2, 1, 5),
    _SwL2PortCtrlDescription_Type()
)
swL2PortCtrlDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlDescription.setStatus("current")


class _SwL2PortCtrlMACNotifyState_Type(Integer32):
    """Custom type swL2PortCtrlMACNotifyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL2PortCtrlMACNotifyState_Type.__name__ = "Integer32"
_SwL2PortCtrlMACNotifyState_Object = MibTableColumn
swL2PortCtrlMACNotifyState = _SwL2PortCtrlMACNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 2, 2, 1, 7),
    _SwL2PortCtrlMACNotifyState_Type()
)
swL2PortCtrlMACNotifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlMACNotifyState.setStatus("current")


class _SwL2PortCtrlMDIXState_Type(Integer32):
    """Custom type swL2PortCtrlMDIXState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("normal", 2),
          ("cross", 3))
    )


_SwL2PortCtrlMDIXState_Type.__name__ = "Integer32"
_SwL2PortCtrlMDIXState_Object = MibTableColumn
swL2PortCtrlMDIXState = _SwL2PortCtrlMDIXState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 2, 2, 1, 10),
    _SwL2PortCtrlMDIXState_Type()
)
swL2PortCtrlMDIXState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlMDIXState.setStatus("current")
_SwL2PortErrTable_Object = MibTable
swL2PortErrTable = _SwL2PortErrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 2, 3)
)
if mibBuilder.loadTexts:
    swL2PortErrTable.setStatus("current")
_SwL2PortErrEntry_Object = MibTableRow
swL2PortErrEntry = _SwL2PortErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 2, 3, 1)
)
swL2PortErrEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2PortErrPortIndex"),
)
if mibBuilder.loadTexts:
    swL2PortErrEntry.setStatus("current")


class _SwL2PortErrPortIndex_Type(Integer32):
    """Custom type swL2PortErrPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwL2PortErrPortIndex_Type.__name__ = "Integer32"
_SwL2PortErrPortIndex_Object = MibTableColumn
swL2PortErrPortIndex = _SwL2PortErrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 2, 3, 1, 1),
    _SwL2PortErrPortIndex_Type()
)
swL2PortErrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortErrPortIndex.setStatus("current")


class _SwL2PortErrPortState_Type(Integer32):
    """Custom type swL2PortErrPortState based on Integer32"""
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


_SwL2PortErrPortState_Type.__name__ = "Integer32"
_SwL2PortErrPortState_Object = MibTableColumn
swL2PortErrPortState = _SwL2PortErrPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 2, 3, 1, 2),
    _SwL2PortErrPortState_Type()
)
swL2PortErrPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortErrPortState.setStatus("current")


class _SwL2PortErrPortStatus_Type(Integer32):
    """Custom type swL2PortErrPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("err-disabled", 2))
    )


_SwL2PortErrPortStatus_Type.__name__ = "Integer32"
_SwL2PortErrPortStatus_Object = MibTableColumn
swL2PortErrPortStatus = _SwL2PortErrPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 2, 3, 1, 3),
    _SwL2PortErrPortStatus_Type()
)
swL2PortErrPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortErrPortStatus.setStatus("current")


class _SwL2PortErrPortReason_Type(Integer32):
    """Custom type swL2PortErrPortReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stp-lbd", 1),
          ("storm-control", 2))
    )


_SwL2PortErrPortReason_Type.__name__ = "Integer32"
_SwL2PortErrPortReason_Object = MibTableColumn
swL2PortErrPortReason = _SwL2PortErrPortReason_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 2, 3, 1, 4),
    _SwL2PortErrPortReason_Type()
)
swL2PortErrPortReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortErrPortReason.setStatus("current")


class _SwL2PortErrDescription_Type(DisplayString):
    """Custom type swL2PortErrDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwL2PortErrDescription_Type.__name__ = "DisplayString"
_SwL2PortErrDescription_Object = MibTableColumn
swL2PortErrDescription = _SwL2PortErrDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 2, 3, 1, 5),
    _SwL2PortErrDescription_Type()
)
swL2PortErrDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortErrDescription.setStatus("current")
_SwL2QOSMgmt_ObjectIdentity = ObjectIdentity
swL2QOSMgmt = _SwL2QOSMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 3)
)
_SwL2QOSBandwidthControlTable_Object = MibTable
swL2QOSBandwidthControlTable = _SwL2QOSBandwidthControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    swL2QOSBandwidthControlTable.setStatus("current")
_SwL2QOSBandwidthControlEntry_Object = MibTableRow
swL2QOSBandwidthControlEntry = _SwL2QOSBandwidthControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 3, 1, 1)
)
swL2QOSBandwidthControlEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2QOSBandwidthPortIndex"),
)
if mibBuilder.loadTexts:
    swL2QOSBandwidthControlEntry.setStatus("current")


class _SwL2QOSBandwidthPortIndex_Type(Integer32):
    """Custom type swL2QOSBandwidthPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 650),
    )


_SwL2QOSBandwidthPortIndex_Type.__name__ = "Integer32"
_SwL2QOSBandwidthPortIndex_Object = MibTableColumn
swL2QOSBandwidthPortIndex = _SwL2QOSBandwidthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 3, 1, 1, 1),
    _SwL2QOSBandwidthPortIndex_Type()
)
swL2QOSBandwidthPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOSBandwidthPortIndex.setStatus("current")


class _SwL2QOSBandwidthRxRate_Type(Integer32):
    """Custom type swL2QOSBandwidthRxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1024000),
    )


_SwL2QOSBandwidthRxRate_Type.__name__ = "Integer32"
_SwL2QOSBandwidthRxRate_Object = MibTableColumn
swL2QOSBandwidthRxRate = _SwL2QOSBandwidthRxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 3, 1, 1, 2),
    _SwL2QOSBandwidthRxRate_Type()
)
swL2QOSBandwidthRxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOSBandwidthRxRate.setStatus("current")


class _SwL2QOSBandwidthTxRate_Type(Integer32):
    """Custom type swL2QOSBandwidthTxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1024000),
    )


_SwL2QOSBandwidthTxRate_Type.__name__ = "Integer32"
_SwL2QOSBandwidthTxRate_Object = MibTableColumn
swL2QOSBandwidthTxRate = _SwL2QOSBandwidthTxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 3, 1, 1, 3),
    _SwL2QOSBandwidthTxRate_Type()
)
swL2QOSBandwidthTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOSBandwidthTxRate.setStatus("current")
_SwL2QOSBandwidthRadiusRxRate_Type = Integer32
_SwL2QOSBandwidthRadiusRxRate_Object = MibTableColumn
swL2QOSBandwidthRadiusRxRate = _SwL2QOSBandwidthRadiusRxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 3, 1, 1, 4),
    _SwL2QOSBandwidthRadiusRxRate_Type()
)
swL2QOSBandwidthRadiusRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOSBandwidthRadiusRxRate.setStatus("current")
_SwL2QOSBandwidthRadiusTxRate_Type = Integer32
_SwL2QOSBandwidthRadiusTxRate_Object = MibTableColumn
swL2QOSBandwidthRadiusTxRate = _SwL2QOSBandwidthRadiusTxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 3, 1, 1, 5),
    _SwL2QOSBandwidthRadiusTxRate_Type()
)
swL2QOSBandwidthRadiusTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOSBandwidthRadiusTxRate.setStatus("current")
_SwL2QOSSchedulingTable_Object = MibTable
swL2QOSSchedulingTable = _SwL2QOSSchedulingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    swL2QOSSchedulingTable.setStatus("current")
_SwL2QOSSchedulingEntry_Object = MibTableRow
swL2QOSSchedulingEntry = _SwL2QOSSchedulingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 3, 2, 1)
)
swL2QOSSchedulingEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2QOSSchedulingClassIndex"),
)
if mibBuilder.loadTexts:
    swL2QOSSchedulingEntry.setStatus("current")


class _SwL2QOSSchedulingClassIndex_Type(Integer32):
    """Custom type swL2QOSSchedulingClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SwL2QOSSchedulingClassIndex_Type.__name__ = "Integer32"
_SwL2QOSSchedulingClassIndex_Object = MibTableColumn
swL2QOSSchedulingClassIndex = _SwL2QOSSchedulingClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 3, 2, 1, 1),
    _SwL2QOSSchedulingClassIndex_Type()
)
swL2QOSSchedulingClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOSSchedulingClassIndex.setStatus("current")


class _SwL2QOSSchedulingMaxWeight_Type(Integer32):
    """Custom type swL2QOSSchedulingMaxWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 55),
    )


_SwL2QOSSchedulingMaxWeight_Type.__name__ = "Integer32"
_SwL2QOSSchedulingMaxWeight_Object = MibTableColumn
swL2QOSSchedulingMaxWeight = _SwL2QOSSchedulingMaxWeight_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 3, 2, 1, 4),
    _SwL2QOSSchedulingMaxWeight_Type()
)
swL2QOSSchedulingMaxWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOSSchedulingMaxWeight.setStatus("current")
_SwL2QOS8021pUserPriorityTable_Object = MibTable
swL2QOS8021pUserPriorityTable = _SwL2QOS8021pUserPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 3, 3)
)
if mibBuilder.loadTexts:
    swL2QOS8021pUserPriorityTable.setStatus("current")
_SwL2QOS8021pUserPriorityEntry_Object = MibTableRow
swL2QOS8021pUserPriorityEntry = _SwL2QOS8021pUserPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 3, 3, 1)
)
swL2QOS8021pUserPriorityEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2QOS8021pUserPriorityIndex"),
)
if mibBuilder.loadTexts:
    swL2QOS8021pUserPriorityEntry.setStatus("current")


class _SwL2QOS8021pUserPriorityIndex_Type(Integer32):
    """Custom type swL2QOS8021pUserPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwL2QOS8021pUserPriorityIndex_Type.__name__ = "Integer32"
_SwL2QOS8021pUserPriorityIndex_Object = MibTableColumn
swL2QOS8021pUserPriorityIndex = _SwL2QOS8021pUserPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 3, 3, 1, 1),
    _SwL2QOS8021pUserPriorityIndex_Type()
)
swL2QOS8021pUserPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOS8021pUserPriorityIndex.setStatus("current")


class _SwL2QOS8021pUserPriorityClass_Type(Integer32):
    """Custom type swL2QOS8021pUserPriorityClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SwL2QOS8021pUserPriorityClass_Type.__name__ = "Integer32"
_SwL2QOS8021pUserPriorityClass_Object = MibTableColumn
swL2QOS8021pUserPriorityClass = _SwL2QOS8021pUserPriorityClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 3, 3, 1, 2),
    _SwL2QOS8021pUserPriorityClass_Type()
)
swL2QOS8021pUserPriorityClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOS8021pUserPriorityClass.setStatus("current")
_SwL2QOS8021pDefaultPriorityTable_Object = MibTable
swL2QOS8021pDefaultPriorityTable = _SwL2QOS8021pDefaultPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 3, 4)
)
if mibBuilder.loadTexts:
    swL2QOS8021pDefaultPriorityTable.setStatus("current")
_SwL2QOS8021pDefaultPriorityEntry_Object = MibTableRow
swL2QOS8021pDefaultPriorityEntry = _SwL2QOS8021pDefaultPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 3, 4, 1)
)
swL2QOS8021pDefaultPriorityEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2QOS8021pDefaultPriorityIndex"),
)
if mibBuilder.loadTexts:
    swL2QOS8021pDefaultPriorityEntry.setStatus("current")


class _SwL2QOS8021pDefaultPriorityIndex_Type(Integer32):
    """Custom type swL2QOS8021pDefaultPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 650),
    )


_SwL2QOS8021pDefaultPriorityIndex_Type.__name__ = "Integer32"
_SwL2QOS8021pDefaultPriorityIndex_Object = MibTableColumn
swL2QOS8021pDefaultPriorityIndex = _SwL2QOS8021pDefaultPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 3, 4, 1, 1),
    _SwL2QOS8021pDefaultPriorityIndex_Type()
)
swL2QOS8021pDefaultPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOS8021pDefaultPriorityIndex.setStatus("current")


class _SwL2QOS8021pDefaultPriority_Type(Integer32):
    """Custom type swL2QOS8021pDefaultPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwL2QOS8021pDefaultPriority_Type.__name__ = "Integer32"
_SwL2QOS8021pDefaultPriority_Object = MibTableColumn
swL2QOS8021pDefaultPriority = _SwL2QOS8021pDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 3, 4, 1, 2),
    _SwL2QOS8021pDefaultPriority_Type()
)
swL2QOS8021pDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOS8021pDefaultPriority.setStatus("current")
_SwL2QOS8021pRadiusPriority_Type = Integer32
_SwL2QOS8021pRadiusPriority_Object = MibTableColumn
swL2QOS8021pRadiusPriority = _SwL2QOS8021pRadiusPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 3, 4, 1, 3),
    _SwL2QOS8021pRadiusPriority_Type()
)
swL2QOS8021pRadiusPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOS8021pRadiusPriority.setStatus("current")


class _SwL2QOSSchedulingMechanismCtrl_Type(Integer32):
    """Custom type swL2QOSSchedulingMechanismCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("strict", 1),
          ("weightfair", 2),
          ("none", 3))
    )


_SwL2QOSSchedulingMechanismCtrl_Type.__name__ = "Integer32"
_SwL2QOSSchedulingMechanismCtrl_Object = MibScalar
swL2QOSSchedulingMechanismCtrl = _SwL2QOSSchedulingMechanismCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 3, 5),
    _SwL2QOSSchedulingMechanismCtrl_Type()
)
swL2QOSSchedulingMechanismCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOSSchedulingMechanismCtrl.setStatus("current")
_SwL2TrunkMgmt_ObjectIdentity = ObjectIdentity
swL2TrunkMgmt = _SwL2TrunkMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 4)
)
_SwPortTrunkMaxEntries_Type = Integer32
_SwPortTrunkMaxEntries_Object = MibScalar
swPortTrunkMaxEntries = _SwPortTrunkMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 4, 1),
    _SwPortTrunkMaxEntries_Type()
)
swPortTrunkMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkMaxEntries.setStatus("current")
_SwPortTrunkMaxPortMembers_Type = Integer32
_SwPortTrunkMaxPortMembers_Object = MibScalar
swPortTrunkMaxPortMembers = _SwPortTrunkMaxPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 4, 2),
    _SwPortTrunkMaxPortMembers_Type()
)
swPortTrunkMaxPortMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkMaxPortMembers.setStatus("current")
_SwPortTrunkTable_Object = MibTable
swPortTrunkTable = _SwPortTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 4, 3)
)
if mibBuilder.loadTexts:
    swPortTrunkTable.setStatus("current")
_SwPortTrunkEntry_Object = MibTableRow
swPortTrunkEntry = _SwPortTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 4, 3, 1)
)
swPortTrunkEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swPortTrunkIndex"),
)
if mibBuilder.loadTexts:
    swPortTrunkEntry.setStatus("current")


class _SwPortTrunkIndex_Type(Integer32):
    """Custom type swPortTrunkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SwPortTrunkIndex_Type.__name__ = "Integer32"
_SwPortTrunkIndex_Object = MibTableColumn
swPortTrunkIndex = _SwPortTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 4, 3, 1, 1),
    _SwPortTrunkIndex_Type()
)
swPortTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkIndex.setStatus("current")
_SwPortTrunkMasterPort_Type = Integer32
_SwPortTrunkMasterPort_Object = MibTableColumn
swPortTrunkMasterPort = _SwPortTrunkMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 4, 3, 1, 2),
    _SwPortTrunkMasterPort_Type()
)
swPortTrunkMasterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPortTrunkMasterPort.setStatus("current")
_SwPortTrunkPortList_Type = PortList
_SwPortTrunkPortList_Object = MibTableColumn
swPortTrunkPortList = _SwPortTrunkPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 4, 3, 1, 3),
    _SwPortTrunkPortList_Type()
)
swPortTrunkPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPortTrunkPortList.setStatus("current")


class _SwPortTrunkType_Type(Integer32):
    """Custom type swPortTrunkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("lacp", 2))
    )


_SwPortTrunkType_Type.__name__ = "Integer32"
_SwPortTrunkType_Object = MibTableColumn
swPortTrunkType = _SwPortTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 4, 3, 1, 4),
    _SwPortTrunkType_Type()
)
swPortTrunkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPortTrunkType.setStatus("current")
_SwPortTrunkActivePort_Type = PortList
_SwPortTrunkActivePort_Object = MibTableColumn
swPortTrunkActivePort = _SwPortTrunkActivePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 4, 3, 1, 5),
    _SwPortTrunkActivePort_Type()
)
swPortTrunkActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkActivePort.setStatus("current")
_SwPortTrunkState_Type = RowStatus
_SwPortTrunkState_Object = MibTableColumn
swPortTrunkState = _SwPortTrunkState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 4, 3, 1, 6),
    _SwPortTrunkState_Type()
)
swPortTrunkState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPortTrunkState.setStatus("current")
_SwPortTrunkFloodingPort_Type = Integer32
_SwPortTrunkFloodingPort_Object = MibTableColumn
swPortTrunkFloodingPort = _SwPortTrunkFloodingPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 4, 3, 1, 7),
    _SwPortTrunkFloodingPort_Type()
)
swPortTrunkFloodingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkFloodingPort.setStatus("current")


class _SwL2TrunkAlgorithm_Type(Integer32):
    """Custom type swL2TrunkAlgorithm based on Integer32"""
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
        *(("other", 1),
          ("mac-source", 2),
          ("mac-destination", 3),
          ("mac-source-dest", 4))
    )


_SwL2TrunkAlgorithm_Type.__name__ = "Integer32"
_SwL2TrunkAlgorithm_Object = MibScalar
swL2TrunkAlgorithm = _SwL2TrunkAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 4, 4),
    _SwL2TrunkAlgorithm_Type()
)
swL2TrunkAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkAlgorithm.setStatus("current")
_SwL2TrunkLACPPortTable_Object = MibTable
swL2TrunkLACPPortTable = _SwL2TrunkLACPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 4, 5)
)
if mibBuilder.loadTexts:
    swL2TrunkLACPPortTable.setStatus("current")
_SwL2TrunkLACPPortEntry_Object = MibTableRow
swL2TrunkLACPPortEntry = _SwL2TrunkLACPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 4, 5, 1)
)
swL2TrunkLACPPortEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2TrunkLACPPortIndex"),
)
if mibBuilder.loadTexts:
    swL2TrunkLACPPortEntry.setStatus("current")


class _SwL2TrunkLACPPortIndex_Type(Integer32):
    """Custom type swL2TrunkLACPPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2TrunkLACPPortIndex_Type.__name__ = "Integer32"
_SwL2TrunkLACPPortIndex_Object = MibTableColumn
swL2TrunkLACPPortIndex = _SwL2TrunkLACPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 4, 5, 1, 1),
    _SwL2TrunkLACPPortIndex_Type()
)
swL2TrunkLACPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrunkLACPPortIndex.setStatus("current")


class _SwL2TrunkLACPPortState_Type(Integer32):
    """Custom type swL2TrunkLACPPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_SwL2TrunkLACPPortState_Type.__name__ = "Integer32"
_SwL2TrunkLACPPortState_Object = MibTableColumn
swL2TrunkLACPPortState = _SwL2TrunkLACPPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 4, 5, 1, 2),
    _SwL2TrunkLACPPortState_Type()
)
swL2TrunkLACPPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkLACPPortState.setStatus("current")
_SwL2TrunkVLANTable_Object = MibTable
swL2TrunkVLANTable = _SwL2TrunkVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 4, 6)
)
if mibBuilder.loadTexts:
    swL2TrunkVLANTable.setStatus("current")
_SwL2TrunkVLANEntry_Object = MibTableRow
swL2TrunkVLANEntry = _SwL2TrunkVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 4, 6, 1)
)
swL2TrunkVLANEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2TrunkVLANPort"),
)
if mibBuilder.loadTexts:
    swL2TrunkVLANEntry.setStatus("current")


class _SwL2TrunkVLANPort_Type(Integer32):
    """Custom type swL2TrunkVLANPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2TrunkVLANPort_Type.__name__ = "Integer32"
_SwL2TrunkVLANPort_Object = MibTableColumn
swL2TrunkVLANPort = _SwL2TrunkVLANPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 4, 6, 1, 1),
    _SwL2TrunkVLANPort_Type()
)
swL2TrunkVLANPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrunkVLANPort.setStatus("current")


class _SwL2TrunkVLANState_Type(Integer32):
    """Custom type swL2TrunkVLANState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwL2TrunkVLANState_Type.__name__ = "Integer32"
_SwL2TrunkVLANState_Object = MibTableColumn
swL2TrunkVLANState = _SwL2TrunkVLANState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 4, 6, 1, 2),
    _SwL2TrunkVLANState_Type()
)
swL2TrunkVLANState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkVLANState.setStatus("current")
_SwPortMirrorPackage_ObjectIdentity = ObjectIdentity
swPortMirrorPackage = _SwPortMirrorPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 6)
)
_SwPortMirrorRxPortList_Type = PortList
_SwPortMirrorRxPortList_Object = MibScalar
swPortMirrorRxPortList = _SwPortMirrorRxPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 6, 2),
    _SwPortMirrorRxPortList_Type()
)
swPortMirrorRxPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMirrorRxPortList.setStatus("current")
_SwPortMirrorTxPortList_Type = PortList
_SwPortMirrorTxPortList_Object = MibScalar
swPortMirrorTxPortList = _SwPortMirrorTxPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 6, 3),
    _SwPortMirrorTxPortList_Type()
)
swPortMirrorTxPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMirrorTxPortList.setStatus("current")
_SwPortMirrorTargetPort_Type = Integer32
_SwPortMirrorTargetPort_Object = MibScalar
swPortMirrorTargetPort = _SwPortMirrorTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 6, 4),
    _SwPortMirrorTargetPort_Type()
)
swPortMirrorTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMirrorTargetPort.setStatus("current")


class _SwPortMirrorState_Type(Integer32):
    """Custom type swPortMirrorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwPortMirrorState_Type.__name__ = "Integer32"
_SwPortMirrorState_Object = MibScalar
swPortMirrorState = _SwPortMirrorState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 6, 5),
    _SwPortMirrorState_Type()
)
swPortMirrorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMirrorState.setStatus("current")
_SwIGMPPackage_ObjectIdentity = ObjectIdentity
swIGMPPackage = _SwIGMPPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7)
)


class _SwL2IGMPMaxSupportedVlans_Type(Integer32):
    """Custom type swL2IGMPMaxSupportedVlans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPMaxSupportedVlans_Type.__name__ = "Integer32"
_SwL2IGMPMaxSupportedVlans_Object = MibScalar
swL2IGMPMaxSupportedVlans = _SwL2IGMPMaxSupportedVlans_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 1),
    _SwL2IGMPMaxSupportedVlans_Type()
)
swL2IGMPMaxSupportedVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMaxSupportedVlans.setStatus("current")


class _SwL2IGMPMaxIpGroupNumPerVlan_Type(Integer32):
    """Custom type swL2IGMPMaxIpGroupNumPerVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPMaxIpGroupNumPerVlan_Type.__name__ = "Integer32"
_SwL2IGMPMaxIpGroupNumPerVlan_Object = MibScalar
swL2IGMPMaxIpGroupNumPerVlan = _SwL2IGMPMaxIpGroupNumPerVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 2),
    _SwL2IGMPMaxIpGroupNumPerVlan_Type()
)
swL2IGMPMaxIpGroupNumPerVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMaxIpGroupNumPerVlan.setStatus("current")
_SwL2IGMPCtrlTable_Object = MibTable
swL2IGMPCtrlTable = _SwL2IGMPCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 3)
)
if mibBuilder.loadTexts:
    swL2IGMPCtrlTable.setStatus("current")
_SwL2IGMPCtrlEntry_Object = MibTableRow
swL2IGMPCtrlEntry = _SwL2IGMPCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 3, 1)
)
swL2IGMPCtrlEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2IGMPCtrlVid"),
)
if mibBuilder.loadTexts:
    swL2IGMPCtrlEntry.setStatus("current")


class _SwL2IGMPCtrlVid_Type(Integer32):
    """Custom type swL2IGMPCtrlVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPCtrlVid_Type.__name__ = "Integer32"
_SwL2IGMPCtrlVid_Object = MibTableColumn
swL2IGMPCtrlVid = _SwL2IGMPCtrlVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 3, 1, 1),
    _SwL2IGMPCtrlVid_Type()
)
swL2IGMPCtrlVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPCtrlVid.setStatus("current")


class _SwL2IGMPQueryInterval_Type(Integer32):
    """Custom type swL2IGMPQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL2IGMPQueryInterval_Type.__name__ = "Integer32"
_SwL2IGMPQueryInterval_Object = MibTableColumn
swL2IGMPQueryInterval = _SwL2IGMPQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 3, 1, 2),
    _SwL2IGMPQueryInterval_Type()
)
swL2IGMPQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPQueryInterval.setStatus("current")


class _SwL2IGMPMaxResponseTime_Type(Integer32):
    """Custom type swL2IGMPMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_SwL2IGMPMaxResponseTime_Type.__name__ = "Integer32"
_SwL2IGMPMaxResponseTime_Object = MibTableColumn
swL2IGMPMaxResponseTime = _SwL2IGMPMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 3, 1, 3),
    _SwL2IGMPMaxResponseTime_Type()
)
swL2IGMPMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPMaxResponseTime.setStatus("current")


class _SwL2IGMPRobustness_Type(Integer32):
    """Custom type swL2IGMPRobustness based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwL2IGMPRobustness_Type.__name__ = "Integer32"
_SwL2IGMPRobustness_Object = MibTableColumn
swL2IGMPRobustness = _SwL2IGMPRobustness_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 3, 1, 4),
    _SwL2IGMPRobustness_Type()
)
swL2IGMPRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPRobustness.setStatus("current")


class _SwL2IGMPLastMemberQueryInterval_Type(Integer32):
    """Custom type swL2IGMPLastMemberQueryInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL2IGMPLastMemberQueryInterval_Type.__name__ = "Integer32"
_SwL2IGMPLastMemberQueryInterval_Object = MibTableColumn
swL2IGMPLastMemberQueryInterval = _SwL2IGMPLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 3, 1, 5),
    _SwL2IGMPLastMemberQueryInterval_Type()
)
swL2IGMPLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPLastMemberQueryInterval.setStatus("current")


class _SwL2IGMPHostTimeout_Type(Integer32):
    """Custom type swL2IGMPHostTimeout based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16711450),
    )


_SwL2IGMPHostTimeout_Type.__name__ = "Integer32"
_SwL2IGMPHostTimeout_Object = MibTableColumn
swL2IGMPHostTimeout = _SwL2IGMPHostTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 3, 1, 6),
    _SwL2IGMPHostTimeout_Type()
)
swL2IGMPHostTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPHostTimeout.setStatus("current")


class _SwL2IGMPRouteTimeout_Type(Integer32):
    """Custom type swL2IGMPRouteTimeout based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16711450),
    )


_SwL2IGMPRouteTimeout_Type.__name__ = "Integer32"
_SwL2IGMPRouteTimeout_Object = MibTableColumn
swL2IGMPRouteTimeout = _SwL2IGMPRouteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 3, 1, 7),
    _SwL2IGMPRouteTimeout_Type()
)
swL2IGMPRouteTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPRouteTimeout.setStatus("current")


class _SwL2IGMPLeaveTimer_Type(Integer32):
    """Custom type swL2IGMPLeaveTimer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16711450),
    )


_SwL2IGMPLeaveTimer_Type.__name__ = "Integer32"
_SwL2IGMPLeaveTimer_Object = MibTableColumn
swL2IGMPLeaveTimer = _SwL2IGMPLeaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 3, 1, 8),
    _SwL2IGMPLeaveTimer_Type()
)
swL2IGMPLeaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPLeaveTimer.setStatus("current")


class _SwL2IGMPQueryState_Type(Integer32):
    """Custom type swL2IGMPQueryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL2IGMPQueryState_Type.__name__ = "Integer32"
_SwL2IGMPQueryState_Object = MibTableColumn
swL2IGMPQueryState = _SwL2IGMPQueryState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 3, 1, 9),
    _SwL2IGMPQueryState_Type()
)
swL2IGMPQueryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPQueryState.setStatus("current")


class _SwL2IGMPCurrentState_Type(Integer32):
    """Custom type swL2IGMPCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("querier", 2),
          ("non-querier", 3))
    )


_SwL2IGMPCurrentState_Type.__name__ = "Integer32"
_SwL2IGMPCurrentState_Object = MibTableColumn
swL2IGMPCurrentState = _SwL2IGMPCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 3, 1, 10),
    _SwL2IGMPCurrentState_Type()
)
swL2IGMPCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPCurrentState.setStatus("current")


class _SwL2IGMPCtrlState_Type(Integer32):
    """Custom type swL2IGMPCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disable", 2),
          ("enable", 3))
    )


_SwL2IGMPCtrlState_Type.__name__ = "Integer32"
_SwL2IGMPCtrlState_Object = MibTableColumn
swL2IGMPCtrlState = _SwL2IGMPCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 3, 1, 11),
    _SwL2IGMPCtrlState_Type()
)
swL2IGMPCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPCtrlState.setStatus("current")


class _SwL2IGMPFastLeave_Type(Integer32):
    """Custom type swL2IGMPFastLeave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disable", 2),
          ("enable", 3))
    )


_SwL2IGMPFastLeave_Type.__name__ = "Integer32"
_SwL2IGMPFastLeave_Object = MibTableColumn
swL2IGMPFastLeave = _SwL2IGMPFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 3, 1, 12),
    _SwL2IGMPFastLeave_Type()
)
swL2IGMPFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPFastLeave.setStatus("current")
_SwL2IGMPQueryInfoTable_Object = MibTable
swL2IGMPQueryInfoTable = _SwL2IGMPQueryInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 4)
)
if mibBuilder.loadTexts:
    swL2IGMPQueryInfoTable.setStatus("current")
_SwL2IGMPQueryInfoEntry_Object = MibTableRow
swL2IGMPQueryInfoEntry = _SwL2IGMPQueryInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 4, 1)
)
swL2IGMPQueryInfoEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2IGMPInfoVid"),
)
if mibBuilder.loadTexts:
    swL2IGMPQueryInfoEntry.setStatus("current")


class _SwL2IGMPInfoVid_Type(Integer32):
    """Custom type swL2IGMPInfoVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPInfoVid_Type.__name__ = "Integer32"
_SwL2IGMPInfoVid_Object = MibTableColumn
swL2IGMPInfoVid = _SwL2IGMPInfoVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 4, 1, 1),
    _SwL2IGMPInfoVid_Type()
)
swL2IGMPInfoVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPInfoVid.setStatus("current")


class _SwL2IGMPInfoQueryCount_Type(Integer32):
    """Custom type swL2IGMPInfoQueryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPInfoQueryCount_Type.__name__ = "Integer32"
_SwL2IGMPInfoQueryCount_Object = MibTableColumn
swL2IGMPInfoQueryCount = _SwL2IGMPInfoQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 4, 1, 2),
    _SwL2IGMPInfoQueryCount_Type()
)
swL2IGMPInfoQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPInfoQueryCount.setStatus("current")


class _SwL2IGMPInfoTxQueryCount_Type(Integer32):
    """Custom type swL2IGMPInfoTxQueryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPInfoTxQueryCount_Type.__name__ = "Integer32"
_SwL2IGMPInfoTxQueryCount_Object = MibTableColumn
swL2IGMPInfoTxQueryCount = _SwL2IGMPInfoTxQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 4, 1, 3),
    _SwL2IGMPInfoTxQueryCount_Type()
)
swL2IGMPInfoTxQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPInfoTxQueryCount.setStatus("current")
_SwL2IGMPInfoTable_Object = MibTable
swL2IGMPInfoTable = _SwL2IGMPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 5)
)
if mibBuilder.loadTexts:
    swL2IGMPInfoTable.setStatus("current")
_SwL2IGMPInfoEntry_Object = MibTableRow
swL2IGMPInfoEntry = _SwL2IGMPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 5, 1)
)
swL2IGMPInfoEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2IGMPVid"),
    (0, "DES3026-L2MGMT-MIB", "swL2IGMPGroupIpAddr"),
)
if mibBuilder.loadTexts:
    swL2IGMPInfoEntry.setStatus("current")


class _SwL2IGMPVid_Type(Integer32):
    """Custom type swL2IGMPVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPVid_Type.__name__ = "Integer32"
_SwL2IGMPVid_Object = MibTableColumn
swL2IGMPVid = _SwL2IGMPVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 5, 1, 1),
    _SwL2IGMPVid_Type()
)
swL2IGMPVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPVid.setStatus("current")
_SwL2IGMPGroupIpAddr_Type = IpAddress
_SwL2IGMPGroupIpAddr_Object = MibTableColumn
swL2IGMPGroupIpAddr = _SwL2IGMPGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 5, 1, 2),
    _SwL2IGMPGroupIpAddr_Type()
)
swL2IGMPGroupIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPGroupIpAddr.setStatus("current")
_SwL2IGMPMacAddr_Type = MacAddress
_SwL2IGMPMacAddr_Object = MibTableColumn
swL2IGMPMacAddr = _SwL2IGMPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 5, 1, 3),
    _SwL2IGMPMacAddr_Type()
)
swL2IGMPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMacAddr.setStatus("current")
_SwL2IGMPPortMap_Type = PortList
_SwL2IGMPPortMap_Object = MibTableColumn
swL2IGMPPortMap = _SwL2IGMPPortMap_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 5, 1, 4),
    _SwL2IGMPPortMap_Type()
)
swL2IGMPPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPPortMap.setStatus("current")


class _SwL2IGMPIpGroupReportCount_Type(Integer32):
    """Custom type swL2IGMPIpGroupReportCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPIpGroupReportCount_Type.__name__ = "Integer32"
_SwL2IGMPIpGroupReportCount_Object = MibTableColumn
swL2IGMPIpGroupReportCount = _SwL2IGMPIpGroupReportCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 5, 1, 5),
    _SwL2IGMPIpGroupReportCount_Type()
)
swL2IGMPIpGroupReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPIpGroupReportCount.setStatus("current")
_SwL2IGMPRouterPortTable_Object = MibTable
swL2IGMPRouterPortTable = _SwL2IGMPRouterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 6)
)
if mibBuilder.loadTexts:
    swL2IGMPRouterPortTable.setStatus("current")
_SwL2IGMPRouterPortEntry_Object = MibTableRow
swL2IGMPRouterPortEntry = _SwL2IGMPRouterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 6, 1)
)
swL2IGMPRouterPortEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2IGMPRouterPortVlanid"),
)
if mibBuilder.loadTexts:
    swL2IGMPRouterPortEntry.setStatus("current")


class _SwL2IGMPRouterPortVlanid_Type(Integer32):
    """Custom type swL2IGMPRouterPortVlanid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwL2IGMPRouterPortVlanid_Type.__name__ = "Integer32"
_SwL2IGMPRouterPortVlanid_Object = MibTableColumn
swL2IGMPRouterPortVlanid = _SwL2IGMPRouterPortVlanid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 6, 1, 1),
    _SwL2IGMPRouterPortVlanid_Type()
)
swL2IGMPRouterPortVlanid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPRouterPortVlanid.setStatus("current")


class _SwL2IGMPRouterPortVlanName_Type(DisplayString):
    """Custom type swL2IGMPRouterPortVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwL2IGMPRouterPortVlanName_Type.__name__ = "DisplayString"
_SwL2IGMPRouterPortVlanName_Object = MibTableColumn
swL2IGMPRouterPortVlanName = _SwL2IGMPRouterPortVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 6, 1, 2),
    _SwL2IGMPRouterPortVlanName_Type()
)
swL2IGMPRouterPortVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPRouterPortVlanName.setStatus("current")
_SwL2IGMPRouterPortStaticPortList_Type = PortList
_SwL2IGMPRouterPortStaticPortList_Object = MibTableColumn
swL2IGMPRouterPortStaticPortList = _SwL2IGMPRouterPortStaticPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 6, 1, 3),
    _SwL2IGMPRouterPortStaticPortList_Type()
)
swL2IGMPRouterPortStaticPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPRouterPortStaticPortList.setStatus("current")
_SwL2IGMPRouterPortDynamicPortList_Type = PortList
_SwL2IGMPRouterPortDynamicPortList_Object = MibTableColumn
swL2IGMPRouterPortDynamicPortList = _SwL2IGMPRouterPortDynamicPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 6, 1, 4),
    _SwL2IGMPRouterPortDynamicPortList_Type()
)
swL2IGMPRouterPortDynamicPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPRouterPortDynamicPortList.setStatus("current")
_SwL2IGMPRouterPortForbiddenPortList_Type = PortList
_SwL2IGMPRouterPortForbiddenPortList_Object = MibTableColumn
swL2IGMPRouterPortForbiddenPortList = _SwL2IGMPRouterPortForbiddenPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 6, 1, 5),
    _SwL2IGMPRouterPortForbiddenPortList_Type()
)
swL2IGMPRouterPortForbiddenPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPRouterPortForbiddenPortList.setStatus("current")
_SwL2IGMPAccessAuthTable_Object = MibTable
swL2IGMPAccessAuthTable = _SwL2IGMPAccessAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 7)
)
if mibBuilder.loadTexts:
    swL2IGMPAccessAuthTable.setStatus("current")
_SwL2IGMPAccessAuthEntry_Object = MibTableRow
swL2IGMPAccessAuthEntry = _SwL2IGMPAccessAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 7, 1)
)
swL2IGMPAccessAuthEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2IGMPAccessAuthPort"),
)
if mibBuilder.loadTexts:
    swL2IGMPAccessAuthEntry.setStatus("current")


class _SwL2IGMPAccessAuthPort_Type(Integer32):
    """Custom type swL2IGMPAccessAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPAccessAuthPort_Type.__name__ = "Integer32"
_SwL2IGMPAccessAuthPort_Object = MibTableColumn
swL2IGMPAccessAuthPort = _SwL2IGMPAccessAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 7, 1, 1),
    _SwL2IGMPAccessAuthPort_Type()
)
swL2IGMPAccessAuthPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPAccessAuthPort.setStatus("current")


class _SwL2IGMPAccessAuthState_Type(Integer32):
    """Custom type swL2IGMPAccessAuthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disable", 2),
          ("enable", 3))
    )


_SwL2IGMPAccessAuthState_Type.__name__ = "Integer32"
_SwL2IGMPAccessAuthState_Object = MibTableColumn
swL2IGMPAccessAuthState = _SwL2IGMPAccessAuthState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 7, 7, 1, 2),
    _SwL2IGMPAccessAuthState_Type()
)
swL2IGMPAccessAuthState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPAccessAuthState.setStatus("current")
_SwL2TrafficMgmt_ObjectIdentity = ObjectIdentity
swL2TrafficMgmt = _SwL2TrafficMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 11)
)
_SwL2TrafficCtrlTable_Object = MibTable
swL2TrafficCtrlTable = _SwL2TrafficCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 11, 1)
)
if mibBuilder.loadTexts:
    swL2TrafficCtrlTable.setStatus("current")
_SwL2TrafficCtrlEntry_Object = MibTableRow
swL2TrafficCtrlEntry = _SwL2TrafficCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 11, 1, 1)
)
swL2TrafficCtrlEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2TrafficCtrlGroupIndex"),
)
if mibBuilder.loadTexts:
    swL2TrafficCtrlEntry.setStatus("current")


class _SwL2TrafficCtrlGroupIndex_Type(Integer32):
    """Custom type swL2TrafficCtrlGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2TrafficCtrlGroupIndex_Type.__name__ = "Integer32"
_SwL2TrafficCtrlGroupIndex_Object = MibTableColumn
swL2TrafficCtrlGroupIndex = _SwL2TrafficCtrlGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 11, 1, 1, 1),
    _SwL2TrafficCtrlGroupIndex_Type()
)
swL2TrafficCtrlGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrafficCtrlGroupIndex.setStatus("current")


class _SwL2TrafficCtrlUnitIndex_Type(Integer32):
    """Custom type swL2TrafficCtrlUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2TrafficCtrlUnitIndex_Type.__name__ = "Integer32"
_SwL2TrafficCtrlUnitIndex_Object = MibTableColumn
swL2TrafficCtrlUnitIndex = _SwL2TrafficCtrlUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 11, 1, 1, 2),
    _SwL2TrafficCtrlUnitIndex_Type()
)
swL2TrafficCtrlUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrafficCtrlUnitIndex.setStatus("current")


class _SwL2TrafficCtrlBMStromthreshold_Type(Integer32):
    """Custom type swL2TrafficCtrlBMStromthreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1024000),
    )


_SwL2TrafficCtrlBMStromthreshold_Type.__name__ = "Integer32"
_SwL2TrafficCtrlBMStromthreshold_Object = MibTableColumn
swL2TrafficCtrlBMStromthreshold = _SwL2TrafficCtrlBMStromthreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 11, 1, 1, 3),
    _SwL2TrafficCtrlBMStromthreshold_Type()
)
swL2TrafficCtrlBMStromthreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrafficCtrlBMStromthreshold.setStatus("current")


class _SwL2TrafficCtrlBcastStromCtrl_Type(Integer32):
    """Custom type swL2TrafficCtrlBcastStromCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL2TrafficCtrlBcastStromCtrl_Type.__name__ = "Integer32"
_SwL2TrafficCtrlBcastStromCtrl_Object = MibTableColumn
swL2TrafficCtrlBcastStromCtrl = _SwL2TrafficCtrlBcastStromCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 11, 1, 1, 4),
    _SwL2TrafficCtrlBcastStromCtrl_Type()
)
swL2TrafficCtrlBcastStromCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrafficCtrlBcastStromCtrl.setStatus("current")


class _SwL2TrafficCtrlMcastStromCtrl_Type(Integer32):
    """Custom type swL2TrafficCtrlMcastStromCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL2TrafficCtrlMcastStromCtrl_Type.__name__ = "Integer32"
_SwL2TrafficCtrlMcastStromCtrl_Object = MibTableColumn
swL2TrafficCtrlMcastStromCtrl = _SwL2TrafficCtrlMcastStromCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 11, 1, 1, 5),
    _SwL2TrafficCtrlMcastStromCtrl_Type()
)
swL2TrafficCtrlMcastStromCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrafficCtrlMcastStromCtrl.setStatus("current")


class _SwL2TrafficCtrlUcastStromCtrl_Type(Integer32):
    """Custom type swL2TrafficCtrlUcastStromCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL2TrafficCtrlUcastStromCtrl_Type.__name__ = "Integer32"
_SwL2TrafficCtrlUcastStromCtrl_Object = MibTableColumn
swL2TrafficCtrlUcastStromCtrl = _SwL2TrafficCtrlUcastStromCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 11, 1, 1, 6),
    _SwL2TrafficCtrlUcastStromCtrl_Type()
)
swL2TrafficCtrlUcastStromCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrafficCtrlUcastStromCtrl.setStatus("current")
_SwL2TrafficSegMgmt_ObjectIdentity = ObjectIdentity
swL2TrafficSegMgmt = _SwL2TrafficSegMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 12)
)
_SwL2TrafficSegTable_Object = MibTable
swL2TrafficSegTable = _SwL2TrafficSegTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 12, 1)
)
if mibBuilder.loadTexts:
    swL2TrafficSegTable.setStatus("current")
_SwL2TrafficSegEntry_Object = MibTableRow
swL2TrafficSegEntry = _SwL2TrafficSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 12, 1, 1)
)
swL2TrafficSegEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2TrafficSegPort"),
)
if mibBuilder.loadTexts:
    swL2TrafficSegEntry.setStatus("current")


class _SwL2TrafficSegPort_Type(Integer32):
    """Custom type swL2TrafficSegPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2TrafficSegPort_Type.__name__ = "Integer32"
_SwL2TrafficSegPort_Object = MibTableColumn
swL2TrafficSegPort = _SwL2TrafficSegPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 12, 1, 1, 1),
    _SwL2TrafficSegPort_Type()
)
swL2TrafficSegPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrafficSegPort.setStatus("current")
_SwL2TrafficSegForwardPorts_Type = PortList
_SwL2TrafficSegForwardPorts_Object = MibTableColumn
swL2TrafficSegForwardPorts = _SwL2TrafficSegForwardPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 12, 1, 1, 2),
    _SwL2TrafficSegForwardPorts_Type()
)
swL2TrafficSegForwardPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrafficSegForwardPorts.setStatus("current")
_SwL2PortSecurityMgmt_ObjectIdentity = ObjectIdentity
swL2PortSecurityMgmt = _SwL2PortSecurityMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 15)
)
_SwL2PortSecurityControlTable_Object = MibTable
swL2PortSecurityControlTable = _SwL2PortSecurityControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 15, 1)
)
if mibBuilder.loadTexts:
    swL2PortSecurityControlTable.setStatus("current")
_SwL2PortSecurityControlEntry_Object = MibTableRow
swL2PortSecurityControlEntry = _SwL2PortSecurityControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 15, 1, 1)
)
swL2PortSecurityControlEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2PortSecurityPortIndex"),
)
if mibBuilder.loadTexts:
    swL2PortSecurityControlEntry.setStatus("current")


class _SwL2PortSecurityPortIndex_Type(Integer32):
    """Custom type swL2PortSecurityPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwL2PortSecurityPortIndex_Type.__name__ = "Integer32"
_SwL2PortSecurityPortIndex_Object = MibTableColumn
swL2PortSecurityPortIndex = _SwL2PortSecurityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 15, 1, 1, 1),
    _SwL2PortSecurityPortIndex_Type()
)
swL2PortSecurityPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortSecurityPortIndex.setStatus("current")


class _SwL2PortSecurityMaxLernAddr_Type(Integer32):
    """Custom type swL2PortSecurityMaxLernAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SwL2PortSecurityMaxLernAddr_Type.__name__ = "Integer32"
_SwL2PortSecurityMaxLernAddr_Object = MibTableColumn
swL2PortSecurityMaxLernAddr = _SwL2PortSecurityMaxLernAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 15, 1, 1, 2),
    _SwL2PortSecurityMaxLernAddr_Type()
)
swL2PortSecurityMaxLernAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityMaxLernAddr.setStatus("current")


class _SwL2PortSecurityMode_Type(Integer32):
    """Custom type swL2PortSecurityMode based on Integer32"""
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
        *(("other", 1),
          ("permanent", 2),
          ("deleteOnTimeout", 3),
          ("deleteOnReset", 4))
    )


_SwL2PortSecurityMode_Type.__name__ = "Integer32"
_SwL2PortSecurityMode_Object = MibTableColumn
swL2PortSecurityMode = _SwL2PortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 15, 1, 1, 3),
    _SwL2PortSecurityMode_Type()
)
swL2PortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityMode.setStatus("current")


class _SwL2PortSecurityAdmState_Type(Integer32):
    """Custom type swL2PortSecurityAdmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("enable", 2),
          ("disable", 3))
    )


_SwL2PortSecurityAdmState_Type.__name__ = "Integer32"
_SwL2PortSecurityAdmState_Object = MibTableColumn
swL2PortSecurityAdmState = _SwL2PortSecurityAdmState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 15, 1, 1, 4),
    _SwL2PortSecurityAdmState_Type()
)
swL2PortSecurityAdmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityAdmState.setStatus("current")


class _SwL2PortSecurityTrapLogState_Type(Integer32):
    """Custom type swL2PortSecurityTrapLogState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("enable", 2),
          ("disable", 3))
    )


_SwL2PortSecurityTrapLogState_Type.__name__ = "Integer32"
_SwL2PortSecurityTrapLogState_Object = MibScalar
swL2PortSecurityTrapLogState = _SwL2PortSecurityTrapLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 15, 2),
    _SwL2PortSecurityTrapLogState_Type()
)
swL2PortSecurityTrapLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityTrapLogState.setStatus("current")
_SwL2StpMgmt_ObjectIdentity = ObjectIdentity
swL2StpMgmt = _SwL2StpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 16)
)


class _SwL2StpForwardBPDU_Type(Integer32):
    """Custom type swL2StpForwardBPDU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL2StpForwardBPDU_Type.__name__ = "Integer32"
_SwL2StpForwardBPDU_Object = MibScalar
swL2StpForwardBPDU = _SwL2StpForwardBPDU_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 16, 1),
    _SwL2StpForwardBPDU_Type()
)
swL2StpForwardBPDU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StpForwardBPDU.setStatus("current")


class _SwL2StpLbd_Type(Integer32):
    """Custom type swL2StpLbd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL2StpLbd_Type.__name__ = "Integer32"
_SwL2StpLbd_Object = MibScalar
swL2StpLbd = _SwL2StpLbd_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 16, 2),
    _SwL2StpLbd_Type()
)
swL2StpLbd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL2StpLbd.setStatus("obsolete")


class _SwL2StpLbdRecoverTime_Type(Integer32):
    """Custom type swL2StpLbdRecoverTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_SwL2StpLbdRecoverTime_Type.__name__ = "Integer32"
_SwL2StpLbdRecoverTime_Object = MibScalar
swL2StpLbdRecoverTime = _SwL2StpLbdRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 16, 3),
    _SwL2StpLbdRecoverTime_Type()
)
swL2StpLbdRecoverTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL2StpLbdRecoverTime.setStatus("obsolete")
_SwL2StpPortTable_Object = MibTable
swL2StpPortTable = _SwL2StpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 16, 4)
)
if mibBuilder.loadTexts:
    swL2StpPortTable.setStatus("current")
_SwL2StpPortEntry_Object = MibTableRow
swL2StpPortEntry = _SwL2StpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 16, 4, 1)
)
swL2StpPortEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2StpPort"),
)
if mibBuilder.loadTexts:
    swL2StpPortEntry.setStatus("current")


class _SwL2StpPort_Type(Integer32):
    """Custom type swL2StpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL2StpPort_Type.__name__ = "Integer32"
_SwL2StpPort_Object = MibTableColumn
swL2StpPort = _SwL2StpPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 16, 4, 1, 1),
    _SwL2StpPort_Type()
)
swL2StpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2StpPort.setStatus("current")


class _SwL2StpPortLbd_Type(Integer32):
    """Custom type swL2StpPortLbd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL2StpPortLbd_Type.__name__ = "Integer32"
_SwL2StpPortLbd_Object = MibTableColumn
swL2StpPortLbd = _SwL2StpPortLbd_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 16, 4, 1, 2),
    _SwL2StpPortLbd_Type()
)
swL2StpPortLbd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL2StpPortLbd.setStatus("obsolete")


class _SwL2StpPortStatus_Type(Integer32):
    """Custom type swL2StpPortStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("discarding", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("broken", 6),
          ("no-stp-enabled", 7),
          ("err-disabled", 8))
    )


_SwL2StpPortStatus_Type.__name__ = "Integer32"
_SwL2StpPortStatus_Object = MibTableColumn
swL2StpPortStatus = _SwL2StpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 16, 4, 1, 3),
    _SwL2StpPortStatus_Type()
)
swL2StpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2StpPortStatus.setStatus("current")


class _SwL2StpPortRole_Type(Integer32):
    """Custom type swL2StpPortRole based on Integer32"""
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
        *(("disabled", 1),
          ("alternate", 2),
          ("backup", 3),
          ("root", 4),
          ("designated", 5),
          ("nonStp", 6),
          ("loopback", 7))
    )


_SwL2StpPortRole_Type.__name__ = "Integer32"
_SwL2StpPortRole_Object = MibTableColumn
swL2StpPortRole = _SwL2StpPortRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 16, 4, 1, 4),
    _SwL2StpPortRole_Type()
)
swL2StpPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2StpPortRole.setStatus("current")


class _SwL2StpPortFBPDU_Type(Integer32):
    """Custom type swL2StpPortFBPDU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL2StpPortFBPDU_Type.__name__ = "Integer32"
_SwL2StpPortFBPDU_Object = MibTableColumn
swL2StpPortFBPDU = _SwL2StpPortFBPDU_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 16, 4, 1, 5),
    _SwL2StpPortFBPDU_Type()
)
swL2StpPortFBPDU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StpPortFBPDU.setStatus("current")


class _SwL2StpPortLinkState_Type(Integer32):
    """Custom type swL2StpPortLinkState based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("link-down", 1),
          ("half-10Mbps-none", 2),
          ("half-10Mbps-backp", 3),
          ("full-10Mbps-none", 4),
          ("full-10Mbps-8023x", 5),
          ("half-100Mbps-none", 6),
          ("half-100Mbps-backp", 7),
          ("full-100Mbps-none", 8),
          ("full-100Mbps-8023x", 9),
          ("half-1000Mbps-none", 10),
          ("full-1000Mbps-backp", 11),
          ("full-1000Mbps-none", 12),
          ("full-1000Mbps-8023x", 13))
    )


_SwL2StpPortLinkState_Type.__name__ = "Integer32"
_SwL2StpPortLinkState_Object = MibTableColumn
swL2StpPortLinkState = _SwL2StpPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 16, 4, 1, 6),
    _SwL2StpPortLinkState_Type()
)
swL2StpPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2StpPortLinkState.setStatus("current")
_SwL2StpPortProtocolMigration_Type = TruthValue
_SwL2StpPortProtocolMigration_Object = MibTableColumn
swL2StpPortProtocolMigration = _SwL2StpPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 16, 4, 1, 7),
    _SwL2StpPortProtocolMigration_Type()
)
swL2StpPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StpPortProtocolMigration.setStatus("current")


class _SwL2StpPortAdminEdgePort_Type(Integer32):
    """Custom type swL2StpPortAdminEdgePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceTrue", 0),
          ("forceFalse", 1),
          ("auto", 2))
    )


_SwL2StpPortAdminEdgePort_Type.__name__ = "Integer32"
_SwL2StpPortAdminEdgePort_Object = MibTableColumn
swL2StpPortAdminEdgePort = _SwL2StpPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 16, 4, 1, 8),
    _SwL2StpPortAdminEdgePort_Type()
)
swL2StpPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StpPortAdminEdgePort.setStatus("current")
_SwL2StpPortOperEdgePort_Type = TruthValue
_SwL2StpPortOperEdgePort_Object = MibTableColumn
swL2StpPortOperEdgePort = _SwL2StpPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 16, 4, 1, 9),
    _SwL2StpPortOperEdgePort_Type()
)
swL2StpPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2StpPortOperEdgePort.setStatus("current")


class _SwL2StpPortAdminPointToPoint_Type(Integer32):
    """Custom type swL2StpPortAdminPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceTrue", 0),
          ("forceFalse", 1),
          ("auto", 2))
    )


_SwL2StpPortAdminPointToPoint_Type.__name__ = "Integer32"
_SwL2StpPortAdminPointToPoint_Object = MibTableColumn
swL2StpPortAdminPointToPoint = _SwL2StpPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 16, 4, 1, 10),
    _SwL2StpPortAdminPointToPoint_Type()
)
swL2StpPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StpPortAdminPointToPoint.setStatus("current")
_SwL2StpPortOperPointToPoint_Type = TruthValue
_SwL2StpPortOperPointToPoint_Object = MibTableColumn
swL2StpPortOperPointToPoint = _SwL2StpPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 16, 4, 1, 11),
    _SwL2StpPortOperPointToPoint_Type()
)
swL2StpPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2StpPortOperPointToPoint.setStatus("current")


class _SwL2StpPortAdminPathCost_Type(Unsigned32):
    """Custom type swL2StpPortAdminPathCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_SwL2StpPortAdminPathCost_Type.__name__ = "Unsigned32"
_SwL2StpPortAdminPathCost_Object = MibTableColumn
swL2StpPortAdminPathCost = _SwL2StpPortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 16, 4, 1, 12),
    _SwL2StpPortAdminPathCost_Type()
)
swL2StpPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StpPortAdminPathCost.setStatus("current")


class _SwL2StpPortPriority_Type(Integer32):
    """Custom type swL2StpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_SwL2StpPortPriority_Type.__name__ = "Integer32"
_SwL2StpPortPriority_Object = MibTableColumn
swL2StpPortPriority = _SwL2StpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 16, 4, 1, 13),
    _SwL2StpPortPriority_Type()
)
swL2StpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StpPortPriority.setStatus("current")


class _SwL2STPPortState_Type(Integer32):
    """Custom type swL2STPPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwL2STPPortState_Type.__name__ = "Integer32"
_SwL2STPPortState_Object = MibTableColumn
swL2STPPortState = _SwL2STPPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 16, 4, 1, 14),
    _SwL2STPPortState_Type()
)
swL2STPPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2STPPortState.setStatus("current")
_SwL2StpPortRestrictedRole_Type = TruthValue
_SwL2StpPortRestrictedRole_Object = MibTableColumn
swL2StpPortRestrictedRole = _SwL2StpPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 16, 4, 1, 15),
    _SwL2StpPortRestrictedRole_Type()
)
swL2StpPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StpPortRestrictedRole.setStatus("current")
_SwL2StpPortRestrictedTCN_Type = TruthValue
_SwL2StpPortRestrictedTCN_Object = MibTableColumn
swL2StpPortRestrictedTCN = _SwL2StpPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 16, 4, 1, 16),
    _SwL2StpPortRestrictedTCN_Type()
)
swL2StpPortRestrictedTCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2StpPortRestrictedTCN.setStatus("current")
_SwL2CosMgmt_ObjectIdentity = ObjectIdentity
swL2CosMgmt = _SwL2CosMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17)
)
_SwL2CosPriorityCtrl_ObjectIdentity = ObjectIdentity
swL2CosPriorityCtrl = _SwL2CosPriorityCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3)
)
_SwL2CosPriorityTable_Object = MibTable
swL2CosPriorityTable = _SwL2CosPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 1)
)
if mibBuilder.loadTexts:
    swL2CosPriorityTable.setStatus("current")
_SwL2CosPriorityEntry_Object = MibTableRow
swL2CosPriorityEntry = _SwL2CosPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 1, 1)
)
swL2CosPriorityEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2CosPriorityPort"),
)
if mibBuilder.loadTexts:
    swL2CosPriorityEntry.setStatus("current")


class _SwL2CosPriorityPort_Type(Integer32):
    """Custom type swL2CosPriorityPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL2CosPriorityPort_Type.__name__ = "Integer32"
_SwL2CosPriorityPort_Object = MibTableColumn
swL2CosPriorityPort = _SwL2CosPriorityPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 1, 1, 1),
    _SwL2CosPriorityPort_Type()
)
swL2CosPriorityPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2CosPriorityPort.setStatus("current")


class _SwL2CosPriorityPortPRI_Type(Integer32):
    """Custom type swL2CosPriorityPortPRI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disable", 2),
          ("enable", 3))
    )


_SwL2CosPriorityPortPRI_Type.__name__ = "Integer32"
_SwL2CosPriorityPortPRI_Object = MibTableColumn
swL2CosPriorityPortPRI = _SwL2CosPriorityPortPRI_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 1, 1, 2),
    _SwL2CosPriorityPortPRI_Type()
)
swL2CosPriorityPortPRI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2CosPriorityPortPRI.setStatus("current")


class _SwL2CosPriorityEtherPRI_Type(Integer32):
    """Custom type swL2CosPriorityEtherPRI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("ether8021p", 2),
          ("macBase", 3))
    )


_SwL2CosPriorityEtherPRI_Type.__name__ = "Integer32"
_SwL2CosPriorityEtherPRI_Object = MibTableColumn
swL2CosPriorityEtherPRI = _SwL2CosPriorityEtherPRI_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 1, 1, 3),
    _SwL2CosPriorityEtherPRI_Type()
)
swL2CosPriorityEtherPRI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2CosPriorityEtherPRI.setStatus("current")


class _SwL2CosPriorityIpPRI_Type(Integer32):
    """Custom type swL2CosPriorityIpPRI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("tos", 2),
          ("dscp", 3))
    )


_SwL2CosPriorityIpPRI_Type.__name__ = "Integer32"
_SwL2CosPriorityIpPRI_Object = MibTableColumn
swL2CosPriorityIpPRI = _SwL2CosPriorityIpPRI_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 1, 1, 4),
    _SwL2CosPriorityIpPRI_Type()
)
swL2CosPriorityIpPRI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2CosPriorityIpPRI.setStatus("current")


class _SwL2CosPriorityNone_Type(Integer32):
    """Custom type swL2CosPriorityNone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_SwL2CosPriorityNone_Type.__name__ = "Integer32"
_SwL2CosPriorityNone_Object = MibTableColumn
swL2CosPriorityNone = _SwL2CosPriorityNone_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 1, 1, 5),
    _SwL2CosPriorityNone_Type()
)
swL2CosPriorityNone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2CosPriorityNone.setStatus("current")
_SwL2CosPortPRITable_Object = MibTable
swL2CosPortPRITable = _SwL2CosPortPRITable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 2)
)
if mibBuilder.loadTexts:
    swL2CosPortPRITable.setStatus("current")
_SwL2CosPortPRIEntry_Object = MibTableRow
swL2CosPortPRIEntry = _SwL2CosPortPRIEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 2, 1)
)
swL2CosPortPRIEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2CosPortPRIIndex"),
)
if mibBuilder.loadTexts:
    swL2CosPortPRIEntry.setStatus("current")


class _SwL2CosPortPRIIndex_Type(Integer32):
    """Custom type swL2CosPortPRIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL2CosPortPRIIndex_Type.__name__ = "Integer32"
_SwL2CosPortPRIIndex_Object = MibTableColumn
swL2CosPortPRIIndex = _SwL2CosPortPRIIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 2, 1, 1),
    _SwL2CosPortPRIIndex_Type()
)
swL2CosPortPRIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2CosPortPRIIndex.setStatus("current")


class _SwL2CosPortPRIClass_Type(Integer32):
    """Custom type swL2CosPortPRIClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SwL2CosPortPRIClass_Type.__name__ = "Integer32"
_SwL2CosPortPRIClass_Object = MibTableColumn
swL2CosPortPRIClass = _SwL2CosPortPRIClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 2, 1, 2),
    _SwL2CosPortPRIClass_Type()
)
swL2CosPortPRIClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2CosPortPRIClass.setStatus("current")
_SwL2CosMacBasePRITable_Object = MibTable
swL2CosMacBasePRITable = _SwL2CosMacBasePRITable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 3)
)
if mibBuilder.loadTexts:
    swL2CosMacBasePRITable.setStatus("current")
_SwL2CosMacBasePRIEntry_Object = MibTableRow
swL2CosMacBasePRIEntry = _SwL2CosMacBasePRIEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 3, 1)
)
swL2CosMacBasePRIEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2CosMacBasePRIIndex"),
)
if mibBuilder.loadTexts:
    swL2CosMacBasePRIEntry.setStatus("current")
_SwL2CosMacBasePRIIndex_Type = MacAddress
_SwL2CosMacBasePRIIndex_Object = MibTableColumn
swL2CosMacBasePRIIndex = _SwL2CosMacBasePRIIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 3, 1, 1),
    _SwL2CosMacBasePRIIndex_Type()
)
swL2CosMacBasePRIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2CosMacBasePRIIndex.setStatus("current")


class _SwL2CosMacBasePRIClass_Type(Integer32):
    """Custom type swL2CosMacBasePRIClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SwL2CosMacBasePRIClass_Type.__name__ = "Integer32"
_SwL2CosMacBasePRIClass_Object = MibTableColumn
swL2CosMacBasePRIClass = _SwL2CosMacBasePRIClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 3, 1, 2),
    _SwL2CosMacBasePRIClass_Type()
)
swL2CosMacBasePRIClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2CosMacBasePRIClass.setStatus("current")
_SwL2CosTosPRITable_Object = MibTable
swL2CosTosPRITable = _SwL2CosTosPRITable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 4)
)
if mibBuilder.loadTexts:
    swL2CosTosPRITable.setStatus("current")
_SwL2CosTosPRIEntry_Object = MibTableRow
swL2CosTosPRIEntry = _SwL2CosTosPRIEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 4, 1)
)
swL2CosTosPRIEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2CosTosPRIIndex"),
)
if mibBuilder.loadTexts:
    swL2CosTosPRIEntry.setStatus("current")


class _SwL2CosTosPRIIndex_Type(Integer32):
    """Custom type swL2CosTosPRIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwL2CosTosPRIIndex_Type.__name__ = "Integer32"
_SwL2CosTosPRIIndex_Object = MibTableColumn
swL2CosTosPRIIndex = _SwL2CosTosPRIIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 4, 1, 1),
    _SwL2CosTosPRIIndex_Type()
)
swL2CosTosPRIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2CosTosPRIIndex.setStatus("current")


class _SwL2CosTosPRIClass_Type(Integer32):
    """Custom type swL2CosTosPRIClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SwL2CosTosPRIClass_Type.__name__ = "Integer32"
_SwL2CosTosPRIClass_Object = MibTableColumn
swL2CosTosPRIClass = _SwL2CosTosPRIClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 4, 1, 2),
    _SwL2CosTosPRIClass_Type()
)
swL2CosTosPRIClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2CosTosPRIClass.setStatus("current")
_SwL2CosDscpPRITable_Object = MibTable
swL2CosDscpPRITable = _SwL2CosDscpPRITable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 5)
)
if mibBuilder.loadTexts:
    swL2CosDscpPRITable.setStatus("current")
_SwL2CosDscpPRIEntry_Object = MibTableRow
swL2CosDscpPRIEntry = _SwL2CosDscpPRIEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 5, 1)
)
swL2CosDscpPRIEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2CosDscpPRIIndex"),
)
if mibBuilder.loadTexts:
    swL2CosDscpPRIEntry.setStatus("current")


class _SwL2CosDscpPRIIndex_Type(Integer32):
    """Custom type swL2CosDscpPRIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwL2CosDscpPRIIndex_Type.__name__ = "Integer32"
_SwL2CosDscpPRIIndex_Object = MibTableColumn
swL2CosDscpPRIIndex = _SwL2CosDscpPRIIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 5, 1, 1),
    _SwL2CosDscpPRIIndex_Type()
)
swL2CosDscpPRIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2CosDscpPRIIndex.setStatus("current")


class _SwL2CosDscpPRIClass_Type(Integer32):
    """Custom type swL2CosDscpPRIClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SwL2CosDscpPRIClass_Type.__name__ = "Integer32"
_SwL2CosDscpPRIClass_Object = MibTableColumn
swL2CosDscpPRIClass = _SwL2CosDscpPRIClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 17, 3, 5, 1, 2),
    _SwL2CosDscpPRIClass_Type()
)
swL2CosDscpPRIClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2CosDscpPRIClass.setStatus("current")
_SwL2LoopDetectMgmt_ObjectIdentity = ObjectIdentity
swL2LoopDetectMgmt = _SwL2LoopDetectMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 18)
)
_SwL2LoopDetectCtrl_ObjectIdentity = ObjectIdentity
swL2LoopDetectCtrl = _SwL2LoopDetectCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 18, 1)
)


class _SwL2LoopDetectAdminState_Type(Integer32):
    """Custom type swL2LoopDetectAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwL2LoopDetectAdminState_Type.__name__ = "Integer32"
_SwL2LoopDetectAdminState_Object = MibScalar
swL2LoopDetectAdminState = _SwL2LoopDetectAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 18, 1, 1),
    _SwL2LoopDetectAdminState_Type()
)
swL2LoopDetectAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LoopDetectAdminState.setStatus("current")


class _SwL2LoopDetectInterval_Type(Integer32):
    """Custom type swL2LoopDetectInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_SwL2LoopDetectInterval_Type.__name__ = "Integer32"
_SwL2LoopDetectInterval_Object = MibScalar
swL2LoopDetectInterval = _SwL2LoopDetectInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 18, 1, 2),
    _SwL2LoopDetectInterval_Type()
)
swL2LoopDetectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LoopDetectInterval.setStatus("current")


class _SwL2LoopDetectRecoverTime_Type(Integer32):
    """Custom type swL2LoopDetectRecoverTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_SwL2LoopDetectRecoverTime_Type.__name__ = "Integer32"
_SwL2LoopDetectRecoverTime_Object = MibScalar
swL2LoopDetectRecoverTime = _SwL2LoopDetectRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 18, 1, 3),
    _SwL2LoopDetectRecoverTime_Type()
)
swL2LoopDetectRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LoopDetectRecoverTime.setStatus("current")
_SwL2LoopDetectPortMgmt_ObjectIdentity = ObjectIdentity
swL2LoopDetectPortMgmt = _SwL2LoopDetectPortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 18, 2)
)
_SwL2LoopDetectPortTable_Object = MibTable
swL2LoopDetectPortTable = _SwL2LoopDetectPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 18, 2, 1)
)
if mibBuilder.loadTexts:
    swL2LoopDetectPortTable.setStatus("current")
_SwL2LoopDetectPortEntry_Object = MibTableRow
swL2LoopDetectPortEntry = _SwL2LoopDetectPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 18, 2, 1, 1)
)
swL2LoopDetectPortEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2LoopDetectPortIndex"),
)
if mibBuilder.loadTexts:
    swL2LoopDetectPortEntry.setStatus("current")


class _SwL2LoopDetectPortIndex_Type(Integer32):
    """Custom type swL2LoopDetectPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL2LoopDetectPortIndex_Type.__name__ = "Integer32"
_SwL2LoopDetectPortIndex_Object = MibTableColumn
swL2LoopDetectPortIndex = _SwL2LoopDetectPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 18, 2, 1, 1, 1),
    _SwL2LoopDetectPortIndex_Type()
)
swL2LoopDetectPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2LoopDetectPortIndex.setStatus("current")


class _SwL2LoopDetectPortState_Type(Integer32):
    """Custom type swL2LoopDetectPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwL2LoopDetectPortState_Type.__name__ = "Integer32"
_SwL2LoopDetectPortState_Object = MibTableColumn
swL2LoopDetectPortState = _SwL2LoopDetectPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 18, 2, 1, 1, 2),
    _SwL2LoopDetectPortState_Type()
)
swL2LoopDetectPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LoopDetectPortState.setStatus("current")


class _SwL2LoopDetectPortLoopStatus_Type(Integer32):
    """Custom type swL2LoopDetectPortLoopStatus based on Integer32"""
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
          ("loop", 2),
          ("error", 3))
    )


_SwL2LoopDetectPortLoopStatus_Type.__name__ = "Integer32"
_SwL2LoopDetectPortLoopStatus_Object = MibTableColumn
swL2LoopDetectPortLoopStatus = _SwL2LoopDetectPortLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 18, 2, 1, 1, 4),
    _SwL2LoopDetectPortLoopStatus_Type()
)
swL2LoopDetectPortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2LoopDetectPortLoopStatus.setStatus("current")
_SwL2VLANMgmt_ObjectIdentity = ObjectIdentity
swL2VLANMgmt = _SwL2VLANMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 19)
)
_SwL2VlanTable_Object = MibTable
swL2VlanTable = _SwL2VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 19, 1)
)
if mibBuilder.loadTexts:
    swL2VlanTable.setStatus("current")
_SwL2VlanEntry_Object = MibTableRow
swL2VlanEntry = _SwL2VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 19, 1, 1)
)
swL2VlanEntry.setIndexNames(
    (0, "DES3026-L2MGMT-MIB", "swL2VlanIndex"),
)
if mibBuilder.loadTexts:
    swL2VlanEntry.setStatus("current")
_SwL2VlanIndex_Type = VlanId
_SwL2VlanIndex_Object = MibTableColumn
swL2VlanIndex = _SwL2VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 19, 1, 1, 1),
    _SwL2VlanIndex_Type()
)
swL2VlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanIndex.setStatus("current")


class _SwL2VlanName_Type(DisplayString):
    """Custom type swL2VlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwL2VlanName_Type.__name__ = "DisplayString"
_SwL2VlanName_Object = MibTableColumn
swL2VlanName = _SwL2VlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 19, 1, 1, 2),
    _SwL2VlanName_Type()
)
swL2VlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanName.setStatus("current")


class _SwL2VlanType_Type(Integer32):
    """Custom type swL2VlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 0),
          ("static", 1))
    )


_SwL2VlanType_Type.__name__ = "Integer32"
_SwL2VlanType_Object = MibTableColumn
swL2VlanType = _SwL2VlanType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 19, 1, 1, 3),
    _SwL2VlanType_Type()
)
swL2VlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanType.setStatus("current")
_SwL2VlanMemberPorts_Type = PortList
_SwL2VlanMemberPorts_Object = MibTableColumn
swL2VlanMemberPorts = _SwL2VlanMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 19, 1, 1, 4),
    _SwL2VlanMemberPorts_Type()
)
swL2VlanMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanMemberPorts.setStatus("current")
_SwL2VlanStaticPorts_Type = PortList
_SwL2VlanStaticPorts_Object = MibTableColumn
swL2VlanStaticPorts = _SwL2VlanStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 19, 1, 1, 5),
    _SwL2VlanStaticPorts_Type()
)
swL2VlanStaticPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanStaticPorts.setStatus("current")
_SwL2VlanUntaggedPorts_Type = PortList
_SwL2VlanUntaggedPorts_Object = MibTableColumn
swL2VlanUntaggedPorts = _SwL2VlanUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 19, 1, 1, 6),
    _SwL2VlanUntaggedPorts_Type()
)
swL2VlanUntaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanUntaggedPorts.setStatus("current")
_SwL2VlanTaggedPorts_Type = PortList
_SwL2VlanTaggedPorts_Object = MibTableColumn
swL2VlanTaggedPorts = _SwL2VlanTaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 19, 1, 1, 7),
    _SwL2VlanTaggedPorts_Type()
)
swL2VlanTaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanTaggedPorts.setStatus("current")
_SwL2MgmtMIBTraps_ObjectIdentity = ObjectIdentity
swL2MgmtMIBTraps = _SwL2MgmtMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 100)
)
_SwL2Notify_ObjectIdentity = ObjectIdentity
swL2Notify = _SwL2Notify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 100, 1)
)
_SwL2NotifyPrefix_ObjectIdentity = ObjectIdentity
swL2NotifyPrefix = _SwL2NotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 100, 1, 2)
)
_SwL2NotifFirmware_ObjectIdentity = ObjectIdentity
swL2NotifFirmware = _SwL2NotifFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 100, 1, 2, 0)
)
_Swl2NotificationBidings_ObjectIdentity = ObjectIdentity
swl2NotificationBidings = _Swl2NotificationBidings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 100, 1, 2, 1)
)


class _SwL2macNotifyInfo_Type(OctetString):
    """Custom type swL2macNotifyInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SwL2macNotifyInfo_Type.__name__ = "OctetString"
_SwL2macNotifyInfo_Object = MibScalar
swL2macNotifyInfo = _SwL2macNotifyInfo_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 100, 1, 2, 1, 1),
    _SwL2macNotifyInfo_Type()
)
swL2macNotifyInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2macNotifyInfo.setStatus("current")
_SwL2PortSecurityViolationMac_Type = MacAddress
_SwL2PortSecurityViolationMac_Object = MibScalar
swL2PortSecurityViolationMac = _SwL2PortSecurityViolationMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 100, 1, 2, 1, 2),
    _SwL2PortSecurityViolationMac_Type()
)
swL2PortSecurityViolationMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swL2PortSecurityViolationMac.setStatus("current")

# Managed Objects groups


# Notification objects

swL2macNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 100, 1, 2, 0, 1)
)
swL2macNotification.setObjects(
    ("DES3026-L2MGMT-MIB", "swL2macNotifyInfo")
)
if mibBuilder.loadTexts:
    swL2macNotification.setStatus(
        "current"
    )

swL2PortSecurityViolationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3, 2, 100, 1, 2, 0, 2)
)
swL2PortSecurityViolationTrap.setObjects(
      *(("DES3026-L2MGMT-MIB", "swL2PortSecurityPortIndex"),
        ("DES3026-L2MGMT-MIB", "swL2PortSecurityViolationMac"))
)
if mibBuilder.loadTexts:
    swL2PortSecurityViolationTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES3026-L2MGMT-MIB",
    **{"VlanId": VlanId,
       "PortList": PortList,
       "MacAddress": MacAddress,
       "swL2MgmtMIB": swL2MgmtMIB,
       "swL2DevMgmt": swL2DevMgmt,
       "swL2DevInfo": swL2DevInfo,
       "swL2DevInfoFrontPanelLedStatus": swL2DevInfoFrontPanelLedStatus,
       "swL2Module-1-Type": swL2Module_1_Type,
       "swL2Module-2-Type": swL2Module_2_Type,
       "swL2DevCtrl": swL2DevCtrl,
       "swL2DevCtrlSystemReboot": swL2DevCtrlSystemReboot,
       "swL2DevCtrlSystemIP": swL2DevCtrlSystemIP,
       "swL2DevCtrlSubnetMask": swL2DevCtrlSubnetMask,
       "swL2DevCtrlDefaultGateway": swL2DevCtrlDefaultGateway,
       "swL2DevCtrlManagementVlanId": swL2DevCtrlManagementVlanId,
       "swL2DevCtrlStpState": swL2DevCtrlStpState,
       "swL2DevCtrlIGMPSnooping": swL2DevCtrlIGMPSnooping,
       "swL2DevCtrlCleanAllStatisticCounter": swL2DevCtrlCleanAllStatisticCounter,
       "swL2DevCtrlSnmpEnableAuthenTraps": swL2DevCtrlSnmpEnableAuthenTraps,
       "swL2DevCtrlRmonState": swL2DevCtrlRmonState,
       "swL2DevCtrlIpAutoConfig": swL2DevCtrlIpAutoConfig,
       "swL2PortCtrlMulticastfilter": swL2PortCtrlMulticastfilter,
       "swL2MACNotifyState": swL2MACNotifyState,
       "swL2MACNotifyHistorySize": swL2MACNotifyHistorySize,
       "swL2MACNotifyInterval": swL2MACNotifyInterval,
       "swL2DevCtrlVLANTrunkState": swL2DevCtrlVLANTrunkState,
       "swL2DevCtrlLLDPState": swL2DevCtrlLLDPState,
       "swL2DevCtrlLLDPForwardMessageState": swL2DevCtrlLLDPForwardMessageState,
       "swL2DevCtrlVlanIdOfFDBTbl": swL2DevCtrlVlanIdOfFDBTbl,
       "swL2CPUutilization": swL2CPUutilization,
       "swL2CPUutilizationIn5sec": swL2CPUutilizationIn5sec,
       "swL2CPUutilizationIn1min": swL2CPUutilizationIn1min,
       "swL2CPUutilizationIn5min": swL2CPUutilizationIn5min,
       "swL2DevAlarm": swL2DevAlarm,
       "swL2DevAlarmLinkChange": swL2DevAlarmLinkChange,
       "swL2PortMgmt": swL2PortMgmt,
       "swL2PortInfoTable": swL2PortInfoTable,
       "swL2PortInfoEntry": swL2PortInfoEntry,
       "swL2PortInfoPortIndex": swL2PortInfoPortIndex,
       "swL2PortInfoLinkStatus": swL2PortInfoLinkStatus,
       "swL2PortInfoNwayStatus": swL2PortInfoNwayStatus,
       "swL2PortCtrlTable": swL2PortCtrlTable,
       "swL2PortCtrlEntry": swL2PortCtrlEntry,
       "swL2PortCtrlPortIndex": swL2PortCtrlPortIndex,
       "swL2PortCtrlAdminState": swL2PortCtrlAdminState,
       "swL2PortCtrlNwayState": swL2PortCtrlNwayState,
       "swL2PortCtrlFlowCtrlState": swL2PortCtrlFlowCtrlState,
       "swL2PortCtrlDescription": swL2PortCtrlDescription,
       "swL2PortCtrlMACNotifyState": swL2PortCtrlMACNotifyState,
       "swL2PortCtrlMDIXState": swL2PortCtrlMDIXState,
       "swL2PortErrTable": swL2PortErrTable,
       "swL2PortErrEntry": swL2PortErrEntry,
       "swL2PortErrPortIndex": swL2PortErrPortIndex,
       "swL2PortErrPortState": swL2PortErrPortState,
       "swL2PortErrPortStatus": swL2PortErrPortStatus,
       "swL2PortErrPortReason": swL2PortErrPortReason,
       "swL2PortErrDescription": swL2PortErrDescription,
       "swL2QOSMgmt": swL2QOSMgmt,
       "swL2QOSBandwidthControlTable": swL2QOSBandwidthControlTable,
       "swL2QOSBandwidthControlEntry": swL2QOSBandwidthControlEntry,
       "swL2QOSBandwidthPortIndex": swL2QOSBandwidthPortIndex,
       "swL2QOSBandwidthRxRate": swL2QOSBandwidthRxRate,
       "swL2QOSBandwidthTxRate": swL2QOSBandwidthTxRate,
       "swL2QOSBandwidthRadiusRxRate": swL2QOSBandwidthRadiusRxRate,
       "swL2QOSBandwidthRadiusTxRate": swL2QOSBandwidthRadiusTxRate,
       "swL2QOSSchedulingTable": swL2QOSSchedulingTable,
       "swL2QOSSchedulingEntry": swL2QOSSchedulingEntry,
       "swL2QOSSchedulingClassIndex": swL2QOSSchedulingClassIndex,
       "swL2QOSSchedulingMaxWeight": swL2QOSSchedulingMaxWeight,
       "swL2QOS8021pUserPriorityTable": swL2QOS8021pUserPriorityTable,
       "swL2QOS8021pUserPriorityEntry": swL2QOS8021pUserPriorityEntry,
       "swL2QOS8021pUserPriorityIndex": swL2QOS8021pUserPriorityIndex,
       "swL2QOS8021pUserPriorityClass": swL2QOS8021pUserPriorityClass,
       "swL2QOS8021pDefaultPriorityTable": swL2QOS8021pDefaultPriorityTable,
       "swL2QOS8021pDefaultPriorityEntry": swL2QOS8021pDefaultPriorityEntry,
       "swL2QOS8021pDefaultPriorityIndex": swL2QOS8021pDefaultPriorityIndex,
       "swL2QOS8021pDefaultPriority": swL2QOS8021pDefaultPriority,
       "swL2QOS8021pRadiusPriority": swL2QOS8021pRadiusPriority,
       "swL2QOSSchedulingMechanismCtrl": swL2QOSSchedulingMechanismCtrl,
       "swL2TrunkMgmt": swL2TrunkMgmt,
       "swPortTrunkMaxEntries": swPortTrunkMaxEntries,
       "swPortTrunkMaxPortMembers": swPortTrunkMaxPortMembers,
       "swPortTrunkTable": swPortTrunkTable,
       "swPortTrunkEntry": swPortTrunkEntry,
       "swPortTrunkIndex": swPortTrunkIndex,
       "swPortTrunkMasterPort": swPortTrunkMasterPort,
       "swPortTrunkPortList": swPortTrunkPortList,
       "swPortTrunkType": swPortTrunkType,
       "swPortTrunkActivePort": swPortTrunkActivePort,
       "swPortTrunkState": swPortTrunkState,
       "swPortTrunkFloodingPort": swPortTrunkFloodingPort,
       "swL2TrunkAlgorithm": swL2TrunkAlgorithm,
       "swL2TrunkLACPPortTable": swL2TrunkLACPPortTable,
       "swL2TrunkLACPPortEntry": swL2TrunkLACPPortEntry,
       "swL2TrunkLACPPortIndex": swL2TrunkLACPPortIndex,
       "swL2TrunkLACPPortState": swL2TrunkLACPPortState,
       "swL2TrunkVLANTable": swL2TrunkVLANTable,
       "swL2TrunkVLANEntry": swL2TrunkVLANEntry,
       "swL2TrunkVLANPort": swL2TrunkVLANPort,
       "swL2TrunkVLANState": swL2TrunkVLANState,
       "swPortMirrorPackage": swPortMirrorPackage,
       "swPortMirrorRxPortList": swPortMirrorRxPortList,
       "swPortMirrorTxPortList": swPortMirrorTxPortList,
       "swPortMirrorTargetPort": swPortMirrorTargetPort,
       "swPortMirrorState": swPortMirrorState,
       "swIGMPPackage": swIGMPPackage,
       "swL2IGMPMaxSupportedVlans": swL2IGMPMaxSupportedVlans,
       "swL2IGMPMaxIpGroupNumPerVlan": swL2IGMPMaxIpGroupNumPerVlan,
       "swL2IGMPCtrlTable": swL2IGMPCtrlTable,
       "swL2IGMPCtrlEntry": swL2IGMPCtrlEntry,
       "swL2IGMPCtrlVid": swL2IGMPCtrlVid,
       "swL2IGMPQueryInterval": swL2IGMPQueryInterval,
       "swL2IGMPMaxResponseTime": swL2IGMPMaxResponseTime,
       "swL2IGMPRobustness": swL2IGMPRobustness,
       "swL2IGMPLastMemberQueryInterval": swL2IGMPLastMemberQueryInterval,
       "swL2IGMPHostTimeout": swL2IGMPHostTimeout,
       "swL2IGMPRouteTimeout": swL2IGMPRouteTimeout,
       "swL2IGMPLeaveTimer": swL2IGMPLeaveTimer,
       "swL2IGMPQueryState": swL2IGMPQueryState,
       "swL2IGMPCurrentState": swL2IGMPCurrentState,
       "swL2IGMPCtrlState": swL2IGMPCtrlState,
       "swL2IGMPFastLeave": swL2IGMPFastLeave,
       "swL2IGMPQueryInfoTable": swL2IGMPQueryInfoTable,
       "swL2IGMPQueryInfoEntry": swL2IGMPQueryInfoEntry,
       "swL2IGMPInfoVid": swL2IGMPInfoVid,
       "swL2IGMPInfoQueryCount": swL2IGMPInfoQueryCount,
       "swL2IGMPInfoTxQueryCount": swL2IGMPInfoTxQueryCount,
       "swL2IGMPInfoTable": swL2IGMPInfoTable,
       "swL2IGMPInfoEntry": swL2IGMPInfoEntry,
       "swL2IGMPVid": swL2IGMPVid,
       "swL2IGMPGroupIpAddr": swL2IGMPGroupIpAddr,
       "swL2IGMPMacAddr": swL2IGMPMacAddr,
       "swL2IGMPPortMap": swL2IGMPPortMap,
       "swL2IGMPIpGroupReportCount": swL2IGMPIpGroupReportCount,
       "swL2IGMPRouterPortTable": swL2IGMPRouterPortTable,
       "swL2IGMPRouterPortEntry": swL2IGMPRouterPortEntry,
       "swL2IGMPRouterPortVlanid": swL2IGMPRouterPortVlanid,
       "swL2IGMPRouterPortVlanName": swL2IGMPRouterPortVlanName,
       "swL2IGMPRouterPortStaticPortList": swL2IGMPRouterPortStaticPortList,
       "swL2IGMPRouterPortDynamicPortList": swL2IGMPRouterPortDynamicPortList,
       "swL2IGMPRouterPortForbiddenPortList": swL2IGMPRouterPortForbiddenPortList,
       "swL2IGMPAccessAuthTable": swL2IGMPAccessAuthTable,
       "swL2IGMPAccessAuthEntry": swL2IGMPAccessAuthEntry,
       "swL2IGMPAccessAuthPort": swL2IGMPAccessAuthPort,
       "swL2IGMPAccessAuthState": swL2IGMPAccessAuthState,
       "swL2TrafficMgmt": swL2TrafficMgmt,
       "swL2TrafficCtrlTable": swL2TrafficCtrlTable,
       "swL2TrafficCtrlEntry": swL2TrafficCtrlEntry,
       "swL2TrafficCtrlGroupIndex": swL2TrafficCtrlGroupIndex,
       "swL2TrafficCtrlUnitIndex": swL2TrafficCtrlUnitIndex,
       "swL2TrafficCtrlBMStromthreshold": swL2TrafficCtrlBMStromthreshold,
       "swL2TrafficCtrlBcastStromCtrl": swL2TrafficCtrlBcastStromCtrl,
       "swL2TrafficCtrlMcastStromCtrl": swL2TrafficCtrlMcastStromCtrl,
       "swL2TrafficCtrlUcastStromCtrl": swL2TrafficCtrlUcastStromCtrl,
       "swL2TrafficSegMgmt": swL2TrafficSegMgmt,
       "swL2TrafficSegTable": swL2TrafficSegTable,
       "swL2TrafficSegEntry": swL2TrafficSegEntry,
       "swL2TrafficSegPort": swL2TrafficSegPort,
       "swL2TrafficSegForwardPorts": swL2TrafficSegForwardPorts,
       "swL2PortSecurityMgmt": swL2PortSecurityMgmt,
       "swL2PortSecurityControlTable": swL2PortSecurityControlTable,
       "swL2PortSecurityControlEntry": swL2PortSecurityControlEntry,
       "swL2PortSecurityPortIndex": swL2PortSecurityPortIndex,
       "swL2PortSecurityMaxLernAddr": swL2PortSecurityMaxLernAddr,
       "swL2PortSecurityMode": swL2PortSecurityMode,
       "swL2PortSecurityAdmState": swL2PortSecurityAdmState,
       "swL2PortSecurityTrapLogState": swL2PortSecurityTrapLogState,
       "swL2StpMgmt": swL2StpMgmt,
       "swL2StpForwardBPDU": swL2StpForwardBPDU,
       "swL2StpLbd": swL2StpLbd,
       "swL2StpLbdRecoverTime": swL2StpLbdRecoverTime,
       "swL2StpPortTable": swL2StpPortTable,
       "swL2StpPortEntry": swL2StpPortEntry,
       "swL2StpPort": swL2StpPort,
       "swL2StpPortLbd": swL2StpPortLbd,
       "swL2StpPortStatus": swL2StpPortStatus,
       "swL2StpPortRole": swL2StpPortRole,
       "swL2StpPortFBPDU": swL2StpPortFBPDU,
       "swL2StpPortLinkState": swL2StpPortLinkState,
       "swL2StpPortProtocolMigration": swL2StpPortProtocolMigration,
       "swL2StpPortAdminEdgePort": swL2StpPortAdminEdgePort,
       "swL2StpPortOperEdgePort": swL2StpPortOperEdgePort,
       "swL2StpPortAdminPointToPoint": swL2StpPortAdminPointToPoint,
       "swL2StpPortOperPointToPoint": swL2StpPortOperPointToPoint,
       "swL2StpPortAdminPathCost": swL2StpPortAdminPathCost,
       "swL2StpPortPriority": swL2StpPortPriority,
       "swL2STPPortState": swL2STPPortState,
       "swL2StpPortRestrictedRole": swL2StpPortRestrictedRole,
       "swL2StpPortRestrictedTCN": swL2StpPortRestrictedTCN,
       "swL2CosMgmt": swL2CosMgmt,
       "swL2CosPriorityCtrl": swL2CosPriorityCtrl,
       "swL2CosPriorityTable": swL2CosPriorityTable,
       "swL2CosPriorityEntry": swL2CosPriorityEntry,
       "swL2CosPriorityPort": swL2CosPriorityPort,
       "swL2CosPriorityPortPRI": swL2CosPriorityPortPRI,
       "swL2CosPriorityEtherPRI": swL2CosPriorityEtherPRI,
       "swL2CosPriorityIpPRI": swL2CosPriorityIpPRI,
       "swL2CosPriorityNone": swL2CosPriorityNone,
       "swL2CosPortPRITable": swL2CosPortPRITable,
       "swL2CosPortPRIEntry": swL2CosPortPRIEntry,
       "swL2CosPortPRIIndex": swL2CosPortPRIIndex,
       "swL2CosPortPRIClass": swL2CosPortPRIClass,
       "swL2CosMacBasePRITable": swL2CosMacBasePRITable,
       "swL2CosMacBasePRIEntry": swL2CosMacBasePRIEntry,
       "swL2CosMacBasePRIIndex": swL2CosMacBasePRIIndex,
       "swL2CosMacBasePRIClass": swL2CosMacBasePRIClass,
       "swL2CosTosPRITable": swL2CosTosPRITable,
       "swL2CosTosPRIEntry": swL2CosTosPRIEntry,
       "swL2CosTosPRIIndex": swL2CosTosPRIIndex,
       "swL2CosTosPRIClass": swL2CosTosPRIClass,
       "swL2CosDscpPRITable": swL2CosDscpPRITable,
       "swL2CosDscpPRIEntry": swL2CosDscpPRIEntry,
       "swL2CosDscpPRIIndex": swL2CosDscpPRIIndex,
       "swL2CosDscpPRIClass": swL2CosDscpPRIClass,
       "swL2LoopDetectMgmt": swL2LoopDetectMgmt,
       "swL2LoopDetectCtrl": swL2LoopDetectCtrl,
       "swL2LoopDetectAdminState": swL2LoopDetectAdminState,
       "swL2LoopDetectInterval": swL2LoopDetectInterval,
       "swL2LoopDetectRecoverTime": swL2LoopDetectRecoverTime,
       "swL2LoopDetectPortMgmt": swL2LoopDetectPortMgmt,
       "swL2LoopDetectPortTable": swL2LoopDetectPortTable,
       "swL2LoopDetectPortEntry": swL2LoopDetectPortEntry,
       "swL2LoopDetectPortIndex": swL2LoopDetectPortIndex,
       "swL2LoopDetectPortState": swL2LoopDetectPortState,
       "swL2LoopDetectPortLoopStatus": swL2LoopDetectPortLoopStatus,
       "swL2VLANMgmt": swL2VLANMgmt,
       "swL2VlanTable": swL2VlanTable,
       "swL2VlanEntry": swL2VlanEntry,
       "swL2VlanIndex": swL2VlanIndex,
       "swL2VlanName": swL2VlanName,
       "swL2VlanType": swL2VlanType,
       "swL2VlanMemberPorts": swL2VlanMemberPorts,
       "swL2VlanStaticPorts": swL2VlanStaticPorts,
       "swL2VlanUntaggedPorts": swL2VlanUntaggedPorts,
       "swL2VlanTaggedPorts": swL2VlanTaggedPorts,
       "swL2MgmtMIBTraps": swL2MgmtMIBTraps,
       "swL2Notify": swL2Notify,
       "swL2NotifyPrefix": swL2NotifyPrefix,
       "swL2NotifFirmware": swL2NotifFirmware,
       "swL2macNotification": swL2macNotification,
       "swL2PortSecurityViolationTrap": swL2PortSecurityViolationTrap,
       "swl2NotificationBidings": swl2NotificationBidings,
       "swL2macNotifyInfo": swL2macNotifyInfo,
       "swL2PortSecurityViolationMac": swL2PortSecurityViolationMac}
)
