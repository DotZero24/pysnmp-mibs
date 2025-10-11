# SNMP MIB module (RAISECOM-RRCP-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-RRCP-VLAN-MIB
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(rcPortIndex,) = mibBuilder.importSymbols(
    "SWITCH-SYSTEM-MIB",
    "rcPortIndex")

(EnableVar,
 PortList,
 Vlanset) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar",
    "PortList",
    "Vlanset")


# MODULE-IDENTITY

rcRrcpRemoteManagement = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2)
)
if mibBuilder.loadTexts:
    rcRrcpRemoteManagement.setRevisions(
        ("2009-07-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcRrcp_ObjectIdentity = ObjectIdentity
rcRrcp = _RcRrcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52)
)
_RcRemoteVlanConifg_ObjectIdentity = ObjectIdentity
rcRemoteVlanConifg = _RcRemoteVlanConifg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1)
)
_RcRemoteConfigTable_Object = MibTable
rcRemoteConfigTable = _RcRemoteConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rcRemoteConfigTable.setStatus("current")
_RcRemoteConfigEntry_Object = MibTableRow
rcRemoteConfigEntry = _RcRemoteConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 1, 1)
)
rcRemoteConfigEntry.setIndexNames(
    (0, "RAISECOM-RRCP-VLAN-MIB", "rcRemoteHostMacAddr"),
)
if mibBuilder.loadTexts:
    rcRemoteConfigEntry.setStatus("current")
_RcRemoteHostMacAddr_Type = MacAddress
_RcRemoteHostMacAddr_Object = MibTableColumn
rcRemoteHostMacAddr = _RcRemoteHostMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 1, 1, 1),
    _RcRemoteHostMacAddr_Type()
)
rcRemoteHostMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcRemoteHostMacAddr.setStatus("current")


