# SNMP MIB module (Es2952-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/Es2952-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:22 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



class PortList(TextualConvention, OctetString):
    status = "current"


class MacAddress(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_EthernetSwitch_ObjectIdentity = ObjectIdentity
ethernetSwitch = _EthernetSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15)
)
_Layer2Switch_ObjectIdentity = ObjectIdentity
layer2Switch = _Layer2Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2)
)
_Series2952Switch_ObjectIdentity = ObjectIdentity
series2952Switch = _Series2952Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11)
)
_SwitchSystem_ObjectIdentity = ObjectIdentity
switchSystem = _SwitchSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 1)
)
_CpuLoad5s_Type = Integer32
_CpuLoad5s_Object = MibScalar
cpuLoad5s = _CpuLoad5s_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 1, 1),
    _CpuLoad5s_Type()
)
cpuLoad5s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoad5s.setStatus("current")
_CpuLoad30s_Type = Integer32
_CpuLoad30s_Object = MibScalar
cpuLoad30s = _CpuLoad30s_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 1, 2),
    _CpuLoad30s_Type()
)
cpuLoad30s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoad30s.setStatus("current")
_CpuLoad2m_Type = Integer32
_CpuLoad2m_Object = MibScalar
cpuLoad2m = _CpuLoad2m_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 1, 3),
    _CpuLoad2m_Type()
)
cpuLoad2m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoad2m.setStatus("current")
_MaxCpuLoad_Type = Integer32
_MaxCpuLoad_Object = MibScalar
maxCpuLoad = _MaxCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 1, 4),
    _MaxCpuLoad_Type()
)
maxCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxCpuLoad.setStatus("current")
_MemUtilityRatio_Type = Integer32
_MemUtilityRatio_Object = MibScalar
memUtilityRatio = _MemUtilityRatio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 1, 5),
    _MemUtilityRatio_Type()
)
memUtilityRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memUtilityRatio.setStatus("current")
_SwitchType_Type = OctetString
_SwitchType_Object = MibScalar
switchType = _SwitchType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 1, 6),
    _SwitchType_Type()
)
switchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchType.setStatus("current")
_SwitchMac_Type = MacAddress
_SwitchMac_Object = MibScalar
switchMac = _SwitchMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 1, 7),
    _SwitchMac_Type()
)
switchMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchMac.setStatus("current")


class _Reboot_Type(Integer32):
    """Custom type reboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_Reboot_Type.__name__ = "Integer32"
_Reboot_Object = MibScalar
reboot = _Reboot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 1, 8),
    _Reboot_Type()
)
reboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reboot.setStatus("current")


class _SaveConfig_Type(Integer32):
    """Custom type saveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_SaveConfig_Type.__name__ = "Integer32"
_SaveConfig_Object = MibScalar
saveConfig = _SaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 1, 9),
    _SaveConfig_Type()
)
saveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveConfig.setStatus("current")


class _SysDateTime_Type(OctetString):
    """Custom type sysDateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SysDateTime_Type.__name__ = "OctetString"
_SysDateTime_Object = MibScalar
sysDateTime = _SysDateTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 1, 10),
    _SysDateTime_Type()
)
sysDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDateTime.setStatus("current")
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2)
)
_PortNumber_Type = Unsigned32
_PortNumber_Object = MibScalar
portNumber = _PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2, 1),
    _PortNumber_Type()
)
portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portNumber.setStatus("current")
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2, 4)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2, 4, 1)
)
portEntry.setIndexNames(
    (0, "Es2952-MIB", "portId"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")
_PortId_Type = Unsigned32
_PortId_Object = MibTableColumn
portId = _PortId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2, 4, 1, 1),
    _PortId_Type()
)
portId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portId.setStatus("current")


class _PortName_Type(OctetString):
    """Custom type portName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_PortName_Type.__name__ = "OctetString"
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2, 4, 1, 2),
    _PortName_Type()
)
portName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portName.setStatus("current")


class _PortDescr_Type(OctetString):
    """Custom type portDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_PortDescr_Type.__name__ = "OctetString"
_PortDescr_Object = MibTableColumn
portDescr = _PortDescr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2, 4, 1, 3),
    _PortDescr_Type()
)
portDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDescr.setStatus("current")


class _PortAdminStatus_Type(Integer32):
    """Custom type portAdminStatus based on Integer32"""
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


_PortAdminStatus_Type.__name__ = "Integer32"
_PortAdminStatus_Object = MibTableColumn
portAdminStatus = _PortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2, 4, 1, 4),
    _PortAdminStatus_Type()
)
portAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAdminStatus.setStatus("current")


class _PortOperStatus_Type(Integer32):
    """Custom type portOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkUp", 1),
          ("linkDown", 2))
    )


_PortOperStatus_Type.__name__ = "Integer32"
_PortOperStatus_Object = MibTableColumn
portOperStatus = _PortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2, 4, 1, 5),
    _PortOperStatus_Type()
)
portOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOperStatus.setStatus("current")


class _PortAdminWorkMode_Type(Integer32):
    """Custom type portAdminWorkMode based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("auto-10M", 1),
          ("auto-100M", 2),
          ("auto-1000M", 3),
          ("auto-auto", 4),
          ("half-10M", 5),
          ("half-100M", 6),
          ("half-1000M", 7),
          ("half-auto", 8),
          ("full-10M", 9),
          ("full-100M", 10),
          ("full-1000M", 11),
          ("full-auto", 12))
    )


_PortAdminWorkMode_Type.__name__ = "Integer32"
_PortAdminWorkMode_Object = MibTableColumn
portAdminWorkMode = _PortAdminWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2, 4, 1, 6),
    _PortAdminWorkMode_Type()
)
portAdminWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAdminWorkMode.setStatus("current")


class _PortOperDuplex_Type(Integer32):
    """Custom type portOperDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_PortOperDuplex_Type.__name__ = "Integer32"
_PortOperDuplex_Object = MibTableColumn
portOperDuplex = _PortOperDuplex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2, 4, 1, 7),
    _PortOperDuplex_Type()
)
portOperDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOperDuplex.setStatus("current")


class _PortOperSpeed_Type(Integer32):
    """Custom type portOperSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed-10M", 1),
          ("speed-100M", 2),
          ("speed-1000M", 3))
    )


_PortOperSpeed_Type.__name__ = "Integer32"
_PortOperSpeed_Object = MibTableColumn
portOperSpeed = _PortOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2, 4, 1, 8),
    _PortOperSpeed_Type()
)
portOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOperSpeed.setStatus("current")


class _PortPvid_Type(Integer32):
    """Custom type portPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PortPvid_Type.__name__ = "Integer32"
_PortPvid_Object = MibTableColumn
portPvid = _PortPvid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2, 4, 1, 9),
    _PortPvid_Type()
)
portPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPvid.setStatus("current")


class _PortFlowControl_Type(Integer32):
    """Custom type portFlowControl based on Integer32"""
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


_PortFlowControl_Type.__name__ = "Integer32"
_PortFlowControl_Object = MibTableColumn
portFlowControl = _PortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2, 4, 1, 10),
    _PortFlowControl_Type()
)
portFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFlowControl.setStatus("current")
_PortVlanMode_Type = OctetString
_PortVlanMode_Object = MibTableColumn
portVlanMode = _PortVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2, 4, 1, 11),
    _PortVlanMode_Type()
)
portVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVlanMode.setStatus("current")


class _PortSecurity_Type(Integer32):
    """Custom type portSecurity based on Integer32"""
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


_PortSecurity_Type.__name__ = "Integer32"
_PortSecurity_Object = MibTableColumn
portSecurity = _PortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2, 4, 1, 12),
    _PortSecurity_Type()
)
portSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurity.setStatus("current")


class _PortPriority_Type(Integer32):
    """Custom type portPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PortPriority_Type.__name__ = "Integer32"
_PortPriority_Object = MibTableColumn
portPriority = _PortPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2, 4, 1, 13),
    _PortPriority_Type()
)
portPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPriority.setStatus("current")


class _PortMulticast_Type(Integer32):
    """Custom type portMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("discard", 2))
    )


_PortMulticast_Type.__name__ = "Integer32"
_PortMulticast_Object = MibTableColumn
portMulticast = _PortMulticast_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2, 4, 1, 14),
    _PortMulticast_Type()
)
portMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMulticast.setStatus("current")


class _PortMediaType_Type(Integer32):
    """Custom type portMediaType based on Integer32"""
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
        *(("mt100BaseT", 1),
          ("mt100BaseFX", 2),
          ("mt1000BaseX", 3),
          ("mt1000BaseT", 4),
          ("unKnown", 5))
    )


_PortMediaType_Type.__name__ = "Integer32"
_PortMediaType_Object = MibTableColumn
portMediaType = _PortMediaType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2, 4, 1, 15),
    _PortMediaType_Type()
)
portMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMediaType.setStatus("current")


class _IsPortInTrunk_Type(Integer32):
    """Custom type isPortInTrunk based on Integer32"""
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


_IsPortInTrunk_Type.__name__ = "Integer32"
_IsPortInTrunk_Object = MibTableColumn
isPortInTrunk = _IsPortInTrunk_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2, 4, 1, 16),
    _IsPortInTrunk_Type()
)
isPortInTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isPortInTrunk.setStatus("current")


class _PortLoopdetectStatus_Type(OctetString):
    """Custom type portLoopdetectStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_PortLoopdetectStatus_Type.__name__ = "OctetString"
_PortLoopdetectStatus_Object = MibTableColumn
portLoopdetectStatus = _PortLoopdetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2, 4, 1, 17),
    _PortLoopdetectStatus_Type()
)
portLoopdetectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLoopdetectStatus.setStatus("current")


class _DynamicMacMaxCount_Type(Integer32):
    """Custom type dynamicMacMaxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DynamicMacMaxCount_Type.__name__ = "Integer32"
_DynamicMacMaxCount_Object = MibTableColumn
dynamicMacMaxCount = _DynamicMacMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2, 4, 1, 18),
    _DynamicMacMaxCount_Type()
)
dynamicMacMaxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dynamicMacMaxCount.setStatus("current")
_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 3)
)
_MaxVlanId_Type = Unsigned32
_MaxVlanId_Object = MibScalar
maxVlanId = _MaxVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 3, 1),
    _MaxVlanId_Type()
)
maxVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxVlanId.setStatus("current")
_MaxSupportedVlans_Type = Unsigned32
_MaxSupportedVlans_Object = MibScalar
maxSupportedVlans = _MaxSupportedVlans_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 3, 2),
    _MaxSupportedVlans_Type()
)
maxSupportedVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxSupportedVlans.setStatus("current")
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 3, 3)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("current")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 3, 3, 1)
)
vlanEntry.setIndexNames(
    (0, "Es2952-MIB", "vlanId"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("current")


class _VlanId_Type(Integer32):
    """Custom type vlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanId_Type.__name__ = "Integer32"
_VlanId_Object = MibTableColumn
vlanId = _VlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 3, 3, 1, 1),
    _VlanId_Type()
)
vlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanId.setStatus("current")
_VlanUntaggedPorts_Type = PortList
_VlanUntaggedPorts_Object = MibTableColumn
vlanUntaggedPorts = _VlanUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 3, 3, 1, 3),
    _VlanUntaggedPorts_Type()
)
vlanUntaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanUntaggedPorts.setStatus("current")
_VlanTaggedPorts_Type = PortList
_VlanTaggedPorts_Object = MibTableColumn
vlanTaggedPorts = _VlanTaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 3, 3, 1, 4),
    _VlanTaggedPorts_Type()
)
vlanTaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTaggedPorts.setStatus("current")


class _VlanName_Type(OctetString):
    """Custom type vlanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VlanName_Type.__name__ = "OctetString"
_VlanName_Object = MibTableColumn
vlanName = _VlanName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 3, 3, 1, 5),
    _VlanName_Type()
)
vlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanName.setStatus("current")


class _VlanAdminStatus_Type(Integer32):
    """Custom type vlanAdminStatus based on Integer32"""
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


_VlanAdminStatus_Type.__name__ = "Integer32"
_VlanAdminStatus_Object = MibTableColumn
vlanAdminStatus = _VlanAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 3, 3, 1, 6),
    _VlanAdminStatus_Type()
)
vlanAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanAdminStatus.setStatus("current")
_VlanUntaggedTrunks_Type = PortList
_VlanUntaggedTrunks_Object = MibTableColumn
vlanUntaggedTrunks = _VlanUntaggedTrunks_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 3, 3, 1, 7),
    _VlanUntaggedTrunks_Type()
)
vlanUntaggedTrunks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanUntaggedTrunks.setStatus("current")
_VlanTaggedTrunks_Type = PortList
_VlanTaggedTrunks_Object = MibTableColumn
vlanTaggedTrunks = _VlanTaggedTrunks_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 3, 3, 1, 8),
    _VlanTaggedTrunks_Type()
)
vlanTaggedTrunks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTaggedTrunks.setStatus("current")
_VlanAssistantTable_Object = MibTable
vlanAssistantTable = _VlanAssistantTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 3, 4)
)
if mibBuilder.loadTexts:
    vlanAssistantTable.setStatus("current")
_VlanAssistantEntry_Object = MibTableRow
vlanAssistantEntry = _VlanAssistantEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 3, 4, 1)
)
vlanAssistantEntry.setIndexNames(
    (0, "Es2952-MIB", "assVlanId"),
)
if mibBuilder.loadTexts:
    vlanAssistantEntry.setStatus("current")
_AssVlanId_Type = Integer32
_AssVlanId_Object = MibTableColumn
assVlanId = _AssVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 3, 4, 1, 1),
    _AssVlanId_Type()
)
assVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assVlanId.setStatus("current")
_Mirror_ObjectIdentity = ObjectIdentity
mirror = _Mirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 4)
)
_SourcePortsIngress_Type = PortList
_SourcePortsIngress_Object = MibScalar
sourcePortsIngress = _SourcePortsIngress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 4, 1),
    _SourcePortsIngress_Type()
)
sourcePortsIngress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourcePortsIngress.setStatus("current")
_SourcePortsEgress_Type = PortList
_SourcePortsEgress_Object = MibScalar
sourcePortsEgress = _SourcePortsEgress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 4, 2),
    _SourcePortsEgress_Type()
)
sourcePortsEgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourcePortsEgress.setStatus("current")
_DesPortIngress_Type = Unsigned32
_DesPortIngress_Object = MibScalar
desPortIngress = _DesPortIngress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 4, 3),
    _DesPortIngress_Type()
)
desPortIngress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    desPortIngress.setStatus("current")
_DesPortEgress_Type = Unsigned32
_DesPortEgress_Object = MibScalar
desPortEgress = _DesPortEgress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 4, 4),
    _DesPortEgress_Type()
)
desPortEgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    desPortEgress.setStatus("current")
_Qos_ObjectIdentity = ObjectIdentity
qos = _Qos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5)
)


class _QueueScheduleWeight_Type(OctetString):
    """Custom type queueScheduleWeight based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QueueScheduleWeight_Type.__name__ = "OctetString"
_QueueScheduleWeight_Object = MibScalar
queueScheduleWeight = _QueueScheduleWeight_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 1),
    _QueueScheduleWeight_Type()
)
queueScheduleWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueScheduleWeight.setStatus("current")


class _QueueScheduleMode0_Type(OctetString):
    """Custom type queueScheduleMode0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QueueScheduleMode0_Type.__name__ = "OctetString"
_QueueScheduleMode0_Object = MibScalar
queueScheduleMode0 = _QueueScheduleMode0_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 2),
    _QueueScheduleMode0_Type()
)
queueScheduleMode0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueScheduleMode0.setStatus("current")


class _QueueScheduleMode1_Type(OctetString):
    """Custom type queueScheduleMode1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QueueScheduleMode1_Type.__name__ = "OctetString"
_QueueScheduleMode1_Object = MibScalar
queueScheduleMode1 = _QueueScheduleMode1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 3),
    _QueueScheduleMode1_Type()
)
queueScheduleMode1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueScheduleMode1.setStatus("current")


class _QueueScheduleMode2_Type(OctetString):
    """Custom type queueScheduleMode2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QueueScheduleMode2_Type.__name__ = "OctetString"
