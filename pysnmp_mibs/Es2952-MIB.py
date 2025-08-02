_AL='loopDetectTrunkBlockStatus'
_AK='trunkPorts'
_AJ='loopDetectTrunkInVlan'
_AI='loopDetectPortBlockStatus'
_AH='loopDetectPortInVlan'
_AG='dynamicMacMaxCount'
_AF='opticalInfoPortId'
_AE='registered'
_AD='fdbFilterAddress'
_AC='globalRuleID'
_AB='globalACLNo'
_AA='hybridRuleID'
_A9='hybridACLNo'
_A8='linkRuleID'
_A7='linkACLNo'
_A6='extendedRuleID'
_A5='extendedACLNo'
_A4='basicRuleID'
_A3='basicACLNo'
_A2='timeRangeName'
_A1='commuName'
_A0='traphostType'
_z='traphostIP'
_y='viewName'
_x='viewIndex'
_w='communityName'
_v='userName'
_u='serverId'
_t='vctPortId'
_s='ingressPortId'
_r='MacAddress'
_q='layer3PortId'
_p='lacpPortId'
_o='trunkId'
_n='sessionId'
_m='portID'
_l='queueID'
_k='gePortSessionID'
_j='gePortID'
_i='sessionNo'
_h='fePortID'
_g='policerID'
_f='assVlanId'
_e='vlanId'
_d='discard'
_c='forward'
_b='null'
_a='invalid'
_Z='fdbStaticAddress'
_Y='clear'
_X='loopDetectTrunkId'
_W='loopDetectPortId'
_V='ipPriority'
_U='fdbID'
_T='impMismatch'
_S='open'
_R='good'
_Q='short'
_P='remoteMAC'
_O='switchMac'
_N='yes'
_M='no'
_L='DisplayString'
_K='Unsigned32'
_J='portId'
_I='OctetString'
_H='disable'
_G='enable'
_F='not-accessible'
_E='Es2952-MIB'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
class PortList(TextualConvention,OctetString):status=_A
class MacAddress(TextualConvention,OctetString):status=_A
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_EthernetSwitch_ObjectIdentity=ObjectIdentity
ethernetSwitch=_EthernetSwitch_ObjectIdentity((1,3,6,1,4,1,3902,15))
_Layer2Switch_ObjectIdentity=ObjectIdentity
layer2Switch=_Layer2Switch_ObjectIdentity((1,3,6,1,4,1,3902,15,2))
_Series2952Switch_ObjectIdentity=ObjectIdentity
series2952Switch=_Series2952Switch_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11))
_SwitchSystem_ObjectIdentity=ObjectIdentity
switchSystem=_SwitchSystem_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,1))
_CpuLoad5s_Type=Integer32
_CpuLoad5s_Object=MibScalar
cpuLoad5s=_CpuLoad5s_Object((1,3,6,1,4,1,3902,15,2,11,1,1),_CpuLoad5s_Type())
cpuLoad5s.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuLoad5s.setStatus(_A)
_CpuLoad30s_Type=Integer32
_CpuLoad30s_Object=MibScalar
cpuLoad30s=_CpuLoad30s_Object((1,3,6,1,4,1,3902,15,2,11,1,2),_CpuLoad30s_Type())
cpuLoad30s.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuLoad30s.setStatus(_A)
_CpuLoad2m_Type=Integer32
_CpuLoad2m_Object=MibScalar
cpuLoad2m=_CpuLoad2m_Object((1,3,6,1,4,1,3902,15,2,11,1,3),_CpuLoad2m_Type())
cpuLoad2m.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuLoad2m.setStatus(_A)
_MaxCpuLoad_Type=Integer32
_MaxCpuLoad_Object=MibScalar
maxCpuLoad=_MaxCpuLoad_Object((1,3,6,1,4,1,3902,15,2,11,1,4),_MaxCpuLoad_Type())
maxCpuLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:maxCpuLoad.setStatus(_A)
_MemUtilityRatio_Type=Integer32
_MemUtilityRatio_Object=MibScalar
memUtilityRatio=_MemUtilityRatio_Object((1,3,6,1,4,1,3902,15,2,11,1,5),_MemUtilityRatio_Type())
memUtilityRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:memUtilityRatio.setStatus(_A)
_SwitchType_Type=OctetString
_SwitchType_Object=MibScalar
switchType=_SwitchType_Object((1,3,6,1,4,1,3902,15,2,11,1,6),_SwitchType_Type())
switchType.setMaxAccess(_C)
if mibBuilder.loadTexts:switchType.setStatus(_A)
_SwitchMac_Type=MacAddress
_SwitchMac_Object=MibScalar
switchMac=_SwitchMac_Object((1,3,6,1,4,1,3902,15,2,11,1,7),_SwitchMac_Type())
switchMac.setMaxAccess(_C)
if mibBuilder.loadTexts:switchMac.setStatus(_A)
class _Reboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_Reboot_Type.__name__=_D
_Reboot_Object=MibScalar
reboot=_Reboot_Object((1,3,6,1,4,1,3902,15,2,11,1,8),_Reboot_Type())
reboot.setMaxAccess(_B)
if mibBuilder.loadTexts:reboot.setStatus(_A)
class _SaveConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_SaveConfig_Type.__name__=_D
_SaveConfig_Object=MibScalar
saveConfig=_SaveConfig_Object((1,3,6,1,4,1,3902,15,2,11,1,9),_SaveConfig_Type())
saveConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:saveConfig.setStatus(_A)
class _SysDateTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SysDateTime_Type.__name__=_I
_SysDateTime_Object=MibScalar
sysDateTime=_SysDateTime_Object((1,3,6,1,4,1,3902,15,2,11,1,10),_SysDateTime_Type())
sysDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sysDateTime.setStatus(_A)
_Port_ObjectIdentity=ObjectIdentity
port=_Port_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,2))
_PortNumber_Type=Unsigned32
_PortNumber_Object=MibScalar
portNumber=_PortNumber_Object((1,3,6,1,4,1,3902,15,2,11,2,1),_PortNumber_Type())
portNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:portNumber.setStatus(_A)
_PortTable_Object=MibTable
portTable=_PortTable_Object((1,3,6,1,4,1,3902,15,2,11,2,4))
if mibBuilder.loadTexts:portTable.setStatus(_A)
_PortEntry_Object=MibTableRow
portEntry=_PortEntry_Object((1,3,6,1,4,1,3902,15,2,11,2,4,1))
portEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:portEntry.setStatus(_A)
_PortId_Type=Unsigned32
_PortId_Object=MibTableColumn
portId=_PortId_Object((1,3,6,1,4,1,3902,15,2,11,2,4,1,1),_PortId_Type())
portId.setMaxAccess(_C)
if mibBuilder.loadTexts:portId.setStatus(_A)
class _PortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,200))
_PortName_Type.__name__=_I
_PortName_Object=MibTableColumn
portName=_PortName_Object((1,3,6,1,4,1,3902,15,2,11,2,4,1,2),_PortName_Type())
portName.setMaxAccess(_B)
if mibBuilder.loadTexts:portName.setStatus(_A)
class _PortDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,200))
_PortDescr_Type.__name__=_I
_PortDescr_Object=MibTableColumn
portDescr=_PortDescr_Object((1,3,6,1,4,1,3902,15,2,11,2,4,1,3),_PortDescr_Type())
portDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:portDescr.setStatus(_A)
class _PortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_PortAdminStatus_Type.__name__=_D
_PortAdminStatus_Object=MibTableColumn
portAdminStatus=_PortAdminStatus_Object((1,3,6,1,4,1,3902,15,2,11,2,4,1,4),_PortAdminStatus_Type())
portAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:portAdminStatus.setStatus(_A)
class _PortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('linkUp',1),('linkDown',2)))
_PortOperStatus_Type.__name__=_D
_PortOperStatus_Object=MibTableColumn
portOperStatus=_PortOperStatus_Object((1,3,6,1,4,1,3902,15,2,11,2,4,1,5),_PortOperStatus_Type())
portOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:portOperStatus.setStatus(_A)
class _PortAdminWorkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('auto-10M',1),('auto-100M',2),('auto-1000M',3),('auto-auto',4),('half-10M',5),('half-100M',6),('half-1000M',7),('half-auto',8),('full-10M',9),('full-100M',10),('full-1000M',11),('full-auto',12)))
_PortAdminWorkMode_Type.__name__=_D
_PortAdminWorkMode_Object=MibTableColumn
portAdminWorkMode=_PortAdminWorkMode_Object((1,3,6,1,4,1,3902,15,2,11,2,4,1,6),_PortAdminWorkMode_Type())
portAdminWorkMode.setMaxAccess(_B)
if mibBuilder.loadTexts:portAdminWorkMode.setStatus(_A)
class _PortOperDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('full',1),('half',2)))
_PortOperDuplex_Type.__name__=_D
_PortOperDuplex_Object=MibTableColumn
portOperDuplex=_PortOperDuplex_Object((1,3,6,1,4,1,3902,15,2,11,2,4,1,7),_PortOperDuplex_Type())
portOperDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:portOperDuplex.setStatus(_A)
class _PortOperSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('speed-10M',1),('speed-100M',2),('speed-1000M',3)))
_PortOperSpeed_Type.__name__=_D
_PortOperSpeed_Object=MibTableColumn
portOperSpeed=_PortOperSpeed_Object((1,3,6,1,4,1,3902,15,2,11,2,4,1,8),_PortOperSpeed_Type())
portOperSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:portOperSpeed.setStatus(_A)
class _PortPvid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_PortPvid_Type.__name__=_D
_PortPvid_Object=MibTableColumn
portPvid=_PortPvid_Object((1,3,6,1,4,1,3902,15,2,11,2,4,1,9),_PortPvid_Type())
portPvid.setMaxAccess(_B)
if mibBuilder.loadTexts:portPvid.setStatus(_A)
class _PortFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_PortFlowControl_Type.__name__=_D
_PortFlowControl_Object=MibTableColumn
portFlowControl=_PortFlowControl_Object((1,3,6,1,4,1,3902,15,2,11,2,4,1,10),_PortFlowControl_Type())
portFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:portFlowControl.setStatus(_A)
_PortVlanMode_Type=OctetString
_PortVlanMode_Object=MibTableColumn
portVlanMode=_PortVlanMode_Object((1,3,6,1,4,1,3902,15,2,11,2,4,1,11),_PortVlanMode_Type())
portVlanMode.setMaxAccess(_B)
if mibBuilder.loadTexts:portVlanMode.setStatus(_A)
class _PortSecurity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_PortSecurity_Type.__name__=_D
_PortSecurity_Object=MibTableColumn
portSecurity=_PortSecurity_Object((1,3,6,1,4,1,3902,15,2,11,2,4,1,12),_PortSecurity_Type())
portSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:portSecurity.setStatus(_A)
class _PortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PortPriority_Type.__name__=_D
_PortPriority_Object=MibTableColumn
portPriority=_PortPriority_Object((1,3,6,1,4,1,3902,15,2,11,2,4,1,13),_PortPriority_Type())
portPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:portPriority.setStatus(_A)
class _PortMulticast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_PortMulticast_Type.__name__=_D
_PortMulticast_Object=MibTableColumn
portMulticast=_PortMulticast_Object((1,3,6,1,4,1,3902,15,2,11,2,4,1,14),_PortMulticast_Type())
portMulticast.setMaxAccess(_B)
if mibBuilder.loadTexts:portMulticast.setStatus(_A)
class _PortMediaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('mt100BaseT',1),('mt100BaseFX',2),('mt1000BaseX',3),('mt1000BaseT',4),('unKnown',5)))
_PortMediaType_Type.__name__=_D
_PortMediaType_Object=MibTableColumn
portMediaType=_PortMediaType_Object((1,3,6,1,4,1,3902,15,2,11,2,4,1,15),_PortMediaType_Type())
portMediaType.setMaxAccess(_C)
if mibBuilder.loadTexts:portMediaType.setStatus(_A)
class _IsPortInTrunk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_IsPortInTrunk_Type.__name__=_D
_IsPortInTrunk_Object=MibTableColumn
isPortInTrunk=_IsPortInTrunk_Object((1,3,6,1,4,1,3902,15,2,11,2,4,1,16),_IsPortInTrunk_Type())
isPortInTrunk.setMaxAccess(_C)
if mibBuilder.loadTexts:isPortInTrunk.setStatus(_A)
class _PortLoopdetectStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,200))
_PortLoopdetectStatus_Type.__name__=_I
_PortLoopdetectStatus_Object=MibTableColumn
portLoopdetectStatus=_PortLoopdetectStatus_Object((1,3,6,1,4,1,3902,15,2,11,2,4,1,17),_PortLoopdetectStatus_Type())
portLoopdetectStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:portLoopdetectStatus.setStatus(_A)
class _DynamicMacMaxCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DynamicMacMaxCount_Type.__name__=_D
_DynamicMacMaxCount_Object=MibTableColumn
dynamicMacMaxCount=_DynamicMacMaxCount_Object((1,3,6,1,4,1,3902,15,2,11,2,4,1,18),_DynamicMacMaxCount_Type())
dynamicMacMaxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dynamicMacMaxCount.setStatus(_A)
_Vlan_ObjectIdentity=ObjectIdentity
vlan=_Vlan_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,3))
_MaxVlanId_Type=Unsigned32
_MaxVlanId_Object=MibScalar
maxVlanId=_MaxVlanId_Object((1,3,6,1,4,1,3902,15,2,11,3,1),_MaxVlanId_Type())
maxVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:maxVlanId.setStatus(_A)
_MaxSupportedVlans_Type=Unsigned32
_MaxSupportedVlans_Object=MibScalar
maxSupportedVlans=_MaxSupportedVlans_Object((1,3,6,1,4,1,3902,15,2,11,3,2),_MaxSupportedVlans_Type())
maxSupportedVlans.setMaxAccess(_C)
if mibBuilder.loadTexts:maxSupportedVlans.setStatus(_A)
_VlanTable_Object=MibTable
vlanTable=_VlanTable_Object((1,3,6,1,4,1,3902,15,2,11,3,3))
if mibBuilder.loadTexts:vlanTable.setStatus(_A)
_VlanEntry_Object=MibTableRow
vlanEntry=_VlanEntry_Object((1,3,6,1,4,1,3902,15,2,11,3,3,1))
vlanEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:vlanEntry.setStatus(_A)
class _VlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VlanId_Type.__name__=_D
_VlanId_Object=MibTableColumn
vlanId=_VlanId_Object((1,3,6,1,4,1,3902,15,2,11,3,3,1,1),_VlanId_Type())
vlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:vlanId.setStatus(_A)
_VlanUntaggedPorts_Type=PortList
_VlanUntaggedPorts_Object=MibTableColumn
vlanUntaggedPorts=_VlanUntaggedPorts_Object((1,3,6,1,4,1,3902,15,2,11,3,3,1,3),_VlanUntaggedPorts_Type())
vlanUntaggedPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanUntaggedPorts.setStatus(_A)
_VlanTaggedPorts_Type=PortList
_VlanTaggedPorts_Object=MibTableColumn
vlanTaggedPorts=_VlanTaggedPorts_Object((1,3,6,1,4,1,3902,15,2,11,3,3,1,4),_VlanTaggedPorts_Type())
vlanTaggedPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanTaggedPorts.setStatus(_A)
class _VlanName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_VlanName_Type.__name__=_I
_VlanName_Object=MibTableColumn
vlanName=_VlanName_Object((1,3,6,1,4,1,3902,15,2,11,3,3,1,5),_VlanName_Type())
vlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanName.setStatus(_A)
class _VlanAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_VlanAdminStatus_Type.__name__=_D
_VlanAdminStatus_Object=MibTableColumn
vlanAdminStatus=_VlanAdminStatus_Object((1,3,6,1,4,1,3902,15,2,11,3,3,1,6),_VlanAdminStatus_Type())
vlanAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanAdminStatus.setStatus(_A)
_VlanUntaggedTrunks_Type=PortList
_VlanUntaggedTrunks_Object=MibTableColumn
vlanUntaggedTrunks=_VlanUntaggedTrunks_Object((1,3,6,1,4,1,3902,15,2,11,3,3,1,7),_VlanUntaggedTrunks_Type())
vlanUntaggedTrunks.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanUntaggedTrunks.setStatus(_A)
_VlanTaggedTrunks_Type=PortList
_VlanTaggedTrunks_Object=MibTableColumn
vlanTaggedTrunks=_VlanTaggedTrunks_Object((1,3,6,1,4,1,3902,15,2,11,3,3,1,8),_VlanTaggedTrunks_Type())
vlanTaggedTrunks.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanTaggedTrunks.setStatus(_A)
_VlanAssistantTable_Object=MibTable
vlanAssistantTable=_VlanAssistantTable_Object((1,3,6,1,4,1,3902,15,2,11,3,4))
if mibBuilder.loadTexts:vlanAssistantTable.setStatus(_A)
_VlanAssistantEntry_Object=MibTableRow
vlanAssistantEntry=_VlanAssistantEntry_Object((1,3,6,1,4,1,3902,15,2,11,3,4,1))
vlanAssistantEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:vlanAssistantEntry.setStatus(_A)
_AssVlanId_Type=Integer32
_AssVlanId_Object=MibTableColumn
assVlanId=_AssVlanId_Object((1,3,6,1,4,1,3902,15,2,11,3,4,1,1),_AssVlanId_Type())
assVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:assVlanId.setStatus(_A)
_Mirror_ObjectIdentity=ObjectIdentity
mirror=_Mirror_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,4))
_SourcePortsIngress_Type=PortList
_SourcePortsIngress_Object=MibScalar
sourcePortsIngress=_SourcePortsIngress_Object((1,3,6,1,4,1,3902,15,2,11,4,1),_SourcePortsIngress_Type())
sourcePortsIngress.setMaxAccess(_B)
if mibBuilder.loadTexts:sourcePortsIngress.setStatus(_A)
_SourcePortsEgress_Type=PortList
_SourcePortsEgress_Object=MibScalar
sourcePortsEgress=_SourcePortsEgress_Object((1,3,6,1,4,1,3902,15,2,11,4,2),_SourcePortsEgress_Type())
sourcePortsEgress.setMaxAccess(_B)
if mibBuilder.loadTexts:sourcePortsEgress.setStatus(_A)
_DesPortIngress_Type=Unsigned32
_DesPortIngress_Object=MibScalar
desPortIngress=_DesPortIngress_Object((1,3,6,1,4,1,3902,15,2,11,4,3),_DesPortIngress_Type())
desPortIngress.setMaxAccess(_B)
if mibBuilder.loadTexts:desPortIngress.setStatus(_A)
_DesPortEgress_Type=Unsigned32
_DesPortEgress_Object=MibScalar
desPortEgress=_DesPortEgress_Object((1,3,6,1,4,1,3902,15,2,11,4,4),_DesPortEgress_Type())
desPortEgress.setMaxAccess(_B)
if mibBuilder.loadTexts:desPortEgress.setStatus(_A)
_Qos_ObjectIdentity=ObjectIdentity
qos=_Qos_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,5))
class _QueueScheduleWeight_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_QueueScheduleWeight_Type.__name__=_I
_QueueScheduleWeight_Object=MibScalar
queueScheduleWeight=_QueueScheduleWeight_Object((1,3,6,1,4,1,3902,15,2,11,5,1),_QueueScheduleWeight_Type())
queueScheduleWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:queueScheduleWeight.setStatus(_A)
class _QueueScheduleMode0_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_QueueScheduleMode0_Type.__name__=_I
_QueueScheduleMode0_Object=MibScalar
queueScheduleMode0=_QueueScheduleMode0_Object((1,3,6,1,4,1,3902,15,2,11,5,2),_QueueScheduleMode0_Type())
queueScheduleMode0.setMaxAccess(_C)
if mibBuilder.loadTexts:queueScheduleMode0.setStatus(_A)
class _QueueScheduleMode1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_QueueScheduleMode1_Type.__name__=_I
_QueueScheduleMode1_Object=MibScalar
queueScheduleMode1=_QueueScheduleMode1_Object((1,3,6,1,4,1,3902,15,2,11,5,3),_QueueScheduleMode1_Type())
queueScheduleMode1.setMaxAccess(_C)
if mibBuilder.loadTexts:queueScheduleMode1.setStatus(_A)
class _QueueScheduleMode2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_QueueScheduleMode2_Type.__name__=_I
_QueueScheduleMode2_Object=MibScalar
queueScheduleMode2=_QueueScheduleMode2_Object((1,3,6,1,4,1,3902,15,2,11,5,4),_QueueScheduleMode2_Type())
queueScheduleMode2.setMaxAccess(_C)
if mibBuilder.loadTexts:queueScheduleMode2.setStatus(_A)
class _QueueScheduleMode3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_QueueScheduleMode3_Type.__name__=_I
_QueueScheduleMode3_Object=MibScalar
queueScheduleMode3=_QueueScheduleMode3_Object((1,3,6,1,4,1,3902,15,2,11,5,5),_QueueScheduleMode3_Type())
queueScheduleMode3.setMaxAccess(_C)
if mibBuilder.loadTexts:queueScheduleMode3.setStatus(_A)
_QosPrimapUsrToTraffic_Type=OctetString
_QosPrimapUsrToTraffic_Object=MibScalar
qosPrimapUsrToTraffic=_QosPrimapUsrToTraffic_Object((1,3,6,1,4,1,3902,15,2,11,5,6),_QosPrimapUsrToTraffic_Type())
qosPrimapUsrToTraffic.setMaxAccess(_B)
if mibBuilder.loadTexts:qosPrimapUsrToTraffic.setStatus(_A)
_QosPolicerTable_Object=MibTable
qosPolicerTable=_QosPolicerTable_Object((1,3,6,1,4,1,3902,15,2,11,5,7))
if mibBuilder.loadTexts:qosPolicerTable.setStatus(_A)
_QosPolicerEntry_Object=MibTableRow
qosPolicerEntry=_QosPolicerEntry_Object((1,3,6,1,4,1,3902,15,2,11,5,7,1))
qosPolicerEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:qosPolicerEntry.setStatus(_A)
_PolicerID_Type=Unsigned32
_PolicerID_Object=MibTableColumn
policerID=_PolicerID_Object((1,3,6,1,4,1,3902,15,2,11,5,7,1,1),_PolicerID_Type())
policerID.setMaxAccess(_F)
if mibBuilder.loadTexts:policerID.setStatus(_A)
_QosPolicerPara_Type=Unsigned32
_QosPolicerPara_Object=MibTableColumn
qosPolicerPara=_QosPolicerPara_Object((1,3,6,1,4,1,3902,15,2,11,5,7,1,2),_QosPolicerPara_Type())
qosPolicerPara.setMaxAccess(_B)
if mibBuilder.loadTexts:qosPolicerPara.setStatus(_A)
class _QosExceededOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noOperation',1),('drop',2)))
_QosExceededOper_Type.__name__=_D
_QosExceededOper_Object=MibTableColumn
qosExceededOper=_QosExceededOper_Object((1,3,6,1,4,1,3902,15,2,11,5,7,1,3),_QosExceededOper_Type())
qosExceededOper.setMaxAccess(_B)
if mibBuilder.loadTexts:qosExceededOper.setStatus(_A)
_QosPolicerBurst_Type=Unsigned32
_QosPolicerBurst_Object=MibTableColumn
qosPolicerBurst=_QosPolicerBurst_Object((1,3,6,1,4,1,3902,15,2,11,5,7,1,4),_QosPolicerBurst_Type())
qosPolicerBurst.setMaxAccess(_B)
if mibBuilder.loadTexts:qosPolicerBurst.setStatus(_A)
_IpPriToTrafficTable_Object=MibTable
ipPriToTrafficTable=_IpPriToTrafficTable_Object((1,3,6,1,4,1,3902,15,2,11,5,8))
if mibBuilder.loadTexts:ipPriToTrafficTable.setStatus(_A)
_IpPriToTrafficEntry_Object=MibTableRow
ipPriToTrafficEntry=_IpPriToTrafficEntry_Object((1,3,6,1,4,1,3902,15,2,11,5,8,1))
ipPriToTrafficEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:ipPriToTrafficEntry.setStatus(_A)
_IpPriority_Type=Unsigned32
_IpPriority_Object=MibTableColumn
ipPriority=_IpPriority_Object((1,3,6,1,4,1,3902,15,2,11,5,8,1,1),_IpPriority_Type())
ipPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:ipPriority.setStatus(_A)
class _TcFePort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_TcFePort_Type.__name__=_K
_TcFePort_Object=MibTableColumn
tcFePort=_TcFePort_Object((1,3,6,1,4,1,3902,15,2,11,5,8,1,2),_TcFePort_Type())
tcFePort.setMaxAccess(_B)
if mibBuilder.loadTexts:tcFePort.setStatus(_A)
class _TcGePort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_TcGePort_Type.__name__=_K
_TcGePort_Object=MibTableColumn
tcGePort=_TcGePort_Object((1,3,6,1,4,1,3902,15,2,11,5,8,1,3),_TcGePort_Type())
tcGePort.setMaxAccess(_B)
if mibBuilder.loadTexts:tcGePort.setStatus(_A)
_FePortIngBandTable_Object=MibTable
fePortIngBandTable=_FePortIngBandTable_Object((1,3,6,1,4,1,3902,15,2,11,5,9))
if mibBuilder.loadTexts:fePortIngBandTable.setStatus(_A)
_FePortIngBandEntry_Object=MibTableRow
fePortIngBandEntry=_FePortIngBandEntry_Object((1,3,6,1,4,1,3902,15,2,11,5,9,1))
fePortIngBandEntry.setIndexNames((0,_E,_h),(0,_E,_i))
if mibBuilder.loadTexts:fePortIngBandEntry.setStatus(_A)
_FePortID_Type=Unsigned32
_FePortID_Object=MibTableColumn
fePortID=_FePortID_Object((1,3,6,1,4,1,3902,15,2,11,5,9,1,1),_FePortID_Type())
fePortID.setMaxAccess(_C)
if mibBuilder.loadTexts:fePortID.setStatus(_A)
_SessionNo_Type=Unsigned32
_SessionNo_Object=MibTableColumn
sessionNo=_SessionNo_Object((1,3,6,1,4,1,3902,15,2,11,5,9,1,2),_SessionNo_Type())
sessionNo.setMaxAccess(_C)
if mibBuilder.loadTexts:sessionNo.setStatus(_A)
class _SessionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SessionStatus_Type.__name__=_D
_SessionStatus_Object=MibTableColumn
sessionStatus=_SessionStatus_Object((1,3,6,1,4,1,3902,15,2,11,5,9,1,3),_SessionStatus_Type())
sessionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sessionStatus.setStatus(_A)
_FeIngressRate_Type=Unsigned32
_FeIngressRate_Object=MibTableColumn
feIngressRate=_FeIngressRate_Object((1,3,6,1,4,1,3902,15,2,11,5,9,1,4),_FeIngressRate_Type())
feIngressRate.setMaxAccess(_B)
if mibBuilder.loadTexts:feIngressRate.setStatus(_A)
_FeIngressPkType_Type=PortList
_FeIngressPkType_Object=MibTableColumn
feIngressPkType=_FeIngressPkType_Object((1,3,6,1,4,1,3902,15,2,11,5,9,1,5),_FeIngressPkType_Type())
feIngressPkType.setMaxAccess(_B)
if mibBuilder.loadTexts:feIngressPkType.setStatus(_A)
_QuePriorityStatus_Type=PortList
_QuePriorityStatus_Object=MibTableColumn
quePriorityStatus=_QuePriorityStatus_Object((1,3,6,1,4,1,3902,15,2,11,5,9,1,6),_QuePriorityStatus_Type())
quePriorityStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:quePriorityStatus.setStatus(_A)
class _MgmtNoRatelimitStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MgmtNoRatelimitStatus_Type.__name__=_D
_MgmtNoRatelimitStatus_Object=MibTableColumn
mgmtNoRatelimitStatus=_MgmtNoRatelimitStatus_Object((1,3,6,1,4,1,3902,15,2,11,5,9,1,7),_MgmtNoRatelimitStatus_Type())
mgmtNoRatelimitStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmtNoRatelimitStatus.setStatus(_A)
_GePortIngBandTable_Object=MibTable
gePortIngBandTable=_GePortIngBandTable_Object((1,3,6,1,4,1,3902,15,2,11,5,10))
if mibBuilder.loadTexts:gePortIngBandTable.setStatus(_A)
_GePortIngBandEntry_Object=MibTableRow
gePortIngBandEntry=_GePortIngBandEntry_Object((1,3,6,1,4,1,3902,15,2,11,5,10,1))
gePortIngBandEntry.setIndexNames((0,_E,_j))
if mibBuilder.loadTexts:gePortIngBandEntry.setStatus(_A)
_GePortID_Type=Unsigned32
_GePortID_Object=MibTableColumn
gePortID=_GePortID_Object((1,3,6,1,4,1,3902,15,2,11,5,10,1,1),_GePortID_Type())
gePortID.setMaxAccess(_C)
if mibBuilder.loadTexts:gePortID.setStatus(_A)
class _GeIngressStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_GeIngressStatus_Type.__name__=_D
_GeIngressStatus_Object=MibTableColumn
geIngressStatus=_GeIngressStatus_Object((1,3,6,1,4,1,3902,15,2,11,5,10,1,2),_GeIngressStatus_Type())
geIngressStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:geIngressStatus.setStatus(_A)
_GeIngressRate_Type=Integer32
_GeIngressRate_Object=MibTableColumn
geIngressRate=_GeIngressRate_Object((1,3,6,1,4,1,3902,15,2,11,5,10,1,3),_GeIngressRate_Type())
geIngressRate.setMaxAccess(_B)
if mibBuilder.loadTexts:geIngressRate.setStatus(_A)
_GeIngressPkType_Type=PortList
_GeIngressPkType_Object=MibTableColumn
geIngressPkType=_GeIngressPkType_Object((1,3,6,1,4,1,3902,15,2,11,5,10,1,4),_GeIngressPkType_Type())
geIngressPkType.setMaxAccess(_B)
if mibBuilder.loadTexts:geIngressPkType.setStatus(_A)
_GeQueScheTable_Object=MibTable
geQueScheTable=_GeQueScheTable_Object((1,3,6,1,4,1,3902,15,2,11,5,11))
if mibBuilder.loadTexts:geQueScheTable.setStatus(_A)
_GeQueScheEntry_Object=MibTableRow
geQueScheEntry=_GeQueScheEntry_Object((1,3,6,1,4,1,3902,15,2,11,5,11,1))
geQueScheEntry.setIndexNames((0,_E,_k),(0,_E,_l))
if mibBuilder.loadTexts:geQueScheEntry.setStatus(_A)
_GePortSessionID_Type=Unsigned32
_GePortSessionID_Object=MibTableColumn
gePortSessionID=_GePortSessionID_Object((1,3,6,1,4,1,3902,15,2,11,5,11,1,1),_GePortSessionID_Type())
gePortSessionID.setMaxAccess(_F)
if mibBuilder.loadTexts:gePortSessionID.setStatus(_A)
_QueueID_Type=Unsigned32
_QueueID_Object=MibTableColumn
queueID=_QueueID_Object((1,3,6,1,4,1,3902,15,2,11,5,11,1,2),_QueueID_Type())
queueID.setMaxAccess(_F)
if mibBuilder.loadTexts:queueID.setStatus(_A)
_QueueSchedule_Type=OctetString
_QueueSchedule_Object=MibTableColumn
queueSchedule=_QueueSchedule_Object((1,3,6,1,4,1,3902,15,2,11,5,11,1,3),_QueueSchedule_Type())
queueSchedule.setMaxAccess(_B)
if mibBuilder.loadTexts:queueSchedule.setStatus(_A)
_GeQosPrimapUsrToTraffic_Type=OctetString
_GeQosPrimapUsrToTraffic_Object=MibScalar
geQosPrimapUsrToTraffic=_GeQosPrimapUsrToTraffic_Object((1,3,6,1,4,1,3902,15,2,11,5,12),_GeQosPrimapUsrToTraffic_Type())
geQosPrimapUsrToTraffic.setMaxAccess(_B)
if mibBuilder.loadTexts:geQosPrimapUsrToTraffic.setStatus(_A)
_GePortIp2UserTable_Object=MibTable
gePortIp2UserTable=_GePortIp2UserTable_Object((1,3,6,1,4,1,3902,15,2,11,5,13))
if mibBuilder.loadTexts:gePortIp2UserTable.setStatus(_A)
_GePortIp2UserEntry_Object=MibTableRow
gePortIp2UserEntry=_GePortIp2UserEntry_Object((1,3,6,1,4,1,3902,15,2,11,5,13,1))
gePortIp2UserEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:gePortIp2UserEntry.setStatus(_A)
class _UserPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_UserPriority_Type.__name__=_K
_UserPriority_Object=MibTableColumn
userPriority=_UserPriority_Object((1,3,6,1,4,1,3902,15,2,11,5,13,1,2),_UserPriority_Type())
userPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:userPriority.setStatus(_A)
_PortQosParamTable_Object=MibTable
portQosParamTable=_PortQosParamTable_Object((1,3,6,1,4,1,3902,15,2,11,5,14))
if mibBuilder.loadTexts:portQosParamTable.setStatus(_A)
_PortQosParamEntry_Object=MibTableRow
portQosParamEntry=_PortQosParamEntry_Object((1,3,6,1,4,1,3902,15,2,11,5,14,1))
portQosParamEntry.setIndexNames((0,_E,_m))
if mibBuilder.loadTexts:portQosParamEntry.setStatus(_A)
_PortID_Type=Unsigned32
_PortID_Object=MibTableColumn
portID=_PortID_Object((1,3,6,1,4,1,3902,15,2,11,5,14,1,1),_PortID_Type())
portID.setMaxAccess(_F)
if mibBuilder.loadTexts:portID.setStatus(_A)
_BandWidthEgress_Type=OctetString
_BandWidthEgress_Object=MibTableColumn
bandWidthEgress=_BandWidthEgress_Object((1,3,6,1,4,1,3902,15,2,11,5,14,1,2),_BandWidthEgress_Type())
bandWidthEgress.setMaxAccess(_B)
if mibBuilder.loadTexts:bandWidthEgress.setStatus(_A)
class _UpPriorityEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_UpPriorityEnable_Type.__name__=_D
_UpPriorityEnable_Object=MibTableColumn
upPriorityEnable=_UpPriorityEnable_Object((1,3,6,1,4,1,3902,15,2,11,5,14,1,3),_UpPriorityEnable_Type())
upPriorityEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:upPriorityEnable.setStatus(_A)
class _DscpPriorityEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DscpPriorityEnable_Type.__name__=_D
_DscpPriorityEnable_Object=MibTableColumn
dscpPriorityEnable=_DscpPriorityEnable_Object((1,3,6,1,4,1,3902,15,2,11,5,14,1,4),_DscpPriorityEnable_Type())
dscpPriorityEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:dscpPriorityEnable.setStatus(_A)
class _QueScheduleMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('wrr0',0),('sp',1),('wrr1-sp',2),('wrr2-sp',3),('session0',4),('session1',5)))
_QueScheduleMode_Type.__name__=_D
_QueScheduleMode_Object=MibTableColumn
queScheduleMode=_QueScheduleMode_Object((1,3,6,1,4,1,3902,15,2,11,5,14,1,5),_QueScheduleMode_Type())
queScheduleMode.setMaxAccess(_B)
if mibBuilder.loadTexts:queScheduleMode.setStatus(_A)
_RemaptagToPriority_Type=OctetString
_RemaptagToPriority_Object=MibTableColumn
remaptagToPriority=_RemaptagToPriority_Object((1,3,6,1,4,1,3902,15,2,11,5,14,1,6),_RemaptagToPriority_Type())
remaptagToPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:remaptagToPriority.setStatus(_A)
_Pvlan_ObjectIdentity=ObjectIdentity
pvlan=_Pvlan_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,6))
class _SessionMaxNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_SessionMaxNum_Type.__name__=_K
_SessionMaxNum_Object=MibScalar
sessionMaxNum=_SessionMaxNum_Object((1,3,6,1,4,1,3902,15,2,11,6,1),_SessionMaxNum_Type())
sessionMaxNum.setMaxAccess(_C)
if mibBuilder.loadTexts:sessionMaxNum.setStatus(_A)
_PvlanTable_Object=MibTable
pvlanTable=_PvlanTable_Object((1,3,6,1,4,1,3902,15,2,11,6,2))
if mibBuilder.loadTexts:pvlanTable.setStatus(_A)
_PvlanEntry_Object=MibTableRow
pvlanEntry=_PvlanEntry_Object((1,3,6,1,4,1,3902,15,2,11,6,2,1))
pvlanEntry.setIndexNames((0,_E,_n))
if mibBuilder.loadTexts:pvlanEntry.setStatus(_A)
_SessionId_Type=Unsigned32
_SessionId_Object=MibTableColumn
sessionId=_SessionId_Object((1,3,6,1,4,1,3902,15,2,11,6,2,1,1),_SessionId_Type())
sessionId.setMaxAccess(_F)
if mibBuilder.loadTexts:sessionId.setStatus(_A)
_ProAndIsoPortOrTrunk_Type=OctetString
_ProAndIsoPortOrTrunk_Object=MibTableColumn
proAndIsoPortOrTrunk=_ProAndIsoPortOrTrunk_Object((1,3,6,1,4,1,3902,15,2,11,6,2,1,2),_ProAndIsoPortOrTrunk_Type())
proAndIsoPortOrTrunk.setMaxAccess(_B)
if mibBuilder.loadTexts:proAndIsoPortOrTrunk.setStatus(_A)
_Lacp_ObjectIdentity=ObjectIdentity
lacp=_Lacp_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,7))
class _LacpAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_LacpAdminStatus_Type.__name__=_D
_LacpAdminStatus_Object=MibScalar
lacpAdminStatus=_LacpAdminStatus_Object((1,3,6,1,4,1,3902,15,2,11,7,1),_LacpAdminStatus_Type())
lacpAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpAdminStatus.setStatus(_A)
class _LacpPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_LacpPriority_Type.__name__=_K
_LacpPriority_Object=MibScalar
lacpPriority=_LacpPriority_Object((1,3,6,1,4,1,3902,15,2,11,7,2),_LacpPriority_Type())
lacpPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpPriority.setStatus(_A)
_TrunkNumber_Type=Unsigned32
_TrunkNumber_Object=MibScalar
trunkNumber=_TrunkNumber_Object((1,3,6,1,4,1,3902,15,2,11,7,3),_TrunkNumber_Type())
trunkNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:trunkNumber.setStatus(_A)
_TrunkTable_Object=MibTable
trunkTable=_TrunkTable_Object((1,3,6,1,4,1,3902,15,2,11,7,4))
if mibBuilder.loadTexts:trunkTable.setStatus(_A)
_TrunkEntry_Object=MibTableRow
trunkEntry=_TrunkEntry_Object((1,3,6,1,4,1,3902,15,2,11,7,4,1))
trunkEntry.setIndexNames((0,_E,_o))
if mibBuilder.loadTexts:trunkEntry.setStatus(_A)
class _TrunkId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_TrunkId_Type.__name__=_K
_TrunkId_Object=MibTableColumn
trunkId=_TrunkId_Object((1,3,6,1,4,1,3902,15,2,11,7,4,1,1),_TrunkId_Type())
trunkId.setMaxAccess(_F)
if mibBuilder.loadTexts:trunkId.setStatus(_A)
class _TrunkPvid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_TrunkPvid_Type.__name__=_D
_TrunkPvid_Object=MibTableColumn
trunkPvid=_TrunkPvid_Object((1,3,6,1,4,1,3902,15,2,11,7,4,1,2),_TrunkPvid_Type())
trunkPvid.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkPvid.setStatus(_A)
class _TrunkMulticast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_TrunkMulticast_Type.__name__=_D
_TrunkMulticast_Object=MibTableColumn
trunkMulticast=_TrunkMulticast_Object((1,3,6,1,4,1,3902,15,2,11,7,4,1,3),_TrunkMulticast_Type())
trunkMulticast.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkMulticast.setStatus(_A)
_TrunkPorts_Type=PortList
_TrunkPorts_Object=MibTableColumn
trunkPorts=_TrunkPorts_Object((1,3,6,1,4,1,3902,15,2,11,7,4,1,4),_TrunkPorts_Type())
trunkPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkPorts.setStatus(_A)
class _TrunkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dynamic',1),('static',2),('mixed',3)))
_TrunkMode_Type.__name__=_D
_TrunkMode_Object=MibTableColumn
trunkMode=_TrunkMode_Object((1,3,6,1,4,1,3902,15,2,11,7,4,1,5),_TrunkMode_Type())
trunkMode.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkMode.setStatus(_A)
_LacpPortTable_Object=MibTable
lacpPortTable=_LacpPortTable_Object((1,3,6,1,4,1,3902,15,2,11,7,5))
if mibBuilder.loadTexts:lacpPortTable.setStatus(_A)
_LacpPortEntry_Object=MibTableRow
lacpPortEntry=_LacpPortEntry_Object((1,3,6,1,4,1,3902,15,2,11,7,5,1))
lacpPortEntry.setIndexNames((0,_E,_p))
if mibBuilder.loadTexts:lacpPortEntry.setStatus(_A)
class _LacpPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_LacpPortId_Type.__name__=_D
_LacpPortId_Object=MibTableColumn
lacpPortId=_LacpPortId_Object((1,3,6,1,4,1,3902,15,2,11,7,5,1,1),_LacpPortId_Type())
lacpPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:lacpPortId.setStatus(_A)
class _LacpPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('passive',2)))
_LacpPortMode_Type.__name__=_D
_LacpPortMode_Object=MibTableColumn
lacpPortMode=_LacpPortMode_Object((1,3,6,1,4,1,3902,15,2,11,7,5,1,2),_LacpPortMode_Type())
lacpPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpPortMode.setStatus(_A)
class _LacpPortTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),('long',2)))
_LacpPortTimeout_Type.__name__=_D
_LacpPortTimeout_Object=MibTableColumn
lacpPortTimeout=_LacpPortTimeout_Object((1,3,6,1,4,1,3902,15,2,11,7,5,1,3),_LacpPortTimeout_Type())
lacpPortTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:lacpPortTimeout.setStatus(_A)
_Layer3_ObjectIdentity=ObjectIdentity
layer3=_Layer3_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,8))
_Layer3PortTable_Object=MibTable
layer3PortTable=_Layer3PortTable_Object((1,3,6,1,4,1,3902,15,2,11,8,1))
if mibBuilder.loadTexts:layer3PortTable.setStatus(_A)
_Layer3PortEntry_Object=MibTableRow
layer3PortEntry=_Layer3PortEntry_Object((1,3,6,1,4,1,3902,15,2,11,8,1,1))
layer3PortEntry.setIndexNames((0,_E,_q))
if mibBuilder.loadTexts:layer3PortEntry.setStatus(_A)
_Layer3PortId_Type=Unsigned32
_Layer3PortId_Object=MibTableColumn
layer3PortId=_Layer3PortId_Object((1,3,6,1,4,1,3902,15,2,11,8,1,1,1),_Layer3PortId_Type())
layer3PortId.setMaxAccess(_F)
if mibBuilder.loadTexts:layer3PortId.setStatus(_A)
_Layer3PortIpAddrAndMask_Type=OctetString
_Layer3PortIpAddrAndMask_Object=MibTableColumn
layer3PortIpAddrAndMask=_Layer3PortIpAddrAndMask_Object((1,3,6,1,4,1,3902,15,2,11,8,1,1,2),_Layer3PortIpAddrAndMask_Type())
layer3PortIpAddrAndMask.setMaxAccess(_B)
if mibBuilder.loadTexts:layer3PortIpAddrAndMask.setStatus(_A)
class _Layer3PortMacAddr_Type(MacAddress):subtypeSpec=MacAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_Layer3PortMacAddr_Type.__name__=_r
_Layer3PortMacAddr_Object=MibTableColumn
layer3PortMacAddr=_Layer3PortMacAddr_Object((1,3,6,1,4,1,3902,15,2,11,8,1,1,3),_Layer3PortMacAddr_Type())
layer3PortMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:layer3PortMacAddr.setStatus(_A)
class _Layer3PortVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Layer3PortVlanId_Type.__name__=_D
_Layer3PortVlanId_Object=MibTableColumn
layer3PortVlanId=_Layer3PortVlanId_Object((1,3,6,1,4,1,3902,15,2,11,8,1,1,4),_Layer3PortVlanId_Type())
layer3PortVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:layer3PortVlanId.setStatus(_A)
class _Layer3PortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Layer3PortAdminStatus_Type.__name__=_D
_Layer3PortAdminStatus_Object=MibTableColumn
layer3PortAdminStatus=_Layer3PortAdminStatus_Object((1,3,6,1,4,1,3902,15,2,11,8,1,1,5),_Layer3PortAdminStatus_Type())
layer3PortAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:layer3PortAdminStatus.setStatus(_A)
_LoopDetect_ObjectIdentity=ObjectIdentity
loopDetect=_LoopDetect_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,9))
class _LoopDetectBlockDelay_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1080))
_LoopDetectBlockDelay_Type.__name__=_K
_LoopDetectBlockDelay_Object=MibScalar
loopDetectBlockDelay=_LoopDetectBlockDelay_Object((1,3,6,1,4,1,3902,15,2,11,9,1),_LoopDetectBlockDelay_Type())
loopDetectBlockDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:loopDetectBlockDelay.setStatus(_A)
class _LoopDetectSendPktInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,60))
_LoopDetectSendPktInterval_Type.__name__=_K
_LoopDetectSendPktInterval_Object=MibScalar
loopDetectSendPktInterval=_LoopDetectSendPktInterval_Object((1,3,6,1,4,1,3902,15,2,11,9,2),_LoopDetectSendPktInterval_Type())
loopDetectSendPktInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:loopDetectSendPktInterval.setStatus(_A)
_LoopDetectPortTable_Object=MibTable
loopDetectPortTable=_LoopDetectPortTable_Object((1,3,6,1,4,1,3902,15,2,11,9,3))
if mibBuilder.loadTexts:loopDetectPortTable.setStatus(_A)
_LoopDetectPortEntry_Object=MibTableRow
loopDetectPortEntry=_LoopDetectPortEntry_Object((1,3,6,1,4,1,3902,15,2,11,9,3,1))
loopDetectPortEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:loopDetectPortEntry.setStatus(_A)
_LoopDetectPortId_Type=Integer32
_LoopDetectPortId_Object=MibTableColumn
loopDetectPortId=_LoopDetectPortId_Object((1,3,6,1,4,1,3902,15,2,11,9,3,1,1),_LoopDetectPortId_Type())
loopDetectPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:loopDetectPortId.setStatus(_A)
class _LoopDetectPortAdminStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,200))
_LoopDetectPortAdminStatus_Type.__name__=_I
_LoopDetectPortAdminStatus_Object=MibTableColumn
loopDetectPortAdminStatus=_LoopDetectPortAdminStatus_Object((1,3,6,1,4,1,3902,15,2,11,9,3,1,2),_LoopDetectPortAdminStatus_Type())
loopDetectPortAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:loopDetectPortAdminStatus.setStatus(_A)
class _LoopDetectPortProtectStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_LoopDetectPortProtectStatus_Type.__name__=_D
_LoopDetectPortProtectStatus_Object=MibTableColumn
loopDetectPortProtectStatus=_LoopDetectPortProtectStatus_Object((1,3,6,1,4,1,3902,15,2,11,9,3,1,3),_LoopDetectPortProtectStatus_Type())
loopDetectPortProtectStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:loopDetectPortProtectStatus.setStatus(_A)
class _LoopDetectPortLoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_LoopDetectPortLoopStatus_Type.__name__=_D
_LoopDetectPortLoopStatus_Object=MibTableColumn
loopDetectPortLoopStatus=_LoopDetectPortLoopStatus_Object((1,3,6,1,4,1,3902,15,2,11,9,3,1,4),_LoopDetectPortLoopStatus_Type())
loopDetectPortLoopStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:loopDetectPortLoopStatus.setStatus(_A)
class _LoopDetectPortBlockStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_LoopDetectPortBlockStatus_Type.__name__=_D
_LoopDetectPortBlockStatus_Object=MibTableColumn
loopDetectPortBlockStatus=_LoopDetectPortBlockStatus_Object((1,3,6,1,4,1,3902,15,2,11,9,3,1,5),_LoopDetectPortBlockStatus_Type())
loopDetectPortBlockStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:loopDetectPortBlockStatus.setStatus(_A)
class _LoopDetectPortInVlan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_LoopDetectPortInVlan_Type.__name__=_K
_LoopDetectPortInVlan_Object=MibTableColumn
loopDetectPortInVlan=_LoopDetectPortInVlan_Object((1,3,6,1,4,1,3902,15,2,11,9,3,1,6),_LoopDetectPortInVlan_Type())
loopDetectPortInVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:loopDetectPortInVlan.setStatus(_A)
_LoopDetectTrunkTable_Object=MibTable
loopDetectTrunkTable=_LoopDetectTrunkTable_Object((1,3,6,1,4,1,3902,15,2,11,9,4))
if mibBuilder.loadTexts:loopDetectTrunkTable.setStatus(_A)
_LoopDetectTrunkEntry_Object=MibTableRow
loopDetectTrunkEntry=_LoopDetectTrunkEntry_Object((1,3,6,1,4,1,3902,15,2,11,9,4,1))
loopDetectTrunkEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:loopDetectTrunkEntry.setStatus(_A)
_LoopDetectTrunkId_Type=Integer32
_LoopDetectTrunkId_Object=MibTableColumn
loopDetectTrunkId=_LoopDetectTrunkId_Object((1,3,6,1,4,1,3902,15,2,11,9,4,1,1),_LoopDetectTrunkId_Type())
loopDetectTrunkId.setMaxAccess(_C)
if mibBuilder.loadTexts:loopDetectTrunkId.setStatus(_A)
class _LoopDetectTrunkAdminStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,200))
_LoopDetectTrunkAdminStatus_Type.__name__=_I
_LoopDetectTrunkAdminStatus_Object=MibTableColumn
loopDetectTrunkAdminStatus=_LoopDetectTrunkAdminStatus_Object((1,3,6,1,4,1,3902,15,2,11,9,4,1,2),_LoopDetectTrunkAdminStatus_Type())
loopDetectTrunkAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:loopDetectTrunkAdminStatus.setStatus(_A)
class _LoopDetectTrunkProtectStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_LoopDetectTrunkProtectStatus_Type.__name__=_D
_LoopDetectTrunkProtectStatus_Object=MibTableColumn
loopDetectTrunkProtectStatus=_LoopDetectTrunkProtectStatus_Object((1,3,6,1,4,1,3902,15,2,11,9,4,1,3),_LoopDetectTrunkProtectStatus_Type())
loopDetectTrunkProtectStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:loopDetectTrunkProtectStatus.setStatus(_A)
class _LoopDetectTrunkLoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_LoopDetectTrunkLoopStatus_Type.__name__=_D
_LoopDetectTrunkLoopStatus_Object=MibTableColumn
loopDetectTrunkLoopStatus=_LoopDetectTrunkLoopStatus_Object((1,3,6,1,4,1,3902,15,2,11,9,4,1,4),_LoopDetectTrunkLoopStatus_Type())
loopDetectTrunkLoopStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:loopDetectTrunkLoopStatus.setStatus(_A)
class _LoopDetectTrunkBlockStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_LoopDetectTrunkBlockStatus_Type.__name__=_D
_LoopDetectTrunkBlockStatus_Object=MibTableColumn
loopDetectTrunkBlockStatus=_LoopDetectTrunkBlockStatus_Object((1,3,6,1,4,1,3902,15,2,11,9,4,1,5),_LoopDetectTrunkBlockStatus_Type())
loopDetectTrunkBlockStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:loopDetectTrunkBlockStatus.setStatus(_A)
class _LoopDetectTrunkInVlan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_LoopDetectTrunkInVlan_Type.__name__=_K
_LoopDetectTrunkInVlan_Object=MibTableColumn
loopDetectTrunkInVlan=_LoopDetectTrunkInVlan_Object((1,3,6,1,4,1,3902,15,2,11,9,4,1,6),_LoopDetectTrunkInVlan_Type())
loopDetectTrunkInVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:loopDetectTrunkInVlan.setStatus(_A)
_VlanTranslation_ObjectIdentity=ObjectIdentity
vlanTranslation=_VlanTranslation_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,10))
_VlanTranslationTable_Object=MibTable
vlanTranslationTable=_VlanTranslationTable_Object((1,3,6,1,4,1,3902,15,2,11,10,1))
if mibBuilder.loadTexts:vlanTranslationTable.setStatus(_A)
_VlanTranslationEntry_Object=MibTableRow
vlanTranslationEntry=_VlanTranslationEntry_Object((1,3,6,1,4,1,3902,15,2,11,10,1,1))
vlanTranslationEntry.setIndexNames((0,_E,_s))
if mibBuilder.loadTexts:vlanTranslationEntry.setStatus(_A)
_IngressPortId_Type=Integer32
_IngressPortId_Object=MibTableColumn
ingressPortId=_IngressPortId_Object((1,3,6,1,4,1,3902,15,2,11,10,1,1,1),_IngressPortId_Type())
ingressPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:ingressPortId.setStatus(_A)
class _VlanTranslationEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_VlanTranslationEnable_Type.__name__=_D
_VlanTranslationEnable_Object=MibTableColumn
vlanTranslationEnable=_VlanTranslationEnable_Object((1,3,6,1,4,1,3902,15,2,11,10,1,1,2),_VlanTranslationEnable_Type())
vlanTranslationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanTranslationEnable.setStatus(_A)
_VlanTranslationStatus_Type=OctetString
_VlanTranslationStatus_Object=MibTableColumn
vlanTranslationStatus=_VlanTranslationStatus_Object((1,3,6,1,4,1,3902,15,2,11,10,1,1,3),_VlanTranslationStatus_Type())
vlanTranslationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanTranslationStatus.setStatus(_A)
_Stp_ObjectIdentity=ObjectIdentity
stp=_Stp_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,11))
class _StpAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_StpAdminStatus_Type.__name__=_D
_StpAdminStatus_Object=MibScalar
stpAdminStatus=_StpAdminStatus_Object((1,3,6,1,4,1,3902,15,2,11,11,1),_StpAdminStatus_Type())
stpAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:stpAdminStatus.setStatus(_A)
_Vct_ObjectIdentity=ObjectIdentity
vct=_Vct_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,12))
_VctPortTable_Object=MibTable
vctPortTable=_VctPortTable_Object((1,3,6,1,4,1,3902,15,2,11,12,1))
if mibBuilder.loadTexts:vctPortTable.setStatus(_A)
_VctPortEntry_Object=MibTableRow
vctPortEntry=_VctPortEntry_Object((1,3,6,1,4,1,3902,15,2,11,12,1,1))
vctPortEntry.setIndexNames((0,_E,_t))
if mibBuilder.loadTexts:vctPortEntry.setStatus(_A)
class _VctPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_VctPortId_Type.__name__=_D
_VctPortId_Object=MibTableColumn
vctPortId=_VctPortId_Object((1,3,6,1,4,1,3902,15,2,11,12,1,1,1),_VctPortId_Type())
vctPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:vctPortId.setStatus(_A)
class _VctDo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_VctDo_Type.__name__=_D
_VctDo_Object=MibTableColumn
vctDo=_VctDo_Object((1,3,6,1,4,1,3902,15,2,11,12,1,1,2),_VctDo_Type())
vctDo.setMaxAccess(_B)
if mibBuilder.loadTexts:vctDo.setStatus(_A)
class _VctIsValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('yes2',2),('yes4',3)))
_VctIsValid_Type.__name__=_D
_VctIsValid_Object=MibTableColumn
vctIsValid=_VctIsValid_Object((1,3,6,1,4,1,3902,15,2,11,12,1,1,3),_VctIsValid_Type())
vctIsValid.setMaxAccess(_C)
if mibBuilder.loadTexts:vctIsValid.setStatus(_A)
class _VctPair1Result_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),(_S,2),(_Q,3),(_T,4)))
_VctPair1Result_Type.__name__=_D
_VctPair1Result_Object=MibTableColumn
vctPair1Result=_VctPair1Result_Object((1,3,6,1,4,1,3902,15,2,11,12,1,1,4),_VctPair1Result_Type())
vctPair1Result.setMaxAccess(_C)
if mibBuilder.loadTexts:vctPair1Result.setStatus(_A)
class _VctPair1Lenth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VctPair1Lenth_Type.__name__=_D
_VctPair1Lenth_Object=MibTableColumn
vctPair1Lenth=_VctPair1Lenth_Object((1,3,6,1,4,1,3902,15,2,11,12,1,1,5),_VctPair1Lenth_Type())
vctPair1Lenth.setMaxAccess(_C)
if mibBuilder.loadTexts:vctPair1Lenth.setStatus(_A)
class _VctPair2Result_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),(_S,2),(_Q,3),(_T,4)))
_VctPair2Result_Type.__name__=_D
_VctPair2Result_Object=MibTableColumn
vctPair2Result=_VctPair2Result_Object((1,3,6,1,4,1,3902,15,2,11,12,1,1,6),_VctPair2Result_Type())
vctPair2Result.setMaxAccess(_C)
if mibBuilder.loadTexts:vctPair2Result.setStatus(_A)
class _VctPair2Lenth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VctPair2Lenth_Type.__name__=_D
_VctPair2Lenth_Object=MibTableColumn
vctPair2Lenth=_VctPair2Lenth_Object((1,3,6,1,4,1,3902,15,2,11,12,1,1,7),_VctPair2Lenth_Type())
vctPair2Lenth.setMaxAccess(_C)
if mibBuilder.loadTexts:vctPair2Lenth.setStatus(_A)
class _VctPair3Result_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),(_S,2),(_Q,3),(_T,4)))
_VctPair3Result_Type.__name__=_D
_VctPair3Result_Object=MibTableColumn
vctPair3Result=_VctPair3Result_Object((1,3,6,1,4,1,3902,15,2,11,12,1,1,8),_VctPair3Result_Type())
vctPair3Result.setMaxAccess(_C)
if mibBuilder.loadTexts:vctPair3Result.setStatus(_A)
class _VctPair3Lenth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VctPair3Lenth_Type.__name__=_D
_VctPair3Lenth_Object=MibTableColumn
vctPair3Lenth=_VctPair3Lenth_Object((1,3,6,1,4,1,3902,15,2,11,12,1,1,9),_VctPair3Lenth_Type())
vctPair3Lenth.setMaxAccess(_C)
if mibBuilder.loadTexts:vctPair3Lenth.setStatus(_A)
class _VctPair4Result_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),(_S,2),(_Q,3),(_T,4)))
_VctPair4Result_Type.__name__=_D
_VctPair4Result_Object=MibTableColumn
vctPair4Result=_VctPair4Result_Object((1,3,6,1,4,1,3902,15,2,11,12,1,1,10),_VctPair4Result_Type())
vctPair4Result.setMaxAccess(_C)
if mibBuilder.loadTexts:vctPair4Result.setStatus(_A)
class _VctPair4Lenth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VctPair4Lenth_Type.__name__=_D
_VctPair4Lenth_Object=MibTableColumn
vctPair4Lenth=_VctPair4Lenth_Object((1,3,6,1,4,1,3902,15,2,11,12,1,1,11),_VctPair4Lenth_Type())
vctPair4Lenth.setMaxAccess(_C)
if mibBuilder.loadTexts:vctPair4Lenth.setStatus(_A)
_Syslog_ObjectIdentity=ObjectIdentity
syslog=_Syslog_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,13))
class _SyslogStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SyslogStatus_Type.__name__=_D
_SyslogStatus_Object=MibScalar
syslogStatus=_SyslogStatus_Object((1,3,6,1,4,1,3902,15,2,11,13,1),_SyslogStatus_Type())
syslogStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:syslogStatus.setStatus(_A)
class _SyslogLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SyslogLevel_Type.__name__=_D
_SyslogLevel_Object=MibScalar
syslogLevel=_SyslogLevel_Object((1,3,6,1,4,1,3902,15,2,11,13,2),_SyslogLevel_Type())
syslogLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:syslogLevel.setStatus(_A)
_EnabledModule_Type=PortList
_EnabledModule_Object=MibScalar
enabledModule=_EnabledModule_Object((1,3,6,1,4,1,3902,15,2,11,13,3),_EnabledModule_Type())
enabledModule.setMaxAccess(_B)
if mibBuilder.loadTexts:enabledModule.setStatus(_A)
class _ServerMaxNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_ServerMaxNum_Type.__name__=_D
_ServerMaxNum_Object=MibScalar
serverMaxNum=_ServerMaxNum_Object((1,3,6,1,4,1,3902,15,2,11,13,4),_ServerMaxNum_Type())
serverMaxNum.setMaxAccess(_C)
if mibBuilder.loadTexts:serverMaxNum.setStatus(_A)
_ServerTable_Object=MibTable
serverTable=_ServerTable_Object((1,3,6,1,4,1,3902,15,2,11,13,5))
if mibBuilder.loadTexts:serverTable.setStatus(_A)
_ServerEntry_Object=MibTableRow
serverEntry=_ServerEntry_Object((1,3,6,1,4,1,3902,15,2,11,13,5,1))
serverEntry.setIndexNames((0,_E,_u))
if mibBuilder.loadTexts:serverEntry.setStatus(_A)
_ServerId_Type=Unsigned32
_ServerId_Object=MibTableColumn
serverId=_ServerId_Object((1,3,6,1,4,1,3902,15,2,11,13,5,1,1),_ServerId_Type())
serverId.setMaxAccess(_F)
if mibBuilder.loadTexts:serverId.setStatus(_A)
_ServerIP_Type=OctetString
_ServerIP_Object=MibTableColumn
serverIP=_ServerIP_Object((1,3,6,1,4,1,3902,15,2,11,13,5,1,2),_ServerIP_Type())
serverIP.setMaxAccess(_B)
if mibBuilder.loadTexts:serverIP.setStatus(_A)
class _ServerName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ServerName_Type.__name__=_I
_ServerName_Object=MibTableColumn
serverName=_ServerName_Object((1,3,6,1,4,1,3902,15,2,11,13,5,1,3),_ServerName_Type())
serverName.setMaxAccess(_B)
if mibBuilder.loadTexts:serverName.setStatus(_A)
class _ServerAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ServerAdminStatus_Type.__name__=_D
_ServerAdminStatus_Object=MibTableColumn
serverAdminStatus=_ServerAdminStatus_Object((1,3,6,1,4,1,3902,15,2,11,13,5,1,4),_ServerAdminStatus_Type())
serverAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:serverAdminStatus.setStatus(_A)
_Ntp_ObjectIdentity=ObjectIdentity
ntp=_Ntp_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,14))
class _SynchronizeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SynchronizeStatus_Type.__name__=_D
_SynchronizeStatus_Object=MibScalar
synchronizeStatus=_SynchronizeStatus_Object((1,3,6,1,4,1,3902,15,2,11,14,1),_SynchronizeStatus_Type())
synchronizeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:synchronizeStatus.setStatus(_A)
class _ProtocolStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ProtocolStatus_Type.__name__=_D
_ProtocolStatus_Object=MibScalar
protocolStatus=_ProtocolStatus_Object((1,3,6,1,4,1,3902,15,2,11,14,2),_ProtocolStatus_Type())
protocolStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:protocolStatus.setStatus(_A)
_SrvIpAddrAndVersion_Type=OctetString
_SrvIpAddrAndVersion_Object=MibScalar
srvIpAddrAndVersion=_SrvIpAddrAndVersion_Object((1,3,6,1,4,1,3902,15,2,11,14,3),_SrvIpAddrAndVersion_Type())
srvIpAddrAndVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:srvIpAddrAndVersion.setStatus(_A)
_SourceIpAddr_Type=OctetString
_SourceIpAddr_Object=MibScalar
sourceIpAddr=_SourceIpAddr_Object((1,3,6,1,4,1,3902,15,2,11,14,4),_SourceIpAddr_Type())
sourceIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:sourceIpAddr.setStatus(_A)
_LoginUser_ObjectIdentity=ObjectIdentity
loginUser=_LoginUser_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,15))
_UserTable_Object=MibTable
userTable=_UserTable_Object((1,3,6,1,4,1,3902,15,2,11,15,1))
if mibBuilder.loadTexts:userTable.setStatus(_A)
_UserEntry_Object=MibTableRow
userEntry=_UserEntry_Object((1,3,6,1,4,1,3902,15,2,11,15,1,1))
userEntry.setIndexNames((0,_E,_v))
if mibBuilder.loadTexts:userEntry.setStatus(_A)
class _UserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_UserName_Type.__name__=_L
_UserName_Object=MibTableColumn
userName=_UserName_Object((1,3,6,1,4,1,3902,15,2,11,15,1,1,1),_UserName_Type())
userName.setMaxAccess(_C)
if mibBuilder.loadTexts:userName.setStatus(_A)
class _UserAttr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Y,1),('administrator',2),('guest',3)))
_UserAttr_Type.__name__=_D
_UserAttr_Object=MibTableColumn
userAttr=_UserAttr_Object((1,3,6,1,4,1,3902,15,2,11,15,1,1,2),_UserAttr_Type())
userAttr.setMaxAccess(_B)
if mibBuilder.loadTexts:userAttr.setStatus(_A)
class _LoginPass_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_LoginPass_Type.__name__=_I
_LoginPass_Object=MibTableColumn
loginPass=_LoginPass_Object((1,3,6,1,4,1,3902,15,2,11,15,1,1,3),_LoginPass_Type())
loginPass.setMaxAccess(_B)
if mibBuilder.loadTexts:loginPass.setStatus(_A)
class _AdminPass_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AdminPass_Type.__name__=_I
_AdminPass_Object=MibTableColumn
adminPass=_AdminPass_Object((1,3,6,1,4,1,3902,15,2,11,15,1,1,4),_AdminPass_Type())
adminPass.setMaxAccess(_B)
if mibBuilder.loadTexts:adminPass.setStatus(_A)
_SnmpConfig_ObjectIdentity=ObjectIdentity
snmpConfig=_SnmpConfig_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,16))
_CommunityTable_Object=MibTable
communityTable=_CommunityTable_Object((1,3,6,1,4,1,3902,15,2,11,16,1))
if mibBuilder.loadTexts:communityTable.setStatus(_A)
_CommunityEntry_Object=MibTableRow
communityEntry=_CommunityEntry_Object((1,3,6,1,4,1,3902,15,2,11,16,1,1))
communityEntry.setIndexNames((0,_E,_w))
if mibBuilder.loadTexts:communityEntry.setStatus(_A)
class _CommunityName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_CommunityName_Type.__name__=_L
_CommunityName_Object=MibTableColumn
communityName=_CommunityName_Object((1,3,6,1,4,1,3902,15,2,11,16,1,1,1),_CommunityName_Type())
communityName.setMaxAccess(_C)
if mibBuilder.loadTexts:communityName.setStatus(_A)
class _CommunityAttr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Y,1),('public',2),('private',3)))
_CommunityAttr_Type.__name__=_D
_CommunityAttr_Object=MibTableColumn
communityAttr=_CommunityAttr_Object((1,3,6,1,4,1,3902,15,2,11,16,1,1,2),_CommunityAttr_Type())
communityAttr.setMaxAccess(_B)
if mibBuilder.loadTexts:communityAttr.setStatus(_A)
class _ViewAttached_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_ViewAttached_Type.__name__=_I
_ViewAttached_Object=MibTableColumn
viewAttached=_ViewAttached_Object((1,3,6,1,4,1,3902,15,2,11,16,1,1,3),_ViewAttached_Type())
viewAttached.setMaxAccess(_B)
if mibBuilder.loadTexts:viewAttached.setStatus(_A)
_ViewTable_Object=MibTable
viewTable=_ViewTable_Object((1,3,6,1,4,1,3902,15,2,11,16,2))
if mibBuilder.loadTexts:viewTable.setStatus(_A)
_ViewEntry_Object=MibTableRow
viewEntry=_ViewEntry_Object((1,3,6,1,4,1,3902,15,2,11,16,2,1))
viewEntry.setIndexNames((0,_E,_x),(0,_E,_y))
if mibBuilder.loadTexts:viewEntry.setStatus(_A)
_ViewIndex_Type=Unsigned32
_ViewIndex_Object=MibTableColumn
viewIndex=_ViewIndex_Object((1,3,6,1,4,1,3902,15,2,11,16,2,1,1),_ViewIndex_Type())
viewIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:viewIndex.setStatus(_A)
class _ViewName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_ViewName_Type.__name__=_I
_ViewName_Object=MibTableColumn
viewName=_ViewName_Object((1,3,6,1,4,1,3902,15,2,11,16,2,1,2),_ViewName_Type())
viewName.setMaxAccess(_C)
if mibBuilder.loadTexts:viewName.setStatus(_A)
class _AttrAndOid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,150))
_AttrAndOid_Type.__name__=_I
_AttrAndOid_Object=MibTableColumn
attrAndOid=_AttrAndOid_Object((1,3,6,1,4,1,3902,15,2,11,16,2,1,3),_AttrAndOid_Type())
attrAndOid.setMaxAccess(_B)
if mibBuilder.loadTexts:attrAndOid.setStatus(_A)
_TrapHostTable_Object=MibTable
trapHostTable=_TrapHostTable_Object((1,3,6,1,4,1,3902,15,2,11,16,3))
if mibBuilder.loadTexts:trapHostTable.setStatus(_A)
_TrapHostEntry_Object=MibTableRow
trapHostEntry=_TrapHostEntry_Object((1,3,6,1,4,1,3902,15,2,11,16,3,1))
trapHostEntry.setIndexNames((0,_E,_z),(0,_E,_A0),(0,_E,_A1))
if mibBuilder.loadTexts:trapHostEntry.setStatus(_A)
_TraphostIP_Type=IpAddress
_TraphostIP_Object=MibTableColumn
traphostIP=_TraphostIP_Object((1,3,6,1,4,1,3902,15,2,11,16,3,1,1),_TraphostIP_Type())
traphostIP.setMaxAccess(_F)
if mibBuilder.loadTexts:traphostIP.setStatus(_A)
_TraphostType_Type=Unsigned32
_TraphostType_Object=MibTableColumn
traphostType=_TraphostType_Object((1,3,6,1,4,1,3902,15,2,11,16,3,1,2),_TraphostType_Type())
traphostType.setMaxAccess(_F)
if mibBuilder.loadTexts:traphostType.setStatus(_A)
class _CommuName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_CommuName_Type.__name__=_I
_CommuName_Object=MibTableColumn
commuName=_CommuName_Object((1,3,6,1,4,1,3902,15,2,11,16,3,1,3),_CommuName_Type())
commuName.setMaxAccess(_C)
if mibBuilder.loadTexts:commuName.setStatus(_A)
_TraphostVer_Type=Integer32
_TraphostVer_Object=MibTableColumn
traphostVer=_TraphostVer_Object((1,3,6,1,4,1,3902,15,2,11,16,3,1,4),_TraphostVer_Type())
traphostVer.setMaxAccess(_B)
if mibBuilder.loadTexts:traphostVer.setStatus(_A)
_TrapEnable_Type=PortList
_TrapEnable_Object=MibScalar
trapEnable=_TrapEnable_Object((1,3,6,1,4,1,3902,15,2,11,16,4),_TrapEnable_Type())
trapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:trapEnable.setStatus(_A)
_Acl_ObjectIdentity=ObjectIdentity
acl=_Acl_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,17))
_TimeAclTable_Object=MibTable
timeAclTable=_TimeAclTable_Object((1,3,6,1,4,1,3902,15,2,11,17,1))
if mibBuilder.loadTexts:timeAclTable.setStatus(_A)
_TimeAclEntry_Object=MibTableRow
timeAclEntry=_TimeAclEntry_Object((1,3,6,1,4,1,3902,15,2,11,17,1,1))
timeAclEntry.setIndexNames((0,_E,_A2))
if mibBuilder.loadTexts:timeAclEntry.setStatus(_A)
class _TimeRangeName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_TimeRangeName_Type.__name__=_I
_TimeRangeName_Object=MibTableColumn
timeRangeName=_TimeRangeName_Object((1,3,6,1,4,1,3902,15,2,11,17,1,1,1),_TimeRangeName_Type())
timeRangeName.setMaxAccess(_F)
if mibBuilder.loadTexts:timeRangeName.setStatus(_A)
class _TimeRange_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,150))
_TimeRange_Type.__name__=_I
_TimeRange_Object=MibTableColumn
timeRange=_TimeRange_Object((1,3,6,1,4,1,3902,15,2,11,17,1,1,2),_TimeRange_Type())
timeRange.setMaxAccess(_B)
if mibBuilder.loadTexts:timeRange.setStatus(_A)
_BasicAclTable_Object=MibTable
basicAclTable=_BasicAclTable_Object((1,3,6,1,4,1,3902,15,2,11,17,2))
if mibBuilder.loadTexts:basicAclTable.setStatus(_A)
_BasicAclEntry_Object=MibTableRow
basicAclEntry=_BasicAclEntry_Object((1,3,6,1,4,1,3902,15,2,11,17,2,1))
basicAclEntry.setIndexNames((0,_E,_A3),(0,_E,_A4))
if mibBuilder.loadTexts:basicAclEntry.setStatus(_A)
_BasicACLNo_Type=Unsigned32
_BasicACLNo_Object=MibTableColumn
basicACLNo=_BasicACLNo_Object((1,3,6,1,4,1,3902,15,2,11,17,2,1,1),_BasicACLNo_Type())
basicACLNo.setMaxAccess(_F)
if mibBuilder.loadTexts:basicACLNo.setStatus(_A)
_BasicRuleID_Type=Unsigned32
_BasicRuleID_Object=MibTableColumn
basicRuleID=_BasicRuleID_Object((1,3,6,1,4,1,3902,15,2,11,17,2,1,2),_BasicRuleID_Type())
basicRuleID.setMaxAccess(_F)
if mibBuilder.loadTexts:basicRuleID.setStatus(_A)
class _RuleBasicStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_RuleBasicStatus_Type.__name__=_D
_RuleBasicStatus_Object=MibTableColumn
ruleBasicStatus=_RuleBasicStatus_Object((1,3,6,1,4,1,3902,15,2,11,17,2,1,3),_RuleBasicStatus_Type())
ruleBasicStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ruleBasicStatus.setStatus(_A)
_RuleBasicACL_Type=OctetString
_RuleBasicACL_Object=MibTableColumn
ruleBasicACL=_RuleBasicACL_Object((1,3,6,1,4,1,3902,15,2,11,17,2,1,4),_RuleBasicACL_Type())
ruleBasicACL.setMaxAccess(_B)
if mibBuilder.loadTexts:ruleBasicACL.setStatus(_A)
_ExtendedAclTable_Object=MibTable
extendedAclTable=_ExtendedAclTable_Object((1,3,6,1,4,1,3902,15,2,11,17,3))
if mibBuilder.loadTexts:extendedAclTable.setStatus(_A)
_ExtendedAclEntry_Object=MibTableRow
extendedAclEntry=_ExtendedAclEntry_Object((1,3,6,1,4,1,3902,15,2,11,17,3,1))
extendedAclEntry.setIndexNames((0,_E,_A5),(0,_E,_A6))
if mibBuilder.loadTexts:extendedAclEntry.setStatus(_A)
_ExtendedACLNo_Type=Unsigned32
_ExtendedACLNo_Object=MibTableColumn
extendedACLNo=_ExtendedACLNo_Object((1,3,6,1,4,1,3902,15,2,11,17,3,1,1),_ExtendedACLNo_Type())
extendedACLNo.setMaxAccess(_F)
if mibBuilder.loadTexts:extendedACLNo.setStatus(_A)
_ExtendedRuleID_Type=Unsigned32
_ExtendedRuleID_Object=MibTableColumn
extendedRuleID=_ExtendedRuleID_Object((1,3,6,1,4,1,3902,15,2,11,17,3,1,2),_ExtendedRuleID_Type())
extendedRuleID.setMaxAccess(_F)
if mibBuilder.loadTexts:extendedRuleID.setStatus(_A)
class _RuleExtendedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_RuleExtendedStatus_Type.__name__=_D
_RuleExtendedStatus_Object=MibTableColumn
ruleExtendedStatus=_RuleExtendedStatus_Object((1,3,6,1,4,1,3902,15,2,11,17,3,1,3),_RuleExtendedStatus_Type())
ruleExtendedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ruleExtendedStatus.setStatus(_A)
_RuleExtendedProtocol_Type=OctetString
_RuleExtendedProtocol_Object=MibTableColumn
ruleExtendedProtocol=_RuleExtendedProtocol_Object((1,3,6,1,4,1,3902,15,2,11,17,3,1,4),_RuleExtendedProtocol_Type())
ruleExtendedProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:ruleExtendedProtocol.setStatus(_A)
_LinkAclTable_Object=MibTable
linkAclTable=_LinkAclTable_Object((1,3,6,1,4,1,3902,15,2,11,17,4))
if mibBuilder.loadTexts:linkAclTable.setStatus(_A)
_LinkAclEntry_Object=MibTableRow
linkAclEntry=_LinkAclEntry_Object((1,3,6,1,4,1,3902,15,2,11,17,4,1))
linkAclEntry.setIndexNames((0,_E,_A7),(0,_E,_A8))
if mibBuilder.loadTexts:linkAclEntry.setStatus(_A)
_LinkACLNo_Type=Unsigned32
_LinkACLNo_Object=MibTableColumn
linkACLNo=_LinkACLNo_Object((1,3,6,1,4,1,3902,15,2,11,17,4,1,1),_LinkACLNo_Type())
linkACLNo.setMaxAccess(_F)
if mibBuilder.loadTexts:linkACLNo.setStatus(_A)
_LinkRuleID_Type=Unsigned32
_LinkRuleID_Object=MibTableColumn
linkRuleID=_LinkRuleID_Object((1,3,6,1,4,1,3902,15,2,11,17,4,1,2),_LinkRuleID_Type())
linkRuleID.setMaxAccess(_F)
if mibBuilder.loadTexts:linkRuleID.setStatus(_A)
class _RuleLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_RuleLinkStatus_Type.__name__=_D
_RuleLinkStatus_Object=MibTableColumn
ruleLinkStatus=_RuleLinkStatus_Object((1,3,6,1,4,1,3902,15,2,11,17,4,1,3),_RuleLinkStatus_Type())
ruleLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ruleLinkStatus.setStatus(_A)
_RuleLinkProtocol_Type=OctetString
_RuleLinkProtocol_Object=MibTableColumn
ruleLinkProtocol=_RuleLinkProtocol_Object((1,3,6,1,4,1,3902,15,2,11,17,4,1,4),_RuleLinkProtocol_Type())
ruleLinkProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:ruleLinkProtocol.setStatus(_A)
_HybridAclTable_Object=MibTable
hybridAclTable=_HybridAclTable_Object((1,3,6,1,4,1,3902,15,2,11,17,5))
if mibBuilder.loadTexts:hybridAclTable.setStatus(_A)
_HybridAclEntry_Object=MibTableRow
hybridAclEntry=_HybridAclEntry_Object((1,3,6,1,4,1,3902,15,2,11,17,5,1))
hybridAclEntry.setIndexNames((0,_E,_A9),(0,_E,_AA))
if mibBuilder.loadTexts:hybridAclEntry.setStatus(_A)
_HybridACLNo_Type=Unsigned32
_HybridACLNo_Object=MibTableColumn
hybridACLNo=_HybridACLNo_Object((1,3,6,1,4,1,3902,15,2,11,17,5,1,1),_HybridACLNo_Type())
hybridACLNo.setMaxAccess(_F)
if mibBuilder.loadTexts:hybridACLNo.setStatus(_A)
_HybridRuleID_Type=Unsigned32
_HybridRuleID_Object=MibTableColumn
hybridRuleID=_HybridRuleID_Object((1,3,6,1,4,1,3902,15,2,11,17,5,1,2),_HybridRuleID_Type())
hybridRuleID.setMaxAccess(_F)
if mibBuilder.loadTexts:hybridRuleID.setStatus(_A)
class _RuleHybridStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_RuleHybridStatus_Type.__name__=_D
_RuleHybridStatus_Object=MibTableColumn
ruleHybridStatus=_RuleHybridStatus_Object((1,3,6,1,4,1,3902,15,2,11,17,5,1,3),_RuleHybridStatus_Type())
ruleHybridStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ruleHybridStatus.setStatus(_A)
_RuleHybridProtocol_Type=OctetString
_RuleHybridProtocol_Object=MibTableColumn
ruleHybridProtocol=_RuleHybridProtocol_Object((1,3,6,1,4,1,3902,15,2,11,17,5,1,4),_RuleHybridProtocol_Type())
ruleHybridProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:ruleHybridProtocol.setStatus(_A)
_GlobalAclTable_Object=MibTable
globalAclTable=_GlobalAclTable_Object((1,3,6,1,4,1,3902,15,2,11,17,6))
if mibBuilder.loadTexts:globalAclTable.setStatus(_A)
_GlobalAclEntry_Object=MibTableRow
globalAclEntry=_GlobalAclEntry_Object((1,3,6,1,4,1,3902,15,2,11,17,6,1))
globalAclEntry.setIndexNames((0,_E,_AB),(0,_E,_AC))
if mibBuilder.loadTexts:globalAclEntry.setStatus(_A)
_GlobalACLNo_Type=Unsigned32
_GlobalACLNo_Object=MibTableColumn
globalACLNo=_GlobalACLNo_Object((1,3,6,1,4,1,3902,15,2,11,17,6,1,1),_GlobalACLNo_Type())
globalACLNo.setMaxAccess(_F)
if mibBuilder.loadTexts:globalACLNo.setStatus(_A)
_GlobalRuleID_Type=Unsigned32
_GlobalRuleID_Object=MibTableColumn
globalRuleID=_GlobalRuleID_Object((1,3,6,1,4,1,3902,15,2,11,17,6,1,2),_GlobalRuleID_Type())
globalRuleID.setMaxAccess(_F)
if mibBuilder.loadTexts:globalRuleID.setStatus(_A)
class _RuleGlobalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_RuleGlobalStatus_Type.__name__=_D
_RuleGlobalStatus_Object=MibTableColumn
ruleGlobalStatus=_RuleGlobalStatus_Object((1,3,6,1,4,1,3902,15,2,11,17,6,1,3),_RuleGlobalStatus_Type())
ruleGlobalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ruleGlobalStatus.setStatus(_A)
_RuleGlobalProtocol_Type=OctetString
_RuleGlobalProtocol_Object=MibTableColumn
ruleGlobalProtocol=_RuleGlobalProtocol_Object((1,3,6,1,4,1,3902,15,2,11,17,6,1,4),_RuleGlobalProtocol_Type())
ruleGlobalProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:ruleGlobalProtocol.setStatus(_A)
_Fdb_ObjectIdentity=ObjectIdentity
fdb=_Fdb_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,18))
class _FdbAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(40,1260))
_FdbAgingTime_Type.__name__=_D
_FdbAgingTime_Object=MibScalar
fdbAgingTime=_FdbAgingTime_Object((1,3,6,1,4,1,3902,15,2,11,18,1),_FdbAgingTime_Type())
fdbAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbAgingTime.setStatus(_A)
_FdbFilterTable_Object=MibTable
fdbFilterTable=_FdbFilterTable_Object((1,3,6,1,4,1,3902,15,2,11,18,2))
if mibBuilder.loadTexts:fdbFilterTable.setStatus(_A)
_FdbFilterEntry_Object=MibTableRow
fdbFilterEntry=_FdbFilterEntry_Object((1,3,6,1,4,1,3902,15,2,11,18,2,1))
fdbFilterEntry.setIndexNames((0,_E,_U),(0,_E,_AD))
if mibBuilder.loadTexts:fdbFilterEntry.setStatus(_A)
_FdbID_Type=Unsigned32
_FdbID_Object=MibTableColumn
fdbID=_FdbID_Object((1,3,6,1,4,1,3902,15,2,11,18,2,1,1),_FdbID_Type())
fdbID.setMaxAccess(_F)
if mibBuilder.loadTexts:fdbID.setStatus(_A)
_FdbFilterAddress_Type=MacAddress
_FdbFilterAddress_Object=MibTableColumn
fdbFilterAddress=_FdbFilterAddress_Object((1,3,6,1,4,1,3902,15,2,11,18,2,1,2),_FdbFilterAddress_Type())
fdbFilterAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fdbFilterAddress.setStatus(_A)
class _FdbFilterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('both',1),(_Y,2)))
_FdbFilterType_Type.__name__=_D
_FdbFilterType_Object=MibTableColumn
fdbFilterType=_FdbFilterType_Object((1,3,6,1,4,1,3902,15,2,11,18,2,1,3),_FdbFilterType_Type())
fdbFilterType.setMaxAccess(_B)
if mibBuilder.loadTexts:fdbFilterType.setStatus(_A)
_FdbStaticPortTable_Object=MibTable
fdbStaticPortTable=_FdbStaticPortTable_Object((1,3,6,1,4,1,3902,15,2,11,18,3))
if mibBuilder.loadTexts:fdbStaticPortTable.setStatus(_A)
_FdbStaticPortEntry_Object=MibTableRow
fdbStaticPortEntry=_FdbStaticPortEntry_Object((1,3,6,1,4,1,3902,15,2,11,18,3,1))
fdbStaticPortEntry.setIndexNames((0,_E,_U),(0,_E,_Z))
if mibBuilder.loadTexts:fdbStaticPortEntry.setStatus(_A)
_FdbStaticAddress_Type=MacAddress
_FdbStaticAddress_Object=MibTableColumn
fdbStaticAddress=_FdbStaticAddress_Object((1,3,6,1,4,1,3902,15,2,11,18,3,1,2),_FdbStaticAddress_Type())
fdbStaticAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fdbStaticAddress.setStatus(_A)
_PortBindMac_Type=Unsigned32
_PortBindMac_Object=MibTableColumn
portBindMac=_PortBindMac_Object((1,3,6,1,4,1,3902,15,2,11,18,3,1,3),_PortBindMac_Type())
portBindMac.setMaxAccess(_B)
if mibBuilder.loadTexts:portBindMac.setStatus(_A)
_FdbStaticTrunkTable_Object=MibTable
fdbStaticTrunkTable=_FdbStaticTrunkTable_Object((1,3,6,1,4,1,3902,15,2,11,18,4))
if mibBuilder.loadTexts:fdbStaticTrunkTable.setStatus(_A)
_FdbStaticTrunkEntry_Object=MibTableRow
fdbStaticTrunkEntry=_FdbStaticTrunkEntry_Object((1,3,6,1,4,1,3902,15,2,11,18,4,1))
fdbStaticTrunkEntry.setIndexNames((0,_E,_U),(0,_E,_Z))
if mibBuilder.loadTexts:fdbStaticTrunkEntry.setStatus(_A)
_TrunkBindMac_Type=Unsigned32
_TrunkBindMac_Object=MibTableColumn
trunkBindMac=_TrunkBindMac_Object((1,3,6,1,4,1,3902,15,2,11,18,4,1,3),_TrunkBindMac_Type())
trunkBindMac.setMaxAccess(_B)
if mibBuilder.loadTexts:trunkBindMac.setStatus(_A)
_P8021xRelay_ObjectIdentity=ObjectIdentity
p8021xRelay=_P8021xRelay_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,19))
class _P8021xRelayAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_a,3)))
_P8021xRelayAdminStatus_Type.__name__=_D
_P8021xRelayAdminStatus_Object=MibScalar
p8021xRelayAdminStatus=_P8021xRelayAdminStatus_Object((1,3,6,1,4,1,3902,15,2,11,19,1),_P8021xRelayAdminStatus_Type())
p8021xRelayAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:p8021xRelayAdminStatus.setStatus(_A)
_IgmpSnooping_ObjectIdentity=ObjectIdentity
igmpSnooping=_IgmpSnooping_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,20))
_MultiGroupTable_Object=MibTable
multiGroupTable=_MultiGroupTable_Object((1,3,6,1,4,1,3902,15,2,11,20,1))
if mibBuilder.loadTexts:multiGroupTable.setStatus(_A)
_MultiGroupEntry_Object=MibTableRow
multiGroupEntry=_MultiGroupEntry_Object((1,3,6,1,4,1,3902,15,2,11,20,1,1))
multiGroupEntry.setIndexNames((0,_E,'number'))
if mibBuilder.loadTexts:multiGroupEntry.setStatus(_A)
_Number_Type=Unsigned32
_Number_Object=MibTableColumn
number=_Number_Object((1,3,6,1,4,1,3902,15,2,11,20,1,1,1),_Number_Type())
number.setMaxAccess(_F)
if mibBuilder.loadTexts:number.setStatus(_A)
_VlanID_Type=Unsigned32
_VlanID_Object=MibTableColumn
vlanID=_VlanID_Object((1,3,6,1,4,1,3902,15,2,11,20,1,1,2),_VlanID_Type())
vlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanID.setStatus(_A)
_MultiGroup_Type=IpAddress
_MultiGroup_Object=MibTableColumn
multiGroup=_MultiGroup_Object((1,3,6,1,4,1,3902,15,2,11,20,1,1,3),_MultiGroup_Type())
multiGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:multiGroup.setStatus(_A)
_PortList_Type=PortList
_PortList_Object=MibTableColumn
portList=_PortList_Object((1,3,6,1,4,1,3902,15,2,11,20,1,1,4),_PortList_Type())
portList.setMaxAccess(_C)
if mibBuilder.loadTexts:portList.setStatus(_A)
_TrunkList_Type=PortList
_TrunkList_Object=MibTableColumn
trunkList=_TrunkList_Object((1,3,6,1,4,1,3902,15,2,11,20,1,1,5),_TrunkList_Type())
trunkList.setMaxAccess(_C)
if mibBuilder.loadTexts:trunkList.setStatus(_A)
_Epon_ObjectIdentity=ObjectIdentity
epon=_Epon_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,21))
class _PonReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_PonReset_Type.__name__=_D
_PonReset_Object=MibScalar
ponReset=_PonReset_Object((1,3,6,1,4,1,3902,15,2,11,21,2),_PonReset_Type())
ponReset.setMaxAccess(_B)
if mibBuilder.loadTexts:ponReset.setStatus(_A)
_PortPonInfo_ObjectIdentity=ObjectIdentity
portPonInfo=_PortPonInfo_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,21,3))
class _PortPonAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_PortPonAdminStatus_Type.__name__=_D
_PortPonAdminStatus_Object=MibScalar
portPonAdminStatus=_PortPonAdminStatus_Object((1,3,6,1,4,1,3902,15,2,11,21,3,1),_PortPonAdminStatus_Type())
portPonAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:portPonAdminStatus.setStatus(_A)
_PortPonStpState_Type=OctetString
_PortPonStpState_Object=MibScalar
portPonStpState=_PortPonStpState_Object((1,3,6,1,4,1,3902,15,2,11,21,3,2),_PortPonStpState_Type())
portPonStpState.setMaxAccess(_C)
if mibBuilder.loadTexts:portPonStpState.setStatus(_A)
_PortPonFecTx_Type=Integer32
_PortPonFecTx_Object=MibScalar
portPonFecTx=_PortPonFecTx_Object((1,3,6,1,4,1,3902,15,2,11,21,3,3),_PortPonFecTx_Type())
portPonFecTx.setMaxAccess(_C)
if mibBuilder.loadTexts:portPonFecTx.setStatus(_A)
_PortPonFecRx_Type=Integer32
_PortPonFecRx_Object=MibScalar
portPonFecRx=_PortPonFecRx_Object((1,3,6,1,4,1,3902,15,2,11,21,3,4),_PortPonFecRx_Type())
portPonFecRx.setMaxAccess(_C)
if mibBuilder.loadTexts:portPonFecRx.setStatus(_A)
_PortPonType_Type=OctetString
_PortPonType_Object=MibScalar
portPonType=_PortPonType_Object((1,3,6,1,4,1,3902,15,2,11,21,3,5),_PortPonType_Type())
portPonType.setMaxAccess(_C)
if mibBuilder.loadTexts:portPonType.setStatus(_A)
class _PortPonOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_PortPonOperStatus_Type.__name__=_D
_PortPonOperStatus_Object=MibScalar
portPonOperStatus=_PortPonOperStatus_Object((1,3,6,1,4,1,3902,15,2,11,21,3,6),_PortPonOperStatus_Type())
portPonOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:portPonOperStatus.setStatus(_A)
_PortPonLlidPortsNum_Type=Integer32
_PortPonLlidPortsNum_Object=MibScalar
portPonLlidPortsNum=_PortPonLlidPortsNum_Object((1,3,6,1,4,1,3902,15,2,11,21,3,7),_PortPonLlidPortsNum_Type())
portPonLlidPortsNum.setMaxAccess(_C)
if mibBuilder.loadTexts:portPonLlidPortsNum.setStatus(_A)
_PonOamInfo_ObjectIdentity=ObjectIdentity
ponOamInfo=_PonOamInfo_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,21,4))
_LocalOamAdmin_Type=Integer32
_LocalOamAdmin_Object=MibScalar
localOamAdmin=_LocalOamAdmin_Object((1,3,6,1,4,1,3902,15,2,11,21,4,1),_LocalOamAdmin_Type())
localOamAdmin.setMaxAccess(_C)
if mibBuilder.loadTexts:localOamAdmin.setStatus(_A)
_LocalOamOper_Type=Integer32
_LocalOamOper_Object=MibScalar
localOamOper=_LocalOamOper_Object((1,3,6,1,4,1,3902,15,2,11,21,4,2),_LocalOamOper_Type())
localOamOper.setMaxAccess(_C)
if mibBuilder.loadTexts:localOamOper.setStatus(_A)
_LocalOamMode_Type=Integer32
_LocalOamMode_Object=MibScalar
localOamMode=_LocalOamMode_Object((1,3,6,1,4,1,3902,15,2,11,21,4,3),_LocalOamMode_Type())
localOamMode.setMaxAccess(_C)
if mibBuilder.loadTexts:localOamMode.setStatus(_A)
_LocalOamMaxPdu_Type=Integer32
_LocalOamMaxPdu_Object=MibScalar
localOamMaxPdu=_LocalOamMaxPdu_Object((1,3,6,1,4,1,3902,15,2,11,21,4,4),_LocalOamMaxPdu_Type())
localOamMaxPdu.setMaxAccess(_C)
if mibBuilder.loadTexts:localOamMaxPdu.setStatus(_A)
_LocalOamRevision_Type=Integer32
_LocalOamRevision_Object=MibScalar
localOamRevision=_LocalOamRevision_Object((1,3,6,1,4,1,3902,15,2,11,21,4,5),_LocalOamRevision_Type())
localOamRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:localOamRevision.setStatus(_A)
_LocalOamFuncSupport_Type=Integer32
_LocalOamFuncSupport_Object=MibScalar
localOamFuncSupport=_LocalOamFuncSupport_Object((1,3,6,1,4,1,3902,15,2,11,21,4,6),_LocalOamFuncSupport_Type())
localOamFuncSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:localOamFuncSupport.setStatus(_A)
_PeerOamStatus_Type=Integer32
_PeerOamStatus_Object=MibScalar
peerOamStatus=_PeerOamStatus_Object((1,3,6,1,4,1,3902,15,2,11,21,4,7),_PeerOamStatus_Type())
peerOamStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:peerOamStatus.setStatus(_A)
_PeerOamMacAddr_Type=MacAddress
_PeerOamMacAddr_Object=MibScalar
peerOamMacAddr=_PeerOamMacAddr_Object((1,3,6,1,4,1,3902,15,2,11,21,4,8),_PeerOamMacAddr_Type())
peerOamMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:peerOamMacAddr.setStatus(_A)
_PeerOamOUI_Type=OctetString
_PeerOamOUI_Object=MibScalar
peerOamOUI=_PeerOamOUI_Object((1,3,6,1,4,1,3902,15,2,11,21,4,9),_PeerOamOUI_Type())
peerOamOUI.setMaxAccess(_C)
if mibBuilder.loadTexts:peerOamOUI.setStatus(_A)
_PeerOamVendor_Type=Integer32
_PeerOamVendor_Object=MibScalar
peerOamVendor=_PeerOamVendor_Object((1,3,6,1,4,1,3902,15,2,11,21,4,10),_PeerOamVendor_Type())
peerOamVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:peerOamVendor.setStatus(_A)
_PeerOamMode_Type=Integer32
_PeerOamMode_Object=MibScalar
peerOamMode=_PeerOamMode_Object((1,3,6,1,4,1,3902,15,2,11,21,4,11),_PeerOamMode_Type())
peerOamMode.setMaxAccess(_C)
if mibBuilder.loadTexts:peerOamMode.setStatus(_A)
_PeerOamMaxPdu_Type=Integer32
_PeerOamMaxPdu_Object=MibScalar
peerOamMaxPdu=_PeerOamMaxPdu_Object((1,3,6,1,4,1,3902,15,2,11,21,4,12),_PeerOamMaxPdu_Type())
peerOamMaxPdu.setMaxAccess(_C)
if mibBuilder.loadTexts:peerOamMaxPdu.setStatus(_A)
_PeerOamRevision_Type=Integer32
_PeerOamRevision_Object=MibScalar
peerOamRevision=_PeerOamRevision_Object((1,3,6,1,4,1,3902,15,2,11,21,4,13),_PeerOamRevision_Type())
peerOamRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:peerOamRevision.setStatus(_A)
_PeerOamFuncSupport_Type=Integer32
_PeerOamFuncSupport_Object=MibScalar
peerOamFuncSupport=_PeerOamFuncSupport_Object((1,3,6,1,4,1,3902,15,2,11,21,4,14),_PeerOamFuncSupport_Type())
peerOamFuncSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:peerOamFuncSupport.setStatus(_A)
_PonLoopbackStatus_Type=OctetString
_PonLoopbackStatus_Object=MibScalar
ponLoopbackStatus=_PonLoopbackStatus_Object((1,3,6,1,4,1,3902,15,2,11,21,4,15),_PonLoopbackStatus_Type())
ponLoopbackStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ponLoopbackStatus.setStatus(_A)
_PonFirmwareInfo_ObjectIdentity=ObjectIdentity
ponFirmwareInfo=_PonFirmwareInfo_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,21,5))
class _EponStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_AE,1),('deregistered',2),('discovered',3),('lost',4),('unknown',5)))
_EponStatus_Type.__name__=_D
_EponStatus_Object=MibScalar
eponStatus=_EponStatus_Object((1,3,6,1,4,1,3902,15,2,11,21,5,1),_EponStatus_Type())
eponStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:eponStatus.setStatus(_A)
_SoftWareVersion_Type=OctetString
_SoftWareVersion_Object=MibScalar
softWareVersion=_SoftWareVersion_Object((1,3,6,1,4,1,3902,15,2,11,21,5,2),_SoftWareVersion_Type())
softWareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:softWareVersion.setStatus(_A)
_LoaderVersion_Type=OctetString
_LoaderVersion_Object=MibScalar
loaderVersion=_LoaderVersion_Object((1,3,6,1,4,1,3902,15,2,11,21,5,3),_LoaderVersion_Type())
loaderVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:loaderVersion.setStatus(_A)
_RegisterOltInfo_Type=OctetString
_RegisterOltInfo_Object=MibScalar
registerOltInfo=_RegisterOltInfo_Object((1,3,6,1,4,1,3902,15,2,11,21,5,4),_RegisterOltInfo_Type())
registerOltInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:registerOltInfo.setStatus(_A)
_RegisterOnuInfo_Type=OctetString
_RegisterOnuInfo_Object=MibScalar
registerOnuInfo=_RegisterOnuInfo_Object((1,3,6,1,4,1,3902,15,2,11,21,5,5),_RegisterOnuInfo_Type())
registerOnuInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:registerOnuInfo.setStatus(_A)
_PortNum_Type=Integer32
_PortNum_Object=MibScalar
portNum=_PortNum_Object((1,3,6,1,4,1,3902,15,2,11,21,5,6),_PortNum_Type())
portNum.setMaxAccess(_C)
if mibBuilder.loadTexts:portNum.setStatus(_A)
class _Registered_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_Registered_Type.__name__=_D
_Registered_Object=MibScalar
registered=_Registered_Object((1,3,6,1,4,1,3902,15,2,11,21,5,7),_Registered_Type())
registered.setMaxAccess(_C)
if mibBuilder.loadTexts:registered.setStatus(_A)
class _Authenticated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_Authenticated_Type.__name__=_D
_Authenticated_Object=MibScalar
authenticated=_Authenticated_Object((1,3,6,1,4,1,3902,15,2,11,21,5,8),_Authenticated_Type())
authenticated.setMaxAccess(_C)
if mibBuilder.loadTexts:authenticated.setStatus(_A)
_PonConfigMac_Type=MacAddress
_PonConfigMac_Object=MibScalar
ponConfigMac=_PonConfigMac_Object((1,3,6,1,4,1,3902,15,2,11,21,5,9),_PonConfigMac_Type())
ponConfigMac.setMaxAccess(_C)
if mibBuilder.loadTexts:ponConfigMac.setStatus(_A)
_ModeAndOamVer_Type=Integer32
_ModeAndOamVer_Object=MibScalar
modeAndOamVer=_ModeAndOamVer_Object((1,3,6,1,4,1,3902,15,2,11,21,5,10),_ModeAndOamVer_Type())
modeAndOamVer.setMaxAccess(_C)
if mibBuilder.loadTexts:modeAndOamVer.setStatus(_A)
_MpcpTimeout_Type=Integer32
_MpcpTimeout_Object=MibScalar
mpcpTimeout=_MpcpTimeout_Object((1,3,6,1,4,1,3902,15,2,11,21,5,11),_MpcpTimeout_Type())
mpcpTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:mpcpTimeout.setStatus(_A)
_CtrlVlan_Type=Integer32
_CtrlVlan_Object=MibScalar
ctrlVlan=_CtrlVlan_Object((1,3,6,1,4,1,3902,15,2,11,21,5,12),_CtrlVlan_Type())
ctrlVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:ctrlVlan.setStatus(_A)
_VendPonUni_Type=OctetString
_VendPonUni_Object=MibScalar
vendPonUni=_VendPonUni_Object((1,3,6,1,4,1,3902,15,2,11,21,5,13),_VendPonUni_Type())
vendPonUni.setMaxAccess(_C)
if mibBuilder.loadTexts:vendPonUni.setStatus(_A)
_CtcOui_Type=OctetString
_CtcOui_Object=MibScalar
ctcOui=_CtcOui_Object((1,3,6,1,4,1,3902,15,2,11,21,5,14),_CtcOui_Type())
ctcOui.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcOui.setStatus(_A)
_CtcVendor_Type=OctetString
_CtcVendor_Object=MibScalar
ctcVendor=_CtcVendor_Object((1,3,6,1,4,1,3902,15,2,11,21,5,15),_CtcVendor_Type())
ctcVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcVendor.setStatus(_A)
_CtcModel_Type=OctetString
_CtcModel_Object=MibScalar
ctcModel=_CtcModel_Object((1,3,6,1,4,1,3902,15,2,11,21,5,16),_CtcModel_Type())
ctcModel.setMaxAccess(_C)
if mibBuilder.loadTexts:ctcModel.setStatus(_A)
_EthernetOam_ObjectIdentity=ObjectIdentity
ethernetOam=_EthernetOam_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,22))
class _EthernetOamStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_EthernetOamStatus_Type.__name__=_D
_EthernetOamStatus_Object=MibScalar
ethernetOamStatus=_EthernetOamStatus_Object((1,3,6,1,4,1,3902,15,2,11,22,1),_EthernetOamStatus_Type())
ethernetOamStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamStatus.setStatus(_A)
_EthernetOamOuiDescr_Type=OctetString
_EthernetOamOuiDescr_Object=MibScalar
ethernetOamOuiDescr=_EthernetOamOuiDescr_Object((1,3,6,1,4,1,3902,15,2,11,22,2),_EthernetOamOuiDescr_Type())
ethernetOamOuiDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamOuiDescr.setStatus(_A)
_OrgSpecificTimeStamp_Type=Integer32
_OrgSpecificTimeStamp_Object=MibScalar
orgSpecificTimeStamp=_OrgSpecificTimeStamp_Object((1,3,6,1,4,1,3902,15,2,11,22,3),_OrgSpecificTimeStamp_Type())
orgSpecificTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:orgSpecificTimeStamp.setStatus(_A)
_RemoteLoopbackTimeout_Type=Integer32
_RemoteLoopbackTimeout_Object=MibScalar
remoteLoopbackTimeout=_RemoteLoopbackTimeout_Object((1,3,6,1,4,1,3902,15,2,11,22,4),_RemoteLoopbackTimeout_Type())
remoteLoopbackTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:remoteLoopbackTimeout.setStatus(_A)
_EthernetOamIfConfigTable_Object=MibTable
ethernetOamIfConfigTable=_EthernetOamIfConfigTable_Object((1,3,6,1,4,1,3902,15,2,11,22,5))
if mibBuilder.loadTexts:ethernetOamIfConfigTable.setStatus(_A)
_EthernetOamIfConfigEntry_Object=MibTableRow
ethernetOamIfConfigEntry=_EthernetOamIfConfigEntry_Object((1,3,6,1,4,1,3902,15,2,11,22,5,1))
ethernetOamIfConfigEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:ethernetOamIfConfigEntry.setStatus(_A)
class _EthernetOamIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_EthernetOamIfStatus_Type.__name__=_D
_EthernetOamIfStatus_Object=MibTableColumn
ethernetOamIfStatus=_EthernetOamIfStatus_Object((1,3,6,1,4,1,3902,15,2,11,22,5,1,2),_EthernetOamIfStatus_Type())
ethernetOamIfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetOamIfStatus.setStatus(_A)
class _RemoteLoopbackIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_RemoteLoopbackIfStatus_Type.__name__=_D
_RemoteLoopbackIfStatus_Object=MibTableColumn
remoteLoopbackIfStatus=_RemoteLoopbackIfStatus_Object((1,3,6,1,4,1,3902,15,2,11,22,5,1,3),_RemoteLoopbackIfStatus_Type())
remoteLoopbackIfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:remoteLoopbackIfStatus.setStatus(_A)
_IfPeriodTimeoutMode_Type=OctetString
_IfPeriodTimeoutMode_Object=MibTableColumn
ifPeriodTimeoutMode=_IfPeriodTimeoutMode_Object((1,3,6,1,4,1,3902,15,2,11,22,5,1,4),_IfPeriodTimeoutMode_Type())
ifPeriodTimeoutMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ifPeriodTimeoutMode.setStatus(_A)
class _IfLinkMonitorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IfLinkMonitorStatus_Type.__name__=_D
_IfLinkMonitorStatus_Object=MibTableColumn
ifLinkMonitorStatus=_IfLinkMonitorStatus_Object((1,3,6,1,4,1,3902,15,2,11,22,5,1,5),_IfLinkMonitorStatus_Type())
ifLinkMonitorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ifLinkMonitorStatus.setStatus(_A)
_IfLinkSymbolPeriodThresholdWindow_Type=OctetString
_IfLinkSymbolPeriodThresholdWindow_Object=MibTableColumn
ifLinkSymbolPeriodThresholdWindow=_IfLinkSymbolPeriodThresholdWindow_Object((1,3,6,1,4,1,3902,15,2,11,22,5,1,6),_IfLinkSymbolPeriodThresholdWindow_Type())
ifLinkSymbolPeriodThresholdWindow.setMaxAccess(_B)
if mibBuilder.loadTexts:ifLinkSymbolPeriodThresholdWindow.setStatus(_A)
_IfLinkFrameThresholdWindow_Type=OctetString
_IfLinkFrameThresholdWindow_Object=MibTableColumn
ifLinkFrameThresholdWindow=_IfLinkFrameThresholdWindow_Object((1,3,6,1,4,1,3902,15,2,11,22,5,1,7),_IfLinkFrameThresholdWindow_Type())
ifLinkFrameThresholdWindow.setMaxAccess(_B)
if mibBuilder.loadTexts:ifLinkFrameThresholdWindow.setStatus(_A)
_IfLinkFramePeriodThresholdWindow_Type=OctetString
_IfLinkFramePeriodThresholdWindow_Object=MibTableColumn
ifLinkFramePeriodThresholdWindow=_IfLinkFramePeriodThresholdWindow_Object((1,3,6,1,4,1,3902,15,2,11,22,5,1,8),_IfLinkFramePeriodThresholdWindow_Type())
ifLinkFramePeriodThresholdWindow.setMaxAccess(_B)
if mibBuilder.loadTexts:ifLinkFramePeriodThresholdWindow.setStatus(_A)
_IfLinkFrameSecondsThresholdWindow_Type=OctetString
_IfLinkFrameSecondsThresholdWindow_Object=MibTableColumn
ifLinkFrameSecondsThresholdWindow=_IfLinkFrameSecondsThresholdWindow_Object((1,3,6,1,4,1,3902,15,2,11,22,5,1,9),_IfLinkFrameSecondsThresholdWindow_Type())
ifLinkFrameSecondsThresholdWindow.setMaxAccess(_B)
if mibBuilder.loadTexts:ifLinkFrameSecondsThresholdWindow.setStatus(_A)
_EthernetOamShowTable_Object=MibTable
ethernetOamShowTable=_EthernetOamShowTable_Object((1,3,6,1,4,1,3902,15,2,11,22,6))
if mibBuilder.loadTexts:ethernetOamShowTable.setStatus(_A)
_EthernetOamShowEntry_Object=MibTableRow
ethernetOamShowEntry=_EthernetOamShowEntry_Object((1,3,6,1,4,1,3902,15,2,11,22,6,1))
ethernetOamShowEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:ethernetOamShowEntry.setStatus(_A)
_EthernetOamShowDiscovery_Type=OctetString
_EthernetOamShowDiscovery_Object=MibTableColumn
ethernetOamShowDiscovery=_EthernetOamShowDiscovery_Object((1,3,6,1,4,1,3902,15,2,11,22,6,1,2),_EthernetOamShowDiscovery_Type())
ethernetOamShowDiscovery.setMaxAccess(_C)
if mibBuilder.loadTexts:ethernetOamShowDiscovery.setStatus(_A)
_EthernetOamShowLinkMonitor_Type=OctetString
_EthernetOamShowLinkMonitor_Object=MibTableColumn
ethernetOamShowLinkMonitor=_EthernetOamShowLinkMonitor_Object((1,3,6,1,4,1,3902,15,2,11,22,6,1,3),_EthernetOamShowLinkMonitor_Type())
ethernetOamShowLinkMonitor.setMaxAccess(_C)
if mibBuilder.loadTexts:ethernetOamShowLinkMonitor.setStatus(_A)
_EthernetOamShowStatistics_Type=OctetString
_EthernetOamShowStatistics_Object=MibTableColumn
ethernetOamShowStatistics=_EthernetOamShowStatistics_Object((1,3,6,1,4,1,3902,15,2,11,22,6,1,4),_EthernetOamShowStatistics_Type())
ethernetOamShowStatistics.setMaxAccess(_C)
if mibBuilder.loadTexts:ethernetOamShowStatistics.setStatus(_A)
_RemoteMAC_Type=MacAddress
_RemoteMAC_Object=MibScalar
remoteMAC=_RemoteMAC_Object((1,3,6,1,4,1,3902,15,2,11,22,15),_RemoteMAC_Type())
remoteMAC.setMaxAccess(_F)
if mibBuilder.loadTexts:remoteMAC.setStatus(_A)
_OpticalInformation_ObjectIdentity=ObjectIdentity
opticalInformation=_OpticalInformation_ObjectIdentity((1,3,6,1,4,1,3902,15,2,11,23))
_OpticalInfoTable_Object=MibTable
opticalInfoTable=_OpticalInfoTable_Object((1,3,6,1,4,1,3902,15,2,11,23,1))
if mibBuilder.loadTexts:opticalInfoTable.setStatus(_A)
_OpticalInfoEntry_Object=MibTableRow
opticalInfoEntry=_OpticalInfoEntry_Object((1,3,6,1,4,1,3902,15,2,11,23,1,1))
opticalInfoEntry.setIndexNames((0,_E,_AF))
if mibBuilder.loadTexts:opticalInfoEntry.setStatus(_A)
_OpticalInfoPortId_Type=Unsigned32
_OpticalInfoPortId_Object=MibTableColumn
opticalInfoPortId=_OpticalInfoPortId_Object((1,3,6,1,4,1,3902,15,2,11,23,1,1,1),_OpticalInfoPortId_Type())
opticalInfoPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:opticalInfoPortId.setStatus(_A)
class _OpticalInfoIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OpticalInfoIfName_Type.__name__=_L
_OpticalInfoIfName_Object=MibTableColumn
opticalInfoIfName=_OpticalInfoIfName_Object((1,3,6,1,4,1,3902,15,2,11,23,1,1,2),_OpticalInfoIfName_Type())
opticalInfoIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:opticalInfoIfName.setStatus(_A)
class _OpticalInfoOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('online',1),('offline',2)))
_OpticalInfoOnline_Type.__name__=_D
_OpticalInfoOnline_Object=MibTableColumn
opticalInfoOnline=_OpticalInfoOnline_Object((1,3,6,1,4,1,3902,15,2,11,23,1,1,3),_OpticalInfoOnline_Type())
opticalInfoOnline.setMaxAccess(_C)
if mibBuilder.loadTexts:opticalInfoOnline.setStatus(_A)
_OpticalInfoSWaveLenth_Type=Integer32
_OpticalInfoSWaveLenth_Object=MibTableColumn
opticalInfoSWaveLenth=_OpticalInfoSWaveLenth_Object((1,3,6,1,4,1,3902,15,2,11,23,1,1,11),_OpticalInfoSWaveLenth_Type())
opticalInfoSWaveLenth.setMaxAccess(_C)
if mibBuilder.loadTexts:opticalInfoSWaveLenth.setStatus(_A)
class _OpticalInfoPowerSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('supported',1),('unsupported',2)))
_OpticalInfoPowerSupport_Type.__name__=_D
_OpticalInfoPowerSupport_Object=MibTableColumn
opticalInfoPowerSupport=_OpticalInfoPowerSupport_Object((1,3,6,1,4,1,3902,15,2,11,23,1,1,12),_OpticalInfoPowerSupport_Type())
opticalInfoPowerSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:opticalInfoPowerSupport.setStatus(_A)
class _OpticalInfoSRxPower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OpticalInfoSRxPower_Type.__name__=_L
_OpticalInfoSRxPower_Object=MibTableColumn
opticalInfoSRxPower=_OpticalInfoSRxPower_Object((1,3,6,1,4,1,3902,15,2,11,23,1,1,13),_OpticalInfoSRxPower_Type())
opticalInfoSRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:opticalInfoSRxPower.setStatus(_A)
class _OpticalInfoSRxPowerValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_a,2)))
_OpticalInfoSRxPowerValid_Type.__name__=_D
_OpticalInfoSRxPowerValid_Object=MibTableColumn
opticalInfoSRxPowerValid=_OpticalInfoSRxPowerValid_Object((1,3,6,1,4,1,3902,15,2,11,23,1,1,14),_OpticalInfoSRxPowerValid_Type())
opticalInfoSRxPowerValid.setMaxAccess(_C)
if mibBuilder.loadTexts:opticalInfoSRxPowerValid.setStatus(_A)
class _OpticalInfoSTxPower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OpticalInfoSTxPower_Type.__name__=_L
_OpticalInfoSTxPower_Object=MibTableColumn
opticalInfoSTxPower=_OpticalInfoSTxPower_Object((1,3,6,1,4,1,3902,15,2,11,23,1,1,15),_OpticalInfoSTxPower_Type())
opticalInfoSTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:opticalInfoSTxPower.setStatus(_A)
class _OpticalInfoSTxPowerValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_a,2)))
_OpticalInfoSTxPowerValid_Type.__name__=_D
_OpticalInfoSTxPowerValid_Object=MibTableColumn
opticalInfoSTxPowerValid=_OpticalInfoSTxPowerValid_Object((1,3,6,1,4,1,3902,15,2,11,23,1,1,16),_OpticalInfoSTxPowerValid_Type())
opticalInfoSTxPowerValid.setMaxAccess(_C)
if mibBuilder.loadTexts:opticalInfoSTxPowerValid.setStatus(_A)
class _OpticalInfoSTxPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('normal',0),('warning',1),('alarm',2),(_b,3)))
_OpticalInfoSTxPowerStatus_Type.__name__=_D
_OpticalInfoSTxPowerStatus_Object=MibTableColumn
opticalInfoSTxPowerStatus=_OpticalInfoSTxPowerStatus_Object((1,3,6,1,4,1,3902,15,2,11,23,1,1,17),_OpticalInfoSTxPowerStatus_Type())
opticalInfoSTxPowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:opticalInfoSTxPowerStatus.setStatus(_A)
class _OpticalInfoSRxPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('normal',0),('warning',1),('alarm',2),(_b,3)))
_OpticalInfoSRxPowerStatus_Type.__name__=_D
_OpticalInfoSRxPowerStatus_Object=MibTableColumn
opticalInfoSRxPowerStatus=_OpticalInfoSRxPowerStatus_Object((1,3,6,1,4,1,3902,15,2,11,23,1,1,18),_OpticalInfoSRxPowerStatus_Type())
opticalInfoSRxPowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:opticalInfoSRxPowerStatus.setStatus(_A)
class _OpticalInfoVName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OpticalInfoVName_Type.__name__=_L
_OpticalInfoVName_Object=MibTableColumn
opticalInfoVName=_OpticalInfoVName_Object((1,3,6,1,4,1,3902,15,2,11,23,1,1,23),_OpticalInfoVName_Type())
opticalInfoVName.setMaxAccess(_C)
if mibBuilder.loadTexts:opticalInfoVName.setStatus(_A)
class _OpticalInfoType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OpticalInfoType_Type.__name__=_L
_OpticalInfoType_Object=MibTableColumn
opticalInfoType=_OpticalInfoType_Object((1,3,6,1,4,1,3902,15,2,11,23,1,1,24),_OpticalInfoType_Type())
opticalInfoType.setMaxAccess(_C)
if mibBuilder.loadTexts:opticalInfoType.setStatus(_A)
class _OpticalInfoVSn_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OpticalInfoVSn_Type.__name__=_L
_OpticalInfoVSn_Object=MibTableColumn
opticalInfoVSn=_OpticalInfoVSn_Object((1,3,6,1,4,1,3902,15,2,11,23,1,1,26),_OpticalInfoVSn_Type())
opticalInfoVSn.setMaxAccess(_C)
if mibBuilder.loadTexts:opticalInfoVSn.setStatus(_A)
_OpticalInfoDistanse_Type=Integer32
_OpticalInfoDistanse_Object=MibTableColumn
opticalInfoDistanse=_OpticalInfoDistanse_Object((1,3,6,1,4,1,3902,15,2,11,23,1,1,27),_OpticalInfoDistanse_Type())
opticalInfoDistanse.setMaxAccess(_C)
if mibBuilder.loadTexts:opticalInfoDistanse.setStatus(_A)
class _OpticalInfoMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_b,0),('single',1),('multi',2),('copper',3)))
_OpticalInfoMode_Type.__name__=_D
_OpticalInfoMode_Object=MibTableColumn
opticalInfoMode=_OpticalInfoMode_Object((1,3,6,1,4,1,3902,15,2,11,23,1,1,28),_OpticalInfoMode_Type())
opticalInfoMode.setMaxAccess(_C)
if mibBuilder.loadTexts:opticalInfoMode.setStatus(_A)
dynamicMacExceedTrap=NotificationType((1,3,6,1,4,1,3902,15,2,11,2,5))
dynamicMacExceedTrap.setObjects(*((_E,_J),(_E,_AG)))
if mibBuilder.loadTexts:dynamicMacExceedTrap.setStatus(_A)
loopDetectPortTrap=NotificationType((1,3,6,1,4,1,3902,15,2,11,9,5))
loopDetectPortTrap.setObjects(*((_E,_W),(_E,_AH),(_E,_AI)))
if mibBuilder.loadTexts:loopDetectPortTrap.setStatus(_A)
loopDetectTrunkTrap=NotificationType((1,3,6,1,4,1,3902,15,2,11,9,6))
loopDetectTrunkTrap.setObjects(*((_E,_X),(_E,_AJ),(_E,_AK),(_E,_AL)))
if mibBuilder.loadTexts:loopDetectTrunkTrap.setStatus(_A)
linkMonitorSymbolPeriodTrap=NotificationType((1,3,6,1,4,1,3902,15,2,11,22,7))
linkMonitorSymbolPeriodTrap.setObjects(*((_E,_J),(_E,_O),(_E,_P)))
if mibBuilder.loadTexts:linkMonitorSymbolPeriodTrap.setStatus(_A)
linkMonitorFrameTrap=NotificationType((1,3,6,1,4,1,3902,15,2,11,22,8))
linkMonitorFrameTrap.setObjects(*((_E,_J),(_E,_O),(_E,_P)))
if mibBuilder.loadTexts:linkMonitorFrameTrap.setStatus(_A)
linkMonitorFramePeriodTrap=NotificationType((1,3,6,1,4,1,3902,15,2,11,22,9))
linkMonitorFramePeriodTrap.setObjects(*((_E,_J),(_E,_O),(_E,_P)))
if mibBuilder.loadTexts:linkMonitorFramePeriodTrap.setStatus(_A)
linkMonitorFrameSecondsTrap=NotificationType((1,3,6,1,4,1,3902,15,2,11,22,10))
linkMonitorFrameSecondsTrap.setObjects(*((_E,_J),(_E,_O),(_E,_P)))
if mibBuilder.loadTexts:linkMonitorFrameSecondsTrap.setStatus(_A)
remoteLinkFailTrap=NotificationType((1,3,6,1,4,1,3902,15,2,11,22,11))
remoteLinkFailTrap.setObjects(*((_E,_J),(_E,_O),(_E,_P)))
if mibBuilder.loadTexts:remoteLinkFailTrap.setStatus(_A)
remoteLinkOKTrap=NotificationType((1,3,6,1,4,1,3902,15,2,11,22,12))
remoteLinkOKTrap.setObjects(*((_E,_J),(_E,_O),(_E,_P)))
if mibBuilder.loadTexts:remoteLinkOKTrap.setStatus(_A)
dyingGaspTrap=NotificationType((1,3,6,1,4,1,3902,15,2,11,22,13))
dyingGaspTrap.setObjects(*((_E,_J),(_E,_O),(_E,_P)))
if mibBuilder.loadTexts:dyingGaspTrap.setStatus(_A)
remoteDiscoveryFailTrap=NotificationType((1,3,6,1,4,1,3902,15,2,11,22,14))
remoteDiscoveryFailTrap.setObjects(*((_E,_J),(_E,_O),(_E,_P)))
if mibBuilder.loadTexts:remoteDiscoveryFailTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'PortList':PortList,_r:MacAddress,_L:DisplayString,'zte':zte,'ethernetSwitch':ethernetSwitch,'layer2Switch':layer2Switch,'series2952Switch':series2952Switch,'switchSystem':switchSystem,'cpuLoad5s':cpuLoad5s,'cpuLoad30s':cpuLoad30s,'cpuLoad2m':cpuLoad2m,'maxCpuLoad':maxCpuLoad,'memUtilityRatio':memUtilityRatio,'switchType':switchType,_O:switchMac,'reboot':reboot,'saveConfig':saveConfig,'sysDateTime':sysDateTime,'port':port,'portNumber':portNumber,'portTable':portTable,'portEntry':portEntry,_J:portId,'portName':portName,'portDescr':portDescr,'portAdminStatus':portAdminStatus,'portOperStatus':portOperStatus,'portAdminWorkMode':portAdminWorkMode,'portOperDuplex':portOperDuplex,'portOperSpeed':portOperSpeed,'portPvid':portPvid,'portFlowControl':portFlowControl,'portVlanMode':portVlanMode,'portSecurity':portSecurity,'portPriority':portPriority,'portMulticast':portMulticast,'portMediaType':portMediaType,'isPortInTrunk':isPortInTrunk,'portLoopdetectStatus':portLoopdetectStatus,_AG:dynamicMacMaxCount,'dynamicMacExceedTrap':dynamicMacExceedTrap,'vlan':vlan,'maxVlanId':maxVlanId,'maxSupportedVlans':maxSupportedVlans,'vlanTable':vlanTable,'vlanEntry':vlanEntry,_e:vlanId,'vlanUntaggedPorts':vlanUntaggedPorts,'vlanTaggedPorts':vlanTaggedPorts,'vlanName':vlanName,'vlanAdminStatus':vlanAdminStatus,'vlanUntaggedTrunks':vlanUntaggedTrunks,'vlanTaggedTrunks':vlanTaggedTrunks,'vlanAssistantTable':vlanAssistantTable,'vlanAssistantEntry':vlanAssistantEntry,_f:assVlanId,'mirror':mirror,'sourcePortsIngress':sourcePortsIngress,'sourcePortsEgress':sourcePortsEgress,'desPortIngress':desPortIngress,'desPortEgress':desPortEgress,'qos':qos,'queueScheduleWeight':queueScheduleWeight,'queueScheduleMode0':queueScheduleMode0,'queueScheduleMode1':queueScheduleMode1,'queueScheduleMode2':queueScheduleMode2,'queueScheduleMode3':queueScheduleMode3,'qosPrimapUsrToTraffic':qosPrimapUsrToTraffic,'qosPolicerTable':qosPolicerTable,'qosPolicerEntry':qosPolicerEntry,_g:policerID,'qosPolicerPara':qosPolicerPara,'qosExceededOper':qosExceededOper,'qosPolicerBurst':qosPolicerBurst,'ipPriToTrafficTable':ipPriToTrafficTable,'ipPriToTrafficEntry':ipPriToTrafficEntry,_V:ipPriority,'tcFePort':tcFePort,'tcGePort':tcGePort,'fePortIngBandTable':fePortIngBandTable,'fePortIngBandEntry':fePortIngBandEntry,_h:fePortID,_i:sessionNo,'sessionStatus':sessionStatus,'feIngressRate':feIngressRate,'feIngressPkType':feIngressPkType,'quePriorityStatus':quePriorityStatus,'mgmtNoRatelimitStatus':mgmtNoRatelimitStatus,'gePortIngBandTable':gePortIngBandTable,'gePortIngBandEntry':gePortIngBandEntry,_j:gePortID,'geIngressStatus':geIngressStatus,'geIngressRate':geIngressRate,'geIngressPkType':geIngressPkType,'geQueScheTable':geQueScheTable,'geQueScheEntry':geQueScheEntry,_k:gePortSessionID,_l:queueID,'queueSchedule':queueSchedule,'geQosPrimapUsrToTraffic':geQosPrimapUsrToTraffic,'gePortIp2UserTable':gePortIp2UserTable,'gePortIp2UserEntry':gePortIp2UserEntry,'userPriority':userPriority,'portQosParamTable':portQosParamTable,'portQosParamEntry':portQosParamEntry,_m:portID,'bandWidthEgress':bandWidthEgress,'upPriorityEnable':upPriorityEnable,'dscpPriorityEnable':dscpPriorityEnable,'queScheduleMode':queScheduleMode,'remaptagToPriority':remaptagToPriority,'pvlan':pvlan,'sessionMaxNum':sessionMaxNum,'pvlanTable':pvlanTable,'pvlanEntry':pvlanEntry,_n:sessionId,'proAndIsoPortOrTrunk':proAndIsoPortOrTrunk,'lacp':lacp,'lacpAdminStatus':lacpAdminStatus,'lacpPriority':lacpPriority,'trunkNumber':trunkNumber,'trunkTable':trunkTable,'trunkEntry':trunkEntry,_o:trunkId,'trunkPvid':trunkPvid,'trunkMulticast':trunkMulticast,_AK:trunkPorts,'trunkMode':trunkMode,'lacpPortTable':lacpPortTable,'lacpPortEntry':lacpPortEntry,_p:lacpPortId,'lacpPortMode':lacpPortMode,'lacpPortTimeout':lacpPortTimeout,'layer3':layer3,'layer3PortTable':layer3PortTable,'layer3PortEntry':layer3PortEntry,_q:layer3PortId,'layer3PortIpAddrAndMask':layer3PortIpAddrAndMask,'layer3PortMacAddr':layer3PortMacAddr,'layer3PortVlanId':layer3PortVlanId,'layer3PortAdminStatus':layer3PortAdminStatus,'loopDetect':loopDetect,'loopDetectBlockDelay':loopDetectBlockDelay,'loopDetectSendPktInterval':loopDetectSendPktInterval,'loopDetectPortTable':loopDetectPortTable,'loopDetectPortEntry':loopDetectPortEntry,_W:loopDetectPortId,'loopDetectPortAdminStatus':loopDetectPortAdminStatus,'loopDetectPortProtectStatus':loopDetectPortProtectStatus,'loopDetectPortLoopStatus':loopDetectPortLoopStatus,_AI:loopDetectPortBlockStatus,_AH:loopDetectPortInVlan,'loopDetectTrunkTable':loopDetectTrunkTable,'loopDetectTrunkEntry':loopDetectTrunkEntry,_X:loopDetectTrunkId,'loopDetectTrunkAdminStatus':loopDetectTrunkAdminStatus,'loopDetectTrunkProtectStatus':loopDetectTrunkProtectStatus,'loopDetectTrunkLoopStatus':loopDetectTrunkLoopStatus,_AL:loopDetectTrunkBlockStatus,_AJ:loopDetectTrunkInVlan,'loopDetectPortTrap':loopDetectPortTrap,'loopDetectTrunkTrap':loopDetectTrunkTrap,'vlanTranslation':vlanTranslation,'vlanTranslationTable':vlanTranslationTable,'vlanTranslationEntry':vlanTranslationEntry,_s:ingressPortId,'vlanTranslationEnable':vlanTranslationEnable,'vlanTranslationStatus':vlanTranslationStatus,'stp':stp,'stpAdminStatus':stpAdminStatus,'vct':vct,'vctPortTable':vctPortTable,'vctPortEntry':vctPortEntry,_t:vctPortId,'vctDo':vctDo,'vctIsValid':vctIsValid,'vctPair1Result':vctPair1Result,'vctPair1Lenth':vctPair1Lenth,'vctPair2Result':vctPair2Result,'vctPair2Lenth':vctPair2Lenth,'vctPair3Result':vctPair3Result,'vctPair3Lenth':vctPair3Lenth,'vctPair4Result':vctPair4Result,'vctPair4Lenth':vctPair4Lenth,'syslog':syslog,'syslogStatus':syslogStatus,'syslogLevel':syslogLevel,'enabledModule':enabledModule,'serverMaxNum':serverMaxNum,'serverTable':serverTable,'serverEntry':serverEntry,_u:serverId,'serverIP':serverIP,'serverName':serverName,'serverAdminStatus':serverAdminStatus,'ntp':ntp,'synchronizeStatus':synchronizeStatus,'protocolStatus':protocolStatus,'srvIpAddrAndVersion':srvIpAddrAndVersion,'sourceIpAddr':sourceIpAddr,'loginUser':loginUser,'userTable':userTable,'userEntry':userEntry,_v:userName,'userAttr':userAttr,'loginPass':loginPass,'adminPass':adminPass,'snmpConfig':snmpConfig,'communityTable':communityTable,'communityEntry':communityEntry,_w:communityName,'communityAttr':communityAttr,'viewAttached':viewAttached,'viewTable':viewTable,'viewEntry':viewEntry,_x:viewIndex,_y:viewName,'attrAndOid':attrAndOid,'trapHostTable':trapHostTable,'trapHostEntry':trapHostEntry,_z:traphostIP,_A0:traphostType,_A1:commuName,'traphostVer':traphostVer,'trapEnable':trapEnable,'acl':acl,'timeAclTable':timeAclTable,'timeAclEntry':timeAclEntry,_A2:timeRangeName,'timeRange':timeRange,'basicAclTable':basicAclTable,'basicAclEntry':basicAclEntry,_A3:basicACLNo,_A4:basicRuleID,'ruleBasicStatus':ruleBasicStatus,'ruleBasicACL':ruleBasicACL,'extendedAclTable':extendedAclTable,'extendedAclEntry':extendedAclEntry,_A5:extendedACLNo,_A6:extendedRuleID,'ruleExtendedStatus':ruleExtendedStatus,'ruleExtendedProtocol':ruleExtendedProtocol,'linkAclTable':linkAclTable,'linkAclEntry':linkAclEntry,_A7:linkACLNo,_A8:linkRuleID,'ruleLinkStatus':ruleLinkStatus,'ruleLinkProtocol':ruleLinkProtocol,'hybridAclTable':hybridAclTable,'hybridAclEntry':hybridAclEntry,_A9:hybridACLNo,_AA:hybridRuleID,'ruleHybridStatus':ruleHybridStatus,'ruleHybridProtocol':ruleHybridProtocol,'globalAclTable':globalAclTable,'globalAclEntry':globalAclEntry,_AB:globalACLNo,_AC:globalRuleID,'ruleGlobalStatus':ruleGlobalStatus,'ruleGlobalProtocol':ruleGlobalProtocol,'fdb':fdb,'fdbAgingTime':fdbAgingTime,'fdbFilterTable':fdbFilterTable,'fdbFilterEntry':fdbFilterEntry,_U:fdbID,_AD:fdbFilterAddress,'fdbFilterType':fdbFilterType,'fdbStaticPortTable':fdbStaticPortTable,'fdbStaticPortEntry':fdbStaticPortEntry,_Z:fdbStaticAddress,'portBindMac':portBindMac,'fdbStaticTrunkTable':fdbStaticTrunkTable,'fdbStaticTrunkEntry':fdbStaticTrunkEntry,'trunkBindMac':trunkBindMac,'p8021xRelay':p8021xRelay,'p8021xRelayAdminStatus':p8021xRelayAdminStatus,'igmpSnooping':igmpSnooping,'multiGroupTable':multiGroupTable,'multiGroupEntry':multiGroupEntry,'number':number,'vlanID':vlanID,'multiGroup':multiGroup,'portList':portList,'trunkList':trunkList,'epon':epon,'ponReset':ponReset,'portPonInfo':portPonInfo,'portPonAdminStatus':portPonAdminStatus,'portPonStpState':portPonStpState,'portPonFecTx':portPonFecTx,'portPonFecRx':portPonFecRx,'portPonType':portPonType,'portPonOperStatus':portPonOperStatus,'portPonLlidPortsNum':portPonLlidPortsNum,'ponOamInfo':ponOamInfo,'localOamAdmin':localOamAdmin,'localOamOper':localOamOper,'localOamMode':localOamMode,'localOamMaxPdu':localOamMaxPdu,'localOamRevision':localOamRevision,'localOamFuncSupport':localOamFuncSupport,'peerOamStatus':peerOamStatus,'peerOamMacAddr':peerOamMacAddr,'peerOamOUI':peerOamOUI,'peerOamVendor':peerOamVendor,'peerOamMode':peerOamMode,'peerOamMaxPdu':peerOamMaxPdu,'peerOamRevision':peerOamRevision,'peerOamFuncSupport':peerOamFuncSupport,'ponLoopbackStatus':ponLoopbackStatus,'ponFirmwareInfo':ponFirmwareInfo,'eponStatus':eponStatus,'softWareVersion':softWareVersion,'loaderVersion':loaderVersion,'registerOltInfo':registerOltInfo,'registerOnuInfo':registerOnuInfo,'portNum':portNum,_AE:registered,'authenticated':authenticated,'ponConfigMac':ponConfigMac,'modeAndOamVer':modeAndOamVer,'mpcpTimeout':mpcpTimeout,'ctrlVlan':ctrlVlan,'vendPonUni':vendPonUni,'ctcOui':ctcOui,'ctcVendor':ctcVendor,'ctcModel':ctcModel,'ethernetOam':ethernetOam,'ethernetOamStatus':ethernetOamStatus,'ethernetOamOuiDescr':ethernetOamOuiDescr,'orgSpecificTimeStamp':orgSpecificTimeStamp,'remoteLoopbackTimeout':remoteLoopbackTimeout,'ethernetOamIfConfigTable':ethernetOamIfConfigTable,'ethernetOamIfConfigEntry':ethernetOamIfConfigEntry,'ethernetOamIfStatus':ethernetOamIfStatus,'remoteLoopbackIfStatus':remoteLoopbackIfStatus,'ifPeriodTimeoutMode':ifPeriodTimeoutMode,'ifLinkMonitorStatus':ifLinkMonitorStatus,'ifLinkSymbolPeriodThresholdWindow':ifLinkSymbolPeriodThresholdWindow,'ifLinkFrameThresholdWindow':ifLinkFrameThresholdWindow,'ifLinkFramePeriodThresholdWindow':ifLinkFramePeriodThresholdWindow,'ifLinkFrameSecondsThresholdWindow':ifLinkFrameSecondsThresholdWindow,'ethernetOamShowTable':ethernetOamShowTable,'ethernetOamShowEntry':ethernetOamShowEntry,'ethernetOamShowDiscovery':ethernetOamShowDiscovery,'ethernetOamShowLinkMonitor':ethernetOamShowLinkMonitor,'ethernetOamShowStatistics':ethernetOamShowStatistics,'linkMonitorSymbolPeriodTrap':linkMonitorSymbolPeriodTrap,'linkMonitorFrameTrap':linkMonitorFrameTrap,'linkMonitorFramePeriodTrap':linkMonitorFramePeriodTrap,'linkMonitorFrameSecondsTrap':linkMonitorFrameSecondsTrap,'remoteLinkFailTrap':remoteLinkFailTrap,'remoteLinkOKTrap':remoteLinkOKTrap,'dyingGaspTrap':dyingGaspTrap,'remoteDiscoveryFailTrap':remoteDiscoveryFailTrap,_P:remoteMAC,'opticalInformation':opticalInformation,'opticalInfoTable':opticalInfoTable,'opticalInfoEntry':opticalInfoEntry,_AF:opticalInfoPortId,'opticalInfoIfName':opticalInfoIfName,'opticalInfoOnline':opticalInfoOnline,'opticalInfoSWaveLenth':opticalInfoSWaveLenth,'opticalInfoPowerSupport':opticalInfoPowerSupport,'opticalInfoSRxPower':opticalInfoSRxPower,'opticalInfoSRxPowerValid':opticalInfoSRxPowerValid,'opticalInfoSTxPower':opticalInfoSTxPower,'opticalInfoSTxPowerValid':opticalInfoSTxPowerValid,'opticalInfoSTxPowerStatus':opticalInfoSTxPowerStatus,'opticalInfoSRxPowerStatus':opticalInfoSRxPowerStatus,'opticalInfoVName':opticalInfoVName,'opticalInfoType':opticalInfoType,'opticalInfoVSn':opticalInfoVSn,'opticalInfoDistanse':opticalInfoDistanse,'opticalInfoMode':opticalInfoMode})