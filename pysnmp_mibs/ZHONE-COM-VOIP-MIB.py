_A4='zhoneVoipServerBehaviorStringOne'
_A3='zhoneVoipMaliciousCallerEnable'
_A2='zhoneVoipMaliciousCallerRowStatus'
_A1='zhoneVoipServerHeaderMethod'
_A0='zhoneVoipServerExpiresRegister'
_z='zhoneVoipServerExpiresInvite'
_y='zhoneVoipServerSessionCalleeSpecifyRefresher'
_x='zhoneVoipServerSessionCallerSpecifyRefresher'
_w='zhoneVoipServerSessionCalleeReqTimer'
_v='zhoneVoipServerSessionCallerReqTimer'
_u='zhoneVoipServerSessionMinSE'
_t='zhoneVoipServerSessionExpiration'
_s='zhoneVoipServerSessionTimer'
_r='zhoneVoipSipDialPlanType'
_q='zhoneVoipServerRowStatus'
_p='zhoneVoipServerAddrType'
_o='zhoneVoipServerAddr'
_n='zhoneVoipServerUdpPortNumber'
_m='zhoneVoipServerId'
_l='zhoneVoipMaliciousCallerUri'
_k='nextVoipMaliciousCallerId'
_j='zhoneVoipHuntGroupDefaultCodec'
_i='zhoneVoipHuntGroupPortMembers'
_h='zhoneVoipSipDialDestName'
_g='zhoneVoipSipDialNumOfDigits'
_f='zhoneVoipSipDialPrefixStrip'
_e='zhoneVoipSipDialPrefixAdd'
_d='zhoneVoipHuntGroupRowStatus'
_c='zhoneVoipHuntGroupDestUri'
_b='nextZhoneVoipHuntGroupId'
_a='zhoneVoipSipDialPlanRowStatus'
_Z='zhoneVoipSipDialIpAddr'
_Y='zhoneVoipSipDialString'
_X='nextVoipSipDialPlanId'
_W='characters'
_V='zhoneVoipServerAddressIndex'
_U='zhoneVoipMaliciousCallerId'
_T='zhoneVoipHuntGroupId'
_S='zhoneVoipSipDialPlanId'
_R='ZhoneCodecType'
_Q='applIndex'
_P='NETWORK-SERVICES-MIB'
_O='InetAddressType'
_N='SnmpAdminString'
_M='not-accessible'
_L='Unsigned32'
_K='seconds'
_J='Bits'
_I='OctetString'
_H='read-only'
_G='TruthValue'
_F='read-write'
_E='deprecated'
_D='Integer32'
_C='ZHONE-COM-VOIP-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_O)
applIndex,=mibBuilder.importSymbols(_P,_Q)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_J,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_G)
ZhoneCodecType,=mibBuilder.importSymbols('ZHONE-GEN-SUBSCRIBER',_R)
zhoneVoice,=mibBuilder.importSymbols('Zhone','zhoneVoice')
ZhoneRowStatus,=mibBuilder.importSymbols('Zhone-TC','ZhoneRowStatus')
zhoneVoip=ModuleIdentity((1,3,6,1,4,1,5504,4,3,4))
if mibBuilder.loadTexts:zhoneVoip.setRevisions(('2014-10-16 23:33','2014-08-26 10:40','2014-07-03 02:40','2014-06-16 21:40','2014-05-22 14:09','2014-01-02 22:13','2012-09-17 23:42','2012-09-17 23:39','2011-12-22 02:24','2011-10-20 12:14','2011-07-25 11:44','2009-10-07 01:41','2009-03-21 02:08','2008-10-31 01:12','2008-08-27 23:02','2008-06-11 17:40','2007-07-16 02:45','2006-04-13 15:53','2005-10-11 11:46','2005-07-12 10:25','2005-07-07 16:06','2005-07-07 15:12','2005-06-01 11:09','2005-05-19 15:46','2005-05-14 21:24','2005-02-28 10:49','2004-11-01 14:34','2004-03-03 17:40','2004-02-24 12:36','2004-01-06 15:37','2003-11-06 10:08','2003-10-16 14:53','2003-08-27 11:30','2003-08-08 17:19','2003-05-28 12:00','2003-03-31 18:03','2003-02-18 14:32'))
_ZhoneVoipSystem_ObjectIdentity=ObjectIdentity
zhoneVoipSystem=_ZhoneVoipSystem_ObjectIdentity((1,3,6,1,4,1,5504,4,3,4,1))
if mibBuilder.loadTexts:zhoneVoipSystem.setStatus(_E)
class _ZhoneVoipSystemProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sip',1),('mgcp',2)))
_ZhoneVoipSystemProtocol_Type.__name__=_D
_ZhoneVoipSystemProtocol_Object=MibScalar
zhoneVoipSystemProtocol=_ZhoneVoipSystemProtocol_Object((1,3,6,1,4,1,5504,4,3,4,1,1),_ZhoneVoipSystemProtocol_Type())
zhoneVoipSystemProtocol.setMaxAccess(_H)
if mibBuilder.loadTexts:zhoneVoipSystemProtocol.setStatus(_E)
class _ZhoneVoipSystemSendCallProceedingTone_Type(TruthValue):defaultValue=2
_ZhoneVoipSystemSendCallProceedingTone_Type.__name__=_G
_ZhoneVoipSystemSendCallProceedingTone_Object=MibScalar
zhoneVoipSystemSendCallProceedingTone=_ZhoneVoipSystemSendCallProceedingTone_Object((1,3,6,1,4,1,5504,4,3,4,1,2),_ZhoneVoipSystemSendCallProceedingTone_Type())
zhoneVoipSystemSendCallProceedingTone.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneVoipSystemSendCallProceedingTone.setStatus(_E)
class _ZhoneVoipSystemRtcpEnabled_Type(TruthValue):defaultValue=2
_ZhoneVoipSystemRtcpEnabled_Type.__name__=_G
_ZhoneVoipSystemRtcpEnabled_Object=MibScalar
zhoneVoipSystemRtcpEnabled=_ZhoneVoipSystemRtcpEnabled_Object((1,3,6,1,4,1,5504,4,3,4,1,3),_ZhoneVoipSystemRtcpEnabled_Type())
zhoneVoipSystemRtcpEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneVoipSystemRtcpEnabled.setStatus(_E)
class _ZhoneVoipSystemRtcpPacketInterval_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2500,10000))
_ZhoneVoipSystemRtcpPacketInterval_Type.__name__=_D
_ZhoneVoipSystemRtcpPacketInterval_Object=MibScalar
zhoneVoipSystemRtcpPacketInterval=_ZhoneVoipSystemRtcpPacketInterval_Object((1,3,6,1,4,1,5504,4,3,4,1,4),_ZhoneVoipSystemRtcpPacketInterval_Type())
zhoneVoipSystemRtcpPacketInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneVoipSystemRtcpPacketInterval.setStatus(_E)
class _ZhoneVoipSystemInterdigitTimeout_Type(Integer32):defaultValue=10
_ZhoneVoipSystemInterdigitTimeout_Type.__name__=_D
_ZhoneVoipSystemInterdigitTimeout_Object=MibScalar
zhoneVoipSystemInterdigitTimeout=_ZhoneVoipSystemInterdigitTimeout_Object((1,3,6,1,4,1,5504,4,3,4,1,5),_ZhoneVoipSystemInterdigitTimeout_Type())
zhoneVoipSystemInterdigitTimeout.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneVoipSystemInterdigitTimeout.setStatus(_E)
class _ZhoneVoipSystemIpTos_Type(Integer32):defaultValue=0
_ZhoneVoipSystemIpTos_Type.__name__=_D
_ZhoneVoipSystemIpTos_Object=MibScalar
zhoneVoipSystemIpTos=_ZhoneVoipSystemIpTos_Object((1,3,6,1,4,1,5504,4,3,4,1,6),_ZhoneVoipSystemIpTos_Type())
zhoneVoipSystemIpTos.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneVoipSystemIpTos.setStatus(_E)
_ZhoneVoipSystemDomainName_Type=SnmpAdminString
_ZhoneVoipSystemDomainName_Object=MibScalar
zhoneVoipSystemDomainName=_ZhoneVoipSystemDomainName_Object((1,3,6,1,4,1,5504,4,3,4,1,7),_ZhoneVoipSystemDomainName_Type())
zhoneVoipSystemDomainName.setMaxAccess(_H)
if mibBuilder.loadTexts:zhoneVoipSystemDomainName.setStatus(_E)
_ZhoneVoipSipDialPlan_ObjectIdentity=ObjectIdentity
zhoneVoipSipDialPlan=_ZhoneVoipSipDialPlan_ObjectIdentity((1,3,6,1,4,1,5504,4,3,4,3))
_NextVoipSipDialPlanId_Type=Integer32
_NextVoipSipDialPlanId_Object=MibScalar
nextVoipSipDialPlanId=_NextVoipSipDialPlanId_Object((1,3,6,1,4,1,5504,4,3,4,3,1),_NextVoipSipDialPlanId_Type())
nextVoipSipDialPlanId.setMaxAccess(_H)
if mibBuilder.loadTexts:nextVoipSipDialPlanId.setStatus(_A)
_ZhoneVoipSipDialPlanTable_Object=MibTable
zhoneVoipSipDialPlanTable=_ZhoneVoipSipDialPlanTable_Object((1,3,6,1,4,1,5504,4,3,4,3,2))
if mibBuilder.loadTexts:zhoneVoipSipDialPlanTable.setStatus(_A)
_ZhoneVoipSipDialPlanEntry_Object=MibTableRow
zhoneVoipSipDialPlanEntry=_ZhoneVoipSipDialPlanEntry_Object((1,3,6,1,4,1,5504,4,3,4,3,2,1))
zhoneVoipSipDialPlanEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:zhoneVoipSipDialPlanEntry.setStatus(_A)
class _ZhoneVoipSipDialPlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ZhoneVoipSipDialPlanId_Type.__name__=_D
_ZhoneVoipSipDialPlanId_Object=MibTableColumn
zhoneVoipSipDialPlanId=_ZhoneVoipSipDialPlanId_Object((1,3,6,1,4,1,5504,4,3,4,3,2,1,1),_ZhoneVoipSipDialPlanId_Type())
zhoneVoipSipDialPlanId.setMaxAccess(_M)
if mibBuilder.loadTexts:zhoneVoipSipDialPlanId.setStatus(_A)
class _ZhoneVoipSipDialString_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_ZhoneVoipSipDialString_Type.__name__=_N
_ZhoneVoipSipDialString_Object=MibTableColumn
zhoneVoipSipDialString=_ZhoneVoipSipDialString_Object((1,3,6,1,4,1,5504,4,3,4,3,2,1,2),_ZhoneVoipSipDialString_Type())
zhoneVoipSipDialString.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipSipDialString.setStatus(_A)
_ZhoneVoipSipDialIpAddr_Type=IpAddress
_ZhoneVoipSipDialIpAddr_Object=MibTableColumn
zhoneVoipSipDialIpAddr=_ZhoneVoipSipDialIpAddr_Object((1,3,6,1,4,1,5504,4,3,4,3,2,1,3),_ZhoneVoipSipDialIpAddr_Type())
zhoneVoipSipDialIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipSipDialIpAddr.setStatus(_A)
_ZhoneVoipSipDialPlanRowStatus_Type=ZhoneRowStatus
_ZhoneVoipSipDialPlanRowStatus_Object=MibTableColumn
zhoneVoipSipDialPlanRowStatus=_ZhoneVoipSipDialPlanRowStatus_Object((1,3,6,1,4,1,5504,4,3,4,3,2,1,4),_ZhoneVoipSipDialPlanRowStatus_Type())
zhoneVoipSipDialPlanRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipSipDialPlanRowStatus.setStatus(_A)
_ZhoneVoipSipDialDestName_Type=SnmpAdminString
_ZhoneVoipSipDialDestName_Object=MibTableColumn
zhoneVoipSipDialDestName=_ZhoneVoipSipDialDestName_Object((1,3,6,1,4,1,5504,4,3,4,3,2,1,5),_ZhoneVoipSipDialDestName_Type())
zhoneVoipSipDialDestName.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipSipDialDestName.setStatus(_A)
class _ZhoneVoipSipDialNumOfDigits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_ZhoneVoipSipDialNumOfDigits_Type.__name__=_D
_ZhoneVoipSipDialNumOfDigits_Object=MibTableColumn
zhoneVoipSipDialNumOfDigits=_ZhoneVoipSipDialNumOfDigits_Object((1,3,6,1,4,1,5504,4,3,4,3,2,1,6),_ZhoneVoipSipDialNumOfDigits_Type())
zhoneVoipSipDialNumOfDigits.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipSipDialNumOfDigits.setStatus(_A)
class _ZhoneVoipSipDialPrefixStrip_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_ZhoneVoipSipDialPrefixStrip_Type.__name__=_D
_ZhoneVoipSipDialPrefixStrip_Object=MibTableColumn
zhoneVoipSipDialPrefixStrip=_ZhoneVoipSipDialPrefixStrip_Object((1,3,6,1,4,1,5504,4,3,4,3,2,1,7),_ZhoneVoipSipDialPrefixStrip_Type())
zhoneVoipSipDialPrefixStrip.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipSipDialPrefixStrip.setStatus(_A)
_ZhoneVoipSipDialPrefixAdd_Type=SnmpAdminString
_ZhoneVoipSipDialPrefixAdd_Object=MibTableColumn
zhoneVoipSipDialPrefixAdd=_ZhoneVoipSipDialPrefixAdd_Object((1,3,6,1,4,1,5504,4,3,4,3,2,1,8),_ZhoneVoipSipDialPrefixAdd_Type())
zhoneVoipSipDialPrefixAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipSipDialPrefixAdd.setStatus(_A)
class _ZhoneVoipSipDialPlanType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('normal',1),('callpark',2),('esa',3),('isdnsig',4),('intercom',5)))
_ZhoneVoipSipDialPlanType_Type.__name__=_D
_ZhoneVoipSipDialPlanType_Object=MibTableColumn
zhoneVoipSipDialPlanType=_ZhoneVoipSipDialPlanType_Object((1,3,6,1,4,1,5504,4,3,4,3,2,1,9),_ZhoneVoipSipDialPlanType_Type())
zhoneVoipSipDialPlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipSipDialPlanType.setStatus(_A)
class _ZhoneVoipServerEntryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZhoneVoipServerEntryIndex_Type.__name__=_D
_ZhoneVoipServerEntryIndex_Object=MibTableColumn
zhoneVoipServerEntryIndex=_ZhoneVoipServerEntryIndex_Object((1,3,6,1,4,1,5504,4,3,4,3,2,1,10),_ZhoneVoipServerEntryIndex_Type())
zhoneVoipServerEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerEntryIndex.setStatus(_A)
_ZhoneVoipOverrideInterdigitTimeout_Type=Integer32
_ZhoneVoipOverrideInterdigitTimeout_Object=MibTableColumn
zhoneVoipOverrideInterdigitTimeout=_ZhoneVoipOverrideInterdigitTimeout_Object((1,3,6,1,4,1,5504,4,3,4,3,2,1,11),_ZhoneVoipOverrideInterdigitTimeout_Type())
zhoneVoipOverrideInterdigitTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipOverrideInterdigitTimeout.setStatus(_A)
class _ZhoneVoipSipDialPlanClass_Type(Bits):namedValues=NamedValues(('emergency',0))
_ZhoneVoipSipDialPlanClass_Type.__name__=_J
_ZhoneVoipSipDialPlanClass_Object=MibTableColumn
zhoneVoipSipDialPlanClass=_ZhoneVoipSipDialPlanClass_Object((1,3,6,1,4,1,5504,4,3,4,3,2,1,12),_ZhoneVoipSipDialPlanClass_Type())
zhoneVoipSipDialPlanClass.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipSipDialPlanClass.setStatus(_A)
_ZhoneVoipSipDialPlanDescription_Type=SnmpAdminString
_ZhoneVoipSipDialPlanDescription_Object=MibTableColumn
zhoneVoipSipDialPlanDescription=_ZhoneVoipSipDialPlanDescription_Object((1,3,6,1,4,1,5504,4,3,4,3,2,1,13),_ZhoneVoipSipDialPlanDescription_Type())
zhoneVoipSipDialPlanDescription.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneVoipSipDialPlanDescription.setStatus(_A)
_ZhoneVoipHuntGroup_ObjectIdentity=ObjectIdentity
zhoneVoipHuntGroup=_ZhoneVoipHuntGroup_ObjectIdentity((1,3,6,1,4,1,5504,4,3,4,4))
_NextZhoneVoipHuntGroupId_Type=Integer32
_NextZhoneVoipHuntGroupId_Object=MibScalar
nextZhoneVoipHuntGroupId=_NextZhoneVoipHuntGroupId_Object((1,3,6,1,4,1,5504,4,3,4,4,2),_NextZhoneVoipHuntGroupId_Type())
nextZhoneVoipHuntGroupId.setMaxAccess(_H)
if mibBuilder.loadTexts:nextZhoneVoipHuntGroupId.setStatus(_A)
_ZhoneVoipHuntGroupTable_Object=MibTable
zhoneVoipHuntGroupTable=_ZhoneVoipHuntGroupTable_Object((1,3,6,1,4,1,5504,4,3,4,4,3))
if mibBuilder.loadTexts:zhoneVoipHuntGroupTable.setStatus(_A)
_ZhoneVoipHuntGroupEntry_Object=MibTableRow
zhoneVoipHuntGroupEntry=_ZhoneVoipHuntGroupEntry_Object((1,3,6,1,4,1,5504,4,3,4,4,3,1))
zhoneVoipHuntGroupEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:zhoneVoipHuntGroupEntry.setStatus(_A)
class _ZhoneVoipHuntGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ZhoneVoipHuntGroupId_Type.__name__=_D
_ZhoneVoipHuntGroupId_Object=MibTableColumn
zhoneVoipHuntGroupId=_ZhoneVoipHuntGroupId_Object((1,3,6,1,4,1,5504,4,3,4,4,3,1,1),_ZhoneVoipHuntGroupId_Type())
zhoneVoipHuntGroupId.setMaxAccess(_M)
if mibBuilder.loadTexts:zhoneVoipHuntGroupId.setStatus(_A)
class _ZhoneVoipHuntGroupDestUri_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_ZhoneVoipHuntGroupDestUri_Type.__name__=_N
_ZhoneVoipHuntGroupDestUri_Object=MibTableColumn
zhoneVoipHuntGroupDestUri=_ZhoneVoipHuntGroupDestUri_Object((1,3,6,1,4,1,5504,4,3,4,4,3,1,2),_ZhoneVoipHuntGroupDestUri_Type())
zhoneVoipHuntGroupDestUri.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipHuntGroupDestUri.setStatus(_A)
class _ZhoneVoipHuntGroupDefaultCodec_Type(ZhoneCodecType):defaultValue=1
_ZhoneVoipHuntGroupDefaultCodec_Type.__name__=_R
_ZhoneVoipHuntGroupDefaultCodec_Object=MibTableColumn
zhoneVoipHuntGroupDefaultCodec=_ZhoneVoipHuntGroupDefaultCodec_Object((1,3,6,1,4,1,5504,4,3,4,4,3,1,3),_ZhoneVoipHuntGroupDefaultCodec_Type())
zhoneVoipHuntGroupDefaultCodec.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipHuntGroupDefaultCodec.setStatus(_A)
class _ZhoneVoipHuntGroupPortMembers_Type(Bits):namedValues=NamedValues(*(('port1',0),('port2',1),('port3',2),('port4',3),('port5',4),('port6',5),('port7',6),('port8',7),('port9',8),('port10',9),('port11',10),('port12',11),('port13',12),('port14',13),('port15',14),('port16',15),('port17',16),('port18',17),('port19',18),('port20',19),('port21',20),('port22',21),('port23',22),('port24',23)))
_ZhoneVoipHuntGroupPortMembers_Type.__name__=_J
_ZhoneVoipHuntGroupPortMembers_Object=MibTableColumn
zhoneVoipHuntGroupPortMembers=_ZhoneVoipHuntGroupPortMembers_Object((1,3,6,1,4,1,5504,4,3,4,4,3,1,4),_ZhoneVoipHuntGroupPortMembers_Type())
zhoneVoipHuntGroupPortMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipHuntGroupPortMembers.setStatus(_A)
_ZhoneVoipHuntGroupRowStatus_Type=ZhoneRowStatus
_ZhoneVoipHuntGroupRowStatus_Object=MibTableColumn
zhoneVoipHuntGroupRowStatus=_ZhoneVoipHuntGroupRowStatus_Object((1,3,6,1,4,1,5504,4,3,4,4,3,1,5),_ZhoneVoipHuntGroupRowStatus_Type())
zhoneVoipHuntGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipHuntGroupRowStatus.setStatus(_A)
_ZhoneVoipMaliciousCaller_ObjectIdentity=ObjectIdentity
zhoneVoipMaliciousCaller=_ZhoneVoipMaliciousCaller_ObjectIdentity((1,3,6,1,4,1,5504,4,3,4,5))
_NextVoipMaliciousCallerId_Type=Integer32
_NextVoipMaliciousCallerId_Object=MibScalar
nextVoipMaliciousCallerId=_NextVoipMaliciousCallerId_Object((1,3,6,1,4,1,5504,4,3,4,5,1),_NextVoipMaliciousCallerId_Type())
nextVoipMaliciousCallerId.setMaxAccess(_H)
if mibBuilder.loadTexts:nextVoipMaliciousCallerId.setStatus(_A)
_ZhoneVoipMaliciousCallerTable_Object=MibTable
zhoneVoipMaliciousCallerTable=_ZhoneVoipMaliciousCallerTable_Object((1,3,6,1,4,1,5504,4,3,4,5,2))
if mibBuilder.loadTexts:zhoneVoipMaliciousCallerTable.setStatus(_A)
_ZhoneVoipMaliciousCallerEntry_Object=MibTableRow
zhoneVoipMaliciousCallerEntry=_ZhoneVoipMaliciousCallerEntry_Object((1,3,6,1,4,1,5504,4,3,4,5,2,1))
zhoneVoipMaliciousCallerEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:zhoneVoipMaliciousCallerEntry.setStatus(_A)
class _ZhoneVoipMaliciousCallerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ZhoneVoipMaliciousCallerId_Type.__name__=_D
_ZhoneVoipMaliciousCallerId_Object=MibTableColumn
zhoneVoipMaliciousCallerId=_ZhoneVoipMaliciousCallerId_Object((1,3,6,1,4,1,5504,4,3,4,5,2,1,1),_ZhoneVoipMaliciousCallerId_Type())
zhoneVoipMaliciousCallerId.setMaxAccess(_M)
if mibBuilder.loadTexts:zhoneVoipMaliciousCallerId.setStatus(_A)
_ZhoneVoipMaliciousCallerUri_Type=SnmpAdminString
_ZhoneVoipMaliciousCallerUri_Object=MibTableColumn
zhoneVoipMaliciousCallerUri=_ZhoneVoipMaliciousCallerUri_Object((1,3,6,1,4,1,5504,4,3,4,5,2,1,2),_ZhoneVoipMaliciousCallerUri_Type())
zhoneVoipMaliciousCallerUri.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipMaliciousCallerUri.setStatus(_A)
class _ZhoneVoipMaliciousCallerEnable_Type(TruthValue):defaultValue=1
_ZhoneVoipMaliciousCallerEnable_Type.__name__=_G
_ZhoneVoipMaliciousCallerEnable_Object=MibTableColumn
zhoneVoipMaliciousCallerEnable=_ZhoneVoipMaliciousCallerEnable_Object((1,3,6,1,4,1,5504,4,3,4,5,2,1,3),_ZhoneVoipMaliciousCallerEnable_Type())
zhoneVoipMaliciousCallerEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipMaliciousCallerEnable.setStatus(_A)
_ZhoneVoipMaliciousCallerRowStatus_Type=ZhoneRowStatus
_ZhoneVoipMaliciousCallerRowStatus_Object=MibTableColumn
zhoneVoipMaliciousCallerRowStatus=_ZhoneVoipMaliciousCallerRowStatus_Object((1,3,6,1,4,1,5504,4,3,4,5,2,1,4),_ZhoneVoipMaliciousCallerRowStatus_Type())
zhoneVoipMaliciousCallerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipMaliciousCallerRowStatus.setStatus(_A)
_ZhoneVoipServerCfg_ObjectIdentity=ObjectIdentity
zhoneVoipServerCfg=_ZhoneVoipServerCfg_ObjectIdentity((1,3,6,1,4,1,5504,4,3,4,6))
_ZhoneVoipServerTable_Object=MibTable
zhoneVoipServerTable=_ZhoneVoipServerTable_Object((1,3,6,1,4,1,5504,4,3,4,6,1))
if mibBuilder.loadTexts:zhoneVoipServerTable.setStatus(_A)
_ZhoneVoipServerEntry_Object=MibTableRow
zhoneVoipServerEntry=_ZhoneVoipServerEntry_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1))
zhoneVoipServerEntry.setIndexNames((0,_P,_Q),(0,_C,_V))
if mibBuilder.loadTexts:zhoneVoipServerEntry.setStatus(_A)
_ZhoneVoipServerAddressIndex_Type=Unsigned32
_ZhoneVoipServerAddressIndex_Object=MibTableColumn
zhoneVoipServerAddressIndex=_ZhoneVoipServerAddressIndex_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,1),_ZhoneVoipServerAddressIndex_Type())
zhoneVoipServerAddressIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:zhoneVoipServerAddressIndex.setStatus(_A)
_ZhoneVoipServerRowStatus_Type=ZhoneRowStatus
_ZhoneVoipServerRowStatus_Object=MibTableColumn
zhoneVoipServerRowStatus=_ZhoneVoipServerRowStatus_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,2),_ZhoneVoipServerRowStatus_Type())
zhoneVoipServerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerRowStatus.setStatus(_A)
class _ZhoneVoipServerAddrType_Type(InetAddressType):defaultValue=1
_ZhoneVoipServerAddrType_Type.__name__=_O
_ZhoneVoipServerAddrType_Object=MibTableColumn
zhoneVoipServerAddrType=_ZhoneVoipServerAddrType_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,3),_ZhoneVoipServerAddrType_Type())
zhoneVoipServerAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerAddrType.setStatus(_A)
_ZhoneVoipServerAddr_Type=InetAddress
_ZhoneVoipServerAddr_Object=MibTableColumn
zhoneVoipServerAddr=_ZhoneVoipServerAddr_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,4),_ZhoneVoipServerAddr_Type())
zhoneVoipServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerAddr.setStatus(_A)
class _ZhoneVoipServerUdpPortNumber_Type(Integer32):defaultValue=2427;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZhoneVoipServerUdpPortNumber_Type.__name__=_D
_ZhoneVoipServerUdpPortNumber_Object=MibTableColumn
zhoneVoipServerUdpPortNumber=_ZhoneVoipServerUdpPortNumber_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,5),_ZhoneVoipServerUdpPortNumber_Type())
zhoneVoipServerUdpPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerUdpPortNumber.setStatus(_A)
class _ZhoneVoipServerId_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38)));namedValues=NamedValues(*(('longboard',1),('asterisk',2),('sipexpressrouter',3),('metaswitch',4),('sylantro',5),('broadsoft',6),('ubiquity',7),('generalbandwidth',8),('tekelec-T6000',9),('generic',10),('sonus',11),('siemens',12),('tekelec-T9000',13),('lucent-telica',14),('nortel-cs2000',15),('nuera',16),('lucent-imerge',17),('coppercom',18),('newcross',19),('cisco-bts',20),('cirpack-utp',21),('italtel-issw',22),('cisco-pgw',23),('microtrol-msk10',24),('nortel-dms10',25),('verso-clarent-c5cm',26),('cedarpoint-safari',27),('huawei-softx3000',28),('nortel-cs1500',29),('taqua-t7000',30),('utstarcom-mswitch',31),('broadsoft-broadworks',32),('broadsoft-m6',33),('genband-g9',34),('netcentrex',35),('genband-g6',36),('alu-5060',37),('ericsson-apz60',38)))
_ZhoneVoipServerId_Type.__name__=_D
_ZhoneVoipServerId_Object=MibTableColumn
zhoneVoipServerId=_ZhoneVoipServerId_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,6),_ZhoneVoipServerId_Type())
zhoneVoipServerId.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerId.setStatus(_A)
class _ZhoneVoipServerProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('sip',1),('mgcp',2),('megaco',3),('ncs',4)))
_ZhoneVoipServerProtocol_Type.__name__=_D
_ZhoneVoipServerProtocol_Object=MibTableColumn
zhoneVoipServerProtocol=_ZhoneVoipServerProtocol_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,7),_ZhoneVoipServerProtocol_Type())
zhoneVoipServerProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerProtocol.setStatus(_A)
class _ZhoneVoipServerSendCallProceedingTone_Type(TruthValue):defaultValue=2
_ZhoneVoipServerSendCallProceedingTone_Type.__name__=_G
_ZhoneVoipServerSendCallProceedingTone_Object=MibTableColumn
zhoneVoipServerSendCallProceedingTone=_ZhoneVoipServerSendCallProceedingTone_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,8),_ZhoneVoipServerSendCallProceedingTone_Type())
zhoneVoipServerSendCallProceedingTone.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerSendCallProceedingTone.setStatus(_A)
class _ZhoneVoipServerRtcpEnabled_Type(TruthValue):defaultValue=2
_ZhoneVoipServerRtcpEnabled_Type.__name__=_G
_ZhoneVoipServerRtcpEnabled_Object=MibTableColumn
zhoneVoipServerRtcpEnabled=_ZhoneVoipServerRtcpEnabled_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,9),_ZhoneVoipServerRtcpEnabled_Type())
zhoneVoipServerRtcpEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerRtcpEnabled.setStatus(_A)
class _ZhoneVoipServerRtcpPacketInterval_Type(Integer32):defaultValue=5000
_ZhoneVoipServerRtcpPacketInterval_Type.__name__=_D
_ZhoneVoipServerRtcpPacketInterval_Object=MibTableColumn
zhoneVoipServerRtcpPacketInterval=_ZhoneVoipServerRtcpPacketInterval_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,10),_ZhoneVoipServerRtcpPacketInterval_Type())
zhoneVoipServerRtcpPacketInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerRtcpPacketInterval.setStatus(_A)
class _ZhoneVoipServerInterDigitTimeout_Type(Integer32):defaultValue=10
_ZhoneVoipServerInterDigitTimeout_Type.__name__=_D
_ZhoneVoipServerInterDigitTimeout_Object=MibTableColumn
zhoneVoipServerInterDigitTimeout=_ZhoneVoipServerInterDigitTimeout_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,11),_ZhoneVoipServerInterDigitTimeout_Type())
zhoneVoipServerInterDigitTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerInterDigitTimeout.setStatus(_A)
class _ZhoneVoipServerIpTos_Type(Integer32):defaultValue=0
_ZhoneVoipServerIpTos_Type.__name__=_D
_ZhoneVoipServerIpTos_Object=MibTableColumn
zhoneVoipServerIpTos=_ZhoneVoipServerIpTos_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,12),_ZhoneVoipServerIpTos_Type())
zhoneVoipServerIpTos.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerIpTos.setStatus(_A)
_ZhoneVoipServerDomainName_Type=SnmpAdminString
_ZhoneVoipServerDomainName_Object=MibTableColumn
zhoneVoipServerDomainName=_ZhoneVoipServerDomainName_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,13),_ZhoneVoipServerDomainName_Type())
zhoneVoipServerDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerDomainName.setStatus(_A)
_ZhoneVoipServerExpiresInvite_Type=Unsigned32
_ZhoneVoipServerExpiresInvite_Object=MibTableColumn
zhoneVoipServerExpiresInvite=_ZhoneVoipServerExpiresInvite_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,14),_ZhoneVoipServerExpiresInvite_Type())
zhoneVoipServerExpiresInvite.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerExpiresInvite.setStatus(_A)
if mibBuilder.loadTexts:zhoneVoipServerExpiresInvite.setUnits(_K)
_ZhoneVoipServerExpiresRegister_Type=Unsigned32
_ZhoneVoipServerExpiresRegister_Object=MibTableColumn
zhoneVoipServerExpiresRegister=_ZhoneVoipServerExpiresRegister_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,15),_ZhoneVoipServerExpiresRegister_Type())
zhoneVoipServerExpiresRegister.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerExpiresRegister.setStatus(_A)
if mibBuilder.loadTexts:zhoneVoipServerExpiresRegister.setUnits(_K)
class _ZhoneVoipServerHeaderMethod_Type(Bits):namedValues=NamedValues(*(('invite',0),('register',1)))
_ZhoneVoipServerHeaderMethod_Type.__name__=_J
_ZhoneVoipServerHeaderMethod_Object=MibTableColumn
zhoneVoipServerHeaderMethod=_ZhoneVoipServerHeaderMethod_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,16),_ZhoneVoipServerHeaderMethod_Type())
zhoneVoipServerHeaderMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerHeaderMethod.setStatus(_A)
class _ZhoneVoipServerSessionTimer_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_ZhoneVoipServerSessionTimer_Type.__name__=_D
_ZhoneVoipServerSessionTimer_Object=MibTableColumn
zhoneVoipServerSessionTimer=_ZhoneVoipServerSessionTimer_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,17),_ZhoneVoipServerSessionTimer_Type())
zhoneVoipServerSessionTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerSessionTimer.setStatus(_A)
class _ZhoneVoipServerSessionExpiration_Type(Unsigned32):defaultValue=180;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(90,2147483647))
_ZhoneVoipServerSessionExpiration_Type.__name__=_L
_ZhoneVoipServerSessionExpiration_Object=MibTableColumn
zhoneVoipServerSessionExpiration=_ZhoneVoipServerSessionExpiration_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,18),_ZhoneVoipServerSessionExpiration_Type())
zhoneVoipServerSessionExpiration.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerSessionExpiration.setStatus(_A)
if mibBuilder.loadTexts:zhoneVoipServerSessionExpiration.setUnits(_K)
class _ZhoneVoipServerSessionMinSE_Type(Unsigned32):defaultValue=180;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(90,2147483647))
_ZhoneVoipServerSessionMinSE_Type.__name__=_L
_ZhoneVoipServerSessionMinSE_Object=MibTableColumn
zhoneVoipServerSessionMinSE=_ZhoneVoipServerSessionMinSE_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,19),_ZhoneVoipServerSessionMinSE_Type())
zhoneVoipServerSessionMinSE.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerSessionMinSE.setStatus(_A)
if mibBuilder.loadTexts:zhoneVoipServerSessionMinSE.setUnits(_K)
class _ZhoneVoipServerSessionCallerReqTimer_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_ZhoneVoipServerSessionCallerReqTimer_Type.__name__=_D
_ZhoneVoipServerSessionCallerReqTimer_Object=MibTableColumn
zhoneVoipServerSessionCallerReqTimer=_ZhoneVoipServerSessionCallerReqTimer_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,20),_ZhoneVoipServerSessionCallerReqTimer_Type())
zhoneVoipServerSessionCallerReqTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerSessionCallerReqTimer.setStatus(_A)
class _ZhoneVoipServerSessionCalleeReqTimer_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_ZhoneVoipServerSessionCalleeReqTimer_Type.__name__=_D
_ZhoneVoipServerSessionCalleeReqTimer_Object=MibTableColumn
zhoneVoipServerSessionCalleeReqTimer=_ZhoneVoipServerSessionCalleeReqTimer_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,21),_ZhoneVoipServerSessionCalleeReqTimer_Type())
zhoneVoipServerSessionCalleeReqTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerSessionCalleeReqTimer.setStatus(_A)
class _ZhoneVoipServerSessionCallerSpecifyRefresher_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('uac',1),('uas',2),('omit',3)))
_ZhoneVoipServerSessionCallerSpecifyRefresher_Type.__name__=_D
_ZhoneVoipServerSessionCallerSpecifyRefresher_Object=MibTableColumn
zhoneVoipServerSessionCallerSpecifyRefresher=_ZhoneVoipServerSessionCallerSpecifyRefresher_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,22),_ZhoneVoipServerSessionCallerSpecifyRefresher_Type())
zhoneVoipServerSessionCallerSpecifyRefresher.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerSessionCallerSpecifyRefresher.setStatus(_A)
class _ZhoneVoipServerSessionCalleeSpecifyRefresher_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uac',1),('uas',2)))
_ZhoneVoipServerSessionCalleeSpecifyRefresher_Type.__name__=_D
_ZhoneVoipServerSessionCalleeSpecifyRefresher_Object=MibTableColumn
zhoneVoipServerSessionCalleeSpecifyRefresher=_ZhoneVoipServerSessionCalleeSpecifyRefresher_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,23),_ZhoneVoipServerSessionCalleeSpecifyRefresher_Type())
zhoneVoipServerSessionCalleeSpecifyRefresher.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerSessionCalleeSpecifyRefresher.setStatus(_A)
class _ZhoneVoipServerDtmfMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inband',1),('rfc2833',2),('rfc2833only',3)))
_ZhoneVoipServerDtmfMode_Type.__name__=_D
_ZhoneVoipServerDtmfMode_Object=MibTableColumn
zhoneVoipServerDtmfMode=_ZhoneVoipServerDtmfMode_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,24),_ZhoneVoipServerDtmfMode_Type())
zhoneVoipServerDtmfMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerDtmfMode.setStatus(_A)
class _ZhoneVoipServerBehaviorStringOne_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_ZhoneVoipServerBehaviorStringOne_Type.__name__=_I
_ZhoneVoipServerBehaviorStringOne_Object=MibTableColumn
zhoneVoipServerBehaviorStringOne=_ZhoneVoipServerBehaviorStringOne_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,25),_ZhoneVoipServerBehaviorStringOne_Type())
zhoneVoipServerBehaviorStringOne.setMaxAccess(_H)
if mibBuilder.loadTexts:zhoneVoipServerBehaviorStringOne.setStatus(_A)
if mibBuilder.loadTexts:zhoneVoipServerBehaviorStringOne.setUnits(_W)
class _ZhoneVoipServerRtpTermIdSyntax_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,96))
_ZhoneVoipServerRtpTermIdSyntax_Type.__name__=_I
_ZhoneVoipServerRtpTermIdSyntax_Object=MibTableColumn
zhoneVoipServerRtpTermIdSyntax=_ZhoneVoipServerRtpTermIdSyntax_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,26),_ZhoneVoipServerRtpTermIdSyntax_Type())
zhoneVoipServerRtpTermIdSyntax.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneVoipServerRtpTermIdSyntax.setStatus(_A)
if mibBuilder.loadTexts:zhoneVoipServerRtpTermIdSyntax.setUnits(_W)
class _ZhoneVoipServerRtpDSCP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_ZhoneVoipServerRtpDSCP_Type.__name__=_I
_ZhoneVoipServerRtpDSCP_Object=MibTableColumn
zhoneVoipServerRtpDSCP=_ZhoneVoipServerRtpDSCP_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,27),_ZhoneVoipServerRtpDSCP_Type())
zhoneVoipServerRtpDSCP.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerRtpDSCP.setStatus(_A)
class _ZhoneVoipServerSignalingDSCP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_ZhoneVoipServerSignalingDSCP_Type.__name__=_I
_ZhoneVoipServerSignalingDSCP_Object=MibTableColumn
zhoneVoipServerSignalingDSCP=_ZhoneVoipServerSignalingDSCP_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,28),_ZhoneVoipServerSignalingDSCP_Type())
zhoneVoipServerSignalingDSCP.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerSignalingDSCP.setStatus(_A)
class _ZhoneVoipServerDtmfPayloadId_Type(Integer32):defaultValue=101;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(96,127))
_ZhoneVoipServerDtmfPayloadId_Type.__name__=_D
_ZhoneVoipServerDtmfPayloadId_Object=MibTableColumn
zhoneVoipServerDtmfPayloadId=_ZhoneVoipServerDtmfPayloadId_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,29),_ZhoneVoipServerDtmfPayloadId_Type())
zhoneVoipServerDtmfPayloadId.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneVoipServerDtmfPayloadId.setStatus(_A)
class _ZhoneVoipServerRegisterReadyTimeout_Type(Unsigned32):defaultValue=10
_ZhoneVoipServerRegisterReadyTimeout_Type.__name__=_L
_ZhoneVoipServerRegisterReadyTimeout_Object=MibTableColumn
zhoneVoipServerRegisterReadyTimeout=_ZhoneVoipServerRegisterReadyTimeout_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,30),_ZhoneVoipServerRegisterReadyTimeout_Type())
zhoneVoipServerRegisterReadyTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerRegisterReadyTimeout.setStatus(_A)
if mibBuilder.loadTexts:zhoneVoipServerRegisterReadyTimeout.setUnits(_K)
class _ZhoneVoipServerMessageRetryCount_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_ZhoneVoipServerMessageRetryCount_Type.__name__=_D
_ZhoneVoipServerMessageRetryCount_Object=MibTableColumn
zhoneVoipServerMessageRetryCount=_ZhoneVoipServerMessageRetryCount_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,31),_ZhoneVoipServerMessageRetryCount_Type())
zhoneVoipServerMessageRetryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerMessageRetryCount.setStatus(_A)
class _ZhoneVoipServerFeatures_Type(Bits):namedValues=NamedValues(*(('sip-outbound',0),('gruu',1)))
_ZhoneVoipServerFeatures_Type.__name__=_J
_ZhoneVoipServerFeatures_Object=MibTableColumn
zhoneVoipServerFeatures=_ZhoneVoipServerFeatures_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,32),_ZhoneVoipServerFeatures_Type())
zhoneVoipServerFeatures.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerFeatures.setStatus(_A)
class _ZhoneVoipServerTransportProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('udp',1),('tcp',2)))
_ZhoneVoipServerTransportProtocol_Type.__name__=_D
_ZhoneVoipServerTransportProtocol_Object=MibTableColumn
zhoneVoipServerTransportProtocol=_ZhoneVoipServerTransportProtocol_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,33),_ZhoneVoipServerTransportProtocol_Type())
zhoneVoipServerTransportProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipServerTransportProtocol.setStatus(_A)
class _ZhoneVoipSigLocalPortNumber_Type(Integer32):defaultValue=5060;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZhoneVoipSigLocalPortNumber_Type.__name__=_D
_ZhoneVoipSigLocalPortNumber_Object=MibTableColumn
zhoneVoipSigLocalPortNumber=_ZhoneVoipSigLocalPortNumber_Object((1,3,6,1,4,1,5504,4,3,4,6,1,1,34),_ZhoneVoipSigLocalPortNumber_Type())
zhoneVoipSigLocalPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:zhoneVoipSigLocalPortNumber.setStatus(_A)
zhoneVoipObjects=ObjectGroup((1,3,6,1,4,1,5504,4,3,4,2))
zhoneVoipObjects.setObjects(*((_C,_X),(_C,_Y),(_C,_Z),(_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_C,_g),(_C,_h),(_C,_i),(_C,_j),(_C,_k),(_C,_l),(_C,_m),(_C,_n),(_C,_o),(_C,_p),(_C,_q),(_C,_r),(_C,_s),(_C,_t),(_C,_u),(_C,_v),(_C,_w),(_C,_x),(_C,_y),(_C,_z),(_C,_A0),(_C,_A1),(_C,_A2),(_C,_A3),(_C,_A4)))
if mibBuilder.loadTexts:zhoneVoipObjects.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zhoneVoip':zhoneVoip,'zhoneVoipSystem':zhoneVoipSystem,'zhoneVoipSystemProtocol':zhoneVoipSystemProtocol,'zhoneVoipSystemSendCallProceedingTone':zhoneVoipSystemSendCallProceedingTone,'zhoneVoipSystemRtcpEnabled':zhoneVoipSystemRtcpEnabled,'zhoneVoipSystemRtcpPacketInterval':zhoneVoipSystemRtcpPacketInterval,'zhoneVoipSystemInterdigitTimeout':zhoneVoipSystemInterdigitTimeout,'zhoneVoipSystemIpTos':zhoneVoipSystemIpTos,'zhoneVoipSystemDomainName':zhoneVoipSystemDomainName,'zhoneVoipObjects':zhoneVoipObjects,'zhoneVoipSipDialPlan':zhoneVoipSipDialPlan,_X:nextVoipSipDialPlanId,'zhoneVoipSipDialPlanTable':zhoneVoipSipDialPlanTable,'zhoneVoipSipDialPlanEntry':zhoneVoipSipDialPlanEntry,_S:zhoneVoipSipDialPlanId,_Y:zhoneVoipSipDialString,_Z:zhoneVoipSipDialIpAddr,_a:zhoneVoipSipDialPlanRowStatus,_h:zhoneVoipSipDialDestName,_g:zhoneVoipSipDialNumOfDigits,_f:zhoneVoipSipDialPrefixStrip,_e:zhoneVoipSipDialPrefixAdd,_r:zhoneVoipSipDialPlanType,'zhoneVoipServerEntryIndex':zhoneVoipServerEntryIndex,'zhoneVoipOverrideInterdigitTimeout':zhoneVoipOverrideInterdigitTimeout,'zhoneVoipSipDialPlanClass':zhoneVoipSipDialPlanClass,'zhoneVoipSipDialPlanDescription':zhoneVoipSipDialPlanDescription,'zhoneVoipHuntGroup':zhoneVoipHuntGroup,_b:nextZhoneVoipHuntGroupId,'zhoneVoipHuntGroupTable':zhoneVoipHuntGroupTable,'zhoneVoipHuntGroupEntry':zhoneVoipHuntGroupEntry,_T:zhoneVoipHuntGroupId,_c:zhoneVoipHuntGroupDestUri,_j:zhoneVoipHuntGroupDefaultCodec,_i:zhoneVoipHuntGroupPortMembers,_d:zhoneVoipHuntGroupRowStatus,'zhoneVoipMaliciousCaller':zhoneVoipMaliciousCaller,_k:nextVoipMaliciousCallerId,'zhoneVoipMaliciousCallerTable':zhoneVoipMaliciousCallerTable,'zhoneVoipMaliciousCallerEntry':zhoneVoipMaliciousCallerEntry,_U:zhoneVoipMaliciousCallerId,_l:zhoneVoipMaliciousCallerUri,_A3:zhoneVoipMaliciousCallerEnable,_A2:zhoneVoipMaliciousCallerRowStatus,'zhoneVoipServerCfg':zhoneVoipServerCfg,'zhoneVoipServerTable':zhoneVoipServerTable,'zhoneVoipServerEntry':zhoneVoipServerEntry,_V:zhoneVoipServerAddressIndex,_q:zhoneVoipServerRowStatus,_p:zhoneVoipServerAddrType,_o:zhoneVoipServerAddr,_n:zhoneVoipServerUdpPortNumber,_m:zhoneVoipServerId,'zhoneVoipServerProtocol':zhoneVoipServerProtocol,'zhoneVoipServerSendCallProceedingTone':zhoneVoipServerSendCallProceedingTone,'zhoneVoipServerRtcpEnabled':zhoneVoipServerRtcpEnabled,'zhoneVoipServerRtcpPacketInterval':zhoneVoipServerRtcpPacketInterval,'zhoneVoipServerInterDigitTimeout':zhoneVoipServerInterDigitTimeout,'zhoneVoipServerIpTos':zhoneVoipServerIpTos,'zhoneVoipServerDomainName':zhoneVoipServerDomainName,_z:zhoneVoipServerExpiresInvite,_A0:zhoneVoipServerExpiresRegister,_A1:zhoneVoipServerHeaderMethod,_s:zhoneVoipServerSessionTimer,_t:zhoneVoipServerSessionExpiration,_u:zhoneVoipServerSessionMinSE,_v:zhoneVoipServerSessionCallerReqTimer,_w:zhoneVoipServerSessionCalleeReqTimer,_x:zhoneVoipServerSessionCallerSpecifyRefresher,_y:zhoneVoipServerSessionCalleeSpecifyRefresher,'zhoneVoipServerDtmfMode':zhoneVoipServerDtmfMode,_A4:zhoneVoipServerBehaviorStringOne,'zhoneVoipServerRtpTermIdSyntax':zhoneVoipServerRtpTermIdSyntax,'zhoneVoipServerRtpDSCP':zhoneVoipServerRtpDSCP,'zhoneVoipServerSignalingDSCP':zhoneVoipServerSignalingDSCP,'zhoneVoipServerDtmfPayloadId':zhoneVoipServerDtmfPayloadId,'zhoneVoipServerRegisterReadyTimeout':zhoneVoipServerRegisterReadyTimeout,'zhoneVoipServerMessageRetryCount':zhoneVoipServerMessageRetryCount,'zhoneVoipServerFeatures':zhoneVoipServerFeatures,'zhoneVoipServerTransportProtocol':zhoneVoipServerTransportProtocol,'zhoneVoipSigLocalPortNumber':zhoneVoipSigLocalPortNumber})