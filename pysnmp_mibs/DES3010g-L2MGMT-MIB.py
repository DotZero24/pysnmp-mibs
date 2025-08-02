_AD='swL2PortSecurityViolationMac'
_AC='swL2macNotifyInfo'
_AB='swL2VlanIndex'
_AA='swL2LoopDetectPortIndex'
_A9='swL2CosDscpPRIIndex'
_A8='swL2CosTosPRIIndex'
_A7='swL2CosMacBasePRIIndex'
_A6='swL2CosPortPRIIndex'
_A5='swL2CosPriorityPort'
_A4='forceFalse'
_A3='forceTrue'
_A2='swL2StpPort'
_A1='swL2TrafficSegPort'
_A0='swL2TrafficCtrlGroupIndex'
_z='swL2IGMPAccessAuthPort'
_y='swL2IGMPRouterPortVlanid'
_x='swL2IGMPGroupIpAddr'
_w='swL2IGMPVid'
_v='swL2IGMPInfoVid'
_u='swL2IGMPCtrlVid'
_t='swL2TrunkVLANPort'
_s='swL2TrunkLACPPortIndex'
_r='static'
_q='swPortTrunkIndex'
_p='swL2QOS8021pDefaultPriorityIndex'
_o='swL2QOS8021pUserPriorityIndex'
_n='swL2QOSSchedulingClassIndex'
_m='swL2QOSBandwidthPortIndex'
_l='err-disabled'
_k='swL2PortErrPortIndex'
_j='swL2PortCtrlPortIndex'
_i='half-100Mbps-none'
_h='half-100Mbps-backp'
_g='full-100Mbps-none'
_f='full-100Mbps-8023x'
_e='half-10Mbps-none'
_d='half-10Mbps-backp'
_c='full-10Mbps-none'
_b='full-10Mbps-8023x'
_a='swL2PortInfoPortIndex'
_Z='active'
_Y='moduleType-DEM-201FL'
_X='moduleType-COMBA'
_W='moduleType-DEM-301G'
_V='moduleType-DEM-201F'
_U='moduleType-DEM-301T'
_T='Unsigned32'
_S='obsolete'
_R='not-accessible'
_Q='swL2PortSecurityPortIndex'
_P='normal'
_O='none'
_N='OctetString'
_M='read-create'
_L='auto'
_K='DisplayString'
_J='enable'
_I='disable'
_H='enabled'
_G='disabled'
_F='DES3010g-L2MGMT-MIB'
_E='other'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
des3010g,=mibBuilder.importSymbols('DLINK-SWPRIMGMT-MIB','des3010g')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_T,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','RowStatus','TextualConvention','TruthValue')
swL2MgmtMIB=ModuleIdentity((1,3,6,1,4,1,171,11,63,1,2,2))
class VlanId(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class PortList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SwL2DevMgmt_ObjectIdentity=ObjectIdentity
swL2DevMgmt=_SwL2DevMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,1))
_SwL2DevInfo_ObjectIdentity=ObjectIdentity
swL2DevInfo=_SwL2DevInfo_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,1,1))
class _SwL2DevInfoFrontPanelLedStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwL2DevInfoFrontPanelLedStatus_Type.__name__=_N
_SwL2DevInfoFrontPanelLedStatus_Object=MibScalar
swL2DevInfoFrontPanelLedStatus=_SwL2DevInfoFrontPanelLedStatus_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,1,5),_SwL2DevInfoFrontPanelLedStatus_Type())
swL2DevInfoFrontPanelLedStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevInfoFrontPanelLedStatus.setStatus(_A)
class _SwL2Module_1_Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_O,0),(_U,1),(_V,2),(_W,3),(_X,4),(_Y,5)))
_SwL2Module_1_Type_Type.__name__=_B
_SwL2Module_1_Type_Object=MibScalar
swL2Module_1_Type=_SwL2Module_1_Type_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,1,6),_SwL2Module_1_Type_Type())
swL2Module_1_Type.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2Module_1_Type.setStatus(_A)
class _SwL2Module_2_Type_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_O,0),(_U,1),(_V,2),(_W,3),(_X,4),(_Y,5)))
_SwL2Module_2_Type_Type.__name__=_B
_SwL2Module_2_Type_Object=MibScalar
swL2Module_2_Type=_SwL2Module_2_Type_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,1,7),_SwL2Module_2_Type_Type())
swL2Module_2_Type.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2Module_2_Type.setStatus(_A)
_SwL2DevCtrl_ObjectIdentity=ObjectIdentity
swL2DevCtrl=_SwL2DevCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,1,2))
class _SwL2DevCtrlSystemReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('reboot',2),('save-config-and-reboot',3),('reboot-and-load-factory-default-config',4)))
_SwL2DevCtrlSystemReboot_Type.__name__=_B
_SwL2DevCtrlSystemReboot_Object=MibScalar
swL2DevCtrlSystemReboot=_SwL2DevCtrlSystemReboot_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,2,1),_SwL2DevCtrlSystemReboot_Type())
swL2DevCtrlSystemReboot.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlSystemReboot.setStatus(_A)
_SwL2DevCtrlSystemIP_Type=IpAddress
_SwL2DevCtrlSystemIP_Object=MibScalar
swL2DevCtrlSystemIP=_SwL2DevCtrlSystemIP_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,2,2),_SwL2DevCtrlSystemIP_Type())
swL2DevCtrlSystemIP.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlSystemIP.setStatus(_A)
_SwL2DevCtrlSubnetMask_Type=IpAddress
_SwL2DevCtrlSubnetMask_Object=MibScalar
swL2DevCtrlSubnetMask=_SwL2DevCtrlSubnetMask_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,2,3),_SwL2DevCtrlSubnetMask_Type())
swL2DevCtrlSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlSubnetMask.setStatus(_A)
_SwL2DevCtrlDefaultGateway_Type=IpAddress
_SwL2DevCtrlDefaultGateway_Object=MibScalar
swL2DevCtrlDefaultGateway=_SwL2DevCtrlDefaultGateway_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,2,4),_SwL2DevCtrlDefaultGateway_Type())
swL2DevCtrlDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlDefaultGateway.setStatus(_A)
_SwL2DevCtrlManagementVlanId_Type=VlanId
_SwL2DevCtrlManagementVlanId_Object=MibScalar
swL2DevCtrlManagementVlanId=_SwL2DevCtrlManagementVlanId_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,2,5),_SwL2DevCtrlManagementVlanId_Type())
swL2DevCtrlManagementVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlManagementVlanId.setStatus(_A)
class _SwL2DevCtrlStpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3)))
_SwL2DevCtrlStpState_Type.__name__=_B
_SwL2DevCtrlStpState_Object=MibScalar
swL2DevCtrlStpState=_SwL2DevCtrlStpState_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,2,6),_SwL2DevCtrlStpState_Type())
swL2DevCtrlStpState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlStpState.setStatus(_A)
class _SwL2DevCtrlIGMPSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3)))
_SwL2DevCtrlIGMPSnooping_Type.__name__=_B
_SwL2DevCtrlIGMPSnooping_Object=MibScalar
swL2DevCtrlIGMPSnooping=_SwL2DevCtrlIGMPSnooping_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,2,7),_SwL2DevCtrlIGMPSnooping_Type())
swL2DevCtrlIGMPSnooping.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlIGMPSnooping.setStatus(_A)
class _SwL2DevCtrlCleanAllStatisticCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Z,2)))
_SwL2DevCtrlCleanAllStatisticCounter_Type.__name__=_B
_SwL2DevCtrlCleanAllStatisticCounter_Object=MibScalar
swL2DevCtrlCleanAllStatisticCounter=_SwL2DevCtrlCleanAllStatisticCounter_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,2,12),_SwL2DevCtrlCleanAllStatisticCounter_Type())
swL2DevCtrlCleanAllStatisticCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlCleanAllStatisticCounter.setStatus(_A)
class _SwL2DevCtrlSnmpEnableAuthenTraps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2DevCtrlSnmpEnableAuthenTraps_Type.__name__=_B
_SwL2DevCtrlSnmpEnableAuthenTraps_Object=MibScalar
swL2DevCtrlSnmpEnableAuthenTraps=_SwL2DevCtrlSnmpEnableAuthenTraps_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,2,13),_SwL2DevCtrlSnmpEnableAuthenTraps_Type())
swL2DevCtrlSnmpEnableAuthenTraps.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlSnmpEnableAuthenTraps.setStatus(_A)
class _SwL2DevCtrlRmonState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3)))
_SwL2DevCtrlRmonState_Type.__name__=_B
_SwL2DevCtrlRmonState_Object=MibScalar
swL2DevCtrlRmonState=_SwL2DevCtrlRmonState_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,2,16),_SwL2DevCtrlRmonState_Type())
swL2DevCtrlRmonState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlRmonState.setStatus(_A)
class _SwL2DevCtrlIpAutoConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3)))
_SwL2DevCtrlIpAutoConfig_Type.__name__=_B
_SwL2DevCtrlIpAutoConfig_Object=MibScalar
swL2DevCtrlIpAutoConfig=_SwL2DevCtrlIpAutoConfig_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,2,17),_SwL2DevCtrlIpAutoConfig_Type())
swL2DevCtrlIpAutoConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlIpAutoConfig.setStatus(_A)
class _SwL2PortCtrlMulticastfilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('forward-unregistered-groups',2),('filter-unregistered-groups',3)))
_SwL2PortCtrlMulticastfilter_Type.__name__=_B
_SwL2PortCtrlMulticastfilter_Object=MibScalar
swL2PortCtrlMulticastfilter=_SwL2PortCtrlMulticastfilter_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,2,18),_SwL2PortCtrlMulticastfilter_Type())
swL2PortCtrlMulticastfilter.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlMulticastfilter.setStatus(_A)
class _SwL2MACNotifyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3)))
_SwL2MACNotifyState_Type.__name__=_B
_SwL2MACNotifyState_Object=MibScalar
swL2MACNotifyState=_SwL2MACNotifyState_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,2,19),_SwL2MACNotifyState_Type())
swL2MACNotifyState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MACNotifyState.setStatus(_A)
class _SwL2MACNotifyHistorySize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,500))
_SwL2MACNotifyHistorySize_Type.__name__=_B
_SwL2MACNotifyHistorySize_Object=MibScalar
swL2MACNotifyHistorySize=_SwL2MACNotifyHistorySize_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,2,20),_SwL2MACNotifyHistorySize_Type())
swL2MACNotifyHistorySize.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MACNotifyHistorySize.setStatus(_A)
class _SwL2MACNotifyInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SwL2MACNotifyInterval_Type.__name__=_B
_SwL2MACNotifyInterval_Object=MibScalar
swL2MACNotifyInterval=_SwL2MACNotifyInterval_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,2,21),_SwL2MACNotifyInterval_Type())
swL2MACNotifyInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2MACNotifyInterval.setStatus(_A)
class _SwL2DevCtrlVLANTrunkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2DevCtrlVLANTrunkState_Type.__name__=_B
_SwL2DevCtrlVLANTrunkState_Object=MibScalar
swL2DevCtrlVLANTrunkState=_SwL2DevCtrlVLANTrunkState_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,2,22),_SwL2DevCtrlVLANTrunkState_Type())
swL2DevCtrlVLANTrunkState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlVLANTrunkState.setStatus(_A)
class _SwL2DevCtrlLLDPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2DevCtrlLLDPState_Type.__name__=_B
_SwL2DevCtrlLLDPState_Object=MibScalar
swL2DevCtrlLLDPState=_SwL2DevCtrlLLDPState_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,2,23),_SwL2DevCtrlLLDPState_Type())
swL2DevCtrlLLDPState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlLLDPState.setStatus(_A)
class _SwL2DevCtrlLLDPForwardMessageState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2DevCtrlLLDPForwardMessageState_Type.__name__=_B
_SwL2DevCtrlLLDPForwardMessageState_Object=MibScalar
swL2DevCtrlLLDPForwardMessageState=_SwL2DevCtrlLLDPForwardMessageState_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,2,24),_SwL2DevCtrlLLDPForwardMessageState_Type())
swL2DevCtrlLLDPForwardMessageState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlLLDPForwardMessageState.setStatus(_A)
_SwL2DevCtrlVlanIdOfFDBTbl_Type=VlanId
_SwL2DevCtrlVlanIdOfFDBTbl_Object=MibScalar
swL2DevCtrlVlanIdOfFDBTbl=_SwL2DevCtrlVlanIdOfFDBTbl_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,2,25),_SwL2DevCtrlVlanIdOfFDBTbl_Type())
swL2DevCtrlVlanIdOfFDBTbl.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlVlanIdOfFDBTbl.setStatus(_A)
_SwL2CPUutilization_ObjectIdentity=ObjectIdentity
swL2CPUutilization=_SwL2CPUutilization_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,1,3))
_SwL2CPUutilizationIn5sec_Type=Integer32
_SwL2CPUutilizationIn5sec_Object=MibScalar
swL2CPUutilizationIn5sec=_SwL2CPUutilizationIn5sec_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,3,1),_SwL2CPUutilizationIn5sec_Type())
swL2CPUutilizationIn5sec.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2CPUutilizationIn5sec.setStatus(_A)
_SwL2CPUutilizationIn1min_Type=Integer32
_SwL2CPUutilizationIn1min_Object=MibScalar
swL2CPUutilizationIn1min=_SwL2CPUutilizationIn1min_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,3,2),_SwL2CPUutilizationIn1min_Type())
swL2CPUutilizationIn1min.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2CPUutilizationIn1min.setStatus(_A)
_SwL2CPUutilizationIn5min_Type=Integer32
_SwL2CPUutilizationIn5min_Object=MibScalar
swL2CPUutilizationIn5min=_SwL2CPUutilizationIn5min_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,3,3),_SwL2CPUutilizationIn5min_Type())
swL2CPUutilizationIn5min.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2CPUutilizationIn5min.setStatus(_A)
_SwL2DevAlarm_ObjectIdentity=ObjectIdentity
swL2DevAlarm=_SwL2DevAlarm_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,1,4))
class _SwL2DevAlarmLinkChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3)))
_SwL2DevAlarmLinkChange_Type.__name__=_B
_SwL2DevAlarmLinkChange_Object=MibScalar
swL2DevAlarmLinkChange=_SwL2DevAlarmLinkChange_Object((1,3,6,1,4,1,171,11,63,1,2,2,1,4,3),_SwL2DevAlarmLinkChange_Type())
swL2DevAlarmLinkChange.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevAlarmLinkChange.setStatus(_A)
_SwL2PortMgmt_ObjectIdentity=ObjectIdentity
swL2PortMgmt=_SwL2PortMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,2))
_SwL2PortInfoTable_Object=MibTable
swL2PortInfoTable=_SwL2PortInfoTable_Object((1,3,6,1,4,1,171,11,63,1,2,2,2,1))
if mibBuilder.loadTexts:swL2PortInfoTable.setStatus(_A)
_SwL2PortInfoEntry_Object=MibTableRow
swL2PortInfoEntry=_SwL2PortInfoEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,2,1,1))
swL2PortInfoEntry.setIndexNames((0,_F,_a))
if mibBuilder.loadTexts:swL2PortInfoEntry.setStatus(_A)
class _SwL2PortInfoPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2PortInfoPortIndex_Type.__name__=_B
_SwL2PortInfoPortIndex_Object=MibTableColumn
swL2PortInfoPortIndex=_SwL2PortInfoPortIndex_Object((1,3,6,1,4,1,171,11,63,1,2,2,2,1,1,1),_SwL2PortInfoPortIndex_Type())
swL2PortInfoPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoPortIndex.setStatus(_A)
class _SwL2PortInfoLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('link-pass',2),('link-fail',3)))
_SwL2PortInfoLinkStatus_Type.__name__=_B
_SwL2PortInfoLinkStatus_Object=MibTableColumn
swL2PortInfoLinkStatus=_SwL2PortInfoLinkStatus_Object((1,3,6,1,4,1,171,11,63,1,2,2,2,1,1,4),_SwL2PortInfoLinkStatus_Type())
swL2PortInfoLinkStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoLinkStatus.setStatus(_A)
class _SwL2PortInfoNwayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_L,1),(_b,2),(_c,3),(_d,4),(_e,5),(_f,6),(_g,7),(_h,8),(_i,9),('full-1Gigabps-8023x',10),('full-1Gigabps-none',11),('half-1Gigabps-backp',12),('half-1Gigabps-none',13)))
_SwL2PortInfoNwayStatus_Type.__name__=_B
_SwL2PortInfoNwayStatus_Object=MibTableColumn
swL2PortInfoNwayStatus=_SwL2PortInfoNwayStatus_Object((1,3,6,1,4,1,171,11,63,1,2,2,2,1,1,5),_SwL2PortInfoNwayStatus_Type())
swL2PortInfoNwayStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoNwayStatus.setStatus(_A)
_SwL2PortCtrlTable_Object=MibTable
swL2PortCtrlTable=_SwL2PortCtrlTable_Object((1,3,6,1,4,1,171,11,63,1,2,2,2,2))
if mibBuilder.loadTexts:swL2PortCtrlTable.setStatus(_A)
_SwL2PortCtrlEntry_Object=MibTableRow
swL2PortCtrlEntry=_SwL2PortCtrlEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,2,2,1))
swL2PortCtrlEntry.setIndexNames((0,_F,_j))
if mibBuilder.loadTexts:swL2PortCtrlEntry.setStatus(_A)
class _SwL2PortCtrlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2PortCtrlPortIndex_Type.__name__=_B
_SwL2PortCtrlPortIndex_Object=MibTableColumn
swL2PortCtrlPortIndex=_SwL2PortCtrlPortIndex_Object((1,3,6,1,4,1,171,11,63,1,2,2,2,2,1,1),_SwL2PortCtrlPortIndex_Type())
swL2PortCtrlPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlPortIndex.setStatus(_A)
class _SwL2PortCtrlAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3)))
_SwL2PortCtrlAdminState_Type.__name__=_B
_SwL2PortCtrlAdminState_Object=MibTableColumn
swL2PortCtrlAdminState=_SwL2PortCtrlAdminState_Object((1,3,6,1,4,1,171,11,63,1,2,2,2,2,1,2),_SwL2PortCtrlAdminState_Type())
swL2PortCtrlAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlAdminState.setStatus(_A)
class _SwL2PortCtrlNwayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7)));namedValues=NamedValues(*(('nway-auto',1),('nway-disabled-10Mbps-Half',2),('nway-disabled-10Mbps-Full',3),('nway-disabled-100Mbps-Half',4),('nway-disabled-100Mbps-Full',5),('nway-disabled-1Gigabps-Full',7)))
_SwL2PortCtrlNwayState_Type.__name__=_B
_SwL2PortCtrlNwayState_Object=MibTableColumn
swL2PortCtrlNwayState=_SwL2PortCtrlNwayState_Object((1,3,6,1,4,1,171,11,63,1,2,2,2,2,1,3),_SwL2PortCtrlNwayState_Type())
swL2PortCtrlNwayState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlNwayState.setStatus(_A)
class _SwL2PortCtrlFlowCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3)))
_SwL2PortCtrlFlowCtrlState_Type.__name__=_B
_SwL2PortCtrlFlowCtrlState_Object=MibTableColumn
swL2PortCtrlFlowCtrlState=_SwL2PortCtrlFlowCtrlState_Object((1,3,6,1,4,1,171,11,63,1,2,2,2,2,1,4),_SwL2PortCtrlFlowCtrlState_Type())
swL2PortCtrlFlowCtrlState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlFlowCtrlState.setStatus(_A)
class _SwL2PortCtrlDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwL2PortCtrlDescription_Type.__name__=_K
_SwL2PortCtrlDescription_Object=MibTableColumn
swL2PortCtrlDescription=_SwL2PortCtrlDescription_Object((1,3,6,1,4,1,171,11,63,1,2,2,2,2,1,5),_SwL2PortCtrlDescription_Type())
swL2PortCtrlDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlDescription.setStatus(_A)
class _SwL2PortCtrlMACNotifyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3)))
_SwL2PortCtrlMACNotifyState_Type.__name__=_B
_SwL2PortCtrlMACNotifyState_Object=MibTableColumn
swL2PortCtrlMACNotifyState=_SwL2PortCtrlMACNotifyState_Object((1,3,6,1,4,1,171,11,63,1,2,2,2,2,1,7),_SwL2PortCtrlMACNotifyState_Type())
swL2PortCtrlMACNotifyState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlMACNotifyState.setStatus(_A)
class _SwL2PortCtrlMDIXState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_P,2),('cross',3)))
_SwL2PortCtrlMDIXState_Type.__name__=_B
_SwL2PortCtrlMDIXState_Object=MibTableColumn
swL2PortCtrlMDIXState=_SwL2PortCtrlMDIXState_Object((1,3,6,1,4,1,171,11,63,1,2,2,2,2,1,10),_SwL2PortCtrlMDIXState_Type())
swL2PortCtrlMDIXState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlMDIXState.setStatus(_A)
_SwL2PortErrTable_Object=MibTable
swL2PortErrTable=_SwL2PortErrTable_Object((1,3,6,1,4,1,171,11,63,1,2,2,2,3))
if mibBuilder.loadTexts:swL2PortErrTable.setStatus(_A)
_SwL2PortErrEntry_Object=MibTableRow
swL2PortErrEntry=_SwL2PortErrEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,2,3,1))
swL2PortErrEntry.setIndexNames((0,_F,_k))
if mibBuilder.loadTexts:swL2PortErrEntry.setStatus(_A)
class _SwL2PortErrPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2PortErrPortIndex_Type.__name__=_B
_SwL2PortErrPortIndex_Object=MibTableColumn
swL2PortErrPortIndex=_SwL2PortErrPortIndex_Object((1,3,6,1,4,1,171,11,63,1,2,2,2,3,1,1),_SwL2PortErrPortIndex_Type())
swL2PortErrPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortErrPortIndex.setStatus(_A)
class _SwL2PortErrPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SwL2PortErrPortState_Type.__name__=_B
_SwL2PortErrPortState_Object=MibTableColumn
swL2PortErrPortState=_SwL2PortErrPortState_Object((1,3,6,1,4,1,171,11,63,1,2,2,2,3,1,2),_SwL2PortErrPortState_Type())
swL2PortErrPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortErrPortState.setStatus(_A)
class _SwL2PortErrPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_l,2)))
_SwL2PortErrPortStatus_Type.__name__=_B
_SwL2PortErrPortStatus_Object=MibTableColumn
swL2PortErrPortStatus=_SwL2PortErrPortStatus_Object((1,3,6,1,4,1,171,11,63,1,2,2,2,3,1,3),_SwL2PortErrPortStatus_Type())
swL2PortErrPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortErrPortStatus.setStatus(_A)
class _SwL2PortErrPortReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stp-lbd',1),('storm-control',2)))
_SwL2PortErrPortReason_Type.__name__=_B
_SwL2PortErrPortReason_Object=MibTableColumn
swL2PortErrPortReason=_SwL2PortErrPortReason_Object((1,3,6,1,4,1,171,11,63,1,2,2,2,3,1,4),_SwL2PortErrPortReason_Type())
swL2PortErrPortReason.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortErrPortReason.setStatus(_A)
class _SwL2PortErrDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwL2PortErrDescription_Type.__name__=_K
_SwL2PortErrDescription_Object=MibTableColumn
swL2PortErrDescription=_SwL2PortErrDescription_Object((1,3,6,1,4,1,171,11,63,1,2,2,2,3,1,5),_SwL2PortErrDescription_Type())
swL2PortErrDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortErrDescription.setStatus(_A)
_SwL2QOSMgmt_ObjectIdentity=ObjectIdentity
swL2QOSMgmt=_SwL2QOSMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,3))
_SwL2QOSBandwidthControlTable_Object=MibTable
swL2QOSBandwidthControlTable=_SwL2QOSBandwidthControlTable_Object((1,3,6,1,4,1,171,11,63,1,2,2,3,1))
if mibBuilder.loadTexts:swL2QOSBandwidthControlTable.setStatus(_A)
_SwL2QOSBandwidthControlEntry_Object=MibTableRow
swL2QOSBandwidthControlEntry=_SwL2QOSBandwidthControlEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,3,1,1))
swL2QOSBandwidthControlEntry.setIndexNames((0,_F,_m))
if mibBuilder.loadTexts:swL2QOSBandwidthControlEntry.setStatus(_A)
class _SwL2QOSBandwidthPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,650))
_SwL2QOSBandwidthPortIndex_Type.__name__=_B
_SwL2QOSBandwidthPortIndex_Object=MibTableColumn
swL2QOSBandwidthPortIndex=_SwL2QOSBandwidthPortIndex_Object((1,3,6,1,4,1,171,11,63,1,2,2,3,1,1,1),_SwL2QOSBandwidthPortIndex_Type())
swL2QOSBandwidthPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSBandwidthPortIndex.setStatus(_A)
class _SwL2QOSBandwidthRxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1024000))
_SwL2QOSBandwidthRxRate_Type.__name__=_B
_SwL2QOSBandwidthRxRate_Object=MibTableColumn
swL2QOSBandwidthRxRate=_SwL2QOSBandwidthRxRate_Object((1,3,6,1,4,1,171,11,63,1,2,2,3,1,1,2),_SwL2QOSBandwidthRxRate_Type())
swL2QOSBandwidthRxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSBandwidthRxRate.setStatus(_A)
class _SwL2QOSBandwidthTxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1024000))
_SwL2QOSBandwidthTxRate_Type.__name__=_B
_SwL2QOSBandwidthTxRate_Object=MibTableColumn
swL2QOSBandwidthTxRate=_SwL2QOSBandwidthTxRate_Object((1,3,6,1,4,1,171,11,63,1,2,2,3,1,1,3),_SwL2QOSBandwidthTxRate_Type())
swL2QOSBandwidthTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSBandwidthTxRate.setStatus(_A)
_SwL2QOSBandwidthRadiusRxRate_Type=Integer32
_SwL2QOSBandwidthRadiusRxRate_Object=MibTableColumn
swL2QOSBandwidthRadiusRxRate=_SwL2QOSBandwidthRadiusRxRate_Object((1,3,6,1,4,1,171,11,63,1,2,2,3,1,1,4),_SwL2QOSBandwidthRadiusRxRate_Type())
swL2QOSBandwidthRadiusRxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSBandwidthRadiusRxRate.setStatus(_A)
_SwL2QOSBandwidthRadiusTxRate_Type=Integer32
_SwL2QOSBandwidthRadiusTxRate_Object=MibTableColumn
swL2QOSBandwidthRadiusTxRate=_SwL2QOSBandwidthRadiusTxRate_Object((1,3,6,1,4,1,171,11,63,1,2,2,3,1,1,5),_SwL2QOSBandwidthRadiusTxRate_Type())
swL2QOSBandwidthRadiusTxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSBandwidthRadiusTxRate.setStatus(_A)
_SwL2QOSSchedulingTable_Object=MibTable
swL2QOSSchedulingTable=_SwL2QOSSchedulingTable_Object((1,3,6,1,4,1,171,11,63,1,2,2,3,2))
if mibBuilder.loadTexts:swL2QOSSchedulingTable.setStatus(_A)
_SwL2QOSSchedulingEntry_Object=MibTableRow
swL2QOSSchedulingEntry=_SwL2QOSSchedulingEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,3,2,1))
swL2QOSSchedulingEntry.setIndexNames((0,_F,_n))
if mibBuilder.loadTexts:swL2QOSSchedulingEntry.setStatus(_A)
class _SwL2QOSSchedulingClassIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_SwL2QOSSchedulingClassIndex_Type.__name__=_B
_SwL2QOSSchedulingClassIndex_Object=MibTableColumn
swL2QOSSchedulingClassIndex=_SwL2QOSSchedulingClassIndex_Object((1,3,6,1,4,1,171,11,63,1,2,2,3,2,1,1),_SwL2QOSSchedulingClassIndex_Type())
swL2QOSSchedulingClassIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOSSchedulingClassIndex.setStatus(_A)
class _SwL2QOSSchedulingMaxWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,55))
_SwL2QOSSchedulingMaxWeight_Type.__name__=_B
_SwL2QOSSchedulingMaxWeight_Object=MibTableColumn
swL2QOSSchedulingMaxWeight=_SwL2QOSSchedulingMaxWeight_Object((1,3,6,1,4,1,171,11,63,1,2,2,3,2,1,4),_SwL2QOSSchedulingMaxWeight_Type())
swL2QOSSchedulingMaxWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSSchedulingMaxWeight.setStatus(_A)
_SwL2QOS8021pUserPriorityTable_Object=MibTable
swL2QOS8021pUserPriorityTable=_SwL2QOS8021pUserPriorityTable_Object((1,3,6,1,4,1,171,11,63,1,2,2,3,3))
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityTable.setStatus(_A)
_SwL2QOS8021pUserPriorityEntry_Object=MibTableRow
swL2QOS8021pUserPriorityEntry=_SwL2QOS8021pUserPriorityEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,3,3,1))
swL2QOS8021pUserPriorityEntry.setIndexNames((0,_F,_o))
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityEntry.setStatus(_A)
class _SwL2QOS8021pUserPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwL2QOS8021pUserPriorityIndex_Type.__name__=_B
_SwL2QOS8021pUserPriorityIndex_Object=MibTableColumn
swL2QOS8021pUserPriorityIndex=_SwL2QOS8021pUserPriorityIndex_Object((1,3,6,1,4,1,171,11,63,1,2,2,3,3,1,1),_SwL2QOS8021pUserPriorityIndex_Type())
swL2QOS8021pUserPriorityIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityIndex.setStatus(_A)
class _SwL2QOS8021pUserPriorityClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_SwL2QOS8021pUserPriorityClass_Type.__name__=_B
_SwL2QOS8021pUserPriorityClass_Object=MibTableColumn
swL2QOS8021pUserPriorityClass=_SwL2QOS8021pUserPriorityClass_Object((1,3,6,1,4,1,171,11,63,1,2,2,3,3,1,2),_SwL2QOS8021pUserPriorityClass_Type())
swL2QOS8021pUserPriorityClass.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOS8021pUserPriorityClass.setStatus(_A)
_SwL2QOS8021pDefaultPriorityTable_Object=MibTable
swL2QOS8021pDefaultPriorityTable=_SwL2QOS8021pDefaultPriorityTable_Object((1,3,6,1,4,1,171,11,63,1,2,2,3,4))
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriorityTable.setStatus(_A)
_SwL2QOS8021pDefaultPriorityEntry_Object=MibTableRow
swL2QOS8021pDefaultPriorityEntry=_SwL2QOS8021pDefaultPriorityEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,3,4,1))
swL2QOS8021pDefaultPriorityEntry.setIndexNames((0,_F,_p))
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriorityEntry.setStatus(_A)
class _SwL2QOS8021pDefaultPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,650))
_SwL2QOS8021pDefaultPriorityIndex_Type.__name__=_B
_SwL2QOS8021pDefaultPriorityIndex_Object=MibTableColumn
swL2QOS8021pDefaultPriorityIndex=_SwL2QOS8021pDefaultPriorityIndex_Object((1,3,6,1,4,1,171,11,63,1,2,2,3,4,1,1),_SwL2QOS8021pDefaultPriorityIndex_Type())
swL2QOS8021pDefaultPriorityIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriorityIndex.setStatus(_A)
class _SwL2QOS8021pDefaultPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwL2QOS8021pDefaultPriority_Type.__name__=_B
_SwL2QOS8021pDefaultPriority_Object=MibTableColumn
swL2QOS8021pDefaultPriority=_SwL2QOS8021pDefaultPriority_Object((1,3,6,1,4,1,171,11,63,1,2,2,3,4,1,2),_SwL2QOS8021pDefaultPriority_Type())
swL2QOS8021pDefaultPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOS8021pDefaultPriority.setStatus(_A)
_SwL2QOS8021pRadiusPriority_Type=Integer32
_SwL2QOS8021pRadiusPriority_Object=MibTableColumn
swL2QOS8021pRadiusPriority=_SwL2QOS8021pRadiusPriority_Object((1,3,6,1,4,1,171,11,63,1,2,2,3,4,1,3),_SwL2QOS8021pRadiusPriority_Type())
swL2QOS8021pRadiusPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2QOS8021pRadiusPriority.setStatus(_A)
class _SwL2QOSSchedulingMechanismCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('strict',1),('weightfair',2),(_O,3)))
_SwL2QOSSchedulingMechanismCtrl_Type.__name__=_B
_SwL2QOSSchedulingMechanismCtrl_Object=MibScalar
swL2QOSSchedulingMechanismCtrl=_SwL2QOSSchedulingMechanismCtrl_Object((1,3,6,1,4,1,171,11,63,1,2,2,3,5),_SwL2QOSSchedulingMechanismCtrl_Type())
swL2QOSSchedulingMechanismCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2QOSSchedulingMechanismCtrl.setStatus(_A)
_SwL2TrunkMgmt_ObjectIdentity=ObjectIdentity
swL2TrunkMgmt=_SwL2TrunkMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,4))
_SwPortTrunkMaxEntries_Type=Integer32
_SwPortTrunkMaxEntries_Object=MibScalar
swPortTrunkMaxEntries=_SwPortTrunkMaxEntries_Object((1,3,6,1,4,1,171,11,63,1,2,2,4,1),_SwPortTrunkMaxEntries_Type())
swPortTrunkMaxEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:swPortTrunkMaxEntries.setStatus(_A)
_SwPortTrunkMaxPortMembers_Type=Integer32
_SwPortTrunkMaxPortMembers_Object=MibScalar
swPortTrunkMaxPortMembers=_SwPortTrunkMaxPortMembers_Object((1,3,6,1,4,1,171,11,63,1,2,2,4,2),_SwPortTrunkMaxPortMembers_Type())
swPortTrunkMaxPortMembers.setMaxAccess(_D)
if mibBuilder.loadTexts:swPortTrunkMaxPortMembers.setStatus(_A)
_SwPortTrunkTable_Object=MibTable
swPortTrunkTable=_SwPortTrunkTable_Object((1,3,6,1,4,1,171,11,63,1,2,2,4,3))
if mibBuilder.loadTexts:swPortTrunkTable.setStatus(_A)
_SwPortTrunkEntry_Object=MibTableRow
swPortTrunkEntry=_SwPortTrunkEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,4,3,1))
swPortTrunkEntry.setIndexNames((0,_F,_q))
if mibBuilder.loadTexts:swPortTrunkEntry.setStatus(_A)
class _SwPortTrunkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_SwPortTrunkIndex_Type.__name__=_B
_SwPortTrunkIndex_Object=MibTableColumn
swPortTrunkIndex=_SwPortTrunkIndex_Object((1,3,6,1,4,1,171,11,63,1,2,2,4,3,1,1),_SwPortTrunkIndex_Type())
swPortTrunkIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swPortTrunkIndex.setStatus(_A)
_SwPortTrunkMasterPort_Type=Integer32
_SwPortTrunkMasterPort_Object=MibTableColumn
swPortTrunkMasterPort=_SwPortTrunkMasterPort_Object((1,3,6,1,4,1,171,11,63,1,2,2,4,3,1,2),_SwPortTrunkMasterPort_Type())
swPortTrunkMasterPort.setMaxAccess(_M)
if mibBuilder.loadTexts:swPortTrunkMasterPort.setStatus(_A)
_SwPortTrunkPortList_Type=PortList
_SwPortTrunkPortList_Object=MibTableColumn
swPortTrunkPortList=_SwPortTrunkPortList_Object((1,3,6,1,4,1,171,11,63,1,2,2,4,3,1,3),_SwPortTrunkPortList_Type())
swPortTrunkPortList.setMaxAccess(_M)
if mibBuilder.loadTexts:swPortTrunkPortList.setStatus(_A)
class _SwPortTrunkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_r,1),('lacp',2)))
_SwPortTrunkType_Type.__name__=_B
_SwPortTrunkType_Object=MibTableColumn
swPortTrunkType=_SwPortTrunkType_Object((1,3,6,1,4,1,171,11,63,1,2,2,4,3,1,4),_SwPortTrunkType_Type())
swPortTrunkType.setMaxAccess(_M)
if mibBuilder.loadTexts:swPortTrunkType.setStatus(_A)
_SwPortTrunkActivePort_Type=PortList
_SwPortTrunkActivePort_Object=MibTableColumn
swPortTrunkActivePort=_SwPortTrunkActivePort_Object((1,3,6,1,4,1,171,11,63,1,2,2,4,3,1,5),_SwPortTrunkActivePort_Type())
swPortTrunkActivePort.setMaxAccess(_D)
if mibBuilder.loadTexts:swPortTrunkActivePort.setStatus(_A)
_SwPortTrunkState_Type=RowStatus
_SwPortTrunkState_Object=MibTableColumn
swPortTrunkState=_SwPortTrunkState_Object((1,3,6,1,4,1,171,11,63,1,2,2,4,3,1,6),_SwPortTrunkState_Type())
swPortTrunkState.setMaxAccess(_M)
if mibBuilder.loadTexts:swPortTrunkState.setStatus(_A)
_SwPortTrunkFloodingPort_Type=Integer32
_SwPortTrunkFloodingPort_Object=MibTableColumn
swPortTrunkFloodingPort=_SwPortTrunkFloodingPort_Object((1,3,6,1,4,1,171,11,63,1,2,2,4,3,1,7),_SwPortTrunkFloodingPort_Type())
swPortTrunkFloodingPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swPortTrunkFloodingPort.setStatus(_A)
class _SwL2TrunkAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('mac-source',2),('mac-destination',3),('mac-source-dest',4)))
_SwL2TrunkAlgorithm_Type.__name__=_B
_SwL2TrunkAlgorithm_Object=MibScalar
swL2TrunkAlgorithm=_SwL2TrunkAlgorithm_Object((1,3,6,1,4,1,171,11,63,1,2,2,4,4),_SwL2TrunkAlgorithm_Type())
swL2TrunkAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkAlgorithm.setStatus(_A)
_SwL2TrunkLACPPortTable_Object=MibTable
swL2TrunkLACPPortTable=_SwL2TrunkLACPPortTable_Object((1,3,6,1,4,1,171,11,63,1,2,2,4,5))
if mibBuilder.loadTexts:swL2TrunkLACPPortTable.setStatus(_A)
_SwL2TrunkLACPPortEntry_Object=MibTableRow
swL2TrunkLACPPortEntry=_SwL2TrunkLACPPortEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,4,5,1))
swL2TrunkLACPPortEntry.setIndexNames((0,_F,_s))
if mibBuilder.loadTexts:swL2TrunkLACPPortEntry.setStatus(_A)
class _SwL2TrunkLACPPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkLACPPortIndex_Type.__name__=_B
_SwL2TrunkLACPPortIndex_Object=MibTableColumn
swL2TrunkLACPPortIndex=_SwL2TrunkLACPPortIndex_Object((1,3,6,1,4,1,171,11,63,1,2,2,4,5,1,1),_SwL2TrunkLACPPortIndex_Type())
swL2TrunkLACPPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkLACPPortIndex.setStatus(_A)
class _SwL2TrunkLACPPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),('passive',2)))
_SwL2TrunkLACPPortState_Type.__name__=_B
_SwL2TrunkLACPPortState_Object=MibTableColumn
swL2TrunkLACPPortState=_SwL2TrunkLACPPortState_Object((1,3,6,1,4,1,171,11,63,1,2,2,4,5,1,2),_SwL2TrunkLACPPortState_Type())
swL2TrunkLACPPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkLACPPortState.setStatus(_A)
_SwL2TrunkVLANTable_Object=MibTable
swL2TrunkVLANTable=_SwL2TrunkVLANTable_Object((1,3,6,1,4,1,171,11,63,1,2,2,4,6))
if mibBuilder.loadTexts:swL2TrunkVLANTable.setStatus(_A)
_SwL2TrunkVLANEntry_Object=MibTableRow
swL2TrunkVLANEntry=_SwL2TrunkVLANEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,4,6,1))
swL2TrunkVLANEntry.setIndexNames((0,_F,_t))
if mibBuilder.loadTexts:swL2TrunkVLANEntry.setStatus(_A)
class _SwL2TrunkVLANPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrunkVLANPort_Type.__name__=_B
_SwL2TrunkVLANPort_Object=MibTableColumn
swL2TrunkVLANPort=_SwL2TrunkVLANPort_Object((1,3,6,1,4,1,171,11,63,1,2,2,4,6,1,1),_SwL2TrunkVLANPort_Type())
swL2TrunkVLANPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrunkVLANPort.setStatus(_A)
class _SwL2TrunkVLANState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2TrunkVLANState_Type.__name__=_B
_SwL2TrunkVLANState_Object=MibTableColumn
swL2TrunkVLANState=_SwL2TrunkVLANState_Object((1,3,6,1,4,1,171,11,63,1,2,2,4,6,1,2),_SwL2TrunkVLANState_Type())
swL2TrunkVLANState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrunkVLANState.setStatus(_A)
_SwPortMirrorPackage_ObjectIdentity=ObjectIdentity
swPortMirrorPackage=_SwPortMirrorPackage_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,6))
_SwPortMirrorRxPortList_Type=PortList
_SwPortMirrorRxPortList_Object=MibScalar
swPortMirrorRxPortList=_SwPortMirrorRxPortList_Object((1,3,6,1,4,1,171,11,63,1,2,2,6,2),_SwPortMirrorRxPortList_Type())
swPortMirrorRxPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:swPortMirrorRxPortList.setStatus(_A)
_SwPortMirrorTxPortList_Type=PortList
_SwPortMirrorTxPortList_Object=MibScalar
swPortMirrorTxPortList=_SwPortMirrorTxPortList_Object((1,3,6,1,4,1,171,11,63,1,2,2,6,3),_SwPortMirrorTxPortList_Type())
swPortMirrorTxPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:swPortMirrorTxPortList.setStatus(_A)
_SwPortMirrorTargetPort_Type=Integer32
_SwPortMirrorTargetPort_Object=MibScalar
swPortMirrorTargetPort=_SwPortMirrorTargetPort_Object((1,3,6,1,4,1,171,11,63,1,2,2,6,4),_SwPortMirrorTargetPort_Type())
swPortMirrorTargetPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swPortMirrorTargetPort.setStatus(_A)
class _SwPortMirrorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3)))
_SwPortMirrorState_Type.__name__=_B
_SwPortMirrorState_Object=MibScalar
swPortMirrorState=_SwPortMirrorState_Object((1,3,6,1,4,1,171,11,63,1,2,2,6,5),_SwPortMirrorState_Type())
swPortMirrorState.setMaxAccess(_C)
if mibBuilder.loadTexts:swPortMirrorState.setStatus(_A)
_SwIGMPPackage_ObjectIdentity=ObjectIdentity
swIGMPPackage=_SwIGMPPackage_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,7))
class _SwL2IGMPMaxSupportedVlans_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPMaxSupportedVlans_Type.__name__=_B
_SwL2IGMPMaxSupportedVlans_Object=MibScalar
swL2IGMPMaxSupportedVlans=_SwL2IGMPMaxSupportedVlans_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,1),_SwL2IGMPMaxSupportedVlans_Type())
swL2IGMPMaxSupportedVlans.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMaxSupportedVlans.setStatus(_A)
class _SwL2IGMPMaxIpGroupNumPerVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPMaxIpGroupNumPerVlan_Type.__name__=_B
_SwL2IGMPMaxIpGroupNumPerVlan_Object=MibScalar
swL2IGMPMaxIpGroupNumPerVlan=_SwL2IGMPMaxIpGroupNumPerVlan_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,2),_SwL2IGMPMaxIpGroupNumPerVlan_Type())
swL2IGMPMaxIpGroupNumPerVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMaxIpGroupNumPerVlan.setStatus(_A)
_SwL2IGMPCtrlTable_Object=MibTable
swL2IGMPCtrlTable=_SwL2IGMPCtrlTable_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,3))
if mibBuilder.loadTexts:swL2IGMPCtrlTable.setStatus(_A)
_SwL2IGMPCtrlEntry_Object=MibTableRow
swL2IGMPCtrlEntry=_SwL2IGMPCtrlEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,3,1))
swL2IGMPCtrlEntry.setIndexNames((0,_F,_u))
if mibBuilder.loadTexts:swL2IGMPCtrlEntry.setStatus(_A)
class _SwL2IGMPCtrlVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPCtrlVid_Type.__name__=_B
_SwL2IGMPCtrlVid_Object=MibTableColumn
swL2IGMPCtrlVid=_SwL2IGMPCtrlVid_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,3,1,1),_SwL2IGMPCtrlVid_Type())
swL2IGMPCtrlVid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPCtrlVid.setStatus(_A)
class _SwL2IGMPQueryInterval_Type(Integer32):defaultValue=125;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2IGMPQueryInterval_Type.__name__=_B
_SwL2IGMPQueryInterval_Object=MibTableColumn
swL2IGMPQueryInterval=_SwL2IGMPQueryInterval_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,3,1,2),_SwL2IGMPQueryInterval_Type())
swL2IGMPQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPQueryInterval.setStatus(_A)
class _SwL2IGMPMaxResponseTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,25))
_SwL2IGMPMaxResponseTime_Type.__name__=_B
_SwL2IGMPMaxResponseTime_Object=MibTableColumn
swL2IGMPMaxResponseTime=_SwL2IGMPMaxResponseTime_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,3,1,3),_SwL2IGMPMaxResponseTime_Type())
swL2IGMPMaxResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPMaxResponseTime.setStatus(_A)
class _SwL2IGMPRobustness_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2IGMPRobustness_Type.__name__=_B
_SwL2IGMPRobustness_Object=MibTableColumn
swL2IGMPRobustness=_SwL2IGMPRobustness_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,3,1,4),_SwL2IGMPRobustness_Type())
swL2IGMPRobustness.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRobustness.setStatus(_A)
class _SwL2IGMPLastMemberQueryInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2IGMPLastMemberQueryInterval_Type.__name__=_B
_SwL2IGMPLastMemberQueryInterval_Object=MibTableColumn
swL2IGMPLastMemberQueryInterval=_SwL2IGMPLastMemberQueryInterval_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,3,1,5),_SwL2IGMPLastMemberQueryInterval_Type())
swL2IGMPLastMemberQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPLastMemberQueryInterval.setStatus(_A)
class _SwL2IGMPHostTimeout_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16711450))
_SwL2IGMPHostTimeout_Type.__name__=_B
_SwL2IGMPHostTimeout_Object=MibTableColumn
swL2IGMPHostTimeout=_SwL2IGMPHostTimeout_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,3,1,6),_SwL2IGMPHostTimeout_Type())
swL2IGMPHostTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPHostTimeout.setStatus(_A)
class _SwL2IGMPRouteTimeout_Type(Integer32):defaultValue=260;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16711450))
_SwL2IGMPRouteTimeout_Type.__name__=_B
_SwL2IGMPRouteTimeout_Object=MibTableColumn
swL2IGMPRouteTimeout=_SwL2IGMPRouteTimeout_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,3,1,7),_SwL2IGMPRouteTimeout_Type())
swL2IGMPRouteTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRouteTimeout.setStatus(_A)
class _SwL2IGMPLeaveTimer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16711450))
_SwL2IGMPLeaveTimer_Type.__name__=_B
_SwL2IGMPLeaveTimer_Object=MibTableColumn
swL2IGMPLeaveTimer=_SwL2IGMPLeaveTimer_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,3,1,8),_SwL2IGMPLeaveTimer_Type())
swL2IGMPLeaveTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPLeaveTimer.setStatus(_A)
class _SwL2IGMPQueryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3)))
_SwL2IGMPQueryState_Type.__name__=_B
_SwL2IGMPQueryState_Object=MibTableColumn
swL2IGMPQueryState=_SwL2IGMPQueryState_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,3,1,9),_SwL2IGMPQueryState_Type())
swL2IGMPQueryState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPQueryState.setStatus(_A)
class _SwL2IGMPCurrentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('querier',2),('non-querier',3)))
_SwL2IGMPCurrentState_Type.__name__=_B
_SwL2IGMPCurrentState_Object=MibTableColumn
swL2IGMPCurrentState=_SwL2IGMPCurrentState_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,3,1,10),_SwL2IGMPCurrentState_Type())
swL2IGMPCurrentState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPCurrentState.setStatus(_A)
class _SwL2IGMPCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_I,2),(_J,3)))
_SwL2IGMPCtrlState_Type.__name__=_B
_SwL2IGMPCtrlState_Object=MibTableColumn
swL2IGMPCtrlState=_SwL2IGMPCtrlState_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,3,1,11),_SwL2IGMPCtrlState_Type())
swL2IGMPCtrlState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPCtrlState.setStatus(_A)
class _SwL2IGMPFastLeave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_I,2),(_J,3)))
_SwL2IGMPFastLeave_Type.__name__=_B
_SwL2IGMPFastLeave_Object=MibTableColumn
swL2IGMPFastLeave=_SwL2IGMPFastLeave_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,3,1,12),_SwL2IGMPFastLeave_Type())
swL2IGMPFastLeave.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPFastLeave.setStatus(_A)
_SwL2IGMPQueryInfoTable_Object=MibTable
swL2IGMPQueryInfoTable=_SwL2IGMPQueryInfoTable_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,4))
if mibBuilder.loadTexts:swL2IGMPQueryInfoTable.setStatus(_A)
_SwL2IGMPQueryInfoEntry_Object=MibTableRow
swL2IGMPQueryInfoEntry=_SwL2IGMPQueryInfoEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,4,1))
swL2IGMPQueryInfoEntry.setIndexNames((0,_F,_v))
if mibBuilder.loadTexts:swL2IGMPQueryInfoEntry.setStatus(_A)
class _SwL2IGMPInfoVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPInfoVid_Type.__name__=_B
_SwL2IGMPInfoVid_Object=MibTableColumn
swL2IGMPInfoVid=_SwL2IGMPInfoVid_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,4,1,1),_SwL2IGMPInfoVid_Type())
swL2IGMPInfoVid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPInfoVid.setStatus(_A)
class _SwL2IGMPInfoQueryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPInfoQueryCount_Type.__name__=_B
_SwL2IGMPInfoQueryCount_Object=MibTableColumn
swL2IGMPInfoQueryCount=_SwL2IGMPInfoQueryCount_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,4,1,2),_SwL2IGMPInfoQueryCount_Type())
swL2IGMPInfoQueryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPInfoQueryCount.setStatus(_A)
class _SwL2IGMPInfoTxQueryCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPInfoTxQueryCount_Type.__name__=_B
_SwL2IGMPInfoTxQueryCount_Object=MibTableColumn
swL2IGMPInfoTxQueryCount=_SwL2IGMPInfoTxQueryCount_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,4,1,3),_SwL2IGMPInfoTxQueryCount_Type())
swL2IGMPInfoTxQueryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPInfoTxQueryCount.setStatus(_A)
_SwL2IGMPInfoTable_Object=MibTable
swL2IGMPInfoTable=_SwL2IGMPInfoTable_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,5))
if mibBuilder.loadTexts:swL2IGMPInfoTable.setStatus(_A)
_SwL2IGMPInfoEntry_Object=MibTableRow
swL2IGMPInfoEntry=_SwL2IGMPInfoEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,5,1))
swL2IGMPInfoEntry.setIndexNames((0,_F,_w),(0,_F,_x))
if mibBuilder.loadTexts:swL2IGMPInfoEntry.setStatus(_A)
class _SwL2IGMPVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPVid_Type.__name__=_B
_SwL2IGMPVid_Object=MibTableColumn
swL2IGMPVid=_SwL2IGMPVid_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,5,1,1),_SwL2IGMPVid_Type())
swL2IGMPVid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPVid.setStatus(_A)
_SwL2IGMPGroupIpAddr_Type=IpAddress
_SwL2IGMPGroupIpAddr_Object=MibTableColumn
swL2IGMPGroupIpAddr=_SwL2IGMPGroupIpAddr_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,5,1,2),_SwL2IGMPGroupIpAddr_Type())
swL2IGMPGroupIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPGroupIpAddr.setStatus(_A)
_SwL2IGMPMacAddr_Type=MacAddress
_SwL2IGMPMacAddr_Object=MibTableColumn
swL2IGMPMacAddr=_SwL2IGMPMacAddr_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,5,1,3),_SwL2IGMPMacAddr_Type())
swL2IGMPMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPMacAddr.setStatus(_A)
_SwL2IGMPPortMap_Type=PortList
_SwL2IGMPPortMap_Object=MibTableColumn
swL2IGMPPortMap=_SwL2IGMPPortMap_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,5,1,4),_SwL2IGMPPortMap_Type())
swL2IGMPPortMap.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPPortMap.setStatus(_A)
class _SwL2IGMPIpGroupReportCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPIpGroupReportCount_Type.__name__=_B
_SwL2IGMPIpGroupReportCount_Object=MibTableColumn
swL2IGMPIpGroupReportCount=_SwL2IGMPIpGroupReportCount_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,5,1,5),_SwL2IGMPIpGroupReportCount_Type())
swL2IGMPIpGroupReportCount.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPIpGroupReportCount.setStatus(_A)
_SwL2IGMPRouterPortTable_Object=MibTable
swL2IGMPRouterPortTable=_SwL2IGMPRouterPortTable_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,6))
if mibBuilder.loadTexts:swL2IGMPRouterPortTable.setStatus(_A)
_SwL2IGMPRouterPortEntry_Object=MibTableRow
swL2IGMPRouterPortEntry=_SwL2IGMPRouterPortEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,6,1))
swL2IGMPRouterPortEntry.setIndexNames((0,_F,_y))
if mibBuilder.loadTexts:swL2IGMPRouterPortEntry.setStatus(_A)
class _SwL2IGMPRouterPortVlanid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2IGMPRouterPortVlanid_Type.__name__=_B
_SwL2IGMPRouterPortVlanid_Object=MibTableColumn
swL2IGMPRouterPortVlanid=_SwL2IGMPRouterPortVlanid_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,6,1,1),_SwL2IGMPRouterPortVlanid_Type())
swL2IGMPRouterPortVlanid.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPRouterPortVlanid.setStatus(_A)
class _SwL2IGMPRouterPortVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL2IGMPRouterPortVlanName_Type.__name__=_K
_SwL2IGMPRouterPortVlanName_Object=MibTableColumn
swL2IGMPRouterPortVlanName=_SwL2IGMPRouterPortVlanName_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,6,1,2),_SwL2IGMPRouterPortVlanName_Type())
swL2IGMPRouterPortVlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPRouterPortVlanName.setStatus(_A)
_SwL2IGMPRouterPortStaticPortList_Type=PortList
_SwL2IGMPRouterPortStaticPortList_Object=MibTableColumn
swL2IGMPRouterPortStaticPortList=_SwL2IGMPRouterPortStaticPortList_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,6,1,3),_SwL2IGMPRouterPortStaticPortList_Type())
swL2IGMPRouterPortStaticPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRouterPortStaticPortList.setStatus(_A)
_SwL2IGMPRouterPortDynamicPortList_Type=PortList
_SwL2IGMPRouterPortDynamicPortList_Object=MibTableColumn
swL2IGMPRouterPortDynamicPortList=_SwL2IGMPRouterPortDynamicPortList_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,6,1,4),_SwL2IGMPRouterPortDynamicPortList_Type())
swL2IGMPRouterPortDynamicPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPRouterPortDynamicPortList.setStatus(_A)
_SwL2IGMPRouterPortForbiddenPortList_Type=PortList
_SwL2IGMPRouterPortForbiddenPortList_Object=MibTableColumn
swL2IGMPRouterPortForbiddenPortList=_SwL2IGMPRouterPortForbiddenPortList_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,6,1,5),_SwL2IGMPRouterPortForbiddenPortList_Type())
swL2IGMPRouterPortForbiddenPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPRouterPortForbiddenPortList.setStatus(_A)
_SwL2IGMPAccessAuthTable_Object=MibTable
swL2IGMPAccessAuthTable=_SwL2IGMPAccessAuthTable_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,7))
if mibBuilder.loadTexts:swL2IGMPAccessAuthTable.setStatus(_A)
_SwL2IGMPAccessAuthEntry_Object=MibTableRow
swL2IGMPAccessAuthEntry=_SwL2IGMPAccessAuthEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,7,1))
swL2IGMPAccessAuthEntry.setIndexNames((0,_F,_z))
if mibBuilder.loadTexts:swL2IGMPAccessAuthEntry.setStatus(_A)
class _SwL2IGMPAccessAuthPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2IGMPAccessAuthPort_Type.__name__=_B
_SwL2IGMPAccessAuthPort_Object=MibTableColumn
swL2IGMPAccessAuthPort=_SwL2IGMPAccessAuthPort_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,7,1,1),_SwL2IGMPAccessAuthPort_Type())
swL2IGMPAccessAuthPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IGMPAccessAuthPort.setStatus(_A)
class _SwL2IGMPAccessAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_I,2),(_J,3)))
_SwL2IGMPAccessAuthState_Type.__name__=_B
_SwL2IGMPAccessAuthState_Object=MibTableColumn
swL2IGMPAccessAuthState=_SwL2IGMPAccessAuthState_Object((1,3,6,1,4,1,171,11,63,1,2,2,7,7,1,2),_SwL2IGMPAccessAuthState_Type())
swL2IGMPAccessAuthState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IGMPAccessAuthState.setStatus(_A)
_SwL2TrafficMgmt_ObjectIdentity=ObjectIdentity
swL2TrafficMgmt=_SwL2TrafficMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,11))
_SwL2TrafficCtrlTable_Object=MibTable
swL2TrafficCtrlTable=_SwL2TrafficCtrlTable_Object((1,3,6,1,4,1,171,11,63,1,2,2,11,1))
if mibBuilder.loadTexts:swL2TrafficCtrlTable.setStatus(_A)
_SwL2TrafficCtrlEntry_Object=MibTableRow
swL2TrafficCtrlEntry=_SwL2TrafficCtrlEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,11,1,1))
swL2TrafficCtrlEntry.setIndexNames((0,_F,_A0))
if mibBuilder.loadTexts:swL2TrafficCtrlEntry.setStatus(_A)
class _SwL2TrafficCtrlGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrafficCtrlGroupIndex_Type.__name__=_B
_SwL2TrafficCtrlGroupIndex_Object=MibTableColumn
swL2TrafficCtrlGroupIndex=_SwL2TrafficCtrlGroupIndex_Object((1,3,6,1,4,1,171,11,63,1,2,2,11,1,1,1),_SwL2TrafficCtrlGroupIndex_Type())
swL2TrafficCtrlGroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrafficCtrlGroupIndex.setStatus(_A)
class _SwL2TrafficCtrlUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrafficCtrlUnitIndex_Type.__name__=_B
_SwL2TrafficCtrlUnitIndex_Object=MibTableColumn
swL2TrafficCtrlUnitIndex=_SwL2TrafficCtrlUnitIndex_Object((1,3,6,1,4,1,171,11,63,1,2,2,11,1,1,2),_SwL2TrafficCtrlUnitIndex_Type())
swL2TrafficCtrlUnitIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrafficCtrlUnitIndex.setStatus(_A)
class _SwL2TrafficCtrlBMStromthreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1024000))
_SwL2TrafficCtrlBMStromthreshold_Type.__name__=_B
_SwL2TrafficCtrlBMStromthreshold_Object=MibTableColumn
swL2TrafficCtrlBMStromthreshold=_SwL2TrafficCtrlBMStromthreshold_Object((1,3,6,1,4,1,171,11,63,1,2,2,11,1,1,3),_SwL2TrafficCtrlBMStromthreshold_Type())
swL2TrafficCtrlBMStromthreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrafficCtrlBMStromthreshold.setStatus(_A)
class _SwL2TrafficCtrlBcastStromCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3)))
_SwL2TrafficCtrlBcastStromCtrl_Type.__name__=_B
_SwL2TrafficCtrlBcastStromCtrl_Object=MibTableColumn
swL2TrafficCtrlBcastStromCtrl=_SwL2TrafficCtrlBcastStromCtrl_Object((1,3,6,1,4,1,171,11,63,1,2,2,11,1,1,4),_SwL2TrafficCtrlBcastStromCtrl_Type())
swL2TrafficCtrlBcastStromCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrafficCtrlBcastStromCtrl.setStatus(_A)
class _SwL2TrafficCtrlMcastStromCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3)))
_SwL2TrafficCtrlMcastStromCtrl_Type.__name__=_B
_SwL2TrafficCtrlMcastStromCtrl_Object=MibTableColumn
swL2TrafficCtrlMcastStromCtrl=_SwL2TrafficCtrlMcastStromCtrl_Object((1,3,6,1,4,1,171,11,63,1,2,2,11,1,1,5),_SwL2TrafficCtrlMcastStromCtrl_Type())
swL2TrafficCtrlMcastStromCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrafficCtrlMcastStromCtrl.setStatus(_A)
class _SwL2TrafficCtrlUcastStromCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3)))
_SwL2TrafficCtrlUcastStromCtrl_Type.__name__=_B
_SwL2TrafficCtrlUcastStromCtrl_Object=MibTableColumn
swL2TrafficCtrlUcastStromCtrl=_SwL2TrafficCtrlUcastStromCtrl_Object((1,3,6,1,4,1,171,11,63,1,2,2,11,1,1,6),_SwL2TrafficCtrlUcastStromCtrl_Type())
swL2TrafficCtrlUcastStromCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrafficCtrlUcastStromCtrl.setStatus(_A)
_SwL2TrafficSegMgmt_ObjectIdentity=ObjectIdentity
swL2TrafficSegMgmt=_SwL2TrafficSegMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,12))
_SwL2TrafficSegTable_Object=MibTable
swL2TrafficSegTable=_SwL2TrafficSegTable_Object((1,3,6,1,4,1,171,11,63,1,2,2,12,1))
if mibBuilder.loadTexts:swL2TrafficSegTable.setStatus(_A)
_SwL2TrafficSegEntry_Object=MibTableRow
swL2TrafficSegEntry=_SwL2TrafficSegEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,12,1,1))
swL2TrafficSegEntry.setIndexNames((0,_F,_A1))
if mibBuilder.loadTexts:swL2TrafficSegEntry.setStatus(_A)
class _SwL2TrafficSegPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2TrafficSegPort_Type.__name__=_B
_SwL2TrafficSegPort_Object=MibTableColumn
swL2TrafficSegPort=_SwL2TrafficSegPort_Object((1,3,6,1,4,1,171,11,63,1,2,2,12,1,1,1),_SwL2TrafficSegPort_Type())
swL2TrafficSegPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2TrafficSegPort.setStatus(_A)
_SwL2TrafficSegForwardPorts_Type=PortList
_SwL2TrafficSegForwardPorts_Object=MibTableColumn
swL2TrafficSegForwardPorts=_SwL2TrafficSegForwardPorts_Object((1,3,6,1,4,1,171,11,63,1,2,2,12,1,1,2),_SwL2TrafficSegForwardPorts_Type())
swL2TrafficSegForwardPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2TrafficSegForwardPorts.setStatus(_A)
_SwL2PortSecurityMgmt_ObjectIdentity=ObjectIdentity
swL2PortSecurityMgmt=_SwL2PortSecurityMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,15))
_SwL2PortSecurityControlTable_Object=MibTable
swL2PortSecurityControlTable=_SwL2PortSecurityControlTable_Object((1,3,6,1,4,1,171,11,63,1,2,2,15,1))
if mibBuilder.loadTexts:swL2PortSecurityControlTable.setStatus(_A)
_SwL2PortSecurityControlEntry_Object=MibTableRow
swL2PortSecurityControlEntry=_SwL2PortSecurityControlEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,15,1,1))
swL2PortSecurityControlEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:swL2PortSecurityControlEntry.setStatus(_A)
class _SwL2PortSecurityPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2PortSecurityPortIndex_Type.__name__=_B
_SwL2PortSecurityPortIndex_Object=MibTableColumn
swL2PortSecurityPortIndex=_SwL2PortSecurityPortIndex_Object((1,3,6,1,4,1,171,11,63,1,2,2,15,1,1,1),_SwL2PortSecurityPortIndex_Type())
swL2PortSecurityPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortSecurityPortIndex.setStatus(_A)
class _SwL2PortSecurityMaxLernAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_SwL2PortSecurityMaxLernAddr_Type.__name__=_B
_SwL2PortSecurityMaxLernAddr_Object=MibTableColumn
swL2PortSecurityMaxLernAddr=_SwL2PortSecurityMaxLernAddr_Object((1,3,6,1,4,1,171,11,63,1,2,2,15,1,1,2),_SwL2PortSecurityMaxLernAddr_Type())
swL2PortSecurityMaxLernAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityMaxLernAddr.setStatus(_A)
class _SwL2PortSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('permanent',2),('deleteOnTimeout',3),('deleteOnReset',4)))
_SwL2PortSecurityMode_Type.__name__=_B
_SwL2PortSecurityMode_Object=MibTableColumn
swL2PortSecurityMode=_SwL2PortSecurityMode_Object((1,3,6,1,4,1,171,11,63,1,2,2,15,1,1,3),_SwL2PortSecurityMode_Type())
swL2PortSecurityMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityMode.setStatus(_A)
class _SwL2PortSecurityAdmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_J,2),(_I,3)))
_SwL2PortSecurityAdmState_Type.__name__=_B
_SwL2PortSecurityAdmState_Object=MibTableColumn
swL2PortSecurityAdmState=_SwL2PortSecurityAdmState_Object((1,3,6,1,4,1,171,11,63,1,2,2,15,1,1,4),_SwL2PortSecurityAdmState_Type())
swL2PortSecurityAdmState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityAdmState.setStatus(_A)
class _SwL2PortSecurityTrapLogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_J,2),(_I,3)))
_SwL2PortSecurityTrapLogState_Type.__name__=_B
_SwL2PortSecurityTrapLogState_Object=MibScalar
swL2PortSecurityTrapLogState=_SwL2PortSecurityTrapLogState_Object((1,3,6,1,4,1,171,11,63,1,2,2,15,2),_SwL2PortSecurityTrapLogState_Type())
swL2PortSecurityTrapLogState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityTrapLogState.setStatus(_A)
_SwL2StpMgmt_ObjectIdentity=ObjectIdentity
swL2StpMgmt=_SwL2StpMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,16))
class _SwL2StpForwardBPDU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3)))
_SwL2StpForwardBPDU_Type.__name__=_B
_SwL2StpForwardBPDU_Object=MibScalar
swL2StpForwardBPDU=_SwL2StpForwardBPDU_Object((1,3,6,1,4,1,171,11,63,1,2,2,16,1),_SwL2StpForwardBPDU_Type())
swL2StpForwardBPDU.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2StpForwardBPDU.setStatus(_A)
class _SwL2StpLbd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3)))
_SwL2StpLbd_Type.__name__=_B
_SwL2StpLbd_Object=MibScalar
swL2StpLbd=_SwL2StpLbd_Object((1,3,6,1,4,1,171,11,63,1,2,2,16,2),_SwL2StpLbd_Type())
swL2StpLbd.setMaxAccess(_R)
if mibBuilder.loadTexts:swL2StpLbd.setStatus(_S)
class _SwL2StpLbdRecoverTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_SwL2StpLbdRecoverTime_Type.__name__=_B
_SwL2StpLbdRecoverTime_Object=MibScalar
swL2StpLbdRecoverTime=_SwL2StpLbdRecoverTime_Object((1,3,6,1,4,1,171,11,63,1,2,2,16,3),_SwL2StpLbdRecoverTime_Type())
swL2StpLbdRecoverTime.setMaxAccess(_R)
if mibBuilder.loadTexts:swL2StpLbdRecoverTime.setStatus(_S)
_SwL2StpPortTable_Object=MibTable
swL2StpPortTable=_SwL2StpPortTable_Object((1,3,6,1,4,1,171,11,63,1,2,2,16,4))
if mibBuilder.loadTexts:swL2StpPortTable.setStatus(_A)
_SwL2StpPortEntry_Object=MibTableRow
swL2StpPortEntry=_SwL2StpPortEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,16,4,1))
swL2StpPortEntry.setIndexNames((0,_F,_A2))
if mibBuilder.loadTexts:swL2StpPortEntry.setStatus(_A)
class _SwL2StpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2StpPort_Type.__name__=_B
_SwL2StpPort_Object=MibTableColumn
swL2StpPort=_SwL2StpPort_Object((1,3,6,1,4,1,171,11,63,1,2,2,16,4,1,1),_SwL2StpPort_Type())
swL2StpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2StpPort.setStatus(_A)
class _SwL2StpPortLbd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3)))
_SwL2StpPortLbd_Type.__name__=_B
_SwL2StpPortLbd_Object=MibTableColumn
swL2StpPortLbd=_SwL2StpPortLbd_Object((1,3,6,1,4,1,171,11,63,1,2,2,16,4,1,2),_SwL2StpPortLbd_Type())
swL2StpPortLbd.setMaxAccess(_R)
if mibBuilder.loadTexts:swL2StpPortLbd.setStatus(_S)
class _SwL2StpPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,1),(_G,2),('discarding',3),('learning',4),('forwarding',5),('broken',6),('no-stp-enabled',7),(_l,8)))
_SwL2StpPortStatus_Type.__name__=_B
_SwL2StpPortStatus_Object=MibTableColumn
swL2StpPortStatus=_SwL2StpPortStatus_Object((1,3,6,1,4,1,171,11,63,1,2,2,16,4,1,3),_SwL2StpPortStatus_Type())
swL2StpPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2StpPortStatus.setStatus(_A)
class _SwL2StpPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,1),('alternate',2),('backup',3),('root',4),('designated',5),('nonStp',6),('loopback',7)))
_SwL2StpPortRole_Type.__name__=_B
_SwL2StpPortRole_Object=MibTableColumn
swL2StpPortRole=_SwL2StpPortRole_Object((1,3,6,1,4,1,171,11,63,1,2,2,16,4,1,4),_SwL2StpPortRole_Type())
swL2StpPortRole.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2StpPortRole.setStatus(_A)
class _SwL2StpPortFBPDU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3)))
_SwL2StpPortFBPDU_Type.__name__=_B
_SwL2StpPortFBPDU_Object=MibTableColumn
swL2StpPortFBPDU=_SwL2StpPortFBPDU_Object((1,3,6,1,4,1,171,11,63,1,2,2,16,4,1,5),_SwL2StpPortFBPDU_Type())
swL2StpPortFBPDU.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2StpPortFBPDU.setStatus(_A)
class _SwL2StpPortLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('link-down',1),(_e,2),(_d,3),(_c,4),(_b,5),(_i,6),(_h,7),(_g,8),(_f,9),('half-1000Mbps-none',10),('full-1000Mbps-backp',11),('full-1000Mbps-none',12),('full-1000Mbps-8023x',13)))
_SwL2StpPortLinkState_Type.__name__=_B
_SwL2StpPortLinkState_Object=MibTableColumn
swL2StpPortLinkState=_SwL2StpPortLinkState_Object((1,3,6,1,4,1,171,11,63,1,2,2,16,4,1,6),_SwL2StpPortLinkState_Type())
swL2StpPortLinkState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2StpPortLinkState.setStatus(_A)
_SwL2StpPortProtocolMigration_Type=TruthValue
_SwL2StpPortProtocolMigration_Object=MibTableColumn
swL2StpPortProtocolMigration=_SwL2StpPortProtocolMigration_Object((1,3,6,1,4,1,171,11,63,1,2,2,16,4,1,7),_SwL2StpPortProtocolMigration_Type())
swL2StpPortProtocolMigration.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2StpPortProtocolMigration.setStatus(_A)
class _SwL2StpPortAdminEdgePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_A3,0),(_A4,1),(_L,2)))
_SwL2StpPortAdminEdgePort_Type.__name__=_B
_SwL2StpPortAdminEdgePort_Object=MibTableColumn
swL2StpPortAdminEdgePort=_SwL2StpPortAdminEdgePort_Object((1,3,6,1,4,1,171,11,63,1,2,2,16,4,1,8),_SwL2StpPortAdminEdgePort_Type())
swL2StpPortAdminEdgePort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2StpPortAdminEdgePort.setStatus(_A)
_SwL2StpPortOperEdgePort_Type=TruthValue
_SwL2StpPortOperEdgePort_Object=MibTableColumn
swL2StpPortOperEdgePort=_SwL2StpPortOperEdgePort_Object((1,3,6,1,4,1,171,11,63,1,2,2,16,4,1,9),_SwL2StpPortOperEdgePort_Type())
swL2StpPortOperEdgePort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2StpPortOperEdgePort.setStatus(_A)
class _SwL2StpPortAdminPointToPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_A3,0),(_A4,1),(_L,2)))
_SwL2StpPortAdminPointToPoint_Type.__name__=_B
_SwL2StpPortAdminPointToPoint_Object=MibTableColumn
swL2StpPortAdminPointToPoint=_SwL2StpPortAdminPointToPoint_Object((1,3,6,1,4,1,171,11,63,1,2,2,16,4,1,10),_SwL2StpPortAdminPointToPoint_Type())
swL2StpPortAdminPointToPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2StpPortAdminPointToPoint.setStatus(_A)
_SwL2StpPortOperPointToPoint_Type=TruthValue
_SwL2StpPortOperPointToPoint_Object=MibTableColumn
swL2StpPortOperPointToPoint=_SwL2StpPortOperPointToPoint_Object((1,3,6,1,4,1,171,11,63,1,2,2,16,4,1,11),_SwL2StpPortOperPointToPoint_Type())
swL2StpPortOperPointToPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2StpPortOperPointToPoint.setStatus(_A)
class _SwL2StpPortAdminPathCost_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_SwL2StpPortAdminPathCost_Type.__name__=_T
_SwL2StpPortAdminPathCost_Object=MibTableColumn
swL2StpPortAdminPathCost=_SwL2StpPortAdminPathCost_Object((1,3,6,1,4,1,171,11,63,1,2,2,16,4,1,12),_SwL2StpPortAdminPathCost_Type())
swL2StpPortAdminPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2StpPortAdminPathCost.setStatus(_A)
class _SwL2StpPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_SwL2StpPortPriority_Type.__name__=_B
_SwL2StpPortPriority_Object=MibTableColumn
swL2StpPortPriority=_SwL2StpPortPriority_Object((1,3,6,1,4,1,171,11,63,1,2,2,16,4,1,13),_SwL2StpPortPriority_Type())
swL2StpPortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2StpPortPriority.setStatus(_A)
class _SwL2STPPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3)))
_SwL2STPPortState_Type.__name__=_B
_SwL2STPPortState_Object=MibTableColumn
swL2STPPortState=_SwL2STPPortState_Object((1,3,6,1,4,1,171,11,63,1,2,2,16,4,1,14),_SwL2STPPortState_Type())
swL2STPPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2STPPortState.setStatus(_A)
_SwL2StpPortRestrictedRole_Type=TruthValue
_SwL2StpPortRestrictedRole_Object=MibTableColumn
swL2StpPortRestrictedRole=_SwL2StpPortRestrictedRole_Object((1,3,6,1,4,1,171,11,63,1,2,2,16,4,1,15),_SwL2StpPortRestrictedRole_Type())
swL2StpPortRestrictedRole.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2StpPortRestrictedRole.setStatus(_A)
_SwL2StpPortRestrictedTCN_Type=TruthValue
_SwL2StpPortRestrictedTCN_Object=MibTableColumn
swL2StpPortRestrictedTCN=_SwL2StpPortRestrictedTCN_Object((1,3,6,1,4,1,171,11,63,1,2,2,16,4,1,16),_SwL2StpPortRestrictedTCN_Type())
swL2StpPortRestrictedTCN.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2StpPortRestrictedTCN.setStatus(_A)
_SwL2CosMgmt_ObjectIdentity=ObjectIdentity
swL2CosMgmt=_SwL2CosMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,17))
_SwL2CosPriorityCtrl_ObjectIdentity=ObjectIdentity
swL2CosPriorityCtrl=_SwL2CosPriorityCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,17,3))
_SwL2CosPriorityTable_Object=MibTable
swL2CosPriorityTable=_SwL2CosPriorityTable_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,1))
if mibBuilder.loadTexts:swL2CosPriorityTable.setStatus(_A)
_SwL2CosPriorityEntry_Object=MibTableRow
swL2CosPriorityEntry=_SwL2CosPriorityEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,1,1))
swL2CosPriorityEntry.setIndexNames((0,_F,_A5))
if mibBuilder.loadTexts:swL2CosPriorityEntry.setStatus(_A)
class _SwL2CosPriorityPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2CosPriorityPort_Type.__name__=_B
_SwL2CosPriorityPort_Object=MibTableColumn
swL2CosPriorityPort=_SwL2CosPriorityPort_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,1,1,1),_SwL2CosPriorityPort_Type())
swL2CosPriorityPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2CosPriorityPort.setStatus(_A)
class _SwL2CosPriorityPortPRI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_I,2),(_J,3)))
_SwL2CosPriorityPortPRI_Type.__name__=_B
_SwL2CosPriorityPortPRI_Object=MibTableColumn
swL2CosPriorityPortPRI=_SwL2CosPriorityPortPRI_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,1,1,2),_SwL2CosPriorityPortPRI_Type())
swL2CosPriorityPortPRI.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2CosPriorityPortPRI.setStatus(_A)
class _SwL2CosPriorityEtherPRI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('ether8021p',2),('macBase',3)))
_SwL2CosPriorityEtherPRI_Type.__name__=_B
_SwL2CosPriorityEtherPRI_Object=MibTableColumn
swL2CosPriorityEtherPRI=_SwL2CosPriorityEtherPRI_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,1,1,3),_SwL2CosPriorityEtherPRI_Type())
swL2CosPriorityEtherPRI.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2CosPriorityEtherPRI.setStatus(_A)
class _SwL2CosPriorityIpPRI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('tos',2),('dscp',3)))
_SwL2CosPriorityIpPRI_Type.__name__=_B
_SwL2CosPriorityIpPRI_Object=MibTableColumn
swL2CosPriorityIpPRI=_SwL2CosPriorityIpPRI_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,1,1,4),_SwL2CosPriorityIpPRI_Type())
swL2CosPriorityIpPRI.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2CosPriorityIpPRI.setStatus(_A)
class _SwL2CosPriorityNone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_SwL2CosPriorityNone_Type.__name__=_B
_SwL2CosPriorityNone_Object=MibTableColumn
swL2CosPriorityNone=_SwL2CosPriorityNone_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,1,1,5),_SwL2CosPriorityNone_Type())
swL2CosPriorityNone.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2CosPriorityNone.setStatus(_A)
_SwL2CosPortPRITable_Object=MibTable
swL2CosPortPRITable=_SwL2CosPortPRITable_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,2))
if mibBuilder.loadTexts:swL2CosPortPRITable.setStatus(_A)
_SwL2CosPortPRIEntry_Object=MibTableRow
swL2CosPortPRIEntry=_SwL2CosPortPRIEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,2,1))
swL2CosPortPRIEntry.setIndexNames((0,_F,_A6))
if mibBuilder.loadTexts:swL2CosPortPRIEntry.setStatus(_A)
class _SwL2CosPortPRIIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2CosPortPRIIndex_Type.__name__=_B
_SwL2CosPortPRIIndex_Object=MibTableColumn
swL2CosPortPRIIndex=_SwL2CosPortPRIIndex_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,2,1,1),_SwL2CosPortPRIIndex_Type())
swL2CosPortPRIIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2CosPortPRIIndex.setStatus(_A)
class _SwL2CosPortPRIClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_SwL2CosPortPRIClass_Type.__name__=_B
_SwL2CosPortPRIClass_Object=MibTableColumn
swL2CosPortPRIClass=_SwL2CosPortPRIClass_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,2,1,2),_SwL2CosPortPRIClass_Type())
swL2CosPortPRIClass.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2CosPortPRIClass.setStatus(_A)
_SwL2CosMacBasePRITable_Object=MibTable
swL2CosMacBasePRITable=_SwL2CosMacBasePRITable_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,3))
if mibBuilder.loadTexts:swL2CosMacBasePRITable.setStatus(_A)
_SwL2CosMacBasePRIEntry_Object=MibTableRow
swL2CosMacBasePRIEntry=_SwL2CosMacBasePRIEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,3,1))
swL2CosMacBasePRIEntry.setIndexNames((0,_F,_A7))
if mibBuilder.loadTexts:swL2CosMacBasePRIEntry.setStatus(_A)
_SwL2CosMacBasePRIIndex_Type=MacAddress
_SwL2CosMacBasePRIIndex_Object=MibTableColumn
swL2CosMacBasePRIIndex=_SwL2CosMacBasePRIIndex_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,3,1,1),_SwL2CosMacBasePRIIndex_Type())
swL2CosMacBasePRIIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2CosMacBasePRIIndex.setStatus(_A)
class _SwL2CosMacBasePRIClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_SwL2CosMacBasePRIClass_Type.__name__=_B
_SwL2CosMacBasePRIClass_Object=MibTableColumn
swL2CosMacBasePRIClass=_SwL2CosMacBasePRIClass_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,3,1,2),_SwL2CosMacBasePRIClass_Type())
swL2CosMacBasePRIClass.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2CosMacBasePRIClass.setStatus(_A)
_SwL2CosTosPRITable_Object=MibTable
swL2CosTosPRITable=_SwL2CosTosPRITable_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,4))
if mibBuilder.loadTexts:swL2CosTosPRITable.setStatus(_A)
_SwL2CosTosPRIEntry_Object=MibTableRow
swL2CosTosPRIEntry=_SwL2CosTosPRIEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,4,1))
swL2CosTosPRIEntry.setIndexNames((0,_F,_A8))
if mibBuilder.loadTexts:swL2CosTosPRIEntry.setStatus(_A)
class _SwL2CosTosPRIIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwL2CosTosPRIIndex_Type.__name__=_B
_SwL2CosTosPRIIndex_Object=MibTableColumn
swL2CosTosPRIIndex=_SwL2CosTosPRIIndex_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,4,1,1),_SwL2CosTosPRIIndex_Type())
swL2CosTosPRIIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2CosTosPRIIndex.setStatus(_A)
class _SwL2CosTosPRIClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_SwL2CosTosPRIClass_Type.__name__=_B
_SwL2CosTosPRIClass_Object=MibTableColumn
swL2CosTosPRIClass=_SwL2CosTosPRIClass_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,4,1,2),_SwL2CosTosPRIClass_Type())
swL2CosTosPRIClass.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2CosTosPRIClass.setStatus(_A)
_SwL2CosDscpPRITable_Object=MibTable
swL2CosDscpPRITable=_SwL2CosDscpPRITable_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,5))
if mibBuilder.loadTexts:swL2CosDscpPRITable.setStatus(_A)
_SwL2CosDscpPRIEntry_Object=MibTableRow
swL2CosDscpPRIEntry=_SwL2CosDscpPRIEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,5,1))
swL2CosDscpPRIEntry.setIndexNames((0,_F,_A9))
if mibBuilder.loadTexts:swL2CosDscpPRIEntry.setStatus(_A)
class _SwL2CosDscpPRIIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_SwL2CosDscpPRIIndex_Type.__name__=_B
_SwL2CosDscpPRIIndex_Object=MibTableColumn
swL2CosDscpPRIIndex=_SwL2CosDscpPRIIndex_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,5,1,1),_SwL2CosDscpPRIIndex_Type())
swL2CosDscpPRIIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2CosDscpPRIIndex.setStatus(_A)
class _SwL2CosDscpPRIClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_SwL2CosDscpPRIClass_Type.__name__=_B
_SwL2CosDscpPRIClass_Object=MibTableColumn
swL2CosDscpPRIClass=_SwL2CosDscpPRIClass_Object((1,3,6,1,4,1,171,11,63,1,2,2,17,3,5,1,2),_SwL2CosDscpPRIClass_Type())
swL2CosDscpPRIClass.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2CosDscpPRIClass.setStatus(_A)
_SwL2LoopDetectMgmt_ObjectIdentity=ObjectIdentity
swL2LoopDetectMgmt=_SwL2LoopDetectMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,18))
_SwL2LoopDetectCtrl_ObjectIdentity=ObjectIdentity
swL2LoopDetectCtrl=_SwL2LoopDetectCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,18,1))
class _SwL2LoopDetectAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2LoopDetectAdminState_Type.__name__=_B
_SwL2LoopDetectAdminState_Object=MibScalar
swL2LoopDetectAdminState=_SwL2LoopDetectAdminState_Object((1,3,6,1,4,1,171,11,63,1,2,2,18,1,1),_SwL2LoopDetectAdminState_Type())
swL2LoopDetectAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectAdminState.setStatus(_A)
class _SwL2LoopDetectInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_SwL2LoopDetectInterval_Type.__name__=_B
_SwL2LoopDetectInterval_Object=MibScalar
swL2LoopDetectInterval=_SwL2LoopDetectInterval_Object((1,3,6,1,4,1,171,11,63,1,2,2,18,1,2),_SwL2LoopDetectInterval_Type())
swL2LoopDetectInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectInterval.setStatus(_A)
class _SwL2LoopDetectRecoverTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_SwL2LoopDetectRecoverTime_Type.__name__=_B
_SwL2LoopDetectRecoverTime_Object=MibScalar
swL2LoopDetectRecoverTime=_SwL2LoopDetectRecoverTime_Object((1,3,6,1,4,1,171,11,63,1,2,2,18,1,3),_SwL2LoopDetectRecoverTime_Type())
swL2LoopDetectRecoverTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectRecoverTime.setStatus(_A)
_SwL2LoopDetectPortMgmt_ObjectIdentity=ObjectIdentity
swL2LoopDetectPortMgmt=_SwL2LoopDetectPortMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,18,2))
_SwL2LoopDetectPortTable_Object=MibTable
swL2LoopDetectPortTable=_SwL2LoopDetectPortTable_Object((1,3,6,1,4,1,171,11,63,1,2,2,18,2,1))
if mibBuilder.loadTexts:swL2LoopDetectPortTable.setStatus(_A)
_SwL2LoopDetectPortEntry_Object=MibTableRow
swL2LoopDetectPortEntry=_SwL2LoopDetectPortEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,18,2,1,1))
swL2LoopDetectPortEntry.setIndexNames((0,_F,_AA))
if mibBuilder.loadTexts:swL2LoopDetectPortEntry.setStatus(_A)
class _SwL2LoopDetectPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL2LoopDetectPortIndex_Type.__name__=_B
_SwL2LoopDetectPortIndex_Object=MibTableColumn
swL2LoopDetectPortIndex=_SwL2LoopDetectPortIndex_Object((1,3,6,1,4,1,171,11,63,1,2,2,18,2,1,1,1),_SwL2LoopDetectPortIndex_Type())
swL2LoopDetectPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectPortIndex.setStatus(_A)
class _SwL2LoopDetectPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_SwL2LoopDetectPortState_Type.__name__=_B
_SwL2LoopDetectPortState_Object=MibTableColumn
swL2LoopDetectPortState=_SwL2LoopDetectPortState_Object((1,3,6,1,4,1,171,11,63,1,2,2,18,2,1,1,2),_SwL2LoopDetectPortState_Type())
swL2LoopDetectPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2LoopDetectPortState.setStatus(_A)
class _SwL2LoopDetectPortLoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('loop',2),('error',3)))
_SwL2LoopDetectPortLoopStatus_Type.__name__=_B
_SwL2LoopDetectPortLoopStatus_Object=MibTableColumn
swL2LoopDetectPortLoopStatus=_SwL2LoopDetectPortLoopStatus_Object((1,3,6,1,4,1,171,11,63,1,2,2,18,2,1,1,4),_SwL2LoopDetectPortLoopStatus_Type())
swL2LoopDetectPortLoopStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2LoopDetectPortLoopStatus.setStatus(_A)
_SwL2VLANMgmt_ObjectIdentity=ObjectIdentity
swL2VLANMgmt=_SwL2VLANMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,19))
_SwL2VlanTable_Object=MibTable
swL2VlanTable=_SwL2VlanTable_Object((1,3,6,1,4,1,171,11,63,1,2,2,19,1))
if mibBuilder.loadTexts:swL2VlanTable.setStatus(_A)
_SwL2VlanEntry_Object=MibTableRow
swL2VlanEntry=_SwL2VlanEntry_Object((1,3,6,1,4,1,171,11,63,1,2,2,19,1,1))
swL2VlanEntry.setIndexNames((0,_F,_AB))
if mibBuilder.loadTexts:swL2VlanEntry.setStatus(_A)
_SwL2VlanIndex_Type=VlanId
_SwL2VlanIndex_Object=MibTableColumn
swL2VlanIndex=_SwL2VlanIndex_Object((1,3,6,1,4,1,171,11,63,1,2,2,19,1,1,1),_SwL2VlanIndex_Type())
swL2VlanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2VlanIndex.setStatus(_A)
class _SwL2VlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL2VlanName_Type.__name__=_K
_SwL2VlanName_Object=MibTableColumn
swL2VlanName=_SwL2VlanName_Object((1,3,6,1,4,1,171,11,63,1,2,2,19,1,1,2),_SwL2VlanName_Type())
swL2VlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2VlanName.setStatus(_A)
class _SwL2VlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dynamic',0),(_r,1)))
_SwL2VlanType_Type.__name__=_B
_SwL2VlanType_Object=MibTableColumn
swL2VlanType=_SwL2VlanType_Object((1,3,6,1,4,1,171,11,63,1,2,2,19,1,1,3),_SwL2VlanType_Type())
swL2VlanType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2VlanType.setStatus(_A)
_SwL2VlanMemberPorts_Type=PortList
_SwL2VlanMemberPorts_Object=MibTableColumn
swL2VlanMemberPorts=_SwL2VlanMemberPorts_Object((1,3,6,1,4,1,171,11,63,1,2,2,19,1,1,4),_SwL2VlanMemberPorts_Type())
swL2VlanMemberPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2VlanMemberPorts.setStatus(_A)
_SwL2VlanStaticPorts_Type=PortList
_SwL2VlanStaticPorts_Object=MibTableColumn
swL2VlanStaticPorts=_SwL2VlanStaticPorts_Object((1,3,6,1,4,1,171,11,63,1,2,2,19,1,1,5),_SwL2VlanStaticPorts_Type())
swL2VlanStaticPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2VlanStaticPorts.setStatus(_A)
_SwL2VlanUntaggedPorts_Type=PortList
_SwL2VlanUntaggedPorts_Object=MibTableColumn
swL2VlanUntaggedPorts=_SwL2VlanUntaggedPorts_Object((1,3,6,1,4,1,171,11,63,1,2,2,19,1,1,6),_SwL2VlanUntaggedPorts_Type())
swL2VlanUntaggedPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2VlanUntaggedPorts.setStatus(_A)
_SwL2VlanTaggedPorts_Type=PortList
_SwL2VlanTaggedPorts_Object=MibTableColumn
swL2VlanTaggedPorts=_SwL2VlanTaggedPorts_Object((1,3,6,1,4,1,171,11,63,1,2,2,19,1,1,7),_SwL2VlanTaggedPorts_Type())
swL2VlanTaggedPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2VlanTaggedPorts.setStatus(_A)
_SwL2MgmtMIBTraps_ObjectIdentity=ObjectIdentity
swL2MgmtMIBTraps=_SwL2MgmtMIBTraps_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,100))
_SwL2Notify_ObjectIdentity=ObjectIdentity
swL2Notify=_SwL2Notify_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,100,1))
_SwL2NotifyPrefix_ObjectIdentity=ObjectIdentity
swL2NotifyPrefix=_SwL2NotifyPrefix_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,100,1,2))
_SwL2NotifFirmware_ObjectIdentity=ObjectIdentity
swL2NotifFirmware=_SwL2NotifFirmware_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,100,1,2,0))
_Swl2NotificationBidings_ObjectIdentity=ObjectIdentity
swl2NotificationBidings=_Swl2NotificationBidings_ObjectIdentity((1,3,6,1,4,1,171,11,63,1,2,2,100,1,2,1))
class _SwL2macNotifyInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_SwL2macNotifyInfo_Type.__name__=_N
_SwL2macNotifyInfo_Object=MibScalar
swL2macNotifyInfo=_SwL2macNotifyInfo_Object((1,3,6,1,4,1,171,11,63,1,2,2,100,1,2,1,1),_SwL2macNotifyInfo_Type())
swL2macNotifyInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2macNotifyInfo.setStatus(_A)
_SwL2PortSecurityViolationMac_Type=MacAddress
_SwL2PortSecurityViolationMac_Object=MibScalar
swL2PortSecurityViolationMac=_SwL2PortSecurityViolationMac_Object((1,3,6,1,4,1,171,11,63,1,2,2,100,1,2,1,2),_SwL2PortSecurityViolationMac_Type())
swL2PortSecurityViolationMac.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:swL2PortSecurityViolationMac.setStatus(_A)
swL2macNotification=NotificationType((1,3,6,1,4,1,171,11,63,1,2,2,100,1,2,0,1))
swL2macNotification.setObjects((_F,_AC))
if mibBuilder.loadTexts:swL2macNotification.setStatus(_A)
swL2PortSecurityViolationTrap=NotificationType((1,3,6,1,4,1,171,11,63,1,2,2,100,1,2,0,2))
swL2PortSecurityViolationTrap.setObjects(*((_F,_Q),(_F,_AD)))
if mibBuilder.loadTexts:swL2PortSecurityViolationTrap.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'VlanId':VlanId,'PortList':PortList,'MacAddress':MacAddress,'swL2MgmtMIB':swL2MgmtMIB,'swL2DevMgmt':swL2DevMgmt,'swL2DevInfo':swL2DevInfo,'swL2DevInfoFrontPanelLedStatus':swL2DevInfoFrontPanelLedStatus,'swL2Module-1-Type':swL2Module_1_Type,'swL2Module-2-Type':swL2Module_2_Type,'swL2DevCtrl':swL2DevCtrl,'swL2DevCtrlSystemReboot':swL2DevCtrlSystemReboot,'swL2DevCtrlSystemIP':swL2DevCtrlSystemIP,'swL2DevCtrlSubnetMask':swL2DevCtrlSubnetMask,'swL2DevCtrlDefaultGateway':swL2DevCtrlDefaultGateway,'swL2DevCtrlManagementVlanId':swL2DevCtrlManagementVlanId,'swL2DevCtrlStpState':swL2DevCtrlStpState,'swL2DevCtrlIGMPSnooping':swL2DevCtrlIGMPSnooping,'swL2DevCtrlCleanAllStatisticCounter':swL2DevCtrlCleanAllStatisticCounter,'swL2DevCtrlSnmpEnableAuthenTraps':swL2DevCtrlSnmpEnableAuthenTraps,'swL2DevCtrlRmonState':swL2DevCtrlRmonState,'swL2DevCtrlIpAutoConfig':swL2DevCtrlIpAutoConfig,'swL2PortCtrlMulticastfilter':swL2PortCtrlMulticastfilter,'swL2MACNotifyState':swL2MACNotifyState,'swL2MACNotifyHistorySize':swL2MACNotifyHistorySize,'swL2MACNotifyInterval':swL2MACNotifyInterval,'swL2DevCtrlVLANTrunkState':swL2DevCtrlVLANTrunkState,'swL2DevCtrlLLDPState':swL2DevCtrlLLDPState,'swL2DevCtrlLLDPForwardMessageState':swL2DevCtrlLLDPForwardMessageState,'swL2DevCtrlVlanIdOfFDBTbl':swL2DevCtrlVlanIdOfFDBTbl,'swL2CPUutilization':swL2CPUutilization,'swL2CPUutilizationIn5sec':swL2CPUutilizationIn5sec,'swL2CPUutilizationIn1min':swL2CPUutilizationIn1min,'swL2CPUutilizationIn5min':swL2CPUutilizationIn5min,'swL2DevAlarm':swL2DevAlarm,'swL2DevAlarmLinkChange':swL2DevAlarmLinkChange,'swL2PortMgmt':swL2PortMgmt,'swL2PortInfoTable':swL2PortInfoTable,'swL2PortInfoEntry':swL2PortInfoEntry,_a:swL2PortInfoPortIndex,'swL2PortInfoLinkStatus':swL2PortInfoLinkStatus,'swL2PortInfoNwayStatus':swL2PortInfoNwayStatus,'swL2PortCtrlTable':swL2PortCtrlTable,'swL2PortCtrlEntry':swL2PortCtrlEntry,_j:swL2PortCtrlPortIndex,'swL2PortCtrlAdminState':swL2PortCtrlAdminState,'swL2PortCtrlNwayState':swL2PortCtrlNwayState,'swL2PortCtrlFlowCtrlState':swL2PortCtrlFlowCtrlState,'swL2PortCtrlDescription':swL2PortCtrlDescription,'swL2PortCtrlMACNotifyState':swL2PortCtrlMACNotifyState,'swL2PortCtrlMDIXState':swL2PortCtrlMDIXState,'swL2PortErrTable':swL2PortErrTable,'swL2PortErrEntry':swL2PortErrEntry,_k:swL2PortErrPortIndex,'swL2PortErrPortState':swL2PortErrPortState,'swL2PortErrPortStatus':swL2PortErrPortStatus,'swL2PortErrPortReason':swL2PortErrPortReason,'swL2PortErrDescription':swL2PortErrDescription,'swL2QOSMgmt':swL2QOSMgmt,'swL2QOSBandwidthControlTable':swL2QOSBandwidthControlTable,'swL2QOSBandwidthControlEntry':swL2QOSBandwidthControlEntry,_m:swL2QOSBandwidthPortIndex,'swL2QOSBandwidthRxRate':swL2QOSBandwidthRxRate,'swL2QOSBandwidthTxRate':swL2QOSBandwidthTxRate,'swL2QOSBandwidthRadiusRxRate':swL2QOSBandwidthRadiusRxRate,'swL2QOSBandwidthRadiusTxRate':swL2QOSBandwidthRadiusTxRate,'swL2QOSSchedulingTable':swL2QOSSchedulingTable,'swL2QOSSchedulingEntry':swL2QOSSchedulingEntry,_n:swL2QOSSchedulingClassIndex,'swL2QOSSchedulingMaxWeight':swL2QOSSchedulingMaxWeight,'swL2QOS8021pUserPriorityTable':swL2QOS8021pUserPriorityTable,'swL2QOS8021pUserPriorityEntry':swL2QOS8021pUserPriorityEntry,_o:swL2QOS8021pUserPriorityIndex,'swL2QOS8021pUserPriorityClass':swL2QOS8021pUserPriorityClass,'swL2QOS8021pDefaultPriorityTable':swL2QOS8021pDefaultPriorityTable,'swL2QOS8021pDefaultPriorityEntry':swL2QOS8021pDefaultPriorityEntry,_p:swL2QOS8021pDefaultPriorityIndex,'swL2QOS8021pDefaultPriority':swL2QOS8021pDefaultPriority,'swL2QOS8021pRadiusPriority':swL2QOS8021pRadiusPriority,'swL2QOSSchedulingMechanismCtrl':swL2QOSSchedulingMechanismCtrl,'swL2TrunkMgmt':swL2TrunkMgmt,'swPortTrunkMaxEntries':swPortTrunkMaxEntries,'swPortTrunkMaxPortMembers':swPortTrunkMaxPortMembers,'swPortTrunkTable':swPortTrunkTable,'swPortTrunkEntry':swPortTrunkEntry,_q:swPortTrunkIndex,'swPortTrunkMasterPort':swPortTrunkMasterPort,'swPortTrunkPortList':swPortTrunkPortList,'swPortTrunkType':swPortTrunkType,'swPortTrunkActivePort':swPortTrunkActivePort,'swPortTrunkState':swPortTrunkState,'swPortTrunkFloodingPort':swPortTrunkFloodingPort,'swL2TrunkAlgorithm':swL2TrunkAlgorithm,'swL2TrunkLACPPortTable':swL2TrunkLACPPortTable,'swL2TrunkLACPPortEntry':swL2TrunkLACPPortEntry,_s:swL2TrunkLACPPortIndex,'swL2TrunkLACPPortState':swL2TrunkLACPPortState,'swL2TrunkVLANTable':swL2TrunkVLANTable,'swL2TrunkVLANEntry':swL2TrunkVLANEntry,_t:swL2TrunkVLANPort,'swL2TrunkVLANState':swL2TrunkVLANState,'swPortMirrorPackage':swPortMirrorPackage,'swPortMirrorRxPortList':swPortMirrorRxPortList,'swPortMirrorTxPortList':swPortMirrorTxPortList,'swPortMirrorTargetPort':swPortMirrorTargetPort,'swPortMirrorState':swPortMirrorState,'swIGMPPackage':swIGMPPackage,'swL2IGMPMaxSupportedVlans':swL2IGMPMaxSupportedVlans,'swL2IGMPMaxIpGroupNumPerVlan':swL2IGMPMaxIpGroupNumPerVlan,'swL2IGMPCtrlTable':swL2IGMPCtrlTable,'swL2IGMPCtrlEntry':swL2IGMPCtrlEntry,_u:swL2IGMPCtrlVid,'swL2IGMPQueryInterval':swL2IGMPQueryInterval,'swL2IGMPMaxResponseTime':swL2IGMPMaxResponseTime,'swL2IGMPRobustness':swL2IGMPRobustness,'swL2IGMPLastMemberQueryInterval':swL2IGMPLastMemberQueryInterval,'swL2IGMPHostTimeout':swL2IGMPHostTimeout,'swL2IGMPRouteTimeout':swL2IGMPRouteTimeout,'swL2IGMPLeaveTimer':swL2IGMPLeaveTimer,'swL2IGMPQueryState':swL2IGMPQueryState,'swL2IGMPCurrentState':swL2IGMPCurrentState,'swL2IGMPCtrlState':swL2IGMPCtrlState,'swL2IGMPFastLeave':swL2IGMPFastLeave,'swL2IGMPQueryInfoTable':swL2IGMPQueryInfoTable,'swL2IGMPQueryInfoEntry':swL2IGMPQueryInfoEntry,_v:swL2IGMPInfoVid,'swL2IGMPInfoQueryCount':swL2IGMPInfoQueryCount,'swL2IGMPInfoTxQueryCount':swL2IGMPInfoTxQueryCount,'swL2IGMPInfoTable':swL2IGMPInfoTable,'swL2IGMPInfoEntry':swL2IGMPInfoEntry,_w:swL2IGMPVid,_x:swL2IGMPGroupIpAddr,'swL2IGMPMacAddr':swL2IGMPMacAddr,'swL2IGMPPortMap':swL2IGMPPortMap,'swL2IGMPIpGroupReportCount':swL2IGMPIpGroupReportCount,'swL2IGMPRouterPortTable':swL2IGMPRouterPortTable,'swL2IGMPRouterPortEntry':swL2IGMPRouterPortEntry,_y:swL2IGMPRouterPortVlanid,'swL2IGMPRouterPortVlanName':swL2IGMPRouterPortVlanName,'swL2IGMPRouterPortStaticPortList':swL2IGMPRouterPortStaticPortList,'swL2IGMPRouterPortDynamicPortList':swL2IGMPRouterPortDynamicPortList,'swL2IGMPRouterPortForbiddenPortList':swL2IGMPRouterPortForbiddenPortList,'swL2IGMPAccessAuthTable':swL2IGMPAccessAuthTable,'swL2IGMPAccessAuthEntry':swL2IGMPAccessAuthEntry,_z:swL2IGMPAccessAuthPort,'swL2IGMPAccessAuthState':swL2IGMPAccessAuthState,'swL2TrafficMgmt':swL2TrafficMgmt,'swL2TrafficCtrlTable':swL2TrafficCtrlTable,'swL2TrafficCtrlEntry':swL2TrafficCtrlEntry,_A0:swL2TrafficCtrlGroupIndex,'swL2TrafficCtrlUnitIndex':swL2TrafficCtrlUnitIndex,'swL2TrafficCtrlBMStromthreshold':swL2TrafficCtrlBMStromthreshold,'swL2TrafficCtrlBcastStromCtrl':swL2TrafficCtrlBcastStromCtrl,'swL2TrafficCtrlMcastStromCtrl':swL2TrafficCtrlMcastStromCtrl,'swL2TrafficCtrlUcastStromCtrl':swL2TrafficCtrlUcastStromCtrl,'swL2TrafficSegMgmt':swL2TrafficSegMgmt,'swL2TrafficSegTable':swL2TrafficSegTable,'swL2TrafficSegEntry':swL2TrafficSegEntry,_A1:swL2TrafficSegPort,'swL2TrafficSegForwardPorts':swL2TrafficSegForwardPorts,'swL2PortSecurityMgmt':swL2PortSecurityMgmt,'swL2PortSecurityControlTable':swL2PortSecurityControlTable,'swL2PortSecurityControlEntry':swL2PortSecurityControlEntry,_Q:swL2PortSecurityPortIndex,'swL2PortSecurityMaxLernAddr':swL2PortSecurityMaxLernAddr,'swL2PortSecurityMode':swL2PortSecurityMode,'swL2PortSecurityAdmState':swL2PortSecurityAdmState,'swL2PortSecurityTrapLogState':swL2PortSecurityTrapLogState,'swL2StpMgmt':swL2StpMgmt,'swL2StpForwardBPDU':swL2StpForwardBPDU,'swL2StpLbd':swL2StpLbd,'swL2StpLbdRecoverTime':swL2StpLbdRecoverTime,'swL2StpPortTable':swL2StpPortTable,'swL2StpPortEntry':swL2StpPortEntry,_A2:swL2StpPort,'swL2StpPortLbd':swL2StpPortLbd,'swL2StpPortStatus':swL2StpPortStatus,'swL2StpPortRole':swL2StpPortRole,'swL2StpPortFBPDU':swL2StpPortFBPDU,'swL2StpPortLinkState':swL2StpPortLinkState,'swL2StpPortProtocolMigration':swL2StpPortProtocolMigration,'swL2StpPortAdminEdgePort':swL2StpPortAdminEdgePort,'swL2StpPortOperEdgePort':swL2StpPortOperEdgePort,'swL2StpPortAdminPointToPoint':swL2StpPortAdminPointToPoint,'swL2StpPortOperPointToPoint':swL2StpPortOperPointToPoint,'swL2StpPortAdminPathCost':swL2StpPortAdminPathCost,'swL2StpPortPriority':swL2StpPortPriority,'swL2STPPortState':swL2STPPortState,'swL2StpPortRestrictedRole':swL2StpPortRestrictedRole,'swL2StpPortRestrictedTCN':swL2StpPortRestrictedTCN,'swL2CosMgmt':swL2CosMgmt,'swL2CosPriorityCtrl':swL2CosPriorityCtrl,'swL2CosPriorityTable':swL2CosPriorityTable,'swL2CosPriorityEntry':swL2CosPriorityEntry,_A5:swL2CosPriorityPort,'swL2CosPriorityPortPRI':swL2CosPriorityPortPRI,'swL2CosPriorityEtherPRI':swL2CosPriorityEtherPRI,'swL2CosPriorityIpPRI':swL2CosPriorityIpPRI,'swL2CosPriorityNone':swL2CosPriorityNone,'swL2CosPortPRITable':swL2CosPortPRITable,'swL2CosPortPRIEntry':swL2CosPortPRIEntry,_A6:swL2CosPortPRIIndex,'swL2CosPortPRIClass':swL2CosPortPRIClass,'swL2CosMacBasePRITable':swL2CosMacBasePRITable,'swL2CosMacBasePRIEntry':swL2CosMacBasePRIEntry,_A7:swL2CosMacBasePRIIndex,'swL2CosMacBasePRIClass':swL2CosMacBasePRIClass,'swL2CosTosPRITable':swL2CosTosPRITable,'swL2CosTosPRIEntry':swL2CosTosPRIEntry,_A8:swL2CosTosPRIIndex,'swL2CosTosPRIClass':swL2CosTosPRIClass,'swL2CosDscpPRITable':swL2CosDscpPRITable,'swL2CosDscpPRIEntry':swL2CosDscpPRIEntry,_A9:swL2CosDscpPRIIndex,'swL2CosDscpPRIClass':swL2CosDscpPRIClass,'swL2LoopDetectMgmt':swL2LoopDetectMgmt,'swL2LoopDetectCtrl':swL2LoopDetectCtrl,'swL2LoopDetectAdminState':swL2LoopDetectAdminState,'swL2LoopDetectInterval':swL2LoopDetectInterval,'swL2LoopDetectRecoverTime':swL2LoopDetectRecoverTime,'swL2LoopDetectPortMgmt':swL2LoopDetectPortMgmt,'swL2LoopDetectPortTable':swL2LoopDetectPortTable,'swL2LoopDetectPortEntry':swL2LoopDetectPortEntry,_AA:swL2LoopDetectPortIndex,'swL2LoopDetectPortState':swL2LoopDetectPortState,'swL2LoopDetectPortLoopStatus':swL2LoopDetectPortLoopStatus,'swL2VLANMgmt':swL2VLANMgmt,'swL2VlanTable':swL2VlanTable,'swL2VlanEntry':swL2VlanEntry,_AB:swL2VlanIndex,'swL2VlanName':swL2VlanName,'swL2VlanType':swL2VlanType,'swL2VlanMemberPorts':swL2VlanMemberPorts,'swL2VlanStaticPorts':swL2VlanStaticPorts,'swL2VlanUntaggedPorts':swL2VlanUntaggedPorts,'swL2VlanTaggedPorts':swL2VlanTaggedPorts,'swL2MgmtMIBTraps':swL2MgmtMIBTraps,'swL2Notify':swL2Notify,'swL2NotifyPrefix':swL2NotifyPrefix,'swL2NotifFirmware':swL2NotifFirmware,'swL2macNotification':swL2macNotification,'swL2PortSecurityViolationTrap':swL2PortSecurityViolationTrap,'swl2NotificationBidings':swl2NotificationBidings,_AC:swL2macNotifyInfo,_AD:swL2PortSecurityViolationMac})