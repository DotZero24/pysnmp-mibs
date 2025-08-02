_f='rbnIpSecNotifyGroup'
_e='rbnIpSecNotifyObjectGroup'
_d='rbnIpSecRSATrustedCertificateNearingExpiryAlarm'
_c='rbnIpSecRSASelfCertificateNearingExpiryAlarm'
_b='rbnIpSecNoValidRSATrustedCertificateAlarm'
_a='rbnIpSecNoValidRSASelfCertificateAlarm'
_Z='rbnIpSecTunnelStatusChangeAlarm'
_Y='rbnIpSecCertificateSubjectName'
_X='rbnIpSecSelfCertificateIdentifier'
_W='rbnIpSecTunnelState'
_V='rbnIpSecRemoteAddress'
_U='rbnIpSecRemoteAddressType'
_T='rbnIpSecLocalAddress'
_S='rbnIpSecLocalAddressType'
_R='rbnIpSecLocalAddrContextName'
_Q='rbnIpSecRemoteId'
_P='rbnIpSecRemoteIdType'
_O='rbnIpSecTunnelDownCause'
_N='rbnIpSecTunnelType'
_M='rbnIpSecTunnelName'
_L='rbnIpSecTunnelIdentifier'
_K='rbnIpSecExpiryDateAndTime'
_J='rbnIpSecCertificateHandle'
_I='Integer32'
_H='rbnIpSecEventProbableCause'
_G='rbnIpSecEventType'
_F='rbnIpSecEventSeverity'
_E='rbnIpSecEventDateAndTime'
_D='SnmpAdminString'
_C='accessible-for-notify'
_B='current'
_A='RBN-IP-SECURITY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAItuEventType,IANAItuProbableCause=mibBuilder.importSymbols('IANA-ITU-ALARM-TC-MIB','IANAItuEventType','IANAItuProbableCause')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ItuPerceivedSeverity,=mibBuilder.importSymbols('ITU-ALARM-TC-MIB','ItuPerceivedSeverity')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
rbnIpSecurityMib=ModuleIdentity((1,3,6,1,4,1,2352,2,55))
if mibBuilder.loadTexts:rbnIpSecurityMib.setRevisions(('2011-01-14 00:00',))
_RbnIpSecNotifications_ObjectIdentity=ObjectIdentity
rbnIpSecNotifications=_RbnIpSecNotifications_ObjectIdentity((1,3,6,1,4,1,2352,2,55,0))
_RbnIpSecObjects_ObjectIdentity=ObjectIdentity
rbnIpSecObjects=_RbnIpSecObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,55,1))
_RbnIpSecNotify_ObjectIdentity=ObjectIdentity
rbnIpSecNotify=_RbnIpSecNotify_ObjectIdentity((1,3,6,1,4,1,2352,2,55,1,1))
_RbnIpSecEventDateAndTime_Type=DateAndTime
_RbnIpSecEventDateAndTime_Object=MibScalar
rbnIpSecEventDateAndTime=_RbnIpSecEventDateAndTime_Object((1,3,6,1,4,1,2352,2,55,1,1,1),_RbnIpSecEventDateAndTime_Type())
rbnIpSecEventDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpSecEventDateAndTime.setStatus(_B)
_RbnIpSecEventSeverity_Type=ItuPerceivedSeverity
_RbnIpSecEventSeverity_Object=MibScalar
rbnIpSecEventSeverity=_RbnIpSecEventSeverity_Object((1,3,6,1,4,1,2352,2,55,1,1,2),_RbnIpSecEventSeverity_Type())
rbnIpSecEventSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpSecEventSeverity.setStatus(_B)
_RbnIpSecEventType_Type=IANAItuEventType
_RbnIpSecEventType_Object=MibScalar
rbnIpSecEventType=_RbnIpSecEventType_Object((1,3,6,1,4,1,2352,2,55,1,1,3),_RbnIpSecEventType_Type())
rbnIpSecEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpSecEventType.setStatus(_B)
_RbnIpSecEventProbableCause_Type=IANAItuProbableCause
_RbnIpSecEventProbableCause_Object=MibScalar
rbnIpSecEventProbableCause=_RbnIpSecEventProbableCause_Object((1,3,6,1,4,1,2352,2,55,1,1,4),_RbnIpSecEventProbableCause_Type())
rbnIpSecEventProbableCause.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpSecEventProbableCause.setStatus(_B)
class _RbnIpSecTunnelIdentifier_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,270))
_RbnIpSecTunnelIdentifier_Type.__name__=_D
_RbnIpSecTunnelIdentifier_Object=MibScalar
rbnIpSecTunnelIdentifier=_RbnIpSecTunnelIdentifier_Object((1,3,6,1,4,1,2352,2,55,1,1,5),_RbnIpSecTunnelIdentifier_Type())
rbnIpSecTunnelIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpSecTunnelIdentifier.setStatus(_B)
class _RbnIpSecTunnelName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_RbnIpSecTunnelName_Type.__name__=_D
_RbnIpSecTunnelName_Object=MibScalar
rbnIpSecTunnelName=_RbnIpSecTunnelName_Object((1,3,6,1,4,1,2352,2,55,1,1,6),_RbnIpSecTunnelName_Type())
rbnIpSecTunnelName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpSecTunnelName.setStatus(_B)
class _RbnIpSecTunnelType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('static',1),('dynamic',2),('manual',3)))
_RbnIpSecTunnelType_Type.__name__=_I
_RbnIpSecTunnelType_Object=MibScalar
rbnIpSecTunnelType=_RbnIpSecTunnelType_Object((1,3,6,1,4,1,2352,2,55,1,1,7),_RbnIpSecTunnelType_Type())
rbnIpSecTunnelType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpSecTunnelType.setStatus(_B)
class _RbnIpSecTunnelDownCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('general',0),('noRoute',1),('aspHomingFailure',2),('ppaHomingFailure',3),('configuredDown',4),('keepaliveFailure',5),('downByPeer',6),('rekeyFailure',7),('aspSoftReset',8),('indeterminate',9)))
_RbnIpSecTunnelDownCause_Type.__name__=_I
_RbnIpSecTunnelDownCause_Object=MibScalar
rbnIpSecTunnelDownCause=_RbnIpSecTunnelDownCause_Object((1,3,6,1,4,1,2352,2,55,1,1,8),_RbnIpSecTunnelDownCause_Type())
rbnIpSecTunnelDownCause.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpSecTunnelDownCause.setStatus(_B)
class _RbnIpSecRemoteIdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,5,9,10,11)));namedValues=NamedValues(*(('reserved',0),('ipv4',1),('fqdn',2),('rfcAddr',3),('ipv6',5),('derAsn1Dn',9),('derAsn1Gn',10),('keyId',11)))
_RbnIpSecRemoteIdType_Type.__name__=_I
_RbnIpSecRemoteIdType_Object=MibScalar
rbnIpSecRemoteIdType=_RbnIpSecRemoteIdType_Object((1,3,6,1,4,1,2352,2,55,1,1,9),_RbnIpSecRemoteIdType_Type())
rbnIpSecRemoteIdType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpSecRemoteIdType.setStatus(_B)
class _RbnIpSecRemoteId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_RbnIpSecRemoteId_Type.__name__=_D
_RbnIpSecRemoteId_Object=MibScalar
rbnIpSecRemoteId=_RbnIpSecRemoteId_Object((1,3,6,1,4,1,2352,2,55,1,1,10),_RbnIpSecRemoteId_Type())
rbnIpSecRemoteId.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpSecRemoteId.setStatus(_B)
class _RbnIpSecLocalAddrContextName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RbnIpSecLocalAddrContextName_Type.__name__=_D
_RbnIpSecLocalAddrContextName_Object=MibScalar
rbnIpSecLocalAddrContextName=_RbnIpSecLocalAddrContextName_Object((1,3,6,1,4,1,2352,2,55,1,1,11),_RbnIpSecLocalAddrContextName_Type())
rbnIpSecLocalAddrContextName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpSecLocalAddrContextName.setStatus(_B)
_RbnIpSecLocalAddressType_Type=InetAddressType
_RbnIpSecLocalAddressType_Object=MibScalar
rbnIpSecLocalAddressType=_RbnIpSecLocalAddressType_Object((1,3,6,1,4,1,2352,2,55,1,1,12),_RbnIpSecLocalAddressType_Type())
rbnIpSecLocalAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpSecLocalAddressType.setStatus(_B)
_RbnIpSecLocalAddress_Type=InetAddress
_RbnIpSecLocalAddress_Object=MibScalar
rbnIpSecLocalAddress=_RbnIpSecLocalAddress_Object((1,3,6,1,4,1,2352,2,55,1,1,13),_RbnIpSecLocalAddress_Type())
rbnIpSecLocalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpSecLocalAddress.setStatus(_B)
_RbnIpSecRemoteAddressType_Type=InetAddressType
_RbnIpSecRemoteAddressType_Object=MibScalar
rbnIpSecRemoteAddressType=_RbnIpSecRemoteAddressType_Object((1,3,6,1,4,1,2352,2,55,1,1,14),_RbnIpSecRemoteAddressType_Type())
rbnIpSecRemoteAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpSecRemoteAddressType.setStatus(_B)
_RbnIpSecRemoteAddress_Type=InetAddress
_RbnIpSecRemoteAddress_Object=MibScalar
rbnIpSecRemoteAddress=_RbnIpSecRemoteAddress_Object((1,3,6,1,4,1,2352,2,55,1,1,15),_RbnIpSecRemoteAddress_Type())
rbnIpSecRemoteAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpSecRemoteAddress.setStatus(_B)
class _RbnIpSecTunnelState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_RbnIpSecTunnelState_Type.__name__=_I
_RbnIpSecTunnelState_Object=MibScalar
rbnIpSecTunnelState=_RbnIpSecTunnelState_Object((1,3,6,1,4,1,2352,2,55,1,1,16),_RbnIpSecTunnelState_Type())
rbnIpSecTunnelState.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpSecTunnelState.setStatus(_B)
class _RbnIpSecSelfCertificateIdentifier_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,522))
_RbnIpSecSelfCertificateIdentifier_Type.__name__=_D
_RbnIpSecSelfCertificateIdentifier_Object=MibScalar
rbnIpSecSelfCertificateIdentifier=_RbnIpSecSelfCertificateIdentifier_Object((1,3,6,1,4,1,2352,2,55,1,1,17),_RbnIpSecSelfCertificateIdentifier_Type())
rbnIpSecSelfCertificateIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpSecSelfCertificateIdentifier.setStatus(_B)
_RbnIpSecCertificateHandle_Type=Unsigned32
_RbnIpSecCertificateHandle_Object=MibScalar
rbnIpSecCertificateHandle=_RbnIpSecCertificateHandle_Object((1,3,6,1,4,1,2352,2,55,1,1,18),_RbnIpSecCertificateHandle_Type())
rbnIpSecCertificateHandle.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpSecCertificateHandle.setStatus(_B)
class _RbnIpSecExpiryDateAndTime_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_RbnIpSecExpiryDateAndTime_Type.__name__=_D
_RbnIpSecExpiryDateAndTime_Object=MibScalar
rbnIpSecExpiryDateAndTime=_RbnIpSecExpiryDateAndTime_Object((1,3,6,1,4,1,2352,2,55,1,1,19),_RbnIpSecExpiryDateAndTime_Type())
rbnIpSecExpiryDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpSecExpiryDateAndTime.setStatus(_B)
class _RbnIpSecCertificateSubjectName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_RbnIpSecCertificateSubjectName_Type.__name__=_D
_RbnIpSecCertificateSubjectName_Object=MibScalar
rbnIpSecCertificateSubjectName=_RbnIpSecCertificateSubjectName_Object((1,3,6,1,4,1,2352,2,55,1,1,20),_RbnIpSecCertificateSubjectName_Type())
rbnIpSecCertificateSubjectName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnIpSecCertificateSubjectName.setStatus(_B)
_RbnIpSecConformance_ObjectIdentity=ObjectIdentity
rbnIpSecConformance=_RbnIpSecConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,55,2))
_RbnIpSecCompliances_ObjectIdentity=ObjectIdentity
rbnIpSecCompliances=_RbnIpSecCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,55,2,1))
_RbnIpSecGroups_ObjectIdentity=ObjectIdentity
rbnIpSecGroups=_RbnIpSecGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,55,2,2))
rbnIpSecNotifyObjectGroup=ObjectGroup((1,3,6,1,4,1,2352,2,55,2,2,1))
rbnIpSecNotifyObjectGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:rbnIpSecNotifyObjectGroup.setStatus(_B)
rbnIpSecTunnelStatusChangeAlarm=NotificationType((1,3,6,1,4,1,2352,2,55,0,1))
rbnIpSecTunnelStatusChangeAlarm.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:rbnIpSecTunnelStatusChangeAlarm.setStatus(_B)
rbnIpSecNoValidRSASelfCertificateAlarm=NotificationType((1,3,6,1,4,1,2352,2,55,0,2))
rbnIpSecNoValidRSASelfCertificateAlarm.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:rbnIpSecNoValidRSASelfCertificateAlarm.setStatus(_B)
rbnIpSecNoValidRSATrustedCertificateAlarm=NotificationType((1,3,6,1,4,1,2352,2,55,0,3))
rbnIpSecNoValidRSATrustedCertificateAlarm.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:rbnIpSecNoValidRSATrustedCertificateAlarm.setStatus(_B)
rbnIpSecRSASelfCertificateNearingExpiryAlarm=NotificationType((1,3,6,1,4,1,2352,2,55,0,4))
rbnIpSecRSASelfCertificateNearingExpiryAlarm.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_X),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:rbnIpSecRSASelfCertificateNearingExpiryAlarm.setStatus(_B)
rbnIpSecRSATrustedCertificateNearingExpiryAlarm=NotificationType((1,3,6,1,4,1,2352,2,55,0,5))
rbnIpSecRSATrustedCertificateNearingExpiryAlarm.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_Y),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:rbnIpSecRSATrustedCertificateNearingExpiryAlarm.setStatus(_B)
rbnIpSecNotifyGroup=NotificationGroup((1,3,6,1,4,1,2352,2,55,2,2,2))
rbnIpSecNotifyGroup.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:rbnIpSecNotifyGroup.setStatus(_B)
rbnIpSecCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,55,2,1,1))
rbnIpSecCompliance.setObjects(*((_A,_e),(_A,_f)))
if mibBuilder.loadTexts:rbnIpSecCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'rbnIpSecurityMib':rbnIpSecurityMib,'rbnIpSecNotifications':rbnIpSecNotifications,_Z:rbnIpSecTunnelStatusChangeAlarm,_a:rbnIpSecNoValidRSASelfCertificateAlarm,_b:rbnIpSecNoValidRSATrustedCertificateAlarm,_c:rbnIpSecRSASelfCertificateNearingExpiryAlarm,_d:rbnIpSecRSATrustedCertificateNearingExpiryAlarm,'rbnIpSecObjects':rbnIpSecObjects,'rbnIpSecNotify':rbnIpSecNotify,_E:rbnIpSecEventDateAndTime,_F:rbnIpSecEventSeverity,_G:rbnIpSecEventType,_H:rbnIpSecEventProbableCause,_L:rbnIpSecTunnelIdentifier,_M:rbnIpSecTunnelName,_N:rbnIpSecTunnelType,_O:rbnIpSecTunnelDownCause,_P:rbnIpSecRemoteIdType,_Q:rbnIpSecRemoteId,_R:rbnIpSecLocalAddrContextName,_S:rbnIpSecLocalAddressType,_T:rbnIpSecLocalAddress,_U:rbnIpSecRemoteAddressType,_V:rbnIpSecRemoteAddress,_W:rbnIpSecTunnelState,_X:rbnIpSecSelfCertificateIdentifier,_J:rbnIpSecCertificateHandle,_K:rbnIpSecExpiryDateAndTime,_Y:rbnIpSecCertificateSubjectName,'rbnIpSecConformance':rbnIpSecConformance,'rbnIpSecCompliances':rbnIpSecCompliances,'rbnIpSecCompliance':rbnIpSecCompliance,'rbnIpSecGroups':rbnIpSecGroups,_e:rbnIpSecNotifyObjectGroup,_f:rbnIpSecNotifyGroup})