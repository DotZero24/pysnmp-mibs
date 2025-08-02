_AR='etsysMultiUser8021xSystemGroup'
_AQ='etsysMulti1xSystemAccountEnable'
_AP='etsysMulti1xActiveSupplicantAddress'
_AO='etsysMulti1xUserAddress'
_AN='etsysMulti1xUserActive'
_AM='etsysMulti1xUserName'
_AL='etsysMulti1xSupplicantUserName'
_AK='etsysMulti1xSupplicantActive'
_AJ='etsysMulti1xSessionActive'
_AI='etsysMulti1xSessionUserName'
_AH='etsysMulti1xSessionTerminateCause'
_AG='etsysMulti1xSessionTime'
_AF='etsysMulti1xSessionAuthenticMethod'
_AE='etsysMulti1xSessionId'
_AD='etsysMulti1xSessionFramesTx'
_AC='etsysMulti1xSessionFramesRx'
_AB='etsysMulti1xSessionOctetsTx'
_AA='etsysMulti1xSessionOctetsRx'
_A9='etsysMulti1xAeBackendAuthFails'
_A8='etsysMulti1xAeBackendAuthSuccesses'
_A7='etsysMulti1xAeBackendNonNakResponsesFromSupplicant'
_A6='etsysMulti1xAeBackendOtherRequestsToSupplicant'
_A5='etsysMulti1xAeBackendAccessChallenges'
_A4='etsysMulti1xAeBackendResponses'
_A3='etsysMulti1xAeAuthEapLogoffWhileAuthenticated'
_A2='etsysMulti1xAeAuthEapStartsWhileAuthenticated'
_A1='etsysMulti1xAeAuthReauthsWhileAuthenticated'
_A0='etsysMulti1xAeAuthEapLogoffWhileAuthenticating'
_z='etsysMulti1xAeAuthEapStartsWhileAuthenticating'
_y='etsysMulti1xAeAuthReauthsWhileAuthenticating'
_x='etsysMulti1xAeAuthFailWhileAuthenticating'
_w='etsysMulti1xAeAuthTimeoutsWhileAuthenticating'
_v='etsysMulti1xAeAuthSuccessWhileAuthenticating'
_u='etsysMulti1xAeEntersAuthenticating'
_t='etsysMulti1xAeEapLogoffsWhileConnecting'
_s='etsysMulti1xAeEntersConnecting'
_r='etsysMulti1xAeEapolFrameSource'
_q='etsysMulti1xAeEapolFrameVersion'
_p='etsysMulti1xAeEapLengthErrorFramesRx'
_o='etsysMulti1xAeInvalidEapolFramesRx'
_n='etsysMulti1xAeEapolReqFramesTx'
_m='etsysMulti1xAeEapolReqIdFramesTx'
_l='etsysMulti1xAeEapolRespFramesRx'
_k='etsysMulti1xAeEapolRespIdFramesRx'
_j='etsysMulti1xAeEapolLogoffFramesRx'
_i='etsysMulti1xAeEapolStartFramesRx'
_h='etsysMulti1xAeEapolFramesTx'
_g='etsysMulti1xAeEapolFramesRx'
_f='etsysMulti1xAeUserName'
_e='etsysMulti1xAeReAuthPeriod'
_d='etsysMulti1xAeReauthenticate'
_c='etsysMulti1xAeInitialize'
_b='etsysMulti1xAeBackendAuthState'
_a='etsysMulti1xAeState'
_Z='etsysMulti1xAeActive'
_Y='etsysMulti1xSessionStatsEntry'
_X='etsysMulti1xAeDiagEntry'
_W='etsysMulti1xAccessEntityStatsEntry'
_V='etsysMulti1xUserNameIndex'
_U='initialize'
_T='not-accessible'
_S='Unsigned32'
_R='SnmpAdminString'
_Q='EnabledStatus'
_P='etsysMultiUser8021xActiveAccessEntityGroup'
_O='etsysMultiUser8021xUserNameGroup'
_N='etsysMultiUser8021xSupplicantAddressGroup'
_M='etsysMultiUser8021xAccessEntitySessionGroup'
_L='etsysMultiUser8021xAccessEntityDiagGroup'
_K='etsysMultiUser8021xAccessEntityStatsGroup'
_J='etsysMultiUser8021xAccessEntityGroup'
_I='etsysMulti1xAeSupplicantAddress'
_H='read-write'
_G='etsysMulti1xAeIndex'
_F='Integer32'
_E='dot1xPaePortNumber'
_D='IEEE8021-PAE-MIB'
_C='read-only'
_B='ENTERASYS-MULTI-USER-8021X-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
dot1xPaePortNumber,=mibBuilder.importSymbols(_D,_E)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_Q)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_R)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_S,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
etsysMultiUser8021xMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,53))
if mibBuilder.loadTexts:etsysMultiUser8021xMIB.setRevisions(('2013-02-12 16:56','2004-11-11 15:31'))
_EtsysMultiUser8021xObjects_ObjectIdentity=ObjectIdentity
etsysMultiUser8021xObjects=_EtsysMultiUser8021xObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,53,1))
_EtsysMultiUser8021xSystem_ObjectIdentity=ObjectIdentity
etsysMultiUser8021xSystem=_EtsysMultiUser8021xSystem_ObjectIdentity((1,3,6,1,4,1,5624,1,2,53,1,1))
class _EtsysMulti1xSystemAccountEnable_Type(EnabledStatus):defaultValue=1
_EtsysMulti1xSystemAccountEnable_Type.__name__=_Q
_EtsysMulti1xSystemAccountEnable_Object=MibScalar
etsysMulti1xSystemAccountEnable=_EtsysMulti1xSystemAccountEnable_Object((1,3,6,1,4,1,5624,1,2,53,1,1,1),_EtsysMulti1xSystemAccountEnable_Type())
etsysMulti1xSystemAccountEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysMulti1xSystemAccountEnable.setStatus(_A)
_EtsysMultiUser8021xAccessEntity_ObjectIdentity=ObjectIdentity
etsysMultiUser8021xAccessEntity=_EtsysMultiUser8021xAccessEntity_ObjectIdentity((1,3,6,1,4,1,5624,1,2,53,1,2))
_EtsysMulti1xAccessEntityTable_Object=MibTable
etsysMulti1xAccessEntityTable=_EtsysMulti1xAccessEntityTable_Object((1,3,6,1,4,1,5624,1,2,53,1,2,1))
if mibBuilder.loadTexts:etsysMulti1xAccessEntityTable.setStatus(_A)
_EtsysMulti1xAccessEntityEntry_Object=MibTableRow
etsysMulti1xAccessEntityEntry=_EtsysMulti1xAccessEntityEntry_Object((1,3,6,1,4,1,5624,1,2,53,1,2,1,1))
etsysMulti1xAccessEntityEntry.setIndexNames((0,_D,_E),(0,_B,_G))
if mibBuilder.loadTexts:etsysMulti1xAccessEntityEntry.setStatus(_A)
_EtsysMulti1xAeIndex_Type=Unsigned32
_EtsysMulti1xAeIndex_Object=MibTableColumn
etsysMulti1xAeIndex=_EtsysMulti1xAeIndex_Object((1,3,6,1,4,1,5624,1,2,53,1,2,1,1,1),_EtsysMulti1xAeIndex_Type())
etsysMulti1xAeIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:etsysMulti1xAeIndex.setStatus(_A)
_EtsysMulti1xAeActive_Type=TruthValue
_EtsysMulti1xAeActive_Object=MibTableColumn
etsysMulti1xAeActive=_EtsysMulti1xAeActive_Object((1,3,6,1,4,1,5624,1,2,53,1,2,1,1,2),_EtsysMulti1xAeActive_Type())
etsysMulti1xAeActive.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeActive.setStatus(_A)
class _EtsysMulti1xAeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_U,1),('disconnected',2),('connecting',3),('authenticating',4),('authenticated',5),('aborting',6),('held',7),('forceAuth',8),('forceUnauth',9)))
_EtsysMulti1xAeState_Type.__name__=_F
_EtsysMulti1xAeState_Object=MibTableColumn
etsysMulti1xAeState=_EtsysMulti1xAeState_Object((1,3,6,1,4,1,5624,1,2,53,1,2,1,1,3),_EtsysMulti1xAeState_Type())
etsysMulti1xAeState.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeState.setStatus(_A)
class _EtsysMulti1xAeBackendAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('request',1),('response',2),('success',3),('fail',4),('timeout',5),('idle',6),(_U,7)))
_EtsysMulti1xAeBackendAuthState_Type.__name__=_F
_EtsysMulti1xAeBackendAuthState_Object=MibTableColumn
etsysMulti1xAeBackendAuthState=_EtsysMulti1xAeBackendAuthState_Object((1,3,6,1,4,1,5624,1,2,53,1,2,1,1,4),_EtsysMulti1xAeBackendAuthState_Type())
etsysMulti1xAeBackendAuthState.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeBackendAuthState.setStatus(_A)
_EtsysMulti1xAeInitialize_Type=TruthValue
_EtsysMulti1xAeInitialize_Object=MibTableColumn
etsysMulti1xAeInitialize=_EtsysMulti1xAeInitialize_Object((1,3,6,1,4,1,5624,1,2,53,1,2,1,1,5),_EtsysMulti1xAeInitialize_Type())
etsysMulti1xAeInitialize.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysMulti1xAeInitialize.setStatus(_A)
_EtsysMulti1xAeReauthenticate_Type=TruthValue
_EtsysMulti1xAeReauthenticate_Object=MibTableColumn
etsysMulti1xAeReauthenticate=_EtsysMulti1xAeReauthenticate_Object((1,3,6,1,4,1,5624,1,2,53,1,2,1,1,6),_EtsysMulti1xAeReauthenticate_Type())
etsysMulti1xAeReauthenticate.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysMulti1xAeReauthenticate.setStatus(_A)
class _EtsysMulti1xAeReAuthPeriod_Type(Unsigned32):defaultValue=3600
_EtsysMulti1xAeReAuthPeriod_Type.__name__=_S
_EtsysMulti1xAeReAuthPeriod_Object=MibTableColumn
etsysMulti1xAeReAuthPeriod=_EtsysMulti1xAeReAuthPeriod_Object((1,3,6,1,4,1,5624,1,2,53,1,2,1,1,7),_EtsysMulti1xAeReAuthPeriod_Type())
etsysMulti1xAeReAuthPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeReAuthPeriod.setStatus(_A)
if mibBuilder.loadTexts:etsysMulti1xAeReAuthPeriod.setUnits('seconds')
_EtsysMulti1xAeSupplicantAddress_Type=MacAddress
_EtsysMulti1xAeSupplicantAddress_Object=MibTableColumn
etsysMulti1xAeSupplicantAddress=_EtsysMulti1xAeSupplicantAddress_Object((1,3,6,1,4,1,5624,1,2,53,1,2,1,1,8),_EtsysMulti1xAeSupplicantAddress_Type())
etsysMulti1xAeSupplicantAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeSupplicantAddress.setStatus(_A)
_EtsysMulti1xAeUserName_Type=SnmpAdminString
_EtsysMulti1xAeUserName_Object=MibTableColumn
etsysMulti1xAeUserName=_EtsysMulti1xAeUserName_Object((1,3,6,1,4,1,5624,1,2,53,1,2,1,1,9),_EtsysMulti1xAeUserName_Type())
etsysMulti1xAeUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeUserName.setStatus(_A)
_EtsysMulti1xAccessEntityStatsTable_Object=MibTable
etsysMulti1xAccessEntityStatsTable=_EtsysMulti1xAccessEntityStatsTable_Object((1,3,6,1,4,1,5624,1,2,53,1,2,2))
if mibBuilder.loadTexts:etsysMulti1xAccessEntityStatsTable.setStatus(_A)
_EtsysMulti1xAccessEntityStatsEntry_Object=MibTableRow
etsysMulti1xAccessEntityStatsEntry=_EtsysMulti1xAccessEntityStatsEntry_Object((1,3,6,1,4,1,5624,1,2,53,1,2,2,1))
if mibBuilder.loadTexts:etsysMulti1xAccessEntityStatsEntry.setStatus(_A)
_EtsysMulti1xAeEapolFramesRx_Type=Counter32
_EtsysMulti1xAeEapolFramesRx_Object=MibTableColumn
etsysMulti1xAeEapolFramesRx=_EtsysMulti1xAeEapolFramesRx_Object((1,3,6,1,4,1,5624,1,2,53,1,2,2,1,1),_EtsysMulti1xAeEapolFramesRx_Type())
etsysMulti1xAeEapolFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeEapolFramesRx.setStatus(_A)
_EtsysMulti1xAeEapolFramesTx_Type=Counter32
_EtsysMulti1xAeEapolFramesTx_Object=MibTableColumn
etsysMulti1xAeEapolFramesTx=_EtsysMulti1xAeEapolFramesTx_Object((1,3,6,1,4,1,5624,1,2,53,1,2,2,1,2),_EtsysMulti1xAeEapolFramesTx_Type())
etsysMulti1xAeEapolFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeEapolFramesTx.setStatus(_A)
_EtsysMulti1xAeEapolStartFramesRx_Type=Counter32
_EtsysMulti1xAeEapolStartFramesRx_Object=MibTableColumn
etsysMulti1xAeEapolStartFramesRx=_EtsysMulti1xAeEapolStartFramesRx_Object((1,3,6,1,4,1,5624,1,2,53,1,2,2,1,3),_EtsysMulti1xAeEapolStartFramesRx_Type())
etsysMulti1xAeEapolStartFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeEapolStartFramesRx.setStatus(_A)
_EtsysMulti1xAeEapolLogoffFramesRx_Type=Counter32
_EtsysMulti1xAeEapolLogoffFramesRx_Object=MibTableColumn
etsysMulti1xAeEapolLogoffFramesRx=_EtsysMulti1xAeEapolLogoffFramesRx_Object((1,3,6,1,4,1,5624,1,2,53,1,2,2,1,4),_EtsysMulti1xAeEapolLogoffFramesRx_Type())
etsysMulti1xAeEapolLogoffFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeEapolLogoffFramesRx.setStatus(_A)
_EtsysMulti1xAeEapolRespIdFramesRx_Type=Counter32
_EtsysMulti1xAeEapolRespIdFramesRx_Object=MibTableColumn
etsysMulti1xAeEapolRespIdFramesRx=_EtsysMulti1xAeEapolRespIdFramesRx_Object((1,3,6,1,4,1,5624,1,2,53,1,2,2,1,5),_EtsysMulti1xAeEapolRespIdFramesRx_Type())
etsysMulti1xAeEapolRespIdFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeEapolRespIdFramesRx.setStatus(_A)
_EtsysMulti1xAeEapolRespFramesRx_Type=Counter32
_EtsysMulti1xAeEapolRespFramesRx_Object=MibTableColumn
etsysMulti1xAeEapolRespFramesRx=_EtsysMulti1xAeEapolRespFramesRx_Object((1,3,6,1,4,1,5624,1,2,53,1,2,2,1,6),_EtsysMulti1xAeEapolRespFramesRx_Type())
etsysMulti1xAeEapolRespFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeEapolRespFramesRx.setStatus(_A)
_EtsysMulti1xAeEapolReqIdFramesTx_Type=Counter32
_EtsysMulti1xAeEapolReqIdFramesTx_Object=MibTableColumn
etsysMulti1xAeEapolReqIdFramesTx=_EtsysMulti1xAeEapolReqIdFramesTx_Object((1,3,6,1,4,1,5624,1,2,53,1,2,2,1,7),_EtsysMulti1xAeEapolReqIdFramesTx_Type())
etsysMulti1xAeEapolReqIdFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeEapolReqIdFramesTx.setStatus(_A)
_EtsysMulti1xAeEapolReqFramesTx_Type=Counter32
_EtsysMulti1xAeEapolReqFramesTx_Object=MibTableColumn
etsysMulti1xAeEapolReqFramesTx=_EtsysMulti1xAeEapolReqFramesTx_Object((1,3,6,1,4,1,5624,1,2,53,1,2,2,1,8),_EtsysMulti1xAeEapolReqFramesTx_Type())
etsysMulti1xAeEapolReqFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeEapolReqFramesTx.setStatus(_A)
_EtsysMulti1xAeInvalidEapolFramesRx_Type=Counter32
_EtsysMulti1xAeInvalidEapolFramesRx_Object=MibTableColumn
etsysMulti1xAeInvalidEapolFramesRx=_EtsysMulti1xAeInvalidEapolFramesRx_Object((1,3,6,1,4,1,5624,1,2,53,1,2,2,1,9),_EtsysMulti1xAeInvalidEapolFramesRx_Type())
etsysMulti1xAeInvalidEapolFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeInvalidEapolFramesRx.setStatus(_A)
_EtsysMulti1xAeEapLengthErrorFramesRx_Type=Counter32
_EtsysMulti1xAeEapLengthErrorFramesRx_Object=MibTableColumn
etsysMulti1xAeEapLengthErrorFramesRx=_EtsysMulti1xAeEapLengthErrorFramesRx_Object((1,3,6,1,4,1,5624,1,2,53,1,2,2,1,10),_EtsysMulti1xAeEapLengthErrorFramesRx_Type())
etsysMulti1xAeEapLengthErrorFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeEapLengthErrorFramesRx.setStatus(_A)
_EtsysMulti1xAeEapolFrameVersion_Type=Unsigned32
_EtsysMulti1xAeEapolFrameVersion_Object=MibTableColumn
etsysMulti1xAeEapolFrameVersion=_EtsysMulti1xAeEapolFrameVersion_Object((1,3,6,1,4,1,5624,1,2,53,1,2,2,1,11),_EtsysMulti1xAeEapolFrameVersion_Type())
etsysMulti1xAeEapolFrameVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeEapolFrameVersion.setStatus(_A)
_EtsysMulti1xAeEapolFrameSource_Type=MacAddress
_EtsysMulti1xAeEapolFrameSource_Object=MibTableColumn
etsysMulti1xAeEapolFrameSource=_EtsysMulti1xAeEapolFrameSource_Object((1,3,6,1,4,1,5624,1,2,53,1,2,2,1,12),_EtsysMulti1xAeEapolFrameSource_Type())
etsysMulti1xAeEapolFrameSource.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeEapolFrameSource.setStatus(_A)
_EtsysMulti1xAeDiagTable_Object=MibTable
etsysMulti1xAeDiagTable=_EtsysMulti1xAeDiagTable_Object((1,3,6,1,4,1,5624,1,2,53,1,2,3))
if mibBuilder.loadTexts:etsysMulti1xAeDiagTable.setStatus(_A)
_EtsysMulti1xAeDiagEntry_Object=MibTableRow
etsysMulti1xAeDiagEntry=_EtsysMulti1xAeDiagEntry_Object((1,3,6,1,4,1,5624,1,2,53,1,2,3,1))
if mibBuilder.loadTexts:etsysMulti1xAeDiagEntry.setStatus(_A)
_EtsysMulti1xAeEntersConnecting_Type=Counter32
_EtsysMulti1xAeEntersConnecting_Object=MibTableColumn
etsysMulti1xAeEntersConnecting=_EtsysMulti1xAeEntersConnecting_Object((1,3,6,1,4,1,5624,1,2,53,1,2,3,1,1),_EtsysMulti1xAeEntersConnecting_Type())
etsysMulti1xAeEntersConnecting.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeEntersConnecting.setStatus(_A)
_EtsysMulti1xAeEapLogoffsWhileConnecting_Type=Counter32
_EtsysMulti1xAeEapLogoffsWhileConnecting_Object=MibTableColumn
etsysMulti1xAeEapLogoffsWhileConnecting=_EtsysMulti1xAeEapLogoffsWhileConnecting_Object((1,3,6,1,4,1,5624,1,2,53,1,2,3,1,2),_EtsysMulti1xAeEapLogoffsWhileConnecting_Type())
etsysMulti1xAeEapLogoffsWhileConnecting.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeEapLogoffsWhileConnecting.setStatus(_A)
_EtsysMulti1xAeEntersAuthenticating_Type=Counter32
_EtsysMulti1xAeEntersAuthenticating_Object=MibTableColumn
etsysMulti1xAeEntersAuthenticating=_EtsysMulti1xAeEntersAuthenticating_Object((1,3,6,1,4,1,5624,1,2,53,1,2,3,1,3),_EtsysMulti1xAeEntersAuthenticating_Type())
etsysMulti1xAeEntersAuthenticating.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeEntersAuthenticating.setStatus(_A)
_EtsysMulti1xAeAuthSuccessWhileAuthenticating_Type=Counter32
_EtsysMulti1xAeAuthSuccessWhileAuthenticating_Object=MibTableColumn
etsysMulti1xAeAuthSuccessWhileAuthenticating=_EtsysMulti1xAeAuthSuccessWhileAuthenticating_Object((1,3,6,1,4,1,5624,1,2,53,1,2,3,1,4),_EtsysMulti1xAeAuthSuccessWhileAuthenticating_Type())
etsysMulti1xAeAuthSuccessWhileAuthenticating.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeAuthSuccessWhileAuthenticating.setStatus(_A)
_EtsysMulti1xAeAuthTimeoutsWhileAuthenticating_Type=Counter32
_EtsysMulti1xAeAuthTimeoutsWhileAuthenticating_Object=MibTableColumn
etsysMulti1xAeAuthTimeoutsWhileAuthenticating=_EtsysMulti1xAeAuthTimeoutsWhileAuthenticating_Object((1,3,6,1,4,1,5624,1,2,53,1,2,3,1,5),_EtsysMulti1xAeAuthTimeoutsWhileAuthenticating_Type())
etsysMulti1xAeAuthTimeoutsWhileAuthenticating.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeAuthTimeoutsWhileAuthenticating.setStatus(_A)
_EtsysMulti1xAeAuthFailWhileAuthenticating_Type=Counter32
_EtsysMulti1xAeAuthFailWhileAuthenticating_Object=MibTableColumn
etsysMulti1xAeAuthFailWhileAuthenticating=_EtsysMulti1xAeAuthFailWhileAuthenticating_Object((1,3,6,1,4,1,5624,1,2,53,1,2,3,1,6),_EtsysMulti1xAeAuthFailWhileAuthenticating_Type())
etsysMulti1xAeAuthFailWhileAuthenticating.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeAuthFailWhileAuthenticating.setStatus(_A)
_EtsysMulti1xAeAuthReauthsWhileAuthenticating_Type=Counter32
_EtsysMulti1xAeAuthReauthsWhileAuthenticating_Object=MibTableColumn
etsysMulti1xAeAuthReauthsWhileAuthenticating=_EtsysMulti1xAeAuthReauthsWhileAuthenticating_Object((1,3,6,1,4,1,5624,1,2,53,1,2,3,1,7),_EtsysMulti1xAeAuthReauthsWhileAuthenticating_Type())
etsysMulti1xAeAuthReauthsWhileAuthenticating.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeAuthReauthsWhileAuthenticating.setStatus(_A)
_EtsysMulti1xAeAuthEapStartsWhileAuthenticating_Type=Counter32
_EtsysMulti1xAeAuthEapStartsWhileAuthenticating_Object=MibTableColumn
etsysMulti1xAeAuthEapStartsWhileAuthenticating=_EtsysMulti1xAeAuthEapStartsWhileAuthenticating_Object((1,3,6,1,4,1,5624,1,2,53,1,2,3,1,8),_EtsysMulti1xAeAuthEapStartsWhileAuthenticating_Type())
etsysMulti1xAeAuthEapStartsWhileAuthenticating.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeAuthEapStartsWhileAuthenticating.setStatus(_A)
_EtsysMulti1xAeAuthEapLogoffWhileAuthenticating_Type=Counter32
_EtsysMulti1xAeAuthEapLogoffWhileAuthenticating_Object=MibTableColumn
etsysMulti1xAeAuthEapLogoffWhileAuthenticating=_EtsysMulti1xAeAuthEapLogoffWhileAuthenticating_Object((1,3,6,1,4,1,5624,1,2,53,1,2,3,1,9),_EtsysMulti1xAeAuthEapLogoffWhileAuthenticating_Type())
etsysMulti1xAeAuthEapLogoffWhileAuthenticating.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeAuthEapLogoffWhileAuthenticating.setStatus(_A)
_EtsysMulti1xAeAuthReauthsWhileAuthenticated_Type=Counter32
_EtsysMulti1xAeAuthReauthsWhileAuthenticated_Object=MibTableColumn
etsysMulti1xAeAuthReauthsWhileAuthenticated=_EtsysMulti1xAeAuthReauthsWhileAuthenticated_Object((1,3,6,1,4,1,5624,1,2,53,1,2,3,1,10),_EtsysMulti1xAeAuthReauthsWhileAuthenticated_Type())
etsysMulti1xAeAuthReauthsWhileAuthenticated.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeAuthReauthsWhileAuthenticated.setStatus(_A)
_EtsysMulti1xAeAuthEapStartsWhileAuthenticated_Type=Counter32
_EtsysMulti1xAeAuthEapStartsWhileAuthenticated_Object=MibTableColumn
etsysMulti1xAeAuthEapStartsWhileAuthenticated=_EtsysMulti1xAeAuthEapStartsWhileAuthenticated_Object((1,3,6,1,4,1,5624,1,2,53,1,2,3,1,11),_EtsysMulti1xAeAuthEapStartsWhileAuthenticated_Type())
etsysMulti1xAeAuthEapStartsWhileAuthenticated.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeAuthEapStartsWhileAuthenticated.setStatus(_A)
_EtsysMulti1xAeAuthEapLogoffWhileAuthenticated_Type=Counter32
_EtsysMulti1xAeAuthEapLogoffWhileAuthenticated_Object=MibTableColumn
etsysMulti1xAeAuthEapLogoffWhileAuthenticated=_EtsysMulti1xAeAuthEapLogoffWhileAuthenticated_Object((1,3,6,1,4,1,5624,1,2,53,1,2,3,1,12),_EtsysMulti1xAeAuthEapLogoffWhileAuthenticated_Type())
etsysMulti1xAeAuthEapLogoffWhileAuthenticated.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeAuthEapLogoffWhileAuthenticated.setStatus(_A)
_EtsysMulti1xAeBackendResponses_Type=Counter32
_EtsysMulti1xAeBackendResponses_Object=MibTableColumn
etsysMulti1xAeBackendResponses=_EtsysMulti1xAeBackendResponses_Object((1,3,6,1,4,1,5624,1,2,53,1,2,3,1,13),_EtsysMulti1xAeBackendResponses_Type())
etsysMulti1xAeBackendResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeBackendResponses.setStatus(_A)
_EtsysMulti1xAeBackendAccessChallenges_Type=Counter32
_EtsysMulti1xAeBackendAccessChallenges_Object=MibTableColumn
etsysMulti1xAeBackendAccessChallenges=_EtsysMulti1xAeBackendAccessChallenges_Object((1,3,6,1,4,1,5624,1,2,53,1,2,3,1,14),_EtsysMulti1xAeBackendAccessChallenges_Type())
etsysMulti1xAeBackendAccessChallenges.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeBackendAccessChallenges.setStatus(_A)
_EtsysMulti1xAeBackendOtherRequestsToSupplicant_Type=Counter32
_EtsysMulti1xAeBackendOtherRequestsToSupplicant_Object=MibTableColumn
etsysMulti1xAeBackendOtherRequestsToSupplicant=_EtsysMulti1xAeBackendOtherRequestsToSupplicant_Object((1,3,6,1,4,1,5624,1,2,53,1,2,3,1,15),_EtsysMulti1xAeBackendOtherRequestsToSupplicant_Type())
etsysMulti1xAeBackendOtherRequestsToSupplicant.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeBackendOtherRequestsToSupplicant.setStatus(_A)
_EtsysMulti1xAeBackendNonNakResponsesFromSupplicant_Type=Counter32
_EtsysMulti1xAeBackendNonNakResponsesFromSupplicant_Object=MibTableColumn
etsysMulti1xAeBackendNonNakResponsesFromSupplicant=_EtsysMulti1xAeBackendNonNakResponsesFromSupplicant_Object((1,3,6,1,4,1,5624,1,2,53,1,2,3,1,16),_EtsysMulti1xAeBackendNonNakResponsesFromSupplicant_Type())
etsysMulti1xAeBackendNonNakResponsesFromSupplicant.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeBackendNonNakResponsesFromSupplicant.setStatus(_A)
_EtsysMulti1xAeBackendAuthSuccesses_Type=Counter32
_EtsysMulti1xAeBackendAuthSuccesses_Object=MibTableColumn
etsysMulti1xAeBackendAuthSuccesses=_EtsysMulti1xAeBackendAuthSuccesses_Object((1,3,6,1,4,1,5624,1,2,53,1,2,3,1,17),_EtsysMulti1xAeBackendAuthSuccesses_Type())
etsysMulti1xAeBackendAuthSuccesses.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeBackendAuthSuccesses.setStatus(_A)
_EtsysMulti1xAeBackendAuthFails_Type=Counter32
_EtsysMulti1xAeBackendAuthFails_Object=MibTableColumn
etsysMulti1xAeBackendAuthFails=_EtsysMulti1xAeBackendAuthFails_Object((1,3,6,1,4,1,5624,1,2,53,1,2,3,1,18),_EtsysMulti1xAeBackendAuthFails_Type())
etsysMulti1xAeBackendAuthFails.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xAeBackendAuthFails.setStatus(_A)
_EtsysMulti1xSessionStatsTable_Object=MibTable
etsysMulti1xSessionStatsTable=_EtsysMulti1xSessionStatsTable_Object((1,3,6,1,4,1,5624,1,2,53,1,2,4))
if mibBuilder.loadTexts:etsysMulti1xSessionStatsTable.setStatus(_A)
_EtsysMulti1xSessionStatsEntry_Object=MibTableRow
etsysMulti1xSessionStatsEntry=_EtsysMulti1xSessionStatsEntry_Object((1,3,6,1,4,1,5624,1,2,53,1,2,4,1))
if mibBuilder.loadTexts:etsysMulti1xSessionStatsEntry.setStatus(_A)
_EtsysMulti1xSessionOctetsRx_Type=Counter64
_EtsysMulti1xSessionOctetsRx_Object=MibTableColumn
etsysMulti1xSessionOctetsRx=_EtsysMulti1xSessionOctetsRx_Object((1,3,6,1,4,1,5624,1,2,53,1,2,4,1,1),_EtsysMulti1xSessionOctetsRx_Type())
etsysMulti1xSessionOctetsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xSessionOctetsRx.setStatus(_A)
_EtsysMulti1xSessionOctetsTx_Type=Counter64
_EtsysMulti1xSessionOctetsTx_Object=MibTableColumn
etsysMulti1xSessionOctetsTx=_EtsysMulti1xSessionOctetsTx_Object((1,3,6,1,4,1,5624,1,2,53,1,2,4,1,2),_EtsysMulti1xSessionOctetsTx_Type())
etsysMulti1xSessionOctetsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xSessionOctetsTx.setStatus(_A)
_EtsysMulti1xSessionFramesRx_Type=Counter32
_EtsysMulti1xSessionFramesRx_Object=MibTableColumn
etsysMulti1xSessionFramesRx=_EtsysMulti1xSessionFramesRx_Object((1,3,6,1,4,1,5624,1,2,53,1,2,4,1,3),_EtsysMulti1xSessionFramesRx_Type())
etsysMulti1xSessionFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xSessionFramesRx.setStatus(_A)
_EtsysMulti1xSessionFramesTx_Type=Counter32
_EtsysMulti1xSessionFramesTx_Object=MibTableColumn
etsysMulti1xSessionFramesTx=_EtsysMulti1xSessionFramesTx_Object((1,3,6,1,4,1,5624,1,2,53,1,2,4,1,4),_EtsysMulti1xSessionFramesTx_Type())
etsysMulti1xSessionFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xSessionFramesTx.setStatus(_A)
_EtsysMulti1xSessionId_Type=SnmpAdminString
_EtsysMulti1xSessionId_Object=MibTableColumn
etsysMulti1xSessionId=_EtsysMulti1xSessionId_Object((1,3,6,1,4,1,5624,1,2,53,1,2,4,1,5),_EtsysMulti1xSessionId_Type())
etsysMulti1xSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xSessionId.setStatus(_A)
class _EtsysMulti1xSessionAuthenticMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('remoteAuthServer',1),('localAuthServer',2)))
_EtsysMulti1xSessionAuthenticMethod_Type.__name__=_F
_EtsysMulti1xSessionAuthenticMethod_Object=MibTableColumn
etsysMulti1xSessionAuthenticMethod=_EtsysMulti1xSessionAuthenticMethod_Object((1,3,6,1,4,1,5624,1,2,53,1,2,4,1,6),_EtsysMulti1xSessionAuthenticMethod_Type())
etsysMulti1xSessionAuthenticMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xSessionAuthenticMethod.setStatus(_A)
_EtsysMulti1xSessionTime_Type=TimeTicks
_EtsysMulti1xSessionTime_Object=MibTableColumn
etsysMulti1xSessionTime=_EtsysMulti1xSessionTime_Object((1,3,6,1,4,1,5624,1,2,53,1,2,4,1,7),_EtsysMulti1xSessionTime_Type())
etsysMulti1xSessionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xSessionTime.setStatus(_A)
class _EtsysMulti1xSessionTerminateCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,999)));namedValues=NamedValues(*(('supplicantLogoff',1),('portFailure',2),('supplicantRestart',3),('reauthFailed',4),('authControlForceUnauth',5),('portReInit',6),('portAdminDisabled',7),('notTerminatedYet',999)))
_EtsysMulti1xSessionTerminateCause_Type.__name__=_F
_EtsysMulti1xSessionTerminateCause_Object=MibTableColumn
etsysMulti1xSessionTerminateCause=_EtsysMulti1xSessionTerminateCause_Object((1,3,6,1,4,1,5624,1,2,53,1,2,4,1,8),_EtsysMulti1xSessionTerminateCause_Type())
etsysMulti1xSessionTerminateCause.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xSessionTerminateCause.setStatus(_A)
_EtsysMulti1xSessionUserName_Type=SnmpAdminString
_EtsysMulti1xSessionUserName_Object=MibTableColumn
etsysMulti1xSessionUserName=_EtsysMulti1xSessionUserName_Object((1,3,6,1,4,1,5624,1,2,53,1,2,4,1,9),_EtsysMulti1xSessionUserName_Type())
etsysMulti1xSessionUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xSessionUserName.setStatus(_A)
_EtsysMulti1xSessionActive_Type=TruthValue
_EtsysMulti1xSessionActive_Object=MibTableColumn
etsysMulti1xSessionActive=_EtsysMulti1xSessionActive_Object((1,3,6,1,4,1,5624,1,2,53,1,2,4,1,10),_EtsysMulti1xSessionActive_Type())
etsysMulti1xSessionActive.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xSessionActive.setStatus(_A)
_EtsysMulti1xSupplicantAddressTable_Object=MibTable
etsysMulti1xSupplicantAddressTable=_EtsysMulti1xSupplicantAddressTable_Object((1,3,6,1,4,1,5624,1,2,53,1,2,5))
if mibBuilder.loadTexts:etsysMulti1xSupplicantAddressTable.setStatus(_A)
_EtsysMulti1xSupplicantAddressEntry_Object=MibTableRow
etsysMulti1xSupplicantAddressEntry=_EtsysMulti1xSupplicantAddressEntry_Object((1,3,6,1,4,1,5624,1,2,53,1,2,5,1))
etsysMulti1xSupplicantAddressEntry.setIndexNames((0,_B,_I),(0,_D,_E),(0,_B,_G))
if mibBuilder.loadTexts:etsysMulti1xSupplicantAddressEntry.setStatus(_A)
_EtsysMulti1xSupplicantActive_Type=TruthValue
_EtsysMulti1xSupplicantActive_Object=MibTableColumn
etsysMulti1xSupplicantActive=_EtsysMulti1xSupplicantActive_Object((1,3,6,1,4,1,5624,1,2,53,1,2,5,1,1),_EtsysMulti1xSupplicantActive_Type())
etsysMulti1xSupplicantActive.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xSupplicantActive.setStatus(_A)
_EtsysMulti1xSupplicantUserName_Type=SnmpAdminString
_EtsysMulti1xSupplicantUserName_Object=MibTableColumn
etsysMulti1xSupplicantUserName=_EtsysMulti1xSupplicantUserName_Object((1,3,6,1,4,1,5624,1,2,53,1,2,5,1,2),_EtsysMulti1xSupplicantUserName_Type())
etsysMulti1xSupplicantUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xSupplicantUserName.setStatus(_A)
_EtsysMulti1xUserNameTable_Object=MibTable
etsysMulti1xUserNameTable=_EtsysMulti1xUserNameTable_Object((1,3,6,1,4,1,5624,1,2,53,1,2,6))
if mibBuilder.loadTexts:etsysMulti1xUserNameTable.setStatus(_A)
_EtsysMulti1xUserNameEntry_Object=MibTableRow
etsysMulti1xUserNameEntry=_EtsysMulti1xUserNameEntry_Object((1,3,6,1,4,1,5624,1,2,53,1,2,6,1))
etsysMulti1xUserNameEntry.setIndexNames((0,_B,_V),(0,_D,_E),(0,_B,_G))
if mibBuilder.loadTexts:etsysMulti1xUserNameEntry.setStatus(_A)
class _EtsysMulti1xUserNameIndex_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_EtsysMulti1xUserNameIndex_Type.__name__=_R
_EtsysMulti1xUserNameIndex_Object=MibTableColumn
etsysMulti1xUserNameIndex=_EtsysMulti1xUserNameIndex_Object((1,3,6,1,4,1,5624,1,2,53,1,2,6,1,1),_EtsysMulti1xUserNameIndex_Type())
etsysMulti1xUserNameIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:etsysMulti1xUserNameIndex.setStatus(_A)
_EtsysMulti1xUserName_Type=SnmpAdminString
_EtsysMulti1xUserName_Object=MibTableColumn
etsysMulti1xUserName=_EtsysMulti1xUserName_Object((1,3,6,1,4,1,5624,1,2,53,1,2,6,1,2),_EtsysMulti1xUserName_Type())
etsysMulti1xUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xUserName.setStatus(_A)
_EtsysMulti1xUserActive_Type=TruthValue
_EtsysMulti1xUserActive_Object=MibTableColumn
etsysMulti1xUserActive=_EtsysMulti1xUserActive_Object((1,3,6,1,4,1,5624,1,2,53,1,2,6,1,3),_EtsysMulti1xUserActive_Type())
etsysMulti1xUserActive.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xUserActive.setStatus(_A)
_EtsysMulti1xUserAddress_Type=MacAddress
_EtsysMulti1xUserAddress_Object=MibTableColumn
etsysMulti1xUserAddress=_EtsysMulti1xUserAddress_Object((1,3,6,1,4,1,5624,1,2,53,1,2,6,1,4),_EtsysMulti1xUserAddress_Type())
etsysMulti1xUserAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xUserAddress.setStatus(_A)
_EtsysMulti1xActiveAccessEntityTable_Object=MibTable
etsysMulti1xActiveAccessEntityTable=_EtsysMulti1xActiveAccessEntityTable_Object((1,3,6,1,4,1,5624,1,2,53,1,2,7))
if mibBuilder.loadTexts:etsysMulti1xActiveAccessEntityTable.setStatus(_A)
_EtsysMulti1xActiveAccessEntityEntry_Object=MibTableRow
etsysMulti1xActiveAccessEntityEntry=_EtsysMulti1xActiveAccessEntityEntry_Object((1,3,6,1,4,1,5624,1,2,53,1,2,7,1))
etsysMulti1xActiveAccessEntityEntry.setIndexNames((0,_D,_E),(0,_B,_G))
if mibBuilder.loadTexts:etsysMulti1xActiveAccessEntityEntry.setStatus(_A)
_EtsysMulti1xActiveSupplicantAddress_Type=MacAddress
_EtsysMulti1xActiveSupplicantAddress_Object=MibTableColumn
etsysMulti1xActiveSupplicantAddress=_EtsysMulti1xActiveSupplicantAddress_Object((1,3,6,1,4,1,5624,1,2,53,1,2,7,1,1),_EtsysMulti1xActiveSupplicantAddress_Type())
etsysMulti1xActiveSupplicantAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMulti1xActiveSupplicantAddress.setStatus(_A)
_EtsysMultiUser8021xConformance_ObjectIdentity=ObjectIdentity
etsysMultiUser8021xConformance=_EtsysMultiUser8021xConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,53,2))
_EtsysMultiUser8021xGroups_ObjectIdentity=ObjectIdentity
etsysMultiUser8021xGroups=_EtsysMultiUser8021xGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,53,2,1))
_EtsysMultiUser8021xCompliances_ObjectIdentity=ObjectIdentity
etsysMultiUser8021xCompliances=_EtsysMultiUser8021xCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,53,2,2))
etsysMulti1xAccessEntityEntry.registerAugmentions((_B,_W))
etsysMulti1xAccessEntityStatsEntry.setIndexNames(*etsysMulti1xAccessEntityEntry.getIndexNames())
etsysMulti1xAccessEntityEntry.registerAugmentions((_B,_X))
etsysMulti1xAeDiagEntry.setIndexNames(*etsysMulti1xAccessEntityEntry.getIndexNames())
etsysMulti1xAccessEntityEntry.registerAugmentions((_B,_Y))
etsysMulti1xSessionStatsEntry.setIndexNames(*etsysMulti1xAccessEntityEntry.getIndexNames())
etsysMultiUser8021xAccessEntityGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,53,2,1,1))
etsysMultiUser8021xAccessEntityGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_I),(_B,_f)))
if mibBuilder.loadTexts:etsysMultiUser8021xAccessEntityGroup.setStatus(_A)
etsysMultiUser8021xAccessEntityStatsGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,53,2,1,2))
etsysMultiUser8021xAccessEntityStatsGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:etsysMultiUser8021xAccessEntityStatsGroup.setStatus(_A)
etsysMultiUser8021xAccessEntityDiagGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,53,2,1,3))
etsysMultiUser8021xAccessEntityDiagGroup.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:etsysMultiUser8021xAccessEntityDiagGroup.setStatus(_A)
etsysMultiUser8021xAccessEntitySessionGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,53,2,1,4))
etsysMultiUser8021xAccessEntitySessionGroup.setObjects(*((_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:etsysMultiUser8021xAccessEntitySessionGroup.setStatus(_A)
etsysMultiUser8021xSupplicantAddressGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,53,2,1,5))
etsysMultiUser8021xSupplicantAddressGroup.setObjects(*((_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:etsysMultiUser8021xSupplicantAddressGroup.setStatus(_A)
etsysMultiUser8021xUserNameGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,53,2,1,6))
etsysMultiUser8021xUserNameGroup.setObjects(*((_B,_AM),(_B,_AN),(_B,_AO)))
if mibBuilder.loadTexts:etsysMultiUser8021xUserNameGroup.setStatus(_A)
etsysMultiUser8021xActiveAccessEntityGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,53,2,1,7))
etsysMultiUser8021xActiveAccessEntityGroup.setObjects((_B,_AP))
if mibBuilder.loadTexts:etsysMultiUser8021xActiveAccessEntityGroup.setStatus(_A)
etsysMultiUser8021xSystemGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,53,2,1,8))
etsysMultiUser8021xSystemGroup.setObjects((_B,_AQ))
if mibBuilder.loadTexts:etsysMultiUser8021xSystemGroup.setStatus(_A)
etsysMulti8021xCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,53,2,2,1))
etsysMulti8021xCompliance.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:etsysMulti8021xCompliance.setStatus('deprecated')
etsysMulti8021xCompliance2=ModuleCompliance((1,3,6,1,4,1,5624,1,2,53,2,2,2))
etsysMulti8021xCompliance2.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_AR)))
if mibBuilder.loadTexts:etsysMulti8021xCompliance2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysMultiUser8021xMIB':etsysMultiUser8021xMIB,'etsysMultiUser8021xObjects':etsysMultiUser8021xObjects,'etsysMultiUser8021xSystem':etsysMultiUser8021xSystem,_AQ:etsysMulti1xSystemAccountEnable,'etsysMultiUser8021xAccessEntity':etsysMultiUser8021xAccessEntity,'etsysMulti1xAccessEntityTable':etsysMulti1xAccessEntityTable,'etsysMulti1xAccessEntityEntry':etsysMulti1xAccessEntityEntry,_G:etsysMulti1xAeIndex,_Z:etsysMulti1xAeActive,_a:etsysMulti1xAeState,_b:etsysMulti1xAeBackendAuthState,_c:etsysMulti1xAeInitialize,_d:etsysMulti1xAeReauthenticate,_e:etsysMulti1xAeReAuthPeriod,_I:etsysMulti1xAeSupplicantAddress,_f:etsysMulti1xAeUserName,'etsysMulti1xAccessEntityStatsTable':etsysMulti1xAccessEntityStatsTable,_W:etsysMulti1xAccessEntityStatsEntry,_g:etsysMulti1xAeEapolFramesRx,_h:etsysMulti1xAeEapolFramesTx,_i:etsysMulti1xAeEapolStartFramesRx,_j:etsysMulti1xAeEapolLogoffFramesRx,_k:etsysMulti1xAeEapolRespIdFramesRx,_l:etsysMulti1xAeEapolRespFramesRx,_m:etsysMulti1xAeEapolReqIdFramesTx,_n:etsysMulti1xAeEapolReqFramesTx,_o:etsysMulti1xAeInvalidEapolFramesRx,_p:etsysMulti1xAeEapLengthErrorFramesRx,_q:etsysMulti1xAeEapolFrameVersion,_r:etsysMulti1xAeEapolFrameSource,'etsysMulti1xAeDiagTable':etsysMulti1xAeDiagTable,_X:etsysMulti1xAeDiagEntry,_s:etsysMulti1xAeEntersConnecting,_t:etsysMulti1xAeEapLogoffsWhileConnecting,_u:etsysMulti1xAeEntersAuthenticating,_v:etsysMulti1xAeAuthSuccessWhileAuthenticating,_w:etsysMulti1xAeAuthTimeoutsWhileAuthenticating,_x:etsysMulti1xAeAuthFailWhileAuthenticating,_y:etsysMulti1xAeAuthReauthsWhileAuthenticating,_z:etsysMulti1xAeAuthEapStartsWhileAuthenticating,_A0:etsysMulti1xAeAuthEapLogoffWhileAuthenticating,_A1:etsysMulti1xAeAuthReauthsWhileAuthenticated,_A2:etsysMulti1xAeAuthEapStartsWhileAuthenticated,_A3:etsysMulti1xAeAuthEapLogoffWhileAuthenticated,_A4:etsysMulti1xAeBackendResponses,_A5:etsysMulti1xAeBackendAccessChallenges,_A6:etsysMulti1xAeBackendOtherRequestsToSupplicant,_A7:etsysMulti1xAeBackendNonNakResponsesFromSupplicant,_A8:etsysMulti1xAeBackendAuthSuccesses,_A9:etsysMulti1xAeBackendAuthFails,'etsysMulti1xSessionStatsTable':etsysMulti1xSessionStatsTable,_Y:etsysMulti1xSessionStatsEntry,_AA:etsysMulti1xSessionOctetsRx,_AB:etsysMulti1xSessionOctetsTx,_AC:etsysMulti1xSessionFramesRx,_AD:etsysMulti1xSessionFramesTx,_AE:etsysMulti1xSessionId,_AF:etsysMulti1xSessionAuthenticMethod,_AG:etsysMulti1xSessionTime,_AH:etsysMulti1xSessionTerminateCause,_AI:etsysMulti1xSessionUserName,_AJ:etsysMulti1xSessionActive,'etsysMulti1xSupplicantAddressTable':etsysMulti1xSupplicantAddressTable,'etsysMulti1xSupplicantAddressEntry':etsysMulti1xSupplicantAddressEntry,_AK:etsysMulti1xSupplicantActive,_AL:etsysMulti1xSupplicantUserName,'etsysMulti1xUserNameTable':etsysMulti1xUserNameTable,'etsysMulti1xUserNameEntry':etsysMulti1xUserNameEntry,_V:etsysMulti1xUserNameIndex,_AM:etsysMulti1xUserName,_AN:etsysMulti1xUserActive,_AO:etsysMulti1xUserAddress,'etsysMulti1xActiveAccessEntityTable':etsysMulti1xActiveAccessEntityTable,'etsysMulti1xActiveAccessEntityEntry':etsysMulti1xActiveAccessEntityEntry,_AP:etsysMulti1xActiveSupplicantAddress,'etsysMultiUser8021xConformance':etsysMultiUser8021xConformance,'etsysMultiUser8021xGroups':etsysMultiUser8021xGroups,_J:etsysMultiUser8021xAccessEntityGroup,_K:etsysMultiUser8021xAccessEntityStatsGroup,_L:etsysMultiUser8021xAccessEntityDiagGroup,_M:etsysMultiUser8021xAccessEntitySessionGroup,_N:etsysMultiUser8021xSupplicantAddressGroup,_O:etsysMultiUser8021xUserNameGroup,_P:etsysMultiUser8021xActiveAccessEntityGroup,_AR:etsysMultiUser8021xSystemGroup,'etsysMultiUser8021xCompliances':etsysMultiUser8021xCompliances,'etsysMulti8021xCompliance':etsysMulti8021xCompliance,'etsysMulti8021xCompliance2':etsysMulti8021xCompliance2})