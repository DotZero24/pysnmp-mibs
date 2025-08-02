_m='agentAuthMgrClientAuthstatus'
_l='agentAuthMgrClientAuthMethod'
_k='agentAuthMgrInterface'
_j='agentAuthMgrPortMethodIndex'
_i='agentAuthMgrAuthHistoryResultIfIndex'
_h='agentAuthMgrAuthHistoryResultIndex'
_g='agentAuthMgrAuthHistoryResultIfaceIndex'
_f='monitorVlan'
_e='voiceVlan'
_d='radius'
_c='success'
_b='mustNotSecure'
_a='mustSecure'
_Z='shouldSecure'
_Y='authorize'
_X='reinitialize'
_W='AuthMgrPortHostMode'
_V='AuthMgrPortControlMode'
_U='agentAuthMgrTimerIfIndex'
_T='read-create'
_S='default'
_R='agentAuthMgrPortIfaceIndex'
_Q='agentAuthMgrClientMacAddress'
_P='methodIndex'
_O='agentAuthMgrIfIndex'
_N='none'
_M='not-accessible'
_L='Unsigned32'
_K='undefined'
_J='captivePortal'
_I='mab'
_H='dot1x'
_G='disable'
_F='enable'
_E='DNOS-AUTHENTICATION-MANAGER-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dnOS,=mibBuilder.importSymbols('DELL-REF-MIB','dnOS')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
fastPathAuthMgr=ModuleIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61))
if mibBuilder.loadTexts:fastPathAuthMgr.setRevisions(('2020-10-08 00:00','2020-08-25 00:00','2018-12-26 00:00','2018-09-24 00:00','2018-05-15 00:00','2017-09-05 00:00','2012-12-28 00:00'))
class AuthMgrPortControlMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('forceUnauthorized',1),('auto',2),('forceAuthorized',3)))
class AuthMgrPortHostMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('singleHost',1),('multiHost',2),('multiAuth',3),('multiDomain',4),('multiDomainMultiHost',5)))
class AuthMgrSessionTerminationAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),('reauthenticate',2)))
_FastpathAuthMgrTraps_ObjectIdentity=ObjectIdentity
fastpathAuthMgrTraps=_FastpathAuthMgrTraps_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,0))
_AgentAuthMgrGlobalConfigGroup_ObjectIdentity=ObjectIdentity
agentAuthMgrGlobalConfigGroup=_AgentAuthMgrGlobalConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,1))
class _AgentAuthMgrAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentAuthMgrAdminMode_Type.__name__=_C
_AgentAuthMgrAdminMode_Object=MibScalar
agentAuthMgrAdminMode=_AgentAuthMgrAdminMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,1,1),_AgentAuthMgrAdminMode_Type())
agentAuthMgrAdminMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrAdminMode.setStatus(_A)
class _AgentAuthMgrRadiusVlanAssignment_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentAuthMgrRadiusVlanAssignment_Type.__name__=_C
_AgentAuthMgrRadiusVlanAssignment_Object=MibScalar
agentAuthMgrRadiusVlanAssignment=_AgentAuthMgrRadiusVlanAssignment_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,1,2),_AgentAuthMgrRadiusVlanAssignment_Type())
agentAuthMgrRadiusVlanAssignment.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrRadiusVlanAssignment.setStatus(_A)
class _AgentAuthMgrDynamicVlanCreationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentAuthMgrDynamicVlanCreationMode_Type.__name__=_C
_AgentAuthMgrDynamicVlanCreationMode_Object=MibScalar
agentAuthMgrDynamicVlanCreationMode=_AgentAuthMgrDynamicVlanCreationMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,1,3),_AgentAuthMgrDynamicVlanCreationMode_Type())
agentAuthMgrDynamicVlanCreationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrDynamicVlanCreationMode.setStatus(_A)
_AgentAuthMgrCriticalRecoveryMaxReauth_Type=Unsigned32
_AgentAuthMgrCriticalRecoveryMaxReauth_Object=MibScalar
agentAuthMgrCriticalRecoveryMaxReauth=_AgentAuthMgrCriticalRecoveryMaxReauth_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,1,4),_AgentAuthMgrCriticalRecoveryMaxReauth_Type())
agentAuthMgrCriticalRecoveryMaxReauth.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrCriticalRecoveryMaxReauth.setStatus(_A)
_AgentAuthMgrInterfaceConfigGroup_ObjectIdentity=ObjectIdentity
agentAuthMgrInterfaceConfigGroup=_AgentAuthMgrInterfaceConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2))
_AgentAuthMgrInterfaceConfigMethodTable_Object=MibTable
agentAuthMgrInterfaceConfigMethodTable=_AgentAuthMgrInterfaceConfigMethodTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,1))
if mibBuilder.loadTexts:agentAuthMgrInterfaceConfigMethodTable.setStatus(_A)
_AgentAuthMgrInterfaceConfigMethodEntry_Object=MibTableRow
agentAuthMgrInterfaceConfigMethodEntry=_AgentAuthMgrInterfaceConfigMethodEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,1,1))
agentAuthMgrInterfaceConfigMethodEntry.setIndexNames((0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:agentAuthMgrInterfaceConfigMethodEntry.setStatus(_A)
_AgentAuthMgrIfIndex_Type=InterfaceIndex
_AgentAuthMgrIfIndex_Object=MibTableColumn
agentAuthMgrIfIndex=_AgentAuthMgrIfIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,1,1,1),_AgentAuthMgrIfIndex_Type())
agentAuthMgrIfIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:agentAuthMgrIfIndex.setStatus(_A)
_MethodIndex_Type=Unsigned32
_MethodIndex_Object=MibTableColumn
methodIndex=_MethodIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,1,1,2),_MethodIndex_Type())
methodIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:methodIndex.setStatus(_A)
class _AgentAuthMgrMethodOrder_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),(_H,1),(_I,2),(_J,3)))
_AgentAuthMgrMethodOrder_Type.__name__=_C
_AgentAuthMgrMethodOrder_Object=MibTableColumn
agentAuthMgrMethodOrder=_AgentAuthMgrMethodOrder_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,1,1,3),_AgentAuthMgrMethodOrder_Type())
agentAuthMgrMethodOrder.setMaxAccess(_T)
if mibBuilder.loadTexts:agentAuthMgrMethodOrder.setStatus(_A)
class _AgentAuthMgrMethodPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),(_H,1),(_I,2),(_J,3)))
_AgentAuthMgrMethodPriority_Type.__name__=_C
_AgentAuthMgrMethodPriority_Object=MibTableColumn
agentAuthMgrMethodPriority=_AgentAuthMgrMethodPriority_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,1,1,4),_AgentAuthMgrMethodPriority_Type())
agentAuthMgrMethodPriority.setMaxAccess(_T)
if mibBuilder.loadTexts:agentAuthMgrMethodPriority.setStatus(_A)
_AgentAuthMgrInterfaceConfigTimerTable_Object=MibTable
agentAuthMgrInterfaceConfigTimerTable=_AgentAuthMgrInterfaceConfigTimerTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,2))
if mibBuilder.loadTexts:agentAuthMgrInterfaceConfigTimerTable.setStatus(_A)
_AgentAuthMgrInterfaceConfigTimerEntry_Object=MibTableRow
agentAuthMgrInterfaceConfigTimerEntry=_AgentAuthMgrInterfaceConfigTimerEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,2,1))
agentAuthMgrInterfaceConfigTimerEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:agentAuthMgrInterfaceConfigTimerEntry.setStatus(_A)
_AgentAuthMgrTimerIfIndex_Type=InterfaceIndex
_AgentAuthMgrTimerIfIndex_Object=MibTableColumn
agentAuthMgrTimerIfIndex=_AgentAuthMgrTimerIfIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,2,1,1),_AgentAuthMgrTimerIfIndex_Type())
agentAuthMgrTimerIfIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:agentAuthMgrTimerIfIndex.setStatus(_A)
class _AgentAuthMgrRestart_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,65535))
_AgentAuthMgrRestart_Type.__name__=_L
_AgentAuthMgrRestart_Object=MibTableColumn
agentAuthMgrRestart=_AgentAuthMgrRestart_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,2,1,2),_AgentAuthMgrRestart_Type())
agentAuthMgrRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrRestart.setStatus(_A)
if mibBuilder.loadTexts:agentAuthMgrRestart.setUnits('seconds')
_AgentAuthMgrInterfaceConfigAuthenticationTable_Object=MibTable
agentAuthMgrInterfaceConfigAuthenticationTable=_AgentAuthMgrInterfaceConfigAuthenticationTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,3))
if mibBuilder.loadTexts:agentAuthMgrInterfaceConfigAuthenticationTable.setStatus(_A)
_AgentAuthMgrInterfaceConfigAuthenticationEntry_Object=MibTableRow
agentAuthMgrInterfaceConfigAuthenticationEntry=_AgentAuthMgrInterfaceConfigAuthenticationEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,3,1))
agentAuthMgrInterfaceConfigAuthenticationEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:agentAuthMgrInterfaceConfigAuthenticationEntry.setStatus(_A)
class _AgentAuthMgrPortControlMode_Type(AuthMgrPortControlMode):defaultValue=2
_AgentAuthMgrPortControlMode_Type.__name__=_V
_AgentAuthMgrPortControlMode_Object=MibTableColumn
agentAuthMgrPortControlMode=_AgentAuthMgrPortControlMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,3,1,1),_AgentAuthMgrPortControlMode_Type())
agentAuthMgrPortControlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrPortControlMode.setStatus(_A)
class _AgentAuthMgrPortHostMode_Type(AuthMgrPortHostMode):defaultValue=2
_AgentAuthMgrPortHostMode_Type.__name__=_W
_AgentAuthMgrPortHostMode_Object=MibTableColumn
agentAuthMgrPortHostMode=_AgentAuthMgrPortHostMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,3,1,2),_AgentAuthMgrPortHostMode_Type())
agentAuthMgrPortHostMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrPortHostMode.setStatus(_A)
class _AgentAuthMgrPortNoResponseVlanId_Type(Unsigned32):defaultValue=0
_AgentAuthMgrPortNoResponseVlanId_Type.__name__=_L
_AgentAuthMgrPortNoResponseVlanId_Object=MibTableColumn
agentAuthMgrPortNoResponseVlanId=_AgentAuthMgrPortNoResponseVlanId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,3,1,3),_AgentAuthMgrPortNoResponseVlanId_Type())
agentAuthMgrPortNoResponseVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrPortNoResponseVlanId.setStatus(_A)
class _AgentAuthMgrPortAuthFailVlanId_Type(Unsigned32):defaultValue=0
_AgentAuthMgrPortAuthFailVlanId_Type.__name__=_L
_AgentAuthMgrPortAuthFailVlanId_Object=MibTableColumn
agentAuthMgrPortAuthFailVlanId=_AgentAuthMgrPortAuthFailVlanId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,3,1,4),_AgentAuthMgrPortAuthFailVlanId_Type())
agentAuthMgrPortAuthFailVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrPortAuthFailVlanId.setStatus(_A)
_AgentAuthMgrPortMaxUsers_Type=Unsigned32
_AgentAuthMgrPortMaxUsers_Object=MibTableColumn
agentAuthMgrPortMaxUsers=_AgentAuthMgrPortMaxUsers_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,3,1,5),_AgentAuthMgrPortMaxUsers_Type())
agentAuthMgrPortMaxUsers.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrPortMaxUsers.setStatus(_A)
class _AgentAuthMgrPortAuthViolationMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('protect',1),('restrict',2),('shutdown',3)))
_AgentAuthMgrPortAuthViolationMode_Type.__name__=_C
_AgentAuthMgrPortAuthViolationMode_Object=MibTableColumn
agentAuthMgrPortAuthViolationMode=_AgentAuthMgrPortAuthViolationMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,3,1,6),_AgentAuthMgrPortAuthViolationMode_Type())
agentAuthMgrPortAuthViolationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrPortAuthViolationMode.setStatus(_A)
class _AgentAuthMgrPortCriticalVlanId_Type(Unsigned32):defaultValue=0
_AgentAuthMgrPortCriticalVlanId_Type.__name__=_L
_AgentAuthMgrPortCriticalVlanId_Object=MibTableColumn
agentAuthMgrPortCriticalVlanId=_AgentAuthMgrPortCriticalVlanId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,3,1,7),_AgentAuthMgrPortCriticalVlanId_Type())
agentAuthMgrPortCriticalVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrPortCriticalVlanId.setStatus(_A)
class _AgentAuthMgrPortAuthServerDeadAction_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_X,1),(_Y,2),(_N,3)))
_AgentAuthMgrPortAuthServerDeadAction_Type.__name__=_C
_AgentAuthMgrPortAuthServerDeadAction_Object=MibTableColumn
agentAuthMgrPortAuthServerDeadAction=_AgentAuthMgrPortAuthServerDeadAction_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,3,1,8),_AgentAuthMgrPortAuthServerDeadAction_Type())
agentAuthMgrPortAuthServerDeadAction.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrPortAuthServerDeadAction.setStatus(_A)
class _AgentAuthMgrPortAuthServerAliveAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_N,2)))
_AgentAuthMgrPortAuthServerAliveAction_Type.__name__=_C
_AgentAuthMgrPortAuthServerAliveAction_Object=MibTableColumn
agentAuthMgrPortAuthServerAliveAction=_AgentAuthMgrPortAuthServerAliveAction_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,3,1,9),_AgentAuthMgrPortAuthServerAliveAction_Type())
agentAuthMgrPortAuthServerAliveAction.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrPortAuthServerAliveAction.setStatus(_A)
class _AgentAuthMgrPortAuthServerDeadVoiceAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_N,2)))
_AgentAuthMgrPortAuthServerDeadVoiceAction_Type.__name__=_C
_AgentAuthMgrPortAuthServerDeadVoiceAction_Object=MibTableColumn
agentAuthMgrPortAuthServerDeadVoiceAction=_AgentAuthMgrPortAuthServerDeadVoiceAction_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,3,1,10),_AgentAuthMgrPortAuthServerDeadVoiceAction_Type())
agentAuthMgrPortAuthServerDeadVoiceAction.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrPortAuthServerDeadVoiceAction.setStatus(_A)
_AgentAuthMgrPortInitialize_Type=TruthValue
_AgentAuthMgrPortInitialize_Object=MibTableColumn
agentAuthMgrPortInitialize=_AgentAuthMgrPortInitialize_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,3,1,11),_AgentAuthMgrPortInitialize_Type())
agentAuthMgrPortInitialize.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrPortInitialize.setStatus(_A)
class _AgentAuthMgrPortUnauthDHCPAllow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentAuthMgrPortUnauthDHCPAllow_Type.__name__=_C
_AgentAuthMgrPortUnauthDHCPAllow_Object=MibTableColumn
agentAuthMgrPortUnauthDHCPAllow=_AgentAuthMgrPortUnauthDHCPAllow_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,3,1,12),_AgentAuthMgrPortUnauthDHCPAllow_Type())
agentAuthMgrPortUnauthDHCPAllow.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrPortUnauthDHCPAllow.setStatus(_A)
class _AgentAuthMgrPortAuthenticationOpen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentAuthMgrPortAuthenticationOpen_Type.__name__=_C
_AgentAuthMgrPortAuthenticationOpen_Object=MibTableColumn
agentAuthMgrPortAuthenticationOpen=_AgentAuthMgrPortAuthenticationOpen_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,3,1,13),_AgentAuthMgrPortAuthenticationOpen_Type())
agentAuthMgrPortAuthenticationOpen.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrPortAuthenticationOpen.setStatus(_A)
class _AgentAuthMgrPortAuthControlDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('both',1),('in',2)))
_AgentAuthMgrPortAuthControlDirection_Type.__name__=_C
_AgentAuthMgrPortAuthControlDirection_Object=MibTableColumn
agentAuthMgrPortAuthControlDirection=_AgentAuthMgrPortAuthControlDirection_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,3,1,14),_AgentAuthMgrPortAuthControlDirection_Type())
agentAuthMgrPortAuthControlDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrPortAuthControlDirection.setStatus(_A)
class _AgentAuthMgrPortLinkSecPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Z,1),(_a,2),(_b,3)))
_AgentAuthMgrPortLinkSecPolicy_Type.__name__=_C
_AgentAuthMgrPortLinkSecPolicy_Object=MibTableColumn
agentAuthMgrPortLinkSecPolicy=_AgentAuthMgrPortLinkSecPolicy_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,2,3,1,15),_AgentAuthMgrPortLinkSecPolicy_Type())
agentAuthMgrPortLinkSecPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrPortLinkSecPolicy.setStatus(_A)
_AgentAuthMgrInterfaceStatusGroup_ObjectIdentity=ObjectIdentity
agentAuthMgrInterfaceStatusGroup=_AgentAuthMgrInterfaceStatusGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,3))
_AgentAuthMgrInterfaceStatusTable_Object=MibTable
agentAuthMgrInterfaceStatusTable=_AgentAuthMgrInterfaceStatusTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,3,1))
if mibBuilder.loadTexts:agentAuthMgrInterfaceStatusTable.setStatus(_A)
_AgentAuthMgrInterfaceStatusEntry_Object=MibTableRow
agentAuthMgrInterfaceStatusEntry=_AgentAuthMgrInterfaceStatusEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,3,1,1))
agentAuthMgrInterfaceStatusEntry.setIndexNames((0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:agentAuthMgrInterfaceStatusEntry.setStatus(_A)
class _AgentAuthMgrStatusMethodOrder_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),(_H,1),(_I,2),(_J,3)))
_AgentAuthMgrStatusMethodOrder_Type.__name__=_C
_AgentAuthMgrStatusMethodOrder_Object=MibTableColumn
agentAuthMgrStatusMethodOrder=_AgentAuthMgrStatusMethodOrder_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,3,1,1,1),_AgentAuthMgrStatusMethodOrder_Type())
agentAuthMgrStatusMethodOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrStatusMethodOrder.setStatus(_A)
class _AgentAuthMgrStatusMethodPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),(_H,1),(_I,2),(_J,3)))
_AgentAuthMgrStatusMethodPriority_Type.__name__=_C
_AgentAuthMgrStatusMethodPriority_Object=MibTableColumn
agentAuthMgrStatusMethodPriority=_AgentAuthMgrStatusMethodPriority_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,3,1,1,2),_AgentAuthMgrStatusMethodPriority_Type())
agentAuthMgrStatusMethodPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrStatusMethodPriority.setStatus(_A)
_AgentAuthMgrClientStatusGroup_ObjectIdentity=ObjectIdentity
agentAuthMgrClientStatusGroup=_AgentAuthMgrClientStatusGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,4))
_AgentAuthMgrClientStatusTable_Object=MibTable
agentAuthMgrClientStatusTable=_AgentAuthMgrClientStatusTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,4,1))
if mibBuilder.loadTexts:agentAuthMgrClientStatusTable.setStatus(_A)
_AgentAuthMgrClientStatusEntry_Object=MibTableRow
agentAuthMgrClientStatusEntry=_AgentAuthMgrClientStatusEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,4,1,1))
agentAuthMgrClientStatusEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:agentAuthMgrClientStatusEntry.setStatus(_A)
_AgentAuthMgrClientMacAddress_Type=MacAddress
_AgentAuthMgrClientMacAddress_Object=MibTableColumn
agentAuthMgrClientMacAddress=_AgentAuthMgrClientMacAddress_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,4,1,1,1),_AgentAuthMgrClientMacAddress_Type())
agentAuthMgrClientMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrClientMacAddress.setStatus(_A)
_AgentAuthMgrLogicalPort_Type=Unsigned32
_AgentAuthMgrLogicalPort_Object=MibTableColumn
agentAuthMgrLogicalPort=_AgentAuthMgrLogicalPort_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,4,1,1,2),_AgentAuthMgrLogicalPort_Type())
agentAuthMgrLogicalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrLogicalPort.setStatus(_A)
_AgentAuthMgrInterface_Type=Unsigned32
_AgentAuthMgrInterface_Object=MibTableColumn
agentAuthMgrInterface=_AgentAuthMgrInterface_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,4,1,1,3),_AgentAuthMgrInterface_Type())
agentAuthMgrInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrInterface.setStatus(_A)
class _AgentAuthMgrClientAuthstatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('authorized',1),('unauthorized',2)))
_AgentAuthMgrClientAuthstatus_Type.__name__=_C
_AgentAuthMgrClientAuthstatus_Object=MibTableColumn
agentAuthMgrClientAuthstatus=_AgentAuthMgrClientAuthstatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,4,1,1,4),_AgentAuthMgrClientAuthstatus_Type())
agentAuthMgrClientAuthstatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrClientAuthstatus.setStatus(_A)
class _AgentAuthMgrClientAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),(_H,1),(_I,2),(_J,3)))
_AgentAuthMgrClientAuthMethod_Type.__name__=_C
_AgentAuthMgrClientAuthMethod_Object=MibTableColumn
agentAuthMgrClientAuthMethod=_AgentAuthMgrClientAuthMethod_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,4,1,1,5),_AgentAuthMgrClientAuthMethod_Type())
agentAuthMgrClientAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrClientAuthMethod.setStatus(_A)
class _AgentAuthMgrClientAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),('failed',2),('running',3)))
_AgentAuthMgrClientAuthState_Type.__name__=_C
_AgentAuthMgrClientAuthState_Object=MibTableColumn
agentAuthMgrClientAuthState=_AgentAuthMgrClientAuthState_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,4,1,1,6),_AgentAuthMgrClientAuthState_Type())
agentAuthMgrClientAuthState.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrClientAuthState.setStatus(_A)
_AgentAuthMgrClientUserName_Type=DisplayString
_AgentAuthMgrClientUserName_Object=MibTableColumn
agentAuthMgrClientUserName=_AgentAuthMgrClientUserName_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,4,1,1,7),_AgentAuthMgrClientUserName_Type())
agentAuthMgrClientUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrClientUserName.setStatus(_A)
_AgentAuthMgrClientVlanAssigned_Type=Unsigned32
_AgentAuthMgrClientVlanAssigned_Object=MibTableColumn
agentAuthMgrClientVlanAssigned=_AgentAuthMgrClientVlanAssigned_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,4,1,1,8),_AgentAuthMgrClientVlanAssigned_Type())
agentAuthMgrClientVlanAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrClientVlanAssigned.setStatus(_A)
class _AgentAuthMgrClientAuthVlanAssignedReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_d,1),('authFailVlan',2),('noResponseVlan',3),(_e,4),(_f,5),('criticalVlan',6),(_N,7)))
_AgentAuthMgrClientAuthVlanAssignedReason_Type.__name__=_C
_AgentAuthMgrClientAuthVlanAssignedReason_Object=MibTableColumn
agentAuthMgrClientAuthVlanAssignedReason=_AgentAuthMgrClientAuthVlanAssignedReason_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,4,1,1,9),_AgentAuthMgrClientAuthVlanAssignedReason_Type())
agentAuthMgrClientAuthVlanAssignedReason.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrClientAuthVlanAssignedReason.setStatus(_A)
_AgentAuthMgrClientSessionTime_Type=Unsigned32
_AgentAuthMgrClientSessionTime_Object=MibTableColumn
agentAuthMgrClientSessionTime=_AgentAuthMgrClientSessionTime_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,4,1,1,10),_AgentAuthMgrClientSessionTime_Type())
agentAuthMgrClientSessionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrClientSessionTime.setStatus(_A)
_AgentAuthMgrClientFilterID_Type=DisplayString
_AgentAuthMgrClientFilterID_Object=MibTableColumn
agentAuthMgrClientFilterID=_AgentAuthMgrClientFilterID_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,4,1,1,11),_AgentAuthMgrClientFilterID_Type())
agentAuthMgrClientFilterID.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrClientFilterID.setStatus(_A)
_AgentAuthMgrClientDACL_Type=DisplayString
_AgentAuthMgrClientDACL_Object=MibTableColumn
agentAuthMgrClientDACL=_AgentAuthMgrClientDACL_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,4,1,1,12),_AgentAuthMgrClientDACL_Type())
agentAuthMgrClientDACL.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrClientDACL.setStatus(_A)
_AgentAuthMgrClientSessionTimeout_Type=Unsigned32
_AgentAuthMgrClientSessionTimeout_Object=MibTableColumn
agentAuthMgrClientSessionTimeout=_AgentAuthMgrClientSessionTimeout_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,4,1,1,13),_AgentAuthMgrClientSessionTimeout_Type())
agentAuthMgrClientSessionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrClientSessionTimeout.setStatus(_A)
_AgentAuthMgrClientTerminationAction_Type=AuthMgrSessionTerminationAction
_AgentAuthMgrClientTerminationAction_Object=MibTableColumn
agentAuthMgrClientTerminationAction=_AgentAuthMgrClientTerminationAction_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,4,1,1,14),_AgentAuthMgrClientTerminationAction_Type())
agentAuthMgrClientTerminationAction.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrClientTerminationAction.setStatus(_A)
_AgentAuthMgrClientAcctSessionId_Type=DisplayString
_AgentAuthMgrClientAcctSessionId_Object=MibTableColumn
agentAuthMgrClientAcctSessionId=_AgentAuthMgrClientAcctSessionId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,4,1,1,15),_AgentAuthMgrClientAcctSessionId_Type())
agentAuthMgrClientAcctSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrClientAcctSessionId.setStatus(_A)
_AgentAuthMgrClientRedirectACL_Type=DisplayString
_AgentAuthMgrClientRedirectACL_Object=MibTableColumn
agentAuthMgrClientRedirectACL=_AgentAuthMgrClientRedirectACL_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,4,1,1,16),_AgentAuthMgrClientRedirectACL_Type())
agentAuthMgrClientRedirectACL.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrClientRedirectACL.setStatus(_A)
_AgentAuthMgrClientRedirectURL_Type=DisplayString
_AgentAuthMgrClientRedirectURL_Object=MibTableColumn
agentAuthMgrClientRedirectURL=_AgentAuthMgrClientRedirectURL_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,4,1,1,17),_AgentAuthMgrClientRedirectURL_Type())
agentAuthMgrClientRedirectURL.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrClientRedirectURL.setStatus(_A)
class _AgentAuthMgrClientLinkSecPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Z,1),(_a,2),(_b,3)))
_AgentAuthMgrClientLinkSecPolicy_Type.__name__=_C
_AgentAuthMgrClientLinkSecPolicy_Object=MibTableColumn
agentAuthMgrClientLinkSecPolicy=_AgentAuthMgrClientLinkSecPolicy_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,4,1,1,18),_AgentAuthMgrClientLinkSecPolicy_Type())
agentAuthMgrClientLinkSecPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrClientLinkSecPolicy.setStatus(_A)
_AgentAuthMgrClientSessionTimeLeft_Type=Unsigned32
_AgentAuthMgrClientSessionTimeLeft_Object=MibTableColumn
agentAuthMgrClientSessionTimeLeft=_AgentAuthMgrClientSessionTimeLeft_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,4,1,1,19),_AgentAuthMgrClientSessionTimeLeft_Type())
agentAuthMgrClientSessionTimeLeft.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrClientSessionTimeLeft.setStatus(_A)
_AgentAuthMgrAuthHistoryResultsGroup_ObjectIdentity=ObjectIdentity
agentAuthMgrAuthHistoryResultsGroup=_AgentAuthMgrAuthHistoryResultsGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,5))
_AgentAuthMgrPortAuthHistoryResultTable_Object=MibTable
agentAuthMgrPortAuthHistoryResultTable=_AgentAuthMgrPortAuthHistoryResultTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,5,1))
if mibBuilder.loadTexts:agentAuthMgrPortAuthHistoryResultTable.setStatus(_A)
_AgentAuthMgrPortAuthHistoryResultEntry_Object=MibTableRow
agentAuthMgrPortAuthHistoryResultEntry=_AgentAuthMgrPortAuthHistoryResultEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,5,1,1))
agentAuthMgrPortAuthHistoryResultEntry.setIndexNames((0,_E,_g),(0,_E,_h))
if mibBuilder.loadTexts:agentAuthMgrPortAuthHistoryResultEntry.setStatus(_A)
_AgentAuthMgrAuthHistoryResultIfaceIndex_Type=Unsigned32
_AgentAuthMgrAuthHistoryResultIfaceIndex_Object=MibTableColumn
agentAuthMgrAuthHistoryResultIfaceIndex=_AgentAuthMgrAuthHistoryResultIfaceIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,5,1,1,1),_AgentAuthMgrAuthHistoryResultIfaceIndex_Type())
agentAuthMgrAuthHistoryResultIfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrAuthHistoryResultIfaceIndex.setStatus(_A)
_AgentAuthMgrAuthHistoryResultIndex_Type=Unsigned32
_AgentAuthMgrAuthHistoryResultIndex_Object=MibTableColumn
agentAuthMgrAuthHistoryResultIndex=_AgentAuthMgrAuthHistoryResultIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,5,1,1,2),_AgentAuthMgrAuthHistoryResultIndex_Type())
agentAuthMgrAuthHistoryResultIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrAuthHistoryResultIndex.setStatus(_A)
_AgentAuthMgrAuthHistoryResultTimeStamp_Type=DateAndTime
_AgentAuthMgrAuthHistoryResultTimeStamp_Object=MibTableColumn
agentAuthMgrAuthHistoryResultTimeStamp=_AgentAuthMgrAuthHistoryResultTimeStamp_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,5,1,1,3),_AgentAuthMgrAuthHistoryResultTimeStamp_Type())
agentAuthMgrAuthHistoryResultTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrAuthHistoryResultTimeStamp.setStatus(_A)
_AgentAuthMgrAuthHistoryResultMacAddress_Type=MacAddress
_AgentAuthMgrAuthHistoryResultMacAddress_Object=MibTableColumn
agentAuthMgrAuthHistoryResultMacAddress=_AgentAuthMgrAuthHistoryResultMacAddress_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,5,1,1,4),_AgentAuthMgrAuthHistoryResultMacAddress_Type())
agentAuthMgrAuthHistoryResultMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrAuthHistoryResultMacAddress.setStatus(_A)
class _AgentAuthMgrAuthHistoryResultAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),(_H,1),(_I,2),(_J,3)))
_AgentAuthMgrAuthHistoryResultAuthMethod_Type.__name__=_C
_AgentAuthMgrAuthHistoryResultAuthMethod_Object=MibTableColumn
agentAuthMgrAuthHistoryResultAuthMethod=_AgentAuthMgrAuthHistoryResultAuthMethod_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,5,1,1,5),_AgentAuthMgrAuthHistoryResultAuthMethod_Type())
agentAuthMgrAuthHistoryResultAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrAuthHistoryResultAuthMethod.setStatus(_A)
class _AgentAuthMgrAuthHistoryResultAuthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),('failure',2)))
_AgentAuthMgrAuthHistoryResultAuthStatus_Type.__name__=_C
_AgentAuthMgrAuthHistoryResultAuthStatus_Object=MibTableColumn
agentAuthMgrAuthHistoryResultAuthStatus=_AgentAuthMgrAuthHistoryResultAuthStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,5,1,1,6),_AgentAuthMgrAuthHistoryResultAuthStatus_Type())
agentAuthMgrAuthHistoryResultAuthStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrAuthHistoryResultAuthStatus.setStatus(_A)
_AgentAuthMgrAuthHistoryResultAge_Type=TimeTicks
_AgentAuthMgrAuthHistoryResultAge_Object=MibTableColumn
agentAuthMgrAuthHistoryResultAge=_AgentAuthMgrAuthHistoryResultAge_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,5,1,1,7),_AgentAuthMgrAuthHistoryResultAge_Type())
agentAuthMgrAuthHistoryResultAge.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrAuthHistoryResultAge.setStatus(_A)
_AgentAuthMgrAuthHistoryResultVlanId_Type=Unsigned32
_AgentAuthMgrAuthHistoryResultVlanId_Object=MibTableColumn
agentAuthMgrAuthHistoryResultVlanId=_AgentAuthMgrAuthHistoryResultVlanId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,5,1,1,8),_AgentAuthMgrAuthHistoryResultVlanId_Type())
agentAuthMgrAuthHistoryResultVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrAuthHistoryResultVlanId.setStatus(_A)
class _AgentAuthMgrAuthHistoryResultAccessStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('granted',1),('denied',2)))
_AgentAuthMgrAuthHistoryResultAccessStatus_Type.__name__=_C
_AgentAuthMgrAuthHistoryResultAccessStatus_Object=MibTableColumn
agentAuthMgrAuthHistoryResultAccessStatus=_AgentAuthMgrAuthHistoryResultAccessStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,5,1,1,9),_AgentAuthMgrAuthHistoryResultAccessStatus_Type())
agentAuthMgrAuthHistoryResultAccessStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrAuthHistoryResultAccessStatus.setStatus(_A)
_AgentAuthMgrAuthHistoryResultFilterID_Type=DisplayString
_AgentAuthMgrAuthHistoryResultFilterID_Object=MibTableColumn
agentAuthMgrAuthHistoryResultFilterID=_AgentAuthMgrAuthHistoryResultFilterID_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,5,1,1,10),_AgentAuthMgrAuthHistoryResultFilterID_Type())
agentAuthMgrAuthHistoryResultFilterID.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrAuthHistoryResultFilterID.setStatus(_A)
_AgentAuthMgrAuthHistoryResultDACL_Type=DisplayString
_AgentAuthMgrAuthHistoryResultDACL_Object=MibTableColumn
agentAuthMgrAuthHistoryResultDACL=_AgentAuthMgrAuthHistoryResultDACL_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,5,1,1,11),_AgentAuthMgrAuthHistoryResultDACL_Type())
agentAuthMgrAuthHistoryResultDACL.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrAuthHistoryResultDACL.setStatus(_A)
class _AgentAuthMgrAuthHistoryResultVlanAssignedType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_S,1),(_d,2),('unauthenticatedVlan',3),('guestVlan',4),(_e,5),(_f,6),('notAssigned',7)))
_AgentAuthMgrAuthHistoryResultVlanAssignedType_Type.__name__=_C
_AgentAuthMgrAuthHistoryResultVlanAssignedType_Object=MibTableColumn
agentAuthMgrAuthHistoryResultVlanAssignedType=_AgentAuthMgrAuthHistoryResultVlanAssignedType_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,5,1,1,12),_AgentAuthMgrAuthHistoryResultVlanAssignedType_Type())
agentAuthMgrAuthHistoryResultVlanAssignedType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrAuthHistoryResultVlanAssignedType.setStatus(_A)
class _AgentAuthMgrAuthHistoryResultReasonCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39)));namedValues=NamedValues(*((_N,0),('supplicant-timeout',1),('eapol-timeout',2),('radius-request-timeout',3),('radius-auth-failure',4),('radius-auth-comm-failure',5),('radius-challenge-process-invalid-nas-port',6),('radius-challenge-process-wrong-eap-msg',7),('radius-request-send-msg-error',8),('radius-accept-process-invalid-nas-port',9),('radius-accept-process-wrong-eap-msg',10),('radius-accept-filter-assignment-failure',11),('radius-accept-diffserv-not-present',12),('radius-accept-vlan-assignment-failure',13),('vlan-assignment-feature-not-enabled',14),('radius-success',15),('local-auth-user-not-found',16),('local-auth-user-no-access',17),('local-auth-md5-validation-failure',18),('local-auth-invalid-eap-type',19),('local-failure',20),('local-success',21),('radius-invalid-radius-status',22),('guest-vlan-timer-expiry',23),('undefined-auth-method',24),('reject-auth-method',25),('invalid-auth-method',26),('auth-method-not-configured',27),('unauth-vlan-not-created',28),('guest-vlan-not-created',29),('radius-accept-invalid-vlan-failure',30),('eapol-request-id-timeout',31),('all-radius-servers-dead',32),('client-disconnected',33),('guest-vlan-success',34),('unauth-vlan-success',35),('critical-vlan-success',36),('monitor-success',37),('dacl-apply-failure',38),('open-success',39)))
_AgentAuthMgrAuthHistoryResultReasonCode_Type.__name__=_C
_AgentAuthMgrAuthHistoryResultReasonCode_Object=MibTableColumn
agentAuthMgrAuthHistoryResultReasonCode=_AgentAuthMgrAuthHistoryResultReasonCode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,5,1,1,13),_AgentAuthMgrAuthHistoryResultReasonCode_Type())
agentAuthMgrAuthHistoryResultReasonCode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrAuthHistoryResultReasonCode.setStatus(_A)
_AgentAuthMgrPortAuthHistoryResultClearTable_Object=MibTable
agentAuthMgrPortAuthHistoryResultClearTable=_AgentAuthMgrPortAuthHistoryResultClearTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,5,3))
if mibBuilder.loadTexts:agentAuthMgrPortAuthHistoryResultClearTable.setStatus(_A)
_AgentAuthMgrPortAuthHistoryResultClearEntry_Object=MibTableRow
agentAuthMgrPortAuthHistoryResultClearEntry=_AgentAuthMgrPortAuthHistoryResultClearEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,5,3,1))
agentAuthMgrPortAuthHistoryResultClearEntry.setIndexNames((0,_E,_i))
if mibBuilder.loadTexts:agentAuthMgrPortAuthHistoryResultClearEntry.setStatus(_A)
_AgentAuthMgrAuthHistoryResultIfIndex_Type=Unsigned32
_AgentAuthMgrAuthHistoryResultIfIndex_Object=MibTableColumn
agentAuthMgrAuthHistoryResultIfIndex=_AgentAuthMgrAuthHistoryResultIfIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,5,3,1,1),_AgentAuthMgrAuthHistoryResultIfIndex_Type())
agentAuthMgrAuthHistoryResultIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrAuthHistoryResultIfIndex.setStatus(_A)
class _AgentAuthMgrPortAuthHistoryResultsClear_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentAuthMgrPortAuthHistoryResultsClear_Type.__name__=_C
_AgentAuthMgrPortAuthHistoryResultsClear_Object=MibTableColumn
agentAuthMgrPortAuthHistoryResultsClear=_AgentAuthMgrPortAuthHistoryResultsClear_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,5,3,1,2),_AgentAuthMgrPortAuthHistoryResultsClear_Type())
agentAuthMgrPortAuthHistoryResultsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrPortAuthHistoryResultsClear.setStatus(_A)
_AgentAuthMgrAuthStatsGroup_ObjectIdentity=ObjectIdentity
agentAuthMgrAuthStatsGroup=_AgentAuthMgrAuthStatsGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,6))
_AgentAuthMgrPortStatsTable_Object=MibTable
agentAuthMgrPortStatsTable=_AgentAuthMgrPortStatsTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,6,1))
if mibBuilder.loadTexts:agentAuthMgrPortStatsTable.setStatus(_A)
_AgentAuthMgrPortStatsEntry_Object=MibTableRow
agentAuthMgrPortStatsEntry=_AgentAuthMgrPortStatsEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,6,1,1))
agentAuthMgrPortStatsEntry.setIndexNames((0,_E,_R),(0,_E,_j))
if mibBuilder.loadTexts:agentAuthMgrPortStatsEntry.setStatus(_A)
_AgentAuthMgrPortIfaceIndex_Type=Unsigned32
_AgentAuthMgrPortIfaceIndex_Object=MibTableColumn
agentAuthMgrPortIfaceIndex=_AgentAuthMgrPortIfaceIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,6,1,1,1),_AgentAuthMgrPortIfaceIndex_Type())
agentAuthMgrPortIfaceIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:agentAuthMgrPortIfaceIndex.setStatus(_A)
class _AgentAuthMgrPortMethodIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3)))
_AgentAuthMgrPortMethodIndex_Type.__name__=_C
_AgentAuthMgrPortMethodIndex_Object=MibTableColumn
agentAuthMgrPortMethodIndex=_AgentAuthMgrPortMethodIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,6,1,1,2),_AgentAuthMgrPortMethodIndex_Type())
agentAuthMgrPortMethodIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:agentAuthMgrPortMethodIndex.setStatus(_A)
_AgentAuthMgrPortStatsAttempts_Type=Unsigned32
_AgentAuthMgrPortStatsAttempts_Object=MibTableColumn
agentAuthMgrPortStatsAttempts=_AgentAuthMgrPortStatsAttempts_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,6,1,1,3),_AgentAuthMgrPortStatsAttempts_Type())
agentAuthMgrPortStatsAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrPortStatsAttempts.setStatus(_A)
_AgentAuthMgrPortStatsFailedAttempts_Type=Unsigned32
_AgentAuthMgrPortStatsFailedAttempts_Object=MibTableColumn
agentAuthMgrPortStatsFailedAttempts=_AgentAuthMgrPortStatsFailedAttempts_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,6,1,1,4),_AgentAuthMgrPortStatsFailedAttempts_Type())
agentAuthMgrPortStatsFailedAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrPortStatsFailedAttempts.setStatus(_A)
_AgentAuthMgrPortStatsClearTable_Object=MibTable
agentAuthMgrPortStatsClearTable=_AgentAuthMgrPortStatsClearTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,6,2))
if mibBuilder.loadTexts:agentAuthMgrPortStatsClearTable.setStatus(_A)
_AgentAuthMgrPortStatsClearEntry_Object=MibTableRow
agentAuthMgrPortStatsClearEntry=_AgentAuthMgrPortStatsClearEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,6,2,1))
agentAuthMgrPortStatsClearEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:agentAuthMgrPortStatsClearEntry.setStatus(_A)
class _AgentAuthMgrPortStatsClear_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentAuthMgrPortStatsClear_Type.__name__=_C
_AgentAuthMgrPortStatsClear_Object=MibTableColumn
agentAuthMgrPortStatsClear=_AgentAuthMgrPortStatsClear_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,6,2,1,2),_AgentAuthMgrPortStatsClear_Type())
agentAuthMgrPortStatsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrPortStatsClear.setStatus(_A)
_AgentAuthMgrTrapsConfigGroup_ObjectIdentity=ObjectIdentity
agentAuthMgrTrapsConfigGroup=_AgentAuthMgrTrapsConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,7))
class _AuthMgrTrapMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AuthMgrTrapMode_Type.__name__=_C
_AuthMgrTrapMode_Object=MibScalar
authMgrTrapMode=_AuthMgrTrapMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,7,1),_AuthMgrTrapMode_Type())
authMgrTrapMode.setMaxAccess(_D)
if mibBuilder.loadTexts:authMgrTrapMode.setStatus(_A)
_AgentAuthMgrMonitorModeConfigGroup_ObjectIdentity=ObjectIdentity
agentAuthMgrMonitorModeConfigGroup=_AgentAuthMgrMonitorModeConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,8))
class _AgentAuthMgrMonitorModeEnabled_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentAuthMgrMonitorModeEnabled_Type.__name__=_C
_AgentAuthMgrMonitorModeEnabled_Object=MibScalar
agentAuthMgrMonitorModeEnabled=_AgentAuthMgrMonitorModeEnabled_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,8,1),_AgentAuthMgrMonitorModeEnabled_Type())
agentAuthMgrMonitorModeEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAuthMgrMonitorModeEnabled.setStatus(_A)
_AgentAuthMgrMonitorModeClients_Type=Unsigned32
_AgentAuthMgrMonitorModeClients_Object=MibScalar
agentAuthMgrMonitorModeClients=_AgentAuthMgrMonitorModeClients_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,8,2),_AgentAuthMgrMonitorModeClients_Type())
agentAuthMgrMonitorModeClients.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrMonitorModeClients.setStatus(_A)
_AgentAuthMgrNonMonitorModeClients_Type=Unsigned32
_AgentAuthMgrNonMonitorModeClients_Object=MibScalar
agentAuthMgrNonMonitorModeClients=_AgentAuthMgrNonMonitorModeClients_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,8,3),_AgentAuthMgrNonMonitorModeClients_Type())
agentAuthMgrNonMonitorModeClients.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAuthMgrNonMonitorModeClients.setStatus(_A)
agentAuthMgrClientAuthStatusTrap=NotificationType((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,61,0,1))
agentAuthMgrClientAuthStatusTrap.setObjects(*((_E,_k),(_E,_Q),(_E,_l),(_E,_m)))
if mibBuilder.loadTexts:agentAuthMgrClientAuthStatusTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_V:AuthMgrPortControlMode,_W:AuthMgrPortHostMode,'AuthMgrSessionTerminationAction':AuthMgrSessionTerminationAction,'fastPathAuthMgr':fastPathAuthMgr,'fastpathAuthMgrTraps':fastpathAuthMgrTraps,'agentAuthMgrClientAuthStatusTrap':agentAuthMgrClientAuthStatusTrap,'agentAuthMgrGlobalConfigGroup':agentAuthMgrGlobalConfigGroup,'agentAuthMgrAdminMode':agentAuthMgrAdminMode,'agentAuthMgrRadiusVlanAssignment':agentAuthMgrRadiusVlanAssignment,'agentAuthMgrDynamicVlanCreationMode':agentAuthMgrDynamicVlanCreationMode,'agentAuthMgrCriticalRecoveryMaxReauth':agentAuthMgrCriticalRecoveryMaxReauth,'agentAuthMgrInterfaceConfigGroup':agentAuthMgrInterfaceConfigGroup,'agentAuthMgrInterfaceConfigMethodTable':agentAuthMgrInterfaceConfigMethodTable,'agentAuthMgrInterfaceConfigMethodEntry':agentAuthMgrInterfaceConfigMethodEntry,_O:agentAuthMgrIfIndex,_P:methodIndex,'agentAuthMgrMethodOrder':agentAuthMgrMethodOrder,'agentAuthMgrMethodPriority':agentAuthMgrMethodPriority,'agentAuthMgrInterfaceConfigTimerTable':agentAuthMgrInterfaceConfigTimerTable,'agentAuthMgrInterfaceConfigTimerEntry':agentAuthMgrInterfaceConfigTimerEntry,_U:agentAuthMgrTimerIfIndex,'agentAuthMgrRestart':agentAuthMgrRestart,'agentAuthMgrInterfaceConfigAuthenticationTable':agentAuthMgrInterfaceConfigAuthenticationTable,'agentAuthMgrInterfaceConfigAuthenticationEntry':agentAuthMgrInterfaceConfigAuthenticationEntry,'agentAuthMgrPortControlMode':agentAuthMgrPortControlMode,'agentAuthMgrPortHostMode':agentAuthMgrPortHostMode,'agentAuthMgrPortNoResponseVlanId':agentAuthMgrPortNoResponseVlanId,'agentAuthMgrPortAuthFailVlanId':agentAuthMgrPortAuthFailVlanId,'agentAuthMgrPortMaxUsers':agentAuthMgrPortMaxUsers,'agentAuthMgrPortAuthViolationMode':agentAuthMgrPortAuthViolationMode,'agentAuthMgrPortCriticalVlanId':agentAuthMgrPortCriticalVlanId,'agentAuthMgrPortAuthServerDeadAction':agentAuthMgrPortAuthServerDeadAction,'agentAuthMgrPortAuthServerAliveAction':agentAuthMgrPortAuthServerAliveAction,'agentAuthMgrPortAuthServerDeadVoiceAction':agentAuthMgrPortAuthServerDeadVoiceAction,'agentAuthMgrPortInitialize':agentAuthMgrPortInitialize,'agentAuthMgrPortUnauthDHCPAllow':agentAuthMgrPortUnauthDHCPAllow,'agentAuthMgrPortAuthenticationOpen':agentAuthMgrPortAuthenticationOpen,'agentAuthMgrPortAuthControlDirection':agentAuthMgrPortAuthControlDirection,'agentAuthMgrPortLinkSecPolicy':agentAuthMgrPortLinkSecPolicy,'agentAuthMgrInterfaceStatusGroup':agentAuthMgrInterfaceStatusGroup,'agentAuthMgrInterfaceStatusTable':agentAuthMgrInterfaceStatusTable,'agentAuthMgrInterfaceStatusEntry':agentAuthMgrInterfaceStatusEntry,'agentAuthMgrStatusMethodOrder':agentAuthMgrStatusMethodOrder,'agentAuthMgrStatusMethodPriority':agentAuthMgrStatusMethodPriority,'agentAuthMgrClientStatusGroup':agentAuthMgrClientStatusGroup,'agentAuthMgrClientStatusTable':agentAuthMgrClientStatusTable,'agentAuthMgrClientStatusEntry':agentAuthMgrClientStatusEntry,_Q:agentAuthMgrClientMacAddress,'agentAuthMgrLogicalPort':agentAuthMgrLogicalPort,_k:agentAuthMgrInterface,_m:agentAuthMgrClientAuthstatus,_l:agentAuthMgrClientAuthMethod,'agentAuthMgrClientAuthState':agentAuthMgrClientAuthState,'agentAuthMgrClientUserName':agentAuthMgrClientUserName,'agentAuthMgrClientVlanAssigned':agentAuthMgrClientVlanAssigned,'agentAuthMgrClientAuthVlanAssignedReason':agentAuthMgrClientAuthVlanAssignedReason,'agentAuthMgrClientSessionTime':agentAuthMgrClientSessionTime,'agentAuthMgrClientFilterID':agentAuthMgrClientFilterID,'agentAuthMgrClientDACL':agentAuthMgrClientDACL,'agentAuthMgrClientSessionTimeout':agentAuthMgrClientSessionTimeout,'agentAuthMgrClientTerminationAction':agentAuthMgrClientTerminationAction,'agentAuthMgrClientAcctSessionId':agentAuthMgrClientAcctSessionId,'agentAuthMgrClientRedirectACL':agentAuthMgrClientRedirectACL,'agentAuthMgrClientRedirectURL':agentAuthMgrClientRedirectURL,'agentAuthMgrClientLinkSecPolicy':agentAuthMgrClientLinkSecPolicy,'agentAuthMgrClientSessionTimeLeft':agentAuthMgrClientSessionTimeLeft,'agentAuthMgrAuthHistoryResultsGroup':agentAuthMgrAuthHistoryResultsGroup,'agentAuthMgrPortAuthHistoryResultTable':agentAuthMgrPortAuthHistoryResultTable,'agentAuthMgrPortAuthHistoryResultEntry':agentAuthMgrPortAuthHistoryResultEntry,_g:agentAuthMgrAuthHistoryResultIfaceIndex,_h:agentAuthMgrAuthHistoryResultIndex,'agentAuthMgrAuthHistoryResultTimeStamp':agentAuthMgrAuthHistoryResultTimeStamp,'agentAuthMgrAuthHistoryResultMacAddress':agentAuthMgrAuthHistoryResultMacAddress,'agentAuthMgrAuthHistoryResultAuthMethod':agentAuthMgrAuthHistoryResultAuthMethod,'agentAuthMgrAuthHistoryResultAuthStatus':agentAuthMgrAuthHistoryResultAuthStatus,'agentAuthMgrAuthHistoryResultAge':agentAuthMgrAuthHistoryResultAge,'agentAuthMgrAuthHistoryResultVlanId':agentAuthMgrAuthHistoryResultVlanId,'agentAuthMgrAuthHistoryResultAccessStatus':agentAuthMgrAuthHistoryResultAccessStatus,'agentAuthMgrAuthHistoryResultFilterID':agentAuthMgrAuthHistoryResultFilterID,'agentAuthMgrAuthHistoryResultDACL':agentAuthMgrAuthHistoryResultDACL,'agentAuthMgrAuthHistoryResultVlanAssignedType':agentAuthMgrAuthHistoryResultVlanAssignedType,'agentAuthMgrAuthHistoryResultReasonCode':agentAuthMgrAuthHistoryResultReasonCode,'agentAuthMgrPortAuthHistoryResultClearTable':agentAuthMgrPortAuthHistoryResultClearTable,'agentAuthMgrPortAuthHistoryResultClearEntry':agentAuthMgrPortAuthHistoryResultClearEntry,_i:agentAuthMgrAuthHistoryResultIfIndex,'agentAuthMgrPortAuthHistoryResultsClear':agentAuthMgrPortAuthHistoryResultsClear,'agentAuthMgrAuthStatsGroup':agentAuthMgrAuthStatsGroup,'agentAuthMgrPortStatsTable':agentAuthMgrPortStatsTable,'agentAuthMgrPortStatsEntry':agentAuthMgrPortStatsEntry,_R:agentAuthMgrPortIfaceIndex,_j:agentAuthMgrPortMethodIndex,'agentAuthMgrPortStatsAttempts':agentAuthMgrPortStatsAttempts,'agentAuthMgrPortStatsFailedAttempts':agentAuthMgrPortStatsFailedAttempts,'agentAuthMgrPortStatsClearTable':agentAuthMgrPortStatsClearTable,'agentAuthMgrPortStatsClearEntry':agentAuthMgrPortStatsClearEntry,'agentAuthMgrPortStatsClear':agentAuthMgrPortStatsClear,'agentAuthMgrTrapsConfigGroup':agentAuthMgrTrapsConfigGroup,'authMgrTrapMode':authMgrTrapMode,'agentAuthMgrMonitorModeConfigGroup':agentAuthMgrMonitorModeConfigGroup,'agentAuthMgrMonitorModeEnabled':agentAuthMgrMonitorModeEnabled,'agentAuthMgrMonitorModeClients':agentAuthMgrMonitorModeClients,'agentAuthMgrNonMonitorModeClients':agentAuthMgrNonMonitorModeClients})