_QueueScheduleMode2_Object = MibScalar
queueScheduleMode2 = _QueueScheduleMode2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 4),
    _QueueScheduleMode2_Type()
)
queueScheduleMode2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueScheduleMode2.setStatus("current")


class _QueueScheduleMode3_Type(OctetString):
    """Custom type queueScheduleMode3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_QueueScheduleMode3_Type.__name__ = "OctetString"
_QueueScheduleMode3_Object = MibScalar
queueScheduleMode3 = _QueueScheduleMode3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 5),
    _QueueScheduleMode3_Type()
)
queueScheduleMode3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueScheduleMode3.setStatus("current")
_QosPrimapUsrToTraffic_Type = OctetString
_QosPrimapUsrToTraffic_Object = MibScalar
qosPrimapUsrToTraffic = _QosPrimapUsrToTraffic_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 6),
    _QosPrimapUsrToTraffic_Type()
)
qosPrimapUsrToTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPrimapUsrToTraffic.setStatus("current")
_QosPolicerTable_Object = MibTable
qosPolicerTable = _QosPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 7)
)
if mibBuilder.loadTexts:
    qosPolicerTable.setStatus("current")
_QosPolicerEntry_Object = MibTableRow
qosPolicerEntry = _QosPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 7, 1)
)
qosPolicerEntry.setIndexNames(
    (0, "Es2952-MIB", "policerID"),
)
if mibBuilder.loadTexts:
    qosPolicerEntry.setStatus("current")
_PolicerID_Type = Unsigned32
_PolicerID_Object = MibTableColumn
policerID = _PolicerID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 7, 1, 1),
    _PolicerID_Type()
)
policerID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policerID.setStatus("current")
_QosPolicerPara_Type = Unsigned32
_QosPolicerPara_Object = MibTableColumn
qosPolicerPara = _QosPolicerPara_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 7, 1, 2),
    _QosPolicerPara_Type()
)
qosPolicerPara.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPolicerPara.setStatus("current")


class _QosExceededOper_Type(Integer32):
    """Custom type qosExceededOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("drop", 2))
    )


_QosExceededOper_Type.__name__ = "Integer32"
_QosExceededOper_Object = MibTableColumn
qosExceededOper = _QosExceededOper_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 7, 1, 3),
    _QosExceededOper_Type()
)
qosExceededOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosExceededOper.setStatus("current")
_QosPolicerBurst_Type = Unsigned32
_QosPolicerBurst_Object = MibTableColumn
qosPolicerBurst = _QosPolicerBurst_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 7, 1, 4),
    _QosPolicerBurst_Type()
)
qosPolicerBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPolicerBurst.setStatus("current")
_IpPriToTrafficTable_Object = MibTable
ipPriToTrafficTable = _IpPriToTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 8)
)
if mibBuilder.loadTexts:
    ipPriToTrafficTable.setStatus("current")
_IpPriToTrafficEntry_Object = MibTableRow
ipPriToTrafficEntry = _IpPriToTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 8, 1)
)
ipPriToTrafficEntry.setIndexNames(
    (0, "Es2952-MIB", "ipPriority"),
)
if mibBuilder.loadTexts:
    ipPriToTrafficEntry.setStatus("current")
_IpPriority_Type = Unsigned32
_IpPriority_Object = MibTableColumn
ipPriority = _IpPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 8, 1, 1),
    _IpPriority_Type()
)
ipPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipPriority.setStatus("current")


class _TcFePort_Type(Unsigned32):
    """Custom type tcFePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TcFePort_Type.__name__ = "Unsigned32"
_TcFePort_Object = MibTableColumn
tcFePort = _TcFePort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 8, 1, 2),
    _TcFePort_Type()
)
tcFePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcFePort.setStatus("current")


class _TcGePort_Type(Unsigned32):
    """Custom type tcGePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TcGePort_Type.__name__ = "Unsigned32"
_TcGePort_Object = MibTableColumn
tcGePort = _TcGePort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 8, 1, 3),
    _TcGePort_Type()
)
tcGePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcGePort.setStatus("current")
_FePortIngBandTable_Object = MibTable
fePortIngBandTable = _FePortIngBandTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 9)
)
if mibBuilder.loadTexts:
    fePortIngBandTable.setStatus("current")
_FePortIngBandEntry_Object = MibTableRow
fePortIngBandEntry = _FePortIngBandEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 9, 1)
)
fePortIngBandEntry.setIndexNames(
    (0, "Es2952-MIB", "fePortID"),
    (0, "Es2952-MIB", "sessionNo"),
)
if mibBuilder.loadTexts:
    fePortIngBandEntry.setStatus("current")
_FePortID_Type = Unsigned32
_FePortID_Object = MibTableColumn
fePortID = _FePortID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 9, 1, 1),
    _FePortID_Type()
)
fePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fePortID.setStatus("current")
_SessionNo_Type = Unsigned32
_SessionNo_Object = MibTableColumn
sessionNo = _SessionNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 9, 1, 2),
    _SessionNo_Type()
)
sessionNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionNo.setStatus("current")


class _SessionStatus_Type(Integer32):
    """Custom type sessionStatus based on Integer32"""
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


_SessionStatus_Type.__name__ = "Integer32"
_SessionStatus_Object = MibTableColumn
sessionStatus = _SessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 9, 1, 3),
    _SessionStatus_Type()
)
sessionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionStatus.setStatus("current")
_FeIngressRate_Type = Unsigned32
_FeIngressRate_Object = MibTableColumn
feIngressRate = _FeIngressRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 9, 1, 4),
    _FeIngressRate_Type()
)
feIngressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feIngressRate.setStatus("current")
_FeIngressPkType_Type = PortList
_FeIngressPkType_Object = MibTableColumn
feIngressPkType = _FeIngressPkType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 9, 1, 5),
    _FeIngressPkType_Type()
)
feIngressPkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    feIngressPkType.setStatus("current")
_QuePriorityStatus_Type = PortList
_QuePriorityStatus_Object = MibTableColumn
quePriorityStatus = _QuePriorityStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 9, 1, 6),
    _QuePriorityStatus_Type()
)
quePriorityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    quePriorityStatus.setStatus("current")


class _MgmtNoRatelimitStatus_Type(Integer32):
    """Custom type mgmtNoRatelimitStatus based on Integer32"""
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


_MgmtNoRatelimitStatus_Type.__name__ = "Integer32"
_MgmtNoRatelimitStatus_Object = MibTableColumn
mgmtNoRatelimitStatus = _MgmtNoRatelimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 9, 1, 7),
    _MgmtNoRatelimitStatus_Type()
)
mgmtNoRatelimitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtNoRatelimitStatus.setStatus("current")
_GePortIngBandTable_Object = MibTable
gePortIngBandTable = _GePortIngBandTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 10)
)
if mibBuilder.loadTexts:
    gePortIngBandTable.setStatus("current")
_GePortIngBandEntry_Object = MibTableRow
gePortIngBandEntry = _GePortIngBandEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 10, 1)
)
gePortIngBandEntry.setIndexNames(
    (0, "Es2952-MIB", "gePortID"),
)
if mibBuilder.loadTexts:
    gePortIngBandEntry.setStatus("current")
_GePortID_Type = Unsigned32
_GePortID_Object = MibTableColumn
gePortID = _GePortID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 10, 1, 1),
    _GePortID_Type()
)
gePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gePortID.setStatus("current")


class _GeIngressStatus_Type(Integer32):
    """Custom type geIngressStatus based on Integer32"""
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


_GeIngressStatus_Type.__name__ = "Integer32"
_GeIngressStatus_Object = MibTableColumn
geIngressStatus = _GeIngressStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 10, 1, 2),
    _GeIngressStatus_Type()
)
geIngressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geIngressStatus.setStatus("current")
_GeIngressRate_Type = Integer32
_GeIngressRate_Object = MibTableColumn
geIngressRate = _GeIngressRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 10, 1, 3),
    _GeIngressRate_Type()
)
geIngressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geIngressRate.setStatus("current")
_GeIngressPkType_Type = PortList
_GeIngressPkType_Object = MibTableColumn
geIngressPkType = _GeIngressPkType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 10, 1, 4),
    _GeIngressPkType_Type()
)
geIngressPkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geIngressPkType.setStatus("current")
_GeQueScheTable_Object = MibTable
geQueScheTable = _GeQueScheTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 11)
)
if mibBuilder.loadTexts:
    geQueScheTable.setStatus("current")
_GeQueScheEntry_Object = MibTableRow
geQueScheEntry = _GeQueScheEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 11, 1)
)
geQueScheEntry.setIndexNames(
    (0, "Es2952-MIB", "gePortSessionID"),
    (0, "Es2952-MIB", "queueID"),
)
if mibBuilder.loadTexts:
    geQueScheEntry.setStatus("current")
_GePortSessionID_Type = Unsigned32
_GePortSessionID_Object = MibTableColumn
gePortSessionID = _GePortSessionID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 11, 1, 1),
    _GePortSessionID_Type()
)
gePortSessionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gePortSessionID.setStatus("current")
_QueueID_Type = Unsigned32
_QueueID_Object = MibTableColumn
queueID = _QueueID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 11, 1, 2),
    _QueueID_Type()
)
queueID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    queueID.setStatus("current")
_QueueSchedule_Type = OctetString
_QueueSchedule_Object = MibTableColumn
queueSchedule = _QueueSchedule_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 11, 1, 3),
    _QueueSchedule_Type()
)
queueSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueSchedule.setStatus("current")
_GeQosPrimapUsrToTraffic_Type = OctetString
_GeQosPrimapUsrToTraffic_Object = MibScalar
geQosPrimapUsrToTraffic = _GeQosPrimapUsrToTraffic_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 12),
    _GeQosPrimapUsrToTraffic_Type()
)
geQosPrimapUsrToTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    geQosPrimapUsrToTraffic.setStatus("current")
_GePortIp2UserTable_Object = MibTable
gePortIp2UserTable = _GePortIp2UserTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 13)
)
if mibBuilder.loadTexts:
    gePortIp2UserTable.setStatus("current")
_GePortIp2UserEntry_Object = MibTableRow
gePortIp2UserEntry = _GePortIp2UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 13, 1)
)
gePortIp2UserEntry.setIndexNames(
    (0, "Es2952-MIB", "ipPriority"),
)
if mibBuilder.loadTexts:
    gePortIp2UserEntry.setStatus("current")


class _UserPriority_Type(Unsigned32):
    """Custom type userPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_UserPriority_Type.__name__ = "Unsigned32"
_UserPriority_Object = MibTableColumn
userPriority = _UserPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 13, 1, 2),
    _UserPriority_Type()
)
userPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userPriority.setStatus("current")
_PortQosParamTable_Object = MibTable
portQosParamTable = _PortQosParamTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 14)
)
if mibBuilder.loadTexts:
    portQosParamTable.setStatus("current")
_PortQosParamEntry_Object = MibTableRow
portQosParamEntry = _PortQosParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 14, 1)
)
portQosParamEntry.setIndexNames(
    (0, "Es2952-MIB", "portID"),
)
if mibBuilder.loadTexts:
    portQosParamEntry.setStatus("current")
_PortID_Type = Unsigned32
_PortID_Object = MibTableColumn
portID = _PortID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 14, 1, 1),
    _PortID_Type()
)
portID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portID.setStatus("current")
_BandWidthEgress_Type = OctetString
_BandWidthEgress_Object = MibTableColumn
bandWidthEgress = _BandWidthEgress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 14, 1, 2),
    _BandWidthEgress_Type()
)
bandWidthEgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandWidthEgress.setStatus("current")


class _UpPriorityEnable_Type(Integer32):
    """Custom type upPriorityEnable based on Integer32"""
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


_UpPriorityEnable_Type.__name__ = "Integer32"
_UpPriorityEnable_Object = MibTableColumn
upPriorityEnable = _UpPriorityEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 14, 1, 3),
    _UpPriorityEnable_Type()
)
upPriorityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upPriorityEnable.setStatus("current")


class _DscpPriorityEnable_Type(Integer32):
    """Custom type dscpPriorityEnable based on Integer32"""
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


_DscpPriorityEnable_Type.__name__ = "Integer32"
_DscpPriorityEnable_Object = MibTableColumn
dscpPriorityEnable = _DscpPriorityEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 14, 1, 4),
    _DscpPriorityEnable_Type()
)
dscpPriorityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscpPriorityEnable.setStatus("current")


class _QueScheduleMode_Type(Integer32):
    """Custom type queScheduleMode based on Integer32"""
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
        *(("wrr0", 0),
          ("sp", 1),
          ("wrr1-sp", 2),
          ("wrr2-sp", 3),
          ("session0", 4),
          ("session1", 5))
    )


_QueScheduleMode_Type.__name__ = "Integer32"
_QueScheduleMode_Object = MibTableColumn
queScheduleMode = _QueScheduleMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 14, 1, 5),
    _QueScheduleMode_Type()
)
queScheduleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queScheduleMode.setStatus("current")
_RemaptagToPriority_Type = OctetString
_RemaptagToPriority_Object = MibTableColumn
remaptagToPriority = _RemaptagToPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 5, 14, 1, 6),
    _RemaptagToPriority_Type()
)
remaptagToPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remaptagToPriority.setStatus("current")
_Pvlan_ObjectIdentity = ObjectIdentity
pvlan = _Pvlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 6)
)


class _SessionMaxNum_Type(Unsigned32):
    """Custom type sessionMaxNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SessionMaxNum_Type.__name__ = "Unsigned32"
_SessionMaxNum_Object = MibScalar
sessionMaxNum = _SessionMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 6, 1),
    _SessionMaxNum_Type()
)
sessionMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionMaxNum.setStatus("current")
_PvlanTable_Object = MibTable
pvlanTable = _PvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 6, 2)
)
if mibBuilder.loadTexts:
    pvlanTable.setStatus("current")
_PvlanEntry_Object = MibTableRow
pvlanEntry = _PvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 6, 2, 1)
)
pvlanEntry.setIndexNames(
    (0, "Es2952-MIB", "sessionId"),
)
if mibBuilder.loadTexts:
    pvlanEntry.setStatus("current")
_SessionId_Type = Unsigned32
_SessionId_Object = MibTableColumn
sessionId = _SessionId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 6, 2, 1, 1),
    _SessionId_Type()
)
sessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sessionId.setStatus("current")
_ProAndIsoPortOrTrunk_Type = OctetString
_ProAndIsoPortOrTrunk_Object = MibTableColumn
proAndIsoPortOrTrunk = _ProAndIsoPortOrTrunk_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 6, 2, 1, 2),
    _ProAndIsoPortOrTrunk_Type()
)
proAndIsoPortOrTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proAndIsoPortOrTrunk.setStatus("current")
_Lacp_ObjectIdentity = ObjectIdentity
lacp = _Lacp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 7)
)


class _LacpAdminStatus_Type(Integer32):
    """Custom type lacpAdminStatus based on Integer32"""
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


_LacpAdminStatus_Type.__name__ = "Integer32"
_LacpAdminStatus_Object = MibScalar
lacpAdminStatus = _LacpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 7, 1),
    _LacpAdminStatus_Type()
)
lacpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpAdminStatus.setStatus("current")


class _LacpPriority_Type(Unsigned32):
    """Custom type lacpPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LacpPriority_Type.__name__ = "Unsigned32"
_LacpPriority_Object = MibScalar
lacpPriority = _LacpPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 7, 2),
    _LacpPriority_Type()
)
lacpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpPriority.setStatus("current")
_TrunkNumber_Type = Unsigned32
_TrunkNumber_Object = MibScalar
trunkNumber = _TrunkNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 7, 3),
    _TrunkNumber_Type()
)
trunkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkNumber.setStatus("current")
_TrunkTable_Object = MibTable
trunkTable = _TrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 7, 4)
)
if mibBuilder.loadTexts:
    trunkTable.setStatus("current")
_TrunkEntry_Object = MibTableRow
trunkEntry = _TrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 7, 4, 1)
)
trunkEntry.setIndexNames(
    (0, "Es2952-MIB", "trunkId"),
)
if mibBuilder.loadTexts:
    trunkEntry.setStatus("current")


class _TrunkId_Type(Unsigned32):
    """Custom type trunkId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TrunkId_Type.__name__ = "Unsigned32"
