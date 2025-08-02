_m='h3cSoftwareInfoString'
_l='h3cExtShutdownVoltageHighThreshold'
_k='h3cExtShutdownVoltageLowThreshold'
_j='h3cExtCriticalVoltageHighThreshold'
_i='h3cExtCriticalVoltageLowThreshold'
_h='h3cAdapterNumber'
_g='h3cBondingIndex'
_f='h3cStorageInterfaceIndex'
_e='h3cDeuIndex'
_d='H3cStorageLedStateType'
_c='h3cRaidRunState'
_b='h3cRaidHideState'
_a='h3cEntityExtShutdownLowerTemperatureThreshold'
_Z='h3cEntityExtOperStatus'
_Y='h3cEntityExtCriticalLowerTemperatureThreshold'
_X='h3cDiskPowerOffReason'
_W='H3C-DISK-MIB'
_V='entPhysicalIndex'
_U='h3cExtVoltageHighThreshold'
_T='h3cExtVoltageLowThreshold'
_S='h3cEntityExtTemperature'
_R='not-accessible'
_Q='h3cEntityExtPhysicalIndex'
_P='entPhysicalName'
_O='entPhysicalDescr'
_N='H3cStorageEnableState'
_M='Integer32'
_L='h3cExtVoltage'
_K='h3cExtVoltagePhysicalName'
_J='ENTITY-MIB'
_I='h3cExtVoltagePhysicalIndex'
_H='H3C-ENTITY-EXT-MIB'
_G='h3cRaidUuid'
_F='h3cRaidName'
_E='read-write'
_D='read-only'
_C='H3C-RAID-MIB'
_B='H3C-STORAGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PhysicalIndex,entPhysicalDescr,entPhysicalIndex,entPhysicalName=mibBuilder.importSymbols(_J,'PhysicalIndex',_O,_V,_P)
h3cDiskPowerOffReason,=mibBuilder.importSymbols(_W,_X)
h3cEntityExtCriticalLowerTemperatureThreshold,h3cEntityExtOperStatus,h3cEntityExtPhysicalIndex,h3cEntityExtShutdownLowerTemperatureThreshold,h3cEntityExtTemperature=mibBuilder.importSymbols(_H,_Y,_Z,_Q,_a,_S)
h3cRaidHideState,h3cRaidName,h3cRaidRunState,h3cRaidUuid=mibBuilder.importSymbols(_C,_b,_F,_c,_G)
H3cSoftwareInfoString,H3cStorageActionType,H3cStorageCapableState,H3cStorageEnableState,H3cStorageLedStateType,H3cWwpnListType,h3cStorageRef=mibBuilder.importSymbols('H3C-STORAGE-REF-MIB','H3cSoftwareInfoString','H3cStorageActionType','H3cStorageCapableState',_N,_d,'H3cWwpnListType','h3cStorageRef')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cStorageMIB=ModuleIdentity((1,3,6,1,4,1,2011,10,10,1))
_H3cStorageMibObjects_ObjectIdentity=ObjectIdentity
h3cStorageMibObjects=_H3cStorageMibObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,10,1,1))
_H3cStorageServerInfo_ObjectIdentity=ObjectIdentity
h3cStorageServerInfo=_H3cStorageServerInfo_ObjectIdentity((1,3,6,1,4,1,2011,10,10,1,1,1))
_H3cStorageServerCapability_ObjectIdentity=ObjectIdentity
h3cStorageServerCapability=_H3cStorageServerCapability_ObjectIdentity((1,3,6,1,4,1,2011,10,10,1,1,1,1))
_H3cRaidCapability_Type=H3cStorageCapableState
_H3cRaidCapability_Object=MibScalar
h3cRaidCapability=_H3cRaidCapability_Object((1,3,6,1,4,1,2011,10,10,1,1,1,1,1),_H3cRaidCapability_Type())
h3cRaidCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRaidCapability.setStatus(_A)
_H3cFcCapability_Type=H3cStorageCapableState
_H3cFcCapability_Object=MibScalar
h3cFcCapability=_H3cFcCapability_Object((1,3,6,1,4,1,2011,10,10,1,1,1,1,2),_H3cFcCapability_Type())
h3cFcCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFcCapability.setStatus(_A)
_H3cNasCapability_Type=H3cStorageCapableState
_H3cNasCapability_Object=MibScalar
h3cNasCapability=_H3cNasCapability_Object((1,3,6,1,4,1,2011,10,10,1,1,1,1,3),_H3cNasCapability_Type())
h3cNasCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cNasCapability.setStatus(_A)
_H3cAdaptiveRepCapability_Type=H3cStorageCapableState
_H3cAdaptiveRepCapability_Object=MibScalar
h3cAdaptiveRepCapability=_H3cAdaptiveRepCapability_Object((1,3,6,1,4,1,2011,10,10,1,1,1,1,4),_H3cAdaptiveRepCapability_Type())
h3cAdaptiveRepCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cAdaptiveRepCapability.setStatus(_A)
_H3cRemoteRepCapability_Type=H3cStorageCapableState
_H3cRemoteRepCapability_Object=MibScalar
h3cRemoteRepCapability=_H3cRemoteRepCapability_Object((1,3,6,1,4,1,2011,10,10,1,1,1,1,5),_H3cRemoteRepCapability_Type())
h3cRemoteRepCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRemoteRepCapability.setStatus(_A)
_H3cSafeCacheCapability_Type=H3cStorageCapableState
_H3cSafeCacheCapability_Object=MibScalar
h3cSafeCacheCapability=_H3cSafeCacheCapability_Object((1,3,6,1,4,1,2011,10,10,1,1,1,1,6),_H3cSafeCacheCapability_Type())
h3cSafeCacheCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSafeCacheCapability.setStatus(_A)
_H3cSyncMirrorCapability_Type=H3cStorageCapableState
_H3cSyncMirrorCapability_Object=MibScalar
h3cSyncMirrorCapability=_H3cSyncMirrorCapability_Object((1,3,6,1,4,1,2011,10,10,1,1,1,1,7),_H3cSyncMirrorCapability_Type())
h3cSyncMirrorCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSyncMirrorCapability.setStatus(_A)
_H3cAsyncMirrorCapability_Type=H3cStorageCapableState
_H3cAsyncMirrorCapability_Object=MibScalar
h3cAsyncMirrorCapability=_H3cAsyncMirrorCapability_Object((1,3,6,1,4,1,2011,10,10,1,1,1,1,8),_H3cAsyncMirrorCapability_Type())
h3cAsyncMirrorCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cAsyncMirrorCapability.setStatus(_A)
_H3cTimeMarkCapability_Type=H3cStorageCapableState
_H3cTimeMarkCapability_Object=MibScalar
h3cTimeMarkCapability=_H3cTimeMarkCapability_Object((1,3,6,1,4,1,2011,10,10,1,1,1,1,9),_H3cTimeMarkCapability_Type())
h3cTimeMarkCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cTimeMarkCapability.setStatus(_A)
_H3cSseCapability_Type=H3cStorageCapableState
_H3cSseCapability_Object=MibScalar
h3cSseCapability=_H3cSseCapability_Object((1,3,6,1,4,1,2011,10,10,1,1,1,1,10),_H3cSseCapability_Type())
h3cSseCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSseCapability.setStatus(_A)
_H3cStorageTargetConfig_ObjectIdentity=ObjectIdentity
h3cStorageTargetConfig=_H3cStorageTargetConfig_ObjectIdentity((1,3,6,1,4,1,2011,10,10,1,1,1,2))
class _H3ciSCSITargetEnable_Type(H3cStorageEnableState):defaultValue=2
_H3ciSCSITargetEnable_Type.__name__=_N
_H3ciSCSITargetEnable_Object=MibScalar
h3ciSCSITargetEnable=_H3ciSCSITargetEnable_Object((1,3,6,1,4,1,2011,10,10,1,1,1,2,1),_H3ciSCSITargetEnable_Type())
h3ciSCSITargetEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3ciSCSITargetEnable.setStatus(_A)
_H3cFcTargetEnable_Type=H3cStorageEnableState
_H3cFcTargetEnable_Object=MibScalar
h3cFcTargetEnable=_H3cFcTargetEnable_Object((1,3,6,1,4,1,2011,10,10,1,1,1,2,2),_H3cFcTargetEnable_Type())
h3cFcTargetEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFcTargetEnable.setStatus(_A)
_H3cStorageServerPhysInfo_ObjectIdentity=ObjectIdentity
h3cStorageServerPhysInfo=_H3cStorageServerPhysInfo_ObjectIdentity((1,3,6,1,4,1,2011,10,10,1,1,1,3))
_H3cServerLocationLedState_Type=H3cStorageLedStateType
_H3cServerLocationLedState_Object=MibScalar
h3cServerLocationLedState=_H3cServerLocationLedState_Object((1,3,6,1,4,1,2011,10,10,1,1,1,3,1),_H3cServerLocationLedState_Type())
h3cServerLocationLedState.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cServerLocationLedState.setStatus(_A)
class _H3cServerResetButtonState_Type(H3cStorageEnableState):defaultValue=1
_H3cServerResetButtonState_Type.__name__=_N
_H3cServerResetButtonState_Object=MibScalar
h3cServerResetButtonState=_H3cServerResetButtonState_Object((1,3,6,1,4,1,2011,10,10,1,1,1,3,2),_H3cServerResetButtonState_Type())
h3cServerResetButtonState.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cServerResetButtonState.setStatus(_A)
class _H3cServerPowerButtonState_Type(H3cStorageEnableState):defaultValue=1
_H3cServerPowerButtonState_Type.__name__=_N
_H3cServerPowerButtonState_Object=MibScalar
h3cServerPowerButtonState=_H3cServerPowerButtonState_Object((1,3,6,1,4,1,2011,10,10,1,1,1,3,3),_H3cServerPowerButtonState_Type())
h3cServerPowerButtonState.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cServerPowerButtonState.setStatus(_A)
class _H3cServerPowerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('online',1),('onlinebypass',2),('onbattery',3),('unknown',4)))
_H3cServerPowerState_Type.__name__=_M
_H3cServerPowerState_Object=MibScalar
h3cServerPowerState=_H3cServerPowerState_Object((1,3,6,1,4,1,2011,10,10,1,1,1,3,4),_H3cServerPowerState_Type())
h3cServerPowerState.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cServerPowerState.setStatus(_A)
_H3cStoragePhysicalInfo_ObjectIdentity=ObjectIdentity
h3cStoragePhysicalInfo=_H3cStoragePhysicalInfo_ObjectIdentity((1,3,6,1,4,1,2011,10,10,1,1,2))
_H3cDeuTable_Object=MibTable
h3cDeuTable=_H3cDeuTable_Object((1,3,6,1,4,1,2011,10,10,1,1,2,1))
if mibBuilder.loadTexts:h3cDeuTable.setStatus(_A)
_H3cDeuEntry_Object=MibTableRow
h3cDeuEntry=_H3cDeuEntry_Object((1,3,6,1,4,1,2011,10,10,1,1,2,1,1))
h3cDeuEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:h3cDeuEntry.setStatus(_A)
_H3cDeuIndex_Type=Integer32
_H3cDeuIndex_Object=MibTableColumn
h3cDeuIndex=_H3cDeuIndex_Object((1,3,6,1,4,1,2011,10,10,1,1,2,1,1,1),_H3cDeuIndex_Type())
h3cDeuIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:h3cDeuIndex.setStatus(_A)
class _H3cDeuIDLed_Type(H3cStorageLedStateType):defaultValue=1
_H3cDeuIDLed_Type.__name__=_d
_H3cDeuIDLed_Object=MibTableColumn
h3cDeuIDLed=_H3cDeuIDLed_Object((1,3,6,1,4,1,2011,10,10,1,1,2,1,1,2),_H3cDeuIDLed_Type())
h3cDeuIDLed.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDeuIDLed.setStatus(_A)
_H3cDeuDiskScan_Type=H3cStorageActionType
_H3cDeuDiskScan_Object=MibTableColumn
h3cDeuDiskScan=_H3cDeuDiskScan_Object((1,3,6,1,4,1,2011,10,10,1,1,2,1,1,3),_H3cDeuDiskScan_Type())
h3cDeuDiskScan.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cDeuDiskScan.setStatus(_A)
_H3cStorageInterfaceTable_Object=MibTable
h3cStorageInterfaceTable=_H3cStorageInterfaceTable_Object((1,3,6,1,4,1,2011,10,10,1,1,2,2))
if mibBuilder.loadTexts:h3cStorageInterfaceTable.setStatus(_A)
_H3cStorageInterfaceEntry_Object=MibTableRow
h3cStorageInterfaceEntry=_H3cStorageInterfaceEntry_Object((1,3,6,1,4,1,2011,10,10,1,1,2,2,1))
h3cStorageInterfaceEntry.setIndexNames((0,_B,_f))
if mibBuilder.loadTexts:h3cStorageInterfaceEntry.setStatus(_A)
_H3cStorageInterfaceIndex_Type=Integer32
_H3cStorageInterfaceIndex_Object=MibTableColumn
h3cStorageInterfaceIndex=_H3cStorageInterfaceIndex_Object((1,3,6,1,4,1,2011,10,10,1,1,2,2,1,1),_H3cStorageInterfaceIndex_Type())
h3cStorageInterfaceIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:h3cStorageInterfaceIndex.setStatus(_A)
_H3cStorageInterfaceGateway_Type=InetAddress
_H3cStorageInterfaceGateway_Object=MibTableColumn
h3cStorageInterfaceGateway=_H3cStorageInterfaceGateway_Object((1,3,6,1,4,1,2011,10,10,1,1,2,2,1,2),_H3cStorageInterfaceGateway_Type())
h3cStorageInterfaceGateway.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cStorageInterfaceGateway.setStatus(_A)
_H3cStorageInterfaceGatewayType_Type=InetAddressType
_H3cStorageInterfaceGatewayType_Object=MibTableColumn
h3cStorageInterfaceGatewayType=_H3cStorageInterfaceGatewayType_Object((1,3,6,1,4,1,2011,10,10,1,1,2,2,1,3),_H3cStorageInterfaceGatewayType_Type())
h3cStorageInterfaceGatewayType.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cStorageInterfaceGatewayType.setStatus(_A)
class _H3cStorageInterfaceMTU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1500,9000)));namedValues=NamedValues(*(('mtu1',1500),('mtu2',9000)))
_H3cStorageInterfaceMTU_Type.__name__=_M
_H3cStorageInterfaceMTU_Object=MibTableColumn
h3cStorageInterfaceMTU=_H3cStorageInterfaceMTU_Object((1,3,6,1,4,1,2011,10,10,1,1,2,2,1,4),_H3cStorageInterfaceMTU_Type())
h3cStorageInterfaceMTU.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cStorageInterfaceMTU.setStatus(_A)
_H3cBondingTable_Object=MibTable
h3cBondingTable=_H3cBondingTable_Object((1,3,6,1,4,1,2011,10,10,1,1,2,3))
if mibBuilder.loadTexts:h3cBondingTable.setStatus(_A)
_H3cBondingEntry_Object=MibTableRow
h3cBondingEntry=_H3cBondingEntry_Object((1,3,6,1,4,1,2011,10,10,1,1,2,3,1))
h3cBondingEntry.setIndexNames((0,_B,_g))
if mibBuilder.loadTexts:h3cBondingEntry.setStatus(_A)
_H3cBondingIndex_Type=Integer32
_H3cBondingIndex_Object=MibTableColumn
h3cBondingIndex=_H3cBondingIndex_Object((1,3,6,1,4,1,2011,10,10,1,1,2,3,1,1),_H3cBondingIndex_Type())
h3cBondingIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:h3cBondingIndex.setStatus(_A)
_H3cBondingPortList_Type=OctetString
_H3cBondingPortList_Object=MibTableColumn
h3cBondingPortList=_H3cBondingPortList_Object((1,3,6,1,4,1,2011,10,10,1,1,2,3,1,2),_H3cBondingPortList_Type())
h3cBondingPortList.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cBondingPortList.setStatus(_A)
_H3cScsiAdapterTable_Object=MibTable
h3cScsiAdapterTable=_H3cScsiAdapterTable_Object((1,3,6,1,4,1,2011,10,10,1,1,2,4))
if mibBuilder.loadTexts:h3cScsiAdapterTable.setStatus(_A)
_H3cScsiAdapterEntry_Object=MibTableRow
h3cScsiAdapterEntry=_H3cScsiAdapterEntry_Object((1,3,6,1,4,1,2011,10,10,1,1,2,4,1))
h3cScsiAdapterEntry.setIndexNames((0,_J,_V),(0,_B,_h))
if mibBuilder.loadTexts:h3cScsiAdapterEntry.setStatus(_A)
_H3cAdapterNumber_Type=Integer32
_H3cAdapterNumber_Object=MibTableColumn
h3cAdapterNumber=_H3cAdapterNumber_Object((1,3,6,1,4,1,2011,10,10,1,1,2,4,1,1),_H3cAdapterNumber_Type())
h3cAdapterNumber.setMaxAccess(_R)
if mibBuilder.loadTexts:h3cAdapterNumber.setStatus(_A)
_H3cAdapterDesc_Type=OctetString
_H3cAdapterDesc_Object=MibTableColumn
h3cAdapterDesc=_H3cAdapterDesc_Object((1,3,6,1,4,1,2011,10,10,1,1,2,4,1,2),_H3cAdapterDesc_Type())
h3cAdapterDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cAdapterDesc.setStatus(_A)
class _H3cAdapterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('scsi',1),('fc',2)))
_H3cAdapterType_Type.__name__=_M
_H3cAdapterType_Object=MibTableColumn
h3cAdapterType=_H3cAdapterType_Object((1,3,6,1,4,1,2011,10,10,1,1,2,4,1,3),_H3cAdapterType_Type())
h3cAdapterType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cAdapterType.setStatus(_A)
class _H3cFcAdapterMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('initiator',1),('target',2),('dual',3)))
_H3cFcAdapterMode_Type.__name__=_M
_H3cFcAdapterMode_Object=MibTableColumn
h3cFcAdapterMode=_H3cFcAdapterMode_Object((1,3,6,1,4,1,2011,10,10,1,1,2,4,1,4),_H3cFcAdapterMode_Type())
h3cFcAdapterMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFcAdapterMode.setStatus(_A)
_H3cFcAdapterInitiatorWwpnName_Type=H3cWwpnListType
_H3cFcAdapterInitiatorWwpnName_Object=MibTableColumn
h3cFcAdapterInitiatorWwpnName=_H3cFcAdapterInitiatorWwpnName_Object((1,3,6,1,4,1,2011,10,10,1,1,2,4,1,5),_H3cFcAdapterInitiatorWwpnName_Type())
h3cFcAdapterInitiatorWwpnName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFcAdapterInitiatorWwpnName.setStatus(_A)
_H3cFcAdapterTargetWwpnName_Type=H3cWwpnListType
_H3cFcAdapterTargetWwpnName_Object=MibTableColumn
h3cFcAdapterTargetWwpnName=_H3cFcAdapterTargetWwpnName_Object((1,3,6,1,4,1,2011,10,10,1,1,2,4,1,6),_H3cFcAdapterTargetWwpnName_Type())
h3cFcAdapterTargetWwpnName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFcAdapterTargetWwpnName.setStatus(_A)
class _H3cFcAdapterPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('linkup',1),('linkdown',2)))
_H3cFcAdapterPortState_Type.__name__=_M
_H3cFcAdapterPortState_Object=MibTableColumn
h3cFcAdapterPortState=_H3cFcAdapterPortState_Object((1,3,6,1,4,1,2011,10,10,1,1,2,4,1,7),_H3cFcAdapterPortState_Type())
h3cFcAdapterPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFcAdapterPortState.setStatus(_A)
class _H3cFcAdapterModeSwitch_Type(H3cStorageEnableState):defaultValue=2
_H3cFcAdapterModeSwitch_Type.__name__=_N
_H3cFcAdapterModeSwitch_Object=MibTableColumn
h3cFcAdapterModeSwitch=_H3cFcAdapterModeSwitch_Object((1,3,6,1,4,1,2011,10,10,1,1,2,4,1,8),_H3cFcAdapterModeSwitch_Type())
h3cFcAdapterModeSwitch.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFcAdapterModeSwitch.setStatus(_A)
_H3cExtVoltageTable_Object=MibTable
h3cExtVoltageTable=_H3cExtVoltageTable_Object((1,3,6,1,4,1,2011,10,10,1,1,2,5))
if mibBuilder.loadTexts:h3cExtVoltageTable.setStatus(_A)
_H3cExtVoltageEntry_Object=MibTableRow
h3cExtVoltageEntry=_H3cExtVoltageEntry_Object((1,3,6,1,4,1,2011,10,10,1,1,2,5,1))
h3cExtVoltageEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:h3cExtVoltageEntry.setStatus(_A)
_H3cExtVoltagePhysicalIndex_Type=PhysicalIndex
_H3cExtVoltagePhysicalIndex_Object=MibTableColumn
h3cExtVoltagePhysicalIndex=_H3cExtVoltagePhysicalIndex_Object((1,3,6,1,4,1,2011,10,10,1,1,2,5,1,1),_H3cExtVoltagePhysicalIndex_Type())
h3cExtVoltagePhysicalIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:h3cExtVoltagePhysicalIndex.setStatus(_A)
_H3cExtVoltagePhysicalName_Type=SnmpAdminString
_H3cExtVoltagePhysicalName_Object=MibTableColumn
h3cExtVoltagePhysicalName=_H3cExtVoltagePhysicalName_Object((1,3,6,1,4,1,2011,10,10,1,1,2,5,1,2),_H3cExtVoltagePhysicalName_Type())
h3cExtVoltagePhysicalName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cExtVoltagePhysicalName.setStatus(_A)
_H3cExtVoltage_Type=Integer32
_H3cExtVoltage_Object=MibTableColumn
h3cExtVoltage=_H3cExtVoltage_Object((1,3,6,1,4,1,2011,10,10,1,1,2,5,1,3),_H3cExtVoltage_Type())
h3cExtVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cExtVoltage.setStatus(_A)
_H3cExtVoltageLowThreshold_Type=Integer32
_H3cExtVoltageLowThreshold_Object=MibTableColumn
h3cExtVoltageLowThreshold=_H3cExtVoltageLowThreshold_Object((1,3,6,1,4,1,2011,10,10,1,1,2,5,1,4),_H3cExtVoltageLowThreshold_Type())
h3cExtVoltageLowThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cExtVoltageLowThreshold.setStatus(_A)
_H3cExtVoltageHighThreshold_Type=Integer32
_H3cExtVoltageHighThreshold_Object=MibTableColumn
h3cExtVoltageHighThreshold=_H3cExtVoltageHighThreshold_Object((1,3,6,1,4,1,2011,10,10,1,1,2,5,1,5),_H3cExtVoltageHighThreshold_Type())
h3cExtVoltageHighThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cExtVoltageHighThreshold.setStatus(_A)
_H3cExtCriticalVoltageLowThreshold_Type=Integer32
_H3cExtCriticalVoltageLowThreshold_Object=MibTableColumn
h3cExtCriticalVoltageLowThreshold=_H3cExtCriticalVoltageLowThreshold_Object((1,3,6,1,4,1,2011,10,10,1,1,2,5,1,6),_H3cExtCriticalVoltageLowThreshold_Type())
h3cExtCriticalVoltageLowThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cExtCriticalVoltageLowThreshold.setStatus(_A)
_H3cExtCriticalVoltageHighThreshold_Type=Integer32
_H3cExtCriticalVoltageHighThreshold_Object=MibTableColumn
h3cExtCriticalVoltageHighThreshold=_H3cExtCriticalVoltageHighThreshold_Object((1,3,6,1,4,1,2011,10,10,1,1,2,5,1,7),_H3cExtCriticalVoltageHighThreshold_Type())
h3cExtCriticalVoltageHighThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cExtCriticalVoltageHighThreshold.setStatus(_A)
_H3cExtShutdownVoltageLowThreshold_Type=Integer32
_H3cExtShutdownVoltageLowThreshold_Object=MibTableColumn
h3cExtShutdownVoltageLowThreshold=_H3cExtShutdownVoltageLowThreshold_Object((1,3,6,1,4,1,2011,10,10,1,1,2,5,1,8),_H3cExtShutdownVoltageLowThreshold_Type())
h3cExtShutdownVoltageLowThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cExtShutdownVoltageLowThreshold.setStatus(_A)
_H3cExtShutdownVoltageHighThreshold_Type=Integer32
_H3cExtShutdownVoltageHighThreshold_Object=MibTableColumn
h3cExtShutdownVoltageHighThreshold=_H3cExtShutdownVoltageHighThreshold_Object((1,3,6,1,4,1,2011,10,10,1,1,2,5,1,9),_H3cExtShutdownVoltageHighThreshold_Type())
h3cExtShutdownVoltageHighThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cExtShutdownVoltageHighThreshold.setStatus(_A)
_H3cStorageTraps_ObjectIdentity=ObjectIdentity
h3cStorageTraps=_H3cStorageTraps_ObjectIdentity((1,3,6,1,4,1,2011,10,10,1,1,3))
_H3cStorageTrapsPrefix_ObjectIdentity=ObjectIdentity
h3cStorageTrapsPrefix=_H3cStorageTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,10,1,1,3,0))
_H3cStorageTrapsObjects_ObjectIdentity=ObjectIdentity
h3cStorageTrapsObjects=_H3cStorageTrapsObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,10,1,1,3,1))
_H3cSoftwareInfoString_Type=H3cSoftwareInfoString
_H3cSoftwareInfoString_Object=MibScalar
h3cSoftwareInfoString=_H3cSoftwareInfoString_Object((1,3,6,1,4,1,2011,10,10,1,1,3,1,1),_H3cSoftwareInfoString_Type())
h3cSoftwareInfoString.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSoftwareInfoString.setStatus(_A)
h3cStorCriticalLowerTemperatureThresholdNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,1))
h3cStorCriticalLowerTemperatureThresholdNotification.setObjects(*((_H,_Q),(_J,_P),(_H,_S),(_H,_Y)))
if mibBuilder.loadTexts:h3cStorCriticalLowerTemperatureThresholdNotification.setStatus(_A)
h3cStorTemperatureTooLow=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,2))
h3cStorTemperatureTooLow.setObjects(*((_H,_Q),(_J,_P),(_H,_S),(_H,_a)))
if mibBuilder.loadTexts:h3cStorTemperatureTooLow.setStatus(_A)
h3cExtVoltageLowThresholdNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,3))
h3cExtVoltageLowThresholdNotification.setObjects(*((_B,_I),(_B,_K),(_B,_L),(_B,_T)))
if mibBuilder.loadTexts:h3cExtVoltageLowThresholdNotification.setStatus(_A)
h3cExtVoltageHighThresholdNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,4))
h3cExtVoltageHighThresholdNotification.setObjects(*((_B,_I),(_B,_K),(_B,_L),(_B,_U)))
if mibBuilder.loadTexts:h3cExtVoltageHighThresholdNotification.setStatus(_A)
h3cExtCriticalVoltageLowThresholdNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,5))
h3cExtCriticalVoltageLowThresholdNotification.setObjects(*((_B,_I),(_B,_K),(_B,_L),(_B,_i)))
if mibBuilder.loadTexts:h3cExtCriticalVoltageLowThresholdNotification.setStatus(_A)
h3cExtCriticalVoltageHighThresholdNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,6))
h3cExtCriticalVoltageHighThresholdNotification.setObjects(*((_B,_I),(_B,_K),(_B,_L),(_B,_j)))
if mibBuilder.loadTexts:h3cExtCriticalVoltageHighThresholdNotification.setStatus(_A)
h3cExtVoltageTooLow=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,7))
h3cExtVoltageTooLow.setObjects(*((_B,_I),(_B,_K),(_B,_L),(_B,_k)))
if mibBuilder.loadTexts:h3cExtVoltageTooLow.setStatus(_A)
h3cExtVoltageTooHigh=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,8))
h3cExtVoltageTooHigh.setObjects(*((_B,_I),(_B,_K),(_B,_L),(_B,_l)))
if mibBuilder.loadTexts:h3cExtVoltageTooHigh.setStatus(_A)
h3cExtBatteryStateNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,9))
h3cExtBatteryStateNotification.setObjects(*((_H,_Q),(_J,_P),(_H,_Z)))
if mibBuilder.loadTexts:h3cExtBatteryStateNotification.setStatus(_A)
h3cDiskIOErrorNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,10))
h3cDiskIOErrorNotification.setObjects((_J,_O))
if mibBuilder.loadTexts:h3cDiskIOErrorNotification.setStatus(_A)
h3cRaidCreateNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,11))
h3cRaidCreateNotification.setObjects(*((_C,_G),(_C,_F)))
if mibBuilder.loadTexts:h3cRaidCreateNotification.setStatus(_A)
h3cRaidDeleteNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,12))
h3cRaidDeleteNotification.setObjects(*((_C,_G),(_C,_F)))
if mibBuilder.loadTexts:h3cRaidDeleteNotification.setStatus(_A)
h3cRaidHideStateNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,13))
h3cRaidHideStateNotification.setObjects(*((_C,_G),(_C,_F),(_C,_b)))
if mibBuilder.loadTexts:h3cRaidHideStateNotification.setStatus(_A)
h3cRaidRunStateNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,14))
h3cRaidRunStateNotification.setObjects(*((_C,_G),(_C,_F),(_C,_c)))
if mibBuilder.loadTexts:h3cRaidRunStateNotification.setStatus(_A)
h3cRaidImportNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,15))
h3cRaidImportNotification.setObjects(*((_C,_G),(_C,_F)))
if mibBuilder.loadTexts:h3cRaidImportNotification.setStatus(_A)
h3cRaidRebuildStartNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,16))
h3cRaidRebuildStartNotification.setObjects(*((_C,_G),(_C,_F)))
if mibBuilder.loadTexts:h3cRaidRebuildStartNotification.setStatus(_A)
h3cRaidRebuildFinishNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,17))
h3cRaidRebuildFinishNotification.setObjects(*((_C,_G),(_C,_F)))
if mibBuilder.loadTexts:h3cRaidRebuildFinishNotification.setStatus(_A)
h3cRaidRebuildPauseNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,18))
h3cRaidRebuildPauseNotification.setObjects(*((_C,_G),(_C,_F)))
if mibBuilder.loadTexts:h3cRaidRebuildPauseNotification.setStatus(_A)
h3cRaidRebuildInterruptNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,19))
h3cRaidRebuildInterruptNotification.setObjects(*((_C,_G),(_C,_F)))
if mibBuilder.loadTexts:h3cRaidRebuildInterruptNotification.setStatus(_A)
h3cSoftwareModuleFailNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,20))
h3cSoftwareModuleFailNotification.setObjects((_B,_m))
if mibBuilder.loadTexts:h3cSoftwareModuleFailNotification.setStatus(_A)
h3cRaidBatteryExpiredNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,21))
if mibBuilder.loadTexts:h3cRaidBatteryExpiredNotification.setStatus(_A)
h3cRaidBatteryWillExpireNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,22))
if mibBuilder.loadTexts:h3cRaidBatteryWillExpireNotification.setStatus(_A)
h3cLvOnlineFailNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,23))
h3cLvOnlineFailNotification.setObjects(*((_C,_G),(_C,_F)))
if mibBuilder.loadTexts:h3cLvOnlineFailNotification.setStatus(_A)
h3cLvOfflineFailNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,24))
h3cLvOfflineFailNotification.setObjects(*((_C,_G),(_C,_F)))
if mibBuilder.loadTexts:h3cLvOfflineFailNotification.setStatus(_A)
h3cRaidRunNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,25))
h3cRaidRunNotification.setObjects(*((_C,_G),(_C,_F)))
if mibBuilder.loadTexts:h3cRaidRunNotification.setStatus(_A)
h3cExtVoltageNormal=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,26))
h3cExtVoltageNormal.setObjects(*((_B,_I),(_B,_K),(_B,_L),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:h3cExtVoltageNormal.setStatus(_A)
h3cDiskPowerOnNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,27))
h3cDiskPowerOnNotification.setObjects((_J,_O))
if mibBuilder.loadTexts:h3cDiskPowerOnNotification.setStatus(_A)
h3cDiskPowerOffNotification=NotificationType((1,3,6,1,4,1,2011,10,10,1,1,3,0,28))
h3cDiskPowerOffNotification.setObjects(*((_J,_O),(_W,_X)))
if mibBuilder.loadTexts:h3cDiskPowerOffNotification.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cStorageMIB':h3cStorageMIB,'h3cStorageMibObjects':h3cStorageMibObjects,'h3cStorageServerInfo':h3cStorageServerInfo,'h3cStorageServerCapability':h3cStorageServerCapability,'h3cRaidCapability':h3cRaidCapability,'h3cFcCapability':h3cFcCapability,'h3cNasCapability':h3cNasCapability,'h3cAdaptiveRepCapability':h3cAdaptiveRepCapability,'h3cRemoteRepCapability':h3cRemoteRepCapability,'h3cSafeCacheCapability':h3cSafeCacheCapability,'h3cSyncMirrorCapability':h3cSyncMirrorCapability,'h3cAsyncMirrorCapability':h3cAsyncMirrorCapability,'h3cTimeMarkCapability':h3cTimeMarkCapability,'h3cSseCapability':h3cSseCapability,'h3cStorageTargetConfig':h3cStorageTargetConfig,'h3ciSCSITargetEnable':h3ciSCSITargetEnable,'h3cFcTargetEnable':h3cFcTargetEnable,'h3cStorageServerPhysInfo':h3cStorageServerPhysInfo,'h3cServerLocationLedState':h3cServerLocationLedState,'h3cServerResetButtonState':h3cServerResetButtonState,'h3cServerPowerButtonState':h3cServerPowerButtonState,'h3cServerPowerState':h3cServerPowerState,'h3cStoragePhysicalInfo':h3cStoragePhysicalInfo,'h3cDeuTable':h3cDeuTable,'h3cDeuEntry':h3cDeuEntry,_e:h3cDeuIndex,'h3cDeuIDLed':h3cDeuIDLed,'h3cDeuDiskScan':h3cDeuDiskScan,'h3cStorageInterfaceTable':h3cStorageInterfaceTable,'h3cStorageInterfaceEntry':h3cStorageInterfaceEntry,_f:h3cStorageInterfaceIndex,'h3cStorageInterfaceGateway':h3cStorageInterfaceGateway,'h3cStorageInterfaceGatewayType':h3cStorageInterfaceGatewayType,'h3cStorageInterfaceMTU':h3cStorageInterfaceMTU,'h3cBondingTable':h3cBondingTable,'h3cBondingEntry':h3cBondingEntry,_g:h3cBondingIndex,'h3cBondingPortList':h3cBondingPortList,'h3cScsiAdapterTable':h3cScsiAdapterTable,'h3cScsiAdapterEntry':h3cScsiAdapterEntry,_h:h3cAdapterNumber,'h3cAdapterDesc':h3cAdapterDesc,'h3cAdapterType':h3cAdapterType,'h3cFcAdapterMode':h3cFcAdapterMode,'h3cFcAdapterInitiatorWwpnName':h3cFcAdapterInitiatorWwpnName,'h3cFcAdapterTargetWwpnName':h3cFcAdapterTargetWwpnName,'h3cFcAdapterPortState':h3cFcAdapterPortState,'h3cFcAdapterModeSwitch':h3cFcAdapterModeSwitch,'h3cExtVoltageTable':h3cExtVoltageTable,'h3cExtVoltageEntry':h3cExtVoltageEntry,_I:h3cExtVoltagePhysicalIndex,_K:h3cExtVoltagePhysicalName,_L:h3cExtVoltage,_T:h3cExtVoltageLowThreshold,_U:h3cExtVoltageHighThreshold,_i:h3cExtCriticalVoltageLowThreshold,_j:h3cExtCriticalVoltageHighThreshold,_k:h3cExtShutdownVoltageLowThreshold,_l:h3cExtShutdownVoltageHighThreshold,'h3cStorageTraps':h3cStorageTraps,'h3cStorageTrapsPrefix':h3cStorageTrapsPrefix,'h3cStorCriticalLowerTemperatureThresholdNotification':h3cStorCriticalLowerTemperatureThresholdNotification,'h3cStorTemperatureTooLow':h3cStorTemperatureTooLow,'h3cExtVoltageLowThresholdNotification':h3cExtVoltageLowThresholdNotification,'h3cExtVoltageHighThresholdNotification':h3cExtVoltageHighThresholdNotification,'h3cExtCriticalVoltageLowThresholdNotification':h3cExtCriticalVoltageLowThresholdNotification,'h3cExtCriticalVoltageHighThresholdNotification':h3cExtCriticalVoltageHighThresholdNotification,'h3cExtVoltageTooLow':h3cExtVoltageTooLow,'h3cExtVoltageTooHigh':h3cExtVoltageTooHigh,'h3cExtBatteryStateNotification':h3cExtBatteryStateNotification,'h3cDiskIOErrorNotification':h3cDiskIOErrorNotification,'h3cRaidCreateNotification':h3cRaidCreateNotification,'h3cRaidDeleteNotification':h3cRaidDeleteNotification,'h3cRaidHideStateNotification':h3cRaidHideStateNotification,'h3cRaidRunStateNotification':h3cRaidRunStateNotification,'h3cRaidImportNotification':h3cRaidImportNotification,'h3cRaidRebuildStartNotification':h3cRaidRebuildStartNotification,'h3cRaidRebuildFinishNotification':h3cRaidRebuildFinishNotification,'h3cRaidRebuildPauseNotification':h3cRaidRebuildPauseNotification,'h3cRaidRebuildInterruptNotification':h3cRaidRebuildInterruptNotification,'h3cSoftwareModuleFailNotification':h3cSoftwareModuleFailNotification,'h3cRaidBatteryExpiredNotification':h3cRaidBatteryExpiredNotification,'h3cRaidBatteryWillExpireNotification':h3cRaidBatteryWillExpireNotification,'h3cLvOnlineFailNotification':h3cLvOnlineFailNotification,'h3cLvOfflineFailNotification':h3cLvOfflineFailNotification,'h3cRaidRunNotification':h3cRaidRunNotification,'h3cExtVoltageNormal':h3cExtVoltageNormal,'h3cDiskPowerOnNotification':h3cDiskPowerOnNotification,'h3cDiskPowerOffNotification':h3cDiskPowerOffNotification,'h3cStorageTrapsObjects':h3cStorageTrapsObjects,_m:h3cSoftwareInfoString})