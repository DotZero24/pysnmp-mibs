_Aj='etsysMultiAuthSystemGroup3'
_Ai='etsysMultiAuthSystemGroup2'
_Ah='etsysMultiAuthOutboundCounterGroup'
_Ag='etsysMultiAuthInboundCounterGroup'
_Af='etsysMultiAuthCounterEnableGroup'
_Ae='etsysMultiAuthTunnelAttributeGroup'
_Ad='etsysMultiAuthCurrentNumUsersGroup'
_Ac='etsysMultiAuthTimeoutGroup'
_Ab='etsysMultiAuthSystemMaxNumUsersReached'
_Aa='etsysMultiAuthModuleMaxNumUsersReached'
_AZ='etsysMultiAuthMaxNumUsersReached'
_AY='etsysMultiAuthTerminated'
_AX='etsysMultiAuthFailed'
_AW='etsysMultiAuthSuccess'
_AV='etsysMultiAuthSystemReAuthenticationTimeoutAction'
_AU='etsysMultiAuthSessionsUniquePerPortOperStatus'
_AT='etsysMultiAuthSessionClear'
_AS='etsysMultiAuthCounterOutboundPackets'
_AR='etsysMultiAuthCounterOutboundBytes'
_AQ='etsysMultiAuthCounterInboundPackets'
_AP='etsysMultiAuthCounterInboundBytes'
_AO='etsysMultiAuthCounterEnable'
_AN='etsysMultiAuthSessionVlanTunnelAttribute'
_AM='etsysMultiAuthSystemMaxNumUsersReachedTrapEnable'
_AL='etsysMultiAuthModuleMaxNumUsersReachedTrapEnable'
_AK='etsysMultiAuthPortTypeCurrentNumUsers'
_AJ='etsysMultiAuthCurrentNumUsers'
_AI='etsysMultiAuthSessionIdleTime'
_AH='etsysMultiAuthSessionDuration'
_AG='etsysMultiAuthSessionIdleTimeout'
_AF='etsysMultiAuthSessionSessionTimeout'
_AE='etsysMultiAuthIdleTimeout'
_AD='etsysMultiAuthSessionTimeout'
_AC='etsysMultiAuthModuleCurrentNumUsers'
_AB='etsysMultiAuthModuleMaxNumUsers'
_AA='etsysMultiAuthStationClearUsers'
_A9='etsysMultiAuthPortTrapEnable'
_A8='etsysMultiAuthPortClearUsers'
_A7='etsysMultiAuthPortCurrentNumUsers'
_A6='etsysMultiAuthPortNumUsersAllowed'
_A5='etsysMultiAuthPortMaxNumUsers'
_A4='etsysMultiAuthPortMode'
_A3='quarantineAgent'
_A2='autoTracking'
_A1='radiusSnooping'
_A0='ieee8021x'
_z='DateAndTime'
_y='etsysMultiAuthSessionGroup3'
_x='etsysMultiAuthSessionGroup2'
_w='etsysMultiAuthSessionGroup'
_v='etsysMultiAuthSessionsUniquePerPort'
_u='etsysMultiAuthSessionTerminationTime'
_t='EtsysMultiAuthTypePrecedence'
_s='Bits'
_r='entPhysicalIndex'
_q='ENTITY-MIB'
_p='etsysMultiAuthNotificationSystemGroup'
_o='etsysMultiAuthSystemTrapGroup'
_n='etsysMultiAuthNotificationModuleGroup'
_m='etsysMultiAuthModuleTrapGroup'
_l='etsysMultiAuthSessionPortAuthStatus'
_k='etsysMultiAuthSessionIsApplied'
_j='etsysMultiAuthSessionPolicyIndex'
_i='etsysMultiAuthSessionAuthServerAddr'
_h='etsysMultiAuthSessionAuthServerAddrType'
_g='etsysMultiAuthSessionAuthServerType'
_f='etsysMultiAuthSessionAuthAttemptTime'
_e='etsysMultiAuthSessionStationAuthStatus'
_d='etsysMultiAuthSystemOperPrecedence'
_c='etsysMultiAuthSystemAdminPrecedence'
_b='etsysMultiAuthSystemDefaultPrecedence'
_a='etsysMultiAuthSystemMode'
_Z='etsysMultiAuthSystemCurrentNumUsers'
_Y='etsysMultiAuthSystemMaxNumUsers'
_X='etsysMultiAuthSystemSupportedTypes'
_W='accessible-for-notify'
_V='etsysMultiAuthType'
_U='EnabledStatus'
_T='etsysMultiAuthSystemGroup'
_S='TruthValue'
_R='Unsigned32'
_Q='etsysMultiAuthModuleGroup'
_P='seconds'
_O='etsysMultiAuthNotificationPortGroup'
_N='etsysMultiAuthPortTrapGroup'
_M='etsysMultiAuthStationGroup'
_L='etsysMultiAuthPortBaseGroup'
_K='Integer32'
_J='deprecated'
_I='etsysMultiAuthSessionAgentType'
_H='etsysMultiAuthStationAddr'
_G='etsysMultiAuthStationAddrType'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='read-only'
_B='current'
_A='ENTERASYS-MULTI-AUTH-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
StationAddress,StationAddressType=mibBuilder.importSymbols('ENTERASYS-UPN-TC-MIB','StationAddress','StationAddressType')
entPhysicalIndex,=mibBuilder.importSymbols(_q,_r)
ifIndex,=mibBuilder.importSymbols(_E,_F)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_U)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_s,'Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_R,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_z,'DisplayString','PhysAddress','TextualConvention','TimeStamp',_S)
etsysMultiAuthMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,46))
if mibBuilder.loadTexts:etsysMultiAuthMIB.setRevisions(('2013-08-08 15:15','2013-01-07 14:38','2012-09-12 15:37','2012-05-31 18:33','2012-05-09 11:03','2008-02-05 18:40','2006-03-23 13:32','2006-02-03 19:15','2005-04-06 18:10','2004-08-30 13:43','2004-07-20 19:43','2004-03-10 13:56'))
class EtsysMultiAuthTypes(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_A0,1),('pwa',2),('macAuth',3),('cep',4),(_A1,5),(_A2,6),(_A3,7)))
class EtsysMultiAuthTypePrecedence(TextualConvention,OctetString):status=_B;displayHint='1d ';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class EtsysMultiAuthStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('authSuccess',1),('authFailed',2),('authInProgress',3),('authServerTimeout',4),('authTerminated',5)))
_EtsysMultiAuthObjects_ObjectIdentity=ObjectIdentity
etsysMultiAuthObjects=_EtsysMultiAuthObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,46,1))
_EtsysMultiAuthNotification_ObjectIdentity=ObjectIdentity
etsysMultiAuthNotification=_EtsysMultiAuthNotification_ObjectIdentity((1,3,6,1,4,1,5624,1,2,46,1,0))
_EtsysMultiAuthSystem_ObjectIdentity=ObjectIdentity
etsysMultiAuthSystem=_EtsysMultiAuthSystem_ObjectIdentity((1,3,6,1,4,1,5624,1,2,46,1,1))
class _EtsysMultiAuthSystemSupportedTypes_Type(Bits):namedValues=NamedValues(*((_A0,0),('pwa',1),('macAuth',2),('cep',3),(_A1,4),(_A2,5),(_A3,6)))
_EtsysMultiAuthSystemSupportedTypes_Type.__name__=_s
_EtsysMultiAuthSystemSupportedTypes_Object=MibScalar
etsysMultiAuthSystemSupportedTypes=_EtsysMultiAuthSystemSupportedTypes_Object((1,3,6,1,4,1,5624,1,2,46,1,1,1),_EtsysMultiAuthSystemSupportedTypes_Type())
etsysMultiAuthSystemSupportedTypes.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthSystemSupportedTypes.setStatus(_B)
_EtsysMultiAuthSystemMaxNumUsers_Type=Unsigned32
_EtsysMultiAuthSystemMaxNumUsers_Object=MibScalar
etsysMultiAuthSystemMaxNumUsers=_EtsysMultiAuthSystemMaxNumUsers_Object((1,3,6,1,4,1,5624,1,2,46,1,1,2),_EtsysMultiAuthSystemMaxNumUsers_Type())
etsysMultiAuthSystemMaxNumUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthSystemMaxNumUsers.setStatus(_B)
_EtsysMultiAuthSystemCurrentNumUsers_Type=Gauge32
_EtsysMultiAuthSystemCurrentNumUsers_Object=MibScalar
etsysMultiAuthSystemCurrentNumUsers=_EtsysMultiAuthSystemCurrentNumUsers_Object((1,3,6,1,4,1,5624,1,2,46,1,1,3),_EtsysMultiAuthSystemCurrentNumUsers_Type())
etsysMultiAuthSystemCurrentNumUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthSystemCurrentNumUsers.setStatus(_B)
class _EtsysMultiAuthSystemMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('strictIeee8021x',1),('etsysMultiAuth',2)))
_EtsysMultiAuthSystemMode_Type.__name__=_K
_EtsysMultiAuthSystemMode_Object=MibScalar
etsysMultiAuthSystemMode=_EtsysMultiAuthSystemMode_Object((1,3,6,1,4,1,5624,1,2,46,1,1,4),_EtsysMultiAuthSystemMode_Type())
etsysMultiAuthSystemMode.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMultiAuthSystemMode.setStatus(_B)
class _EtsysMultiAuthSystemDefaultPrecedence_Type(EtsysMultiAuthTypePrecedence):defaultHexValue='07010203040506'
_EtsysMultiAuthSystemDefaultPrecedence_Type.__name__=_t
_EtsysMultiAuthSystemDefaultPrecedence_Object=MibScalar
etsysMultiAuthSystemDefaultPrecedence=_EtsysMultiAuthSystemDefaultPrecedence_Object((1,3,6,1,4,1,5624,1,2,46,1,1,5),_EtsysMultiAuthSystemDefaultPrecedence_Type())
etsysMultiAuthSystemDefaultPrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthSystemDefaultPrecedence.setStatus(_B)
class _EtsysMultiAuthSystemAdminPrecedence_Type(EtsysMultiAuthTypePrecedence):defaultHexValue=''
_EtsysMultiAuthSystemAdminPrecedence_Type.__name__=_t
_EtsysMultiAuthSystemAdminPrecedence_Object=MibScalar
etsysMultiAuthSystemAdminPrecedence=_EtsysMultiAuthSystemAdminPrecedence_Object((1,3,6,1,4,1,5624,1,2,46,1,1,6),_EtsysMultiAuthSystemAdminPrecedence_Type())
etsysMultiAuthSystemAdminPrecedence.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMultiAuthSystemAdminPrecedence.setStatus(_B)
_EtsysMultiAuthSystemOperPrecedence_Type=EtsysMultiAuthTypePrecedence
_EtsysMultiAuthSystemOperPrecedence_Object=MibScalar
etsysMultiAuthSystemOperPrecedence=_EtsysMultiAuthSystemOperPrecedence_Object((1,3,6,1,4,1,5624,1,2,46,1,1,7),_EtsysMultiAuthSystemOperPrecedence_Type())
etsysMultiAuthSystemOperPrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthSystemOperPrecedence.setStatus(_B)
_EtsysMultiAuthTypePropertiesTable_Object=MibTable
etsysMultiAuthTypePropertiesTable=_EtsysMultiAuthTypePropertiesTable_Object((1,3,6,1,4,1,5624,1,2,46,1,1,8))
if mibBuilder.loadTexts:etsysMultiAuthTypePropertiesTable.setStatus(_B)
_EtsysMultiAuthTypePropertiesEntry_Object=MibTableRow
etsysMultiAuthTypePropertiesEntry=_EtsysMultiAuthTypePropertiesEntry_Object((1,3,6,1,4,1,5624,1,2,46,1,1,8,1))
etsysMultiAuthTypePropertiesEntry.setIndexNames((0,_A,_V))
if mibBuilder.loadTexts:etsysMultiAuthTypePropertiesEntry.setStatus(_B)
_EtsysMultiAuthType_Type=EtsysMultiAuthTypes
_EtsysMultiAuthType_Object=MibTableColumn
etsysMultiAuthType=_EtsysMultiAuthType_Object((1,3,6,1,4,1,5624,1,2,46,1,1,8,1,1),_EtsysMultiAuthType_Type())
etsysMultiAuthType.setMaxAccess(_W)
if mibBuilder.loadTexts:etsysMultiAuthType.setStatus(_B)
class _EtsysMultiAuthSessionTimeout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,172800))
_EtsysMultiAuthSessionTimeout_Type.__name__=_R
_EtsysMultiAuthSessionTimeout_Object=MibTableColumn
etsysMultiAuthSessionTimeout=_EtsysMultiAuthSessionTimeout_Object((1,3,6,1,4,1,5624,1,2,46,1,1,8,1,2),_EtsysMultiAuthSessionTimeout_Type())
etsysMultiAuthSessionTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMultiAuthSessionTimeout.setStatus(_B)
if mibBuilder.loadTexts:etsysMultiAuthSessionTimeout.setUnits(_P)
class _EtsysMultiAuthIdleTimeout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,172800))
_EtsysMultiAuthIdleTimeout_Type.__name__=_R
_EtsysMultiAuthIdleTimeout_Object=MibTableColumn
etsysMultiAuthIdleTimeout=_EtsysMultiAuthIdleTimeout_Object((1,3,6,1,4,1,5624,1,2,46,1,1,8,1,3),_EtsysMultiAuthIdleTimeout_Type())
etsysMultiAuthIdleTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMultiAuthIdleTimeout.setStatus(_B)
if mibBuilder.loadTexts:etsysMultiAuthIdleTimeout.setUnits(_P)
_EtsysMultiAuthCurrentNumUsers_Type=Gauge32
_EtsysMultiAuthCurrentNumUsers_Object=MibTableColumn
etsysMultiAuthCurrentNumUsers=_EtsysMultiAuthCurrentNumUsers_Object((1,3,6,1,4,1,5624,1,2,46,1,1,8,1,4),_EtsysMultiAuthCurrentNumUsers_Type())
etsysMultiAuthCurrentNumUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthCurrentNumUsers.setStatus(_B)
class _EtsysMultiAuthSystemMaxNumUsersReachedTrapEnable_Type(EnabledStatus):defaultValue=2
_EtsysMultiAuthSystemMaxNumUsersReachedTrapEnable_Type.__name__=_U
_EtsysMultiAuthSystemMaxNumUsersReachedTrapEnable_Object=MibScalar
etsysMultiAuthSystemMaxNumUsersReachedTrapEnable=_EtsysMultiAuthSystemMaxNumUsersReachedTrapEnable_Object((1,3,6,1,4,1,5624,1,2,46,1,1,9),_EtsysMultiAuthSystemMaxNumUsersReachedTrapEnable_Type())
etsysMultiAuthSystemMaxNumUsersReachedTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMultiAuthSystemMaxNumUsersReachedTrapEnable.setStatus(_B)
class _EtsysMultiAuthSessionsUniquePerPort_Type(TruthValue):defaultValue=2
_EtsysMultiAuthSessionsUniquePerPort_Type.__name__=_S
_EtsysMultiAuthSessionsUniquePerPort_Object=MibScalar
etsysMultiAuthSessionsUniquePerPort=_EtsysMultiAuthSessionsUniquePerPort_Object((1,3,6,1,4,1,5624,1,2,46,1,1,10),_EtsysMultiAuthSessionsUniquePerPort_Type())
etsysMultiAuthSessionsUniquePerPort.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMultiAuthSessionsUniquePerPort.setStatus(_B)
_EtsysMultiAuthSessionsUniquePerPortOperStatus_Type=TruthValue
_EtsysMultiAuthSessionsUniquePerPortOperStatus_Object=MibScalar
etsysMultiAuthSessionsUniquePerPortOperStatus=_EtsysMultiAuthSessionsUniquePerPortOperStatus_Object((1,3,6,1,4,1,5624,1,2,46,1,1,11),_EtsysMultiAuthSessionsUniquePerPortOperStatus_Type())
etsysMultiAuthSessionsUniquePerPortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthSessionsUniquePerPortOperStatus.setStatus(_B)
class _EtsysMultiAuthSystemReAuthenticationTimeoutAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('terminate',1),('none',2)))
_EtsysMultiAuthSystemReAuthenticationTimeoutAction_Type.__name__=_K
_EtsysMultiAuthSystemReAuthenticationTimeoutAction_Object=MibScalar
etsysMultiAuthSystemReAuthenticationTimeoutAction=_EtsysMultiAuthSystemReAuthenticationTimeoutAction_Object((1,3,6,1,4,1,5624,1,2,46,1,1,12),_EtsysMultiAuthSystemReAuthenticationTimeoutAction_Type())
etsysMultiAuthSystemReAuthenticationTimeoutAction.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMultiAuthSystemReAuthenticationTimeoutAction.setStatus(_B)
_EtsysMultiAuthPort_ObjectIdentity=ObjectIdentity
etsysMultiAuthPort=_EtsysMultiAuthPort_ObjectIdentity((1,3,6,1,4,1,5624,1,2,46,1,2))
_EtsysMultiAuthPortTable_Object=MibTable
etsysMultiAuthPortTable=_EtsysMultiAuthPortTable_Object((1,3,6,1,4,1,5624,1,2,46,1,2,1))
if mibBuilder.loadTexts:etsysMultiAuthPortTable.setStatus(_B)
_EtsysMultiAuthPortEntry_Object=MibTableRow
etsysMultiAuthPortEntry=_EtsysMultiAuthPortEntry_Object((1,3,6,1,4,1,5624,1,2,46,1,2,1,1))
etsysMultiAuthPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:etsysMultiAuthPortEntry.setStatus(_B)
class _EtsysMultiAuthPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('forceUnauthorized',1),('forceAuthorized',2),('authOptional',3),('authRequired',4)))
_EtsysMultiAuthPortMode_Type.__name__=_K
_EtsysMultiAuthPortMode_Object=MibTableColumn
etsysMultiAuthPortMode=_EtsysMultiAuthPortMode_Object((1,3,6,1,4,1,5624,1,2,46,1,2,1,1,1),_EtsysMultiAuthPortMode_Type())
etsysMultiAuthPortMode.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMultiAuthPortMode.setStatus(_B)
_EtsysMultiAuthPortMaxNumUsers_Type=Unsigned32
_EtsysMultiAuthPortMaxNumUsers_Object=MibTableColumn
etsysMultiAuthPortMaxNumUsers=_EtsysMultiAuthPortMaxNumUsers_Object((1,3,6,1,4,1,5624,1,2,46,1,2,1,1,2),_EtsysMultiAuthPortMaxNumUsers_Type())
etsysMultiAuthPortMaxNumUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthPortMaxNumUsers.setStatus(_B)
_EtsysMultiAuthPortNumUsersAllowed_Type=Unsigned32
_EtsysMultiAuthPortNumUsersAllowed_Object=MibTableColumn
etsysMultiAuthPortNumUsersAllowed=_EtsysMultiAuthPortNumUsersAllowed_Object((1,3,6,1,4,1,5624,1,2,46,1,2,1,1,3),_EtsysMultiAuthPortNumUsersAllowed_Type())
etsysMultiAuthPortNumUsersAllowed.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMultiAuthPortNumUsersAllowed.setStatus(_B)
_EtsysMultiAuthPortCurrentNumUsers_Type=Gauge32
_EtsysMultiAuthPortCurrentNumUsers_Object=MibTableColumn
etsysMultiAuthPortCurrentNumUsers=_EtsysMultiAuthPortCurrentNumUsers_Object((1,3,6,1,4,1,5624,1,2,46,1,2,1,1,4),_EtsysMultiAuthPortCurrentNumUsers_Type())
etsysMultiAuthPortCurrentNumUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthPortCurrentNumUsers.setStatus(_B)
class _EtsysMultiAuthPortClearUsers_Type(TruthValue):defaultValue=2
_EtsysMultiAuthPortClearUsers_Type.__name__=_S
_EtsysMultiAuthPortClearUsers_Object=MibTableColumn
etsysMultiAuthPortClearUsers=_EtsysMultiAuthPortClearUsers_Object((1,3,6,1,4,1,5624,1,2,46,1,2,1,1,5),_EtsysMultiAuthPortClearUsers_Type())
etsysMultiAuthPortClearUsers.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMultiAuthPortClearUsers.setStatus(_B)
class _EtsysMultiAuthPortTrapEnable_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('authSuccessTrap',0),('authFailedTrap',1),('authTerminatedTrap',2),('maxNumUsersReachedTrap',3)))
_EtsysMultiAuthPortTrapEnable_Type.__name__=_s
_EtsysMultiAuthPortTrapEnable_Object=MibTableColumn
etsysMultiAuthPortTrapEnable=_EtsysMultiAuthPortTrapEnable_Object((1,3,6,1,4,1,5624,1,2,46,1,2,1,1,6),_EtsysMultiAuthPortTrapEnable_Type())
etsysMultiAuthPortTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMultiAuthPortTrapEnable.setStatus(_B)
_EtsysMultiAuthPortTypeTable_Object=MibTable
etsysMultiAuthPortTypeTable=_EtsysMultiAuthPortTypeTable_Object((1,3,6,1,4,1,5624,1,2,46,1,2,2))
if mibBuilder.loadTexts:etsysMultiAuthPortTypeTable.setStatus(_B)
_EtsysMultiAuthPortTypeEntry_Object=MibTableRow
etsysMultiAuthPortTypeEntry=_EtsysMultiAuthPortTypeEntry_Object((1,3,6,1,4,1,5624,1,2,46,1,2,2,1))
etsysMultiAuthPortTypeEntry.setIndexNames((0,_E,_F),(0,_A,_V))
if mibBuilder.loadTexts:etsysMultiAuthPortTypeEntry.setStatus(_B)
_EtsysMultiAuthPortTypeCurrentNumUsers_Type=Gauge32
_EtsysMultiAuthPortTypeCurrentNumUsers_Object=MibTableColumn
etsysMultiAuthPortTypeCurrentNumUsers=_EtsysMultiAuthPortTypeCurrentNumUsers_Object((1,3,6,1,4,1,5624,1,2,46,1,2,2,1,1),_EtsysMultiAuthPortTypeCurrentNumUsers_Type())
etsysMultiAuthPortTypeCurrentNumUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthPortTypeCurrentNumUsers.setStatus(_B)
_EtsysMultiAuthStation_ObjectIdentity=ObjectIdentity
etsysMultiAuthStation=_EtsysMultiAuthStation_ObjectIdentity((1,3,6,1,4,1,5624,1,2,46,1,3))
_EtsysMultiAuthStationTable_Object=MibTable
etsysMultiAuthStationTable=_EtsysMultiAuthStationTable_Object((1,3,6,1,4,1,5624,1,2,46,1,3,1))
if mibBuilder.loadTexts:etsysMultiAuthStationTable.setStatus(_B)
_EtsysMultiAuthStationEntry_Object=MibTableRow
etsysMultiAuthStationEntry=_EtsysMultiAuthStationEntry_Object((1,3,6,1,4,1,5624,1,2,46,1,3,1,1))
etsysMultiAuthStationEntry.setIndexNames((0,_A,_G),(0,_A,_H),(0,_E,_F))
if mibBuilder.loadTexts:etsysMultiAuthStationEntry.setStatus(_B)
_EtsysMultiAuthStationAddrType_Type=StationAddressType
_EtsysMultiAuthStationAddrType_Object=MibTableColumn
etsysMultiAuthStationAddrType=_EtsysMultiAuthStationAddrType_Object((1,3,6,1,4,1,5624,1,2,46,1,3,1,1,1),_EtsysMultiAuthStationAddrType_Type())
etsysMultiAuthStationAddrType.setMaxAccess(_W)
if mibBuilder.loadTexts:etsysMultiAuthStationAddrType.setStatus(_B)
_EtsysMultiAuthStationAddr_Type=StationAddress
_EtsysMultiAuthStationAddr_Object=MibTableColumn
etsysMultiAuthStationAddr=_EtsysMultiAuthStationAddr_Object((1,3,6,1,4,1,5624,1,2,46,1,3,1,1,2),_EtsysMultiAuthStationAddr_Type())
etsysMultiAuthStationAddr.setMaxAccess(_W)
if mibBuilder.loadTexts:etsysMultiAuthStationAddr.setStatus(_B)
class _EtsysMultiAuthStationClearUsers_Type(TruthValue):defaultValue=2
_EtsysMultiAuthStationClearUsers_Type.__name__=_S
_EtsysMultiAuthStationClearUsers_Object=MibTableColumn
etsysMultiAuthStationClearUsers=_EtsysMultiAuthStationClearUsers_Object((1,3,6,1,4,1,5624,1,2,46,1,3,1,1,3),_EtsysMultiAuthStationClearUsers_Type())
etsysMultiAuthStationClearUsers.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMultiAuthStationClearUsers.setStatus(_B)
_EtsysMultiAuthSession_ObjectIdentity=ObjectIdentity
etsysMultiAuthSession=_EtsysMultiAuthSession_ObjectIdentity((1,3,6,1,4,1,5624,1,2,46,1,4))
_EtsysMultiAuthSessionStationTable_Object=MibTable
etsysMultiAuthSessionStationTable=_EtsysMultiAuthSessionStationTable_Object((1,3,6,1,4,1,5624,1,2,46,1,4,1))
if mibBuilder.loadTexts:etsysMultiAuthSessionStationTable.setStatus(_B)
_EtsysMultiAuthSessionStationEntry_Object=MibTableRow
etsysMultiAuthSessionStationEntry=_EtsysMultiAuthSessionStationEntry_Object((1,3,6,1,4,1,5624,1,2,46,1,4,1,1))
etsysMultiAuthSessionStationEntry.setIndexNames((0,_A,_G),(0,_A,_H),(0,_E,_F),(0,_A,_I))
if mibBuilder.loadTexts:etsysMultiAuthSessionStationEntry.setStatus(_B)
_EtsysMultiAuthSessionAgentType_Type=EtsysMultiAuthTypes
_EtsysMultiAuthSessionAgentType_Object=MibTableColumn
etsysMultiAuthSessionAgentType=_EtsysMultiAuthSessionAgentType_Object((1,3,6,1,4,1,5624,1,2,46,1,4,1,1,1),_EtsysMultiAuthSessionAgentType_Type())
etsysMultiAuthSessionAgentType.setMaxAccess(_W)
if mibBuilder.loadTexts:etsysMultiAuthSessionAgentType.setStatus(_B)
_EtsysMultiAuthSessionStationAuthStatus_Type=EtsysMultiAuthStatus
_EtsysMultiAuthSessionStationAuthStatus_Object=MibTableColumn
etsysMultiAuthSessionStationAuthStatus=_EtsysMultiAuthSessionStationAuthStatus_Object((1,3,6,1,4,1,5624,1,2,46,1,4,1,1,2),_EtsysMultiAuthSessionStationAuthStatus_Type())
etsysMultiAuthSessionStationAuthStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthSessionStationAuthStatus.setStatus(_B)
_EtsysMultiAuthSessionAuthAttemptTime_Type=TimeStamp
_EtsysMultiAuthSessionAuthAttemptTime_Object=MibTableColumn
etsysMultiAuthSessionAuthAttemptTime=_EtsysMultiAuthSessionAuthAttemptTime_Object((1,3,6,1,4,1,5624,1,2,46,1,4,1,1,3),_EtsysMultiAuthSessionAuthAttemptTime_Type())
etsysMultiAuthSessionAuthAttemptTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthSessionAuthAttemptTime.setStatus(_B)
class _EtsysMultiAuthSessionAuthServerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('radius',1),('local',2)))
_EtsysMultiAuthSessionAuthServerType_Type.__name__=_K
_EtsysMultiAuthSessionAuthServerType_Object=MibTableColumn
etsysMultiAuthSessionAuthServerType=_EtsysMultiAuthSessionAuthServerType_Object((1,3,6,1,4,1,5624,1,2,46,1,4,1,1,4),_EtsysMultiAuthSessionAuthServerType_Type())
etsysMultiAuthSessionAuthServerType.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthSessionAuthServerType.setStatus(_B)
_EtsysMultiAuthSessionAuthServerAddrType_Type=InetAddressType
_EtsysMultiAuthSessionAuthServerAddrType_Object=MibTableColumn
etsysMultiAuthSessionAuthServerAddrType=_EtsysMultiAuthSessionAuthServerAddrType_Object((1,3,6,1,4,1,5624,1,2,46,1,4,1,1,5),_EtsysMultiAuthSessionAuthServerAddrType_Type())
etsysMultiAuthSessionAuthServerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthSessionAuthServerAddrType.setStatus(_B)
_EtsysMultiAuthSessionAuthServerAddr_Type=InetAddress
_EtsysMultiAuthSessionAuthServerAddr_Object=MibTableColumn
etsysMultiAuthSessionAuthServerAddr=_EtsysMultiAuthSessionAuthServerAddr_Object((1,3,6,1,4,1,5624,1,2,46,1,4,1,1,6),_EtsysMultiAuthSessionAuthServerAddr_Type())
etsysMultiAuthSessionAuthServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthSessionAuthServerAddr.setStatus(_B)
class _EtsysMultiAuthSessionPolicyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,65535))
_EtsysMultiAuthSessionPolicyIndex_Type.__name__=_K
_EtsysMultiAuthSessionPolicyIndex_Object=MibTableColumn
etsysMultiAuthSessionPolicyIndex=_EtsysMultiAuthSessionPolicyIndex_Object((1,3,6,1,4,1,5624,1,2,46,1,4,1,1,7),_EtsysMultiAuthSessionPolicyIndex_Type())
etsysMultiAuthSessionPolicyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthSessionPolicyIndex.setStatus(_B)
_EtsysMultiAuthSessionIsApplied_Type=TruthValue
_EtsysMultiAuthSessionIsApplied_Object=MibTableColumn
etsysMultiAuthSessionIsApplied=_EtsysMultiAuthSessionIsApplied_Object((1,3,6,1,4,1,5624,1,2,46,1,4,1,1,8),_EtsysMultiAuthSessionIsApplied_Type())
etsysMultiAuthSessionIsApplied.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthSessionIsApplied.setStatus(_B)
class _EtsysMultiAuthSessionTerminationTime_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_EtsysMultiAuthSessionTerminationTime_Type.__name__=_z
_EtsysMultiAuthSessionTerminationTime_Object=MibTableColumn
etsysMultiAuthSessionTerminationTime=_EtsysMultiAuthSessionTerminationTime_Object((1,3,6,1,4,1,5624,1,2,46,1,4,1,1,9),_EtsysMultiAuthSessionTerminationTime_Type())
etsysMultiAuthSessionTerminationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthSessionTerminationTime.setStatus(_B)
class _EtsysMultiAuthSessionSessionTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,172800))
_EtsysMultiAuthSessionSessionTimeout_Type.__name__=_R
_EtsysMultiAuthSessionSessionTimeout_Object=MibTableColumn
etsysMultiAuthSessionSessionTimeout=_EtsysMultiAuthSessionSessionTimeout_Object((1,3,6,1,4,1,5624,1,2,46,1,4,1,1,10),_EtsysMultiAuthSessionSessionTimeout_Type())
etsysMultiAuthSessionSessionTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthSessionSessionTimeout.setStatus(_B)
if mibBuilder.loadTexts:etsysMultiAuthSessionSessionTimeout.setUnits(_P)
class _EtsysMultiAuthSessionIdleTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,172800))
_EtsysMultiAuthSessionIdleTimeout_Type.__name__=_R
_EtsysMultiAuthSessionIdleTimeout_Object=MibTableColumn
etsysMultiAuthSessionIdleTimeout=_EtsysMultiAuthSessionIdleTimeout_Object((1,3,6,1,4,1,5624,1,2,46,1,4,1,1,11),_EtsysMultiAuthSessionIdleTimeout_Type())
etsysMultiAuthSessionIdleTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthSessionIdleTimeout.setStatus(_B)
if mibBuilder.loadTexts:etsysMultiAuthSessionIdleTimeout.setUnits(_P)
_EtsysMultiAuthSessionDuration_Type=Gauge32
_EtsysMultiAuthSessionDuration_Object=MibTableColumn
etsysMultiAuthSessionDuration=_EtsysMultiAuthSessionDuration_Object((1,3,6,1,4,1,5624,1,2,46,1,4,1,1,12),_EtsysMultiAuthSessionDuration_Type())
etsysMultiAuthSessionDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthSessionDuration.setStatus(_B)
if mibBuilder.loadTexts:etsysMultiAuthSessionDuration.setUnits(_P)
_EtsysMultiAuthSessionIdleTime_Type=Gauge32
_EtsysMultiAuthSessionIdleTime_Object=MibTableColumn
etsysMultiAuthSessionIdleTime=_EtsysMultiAuthSessionIdleTime_Object((1,3,6,1,4,1,5624,1,2,46,1,4,1,1,13),_EtsysMultiAuthSessionIdleTime_Type())
etsysMultiAuthSessionIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthSessionIdleTime.setStatus(_B)
if mibBuilder.loadTexts:etsysMultiAuthSessionIdleTime.setUnits(_P)
class _EtsysMultiAuthSessionVlanTunnelAttribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4094),ValueRangeConstraint(4095,4095))
_EtsysMultiAuthSessionVlanTunnelAttribute_Type.__name__=_K
_EtsysMultiAuthSessionVlanTunnelAttribute_Object=MibTableColumn
etsysMultiAuthSessionVlanTunnelAttribute=_EtsysMultiAuthSessionVlanTunnelAttribute_Object((1,3,6,1,4,1,5624,1,2,46,1,4,1,1,14),_EtsysMultiAuthSessionVlanTunnelAttribute_Type())
etsysMultiAuthSessionVlanTunnelAttribute.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthSessionVlanTunnelAttribute.setStatus(_B)
class _EtsysMultiAuthSessionClear_Type(TruthValue):defaultValue=2
_EtsysMultiAuthSessionClear_Type.__name__=_S
_EtsysMultiAuthSessionClear_Object=MibTableColumn
etsysMultiAuthSessionClear=_EtsysMultiAuthSessionClear_Object((1,3,6,1,4,1,5624,1,2,46,1,4,1,1,15),_EtsysMultiAuthSessionClear_Type())
etsysMultiAuthSessionClear.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMultiAuthSessionClear.setStatus(_B)
_EtsysMultiAuthSessionPortTable_Object=MibTable
etsysMultiAuthSessionPortTable=_EtsysMultiAuthSessionPortTable_Object((1,3,6,1,4,1,5624,1,2,46,1,4,2))
if mibBuilder.loadTexts:etsysMultiAuthSessionPortTable.setStatus(_B)
_EtsysMultiAuthSessionPortEntry_Object=MibTableRow
etsysMultiAuthSessionPortEntry=_EtsysMultiAuthSessionPortEntry_Object((1,3,6,1,4,1,5624,1,2,46,1,4,2,1))
etsysMultiAuthSessionPortEntry.setIndexNames((0,_E,_F),(0,_A,_G),(0,_A,_H),(0,_A,_I))
if mibBuilder.loadTexts:etsysMultiAuthSessionPortEntry.setStatus(_B)
_EtsysMultiAuthSessionPortAuthStatus_Type=EtsysMultiAuthStatus
_EtsysMultiAuthSessionPortAuthStatus_Object=MibTableColumn
etsysMultiAuthSessionPortAuthStatus=_EtsysMultiAuthSessionPortAuthStatus_Object((1,3,6,1,4,1,5624,1,2,46,1,4,2,1,1),_EtsysMultiAuthSessionPortAuthStatus_Type())
etsysMultiAuthSessionPortAuthStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthSessionPortAuthStatus.setStatus(_B)
_EtsysMultiAuthModule_ObjectIdentity=ObjectIdentity
etsysMultiAuthModule=_EtsysMultiAuthModule_ObjectIdentity((1,3,6,1,4,1,5624,1,2,46,1,5))
_EtsysMultiAuthModuleTable_Object=MibTable
etsysMultiAuthModuleTable=_EtsysMultiAuthModuleTable_Object((1,3,6,1,4,1,5624,1,2,46,1,5,1))
if mibBuilder.loadTexts:etsysMultiAuthModuleTable.setStatus(_B)
_EtsysMultiAuthModuleEntry_Object=MibTableRow
etsysMultiAuthModuleEntry=_EtsysMultiAuthModuleEntry_Object((1,3,6,1,4,1,5624,1,2,46,1,5,1,1))
etsysMultiAuthModuleEntry.setIndexNames((0,_q,_r))
if mibBuilder.loadTexts:etsysMultiAuthModuleEntry.setStatus(_B)
_EtsysMultiAuthModuleMaxNumUsers_Type=Unsigned32
_EtsysMultiAuthModuleMaxNumUsers_Object=MibTableColumn
etsysMultiAuthModuleMaxNumUsers=_EtsysMultiAuthModuleMaxNumUsers_Object((1,3,6,1,4,1,5624,1,2,46,1,5,1,1,1),_EtsysMultiAuthModuleMaxNumUsers_Type())
etsysMultiAuthModuleMaxNumUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthModuleMaxNumUsers.setStatus(_B)
_EtsysMultiAuthModuleCurrentNumUsers_Type=Gauge32
_EtsysMultiAuthModuleCurrentNumUsers_Object=MibTableColumn
etsysMultiAuthModuleCurrentNumUsers=_EtsysMultiAuthModuleCurrentNumUsers_Object((1,3,6,1,4,1,5624,1,2,46,1,5,1,1,2),_EtsysMultiAuthModuleCurrentNumUsers_Type())
etsysMultiAuthModuleCurrentNumUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthModuleCurrentNumUsers.setStatus(_B)
class _EtsysMultiAuthModuleMaxNumUsersReachedTrapEnable_Type(EnabledStatus):defaultValue=2
_EtsysMultiAuthModuleMaxNumUsersReachedTrapEnable_Type.__name__=_U
_EtsysMultiAuthModuleMaxNumUsersReachedTrapEnable_Object=MibScalar
etsysMultiAuthModuleMaxNumUsersReachedTrapEnable=_EtsysMultiAuthModuleMaxNumUsersReachedTrapEnable_Object((1,3,6,1,4,1,5624,1,2,46,1,5,2),_EtsysMultiAuthModuleMaxNumUsersReachedTrapEnable_Type())
etsysMultiAuthModuleMaxNumUsersReachedTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMultiAuthModuleMaxNumUsersReachedTrapEnable.setStatus(_B)
_EtsysMultiAuthCounters_ObjectIdentity=ObjectIdentity
etsysMultiAuthCounters=_EtsysMultiAuthCounters_ObjectIdentity((1,3,6,1,4,1,5624,1,2,46,1,6))
_EtsysMultiAuthCounterTable_Object=MibTable
etsysMultiAuthCounterTable=_EtsysMultiAuthCounterTable_Object((1,3,6,1,4,1,5624,1,2,46,1,6,1))
if mibBuilder.loadTexts:etsysMultiAuthCounterTable.setStatus(_B)
_EtsysMultiAuthCounterEntry_Object=MibTableRow
etsysMultiAuthCounterEntry=_EtsysMultiAuthCounterEntry_Object((1,3,6,1,4,1,5624,1,2,46,1,6,1,1))
etsysMultiAuthCounterEntry.setIndexNames((0,_E,_F),(0,_A,_G),(0,_A,_H))
if mibBuilder.loadTexts:etsysMultiAuthCounterEntry.setStatus(_B)
_EtsysMultiAuthCounterInboundBytes_Type=Counter64
_EtsysMultiAuthCounterInboundBytes_Object=MibTableColumn
etsysMultiAuthCounterInboundBytes=_EtsysMultiAuthCounterInboundBytes_Object((1,3,6,1,4,1,5624,1,2,46,1,6,1,1,1),_EtsysMultiAuthCounterInboundBytes_Type())
etsysMultiAuthCounterInboundBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthCounterInboundBytes.setStatus(_B)
_EtsysMultiAuthCounterInboundPackets_Type=Counter64
_EtsysMultiAuthCounterInboundPackets_Object=MibTableColumn
etsysMultiAuthCounterInboundPackets=_EtsysMultiAuthCounterInboundPackets_Object((1,3,6,1,4,1,5624,1,2,46,1,6,1,1,2),_EtsysMultiAuthCounterInboundPackets_Type())
etsysMultiAuthCounterInboundPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthCounterInboundPackets.setStatus(_B)
_EtsysMultiAuthCounterOutboundBytes_Type=Counter64
_EtsysMultiAuthCounterOutboundBytes_Object=MibTableColumn
etsysMultiAuthCounterOutboundBytes=_EtsysMultiAuthCounterOutboundBytes_Object((1,3,6,1,4,1,5624,1,2,46,1,6,1,1,3),_EtsysMultiAuthCounterOutboundBytes_Type())
etsysMultiAuthCounterOutboundBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthCounterOutboundBytes.setStatus(_B)
_EtsysMultiAuthCounterOutboundPackets_Type=Counter64
_EtsysMultiAuthCounterOutboundPackets_Object=MibTableColumn
etsysMultiAuthCounterOutboundPackets=_EtsysMultiAuthCounterOutboundPackets_Object((1,3,6,1,4,1,5624,1,2,46,1,6,1,1,4),_EtsysMultiAuthCounterOutboundPackets_Type())
etsysMultiAuthCounterOutboundPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMultiAuthCounterOutboundPackets.setStatus(_B)
class _EtsysMultiAuthCounterEnable_Type(EnabledStatus):defaultValue=2
_EtsysMultiAuthCounterEnable_Type.__name__=_U
_EtsysMultiAuthCounterEnable_Object=MibScalar
etsysMultiAuthCounterEnable=_EtsysMultiAuthCounterEnable_Object((1,3,6,1,4,1,5624,1,2,46,1,6,2),_EtsysMultiAuthCounterEnable_Type())
etsysMultiAuthCounterEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMultiAuthCounterEnable.setStatus(_B)
_EtsysMultiAuthConformance_ObjectIdentity=ObjectIdentity
etsysMultiAuthConformance=_EtsysMultiAuthConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,46,2))
_EtsysMultiAuthGroups_ObjectIdentity=ObjectIdentity
etsysMultiAuthGroups=_EtsysMultiAuthGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,46,2,1))
_EtsysMultiAuthCompliances_ObjectIdentity=ObjectIdentity
etsysMultiAuthCompliances=_EtsysMultiAuthCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,46,2,2))
etsysMultiAuthSystemGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,46,2,1,1))
etsysMultiAuthSystemGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:etsysMultiAuthSystemGroup.setStatus(_J)
etsysMultiAuthPortBaseGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,46,2,1,2))
etsysMultiAuthPortBaseGroup.setObjects(*((_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:etsysMultiAuthPortBaseGroup.setStatus(_B)
etsysMultiAuthPortTrapGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,46,2,1,3))
etsysMultiAuthPortTrapGroup.setObjects((_A,_A9))
if mibBuilder.loadTexts:etsysMultiAuthPortTrapGroup.setStatus(_B)
etsysMultiAuthStationGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,46,2,1,4))
etsysMultiAuthStationGroup.setObjects(*((_A,_G),(_A,_H),(_A,_AA)))
if mibBuilder.loadTexts:etsysMultiAuthStationGroup.setStatus(_B)
etsysMultiAuthSessionGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,46,2,1,5))
etsysMultiAuthSessionGroup.setObjects(*((_A,_I),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:etsysMultiAuthSessionGroup.setStatus(_J)
etsysMultiAuthModuleGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,46,2,1,7))
etsysMultiAuthModuleGroup.setObjects(*((_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:etsysMultiAuthModuleGroup.setStatus(_B)
etsysMultiAuthSessionGroup2=ObjectGroup((1,3,6,1,4,1,5624,1,2,46,2,1,8))
etsysMultiAuthSessionGroup2.setObjects(*((_A,_I),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_u),(_A,_l)))
if mibBuilder.loadTexts:etsysMultiAuthSessionGroup2.setStatus(_J)
etsysMultiAuthTimeoutGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,46,2,1,9))
etsysMultiAuthTimeoutGroup.setObjects(*((_A,_V),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:etsysMultiAuthTimeoutGroup.setStatus(_B)
etsysMultiAuthCurrentNumUsersGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,46,2,1,10))
etsysMultiAuthCurrentNumUsersGroup.setObjects(*((_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:etsysMultiAuthCurrentNumUsersGroup.setStatus(_B)
etsysMultiAuthModuleTrapGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,46,2,1,11))
etsysMultiAuthModuleTrapGroup.setObjects((_A,_AL))
if mibBuilder.loadTexts:etsysMultiAuthModuleTrapGroup.setStatus(_B)
etsysMultiAuthSystemTrapGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,46,2,1,12))
etsysMultiAuthSystemTrapGroup.setObjects((_A,_AM))
if mibBuilder.loadTexts:etsysMultiAuthSystemTrapGroup.setStatus(_B)
etsysMultiAuthTunnelAttributeGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,46,2,1,15))
etsysMultiAuthTunnelAttributeGroup.setObjects((_A,_AN))
if mibBuilder.loadTexts:etsysMultiAuthTunnelAttributeGroup.setStatus(_B)
etsysMultiAuthCounterEnableGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,46,2,1,16))
etsysMultiAuthCounterEnableGroup.setObjects((_A,_AO))
if mibBuilder.loadTexts:etsysMultiAuthCounterEnableGroup.setStatus(_B)
etsysMultiAuthInboundCounterGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,46,2,1,17))
etsysMultiAuthInboundCounterGroup.setObjects(*((_A,_AP),(_A,_AQ)))
if mibBuilder.loadTexts:etsysMultiAuthInboundCounterGroup.setStatus(_B)
etsysMultiAuthOutboundCounterGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,46,2,1,18))
etsysMultiAuthOutboundCounterGroup.setObjects(*((_A,_AR),(_A,_AS)))
if mibBuilder.loadTexts:etsysMultiAuthOutboundCounterGroup.setStatus(_B)
etsysMultiAuthSessionGroup3=ObjectGroup((1,3,6,1,4,1,5624,1,2,46,2,1,19))
etsysMultiAuthSessionGroup3.setObjects(*((_A,_I),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_u),(_A,_l),(_A,_AT)))
if mibBuilder.loadTexts:etsysMultiAuthSessionGroup3.setStatus(_B)
etsysMultiAuthSystemGroup2=ObjectGroup((1,3,6,1,4,1,5624,1,2,46,2,1,20))
etsysMultiAuthSystemGroup2.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_v)))
if mibBuilder.loadTexts:etsysMultiAuthSystemGroup2.setStatus(_J)
etsysMultiAuthSystemGroup3=ObjectGroup((1,3,6,1,4,1,5624,1,2,46,2,1,21))
etsysMultiAuthSystemGroup3.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_v),(_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:etsysMultiAuthSystemGroup3.setStatus(_B)
etsysMultiAuthSuccess=NotificationType((1,3,6,1,4,1,5624,1,2,46,1,0,1))
etsysMultiAuthSuccess.setObjects(*((_A,_G),(_A,_H),(_E,_F),(_A,_I)))
if mibBuilder.loadTexts:etsysMultiAuthSuccess.setStatus(_B)
etsysMultiAuthFailed=NotificationType((1,3,6,1,4,1,5624,1,2,46,1,0,2))
etsysMultiAuthFailed.setObjects(*((_A,_G),(_A,_H),(_E,_F),(_A,_I)))
if mibBuilder.loadTexts:etsysMultiAuthFailed.setStatus(_B)
etsysMultiAuthTerminated=NotificationType((1,3,6,1,4,1,5624,1,2,46,1,0,3))
etsysMultiAuthTerminated.setObjects(*((_A,_G),(_A,_H),(_E,_F),(_A,_I)))
if mibBuilder.loadTexts:etsysMultiAuthTerminated.setStatus(_B)
etsysMultiAuthMaxNumUsersReached=NotificationType((1,3,6,1,4,1,5624,1,2,46,1,0,4))
etsysMultiAuthMaxNumUsersReached.setObjects((_E,_F))
if mibBuilder.loadTexts:etsysMultiAuthMaxNumUsersReached.setStatus(_B)
etsysMultiAuthModuleMaxNumUsersReached=NotificationType((1,3,6,1,4,1,5624,1,2,46,1,0,5))
etsysMultiAuthModuleMaxNumUsersReached.setObjects((_q,_r))
if mibBuilder.loadTexts:etsysMultiAuthModuleMaxNumUsersReached.setStatus(_B)
etsysMultiAuthSystemMaxNumUsersReached=NotificationType((1,3,6,1,4,1,5624,1,2,46,1,0,6))
if mibBuilder.loadTexts:etsysMultiAuthSystemMaxNumUsersReached.setStatus(_B)
etsysMultiAuthNotificationPortGroup=NotificationGroup((1,3,6,1,4,1,5624,1,2,46,2,1,6))
etsysMultiAuthNotificationPortGroup.setObjects(*((_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:etsysMultiAuthNotificationPortGroup.setStatus(_B)
etsysMultiAuthNotificationModuleGroup=NotificationGroup((1,3,6,1,4,1,5624,1,2,46,2,1,13))
etsysMultiAuthNotificationModuleGroup.setObjects((_A,_Aa))
if mibBuilder.loadTexts:etsysMultiAuthNotificationModuleGroup.setStatus(_B)
etsysMultiAuthNotificationSystemGroup=NotificationGroup((1,3,6,1,4,1,5624,1,2,46,2,1,14))
etsysMultiAuthNotificationSystemGroup.setObjects((_A,_Ab))
if mibBuilder.loadTexts:etsysMultiAuthNotificationSystemGroup.setStatus(_B)
etsysMultiAuthCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,46,2,2,1))
etsysMultiAuthCompliance.setObjects(*((_A,_T),(_A,_L),(_A,_M),(_A,_w),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:etsysMultiAuthCompliance.setStatus(_J)
etsysMultiAuthCompliance2=ModuleCompliance((1,3,6,1,4,1,5624,1,2,46,2,2,2))
etsysMultiAuthCompliance2.setObjects(*((_A,_T),(_A,_L),(_A,_M),(_A,_w),(_A,_N),(_A,_O),(_A,_Q)))
if mibBuilder.loadTexts:etsysMultiAuthCompliance2.setStatus(_J)
etsysMultiAuthCompliance3=ModuleCompliance((1,3,6,1,4,1,5624,1,2,46,2,2,3))
etsysMultiAuthCompliance3.setObjects(*((_A,_T),(_A,_L),(_A,_M),(_A,_x),(_A,_N),(_A,_O),(_A,_Q)))
if mibBuilder.loadTexts:etsysMultiAuthCompliance3.setStatus(_J)
etsysMultiAuthTimeoutCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,46,2,2,4))
etsysMultiAuthTimeoutCompliance.setObjects((_A,_Ac))
if mibBuilder.loadTexts:etsysMultiAuthTimeoutCompliance.setStatus(_B)
etsysMultiAuthCurrentNumUserCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,46,2,2,5))
etsysMultiAuthCurrentNumUserCompliance.setObjects((_A,_Ad))
if mibBuilder.loadTexts:etsysMultiAuthCurrentNumUserCompliance.setStatus(_B)
etsysMultiAuthCompliance4=ModuleCompliance((1,3,6,1,4,1,5624,1,2,46,2,2,6))
etsysMultiAuthCompliance4.setObjects(*((_A,_T),(_A,_L),(_A,_M),(_A,_x),(_A,_N),(_A,_O),(_A,_Q),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:etsysMultiAuthCompliance4.setStatus(_J)
etsysMultiTunnelAttributeCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,46,2,2,7))
etsysMultiTunnelAttributeCompliance.setObjects((_A,_Ae))
if mibBuilder.loadTexts:etsysMultiTunnelAttributeCompliance.setStatus(_B)
etsysMultiAuthCounterCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,46,2,2,8))
etsysMultiAuthCounterCompliance.setObjects(*((_A,_Af),(_A,_Ag),(_A,_Ah)))
if mibBuilder.loadTexts:etsysMultiAuthCounterCompliance.setStatus(_B)
etsysMultiAuthCompliance5=ModuleCompliance((1,3,6,1,4,1,5624,1,2,46,2,2,9))
etsysMultiAuthCompliance5.setObjects(*((_A,_Ai),(_A,_L),(_A,_M),(_A,_y),(_A,_N),(_A,_O),(_A,_Q),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:etsysMultiAuthCompliance5.setStatus(_J)
etsysMultiAuthCompliance6=ModuleCompliance((1,3,6,1,4,1,5624,1,2,46,2,2,10))
etsysMultiAuthCompliance6.setObjects(*((_A,_Aj),(_A,_L),(_A,_M),(_A,_y),(_A,_N),(_A,_O),(_A,_Q),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:etsysMultiAuthCompliance6.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'EtsysMultiAuthTypes':EtsysMultiAuthTypes,_t:EtsysMultiAuthTypePrecedence,'EtsysMultiAuthStatus':EtsysMultiAuthStatus,'etsysMultiAuthMIB':etsysMultiAuthMIB,'etsysMultiAuthObjects':etsysMultiAuthObjects,'etsysMultiAuthNotification':etsysMultiAuthNotification,_AW:etsysMultiAuthSuccess,_AX:etsysMultiAuthFailed,_AY:etsysMultiAuthTerminated,_AZ:etsysMultiAuthMaxNumUsersReached,_Aa:etsysMultiAuthModuleMaxNumUsersReached,_Ab:etsysMultiAuthSystemMaxNumUsersReached,'etsysMultiAuthSystem':etsysMultiAuthSystem,_X:etsysMultiAuthSystemSupportedTypes,_Y:etsysMultiAuthSystemMaxNumUsers,_Z:etsysMultiAuthSystemCurrentNumUsers,_a:etsysMultiAuthSystemMode,_b:etsysMultiAuthSystemDefaultPrecedence,_c:etsysMultiAuthSystemAdminPrecedence,_d:etsysMultiAuthSystemOperPrecedence,'etsysMultiAuthTypePropertiesTable':etsysMultiAuthTypePropertiesTable,'etsysMultiAuthTypePropertiesEntry':etsysMultiAuthTypePropertiesEntry,_V:etsysMultiAuthType,_AD:etsysMultiAuthSessionTimeout,_AE:etsysMultiAuthIdleTimeout,_AJ:etsysMultiAuthCurrentNumUsers,_AM:etsysMultiAuthSystemMaxNumUsersReachedTrapEnable,_v:etsysMultiAuthSessionsUniquePerPort,_AU:etsysMultiAuthSessionsUniquePerPortOperStatus,_AV:etsysMultiAuthSystemReAuthenticationTimeoutAction,'etsysMultiAuthPort':etsysMultiAuthPort,'etsysMultiAuthPortTable':etsysMultiAuthPortTable,'etsysMultiAuthPortEntry':etsysMultiAuthPortEntry,_A4:etsysMultiAuthPortMode,_A5:etsysMultiAuthPortMaxNumUsers,_A6:etsysMultiAuthPortNumUsersAllowed,_A7:etsysMultiAuthPortCurrentNumUsers,_A8:etsysMultiAuthPortClearUsers,_A9:etsysMultiAuthPortTrapEnable,'etsysMultiAuthPortTypeTable':etsysMultiAuthPortTypeTable,'etsysMultiAuthPortTypeEntry':etsysMultiAuthPortTypeEntry,_AK:etsysMultiAuthPortTypeCurrentNumUsers,'etsysMultiAuthStation':etsysMultiAuthStation,'etsysMultiAuthStationTable':etsysMultiAuthStationTable,'etsysMultiAuthStationEntry':etsysMultiAuthStationEntry,_G:etsysMultiAuthStationAddrType,_H:etsysMultiAuthStationAddr,_AA:etsysMultiAuthStationClearUsers,'etsysMultiAuthSession':etsysMultiAuthSession,'etsysMultiAuthSessionStationTable':etsysMultiAuthSessionStationTable,'etsysMultiAuthSessionStationEntry':etsysMultiAuthSessionStationEntry,_I:etsysMultiAuthSessionAgentType,_e:etsysMultiAuthSessionStationAuthStatus,_f:etsysMultiAuthSessionAuthAttemptTime,_g:etsysMultiAuthSessionAuthServerType,_h:etsysMultiAuthSessionAuthServerAddrType,_i:etsysMultiAuthSessionAuthServerAddr,_j:etsysMultiAuthSessionPolicyIndex,_k:etsysMultiAuthSessionIsApplied,_u:etsysMultiAuthSessionTerminationTime,_AF:etsysMultiAuthSessionSessionTimeout,_AG:etsysMultiAuthSessionIdleTimeout,_AH:etsysMultiAuthSessionDuration,_AI:etsysMultiAuthSessionIdleTime,_AN:etsysMultiAuthSessionVlanTunnelAttribute,_AT:etsysMultiAuthSessionClear,'etsysMultiAuthSessionPortTable':etsysMultiAuthSessionPortTable,'etsysMultiAuthSessionPortEntry':etsysMultiAuthSessionPortEntry,_l:etsysMultiAuthSessionPortAuthStatus,'etsysMultiAuthModule':etsysMultiAuthModule,'etsysMultiAuthModuleTable':etsysMultiAuthModuleTable,'etsysMultiAuthModuleEntry':etsysMultiAuthModuleEntry,_AB:etsysMultiAuthModuleMaxNumUsers,_AC:etsysMultiAuthModuleCurrentNumUsers,_AL:etsysMultiAuthModuleMaxNumUsersReachedTrapEnable,'etsysMultiAuthCounters':etsysMultiAuthCounters,'etsysMultiAuthCounterTable':etsysMultiAuthCounterTable,'etsysMultiAuthCounterEntry':etsysMultiAuthCounterEntry,_AP:etsysMultiAuthCounterInboundBytes,_AQ:etsysMultiAuthCounterInboundPackets,_AR:etsysMultiAuthCounterOutboundBytes,_AS:etsysMultiAuthCounterOutboundPackets,_AO:etsysMultiAuthCounterEnable,'etsysMultiAuthConformance':etsysMultiAuthConformance,'etsysMultiAuthGroups':etsysMultiAuthGroups,_T:etsysMultiAuthSystemGroup,_L:etsysMultiAuthPortBaseGroup,_N:etsysMultiAuthPortTrapGroup,_M:etsysMultiAuthStationGroup,_w:etsysMultiAuthSessionGroup,_O:etsysMultiAuthNotificationPortGroup,_Q:etsysMultiAuthModuleGroup,_x:etsysMultiAuthSessionGroup2,_Ac:etsysMultiAuthTimeoutGroup,_Ad:etsysMultiAuthCurrentNumUsersGroup,_m:etsysMultiAuthModuleTrapGroup,_o:etsysMultiAuthSystemTrapGroup,_n:etsysMultiAuthNotificationModuleGroup,_p:etsysMultiAuthNotificationSystemGroup,_Ae:etsysMultiAuthTunnelAttributeGroup,_Af:etsysMultiAuthCounterEnableGroup,_Ag:etsysMultiAuthInboundCounterGroup,_Ah:etsysMultiAuthOutboundCounterGroup,_y:etsysMultiAuthSessionGroup3,_Ai:etsysMultiAuthSystemGroup2,_Aj:etsysMultiAuthSystemGroup3,'etsysMultiAuthCompliances':etsysMultiAuthCompliances,'etsysMultiAuthCompliance':etsysMultiAuthCompliance,'etsysMultiAuthCompliance2':etsysMultiAuthCompliance2,'etsysMultiAuthCompliance3':etsysMultiAuthCompliance3,'etsysMultiAuthTimeoutCompliance':etsysMultiAuthTimeoutCompliance,'etsysMultiAuthCurrentNumUserCompliance':etsysMultiAuthCurrentNumUserCompliance,'etsysMultiAuthCompliance4':etsysMultiAuthCompliance4,'etsysMultiTunnelAttributeCompliance':etsysMultiTunnelAttributeCompliance,'etsysMultiAuthCounterCompliance':etsysMultiAuthCounterCompliance,'etsysMultiAuthCompliance5':etsysMultiAuthCompliance5,'etsysMultiAuthCompliance6':etsysMultiAuthCompliance6})