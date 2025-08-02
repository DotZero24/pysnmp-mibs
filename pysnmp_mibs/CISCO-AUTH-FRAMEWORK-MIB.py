_Af='cafAuthFailClientGroup'
_Ae='cafAuthFailNotifEnableGroup'
_Ad='cafAuthFailNotifGroup'
_Ac='cafAuthFailNotif'
_Ab='cafSecurityViolationNotif'
_Aa='cafAuthFailNotifEnable'
_AZ='cafCoADisablePortCommandIgnoreEnabled'
_AY='cafCoABouncePortCommandIgnoreEnabled'
_AX='cafMacMoveMode'
_AW='cafSessionVlanGroupName'
_AV='cafSecurityViolationNotifEnable'
_AU='cafSessionMethodState'
_AT='cafSessionTerminate'
_AS='cafSessionReauth'
_AR='cafSessionInactivityTimeLeft'
_AQ='cafSessionInactivityTimeout'
_AP='cafSessionTimeoutAction'
_AO='cafSessionTimeLeft'
_AN='cafSessionTimeout'
_AM='cafSessionAuthVlan'
_AL='cafSessionCriticalTimeLeft'
_AK='cafSessionAuthorizedBy'
_AJ='cafSessionClientFramedIpPool'
_AI='cafSessionAuthUserName'
_AH='cafSessionPostureToken'
_AG='cafSessionControlledDirection'
_AF='cafSessionAuthHostMode'
_AE='cafSessionStatus'
_AD='cafSessionDomain'
_AC='cafSessionClientAddress'
_AB='cafSessionClientAddrType'
_AA='cafSessionClientMacAddress'
_A9='cafServerAliveAction'
_A8='cafServerDeadAuthorizedVlan'
_A7='cafServerDeadRemainAuthorized'
_A6='cafServerDeadNoActionEnabled'
_A5='cafClientNoRespAuthorizedVlan'
_A4='cafClientNoRespNoActionEnabled'
_A3='cafAuthFailedNextMethodEnabled'
_A2='cafAuthFailedAuthorizedVlan'
_A1='cafAuthFailedNoActionEnabled'
_A0='cafAuthFailedMaxRetry'
_z='cafPortMethodOperPriority'
_y='cafPortMethodOperExecOrder'
_x='cafPortMethodAvailable'
_w='cafPortMethodAdminPriority'
_v='cafPortMethodAdminExecOrder'
_u='cafPortViolationAction'
_t='cafPortInactivityTimeout'
_s='cafPortRestartInterval'
_r='cafPortReauthInterval'
_q='cafPortReauthEnabled'
_p='cafPortAuthorizeControl'
_o='cafPortPreAuthOpenAccess'
_n='cafPortAuthHostMode'
_m='cafPortFallBackProfile'
_l='cafPortControlledDirection'
_k='cafAaaNoRespRecoveryDelay'
_j='cafAuthMethodDefaultExecOrder'
_i='cafAuthMethodDefaultPriority'
_h='accessible-for-notify'
_g='cafSessionMethod'
_f='running'
_e='cafAuthMethod'
_d='OctetString'
_c='cafCoACommandConfigGroup'
_b='cafMacMoveConfigGroup'
_a='deprecated'
_Z='cafAuthFailClient'
_Y='cafSecurityViolationClient'
_X='cafSessionId'
_W='not-accessible'
_V='ifName'
_U='cafSessionVlanGroupNameGroup'
_T='cafSecurityViolationClientGroup'
_S='cafSecurityViolationNotifGroup'
_R='cafSecViolationNotifEnableGroup'
_Q='cafServerEventGroup'
_P='cafClientNoRespEventGroup'
_O='cafAuthFailedEventGroup'
_N='cafAaaNoRespRecoveryDelayGroup'
_M='cafSessionMethodInfoGroup'
_L='cafSessionGroup'
_K='cafPortMethodGroup'
_J='cafAuthPortConfigGroup'
_I='cafAuthMethodRegGroup'
_H='seconds'
_G='ifIndex'
_F='IF-MIB'
_E='Integer32'
_D='read-only'
_C='read-write'
_B='current'
_A='CISCO-AUTH-FRAMEWORK-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_d,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CnnEouPostureTokenString,=mibBuilder.importSymbols('CISCO-NAC-TC-MIB','CnnEouPostureTokenString')
VlanIndexOrZero,=mibBuilder.importSymbols('CISCO-PRIVATE-VLAN-MIB','VlanIndexOrZero')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,ifName=mibBuilder.importSymbols(_F,_G,_V)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
ciscoAuthFrameworkMIB=ModuleIdentity((1,3,6,1,4,1,9,9,656))
if mibBuilder.loadTexts:ciscoAuthFrameworkMIB.setRevisions(('2013-08-23 00:00','2010-11-17 00:00','2010-04-01 00:00','2009-04-20 00:00','2008-10-24 00:00','2008-08-25 00:00'))
class CiscoAuthControlledDirections(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('both',0),('in',1)))
class CiscoAuthControlledPortControl(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('forceUnauthorized',1),('auto',2),('forceAuthorized',3)))
class CiscoAuthMethod(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('dot1x',2),('macAuthBypass',3),('webAuth',4)))
class CiscoAuthMethodList(TextualConvention,OctetString):status=_B
class CiscoAuthHostMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('singleHost',1),('multiHost',2),('multiAuth',3),('multiDomain',4)))
_CiscoAuthFrameworkMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoAuthFrameworkMIBNotifs=_CiscoAuthFrameworkMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,656,0))
_CiscoAuthFrameworkMIBObjects_ObjectIdentity=ObjectIdentity
ciscoAuthFrameworkMIBObjects=_CiscoAuthFrameworkMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,656,1))
_CiscoAuthFrameworkSystem_ObjectIdentity=ObjectIdentity
ciscoAuthFrameworkSystem=_CiscoAuthFrameworkSystem_ObjectIdentity((1,3,6,1,4,1,9,9,656,1,1))
_CafAaaNoRespRecoveryDelay_Type=Unsigned32
_CafAaaNoRespRecoveryDelay_Object=MibScalar
cafAaaNoRespRecoveryDelay=_CafAaaNoRespRecoveryDelay_Object((1,3,6,1,4,1,9,9,656,1,1,1),_CafAaaNoRespRecoveryDelay_Type())
cafAaaNoRespRecoveryDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cafAaaNoRespRecoveryDelay.setStatus(_B)
if mibBuilder.loadTexts:cafAaaNoRespRecoveryDelay.setUnits('milliseconds')
_CafAuthMethodRegTable_Object=MibTable
cafAuthMethodRegTable=_CafAuthMethodRegTable_Object((1,3,6,1,4,1,9,9,656,1,1,2))
if mibBuilder.loadTexts:cafAuthMethodRegTable.setStatus(_B)
_CafAuthMethodRegEntry_Object=MibTableRow
cafAuthMethodRegEntry=_CafAuthMethodRegEntry_Object((1,3,6,1,4,1,9,9,656,1,1,2,1))
cafAuthMethodRegEntry.setIndexNames((0,_A,_e))
if mibBuilder.loadTexts:cafAuthMethodRegEntry.setStatus(_B)
_CafAuthMethod_Type=CiscoAuthMethod
_CafAuthMethod_Object=MibTableColumn
cafAuthMethod=_CafAuthMethod_Object((1,3,6,1,4,1,9,9,656,1,1,2,1,1),_CafAuthMethod_Type())
cafAuthMethod.setMaxAccess(_W)
if mibBuilder.loadTexts:cafAuthMethod.setStatus(_B)
_CafAuthMethodDefaultPriority_Type=Unsigned32
_CafAuthMethodDefaultPriority_Object=MibTableColumn
cafAuthMethodDefaultPriority=_CafAuthMethodDefaultPriority_Object((1,3,6,1,4,1,9,9,656,1,1,2,1,2),_CafAuthMethodDefaultPriority_Type())
cafAuthMethodDefaultPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:cafAuthMethodDefaultPriority.setStatus(_B)
_CafAuthMethodDefaultExecOrder_Type=Unsigned32
_CafAuthMethodDefaultExecOrder_Object=MibTableColumn
cafAuthMethodDefaultExecOrder=_CafAuthMethodDefaultExecOrder_Object((1,3,6,1,4,1,9,9,656,1,1,2,1,3),_CafAuthMethodDefaultExecOrder_Type())
cafAuthMethodDefaultExecOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:cafAuthMethodDefaultExecOrder.setStatus(_B)
class _CafMacMoveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('deny',1),('permit',2)))
_CafMacMoveMode_Type.__name__=_E
_CafMacMoveMode_Object=MibScalar
cafMacMoveMode=_CafMacMoveMode_Object((1,3,6,1,4,1,9,9,656,1,1,3),_CafMacMoveMode_Type())
cafMacMoveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cafMacMoveMode.setStatus(_B)
_CafCoABouncePortCommandIgnoreEnabled_Type=TruthValue
_CafCoABouncePortCommandIgnoreEnabled_Object=MibScalar
cafCoABouncePortCommandIgnoreEnabled=_CafCoABouncePortCommandIgnoreEnabled_Object((1,3,6,1,4,1,9,9,656,1,1,4),_CafCoABouncePortCommandIgnoreEnabled_Type())
cafCoABouncePortCommandIgnoreEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cafCoABouncePortCommandIgnoreEnabled.setStatus(_B)
_CafCoADisablePortCommandIgnoreEnabled_Type=TruthValue
_CafCoADisablePortCommandIgnoreEnabled_Object=MibScalar
cafCoADisablePortCommandIgnoreEnabled=_CafCoADisablePortCommandIgnoreEnabled_Object((1,3,6,1,4,1,9,9,656,1,1,5),_CafCoADisablePortCommandIgnoreEnabled_Type())
cafCoADisablePortCommandIgnoreEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cafCoADisablePortCommandIgnoreEnabled.setStatus(_B)
_CiscoAuthFrwkAuthenticator_ObjectIdentity=ObjectIdentity
ciscoAuthFrwkAuthenticator=_CiscoAuthFrwkAuthenticator_ObjectIdentity((1,3,6,1,4,1,9,9,656,1,2))
_CafPortConfigTable_Object=MibTable
cafPortConfigTable=_CafPortConfigTable_Object((1,3,6,1,4,1,9,9,656,1,2,1))
if mibBuilder.loadTexts:cafPortConfigTable.setStatus(_B)
_CafPortConfigEntry_Object=MibTableRow
cafPortConfigEntry=_CafPortConfigEntry_Object((1,3,6,1,4,1,9,9,656,1,2,1,1))
cafPortConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cafPortConfigEntry.setStatus(_B)
_CafPortControlledDirection_Type=CiscoAuthControlledDirections
_CafPortControlledDirection_Object=MibTableColumn
cafPortControlledDirection=_CafPortControlledDirection_Object((1,3,6,1,4,1,9,9,656,1,2,1,1,1),_CafPortControlledDirection_Type())
cafPortControlledDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:cafPortControlledDirection.setStatus(_B)
_CafPortFallBackProfile_Type=SnmpAdminString
_CafPortFallBackProfile_Object=MibTableColumn
cafPortFallBackProfile=_CafPortFallBackProfile_Object((1,3,6,1,4,1,9,9,656,1,2,1,1,2),_CafPortFallBackProfile_Type())
cafPortFallBackProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:cafPortFallBackProfile.setStatus(_B)
_CafPortAuthHostMode_Type=CiscoAuthHostMode
_CafPortAuthHostMode_Object=MibTableColumn
cafPortAuthHostMode=_CafPortAuthHostMode_Object((1,3,6,1,4,1,9,9,656,1,2,1,1,3),_CafPortAuthHostMode_Type())
cafPortAuthHostMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cafPortAuthHostMode.setStatus(_B)
_CafPortPreAuthOpenAccess_Type=TruthValue
_CafPortPreAuthOpenAccess_Object=MibTableColumn
cafPortPreAuthOpenAccess=_CafPortPreAuthOpenAccess_Object((1,3,6,1,4,1,9,9,656,1,2,1,1,4),_CafPortPreAuthOpenAccess_Type())
cafPortPreAuthOpenAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:cafPortPreAuthOpenAccess.setStatus(_B)
_CafPortAuthorizeControl_Type=CiscoAuthControlledPortControl
_CafPortAuthorizeControl_Object=MibTableColumn
cafPortAuthorizeControl=_CafPortAuthorizeControl_Object((1,3,6,1,4,1,9,9,656,1,2,1,1,5),_CafPortAuthorizeControl_Type())
cafPortAuthorizeControl.setMaxAccess(_C)
if mibBuilder.loadTexts:cafPortAuthorizeControl.setStatus(_B)
_CafPortReauthEnabled_Type=TruthValue
_CafPortReauthEnabled_Object=MibTableColumn
cafPortReauthEnabled=_CafPortReauthEnabled_Object((1,3,6,1,4,1,9,9,656,1,2,1,1,6),_CafPortReauthEnabled_Type())
cafPortReauthEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cafPortReauthEnabled.setStatus(_B)
_CafPortReauthInterval_Type=Unsigned32
_CafPortReauthInterval_Object=MibTableColumn
cafPortReauthInterval=_CafPortReauthInterval_Object((1,3,6,1,4,1,9,9,656,1,2,1,1,7),_CafPortReauthInterval_Type())
cafPortReauthInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cafPortReauthInterval.setStatus(_B)
if mibBuilder.loadTexts:cafPortReauthInterval.setUnits(_H)
_CafPortRestartInterval_Type=Unsigned32
_CafPortRestartInterval_Object=MibTableColumn
cafPortRestartInterval=_CafPortRestartInterval_Object((1,3,6,1,4,1,9,9,656,1,2,1,1,8),_CafPortRestartInterval_Type())
cafPortRestartInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cafPortRestartInterval.setStatus(_B)
if mibBuilder.loadTexts:cafPortRestartInterval.setUnits(_H)
class _CafPortInactivityTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,0),ValueRangeConstraint(1,65535))
_CafPortInactivityTimeout_Type.__name__=_E
_CafPortInactivityTimeout_Object=MibTableColumn
cafPortInactivityTimeout=_CafPortInactivityTimeout_Object((1,3,6,1,4,1,9,9,656,1,2,1,1,9),_CafPortInactivityTimeout_Type())
cafPortInactivityTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cafPortInactivityTimeout.setStatus(_B)
if mibBuilder.loadTexts:cafPortInactivityTimeout.setUnits(_H)
class _CafPortViolationAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('restrict',1),('shutdown',2),('protect',3),('replace',4)))
_CafPortViolationAction_Type.__name__=_E
_CafPortViolationAction_Object=MibTableColumn
cafPortViolationAction=_CafPortViolationAction_Object((1,3,6,1,4,1,9,9,656,1,2,1,1,10),_CafPortViolationAction_Type())
cafPortViolationAction.setMaxAccess(_C)
if mibBuilder.loadTexts:cafPortViolationAction.setStatus(_B)
_CafPortMethodTable_Object=MibTable
cafPortMethodTable=_CafPortMethodTable_Object((1,3,6,1,4,1,9,9,656,1,2,2))
if mibBuilder.loadTexts:cafPortMethodTable.setStatus(_B)
_CafPortMethodEntry_Object=MibTableRow
cafPortMethodEntry=_CafPortMethodEntry_Object((1,3,6,1,4,1,9,9,656,1,2,2,1))
cafPortMethodEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cafPortMethodEntry.setStatus(_B)
_CafPortMethodAdminExecOrder_Type=CiscoAuthMethodList
_CafPortMethodAdminExecOrder_Object=MibTableColumn
cafPortMethodAdminExecOrder=_CafPortMethodAdminExecOrder_Object((1,3,6,1,4,1,9,9,656,1,2,2,1,1),_CafPortMethodAdminExecOrder_Type())
cafPortMethodAdminExecOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:cafPortMethodAdminExecOrder.setStatus(_B)
_CafPortMethodAdminPriority_Type=CiscoAuthMethodList
_CafPortMethodAdminPriority_Object=MibTableColumn
cafPortMethodAdminPriority=_CafPortMethodAdminPriority_Object((1,3,6,1,4,1,9,9,656,1,2,2,1,2),_CafPortMethodAdminPriority_Type())
cafPortMethodAdminPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cafPortMethodAdminPriority.setStatus(_B)
_CafPortMethodAvailable_Type=CiscoAuthMethodList
_CafPortMethodAvailable_Object=MibTableColumn
cafPortMethodAvailable=_CafPortMethodAvailable_Object((1,3,6,1,4,1,9,9,656,1,2,2,1,3),_CafPortMethodAvailable_Type())
cafPortMethodAvailable.setMaxAccess(_D)
if mibBuilder.loadTexts:cafPortMethodAvailable.setStatus(_B)
_CafPortMethodOperExecOrder_Type=CiscoAuthMethodList
_CafPortMethodOperExecOrder_Object=MibTableColumn
cafPortMethodOperExecOrder=_CafPortMethodOperExecOrder_Object((1,3,6,1,4,1,9,9,656,1,2,2,1,4),_CafPortMethodOperExecOrder_Type())
cafPortMethodOperExecOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:cafPortMethodOperExecOrder.setStatus(_B)
_CafPortMethodOperPriority_Type=CiscoAuthMethodList
_CafPortMethodOperPriority_Object=MibTableColumn
cafPortMethodOperPriority=_CafPortMethodOperPriority_Object((1,3,6,1,4,1,9,9,656,1,2,2,1,5),_CafPortMethodOperPriority_Type())
cafPortMethodOperPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:cafPortMethodOperPriority.setStatus(_B)
_CiscoAuthFrameworkEvent_ObjectIdentity=ObjectIdentity
ciscoAuthFrameworkEvent=_CiscoAuthFrameworkEvent_ObjectIdentity((1,3,6,1,4,1,9,9,656,1,3))
_CafAuthFailedEventPortTable_Object=MibTable
cafAuthFailedEventPortTable=_CafAuthFailedEventPortTable_Object((1,3,6,1,4,1,9,9,656,1,3,1))
if mibBuilder.loadTexts:cafAuthFailedEventPortTable.setStatus(_B)
_CafAuthFailedEventPortEntry_Object=MibTableRow
cafAuthFailedEventPortEntry=_CafAuthFailedEventPortEntry_Object((1,3,6,1,4,1,9,9,656,1,3,1,1))
cafAuthFailedEventPortEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cafAuthFailedEventPortEntry.setStatus(_B)
_CafAuthFailedMaxRetry_Type=Unsigned32
_CafAuthFailedMaxRetry_Object=MibTableColumn
cafAuthFailedMaxRetry=_CafAuthFailedMaxRetry_Object((1,3,6,1,4,1,9,9,656,1,3,1,1,1),_CafAuthFailedMaxRetry_Type())
cafAuthFailedMaxRetry.setMaxAccess(_C)
if mibBuilder.loadTexts:cafAuthFailedMaxRetry.setStatus(_B)
_CafAuthFailedNoActionEnabled_Type=TruthValue
_CafAuthFailedNoActionEnabled_Object=MibTableColumn
cafAuthFailedNoActionEnabled=_CafAuthFailedNoActionEnabled_Object((1,3,6,1,4,1,9,9,656,1,3,1,1,2),_CafAuthFailedNoActionEnabled_Type())
cafAuthFailedNoActionEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cafAuthFailedNoActionEnabled.setStatus(_B)
class _CafAuthFailedAuthorizedVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_CafAuthFailedAuthorizedVlan_Type.__name__=_E
_CafAuthFailedAuthorizedVlan_Object=MibTableColumn
cafAuthFailedAuthorizedVlan=_CafAuthFailedAuthorizedVlan_Object((1,3,6,1,4,1,9,9,656,1,3,1,1,3),_CafAuthFailedAuthorizedVlan_Type())
cafAuthFailedAuthorizedVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:cafAuthFailedAuthorizedVlan.setStatus(_B)
_CafAuthFailedNextMethodEnabled_Type=TruthValue
_CafAuthFailedNextMethodEnabled_Object=MibTableColumn
cafAuthFailedNextMethodEnabled=_CafAuthFailedNextMethodEnabled_Object((1,3,6,1,4,1,9,9,656,1,3,1,1,4),_CafAuthFailedNextMethodEnabled_Type())
cafAuthFailedNextMethodEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cafAuthFailedNextMethodEnabled.setStatus(_B)
_CafClientNoRespEventPortTable_Object=MibTable
cafClientNoRespEventPortTable=_CafClientNoRespEventPortTable_Object((1,3,6,1,4,1,9,9,656,1,3,2))
if mibBuilder.loadTexts:cafClientNoRespEventPortTable.setStatus(_B)
_CafClientNoRespEventPortEntry_Object=MibTableRow
cafClientNoRespEventPortEntry=_CafClientNoRespEventPortEntry_Object((1,3,6,1,4,1,9,9,656,1,3,2,1))
cafClientNoRespEventPortEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cafClientNoRespEventPortEntry.setStatus(_B)
_CafClientNoRespNoActionEnabled_Type=TruthValue
_CafClientNoRespNoActionEnabled_Object=MibTableColumn
cafClientNoRespNoActionEnabled=_CafClientNoRespNoActionEnabled_Object((1,3,6,1,4,1,9,9,656,1,3,2,1,1),_CafClientNoRespNoActionEnabled_Type())
cafClientNoRespNoActionEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cafClientNoRespNoActionEnabled.setStatus(_B)
class _CafClientNoRespAuthorizedVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_CafClientNoRespAuthorizedVlan_Type.__name__=_E
_CafClientNoRespAuthorizedVlan_Object=MibTableColumn
cafClientNoRespAuthorizedVlan=_CafClientNoRespAuthorizedVlan_Object((1,3,6,1,4,1,9,9,656,1,3,2,1,2),_CafClientNoRespAuthorizedVlan_Type())
cafClientNoRespAuthorizedVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:cafClientNoRespAuthorizedVlan.setStatus(_B)
_CafServerEventPortTable_Object=MibTable
cafServerEventPortTable=_CafServerEventPortTable_Object((1,3,6,1,4,1,9,9,656,1,3,3))
if mibBuilder.loadTexts:cafServerEventPortTable.setStatus(_B)
_CafServerEventPortEntry_Object=MibTableRow
cafServerEventPortEntry=_CafServerEventPortEntry_Object((1,3,6,1,4,1,9,9,656,1,3,3,1))
cafServerEventPortEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cafServerEventPortEntry.setStatus(_B)
_CafServerDeadNoActionEnabled_Type=TruthValue
_CafServerDeadNoActionEnabled_Object=MibTableColumn
cafServerDeadNoActionEnabled=_CafServerDeadNoActionEnabled_Object((1,3,6,1,4,1,9,9,656,1,3,3,1,1),_CafServerDeadNoActionEnabled_Type())
cafServerDeadNoActionEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cafServerDeadNoActionEnabled.setStatus(_B)
_CafServerDeadRemainAuthorized_Type=TruthValue
_CafServerDeadRemainAuthorized_Object=MibTableColumn
cafServerDeadRemainAuthorized=_CafServerDeadRemainAuthorized_Object((1,3,6,1,4,1,9,9,656,1,3,3,1,2),_CafServerDeadRemainAuthorized_Type())
cafServerDeadRemainAuthorized.setMaxAccess(_C)
if mibBuilder.loadTexts:cafServerDeadRemainAuthorized.setStatus(_B)
class _CafServerDeadAuthorizedVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_CafServerDeadAuthorizedVlan_Type.__name__=_E
_CafServerDeadAuthorizedVlan_Object=MibTableColumn
cafServerDeadAuthorizedVlan=_CafServerDeadAuthorizedVlan_Object((1,3,6,1,4,1,9,9,656,1,3,3,1,3),_CafServerDeadAuthorizedVlan_Type())
cafServerDeadAuthorizedVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:cafServerDeadAuthorizedVlan.setStatus(_B)
class _CafServerAliveAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('reinitialize',2)))
_CafServerAliveAction_Type.__name__=_E
_CafServerAliveAction_Object=MibTableColumn
cafServerAliveAction=_CafServerAliveAction_Object((1,3,6,1,4,1,9,9,656,1,3,3,1,4),_CafServerAliveAction_Type())
cafServerAliveAction.setMaxAccess(_C)
if mibBuilder.loadTexts:cafServerAliveAction.setStatus(_B)
_CiscoAuthFrameworkSession_ObjectIdentity=ObjectIdentity
ciscoAuthFrameworkSession=_CiscoAuthFrameworkSession_ObjectIdentity((1,3,6,1,4,1,9,9,656,1,4))
_CafSessionTable_Object=MibTable
cafSessionTable=_CafSessionTable_Object((1,3,6,1,4,1,9,9,656,1,4,1))
if mibBuilder.loadTexts:cafSessionTable.setStatus(_B)
_CafSessionEntry_Object=MibTableRow
cafSessionEntry=_CafSessionEntry_Object((1,3,6,1,4,1,9,9,656,1,4,1,1))
cafSessionEntry.setIndexNames((0,_F,_G),(1,_A,_X))
if mibBuilder.loadTexts:cafSessionEntry.setStatus(_B)
class _CafSessionId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CafSessionId_Type.__name__=_d
_CafSessionId_Object=MibTableColumn
cafSessionId=_CafSessionId_Object((1,3,6,1,4,1,9,9,656,1,4,1,1,1),_CafSessionId_Type())
cafSessionId.setMaxAccess(_W)
if mibBuilder.loadTexts:cafSessionId.setStatus(_B)
_CafSessionClientMacAddress_Type=MacAddress
_CafSessionClientMacAddress_Object=MibTableColumn
cafSessionClientMacAddress=_CafSessionClientMacAddress_Object((1,3,6,1,4,1,9,9,656,1,4,1,1,2),_CafSessionClientMacAddress_Type())
cafSessionClientMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cafSessionClientMacAddress.setStatus(_B)
_CafSessionClientAddrType_Type=InetAddressType
_CafSessionClientAddrType_Object=MibTableColumn
cafSessionClientAddrType=_CafSessionClientAddrType_Object((1,3,6,1,4,1,9,9,656,1,4,1,1,3),_CafSessionClientAddrType_Type())
cafSessionClientAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cafSessionClientAddrType.setStatus(_B)
_CafSessionClientAddress_Type=InetAddress
_CafSessionClientAddress_Object=MibTableColumn
cafSessionClientAddress=_CafSessionClientAddress_Object((1,3,6,1,4,1,9,9,656,1,4,1,1,4),_CafSessionClientAddress_Type())
cafSessionClientAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cafSessionClientAddress.setStatus(_B)
class _CafSessionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('idle',1),(_f,2),('noMethod',3),('authenticationSuccess',4),('authenticationFailed',5),('authorizationSuccess',6),('authorizationFailed',7)))
_CafSessionStatus_Type.__name__=_E
_CafSessionStatus_Object=MibTableColumn
cafSessionStatus=_CafSessionStatus_Object((1,3,6,1,4,1,9,9,656,1,4,1,1,5),_CafSessionStatus_Type())
cafSessionStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cafSessionStatus.setStatus(_B)
class _CafSessionDomain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('data',2),('voice',3)))
_CafSessionDomain_Type.__name__=_E
_CafSessionDomain_Object=MibTableColumn
cafSessionDomain=_CafSessionDomain_Object((1,3,6,1,4,1,9,9,656,1,4,1,1,6),_CafSessionDomain_Type())
cafSessionDomain.setMaxAccess(_D)
if mibBuilder.loadTexts:cafSessionDomain.setStatus(_B)
_CafSessionAuthHostMode_Type=CiscoAuthHostMode
_CafSessionAuthHostMode_Object=MibTableColumn
cafSessionAuthHostMode=_CafSessionAuthHostMode_Object((1,3,6,1,4,1,9,9,656,1,4,1,1,7),_CafSessionAuthHostMode_Type())
cafSessionAuthHostMode.setMaxAccess(_D)
if mibBuilder.loadTexts:cafSessionAuthHostMode.setStatus(_B)
_CafSessionControlledDirection_Type=CiscoAuthControlledDirections
_CafSessionControlledDirection_Object=MibTableColumn
cafSessionControlledDirection=_CafSessionControlledDirection_Object((1,3,6,1,4,1,9,9,656,1,4,1,1,8),_CafSessionControlledDirection_Type())
cafSessionControlledDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:cafSessionControlledDirection.setStatus(_B)
_CafSessionPostureToken_Type=CnnEouPostureTokenString
_CafSessionPostureToken_Object=MibTableColumn
cafSessionPostureToken=_CafSessionPostureToken_Object((1,3,6,1,4,1,9,9,656,1,4,1,1,9),_CafSessionPostureToken_Type())
cafSessionPostureToken.setMaxAccess(_D)
if mibBuilder.loadTexts:cafSessionPostureToken.setStatus(_B)
_CafSessionAuthUserName_Type=SnmpAdminString
_CafSessionAuthUserName_Object=MibTableColumn
cafSessionAuthUserName=_CafSessionAuthUserName_Object((1,3,6,1,4,1,9,9,656,1,4,1,1,10),_CafSessionAuthUserName_Type())
cafSessionAuthUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:cafSessionAuthUserName.setStatus(_B)
_CafSessionClientFramedIpPool_Type=SnmpAdminString
_CafSessionClientFramedIpPool_Object=MibTableColumn
cafSessionClientFramedIpPool=_CafSessionClientFramedIpPool_Object((1,3,6,1,4,1,9,9,656,1,4,1,1,11),_CafSessionClientFramedIpPool_Type())
cafSessionClientFramedIpPool.setMaxAccess(_D)
if mibBuilder.loadTexts:cafSessionClientFramedIpPool.setStatus(_B)
_CafSessionAuthorizedBy_Type=SnmpAdminString
_CafSessionAuthorizedBy_Object=MibTableColumn
cafSessionAuthorizedBy=_CafSessionAuthorizedBy_Object((1,3,6,1,4,1,9,9,656,1,4,1,1,12),_CafSessionAuthorizedBy_Type())
cafSessionAuthorizedBy.setMaxAccess(_D)
if mibBuilder.loadTexts:cafSessionAuthorizedBy.setStatus(_B)
_CafSessionCriticalTimeLeft_Type=Unsigned32
_CafSessionCriticalTimeLeft_Object=MibTableColumn
cafSessionCriticalTimeLeft=_CafSessionCriticalTimeLeft_Object((1,3,6,1,4,1,9,9,656,1,4,1,1,13),_CafSessionCriticalTimeLeft_Type())
cafSessionCriticalTimeLeft.setMaxAccess(_D)
if mibBuilder.loadTexts:cafSessionCriticalTimeLeft.setStatus(_B)
if mibBuilder.loadTexts:cafSessionCriticalTimeLeft.setUnits(_H)
_CafSessionAuthVlan_Type=VlanIndexOrZero
_CafSessionAuthVlan_Object=MibTableColumn
cafSessionAuthVlan=_CafSessionAuthVlan_Object((1,3,6,1,4,1,9,9,656,1,4,1,1,14),_CafSessionAuthVlan_Type())
cafSessionAuthVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:cafSessionAuthVlan.setStatus(_B)
_CafSessionTimeout_Type=Unsigned32
_CafSessionTimeout_Object=MibTableColumn
cafSessionTimeout=_CafSessionTimeout_Object((1,3,6,1,4,1,9,9,656,1,4,1,1,15),_CafSessionTimeout_Type())
cafSessionTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cafSessionTimeout.setStatus(_B)
if mibBuilder.loadTexts:cafSessionTimeout.setUnits(_H)
_CafSessionTimeLeft_Type=Unsigned32
_CafSessionTimeLeft_Object=MibTableColumn
cafSessionTimeLeft=_CafSessionTimeLeft_Object((1,3,6,1,4,1,9,9,656,1,4,1,1,16),_CafSessionTimeLeft_Type())
cafSessionTimeLeft.setMaxAccess(_D)
if mibBuilder.loadTexts:cafSessionTimeLeft.setStatus(_B)
if mibBuilder.loadTexts:cafSessionTimeLeft.setUnits(_H)
class _CafSessionTimeoutAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('terminate',2),('reauthenticate',3)))
_CafSessionTimeoutAction_Type.__name__=_E
_CafSessionTimeoutAction_Object=MibTableColumn
cafSessionTimeoutAction=_CafSessionTimeoutAction_Object((1,3,6,1,4,1,9,9,656,1,4,1,1,17),_CafSessionTimeoutAction_Type())
cafSessionTimeoutAction.setMaxAccess(_D)
if mibBuilder.loadTexts:cafSessionTimeoutAction.setStatus(_B)
_CafSessionInactivityTimeout_Type=Unsigned32
_CafSessionInactivityTimeout_Object=MibTableColumn
cafSessionInactivityTimeout=_CafSessionInactivityTimeout_Object((1,3,6,1,4,1,9,9,656,1,4,1,1,18),_CafSessionInactivityTimeout_Type())
cafSessionInactivityTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cafSessionInactivityTimeout.setStatus(_B)
if mibBuilder.loadTexts:cafSessionInactivityTimeout.setUnits(_H)
_CafSessionInactivityTimeLeft_Type=Unsigned32
_CafSessionInactivityTimeLeft_Object=MibTableColumn
cafSessionInactivityTimeLeft=_CafSessionInactivityTimeLeft_Object((1,3,6,1,4,1,9,9,656,1,4,1,1,19),_CafSessionInactivityTimeLeft_Type())
cafSessionInactivityTimeLeft.setMaxAccess(_D)
if mibBuilder.loadTexts:cafSessionInactivityTimeLeft.setStatus(_B)
if mibBuilder.loadTexts:cafSessionInactivityTimeLeft.setUnits(_H)
_CafSessionReauth_Type=TruthValue
_CafSessionReauth_Object=MibTableColumn
cafSessionReauth=_CafSessionReauth_Object((1,3,6,1,4,1,9,9,656,1,4,1,1,20),_CafSessionReauth_Type())
cafSessionReauth.setMaxAccess(_C)
if mibBuilder.loadTexts:cafSessionReauth.setStatus(_B)
_CafSessionTerminate_Type=TruthValue
_CafSessionTerminate_Object=MibTableColumn
cafSessionTerminate=_CafSessionTerminate_Object((1,3,6,1,4,1,9,9,656,1,4,1,1,21),_CafSessionTerminate_Type())
cafSessionTerminate.setMaxAccess(_C)
if mibBuilder.loadTexts:cafSessionTerminate.setStatus(_B)
_CafSessionVlanGroupName_Type=SnmpAdminString
_CafSessionVlanGroupName_Object=MibTableColumn
cafSessionVlanGroupName=_CafSessionVlanGroupName_Object((1,3,6,1,4,1,9,9,656,1,4,1,1,22),_CafSessionVlanGroupName_Type())
cafSessionVlanGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:cafSessionVlanGroupName.setStatus(_B)
_CafSessionMethodsInfoTable_Object=MibTable
cafSessionMethodsInfoTable=_CafSessionMethodsInfoTable_Object((1,3,6,1,4,1,9,9,656,1,4,2))
if mibBuilder.loadTexts:cafSessionMethodsInfoTable.setStatus(_B)
_CafSessionMethodsInfoEntry_Object=MibTableRow
cafSessionMethodsInfoEntry=_CafSessionMethodsInfoEntry_Object((1,3,6,1,4,1,9,9,656,1,4,2,1))
cafSessionMethodsInfoEntry.setIndexNames((0,_F,_G),(0,_A,_X),(0,_A,_g))
if mibBuilder.loadTexts:cafSessionMethodsInfoEntry.setStatus(_B)
_CafSessionMethod_Type=CiscoAuthMethod
_CafSessionMethod_Object=MibTableColumn
cafSessionMethod=_CafSessionMethod_Object((1,3,6,1,4,1,9,9,656,1,4,2,1,1),_CafSessionMethod_Type())
cafSessionMethod.setMaxAccess(_W)
if mibBuilder.loadTexts:cafSessionMethod.setStatus(_B)
class _CafSessionMethodState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notRun',1),(_f,2),('failedOver',3),('authcSuccess',4),('authcFailed',5)))
_CafSessionMethodState_Type.__name__=_E
_CafSessionMethodState_Object=MibTableColumn
cafSessionMethodState=_CafSessionMethodState_Object((1,3,6,1,4,1,9,9,656,1,4,2,1,2),_CafSessionMethodState_Type())
cafSessionMethodState.setMaxAccess(_D)
if mibBuilder.loadTexts:cafSessionMethodState.setStatus(_B)
_CiscoAuthFrwkNotifControl_ObjectIdentity=ObjectIdentity
ciscoAuthFrwkNotifControl=_CiscoAuthFrwkNotifControl_ObjectIdentity((1,3,6,1,4,1,9,9,656,1,5))
_CafSecurityViolationNotifEnable_Type=TruthValue
_CafSecurityViolationNotifEnable_Object=MibScalar
cafSecurityViolationNotifEnable=_CafSecurityViolationNotifEnable_Object((1,3,6,1,4,1,9,9,656,1,5,1),_CafSecurityViolationNotifEnable_Type())
cafSecurityViolationNotifEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cafSecurityViolationNotifEnable.setStatus(_B)
_CafAuthFailNotifEnable_Type=TruthValue
_CafAuthFailNotifEnable_Object=MibScalar
cafAuthFailNotifEnable=_CafAuthFailNotifEnable_Object((1,3,6,1,4,1,9,9,656,1,5,2),_CafAuthFailNotifEnable_Type())
cafAuthFailNotifEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cafAuthFailNotifEnable.setStatus(_B)
_CiscoAuthFrwkNotifInfo_ObjectIdentity=ObjectIdentity
ciscoAuthFrwkNotifInfo=_CiscoAuthFrwkNotifInfo_ObjectIdentity((1,3,6,1,4,1,9,9,656,1,6))
_CafSecurityViolationClient_Type=MacAddress
_CafSecurityViolationClient_Object=MibScalar
cafSecurityViolationClient=_CafSecurityViolationClient_Object((1,3,6,1,4,1,9,9,656,1,6,1),_CafSecurityViolationClient_Type())
cafSecurityViolationClient.setMaxAccess(_h)
if mibBuilder.loadTexts:cafSecurityViolationClient.setStatus(_B)
_CafAuthFailClient_Type=MacAddress
_CafAuthFailClient_Object=MibScalar
cafAuthFailClient=_CafAuthFailClient_Object((1,3,6,1,4,1,9,9,656,1,6,2),_CafAuthFailClient_Type())
cafAuthFailClient.setMaxAccess(_h)
if mibBuilder.loadTexts:cafAuthFailClient.setStatus(_B)
_CiscoAuthFrameworkMIBConform_ObjectIdentity=ObjectIdentity
ciscoAuthFrameworkMIBConform=_CiscoAuthFrameworkMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,656,2))
_CiscoAuthFrameworkMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoAuthFrameworkMIBCompliances=_CiscoAuthFrameworkMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,656,2,1))
_CiscoAuthFrameworkMIBGroups_ObjectIdentity=ObjectIdentity
ciscoAuthFrameworkMIBGroups=_CiscoAuthFrameworkMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,656,2,2))
cafAuthMethodRegGroup=ObjectGroup((1,3,6,1,4,1,9,9,656,2,2,1))
cafAuthMethodRegGroup.setObjects(*((_A,_i),(_A,_j)))
if mibBuilder.loadTexts:cafAuthMethodRegGroup.setStatus(_B)
cafAaaNoRespRecoveryDelayGroup=ObjectGroup((1,3,6,1,4,1,9,9,656,2,2,2))
cafAaaNoRespRecoveryDelayGroup.setObjects((_A,_k))
if mibBuilder.loadTexts:cafAaaNoRespRecoveryDelayGroup.setStatus(_B)
cafAuthPortConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,656,2,2,3))
cafAuthPortConfigGroup.setObjects(*((_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:cafAuthPortConfigGroup.setStatus(_B)
cafPortMethodGroup=ObjectGroup((1,3,6,1,4,1,9,9,656,2,2,4))
cafPortMethodGroup.setObjects(*((_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:cafPortMethodGroup.setStatus(_B)
cafAuthFailedEventGroup=ObjectGroup((1,3,6,1,4,1,9,9,656,2,2,5))
cafAuthFailedEventGroup.setObjects(*((_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:cafAuthFailedEventGroup.setStatus(_B)
cafClientNoRespEventGroup=ObjectGroup((1,3,6,1,4,1,9,9,656,2,2,6))
cafClientNoRespEventGroup.setObjects(*((_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:cafClientNoRespEventGroup.setStatus(_B)
cafServerEventGroup=ObjectGroup((1,3,6,1,4,1,9,9,656,2,2,7))
cafServerEventGroup.setObjects(*((_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:cafServerEventGroup.setStatus(_B)
cafSessionGroup=ObjectGroup((1,3,6,1,4,1,9,9,656,2,2,8))
cafSessionGroup.setObjects(*((_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT)))
if mibBuilder.loadTexts:cafSessionGroup.setStatus(_B)
cafSessionMethodInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,656,2,2,9))
cafSessionMethodInfoGroup.setObjects((_A,_AU))
if mibBuilder.loadTexts:cafSessionMethodInfoGroup.setStatus(_B)
cafSecViolationNotifEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,656,2,2,10))
cafSecViolationNotifEnableGroup.setObjects((_A,_AV))
if mibBuilder.loadTexts:cafSecViolationNotifEnableGroup.setStatus(_B)
cafSecurityViolationClientGroup=ObjectGroup((1,3,6,1,4,1,9,9,656,2,2,12))
cafSecurityViolationClientGroup.setObjects((_A,_Y))
if mibBuilder.loadTexts:cafSecurityViolationClientGroup.setStatus(_B)
cafSessionVlanGroupNameGroup=ObjectGroup((1,3,6,1,4,1,9,9,656,2,2,13))
cafSessionVlanGroupNameGroup.setObjects((_A,_AW))
if mibBuilder.loadTexts:cafSessionVlanGroupNameGroup.setStatus(_B)
cafMacMoveConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,656,2,2,14))
cafMacMoveConfigGroup.setObjects((_A,_AX))
if mibBuilder.loadTexts:cafMacMoveConfigGroup.setStatus(_B)
cafCoACommandConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,656,2,2,15))
cafCoACommandConfigGroup.setObjects(*((_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:cafCoACommandConfigGroup.setStatus(_B)
cafAuthFailNotifEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,656,2,2,17))
cafAuthFailNotifEnableGroup.setObjects((_A,_Aa))
if mibBuilder.loadTexts:cafAuthFailNotifEnableGroup.setStatus(_B)
cafAuthFailClientGroup=ObjectGroup((1,3,6,1,4,1,9,9,656,2,2,18))
cafAuthFailClientGroup.setObjects((_A,_Z))
if mibBuilder.loadTexts:cafAuthFailClientGroup.setStatus(_B)
cafSecurityViolationNotif=NotificationType((1,3,6,1,4,1,9,9,656,0,1))
cafSecurityViolationNotif.setObjects(*((_F,_G),(_F,_V),(_A,_Y)))
if mibBuilder.loadTexts:cafSecurityViolationNotif.setStatus(_B)
cafAuthFailNotif=NotificationType((1,3,6,1,4,1,9,9,656,0,2))
cafAuthFailNotif.setObjects(*((_F,_V),(_A,_Z)))
if mibBuilder.loadTexts:cafAuthFailNotif.setStatus(_B)
cafSecurityViolationNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,656,2,2,11))
cafSecurityViolationNotifGroup.setObjects((_A,_Ab))
if mibBuilder.loadTexts:cafSecurityViolationNotifGroup.setStatus(_B)
cafAuthFailNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,656,2,2,16))
cafAuthFailNotifGroup.setObjects((_A,_Ac))
if mibBuilder.loadTexts:cafAuthFailNotifGroup.setStatus(_B)
ciscoAuthFrameworkMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,656,2,1,1))
ciscoAuthFrameworkMIBCompliance.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:ciscoAuthFrameworkMIBCompliance.setStatus(_a)
ciscoAuthFrameworkMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,656,2,1,2))
ciscoAuthFrameworkMIBCompliance2.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:ciscoAuthFrameworkMIBCompliance2.setStatus(_a)
ciscoAuthFrameworkMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,656,2,1,3))
ciscoAuthFrameworkMIBCompliance3.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:ciscoAuthFrameworkMIBCompliance3.setStatus(_a)
ciscoAuthFrameworkMIBCompliance4=ModuleCompliance((1,3,6,1,4,1,9,9,656,2,1,4))
ciscoAuthFrameworkMIBCompliance4.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_b),(_A,_c),(_A,_Ad),(_A,_Ae),(_A,_Af)))
if mibBuilder.loadTexts:ciscoAuthFrameworkMIBCompliance4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CiscoAuthControlledDirections':CiscoAuthControlledDirections,'CiscoAuthControlledPortControl':CiscoAuthControlledPortControl,'CiscoAuthMethod':CiscoAuthMethod,'CiscoAuthMethodList':CiscoAuthMethodList,'CiscoAuthHostMode':CiscoAuthHostMode,'ciscoAuthFrameworkMIB':ciscoAuthFrameworkMIB,'ciscoAuthFrameworkMIBNotifs':ciscoAuthFrameworkMIBNotifs,_Ab:cafSecurityViolationNotif,_Ac:cafAuthFailNotif,'ciscoAuthFrameworkMIBObjects':ciscoAuthFrameworkMIBObjects,'ciscoAuthFrameworkSystem':ciscoAuthFrameworkSystem,_k:cafAaaNoRespRecoveryDelay,'cafAuthMethodRegTable':cafAuthMethodRegTable,'cafAuthMethodRegEntry':cafAuthMethodRegEntry,_e:cafAuthMethod,_i:cafAuthMethodDefaultPriority,_j:cafAuthMethodDefaultExecOrder,_AX:cafMacMoveMode,_AY:cafCoABouncePortCommandIgnoreEnabled,_AZ:cafCoADisablePortCommandIgnoreEnabled,'ciscoAuthFrwkAuthenticator':ciscoAuthFrwkAuthenticator,'cafPortConfigTable':cafPortConfigTable,'cafPortConfigEntry':cafPortConfigEntry,_l:cafPortControlledDirection,_m:cafPortFallBackProfile,_n:cafPortAuthHostMode,_o:cafPortPreAuthOpenAccess,_p:cafPortAuthorizeControl,_q:cafPortReauthEnabled,_r:cafPortReauthInterval,_s:cafPortRestartInterval,_t:cafPortInactivityTimeout,_u:cafPortViolationAction,'cafPortMethodTable':cafPortMethodTable,'cafPortMethodEntry':cafPortMethodEntry,_v:cafPortMethodAdminExecOrder,_w:cafPortMethodAdminPriority,_x:cafPortMethodAvailable,_y:cafPortMethodOperExecOrder,_z:cafPortMethodOperPriority,'ciscoAuthFrameworkEvent':ciscoAuthFrameworkEvent,'cafAuthFailedEventPortTable':cafAuthFailedEventPortTable,'cafAuthFailedEventPortEntry':cafAuthFailedEventPortEntry,_A0:cafAuthFailedMaxRetry,_A1:cafAuthFailedNoActionEnabled,_A2:cafAuthFailedAuthorizedVlan,_A3:cafAuthFailedNextMethodEnabled,'cafClientNoRespEventPortTable':cafClientNoRespEventPortTable,'cafClientNoRespEventPortEntry':cafClientNoRespEventPortEntry,_A4:cafClientNoRespNoActionEnabled,_A5:cafClientNoRespAuthorizedVlan,'cafServerEventPortTable':cafServerEventPortTable,'cafServerEventPortEntry':cafServerEventPortEntry,_A6:cafServerDeadNoActionEnabled,_A7:cafServerDeadRemainAuthorized,_A8:cafServerDeadAuthorizedVlan,_A9:cafServerAliveAction,'ciscoAuthFrameworkSession':ciscoAuthFrameworkSession,'cafSessionTable':cafSessionTable,'cafSessionEntry':cafSessionEntry,_X:cafSessionId,_AA:cafSessionClientMacAddress,_AB:cafSessionClientAddrType,_AC:cafSessionClientAddress,_AE:cafSessionStatus,_AD:cafSessionDomain,_AF:cafSessionAuthHostMode,_AG:cafSessionControlledDirection,_AH:cafSessionPostureToken,_AI:cafSessionAuthUserName,_AJ:cafSessionClientFramedIpPool,_AK:cafSessionAuthorizedBy,_AL:cafSessionCriticalTimeLeft,_AM:cafSessionAuthVlan,_AN:cafSessionTimeout,_AO:cafSessionTimeLeft,_AP:cafSessionTimeoutAction,_AQ:cafSessionInactivityTimeout,_AR:cafSessionInactivityTimeLeft,_AS:cafSessionReauth,_AT:cafSessionTerminate,_AW:cafSessionVlanGroupName,'cafSessionMethodsInfoTable':cafSessionMethodsInfoTable,'cafSessionMethodsInfoEntry':cafSessionMethodsInfoEntry,_g:cafSessionMethod,_AU:cafSessionMethodState,'ciscoAuthFrwkNotifControl':ciscoAuthFrwkNotifControl,_AV:cafSecurityViolationNotifEnable,_Aa:cafAuthFailNotifEnable,'ciscoAuthFrwkNotifInfo':ciscoAuthFrwkNotifInfo,_Y:cafSecurityViolationClient,_Z:cafAuthFailClient,'ciscoAuthFrameworkMIBConform':ciscoAuthFrameworkMIBConform,'ciscoAuthFrameworkMIBCompliances':ciscoAuthFrameworkMIBCompliances,'ciscoAuthFrameworkMIBCompliance':ciscoAuthFrameworkMIBCompliance,'ciscoAuthFrameworkMIBCompliance2':ciscoAuthFrameworkMIBCompliance2,'ciscoAuthFrameworkMIBCompliance3':ciscoAuthFrameworkMIBCompliance3,'ciscoAuthFrameworkMIBCompliance4':ciscoAuthFrameworkMIBCompliance4,'ciscoAuthFrameworkMIBGroups':ciscoAuthFrameworkMIBGroups,_I:cafAuthMethodRegGroup,_N:cafAaaNoRespRecoveryDelayGroup,_J:cafAuthPortConfigGroup,_K:cafPortMethodGroup,_O:cafAuthFailedEventGroup,_P:cafClientNoRespEventGroup,_Q:cafServerEventGroup,_L:cafSessionGroup,_M:cafSessionMethodInfoGroup,_R:cafSecViolationNotifEnableGroup,_S:cafSecurityViolationNotifGroup,_T:cafSecurityViolationClientGroup,_U:cafSessionVlanGroupNameGroup,_b:cafMacMoveConfigGroup,_c:cafCoACommandConfigGroup,_Ad:cafAuthFailNotifGroup,_Ae:cafAuthFailNotifEnableGroup,_Af:cafAuthFailClientGroup})