_TrunkId_Object = MibTableColumn
trunkId = _TrunkId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 7, 4, 1, 1),
    _TrunkId_Type()
)
trunkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trunkId.setStatus("current")


class _TrunkPvid_Type(Integer32):
    """Custom type trunkPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TrunkPvid_Type.__name__ = "Integer32"
_TrunkPvid_Object = MibTableColumn
trunkPvid = _TrunkPvid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 7, 4, 1, 2),
    _TrunkPvid_Type()
)
trunkPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkPvid.setStatus("current")


class _TrunkMulticast_Type(Integer32):
    """Custom type trunkMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("discard", 2))
    )


_TrunkMulticast_Type.__name__ = "Integer32"
_TrunkMulticast_Object = MibTableColumn
trunkMulticast = _TrunkMulticast_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 7, 4, 1, 3),
    _TrunkMulticast_Type()
)
trunkMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkMulticast.setStatus("current")
_TrunkPorts_Type = PortList
_TrunkPorts_Object = MibTableColumn
trunkPorts = _TrunkPorts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 7, 4, 1, 4),
    _TrunkPorts_Type()
)
trunkPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkPorts.setStatus("current")


class _TrunkMode_Type(Integer32):
    """Custom type trunkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2),
          ("mixed", 3))
    )


_TrunkMode_Type.__name__ = "Integer32"
_TrunkMode_Object = MibTableColumn
trunkMode = _TrunkMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 7, 4, 1, 5),
    _TrunkMode_Type()
)
trunkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkMode.setStatus("current")
_LacpPortTable_Object = MibTable
lacpPortTable = _LacpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 7, 5)
)
if mibBuilder.loadTexts:
    lacpPortTable.setStatus("current")
_LacpPortEntry_Object = MibTableRow
lacpPortEntry = _LacpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 7, 5, 1)
)
lacpPortEntry.setIndexNames(
    (0, "Es2952-MIB", "lacpPortId"),
)
if mibBuilder.loadTexts:
    lacpPortEntry.setStatus("current")


class _LacpPortId_Type(Integer32):
    """Custom type lacpPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_LacpPortId_Type.__name__ = "Integer32"
_LacpPortId_Object = MibTableColumn
lacpPortId = _LacpPortId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 7, 5, 1, 1),
    _LacpPortId_Type()
)
lacpPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lacpPortId.setStatus("current")


class _LacpPortMode_Type(Integer32):
    """Custom type lacpPortMode based on Integer32"""
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


_LacpPortMode_Type.__name__ = "Integer32"
_LacpPortMode_Object = MibTableColumn
lacpPortMode = _LacpPortMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 7, 5, 1, 2),
    _LacpPortMode_Type()
)
lacpPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpPortMode.setStatus("current")


class _LacpPortTimeout_Type(Integer32):
    """Custom type lacpPortTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("short", 1),
          ("long", 2))
    )


_LacpPortTimeout_Type.__name__ = "Integer32"
_LacpPortTimeout_Object = MibTableColumn
lacpPortTimeout = _LacpPortTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 7, 5, 1, 3),
    _LacpPortTimeout_Type()
)
lacpPortTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpPortTimeout.setStatus("current")
_Layer3_ObjectIdentity = ObjectIdentity
layer3 = _Layer3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 8)
)
_Layer3PortTable_Object = MibTable
layer3PortTable = _Layer3PortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 8, 1)
)
if mibBuilder.loadTexts:
    layer3PortTable.setStatus("current")
_Layer3PortEntry_Object = MibTableRow
layer3PortEntry = _Layer3PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 8, 1, 1)
)
layer3PortEntry.setIndexNames(
    (0, "Es2952-MIB", "layer3PortId"),
)
if mibBuilder.loadTexts:
    layer3PortEntry.setStatus("current")
_Layer3PortId_Type = Unsigned32
_Layer3PortId_Object = MibTableColumn
layer3PortId = _Layer3PortId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 8, 1, 1, 1),
    _Layer3PortId_Type()
)
layer3PortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    layer3PortId.setStatus("current")
_Layer3PortIpAddrAndMask_Type = OctetString
_Layer3PortIpAddrAndMask_Object = MibTableColumn
layer3PortIpAddrAndMask = _Layer3PortIpAddrAndMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 8, 1, 1, 2),
    _Layer3PortIpAddrAndMask_Type()
)
layer3PortIpAddrAndMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer3PortIpAddrAndMask.setStatus("current")


class _Layer3PortMacAddr_Type(MacAddress):
    """Custom type layer3PortMacAddr based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Layer3PortMacAddr_Type.__name__ = "MacAddress"
_Layer3PortMacAddr_Object = MibTableColumn
layer3PortMacAddr = _Layer3PortMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 8, 1, 1, 3),
    _Layer3PortMacAddr_Type()
)
layer3PortMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer3PortMacAddr.setStatus("current")


class _Layer3PortVlanId_Type(Integer32):
    """Custom type layer3PortVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Layer3PortVlanId_Type.__name__ = "Integer32"
_Layer3PortVlanId_Object = MibTableColumn
layer3PortVlanId = _Layer3PortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 8, 1, 1, 4),
    _Layer3PortVlanId_Type()
)
layer3PortVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer3PortVlanId.setStatus("current")


class _Layer3PortAdminStatus_Type(Integer32):
    """Custom type layer3PortAdminStatus based on Integer32"""
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


_Layer3PortAdminStatus_Type.__name__ = "Integer32"
_Layer3PortAdminStatus_Object = MibTableColumn
layer3PortAdminStatus = _Layer3PortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 8, 1, 1, 5),
    _Layer3PortAdminStatus_Type()
)
layer3PortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer3PortAdminStatus.setStatus("current")
_LoopDetect_ObjectIdentity = ObjectIdentity
loopDetect = _LoopDetect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 9)
)


class _LoopDetectBlockDelay_Type(Unsigned32):
    """Custom type loopDetectBlockDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1080),
    )


_LoopDetectBlockDelay_Type.__name__ = "Unsigned32"
_LoopDetectBlockDelay_Object = MibScalar
loopDetectBlockDelay = _LoopDetectBlockDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 9, 1),
    _LoopDetectBlockDelay_Type()
)
loopDetectBlockDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopDetectBlockDelay.setStatus("current")


class _LoopDetectSendPktInterval_Type(Unsigned32):
    """Custom type loopDetectSendPktInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_LoopDetectSendPktInterval_Type.__name__ = "Unsigned32"
_LoopDetectSendPktInterval_Object = MibScalar
loopDetectSendPktInterval = _LoopDetectSendPktInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 9, 2),
    _LoopDetectSendPktInterval_Type()
)
loopDetectSendPktInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopDetectSendPktInterval.setStatus("current")
_LoopDetectPortTable_Object = MibTable
loopDetectPortTable = _LoopDetectPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 9, 3)
)
if mibBuilder.loadTexts:
    loopDetectPortTable.setStatus("current")
_LoopDetectPortEntry_Object = MibTableRow
loopDetectPortEntry = _LoopDetectPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 9, 3, 1)
)
loopDetectPortEntry.setIndexNames(
    (0, "Es2952-MIB", "loopDetectPortId"),
)
if mibBuilder.loadTexts:
    loopDetectPortEntry.setStatus("current")
_LoopDetectPortId_Type = Integer32
_LoopDetectPortId_Object = MibTableColumn
loopDetectPortId = _LoopDetectPortId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 9, 3, 1, 1),
    _LoopDetectPortId_Type()
)
loopDetectPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopDetectPortId.setStatus("current")


class _LoopDetectPortAdminStatus_Type(OctetString):
    """Custom type loopDetectPortAdminStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_LoopDetectPortAdminStatus_Type.__name__ = "OctetString"
_LoopDetectPortAdminStatus_Object = MibTableColumn
loopDetectPortAdminStatus = _LoopDetectPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 9, 3, 1, 2),
    _LoopDetectPortAdminStatus_Type()
)
loopDetectPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopDetectPortAdminStatus.setStatus("current")


class _LoopDetectPortProtectStatus_Type(Integer32):
    """Custom type loopDetectPortProtectStatus based on Integer32"""
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


_LoopDetectPortProtectStatus_Type.__name__ = "Integer32"
_LoopDetectPortProtectStatus_Object = MibTableColumn
loopDetectPortProtectStatus = _LoopDetectPortProtectStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 9, 3, 1, 3),
    _LoopDetectPortProtectStatus_Type()
)
loopDetectPortProtectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopDetectPortProtectStatus.setStatus("current")


class _LoopDetectPortLoopStatus_Type(Integer32):
    """Custom type loopDetectPortLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LoopDetectPortLoopStatus_Type.__name__ = "Integer32"
_LoopDetectPortLoopStatus_Object = MibTableColumn
loopDetectPortLoopStatus = _LoopDetectPortLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 9, 3, 1, 4),
    _LoopDetectPortLoopStatus_Type()
)
loopDetectPortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopDetectPortLoopStatus.setStatus("current")


class _LoopDetectPortBlockStatus_Type(Integer32):
    """Custom type loopDetectPortBlockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LoopDetectPortBlockStatus_Type.__name__ = "Integer32"
_LoopDetectPortBlockStatus_Object = MibTableColumn
loopDetectPortBlockStatus = _LoopDetectPortBlockStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 9, 3, 1, 5),
    _LoopDetectPortBlockStatus_Type()
)
loopDetectPortBlockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopDetectPortBlockStatus.setStatus("current")


class _LoopDetectPortInVlan_Type(Unsigned32):
    """Custom type loopDetectPortInVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_LoopDetectPortInVlan_Type.__name__ = "Unsigned32"
_LoopDetectPortInVlan_Object = MibTableColumn
loopDetectPortInVlan = _LoopDetectPortInVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 9, 3, 1, 6),
    _LoopDetectPortInVlan_Type()
)
loopDetectPortInVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopDetectPortInVlan.setStatus("current")
_LoopDetectTrunkTable_Object = MibTable
loopDetectTrunkTable = _LoopDetectTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 9, 4)
)
if mibBuilder.loadTexts:
    loopDetectTrunkTable.setStatus("current")
_LoopDetectTrunkEntry_Object = MibTableRow
loopDetectTrunkEntry = _LoopDetectTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 9, 4, 1)
)
loopDetectTrunkEntry.setIndexNames(
    (0, "Es2952-MIB", "loopDetectTrunkId"),
)
if mibBuilder.loadTexts:
    loopDetectTrunkEntry.setStatus("current")
_LoopDetectTrunkId_Type = Integer32
_LoopDetectTrunkId_Object = MibTableColumn
loopDetectTrunkId = _LoopDetectTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 9, 4, 1, 1),
    _LoopDetectTrunkId_Type()
)
loopDetectTrunkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopDetectTrunkId.setStatus("current")


class _LoopDetectTrunkAdminStatus_Type(OctetString):
    """Custom type loopDetectTrunkAdminStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_LoopDetectTrunkAdminStatus_Type.__name__ = "OctetString"
_LoopDetectTrunkAdminStatus_Object = MibTableColumn
loopDetectTrunkAdminStatus = _LoopDetectTrunkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 9, 4, 1, 2),
    _LoopDetectTrunkAdminStatus_Type()
)
loopDetectTrunkAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopDetectTrunkAdminStatus.setStatus("current")


class _LoopDetectTrunkProtectStatus_Type(Integer32):
    """Custom type loopDetectTrunkProtectStatus based on Integer32"""
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


_LoopDetectTrunkProtectStatus_Type.__name__ = "Integer32"
_LoopDetectTrunkProtectStatus_Object = MibTableColumn
loopDetectTrunkProtectStatus = _LoopDetectTrunkProtectStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 9, 4, 1, 3),
    _LoopDetectTrunkProtectStatus_Type()
)
loopDetectTrunkProtectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopDetectTrunkProtectStatus.setStatus("current")


class _LoopDetectTrunkLoopStatus_Type(Integer32):
    """Custom type loopDetectTrunkLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LoopDetectTrunkLoopStatus_Type.__name__ = "Integer32"
_LoopDetectTrunkLoopStatus_Object = MibTableColumn
loopDetectTrunkLoopStatus = _LoopDetectTrunkLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 9, 4, 1, 4),
    _LoopDetectTrunkLoopStatus_Type()
)
loopDetectTrunkLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopDetectTrunkLoopStatus.setStatus("current")


class _LoopDetectTrunkBlockStatus_Type(Integer32):
    """Custom type loopDetectTrunkBlockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LoopDetectTrunkBlockStatus_Type.__name__ = "Integer32"
_LoopDetectTrunkBlockStatus_Object = MibTableColumn
loopDetectTrunkBlockStatus = _LoopDetectTrunkBlockStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 9, 4, 1, 5),
    _LoopDetectTrunkBlockStatus_Type()
)
loopDetectTrunkBlockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopDetectTrunkBlockStatus.setStatus("current")


class _LoopDetectTrunkInVlan_Type(Unsigned32):
    """Custom type loopDetectTrunkInVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_LoopDetectTrunkInVlan_Type.__name__ = "Unsigned32"
_LoopDetectTrunkInVlan_Object = MibTableColumn
loopDetectTrunkInVlan = _LoopDetectTrunkInVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 9, 4, 1, 6),
    _LoopDetectTrunkInVlan_Type()
)
loopDetectTrunkInVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopDetectTrunkInVlan.setStatus("current")
_VlanTranslation_ObjectIdentity = ObjectIdentity
vlanTranslation = _VlanTranslation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 10)
)
_VlanTranslationTable_Object = MibTable
vlanTranslationTable = _VlanTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 10, 1)
)
if mibBuilder.loadTexts:
    vlanTranslationTable.setStatus("current")
_VlanTranslationEntry_Object = MibTableRow
vlanTranslationEntry = _VlanTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 10, 1, 1)
)
vlanTranslationEntry.setIndexNames(
    (0, "Es2952-MIB", "ingressPortId"),
)
if mibBuilder.loadTexts:
    vlanTranslationEntry.setStatus("current")
_IngressPortId_Type = Integer32
_IngressPortId_Object = MibTableColumn
ingressPortId = _IngressPortId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 10, 1, 1, 1),
    _IngressPortId_Type()
)
ingressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingressPortId.setStatus("current")


class _VlanTranslationEnable_Type(Integer32):
    """Custom type vlanTranslationEnable based on Integer32"""
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


_VlanTranslationEnable_Type.__name__ = "Integer32"
_VlanTranslationEnable_Object = MibTableColumn
vlanTranslationEnable = _VlanTranslationEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 10, 1, 1, 2),
    _VlanTranslationEnable_Type()
)
vlanTranslationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTranslationEnable.setStatus("current")
_VlanTranslationStatus_Type = OctetString
_VlanTranslationStatus_Object = MibTableColumn
vlanTranslationStatus = _VlanTranslationStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 10, 1, 1, 3),
    _VlanTranslationStatus_Type()
)
vlanTranslationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTranslationStatus.setStatus("current")
_Stp_ObjectIdentity = ObjectIdentity
stp = _Stp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 11)
)


class _StpAdminStatus_Type(Integer32):
    """Custom type stpAdminStatus based on Integer32"""
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


_StpAdminStatus_Type.__name__ = "Integer32"
_StpAdminStatus_Object = MibScalar
stpAdminStatus = _StpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 11, 1),
    _StpAdminStatus_Type()
)
stpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpAdminStatus.setStatus("current")
_Vct_ObjectIdentity = ObjectIdentity
vct = _Vct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 12)
)
_VctPortTable_Object = MibTable
vctPortTable = _VctPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 12, 1)
)
if mibBuilder.loadTexts:
    vctPortTable.setStatus("current")
_VctPortEntry_Object = MibTableRow
vctPortEntry = _VctPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 12, 1, 1)
)
vctPortEntry.setIndexNames(
    (0, "Es2952-MIB", "vctPortId"),
)
if mibBuilder.loadTexts:
    vctPortEntry.setStatus("current")


class _VctPortId_Type(Integer32):
    """Custom type vctPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_VctPortId_Type.__name__ = "Integer32"