class _RcRemoteHostName_Type(OctetString):
    """Custom type rcRemoteHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RcRemoteHostName_Type.__name__ = "OctetString"
_RcRemoteHostName_Object = MibTableColumn
rcRemoteHostName = _RcRemoteHostName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 1, 1, 2),
    _RcRemoteHostName_Type()
)
rcRemoteHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRemoteHostName.setStatus("current")
_RcRemoteBroadcastStormCtrl_Type = EnableVar
_RcRemoteBroadcastStormCtrl_Object = MibTableColumn
rcRemoteBroadcastStormCtrl = _RcRemoteBroadcastStormCtrl_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 1, 1, 3),
    _RcRemoteBroadcastStormCtrl_Type()
)
rcRemoteBroadcastStormCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRemoteBroadcastStormCtrl.setStatus("current")
_RcRemoteLoopbackDetection_Type = EnableVar
_RcRemoteLoopbackDetection_Object = MibTableColumn
rcRemoteLoopbackDetection = _RcRemoteLoopbackDetection_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 1, 1, 4),
    _RcRemoteLoopbackDetection_Type()
)
rcRemoteLoopbackDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRemoteLoopbackDetection.setStatus("current")
_RcRemoteLoopbackDetectionStatus_Type = PortList
_RcRemoteLoopbackDetectionStatus_Object = MibTableColumn
rcRemoteLoopbackDetectionStatus = _RcRemoteLoopbackDetectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 1, 1, 5),
    _RcRemoteLoopbackDetectionStatus_Type()
)
rcRemoteLoopbackDetectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRemoteLoopbackDetectionStatus.setStatus("current")
_RcRemoteDeviceManageVlan_Type = Integer32
_RcRemoteDeviceManageVlan_Object = MibTableColumn
rcRemoteDeviceManageVlan = _RcRemoteDeviceManageVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 1, 1, 6),
    _RcRemoteDeviceManageVlan_Type()
)
rcRemoteDeviceManageVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRemoteDeviceManageVlan.setStatus("current")
_RcRemoteDeviceCfgWrite_Type = TruthValue
_RcRemoteDeviceCfgWrite_Object = MibTableColumn
rcRemoteDeviceCfgWrite = _RcRemoteDeviceCfgWrite_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 1, 1, 7),
    _RcRemoteDeviceCfgWrite_Type()
)
rcRemoteDeviceCfgWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRemoteDeviceCfgWrite.setStatus("current")


class _RcRemoteDeviceCfgWriteResult_Type(Integer32):
    """Custom type rcRemoteDeviceCfgWriteResult based on Integer32"""
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
          ("saving", 2),
          ("successed", 3),
          ("failed", 4))
    )


_RcRemoteDeviceCfgWriteResult_Type.__name__ = "Integer32"
_RcRemoteDeviceCfgWriteResult_Object = MibTableColumn
rcRemoteDeviceCfgWriteResult = _RcRemoteDeviceCfgWriteResult_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 1, 1, 8),
    _RcRemoteDeviceCfgWriteResult_Type()
)
rcRemoteDeviceCfgWriteResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRemoteDeviceCfgWriteResult.setStatus("current")
_RcRemoteDeviceResetFactory_Type = TruthValue
_RcRemoteDeviceResetFactory_Object = MibTableColumn
rcRemoteDeviceResetFactory = _RcRemoteDeviceResetFactory_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 1, 1, 9),
    _RcRemoteDeviceResetFactory_Type()
)
rcRemoteDeviceResetFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRemoteDeviceResetFactory.setStatus("current")


class _RcRemoteDeviceResetFactoryResult_Type(Integer32):
    """Custom type rcRemoteDeviceResetFactoryResult based on Integer32"""
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
          ("factory-reseting", 2),
          ("successed", 3),
          ("failed", 4))
    )


_RcRemoteDeviceResetFactoryResult_Type.__name__ = "Integer32"
_RcRemoteDeviceResetFactoryResult_Object = MibTableColumn
rcRemoteDeviceResetFactoryResult = _RcRemoteDeviceResetFactoryResult_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 1, 1, 10),
    _RcRemoteDeviceResetFactoryResult_Type()
)
rcRemoteDeviceResetFactoryResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRemoteDeviceResetFactoryResult.setStatus("current")
_RcRemoteDeviceReboot_Type = TruthValue
_RcRemoteDeviceReboot_Object = MibTableColumn
rcRemoteDeviceReboot = _RcRemoteDeviceReboot_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 1, 1, 11),
    _RcRemoteDeviceReboot_Type()
)
rcRemoteDeviceReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRemoteDeviceReboot.setStatus("current")
_RcRemoteVlanCfgTable_Object = MibTable
rcRemoteVlanCfgTable = _RcRemoteVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 2)
)
if mibBuilder.loadTexts:
    rcRemoteVlanCfgTable.setStatus("current")
_RcRemoteVlanCfgEntry_Object = MibTableRow
rcRemoteVlanCfgEntry = _RcRemoteVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 2, 1)
)
rcRemoteVlanCfgEntry.setIndexNames(
    (0, "RAISECOM-RRCP-VLAN-MIB", "rcRemoteHostMacAddr"),
)
if mibBuilder.loadTexts:
    rcRemoteVlanCfgEntry.setStatus("current")


class _RcRemoteSwitchMode_Type(Integer32):
    """Custom type rcRemoteSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 1),
          ("dot1q-vlan", 2),
          ("port-based-vlan", 3))
    )


_RcRemoteSwitchMode_Type.__name__ = "Integer32"
_RcRemoteSwitchMode_Object = MibTableColumn
rcRemoteSwitchMode = _RcRemoteSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 2, 1, 1),
    _RcRemoteSwitchMode_Type()
)
rcRemoteSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRemoteSwitchMode.setStatus("current")


