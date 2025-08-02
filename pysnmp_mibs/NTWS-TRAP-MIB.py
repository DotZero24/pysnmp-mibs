_Ay='ntwsClusterFailureDescription'
_Ax='ntwsClusterFailureReason'
_Aw='ntwsClientRadioType'
_Av='ntwsRadioMimoState'
_Au='ntwsRadioChannelWidth'
_At='ntwsMobilityDomainResiliencyStatus'
_As='ntwsClientClearedReason'
_Ar='ntwsClientSessionElapsedSeconds'
_Aq='ntwsApMgrChangeReason'
_Ap='ntwsApMgrNewIp'
_Ao='ntwsApMgrOldIp'
_An='ntwsMichaelMICFailureCause'
_Am='ntwsConfigSaveGeneration'
_Al='ntwsConfigSaveInitiatorDetails'
_Ak='ntwsConfigSaveInitiatorIp'
_Aj='ntwsConfigSaveInitiatorType'
_Ai='ntwsConfigSaveFileName'
_Ah='ntwsMobilityDomainPrimarySeedIp'
_Ag='ntwsMobilityDomainSecondarySeedIp'
_Af='ntwsClientDisconnectDescription'
_Ae='ntwsClientDisconnectSource'
_Ad='ntwsChangedUserParamNewValues'
_Ac='ntwsChangedUserParamOldValues'
_Ab='ntwsNumLicensedActiveAPs'
_Aa='ntwsBlacklistingCause'
_AZ='ntwsBlacklistingRemainingTime'
_AY='ntwsClientIpAddrChangeReason'
_AX='ntwsDAPconnectWarningType'
_AW='ntwsRsaPubKeyFingerPrint'
_AV='ntwsDeviceModel'
_AU='ntwsClientSessionElapsedTime'
_AT='ntwsClientDot1xFailureCause'
_AS='ntwsClientDot1xState'
_AR='ntwsChannelChangeReason'
_AQ='ntwsOldChannelNum'
_AP='ntwsNewChannelNum'
_AO='ntwsRadioPowerChangeDescription'
_AN='ntwsRadioPowerChangeReason'
_AM='ntwsOldPowerLevel'
_AL='ntwsNewPowerLevel'
_AK='ntwsClientTimeSinceLastRoam'
_AJ='ntwsClientRoamedFromWsIp'
_AI='ntwsClientRoamedFromDAPNum'
_AH='ntwsClientRoamedFromRadioNum'
_AG='ntwsClientRoamedFromPortNum'
_AF='ntwsClientRoamedFromAccessType'
_AE='ntwsRadioRssi'
_AD='ntwsClientAssociationFailureCause'
_AC='ntwsClientLocationPolicyIndex'
_AB='ntwsClientAuthenticationFailureCause'
_AA='user-glob-mismatch'
_A9='quiet-period'
_A8='Unsigned32'
_A7='ntwsRFDetectXmtrCryptoType'
_A6='ntwsRFDetectXmtrRadioType'
_A5='ntwsClientAuthorizationReason'
_A4='ntwsRadioMode'
_A3='ntwsClientDynAuthorClientIp'
_A2='ntwsRFDetectRogueAPMacAddr'
_A1='ntwsApWasOperational'
_A0='ntwsApFailDetail'
_z='ntwsApTransition'
_y='ntwsApPortOrDapNum'
_x='ntwsApAttachType'
_w='ntwsClientMACAddress2'
_v='ntwsRFDetectDoSType'
_u='ntwsClientSessionStartTime'
_t='ntwsClientAuthorizationFailureCause'
_s='ntwsUserParams'
_r='ntwsMobilityDomainIp'
_q='ntwsAPAccessType'
_p='ntwsDeviceId'
_o='OctetString'
_n='ntwsPhysPortNum'
_m='ntwsClientAccessMode'
_l='ntwsApServiceAvailability'
_k='ntwsApConnectSecurityType'
_j='ntwsRadioConfigState'
_i='ntwsRadioType'
_h='ntwsClientVLANtag'
_g='ntwsClientVLANid'
_f='ntwsSourceWsIp'
_e='ntwsRFDetectClassificationReason'
_d='ntwsUserAccessType'
_c='ntwsClientFailureCauseDescription'
_b='ntwsAPMACAddress'
_a='ntwsApName'
_Z='ntwsClientSessionState'
_Y='ntwsDeviceSerNum'
_X='ntwsClientVLANName'
_W='ntwsApNum'
_V='ntwsLocalId'
_U='ntwsClientAuthServerIp'
_T='ntwsRadioMACAddress'
_S='other'
_R='ntwsClientIp'
_Q='ntwsClientAuthenProtocolType'
_P='Integer32'
_O='DisplayString'
_N='ntwsClientSessionId'
_M='ntwsUserName'
_L='ntwsRFDetectListenerListInfo'
_K='ntwsClientAccessType'
_J='ntwsRadioSSID'
_I='ntwsDAPNum'
_H='ntwsClientMACAddress'
_G='ntwsRFDetectXmtrMacAddr'
_F='ntwsAPRadioNum'
_E='ntwsPortNum'
_D='obsolete'
_C='accessible-for-notify'
_B='current'
_A='NTWS-TRAP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_o,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
NtwsAccessType,NtwsApAttachType,NtwsApConnectSecurityType,NtwsApFailDetail,NtwsApFingerprint,NtwsApNum,NtwsApPortOrDapNum,NtwsApSerialNum,NtwsApServiceAvailability,NtwsApTransition,NtwsApWasOperational,NtwsChannelChangeType,NtwsCryptoType,NtwsPowerLevel,NtwsRadioChannelWidth,NtwsRadioConfigState,NtwsRadioMimoState,NtwsRadioMode,NtwsRadioNum,NtwsRadioPowerChangeType,NtwsRadioType=mibBuilder.importSymbols('NTWS-AP-TC','NtwsAccessType','NtwsApAttachType','NtwsApConnectSecurityType','NtwsApFailDetail','NtwsApFingerprint','NtwsApNum','NtwsApPortOrDapNum','NtwsApSerialNum','NtwsApServiceAvailability','NtwsApTransition','NtwsApWasOperational','NtwsChannelChangeType','NtwsCryptoType','NtwsPowerLevel','NtwsRadioChannelWidth','NtwsRadioConfigState','NtwsRadioMimoState','NtwsRadioMode','NtwsRadioNum','NtwsRadioPowerChangeType','NtwsRadioType')
NtwsClientAccessMode,NtwsClientAuthenProtocolType,NtwsClientDot1xState,NtwsClientSessionState,NtwsUserAccessType=mibBuilder.importSymbols('NTWS-CLIENT-SESSION-TC','NtwsClientAccessMode','NtwsClientAuthenProtocolType','NtwsClientDot1xState','NtwsClientSessionState','NtwsUserAccessType')
NtwsRFDetectClassificationReason,=mibBuilder.importSymbols('NTWS-RF-DETECT-TC','NtwsRFDetectClassificationReason')
ntwsMibs,ntwsTemporary,ntwsTraps=mibBuilder.importSymbols('NTWS-ROOT-MIB','ntwsMibs','ntwsTemporary','ntwsTraps')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_P,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_A8,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_O,'MacAddress','PhysAddress','TextualConvention')
ntwsTrapMib=ModuleIdentity((1,3,6,1,4,1,45,6,1,4,1))
if mibBuilder.loadTexts:ntwsTrapMib.setRevisions(('2008-05-15 02:15','2008-05-07 02:12','2008-04-22 02:02','2008-04-10 02:01','2008-04-08 01:58','2008-02-18 01:57','2007-12-03 01:53','2007-11-15 01:52','2007-11-01 01:45','2007-10-01 01:41','2007-08-31 01:40','2007-08-31 01:30','2007-08-24 01:22','2007-07-06 01:10','2007-06-05 01:07','2007-05-17 01:06','2007-05-04 01:03','2007-04-19 01:00','2007-03-27 00:54','2007-02-15 00:53','2007-01-09 00:52','2007-01-09 00:51','2007-01-09 00:50','2006-09-28 00:45','2006-08-08 00:42','2006-07-31 00:40','2006-07-28 00:32','2006-07-23 00:29','2006-07-12 00:28','2006-07-07 00:26','2006-07-07 00:25','2006-07-06 00:23','2006-04-19 00:22','2006-04-19 00:21','2005-01-01 00:00'))
class NtwsAssociationFailureType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_S,1),('load-balance',2),(_A9,3),('dot1x',4),('no-prev-assoc',5),('glare',6),('cipher-rejected',7),('cipher-mismatch',8),('wep-not-configured',9),('bad-assoc-request',10),('out-of-memory',11),('tkip-cm-active',12),('roam-in-progress',13)))
class NtwsAuthenticationFailureType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_S,1),(_AA,2),('user-does-not-exist',3),('invalid-password',4),('server-timeout',5),('signature-failed',6),('local-certificate-error',7),('all-servers-down',8),('authentication-type-mismatch',9),('server-rejected',10),('fallthru-auth-misconfig',11),('no-lastresort-auth',12),('exceeded-max-attempts',13),('password-expired',14)))
class NtwsAuthorizationFailureType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_S,1),('user-param',2),('location-policy',3),('vlan-tunnel-failure',4),('ssid-mismatch',5),('acl-mismatch',6),('timeofday-mismatch',7),('crypto-type-mismatch',8),('mobility-profile-mismatch',9),('start-date-mismatch',10),('end-date-mismatch',11),('svr-type-mismatch',12),('ssid-defaults',13),('qos-profile-mismatch',14),('simultaneous-logins',15)))
class NtwsDot1xFailureType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_S,1),(_A9,2),('administrative-kill',3),('bad-rsnie',4),('timeout',5),('max-sessions-exceeded',6),('fourway-hs-failure',7),(_AA,8),('bonded-auth-failure',9),('reauth-disabled',10),('gkhs-failure',11),('force-unauth-configured',12),('cert-not-installed',13)))
class NtwsRFDetectDoSType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*(('probe-flood',1),('auth-flood',2),('null-data-flood',3),('mgmt-6-flood',4),('mgmt-7-flood',5),('mgmt-d-flood',6),('mgmt-e-flood',7),('mgmt-f-flood',8),('fakeap-ssid',9),('fakeap-bssid',10),('bcast-deauth',11),('null-probe-resp',12),('disassoc-spoof',13),('deauth-spoof',14),('decrypt-err',15),('weak-wep-iv',16),('wireless-bridge',17),('netstumbler',18),('wellenreiter',19),('adhoc-client-frame',20),('associate-pkt-flood',21),('re-associate-pkt-flood',22),('de-associate-pkt-flood',23),('bssid-spoof',24)))
class NtwsClientIpAddrChangeReason(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('client-connected',1),(_S,2),('dhcp-to-static',3)))
class NtwsBlacklistingCause(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('bl-configured',1),('bl-associate-pkt-flood',2),('bl-re-associate-pkt-flood',3),('bl-de-associate-pkt-flood',4)))
class NtwsUserAttributeList(DisplayString):status=_B;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2048))
class NtwsSessionDisconnectType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('admin-disconnect',2),('dyn-auth-disconnect',3)))
class NtwsConfigSaveInitiatorType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_S,1),('cli-console',2),('cli-remote',3),('https',4),('snmp-set',5)))
class NtwsMichaelMICFailureCause(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('detected-by-ap',1),('detected-by-client',2)))
class NtwsClientAuthorizationReason(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),('new-client',2),('re-auth',3),('roam',4)))
class NtwsApMgrChangeReason(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('failover',2),('load-balancing',3)))
class NtwsClientClearedReason(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('normal',2),('backup-failure',3)))
class NtwsMobilityDomainResiliencyStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('resilient',2),('degraded',3)))
class NtwsClusterFailureReason(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),('validation-error',2)))
_NtwsDeviceId_Type=ObjectIdentifier
_NtwsDeviceId_Object=MibScalar
ntwsDeviceId=_NtwsDeviceId_Object((1,3,6,1,4,1,45,6,1,2,1),_NtwsDeviceId_Type())
ntwsDeviceId.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsDeviceId.setStatus(_B)
_NtwsMobilityDomainIp_Type=IpAddress
_NtwsMobilityDomainIp_Object=MibScalar
ntwsMobilityDomainIp=_NtwsMobilityDomainIp_Object((1,3,6,1,4,1,45,6,1,2,2),_NtwsMobilityDomainIp_Type())
ntwsMobilityDomainIp.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsMobilityDomainIp.setStatus(_B)
_NtwsAPMACAddress_Type=MacAddress
_NtwsAPMACAddress_Object=MibScalar
ntwsAPMACAddress=_NtwsAPMACAddress_Object((1,3,6,1,4,1,45,6,1,2,3),_NtwsAPMACAddress_Type())
ntwsAPMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsAPMACAddress.setStatus(_B)
_NtwsClientMACAddress_Type=MacAddress
_NtwsClientMACAddress_Object=MibScalar
ntwsClientMACAddress=_NtwsClientMACAddress_Object((1,3,6,1,4,1,45,6,1,2,4),_NtwsClientMACAddress_Type())
ntwsClientMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientMACAddress.setStatus(_B)
_NtwsRFDetectXmtrMacAddr_Type=MacAddress
_NtwsRFDetectXmtrMacAddr_Object=MibScalar
ntwsRFDetectXmtrMacAddr=_NtwsRFDetectXmtrMacAddr_Object((1,3,6,1,4,1,45,6,1,2,5),_NtwsRFDetectXmtrMacAddr_Type())
ntwsRFDetectXmtrMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsRFDetectXmtrMacAddr.setStatus(_B)
class _NtwsPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,22))
_NtwsPortNum_Type.__name__=_P
_NtwsPortNum_Object=MibScalar
ntwsPortNum=_NtwsPortNum_Object((1,3,6,1,4,1,45,6,1,2,6),_NtwsPortNum_Type())
ntwsPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsPortNum.setStatus(_B)
_NtwsAPRadioNum_Type=NtwsRadioNum
_NtwsAPRadioNum_Object=MibScalar
ntwsAPRadioNum=_NtwsAPRadioNum_Object((1,3,6,1,4,1,45,6,1,2,7),_NtwsAPRadioNum_Type())
ntwsAPRadioNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsAPRadioNum.setStatus(_B)
class _NtwsRadioRssi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_NtwsRadioRssi_Type.__name__=_P
_NtwsRadioRssi_Object=MibScalar
ntwsRadioRssi=_NtwsRadioRssi_Object((1,3,6,1,4,1,45,6,1,2,8),_NtwsRadioRssi_Type())
ntwsRadioRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsRadioRssi.setStatus(_D)
class _NtwsRadioBSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_NtwsRadioBSSID_Type.__name__=_o
_NtwsRadioBSSID_Object=MibScalar
ntwsRadioBSSID=_NtwsRadioBSSID_Object((1,3,6,1,4,1,45,6,1,2,9),_NtwsRadioBSSID_Type())
ntwsRadioBSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsRadioBSSID.setStatus(_B)
class _NtwsUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtwsUserName_Type.__name__=_O
_NtwsUserName_Object=MibScalar
ntwsUserName=_NtwsUserName_Object((1,3,6,1,4,1,45,6,1,2,10),_NtwsUserName_Type())
ntwsUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsUserName.setStatus(_B)
_NtwsClientAuthServerIp_Type=IpAddress
_NtwsClientAuthServerIp_Object=MibScalar
ntwsClientAuthServerIp=_NtwsClientAuthServerIp_Object((1,3,6,1,4,1,45,6,1,2,11),_NtwsClientAuthServerIp_Type())
ntwsClientAuthServerIp.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientAuthServerIp.setStatus(_B)
_NtwsClientSessionState_Type=NtwsClientSessionState
_NtwsClientSessionState_Object=MibScalar
ntwsClientSessionState=_NtwsClientSessionState_Object((1,3,6,1,4,1,45,6,1,2,12),_NtwsClientSessionState_Type())
ntwsClientSessionState.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientSessionState.setStatus(_B)
class _NtwsDAPNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_NtwsDAPNum_Type.__name__=_P
_NtwsDAPNum_Object=MibScalar
ntwsDAPNum=_NtwsDAPNum_Object((1,3,6,1,4,1,45,6,1,2,13),_NtwsDAPNum_Type())
ntwsDAPNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsDAPNum.setStatus(_B)
_NtwsClientIp_Type=IpAddress
_NtwsClientIp_Object=MibScalar
ntwsClientIp=_NtwsClientIp_Object((1,3,6,1,4,1,45,6,1,2,14),_NtwsClientIp_Type())
ntwsClientIp.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientIp.setStatus(_B)
class _NtwsClientSessionId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtwsClientSessionId_Type.__name__=_O
_NtwsClientSessionId_Object=MibScalar
ntwsClientSessionId=_NtwsClientSessionId_Object((1,3,6,1,4,1,45,6,1,2,15),_NtwsClientSessionId_Type())
ntwsClientSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientSessionId.setStatus(_B)
_NtwsClientAuthenProtocolType_Type=NtwsClientAuthenProtocolType
_NtwsClientAuthenProtocolType_Object=MibScalar
ntwsClientAuthenProtocolType=_NtwsClientAuthenProtocolType_Object((1,3,6,1,4,1,45,6,1,2,16),_NtwsClientAuthenProtocolType_Type())
ntwsClientAuthenProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientAuthenProtocolType.setStatus(_B)
class _NtwsClientVLANName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtwsClientVLANName_Type.__name__=_O
_NtwsClientVLANName_Object=MibScalar
ntwsClientVLANName=_NtwsClientVLANName_Object((1,3,6,1,4,1,45,6,1,2,17),_NtwsClientVLANName_Type())
ntwsClientVLANName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientVLANName.setStatus(_B)
_NtwsClientSessionStartTime_Type=TimeTicks
_NtwsClientSessionStartTime_Object=MibScalar
ntwsClientSessionStartTime=_NtwsClientSessionStartTime_Object((1,3,6,1,4,1,45,6,1,2,18),_NtwsClientSessionStartTime_Type())
ntwsClientSessionStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientSessionStartTime.setStatus(_D)
class _NtwsClientFailureCause_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtwsClientFailureCause_Type.__name__=_O
_NtwsClientFailureCause_Object=MibScalar
ntwsClientFailureCause=_NtwsClientFailureCause_Object((1,3,6,1,4,1,45,6,1,2,19),_NtwsClientFailureCause_Type())
ntwsClientFailureCause.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientFailureCause.setStatus(_B)
class _NtwsClientRoamedFromPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_NtwsClientRoamedFromPortNum_Type.__name__=_P
_NtwsClientRoamedFromPortNum_Object=MibScalar
ntwsClientRoamedFromPortNum=_NtwsClientRoamedFromPortNum_Object((1,3,6,1,4,1,45,6,1,2,20),_NtwsClientRoamedFromPortNum_Type())
ntwsClientRoamedFromPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientRoamedFromPortNum.setStatus(_B)
_NtwsClientRoamedFromRadioNum_Type=NtwsRadioNum
_NtwsClientRoamedFromRadioNum_Object=MibScalar
ntwsClientRoamedFromRadioNum=_NtwsClientRoamedFromRadioNum_Object((1,3,6,1,4,1,45,6,1,2,21),_NtwsClientRoamedFromRadioNum_Type())
ntwsClientRoamedFromRadioNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientRoamedFromRadioNum.setStatus(_B)
class _NtwsClientRoamedFromDAPNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_NtwsClientRoamedFromDAPNum_Type.__name__=_P
_NtwsClientRoamedFromDAPNum_Object=MibScalar
ntwsClientRoamedFromDAPNum=_NtwsClientRoamedFromDAPNum_Object((1,3,6,1,4,1,45,6,1,2,22),_NtwsClientRoamedFromDAPNum_Type())
ntwsClientRoamedFromDAPNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientRoamedFromDAPNum.setStatus(_B)
class _NtwsUserParams_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtwsUserParams_Type.__name__=_O
_NtwsUserParams_Object=MibScalar
ntwsUserParams=_NtwsUserParams_Object((1,3,6,1,4,1,45,6,1,2,23),_NtwsUserParams_Type())
ntwsUserParams.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsUserParams.setStatus(_B)
class _NtwsClientLocationPolicyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_NtwsClientLocationPolicyIndex_Type.__name__=_P
_NtwsClientLocationPolicyIndex_Object=MibScalar
ntwsClientLocationPolicyIndex=_NtwsClientLocationPolicyIndex_Object((1,3,6,1,4,1,45,6,1,2,24),_NtwsClientLocationPolicyIndex_Type())
ntwsClientLocationPolicyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientLocationPolicyIndex.setStatus(_B)
_NtwsClientAssociationFailureCause_Type=NtwsAssociationFailureType
_NtwsClientAssociationFailureCause_Object=MibScalar
ntwsClientAssociationFailureCause=_NtwsClientAssociationFailureCause_Object((1,3,6,1,4,1,45,6,1,2,25),_NtwsClientAssociationFailureCause_Type())
ntwsClientAssociationFailureCause.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientAssociationFailureCause.setStatus(_B)
_NtwsClientAuthenticationFailureCause_Type=NtwsAuthenticationFailureType
_NtwsClientAuthenticationFailureCause_Object=MibScalar
ntwsClientAuthenticationFailureCause=_NtwsClientAuthenticationFailureCause_Object((1,3,6,1,4,1,45,6,1,2,26),_NtwsClientAuthenticationFailureCause_Type())
ntwsClientAuthenticationFailureCause.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientAuthenticationFailureCause.setStatus(_B)
_NtwsClientAuthorizationFailureCause_Type=NtwsAuthorizationFailureType
_NtwsClientAuthorizationFailureCause_Object=MibScalar
ntwsClientAuthorizationFailureCause=_NtwsClientAuthorizationFailureCause_Object((1,3,6,1,4,1,45,6,1,2,27),_NtwsClientAuthorizationFailureCause_Type())
ntwsClientAuthorizationFailureCause.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientAuthorizationFailureCause.setStatus(_B)
class _NtwsClientFailureCauseDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtwsClientFailureCauseDescription_Type.__name__=_O
_NtwsClientFailureCauseDescription_Object=MibScalar
ntwsClientFailureCauseDescription=_NtwsClientFailureCauseDescription_Object((1,3,6,1,4,1,45,6,1,2,28),_NtwsClientFailureCauseDescription_Type())
ntwsClientFailureCauseDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientFailureCauseDescription.setStatus(_B)
_NtwsClientRoamedFromWsIp_Type=IpAddress
_NtwsClientRoamedFromWsIp_Object=MibScalar
ntwsClientRoamedFromWsIp=_NtwsClientRoamedFromWsIp_Object((1,3,6,1,4,1,45,6,1,2,29),_NtwsClientRoamedFromWsIp_Type())
ntwsClientRoamedFromWsIp.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientRoamedFromWsIp.setStatus(_B)
_NtwsClientRoamedFromAccessType_Type=NtwsAccessType
_NtwsClientRoamedFromAccessType_Object=MibScalar
ntwsClientRoamedFromAccessType=_NtwsClientRoamedFromAccessType_Object((1,3,6,1,4,1,45,6,1,2,30),_NtwsClientRoamedFromAccessType_Type())
ntwsClientRoamedFromAccessType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientRoamedFromAccessType.setStatus(_B)
_NtwsClientAccessType_Type=NtwsAccessType
_NtwsClientAccessType_Object=MibScalar
ntwsClientAccessType=_NtwsClientAccessType_Object((1,3,6,1,4,1,45,6,1,2,31),_NtwsClientAccessType_Type())
ntwsClientAccessType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientAccessType.setStatus(_B)
_NtwsRadioMACAddress_Type=MacAddress
_NtwsRadioMACAddress_Object=MibScalar
ntwsRadioMACAddress=_NtwsRadioMACAddress_Object((1,3,6,1,4,1,45,6,1,2,32),_NtwsRadioMACAddress_Type())
ntwsRadioMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsRadioMACAddress.setStatus(_B)
_NtwsRadioPowerChangeReason_Type=NtwsRadioPowerChangeType
_NtwsRadioPowerChangeReason_Object=MibScalar
ntwsRadioPowerChangeReason=_NtwsRadioPowerChangeReason_Object((1,3,6,1,4,1,45,6,1,2,33),_NtwsRadioPowerChangeReason_Type())
ntwsRadioPowerChangeReason.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsRadioPowerChangeReason.setStatus(_B)
class _NtwsNewChannelNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_NtwsNewChannelNum_Type.__name__=_P
_NtwsNewChannelNum_Object=MibScalar
ntwsNewChannelNum=_NtwsNewChannelNum_Object((1,3,6,1,4,1,45,6,1,2,34),_NtwsNewChannelNum_Type())
ntwsNewChannelNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsNewChannelNum.setStatus(_B)
class _NtwsOldChannelNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_NtwsOldChannelNum_Type.__name__=_P
_NtwsOldChannelNum_Object=MibScalar
ntwsOldChannelNum=_NtwsOldChannelNum_Object((1,3,6,1,4,1,45,6,1,2,35),_NtwsOldChannelNum_Type())
ntwsOldChannelNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsOldChannelNum.setStatus(_B)
_NtwsChannelChangeReason_Type=NtwsChannelChangeType
_NtwsChannelChangeReason_Object=MibScalar
ntwsChannelChangeReason=_NtwsChannelChangeReason_Object((1,3,6,1,4,1,45,6,1,2,36),_NtwsChannelChangeReason_Type())
ntwsChannelChangeReason.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsChannelChangeReason.setStatus(_B)
class _NtwsRFDetectListenerListInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,571))
_NtwsRFDetectListenerListInfo_Type.__name__=_o
_NtwsRFDetectListenerListInfo_Object=MibScalar
ntwsRFDetectListenerListInfo=_NtwsRFDetectListenerListInfo_Object((1,3,6,1,4,1,45,6,1,2,37),_NtwsRFDetectListenerListInfo_Type())
ntwsRFDetectListenerListInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsRFDetectListenerListInfo.setStatus(_B)
class _NtwsRadioSSID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtwsRadioSSID_Type.__name__=_O
_NtwsRadioSSID_Object=MibScalar
ntwsRadioSSID=_NtwsRadioSSID_Object((1,3,6,1,4,1,45,6,1,2,38),_NtwsRadioSSID_Type())
ntwsRadioSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsRadioSSID.setStatus(_B)
_NtwsNewPowerLevel_Type=NtwsPowerLevel
_NtwsNewPowerLevel_Object=MibScalar
ntwsNewPowerLevel=_NtwsNewPowerLevel_Object((1,3,6,1,4,1,45,6,1,2,39),_NtwsNewPowerLevel_Type())
ntwsNewPowerLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsNewPowerLevel.setStatus(_B)
_NtwsOldPowerLevel_Type=NtwsPowerLevel
_NtwsOldPowerLevel_Object=MibScalar
ntwsOldPowerLevel=_NtwsOldPowerLevel_Object((1,3,6,1,4,1,45,6,1,2,40),_NtwsOldPowerLevel_Type())
ntwsOldPowerLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsOldPowerLevel.setStatus(_B)
class _NtwsRadioPowerChangeDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtwsRadioPowerChangeDescription_Type.__name__=_O
_NtwsRadioPowerChangeDescription_Object=MibScalar
ntwsRadioPowerChangeDescription=_NtwsRadioPowerChangeDescription_Object((1,3,6,1,4,1,45,6,1,2,41),_NtwsRadioPowerChangeDescription_Type())
ntwsRadioPowerChangeDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsRadioPowerChangeDescription.setStatus(_B)
class _NtwsCounterMeasurePerformerListInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtwsCounterMeasurePerformerListInfo_Type.__name__=_O
_NtwsCounterMeasurePerformerListInfo_Object=MibScalar
ntwsCounterMeasurePerformerListInfo=_NtwsCounterMeasurePerformerListInfo_Object((1,3,6,1,4,1,45,6,1,2,42),_NtwsCounterMeasurePerformerListInfo_Type())
ntwsCounterMeasurePerformerListInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsCounterMeasurePerformerListInfo.setStatus(_D)
_NtwsClientDot1xState_Type=NtwsClientDot1xState
_NtwsClientDot1xState_Object=MibScalar
ntwsClientDot1xState=_NtwsClientDot1xState_Object((1,3,6,1,4,1,45,6,1,2,43),_NtwsClientDot1xState_Type())
ntwsClientDot1xState.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientDot1xState.setStatus(_B)
_NtwsClientDot1xFailureCause_Type=NtwsDot1xFailureType
_NtwsClientDot1xFailureCause_Object=MibScalar
ntwsClientDot1xFailureCause=_NtwsClientDot1xFailureCause_Object((1,3,6,1,4,1,45,6,1,2,44),_NtwsClientDot1xFailureCause_Type())
ntwsClientDot1xFailureCause.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientDot1xFailureCause.setStatus(_B)
_NtwsAPAccessType_Type=NtwsAccessType
_NtwsAPAccessType_Object=MibScalar
ntwsAPAccessType=_NtwsAPAccessType_Object((1,3,6,1,4,1,45,6,1,2,45),_NtwsAPAccessType_Type())
ntwsAPAccessType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsAPAccessType.setStatus(_D)
_NtwsUserAccessType_Type=NtwsUserAccessType
_NtwsUserAccessType_Object=MibScalar
ntwsUserAccessType=_NtwsUserAccessType_Object((1,3,6,1,4,1,45,6,1,2,46),_NtwsUserAccessType_Type())
ntwsUserAccessType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsUserAccessType.setStatus(_B)
_NtwsClientSessionElapsedTime_Type=TimeTicks
_NtwsClientSessionElapsedTime_Object=MibScalar
ntwsClientSessionElapsedTime=_NtwsClientSessionElapsedTime_Object((1,3,6,1,4,1,45,6,1,2,47),_NtwsClientSessionElapsedTime_Type())
ntwsClientSessionElapsedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientSessionElapsedTime.setStatus(_D)
class _NtwsLocalId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65000))
_NtwsLocalId_Type.__name__=_P
_NtwsLocalId_Object=MibScalar
ntwsLocalId=_NtwsLocalId_Object((1,3,6,1,4,1,45,6,1,2,48),_NtwsLocalId_Type())
ntwsLocalId.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsLocalId.setStatus(_B)
_NtwsRFDetectDoSType_Type=NtwsRFDetectDoSType
_NtwsRFDetectDoSType_Object=MibScalar
ntwsRFDetectDoSType=_NtwsRFDetectDoSType_Object((1,3,6,1,4,1,45,6,1,2,49),_NtwsRFDetectDoSType_Type())
ntwsRFDetectDoSType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsRFDetectDoSType.setStatus(_B)
_NtwsSourceWsIp_Type=IpAddress
_NtwsSourceWsIp_Object=MibScalar
ntwsSourceWsIp=_NtwsSourceWsIp_Object((1,3,6,1,4,1,45,6,1,2,50),_NtwsSourceWsIp_Type())
ntwsSourceWsIp.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsSourceWsIp.setStatus(_B)
class _NtwsClientVLANid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_NtwsClientVLANid_Type.__name__=_P
_NtwsClientVLANid_Object=MibScalar
ntwsClientVLANid=_NtwsClientVLANid_Object((1,3,6,1,4,1,45,6,1,2,51),_NtwsClientVLANid_Type())
ntwsClientVLANid.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientVLANid.setStatus(_B)
class _NtwsClientVLANtag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_NtwsClientVLANtag_Type.__name__=_P
_NtwsClientVLANtag_Object=MibScalar
ntwsClientVLANtag=_NtwsClientVLANtag_Object((1,3,6,1,4,1,45,6,1,2,52),_NtwsClientVLANtag_Type())
ntwsClientVLANtag.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientVLANtag.setStatus(_B)
_NtwsDeviceModel_Type=DisplayString
_NtwsDeviceModel_Object=MibScalar
ntwsDeviceModel=_NtwsDeviceModel_Object((1,3,6,1,4,1,45,6,1,2,53),_NtwsDeviceModel_Type())
ntwsDeviceModel.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsDeviceModel.setStatus(_B)
_NtwsDeviceSerNum_Type=NtwsApSerialNum
_NtwsDeviceSerNum_Object=MibScalar
ntwsDeviceSerNum=_NtwsDeviceSerNum_Object((1,3,6,1,4,1,45,6,1,2,54),_NtwsDeviceSerNum_Type())
ntwsDeviceSerNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsDeviceSerNum.setStatus(_B)
_NtwsRsaPubKeyFingerPrint_Type=NtwsApFingerprint
_NtwsRsaPubKeyFingerPrint_Object=MibScalar
ntwsRsaPubKeyFingerPrint=_NtwsRsaPubKeyFingerPrint_Object((1,3,6,1,4,1,45,6,1,2,55),_NtwsRsaPubKeyFingerPrint_Type())
ntwsRsaPubKeyFingerPrint.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsRsaPubKeyFingerPrint.setStatus(_B)
class _NtwsDAPconnectWarningType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('not-configured-fingerprint-connect',1),('secure-handshake-failure',2),('not-configured-fingerprint-required',3),('fingerprint-mismatch',4)))
_NtwsDAPconnectWarningType_Type.__name__=_P
_NtwsDAPconnectWarningType_Object=MibScalar
ntwsDAPconnectWarningType=_NtwsDAPconnectWarningType_Object((1,3,6,1,4,1,45,6,1,2,56),_NtwsDAPconnectWarningType_Type())
ntwsDAPconnectWarningType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsDAPconnectWarningType.setStatus(_B)
_NtwsClientMACAddress2_Type=MacAddress
_NtwsClientMACAddress2_Object=MibScalar
ntwsClientMACAddress2=_NtwsClientMACAddress2_Object((1,3,6,1,4,1,45,6,1,2,57),_NtwsClientMACAddress2_Type())
ntwsClientMACAddress2.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientMACAddress2.setStatus(_B)
_NtwsApAttachType_Type=NtwsApAttachType
_NtwsApAttachType_Object=MibScalar
ntwsApAttachType=_NtwsApAttachType_Object((1,3,6,1,4,1,45,6,1,2,58),_NtwsApAttachType_Type())
ntwsApAttachType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsApAttachType.setStatus(_B)
_NtwsApPortOrDapNum_Type=NtwsApPortOrDapNum
_NtwsApPortOrDapNum_Object=MibScalar
ntwsApPortOrDapNum=_NtwsApPortOrDapNum_Object((1,3,6,1,4,1,45,6,1,2,59),_NtwsApPortOrDapNum_Type())
ntwsApPortOrDapNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsApPortOrDapNum.setStatus(_D)
_NtwsApName_Type=DisplayString
_NtwsApName_Object=MibScalar
ntwsApName=_NtwsApName_Object((1,3,6,1,4,1,45,6,1,2,60),_NtwsApName_Type())
ntwsApName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsApName.setStatus(_B)
_NtwsApTransition_Type=NtwsApTransition
_NtwsApTransition_Object=MibScalar
ntwsApTransition=_NtwsApTransition_Object((1,3,6,1,4,1,45,6,1,2,61),_NtwsApTransition_Type())
ntwsApTransition.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsApTransition.setStatus(_B)
_NtwsApFailDetail_Type=NtwsApFailDetail
_NtwsApFailDetail_Object=MibScalar
ntwsApFailDetail=_NtwsApFailDetail_Object((1,3,6,1,4,1,45,6,1,2,62),_NtwsApFailDetail_Type())
ntwsApFailDetail.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsApFailDetail.setStatus(_B)
_NtwsRadioType_Type=NtwsRadioType
_NtwsRadioType_Object=MibScalar
ntwsRadioType=_NtwsRadioType_Object((1,3,6,1,4,1,45,6,1,2,63),_NtwsRadioType_Type())
ntwsRadioType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsRadioType.setStatus(_B)
_NtwsRadioConfigState_Type=NtwsRadioConfigState
_NtwsRadioConfigState_Object=MibScalar
ntwsRadioConfigState=_NtwsRadioConfigState_Object((1,3,6,1,4,1,45,6,1,2,64),_NtwsRadioConfigState_Type())
ntwsRadioConfigState.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsRadioConfigState.setStatus(_B)
_NtwsApConnectSecurityType_Type=NtwsApConnectSecurityType
_NtwsApConnectSecurityType_Object=MibScalar
ntwsApConnectSecurityType=_NtwsApConnectSecurityType_Object((1,3,6,1,4,1,45,6,1,2,65),_NtwsApConnectSecurityType_Type())
ntwsApConnectSecurityType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsApConnectSecurityType.setStatus(_B)
_NtwsApServiceAvailability_Type=NtwsApServiceAvailability
_NtwsApServiceAvailability_Object=MibScalar
ntwsApServiceAvailability=_NtwsApServiceAvailability_Object((1,3,6,1,4,1,45,6,1,2,66),_NtwsApServiceAvailability_Type())
ntwsApServiceAvailability.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsApServiceAvailability.setStatus(_B)
_NtwsApWasOperational_Type=NtwsApWasOperational
_NtwsApWasOperational_Object=MibScalar
ntwsApWasOperational=_NtwsApWasOperational_Object((1,3,6,1,4,1,45,6,1,2,67),_NtwsApWasOperational_Type())
ntwsApWasOperational.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsApWasOperational.setStatus(_B)
_NtwsClientTimeSinceLastRoam_Type=Unsigned32
_NtwsClientTimeSinceLastRoam_Object=MibScalar
ntwsClientTimeSinceLastRoam=_NtwsClientTimeSinceLastRoam_Object((1,3,6,1,4,1,45,6,1,2,68),_NtwsClientTimeSinceLastRoam_Type())
ntwsClientTimeSinceLastRoam.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientTimeSinceLastRoam.setStatus(_B)
_NtwsClientIpAddrChangeReason_Type=NtwsClientIpAddrChangeReason
_NtwsClientIpAddrChangeReason_Object=MibScalar
ntwsClientIpAddrChangeReason=_NtwsClientIpAddrChangeReason_Object((1,3,6,1,4,1,45,6,1,2,69),_NtwsClientIpAddrChangeReason_Type())
ntwsClientIpAddrChangeReason.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientIpAddrChangeReason.setStatus(_B)
_NtwsRFDetectRogueAPMacAddr_Type=MacAddress
_NtwsRFDetectRogueAPMacAddr_Object=MibScalar
ntwsRFDetectRogueAPMacAddr=_NtwsRFDetectRogueAPMacAddr_Object((1,3,6,1,4,1,45,6,1,2,70),_NtwsRFDetectRogueAPMacAddr_Type())
ntwsRFDetectRogueAPMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsRFDetectRogueAPMacAddr.setStatus(_B)
_NtwsBlacklistingRemainingTime_Type=Unsigned32
_NtwsBlacklistingRemainingTime_Object=MibScalar
ntwsBlacklistingRemainingTime=_NtwsBlacklistingRemainingTime_Object((1,3,6,1,4,1,45,6,1,2,71),_NtwsBlacklistingRemainingTime_Type())
ntwsBlacklistingRemainingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsBlacklistingRemainingTime.setStatus(_B)
_NtwsBlacklistingCause_Type=NtwsBlacklistingCause
_NtwsBlacklistingCause_Object=MibScalar
ntwsBlacklistingCause=_NtwsBlacklistingCause_Object((1,3,6,1,4,1,45,6,1,2,72),_NtwsBlacklistingCause_Type())
ntwsBlacklistingCause.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsBlacklistingCause.setStatus(_B)
_NtwsNumLicensedActiveAPs_Type=Unsigned32
_NtwsNumLicensedActiveAPs_Object=MibScalar
ntwsNumLicensedActiveAPs=_NtwsNumLicensedActiveAPs_Object((1,3,6,1,4,1,45,6,1,2,73),_NtwsNumLicensedActiveAPs_Type())
ntwsNumLicensedActiveAPs.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsNumLicensedActiveAPs.setStatus(_B)
_NtwsClientDynAuthorClientIp_Type=IpAddress
_NtwsClientDynAuthorClientIp_Object=MibScalar
ntwsClientDynAuthorClientIp=_NtwsClientDynAuthorClientIp_Object((1,3,6,1,4,1,45,6,1,2,74),_NtwsClientDynAuthorClientIp_Type())
ntwsClientDynAuthorClientIp.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientDynAuthorClientIp.setStatus(_B)
_NtwsChangedUserParamOldValues_Type=NtwsUserAttributeList
_NtwsChangedUserParamOldValues_Object=MibScalar
ntwsChangedUserParamOldValues=_NtwsChangedUserParamOldValues_Object((1,3,6,1,4,1,45,6,1,2,75),_NtwsChangedUserParamOldValues_Type())
ntwsChangedUserParamOldValues.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsChangedUserParamOldValues.setStatus(_B)
_NtwsChangedUserParamNewValues_Type=NtwsUserAttributeList
_NtwsChangedUserParamNewValues_Object=MibScalar
ntwsChangedUserParamNewValues=_NtwsChangedUserParamNewValues_Object((1,3,6,1,4,1,45,6,1,2,76),_NtwsChangedUserParamNewValues_Type())
ntwsChangedUserParamNewValues.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsChangedUserParamNewValues.setStatus(_B)
_NtwsClientDisconnectSource_Type=NtwsSessionDisconnectType
_NtwsClientDisconnectSource_Object=MibScalar
ntwsClientDisconnectSource=_NtwsClientDisconnectSource_Object((1,3,6,1,4,1,45,6,1,2,77),_NtwsClientDisconnectSource_Type())
ntwsClientDisconnectSource.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientDisconnectSource.setStatus(_B)
class _NtwsClientDisconnectDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtwsClientDisconnectDescription_Type.__name__=_O
_NtwsClientDisconnectDescription_Object=MibScalar
ntwsClientDisconnectDescription=_NtwsClientDisconnectDescription_Object((1,3,6,1,4,1,45,6,1,2,78),_NtwsClientDisconnectDescription_Type())
ntwsClientDisconnectDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientDisconnectDescription.setStatus(_B)
_NtwsMobilityDomainSecondarySeedIp_Type=IpAddress
_NtwsMobilityDomainSecondarySeedIp_Object=MibScalar
ntwsMobilityDomainSecondarySeedIp=_NtwsMobilityDomainSecondarySeedIp_Object((1,3,6,1,4,1,45,6,1,2,79),_NtwsMobilityDomainSecondarySeedIp_Type())
ntwsMobilityDomainSecondarySeedIp.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsMobilityDomainSecondarySeedIp.setStatus(_B)
_NtwsMobilityDomainPrimarySeedIp_Type=IpAddress
_NtwsMobilityDomainPrimarySeedIp_Object=MibScalar
ntwsMobilityDomainPrimarySeedIp=_NtwsMobilityDomainPrimarySeedIp_Object((1,3,6,1,4,1,45,6,1,2,80),_NtwsMobilityDomainPrimarySeedIp_Type())
ntwsMobilityDomainPrimarySeedIp.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsMobilityDomainPrimarySeedIp.setStatus(_B)
_NtwsRFDetectClassificationReason_Type=NtwsRFDetectClassificationReason
_NtwsRFDetectClassificationReason_Object=MibScalar
ntwsRFDetectClassificationReason=_NtwsRFDetectClassificationReason_Object((1,3,6,1,4,1,45,6,1,2,81),_NtwsRFDetectClassificationReason_Type())
ntwsRFDetectClassificationReason.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsRFDetectClassificationReason.setStatus(_B)
class _NtwsConfigSaveFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtwsConfigSaveFileName_Type.__name__=_O
_NtwsConfigSaveFileName_Object=MibScalar
ntwsConfigSaveFileName=_NtwsConfigSaveFileName_Object((1,3,6,1,4,1,45,6,1,2,82),_NtwsConfigSaveFileName_Type())
ntwsConfigSaveFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsConfigSaveFileName.setStatus(_B)
_NtwsConfigSaveInitiatorType_Type=NtwsConfigSaveInitiatorType
_NtwsConfigSaveInitiatorType_Object=MibScalar
ntwsConfigSaveInitiatorType=_NtwsConfigSaveInitiatorType_Object((1,3,6,1,4,1,45,6,1,2,83),_NtwsConfigSaveInitiatorType_Type())
ntwsConfigSaveInitiatorType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsConfigSaveInitiatorType.setStatus(_B)
_NtwsConfigSaveInitiatorIp_Type=IpAddress
_NtwsConfigSaveInitiatorIp_Object=MibScalar
ntwsConfigSaveInitiatorIp=_NtwsConfigSaveInitiatorIp_Object((1,3,6,1,4,1,45,6,1,2,84),_NtwsConfigSaveInitiatorIp_Type())
ntwsConfigSaveInitiatorIp.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsConfigSaveInitiatorIp.setStatus(_B)
class _NtwsConfigSaveInitiatorDetails_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtwsConfigSaveInitiatorDetails_Type.__name__=_O
_NtwsConfigSaveInitiatorDetails_Object=MibScalar
ntwsConfigSaveInitiatorDetails=_NtwsConfigSaveInitiatorDetails_Object((1,3,6,1,4,1,45,6,1,2,85),_NtwsConfigSaveInitiatorDetails_Type())
ntwsConfigSaveInitiatorDetails.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsConfigSaveInitiatorDetails.setStatus(_B)
_NtwsConfigSaveGeneration_Type=Counter32
_NtwsConfigSaveGeneration_Object=MibScalar
ntwsConfigSaveGeneration=_NtwsConfigSaveGeneration_Object((1,3,6,1,4,1,45,6,1,2,86),_NtwsConfigSaveGeneration_Type())
ntwsConfigSaveGeneration.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsConfigSaveGeneration.setStatus(_B)
_NtwsApNum_Type=NtwsApNum
_NtwsApNum_Object=MibScalar
ntwsApNum=_NtwsApNum_Object((1,3,6,1,4,1,45,6,1,2,87),_NtwsApNum_Type())
ntwsApNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsApNum.setStatus(_B)
_NtwsRadioMode_Type=NtwsRadioMode
_NtwsRadioMode_Object=MibScalar
ntwsRadioMode=_NtwsRadioMode_Object((1,3,6,1,4,1,45,6,1,2,88),_NtwsRadioMode_Type())
ntwsRadioMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsRadioMode.setStatus(_B)
_NtwsMichaelMICFailureCause_Type=NtwsMichaelMICFailureCause
_NtwsMichaelMICFailureCause_Object=MibScalar
ntwsMichaelMICFailureCause=_NtwsMichaelMICFailureCause_Object((1,3,6,1,4,1,45,6,1,2,89),_NtwsMichaelMICFailureCause_Type())
ntwsMichaelMICFailureCause.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsMichaelMICFailureCause.setStatus(_B)
_NtwsClientAccessMode_Type=NtwsClientAccessMode
_NtwsClientAccessMode_Object=MibScalar
ntwsClientAccessMode=_NtwsClientAccessMode_Object((1,3,6,1,4,1,45,6,1,2,90),_NtwsClientAccessMode_Type())
ntwsClientAccessMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientAccessMode.setStatus(_B)
_NtwsClientAuthorizationReason_Type=NtwsClientAuthorizationReason
_NtwsClientAuthorizationReason_Object=MibScalar
ntwsClientAuthorizationReason=_NtwsClientAuthorizationReason_Object((1,3,6,1,4,1,45,6,1,2,91),_NtwsClientAuthorizationReason_Type())
ntwsClientAuthorizationReason.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientAuthorizationReason.setStatus(_B)
class _NtwsPhysPortNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_NtwsPhysPortNum_Type.__name__=_A8
_NtwsPhysPortNum_Object=MibScalar
ntwsPhysPortNum=_NtwsPhysPortNum_Object((1,3,6,1,4,1,45,6,1,2,92),_NtwsPhysPortNum_Type())
ntwsPhysPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsPhysPortNum.setStatus(_B)
_NtwsApMgrOldIp_Type=IpAddress
_NtwsApMgrOldIp_Object=MibScalar
ntwsApMgrOldIp=_NtwsApMgrOldIp_Object((1,3,6,1,4,1,45,6,1,2,93),_NtwsApMgrOldIp_Type())
ntwsApMgrOldIp.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsApMgrOldIp.setStatus(_B)
_NtwsApMgrNewIp_Type=IpAddress
_NtwsApMgrNewIp_Object=MibScalar
ntwsApMgrNewIp=_NtwsApMgrNewIp_Object((1,3,6,1,4,1,45,6,1,2,94),_NtwsApMgrNewIp_Type())
ntwsApMgrNewIp.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsApMgrNewIp.setStatus(_B)
_NtwsApMgrChangeReason_Type=NtwsApMgrChangeReason
_NtwsApMgrChangeReason_Object=MibScalar
ntwsApMgrChangeReason=_NtwsApMgrChangeReason_Object((1,3,6,1,4,1,45,6,1,2,95),_NtwsApMgrChangeReason_Type())
ntwsApMgrChangeReason.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsApMgrChangeReason.setStatus(_B)
_NtwsClientClearedReason_Type=NtwsClientClearedReason
_NtwsClientClearedReason_Object=MibScalar
ntwsClientClearedReason=_NtwsClientClearedReason_Object((1,3,6,1,4,1,45,6,1,2,96),_NtwsClientClearedReason_Type())
ntwsClientClearedReason.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientClearedReason.setStatus(_B)
_NtwsMobilityDomainResiliencyStatus_Type=NtwsMobilityDomainResiliencyStatus
_NtwsMobilityDomainResiliencyStatus_Object=MibScalar
ntwsMobilityDomainResiliencyStatus=_NtwsMobilityDomainResiliencyStatus_Object((1,3,6,1,4,1,45,6,1,2,97),_NtwsMobilityDomainResiliencyStatus_Type())
ntwsMobilityDomainResiliencyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsMobilityDomainResiliencyStatus.setStatus(_B)
_NtwsClientSessionElapsedSeconds_Type=Unsigned32
_NtwsClientSessionElapsedSeconds_Object=MibScalar
ntwsClientSessionElapsedSeconds=_NtwsClientSessionElapsedSeconds_Object((1,3,6,1,4,1,45,6,1,2,98),_NtwsClientSessionElapsedSeconds_Type())
ntwsClientSessionElapsedSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientSessionElapsedSeconds.setStatus(_B)
_NtwsRadioChannelWidth_Type=NtwsRadioChannelWidth
_NtwsRadioChannelWidth_Object=MibScalar
ntwsRadioChannelWidth=_NtwsRadioChannelWidth_Object((1,3,6,1,4,1,45,6,1,2,99),_NtwsRadioChannelWidth_Type())
ntwsRadioChannelWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsRadioChannelWidth.setStatus(_B)
_NtwsRadioMimoState_Type=NtwsRadioMimoState
_NtwsRadioMimoState_Object=MibScalar
ntwsRadioMimoState=_NtwsRadioMimoState_Object((1,3,6,1,4,1,45,6,1,2,100),_NtwsRadioMimoState_Type())
ntwsRadioMimoState.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsRadioMimoState.setStatus(_B)
_NtwsClientRadioType_Type=NtwsRadioType
_NtwsClientRadioType_Object=MibScalar
ntwsClientRadioType=_NtwsClientRadioType_Object((1,3,6,1,4,1,45,6,1,2,101),_NtwsClientRadioType_Type())
ntwsClientRadioType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClientRadioType.setStatus(_B)
_NtwsRFDetectXmtrRadioType_Type=NtwsRadioType
_NtwsRFDetectXmtrRadioType_Object=MibScalar
ntwsRFDetectXmtrRadioType=_NtwsRFDetectXmtrRadioType_Object((1,3,6,1,4,1,45,6,1,2,102),_NtwsRFDetectXmtrRadioType_Type())
ntwsRFDetectXmtrRadioType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsRFDetectXmtrRadioType.setStatus(_B)
_NtwsRFDetectXmtrCryptoType_Type=NtwsCryptoType
_NtwsRFDetectXmtrCryptoType_Object=MibScalar
ntwsRFDetectXmtrCryptoType=_NtwsRFDetectXmtrCryptoType_Object((1,3,6,1,4,1,45,6,1,2,103),_NtwsRFDetectXmtrCryptoType_Type())
ntwsRFDetectXmtrCryptoType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsRFDetectXmtrCryptoType.setStatus(_B)
_NtwsClusterFailureReason_Type=NtwsClusterFailureReason
_NtwsClusterFailureReason_Object=MibScalar
ntwsClusterFailureReason=_NtwsClusterFailureReason_Object((1,3,6,1,4,1,45,6,1,2,104),_NtwsClusterFailureReason_Type())
ntwsClusterFailureReason.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClusterFailureReason.setStatus(_B)
class _NtwsClusterFailureDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtwsClusterFailureDescription_Type.__name__=_O
_NtwsClusterFailureDescription_Object=MibScalar
ntwsClusterFailureDescription=_NtwsClusterFailureDescription_Object((1,3,6,1,4,1,45,6,1,2,105),_NtwsClusterFailureDescription_Type())
ntwsClusterFailureDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ntwsClusterFailureDescription.setStatus(_B)
_NtwsTrapsV2_ObjectIdentity=ObjectIdentity
ntwsTrapsV2=_NtwsTrapsV2_ObjectIdentity((1,3,6,1,4,1,45,6,1,5,0))
ntwsDeviceFailTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,1))
ntwsDeviceFailTrap.setObjects((_A,_p))
if mibBuilder.loadTexts:ntwsDeviceFailTrap.setStatus(_B)
ntwsDeviceOkayTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,2))
ntwsDeviceOkayTrap.setObjects((_A,_p))
if mibBuilder.loadTexts:ntwsDeviceOkayTrap.setStatus(_B)
ntwsPoEFailTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,3))
ntwsPoEFailTrap.setObjects((_A,_E))
if mibBuilder.loadTexts:ntwsPoEFailTrap.setStatus(_B)
ntwsApTimeoutTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,4))
ntwsApTimeoutTrap.setObjects(*((_A,_E),(_A,_b),(_A,_q),(_A,_I)))
if mibBuilder.loadTexts:ntwsApTimeoutTrap.setStatus(_D)
ntwsAPBootTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,5))
ntwsAPBootTrap.setObjects(*((_A,_E),(_A,_b),(_A,_q),(_A,_I)))
if mibBuilder.loadTexts:ntwsAPBootTrap.setStatus(_D)
ntwsMobilityDomainJoinTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,6))
ntwsMobilityDomainJoinTrap.setObjects((_A,_r))
if mibBuilder.loadTexts:ntwsMobilityDomainJoinTrap.setStatus(_B)
ntwsMobilityDomainTimeoutTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,7))
ntwsMobilityDomainTimeoutTrap.setObjects((_A,_r))
if mibBuilder.loadTexts:ntwsMobilityDomainTimeoutTrap.setStatus(_B)
ntwsMpMichaelMICFailure=NotificationType((1,3,6,1,4,1,45,6,1,5,0,8))
ntwsMpMichaelMICFailure.setObjects(*((_A,_E),(_A,_T),(_A,_J),(_A,_F),(_A,_H),(_A,_H)))
if mibBuilder.loadTexts:ntwsMpMichaelMICFailure.setStatus(_D)
ntwsRFDetectRogueAPTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,9))
ntwsRFDetectRogueAPTrap.setObjects(*((_A,_G),(_A,_L)))
if mibBuilder.loadTexts:ntwsRFDetectRogueAPTrap.setStatus(_D)
ntwsRFDetectAdhocUserTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,10))
ntwsRFDetectAdhocUserTrap.setObjects(*((_A,_G),(_A,_L)))
if mibBuilder.loadTexts:ntwsRFDetectAdhocUserTrap.setStatus(_B)
ntwsRFDetectRogueDisappearTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,11))
ntwsRFDetectRogueDisappearTrap.setObjects((_A,_G))
if mibBuilder.loadTexts:ntwsRFDetectRogueDisappearTrap.setStatus(_D)
ntwsClientAuthenticationFailureTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,12))
ntwsClientAuthenticationFailureTrap.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_U),(_A,_Q),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J),(_A,_AB),(_A,_c)))
if mibBuilder.loadTexts:ntwsClientAuthenticationFailureTrap.setStatus(_B)
ntwsClientAuthorizationFailureTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,13))
ntwsClientAuthorizationFailureTrap.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_U),(_A,_Q),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J),(_A,_AC),(_A,_s),(_A,_t),(_A,_c)))
if mibBuilder.loadTexts:ntwsClientAuthorizationFailureTrap.setStatus(_B)
ntwsClientAssociationFailureTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,14))
ntwsClientAssociationFailureTrap.setObjects(*((_A,_H),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J),(_A,_AD),(_A,_c)))
if mibBuilder.loadTexts:ntwsClientAssociationFailureTrap.setStatus(_B)
ntwsClientAuthorizationSuccessTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,15))
ntwsClientAuthorizationSuccessTrap.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_X),(_A,_Z),(_A,_u),(_A,_U),(_A,_Q),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J),(_A,_AE)))
if mibBuilder.loadTexts:ntwsClientAuthorizationSuccessTrap.setStatus(_D)
ntwsClientDeAssociationTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,16))
ntwsClientDeAssociationTrap.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_X),(_A,_U),(_A,_Q),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:ntwsClientDeAssociationTrap.setStatus(_B)
ntwsClientRoamingTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,17))
ntwsClientRoamingTrap.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:ntwsClientRoamingTrap.setStatus(_B)
ntwsAutoTuneRadioPowerChangeTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,18))
ntwsAutoTuneRadioPowerChangeTrap.setObjects(*((_A,_T),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:ntwsAutoTuneRadioPowerChangeTrap.setStatus(_B)
ntwsAutoTuneRadioChannelChangeTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,19))
ntwsAutoTuneRadioChannelChangeTrap.setObjects(*((_A,_T),(_A,_AP),(_A,_AQ),(_A,_AR)))
if mibBuilder.loadTexts:ntwsAutoTuneRadioChannelChangeTrap.setStatus(_B)
ntwsCounterMeasureStartTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,20))
ntwsCounterMeasureStartTrap.setObjects(*((_A,_G),(_A,_T)))
if mibBuilder.loadTexts:ntwsCounterMeasureStartTrap.setStatus(_B)
ntwsCounterMeasureStopTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,21))
ntwsCounterMeasureStopTrap.setObjects(*((_A,_G),(_A,_T)))
if mibBuilder.loadTexts:ntwsCounterMeasureStopTrap.setStatus(_B)
ntwsClientDot1xFailureTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,22))
ntwsClientDot1xFailureTrap.setObjects(*((_A,_M),(_A,_H),(_A,_Q),(_A,_K),(_A,_I),(_A,_E),(_A,_F),(_A,_J),(_A,_AS),(_A,_AT),(_A,_c)))
if mibBuilder.loadTexts:ntwsClientDot1xFailureTrap.setStatus(_B)
ntwsClientClearedTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,23))
ntwsClientClearedTrap.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J),(_A,_AU),(_A,_V)))
if mibBuilder.loadTexts:ntwsClientClearedTrap.setStatus(_D)
ntwsClientAuthorizationSuccessTrap2=NotificationType((1,3,6,1,4,1,45,6,1,5,0,24))
ntwsClientAuthorizationSuccessTrap2.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_X),(_A,_Z),(_A,_u),(_A,_U),(_A,_Q),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J),(_A,_d),(_A,_V)))
if mibBuilder.loadTexts:ntwsClientAuthorizationSuccessTrap2.setStatus(_D)
ntwsRFDetectSpoofedMacAPTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,25))
ntwsRFDetectSpoofedMacAPTrap.setObjects(*((_A,_G),(_A,_L)))
if mibBuilder.loadTexts:ntwsRFDetectSpoofedMacAPTrap.setStatus(_D)
ntwsRFDetectSpoofedSsidAPTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,26))
ntwsRFDetectSpoofedSsidAPTrap.setObjects(*((_A,_G),(_A,_L)))
if mibBuilder.loadTexts:ntwsRFDetectSpoofedSsidAPTrap.setStatus(_D)
ntwsRFDetectDoSTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,27))
ntwsRFDetectDoSTrap.setObjects(*((_A,_v),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:ntwsRFDetectDoSTrap.setStatus(_B)
ntwsRFDetectClientViaRogueWiredAPTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,28))
ntwsRFDetectClientViaRogueWiredAPTrap.setObjects(*((_A,_f),(_A,_E),(_A,_g),(_A,_h),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:ntwsRFDetectClientViaRogueWiredAPTrap.setStatus(_D)
ntwsRFDetectInterferingRogueAPTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,29))
ntwsRFDetectInterferingRogueAPTrap.setObjects(*((_A,_G),(_A,_L)))
if mibBuilder.loadTexts:ntwsRFDetectInterferingRogueAPTrap.setStatus(_D)
ntwsRFDetectInterferingRogueDisappearTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,30))
ntwsRFDetectInterferingRogueDisappearTrap.setObjects((_A,_G))
if mibBuilder.loadTexts:ntwsRFDetectInterferingRogueDisappearTrap.setStatus(_D)
ntwsRFDetectUnAuthorizedSsidTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,31))
ntwsRFDetectUnAuthorizedSsidTrap.setObjects(*((_A,_G),(_A,_L)))
if mibBuilder.loadTexts:ntwsRFDetectUnAuthorizedSsidTrap.setStatus(_D)
ntwsRFDetectUnAuthorizedOuiTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,32))
ntwsRFDetectUnAuthorizedOuiTrap.setObjects(*((_A,_G),(_A,_L)))
if mibBuilder.loadTexts:ntwsRFDetectUnAuthorizedOuiTrap.setStatus(_D)
ntwsRFDetectUnAuthorizedAPTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,33))
ntwsRFDetectUnAuthorizedAPTrap.setObjects(*((_A,_G),(_A,_L)))
if mibBuilder.loadTexts:ntwsRFDetectUnAuthorizedAPTrap.setStatus(_D)
ntwsDAPConnectWarningTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,34))
ntwsDAPConnectWarningTrap.setObjects(*((_A,_AV),(_A,_Y),(_A,_AW),(_A,_AX)))
if mibBuilder.loadTexts:ntwsDAPConnectWarningTrap.setStatus(_D)
ntwsRFDetectDoSPortTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,35))
ntwsRFDetectDoSPortTrap.setObjects(*((_A,_v),(_A,_G),(_A,_K),(_A,_E),(_A,_I)))
if mibBuilder.loadTexts:ntwsRFDetectDoSPortTrap.setStatus(_B)
ntwsMpMichaelMICFailure2=NotificationType((1,3,6,1,4,1,45,6,1,5,0,36))
ntwsMpMichaelMICFailure2.setObjects(*((_A,_E),(_A,_F),(_A,_H),(_A,_w)))
if mibBuilder.loadTexts:ntwsMpMichaelMICFailure2.setStatus(_D)
ntwsApNonOperStatusTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,37))
ntwsApNonOperStatusTrap.setObjects(*((_A,_Y),(_A,_b),(_A,_x),(_A,_y),(_A,_a),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:ntwsApNonOperStatusTrap.setStatus(_D)
ntwsApOperRadioStatusTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,38))
ntwsApOperRadioStatusTrap.setObjects(*((_A,_Y),(_A,_x),(_A,_y),(_A,_a),(_A,_F),(_A,_T),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:ntwsApOperRadioStatusTrap.setStatus(_D)
ntwsClientIpAddrChangeTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,39))
ntwsClientIpAddrChangeTrap.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_X),(_A,_Z),(_A,_U),(_A,_Q),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J),(_A,_d),(_A,_V),(_A,_AY)))
if mibBuilder.loadTexts:ntwsClientIpAddrChangeTrap.setStatus(_B)
ntwsClientAssociationSuccessTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,40))
ntwsClientAssociationSuccessTrap.setObjects(*((_A,_H),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:ntwsClientAssociationSuccessTrap.setStatus(_B)
ntwsClientAuthenticationSuccessTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,41))
ntwsClientAuthenticationSuccessTrap.setObjects(*((_A,_H),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:ntwsClientAuthenticationSuccessTrap.setStatus(_B)
ntwsClientDeAuthenticationTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,42))
ntwsClientDeAuthenticationTrap.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_X),(_A,_U),(_A,_Q),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:ntwsClientDeAuthenticationTrap.setStatus(_B)
ntwsRFDetectBlacklistedTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,43))
ntwsRFDetectBlacklistedTrap.setObjects(*((_A,_G),(_A,_K),(_A,_E),(_A,_I),(_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:ntwsRFDetectBlacklistedTrap.setStatus(_B)
ntwsRFDetectClientViaRogueWiredAPTrap2=NotificationType((1,3,6,1,4,1,45,6,1,5,0,44))
ntwsRFDetectClientViaRogueWiredAPTrap2.setObjects(*((_A,_f),(_A,_E),(_A,_g),(_A,_h),(_A,_G),(_A,_L),(_A,_A2)))
if mibBuilder.loadTexts:ntwsRFDetectClientViaRogueWiredAPTrap2.setStatus(_D)
ntwsRFDetectAdhocUserDisappearTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,45))
ntwsRFDetectAdhocUserDisappearTrap.setObjects((_A,_G))
if mibBuilder.loadTexts:ntwsRFDetectAdhocUserDisappearTrap.setStatus(_B)
ntwsApRejectLicenseExceededTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,46))
ntwsApRejectLicenseExceededTrap.setObjects((_A,_Ab))
if mibBuilder.loadTexts:ntwsApRejectLicenseExceededTrap.setStatus(_B)
ntwsClientDynAuthorChangeSuccessTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,47))
ntwsClientDynAuthorChangeSuccessTrap.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_Z),(_A,_A3),(_A,_Q),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J),(_A,_d),(_A,_V),(_A,_Ac),(_A,_Ad)))
if mibBuilder.loadTexts:ntwsClientDynAuthorChangeSuccessTrap.setStatus(_B)
ntwsClientDynAuthorChangeFailureTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,48))
ntwsClientDynAuthorChangeFailureTrap.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_A3),(_A,_Q),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J),(_A,_s),(_A,_t),(_A,_c)))
if mibBuilder.loadTexts:ntwsClientDynAuthorChangeFailureTrap.setStatus(_B)
ntwsClientDisconnectTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,49))
ntwsClientDisconnectTrap.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_K),(_A,_E),(_A,_F),(_A,_I),(_A,_J),(_A,_V),(_A,_Ae),(_A,_Af)))
if mibBuilder.loadTexts:ntwsClientDisconnectTrap.setStatus(_B)
ntwsMobilityDomainFailOverTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,50))
ntwsMobilityDomainFailOverTrap.setObjects((_A,_Ag))
if mibBuilder.loadTexts:ntwsMobilityDomainFailOverTrap.setStatus(_B)
ntwsMobilityDomainFailBackTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,51))
ntwsMobilityDomainFailBackTrap.setObjects((_A,_Ah))
if mibBuilder.loadTexts:ntwsMobilityDomainFailBackTrap.setStatus(_B)
ntwsRFDetectRogueDeviceTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,52))
ntwsRFDetectRogueDeviceTrap.setObjects(*((_A,_G),(_A,_L),(_A,_e)))
if mibBuilder.loadTexts:ntwsRFDetectRogueDeviceTrap.setStatus(_D)
ntwsRFDetectRogueDeviceDisappearTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,53))
ntwsRFDetectRogueDeviceDisappearTrap.setObjects((_A,_G))
if mibBuilder.loadTexts:ntwsRFDetectRogueDeviceDisappearTrap.setStatus(_B)
ntwsRFDetectSuspectDeviceTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,54))
ntwsRFDetectSuspectDeviceTrap.setObjects(*((_A,_G),(_A,_L),(_A,_e)))
if mibBuilder.loadTexts:ntwsRFDetectSuspectDeviceTrap.setStatus(_D)
ntwsRFDetectSuspectDeviceDisappearTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,55))
ntwsRFDetectSuspectDeviceDisappearTrap.setObjects((_A,_G))
if mibBuilder.loadTexts:ntwsRFDetectSuspectDeviceDisappearTrap.setStatus(_B)
ntwsRFDetectClientViaRogueWiredAPTrap3=NotificationType((1,3,6,1,4,1,45,6,1,5,0,56))
ntwsRFDetectClientViaRogueWiredAPTrap3.setObjects(*((_A,_f),(_A,_E),(_A,_g),(_A,_h),(_A,_G),(_A,_L),(_A,_A2),(_A,_e)))
if mibBuilder.loadTexts:ntwsRFDetectClientViaRogueWiredAPTrap3.setStatus(_B)
ntwsRFDetectClassificationChangeTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,57))
if mibBuilder.loadTexts:ntwsRFDetectClassificationChangeTrap.setStatus(_B)
ntwsConfigurationSavedTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,58))
ntwsConfigurationSavedTrap.setObjects(*((_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am)))
if mibBuilder.loadTexts:ntwsConfigurationSavedTrap.setStatus(_B)
ntwsApNonOperStatusTrap2=NotificationType((1,3,6,1,4,1,45,6,1,5,0,59))
ntwsApNonOperStatusTrap2.setObjects(*((_A,_Y),(_A,_b),(_A,_W),(_A,_a),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:ntwsApNonOperStatusTrap2.setStatus(_B)
ntwsApOperRadioStatusTrap2=NotificationType((1,3,6,1,4,1,45,6,1,5,0,60))
ntwsApOperRadioStatusTrap2.setObjects(*((_A,_Y),(_A,_W),(_A,_a),(_A,_F),(_A,_T),(_A,_i),(_A,_A4),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:ntwsApOperRadioStatusTrap2.setStatus(_D)
ntwsMichaelMICFailure=NotificationType((1,3,6,1,4,1,45,6,1,5,0,61))
ntwsMichaelMICFailure.setObjects(*((_A,_W),(_A,_F),(_A,_T),(_A,_An),(_A,_H),(_A,_w)))
if mibBuilder.loadTexts:ntwsMichaelMICFailure.setStatus(_B)
ntwsClientAuthorizationSuccessTrap3=NotificationType((1,3,6,1,4,1,45,6,1,5,0,62))
ntwsClientAuthorizationSuccessTrap3.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_X),(_A,_Z),(_A,_U),(_A,_Q),(_A,_m),(_A,_n),(_A,_W),(_A,_F),(_A,_J),(_A,_d),(_A,_V),(_A,_A5)))
if mibBuilder.loadTexts:ntwsClientAuthorizationSuccessTrap3.setStatus(_D)
ntwsApManagerChangeTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,63))
ntwsApManagerChangeTrap.setObjects(*((_A,_Y),(_A,_b),(_A,_W),(_A,_a),(_A,_Ao),(_A,_Ap),(_A,_Aq)))
if mibBuilder.loadTexts:ntwsApManagerChangeTrap.setStatus(_B)
ntwsClientClearedTrap2=NotificationType((1,3,6,1,4,1,45,6,1,5,0,64))
ntwsClientClearedTrap2.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_m),(_A,_n),(_A,_W),(_A,_F),(_A,_J),(_A,_Ar),(_A,_V),(_A,_As)))
if mibBuilder.loadTexts:ntwsClientClearedTrap2.setStatus(_B)
ntwsMobilityDomainResiliencyStatusTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,65))
ntwsMobilityDomainResiliencyStatusTrap.setObjects((_A,_At))
if mibBuilder.loadTexts:ntwsMobilityDomainResiliencyStatusTrap.setStatus(_B)
ntwsApOperRadioStatusTrap3=NotificationType((1,3,6,1,4,1,45,6,1,5,0,66))
ntwsApOperRadioStatusTrap3.setObjects(*((_A,_Y),(_A,_W),(_A,_a),(_A,_F),(_A,_T),(_A,_i),(_A,_A4),(_A,_j),(_A,_Au),(_A,_Av),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:ntwsApOperRadioStatusTrap3.setStatus(_B)
ntwsClientAuthorizationSuccessTrap4=NotificationType((1,3,6,1,4,1,45,6,1,5,0,67))
ntwsClientAuthorizationSuccessTrap4.setObjects(*((_A,_M),(_A,_N),(_A,_H),(_A,_R),(_A,_X),(_A,_Z),(_A,_U),(_A,_Q),(_A,_m),(_A,_n),(_A,_W),(_A,_F),(_A,_J),(_A,_Aw),(_A,_d),(_A,_V),(_A,_A5)))
if mibBuilder.loadTexts:ntwsClientAuthorizationSuccessTrap4.setStatus(_B)
ntwsRFDetectRogueDeviceTrap2=NotificationType((1,3,6,1,4,1,45,6,1,5,0,68))
ntwsRFDetectRogueDeviceTrap2.setObjects(*((_A,_G),(_A,_A6),(_A,_A7),(_A,_L),(_A,_e)))
if mibBuilder.loadTexts:ntwsRFDetectRogueDeviceTrap2.setStatus(_B)
ntwsRFDetectSuspectDeviceTrap2=NotificationType((1,3,6,1,4,1,45,6,1,5,0,69))
ntwsRFDetectSuspectDeviceTrap2.setObjects(*((_A,_G),(_A,_A6),(_A,_A7),(_A,_L),(_A,_e)))
if mibBuilder.loadTexts:ntwsRFDetectSuspectDeviceTrap2.setStatus(_B)
ntwsClusterFailureTrap=NotificationType((1,3,6,1,4,1,45,6,1,5,0,70))
ntwsClusterFailureTrap.setObjects(*((_A,_Ax),(_A,_Ay)))
if mibBuilder.loadTexts:ntwsClusterFailureTrap.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'NtwsAssociationFailureType':NtwsAssociationFailureType,'NtwsAuthenticationFailureType':NtwsAuthenticationFailureType,'NtwsAuthorizationFailureType':NtwsAuthorizationFailureType,'NtwsDot1xFailureType':NtwsDot1xFailureType,'NtwsRFDetectDoSType':NtwsRFDetectDoSType,'NtwsClientIpAddrChangeReason':NtwsClientIpAddrChangeReason,'NtwsBlacklistingCause':NtwsBlacklistingCause,'NtwsUserAttributeList':NtwsUserAttributeList,'NtwsSessionDisconnectType':NtwsSessionDisconnectType,'NtwsConfigSaveInitiatorType':NtwsConfigSaveInitiatorType,'NtwsMichaelMICFailureCause':NtwsMichaelMICFailureCause,'NtwsClientAuthorizationReason':NtwsClientAuthorizationReason,'NtwsApMgrChangeReason':NtwsApMgrChangeReason,'NtwsClientClearedReason':NtwsClientClearedReason,'NtwsMobilityDomainResiliencyStatus':NtwsMobilityDomainResiliencyStatus,'NtwsClusterFailureReason':NtwsClusterFailureReason,_p:ntwsDeviceId,_r:ntwsMobilityDomainIp,_b:ntwsAPMACAddress,_H:ntwsClientMACAddress,_G:ntwsRFDetectXmtrMacAddr,_E:ntwsPortNum,_F:ntwsAPRadioNum,_AE:ntwsRadioRssi,'ntwsRadioBSSID':ntwsRadioBSSID,_M:ntwsUserName,_U:ntwsClientAuthServerIp,_Z:ntwsClientSessionState,_I:ntwsDAPNum,_R:ntwsClientIp,_N:ntwsClientSessionId,_Q:ntwsClientAuthenProtocolType,_X:ntwsClientVLANName,_u:ntwsClientSessionStartTime,'ntwsClientFailureCause':ntwsClientFailureCause,_AG:ntwsClientRoamedFromPortNum,_AH:ntwsClientRoamedFromRadioNum,_AI:ntwsClientRoamedFromDAPNum,_s:ntwsUserParams,_AC:ntwsClientLocationPolicyIndex,_AD:ntwsClientAssociationFailureCause,_AB:ntwsClientAuthenticationFailureCause,_t:ntwsClientAuthorizationFailureCause,_c:ntwsClientFailureCauseDescription,_AJ:ntwsClientRoamedFromWsIp,_AF:ntwsClientRoamedFromAccessType,_K:ntwsClientAccessType,_T:ntwsRadioMACAddress,_AN:ntwsRadioPowerChangeReason,_AP:ntwsNewChannelNum,_AQ:ntwsOldChannelNum,_AR:ntwsChannelChangeReason,_L:ntwsRFDetectListenerListInfo,_J:ntwsRadioSSID,_AL:ntwsNewPowerLevel,_AM:ntwsOldPowerLevel,_AO:ntwsRadioPowerChangeDescription,'ntwsCounterMeasurePerformerListInfo':ntwsCounterMeasurePerformerListInfo,_AS:ntwsClientDot1xState,_AT:ntwsClientDot1xFailureCause,_q:ntwsAPAccessType,_d:ntwsUserAccessType,_AU:ntwsClientSessionElapsedTime,_V:ntwsLocalId,_v:ntwsRFDetectDoSType,_f:ntwsSourceWsIp,_g:ntwsClientVLANid,_h:ntwsClientVLANtag,_AV:ntwsDeviceModel,_Y:ntwsDeviceSerNum,_AW:ntwsRsaPubKeyFingerPrint,_AX:ntwsDAPconnectWarningType,_w:ntwsClientMACAddress2,_x:ntwsApAttachType,_y:ntwsApPortOrDapNum,_a:ntwsApName,_z:ntwsApTransition,_A0:ntwsApFailDetail,_i:ntwsRadioType,_j:ntwsRadioConfigState,_k:ntwsApConnectSecurityType,_l:ntwsApServiceAvailability,_A1:ntwsApWasOperational,_AK:ntwsClientTimeSinceLastRoam,_AY:ntwsClientIpAddrChangeReason,_A2:ntwsRFDetectRogueAPMacAddr,_AZ:ntwsBlacklistingRemainingTime,_Aa:ntwsBlacklistingCause,_Ab:ntwsNumLicensedActiveAPs,_A3:ntwsClientDynAuthorClientIp,_Ac:ntwsChangedUserParamOldValues,_Ad:ntwsChangedUserParamNewValues,_Ae:ntwsClientDisconnectSource,_Af:ntwsClientDisconnectDescription,_Ag:ntwsMobilityDomainSecondarySeedIp,_Ah:ntwsMobilityDomainPrimarySeedIp,_e:ntwsRFDetectClassificationReason,_Ai:ntwsConfigSaveFileName,_Aj:ntwsConfigSaveInitiatorType,_Ak:ntwsConfigSaveInitiatorIp,_Al:ntwsConfigSaveInitiatorDetails,_Am:ntwsConfigSaveGeneration,_W:ntwsApNum,_A4:ntwsRadioMode,_An:ntwsMichaelMICFailureCause,_m:ntwsClientAccessMode,_A5:ntwsClientAuthorizationReason,_n:ntwsPhysPortNum,_Ao:ntwsApMgrOldIp,_Ap:ntwsApMgrNewIp,_Aq:ntwsApMgrChangeReason,_As:ntwsClientClearedReason,_At:ntwsMobilityDomainResiliencyStatus,_Ar:ntwsClientSessionElapsedSeconds,_Au:ntwsRadioChannelWidth,_Av:ntwsRadioMimoState,_Aw:ntwsClientRadioType,_A6:ntwsRFDetectXmtrRadioType,_A7:ntwsRFDetectXmtrCryptoType,_Ax:ntwsClusterFailureReason,_Ay:ntwsClusterFailureDescription,'ntwsTrapMib':ntwsTrapMib,'ntwsTrapsV2':ntwsTrapsV2,'ntwsDeviceFailTrap':ntwsDeviceFailTrap,'ntwsDeviceOkayTrap':ntwsDeviceOkayTrap,'ntwsPoEFailTrap':ntwsPoEFailTrap,'ntwsApTimeoutTrap':ntwsApTimeoutTrap,'ntwsAPBootTrap':ntwsAPBootTrap,'ntwsMobilityDomainJoinTrap':ntwsMobilityDomainJoinTrap,'ntwsMobilityDomainTimeoutTrap':ntwsMobilityDomainTimeoutTrap,'ntwsMpMichaelMICFailure':ntwsMpMichaelMICFailure,'ntwsRFDetectRogueAPTrap':ntwsRFDetectRogueAPTrap,'ntwsRFDetectAdhocUserTrap':ntwsRFDetectAdhocUserTrap,'ntwsRFDetectRogueDisappearTrap':ntwsRFDetectRogueDisappearTrap,'ntwsClientAuthenticationFailureTrap':ntwsClientAuthenticationFailureTrap,'ntwsClientAuthorizationFailureTrap':ntwsClientAuthorizationFailureTrap,'ntwsClientAssociationFailureTrap':ntwsClientAssociationFailureTrap,'ntwsClientAuthorizationSuccessTrap':ntwsClientAuthorizationSuccessTrap,'ntwsClientDeAssociationTrap':ntwsClientDeAssociationTrap,'ntwsClientRoamingTrap':ntwsClientRoamingTrap,'ntwsAutoTuneRadioPowerChangeTrap':ntwsAutoTuneRadioPowerChangeTrap,'ntwsAutoTuneRadioChannelChangeTrap':ntwsAutoTuneRadioChannelChangeTrap,'ntwsCounterMeasureStartTrap':ntwsCounterMeasureStartTrap,'ntwsCounterMeasureStopTrap':ntwsCounterMeasureStopTrap,'ntwsClientDot1xFailureTrap':ntwsClientDot1xFailureTrap,'ntwsClientClearedTrap':ntwsClientClearedTrap,'ntwsClientAuthorizationSuccessTrap2':ntwsClientAuthorizationSuccessTrap2,'ntwsRFDetectSpoofedMacAPTrap':ntwsRFDetectSpoofedMacAPTrap,'ntwsRFDetectSpoofedSsidAPTrap':ntwsRFDetectSpoofedSsidAPTrap,'ntwsRFDetectDoSTrap':ntwsRFDetectDoSTrap,'ntwsRFDetectClientViaRogueWiredAPTrap':ntwsRFDetectClientViaRogueWiredAPTrap,'ntwsRFDetectInterferingRogueAPTrap':ntwsRFDetectInterferingRogueAPTrap,'ntwsRFDetectInterferingRogueDisappearTrap':ntwsRFDetectInterferingRogueDisappearTrap,'ntwsRFDetectUnAuthorizedSsidTrap':ntwsRFDetectUnAuthorizedSsidTrap,'ntwsRFDetectUnAuthorizedOuiTrap':ntwsRFDetectUnAuthorizedOuiTrap,'ntwsRFDetectUnAuthorizedAPTrap':ntwsRFDetectUnAuthorizedAPTrap,'ntwsDAPConnectWarningTrap':ntwsDAPConnectWarningTrap,'ntwsRFDetectDoSPortTrap':ntwsRFDetectDoSPortTrap,'ntwsMpMichaelMICFailure2':ntwsMpMichaelMICFailure2,'ntwsApNonOperStatusTrap':ntwsApNonOperStatusTrap,'ntwsApOperRadioStatusTrap':ntwsApOperRadioStatusTrap,'ntwsClientIpAddrChangeTrap':ntwsClientIpAddrChangeTrap,'ntwsClientAssociationSuccessTrap':ntwsClientAssociationSuccessTrap,'ntwsClientAuthenticationSuccessTrap':ntwsClientAuthenticationSuccessTrap,'ntwsClientDeAuthenticationTrap':ntwsClientDeAuthenticationTrap,'ntwsRFDetectBlacklistedTrap':ntwsRFDetectBlacklistedTrap,'ntwsRFDetectClientViaRogueWiredAPTrap2':ntwsRFDetectClientViaRogueWiredAPTrap2,'ntwsRFDetectAdhocUserDisappearTrap':ntwsRFDetectAdhocUserDisappearTrap,'ntwsApRejectLicenseExceededTrap':ntwsApRejectLicenseExceededTrap,'ntwsClientDynAuthorChangeSuccessTrap':ntwsClientDynAuthorChangeSuccessTrap,'ntwsClientDynAuthorChangeFailureTrap':ntwsClientDynAuthorChangeFailureTrap,'ntwsClientDisconnectTrap':ntwsClientDisconnectTrap,'ntwsMobilityDomainFailOverTrap':ntwsMobilityDomainFailOverTrap,'ntwsMobilityDomainFailBackTrap':ntwsMobilityDomainFailBackTrap,'ntwsRFDetectRogueDeviceTrap':ntwsRFDetectRogueDeviceTrap,'ntwsRFDetectRogueDeviceDisappearTrap':ntwsRFDetectRogueDeviceDisappearTrap,'ntwsRFDetectSuspectDeviceTrap':ntwsRFDetectSuspectDeviceTrap,'ntwsRFDetectSuspectDeviceDisappearTrap':ntwsRFDetectSuspectDeviceDisappearTrap,'ntwsRFDetectClientViaRogueWiredAPTrap3':ntwsRFDetectClientViaRogueWiredAPTrap3,'ntwsRFDetectClassificationChangeTrap':ntwsRFDetectClassificationChangeTrap,'ntwsConfigurationSavedTrap':ntwsConfigurationSavedTrap,'ntwsApNonOperStatusTrap2':ntwsApNonOperStatusTrap2,'ntwsApOperRadioStatusTrap2':ntwsApOperRadioStatusTrap2,'ntwsMichaelMICFailure':ntwsMichaelMICFailure,'ntwsClientAuthorizationSuccessTrap3':ntwsClientAuthorizationSuccessTrap3,'ntwsApManagerChangeTrap':ntwsApManagerChangeTrap,'ntwsClientClearedTrap2':ntwsClientClearedTrap2,'ntwsMobilityDomainResiliencyStatusTrap':ntwsMobilityDomainResiliencyStatusTrap,'ntwsApOperRadioStatusTrap3':ntwsApOperRadioStatusTrap3,'ntwsClientAuthorizationSuccessTrap4':ntwsClientAuthorizationSuccessTrap4,'ntwsRFDetectRogueDeviceTrap2':ntwsRFDetectRogueDeviceTrap2,'ntwsRFDetectSuspectDeviceTrap2':ntwsRFDetectSuspectDeviceTrap2,'ntwsClusterFailureTrap':ntwsClusterFailureTrap})