_VctPortId_Object = MibTableColumn
vctPortId = _VctPortId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 12, 1, 1, 1),
    _VctPortId_Type()
)
vctPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vctPortId.setStatus("current")


class _VctDo_Type(Integer32):
    """Custom type vctDo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_VctDo_Type.__name__ = "Integer32"
_VctDo_Object = MibTableColumn
vctDo = _VctDo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 12, 1, 1, 2),
    _VctDo_Type()
)
vctDo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vctDo.setStatus("current")


class _VctIsValid_Type(Integer32):
    """Custom type vctIsValid based on Integer32"""
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
          ("yes2", 2),
          ("yes4", 3))
    )


_VctIsValid_Type.__name__ = "Integer32"
_VctIsValid_Object = MibTableColumn
vctIsValid = _VctIsValid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 12, 1, 1, 3),
    _VctIsValid_Type()
)
vctIsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctIsValid.setStatus("current")


class _VctPair1Result_Type(Integer32):
    """Custom type vctPair1Result based on Integer32"""
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
        *(("good", 1),
          ("open", 2),
          ("short", 3),
          ("impMismatch", 4))
    )


_VctPair1Result_Type.__name__ = "Integer32"
_VctPair1Result_Object = MibTableColumn
vctPair1Result = _VctPair1Result_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 12, 1, 1, 4),
    _VctPair1Result_Type()
)
vctPair1Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctPair1Result.setStatus("current")


class _VctPair1Lenth_Type(Integer32):
    """Custom type vctPair1Lenth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VctPair1Lenth_Type.__name__ = "Integer32"
_VctPair1Lenth_Object = MibTableColumn
vctPair1Lenth = _VctPair1Lenth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 12, 1, 1, 5),
    _VctPair1Lenth_Type()
)
vctPair1Lenth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctPair1Lenth.setStatus("current")


class _VctPair2Result_Type(Integer32):
    """Custom type vctPair2Result based on Integer32"""
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
        *(("good", 1),
          ("open", 2),
          ("short", 3),
          ("impMismatch", 4))
    )


_VctPair2Result_Type.__name__ = "Integer32"
_VctPair2Result_Object = MibTableColumn
vctPair2Result = _VctPair2Result_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 12, 1, 1, 6),
    _VctPair2Result_Type()
)
vctPair2Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctPair2Result.setStatus("current")


class _VctPair2Lenth_Type(Integer32):
    """Custom type vctPair2Lenth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VctPair2Lenth_Type.__name__ = "Integer32"
_VctPair2Lenth_Object = MibTableColumn
vctPair2Lenth = _VctPair2Lenth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 12, 1, 1, 7),
    _VctPair2Lenth_Type()
)
vctPair2Lenth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctPair2Lenth.setStatus("current")


class _VctPair3Result_Type(Integer32):
    """Custom type vctPair3Result based on Integer32"""
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
        *(("good", 1),
          ("open", 2),
          ("short", 3),
          ("impMismatch", 4))
    )


_VctPair3Result_Type.__name__ = "Integer32"
_VctPair3Result_Object = MibTableColumn
vctPair3Result = _VctPair3Result_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 12, 1, 1, 8),
    _VctPair3Result_Type()
)
vctPair3Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctPair3Result.setStatus("current")


class _VctPair3Lenth_Type(Integer32):
    """Custom type vctPair3Lenth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VctPair3Lenth_Type.__name__ = "Integer32"
_VctPair3Lenth_Object = MibTableColumn
vctPair3Lenth = _VctPair3Lenth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 12, 1, 1, 9),
    _VctPair3Lenth_Type()
)
vctPair3Lenth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctPair3Lenth.setStatus("current")


class _VctPair4Result_Type(Integer32):
    """Custom type vctPair4Result based on Integer32"""
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
        *(("good", 1),
          ("open", 2),
          ("short", 3),
          ("impMismatch", 4))
    )


_VctPair4Result_Type.__name__ = "Integer32"
_VctPair4Result_Object = MibTableColumn
vctPair4Result = _VctPair4Result_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 12, 1, 1, 10),
    _VctPair4Result_Type()
)
vctPair4Result.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctPair4Result.setStatus("current")


class _VctPair4Lenth_Type(Integer32):
    """Custom type vctPair4Lenth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VctPair4Lenth_Type.__name__ = "Integer32"
_VctPair4Lenth_Object = MibTableColumn
vctPair4Lenth = _VctPair4Lenth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 12, 1, 1, 11),
    _VctPair4Lenth_Type()
)
vctPair4Lenth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vctPair4Lenth.setStatus("current")
_Syslog_ObjectIdentity = ObjectIdentity
syslog = _Syslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 13)
)


class _SyslogStatus_Type(Integer32):
    """Custom type syslogStatus based on Integer32"""
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


_SyslogStatus_Type.__name__ = "Integer32"
_SyslogStatus_Object = MibScalar
syslogStatus = _SyslogStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 13, 1),
    _SyslogStatus_Type()
)
syslogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogStatus.setStatus("current")


class _SyslogLevel_Type(Integer32):
    """Custom type syslogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SyslogLevel_Type.__name__ = "Integer32"
_SyslogLevel_Object = MibScalar
syslogLevel = _SyslogLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 13, 2),
    _SyslogLevel_Type()
)
syslogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogLevel.setStatus("current")
_EnabledModule_Type = PortList
_EnabledModule_Object = MibScalar
enabledModule = _EnabledModule_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 13, 3),
    _EnabledModule_Type()
)
enabledModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enabledModule.setStatus("current")


class _ServerMaxNum_Type(Integer32):
    """Custom type serverMaxNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_ServerMaxNum_Type.__name__ = "Integer32"
_ServerMaxNum_Object = MibScalar
serverMaxNum = _ServerMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 13, 4),
    _ServerMaxNum_Type()
)
serverMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverMaxNum.setStatus("current")
_ServerTable_Object = MibTable
serverTable = _ServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 13, 5)
)
if mibBuilder.loadTexts:
    serverTable.setStatus("current")
_ServerEntry_Object = MibTableRow
serverEntry = _ServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 13, 5, 1)
)
serverEntry.setIndexNames(
    (0, "Es2952-MIB", "serverId"),
)
if mibBuilder.loadTexts:
    serverEntry.setStatus("current")
_ServerId_Type = Unsigned32
_ServerId_Object = MibTableColumn
serverId = _ServerId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 13, 5, 1, 1),
    _ServerId_Type()
)
serverId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serverId.setStatus("current")
_ServerIP_Type = OctetString
_ServerIP_Object = MibTableColumn
serverIP = _ServerIP_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 13, 5, 1, 2),
    _ServerIP_Type()
)
serverIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverIP.setStatus("current")


class _ServerName_Type(OctetString):
    """Custom type serverName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ServerName_Type.__name__ = "OctetString"
_ServerName_Object = MibTableColumn
serverName = _ServerName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 13, 5, 1, 3),
    _ServerName_Type()
)
serverName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverName.setStatus("current")


class _ServerAdminStatus_Type(Integer32):
    """Custom type serverAdminStatus based on Integer32"""
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


_ServerAdminStatus_Type.__name__ = "Integer32"
_ServerAdminStatus_Object = MibTableColumn
serverAdminStatus = _ServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 13, 5, 1, 4),
    _ServerAdminStatus_Type()
)
serverAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAdminStatus.setStatus("current")
_Ntp_ObjectIdentity = ObjectIdentity
ntp = _Ntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 14)
)


class _SynchronizeStatus_Type(Integer32):
    """Custom type synchronizeStatus based on Integer32"""
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


_SynchronizeStatus_Type.__name__ = "Integer32"
_SynchronizeStatus_Object = MibScalar
synchronizeStatus = _SynchronizeStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 14, 1),
    _SynchronizeStatus_Type()
)
synchronizeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    synchronizeStatus.setStatus("current")


class _ProtocolStatus_Type(Integer32):
    """Custom type protocolStatus based on Integer32"""
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


_ProtocolStatus_Type.__name__ = "Integer32"
_ProtocolStatus_Object = MibScalar
protocolStatus = _ProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 14, 2),
    _ProtocolStatus_Type()
)
protocolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolStatus.setStatus("current")
_SrvIpAddrAndVersion_Type = OctetString
_SrvIpAddrAndVersion_Object = MibScalar
srvIpAddrAndVersion = _SrvIpAddrAndVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 14, 3),
    _SrvIpAddrAndVersion_Type()
)
srvIpAddrAndVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srvIpAddrAndVersion.setStatus("current")
_SourceIpAddr_Type = OctetString
_SourceIpAddr_Object = MibScalar
sourceIpAddr = _SourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 14, 4),
    _SourceIpAddr_Type()
)
sourceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sourceIpAddr.setStatus("current")
_LoginUser_ObjectIdentity = ObjectIdentity
loginUser = _LoginUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 15)
)
_UserTable_Object = MibTable
userTable = _UserTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 15, 1)
)
if mibBuilder.loadTexts:
    userTable.setStatus("current")
_UserEntry_Object = MibTableRow
userEntry = _UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 15, 1, 1)
)
userEntry.setIndexNames(
    (0, "Es2952-MIB", "userName"),
)
if mibBuilder.loadTexts:
    userEntry.setStatus("current")


class _UserName_Type(DisplayString):
    """Custom type userName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_UserName_Type.__name__ = "DisplayString"
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 15, 1, 1, 1),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("current")


class _UserAttr_Type(Integer32):
    """Custom type userAttr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("administrator", 2),
          ("guest", 3))
    )


_UserAttr_Type.__name__ = "Integer32"
_UserAttr_Object = MibTableColumn
userAttr = _UserAttr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 15, 1, 1, 2),
    _UserAttr_Type()
)
userAttr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAttr.setStatus("current")


class _LoginPass_Type(OctetString):
    """Custom type loginPass based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LoginPass_Type.__name__ = "OctetString"
_LoginPass_Object = MibTableColumn
loginPass = _LoginPass_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 15, 1, 1, 3),
    _LoginPass_Type()
)
loginPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loginPass.setStatus("current")


class _AdminPass_Type(OctetString):
    """Custom type adminPass based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AdminPass_Type.__name__ = "OctetString"
_AdminPass_Object = MibTableColumn
adminPass = _AdminPass_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 15, 1, 1, 4),
    _AdminPass_Type()
)
adminPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminPass.setStatus("current")
_SnmpConfig_ObjectIdentity = ObjectIdentity
snmpConfig = _SnmpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 16)
)
_CommunityTable_Object = MibTable
communityTable = _CommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 16, 1)
)
if mibBuilder.loadTexts:
    communityTable.setStatus("current")
_CommunityEntry_Object = MibTableRow
communityEntry = _CommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 16, 1, 1)
)
communityEntry.setIndexNames(
    (0, "Es2952-MIB", "communityName"),
)
if mibBuilder.loadTexts:
    communityEntry.setStatus("current")


class _CommunityName_Type(DisplayString):
    """Custom type communityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_CommunityName_Type.__name__ = "DisplayString"
_CommunityName_Object = MibTableColumn
communityName = _CommunityName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 16, 1, 1, 1),
    _CommunityName_Type()
)
communityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    communityName.setStatus("current")


class _CommunityAttr_Type(Integer32):
    """Custom type communityAttr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("public", 2),
          ("private", 3))
    )


_CommunityAttr_Type.__name__ = "Integer32"
_CommunityAttr_Object = MibTableColumn
communityAttr = _CommunityAttr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 16, 1, 1, 2),
    _CommunityAttr_Type()
)
communityAttr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityAttr.setStatus("current")


class _ViewAttached_Type(OctetString):
    """Custom type viewAttached based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ViewAttached_Type.__name__ = "OctetString"
_ViewAttached_Object = MibTableColumn
viewAttached = _ViewAttached_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 16, 1, 1, 3),
    _ViewAttached_Type()
)
viewAttached.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    viewAttached.setStatus("current")
_ViewTable_Object = MibTable
viewTable = _ViewTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 16, 2)
)
if mibBuilder.loadTexts:
    viewTable.setStatus("current")
_ViewEntry_Object = MibTableRow
viewEntry = _ViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 16, 2, 1)
)
viewEntry.setIndexNames(
    (0, "Es2952-MIB", "viewIndex"),
    (0, "Es2952-MIB", "viewName"),
)
if mibBuilder.loadTexts:
    viewEntry.setStatus("current")
_ViewIndex_Type = Unsigned32
_ViewIndex_Object = MibTableColumn
viewIndex = _ViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 16, 2, 1, 1),
    _ViewIndex_Type()
)
viewIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    viewIndex.setStatus("current")


class _ViewName_Type(OctetString):
    """Custom type viewName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_ViewName_Type.__name__ = "OctetString"
_ViewName_Object = MibTableColumn
viewName = _ViewName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 16, 2, 1, 2),
    _ViewName_Type()
)
viewName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    viewName.setStatus("current")


class _AttrAndOid_Type(OctetString):
    """Custom type attrAndOid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 150),
    )


_AttrAndOid_Type.__name__ = "OctetString"
_AttrAndOid_Object = MibTableColumn
attrAndOid = _AttrAndOid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 16, 2, 1, 3),
    _AttrAndOid_Type()
)
attrAndOid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    attrAndOid.setStatus("current")
_TrapHostTable_Object = MibTable
trapHostTable = _TrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 16, 3)
)
if mibBuilder.loadTexts:
    trapHostTable.setStatus("current")
_TrapHostEntry_Object = MibTableRow
trapHostEntry = _TrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 16, 3, 1)
)
trapHostEntry.setIndexNames(
    (0, "Es2952-MIB", "traphostIP"),
    (0, "Es2952-MIB", "traphostType"),
    (0, "Es2952-MIB", "commuName"),
)
if mibBuilder.loadTexts:
    trapHostEntry.setStatus("current")
_TraphostIP_Type = IpAddress
_TraphostIP_Object = MibTableColumn
traphostIP = _TraphostIP_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 16, 3, 1, 1),
    _TraphostIP_Type()
)
traphostIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traphostIP.setStatus("current")
_TraphostType_Type = Unsigned32
_TraphostType_Object = MibTableColumn
traphostType = _TraphostType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 16, 3, 1, 2),
    _TraphostType_Type()
)
traphostType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traphostType.setStatus("current")


class _CommuName_Type(OctetString):
    """Custom type commuName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_CommuName_Type.__name__ = "OctetString"
_CommuName_Object = MibTableColumn
commuName = _CommuName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 16, 3, 1, 3),
    _CommuName_Type()
)
commuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commuName.setStatus("current")
_TraphostVer_Type = Integer32
_TraphostVer_Object = MibTableColumn
traphostVer = _TraphostVer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 16, 3, 1, 4),
    _TraphostVer_Type()
)
traphostVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traphostVer.setStatus("current")
_TrapEnable_Type = PortList
_TrapEnable_Object = MibScalar
trapEnable = _TrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 16, 4),
    _TrapEnable_Type()
)
trapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapEnable.setStatus("current")
_Acl_ObjectIdentity = ObjectIdentity
acl = _Acl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17)
)
_TimeAclTable_Object = MibTable
timeAclTable = _TimeAclTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 1)
)
if mibBuilder.loadTexts:
    timeAclTable.setStatus("current")
_TimeAclEntry_Object = MibTableRow
timeAclEntry = _TimeAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 1, 1)
)
timeAclEntry.setIndexNames(
    (0, "Es2952-MIB", "timeRangeName"),
)
if mibBuilder.loadTexts:
    timeAclEntry.setStatus("current")