class _RcRemotePortBasedVlanUpLinkPort_Type(Integer32):
    """Custom type rcRemotePortBasedVlanUpLinkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcRemotePortBasedVlanUpLinkPort_Type.__name__ = "Integer32"
_RcRemotePortBasedVlanUpLinkPort_Object = MibTableColumn
rcRemotePortBasedVlanUpLinkPort = _RcRemotePortBasedVlanUpLinkPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 2, 1, 2),
    _RcRemotePortBasedVlanUpLinkPort_Type()
)
rcRemotePortBasedVlanUpLinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRemotePortBasedVlanUpLinkPort.setStatus("current")
_RcRemoteCurrentVlanTable_Object = MibTable
rcRemoteCurrentVlanTable = _RcRemoteCurrentVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 3)
)
if mibBuilder.loadTexts:
    rcRemoteCurrentVlanTable.setStatus("current")
_RcRemoteCurrentVlanEntry_Object = MibTableRow
rcRemoteCurrentVlanEntry = _RcRemoteCurrentVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 3, 1)
)
rcRemoteCurrentVlanEntry.setIndexNames(
    (0, "RAISECOM-RRCP-VLAN-MIB", "rcRemoteHostMacAddr"),
    (0, "RAISECOM-RRCP-VLAN-MIB", "rcRemoteCurrentVlanIndex"),
)
if mibBuilder.loadTexts:
    rcRemoteCurrentVlanEntry.setStatus("current")


class _RcRemoteCurrentVlanIndex_Type(Integer32):
    """Custom type rcRemoteCurrentVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcRemoteCurrentVlanIndex_Type.__name__ = "Integer32"
_RcRemoteCurrentVlanIndex_Object = MibTableColumn
rcRemoteCurrentVlanIndex = _RcRemoteCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 3, 1, 1),
    _RcRemoteCurrentVlanIndex_Type()
)
rcRemoteCurrentVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcRemoteCurrentVlanIndex.setStatus("current")
_RcRemoteCurrentVlanEgressPorts_Type = PortList
_RcRemoteCurrentVlanEgressPorts_Object = MibTableColumn
rcRemoteCurrentVlanEgressPorts = _RcRemoteCurrentVlanEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 3, 1, 2),
    _RcRemoteCurrentVlanEgressPorts_Type()
)
rcRemoteCurrentVlanEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRemoteCurrentVlanEgressPorts.setStatus("current")
_RcRemoteCurrentVlanRowStatus_Type = RowStatus
_RcRemoteCurrentVlanRowStatus_Object = MibTableColumn
rcRemoteCurrentVlanRowStatus = _RcRemoteCurrentVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 3, 1, 3),
    _RcRemoteCurrentVlanRowStatus_Type()
)
rcRemoteCurrentVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcRemoteCurrentVlanRowStatus.setStatus("current")
_RcRemoteVlanPortTable_Object = MibTable
rcRemoteVlanPortTable = _RcRemoteVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 4)
)
if mibBuilder.loadTexts:
    rcRemoteVlanPortTable.setStatus("current")
_RcRemoteVlanPortEntry_Object = MibTableRow
rcRemoteVlanPortEntry = _RcRemoteVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 4, 1)
)
rcRemoteVlanPortEntry.setIndexNames(
    (0, "RAISECOM-RRCP-VLAN-MIB", "rcRemoteHostMacAddr"),
    (0, "RAISECOM-RRCP-VLAN-MIB", "rcRemotePortIndex"),
)
if mibBuilder.loadTexts:
    rcRemoteVlanPortEntry.setStatus("current")


class _RcRemotePortIndex_Type(Integer32):
    """Custom type rcRemotePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcRemotePortIndex_Type.__name__ = "Integer32"
_RcRemotePortIndex_Object = MibTableColumn
rcRemotePortIndex = _RcRemotePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 4, 1, 1),
    _RcRemotePortIndex_Type()
)
rcRemotePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcRemotePortIndex.setStatus("current")


class _RcRemotePortMode_Type(Integer32):
    """Custom type rcRemotePortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("trunk", 2))
    )


_RcRemotePortMode_Type.__name__ = "Integer32"
_RcRemotePortMode_Object = MibTableColumn
rcRemotePortMode = _RcRemotePortMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 4, 1, 2),
    _RcRemotePortMode_Type()
)
rcRemotePortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRemotePortMode.setStatus("current")


