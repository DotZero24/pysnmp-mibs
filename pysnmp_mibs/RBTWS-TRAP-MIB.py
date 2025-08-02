_Ay='rbtwsClusterFailureDescription'
_Ax='rbtwsClusterFailureReason'
_Aw='rbtwsClientRadioType'
_Av='rbtwsRadioMimoState'
_Au='rbtwsRadioChannelWidth'
_At='rbtwsMobilityDomainResiliencyStatus'
_As='rbtwsClientClearedReason'
_Ar='rbtwsClientSessionElapsedSeconds'
_Aq='rbtwsApMgrChangeReason'
_Ap='rbtwsApMgrNewIp'
_Ao='rbtwsApMgrOldIp'
_An='rbtwsMichaelMICFailureCause'
_Am='rbtwsConfigSaveGeneration'
_Al='rbtwsConfigSaveInitiatorDetails'
_Ak='rbtwsConfigSaveInitiatorIp'
_Aj='rbtwsConfigSaveInitiatorType'
_Ai='rbtwsConfigSaveFileName'
_Ah='rbtwsMobilityDomainPrimarySeedIp'
_Ag='rbtwsMobilityDomainSecondarySeedIp'
_Af='rbtwsClientDisconnectDescription'
_Ae='rbtwsClientDisconnectSource'
_Ad='rbtwsChangedUserParamNewValues'
_Ac='rbtwsChangedUserParamOldValues'
_Ab='rbtwsNumLicensedActiveAPs'
_Aa='rbtwsBlacklistingCause'
_AZ='rbtwsBlacklistingRemainingTime'
_AY='rbtwsClientIpAddrChangeReason'
_AX='rbtwsDAPconnectWarningType'
_AW='rbtwsRsaPubKeyFingerPrint'
_AV='rbtwsDeviceModel'
_AU='rbtwsClientSessionElapsedTime'
_AT='rbtwsClientDot1xFailureCause'
_AS='rbtwsClientDot1xState'
_AR='rbtwsChannelChangeReason'
_AQ='rbtwsOldChannelNum'
_AP='rbtwsNewChannelNum'
_AO='rbtwsRadioPowerChangeDescription'
_AN='rbtwsRadioPowerChangeReason'
_AM='rbtwsOldPowerLevel'
_AL='rbtwsNewPowerLevel'
_AK='rbtwsClientTimeSinceLastRoam'
_AJ='rbtwsClientRoamedFromWsIp'
_AI='rbtwsClientRoamedFromDAPNum'
_AH='rbtwsClientRoamedFromRadioNum'
_AG='rbtwsClientRoamedFromPortNum'
_AF='rbtwsClientRoamedFromAccessType'
_AE='rbtwsRadioRssi'
_AD='rbtwsClientAssociationFailureCause'
_AC='rbtwsClientLocationPolicyIndex'
_AB='rbtwsClientAuthenticationFailureCause'
_AA='user-glob-mismatch'
_A9='quiet-period'
_A8='Unsigned32'
_A7='rbtwsRFDetectXmtrCryptoType'
_A6='rbtwsRFDetectXmtrRadioType'
_A5='rbtwsClientAuthorizationReason'
_A4='rbtwsRadioMode'
_A3='rbtwsClientDynAuthorClientIp'
_A2='rbtwsRFDetectRogueAPMacAddr'
_A1='rbtwsApWasOperational'
_A0='rbtwsApFailDetail'
_z='rbtwsApTransition'
_y='rbtwsApPortOrDapNum'
_x='rbtwsApAttachType'
_w='rbtwsClientMACAddress2'
_v='rbtwsRFDetectDoSType'
_u='rbtwsClientSessionStartTime'
_t='rbtwsClientAuthorizationFailureCause'
_s='rbtwsUserParams'
_r='rbtwsMobilityDomainIp'
_q='rbtwsAPAccessType'
_p='rbtwsDeviceId'
_o='OctetString'
_n='rbtwsPhysPortNum'
_m='rbtwsClientAccessMode'
_l='rbtwsApServiceAvailability'
_k='rbtwsApConnectSecurityType'
_j='rbtwsRadioConfigState'
_i='rbtwsRadioType'
_h='rbtwsClientVLANtag'
_g='rbtwsClientVLANid'
_f='rbtwsSourceWsIp'
_e='rbtwsRFDetectClassificationReason'
_d='rbtwsUserAccessType'
_c='rbtwsClientFailureCauseDescription'
_b='rbtwsAPMACAddress'
_a='rbtwsApName'
_Z='rbtwsClientSessionState'
_Y='rbtwsDeviceSerNum'
_X='rbtwsClientVLANName'
_W='rbtwsApNum'
_V='rbtwsLocalId'
_U='rbtwsClientAuthServerIp'
_T='rbtwsRadioMACAddress'
_S='other'
_R='rbtwsClientIp'
_Q='rbtwsClientAuthenProtocolType'
_P='Integer32'
_O='DisplayString'
_N='rbtwsClientSessionId'
_M='rbtwsUserName'
_L='rbtwsRFDetectListenerListInfo'
_K='rbtwsClientAccessType'
_J='rbtwsRadioSSID'
_I='rbtwsDAPNum'
_H='rbtwsClientMACAddress'
_G='rbtwsRFDetectXmtrMacAddr'
_F='rbtwsAPRadioNum'
_E='rbtwsPortNum'
_D='obsolete'
_C='accessible-for-notify'
_B='current'
_A='RBTWS-TRAP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_o,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
RbtwsAccessType,RbtwsApAttachType,RbtwsApConnectSecurityType,RbtwsApFailDetail,RbtwsApFingerprint,RbtwsApNum,RbtwsApPortOrDapNum,RbtwsApSerialNum,RbtwsApServiceAvailability,RbtwsApTransition,RbtwsApWasOperational,RbtwsChannelChangeType,RbtwsCryptoType,RbtwsPowerLevel,RbtwsRadioChannelWidth,RbtwsRadioConfigState,RbtwsRadioMimoState,RbtwsRadioMode,RbtwsRadioNum,RbtwsRadioPowerChangeType,RbtwsRadioType=mibBuilder.importSymbols('RBTWS-AP-TC','RbtwsAccessType','RbtwsApAttachType','RbtwsApConnectSecurityType','RbtwsApFailDetail','RbtwsApFingerprint','RbtwsApNum','RbtwsApPortOrDapNum','RbtwsApSerialNum','RbtwsApServiceAvailability','RbtwsApTransition','RbtwsApWasOperational','RbtwsChannelChangeType','RbtwsCryptoType','RbtwsPowerLevel','RbtwsRadioChannelWidth','RbtwsRadioConfigState','RbtwsRadioMimoState','RbtwsRadioMode','RbtwsRadioNum','RbtwsRadioPowerChangeType','RbtwsRadioType')
RbtwsClientAccessMode,RbtwsClientAuthenProtocolType,RbtwsClientDot1xState,RbtwsClientSessionState,RbtwsUserAccessType=mibBuilder.importSymbols('RBTWS-CLIENT-SESSION-TC','RbtwsClientAccessMode','RbtwsClientAuthenProtocolType','RbtwsClientDot1xState','RbtwsClientSessionState','RbtwsUserAccessType')
RbtwsRFDetectClassificationReason,=mibBuilder.importSymbols('RBTWS-RF-DETECT-TC','RbtwsRFDetectClassificationReason')
rbtwsMibs,rbtwsTemporary,rbtwsTraps=mibBuilder.importSymbols('RBTWS-ROOT-MIB','rbtwsMibs','rbtwsTemporary','rbtwsTraps')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_P,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_A8,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_O,'MacAddress','PhysAddress','TextualConvention')
rbtwsTrapMib=ModuleIdentity((1,3,6,1,4,1,52,4,15,1,4,1))
if mibBuilder.loadTexts:rbtwsTrapMib.setRevisions(('2008-05-15 02:15','2008-05-07 02:12','2008-04-22 02:02','2008-04-10 02:01','2008-04-08 01:58','2008-02-18 01:57','2007-12-03 01:53','2007-11-15 01:52','2007-11-01 01:45','2007-10-01 01:41','2007-08-31 01:40','2007-08-24 01:22','2007-07-06 01:10','2007-06-05 01:07','2007-05-17 01:06','2007-05-04 01:03','2007-04-19 01:00','2007-03-27 00:54','2007-02-15 00:53','2007-01-09 00:52','2007-01-09 00:51','2007-01-09 00:50','2006-09-28 00:45','2006-08-08 00:42','2006-07-31 00:40','2006-07-28 00:32','2006-07-23 00:29','2006-07-12 00:28','2006-07-07 00:26','2006-07-07 00:25','2006-07-06 00:23','2006-04-19 00:22','2006-04-19 00:21','2005-01-01 00:00'))
class RbtwsAssociationFailureType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_S,1),('load-balance',2),(_A9,3),('dot1x',4),('no-prev-assoc',5),('glare',6),('cipher-rejected',7),('cipher-mismatch',8),('wep-not-configured',9),('bad-assoc-request',10),('out-of-memory',11),('tkip-cm-active',12),('roam-in-progress',13)))
class RbtwsAuthenticationFailureType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_S,1),(_AA,2),('user-does-not-exist',3),('invalid-password',4),('server-timeout',5),('signature-failed',6),('local-certificate-error',7),('all-servers-down',8),('authentication-type-mismatch',9),('server-rejected',10),('fallthru-auth-misconfig',11),('no-lastresort-auth',12),('exceeded-max-attempts',13),('password-expired',14)))
class RbtwsAuthorizationFailureType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_S,1),('user-param',2),('location-policy',3),('vlan-tunnel-failure',4),('ssid-mismatch',5),('acl-mismatch',6),('timeofday-mismatch',7),('crypto-type-mismatch',8),('mobility-profile-mismatch',9),('start-date-mismatch',10),('end-date-mismatch',11),('svr-type-mismatch',12),('ssid-defaults',13),('qos-profile-mismatch',14),('simultaneous-logins',15)))
class RbtwsDot1xFailureType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_S,1),(_A9,2),('administrative-kill',3),('bad-rsnie',4),('timeout',5),('max-sessions-exceeded',6),('fourway-hs-failure',7),(_AA,8),('bonded-auth-failure',9),('reauth-disabled',10),('gkhs-failure',11),('force-unauth-configured',12),('cert-not-installed',13)))
class RbtwsRFDetectDoSType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*(('probe-flood',1),('auth-flood',2),('null-data-flood',3),('mgmt-6-flood',4),('mgmt-7-flood',5),('mgmt-d-flood',6),('mgmt-e-flood',7),('mgmt-f-flood',8),('fakeap-ssid',9),('fakeap-bssid',10),('bcast-deauth',11),('null-probe-resp',12),('disassoc-spoof',13),('deauth-spoof',14),('decrypt-err',15),('weak-wep-iv',16),('wireless-bridge',17),('netstumbler',18),('wellenreiter',19),('adhoc-client-frame',20),('associate-pkt-flood',21),('re-associate-pkt-flood',22),('de-associate-pkt-flood',23),('bssid-spoof',24)))
class RbtwsClientIpAddrChangeReason(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('client-connected',1),(_S,2),('dhcp-to-static',3)))
class RbtwsBlacklistingCause(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('bl-configured',1),('bl-associate-pkt-flood',2),('bl-re-associate-pkt-flood',3),('bl-de-associate-pkt-flood',4)))
class RbtwsUserAttributeList(DisplayString):status=_B;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2048))
class RbtwsSessionDisconnectType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('admin-disconnect',2),('dyn-auth-disconnect',3)))
class RbtwsConfigSaveInitiatorType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_S,1),('cli-console',2),('cli-remote',3),('https',4),('snmp-set',5)))
class RbtwsMichaelMICFailureCause(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('detected-by-ap',1),('detected-by-client',2)))
class RbtwsClientAuthorizationReason(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),('new-client',2),('re-auth',3),('roam',4)))
class RbtwsApMgrChangeReason(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('failover',2),('load-balancing',3)))
class RbtwsClientClearedReason(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('normal',2),('backup-failure',3)))
class RbtwsMobilityDomainResiliencyStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('resilient',2),('degraded',3)))
class RbtwsClusterFailureReason(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),('validation-error',2)))
_RbtwsDeviceId_Type=ObjectIdentifier
_RbtwsDeviceId_Object=MibScalar
rbtwsDeviceId=_RbtwsDeviceId_Object((1,3,6,1,4,1,52,4,15,1,2,1),_RbtwsDeviceId_Type())
rbtwsDeviceId.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsDeviceId.setStatus(_B)
_RbtwsMobilityDomainIp_Type=IpAddress
_RbtwsMobilityDomainIp_Object=MibScalar
rbtwsMobilityDomainIp=_RbtwsMobilityDomainIp_Object((1,3,6,1,4,1,52,4,15,1,2,2),_RbtwsMobilityDomainIp_Type())
rbtwsMobilityDomainIp.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsMobilityDomainIp.setStatus(_B)
_RbtwsAPMACAddress_Type=MacAddress
_RbtwsAPMACAddress_Object=MibScalar
rbtwsAPMACAddress=_RbtwsAPMACAddress_Object((1,3,6,1,4,1,52,4,15,1,2,3),_RbtwsAPMACAddress_Type())
rbtwsAPMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsAPMACAddress.setStatus(_B)
_RbtwsClientMACAddress_Type=MacAddress
_RbtwsClientMACAddress_Object=MibScalar
rbtwsClientMACAddress=_RbtwsClientMACAddress_Object((1,3,6,1,4,1,52,4,15,1,2,4),_RbtwsClientMACAddress_Type())
rbtwsClientMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientMACAddress.setStatus(_B)
_RbtwsRFDetectXmtrMacAddr_Type=MacAddress
_RbtwsRFDetectXmtrMacAddr_Object=MibScalar
rbtwsRFDetectXmtrMacAddr=_RbtwsRFDetectXmtrMacAddr_Object((1,3,6,1,4,1,52,4,15,1,2,5),_RbtwsRFDetectXmtrMacAddr_Type())
rbtwsRFDetectXmtrMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsRFDetectXmtrMacAddr.setStatus(_B)
class _RbtwsPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,22))
_RbtwsPortNum_Type.__name__=_P
_RbtwsPortNum_Object=MibScalar
rbtwsPortNum=_RbtwsPortNum_Object((1,3,6,1,4,1,52,4,15,1,2,6),_RbtwsPortNum_Type())
rbtwsPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsPortNum.setStatus(_B)
_RbtwsAPRadioNum_Type=RbtwsRadioNum
_RbtwsAPRadioNum_Object=MibScalar
rbtwsAPRadioNum=_RbtwsAPRadioNum_Object((1,3,6,1,4,1,52,4,15,1,2,7),_RbtwsAPRadioNum_Type())
rbtwsAPRadioNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsAPRadioNum.setStatus(_B)
class _RbtwsRadioRssi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_RbtwsRadioRssi_Type.__name__=_P
_RbtwsRadioRssi_Object=MibScalar
rbtwsRadioRssi=_RbtwsRadioRssi_Object((1,3,6,1,4,1,52,4,15,1,2,8),_RbtwsRadioRssi_Type())
rbtwsRadioRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsRadioRssi.setStatus(_D)
class _RbtwsRadioBSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_RbtwsRadioBSSID_Type.__name__=_o
_RbtwsRadioBSSID_Object=MibScalar
rbtwsRadioBSSID=_RbtwsRadioBSSID_Object((1,3,6,1,4,1,52,4,15,1,2,9),_RbtwsRadioBSSID_Type())
rbtwsRadioBSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsRadioBSSID.setStatus(_B)
class _RbtwsUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RbtwsUserName_Type.__name__=_O
_RbtwsUserName_Object=MibScalar
rbtwsUserName=_RbtwsUserName_Object((1,3,6,1,4,1,52,4,15,1,2,10),_RbtwsUserName_Type())
rbtwsUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsUserName.setStatus(_B)
_RbtwsClientAuthServerIp_Type=IpAddress
_RbtwsClientAuthServerIp_Object=MibScalar
rbtwsClientAuthServerIp=_RbtwsClientAuthServerIp_Object((1,3,6,1,4,1,52,4,15,1,2,11),_RbtwsClientAuthServerIp_Type())
rbtwsClientAuthServerIp.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientAuthServerIp.setStatus(_B)
_RbtwsClientSessionState_Type=RbtwsClientSessionState
_RbtwsClientSessionState_Object=MibScalar
rbtwsClientSessionState=_RbtwsClientSessionState_Object((1,3,6,1,4,1,52,4,15,1,2,12),_RbtwsClientSessionState_Type())
rbtwsClientSessionState.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientSessionState.setStatus(_B)
class _RbtwsDAPNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RbtwsDAPNum_Type.__name__=_P
_RbtwsDAPNum_Object=MibScalar
rbtwsDAPNum=_RbtwsDAPNum_Object((1,3,6,1,4,1,52,4,15,1,2,13),_RbtwsDAPNum_Type())
rbtwsDAPNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsDAPNum.setStatus(_B)
_RbtwsClientIp_Type=IpAddress
_RbtwsClientIp_Object=MibScalar
rbtwsClientIp=_RbtwsClientIp_Object((1,3,6,1,4,1,52,4,15,1,2,14),_RbtwsClientIp_Type())
rbtwsClientIp.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientIp.setStatus(_B)
class _RbtwsClientSessionId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RbtwsClientSessionId_Type.__name__=_O
_RbtwsClientSessionId_Object=MibScalar
rbtwsClientSessionId=_RbtwsClientSessionId_Object((1,3,6,1,4,1,52,4,15,1,2,15),_RbtwsClientSessionId_Type())
rbtwsClientSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientSessionId.setStatus(_B)
_RbtwsClientAuthenProtocolType_Type=RbtwsClientAuthenProtocolType
_RbtwsClientAuthenProtocolType_Object=MibScalar
rbtwsClientAuthenProtocolType=_RbtwsClientAuthenProtocolType_Object((1,3,6,1,4,1,52,4,15,1,2,16),_RbtwsClientAuthenProtocolType_Type())
rbtwsClientAuthenProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientAuthenProtocolType.setStatus(_B)
class _RbtwsClientVLANName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RbtwsClientVLANName_Type.__name__=_O
_RbtwsClientVLANName_Object=MibScalar
rbtwsClientVLANName=_RbtwsClientVLANName_Object((1,3,6,1,4,1,52,4,15,1,2,17),_RbtwsClientVLANName_Type())
rbtwsClientVLANName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientVLANName.setStatus(_B)
_RbtwsClientSessionStartTime_Type=TimeTicks
_RbtwsClientSessionStartTime_Object=MibScalar
rbtwsClientSessionStartTime=_RbtwsClientSessionStartTime_Object((1,3,6,1,4,1,52,4,15,1,2,18),_RbtwsClientSessionStartTime_Type())
rbtwsClientSessionStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientSessionStartTime.setStatus(_D)
class _RbtwsClientFailureCause_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RbtwsClientFailureCause_Type.__name__=_O
_RbtwsClientFailureCause_Object=MibScalar
rbtwsClientFailureCause=_RbtwsClientFailureCause_Object((1,3,6,1,4,1,52,4,15,1,2,19),_RbtwsClientFailureCause_Type())
rbtwsClientFailureCause.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientFailureCause.setStatus(_B)
class _RbtwsClientRoamedFromPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_RbtwsClientRoamedFromPortNum_Type.__name__=_P
_RbtwsClientRoamedFromPortNum_Object=MibScalar
rbtwsClientRoamedFromPortNum=_RbtwsClientRoamedFromPortNum_Object((1,3,6,1,4,1,52,4,15,1,2,20),_RbtwsClientRoamedFromPortNum_Type())
rbtwsClientRoamedFromPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientRoamedFromPortNum.setStatus(_B)
_RbtwsClientRoamedFromRadioNum_Type=RbtwsRadioNum
_RbtwsClientRoamedFromRadioNum_Object=MibScalar
rbtwsClientRoamedFromRadioNum=_RbtwsClientRoamedFromRadioNum_Object((1,3,6,1,4,1,52,4,15,1,2,21),_RbtwsClientRoamedFromRadioNum_Type())
rbtwsClientRoamedFromRadioNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientRoamedFromRadioNum.setStatus(_B)
class _RbtwsClientRoamedFromDAPNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_RbtwsClientRoamedFromDAPNum_Type.__name__=_P
_RbtwsClientRoamedFromDAPNum_Object=MibScalar
rbtwsClientRoamedFromDAPNum=_RbtwsClientRoamedFromDAPNum_Object((1,3,6,1,4,1,52,4,15,1,2,22),_RbtwsClientRoamedFromDAPNum_Type())
rbtwsClientRoamedFromDAPNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientRoamedFromDAPNum.setStatus(_B)
class _RbtwsUserParams_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RbtwsUserParams_Type.__name__=_O
_RbtwsUserParams_Object=MibScalar
rbtwsUserParams=_RbtwsUserParams_Object((1,3,6,1,4,1,52,4,15,1,2,23),_RbtwsUserParams_Type())
rbtwsUserParams.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsUserParams.setStatus(_B)
class _RbtwsClientLocationPolicyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_RbtwsClientLocationPolicyIndex_Type.__name__=_P
_RbtwsClientLocationPolicyIndex_Object=MibScalar
rbtwsClientLocationPolicyIndex=_RbtwsClientLocationPolicyIndex_Object((1,3,6,1,4,1,52,4,15,1,2,24),_RbtwsClientLocationPolicyIndex_Type())
rbtwsClientLocationPolicyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientLocationPolicyIndex.setStatus(_B)
_RbtwsClientAssociationFailureCause_Type=RbtwsAssociationFailureType
_RbtwsClientAssociationFailureCause_Object=MibScalar
rbtwsClientAssociationFailureCause=_RbtwsClientAssociationFailureCause_Object((1,3,6,1,4,1,52,4,15,1,2,25),_RbtwsClientAssociationFailureCause_Type())
rbtwsClientAssociationFailureCause.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientAssociationFailureCause.setStatus(_B)
_RbtwsClientAuthenticationFailureCause_Type=RbtwsAuthenticationFailureType
_RbtwsClientAuthenticationFailureCause_Object=MibScalar
rbtwsClientAuthenticationFailureCause=_RbtwsClientAuthenticationFailureCause_Object((1,3,6,1,4,1,52,4,15,1,2,26),_RbtwsClientAuthenticationFailureCause_Type())
rbtwsClientAuthenticationFailureCause.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientAuthenticationFailureCause.setStatus(_B)
_RbtwsClientAuthorizationFailureCause_Type=RbtwsAuthorizationFailureType
_RbtwsClientAuthorizationFailureCause_Object=MibScalar
rbtwsClientAuthorizationFailureCause=_RbtwsClientAuthorizationFailureCause_Object((1,3,6,1,4,1,52,4,15,1,2,27),_RbtwsClientAuthorizationFailureCause_Type())
rbtwsClientAuthorizationFailureCause.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientAuthorizationFailureCause.setStatus(_B)
class _RbtwsClientFailureCauseDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RbtwsClientFailureCauseDescription_Type.__name__=_O
_RbtwsClientFailureCauseDescription_Object=MibScalar
rbtwsClientFailureCauseDescription=_RbtwsClientFailureCauseDescription_Object((1,3,6,1,4,1,52,4,15,1,2,28),_RbtwsClientFailureCauseDescription_Type())
rbtwsClientFailureCauseDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientFailureCauseDescription.setStatus(_B)
_RbtwsClientRoamedFromWsIp_Type=IpAddress
_RbtwsClientRoamedFromWsIp_Object=MibScalar
rbtwsClientRoamedFromWsIp=_RbtwsClientRoamedFromWsIp_Object((1,3,6,1,4,1,52,4,15,1,2,29),_RbtwsClientRoamedFromWsIp_Type())
rbtwsClientRoamedFromWsIp.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientRoamedFromWsIp.setStatus(_B)
_RbtwsClientRoamedFromAccessType_Type=RbtwsAccessType
_RbtwsClientRoamedFromAccessType_Object=MibScalar
rbtwsClientRoamedFromAccessType=_RbtwsClientRoamedFromAccessType_Object((1,3,6,1,4,1,52,4,15,1,2,30),_RbtwsClientRoamedFromAccessType_Type())
rbtwsClientRoamedFromAccessType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientRoamedFromAccessType.setStatus(_B)
_RbtwsClientAccessType_Type=RbtwsAccessType
_RbtwsClientAccessType_Object=MibScalar
rbtwsClientAccessType=_RbtwsClientAccessType_Object((1,3,6,1,4,1,52,4,15,1,2,31),_RbtwsClientAccessType_Type())
rbtwsClientAccessType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientAccessType.setStatus(_B)
_RbtwsRadioMACAddress_Type=MacAddress
_RbtwsRadioMACAddress_Object=MibScalar
rbtwsRadioMACAddress=_RbtwsRadioMACAddress_Object((1,3,6,1,4,1,52,4,15,1,2,32),_RbtwsRadioMACAddress_Type())
rbtwsRadioMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsRadioMACAddress.setStatus(_B)
_RbtwsRadioPowerChangeReason_Type=RbtwsRadioPowerChangeType
_RbtwsRadioPowerChangeReason_Object=MibScalar
rbtwsRadioPowerChangeReason=_RbtwsRadioPowerChangeReason_Object((1,3,6,1,4,1,52,4,15,1,2,33),_RbtwsRadioPowerChangeReason_Type())
rbtwsRadioPowerChangeReason.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsRadioPowerChangeReason.setStatus(_B)
class _RbtwsNewChannelNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_RbtwsNewChannelNum_Type.__name__=_P
_RbtwsNewChannelNum_Object=MibScalar
rbtwsNewChannelNum=_RbtwsNewChannelNum_Object((1,3,6,1,4,1,52,4,15,1,2,34),_RbtwsNewChannelNum_Type())
rbtwsNewChannelNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsNewChannelNum.setStatus(_B)
class _RbtwsOldChannelNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_RbtwsOldChannelNum_Type.__name__=_P
_RbtwsOldChannelNum_Object=MibScalar
rbtwsOldChannelNum=_RbtwsOldChannelNum_Object((1,3,6,1,4,1,52,4,15,1,2,35),_RbtwsOldChannelNum_Type())
rbtwsOldChannelNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsOldChannelNum.setStatus(_B)
_RbtwsChannelChangeReason_Type=RbtwsChannelChangeType
_RbtwsChannelChangeReason_Object=MibScalar
rbtwsChannelChangeReason=_RbtwsChannelChangeReason_Object((1,3,6,1,4,1,52,4,15,1,2,36),_RbtwsChannelChangeReason_Type())
rbtwsChannelChangeReason.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsChannelChangeReason.setStatus(_B)
class _RbtwsRFDetectListenerListInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,571))
_RbtwsRFDetectListenerListInfo_Type.__name__=_o
_RbtwsRFDetectListenerListInfo_Object=MibScalar
rbtwsRFDetectListenerListInfo=_RbtwsRFDetectListenerListInfo_Object((1,3,6,1,4,1,52,4,15,1,2,37),_RbtwsRFDetectListenerListInfo_Type())
rbtwsRFDetectListenerListInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsRFDetectListenerListInfo.setStatus(_B)
class _RbtwsRadioSSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RbtwsRadioSSID_Type.__name__=_O
_RbtwsRadioSSID_Object=MibScalar
rbtwsRadioSSID=_RbtwsRadioSSID_Object((1,3,6,1,4,1,52,4,15,1,2,38),_RbtwsRadioSSID_Type())
rbtwsRadioSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsRadioSSID.setStatus(_B)
_RbtwsNewPowerLevel_Type=RbtwsPowerLevel
_RbtwsNewPowerLevel_Object=MibScalar
rbtwsNewPowerLevel=_RbtwsNewPowerLevel_Object((1,3,6,1,4,1,52,4,15,1,2,39),_RbtwsNewPowerLevel_Type())
rbtwsNewPowerLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsNewPowerLevel.setStatus(_B)
_RbtwsOldPowerLevel_Type=RbtwsPowerLevel
_RbtwsOldPowerLevel_Object=MibScalar
rbtwsOldPowerLevel=_RbtwsOldPowerLevel_Object((1,3,6,1,4,1,52,4,15,1,2,40),_RbtwsOldPowerLevel_Type())
rbtwsOldPowerLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsOldPowerLevel.setStatus(_B)
class _RbtwsRadioPowerChangeDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RbtwsRadioPowerChangeDescription_Type.__name__=_O
_RbtwsRadioPowerChangeDescription_Object=MibScalar
rbtwsRadioPowerChangeDescription=_RbtwsRadioPowerChangeDescription_Object((1,3,6,1,4,1,52,4,15,1,2,41),_RbtwsRadioPowerChangeDescription_Type())
rbtwsRadioPowerChangeDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsRadioPowerChangeDescription.setStatus(_B)
class _RbtwsCounterMeasurePerformerListInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RbtwsCounterMeasurePerformerListInfo_Type.__name__=_O
_RbtwsCounterMeasurePerformerListInfo_Object=MibScalar
rbtwsCounterMeasurePerformerListInfo=_RbtwsCounterMeasurePerformerListInfo_Object((1,3,6,1,4,1,52,4,15,1,2,42),_RbtwsCounterMeasurePerformerListInfo_Type())
rbtwsCounterMeasurePerformerListInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsCounterMeasurePerformerListInfo.setStatus(_D)
_RbtwsClientDot1xState_Type=RbtwsClientDot1xState
_RbtwsClientDot1xState_Object=MibScalar
rbtwsClientDot1xState=_RbtwsClientDot1xState_Object((1,3,6,1,4,1,52,4,15,1,2,43),_RbtwsClientDot1xState_Type())
rbtwsClientDot1xState.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientDot1xState.setStatus(_B)
_RbtwsClientDot1xFailureCause_Type=RbtwsDot1xFailureType
_RbtwsClientDot1xFailureCause_Object=MibScalar
rbtwsClientDot1xFailureCause=_RbtwsClientDot1xFailureCause_Object((1,3,6,1,4,1,52,4,15,1,2,44),_RbtwsClientDot1xFailureCause_Type())
rbtwsClientDot1xFailureCause.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientDot1xFailureCause.setStatus(_B)
_RbtwsAPAccessType_Type=RbtwsAccessType
_RbtwsAPAccessType_Object=MibScalar
rbtwsAPAccessType=_RbtwsAPAccessType_Object((1,3,6,1,4,1,52,4,15,1,2,45),_RbtwsAPAccessType_Type())
rbtwsAPAccessType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsAPAccessType.setStatus(_D)
_RbtwsUserAccessType_Type=RbtwsUserAccessType
_RbtwsUserAccessType_Object=MibScalar
rbtwsUserAccessType=_RbtwsUserAccessType_Object((1,3,6,1,4,1,52,4,15,1,2,46),_RbtwsUserAccessType_Type())
rbtwsUserAccessType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsUserAccessType.setStatus(_B)
_RbtwsClientSessionElapsedTime_Type=TimeTicks
_RbtwsClientSessionElapsedTime_Object=MibScalar
rbtwsClientSessionElapsedTime=_RbtwsClientSessionElapsedTime_Object((1,3,6,1,4,1,52,4,15,1,2,47),_RbtwsClientSessionElapsedTime_Type())
rbtwsClientSessionElapsedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientSessionElapsedTime.setStatus(_D)
class _RbtwsLocalId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65000))
_RbtwsLocalId_Type.__name__=_P
_RbtwsLocalId_Object=MibScalar
rbtwsLocalId=_RbtwsLocalId_Object((1,3,6,1,4,1,52,4,15,1,2,48),_RbtwsLocalId_Type())
rbtwsLocalId.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsLocalId.setStatus(_B)
_RbtwsRFDetectDoSType_Type=RbtwsRFDetectDoSType
_RbtwsRFDetectDoSType_Object=MibScalar
rbtwsRFDetectDoSType=_RbtwsRFDetectDoSType_Object((1,3,6,1,4,1,52,4,15,1,2,49),_RbtwsRFDetectDoSType_Type())
rbtwsRFDetectDoSType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsRFDetectDoSType.setStatus(_B)
_RbtwsSourceWsIp_Type=IpAddress
_RbtwsSourceWsIp_Object=MibScalar
rbtwsSourceWsIp=_RbtwsSourceWsIp_Object((1,3,6,1,4,1,52,4,15,1,2,50),_RbtwsSourceWsIp_Type())
rbtwsSourceWsIp.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsSourceWsIp.setStatus(_B)
class _RbtwsClientVLANid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_RbtwsClientVLANid_Type.__name__=_P
_RbtwsClientVLANid_Object=MibScalar
rbtwsClientVLANid=_RbtwsClientVLANid_Object((1,3,6,1,4,1,52,4,15,1,2,51),_RbtwsClientVLANid_Type())
rbtwsClientVLANid.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientVLANid.setStatus(_B)
class _RbtwsClientVLANtag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_RbtwsClientVLANtag_Type.__name__=_P
_RbtwsClientVLANtag_Object=MibScalar
rbtwsClientVLANtag=_RbtwsClientVLANtag_Object((1,3,6,1,4,1,52,4,15,1,2,52),_RbtwsClientVLANtag_Type())
rbtwsClientVLANtag.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientVLANtag.setStatus(_B)
_RbtwsDeviceModel_Type=DisplayString
_RbtwsDeviceModel_Object=MibScalar
rbtwsDeviceModel=_RbtwsDeviceModel_Object((1,3,6,1,4,1,52,4,15,1,2,53),_RbtwsDeviceModel_Type())
rbtwsDeviceModel.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsDeviceModel.setStatus(_B)
_RbtwsDeviceSerNum_Type=RbtwsApSerialNum
_RbtwsDeviceSerNum_Object=MibScalar
rbtwsDeviceSerNum=_RbtwsDeviceSerNum_Object((1,3,6,1,4,1,52,4,15,1,2,54),_RbtwsDeviceSerNum_Type())
rbtwsDeviceSerNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsDeviceSerNum.setStatus(_B)
_RbtwsRsaPubKeyFingerPrint_Type=RbtwsApFingerprint
_RbtwsRsaPubKeyFingerPrint_Object=MibScalar
rbtwsRsaPubKeyFingerPrint=_RbtwsRsaPubKeyFingerPrint_Object((1,3,6,1,4,1,52,4,15,1,2,55),_RbtwsRsaPubKeyFingerPrint_Type())
rbtwsRsaPubKeyFingerPrint.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsRsaPubKeyFingerPrint.setStatus(_B)
class _RbtwsDAPconnectWarningType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('not-configured-fingerprint-connect',1),('secure-handshake-failure',2),('not-configured-fingerprint-required',3),('fingerprint-mismatch',4)))
_RbtwsDAPconnectWarningType_Type.__name__=_P
_RbtwsDAPconnectWarningType_Object=MibScalar
rbtwsDAPconnectWarningType=_RbtwsDAPconnectWarningType_Object((1,3,6,1,4,1,52,4,15,1,2,56),_RbtwsDAPconnectWarningType_Type())
rbtwsDAPconnectWarningType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsDAPconnectWarningType.setStatus(_B)
_RbtwsClientMACAddress2_Type=MacAddress
_RbtwsClientMACAddress2_Object=MibScalar
rbtwsClientMACAddress2=_RbtwsClientMACAddress2_Object((1,3,6,1,4,1,52,4,15,1,2,57),_RbtwsClientMACAddress2_Type())
rbtwsClientMACAddress2.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientMACAddress2.setStatus(_B)
_RbtwsApAttachType_Type=RbtwsApAttachType
_RbtwsApAttachType_Object=MibScalar
rbtwsApAttachType=_RbtwsApAttachType_Object((1,3,6,1,4,1,52,4,15,1,2,58),_RbtwsApAttachType_Type())
rbtwsApAttachType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsApAttachType.setStatus(_B)
_RbtwsApPortOrDapNum_Type=RbtwsApPortOrDapNum
_RbtwsApPortOrDapNum_Object=MibScalar
rbtwsApPortOrDapNum=_RbtwsApPortOrDapNum_Object((1,3,6,1,4,1,52,4,15,1,2,59),_RbtwsApPortOrDapNum_Type())
rbtwsApPortOrDapNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsApPortOrDapNum.setStatus(_D)
_RbtwsApName_Type=DisplayString
_RbtwsApName_Object=MibScalar
rbtwsApName=_RbtwsApName_Object((1,3,6,1,4,1,52,4,15,1,2,60),_RbtwsApName_Type())
rbtwsApName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsApName.setStatus(_B)
_RbtwsApTransition_Type=RbtwsApTransition
_RbtwsApTransition_Object=MibScalar
rbtwsApTransition=_RbtwsApTransition_Object((1,3,6,1,4,1,52,4,15,1,2,61),_RbtwsApTransition_Type())
rbtwsApTransition.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsApTransition.setStatus(_B)
_RbtwsApFailDetail_Type=RbtwsApFailDetail
_RbtwsApFailDetail_Object=MibScalar
rbtwsApFailDetail=_RbtwsApFailDetail_Object((1,3,6,1,4,1,52,4,15,1,2,62),_RbtwsApFailDetail_Type())
rbtwsApFailDetail.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsApFailDetail.setStatus(_B)
_RbtwsRadioType_Type=RbtwsRadioType
_RbtwsRadioType_Object=MibScalar
rbtwsRadioType=_RbtwsRadioType_Object((1,3,6,1,4,1,52,4,15,1,2,63),_RbtwsRadioType_Type())
rbtwsRadioType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsRadioType.setStatus(_B)
_RbtwsRadioConfigState_Type=RbtwsRadioConfigState
_RbtwsRadioConfigState_Object=MibScalar
rbtwsRadioConfigState=_RbtwsRadioConfigState_Object((1,3,6,1,4,1,52,4,15,1,2,64),_RbtwsRadioConfigState_Type())
rbtwsRadioConfigState.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsRadioConfigState.setStatus(_B)
_RbtwsApConnectSecurityType_Type=RbtwsApConnectSecurityType
_RbtwsApConnectSecurityType_Object=MibScalar
rbtwsApConnectSecurityType=_RbtwsApConnectSecurityType_Object((1,3,6,1,4,1,52,4,15,1,2,65),_RbtwsApConnectSecurityType_Type())
rbtwsApConnectSecurityType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsApConnectSecurityType.setStatus(_B)
_RbtwsApServiceAvailability_Type=RbtwsApServiceAvailability
_RbtwsApServiceAvailability_Object=MibScalar
rbtwsApServiceAvailability=_RbtwsApServiceAvailability_Object((1,3,6,1,4,1,52,4,15,1,2,66),_RbtwsApServiceAvailability_Type())
rbtwsApServiceAvailability.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsApServiceAvailability.setStatus(_B)
_RbtwsApWasOperational_Type=RbtwsApWasOperational
_RbtwsApWasOperational_Object=MibScalar
rbtwsApWasOperational=_RbtwsApWasOperational_Object((1,3,6,1,4,1,52,4,15,1,2,67),_RbtwsApWasOperational_Type())
rbtwsApWasOperational.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsApWasOperational.setStatus(_B)
_RbtwsClientTimeSinceLastRoam_Type=Unsigned32
_RbtwsClientTimeSinceLastRoam_Object=MibScalar
rbtwsClientTimeSinceLastRoam=_RbtwsClientTimeSinceLastRoam_Object((1,3,6,1,4,1,52,4,15,1,2,68),_RbtwsClientTimeSinceLastRoam_Type())
rbtwsClientTimeSinceLastRoam.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientTimeSinceLastRoam.setStatus(_B)
_RbtwsClientIpAddrChangeReason_Type=RbtwsClientIpAddrChangeReason
_RbtwsClientIpAddrChangeReason_Object=MibScalar
rbtwsClientIpAddrChangeReason=_RbtwsClientIpAddrChangeReason_Object((1,3,6,1,4,1,52,4,15,1,2,69),_RbtwsClientIpAddrChangeReason_Type())
rbtwsClientIpAddrChangeReason.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientIpAddrChangeReason.setStatus(_B)
_RbtwsRFDetectRogueAPMacAddr_Type=MacAddress
_RbtwsRFDetectRogueAPMacAddr_Object=MibScalar
rbtwsRFDetectRogueAPMacAddr=_RbtwsRFDetectRogueAPMacAddr_Object((1,3,6,1,4,1,52,4,15,1,2,70),_RbtwsRFDetectRogueAPMacAddr_Type())
rbtwsRFDetectRogueAPMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsRFDetectRogueAPMacAddr.setStatus(_B)
_RbtwsBlacklistingRemainingTime_Type=Unsigned32
_RbtwsBlacklistingRemainingTime_Object=MibScalar
rbtwsBlacklistingRemainingTime=_RbtwsBlacklistingRemainingTime_Object((1,3,6,1,4,1,52,4,15,1,2,71),_RbtwsBlacklistingRemainingTime_Type())
rbtwsBlacklistingRemainingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsBlacklistingRemainingTime.setStatus(_B)
_RbtwsBlacklistingCause_Type=RbtwsBlacklistingCause
_RbtwsBlacklistingCause_Object=MibScalar
rbtwsBlacklistingCause=_RbtwsBlacklistingCause_Object((1,3,6,1,4,1,52,4,15,1,2,72),_RbtwsBlacklistingCause_Type())
rbtwsBlacklistingCause.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsBlacklistingCause.setStatus(_B)
_RbtwsNumLicensedActiveAPs_Type=Unsigned32
_RbtwsNumLicensedActiveAPs_Object=MibScalar
rbtwsNumLicensedActiveAPs=_RbtwsNumLicensedActiveAPs_Object((1,3,6,1,4,1,52,4,15,1,2,73),_RbtwsNumLicensedActiveAPs_Type())
rbtwsNumLicensedActiveAPs.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsNumLicensedActiveAPs.setStatus(_B)
_RbtwsClientDynAuthorClientIp_Type=IpAddress
_RbtwsClientDynAuthorClientIp_Object=MibScalar
rbtwsClientDynAuthorClientIp=_RbtwsClientDynAuthorClientIp_Object((1,3,6,1,4,1,52,4,15,1,2,74),_RbtwsClientDynAuthorClientIp_Type())
rbtwsClientDynAuthorClientIp.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientDynAuthorClientIp.setStatus(_B)
_RbtwsChangedUserParamOldValues_Type=RbtwsUserAttributeList
_RbtwsChangedUserParamOldValues_Object=MibScalar
rbtwsChangedUserParamOldValues=_RbtwsChangedUserParamOldValues_Object((1,3,6,1,4,1,52,4,15,1,2,75),_RbtwsChangedUserParamOldValues_Type())
rbtwsChangedUserParamOldValues.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsChangedUserParamOldValues.setStatus(_B)
_RbtwsChangedUserParamNewValues_Type=RbtwsUserAttributeList
_RbtwsChangedUserParamNewValues_Object=MibScalar
rbtwsChangedUserParamNewValues=_RbtwsChangedUserParamNewValues_Object((1,3,6,1,4,1,52,4,15,1,2,76),_RbtwsChangedUserParamNewValues_Type())
rbtwsChangedUserParamNewValues.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsChangedUserParamNewValues.setStatus(_B)
_RbtwsClientDisconnectSource_Type=RbtwsSessionDisconnectType
_RbtwsClientDisconnectSource_Object=MibScalar
rbtwsClientDisconnectSource=_RbtwsClientDisconnectSource_Object((1,3,6,1,4,1,52,4,15,1,2,77),_RbtwsClientDisconnectSource_Type())
rbtwsClientDisconnectSource.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientDisconnectSource.setStatus(_B)
class _RbtwsClientDisconnectDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RbtwsClientDisconnectDescription_Type.__name__=_O
_RbtwsClientDisconnectDescription_Object=MibScalar
rbtwsClientDisconnectDescription=_RbtwsClientDisconnectDescription_Object((1,3,6,1,4,1,52,4,15,1,2,78),_RbtwsClientDisconnectDescription_Type())
rbtwsClientDisconnectDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientDisconnectDescription.setStatus(_B)
_RbtwsMobilityDomainSecondarySeedIp_Type=IpAddress
_RbtwsMobilityDomainSecondarySeedIp_Object=MibScalar
rbtwsMobilityDomainSecondarySeedIp=_RbtwsMobilityDomainSecondarySeedIp_Object((1,3,6,1,4,1,52,4,15,1,2,79),_RbtwsMobilityDomainSecondarySeedIp_Type())
rbtwsMobilityDomainSecondarySeedIp.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsMobilityDomainSecondarySeedIp.setStatus(_B)
_RbtwsMobilityDomainPrimarySeedIp_Type=IpAddress
_RbtwsMobilityDomainPrimarySeedIp_Object=MibScalar
rbtwsMobilityDomainPrimarySeedIp=_RbtwsMobilityDomainPrimarySeedIp_Object((1,3,6,1,4,1,52,4,15,1,2,80),_RbtwsMobilityDomainPrimarySeedIp_Type())
rbtwsMobilityDomainPrimarySeedIp.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsMobilityDomainPrimarySeedIp.setStatus(_B)
_RbtwsRFDetectClassificationReason_Type=RbtwsRFDetectClassificationReason
_RbtwsRFDetectClassificationReason_Object=MibScalar
rbtwsRFDetectClassificationReason=_RbtwsRFDetectClassificationReason_Object((1,3,6,1,4,1,52,4,15,1,2,81),_RbtwsRFDetectClassificationReason_Type())
rbtwsRFDetectClassificationReason.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsRFDetectClassificationReason.setStatus(_B)
class _RbtwsConfigSaveFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RbtwsConfigSaveFileName_Type.__name__=_O
_RbtwsConfigSaveFileName_Object=MibScalar
rbtwsConfigSaveFileName=_RbtwsConfigSaveFileName_Object((1,3,6,1,4,1,52,4,15,1,2,82),_RbtwsConfigSaveFileName_Type())
rbtwsConfigSaveFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsConfigSaveFileName.setStatus(_B)
_RbtwsConfigSaveInitiatorType_Type=RbtwsConfigSaveInitiatorType
_RbtwsConfigSaveInitiatorType_Object=MibScalar
rbtwsConfigSaveInitiatorType=_RbtwsConfigSaveInitiatorType_Object((1,3,6,1,4,1,52,4,15,1,2,83),_RbtwsConfigSaveInitiatorType_Type())
rbtwsConfigSaveInitiatorType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsConfigSaveInitiatorType.setStatus(_B)
_RbtwsConfigSaveInitiatorIp_Type=IpAddress
_RbtwsConfigSaveInitiatorIp_Object=MibScalar
rbtwsConfigSaveInitiatorIp=_RbtwsConfigSaveInitiatorIp_Object((1,3,6,1,4,1,52,4,15,1,2,84),_RbtwsConfigSaveInitiatorIp_Type())
rbtwsConfigSaveInitiatorIp.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsConfigSaveInitiatorIp.setStatus(_B)
class _RbtwsConfigSaveInitiatorDetails_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RbtwsConfigSaveInitiatorDetails_Type.__name__=_O
_RbtwsConfigSaveInitiatorDetails_Object=MibScalar
rbtwsConfigSaveInitiatorDetails=_RbtwsConfigSaveInitiatorDetails_Object((1,3,6,1,4,1,52,4,15,1,2,85),_RbtwsConfigSaveInitiatorDetails_Type())
rbtwsConfigSaveInitiatorDetails.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsConfigSaveInitiatorDetails.setStatus(_B)
_RbtwsConfigSaveGeneration_Type=Counter32
_RbtwsConfigSaveGeneration_Object=MibScalar
rbtwsConfigSaveGeneration=_RbtwsConfigSaveGeneration_Object((1,3,6,1,4,1,52,4,15,1,2,86),_RbtwsConfigSaveGeneration_Type())
rbtwsConfigSaveGeneration.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsConfigSaveGeneration.setStatus(_B)
_RbtwsApNum_Type=RbtwsApNum
_RbtwsApNum_Object=MibScalar
rbtwsApNum=_RbtwsApNum_Object((1,3,6,1,4,1,52,4,15,1,2,87),_RbtwsApNum_Type())
rbtwsApNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsApNum.setStatus(_B)
_RbtwsRadioMode_Type=RbtwsRadioMode
_RbtwsRadioMode_Object=MibScalar
rbtwsRadioMode=_RbtwsRadioMode_Object((1,3,6,1,4,1,52,4,15,1,2,88),_RbtwsRadioMode_Type())
rbtwsRadioMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsRadioMode.setStatus(_B)
_RbtwsMichaelMICFailureCause_Type=RbtwsMichaelMICFailureCause
_RbtwsMichaelMICFailureCause_Object=MibScalar
rbtwsMichaelMICFailureCause=_RbtwsMichaelMICFailureCause_Object((1,3,6,1,4,1,52,4,15,1,2,89),_RbtwsMichaelMICFailureCause_Type())
rbtwsMichaelMICFailureCause.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsMichaelMICFailureCause.setStatus(_B)
_RbtwsClientAccessMode_Type=RbtwsClientAccessMode
_RbtwsClientAccessMode_Object=MibScalar
rbtwsClientAccessMode=_RbtwsClientAccessMode_Object((1,3,6,1,4,1,52,4,15,1,2,90),_RbtwsClientAccessMode_Type())
rbtwsClientAccessMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientAccessMode.setStatus(_B)
_RbtwsClientAuthorizationReason_Type=RbtwsClientAuthorizationReason
_RbtwsClientAuthorizationReason_Object=MibScalar
rbtwsClientAuthorizationReason=_RbtwsClientAuthorizationReason_Object((1,3,6,1,4,1,52,4,15,1,2,91),_RbtwsClientAuthorizationReason_Type())
rbtwsClientAuthorizationReason.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientAuthorizationReason.setStatus(_B)
class _RbtwsPhysPortNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_RbtwsPhysPortNum_Type.__name__=_A8
_RbtwsPhysPortNum_Object=MibScalar
rbtwsPhysPortNum=_RbtwsPhysPortNum_Object((1,3,6,1,4,1,52,4,15,1,2,92),_RbtwsPhysPortNum_Type())
rbtwsPhysPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsPhysPortNum.setStatus(_B)
_RbtwsApMgrOldIp_Type=IpAddress
_RbtwsApMgrOldIp_Object=MibScalar
rbtwsApMgrOldIp=_RbtwsApMgrOldIp_Object((1,3,6,1,4,1,52,4,15,1,2,93),_RbtwsApMgrOldIp_Type())
rbtwsApMgrOldIp.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsApMgrOldIp.setStatus(_B)
_RbtwsApMgrNewIp_Type=IpAddress
_RbtwsApMgrNewIp_Object=MibScalar
rbtwsApMgrNewIp=_RbtwsApMgrNewIp_Object((1,3,6,1,4,1,52,4,15,1,2,94),_RbtwsApMgrNewIp_Type())
rbtwsApMgrNewIp.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsApMgrNewIp.setStatus(_B)
_RbtwsApMgrChangeReason_Type=RbtwsApMgrChangeReason
_RbtwsApMgrChangeReason_Object=MibScalar
rbtwsApMgrChangeReason=_RbtwsApMgrChangeReason_Object((1,3,6,1,4,1,52,4,15,1,2,95),_RbtwsApMgrChangeReason_Type())
rbtwsApMgrChangeReason.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsApMgrChangeReason.setStatus(_B)
_RbtwsClientClearedReason_Type=RbtwsClientClearedReason
_RbtwsClientClearedReason_Object=MibScalar
rbtwsClientClearedReason=_RbtwsClientClearedReason_Object((1,3,6,1,4,1,52,4,15,1,2,96),_RbtwsClientClearedReason_Type())
rbtwsClientClearedReason.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientClearedReason.setStatus(_B)
_RbtwsMobilityDomainResiliencyStatus_Type=RbtwsMobilityDomainResiliencyStatus
_RbtwsMobilityDomainResiliencyStatus_Object=MibScalar
rbtwsMobilityDomainResiliencyStatus=_RbtwsMobilityDomainResiliencyStatus_Object((1,3,6,1,4,1,52,4,15,1,2,97),_RbtwsMobilityDomainResiliencyStatus_Type())
rbtwsMobilityDomainResiliencyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsMobilityDomainResiliencyStatus.setStatus(_B)
_RbtwsClientSessionElapsedSeconds_Type=Unsigned32
_RbtwsClientSessionElapsedSeconds_Object=MibScalar
rbtwsClientSessionElapsedSeconds=_RbtwsClientSessionElapsedSeconds_Object((1,3,6,1,4,1,52,4,15,1,2,98),_RbtwsClientSessionElapsedSeconds_Type())
rbtwsClientSessionElapsedSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientSessionElapsedSeconds.setStatus(_B)
_RbtwsRadioChannelWidth_Type=RbtwsRadioChannelWidth
_RbtwsRadioChannelWidth_Object=MibScalar
rbtwsRadioChannelWidth=_RbtwsRadioChannelWidth_Object((1,3,6,1,4,1,52,4,15,1,2,99),_RbtwsRadioChannelWidth_Type())
rbtwsRadioChannelWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsRadioChannelWidth.setStatus(_B)
_RbtwsRadioMimoState_Type=RbtwsRadioMimoState
_RbtwsRadioMimoState_Object=MibScalar
rbtwsRadioMimoState=_RbtwsRadioMimoState_Object((1,3,6,1,4,1,52,4,15,1,2,100),_RbtwsRadioMimoState_Type())
rbtwsRadioMimoState.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsRadioMimoState.setStatus(_B)
_RbtwsClientRadioType_Type=RbtwsRadioType
_RbtwsClientRadioType_Object=MibScalar
rbtwsClientRadioType=_RbtwsClientRadioType_Object((1,3,6,1,4,1,52,4,15,1,2,101),_RbtwsClientRadioType_Type())
rbtwsClientRadioType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClientRadioType.setStatus(_B)
_RbtwsRFDetectXmtrRadioType_Type=RbtwsRadioType
_RbtwsRFDetectXmtrRadioType_Object=MibScalar
rbtwsRFDetectXmtrRadioType=_RbtwsRFDetectXmtrRadioType_Object((1,3,6,1,4,1,52,4,15,1,2,102),_RbtwsRFDetectXmtrRadioType_Type())
rbtwsRFDetectXmtrRadioType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsRFDetectXmtrRadioType.setStatus(_B)
_RbtwsRFDetectXmtrCryptoType_Type=RbtwsCryptoType
_RbtwsRFDetectXmtrCryptoType_Object=MibScalar
rbtwsRFDetectXmtrCryptoType=_RbtwsRFDetectXmtrCryptoType_Object((1,3,6,1,4,1,52,4,15,1,2,103),_RbtwsRFDetectXmtrCryptoType_Type())
rbtwsRFDetectXmtrCryptoType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsRFDetectXmtrCryptoType.setStatus(_B)
_RbtwsClusterFailureReason_Type=RbtwsClusterFailureReason
_RbtwsClusterFailureReason_Object=MibScalar
rbtwsClusterFailureReason=_RbtwsClusterFailureReason_Object((1,3,6,1,4,1,52,4,15,1,2,104),_RbtwsClusterFailureReason_Type())
rbtwsClusterFailureReason.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClusterFailureReason.setStatus(_B)
class _RbtwsClusterFailureDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RbtwsClusterFailureDescription_Type.__name__=_O
_RbtwsClusterFailureDescription_Object=MibScalar
rbtwsClusterFailureDescription=_RbtwsClusterFailureDescription_Object((1,3,6,1,4,1,52,4,15,1,2,105),_RbtwsClusterFailureDescription_Type())
rbtwsClusterFailureDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsClusterFailureDescription.setStatus(_B)
_RbtwsTrapsV2_ObjectIdentity=ObjectIdentity
rbtwsTrapsV2=_RbtwsTrapsV2_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,5,0))
rbtwsDeviceFailTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,1))
rbtwsDeviceFailTrap.setObjects((_A,_p))
if mibBuilder.loadTexts:rbtwsDeviceFailTrap.setStatus(_B)
rbtwsDeviceOkayTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,2))
rbtwsDeviceOkayTrap.setObjects((_A,_p))
if mibBuilder.loadTexts:rbtwsDeviceOkayTrap.setStatus(_B)
rbtwsPoEFailTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,3))
rbtwsPoEFailTrap.setObjects((_A,_E))
if mibBuilder.loadTexts:rbtwsPoEFailTrap.setStatus(_B)
rbtwsApTimeoutTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,4))
rbtwsApTimeoutTrap.setObjects(*((_A,_E),(_A,_b),(_A,_q),(_A,_I)))
if mibBuilder.loadTexts:rbtwsApTimeoutTrap.setStatus(_D)
rbtwsAPBootTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,5))
rbtwsAPBootTrap.setObjects(*((_A,_E),(_A,_b),(_A,_q),(_A,_I)))
if mibBuilder.loadTexts:rbtwsAPBootTrap.setStatus(_D)
rbtwsMobilityDomainJoinTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,6))
rbtwsMobilityDomainJoinTrap.setObjects((_A,_r))
if mibBuilder.loadTexts:rbtwsMobilityDomainJoinTrap.setStatus(_B)
rbtwsMobilityDomainTimeoutTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,7))
rbtwsMobilityDomainTimeoutTrap.setObjects((_A,_r))
if mibBuilder.loadTexts:rbtwsMobilityDomainTimeoutTrap.setStatus(_B)
rbtwsMpMichaelMICFailure=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,8))
rbtwsMpMichaelMICFailure.setObjects(*((_A,_E),(_A,_T),(_A,_J),(_A,_F),(_A,_H),(_A,_H)))
if mibBuilder.loadTexts:rbtwsMpMichaelMICFailure.setStatus(_D)
rbtwsRFDetectRogueAPTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,9))
rbtwsRFDetectRogueAPTrap.setObjects(*((_A,_G),(_A,_L)))
if mibBuilder.loadTexts:rbtwsRFDetectRogueAPTrap.setStatus(_D)
rbtwsRFDetectAdhocUserTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,10))
rbtwsRFDetectAdhocUserTrap.setObjects(*((_A,_G),(_A,_L)))
if mibBuilder.loadTexts:rbtwsRFDetectAdhocUserTrap.setStatus(_B)
rbtwsRFDetectRogueDisappearTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,11))
rbtwsRFDetectRogueDisappearTrap.setObjects((_A,_G))
if mibBuilder.loadTexts:rbtwsRFDetectRogueDisappearTrap.setStatus(_D)
rbtwsClientAuthenticationFailureTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,12))
rbtwsClientAuthenticationFailureTrap.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_U),(_A,_Q),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J),(_A,_AB),(_A,_c)))
if mibBuilder.loadTexts:rbtwsClientAuthenticationFailureTrap.setStatus(_B)
rbtwsClientAuthorizationFailureTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,13))
rbtwsClientAuthorizationFailureTrap.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_U),(_A,_Q),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J),(_A,_AC),(_A,_s),(_A,_t),(_A,_c)))
if mibBuilder.loadTexts:rbtwsClientAuthorizationFailureTrap.setStatus(_B)
rbtwsClientAssociationFailureTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,14))
rbtwsClientAssociationFailureTrap.setObjects(*((_A,_H),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J),(_A,_AD),(_A,_c)))
if mibBuilder.loadTexts:rbtwsClientAssociationFailureTrap.setStatus(_B)
rbtwsClientAuthorizationSuccessTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,15))
rbtwsClientAuthorizationSuccessTrap.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_X),(_A,_Z),(_A,_u),(_A,_U),(_A,_Q),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J),(_A,_AE)))
if mibBuilder.loadTexts:rbtwsClientAuthorizationSuccessTrap.setStatus(_D)
rbtwsClientDeAssociationTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,16))
rbtwsClientDeAssociationTrap.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_X),(_A,_U),(_A,_Q),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:rbtwsClientDeAssociationTrap.setStatus(_B)
rbtwsClientRoamingTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,17))
rbtwsClientRoamingTrap.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:rbtwsClientRoamingTrap.setStatus(_B)
rbtwsAutoTuneRadioPowerChangeTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,18))
rbtwsAutoTuneRadioPowerChangeTrap.setObjects(*((_A,_T),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:rbtwsAutoTuneRadioPowerChangeTrap.setStatus(_B)
rbtwsAutoTuneRadioChannelChangeTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,19))
rbtwsAutoTuneRadioChannelChangeTrap.setObjects(*((_A,_T),(_A,_AP),(_A,_AQ),(_A,_AR)))
if mibBuilder.loadTexts:rbtwsAutoTuneRadioChannelChangeTrap.setStatus(_B)
rbtwsCounterMeasureStartTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,20))
rbtwsCounterMeasureStartTrap.setObjects(*((_A,_G),(_A,_T)))
if mibBuilder.loadTexts:rbtwsCounterMeasureStartTrap.setStatus(_B)
rbtwsCounterMeasureStopTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,21))
rbtwsCounterMeasureStopTrap.setObjects(*((_A,_G),(_A,_T)))
if mibBuilder.loadTexts:rbtwsCounterMeasureStopTrap.setStatus(_B)
rbtwsClientDot1xFailureTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,22))
rbtwsClientDot1xFailureTrap.setObjects(*((_A,_M),(_A,_H),(_A,_Q),(_A,_K),(_A,_I),(_A,_E),(_A,_F),(_A,_J),(_A,_AS),(_A,_AT),(_A,_c)))
if mibBuilder.loadTexts:rbtwsClientDot1xFailureTrap.setStatus(_B)
rbtwsClientClearedTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,23))
rbtwsClientClearedTrap.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J),(_A,_AU),(_A,_V)))
if mibBuilder.loadTexts:rbtwsClientClearedTrap.setStatus(_D)
rbtwsClientAuthorizationSuccessTrap2=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,24))
rbtwsClientAuthorizationSuccessTrap2.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_X),(_A,_Z),(_A,_u),(_A,_U),(_A,_Q),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J),(_A,_d),(_A,_V)))
if mibBuilder.loadTexts:rbtwsClientAuthorizationSuccessTrap2.setStatus(_D)
rbtwsRFDetectSpoofedMacAPTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,25))
rbtwsRFDetectSpoofedMacAPTrap.setObjects(*((_A,_G),(_A,_L)))
if mibBuilder.loadTexts:rbtwsRFDetectSpoofedMacAPTrap.setStatus(_D)
rbtwsRFDetectSpoofedSsidAPTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,26))
rbtwsRFDetectSpoofedSsidAPTrap.setObjects(*((_A,_G),(_A,_L)))
if mibBuilder.loadTexts:rbtwsRFDetectSpoofedSsidAPTrap.setStatus(_D)
rbtwsRFDetectDoSTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,27))
rbtwsRFDetectDoSTrap.setObjects(*((_A,_v),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:rbtwsRFDetectDoSTrap.setStatus(_B)
rbtwsRFDetectClientViaRogueWiredAPTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,28))
rbtwsRFDetectClientViaRogueWiredAPTrap.setObjects(*((_A,_f),(_A,_E),(_A,_g),(_A,_h),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:rbtwsRFDetectClientViaRogueWiredAPTrap.setStatus(_D)
rbtwsRFDetectInterferingRogueAPTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,29))
rbtwsRFDetectInterferingRogueAPTrap.setObjects(*((_A,_G),(_A,_L)))
if mibBuilder.loadTexts:rbtwsRFDetectInterferingRogueAPTrap.setStatus(_D)
rbtwsRFDetectInterferingRogueDisappearTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,30))
rbtwsRFDetectInterferingRogueDisappearTrap.setObjects((_A,_G))
if mibBuilder.loadTexts:rbtwsRFDetectInterferingRogueDisappearTrap.setStatus(_D)
rbtwsRFDetectUnAuthorizedSsidTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,31))
rbtwsRFDetectUnAuthorizedSsidTrap.setObjects(*((_A,_G),(_A,_L)))
if mibBuilder.loadTexts:rbtwsRFDetectUnAuthorizedSsidTrap.setStatus(_D)
rbtwsRFDetectUnAuthorizedOuiTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,32))
rbtwsRFDetectUnAuthorizedOuiTrap.setObjects(*((_A,_G),(_A,_L)))
if mibBuilder.loadTexts:rbtwsRFDetectUnAuthorizedOuiTrap.setStatus(_D)
rbtwsRFDetectUnAuthorizedAPTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,33))
rbtwsRFDetectUnAuthorizedAPTrap.setObjects(*((_A,_G),(_A,_L)))
if mibBuilder.loadTexts:rbtwsRFDetectUnAuthorizedAPTrap.setStatus(_D)
rbtwsDAPConnectWarningTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,34))
rbtwsDAPConnectWarningTrap.setObjects(*((_A,_AV),(_A,_Y),(_A,_AW),(_A,_AX)))
if mibBuilder.loadTexts:rbtwsDAPConnectWarningTrap.setStatus(_D)
rbtwsRFDetectDoSPortTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,35))
rbtwsRFDetectDoSPortTrap.setObjects(*((_A,_v),(_A,_G),(_A,_K),(_A,_E),(_A,_I)))
if mibBuilder.loadTexts:rbtwsRFDetectDoSPortTrap.setStatus(_B)
rbtwsMpMichaelMICFailure2=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,36))
rbtwsMpMichaelMICFailure2.setObjects(*((_A,_E),(_A,_F),(_A,_H),(_A,_w)))
if mibBuilder.loadTexts:rbtwsMpMichaelMICFailure2.setStatus(_D)
rbtwsApNonOperStatusTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,37))
rbtwsApNonOperStatusTrap.setObjects(*((_A,_Y),(_A,_b),(_A,_x),(_A,_y),(_A,_a),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:rbtwsApNonOperStatusTrap.setStatus(_D)
rbtwsApOperRadioStatusTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,38))
rbtwsApOperRadioStatusTrap.setObjects(*((_A,_Y),(_A,_x),(_A,_y),(_A,_a),(_A,_F),(_A,_T),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:rbtwsApOperRadioStatusTrap.setStatus(_D)
rbtwsClientIpAddrChangeTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,39))
rbtwsClientIpAddrChangeTrap.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_X),(_A,_Z),(_A,_U),(_A,_Q),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J),(_A,_d),(_A,_V),(_A,_AY)))
if mibBuilder.loadTexts:rbtwsClientIpAddrChangeTrap.setStatus(_B)
rbtwsClientAssociationSuccessTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,40))
rbtwsClientAssociationSuccessTrap.setObjects(*((_A,_H),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:rbtwsClientAssociationSuccessTrap.setStatus(_B)
rbtwsClientAuthenticationSuccessTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,41))
rbtwsClientAuthenticationSuccessTrap.setObjects(*((_A,_H),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:rbtwsClientAuthenticationSuccessTrap.setStatus(_B)
rbtwsClientDeAuthenticationTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,42))
rbtwsClientDeAuthenticationTrap.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_X),(_A,_U),(_A,_Q),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:rbtwsClientDeAuthenticationTrap.setStatus(_B)
rbtwsRFDetectBlacklistedTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,43))
rbtwsRFDetectBlacklistedTrap.setObjects(*((_A,_G),(_A,_K),(_A,_E),(_A,_I),(_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:rbtwsRFDetectBlacklistedTrap.setStatus(_B)
rbtwsRFDetectClientViaRogueWiredAPTrap2=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,44))
rbtwsRFDetectClientViaRogueWiredAPTrap2.setObjects(*((_A,_f),(_A,_E),(_A,_g),(_A,_h),(_A,_G),(_A,_L),(_A,_A2)))
if mibBuilder.loadTexts:rbtwsRFDetectClientViaRogueWiredAPTrap2.setStatus(_D)
rbtwsRFDetectAdhocUserDisappearTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,45))
rbtwsRFDetectAdhocUserDisappearTrap.setObjects((_A,_G))
if mibBuilder.loadTexts:rbtwsRFDetectAdhocUserDisappearTrap.setStatus(_B)
rbtwsApRejectLicenseExceededTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,46))
rbtwsApRejectLicenseExceededTrap.setObjects((_A,_Ab))
if mibBuilder.loadTexts:rbtwsApRejectLicenseExceededTrap.setStatus(_B)
rbtwsClientDynAuthorChangeSuccessTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,47))
rbtwsClientDynAuthorChangeSuccessTrap.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_Z),(_A,_A3),(_A,_Q),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J),(_A,_d),(_A,_V),(_A,_Ac),(_A,_Ad)))
if mibBuilder.loadTexts:rbtwsClientDynAuthorChangeSuccessTrap.setStatus(_B)
rbtwsClientDynAuthorChangeFailureTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,48))
rbtwsClientDynAuthorChangeFailureTrap.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_A3),(_A,_Q),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J),(_A,_s),(_A,_t),(_A,_c)))
if mibBuilder.loadTexts:rbtwsClientDynAuthorChangeFailureTrap.setStatus(_B)
rbtwsClientDisconnectTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,49))
rbtwsClientDisconnectTrap.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J),(_A,_V),(_A,_Ae),(_A,_Af)))
if mibBuilder.loadTexts:rbtwsClientDisconnectTrap.setStatus(_B)
rbtwsMobilityDomainFailOverTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,50))
rbtwsMobilityDomainFailOverTrap.setObjects((_A,_Ag))
if mibBuilder.loadTexts:rbtwsMobilityDomainFailOverTrap.setStatus(_B)
rbtwsMobilityDomainFailBackTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,51))
rbtwsMobilityDomainFailBackTrap.setObjects((_A,_Ah))
if mibBuilder.loadTexts:rbtwsMobilityDomainFailBackTrap.setStatus(_B)
rbtwsRFDetectRogueDeviceTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,52))
rbtwsRFDetectRogueDeviceTrap.setObjects(*((_A,_G),(_A,_L),(_A,_e)))
if mibBuilder.loadTexts:rbtwsRFDetectRogueDeviceTrap.setStatus(_D)
rbtwsRFDetectRogueDeviceDisappearTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,53))
rbtwsRFDetectRogueDeviceDisappearTrap.setObjects((_A,_G))
if mibBuilder.loadTexts:rbtwsRFDetectRogueDeviceDisappearTrap.setStatus(_B)
rbtwsRFDetectSuspectDeviceTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,54))
rbtwsRFDetectSuspectDeviceTrap.setObjects(*((_A,_G),(_A,_L),(_A,_e)))
if mibBuilder.loadTexts:rbtwsRFDetectSuspectDeviceTrap.setStatus(_D)
rbtwsRFDetectSuspectDeviceDisappearTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,55))
rbtwsRFDetectSuspectDeviceDisappearTrap.setObjects((_A,_G))
if mibBuilder.loadTexts:rbtwsRFDetectSuspectDeviceDisappearTrap.setStatus(_B)
rbtwsRFDetectClientViaRogueWiredAPTrap3=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,56))
rbtwsRFDetectClientViaRogueWiredAPTrap3.setObjects(*((_A,_f),(_A,_E),(_A,_g),(_A,_h),(_A,_G),(_A,_L),(_A,_A2),(_A,_e)))
if mibBuilder.loadTexts:rbtwsRFDetectClientViaRogueWiredAPTrap3.setStatus(_B)
rbtwsRFDetectClassificationChangeTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,57))
if mibBuilder.loadTexts:rbtwsRFDetectClassificationChangeTrap.setStatus(_B)
rbtwsConfigurationSavedTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,58))
rbtwsConfigurationSavedTrap.setObjects(*((_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am)))
if mibBuilder.loadTexts:rbtwsConfigurationSavedTrap.setStatus(_B)
rbtwsApNonOperStatusTrap2=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,59))
rbtwsApNonOperStatusTrap2.setObjects(*((_A,_Y),(_A,_b),(_A,_W),(_A,_a),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:rbtwsApNonOperStatusTrap2.setStatus(_B)
rbtwsApOperRadioStatusTrap2=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,60))
rbtwsApOperRadioStatusTrap2.setObjects(*((_A,_Y),(_A,_W),(_A,_a),(_A,_F),(_A,_T),(_A,_i),(_A,_A4),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:rbtwsApOperRadioStatusTrap2.setStatus(_D)
rbtwsMichaelMICFailure=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,61))
rbtwsMichaelMICFailure.setObjects(*((_A,_W),(_A,_F),(_A,_T),(_A,_An),(_A,_H),(_A,_w)))
if mibBuilder.loadTexts:rbtwsMichaelMICFailure.setStatus(_B)
rbtwsClientAuthorizationSuccessTrap3=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,62))
rbtwsClientAuthorizationSuccessTrap3.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_X),(_A,_Z),(_A,_U),(_A,_Q),(_A,_m),(_A,_n),(_A,_W),(_A,_F),(_A,_J),(_A,_d),(_A,_V),(_A,_A5)))
if mibBuilder.loadTexts:rbtwsClientAuthorizationSuccessTrap3.setStatus(_D)
rbtwsApManagerChangeTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,63))
rbtwsApManagerChangeTrap.setObjects(*((_A,_Y),(_A,_b),(_A,_W),(_A,_a),(_A,_Ao),(_A,_Ap),(_A,_Aq)))
if mibBuilder.loadTexts:rbtwsApManagerChangeTrap.setStatus(_B)
rbtwsClientClearedTrap2=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,64))
rbtwsClientClearedTrap2.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_m),(_A,_n),(_A,_W),(_A,_F),(_A,_J),(_A,_Ar),(_A,_V),(_A,_As)))
if mibBuilder.loadTexts:rbtwsClientClearedTrap2.setStatus(_B)
rbtwsMobilityDomainResiliencyStatusTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,65))
rbtwsMobilityDomainResiliencyStatusTrap.setObjects((_A,_At))
if mibBuilder.loadTexts:rbtwsMobilityDomainResiliencyStatusTrap.setStatus(_B)
rbtwsApOperRadioStatusTrap3=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,66))
rbtwsApOperRadioStatusTrap3.setObjects(*((_A,_Y),(_A,_W),(_A,_a),(_A,_F),(_A,_T),(_A,_i),(_A,_A4),(_A,_j),(_A,_Au),(_A,_Av),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:rbtwsApOperRadioStatusTrap3.setStatus(_B)
rbtwsClientAuthorizationSuccessTrap4=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,67))
rbtwsClientAuthorizationSuccessTrap4.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_X),(_A,_Z),(_A,_U),(_A,_Q),(_A,_m),(_A,_n),(_A,_W),(_A,_F),(_A,_J),(_A,_Aw),(_A,_d),(_A,_V),(_A,_A5)))
if mibBuilder.loadTexts:rbtwsClientAuthorizationSuccessTrap4.setStatus(_B)
rbtwsRFDetectRogueDeviceTrap2=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,68))
rbtwsRFDetectRogueDeviceTrap2.setObjects(*((_A,_G),(_A,_A6),(_A,_A7),(_A,_L),(_A,_e)))
if mibBuilder.loadTexts:rbtwsRFDetectRogueDeviceTrap2.setStatus(_B)
rbtwsRFDetectSuspectDeviceTrap2=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,69))
rbtwsRFDetectSuspectDeviceTrap2.setObjects(*((_A,_G),(_A,_A6),(_A,_A7),(_A,_L),(_A,_e)))
if mibBuilder.loadTexts:rbtwsRFDetectSuspectDeviceTrap2.setStatus(_B)
rbtwsClusterFailureTrap=NotificationType((1,3,6,1,4,1,52,4,15,1,5,0,70))
rbtwsClusterFailureTrap.setObjects(*((_A,_Ax),(_A,_Ay)))
if mibBuilder.loadTexts:rbtwsClusterFailureTrap.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'RbtwsAssociationFailureType':RbtwsAssociationFailureType,'RbtwsAuthenticationFailureType':RbtwsAuthenticationFailureType,'RbtwsAuthorizationFailureType':RbtwsAuthorizationFailureType,'RbtwsDot1xFailureType':RbtwsDot1xFailureType,'RbtwsRFDetectDoSType':RbtwsRFDetectDoSType,'RbtwsClientIpAddrChangeReason':RbtwsClientIpAddrChangeReason,'RbtwsBlacklistingCause':RbtwsBlacklistingCause,'RbtwsUserAttributeList':RbtwsUserAttributeList,'RbtwsSessionDisconnectType':RbtwsSessionDisconnectType,'RbtwsConfigSaveInitiatorType':RbtwsConfigSaveInitiatorType,'RbtwsMichaelMICFailureCause':RbtwsMichaelMICFailureCause,'RbtwsClientAuthorizationReason':RbtwsClientAuthorizationReason,'RbtwsApMgrChangeReason':RbtwsApMgrChangeReason,'RbtwsClientClearedReason':RbtwsClientClearedReason,'RbtwsMobilityDomainResiliencyStatus':RbtwsMobilityDomainResiliencyStatus,'RbtwsClusterFailureReason':RbtwsClusterFailureReason,_p:rbtwsDeviceId,_r:rbtwsMobilityDomainIp,_b:rbtwsAPMACAddress,_H:rbtwsClientMACAddress,_G:rbtwsRFDetectXmtrMacAddr,_E:rbtwsPortNum,_F:rbtwsAPRadioNum,_AE:rbtwsRadioRssi,'rbtwsRadioBSSID':rbtwsRadioBSSID,_M:rbtwsUserName,_U:rbtwsClientAuthServerIp,_Z:rbtwsClientSessionState,_I:rbtwsDAPNum,_R:rbtwsClientIp,_N:rbtwsClientSessionId,_Q:rbtwsClientAuthenProtocolType,_X:rbtwsClientVLANName,_u:rbtwsClientSessionStartTime,'rbtwsClientFailureCause':rbtwsClientFailureCause,_AG:rbtwsClientRoamedFromPortNum,_AH:rbtwsClientRoamedFromRadioNum,_AI:rbtwsClientRoamedFromDAPNum,_s:rbtwsUserParams,_AC:rbtwsClientLocationPolicyIndex,_AD:rbtwsClientAssociationFailureCause,_AB:rbtwsClientAuthenticationFailureCause,_t:rbtwsClientAuthorizationFailureCause,_c:rbtwsClientFailureCauseDescription,_AJ:rbtwsClientRoamedFromWsIp,_AF:rbtwsClientRoamedFromAccessType,_K:rbtwsClientAccessType,_T:rbtwsRadioMACAddress,_AN:rbtwsRadioPowerChangeReason,_AP:rbtwsNewChannelNum,_AQ:rbtwsOldChannelNum,_AR:rbtwsChannelChangeReason,_L:rbtwsRFDetectListenerListInfo,_J:rbtwsRadioSSID,_AL:rbtwsNewPowerLevel,_AM:rbtwsOldPowerLevel,_AO:rbtwsRadioPowerChangeDescription,'rbtwsCounterMeasurePerformerListInfo':rbtwsCounterMeasurePerformerListInfo,_AS:rbtwsClientDot1xState,_AT:rbtwsClientDot1xFailureCause,_q:rbtwsAPAccessType,_d:rbtwsUserAccessType,_AU:rbtwsClientSessionElapsedTime,_V:rbtwsLocalId,_v:rbtwsRFDetectDoSType,_f:rbtwsSourceWsIp,_g:rbtwsClientVLANid,_h:rbtwsClientVLANtag,_AV:rbtwsDeviceModel,_Y:rbtwsDeviceSerNum,_AW:rbtwsRsaPubKeyFingerPrint,_AX:rbtwsDAPconnectWarningType,_w:rbtwsClientMACAddress2,_x:rbtwsApAttachType,_y:rbtwsApPortOrDapNum,_a:rbtwsApName,_z:rbtwsApTransition,_A0:rbtwsApFailDetail,_i:rbtwsRadioType,_j:rbtwsRadioConfigState,_k:rbtwsApConnectSecurityType,_l:rbtwsApServiceAvailability,_A1:rbtwsApWasOperational,_AK:rbtwsClientTimeSinceLastRoam,_AY:rbtwsClientIpAddrChangeReason,_A2:rbtwsRFDetectRogueAPMacAddr,_AZ:rbtwsBlacklistingRemainingTime,_Aa:rbtwsBlacklistingCause,_Ab:rbtwsNumLicensedActiveAPs,_A3:rbtwsClientDynAuthorClientIp,_Ac:rbtwsChangedUserParamOldValues,_Ad:rbtwsChangedUserParamNewValues,_Ae:rbtwsClientDisconnectSource,_Af:rbtwsClientDisconnectDescription,_Ag:rbtwsMobilityDomainSecondarySeedIp,_Ah:rbtwsMobilityDomainPrimarySeedIp,_e:rbtwsRFDetectClassificationReason,_Ai:rbtwsConfigSaveFileName,_Aj:rbtwsConfigSaveInitiatorType,_Ak:rbtwsConfigSaveInitiatorIp,_Al:rbtwsConfigSaveInitiatorDetails,_Am:rbtwsConfigSaveGeneration,_W:rbtwsApNum,_A4:rbtwsRadioMode,_An:rbtwsMichaelMICFailureCause,_m:rbtwsClientAccessMode,_A5:rbtwsClientAuthorizationReason,_n:rbtwsPhysPortNum,_Ao:rbtwsApMgrOldIp,_Ap:rbtwsApMgrNewIp,_Aq:rbtwsApMgrChangeReason,_As:rbtwsClientClearedReason,_At:rbtwsMobilityDomainResiliencyStatus,_Ar:rbtwsClientSessionElapsedSeconds,_Au:rbtwsRadioChannelWidth,_Av:rbtwsRadioMimoState,_Aw:rbtwsClientRadioType,_A6:rbtwsRFDetectXmtrRadioType,_A7:rbtwsRFDetectXmtrCryptoType,_Ax:rbtwsClusterFailureReason,_Ay:rbtwsClusterFailureDescription,'rbtwsTrapMib':rbtwsTrapMib,'rbtwsTrapsV2':rbtwsTrapsV2,'rbtwsDeviceFailTrap':rbtwsDeviceFailTrap,'rbtwsDeviceOkayTrap':rbtwsDeviceOkayTrap,'rbtwsPoEFailTrap':rbtwsPoEFailTrap,'rbtwsApTimeoutTrap':rbtwsApTimeoutTrap,'rbtwsAPBootTrap':rbtwsAPBootTrap,'rbtwsMobilityDomainJoinTrap':rbtwsMobilityDomainJoinTrap,'rbtwsMobilityDomainTimeoutTrap':rbtwsMobilityDomainTimeoutTrap,'rbtwsMpMichaelMICFailure':rbtwsMpMichaelMICFailure,'rbtwsRFDetectRogueAPTrap':rbtwsRFDetectRogueAPTrap,'rbtwsRFDetectAdhocUserTrap':rbtwsRFDetectAdhocUserTrap,'rbtwsRFDetectRogueDisappearTrap':rbtwsRFDetectRogueDisappearTrap,'rbtwsClientAuthenticationFailureTrap':rbtwsClientAuthenticationFailureTrap,'rbtwsClientAuthorizationFailureTrap':rbtwsClientAuthorizationFailureTrap,'rbtwsClientAssociationFailureTrap':rbtwsClientAssociationFailureTrap,'rbtwsClientAuthorizationSuccessTrap':rbtwsClientAuthorizationSuccessTrap,'rbtwsClientDeAssociationTrap':rbtwsClientDeAssociationTrap,'rbtwsClientRoamingTrap':rbtwsClientRoamingTrap,'rbtwsAutoTuneRadioPowerChangeTrap':rbtwsAutoTuneRadioPowerChangeTrap,'rbtwsAutoTuneRadioChannelChangeTrap':rbtwsAutoTuneRadioChannelChangeTrap,'rbtwsCounterMeasureStartTrap':rbtwsCounterMeasureStartTrap,'rbtwsCounterMeasureStopTrap':rbtwsCounterMeasureStopTrap,'rbtwsClientDot1xFailureTrap':rbtwsClientDot1xFailureTrap,'rbtwsClientClearedTrap':rbtwsClientClearedTrap,'rbtwsClientAuthorizationSuccessTrap2':rbtwsClientAuthorizationSuccessTrap2,'rbtwsRFDetectSpoofedMacAPTrap':rbtwsRFDetectSpoofedMacAPTrap,'rbtwsRFDetectSpoofedSsidAPTrap':rbtwsRFDetectSpoofedSsidAPTrap,'rbtwsRFDetectDoSTrap':rbtwsRFDetectDoSTrap,'rbtwsRFDetectClientViaRogueWiredAPTrap':rbtwsRFDetectClientViaRogueWiredAPTrap,'rbtwsRFDetectInterferingRogueAPTrap':rbtwsRFDetectInterferingRogueAPTrap,'rbtwsRFDetectInterferingRogueDisappearTrap':rbtwsRFDetectInterferingRogueDisappearTrap,'rbtwsRFDetectUnAuthorizedSsidTrap':rbtwsRFDetectUnAuthorizedSsidTrap,'rbtwsRFDetectUnAuthorizedOuiTrap':rbtwsRFDetectUnAuthorizedOuiTrap,'rbtwsRFDetectUnAuthorizedAPTrap':rbtwsRFDetectUnAuthorizedAPTrap,'rbtwsDAPConnectWarningTrap':rbtwsDAPConnectWarningTrap,'rbtwsRFDetectDoSPortTrap':rbtwsRFDetectDoSPortTrap,'rbtwsMpMichaelMICFailure2':rbtwsMpMichaelMICFailure2,'rbtwsApNonOperStatusTrap':rbtwsApNonOperStatusTrap,'rbtwsApOperRadioStatusTrap':rbtwsApOperRadioStatusTrap,'rbtwsClientIpAddrChangeTrap':rbtwsClientIpAddrChangeTrap,'rbtwsClientAssociationSuccessTrap':rbtwsClientAssociationSuccessTrap,'rbtwsClientAuthenticationSuccessTrap':rbtwsClientAuthenticationSuccessTrap,'rbtwsClientDeAuthenticationTrap':rbtwsClientDeAuthenticationTrap,'rbtwsRFDetectBlacklistedTrap':rbtwsRFDetectBlacklistedTrap,'rbtwsRFDetectClientViaRogueWiredAPTrap2':rbtwsRFDetectClientViaRogueWiredAPTrap2,'rbtwsRFDetectAdhocUserDisappearTrap':rbtwsRFDetectAdhocUserDisappearTrap,'rbtwsApRejectLicenseExceededTrap':rbtwsApRejectLicenseExceededTrap,'rbtwsClientDynAuthorChangeSuccessTrap':rbtwsClientDynAuthorChangeSuccessTrap,'rbtwsClientDynAuthorChangeFailureTrap':rbtwsClientDynAuthorChangeFailureTrap,'rbtwsClientDisconnectTrap':rbtwsClientDisconnectTrap,'rbtwsMobilityDomainFailOverTrap':rbtwsMobilityDomainFailOverTrap,'rbtwsMobilityDomainFailBackTrap':rbtwsMobilityDomainFailBackTrap,'rbtwsRFDetectRogueDeviceTrap':rbtwsRFDetectRogueDeviceTrap,'rbtwsRFDetectRogueDeviceDisappearTrap':rbtwsRFDetectRogueDeviceDisappearTrap,'rbtwsRFDetectSuspectDeviceTrap':rbtwsRFDetectSuspectDeviceTrap,'rbtwsRFDetectSuspectDeviceDisappearTrap':rbtwsRFDetectSuspectDeviceDisappearTrap,'rbtwsRFDetectClientViaRogueWiredAPTrap3':rbtwsRFDetectClientViaRogueWiredAPTrap3,'rbtwsRFDetectClassificationChangeTrap':rbtwsRFDetectClassificationChangeTrap,'rbtwsConfigurationSavedTrap':rbtwsConfigurationSavedTrap,'rbtwsApNonOperStatusTrap2':rbtwsApNonOperStatusTrap2,'rbtwsApOperRadioStatusTrap2':rbtwsApOperRadioStatusTrap2,'rbtwsMichaelMICFailure':rbtwsMichaelMICFailure,'rbtwsClientAuthorizationSuccessTrap3':rbtwsClientAuthorizationSuccessTrap3,'rbtwsApManagerChangeTrap':rbtwsApManagerChangeTrap,'rbtwsClientClearedTrap2':rbtwsClientClearedTrap2,'rbtwsMobilityDomainResiliencyStatusTrap':rbtwsMobilityDomainResiliencyStatusTrap,'rbtwsApOperRadioStatusTrap3':rbtwsApOperRadioStatusTrap3,'rbtwsClientAuthorizationSuccessTrap4':rbtwsClientAuthorizationSuccessTrap4,'rbtwsRFDetectRogueDeviceTrap2':rbtwsRFDetectRogueDeviceTrap2,'rbtwsRFDetectSuspectDeviceTrap2':rbtwsRFDetectSuspectDeviceTrap2,'rbtwsClusterFailureTrap':rbtwsClusterFailureTrap})