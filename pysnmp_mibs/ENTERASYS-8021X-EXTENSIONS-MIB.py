_AQ='etsysDot1xAuthSessionControlGroup'
_AP='etsysDot1xAuthSessionStatsGroup'
_AO='etsysDot1xAuthDiagGroup'
_AN='etsysDot1xAuthStatsGroup'
_AM='etsysDot1xAuthConfigGroup'
_AL='etsysDot1xAuthStationGroup'
_AK='etsysDot1xAuthInfoStationRowStatus'
_AJ='etsysDot1xMaximumStationsStatsGathered'
_AI='etsysDot1xCurrentStationsStatsGathered'
_AH='etsysDot1xMaxCapableAuthStations'
_AG='etsysDot1xAuthSessionSuppportedObjs'
_AF='etsysDot1xAuthSessionTerminateCause'
_AE='etsysDot1xAuthSessionTime'
_AD='etsysDot1xAuthSessionAuthenticMethod'
_AC='etsysDot1xAuthSessionId'
_AB='etsysDot1xAuthSessionFramesTx'
_AA='etsysDot1xAuthSessionFramesRx'
_A9='etsysDot1xAuthSessionOctetsTx'
_A8='etsysDot1xAuthSessionOctetsRx'
_A7='etsysDot1xAuthBackendAuthFails'
_A6='etsysDot1xAuthBackendAuthSuccesses'
_A5='etsysDot1xAuthBackendNonNakResponsesFromSupplicant'
_A4='etsysDot1xAuthBackendOtherRequestsToSupplicant'
_A3='etsysDot1xAuthBackendAccessChallenges'
_A2='etsysDot1xAuthBackendResponses'
_A1='etsysDot1xAuthAuthEapLogoffWhileAuthenticated'
_A0='etsysDot1xAuthAuthEapStartsWhileAuthenticated'
_z='etsysDot1xAuthAuthReauthsWhileAuthenticated'
_y='etsysDot1xAuthAuthEapLogoffWhileAuthenticating'
_x='etsysDot1xAuthAuthEapStartsWhileAuthenticating'
_w='etsysDot1xAuthAuthReauthsWhileAuthenticating'
_v='etsysDot1xAuthAuthFailWhileAuthenticating'
_u='etsysDot1xAuthAuthTimeoutsWhileAuthenticating'
_t='etsysDot1xAuthAuthSuccessWhileAuthenticating'
_s='etsysDot1xAuthEntersAuthenticating'
_r='etsysDot1xAuthEapLogoffsWhileConnecting'
_q='etsysDot1xAuthEntersConnecting'
_p='etsysDot1xAuthLastEapolFrameSource'
_o='etsysDot1xAuthLastEapolFrameVersion'
_n='etsysDot1xAuthEapLengthErrorFramesRx'
_m='etsysDot1xAuthInvalidEapolFramesRx'
_l='etsysDot1xAuthEapolReqFramesTx'
_k='etsysDot1xAuthEapolReqIdFramesTx'
_j='etsysDot1xAuthEapolRespFramesRx'
_i='etsysDot1xAuthEapolRespIdFramesRx'
_h='etsysDot1xAuthEapolLogoffFramesRx'
_g='etsysDot1xAuthEapolStartFramesRx'
_f='etsysDot1xAuthEapolFramesTx'
_e='etsysDot1xAuthEapolFramesRx'
_d='etsysDot1xAuthKeyTxEnabled'
_c='etsysDot1xAuthReAuthEnabled'
_b='etsysDot1xAuthReAuthPeriod'
_a='etsysDot1xAuthMaxReq'
_Z='etsysDot1xAuthServerTimeout'
_Y='etsysDot1xAuthSuppTimeout'
_X='etsysDot1xAuthTxPeriod'
_W='etsysDot1xAuthQuietPeriod'
_V='etsysDot1xAuthAuthControlledPortControl'
_U='etsysDot1xAuthAuthControlledPortStatus'
_T='etsysDot1xAuthOperControlledDirections'
_S='etsysDot1xAuthAdminControlledDirections'
_R='etsysDot1xAuthReauthenticate'
_Q='etsysDot1xAuthInitialize'
_P='etsysDot1xAuthStationUserName'
_O='etsysDot1xAuthStationBackendAuthState'
_N='etsysDot1xAuthStationPaeState'
_M='etsysDot1xAuthStationPaePort'
_L='read-create'
_K='read-write'
_J='initialize'
_I='TruthValue'
_H='etsysDot1xAuthInfoStationAddress'
_G='Unsigned32'
_F='Bits'
_E='Integer32'
_D='etsysDot1xAuthStationAddress'
_C='read-only'
_B='ENTERASYS-8021X-EXTENSIONS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
PaeControlledDirections,PaeControlledPortControl,PaeControlledPortStatus=mibBuilder.importSymbols('IEEE8021-PAE-MIB','PaeControlledDirections','PaeControlledPortControl','PaeControlledPortStatus')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_F,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_I)
etsys8021xExtensionsMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,18))
if mibBuilder.loadTexts:etsys8021xExtensionsMIB.setRevisions(('2003-11-21 16:23','2002-03-07 20:10'))
_EtsysDot1xExtensionsObjects_ObjectIdentity=ObjectIdentity
etsysDot1xExtensionsObjects=_EtsysDot1xExtensionsObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,18,1))
_EtsysDot1xSystemBranch_ObjectIdentity=ObjectIdentity
etsysDot1xSystemBranch=_EtsysDot1xSystemBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,18,1,1))
_EtsysDot1xAuthenticatorBranch_ObjectIdentity=ObjectIdentity
etsysDot1xAuthenticatorBranch=_EtsysDot1xAuthenticatorBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,18,1,2))
_EtsysDot1xAuthStationBranch_ObjectIdentity=ObjectIdentity
etsysDot1xAuthStationBranch=_EtsysDot1xAuthStationBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,18,1,2,1))
_EtsysDot1xAuthStationTable_Object=MibTable
etsysDot1xAuthStationTable=_EtsysDot1xAuthStationTable_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,1))
if mibBuilder.loadTexts:etsysDot1xAuthStationTable.setStatus(_A)
_EtsysDot1xAuthStationEntry_Object=MibTableRow
etsysDot1xAuthStationEntry=_EtsysDot1xAuthStationEntry_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,1,1))
etsysDot1xAuthStationEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:etsysDot1xAuthStationEntry.setStatus(_A)
_EtsysDot1xAuthStationAddress_Type=MacAddress
_EtsysDot1xAuthStationAddress_Object=MibTableColumn
etsysDot1xAuthStationAddress=_EtsysDot1xAuthStationAddress_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,1,1,1),_EtsysDot1xAuthStationAddress_Type())
etsysDot1xAuthStationAddress.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:etsysDot1xAuthStationAddress.setStatus(_A)
_EtsysDot1xAuthStationPaePort_Type=InterfaceIndex
_EtsysDot1xAuthStationPaePort_Object=MibTableColumn
etsysDot1xAuthStationPaePort=_EtsysDot1xAuthStationPaePort_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,1,1,2),_EtsysDot1xAuthStationPaePort_Type())
etsysDot1xAuthStationPaePort.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthStationPaePort.setStatus(_A)
class _EtsysDot1xAuthStationPaeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_J,1),('disconnected',2),('connecting',3),('authenticating',4),('authenticated',5),('aborting',6),('held',7),('forceAuth',8),('forceUnauth',9)))
_EtsysDot1xAuthStationPaeState_Type.__name__=_E
_EtsysDot1xAuthStationPaeState_Object=MibTableColumn
etsysDot1xAuthStationPaeState=_EtsysDot1xAuthStationPaeState_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,1,1,3),_EtsysDot1xAuthStationPaeState_Type())
etsysDot1xAuthStationPaeState.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthStationPaeState.setStatus(_A)
class _EtsysDot1xAuthStationBackendAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('request',1),('response',2),('success',3),('fail',4),('timeout',5),('idle',6),(_J,7)))
_EtsysDot1xAuthStationBackendAuthState_Type.__name__=_E
_EtsysDot1xAuthStationBackendAuthState_Object=MibTableColumn
etsysDot1xAuthStationBackendAuthState=_EtsysDot1xAuthStationBackendAuthState_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,1,1,4),_EtsysDot1xAuthStationBackendAuthState_Type())
etsysDot1xAuthStationBackendAuthState.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthStationBackendAuthState.setStatus(_A)
_EtsysDot1xAuthStationUserName_Type=SnmpAdminString
_EtsysDot1xAuthStationUserName_Object=MibTableColumn
etsysDot1xAuthStationUserName=_EtsysDot1xAuthStationUserName_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,1,1,5),_EtsysDot1xAuthStationUserName_Type())
etsysDot1xAuthStationUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthStationUserName.setStatus(_A)
_EtsysDot1xAuthConfigTable_Object=MibTable
etsysDot1xAuthConfigTable=_EtsysDot1xAuthConfigTable_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,2))
if mibBuilder.loadTexts:etsysDot1xAuthConfigTable.setStatus(_A)
_EtsysDot1xAuthConfigEntry_Object=MibTableRow
etsysDot1xAuthConfigEntry=_EtsysDot1xAuthConfigEntry_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,2,1))
etsysDot1xAuthConfigEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:etsysDot1xAuthConfigEntry.setStatus(_A)
_EtsysDot1xAuthInitialize_Type=TruthValue
_EtsysDot1xAuthInitialize_Object=MibTableColumn
etsysDot1xAuthInitialize=_EtsysDot1xAuthInitialize_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,2,1,1),_EtsysDot1xAuthInitialize_Type())
etsysDot1xAuthInitialize.setMaxAccess(_K)
if mibBuilder.loadTexts:etsysDot1xAuthInitialize.setStatus(_A)
_EtsysDot1xAuthReauthenticate_Type=TruthValue
_EtsysDot1xAuthReauthenticate_Object=MibTableColumn
etsysDot1xAuthReauthenticate=_EtsysDot1xAuthReauthenticate_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,2,1,2),_EtsysDot1xAuthReauthenticate_Type())
etsysDot1xAuthReauthenticate.setMaxAccess(_K)
if mibBuilder.loadTexts:etsysDot1xAuthReauthenticate.setStatus(_A)
_EtsysDot1xAuthAdminControlledDirections_Type=PaeControlledDirections
_EtsysDot1xAuthAdminControlledDirections_Object=MibTableColumn
etsysDot1xAuthAdminControlledDirections=_EtsysDot1xAuthAdminControlledDirections_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,2,1,3),_EtsysDot1xAuthAdminControlledDirections_Type())
etsysDot1xAuthAdminControlledDirections.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthAdminControlledDirections.setStatus(_A)
_EtsysDot1xAuthOperControlledDirections_Type=PaeControlledDirections
_EtsysDot1xAuthOperControlledDirections_Object=MibTableColumn
etsysDot1xAuthOperControlledDirections=_EtsysDot1xAuthOperControlledDirections_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,2,1,4),_EtsysDot1xAuthOperControlledDirections_Type())
etsysDot1xAuthOperControlledDirections.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthOperControlledDirections.setStatus(_A)
_EtsysDot1xAuthAuthControlledPortStatus_Type=PaeControlledPortStatus
_EtsysDot1xAuthAuthControlledPortStatus_Object=MibTableColumn
etsysDot1xAuthAuthControlledPortStatus=_EtsysDot1xAuthAuthControlledPortStatus_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,2,1,5),_EtsysDot1xAuthAuthControlledPortStatus_Type())
etsysDot1xAuthAuthControlledPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthAuthControlledPortStatus.setStatus(_A)
_EtsysDot1xAuthAuthControlledPortControl_Type=PaeControlledPortControl
_EtsysDot1xAuthAuthControlledPortControl_Object=MibTableColumn
etsysDot1xAuthAuthControlledPortControl=_EtsysDot1xAuthAuthControlledPortControl_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,2,1,6),_EtsysDot1xAuthAuthControlledPortControl_Type())
etsysDot1xAuthAuthControlledPortControl.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthAuthControlledPortControl.setStatus(_A)
_EtsysDot1xAuthQuietPeriod_Type=Unsigned32
_EtsysDot1xAuthQuietPeriod_Object=MibTableColumn
etsysDot1xAuthQuietPeriod=_EtsysDot1xAuthQuietPeriod_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,2,1,7),_EtsysDot1xAuthQuietPeriod_Type())
etsysDot1xAuthQuietPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthQuietPeriod.setStatus(_A)
_EtsysDot1xAuthTxPeriod_Type=Unsigned32
_EtsysDot1xAuthTxPeriod_Object=MibTableColumn
etsysDot1xAuthTxPeriod=_EtsysDot1xAuthTxPeriod_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,2,1,8),_EtsysDot1xAuthTxPeriod_Type())
etsysDot1xAuthTxPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthTxPeriod.setStatus(_A)
_EtsysDot1xAuthSuppTimeout_Type=Unsigned32
_EtsysDot1xAuthSuppTimeout_Object=MibTableColumn
etsysDot1xAuthSuppTimeout=_EtsysDot1xAuthSuppTimeout_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,2,1,9),_EtsysDot1xAuthSuppTimeout_Type())
etsysDot1xAuthSuppTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthSuppTimeout.setStatus(_A)
_EtsysDot1xAuthServerTimeout_Type=Unsigned32
_EtsysDot1xAuthServerTimeout_Object=MibTableColumn
etsysDot1xAuthServerTimeout=_EtsysDot1xAuthServerTimeout_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,2,1,10),_EtsysDot1xAuthServerTimeout_Type())
etsysDot1xAuthServerTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthServerTimeout.setStatus(_A)
_EtsysDot1xAuthMaxReq_Type=Unsigned32
_EtsysDot1xAuthMaxReq_Object=MibTableColumn
etsysDot1xAuthMaxReq=_EtsysDot1xAuthMaxReq_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,2,1,11),_EtsysDot1xAuthMaxReq_Type())
etsysDot1xAuthMaxReq.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthMaxReq.setStatus(_A)
_EtsysDot1xAuthReAuthPeriod_Type=Unsigned32
_EtsysDot1xAuthReAuthPeriod_Object=MibTableColumn
etsysDot1xAuthReAuthPeriod=_EtsysDot1xAuthReAuthPeriod_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,2,1,12),_EtsysDot1xAuthReAuthPeriod_Type())
etsysDot1xAuthReAuthPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthReAuthPeriod.setStatus(_A)
class _EtsysDot1xAuthReAuthEnabled_Type(TruthValue):defaultValue=2
_EtsysDot1xAuthReAuthEnabled_Type.__name__=_I
_EtsysDot1xAuthReAuthEnabled_Object=MibTableColumn
etsysDot1xAuthReAuthEnabled=_EtsysDot1xAuthReAuthEnabled_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,2,1,13),_EtsysDot1xAuthReAuthEnabled_Type())
etsysDot1xAuthReAuthEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthReAuthEnabled.setStatus(_A)
_EtsysDot1xAuthKeyTxEnabled_Type=TruthValue
_EtsysDot1xAuthKeyTxEnabled_Object=MibTableColumn
etsysDot1xAuthKeyTxEnabled=_EtsysDot1xAuthKeyTxEnabled_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,2,1,14),_EtsysDot1xAuthKeyTxEnabled_Type())
etsysDot1xAuthKeyTxEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthKeyTxEnabled.setStatus(_A)
_EtsysDot1xAuthStatsTable_Object=MibTable
etsysDot1xAuthStatsTable=_EtsysDot1xAuthStatsTable_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,3))
if mibBuilder.loadTexts:etsysDot1xAuthStatsTable.setStatus(_A)
_EtsysDot1xAuthStatsEntry_Object=MibTableRow
etsysDot1xAuthStatsEntry=_EtsysDot1xAuthStatsEntry_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,3,1))
etsysDot1xAuthStatsEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:etsysDot1xAuthStatsEntry.setStatus(_A)
_EtsysDot1xAuthEapolFramesRx_Type=Counter32
_EtsysDot1xAuthEapolFramesRx_Object=MibTableColumn
etsysDot1xAuthEapolFramesRx=_EtsysDot1xAuthEapolFramesRx_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,3,1,1),_EtsysDot1xAuthEapolFramesRx_Type())
etsysDot1xAuthEapolFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthEapolFramesRx.setStatus(_A)
_EtsysDot1xAuthEapolFramesTx_Type=Counter32
_EtsysDot1xAuthEapolFramesTx_Object=MibTableColumn
etsysDot1xAuthEapolFramesTx=_EtsysDot1xAuthEapolFramesTx_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,3,1,2),_EtsysDot1xAuthEapolFramesTx_Type())
etsysDot1xAuthEapolFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthEapolFramesTx.setStatus(_A)
_EtsysDot1xAuthEapolStartFramesRx_Type=Counter32
_EtsysDot1xAuthEapolStartFramesRx_Object=MibTableColumn
etsysDot1xAuthEapolStartFramesRx=_EtsysDot1xAuthEapolStartFramesRx_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,3,1,3),_EtsysDot1xAuthEapolStartFramesRx_Type())
etsysDot1xAuthEapolStartFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthEapolStartFramesRx.setStatus(_A)
_EtsysDot1xAuthEapolLogoffFramesRx_Type=Counter32
_EtsysDot1xAuthEapolLogoffFramesRx_Object=MibTableColumn
etsysDot1xAuthEapolLogoffFramesRx=_EtsysDot1xAuthEapolLogoffFramesRx_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,3,1,4),_EtsysDot1xAuthEapolLogoffFramesRx_Type())
etsysDot1xAuthEapolLogoffFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthEapolLogoffFramesRx.setStatus(_A)
_EtsysDot1xAuthEapolRespIdFramesRx_Type=Counter32
_EtsysDot1xAuthEapolRespIdFramesRx_Object=MibTableColumn
etsysDot1xAuthEapolRespIdFramesRx=_EtsysDot1xAuthEapolRespIdFramesRx_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,3,1,5),_EtsysDot1xAuthEapolRespIdFramesRx_Type())
etsysDot1xAuthEapolRespIdFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthEapolRespIdFramesRx.setStatus(_A)
_EtsysDot1xAuthEapolRespFramesRx_Type=Counter32
_EtsysDot1xAuthEapolRespFramesRx_Object=MibTableColumn
etsysDot1xAuthEapolRespFramesRx=_EtsysDot1xAuthEapolRespFramesRx_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,3,1,6),_EtsysDot1xAuthEapolRespFramesRx_Type())
etsysDot1xAuthEapolRespFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthEapolRespFramesRx.setStatus(_A)
_EtsysDot1xAuthEapolReqIdFramesTx_Type=Counter32
_EtsysDot1xAuthEapolReqIdFramesTx_Object=MibTableColumn
etsysDot1xAuthEapolReqIdFramesTx=_EtsysDot1xAuthEapolReqIdFramesTx_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,3,1,7),_EtsysDot1xAuthEapolReqIdFramesTx_Type())
etsysDot1xAuthEapolReqIdFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthEapolReqIdFramesTx.setStatus(_A)
_EtsysDot1xAuthEapolReqFramesTx_Type=Counter32
_EtsysDot1xAuthEapolReqFramesTx_Object=MibTableColumn
etsysDot1xAuthEapolReqFramesTx=_EtsysDot1xAuthEapolReqFramesTx_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,3,1,8),_EtsysDot1xAuthEapolReqFramesTx_Type())
etsysDot1xAuthEapolReqFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthEapolReqFramesTx.setStatus(_A)
_EtsysDot1xAuthInvalidEapolFramesRx_Type=Counter32
_EtsysDot1xAuthInvalidEapolFramesRx_Object=MibTableColumn
etsysDot1xAuthInvalidEapolFramesRx=_EtsysDot1xAuthInvalidEapolFramesRx_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,3,1,9),_EtsysDot1xAuthInvalidEapolFramesRx_Type())
etsysDot1xAuthInvalidEapolFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthInvalidEapolFramesRx.setStatus(_A)
_EtsysDot1xAuthEapLengthErrorFramesRx_Type=Counter32
_EtsysDot1xAuthEapLengthErrorFramesRx_Object=MibTableColumn
etsysDot1xAuthEapLengthErrorFramesRx=_EtsysDot1xAuthEapLengthErrorFramesRx_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,3,1,10),_EtsysDot1xAuthEapLengthErrorFramesRx_Type())
etsysDot1xAuthEapLengthErrorFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthEapLengthErrorFramesRx.setStatus(_A)
_EtsysDot1xAuthLastEapolFrameVersion_Type=Unsigned32
_EtsysDot1xAuthLastEapolFrameVersion_Object=MibTableColumn
etsysDot1xAuthLastEapolFrameVersion=_EtsysDot1xAuthLastEapolFrameVersion_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,3,1,11),_EtsysDot1xAuthLastEapolFrameVersion_Type())
etsysDot1xAuthLastEapolFrameVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthLastEapolFrameVersion.setStatus(_A)
_EtsysDot1xAuthLastEapolFrameSource_Type=MacAddress
_EtsysDot1xAuthLastEapolFrameSource_Object=MibTableColumn
etsysDot1xAuthLastEapolFrameSource=_EtsysDot1xAuthLastEapolFrameSource_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,3,1,12),_EtsysDot1xAuthLastEapolFrameSource_Type())
etsysDot1xAuthLastEapolFrameSource.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthLastEapolFrameSource.setStatus('deprecated')
_EtsysDot1xAuthDiagTable_Object=MibTable
etsysDot1xAuthDiagTable=_EtsysDot1xAuthDiagTable_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,4))
if mibBuilder.loadTexts:etsysDot1xAuthDiagTable.setStatus(_A)
_EtsysDot1xAuthDiagEntry_Object=MibTableRow
etsysDot1xAuthDiagEntry=_EtsysDot1xAuthDiagEntry_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,4,1))
etsysDot1xAuthDiagEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:etsysDot1xAuthDiagEntry.setStatus(_A)
_EtsysDot1xAuthEntersConnecting_Type=Counter32
_EtsysDot1xAuthEntersConnecting_Object=MibTableColumn
etsysDot1xAuthEntersConnecting=_EtsysDot1xAuthEntersConnecting_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,4,1,1),_EtsysDot1xAuthEntersConnecting_Type())
etsysDot1xAuthEntersConnecting.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthEntersConnecting.setStatus(_A)
_EtsysDot1xAuthEapLogoffsWhileConnecting_Type=Counter32
_EtsysDot1xAuthEapLogoffsWhileConnecting_Object=MibTableColumn
etsysDot1xAuthEapLogoffsWhileConnecting=_EtsysDot1xAuthEapLogoffsWhileConnecting_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,4,1,2),_EtsysDot1xAuthEapLogoffsWhileConnecting_Type())
etsysDot1xAuthEapLogoffsWhileConnecting.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthEapLogoffsWhileConnecting.setStatus(_A)
_EtsysDot1xAuthEntersAuthenticating_Type=Counter32
_EtsysDot1xAuthEntersAuthenticating_Object=MibTableColumn
etsysDot1xAuthEntersAuthenticating=_EtsysDot1xAuthEntersAuthenticating_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,4,1,3),_EtsysDot1xAuthEntersAuthenticating_Type())
etsysDot1xAuthEntersAuthenticating.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthEntersAuthenticating.setStatus(_A)
_EtsysDot1xAuthAuthSuccessWhileAuthenticating_Type=Counter32
_EtsysDot1xAuthAuthSuccessWhileAuthenticating_Object=MibTableColumn
etsysDot1xAuthAuthSuccessWhileAuthenticating=_EtsysDot1xAuthAuthSuccessWhileAuthenticating_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,4,1,4),_EtsysDot1xAuthAuthSuccessWhileAuthenticating_Type())
etsysDot1xAuthAuthSuccessWhileAuthenticating.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthAuthSuccessWhileAuthenticating.setStatus(_A)
_EtsysDot1xAuthAuthTimeoutsWhileAuthenticating_Type=Counter32
_EtsysDot1xAuthAuthTimeoutsWhileAuthenticating_Object=MibTableColumn
etsysDot1xAuthAuthTimeoutsWhileAuthenticating=_EtsysDot1xAuthAuthTimeoutsWhileAuthenticating_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,4,1,5),_EtsysDot1xAuthAuthTimeoutsWhileAuthenticating_Type())
etsysDot1xAuthAuthTimeoutsWhileAuthenticating.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthAuthTimeoutsWhileAuthenticating.setStatus(_A)
_EtsysDot1xAuthAuthFailWhileAuthenticating_Type=Counter32
_EtsysDot1xAuthAuthFailWhileAuthenticating_Object=MibTableColumn
etsysDot1xAuthAuthFailWhileAuthenticating=_EtsysDot1xAuthAuthFailWhileAuthenticating_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,4,1,6),_EtsysDot1xAuthAuthFailWhileAuthenticating_Type())
etsysDot1xAuthAuthFailWhileAuthenticating.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthAuthFailWhileAuthenticating.setStatus(_A)
_EtsysDot1xAuthAuthReauthsWhileAuthenticating_Type=Counter32
_EtsysDot1xAuthAuthReauthsWhileAuthenticating_Object=MibTableColumn
etsysDot1xAuthAuthReauthsWhileAuthenticating=_EtsysDot1xAuthAuthReauthsWhileAuthenticating_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,4,1,7),_EtsysDot1xAuthAuthReauthsWhileAuthenticating_Type())
etsysDot1xAuthAuthReauthsWhileAuthenticating.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthAuthReauthsWhileAuthenticating.setStatus(_A)
_EtsysDot1xAuthAuthEapStartsWhileAuthenticating_Type=Counter32
_EtsysDot1xAuthAuthEapStartsWhileAuthenticating_Object=MibTableColumn
etsysDot1xAuthAuthEapStartsWhileAuthenticating=_EtsysDot1xAuthAuthEapStartsWhileAuthenticating_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,4,1,8),_EtsysDot1xAuthAuthEapStartsWhileAuthenticating_Type())
etsysDot1xAuthAuthEapStartsWhileAuthenticating.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthAuthEapStartsWhileAuthenticating.setStatus(_A)
_EtsysDot1xAuthAuthEapLogoffWhileAuthenticating_Type=Counter32
_EtsysDot1xAuthAuthEapLogoffWhileAuthenticating_Object=MibTableColumn
etsysDot1xAuthAuthEapLogoffWhileAuthenticating=_EtsysDot1xAuthAuthEapLogoffWhileAuthenticating_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,4,1,9),_EtsysDot1xAuthAuthEapLogoffWhileAuthenticating_Type())
etsysDot1xAuthAuthEapLogoffWhileAuthenticating.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthAuthEapLogoffWhileAuthenticating.setStatus(_A)
_EtsysDot1xAuthAuthReauthsWhileAuthenticated_Type=Counter32
_EtsysDot1xAuthAuthReauthsWhileAuthenticated_Object=MibTableColumn
etsysDot1xAuthAuthReauthsWhileAuthenticated=_EtsysDot1xAuthAuthReauthsWhileAuthenticated_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,4,1,10),_EtsysDot1xAuthAuthReauthsWhileAuthenticated_Type())
etsysDot1xAuthAuthReauthsWhileAuthenticated.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthAuthReauthsWhileAuthenticated.setStatus(_A)
_EtsysDot1xAuthAuthEapStartsWhileAuthenticated_Type=Counter32
_EtsysDot1xAuthAuthEapStartsWhileAuthenticated_Object=MibTableColumn
etsysDot1xAuthAuthEapStartsWhileAuthenticated=_EtsysDot1xAuthAuthEapStartsWhileAuthenticated_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,4,1,11),_EtsysDot1xAuthAuthEapStartsWhileAuthenticated_Type())
etsysDot1xAuthAuthEapStartsWhileAuthenticated.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthAuthEapStartsWhileAuthenticated.setStatus(_A)
_EtsysDot1xAuthAuthEapLogoffWhileAuthenticated_Type=Counter32
_EtsysDot1xAuthAuthEapLogoffWhileAuthenticated_Object=MibTableColumn
etsysDot1xAuthAuthEapLogoffWhileAuthenticated=_EtsysDot1xAuthAuthEapLogoffWhileAuthenticated_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,4,1,12),_EtsysDot1xAuthAuthEapLogoffWhileAuthenticated_Type())
etsysDot1xAuthAuthEapLogoffWhileAuthenticated.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthAuthEapLogoffWhileAuthenticated.setStatus(_A)
_EtsysDot1xAuthBackendResponses_Type=Counter32
_EtsysDot1xAuthBackendResponses_Object=MibTableColumn
etsysDot1xAuthBackendResponses=_EtsysDot1xAuthBackendResponses_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,4,1,13),_EtsysDot1xAuthBackendResponses_Type())
etsysDot1xAuthBackendResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthBackendResponses.setStatus(_A)
_EtsysDot1xAuthBackendAccessChallenges_Type=Counter32
_EtsysDot1xAuthBackendAccessChallenges_Object=MibTableColumn
etsysDot1xAuthBackendAccessChallenges=_EtsysDot1xAuthBackendAccessChallenges_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,4,1,14),_EtsysDot1xAuthBackendAccessChallenges_Type())
etsysDot1xAuthBackendAccessChallenges.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthBackendAccessChallenges.setStatus(_A)
_EtsysDot1xAuthBackendOtherRequestsToSupplicant_Type=Counter32
_EtsysDot1xAuthBackendOtherRequestsToSupplicant_Object=MibTableColumn
etsysDot1xAuthBackendOtherRequestsToSupplicant=_EtsysDot1xAuthBackendOtherRequestsToSupplicant_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,4,1,15),_EtsysDot1xAuthBackendOtherRequestsToSupplicant_Type())
etsysDot1xAuthBackendOtherRequestsToSupplicant.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthBackendOtherRequestsToSupplicant.setStatus(_A)
_EtsysDot1xAuthBackendNonNakResponsesFromSupplicant_Type=Counter32
_EtsysDot1xAuthBackendNonNakResponsesFromSupplicant_Object=MibTableColumn
etsysDot1xAuthBackendNonNakResponsesFromSupplicant=_EtsysDot1xAuthBackendNonNakResponsesFromSupplicant_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,4,1,16),_EtsysDot1xAuthBackendNonNakResponsesFromSupplicant_Type())
etsysDot1xAuthBackendNonNakResponsesFromSupplicant.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthBackendNonNakResponsesFromSupplicant.setStatus(_A)
_EtsysDot1xAuthBackendAuthSuccesses_Type=Counter32
_EtsysDot1xAuthBackendAuthSuccesses_Object=MibTableColumn
etsysDot1xAuthBackendAuthSuccesses=_EtsysDot1xAuthBackendAuthSuccesses_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,4,1,17),_EtsysDot1xAuthBackendAuthSuccesses_Type())
etsysDot1xAuthBackendAuthSuccesses.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthBackendAuthSuccesses.setStatus(_A)
_EtsysDot1xAuthBackendAuthFails_Type=Counter32
_EtsysDot1xAuthBackendAuthFails_Object=MibTableColumn
etsysDot1xAuthBackendAuthFails=_EtsysDot1xAuthBackendAuthFails_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,4,1,18),_EtsysDot1xAuthBackendAuthFails_Type())
etsysDot1xAuthBackendAuthFails.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthBackendAuthFails.setStatus(_A)
_EtsysDot1xAuthSessionStatsTable_Object=MibTable
etsysDot1xAuthSessionStatsTable=_EtsysDot1xAuthSessionStatsTable_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,5))
if mibBuilder.loadTexts:etsysDot1xAuthSessionStatsTable.setStatus(_A)
_EtsysDot1xAuthSessionStatsEntry_Object=MibTableRow
etsysDot1xAuthSessionStatsEntry=_EtsysDot1xAuthSessionStatsEntry_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,5,1))
etsysDot1xAuthSessionStatsEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:etsysDot1xAuthSessionStatsEntry.setStatus(_A)
_EtsysDot1xAuthSessionOctetsRx_Type=Counter64
_EtsysDot1xAuthSessionOctetsRx_Object=MibTableColumn
etsysDot1xAuthSessionOctetsRx=_EtsysDot1xAuthSessionOctetsRx_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,5,1,1),_EtsysDot1xAuthSessionOctetsRx_Type())
etsysDot1xAuthSessionOctetsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthSessionOctetsRx.setStatus(_A)
_EtsysDot1xAuthSessionOctetsTx_Type=Counter64
_EtsysDot1xAuthSessionOctetsTx_Object=MibTableColumn
etsysDot1xAuthSessionOctetsTx=_EtsysDot1xAuthSessionOctetsTx_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,5,1,2),_EtsysDot1xAuthSessionOctetsTx_Type())
etsysDot1xAuthSessionOctetsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthSessionOctetsTx.setStatus(_A)
_EtsysDot1xAuthSessionFramesRx_Type=Counter32
_EtsysDot1xAuthSessionFramesRx_Object=MibTableColumn
etsysDot1xAuthSessionFramesRx=_EtsysDot1xAuthSessionFramesRx_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,5,1,3),_EtsysDot1xAuthSessionFramesRx_Type())
etsysDot1xAuthSessionFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthSessionFramesRx.setStatus(_A)
_EtsysDot1xAuthSessionFramesTx_Type=Counter32
_EtsysDot1xAuthSessionFramesTx_Object=MibTableColumn
etsysDot1xAuthSessionFramesTx=_EtsysDot1xAuthSessionFramesTx_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,5,1,4),_EtsysDot1xAuthSessionFramesTx_Type())
etsysDot1xAuthSessionFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthSessionFramesTx.setStatus(_A)
_EtsysDot1xAuthSessionId_Type=SnmpAdminString
_EtsysDot1xAuthSessionId_Object=MibTableColumn
etsysDot1xAuthSessionId=_EtsysDot1xAuthSessionId_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,5,1,5),_EtsysDot1xAuthSessionId_Type())
etsysDot1xAuthSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthSessionId.setStatus(_A)
class _EtsysDot1xAuthSessionAuthenticMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('remoteAuthServer',1),('localAuthServer',2)))
_EtsysDot1xAuthSessionAuthenticMethod_Type.__name__=_E
_EtsysDot1xAuthSessionAuthenticMethod_Object=MibTableColumn
etsysDot1xAuthSessionAuthenticMethod=_EtsysDot1xAuthSessionAuthenticMethod_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,5,1,6),_EtsysDot1xAuthSessionAuthenticMethod_Type())
etsysDot1xAuthSessionAuthenticMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthSessionAuthenticMethod.setStatus(_A)
_EtsysDot1xAuthSessionTime_Type=TimeTicks
_EtsysDot1xAuthSessionTime_Object=MibTableColumn
etsysDot1xAuthSessionTime=_EtsysDot1xAuthSessionTime_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,5,1,7),_EtsysDot1xAuthSessionTime_Type())
etsysDot1xAuthSessionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthSessionTime.setStatus(_A)
class _EtsysDot1xAuthSessionTerminateCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,999)));namedValues=NamedValues(*(('supplicantLogoff',1),('portFailure',2),('supplicantRestart',3),('reauthFailed',4),('authControlForceUnauth',5),('portReInit',6),('portAdminDisabled',7),('notTerminatedYet',999)))
_EtsysDot1xAuthSessionTerminateCause_Type.__name__=_E
_EtsysDot1xAuthSessionTerminateCause_Object=MibTableColumn
etsysDot1xAuthSessionTerminateCause=_EtsysDot1xAuthSessionTerminateCause_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,5,1,8),_EtsysDot1xAuthSessionTerminateCause_Type())
etsysDot1xAuthSessionTerminateCause.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthSessionTerminateCause.setStatus(_A)
class _EtsysDot1xAuthStatsSupported_Type(Bits):namedValues=NamedValues(*(('etsysDot1xAuthEapolFramesRxSupported',0),('etsysDot1xAuthEapolFramesTxSupported',1),('etsysDot1xAuthEapolStartFramesRxSupported',2),('etsysDot1xAuthEapolLogoffFramesRxSupported',3),('etsysDot1xAuthEapolRespIdFramesRxSupported',4),('etsysDot1xAuthEapolRespFramesRxSupported',5),('etsysDot1xAuthEapolReqIdFramesTxSupported',6),('etsysDot1xAuthEapolReqFramesTxSupported',7),('etsysDot1xAuthInvalidEapolFramesRxSupported',8),('etsysDot1xAuthEapLengthErrorFramesRxSupported',9),('etsysDot1xAuthLastEapolFrameVersionSupported',10)))
_EtsysDot1xAuthStatsSupported_Type.__name__=_F
_EtsysDot1xAuthStatsSupported_Object=MibScalar
etsysDot1xAuthStatsSupported=_EtsysDot1xAuthStatsSupported_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,6),_EtsysDot1xAuthStatsSupported_Type())
etsysDot1xAuthStatsSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthStatsSupported.setStatus(_A)
class _EtsysDot1xAuthDiagSupported_Type(Bits):namedValues=NamedValues(*(('etsysDot1xAuthEntersConnectingSupported',0),('etsysDot1xAuthEapLogoffsWhileConnectingSupported',1),('etsysDot1xAuthEntersAuthenticatingSupported',2),('etsysDot1xAuthAuthSuccessWhileAuthenticatingSupported',3),('etsysDot1xAuthAuthTimeoutsWhileAuthenticatingSupported',4),('etsysDot1xAuthAuthFailWhileAuthenticatingSupported',5),('etsysDot1xAuthAuthReauthsWhileAuthenticatingSupported',6),('etsysDot1xAuthAuthEapStartsWhileAuthenticatingSupported',7),('etsysDot1xAuthAuthEapLogoffWhileAuthenticatingSupported',8),('etsysDot1xAuthAuthReauthsWhileAuthenticatedSupported',9),('etsysDot1xAuthAuthEapStartsWhileAuthenticatedSupported',10),('etsysDot1xAuthAuthEapLogoffWhileAuthenticatedSupported',11),('etsysDot1xAuthBackendResponsesSupported',12),('etsysDot1xAuthBackendAccessChallengesSupported',13),('etsysDot1xAuthBackendOtherRequestsToSupplicantSupported',14),('etsysDot1xAuthBackendNonNakResponsesFromSupplicantSupported',15),('etsysDot1xAuthBackendAuthSuccessesSupported',16),('etsysDot1xAuthBackendAuthFailsSupported',17)))
_EtsysDot1xAuthDiagSupported_Type.__name__=_F
_EtsysDot1xAuthDiagSupported_Object=MibScalar
etsysDot1xAuthDiagSupported=_EtsysDot1xAuthDiagSupported_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,7),_EtsysDot1xAuthDiagSupported_Type())
etsysDot1xAuthDiagSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthDiagSupported.setStatus(_A)
class _EtsysDot1xAuthSessionSuppportedObjs_Type(Bits):namedValues=NamedValues(*(('etsysDot1xAuthSessionOctetsRxSupported',0),('etsysDot1xAuthSessionOctetsTxSupported',1),('etsysDot1xAuthSessionFramesRxSupported',2),('etsysDot1xAuthSessionFramesTxSupported',3),('etsysDot1xAuthSessionIdSupported',4),('etsysDot1xAuthSessionAuthenticMethodSupported',5),('etsysDot1xAuthSessionTimeSupported',6),('etsysDot1xAuthSessionTerminateCauseSupported',7)))
_EtsysDot1xAuthSessionSuppportedObjs_Type.__name__=_F
_EtsysDot1xAuthSessionSuppportedObjs_Object=MibScalar
etsysDot1xAuthSessionSuppportedObjs=_EtsysDot1xAuthSessionSuppportedObjs_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,8),_EtsysDot1xAuthSessionSuppportedObjs_Type())
etsysDot1xAuthSessionSuppportedObjs.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xAuthSessionSuppportedObjs.setStatus(_A)
class _EtsysDot1xMaxCapableAuthStations_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_EtsysDot1xMaxCapableAuthStations_Type.__name__=_G
_EtsysDot1xMaxCapableAuthStations_Object=MibScalar
etsysDot1xMaxCapableAuthStations=_EtsysDot1xMaxCapableAuthStations_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,9),_EtsysDot1xMaxCapableAuthStations_Type())
etsysDot1xMaxCapableAuthStations.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xMaxCapableAuthStations.setStatus(_A)
class _EtsysDot1xMaximumStationsStatsGathered_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_EtsysDot1xMaximumStationsStatsGathered_Type.__name__=_G
_EtsysDot1xMaximumStationsStatsGathered_Object=MibScalar
etsysDot1xMaximumStationsStatsGathered=_EtsysDot1xMaximumStationsStatsGathered_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,10),_EtsysDot1xMaximumStationsStatsGathered_Type())
etsysDot1xMaximumStationsStatsGathered.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xMaximumStationsStatsGathered.setStatus(_A)
class _EtsysDot1xCurrentStationsStatsGathered_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_EtsysDot1xCurrentStationsStatsGathered_Type.__name__=_G
_EtsysDot1xCurrentStationsStatsGathered_Object=MibScalar
etsysDot1xCurrentStationsStatsGathered=_EtsysDot1xCurrentStationsStatsGathered_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,11),_EtsysDot1xCurrentStationsStatsGathered_Type())
etsysDot1xCurrentStationsStatsGathered.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xCurrentStationsStatsGathered.setStatus(_A)
_EtsysDot1xAuthStationWatchTable_Object=MibTable
etsysDot1xAuthStationWatchTable=_EtsysDot1xAuthStationWatchTable_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,12))
if mibBuilder.loadTexts:etsysDot1xAuthStationWatchTable.setStatus(_A)
_EtsysDot1xAuthStationWatchEntry_Object=MibTableRow
etsysDot1xAuthStationWatchEntry=_EtsysDot1xAuthStationWatchEntry_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,12,1))
etsysDot1xAuthStationWatchEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:etsysDot1xAuthStationWatchEntry.setStatus(_A)
_EtsysDot1xAuthInfoStationAddress_Type=MacAddress
_EtsysDot1xAuthInfoStationAddress_Object=MibTableColumn
etsysDot1xAuthInfoStationAddress=_EtsysDot1xAuthInfoStationAddress_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,12,1,1),_EtsysDot1xAuthInfoStationAddress_Type())
etsysDot1xAuthInfoStationAddress.setMaxAccess(_L)
if mibBuilder.loadTexts:etsysDot1xAuthInfoStationAddress.setStatus(_A)
_EtsysDot1xAuthInfoStationRowStatus_Type=RowStatus
_EtsysDot1xAuthInfoStationRowStatus_Object=MibTableColumn
etsysDot1xAuthInfoStationRowStatus=_EtsysDot1xAuthInfoStationRowStatus_Object((1,3,6,1,4,1,5624,1,2,18,1,2,1,12,1,2),_EtsysDot1xAuthInfoStationRowStatus_Type())
etsysDot1xAuthInfoStationRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:etsysDot1xAuthInfoStationRowStatus.setStatus(_A)
_EtsysDot1xSupplicantBranch_ObjectIdentity=ObjectIdentity
etsysDot1xSupplicantBranch=_EtsysDot1xSupplicantBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,18,1,3))
_EtsysDot1xConformance_ObjectIdentity=ObjectIdentity
etsysDot1xConformance=_EtsysDot1xConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,18,2))
_EtsysDot1xGroups_ObjectIdentity=ObjectIdentity
etsysDot1xGroups=_EtsysDot1xGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,18,2,1))
_EtsysDot1xCompliances_ObjectIdentity=ObjectIdentity
etsysDot1xCompliances=_EtsysDot1xCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,18,2,2))
etsysDot1xAuthStationGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,18,2,1,1))
etsysDot1xAuthStationGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:etsysDot1xAuthStationGroup.setStatus(_A)
etsysDot1xAuthConfigGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,18,2,1,2))
etsysDot1xAuthConfigGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:etsysDot1xAuthConfigGroup.setStatus(_A)
etsysDot1xAuthStatsGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,18,2,1,3))
etsysDot1xAuthStatsGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:etsysDot1xAuthStatsGroup.setStatus(_A)
etsysDot1xAuthDiagGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,18,2,1,4))
etsysDot1xAuthDiagGroup.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:etsysDot1xAuthDiagGroup.setStatus(_A)
etsysDot1xAuthSessionStatsGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,18,2,1,5))
etsysDot1xAuthSessionStatsGroup.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:etsysDot1xAuthSessionStatsGroup.setStatus(_A)
etsysDot1xAuthSessionControlGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,18,2,1,6))
etsysDot1xAuthSessionControlGroup.setObjects(*((_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_H),(_B,_AK)))
if mibBuilder.loadTexts:etsysDot1xAuthSessionControlGroup.setStatus(_A)
etsysDot1xCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,18,2,2,1))
etsysDot1xCompliance.setObjects(*((_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ)))
if mibBuilder.loadTexts:etsysDot1xCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsys8021xExtensionsMIB':etsys8021xExtensionsMIB,'etsysDot1xExtensionsObjects':etsysDot1xExtensionsObjects,'etsysDot1xSystemBranch':etsysDot1xSystemBranch,'etsysDot1xAuthenticatorBranch':etsysDot1xAuthenticatorBranch,'etsysDot1xAuthStationBranch':etsysDot1xAuthStationBranch,'etsysDot1xAuthStationTable':etsysDot1xAuthStationTable,'etsysDot1xAuthStationEntry':etsysDot1xAuthStationEntry,_D:etsysDot1xAuthStationAddress,_M:etsysDot1xAuthStationPaePort,_N:etsysDot1xAuthStationPaeState,_O:etsysDot1xAuthStationBackendAuthState,_P:etsysDot1xAuthStationUserName,'etsysDot1xAuthConfigTable':etsysDot1xAuthConfigTable,'etsysDot1xAuthConfigEntry':etsysDot1xAuthConfigEntry,_Q:etsysDot1xAuthInitialize,_R:etsysDot1xAuthReauthenticate,_S:etsysDot1xAuthAdminControlledDirections,_T:etsysDot1xAuthOperControlledDirections,_U:etsysDot1xAuthAuthControlledPortStatus,_V:etsysDot1xAuthAuthControlledPortControl,_W:etsysDot1xAuthQuietPeriod,_X:etsysDot1xAuthTxPeriod,_Y:etsysDot1xAuthSuppTimeout,_Z:etsysDot1xAuthServerTimeout,_a:etsysDot1xAuthMaxReq,_b:etsysDot1xAuthReAuthPeriod,_c:etsysDot1xAuthReAuthEnabled,_d:etsysDot1xAuthKeyTxEnabled,'etsysDot1xAuthStatsTable':etsysDot1xAuthStatsTable,'etsysDot1xAuthStatsEntry':etsysDot1xAuthStatsEntry,_e:etsysDot1xAuthEapolFramesRx,_f:etsysDot1xAuthEapolFramesTx,_g:etsysDot1xAuthEapolStartFramesRx,_h:etsysDot1xAuthEapolLogoffFramesRx,_i:etsysDot1xAuthEapolRespIdFramesRx,_j:etsysDot1xAuthEapolRespFramesRx,_k:etsysDot1xAuthEapolReqIdFramesTx,_l:etsysDot1xAuthEapolReqFramesTx,_m:etsysDot1xAuthInvalidEapolFramesRx,_n:etsysDot1xAuthEapLengthErrorFramesRx,_o:etsysDot1xAuthLastEapolFrameVersion,_p:etsysDot1xAuthLastEapolFrameSource,'etsysDot1xAuthDiagTable':etsysDot1xAuthDiagTable,'etsysDot1xAuthDiagEntry':etsysDot1xAuthDiagEntry,_q:etsysDot1xAuthEntersConnecting,_r:etsysDot1xAuthEapLogoffsWhileConnecting,_s:etsysDot1xAuthEntersAuthenticating,_t:etsysDot1xAuthAuthSuccessWhileAuthenticating,_u:etsysDot1xAuthAuthTimeoutsWhileAuthenticating,_v:etsysDot1xAuthAuthFailWhileAuthenticating,_w:etsysDot1xAuthAuthReauthsWhileAuthenticating,_x:etsysDot1xAuthAuthEapStartsWhileAuthenticating,_y:etsysDot1xAuthAuthEapLogoffWhileAuthenticating,_z:etsysDot1xAuthAuthReauthsWhileAuthenticated,_A0:etsysDot1xAuthAuthEapStartsWhileAuthenticated,_A1:etsysDot1xAuthAuthEapLogoffWhileAuthenticated,_A2:etsysDot1xAuthBackendResponses,_A3:etsysDot1xAuthBackendAccessChallenges,_A4:etsysDot1xAuthBackendOtherRequestsToSupplicant,_A5:etsysDot1xAuthBackendNonNakResponsesFromSupplicant,_A6:etsysDot1xAuthBackendAuthSuccesses,_A7:etsysDot1xAuthBackendAuthFails,'etsysDot1xAuthSessionStatsTable':etsysDot1xAuthSessionStatsTable,'etsysDot1xAuthSessionStatsEntry':etsysDot1xAuthSessionStatsEntry,_A8:etsysDot1xAuthSessionOctetsRx,_A9:etsysDot1xAuthSessionOctetsTx,_AA:etsysDot1xAuthSessionFramesRx,_AB:etsysDot1xAuthSessionFramesTx,_AC:etsysDot1xAuthSessionId,_AD:etsysDot1xAuthSessionAuthenticMethod,_AE:etsysDot1xAuthSessionTime,_AF:etsysDot1xAuthSessionTerminateCause,'etsysDot1xAuthStatsSupported':etsysDot1xAuthStatsSupported,'etsysDot1xAuthDiagSupported':etsysDot1xAuthDiagSupported,_AG:etsysDot1xAuthSessionSuppportedObjs,_AH:etsysDot1xMaxCapableAuthStations,_AJ:etsysDot1xMaximumStationsStatsGathered,_AI:etsysDot1xCurrentStationsStatsGathered,'etsysDot1xAuthStationWatchTable':etsysDot1xAuthStationWatchTable,'etsysDot1xAuthStationWatchEntry':etsysDot1xAuthStationWatchEntry,_H:etsysDot1xAuthInfoStationAddress,_AK:etsysDot1xAuthInfoStationRowStatus,'etsysDot1xSupplicantBranch':etsysDot1xSupplicantBranch,'etsysDot1xConformance':etsysDot1xConformance,'etsysDot1xGroups':etsysDot1xGroups,_AL:etsysDot1xAuthStationGroup,_AM:etsysDot1xAuthConfigGroup,_AN:etsysDot1xAuthStatsGroup,_AO:etsysDot1xAuthDiagGroup,_AP:etsysDot1xAuthSessionStatsGroup,_AQ:etsysDot1xAuthSessionControlGroup,'etsysDot1xCompliances':etsysDot1xCompliances,'etsysDot1xCompliance':etsysDot1xCompliance})