class _TimeRangeName_Type(OctetString):
    """Custom type timeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_TimeRangeName_Type.__name__ = "OctetString"
_TimeRangeName_Object = MibTableColumn
timeRangeName = _TimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 1, 1, 1),
    _TimeRangeName_Type()
)
timeRangeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeRangeName.setStatus("current")


class _TimeRange_Type(OctetString):
    """Custom type timeRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 150),
    )


_TimeRange_Type.__name__ = "OctetString"
_TimeRange_Object = MibTableColumn
timeRange = _TimeRange_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 1, 1, 2),
    _TimeRange_Type()
)
timeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeRange.setStatus("current")
_BasicAclTable_Object = MibTable
basicAclTable = _BasicAclTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 2)
)
if mibBuilder.loadTexts:
    basicAclTable.setStatus("current")
_BasicAclEntry_Object = MibTableRow
basicAclEntry = _BasicAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 2, 1)
)
basicAclEntry.setIndexNames(
    (0, "Es2952-MIB", "basicACLNo"),
    (0, "Es2952-MIB", "basicRuleID"),
)
if mibBuilder.loadTexts:
    basicAclEntry.setStatus("current")
_BasicACLNo_Type = Unsigned32
_BasicACLNo_Object = MibTableColumn
basicACLNo = _BasicACLNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 2, 1, 1),
    _BasicACLNo_Type()
)
basicACLNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basicACLNo.setStatus("current")
_BasicRuleID_Type = Unsigned32
_BasicRuleID_Object = MibTableColumn
basicRuleID = _BasicRuleID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 2, 1, 2),
    _BasicRuleID_Type()
)
basicRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basicRuleID.setStatus("current")


class _RuleBasicStatus_Type(Integer32):
    """Custom type ruleBasicStatus based on Integer32"""
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


_RuleBasicStatus_Type.__name__ = "Integer32"
_RuleBasicStatus_Object = MibTableColumn
ruleBasicStatus = _RuleBasicStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 2, 1, 3),
    _RuleBasicStatus_Type()
)
ruleBasicStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleBasicStatus.setStatus("current")
_RuleBasicACL_Type = OctetString
_RuleBasicACL_Object = MibTableColumn
ruleBasicACL = _RuleBasicACL_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 2, 1, 4),
    _RuleBasicACL_Type()
)
ruleBasicACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleBasicACL.setStatus("current")
_ExtendedAclTable_Object = MibTable
extendedAclTable = _ExtendedAclTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 3)
)
if mibBuilder.loadTexts:
    extendedAclTable.setStatus("current")
_ExtendedAclEntry_Object = MibTableRow
extendedAclEntry = _ExtendedAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 3, 1)
)
extendedAclEntry.setIndexNames(
    (0, "Es2952-MIB", "extendedACLNo"),
    (0, "Es2952-MIB", "extendedRuleID"),
)
if mibBuilder.loadTexts:
    extendedAclEntry.setStatus("current")
_ExtendedACLNo_Type = Unsigned32
_ExtendedACLNo_Object = MibTableColumn
extendedACLNo = _ExtendedACLNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 3, 1, 1),
    _ExtendedACLNo_Type()
)
extendedACLNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extendedACLNo.setStatus("current")
_ExtendedRuleID_Type = Unsigned32
_ExtendedRuleID_Object = MibTableColumn
extendedRuleID = _ExtendedRuleID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 3, 1, 2),
    _ExtendedRuleID_Type()
)
extendedRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extendedRuleID.setStatus("current")


class _RuleExtendedStatus_Type(Integer32):
    """Custom type ruleExtendedStatus based on Integer32"""
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


_RuleExtendedStatus_Type.__name__ = "Integer32"
_RuleExtendedStatus_Object = MibTableColumn
ruleExtendedStatus = _RuleExtendedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 3, 1, 3),
    _RuleExtendedStatus_Type()
)
ruleExtendedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleExtendedStatus.setStatus("current")
_RuleExtendedProtocol_Type = OctetString
_RuleExtendedProtocol_Object = MibTableColumn
ruleExtendedProtocol = _RuleExtendedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 3, 1, 4),
    _RuleExtendedProtocol_Type()
)
ruleExtendedProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleExtendedProtocol.setStatus("current")
_LinkAclTable_Object = MibTable
linkAclTable = _LinkAclTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 4)
)
if mibBuilder.loadTexts:
    linkAclTable.setStatus("current")
_LinkAclEntry_Object = MibTableRow
linkAclEntry = _LinkAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 4, 1)
)
linkAclEntry.setIndexNames(
    (0, "Es2952-MIB", "linkACLNo"),
    (0, "Es2952-MIB", "linkRuleID"),
)
if mibBuilder.loadTexts:
    linkAclEntry.setStatus("current")
_LinkACLNo_Type = Unsigned32
_LinkACLNo_Object = MibTableColumn
linkACLNo = _LinkACLNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 4, 1, 1),
    _LinkACLNo_Type()
)
linkACLNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linkACLNo.setStatus("current")
_LinkRuleID_Type = Unsigned32
_LinkRuleID_Object = MibTableColumn
linkRuleID = _LinkRuleID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 4, 1, 2),
    _LinkRuleID_Type()
)
linkRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linkRuleID.setStatus("current")


class _RuleLinkStatus_Type(Integer32):
    """Custom type ruleLinkStatus based on Integer32"""
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


_RuleLinkStatus_Type.__name__ = "Integer32"
_RuleLinkStatus_Object = MibTableColumn
ruleLinkStatus = _RuleLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 4, 1, 3),
    _RuleLinkStatus_Type()
)
ruleLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleLinkStatus.setStatus("current")
_RuleLinkProtocol_Type = OctetString
_RuleLinkProtocol_Object = MibTableColumn
ruleLinkProtocol = _RuleLinkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 4, 1, 4),
    _RuleLinkProtocol_Type()
)
ruleLinkProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleLinkProtocol.setStatus("current")
_HybridAclTable_Object = MibTable
hybridAclTable = _HybridAclTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 5)
)
if mibBuilder.loadTexts:
    hybridAclTable.setStatus("current")
_HybridAclEntry_Object = MibTableRow
hybridAclEntry = _HybridAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 5, 1)
)
hybridAclEntry.setIndexNames(
    (0, "Es2952-MIB", "hybridACLNo"),
    (0, "Es2952-MIB", "hybridRuleID"),
)
if mibBuilder.loadTexts:
    hybridAclEntry.setStatus("current")
_HybridACLNo_Type = Unsigned32
_HybridACLNo_Object = MibTableColumn
hybridACLNo = _HybridACLNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 5, 1, 1),
    _HybridACLNo_Type()
)
hybridACLNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hybridACLNo.setStatus("current")
_HybridRuleID_Type = Unsigned32
_HybridRuleID_Object = MibTableColumn
hybridRuleID = _HybridRuleID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 5, 1, 2),
    _HybridRuleID_Type()
)
hybridRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hybridRuleID.setStatus("current")


class _RuleHybridStatus_Type(Integer32):
    """Custom type ruleHybridStatus based on Integer32"""
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


_RuleHybridStatus_Type.__name__ = "Integer32"
_RuleHybridStatus_Object = MibTableColumn
ruleHybridStatus = _RuleHybridStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 5, 1, 3),
    _RuleHybridStatus_Type()
)
ruleHybridStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleHybridStatus.setStatus("current")
_RuleHybridProtocol_Type = OctetString
_RuleHybridProtocol_Object = MibTableColumn
ruleHybridProtocol = _RuleHybridProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 5, 1, 4),
    _RuleHybridProtocol_Type()
)
ruleHybridProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleHybridProtocol.setStatus("current")
_GlobalAclTable_Object = MibTable
globalAclTable = _GlobalAclTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 6)
)
if mibBuilder.loadTexts:
    globalAclTable.setStatus("current")
_GlobalAclEntry_Object = MibTableRow
globalAclEntry = _GlobalAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 6, 1)
)
globalAclEntry.setIndexNames(
    (0, "Es2952-MIB", "globalACLNo"),
    (0, "Es2952-MIB", "globalRuleID"),
)
if mibBuilder.loadTexts:
    globalAclEntry.setStatus("current")
_GlobalACLNo_Type = Unsigned32
_GlobalACLNo_Object = MibTableColumn
globalACLNo = _GlobalACLNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 6, 1, 1),
    _GlobalACLNo_Type()
)
globalACLNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    globalACLNo.setStatus("current")
_GlobalRuleID_Type = Unsigned32
_GlobalRuleID_Object = MibTableColumn
globalRuleID = _GlobalRuleID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 6, 1, 2),
    _GlobalRuleID_Type()
)
globalRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    globalRuleID.setStatus("current")


class _RuleGlobalStatus_Type(Integer32):
    """Custom type ruleGlobalStatus based on Integer32"""
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


_RuleGlobalStatus_Type.__name__ = "Integer32"
_RuleGlobalStatus_Object = MibTableColumn
ruleGlobalStatus = _RuleGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 6, 1, 3),
    _RuleGlobalStatus_Type()
)
ruleGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleGlobalStatus.setStatus("current")
_RuleGlobalProtocol_Type = OctetString
_RuleGlobalProtocol_Object = MibTableColumn
ruleGlobalProtocol = _RuleGlobalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 17, 6, 1, 4),
    _RuleGlobalProtocol_Type()
)
ruleGlobalProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruleGlobalProtocol.setStatus("current")
_Fdb_ObjectIdentity = ObjectIdentity
fdb = _Fdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 18)
)


class _FdbAgingTime_Type(Integer32):
    """Custom type fdbAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 1260),
    )


_FdbAgingTime_Type.__name__ = "Integer32"
_FdbAgingTime_Object = MibScalar
fdbAgingTime = _FdbAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 18, 1),
    _FdbAgingTime_Type()
)
fdbAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbAgingTime.setStatus("current")
_FdbFilterTable_Object = MibTable
fdbFilterTable = _FdbFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 18, 2)
)
if mibBuilder.loadTexts:
    fdbFilterTable.setStatus("current")
_FdbFilterEntry_Object = MibTableRow
fdbFilterEntry = _FdbFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 18, 2, 1)
)
fdbFilterEntry.setIndexNames(
    (0, "Es2952-MIB", "fdbID"),
    (0, "Es2952-MIB", "fdbFilterAddress"),
)
if mibBuilder.loadTexts:
    fdbFilterEntry.setStatus("current")
_FdbID_Type = Unsigned32
_FdbID_Object = MibTableColumn
fdbID = _FdbID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 18, 2, 1, 1),
    _FdbID_Type()
)
fdbID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdbID.setStatus("current")
_FdbFilterAddress_Type = MacAddress
_FdbFilterAddress_Object = MibTableColumn
fdbFilterAddress = _FdbFilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 18, 2, 1, 2),
    _FdbFilterAddress_Type()
)
fdbFilterAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdbFilterAddress.setStatus("current")


class _FdbFilterType_Type(Integer32):
    """Custom type fdbFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("clear", 2))
    )


_FdbFilterType_Type.__name__ = "Integer32"
_FdbFilterType_Object = MibTableColumn
fdbFilterType = _FdbFilterType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 18, 2, 1, 3),
    _FdbFilterType_Type()
)
fdbFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdbFilterType.setStatus("current")
_FdbStaticPortTable_Object = MibTable
fdbStaticPortTable = _FdbStaticPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 18, 3)
)
if mibBuilder.loadTexts:
    fdbStaticPortTable.setStatus("current")
_FdbStaticPortEntry_Object = MibTableRow
fdbStaticPortEntry = _FdbStaticPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 18, 3, 1)
)
fdbStaticPortEntry.setIndexNames(
    (0, "Es2952-MIB", "fdbID"),
    (0, "Es2952-MIB", "fdbStaticAddress"),
)
if mibBuilder.loadTexts:
    fdbStaticPortEntry.setStatus("current")
_FdbStaticAddress_Type = MacAddress
_FdbStaticAddress_Object = MibTableColumn
fdbStaticAddress = _FdbStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 18, 3, 1, 2),
    _FdbStaticAddress_Type()
)
fdbStaticAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdbStaticAddress.setStatus("current")
_PortBindMac_Type = Unsigned32
_PortBindMac_Object = MibTableColumn
portBindMac = _PortBindMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 18, 3, 1, 3),
    _PortBindMac_Type()
)
portBindMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBindMac.setStatus("current")
_FdbStaticTrunkTable_Object = MibTable
fdbStaticTrunkTable = _FdbStaticTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 18, 4)
)
if mibBuilder.loadTexts:
    fdbStaticTrunkTable.setStatus("current")
_FdbStaticTrunkEntry_Object = MibTableRow
fdbStaticTrunkEntry = _FdbStaticTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 18, 4, 1)
)
fdbStaticTrunkEntry.setIndexNames(
    (0, "Es2952-MIB", "fdbID"),
    (0, "Es2952-MIB", "fdbStaticAddress"),
)
if mibBuilder.loadTexts:
    fdbStaticTrunkEntry.setStatus("current")
_TrunkBindMac_Type = Unsigned32
_TrunkBindMac_Object = MibTableColumn
trunkBindMac = _TrunkBindMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 18, 4, 1, 3),
    _TrunkBindMac_Type()
)
trunkBindMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkBindMac.setStatus("current")
_P8021xRelay_ObjectIdentity = ObjectIdentity
p8021xRelay = _P8021xRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 19)
)


class _P8021xRelayAdminStatus_Type(Integer32):
    """Custom type p8021xRelayAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("invalid", 3))
    )


_P8021xRelayAdminStatus_Type.__name__ = "Integer32"
_P8021xRelayAdminStatus_Object = MibScalar
p8021xRelayAdminStatus = _P8021xRelayAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 19, 1),
    _P8021xRelayAdminStatus_Type()
)
p8021xRelayAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p8021xRelayAdminStatus.setStatus("current")
_IgmpSnooping_ObjectIdentity = ObjectIdentity
igmpSnooping = _IgmpSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 20)
)
_MultiGroupTable_Object = MibTable
multiGroupTable = _MultiGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 20, 1)
)
if mibBuilder.loadTexts:
    multiGroupTable.setStatus("current")
_MultiGroupEntry_Object = MibTableRow
multiGroupEntry = _MultiGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 20, 1, 1)
)
multiGroupEntry.setIndexNames(
    (0, "Es2952-MIB", "number"),
)
if mibBuilder.loadTexts:
    multiGroupEntry.setStatus("current")
_Number_Type = Unsigned32
_Number_Object = MibTableColumn
number = _Number_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 20, 1, 1, 1),
    _Number_Type()
)
number.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    number.setStatus("current")
_VlanID_Type = Unsigned32
_VlanID_Object = MibTableColumn
vlanID = _VlanID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 20, 1, 1, 2),
    _VlanID_Type()
)
vlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanID.setStatus("current")
_MultiGroup_Type = IpAddress
_MultiGroup_Object = MibTableColumn
multiGroup = _MultiGroup_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 20, 1, 1, 3),
    _MultiGroup_Type()
)
multiGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiGroup.setStatus("current")
_PortList_Type = PortList
_PortList_Object = MibTableColumn
portList = _PortList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 20, 1, 1, 4),
    _PortList_Type()
)
portList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portList.setStatus("current")
_TrunkList_Type = PortList
_TrunkList_Object = MibTableColumn
trunkList = _TrunkList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 20, 1, 1, 5),
    _TrunkList_Type()
)
trunkList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkList.setStatus("current")
_Epon_ObjectIdentity = ObjectIdentity
epon = _Epon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21)
)


class _PonReset_Type(Integer32):
    """Custom type ponReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_PonReset_Type.__name__ = "Integer32"
_PonReset_Object = MibScalar
ponReset = _PonReset_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 2),
    _PonReset_Type()
)
ponReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponReset.setStatus("current")
_PortPonInfo_ObjectIdentity = ObjectIdentity
portPonInfo = _PortPonInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 3)
)


