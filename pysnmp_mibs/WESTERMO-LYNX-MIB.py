_A5='linkDownChangeWarning'
_A4='linkUpChangeWarning'
_A3='statNoWarning'
_A2='statWarning'
_A1='querytimeout'
_A0='stopfilter'
_z='enableStatusTrap'
_y='statusCode'
_x='dhcpRelayAgentServer2'
_w='dhcpRelayAgentServer1'
_v='dhcpRelayAgent'
_u='defaultGateway'
_t='ipNetMask'
_s='ipAddress'
_r='enableVlan'
_q='frntPorts'
_p='ontPortNumber'
_o='writePassword'
_n='readPassword'
_m='trapHostAddr2'
_l='trapHostAddr1'
_k='powerSupply'
_j='hwConfig'
_i='batchID'
_h='serialNumber'
_g='hwVersionPld'
_f='hwVersionBoard'
_e='swVersionBootLoader'
_d='swVersion'
_c='temperature'
_b='linkStatus'
_a='rstpPortStatus'
_Z='igmpColor'
_Y='vlanDefaultColor'
_X='vlanPrio'
_W='vlanId'
_V='removePortTag'
_U='portVlanColors'
_T='igmpPortTrunk'
_S='rstpPortTrunk'
_R='timeSyncFilters'
_Q='portType'
_P='portAlarm'
_O='portSpeed'
_N='portAutoNegotiate'
_M='portDuplexMode'
_L='portEnable'
_K='portIndex'
_J='reset'
_I='enable'
_H='disable'
_G='off'
_F='on'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='WESTERMO-LYNX-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
products,=mibBuilder.importSymbols('WESTERMO-OID-MIB','products')
lynx=ModuleIdentity((1,3,6,1,4,1,16177,1,2))
if mibBuilder.loadTexts:lynx.setRevisions(('2009-05-28 00:00','2006-06-29 23:59','2006-04-12 08:19','2006-04-12 06:19'))
_General_ObjectIdentity=ObjectIdentity
general=_General_ObjectIdentity((1,3,6,1,4,1,16177,1,2,1))
class _Temperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_Temperature_Type.__name__=_D
_Temperature_Object=MibScalar
temperature=_Temperature_Object((1,3,6,1,4,1,16177,1,2,1,1),_Temperature_Type())
temperature.setMaxAccess(_E)
if mibBuilder.loadTexts:temperature.setStatus(_A)
_SwVersion_Type=DisplayString
_SwVersion_Object=MibScalar
swVersion=_SwVersion_Object((1,3,6,1,4,1,16177,1,2,1,2),_SwVersion_Type())
swVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:swVersion.setStatus(_A)
_SwVersionBootLoader_Type=DisplayString
_SwVersionBootLoader_Object=MibScalar
swVersionBootLoader=_SwVersionBootLoader_Object((1,3,6,1,4,1,16177,1,2,1,3),_SwVersionBootLoader_Type())
swVersionBootLoader.setMaxAccess(_E)
if mibBuilder.loadTexts:swVersionBootLoader.setStatus(_A)
_HwVersionBoard_Type=DisplayString
_HwVersionBoard_Object=MibScalar
hwVersionBoard=_HwVersionBoard_Object((1,3,6,1,4,1,16177,1,2,1,4),_HwVersionBoard_Type())
hwVersionBoard.setMaxAccess(_E)
if mibBuilder.loadTexts:hwVersionBoard.setStatus(_A)
_HwVersionPld_Type=DisplayString
_HwVersionPld_Object=MibScalar
hwVersionPld=_HwVersionPld_Object((1,3,6,1,4,1,16177,1,2,1,5),_HwVersionPld_Type())
hwVersionPld.setMaxAccess(_E)
if mibBuilder.loadTexts:hwVersionPld.setStatus(_A)
_SerialNumber_Type=DisplayString
_SerialNumber_Object=MibScalar
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,16177,1,2,1,6),_SerialNumber_Type())
serialNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:serialNumber.setStatus(_A)
_BatchID_Type=DisplayString
_BatchID_Object=MibScalar
batchID=_BatchID_Object((1,3,6,1,4,1,16177,1,2,1,7),_BatchID_Type())
batchID.setMaxAccess(_E)
if mibBuilder.loadTexts:batchID.setStatus(_A)
class _HwConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(22,23)));namedValues=NamedValues(*(('amd',22),('intel',23)))
_HwConfig_Type.__name__=_D
_HwConfig_Object=MibScalar
hwConfig=_HwConfig_Object((1,3,6,1,4,1,16177,1,2,1,8),_HwConfig_Type())
hwConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:hwConfig.setStatus(_A)
class _Reset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('factoryDefault',2)))
_Reset_Type.__name__=_D
_Reset_Object=MibScalar
reset=_Reset_Object((1,3,6,1,4,1,16177,1,2,1,9),_Reset_Type())
reset.setMaxAccess(_C)
if mibBuilder.loadTexts:reset.setStatus(_A)
class _PowerSupply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('okpowerAB',1),('okpowerA',2),('okpowerB',3)))
_PowerSupply_Type.__name__=_D
_PowerSupply_Object=MibScalar
powerSupply=_PowerSupply_Object((1,3,6,1,4,1,16177,1,2,1,10),_PowerSupply_Type())
powerSupply.setMaxAccess(_E)
if mibBuilder.loadTexts:powerSupply.setStatus(_A)
_TrapHostAddr1_Type=DisplayString
_TrapHostAddr1_Object=MibScalar
trapHostAddr1=_TrapHostAddr1_Object((1,3,6,1,4,1,16177,1,2,1,11),_TrapHostAddr1_Type())
trapHostAddr1.setMaxAccess(_C)
if mibBuilder.loadTexts:trapHostAddr1.setStatus(_A)
_TrapHostAddr2_Type=DisplayString
_TrapHostAddr2_Object=MibScalar
trapHostAddr2=_TrapHostAddr2_Object((1,3,6,1,4,1,16177,1,2,1,12),_TrapHostAddr2_Type())
trapHostAddr2.setMaxAccess(_C)
if mibBuilder.loadTexts:trapHostAddr2.setStatus(_A)
_ReadPassword_Type=DisplayString
_ReadPassword_Object=MibScalar
readPassword=_ReadPassword_Object((1,3,6,1,4,1,16177,1,2,1,13),_ReadPassword_Type())
readPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:readPassword.setStatus(_A)
_WritePassword_Type=DisplayString
_WritePassword_Object=MibScalar
writePassword=_WritePassword_Object((1,3,6,1,4,1,16177,1,2,1,14),_WritePassword_Type())
writePassword.setMaxAccess(_C)
if mibBuilder.loadTexts:writePassword.setStatus(_A)
_Config_ObjectIdentity=ObjectIdentity
config=_Config_ObjectIdentity((1,3,6,1,4,1,16177,1,2,2))
class _OntPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_OntPortNumber_Type.__name__=_D
_OntPortNumber_Object=MibScalar
ontPortNumber=_OntPortNumber_Object((1,3,6,1,4,1,16177,1,2,2,1),_OntPortNumber_Type())
ontPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:ontPortNumber.setStatus(_A)
_OntTable_Object=MibTable
ontTable=_OntTable_Object((1,3,6,1,4,1,16177,1,2,2,2))
if mibBuilder.loadTexts:ontTable.setStatus(_A)
_OntEntry_Object=MibTableRow
ontEntry=_OntEntry_Object((1,3,6,1,4,1,16177,1,2,2,2,1))
ontEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:ontEntry.setStatus(_A)
_PortIndex_Type=Integer32
_PortIndex_Object=MibTableColumn
portIndex=_PortIndex_Object((1,3,6,1,4,1,16177,1,2,2,2,1,1),_PortIndex_Type())
portIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
class _PortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_I,2),(_H,3)))
_PortEnable_Type.__name__=_D
_PortEnable_Object=MibTableColumn
portEnable=_PortEnable_Object((1,3,6,1,4,1,16177,1,2,2,2,1,2),_PortEnable_Type())
portEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:portEnable.setStatus(_A)
class _PortDuplexMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('half',2),('full',3)))
_PortDuplexMode_Type.__name__=_D
_PortDuplexMode_Object=MibTableColumn
portDuplexMode=_PortDuplexMode_Object((1,3,6,1,4,1,16177,1,2,2,2,1,3),_PortDuplexMode_Type())
portDuplexMode.setMaxAccess(_C)
if mibBuilder.loadTexts:portDuplexMode.setStatus(_A)
class _PortAutoNegotiate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_I,2),(_H,3)))
_PortAutoNegotiate_Type.__name__=_D
_PortAutoNegotiate_Object=MibTableColumn
portAutoNegotiate=_PortAutoNegotiate_Object((1,3,6,1,4,1,16177,1,2,2,2,1,4),_PortAutoNegotiate_Type())
portAutoNegotiate.setMaxAccess(_C)
if mibBuilder.loadTexts:portAutoNegotiate.setStatus(_A)
class _PortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,100,1000)));namedValues=NamedValues(*(('s10M',10),('s100M',100),('s1000M',1000)))
_PortSpeed_Type.__name__=_D
_PortSpeed_Object=MibTableColumn
portSpeed=_PortSpeed_Object((1,3,6,1,4,1,16177,1,2,2,2,1,5),_PortSpeed_Type())
portSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:portSpeed.setStatus(_A)
class _PortAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_PortAlarm_Type.__name__=_D
_PortAlarm_Object=MibTableColumn
portAlarm=_PortAlarm_Object((1,3,6,1,4,1,16177,1,2,2,2,1,6),_PortAlarm_Type())
portAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:portAlarm.setStatus(_A)
_PortType_Type=DisplayString
_PortType_Object=MibTableColumn
portType=_PortType_Object((1,3,6,1,4,1,16177,1,2,2,2,1,7),_PortType_Type())
portType.setMaxAccess(_E)
if mibBuilder.loadTexts:portType.setStatus(_A)
class _TimeSyncFilters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('nonTiming',1),('timing',2),('unfiltered',3)))
_TimeSyncFilters_Type.__name__=_D
_TimeSyncFilters_Object=MibTableColumn
timeSyncFilters=_TimeSyncFilters_Object((1,3,6,1,4,1,16177,1,2,2,2,1,8),_TimeSyncFilters_Type())
timeSyncFilters.setMaxAccess(_C)
if mibBuilder.loadTexts:timeSyncFilters.setStatus(_A)
class _RstpPortTrunk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_RstpPortTrunk_Type.__name__=_D
_RstpPortTrunk_Object=MibTableColumn
rstpPortTrunk=_RstpPortTrunk_Object((1,3,6,1,4,1,16177,1,2,2,2,1,9),_RstpPortTrunk_Type())
rstpPortTrunk.setMaxAccess(_C)
if mibBuilder.loadTexts:rstpPortTrunk.setStatus(_A)
class _IgmpPortTrunk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_IgmpPortTrunk_Type.__name__=_D
_IgmpPortTrunk_Object=MibTableColumn
igmpPortTrunk=_IgmpPortTrunk_Object((1,3,6,1,4,1,16177,1,2,2,2,1,10),_IgmpPortTrunk_Type())
igmpPortTrunk.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpPortTrunk.setStatus(_A)
class _RemovePortTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('keepTag',1),('removeTag',2)))
_RemovePortTag_Type.__name__=_D
_RemovePortTag_Object=MibTableColumn
removePortTag=_RemovePortTag_Object((1,3,6,1,4,1,16177,1,2,2,2,1,12),_RemovePortTag_Type())
removePortTag.setMaxAccess(_C)
if mibBuilder.loadTexts:removePortTag.setStatus(_A)
class _VlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_VlanId_Type.__name__=_D
_VlanId_Object=MibTableColumn
vlanId=_VlanId_Object((1,3,6,1,4,1,16177,1,2,2,2,1,13),_VlanId_Type())
vlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanId.setStatus(_A)
class _VlanPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('prio0',0),('prio1',1),('prio2',2),('prio3',3),('prio4',4),('prio5',5),('prio6',6),('prio7',7)))
_VlanPrio_Type.__name__=_D
_VlanPrio_Object=MibTableColumn
vlanPrio=_VlanPrio_Object((1,3,6,1,4,1,16177,1,2,2,2,1,14),_VlanPrio_Type())
vlanPrio.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanPrio.setStatus(_A)
_PortVlanColors_Type=DisplayString
_PortVlanColors_Object=MibTableColumn
portVlanColors=_PortVlanColors_Object((1,3,6,1,4,1,16177,1,2,2,2,1,15),_PortVlanColors_Type())
portVlanColors.setMaxAccess(_C)
if mibBuilder.loadTexts:portVlanColors.setStatus(_A)
class _VlanDefaultColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('white',0),('red',1),('blue',2),('green',3),('yellow',4),('brown',5),('pink',6)))
_VlanDefaultColor_Type.__name__=_D
_VlanDefaultColor_Object=MibTableColumn
vlanDefaultColor=_VlanDefaultColor_Object((1,3,6,1,4,1,16177,1,2,2,2,1,16),_VlanDefaultColor_Type())
vlanDefaultColor.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanDefaultColor.setStatus(_A)
class _IgmpColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*(('black',1),('red',3)))
_IgmpColor_Type.__name__=_D
_IgmpColor_Object=MibTableColumn
igmpColor=_IgmpColor_Object((1,3,6,1,4,1,16177,1,2,2,2,1,17),_IgmpColor_Type())
igmpColor.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpColor.setStatus(_A)
class _RstpPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('discarding',1),('forwarding',2)))
_RstpPortStatus_Type.__name__=_D
_RstpPortStatus_Object=MibTableColumn
rstpPortStatus=_RstpPortStatus_Object((1,3,6,1,4,1,16177,1,2,2,2,1,18),_RstpPortStatus_Type())
rstpPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rstpPortStatus.setStatus(_A)
class _LinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_LinkStatus_Type.__name__=_D
_LinkStatus_Object=MibTableColumn
linkStatus=_LinkStatus_Object((1,3,6,1,4,1,16177,1,2,2,2,1,19),_LinkStatus_Type())
linkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:linkStatus.setStatus(_A)
class _Snmp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_Snmp_Type.__name__=_D
_Snmp_Object=MibScalar
snmp=_Snmp_Object((1,3,6,1,4,1,16177,1,2,2,3),_Snmp_Type())
snmp.setMaxAccess(_C)
if mibBuilder.loadTexts:snmp.setStatus(_A)
class _Frnt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_H,2),('focalpoint',3),('member',4)))
_Frnt_Type.__name__=_D
_Frnt_Object=MibScalar
frnt=_Frnt_Object((1,3,6,1,4,1,16177,1,2,2,4),_Frnt_Type())
frnt.setMaxAccess(_C)
if mibBuilder.loadTexts:frnt.setStatus(_A)
class _FrntPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_FrntPorts_Type.__name__=_D
_FrntPorts_Object=MibScalar
frntPorts=_FrntPorts_Object((1,3,6,1,4,1,16177,1,2,2,5),_FrntPorts_Type())
frntPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:frntPorts.setStatus(_A)
class _Dhcp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_Dhcp_Type.__name__=_D
_Dhcp_Object=MibScalar
dhcp=_Dhcp_Object((1,3,6,1,4,1,16177,1,2,2,6),_Dhcp_Type())
dhcp.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcp.setStatus(_A)
class _EnableVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_EnableVlan_Type.__name__=_D
_EnableVlan_Object=MibScalar
enableVlan=_EnableVlan_Object((1,3,6,1,4,1,16177,1,2,2,7),_EnableVlan_Type())
enableVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:enableVlan.setStatus(_A)
_IpAddress_Type=IpAddress
_IpAddress_Object=MibScalar
ipAddress=_IpAddress_Object((1,3,6,1,4,1,16177,1,2,2,8),_IpAddress_Type())
ipAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ipAddress.setStatus(_A)
_IpNetMask_Type=IpAddress
_IpNetMask_Object=MibScalar
ipNetMask=_IpNetMask_Object((1,3,6,1,4,1,16177,1,2,2,9),_IpNetMask_Type())
ipNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ipNetMask.setStatus(_A)
_DefaultGateway_Type=IpAddress
_DefaultGateway_Object=MibScalar
defaultGateway=_DefaultGateway_Object((1,3,6,1,4,1,16177,1,2,2,10),_DefaultGateway_Type())
defaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:defaultGateway.setStatus(_A)
class _DhcpRelayAgent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_DhcpRelayAgent_Type.__name__=_D
_DhcpRelayAgent_Object=MibScalar
dhcpRelayAgent=_DhcpRelayAgent_Object((1,3,6,1,4,1,16177,1,2,2,11),_DhcpRelayAgent_Type())
dhcpRelayAgent.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRelayAgent.setStatus(_A)
_DhcpRelayAgentServer1_Type=IpAddress
_DhcpRelayAgentServer1_Object=MibScalar
dhcpRelayAgentServer1=_DhcpRelayAgentServer1_Object((1,3,6,1,4,1,16177,1,2,2,12),_DhcpRelayAgentServer1_Type())
dhcpRelayAgentServer1.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRelayAgentServer1.setStatus(_A)
_DhcpRelayAgentServer2_Type=IpAddress
_DhcpRelayAgentServer2_Object=MibScalar
dhcpRelayAgentServer2=_DhcpRelayAgentServer2_Object((1,3,6,1,4,1,16177,1,2,2,13),_DhcpRelayAgentServer2_Type())
dhcpRelayAgentServer2.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRelayAgentServer2.setStatus(_A)
class _Rstp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('root',1),(_F,2),(_G,3)))
_Rstp_Type.__name__=_D
_Rstp_Object=MibScalar
rstp=_Rstp_Object((1,3,6,1,4,1,16177,1,2,2,14),_Rstp_Type())
rstp.setMaxAccess(_C)
if mibBuilder.loadTexts:rstp.setStatus(_A)
_Igmp_ObjectIdentity=ObjectIdentity
igmp=_Igmp_ObjectIdentity((1,3,6,1,4,1,16177,1,2,5))
class _Snooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_Snooping_Type.__name__=_D
_Snooping_Object=MibScalar
snooping=_Snooping_Object((1,3,6,1,4,1,16177,1,2,5,1),_Snooping_Type())
snooping.setMaxAccess(_C)
if mibBuilder.loadTexts:snooping.setStatus(_A)
class _Automode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_Automode_Type.__name__=_D
_Automode_Object=MibScalar
automode=_Automode_Object((1,3,6,1,4,1,16177,1,2,5,2),_Automode_Type())
automode.setMaxAccess(_C)
if mibBuilder.loadTexts:automode.setStatus(_A)
class _Querier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_Querier_Type.__name__=_D
_Querier_Object=MibScalar
querier=_Querier_Object((1,3,6,1,4,1,16177,1,2,5,3),_Querier_Type())
querier.setMaxAccess(_C)
if mibBuilder.loadTexts:querier.setStatus(_A)
class _Stopfilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_Stopfilter_Type.__name__=_D
_Stopfilter_Object=MibScalar
stopfilter=_Stopfilter_Object((1,3,6,1,4,1,16177,1,2,5,4),_Stopfilter_Type())
stopfilter.setMaxAccess(_C)
if mibBuilder.loadTexts:stopfilter.setStatus(_A)
class _Querytimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(12,30,70,150)));namedValues=NamedValues(*(('t12s',12),('t30s',30),('t70s',70),('t150s',150)))
_Querytimeout_Type.__name__=_D
_Querytimeout_Object=MibScalar
querytimeout=_Querytimeout_Object((1,3,6,1,4,1,16177,1,2,5,6),_Querytimeout_Type())
querytimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:querytimeout.setStatus(_A)
_Stat_ObjectIdentity=ObjectIdentity
stat=_Stat_ObjectIdentity((1,3,6,1,4,1,16177,1,2,6))
class _StatusCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('error',2)))
_StatusCode_Type.__name__=_D
_StatusCode_Object=MibScalar
statusCode=_StatusCode_Object((1,3,6,1,4,1,16177,1,2,6,1),_StatusCode_Type())
statusCode.setMaxAccess(_E)
if mibBuilder.loadTexts:statusCode.setStatus(_A)
class _EnableStatusTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_F,2),(_G,3)))
_EnableStatusTrap_Type.__name__=_D
_EnableStatusTrap_Object=MibScalar
enableStatusTrap=_EnableStatusTrap_Object((1,3,6,1,4,1,16177,1,2,6,2),_EnableStatusTrap_Type())
enableStatusTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:enableStatusTrap.setStatus(_A)
_PrivTraps_ObjectIdentity=ObjectIdentity
privTraps=_PrivTraps_ObjectIdentity((1,3,6,1,4,1,16177,1,2,7))
portGroup=ObjectGroup((1,3,6,1,4,1,16177,1,2,1,15))
portGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:portGroup.setStatus(_A)
miscGroup=ObjectGroup((1,3,6,1,4,1,16177,1,2,1,16))
miscGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_J),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,'snmp'),(_B,'frnt'),(_B,_q),(_B,'dhcp'),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,'rstp'),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:miscGroup.setStatus(_A)
igmpGroup=ObjectGroup((1,3,6,1,4,1,16177,1,2,1,18))
igmpGroup.setObjects(*((_B,'snooping'),(_B,'querier'),(_B,'automode'),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:igmpGroup.setStatus(_A)
statWarning=NotificationType((1,3,6,1,4,1,16177,1,2,7,1))
if mibBuilder.loadTexts:statWarning.setStatus(_A)
statNoWarning=NotificationType((1,3,6,1,4,1,16177,1,2,7,2))
if mibBuilder.loadTexts:statNoWarning.setStatus(_A)
linkUpChangeWarning=NotificationType((1,3,6,1,4,1,16177,1,2,7,3))
if mibBuilder.loadTexts:linkUpChangeWarning.setStatus(_A)
linkDownChangeWarning=NotificationType((1,3,6,1,4,1,16177,1,2,7,4))
if mibBuilder.loadTexts:linkDownChangeWarning.setStatus(_A)
trapGroup=NotificationGroup((1,3,6,1,4,1,16177,1,2,1,17))
trapGroup.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:trapGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lynx':lynx,'general':general,_c:temperature,_d:swVersion,_e:swVersionBootLoader,_f:hwVersionBoard,_g:hwVersionPld,_h:serialNumber,_i:batchID,_j:hwConfig,_J:reset,_k:powerSupply,_l:trapHostAddr1,_m:trapHostAddr2,_n:readPassword,_o:writePassword,'portGroup':portGroup,'miscGroup':miscGroup,'trapGroup':trapGroup,'igmpGroup':igmpGroup,'config':config,_p:ontPortNumber,'ontTable':ontTable,'ontEntry':ontEntry,_K:portIndex,_L:portEnable,_M:portDuplexMode,_N:portAutoNegotiate,_O:portSpeed,_P:portAlarm,_Q:portType,_R:timeSyncFilters,_S:rstpPortTrunk,_T:igmpPortTrunk,_V:removePortTag,_W:vlanId,_X:vlanPrio,_U:portVlanColors,_Y:vlanDefaultColor,_Z:igmpColor,_a:rstpPortStatus,_b:linkStatus,'snmp':snmp,'frnt':frnt,_q:frntPorts,'dhcp':dhcp,_r:enableVlan,_s:ipAddress,_t:ipNetMask,_u:defaultGateway,_v:dhcpRelayAgent,_w:dhcpRelayAgentServer1,_x:dhcpRelayAgentServer2,'rstp':rstp,'igmp':igmp,'snooping':snooping,'automode':automode,'querier':querier,_A0:stopfilter,_A1:querytimeout,'stat':stat,_y:statusCode,_z:enableStatusTrap,'privTraps':privTraps,_A2:statWarning,_A3:statNoWarning,_A4:linkUpChangeWarning,_A5:linkDownChangeWarning})