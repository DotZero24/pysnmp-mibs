_As='dot1xPaeSuppConfigGroup2'
_Ar='dot1xPaeSuppStatsGroup2'
_Aq='dot1xPaeAuthConfigGroup2'
_Ap='dot1xPaeSuppStatsGroup'
_Ao='dot1xPaeAuthDiagGroup'
_An='dot1xPaeAuthConfigGroup'
_Am='dot1xSuppBackendState'
_Al='dot1xSuppAccessCtrlWithAuth'
_Ak='dot1xSuppControlledPortStatus'
_Aj='dot1xSuppEapolReqFramesRx'
_Ai='dot1xSuppEapolReqIdFramesRx'
_Ah='dot1xSuppEapolRespFramesTx'
_Ag='dot1xSuppEapolRespIdFramesTx'
_Af='dot1xSuppMaxStart'
_Ae='dot1xSuppStartPeriod'
_Ad='dot1xSuppAuthPeriod'
_Ac='dot1xSuppHeldPeriod'
_Ab='dot1xSuppPaeState'
_Aa='dot1xAuthSessionUserName'
_AZ='dot1xAuthSessionTerminateCause'
_AY='dot1xAuthSessionTime'
_AX='dot1xAuthSessionAuthenticMethod'
_AW='dot1xAuthSessionId'
_AV='dot1xAuthSessionFramesTx'
_AU='dot1xAuthSessionFramesRx'
_AT='dot1xAuthSessionOctetsTx'
_AS='dot1xAuthSessionOctetsRx'
_AR='dot1xAuthBackendAuthFails'
_AQ='dot1xAuthBackendAuthSuccesses'
_AP='dot1xAuthBackendNonNakResponsesFromSupplicant'
_AO='dot1xAuthBackendOtherRequestsToSupplicant'
_AN='dot1xAuthBackendAccessChallenges'
_AM='dot1xAuthBackendResponses'
_AL='dot1xAuthAuthEapLogoffWhileAuthenticated'
_AK='dot1xAuthAuthEapStartsWhileAuthenticated'
_AJ='dot1xAuthAuthReauthsWhileAuthenticated'
_AI='dot1xAuthAuthEapLogoffWhileAuthenticating'
_AH='dot1xAuthAuthEapStartsWhileAuthenticating'
_AG='dot1xAuthAuthReauthsWhileAuthenticating'
_AF='dot1xAuthAuthFailWhileAuthenticating'
_AE='dot1xAuthAuthTimeoutsWhileAuthenticating'
_AD='dot1xAuthAuthSuccessWhileAuthenticating'
_AC='dot1xAuthEntersAuthenticating'
_AB='dot1xAuthEapLogoffsWhileConnecting'
_AA='dot1xAuthEntersConnecting'
_A9='dot1xAuthLastEapolFrameSource'
_A8='dot1xAuthLastEapolFrameVersion'
_A7='dot1xAuthEapLengthErrorFramesRx'
_A6='dot1xAuthInvalidEapolFramesRx'
_A5='dot1xAuthEapolReqFramesTx'
_A4='dot1xAuthEapolReqIdFramesTx'
_A3='dot1xAuthEapolRespFramesRx'
_A2='dot1xAuthEapolRespIdFramesRx'
_A1='dot1xAuthEapolLogoffFramesRx'
_A0='dot1xAuthEapolStartFramesRx'
_z='dot1xAuthEapolFramesTx'
_y='dot1xAuthEapolFramesRx'
_x='dot1xAuthMaxReq'
_w='dot1xAuthSuppTimeout'
_v='dot1xAuthTxPeriod'
_u='dot1xPaePortReauthenticate'
_t='dot1xPaePortInitialize'
_s='dot1xPaePortCapabilities'
_r='dot1xPaePortProtocolVersion'
_q='dot1xPaeSystemAuthControl'
_p='timeout'
_o='success'
_n='response'
_m='request'
_l='restart'
_k='authenticated'
_j='authenticating'
_i='connecting'
_h='disconnected'
_g='TruthValue'
_f='dot1xPaeSuppConfigGroup'
_e='dot1xPaeAuthSessionStatsGroup'
_d='dot1xPaeAuthStatsGroup'
_c='dot1xPaeSystemGroup'
_b='dot1xSuppLastEapolFrameSource'
_a='dot1xSuppLastEapolFrameVersion'
_Z='dot1xSuppEapLengthErrorFramesRx'
_Y='dot1xSuppInvalidEapolFramesRx'
_X='dot1xSuppEapolLogoffFramesTx'
_W='dot1xSuppEapolStartFramesTx'
_V='dot1xSuppEapolFramesTx'
_U='dot1xSuppEapolFramesRx'
_T='dot1xAuthKeyTxEnabled'
_S='dot1xAuthReAuthEnabled'
_R='dot1xAuthReAuthPeriod'
_Q='dot1xAuthServerTimeout'
_P='dot1xAuthQuietPeriod'
_O='dot1xAuthAuthControlledPortControl'
_N='dot1xAuthAuthControlledPortStatus'
_M='dot1xAuthOperControlledDirections'
_L='dot1xAuthAdminControlledDirections'
_K='dot1xAuthBackendAuthState'
_J='dot1xAuthPaeState'
_I='initialize'
_H='dot1xPaePortNumber'
_G='Integer32'
_F='Unsigned32'
_E='read-write'
_D='deprecated'
_C='read-only'
_B='current'
_A='IEEE8021-PAE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_g)
ieee8021paeMIB=ModuleIdentity((1,0,8802,1,1,1))
if mibBuilder.loadTexts:ieee8021paeMIB.setRevisions(('2004-06-22 00:00','2001-01-16 00:00'))
class PaeControlledDirections(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('both',0),('in',1)))
class PaeControlledPortStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('authorized',1),('unauthorized',2)))
class PaeControlledPortControl(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('forceUnauthorized',1),('auto',2),('forceAuthorized',3)))
_PaeMIBObjects_ObjectIdentity=ObjectIdentity
paeMIBObjects=_PaeMIBObjects_ObjectIdentity((1,0,8802,1,1,1,1))
_Dot1xPaeSystem_ObjectIdentity=ObjectIdentity
dot1xPaeSystem=_Dot1xPaeSystem_ObjectIdentity((1,0,8802,1,1,1,1,1))
class _Dot1xPaeSystemAuthControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_Dot1xPaeSystemAuthControl_Type.__name__=_G
_Dot1xPaeSystemAuthControl_Object=MibScalar
dot1xPaeSystemAuthControl=_Dot1xPaeSystemAuthControl_Object((1,0,8802,1,1,1,1,1,1),_Dot1xPaeSystemAuthControl_Type())
dot1xPaeSystemAuthControl.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1xPaeSystemAuthControl.setStatus(_B)
_Dot1xPaePortTable_Object=MibTable
dot1xPaePortTable=_Dot1xPaePortTable_Object((1,0,8802,1,1,1,1,1,2))
if mibBuilder.loadTexts:dot1xPaePortTable.setStatus(_B)
_Dot1xPaePortEntry_Object=MibTableRow
dot1xPaePortEntry=_Dot1xPaePortEntry_Object((1,0,8802,1,1,1,1,1,2,1))
dot1xPaePortEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:dot1xPaePortEntry.setStatus(_B)
_Dot1xPaePortNumber_Type=InterfaceIndex
_Dot1xPaePortNumber_Object=MibTableColumn
dot1xPaePortNumber=_Dot1xPaePortNumber_Object((1,0,8802,1,1,1,1,1,2,1,1),_Dot1xPaePortNumber_Type())
dot1xPaePortNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dot1xPaePortNumber.setStatus(_B)
_Dot1xPaePortProtocolVersion_Type=Unsigned32
_Dot1xPaePortProtocolVersion_Object=MibTableColumn
dot1xPaePortProtocolVersion=_Dot1xPaePortProtocolVersion_Object((1,0,8802,1,1,1,1,1,2,1,2),_Dot1xPaePortProtocolVersion_Type())
dot1xPaePortProtocolVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xPaePortProtocolVersion.setStatus(_B)
class _Dot1xPaePortCapabilities_Type(Bits):namedValues=NamedValues(*(('dot1xPaePortAuthCapable',0),('dot1xPaePortSuppCapable',1)))
_Dot1xPaePortCapabilities_Type.__name__='Bits'
_Dot1xPaePortCapabilities_Object=MibTableColumn
dot1xPaePortCapabilities=_Dot1xPaePortCapabilities_Object((1,0,8802,1,1,1,1,1,2,1,3),_Dot1xPaePortCapabilities_Type())
dot1xPaePortCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xPaePortCapabilities.setStatus(_B)
_Dot1xPaePortInitialize_Type=TruthValue
_Dot1xPaePortInitialize_Object=MibTableColumn
dot1xPaePortInitialize=_Dot1xPaePortInitialize_Object((1,0,8802,1,1,1,1,1,2,1,4),_Dot1xPaePortInitialize_Type())
dot1xPaePortInitialize.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1xPaePortInitialize.setStatus(_B)
_Dot1xPaePortReauthenticate_Type=TruthValue
_Dot1xPaePortReauthenticate_Object=MibTableColumn
dot1xPaePortReauthenticate=_Dot1xPaePortReauthenticate_Object((1,0,8802,1,1,1,1,1,2,1,5),_Dot1xPaePortReauthenticate_Type())
dot1xPaePortReauthenticate.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1xPaePortReauthenticate.setStatus(_B)
_Dot1xPaeAuthenticator_ObjectIdentity=ObjectIdentity
dot1xPaeAuthenticator=_Dot1xPaeAuthenticator_ObjectIdentity((1,0,8802,1,1,1,1,2))
_Dot1xAuthConfigTable_Object=MibTable
dot1xAuthConfigTable=_Dot1xAuthConfigTable_Object((1,0,8802,1,1,1,1,2,1))
if mibBuilder.loadTexts:dot1xAuthConfigTable.setStatus(_B)
_Dot1xAuthConfigEntry_Object=MibTableRow
dot1xAuthConfigEntry=_Dot1xAuthConfigEntry_Object((1,0,8802,1,1,1,1,2,1,1))
dot1xAuthConfigEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:dot1xAuthConfigEntry.setStatus(_B)
class _Dot1xAuthPaeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_I,1),(_h,2),(_i,3),(_j,4),(_k,5),('aborting',6),('held',7),('forceAuth',8),('forceUnauth',9),(_l,10)))
_Dot1xAuthPaeState_Type.__name__=_G
_Dot1xAuthPaeState_Object=MibTableColumn
dot1xAuthPaeState=_Dot1xAuthPaeState_Object((1,0,8802,1,1,1,1,2,1,1,1),_Dot1xAuthPaeState_Type())
dot1xAuthPaeState.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthPaeState.setStatus(_B)
class _Dot1xAuthBackendAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_m,1),(_n,2),(_o,3),('fail',4),(_p,5),('idle',6),(_I,7),('ignore',8)))
_Dot1xAuthBackendAuthState_Type.__name__=_G
_Dot1xAuthBackendAuthState_Object=MibTableColumn
dot1xAuthBackendAuthState=_Dot1xAuthBackendAuthState_Object((1,0,8802,1,1,1,1,2,1,1,2),_Dot1xAuthBackendAuthState_Type())
dot1xAuthBackendAuthState.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthBackendAuthState.setStatus(_B)
_Dot1xAuthAdminControlledDirections_Type=PaeControlledDirections
_Dot1xAuthAdminControlledDirections_Object=MibTableColumn
dot1xAuthAdminControlledDirections=_Dot1xAuthAdminControlledDirections_Object((1,0,8802,1,1,1,1,2,1,1,3),_Dot1xAuthAdminControlledDirections_Type())
dot1xAuthAdminControlledDirections.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1xAuthAdminControlledDirections.setStatus(_B)
_Dot1xAuthOperControlledDirections_Type=PaeControlledDirections
_Dot1xAuthOperControlledDirections_Object=MibTableColumn
dot1xAuthOperControlledDirections=_Dot1xAuthOperControlledDirections_Object((1,0,8802,1,1,1,1,2,1,1,4),_Dot1xAuthOperControlledDirections_Type())
dot1xAuthOperControlledDirections.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthOperControlledDirections.setStatus(_B)
_Dot1xAuthAuthControlledPortStatus_Type=PaeControlledPortStatus
_Dot1xAuthAuthControlledPortStatus_Object=MibTableColumn
dot1xAuthAuthControlledPortStatus=_Dot1xAuthAuthControlledPortStatus_Object((1,0,8802,1,1,1,1,2,1,1,5),_Dot1xAuthAuthControlledPortStatus_Type())
dot1xAuthAuthControlledPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthAuthControlledPortStatus.setStatus(_B)
_Dot1xAuthAuthControlledPortControl_Type=PaeControlledPortControl
_Dot1xAuthAuthControlledPortControl_Object=MibTableColumn
dot1xAuthAuthControlledPortControl=_Dot1xAuthAuthControlledPortControl_Object((1,0,8802,1,1,1,1,2,1,1,6),_Dot1xAuthAuthControlledPortControl_Type())
dot1xAuthAuthControlledPortControl.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1xAuthAuthControlledPortControl.setStatus(_B)
class _Dot1xAuthQuietPeriod_Type(Unsigned32):defaultValue=60
_Dot1xAuthQuietPeriod_Type.__name__=_F
_Dot1xAuthQuietPeriod_Object=MibTableColumn
dot1xAuthQuietPeriod=_Dot1xAuthQuietPeriod_Object((1,0,8802,1,1,1,1,2,1,1,7),_Dot1xAuthQuietPeriod_Type())
dot1xAuthQuietPeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1xAuthQuietPeriod.setStatus(_B)
class _Dot1xAuthTxPeriod_Type(Unsigned32):defaultValue=30
_Dot1xAuthTxPeriod_Type.__name__=_F
_Dot1xAuthTxPeriod_Object=MibTableColumn
dot1xAuthTxPeriod=_Dot1xAuthTxPeriod_Object((1,0,8802,1,1,1,1,2,1,1,8),_Dot1xAuthTxPeriod_Type())
dot1xAuthTxPeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1xAuthTxPeriod.setStatus(_D)
class _Dot1xAuthSuppTimeout_Type(Unsigned32):defaultValue=30
_Dot1xAuthSuppTimeout_Type.__name__=_F
_Dot1xAuthSuppTimeout_Object=MibTableColumn
dot1xAuthSuppTimeout=_Dot1xAuthSuppTimeout_Object((1,0,8802,1,1,1,1,2,1,1,9),_Dot1xAuthSuppTimeout_Type())
dot1xAuthSuppTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1xAuthSuppTimeout.setStatus(_D)
class _Dot1xAuthServerTimeout_Type(Unsigned32):defaultValue=30
_Dot1xAuthServerTimeout_Type.__name__=_F
_Dot1xAuthServerTimeout_Object=MibTableColumn
dot1xAuthServerTimeout=_Dot1xAuthServerTimeout_Object((1,0,8802,1,1,1,1,2,1,1,10),_Dot1xAuthServerTimeout_Type())
dot1xAuthServerTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1xAuthServerTimeout.setStatus(_B)
class _Dot1xAuthMaxReq_Type(Unsigned32):defaultValue=2
_Dot1xAuthMaxReq_Type.__name__=_F
_Dot1xAuthMaxReq_Object=MibTableColumn
dot1xAuthMaxReq=_Dot1xAuthMaxReq_Object((1,0,8802,1,1,1,1,2,1,1,11),_Dot1xAuthMaxReq_Type())
dot1xAuthMaxReq.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1xAuthMaxReq.setStatus(_D)
class _Dot1xAuthReAuthPeriod_Type(Unsigned32):defaultValue=3600
_Dot1xAuthReAuthPeriod_Type.__name__=_F
_Dot1xAuthReAuthPeriod_Object=MibTableColumn
dot1xAuthReAuthPeriod=_Dot1xAuthReAuthPeriod_Object((1,0,8802,1,1,1,1,2,1,1,12),_Dot1xAuthReAuthPeriod_Type())
dot1xAuthReAuthPeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1xAuthReAuthPeriod.setStatus(_B)
class _Dot1xAuthReAuthEnabled_Type(TruthValue):defaultValue=2
_Dot1xAuthReAuthEnabled_Type.__name__=_g
_Dot1xAuthReAuthEnabled_Object=MibTableColumn
dot1xAuthReAuthEnabled=_Dot1xAuthReAuthEnabled_Object((1,0,8802,1,1,1,1,2,1,1,13),_Dot1xAuthReAuthEnabled_Type())
dot1xAuthReAuthEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1xAuthReAuthEnabled.setStatus(_B)
_Dot1xAuthKeyTxEnabled_Type=TruthValue
_Dot1xAuthKeyTxEnabled_Object=MibTableColumn
dot1xAuthKeyTxEnabled=_Dot1xAuthKeyTxEnabled_Object((1,0,8802,1,1,1,1,2,1,1,14),_Dot1xAuthKeyTxEnabled_Type())
dot1xAuthKeyTxEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1xAuthKeyTxEnabled.setStatus(_B)
_Dot1xAuthStatsTable_Object=MibTable
dot1xAuthStatsTable=_Dot1xAuthStatsTable_Object((1,0,8802,1,1,1,1,2,2))
if mibBuilder.loadTexts:dot1xAuthStatsTable.setStatus(_B)
_Dot1xAuthStatsEntry_Object=MibTableRow
dot1xAuthStatsEntry=_Dot1xAuthStatsEntry_Object((1,0,8802,1,1,1,1,2,2,1))
dot1xAuthStatsEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:dot1xAuthStatsEntry.setStatus(_B)
_Dot1xAuthEapolFramesRx_Type=Counter32
_Dot1xAuthEapolFramesRx_Object=MibTableColumn
dot1xAuthEapolFramesRx=_Dot1xAuthEapolFramesRx_Object((1,0,8802,1,1,1,1,2,2,1,1),_Dot1xAuthEapolFramesRx_Type())
dot1xAuthEapolFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthEapolFramesRx.setStatus(_B)
_Dot1xAuthEapolFramesTx_Type=Counter32
_Dot1xAuthEapolFramesTx_Object=MibTableColumn
dot1xAuthEapolFramesTx=_Dot1xAuthEapolFramesTx_Object((1,0,8802,1,1,1,1,2,2,1,2),_Dot1xAuthEapolFramesTx_Type())
dot1xAuthEapolFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthEapolFramesTx.setStatus(_B)
_Dot1xAuthEapolStartFramesRx_Type=Counter32
_Dot1xAuthEapolStartFramesRx_Object=MibTableColumn
dot1xAuthEapolStartFramesRx=_Dot1xAuthEapolStartFramesRx_Object((1,0,8802,1,1,1,1,2,2,1,3),_Dot1xAuthEapolStartFramesRx_Type())
dot1xAuthEapolStartFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthEapolStartFramesRx.setStatus(_B)
_Dot1xAuthEapolLogoffFramesRx_Type=Counter32
_Dot1xAuthEapolLogoffFramesRx_Object=MibTableColumn
dot1xAuthEapolLogoffFramesRx=_Dot1xAuthEapolLogoffFramesRx_Object((1,0,8802,1,1,1,1,2,2,1,4),_Dot1xAuthEapolLogoffFramesRx_Type())
dot1xAuthEapolLogoffFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthEapolLogoffFramesRx.setStatus(_B)
_Dot1xAuthEapolRespIdFramesRx_Type=Counter32
_Dot1xAuthEapolRespIdFramesRx_Object=MibTableColumn
dot1xAuthEapolRespIdFramesRx=_Dot1xAuthEapolRespIdFramesRx_Object((1,0,8802,1,1,1,1,2,2,1,5),_Dot1xAuthEapolRespIdFramesRx_Type())
dot1xAuthEapolRespIdFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthEapolRespIdFramesRx.setStatus(_B)
_Dot1xAuthEapolRespFramesRx_Type=Counter32
_Dot1xAuthEapolRespFramesRx_Object=MibTableColumn
dot1xAuthEapolRespFramesRx=_Dot1xAuthEapolRespFramesRx_Object((1,0,8802,1,1,1,1,2,2,1,6),_Dot1xAuthEapolRespFramesRx_Type())
dot1xAuthEapolRespFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthEapolRespFramesRx.setStatus(_B)
_Dot1xAuthEapolReqIdFramesTx_Type=Counter32
_Dot1xAuthEapolReqIdFramesTx_Object=MibTableColumn
dot1xAuthEapolReqIdFramesTx=_Dot1xAuthEapolReqIdFramesTx_Object((1,0,8802,1,1,1,1,2,2,1,7),_Dot1xAuthEapolReqIdFramesTx_Type())
dot1xAuthEapolReqIdFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthEapolReqIdFramesTx.setStatus(_B)
_Dot1xAuthEapolReqFramesTx_Type=Counter32
_Dot1xAuthEapolReqFramesTx_Object=MibTableColumn
dot1xAuthEapolReqFramesTx=_Dot1xAuthEapolReqFramesTx_Object((1,0,8802,1,1,1,1,2,2,1,8),_Dot1xAuthEapolReqFramesTx_Type())
dot1xAuthEapolReqFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthEapolReqFramesTx.setStatus(_B)
_Dot1xAuthInvalidEapolFramesRx_Type=Counter32
_Dot1xAuthInvalidEapolFramesRx_Object=MibTableColumn
dot1xAuthInvalidEapolFramesRx=_Dot1xAuthInvalidEapolFramesRx_Object((1,0,8802,1,1,1,1,2,2,1,9),_Dot1xAuthInvalidEapolFramesRx_Type())
dot1xAuthInvalidEapolFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthInvalidEapolFramesRx.setStatus(_B)
_Dot1xAuthEapLengthErrorFramesRx_Type=Counter32
_Dot1xAuthEapLengthErrorFramesRx_Object=MibTableColumn
dot1xAuthEapLengthErrorFramesRx=_Dot1xAuthEapLengthErrorFramesRx_Object((1,0,8802,1,1,1,1,2,2,1,10),_Dot1xAuthEapLengthErrorFramesRx_Type())
dot1xAuthEapLengthErrorFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthEapLengthErrorFramesRx.setStatus(_B)
_Dot1xAuthLastEapolFrameVersion_Type=Unsigned32
_Dot1xAuthLastEapolFrameVersion_Object=MibTableColumn
dot1xAuthLastEapolFrameVersion=_Dot1xAuthLastEapolFrameVersion_Object((1,0,8802,1,1,1,1,2,2,1,11),_Dot1xAuthLastEapolFrameVersion_Type())
dot1xAuthLastEapolFrameVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthLastEapolFrameVersion.setStatus(_B)
_Dot1xAuthLastEapolFrameSource_Type=MacAddress
_Dot1xAuthLastEapolFrameSource_Object=MibTableColumn
dot1xAuthLastEapolFrameSource=_Dot1xAuthLastEapolFrameSource_Object((1,0,8802,1,1,1,1,2,2,1,12),_Dot1xAuthLastEapolFrameSource_Type())
dot1xAuthLastEapolFrameSource.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthLastEapolFrameSource.setStatus(_B)
_Dot1xAuthDiagTable_Object=MibTable
dot1xAuthDiagTable=_Dot1xAuthDiagTable_Object((1,0,8802,1,1,1,1,2,3))
if mibBuilder.loadTexts:dot1xAuthDiagTable.setStatus(_D)
_Dot1xAuthDiagEntry_Object=MibTableRow
dot1xAuthDiagEntry=_Dot1xAuthDiagEntry_Object((1,0,8802,1,1,1,1,2,3,1))
dot1xAuthDiagEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:dot1xAuthDiagEntry.setStatus(_D)
_Dot1xAuthEntersConnecting_Type=Counter32
_Dot1xAuthEntersConnecting_Object=MibTableColumn
dot1xAuthEntersConnecting=_Dot1xAuthEntersConnecting_Object((1,0,8802,1,1,1,1,2,3,1,1),_Dot1xAuthEntersConnecting_Type())
dot1xAuthEntersConnecting.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthEntersConnecting.setStatus(_D)
_Dot1xAuthEapLogoffsWhileConnecting_Type=Counter32
_Dot1xAuthEapLogoffsWhileConnecting_Object=MibTableColumn
dot1xAuthEapLogoffsWhileConnecting=_Dot1xAuthEapLogoffsWhileConnecting_Object((1,0,8802,1,1,1,1,2,3,1,2),_Dot1xAuthEapLogoffsWhileConnecting_Type())
dot1xAuthEapLogoffsWhileConnecting.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthEapLogoffsWhileConnecting.setStatus(_D)
_Dot1xAuthEntersAuthenticating_Type=Counter32
_Dot1xAuthEntersAuthenticating_Object=MibTableColumn
dot1xAuthEntersAuthenticating=_Dot1xAuthEntersAuthenticating_Object((1,0,8802,1,1,1,1,2,3,1,3),_Dot1xAuthEntersAuthenticating_Type())
dot1xAuthEntersAuthenticating.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthEntersAuthenticating.setStatus(_D)
_Dot1xAuthAuthSuccessWhileAuthenticating_Type=Counter32
_Dot1xAuthAuthSuccessWhileAuthenticating_Object=MibTableColumn
dot1xAuthAuthSuccessWhileAuthenticating=_Dot1xAuthAuthSuccessWhileAuthenticating_Object((1,0,8802,1,1,1,1,2,3,1,4),_Dot1xAuthAuthSuccessWhileAuthenticating_Type())
dot1xAuthAuthSuccessWhileAuthenticating.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthAuthSuccessWhileAuthenticating.setStatus(_D)
_Dot1xAuthAuthTimeoutsWhileAuthenticating_Type=Counter32
_Dot1xAuthAuthTimeoutsWhileAuthenticating_Object=MibTableColumn
dot1xAuthAuthTimeoutsWhileAuthenticating=_Dot1xAuthAuthTimeoutsWhileAuthenticating_Object((1,0,8802,1,1,1,1,2,3,1,5),_Dot1xAuthAuthTimeoutsWhileAuthenticating_Type())
dot1xAuthAuthTimeoutsWhileAuthenticating.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthAuthTimeoutsWhileAuthenticating.setStatus(_D)
_Dot1xAuthAuthFailWhileAuthenticating_Type=Counter32
_Dot1xAuthAuthFailWhileAuthenticating_Object=MibTableColumn
dot1xAuthAuthFailWhileAuthenticating=_Dot1xAuthAuthFailWhileAuthenticating_Object((1,0,8802,1,1,1,1,2,3,1,6),_Dot1xAuthAuthFailWhileAuthenticating_Type())
dot1xAuthAuthFailWhileAuthenticating.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthAuthFailWhileAuthenticating.setStatus(_D)
_Dot1xAuthAuthReauthsWhileAuthenticating_Type=Counter32
_Dot1xAuthAuthReauthsWhileAuthenticating_Object=MibTableColumn
dot1xAuthAuthReauthsWhileAuthenticating=_Dot1xAuthAuthReauthsWhileAuthenticating_Object((1,0,8802,1,1,1,1,2,3,1,7),_Dot1xAuthAuthReauthsWhileAuthenticating_Type())
dot1xAuthAuthReauthsWhileAuthenticating.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthAuthReauthsWhileAuthenticating.setStatus(_D)
_Dot1xAuthAuthEapStartsWhileAuthenticating_Type=Counter32
_Dot1xAuthAuthEapStartsWhileAuthenticating_Object=MibTableColumn
dot1xAuthAuthEapStartsWhileAuthenticating=_Dot1xAuthAuthEapStartsWhileAuthenticating_Object((1,0,8802,1,1,1,1,2,3,1,8),_Dot1xAuthAuthEapStartsWhileAuthenticating_Type())
dot1xAuthAuthEapStartsWhileAuthenticating.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthAuthEapStartsWhileAuthenticating.setStatus(_D)
_Dot1xAuthAuthEapLogoffWhileAuthenticating_Type=Counter32
_Dot1xAuthAuthEapLogoffWhileAuthenticating_Object=MibTableColumn
dot1xAuthAuthEapLogoffWhileAuthenticating=_Dot1xAuthAuthEapLogoffWhileAuthenticating_Object((1,0,8802,1,1,1,1,2,3,1,9),_Dot1xAuthAuthEapLogoffWhileAuthenticating_Type())
dot1xAuthAuthEapLogoffWhileAuthenticating.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthAuthEapLogoffWhileAuthenticating.setStatus(_D)
_Dot1xAuthAuthReauthsWhileAuthenticated_Type=Counter32
_Dot1xAuthAuthReauthsWhileAuthenticated_Object=MibTableColumn
dot1xAuthAuthReauthsWhileAuthenticated=_Dot1xAuthAuthReauthsWhileAuthenticated_Object((1,0,8802,1,1,1,1,2,3,1,10),_Dot1xAuthAuthReauthsWhileAuthenticated_Type())
dot1xAuthAuthReauthsWhileAuthenticated.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthAuthReauthsWhileAuthenticated.setStatus(_D)
_Dot1xAuthAuthEapStartsWhileAuthenticated_Type=Counter32
_Dot1xAuthAuthEapStartsWhileAuthenticated_Object=MibTableColumn
dot1xAuthAuthEapStartsWhileAuthenticated=_Dot1xAuthAuthEapStartsWhileAuthenticated_Object((1,0,8802,1,1,1,1,2,3,1,11),_Dot1xAuthAuthEapStartsWhileAuthenticated_Type())
dot1xAuthAuthEapStartsWhileAuthenticated.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthAuthEapStartsWhileAuthenticated.setStatus(_D)
_Dot1xAuthAuthEapLogoffWhileAuthenticated_Type=Counter32
_Dot1xAuthAuthEapLogoffWhileAuthenticated_Object=MibTableColumn
dot1xAuthAuthEapLogoffWhileAuthenticated=_Dot1xAuthAuthEapLogoffWhileAuthenticated_Object((1,0,8802,1,1,1,1,2,3,1,12),_Dot1xAuthAuthEapLogoffWhileAuthenticated_Type())
dot1xAuthAuthEapLogoffWhileAuthenticated.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthAuthEapLogoffWhileAuthenticated.setStatus(_D)
_Dot1xAuthBackendResponses_Type=Counter32
_Dot1xAuthBackendResponses_Object=MibTableColumn
dot1xAuthBackendResponses=_Dot1xAuthBackendResponses_Object((1,0,8802,1,1,1,1,2,3,1,13),_Dot1xAuthBackendResponses_Type())
dot1xAuthBackendResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthBackendResponses.setStatus(_D)
_Dot1xAuthBackendAccessChallenges_Type=Counter32
_Dot1xAuthBackendAccessChallenges_Object=MibTableColumn
dot1xAuthBackendAccessChallenges=_Dot1xAuthBackendAccessChallenges_Object((1,0,8802,1,1,1,1,2,3,1,14),_Dot1xAuthBackendAccessChallenges_Type())
dot1xAuthBackendAccessChallenges.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthBackendAccessChallenges.setStatus(_D)
_Dot1xAuthBackendOtherRequestsToSupplicant_Type=Counter32
_Dot1xAuthBackendOtherRequestsToSupplicant_Object=MibTableColumn
dot1xAuthBackendOtherRequestsToSupplicant=_Dot1xAuthBackendOtherRequestsToSupplicant_Object((1,0,8802,1,1,1,1,2,3,1,15),_Dot1xAuthBackendOtherRequestsToSupplicant_Type())
dot1xAuthBackendOtherRequestsToSupplicant.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthBackendOtherRequestsToSupplicant.setStatus(_D)
_Dot1xAuthBackendNonNakResponsesFromSupplicant_Type=Counter32
_Dot1xAuthBackendNonNakResponsesFromSupplicant_Object=MibTableColumn
dot1xAuthBackendNonNakResponsesFromSupplicant=_Dot1xAuthBackendNonNakResponsesFromSupplicant_Object((1,0,8802,1,1,1,1,2,3,1,16),_Dot1xAuthBackendNonNakResponsesFromSupplicant_Type())
dot1xAuthBackendNonNakResponsesFromSupplicant.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthBackendNonNakResponsesFromSupplicant.setStatus(_D)
_Dot1xAuthBackendAuthSuccesses_Type=Counter32
_Dot1xAuthBackendAuthSuccesses_Object=MibTableColumn
dot1xAuthBackendAuthSuccesses=_Dot1xAuthBackendAuthSuccesses_Object((1,0,8802,1,1,1,1,2,3,1,17),_Dot1xAuthBackendAuthSuccesses_Type())
dot1xAuthBackendAuthSuccesses.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthBackendAuthSuccesses.setStatus(_D)
_Dot1xAuthBackendAuthFails_Type=Counter32
_Dot1xAuthBackendAuthFails_Object=MibTableColumn
dot1xAuthBackendAuthFails=_Dot1xAuthBackendAuthFails_Object((1,0,8802,1,1,1,1,2,3,1,18),_Dot1xAuthBackendAuthFails_Type())
dot1xAuthBackendAuthFails.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthBackendAuthFails.setStatus(_D)
_Dot1xAuthSessionStatsTable_Object=MibTable
dot1xAuthSessionStatsTable=_Dot1xAuthSessionStatsTable_Object((1,0,8802,1,1,1,1,2,4))
if mibBuilder.loadTexts:dot1xAuthSessionStatsTable.setStatus(_B)
_Dot1xAuthSessionStatsEntry_Object=MibTableRow
dot1xAuthSessionStatsEntry=_Dot1xAuthSessionStatsEntry_Object((1,0,8802,1,1,1,1,2,4,1))
dot1xAuthSessionStatsEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:dot1xAuthSessionStatsEntry.setStatus(_B)
_Dot1xAuthSessionOctetsRx_Type=Counter64
_Dot1xAuthSessionOctetsRx_Object=MibTableColumn
dot1xAuthSessionOctetsRx=_Dot1xAuthSessionOctetsRx_Object((1,0,8802,1,1,1,1,2,4,1,1),_Dot1xAuthSessionOctetsRx_Type())
dot1xAuthSessionOctetsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthSessionOctetsRx.setStatus(_B)
_Dot1xAuthSessionOctetsTx_Type=Counter64
_Dot1xAuthSessionOctetsTx_Object=MibTableColumn
dot1xAuthSessionOctetsTx=_Dot1xAuthSessionOctetsTx_Object((1,0,8802,1,1,1,1,2,4,1,2),_Dot1xAuthSessionOctetsTx_Type())
dot1xAuthSessionOctetsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthSessionOctetsTx.setStatus(_B)
_Dot1xAuthSessionFramesRx_Type=Counter32
_Dot1xAuthSessionFramesRx_Object=MibTableColumn
dot1xAuthSessionFramesRx=_Dot1xAuthSessionFramesRx_Object((1,0,8802,1,1,1,1,2,4,1,3),_Dot1xAuthSessionFramesRx_Type())
dot1xAuthSessionFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthSessionFramesRx.setStatus(_B)
_Dot1xAuthSessionFramesTx_Type=Counter32
_Dot1xAuthSessionFramesTx_Object=MibTableColumn
dot1xAuthSessionFramesTx=_Dot1xAuthSessionFramesTx_Object((1,0,8802,1,1,1,1,2,4,1,4),_Dot1xAuthSessionFramesTx_Type())
dot1xAuthSessionFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthSessionFramesTx.setStatus(_B)
_Dot1xAuthSessionId_Type=SnmpAdminString
_Dot1xAuthSessionId_Object=MibTableColumn
dot1xAuthSessionId=_Dot1xAuthSessionId_Object((1,0,8802,1,1,1,1,2,4,1,5),_Dot1xAuthSessionId_Type())
dot1xAuthSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthSessionId.setStatus(_B)
class _Dot1xAuthSessionAuthenticMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('remoteAuthServer',1),('localAuthServer',2)))
_Dot1xAuthSessionAuthenticMethod_Type.__name__=_G
_Dot1xAuthSessionAuthenticMethod_Object=MibTableColumn
dot1xAuthSessionAuthenticMethod=_Dot1xAuthSessionAuthenticMethod_Object((1,0,8802,1,1,1,1,2,4,1,6),_Dot1xAuthSessionAuthenticMethod_Type())
dot1xAuthSessionAuthenticMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthSessionAuthenticMethod.setStatus(_B)
_Dot1xAuthSessionTime_Type=TimeTicks
_Dot1xAuthSessionTime_Object=MibTableColumn
dot1xAuthSessionTime=_Dot1xAuthSessionTime_Object((1,0,8802,1,1,1,1,2,4,1,7),_Dot1xAuthSessionTime_Type())
dot1xAuthSessionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthSessionTime.setStatus(_B)
class _Dot1xAuthSessionTerminateCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,999)));namedValues=NamedValues(*(('supplicantLogoff',1),('portFailure',2),('supplicantRestart',3),('reauthFailed',4),('authControlForceUnauth',5),('portReInit',6),('portAdminDisabled',7),('notTerminatedYet',999)))
_Dot1xAuthSessionTerminateCause_Type.__name__=_G
_Dot1xAuthSessionTerminateCause_Object=MibTableColumn
dot1xAuthSessionTerminateCause=_Dot1xAuthSessionTerminateCause_Object((1,0,8802,1,1,1,1,2,4,1,8),_Dot1xAuthSessionTerminateCause_Type())
dot1xAuthSessionTerminateCause.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthSessionTerminateCause.setStatus(_B)
_Dot1xAuthSessionUserName_Type=SnmpAdminString
_Dot1xAuthSessionUserName_Object=MibTableColumn
dot1xAuthSessionUserName=_Dot1xAuthSessionUserName_Object((1,0,8802,1,1,1,1,2,4,1,9),_Dot1xAuthSessionUserName_Type())
dot1xAuthSessionUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xAuthSessionUserName.setStatus(_B)
_Dot1xPaeSupplicant_ObjectIdentity=ObjectIdentity
dot1xPaeSupplicant=_Dot1xPaeSupplicant_ObjectIdentity((1,0,8802,1,1,1,1,3))
_Dot1xSuppConfigTable_Object=MibTable
dot1xSuppConfigTable=_Dot1xSuppConfigTable_Object((1,0,8802,1,1,1,1,3,1))
if mibBuilder.loadTexts:dot1xSuppConfigTable.setStatus(_B)
_Dot1xSuppConfigEntry_Object=MibTableRow
dot1xSuppConfigEntry=_Dot1xSuppConfigEntry_Object((1,0,8802,1,1,1,1,3,1,1))
dot1xSuppConfigEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:dot1xSuppConfigEntry.setStatus(_B)
class _Dot1xSuppPaeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_h,1),('logoff',2),(_i,3),(_j,4),(_k,5),('acquired',6),('held',7),(_l,8),('sForceAuth',9),('sForceUnauth',10)))
_Dot1xSuppPaeState_Type.__name__=_G
_Dot1xSuppPaeState_Object=MibTableColumn
dot1xSuppPaeState=_Dot1xSuppPaeState_Object((1,0,8802,1,1,1,1,3,1,1,1),_Dot1xSuppPaeState_Type())
dot1xSuppPaeState.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xSuppPaeState.setStatus(_B)
class _Dot1xSuppHeldPeriod_Type(Unsigned32):defaultValue=60
_Dot1xSuppHeldPeriod_Type.__name__=_F
_Dot1xSuppHeldPeriod_Object=MibTableColumn
dot1xSuppHeldPeriod=_Dot1xSuppHeldPeriod_Object((1,0,8802,1,1,1,1,3,1,1,2),_Dot1xSuppHeldPeriod_Type())
dot1xSuppHeldPeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1xSuppHeldPeriod.setStatus(_B)
class _Dot1xSuppAuthPeriod_Type(Unsigned32):defaultValue=30
_Dot1xSuppAuthPeriod_Type.__name__=_F
_Dot1xSuppAuthPeriod_Object=MibTableColumn
dot1xSuppAuthPeriod=_Dot1xSuppAuthPeriod_Object((1,0,8802,1,1,1,1,3,1,1,3),_Dot1xSuppAuthPeriod_Type())
dot1xSuppAuthPeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1xSuppAuthPeriod.setStatus(_B)
class _Dot1xSuppStartPeriod_Type(Unsigned32):defaultValue=30
_Dot1xSuppStartPeriod_Type.__name__=_F
_Dot1xSuppStartPeriod_Object=MibTableColumn
dot1xSuppStartPeriod=_Dot1xSuppStartPeriod_Object((1,0,8802,1,1,1,1,3,1,1,4),_Dot1xSuppStartPeriod_Type())
dot1xSuppStartPeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1xSuppStartPeriod.setStatus(_B)
class _Dot1xSuppMaxStart_Type(Unsigned32):defaultValue=3
_Dot1xSuppMaxStart_Type.__name__=_F
_Dot1xSuppMaxStart_Object=MibTableColumn
dot1xSuppMaxStart=_Dot1xSuppMaxStart_Object((1,0,8802,1,1,1,1,3,1,1,5),_Dot1xSuppMaxStart_Type())
dot1xSuppMaxStart.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1xSuppMaxStart.setStatus(_B)
_Dot1xSuppControlledPortStatus_Type=PaeControlledPortStatus
_Dot1xSuppControlledPortStatus_Object=MibTableColumn
dot1xSuppControlledPortStatus=_Dot1xSuppControlledPortStatus_Object((1,0,8802,1,1,1,1,3,1,1,6),_Dot1xSuppControlledPortStatus_Type())
dot1xSuppControlledPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xSuppControlledPortStatus.setStatus(_B)
class _Dot1xSuppAccessCtrlWithAuth_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inactive',1),('active',2)))
_Dot1xSuppAccessCtrlWithAuth_Type.__name__=_G
_Dot1xSuppAccessCtrlWithAuth_Object=MibTableColumn
dot1xSuppAccessCtrlWithAuth=_Dot1xSuppAccessCtrlWithAuth_Object((1,0,8802,1,1,1,1,3,1,1,7),_Dot1xSuppAccessCtrlWithAuth_Type())
dot1xSuppAccessCtrlWithAuth.setMaxAccess(_E)
if mibBuilder.loadTexts:dot1xSuppAccessCtrlWithAuth.setStatus(_B)
class _Dot1xSuppBackendState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_I,1),('idle',2),(_m,3),(_n,4),('receive',5),('fail',6),(_o,7),(_p,8)))
_Dot1xSuppBackendState_Type.__name__=_G
_Dot1xSuppBackendState_Object=MibTableColumn
dot1xSuppBackendState=_Dot1xSuppBackendState_Object((1,0,8802,1,1,1,1,3,1,1,8),_Dot1xSuppBackendState_Type())
dot1xSuppBackendState.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xSuppBackendState.setStatus(_B)
_Dot1xSuppStatsTable_Object=MibTable
dot1xSuppStatsTable=_Dot1xSuppStatsTable_Object((1,0,8802,1,1,1,1,3,2))
if mibBuilder.loadTexts:dot1xSuppStatsTable.setStatus(_B)
_Dot1xSuppStatsEntry_Object=MibTableRow
dot1xSuppStatsEntry=_Dot1xSuppStatsEntry_Object((1,0,8802,1,1,1,1,3,2,1))
dot1xSuppStatsEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:dot1xSuppStatsEntry.setStatus(_B)
_Dot1xSuppEapolFramesRx_Type=Counter32
_Dot1xSuppEapolFramesRx_Object=MibTableColumn
dot1xSuppEapolFramesRx=_Dot1xSuppEapolFramesRx_Object((1,0,8802,1,1,1,1,3,2,1,1),_Dot1xSuppEapolFramesRx_Type())
dot1xSuppEapolFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xSuppEapolFramesRx.setStatus(_B)
_Dot1xSuppEapolFramesTx_Type=Counter32
_Dot1xSuppEapolFramesTx_Object=MibTableColumn
dot1xSuppEapolFramesTx=_Dot1xSuppEapolFramesTx_Object((1,0,8802,1,1,1,1,3,2,1,2),_Dot1xSuppEapolFramesTx_Type())
dot1xSuppEapolFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xSuppEapolFramesTx.setStatus(_B)
_Dot1xSuppEapolStartFramesTx_Type=Counter32
_Dot1xSuppEapolStartFramesTx_Object=MibTableColumn
dot1xSuppEapolStartFramesTx=_Dot1xSuppEapolStartFramesTx_Object((1,0,8802,1,1,1,1,3,2,1,3),_Dot1xSuppEapolStartFramesTx_Type())
dot1xSuppEapolStartFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xSuppEapolStartFramesTx.setStatus(_B)
_Dot1xSuppEapolLogoffFramesTx_Type=Counter32
_Dot1xSuppEapolLogoffFramesTx_Object=MibTableColumn
dot1xSuppEapolLogoffFramesTx=_Dot1xSuppEapolLogoffFramesTx_Object((1,0,8802,1,1,1,1,3,2,1,4),_Dot1xSuppEapolLogoffFramesTx_Type())
dot1xSuppEapolLogoffFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xSuppEapolLogoffFramesTx.setStatus(_B)
_Dot1xSuppEapolRespIdFramesTx_Type=Counter32
_Dot1xSuppEapolRespIdFramesTx_Object=MibTableColumn
dot1xSuppEapolRespIdFramesTx=_Dot1xSuppEapolRespIdFramesTx_Object((1,0,8802,1,1,1,1,3,2,1,5),_Dot1xSuppEapolRespIdFramesTx_Type())
dot1xSuppEapolRespIdFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xSuppEapolRespIdFramesTx.setStatus(_D)
_Dot1xSuppEapolRespFramesTx_Type=Counter32
_Dot1xSuppEapolRespFramesTx_Object=MibTableColumn
dot1xSuppEapolRespFramesTx=_Dot1xSuppEapolRespFramesTx_Object((1,0,8802,1,1,1,1,3,2,1,6),_Dot1xSuppEapolRespFramesTx_Type())
dot1xSuppEapolRespFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xSuppEapolRespFramesTx.setStatus(_D)
_Dot1xSuppEapolReqIdFramesRx_Type=Counter32
_Dot1xSuppEapolReqIdFramesRx_Object=MibTableColumn
dot1xSuppEapolReqIdFramesRx=_Dot1xSuppEapolReqIdFramesRx_Object((1,0,8802,1,1,1,1,3,2,1,7),_Dot1xSuppEapolReqIdFramesRx_Type())
dot1xSuppEapolReqIdFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xSuppEapolReqIdFramesRx.setStatus(_D)
_Dot1xSuppEapolReqFramesRx_Type=Counter32
_Dot1xSuppEapolReqFramesRx_Object=MibTableColumn
dot1xSuppEapolReqFramesRx=_Dot1xSuppEapolReqFramesRx_Object((1,0,8802,1,1,1,1,3,2,1,8),_Dot1xSuppEapolReqFramesRx_Type())
dot1xSuppEapolReqFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xSuppEapolReqFramesRx.setStatus(_D)
_Dot1xSuppInvalidEapolFramesRx_Type=Counter32
_Dot1xSuppInvalidEapolFramesRx_Object=MibTableColumn
dot1xSuppInvalidEapolFramesRx=_Dot1xSuppInvalidEapolFramesRx_Object((1,0,8802,1,1,1,1,3,2,1,9),_Dot1xSuppInvalidEapolFramesRx_Type())
dot1xSuppInvalidEapolFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xSuppInvalidEapolFramesRx.setStatus(_B)
_Dot1xSuppEapLengthErrorFramesRx_Type=Counter32
_Dot1xSuppEapLengthErrorFramesRx_Object=MibTableColumn
dot1xSuppEapLengthErrorFramesRx=_Dot1xSuppEapLengthErrorFramesRx_Object((1,0,8802,1,1,1,1,3,2,1,10),_Dot1xSuppEapLengthErrorFramesRx_Type())
dot1xSuppEapLengthErrorFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xSuppEapLengthErrorFramesRx.setStatus(_B)
_Dot1xSuppLastEapolFrameVersion_Type=Unsigned32
_Dot1xSuppLastEapolFrameVersion_Object=MibTableColumn
dot1xSuppLastEapolFrameVersion=_Dot1xSuppLastEapolFrameVersion_Object((1,0,8802,1,1,1,1,3,2,1,11),_Dot1xSuppLastEapolFrameVersion_Type())
dot1xSuppLastEapolFrameVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xSuppLastEapolFrameVersion.setStatus(_B)
_Dot1xSuppLastEapolFrameSource_Type=MacAddress
_Dot1xSuppLastEapolFrameSource_Object=MibTableColumn
dot1xSuppLastEapolFrameSource=_Dot1xSuppLastEapolFrameSource_Object((1,0,8802,1,1,1,1,3,2,1,12),_Dot1xSuppLastEapolFrameSource_Type())
dot1xSuppLastEapolFrameSource.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1xSuppLastEapolFrameSource.setStatus(_B)
_Dot1xPaeConformance_ObjectIdentity=ObjectIdentity
dot1xPaeConformance=_Dot1xPaeConformance_ObjectIdentity((1,0,8802,1,1,1,2))
_Dot1xPaeGroups_ObjectIdentity=ObjectIdentity
dot1xPaeGroups=_Dot1xPaeGroups_ObjectIdentity((1,0,8802,1,1,1,2,1))
_Dot1xPaeCompliances_ObjectIdentity=ObjectIdentity
dot1xPaeCompliances=_Dot1xPaeCompliances_ObjectIdentity((1,0,8802,1,1,1,2,2))
dot1xPaeSystemGroup=ObjectGroup((1,0,8802,1,1,1,2,1,1))
dot1xPaeSystemGroup.setObjects(*((_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:dot1xPaeSystemGroup.setStatus(_B)
dot1xPaeAuthConfigGroup=ObjectGroup((1,0,8802,1,1,1,2,1,2))
dot1xPaeAuthConfigGroup.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_v),(_A,_w),(_A,_Q),(_A,_x),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:dot1xPaeAuthConfigGroup.setStatus(_D)
dot1xPaeAuthStatsGroup=ObjectGroup((1,0,8802,1,1,1,2,1,3))
dot1xPaeAuthStatsGroup.setObjects(*((_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:dot1xPaeAuthStatsGroup.setStatus(_B)
dot1xPaeAuthDiagGroup=ObjectGroup((1,0,8802,1,1,1,2,1,4))
dot1xPaeAuthDiagGroup.setObjects(*((_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR)))
if mibBuilder.loadTexts:dot1xPaeAuthDiagGroup.setStatus(_D)
dot1xPaeAuthSessionStatsGroup=ObjectGroup((1,0,8802,1,1,1,2,1,5))
dot1xPaeAuthSessionStatsGroup.setObjects(*((_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:dot1xPaeAuthSessionStatsGroup.setStatus(_B)
dot1xPaeSuppConfigGroup=ObjectGroup((1,0,8802,1,1,1,2,1,6))
dot1xPaeSuppConfigGroup.setObjects(*((_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af)))
if mibBuilder.loadTexts:dot1xPaeSuppConfigGroup.setStatus(_B)
dot1xPaeSuppStatsGroup=ObjectGroup((1,0,8802,1,1,1,2,1,7))
dot1xPaeSuppStatsGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:dot1xPaeSuppStatsGroup.setStatus(_D)
dot1xPaeAuthConfigGroup2=ObjectGroup((1,0,8802,1,1,1,2,1,8))
dot1xPaeAuthConfigGroup2.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:dot1xPaeAuthConfigGroup2.setStatus(_B)
dot1xPaeSuppConfigGroup2=ObjectGroup((1,0,8802,1,1,1,2,1,9))
dot1xPaeSuppConfigGroup2.setObjects(*((_A,_Ak),(_A,_Al),(_A,_Am)))
if mibBuilder.loadTexts:dot1xPaeSuppConfigGroup2.setStatus(_B)
dot1xPaeSuppStatsGroup2=ObjectGroup((1,0,8802,1,1,1,2,1,10))
dot1xPaeSuppStatsGroup2.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:dot1xPaeSuppStatsGroup2.setStatus(_B)
dot1xPaeCompliance=ModuleCompliance((1,0,8802,1,1,1,2,2,1))
dot1xPaeCompliance.setObjects(*((_A,_c),(_A,_An),(_A,_d),(_A,_Ao),(_A,_e),(_A,_f),(_A,_Ap)))
if mibBuilder.loadTexts:dot1xPaeCompliance.setStatus(_D)
dot1xPaeCompliance2=ModuleCompliance((1,0,8802,1,1,1,2,2,2))
dot1xPaeCompliance2.setObjects(*((_A,_c),(_A,_Aq),(_A,_d),(_A,_e),(_A,_f),(_A,_Ar),(_A,_As)))
if mibBuilder.loadTexts:dot1xPaeCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'PaeControlledDirections':PaeControlledDirections,'PaeControlledPortStatus':PaeControlledPortStatus,'PaeControlledPortControl':PaeControlledPortControl,'ieee8021paeMIB':ieee8021paeMIB,'paeMIBObjects':paeMIBObjects,'dot1xPaeSystem':dot1xPaeSystem,_q:dot1xPaeSystemAuthControl,'dot1xPaePortTable':dot1xPaePortTable,'dot1xPaePortEntry':dot1xPaePortEntry,_H:dot1xPaePortNumber,_r:dot1xPaePortProtocolVersion,_s:dot1xPaePortCapabilities,_t:dot1xPaePortInitialize,_u:dot1xPaePortReauthenticate,'dot1xPaeAuthenticator':dot1xPaeAuthenticator,'dot1xAuthConfigTable':dot1xAuthConfigTable,'dot1xAuthConfigEntry':dot1xAuthConfigEntry,_J:dot1xAuthPaeState,_K:dot1xAuthBackendAuthState,_L:dot1xAuthAdminControlledDirections,_M:dot1xAuthOperControlledDirections,_N:dot1xAuthAuthControlledPortStatus,_O:dot1xAuthAuthControlledPortControl,_P:dot1xAuthQuietPeriod,_v:dot1xAuthTxPeriod,_w:dot1xAuthSuppTimeout,_Q:dot1xAuthServerTimeout,_x:dot1xAuthMaxReq,_R:dot1xAuthReAuthPeriod,_S:dot1xAuthReAuthEnabled,_T:dot1xAuthKeyTxEnabled,'dot1xAuthStatsTable':dot1xAuthStatsTable,'dot1xAuthStatsEntry':dot1xAuthStatsEntry,_y:dot1xAuthEapolFramesRx,_z:dot1xAuthEapolFramesTx,_A0:dot1xAuthEapolStartFramesRx,_A1:dot1xAuthEapolLogoffFramesRx,_A2:dot1xAuthEapolRespIdFramesRx,_A3:dot1xAuthEapolRespFramesRx,_A4:dot1xAuthEapolReqIdFramesTx,_A5:dot1xAuthEapolReqFramesTx,_A6:dot1xAuthInvalidEapolFramesRx,_A7:dot1xAuthEapLengthErrorFramesRx,_A8:dot1xAuthLastEapolFrameVersion,_A9:dot1xAuthLastEapolFrameSource,'dot1xAuthDiagTable':dot1xAuthDiagTable,'dot1xAuthDiagEntry':dot1xAuthDiagEntry,_AA:dot1xAuthEntersConnecting,_AB:dot1xAuthEapLogoffsWhileConnecting,_AC:dot1xAuthEntersAuthenticating,_AD:dot1xAuthAuthSuccessWhileAuthenticating,_AE:dot1xAuthAuthTimeoutsWhileAuthenticating,_AF:dot1xAuthAuthFailWhileAuthenticating,_AG:dot1xAuthAuthReauthsWhileAuthenticating,_AH:dot1xAuthAuthEapStartsWhileAuthenticating,_AI:dot1xAuthAuthEapLogoffWhileAuthenticating,_AJ:dot1xAuthAuthReauthsWhileAuthenticated,_AK:dot1xAuthAuthEapStartsWhileAuthenticated,_AL:dot1xAuthAuthEapLogoffWhileAuthenticated,_AM:dot1xAuthBackendResponses,_AN:dot1xAuthBackendAccessChallenges,_AO:dot1xAuthBackendOtherRequestsToSupplicant,_AP:dot1xAuthBackendNonNakResponsesFromSupplicant,_AQ:dot1xAuthBackendAuthSuccesses,_AR:dot1xAuthBackendAuthFails,'dot1xAuthSessionStatsTable':dot1xAuthSessionStatsTable,'dot1xAuthSessionStatsEntry':dot1xAuthSessionStatsEntry,_AS:dot1xAuthSessionOctetsRx,_AT:dot1xAuthSessionOctetsTx,_AU:dot1xAuthSessionFramesRx,_AV:dot1xAuthSessionFramesTx,_AW:dot1xAuthSessionId,_AX:dot1xAuthSessionAuthenticMethod,_AY:dot1xAuthSessionTime,_AZ:dot1xAuthSessionTerminateCause,_Aa:dot1xAuthSessionUserName,'dot1xPaeSupplicant':dot1xPaeSupplicant,'dot1xSuppConfigTable':dot1xSuppConfigTable,'dot1xSuppConfigEntry':dot1xSuppConfigEntry,_Ab:dot1xSuppPaeState,_Ac:dot1xSuppHeldPeriod,_Ad:dot1xSuppAuthPeriod,_Ae:dot1xSuppStartPeriod,_Af:dot1xSuppMaxStart,_Ak:dot1xSuppControlledPortStatus,_Al:dot1xSuppAccessCtrlWithAuth,_Am:dot1xSuppBackendState,'dot1xSuppStatsTable':dot1xSuppStatsTable,'dot1xSuppStatsEntry':dot1xSuppStatsEntry,_U:dot1xSuppEapolFramesRx,_V:dot1xSuppEapolFramesTx,_W:dot1xSuppEapolStartFramesTx,_X:dot1xSuppEapolLogoffFramesTx,_Ag:dot1xSuppEapolRespIdFramesTx,_Ah:dot1xSuppEapolRespFramesTx,_Ai:dot1xSuppEapolReqIdFramesRx,_Aj:dot1xSuppEapolReqFramesRx,_Y:dot1xSuppInvalidEapolFramesRx,_Z:dot1xSuppEapLengthErrorFramesRx,_a:dot1xSuppLastEapolFrameVersion,_b:dot1xSuppLastEapolFrameSource,'dot1xPaeConformance':dot1xPaeConformance,'dot1xPaeGroups':dot1xPaeGroups,_c:dot1xPaeSystemGroup,_An:dot1xPaeAuthConfigGroup,_d:dot1xPaeAuthStatsGroup,_Ao:dot1xPaeAuthDiagGroup,_e:dot1xPaeAuthSessionStatsGroup,_f:dot1xPaeSuppConfigGroup,_Ap:dot1xPaeSuppStatsGroup,_Aq:dot1xPaeAuthConfigGroup2,_As:dot1xPaeSuppConfigGroup2,_Ar:dot1xPaeSuppStatsGroup2,'dot1xPaeCompliances':dot1xPaeCompliances,'dot1xPaeCompliance':dot1xPaeCompliance,'dot1xPaeCompliance2':dot1xPaeCompliance2})