class _PortPonAdminStatus_Type(Integer32):
    """Custom type portPonAdminStatus based on Integer32"""
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


_PortPonAdminStatus_Type.__name__ = "Integer32"
_PortPonAdminStatus_Object = MibScalar
portPonAdminStatus = _PortPonAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 3, 1),
    _PortPonAdminStatus_Type()
)
portPonAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPonAdminStatus.setStatus("current")
_PortPonStpState_Type = OctetString
_PortPonStpState_Object = MibScalar
portPonStpState = _PortPonStpState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 3, 2),
    _PortPonStpState_Type()
)
portPonStpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPonStpState.setStatus("current")
_PortPonFecTx_Type = Integer32
_PortPonFecTx_Object = MibScalar
portPonFecTx = _PortPonFecTx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 3, 3),
    _PortPonFecTx_Type()
)
portPonFecTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPonFecTx.setStatus("current")
_PortPonFecRx_Type = Integer32
_PortPonFecRx_Object = MibScalar
portPonFecRx = _PortPonFecRx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 3, 4),
    _PortPonFecRx_Type()
)
portPonFecRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPonFecRx.setStatus("current")
_PortPonType_Type = OctetString
_PortPonType_Object = MibScalar
portPonType = _PortPonType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 3, 5),
    _PortPonType_Type()
)
portPonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPonType.setStatus("current")


class _PortPonOperStatus_Type(Integer32):
    """Custom type portPonOperStatus based on Integer32"""
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


_PortPonOperStatus_Type.__name__ = "Integer32"
_PortPonOperStatus_Object = MibScalar
portPonOperStatus = _PortPonOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 3, 6),
    _PortPonOperStatus_Type()
)
portPonOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPonOperStatus.setStatus("current")
_PortPonLlidPortsNum_Type = Integer32
_PortPonLlidPortsNum_Object = MibScalar
portPonLlidPortsNum = _PortPonLlidPortsNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 3, 7),
    _PortPonLlidPortsNum_Type()
)
portPonLlidPortsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portPonLlidPortsNum.setStatus("current")
_PonOamInfo_ObjectIdentity = ObjectIdentity
ponOamInfo = _PonOamInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 4)
)
_LocalOamAdmin_Type = Integer32
_LocalOamAdmin_Object = MibScalar
localOamAdmin = _LocalOamAdmin_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 4, 1),
    _LocalOamAdmin_Type()
)
localOamAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localOamAdmin.setStatus("current")
_LocalOamOper_Type = Integer32
_LocalOamOper_Object = MibScalar
localOamOper = _LocalOamOper_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 4, 2),
    _LocalOamOper_Type()
)
localOamOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localOamOper.setStatus("current")
_LocalOamMode_Type = Integer32
_LocalOamMode_Object = MibScalar
localOamMode = _LocalOamMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 4, 3),
    _LocalOamMode_Type()
)
localOamMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localOamMode.setStatus("current")
_LocalOamMaxPdu_Type = Integer32
_LocalOamMaxPdu_Object = MibScalar
localOamMaxPdu = _LocalOamMaxPdu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 4, 4),
    _LocalOamMaxPdu_Type()
)
localOamMaxPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localOamMaxPdu.setStatus("current")
_LocalOamRevision_Type = Integer32
_LocalOamRevision_Object = MibScalar
localOamRevision = _LocalOamRevision_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 4, 5),
    _LocalOamRevision_Type()
)
localOamRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localOamRevision.setStatus("current")
_LocalOamFuncSupport_Type = Integer32
_LocalOamFuncSupport_Object = MibScalar
localOamFuncSupport = _LocalOamFuncSupport_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 4, 6),
    _LocalOamFuncSupport_Type()
)
localOamFuncSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localOamFuncSupport.setStatus("current")
_PeerOamStatus_Type = Integer32
_PeerOamStatus_Object = MibScalar
peerOamStatus = _PeerOamStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 4, 7),
    _PeerOamStatus_Type()
)
peerOamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerOamStatus.setStatus("current")
_PeerOamMacAddr_Type = MacAddress
_PeerOamMacAddr_Object = MibScalar
peerOamMacAddr = _PeerOamMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 4, 8),
    _PeerOamMacAddr_Type()
)
peerOamMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerOamMacAddr.setStatus("current")
_PeerOamOUI_Type = OctetString
_PeerOamOUI_Object = MibScalar
peerOamOUI = _PeerOamOUI_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 4, 9),
    _PeerOamOUI_Type()
)
peerOamOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerOamOUI.setStatus("current")
_PeerOamVendor_Type = Integer32
_PeerOamVendor_Object = MibScalar
peerOamVendor = _PeerOamVendor_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 4, 10),
    _PeerOamVendor_Type()
)
peerOamVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerOamVendor.setStatus("current")
_PeerOamMode_Type = Integer32
_PeerOamMode_Object = MibScalar
peerOamMode = _PeerOamMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 4, 11),
    _PeerOamMode_Type()
)
peerOamMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerOamMode.setStatus("current")
_PeerOamMaxPdu_Type = Integer32
_PeerOamMaxPdu_Object = MibScalar
peerOamMaxPdu = _PeerOamMaxPdu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 4, 12),
    _PeerOamMaxPdu_Type()
)
peerOamMaxPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerOamMaxPdu.setStatus("current")
_PeerOamRevision_Type = Integer32
_PeerOamRevision_Object = MibScalar
peerOamRevision = _PeerOamRevision_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 4, 13),
    _PeerOamRevision_Type()
)
peerOamRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerOamRevision.setStatus("current")
_PeerOamFuncSupport_Type = Integer32
_PeerOamFuncSupport_Object = MibScalar
peerOamFuncSupport = _PeerOamFuncSupport_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 4, 14),
    _PeerOamFuncSupport_Type()
)
peerOamFuncSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerOamFuncSupport.setStatus("current")
_PonLoopbackStatus_Type = OctetString
_PonLoopbackStatus_Object = MibScalar
ponLoopbackStatus = _PonLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 4, 15),
    _PonLoopbackStatus_Type()
)
ponLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponLoopbackStatus.setStatus("current")
_PonFirmwareInfo_ObjectIdentity = ObjectIdentity
ponFirmwareInfo = _PonFirmwareInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 5)
)


class _EponStatus_Type(Integer32):
    """Custom type eponStatus based on Integer32"""
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
        *(("registered", 1),
          ("deregistered", 2),
          ("discovered", 3),
          ("lost", 4),
          ("unknown", 5))
    )


_EponStatus_Type.__name__ = "Integer32"
_EponStatus_Object = MibScalar
eponStatus = _EponStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 5, 1),
    _EponStatus_Type()
)
eponStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponStatus.setStatus("current")
_SoftWareVersion_Type = OctetString
_SoftWareVersion_Object = MibScalar
softWareVersion = _SoftWareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 5, 2),
    _SoftWareVersion_Type()
)
softWareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softWareVersion.setStatus("current")
_LoaderVersion_Type = OctetString
_LoaderVersion_Object = MibScalar
loaderVersion = _LoaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 5, 3),
    _LoaderVersion_Type()
)
loaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loaderVersion.setStatus("current")
_RegisterOltInfo_Type = OctetString
_RegisterOltInfo_Object = MibScalar
registerOltInfo = _RegisterOltInfo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 5, 4),
    _RegisterOltInfo_Type()
)
registerOltInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registerOltInfo.setStatus("current")
_RegisterOnuInfo_Type = OctetString
_RegisterOnuInfo_Object = MibScalar
registerOnuInfo = _RegisterOnuInfo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 5, 5),
    _RegisterOnuInfo_Type()
)
registerOnuInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registerOnuInfo.setStatus("current")
_PortNum_Type = Integer32
_PortNum_Object = MibScalar
portNum = _PortNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 5, 6),
    _PortNum_Type()
)
portNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portNum.setStatus("current")


class _Registered_Type(Integer32):
    """Custom type registered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_Registered_Type.__name__ = "Integer32"
_Registered_Object = MibScalar
registered = _Registered_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 5, 7),
    _Registered_Type()
)
registered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registered.setStatus("current")


class _Authenticated_Type(Integer32):
    """Custom type authenticated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_Authenticated_Type.__name__ = "Integer32"
_Authenticated_Object = MibScalar
authenticated = _Authenticated_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 5, 8),
    _Authenticated_Type()
)
authenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authenticated.setStatus("current")
_PonConfigMac_Type = MacAddress
_PonConfigMac_Object = MibScalar
ponConfigMac = _PonConfigMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 5, 9),
    _PonConfigMac_Type()
)
ponConfigMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponConfigMac.setStatus("current")
_ModeAndOamVer_Type = Integer32
_ModeAndOamVer_Object = MibScalar
modeAndOamVer = _ModeAndOamVer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 5, 10),
    _ModeAndOamVer_Type()
)
modeAndOamVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modeAndOamVer.setStatus("current")
_MpcpTimeout_Type = Integer32
_MpcpTimeout_Object = MibScalar
mpcpTimeout = _MpcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 5, 11),
    _MpcpTimeout_Type()
)
mpcpTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcpTimeout.setStatus("current")
_CtrlVlan_Type = Integer32
_CtrlVlan_Object = MibScalar
ctrlVlan = _CtrlVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 5, 12),
    _CtrlVlan_Type()
)
ctrlVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlVlan.setStatus("current")
_VendPonUni_Type = OctetString
_VendPonUni_Object = MibScalar
vendPonUni = _VendPonUni_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 5, 13),
    _VendPonUni_Type()
)
vendPonUni.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendPonUni.setStatus("current")
_CtcOui_Type = OctetString
_CtcOui_Object = MibScalar
ctcOui = _CtcOui_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 5, 14),
    _CtcOui_Type()
)
ctcOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcOui.setStatus("current")
_CtcVendor_Type = OctetString
_CtcVendor_Object = MibScalar
ctcVendor = _CtcVendor_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 5, 15),
    _CtcVendor_Type()
)
ctcVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcVendor.setStatus("current")
_CtcModel_Type = OctetString
_CtcModel_Object = MibScalar
ctcModel = _CtcModel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 21, 5, 16),
    _CtcModel_Type()
)
ctcModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctcModel.setStatus("current")
_EthernetOam_ObjectIdentity = ObjectIdentity
ethernetOam = _EthernetOam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22)
)


class _EthernetOamStatus_Type(Integer32):
    """Custom type ethernetOamStatus based on Integer32"""
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


_EthernetOamStatus_Type.__name__ = "Integer32"
_EthernetOamStatus_Object = MibScalar
ethernetOamStatus = _EthernetOamStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 1),
    _EthernetOamStatus_Type()
)
ethernetOamStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetOamStatus.setStatus("current")
_EthernetOamOuiDescr_Type = OctetString
_EthernetOamOuiDescr_Object = MibScalar
ethernetOamOuiDescr = _EthernetOamOuiDescr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 2),
    _EthernetOamOuiDescr_Type()
)
ethernetOamOuiDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetOamOuiDescr.setStatus("current")
_OrgSpecificTimeStamp_Type = Integer32
_OrgSpecificTimeStamp_Object = MibScalar
orgSpecificTimeStamp = _OrgSpecificTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 3),
    _OrgSpecificTimeStamp_Type()
)
orgSpecificTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    orgSpecificTimeStamp.setStatus("current")
_RemoteLoopbackTimeout_Type = Integer32
_RemoteLoopbackTimeout_Object = MibScalar
remoteLoopbackTimeout = _RemoteLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 4),
    _RemoteLoopbackTimeout_Type()
)
remoteLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteLoopbackTimeout.setStatus("current")
_EthernetOamIfConfigTable_Object = MibTable
ethernetOamIfConfigTable = _EthernetOamIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 5)
)
if mibBuilder.loadTexts:
    ethernetOamIfConfigTable.setStatus("current")
_EthernetOamIfConfigEntry_Object = MibTableRow
ethernetOamIfConfigEntry = _EthernetOamIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 5, 1)
)
ethernetOamIfConfigEntry.setIndexNames(
    (0, "Es2952-MIB", "portId"),
)
if mibBuilder.loadTexts:
    ethernetOamIfConfigEntry.setStatus("current")


class _EthernetOamIfStatus_Type(Integer32):
    """Custom type ethernetOamIfStatus based on Integer32"""
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


_EthernetOamIfStatus_Type.__name__ = "Integer32"
_EthernetOamIfStatus_Object = MibTableColumn
ethernetOamIfStatus = _EthernetOamIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 5, 1, 2),
    _EthernetOamIfStatus_Type()
)
ethernetOamIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetOamIfStatus.setStatus("current")


class _RemoteLoopbackIfStatus_Type(Integer32):
    """Custom type remoteLoopbackIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_RemoteLoopbackIfStatus_Type.__name__ = "Integer32"
_RemoteLoopbackIfStatus_Object = MibTableColumn
remoteLoopbackIfStatus = _RemoteLoopbackIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 5, 1, 3),
    _RemoteLoopbackIfStatus_Type()
)
remoteLoopbackIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteLoopbackIfStatus.setStatus("current")
_IfPeriodTimeoutMode_Type = OctetString
_IfPeriodTimeoutMode_Object = MibTableColumn
ifPeriodTimeoutMode = _IfPeriodTimeoutMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 5, 1, 4),
    _IfPeriodTimeoutMode_Type()
)
ifPeriodTimeoutMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifPeriodTimeoutMode.setStatus("current")


class _IfLinkMonitorStatus_Type(Integer32):
    """Custom type ifLinkMonitorStatus based on Integer32"""
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


_IfLinkMonitorStatus_Type.__name__ = "Integer32"
_IfLinkMonitorStatus_Object = MibTableColumn
ifLinkMonitorStatus = _IfLinkMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 5, 1, 5),
    _IfLinkMonitorStatus_Type()
)
ifLinkMonitorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifLinkMonitorStatus.setStatus("current")
_IfLinkSymbolPeriodThresholdWindow_Type = OctetString
_IfLinkSymbolPeriodThresholdWindow_Object = MibTableColumn
ifLinkSymbolPeriodThresholdWindow = _IfLinkSymbolPeriodThresholdWindow_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 5, 1, 6),
    _IfLinkSymbolPeriodThresholdWindow_Type()
)
ifLinkSymbolPeriodThresholdWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifLinkSymbolPeriodThresholdWindow.setStatus("current")
_IfLinkFrameThresholdWindow_Type = OctetString
_IfLinkFrameThresholdWindow_Object = MibTableColumn
ifLinkFrameThresholdWindow = _IfLinkFrameThresholdWindow_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 5, 1, 7),
    _IfLinkFrameThresholdWindow_Type()
)
ifLinkFrameThresholdWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifLinkFrameThresholdWindow.setStatus("current")
_IfLinkFramePeriodThresholdWindow_Type = OctetString
_IfLinkFramePeriodThresholdWindow_Object = MibTableColumn
ifLinkFramePeriodThresholdWindow = _IfLinkFramePeriodThresholdWindow_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 5, 1, 8),
    _IfLinkFramePeriodThresholdWindow_Type()
)
ifLinkFramePeriodThresholdWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifLinkFramePeriodThresholdWindow.setStatus("current")
_IfLinkFrameSecondsThresholdWindow_Type = OctetString
_IfLinkFrameSecondsThresholdWindow_Object = MibTableColumn
ifLinkFrameSecondsThresholdWindow = _IfLinkFrameSecondsThresholdWindow_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 5, 1, 9),
    _IfLinkFrameSecondsThresholdWindow_Type()
)
ifLinkFrameSecondsThresholdWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifLinkFrameSecondsThresholdWindow.setStatus("current")
_EthernetOamShowTable_Object = MibTable
ethernetOamShowTable = _EthernetOamShowTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 6)
)
if mibBuilder.loadTexts:
    ethernetOamShowTable.setStatus("current")
_EthernetOamShowEntry_Object = MibTableRow
ethernetOamShowEntry = _EthernetOamShowEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 6, 1)
)
ethernetOamShowEntry.setIndexNames(
    (0, "Es2952-MIB", "portId"),
)
if mibBuilder.loadTexts:
    ethernetOamShowEntry.setStatus("current")
_EthernetOamShowDiscovery_Type = OctetString
_EthernetOamShowDiscovery_Object = MibTableColumn
ethernetOamShowDiscovery = _EthernetOamShowDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 6, 1, 2),
    _EthernetOamShowDiscovery_Type()
)
ethernetOamShowDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamShowDiscovery.setStatus("current")
_EthernetOamShowLinkMonitor_Type = OctetString
_EthernetOamShowLinkMonitor_Object = MibTableColumn
ethernetOamShowLinkMonitor = _EthernetOamShowLinkMonitor_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 6, 1, 3),
    _EthernetOamShowLinkMonitor_Type()
)
ethernetOamShowLinkMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamShowLinkMonitor.setStatus("current")
_EthernetOamShowStatistics_Type = OctetString
_EthernetOamShowStatistics_Object = MibTableColumn
ethernetOamShowStatistics = _EthernetOamShowStatistics_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 6, 1, 4),
    _EthernetOamShowStatistics_Type()
)
ethernetOamShowStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetOamShowStatistics.setStatus("current")
_RemoteMAC_Type = MacAddress
_RemoteMAC_Object = MibScalar
remoteMAC = _RemoteMAC_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 15),
    _RemoteMAC_Type()
)
remoteMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    remoteMAC.setStatus("current")
_OpticalInformation_ObjectIdentity = ObjectIdentity
opticalInformation = _OpticalInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 23)
)
_OpticalInfoTable_Object = MibTable
opticalInfoTable = _OpticalInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 23, 1)
)
if mibBuilder.loadTexts:
    opticalInfoTable.setStatus("current")
_OpticalInfoEntry_Object = MibTableRow
opticalInfoEntry = _OpticalInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 23, 1, 1)
)
opticalInfoEntry.setIndexNames(
    (0, "Es2952-MIB", "opticalInfoPortId"),
)
if mibBuilder.loadTexts:
    opticalInfoEntry.setStatus("current")
_OpticalInfoPortId_Type = Unsigned32
_OpticalInfoPortId_Object = MibTableColumn
opticalInfoPortId = _OpticalInfoPortId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 23, 1, 1, 1),
    _OpticalInfoPortId_Type()
)
opticalInfoPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalInfoPortId.setStatus("current")


class _OpticalInfoIfName_Type(DisplayString):
    """Custom type opticalInfoIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OpticalInfoIfName_Type.__name__ = "DisplayString"
