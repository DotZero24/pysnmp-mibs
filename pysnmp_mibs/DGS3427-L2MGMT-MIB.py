_AH='swL2macNotifyInfo'
_AG='swL2DhcpLocalRelayVLANID'
_AF='swL2VlanIndex'
_AE='swL2IpLimitedMulticastPortIndex'
_AD='swL2TrafficSegPort'
_AC='swL2IGMPSnoopingDataDrivenLearningGrpGrpAddr'
_AB='swL2IGMPSnoopingDataDrivenLearningGrpVID'
_AA='swL2IGMPSnoopingStaticGroupIPaddress'
_A9='swL2IGMPSnoopingStaticGroupVID'
_A8='swIGMPSnoopingGroupSourceAddr'
_A7='swIGMPSnoopingGroupGroupAddr'
_A6='swIGMPSnoopingGroupVid'
_A5='swL2IGMPMulticastVlanGroupToIp'
_A4='swL2IGMPMulticastVlanGroupFromIp'
_A3='swL2IGMPMulticastVlanGroupVid'
_A2='swL2IGMPMulticastVlanid'
_A1='swL2IGMPRouterPortsVid'
_A0='swL2IGMPGroupIpAddr'
_z='swL2IGMPVid'
_y='swL2IGMPInfoVid'
_x='swL2IGMPCtrlVid'
_w='not-accessible'
_v='swL2MirrorGroupID'
_u='swL2TrunkVLANPort'
_t='swL2TrunkLACPPortIndex'
_s='swL2TrunkIndex'
_r='swL2PortSecurityPortIndex'
_q='swQosDscpMapGlobalCtrlDscpIndex'
_p='swQosDscpTrustPortCtrlPortIndex'
_o='swCosBandwidthClassID'
_n='swCosBandwidthPort'
_m='swL2QOS8021pDefaultPriorityIndex'
_l='swL2QOS8021pUserPriorityIndex'
_k='swL2QOSSchedulingClassID'
_j='swL2QOSSchedulingPort'
_i='swL2QOSBandwidthPortIndex'
_h='swL2PortSfpInfoPortIndex'
_g='swL2PortStatisPortIndex'
_f='swL2PortDropCounterPortIndex'
_e='swL2PortAutoNegInfoPortIndex'
_d='swL2PortCounterCtrlPortIndex'
_c='swL2PortCtrlMediumType'
_b='swL2PortCtrlPortIndex'
_a='copper'
_Z='swL2PortInfoMediumType'
_Y='swL2PortInfoPortIndex'
_X='swL2MultiFilterVid'
_W='active'
_V='normal'
_U='swDevModuleInfoModuleID'
_T='swDevModuleInfoUnitID'
_S='swL2VlanLoopDetectVID'
_R='disable'
_Q='enable'
_P='weightfair'
_O='strict'
_N='start'
_M='OctetString'
_L='none'
_K='swL2LoopDetectPortIndex'
_J='read-create'
_I='DisplayString'
_H='other'
_G='enabled'
_F='disabled'
_E='DGS3427-L2MGMT-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AgentNotifyLevel,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','AgentNotifyLevel')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','TextualConvention')
dgs3427,=mibBuilder.importSymbols('SW34XXPRIMGMT-MIB','dgs3427')
swL2MgmtMIB=ModuleIdentity((1,3,6,1,4,1,171,11,70,2,2))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class VlanId(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class PortList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
class IANAifMauAutoNegCapBits(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('bOther',0),('b10baseT',1),('b10baseTFD',2),('b100baseT4',3),('b100baseTX',4),('b100baseTXFD',5),('b100baseT2',6),('b100baseT2FD',7),('bFdxPause',8),('bFdxAPause',9),('bFdxSPause',10),('bFdxBPause',11),('b1000baseX',12),('b1000baseXFD',13),('b1000baseT',14),('b1000baseTFD',15)))
_SwL2DevMgmt_ObjectIdentity=ObjectIdentity
swL2DevMgmt=_SwL2DevMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,1))
_SwL2DevInfo_ObjectIdentity=ObjectIdentity
swL2DevInfo=_SwL2DevInfo_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,1,1))
class _SwDevInfoTotalNumOfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwDevInfoTotalNumOfPort_Type.__name__=_B
_SwDevInfoTotalNumOfPort_Object=MibScalar
swDevInfoTotalNumOfPort=_SwDevInfoTotalNumOfPort_Object((1,3,6,1,4,1,171,11,70,2,2,1,1,1),_SwDevInfoTotalNumOfPort_Type())
swDevInfoTotalNumOfPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swDevInfoTotalNumOfPort.setStatus(_A)
class _SwDevInfoNumOfPortInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwDevInfoNumOfPortInUse_Type.__name__=_B
_SwDevInfoNumOfPortInUse_Object=MibScalar
swDevInfoNumOfPortInUse=_SwDevInfoNumOfPortInUse_Object((1,3,6,1,4,1,171,11,70,2,2,1,1,2),_SwDevInfoNumOfPortInUse_Type())
swDevInfoNumOfPortInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:swDevInfoNumOfPortInUse.setStatus(_A)
_SwDevModuleInfoTable_Object=MibTable
swDevModuleInfoTable=_SwDevModuleInfoTable_Object((1,3,6,1,4,1,171,11,70,2,2,1,1,3))
if mibBuilder.loadTexts:swDevModuleInfoTable.setStatus(_A)
_SwDevModuleInfoEntry_Object=MibTableRow
swDevModuleInfoEntry=_SwDevModuleInfoEntry_Object((1,3,6,1,4,1,171,11,70,2,2,1,1,3,1))
swDevModuleInfoEntry.setIndexNames((0,_E,_T),(0,_E,_U))
if mibBuilder.loadTexts:swDevModuleInfoEntry.setStatus(_A)
class _SwDevModuleInfoUnitID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_SwDevModuleInfoUnitID_Type.__name__=_B
_SwDevModuleInfoUnitID_Object=MibTableColumn
swDevModuleInfoUnitID=_SwDevModuleInfoUnitID_Object((1,3,6,1,4,1,171,11,70,2,2,1,1,3,1,1),_SwDevModuleInfoUnitID_Type())
swDevModuleInfoUnitID.setMaxAccess(_C)
if mibBuilder.loadTexts:swDevModuleInfoUnitID.setStatus(_A)
class _SwDevModuleInfoModuleID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_SwDevModuleInfoModuleID_Type.__name__=_B
_SwDevModuleInfoModuleID_Object=MibTableColumn
swDevModuleInfoModuleID=_SwDevModuleInfoModuleID_Object((1,3,6,1,4,1,171,11,70,2,2,1,1,3,1,2),_SwDevModuleInfoModuleID_Type())
swDevModuleInfoModuleID.setMaxAccess(_C)
if mibBuilder.loadTexts:swDevModuleInfoModuleID.setStatus(_A)
class _SwDevModuleInfoModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_SwDevModuleInfoModuleName_Type.__name__=_I
_SwDevModuleInfoModuleName_Object=MibTableColumn
swDevModuleInfoModuleName=_SwDevModuleInfoModuleName_Object((1,3,6,1,4,1,171,11,70,2,2,1,1,3,1,3),_SwDevModuleInfoModuleName_Type())
swDevModuleInfoModuleName.setMaxAccess(_C)
if mibBuilder.loadTexts:swDevModuleInfoModuleName.setStatus(_A)
class _SwDevModuleInfoReversion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_SwDevModuleInfoReversion_Type.__name__=_I
_SwDevModuleInfoReversion_Object=MibTableColumn
swDevModuleInfoReversion=_SwDevModuleInfoReversion_Object((1,3,6,1,4,1,171,11,70,2,2,1,1,3,1,4),_SwDevModuleInfoReversion_Type())
swDevModuleInfoReversion.setMaxAccess(_C)
if mibBuilder.loadTexts:swDevModuleInfoReversion.setStatus(_A)
class _SwDevModuleInfoSerial_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_SwDevModuleInfoSerial_Type.__name__=_I
_SwDevModuleInfoSerial_Object=MibTableColumn
swDevModuleInfoSerial=_SwDevModuleInfoSerial_Object((1,3,6,1,4,1,171,11,70,2,2,1,1,3,1,5),_SwDevModuleInfoSerial_Type())
swDevModuleInfoSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:swDevModuleInfoSerial.setStatus(_A)
class _SwDevModuleInfoDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwDevModuleInfoDescription_Type.__name__=_I
_SwDevModuleInfoDescription_Object=MibTableColumn
swDevModuleInfoDescription=_SwDevModuleInfoDescription_Object((1,3,6,1,4,1,171,11,70,2,2,1,1,3,1,6),_SwDevModuleInfoDescription_Type())
swDevModuleInfoDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:swDevModuleInfoDescription.setStatus(_A)
class _SwDevInfoBootPromVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwDevInfoBootPromVersion_Type.__name__=_I
_SwDevInfoBootPromVersion_Object=MibScalar
swDevInfoBootPromVersion=_SwDevInfoBootPromVersion_Object((1,3,6,1,4,1,171,11,70,2,2,1,1,4),_SwDevInfoBootPromVersion_Type())
swDevInfoBootPromVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:swDevInfoBootPromVersion.setStatus(_A)
class _SwDevInfoFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwDevInfoFirmwareVersion_Type.__name__=_I
_SwDevInfoFirmwareVersion_Object=MibScalar
swDevInfoFirmwareVersion=_SwDevInfoFirmwareVersion_Object((1,3,6,1,4,1,171,11,70,2,2,1,1,5),_SwDevInfoFirmwareVersion_Type())
swDevInfoFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:swDevInfoFirmwareVersion.setStatus(_A)
class _SwDevInfoFrontPanelLedStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwDevInfoFrontPanelLedStatus_Type.__name__=_M
_SwDevInfoFrontPanelLedStatus_Object=MibScalar
swDevInfoFrontPanelLedStatus=_SwDevInfoFrontPanelLedStatus_Object((1,3,6,1,4,1,171,11,70,2,2,1,1,6),_SwDevInfoFrontPanelLedStatus_Type())
swDevInfoFrontPanelLedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swDevInfoFrontPanelLedStatus.setStatus(_A)
_SwL2DevCtrl_ObjectIdentity=ObjectIdentity
swL2DevCtrl=_SwL2DevCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,1,2))
class _SwL2DevCtrlStpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2DevCtrlStpState_Type.__name__=_B
_SwL2DevCtrlStpState_Object=MibScalar
swL2DevCtrlStpState=_SwL2DevCtrlStpState_Object((1,3,6,1,4,1,171,11,70,2,2,1,2,1),_SwL2DevCtrlStpState_Type())
swL2DevCtrlStpState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlStpState.setStatus(_A)
class _SwL2DevCtrlIGMPSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2DevCtrlIGMPSnooping_Type.__name__=_B
_SwL2DevCtrlIGMPSnooping_Object=MibScalar
swL2DevCtrlIGMPSnooping=_SwL2DevCtrlIGMPSnooping_Object((1,3,6,1,4,1,171,11,70,2,2,1,2,2),_SwL2DevCtrlIGMPSnooping_Type())
swL2DevCtrlIGMPSnooping.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlIGMPSnooping.setStatus(_A)
class _SwL2DevCtrlIGMPSnoopingMcstRTOnly_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2DevCtrlIGMPSnoopingMcstRTOnly_Type.__name__=_B
_SwL2DevCtrlIGMPSnoopingMcstRTOnly_Object=MibScalar
swL2DevCtrlIGMPSnoopingMcstRTOnly=_SwL2DevCtrlIGMPSnoopingMcstRTOnly_Object((1,3,6,1,4,1,171,11,70,2,2,1,2,3),_SwL2DevCtrlIGMPSnoopingMcstRTOnly_Type())
swL2DevCtrlIGMPSnoopingMcstRTOnly.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlIGMPSnoopingMcstRTOnly.setStatus(_A)
class _SwL2DevCtrlRmonState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2DevCtrlRmonState_Type.__name__=_B
_SwL2DevCtrlRmonState_Object=MibScalar
swL2DevCtrlRmonState=_SwL2DevCtrlRmonState_Object((1,3,6,1,4,1,171,11,70,2,2,1,2,4),_SwL2DevCtrlRmonState_Type())
swL2DevCtrlRmonState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlRmonState.setStatus(_A)
class _SwL2DevCtrlCleanAllStatisticCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_W,2)))
_SwL2DevCtrlCleanAllStatisticCounter_Type.__name__=_B
_SwL2DevCtrlCleanAllStatisticCounter_Object=MibScalar
swL2DevCtrlCleanAllStatisticCounter=_SwL2DevCtrlCleanAllStatisticCounter_Object((1,3,6,1,4,1,171,11,70,2,2,1,2,5),_SwL2DevCtrlCleanAllStatisticCounter_Type())
swL2DevCtrlCleanAllStatisticCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlCleanAllStatisticCounter.setStatus(_A)
_SwL2DevCtrlVlanIdOfFDBTbl_Type=VlanId
_SwL2DevCtrlVlanIdOfFDBTbl_Object=MibScalar
swL2DevCtrlVlanIdOfFDBTbl=_SwL2DevCtrlVlanIdOfFDBTbl_Object((1,3,6,1,4,1,171,11,70,2,2,1,2,6),_SwL2DevCtrlVlanIdOfFDBTbl_Type())
swL2DevCtrlVlanIdOfFDBTbl.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlVlanIdOfFDBTbl.setStatus(_A)
_SwL2DevCtrlManagementVlanId_Type=VlanId
_SwL2DevCtrlManagementVlanId_Object=MibScalar
swL2DevCtrlManagementVlanId=_SwL2DevCtrlManagementVlanId_Object((1,3,6,1,4,1,171,11,70,2,2,1,2,7),_SwL2DevCtrlManagementVlanId_Type())
swL2DevCtrlManagementVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlManagementVlanId.setStatus(_A)
class _SwL2MACNotifyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2MACNotifyState_Type.__name__=_B
_SwL2MACNotifyState_Object=MibScalar
swL2MACNotifyState=_SwL2MACNotifyState_Object((1,3,6,1,4,1,171,11,70,2,2,1,2,8),_SwL2MACNotifyState_Type())
swL2MACNotifyState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MACNotifyState.setStatus(_A)
class _SwL2MACNotifyHistorySize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,500))
_SwL2MACNotifyHistorySize_Type.__name__=_B
_SwL2MACNotifyHistorySize_Object=MibScalar
swL2MACNotifyHistorySize=_SwL2MACNotifyHistorySize_Object((1,3,6,1,4,1,171,11,70,2,2,1,2,9),_SwL2MACNotifyHistorySize_Type())
swL2MACNotifyHistorySize.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MACNotifyHistorySize.setStatus(_A)
class _SwL2MACNotifyInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SwL2MACNotifyInterval_Type.__name__=_B
_SwL2MACNotifyInterval_Object=MibScalar
swL2MACNotifyInterval=_SwL2MACNotifyInterval_Object((1,3,6,1,4,1,171,11,70,2,2,1,2,10),_SwL2MACNotifyInterval_Type())
swL2MACNotifyInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MACNotifyInterval.setStatus(_A)
_SwL2DevCtrlWeb_ObjectIdentity=ObjectIdentity
swL2DevCtrlWeb=_SwL2DevCtrlWeb_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,1,2,13))
class _SwL2DevCtrlWebState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2DevCtrlWebState_Type.__name__=_B
_SwL2DevCtrlWebState_Object=MibScalar
swL2DevCtrlWebState=_SwL2DevCtrlWebState_Object((1,3,6,1,4,1,171,11,70,2,2,1,2,13,1),_SwL2DevCtrlWebState_Type())
swL2DevCtrlWebState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlWebState.setStatus(_A)
class _SwL2DevCtrlWebTcpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2DevCtrlWebTcpPort_Type.__name__=_B
_SwL2DevCtrlWebTcpPort_Object=MibScalar
swL2DevCtrlWebTcpPort=_SwL2DevCtrlWebTcpPort_Object((1,3,6,1,4,1,171,11,70,2,2,1,2,13,2),_SwL2DevCtrlWebTcpPort_Type())
swL2DevCtrlWebTcpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlWebTcpPort.setStatus(_A)
_SwL2DevCtrlTelnet_ObjectIdentity=ObjectIdentity
swL2DevCtrlTelnet=_SwL2DevCtrlTelnet_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,1,2,14))
class _SwL2DevCtrlTelnetState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2DevCtrlTelnetState_Type.__name__=_B
_SwL2DevCtrlTelnetState_Object=MibScalar
swL2DevCtrlTelnetState=_SwL2DevCtrlTelnetState_Object((1,3,6,1,4,1,171,11,70,2,2,1,2,14,1),_SwL2DevCtrlTelnetState_Type())
swL2DevCtrlTelnetState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlTelnetState.setStatus(_A)
class _SwL2DevCtrlTelnetTcpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2DevCtrlTelnetTcpPort_Type.__name__=_B
_SwL2DevCtrlTelnetTcpPort_Object=MibScalar
swL2DevCtrlTelnetTcpPort=_SwL2DevCtrlTelnetTcpPort_Object((1,3,6,1,4,1,171,11,70,2,2,1,2,14,2),_SwL2DevCtrlTelnetTcpPort_Type())
swL2DevCtrlTelnetTcpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlTelnetTcpPort.setStatus(_A)
class _SwL2DevCtrlIpAutoconfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2DevCtrlIpAutoconfig_Type.__name__=_B
_SwL2DevCtrlIpAutoconfig_Object=MibScalar
swL2DevCtrlIpAutoconfig=_SwL2DevCtrlIpAutoconfig_Object((1,3,6,1,4,1,171,11,70,2,2,1,2,15),_SwL2DevCtrlIpAutoconfig_Type())
swL2DevCtrlIpAutoconfig.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlIpAutoconfig.setStatus(_A)
class _SwL2DevCtrlClipagingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2DevCtrlClipagingState_Type.__name__=_B
_SwL2DevCtrlClipagingState_Object=MibScalar
swL2DevCtrlClipagingState=_SwL2DevCtrlClipagingState_Object((1,3,6,1,4,1,171,11,70,2,2,1,2,17),_SwL2DevCtrlClipagingState_Type())
swL2DevCtrlClipagingState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlClipagingState.setStatus(_A)
class _SwL2DevCtrlLLDPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2DevCtrlLLDPState_Type.__name__=_B
_SwL2DevCtrlLLDPState_Object=MibScalar
swL2DevCtrlLLDPState=_SwL2DevCtrlLLDPState_Object((1,3,6,1,4,1,171,11,70,2,2,1,2,18),_SwL2DevCtrlLLDPState_Type())
swL2DevCtrlLLDPState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlLLDPState.setStatus(_A)
class _SwL2DevCtrlLLDPForwardMessageState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2DevCtrlLLDPForwardMessageState_Type.__name__=_B
_SwL2DevCtrlLLDPForwardMessageState_Object=MibScalar
swL2DevCtrlLLDPForwardMessageState=_SwL2DevCtrlLLDPForwardMessageState_Object((1,3,6,1,4,1,171,11,70,2,2,1,2,19),_SwL2DevCtrlLLDPForwardMessageState_Type())
swL2DevCtrlLLDPForwardMessageState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlLLDPForwardMessageState.setStatus(_A)
class _SwL2DevCtrlVLANTrunkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2DevCtrlVLANTrunkState_Type.__name__=_B
_SwL2DevCtrlVLANTrunkState_Object=MibScalar
swL2DevCtrlVLANTrunkState=_SwL2DevCtrlVLANTrunkState_Object((1,3,6,1,4,1,171,11,70,2,2,1,2,22),_SwL2DevCtrlVLANTrunkState_Type())
swL2DevCtrlVLANTrunkState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlVLANTrunkState.setStatus(_A)
class _SwL2DevCtrlIGMPSnoopingMaxDataDrivenLearningCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2DevCtrlIGMPSnoopingMaxDataDrivenLearningCount_Type.__name__=_B
_SwL2DevCtrlIGMPSnoopingMaxDataDrivenLearningCount_Object=MibScalar
swL2DevCtrlIGMPSnoopingMaxDataDrivenLearningCount=_SwL2DevCtrlIGMPSnoopingMaxDataDrivenLearningCount_Object((1,3,6,1,4,1,171,11,70,2,2,1,2,23),_SwL2DevCtrlIGMPSnoopingMaxDataDrivenLearningCount_Type())
swL2DevCtrlIGMPSnoopingMaxDataDrivenLearningCount.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevCtrlIGMPSnoopingMaxDataDrivenLearningCount.setStatus(_A)
_SwL2DevAlarm_ObjectIdentity=ObjectIdentity
swL2DevAlarm=_SwL2DevAlarm_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,1,3))
class _SwL2DevAlarmNewRoot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_SwL2DevAlarmNewRoot_Type.__name__=_B
_SwL2DevAlarmNewRoot_Object=MibScalar
swL2DevAlarmNewRoot=_SwL2DevAlarmNewRoot_Object((1,3,6,1,4,1,171,11,70,2,2,1,3,1),_SwL2DevAlarmNewRoot_Type())
swL2DevAlarmNewRoot.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevAlarmNewRoot.setStatus(_A)
class _SwL2DevAlarmTopologyChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_SwL2DevAlarmTopologyChange_Type.__name__=_B
_SwL2DevAlarmTopologyChange_Object=MibScalar
swL2DevAlarmTopologyChange=_SwL2DevAlarmTopologyChange_Object((1,3,6,1,4,1,171,11,70,2,2,1,3,2),_SwL2DevAlarmTopologyChange_Type())
swL2DevAlarmTopologyChange.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevAlarmTopologyChange.setStatus(_A)
class _SwL2DevAlarmLinkChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_SwL2DevAlarmLinkChange_Type.__name__=_B
_SwL2DevAlarmLinkChange_Object=MibScalar
swL2DevAlarmLinkChange=_SwL2DevAlarmLinkChange_Object((1,3,6,1,4,1,171,11,70,2,2,1,3,3),_SwL2DevAlarmLinkChange_Type())
swL2DevAlarmLinkChange.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevAlarmLinkChange.setStatus(_A)
_SwL2MultiFilter_ObjectIdentity=ObjectIdentity
swL2MultiFilter=_SwL2MultiFilter_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,2))
_SwL2MultiFilterTable_Object=MibTable
swL2MultiFilterTable=_SwL2MultiFilterTable_Object((1,3,6,1,4,1,171,11,70,2,2,2,1))
if mibBuilder.loadTexts:swL2MultiFilterTable.setStatus(_A)
_SwL2MultiFilterEntry_Object=MibTableRow
swL2MultiFilterEntry=_SwL2MultiFilterEntry_Object((1,3,6,1,4,1,171,11,70,2,2,2,1,1))
swL2MultiFilterEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:swL2MultiFilterEntry.setStatus(_A)
class _SwL2MultiFilterVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2MultiFilterVid_Type.__name__=_B
_SwL2MultiFilterVid_Object=MibTableColumn
swL2MultiFilterVid=_SwL2MultiFilterVid_Object((1,3,6,1,4,1,171,11,70,2,2,2,1,1,1),_SwL2MultiFilterVid_Type())
swL2MultiFilterVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MultiFilterVid.setStatus(_A)
class _SwL2MultiFilterMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('forward-all-groups',1),('forward-unregistered-groups',2),('filter-unregistered-groups',3)))
_SwL2MultiFilterMode_Type.__name__=_B
_SwL2MultiFilterMode_Object=MibTableColumn
swL2MultiFilterMode=_SwL2MultiFilterMode_Object((1,3,6,1,4,1,171,11,70,2,2,2,1,1,2),_SwL2MultiFilterMode_Type())
swL2MultiFilterMode.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MultiFilterMode.setStatus(_A)
_SwL2PortMgmt_ObjectIdentity=ObjectIdentity
swL2PortMgmt=_SwL2PortMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,3))
_SwL2PortInfoTable_Object=MibTable
swL2PortInfoTable=_SwL2PortInfoTable_Object((1,3,6,1,4,1,171,11,70,2,2,3,1))
if mibBuilder.loadTexts:swL2PortInfoTable.setStatus(_A)
_SwL2PortInfoEntry_Object=MibTableRow
swL2PortInfoEntry=_SwL2PortInfoEntry_Object((1,3,6,1,4,1,171,11,70,2,2,3,1,1))
swL2PortInfoEntry.setIndexNames((0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:swL2PortInfoEntry.setStatus(_A)
class _SwL2PortInfoPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortInfoPortIndex_Type.__name__=_B
_SwL2PortInfoPortIndex_Object=MibTableColumn
swL2PortInfoPortIndex=_SwL2PortInfoPortIndex_Object((1,3,6,1,4,1,171,11,70,2,2,3,1,1,1),_SwL2PortInfoPortIndex_Type())
swL2PortInfoPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortInfoPortIndex.setStatus(_A)
class _SwL2PortInfoMediumType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),('fiber',2)))
_SwL2PortInfoMediumType_Type.__name__=_B
_SwL2PortInfoMediumType_Object=MibTableColumn
swL2PortInfoMediumType=_SwL2PortInfoMediumType_Object((1,3,6,1,4,1,171,11,70,2,2,3,1,1,2),_SwL2PortInfoMediumType_Type())
swL2PortInfoMediumType.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortInfoMediumType.setStatus(_A)
class _SwL2PortInfoUnitID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortInfoUnitID_Type.__name__=_B
_SwL2PortInfoUnitID_Object=MibTableColumn
swL2PortInfoUnitID=_SwL2PortInfoUnitID_Object((1,3,6,1,4,1,171,11,70,2,2,3,1,1,3),_SwL2PortInfoUnitID_Type())
swL2PortInfoUnitID.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortInfoUnitID.setStatus(_A)
class _SwL2PortInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('portType-none',0),('portType-100Base-T',2),('portType-100Base-X',3),('portType-1000Base-T',4),('portType-1000Base-X',5),('portType-10GBase-R',6),('portType-10GBase-CX4',7),('portType-SIO',8),('portType-module-empty',9),('portType-user-last',10)))
_SwL2PortInfoType_Type.__name__=_B
_SwL2PortInfoType_Object=MibTableColumn
swL2PortInfoType=_SwL2PortInfoType_Object((1,3,6,1,4,1,171,11,70,2,2,3,1,1,4),_SwL2PortInfoType_Type())
swL2PortInfoType.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortInfoType.setStatus(_A)
class _SwL2PortInfoLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('link-pass',2),('link-fail',3)))
_SwL2PortInfoLinkStatus_Type.__name__=_B
_SwL2PortInfoLinkStatus_Object=MibTableColumn
swL2PortInfoLinkStatus=_SwL2PortInfoLinkStatus_Object((1,3,6,1,4,1,171,11,70,2,2,3,1,1,5),_SwL2PortInfoLinkStatus_Type())
swL2PortInfoLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortInfoLinkStatus.setStatus(_A)
class _SwL2PortInfoNwayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*(('link-down',0),('full-10Mbps-8023x',1),('full-10Mbps-none',2),('half-10Mbps-backp',3),('half-10Mbps-none',4),('full-100Mbps-8023x',5),('full-100Mbps-none',6),('half-100Mbps-backp',7),('half-100Mbps-none',8),('full-1Gigabps-8023x',9),('full-1Gigabps-none',10),('half-1Gigabps-backp',11),('half-1Gigabps-none',12),('full-10Gigabps-8023x',13),('full-10Gigabps-none',14),('half-10Gigabps-8023x',15),('half-10Gigabps-none',16),('empty',17),('err-disabled',18)))
_SwL2PortInfoNwayStatus_Type.__name__=_B
_SwL2PortInfoNwayStatus_Object=MibTableColumn
swL2PortInfoNwayStatus=_SwL2PortInfoNwayStatus_Object((1,3,6,1,4,1,171,11,70,2,2,3,1,1,6),_SwL2PortInfoNwayStatus_Type())
swL2PortInfoNwayStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortInfoNwayStatus.setStatus(_A)
class _SwL2PortInfoErrDisReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('err-none',1),('storm-control',2),('lbd-control',3),('ddm-control',4),('bpdu-protection',5),('unidirectional',6)))
_SwL2PortInfoErrDisReason_Type.__name__=_B
_SwL2PortInfoErrDisReason_Object=MibTableColumn
swL2PortInfoErrDisReason=_SwL2PortInfoErrDisReason_Object((1,3,6,1,4,1,171,11,70,2,2,3,1,1,7),_SwL2PortInfoErrDisReason_Type())
swL2PortInfoErrDisReason.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortInfoErrDisReason.setStatus(_A)
_SwL2PortCtrlTable_Object=MibTable
swL2PortCtrlTable=_SwL2PortCtrlTable_Object((1,3,6,1,4,1,171,11,70,2,2,3,2))
if mibBuilder.loadTexts:swL2PortCtrlTable.setStatus(_A)
_SwL2PortCtrlEntry_Object=MibTableRow
swL2PortCtrlEntry=_SwL2PortCtrlEntry_Object((1,3,6,1,4,1,171,11,70,2,2,3,2,1))
swL2PortCtrlEntry.setIndexNames((0,_E,_b),(0,_E,_c))
if mibBuilder.loadTexts:swL2PortCtrlEntry.setStatus(_A)
class _SwL2PortCtrlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortCtrlPortIndex_Type.__name__=_B
_SwL2PortCtrlPortIndex_Object=MibTableColumn
swL2PortCtrlPortIndex=_SwL2PortCtrlPortIndex_Object((1,3,6,1,4,1,171,11,70,2,2,3,2,1,1),_SwL2PortCtrlPortIndex_Type())
swL2PortCtrlPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlPortIndex.setStatus(_A)
class _SwL2PortCtrlMediumType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),('fiber',2)))
_SwL2PortCtrlMediumType_Type.__name__=_B
_SwL2PortCtrlMediumType_Object=MibTableColumn
swL2PortCtrlMediumType=_SwL2PortCtrlMediumType_Object((1,3,6,1,4,1,171,11,70,2,2,3,2,1,2),_SwL2PortCtrlMediumType_Type())
swL2PortCtrlMediumType.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlMediumType.setStatus(_A)
class _SwL2PortCtrlUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortCtrlUnitIndex_Type.__name__=_B
_SwL2PortCtrlUnitIndex_Object=MibTableColumn
swL2PortCtrlUnitIndex=_SwL2PortCtrlUnitIndex_Object((1,3,6,1,4,1,171,11,70,2,2,3,2,1,3),_SwL2PortCtrlUnitIndex_Type())
swL2PortCtrlUnitIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlUnitIndex.setStatus(_A)
class _SwL2PortCtrlAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2PortCtrlAdminState_Type.__name__=_B
_SwL2PortCtrlAdminState_Object=MibTableColumn
swL2PortCtrlAdminState=_SwL2PortCtrlAdminState_Object((1,3,6,1,4,1,171,11,70,2,2,3,2,1,4),_SwL2PortCtrlAdminState_Type())
swL2PortCtrlAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlAdminState.setStatus(_A)
class _SwL2PortCtrlNwayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,8,9,10)));namedValues=NamedValues(*((_H,1),('nway-enabled',2),('nway-disabled-10Mbps-Half',3),('nway-disabled-10Mbps-Full',4),('nway-disabled-100Mbps-Half',5),('nway-disabled-100Mbps-Full',6),('nway-disabled-1Gigabps-Full',8),('nway-disabled-1Gigabps-Full-master',9),('nway-disabled-1Gigabps-Full-slave',10)))
_SwL2PortCtrlNwayState_Type.__name__=_B
_SwL2PortCtrlNwayState_Object=MibTableColumn
swL2PortCtrlNwayState=_SwL2PortCtrlNwayState_Object((1,3,6,1,4,1,171,11,70,2,2,3,2,1,5),_SwL2PortCtrlNwayState_Type())
swL2PortCtrlNwayState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlNwayState.setStatus(_A)
class _SwL2PortCtrlFlowCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2PortCtrlFlowCtrlState_Type.__name__=_B
_SwL2PortCtrlFlowCtrlState_Object=MibTableColumn
swL2PortCtrlFlowCtrlState=_SwL2PortCtrlFlowCtrlState_Object((1,3,6,1,4,1,171,11,70,2,2,3,2,1,6),_SwL2PortCtrlFlowCtrlState_Type())
swL2PortCtrlFlowCtrlState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlFlowCtrlState.setStatus(_A)
class _SwL2PortCtrlLockState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2PortCtrlLockState_Type.__name__=_B
_SwL2PortCtrlLockState_Object=MibTableColumn
swL2PortCtrlLockState=_SwL2PortCtrlLockState_Object((1,3,6,1,4,1,171,11,70,2,2,3,2,1,7),_SwL2PortCtrlLockState_Type())
swL2PortCtrlLockState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlLockState.setStatus(_A)
class _SwL2PortCtrlMACNotifyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2PortCtrlMACNotifyState_Type.__name__=_B
_SwL2PortCtrlMACNotifyState_Object=MibTableColumn
swL2PortCtrlMACNotifyState=_SwL2PortCtrlMACNotifyState_Object((1,3,6,1,4,1,171,11,70,2,2,3,2,1,8),_SwL2PortCtrlMACNotifyState_Type())
swL2PortCtrlMACNotifyState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlMACNotifyState.setStatus(_A)
class _SwL2PortCtrlAutoNegRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('restart',1),('norestart',2)))
_SwL2PortCtrlAutoNegRestart_Type.__name__=_B
_SwL2PortCtrlAutoNegRestart_Object=MibTableColumn
swL2PortCtrlAutoNegRestart=_SwL2PortCtrlAutoNegRestart_Object((1,3,6,1,4,1,171,11,70,2,2,3,2,1,11),_SwL2PortCtrlAutoNegRestart_Type())
swL2PortCtrlAutoNegRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlAutoNegRestart.setStatus(_A)
_SwL2PortCtrlAutoNegCapAdvertisedBits_Type=IANAifMauAutoNegCapBits
_SwL2PortCtrlAutoNegCapAdvertisedBits_Object=MibTableColumn
swL2PortCtrlAutoNegCapAdvertisedBits=_SwL2PortCtrlAutoNegCapAdvertisedBits_Object((1,3,6,1,4,1,171,11,70,2,2,3,2,1,12),_SwL2PortCtrlAutoNegCapAdvertisedBits_Type())
swL2PortCtrlAutoNegCapAdvertisedBits.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlAutoNegCapAdvertisedBits.setStatus(_A)
class _SwL2PortCtrlJumboFrame_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2PortCtrlJumboFrame_Type.__name__=_B
_SwL2PortCtrlJumboFrame_Object=MibScalar
swL2PortCtrlJumboFrame=_SwL2PortCtrlJumboFrame_Object((1,3,6,1,4,1,171,11,70,2,2,3,3),_SwL2PortCtrlJumboFrame_Type())
swL2PortCtrlJumboFrame.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlJumboFrame.setStatus(_A)
_SwL2PortCtrlJumboFrameMaxSize_Type=Integer32
_SwL2PortCtrlJumboFrameMaxSize_Object=MibScalar
swL2PortCtrlJumboFrameMaxSize=_SwL2PortCtrlJumboFrameMaxSize_Object((1,3,6,1,4,1,171,11,70,2,2,3,4),_SwL2PortCtrlJumboFrameMaxSize_Type())
swL2PortCtrlJumboFrameMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlJumboFrameMaxSize.setStatus(_A)
_SwL2PortCounterCtrlTable_Object=MibTable
swL2PortCounterCtrlTable=_SwL2PortCounterCtrlTable_Object((1,3,6,1,4,1,171,11,70,2,2,3,6))
if mibBuilder.loadTexts:swL2PortCounterCtrlTable.setStatus(_A)
_SwL2PortCounterCtrlEntry_Object=MibTableRow
swL2PortCounterCtrlEntry=_SwL2PortCounterCtrlEntry_Object((1,3,6,1,4,1,171,11,70,2,2,3,6,1))
swL2PortCounterCtrlEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:swL2PortCounterCtrlEntry.setStatus(_A)
class _SwL2PortCounterCtrlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortCounterCtrlPortIndex_Type.__name__=_B
_SwL2PortCounterCtrlPortIndex_Object=MibTableColumn
swL2PortCounterCtrlPortIndex=_SwL2PortCounterCtrlPortIndex_Object((1,3,6,1,4,1,171,11,70,2,2,3,6,1,1),_SwL2PortCounterCtrlPortIndex_Type())
swL2PortCounterCtrlPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCounterCtrlPortIndex.setStatus(_A)
class _SwL2PortCounterClearCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_N,2)))
_SwL2PortCounterClearCtrl_Type.__name__=_B
_SwL2PortCounterClearCtrl_Object=MibTableColumn
swL2PortCounterClearCtrl=_SwL2PortCounterClearCtrl_Object((1,3,6,1,4,1,171,11,70,2,2,3,6,1,2),_SwL2PortCounterClearCtrl_Type())
swL2PortCounterClearCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCounterClearCtrl.setStatus(_A)
_SwL2PortAutoNegInfoTable_Object=MibTable
swL2PortAutoNegInfoTable=_SwL2PortAutoNegInfoTable_Object((1,3,6,1,4,1,171,11,70,2,2,3,8))
if mibBuilder.loadTexts:swL2PortAutoNegInfoTable.setStatus(_A)
_SwL2PortAutoNegInfoEntry_Object=MibTableRow
swL2PortAutoNegInfoEntry=_SwL2PortAutoNegInfoEntry_Object((1,3,6,1,4,1,171,11,70,2,2,3,8,1))
swL2PortAutoNegInfoEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:swL2PortAutoNegInfoEntry.setStatus(_A)
class _SwL2PortAutoNegInfoPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortAutoNegInfoPortIndex_Type.__name__=_B
_SwL2PortAutoNegInfoPortIndex_Object=MibTableColumn
swL2PortAutoNegInfoPortIndex=_SwL2PortAutoNegInfoPortIndex_Object((1,3,6,1,4,1,171,11,70,2,2,3,8,1,1),_SwL2PortAutoNegInfoPortIndex_Type())
swL2PortAutoNegInfoPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortAutoNegInfoPortIndex.setStatus(_A)
class _SwL2PortAutoNegInfoAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2PortAutoNegInfoAdminStatus_Type.__name__=_B
_SwL2PortAutoNegInfoAdminStatus_Object=MibTableColumn
swL2PortAutoNegInfoAdminStatus=_SwL2PortAutoNegInfoAdminStatus_Object((1,3,6,1,4,1,171,11,70,2,2,3,8,1,2),_SwL2PortAutoNegInfoAdminStatus_Type())
swL2PortAutoNegInfoAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortAutoNegInfoAdminStatus.setStatus(_A)
_SwL2PortAutoNegInfoCapabilityBits_Type=IANAifMauAutoNegCapBits
_SwL2PortAutoNegInfoCapabilityBits_Object=MibTableColumn
swL2PortAutoNegInfoCapabilityBits=_SwL2PortAutoNegInfoCapabilityBits_Object((1,3,6,1,4,1,171,11,70,2,2,3,8,1,3),_SwL2PortAutoNegInfoCapabilityBits_Type())
swL2PortAutoNegInfoCapabilityBits.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortAutoNegInfoCapabilityBits.setStatus(_A)
_SwL2PortAutoNegInfoCapAdvertisedBits_Type=IANAifMauAutoNegCapBits
_SwL2PortAutoNegInfoCapAdvertisedBits_Object=MibTableColumn
swL2PortAutoNegInfoCapAdvertisedBits=_SwL2PortAutoNegInfoCapAdvertisedBits_Object((1,3,6,1,4,1,171,11,70,2,2,3,8,1,4),_SwL2PortAutoNegInfoCapAdvertisedBits_Type())
swL2PortAutoNegInfoCapAdvertisedBits.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortAutoNegInfoCapAdvertisedBits.setStatus(_A)
_SwL2PortAutoNegInfoCapReceivedBits_Type=IANAifMauAutoNegCapBits
_SwL2PortAutoNegInfoCapReceivedBits_Object=MibTableColumn
swL2PortAutoNegInfoCapReceivedBits=_SwL2PortAutoNegInfoCapReceivedBits_Object((1,3,6,1,4,1,171,11,70,2,2,3,8,1,5),_SwL2PortAutoNegInfoCapReceivedBits_Type())
swL2PortAutoNegInfoCapReceivedBits.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortAutoNegInfoCapReceivedBits.setStatus(_A)
_SwL2PortDropCounterTable_Object=MibTable
swL2PortDropCounterTable=_SwL2PortDropCounterTable_Object((1,3,6,1,4,1,171,11,70,2,2,3,9))
if mibBuilder.loadTexts:swL2PortDropCounterTable.setStatus(_A)
_SwL2PortDropCounterEntry_Object=MibTableRow
swL2PortDropCounterEntry=_SwL2PortDropCounterEntry_Object((1,3,6,1,4,1,171,11,70,2,2,3,9,1))
swL2PortDropCounterEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:swL2PortDropCounterEntry.setStatus(_A)
class _SwL2PortDropCounterPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortDropCounterPortIndex_Type.__name__=_B
_SwL2PortDropCounterPortIndex_Object=MibTableColumn
swL2PortDropCounterPortIndex=_SwL2PortDropCounterPortIndex_Object((1,3,6,1,4,1,171,11,70,2,2,3,9,1,1),_SwL2PortDropCounterPortIndex_Type())
swL2PortDropCounterPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortDropCounterPortIndex.setStatus(_A)
_SwL2PortBufferFullDrops_Type=Counter32
_SwL2PortBufferFullDrops_Object=MibTableColumn
swL2PortBufferFullDrops=_SwL2PortBufferFullDrops_Object((1,3,6,1,4,1,171,11,70,2,2,3,9,1,2),_SwL2PortBufferFullDrops_Type())
swL2PortBufferFullDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortBufferFullDrops.setStatus(_A)
_SwL2PortACLDrops_Type=Counter32
_SwL2PortACLDrops_Object=MibTableColumn
swL2PortACLDrops=_SwL2PortACLDrops_Object((1,3,6,1,4,1,171,11,70,2,2,3,9,1,3),_SwL2PortACLDrops_Type())
swL2PortACLDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortACLDrops.setStatus(_A)
_SwL2PortMulticastDrops_Type=Counter32
_SwL2PortMulticastDrops_Object=MibTableColumn
swL2PortMulticastDrops=_SwL2PortMulticastDrops_Object((1,3,6,1,4,1,171,11,70,2,2,3,9,1,4),_SwL2PortMulticastDrops_Type())
swL2PortMulticastDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortMulticastDrops.setStatus(_A)
_SwL2PortVLANIngressDrops_Type=Counter32
_SwL2PortVLANIngressDrops_Object=MibTableColumn
swL2PortVLANIngressDrops=_SwL2PortVLANIngressDrops_Object((1,3,6,1,4,1,171,11,70,2,2,3,9,1,5),_SwL2PortVLANIngressDrops_Type())
swL2PortVLANIngressDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortVLANIngressDrops.setStatus(_A)
_SwL2PortStatisTable_Object=MibTable
swL2PortStatisTable=_SwL2PortStatisTable_Object((1,3,6,1,4,1,171,11,70,2,2,3,10))
if mibBuilder.loadTexts:swL2PortStatisTable.setStatus(_A)
_SwL2PortStatisEntry_Object=MibTableRow
swL2PortStatisEntry=_SwL2PortStatisEntry_Object((1,3,6,1,4,1,171,11,70,2,2,3,10,1))
swL2PortStatisEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:swL2PortStatisEntry.setStatus(_A)
class _SwL2PortStatisPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortStatisPortIndex_Type.__name__=_B
_SwL2PortStatisPortIndex_Object=MibTableColumn
swL2PortStatisPortIndex=_SwL2PortStatisPortIndex_Object((1,3,6,1,4,1,171,11,70,2,2,3,10,1,1),_SwL2PortStatisPortIndex_Type())
swL2PortStatisPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortStatisPortIndex.setStatus(_A)
_SwL2PortStatisPkts1519to1522Octets_Type=Counter32
_SwL2PortStatisPkts1519to1522Octets_Object=MibTableColumn
swL2PortStatisPkts1519to1522Octets=_SwL2PortStatisPkts1519to1522Octets_Object((1,3,6,1,4,1,171,11,70,2,2,3,10,1,2),_SwL2PortStatisPkts1519to1522Octets_Type())
swL2PortStatisPkts1519to1522Octets.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortStatisPkts1519to1522Octets.setStatus(_A)
_SwL2PortStatisPkts1519to2047Octets_Type=Counter32
_SwL2PortStatisPkts1519to2047Octets_Object=MibTableColumn
swL2PortStatisPkts1519to2047Octets=_SwL2PortStatisPkts1519to2047Octets_Object((1,3,6,1,4,1,171,11,70,2,2,3,10,1,3),_SwL2PortStatisPkts1519to2047Octets_Type())
swL2PortStatisPkts1519to2047Octets.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortStatisPkts1519to2047Octets.setStatus(_A)
_SwL2PortStatisPkts2048to4095Octets_Type=Counter32
_SwL2PortStatisPkts2048to4095Octets_Object=MibTableColumn
swL2PortStatisPkts2048to4095Octets=_SwL2PortStatisPkts2048to4095Octets_Object((1,3,6,1,4,1,171,11,70,2,2,3,10,1,4),_SwL2PortStatisPkts2048to4095Octets_Type())
swL2PortStatisPkts2048to4095Octets.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortStatisPkts2048to4095Octets.setStatus(_A)
_SwL2PortStatisPkts4096to9216Octets_Type=Counter32
_SwL2PortStatisPkts4096to9216Octets_Object=MibTableColumn
swL2PortStatisPkts4096to9216Octets=_SwL2PortStatisPkts4096to9216Octets_Object((1,3,6,1,4,1,171,11,70,2,2,3,10,1,5),_SwL2PortStatisPkts4096to9216Octets_Type())
swL2PortStatisPkts4096to9216Octets.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortStatisPkts4096to9216Octets.setStatus(_A)
_SwL2PortSfpInfoTable_Object=MibTable
swL2PortSfpInfoTable=_SwL2PortSfpInfoTable_Object((1,3,6,1,4,1,171,11,70,2,2,3,11))
if mibBuilder.loadTexts:swL2PortSfpInfoTable.setStatus(_A)
_SwL2PortSfpInfoEntry_Object=MibTableRow
swL2PortSfpInfoEntry=_SwL2PortSfpInfoEntry_Object((1,3,6,1,4,1,171,11,70,2,2,3,11,1))
swL2PortSfpInfoEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:swL2PortSfpInfoEntry.setStatus(_A)
class _SwL2PortSfpInfoPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortSfpInfoPortIndex_Type.__name__=_B
_SwL2PortSfpInfoPortIndex_Object=MibTableColumn
swL2PortSfpInfoPortIndex=_SwL2PortSfpInfoPortIndex_Object((1,3,6,1,4,1,171,11,70,2,2,3,11,1,1),_SwL2PortSfpInfoPortIndex_Type())
swL2PortSfpInfoPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSfpInfoPortIndex.setStatus(_A)
class _SwL2PortSfpInfoConnectType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_SwL2PortSfpInfoConnectType_Type.__name__=_I
_SwL2PortSfpInfoConnectType_Object=MibTableColumn
swL2PortSfpInfoConnectType=_SwL2PortSfpInfoConnectType_Object((1,3,6,1,4,1,171,11,70,2,2,3,11,1,2),_SwL2PortSfpInfoConnectType_Type())
swL2PortSfpInfoConnectType.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSfpInfoConnectType.setStatus(_A)
class _SwL2PortSfpInfoVendorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_SwL2PortSfpInfoVendorName_Type.__name__=_I
_SwL2PortSfpInfoVendorName_Object=MibTableColumn
swL2PortSfpInfoVendorName=_SwL2PortSfpInfoVendorName_Object((1,3,6,1,4,1,171,11,70,2,2,3,11,1,3),_SwL2PortSfpInfoVendorName_Type())
swL2PortSfpInfoVendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSfpInfoVendorName.setStatus(_A)
class _SwL2PortSfpInfoVendorPN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_SwL2PortSfpInfoVendorPN_Type.__name__=_I
_SwL2PortSfpInfoVendorPN_Object=MibTableColumn
swL2PortSfpInfoVendorPN=_SwL2PortSfpInfoVendorPN_Object((1,3,6,1,4,1,171,11,70,2,2,3,11,1,4),_SwL2PortSfpInfoVendorPN_Type())
swL2PortSfpInfoVendorPN.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSfpInfoVendorPN.setStatus(_A)
class _SwL2PortSfpInfoVendorSN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_SwL2PortSfpInfoVendorSN_Type.__name__=_I
_SwL2PortSfpInfoVendorSN_Object=MibTableColumn
swL2PortSfpInfoVendorSN=_SwL2PortSfpInfoVendorSN_Object((1,3,6,1,4,1,171,11,70,2,2,3,11,1,5),_SwL2PortSfpInfoVendorSN_Type())
swL2PortSfpInfoVendorSN.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSfpInfoVendorSN.setStatus(_A)
class _SwL2PortSfpInfoVendorOUI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,6))
_SwL2PortSfpInfoVendorOUI_Type.__name__=_I
_SwL2PortSfpInfoVendorOUI_Object=MibTableColumn
swL2PortSfpInfoVendorOUI=_SwL2PortSfpInfoVendorOUI_Object((1,3,6,1,4,1,171,11,70,2,2,3,11,1,6),_SwL2PortSfpInfoVendorOUI_Type())
swL2PortSfpInfoVendorOUI.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSfpInfoVendorOUI.setStatus(_A)
class _SwL2PortSfpInfoVendorRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,4))
_SwL2PortSfpInfoVendorRev_Type.__name__=_I
_SwL2PortSfpInfoVendorRev_Object=MibTableColumn
swL2PortSfpInfoVendorRev=_SwL2PortSfpInfoVendorRev_Object((1,3,6,1,4,1,171,11,70,2,2,3,11,1,7),_SwL2PortSfpInfoVendorRev_Type())
swL2PortSfpInfoVendorRev.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSfpInfoVendorRev.setStatus(_A)
class _SwL2PortSfpInfoDateCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_SwL2PortSfpInfoDateCode_Type.__name__=_I
_SwL2PortSfpInfoDateCode_Object=MibTableColumn
swL2PortSfpInfoDateCode=_SwL2PortSfpInfoDateCode_Object((1,3,6,1,4,1,171,11,70,2,2,3,11,1,8),_SwL2PortSfpInfoDateCode_Type())
swL2PortSfpInfoDateCode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSfpInfoDateCode.setStatus(_A)
class _SwL2PortSfpInfoFiberType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_SwL2PortSfpInfoFiberType_Type.__name__=_I
_SwL2PortSfpInfoFiberType_Object=MibTableColumn
swL2PortSfpInfoFiberType=_SwL2PortSfpInfoFiberType_Object((1,3,6,1,4,1,171,11,70,2,2,3,11,1,9),_SwL2PortSfpInfoFiberType_Type())
swL2PortSfpInfoFiberType.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSfpInfoFiberType.setStatus(_A)
class _SwL2PortSfpInfoBaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortSfpInfoBaudRate_Type.__name__=_B
_SwL2PortSfpInfoBaudRate_Object=MibTableColumn
swL2PortSfpInfoBaudRate=_SwL2PortSfpInfoBaudRate_Object((1,3,6,1,4,1,171,11,70,2,2,3,11,1,10),_SwL2PortSfpInfoBaudRate_Type())
swL2PortSfpInfoBaudRate.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSfpInfoBaudRate.setStatus(_A)
class _SwL2PortSfpInfoWavelength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortSfpInfoWavelength_Type.__name__=_B
_SwL2PortSfpInfoWavelength_Object=MibTableColumn
swL2PortSfpInfoWavelength=_SwL2PortSfpInfoWavelength_Object((1,3,6,1,4,1,171,11,70,2,2,3,11,1,11),_SwL2PortSfpInfoWavelength_Type())
swL2PortSfpInfoWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSfpInfoWavelength.setStatus(_A)
_SwL2QOSMgmt_ObjectIdentity=ObjectIdentity
swL2QOSMgmt=_SwL2QOSMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,6))
_SwL2QOSBandwidthControlTable_Object=MibTable
swL2QOSBandwidthControlTable=_SwL2QOSBandwidthControlTable_Object((1,3,6,1,4,1,171,11,70,2,2,6,1))
if mibBuilder.loadTexts:swL2QOSBandwidthControlTable.setStatus(_A)
_SwL2QOSBandwidthControlEntry_Object=MibTableRow
swL2QOSBandwidthControlEntry=_SwL2QOSBandwidthControlEntry_Object((1,3,6,1,4,1,171,11,70,2,2,6,1,1))
swL2QOSBandwidthControlEntry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:swL2QOSBandwidthControlEntry.setStatus(_A)
class _SwL2QOSBandwidthPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,768))
_SwL2QOSBandwidthPortIndex_Type.__name__=_B
_SwL2QOSBandwidthPortIndex_Object=MibTableColumn
swL2QOSBandwidthPortIndex=_SwL2QOSBandwidthPortIndex_Object((1,3,6,1,4,1,171,11,70,2,2,6,1,1,1),_SwL2QOSBandwidthPortIndex_Type())
swL2QOSBandwidthPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSBandwidthPortIndex.setStatus(_A)
class _SwL2QOSBandwidthRxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,10000000))
_SwL2QOSBandwidthRxRate_Type.__name__=_B
_SwL2QOSBandwidthRxRate_Object=MibTableColumn
swL2QOSBandwidthRxRate=_SwL2QOSBandwidthRxRate_Object((1,3,6,1,4,1,171,11,70,2,2,6,1,1,2),_SwL2QOSBandwidthRxRate_Type())
swL2QOSBandwidthRxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSBandwidthRxRate.setStatus(_A)
class _SwL2QOSBandwidthTxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,10000000))
_SwL2QOSBandwidthTxRate_Type.__name__=_B
_SwL2QOSBandwidthTxRate_Object=MibTableColumn
swL2QOSBandwidthTxRate=_SwL2QOSBandwidthTxRate_Object((1,3,6,1,4,1,171,11,70,2,2,6,1,1,3),_SwL2QOSBandwidthTxRate_Type())
swL2QOSBandwidthTxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSBandwidthTxRate.setStatus(_A)
_SwL2QOSBandwidthRadiusRxRate_Type=Integer32
_SwL2QOSBandwidthRadiusRxRate_Object=MibTableColumn
swL2QOSBandwidthRadiusRxRate=_SwL2QOSBandwidthRadiusRxRate_Object((1,3,6,1,4,1,171,11,70,2,2,6,1,1,4),_SwL2QOSBandwidthRadiusRxRate_Type())
swL2QOSBandwidthRadiusRxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSBandwidthRadiusRxRate.setStatus(_A)
_SwL2QOSBandwidthRadiusTxRate_Type=Integer32
_SwL2QOSBandwidthRadiusTxRate_Object=MibTableColumn
swL2QOSBandwidthRadiusTxRate=_SwL2QOSBandwidthRadiusTxRate_Object((1,3,6,1,4,1,171,11,70,2,2,6,1,1,5),_SwL2QOSBandwidthRadiusTxRate_Type())
swL2QOSBandwidthRadiusTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSBandwidthRadiusTxRate.setStatus(_A)
_SwL2QOSSchedulingTable_Object=MibTable
swL2QOSSchedulingTable=_SwL2QOSSchedulingTable_Object((1,3,6,1,4,1,171,11,70,2,2,6,2))
if mibBuilder.loadTexts:swL2QOSSchedulingTable.setStatus(_A)
_SwL2QOSSchedulingEntry_Object=MibTableRow
swL2QOSSchedulingEntry=_SwL2QOSSchedulingEntry_Object((1,3,6,1,4,1,171,11,70,2,2,6,2,1))
swL2QOSSchedulingEntry.setIndexNames((0,_E,_j),(0,_E,_k))
if mibBuilder.loadTexts:swL2QOSSchedulingEntry.setStatus(_A)
_SwL2QOSSchedulingPort_Type=Integer32
_SwL2QOSSchedulingPort_Object=MibTableColumn
swL2QOSSchedulingPort=_SwL2QOSSchedulingPort_Object((1,3,6,1,4,1,171,11,70,2,2,6,2,1,1),_SwL2QOSSchedulingPort_Type())
swL2QOSSchedulingPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSSchedulingPort.setStatus(_A)
class _SwL2QOSSchedulingClassID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwL2QOSSchedulingClassID_Type.__name__=_B
_SwL2QOSSchedulingClassID_Object=MibTableColumn
swL2QOSSchedulingClassID=_SwL2QOSSchedulingClassID_Object((1,3,6,1,4,1,171,11,70,2,2,6,2,1,2),_SwL2QOSSchedulingClassID_Type())
swL2QOSSchedulingClassID.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSSchedulingClassID.setStatus(_A)
class _SwL2QOSSchedulingMaxPkts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_SwL2QOSSchedulingMaxPkts_Type.__name__=_B
_SwL2QOSSchedulingMaxPkts_Object=MibTableColumn
swL2QOSSchedulingMaxPkts=_SwL2QOSSchedulingMaxPkts_Object((1,3,6,1,4,1,171,11,70,2,2,6,2,1,3),_SwL2QOSSchedulingMaxPkts_Type())
swL2QOSSchedulingMaxPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSSchedulingMaxPkts.setStatus(_A)
class _SwL2QOSSchedulingMechanism_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_O,1),(_P,3)))
_SwL2QOSSchedulingMechanism_Type.__name__=_B
_SwL2QOSSchedulingMechanism_Object=MibTableColumn
swL2QOSSchedulingMechanism=_SwL2QOSSchedulingMechanism_Object((1,3,6,1,4,1,171,11,70,2,2,6,2,1,4),_SwL2QOSSchedulingMechanism_Type())
swL2QOSSchedulingMechanism.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSSchedulingMechanism.setStatus(_A)
class _SwL2QOSSchedulingMechanismEffec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_O,1),(_P,3)))
_SwL2QOSSchedulingMechanismEffec_Type.__name__=_B
_SwL2QOSSchedulingMechanismEffec_Object=MibTableColumn
swL2QOSSchedulingMechanismEffec=_SwL2QOSSchedulingMechanismEffec_Object((1,3,6,1,4,1,171,11,70,2,2,6,2,1,5),_SwL2QOSSchedulingMechanismEffec_Type())
swL2QOSSchedulingMechanismEffec.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSSchedulingMechanismEffec.setStatus(_A)
_SwL2QOS8021pUserPriorityTable_Object=MibTable
swL2QOS8021pUserPriorityTable=_SwL2QOS8021pUserPriorityTable_Object((1,3,6,1,4,1,171,11,70,2,2,6,3))
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityTable.setStatus(_A)
_SwL2QOS8021pUserPriorityEntry_Object=MibTableRow
swL2QOS8021pUserPriorityEntry=_SwL2QOS8021pUserPriorityEntry_Object((1,3,6,1,4,1,171,11,70,2,2,6,3,1))
swL2QOS8021pUserPriorityEntry.setIndexNames((0,_E,_l))
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityEntry.setStatus(_A)
class _SwL2QOS8021pUserPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwL2QOS8021pUserPriorityIndex_Type.__name__=_B
_SwL2QOS8021pUserPriorityIndex_Object=MibTableColumn
swL2QOS8021pUserPriorityIndex=_SwL2QOS8021pUserPriorityIndex_Object((1,3,6,1,4,1,171,11,70,2,2,6,3,1,1),_SwL2QOS8021pUserPriorityIndex_Type())
swL2QOS8021pUserPriorityIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityIndex.setStatus(_A)
class _SwL2QOS8021pUserPriorityClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_SwL2QOS8021pUserPriorityClass_Type.__name__=_B
_SwL2QOS8021pUserPriorityClass_Object=MibTableColumn
swL2QOS8021pUserPriorityClass=_SwL2QOS8021pUserPriorityClass_Object((1,3,6,1,4,1,171,11,70,2,2,6,3,1,2),_SwL2QOS8021pUserPriorityClass_Type())
swL2QOS8021pUserPriorityClass.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityClass.setStatus(_A)
_SwL2QOS8021pDefaultPriorityTable_Object=MibTable
swL2QOS8021pDefaultPriorityTable=_SwL2QOS8021pDefaultPriorityTable_Object((1,3,6,1,4,1,171,11,70,2,2,6,4))
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriorityTable.setStatus(_A)
_SwL2QOS8021pDefaultPriorityEntry_Object=MibTableRow
swL2QOS8021pDefaultPriorityEntry=_SwL2QOS8021pDefaultPriorityEntry_Object((1,3,6,1,4,1,171,11,70,2,2,6,4,1))
swL2QOS8021pDefaultPriorityEntry.setIndexNames((0,_E,_m))
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriorityEntry.setStatus(_A)
class _SwL2QOS8021pDefaultPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,768))
_SwL2QOS8021pDefaultPriorityIndex_Type.__name__=_B
_SwL2QOS8021pDefaultPriorityIndex_Object=MibTableColumn
swL2QOS8021pDefaultPriorityIndex=_SwL2QOS8021pDefaultPriorityIndex_Object((1,3,6,1,4,1,171,11,70,2,2,6,4,1,1),_SwL2QOS8021pDefaultPriorityIndex_Type())
swL2QOS8021pDefaultPriorityIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriorityIndex.setStatus(_A)
class _SwL2QOS8021pDefaultPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwL2QOS8021pDefaultPriority_Type.__name__=_B
_SwL2QOS8021pDefaultPriority_Object=MibTableColumn
swL2QOS8021pDefaultPriority=_SwL2QOS8021pDefaultPriority_Object((1,3,6,1,4,1,171,11,70,2,2,6,4,1,2),_SwL2QOS8021pDefaultPriority_Type())
swL2QOS8021pDefaultPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriority.setStatus(_A)
_SwL2QOS8021pRadiusPriority_Type=Integer32
_SwL2QOS8021pRadiusPriority_Object=MibTableColumn
swL2QOS8021pRadiusPriority=_SwL2QOS8021pRadiusPriority_Object((1,3,6,1,4,1,171,11,70,2,2,6,4,1,3),_SwL2QOS8021pRadiusPriority_Type())
swL2QOS8021pRadiusPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOS8021pRadiusPriority.setStatus(_A)
class _SwL2QOSSchedulingMechanismCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),('roundrobin',2),(_P,3)))
_SwL2QOSSchedulingMechanismCtrl_Type.__name__=_B
_SwL2QOSSchedulingMechanismCtrl_Object=MibScalar
swL2QOSSchedulingMechanismCtrl=_SwL2QOSSchedulingMechanismCtrl_Object((1,3,6,1,4,1,171,11,70,2,2,6,5),_SwL2QOSSchedulingMechanismCtrl_Type())
swL2QOSSchedulingMechanismCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSSchedulingMechanismCtrl.setStatus(_A)
class _SwL2QOSHolPreventionCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2QOSHolPreventionCtrl_Type.__name__=_B
_SwL2QOSHolPreventionCtrl_Object=MibScalar
swL2QOSHolPreventionCtrl=_SwL2QOSHolPreventionCtrl_Object((1,3,6,1,4,1,171,11,70,2,2,6,6),_SwL2QOSHolPreventionCtrl_Type())
swL2QOSHolPreventionCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSHolPreventionCtrl.setStatus(_A)
_SwCosBandwidthControlTable_Object=MibTable
swCosBandwidthControlTable=_SwCosBandwidthControlTable_Object((1,3,6,1,4,1,171,11,70,2,2,6,7))
if mibBuilder.loadTexts:swCosBandwidthControlTable.setStatus(_A)
_SwCosBandwidthControlEntry_Object=MibTableRow
swCosBandwidthControlEntry=_SwCosBandwidthControlEntry_Object((1,3,6,1,4,1,171,11,70,2,2,6,7,1))
swCosBandwidthControlEntry.setIndexNames((0,_E,_n),(0,_E,_o))
if mibBuilder.loadTexts:swCosBandwidthControlEntry.setStatus(_A)
_SwCosBandwidthPort_Type=Integer32
_SwCosBandwidthPort_Object=MibTableColumn
swCosBandwidthPort=_SwCosBandwidthPort_Object((1,3,6,1,4,1,171,11,70,2,2,6,7,1,1),_SwCosBandwidthPort_Type())
swCosBandwidthPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swCosBandwidthPort.setStatus(_A)
class _SwCosBandwidthClassID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwCosBandwidthClassID_Type.__name__=_B
_SwCosBandwidthClassID_Object=MibTableColumn
swCosBandwidthClassID=_SwCosBandwidthClassID_Object((1,3,6,1,4,1,171,11,70,2,2,6,7,1,2),_SwCosBandwidthClassID_Type())
swCosBandwidthClassID.setMaxAccess(_C)
if mibBuilder.loadTexts:swCosBandwidthClassID.setStatus(_A)
class _SwCosBandwidthMinRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(64,10000000))
_SwCosBandwidthMinRate_Type.__name__=_B
_SwCosBandwidthMinRate_Object=MibTableColumn
swCosBandwidthMinRate=_SwCosBandwidthMinRate_Object((1,3,6,1,4,1,171,11,70,2,2,6,7,1,3),_SwCosBandwidthMinRate_Type())
swCosBandwidthMinRate.setMaxAccess(_D)
if mibBuilder.loadTexts:swCosBandwidthMinRate.setStatus(_A)
class _SwCosBandwidthMaxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(64,10000000))
_SwCosBandwidthMaxRate_Type.__name__=_B
_SwCosBandwidthMaxRate_Object=MibTableColumn
swCosBandwidthMaxRate=_SwCosBandwidthMaxRate_Object((1,3,6,1,4,1,171,11,70,2,2,6,7,1,4),_SwCosBandwidthMaxRate_Type())
swCosBandwidthMaxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:swCosBandwidthMaxRate.setStatus(_A)
_SwQosDscpTrustPortCtrlTable_Object=MibTable
swQosDscpTrustPortCtrlTable=_SwQosDscpTrustPortCtrlTable_Object((1,3,6,1,4,1,171,11,70,2,2,6,8))
if mibBuilder.loadTexts:swQosDscpTrustPortCtrlTable.setStatus(_A)
_SwQosDscpTrustPortCtrlEntry_Object=MibTableRow
swQosDscpTrustPortCtrlEntry=_SwQosDscpTrustPortCtrlEntry_Object((1,3,6,1,4,1,171,11,70,2,2,6,8,1))
swQosDscpTrustPortCtrlEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:swQosDscpTrustPortCtrlEntry.setStatus(_A)
_SwQosDscpTrustPortCtrlPortIndex_Type=Integer32
_SwQosDscpTrustPortCtrlPortIndex_Object=MibTableColumn
swQosDscpTrustPortCtrlPortIndex=_SwQosDscpTrustPortCtrlPortIndex_Object((1,3,6,1,4,1,171,11,70,2,2,6,8,1,1),_SwQosDscpTrustPortCtrlPortIndex_Type())
swQosDscpTrustPortCtrlPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swQosDscpTrustPortCtrlPortIndex.setStatus(_A)
class _SwQosDscpTrustPortCtrlState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwQosDscpTrustPortCtrlState_Type.__name__=_B
_SwQosDscpTrustPortCtrlState_Object=MibTableColumn
swQosDscpTrustPortCtrlState=_SwQosDscpTrustPortCtrlState_Object((1,3,6,1,4,1,171,11,70,2,2,6,8,1,2),_SwQosDscpTrustPortCtrlState_Type())
swQosDscpTrustPortCtrlState.setMaxAccess(_D)
if mibBuilder.loadTexts:swQosDscpTrustPortCtrlState.setStatus(_A)
_SwQosDscpMapGlobalCtrlTable_Object=MibTable
swQosDscpMapGlobalCtrlTable=_SwQosDscpMapGlobalCtrlTable_Object((1,3,6,1,4,1,171,11,70,2,2,6,9))
if mibBuilder.loadTexts:swQosDscpMapGlobalCtrlTable.setStatus(_A)
_SwQosDscpMapGlobalCtrlEntry_Object=MibTableRow
swQosDscpMapGlobalCtrlEntry=_SwQosDscpMapGlobalCtrlEntry_Object((1,3,6,1,4,1,171,11,70,2,2,6,9,1))
swQosDscpMapGlobalCtrlEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:swQosDscpMapGlobalCtrlEntry.setStatus(_A)
_SwQosDscpMapGlobalCtrlDscpIndex_Type=Integer32
_SwQosDscpMapGlobalCtrlDscpIndex_Object=MibTableColumn
swQosDscpMapGlobalCtrlDscpIndex=_SwQosDscpMapGlobalCtrlDscpIndex_Object((1,3,6,1,4,1,171,11,70,2,2,6,9,1,1),_SwQosDscpMapGlobalCtrlDscpIndex_Type())
swQosDscpMapGlobalCtrlDscpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swQosDscpMapGlobalCtrlDscpIndex.setStatus(_A)
class _SwQosDscpMapGlobalCtrl8021pPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwQosDscpMapGlobalCtrl8021pPriority_Type.__name__=_B
_SwQosDscpMapGlobalCtrl8021pPriority_Object=MibTableColumn
swQosDscpMapGlobalCtrl8021pPriority=_SwQosDscpMapGlobalCtrl8021pPriority_Object((1,3,6,1,4,1,171,11,70,2,2,6,9,1,2),_SwQosDscpMapGlobalCtrl8021pPriority_Type())
swQosDscpMapGlobalCtrl8021pPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swQosDscpMapGlobalCtrl8021pPriority.setStatus(_A)
class _SwQosDscpMapGlobalCtrlNewDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_SwQosDscpMapGlobalCtrlNewDscp_Type.__name__=_B
_SwQosDscpMapGlobalCtrlNewDscp_Object=MibTableColumn
swQosDscpMapGlobalCtrlNewDscp=_SwQosDscpMapGlobalCtrlNewDscp_Object((1,3,6,1,4,1,171,11,70,2,2,6,9,1,3),_SwQosDscpMapGlobalCtrlNewDscp_Type())
swQosDscpMapGlobalCtrlNewDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:swQosDscpMapGlobalCtrlNewDscp.setStatus(_A)
_SwL2PortSecurityMgmt_ObjectIdentity=ObjectIdentity
swL2PortSecurityMgmt=_SwL2PortSecurityMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,7))
_SwL2PortSecurityControlTable_Object=MibTable
swL2PortSecurityControlTable=_SwL2PortSecurityControlTable_Object((1,3,6,1,4,1,171,11,70,2,2,7,1))
if mibBuilder.loadTexts:swL2PortSecurityControlTable.setStatus(_A)
_SwL2PortSecurityControlEntry_Object=MibTableRow
swL2PortSecurityControlEntry=_SwL2PortSecurityControlEntry_Object((1,3,6,1,4,1,171,11,70,2,2,7,1,1))
swL2PortSecurityControlEntry.setIndexNames((0,_E,_r))
if mibBuilder.loadTexts:swL2PortSecurityControlEntry.setStatus(_A)
class _SwL2PortSecurityPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,768))
_SwL2PortSecurityPortIndex_Type.__name__=_B
_SwL2PortSecurityPortIndex_Object=MibTableColumn
swL2PortSecurityPortIndex=_SwL2PortSecurityPortIndex_Object((1,3,6,1,4,1,171,11,70,2,2,7,1,1,1),_SwL2PortSecurityPortIndex_Type())
swL2PortSecurityPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityPortIndex.setStatus(_A)
class _SwL2PortSecurityMaxLernAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_SwL2PortSecurityMaxLernAddr_Type.__name__=_B
_SwL2PortSecurityMaxLernAddr_Object=MibTableColumn
swL2PortSecurityMaxLernAddr=_SwL2PortSecurityMaxLernAddr_Object((1,3,6,1,4,1,171,11,70,2,2,7,1,1,2),_SwL2PortSecurityMaxLernAddr_Type())
swL2PortSecurityMaxLernAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortSecurityMaxLernAddr.setStatus(_A)
class _SwL2PortSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('permanent',2),('deleteOnTimeout',3),('deleteOnReset',4)))
_SwL2PortSecurityMode_Type.__name__=_B
_SwL2PortSecurityMode_Object=MibTableColumn
swL2PortSecurityMode=_SwL2PortSecurityMode_Object((1,3,6,1,4,1,171,11,70,2,2,7,1,1,3),_SwL2PortSecurityMode_Type())
swL2PortSecurityMode.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortSecurityMode.setStatus(_A)
class _SwL2PortSecurityAdmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_Q,2),(_R,3)))
_SwL2PortSecurityAdmState_Type.__name__=_B
_SwL2PortSecurityAdmState_Object=MibTableColumn
swL2PortSecurityAdmState=_SwL2PortSecurityAdmState_Object((1,3,6,1,4,1,171,11,70,2,2,7,1,1,4),_SwL2PortSecurityAdmState_Type())
swL2PortSecurityAdmState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortSecurityAdmState.setStatus(_A)
_SwL2PortSecurityDelCtrl_ObjectIdentity=ObjectIdentity
swL2PortSecurityDelCtrl=_SwL2PortSecurityDelCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,7,2))
class _SwL2PortSecurityDelVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL2PortSecurityDelVlanName_Type.__name__=_I
_SwL2PortSecurityDelVlanName_Object=MibScalar
swL2PortSecurityDelVlanName=_SwL2PortSecurityDelVlanName_Object((1,3,6,1,4,1,171,11,70,2,2,7,2,1),_SwL2PortSecurityDelVlanName_Type())
swL2PortSecurityDelVlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortSecurityDelVlanName.setStatus(_A)
class _SwL2PortSecurityDelPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,768))
_SwL2PortSecurityDelPort_Type.__name__=_B
_SwL2PortSecurityDelPort_Object=MibScalar
swL2PortSecurityDelPort=_SwL2PortSecurityDelPort_Object((1,3,6,1,4,1,171,11,70,2,2,7,2,2),_SwL2PortSecurityDelPort_Type())
swL2PortSecurityDelPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortSecurityDelPort.setStatus(_A)
_SwL2PortSecurityDelMacAddress_Type=MacAddress
_SwL2PortSecurityDelMacAddress_Object=MibScalar
swL2PortSecurityDelMacAddress=_SwL2PortSecurityDelMacAddress_Object((1,3,6,1,4,1,171,11,70,2,2,7,2,3),_SwL2PortSecurityDelMacAddress_Type())
swL2PortSecurityDelMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortSecurityDelMacAddress.setStatus(_A)
class _SwL2PortSecurityDelActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_N,2)))
_SwL2PortSecurityDelActivity_Type.__name__=_B
_SwL2PortSecurityDelActivity_Object=MibScalar
swL2PortSecurityDelActivity=_SwL2PortSecurityDelActivity_Object((1,3,6,1,4,1,171,11,70,2,2,7,2,4),_SwL2PortSecurityDelActivity_Type())
swL2PortSecurityDelActivity.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortSecurityDelActivity.setStatus(_A)
_SwL2TrunkMgmt_ObjectIdentity=ObjectIdentity
swL2TrunkMgmt=_SwL2TrunkMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,9))
class _SwL2TrunkMaxSupportedEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkMaxSupportedEntries_Type.__name__=_B
_SwL2TrunkMaxSupportedEntries_Object=MibScalar
swL2TrunkMaxSupportedEntries=_SwL2TrunkMaxSupportedEntries_Object((1,3,6,1,4,1,171,11,70,2,2,9,1),_SwL2TrunkMaxSupportedEntries_Type())
swL2TrunkMaxSupportedEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkMaxSupportedEntries.setStatus(_A)
class _SwL2TrunkCurrentNumEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkCurrentNumEntries_Type.__name__=_B
_SwL2TrunkCurrentNumEntries_Object=MibScalar
swL2TrunkCurrentNumEntries=_SwL2TrunkCurrentNumEntries_Object((1,3,6,1,4,1,171,11,70,2,2,9,2),_SwL2TrunkCurrentNumEntries_Type())
swL2TrunkCurrentNumEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkCurrentNumEntries.setStatus(_A)
_SwL2TrunkCtrlTable_Object=MibTable
swL2TrunkCtrlTable=_SwL2TrunkCtrlTable_Object((1,3,6,1,4,1,171,11,70,2,2,9,3))
if mibBuilder.loadTexts:swL2TrunkCtrlTable.setStatus(_A)
_SwL2TrunkCtrlEntry_Object=MibTableRow
swL2TrunkCtrlEntry=_SwL2TrunkCtrlEntry_Object((1,3,6,1,4,1,171,11,70,2,2,9,3,1))
swL2TrunkCtrlEntry.setIndexNames((0,_E,_s))
if mibBuilder.loadTexts:swL2TrunkCtrlEntry.setStatus(_A)
class _SwL2TrunkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkIndex_Type.__name__=_B
_SwL2TrunkIndex_Object=MibTableColumn
swL2TrunkIndex=_SwL2TrunkIndex_Object((1,3,6,1,4,1,171,11,70,2,2,9,3,1,1),_SwL2TrunkIndex_Type())
swL2TrunkIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkIndex.setStatus(_A)
class _SwL2TrunkName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_SwL2TrunkName_Type.__name__=_I
_SwL2TrunkName_Object=MibTableColumn
swL2TrunkName=_SwL2TrunkName_Object((1,3,6,1,4,1,171,11,70,2,2,9,3,1,2),_SwL2TrunkName_Type())
swL2TrunkName.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2TrunkName.setStatus(_A)
class _SwL2TrunkMasterPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2TrunkMasterPort_Type.__name__=_B
_SwL2TrunkMasterPort_Object=MibTableColumn
swL2TrunkMasterPort=_SwL2TrunkMasterPort_Object((1,3,6,1,4,1,171,11,70,2,2,9,3,1,3),_SwL2TrunkMasterPort_Type())
swL2TrunkMasterPort.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2TrunkMasterPort.setStatus(_A)
_SwL2TrunkMember_Type=PortList
_SwL2TrunkMember_Object=MibTableColumn
swL2TrunkMember=_SwL2TrunkMember_Object((1,3,6,1,4,1,171,11,70,2,2,9,3,1,4),_SwL2TrunkMember_Type())
swL2TrunkMember.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2TrunkMember.setStatus(_A)
class _SwL2TrunkFloodingPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2TrunkFloodingPort_Type.__name__=_B
_SwL2TrunkFloodingPort_Object=MibTableColumn
swL2TrunkFloodingPort=_SwL2TrunkFloodingPort_Object((1,3,6,1,4,1,171,11,70,2,2,9,3,1,5),_SwL2TrunkFloodingPort_Type())
swL2TrunkFloodingPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkFloodingPort.setStatus(_A)
class _SwL2TrunkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('static',2),('lacp',3)))
_SwL2TrunkType_Type.__name__=_B
_SwL2TrunkType_Object=MibTableColumn
swL2TrunkType=_SwL2TrunkType_Object((1,3,6,1,4,1,171,11,70,2,2,9,3,1,6),_SwL2TrunkType_Type())
swL2TrunkType.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2TrunkType.setStatus(_A)
_SwL2TrunkState_Type=RowStatus
_SwL2TrunkState_Object=MibTableColumn
swL2TrunkState=_SwL2TrunkState_Object((1,3,6,1,4,1,171,11,70,2,2,9,3,1,7),_SwL2TrunkState_Type())
swL2TrunkState.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2TrunkState.setStatus(_A)
_SwL2TrunkActivePorts_Type=PortList
_SwL2TrunkActivePorts_Object=MibTableColumn
swL2TrunkActivePorts=_SwL2TrunkActivePorts_Object((1,3,6,1,4,1,171,11,70,2,2,9,3,1,8),_SwL2TrunkActivePorts_Type())
swL2TrunkActivePorts.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkActivePorts.setStatus(_A)
class _SwL2TrunkAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_H,1),('mac-source',2),('mac-destination',3),('mac-source-dest',4),('ip-source',5),('ip-destination',6),('ip-source-dest',7)))
_SwL2TrunkAlgorithm_Type.__name__=_B
_SwL2TrunkAlgorithm_Object=MibScalar
swL2TrunkAlgorithm=_SwL2TrunkAlgorithm_Object((1,3,6,1,4,1,171,11,70,2,2,9,4),_SwL2TrunkAlgorithm_Type())
swL2TrunkAlgorithm.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkAlgorithm.setStatus(_A)
_SwL2TrunkLACPPortTable_Object=MibTable
swL2TrunkLACPPortTable=_SwL2TrunkLACPPortTable_Object((1,3,6,1,4,1,171,11,70,2,2,9,5))
if mibBuilder.loadTexts:swL2TrunkLACPPortTable.setStatus(_A)
_SwL2TrunkLACPPortEntry_Object=MibTableRow
swL2TrunkLACPPortEntry=_SwL2TrunkLACPPortEntry_Object((1,3,6,1,4,1,171,11,70,2,2,9,5,1))
swL2TrunkLACPPortEntry.setIndexNames((0,_E,_t))
if mibBuilder.loadTexts:swL2TrunkLACPPortEntry.setStatus(_A)
class _SwL2TrunkLACPPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkLACPPortIndex_Type.__name__=_B
_SwL2TrunkLACPPortIndex_Object=MibTableColumn
swL2TrunkLACPPortIndex=_SwL2TrunkLACPPortIndex_Object((1,3,6,1,4,1,171,11,70,2,2,9,5,1,1),_SwL2TrunkLACPPortIndex_Type())
swL2TrunkLACPPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkLACPPortIndex.setStatus(_A)
class _SwL2TrunkLACPPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),('passive',2)))
_SwL2TrunkLACPPortState_Type.__name__=_B
_SwL2TrunkLACPPortState_Object=MibTableColumn
swL2TrunkLACPPortState=_SwL2TrunkLACPPortState_Object((1,3,6,1,4,1,171,11,70,2,2,9,5,1,2),_SwL2TrunkLACPPortState_Type())
swL2TrunkLACPPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkLACPPortState.setStatus(_A)
_SwL2TrunkVLANTable_Object=MibTable
swL2TrunkVLANTable=_SwL2TrunkVLANTable_Object((1,3,6,1,4,1,171,11,70,2,2,9,6))
if mibBuilder.loadTexts:swL2TrunkVLANTable.setStatus(_A)
_SwL2TrunkVLANEntry_Object=MibTableRow
swL2TrunkVLANEntry=_SwL2TrunkVLANEntry_Object((1,3,6,1,4,1,171,11,70,2,2,9,6,1))
swL2TrunkVLANEntry.setIndexNames((0,_E,_u))
if mibBuilder.loadTexts:swL2TrunkVLANEntry.setStatus(_A)
class _SwL2TrunkVLANPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkVLANPort_Type.__name__=_B
_SwL2TrunkVLANPort_Object=MibTableColumn
swL2TrunkVLANPort=_SwL2TrunkVLANPort_Object((1,3,6,1,4,1,171,11,70,2,2,9,6,1,1),_SwL2TrunkVLANPort_Type())
swL2TrunkVLANPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkVLANPort.setStatus(_A)
class _SwL2TrunkVLANState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2TrunkVLANState_Type.__name__=_B
_SwL2TrunkVLANState_Object=MibTableColumn
swL2TrunkVLANState=_SwL2TrunkVLANState_Object((1,3,6,1,4,1,171,11,70,2,2,9,6,1,2),_SwL2TrunkVLANState_Type())
swL2TrunkVLANState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkVLANState.setStatus(_A)
_SwL2MirrorMgmt_ObjectIdentity=ObjectIdentity
swL2MirrorMgmt=_SwL2MirrorMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,10))
class _SwL2MirrorLogicTargetPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2MirrorLogicTargetPort_Type.__name__=_B
_SwL2MirrorLogicTargetPort_Object=MibScalar
swL2MirrorLogicTargetPort=_SwL2MirrorLogicTargetPort_Object((1,3,6,1,4,1,171,11,70,2,2,10,1),_SwL2MirrorLogicTargetPort_Type())
swL2MirrorLogicTargetPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MirrorLogicTargetPort.setStatus(_A)
_SwL2MirrorPortSourceIngress_Type=PortList
_SwL2MirrorPortSourceIngress_Object=MibScalar
swL2MirrorPortSourceIngress=_SwL2MirrorPortSourceIngress_Object((1,3,6,1,4,1,171,11,70,2,2,10,2),_SwL2MirrorPortSourceIngress_Type())
swL2MirrorPortSourceIngress.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MirrorPortSourceIngress.setStatus(_A)
_SwL2MirrorPortSourceEgress_Type=PortList
_SwL2MirrorPortSourceEgress_Object=MibScalar
swL2MirrorPortSourceEgress=_SwL2MirrorPortSourceEgress_Object((1,3,6,1,4,1,171,11,70,2,2,10,3),_SwL2MirrorPortSourceEgress_Type())
swL2MirrorPortSourceEgress.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MirrorPortSourceEgress.setStatus(_A)
class _SwL2MirrorPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2MirrorPortState_Type.__name__=_B
_SwL2MirrorPortState_Object=MibScalar
swL2MirrorPortState=_SwL2MirrorPortState_Object((1,3,6,1,4,1,171,11,70,2,2,10,4),_SwL2MirrorPortState_Type())
swL2MirrorPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2MirrorPortState.setStatus(_A)
_SwL2MirrorGroupTable_Object=MibTable
swL2MirrorGroupTable=_SwL2MirrorGroupTable_Object((1,3,6,1,4,1,171,11,70,2,2,10,5))
if mibBuilder.loadTexts:swL2MirrorGroupTable.setStatus(_A)
_SwL2MirrorGroupEntry_Object=MibTableRow
swL2MirrorGroupEntry=_SwL2MirrorGroupEntry_Object((1,3,6,1,4,1,171,11,70,2,2,10,5,1))
swL2MirrorGroupEntry.setIndexNames((0,_E,_v))
if mibBuilder.loadTexts:swL2MirrorGroupEntry.setStatus(_A)
_SwL2MirrorGroupID_Type=Integer32
_SwL2MirrorGroupID_Object=MibTableColumn
swL2MirrorGroupID=_SwL2MirrorGroupID_Object((1,3,6,1,4,1,171,11,70,2,2,10,5,1,1),_SwL2MirrorGroupID_Type())
swL2MirrorGroupID.setMaxAccess(_w)
if mibBuilder.loadTexts:swL2MirrorGroupID.setStatus(_A)
_SwL2MirrorGroupRowStatus_Type=RowStatus
_SwL2MirrorGroupRowStatus_Object=MibTableColumn
swL2MirrorGroupRowStatus=_SwL2MirrorGroupRowStatus_Object((1,3,6,1,4,1,171,11,70,2,2,10,5,1,2),_SwL2MirrorGroupRowStatus_Type())
swL2MirrorGroupRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2MirrorGroupRowStatus.setStatus(_A)
class _SwL2MirrorGroupState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2MirrorGroupState_Type.__name__=_B
_SwL2MirrorGroupState_Object=MibTableColumn
swL2MirrorGroupState=_SwL2MirrorGroupState_Object((1,3,6,1,4,1,171,11,70,2,2,10,5,1,3),_SwL2MirrorGroupState_Type())
swL2MirrorGroupState.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2MirrorGroupState.setStatus(_A)
class _SwL2MirrorGroupLogicTargetPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2MirrorGroupLogicTargetPort_Type.__name__=_B
_SwL2MirrorGroupLogicTargetPort_Object=MibTableColumn
swL2MirrorGroupLogicTargetPort=_SwL2MirrorGroupLogicTargetPort_Object((1,3,6,1,4,1,171,11,70,2,2,10,5,1,4),_SwL2MirrorGroupLogicTargetPort_Type())
swL2MirrorGroupLogicTargetPort.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2MirrorGroupLogicTargetPort.setStatus(_A)
_SwL2MirrorGroupPortSourceIngress_Type=PortList
_SwL2MirrorGroupPortSourceIngress_Object=MibTableColumn
swL2MirrorGroupPortSourceIngress=_SwL2MirrorGroupPortSourceIngress_Object((1,3,6,1,4,1,171,11,70,2,2,10,5,1,5),_SwL2MirrorGroupPortSourceIngress_Type())
swL2MirrorGroupPortSourceIngress.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2MirrorGroupPortSourceIngress.setStatus(_A)
_SwL2MirrorGroupPortSourceEngress_Type=PortList
_SwL2MirrorGroupPortSourceEngress_Object=MibTableColumn
swL2MirrorGroupPortSourceEngress=_SwL2MirrorGroupPortSourceEngress_Object((1,3,6,1,4,1,171,11,70,2,2,10,5,1,6),_SwL2MirrorGroupPortSourceEngress_Type())
swL2MirrorGroupPortSourceEngress.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2MirrorGroupPortSourceEngress.setStatus(_A)
_SwL2IGMPMgmt_ObjectIdentity=ObjectIdentity
swL2IGMPMgmt=_SwL2IGMPMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,11))
class _SwL2IGMPMaxSupportedVlans_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPMaxSupportedVlans_Type.__name__=_B
_SwL2IGMPMaxSupportedVlans_Object=MibScalar
swL2IGMPMaxSupportedVlans=_SwL2IGMPMaxSupportedVlans_Object((1,3,6,1,4,1,171,11,70,2,2,11,1),_SwL2IGMPMaxSupportedVlans_Type())
swL2IGMPMaxSupportedVlans.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMaxSupportedVlans.setStatus(_A)
class _SwL2IGMPMaxIpGroupNumPerVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPMaxIpGroupNumPerVlan_Type.__name__=_B
_SwL2IGMPMaxIpGroupNumPerVlan_Object=MibScalar
swL2IGMPMaxIpGroupNumPerVlan=_SwL2IGMPMaxIpGroupNumPerVlan_Object((1,3,6,1,4,1,171,11,70,2,2,11,2),_SwL2IGMPMaxIpGroupNumPerVlan_Type())
swL2IGMPMaxIpGroupNumPerVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMaxIpGroupNumPerVlan.setStatus(_A)
_SwL2IGMPCtrlTable_Object=MibTable
swL2IGMPCtrlTable=_SwL2IGMPCtrlTable_Object((1,3,6,1,4,1,171,11,70,2,2,11,3))
if mibBuilder.loadTexts:swL2IGMPCtrlTable.setStatus(_A)
_SwL2IGMPCtrlEntry_Object=MibTableRow
swL2IGMPCtrlEntry=_SwL2IGMPCtrlEntry_Object((1,3,6,1,4,1,171,11,70,2,2,11,3,1))
swL2IGMPCtrlEntry.setIndexNames((0,_E,_x))
if mibBuilder.loadTexts:swL2IGMPCtrlEntry.setStatus(_A)
class _SwL2IGMPCtrlVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPCtrlVid_Type.__name__=_B
_SwL2IGMPCtrlVid_Object=MibTableColumn
swL2IGMPCtrlVid=_SwL2IGMPCtrlVid_Object((1,3,6,1,4,1,171,11,70,2,2,11,3,1,1),_SwL2IGMPCtrlVid_Type())
swL2IGMPCtrlVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPCtrlVid.setStatus(_A)
class _SwL2IGMPQueryInterval_Type(Integer32):defaultValue=125;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2IGMPQueryInterval_Type.__name__=_B
_SwL2IGMPQueryInterval_Object=MibTableColumn
swL2IGMPQueryInterval=_SwL2IGMPQueryInterval_Object((1,3,6,1,4,1,171,11,70,2,2,11,3,1,2),_SwL2IGMPQueryInterval_Type())
swL2IGMPQueryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPQueryInterval.setStatus(_A)
class _SwL2IGMPMaxResponseTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_SwL2IGMPMaxResponseTime_Type.__name__=_B
_SwL2IGMPMaxResponseTime_Object=MibTableColumn
swL2IGMPMaxResponseTime=_SwL2IGMPMaxResponseTime_Object((1,3,6,1,4,1,171,11,70,2,2,11,3,1,3),_SwL2IGMPMaxResponseTime_Type())
swL2IGMPMaxResponseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMaxResponseTime.setStatus(_A)
class _SwL2IGMPRobustness_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2IGMPRobustness_Type.__name__=_B
_SwL2IGMPRobustness_Object=MibTableColumn
swL2IGMPRobustness=_SwL2IGMPRobustness_Object((1,3,6,1,4,1,171,11,70,2,2,11,3,1,4),_SwL2IGMPRobustness_Type())
swL2IGMPRobustness.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPRobustness.setStatus(_A)
class _SwL2IGMPLastMemberQueryInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_SwL2IGMPLastMemberQueryInterval_Type.__name__=_B
_SwL2IGMPLastMemberQueryInterval_Object=MibTableColumn
swL2IGMPLastMemberQueryInterval=_SwL2IGMPLastMemberQueryInterval_Object((1,3,6,1,4,1,171,11,70,2,2,11,3,1,5),_SwL2IGMPLastMemberQueryInterval_Type())
swL2IGMPLastMemberQueryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPLastMemberQueryInterval.setStatus(_A)
class _SwL2IGMPHostTimeout_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16711450))
_SwL2IGMPHostTimeout_Type.__name__=_B
_SwL2IGMPHostTimeout_Object=MibTableColumn
swL2IGMPHostTimeout=_SwL2IGMPHostTimeout_Object((1,3,6,1,4,1,171,11,70,2,2,11,3,1,6),_SwL2IGMPHostTimeout_Type())
swL2IGMPHostTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPHostTimeout.setStatus(_A)
class _SwL2IGMPRouteTimeout_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16711450))
_SwL2IGMPRouteTimeout_Type.__name__=_B
_SwL2IGMPRouteTimeout_Object=MibTableColumn
swL2IGMPRouteTimeout=_SwL2IGMPRouteTimeout_Object((1,3,6,1,4,1,171,11,70,2,2,11,3,1,7),_SwL2IGMPRouteTimeout_Type())
swL2IGMPRouteTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPRouteTimeout.setStatus(_A)
class _SwL2IGMPLeaveTimer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16711450))
_SwL2IGMPLeaveTimer_Type.__name__=_B
_SwL2IGMPLeaveTimer_Object=MibTableColumn
swL2IGMPLeaveTimer=_SwL2IGMPLeaveTimer_Object((1,3,6,1,4,1,171,11,70,2,2,11,3,1,8),_SwL2IGMPLeaveTimer_Type())
swL2IGMPLeaveTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPLeaveTimer.setStatus(_A)
class _SwL2IGMPQueryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2IGMPQueryState_Type.__name__=_B
_SwL2IGMPQueryState_Object=MibTableColumn
swL2IGMPQueryState=_SwL2IGMPQueryState_Object((1,3,6,1,4,1,171,11,70,2,2,11,3,1,9),_SwL2IGMPQueryState_Type())
swL2IGMPQueryState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPQueryState.setStatus(_A)
class _SwL2IGMPCurrentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('querier',2),('non-querier',3)))
_SwL2IGMPCurrentState_Type.__name__=_B
_SwL2IGMPCurrentState_Object=MibTableColumn
swL2IGMPCurrentState=_SwL2IGMPCurrentState_Object((1,3,6,1,4,1,171,11,70,2,2,11,3,1,10),_SwL2IGMPCurrentState_Type())
swL2IGMPCurrentState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPCurrentState.setStatus(_A)
class _SwL2IGMPCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_R,2),(_Q,3)))
_SwL2IGMPCtrlState_Type.__name__=_B
_SwL2IGMPCtrlState_Object=MibTableColumn
swL2IGMPCtrlState=_SwL2IGMPCtrlState_Object((1,3,6,1,4,1,171,11,70,2,2,11,3,1,11),_SwL2IGMPCtrlState_Type())
swL2IGMPCtrlState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPCtrlState.setStatus(_A)
class _SwL2IGMPFastLeaveState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_R,2),(_Q,3)))
_SwL2IGMPFastLeaveState_Type.__name__=_B
_SwL2IGMPFastLeaveState_Object=MibTableColumn
swL2IGMPFastLeaveState=_SwL2IGMPFastLeaveState_Object((1,3,6,1,4,1,171,11,70,2,2,11,3,1,12),_SwL2IGMPFastLeaveState_Type())
swL2IGMPFastLeaveState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPFastLeaveState.setStatus(_A)
class _SwL2IGMPQueryVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_SwL2IGMPQueryVersion_Type.__name__=_B
_SwL2IGMPQueryVersion_Object=MibTableColumn
swL2IGMPQueryVersion=_SwL2IGMPQueryVersion_Object((1,3,6,1,4,1,171,11,70,2,2,11,3,1,13),_SwL2IGMPQueryVersion_Type())
swL2IGMPQueryVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPQueryVersion.setStatus(_A)
class _SwL2IGMPReportSuppression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2IGMPReportSuppression_Type.__name__=_B
_SwL2IGMPReportSuppression_Object=MibTableColumn
swL2IGMPReportSuppression=_SwL2IGMPReportSuppression_Object((1,3,6,1,4,1,171,11,70,2,2,11,3,1,15),_SwL2IGMPReportSuppression_Type())
swL2IGMPReportSuppression.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPReportSuppression.setStatus(_A)
class _SwL2IGMPDataDrivenLearningState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2IGMPDataDrivenLearningState_Type.__name__=_B
_SwL2IGMPDataDrivenLearningState_Object=MibTableColumn
swL2IGMPDataDrivenLearningState=_SwL2IGMPDataDrivenLearningState_Object((1,3,6,1,4,1,171,11,70,2,2,11,3,1,16),_SwL2IGMPDataDrivenLearningState_Type())
swL2IGMPDataDrivenLearningState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPDataDrivenLearningState.setStatus(_A)
class _SwL2IGMPDataDrivenLearningAgedOutState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2IGMPDataDrivenLearningAgedOutState_Type.__name__=_B
_SwL2IGMPDataDrivenLearningAgedOutState_Object=MibTableColumn
swL2IGMPDataDrivenLearningAgedOutState=_SwL2IGMPDataDrivenLearningAgedOutState_Object((1,3,6,1,4,1,171,11,70,2,2,11,3,1,17),_SwL2IGMPDataDrivenLearningAgedOutState_Type())
swL2IGMPDataDrivenLearningAgedOutState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPDataDrivenLearningAgedOutState.setStatus(_A)
class _SwL2IGMPDataDrivenGroupExpiryTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2IGMPDataDrivenGroupExpiryTime_Type.__name__=_B
_SwL2IGMPDataDrivenGroupExpiryTime_Object=MibTableColumn
swL2IGMPDataDrivenGroupExpiryTime=_SwL2IGMPDataDrivenGroupExpiryTime_Object((1,3,6,1,4,1,171,11,70,2,2,11,3,1,18),_SwL2IGMPDataDrivenGroupExpiryTime_Type())
swL2IGMPDataDrivenGroupExpiryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPDataDrivenGroupExpiryTime.setStatus(_A)
_SwL2IGMPQueryInfoTable_Object=MibTable
swL2IGMPQueryInfoTable=_SwL2IGMPQueryInfoTable_Object((1,3,6,1,4,1,171,11,70,2,2,11,4))
if mibBuilder.loadTexts:swL2IGMPQueryInfoTable.setStatus(_A)
_SwL2IGMPQueryInfoEntry_Object=MibTableRow
swL2IGMPQueryInfoEntry=_SwL2IGMPQueryInfoEntry_Object((1,3,6,1,4,1,171,11,70,2,2,11,4,1))
swL2IGMPQueryInfoEntry.setIndexNames((0,_E,_y))
if mibBuilder.loadTexts:swL2IGMPQueryInfoEntry.setStatus(_A)
class _SwL2IGMPInfoVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPInfoVid_Type.__name__=_B
_SwL2IGMPInfoVid_Object=MibTableColumn
swL2IGMPInfoVid=_SwL2IGMPInfoVid_Object((1,3,6,1,4,1,171,11,70,2,2,11,4,1,1),_SwL2IGMPInfoVid_Type())
swL2IGMPInfoVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPInfoVid.setStatus(_A)
class _SwL2IGMPInfoQueryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPInfoQueryCount_Type.__name__=_B
_SwL2IGMPInfoQueryCount_Object=MibTableColumn
swL2IGMPInfoQueryCount=_SwL2IGMPInfoQueryCount_Object((1,3,6,1,4,1,171,11,70,2,2,11,4,1,2),_SwL2IGMPInfoQueryCount_Type())
swL2IGMPInfoQueryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPInfoQueryCount.setStatus(_A)
class _SwL2IGMPInfoTxQueryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPInfoTxQueryCount_Type.__name__=_B
_SwL2IGMPInfoTxQueryCount_Object=MibTableColumn
swL2IGMPInfoTxQueryCount=_SwL2IGMPInfoTxQueryCount_Object((1,3,6,1,4,1,171,11,70,2,2,11,4,1,3),_SwL2IGMPInfoTxQueryCount_Type())
swL2IGMPInfoTxQueryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPInfoTxQueryCount.setStatus(_A)
_SwL2IGMPInfoTable_Object=MibTable
swL2IGMPInfoTable=_SwL2IGMPInfoTable_Object((1,3,6,1,4,1,171,11,70,2,2,11,5))
if mibBuilder.loadTexts:swL2IGMPInfoTable.setStatus(_A)
_SwL2IGMPInfoEntry_Object=MibTableRow
swL2IGMPInfoEntry=_SwL2IGMPInfoEntry_Object((1,3,6,1,4,1,171,11,70,2,2,11,5,1))
swL2IGMPInfoEntry.setIndexNames((0,_E,_z),(0,_E,_A0))
if mibBuilder.loadTexts:swL2IGMPInfoEntry.setStatus(_A)
class _SwL2IGMPVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPVid_Type.__name__=_B
_SwL2IGMPVid_Object=MibTableColumn
swL2IGMPVid=_SwL2IGMPVid_Object((1,3,6,1,4,1,171,11,70,2,2,11,5,1,1),_SwL2IGMPVid_Type())
swL2IGMPVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPVid.setStatus(_A)
_SwL2IGMPGroupIpAddr_Type=IpAddress
_SwL2IGMPGroupIpAddr_Object=MibTableColumn
swL2IGMPGroupIpAddr=_SwL2IGMPGroupIpAddr_Object((1,3,6,1,4,1,171,11,70,2,2,11,5,1,2),_SwL2IGMPGroupIpAddr_Type())
swL2IGMPGroupIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPGroupIpAddr.setStatus(_A)
_SwL2IGMPMacAddr_Type=MacAddress
_SwL2IGMPMacAddr_Object=MibTableColumn
swL2IGMPMacAddr=_SwL2IGMPMacAddr_Object((1,3,6,1,4,1,171,11,70,2,2,11,5,1,3),_SwL2IGMPMacAddr_Type())
swL2IGMPMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMacAddr.setStatus(_A)
_SwL2IGMPPortMap_Type=PortList
_SwL2IGMPPortMap_Object=MibTableColumn
swL2IGMPPortMap=_SwL2IGMPPortMap_Object((1,3,6,1,4,1,171,11,70,2,2,11,5,1,4),_SwL2IGMPPortMap_Type())
swL2IGMPPortMap.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPPortMap.setStatus(_A)
class _SwL2IGMPIpGroupReportCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPIpGroupReportCount_Type.__name__=_B
_SwL2IGMPIpGroupReportCount_Object=MibTableColumn
swL2IGMPIpGroupReportCount=_SwL2IGMPIpGroupReportCount_Object((1,3,6,1,4,1,171,11,70,2,2,11,5,1,5),_SwL2IGMPIpGroupReportCount_Type())
swL2IGMPIpGroupReportCount.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPIpGroupReportCount.setStatus(_A)
_SwL2IGMPRouterPortsTable_Object=MibTable
swL2IGMPRouterPortsTable=_SwL2IGMPRouterPortsTable_Object((1,3,6,1,4,1,171,11,70,2,2,11,6))
if mibBuilder.loadTexts:swL2IGMPRouterPortsTable.setStatus(_A)
_SwL2IGMPRouterPortsEntry_Object=MibTableRow
swL2IGMPRouterPortsEntry=_SwL2IGMPRouterPortsEntry_Object((1,3,6,1,4,1,171,11,70,2,2,11,6,1))
swL2IGMPRouterPortsEntry.setIndexNames((0,_E,_A1))
if mibBuilder.loadTexts:swL2IGMPRouterPortsEntry.setStatus(_A)
class _SwL2IGMPRouterPortsVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPRouterPortsVid_Type.__name__=_B
_SwL2IGMPRouterPortsVid_Object=MibTableColumn
swL2IGMPRouterPortsVid=_SwL2IGMPRouterPortsVid_Object((1,3,6,1,4,1,171,11,70,2,2,11,6,1,1),_SwL2IGMPRouterPortsVid_Type())
swL2IGMPRouterPortsVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRouterPortsVid.setStatus(_A)
_SwL2IGMPRouterStaticPortList_Type=PortList
_SwL2IGMPRouterStaticPortList_Object=MibTableColumn
swL2IGMPRouterStaticPortList=_SwL2IGMPRouterStaticPortList_Object((1,3,6,1,4,1,171,11,70,2,2,11,6,1,2),_SwL2IGMPRouterStaticPortList_Type())
swL2IGMPRouterStaticPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPRouterStaticPortList.setStatus(_A)
_SwL2IGMPRouterDynamicPortList_Type=PortList
_SwL2IGMPRouterDynamicPortList_Object=MibTableColumn
swL2IGMPRouterDynamicPortList=_SwL2IGMPRouterDynamicPortList_Object((1,3,6,1,4,1,171,11,70,2,2,11,6,1,3),_SwL2IGMPRouterDynamicPortList_Type())
swL2IGMPRouterDynamicPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRouterDynamicPortList.setStatus(_A)
_SwL2IGMPRouterForbiddenPortList_Type=PortList
_SwL2IGMPRouterForbiddenPortList_Object=MibTableColumn
swL2IGMPRouterForbiddenPortList=_SwL2IGMPRouterForbiddenPortList_Object((1,3,6,1,4,1,171,11,70,2,2,11,6,1,4),_SwL2IGMPRouterForbiddenPortList_Type())
swL2IGMPRouterForbiddenPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPRouterForbiddenPortList.setStatus(_A)
_SwL2IGMPMulticastVlanTable_Object=MibTable
swL2IGMPMulticastVlanTable=_SwL2IGMPMulticastVlanTable_Object((1,3,6,1,4,1,171,11,70,2,2,11,7))
if mibBuilder.loadTexts:swL2IGMPMulticastVlanTable.setStatus(_A)
_SwL2IGMPMulticastVlanEntry_Object=MibTableRow
swL2IGMPMulticastVlanEntry=_SwL2IGMPMulticastVlanEntry_Object((1,3,6,1,4,1,171,11,70,2,2,11,7,1))
swL2IGMPMulticastVlanEntry.setIndexNames((0,_E,_A2))
if mibBuilder.loadTexts:swL2IGMPMulticastVlanEntry.setStatus(_A)
class _SwL2IGMPMulticastVlanid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_SwL2IGMPMulticastVlanid_Type.__name__=_B
_SwL2IGMPMulticastVlanid_Object=MibTableColumn
swL2IGMPMulticastVlanid=_SwL2IGMPMulticastVlanid_Object((1,3,6,1,4,1,171,11,70,2,2,11,7,1,1),_SwL2IGMPMulticastVlanid_Type())
swL2IGMPMulticastVlanid.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanid.setStatus(_A)
class _SwL2IGMPMulticastVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL2IGMPMulticastVlanName_Type.__name__=_I
_SwL2IGMPMulticastVlanName_Object=MibTableColumn
swL2IGMPMulticastVlanName=_SwL2IGMPMulticastVlanName_Object((1,3,6,1,4,1,171,11,70,2,2,11,7,1,2),_SwL2IGMPMulticastVlanName_Type())
swL2IGMPMulticastVlanName.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanName.setStatus(_A)
_SwL2IGMPMulticastVlanSourcePort_Type=PortList
_SwL2IGMPMulticastVlanSourcePort_Object=MibTableColumn
swL2IGMPMulticastVlanSourcePort=_SwL2IGMPMulticastVlanSourcePort_Object((1,3,6,1,4,1,171,11,70,2,2,11,7,1,3),_SwL2IGMPMulticastVlanSourcePort_Type())
swL2IGMPMulticastVlanSourcePort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanSourcePort.setStatus(_A)
_SwL2IGMPMulticastVlanMemberPort_Type=PortList
_SwL2IGMPMulticastVlanMemberPort_Object=MibTableColumn
swL2IGMPMulticastVlanMemberPort=_SwL2IGMPMulticastVlanMemberPort_Object((1,3,6,1,4,1,171,11,70,2,2,11,7,1,4),_SwL2IGMPMulticastVlanMemberPort_Type())
swL2IGMPMulticastVlanMemberPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanMemberPort.setStatus(_A)
_SwL2IGMPMulticastVlanTagMemberPort_Type=PortList
_SwL2IGMPMulticastVlanTagMemberPort_Object=MibTableColumn
swL2IGMPMulticastVlanTagMemberPort=_SwL2IGMPMulticastVlanTagMemberPort_Object((1,3,6,1,4,1,171,11,70,2,2,11,7,1,5),_SwL2IGMPMulticastVlanTagMemberPort_Type())
swL2IGMPMulticastVlanTagMemberPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanTagMemberPort.setStatus(_A)
class _SwL2IGMPMulticastVlanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2IGMPMulticastVlanState_Type.__name__=_B
_SwL2IGMPMulticastVlanState_Object=MibTableColumn
swL2IGMPMulticastVlanState=_SwL2IGMPMulticastVlanState_Object((1,3,6,1,4,1,171,11,70,2,2,11,7,1,6),_SwL2IGMPMulticastVlanState_Type())
swL2IGMPMulticastVlanState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanState.setStatus(_A)
_SwL2IGMPMulticastVlanReplaceSourceIp_Type=IpAddress
_SwL2IGMPMulticastVlanReplaceSourceIp_Object=MibTableColumn
swL2IGMPMulticastVlanReplaceSourceIp=_SwL2IGMPMulticastVlanReplaceSourceIp_Object((1,3,6,1,4,1,171,11,70,2,2,11,7,1,7),_SwL2IGMPMulticastVlanReplaceSourceIp_Type())
swL2IGMPMulticastVlanReplaceSourceIp.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanReplaceSourceIp.setStatus(_A)
_SwL2IGMPMulticastVlanRowStatus_Type=RowStatus
_SwL2IGMPMulticastVlanRowStatus_Object=MibTableColumn
swL2IGMPMulticastVlanRowStatus=_SwL2IGMPMulticastVlanRowStatus_Object((1,3,6,1,4,1,171,11,70,2,2,11,7,1,8),_SwL2IGMPMulticastVlanRowStatus_Type())
swL2IGMPMulticastVlanRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanRowStatus.setStatus(_A)
class _SwL2IGMPMulticastVlanRemoveAllMcastAddrListAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_N,2)))
_SwL2IGMPMulticastVlanRemoveAllMcastAddrListAction_Type.__name__=_B
_SwL2IGMPMulticastVlanRemoveAllMcastAddrListAction_Object=MibTableColumn
swL2IGMPMulticastVlanRemoveAllMcastAddrListAction=_SwL2IGMPMulticastVlanRemoveAllMcastAddrListAction_Object((1,3,6,1,4,1,171,11,70,2,2,11,7,1,9),_SwL2IGMPMulticastVlanRemoveAllMcastAddrListAction_Type())
swL2IGMPMulticastVlanRemoveAllMcastAddrListAction.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanRemoveAllMcastAddrListAction.setStatus(_A)
_SwL2IGMPMulticastVlanUntagSourcePort_Type=PortList
_SwL2IGMPMulticastVlanUntagSourcePort_Object=MibTableColumn
swL2IGMPMulticastVlanUntagSourcePort=_SwL2IGMPMulticastVlanUntagSourcePort_Object((1,3,6,1,4,1,171,11,70,2,2,11,7,1,10),_SwL2IGMPMulticastVlanUntagSourcePort_Type())
swL2IGMPMulticastVlanUntagSourcePort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanUntagSourcePort.setStatus(_A)
class _SwL2IGMPMulticastVlanRemapPriority_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_SwL2IGMPMulticastVlanRemapPriority_Type.__name__=_B
_SwL2IGMPMulticastVlanRemapPriority_Object=MibTableColumn
swL2IGMPMulticastVlanRemapPriority=_SwL2IGMPMulticastVlanRemapPriority_Object((1,3,6,1,4,1,171,11,70,2,2,11,7,1,11),_SwL2IGMPMulticastVlanRemapPriority_Type())
swL2IGMPMulticastVlanRemapPriority.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanRemapPriority.setStatus(_A)
class _SwL2IGMPMulticastVlanReplacePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_SwL2IGMPMulticastVlanReplacePriority_Type.__name__=_B
_SwL2IGMPMulticastVlanReplacePriority_Object=MibTableColumn
swL2IGMPMulticastVlanReplacePriority=_SwL2IGMPMulticastVlanReplacePriority_Object((1,3,6,1,4,1,171,11,70,2,2,11,7,1,12),_SwL2IGMPMulticastVlanReplacePriority_Type())
swL2IGMPMulticastVlanReplacePriority.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanReplacePriority.setStatus(_A)
_SwL2IGMPMulticastVlanGroupTable_Object=MibTable
swL2IGMPMulticastVlanGroupTable=_SwL2IGMPMulticastVlanGroupTable_Object((1,3,6,1,4,1,171,11,70,2,2,11,8))
if mibBuilder.loadTexts:swL2IGMPMulticastVlanGroupTable.setStatus(_A)
_SwL2IGMPMulticastVlanGroupEntry_Object=MibTableRow
swL2IGMPMulticastVlanGroupEntry=_SwL2IGMPMulticastVlanGroupEntry_Object((1,3,6,1,4,1,171,11,70,2,2,11,8,1))
swL2IGMPMulticastVlanGroupEntry.setIndexNames((0,_E,_A3),(0,_E,_A4),(0,_E,_A5))
if mibBuilder.loadTexts:swL2IGMPMulticastVlanGroupEntry.setStatus(_A)
class _SwL2IGMPMulticastVlanGroupVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPMulticastVlanGroupVid_Type.__name__=_B
_SwL2IGMPMulticastVlanGroupVid_Object=MibTableColumn
swL2IGMPMulticastVlanGroupVid=_SwL2IGMPMulticastVlanGroupVid_Object((1,3,6,1,4,1,171,11,70,2,2,11,8,1,1),_SwL2IGMPMulticastVlanGroupVid_Type())
swL2IGMPMulticastVlanGroupVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanGroupVid.setStatus(_A)
_SwL2IGMPMulticastVlanGroupFromIp_Type=IpAddress
_SwL2IGMPMulticastVlanGroupFromIp_Object=MibTableColumn
swL2IGMPMulticastVlanGroupFromIp=_SwL2IGMPMulticastVlanGroupFromIp_Object((1,3,6,1,4,1,171,11,70,2,2,11,8,1,2),_SwL2IGMPMulticastVlanGroupFromIp_Type())
swL2IGMPMulticastVlanGroupFromIp.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanGroupFromIp.setStatus(_A)
_SwL2IGMPMulticastVlanGroupToIp_Type=IpAddress
_SwL2IGMPMulticastVlanGroupToIp_Object=MibTableColumn
swL2IGMPMulticastVlanGroupToIp=_SwL2IGMPMulticastVlanGroupToIp_Object((1,3,6,1,4,1,171,11,70,2,2,11,8,1,3),_SwL2IGMPMulticastVlanGroupToIp_Type())
swL2IGMPMulticastVlanGroupToIp.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanGroupToIp.setStatus(_A)
_SwL2IGMPMulticastVlanGroupStatus_Type=RowStatus
_SwL2IGMPMulticastVlanGroupStatus_Object=MibTableColumn
swL2IGMPMulticastVlanGroupStatus=_SwL2IGMPMulticastVlanGroupStatus_Object((1,3,6,1,4,1,171,11,70,2,2,11,8,1,4),_SwL2IGMPMulticastVlanGroupStatus_Type())
swL2IGMPMulticastVlanGroupStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2IGMPMulticastVlanGroupStatus.setStatus(_A)
_SwIGMPSnoopingGroupTable_Object=MibTable
swIGMPSnoopingGroupTable=_SwIGMPSnoopingGroupTable_Object((1,3,6,1,4,1,171,11,70,2,2,11,11))
if mibBuilder.loadTexts:swIGMPSnoopingGroupTable.setStatus(_A)
_SwIGMPSnoopingGroupEntry_Object=MibTableRow
swIGMPSnoopingGroupEntry=_SwIGMPSnoopingGroupEntry_Object((1,3,6,1,4,1,171,11,70,2,2,11,11,1))
swIGMPSnoopingGroupEntry.setIndexNames((0,_E,_A6),(0,_E,_A7),(0,_E,_A8))
if mibBuilder.loadTexts:swIGMPSnoopingGroupEntry.setStatus(_A)
class _SwIGMPSnoopingGroupVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwIGMPSnoopingGroupVid_Type.__name__=_B
_SwIGMPSnoopingGroupVid_Object=MibTableColumn
swIGMPSnoopingGroupVid=_SwIGMPSnoopingGroupVid_Object((1,3,6,1,4,1,171,11,70,2,2,11,11,1,1),_SwIGMPSnoopingGroupVid_Type())
swIGMPSnoopingGroupVid.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPSnoopingGroupVid.setStatus(_A)
_SwIGMPSnoopingGroupGroupAddr_Type=IpAddress
_SwIGMPSnoopingGroupGroupAddr_Object=MibTableColumn
swIGMPSnoopingGroupGroupAddr=_SwIGMPSnoopingGroupGroupAddr_Object((1,3,6,1,4,1,171,11,70,2,2,11,11,1,2),_SwIGMPSnoopingGroupGroupAddr_Type())
swIGMPSnoopingGroupGroupAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPSnoopingGroupGroupAddr.setStatus(_A)
_SwIGMPSnoopingGroupSourceAddr_Type=IpAddress
_SwIGMPSnoopingGroupSourceAddr_Object=MibTableColumn
swIGMPSnoopingGroupSourceAddr=_SwIGMPSnoopingGroupSourceAddr_Object((1,3,6,1,4,1,171,11,70,2,2,11,11,1,3),_SwIGMPSnoopingGroupSourceAddr_Type())
swIGMPSnoopingGroupSourceAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPSnoopingGroupSourceAddr.setStatus(_A)
_SwIGMPSnoopingGroupIncludePortMap_Type=PortList
_SwIGMPSnoopingGroupIncludePortMap_Object=MibTableColumn
swIGMPSnoopingGroupIncludePortMap=_SwIGMPSnoopingGroupIncludePortMap_Object((1,3,6,1,4,1,171,11,70,2,2,11,11,1,4),_SwIGMPSnoopingGroupIncludePortMap_Type())
swIGMPSnoopingGroupIncludePortMap.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPSnoopingGroupIncludePortMap.setStatus(_A)
_SwIGMPSnoopingGroupExcludePortMap_Type=PortList
_SwIGMPSnoopingGroupExcludePortMap_Object=MibTableColumn
swIGMPSnoopingGroupExcludePortMap=_SwIGMPSnoopingGroupExcludePortMap_Object((1,3,6,1,4,1,171,11,70,2,2,11,11,1,5),_SwIGMPSnoopingGroupExcludePortMap_Type())
swIGMPSnoopingGroupExcludePortMap.setMaxAccess(_C)
if mibBuilder.loadTexts:swIGMPSnoopingGroupExcludePortMap.setStatus(_A)
_SwL2IGMPSnoopingStaticGroupTable_Object=MibTable
swL2IGMPSnoopingStaticGroupTable=_SwL2IGMPSnoopingStaticGroupTable_Object((1,3,6,1,4,1,171,11,70,2,2,11,16))
if mibBuilder.loadTexts:swL2IGMPSnoopingStaticGroupTable.setStatus(_A)
_SwL2IGMPSnoopingStaticGroupEntry_Object=MibTableRow
swL2IGMPSnoopingStaticGroupEntry=_SwL2IGMPSnoopingStaticGroupEntry_Object((1,3,6,1,4,1,171,11,70,2,2,11,16,1))
swL2IGMPSnoopingStaticGroupEntry.setIndexNames((0,_E,_A9),(0,_E,_AA))
if mibBuilder.loadTexts:swL2IGMPSnoopingStaticGroupEntry.setStatus(_A)
class _SwL2IGMPSnoopingStaticGroupVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2IGMPSnoopingStaticGroupVID_Type.__name__=_B
_SwL2IGMPSnoopingStaticGroupVID_Object=MibTableColumn
swL2IGMPSnoopingStaticGroupVID=_SwL2IGMPSnoopingStaticGroupVID_Object((1,3,6,1,4,1,171,11,70,2,2,11,16,1,1),_SwL2IGMPSnoopingStaticGroupVID_Type())
swL2IGMPSnoopingStaticGroupVID.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPSnoopingStaticGroupVID.setStatus(_A)
_SwL2IGMPSnoopingStaticGroupIPaddress_Type=IpAddress
_SwL2IGMPSnoopingStaticGroupIPaddress_Object=MibTableColumn
swL2IGMPSnoopingStaticGroupIPaddress=_SwL2IGMPSnoopingStaticGroupIPaddress_Object((1,3,6,1,4,1,171,11,70,2,2,11,16,1,2),_SwL2IGMPSnoopingStaticGroupIPaddress_Type())
swL2IGMPSnoopingStaticGroupIPaddress.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPSnoopingStaticGroupIPaddress.setStatus(_A)
_SwL2IGMPSnoopingStaticGroupMemberPortList_Type=PortList
_SwL2IGMPSnoopingStaticGroupMemberPortList_Object=MibTableColumn
swL2IGMPSnoopingStaticGroupMemberPortList=_SwL2IGMPSnoopingStaticGroupMemberPortList_Object((1,3,6,1,4,1,171,11,70,2,2,11,16,1,3),_SwL2IGMPSnoopingStaticGroupMemberPortList_Type())
swL2IGMPSnoopingStaticGroupMemberPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPSnoopingStaticGroupMemberPortList.setStatus(_A)
_SwL2IGMPSnoopingStaticGroupRowStatus_Type=RowStatus
_SwL2IGMPSnoopingStaticGroupRowStatus_Object=MibTableColumn
swL2IGMPSnoopingStaticGroupRowStatus=_SwL2IGMPSnoopingStaticGroupRowStatus_Object((1,3,6,1,4,1,171,11,70,2,2,11,16,1,4),_SwL2IGMPSnoopingStaticGroupRowStatus_Type())
swL2IGMPSnoopingStaticGroupRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:swL2IGMPSnoopingStaticGroupRowStatus.setStatus(_A)
_SwL2IGMPSnoopingDataDrivenLearningGroupTable_Object=MibTable
swL2IGMPSnoopingDataDrivenLearningGroupTable=_SwL2IGMPSnoopingDataDrivenLearningGroupTable_Object((1,3,6,1,4,1,171,11,70,2,2,11,20))
if mibBuilder.loadTexts:swL2IGMPSnoopingDataDrivenLearningGroupTable.setStatus(_A)
_SwL2IGMPSnoopingDataDrivenLearningGroupEntry_Object=MibTableRow
swL2IGMPSnoopingDataDrivenLearningGroupEntry=_SwL2IGMPSnoopingDataDrivenLearningGroupEntry_Object((1,3,6,1,4,1,171,11,70,2,2,11,20,1))
swL2IGMPSnoopingDataDrivenLearningGroupEntry.setIndexNames((0,_E,_AB),(0,_E,_AC))
if mibBuilder.loadTexts:swL2IGMPSnoopingDataDrivenLearningGroupEntry.setStatus(_A)
class _SwL2IGMPSnoopingDataDrivenLearningGrpVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2IGMPSnoopingDataDrivenLearningGrpVID_Type.__name__=_B
_SwL2IGMPSnoopingDataDrivenLearningGrpVID_Object=MibTableColumn
swL2IGMPSnoopingDataDrivenLearningGrpVID=_SwL2IGMPSnoopingDataDrivenLearningGrpVID_Object((1,3,6,1,4,1,171,11,70,2,2,11,20,1,1),_SwL2IGMPSnoopingDataDrivenLearningGrpVID_Type())
swL2IGMPSnoopingDataDrivenLearningGrpVID.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPSnoopingDataDrivenLearningGrpVID.setStatus(_A)
_SwL2IGMPSnoopingDataDrivenLearningGrpGrpAddr_Type=IpAddress
_SwL2IGMPSnoopingDataDrivenLearningGrpGrpAddr_Object=MibTableColumn
swL2IGMPSnoopingDataDrivenLearningGrpGrpAddr=_SwL2IGMPSnoopingDataDrivenLearningGrpGrpAddr_Object((1,3,6,1,4,1,171,11,70,2,2,11,20,1,2),_SwL2IGMPSnoopingDataDrivenLearningGrpGrpAddr_Type())
swL2IGMPSnoopingDataDrivenLearningGrpGrpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPSnoopingDataDrivenLearningGrpGrpAddr.setStatus(_A)
_SwL2IGMPSnoopingDataDrivenLearningGrpRouterPorts_Type=PortList
_SwL2IGMPSnoopingDataDrivenLearningGrpRouterPorts_Object=MibTableColumn
swL2IGMPSnoopingDataDrivenLearningGrpRouterPorts=_SwL2IGMPSnoopingDataDrivenLearningGrpRouterPorts_Object((1,3,6,1,4,1,171,11,70,2,2,11,20,1,3),_SwL2IGMPSnoopingDataDrivenLearningGrpRouterPorts_Type())
swL2IGMPSnoopingDataDrivenLearningGrpRouterPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPSnoopingDataDrivenLearningGrpRouterPorts.setStatus(_A)
class _SwL2IGMPSnoopingDataDrivenLearningGrpClearGrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('clear',2)))
_SwL2IGMPSnoopingDataDrivenLearningGrpClearGrp_Type.__name__=_B
_SwL2IGMPSnoopingDataDrivenLearningGrpClearGrp_Object=MibTableColumn
swL2IGMPSnoopingDataDrivenLearningGrpClearGrp=_SwL2IGMPSnoopingDataDrivenLearningGrpClearGrp_Object((1,3,6,1,4,1,171,11,70,2,2,11,20,1,100),_SwL2IGMPSnoopingDataDrivenLearningGrpClearGrp_Type())
swL2IGMPSnoopingDataDrivenLearningGrpClearGrp.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPSnoopingDataDrivenLearningGrpClearGrp.setStatus(_A)
_SwL2TrafficSegMgmt_ObjectIdentity=ObjectIdentity
swL2TrafficSegMgmt=_SwL2TrafficSegMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,14))
_SwL2TrafficSegTable_Object=MibTable
swL2TrafficSegTable=_SwL2TrafficSegTable_Object((1,3,6,1,4,1,171,11,70,2,2,14,1))
if mibBuilder.loadTexts:swL2TrafficSegTable.setStatus(_A)
_SwL2TrafficSegEntry_Object=MibTableRow
swL2TrafficSegEntry=_SwL2TrafficSegEntry_Object((1,3,6,1,4,1,171,11,70,2,2,14,1,1))
swL2TrafficSegEntry.setIndexNames((0,_E,_AD))
if mibBuilder.loadTexts:swL2TrafficSegEntry.setStatus(_A)
class _SwL2TrafficSegPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrafficSegPort_Type.__name__=_B
_SwL2TrafficSegPort_Object=MibTableColumn
swL2TrafficSegPort=_SwL2TrafficSegPort_Object((1,3,6,1,4,1,171,11,70,2,2,14,1,1,1),_SwL2TrafficSegPort_Type())
swL2TrafficSegPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrafficSegPort.setStatus(_A)
_SwL2TrafficSegForwardPorts_Type=PortList
_SwL2TrafficSegForwardPorts_Object=MibTableColumn
swL2TrafficSegForwardPorts=_SwL2TrafficSegForwardPorts_Object((1,3,6,1,4,1,171,11,70,2,2,14,1,1,2),_SwL2TrafficSegForwardPorts_Type())
swL2TrafficSegForwardPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrafficSegForwardPorts.setStatus(_A)
_SwL2IpLimitedMulticastMgmt_ObjectIdentity=ObjectIdentity
swL2IpLimitedMulticastMgmt=_SwL2IpLimitedMulticastMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,15))
_SwL2IpLimitedMulticastTable_Object=MibTable
swL2IpLimitedMulticastTable=_SwL2IpLimitedMulticastTable_Object((1,3,6,1,4,1,171,11,70,2,2,15,1))
if mibBuilder.loadTexts:swL2IpLimitedMulticastTable.setStatus(_A)
_SwL2IpLimitedMulticastEntry_Object=MibTableRow
swL2IpLimitedMulticastEntry=_SwL2IpLimitedMulticastEntry_Object((1,3,6,1,4,1,171,11,70,2,2,15,1,1))
swL2IpLimitedMulticastEntry.setIndexNames((0,_E,_AE))
if mibBuilder.loadTexts:swL2IpLimitedMulticastEntry.setStatus(_A)
class _SwL2IpLimitedMulticastPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IpLimitedMulticastPortIndex_Type.__name__=_B
_SwL2IpLimitedMulticastPortIndex_Object=MibTableColumn
swL2IpLimitedMulticastPortIndex=_SwL2IpLimitedMulticastPortIndex_Object((1,3,6,1,4,1,171,11,70,2,2,15,1,1,1),_SwL2IpLimitedMulticastPortIndex_Type())
swL2IpLimitedMulticastPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IpLimitedMulticastPortIndex.setStatus(_A)
_SwL2IpLimitedMulticastHead_Type=IpAddress
_SwL2IpLimitedMulticastHead_Object=MibTableColumn
swL2IpLimitedMulticastHead=_SwL2IpLimitedMulticastHead_Object((1,3,6,1,4,1,171,11,70,2,2,15,1,1,2),_SwL2IpLimitedMulticastHead_Type())
swL2IpLimitedMulticastHead.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IpLimitedMulticastHead.setStatus(_A)
_SwL2IpLimitedMulticastTail_Type=IpAddress
_SwL2IpLimitedMulticastTail_Object=MibTableColumn
swL2IpLimitedMulticastTail=_SwL2IpLimitedMulticastTail_Object((1,3,6,1,4,1,171,11,70,2,2,15,1,1,3),_SwL2IpLimitedMulticastTail_Type())
swL2IpLimitedMulticastTail.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IpLimitedMulticastTail.setStatus(_A)
class _SwL2IpLimitedMulticastAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),('permit',1),('deny',2)))
_SwL2IpLimitedMulticastAccess_Type.__name__=_B
_SwL2IpLimitedMulticastAccess_Object=MibTableColumn
swL2IpLimitedMulticastAccess=_SwL2IpLimitedMulticastAccess_Object((1,3,6,1,4,1,171,11,70,2,2,15,1,1,4),_SwL2IpLimitedMulticastAccess_Type())
swL2IpLimitedMulticastAccess.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IpLimitedMulticastAccess.setStatus(_A)
class _SwL2IpLimitedMulticastState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2IpLimitedMulticastState_Type.__name__=_B
_SwL2IpLimitedMulticastState_Object=MibTableColumn
swL2IpLimitedMulticastState=_SwL2IpLimitedMulticastState_Object((1,3,6,1,4,1,171,11,70,2,2,15,1,1,5),_SwL2IpLimitedMulticastState_Type())
swL2IpLimitedMulticastState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IpLimitedMulticastState.setStatus(_A)
class _SwL2IpLimitedMulticastDelState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_SwL2IpLimitedMulticastDelState_Type.__name__=_B
_SwL2IpLimitedMulticastDelState_Object=MibTableColumn
swL2IpLimitedMulticastDelState=_SwL2IpLimitedMulticastDelState_Object((1,3,6,1,4,1,171,11,70,2,2,15,1,1,6),_SwL2IpLimitedMulticastDelState_Type())
swL2IpLimitedMulticastDelState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IpLimitedMulticastDelState.setStatus(_A)
_SwL2MgmtMIBTraps_ObjectIdentity=ObjectIdentity
swL2MgmtMIBTraps=_SwL2MgmtMIBTraps_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,16))
_SwL2Notify_ObjectIdentity=ObjectIdentity
swL2Notify=_SwL2Notify_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,16,1))
_SwL2NotifyPrefix_ObjectIdentity=ObjectIdentity
swL2NotifyPrefix=_SwL2NotifyPrefix_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,16,1,2))
_SwL2NotifFirmware_ObjectIdentity=ObjectIdentity
swL2NotifFirmware=_SwL2NotifFirmware_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,16,1,2,0))
_SwL2LoopDetectedNotify_ObjectIdentity=ObjectIdentity
swL2LoopDetectedNotify=_SwL2LoopDetectedNotify_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,16,1,2,0,0))
_Swl2NotificationBidings_ObjectIdentity=ObjectIdentity
swl2NotificationBidings=_Swl2NotificationBidings_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,16,1,2,1))
class _SwL2macNotifyInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_SwL2macNotifyInfo_Type.__name__=_M
_SwL2macNotifyInfo_Object=MibScalar
swL2macNotifyInfo=_SwL2macNotifyInfo_Object((1,3,6,1,4,1,171,11,70,2,2,16,1,2,1,1),_SwL2macNotifyInfo_Type())
swL2macNotifyInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2macNotifyInfo.setStatus(_A)
_SwL2VlanLoopDetectVID_Type=Integer32
_SwL2VlanLoopDetectVID_Object=MibScalar
swL2VlanLoopDetectVID=_SwL2VlanLoopDetectVID_Object((1,3,6,1,4,1,171,11,70,2,2,16,1,2,1,3),_SwL2VlanLoopDetectVID_Type())
swL2VlanLoopDetectVID.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:swL2VlanLoopDetectVID.setStatus(_A)
_SwL2VlanMgmt_ObjectIdentity=ObjectIdentity
swL2VlanMgmt=_SwL2VlanMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,17))
_SwL2VlanTable_Object=MibTable
swL2VlanTable=_SwL2VlanTable_Object((1,3,6,1,4,1,171,11,70,2,2,17,1))
if mibBuilder.loadTexts:swL2VlanTable.setStatus(_A)
_SwL2VlanEntry_Object=MibTableRow
swL2VlanEntry=_SwL2VlanEntry_Object((1,3,6,1,4,1,171,11,70,2,2,17,1,1))
swL2VlanEntry.setIndexNames((0,_E,_AF))
if mibBuilder.loadTexts:swL2VlanEntry.setStatus(_A)
_SwL2VlanIndex_Type=VlanId
_SwL2VlanIndex_Object=MibTableColumn
swL2VlanIndex=_SwL2VlanIndex_Object((1,3,6,1,4,1,171,11,70,2,2,17,1,1,1),_SwL2VlanIndex_Type())
swL2VlanIndex.setMaxAccess(_w)
if mibBuilder.loadTexts:swL2VlanIndex.setStatus(_A)
class _SwL2VlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL2VlanName_Type.__name__=_I
_SwL2VlanName_Object=MibTableColumn
swL2VlanName=_SwL2VlanName_Object((1,3,6,1,4,1,171,11,70,2,2,17,1,1,2),_SwL2VlanName_Type())
swL2VlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2VlanName.setStatus(_A)
class _SwL2VlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('invalid-vlan-type',0),('static-1q-vlan',1),('dynamic-vlan',2),('port-base-vlan',3),('protocolvlan',4),('double-vlan',5)))
_SwL2VlanType_Type.__name__=_B
_SwL2VlanType_Object=MibTableColumn
swL2VlanType=_SwL2VlanType_Object((1,3,6,1,4,1,171,11,70,2,2,17,1,1,3),_SwL2VlanType_Type())
swL2VlanType.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2VlanType.setStatus(_A)
_SwL2VlanMemberPorts_Type=PortList
_SwL2VlanMemberPorts_Object=MibTableColumn
swL2VlanMemberPorts=_SwL2VlanMemberPorts_Object((1,3,6,1,4,1,171,11,70,2,2,17,1,1,4),_SwL2VlanMemberPorts_Type())
swL2VlanMemberPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2VlanMemberPorts.setStatus(_A)
_SwL2VlanStaticPorts_Type=PortList
_SwL2VlanStaticPorts_Object=MibTableColumn
swL2VlanStaticPorts=_SwL2VlanStaticPorts_Object((1,3,6,1,4,1,171,11,70,2,2,17,1,1,5),_SwL2VlanStaticPorts_Type())
swL2VlanStaticPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2VlanStaticPorts.setStatus(_A)
_SwL2VlanStaticTaggedPorts_Type=PortList
_SwL2VlanStaticTaggedPorts_Object=MibTableColumn
swL2VlanStaticTaggedPorts=_SwL2VlanStaticTaggedPorts_Object((1,3,6,1,4,1,171,11,70,2,2,17,1,1,6),_SwL2VlanStaticTaggedPorts_Type())
swL2VlanStaticTaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2VlanStaticTaggedPorts.setStatus(_A)
_SwL2VlanStaticUntaggedPorts_Type=PortList
_SwL2VlanStaticUntaggedPorts_Object=MibTableColumn
swL2VlanStaticUntaggedPorts=_SwL2VlanStaticUntaggedPorts_Object((1,3,6,1,4,1,171,11,70,2,2,17,1,1,7),_SwL2VlanStaticUntaggedPorts_Type())
swL2VlanStaticUntaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2VlanStaticUntaggedPorts.setStatus(_A)
_SwL2VlanForbiddenPorts_Type=PortList
_SwL2VlanForbiddenPorts_Object=MibTableColumn
swL2VlanForbiddenPorts=_SwL2VlanForbiddenPorts_Object((1,3,6,1,4,1,171,11,70,2,2,17,1,1,8),_SwL2VlanForbiddenPorts_Type())
swL2VlanForbiddenPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2VlanForbiddenPorts.setStatus(_A)
_SwL2VlanCurrentTaggedPorts_Type=PortList
_SwL2VlanCurrentTaggedPorts_Object=MibTableColumn
swL2VlanCurrentTaggedPorts=_SwL2VlanCurrentTaggedPorts_Object((1,3,6,1,4,1,171,11,70,2,2,17,1,1,9),_SwL2VlanCurrentTaggedPorts_Type())
swL2VlanCurrentTaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2VlanCurrentTaggedPorts.setStatus(_A)
_SwL2VlanCurrentUntaggedPorts_Type=PortList
_SwL2VlanCurrentUntaggedPorts_Object=MibTableColumn
swL2VlanCurrentUntaggedPorts=_SwL2VlanCurrentUntaggedPorts_Object((1,3,6,1,4,1,171,11,70,2,2,17,1,1,10),_SwL2VlanCurrentUntaggedPorts_Type())
swL2VlanCurrentUntaggedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2VlanCurrentUntaggedPorts.setStatus(_A)
class _SwL2VlanAdvertisementState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2VlanAdvertisementState_Type.__name__=_B
_SwL2VlanAdvertisementState_Object=MibTableColumn
swL2VlanAdvertisementState=_SwL2VlanAdvertisementState_Object((1,3,6,1,4,1,171,11,70,2,2,17,1,1,11),_SwL2VlanAdvertisementState_Type())
swL2VlanAdvertisementState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2VlanAdvertisementState.setStatus(_A)
class _SwL2PVIDAutoAssignmentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2PVIDAutoAssignmentState_Type.__name__=_B
_SwL2PVIDAutoAssignmentState_Object=MibScalar
swL2PVIDAutoAssignmentState=_SwL2PVIDAutoAssignmentState_Object((1,3,6,1,4,1,171,11,70,2,2,17,2),_SwL2PVIDAutoAssignmentState_Type())
swL2PVIDAutoAssignmentState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PVIDAutoAssignmentState.setStatus(_A)
_SwL2LoopDetectMgmt_ObjectIdentity=ObjectIdentity
swL2LoopDetectMgmt=_SwL2LoopDetectMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,18))
_SwL2LoopDetectCtrl_ObjectIdentity=ObjectIdentity
swL2LoopDetectCtrl=_SwL2LoopDetectCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,18,1))
class _SwL2LoopDetectAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2LoopDetectAdminState_Type.__name__=_B
_SwL2LoopDetectAdminState_Object=MibScalar
swL2LoopDetectAdminState=_SwL2LoopDetectAdminState_Object((1,3,6,1,4,1,171,11,70,2,2,18,1,1),_SwL2LoopDetectAdminState_Type())
swL2LoopDetectAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectAdminState.setStatus(_A)
class _SwL2LoopDetectInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_SwL2LoopDetectInterval_Type.__name__=_B
_SwL2LoopDetectInterval_Object=MibScalar
swL2LoopDetectInterval=_SwL2LoopDetectInterval_Object((1,3,6,1,4,1,171,11,70,2,2,18,1,2),_SwL2LoopDetectInterval_Type())
swL2LoopDetectInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectInterval.setStatus(_A)
class _SwL2LoopDetectRecoverTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_SwL2LoopDetectRecoverTime_Type.__name__=_B
_SwL2LoopDetectRecoverTime_Object=MibScalar
swL2LoopDetectRecoverTime=_SwL2LoopDetectRecoverTime_Object((1,3,6,1,4,1,171,11,70,2,2,18,1,3),_SwL2LoopDetectRecoverTime_Type())
swL2LoopDetectRecoverTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectRecoverTime.setStatus(_A)
class _SwL2LoopDetectMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vlan-based',1),('port-based',2)))
_SwL2LoopDetectMode_Type.__name__=_B
_SwL2LoopDetectMode_Object=MibScalar
swL2LoopDetectMode=_SwL2LoopDetectMode_Object((1,3,6,1,4,1,171,11,70,2,2,18,1,4),_SwL2LoopDetectMode_Type())
swL2LoopDetectMode.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectMode.setStatus(_A)
class _SwL2LoopDetectTrapMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),('loop_detected',2),('loop_cleared',3),('both',4)))
_SwL2LoopDetectTrapMode_Type.__name__=_B
_SwL2LoopDetectTrapMode_Object=MibScalar
swL2LoopDetectTrapMode=_SwL2LoopDetectTrapMode_Object((1,3,6,1,4,1,171,11,70,2,2,18,1,5),_SwL2LoopDetectTrapMode_Type())
swL2LoopDetectTrapMode.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectTrapMode.setStatus(_A)
_SwL2LoopDetectPortMgmt_ObjectIdentity=ObjectIdentity
swL2LoopDetectPortMgmt=_SwL2LoopDetectPortMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,18,2))
_SwL2LoopDetectPortTable_Object=MibTable
swL2LoopDetectPortTable=_SwL2LoopDetectPortTable_Object((1,3,6,1,4,1,171,11,70,2,2,18,2,1))
if mibBuilder.loadTexts:swL2LoopDetectPortTable.setStatus(_A)
_SwL2LoopDetectPortEntry_Object=MibTableRow
swL2LoopDetectPortEntry=_SwL2LoopDetectPortEntry_Object((1,3,6,1,4,1,171,11,70,2,2,18,2,1,1))
swL2LoopDetectPortEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:swL2LoopDetectPortEntry.setStatus(_A)
class _SwL2LoopDetectPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2LoopDetectPortIndex_Type.__name__=_B
_SwL2LoopDetectPortIndex_Object=MibTableColumn
swL2LoopDetectPortIndex=_SwL2LoopDetectPortIndex_Object((1,3,6,1,4,1,171,11,70,2,2,18,2,1,1,1),_SwL2LoopDetectPortIndex_Type())
swL2LoopDetectPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectPortIndex.setStatus(_A)
class _SwL2LoopDetectPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2LoopDetectPortState_Type.__name__=_B
_SwL2LoopDetectPortState_Object=MibTableColumn
swL2LoopDetectPortState=_SwL2LoopDetectPortState_Object((1,3,6,1,4,1,171,11,70,2,2,18,2,1,1,2),_SwL2LoopDetectPortState_Type())
swL2LoopDetectPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectPortState.setStatus(_A)
_SwL2LoopDetectPortLoopVLAN_Type=DisplayString
_SwL2LoopDetectPortLoopVLAN_Object=MibTableColumn
swL2LoopDetectPortLoopVLAN=_SwL2LoopDetectPortLoopVLAN_Object((1,3,6,1,4,1,171,11,70,2,2,18,2,1,1,3),_SwL2LoopDetectPortLoopVLAN_Type())
swL2LoopDetectPortLoopVLAN.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectPortLoopVLAN.setStatus(_A)
class _SwL2LoopDetectPortLoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_V,1),('loop',2),('error',3),(_L,4)))
_SwL2LoopDetectPortLoopStatus_Type.__name__=_B
_SwL2LoopDetectPortLoopStatus_Object=MibTableColumn
swL2LoopDetectPortLoopStatus=_SwL2LoopDetectPortLoopStatus_Object((1,3,6,1,4,1,171,11,70,2,2,18,2,1,1,4),_SwL2LoopDetectPortLoopStatus_Type())
swL2LoopDetectPortLoopStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectPortLoopStatus.setStatus(_A)
_SwL2DhcpLocalRelayMgmt_ObjectIdentity=ObjectIdentity
swL2DhcpLocalRelayMgmt=_SwL2DhcpLocalRelayMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,70,2,2,24))
class _SwL2DhcpLocalRelayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2DhcpLocalRelayState_Type.__name__=_B
_SwL2DhcpLocalRelayState_Object=MibScalar
swL2DhcpLocalRelayState=_SwL2DhcpLocalRelayState_Object((1,3,6,1,4,1,171,11,70,2,2,24,1),_SwL2DhcpLocalRelayState_Type())
swL2DhcpLocalRelayState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DhcpLocalRelayState.setStatus(_A)
_SwL2DhcpLocalRelayVLANTable_Object=MibTable
swL2DhcpLocalRelayVLANTable=_SwL2DhcpLocalRelayVLANTable_Object((1,3,6,1,4,1,171,11,70,2,2,24,2))
if mibBuilder.loadTexts:swL2DhcpLocalRelayVLANTable.setStatus(_A)
_SwL2DhcpLocalRelayVLANEntry_Object=MibTableRow
swL2DhcpLocalRelayVLANEntry=_SwL2DhcpLocalRelayVLANEntry_Object((1,3,6,1,4,1,171,11,70,2,2,24,2,1))
swL2DhcpLocalRelayVLANEntry.setIndexNames((0,_E,_AG))
if mibBuilder.loadTexts:swL2DhcpLocalRelayVLANEntry.setStatus(_A)
class _SwL2DhcpLocalRelayVLANID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2DhcpLocalRelayVLANID_Type.__name__=_B
_SwL2DhcpLocalRelayVLANID_Object=MibTableColumn
swL2DhcpLocalRelayVLANID=_SwL2DhcpLocalRelayVLANID_Object((1,3,6,1,4,1,171,11,70,2,2,24,2,1,1),_SwL2DhcpLocalRelayVLANID_Type())
swL2DhcpLocalRelayVLANID.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DhcpLocalRelayVLANID.setStatus(_A)
class _SwL2DhcpLocalRelayVLANState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_F,2),(_G,3)))
_SwL2DhcpLocalRelayVLANState_Type.__name__=_B
_SwL2DhcpLocalRelayVLANState_Object=MibTableColumn
swL2DhcpLocalRelayVLANState=_SwL2DhcpLocalRelayVLANState_Object((1,3,6,1,4,1,171,11,70,2,2,24,2,1,2),_SwL2DhcpLocalRelayVLANState_Type())
swL2DhcpLocalRelayVLANState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DhcpLocalRelayVLANState.setStatus(_A)
swL2PortLoopOccurred=NotificationType((1,3,6,1,4,1,171,11,70,2,2,16,1,2,0,0,3))
swL2PortLoopOccurred.setObjects((_E,_K))
if mibBuilder.loadTexts:swL2PortLoopOccurred.setStatus(_A)
swL2PortLoopRestart=NotificationType((1,3,6,1,4,1,171,11,70,2,2,16,1,2,0,0,4))
swL2PortLoopRestart.setObjects((_E,_K))
if mibBuilder.loadTexts:swL2PortLoopRestart.setStatus(_A)
swL2VlanLoopOccurred=NotificationType((1,3,6,1,4,1,171,11,70,2,2,16,1,2,0,0,5))
swL2VlanLoopOccurred.setObjects(*((_E,_K),(_E,_S)))
if mibBuilder.loadTexts:swL2VlanLoopOccurred.setStatus(_A)
swL2VlanLoopRestart=NotificationType((1,3,6,1,4,1,171,11,70,2,2,16,1,2,0,0,6))
swL2VlanLoopRestart.setObjects(*((_E,_K),(_E,_S)))
if mibBuilder.loadTexts:swL2VlanLoopRestart.setStatus(_A)
swL2macNotification=NotificationType((1,3,6,1,4,1,171,11,70,2,2,16,1,2,0,1))
swL2macNotification.setObjects((_E,_AH))
if mibBuilder.loadTexts:swL2macNotification.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'MacAddress':MacAddress,'VlanId':VlanId,'PortList':PortList,'IANAifMauAutoNegCapBits':IANAifMauAutoNegCapBits,'swL2MgmtMIB':swL2MgmtMIB,'swL2DevMgmt':swL2DevMgmt,'swL2DevInfo':swL2DevInfo,'swDevInfoTotalNumOfPort':swDevInfoTotalNumOfPort,'swDevInfoNumOfPortInUse':swDevInfoNumOfPortInUse,'swDevModuleInfoTable':swDevModuleInfoTable,'swDevModuleInfoEntry':swDevModuleInfoEntry,_T:swDevModuleInfoUnitID,_U:swDevModuleInfoModuleID,'swDevModuleInfoModuleName':swDevModuleInfoModuleName,'swDevModuleInfoReversion':swDevModuleInfoReversion,'swDevModuleInfoSerial':swDevModuleInfoSerial,'swDevModuleInfoDescription':swDevModuleInfoDescription,'swDevInfoBootPromVersion':swDevInfoBootPromVersion,'swDevInfoFirmwareVersion':swDevInfoFirmwareVersion,'swDevInfoFrontPanelLedStatus':swDevInfoFrontPanelLedStatus,'swL2DevCtrl':swL2DevCtrl,'swL2DevCtrlStpState':swL2DevCtrlStpState,'swL2DevCtrlIGMPSnooping':swL2DevCtrlIGMPSnooping,'swL2DevCtrlIGMPSnoopingMcstRTOnly':swL2DevCtrlIGMPSnoopingMcstRTOnly,'swL2DevCtrlRmonState':swL2DevCtrlRmonState,'swL2DevCtrlCleanAllStatisticCounter':swL2DevCtrlCleanAllStatisticCounter,'swL2DevCtrlVlanIdOfFDBTbl':swL2DevCtrlVlanIdOfFDBTbl,'swL2DevCtrlManagementVlanId':swL2DevCtrlManagementVlanId,'swL2MACNotifyState':swL2MACNotifyState,'swL2MACNotifyHistorySize':swL2MACNotifyHistorySize,'swL2MACNotifyInterval':swL2MACNotifyInterval,'swL2DevCtrlWeb':swL2DevCtrlWeb,'swL2DevCtrlWebState':swL2DevCtrlWebState,'swL2DevCtrlWebTcpPort':swL2DevCtrlWebTcpPort,'swL2DevCtrlTelnet':swL2DevCtrlTelnet,'swL2DevCtrlTelnetState':swL2DevCtrlTelnetState,'swL2DevCtrlTelnetTcpPort':swL2DevCtrlTelnetTcpPort,'swL2DevCtrlIpAutoconfig':swL2DevCtrlIpAutoconfig,'swL2DevCtrlClipagingState':swL2DevCtrlClipagingState,'swL2DevCtrlLLDPState':swL2DevCtrlLLDPState,'swL2DevCtrlLLDPForwardMessageState':swL2DevCtrlLLDPForwardMessageState,'swL2DevCtrlVLANTrunkState':swL2DevCtrlVLANTrunkState,'swL2DevCtrlIGMPSnoopingMaxDataDrivenLearningCount':swL2DevCtrlIGMPSnoopingMaxDataDrivenLearningCount,'swL2DevAlarm':swL2DevAlarm,'swL2DevAlarmNewRoot':swL2DevAlarmNewRoot,'swL2DevAlarmTopologyChange':swL2DevAlarmTopologyChange,'swL2DevAlarmLinkChange':swL2DevAlarmLinkChange,'swL2MultiFilter':swL2MultiFilter,'swL2MultiFilterTable':swL2MultiFilterTable,'swL2MultiFilterEntry':swL2MultiFilterEntry,_X:swL2MultiFilterVid,'swL2MultiFilterMode':swL2MultiFilterMode,'swL2PortMgmt':swL2PortMgmt,'swL2PortInfoTable':swL2PortInfoTable,'swL2PortInfoEntry':swL2PortInfoEntry,_Y:swL2PortInfoPortIndex,_Z:swL2PortInfoMediumType,'swL2PortInfoUnitID':swL2PortInfoUnitID,'swL2PortInfoType':swL2PortInfoType,'swL2PortInfoLinkStatus':swL2PortInfoLinkStatus,'swL2PortInfoNwayStatus':swL2PortInfoNwayStatus,'swL2PortInfoErrDisReason':swL2PortInfoErrDisReason,'swL2PortCtrlTable':swL2PortCtrlTable,'swL2PortCtrlEntry':swL2PortCtrlEntry,_b:swL2PortCtrlPortIndex,_c:swL2PortCtrlMediumType,'swL2PortCtrlUnitIndex':swL2PortCtrlUnitIndex,'swL2PortCtrlAdminState':swL2PortCtrlAdminState,'swL2PortCtrlNwayState':swL2PortCtrlNwayState,'swL2PortCtrlFlowCtrlState':swL2PortCtrlFlowCtrlState,'swL2PortCtrlLockState':swL2PortCtrlLockState,'swL2PortCtrlMACNotifyState':swL2PortCtrlMACNotifyState,'swL2PortCtrlAutoNegRestart':swL2PortCtrlAutoNegRestart,'swL2PortCtrlAutoNegCapAdvertisedBits':swL2PortCtrlAutoNegCapAdvertisedBits,'swL2PortCtrlJumboFrame':swL2PortCtrlJumboFrame,'swL2PortCtrlJumboFrameMaxSize':swL2PortCtrlJumboFrameMaxSize,'swL2PortCounterCtrlTable':swL2PortCounterCtrlTable,'swL2PortCounterCtrlEntry':swL2PortCounterCtrlEntry,_d:swL2PortCounterCtrlPortIndex,'swL2PortCounterClearCtrl':swL2PortCounterClearCtrl,'swL2PortAutoNegInfoTable':swL2PortAutoNegInfoTable,'swL2PortAutoNegInfoEntry':swL2PortAutoNegInfoEntry,_e:swL2PortAutoNegInfoPortIndex,'swL2PortAutoNegInfoAdminStatus':swL2PortAutoNegInfoAdminStatus,'swL2PortAutoNegInfoCapabilityBits':swL2PortAutoNegInfoCapabilityBits,'swL2PortAutoNegInfoCapAdvertisedBits':swL2PortAutoNegInfoCapAdvertisedBits,'swL2PortAutoNegInfoCapReceivedBits':swL2PortAutoNegInfoCapReceivedBits,'swL2PortDropCounterTable':swL2PortDropCounterTable,'swL2PortDropCounterEntry':swL2PortDropCounterEntry,_f:swL2PortDropCounterPortIndex,'swL2PortBufferFullDrops':swL2PortBufferFullDrops,'swL2PortACLDrops':swL2PortACLDrops,'swL2PortMulticastDrops':swL2PortMulticastDrops,'swL2PortVLANIngressDrops':swL2PortVLANIngressDrops,'swL2PortStatisTable':swL2PortStatisTable,'swL2PortStatisEntry':swL2PortStatisEntry,_g:swL2PortStatisPortIndex,'swL2PortStatisPkts1519to1522Octets':swL2PortStatisPkts1519to1522Octets,'swL2PortStatisPkts1519to2047Octets':swL2PortStatisPkts1519to2047Octets,'swL2PortStatisPkts2048to4095Octets':swL2PortStatisPkts2048to4095Octets,'swL2PortStatisPkts4096to9216Octets':swL2PortStatisPkts4096to9216Octets,'swL2PortSfpInfoTable':swL2PortSfpInfoTable,'swL2PortSfpInfoEntry':swL2PortSfpInfoEntry,_h:swL2PortSfpInfoPortIndex,'swL2PortSfpInfoConnectType':swL2PortSfpInfoConnectType,'swL2PortSfpInfoVendorName':swL2PortSfpInfoVendorName,'swL2PortSfpInfoVendorPN':swL2PortSfpInfoVendorPN,'swL2PortSfpInfoVendorSN':swL2PortSfpInfoVendorSN,'swL2PortSfpInfoVendorOUI':swL2PortSfpInfoVendorOUI,'swL2PortSfpInfoVendorRev':swL2PortSfpInfoVendorRev,'swL2PortSfpInfoDateCode':swL2PortSfpInfoDateCode,'swL2PortSfpInfoFiberType':swL2PortSfpInfoFiberType,'swL2PortSfpInfoBaudRate':swL2PortSfpInfoBaudRate,'swL2PortSfpInfoWavelength':swL2PortSfpInfoWavelength,'swL2QOSMgmt':swL2QOSMgmt,'swL2QOSBandwidthControlTable':swL2QOSBandwidthControlTable,'swL2QOSBandwidthControlEntry':swL2QOSBandwidthControlEntry,_i:swL2QOSBandwidthPortIndex,'swL2QOSBandwidthRxRate':swL2QOSBandwidthRxRate,'swL2QOSBandwidthTxRate':swL2QOSBandwidthTxRate,'swL2QOSBandwidthRadiusRxRate':swL2QOSBandwidthRadiusRxRate,'swL2QOSBandwidthRadiusTxRate':swL2QOSBandwidthRadiusTxRate,'swL2QOSSchedulingTable':swL2QOSSchedulingTable,'swL2QOSSchedulingEntry':swL2QOSSchedulingEntry,_j:swL2QOSSchedulingPort,_k:swL2QOSSchedulingClassID,'swL2QOSSchedulingMaxPkts':swL2QOSSchedulingMaxPkts,'swL2QOSSchedulingMechanism':swL2QOSSchedulingMechanism,'swL2QOSSchedulingMechanismEffec':swL2QOSSchedulingMechanismEffec,'swL2QOS8021pUserPriorityTable':swL2QOS8021pUserPriorityTable,'swL2QOS8021pUserPriorityEntry':swL2QOS8021pUserPriorityEntry,_l:swL2QOS8021pUserPriorityIndex,'swL2QOS8021pUserPriorityClass':swL2QOS8021pUserPriorityClass,'swL2QOS8021pDefaultPriorityTable':swL2QOS8021pDefaultPriorityTable,'swL2QOS8021pDefaultPriorityEntry':swL2QOS8021pDefaultPriorityEntry,_m:swL2QOS8021pDefaultPriorityIndex,'swL2QOS8021pDefaultPriority':swL2QOS8021pDefaultPriority,'swL2QOS8021pRadiusPriority':swL2QOS8021pRadiusPriority,'swL2QOSSchedulingMechanismCtrl':swL2QOSSchedulingMechanismCtrl,'swL2QOSHolPreventionCtrl':swL2QOSHolPreventionCtrl,'swCosBandwidthControlTable':swCosBandwidthControlTable,'swCosBandwidthControlEntry':swCosBandwidthControlEntry,_n:swCosBandwidthPort,_o:swCosBandwidthClassID,'swCosBandwidthMinRate':swCosBandwidthMinRate,'swCosBandwidthMaxRate':swCosBandwidthMaxRate,'swQosDscpTrustPortCtrlTable':swQosDscpTrustPortCtrlTable,'swQosDscpTrustPortCtrlEntry':swQosDscpTrustPortCtrlEntry,_p:swQosDscpTrustPortCtrlPortIndex,'swQosDscpTrustPortCtrlState':swQosDscpTrustPortCtrlState,'swQosDscpMapGlobalCtrlTable':swQosDscpMapGlobalCtrlTable,'swQosDscpMapGlobalCtrlEntry':swQosDscpMapGlobalCtrlEntry,_q:swQosDscpMapGlobalCtrlDscpIndex,'swQosDscpMapGlobalCtrl8021pPriority':swQosDscpMapGlobalCtrl8021pPriority,'swQosDscpMapGlobalCtrlNewDscp':swQosDscpMapGlobalCtrlNewDscp,'swL2PortSecurityMgmt':swL2PortSecurityMgmt,'swL2PortSecurityControlTable':swL2PortSecurityControlTable,'swL2PortSecurityControlEntry':swL2PortSecurityControlEntry,_r:swL2PortSecurityPortIndex,'swL2PortSecurityMaxLernAddr':swL2PortSecurityMaxLernAddr,'swL2PortSecurityMode':swL2PortSecurityMode,'swL2PortSecurityAdmState':swL2PortSecurityAdmState,'swL2PortSecurityDelCtrl':swL2PortSecurityDelCtrl,'swL2PortSecurityDelVlanName':swL2PortSecurityDelVlanName,'swL2PortSecurityDelPort':swL2PortSecurityDelPort,'swL2PortSecurityDelMacAddress':swL2PortSecurityDelMacAddress,'swL2PortSecurityDelActivity':swL2PortSecurityDelActivity,'swL2TrunkMgmt':swL2TrunkMgmt,'swL2TrunkMaxSupportedEntries':swL2TrunkMaxSupportedEntries,'swL2TrunkCurrentNumEntries':swL2TrunkCurrentNumEntries,'swL2TrunkCtrlTable':swL2TrunkCtrlTable,'swL2TrunkCtrlEntry':swL2TrunkCtrlEntry,_s:swL2TrunkIndex,'swL2TrunkName':swL2TrunkName,'swL2TrunkMasterPort':swL2TrunkMasterPort,'swL2TrunkMember':swL2TrunkMember,'swL2TrunkFloodingPort':swL2TrunkFloodingPort,'swL2TrunkType':swL2TrunkType,'swL2TrunkState':swL2TrunkState,'swL2TrunkActivePorts':swL2TrunkActivePorts,'swL2TrunkAlgorithm':swL2TrunkAlgorithm,'swL2TrunkLACPPortTable':swL2TrunkLACPPortTable,'swL2TrunkLACPPortEntry':swL2TrunkLACPPortEntry,_t:swL2TrunkLACPPortIndex,'swL2TrunkLACPPortState':swL2TrunkLACPPortState,'swL2TrunkVLANTable':swL2TrunkVLANTable,'swL2TrunkVLANEntry':swL2TrunkVLANEntry,_u:swL2TrunkVLANPort,'swL2TrunkVLANState':swL2TrunkVLANState,'swL2MirrorMgmt':swL2MirrorMgmt,'swL2MirrorLogicTargetPort':swL2MirrorLogicTargetPort,'swL2MirrorPortSourceIngress':swL2MirrorPortSourceIngress,'swL2MirrorPortSourceEgress':swL2MirrorPortSourceEgress,'swL2MirrorPortState':swL2MirrorPortState,'swL2MirrorGroupTable':swL2MirrorGroupTable,'swL2MirrorGroupEntry':swL2MirrorGroupEntry,_v:swL2MirrorGroupID,'swL2MirrorGroupRowStatus':swL2MirrorGroupRowStatus,'swL2MirrorGroupState':swL2MirrorGroupState,'swL2MirrorGroupLogicTargetPort':swL2MirrorGroupLogicTargetPort,'swL2MirrorGroupPortSourceIngress':swL2MirrorGroupPortSourceIngress,'swL2MirrorGroupPortSourceEngress':swL2MirrorGroupPortSourceEngress,'swL2IGMPMgmt':swL2IGMPMgmt,'swL2IGMPMaxSupportedVlans':swL2IGMPMaxSupportedVlans,'swL2IGMPMaxIpGroupNumPerVlan':swL2IGMPMaxIpGroupNumPerVlan,'swL2IGMPCtrlTable':swL2IGMPCtrlTable,'swL2IGMPCtrlEntry':swL2IGMPCtrlEntry,_x:swL2IGMPCtrlVid,'swL2IGMPQueryInterval':swL2IGMPQueryInterval,'swL2IGMPMaxResponseTime':swL2IGMPMaxResponseTime,'swL2IGMPRobustness':swL2IGMPRobustness,'swL2IGMPLastMemberQueryInterval':swL2IGMPLastMemberQueryInterval,'swL2IGMPHostTimeout':swL2IGMPHostTimeout,'swL2IGMPRouteTimeout':swL2IGMPRouteTimeout,'swL2IGMPLeaveTimer':swL2IGMPLeaveTimer,'swL2IGMPQueryState':swL2IGMPQueryState,'swL2IGMPCurrentState':swL2IGMPCurrentState,'swL2IGMPCtrlState':swL2IGMPCtrlState,'swL2IGMPFastLeaveState':swL2IGMPFastLeaveState,'swL2IGMPQueryVersion':swL2IGMPQueryVersion,'swL2IGMPReportSuppression':swL2IGMPReportSuppression,'swL2IGMPDataDrivenLearningState':swL2IGMPDataDrivenLearningState,'swL2IGMPDataDrivenLearningAgedOutState':swL2IGMPDataDrivenLearningAgedOutState,'swL2IGMPDataDrivenGroupExpiryTime':swL2IGMPDataDrivenGroupExpiryTime,'swL2IGMPQueryInfoTable':swL2IGMPQueryInfoTable,'swL2IGMPQueryInfoEntry':swL2IGMPQueryInfoEntry,_y:swL2IGMPInfoVid,'swL2IGMPInfoQueryCount':swL2IGMPInfoQueryCount,'swL2IGMPInfoTxQueryCount':swL2IGMPInfoTxQueryCount,'swL2IGMPInfoTable':swL2IGMPInfoTable,'swL2IGMPInfoEntry':swL2IGMPInfoEntry,_z:swL2IGMPVid,_A0:swL2IGMPGroupIpAddr,'swL2IGMPMacAddr':swL2IGMPMacAddr,'swL2IGMPPortMap':swL2IGMPPortMap,'swL2IGMPIpGroupReportCount':swL2IGMPIpGroupReportCount,'swL2IGMPRouterPortsTable':swL2IGMPRouterPortsTable,'swL2IGMPRouterPortsEntry':swL2IGMPRouterPortsEntry,_A1:swL2IGMPRouterPortsVid,'swL2IGMPRouterStaticPortList':swL2IGMPRouterStaticPortList,'swL2IGMPRouterDynamicPortList':swL2IGMPRouterDynamicPortList,'swL2IGMPRouterForbiddenPortList':swL2IGMPRouterForbiddenPortList,'swL2IGMPMulticastVlanTable':swL2IGMPMulticastVlanTable,'swL2IGMPMulticastVlanEntry':swL2IGMPMulticastVlanEntry,_A2:swL2IGMPMulticastVlanid,'swL2IGMPMulticastVlanName':swL2IGMPMulticastVlanName,'swL2IGMPMulticastVlanSourcePort':swL2IGMPMulticastVlanSourcePort,'swL2IGMPMulticastVlanMemberPort':swL2IGMPMulticastVlanMemberPort,'swL2IGMPMulticastVlanTagMemberPort':swL2IGMPMulticastVlanTagMemberPort,'swL2IGMPMulticastVlanState':swL2IGMPMulticastVlanState,'swL2IGMPMulticastVlanReplaceSourceIp':swL2IGMPMulticastVlanReplaceSourceIp,'swL2IGMPMulticastVlanRowStatus':swL2IGMPMulticastVlanRowStatus,'swL2IGMPMulticastVlanRemoveAllMcastAddrListAction':swL2IGMPMulticastVlanRemoveAllMcastAddrListAction,'swL2IGMPMulticastVlanUntagSourcePort':swL2IGMPMulticastVlanUntagSourcePort,'swL2IGMPMulticastVlanRemapPriority':swL2IGMPMulticastVlanRemapPriority,'swL2IGMPMulticastVlanReplacePriority':swL2IGMPMulticastVlanReplacePriority,'swL2IGMPMulticastVlanGroupTable':swL2IGMPMulticastVlanGroupTable,'swL2IGMPMulticastVlanGroupEntry':swL2IGMPMulticastVlanGroupEntry,_A3:swL2IGMPMulticastVlanGroupVid,_A4:swL2IGMPMulticastVlanGroupFromIp,_A5:swL2IGMPMulticastVlanGroupToIp,'swL2IGMPMulticastVlanGroupStatus':swL2IGMPMulticastVlanGroupStatus,'swIGMPSnoopingGroupTable':swIGMPSnoopingGroupTable,'swIGMPSnoopingGroupEntry':swIGMPSnoopingGroupEntry,_A6:swIGMPSnoopingGroupVid,_A7:swIGMPSnoopingGroupGroupAddr,_A8:swIGMPSnoopingGroupSourceAddr,'swIGMPSnoopingGroupIncludePortMap':swIGMPSnoopingGroupIncludePortMap,'swIGMPSnoopingGroupExcludePortMap':swIGMPSnoopingGroupExcludePortMap,'swL2IGMPSnoopingStaticGroupTable':swL2IGMPSnoopingStaticGroupTable,'swL2IGMPSnoopingStaticGroupEntry':swL2IGMPSnoopingStaticGroupEntry,_A9:swL2IGMPSnoopingStaticGroupVID,_AA:swL2IGMPSnoopingStaticGroupIPaddress,'swL2IGMPSnoopingStaticGroupMemberPortList':swL2IGMPSnoopingStaticGroupMemberPortList,'swL2IGMPSnoopingStaticGroupRowStatus':swL2IGMPSnoopingStaticGroupRowStatus,'swL2IGMPSnoopingDataDrivenLearningGroupTable':swL2IGMPSnoopingDataDrivenLearningGroupTable,'swL2IGMPSnoopingDataDrivenLearningGroupEntry':swL2IGMPSnoopingDataDrivenLearningGroupEntry,_AB:swL2IGMPSnoopingDataDrivenLearningGrpVID,_AC:swL2IGMPSnoopingDataDrivenLearningGrpGrpAddr,'swL2IGMPSnoopingDataDrivenLearningGrpRouterPorts':swL2IGMPSnoopingDataDrivenLearningGrpRouterPorts,'swL2IGMPSnoopingDataDrivenLearningGrpClearGrp':swL2IGMPSnoopingDataDrivenLearningGrpClearGrp,'swL2TrafficSegMgmt':swL2TrafficSegMgmt,'swL2TrafficSegTable':swL2TrafficSegTable,'swL2TrafficSegEntry':swL2TrafficSegEntry,_AD:swL2TrafficSegPort,'swL2TrafficSegForwardPorts':swL2TrafficSegForwardPorts,'swL2IpLimitedMulticastMgmt':swL2IpLimitedMulticastMgmt,'swL2IpLimitedMulticastTable':swL2IpLimitedMulticastTable,'swL2IpLimitedMulticastEntry':swL2IpLimitedMulticastEntry,_AE:swL2IpLimitedMulticastPortIndex,'swL2IpLimitedMulticastHead':swL2IpLimitedMulticastHead,'swL2IpLimitedMulticastTail':swL2IpLimitedMulticastTail,'swL2IpLimitedMulticastAccess':swL2IpLimitedMulticastAccess,'swL2IpLimitedMulticastState':swL2IpLimitedMulticastState,'swL2IpLimitedMulticastDelState':swL2IpLimitedMulticastDelState,'swL2MgmtMIBTraps':swL2MgmtMIBTraps,'swL2Notify':swL2Notify,'swL2NotifyPrefix':swL2NotifyPrefix,'swL2NotifFirmware':swL2NotifFirmware,'swL2LoopDetectedNotify':swL2LoopDetectedNotify,'swL2PortLoopOccurred':swL2PortLoopOccurred,'swL2PortLoopRestart':swL2PortLoopRestart,'swL2VlanLoopOccurred':swL2VlanLoopOccurred,'swL2VlanLoopRestart':swL2VlanLoopRestart,'swL2macNotification':swL2macNotification,'swl2NotificationBidings':swl2NotificationBidings,_AH:swL2macNotifyInfo,_S:swL2VlanLoopDetectVID,'swL2VlanMgmt':swL2VlanMgmt,'swL2VlanTable':swL2VlanTable,'swL2VlanEntry':swL2VlanEntry,_AF:swL2VlanIndex,'swL2VlanName':swL2VlanName,'swL2VlanType':swL2VlanType,'swL2VlanMemberPorts':swL2VlanMemberPorts,'swL2VlanStaticPorts':swL2VlanStaticPorts,'swL2VlanStaticTaggedPorts':swL2VlanStaticTaggedPorts,'swL2VlanStaticUntaggedPorts':swL2VlanStaticUntaggedPorts,'swL2VlanForbiddenPorts':swL2VlanForbiddenPorts,'swL2VlanCurrentTaggedPorts':swL2VlanCurrentTaggedPorts,'swL2VlanCurrentUntaggedPorts':swL2VlanCurrentUntaggedPorts,'swL2VlanAdvertisementState':swL2VlanAdvertisementState,'swL2PVIDAutoAssignmentState':swL2PVIDAutoAssignmentState,'swL2LoopDetectMgmt':swL2LoopDetectMgmt,'swL2LoopDetectCtrl':swL2LoopDetectCtrl,'swL2LoopDetectAdminState':swL2LoopDetectAdminState,'swL2LoopDetectInterval':swL2LoopDetectInterval,'swL2LoopDetectRecoverTime':swL2LoopDetectRecoverTime,'swL2LoopDetectMode':swL2LoopDetectMode,'swL2LoopDetectTrapMode':swL2LoopDetectTrapMode,'swL2LoopDetectPortMgmt':swL2LoopDetectPortMgmt,'swL2LoopDetectPortTable':swL2LoopDetectPortTable,'swL2LoopDetectPortEntry':swL2LoopDetectPortEntry,_K:swL2LoopDetectPortIndex,'swL2LoopDetectPortState':swL2LoopDetectPortState,'swL2LoopDetectPortLoopVLAN':swL2LoopDetectPortLoopVLAN,'swL2LoopDetectPortLoopStatus':swL2LoopDetectPortLoopStatus,'swL2DhcpLocalRelayMgmt':swL2DhcpLocalRelayMgmt,'swL2DhcpLocalRelayState':swL2DhcpLocalRelayState,'swL2DhcpLocalRelayVLANTable':swL2DhcpLocalRelayVLANTable,'swL2DhcpLocalRelayVLANEntry':swL2DhcpLocalRelayVLANEntry,_AG:swL2DhcpLocalRelayVLANID,'swL2DhcpLocalRelayVLANState':swL2DhcpLocalRelayVLANState})