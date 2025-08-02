_AH='myClientProbeGroup'
_AG='myAuthModeMIBGroup'
_AF='myAuthAddrMIBGroup'
_AE='myAAAServerMIBGroup'
_AD='myDot1xAuthMIBGroup'
_AC='myClientProbeAliveInteval'
_AB='myClientProbeHelloInterval'
_AA='myClientProbeEnabledStatus'
_A9='myIpAuthorizationMode'
_A8='myAuthUserStatus'
_A7='myAuthUserPort'
_A6='myAuthUserIpAddr'
_A5='myAuthUserSessionId'
_A4='myAuthUserName'
_A3='myAuthAddrStatus'
_A2='myAAAAuthenBackUpServerIpAddr'
_A1='myAAAAccountBackUpServerIpAddr'
_A0='myAAAAccountServerIpAddr'
_z='myAAAKeyStrOfAAAServer'
_y='myAAAServerObjectsAcctPort'
_x='myAAAAuthenServerAuthenPort'
_w='myAAAAuthenServerIpAddr'
_v='myAuthenticationMode'
_u='myAuthIfStatus'
_t='myDot1xAuthObjectsMaxReauth'
_s='myDot1xCurrentAuthenticatedUserNumber'
_r='myDot1xCurrentUserNumber'
_q='myDot1xAuthObjectsLastEapolFrameSource'
_p='myDot1xAuthObjectsLastEapolFrameVersion'
_o='myDot1xAuthObjectsEapLengthErrorFramesRx'
_n='myDot1xAuthObjectsInvalidEapolFramesRx'
_m='myDot1xAuthObjectsEapolReqFramesTx'
_l='myDot1xAuthObjectsEapolReqIdFramesTx'
_k='myDot1xAuthObjectsEapolRespFramesRx'
_j='myDot1xAuthObjectsEapolRespIdFramesRx'
_i='myDot1xAuthObjectsEapolLogoffFramesRx'
_h='myDot1xAuthObjectsEapolMyFramesRx'
_g='myDot1xAuthObjectsEapolFramesTx'
_f='myDot1xAuthObjectsEapolFramesRx'
_e='myDot1xAuthObjectsIfIndex'
_d='myDot1xAuthObjectsKeyTxEnabled'
_c='myDot1xAuthObjectsAuthControlledPortStatus'
_b='myDot1xAuthObjectsBackendAuthState'
_a='myDot1xAuthObjectsPaeState'
_Z='myDot1xAuthObjectsReAuthEnable'
_Y='myDot1xAuthObjectsReAuthPeriod'
_X='myDot1xAuthObjectsMaxReq'
_W='myDot1xAuthObjectsServerTimeout'
_V='myDot1xAuthObjectsSuppTimeout'
_U='myDot1xAuthObjectsTxPeriod'
_T='myDot1xAuthObjectsQuietPeriod'
_S='myDot1xAuthStatus'
_R='initialize'
_Q='myAuthUserMacAddress'
_P='myAuthUserFdbId'
_O='myAuthMacAddress'
_N='myAuthPort'
_M='myAuthIf'
_L='myDot1xAuthObjectsStatsAddr'
_K='myDot1xAuthObjectsStatsFdbId'
_J='myDot1xAuthObjectsConfigAddr'
_I='myDot1xAuthObjectsConfigFdbId'
_H='DisplayString'
_G='EnabledStatus'
_F='Unsigned32'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='MY-AAA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('MY-SMI','myMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('MY-TC','ConfigStatus','IfIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_G)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
myAAAMIB=ModuleIdentity((1,3,6,1,4,1,4881,1,1,10,2,19))
if mibBuilder.loadTexts:myAAAMIB.setRevisions(('2002-03-20 00:00',))
_MyAAAMIBObjects_ObjectIdentity=ObjectIdentity
myAAAMIBObjects=_MyAAAMIBObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,19,1))
_MyDot1xAuthObjects_ObjectIdentity=ObjectIdentity
myDot1xAuthObjects=_MyDot1xAuthObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,19,1,1))
class _MyDot1xAuthStatus_Type(EnabledStatus):defaultValue=2
_MyDot1xAuthStatus_Type.__name__=_G
_MyDot1xAuthStatus_Object=MibScalar
myDot1xAuthStatus=_MyDot1xAuthStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,1),_MyDot1xAuthStatus_Type())
myDot1xAuthStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAuthStatus.setStatus(_A)
class _MyDot1xAuthObjectsQuietPeriod_Type(Unsigned32):defaultValue=60
_MyDot1xAuthObjectsQuietPeriod_Type.__name__=_F
_MyDot1xAuthObjectsQuietPeriod_Object=MibScalar
myDot1xAuthObjectsQuietPeriod=_MyDot1xAuthObjectsQuietPeriod_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,2),_MyDot1xAuthObjectsQuietPeriod_Type())
myDot1xAuthObjectsQuietPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAuthObjectsQuietPeriod.setStatus(_A)
class _MyDot1xAuthObjectsTxPeriod_Type(Unsigned32):defaultValue=30
_MyDot1xAuthObjectsTxPeriod_Type.__name__=_F
_MyDot1xAuthObjectsTxPeriod_Object=MibScalar
myDot1xAuthObjectsTxPeriod=_MyDot1xAuthObjectsTxPeriod_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,3),_MyDot1xAuthObjectsTxPeriod_Type())
myDot1xAuthObjectsTxPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAuthObjectsTxPeriod.setStatus(_A)
class _MyDot1xAuthObjectsSuppTimeout_Type(Unsigned32):defaultValue=30
_MyDot1xAuthObjectsSuppTimeout_Type.__name__=_F
_MyDot1xAuthObjectsSuppTimeout_Object=MibScalar
myDot1xAuthObjectsSuppTimeout=_MyDot1xAuthObjectsSuppTimeout_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,4),_MyDot1xAuthObjectsSuppTimeout_Type())
myDot1xAuthObjectsSuppTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAuthObjectsSuppTimeout.setStatus(_A)
class _MyDot1xAuthObjectsServerTimeout_Type(Unsigned32):defaultValue=30
_MyDot1xAuthObjectsServerTimeout_Type.__name__=_F
_MyDot1xAuthObjectsServerTimeout_Object=MibScalar
myDot1xAuthObjectsServerTimeout=_MyDot1xAuthObjectsServerTimeout_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,5),_MyDot1xAuthObjectsServerTimeout_Type())
myDot1xAuthObjectsServerTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAuthObjectsServerTimeout.setStatus(_A)
class _MyDot1xAuthObjectsMaxReq_Type(Unsigned32):defaultValue=2
_MyDot1xAuthObjectsMaxReq_Type.__name__=_F
_MyDot1xAuthObjectsMaxReq_Object=MibScalar
myDot1xAuthObjectsMaxReq=_MyDot1xAuthObjectsMaxReq_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,6),_MyDot1xAuthObjectsMaxReq_Type())
myDot1xAuthObjectsMaxReq.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAuthObjectsMaxReq.setStatus(_A)
class _MyDot1xAuthObjectsReAuthPeriod_Type(Unsigned32):defaultValue=3600
_MyDot1xAuthObjectsReAuthPeriod_Type.__name__=_F
_MyDot1xAuthObjectsReAuthPeriod_Object=MibScalar
myDot1xAuthObjectsReAuthPeriod=_MyDot1xAuthObjectsReAuthPeriod_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,7),_MyDot1xAuthObjectsReAuthPeriod_Type())
myDot1xAuthObjectsReAuthPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAuthObjectsReAuthPeriod.setStatus(_A)
class _MyDot1xAuthObjectsMaxReauth_Type(Unsigned32):defaultValue=2
_MyDot1xAuthObjectsMaxReauth_Type.__name__=_F
_MyDot1xAuthObjectsMaxReauth_Object=MibScalar
myDot1xAuthObjectsMaxReauth=_MyDot1xAuthObjectsMaxReauth_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,8),_MyDot1xAuthObjectsMaxReauth_Type())
myDot1xAuthObjectsMaxReauth.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAuthObjectsMaxReauth.setStatus(_A)
class _MyDot1xAuthObjectsReAuthEnable_Type(EnabledStatus):defaultValue=2
_MyDot1xAuthObjectsReAuthEnable_Type.__name__=_G
_MyDot1xAuthObjectsReAuthEnable_Object=MibScalar
myDot1xAuthObjectsReAuthEnable=_MyDot1xAuthObjectsReAuthEnable_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,9),_MyDot1xAuthObjectsReAuthEnable_Type())
myDot1xAuthObjectsReAuthEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAuthObjectsReAuthEnable.setStatus(_A)
_MyDot1xAuthObjectsConfigTable_Object=MibTable
myDot1xAuthObjectsConfigTable=_MyDot1xAuthObjectsConfigTable_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,10))
if mibBuilder.loadTexts:myDot1xAuthObjectsConfigTable.setStatus(_A)
_MyDot1xAuthObjectsConfigEntry_Object=MibTableRow
myDot1xAuthObjectsConfigEntry=_MyDot1xAuthObjectsConfigEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,10,1))
myDot1xAuthObjectsConfigEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:myDot1xAuthObjectsConfigEntry.setStatus(_A)
_MyDot1xAuthObjectsConfigFdbId_Type=Unsigned32
_MyDot1xAuthObjectsConfigFdbId_Object=MibTableColumn
myDot1xAuthObjectsConfigFdbId=_MyDot1xAuthObjectsConfigFdbId_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,10,1,1),_MyDot1xAuthObjectsConfigFdbId_Type())
myDot1xAuthObjectsConfigFdbId.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsConfigFdbId.setStatus(_A)
_MyDot1xAuthObjectsConfigAddr_Type=MacAddress
_MyDot1xAuthObjectsConfigAddr_Object=MibTableColumn
myDot1xAuthObjectsConfigAddr=_MyDot1xAuthObjectsConfigAddr_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,10,1,2),_MyDot1xAuthObjectsConfigAddr_Type())
myDot1xAuthObjectsConfigAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsConfigAddr.setStatus(_A)
class _MyDot1xAuthObjectsPaeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_R,1),('disconnected',2),('connecting',3),('authenticating',4),('authenticated',5),('aborting',6),('held',7),('forceAuth',8),('forceUnauth',9)))
_MyDot1xAuthObjectsPaeState_Type.__name__=_E
_MyDot1xAuthObjectsPaeState_Object=MibTableColumn
myDot1xAuthObjectsPaeState=_MyDot1xAuthObjectsPaeState_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,10,1,3),_MyDot1xAuthObjectsPaeState_Type())
myDot1xAuthObjectsPaeState.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsPaeState.setStatus(_A)
class _MyDot1xAuthObjectsBackendAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('request',1),('response',2),('success',3),('fail',4),('timeout',5),('idle',6),(_R,7)))
_MyDot1xAuthObjectsBackendAuthState_Type.__name__=_E
_MyDot1xAuthObjectsBackendAuthState_Object=MibTableColumn
myDot1xAuthObjectsBackendAuthState=_MyDot1xAuthObjectsBackendAuthState_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,10,1,4),_MyDot1xAuthObjectsBackendAuthState_Type())
myDot1xAuthObjectsBackendAuthState.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsBackendAuthState.setStatus(_A)
class _MyDot1xAuthObjectsAuthControlledPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('authorized',1),('unauthorized',2)))
_MyDot1xAuthObjectsAuthControlledPortStatus_Type.__name__=_E
_MyDot1xAuthObjectsAuthControlledPortStatus_Object=MibTableColumn
myDot1xAuthObjectsAuthControlledPortStatus=_MyDot1xAuthObjectsAuthControlledPortStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,10,1,5),_MyDot1xAuthObjectsAuthControlledPortStatus_Type())
myDot1xAuthObjectsAuthControlledPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsAuthControlledPortStatus.setStatus(_A)
_MyDot1xAuthObjectsKeyTxEnabled_Type=TruthValue
_MyDot1xAuthObjectsKeyTxEnabled_Object=MibTableColumn
myDot1xAuthObjectsKeyTxEnabled=_MyDot1xAuthObjectsKeyTxEnabled_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,10,1,6),_MyDot1xAuthObjectsKeyTxEnabled_Type())
myDot1xAuthObjectsKeyTxEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsKeyTxEnabled.setStatus(_A)
_MyDot1xAuthObjectsIfIndex_Type=IfIndex
_MyDot1xAuthObjectsIfIndex_Object=MibTableColumn
myDot1xAuthObjectsIfIndex=_MyDot1xAuthObjectsIfIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,10,1,7),_MyDot1xAuthObjectsIfIndex_Type())
myDot1xAuthObjectsIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsIfIndex.setStatus(_A)
_MyDot1xAuthObjectsStatsTable_Object=MibTable
myDot1xAuthObjectsStatsTable=_MyDot1xAuthObjectsStatsTable_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,11))
if mibBuilder.loadTexts:myDot1xAuthObjectsStatsTable.setStatus(_A)
_MyDot1xAuthStatsEntry_Object=MibTableRow
myDot1xAuthStatsEntry=_MyDot1xAuthStatsEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,11,1))
myDot1xAuthStatsEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:myDot1xAuthStatsEntry.setStatus(_A)
_MyDot1xAuthObjectsStatsFdbId_Type=Unsigned32
_MyDot1xAuthObjectsStatsFdbId_Object=MibTableColumn
myDot1xAuthObjectsStatsFdbId=_MyDot1xAuthObjectsStatsFdbId_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,11,1,1),_MyDot1xAuthObjectsStatsFdbId_Type())
myDot1xAuthObjectsStatsFdbId.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsStatsFdbId.setStatus(_A)
_MyDot1xAuthObjectsStatsAddr_Type=MacAddress
_MyDot1xAuthObjectsStatsAddr_Object=MibTableColumn
myDot1xAuthObjectsStatsAddr=_MyDot1xAuthObjectsStatsAddr_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,11,1,2),_MyDot1xAuthObjectsStatsAddr_Type())
myDot1xAuthObjectsStatsAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsStatsAddr.setStatus(_A)
_MyDot1xAuthObjectsEapolFramesRx_Type=Counter32
_MyDot1xAuthObjectsEapolFramesRx_Object=MibTableColumn
myDot1xAuthObjectsEapolFramesRx=_MyDot1xAuthObjectsEapolFramesRx_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,11,1,3),_MyDot1xAuthObjectsEapolFramesRx_Type())
myDot1xAuthObjectsEapolFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsEapolFramesRx.setStatus(_A)
_MyDot1xAuthObjectsEapolFramesTx_Type=Counter32
_MyDot1xAuthObjectsEapolFramesTx_Object=MibTableColumn
myDot1xAuthObjectsEapolFramesTx=_MyDot1xAuthObjectsEapolFramesTx_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,11,1,4),_MyDot1xAuthObjectsEapolFramesTx_Type())
myDot1xAuthObjectsEapolFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsEapolFramesTx.setStatus(_A)
_MyDot1xAuthObjectsEapolMyFramesRx_Type=Counter32
_MyDot1xAuthObjectsEapolMyFramesRx_Object=MibTableColumn
myDot1xAuthObjectsEapolMyFramesRx=_MyDot1xAuthObjectsEapolMyFramesRx_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,11,1,5),_MyDot1xAuthObjectsEapolMyFramesRx_Type())
myDot1xAuthObjectsEapolMyFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsEapolMyFramesRx.setStatus(_A)
_MyDot1xAuthObjectsEapolLogoffFramesRx_Type=Counter32
_MyDot1xAuthObjectsEapolLogoffFramesRx_Object=MibTableColumn
myDot1xAuthObjectsEapolLogoffFramesRx=_MyDot1xAuthObjectsEapolLogoffFramesRx_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,11,1,6),_MyDot1xAuthObjectsEapolLogoffFramesRx_Type())
myDot1xAuthObjectsEapolLogoffFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsEapolLogoffFramesRx.setStatus(_A)
_MyDot1xAuthObjectsEapolRespIdFramesRx_Type=Counter32
_MyDot1xAuthObjectsEapolRespIdFramesRx_Object=MibTableColumn
myDot1xAuthObjectsEapolRespIdFramesRx=_MyDot1xAuthObjectsEapolRespIdFramesRx_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,11,1,7),_MyDot1xAuthObjectsEapolRespIdFramesRx_Type())
myDot1xAuthObjectsEapolRespIdFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsEapolRespIdFramesRx.setStatus(_A)
_MyDot1xAuthObjectsEapolRespFramesRx_Type=Counter32
_MyDot1xAuthObjectsEapolRespFramesRx_Object=MibTableColumn
myDot1xAuthObjectsEapolRespFramesRx=_MyDot1xAuthObjectsEapolRespFramesRx_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,11,1,8),_MyDot1xAuthObjectsEapolRespFramesRx_Type())
myDot1xAuthObjectsEapolRespFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsEapolRespFramesRx.setStatus(_A)
_MyDot1xAuthObjectsEapolReqIdFramesTx_Type=Counter32
_MyDot1xAuthObjectsEapolReqIdFramesTx_Object=MibTableColumn
myDot1xAuthObjectsEapolReqIdFramesTx=_MyDot1xAuthObjectsEapolReqIdFramesTx_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,11,1,9),_MyDot1xAuthObjectsEapolReqIdFramesTx_Type())
myDot1xAuthObjectsEapolReqIdFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsEapolReqIdFramesTx.setStatus(_A)
_MyDot1xAuthObjectsEapolReqFramesTx_Type=Counter32
_MyDot1xAuthObjectsEapolReqFramesTx_Object=MibTableColumn
myDot1xAuthObjectsEapolReqFramesTx=_MyDot1xAuthObjectsEapolReqFramesTx_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,11,1,10),_MyDot1xAuthObjectsEapolReqFramesTx_Type())
myDot1xAuthObjectsEapolReqFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsEapolReqFramesTx.setStatus(_A)
_MyDot1xAuthObjectsInvalidEapolFramesRx_Type=Counter32
_MyDot1xAuthObjectsInvalidEapolFramesRx_Object=MibTableColumn
myDot1xAuthObjectsInvalidEapolFramesRx=_MyDot1xAuthObjectsInvalidEapolFramesRx_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,11,1,11),_MyDot1xAuthObjectsInvalidEapolFramesRx_Type())
myDot1xAuthObjectsInvalidEapolFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsInvalidEapolFramesRx.setStatus(_A)
_MyDot1xAuthObjectsEapLengthErrorFramesRx_Type=Counter32
_MyDot1xAuthObjectsEapLengthErrorFramesRx_Object=MibTableColumn
myDot1xAuthObjectsEapLengthErrorFramesRx=_MyDot1xAuthObjectsEapLengthErrorFramesRx_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,11,1,12),_MyDot1xAuthObjectsEapLengthErrorFramesRx_Type())
myDot1xAuthObjectsEapLengthErrorFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsEapLengthErrorFramesRx.setStatus(_A)
_MyDot1xAuthObjectsLastEapolFrameVersion_Type=Unsigned32
_MyDot1xAuthObjectsLastEapolFrameVersion_Object=MibTableColumn
myDot1xAuthObjectsLastEapolFrameVersion=_MyDot1xAuthObjectsLastEapolFrameVersion_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,11,1,13),_MyDot1xAuthObjectsLastEapolFrameVersion_Type())
myDot1xAuthObjectsLastEapolFrameVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsLastEapolFrameVersion.setStatus(_A)
_MyDot1xAuthObjectsLastEapolFrameSource_Type=MacAddress
_MyDot1xAuthObjectsLastEapolFrameSource_Object=MibTableColumn
myDot1xAuthObjectsLastEapolFrameSource=_MyDot1xAuthObjectsLastEapolFrameSource_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,11,1,14),_MyDot1xAuthObjectsLastEapolFrameSource_Type())
myDot1xAuthObjectsLastEapolFrameSource.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xAuthObjectsLastEapolFrameSource.setStatus(_A)
_MyDot1xCurrentUserNumber_Type=Counter32
_MyDot1xCurrentUserNumber_Object=MibScalar
myDot1xCurrentUserNumber=_MyDot1xCurrentUserNumber_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,12),_MyDot1xCurrentUserNumber_Type())
myDot1xCurrentUserNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xCurrentUserNumber.setStatus(_A)
_MyDot1xCurrentAuthenticatedUserNumber_Type=Counter32
_MyDot1xCurrentAuthenticatedUserNumber_Object=MibScalar
myDot1xCurrentAuthenticatedUserNumber=_MyDot1xCurrentAuthenticatedUserNumber_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,13),_MyDot1xCurrentAuthenticatedUserNumber_Type())
myDot1xCurrentAuthenticatedUserNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:myDot1xCurrentAuthenticatedUserNumber.setStatus(_A)
class _MyDot1xAccountStatus_Type(EnabledStatus):defaultValue=2
_MyDot1xAccountStatus_Type.__name__=_G
_MyDot1xAccountStatus_Object=MibScalar
myDot1xAccountStatus=_MyDot1xAccountStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,14),_MyDot1xAccountStatus_Type())
myDot1xAccountStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAccountStatus.setStatus(_A)
_MyAuthIfTable_Object=MibTable
myAuthIfTable=_MyAuthIfTable_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,15))
if mibBuilder.loadTexts:myAuthIfTable.setStatus(_A)
_MyAuthIfEntry_Object=MibTableRow
myAuthIfEntry=_MyAuthIfEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,15,1))
myAuthIfEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:myAuthIfEntry.setStatus(_A)
_MyAuthIf_Type=IfIndex
_MyAuthIf_Object=MibTableColumn
myAuthIf=_MyAuthIf_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,15,1,1),_MyAuthIf_Type())
myAuthIf.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthIf.setStatus(_A)
class _MyAuthIfStatus_Type(EnabledStatus):defaultValue=2
_MyAuthIfStatus_Type.__name__=_G
_MyAuthIfStatus_Object=MibTableColumn
myAuthIfStatus=_MyAuthIfStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,15,1,2),_MyAuthIfStatus_Type())
myAuthIfStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:myAuthIfStatus.setStatus(_A)
class _MyAuthenticationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eap-md5',1),('chap',2)))
_MyAuthenticationMode_Type.__name__=_E
_MyAuthenticationMode_Object=MibScalar
myAuthenticationMode=_MyAuthenticationMode_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,16),_MyAuthenticationMode_Type())
myAuthenticationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:myAuthenticationMode.setStatus(_A)
_MyDot1xAccountUpdateStatus_Type=EnabledStatus
_MyDot1xAccountUpdateStatus_Object=MibScalar
myDot1xAccountUpdateStatus=_MyDot1xAccountUpdateStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,17),_MyDot1xAccountUpdateStatus_Type())
myDot1xAccountUpdateStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAccountUpdateStatus.setStatus(_A)
class _MyDot1xAcctInterimInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,65535))
_MyDot1xAcctInterimInterval_Type.__name__=_F
_MyDot1xAcctInterimInterval_Object=MibScalar
myDot1xAcctInterimInterval=_MyDot1xAcctInterimInterval_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,18),_MyDot1xAcctInterimInterval_Type())
myDot1xAcctInterimInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xAcctInterimInterval.setStatus(_A)
_MyDot1xEapolTagEnabled_Type=EnabledStatus
_MyDot1xEapolTagEnabled_Object=MibScalar
myDot1xEapolTagEnabled=_MyDot1xEapolTagEnabled_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,1,19),_MyDot1xEapolTagEnabled_Type())
myDot1xEapolTagEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:myDot1xEapolTagEnabled.setStatus(_A)
_MyAAAServerObjects_ObjectIdentity=ObjectIdentity
myAAAServerObjects=_MyAAAServerObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,19,1,2))
_MyAAAAuthenServerIpAddr_Type=IpAddress
_MyAAAAuthenServerIpAddr_Object=MibScalar
myAAAAuthenServerIpAddr=_MyAAAAuthenServerIpAddr_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,2,1),_MyAAAAuthenServerIpAddr_Type())
myAAAAuthenServerIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:myAAAAuthenServerIpAddr.setStatus(_A)
class _MyAAAAuthenServerAuthenPort_Type(Integer32):defaultValue=1812;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MyAAAAuthenServerAuthenPort_Type.__name__=_E
_MyAAAAuthenServerAuthenPort_Object=MibScalar
myAAAAuthenServerAuthenPort=_MyAAAAuthenServerAuthenPort_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,2,2),_MyAAAAuthenServerAuthenPort_Type())
myAAAAuthenServerAuthenPort.setMaxAccess(_D)
if mibBuilder.loadTexts:myAAAAuthenServerAuthenPort.setStatus(_A)
class _MyAAAServerObjectsAcctPort_Type(Integer32):defaultValue=1813;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MyAAAServerObjectsAcctPort_Type.__name__=_E
_MyAAAServerObjectsAcctPort_Object=MibScalar
myAAAServerObjectsAcctPort=_MyAAAServerObjectsAcctPort_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,2,3),_MyAAAServerObjectsAcctPort_Type())
myAAAServerObjectsAcctPort.setMaxAccess(_D)
if mibBuilder.loadTexts:myAAAServerObjectsAcctPort.setStatus(_A)
class _MyAAAKeyStrOfAAAServer_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_MyAAAKeyStrOfAAAServer_Type.__name__=_H
_MyAAAKeyStrOfAAAServer_Object=MibScalar
myAAAKeyStrOfAAAServer=_MyAAAKeyStrOfAAAServer_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,2,4),_MyAAAKeyStrOfAAAServer_Type())
myAAAKeyStrOfAAAServer.setMaxAccess(_D)
if mibBuilder.loadTexts:myAAAKeyStrOfAAAServer.setStatus(_A)
_MyAAAAccountServerIpAddr_Type=IpAddress
_MyAAAAccountServerIpAddr_Object=MibScalar
myAAAAccountServerIpAddr=_MyAAAAccountServerIpAddr_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,2,5),_MyAAAAccountServerIpAddr_Type())
myAAAAccountServerIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:myAAAAccountServerIpAddr.setStatus(_A)
_MyAAAAccountBackUpServerIpAddr_Type=IpAddress
_MyAAAAccountBackUpServerIpAddr_Object=MibScalar
myAAAAccountBackUpServerIpAddr=_MyAAAAccountBackUpServerIpAddr_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,2,6),_MyAAAAccountBackUpServerIpAddr_Type())
myAAAAccountBackUpServerIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:myAAAAccountBackUpServerIpAddr.setStatus(_A)
_MyAAAAuthenBackUpServerIpAddr_Type=IpAddress
_MyAAAAuthenBackUpServerIpAddr_Object=MibScalar
myAAAAuthenBackUpServerIpAddr=_MyAAAAuthenBackUpServerIpAddr_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,2,7),_MyAAAAuthenBackUpServerIpAddr_Type())
myAAAAuthenBackUpServerIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:myAAAAuthenBackUpServerIpAddr.setStatus(_A)
_MyAuthUserObjects_ObjectIdentity=ObjectIdentity
myAuthUserObjects=_MyAuthUserObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,19,1,3))
_MyAuthAddrTable_Object=MibTable
myAuthAddrTable=_MyAuthAddrTable_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,3,1))
if mibBuilder.loadTexts:myAuthAddrTable.setStatus(_A)
_MyAuthAddrEntry_Object=MibTableRow
myAuthAddrEntry=_MyAuthAddrEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,3,1,1))
myAuthAddrEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:myAuthAddrEntry.setStatus(_A)
_MyAuthPort_Type=IfIndex
_MyAuthPort_Object=MibTableColumn
myAuthPort=_MyAuthPort_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,3,1,1,1),_MyAuthPort_Type())
myAuthPort.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthPort.setStatus(_A)
_MyAuthMacAddress_Type=MacAddress
_MyAuthMacAddress_Object=MibTableColumn
myAuthMacAddress=_MyAuthMacAddress_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,3,1,1,2),_MyAuthMacAddress_Type())
myAuthMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthMacAddress.setStatus(_A)
class _MyAuthAddrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_MyAuthAddrStatus_Type.__name__=_E
_MyAuthAddrStatus_Object=MibTableColumn
myAuthAddrStatus=_MyAuthAddrStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,3,1,1,3),_MyAuthAddrStatus_Type())
myAuthAddrStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:myAuthAddrStatus.setStatus(_A)
_MyAuthUserTable_Object=MibTable
myAuthUserTable=_MyAuthUserTable_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,3,2))
if mibBuilder.loadTexts:myAuthUserTable.setStatus(_A)
_MyAuthUserEntry_Object=MibTableRow
myAuthUserEntry=_MyAuthUserEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,3,2,1))
myAuthUserEntry.setIndexNames((0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:myAuthUserEntry.setStatus(_A)
_MyAuthUserFdbId_Type=Unsigned32
_MyAuthUserFdbId_Object=MibTableColumn
myAuthUserFdbId=_MyAuthUserFdbId_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,3,2,1,1),_MyAuthUserFdbId_Type())
myAuthUserFdbId.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthUserFdbId.setStatus(_A)
_MyAuthUserMacAddress_Type=MacAddress
_MyAuthUserMacAddress_Object=MibTableColumn
myAuthUserMacAddress=_MyAuthUserMacAddress_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,3,2,1,2),_MyAuthUserMacAddress_Type())
myAuthUserMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthUserMacAddress.setStatus(_A)
_MyAuthUserName_Type=DisplayString
_MyAuthUserName_Object=MibTableColumn
myAuthUserName=_MyAuthUserName_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,3,2,1,3),_MyAuthUserName_Type())
myAuthUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthUserName.setStatus(_A)
_MyAuthUserSessionId_Type=DisplayString
_MyAuthUserSessionId_Object=MibTableColumn
myAuthUserSessionId=_MyAuthUserSessionId_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,3,2,1,4),_MyAuthUserSessionId_Type())
myAuthUserSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthUserSessionId.setStatus(_A)
_MyAuthUserIpAddr_Type=IpAddress
_MyAuthUserIpAddr_Object=MibTableColumn
myAuthUserIpAddr=_MyAuthUserIpAddr_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,3,2,1,5),_MyAuthUserIpAddr_Type())
myAuthUserIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthUserIpAddr.setStatus(_A)
_MyAuthUserPort_Type=Integer32
_MyAuthUserPort_Object=MibTableColumn
myAuthUserPort=_MyAuthUserPort_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,3,2,1,6),_MyAuthUserPort_Type())
myAuthUserPort.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthUserPort.setStatus(_A)
_MyAuthUserStatus_Type=ConfigStatus
_MyAuthUserStatus_Object=MibTableColumn
myAuthUserStatus=_MyAuthUserStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,3,2,1,7),_MyAuthUserStatus_Type())
myAuthUserStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:myAuthUserStatus.setStatus(_A)
class _MyAuthUserForVPNDel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_MyAuthUserForVPNDel_Type.__name__=_H
_MyAuthUserForVPNDel_Object=MibScalar
myAuthUserForVPNDel=_MyAuthUserForVPNDel_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,3,3),_MyAuthUserForVPNDel_Type())
myAuthUserForVPNDel.setMaxAccess(_D)
if mibBuilder.loadTexts:myAuthUserForVPNDel.setStatus(_A)
_MyAuthModeObjects_ObjectIdentity=ObjectIdentity
myAuthModeObjects=_MyAuthModeObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,19,1,4))
class _MyIpAuthorizationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('disable',1),('dhcpServer',2),('radiusServer',3),('supplicant',4)))
_MyIpAuthorizationMode_Type.__name__=_E
_MyIpAuthorizationMode_Object=MibScalar
myIpAuthorizationMode=_MyIpAuthorizationMode_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,4,1),_MyIpAuthorizationMode_Type())
myIpAuthorizationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:myIpAuthorizationMode.setStatus(_A)
_MyClientProbeObjects_ObjectIdentity=ObjectIdentity
myClientProbeObjects=_MyClientProbeObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,19,1,5))
_MyClientProbeEnabledStatus_Type=EnabledStatus
_MyClientProbeEnabledStatus_Object=MibScalar
myClientProbeEnabledStatus=_MyClientProbeEnabledStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,5,1),_MyClientProbeEnabledStatus_Type())
myClientProbeEnabledStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:myClientProbeEnabledStatus.setStatus(_A)
_MyClientProbeHelloInterval_Type=Unsigned32
_MyClientProbeHelloInterval_Object=MibScalar
myClientProbeHelloInterval=_MyClientProbeHelloInterval_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,5,2),_MyClientProbeHelloInterval_Type())
myClientProbeHelloInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:myClientProbeHelloInterval.setStatus(_A)
_MyClientProbeAliveInteval_Type=Unsigned32
_MyClientProbeAliveInteval_Object=MibScalar
myClientProbeAliveInteval=_MyClientProbeAliveInteval_Object((1,3,6,1,4,1,4881,1,1,10,2,19,1,5,3),_MyClientProbeAliveInteval_Type())
myClientProbeAliveInteval.setMaxAccess(_D)
if mibBuilder.loadTexts:myClientProbeAliveInteval.setStatus(_A)
_MyAAAMIBConformance_ObjectIdentity=ObjectIdentity
myAAAMIBConformance=_MyAAAMIBConformance_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,19,2))
_MyAAAMIBCompliances_ObjectIdentity=ObjectIdentity
myAAAMIBCompliances=_MyAAAMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,19,2,1))
_MyAAAMIBGroups_ObjectIdentity=ObjectIdentity
myAAAMIBGroups=_MyAAAMIBGroups_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,19,2,2))
myDot1xAuthMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,19,2,2,1))
myDot1xAuthMIBGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_I),(_B,_J),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_K),(_B,_L),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_M),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:myDot1xAuthMIBGroup.setStatus(_A)
myAAAServerMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,19,2,2,2))
myAAAServerMIBGroup.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:myAAAServerMIBGroup.setStatus(_A)
myAuthAddrMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,19,2,2,3))
myAuthAddrMIBGroup.setObjects(*((_B,_O),(_B,_N),(_B,_A3),(_B,_P),(_B,_Q),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:myAuthAddrMIBGroup.setStatus(_A)
myAuthModeMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,19,2,2,4))
myAuthModeMIBGroup.setObjects((_B,_A9))
if mibBuilder.loadTexts:myAuthModeMIBGroup.setStatus(_A)
myClientProbeGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,19,2,2,5))
myClientProbeGroup.setObjects(*((_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:myClientProbeGroup.setStatus(_A)
myAAAMIBCompliance=ModuleCompliance((1,3,6,1,4,1,4881,1,1,10,2,19,2,1,1))
myAAAMIBCompliance.setObjects(*((_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:myAAAMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'myAAAMIB':myAAAMIB,'myAAAMIBObjects':myAAAMIBObjects,'myDot1xAuthObjects':myDot1xAuthObjects,_S:myDot1xAuthStatus,_T:myDot1xAuthObjectsQuietPeriod,_U:myDot1xAuthObjectsTxPeriod,_V:myDot1xAuthObjectsSuppTimeout,_W:myDot1xAuthObjectsServerTimeout,_X:myDot1xAuthObjectsMaxReq,_Y:myDot1xAuthObjectsReAuthPeriod,_t:myDot1xAuthObjectsMaxReauth,_Z:myDot1xAuthObjectsReAuthEnable,'myDot1xAuthObjectsConfigTable':myDot1xAuthObjectsConfigTable,'myDot1xAuthObjectsConfigEntry':myDot1xAuthObjectsConfigEntry,_I:myDot1xAuthObjectsConfigFdbId,_J:myDot1xAuthObjectsConfigAddr,_a:myDot1xAuthObjectsPaeState,_b:myDot1xAuthObjectsBackendAuthState,_c:myDot1xAuthObjectsAuthControlledPortStatus,_d:myDot1xAuthObjectsKeyTxEnabled,_e:myDot1xAuthObjectsIfIndex,'myDot1xAuthObjectsStatsTable':myDot1xAuthObjectsStatsTable,'myDot1xAuthStatsEntry':myDot1xAuthStatsEntry,_K:myDot1xAuthObjectsStatsFdbId,_L:myDot1xAuthObjectsStatsAddr,_f:myDot1xAuthObjectsEapolFramesRx,_g:myDot1xAuthObjectsEapolFramesTx,_h:myDot1xAuthObjectsEapolMyFramesRx,_i:myDot1xAuthObjectsEapolLogoffFramesRx,_j:myDot1xAuthObjectsEapolRespIdFramesRx,_k:myDot1xAuthObjectsEapolRespFramesRx,_l:myDot1xAuthObjectsEapolReqIdFramesTx,_m:myDot1xAuthObjectsEapolReqFramesTx,_n:myDot1xAuthObjectsInvalidEapolFramesRx,_o:myDot1xAuthObjectsEapLengthErrorFramesRx,_p:myDot1xAuthObjectsLastEapolFrameVersion,_q:myDot1xAuthObjectsLastEapolFrameSource,_r:myDot1xCurrentUserNumber,_s:myDot1xCurrentAuthenticatedUserNumber,'myDot1xAccountStatus':myDot1xAccountStatus,'myAuthIfTable':myAuthIfTable,'myAuthIfEntry':myAuthIfEntry,_M:myAuthIf,_u:myAuthIfStatus,_v:myAuthenticationMode,'myDot1xAccountUpdateStatus':myDot1xAccountUpdateStatus,'myDot1xAcctInterimInterval':myDot1xAcctInterimInterval,'myDot1xEapolTagEnabled':myDot1xEapolTagEnabled,'myAAAServerObjects':myAAAServerObjects,_w:myAAAAuthenServerIpAddr,_x:myAAAAuthenServerAuthenPort,_y:myAAAServerObjectsAcctPort,_z:myAAAKeyStrOfAAAServer,_A0:myAAAAccountServerIpAddr,_A1:myAAAAccountBackUpServerIpAddr,_A2:myAAAAuthenBackUpServerIpAddr,'myAuthUserObjects':myAuthUserObjects,'myAuthAddrTable':myAuthAddrTable,'myAuthAddrEntry':myAuthAddrEntry,_N:myAuthPort,_O:myAuthMacAddress,_A3:myAuthAddrStatus,'myAuthUserTable':myAuthUserTable,'myAuthUserEntry':myAuthUserEntry,_P:myAuthUserFdbId,_Q:myAuthUserMacAddress,_A4:myAuthUserName,_A5:myAuthUserSessionId,_A6:myAuthUserIpAddr,_A7:myAuthUserPort,_A8:myAuthUserStatus,'myAuthUserForVPNDel':myAuthUserForVPNDel,'myAuthModeObjects':myAuthModeObjects,_A9:myIpAuthorizationMode,'myClientProbeObjects':myClientProbeObjects,_AA:myClientProbeEnabledStatus,_AB:myClientProbeHelloInterval,_AC:myClientProbeAliveInteval,'myAAAMIBConformance':myAAAMIBConformance,'myAAAMIBCompliances':myAAAMIBCompliances,'myAAAMIBCompliance':myAAAMIBCompliance,'myAAAMIBGroups':myAAAMIBGroups,_AD:myDot1xAuthMIBGroup,_AE:myAAAServerMIBGroup,_AF:myAuthAddrMIBGroup,_AG:myAuthModeMIBGroup,_AH:myClientProbeGroup})