_OpticalInfoIfName_Object = MibTableColumn
opticalInfoIfName = _OpticalInfoIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 23, 1, 1, 2),
    _OpticalInfoIfName_Type()
)
opticalInfoIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalInfoIfName.setStatus("current")


class _OpticalInfoOnline_Type(Integer32):
    """Custom type opticalInfoOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2))
    )


_OpticalInfoOnline_Type.__name__ = "Integer32"
_OpticalInfoOnline_Object = MibTableColumn
opticalInfoOnline = _OpticalInfoOnline_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 23, 1, 1, 3),
    _OpticalInfoOnline_Type()
)
opticalInfoOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalInfoOnline.setStatus("current")
_OpticalInfoSWaveLenth_Type = Integer32
_OpticalInfoSWaveLenth_Object = MibTableColumn
opticalInfoSWaveLenth = _OpticalInfoSWaveLenth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 23, 1, 1, 11),
    _OpticalInfoSWaveLenth_Type()
)
opticalInfoSWaveLenth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalInfoSWaveLenth.setStatus("current")


class _OpticalInfoPowerSupport_Type(Integer32):
    """Custom type opticalInfoPowerSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_OpticalInfoPowerSupport_Type.__name__ = "Integer32"
_OpticalInfoPowerSupport_Object = MibTableColumn
opticalInfoPowerSupport = _OpticalInfoPowerSupport_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 23, 1, 1, 12),
    _OpticalInfoPowerSupport_Type()
)
opticalInfoPowerSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalInfoPowerSupport.setStatus("current")


class _OpticalInfoSRxPower_Type(DisplayString):
    """Custom type opticalInfoSRxPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OpticalInfoSRxPower_Type.__name__ = "DisplayString"
_OpticalInfoSRxPower_Object = MibTableColumn
opticalInfoSRxPower = _OpticalInfoSRxPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 23, 1, 1, 13),
    _OpticalInfoSRxPower_Type()
)
opticalInfoSRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalInfoSRxPower.setStatus("current")


class _OpticalInfoSRxPowerValid_Type(Integer32):
    """Custom type opticalInfoSRxPowerValid based on Integer32"""
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


_OpticalInfoSRxPowerValid_Type.__name__ = "Integer32"
_OpticalInfoSRxPowerValid_Object = MibTableColumn
opticalInfoSRxPowerValid = _OpticalInfoSRxPowerValid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 23, 1, 1, 14),
    _OpticalInfoSRxPowerValid_Type()
)
opticalInfoSRxPowerValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalInfoSRxPowerValid.setStatus("current")


class _OpticalInfoSTxPower_Type(DisplayString):
    """Custom type opticalInfoSTxPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OpticalInfoSTxPower_Type.__name__ = "DisplayString"
_OpticalInfoSTxPower_Object = MibTableColumn
opticalInfoSTxPower = _OpticalInfoSTxPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 23, 1, 1, 15),
    _OpticalInfoSTxPower_Type()
)
opticalInfoSTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalInfoSTxPower.setStatus("current")


class _OpticalInfoSTxPowerValid_Type(Integer32):
    """Custom type opticalInfoSTxPowerValid based on Integer32"""
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


_OpticalInfoSTxPowerValid_Type.__name__ = "Integer32"
_OpticalInfoSTxPowerValid_Object = MibTableColumn
opticalInfoSTxPowerValid = _OpticalInfoSTxPowerValid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 23, 1, 1, 16),
    _OpticalInfoSTxPowerValid_Type()
)
opticalInfoSTxPowerValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalInfoSTxPowerValid.setStatus("current")


class _OpticalInfoSTxPowerStatus_Type(Integer32):
    """Custom type opticalInfoSTxPowerStatus based on Integer32"""
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
        *(("normal", 0),
          ("warning", 1),
          ("alarm", 2),
          ("null", 3))
    )


_OpticalInfoSTxPowerStatus_Type.__name__ = "Integer32"
_OpticalInfoSTxPowerStatus_Object = MibTableColumn
opticalInfoSTxPowerStatus = _OpticalInfoSTxPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 23, 1, 1, 17),
    _OpticalInfoSTxPowerStatus_Type()
)
opticalInfoSTxPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalInfoSTxPowerStatus.setStatus("current")


class _OpticalInfoSRxPowerStatus_Type(Integer32):
    """Custom type opticalInfoSRxPowerStatus based on Integer32"""
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
        *(("normal", 0),
          ("warning", 1),
          ("alarm", 2),
          ("null", 3))
    )


_OpticalInfoSRxPowerStatus_Type.__name__ = "Integer32"
_OpticalInfoSRxPowerStatus_Object = MibTableColumn
opticalInfoSRxPowerStatus = _OpticalInfoSRxPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 23, 1, 1, 18),
    _OpticalInfoSRxPowerStatus_Type()
)
opticalInfoSRxPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalInfoSRxPowerStatus.setStatus("current")


class _OpticalInfoVName_Type(DisplayString):
    """Custom type opticalInfoVName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OpticalInfoVName_Type.__name__ = "DisplayString"
_OpticalInfoVName_Object = MibTableColumn
opticalInfoVName = _OpticalInfoVName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 23, 1, 1, 23),
    _OpticalInfoVName_Type()
)
opticalInfoVName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalInfoVName.setStatus("current")


class _OpticalInfoType_Type(DisplayString):
    """Custom type opticalInfoType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OpticalInfoType_Type.__name__ = "DisplayString"
_OpticalInfoType_Object = MibTableColumn
opticalInfoType = _OpticalInfoType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 23, 1, 1, 24),
    _OpticalInfoType_Type()
)
opticalInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalInfoType.setStatus("current")


