_BI='tmnxNtpV8v0Group'
_BH='tmnxNtpGlobalV8v0Group'
_BG='tmnxNtpNotificationV4v0Group'
_BF='tmnxNtpNotificationGroup'
_BE='tmnxNtpServerChange'
_BD='tmnxNtpClientInfoLastRequestTime'
_BC='tmnxNtpConfigAuthCheck'
_BB='tmnxNtpConfigServerAuthenticate'
_BA='tmnxNtpConfigServer'
_B9='tmnxNtpConfigAdminState'
_B8='tmnxNtpConfigRowStatus'
_B7='tmnxNtpAuthKeyType'
_B6='tmnxNtpAuthKey'
_B5='tmnxNtpAuthKeyLastChanged'
_B4='tmnxNtpAuthKeyEntryStatus'
_B3='tmnxNtpPeersStatusFlags'
_B2='tmnxNtpPeersStatus'
_B1='tmnxNtpPeersPrefPeer'
_B0='tmnxNtpPeersOffset'
_A_='tmnxNtpPeersReach'
_Az='tmnxNtpPeersReceiveTime'
_Ay='tmnxNtpPeersRefId'
_Ax='tmnxNtpPeersHostPoll'
_Aw='tmnxNtpPeersPeerPoll'
_Av='tmnxNtpPeersStratum'
_Au='tmnxNtpPeersMode'
_At='tmnxNtpPeersHostPort'
_As='tmnxNtpPeersHostAddress'
_Ar='tmnxNtpPeersHostAddrType'
_Aq='tmnxNtpPeersPeerPort'
_Ap='tmnxNtpPeersConfigured'
_Ao='tmnxNtpPeersAuthErrs'
_An='tmnxNtpPeersAssocId'
_Am='tmnxNtpPeersPrefer'
_Al='tmnxNtpPeersVersion'
_Ak='tmnxNtpPeersAuthKeyId'
_Aj='tmnxNtpPeersLastChanged'
_Ai='tmnxNtpPeersEntryStatus'
_Ah='tmnxNtpServersAuthErrs'
_Ag='tmnxNtpServersAssocId'
_Af='tmnxNtpServersPrefer'
_Ae='tmnxNtpServersVersion'
_Ad='tmnxNtpServersAuthKeyId'
_Ac='tmnxNtpServersLastChanged'
_Ab='tmnxNtpServersEntryStatus'
_Aa='tmnxNtpMulticastAssocId'
_AZ='tmnxNtpMulticastAuthenticate'
_AY='tmnxNtpMulticastAuthErrs'
_AX='tmnxNtpMulticastTtl'
_AW='tmnxNtpMulticastVersion'
_AV='tmnxNtpMulticastAuthKeyId'
_AU='tmnxNtpMulticastLastChanged'
_AT='tmnxNtpMulticastEntryStatus'
_AS='tmnxNtpMulticastAddress'
_AR='tmnxNtpMulticastAddressType'
_AQ='tmnxNtpBroadcastAssocId'
_AP='tmnxNtpBroadcastAuthenticate'
_AO='tmnxNtpBroadcastAuthErrs'
_AN='tmnxNtpBroadcastTtl'
_AM='tmnxNtpBroadcastVersion'
_AL='tmnxNtpBroadcastAuthKeyId'
_AK='tmnxNtpBroadcastLastChanged'
_AJ='tmnxNtpBroadcastEntryStatus'
_AI='tmnxNtpClientAddress'
_AH='tmnxNtpClientAddressType'
_AG='tmnxNtpAuthKeyId'
_AF='broadcastclient'
_AE='broadcast'
_AD='tmnxNtpPeersVarAssocId'
_AC='tmnxNtpPeersAddress'
_AB='tmnxNtpPeersAddrType'
_AA='tmnxNtpServersAddress'
_A9='tmnxNtpServersAddrType'
_A8='tmnxNtpMulticastIfIndex'
_A7='tmnxNtpMulticastDirection'
_A6='tmnxNtpBroadcastIfIndex'
_A5='tmnxNtpBroadcastDirection'
_A4='outOfService'
_A3='inService'
_A2='TmnxAdminState'
_A1='InetAddressType'
_A0='OctetString'
_z='tmnxNtpNotificationV6v0Group'
_y='tmnxNtpUtcOffsetInThreshold'
_x='tmnxNtpUtcOffsetExThreshold'
_w='tmnxNtpAuthKeyFailType'
_v='tmnxNtpAuthCheck'
_u='tmnxNtpServerKeyId'
_t='tmnxNtpServer'
_s='tmnxNtpAdminState'
_r='tmnxNtp'
_q='tmnxNtpSysClock'
_p='tmnxNtpSysPeer'
_o='tmnxNtpSysPoll'
_n='tmnxNtpSysRefTime'
_m='tmnxNtpSysRefId'
_l='tmnxNtpSysStratum'
_k='tmnxNtpSysLeap'
_j='accessible-for-notify'
_i='seconds'
_h='NTPVersionPeerServer'
_g='NTPVersion'
_f='seconds as a power of two'
_e='4d.4d'
_d='tmnxNtpGlobalGroup'
_c='tmnxNtpOperChange'
_b='tmnxNtpMaxFreqDftExceed'
_a='tmnxNtpServersAvail'
_Z='tmnxNtpNoServersAvail'
_Y='tmnxNtpAuthMismatch'
_X='tmnxNtpUTCOffsetThreshold'
_W='tmnxNtpUTCOffset'
_V='tmnxNtpPeersPeerVRtrID'
_U='tmnxNtpPeersPeerAddress'
_T='tmnxNtpPeersPeerAddrType'
_S='tmnxNtpOperState'
_R='tmnxNtpAuthKeyGroup'
_Q='tmnxNtpPeersGroup'
_P='tmnxNtpServersGroup'
_O='tmnxNtpMulticastGroup'
_N='tmnxNtpBroadcastGroup'
_M='read-write'
_L='vRtrID'
_K='TIMETRA-VRTR-MIB'
_J='InetAddress'
_I='Integer32'
_H='Unsigned32'
_G='TruthValue'
_F='not-accessible'
_E='obsolete'
_D='read-create'
_C='read-only'
_B='current'
_A='TIMETRA-NTP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_A0,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_J,_A1)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_G)
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
TmnxAdminState,TmnxVRtrID=mibBuilder.importSymbols('TIMETRA-TC-MIB',_A2,'TmnxVRtrID')
vRtrID,=mibBuilder.importSymbols(_K,_L)
timetraNtpMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,38))
if mibBuilder.loadTexts:timetraNtpMIBModule.setRevisions(('2008-01-01 00:00','2006-03-27 00:00'))
class NTPTimeStamp(TextualConvention,OctetString):status=_B;displayHint=_e;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class NTPLeapIndicator(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noWarning',0),('addSecond',1),('subtractSecond',2),('alarm',3)))
class NTPSignedTimeValue(TextualConvention,OctetString):status=_B;displayHint=_e;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class NTPUnsignedTimeValue(TextualConvention,OctetString):status=_B;displayHint=_e;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class NTPStratum(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class NTPRefId(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class NTPPollInterval(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
class NTPAssocIdentifier(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class NTPVersion(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4))
class NTPVersionPeerServer(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2,4))
class TmnxNtpDirection(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('transmit',1),('receive',2)))
_TmnxNtpConformance_ObjectIdentity=ObjectIdentity
tmnxNtpConformance=_TmnxNtpConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,38))
_TmnxNtpCompliances_ObjectIdentity=ObjectIdentity
tmnxNtpCompliances=_TmnxNtpCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,38,1))
_TmnxNtpGroups_ObjectIdentity=ObjectIdentity
tmnxNtpGroups=_TmnxNtpGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,38,2))
_TmnxNtpObjs_ObjectIdentity=ObjectIdentity
tmnxNtpObjs=_TmnxNtpObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,38))
_TmnxNtpSysObjs_ObjectIdentity=ObjectIdentity
tmnxNtpSysObjs=_TmnxNtpSysObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,38,1))
_TmnxNtpSystem_ObjectIdentity=ObjectIdentity
tmnxNtpSystem=_TmnxNtpSystem_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,38,1,1))
_TmnxNtpSysLeap_Type=NTPLeapIndicator
_TmnxNtpSysLeap_Object=MibScalar
tmnxNtpSysLeap=_TmnxNtpSysLeap_Object((1,3,6,1,4,1,6527,3,1,2,38,1,1,1),_TmnxNtpSysLeap_Type())
tmnxNtpSysLeap.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpSysLeap.setStatus(_B)
_TmnxNtpSysStratum_Type=NTPStratum
_TmnxNtpSysStratum_Object=MibScalar
tmnxNtpSysStratum=_TmnxNtpSysStratum_Object((1,3,6,1,4,1,6527,3,1,2,38,1,1,2),_TmnxNtpSysStratum_Type())
tmnxNtpSysStratum.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpSysStratum.setStatus(_B)
_TmnxNtpSysRefId_Type=NTPRefId
_TmnxNtpSysRefId_Object=MibScalar
tmnxNtpSysRefId=_TmnxNtpSysRefId_Object((1,3,6,1,4,1,6527,3,1,2,38,1,1,3),_TmnxNtpSysRefId_Type())
tmnxNtpSysRefId.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpSysRefId.setStatus(_B)
_TmnxNtpSysRefTime_Type=NTPTimeStamp
_TmnxNtpSysRefTime_Object=MibScalar
tmnxNtpSysRefTime=_TmnxNtpSysRefTime_Object((1,3,6,1,4,1,6527,3,1,2,38,1,1,4),_TmnxNtpSysRefTime_Type())
tmnxNtpSysRefTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpSysRefTime.setStatus(_B)
_TmnxNtpSysPoll_Type=NTPPollInterval
_TmnxNtpSysPoll_Object=MibScalar
tmnxNtpSysPoll=_TmnxNtpSysPoll_Object((1,3,6,1,4,1,6527,3,1,2,38,1,1,5),_TmnxNtpSysPoll_Type())
tmnxNtpSysPoll.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpSysPoll.setStatus(_B)
if mibBuilder.loadTexts:tmnxNtpSysPoll.setUnits(_f)
_TmnxNtpSysPeer_Type=NTPAssocIdentifier
_TmnxNtpSysPeer_Object=MibScalar
tmnxNtpSysPeer=_TmnxNtpSysPeer_Object((1,3,6,1,4,1,6527,3,1,2,38,1,1,6),_TmnxNtpSysPeer_Type())
tmnxNtpSysPeer.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpSysPeer.setStatus(_B)
_TmnxNtpSysClock_Type=NTPTimeStamp
_TmnxNtpSysClock_Object=MibScalar
tmnxNtpSysClock=_TmnxNtpSysClock_Object((1,3,6,1,4,1,6527,3,1,2,38,1,1,7),_TmnxNtpSysClock_Type())
tmnxNtpSysClock.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpSysClock.setStatus(_B)
class _TmnxNtp_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_TmnxNtp_Type.__name__=_I
_TmnxNtp_Object=MibScalar
tmnxNtp=_TmnxNtp_Object((1,3,6,1,4,1,6527,3,1,2,38,1,1,8),_TmnxNtp_Type())
tmnxNtp.setMaxAccess(_M)
if mibBuilder.loadTexts:tmnxNtp.setStatus(_E)
class _TmnxNtpAdminState_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noop',1),(_A3,2),(_A4,3)))
_TmnxNtpAdminState_Type.__name__=_I
_TmnxNtpAdminState_Object=MibScalar
tmnxNtpAdminState=_TmnxNtpAdminState_Object((1,3,6,1,4,1,6527,3,1,2,38,1,1,9),_TmnxNtpAdminState_Type())
tmnxNtpAdminState.setMaxAccess(_M)
if mibBuilder.loadTexts:tmnxNtpAdminState.setStatus(_E)
class _TmnxNtpOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),(_A3,2),(_A4,3)))
_TmnxNtpOperState_Type.__name__=_I
_TmnxNtpOperState_Object=MibScalar
tmnxNtpOperState=_TmnxNtpOperState_Object((1,3,6,1,4,1,6527,3,1,2,38,1,1,10),_TmnxNtpOperState_Type())
tmnxNtpOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpOperState.setStatus(_B)
class _TmnxNtpServer_Type(TruthValue):defaultValue=2
_TmnxNtpServer_Type.__name__=_G
_TmnxNtpServer_Object=MibScalar
tmnxNtpServer=_TmnxNtpServer_Object((1,3,6,1,4,1,6527,3,1,2,38,1,1,11),_TmnxNtpServer_Type())
tmnxNtpServer.setMaxAccess(_M)
if mibBuilder.loadTexts:tmnxNtpServer.setStatus(_E)
class _TmnxNtpServerKeyId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,255))
_TmnxNtpServerKeyId_Type.__name__=_H
_TmnxNtpServerKeyId_Object=MibScalar
tmnxNtpServerKeyId=_TmnxNtpServerKeyId_Object((1,3,6,1,4,1,6527,3,1,2,38,1,1,12),_TmnxNtpServerKeyId_Type())
tmnxNtpServerKeyId.setMaxAccess(_M)
if mibBuilder.loadTexts:tmnxNtpServerKeyId.setStatus(_E)
class _TmnxNtpAuthCheck_Type(TruthValue):defaultValue=1
_TmnxNtpAuthCheck_Type.__name__=_G
_TmnxNtpAuthCheck_Object=MibScalar
tmnxNtpAuthCheck=_TmnxNtpAuthCheck_Object((1,3,6,1,4,1,6527,3,1,2,38,1,1,13),_TmnxNtpAuthCheck_Type())
tmnxNtpAuthCheck.setMaxAccess(_M)
if mibBuilder.loadTexts:tmnxNtpAuthCheck.setStatus(_E)
_TmnxNtpBroadcastTable_Object=MibTable
tmnxNtpBroadcastTable=_TmnxNtpBroadcastTable_Object((1,3,6,1,4,1,6527,3,1,2,38,1,2))
if mibBuilder.loadTexts:tmnxNtpBroadcastTable.setStatus(_B)
_TmnxNtpBroadcastEntry_Object=MibTableRow
tmnxNtpBroadcastEntry=_TmnxNtpBroadcastEntry_Object((1,3,6,1,4,1,6527,3,1,2,38,1,2,1))
tmnxNtpBroadcastEntry.setIndexNames((0,_A,_A5),(0,_K,_L),(0,_A,_A6))
if mibBuilder.loadTexts:tmnxNtpBroadcastEntry.setStatus(_B)
_TmnxNtpBroadcastDirection_Type=TmnxNtpDirection
_TmnxNtpBroadcastDirection_Object=MibTableColumn
tmnxNtpBroadcastDirection=_TmnxNtpBroadcastDirection_Object((1,3,6,1,4,1,6527,3,1,2,38,1,2,1,1),_TmnxNtpBroadcastDirection_Type())
tmnxNtpBroadcastDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxNtpBroadcastDirection.setStatus(_B)
_TmnxNtpBroadcastIfIndex_Type=InterfaceIndex
_TmnxNtpBroadcastIfIndex_Object=MibTableColumn
tmnxNtpBroadcastIfIndex=_TmnxNtpBroadcastIfIndex_Object((1,3,6,1,4,1,6527,3,1,2,38,1,2,1,2),_TmnxNtpBroadcastIfIndex_Type())
tmnxNtpBroadcastIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxNtpBroadcastIfIndex.setStatus(_B)
_TmnxNtpBroadcastEntryStatus_Type=RowStatus
_TmnxNtpBroadcastEntryStatus_Object=MibTableColumn
tmnxNtpBroadcastEntryStatus=_TmnxNtpBroadcastEntryStatus_Object((1,3,6,1,4,1,6527,3,1,2,38,1,2,1,3),_TmnxNtpBroadcastEntryStatus_Type())
tmnxNtpBroadcastEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpBroadcastEntryStatus.setStatus(_B)
_TmnxNtpBroadcastLastChanged_Type=TimeStamp
_TmnxNtpBroadcastLastChanged_Object=MibTableColumn
tmnxNtpBroadcastLastChanged=_TmnxNtpBroadcastLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,38,1,2,1,4),_TmnxNtpBroadcastLastChanged_Type())
tmnxNtpBroadcastLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpBroadcastLastChanged.setStatus(_B)
class _TmnxNtpBroadcastAuthKeyId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,255))
_TmnxNtpBroadcastAuthKeyId_Type.__name__=_H
_TmnxNtpBroadcastAuthKeyId_Object=MibTableColumn
tmnxNtpBroadcastAuthKeyId=_TmnxNtpBroadcastAuthKeyId_Object((1,3,6,1,4,1,6527,3,1,2,38,1,2,1,5),_TmnxNtpBroadcastAuthKeyId_Type())
tmnxNtpBroadcastAuthKeyId.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpBroadcastAuthKeyId.setStatus(_B)
class _TmnxNtpBroadcastVersion_Type(NTPVersion):defaultValue=4
_TmnxNtpBroadcastVersion_Type.__name__=_g
_TmnxNtpBroadcastVersion_Object=MibTableColumn
tmnxNtpBroadcastVersion=_TmnxNtpBroadcastVersion_Object((1,3,6,1,4,1,6527,3,1,2,38,1,2,1,6),_TmnxNtpBroadcastVersion_Type())
tmnxNtpBroadcastVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpBroadcastVersion.setStatus(_B)
class _TmnxNtpBroadcastTtl_Type(Unsigned32):defaultValue=127;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TmnxNtpBroadcastTtl_Type.__name__=_H
_TmnxNtpBroadcastTtl_Object=MibTableColumn
tmnxNtpBroadcastTtl=_TmnxNtpBroadcastTtl_Object((1,3,6,1,4,1,6527,3,1,2,38,1,2,1,7),_TmnxNtpBroadcastTtl_Type())
tmnxNtpBroadcastTtl.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpBroadcastTtl.setStatus(_B)
_TmnxNtpBroadcastAuthErrs_Type=Counter32
_TmnxNtpBroadcastAuthErrs_Object=MibTableColumn
tmnxNtpBroadcastAuthErrs=_TmnxNtpBroadcastAuthErrs_Object((1,3,6,1,4,1,6527,3,1,2,38,1,2,1,8),_TmnxNtpBroadcastAuthErrs_Type())
tmnxNtpBroadcastAuthErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpBroadcastAuthErrs.setStatus(_B)
class _TmnxNtpBroadcastAuthenticate_Type(TruthValue):defaultValue=2
_TmnxNtpBroadcastAuthenticate_Type.__name__=_G
_TmnxNtpBroadcastAuthenticate_Object=MibTableColumn
tmnxNtpBroadcastAuthenticate=_TmnxNtpBroadcastAuthenticate_Object((1,3,6,1,4,1,6527,3,1,2,38,1,2,1,9),_TmnxNtpBroadcastAuthenticate_Type())
tmnxNtpBroadcastAuthenticate.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpBroadcastAuthenticate.setStatus(_B)
_TmnxNtpBroadcastAssocId_Type=NTPAssocIdentifier
_TmnxNtpBroadcastAssocId_Object=MibTableColumn
tmnxNtpBroadcastAssocId=_TmnxNtpBroadcastAssocId_Object((1,3,6,1,4,1,6527,3,1,2,38,1,2,1,10),_TmnxNtpBroadcastAssocId_Type())
tmnxNtpBroadcastAssocId.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpBroadcastAssocId.setStatus(_B)
_TmnxNtpMulticastTable_Object=MibTable
tmnxNtpMulticastTable=_TmnxNtpMulticastTable_Object((1,3,6,1,4,1,6527,3,1,2,38,1,3))
if mibBuilder.loadTexts:tmnxNtpMulticastTable.setStatus(_B)
_TmnxNtpMulticastEntry_Object=MibTableRow
tmnxNtpMulticastEntry=_TmnxNtpMulticastEntry_Object((1,3,6,1,4,1,6527,3,1,2,38,1,3,1))
tmnxNtpMulticastEntry.setIndexNames((0,_A,_A7),(0,_A,_A8))
if mibBuilder.loadTexts:tmnxNtpMulticastEntry.setStatus(_B)
_TmnxNtpMulticastDirection_Type=TmnxNtpDirection
_TmnxNtpMulticastDirection_Object=MibTableColumn
tmnxNtpMulticastDirection=_TmnxNtpMulticastDirection_Object((1,3,6,1,4,1,6527,3,1,2,38,1,3,1,1),_TmnxNtpMulticastDirection_Type())
tmnxNtpMulticastDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxNtpMulticastDirection.setStatus(_B)
_TmnxNtpMulticastIfIndex_Type=InterfaceIndex
_TmnxNtpMulticastIfIndex_Object=MibTableColumn
tmnxNtpMulticastIfIndex=_TmnxNtpMulticastIfIndex_Object((1,3,6,1,4,1,6527,3,1,2,38,1,3,1,2),_TmnxNtpMulticastIfIndex_Type())
tmnxNtpMulticastIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxNtpMulticastIfIndex.setStatus(_B)
class _TmnxNtpMulticastAddressType_Type(InetAddressType):defaultValue=1
_TmnxNtpMulticastAddressType_Type.__name__=_A1
_TmnxNtpMulticastAddressType_Object=MibTableColumn
tmnxNtpMulticastAddressType=_TmnxNtpMulticastAddressType_Object((1,3,6,1,4,1,6527,3,1,2,38,1,3,1,3),_TmnxNtpMulticastAddressType_Type())
tmnxNtpMulticastAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpMulticastAddressType.setStatus(_B)
class _TmnxNtpMulticastAddress_Type(InetAddress):defaultHexValue='E0000101';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxNtpMulticastAddress_Type.__name__=_J
_TmnxNtpMulticastAddress_Object=MibTableColumn
tmnxNtpMulticastAddress=_TmnxNtpMulticastAddress_Object((1,3,6,1,4,1,6527,3,1,2,38,1,3,1,4),_TmnxNtpMulticastAddress_Type())
tmnxNtpMulticastAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpMulticastAddress.setStatus(_B)
_TmnxNtpMulticastEntryStatus_Type=RowStatus
_TmnxNtpMulticastEntryStatus_Object=MibTableColumn
tmnxNtpMulticastEntryStatus=_TmnxNtpMulticastEntryStatus_Object((1,3,6,1,4,1,6527,3,1,2,38,1,3,1,5),_TmnxNtpMulticastEntryStatus_Type())
tmnxNtpMulticastEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpMulticastEntryStatus.setStatus(_B)
_TmnxNtpMulticastLastChanged_Type=TimeStamp
_TmnxNtpMulticastLastChanged_Object=MibTableColumn
tmnxNtpMulticastLastChanged=_TmnxNtpMulticastLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,38,1,3,1,6),_TmnxNtpMulticastLastChanged_Type())
tmnxNtpMulticastLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpMulticastLastChanged.setStatus(_B)
class _TmnxNtpMulticastAuthKeyId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,255))
_TmnxNtpMulticastAuthKeyId_Type.__name__=_H
_TmnxNtpMulticastAuthKeyId_Object=MibTableColumn
tmnxNtpMulticastAuthKeyId=_TmnxNtpMulticastAuthKeyId_Object((1,3,6,1,4,1,6527,3,1,2,38,1,3,1,7),_TmnxNtpMulticastAuthKeyId_Type())
tmnxNtpMulticastAuthKeyId.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpMulticastAuthKeyId.setStatus(_B)
class _TmnxNtpMulticastVersion_Type(NTPVersion):defaultValue=4
_TmnxNtpMulticastVersion_Type.__name__=_g
_TmnxNtpMulticastVersion_Object=MibTableColumn
tmnxNtpMulticastVersion=_TmnxNtpMulticastVersion_Object((1,3,6,1,4,1,6527,3,1,2,38,1,3,1,8),_TmnxNtpMulticastVersion_Type())
tmnxNtpMulticastVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpMulticastVersion.setStatus(_B)
class _TmnxNtpMulticastTtl_Type(Unsigned32):defaultValue=127;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TmnxNtpMulticastTtl_Type.__name__=_H
_TmnxNtpMulticastTtl_Object=MibTableColumn
tmnxNtpMulticastTtl=_TmnxNtpMulticastTtl_Object((1,3,6,1,4,1,6527,3,1,2,38,1,3,1,9),_TmnxNtpMulticastTtl_Type())
tmnxNtpMulticastTtl.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpMulticastTtl.setStatus(_B)
_TmnxNtpMulticastAuthErrs_Type=Counter32
_TmnxNtpMulticastAuthErrs_Object=MibTableColumn
tmnxNtpMulticastAuthErrs=_TmnxNtpMulticastAuthErrs_Object((1,3,6,1,4,1,6527,3,1,2,38,1,3,1,10),_TmnxNtpMulticastAuthErrs_Type())
tmnxNtpMulticastAuthErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpMulticastAuthErrs.setStatus(_B)
class _TmnxNtpMulticastAuthenticate_Type(TruthValue):defaultValue=2
_TmnxNtpMulticastAuthenticate_Type.__name__=_G
_TmnxNtpMulticastAuthenticate_Object=MibTableColumn
tmnxNtpMulticastAuthenticate=_TmnxNtpMulticastAuthenticate_Object((1,3,6,1,4,1,6527,3,1,2,38,1,3,1,11),_TmnxNtpMulticastAuthenticate_Type())
tmnxNtpMulticastAuthenticate.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpMulticastAuthenticate.setStatus(_B)
_TmnxNtpMulticastAssocId_Type=NTPAssocIdentifier
_TmnxNtpMulticastAssocId_Object=MibTableColumn
tmnxNtpMulticastAssocId=_TmnxNtpMulticastAssocId_Object((1,3,6,1,4,1,6527,3,1,2,38,1,3,1,12),_TmnxNtpMulticastAssocId_Type())
tmnxNtpMulticastAssocId.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpMulticastAssocId.setStatus(_B)
_TmnxNtpServers_ObjectIdentity=ObjectIdentity
tmnxNtpServers=_TmnxNtpServers_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,38,2))
_TmnxNtpServersTable_Object=MibTable
tmnxNtpServersTable=_TmnxNtpServersTable_Object((1,3,6,1,4,1,6527,3,1,2,38,2,1))
if mibBuilder.loadTexts:tmnxNtpServersTable.setStatus(_B)
_TmnxNtpServersEntry_Object=MibTableRow
tmnxNtpServersEntry=_TmnxNtpServersEntry_Object((1,3,6,1,4,1,6527,3,1,2,38,2,1,1))
tmnxNtpServersEntry.setIndexNames((0,_A,_A9),(0,_A,_AA),(0,_K,_L))
if mibBuilder.loadTexts:tmnxNtpServersEntry.setStatus(_B)
_TmnxNtpServersAddrType_Type=InetAddressType
_TmnxNtpServersAddrType_Object=MibTableColumn
tmnxNtpServersAddrType=_TmnxNtpServersAddrType_Object((1,3,6,1,4,1,6527,3,1,2,38,2,1,1,1),_TmnxNtpServersAddrType_Type())
tmnxNtpServersAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxNtpServersAddrType.setStatus(_B)
class _TmnxNtpServersAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxNtpServersAddress_Type.__name__=_J
_TmnxNtpServersAddress_Object=MibTableColumn
tmnxNtpServersAddress=_TmnxNtpServersAddress_Object((1,3,6,1,4,1,6527,3,1,2,38,2,1,1,2),_TmnxNtpServersAddress_Type())
tmnxNtpServersAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxNtpServersAddress.setStatus(_B)
_TmnxNtpServersEntryStatus_Type=RowStatus
_TmnxNtpServersEntryStatus_Object=MibTableColumn
tmnxNtpServersEntryStatus=_TmnxNtpServersEntryStatus_Object((1,3,6,1,4,1,6527,3,1,2,38,2,1,1,3),_TmnxNtpServersEntryStatus_Type())
tmnxNtpServersEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpServersEntryStatus.setStatus(_B)
_TmnxNtpServersLastChanged_Type=TimeStamp
_TmnxNtpServersLastChanged_Object=MibTableColumn
tmnxNtpServersLastChanged=_TmnxNtpServersLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,38,2,1,1,4),_TmnxNtpServersLastChanged_Type())
tmnxNtpServersLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpServersLastChanged.setStatus(_B)
class _TmnxNtpServersAuthKeyId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,255))
_TmnxNtpServersAuthKeyId_Type.__name__=_H
_TmnxNtpServersAuthKeyId_Object=MibTableColumn
tmnxNtpServersAuthKeyId=_TmnxNtpServersAuthKeyId_Object((1,3,6,1,4,1,6527,3,1,2,38,2,1,1,5),_TmnxNtpServersAuthKeyId_Type())
tmnxNtpServersAuthKeyId.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpServersAuthKeyId.setStatus(_B)
class _TmnxNtpServersVersion_Type(NTPVersionPeerServer):defaultValue=4
_TmnxNtpServersVersion_Type.__name__=_h
_TmnxNtpServersVersion_Object=MibTableColumn
tmnxNtpServersVersion=_TmnxNtpServersVersion_Object((1,3,6,1,4,1,6527,3,1,2,38,2,1,1,6),_TmnxNtpServersVersion_Type())
tmnxNtpServersVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpServersVersion.setStatus(_B)
class _TmnxNtpServersPrefer_Type(TruthValue):defaultValue=2
_TmnxNtpServersPrefer_Type.__name__=_G
_TmnxNtpServersPrefer_Object=MibTableColumn
tmnxNtpServersPrefer=_TmnxNtpServersPrefer_Object((1,3,6,1,4,1,6527,3,1,2,38,2,1,1,7),_TmnxNtpServersPrefer_Type())
tmnxNtpServersPrefer.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpServersPrefer.setStatus(_B)
_TmnxNtpServersAssocId_Type=NTPAssocIdentifier
_TmnxNtpServersAssocId_Object=MibTableColumn
tmnxNtpServersAssocId=_TmnxNtpServersAssocId_Object((1,3,6,1,4,1,6527,3,1,2,38,2,1,1,8),_TmnxNtpServersAssocId_Type())
tmnxNtpServersAssocId.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpServersAssocId.setStatus(_B)
_TmnxNtpServersAuthErrs_Type=Counter32
_TmnxNtpServersAuthErrs_Object=MibTableColumn
tmnxNtpServersAuthErrs=_TmnxNtpServersAuthErrs_Object((1,3,6,1,4,1,6527,3,1,2,38,2,1,1,9),_TmnxNtpServersAuthErrs_Type())
tmnxNtpServersAuthErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpServersAuthErrs.setStatus(_B)
_TmnxNtpPeers_ObjectIdentity=ObjectIdentity
tmnxNtpPeers=_TmnxNtpPeers_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,38,3))
_TmnxNtpPeersTable_Object=MibTable
tmnxNtpPeersTable=_TmnxNtpPeersTable_Object((1,3,6,1,4,1,6527,3,1,2,38,3,1))
if mibBuilder.loadTexts:tmnxNtpPeersTable.setStatus(_B)
_TmnxNtpPeersEntry_Object=MibTableRow
tmnxNtpPeersEntry=_TmnxNtpPeersEntry_Object((1,3,6,1,4,1,6527,3,1,2,38,3,1,1))
tmnxNtpPeersEntry.setIndexNames((0,_A,_AB),(0,_A,_AC),(0,_K,_L))
if mibBuilder.loadTexts:tmnxNtpPeersEntry.setStatus(_B)
_TmnxNtpPeersAddrType_Type=InetAddressType
_TmnxNtpPeersAddrType_Object=MibTableColumn
tmnxNtpPeersAddrType=_TmnxNtpPeersAddrType_Object((1,3,6,1,4,1,6527,3,1,2,38,3,1,1,1),_TmnxNtpPeersAddrType_Type())
tmnxNtpPeersAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxNtpPeersAddrType.setStatus(_B)
class _TmnxNtpPeersAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxNtpPeersAddress_Type.__name__=_J
_TmnxNtpPeersAddress_Object=MibTableColumn
tmnxNtpPeersAddress=_TmnxNtpPeersAddress_Object((1,3,6,1,4,1,6527,3,1,2,38,3,1,1,2),_TmnxNtpPeersAddress_Type())
tmnxNtpPeersAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxNtpPeersAddress.setStatus(_B)
_TmnxNtpPeersEntryStatus_Type=RowStatus
_TmnxNtpPeersEntryStatus_Object=MibTableColumn
tmnxNtpPeersEntryStatus=_TmnxNtpPeersEntryStatus_Object((1,3,6,1,4,1,6527,3,1,2,38,3,1,1,3),_TmnxNtpPeersEntryStatus_Type())
tmnxNtpPeersEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpPeersEntryStatus.setStatus(_B)
_TmnxNtpPeersLastChanged_Type=TimeStamp
_TmnxNtpPeersLastChanged_Object=MibTableColumn
tmnxNtpPeersLastChanged=_TmnxNtpPeersLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,38,3,1,1,4),_TmnxNtpPeersLastChanged_Type())
tmnxNtpPeersLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpPeersLastChanged.setStatus(_B)
class _TmnxNtpPeersAuthKeyId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,255))
_TmnxNtpPeersAuthKeyId_Type.__name__=_H
_TmnxNtpPeersAuthKeyId_Object=MibTableColumn
tmnxNtpPeersAuthKeyId=_TmnxNtpPeersAuthKeyId_Object((1,3,6,1,4,1,6527,3,1,2,38,3,1,1,5),_TmnxNtpPeersAuthKeyId_Type())
tmnxNtpPeersAuthKeyId.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpPeersAuthKeyId.setStatus(_B)
class _TmnxNtpPeersVersion_Type(NTPVersionPeerServer):defaultValue=4
_TmnxNtpPeersVersion_Type.__name__=_h
_TmnxNtpPeersVersion_Object=MibTableColumn
tmnxNtpPeersVersion=_TmnxNtpPeersVersion_Object((1,3,6,1,4,1,6527,3,1,2,38,3,1,1,6),_TmnxNtpPeersVersion_Type())
tmnxNtpPeersVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpPeersVersion.setStatus(_B)
class _TmnxNtpPeersPrefer_Type(TruthValue):defaultValue=2
_TmnxNtpPeersPrefer_Type.__name__=_G
_TmnxNtpPeersPrefer_Object=MibTableColumn
tmnxNtpPeersPrefer=_TmnxNtpPeersPrefer_Object((1,3,6,1,4,1,6527,3,1,2,38,3,1,1,7),_TmnxNtpPeersPrefer_Type())
tmnxNtpPeersPrefer.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpPeersPrefer.setStatus(_B)
_TmnxNtpPeersAssocId_Type=NTPAssocIdentifier
_TmnxNtpPeersAssocId_Object=MibTableColumn
tmnxNtpPeersAssocId=_TmnxNtpPeersAssocId_Object((1,3,6,1,4,1,6527,3,1,2,38,3,1,1,8),_TmnxNtpPeersAssocId_Type())
tmnxNtpPeersAssocId.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpPeersAssocId.setStatus(_B)
_TmnxNtpPeersAuthErrs_Type=Counter32
_TmnxNtpPeersAuthErrs_Object=MibTableColumn
tmnxNtpPeersAuthErrs=_TmnxNtpPeersAuthErrs_Object((1,3,6,1,4,1,6527,3,1,2,38,3,1,1,9),_TmnxNtpPeersAuthErrs_Type())
tmnxNtpPeersAuthErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpPeersAuthErrs.setStatus(_B)
_TmnxNtpPeersVarTable_Object=MibTable
tmnxNtpPeersVarTable=_TmnxNtpPeersVarTable_Object((1,3,6,1,4,1,6527,3,1,2,38,3,2))
if mibBuilder.loadTexts:tmnxNtpPeersVarTable.setStatus(_B)
_TmnxNtpPeersVarEntry_Object=MibTableRow
tmnxNtpPeersVarEntry=_TmnxNtpPeersVarEntry_Object((1,3,6,1,4,1,6527,3,1,2,38,3,2,1))
tmnxNtpPeersVarEntry.setIndexNames((0,_A,_AD))
if mibBuilder.loadTexts:tmnxNtpPeersVarEntry.setStatus(_B)
_TmnxNtpPeersVarAssocId_Type=NTPAssocIdentifier
_TmnxNtpPeersVarAssocId_Object=MibTableColumn
tmnxNtpPeersVarAssocId=_TmnxNtpPeersVarAssocId_Object((1,3,6,1,4,1,6527,3,1,2,38,3,2,1,1),_TmnxNtpPeersVarAssocId_Type())
tmnxNtpPeersVarAssocId.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxNtpPeersVarAssocId.setStatus(_B)
_TmnxNtpPeersConfigured_Type=TruthValue
_TmnxNtpPeersConfigured_Object=MibTableColumn
tmnxNtpPeersConfigured=_TmnxNtpPeersConfigured_Object((1,3,6,1,4,1,6527,3,1,2,38,3,2,1,2),_TmnxNtpPeersConfigured_Type())
tmnxNtpPeersConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpPeersConfigured.setStatus(_B)
_TmnxNtpPeersPeerAddrType_Type=InetAddressType
_TmnxNtpPeersPeerAddrType_Object=MibTableColumn
tmnxNtpPeersPeerAddrType=_TmnxNtpPeersPeerAddrType_Object((1,3,6,1,4,1,6527,3,1,2,38,3,2,1,3),_TmnxNtpPeersPeerAddrType_Type())
tmnxNtpPeersPeerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpPeersPeerAddrType.setStatus(_B)
class _TmnxNtpPeersPeerAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxNtpPeersPeerAddress_Type.__name__=_J
_TmnxNtpPeersPeerAddress_Object=MibTableColumn
tmnxNtpPeersPeerAddress=_TmnxNtpPeersPeerAddress_Object((1,3,6,1,4,1,6527,3,1,2,38,3,2,1,4),_TmnxNtpPeersPeerAddress_Type())
tmnxNtpPeersPeerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpPeersPeerAddress.setStatus(_B)
_TmnxNtpPeersPeerPort_Type=Unsigned32
_TmnxNtpPeersPeerPort_Object=MibTableColumn
tmnxNtpPeersPeerPort=_TmnxNtpPeersPeerPort_Object((1,3,6,1,4,1,6527,3,1,2,38,3,2,1,5),_TmnxNtpPeersPeerPort_Type())
tmnxNtpPeersPeerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpPeersPeerPort.setStatus(_B)
_TmnxNtpPeersHostAddrType_Type=InetAddressType
_TmnxNtpPeersHostAddrType_Object=MibTableColumn
tmnxNtpPeersHostAddrType=_TmnxNtpPeersHostAddrType_Object((1,3,6,1,4,1,6527,3,1,2,38,3,2,1,6),_TmnxNtpPeersHostAddrType_Type())
tmnxNtpPeersHostAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpPeersHostAddrType.setStatus(_B)
class _TmnxNtpPeersHostAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxNtpPeersHostAddress_Type.__name__=_J
_TmnxNtpPeersHostAddress_Object=MibTableColumn
tmnxNtpPeersHostAddress=_TmnxNtpPeersHostAddress_Object((1,3,6,1,4,1,6527,3,1,2,38,3,2,1,7),_TmnxNtpPeersHostAddress_Type())
tmnxNtpPeersHostAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpPeersHostAddress.setStatus(_B)
_TmnxNtpPeersHostPort_Type=Unsigned32
_TmnxNtpPeersHostPort_Object=MibTableColumn
tmnxNtpPeersHostPort=_TmnxNtpPeersHostPort_Object((1,3,6,1,4,1,6527,3,1,2,38,3,2,1,8),_TmnxNtpPeersHostPort_Type())
tmnxNtpPeersHostPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpPeersHostPort.setStatus(_B)
class _TmnxNtpPeersMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('unspecified',0),('symmetricActive',1),('symmetricPassive',2),('client',3),('server',4),(_AE,5),('reservedControl',6),('reservedPrivate',7),(_AF,8)))
_TmnxNtpPeersMode_Type.__name__=_I
_TmnxNtpPeersMode_Object=MibTableColumn
tmnxNtpPeersMode=_TmnxNtpPeersMode_Object((1,3,6,1,4,1,6527,3,1,2,38,3,2,1,9),_TmnxNtpPeersMode_Type())
tmnxNtpPeersMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpPeersMode.setStatus(_B)
_TmnxNtpPeersStratum_Type=NTPStratum
_TmnxNtpPeersStratum_Object=MibTableColumn
tmnxNtpPeersStratum=_TmnxNtpPeersStratum_Object((1,3,6,1,4,1,6527,3,1,2,38,3,2,1,10),_TmnxNtpPeersStratum_Type())
tmnxNtpPeersStratum.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpPeersStratum.setStatus(_B)
_TmnxNtpPeersPeerPoll_Type=NTPPollInterval
_TmnxNtpPeersPeerPoll_Object=MibTableColumn
tmnxNtpPeersPeerPoll=_TmnxNtpPeersPeerPoll_Object((1,3,6,1,4,1,6527,3,1,2,38,3,2,1,11),_TmnxNtpPeersPeerPoll_Type())
tmnxNtpPeersPeerPoll.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpPeersPeerPoll.setStatus(_B)
if mibBuilder.loadTexts:tmnxNtpPeersPeerPoll.setUnits(_f)
_TmnxNtpPeersHostPoll_Type=NTPPollInterval
_TmnxNtpPeersHostPoll_Object=MibTableColumn
tmnxNtpPeersHostPoll=_TmnxNtpPeersHostPoll_Object((1,3,6,1,4,1,6527,3,1,2,38,3,2,1,12),_TmnxNtpPeersHostPoll_Type())
tmnxNtpPeersHostPoll.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpPeersHostPoll.setStatus(_B)
if mibBuilder.loadTexts:tmnxNtpPeersHostPoll.setUnits(_f)
_TmnxNtpPeersRefId_Type=NTPRefId
_TmnxNtpPeersRefId_Object=MibTableColumn
tmnxNtpPeersRefId=_TmnxNtpPeersRefId_Object((1,3,6,1,4,1,6527,3,1,2,38,3,2,1,13),_TmnxNtpPeersRefId_Type())
tmnxNtpPeersRefId.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpPeersRefId.setStatus(_B)
_TmnxNtpPeersReceiveTime_Type=NTPTimeStamp
_TmnxNtpPeersReceiveTime_Object=MibTableColumn
tmnxNtpPeersReceiveTime=_TmnxNtpPeersReceiveTime_Object((1,3,6,1,4,1,6527,3,1,2,38,3,2,1,14),_TmnxNtpPeersReceiveTime_Type())
tmnxNtpPeersReceiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpPeersReceiveTime.setStatus(_B)
_TmnxNtpPeersReach_Type=Unsigned32
_TmnxNtpPeersReach_Object=MibTableColumn
tmnxNtpPeersReach=_TmnxNtpPeersReach_Object((1,3,6,1,4,1,6527,3,1,2,38,3,2,1,15),_TmnxNtpPeersReach_Type())
tmnxNtpPeersReach.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpPeersReach.setStatus(_B)
_TmnxNtpPeersOffset_Type=NTPSignedTimeValue
_TmnxNtpPeersOffset_Object=MibTableColumn
tmnxNtpPeersOffset=_TmnxNtpPeersOffset_Object((1,3,6,1,4,1,6527,3,1,2,38,3,2,1,16),_TmnxNtpPeersOffset_Type())
tmnxNtpPeersOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpPeersOffset.setStatus(_B)
if mibBuilder.loadTexts:tmnxNtpPeersOffset.setUnits(_i)
_TmnxNtpPeersPrefPeer_Type=TruthValue
_TmnxNtpPeersPrefPeer_Object=MibTableColumn
tmnxNtpPeersPrefPeer=_TmnxNtpPeersPrefPeer_Object((1,3,6,1,4,1,6527,3,1,2,38,3,2,1,17),_TmnxNtpPeersPrefPeer_Type())
tmnxNtpPeersPrefPeer.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpPeersPrefPeer.setStatus(_B)
class _TmnxNtpPeersStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('reject',0),('inaccurate',1),('excess',2),('outlyer',3),('candidate',4),('selected',5),('syspeer',6),('ppspeer',7)))
_TmnxNtpPeersStatus_Type.__name__=_I
_TmnxNtpPeersStatus_Object=MibTableColumn
tmnxNtpPeersStatus=_TmnxNtpPeersStatus_Object((1,3,6,1,4,1,6527,3,1,2,38,3,2,1,18),_TmnxNtpPeersStatus_Type())
tmnxNtpPeersStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpPeersStatus.setStatus(_B)
class _TmnxNtpPeersStatusFlags_Type(Bits):namedValues=NamedValues(*(('config',0),('authenable',1),('authentic',2),('reachable',3),(_AF,4),('multicastclient',5),(_AE,6),('multicast',7)))
_TmnxNtpPeersStatusFlags_Type.__name__='Bits'
_TmnxNtpPeersStatusFlags_Object=MibTableColumn
tmnxNtpPeersStatusFlags=_TmnxNtpPeersStatusFlags_Object((1,3,6,1,4,1,6527,3,1,2,38,3,2,1,19),_TmnxNtpPeersStatusFlags_Type())
tmnxNtpPeersStatusFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpPeersStatusFlags.setStatus(_B)
_TmnxNtpPeersPeerVRtrID_Type=TmnxVRtrID
_TmnxNtpPeersPeerVRtrID_Object=MibTableColumn
tmnxNtpPeersPeerVRtrID=_TmnxNtpPeersPeerVRtrID_Object((1,3,6,1,4,1,6527,3,1,2,38,3,2,1,20),_TmnxNtpPeersPeerVRtrID_Type())
tmnxNtpPeersPeerVRtrID.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpPeersPeerVRtrID.setStatus(_B)
_TmnxNtpFilter_ObjectIdentity=ObjectIdentity
tmnxNtpFilter=_TmnxNtpFilter_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,38,4))
_TmnxNtpAuthKeys_ObjectIdentity=ObjectIdentity
tmnxNtpAuthKeys=_TmnxNtpAuthKeys_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,38,5))
_TmnxNtpAuthKeyTable_Object=MibTable
tmnxNtpAuthKeyTable=_TmnxNtpAuthKeyTable_Object((1,3,6,1,4,1,6527,3,1,2,38,5,1))
if mibBuilder.loadTexts:tmnxNtpAuthKeyTable.setStatus(_B)
_TmnxNtpAuthKeyEntry_Object=MibTableRow
tmnxNtpAuthKeyEntry=_TmnxNtpAuthKeyEntry_Object((1,3,6,1,4,1,6527,3,1,2,38,5,1,1))
tmnxNtpAuthKeyEntry.setIndexNames((0,_K,_L),(0,_A,_AG))
if mibBuilder.loadTexts:tmnxNtpAuthKeyEntry.setStatus(_B)
class _TmnxNtpAuthKeyId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TmnxNtpAuthKeyId_Type.__name__=_H
_TmnxNtpAuthKeyId_Object=MibTableColumn
tmnxNtpAuthKeyId=_TmnxNtpAuthKeyId_Object((1,3,6,1,4,1,6527,3,1,2,38,5,1,1,1),_TmnxNtpAuthKeyId_Type())
tmnxNtpAuthKeyId.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxNtpAuthKeyId.setStatus(_B)
_TmnxNtpAuthKeyEntryStatus_Type=RowStatus
_TmnxNtpAuthKeyEntryStatus_Object=MibTableColumn
tmnxNtpAuthKeyEntryStatus=_TmnxNtpAuthKeyEntryStatus_Object((1,3,6,1,4,1,6527,3,1,2,38,5,1,1,2),_TmnxNtpAuthKeyEntryStatus_Type())
tmnxNtpAuthKeyEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpAuthKeyEntryStatus.setStatus(_B)
_TmnxNtpAuthKeyLastChanged_Type=TimeStamp
_TmnxNtpAuthKeyLastChanged_Object=MibTableColumn
tmnxNtpAuthKeyLastChanged=_TmnxNtpAuthKeyLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,38,5,1,1,3),_TmnxNtpAuthKeyLastChanged_Type())
tmnxNtpAuthKeyLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpAuthKeyLastChanged.setStatus(_B)
class _TmnxNtpAuthKey_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TmnxNtpAuthKey_Type.__name__=_A0
_TmnxNtpAuthKey_Object=MibTableColumn
tmnxNtpAuthKey=_TmnxNtpAuthKey_Object((1,3,6,1,4,1,6527,3,1,2,38,5,1,1,4),_TmnxNtpAuthKey_Type())
tmnxNtpAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpAuthKey.setStatus(_B)
class _TmnxNtpAuthKeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('des',1),('messageDigest',2)))
_TmnxNtpAuthKeyType_Type.__name__=_I
_TmnxNtpAuthKeyType_Object=MibTableColumn
tmnxNtpAuthKeyType=_TmnxNtpAuthKeyType_Object((1,3,6,1,4,1,6527,3,1,2,38,5,1,1,5),_TmnxNtpAuthKeyType_Type())
tmnxNtpAuthKeyType.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpAuthKeyType.setStatus(_B)
_TmnxNtpNotifyObjs_ObjectIdentity=ObjectIdentity
tmnxNtpNotifyObjs=_TmnxNtpNotifyObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,38,6))
_TmnxNtpUTCOffset_Type=NTPSignedTimeValue
_TmnxNtpUTCOffset_Object=MibScalar
tmnxNtpUTCOffset=_TmnxNtpUTCOffset_Object((1,3,6,1,4,1,6527,3,1,2,38,6,1),_TmnxNtpUTCOffset_Type())
tmnxNtpUTCOffset.setMaxAccess(_j)
if mibBuilder.loadTexts:tmnxNtpUTCOffset.setStatus(_B)
if mibBuilder.loadTexts:tmnxNtpUTCOffset.setUnits(_i)
_TmnxNtpUTCOffsetThreshold_Type=NTPSignedTimeValue
_TmnxNtpUTCOffsetThreshold_Object=MibScalar
tmnxNtpUTCOffsetThreshold=_TmnxNtpUTCOffsetThreshold_Object((1,3,6,1,4,1,6527,3,1,2,38,6,2),_TmnxNtpUTCOffsetThreshold_Type())
tmnxNtpUTCOffsetThreshold.setMaxAccess(_j)
if mibBuilder.loadTexts:tmnxNtpUTCOffsetThreshold.setStatus(_B)
if mibBuilder.loadTexts:tmnxNtpUTCOffsetThreshold.setUnits(_i)
class _TmnxNtpAuthKeyFailType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('invalidAuthKeyType',1),('invalidAuthKey',2),('invalidAuthKeyId',3)))
_TmnxNtpAuthKeyFailType_Type.__name__=_I
_TmnxNtpAuthKeyFailType_Object=MibScalar
tmnxNtpAuthKeyFailType=_TmnxNtpAuthKeyFailType_Object((1,3,6,1,4,1,6527,3,1,2,38,6,3),_TmnxNtpAuthKeyFailType_Type())
tmnxNtpAuthKeyFailType.setMaxAccess(_j)
if mibBuilder.loadTexts:tmnxNtpAuthKeyFailType.setStatus(_B)
_TmnxNtpConfigs_ObjectIdentity=ObjectIdentity
tmnxNtpConfigs=_TmnxNtpConfigs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,38,7))
_TmnxNtpConfigTable_Object=MibTable
tmnxNtpConfigTable=_TmnxNtpConfigTable_Object((1,3,6,1,4,1,6527,3,1,2,38,7,1))
if mibBuilder.loadTexts:tmnxNtpConfigTable.setStatus(_B)
_TmnxNtpConfigEntry_Object=MibTableRow
tmnxNtpConfigEntry=_TmnxNtpConfigEntry_Object((1,3,6,1,4,1,6527,3,1,2,38,7,1,1))
tmnxNtpConfigEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:tmnxNtpConfigEntry.setStatus(_B)
_TmnxNtpConfigRowStatus_Type=RowStatus
_TmnxNtpConfigRowStatus_Object=MibTableColumn
tmnxNtpConfigRowStatus=_TmnxNtpConfigRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,38,7,1,1,1),_TmnxNtpConfigRowStatus_Type())
tmnxNtpConfigRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpConfigRowStatus.setStatus(_B)
class _TmnxNtpConfigAdminState_Type(TmnxAdminState):defaultValue=3
_TmnxNtpConfigAdminState_Type.__name__=_A2
_TmnxNtpConfigAdminState_Object=MibTableColumn
tmnxNtpConfigAdminState=_TmnxNtpConfigAdminState_Object((1,3,6,1,4,1,6527,3,1,2,38,7,1,1,2),_TmnxNtpConfigAdminState_Type())
tmnxNtpConfigAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpConfigAdminState.setStatus(_B)
class _TmnxNtpConfigServer_Type(TruthValue):defaultValue=1
_TmnxNtpConfigServer_Type.__name__=_G
_TmnxNtpConfigServer_Object=MibTableColumn
tmnxNtpConfigServer=_TmnxNtpConfigServer_Object((1,3,6,1,4,1,6527,3,1,2,38,7,1,1,3),_TmnxNtpConfigServer_Type())
tmnxNtpConfigServer.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpConfigServer.setStatus(_B)
class _TmnxNtpConfigServerAuthenticate_Type(TruthValue):defaultValue=2
_TmnxNtpConfigServerAuthenticate_Type.__name__=_G
_TmnxNtpConfigServerAuthenticate_Object=MibTableColumn
tmnxNtpConfigServerAuthenticate=_TmnxNtpConfigServerAuthenticate_Object((1,3,6,1,4,1,6527,3,1,2,38,7,1,1,4),_TmnxNtpConfigServerAuthenticate_Type())
tmnxNtpConfigServerAuthenticate.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpConfigServerAuthenticate.setStatus(_B)
class _TmnxNtpConfigAuthCheck_Type(TruthValue):defaultValue=1
_TmnxNtpConfigAuthCheck_Type.__name__=_G
_TmnxNtpConfigAuthCheck_Object=MibTableColumn
tmnxNtpConfigAuthCheck=_TmnxNtpConfigAuthCheck_Object((1,3,6,1,4,1,6527,3,1,2,38,7,1,1,5),_TmnxNtpConfigAuthCheck_Type())
tmnxNtpConfigAuthCheck.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxNtpConfigAuthCheck.setStatus(_B)
_TmnxNtpClientInfoTable_Object=MibTable
tmnxNtpClientInfoTable=_TmnxNtpClientInfoTable_Object((1,3,6,1,4,1,6527,3,1,2,38,7,2))
if mibBuilder.loadTexts:tmnxNtpClientInfoTable.setStatus(_B)
_TmnxNtpClientInfoEntry_Object=MibTableRow
tmnxNtpClientInfoEntry=_TmnxNtpClientInfoEntry_Object((1,3,6,1,4,1,6527,3,1,2,38,7,2,1))
tmnxNtpClientInfoEntry.setIndexNames((0,_K,_L),(0,_A,_AH),(0,_A,_AI))
if mibBuilder.loadTexts:tmnxNtpClientInfoEntry.setStatus(_B)
_TmnxNtpClientAddressType_Type=InetAddressType
_TmnxNtpClientAddressType_Object=MibTableColumn
tmnxNtpClientAddressType=_TmnxNtpClientAddressType_Object((1,3,6,1,4,1,6527,3,1,2,38,7,2,1,1),_TmnxNtpClientAddressType_Type())
tmnxNtpClientAddressType.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxNtpClientAddressType.setStatus(_B)
class _TmnxNtpClientAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TmnxNtpClientAddress_Type.__name__=_J
_TmnxNtpClientAddress_Object=MibTableColumn
tmnxNtpClientAddress=_TmnxNtpClientAddress_Object((1,3,6,1,4,1,6527,3,1,2,38,7,2,1,2),_TmnxNtpClientAddress_Type())
tmnxNtpClientAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:tmnxNtpClientAddress.setStatus(_B)
_TmnxNtpClientInfoLastRequestTime_Type=TimeStamp
_TmnxNtpClientInfoLastRequestTime_Object=MibTableColumn
tmnxNtpClientInfoLastRequestTime=_TmnxNtpClientInfoLastRequestTime_Object((1,3,6,1,4,1,6527,3,1,2,38,7,2,1,3),_TmnxNtpClientInfoLastRequestTime_Type())
tmnxNtpClientInfoLastRequestTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxNtpClientInfoLastRequestTime.setStatus(_B)
_TmnxNtpNotifyPrefix_ObjectIdentity=ObjectIdentity
tmnxNtpNotifyPrefix=_TmnxNtpNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,38))
_TmnxNtpNotifications_ObjectIdentity=ObjectIdentity
tmnxNtpNotifications=_TmnxNtpNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,38,0))
tmnxNtpGlobalGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,38,2,1))
tmnxNtpGlobalGroup.setObjects(*((_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_S),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:tmnxNtpGlobalGroup.setStatus(_E)
tmnxNtpBroadcastGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,38,2,2))
tmnxNtpBroadcastGroup.setObjects(*((_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ)))
if mibBuilder.loadTexts:tmnxNtpBroadcastGroup.setStatus(_B)
tmnxNtpMulticastGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,38,2,3))
tmnxNtpMulticastGroup.setObjects(*((_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:tmnxNtpMulticastGroup.setStatus(_B)
tmnxNtpServersGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,38,2,4))
tmnxNtpServersGroup.setObjects(*((_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah)))
if mibBuilder.loadTexts:tmnxNtpServersGroup.setStatus(_B)
tmnxNtpPeersGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,38,2,5))
tmnxNtpPeersGroup.setObjects(*((_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_T),(_A,_U),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az),(_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3),(_A,_V)))
if mibBuilder.loadTexts:tmnxNtpPeersGroup.setStatus(_B)
tmnxNtpAuthKeyGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,38,2,6))
tmnxNtpAuthKeyGroup.setObjects(*((_A,_B4),(_A,_B5),(_A,_B6),(_A,_B7)))
if mibBuilder.loadTexts:tmnxNtpAuthKeyGroup.setStatus(_B)
tmnxNtpNotifyObjsGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,38,2,8))
tmnxNtpNotifyObjsGroup.setObjects(*((_A,_W),(_A,_X),(_A,_w)))
if mibBuilder.loadTexts:tmnxNtpNotifyObjsGroup.setStatus(_B)
tmnxNtpObsoleteV8v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,38,2,13))
tmnxNtpObsoleteV8v0Group.setObjects(*((_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:tmnxNtpObsoleteV8v0Group.setStatus(_B)
tmnxNtpGlobalV8v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,38,2,14))
tmnxNtpGlobalV8v0Group.setObjects(*((_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_S)))
if mibBuilder.loadTexts:tmnxNtpGlobalV8v0Group.setStatus(_B)
tmnxNtpV8v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,38,2,15))
tmnxNtpV8v0Group.setObjects(*((_A,_B8),(_A,_B9),(_A,_BA),(_A,_BB),(_A,_BC),(_A,_BD)))
if mibBuilder.loadTexts:tmnxNtpV8v0Group.setStatus(_B)
tmnxNtpAuthMismatch=NotificationType((1,3,6,1,4,1,6527,3,1,3,38,0,1))
tmnxNtpAuthMismatch.setObjects(*((_A,_T),(_A,_U),(_A,_w),(_A,_V)))
if mibBuilder.loadTexts:tmnxNtpAuthMismatch.setStatus(_B)
tmnxNtpNoServersAvail=NotificationType((1,3,6,1,4,1,6527,3,1,3,38,0,2))
if mibBuilder.loadTexts:tmnxNtpNoServersAvail.setStatus(_B)
tmnxNtpServersAvail=NotificationType((1,3,6,1,4,1,6527,3,1,3,38,0,3))
if mibBuilder.loadTexts:tmnxNtpServersAvail.setStatus(_B)
tmnxNtpMaxFreqDftExceed=NotificationType((1,3,6,1,4,1,6527,3,1,3,38,0,4))
if mibBuilder.loadTexts:tmnxNtpMaxFreqDftExceed.setStatus(_E)
tmnxNtpUtcOffsetExThreshold=NotificationType((1,3,6,1,4,1,6527,3,1,3,38,0,5))
tmnxNtpUtcOffsetExThreshold.setObjects(*((_A,_W),(_A,_X)))
if mibBuilder.loadTexts:tmnxNtpUtcOffsetExThreshold.setStatus(_E)
tmnxNtpUtcOffsetInThreshold=NotificationType((1,3,6,1,4,1,6527,3,1,3,38,0,6))
tmnxNtpUtcOffsetInThreshold.setObjects(*((_A,_W),(_A,_X)))
if mibBuilder.loadTexts:tmnxNtpUtcOffsetInThreshold.setStatus(_E)
tmnxNtpOperChange=NotificationType((1,3,6,1,4,1,6527,3,1,3,38,0,7))
tmnxNtpOperChange.setObjects((_A,_S))
if mibBuilder.loadTexts:tmnxNtpOperChange.setStatus(_B)
tmnxNtpServerChange=NotificationType((1,3,6,1,4,1,6527,3,1,3,38,0,8))
tmnxNtpServerChange.setObjects(*((_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:tmnxNtpServerChange.setStatus(_B)
tmnxNtpNotificationGroup=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,38,2,7))
tmnxNtpNotificationGroup.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_x),(_A,_y),(_A,_c)))
if mibBuilder.loadTexts:tmnxNtpNotificationGroup.setStatus(_E)
tmnxNtpObsoleteNotificationV4v0Group=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,38,2,9))
tmnxNtpObsoleteNotificationV4v0Group.setObjects(*((_A,_x),(_A,_y)))
if mibBuilder.loadTexts:tmnxNtpObsoleteNotificationV4v0Group.setStatus(_B)
tmnxNtpNotificationV4v0Group=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,38,2,10))
tmnxNtpNotificationV4v0Group.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:tmnxNtpNotificationV4v0Group.setStatus(_E)
tmnxNtpNotificationV6v0Group=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,38,2,11))
tmnxNtpNotificationV6v0Group.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_c),(_A,_BE)))
if mibBuilder.loadTexts:tmnxNtpNotificationV6v0Group.setStatus(_B)
tmnxNtpObsoleteNotficatnV6v0Grp=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,38,2,12))
tmnxNtpObsoleteNotficatnV6v0Grp.setObjects((_A,_b))
if mibBuilder.loadTexts:tmnxNtpObsoleteNotficatnV6v0Grp.setStatus(_B)
tmnxNtpCompliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,38,1,1))
tmnxNtpCompliance.setObjects(*((_A,_d),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_BF)))
if mibBuilder.loadTexts:tmnxNtpCompliance.setStatus(_E)
tmnxNtpV4v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,38,1,2))
tmnxNtpV4v0Compliance.setObjects(*((_A,_d),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_BG)))
if mibBuilder.loadTexts:tmnxNtpV4v0Compliance.setStatus(_E)
tmnxNtpV6v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,38,1,3))
tmnxNtpV6v0Compliance.setObjects(*((_A,_d),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_z)))
if mibBuilder.loadTexts:tmnxNtpV6v0Compliance.setStatus(_E)
tmnxNtpV8v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,38,1,4))
tmnxNtpV8v0Compliance.setObjects(*((_A,_BH),(_A,_BI),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_z)))
if mibBuilder.loadTexts:tmnxNtpV8v0Compliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'NTPTimeStamp':NTPTimeStamp,'NTPLeapIndicator':NTPLeapIndicator,'NTPSignedTimeValue':NTPSignedTimeValue,'NTPUnsignedTimeValue':NTPUnsignedTimeValue,'NTPStratum':NTPStratum,'NTPRefId':NTPRefId,'NTPPollInterval':NTPPollInterval,'NTPAssocIdentifier':NTPAssocIdentifier,_g:NTPVersion,_h:NTPVersionPeerServer,'TmnxNtpDirection':TmnxNtpDirection,'timetraNtpMIBModule':timetraNtpMIBModule,'tmnxNtpConformance':tmnxNtpConformance,'tmnxNtpCompliances':tmnxNtpCompliances,'tmnxNtpCompliance':tmnxNtpCompliance,'tmnxNtpV4v0Compliance':tmnxNtpV4v0Compliance,'tmnxNtpV6v0Compliance':tmnxNtpV6v0Compliance,'tmnxNtpV8v0Compliance':tmnxNtpV8v0Compliance,'tmnxNtpGroups':tmnxNtpGroups,_d:tmnxNtpGlobalGroup,_N:tmnxNtpBroadcastGroup,_O:tmnxNtpMulticastGroup,_P:tmnxNtpServersGroup,_Q:tmnxNtpPeersGroup,_R:tmnxNtpAuthKeyGroup,_BF:tmnxNtpNotificationGroup,'tmnxNtpNotifyObjsGroup':tmnxNtpNotifyObjsGroup,'tmnxNtpObsoleteNotificationV4v0Group':tmnxNtpObsoleteNotificationV4v0Group,_BG:tmnxNtpNotificationV4v0Group,_z:tmnxNtpNotificationV6v0Group,'tmnxNtpObsoleteNotficatnV6v0Grp':tmnxNtpObsoleteNotficatnV6v0Grp,'tmnxNtpObsoleteV8v0Group':tmnxNtpObsoleteV8v0Group,_BH:tmnxNtpGlobalV8v0Group,_BI:tmnxNtpV8v0Group,'tmnxNtpObjs':tmnxNtpObjs,'tmnxNtpSysObjs':tmnxNtpSysObjs,'tmnxNtpSystem':tmnxNtpSystem,_k:tmnxNtpSysLeap,_l:tmnxNtpSysStratum,_m:tmnxNtpSysRefId,_n:tmnxNtpSysRefTime,_o:tmnxNtpSysPoll,_p:tmnxNtpSysPeer,_q:tmnxNtpSysClock,_r:tmnxNtp,_s:tmnxNtpAdminState,_S:tmnxNtpOperState,_t:tmnxNtpServer,_u:tmnxNtpServerKeyId,_v:tmnxNtpAuthCheck,'tmnxNtpBroadcastTable':tmnxNtpBroadcastTable,'tmnxNtpBroadcastEntry':tmnxNtpBroadcastEntry,_A5:tmnxNtpBroadcastDirection,_A6:tmnxNtpBroadcastIfIndex,_AJ:tmnxNtpBroadcastEntryStatus,_AK:tmnxNtpBroadcastLastChanged,_AL:tmnxNtpBroadcastAuthKeyId,_AM:tmnxNtpBroadcastVersion,_AN:tmnxNtpBroadcastTtl,_AO:tmnxNtpBroadcastAuthErrs,_AP:tmnxNtpBroadcastAuthenticate,_AQ:tmnxNtpBroadcastAssocId,'tmnxNtpMulticastTable':tmnxNtpMulticastTable,'tmnxNtpMulticastEntry':tmnxNtpMulticastEntry,_A7:tmnxNtpMulticastDirection,_A8:tmnxNtpMulticastIfIndex,_AR:tmnxNtpMulticastAddressType,_AS:tmnxNtpMulticastAddress,_AT:tmnxNtpMulticastEntryStatus,_AU:tmnxNtpMulticastLastChanged,_AV:tmnxNtpMulticastAuthKeyId,_AW:tmnxNtpMulticastVersion,_AX:tmnxNtpMulticastTtl,_AY:tmnxNtpMulticastAuthErrs,_AZ:tmnxNtpMulticastAuthenticate,_Aa:tmnxNtpMulticastAssocId,'tmnxNtpServers':tmnxNtpServers,'tmnxNtpServersTable':tmnxNtpServersTable,'tmnxNtpServersEntry':tmnxNtpServersEntry,_A9:tmnxNtpServersAddrType,_AA:tmnxNtpServersAddress,_Ab:tmnxNtpServersEntryStatus,_Ac:tmnxNtpServersLastChanged,_Ad:tmnxNtpServersAuthKeyId,_Ae:tmnxNtpServersVersion,_Af:tmnxNtpServersPrefer,_Ag:tmnxNtpServersAssocId,_Ah:tmnxNtpServersAuthErrs,'tmnxNtpPeers':tmnxNtpPeers,'tmnxNtpPeersTable':tmnxNtpPeersTable,'tmnxNtpPeersEntry':tmnxNtpPeersEntry,_AB:tmnxNtpPeersAddrType,_AC:tmnxNtpPeersAddress,_Ai:tmnxNtpPeersEntryStatus,_Aj:tmnxNtpPeersLastChanged,_Ak:tmnxNtpPeersAuthKeyId,_Al:tmnxNtpPeersVersion,_Am:tmnxNtpPeersPrefer,_An:tmnxNtpPeersAssocId,_Ao:tmnxNtpPeersAuthErrs,'tmnxNtpPeersVarTable':tmnxNtpPeersVarTable,'tmnxNtpPeersVarEntry':tmnxNtpPeersVarEntry,_AD:tmnxNtpPeersVarAssocId,_Ap:tmnxNtpPeersConfigured,_T:tmnxNtpPeersPeerAddrType,_U:tmnxNtpPeersPeerAddress,_Aq:tmnxNtpPeersPeerPort,_Ar:tmnxNtpPeersHostAddrType,_As:tmnxNtpPeersHostAddress,_At:tmnxNtpPeersHostPort,_Au:tmnxNtpPeersMode,_Av:tmnxNtpPeersStratum,_Aw:tmnxNtpPeersPeerPoll,_Ax:tmnxNtpPeersHostPoll,_Ay:tmnxNtpPeersRefId,_Az:tmnxNtpPeersReceiveTime,_A_:tmnxNtpPeersReach,_B0:tmnxNtpPeersOffset,_B1:tmnxNtpPeersPrefPeer,_B2:tmnxNtpPeersStatus,_B3:tmnxNtpPeersStatusFlags,_V:tmnxNtpPeersPeerVRtrID,'tmnxNtpFilter':tmnxNtpFilter,'tmnxNtpAuthKeys':tmnxNtpAuthKeys,'tmnxNtpAuthKeyTable':tmnxNtpAuthKeyTable,'tmnxNtpAuthKeyEntry':tmnxNtpAuthKeyEntry,_AG:tmnxNtpAuthKeyId,_B4:tmnxNtpAuthKeyEntryStatus,_B5:tmnxNtpAuthKeyLastChanged,_B6:tmnxNtpAuthKey,_B7:tmnxNtpAuthKeyType,'tmnxNtpNotifyObjs':tmnxNtpNotifyObjs,_W:tmnxNtpUTCOffset,_X:tmnxNtpUTCOffsetThreshold,_w:tmnxNtpAuthKeyFailType,'tmnxNtpConfigs':tmnxNtpConfigs,'tmnxNtpConfigTable':tmnxNtpConfigTable,'tmnxNtpConfigEntry':tmnxNtpConfigEntry,_B8:tmnxNtpConfigRowStatus,_B9:tmnxNtpConfigAdminState,_BA:tmnxNtpConfigServer,_BB:tmnxNtpConfigServerAuthenticate,_BC:tmnxNtpConfigAuthCheck,'tmnxNtpClientInfoTable':tmnxNtpClientInfoTable,'tmnxNtpClientInfoEntry':tmnxNtpClientInfoEntry,_AH:tmnxNtpClientAddressType,_AI:tmnxNtpClientAddress,_BD:tmnxNtpClientInfoLastRequestTime,'tmnxNtpNotifyPrefix':tmnxNtpNotifyPrefix,'tmnxNtpNotifications':tmnxNtpNotifications,_Y:tmnxNtpAuthMismatch,_Z:tmnxNtpNoServersAvail,_a:tmnxNtpServersAvail,_b:tmnxNtpMaxFreqDftExceed,_x:tmnxNtpUtcOffsetExThreshold,_y:tmnxNtpUtcOffsetInThreshold,_c:tmnxNtpOperChange,_BE:tmnxNtpServerChange})