_AP='myClientProbeGroup'
_AO='myAuthModeMIBGroup'
_AN='myAuthAddrMIBGroup'
_AM='myAAAServerMIBGroup'
_AL='myDot1xAuthMIBGroup'
_AK='myClientProbeAliveInteval'
_AJ='myClientProbeHelloInterval'
_AI='myClientProbeEnabledStatus'
_AH='myIpAuthorizationMode'
_AG='myAuthUserStatus'
_AF='myAuthUserPort'
_AE='myAuthUserIpAddr'
_AD='myAuthUserSessionId'
_AC='myAuthUserName'
_AB='myAuthAddrStatus'
_AA='myAAAServerConfigRowStatus'
_A9='myAAAServerConfigKeyStr'
_A8='myAAAServerConfigAcctPort'
_A7='myAAAServerConfigAuthPort'
_A6='myAAAServerConfigAddress'
_A5='myAAAServerConfigAddressType'
_A4='myAAAServerTacplusKeyStr'
_A3='myAAAServerRadiusKeyStr'
_A2='myAAAServerAcctPort'
_A1='myAAAServerAuthPort'
_A0='myAuthenticationMode'
_z='myAuthIfStatus'
_y='myDot1xAuthObjectsMaxReauth'
_x='myDot1xCurrentAuthenticatedUserNumber'
_w='myDot1xCurrentUserNumber'
_v='myDot1xAuthObjectsLastEapolFrameSource'
_u='myDot1xAuthObjectsLastEapolFrameVersion'
_t='myDot1xAuthObjectsEapLengthErrorFramesRx'
_s='myDot1xAuthObjectsInvalidEapolFramesRx'
_r='myDot1xAuthObjectsEapolReqFramesTx'
_q='myDot1xAuthObjectsEapolReqIdFramesTx'
_p='myDot1xAuthObjectsEapolRespFramesRx'
_o='myDot1xAuthObjectsEapolRespIdFramesRx'
_n='myDot1xAuthObjectsEapolLogoffFramesRx'
_m='myDot1xAuthObjectsEapolMyFramesRx'
_l='myDot1xAuthObjectsEapolFramesTx'
_k='myDot1xAuthObjectsEapolFramesRx'
_j='myDot1xAuthObjectsIfIndex'
_i='myDot1xAuthObjectsKeyTxEnabled'
_h='myDot1xAuthObjectsAuthControlledPortStatus'
_g='myDot1xAuthObjectsBackendAuthState'
_f='myDot1xAuthObjectsPaeState'
_e='myDot1xAuthObjectsReAuthEnable'
_d='myDot1xAuthObjectsReAuthPeriod'
_c='myDot1xAuthObjectsMaxReq'
_b='myDot1xAuthObjectsServerTimeout'
_a='myDot1xAuthObjectsSuppTimeout'
_Z='myDot1xAuthObjectsTxPeriod'
_Y='myDot1xAuthObjectsQuietPeriod'
_X='myDot1xAuthStatus'
_W='not-accessible'
_V='myAAAServerConfigIndex'
_U='myAAAServerConfigProtocol'
_T='myDot1xIfUserMaxIndex'
_S='initialize'
_R='myAuthUserMacAddress'
_Q='myAuthUserFdbId'
_P='myAuthMacAddress'
_O='myAuthPort'
_N='myAuthIf'
_M='myDot1xAuthObjectsStatsAddr'
_L='myDot1xAuthObjectsStatsFdbId'
_K='myDot1xAuthObjectsConfigAddr'
_J='myDot1xAuthObjectsConfigFdbId'
_I='DisplayString'
_H='EnabledStatus'
_G='read-create'
_F='Unsigned32'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='DES7200-AAA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('DES7200-SMI','myMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('DES7200-TC','ConfigStatus','IfIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_H)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
myAAAMIB=ModuleIdentity((1,3,6,1,4,1,171,10,97,2,19))
if mibBuilder.loadTexts:myAAAMIB.setRevisions(('2002-03-20 00:00',))
_MyAAAMIBObjects_ObjectIdentity=ObjectIdentity
myAAAMIBObjects=_MyAAAMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,19,1))
_MyDot1xAuthObjects_ObjectIdentity=ObjectIdentity
myDot1xAuthObjects=_MyDot1xAuthObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,19,1,1))
class _MyDot1xAuthStatus_Type(EnabledStatus):defaultValue=2
_MyDot1xAuthStatus_Type.__name__=_H
_MyDot1xAuthStatus_Object=MibScalar
myDot1xAuthStatus=_MyDot1xAuthStatus_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,1),_MyDot1xAuthStatus_Type())
myDot1xAuthStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAuthStatus.setStatus(_A)
class _MyDot1xAuthObjectsQuietPeriod_Type(Unsigned32):defaultValue=60
_MyDot1xAuthObjectsQuietPeriod_Type.__name__=_F
_MyDot1xAuthObjectsQuietPeriod_Object=MibScalar
myDot1xAuthObjectsQuietPeriod=_MyDot1xAuthObjectsQuietPeriod_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,2),_MyDot1xAuthObjectsQuietPeriod_Type())
myDot1xAuthObjectsQuietPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAuthObjectsQuietPeriod.setStatus(_A)
class _MyDot1xAuthObjectsTxPeriod_Type(Unsigned32):defaultValue=30
_MyDot1xAuthObjectsTxPeriod_Type.__name__=_F
_MyDot1xAuthObjectsTxPeriod_Object=MibScalar
myDot1xAuthObjectsTxPeriod=_MyDot1xAuthObjectsTxPeriod_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,3),_MyDot1xAuthObjectsTxPeriod_Type())
myDot1xAuthObjectsTxPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAuthObjectsTxPeriod.setStatus(_A)
class _MyDot1xAuthObjectsSuppTimeout_Type(Unsigned32):defaultValue=30
_MyDot1xAuthObjectsSuppTimeout_Type.__name__=_F
_MyDot1xAuthObjectsSuppTimeout_Object=MibScalar
myDot1xAuthObjectsSuppTimeout=_MyDot1xAuthObjectsSuppTimeout_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,4),_MyDot1xAuthObjectsSuppTimeout_Type())
myDot1xAuthObjectsSuppTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAuthObjectsSuppTimeout.setStatus(_A)
class _MyDot1xAuthObjectsServerTimeout_Type(Unsigned32):defaultValue=30
_MyDot1xAuthObjectsServerTimeout_Type.__name__=_F
_MyDot1xAuthObjectsServerTimeout_Object=MibScalar
myDot1xAuthObjectsServerTimeout=_MyDot1xAuthObjectsServerTimeout_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,5),_MyDot1xAuthObjectsServerTimeout_Type())
myDot1xAuthObjectsServerTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAuthObjectsServerTimeout.setStatus(_A)
class _MyDot1xAuthObjectsMaxReq_Type(Unsigned32):defaultValue=2
_MyDot1xAuthObjectsMaxReq_Type.__name__=_F
_MyDot1xAuthObjectsMaxReq_Object=MibScalar
myDot1xAuthObjectsMaxReq=_MyDot1xAuthObjectsMaxReq_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,6),_MyDot1xAuthObjectsMaxReq_Type())
myDot1xAuthObjectsMaxReq.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAuthObjectsMaxReq.setStatus(_A)
class _MyDot1xAuthObjectsReAuthPeriod_Type(Unsigned32):defaultValue=3600
_MyDot1xAuthObjectsReAuthPeriod_Type.__name__=_F
_MyDot1xAuthObjectsReAuthPeriod_Object=MibScalar
myDot1xAuthObjectsReAuthPeriod=_MyDot1xAuthObjectsReAuthPeriod_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,7),_MyDot1xAuthObjectsReAuthPeriod_Type())
myDot1xAuthObjectsReAuthPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAuthObjectsReAuthPeriod.setStatus(_A)
class _MyDot1xAuthObjectsMaxReauth_Type(Unsigned32):defaultValue=2
_MyDot1xAuthObjectsMaxReauth_Type.__name__=_F
_MyDot1xAuthObjectsMaxReauth_Object=MibScalar
myDot1xAuthObjectsMaxReauth=_MyDot1xAuthObjectsMaxReauth_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,8),_MyDot1xAuthObjectsMaxReauth_Type())
myDot1xAuthObjectsMaxReauth.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAuthObjectsMaxReauth.setStatus(_A)
class _MyDot1xAuthObjectsReAuthEnable_Type(EnabledStatus):defaultValue=2
_MyDot1xAuthObjectsReAuthEnable_Type.__name__=_H
_MyDot1xAuthObjectsReAuthEnable_Object=MibScalar
myDot1xAuthObjectsReAuthEnable=_MyDot1xAuthObjectsReAuthEnable_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,9),_MyDot1xAuthObjectsReAuthEnable_Type())
myDot1xAuthObjectsReAuthEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAuthObjectsReAuthEnable.setStatus(_A)
_MyDot1xAuthObjectsConfigTable_Object=MibTable
myDot1xAuthObjectsConfigTable=_MyDot1xAuthObjectsConfigTable_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,10))
if mibBuilder.loadTexts:myDot1xAuthObjectsConfigTable.setStatus(_A)
_MyDot1xAuthObjectsConfigEntry_Object=MibTableRow
myDot1xAuthObjectsConfigEntry=_MyDot1xAuthObjectsConfigEntry_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,10,1))
myDot1xAuthObjectsConfigEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:myDot1xAuthObjectsConfigEntry.setStatus(_A)
_MyDot1xAuthObjectsConfigFdbId_Type=Unsigned32
_MyDot1xAuthObjectsConfigFdbId_Object=MibTableColumn
myDot1xAuthObjectsConfigFdbId=_MyDot1xAuthObjectsConfigFdbId_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,10,1,1),_MyDot1xAuthObjectsConfigFdbId_Type())
myDot1xAuthObjectsConfigFdbId.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsConfigFdbId.setStatus(_A)
_MyDot1xAuthObjectsConfigAddr_Type=MacAddress
_MyDot1xAuthObjectsConfigAddr_Object=MibTableColumn
myDot1xAuthObjectsConfigAddr=_MyDot1xAuthObjectsConfigAddr_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,10,1,2),_MyDot1xAuthObjectsConfigAddr_Type())
myDot1xAuthObjectsConfigAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsConfigAddr.setStatus(_A)
class _MyDot1xAuthObjectsPaeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_S,1),('disconnected',2),('connecting',3),('authenticating',4),('authenticated',5),('aborting',6),('held',7),('forceAuth',8),('forceUnauth',9)))
_MyDot1xAuthObjectsPaeState_Type.__name__=_E
_MyDot1xAuthObjectsPaeState_Object=MibTableColumn
myDot1xAuthObjectsPaeState=_MyDot1xAuthObjectsPaeState_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,10,1,3),_MyDot1xAuthObjectsPaeState_Type())
myDot1xAuthObjectsPaeState.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsPaeState.setStatus(_A)
class _MyDot1xAuthObjectsBackendAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('request',1),('response',2),('success',3),('fail',4),('timeout',5),('idle',6),(_S,7)))
_MyDot1xAuthObjectsBackendAuthState_Type.__name__=_E
_MyDot1xAuthObjectsBackendAuthState_Object=MibTableColumn
myDot1xAuthObjectsBackendAuthState=_MyDot1xAuthObjectsBackendAuthState_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,10,1,4),_MyDot1xAuthObjectsBackendAuthState_Type())
myDot1xAuthObjectsBackendAuthState.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsBackendAuthState.setStatus(_A)
class _MyDot1xAuthObjectsAuthControlledPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('authorized',1),('unauthorized',2)))
_MyDot1xAuthObjectsAuthControlledPortStatus_Type.__name__=_E
_MyDot1xAuthObjectsAuthControlledPortStatus_Object=MibTableColumn
myDot1xAuthObjectsAuthControlledPortStatus=_MyDot1xAuthObjectsAuthControlledPortStatus_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,10,1,5),_MyDot1xAuthObjectsAuthControlledPortStatus_Type())
myDot1xAuthObjectsAuthControlledPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsAuthControlledPortStatus.setStatus(_A)
_MyDot1xAuthObjectsKeyTxEnabled_Type=TruthValue
_MyDot1xAuthObjectsKeyTxEnabled_Object=MibTableColumn
myDot1xAuthObjectsKeyTxEnabled=_MyDot1xAuthObjectsKeyTxEnabled_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,10,1,6),_MyDot1xAuthObjectsKeyTxEnabled_Type())
myDot1xAuthObjectsKeyTxEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsKeyTxEnabled.setStatus(_A)
_MyDot1xAuthObjectsIfIndex_Type=IfIndex
_MyDot1xAuthObjectsIfIndex_Object=MibTableColumn
myDot1xAuthObjectsIfIndex=_MyDot1xAuthObjectsIfIndex_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,10,1,7),_MyDot1xAuthObjectsIfIndex_Type())
myDot1xAuthObjectsIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsIfIndex.setStatus(_A)
_MyDot1xAuthObjectsStatsTable_Object=MibTable
myDot1xAuthObjectsStatsTable=_MyDot1xAuthObjectsStatsTable_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,11))
if mibBuilder.loadTexts:myDot1xAuthObjectsStatsTable.setStatus(_A)
_MyDot1xAuthStatsEntry_Object=MibTableRow
myDot1xAuthStatsEntry=_MyDot1xAuthStatsEntry_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,11,1))
myDot1xAuthStatsEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:myDot1xAuthStatsEntry.setStatus(_A)
_MyDot1xAuthObjectsStatsFdbId_Type=Unsigned32
_MyDot1xAuthObjectsStatsFdbId_Object=MibTableColumn
myDot1xAuthObjectsStatsFdbId=_MyDot1xAuthObjectsStatsFdbId_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,11,1,1),_MyDot1xAuthObjectsStatsFdbId_Type())
myDot1xAuthObjectsStatsFdbId.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsStatsFdbId.setStatus(_A)
_MyDot1xAuthObjectsStatsAddr_Type=MacAddress
_MyDot1xAuthObjectsStatsAddr_Object=MibTableColumn
myDot1xAuthObjectsStatsAddr=_MyDot1xAuthObjectsStatsAddr_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,11,1,2),_MyDot1xAuthObjectsStatsAddr_Type())
myDot1xAuthObjectsStatsAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsStatsAddr.setStatus(_A)
_MyDot1xAuthObjectsEapolFramesRx_Type=Counter32
_MyDot1xAuthObjectsEapolFramesRx_Object=MibTableColumn
myDot1xAuthObjectsEapolFramesRx=_MyDot1xAuthObjectsEapolFramesRx_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,11,1,3),_MyDot1xAuthObjectsEapolFramesRx_Type())
myDot1xAuthObjectsEapolFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsEapolFramesRx.setStatus(_A)
_MyDot1xAuthObjectsEapolFramesTx_Type=Counter32
_MyDot1xAuthObjectsEapolFramesTx_Object=MibTableColumn
myDot1xAuthObjectsEapolFramesTx=_MyDot1xAuthObjectsEapolFramesTx_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,11,1,4),_MyDot1xAuthObjectsEapolFramesTx_Type())
myDot1xAuthObjectsEapolFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsEapolFramesTx.setStatus(_A)
_MyDot1xAuthObjectsEapolMyFramesRx_Type=Counter32
_MyDot1xAuthObjectsEapolMyFramesRx_Object=MibTableColumn
myDot1xAuthObjectsEapolMyFramesRx=_MyDot1xAuthObjectsEapolMyFramesRx_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,11,1,5),_MyDot1xAuthObjectsEapolMyFramesRx_Type())
myDot1xAuthObjectsEapolMyFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsEapolMyFramesRx.setStatus(_A)
_MyDot1xAuthObjectsEapolLogoffFramesRx_Type=Counter32
_MyDot1xAuthObjectsEapolLogoffFramesRx_Object=MibTableColumn
myDot1xAuthObjectsEapolLogoffFramesRx=_MyDot1xAuthObjectsEapolLogoffFramesRx_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,11,1,6),_MyDot1xAuthObjectsEapolLogoffFramesRx_Type())
myDot1xAuthObjectsEapolLogoffFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsEapolLogoffFramesRx.setStatus(_A)
_MyDot1xAuthObjectsEapolRespIdFramesRx_Type=Counter32
_MyDot1xAuthObjectsEapolRespIdFramesRx_Object=MibTableColumn
myDot1xAuthObjectsEapolRespIdFramesRx=_MyDot1xAuthObjectsEapolRespIdFramesRx_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,11,1,7),_MyDot1xAuthObjectsEapolRespIdFramesRx_Type())
myDot1xAuthObjectsEapolRespIdFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsEapolRespIdFramesRx.setStatus(_A)
_MyDot1xAuthObjectsEapolRespFramesRx_Type=Counter32
_MyDot1xAuthObjectsEapolRespFramesRx_Object=MibTableColumn
myDot1xAuthObjectsEapolRespFramesRx=_MyDot1xAuthObjectsEapolRespFramesRx_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,11,1,8),_MyDot1xAuthObjectsEapolRespFramesRx_Type())
myDot1xAuthObjectsEapolRespFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsEapolRespFramesRx.setStatus(_A)
_MyDot1xAuthObjectsEapolReqIdFramesTx_Type=Counter32
_MyDot1xAuthObjectsEapolReqIdFramesTx_Object=MibTableColumn
myDot1xAuthObjectsEapolReqIdFramesTx=_MyDot1xAuthObjectsEapolReqIdFramesTx_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,11,1,9),_MyDot1xAuthObjectsEapolReqIdFramesTx_Type())
myDot1xAuthObjectsEapolReqIdFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsEapolReqIdFramesTx.setStatus(_A)
_MyDot1xAuthObjectsEapolReqFramesTx_Type=Counter32
_MyDot1xAuthObjectsEapolReqFramesTx_Object=MibTableColumn
myDot1xAuthObjectsEapolReqFramesTx=_MyDot1xAuthObjectsEapolReqFramesTx_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,11,1,10),_MyDot1xAuthObjectsEapolReqFramesTx_Type())
myDot1xAuthObjectsEapolReqFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsEapolReqFramesTx.setStatus(_A)
_MyDot1xAuthObjectsInvalidEapolFramesRx_Type=Counter32
_MyDot1xAuthObjectsInvalidEapolFramesRx_Object=MibTableColumn
myDot1xAuthObjectsInvalidEapolFramesRx=_MyDot1xAuthObjectsInvalidEapolFramesRx_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,11,1,11),_MyDot1xAuthObjectsInvalidEapolFramesRx_Type())
myDot1xAuthObjectsInvalidEapolFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsInvalidEapolFramesRx.setStatus(_A)
_MyDot1xAuthObjectsEapLengthErrorFramesRx_Type=Counter32
_MyDot1xAuthObjectsEapLengthErrorFramesRx_Object=MibTableColumn
myDot1xAuthObjectsEapLengthErrorFramesRx=_MyDot1xAuthObjectsEapLengthErrorFramesRx_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,11,1,12),_MyDot1xAuthObjectsEapLengthErrorFramesRx_Type())
myDot1xAuthObjectsEapLengthErrorFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsEapLengthErrorFramesRx.setStatus(_A)
_MyDot1xAuthObjectsLastEapolFrameVersion_Type=Unsigned32
_MyDot1xAuthObjectsLastEapolFrameVersion_Object=MibTableColumn
myDot1xAuthObjectsLastEapolFrameVersion=_MyDot1xAuthObjectsLastEapolFrameVersion_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,11,1,13),_MyDot1xAuthObjectsLastEapolFrameVersion_Type())
myDot1xAuthObjectsLastEapolFrameVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsLastEapolFrameVersion.setStatus(_A)
_MyDot1xAuthObjectsLastEapolFrameSource_Type=MacAddress
_MyDot1xAuthObjectsLastEapolFrameSource_Object=MibTableColumn
myDot1xAuthObjectsLastEapolFrameSource=_MyDot1xAuthObjectsLastEapolFrameSource_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,11,1,14),_MyDot1xAuthObjectsLastEapolFrameSource_Type())
myDot1xAuthObjectsLastEapolFrameSource.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsLastEapolFrameSource.setStatus(_A)
_MyDot1xCurrentUserNumber_Type=Counter32
_MyDot1xCurrentUserNumber_Object=MibScalar
myDot1xCurrentUserNumber=_MyDot1xCurrentUserNumber_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,12),_MyDot1xCurrentUserNumber_Type())
myDot1xCurrentUserNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xCurrentUserNumber.setStatus(_A)
_MyDot1xCurrentAuthenticatedUserNumber_Type=Counter32
_MyDot1xCurrentAuthenticatedUserNumber_Object=MibScalar
myDot1xCurrentAuthenticatedUserNumber=_MyDot1xCurrentAuthenticatedUserNumber_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,13),_MyDot1xCurrentAuthenticatedUserNumber_Type())
myDot1xCurrentAuthenticatedUserNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xCurrentAuthenticatedUserNumber.setStatus(_A)
class _MyDot1xAccountStatus_Type(EnabledStatus):defaultValue=2
_MyDot1xAccountStatus_Type.__name__=_H
_MyDot1xAccountStatus_Object=MibScalar
myDot1xAccountStatus=_MyDot1xAccountStatus_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,14),_MyDot1xAccountStatus_Type())
myDot1xAccountStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAccountStatus.setStatus(_A)
_MyAuthIfTable_Object=MibTable
myAuthIfTable=_MyAuthIfTable_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,15))
if mibBuilder.loadTexts:myAuthIfTable.setStatus(_A)
_MyAuthIfEntry_Object=MibTableRow
myAuthIfEntry=_MyAuthIfEntry_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,15,1))
myAuthIfEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:myAuthIfEntry.setStatus(_A)
_MyAuthIf_Type=IfIndex
_MyAuthIf_Object=MibTableColumn
myAuthIf=_MyAuthIf_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,15,1,1),_MyAuthIf_Type())
myAuthIf.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthIf.setStatus(_A)
class _MyAuthIfStatus_Type(EnabledStatus):defaultValue=2
_MyAuthIfStatus_Type.__name__=_H
_MyAuthIfStatus_Object=MibTableColumn
myAuthIfStatus=_MyAuthIfStatus_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,15,1,2),_MyAuthIfStatus_Type())
myAuthIfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:myAuthIfStatus.setStatus(_A)
class _MyAuthenticationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eap-md5',1),('chap',2)))
_MyAuthenticationMode_Type.__name__=_E
_MyAuthenticationMode_Object=MibScalar
myAuthenticationMode=_MyAuthenticationMode_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,16),_MyAuthenticationMode_Type())
myAuthenticationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:myAuthenticationMode.setStatus(_A)
_MyDot1xAccountUpdateStatus_Type=EnabledStatus
_MyDot1xAccountUpdateStatus_Object=MibScalar
myDot1xAccountUpdateStatus=_MyDot1xAccountUpdateStatus_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,17),_MyDot1xAccountUpdateStatus_Type())
myDot1xAccountUpdateStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAccountUpdateStatus.setStatus(_A)
class _MyDot1xAcctInterimInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,65535))
_MyDot1xAcctInterimInterval_Type.__name__=_F
_MyDot1xAcctInterimInterval_Object=MibScalar
myDot1xAcctInterimInterval=_MyDot1xAcctInterimInterval_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,18),_MyDot1xAcctInterimInterval_Type())
myDot1xAcctInterimInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAcctInterimInterval.setStatus(_A)
_MyDot1xEapolTagEnabled_Type=EnabledStatus
_MyDot1xEapolTagEnabled_Object=MibScalar
myDot1xEapolTagEnabled=_MyDot1xEapolTagEnabled_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,19),_MyDot1xEapolTagEnabled_Type())
myDot1xEapolTagEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xEapolTagEnabled.setStatus(_A)
_MyDot1xIfUserMaxTable_Object=MibTable
myDot1xIfUserMaxTable=_MyDot1xIfUserMaxTable_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,20))
if mibBuilder.loadTexts:myDot1xIfUserMaxTable.setStatus(_A)
_MyDot1xIfUserMaxEntry_Object=MibTableRow
myDot1xIfUserMaxEntry=_MyDot1xIfUserMaxEntry_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,20,1))
myDot1xIfUserMaxEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:myDot1xIfUserMaxEntry.setStatus(_A)
_MyDot1xIfUserMaxIndex_Type=IfIndex
_MyDot1xIfUserMaxIndex_Object=MibTableColumn
myDot1xIfUserMaxIndex=_MyDot1xIfUserMaxIndex_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,20,1,1),_MyDot1xIfUserMaxIndex_Type())
myDot1xIfUserMaxIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xIfUserMaxIndex.setStatus(_A)
class _MyDot1xIfUserMaxNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4000))
_MyDot1xIfUserMaxNum_Type.__name__=_F
_MyDot1xIfUserMaxNum_Object=MibTableColumn
myDot1xIfUserMaxNum=_MyDot1xIfUserMaxNum_Object((1,3,6,1,4,1,171,10,97,2,19,1,1,20,1,2),_MyDot1xIfUserMaxNum_Type())
myDot1xIfUserMaxNum.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xIfUserMaxNum.setStatus(_A)
_MyAAAServerObjects_ObjectIdentity=ObjectIdentity
myAAAServerObjects=_MyAAAServerObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,19,1,2))
class _MyAAAServerAuthPort_Type(Integer32):defaultValue=1812;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MyAAAServerAuthPort_Type.__name__=_E
_MyAAAServerAuthPort_Object=MibScalar
myAAAServerAuthPort=_MyAAAServerAuthPort_Object((1,3,6,1,4,1,171,10,97,2,19,1,2,2),_MyAAAServerAuthPort_Type())
myAAAServerAuthPort.setMaxAccess(_D)
if mibBuilder.loadTexts:myAAAServerAuthPort.setStatus(_A)
class _MyAAAServerAcctPort_Type(Integer32):defaultValue=1813;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MyAAAServerAcctPort_Type.__name__=_E
_MyAAAServerAcctPort_Object=MibScalar
myAAAServerAcctPort=_MyAAAServerAcctPort_Object((1,3,6,1,4,1,171,10,97,2,19,1,2,3),_MyAAAServerAcctPort_Type())
myAAAServerAcctPort.setMaxAccess(_D)
if mibBuilder.loadTexts:myAAAServerAcctPort.setStatus(_A)
class _MyAAAServerRadiusKeyStr_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MyAAAServerRadiusKeyStr_Type.__name__=_I
_MyAAAServerRadiusKeyStr_Object=MibScalar
myAAAServerRadiusKeyStr=_MyAAAServerRadiusKeyStr_Object((1,3,6,1,4,1,171,10,97,2,19,1,2,4),_MyAAAServerRadiusKeyStr_Type())
myAAAServerRadiusKeyStr.setMaxAccess(_D)
if mibBuilder.loadTexts:myAAAServerRadiusKeyStr.setStatus(_A)
class _MyAAAServerTacplusKeyStr_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MyAAAServerTacplusKeyStr_Type.__name__=_I
_MyAAAServerTacplusKeyStr_Object=MibScalar
myAAAServerTacplusKeyStr=_MyAAAServerTacplusKeyStr_Object((1,3,6,1,4,1,171,10,97,2,19,1,2,8),_MyAAAServerTacplusKeyStr_Type())
myAAAServerTacplusKeyStr.setMaxAccess(_D)
if mibBuilder.loadTexts:myAAAServerTacplusKeyStr.setStatus(_A)
_MyAAAServerConfigTable_Object=MibTable
myAAAServerConfigTable=_MyAAAServerConfigTable_Object((1,3,6,1,4,1,171,10,97,2,19,1,2,9))
if mibBuilder.loadTexts:myAAAServerConfigTable.setStatus(_A)
_MyAAAServerConfigEntry_Object=MibTableRow
myAAAServerConfigEntry=_MyAAAServerConfigEntry_Object((1,3,6,1,4,1,171,10,97,2,19,1,2,9,1))
myAAAServerConfigEntry.setIndexNames((0,_B,_U),(0,_B,_V))
if mibBuilder.loadTexts:myAAAServerConfigEntry.setStatus(_A)
class _MyAAAServerConfigProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('radius',1),('tacplus',2)))
_MyAAAServerConfigProtocol_Type.__name__=_E
_MyAAAServerConfigProtocol_Object=MibTableColumn
myAAAServerConfigProtocol=_MyAAAServerConfigProtocol_Object((1,3,6,1,4,1,171,10,97,2,19,1,2,9,1,1),_MyAAAServerConfigProtocol_Type())
myAAAServerConfigProtocol.setMaxAccess(_W)
if mibBuilder.loadTexts:myAAAServerConfigProtocol.setStatus(_A)
class _MyAAAServerConfigIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_MyAAAServerConfigIndex_Type.__name__=_F
_MyAAAServerConfigIndex_Object=MibTableColumn
myAAAServerConfigIndex=_MyAAAServerConfigIndex_Object((1,3,6,1,4,1,171,10,97,2,19,1,2,9,1,2),_MyAAAServerConfigIndex_Type())
myAAAServerConfigIndex.setMaxAccess(_W)
if mibBuilder.loadTexts:myAAAServerConfigIndex.setStatus(_A)
_MyAAAServerConfigAddressType_Type=InetAddressType
_MyAAAServerConfigAddressType_Object=MibTableColumn
myAAAServerConfigAddressType=_MyAAAServerConfigAddressType_Object((1,3,6,1,4,1,171,10,97,2,19,1,2,9,1,3),_MyAAAServerConfigAddressType_Type())
myAAAServerConfigAddressType.setMaxAccess(_G)
if mibBuilder.loadTexts:myAAAServerConfigAddressType.setStatus(_A)
_MyAAAServerConfigAddress_Type=InetAddress
_MyAAAServerConfigAddress_Object=MibTableColumn
myAAAServerConfigAddress=_MyAAAServerConfigAddress_Object((1,3,6,1,4,1,171,10,97,2,19,1,2,9,1,4),_MyAAAServerConfigAddress_Type())
myAAAServerConfigAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:myAAAServerConfigAddress.setStatus(_A)
class _MyAAAServerConfigAuthPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MyAAAServerConfigAuthPort_Type.__name__=_E
_MyAAAServerConfigAuthPort_Object=MibTableColumn
myAAAServerConfigAuthPort=_MyAAAServerConfigAuthPort_Object((1,3,6,1,4,1,171,10,97,2,19,1,2,9,1,5),_MyAAAServerConfigAuthPort_Type())
myAAAServerConfigAuthPort.setMaxAccess(_G)
if mibBuilder.loadTexts:myAAAServerConfigAuthPort.setStatus(_A)
class _MyAAAServerConfigAcctPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MyAAAServerConfigAcctPort_Type.__name__=_E
_MyAAAServerConfigAcctPort_Object=MibTableColumn
myAAAServerConfigAcctPort=_MyAAAServerConfigAcctPort_Object((1,3,6,1,4,1,171,10,97,2,19,1,2,9,1,6),_MyAAAServerConfigAcctPort_Type())
myAAAServerConfigAcctPort.setMaxAccess(_G)
if mibBuilder.loadTexts:myAAAServerConfigAcctPort.setStatus(_A)
class _MyAAAServerConfigKeyStr_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MyAAAServerConfigKeyStr_Type.__name__=_I
_MyAAAServerConfigKeyStr_Object=MibTableColumn
myAAAServerConfigKeyStr=_MyAAAServerConfigKeyStr_Object((1,3,6,1,4,1,171,10,97,2,19,1,2,9,1,7),_MyAAAServerConfigKeyStr_Type())
myAAAServerConfigKeyStr.setMaxAccess(_G)
if mibBuilder.loadTexts:myAAAServerConfigKeyStr.setStatus(_A)
_MyAAAServerConfigRowStatus_Type=RowStatus
_MyAAAServerConfigRowStatus_Object=MibTableColumn
myAAAServerConfigRowStatus=_MyAAAServerConfigRowStatus_Object((1,3,6,1,4,1,171,10,97,2,19,1,2,9,1,8),_MyAAAServerConfigRowStatus_Type())
myAAAServerConfigRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:myAAAServerConfigRowStatus.setStatus(_A)
_MyAuthUserObjects_ObjectIdentity=ObjectIdentity
myAuthUserObjects=_MyAuthUserObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,19,1,3))
_MyAuthAddrTable_Object=MibTable
myAuthAddrTable=_MyAuthAddrTable_Object((1,3,6,1,4,1,171,10,97,2,19,1,3,1))
if mibBuilder.loadTexts:myAuthAddrTable.setStatus(_A)
_MyAuthAddrEntry_Object=MibTableRow
myAuthAddrEntry=_MyAuthAddrEntry_Object((1,3,6,1,4,1,171,10,97,2,19,1,3,1,1))
myAuthAddrEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:myAuthAddrEntry.setStatus(_A)
_MyAuthPort_Type=IfIndex
_MyAuthPort_Object=MibTableColumn
myAuthPort=_MyAuthPort_Object((1,3,6,1,4,1,171,10,97,2,19,1,3,1,1,1),_MyAuthPort_Type())
myAuthPort.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthPort.setStatus(_A)
_MyAuthMacAddress_Type=MacAddress
_MyAuthMacAddress_Object=MibTableColumn
myAuthMacAddress=_MyAuthMacAddress_Object((1,3,6,1,4,1,171,10,97,2,19,1,3,1,1,2),_MyAuthMacAddress_Type())
myAuthMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthMacAddress.setStatus(_A)
class _MyAuthAddrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_MyAuthAddrStatus_Type.__name__=_E
_MyAuthAddrStatus_Object=MibTableColumn
myAuthAddrStatus=_MyAuthAddrStatus_Object((1,3,6,1,4,1,171,10,97,2,19,1,3,1,1,3),_MyAuthAddrStatus_Type())
myAuthAddrStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:myAuthAddrStatus.setStatus(_A)
_MyAuthUserTable_Object=MibTable
myAuthUserTable=_MyAuthUserTable_Object((1,3,6,1,4,1,171,10,97,2,19,1,3,2))
if mibBuilder.loadTexts:myAuthUserTable.setStatus(_A)
_MyAuthUserEntry_Object=MibTableRow
myAuthUserEntry=_MyAuthUserEntry_Object((1,3,6,1,4,1,171,10,97,2,19,1,3,2,1))
myAuthUserEntry.setIndexNames((0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:myAuthUserEntry.setStatus(_A)
_MyAuthUserFdbId_Type=Unsigned32
_MyAuthUserFdbId_Object=MibTableColumn
myAuthUserFdbId=_MyAuthUserFdbId_Object((1,3,6,1,4,1,171,10,97,2,19,1,3,2,1,1),_MyAuthUserFdbId_Type())
myAuthUserFdbId.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthUserFdbId.setStatus(_A)
_MyAuthUserMacAddress_Type=MacAddress
_MyAuthUserMacAddress_Object=MibTableColumn
myAuthUserMacAddress=_MyAuthUserMacAddress_Object((1,3,6,1,4,1,171,10,97,2,19,1,3,2,1,2),_MyAuthUserMacAddress_Type())
myAuthUserMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthUserMacAddress.setStatus(_A)
_MyAuthUserName_Type=DisplayString
_MyAuthUserName_Object=MibTableColumn
myAuthUserName=_MyAuthUserName_Object((1,3,6,1,4,1,171,10,97,2,19,1,3,2,1,3),_MyAuthUserName_Type())
myAuthUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthUserName.setStatus(_A)
_MyAuthUserSessionId_Type=DisplayString
_MyAuthUserSessionId_Object=MibTableColumn
myAuthUserSessionId=_MyAuthUserSessionId_Object((1,3,6,1,4,1,171,10,97,2,19,1,3,2,1,4),_MyAuthUserSessionId_Type())
myAuthUserSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthUserSessionId.setStatus(_A)
_MyAuthUserIpAddr_Type=IpAddress
_MyAuthUserIpAddr_Object=MibTableColumn
myAuthUserIpAddr=_MyAuthUserIpAddr_Object((1,3,6,1,4,1,171,10,97,2,19,1,3,2,1,5),_MyAuthUserIpAddr_Type())
myAuthUserIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthUserIpAddr.setStatus(_A)
_MyAuthUserPort_Type=Integer32
_MyAuthUserPort_Object=MibTableColumn
myAuthUserPort=_MyAuthUserPort_Object((1,3,6,1,4,1,171,10,97,2,19,1,3,2,1,6),_MyAuthUserPort_Type())
myAuthUserPort.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthUserPort.setStatus(_A)
_MyAuthUserStatus_Type=ConfigStatus
_MyAuthUserStatus_Object=MibTableColumn
myAuthUserStatus=_MyAuthUserStatus_Object((1,3,6,1,4,1,171,10,97,2,19,1,3,2,1,7),_MyAuthUserStatus_Type())
myAuthUserStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:myAuthUserStatus.setStatus(_A)
class _MyAuthUserForVPNDel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_MyAuthUserForVPNDel_Type.__name__=_I
_MyAuthUserForVPNDel_Object=MibScalar
myAuthUserForVPNDel=_MyAuthUserForVPNDel_Object((1,3,6,1,4,1,171,10,97,2,19,1,3,3),_MyAuthUserForVPNDel_Type())
myAuthUserForVPNDel.setMaxAccess(_D)
if mibBuilder.loadTexts:myAuthUserForVPNDel.setStatus(_A)
_MyAuthModeObjects_ObjectIdentity=ObjectIdentity
myAuthModeObjects=_MyAuthModeObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,19,1,4))
class _MyIpAuthorizationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('disable',1),('dhcpServer',2),('radiusServer',3),('supplicant',4)))
_MyIpAuthorizationMode_Type.__name__=_E
_MyIpAuthorizationMode_Object=MibScalar
myIpAuthorizationMode=_MyIpAuthorizationMode_Object((1,3,6,1,4,1,171,10,97,2,19,1,4,1),_MyIpAuthorizationMode_Type())
myIpAuthorizationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:myIpAuthorizationMode.setStatus(_A)
_MyClientProbeObjects_ObjectIdentity=ObjectIdentity
myClientProbeObjects=_MyClientProbeObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,19,1,5))
_MyClientProbeEnabledStatus_Type=EnabledStatus
_MyClientProbeEnabledStatus_Object=MibScalar
myClientProbeEnabledStatus=_MyClientProbeEnabledStatus_Object((1,3,6,1,4,1,171,10,97,2,19,1,5,1),_MyClientProbeEnabledStatus_Type())
myClientProbeEnabledStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:myClientProbeEnabledStatus.setStatus(_A)
_MyClientProbeHelloInterval_Type=Unsigned32
_MyClientProbeHelloInterval_Object=MibScalar
myClientProbeHelloInterval=_MyClientProbeHelloInterval_Object((1,3,6,1,4,1,171,10,97,2,19,1,5,2),_MyClientProbeHelloInterval_Type())
myClientProbeHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:myClientProbeHelloInterval.setStatus(_A)
_MyClientProbeAliveInteval_Type=Unsigned32
_MyClientProbeAliveInteval_Object=MibScalar
myClientProbeAliveInteval=_MyClientProbeAliveInteval_Object((1,3,6,1,4,1,171,10,97,2,19,1,5,3),_MyClientProbeAliveInteval_Type())
myClientProbeAliveInteval.setMaxAccess(_D)
if mibBuilder.loadTexts:myClientProbeAliveInteval.setStatus(_A)
_MyAAAMIBConformance_ObjectIdentity=ObjectIdentity
myAAAMIBConformance=_MyAAAMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,19,2))
_MyAAAMIBCompliances_ObjectIdentity=ObjectIdentity
myAAAMIBCompliances=_MyAAAMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,19,2,1))
_MyAAAMIBGroups_ObjectIdentity=ObjectIdentity
myAAAMIBGroups=_MyAAAMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,19,2,2))
myDot1xAuthMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,19,2,2,1))
myDot1xAuthMIBGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_J),(_B,_K),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_L),(_B,_M),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_N),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:myDot1xAuthMIBGroup.setStatus(_A)
myAAAServerMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,19,2,2,2))
myAAAServerMIBGroup.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:myAAAServerMIBGroup.setStatus(_A)
myAuthAddrMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,19,2,2,3))
myAuthAddrMIBGroup.setObjects(*((_B,_P),(_B,_O),(_B,_AB),(_B,_Q),(_B,_R),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:myAuthAddrMIBGroup.setStatus(_A)
myAuthModeMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,19,2,2,4))
myAuthModeMIBGroup.setObjects((_B,_AH))
if mibBuilder.loadTexts:myAuthModeMIBGroup.setStatus(_A)
myClientProbeGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,19,2,2,5))
myClientProbeGroup.setObjects(*((_B,_AI),(_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:myClientProbeGroup.setStatus(_A)
myAAAMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,97,2,19,2,1,1))
myAAAMIBCompliance.setObjects(*((_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:myAAAMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'myAAAMIB':myAAAMIB,'myAAAMIBObjects':myAAAMIBObjects,'myDot1xAuthObjects':myDot1xAuthObjects,_X:myDot1xAuthStatus,_Y:myDot1xAuthObjectsQuietPeriod,_Z:myDot1xAuthObjectsTxPeriod,_a:myDot1xAuthObjectsSuppTimeout,_b:myDot1xAuthObjectsServerTimeout,_c:myDot1xAuthObjectsMaxReq,_d:myDot1xAuthObjectsReAuthPeriod,_y:myDot1xAuthObjectsMaxReauth,_e:myDot1xAuthObjectsReAuthEnable,'myDot1xAuthObjectsConfigTable':myDot1xAuthObjectsConfigTable,'myDot1xAuthObjectsConfigEntry':myDot1xAuthObjectsConfigEntry,_J:myDot1xAuthObjectsConfigFdbId,_K:myDot1xAuthObjectsConfigAddr,_f:myDot1xAuthObjectsPaeState,_g:myDot1xAuthObjectsBackendAuthState,_h:myDot1xAuthObjectsAuthControlledPortStatus,_i:myDot1xAuthObjectsKeyTxEnabled,_j:myDot1xAuthObjectsIfIndex,'myDot1xAuthObjectsStatsTable':myDot1xAuthObjectsStatsTable,'myDot1xAuthStatsEntry':myDot1xAuthStatsEntry,_L:myDot1xAuthObjectsStatsFdbId,_M:myDot1xAuthObjectsStatsAddr,_k:myDot1xAuthObjectsEapolFramesRx,_l:myDot1xAuthObjectsEapolFramesTx,_m:myDot1xAuthObjectsEapolMyFramesRx,_n:myDot1xAuthObjectsEapolLogoffFramesRx,_o:myDot1xAuthObjectsEapolRespIdFramesRx,_p:myDot1xAuthObjectsEapolRespFramesRx,_q:myDot1xAuthObjectsEapolReqIdFramesTx,_r:myDot1xAuthObjectsEapolReqFramesTx,_s:myDot1xAuthObjectsInvalidEapolFramesRx,_t:myDot1xAuthObjectsEapLengthErrorFramesRx,_u:myDot1xAuthObjectsLastEapolFrameVersion,_v:myDot1xAuthObjectsLastEapolFrameSource,_w:myDot1xCurrentUserNumber,_x:myDot1xCurrentAuthenticatedUserNumber,'myDot1xAccountStatus':myDot1xAccountStatus,'myAuthIfTable':myAuthIfTable,'myAuthIfEntry':myAuthIfEntry,_N:myAuthIf,_z:myAuthIfStatus,_A0:myAuthenticationMode,'myDot1xAccountUpdateStatus':myDot1xAccountUpdateStatus,'myDot1xAcctInterimInterval':myDot1xAcctInterimInterval,'myDot1xEapolTagEnabled':myDot1xEapolTagEnabled,'myDot1xIfUserMaxTable':myDot1xIfUserMaxTable,'myDot1xIfUserMaxEntry':myDot1xIfUserMaxEntry,_T:myDot1xIfUserMaxIndex,'myDot1xIfUserMaxNum':myDot1xIfUserMaxNum,'myAAAServerObjects':myAAAServerObjects,_A1:myAAAServerAuthPort,_A2:myAAAServerAcctPort,_A3:myAAAServerRadiusKeyStr,_A4:myAAAServerTacplusKeyStr,'myAAAServerConfigTable':myAAAServerConfigTable,'myAAAServerConfigEntry':myAAAServerConfigEntry,_U:myAAAServerConfigProtocol,_V:myAAAServerConfigIndex,_A5:myAAAServerConfigAddressType,_A6:myAAAServerConfigAddress,_A7:myAAAServerConfigAuthPort,_A8:myAAAServerConfigAcctPort,_A9:myAAAServerConfigKeyStr,_AA:myAAAServerConfigRowStatus,'myAuthUserObjects':myAuthUserObjects,'myAuthAddrTable':myAuthAddrTable,'myAuthAddrEntry':myAuthAddrEntry,_O:myAuthPort,_P:myAuthMacAddress,_AB:myAuthAddrStatus,'myAuthUserTable':myAuthUserTable,'myAuthUserEntry':myAuthUserEntry,_Q:myAuthUserFdbId,_R:myAuthUserMacAddress,_AC:myAuthUserName,_AD:myAuthUserSessionId,_AE:myAuthUserIpAddr,_AF:myAuthUserPort,_AG:myAuthUserStatus,'myAuthUserForVPNDel':myAuthUserForVPNDel,'myAuthModeObjects':myAuthModeObjects,_AH:myIpAuthorizationMode,'myClientProbeObjects':myClientProbeObjects,_AI:myClientProbeEnabledStatus,_AJ:myClientProbeHelloInterval,_AK:myClientProbeAliveInteval,'myAAAMIBConformance':myAAAMIBConformance,'myAAAMIBCompliances':myAAAMIBCompliances,'myAAAMIBCompliance':myAAAMIBCompliance,'myAAAMIBGroups':myAAAMIBGroups,_AL:myDot1xAuthMIBGroup,_AM:myAAAServerMIBGroup,_AN:myAuthAddrMIBGroup,_AO:myAuthModeMIBGroup,_AP:myClientProbeGroup})