class _OpticalInfoVSn_Type(DisplayString):
    """Custom type opticalInfoVSn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OpticalInfoVSn_Type.__name__ = "DisplayString"
_OpticalInfoVSn_Object = MibTableColumn
opticalInfoVSn = _OpticalInfoVSn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 23, 1, 1, 26),
    _OpticalInfoVSn_Type()
)
opticalInfoVSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalInfoVSn.setStatus("current")
_OpticalInfoDistanse_Type = Integer32
_OpticalInfoDistanse_Object = MibTableColumn
opticalInfoDistanse = _OpticalInfoDistanse_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 23, 1, 1, 27),
    _OpticalInfoDistanse_Type()
)
opticalInfoDistanse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalInfoDistanse.setStatus("current")


class _OpticalInfoMode_Type(Integer32):
    """Custom type opticalInfoMode based on Integer32"""
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
        *(("null", 0),
          ("single", 1),
          ("multi", 2),
          ("copper", 3))
    )


_OpticalInfoMode_Type.__name__ = "Integer32"
_OpticalInfoMode_Object = MibTableColumn
opticalInfoMode = _OpticalInfoMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 23, 1, 1, 28),
    _OpticalInfoMode_Type()
)
opticalInfoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalInfoMode.setStatus("current")

# Managed Objects groups


# Notification objects

dynamicMacExceedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 2, 5)
)
dynamicMacExceedTrap.setObjects(
      *(("Es2952-MIB", "portId"),
        ("Es2952-MIB", "dynamicMacMaxCount"))
)
if mibBuilder.loadTexts:
    dynamicMacExceedTrap.setStatus(
        "current"
    )

loopDetectPortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 9, 5)
)
loopDetectPortTrap.setObjects(
      *(("Es2952-MIB", "loopDetectPortId"),
        ("Es2952-MIB", "loopDetectPortInVlan"),
        ("Es2952-MIB", "loopDetectPortBlockStatus"))
)
if mibBuilder.loadTexts:
    loopDetectPortTrap.setStatus(
        "current"
    )

loopDetectTrunkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 9, 6)
)
loopDetectTrunkTrap.setObjects(
      *(("Es2952-MIB", "loopDetectTrunkId"),
        ("Es2952-MIB", "loopDetectTrunkInVlan"),
        ("Es2952-MIB", "trunkPorts"),
        ("Es2952-MIB", "loopDetectTrunkBlockStatus"))
)
if mibBuilder.loadTexts:
    loopDetectTrunkTrap.setStatus(
        "current"
    )

linkMonitorSymbolPeriodTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 7)
)
linkMonitorSymbolPeriodTrap.setObjects(
      *(("Es2952-MIB", "portId"),
        ("Es2952-MIB", "switchMac"),
        ("Es2952-MIB", "remoteMAC"))
)
if mibBuilder.loadTexts:
    linkMonitorSymbolPeriodTrap.setStatus(
        "current"
    )

linkMonitorFrameTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 8)
)
linkMonitorFrameTrap.setObjects(
      *(("Es2952-MIB", "portId"),
        ("Es2952-MIB", "switchMac"),
        ("Es2952-MIB", "remoteMAC"))
)
if mibBuilder.loadTexts:
    linkMonitorFrameTrap.setStatus(
        "current"
    )

linkMonitorFramePeriodTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 9)
)
linkMonitorFramePeriodTrap.setObjects(
      *(("Es2952-MIB", "portId"),
        ("Es2952-MIB", "switchMac"),
        ("Es2952-MIB", "remoteMAC"))
)
if mibBuilder.loadTexts:
    linkMonitorFramePeriodTrap.setStatus(
        "current"
    )

linkMonitorFrameSecondsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 10)
)
linkMonitorFrameSecondsTrap.setObjects(
      *(("Es2952-MIB", "portId"),
        ("Es2952-MIB", "switchMac"),
        ("Es2952-MIB", "remoteMAC"))
)
if mibBuilder.loadTexts:
    linkMonitorFrameSecondsTrap.setStatus(
        "current"
    )

remoteLinkFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 11)
)
remoteLinkFailTrap.setObjects(
      *(("Es2952-MIB", "portId"),
        ("Es2952-MIB", "switchMac"),
        ("Es2952-MIB", "remoteMAC"))
)
if mibBuilder.loadTexts:
    remoteLinkFailTrap.setStatus(
        "current"
    )

remoteLinkOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 12)
)
remoteLinkOKTrap.setObjects(
      *(("Es2952-MIB", "portId"),
        ("Es2952-MIB", "switchMac"),
        ("Es2952-MIB", "remoteMAC"))
)
if mibBuilder.loadTexts:
    remoteLinkOKTrap.setStatus(
        "current"
    )

dyingGaspTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 13)
)
dyingGaspTrap.setObjects(
      *(("Es2952-MIB", "portId"),
        ("Es2952-MIB", "switchMac"),
        ("Es2952-MIB", "remoteMAC"))
)
if mibBuilder.loadTexts:
    dyingGaspTrap.setStatus(
        "current"
    )

remoteDiscoveryFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 15, 2, 11, 22, 14)
)
remoteDiscoveryFailTrap.setObjects(
      *(("Es2952-MIB", "portId"),
        ("Es2952-MIB", "switchMac"),
        ("Es2952-MIB", "remoteMAC"))
)
if mibBuilder.loadTexts:
    remoteDiscoveryFailTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Es2952-MIB",
    **{"PortList": PortList,
       "MacAddress": MacAddress,
       "DisplayString": DisplayString,
       "zte": zte,
       "ethernetSwitch": ethernetSwitch,
       "layer2Switch": layer2Switch,
       "series2952Switch": series2952Switch,
       "switchSystem": switchSystem,
       "cpuLoad5s": cpuLoad5s,
       "cpuLoad30s": cpuLoad30s,
       "cpuLoad2m": cpuLoad2m,
       "maxCpuLoad": maxCpuLoad,
       "memUtilityRatio": memUtilityRatio,
       "switchType": switchType,
       "switchMac": switchMac,
       "reboot": reboot,
       "saveConfig": saveConfig,
       "sysDateTime": sysDateTime,
       "port": port,
       "portNumber": portNumber,
       "portTable": portTable,
       "portEntry": portEntry,
       "portId": portId,
       "portName": portName,
       "portDescr": portDescr,
       "portAdminStatus": portAdminStatus,
       "portOperStatus": portOperStatus,
       "portAdminWorkMode": portAdminWorkMode,
       "portOperDuplex": portOperDuplex,
       "portOperSpeed": portOperSpeed,
       "portPvid": portPvid,
       "portFlowControl": portFlowControl,
       "portVlanMode": portVlanMode,
       "portSecurity": portSecurity,
       "portPriority": portPriority,
       "portMulticast": portMulticast,
       "portMediaType": portMediaType,
       "isPortInTrunk": isPortInTrunk,
       "portLoopdetectStatus": portLoopdetectStatus,
       "dynamicMacMaxCount": dynamicMacMaxCount,
       "dynamicMacExceedTrap": dynamicMacExceedTrap,
       "vlan": vlan,
       "maxVlanId": maxVlanId,
       "maxSupportedVlans": maxSupportedVlans,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanId": vlanId,
       "vlanUntaggedPorts": vlanUntaggedPorts,
       "vlanTaggedPorts": vlanTaggedPorts,
       "vlanName": vlanName,
       "vlanAdminStatus": vlanAdminStatus,
       "vlanUntaggedTrunks": vlanUntaggedTrunks,
       "vlanTaggedTrunks": vlanTaggedTrunks,
       "vlanAssistantTable": vlanAssistantTable,
       "vlanAssistantEntry": vlanAssistantEntry,
       "assVlanId": assVlanId,
       "mirror": mirror,
       "sourcePortsIngress": sourcePortsIngress,
       "sourcePortsEgress": sourcePortsEgress,
       "desPortIngress": desPortIngress,
       "desPortEgress": desPortEgress,
       "qos": qos,
       "queueScheduleWeight": queueScheduleWeight,
       "queueScheduleMode0": queueScheduleMode0,
       "queueScheduleMode1": queueScheduleMode1,
       "queueScheduleMode2": queueScheduleMode2,
       "queueScheduleMode3": queueScheduleMode3,
       "qosPrimapUsrToTraffic": qosPrimapUsrToTraffic,
       "qosPolicerTable": qosPolicerTable,
       "qosPolicerEntry": qosPolicerEntry,
       "policerID": policerID,
       "qosPolicerPara": qosPolicerPara,
       "qosExceededOper": qosExceededOper,
       "qosPolicerBurst": qosPolicerBurst,
       "ipPriToTrafficTable": ipPriToTrafficTable,
       "ipPriToTrafficEntry": ipPriToTrafficEntry,
       "ipPriority": ipPriority,
       "tcFePort": tcFePort,
       "tcGePort": tcGePort,
       "fePortIngBandTable": fePortIngBandTable,
       "fePortIngBandEntry": fePortIngBandEntry,
       "fePortID": fePortID,
       "sessionNo": sessionNo,
       "sessionStatus": sessionStatus,
       "feIngressRate": feIngressRate,
       "feIngressPkType": feIngressPkType,
       "quePriorityStatus": quePriorityStatus,
       "mgmtNoRatelimitStatus": mgmtNoRatelimitStatus,
       "gePortIngBandTable": gePortIngBandTable,
       "gePortIngBandEntry": gePortIngBandEntry,
       "gePortID": gePortID,
       "geIngressStatus": geIngressStatus,
       "geIngressRate": geIngressRate,
       "geIngressPkType": geIngressPkType,
       "geQueScheTable": geQueScheTable,
       "geQueScheEntry": geQueScheEntry,
       "gePortSessionID": gePortSessionID,
       "queueID": queueID,
       "queueSchedule": queueSchedule,
       "geQosPrimapUsrToTraffic": geQosPrimapUsrToTraffic,
       "gePortIp2UserTable": gePortIp2UserTable,
       "gePortIp2UserEntry": gePortIp2UserEntry,
       "userPriority": userPriority,
       "portQosParamTable": portQosParamTable,
       "portQosParamEntry": portQosParamEntry,
       "portID": portID,
       "bandWidthEgress": bandWidthEgress,
       "upPriorityEnable": upPriorityEnable,
       "dscpPriorityEnable": dscpPriorityEnable,
       "queScheduleMode": queScheduleMode,
       "remaptagToPriority": remaptagToPriority,
       "pvlan": pvlan,
       "sessionMaxNum": sessionMaxNum,
       "pvlanTable": pvlanTable,
       "pvlanEntry": pvlanEntry,
       "sessionId": sessionId,
       "proAndIsoPortOrTrunk": proAndIsoPortOrTrunk,
       "lacp": lacp,
       "lacpAdminStatus": lacpAdminStatus,
       "lacpPriority": lacpPriority,
       "trunkNumber": trunkNumber,
       "trunkTable": trunkTable,
       "trunkEntry": trunkEntry,
       "trunkId": trunkId,
       "trunkPvid": trunkPvid,
       "trunkMulticast": trunkMulticast,
       "trunkPorts": trunkPorts,
       "trunkMode": trunkMode,
       "lacpPortTable": lacpPortTable,
       "lacpPortEntry": lacpPortEntry,
       "lacpPortId": lacpPortId,
       "lacpPortMode": lacpPortMode,
       "lacpPortTimeout": lacpPortTimeout,
       "layer3": layer3,
       "layer3PortTable": layer3PortTable,
       "layer3PortEntry": layer3PortEntry,
       "layer3PortId": layer3PortId,
       "layer3PortIpAddrAndMask": layer3PortIpAddrAndMask,
       "layer3PortMacAddr": layer3PortMacAddr,
       "layer3PortVlanId": layer3PortVlanId,
       "layer3PortAdminStatus": layer3PortAdminStatus,
       "loopDetect": loopDetect,
       "loopDetectBlockDelay": loopDetectBlockDelay,
       "loopDetectSendPktInterval": loopDetectSendPktInterval,
       "loopDetectPortTable": loopDetectPortTable,
       "loopDetectPortEntry": loopDetectPortEntry,
       "loopDetectPortId": loopDetectPortId,
       "loopDetectPortAdminStatus": loopDetectPortAdminStatus,
       "loopDetectPortProtectStatus": loopDetectPortProtectStatus,
       "loopDetectPortLoopStatus": loopDetectPortLoopStatus,
       "loopDetectPortBlockStatus": loopDetectPortBlockStatus,
       "loopDetectPortInVlan": loopDetectPortInVlan,
       "loopDetectTrunkTable": loopDetectTrunkTable,
       "loopDetectTrunkEntry": loopDetectTrunkEntry,
       "loopDetectTrunkId": loopDetectTrunkId,
       "loopDetectTrunkAdminStatus": loopDetectTrunkAdminStatus,
       "loopDetectTrunkProtectStatus": loopDetectTrunkProtectStatus,
       "loopDetectTrunkLoopStatus": loopDetectTrunkLoopStatus,
       "loopDetectTrunkBlockStatus": loopDetectTrunkBlockStatus,
       "loopDetectTrunkInVlan": loopDetectTrunkInVlan,
       "loopDetectPortTrap": loopDetectPortTrap,
       "loopDetectTrunkTrap": loopDetectTrunkTrap,
       "vlanTranslation": vlanTranslation,
       "vlanTranslationTable": vlanTranslationTable,
       "vlanTranslationEntry": vlanTranslationEntry,
       "ingressPortId": ingressPortId,
       "vlanTranslationEnable": vlanTranslationEnable,
       "vlanTranslationStatus": vlanTranslationStatus,
       "stp": stp,
       "stpAdminStatus": stpAdminStatus,
       "vct": vct,
       "vctPortTable": vctPortTable,
       "vctPortEntry": vctPortEntry,
       "vctPortId": vctPortId,
       "vctDo": vctDo,
       "vctIsValid": vctIsValid,
       "vctPair1Result": vctPair1Result,
       "vctPair1Lenth": vctPair1Lenth,
       "vctPair2Result": vctPair2Result,
       "vctPair2Lenth": vctPair2Lenth,
       "vctPair3Result": vctPair3Result,
       "vctPair3Lenth": vctPair3Lenth,
       "vctPair4Result": vctPair4Result,
       "vctPair4Lenth": vctPair4Lenth,
       "syslog": syslog,
       "syslogStatus": syslogStatus,
       "syslogLevel": syslogLevel,
       "enabledModule": enabledModule,
       "serverMaxNum": serverMaxNum,
       "serverTable": serverTable,
       "serverEntry": serverEntry,
       "serverId": serverId,
       "serverIP": serverIP,
       "serverName": serverName,
       "serverAdminStatus": serverAdminStatus,
       "ntp": ntp,
       "synchronizeStatus": synchronizeStatus,
       "protocolStatus": protocolStatus,
       "srvIpAddrAndVersion": srvIpAddrAndVersion,
       "sourceIpAddr": sourceIpAddr,
       "loginUser": loginUser,
       "userTable": userTable,
       "userEntry": userEntry,
       "userName": userName,
       "userAttr": userAttr,
       "loginPass": loginPass,
       "adminPass": adminPass,
       "snmpConfig": snmpConfig,
       "communityTable": communityTable,
       "communityEntry": communityEntry,
       "communityName": communityName,
       "communityAttr": communityAttr,
       "viewAttached": viewAttached,
       "viewTable": viewTable,
       "viewEntry": viewEntry,
       "viewIndex": viewIndex,
       "viewName": viewName,
       "attrAndOid": attrAndOid,
       "trapHostTable": trapHostTable,
       "trapHostEntry": trapHostEntry,
       "traphostIP": traphostIP,
       "traphostType": traphostType,
       "commuName": commuName,
       "traphostVer": traphostVer,
       "trapEnable": trapEnable,
       "acl": acl,
       "timeAclTable": timeAclTable,
       "timeAclEntry": timeAclEntry,
       "timeRangeName": timeRangeName,
       "timeRange": timeRange,
       "basicAclTable": basicAclTable,
       "basicAclEntry": basicAclEntry,
       "basicACLNo": basicACLNo,
       "basicRuleID": basicRuleID,
       "ruleBasicStatus": ruleBasicStatus,
       "ruleBasicACL": ruleBasicACL,
       "extendedAclTable": extendedAclTable,
       "extendedAclEntry": extendedAclEntry,
       "extendedACLNo": extendedACLNo,
       "extendedRuleID": extendedRuleID,
       "ruleExtendedStatus": ruleExtendedStatus,
       "ruleExtendedProtocol": ruleExtendedProtocol,
       "linkAclTable": linkAclTable,
       "linkAclEntry": linkAclEntry,
       "linkACLNo": linkACLNo,
       "linkRuleID": linkRuleID,
       "ruleLinkStatus": ruleLinkStatus,
       "ruleLinkProtocol": ruleLinkProtocol,
       "hybridAclTable": hybridAclTable,
       "hybridAclEntry": hybridAclEntry,
       "hybridACLNo": hybridACLNo,
       "hybridRuleID": hybridRuleID,
       "ruleHybridStatus": ruleHybridStatus,
       "ruleHybridProtocol": ruleHybridProtocol,
       "globalAclTable": globalAclTable,
       "globalAclEntry": globalAclEntry,
       "globalACLNo": globalACLNo,
       "globalRuleID": globalRuleID,
       "ruleGlobalStatus": ruleGlobalStatus,
       "ruleGlobalProtocol": ruleGlobalProtocol,
       "fdb": fdb,
       "fdbAgingTime": fdbAgingTime,
       "fdbFilterTable": fdbFilterTable,
       "fdbFilterEntry": fdbFilterEntry,
       "fdbID": fdbID,
       "fdbFilterAddress": fdbFilterAddress,
       "fdbFilterType": fdbFilterType,
       "fdbStaticPortTable": fdbStaticPortTable,
       "fdbStaticPortEntry": fdbStaticPortEntry,
       "fdbStaticAddress": fdbStaticAddress,
       "portBindMac": portBindMac,
       "fdbStaticTrunkTable": fdbStaticTrunkTable,
       "fdbStaticTrunkEntry": fdbStaticTrunkEntry,
       "trunkBindMac": trunkBindMac,
       "p8021xRelay": p8021xRelay,
       "p8021xRelayAdminStatus": p8021xRelayAdminStatus,
       "igmpSnooping": igmpSnooping,
       "multiGroupTable": multiGroupTable,
       "multiGroupEntry": multiGroupEntry,
       "number": number,
       "vlanID": vlanID,
       "multiGroup": multiGroup,
       "portList": portList,
       "trunkList": trunkList,
       "epon": epon,
       "ponReset": ponReset,
       "portPonInfo": portPonInfo,
       "portPonAdminStatus": portPonAdminStatus,
       "portPonStpState": portPonStpState,
       "portPonFecTx": portPonFecTx,
       "portPonFecRx": portPonFecRx,
       "portPonType": portPonType,
       "portPonOperStatus": portPonOperStatus,
       "portPonLlidPortsNum": portPonLlidPortsNum,
       "ponOamInfo": ponOamInfo,
       "localOamAdmin": localOamAdmin,
       "localOamOper": localOamOper,
       "localOamMode": localOamMode,
       "localOamMaxPdu": localOamMaxPdu,
       "localOamRevision": localOamRevision,
       "localOamFuncSupport": localOamFuncSupport,
       "peerOamStatus": peerOamStatus,
       "peerOamMacAddr": peerOamMacAddr,
       "peerOamOUI": peerOamOUI,
       "peerOamVendor": peerOamVendor,
       "peerOamMode": peerOamMode,
       "peerOamMaxPdu": peerOamMaxPdu,
       "peerOamRevision": peerOamRevision,
       "peerOamFuncSupport": peerOamFuncSupport,
       "ponLoopbackStatus": ponLoopbackStatus,
       "ponFirmwareInfo": ponFirmwareInfo,
       "eponStatus": eponStatus,
       "softWareVersion": softWareVersion,
       "loaderVersion": loaderVersion,
       "registerOltInfo": registerOltInfo,
       "registerOnuInfo": registerOnuInfo,
       "portNum": portNum,
       "registered": registered,
       "authenticated": authenticated,
       "ponConfigMac": ponConfigMac,
       "modeAndOamVer": modeAndOamVer,
       "mpcpTimeout": mpcpTimeout,
       "ctrlVlan": ctrlVlan,
       "vendPonUni": vendPonUni,
       "ctcOui": ctcOui,
       "ctcVendor": ctcVendor,
       "ctcModel": ctcModel,
       "ethernetOam": ethernetOam,
       "ethernetOamStatus": ethernetOamStatus,
       "ethernetOamOuiDescr": ethernetOamOuiDescr,
       "orgSpecificTimeStamp": orgSpecificTimeStamp,
       "remoteLoopbackTimeout": remoteLoopbackTimeout,
       "ethernetOamIfConfigTable": ethernetOamIfConfigTable,
       "ethernetOamIfConfigEntry": ethernetOamIfConfigEntry,
       "ethernetOamIfStatus": ethernetOamIfStatus,
       "remoteLoopbackIfStatus": remoteLoopbackIfStatus,
       "ifPeriodTimeoutMode": ifPeriodTimeoutMode,
       "ifLinkMonitorStatus": ifLinkMonitorStatus,
       "ifLinkSymbolPeriodThresholdWindow": ifLinkSymbolPeriodThresholdWindow,
       "ifLinkFrameThresholdWindow": ifLinkFrameThresholdWindow,
       "ifLinkFramePeriodThresholdWindow": ifLinkFramePeriodThresholdWindow,
       "ifLinkFrameSecondsThresholdWindow": ifLinkFrameSecondsThresholdWindow,
       "ethernetOamShowTable": ethernetOamShowTable,
       "ethernetOamShowEntry": ethernetOamShowEntry,
       "ethernetOamShowDiscovery": ethernetOamShowDiscovery,
       "ethernetOamShowLinkMonitor": ethernetOamShowLinkMonitor,
       "ethernetOamShowStatistics": ethernetOamShowStatistics,
       "linkMonitorSymbolPeriodTrap": linkMonitorSymbolPeriodTrap,
       "linkMonitorFrameTrap": linkMonitorFrameTrap,
       "linkMonitorFramePeriodTrap": linkMonitorFramePeriodTrap,
       "linkMonitorFrameSecondsTrap": linkMonitorFrameSecondsTrap,
       "remoteLinkFailTrap": remoteLinkFailTrap,
       "remoteLinkOKTrap": remoteLinkOKTrap,
       "dyingGaspTrap": dyingGaspTrap,
       "remoteDiscoveryFailTrap": remoteDiscoveryFailTrap,
       "remoteMAC": remoteMAC,
       "opticalInformation": opticalInformation,
       "opticalInfoTable": opticalInfoTable,
       "opticalInfoEntry": opticalInfoEntry,
       "opticalInfoPortId": opticalInfoPortId,
       "opticalInfoIfName": opticalInfoIfName,
       "opticalInfoOnline": opticalInfoOnline,
       "opticalInfoSWaveLenth": opticalInfoSWaveLenth,
       "opticalInfoPowerSupport": opticalInfoPowerSupport,
       "opticalInfoSRxPower": opticalInfoSRxPower,
       "opticalInfoSRxPowerValid": opticalInfoSRxPowerValid,
       "opticalInfoSTxPower": opticalInfoSTxPower,
       "opticalInfoSTxPowerValid": opticalInfoSTxPowerValid,
       "opticalInfoSTxPowerStatus": opticalInfoSTxPowerStatus,
       "opticalInfoSRxPowerStatus": opticalInfoSRxPowerStatus,
       "opticalInfoVName": opticalInfoVName,
       "opticalInfoType": opticalInfoType,
       "opticalInfoVSn": opticalInfoVSn,
       "opticalInfoDistanse": opticalInfoDistanse,
       "opticalInfoMode": opticalInfoMode}
)