class _RcRemotePortNativeVid_Type(Integer32):
    """Custom type rcRemotePortNativeVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcRemotePortNativeVid_Type.__name__ = "Integer32"
_RcRemotePortNativeVid_Object = MibTableColumn
rcRemotePortNativeVid = _RcRemotePortNativeVid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 4, 1, 3),
    _RcRemotePortNativeVid_Type()
)
rcRemotePortNativeVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRemotePortNativeVid.setStatus("current")
_RcRemotePortAccessEgressAllowVlan_Type = Vlanset
_RcRemotePortAccessEgressAllowVlan_Object = MibTableColumn
rcRemotePortAccessEgressAllowVlan = _RcRemotePortAccessEgressAllowVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 4, 1, 4),
    _RcRemotePortAccessEgressAllowVlan_Type()
)
rcRemotePortAccessEgressAllowVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRemotePortAccessEgressAllowVlan.setStatus("current")
_RcRemoteQosCfgTable_Object = MibTable
rcRemoteQosCfgTable = _RcRemoteQosCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 5)
)
if mibBuilder.loadTexts:
    rcRemoteQosCfgTable.setStatus("current")
_RcRemoteQosCfgEntry_Object = MibTableRow
rcRemoteQosCfgEntry = _RcRemoteQosCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 5, 1)
)
rcRemoteQosCfgEntry.setIndexNames(
    (0, "RAISECOM-RRCP-VLAN-MIB", "rcRemoteHostMacAddr"),
)
if mibBuilder.loadTexts:
    rcRemoteQosCfgEntry.setStatus("current")


class _RcRemoteMlsQosTrustMode_Type(Integer32):
    """Custom type rcRemoteMlsQosTrustMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port-priority", 1),
          ("cos", 2))
    )


_RcRemoteMlsQosTrustMode_Type.__name__ = "Integer32"
_RcRemoteMlsQosTrustMode_Object = MibTableColumn
rcRemoteMlsQosTrustMode = _RcRemoteMlsQosTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 5, 1, 1),
    _RcRemoteMlsQosTrustMode_Type()
)
rcRemoteMlsQosTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRemoteMlsQosTrustMode.setStatus("current")


class _RcRemoteMlsQosScheduleMode_Type(Integer32):
    """Custom type rcRemoteMlsQosScheduleMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sp", 1),
          ("wrr", 2))
    )


_RcRemoteMlsQosScheduleMode_Type.__name__ = "Integer32"
_RcRemoteMlsQosScheduleMode_Object = MibTableColumn
rcRemoteMlsQosScheduleMode = _RcRemoteMlsQosScheduleMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 5, 1, 2),
    _RcRemoteMlsQosScheduleMode_Type()
)
rcRemoteMlsQosScheduleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRemoteMlsQosScheduleMode.setStatus("current")


class _RcRemoteMlsQosQueueWeight_Type(Integer32):
    """Custom type rcRemoteMlsQosQueueWeight based on Integer32"""
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
        *(("fourth", 1),
          ("eighth", 2),
          ("sixteen", 3),
          ("other", 4))
    )


_RcRemoteMlsQosQueueWeight_Type.__name__ = "Integer32"
_RcRemoteMlsQosQueueWeight_Object = MibTableColumn
rcRemoteMlsQosQueueWeight = _RcRemoteMlsQosQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 5, 1, 3),
    _RcRemoteMlsQosQueueWeight_Type()
)
rcRemoteMlsQosQueueWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRemoteMlsQosQueueWeight.setStatus("current")
_RcRemoteMlsQosPortPriorityList_Type = PortList
_RcRemoteMlsQosPortPriorityList_Object = MibTableColumn
rcRemoteMlsQosPortPriorityList = _RcRemoteMlsQosPortPriorityList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 5, 1, 4),
    _RcRemoteMlsQosPortPriorityList_Type()
)
rcRemoteMlsQosPortPriorityList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRemoteMlsQosPortPriorityList.setStatus("current")
_RcRemoteConfigNotifications_ObjectIdentity = ObjectIdentity
rcRemoteConfigNotifications = _RcRemoteConfigNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 6)
)
_RcRemotePortConfig_ObjectIdentity = ObjectIdentity
rcRemotePortConfig = _RcRemotePortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2)
)
_RcRemotePortConfigAttriTable_Object = MibTable
rcRemotePortConfigAttriTable = _RcRemotePortConfigAttriTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rcRemotePortConfigAttriTable.setStatus("current")
_RcRemotePortConfigAttriEntry_Object = MibTableRow
rcRemotePortConfigAttriEntry = _RcRemotePortConfigAttriEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 1, 1)
)
rcRemotePortConfigAttriEntry.setIndexNames(
    (0, "RAISECOM-RRCP-VLAN-MIB", "rcRemoteHostMacAddr"),
    (0, "RAISECOM-RRCP-VLAN-MIB", "rcRemotePortIndex"),
)
if mibBuilder.loadTexts:
    rcRemotePortConfigAttriEntry.setStatus("current")
_RcRemotePortAdminStatus_Type = EnableVar
_RcRemotePortAdminStatus_Object = MibTableColumn
rcRemotePortAdminStatus = _RcRemotePortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 1, 1, 1),
    _RcRemotePortAdminStatus_Type()
)
rcRemotePortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRemotePortAdminStatus.setStatus("current")


class _RcRemotePortOperStatus_Type(Integer32):
    """Custom type rcRemotePortOperStatus based on Integer32"""
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


_RcRemotePortOperStatus_Type.__name__ = "Integer32"
_RcRemotePortOperStatus_Object = MibTableColumn
rcRemotePortOperStatus = _RcRemotePortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 1, 1, 2),
    _RcRemotePortOperStatus_Type()
)
rcRemotePortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRemotePortOperStatus.setStatus("current")


class _RcRemotePortDuplexSpeedSet_Type(Integer32):
    """Custom type rcRemotePortDuplexSpeedSet based on Integer32"""
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
        *(("autonegotiate", 1),
          ("half-10", 2),
          ("full-10", 3),
          ("half-100", 4),
          ("full-100", 5))
    )


_RcRemotePortDuplexSpeedSet_Type.__name__ = "Integer32"
_RcRemotePortDuplexSpeedSet_Object = MibTableColumn
rcRemotePortDuplexSpeedSet = _RcRemotePortDuplexSpeedSet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 1, 1, 3),
    _RcRemotePortDuplexSpeedSet_Type()
)
rcRemotePortDuplexSpeedSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRemotePortDuplexSpeedSet.setStatus("current")


class _RcRemotePortDuplexSpeedGet_Type(Integer32):
    """Custom type rcRemotePortDuplexSpeedGet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("half-10", 2),
          ("full-10", 3),
          ("half-100", 4),
          ("full-100", 5),
          ("illegal", 99))
    )


