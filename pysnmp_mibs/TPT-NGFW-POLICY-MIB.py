_x='tptNgfwPolicyNotificationGroup'
_w='tptNgfwPolicyGroup'
_v='tptNgfwPolicyNotify'
_u='tptNgfwPolicyNotifyActionSetName'
_t='quarantine'
_s='tptNgfwSystemSerial'
_r='TPT-NGFW-SYSTEM-INFO-MIB'
_q='tptNgfwPolicyNotifyPeriod'
_p='tptNgfwPolicyNotifyMsgParams'
_o='tptNgfwPolicyNotifyHitCount'
_n='tptNgfwPolicyNotifyVlanId'
_m='tptNgfwPolicyNotifyPolicyName'
_l='tptNgfwPolicyNotifyProfileName'
_k='tptNgfwPolicyNotifyFilterName'
_j='tptNgfwPolicyNotifyPktTraceEnd'
_i='tptNgfwPolicyNotifyPktTraceBegin'
_h='tptNgfwPolicyNotifyPktTraceId'
_g='tptNgfwPolicyNotifyPktTraceVer'
_f='tptNgfwPolicyNotifyRateLimit'
_e='tptNgfwPolicyNotifyStartTimeNano'
_d='tptNgfwPolicyNotifyStartTimeSec'
_c='tptNgfwPolicyNotifyBytesOut'
_b='tptNgfwPolicyNotifyBytesIn'
_a='tptNgfwPolicyNotifyUserName'
_Z='tptNgfwPolicyNotifyApplicationName'
_Y='tptNgfwPolicyNotifyProtocol'
_X='tptNgfwPolicyNotifyDestTransPort'
_W='tptNgfwPolicyNotifyDestTransIpAddr'
_V='tptNgfwPolicyNotifyDestPort'
_U='tptNgfwPolicyNotifyDestIpAddr'
_T='tptNgfwPolicyNotifyDestIpAddrType'
_S='tptNgfwPolicyNotifySrcTransPort'
_R='tptNgfwPolicyNotifySrcTransIpAddr'
_Q='tptNgfwPolicyNotifySrcPort'
_P='tptNgfwPolicyNotifySrcIpAddr'
_O='tptNgfwPolicyNotifySrcIpAddrType'
_N='tptNgfwPolicyNotifyOutInterface'
_M='tptNgfwPolicyNotifyInInterface'
_L='tptNgfwPolicyNotifyRuleName'
_K='tptNgfwPolicyNotifyAction'
_J='tptNgfwPolicyNotifyActionType'
_I='tptNgfwPolicyNotifyCorrelationId'
_H='tptNgfwPolicyNotifyEventSeverity'
_G='tptNgfwPolicyNotifyEventType'
_F='tptNgfwPolicyNotifyEventSource'
_E='tptNgfwPolicyNotifyTime'
_D='SnmpAdminString'
_C='accessible-for-notify'
_B='current'
_A='TPT-NGFW-POLICY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
tpt_ngfw_compls,tpt_ngfw_eventsV2,tpt_ngfw_groups,tpt_ngfw_objs,tpt_ngfw_params=mibBuilder.importSymbols('TPT-NGFW-REG-MIB','tpt-ngfw-compls','tpt-ngfw-eventsV2','tpt-ngfw-groups','tpt-ngfw-objs','tpt-ngfw-params')
tptNgfwSystemSerial,=mibBuilder.importSymbols(_r,_s)
tptNgfwPolicy=ModuleIdentity((1,3,6,1,4,1,10734,3,9,2,4))
if mibBuilder.loadTexts:tptNgfwPolicy.setRevisions(('2016-05-25 18:54','2013-03-13 12:00'))
class EventSource(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('firewall',1),('ips',2),('reputation',3),(_t,4)))
class FirewallEventType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('sessionStart',1),('applicationDetect',2),('sessionEnd',3),('blockedByFirewall',4)))
class EventSeverity(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('info',1),('low',2),('minor',3),('major',4),('critical',5)))
class ActionType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('permit',1),('rateLimit',2),('trust',3),('block',4),(_t,5)))
class PacketTraceVersion(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('packetTraceV1',1),('packetTraceV2',2),('none',3)))
_TptNgfwPolicyNotifyTime_Type=DateAndTime
_TptNgfwPolicyNotifyTime_Object=MibScalar
tptNgfwPolicyNotifyTime=_TptNgfwPolicyNotifyTime_Object((1,3,6,1,4,1,10734,3,9,3,1,20),_TptNgfwPolicyNotifyTime_Type())
tptNgfwPolicyNotifyTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyTime.setStatus(_B)
_TptNgfwPolicyNotifyEventSource_Type=EventSource
_TptNgfwPolicyNotifyEventSource_Object=MibScalar
tptNgfwPolicyNotifyEventSource=_TptNgfwPolicyNotifyEventSource_Object((1,3,6,1,4,1,10734,3,9,3,1,21),_TptNgfwPolicyNotifyEventSource_Type())
tptNgfwPolicyNotifyEventSource.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyEventSource.setStatus(_B)
_TptNgfwPolicyNotifyEventType_Type=FirewallEventType
_TptNgfwPolicyNotifyEventType_Object=MibScalar
tptNgfwPolicyNotifyEventType=_TptNgfwPolicyNotifyEventType_Object((1,3,6,1,4,1,10734,3,9,3,1,22),_TptNgfwPolicyNotifyEventType_Type())
tptNgfwPolicyNotifyEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyEventType.setStatus(_B)
_TptNgfwPolicyNotifyEventSeverity_Type=EventSeverity
_TptNgfwPolicyNotifyEventSeverity_Object=MibScalar
tptNgfwPolicyNotifyEventSeverity=_TptNgfwPolicyNotifyEventSeverity_Object((1,3,6,1,4,1,10734,3,9,3,1,23),_TptNgfwPolicyNotifyEventSeverity_Type())
tptNgfwPolicyNotifyEventSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyEventSeverity.setStatus(_B)
class _TptNgfwPolicyNotifyCorrelationId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TptNgfwPolicyNotifyCorrelationId_Type.__name__=_D
_TptNgfwPolicyNotifyCorrelationId_Object=MibScalar
tptNgfwPolicyNotifyCorrelationId=_TptNgfwPolicyNotifyCorrelationId_Object((1,3,6,1,4,1,10734,3,9,3,1,24),_TptNgfwPolicyNotifyCorrelationId_Type())
tptNgfwPolicyNotifyCorrelationId.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyCorrelationId.setStatus(_B)
_TptNgfwPolicyNotifyActionType_Type=ActionType
_TptNgfwPolicyNotifyActionType_Object=MibScalar
tptNgfwPolicyNotifyActionType=_TptNgfwPolicyNotifyActionType_Object((1,3,6,1,4,1,10734,3,9,3,1,25),_TptNgfwPolicyNotifyActionType_Type())
tptNgfwPolicyNotifyActionType.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyActionType.setStatus(_B)
class _TptNgfwPolicyNotifyAction_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TptNgfwPolicyNotifyAction_Type.__name__=_D
_TptNgfwPolicyNotifyAction_Object=MibScalar
tptNgfwPolicyNotifyAction=_TptNgfwPolicyNotifyAction_Object((1,3,6,1,4,1,10734,3,9,3,1,26),_TptNgfwPolicyNotifyAction_Type())
tptNgfwPolicyNotifyAction.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyAction.setStatus(_B)
class _TptNgfwPolicyNotifyActionSetName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TptNgfwPolicyNotifyActionSetName_Type.__name__=_D
_TptNgfwPolicyNotifyActionSetName_Object=MibScalar
tptNgfwPolicyNotifyActionSetName=_TptNgfwPolicyNotifyActionSetName_Object((1,3,6,1,4,1,10734,3,9,3,1,27),_TptNgfwPolicyNotifyActionSetName_Type())
tptNgfwPolicyNotifyActionSetName.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyActionSetName.setStatus(_B)
class _TptNgfwPolicyNotifyRuleName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_TptNgfwPolicyNotifyRuleName_Type.__name__=_D
_TptNgfwPolicyNotifyRuleName_Object=MibScalar
tptNgfwPolicyNotifyRuleName=_TptNgfwPolicyNotifyRuleName_Object((1,3,6,1,4,1,10734,3,9,3,1,28),_TptNgfwPolicyNotifyRuleName_Type())
tptNgfwPolicyNotifyRuleName.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyRuleName.setStatus(_B)
class _TptNgfwPolicyNotifyInInterface_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptNgfwPolicyNotifyInInterface_Type.__name__=_D
_TptNgfwPolicyNotifyInInterface_Object=MibScalar
tptNgfwPolicyNotifyInInterface=_TptNgfwPolicyNotifyInInterface_Object((1,3,6,1,4,1,10734,3,9,3,1,29),_TptNgfwPolicyNotifyInInterface_Type())
tptNgfwPolicyNotifyInInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyInInterface.setStatus(_B)
class _TptNgfwPolicyNotifyOutInterface_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptNgfwPolicyNotifyOutInterface_Type.__name__=_D
_TptNgfwPolicyNotifyOutInterface_Object=MibScalar
tptNgfwPolicyNotifyOutInterface=_TptNgfwPolicyNotifyOutInterface_Object((1,3,6,1,4,1,10734,3,9,3,1,30),_TptNgfwPolicyNotifyOutInterface_Type())
tptNgfwPolicyNotifyOutInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyOutInterface.setStatus(_B)
_TptNgfwPolicyNotifySrcIpAddrType_Type=InetAddressType
_TptNgfwPolicyNotifySrcIpAddrType_Object=MibScalar
tptNgfwPolicyNotifySrcIpAddrType=_TptNgfwPolicyNotifySrcIpAddrType_Object((1,3,6,1,4,1,10734,3,9,3,1,31),_TptNgfwPolicyNotifySrcIpAddrType_Type())
tptNgfwPolicyNotifySrcIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifySrcIpAddrType.setStatus(_B)
_TptNgfwPolicyNotifySrcIpAddr_Type=InetAddress
_TptNgfwPolicyNotifySrcIpAddr_Object=MibScalar
tptNgfwPolicyNotifySrcIpAddr=_TptNgfwPolicyNotifySrcIpAddr_Object((1,3,6,1,4,1,10734,3,9,3,1,32),_TptNgfwPolicyNotifySrcIpAddr_Type())
tptNgfwPolicyNotifySrcIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifySrcIpAddr.setStatus(_B)
_TptNgfwPolicyNotifySrcPort_Type=Unsigned32
_TptNgfwPolicyNotifySrcPort_Object=MibScalar
tptNgfwPolicyNotifySrcPort=_TptNgfwPolicyNotifySrcPort_Object((1,3,6,1,4,1,10734,3,9,3,1,33),_TptNgfwPolicyNotifySrcPort_Type())
tptNgfwPolicyNotifySrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifySrcPort.setStatus(_B)
_TptNgfwPolicyNotifySrcTransIpAddr_Type=InetAddress
_TptNgfwPolicyNotifySrcTransIpAddr_Object=MibScalar
tptNgfwPolicyNotifySrcTransIpAddr=_TptNgfwPolicyNotifySrcTransIpAddr_Object((1,3,6,1,4,1,10734,3,9,3,1,34),_TptNgfwPolicyNotifySrcTransIpAddr_Type())
tptNgfwPolicyNotifySrcTransIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifySrcTransIpAddr.setStatus(_B)
_TptNgfwPolicyNotifySrcTransPort_Type=Unsigned32
_TptNgfwPolicyNotifySrcTransPort_Object=MibScalar
tptNgfwPolicyNotifySrcTransPort=_TptNgfwPolicyNotifySrcTransPort_Object((1,3,6,1,4,1,10734,3,9,3,1,35),_TptNgfwPolicyNotifySrcTransPort_Type())
tptNgfwPolicyNotifySrcTransPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifySrcTransPort.setStatus(_B)
_TptNgfwPolicyNotifyDestIpAddrType_Type=InetAddressType
_TptNgfwPolicyNotifyDestIpAddrType_Object=MibScalar
tptNgfwPolicyNotifyDestIpAddrType=_TptNgfwPolicyNotifyDestIpAddrType_Object((1,3,6,1,4,1,10734,3,9,3,1,36),_TptNgfwPolicyNotifyDestIpAddrType_Type())
tptNgfwPolicyNotifyDestIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyDestIpAddrType.setStatus(_B)
_TptNgfwPolicyNotifyDestIpAddr_Type=InetAddress
_TptNgfwPolicyNotifyDestIpAddr_Object=MibScalar
tptNgfwPolicyNotifyDestIpAddr=_TptNgfwPolicyNotifyDestIpAddr_Object((1,3,6,1,4,1,10734,3,9,3,1,37),_TptNgfwPolicyNotifyDestIpAddr_Type())
tptNgfwPolicyNotifyDestIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyDestIpAddr.setStatus(_B)
_TptNgfwPolicyNotifyDestPort_Type=Unsigned32
_TptNgfwPolicyNotifyDestPort_Object=MibScalar
tptNgfwPolicyNotifyDestPort=_TptNgfwPolicyNotifyDestPort_Object((1,3,6,1,4,1,10734,3,9,3,1,38),_TptNgfwPolicyNotifyDestPort_Type())
tptNgfwPolicyNotifyDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyDestPort.setStatus(_B)
_TptNgfwPolicyNotifyDestTransIpAddr_Type=InetAddress
_TptNgfwPolicyNotifyDestTransIpAddr_Object=MibScalar
tptNgfwPolicyNotifyDestTransIpAddr=_TptNgfwPolicyNotifyDestTransIpAddr_Object((1,3,6,1,4,1,10734,3,9,3,1,39),_TptNgfwPolicyNotifyDestTransIpAddr_Type())
tptNgfwPolicyNotifyDestTransIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyDestTransIpAddr.setStatus(_B)
_TptNgfwPolicyNotifyDestTransPort_Type=Unsigned32
_TptNgfwPolicyNotifyDestTransPort_Object=MibScalar
tptNgfwPolicyNotifyDestTransPort=_TptNgfwPolicyNotifyDestTransPort_Object((1,3,6,1,4,1,10734,3,9,3,1,40),_TptNgfwPolicyNotifyDestTransPort_Type())
tptNgfwPolicyNotifyDestTransPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyDestTransPort.setStatus(_B)
class _TptNgfwPolicyNotifyProtocol_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptNgfwPolicyNotifyProtocol_Type.__name__=_D
_TptNgfwPolicyNotifyProtocol_Object=MibScalar
tptNgfwPolicyNotifyProtocol=_TptNgfwPolicyNotifyProtocol_Object((1,3,6,1,4,1,10734,3,9,3,1,41),_TptNgfwPolicyNotifyProtocol_Type())
tptNgfwPolicyNotifyProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyProtocol.setStatus(_B)
class _TptNgfwPolicyNotifyApplicationName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TptNgfwPolicyNotifyApplicationName_Type.__name__=_D
_TptNgfwPolicyNotifyApplicationName_Object=MibScalar
tptNgfwPolicyNotifyApplicationName=_TptNgfwPolicyNotifyApplicationName_Object((1,3,6,1,4,1,10734,3,9,3,1,42),_TptNgfwPolicyNotifyApplicationName_Type())
tptNgfwPolicyNotifyApplicationName.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyApplicationName.setStatus(_B)
class _TptNgfwPolicyNotifyUserName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TptNgfwPolicyNotifyUserName_Type.__name__=_D
_TptNgfwPolicyNotifyUserName_Object=MibScalar
tptNgfwPolicyNotifyUserName=_TptNgfwPolicyNotifyUserName_Object((1,3,6,1,4,1,10734,3,9,3,1,43),_TptNgfwPolicyNotifyUserName_Type())
tptNgfwPolicyNotifyUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyUserName.setStatus(_B)
_TptNgfwPolicyNotifyBytesIn_Type=Counter64
_TptNgfwPolicyNotifyBytesIn_Object=MibScalar
tptNgfwPolicyNotifyBytesIn=_TptNgfwPolicyNotifyBytesIn_Object((1,3,6,1,4,1,10734,3,9,3,1,44),_TptNgfwPolicyNotifyBytesIn_Type())
tptNgfwPolicyNotifyBytesIn.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyBytesIn.setStatus(_B)
_TptNgfwPolicyNotifyBytesOut_Type=Counter64
_TptNgfwPolicyNotifyBytesOut_Object=MibScalar
tptNgfwPolicyNotifyBytesOut=_TptNgfwPolicyNotifyBytesOut_Object((1,3,6,1,4,1,10734,3,9,3,1,45),_TptNgfwPolicyNotifyBytesOut_Type())
tptNgfwPolicyNotifyBytesOut.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyBytesOut.setStatus(_B)
_TptNgfwPolicyNotifyStartTimeSec_Type=Counter64
_TptNgfwPolicyNotifyStartTimeSec_Object=MibScalar
tptNgfwPolicyNotifyStartTimeSec=_TptNgfwPolicyNotifyStartTimeSec_Object((1,3,6,1,4,1,10734,3,9,3,1,46),_TptNgfwPolicyNotifyStartTimeSec_Type())
tptNgfwPolicyNotifyStartTimeSec.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyStartTimeSec.setStatus(_B)
_TptNgfwPolicyNotifyStartTimeNano_Type=Counter64
_TptNgfwPolicyNotifyStartTimeNano_Object=MibScalar
tptNgfwPolicyNotifyStartTimeNano=_TptNgfwPolicyNotifyStartTimeNano_Object((1,3,6,1,4,1,10734,3,9,3,1,47),_TptNgfwPolicyNotifyStartTimeNano_Type())
tptNgfwPolicyNotifyStartTimeNano.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyStartTimeNano.setStatus(_B)
_TptNgfwPolicyNotifyRateLimit_Type=Counter64
_TptNgfwPolicyNotifyRateLimit_Object=MibScalar
tptNgfwPolicyNotifyRateLimit=_TptNgfwPolicyNotifyRateLimit_Object((1,3,6,1,4,1,10734,3,9,3,1,48),_TptNgfwPolicyNotifyRateLimit_Type())
tptNgfwPolicyNotifyRateLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyRateLimit.setStatus(_B)
_TptNgfwPolicyNotifyPktTraceVer_Type=PacketTraceVersion
_TptNgfwPolicyNotifyPktTraceVer_Object=MibScalar
tptNgfwPolicyNotifyPktTraceVer=_TptNgfwPolicyNotifyPktTraceVer_Object((1,3,6,1,4,1,10734,3,9,3,1,49),_TptNgfwPolicyNotifyPktTraceVer_Type())
tptNgfwPolicyNotifyPktTraceVer.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyPktTraceVer.setStatus(_B)
_TptNgfwPolicyNotifyPktTraceId_Type=Unsigned32
_TptNgfwPolicyNotifyPktTraceId_Object=MibScalar
tptNgfwPolicyNotifyPktTraceId=_TptNgfwPolicyNotifyPktTraceId_Object((1,3,6,1,4,1,10734,3,9,3,1,50),_TptNgfwPolicyNotifyPktTraceId_Type())
tptNgfwPolicyNotifyPktTraceId.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyPktTraceId.setStatus(_B)
_TptNgfwPolicyNotifyPktTraceBegin_Type=Unsigned32
_TptNgfwPolicyNotifyPktTraceBegin_Object=MibScalar
tptNgfwPolicyNotifyPktTraceBegin=_TptNgfwPolicyNotifyPktTraceBegin_Object((1,3,6,1,4,1,10734,3,9,3,1,51),_TptNgfwPolicyNotifyPktTraceBegin_Type())
tptNgfwPolicyNotifyPktTraceBegin.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyPktTraceBegin.setStatus(_B)
_TptNgfwPolicyNotifyPktTraceEnd_Type=Unsigned32
_TptNgfwPolicyNotifyPktTraceEnd_Object=MibScalar
tptNgfwPolicyNotifyPktTraceEnd=_TptNgfwPolicyNotifyPktTraceEnd_Object((1,3,6,1,4,1,10734,3,9,3,1,52),_TptNgfwPolicyNotifyPktTraceEnd_Type())
tptNgfwPolicyNotifyPktTraceEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyPktTraceEnd.setStatus(_B)
class _TptNgfwPolicyNotifyFilterName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptNgfwPolicyNotifyFilterName_Type.__name__=_D
_TptNgfwPolicyNotifyFilterName_Object=MibScalar
tptNgfwPolicyNotifyFilterName=_TptNgfwPolicyNotifyFilterName_Object((1,3,6,1,4,1,10734,3,9,3,1,53),_TptNgfwPolicyNotifyFilterName_Type())
tptNgfwPolicyNotifyFilterName.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyFilterName.setStatus(_B)
class _TptNgfwPolicyNotifyProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TptNgfwPolicyNotifyProfileName_Type.__name__=_D
_TptNgfwPolicyNotifyProfileName_Object=MibScalar
tptNgfwPolicyNotifyProfileName=_TptNgfwPolicyNotifyProfileName_Object((1,3,6,1,4,1,10734,3,9,3,1,54),_TptNgfwPolicyNotifyProfileName_Type())
tptNgfwPolicyNotifyProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyProfileName.setStatus(_B)
class _TptNgfwPolicyNotifyPolicyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_TptNgfwPolicyNotifyPolicyName_Type.__name__=_D
_TptNgfwPolicyNotifyPolicyName_Object=MibScalar
tptNgfwPolicyNotifyPolicyName=_TptNgfwPolicyNotifyPolicyName_Object((1,3,6,1,4,1,10734,3,9,3,1,55),_TptNgfwPolicyNotifyPolicyName_Type())
tptNgfwPolicyNotifyPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyPolicyName.setStatus(_B)
class _TptNgfwPolicyNotifyVlanId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptNgfwPolicyNotifyVlanId_Type.__name__=_D
_TptNgfwPolicyNotifyVlanId_Object=MibScalar
tptNgfwPolicyNotifyVlanId=_TptNgfwPolicyNotifyVlanId_Object((1,3,6,1,4,1,10734,3,9,3,1,56),_TptNgfwPolicyNotifyVlanId_Type())
tptNgfwPolicyNotifyVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyVlanId.setStatus(_B)
_TptNgfwPolicyNotifyHitCount_Type=Counter64
_TptNgfwPolicyNotifyHitCount_Object=MibScalar
tptNgfwPolicyNotifyHitCount=_TptNgfwPolicyNotifyHitCount_Object((1,3,6,1,4,1,10734,3,9,3,1,57),_TptNgfwPolicyNotifyHitCount_Type())
tptNgfwPolicyNotifyHitCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyHitCount.setStatus(_B)
class _TptNgfwPolicyNotifyMsgParams_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TptNgfwPolicyNotifyMsgParams_Type.__name__=_D
_TptNgfwPolicyNotifyMsgParams_Object=MibScalar
tptNgfwPolicyNotifyMsgParams=_TptNgfwPolicyNotifyMsgParams_Object((1,3,6,1,4,1,10734,3,9,3,1,58),_TptNgfwPolicyNotifyMsgParams_Type())
tptNgfwPolicyNotifyMsgParams.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyMsgParams.setStatus(_B)
_TptNgfwPolicyNotifyPeriod_Type=Unsigned32
_TptNgfwPolicyNotifyPeriod_Object=MibScalar
tptNgfwPolicyNotifyPeriod=_TptNgfwPolicyNotifyPeriod_Object((1,3,6,1,4,1,10734,3,9,3,1,59),_TptNgfwPolicyNotifyPeriod_Type())
tptNgfwPolicyNotifyPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:tptNgfwPolicyNotifyPeriod.setStatus(_B)
tptNgfwPolicyGroup=ObjectGroup((1,3,6,1,4,1,10734,3,9,1,1,7))
tptNgfwPolicyGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_u),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:tptNgfwPolicyGroup.setStatus(_B)
tptNgfwPolicyNotify=NotificationType((1,3,6,1,4,1,10734,3,9,3,0,10))
tptNgfwPolicyNotify.setObjects(*((_r,_s),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:tptNgfwPolicyNotify.setStatus(_B)
tptNgfwPolicyNotificationGroup=NotificationGroup((1,3,6,1,4,1,10734,3,9,1,1,8))
tptNgfwPolicyNotificationGroup.setObjects((_A,_v))
if mibBuilder.loadTexts:tptNgfwPolicyNotificationGroup.setStatus(_B)
tptNgfwPolicyCompl=ModuleCompliance((1,3,6,1,4,1,10734,3,9,1,2,4))
tptNgfwPolicyCompl.setObjects(*((_A,_w),(_A,_x)))
if mibBuilder.loadTexts:tptNgfwPolicyCompl.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'EventSource':EventSource,'FirewallEventType':FirewallEventType,'EventSeverity':EventSeverity,'ActionType':ActionType,'PacketTraceVersion':PacketTraceVersion,_w:tptNgfwPolicyGroup,_x:tptNgfwPolicyNotificationGroup,'tptNgfwPolicyCompl':tptNgfwPolicyCompl,'tptNgfwPolicy':tptNgfwPolicy,_v:tptNgfwPolicyNotify,_E:tptNgfwPolicyNotifyTime,_F:tptNgfwPolicyNotifyEventSource,_G:tptNgfwPolicyNotifyEventType,_H:tptNgfwPolicyNotifyEventSeverity,_I:tptNgfwPolicyNotifyCorrelationId,_J:tptNgfwPolicyNotifyActionType,_K:tptNgfwPolicyNotifyAction,_u:tptNgfwPolicyNotifyActionSetName,_L:tptNgfwPolicyNotifyRuleName,_M:tptNgfwPolicyNotifyInInterface,_N:tptNgfwPolicyNotifyOutInterface,_O:tptNgfwPolicyNotifySrcIpAddrType,_P:tptNgfwPolicyNotifySrcIpAddr,_Q:tptNgfwPolicyNotifySrcPort,_R:tptNgfwPolicyNotifySrcTransIpAddr,_S:tptNgfwPolicyNotifySrcTransPort,_T:tptNgfwPolicyNotifyDestIpAddrType,_U:tptNgfwPolicyNotifyDestIpAddr,_V:tptNgfwPolicyNotifyDestPort,_W:tptNgfwPolicyNotifyDestTransIpAddr,_X:tptNgfwPolicyNotifyDestTransPort,_Y:tptNgfwPolicyNotifyProtocol,_Z:tptNgfwPolicyNotifyApplicationName,_a:tptNgfwPolicyNotifyUserName,_b:tptNgfwPolicyNotifyBytesIn,_c:tptNgfwPolicyNotifyBytesOut,_d:tptNgfwPolicyNotifyStartTimeSec,_e:tptNgfwPolicyNotifyStartTimeNano,_f:tptNgfwPolicyNotifyRateLimit,_g:tptNgfwPolicyNotifyPktTraceVer,_h:tptNgfwPolicyNotifyPktTraceId,_i:tptNgfwPolicyNotifyPktTraceBegin,_j:tptNgfwPolicyNotifyPktTraceEnd,_k:tptNgfwPolicyNotifyFilterName,_l:tptNgfwPolicyNotifyProfileName,_m:tptNgfwPolicyNotifyPolicyName,_n:tptNgfwPolicyNotifyVlanId,_o:tptNgfwPolicyNotifyHitCount,_p:tptNgfwPolicyNotifyMsgParams,_q:tptNgfwPolicyNotifyPeriod})