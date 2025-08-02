_A7='spanningTreePortStatusIndex'
_A6='remoteIpIndex'
_A5='groupName'
_A4='userAccountIndex'
_A3='userTableIndex'
_A2='routeTableIndex'
_A1='hostTableIndex'
_A0='accessibleIpListIndex'
_z='bits-7'
_y='bits-6'
_x='bits-5'
_w='rs-485-4-wire'
_v='rs-485-2-wire'
_u='rs-422'
_t='rs-232'
_s='forward-to-all-open-connections'
_r='forward-to-last-requester'
_q='discard'
_p='ethernet-Modem'
_o='socket'
_n='printer'
_m='terminal'
_l='spanningTreePortIndex'
_k='priority-0'
_j='static'
_i='remoteHostFail-remoteHostRecovered'
_h='periodicallyConnect-InactivityTime'
_g='alwaysOn-None'
_f='pppd'
_e='ppp'
_d='yes'
_c='turboRingV2'
_b='turboRing'
_a='spanningTree'
_Z='always-low'
_Y='always-high'
_X='acked'
_W='alarm-Acked'
_V='alarm'
_U='no-display'
_T='local-tacacsPlus'
_S='tacacsPlus-local'
_R='tacacsPlus'
_Q='local-radius'
_P='radius-local'
_O='radius'
_N='local'
_M='on'
_L='off'
_K='write-only'
_J='none'
_I='portIndex'
_H='MOXA-NP6000-MIB'
_G='read-only'
_F='DisplayString'
_E='enable'
_D='disable'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','TextualConvention')
np6000=ModuleIdentity((1,3,6,1,4,1,8691,2,8))
class PortList(TextualConvention,OctetString):status=_A
_Moxa_ObjectIdentity=ObjectIdentity
moxa=_Moxa_ObjectIdentity((1,3,6,1,4,1,8691))
_Nport_ObjectIdentity=ObjectIdentity
nport=_Nport_ObjectIdentity((1,3,6,1,4,1,8691,2))
_SwMgmt_ObjectIdentity=ObjectIdentity
swMgmt=_SwMgmt_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1))
_Overview_ObjectIdentity=ObjectIdentity
overview=_Overview_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,1))
_ModelName_Type=DisplayString
_ModelName_Object=MibScalar
modelName=_ModelName_Object((1,3,6,1,4,1,8691,2,8,1,1,1),_ModelName_Type())
modelName.setMaxAccess(_G)
if mibBuilder.loadTexts:modelName.setStatus(_A)
_SerialNumber_Type=Integer32
_SerialNumber_Object=MibScalar
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,8691,2,8,1,1,2),_SerialNumber_Type())
serialNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:serialNumber.setStatus(_A)
_FirmwareVersion_Type=DisplayString
_FirmwareVersion_Object=MibScalar
firmwareVersion=_FirmwareVersion_Object((1,3,6,1,4,1,8691,2,8,1,1,3),_FirmwareVersion_Type())
firmwareVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:firmwareVersion.setStatus(_A)
_MacAddress_Type=MacAddress
_MacAddress_Object=MibScalar
macAddress=_MacAddress_Object((1,3,6,1,4,1,8691,2,8,1,1,4),_MacAddress_Type())
macAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:macAddress.setStatus(_A)
_ViewLanSpeed_Type=DisplayString
_ViewLanSpeed_Object=MibScalar
viewLanSpeed=_ViewLanSpeed_Object((1,3,6,1,4,1,8691,2,8,1,1,5),_ViewLanSpeed_Type())
viewLanSpeed.setMaxAccess(_G)
if mibBuilder.loadTexts:viewLanSpeed.setStatus(_A)
_ViewLanModuleSpeed_Type=DisplayString
_ViewLanModuleSpeed_Object=MibScalar
viewLanModuleSpeed=_ViewLanModuleSpeed_Object((1,3,6,1,4,1,8691,2,8,1,1,6),_ViewLanModuleSpeed_Type())
viewLanModuleSpeed.setMaxAccess(_G)
if mibBuilder.loadTexts:viewLanModuleSpeed.setStatus(_A)
_UpTime_Type=DisplayString
_UpTime_Object=MibScalar
upTime=_UpTime_Object((1,3,6,1,4,1,8691,2,8,1,1,7),_UpTime_Type())
upTime.setMaxAccess(_G)
if mibBuilder.loadTexts:upTime.setStatus(_A)
_ModuleType_Type=DisplayString
_ModuleType_Object=MibScalar
moduleType=_ModuleType_Object((1,3,6,1,4,1,8691,2,8,1,1,8),_ModuleType_Type())
moduleType.setMaxAccess(_G)
if mibBuilder.loadTexts:moduleType.setStatus(_A)
_ModuleApVersion_Type=DisplayString
_ModuleApVersion_Object=MibScalar
moduleApVersion=_ModuleApVersion_Object((1,3,6,1,4,1,8691,2,8,1,1,9),_ModuleApVersion_Type())
moduleApVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:moduleApVersion.setStatus(_A)
_ViewIpv4Address_Type=DisplayString
_ViewIpv4Address_Object=MibScalar
viewIpv4Address=_ViewIpv4Address_Object((1,3,6,1,4,1,8691,2,8,1,1,10),_ViewIpv4Address_Type())
viewIpv4Address.setMaxAccess(_G)
if mibBuilder.loadTexts:viewIpv4Address.setStatus(_A)
_ViewIpv6LinkLocalAddress_Type=DisplayString
_ViewIpv6LinkLocalAddress_Object=MibScalar
viewIpv6LinkLocalAddress=_ViewIpv6LinkLocalAddress_Object((1,3,6,1,4,1,8691,2,8,1,1,11),_ViewIpv6LinkLocalAddress_Type())
viewIpv6LinkLocalAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:viewIpv6LinkLocalAddress.setStatus(_A)
_ViewIpv6GlobalAddress_Type=DisplayString
_ViewIpv6GlobalAddress_Object=MibScalar
viewIpv6GlobalAddress=_ViewIpv6GlobalAddress_Object((1,3,6,1,4,1,8691,2,8,1,1,12),_ViewIpv6GlobalAddress_Type())
viewIpv6GlobalAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:viewIpv6GlobalAddress.setStatus(_A)
_BasicSetting_ObjectIdentity=ObjectIdentity
basicSetting=_BasicSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,2))
_ServerSetting_ObjectIdentity=ObjectIdentity
serverSetting=_ServerSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,2,1))
_ServerName_Type=DisplayString
_ServerName_Object=MibScalar
serverName=_ServerName_Object((1,3,6,1,4,1,8691,2,8,1,2,1,1),_ServerName_Type())
serverName.setMaxAccess(_B)
if mibBuilder.loadTexts:serverName.setStatus(_A)
_ServerLocation_Type=DisplayString
_ServerLocation_Object=MibScalar
serverLocation=_ServerLocation_Object((1,3,6,1,4,1,8691,2,8,1,2,1,2),_ServerLocation_Type())
serverLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:serverLocation.setStatus(_A)
_TimeSetting_ObjectIdentity=ObjectIdentity
timeSetting=_TimeSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,2,2))
_TimeZone_Type=Integer32
_TimeZone_Object=MibScalar
timeZone=_TimeZone_Object((1,3,6,1,4,1,8691,2,8,1,2,2,1),_TimeZone_Type())
timeZone.setMaxAccess(_B)
if mibBuilder.loadTexts:timeZone.setStatus(_A)
class _LocalTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,19))
_LocalTime_Type.__name__=_F
_LocalTime_Object=MibScalar
localTime=_LocalTime_Object((1,3,6,1,4,1,8691,2,8,1,2,2,2),_LocalTime_Type())
localTime.setMaxAccess(_B)
if mibBuilder.loadTexts:localTime.setStatus(_A)
_TimeServer_Type=DisplayString
_TimeServer_Object=MibScalar
timeServer=_TimeServer_Object((1,3,6,1,4,1,8691,2,8,1,2,2,3),_TimeServer_Type())
timeServer.setMaxAccess(_B)
if mibBuilder.loadTexts:timeServer.setStatus(_A)
_NetworkSetting_ObjectIdentity=ObjectIdentity
networkSetting=_NetworkSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,3))
class _Ipv4Configuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_j,0),('dhcp',1),('dhcp-BOOTP',2),('bootp',3),('pppoe',4)))
_Ipv4Configuration_Type.__name__=_C
_Ipv4Configuration_Object=MibScalar
ipv4Configuration=_Ipv4Configuration_Object((1,3,6,1,4,1,8691,2,8,1,3,1),_Ipv4Configuration_Type())
ipv4Configuration.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv4Configuration.setStatus(_A)
_Ipv4Address_Type=IpAddress
_Ipv4Address_Object=MibScalar
ipv4Address=_Ipv4Address_Object((1,3,6,1,4,1,8691,2,8,1,3,2),_Ipv4Address_Type())
ipv4Address.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv4Address.setStatus(_A)
_Ipv4NetMask_Type=IpAddress
_Ipv4NetMask_Object=MibScalar
ipv4NetMask=_Ipv4NetMask_Object((1,3,6,1,4,1,8691,2,8,1,3,3),_Ipv4NetMask_Type())
ipv4NetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv4NetMask.setStatus(_A)
_Ipv4DefaultGateway_Type=IpAddress
_Ipv4DefaultGateway_Object=MibScalar
ipv4DefaultGateway=_Ipv4DefaultGateway_Object((1,3,6,1,4,1,8691,2,8,1,3,4),_Ipv4DefaultGateway_Type())
ipv4DefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv4DefaultGateway.setStatus(_A)
_Ipv4DnsServer1IpAddr_Type=IpAddress
_Ipv4DnsServer1IpAddr_Object=MibScalar
ipv4DnsServer1IpAddr=_Ipv4DnsServer1IpAddr_Object((1,3,6,1,4,1,8691,2,8,1,3,5),_Ipv4DnsServer1IpAddr_Type())
ipv4DnsServer1IpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv4DnsServer1IpAddr.setStatus(_A)
_Ipv4DnsServer2IpAddr_Type=IpAddress
_Ipv4DnsServer2IpAddr_Object=MibScalar
ipv4DnsServer2IpAddr=_Ipv4DnsServer2IpAddr_Object((1,3,6,1,4,1,8691,2,8,1,3,6),_Ipv4DnsServer2IpAddr_Type())
ipv4DnsServer2IpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv4DnsServer2IpAddr.setStatus(_A)
_Ipv4PppoeUserAccount_Type=DisplayString
_Ipv4PppoeUserAccount_Object=MibScalar
ipv4PppoeUserAccount=_Ipv4PppoeUserAccount_Object((1,3,6,1,4,1,8691,2,8,1,3,7),_Ipv4PppoeUserAccount_Type())
ipv4PppoeUserAccount.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv4PppoeUserAccount.setStatus(_A)
_Ipv4PppoePassword_Type=DisplayString
_Ipv4PppoePassword_Object=MibScalar
ipv4PppoePassword=_Ipv4PppoePassword_Object((1,3,6,1,4,1,8691,2,8,1,3,8),_Ipv4PppoePassword_Type())
ipv4PppoePassword.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv4PppoePassword.setStatus(_A)
class _Ipv4WinsFunction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_Ipv4WinsFunction_Type.__name__=_C
_Ipv4WinsFunction_Object=MibScalar
ipv4WinsFunction=_Ipv4WinsFunction_Object((1,3,6,1,4,1,8691,2,8,1,3,9),_Ipv4WinsFunction_Type())
ipv4WinsFunction.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv4WinsFunction.setStatus(_A)
_Ipv4WinsServer_Type=IpAddress
_Ipv4WinsServer_Object=MibScalar
ipv4WinsServer=_Ipv4WinsServer_Object((1,3,6,1,4,1,8691,2,8,1,3,10),_Ipv4WinsServer_Type())
ipv4WinsServer.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv4WinsServer.setStatus(_A)
class _Lan1Speed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('auto-Negation',0),('tenMbps-Half',1),('tenMbps-Full',2),('hundredMbps-Half',3),('hundredMbps-Full',4)))
_Lan1Speed_Type.__name__=_C
_Lan1Speed_Object=MibScalar
lan1Speed=_Lan1Speed_Object((1,3,6,1,4,1,8691,2,8,1,3,11),_Lan1Speed_Type())
lan1Speed.setMaxAccess(_B)
if mibBuilder.loadTexts:lan1Speed.setStatus(_A)
class _RoutingProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('rip-1',1),('rip-2',2)))
_RoutingProtocol_Type.__name__=_C
_RoutingProtocol_Object=MibScalar
routingProtocol=_RoutingProtocol_Object((1,3,6,1,4,1,8691,2,8,1,3,12),_RoutingProtocol_Type())
routingProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:routingProtocol.setStatus(_A)
class _GratuitousArp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_GratuitousArp_Type.__name__=_C
_GratuitousArp_Object=MibScalar
gratuitousArp=_GratuitousArp_Object((1,3,6,1,4,1,8691,2,8,1,3,13),_GratuitousArp_Type())
gratuitousArp.setMaxAccess(_B)
if mibBuilder.loadTexts:gratuitousArp.setStatus(_A)
_GratuitousArpSendPeriod_Type=Integer32
_GratuitousArpSendPeriod_Object=MibScalar
gratuitousArpSendPeriod=_GratuitousArpSendPeriod_Object((1,3,6,1,4,1,8691,2,8,1,3,14),_GratuitousArpSendPeriod_Type())
gratuitousArpSendPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:gratuitousArpSendPeriod.setStatus(_A)
_ModuleSetting_ObjectIdentity=ObjectIdentity
moduleSetting=_ModuleSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,3,15))
_RedundancySetting_ObjectIdentity=ObjectIdentity
redundancySetting=_RedundancySetting_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,3,15,1))
class _RedundancyProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_a,1),(_b,2),(_c,3)))
_RedundancyProtocol_Type.__name__=_C
_RedundancyProtocol_Object=MibScalar
redundancyProtocol=_RedundancyProtocol_Object((1,3,6,1,4,1,8691,2,8,1,3,15,1,1),_RedundancyProtocol_Type())
redundancyProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:redundancyProtocol.setStatus(_A)
_SpanningTree_ObjectIdentity=ObjectIdentity
spanningTree=_SpanningTree_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,3,15,1,2))
class _SpanningTreeBridgePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4096,8192,12288,16384,20480,24576,28672,32768,36864,40960,45056,49152,53248,57344,61440)));namedValues=NamedValues(*((_k,0),('priority-4096',4096),('priority-8192',8192),('priority-12288',12288),('priority-16384',16384),('priority-20480',20480),('priority-24576',24576),('priority-28672',28672),('priority-32768',32768),('priority-36864',36864),('priority-40960',40960),('priority-45056',45056),('priority-49152',49152),('priority-53248',53248),('priority-57344',57344),('priority-61440',61440)))
_SpanningTreeBridgePriority_Type.__name__=_C
_SpanningTreeBridgePriority_Object=MibScalar
spanningTreeBridgePriority=_SpanningTreeBridgePriority_Object((1,3,6,1,4,1,8691,2,8,1,3,15,1,2,1),_SpanningTreeBridgePriority_Type())
spanningTreeBridgePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreeBridgePriority.setStatus(_A)
_SpanningTreeHelloTime_Type=Integer32
_SpanningTreeHelloTime_Object=MibScalar
spanningTreeHelloTime=_SpanningTreeHelloTime_Object((1,3,6,1,4,1,8691,2,8,1,3,15,1,2,2),_SpanningTreeHelloTime_Type())
spanningTreeHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreeHelloTime.setStatus(_A)
_SpanningTreeForwardingDelay_Type=Integer32
_SpanningTreeForwardingDelay_Object=MibScalar
spanningTreeForwardingDelay=_SpanningTreeForwardingDelay_Object((1,3,6,1,4,1,8691,2,8,1,3,15,1,2,3),_SpanningTreeForwardingDelay_Type())
spanningTreeForwardingDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreeForwardingDelay.setStatus(_A)
_SpanningTreeMaxAge_Type=Integer32
_SpanningTreeMaxAge_Object=MibScalar
spanningTreeMaxAge=_SpanningTreeMaxAge_Object((1,3,6,1,4,1,8691,2,8,1,3,15,1,2,4),_SpanningTreeMaxAge_Type())
spanningTreeMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreeMaxAge.setStatus(_A)
_SpanningTreePortTable_Object=MibTable
spanningTreePortTable=_SpanningTreePortTable_Object((1,3,6,1,4,1,8691,2,8,1,3,15,1,2,5))
if mibBuilder.loadTexts:spanningTreePortTable.setStatus(_A)
_SpanningTreePortEntry_Object=MibTableRow
spanningTreePortEntry=_SpanningTreePortEntry_Object((1,3,6,1,4,1,8691,2,8,1,3,15,1,2,5,1))
spanningTreePortEntry.setIndexNames((0,_H,_l))
if mibBuilder.loadTexts:spanningTreePortEntry.setStatus(_A)
_SpanningTreePortIndex_Type=Integer32
_SpanningTreePortIndex_Object=MibTableColumn
spanningTreePortIndex=_SpanningTreePortIndex_Object((1,3,6,1,4,1,8691,2,8,1,3,15,1,2,5,1,1),_SpanningTreePortIndex_Type())
spanningTreePortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:spanningTreePortIndex.setStatus(_A)
class _SpanningTreePortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SpanningTreePortEnable_Type.__name__=_C
_SpanningTreePortEnable_Object=MibTableColumn
spanningTreePortEnable=_SpanningTreePortEnable_Object((1,3,6,1,4,1,8691,2,8,1,3,15,1,2,5,1,2),_SpanningTreePortEnable_Type())
spanningTreePortEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreePortEnable.setStatus(_A)
class _SpanningTreePortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,16,32,48,64,80,96,112,128,144,160,176,192,208,224,240)));namedValues=NamedValues(*((_k,0),('priority-16',16),('priority-32',32),('priority-48',48),('priority-64',64),('priority-80',80),('priority-96',96),('priority-112',112),('priority-128',128),('priority-144',144),('priority-160',160),('priority-176',176),('priority-192',192),('priority-208',208),('priority-224',224),('priority-240',240)))
_SpanningTreePortPriority_Type.__name__=_C
_SpanningTreePortPriority_Object=MibTableColumn
spanningTreePortPriority=_SpanningTreePortPriority_Object((1,3,6,1,4,1,8691,2,8,1,3,15,1,2,5,1,3),_SpanningTreePortPriority_Type())
spanningTreePortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreePortPriority.setStatus(_A)
_SpanningTreePortCost_Type=Integer32
_SpanningTreePortCost_Object=MibTableColumn
spanningTreePortCost=_SpanningTreePortCost_Object((1,3,6,1,4,1,8691,2,8,1,3,15,1,2,5,1,4),_SpanningTreePortCost_Type())
spanningTreePortCost.setMaxAccess(_B)
if mibBuilder.loadTexts:spanningTreePortCost.setStatus(_A)
_TurboRing_ObjectIdentity=ObjectIdentity
turboRing=_TurboRing_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,3,15,1,3))
class _TurboRingMasterSetup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),(_d,1)))
_TurboRingMasterSetup_Type.__name__=_C
_TurboRingMasterSetup_Object=MibScalar
turboRingMasterSetup=_TurboRingMasterSetup_Object((1,3,6,1,4,1,8691,2,8,1,3,15,1,3,1),_TurboRingMasterSetup_Type())
turboRingMasterSetup.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingMasterSetup.setStatus(_A)
_TurboRingRdntPort1_Type=Integer32
_TurboRingRdntPort1_Object=MibScalar
turboRingRdntPort1=_TurboRingRdntPort1_Object((1,3,6,1,4,1,8691,2,8,1,3,15,1,3,2),_TurboRingRdntPort1_Type())
turboRingRdntPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingRdntPort1.setStatus(_A)
_TurboRingRdntPort2_Type=Integer32
_TurboRingRdntPort2_Object=MibScalar
turboRingRdntPort2=_TurboRingRdntPort2_Object((1,3,6,1,4,1,8691,2,8,1,3,15,1,3,3),_TurboRingRdntPort2_Type())
turboRingRdntPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingRdntPort2.setStatus(_A)
_TurboRingV2_ObjectIdentity=ObjectIdentity
turboRingV2=_TurboRingV2_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,3,15,1,4))
class _TurboRingV2MasterSetup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),(_d,1)))
_TurboRingV2MasterSetup_Type.__name__=_C
_TurboRingV2MasterSetup_Object=MibScalar
turboRingV2MasterSetup=_TurboRingV2MasterSetup_Object((1,3,6,1,4,1,8691,2,8,1,3,15,1,4,1),_TurboRingV2MasterSetup_Type())
turboRingV2MasterSetup.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingV2MasterSetup.setStatus(_A)
_TurboRingV2RdntPort1_Type=Integer32
_TurboRingV2RdntPort1_Object=MibScalar
turboRingV2RdntPort1=_TurboRingV2RdntPort1_Object((1,3,6,1,4,1,8691,2,8,1,3,15,1,4,2),_TurboRingV2RdntPort1_Type())
turboRingV2RdntPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingV2RdntPort1.setStatus(_A)
_TurboRingV2RdntPort2_Type=Integer32
_TurboRingV2RdntPort2_Object=MibScalar
turboRingV2RdntPort2=_TurboRingV2RdntPort2_Object((1,3,6,1,4,1,8691,2,8,1,3,15,1,4,3),_TurboRingV2RdntPort2_Type())
turboRingV2RdntPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:turboRingV2RdntPort2.setStatus(_A)
_GsmGprsSetting_ObjectIdentity=ObjectIdentity
gsmGprsSetting=_GsmGprsSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,3,15,2))
class _GsmGprsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('gsm',0),('gprs',1),('sms',2)))
_GsmGprsType_Type.__name__=_C
_GsmGprsType_Object=MibScalar
gsmGprsType=_GsmGprsType_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,1),_GsmGprsType_Type())
gsmGprsType.setMaxAccess(_B)
if mibBuilder.loadTexts:gsmGprsType.setStatus(_A)
_GsmGprsPIN_Type=DisplayString
_GsmGprsPIN_Object=MibScalar
gsmGprsPIN=_GsmGprsPIN_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,2),_GsmGprsPIN_Type())
gsmGprsPIN.setMaxAccess(_B)
if mibBuilder.loadTexts:gsmGprsPIN.setStatus(_A)
class _GsmGprsBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('band-850-Mhz',0),('band-900-Mhz',1),('band-1800-Mhz',2),('band-1900-Mhz',3),('band-850-1900-Mhz',4),('band-900-1800-Mhz',5),('band-900-1900-Mhz',6)))
_GsmGprsBand_Type.__name__=_C
_GsmGprsBand_Object=MibScalar
gsmGprsBand=_GsmGprsBand_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,3),_GsmGprsBand_Type())
gsmGprsBand.setMaxAccess(_B)
if mibBuilder.loadTexts:gsmGprsBand.setStatus(_A)
_GsmSetting_ObjectIdentity=ObjectIdentity
gsmSetting=_GsmSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,3,15,2,4))
class _GsmMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_e,0),(_f,1)))
_GsmMode_Type.__name__=_C
_GsmMode_Object=MibScalar
gsmMode=_GsmMode_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,4,1),_GsmMode_Type())
gsmMode.setMaxAccess(_B)
if mibBuilder.loadTexts:gsmMode.setStatus(_A)
_GsmDestinationIpAddress_Type=IpAddress
_GsmDestinationIpAddress_Object=MibScalar
gsmDestinationIpAddress=_GsmDestinationIpAddress_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,4,2),_GsmDestinationIpAddress_Type())
gsmDestinationIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gsmDestinationIpAddress.setStatus(_A)
_GsmSourceIpAddress_Type=IpAddress
_GsmSourceIpAddress_Object=MibScalar
gsmSourceIpAddress=_GsmSourceIpAddress_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,4,3),_GsmSourceIpAddress_Type())
gsmSourceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:gsmSourceIpAddress.setStatus(_A)
_GsmIpNetmask_Type=IpAddress
_GsmIpNetmask_Object=MibScalar
gsmIpNetmask=_GsmIpNetmask_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,4,4),_GsmIpNetmask_Type())
gsmIpNetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:gsmIpNetmask.setStatus(_A)
class _GsmTcpIpCompression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_GsmTcpIpCompression_Type.__name__=_C
_GsmTcpIpCompression_Object=MibScalar
gsmTcpIpCompression=_GsmTcpIpCompression_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,4,5),_GsmTcpIpCompression_Type())
gsmTcpIpCompression.setMaxAccess(_B)
if mibBuilder.loadTexts:gsmTcpIpCompression.setStatus(_A)
_GsmInactivityTime_Type=Integer32
_GsmInactivityTime_Object=MibScalar
gsmInactivityTime=_GsmInactivityTime_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,4,6),_GsmInactivityTime_Type())
gsmInactivityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:gsmInactivityTime.setStatus(_A)
class _GsmLinkQualityReport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_GsmLinkQualityReport_Type.__name__=_C
_GsmLinkQualityReport_Object=MibScalar
gsmLinkQualityReport=_GsmLinkQualityReport_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,4,7),_GsmLinkQualityReport_Type())
gsmLinkQualityReport.setMaxAccess(_B)
if mibBuilder.loadTexts:gsmLinkQualityReport.setStatus(_A)
class _GsmUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_GsmUsername_Type.__name__=_F
_GsmUsername_Object=MibScalar
gsmUsername=_GsmUsername_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,4,8),_GsmUsername_Type())
gsmUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:gsmUsername.setStatus(_A)
class _GsmPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_GsmPassword_Type.__name__=_F
_GsmPassword_Object=MibScalar
gsmPassword=_GsmPassword_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,4,9),_GsmPassword_Type())
gsmPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:gsmPassword.setStatus(_A)
class _GsmAuthenticationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_J,0),(_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6),(_T,7)))
_GsmAuthenticationType_Type.__name__=_C
_GsmAuthenticationType_Object=MibScalar
gsmAuthenticationType=_GsmAuthenticationType_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,4,10),_GsmAuthenticationType_Type())
gsmAuthenticationType.setMaxAccess(_B)
if mibBuilder.loadTexts:gsmAuthenticationType.setStatus(_A)
class _GsmTryNextAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_GsmTryNextAuth_Type.__name__=_C
_GsmTryNextAuth_Object=MibScalar
gsmTryNextAuth=_GsmTryNextAuth_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,4,11),_GsmTryNextAuth_Type())
gsmTryNextAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:gsmTryNextAuth.setStatus(_A)
class _GsmOutPhoneNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_GsmOutPhoneNumber_Type.__name__=_F
_GsmOutPhoneNumber_Object=MibScalar
gsmOutPhoneNumber=_GsmOutPhoneNumber_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,4,12),_GsmOutPhoneNumber_Type())
gsmOutPhoneNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:gsmOutPhoneNumber.setStatus(_A)
class _GsmInitialString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_GsmInitialString_Type.__name__=_F
_GsmInitialString_Object=MibScalar
gsmInitialString=_GsmInitialString_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,4,13),_GsmInitialString_Type())
gsmInitialString.setMaxAccess(_B)
if mibBuilder.loadTexts:gsmInitialString.setStatus(_A)
class _GsmConnectionControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_g,0),(_h,1),(_i,2)))
_GsmConnectionControl_Type.__name__=_C
_GsmConnectionControl_Object=MibScalar
gsmConnectionControl=_GsmConnectionControl_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,4,14),_GsmConnectionControl_Type())
gsmConnectionControl.setMaxAccess(_B)
if mibBuilder.loadTexts:gsmConnectionControl.setStatus(_A)
_GsmConnectionInterval_Type=Integer32
_GsmConnectionInterval_Object=MibScalar
gsmConnectionInterval=_GsmConnectionInterval_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,4,15),_GsmConnectionInterval_Type())
gsmConnectionInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:gsmConnectionInterval.setStatus(_A)
class _GsmPingRemoteHost_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_GsmPingRemoteHost_Type.__name__=_F
_GsmPingRemoteHost_Object=MibScalar
gsmPingRemoteHost=_GsmPingRemoteHost_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,4,16),_GsmPingRemoteHost_Type())
gsmPingRemoteHost.setMaxAccess(_B)
if mibBuilder.loadTexts:gsmPingRemoteHost.setStatus(_A)
class _GsmInPhoneNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_GsmInPhoneNumber_Type.__name__=_F
_GsmInPhoneNumber_Object=MibScalar
gsmInPhoneNumber=_GsmInPhoneNumber_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,4,17),_GsmInPhoneNumber_Type())
gsmInPhoneNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:gsmInPhoneNumber.setStatus(_A)
_GprsSetting_ObjectIdentity=ObjectIdentity
gprsSetting=_GprsSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,3,15,2,5))
class _GprsTcpIpCompression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_GprsTcpIpCompression_Type.__name__=_C
_GprsTcpIpCompression_Object=MibScalar
gprsTcpIpCompression=_GprsTcpIpCompression_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,5,1),_GprsTcpIpCompression_Type())
gprsTcpIpCompression.setMaxAccess(_B)
if mibBuilder.loadTexts:gprsTcpIpCompression.setStatus(_A)
_GprsInactivityTime_Type=Integer32
_GprsInactivityTime_Object=MibScalar
gprsInactivityTime=_GprsInactivityTime_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,5,2),_GprsInactivityTime_Type())
gprsInactivityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:gprsInactivityTime.setStatus(_A)
class _GprsLinkQualityReport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_GprsLinkQualityReport_Type.__name__=_C
_GprsLinkQualityReport_Object=MibScalar
gprsLinkQualityReport=_GprsLinkQualityReport_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,5,3),_GprsLinkQualityReport_Type())
gprsLinkQualityReport.setMaxAccess(_B)
if mibBuilder.loadTexts:gprsLinkQualityReport.setStatus(_A)
class _GprsInitialString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_GprsInitialString_Type.__name__=_F
_GprsInitialString_Object=MibScalar
gprsInitialString=_GprsInitialString_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,5,4),_GprsInitialString_Type())
gprsInitialString.setMaxAccess(_B)
if mibBuilder.loadTexts:gprsInitialString.setStatus(_A)
class _GprsUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_GprsUsername_Type.__name__=_F
_GprsUsername_Object=MibScalar
gprsUsername=_GprsUsername_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,5,5),_GprsUsername_Type())
gprsUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:gprsUsername.setStatus(_A)
class _GprsPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_GprsPassword_Type.__name__=_F
_GprsPassword_Object=MibScalar
gprsPassword=_GprsPassword_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,5,6),_GprsPassword_Type())
gprsPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:gprsPassword.setStatus(_A)
class _GprsAPN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_GprsAPN_Type.__name__=_F
_GprsAPN_Object=MibScalar
gprsAPN=_GprsAPN_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,5,7),_GprsAPN_Type())
gprsAPN.setMaxAccess(_B)
if mibBuilder.loadTexts:gprsAPN.setStatus(_A)
class _GprsConnectionControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_g,0),(_h,1),(_i,2)))
_GprsConnectionControl_Type.__name__=_C
_GprsConnectionControl_Object=MibScalar
gprsConnectionControl=_GprsConnectionControl_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,5,8),_GprsConnectionControl_Type())
gprsConnectionControl.setMaxAccess(_B)
if mibBuilder.loadTexts:gprsConnectionControl.setStatus(_A)
_GprsConnectionInterval_Type=Integer32
_GprsConnectionInterval_Object=MibScalar
gprsConnectionInterval=_GprsConnectionInterval_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,5,9),_GprsConnectionInterval_Type())
gprsConnectionInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:gprsConnectionInterval.setStatus(_A)
class _GprsPingRemoteHost_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_GprsPingRemoteHost_Type.__name__=_F
_GprsPingRemoteHost_Object=MibScalar
gprsPingRemoteHost=_GprsPingRemoteHost_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,5,10),_GprsPingRemoteHost_Type())
gprsPingRemoteHost.setMaxAccess(_B)
if mibBuilder.loadTexts:gprsPingRemoteHost.setStatus(_A)
_SmsSetting_ObjectIdentity=ObjectIdentity
smsSetting=_SmsSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,3,15,2,6))
class _SmsFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('sms-Text-ASCII',0))
_SmsFormat_Type.__name__=_C
_SmsFormat_Object=MibScalar
smsFormat=_SmsFormat_Object((1,3,6,1,4,1,8691,2,8,1,3,15,2,6,1),_SmsFormat_Type())
smsFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:smsFormat.setStatus(_A)
_V92ModemSetting_ObjectIdentity=ObjectIdentity
v92ModemSetting=_V92ModemSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,3,15,3))
class _V92ModemMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_e,0),(_f,1)))
_V92ModemMode_Type.__name__=_C
_V92ModemMode_Object=MibScalar
v92ModemMode=_V92ModemMode_Object((1,3,6,1,4,1,8691,2,8,1,3,15,3,1),_V92ModemMode_Type())
v92ModemMode.setMaxAccess(_B)
if mibBuilder.loadTexts:v92ModemMode.setStatus(_A)
_V92ModemDestinationIpAddress_Type=IpAddress
_V92ModemDestinationIpAddress_Object=MibScalar
v92ModemDestinationIpAddress=_V92ModemDestinationIpAddress_Object((1,3,6,1,4,1,8691,2,8,1,3,15,3,2),_V92ModemDestinationIpAddress_Type())
v92ModemDestinationIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:v92ModemDestinationIpAddress.setStatus(_A)
_V92ModemSourceIpAddress_Type=IpAddress
_V92ModemSourceIpAddress_Object=MibScalar
v92ModemSourceIpAddress=_V92ModemSourceIpAddress_Object((1,3,6,1,4,1,8691,2,8,1,3,15,3,3),_V92ModemSourceIpAddress_Type())
v92ModemSourceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:v92ModemSourceIpAddress.setStatus(_A)
_V92ModemIpNetmask_Type=IpAddress
_V92ModemIpNetmask_Object=MibScalar
v92ModemIpNetmask=_V92ModemIpNetmask_Object((1,3,6,1,4,1,8691,2,8,1,3,15,3,4),_V92ModemIpNetmask_Type())
v92ModemIpNetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:v92ModemIpNetmask.setStatus(_A)
class _V92ModemTcpIpCompression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_V92ModemTcpIpCompression_Type.__name__=_C
_V92ModemTcpIpCompression_Object=MibScalar
v92ModemTcpIpCompression=_V92ModemTcpIpCompression_Object((1,3,6,1,4,1,8691,2,8,1,3,15,3,5),_V92ModemTcpIpCompression_Type())
v92ModemTcpIpCompression.setMaxAccess(_B)
if mibBuilder.loadTexts:v92ModemTcpIpCompression.setStatus(_A)
_V92ModemInactivityTime_Type=Integer32
_V92ModemInactivityTime_Object=MibScalar
v92ModemInactivityTime=_V92ModemInactivityTime_Object((1,3,6,1,4,1,8691,2,8,1,3,15,3,6),_V92ModemInactivityTime_Type())
v92ModemInactivityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:v92ModemInactivityTime.setStatus(_A)
class _V92ModemLinkQualityReport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_V92ModemLinkQualityReport_Type.__name__=_C
_V92ModemLinkQualityReport_Object=MibScalar
v92ModemLinkQualityReport=_V92ModemLinkQualityReport_Object((1,3,6,1,4,1,8691,2,8,1,3,15,3,7),_V92ModemLinkQualityReport_Type())
v92ModemLinkQualityReport.setMaxAccess(_B)
if mibBuilder.loadTexts:v92ModemLinkQualityReport.setStatus(_A)
class _V92ModemUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_V92ModemUsername_Type.__name__=_F
_V92ModemUsername_Object=MibScalar
v92ModemUsername=_V92ModemUsername_Object((1,3,6,1,4,1,8691,2,8,1,3,15,3,8),_V92ModemUsername_Type())
v92ModemUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:v92ModemUsername.setStatus(_A)
class _V92ModemPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_V92ModemPassword_Type.__name__=_F
_V92ModemPassword_Object=MibScalar
v92ModemPassword=_V92ModemPassword_Object((1,3,6,1,4,1,8691,2,8,1,3,15,3,9),_V92ModemPassword_Type())
v92ModemPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:v92ModemPassword.setStatus(_A)
class _V92ModemIncomingPAPCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_J,0),(_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6),(_T,7)))
_V92ModemIncomingPAPCheck_Type.__name__=_C
_V92ModemIncomingPAPCheck_Object=MibScalar
v92ModemIncomingPAPCheck=_V92ModemIncomingPAPCheck_Object((1,3,6,1,4,1,8691,2,8,1,3,15,3,10),_V92ModemIncomingPAPCheck_Type())
v92ModemIncomingPAPCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:v92ModemIncomingPAPCheck.setStatus(_A)
class _V92ModemIncomingTryNextAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_V92ModemIncomingTryNextAuth_Type.__name__=_C
_V92ModemIncomingTryNextAuth_Object=MibScalar
v92ModemIncomingTryNextAuth=_V92ModemIncomingTryNextAuth_Object((1,3,6,1,4,1,8691,2,8,1,3,15,3,11),_V92ModemIncomingTryNextAuth_Type())
v92ModemIncomingTryNextAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:v92ModemIncomingTryNextAuth.setStatus(_A)
class _V92ModemPhoneNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_V92ModemPhoneNumber_Type.__name__=_F
_V92ModemPhoneNumber_Object=MibScalar
v92ModemPhoneNumber=_V92ModemPhoneNumber_Object((1,3,6,1,4,1,8691,2,8,1,3,15,3,12),_V92ModemPhoneNumber_Type())
v92ModemPhoneNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:v92ModemPhoneNumber.setStatus(_A)
class _V92ModemInitialString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_V92ModemInitialString_Type.__name__=_F
_V92ModemInitialString_Object=MibScalar
v92ModemInitialString=_V92ModemInitialString_Object((1,3,6,1,4,1,8691,2,8,1,3,15,3,13),_V92ModemInitialString_Type())
v92ModemInitialString.setMaxAccess(_B)
if mibBuilder.loadTexts:v92ModemInitialString.setStatus(_A)
class _V92ModemConnectionControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_g,0),(_h,1),(_i,2)))
_V92ModemConnectionControl_Type.__name__=_C
_V92ModemConnectionControl_Object=MibScalar
v92ModemConnectionControl=_V92ModemConnectionControl_Object((1,3,6,1,4,1,8691,2,8,1,3,15,3,14),_V92ModemConnectionControl_Type())
v92ModemConnectionControl.setMaxAccess(_B)
if mibBuilder.loadTexts:v92ModemConnectionControl.setStatus(_A)
_V92ModemConnectionInterval_Type=Integer32
_V92ModemConnectionInterval_Object=MibScalar
v92ModemConnectionInterval=_V92ModemConnectionInterval_Object((1,3,6,1,4,1,8691,2,8,1,3,15,3,15),_V92ModemConnectionInterval_Type())
v92ModemConnectionInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:v92ModemConnectionInterval.setStatus(_A)
class _V92ModemPingRemoteHost_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_V92ModemPingRemoteHost_Type.__name__=_F
_V92ModemPingRemoteHost_Object=MibScalar
v92ModemPingRemoteHost=_V92ModemPingRemoteHost_Object((1,3,6,1,4,1,8691,2,8,1,3,15,3,16),_V92ModemPingRemoteHost_Type())
v92ModemPingRemoteHost.setMaxAccess(_B)
if mibBuilder.loadTexts:v92ModemPingRemoteHost.setStatus(_A)
class _Ipv6Configuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('auto',0),(_j,1),(_D,2)))
_Ipv6Configuration_Type.__name__=_C
_Ipv6Configuration_Object=MibScalar
ipv6Configuration=_Ipv6Configuration_Object((1,3,6,1,4,1,8691,2,8,1,3,16),_Ipv6Configuration_Type())
ipv6Configuration.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv6Configuration.setStatus(_A)
class _Ipv6Address_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Ipv6Address_Type.__name__=_F
_Ipv6Address_Object=MibScalar
ipv6Address=_Ipv6Address_Object((1,3,6,1,4,1,8691,2,8,1,3,17),_Ipv6Address_Type())
ipv6Address.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv6Address.setStatus(_A)
_Ipv6Prefix_Type=Integer32
_Ipv6Prefix_Object=MibScalar
ipv6Prefix=_Ipv6Prefix_Object((1,3,6,1,4,1,8691,2,8,1,3,18),_Ipv6Prefix_Type())
ipv6Prefix.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv6Prefix.setStatus(_A)
class _Ipv6DefaultGateway_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Ipv6DefaultGateway_Type.__name__=_F
_Ipv6DefaultGateway_Object=MibScalar
ipv6DefaultGateway=_Ipv6DefaultGateway_Object((1,3,6,1,4,1,8691,2,8,1,3,19),_Ipv6DefaultGateway_Type())
ipv6DefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv6DefaultGateway.setStatus(_A)
class _Ipv6DnsServer1IpAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Ipv6DnsServer1IpAddr_Type.__name__=_F
_Ipv6DnsServer1IpAddr_Object=MibScalar
ipv6DnsServer1IpAddr=_Ipv6DnsServer1IpAddr_Object((1,3,6,1,4,1,8691,2,8,1,3,20),_Ipv6DnsServer1IpAddr_Type())
ipv6DnsServer1IpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv6DnsServer1IpAddr.setStatus(_A)
class _Ipv6DnsServer2IpAddr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Ipv6DnsServer2IpAddr_Type.__name__=_F
_Ipv6DnsServer2IpAddr_Object=MibScalar
ipv6DnsServer2IpAddr=_Ipv6DnsServer2IpAddr_Object((1,3,6,1,4,1,8691,2,8,1,3,21),_Ipv6DnsServer2IpAddr_Type())
ipv6DnsServer2IpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv6DnsServer2IpAddr.setStatus(_A)
class _ConnectionPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ipv6-first',0),('ipv4-first',1)))
_ConnectionPriority_Type.__name__=_C
_ConnectionPriority_Object=MibScalar
connectionPriority=_ConnectionPriority_Object((1,3,6,1,4,1,8691,2,8,1,3,22),_ConnectionPriority_Type())
connectionPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:connectionPriority.setStatus(_A)
_PortSetting_ObjectIdentity=ObjectIdentity
portSetting=_PortSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,4))
_OpModeSetting_ObjectIdentity=ObjectIdentity
opModeSetting=_OpModeSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,4,1))
_OpMode_ObjectIdentity=ObjectIdentity
opMode=_OpMode_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,4,1,1))
_OpModePortTable_Object=MibTable
opModePortTable=_OpModePortTable_Object((1,3,6,1,4,1,8691,2,8,1,4,1,1,1))
if mibBuilder.loadTexts:opModePortTable.setStatus(_A)
_OpModePortEntry_Object=MibTableRow
opModePortEntry=_OpModePortEntry_Object((1,3,6,1,4,1,8691,2,8,1,4,1,1,1,1))
opModePortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:opModePortEntry.setStatus(_A)
_PortIndex_Type=Integer32
_PortIndex_Object=MibTableColumn
portIndex=_PortIndex_Object((1,3,6,1,4,1,8691,2,8,1,4,1,1,1,1,1),_PortIndex_Type())
portIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
class _PortApplication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,6,11,12,13)));namedValues=NamedValues(*((_D,0),('dial-InOut',1),(_m,2),('reverse-Terminal',3),('device-Control',4),(_n,6),(_o,11),(_p,12),('pair-Connection',13)))
_PortApplication_Type.__name__=_C
_PortApplication_Object=MibTableColumn
portApplication=_PortApplication_Object((1,3,6,1,4,1,8691,2,8,1,4,1,1,1,1,2),_PortApplication_Type())
portApplication.setMaxAccess(_B)
if mibBuilder.loadTexts:portApplication.setStatus(_A)
class _PortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)));namedValues=NamedValues(*(('pair-Slave',0),('pair-Master',1),('real-Com',2),('raw-PRN',3),('slip',4),('slipd',5),(_e,6),(_D,7),('reverse-Telnet',8),('dynamic',9),('tcp-Server',10),('lpd-PRN',11),(_p,12),('tcp-Client',13),('udp',14),(_f,15),('term-ASC',16),('term-BIN',17),('reverse-SSH',18),('ssh',19),('rfc-2217',20),('reverse-Real-Com',21)))
_PortMode_Type.__name__=_C
_PortMode_Object=MibTableColumn
portMode=_PortMode_Object((1,3,6,1,4,1,8691,2,8,1,4,1,1,1,1,3),_PortMode_Type())
portMode.setMaxAccess(_B)
if mibBuilder.loadTexts:portMode.setStatus(_A)
_Application_ObjectIdentity=ObjectIdentity
application=_Application_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,4,1,2))
_DeviceControl_ObjectIdentity=ObjectIdentity
deviceControl=_DeviceControl_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,4,1,2,1))
_DeviceControlTable_Object=MibTable
deviceControlTable=_DeviceControlTable_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1))
if mibBuilder.loadTexts:deviceControlTable.setStatus(_A)
_DeviceControlEntry_Object=MibTableRow
deviceControlEntry=_DeviceControlEntry_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1,1))
deviceControlEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:deviceControlEntry.setStatus(_A)
_DeviceControlTcpAliveCheck_Type=Integer32
_DeviceControlTcpAliveCheck_Object=MibTableColumn
deviceControlTcpAliveCheck=_DeviceControlTcpAliveCheck_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1,1,1),_DeviceControlTcpAliveCheck_Type())
deviceControlTcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceControlTcpAliveCheck.setStatus(_A)
_DeviceControlMaxConnection_Type=Integer32
_DeviceControlMaxConnection_Object=MibTableColumn
deviceControlMaxConnection=_DeviceControlMaxConnection_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1,1,2),_DeviceControlMaxConnection_Type())
deviceControlMaxConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceControlMaxConnection.setStatus(_A)
class _DeviceControlIgnoreJammedIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DeviceControlIgnoreJammedIp_Type.__name__=_C
_DeviceControlIgnoreJammedIp_Object=MibTableColumn
deviceControlIgnoreJammedIp=_DeviceControlIgnoreJammedIp_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1,1,3),_DeviceControlIgnoreJammedIp_Type())
deviceControlIgnoreJammedIp.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceControlIgnoreJammedIp.setStatus(_A)
class _DeviceControlAllowDriverControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DeviceControlAllowDriverControl_Type.__name__=_C
_DeviceControlAllowDriverControl_Object=MibTableColumn
deviceControlAllowDriverControl=_DeviceControlAllowDriverControl_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1,1,4),_DeviceControlAllowDriverControl_Type())
deviceControlAllowDriverControl.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceControlAllowDriverControl.setStatus(_A)
class _DeviceControlCommandByCommandOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DeviceControlCommandByCommandOperation_Type.__name__=_C
_DeviceControlCommandByCommandOperation_Object=MibTableColumn
deviceControlCommandByCommandOperation=_DeviceControlCommandByCommandOperation_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1,1,5),_DeviceControlCommandByCommandOperation_Type())
deviceControlCommandByCommandOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceControlCommandByCommandOperation.setStatus(_A)
class _DeviceControlSecure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DeviceControlSecure_Type.__name__=_C
_DeviceControlSecure_Object=MibTableColumn
deviceControlSecure=_DeviceControlSecure_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1,1,6),_DeviceControlSecure_Type())
deviceControlSecure.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceControlSecure.setStatus(_A)
class _DeviceControlConnectionDownRTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Y,0),(_Z,1)))
_DeviceControlConnectionDownRTS_Type.__name__=_C
_DeviceControlConnectionDownRTS_Object=MibTableColumn
deviceControlConnectionDownRTS=_DeviceControlConnectionDownRTS_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1,1,7),_DeviceControlConnectionDownRTS_Type())
deviceControlConnectionDownRTS.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceControlConnectionDownRTS.setStatus(_A)
class _DeviceControlConnectionDownDTR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Y,0),(_Z,1)))
_DeviceControlConnectionDownDTR_Type.__name__=_C
_DeviceControlConnectionDownDTR_Object=MibTableColumn
deviceControlConnectionDownDTR=_DeviceControlConnectionDownDTR_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1,1,8),_DeviceControlConnectionDownDTR_Type())
deviceControlConnectionDownDTR.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceControlConnectionDownDTR.setStatus(_A)
_DeviceControlResponseTimeout_Type=Integer32
_DeviceControlResponseTimeout_Object=MibTableColumn
deviceControlResponseTimeout=_DeviceControlResponseTimeout_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1,1,9),_DeviceControlResponseTimeout_Type())
deviceControlResponseTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceControlResponseTimeout.setStatus(_A)
class _DeviceControlNonRequestSerialData_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_q,0),(_r,1),(_s,2)))
_DeviceControlNonRequestSerialData_Type.__name__=_C
_DeviceControlNonRequestSerialData_Object=MibTableColumn
deviceControlNonRequestSerialData=_DeviceControlNonRequestSerialData_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1,1,10),_DeviceControlNonRequestSerialData_Type())
deviceControlNonRequestSerialData.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceControlNonRequestSerialData.setStatus(_A)
_DeviceControlTcpPort_Type=Integer32
_DeviceControlTcpPort_Object=MibTableColumn
deviceControlTcpPort=_DeviceControlTcpPort_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1,1,11),_DeviceControlTcpPort_Type())
deviceControlTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceControlTcpPort.setStatus(_A)
class _DeviceControlDestinationAddress1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_DeviceControlDestinationAddress1_Type.__name__=_F
_DeviceControlDestinationAddress1_Object=MibTableColumn
deviceControlDestinationAddress1=_DeviceControlDestinationAddress1_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1,1,12),_DeviceControlDestinationAddress1_Type())
deviceControlDestinationAddress1.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceControlDestinationAddress1.setStatus(_A)
_DeviceControlDestinationTcpPort1_Type=Integer32
_DeviceControlDestinationTcpPort1_Object=MibTableColumn
deviceControlDestinationTcpPort1=_DeviceControlDestinationTcpPort1_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1,1,13),_DeviceControlDestinationTcpPort1_Type())
deviceControlDestinationTcpPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceControlDestinationTcpPort1.setStatus(_A)
_DeviceControlDestinationCmdPort1_Type=Integer32
_DeviceControlDestinationCmdPort1_Object=MibTableColumn
deviceControlDestinationCmdPort1=_DeviceControlDestinationCmdPort1_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1,1,14),_DeviceControlDestinationCmdPort1_Type())
deviceControlDestinationCmdPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceControlDestinationCmdPort1.setStatus(_A)
class _DeviceControlDestinationAddress2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_DeviceControlDestinationAddress2_Type.__name__=_F
_DeviceControlDestinationAddress2_Object=MibTableColumn
deviceControlDestinationAddress2=_DeviceControlDestinationAddress2_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1,1,15),_DeviceControlDestinationAddress2_Type())
deviceControlDestinationAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceControlDestinationAddress2.setStatus(_A)
_DeviceControlDestinationTcpPort2_Type=Integer32
_DeviceControlDestinationTcpPort2_Object=MibTableColumn
deviceControlDestinationTcpPort2=_DeviceControlDestinationTcpPort2_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1,1,16),_DeviceControlDestinationTcpPort2_Type())
deviceControlDestinationTcpPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceControlDestinationTcpPort2.setStatus(_A)
_DeviceControlDestinationCmdPort2_Type=Integer32
_DeviceControlDestinationCmdPort2_Object=MibTableColumn
deviceControlDestinationCmdPort2=_DeviceControlDestinationCmdPort2_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1,1,17),_DeviceControlDestinationCmdPort2_Type())
deviceControlDestinationCmdPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceControlDestinationCmdPort2.setStatus(_A)
_DeviceControlDesignatedLocalTcpPort1_Type=Integer32
_DeviceControlDesignatedLocalTcpPort1_Object=MibTableColumn
deviceControlDesignatedLocalTcpPort1=_DeviceControlDesignatedLocalTcpPort1_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1,1,18),_DeviceControlDesignatedLocalTcpPort1_Type())
deviceControlDesignatedLocalTcpPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceControlDesignatedLocalTcpPort1.setStatus(_A)
_DeviceControlDesignatedLocalCmdPort1_Type=Integer32
_DeviceControlDesignatedLocalCmdPort1_Object=MibTableColumn
deviceControlDesignatedLocalCmdPort1=_DeviceControlDesignatedLocalCmdPort1_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1,1,19),_DeviceControlDesignatedLocalCmdPort1_Type())
deviceControlDesignatedLocalCmdPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceControlDesignatedLocalCmdPort1.setStatus(_A)
_DeviceControlDesignatedLocalTcpPort2_Type=Integer32
_DeviceControlDesignatedLocalTcpPort2_Object=MibTableColumn
deviceControlDesignatedLocalTcpPort2=_DeviceControlDesignatedLocalTcpPort2_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1,1,20),_DeviceControlDesignatedLocalTcpPort2_Type())
deviceControlDesignatedLocalTcpPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceControlDesignatedLocalTcpPort2.setStatus(_A)
_DeviceControlDesignatedLocalCmdPort2_Type=Integer32
_DeviceControlDesignatedLocalCmdPort2_Object=MibTableColumn
deviceControlDesignatedLocalCmdPort2=_DeviceControlDesignatedLocalCmdPort2_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,1,1,1,21),_DeviceControlDesignatedLocalCmdPort2_Type())
deviceControlDesignatedLocalCmdPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceControlDesignatedLocalCmdPort2.setStatus(_A)
_Socket_ObjectIdentity=ObjectIdentity
socket=_Socket_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,4,1,2,2))
_SocketTable_Object=MibTable
socketTable=_SocketTable_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1))
if mibBuilder.loadTexts:socketTable.setStatus(_A)
_SocketEntry_Object=MibTableRow
socketEntry=_SocketEntry_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1))
socketEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:socketEntry.setStatus(_A)
_SocketTcpAliveCheck_Type=Integer32
_SocketTcpAliveCheck_Object=MibTableColumn
socketTcpAliveCheck=_SocketTcpAliveCheck_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,1),_SocketTcpAliveCheck_Type())
socketTcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:socketTcpAliveCheck.setStatus(_A)
_SocketInactivityTime_Type=Integer32
_SocketInactivityTime_Object=MibTableColumn
socketInactivityTime=_SocketInactivityTime_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,2),_SocketInactivityTime_Type())
socketInactivityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:socketInactivityTime.setStatus(_A)
_SocketMaxConnection_Type=Integer32
_SocketMaxConnection_Object=MibTableColumn
socketMaxConnection=_SocketMaxConnection_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,3),_SocketMaxConnection_Type())
socketMaxConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:socketMaxConnection.setStatus(_A)
class _SocketIgnoreJammedIp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SocketIgnoreJammedIp_Type.__name__=_C
_SocketIgnoreJammedIp_Object=MibTableColumn
socketIgnoreJammedIp=_SocketIgnoreJammedIp_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,4),_SocketIgnoreJammedIp_Type())
socketIgnoreJammedIp.setMaxAccess(_B)
if mibBuilder.loadTexts:socketIgnoreJammedIp.setStatus(_A)
class _SocketAllowDriverControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SocketAllowDriverControl_Type.__name__=_C
_SocketAllowDriverControl_Object=MibTableColumn
socketAllowDriverControl=_SocketAllowDriverControl_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,5),_SocketAllowDriverControl_Type())
socketAllowDriverControl.setMaxAccess(_B)
if mibBuilder.loadTexts:socketAllowDriverControl.setStatus(_A)
class _SocketCommandByCommandOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SocketCommandByCommandOperation_Type.__name__=_C
_SocketCommandByCommandOperation_Object=MibTableColumn
socketCommandByCommandOperation=_SocketCommandByCommandOperation_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,6),_SocketCommandByCommandOperation_Type())
socketCommandByCommandOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:socketCommandByCommandOperation.setStatus(_A)
class _SocketSecure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SocketSecure_Type.__name__=_C
_SocketSecure_Object=MibTableColumn
socketSecure=_SocketSecure_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,7),_SocketSecure_Type())
socketSecure.setMaxAccess(_B)
if mibBuilder.loadTexts:socketSecure.setStatus(_A)
_SocketTcpPort_Type=Integer32
_SocketTcpPort_Object=MibTableColumn
socketTcpPort=_SocketTcpPort_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,8),_SocketTcpPort_Type())
socketTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:socketTcpPort.setStatus(_A)
_SocketCmdPort_Type=Integer32
_SocketCmdPort_Object=MibTableColumn
socketCmdPort=_SocketCmdPort_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,9),_SocketCmdPort_Type())
socketCmdPort.setMaxAccess(_B)
if mibBuilder.loadTexts:socketCmdPort.setStatus(_A)
class _SocketTcpServerConnectionDownRTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Y,0),(_Z,1)))
_SocketTcpServerConnectionDownRTS_Type.__name__=_C
_SocketTcpServerConnectionDownRTS_Object=MibTableColumn
socketTcpServerConnectionDownRTS=_SocketTcpServerConnectionDownRTS_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,10),_SocketTcpServerConnectionDownRTS_Type())
socketTcpServerConnectionDownRTS.setMaxAccess(_B)
if mibBuilder.loadTexts:socketTcpServerConnectionDownRTS.setStatus(_A)
class _SocketTcpServerConnectionDownDTR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Y,0),(_Z,1)))
_SocketTcpServerConnectionDownDTR_Type.__name__=_C
_SocketTcpServerConnectionDownDTR_Object=MibTableColumn
socketTcpServerConnectionDownDTR=_SocketTcpServerConnectionDownDTR_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,11),_SocketTcpServerConnectionDownDTR_Type())
socketTcpServerConnectionDownDTR.setMaxAccess(_B)
if mibBuilder.loadTexts:socketTcpServerConnectionDownDTR.setStatus(_A)
_SocketResponseTimeout_Type=Integer32
_SocketResponseTimeout_Object=MibTableColumn
socketResponseTimeout=_SocketResponseTimeout_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,12),_SocketResponseTimeout_Type())
socketResponseTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:socketResponseTimeout.setStatus(_A)
class _SocketNonRequestSerialData_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_q,0),(_r,1),(_s,2)))
_SocketNonRequestSerialData_Type.__name__=_C
_SocketNonRequestSerialData_Object=MibTableColumn
socketNonRequestSerialData=_SocketNonRequestSerialData_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,13),_SocketNonRequestSerialData_Type())
socketNonRequestSerialData.setMaxAccess(_B)
if mibBuilder.loadTexts:socketNonRequestSerialData.setStatus(_A)
class _SocketTcpClientDestinationAddress1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SocketTcpClientDestinationAddress1_Type.__name__=_F
_SocketTcpClientDestinationAddress1_Object=MibTableColumn
socketTcpClientDestinationAddress1=_SocketTcpClientDestinationAddress1_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,14),_SocketTcpClientDestinationAddress1_Type())
socketTcpClientDestinationAddress1.setMaxAccess(_B)
if mibBuilder.loadTexts:socketTcpClientDestinationAddress1.setStatus(_A)
_SocketTcpClientDestinationPort1_Type=Integer32
_SocketTcpClientDestinationPort1_Object=MibTableColumn
socketTcpClientDestinationPort1=_SocketTcpClientDestinationPort1_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,15),_SocketTcpClientDestinationPort1_Type())
socketTcpClientDestinationPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:socketTcpClientDestinationPort1.setStatus(_A)
class _SocketTcpClientDestinationAddress2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SocketTcpClientDestinationAddress2_Type.__name__=_F
_SocketTcpClientDestinationAddress2_Object=MibTableColumn
socketTcpClientDestinationAddress2=_SocketTcpClientDestinationAddress2_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,16),_SocketTcpClientDestinationAddress2_Type())
socketTcpClientDestinationAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:socketTcpClientDestinationAddress2.setStatus(_A)
_SocketTcpClientDestinationPort2_Type=Integer32
_SocketTcpClientDestinationPort2_Object=MibTableColumn
socketTcpClientDestinationPort2=_SocketTcpClientDestinationPort2_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,17),_SocketTcpClientDestinationPort2_Type())
socketTcpClientDestinationPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:socketTcpClientDestinationPort2.setStatus(_A)
class _SocketTcpClientDestinationAddress3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SocketTcpClientDestinationAddress3_Type.__name__=_F
_SocketTcpClientDestinationAddress3_Object=MibTableColumn
socketTcpClientDestinationAddress3=_SocketTcpClientDestinationAddress3_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,18),_SocketTcpClientDestinationAddress3_Type())
socketTcpClientDestinationAddress3.setMaxAccess(_B)
if mibBuilder.loadTexts:socketTcpClientDestinationAddress3.setStatus(_A)
_SocketTcpClientDestinationPort3_Type=Integer32
_SocketTcpClientDestinationPort3_Object=MibTableColumn
socketTcpClientDestinationPort3=_SocketTcpClientDestinationPort3_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,19),_SocketTcpClientDestinationPort3_Type())
socketTcpClientDestinationPort3.setMaxAccess(_B)
if mibBuilder.loadTexts:socketTcpClientDestinationPort3.setStatus(_A)
class _SocketTcpClientDestinationAddress4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SocketTcpClientDestinationAddress4_Type.__name__=_F
_SocketTcpClientDestinationAddress4_Object=MibTableColumn
socketTcpClientDestinationAddress4=_SocketTcpClientDestinationAddress4_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,20),_SocketTcpClientDestinationAddress4_Type())
socketTcpClientDestinationAddress4.setMaxAccess(_B)
if mibBuilder.loadTexts:socketTcpClientDestinationAddress4.setStatus(_A)
_SocketTcpClientDestinationPort4_Type=Integer32
_SocketTcpClientDestinationPort4_Object=MibTableColumn
socketTcpClientDestinationPort4=_SocketTcpClientDestinationPort4_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,21),_SocketTcpClientDestinationPort4_Type())
socketTcpClientDestinationPort4.setMaxAccess(_B)
if mibBuilder.loadTexts:socketTcpClientDestinationPort4.setStatus(_A)
_SocketTcpClientDesignatedLocalPort1_Type=Integer32
_SocketTcpClientDesignatedLocalPort1_Object=MibTableColumn
socketTcpClientDesignatedLocalPort1=_SocketTcpClientDesignatedLocalPort1_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,22),_SocketTcpClientDesignatedLocalPort1_Type())
socketTcpClientDesignatedLocalPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:socketTcpClientDesignatedLocalPort1.setStatus(_A)
_SocketTcpClientDesignatedLocalPort2_Type=Integer32
_SocketTcpClientDesignatedLocalPort2_Object=MibTableColumn
socketTcpClientDesignatedLocalPort2=_SocketTcpClientDesignatedLocalPort2_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,23),_SocketTcpClientDesignatedLocalPort2_Type())
socketTcpClientDesignatedLocalPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:socketTcpClientDesignatedLocalPort2.setStatus(_A)
_SocketTcpClientDesignatedLocalPort3_Type=Integer32
_SocketTcpClientDesignatedLocalPort3_Object=MibTableColumn
socketTcpClientDesignatedLocalPort3=_SocketTcpClientDesignatedLocalPort3_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,24),_SocketTcpClientDesignatedLocalPort3_Type())
socketTcpClientDesignatedLocalPort3.setMaxAccess(_B)
if mibBuilder.loadTexts:socketTcpClientDesignatedLocalPort3.setStatus(_A)
_SocketTcpClientDesignatedLocalPort4_Type=Integer32
_SocketTcpClientDesignatedLocalPort4_Object=MibTableColumn
socketTcpClientDesignatedLocalPort4=_SocketTcpClientDesignatedLocalPort4_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,25),_SocketTcpClientDesignatedLocalPort4_Type())
socketTcpClientDesignatedLocalPort4.setMaxAccess(_B)
if mibBuilder.loadTexts:socketTcpClientDesignatedLocalPort4.setStatus(_A)
class _SocketTcpClientConnectionControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(257,258,260,264,514,1028,2056)));namedValues=NamedValues(*(('startup-None',257),('anyCharacter-None',258),('dsrOn-None',260),('dcdOn-None',264),('anyCharacter-InactivityTime',514),('dsrOn-DSR-Off',1028),('dcdOn-DCD-Off',2056)))
_SocketTcpClientConnectionControl_Type.__name__=_C
_SocketTcpClientConnectionControl_Object=MibTableColumn
socketTcpClientConnectionControl=_SocketTcpClientConnectionControl_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,26),_SocketTcpClientConnectionControl_Type())
socketTcpClientConnectionControl.setMaxAccess(_B)
if mibBuilder.loadTexts:socketTcpClientConnectionControl.setStatus(_A)
class _SocketUdpDestinationAddress1Begin_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SocketUdpDestinationAddress1Begin_Type.__name__=_F
_SocketUdpDestinationAddress1Begin_Object=MibTableColumn
socketUdpDestinationAddress1Begin=_SocketUdpDestinationAddress1Begin_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,27),_SocketUdpDestinationAddress1Begin_Type())
socketUdpDestinationAddress1Begin.setMaxAccess(_B)
if mibBuilder.loadTexts:socketUdpDestinationAddress1Begin.setStatus(_A)
class _SocketUdpDestinationAddress1End_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SocketUdpDestinationAddress1End_Type.__name__=_F
_SocketUdpDestinationAddress1End_Object=MibTableColumn
socketUdpDestinationAddress1End=_SocketUdpDestinationAddress1End_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,28),_SocketUdpDestinationAddress1End_Type())
socketUdpDestinationAddress1End.setMaxAccess(_B)
if mibBuilder.loadTexts:socketUdpDestinationAddress1End.setStatus(_A)
_SocketUdpDestinationPort1_Type=Integer32
_SocketUdpDestinationPort1_Object=MibTableColumn
socketUdpDestinationPort1=_SocketUdpDestinationPort1_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,29),_SocketUdpDestinationPort1_Type())
socketUdpDestinationPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:socketUdpDestinationPort1.setStatus(_A)
class _SocketUdpDestinationAddress2Begin_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SocketUdpDestinationAddress2Begin_Type.__name__=_F
_SocketUdpDestinationAddress2Begin_Object=MibTableColumn
socketUdpDestinationAddress2Begin=_SocketUdpDestinationAddress2Begin_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,30),_SocketUdpDestinationAddress2Begin_Type())
socketUdpDestinationAddress2Begin.setMaxAccess(_B)
if mibBuilder.loadTexts:socketUdpDestinationAddress2Begin.setStatus(_A)
class _SocketUdpDestinationAddress2End_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SocketUdpDestinationAddress2End_Type.__name__=_F
_SocketUdpDestinationAddress2End_Object=MibTableColumn
socketUdpDestinationAddress2End=_SocketUdpDestinationAddress2End_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,31),_SocketUdpDestinationAddress2End_Type())
socketUdpDestinationAddress2End.setMaxAccess(_B)
if mibBuilder.loadTexts:socketUdpDestinationAddress2End.setStatus(_A)
_SocketUdpDestinationPort2_Type=Integer32
_SocketUdpDestinationPort2_Object=MibTableColumn
socketUdpDestinationPort2=_SocketUdpDestinationPort2_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,32),_SocketUdpDestinationPort2_Type())
socketUdpDestinationPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:socketUdpDestinationPort2.setStatus(_A)
class _SocketUdpDestinationAddress3Begin_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SocketUdpDestinationAddress3Begin_Type.__name__=_F
_SocketUdpDestinationAddress3Begin_Object=MibTableColumn
socketUdpDestinationAddress3Begin=_SocketUdpDestinationAddress3Begin_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,33),_SocketUdpDestinationAddress3Begin_Type())
socketUdpDestinationAddress3Begin.setMaxAccess(_B)
if mibBuilder.loadTexts:socketUdpDestinationAddress3Begin.setStatus(_A)
class _SocketUdpDestinationAddress3End_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SocketUdpDestinationAddress3End_Type.__name__=_F
_SocketUdpDestinationAddress3End_Object=MibTableColumn
socketUdpDestinationAddress3End=_SocketUdpDestinationAddress3End_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,34),_SocketUdpDestinationAddress3End_Type())
socketUdpDestinationAddress3End.setMaxAccess(_B)
if mibBuilder.loadTexts:socketUdpDestinationAddress3End.setStatus(_A)
_SocketUdpDestinationPort3_Type=Integer32
_SocketUdpDestinationPort3_Object=MibTableColumn
socketUdpDestinationPort3=_SocketUdpDestinationPort3_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,35),_SocketUdpDestinationPort3_Type())
socketUdpDestinationPort3.setMaxAccess(_B)
if mibBuilder.loadTexts:socketUdpDestinationPort3.setStatus(_A)
class _SocketUdpDestinationAddress4Begin_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SocketUdpDestinationAddress4Begin_Type.__name__=_F
_SocketUdpDestinationAddress4Begin_Object=MibTableColumn
socketUdpDestinationAddress4Begin=_SocketUdpDestinationAddress4Begin_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,36),_SocketUdpDestinationAddress4Begin_Type())
socketUdpDestinationAddress4Begin.setMaxAccess(_B)
if mibBuilder.loadTexts:socketUdpDestinationAddress4Begin.setStatus(_A)
class _SocketUdpDestinationAddress4End_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SocketUdpDestinationAddress4End_Type.__name__=_F
_SocketUdpDestinationAddress4End_Object=MibTableColumn
socketUdpDestinationAddress4End=_SocketUdpDestinationAddress4End_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,37),_SocketUdpDestinationAddress4End_Type())
socketUdpDestinationAddress4End.setMaxAccess(_B)
if mibBuilder.loadTexts:socketUdpDestinationAddress4End.setStatus(_A)
_SocketUdpDestinationPort4_Type=Integer32
_SocketUdpDestinationPort4_Object=MibTableColumn
socketUdpDestinationPort4=_SocketUdpDestinationPort4_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,38),_SocketUdpDestinationPort4_Type())
socketUdpDestinationPort4.setMaxAccess(_B)
if mibBuilder.loadTexts:socketUdpDestinationPort4.setStatus(_A)
_SocketUdpLocalListenPort_Type=Integer32
_SocketUdpLocalListenPort_Object=MibTableColumn
socketUdpLocalListenPort=_SocketUdpLocalListenPort_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,39),_SocketUdpLocalListenPort_Type())
socketUdpLocalListenPort.setMaxAccess(_B)
if mibBuilder.loadTexts:socketUdpLocalListenPort.setStatus(_A)
class _SocketUDPDynamicDst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SocketUDPDynamicDst_Type.__name__=_C
_SocketUDPDynamicDst_Object=MibTableColumn
socketUDPDynamicDst=_SocketUDPDynamicDst_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,40),_SocketUDPDynamicDst_Type())
socketUDPDynamicDst.setMaxAccess(_B)
if mibBuilder.loadTexts:socketUDPDynamicDst.setStatus(_A)
_SocketUDPDynamicDstTimeout_Type=Integer32
_SocketUDPDynamicDstTimeout_Object=MibTableColumn
socketUDPDynamicDstTimeout=_SocketUDPDynamicDstTimeout_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,2,1,1,41),_SocketUDPDynamicDstTimeout_Type())
socketUDPDynamicDstTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:socketUDPDynamicDstTimeout.setStatus(_A)
_PairConnection_ObjectIdentity=ObjectIdentity
pairConnection=_PairConnection_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,4,1,2,3))
_PairConnectionTable_Object=MibTable
pairConnectionTable=_PairConnectionTable_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,3,1))
if mibBuilder.loadTexts:pairConnectionTable.setStatus(_A)
_PairConnectionEntry_Object=MibTableRow
pairConnectionEntry=_PairConnectionEntry_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,3,1,1))
pairConnectionEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:pairConnectionEntry.setStatus(_A)
_PairConnectionTcpAliveCheck_Type=Integer32
_PairConnectionTcpAliveCheck_Object=MibTableColumn
pairConnectionTcpAliveCheck=_PairConnectionTcpAliveCheck_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,3,1,1,1),_PairConnectionTcpAliveCheck_Type())
pairConnectionTcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:pairConnectionTcpAliveCheck.setStatus(_A)
class _PairConnectionSecure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PairConnectionSecure_Type.__name__=_C
_PairConnectionSecure_Object=MibTableColumn
pairConnectionSecure=_PairConnectionSecure_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,3,1,1,2),_PairConnectionSecure_Type())
pairConnectionSecure.setMaxAccess(_B)
if mibBuilder.loadTexts:pairConnectionSecure.setStatus(_A)
class _PairConnectionDestinationAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_PairConnectionDestinationAddress_Type.__name__=_F
_PairConnectionDestinationAddress_Object=MibTableColumn
pairConnectionDestinationAddress=_PairConnectionDestinationAddress_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,3,1,1,3),_PairConnectionDestinationAddress_Type())
pairConnectionDestinationAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:pairConnectionDestinationAddress.setStatus(_A)
_PairConnectionDestinationPort_Type=Integer32
_PairConnectionDestinationPort_Object=MibTableColumn
pairConnectionDestinationPort=_PairConnectionDestinationPort_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,3,1,1,4),_PairConnectionDestinationPort_Type())
pairConnectionDestinationPort.setMaxAccess(_B)
if mibBuilder.loadTexts:pairConnectionDestinationPort.setStatus(_A)
_PairConnectionTcpPort_Type=Integer32
_PairConnectionTcpPort_Object=MibTableColumn
pairConnectionTcpPort=_PairConnectionTcpPort_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,3,1,1,5),_PairConnectionTcpPort_Type())
pairConnectionTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:pairConnectionTcpPort.setStatus(_A)
_EthernetModem_ObjectIdentity=ObjectIdentity
ethernetModem=_EthernetModem_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,4,1,2,4))
_EthernetModemTable_Object=MibTable
ethernetModemTable=_EthernetModemTable_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,4,1))
if mibBuilder.loadTexts:ethernetModemTable.setStatus(_A)
_EthernetModemEntry_Object=MibTableRow
ethernetModemEntry=_EthernetModemEntry_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,4,1,1))
ethernetModemEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:ethernetModemEntry.setStatus(_A)
_EthernetModemTcpAliveCheck_Type=Integer32
_EthernetModemTcpAliveCheck_Object=MibTableColumn
ethernetModemTcpAliveCheck=_EthernetModemTcpAliveCheck_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,4,1,1,1),_EthernetModemTcpAliveCheck_Type())
ethernetModemTcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetModemTcpAliveCheck.setStatus(_A)
_EthernetModemTcpPort_Type=Integer32
_EthernetModemTcpPort_Object=MibTableColumn
ethernetModemTcpPort=_EthernetModemTcpPort_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,4,1,1,2),_EthernetModemTcpPort_Type())
ethernetModemTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetModemTcpPort.setStatus(_A)
_Terminal_ObjectIdentity=ObjectIdentity
terminal=_Terminal_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,4,1,2,5))
_TerminalTable_Object=MibTable
terminalTable=_TerminalTable_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,5,1))
if mibBuilder.loadTexts:terminalTable.setStatus(_A)
_TerminalEntry_Object=MibTableRow
terminalEntry=_TerminalEntry_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,5,1,1))
terminalEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:terminalEntry.setStatus(_A)
_TerminalTcpAliveCheck_Type=Integer32
_TerminalTcpAliveCheck_Object=MibTableColumn
terminalTcpAliveCheck=_TerminalTcpAliveCheck_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,5,1,1,1),_TerminalTcpAliveCheck_Type())
terminalTcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalTcpAliveCheck.setStatus(_A)
_TerminalInactivityTime_Type=Integer32
_TerminalInactivityTime_Object=MibTableColumn
terminalInactivityTime=_TerminalInactivityTime_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,5,1,1,2),_TerminalInactivityTime_Type())
terminalInactivityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalInactivityTime.setStatus(_A)
class _TerminalAutoLinkProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('telnet',1),('rlogin',2)))
_TerminalAutoLinkProtocol_Type.__name__=_C
_TerminalAutoLinkProtocol_Object=MibTableColumn
terminalAutoLinkProtocol=_TerminalAutoLinkProtocol_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,5,1,1,3),_TerminalAutoLinkProtocol_Type())
terminalAutoLinkProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalAutoLinkProtocol.setStatus(_A)
class _TerminalPrimaryHostAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TerminalPrimaryHostAddress_Type.__name__=_F
_TerminalPrimaryHostAddress_Object=MibTableColumn
terminalPrimaryHostAddress=_TerminalPrimaryHostAddress_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,5,1,1,4),_TerminalPrimaryHostAddress_Type())
terminalPrimaryHostAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalPrimaryHostAddress.setStatus(_A)
class _TerminalSecondHostAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TerminalSecondHostAddress_Type.__name__=_F
_TerminalSecondHostAddress_Object=MibTableColumn
terminalSecondHostAddress=_TerminalSecondHostAddress_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,5,1,1,5),_TerminalSecondHostAddress_Type())
terminalSecondHostAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalSecondHostAddress.setStatus(_A)
_TerminalTelnetTcpPort_Type=Integer32
_TerminalTelnetTcpPort_Object=MibTableColumn
terminalTelnetTcpPort=_TerminalTelnetTcpPort_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,5,1,1,6),_TerminalTelnetTcpPort_Type())
terminalTelnetTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalTelnetTcpPort.setStatus(_A)
_TerminalSshTcpPort_Type=Integer32
_TerminalSshTcpPort_Object=MibTableColumn
terminalSshTcpPort=_TerminalSshTcpPort_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,5,1,1,7),_TerminalSshTcpPort_Type())
terminalSshTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalSshTcpPort.setStatus(_A)
class _TerminalType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_TerminalType_Type.__name__=_F
_TerminalType_Object=MibTableColumn
terminalType=_TerminalType_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,5,1,1,8),_TerminalType_Type())
terminalType.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalType.setStatus(_A)
class _TerminalMaxSessions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_TerminalMaxSessions_Type.__name__=_C
_TerminalMaxSessions_Object=MibTableColumn
terminalMaxSessions=_TerminalMaxSessions_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,5,1,1,9),_TerminalMaxSessions_Type())
terminalMaxSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalMaxSessions.setStatus(_A)
class _TerminalChangeSession_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_TerminalChangeSession_Type.__name__=_F
_TerminalChangeSession_Object=MibTableColumn
terminalChangeSession=_TerminalChangeSession_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,5,1,1,10),_TerminalChangeSession_Type())
terminalChangeSession.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalChangeSession.setStatus(_A)
class _TerminalQuit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_TerminalQuit_Type.__name__=_F
_TerminalQuit_Object=MibTableColumn
terminalQuit=_TerminalQuit_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,5,1,1,11),_TerminalQuit_Type())
terminalQuit.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalQuit.setStatus(_A)
class _TerminalBreak_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_TerminalBreak_Type.__name__=_F
_TerminalBreak_Object=MibTableColumn
terminalBreak=_TerminalBreak_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,5,1,1,12),_TerminalBreak_Type())
terminalBreak.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalBreak.setStatus(_A)
class _TerminalInterrupt_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_TerminalInterrupt_Type.__name__=_F
_TerminalInterrupt_Object=MibTableColumn
terminalInterrupt=_TerminalInterrupt_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,5,1,1,13),_TerminalInterrupt_Type())
terminalInterrupt.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalInterrupt.setStatus(_A)
class _TerminalAuthenticationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_J,0),(_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6),(_T,7)))
_TerminalAuthenticationType_Type.__name__=_C
_TerminalAuthenticationType_Object=MibTableColumn
terminalAuthenticationType=_TerminalAuthenticationType_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,5,1,1,14),_TerminalAuthenticationType_Type())
terminalAuthenticationType.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalAuthenticationType.setStatus(_A)
class _TerminalTryNextAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TerminalTryNextAuth_Type.__name__=_C
_TerminalTryNextAuth_Object=MibTableColumn
terminalTryNextAuth=_TerminalTryNextAuth_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,5,1,1,15),_TerminalTryNextAuth_Type())
terminalTryNextAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalTryNextAuth.setStatus(_A)
class _TerminalAutoLoginPrompt_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_TerminalAutoLoginPrompt_Type.__name__=_F
_TerminalAutoLoginPrompt_Object=MibTableColumn
terminalAutoLoginPrompt=_TerminalAutoLoginPrompt_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,5,1,1,16),_TerminalAutoLoginPrompt_Type())
terminalAutoLoginPrompt.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalAutoLoginPrompt.setStatus(_A)
class _TerminalPasswordPrompt_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_TerminalPasswordPrompt_Type.__name__=_F
_TerminalPasswordPrompt_Object=MibTableColumn
terminalPasswordPrompt=_TerminalPasswordPrompt_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,5,1,1,17),_TerminalPasswordPrompt_Type())
terminalPasswordPrompt.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalPasswordPrompt.setStatus(_A)
class _TerminalLoginUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_TerminalLoginUserName_Type.__name__=_F
_TerminalLoginUserName_Object=MibTableColumn
terminalLoginUserName=_TerminalLoginUserName_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,5,1,1,18),_TerminalLoginUserName_Type())
terminalLoginUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalLoginUserName.setStatus(_A)
class _TerminalLoginPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_TerminalLoginPassword_Type.__name__=_F
_TerminalLoginPassword_Object=MibTableColumn
terminalLoginPassword=_TerminalLoginPassword_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,5,1,1,19),_TerminalLoginPassword_Type())
terminalLoginPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:terminalLoginPassword.setStatus(_A)
_ReverseTerminal_ObjectIdentity=ObjectIdentity
reverseTerminal=_ReverseTerminal_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,4,1,2,6))
_ReverseTerminalTable_Object=MibTable
reverseTerminalTable=_ReverseTerminalTable_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,6,1))
if mibBuilder.loadTexts:reverseTerminalTable.setStatus(_A)
_ReverseTerminalEntry_Object=MibTableRow
reverseTerminalEntry=_ReverseTerminalEntry_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,6,1,1))
reverseTerminalEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:reverseTerminalEntry.setStatus(_A)
_ReverseTerminalTcpAliveCheck_Type=Integer32
_ReverseTerminalTcpAliveCheck_Object=MibTableColumn
reverseTerminalTcpAliveCheck=_ReverseTerminalTcpAliveCheck_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,6,1,1,1),_ReverseTerminalTcpAliveCheck_Type())
reverseTerminalTcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:reverseTerminalTcpAliveCheck.setStatus(_A)
_ReverseTerminalInactivityTime_Type=Integer32
_ReverseTerminalInactivityTime_Object=MibTableColumn
reverseTerminalInactivityTime=_ReverseTerminalInactivityTime_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,6,1,1,2),_ReverseTerminalInactivityTime_Type())
reverseTerminalInactivityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:reverseTerminalInactivityTime.setStatus(_A)
_ReverseTerminalTcpPort_Type=Integer32
_ReverseTerminalTcpPort_Object=MibTableColumn
reverseTerminalTcpPort=_ReverseTerminalTcpPort_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,6,1,1,3),_ReverseTerminalTcpPort_Type())
reverseTerminalTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:reverseTerminalTcpPort.setStatus(_A)
class _ReverseTerminalAuthenticationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_J,0),(_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6),(_T,7)))
_ReverseTerminalAuthenticationType_Type.__name__=_C
_ReverseTerminalAuthenticationType_Object=MibTableColumn
reverseTerminalAuthenticationType=_ReverseTerminalAuthenticationType_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,6,1,1,4),_ReverseTerminalAuthenticationType_Type())
reverseTerminalAuthenticationType.setMaxAccess(_B)
if mibBuilder.loadTexts:reverseTerminalAuthenticationType.setStatus(_A)
class _ReverseTerminalTryNextAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_ReverseTerminalTryNextAuth_Type.__name__=_C
_ReverseTerminalTryNextAuth_Object=MibTableColumn
reverseTerminalTryNextAuth=_ReverseTerminalTryNextAuth_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,6,1,1,5),_ReverseTerminalTryNextAuth_Type())
reverseTerminalTryNextAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:reverseTerminalTryNextAuth.setStatus(_A)
class _ReverseTerminalMapKeys_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('cr-lf',0),('cr',1),('lf',2)))
_ReverseTerminalMapKeys_Type.__name__=_C
_ReverseTerminalMapKeys_Object=MibTableColumn
reverseTerminalMapKeys=_ReverseTerminalMapKeys_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,6,1,1,6),_ReverseTerminalMapKeys_Type())
reverseTerminalMapKeys.setMaxAccess(_B)
if mibBuilder.loadTexts:reverseTerminalMapKeys.setStatus(_A)
_Printer_ObjectIdentity=ObjectIdentity
printer=_Printer_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,4,1,2,7))
_PrinterTable_Object=MibTable
printerTable=_PrinterTable_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,7,1))
if mibBuilder.loadTexts:printerTable.setStatus(_A)
_PrinterEntry_Object=MibTableRow
printerEntry=_PrinterEntry_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,7,1,1))
printerEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:printerEntry.setStatus(_A)
_PrinterTcpAliveCheck_Type=Integer32
_PrinterTcpAliveCheck_Object=MibTableColumn
printerTcpAliveCheck=_PrinterTcpAliveCheck_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,7,1,1,1),_PrinterTcpAliveCheck_Type())
printerTcpAliveCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:printerTcpAliveCheck.setStatus(_A)
_PrinterTcpPort_Type=Integer32
_PrinterTcpPort_Object=MibTableColumn
printerTcpPort=_PrinterTcpPort_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,7,1,1,2),_PrinterTcpPort_Type())
printerTcpPort.setMaxAccess(_G)
if mibBuilder.loadTexts:printerTcpPort.setStatus(_A)
class _PrinterGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)));namedValues=NamedValues(*(('group1',0),('group2',1),('group3',2),('group4',3),('group5',4),('group6',5),('group7',6),('group8',7),('group9',8),('group10',9),('group11',10),('group12',11),('group13',12),('group14',13),('group15',14),('group16',15),('group17',16),('group18',17),('group19',18),('group20',19),('group21',20),('group22',21),('group23',22),('group24',23),('group25',24),('group26',25),('group27',26),('group28',27),('group29',28),('group30',29),('group31',30),('group32',31)))
_PrinterGroup_Type.__name__=_C
_PrinterGroup_Object=MibTableColumn
printerGroup=_PrinterGroup_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,7,1,1,3),_PrinterGroup_Type())
printerGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:printerGroup.setStatus(_A)
class _PrinterQueueNameRaw_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PrinterQueueNameRaw_Type.__name__=_F
_PrinterQueueNameRaw_Object=MibTableColumn
printerQueueNameRaw=_PrinterQueueNameRaw_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,7,1,1,4),_PrinterQueueNameRaw_Type())
printerQueueNameRaw.setMaxAccess(_B)
if mibBuilder.loadTexts:printerQueueNameRaw.setStatus(_A)
class _PrinterQueueNameASCII_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PrinterQueueNameASCII_Type.__name__=_F
_PrinterQueueNameASCII_Object=MibTableColumn
printerQueueNameASCII=_PrinterQueueNameASCII_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,7,1,1,5),_PrinterQueueNameASCII_Type())
printerQueueNameASCII.setMaxAccess(_B)
if mibBuilder.loadTexts:printerQueueNameASCII.setStatus(_A)
class _PrinterAppendFormFeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PrinterAppendFormFeed_Type.__name__=_C
_PrinterAppendFormFeed_Object=MibTableColumn
printerAppendFormFeed=_PrinterAppendFormFeed_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,7,1,1,6),_PrinterAppendFormFeed_Type())
printerAppendFormFeed.setMaxAccess(_B)
if mibBuilder.loadTexts:printerAppendFormFeed.setStatus(_A)
_Dial_ObjectIdentity=ObjectIdentity
dial=_Dial_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,4,1,2,8))
_DialTable_Object=MibTable
dialTable=_DialTable_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,8,1))
if mibBuilder.loadTexts:dialTable.setStatus(_A)
_DialEntry_Object=MibTableRow
dialEntry=_DialEntry_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,8,1,1))
dialEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:dialEntry.setStatus(_A)
class _DialTERMBINMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DialTERMBINMode_Type.__name__=_C
_DialTERMBINMode_Object=MibTableColumn
dialTERMBINMode=_DialTERMBINMode_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,8,1,1,1),_DialTERMBINMode_Type())
dialTERMBINMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dialTERMBINMode.setStatus(_A)
class _DialPPPDMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DialPPPDMode_Type.__name__=_C
_DialPPPDMode_Object=MibTableColumn
dialPPPDMode=_DialPPPDMode_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,8,1,1,2),_DialPPPDMode_Type())
dialPPPDMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dialPPPDMode.setStatus(_A)
class _DialSLIPDMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DialSLIPDMode_Type.__name__=_C
_DialSLIPDMode_Object=MibTableColumn
dialSLIPDMode=_DialSLIPDMode_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,8,1,1,3),_DialSLIPDMode_Type())
dialSLIPDMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dialSLIPDMode.setStatus(_A)
class _DialAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_J,0),(_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6),(_T,7)))
_DialAuthType_Type.__name__=_C
_DialAuthType_Object=MibTableColumn
dialAuthType=_DialAuthType_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,8,1,1,4),_DialAuthType_Type())
dialAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:dialAuthType.setStatus(_A)
class _DialTryNextAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DialTryNextAuth_Type.__name__=_C
_DialTryNextAuth_Object=MibTableColumn
dialTryNextAuth=_DialTryNextAuth_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,8,1,1,5),_DialTryNextAuth_Type())
dialTryNextAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:dialTryNextAuth.setStatus(_A)
class _DialDisconnectBy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,4)));namedValues=NamedValues(*((_J,0),('dcd-off',2),('dsr-off',4)))
_DialDisconnectBy_Type.__name__=_C
_DialDisconnectBy_Object=MibTableColumn
dialDisconnectBy=_DialDisconnectBy_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,8,1,1,6),_DialDisconnectBy_Type())
dialDisconnectBy.setMaxAccess(_B)
if mibBuilder.loadTexts:dialDisconnectBy.setStatus(_A)
_DialDestinationIpAddress_Type=IpAddress
_DialDestinationIpAddress_Object=MibTableColumn
dialDestinationIpAddress=_DialDestinationIpAddress_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,8,1,1,7),_DialDestinationIpAddress_Type())
dialDestinationIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dialDestinationIpAddress.setStatus(_A)
_DialSourceIpAddress_Type=IpAddress
_DialSourceIpAddress_Object=MibTableColumn
dialSourceIpAddress=_DialSourceIpAddress_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,8,1,1,8),_DialSourceIpAddress_Type())
dialSourceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dialSourceIpAddress.setStatus(_A)
_DialIpNetmask_Type=IpAddress
_DialIpNetmask_Object=MibTableColumn
dialIpNetmask=_DialIpNetmask_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,8,1,1,9),_DialIpNetmask_Type())
dialIpNetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:dialIpNetmask.setStatus(_A)
class _DialTcpIpCompression_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DialTcpIpCompression_Type.__name__=_C
_DialTcpIpCompression_Object=MibTableColumn
dialTcpIpCompression=_DialTcpIpCompression_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,8,1,1,10),_DialTcpIpCompression_Type())
dialTcpIpCompression.setMaxAccess(_B)
if mibBuilder.loadTexts:dialTcpIpCompression.setStatus(_A)
_DialInactivityTime_Type=Integer32
_DialInactivityTime_Object=MibTableColumn
dialInactivityTime=_DialInactivityTime_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,8,1,1,11),_DialInactivityTime_Type())
dialInactivityTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dialInactivityTime.setStatus(_A)
class _DialLinkQualityReport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DialLinkQualityReport_Type.__name__=_C
_DialLinkQualityReport_Object=MibTableColumn
dialLinkQualityReport=_DialLinkQualityReport_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,8,1,1,12),_DialLinkQualityReport_Type())
dialLinkQualityReport.setMaxAccess(_B)
if mibBuilder.loadTexts:dialLinkQualityReport.setStatus(_A)
class _DialUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_DialUsername_Type.__name__=_F
_DialUsername_Object=MibTableColumn
dialUsername=_DialUsername_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,8,1,1,13),_DialUsername_Type())
dialUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:dialUsername.setStatus(_A)
class _DialPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_DialPassword_Type.__name__=_F
_DialPassword_Object=MibTableColumn
dialPassword=_DialPassword_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,8,1,1,14),_DialPassword_Type())
dialPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:dialPassword.setStatus(_A)
class _DialIncomingPAPCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_J,0),(_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6),(_T,7)))
_DialIncomingPAPCheck_Type.__name__=_C
_DialIncomingPAPCheck_Object=MibTableColumn
dialIncomingPAPCheck=_DialIncomingPAPCheck_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,8,1,1,15),_DialIncomingPAPCheck_Type())
dialIncomingPAPCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:dialIncomingPAPCheck.setStatus(_A)
class _DialIncomingTryNextAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DialIncomingTryNextAuth_Type.__name__=_C
_DialIncomingTryNextAuth_Object=MibTableColumn
dialIncomingTryNextAuth=_DialIncomingTryNextAuth_Object((1,3,6,1,4,1,8691,2,8,1,4,1,2,8,1,1,16),_DialIncomingTryNextAuth_Type())
dialIncomingTryNextAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:dialIncomingTryNextAuth.setStatus(_A)
_DataPacking_ObjectIdentity=ObjectIdentity
dataPacking=_DataPacking_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,4,1,3))
_DataPackingPortTable_Object=MibTable
dataPackingPortTable=_DataPackingPortTable_Object((1,3,6,1,4,1,8691,2,8,1,4,1,3,1))
if mibBuilder.loadTexts:dataPackingPortTable.setStatus(_A)
_DataPackingPortEntry_Object=MibTableRow
dataPackingPortEntry=_DataPackingPortEntry_Object((1,3,6,1,4,1,8691,2,8,1,4,1,3,1,1))
dataPackingPortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:dataPackingPortEntry.setStatus(_A)
_PortPacketLength_Type=Integer32
_PortPacketLength_Object=MibTableColumn
portPacketLength=_PortPacketLength_Object((1,3,6,1,4,1,8691,2,8,1,4,1,3,1,1,1),_PortPacketLength_Type())
portPacketLength.setMaxAccess(_B)
if mibBuilder.loadTexts:portPacketLength.setStatus(_A)
class _PortDelimiter1Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PortDelimiter1Enable_Type.__name__=_C
_PortDelimiter1Enable_Object=MibTableColumn
portDelimiter1Enable=_PortDelimiter1Enable_Object((1,3,6,1,4,1,8691,2,8,1,4,1,3,1,1,2),_PortDelimiter1Enable_Type())
portDelimiter1Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:portDelimiter1Enable.setStatus(_A)
class _PortDelimiter1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_PortDelimiter1_Type.__name__=_F
_PortDelimiter1_Object=MibTableColumn
portDelimiter1=_PortDelimiter1_Object((1,3,6,1,4,1,8691,2,8,1,4,1,3,1,1,3),_PortDelimiter1_Type())
portDelimiter1.setMaxAccess(_B)
if mibBuilder.loadTexts:portDelimiter1.setStatus(_A)
class _PortDelimiter2Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PortDelimiter2Enable_Type.__name__=_C
_PortDelimiter2Enable_Object=MibTableColumn
portDelimiter2Enable=_PortDelimiter2Enable_Object((1,3,6,1,4,1,8691,2,8,1,4,1,3,1,1,4),_PortDelimiter2Enable_Type())
portDelimiter2Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:portDelimiter2Enable.setStatus(_A)
class _PortDelimiter2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_PortDelimiter2_Type.__name__=_F
_PortDelimiter2_Object=MibTableColumn
portDelimiter2=_PortDelimiter2_Object((1,3,6,1,4,1,8691,2,8,1,4,1,3,1,1,5),_PortDelimiter2_Type())
portDelimiter2.setMaxAccess(_B)
if mibBuilder.loadTexts:portDelimiter2.setStatus(_A)
class _PortDelimiterProcess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8)));namedValues=NamedValues(*(('doNothing',1),('delimiterAddOne',2),('delimiterAddTwo',4),('stripDelimiter',8)))
_PortDelimiterProcess_Type.__name__=_C
_PortDelimiterProcess_Object=MibTableColumn
portDelimiterProcess=_PortDelimiterProcess_Object((1,3,6,1,4,1,8691,2,8,1,4,1,3,1,1,6),_PortDelimiterProcess_Type())
portDelimiterProcess.setMaxAccess(_B)
if mibBuilder.loadTexts:portDelimiterProcess.setStatus(_A)
_PortForceTransmit_Type=Integer32
_PortForceTransmit_Object=MibTableColumn
portForceTransmit=_PortForceTransmit_Object((1,3,6,1,4,1,8691,2,8,1,4,1,3,1,1,7),_PortForceTransmit_Type())
portForceTransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:portForceTransmit.setStatus(_A)
_ComParamSetting_ObjectIdentity=ObjectIdentity
comParamSetting=_ComParamSetting_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,4,2))
_ComParamPortTable_Object=MibTable
comParamPortTable=_ComParamPortTable_Object((1,3,6,1,4,1,8691,2,8,1,4,2,1))
if mibBuilder.loadTexts:comParamPortTable.setStatus(_A)
_ComParamPortEntry_Object=MibTableRow
comParamPortEntry=_ComParamPortEntry_Object((1,3,6,1,4,1,8691,2,8,1,4,2,1,1))
comParamPortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:comParamPortEntry.setStatus(_A)
class _PortAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortAlias_Type.__name__=_F
_PortAlias_Object=MibTableColumn
portAlias=_PortAlias_Object((1,3,6,1,4,1,8691,2,8,1,4,2,1,1,1),_PortAlias_Type())
portAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:portAlias.setStatus(_A)
class _PortInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_t,0),(_u,1),(_v,2),(_w,3)))
_PortInterface_Type.__name__=_C
_PortInterface_Object=MibTableColumn
portInterface=_PortInterface_Object((1,3,6,1,4,1,8691,2,8,1,4,2,1,1,2),_PortInterface_Type())
portInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:portInterface.setStatus(_A)
class _PortBaudRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*(('b50',0),('b75',1),('b110',2),('b134',3),('b150',4),('b300',5),('b600',6),('b1200',7),('b1800',8),('b2400',9),('b4800',10),('b7200',11),('b9600',12),('b19200',13),('b38400',14),('b57600',15),('b115200',16),('b230400',17),('b460800',18),('b921600',19)))
_PortBaudRate_Type.__name__=_C
_PortBaudRate_Object=MibTableColumn
portBaudRate=_PortBaudRate_Object((1,3,6,1,4,1,8691,2,8,1,4,2,1,1,3),_PortBaudRate_Type())
portBaudRate.setMaxAccess(_B)
if mibBuilder.loadTexts:portBaudRate.setStatus(_A)
class _PortBaudRateManual_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,921600))
_PortBaudRateManual_Type.__name__=_C
_PortBaudRateManual_Object=MibTableColumn
portBaudRateManual=_PortBaudRateManual_Object((1,3,6,1,4,1,8691,2,8,1,4,2,1,1,4),_PortBaudRateManual_Type())
portBaudRateManual.setMaxAccess(_B)
if mibBuilder.loadTexts:portBaudRateManual.setStatus(_A)
class _PortDataBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_x,0),(_y,1),(_z,2),('bits-8',3)))
_PortDataBits_Type.__name__=_C
_PortDataBits_Object=MibTableColumn
portDataBits=_PortDataBits_Object((1,3,6,1,4,1,8691,2,8,1,4,2,1,1,5),_PortDataBits_Type())
portDataBits.setMaxAccess(_B)
if mibBuilder.loadTexts:portDataBits.setStatus(_A)
class _PortStopBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('bits-1',0),('bits-1dot5',1),('bits-2',2)))
_PortStopBits_Type.__name__=_C
_PortStopBits_Object=MibTableColumn
portStopBits=_PortStopBits_Object((1,3,6,1,4,1,8691,2,8,1,4,2,1,1,6),_PortStopBits_Type())
portStopBits.setMaxAccess(_B)
if mibBuilder.loadTexts:portStopBits.setStatus(_A)
class _PortParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_J,0),('odd',1),('even',2),('mark',3),('space',4)))
_PortParity_Type.__name__=_C
_PortParity_Object=MibTableColumn
portParity=_PortParity_Object((1,3,6,1,4,1,8691,2,8,1,4,2,1,1,7),_PortParity_Type())
portParity.setMaxAccess(_B)
if mibBuilder.loadTexts:portParity.setStatus(_A)
class _PortFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_J,0),('rts-cts',1),('xon-xoff',2),('dtr-dsr',3),('rts-toggle',4)))
_PortFlowControl_Type.__name__=_C
_PortFlowControl_Object=MibTableColumn
portFlowControl=_PortFlowControl_Object((1,3,6,1,4,1,8691,2,8,1,4,2,1,1,8),_PortFlowControl_Type())
portFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:portFlowControl.setStatus(_A)
class _PortFIFO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PortFIFO_Type.__name__=_C
_PortFIFO_Object=MibTableColumn
portFIFO=_PortFIFO_Object((1,3,6,1,4,1,8691,2,8,1,4,2,1,1,9),_PortFIFO_Type())
portFIFO.setMaxAccess(_B)
if mibBuilder.loadTexts:portFIFO.setStatus(_A)
_PortOnDelay_Type=Integer32
_PortOnDelay_Object=MibTableColumn
portOnDelay=_PortOnDelay_Object((1,3,6,1,4,1,8691,2,8,1,4,2,1,1,10),_PortOnDelay_Type())
portOnDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:portOnDelay.setStatus(_A)
_PortOffDelay_Type=Integer32
_PortOffDelay_Object=MibTableColumn
portOffDelay=_PortOffDelay_Object((1,3,6,1,4,1,8691,2,8,1,4,2,1,1,11),_PortOffDelay_Type())
portOffDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:portOffDelay.setStatus(_A)
_DataBuffering_ObjectIdentity=ObjectIdentity
dataBuffering=_DataBuffering_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,4,3))
_DataBufferingPortTable_Object=MibTable
dataBufferingPortTable=_DataBufferingPortTable_Object((1,3,6,1,4,1,8691,2,8,1,4,3,1))
if mibBuilder.loadTexts:dataBufferingPortTable.setStatus(_A)
_DataBufferingPortEntry_Object=MibTableRow
dataBufferingPortEntry=_DataBufferingPortEntry_Object((1,3,6,1,4,1,8691,2,8,1,4,3,1,1))
dataBufferingPortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:dataBufferingPortEntry.setStatus(_A)
class _PortBufferingEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PortBufferingEnable_Type.__name__=_C
_PortBufferingEnable_Object=MibTableColumn
portBufferingEnable=_PortBufferingEnable_Object((1,3,6,1,4,1,8691,2,8,1,4,3,1,1,1),_PortBufferingEnable_Type())
portBufferingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:portBufferingEnable.setStatus(_A)
class _PortBufferingLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('memory',0),('sdCard',1)))
_PortBufferingLocation_Type.__name__=_C
_PortBufferingLocation_Object=MibTableColumn
portBufferingLocation=_PortBufferingLocation_Object((1,3,6,1,4,1,8691,2,8,1,4,3,1,1,2),_PortBufferingLocation_Type())
portBufferingLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:portBufferingLocation.setStatus(_A)
_PortBufferingSDFileSize_Type=Integer32
_PortBufferingSDFileSize_Object=MibTableColumn
portBufferingSDFileSize=_PortBufferingSDFileSize_Object((1,3,6,1,4,1,8691,2,8,1,4,3,1,1,3),_PortBufferingSDFileSize_Type())
portBufferingSDFileSize.setMaxAccess(_B)
if mibBuilder.loadTexts:portBufferingSDFileSize.setStatus(_A)
class _PortSerialDataLoggingEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PortSerialDataLoggingEnable_Type.__name__=_C
_PortSerialDataLoggingEnable_Object=MibTableColumn
portSerialDataLoggingEnable=_PortSerialDataLoggingEnable_Object((1,3,6,1,4,1,8691,2,8,1,4,3,1,1,4),_PortSerialDataLoggingEnable_Type())
portSerialDataLoggingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:portSerialDataLoggingEnable.setStatus(_A)
_ModemSettings_ObjectIdentity=ObjectIdentity
modemSettings=_ModemSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,4,4))
_ModemSettingsPortTable_Object=MibTable
modemSettingsPortTable=_ModemSettingsPortTable_Object((1,3,6,1,4,1,8691,2,8,1,4,4,1))
if mibBuilder.loadTexts:modemSettingsPortTable.setStatus(_A)
_ModemSettingsPortEntry_Object=MibTableRow
modemSettingsPortEntry=_ModemSettingsPortEntry_Object((1,3,6,1,4,1,8691,2,8,1,4,4,1,1))
modemSettingsPortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:modemSettingsPortEntry.setStatus(_A)
class _PortEnableModem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PortEnableModem_Type.__name__=_C
_PortEnableModem_Object=MibTableColumn
portEnableModem=_PortEnableModem_Object((1,3,6,1,4,1,8691,2,8,1,4,4,1,1,1),_PortEnableModem_Type())
portEnableModem.setMaxAccess(_B)
if mibBuilder.loadTexts:portEnableModem.setStatus(_A)
class _PortInitialString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_PortInitialString_Type.__name__=_F
_PortInitialString_Object=MibTableColumn
portInitialString=_PortInitialString_Object((1,3,6,1,4,1,8691,2,8,1,4,4,1,1,2),_PortInitialString_Type())
portInitialString.setMaxAccess(_B)
if mibBuilder.loadTexts:portInitialString.setStatus(_A)
class _PortDialUp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_PortDialUp_Type.__name__=_F
_PortDialUp_Object=MibTableColumn
portDialUp=_PortDialUp_Object((1,3,6,1,4,1,8691,2,8,1,4,4,1,1,3),_PortDialUp_Type())
portDialUp.setMaxAccess(_B)
if mibBuilder.loadTexts:portDialUp.setStatus(_A)
class _PortPhoneNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortPhoneNumber_Type.__name__=_F
_PortPhoneNumber_Object=MibTableColumn
portPhoneNumber=_PortPhoneNumber_Object((1,3,6,1,4,1,8691,2,8,1,4,4,1,1,4),_PortPhoneNumber_Type())
portPhoneNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:portPhoneNumber.setStatus(_A)
_CipherSettings_ObjectIdentity=ObjectIdentity
cipherSettings=_CipherSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,4,5))
_CipherSettingsPortTable_Object=MibTable
cipherSettingsPortTable=_CipherSettingsPortTable_Object((1,3,6,1,4,1,8691,2,8,1,4,5,1))
if mibBuilder.loadTexts:cipherSettingsPortTable.setStatus(_A)
_CipherSettingsPortEntry_Object=MibTableRow
cipherSettingsPortEntry=_CipherSettingsPortEntry_Object((1,3,6,1,4,1,8691,2,8,1,4,5,1,1))
cipherSettingsPortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cipherSettingsPortEntry.setStatus(_A)
class _SslCipherSort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(53,53));fixedLength=53
_SslCipherSort_Type.__name__=_F
_SslCipherSort_Object=MibTableColumn
sslCipherSort=_SslCipherSort_Object((1,3,6,1,4,1,8691,2,8,1,4,5,1,1,1),_SslCipherSort_Type())
sslCipherSort.setMaxAccess(_B)
if mibBuilder.loadTexts:sslCipherSort.setStatus(_A)
class _SshCipherSort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SshCipherSort_Type.__name__=_F
_SshCipherSort_Object=MibTableColumn
sshCipherSort=_SshCipherSort_Object((1,3,6,1,4,1,8691,2,8,1,4,5,1,1,2),_SshCipherSort_Type())
sshCipherSort.setMaxAccess(_B)
if mibBuilder.loadTexts:sshCipherSort.setStatus(_A)
_WelcomeMessage_ObjectIdentity=ObjectIdentity
welcomeMessage=_WelcomeMessage_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,4,6))
class _PortEnableWelcomeMessage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PortEnableWelcomeMessage_Type.__name__=_C
_PortEnableWelcomeMessage_Object=MibScalar
portEnableWelcomeMessage=_PortEnableWelcomeMessage_Object((1,3,6,1,4,1,8691,2,8,1,4,6,1),_PortEnableWelcomeMessage_Type())
portEnableWelcomeMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:portEnableWelcomeMessage.setStatus(_A)
class _PortMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1280))
_PortMessage_Type.__name__=_F
_PortMessage_Object=MibScalar
portMessage=_PortMessage_Object((1,3,6,1,4,1,8691,2,8,1,4,6,2),_PortMessage_Type())
portMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:portMessage.setStatus(_A)
_SysManagement_ObjectIdentity=ObjectIdentity
sysManagement=_SysManagement_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5))
_MiscNetworkSettings_ObjectIdentity=ObjectIdentity
miscNetworkSettings=_MiscNetworkSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,1))
_AccessibleIp_ObjectIdentity=ObjectIdentity
accessibleIp=_AccessibleIp_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,1,1))
class _EnableAccessibleIpList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_EnableAccessibleIpList_Type.__name__=_C
_EnableAccessibleIpList_Object=MibScalar
enableAccessibleIpList=_EnableAccessibleIpList_Object((1,3,6,1,4,1,8691,2,8,1,5,1,1,1),_EnableAccessibleIpList_Type())
enableAccessibleIpList.setMaxAccess(_B)
if mibBuilder.loadTexts:enableAccessibleIpList.setStatus(_A)
_AccessibleIpListTable_Object=MibTable
accessibleIpListTable=_AccessibleIpListTable_Object((1,3,6,1,4,1,8691,2,8,1,5,1,1,2))
if mibBuilder.loadTexts:accessibleIpListTable.setStatus(_A)
_AccessibleIpListEntry_Object=MibTableRow
accessibleIpListEntry=_AccessibleIpListEntry_Object((1,3,6,1,4,1,8691,2,8,1,5,1,1,2,1))
accessibleIpListEntry.setIndexNames((0,_H,_A0))
if mibBuilder.loadTexts:accessibleIpListEntry.setStatus(_A)
_AccessibleIpListIndex_Type=Integer32
_AccessibleIpListIndex_Object=MibTableColumn
accessibleIpListIndex=_AccessibleIpListIndex_Object((1,3,6,1,4,1,8691,2,8,1,5,1,1,2,1,1),_AccessibleIpListIndex_Type())
accessibleIpListIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:accessibleIpListIndex.setStatus(_A)
class _ActiveAccessibleIpList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_ActiveAccessibleIpList_Type.__name__=_C
_ActiveAccessibleIpList_Object=MibTableColumn
activeAccessibleIpList=_ActiveAccessibleIpList_Object((1,3,6,1,4,1,8691,2,8,1,5,1,1,2,1,2),_ActiveAccessibleIpList_Type())
activeAccessibleIpList.setMaxAccess(_B)
if mibBuilder.loadTexts:activeAccessibleIpList.setStatus(_A)
class _AccessibleIpListAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_AccessibleIpListAddress_Type.__name__=_F
_AccessibleIpListAddress_Object=MibTableColumn
accessibleIpListAddress=_AccessibleIpListAddress_Object((1,3,6,1,4,1,8691,2,8,1,5,1,1,2,1,3),_AccessibleIpListAddress_Type())
accessibleIpListAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:accessibleIpListAddress.setStatus(_A)
class _AccessibleIpListNetmask_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AccessibleIpListNetmask_Type.__name__=_F
_AccessibleIpListNetmask_Object=MibTableColumn
accessibleIpListNetmask=_AccessibleIpListNetmask_Object((1,3,6,1,4,1,8691,2,8,1,5,1,1,2,1,4),_AccessibleIpListNetmask_Type())
accessibleIpListNetmask.setMaxAccess(_B)
if mibBuilder.loadTexts:accessibleIpListNetmask.setStatus(_A)
_SnmpAgentSettings_ObjectIdentity=ObjectIdentity
snmpAgentSettings=_SnmpAgentSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,1,2))
class _SnmpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SnmpEnable_Type.__name__=_C
_SnmpEnable_Object=MibScalar
snmpEnable=_SnmpEnable_Object((1,3,6,1,4,1,8691,2,8,1,5,1,2,1),_SnmpEnable_Type())
snmpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpEnable.setStatus(_A)
class _SnmpContactName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SnmpContactName_Type.__name__=_F
_SnmpContactName_Object=MibScalar
snmpContactName=_SnmpContactName_Object((1,3,6,1,4,1,8691,2,8,1,5,1,2,2),_SnmpContactName_Type())
snmpContactName.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpContactName.setStatus(_A)
class _SnmpLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SnmpLocation_Type.__name__=_F
_SnmpLocation_Object=MibScalar
snmpLocation=_SnmpLocation_Object((1,3,6,1,4,1,8691,2,8,1,5,1,2,3),_SnmpLocation_Type())
snmpLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpLocation.setStatus(_A)
_DDNS_ObjectIdentity=ObjectIdentity
dDNS=_DDNS_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,1,3))
class _DDNSEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_DDNSEnable_Type.__name__=_C
_DDNSEnable_Object=MibScalar
dDNSEnable=_DDNSEnable_Object((1,3,6,1,4,1,8691,2,8,1,5,1,3,1),_DDNSEnable_Type())
dDNSEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:dDNSEnable.setStatus(_A)
class _DDNSServerAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('dynDns-org',0))
_DDNSServerAddress_Type.__name__=_C
_DDNSServerAddress_Object=MibScalar
dDNSServerAddress=_DDNSServerAddress_Object((1,3,6,1,4,1,8691,2,8,1,5,1,3,2),_DDNSServerAddress_Type())
dDNSServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dDNSServerAddress.setStatus(_A)
class _DDNSHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,60))
_DDNSHostName_Type.__name__=_F
_DDNSHostName_Object=MibScalar
dDNSHostName=_DDNSHostName_Object((1,3,6,1,4,1,8691,2,8,1,5,1,3,3),_DDNSHostName_Type())
dDNSHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:dDNSHostName.setStatus(_A)
class _DDNSUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,60))
_DDNSUserName_Type.__name__=_F
_DDNSUserName_Object=MibScalar
dDNSUserName=_DDNSUserName_Object((1,3,6,1,4,1,8691,2,8,1,5,1,3,4),_DDNSUserName_Type())
dDNSUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:dDNSUserName.setStatus(_A)
class _DDNSPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,60))
_DDNSPassword_Type.__name__=_F
_DDNSPassword_Object=MibScalar
dDNSPassword=_DDNSPassword_Object((1,3,6,1,4,1,8691,2,8,1,5,1,3,5),_DDNSPassword_Type())
dDNSPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:dDNSPassword.setStatus(_A)
_HostTable_ObjectIdentity=ObjectIdentity
hostTable=_HostTable_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,1,4))
_HostTableTable_Object=MibTable
hostTableTable=_HostTableTable_Object((1,3,6,1,4,1,8691,2,8,1,5,1,4,1))
if mibBuilder.loadTexts:hostTableTable.setStatus(_A)
_HostTableEntry_Object=MibTableRow
hostTableEntry=_HostTableEntry_Object((1,3,6,1,4,1,8691,2,8,1,5,1,4,1,1))
hostTableEntry.setIndexNames((0,_H,_A1))
if mibBuilder.loadTexts:hostTableEntry.setStatus(_A)
_HostTableIndex_Type=Integer32
_HostTableIndex_Object=MibTableColumn
hostTableIndex=_HostTableIndex_Object((1,3,6,1,4,1,8691,2,8,1,5,1,4,1,1,1),_HostTableIndex_Type())
hostTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hostTableIndex.setStatus(_A)
class _HostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_HostName_Type.__name__=_F
_HostName_Object=MibTableColumn
hostName=_HostName_Object((1,3,6,1,4,1,8691,2,8,1,5,1,4,1,1,2),_HostName_Type())
hostName.setMaxAccess(_B)
if mibBuilder.loadTexts:hostName.setStatus(_A)
class _HostIpAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_HostIpAddress_Type.__name__=_F
_HostIpAddress_Object=MibTableColumn
hostIpAddress=_HostIpAddress_Object((1,3,6,1,4,1,8691,2,8,1,5,1,4,1,1,3),_HostIpAddress_Type())
hostIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hostIpAddress.setStatus(_A)
_RouteTable_ObjectIdentity=ObjectIdentity
routeTable=_RouteTable_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,1,5))
_RouteTableTable_Object=MibTable
routeTableTable=_RouteTableTable_Object((1,3,6,1,4,1,8691,2,8,1,5,1,5,1))
if mibBuilder.loadTexts:routeTableTable.setStatus(_A)
_RouteTableEntry_Object=MibTableRow
routeTableEntry=_RouteTableEntry_Object((1,3,6,1,4,1,8691,2,8,1,5,1,5,1,1))
routeTableEntry.setIndexNames((0,_H,_A2))
if mibBuilder.loadTexts:routeTableEntry.setStatus(_A)
_RouteTableIndex_Type=Integer32
_RouteTableIndex_Object=MibTableColumn
routeTableIndex=_RouteTableIndex_Object((1,3,6,1,4,1,8691,2,8,1,5,1,5,1,1,1),_RouteTableIndex_Type())
routeTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:routeTableIndex.setStatus(_A)
_GatewayRouteTable_Type=IpAddress
_GatewayRouteTable_Object=MibTableColumn
gatewayRouteTable=_GatewayRouteTable_Object((1,3,6,1,4,1,8691,2,8,1,5,1,5,1,1,2),_GatewayRouteTable_Type())
gatewayRouteTable.setMaxAccess(_B)
if mibBuilder.loadTexts:gatewayRouteTable.setStatus(_A)
_DestinationRouteTable_Type=IpAddress
_DestinationRouteTable_Object=MibTableColumn
destinationRouteTable=_DestinationRouteTable_Object((1,3,6,1,4,1,8691,2,8,1,5,1,5,1,1,3),_DestinationRouteTable_Type())
destinationRouteTable.setMaxAccess(_B)
if mibBuilder.loadTexts:destinationRouteTable.setStatus(_A)
_NetmaskRouteTable_Type=IpAddress
_NetmaskRouteTable_Object=MibTableColumn
netmaskRouteTable=_NetmaskRouteTable_Object((1,3,6,1,4,1,8691,2,8,1,5,1,5,1,1,4),_NetmaskRouteTable_Type())
netmaskRouteTable.setMaxAccess(_B)
if mibBuilder.loadTexts:netmaskRouteTable.setStatus(_A)
_MetricRouteTable_Type=Integer32
_MetricRouteTable_Object=MibTableColumn
metricRouteTable=_MetricRouteTable_Object((1,3,6,1,4,1,8691,2,8,1,5,1,5,1,1,5),_MetricRouteTable_Type())
metricRouteTable.setMaxAccess(_B)
if mibBuilder.loadTexts:metricRouteTable.setStatus(_A)
class _InterfaceRouteTable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,256)));namedValues=NamedValues(*(('port1',0),('port2',1),('port3',2),('port4',3),('port5',4),('port6',5),('port7',6),('port8',7),('port9',8),('port10',9),('port11',10),('port12',11),('port13',12),('port14',13),('port15',14),('port16',15),('port17',16),('port18',17),('port19',18),('port20',19),('port21',20),('port22',21),('port23',22),('port24',23),('port25',24),('port26',25),('port27',26),('port28',27),('port29',28),('port30',29),('port31',30),('port32',31),('lan',256)))
_InterfaceRouteTable_Type.__name__=_C
_InterfaceRouteTable_Object=MibTableColumn
interfaceRouteTable=_InterfaceRouteTable_Object((1,3,6,1,4,1,8691,2,8,1,5,1,5,1,1,6),_InterfaceRouteTable_Type())
interfaceRouteTable.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceRouteTable.setStatus(_A)
_UserTable_ObjectIdentity=ObjectIdentity
userTable=_UserTable_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,1,6))
_UserTableTable_Object=MibTable
userTableTable=_UserTableTable_Object((1,3,6,1,4,1,8691,2,8,1,5,1,6,1))
if mibBuilder.loadTexts:userTableTable.setStatus(_A)
_UserTableEntry_Object=MibTableRow
userTableEntry=_UserTableEntry_Object((1,3,6,1,4,1,8691,2,8,1,5,1,6,1,1))
userTableEntry.setIndexNames((0,_H,_A3))
if mibBuilder.loadTexts:userTableEntry.setStatus(_A)
_UserTableIndex_Type=Integer32
_UserTableIndex_Object=MibTableColumn
userTableIndex=_UserTableIndex_Object((1,3,6,1,4,1,8691,2,8,1,5,1,6,1,1,1),_UserTableIndex_Type())
userTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:userTableIndex.setStatus(_A)
class _UserNameUserTable_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_UserNameUserTable_Type.__name__=_F
_UserNameUserTable_Object=MibTableColumn
userNameUserTable=_UserNameUserTable_Object((1,3,6,1,4,1,8691,2,8,1,5,1,6,1,1,2),_UserNameUserTable_Type())
userNameUserTable.setMaxAccess(_B)
if mibBuilder.loadTexts:userNameUserTable.setStatus(_A)
class _PasswordUserTable_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PasswordUserTable_Type.__name__=_F
_PasswordUserTable_Object=MibTableColumn
passwordUserTable=_PasswordUserTable_Object((1,3,6,1,4,1,8691,2,8,1,5,1,6,1,1,3),_PasswordUserTable_Type())
passwordUserTable.setMaxAccess(_B)
if mibBuilder.loadTexts:passwordUserTable.setStatus(_A)
class _PhoneNumberUserTable_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PhoneNumberUserTable_Type.__name__=_F
_PhoneNumberUserTable_Object=MibTableColumn
phoneNumberUserTable=_PhoneNumberUserTable_Object((1,3,6,1,4,1,8691,2,8,1,5,1,6,1,1,4),_PhoneNumberUserTable_Type())
phoneNumberUserTable.setMaxAccess(_B)
if mibBuilder.loadTexts:phoneNumberUserTable.setStatus(_A)
_AuthenticationServer_ObjectIdentity=ObjectIdentity
authenticationServer=_AuthenticationServer_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,1,7))
class _RadiusServerIp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RadiusServerIp_Type.__name__=_F
_RadiusServerIp_Object=MibScalar
radiusServerIp=_RadiusServerIp_Object((1,3,6,1,4,1,8691,2,8,1,5,1,7,1),_RadiusServerIp_Type())
radiusServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusServerIp.setStatus(_A)
class _RadiusKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_RadiusKey_Type.__name__=_F
_RadiusKey_Object=MibScalar
radiusKey=_RadiusKey_Object((1,3,6,1,4,1,8691,2,8,1,5,1,7,2),_RadiusKey_Type())
radiusKey.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusKey.setStatus(_A)
class _UdpPortAuthenticationServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1645,1812)));namedValues=NamedValues(*(('port1645',1645),('port1812',1812)))
_UdpPortAuthenticationServer_Type.__name__=_C
_UdpPortAuthenticationServer_Object=MibScalar
udpPortAuthenticationServer=_UdpPortAuthenticationServer_Object((1,3,6,1,4,1,8691,2,8,1,5,1,7,3),_UdpPortAuthenticationServer_Type())
udpPortAuthenticationServer.setMaxAccess(_B)
if mibBuilder.loadTexts:udpPortAuthenticationServer.setStatus(_A)
class _RadiusAccounting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_RadiusAccounting_Type.__name__=_C
_RadiusAccounting_Object=MibScalar
radiusAccounting=_RadiusAccounting_Object((1,3,6,1,4,1,8691,2,8,1,5,1,7,4),_RadiusAccounting_Type())
radiusAccounting.setMaxAccess(_B)
if mibBuilder.loadTexts:radiusAccounting.setStatus(_A)
class _TacacsPlusServerIp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TacacsPlusServerIp_Type.__name__=_F
_TacacsPlusServerIp_Object=MibScalar
tacacsPlusServerIp=_TacacsPlusServerIp_Object((1,3,6,1,4,1,8691,2,8,1,5,1,7,5),_TacacsPlusServerIp_Type())
tacacsPlusServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:tacacsPlusServerIp.setStatus(_A)
class _TacacsPlusSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_TacacsPlusSecret_Type.__name__=_F
_TacacsPlusSecret_Object=MibScalar
tacacsPlusSecret=_TacacsPlusSecret_Object((1,3,6,1,4,1,8691,2,8,1,5,1,7,6),_TacacsPlusSecret_Type())
tacacsPlusSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:tacacsPlusSecret.setStatus(_A)
class _TacacsPlusAccounting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TacacsPlusAccounting_Type.__name__=_C
_TacacsPlusAccounting_Object=MibScalar
tacacsPlusAccounting=_TacacsPlusAccounting_Object((1,3,6,1,4,1,8691,2,8,1,5,1,7,7),_TacacsPlusAccounting_Type())
tacacsPlusAccounting.setMaxAccess(_B)
if mibBuilder.loadTexts:tacacsPlusAccounting.setStatus(_A)
_SysLogSettings_ObjectIdentity=ObjectIdentity
sysLogSettings=_SysLogSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,1,8))
class _SysLocalLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SysLocalLog_Type.__name__=_C
_SysLocalLog_Object=MibScalar
sysLocalLog=_SysLocalLog_Object((1,3,6,1,4,1,8691,2,8,1,5,1,8,1),_SysLocalLog_Type())
sysLocalLog.setMaxAccess(_B)
if mibBuilder.loadTexts:sysLocalLog.setStatus(_A)
class _NetworkLocalLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NetworkLocalLog_Type.__name__=_C
_NetworkLocalLog_Object=MibScalar
networkLocalLog=_NetworkLocalLog_Object((1,3,6,1,4,1,8691,2,8,1,5,1,8,2),_NetworkLocalLog_Type())
networkLocalLog.setMaxAccess(_B)
if mibBuilder.loadTexts:networkLocalLog.setStatus(_A)
class _ConfigLocalLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_ConfigLocalLog_Type.__name__=_C
_ConfigLocalLog_Object=MibScalar
configLocalLog=_ConfigLocalLog_Object((1,3,6,1,4,1,8691,2,8,1,5,1,8,3),_ConfigLocalLog_Type())
configLocalLog.setMaxAccess(_B)
if mibBuilder.loadTexts:configLocalLog.setStatus(_A)
class _OpModeLocalLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_OpModeLocalLog_Type.__name__=_C
_OpModeLocalLog_Object=MibScalar
opModeLocalLog=_OpModeLocalLog_Object((1,3,6,1,4,1,8691,2,8,1,5,1,8,4),_OpModeLocalLog_Type())
opModeLocalLog.setMaxAccess(_B)
if mibBuilder.loadTexts:opModeLocalLog.setStatus(_A)
class _SysRemoteLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SysRemoteLog_Type.__name__=_C
_SysRemoteLog_Object=MibScalar
sysRemoteLog=_SysRemoteLog_Object((1,3,6,1,4,1,8691,2,8,1,5,1,8,5),_SysRemoteLog_Type())
sysRemoteLog.setMaxAccess(_B)
if mibBuilder.loadTexts:sysRemoteLog.setStatus(_A)
class _NetworkRemoteLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NetworkRemoteLog_Type.__name__=_C
_NetworkRemoteLog_Object=MibScalar
networkRemoteLog=_NetworkRemoteLog_Object((1,3,6,1,4,1,8691,2,8,1,5,1,8,6),_NetworkRemoteLog_Type())
networkRemoteLog.setMaxAccess(_B)
if mibBuilder.loadTexts:networkRemoteLog.setStatus(_A)
class _ConfigRemoteLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_ConfigRemoteLog_Type.__name__=_C
_ConfigRemoteLog_Object=MibScalar
configRemoteLog=_ConfigRemoteLog_Object((1,3,6,1,4,1,8691,2,8,1,5,1,8,7),_ConfigRemoteLog_Type())
configRemoteLog.setMaxAccess(_B)
if mibBuilder.loadTexts:configRemoteLog.setStatus(_A)
class _OpModeRemoteLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_OpModeRemoteLog_Type.__name__=_C
_OpModeRemoteLog_Object=MibScalar
opModeRemoteLog=_OpModeRemoteLog_Object((1,3,6,1,4,1,8691,2,8,1,5,1,8,8),_OpModeRemoteLog_Type())
opModeRemoteLog.setMaxAccess(_B)
if mibBuilder.loadTexts:opModeRemoteLog.setStatus(_A)
_RemoteLogServer_ObjectIdentity=ObjectIdentity
remoteLogServer=_RemoteLogServer_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,1,9))
class _SyslogServerIp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_SyslogServerIp_Type.__name__=_F
_SyslogServerIp_Object=MibScalar
syslogServerIp=_SyslogServerIp_Object((1,3,6,1,4,1,8691,2,8,1,5,1,9,1),_SyslogServerIp_Type())
syslogServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:syslogServerIp.setStatus(_A)
class _SyslogFacility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('local-use-0',0),('local-use-1',1),('local-use-2',2),('local-use-3',3),('local-use-4',4),('local-use-5',5),('local-use-6',6),('local-use-7',7)))
_SyslogFacility_Type.__name__=_C
_SyslogFacility_Object=MibScalar
syslogFacility=_SyslogFacility_Object((1,3,6,1,4,1,8691,2,8,1,5,1,9,2),_SyslogFacility_Type())
syslogFacility.setMaxAccess(_B)
if mibBuilder.loadTexts:syslogFacility.setStatus(_A)
class _SyslogSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('emergency',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('informational',6),('debug',7)))
_SyslogSeverity_Type.__name__=_C
_SyslogSeverity_Object=MibScalar
syslogSeverity=_SyslogSeverity_Object((1,3,6,1,4,1,8691,2,8,1,5,1,9,3),_SyslogSeverity_Type())
syslogSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:syslogSeverity.setStatus(_A)
_AutoWarningSettings_ObjectIdentity=ObjectIdentity
autoWarningSettings=_AutoWarningSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,2))
_EventSettings_ObjectIdentity=ObjectIdentity
eventSettings=_EventSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,2,1))
class _MailWarningColdStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_MailWarningColdStart_Type.__name__=_C
_MailWarningColdStart_Object=MibScalar
mailWarningColdStart=_MailWarningColdStart_Object((1,3,6,1,4,1,8691,2,8,1,5,2,1,1),_MailWarningColdStart_Type())
mailWarningColdStart.setMaxAccess(_B)
if mibBuilder.loadTexts:mailWarningColdStart.setStatus(_A)
class _MailWarningWarmStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_MailWarningWarmStart_Type.__name__=_C
_MailWarningWarmStart_Object=MibScalar
mailWarningWarmStart=_MailWarningWarmStart_Object((1,3,6,1,4,1,8691,2,8,1,5,2,1,2),_MailWarningWarmStart_Type())
mailWarningWarmStart.setMaxAccess(_B)
if mibBuilder.loadTexts:mailWarningWarmStart.setStatus(_A)
class _MailWarningAuthFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_MailWarningAuthFailure_Type.__name__=_C
_MailWarningAuthFailure_Object=MibScalar
mailWarningAuthFailure=_MailWarningAuthFailure_Object((1,3,6,1,4,1,8691,2,8,1,5,2,1,3),_MailWarningAuthFailure_Type())
mailWarningAuthFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:mailWarningAuthFailure.setStatus(_A)
class _MailWarningIpChanged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_MailWarningIpChanged_Type.__name__=_C
_MailWarningIpChanged_Object=MibScalar
mailWarningIpChanged=_MailWarningIpChanged_Object((1,3,6,1,4,1,8691,2,8,1,5,2,1,4),_MailWarningIpChanged_Type())
mailWarningIpChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:mailWarningIpChanged.setStatus(_A)
class _MailWarningPasswordChanged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_MailWarningPasswordChanged_Type.__name__=_C
_MailWarningPasswordChanged_Object=MibScalar
mailWarningPasswordChanged=_MailWarningPasswordChanged_Object((1,3,6,1,4,1,8691,2,8,1,5,2,1,5),_MailWarningPasswordChanged_Type())
mailWarningPasswordChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:mailWarningPasswordChanged.setStatus(_A)
class _TrapServerColdStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TrapServerColdStart_Type.__name__=_C
_TrapServerColdStart_Object=MibScalar
trapServerColdStart=_TrapServerColdStart_Object((1,3,6,1,4,1,8691,2,8,1,5,2,1,6),_TrapServerColdStart_Type())
trapServerColdStart.setMaxAccess(_B)
if mibBuilder.loadTexts:trapServerColdStart.setStatus(_A)
class _TrapServerWarmStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TrapServerWarmStart_Type.__name__=_C
_TrapServerWarmStart_Object=MibScalar
trapServerWarmStart=_TrapServerWarmStart_Object((1,3,6,1,4,1,8691,2,8,1,5,2,1,7),_TrapServerWarmStart_Type())
trapServerWarmStart.setMaxAccess(_B)
if mibBuilder.loadTexts:trapServerWarmStart.setStatus(_A)
class _TrapServerAuthFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TrapServerAuthFailure_Type.__name__=_C
_TrapServerAuthFailure_Object=MibScalar
trapServerAuthFailure=_TrapServerAuthFailure_Object((1,3,6,1,4,1,8691,2,8,1,5,2,1,8),_TrapServerAuthFailure_Type())
trapServerAuthFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:trapServerAuthFailure.setStatus(_A)
class _AlarmServerEthernet1LinkDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_AlarmServerEthernet1LinkDown_Type.__name__=_C
_AlarmServerEthernet1LinkDown_Object=MibScalar
alarmServerEthernet1LinkDown=_AlarmServerEthernet1LinkDown_Object((1,3,6,1,4,1,8691,2,8,1,5,2,1,9),_AlarmServerEthernet1LinkDown_Type())
alarmServerEthernet1LinkDown.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmServerEthernet1LinkDown.setStatus(_A)
class _AlarmServerEthernet2LinkDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_AlarmServerEthernet2LinkDown_Type.__name__=_C
_AlarmServerEthernet2LinkDown_Object=MibScalar
alarmServerEthernet2LinkDown=_AlarmServerEthernet2LinkDown_Object((1,3,6,1,4,1,8691,2,8,1,5,2,1,10),_AlarmServerEthernet2LinkDown_Type())
alarmServerEthernet2LinkDown.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmServerEthernet2LinkDown.setStatus(_A)
class _AlarmServerEthernet3LinkDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_AlarmServerEthernet3LinkDown_Type.__name__=_C
_AlarmServerEthernet3LinkDown_Object=MibScalar
alarmServerEthernet3LinkDown=_AlarmServerEthernet3LinkDown_Object((1,3,6,1,4,1,8691,2,8,1,5,2,1,11),_AlarmServerEthernet3LinkDown_Type())
alarmServerEthernet3LinkDown.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmServerEthernet3LinkDown.setStatus(_A)
class _SmsServerColdStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SmsServerColdStart_Type.__name__=_C
_SmsServerColdStart_Object=MibScalar
smsServerColdStart=_SmsServerColdStart_Object((1,3,6,1,4,1,8691,2,8,1,5,2,1,12),_SmsServerColdStart_Type())
smsServerColdStart.setMaxAccess(_B)
if mibBuilder.loadTexts:smsServerColdStart.setStatus(_A)
class _SmsServerWarmStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SmsServerWarmStart_Type.__name__=_C
_SmsServerWarmStart_Object=MibScalar
smsServerWarmStart=_SmsServerWarmStart_Object((1,3,6,1,4,1,8691,2,8,1,5,2,1,13),_SmsServerWarmStart_Type())
smsServerWarmStart.setMaxAccess(_B)
if mibBuilder.loadTexts:smsServerWarmStart.setStatus(_A)
class _SmsServerEthernet1LinkDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SmsServerEthernet1LinkDown_Type.__name__=_C
_SmsServerEthernet1LinkDown_Object=MibScalar
smsServerEthernet1LinkDown=_SmsServerEthernet1LinkDown_Object((1,3,6,1,4,1,8691,2,8,1,5,2,1,14),_SmsServerEthernet1LinkDown_Type())
smsServerEthernet1LinkDown.setMaxAccess(_B)
if mibBuilder.loadTexts:smsServerEthernet1LinkDown.setStatus(_A)
class _SmsServerEthernet2LinkDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SmsServerEthernet2LinkDown_Type.__name__=_C
_SmsServerEthernet2LinkDown_Object=MibScalar
smsServerEthernet2LinkDown=_SmsServerEthernet2LinkDown_Object((1,3,6,1,4,1,8691,2,8,1,5,2,1,15),_SmsServerEthernet2LinkDown_Type())
smsServerEthernet2LinkDown.setMaxAccess(_B)
if mibBuilder.loadTexts:smsServerEthernet2LinkDown.setStatus(_A)
class _SmsServerEthernet3LinkDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SmsServerEthernet3LinkDown_Type.__name__=_C
_SmsServerEthernet3LinkDown_Object=MibScalar
smsServerEthernet3LinkDown=_SmsServerEthernet3LinkDown_Object((1,3,6,1,4,1,8691,2,8,1,5,2,1,16),_SmsServerEthernet3LinkDown_Type())
smsServerEthernet3LinkDown.setMaxAccess(_B)
if mibBuilder.loadTexts:smsServerEthernet3LinkDown.setStatus(_A)
class _SmsServerAuthFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SmsServerAuthFailure_Type.__name__=_C
_SmsServerAuthFailure_Object=MibScalar
smsServerAuthFailure=_SmsServerAuthFailure_Object((1,3,6,1,4,1,8691,2,8,1,5,2,1,17),_SmsServerAuthFailure_Type())
smsServerAuthFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:smsServerAuthFailure.setStatus(_A)
class _SmsServerIpChanged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SmsServerIpChanged_Type.__name__=_C
_SmsServerIpChanged_Object=MibScalar
smsServerIpChanged=_SmsServerIpChanged_Object((1,3,6,1,4,1,8691,2,8,1,5,2,1,18),_SmsServerIpChanged_Type())
smsServerIpChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:smsServerIpChanged.setStatus(_A)
class _SmsServerPasswordChanged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SmsServerPasswordChanged_Type.__name__=_C
_SmsServerPasswordChanged_Object=MibScalar
smsServerPasswordChanged=_SmsServerPasswordChanged_Object((1,3,6,1,4,1,8691,2,8,1,5,2,1,19),_SmsServerPasswordChanged_Type())
smsServerPasswordChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:smsServerPasswordChanged.setStatus(_A)
_SerialEventSettings_ObjectIdentity=ObjectIdentity
serialEventSettings=_SerialEventSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,2,2))
_PortEventSettingsTable_Object=MibTable
portEventSettingsTable=_PortEventSettingsTable_Object((1,3,6,1,4,1,8691,2,8,1,5,2,2,1))
if mibBuilder.loadTexts:portEventSettingsTable.setStatus(_A)
_PortEventSettingsEntry_Object=MibTableRow
portEventSettingsEntry=_PortEventSettingsEntry_Object((1,3,6,1,4,1,8691,2,8,1,5,2,2,1,1))
portEventSettingsEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:portEventSettingsEntry.setStatus(_A)
class _MailDCDchange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_MailDCDchange_Type.__name__=_C
_MailDCDchange_Object=MibTableColumn
mailDCDchange=_MailDCDchange_Object((1,3,6,1,4,1,8691,2,8,1,5,2,2,1,1,1),_MailDCDchange_Type())
mailDCDchange.setMaxAccess(_B)
if mibBuilder.loadTexts:mailDCDchange.setStatus(_A)
class _TrapDCDchange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TrapDCDchange_Type.__name__=_C
_TrapDCDchange_Object=MibTableColumn
trapDCDchange=_TrapDCDchange_Object((1,3,6,1,4,1,8691,2,8,1,5,2,2,1,1,2),_TrapDCDchange_Type())
trapDCDchange.setMaxAccess(_B)
if mibBuilder.loadTexts:trapDCDchange.setStatus(_A)
class _AlarmDCDchange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_AlarmDCDchange_Type.__name__=_C
_AlarmDCDchange_Object=MibTableColumn
alarmDCDchange=_AlarmDCDchange_Object((1,3,6,1,4,1,8691,2,8,1,5,2,2,1,1,3),_AlarmDCDchange_Type())
alarmDCDchange.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmDCDchange.setStatus(_A)
class _SmsDCDchange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SmsDCDchange_Type.__name__=_C
_SmsDCDchange_Object=MibTableColumn
smsDCDchange=_SmsDCDchange_Object((1,3,6,1,4,1,8691,2,8,1,5,2,2,1,1,4),_SmsDCDchange_Type())
smsDCDchange.setMaxAccess(_B)
if mibBuilder.loadTexts:smsDCDchange.setStatus(_A)
class _MailDSRchange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_MailDSRchange_Type.__name__=_C
_MailDSRchange_Object=MibTableColumn
mailDSRchange=_MailDSRchange_Object((1,3,6,1,4,1,8691,2,8,1,5,2,2,1,1,5),_MailDSRchange_Type())
mailDSRchange.setMaxAccess(_B)
if mibBuilder.loadTexts:mailDSRchange.setStatus(_A)
class _TrapDSRchange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TrapDSRchange_Type.__name__=_C
_TrapDSRchange_Object=MibTableColumn
trapDSRchange=_TrapDSRchange_Object((1,3,6,1,4,1,8691,2,8,1,5,2,2,1,1,6),_TrapDSRchange_Type())
trapDSRchange.setMaxAccess(_B)
if mibBuilder.loadTexts:trapDSRchange.setStatus(_A)
class _AlarmDSRchange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_AlarmDSRchange_Type.__name__=_C
_AlarmDSRchange_Object=MibTableColumn
alarmDSRchange=_AlarmDSRchange_Object((1,3,6,1,4,1,8691,2,8,1,5,2,2,1,1,7),_AlarmDSRchange_Type())
alarmDSRchange.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmDSRchange.setStatus(_A)
class _SmsDSRchange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SmsDSRchange_Type.__name__=_C
_SmsDSRchange_Object=MibTableColumn
smsDSRchange=_SmsDSRchange_Object((1,3,6,1,4,1,8691,2,8,1,5,2,2,1,1,8),_SmsDSRchange_Type())
smsDSRchange.setMaxAccess(_B)
if mibBuilder.loadTexts:smsDSRchange.setStatus(_A)
_EmailAlert_ObjectIdentity=ObjectIdentity
emailAlert=_EmailAlert_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,2,3))
_EmailWarningMailServer_Type=DisplayString
_EmailWarningMailServer_Object=MibScalar
emailWarningMailServer=_EmailWarningMailServer_Object((1,3,6,1,4,1,8691,2,8,1,5,2,3,1),_EmailWarningMailServer_Type())
emailWarningMailServer.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningMailServer.setStatus(_A)
class _EmailRequiresAuthentication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('non-require',0),('require',1)))
_EmailRequiresAuthentication_Type.__name__=_C
_EmailRequiresAuthentication_Object=MibScalar
emailRequiresAuthentication=_EmailRequiresAuthentication_Object((1,3,6,1,4,1,8691,2,8,1,5,2,3,2),_EmailRequiresAuthentication_Type())
emailRequiresAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:emailRequiresAuthentication.setStatus(_A)
class _EmailWarningUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EmailWarningUserName_Type.__name__=_F
_EmailWarningUserName_Object=MibScalar
emailWarningUserName=_EmailWarningUserName_Object((1,3,6,1,4,1,8691,2,8,1,5,2,3,3),_EmailWarningUserName_Type())
emailWarningUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningUserName.setStatus(_A)
class _EmailWarningPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_EmailWarningPassword_Type.__name__=_F
_EmailWarningPassword_Object=MibScalar
emailWarningPassword=_EmailWarningPassword_Object((1,3,6,1,4,1,8691,2,8,1,5,2,3,4),_EmailWarningPassword_Type())
emailWarningPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningPassword.setStatus(_A)
_EmailWarningFromEmail_Type=DisplayString
_EmailWarningFromEmail_Object=MibScalar
emailWarningFromEmail=_EmailWarningFromEmail_Object((1,3,6,1,4,1,8691,2,8,1,5,2,3,5),_EmailWarningFromEmail_Type())
emailWarningFromEmail.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningFromEmail.setStatus(_A)
_EmailWarningFirstEmailAddr_Type=DisplayString
_EmailWarningFirstEmailAddr_Object=MibScalar
emailWarningFirstEmailAddr=_EmailWarningFirstEmailAddr_Object((1,3,6,1,4,1,8691,2,8,1,5,2,3,6),_EmailWarningFirstEmailAddr_Type())
emailWarningFirstEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningFirstEmailAddr.setStatus(_A)
_EmailWarningSecondEmailAddr_Type=DisplayString
_EmailWarningSecondEmailAddr_Object=MibScalar
emailWarningSecondEmailAddr=_EmailWarningSecondEmailAddr_Object((1,3,6,1,4,1,8691,2,8,1,5,2,3,7),_EmailWarningSecondEmailAddr_Type())
emailWarningSecondEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningSecondEmailAddr.setStatus(_A)
_EmailWarningThirdEmailAddr_Type=DisplayString
_EmailWarningThirdEmailAddr_Object=MibScalar
emailWarningThirdEmailAddr=_EmailWarningThirdEmailAddr_Object((1,3,6,1,4,1,8691,2,8,1,5,2,3,8),_EmailWarningThirdEmailAddr_Type())
emailWarningThirdEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningThirdEmailAddr.setStatus(_A)
_EmailWarningFourthEmailAddr_Type=DisplayString
_EmailWarningFourthEmailAddr_Object=MibScalar
emailWarningFourthEmailAddr=_EmailWarningFourthEmailAddr_Object((1,3,6,1,4,1,8691,2,8,1,5,2,3,9),_EmailWarningFourthEmailAddr_Type())
emailWarningFourthEmailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:emailWarningFourthEmailAddr.setStatus(_A)
_SnmpTrap_ObjectIdentity=ObjectIdentity
snmpTrap=_SnmpTrap_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,2,4))
_SnmpTrapReceiverIp_Type=DisplayString
_SnmpTrapReceiverIp_Object=MibScalar
snmpTrapReceiverIp=_SnmpTrapReceiverIp_Object((1,3,6,1,4,1,8691,2,8,1,5,2,4,1),_SnmpTrapReceiverIp_Type())
snmpTrapReceiverIp.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpTrapReceiverIp.setStatus(_A)
class _TrapVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('v1',0),('v2c',1)))
_TrapVersion_Type.__name__=_C
_TrapVersion_Object=MibScalar
trapVersion=_TrapVersion_Object((1,3,6,1,4,1,8691,2,8,1,5,2,4,2),_TrapVersion_Type())
trapVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:trapVersion.setStatus(_A)
_SmsAlert_ObjectIdentity=ObjectIdentity
smsAlert=_SmsAlert_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,2,5))
class _SmsAlertFirstPhoneNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SmsAlertFirstPhoneNumber_Type.__name__=_F
_SmsAlertFirstPhoneNumber_Object=MibScalar
smsAlertFirstPhoneNumber=_SmsAlertFirstPhoneNumber_Object((1,3,6,1,4,1,8691,2,8,1,5,2,5,1),_SmsAlertFirstPhoneNumber_Type())
smsAlertFirstPhoneNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:smsAlertFirstPhoneNumber.setStatus(_A)
class _SmsAlertSecondPhoneNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SmsAlertSecondPhoneNumber_Type.__name__=_F
_SmsAlertSecondPhoneNumber_Object=MibScalar
smsAlertSecondPhoneNumber=_SmsAlertSecondPhoneNumber_Object((1,3,6,1,4,1,8691,2,8,1,5,2,5,2),_SmsAlertSecondPhoneNumber_Type())
smsAlertSecondPhoneNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:smsAlertSecondPhoneNumber.setStatus(_A)
class _SmsAlertThirdPhoneNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SmsAlertThirdPhoneNumber_Type.__name__=_F
_SmsAlertThirdPhoneNumber_Object=MibScalar
smsAlertThirdPhoneNumber=_SmsAlertThirdPhoneNumber_Object((1,3,6,1,4,1,8691,2,8,1,5,2,5,3),_SmsAlertThirdPhoneNumber_Type())
smsAlertThirdPhoneNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:smsAlertThirdPhoneNumber.setStatus(_A)
class _SmsAlertFourthPhoneNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SmsAlertFourthPhoneNumber_Type.__name__=_F
_SmsAlertFourthPhoneNumber_Object=MibScalar
smsAlertFourthPhoneNumber=_SmsAlertFourthPhoneNumber_Object((1,3,6,1,4,1,8691,2,8,1,5,2,5,4),_SmsAlertFourthPhoneNumber_Type())
smsAlertFourthPhoneNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:smsAlertFourthPhoneNumber.setStatus(_A)
_EventLogSettings_ObjectIdentity=ObjectIdentity
eventLogSettings=_EventLogSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,2,6))
_CurrentLogCapacityRatio_Type=DisplayString
_CurrentLogCapacityRatio_Object=MibScalar
currentLogCapacityRatio=_CurrentLogCapacityRatio_Object((1,3,6,1,4,1,8691,2,8,1,5,2,6,1),_CurrentLogCapacityRatio_Type())
currentLogCapacityRatio.setMaxAccess(_G)
if mibBuilder.loadTexts:currentLogCapacityRatio.setStatus(_A)
class _LogCapacityWarningEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_LogCapacityWarningEnable_Type.__name__=_C
_LogCapacityWarningEnable_Object=MibScalar
logCapacityWarningEnable=_LogCapacityWarningEnable_Object((1,3,6,1,4,1,8691,2,8,1,5,2,6,2),_LogCapacityWarningEnable_Type())
logCapacityWarningEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:logCapacityWarningEnable.setStatus(_A)
class _LogCapacityWarningThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_LogCapacityWarningThreshold_Type.__name__=_C
_LogCapacityWarningThreshold_Object=MibScalar
logCapacityWarningThreshold=_LogCapacityWarningThreshold_Object((1,3,6,1,4,1,8691,2,8,1,5,2,6,3),_LogCapacityWarningThreshold_Type())
logCapacityWarningThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:logCapacityWarningThreshold.setStatus(_A)
class _MailLogCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_MailLogCapacity_Type.__name__=_C
_MailLogCapacity_Object=MibScalar
mailLogCapacity=_MailLogCapacity_Object((1,3,6,1,4,1,8691,2,8,1,5,2,6,4),_MailLogCapacity_Type())
mailLogCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:mailLogCapacity.setStatus(_A)
class _TrapLogCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TrapLogCapacity_Type.__name__=_C
_TrapLogCapacity_Object=MibScalar
trapLogCapacity=_TrapLogCapacity_Object((1,3,6,1,4,1,8691,2,8,1,5,2,6,5),_TrapLogCapacity_Type())
trapLogCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:trapLogCapacity.setStatus(_A)
class _LogOversizeAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('overwriteTheOldestEventLog',0),('stopRecordingEventLog',1)))
_LogOversizeAction_Type.__name__=_C
_LogOversizeAction_Object=MibScalar
logOversizeAction=_LogOversizeAction_Object((1,3,6,1,4,1,8691,2,8,1,5,2,6,6),_LogOversizeAction_Type())
logOversizeAction.setMaxAccess(_B)
if mibBuilder.loadTexts:logOversizeAction.setStatus(_A)
_Maintenance_ObjectIdentity=ObjectIdentity
maintenance=_Maintenance_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,3))
_ConsoleSettings_ObjectIdentity=ObjectIdentity
consoleSettings=_ConsoleSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,3,1))
class _HttpConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_HttpConsole_Type.__name__=_C
_HttpConsole_Object=MibScalar
httpConsole=_HttpConsole_Object((1,3,6,1,4,1,8691,2,8,1,5,3,1,1),_HttpConsole_Type())
httpConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:httpConsole.setStatus(_A)
class _HttpsConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_HttpsConsole_Type.__name__=_C
_HttpsConsole_Object=MibScalar
httpsConsole=_HttpsConsole_Object((1,3,6,1,4,1,8691,2,8,1,5,3,1,2),_HttpsConsole_Type())
httpsConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:httpsConsole.setStatus(_A)
class _TelnetConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TelnetConsole_Type.__name__=_C
_TelnetConsole_Object=MibScalar
telnetConsole=_TelnetConsole_Object((1,3,6,1,4,1,8691,2,8,1,5,3,1,3),_TelnetConsole_Type())
telnetConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:telnetConsole.setStatus(_A)
class _SshConsole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SshConsole_Type.__name__=_C
_SshConsole_Object=MibScalar
sshConsole=_SshConsole_Object((1,3,6,1,4,1,8691,2,8,1,5,3,1,4),_SshConsole_Type())
sshConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:sshConsole.setStatus(_A)
class _ConsoleAuthenticationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6)))
_ConsoleAuthenticationType_Type.__name__=_C
_ConsoleAuthenticationType_Object=MibScalar
consoleAuthenticationType=_ConsoleAuthenticationType_Object((1,3,6,1,4,1,8691,2,8,1,5,3,1,5),_ConsoleAuthenticationType_Type())
consoleAuthenticationType.setMaxAccess(_B)
if mibBuilder.loadTexts:consoleAuthenticationType.setStatus(_A)
class _TryNextTypeOnAuthDenied_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TryNextTypeOnAuthDenied_Type.__name__=_C
_TryNextTypeOnAuthDenied_Object=MibScalar
tryNextTypeOnAuthDenied=_TryNextTypeOnAuthDenied_Object((1,3,6,1,4,1,8691,2,8,1,5,3,1,6),_TryNextTypeOnAuthDenied_Type())
tryNextTypeOnAuthDenied.setMaxAccess(_B)
if mibBuilder.loadTexts:tryNextTypeOnAuthDenied.setStatus(_A)
class _ResetButtonFunction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable-after-60-sec',0),('always-enable',1)))
_ResetButtonFunction_Type.__name__=_C
_ResetButtonFunction_Object=MibScalar
resetButtonFunction=_ResetButtonFunction_Object((1,3,6,1,4,1,8691,2,8,1,5,3,1,7),_ResetButtonFunction_Type())
resetButtonFunction.setMaxAccess(_B)
if mibBuilder.loadTexts:resetButtonFunction.setStatus(_A)
class _LcmReadOnlyProtect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('readonly',0),('writable',1)))
_LcmReadOnlyProtect_Type.__name__=_C
_LcmReadOnlyProtect_Object=MibScalar
lcmReadOnlyProtect=_LcmReadOnlyProtect_Object((1,3,6,1,4,1,8691,2,8,1,5,3,1,8),_LcmReadOnlyProtect_Type())
lcmReadOnlyProtect.setMaxAccess(_B)
if mibBuilder.loadTexts:lcmReadOnlyProtect.setStatus(_A)
class _MaxHttpLoginUsers_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_MaxHttpLoginUsers_Type.__name__=_C
_MaxHttpLoginUsers_Object=MibScalar
maxHttpLoginUsers=_MaxHttpLoginUsers_Object((1,3,6,1,4,1,8691,2,8,1,5,3,1,9),_MaxHttpLoginUsers_Type())
maxHttpLoginUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:maxHttpLoginUsers.setStatus(_A)
class _AutoLogoutSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_AutoLogoutSetting_Type.__name__=_C
_AutoLogoutSetting_Object=MibScalar
autoLogoutSetting=_AutoLogoutSetting_Object((1,3,6,1,4,1,8691,2,8,1,5,3,1,10),_AutoLogoutSetting_Type())
autoLogoutSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:autoLogoutSetting.setStatus(_A)
_LoadFactoryDefault_ObjectIdentity=ObjectIdentity
loadFactoryDefault=_LoadFactoryDefault_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,3,2))
class _LoadFactoryDefaultSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('resetToFactoryDefault-ExcludingIpConfiguration',0),('resetToFactoryDefault',1)))
_LoadFactoryDefaultSetting_Type.__name__=_C
_LoadFactoryDefaultSetting_Object=MibScalar
loadFactoryDefaultSetting=_LoadFactoryDefaultSetting_Object((1,3,6,1,4,1,8691,2,8,1,5,3,2,1),_LoadFactoryDefaultSetting_Type())
loadFactoryDefaultSetting.setMaxAccess(_K)
if mibBuilder.loadTexts:loadFactoryDefaultSetting.setStatus(_A)
_AccountManagement_ObjectIdentity=ObjectIdentity
accountManagement=_AccountManagement_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,4))
_NotificationMessage_ObjectIdentity=ObjectIdentity
notificationMessage=_NotificationMessage_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,4,1))
class _LoginNotificationMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,240))
_LoginNotificationMessage_Type.__name__=_F
_LoginNotificationMessage_Object=MibScalar
loginNotificationMessage=_LoginNotificationMessage_Object((1,3,6,1,4,1,8691,2,8,1,5,4,1,1),_LoginNotificationMessage_Type())
loginNotificationMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:loginNotificationMessage.setStatus(_A)
class _LoginFailureMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,240))
_LoginFailureMessage_Type.__name__=_F
_LoginFailureMessage_Object=MibScalar
loginFailureMessage=_LoginFailureMessage_Object((1,3,6,1,4,1,8691,2,8,1,5,4,1,2),_LoginFailureMessage_Type())
loginFailureMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:loginFailureMessage.setStatus(_A)
_UserAccount_ObjectIdentity=ObjectIdentity
userAccount=_UserAccount_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,4,2))
_UserAccountTable_Object=MibTable
userAccountTable=_UserAccountTable_Object((1,3,6,1,4,1,8691,2,8,1,5,4,2,1))
if mibBuilder.loadTexts:userAccountTable.setStatus(_A)
_UserAccountEntry_Object=MibTableRow
userAccountEntry=_UserAccountEntry_Object((1,3,6,1,4,1,8691,2,8,1,5,4,2,1,1))
userAccountEntry.setIndexNames((0,_H,_A4))
if mibBuilder.loadTexts:userAccountEntry.setStatus(_A)
_UserAccountIndex_Type=Integer32
_UserAccountIndex_Object=MibTableColumn
userAccountIndex=_UserAccountIndex_Object((1,3,6,1,4,1,8691,2,8,1,5,4,2,1,1,1),_UserAccountIndex_Type())
userAccountIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:userAccountIndex.setStatus(_A)
class _ActiveUserAccount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('non_active',0),('avtive',1)))
_ActiveUserAccount_Type.__name__=_C
_ActiveUserAccount_Object=MibTableColumn
activeUserAccount=_ActiveUserAccount_Object((1,3,6,1,4,1,8691,2,8,1,5,4,2,1,1,2),_ActiveUserAccount_Type())
activeUserAccount.setMaxAccess(_B)
if mibBuilder.loadTexts:activeUserAccount.setStatus(_A)
class _AccountName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_AccountName_Type.__name__=_F
_AccountName_Object=MibTableColumn
accountName=_AccountName_Object((1,3,6,1,4,1,8691,2,8,1,5,4,2,1,1,3),_AccountName_Type())
accountName.setMaxAccess(_B)
if mibBuilder.loadTexts:accountName.setStatus(_A)
class _AccountGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_AccountGroupName_Type.__name__=_F
_AccountGroupName_Object=MibTableColumn
accountGroupName=_AccountGroupName_Object((1,3,6,1,4,1,8691,2,8,1,5,4,2,1,1,4),_AccountGroupName_Type())
accountGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:accountGroupName.setStatus(_A)
_AccessPermission_ObjectIdentity=ObjectIdentity
accessPermission=_AccessPermission_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,4,3))
_AccessPermissionTable_Object=MibTable
accessPermissionTable=_AccessPermissionTable_Object((1,3,6,1,4,1,8691,2,8,1,5,4,3,1))
if mibBuilder.loadTexts:accessPermissionTable.setStatus(_A)
_AccessPermissionEntry_Object=MibTableRow
accessPermissionEntry=_AccessPermissionEntry_Object((1,3,6,1,4,1,8691,2,8,1,5,4,3,1,1))
accessPermissionEntry.setIndexNames((0,_H,_A5))
if mibBuilder.loadTexts:accessPermissionEntry.setStatus(_A)
class _GroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_GroupName_Type.__name__=_F
_GroupName_Object=MibTableColumn
groupName=_GroupName_Object((1,3,6,1,4,1,8691,2,8,1,5,4,3,1,1,1),_GroupName_Type())
groupName.setMaxAccess(_B)
if mibBuilder.loadTexts:groupName.setStatus(_A)
class _NetworkConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_U,0),(_G,1),(_B,2)))
_NetworkConfig_Type.__name__=_C
_NetworkConfig_Object=MibTableColumn
networkConfig=_NetworkConfig_Object((1,3,6,1,4,1,8691,2,8,1,5,4,3,1,1,2),_NetworkConfig_Type())
networkConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:networkConfig.setStatus(_A)
class _SerialConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_U,0),(_G,1),(_B,2)))
_SerialConfig_Type.__name__=_C
_SerialConfig_Object=MibTableColumn
serialConfig=_SerialConfig_Object((1,3,6,1,4,1,8691,2,8,1,5,4,3,1,1,3),_SerialConfig_Type())
serialConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:serialConfig.setStatus(_A)
class _SystemConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_U,0),(_G,1),(_B,2)))
_SystemConfig_Type.__name__=_C
_SystemConfig_Object=MibTableColumn
systemConfig=_SystemConfig_Object((1,3,6,1,4,1,8691,2,8,1,5,4,3,1,1,4),_SystemConfig_Type())
systemConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:systemConfig.setStatus(_A)
class _AdminConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_U,0),(_G,1),(_B,2)))
_AdminConfig_Type.__name__=_C
_AdminConfig_Object=MibTableColumn
adminConfig=_AdminConfig_Object((1,3,6,1,4,1,8691,2,8,1,5,4,3,1,1,5),_AdminConfig_Type())
adminConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:adminConfig.setStatus(_A)
class _MonitorLogWarning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_U,0),(_G,1),(_B,2)))
_MonitorLogWarning_Type.__name__=_C
_MonitorLogWarning_Object=MibTableColumn
monitorLogWarning=_MonitorLogWarning_Object((1,3,6,1,4,1,8691,2,8,1,5,4,3,1,1,6),_MonitorLogWarning_Type())
monitorLogWarning.setMaxAccess(_B)
if mibBuilder.loadTexts:monitorLogWarning.setStatus(_A)
class _CommonSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_U,0),(_G,1),(_B,2)))
_CommonSetting_Type.__name__=_C
_CommonSetting_Object=MibTableColumn
commonSetting=_CommonSetting_Object((1,3,6,1,4,1,8691,2,8,1,5,4,3,1,1,7),_CommonSetting_Type())
commonSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:commonSetting.setStatus(_A)
_AccountPasswordAndLoginMgmt_ObjectIdentity=ObjectIdentity
accountPasswordAndLoginMgmt=_AccountPasswordAndLoginMgmt_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,4,4))
_AccountPasswordPolicy_ObjectIdentity=ObjectIdentity
accountPasswordPolicy=_AccountPasswordPolicy_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,4,4,1))
class _PwdMinLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,16))
_PwdMinLength_Type.__name__=_C
_PwdMinLength_Object=MibScalar
pwdMinLength=_PwdMinLength_Object((1,3,6,1,4,1,8691,2,8,1,5,4,4,1,1),_PwdMinLength_Type())
pwdMinLength.setMaxAccess(_B)
if mibBuilder.loadTexts:pwdMinLength.setStatus(_A)
class _PwdComplexityCheckEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PwdComplexityCheckEnable_Type.__name__=_C
_PwdComplexityCheckEnable_Object=MibScalar
pwdComplexityCheckEnable=_PwdComplexityCheckEnable_Object((1,3,6,1,4,1,8691,2,8,1,5,4,4,1,2),_PwdComplexityCheckEnable_Type())
pwdComplexityCheckEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:pwdComplexityCheckEnable.setStatus(_A)
class _PwdComplexityCheckDigitEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PwdComplexityCheckDigitEnable_Type.__name__=_C
_PwdComplexityCheckDigitEnable_Object=MibScalar
pwdComplexityCheckDigitEnable=_PwdComplexityCheckDigitEnable_Object((1,3,6,1,4,1,8691,2,8,1,5,4,4,1,3),_PwdComplexityCheckDigitEnable_Type())
pwdComplexityCheckDigitEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:pwdComplexityCheckDigitEnable.setStatus(_A)
class _PwdComplexityCheckAlphabetEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PwdComplexityCheckAlphabetEnable_Type.__name__=_C
_PwdComplexityCheckAlphabetEnable_Object=MibScalar
pwdComplexityCheckAlphabetEnable=_PwdComplexityCheckAlphabetEnable_Object((1,3,6,1,4,1,8691,2,8,1,5,4,4,1,4),_PwdComplexityCheckAlphabetEnable_Type())
pwdComplexityCheckAlphabetEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:pwdComplexityCheckAlphabetEnable.setStatus(_A)
class _PwdComplexityCheckSpecialCharEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_PwdComplexityCheckSpecialCharEnable_Type.__name__=_C
_PwdComplexityCheckSpecialCharEnable_Object=MibScalar
pwdComplexityCheckSpecialCharEnable=_PwdComplexityCheckSpecialCharEnable_Object((1,3,6,1,4,1,8691,2,8,1,5,4,4,1,5),_PwdComplexityCheckSpecialCharEnable_Type())
pwdComplexityCheckSpecialCharEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:pwdComplexityCheckSpecialCharEnable.setStatus(_A)
class _PwdLifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(90,180))
_PwdLifetime_Type.__name__=_C
_PwdLifetime_Object=MibScalar
pwdLifetime=_PwdLifetime_Object((1,3,6,1,4,1,8691,2,8,1,5,4,4,1,6),_PwdLifetime_Type())
pwdLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:pwdLifetime.setStatus(_A)
_AccountLoginFailureLockout_ObjectIdentity=ObjectIdentity
accountLoginFailureLockout=_AccountLoginFailureLockout_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,5,4,4,2))
class _LoginFailureLockoutEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_LoginFailureLockoutEnable_Type.__name__=_C
_LoginFailureLockoutEnable_Object=MibScalar
loginFailureLockoutEnable=_LoginFailureLockoutEnable_Object((1,3,6,1,4,1,8691,2,8,1,5,4,4,2,1),_LoginFailureLockoutEnable_Type())
loginFailureLockoutEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:loginFailureLockoutEnable.setStatus(_A)
class _LoginFailureLockoutRetrys_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_LoginFailureLockoutRetrys_Type.__name__=_C
_LoginFailureLockoutRetrys_Object=MibScalar
loginFailureLockoutRetrys=_LoginFailureLockoutRetrys_Object((1,3,6,1,4,1,8691,2,8,1,5,4,4,2,2),_LoginFailureLockoutRetrys_Type())
loginFailureLockoutRetrys.setMaxAccess(_B)
if mibBuilder.loadTexts:loginFailureLockoutRetrys.setStatus(_A)
class _LoginFailureLockoutTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_LoginFailureLockoutTime_Type.__name__=_C
_LoginFailureLockoutTime_Object=MibScalar
loginFailureLockoutTime=_LoginFailureLockoutTime_Object((1,3,6,1,4,1,8691,2,8,1,5,4,4,2,3),_LoginFailureLockoutTime_Type())
loginFailureLockoutTime.setMaxAccess(_B)
if mibBuilder.loadTexts:loginFailureLockoutTime.setStatus(_A)
_SysStatus_ObjectIdentity=ObjectIdentity
sysStatus=_SysStatus_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,6))
_S2eConnections_ObjectIdentity=ObjectIdentity
s2eConnections=_S2eConnections_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,6,1))
_MonitorRemoteIpTable_Object=MibTable
monitorRemoteIpTable=_MonitorRemoteIpTable_Object((1,3,6,1,4,1,8691,2,8,1,6,1,1))
if mibBuilder.loadTexts:monitorRemoteIpTable.setStatus(_A)
_MonitorRemoteIpEntry_Object=MibTableRow
monitorRemoteIpEntry=_MonitorRemoteIpEntry_Object((1,3,6,1,4,1,8691,2,8,1,6,1,1,1))
monitorRemoteIpEntry.setIndexNames((0,_H,_I),(0,_H,_A6))
if mibBuilder.loadTexts:monitorRemoteIpEntry.setStatus(_A)
_RemoteIpIndex_Type=Integer32
_RemoteIpIndex_Object=MibTableColumn
remoteIpIndex=_RemoteIpIndex_Object((1,3,6,1,4,1,8691,2,8,1,6,1,1,1,1),_RemoteIpIndex_Type())
remoteIpIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:remoteIpIndex.setStatus(_A)
_MonitorRemoteIp_Type=DisplayString
_MonitorRemoteIp_Object=MibTableColumn
monitorRemoteIp=_MonitorRemoteIp_Object((1,3,6,1,4,1,8691,2,8,1,6,1,1,1,2),_MonitorRemoteIp_Type())
monitorRemoteIp.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorRemoteIp.setStatus(_A)
_MonitorCipher_Type=DisplayString
_MonitorCipher_Object=MibTableColumn
monitorCipher=_MonitorCipher_Object((1,3,6,1,4,1,8691,2,8,1,6,1,1,1,3),_MonitorCipher_Type())
monitorCipher.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorCipher.setStatus(_A)
_SerialPortStatus_ObjectIdentity=ObjectIdentity
serialPortStatus=_SerialPortStatus_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,6,2))
_MonitorSerialPortStatusTable_Object=MibTable
monitorSerialPortStatusTable=_MonitorSerialPortStatusTable_Object((1,3,6,1,4,1,8691,2,8,1,6,2,1))
if mibBuilder.loadTexts:monitorSerialPortStatusTable.setStatus(_A)
_MonitorSerialPortStatusEntry_Object=MibTableRow
monitorSerialPortStatusEntry=_MonitorSerialPortStatusEntry_Object((1,3,6,1,4,1,8691,2,8,1,6,2,1,1))
monitorSerialPortStatusEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:monitorSerialPortStatusEntry.setStatus(_A)
_MonitorTxCount_Type=Integer32
_MonitorTxCount_Object=MibTableColumn
monitorTxCount=_MonitorTxCount_Object((1,3,6,1,4,1,8691,2,8,1,6,2,1,1,1),_MonitorTxCount_Type())
monitorTxCount.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorTxCount.setStatus(_A)
_MonitorRxCount_Type=Integer32
_MonitorRxCount_Object=MibTableColumn
monitorRxCount=_MonitorRxCount_Object((1,3,6,1,4,1,8691,2,8,1,6,2,1,1,2),_MonitorRxCount_Type())
monitorRxCount.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorRxCount.setStatus(_A)
_MonitorTxTotalCount_Type=Integer32
_MonitorTxTotalCount_Object=MibTableColumn
monitorTxTotalCount=_MonitorTxTotalCount_Object((1,3,6,1,4,1,8691,2,8,1,6,2,1,1,3),_MonitorTxTotalCount_Type())
monitorTxTotalCount.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorTxTotalCount.setStatus(_A)
_MonitorRxTotalCount_Type=Integer32
_MonitorRxTotalCount_Object=MibTableColumn
monitorRxTotalCount=_MonitorRxTotalCount_Object((1,3,6,1,4,1,8691,2,8,1,6,2,1,1,4),_MonitorRxTotalCount_Type())
monitorRxTotalCount.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorRxTotalCount.setStatus(_A)
class _MonitorDSR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_MonitorDSR_Type.__name__=_C
_MonitorDSR_Object=MibTableColumn
monitorDSR=_MonitorDSR_Object((1,3,6,1,4,1,8691,2,8,1,6,2,1,1,5),_MonitorDSR_Type())
monitorDSR.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorDSR.setStatus(_A)
class _MonitorDTR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_MonitorDTR_Type.__name__=_C
_MonitorDTR_Object=MibTableColumn
monitorDTR=_MonitorDTR_Object((1,3,6,1,4,1,8691,2,8,1,6,2,1,1,6),_MonitorDTR_Type())
monitorDTR.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorDTR.setStatus(_A)
class _MonitorRTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_MonitorRTS_Type.__name__=_C
_MonitorRTS_Object=MibTableColumn
monitorRTS=_MonitorRTS_Object((1,3,6,1,4,1,8691,2,8,1,6,2,1,1,7),_MonitorRTS_Type())
monitorRTS.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorRTS.setStatus(_A)
class _MonitorCTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_MonitorCTS_Type.__name__=_C
_MonitorCTS_Object=MibTableColumn
monitorCTS=_MonitorCTS_Object((1,3,6,1,4,1,8691,2,8,1,6,2,1,1,8),_MonitorCTS_Type())
monitorCTS.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorCTS.setStatus(_A)
class _MonitorDCD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_MonitorDCD_Type.__name__=_C
_MonitorDCD_Object=MibTableColumn
monitorDCD=_MonitorDCD_Object((1,3,6,1,4,1,8691,2,8,1,6,2,1,1,9),_MonitorDCD_Type())
monitorDCD.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorDCD.setStatus(_A)
_SerialPortErrorCount_ObjectIdentity=ObjectIdentity
serialPortErrorCount=_SerialPortErrorCount_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,6,3))
_MonitorSerialPortErrorCountTable_Object=MibTable
monitorSerialPortErrorCountTable=_MonitorSerialPortErrorCountTable_Object((1,3,6,1,4,1,8691,2,8,1,6,3,1))
if mibBuilder.loadTexts:monitorSerialPortErrorCountTable.setStatus(_A)
_MonitorSerialPortErrorCountEntry_Object=MibTableRow
monitorSerialPortErrorCountEntry=_MonitorSerialPortErrorCountEntry_Object((1,3,6,1,4,1,8691,2,8,1,6,3,1,1))
monitorSerialPortErrorCountEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:monitorSerialPortErrorCountEntry.setStatus(_A)
_MonitorErrorCountFrame_Type=Integer32
_MonitorErrorCountFrame_Object=MibTableColumn
monitorErrorCountFrame=_MonitorErrorCountFrame_Object((1,3,6,1,4,1,8691,2,8,1,6,3,1,1,1),_MonitorErrorCountFrame_Type())
monitorErrorCountFrame.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorErrorCountFrame.setStatus(_A)
_MonitorErrorCountParity_Type=Integer32
_MonitorErrorCountParity_Object=MibTableColumn
monitorErrorCountParity=_MonitorErrorCountParity_Object((1,3,6,1,4,1,8691,2,8,1,6,3,1,1,2),_MonitorErrorCountParity_Type())
monitorErrorCountParity.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorErrorCountParity.setStatus(_A)
_MonitorErrorCountOverrun_Type=Integer32
_MonitorErrorCountOverrun_Object=MibTableColumn
monitorErrorCountOverrun=_MonitorErrorCountOverrun_Object((1,3,6,1,4,1,8691,2,8,1,6,3,1,1,3),_MonitorErrorCountOverrun_Type())
monitorErrorCountOverrun.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorErrorCountOverrun.setStatus(_A)
_MonitorErrorCountBreak_Type=Integer32
_MonitorErrorCountBreak_Object=MibTableColumn
monitorErrorCountBreak=_MonitorErrorCountBreak_Object((1,3,6,1,4,1,8691,2,8,1,6,3,1,1,4),_MonitorErrorCountBreak_Type())
monitorErrorCountBreak.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorErrorCountBreak.setStatus(_A)
_SerialPortSettings_ObjectIdentity=ObjectIdentity
serialPortSettings=_SerialPortSettings_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,6,4))
_MonitorSerialPortSettingsTable_Object=MibTable
monitorSerialPortSettingsTable=_MonitorSerialPortSettingsTable_Object((1,3,6,1,4,1,8691,2,8,1,6,4,1))
if mibBuilder.loadTexts:monitorSerialPortSettingsTable.setStatus(_A)
_MonitorSerialPortSettingsEntry_Object=MibTableRow
monitorSerialPortSettingsEntry=_MonitorSerialPortSettingsEntry_Object((1,3,6,1,4,1,8691,2,8,1,6,4,1,1))
monitorSerialPortSettingsEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:monitorSerialPortSettingsEntry.setStatus(_A)
_MonitorBaudRate_Type=Integer32
_MonitorBaudRate_Object=MibTableColumn
monitorBaudRate=_MonitorBaudRate_Object((1,3,6,1,4,1,8691,2,8,1,6,4,1,1,1),_MonitorBaudRate_Type())
monitorBaudRate.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorBaudRate.setStatus(_A)
class _MonitorDataBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_x,0),(_y,1),(_z,2),('bits-8',3)))
_MonitorDataBits_Type.__name__=_C
_MonitorDataBits_Object=MibTableColumn
monitorDataBits=_MonitorDataBits_Object((1,3,6,1,4,1,8691,2,8,1,6,4,1,1,2),_MonitorDataBits_Type())
monitorDataBits.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorDataBits.setStatus(_A)
_MonitorStopBits_Type=DisplayString
_MonitorStopBits_Object=MibTableColumn
monitorStopBits=_MonitorStopBits_Object((1,3,6,1,4,1,8691,2,8,1,6,4,1,1,3),_MonitorStopBits_Type())
monitorStopBits.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorStopBits.setStatus(_A)
class _MonitorParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,8,24,40,56)));namedValues=NamedValues(*((_J,0),('odd',8),('even',24),('mark',40),('space',56)))
_MonitorParity_Type.__name__=_C
_MonitorParity_Object=MibTableColumn
monitorParity=_MonitorParity_Object((1,3,6,1,4,1,8691,2,8,1,6,4,1,1,4),_MonitorParity_Type())
monitorParity.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorParity.setStatus(_A)
class _MonitorRTSCTSFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_MonitorRTSCTSFlowControl_Type.__name__=_C
_MonitorRTSCTSFlowControl_Object=MibTableColumn
monitorRTSCTSFlowControl=_MonitorRTSCTSFlowControl_Object((1,3,6,1,4,1,8691,2,8,1,6,4,1,1,5),_MonitorRTSCTSFlowControl_Type())
monitorRTSCTSFlowControl.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorRTSCTSFlowControl.setStatus(_A)
class _MonitorXONXOFFFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_MonitorXONXOFFFlowControl_Type.__name__=_C
_MonitorXONXOFFFlowControl_Object=MibTableColumn
monitorXONXOFFFlowControl=_MonitorXONXOFFFlowControl_Object((1,3,6,1,4,1,8691,2,8,1,6,4,1,1,6),_MonitorXONXOFFFlowControl_Type())
monitorXONXOFFFlowControl.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorXONXOFFFlowControl.setStatus(_A)
class _MonitorDTRDSRFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_MonitorDTRDSRFlowControl_Type.__name__=_C
_MonitorDTRDSRFlowControl_Object=MibTableColumn
monitorDTRDSRFlowControl=_MonitorDTRDSRFlowControl_Object((1,3,6,1,4,1,8691,2,8,1,6,4,1,1,7),_MonitorDTRDSRFlowControl_Type())
monitorDTRDSRFlowControl.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorDTRDSRFlowControl.setStatus(_A)
class _MonitorRTSToggleFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_MonitorRTSToggleFlowControl_Type.__name__=_C
_MonitorRTSToggleFlowControl_Object=MibTableColumn
monitorRTSToggleFlowControl=_MonitorRTSToggleFlowControl_Object((1,3,6,1,4,1,8691,2,8,1,6,4,1,1,8),_MonitorRTSToggleFlowControl_Type())
monitorRTSToggleFlowControl.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorRTSToggleFlowControl.setStatus(_A)
class _MonitorFIFO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_MonitorFIFO_Type.__name__=_C
_MonitorFIFO_Object=MibTableColumn
monitorFIFO=_MonitorFIFO_Object((1,3,6,1,4,1,8691,2,8,1,6,4,1,1,9),_MonitorFIFO_Type())
monitorFIFO.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorFIFO.setStatus(_A)
class _MonitorInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_t,0),(_u,1),(_v,2),(_w,3)))
_MonitorInterface_Type.__name__=_C
_MonitorInterface_Object=MibTableColumn
monitorInterface=_MonitorInterface_Object((1,3,6,1,4,1,8691,2,8,1,6,4,1,1,10),_MonitorInterface_Type())
monitorInterface.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorInterface.setStatus(_A)
_SerialPortBuffering_ObjectIdentity=ObjectIdentity
serialPortBuffering=_SerialPortBuffering_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,6,5))
_MonitorSerialPortBufferingTable_Object=MibTable
monitorSerialPortBufferingTable=_MonitorSerialPortBufferingTable_Object((1,3,6,1,4,1,8691,2,8,1,6,5,1))
if mibBuilder.loadTexts:monitorSerialPortBufferingTable.setStatus(_A)
_MonitorSerialPortBufferingEntry_Object=MibTableRow
monitorSerialPortBufferingEntry=_MonitorSerialPortBufferingEntry_Object((1,3,6,1,4,1,8691,2,8,1,6,5,1,1))
monitorSerialPortBufferingEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:monitorSerialPortBufferingEntry.setStatus(_A)
_MonitorBuffering_Type=Integer32
_MonitorBuffering_Object=MibTableColumn
monitorBuffering=_MonitorBuffering_Object((1,3,6,1,4,1,8691,2,8,1,6,5,1,1,1),_MonitorBuffering_Type())
monitorBuffering.setMaxAccess(_G)
if mibBuilder.loadTexts:monitorBuffering.setStatus(_A)
_RelayOutputStatus_ObjectIdentity=ObjectIdentity
relayOutputStatus=_RelayOutputStatus_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,6,6))
class _RelayOutputEthernet1LinkDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_V,1),(_W,2)))
_RelayOutputEthernet1LinkDown_Type.__name__=_C
_RelayOutputEthernet1LinkDown_Object=MibScalar
relayOutputEthernet1LinkDown=_RelayOutputEthernet1LinkDown_Object((1,3,6,1,4,1,8691,2,8,1,6,6,1),_RelayOutputEthernet1LinkDown_Type())
relayOutputEthernet1LinkDown.setMaxAccess(_G)
if mibBuilder.loadTexts:relayOutputEthernet1LinkDown.setStatus(_A)
class _Ethernet1LinkDownAcknowledge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues((_X,0))
_Ethernet1LinkDownAcknowledge_Type.__name__=_C
_Ethernet1LinkDownAcknowledge_Object=MibScalar
ethernet1LinkDownAcknowledge=_Ethernet1LinkDownAcknowledge_Object((1,3,6,1,4,1,8691,2,8,1,6,6,2),_Ethernet1LinkDownAcknowledge_Type())
ethernet1LinkDownAcknowledge.setMaxAccess(_K)
if mibBuilder.loadTexts:ethernet1LinkDownAcknowledge.setStatus(_A)
class _RelayOutputEthernet2LinkDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_V,1),(_W,2)))
_RelayOutputEthernet2LinkDown_Type.__name__=_C
_RelayOutputEthernet2LinkDown_Object=MibScalar
relayOutputEthernet2LinkDown=_RelayOutputEthernet2LinkDown_Object((1,3,6,1,4,1,8691,2,8,1,6,6,3),_RelayOutputEthernet2LinkDown_Type())
relayOutputEthernet2LinkDown.setMaxAccess(_G)
if mibBuilder.loadTexts:relayOutputEthernet2LinkDown.setStatus(_A)
class _Ethernet2LinkDownAcknowledge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues((_X,0))
_Ethernet2LinkDownAcknowledge_Type.__name__=_C
_Ethernet2LinkDownAcknowledge_Object=MibScalar
ethernet2LinkDownAcknowledge=_Ethernet2LinkDownAcknowledge_Object((1,3,6,1,4,1,8691,2,8,1,6,6,4),_Ethernet2LinkDownAcknowledge_Type())
ethernet2LinkDownAcknowledge.setMaxAccess(_K)
if mibBuilder.loadTexts:ethernet2LinkDownAcknowledge.setStatus(_A)
class _RelayOutputEthernet3LinkDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_V,1),(_W,2)))
_RelayOutputEthernet3LinkDown_Type.__name__=_C
_RelayOutputEthernet3LinkDown_Object=MibScalar
relayOutputEthernet3LinkDown=_RelayOutputEthernet3LinkDown_Object((1,3,6,1,4,1,8691,2,8,1,6,6,5),_RelayOutputEthernet3LinkDown_Type())
relayOutputEthernet3LinkDown.setMaxAccess(_G)
if mibBuilder.loadTexts:relayOutputEthernet3LinkDown.setStatus(_A)
class _Ethernet3LinkDownAcknowledge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues((_X,0))
_Ethernet3LinkDownAcknowledge_Type.__name__=_C
_Ethernet3LinkDownAcknowledge_Object=MibScalar
ethernet3LinkDownAcknowledge=_Ethernet3LinkDownAcknowledge_Object((1,3,6,1,4,1,8691,2,8,1,6,6,6),_Ethernet3LinkDownAcknowledge_Type())
ethernet3LinkDownAcknowledge.setMaxAccess(_K)
if mibBuilder.loadTexts:ethernet3LinkDownAcknowledge.setStatus(_A)
_PortDCDChangedStatusTable_Object=MibTable
portDCDChangedStatusTable=_PortDCDChangedStatusTable_Object((1,3,6,1,4,1,8691,2,8,1,6,6,7))
if mibBuilder.loadTexts:portDCDChangedStatusTable.setStatus(_A)
_PortDCDChangedStatusEntry_Object=MibTableRow
portDCDChangedStatusEntry=_PortDCDChangedStatusEntry_Object((1,3,6,1,4,1,8691,2,8,1,6,6,7,1))
portDCDChangedStatusEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:portDCDChangedStatusEntry.setStatus(_A)
class _PortDCDChangedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_V,1),(_W,2)))
_PortDCDChangedStatus_Type.__name__=_C
_PortDCDChangedStatus_Object=MibTableColumn
portDCDChangedStatus=_PortDCDChangedStatus_Object((1,3,6,1,4,1,8691,2,8,1,6,6,7,1,1),_PortDCDChangedStatus_Type())
portDCDChangedStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:portDCDChangedStatus.setStatus(_A)
class _PortDCDChangedAcknowledge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues((_X,0))
_PortDCDChangedAcknowledge_Type.__name__=_C
_PortDCDChangedAcknowledge_Object=MibTableColumn
portDCDChangedAcknowledge=_PortDCDChangedAcknowledge_Object((1,3,6,1,4,1,8691,2,8,1,6,6,7,1,2),_PortDCDChangedAcknowledge_Type())
portDCDChangedAcknowledge.setMaxAccess(_K)
if mibBuilder.loadTexts:portDCDChangedAcknowledge.setStatus(_A)
_PortDSRChangedStatusTable_Object=MibTable
portDSRChangedStatusTable=_PortDSRChangedStatusTable_Object((1,3,6,1,4,1,8691,2,8,1,6,6,8))
if mibBuilder.loadTexts:portDSRChangedStatusTable.setStatus(_A)
_PortDSRChangedStatusEntry_Object=MibTableRow
portDSRChangedStatusEntry=_PortDSRChangedStatusEntry_Object((1,3,6,1,4,1,8691,2,8,1,6,6,8,1))
portDSRChangedStatusEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:portDSRChangedStatusEntry.setStatus(_A)
class _PortDSRChangedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_V,1),(_W,2)))
_PortDSRChangedStatus_Type.__name__=_C
_PortDSRChangedStatus_Object=MibTableColumn
portDSRChangedStatus=_PortDSRChangedStatus_Object((1,3,6,1,4,1,8691,2,8,1,6,6,8,1,1),_PortDSRChangedStatus_Type())
portDSRChangedStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:portDSRChangedStatus.setStatus(_A)
class _PortDSRChangedAcknowledge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues((_X,0))
_PortDSRChangedAcknowledge_Type.__name__=_C
_PortDSRChangedAcknowledge_Object=MibTableColumn
portDSRChangedAcknowledge=_PortDSRChangedAcknowledge_Object((1,3,6,1,4,1,8691,2,8,1,6,6,8,1,2),_PortDSRChangedAcknowledge_Type())
portDSRChangedAcknowledge.setMaxAccess(_K)
if mibBuilder.loadTexts:portDSRChangedAcknowledge.setStatus(_A)
_ModuleStatus_ObjectIdentity=ObjectIdentity
moduleStatus=_ModuleStatus_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,6,7))
_RedundancyStatus_ObjectIdentity=ObjectIdentity
redundancyStatus=_RedundancyStatus_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,6,7,1))
class _ActiveRedundancyProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_J,0),(_a,1),(_b,2),(_c,3)))
_ActiveRedundancyProtocol_Type.__name__=_C
_ActiveRedundancyProtocol_Object=MibScalar
activeRedundancyProtocol=_ActiveRedundancyProtocol_Object((1,3,6,1,4,1,8691,2,8,1,6,7,1,1),_ActiveRedundancyProtocol_Type())
activeRedundancyProtocol.setMaxAccess(_G)
if mibBuilder.loadTexts:activeRedundancyProtocol.setStatus(_A)
_SpanningTreeStatus_ObjectIdentity=ObjectIdentity
spanningTreeStatus=_SpanningTreeStatus_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,6,7,1,2))
_SpanningTreeBridgeRole_Type=DisplayString
_SpanningTreeBridgeRole_Object=MibScalar
spanningTreeBridgeRole=_SpanningTreeBridgeRole_Object((1,3,6,1,4,1,8691,2,8,1,6,7,1,2,1),_SpanningTreeBridgeRole_Type())
spanningTreeBridgeRole.setMaxAccess(_G)
if mibBuilder.loadTexts:spanningTreeBridgeRole.setStatus(_A)
_SpanningTreeRootBridge_Type=DisplayString
_SpanningTreeRootBridge_Object=MibScalar
spanningTreeRootBridge=_SpanningTreeRootBridge_Object((1,3,6,1,4,1,8691,2,8,1,6,7,1,2,2),_SpanningTreeRootBridge_Type())
spanningTreeRootBridge.setMaxAccess(_G)
if mibBuilder.loadTexts:spanningTreeRootBridge.setStatus(_A)
_SpanningTreeRootPathCost_Type=DisplayString
_SpanningTreeRootPathCost_Object=MibScalar
spanningTreeRootPathCost=_SpanningTreeRootPathCost_Object((1,3,6,1,4,1,8691,2,8,1,6,7,1,2,3),_SpanningTreeRootPathCost_Type())
spanningTreeRootPathCost.setMaxAccess(_G)
if mibBuilder.loadTexts:spanningTreeRootPathCost.setStatus(_A)
_SpanningTreePortStatusTable_Object=MibTable
spanningTreePortStatusTable=_SpanningTreePortStatusTable_Object((1,3,6,1,4,1,8691,2,8,1,6,7,1,2,4))
if mibBuilder.loadTexts:spanningTreePortStatusTable.setStatus(_A)
_SpanningTreePortStatusEntry_Object=MibTableRow
spanningTreePortStatusEntry=_SpanningTreePortStatusEntry_Object((1,3,6,1,4,1,8691,2,8,1,6,7,1,2,4,1))
spanningTreePortStatusEntry.setIndexNames((0,_H,_A7))
if mibBuilder.loadTexts:spanningTreePortStatusEntry.setStatus(_A)
_SpanningTreePortStatusIndex_Type=Integer32
_SpanningTreePortStatusIndex_Object=MibTableColumn
spanningTreePortStatusIndex=_SpanningTreePortStatusIndex_Object((1,3,6,1,4,1,8691,2,8,1,6,7,1,2,4,1,1),_SpanningTreePortStatusIndex_Type())
spanningTreePortStatusIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:spanningTreePortStatusIndex.setStatus(_A)
class _SpanningTreePortEnableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SpanningTreePortEnableStatus_Type.__name__=_C
_SpanningTreePortEnableStatus_Object=MibTableColumn
spanningTreePortEnableStatus=_SpanningTreePortEnableStatus_Object((1,3,6,1,4,1,8691,2,8,1,6,7,1,2,4,1,2),_SpanningTreePortEnableStatus_Type())
spanningTreePortEnableStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:spanningTreePortEnableStatus.setStatus(_A)
_SpanningTreePortRole_Type=DisplayString
_SpanningTreePortRole_Object=MibTableColumn
spanningTreePortRole=_SpanningTreePortRole_Object((1,3,6,1,4,1,8691,2,8,1,6,7,1,2,4,1,3),_SpanningTreePortRole_Type())
spanningTreePortRole.setMaxAccess(_G)
if mibBuilder.loadTexts:spanningTreePortRole.setStatus(_A)
_SpanningTreePortDesignatedBridge_Type=DisplayString
_SpanningTreePortDesignatedBridge_Object=MibTableColumn
spanningTreePortDesignatedBridge=_SpanningTreePortDesignatedBridge_Object((1,3,6,1,4,1,8691,2,8,1,6,7,1,2,4,1,4),_SpanningTreePortDesignatedBridge_Type())
spanningTreePortDesignatedBridge.setMaxAccess(_G)
if mibBuilder.loadTexts:spanningTreePortDesignatedBridge.setStatus(_A)
_SpanningTreePortStatus_Type=DisplayString
_SpanningTreePortStatus_Object=MibTableColumn
spanningTreePortStatus=_SpanningTreePortStatus_Object((1,3,6,1,4,1,8691,2,8,1,6,7,1,2,4,1,5),_SpanningTreePortStatus_Type())
spanningTreePortStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:spanningTreePortStatus.setStatus(_A)
_TurboRingStatus_ObjectIdentity=ObjectIdentity
turboRingStatus=_TurboRingStatus_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,6,7,1,3))
class _TurboRingBrokenStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('notTurboRingV2',0),('healthy',1),('break',2)))
_TurboRingBrokenStatus_Type.__name__=_C
_TurboRingBrokenStatus_Object=MibScalar
turboRingBrokenStatus=_TurboRingBrokenStatus_Object((1,3,6,1,4,1,8691,2,8,1,6,7,1,3,1),_TurboRingBrokenStatus_Type())
turboRingBrokenStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:turboRingBrokenStatus.setStatus(_A)
class _TurboRingMaster_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),(_d,1)))
_TurboRingMaster_Type.__name__=_C
_TurboRingMaster_Object=MibScalar
turboRingMaster=_TurboRingMaster_Object((1,3,6,1,4,1,8691,2,8,1,6,7,1,3,2),_TurboRingMaster_Type())
turboRingMaster.setMaxAccess(_G)
if mibBuilder.loadTexts:turboRingMaster.setStatus(_A)
_TurboRingPort1_Type=Integer32
_TurboRingPort1_Object=MibScalar
turboRingPort1=_TurboRingPort1_Object((1,3,6,1,4,1,8691,2,8,1,6,7,1,3,3),_TurboRingPort1_Type())
turboRingPort1.setMaxAccess(_G)
if mibBuilder.loadTexts:turboRingPort1.setStatus(_A)
_TurboRingPort2_Type=Integer32
_TurboRingPort2_Object=MibScalar
turboRingPort2=_TurboRingPort2_Object((1,3,6,1,4,1,8691,2,8,1,6,7,1,3,4),_TurboRingPort2_Type())
turboRingPort2.setMaxAccess(_G)
if mibBuilder.loadTexts:turboRingPort2.setStatus(_A)
_TurboRingPort1Status_Type=DisplayString
_TurboRingPort1Status_Object=MibScalar
turboRingPort1Status=_TurboRingPort1Status_Object((1,3,6,1,4,1,8691,2,8,1,6,7,1,3,5),_TurboRingPort1Status_Type())
turboRingPort1Status.setMaxAccess(_G)
if mibBuilder.loadTexts:turboRingPort1Status.setStatus(_A)
_TurboRingPort2Status_Type=DisplayString
_TurboRingPort2Status_Object=MibScalar
turboRingPort2Status=_TurboRingPort2Status_Object((1,3,6,1,4,1,8691,2,8,1,6,7,1,3,6),_TurboRingPort2Status_Type())
turboRingPort2Status.setMaxAccess(_G)
if mibBuilder.loadTexts:turboRingPort2Status.setStatus(_A)
_SaveConfiguration_ObjectIdentity=ObjectIdentity
saveConfiguration=_SaveConfiguration_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,7))
class _SaveConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('save',1))
_SaveConfig_Type.__name__=_C
_SaveConfig_Object=MibScalar
saveConfig=_SaveConfig_Object((1,3,6,1,4,1,8691,2,8,1,7,1),_SaveConfig_Type())
saveConfig.setMaxAccess(_K)
if mibBuilder.loadTexts:saveConfig.setStatus(_A)
_Restart_ObjectIdentity=ObjectIdentity
restart=_Restart_ObjectIdentity((1,3,6,1,4,1,8691,2,8,1,8))
class _RestartPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)));namedValues=NamedValues(*(('port1',0),('port2',1),('port3',2),('port4',3),('port5',4),('port6',5),('port7',6),('port8',7),('port9',8),('port10',9),('port11',10),('port12',11),('port13',12),('port14',13),('port15',14),('port16',15),('port17',16),('port18',17),('port19',18),('port20',19),('port21',20),('port22',21),('port23',22),('port24',23),('port25',24),('port26',25),('port27',26),('port28',27),('port29',28),('port30',29),('port31',30),('port32',31)))
_RestartPorts_Type.__name__=_C
_RestartPorts_Object=MibScalar
restartPorts=_RestartPorts_Object((1,3,6,1,4,1,8691,2,8,1,8,1),_RestartPorts_Type())
restartPorts.setMaxAccess(_K)
if mibBuilder.loadTexts:restartPorts.setStatus(_A)
class _RestartSystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('restart',1))
_RestartSystem_Type.__name__=_C
_RestartSystem_Object=MibScalar
restartSystem=_RestartSystem_Object((1,3,6,1,4,1,8691,2,8,1,8,2),_RestartSystem_Type())
restartSystem.setMaxAccess(_K)
if mibBuilder.loadTexts:restartSystem.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'PortList':PortList,'moxa':moxa,'nport':nport,'np6000':np6000,'swMgmt':swMgmt,'overview':overview,'modelName':modelName,'serialNumber':serialNumber,'firmwareVersion':firmwareVersion,'macAddress':macAddress,'viewLanSpeed':viewLanSpeed,'viewLanModuleSpeed':viewLanModuleSpeed,'upTime':upTime,'moduleType':moduleType,'moduleApVersion':moduleApVersion,'viewIpv4Address':viewIpv4Address,'viewIpv6LinkLocalAddress':viewIpv6LinkLocalAddress,'viewIpv6GlobalAddress':viewIpv6GlobalAddress,'basicSetting':basicSetting,'serverSetting':serverSetting,'serverName':serverName,'serverLocation':serverLocation,'timeSetting':timeSetting,'timeZone':timeZone,'localTime':localTime,'timeServer':timeServer,'networkSetting':networkSetting,'ipv4Configuration':ipv4Configuration,'ipv4Address':ipv4Address,'ipv4NetMask':ipv4NetMask,'ipv4DefaultGateway':ipv4DefaultGateway,'ipv4DnsServer1IpAddr':ipv4DnsServer1IpAddr,'ipv4DnsServer2IpAddr':ipv4DnsServer2IpAddr,'ipv4PppoeUserAccount':ipv4PppoeUserAccount,'ipv4PppoePassword':ipv4PppoePassword,'ipv4WinsFunction':ipv4WinsFunction,'ipv4WinsServer':ipv4WinsServer,'lan1Speed':lan1Speed,'routingProtocol':routingProtocol,'gratuitousArp':gratuitousArp,'gratuitousArpSendPeriod':gratuitousArpSendPeriod,'moduleSetting':moduleSetting,'redundancySetting':redundancySetting,'redundancyProtocol':redundancyProtocol,_a:spanningTree,'spanningTreeBridgePriority':spanningTreeBridgePriority,'spanningTreeHelloTime':spanningTreeHelloTime,'spanningTreeForwardingDelay':spanningTreeForwardingDelay,'spanningTreeMaxAge':spanningTreeMaxAge,'spanningTreePortTable':spanningTreePortTable,'spanningTreePortEntry':spanningTreePortEntry,_l:spanningTreePortIndex,'spanningTreePortEnable':spanningTreePortEnable,'spanningTreePortPriority':spanningTreePortPriority,'spanningTreePortCost':spanningTreePortCost,_b:turboRing,'turboRingMasterSetup':turboRingMasterSetup,'turboRingRdntPort1':turboRingRdntPort1,'turboRingRdntPort2':turboRingRdntPort2,_c:turboRingV2,'turboRingV2MasterSetup':turboRingV2MasterSetup,'turboRingV2RdntPort1':turboRingV2RdntPort1,'turboRingV2RdntPort2':turboRingV2RdntPort2,'gsmGprsSetting':gsmGprsSetting,'gsmGprsType':gsmGprsType,'gsmGprsPIN':gsmGprsPIN,'gsmGprsBand':gsmGprsBand,'gsmSetting':gsmSetting,'gsmMode':gsmMode,'gsmDestinationIpAddress':gsmDestinationIpAddress,'gsmSourceIpAddress':gsmSourceIpAddress,'gsmIpNetmask':gsmIpNetmask,'gsmTcpIpCompression':gsmTcpIpCompression,'gsmInactivityTime':gsmInactivityTime,'gsmLinkQualityReport':gsmLinkQualityReport,'gsmUsername':gsmUsername,'gsmPassword':gsmPassword,'gsmAuthenticationType':gsmAuthenticationType,'gsmTryNextAuth':gsmTryNextAuth,'gsmOutPhoneNumber':gsmOutPhoneNumber,'gsmInitialString':gsmInitialString,'gsmConnectionControl':gsmConnectionControl,'gsmConnectionInterval':gsmConnectionInterval,'gsmPingRemoteHost':gsmPingRemoteHost,'gsmInPhoneNumber':gsmInPhoneNumber,'gprsSetting':gprsSetting,'gprsTcpIpCompression':gprsTcpIpCompression,'gprsInactivityTime':gprsInactivityTime,'gprsLinkQualityReport':gprsLinkQualityReport,'gprsInitialString':gprsInitialString,'gprsUsername':gprsUsername,'gprsPassword':gprsPassword,'gprsAPN':gprsAPN,'gprsConnectionControl':gprsConnectionControl,'gprsConnectionInterval':gprsConnectionInterval,'gprsPingRemoteHost':gprsPingRemoteHost,'smsSetting':smsSetting,'smsFormat':smsFormat,'v92ModemSetting':v92ModemSetting,'v92ModemMode':v92ModemMode,'v92ModemDestinationIpAddress':v92ModemDestinationIpAddress,'v92ModemSourceIpAddress':v92ModemSourceIpAddress,'v92ModemIpNetmask':v92ModemIpNetmask,'v92ModemTcpIpCompression':v92ModemTcpIpCompression,'v92ModemInactivityTime':v92ModemInactivityTime,'v92ModemLinkQualityReport':v92ModemLinkQualityReport,'v92ModemUsername':v92ModemUsername,'v92ModemPassword':v92ModemPassword,'v92ModemIncomingPAPCheck':v92ModemIncomingPAPCheck,'v92ModemIncomingTryNextAuth':v92ModemIncomingTryNextAuth,'v92ModemPhoneNumber':v92ModemPhoneNumber,'v92ModemInitialString':v92ModemInitialString,'v92ModemConnectionControl':v92ModemConnectionControl,'v92ModemConnectionInterval':v92ModemConnectionInterval,'v92ModemPingRemoteHost':v92ModemPingRemoteHost,'ipv6Configuration':ipv6Configuration,'ipv6Address':ipv6Address,'ipv6Prefix':ipv6Prefix,'ipv6DefaultGateway':ipv6DefaultGateway,'ipv6DnsServer1IpAddr':ipv6DnsServer1IpAddr,'ipv6DnsServer2IpAddr':ipv6DnsServer2IpAddr,'connectionPriority':connectionPriority,'portSetting':portSetting,'opModeSetting':opModeSetting,'opMode':opMode,'opModePortTable':opModePortTable,'opModePortEntry':opModePortEntry,_I:portIndex,'portApplication':portApplication,'portMode':portMode,'application':application,'deviceControl':deviceControl,'deviceControlTable':deviceControlTable,'deviceControlEntry':deviceControlEntry,'deviceControlTcpAliveCheck':deviceControlTcpAliveCheck,'deviceControlMaxConnection':deviceControlMaxConnection,'deviceControlIgnoreJammedIp':deviceControlIgnoreJammedIp,'deviceControlAllowDriverControl':deviceControlAllowDriverControl,'deviceControlCommandByCommandOperation':deviceControlCommandByCommandOperation,'deviceControlSecure':deviceControlSecure,'deviceControlConnectionDownRTS':deviceControlConnectionDownRTS,'deviceControlConnectionDownDTR':deviceControlConnectionDownDTR,'deviceControlResponseTimeout':deviceControlResponseTimeout,'deviceControlNonRequestSerialData':deviceControlNonRequestSerialData,'deviceControlTcpPort':deviceControlTcpPort,'deviceControlDestinationAddress1':deviceControlDestinationAddress1,'deviceControlDestinationTcpPort1':deviceControlDestinationTcpPort1,'deviceControlDestinationCmdPort1':deviceControlDestinationCmdPort1,'deviceControlDestinationAddress2':deviceControlDestinationAddress2,'deviceControlDestinationTcpPort2':deviceControlDestinationTcpPort2,'deviceControlDestinationCmdPort2':deviceControlDestinationCmdPort2,'deviceControlDesignatedLocalTcpPort1':deviceControlDesignatedLocalTcpPort1,'deviceControlDesignatedLocalCmdPort1':deviceControlDesignatedLocalCmdPort1,'deviceControlDesignatedLocalTcpPort2':deviceControlDesignatedLocalTcpPort2,'deviceControlDesignatedLocalCmdPort2':deviceControlDesignatedLocalCmdPort2,_o:socket,'socketTable':socketTable,'socketEntry':socketEntry,'socketTcpAliveCheck':socketTcpAliveCheck,'socketInactivityTime':socketInactivityTime,'socketMaxConnection':socketMaxConnection,'socketIgnoreJammedIp':socketIgnoreJammedIp,'socketAllowDriverControl':socketAllowDriverControl,'socketCommandByCommandOperation':socketCommandByCommandOperation,'socketSecure':socketSecure,'socketTcpPort':socketTcpPort,'socketCmdPort':socketCmdPort,'socketTcpServerConnectionDownRTS':socketTcpServerConnectionDownRTS,'socketTcpServerConnectionDownDTR':socketTcpServerConnectionDownDTR,'socketResponseTimeout':socketResponseTimeout,'socketNonRequestSerialData':socketNonRequestSerialData,'socketTcpClientDestinationAddress1':socketTcpClientDestinationAddress1,'socketTcpClientDestinationPort1':socketTcpClientDestinationPort1,'socketTcpClientDestinationAddress2':socketTcpClientDestinationAddress2,'socketTcpClientDestinationPort2':socketTcpClientDestinationPort2,'socketTcpClientDestinationAddress3':socketTcpClientDestinationAddress3,'socketTcpClientDestinationPort3':socketTcpClientDestinationPort3,'socketTcpClientDestinationAddress4':socketTcpClientDestinationAddress4,'socketTcpClientDestinationPort4':socketTcpClientDestinationPort4,'socketTcpClientDesignatedLocalPort1':socketTcpClientDesignatedLocalPort1,'socketTcpClientDesignatedLocalPort2':socketTcpClientDesignatedLocalPort2,'socketTcpClientDesignatedLocalPort3':socketTcpClientDesignatedLocalPort3,'socketTcpClientDesignatedLocalPort4':socketTcpClientDesignatedLocalPort4,'socketTcpClientConnectionControl':socketTcpClientConnectionControl,'socketUdpDestinationAddress1Begin':socketUdpDestinationAddress1Begin,'socketUdpDestinationAddress1End':socketUdpDestinationAddress1End,'socketUdpDestinationPort1':socketUdpDestinationPort1,'socketUdpDestinationAddress2Begin':socketUdpDestinationAddress2Begin,'socketUdpDestinationAddress2End':socketUdpDestinationAddress2End,'socketUdpDestinationPort2':socketUdpDestinationPort2,'socketUdpDestinationAddress3Begin':socketUdpDestinationAddress3Begin,'socketUdpDestinationAddress3End':socketUdpDestinationAddress3End,'socketUdpDestinationPort3':socketUdpDestinationPort3,'socketUdpDestinationAddress4Begin':socketUdpDestinationAddress4Begin,'socketUdpDestinationAddress4End':socketUdpDestinationAddress4End,'socketUdpDestinationPort4':socketUdpDestinationPort4,'socketUdpLocalListenPort':socketUdpLocalListenPort,'socketUDPDynamicDst':socketUDPDynamicDst,'socketUDPDynamicDstTimeout':socketUDPDynamicDstTimeout,'pairConnection':pairConnection,'pairConnectionTable':pairConnectionTable,'pairConnectionEntry':pairConnectionEntry,'pairConnectionTcpAliveCheck':pairConnectionTcpAliveCheck,'pairConnectionSecure':pairConnectionSecure,'pairConnectionDestinationAddress':pairConnectionDestinationAddress,'pairConnectionDestinationPort':pairConnectionDestinationPort,'pairConnectionTcpPort':pairConnectionTcpPort,'ethernetModem':ethernetModem,'ethernetModemTable':ethernetModemTable,'ethernetModemEntry':ethernetModemEntry,'ethernetModemTcpAliveCheck':ethernetModemTcpAliveCheck,'ethernetModemTcpPort':ethernetModemTcpPort,_m:terminal,'terminalTable':terminalTable,'terminalEntry':terminalEntry,'terminalTcpAliveCheck':terminalTcpAliveCheck,'terminalInactivityTime':terminalInactivityTime,'terminalAutoLinkProtocol':terminalAutoLinkProtocol,'terminalPrimaryHostAddress':terminalPrimaryHostAddress,'terminalSecondHostAddress':terminalSecondHostAddress,'terminalTelnetTcpPort':terminalTelnetTcpPort,'terminalSshTcpPort':terminalSshTcpPort,'terminalType':terminalType,'terminalMaxSessions':terminalMaxSessions,'terminalChangeSession':terminalChangeSession,'terminalQuit':terminalQuit,'terminalBreak':terminalBreak,'terminalInterrupt':terminalInterrupt,'terminalAuthenticationType':terminalAuthenticationType,'terminalTryNextAuth':terminalTryNextAuth,'terminalAutoLoginPrompt':terminalAutoLoginPrompt,'terminalPasswordPrompt':terminalPasswordPrompt,'terminalLoginUserName':terminalLoginUserName,'terminalLoginPassword':terminalLoginPassword,'reverseTerminal':reverseTerminal,'reverseTerminalTable':reverseTerminalTable,'reverseTerminalEntry':reverseTerminalEntry,'reverseTerminalTcpAliveCheck':reverseTerminalTcpAliveCheck,'reverseTerminalInactivityTime':reverseTerminalInactivityTime,'reverseTerminalTcpPort':reverseTerminalTcpPort,'reverseTerminalAuthenticationType':reverseTerminalAuthenticationType,'reverseTerminalTryNextAuth':reverseTerminalTryNextAuth,'reverseTerminalMapKeys':reverseTerminalMapKeys,_n:printer,'printerTable':printerTable,'printerEntry':printerEntry,'printerTcpAliveCheck':printerTcpAliveCheck,'printerTcpPort':printerTcpPort,'printerGroup':printerGroup,'printerQueueNameRaw':printerQueueNameRaw,'printerQueueNameASCII':printerQueueNameASCII,'printerAppendFormFeed':printerAppendFormFeed,'dial':dial,'dialTable':dialTable,'dialEntry':dialEntry,'dialTERMBINMode':dialTERMBINMode,'dialPPPDMode':dialPPPDMode,'dialSLIPDMode':dialSLIPDMode,'dialAuthType':dialAuthType,'dialTryNextAuth':dialTryNextAuth,'dialDisconnectBy':dialDisconnectBy,'dialDestinationIpAddress':dialDestinationIpAddress,'dialSourceIpAddress':dialSourceIpAddress,'dialIpNetmask':dialIpNetmask,'dialTcpIpCompression':dialTcpIpCompression,'dialInactivityTime':dialInactivityTime,'dialLinkQualityReport':dialLinkQualityReport,'dialUsername':dialUsername,'dialPassword':dialPassword,'dialIncomingPAPCheck':dialIncomingPAPCheck,'dialIncomingTryNextAuth':dialIncomingTryNextAuth,'dataPacking':dataPacking,'dataPackingPortTable':dataPackingPortTable,'dataPackingPortEntry':dataPackingPortEntry,'portPacketLength':portPacketLength,'portDelimiter1Enable':portDelimiter1Enable,'portDelimiter1':portDelimiter1,'portDelimiter2Enable':portDelimiter2Enable,'portDelimiter2':portDelimiter2,'portDelimiterProcess':portDelimiterProcess,'portForceTransmit':portForceTransmit,'comParamSetting':comParamSetting,'comParamPortTable':comParamPortTable,'comParamPortEntry':comParamPortEntry,'portAlias':portAlias,'portInterface':portInterface,'portBaudRate':portBaudRate,'portBaudRateManual':portBaudRateManual,'portDataBits':portDataBits,'portStopBits':portStopBits,'portParity':portParity,'portFlowControl':portFlowControl,'portFIFO':portFIFO,'portOnDelay':portOnDelay,'portOffDelay':portOffDelay,'dataBuffering':dataBuffering,'dataBufferingPortTable':dataBufferingPortTable,'dataBufferingPortEntry':dataBufferingPortEntry,'portBufferingEnable':portBufferingEnable,'portBufferingLocation':portBufferingLocation,'portBufferingSDFileSize':portBufferingSDFileSize,'portSerialDataLoggingEnable':portSerialDataLoggingEnable,'modemSettings':modemSettings,'modemSettingsPortTable':modemSettingsPortTable,'modemSettingsPortEntry':modemSettingsPortEntry,'portEnableModem':portEnableModem,'portInitialString':portInitialString,'portDialUp':portDialUp,'portPhoneNumber':portPhoneNumber,'cipherSettings':cipherSettings,'cipherSettingsPortTable':cipherSettingsPortTable,'cipherSettingsPortEntry':cipherSettingsPortEntry,'sslCipherSort':sslCipherSort,'sshCipherSort':sshCipherSort,'welcomeMessage':welcomeMessage,'portEnableWelcomeMessage':portEnableWelcomeMessage,'portMessage':portMessage,'sysManagement':sysManagement,'miscNetworkSettings':miscNetworkSettings,'accessibleIp':accessibleIp,'enableAccessibleIpList':enableAccessibleIpList,'accessibleIpListTable':accessibleIpListTable,'accessibleIpListEntry':accessibleIpListEntry,_A0:accessibleIpListIndex,'activeAccessibleIpList':activeAccessibleIpList,'accessibleIpListAddress':accessibleIpListAddress,'accessibleIpListNetmask':accessibleIpListNetmask,'snmpAgentSettings':snmpAgentSettings,'snmpEnable':snmpEnable,'snmpContactName':snmpContactName,'snmpLocation':snmpLocation,'dDNS':dDNS,'dDNSEnable':dDNSEnable,'dDNSServerAddress':dDNSServerAddress,'dDNSHostName':dDNSHostName,'dDNSUserName':dDNSUserName,'dDNSPassword':dDNSPassword,'hostTable':hostTable,'hostTableTable':hostTableTable,'hostTableEntry':hostTableEntry,_A1:hostTableIndex,'hostName':hostName,'hostIpAddress':hostIpAddress,'routeTable':routeTable,'routeTableTable':routeTableTable,'routeTableEntry':routeTableEntry,_A2:routeTableIndex,'gatewayRouteTable':gatewayRouteTable,'destinationRouteTable':destinationRouteTable,'netmaskRouteTable':netmaskRouteTable,'metricRouteTable':metricRouteTable,'interfaceRouteTable':interfaceRouteTable,'userTable':userTable,'userTableTable':userTableTable,'userTableEntry':userTableEntry,_A3:userTableIndex,'userNameUserTable':userNameUserTable,'passwordUserTable':passwordUserTable,'phoneNumberUserTable':phoneNumberUserTable,'authenticationServer':authenticationServer,'radiusServerIp':radiusServerIp,'radiusKey':radiusKey,'udpPortAuthenticationServer':udpPortAuthenticationServer,'radiusAccounting':radiusAccounting,'tacacsPlusServerIp':tacacsPlusServerIp,'tacacsPlusSecret':tacacsPlusSecret,'tacacsPlusAccounting':tacacsPlusAccounting,'sysLogSettings':sysLogSettings,'sysLocalLog':sysLocalLog,'networkLocalLog':networkLocalLog,'configLocalLog':configLocalLog,'opModeLocalLog':opModeLocalLog,'sysRemoteLog':sysRemoteLog,'networkRemoteLog':networkRemoteLog,'configRemoteLog':configRemoteLog,'opModeRemoteLog':opModeRemoteLog,'remoteLogServer':remoteLogServer,'syslogServerIp':syslogServerIp,'syslogFacility':syslogFacility,'syslogSeverity':syslogSeverity,'autoWarningSettings':autoWarningSettings,'eventSettings':eventSettings,'mailWarningColdStart':mailWarningColdStart,'mailWarningWarmStart':mailWarningWarmStart,'mailWarningAuthFailure':mailWarningAuthFailure,'mailWarningIpChanged':mailWarningIpChanged,'mailWarningPasswordChanged':mailWarningPasswordChanged,'trapServerColdStart':trapServerColdStart,'trapServerWarmStart':trapServerWarmStart,'trapServerAuthFailure':trapServerAuthFailure,'alarmServerEthernet1LinkDown':alarmServerEthernet1LinkDown,'alarmServerEthernet2LinkDown':alarmServerEthernet2LinkDown,'alarmServerEthernet3LinkDown':alarmServerEthernet3LinkDown,'smsServerColdStart':smsServerColdStart,'smsServerWarmStart':smsServerWarmStart,'smsServerEthernet1LinkDown':smsServerEthernet1LinkDown,'smsServerEthernet2LinkDown':smsServerEthernet2LinkDown,'smsServerEthernet3LinkDown':smsServerEthernet3LinkDown,'smsServerAuthFailure':smsServerAuthFailure,'smsServerIpChanged':smsServerIpChanged,'smsServerPasswordChanged':smsServerPasswordChanged,'serialEventSettings':serialEventSettings,'portEventSettingsTable':portEventSettingsTable,'portEventSettingsEntry':portEventSettingsEntry,'mailDCDchange':mailDCDchange,'trapDCDchange':trapDCDchange,'alarmDCDchange':alarmDCDchange,'smsDCDchange':smsDCDchange,'mailDSRchange':mailDSRchange,'trapDSRchange':trapDSRchange,'alarmDSRchange':alarmDSRchange,'smsDSRchange':smsDSRchange,'emailAlert':emailAlert,'emailWarningMailServer':emailWarningMailServer,'emailRequiresAuthentication':emailRequiresAuthentication,'emailWarningUserName':emailWarningUserName,'emailWarningPassword':emailWarningPassword,'emailWarningFromEmail':emailWarningFromEmail,'emailWarningFirstEmailAddr':emailWarningFirstEmailAddr,'emailWarningSecondEmailAddr':emailWarningSecondEmailAddr,'emailWarningThirdEmailAddr':emailWarningThirdEmailAddr,'emailWarningFourthEmailAddr':emailWarningFourthEmailAddr,'snmpTrap':snmpTrap,'snmpTrapReceiverIp':snmpTrapReceiverIp,'trapVersion':trapVersion,'smsAlert':smsAlert,'smsAlertFirstPhoneNumber':smsAlertFirstPhoneNumber,'smsAlertSecondPhoneNumber':smsAlertSecondPhoneNumber,'smsAlertThirdPhoneNumber':smsAlertThirdPhoneNumber,'smsAlertFourthPhoneNumber':smsAlertFourthPhoneNumber,'eventLogSettings':eventLogSettings,'currentLogCapacityRatio':currentLogCapacityRatio,'logCapacityWarningEnable':logCapacityWarningEnable,'logCapacityWarningThreshold':logCapacityWarningThreshold,'mailLogCapacity':mailLogCapacity,'trapLogCapacity':trapLogCapacity,'logOversizeAction':logOversizeAction,'maintenance':maintenance,'consoleSettings':consoleSettings,'httpConsole':httpConsole,'httpsConsole':httpsConsole,'telnetConsole':telnetConsole,'sshConsole':sshConsole,'consoleAuthenticationType':consoleAuthenticationType,'tryNextTypeOnAuthDenied':tryNextTypeOnAuthDenied,'resetButtonFunction':resetButtonFunction,'lcmReadOnlyProtect':lcmReadOnlyProtect,'maxHttpLoginUsers':maxHttpLoginUsers,'autoLogoutSetting':autoLogoutSetting,'loadFactoryDefault':loadFactoryDefault,'loadFactoryDefaultSetting':loadFactoryDefaultSetting,'accountManagement':accountManagement,'notificationMessage':notificationMessage,'loginNotificationMessage':loginNotificationMessage,'loginFailureMessage':loginFailureMessage,'userAccount':userAccount,'userAccountTable':userAccountTable,'userAccountEntry':userAccountEntry,_A4:userAccountIndex,'activeUserAccount':activeUserAccount,'accountName':accountName,'accountGroupName':accountGroupName,'accessPermission':accessPermission,'accessPermissionTable':accessPermissionTable,'accessPermissionEntry':accessPermissionEntry,_A5:groupName,'networkConfig':networkConfig,'serialConfig':serialConfig,'systemConfig':systemConfig,'adminConfig':adminConfig,'monitorLogWarning':monitorLogWarning,'commonSetting':commonSetting,'accountPasswordAndLoginMgmt':accountPasswordAndLoginMgmt,'accountPasswordPolicy':accountPasswordPolicy,'pwdMinLength':pwdMinLength,'pwdComplexityCheckEnable':pwdComplexityCheckEnable,'pwdComplexityCheckDigitEnable':pwdComplexityCheckDigitEnable,'pwdComplexityCheckAlphabetEnable':pwdComplexityCheckAlphabetEnable,'pwdComplexityCheckSpecialCharEnable':pwdComplexityCheckSpecialCharEnable,'pwdLifetime':pwdLifetime,'accountLoginFailureLockout':accountLoginFailureLockout,'loginFailureLockoutEnable':loginFailureLockoutEnable,'loginFailureLockoutRetrys':loginFailureLockoutRetrys,'loginFailureLockoutTime':loginFailureLockoutTime,'sysStatus':sysStatus,'s2eConnections':s2eConnections,'monitorRemoteIpTable':monitorRemoteIpTable,'monitorRemoteIpEntry':monitorRemoteIpEntry,_A6:remoteIpIndex,'monitorRemoteIp':monitorRemoteIp,'monitorCipher':monitorCipher,'serialPortStatus':serialPortStatus,'monitorSerialPortStatusTable':monitorSerialPortStatusTable,'monitorSerialPortStatusEntry':monitorSerialPortStatusEntry,'monitorTxCount':monitorTxCount,'monitorRxCount':monitorRxCount,'monitorTxTotalCount':monitorTxTotalCount,'monitorRxTotalCount':monitorRxTotalCount,'monitorDSR':monitorDSR,'monitorDTR':monitorDTR,'monitorRTS':monitorRTS,'monitorCTS':monitorCTS,'monitorDCD':monitorDCD,'serialPortErrorCount':serialPortErrorCount,'monitorSerialPortErrorCountTable':monitorSerialPortErrorCountTable,'monitorSerialPortErrorCountEntry':monitorSerialPortErrorCountEntry,'monitorErrorCountFrame':monitorErrorCountFrame,'monitorErrorCountParity':monitorErrorCountParity,'monitorErrorCountOverrun':monitorErrorCountOverrun,'monitorErrorCountBreak':monitorErrorCountBreak,'serialPortSettings':serialPortSettings,'monitorSerialPortSettingsTable':monitorSerialPortSettingsTable,'monitorSerialPortSettingsEntry':monitorSerialPortSettingsEntry,'monitorBaudRate':monitorBaudRate,'monitorDataBits':monitorDataBits,'monitorStopBits':monitorStopBits,'monitorParity':monitorParity,'monitorRTSCTSFlowControl':monitorRTSCTSFlowControl,'monitorXONXOFFFlowControl':monitorXONXOFFFlowControl,'monitorDTRDSRFlowControl':monitorDTRDSRFlowControl,'monitorRTSToggleFlowControl':monitorRTSToggleFlowControl,'monitorFIFO':monitorFIFO,'monitorInterface':monitorInterface,'serialPortBuffering':serialPortBuffering,'monitorSerialPortBufferingTable':monitorSerialPortBufferingTable,'monitorSerialPortBufferingEntry':monitorSerialPortBufferingEntry,'monitorBuffering':monitorBuffering,'relayOutputStatus':relayOutputStatus,'relayOutputEthernet1LinkDown':relayOutputEthernet1LinkDown,'ethernet1LinkDownAcknowledge':ethernet1LinkDownAcknowledge,'relayOutputEthernet2LinkDown':relayOutputEthernet2LinkDown,'ethernet2LinkDownAcknowledge':ethernet2LinkDownAcknowledge,'relayOutputEthernet3LinkDown':relayOutputEthernet3LinkDown,'ethernet3LinkDownAcknowledge':ethernet3LinkDownAcknowledge,'portDCDChangedStatusTable':portDCDChangedStatusTable,'portDCDChangedStatusEntry':portDCDChangedStatusEntry,'portDCDChangedStatus':portDCDChangedStatus,'portDCDChangedAcknowledge':portDCDChangedAcknowledge,'portDSRChangedStatusTable':portDSRChangedStatusTable,'portDSRChangedStatusEntry':portDSRChangedStatusEntry,'portDSRChangedStatus':portDSRChangedStatus,'portDSRChangedAcknowledge':portDSRChangedAcknowledge,'moduleStatus':moduleStatus,'redundancyStatus':redundancyStatus,'activeRedundancyProtocol':activeRedundancyProtocol,'spanningTreeStatus':spanningTreeStatus,'spanningTreeBridgeRole':spanningTreeBridgeRole,'spanningTreeRootBridge':spanningTreeRootBridge,'spanningTreeRootPathCost':spanningTreeRootPathCost,'spanningTreePortStatusTable':spanningTreePortStatusTable,'spanningTreePortStatusEntry':spanningTreePortStatusEntry,_A7:spanningTreePortStatusIndex,'spanningTreePortEnableStatus':spanningTreePortEnableStatus,'spanningTreePortRole':spanningTreePortRole,'spanningTreePortDesignatedBridge':spanningTreePortDesignatedBridge,'spanningTreePortStatus':spanningTreePortStatus,'turboRingStatus':turboRingStatus,'turboRingBrokenStatus':turboRingBrokenStatus,'turboRingMaster':turboRingMaster,'turboRingPort1':turboRingPort1,'turboRingPort2':turboRingPort2,'turboRingPort1Status':turboRingPort1Status,'turboRingPort2Status':turboRingPort2Status,'saveConfiguration':saveConfiguration,'saveConfig':saveConfig,'restart':restart,'restartPorts':restartPorts,'restartSystem':restartSystem})