_RcRemotePortDuplexSpeedGet_Type.__name__ = "Integer32"
_RcRemotePortDuplexSpeedGet_Object = MibTableColumn
rcRemotePortDuplexSpeedGet = _RcRemotePortDuplexSpeedGet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 1, 1, 4),
    _RcRemotePortDuplexSpeedGet_Type()
)
rcRemotePortDuplexSpeedGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRemotePortDuplexSpeedGet.setStatus("current")
_RcRemoteManPortFlowControlEnable_Type = EnableVar
_RcRemoteManPortFlowControlEnable_Object = MibTableColumn
rcRemoteManPortFlowControlEnable = _RcRemoteManPortFlowControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 1, 1, 5),
    _RcRemoteManPortFlowControlEnable_Type()
)
rcRemoteManPortFlowControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRemoteManPortFlowControlEnable.setStatus("current")


class _RcRemotePortRxRateLimit_Type(Integer32):
    """Custom type rcRemotePortRxRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(128, 8000),
    )


_RcRemotePortRxRateLimit_Type.__name__ = "Integer32"
_RcRemotePortRxRateLimit_Object = MibTableColumn
rcRemotePortRxRateLimit = _RcRemotePortRxRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 1, 1, 6),
    _RcRemotePortRxRateLimit_Type()
)
rcRemotePortRxRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRemotePortRxRateLimit.setStatus("current")


class _RcRemotePortTxRateLimit_Type(Integer32):
    """Custom type rcRemotePortTxRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(128, 8000),
    )


_RcRemotePortTxRateLimit_Type.__name__ = "Integer32"
_RcRemotePortTxRateLimit_Object = MibTableColumn
rcRemotePortTxRateLimit = _RcRemotePortTxRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 1, 1, 7),
    _RcRemotePortTxRateLimit_Type()
)
rcRemotePortTxRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRemotePortTxRateLimit.setStatus("current")
_RcRemotePortVctTable_Object = MibTable
rcRemotePortVctTable = _RcRemotePortVctTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 2)
)
if mibBuilder.loadTexts:
    rcRemotePortVctTable.setStatus("current")
