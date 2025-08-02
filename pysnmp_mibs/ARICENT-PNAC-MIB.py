_a='fsPnacTrapAuthSessionStatus'
_Z='fsPnacAuthSessionPortStatus'
_Y='fsPnacAuthSessionPortNumber'
_X='fsPnacPaePortStatus'
_W='fsPnacTrapAuthSessionEntry'
_V='fsDPnacPortIndex'
_U='fsPnacASUserConfigUserName'
_T='initialize'
_S='RemoteAuthServerType'
_R='disabled'
_Q='enabled'
_P='fsPnacPaePortNumber'
_O='dot1xAuthOperControlledDirections'
_N='IEEE8021-PAE-MIB'
_M='OctetString'
_L='fsDPnacSlotNumber'
_K='fsPnacAuthSessionSuppAddress'
_J='TruthValue'
_I='Unsigned32'
_H='deprecated'
_G='not-accessible'
_F='DisplayString'
_E='ARICENT-PNAC-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PaeControlledPortStatus,dot1xAuthOperControlledDirections=mibBuilder.importSymbols(_N,'PaeControlledPortStatus',_O)
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention',_J)
fspnac=ModuleIdentity((1,3,6,1,4,1,2076,64))
if mibBuilder.loadTexts:fspnac.setRevisions(('2012-09-05 00:00',))
class AuthenticMethod(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('remoteServer',1),('localServer',2)))
class RemoteAuthServerType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('radiusServer',1),('tacacsplusServer',2)))
class PermissionType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('deny',2)))
_FsPnacPaeSystem_ObjectIdentity=ObjectIdentity
fsPnacPaeSystem=_FsPnacPaeSystem_ObjectIdentity((1,3,6,1,4,1,2076,64,1))
class _FsPnacSystemControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsPnacSystemControl_Type.__name__=_D
_FsPnacSystemControl_Object=MibScalar
fsPnacSystemControl=_FsPnacSystemControl_Object((1,3,6,1,4,1,2076,64,1,1),_FsPnacSystemControl_Type())
fsPnacSystemControl.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPnacSystemControl.setStatus(_A)
class _FsPnacTraceOption_Type(Integer32):defaultValue=0
_FsPnacTraceOption_Type.__name__=_D
_FsPnacTraceOption_Object=MibScalar
fsPnacTraceOption=_FsPnacTraceOption_Object((1,3,6,1,4,1,2076,64,1,2),_FsPnacTraceOption_Type())
fsPnacTraceOption.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPnacTraceOption.setStatus(_A)
_FsPnacAuthenticServer_Type=AuthenticMethod
_FsPnacAuthenticServer_Object=MibScalar
fsPnacAuthenticServer=_FsPnacAuthenticServer_Object((1,3,6,1,4,1,2076,64,1,3),_FsPnacAuthenticServer_Type())
fsPnacAuthenticServer.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPnacAuthenticServer.setStatus(_A)
class _FsPnacNasId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_FsPnacNasId_Type.__name__=_F
_FsPnacNasId_Object=MibScalar
fsPnacNasId=_FsPnacNasId_Object((1,3,6,1,4,1,2076,64,1,4),_FsPnacNasId_Type())
fsPnacNasId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPnacNasId.setStatus(_H)
_FsPnacPaePortTable_Object=MibTable
fsPnacPaePortTable=_FsPnacPaePortTable_Object((1,3,6,1,4,1,2076,64,1,5))
if mibBuilder.loadTexts:fsPnacPaePortTable.setStatus(_A)
_FsPnacPaePortEntry_Object=MibTableRow
fsPnacPaePortEntry=_FsPnacPaePortEntry_Object((1,3,6,1,4,1,2076,64,1,5,1))
fsPnacPaePortEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:fsPnacPaePortEntry.setStatus(_A)
_FsPnacPaePortNumber_Type=InterfaceIndex
_FsPnacPaePortNumber_Object=MibTableColumn
fsPnacPaePortNumber=_FsPnacPaePortNumber_Object((1,3,6,1,4,1,2076,64,1,5,1,1),_FsPnacPaePortNumber_Type())
fsPnacPaePortNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:fsPnacPaePortNumber.setStatus(_A)
class _FsPnacPaePortAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('portBased',1),('macBased',2)))
_FsPnacPaePortAuthMode_Type.__name__=_D
_FsPnacPaePortAuthMode_Object=MibTableColumn
fsPnacPaePortAuthMode=_FsPnacPaePortAuthMode_Object((1,3,6,1,4,1,2076,64,1,5,1,2),_FsPnacPaePortAuthMode_Type())
fsPnacPaePortAuthMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPnacPaePortAuthMode.setStatus(_A)
_FsPnacPaePortSupplicantCount_Type=Counter32
_FsPnacPaePortSupplicantCount_Object=MibTableColumn
fsPnacPaePortSupplicantCount=_FsPnacPaePortSupplicantCount_Object((1,3,6,1,4,1,2076,64,1,5,1,3),_FsPnacPaePortSupplicantCount_Type())
fsPnacPaePortSupplicantCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPnacPaePortSupplicantCount.setStatus(_A)
class _FsPnacPaePortUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,63))
_FsPnacPaePortUserName_Type.__name__=_F
_FsPnacPaePortUserName_Object=MibTableColumn
fsPnacPaePortUserName=_FsPnacPaePortUserName_Object((1,3,6,1,4,1,2076,64,1,5,1,4),_FsPnacPaePortUserName_Type())
fsPnacPaePortUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPnacPaePortUserName.setStatus(_A)
class _FsPnacPaePortPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,20))
_FsPnacPaePortPassword_Type.__name__=_F
_FsPnacPaePortPassword_Object=MibTableColumn
fsPnacPaePortPassword=_FsPnacPaePortPassword_Object((1,3,6,1,4,1,2076,64,1,5,1,5),_FsPnacPaePortPassword_Type())
fsPnacPaePortPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPnacPaePortPassword.setStatus(_A)
_FsPnacPaePortStatus_Type=PaeControlledPortStatus
_FsPnacPaePortStatus_Object=MibTableColumn
fsPnacPaePortStatus=_FsPnacPaePortStatus_Object((1,3,6,1,4,1,2076,64,1,5,1,6),_FsPnacPaePortStatus_Type())
fsPnacPaePortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPnacPaePortStatus.setStatus(_A)
class _FsPnacPaePortStatisticsClear_Type(TruthValue):defaultValue=2
_FsPnacPaePortStatisticsClear_Type.__name__=_J
_FsPnacPaePortStatisticsClear_Object=MibTableColumn
fsPnacPaePortStatisticsClear=_FsPnacPaePortStatisticsClear_Object((1,3,6,1,4,1,2076,64,1,5,1,7),_FsPnacPaePortStatisticsClear_Type())
fsPnacPaePortStatisticsClear.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPnacPaePortStatisticsClear.setStatus(_A)
class _FsPnacPaePortAuthStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_FsPnacPaePortAuthStatus_Type.__name__=_D
_FsPnacPaePortAuthStatus_Object=MibTableColumn
fsPnacPaePortAuthStatus=_FsPnacPaePortAuthStatus_Object((1,3,6,1,4,1,2076,64,1,5,1,8),_FsPnacPaePortAuthStatus_Type())
fsPnacPaePortAuthStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPnacPaePortAuthStatus.setStatus(_H)
class _FsPnacPaeAuthReAuthMax_Type(Unsigned32):defaultValue=2
_FsPnacPaeAuthReAuthMax_Type.__name__=_I
_FsPnacPaeAuthReAuthMax_Object=MibTableColumn
fsPnacPaeAuthReAuthMax=_FsPnacPaeAuthReAuthMax_Object((1,3,6,1,4,1,2076,64,1,5,1,9),_FsPnacPaeAuthReAuthMax_Type())
fsPnacPaeAuthReAuthMax.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPnacPaeAuthReAuthMax.setStatus(_A)
class _FsPnacModuleOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_FsPnacModuleOperStatus_Type.__name__=_D
_FsPnacModuleOperStatus_Object=MibScalar
fsPnacModuleOperStatus=_FsPnacModuleOperStatus_Object((1,3,6,1,4,1,2076,64,1,6),_FsPnacModuleOperStatus_Type())
fsPnacModuleOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPnacModuleOperStatus.setStatus(_A)
class _FsPnacRemoteAuthServerType_Type(RemoteAuthServerType):defaultValue=1
_FsPnacRemoteAuthServerType_Type.__name__=_S
_FsPnacRemoteAuthServerType_Object=MibScalar
fsPnacRemoteAuthServerType=_FsPnacRemoteAuthServerType_Object((1,3,6,1,4,1,2076,64,1,7),_FsPnacRemoteAuthServerType_Type())
fsPnacRemoteAuthServerType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPnacRemoteAuthServerType.setStatus(_A)
_FsPnacPaeAuthenticator_ObjectIdentity=ObjectIdentity
fsPnacPaeAuthenticator=_FsPnacPaeAuthenticator_ObjectIdentity((1,3,6,1,4,1,2076,64,2))
_FsPnacAuthSessionTable_Object=MibTable
fsPnacAuthSessionTable=_FsPnacAuthSessionTable_Object((1,3,6,1,4,1,2076,64,2,1))
if mibBuilder.loadTexts:fsPnacAuthSessionTable.setStatus(_A)
_FsPnacAuthSessionEntry_Object=MibTableRow
fsPnacAuthSessionEntry=_FsPnacAuthSessionEntry_Object((1,3,6,1,4,1,2076,64,2,1,1))
fsPnacAuthSessionEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:fsPnacAuthSessionEntry.setStatus(_A)
_FsPnacAuthSessionSuppAddress_Type=MacAddress
_FsPnacAuthSessionSuppAddress_Object=MibTableColumn
fsPnacAuthSessionSuppAddress=_FsPnacAuthSessionSuppAddress_Object((1,3,6,1,4,1,2076,64,2,1,1,1),_FsPnacAuthSessionSuppAddress_Type())
fsPnacAuthSessionSuppAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:fsPnacAuthSessionSuppAddress.setStatus(_A)
_FsPnacAuthSessionIdentifier_Type=Integer32
_FsPnacAuthSessionIdentifier_Object=MibTableColumn
fsPnacAuthSessionIdentifier=_FsPnacAuthSessionIdentifier_Object((1,3,6,1,4,1,2076,64,2,1,1,2),_FsPnacAuthSessionIdentifier_Type())
fsPnacAuthSessionIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPnacAuthSessionIdentifier.setStatus(_A)
class _FsPnacAuthSessionAuthPaeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_T,1),('disconnected',2),('connecting',3),('authenticating',4),('authenticated',5),('aborting',6),('held',7),('forceAuth',8),('forceUnauth',9)))
_FsPnacAuthSessionAuthPaeState_Type.__name__=_D
_FsPnacAuthSessionAuthPaeState_Object=MibTableColumn
fsPnacAuthSessionAuthPaeState=_FsPnacAuthSessionAuthPaeState_Object((1,3,6,1,4,1,2076,64,2,1,1,3),_FsPnacAuthSessionAuthPaeState_Type())
fsPnacAuthSessionAuthPaeState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPnacAuthSessionAuthPaeState.setStatus(_A)
class _FsPnacAuthSessionBackendAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('request',1),('response',2),('success',3),('fail',4),('timeout',5),('idle',6),(_T,7)))
_FsPnacAuthSessionBackendAuthState_Type.__name__=_D
_FsPnacAuthSessionBackendAuthState_Object=MibTableColumn
fsPnacAuthSessionBackendAuthState=_FsPnacAuthSessionBackendAuthState_Object((1,3,6,1,4,1,2076,64,2,1,1,4),_FsPnacAuthSessionBackendAuthState_Type())
fsPnacAuthSessionBackendAuthState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPnacAuthSessionBackendAuthState.setStatus(_A)
_FsPnacAuthSessionPortStatus_Type=PaeControlledPortStatus
_FsPnacAuthSessionPortStatus_Object=MibTableColumn
fsPnacAuthSessionPortStatus=_FsPnacAuthSessionPortStatus_Object((1,3,6,1,4,1,2076,64,2,1,1,5),_FsPnacAuthSessionPortStatus_Type())
fsPnacAuthSessionPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPnacAuthSessionPortStatus.setStatus(_A)
_FsPnacAuthSessionPortNumber_Type=InterfaceIndex
_FsPnacAuthSessionPortNumber_Object=MibTableColumn
fsPnacAuthSessionPortNumber=_FsPnacAuthSessionPortNumber_Object((1,3,6,1,4,1,2076,64,2,1,1,6),_FsPnacAuthSessionPortNumber_Type())
fsPnacAuthSessionPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPnacAuthSessionPortNumber.setStatus(_A)
_FsPnacAuthSessionInitialize_Type=TruthValue
_FsPnacAuthSessionInitialize_Object=MibTableColumn
fsPnacAuthSessionInitialize=_FsPnacAuthSessionInitialize_Object((1,3,6,1,4,1,2076,64,2,1,1,7),_FsPnacAuthSessionInitialize_Type())
fsPnacAuthSessionInitialize.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPnacAuthSessionInitialize.setStatus(_H)
_FsPnacAuthSessionReauthenticate_Type=TruthValue
_FsPnacAuthSessionReauthenticate_Object=MibTableColumn
fsPnacAuthSessionReauthenticate=_FsPnacAuthSessionReauthenticate_Object((1,3,6,1,4,1,2076,64,2,1,1,8),_FsPnacAuthSessionReauthenticate_Type())
fsPnacAuthSessionReauthenticate.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPnacAuthSessionReauthenticate.setStatus(_H)
_FsPnacAuthSessionStatsTable_Object=MibTable
fsPnacAuthSessionStatsTable=_FsPnacAuthSessionStatsTable_Object((1,3,6,1,4,1,2076,64,2,2))
if mibBuilder.loadTexts:fsPnacAuthSessionStatsTable.setStatus(_A)
_FsPnacAuthSessionStatsEntry_Object=MibTableRow
fsPnacAuthSessionStatsEntry=_FsPnacAuthSessionStatsEntry_Object((1,3,6,1,4,1,2076,64,2,2,1))
fsPnacAuthSessionStatsEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:fsPnacAuthSessionStatsEntry.setStatus(_A)
_FsPnacAuthSessionOctetsRx_Type=Counter64
_FsPnacAuthSessionOctetsRx_Object=MibTableColumn
fsPnacAuthSessionOctetsRx=_FsPnacAuthSessionOctetsRx_Object((1,3,6,1,4,1,2076,64,2,2,1,1),_FsPnacAuthSessionOctetsRx_Type())
fsPnacAuthSessionOctetsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPnacAuthSessionOctetsRx.setStatus(_A)
_FsPnacAuthSessionOctetsTx_Type=Counter64
_FsPnacAuthSessionOctetsTx_Object=MibTableColumn
fsPnacAuthSessionOctetsTx=_FsPnacAuthSessionOctetsTx_Object((1,3,6,1,4,1,2076,64,2,2,1,2),_FsPnacAuthSessionOctetsTx_Type())
fsPnacAuthSessionOctetsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPnacAuthSessionOctetsTx.setStatus(_A)
_FsPnacAuthSessionFramesRx_Type=Counter32
_FsPnacAuthSessionFramesRx_Object=MibTableColumn
fsPnacAuthSessionFramesRx=_FsPnacAuthSessionFramesRx_Object((1,3,6,1,4,1,2076,64,2,2,1,3),_FsPnacAuthSessionFramesRx_Type())
fsPnacAuthSessionFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPnacAuthSessionFramesRx.setStatus(_A)
_FsPnacAuthSessionFramesTx_Type=Counter32
_FsPnacAuthSessionFramesTx_Object=MibTableColumn
fsPnacAuthSessionFramesTx=_FsPnacAuthSessionFramesTx_Object((1,3,6,1,4,1,2076,64,2,2,1,4),_FsPnacAuthSessionFramesTx_Type())
fsPnacAuthSessionFramesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPnacAuthSessionFramesTx.setStatus(_A)
_FsPnacAuthSessionId_Type=SnmpAdminString
_FsPnacAuthSessionId_Object=MibTableColumn
fsPnacAuthSessionId=_FsPnacAuthSessionId_Object((1,3,6,1,4,1,2076,64,2,2,1,5),_FsPnacAuthSessionId_Type())
fsPnacAuthSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPnacAuthSessionId.setStatus(_A)
class _FsPnacAuthSessionAuthenticMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('remoteAuthServer',1),('localAuthServer',2)))
_FsPnacAuthSessionAuthenticMethod_Type.__name__=_D
_FsPnacAuthSessionAuthenticMethod_Object=MibTableColumn
fsPnacAuthSessionAuthenticMethod=_FsPnacAuthSessionAuthenticMethod_Object((1,3,6,1,4,1,2076,64,2,2,1,6),_FsPnacAuthSessionAuthenticMethod_Type())
fsPnacAuthSessionAuthenticMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPnacAuthSessionAuthenticMethod.setStatus(_A)
_FsPnacAuthSessionTime_Type=TimeTicks
_FsPnacAuthSessionTime_Object=MibTableColumn
fsPnacAuthSessionTime=_FsPnacAuthSessionTime_Object((1,3,6,1,4,1,2076,64,2,2,1,7),_FsPnacAuthSessionTime_Type())
fsPnacAuthSessionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPnacAuthSessionTime.setStatus(_A)
class _FsPnacAuthSessionTerminateCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,999)));namedValues=NamedValues(*(('supplicantLogoff',1),('portFailure',2),('supplicantRestart',3),('reauthFailed',4),('authControlForceUnauth',5),('portReInit',6),('portAdminDisabled',7),('notTerminatedYet',999)))
_FsPnacAuthSessionTerminateCause_Type.__name__=_D
_FsPnacAuthSessionTerminateCause_Object=MibTableColumn
fsPnacAuthSessionTerminateCause=_FsPnacAuthSessionTerminateCause_Object((1,3,6,1,4,1,2076,64,2,2,1,8),_FsPnacAuthSessionTerminateCause_Type())
fsPnacAuthSessionTerminateCause.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPnacAuthSessionTerminateCause.setStatus(_A)
_FsPnacAuthSessionUserName_Type=SnmpAdminString
_FsPnacAuthSessionUserName_Object=MibTableColumn
fsPnacAuthSessionUserName=_FsPnacAuthSessionUserName_Object((1,3,6,1,4,1,2076,64,2,2,1,9),_FsPnacAuthSessionUserName_Type())
fsPnacAuthSessionUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPnacAuthSessionUserName.setStatus(_A)
class _FsPnacAuthSessionStatisticsClear_Type(TruthValue):defaultValue=2
_FsPnacAuthSessionStatisticsClear_Type.__name__=_J
_FsPnacAuthSessionStatisticsClear_Object=MibTableColumn
fsPnacAuthSessionStatisticsClear=_FsPnacAuthSessionStatisticsClear_Object((1,3,6,1,4,1,2076,64,2,2,1,10),_FsPnacAuthSessionStatisticsClear_Type())
fsPnacAuthSessionStatisticsClear.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPnacAuthSessionStatisticsClear.setStatus(_A)
_FsPnacAuthServer_ObjectIdentity=ObjectIdentity
fsPnacAuthServer=_FsPnacAuthServer_ObjectIdentity((1,3,6,1,4,1,2076,64,3))
_FsPnacASUserConfigTable_Object=MibTable
fsPnacASUserConfigTable=_FsPnacASUserConfigTable_Object((1,3,6,1,4,1,2076,64,3,1))
if mibBuilder.loadTexts:fsPnacASUserConfigTable.setStatus(_A)
_FsPnacASUserConfigEntry_Object=MibTableRow
fsPnacASUserConfigEntry=_FsPnacASUserConfigEntry_Object((1,3,6,1,4,1,2076,64,3,1,1))
fsPnacASUserConfigEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:fsPnacASUserConfigEntry.setStatus(_A)
class _FsPnacASUserConfigUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,115))
_FsPnacASUserConfigUserName_Type.__name__=_M
_FsPnacASUserConfigUserName_Object=MibTableColumn
fsPnacASUserConfigUserName=_FsPnacASUserConfigUserName_Object((1,3,6,1,4,1,2076,64,3,1,1,1),_FsPnacASUserConfigUserName_Type())
fsPnacASUserConfigUserName.setMaxAccess(_G)
if mibBuilder.loadTexts:fsPnacASUserConfigUserName.setStatus(_A)
class _FsPnacASUserConfigPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_FsPnacASUserConfigPassword_Type.__name__=_F
_FsPnacASUserConfigPassword_Object=MibTableColumn
fsPnacASUserConfigPassword=_FsPnacASUserConfigPassword_Object((1,3,6,1,4,1,2076,64,3,1,1,2),_FsPnacASUserConfigPassword_Type())
fsPnacASUserConfigPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPnacASUserConfigPassword.setStatus(_A)
_FsPnacASUserConfigAuthProtocol_Type=Unsigned32
_FsPnacASUserConfigAuthProtocol_Object=MibTableColumn
fsPnacASUserConfigAuthProtocol=_FsPnacASUserConfigAuthProtocol_Object((1,3,6,1,4,1,2076,64,3,1,1,3),_FsPnacASUserConfigAuthProtocol_Type())
fsPnacASUserConfigAuthProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPnacASUserConfigAuthProtocol.setStatus(_A)
_FsPnacASUserConfigAuthTimeout_Type=Unsigned32
_FsPnacASUserConfigAuthTimeout_Object=MibTableColumn
fsPnacASUserConfigAuthTimeout=_FsPnacASUserConfigAuthTimeout_Object((1,3,6,1,4,1,2076,64,3,1,1,4),_FsPnacASUserConfigAuthTimeout_Type())
fsPnacASUserConfigAuthTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPnacASUserConfigAuthTimeout.setStatus(_A)
_FsPnacASUserConfigPortList_Type=PortList
_FsPnacASUserConfigPortList_Object=MibTableColumn
fsPnacASUserConfigPortList=_FsPnacASUserConfigPortList_Object((1,3,6,1,4,1,2076,64,3,1,1,5),_FsPnacASUserConfigPortList_Type())
fsPnacASUserConfigPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPnacASUserConfigPortList.setStatus(_A)
_FsPnacASUserConfigPermission_Type=PermissionType
_FsPnacASUserConfigPermission_Object=MibTableColumn
fsPnacASUserConfigPermission=_FsPnacASUserConfigPermission_Object((1,3,6,1,4,1,2076,64,3,1,1,6),_FsPnacASUserConfigPermission_Type())
fsPnacASUserConfigPermission.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPnacASUserConfigPermission.setStatus(_A)
_FsPnacASUserConfigRowStatus_Type=RowStatus
_FsPnacASUserConfigRowStatus_Object=MibTableColumn
fsPnacASUserConfigRowStatus=_FsPnacASUserConfigRowStatus_Object((1,3,6,1,4,1,2076,64,3,1,1,7),_FsPnacASUserConfigRowStatus_Type())
fsPnacASUserConfigRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsPnacASUserConfigRowStatus.setStatus(_A)
_FsPnacTrapObjects_ObjectIdentity=ObjectIdentity
fsPnacTrapObjects=_FsPnacTrapObjects_ObjectIdentity((1,3,6,1,4,1,2076,64,4))
_FsPnacTrapAuthSessionTable_Object=MibTable
fsPnacTrapAuthSessionTable=_FsPnacTrapAuthSessionTable_Object((1,3,6,1,4,1,2076,64,4,1))
if mibBuilder.loadTexts:fsPnacTrapAuthSessionTable.setStatus(_A)
_FsPnacTrapAuthSessionEntry_Object=MibTableRow
fsPnacTrapAuthSessionEntry=_FsPnacTrapAuthSessionEntry_Object((1,3,6,1,4,1,2076,64,4,1,1))
if mibBuilder.loadTexts:fsPnacTrapAuthSessionEntry.setStatus(_A)
class _FsPnacTrapAuthSessionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('createFailed',1),('deleteFailed',2),('entryPresent',3)))
_FsPnacTrapAuthSessionStatus_Type.__name__=_D
_FsPnacTrapAuthSessionStatus_Object=MibTableColumn
fsPnacTrapAuthSessionStatus=_FsPnacTrapAuthSessionStatus_Object((1,3,6,1,4,1,2076,64,4,1,1,1),_FsPnacTrapAuthSessionStatus_Type())
fsPnacTrapAuthSessionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPnacTrapAuthSessionStatus.setStatus(_A)
_FsPnacNotifications_ObjectIdentity=ObjectIdentity
fsPnacNotifications=_FsPnacNotifications_ObjectIdentity((1,3,6,1,4,1,2076,64,5))
_FsPnacHwFailureTrap_ObjectIdentity=ObjectIdentity
fsPnacHwFailureTrap=_FsPnacHwFailureTrap_ObjectIdentity((1,3,6,1,4,1,2076,64,5,0))
_FsDPnac_ObjectIdentity=ObjectIdentity
fsDPnac=_FsDPnac_ObjectIdentity((1,3,6,1,4,1,2076,64,6))
class _FsDPnacSystemStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('centralized',1),('distributed',2)))
_FsDPnacSystemStatus_Type.__name__=_D
_FsDPnacSystemStatus_Object=MibScalar
fsDPnacSystemStatus=_FsDPnacSystemStatus_Object((1,3,6,1,4,1,2076,64,6,1),_FsDPnacSystemStatus_Type())
fsDPnacSystemStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDPnacSystemStatus.setStatus(_A)
class _FsDPnacPeriodicSyncTime_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_FsDPnacPeriodicSyncTime_Type.__name__=_I
_FsDPnacPeriodicSyncTime_Object=MibScalar
fsDPnacPeriodicSyncTime=_FsDPnacPeriodicSyncTime_Object((1,3,6,1,4,1,2076,64,6,2),_FsDPnacPeriodicSyncTime_Type())
fsDPnacPeriodicSyncTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDPnacPeriodicSyncTime.setStatus(_A)
class _FsDPnacMaxKeepAliveCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_FsDPnacMaxKeepAliveCount_Type.__name__=_D
_FsDPnacMaxKeepAliveCount_Object=MibScalar
fsDPnacMaxKeepAliveCount=_FsDPnacMaxKeepAliveCount_Object((1,3,6,1,4,1,2076,64,6,3),_FsDPnacMaxKeepAliveCount_Type())
fsDPnacMaxKeepAliveCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDPnacMaxKeepAliveCount.setStatus(_A)
_FsDPnacStatsTable_Object=MibTable
fsDPnacStatsTable=_FsDPnacStatsTable_Object((1,3,6,1,4,1,2076,64,6,4))
if mibBuilder.loadTexts:fsDPnacStatsTable.setStatus(_A)
_FsDPnacStatsEntry_Object=MibTableRow
fsDPnacStatsEntry=_FsDPnacStatsEntry_Object((1,3,6,1,4,1,2076,64,6,4,1))
fsDPnacStatsEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:fsDPnacStatsEntry.setStatus(_A)
class _FsDPnacSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsDPnacSlotNumber_Type.__name__=_D
_FsDPnacSlotNumber_Object=MibTableColumn
fsDPnacSlotNumber=_FsDPnacSlotNumber_Object((1,3,6,1,4,1,2076,64,6,4,1,1),_FsDPnacSlotNumber_Type())
fsDPnacSlotNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:fsDPnacSlotNumber.setStatus(_A)
_FsDPnacEventUpdateFramesRx_Type=Counter32
_FsDPnacEventUpdateFramesRx_Object=MibTableColumn
fsDPnacEventUpdateFramesRx=_FsDPnacEventUpdateFramesRx_Object((1,3,6,1,4,1,2076,64,6,4,1,2),_FsDPnacEventUpdateFramesRx_Type())
fsDPnacEventUpdateFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDPnacEventUpdateFramesRx.setStatus(_A)
_FsDPnacEventUpdateFramesTx_Type=Counter32
_FsDPnacEventUpdateFramesTx_Object=MibTableColumn
fsDPnacEventUpdateFramesTx=_FsDPnacEventUpdateFramesTx_Object((1,3,6,1,4,1,2076,64,6,4,1,3),_FsDPnacEventUpdateFramesTx_Type())
fsDPnacEventUpdateFramesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDPnacEventUpdateFramesTx.setStatus(_A)
_FsDPnacPeriodicFramesTx_Type=Counter32
_FsDPnacPeriodicFramesTx_Object=MibTableColumn
fsDPnacPeriodicFramesTx=_FsDPnacPeriodicFramesTx_Object((1,3,6,1,4,1,2076,64,6,4,1,4),_FsDPnacPeriodicFramesTx_Type())
fsDPnacPeriodicFramesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDPnacPeriodicFramesTx.setStatus(_A)
_FsDPnacPeriodicFramesRx_Type=Counter32
_FsDPnacPeriodicFramesRx_Object=MibTableColumn
fsDPnacPeriodicFramesRx=_FsDPnacPeriodicFramesRx_Object((1,3,6,1,4,1,2076,64,6,4,1,5),_FsDPnacPeriodicFramesRx_Type())
fsDPnacPeriodicFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDPnacPeriodicFramesRx.setStatus(_A)
_FsDPnacSlotPortTable_Object=MibTable
fsDPnacSlotPortTable=_FsDPnacSlotPortTable_Object((1,3,6,1,4,1,2076,64,6,5))
if mibBuilder.loadTexts:fsDPnacSlotPortTable.setStatus(_A)
_FsDPnacSlotPortEntry_Object=MibTableRow
fsDPnacSlotPortEntry=_FsDPnacSlotPortEntry_Object((1,3,6,1,4,1,2076,64,6,5,1))
fsDPnacSlotPortEntry.setIndexNames((0,_E,_L),(0,_E,_V))
if mibBuilder.loadTexts:fsDPnacSlotPortEntry.setStatus(_A)
_FsDPnacPortIndex_Type=InterfaceIndex
_FsDPnacPortIndex_Object=MibTableColumn
fsDPnacPortIndex=_FsDPnacPortIndex_Object((1,3,6,1,4,1,2076,64,6,5,1,1),_FsDPnacPortIndex_Type())
fsDPnacPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsDPnacPortIndex.setStatus(_A)
_FsDPnacPortAuthStatus_Type=PaeControlledPortStatus
_FsDPnacPortAuthStatus_Object=MibTableColumn
fsDPnacPortAuthStatus=_FsDPnacPortAuthStatus_Object((1,3,6,1,4,1,2076,64,6,5,1,2),_FsDPnacPortAuthStatus_Type())
fsDPnacPortAuthStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDPnacPortAuthStatus.setStatus(_A)
class _FsDPnacPortControlledDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('both',0),('in',1)))
_FsDPnacPortControlledDirection_Type.__name__=_D
_FsDPnacPortControlledDirection_Object=MibTableColumn
fsDPnacPortControlledDirection=_FsDPnacPortControlledDirection_Object((1,3,6,1,4,1,2076,64,6,5,1,3),_FsDPnacPortControlledDirection_Type())
fsDPnacPortControlledDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDPnacPortControlledDirection.setStatus(_A)
fsPnacAuthSessionEntry.registerAugmentions((_E,_W))
fsPnacTrapAuthSessionEntry.setIndexNames(*fsPnacAuthSessionEntry.getIndexNames())
fsPnacPortBasedHwFailureTrap=NotificationType((1,3,6,1,4,1,2076,64,5,0,1))
fsPnacPortBasedHwFailureTrap.setObjects(*((_E,_X),(_N,_O)))
if mibBuilder.loadTexts:fsPnacPortBasedHwFailureTrap.setStatus(_A)
fsPnacMacBasedHwFailureTrap=NotificationType((1,3,6,1,4,1,2076,64,5,0,2))
fsPnacMacBasedHwFailureTrap.setObjects(*((_E,_Y),(_E,_Z),(_E,_a)))
if mibBuilder.loadTexts:fsPnacMacBasedHwFailureTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'AuthenticMethod':AuthenticMethod,_S:RemoteAuthServerType,'PermissionType':PermissionType,'fspnac':fspnac,'fsPnacPaeSystem':fsPnacPaeSystem,'fsPnacSystemControl':fsPnacSystemControl,'fsPnacTraceOption':fsPnacTraceOption,'fsPnacAuthenticServer':fsPnacAuthenticServer,'fsPnacNasId':fsPnacNasId,'fsPnacPaePortTable':fsPnacPaePortTable,'fsPnacPaePortEntry':fsPnacPaePortEntry,_P:fsPnacPaePortNumber,'fsPnacPaePortAuthMode':fsPnacPaePortAuthMode,'fsPnacPaePortSupplicantCount':fsPnacPaePortSupplicantCount,'fsPnacPaePortUserName':fsPnacPaePortUserName,'fsPnacPaePortPassword':fsPnacPaePortPassword,_X:fsPnacPaePortStatus,'fsPnacPaePortStatisticsClear':fsPnacPaePortStatisticsClear,'fsPnacPaePortAuthStatus':fsPnacPaePortAuthStatus,'fsPnacPaeAuthReAuthMax':fsPnacPaeAuthReAuthMax,'fsPnacModuleOperStatus':fsPnacModuleOperStatus,'fsPnacRemoteAuthServerType':fsPnacRemoteAuthServerType,'fsPnacPaeAuthenticator':fsPnacPaeAuthenticator,'fsPnacAuthSessionTable':fsPnacAuthSessionTable,'fsPnacAuthSessionEntry':fsPnacAuthSessionEntry,_K:fsPnacAuthSessionSuppAddress,'fsPnacAuthSessionIdentifier':fsPnacAuthSessionIdentifier,'fsPnacAuthSessionAuthPaeState':fsPnacAuthSessionAuthPaeState,'fsPnacAuthSessionBackendAuthState':fsPnacAuthSessionBackendAuthState,_Z:fsPnacAuthSessionPortStatus,_Y:fsPnacAuthSessionPortNumber,'fsPnacAuthSessionInitialize':fsPnacAuthSessionInitialize,'fsPnacAuthSessionReauthenticate':fsPnacAuthSessionReauthenticate,'fsPnacAuthSessionStatsTable':fsPnacAuthSessionStatsTable,'fsPnacAuthSessionStatsEntry':fsPnacAuthSessionStatsEntry,'fsPnacAuthSessionOctetsRx':fsPnacAuthSessionOctetsRx,'fsPnacAuthSessionOctetsTx':fsPnacAuthSessionOctetsTx,'fsPnacAuthSessionFramesRx':fsPnacAuthSessionFramesRx,'fsPnacAuthSessionFramesTx':fsPnacAuthSessionFramesTx,'fsPnacAuthSessionId':fsPnacAuthSessionId,'fsPnacAuthSessionAuthenticMethod':fsPnacAuthSessionAuthenticMethod,'fsPnacAuthSessionTime':fsPnacAuthSessionTime,'fsPnacAuthSessionTerminateCause':fsPnacAuthSessionTerminateCause,'fsPnacAuthSessionUserName':fsPnacAuthSessionUserName,'fsPnacAuthSessionStatisticsClear':fsPnacAuthSessionStatisticsClear,'fsPnacAuthServer':fsPnacAuthServer,'fsPnacASUserConfigTable':fsPnacASUserConfigTable,'fsPnacASUserConfigEntry':fsPnacASUserConfigEntry,_U:fsPnacASUserConfigUserName,'fsPnacASUserConfigPassword':fsPnacASUserConfigPassword,'fsPnacASUserConfigAuthProtocol':fsPnacASUserConfigAuthProtocol,'fsPnacASUserConfigAuthTimeout':fsPnacASUserConfigAuthTimeout,'fsPnacASUserConfigPortList':fsPnacASUserConfigPortList,'fsPnacASUserConfigPermission':fsPnacASUserConfigPermission,'fsPnacASUserConfigRowStatus':fsPnacASUserConfigRowStatus,'fsPnacTrapObjects':fsPnacTrapObjects,'fsPnacTrapAuthSessionTable':fsPnacTrapAuthSessionTable,_W:fsPnacTrapAuthSessionEntry,_a:fsPnacTrapAuthSessionStatus,'fsPnacNotifications':fsPnacNotifications,'fsPnacHwFailureTrap':fsPnacHwFailureTrap,'fsPnacPortBasedHwFailureTrap':fsPnacPortBasedHwFailureTrap,'fsPnacMacBasedHwFailureTrap':fsPnacMacBasedHwFailureTrap,'fsDPnac':fsDPnac,'fsDPnacSystemStatus':fsDPnacSystemStatus,'fsDPnacPeriodicSyncTime':fsDPnacPeriodicSyncTime,'fsDPnacMaxKeepAliveCount':fsDPnacMaxKeepAliveCount,'fsDPnacStatsTable':fsDPnacStatsTable,'fsDPnacStatsEntry':fsDPnacStatsEntry,_L:fsDPnacSlotNumber,'fsDPnacEventUpdateFramesRx':fsDPnacEventUpdateFramesRx,'fsDPnacEventUpdateFramesTx':fsDPnacEventUpdateFramesTx,'fsDPnacPeriodicFramesTx':fsDPnacPeriodicFramesTx,'fsDPnacPeriodicFramesRx':fsDPnacPeriodicFramesRx,'fsDPnacSlotPortTable':fsDPnacSlotPortTable,'fsDPnacSlotPortEntry':fsDPnacSlotPortEntry,_V:fsDPnacPortIndex,'fsDPnacPortAuthStatus':fsDPnacPortAuthStatus,'fsDPnacPortControlledDirection':fsDPnacPortControlledDirection})