_RcRemotePortVctEntry_Object = MibTableRow
rcRemotePortVctEntry = _RcRemotePortVctEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 2, 1)
)
rcRemotePortVctEntry.setIndexNames(
    (0, "RAISECOM-RRCP-VLAN-MIB", "rcRemoteHostMacAddr"),
    (0, "RAISECOM-RRCP-VLAN-MIB", "rcRemotePortIndex"),
)
if mibBuilder.loadTexts:
    rcRemotePortVctEntry.setStatus("current")


class _RcRemotePortVCTStart_Type(Integer32):
    """Custom type rcRemotePortVCTStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("started", 1),
          ("stoped", 2))
    )


_RcRemotePortVCTStart_Type.__name__ = "Integer32"
_RcRemotePortVCTStart_Object = MibTableColumn
rcRemotePortVCTStart = _RcRemotePortVCTStart_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 2, 1, 1),
    _RcRemotePortVCTStart_Type()
)
rcRemotePortVCTStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRemotePortVCTStart.setStatus("current")


class _RcRemotePortVctCableTxStatus_Type(Integer32):
    """Custom type rcRemotePortVctCableTxStatus based on Integer32"""
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
        *(("normal", 1),
          ("open", 2),
          ("shorted", 3),
          ("error", 4),
          ("testing", 5))
    )


_RcRemotePortVctCableTxStatus_Type.__name__ = "Integer32"
_RcRemotePortVctCableTxStatus_Object = MibTableColumn
rcRemotePortVctCableTxStatus = _RcRemotePortVctCableTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 2, 1, 2),
    _RcRemotePortVctCableTxStatus_Type()
)
rcRemotePortVctCableTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRemotePortVctCableTxStatus.setStatus("current")


class _RcRemotePortVctCableRxStatus_Type(Integer32):
    """Custom type rcRemotePortVctCableRxStatus based on Integer32"""
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
        *(("normal", 1),
          ("open", 2),
          ("shorted", 3),
          ("error", 4),
          ("testing", 5))
    )


_RcRemotePortVctCableRxStatus_Type.__name__ = "Integer32"
_RcRemotePortVctCableRxStatus_Object = MibTableColumn
rcRemotePortVctCableRxStatus = _RcRemotePortVctCableRxStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 2, 1, 3),
    _RcRemotePortVctCableRxStatus_Type()
)
rcRemotePortVctCableRxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRemotePortVctCableRxStatus.setStatus("current")
_RcRemotePortVctCableTxLength_Type = Unsigned32
_RcRemotePortVctCableTxLength_Object = MibTableColumn
rcRemotePortVctCableTxLength = _RcRemotePortVctCableTxLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 2, 1, 4),
    _RcRemotePortVctCableTxLength_Type()
)
rcRemotePortVctCableTxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRemotePortVctCableTxLength.setStatus("current")
_RcRemotePortVctCableRxLength_Type = Unsigned32
_RcRemotePortVctCableRxLength_Object = MibTableColumn
rcRemotePortVctCableRxLength = _RcRemotePortVctCableRxLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 2, 1, 5),
    _RcRemotePortVctCableRxLength_Type()
)
rcRemotePortVctCableRxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRemotePortVctCableRxLength.setStatus("current")
_RcRemotePortStatisticsTable_Object = MibTable
rcRemotePortStatisticsTable = _RcRemotePortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 3)
)
if mibBuilder.loadTexts:
    rcRemotePortStatisticsTable.setStatus("current")
_RcRemotePortStatisticsEntry_Object = MibTableRow
rcRemotePortStatisticsEntry = _RcRemotePortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 3, 1)
)
rcRemotePortStatisticsEntry.setIndexNames(
    (0, "RAISECOM-RRCP-VLAN-MIB", "rcRemoteHostMacAddr"),
    (0, "RAISECOM-RRCP-VLAN-MIB", "rcRemotePortIndex"),
)
if mibBuilder.loadTexts:
    rcRemotePortStatisticsEntry.setStatus("current")
_RcRemotePortRxOctets_Type = Unsigned32
_RcRemotePortRxOctets_Object = MibTableColumn
rcRemotePortRxOctets = _RcRemotePortRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 3, 1, 1),
    _RcRemotePortRxOctets_Type()
)
rcRemotePortRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRemotePortRxOctets.setStatus("current")
_RcRemotePortTxOctets_Type = Unsigned32
_RcRemotePortTxOctets_Object = MibTableColumn
rcRemotePortTxOctets = _RcRemotePortTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 3, 1, 2),
    _RcRemotePortTxOctets_Type()
)
rcRemotePortTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRemotePortTxOctets.setStatus("current")
_RcRemotePortDropOctets_Type = Unsigned32
_RcRemotePortDropOctets_Object = MibTableColumn
rcRemotePortDropOctets = _RcRemotePortDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 3, 1, 3),
    _RcRemotePortDropOctets_Type()
)
rcRemotePortDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRemotePortDropOctets.setStatus("current")
_RcRemotePortNotifications_ObjectIdentity = ObjectIdentity
rcRemotePortNotifications = _RcRemotePortNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 4)
)

# Managed Objects groups


# Notification objects

rcRemoteConfigWriteResultNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 6, 1)
)
rcRemoteConfigWriteResultNotification.setObjects(
      *(("RAISECOM-RRCP-VLAN-MIB", "rcRemoteHostMacAddr"),
        ("RAISECOM-RRCP-VLAN-MIB", "rcRemoteDeviceCfgWriteResult"))
)
if mibBuilder.loadTexts:
    rcRemoteConfigWriteResultNotification.setStatus(
        "current"
    )

rcRemoteConfigResetFactoryResultNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 1, 6, 2)
)
rcRemoteConfigResetFactoryResultNotification.setObjects(
      *(("RAISECOM-RRCP-VLAN-MIB", "rcRemoteHostMacAddr"),
        ("RAISECOM-RRCP-VLAN-MIB", "rcRemoteDeviceResetFactoryResult"))
)
if mibBuilder.loadTexts:
    rcRemoteConfigResetFactoryResultNotification.setStatus(
        "current"
    )

rcRemotePortUpNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 4, 1)
)
rcRemotePortUpNotification.setObjects(
    ("RAISECOM-RRCP-VLAN-MIB", "rcRemoteManPortOperStatus")
)
if mibBuilder.loadTexts:
    rcRemotePortUpNotification.setStatus(
        "current"
    )

rcRemotePortDownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 2, 2, 4, 2)
)
rcRemotePortDownNotification.setObjects(
    ("RAISECOM-RRCP-VLAN-MIB", "rcRemoteManPortOperStatus")
)
if mibBuilder.loadTexts:
    rcRemotePortDownNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-RRCP-VLAN-MIB",
    **{"rcRrcp": rcRrcp,
       "rcRrcpRemoteManagement": rcRrcpRemoteManagement,
       "rcRemoteVlanConifg": rcRemoteVlanConifg,
       "rcRemoteConfigTable": rcRemoteConfigTable,
       "rcRemoteConfigEntry": rcRemoteConfigEntry,
       "rcRemoteHostMacAddr": rcRemoteHostMacAddr,
       "rcRemoteHostName": rcRemoteHostName,
       "rcRemoteBroadcastStormCtrl": rcRemoteBroadcastStormCtrl,
       "rcRemoteLoopbackDetection": rcRemoteLoopbackDetection,
       "rcRemoteLoopbackDetectionStatus": rcRemoteLoopbackDetectionStatus,
       "rcRemoteDeviceManageVlan": rcRemoteDeviceManageVlan,
       "rcRemoteDeviceCfgWrite": rcRemoteDeviceCfgWrite,
       "rcRemoteDeviceCfgWriteResult": rcRemoteDeviceCfgWriteResult,
       "rcRemoteDeviceResetFactory": rcRemoteDeviceResetFactory,
       "rcRemoteDeviceResetFactoryResult": rcRemoteDeviceResetFactoryResult,
       "rcRemoteDeviceReboot": rcRemoteDeviceReboot,
       "rcRemoteVlanCfgTable": rcRemoteVlanCfgTable,
       "rcRemoteVlanCfgEntry": rcRemoteVlanCfgEntry,
       "rcRemoteSwitchMode": rcRemoteSwitchMode,
       "rcRemotePortBasedVlanUpLinkPort": rcRemotePortBasedVlanUpLinkPort,
       "rcRemoteCurrentVlanTable": rcRemoteCurrentVlanTable,
       "rcRemoteCurrentVlanEntry": rcRemoteCurrentVlanEntry,
       "rcRemoteCurrentVlanIndex": rcRemoteCurrentVlanIndex,
       "rcRemoteCurrentVlanEgressPorts": rcRemoteCurrentVlanEgressPorts,
       "rcRemoteCurrentVlanRowStatus": rcRemoteCurrentVlanRowStatus,
       "rcRemoteVlanPortTable": rcRemoteVlanPortTable,
       "rcRemoteVlanPortEntry": rcRemoteVlanPortEntry,
       "rcRemotePortIndex": rcRemotePortIndex,
       "rcRemotePortMode": rcRemotePortMode,
       "rcRemotePortNativeVid": rcRemotePortNativeVid,
       "rcRemotePortAccessEgressAllowVlan": rcRemotePortAccessEgressAllowVlan,
       "rcRemoteQosCfgTable": rcRemoteQosCfgTable,
       "rcRemoteQosCfgEntry": rcRemoteQosCfgEntry,
       "rcRemoteMlsQosTrustMode": rcRemoteMlsQosTrustMode,
       "rcRemoteMlsQosScheduleMode": rcRemoteMlsQosScheduleMode,
       "rcRemoteMlsQosQueueWeight": rcRemoteMlsQosQueueWeight,
       "rcRemoteMlsQosPortPriorityList": rcRemoteMlsQosPortPriorityList,
       "rcRemoteConfigNotifications": rcRemoteConfigNotifications,
       "rcRemoteConfigWriteResultNotification": rcRemoteConfigWriteResultNotification,
       "rcRemoteConfigResetFactoryResultNotification": rcRemoteConfigResetFactoryResultNotification,
       "rcRemotePortConfig": rcRemotePortConfig,
       "rcRemotePortConfigAttriTable": rcRemotePortConfigAttriTable,
       "rcRemotePortConfigAttriEntry": rcRemotePortConfigAttriEntry,
       "rcRemotePortAdminStatus": rcRemotePortAdminStatus,
       "rcRemotePortOperStatus": rcRemotePortOperStatus,
       "rcRemotePortDuplexSpeedSet": rcRemotePortDuplexSpeedSet,
       "rcRemotePortDuplexSpeedGet": rcRemotePortDuplexSpeedGet,
       "rcRemoteManPortFlowControlEnable": rcRemoteManPortFlowControlEnable,
       "rcRemotePortRxRateLimit": rcRemotePortRxRateLimit,
       "rcRemotePortTxRateLimit": rcRemotePortTxRateLimit,
       "rcRemotePortVctTable": rcRemotePortVctTable,
       "rcRemotePortVctEntry": rcRemotePortVctEntry,
       "rcRemotePortVCTStart": rcRemotePortVCTStart,
       "rcRemotePortVctCableTxStatus": rcRemotePortVctCableTxStatus,
       "rcRemotePortVctCableRxStatus": rcRemotePortVctCableRxStatus,
       "rcRemotePortVctCableTxLength": rcRemotePortVctCableTxLength,
       "rcRemotePortVctCableRxLength": rcRemotePortVctCableRxLength,
       "rcRemotePortStatisticsTable": rcRemotePortStatisticsTable,
       "rcRemotePortStatisticsEntry": rcRemotePortStatisticsEntry,
       "rcRemotePortRxOctets": rcRemotePortRxOctets,
       "rcRemotePortTxOctets": rcRemotePortTxOctets,
       "rcRemotePortDropOctets": rcRemotePortDropOctets,
       "rcRemotePortNotifications": rcRemotePortNotifications,
       "rcRemotePortUpNotification": rcRemotePortUpNotification,
       "rcRemotePortDownNotification": rcRemotePortDownNotification}
)
