_A9='etsysPwaSessionHCGroup'
_A8='etsysPwaSystemGroup2'
_A7='etsysPwaSystemGroupI'
_A6='etsysPwaSystemGroup'
_A5='etsysPwaSystemAccountEnable'
_A4='etsysPwaSystemAuthEnhancedMode'
_A3='etsysPwaAuthSessionOctetsTxHc'
_A2='etsysPwaAuthSessionOctetsRxHc'
_A1='etsysPwaAuthSessionUserName'
_A0='etsysPwaAuthSessionIPAddress'
_z='etsysPwaAuthSessionIPAddressType'
_y='etsysPwaAuthSessionMacAddress'
_x='etsysPwaAuthSessionTerminateCause'
_w='etsysPwaAuthSessionDuration'
_v='etsysPwaAuthSessionStartTime'
_u='etsysPwaAuthSessionFramesTx'
_t='etsysPwaAuthSessionFramesRx'
_s='etsysPwaAuthSessionOctetsTxOverflow'
_r='etsysPwaAuthSessionOctetsTx'
_q='etsysPwaAuthSessionOctetsRxOverflow'
_p='etsysPwaAuthSessionOctetsRx'
_o='etsysPwaLastLogonResult'
_n='etsysPwaFailedAttemptsSinceLogon'
_m='etsysPwaMaxFailedAttempts'
_l='etsysPwaAuthPwaState'
_k='etsysPwaControlledPortControl'
_j='etsysPwaAuthMaxReq'
_i='etsysPwaAuthQuietPeriod'
_h='etsysPwaInitializePort'
_g='etsysPwaSystemAuthIPAddress'
_f='etsysPwaSystemAuthIPAddressType'
_e='seconds'
_d='TruthValue'
_c='SnmpAdminString'
_b='etsysPwaSystemEnhancedModeRefreshTime'
_a='etsysPwaSystemGuestNetworkingStatus'
_Z='etsysPwaSystemGuestPasswordValid'
_Y='etsysPwaSystemGuestPassword'
_X='etsysPwaSystemGuestUsername'
_W='etsysPwaLogoDisplayStatus'
_V='etsysPwaSystemAuthInetAddress'
_U='etsysPwaSystemAuthInetAddressType'
_T='etsysPwaAuthSessionHCID'
_S='etsysPwaAuthSessionID'
_R='etsysPwaSessionGroup'
_Q='etsysPwaPortStatusGroup'
_P='etsysPwaPortConfigurationGroup'
_O='etsysPwaSystemAuthDomain'
_N='etsysPwaSystemAuthProtocol'
_M='etsysPwaSystemPwaNameServicesEnable'
_L='etsysPwaSystemAuthBanner'
_K='etsysPwaSystemAuthHostName'
_J='etsysPwaSystemAuthControl'
_I='DisplayString'
_H='etsysPwaPortNumber'
_G='deprecated'
_F='EnabledStatus'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='current'
_A='ENTERASYS-PWA-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_F)
ZeroBasedCounter32,=mibBuilder.importSymbols('RMON2-MIB','ZeroBasedCounter32')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_c)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'MacAddress','PhysAddress','TextualConvention','TimeInterval','TimeStamp',_d)
etsysPwaMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,8))
if mibBuilder.loadTexts:etsysPwaMIB.setRevisions(('2013-08-08 14:18','2013-02-12 16:56','2003-11-05 16:56','2003-08-04 11:22','2003-05-14 19:32','2002-12-13 21:56','2002-05-15 20:44','2002-05-14 21:30','2002-03-21 21:49','2001-06-07 16:00'))
_EtsysPwaSystem_ObjectIdentity=ObjectIdentity
etsysPwaSystem=_EtsysPwaSystem_ObjectIdentity((1,3,6,1,4,1,5624,1,2,8,1))
class _EtsysPwaSystemAuthControl_Type(EnabledStatus):defaultValue=2
_EtsysPwaSystemAuthControl_Type.__name__=_F
_EtsysPwaSystemAuthControl_Object=MibScalar
etsysPwaSystemAuthControl=_EtsysPwaSystemAuthControl_Object((1,3,6,1,4,1,5624,1,2,8,1,1),_EtsysPwaSystemAuthControl_Type())
etsysPwaSystemAuthControl.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPwaSystemAuthControl.setStatus(_B)
class _EtsysPwaSystemAuthHostName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EtsysPwaSystemAuthHostName_Type.__name__=_I
_EtsysPwaSystemAuthHostName_Object=MibScalar
etsysPwaSystemAuthHostName=_EtsysPwaSystemAuthHostName_Object((1,3,6,1,4,1,5624,1,2,8,1,2),_EtsysPwaSystemAuthHostName_Type())
etsysPwaSystemAuthHostName.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPwaSystemAuthHostName.setStatus(_B)
class _EtsysPwaSystemAuthBanner_Type(SnmpAdminString):defaultValue=OctetString('')
_EtsysPwaSystemAuthBanner_Type.__name__=_c
_EtsysPwaSystemAuthBanner_Object=MibScalar
etsysPwaSystemAuthBanner=_EtsysPwaSystemAuthBanner_Object((1,3,6,1,4,1,5624,1,2,8,1,3),_EtsysPwaSystemAuthBanner_Type())
etsysPwaSystemAuthBanner.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPwaSystemAuthBanner.setStatus(_B)
class _EtsysPwaSystemPwaNameServicesEnable_Type(EnabledStatus):defaultValue=2
_EtsysPwaSystemPwaNameServicesEnable_Type.__name__=_F
_EtsysPwaSystemPwaNameServicesEnable_Object=MibScalar
etsysPwaSystemPwaNameServicesEnable=_EtsysPwaSystemPwaNameServicesEnable_Object((1,3,6,1,4,1,5624,1,2,8,1,4),_EtsysPwaSystemPwaNameServicesEnable_Type())
etsysPwaSystemPwaNameServicesEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPwaSystemPwaNameServicesEnable.setStatus(_B)
_EtsysPwaSystemAuthIPAddressType_Type=InetAddressType
_EtsysPwaSystemAuthIPAddressType_Object=MibScalar
etsysPwaSystemAuthIPAddressType=_EtsysPwaSystemAuthIPAddressType_Object((1,3,6,1,4,1,5624,1,2,8,1,5),_EtsysPwaSystemAuthIPAddressType_Type())
etsysPwaSystemAuthIPAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPwaSystemAuthIPAddressType.setStatus(_G)
_EtsysPwaSystemAuthIPAddress_Type=IpAddress
_EtsysPwaSystemAuthIPAddress_Object=MibScalar
etsysPwaSystemAuthIPAddress=_EtsysPwaSystemAuthIPAddress_Object((1,3,6,1,4,1,5624,1,2,8,1,6),_EtsysPwaSystemAuthIPAddress_Type())
etsysPwaSystemAuthIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPwaSystemAuthIPAddress.setStatus(_G)
class _EtsysPwaSystemAuthProtocol_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('chap',1),('pap',2)))
_EtsysPwaSystemAuthProtocol_Type.__name__=_E
_EtsysPwaSystemAuthProtocol_Object=MibScalar
etsysPwaSystemAuthProtocol=_EtsysPwaSystemAuthProtocol_Object((1,3,6,1,4,1,5624,1,2,8,1,7),_EtsysPwaSystemAuthProtocol_Type())
etsysPwaSystemAuthProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPwaSystemAuthProtocol.setStatus(_B)
_EtsysPwaSystemAuthDomain_Type=SnmpAdminString
_EtsysPwaSystemAuthDomain_Object=MibScalar
etsysPwaSystemAuthDomain=_EtsysPwaSystemAuthDomain_Object((1,3,6,1,4,1,5624,1,2,8,1,8),_EtsysPwaSystemAuthDomain_Type())
etsysPwaSystemAuthDomain.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPwaSystemAuthDomain.setStatus(_B)
_EtsysPwaSystemAuthInetAddressType_Type=InetAddressType
_EtsysPwaSystemAuthInetAddressType_Object=MibScalar
etsysPwaSystemAuthInetAddressType=_EtsysPwaSystemAuthInetAddressType_Object((1,3,6,1,4,1,5624,1,2,8,1,9),_EtsysPwaSystemAuthInetAddressType_Type())
etsysPwaSystemAuthInetAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPwaSystemAuthInetAddressType.setStatus(_B)
_EtsysPwaSystemAuthInetAddress_Type=InetAddress
_EtsysPwaSystemAuthInetAddress_Object=MibScalar
etsysPwaSystemAuthInetAddress=_EtsysPwaSystemAuthInetAddress_Object((1,3,6,1,4,1,5624,1,2,8,1,10),_EtsysPwaSystemAuthInetAddress_Type())
etsysPwaSystemAuthInetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPwaSystemAuthInetAddress.setStatus(_B)
class _EtsysPwaSystemAuthEnhancedMode_Type(EnabledStatus):defaultValue=2
_EtsysPwaSystemAuthEnhancedMode_Type.__name__=_F
_EtsysPwaSystemAuthEnhancedMode_Object=MibScalar
etsysPwaSystemAuthEnhancedMode=_EtsysPwaSystemAuthEnhancedMode_Object((1,3,6,1,4,1,5624,1,2,8,1,11),_EtsysPwaSystemAuthEnhancedMode_Type())
etsysPwaSystemAuthEnhancedMode.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPwaSystemAuthEnhancedMode.setStatus(_B)
class _EtsysPwaLogoDisplayStatus_Type(EnabledStatus):defaultValue=1
_EtsysPwaLogoDisplayStatus_Type.__name__=_F
_EtsysPwaLogoDisplayStatus_Object=MibScalar
etsysPwaLogoDisplayStatus=_EtsysPwaLogoDisplayStatus_Object((1,3,6,1,4,1,5624,1,2,8,1,12),_EtsysPwaLogoDisplayStatus_Type())
etsysPwaLogoDisplayStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPwaLogoDisplayStatus.setStatus(_B)
class _EtsysPwaSystemGuestUsername_Type(DisplayString):defaultValue=OctetString('guest');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EtsysPwaSystemGuestUsername_Type.__name__=_I
_EtsysPwaSystemGuestUsername_Object=MibScalar
etsysPwaSystemGuestUsername=_EtsysPwaSystemGuestUsername_Object((1,3,6,1,4,1,5624,1,2,8,1,13),_EtsysPwaSystemGuestUsername_Type())
etsysPwaSystemGuestUsername.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPwaSystemGuestUsername.setStatus(_B)
class _EtsysPwaSystemGuestPassword_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EtsysPwaSystemGuestPassword_Type.__name__=_I
_EtsysPwaSystemGuestPassword_Object=MibScalar
etsysPwaSystemGuestPassword=_EtsysPwaSystemGuestPassword_Object((1,3,6,1,4,1,5624,1,2,8,1,14),_EtsysPwaSystemGuestPassword_Type())
etsysPwaSystemGuestPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPwaSystemGuestPassword.setStatus(_B)
class _EtsysPwaSystemGuestPasswordValid_Type(TruthValue):defaultValue=2
_EtsysPwaSystemGuestPasswordValid_Type.__name__=_d
_EtsysPwaSystemGuestPasswordValid_Object=MibScalar
etsysPwaSystemGuestPasswordValid=_EtsysPwaSystemGuestPasswordValid_Object((1,3,6,1,4,1,5624,1,2,8,1,15),_EtsysPwaSystemGuestPasswordValid_Type())
etsysPwaSystemGuestPasswordValid.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPwaSystemGuestPasswordValid.setStatus(_B)
class _EtsysPwaSystemGuestNetworkingStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('authNone',2),('authRadius',3)))
_EtsysPwaSystemGuestNetworkingStatus_Type.__name__=_E
_EtsysPwaSystemGuestNetworkingStatus_Object=MibScalar
etsysPwaSystemGuestNetworkingStatus=_EtsysPwaSystemGuestNetworkingStatus_Object((1,3,6,1,4,1,5624,1,2,8,1,16),_EtsysPwaSystemGuestNetworkingStatus_Type())
etsysPwaSystemGuestNetworkingStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPwaSystemGuestNetworkingStatus.setStatus(_B)
class _EtsysPwaSystemEnhancedModeRefreshTime_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_EtsysPwaSystemEnhancedModeRefreshTime_Type.__name__=_E
_EtsysPwaSystemEnhancedModeRefreshTime_Object=MibScalar
etsysPwaSystemEnhancedModeRefreshTime=_EtsysPwaSystemEnhancedModeRefreshTime_Object((1,3,6,1,4,1,5624,1,2,8,1,17),_EtsysPwaSystemEnhancedModeRefreshTime_Type())
etsysPwaSystemEnhancedModeRefreshTime.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPwaSystemEnhancedModeRefreshTime.setStatus(_B)
if mibBuilder.loadTexts:etsysPwaSystemEnhancedModeRefreshTime.setUnits(_e)
class _EtsysPwaSystemAccountEnable_Type(EnabledStatus):defaultValue=1
_EtsysPwaSystemAccountEnable_Type.__name__=_F
_EtsysPwaSystemAccountEnable_Object=MibScalar
etsysPwaSystemAccountEnable=_EtsysPwaSystemAccountEnable_Object((1,3,6,1,4,1,5624,1,2,8,1,18),_EtsysPwaSystemAccountEnable_Type())
etsysPwaSystemAccountEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPwaSystemAccountEnable.setStatus(_B)
_EtsysPwaPortConfiguration_ObjectIdentity=ObjectIdentity
etsysPwaPortConfiguration=_EtsysPwaPortConfiguration_ObjectIdentity((1,3,6,1,4,1,5624,1,2,8,2))
_EtsysPwaPortConfigurationTable_Object=MibTable
etsysPwaPortConfigurationTable=_EtsysPwaPortConfigurationTable_Object((1,3,6,1,4,1,5624,1,2,8,2,1))
if mibBuilder.loadTexts:etsysPwaPortConfigurationTable.setStatus(_B)
_EtsysPwaPortConfigurationEntry_Object=MibTableRow
etsysPwaPortConfigurationEntry=_EtsysPwaPortConfigurationEntry_Object((1,3,6,1,4,1,5624,1,2,8,2,1,1))
etsysPwaPortConfigurationEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:etsysPwaPortConfigurationEntry.setStatus(_B)
_EtsysPwaPortNumber_Type=InterfaceIndex
_EtsysPwaPortNumber_Object=MibTableColumn
etsysPwaPortNumber=_EtsysPwaPortNumber_Object((1,3,6,1,4,1,5624,1,2,8,2,1,1,1),_EtsysPwaPortNumber_Type())
etsysPwaPortNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:etsysPwaPortNumber.setStatus(_B)
_EtsysPwaInitializePort_Type=TruthValue
_EtsysPwaInitializePort_Object=MibTableColumn
etsysPwaInitializePort=_EtsysPwaInitializePort_Object((1,3,6,1,4,1,5624,1,2,8,2,1,1,2),_EtsysPwaInitializePort_Type())
etsysPwaInitializePort.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPwaInitializePort.setStatus(_B)
class _EtsysPwaAuthQuietPeriod_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_EtsysPwaAuthQuietPeriod_Type.__name__=_E
_EtsysPwaAuthQuietPeriod_Object=MibTableColumn
etsysPwaAuthQuietPeriod=_EtsysPwaAuthQuietPeriod_Object((1,3,6,1,4,1,5624,1,2,8,2,1,1,3),_EtsysPwaAuthQuietPeriod_Type())
etsysPwaAuthQuietPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPwaAuthQuietPeriod.setStatus(_B)
if mibBuilder.loadTexts:etsysPwaAuthQuietPeriod.setUnits(_e)
class _EtsysPwaAuthMaxReq_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_EtsysPwaAuthMaxReq_Type.__name__=_E
_EtsysPwaAuthMaxReq_Object=MibTableColumn
etsysPwaAuthMaxReq=_EtsysPwaAuthMaxReq_Object((1,3,6,1,4,1,5624,1,2,8,2,1,1,4),_EtsysPwaAuthMaxReq_Type())
etsysPwaAuthMaxReq.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPwaAuthMaxReq.setStatus(_B)
class _EtsysPwaControlledPortControl_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('forceUnauthorized',1),('auto',2),('forceAuthorized',3),('promiscousAuto',4)))
_EtsysPwaControlledPortControl_Type.__name__=_E
_EtsysPwaControlledPortControl_Object=MibTableColumn
etsysPwaControlledPortControl=_EtsysPwaControlledPortControl_Object((1,3,6,1,4,1,5624,1,2,8,2,1,1,5),_EtsysPwaControlledPortControl_Type())
etsysPwaControlledPortControl.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysPwaControlledPortControl.setStatus(_B)
_EtsysPwaPortStatus_ObjectIdentity=ObjectIdentity
etsysPwaPortStatus=_EtsysPwaPortStatus_ObjectIdentity((1,3,6,1,4,1,5624,1,2,8,3))
_EtsysPwaAuthStatusTable_Object=MibTable
etsysPwaAuthStatusTable=_EtsysPwaAuthStatusTable_Object((1,3,6,1,4,1,5624,1,2,8,3,1))
if mibBuilder.loadTexts:etsysPwaAuthStatusTable.setStatus(_B)
_EtsysPwaAuthStatusEntry_Object=MibTableRow
etsysPwaAuthStatusEntry=_EtsysPwaAuthStatusEntry_Object((1,3,6,1,4,1,5624,1,2,8,3,1,1))
etsysPwaAuthStatusEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:etsysPwaAuthStatusEntry.setStatus(_B)
class _EtsysPwaAuthPwaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('disconnected',1),('authenticating',2),('authenticated',3),('held',4)))
_EtsysPwaAuthPwaState_Type.__name__=_E
_EtsysPwaAuthPwaState_Object=MibTableColumn
etsysPwaAuthPwaState=_EtsysPwaAuthPwaState_Object((1,3,6,1,4,1,5624,1,2,8,3,1,1,1),_EtsysPwaAuthPwaState_Type())
etsysPwaAuthPwaState.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPwaAuthPwaState.setStatus(_B)
_EtsysPwaMaxFailedAttempts_Type=ZeroBasedCounter32
_EtsysPwaMaxFailedAttempts_Object=MibTableColumn
etsysPwaMaxFailedAttempts=_EtsysPwaMaxFailedAttempts_Object((1,3,6,1,4,1,5624,1,2,8,3,1,1,2),_EtsysPwaMaxFailedAttempts_Type())
etsysPwaMaxFailedAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPwaMaxFailedAttempts.setStatus(_B)
_EtsysPwaFailedAttemptsSinceLogon_Type=ZeroBasedCounter32
_EtsysPwaFailedAttemptsSinceLogon_Object=MibTableColumn
etsysPwaFailedAttemptsSinceLogon=_EtsysPwaFailedAttemptsSinceLogon_Object((1,3,6,1,4,1,5624,1,2,8,3,1,1,3),_EtsysPwaFailedAttemptsSinceLogon_Type())
etsysPwaFailedAttemptsSinceLogon.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPwaFailedAttemptsSinceLogon.setStatus(_B)
_EtsysPwaLastLogonResult_Type=SnmpAdminString
_EtsysPwaLastLogonResult_Object=MibTableColumn
etsysPwaLastLogonResult=_EtsysPwaLastLogonResult_Object((1,3,6,1,4,1,5624,1,2,8,3,1,1,4),_EtsysPwaLastLogonResult_Type())
etsysPwaLastLogonResult.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPwaLastLogonResult.setStatus(_B)
_EtsysPwaSession_ObjectIdentity=ObjectIdentity
etsysPwaSession=_EtsysPwaSession_ObjectIdentity((1,3,6,1,4,1,5624,1,2,8,4))
_EtsysPwaAuthSessionStatsTable_Object=MibTable
etsysPwaAuthSessionStatsTable=_EtsysPwaAuthSessionStatsTable_Object((1,3,6,1,4,1,5624,1,2,8,4,1))
if mibBuilder.loadTexts:etsysPwaAuthSessionStatsTable.setStatus(_B)
_EtsysPwaAuthSessionStatsEntry_Object=MibTableRow
etsysPwaAuthSessionStatsEntry=_EtsysPwaAuthSessionStatsEntry_Object((1,3,6,1,4,1,5624,1,2,8,4,1,1))
etsysPwaAuthSessionStatsEntry.setIndexNames((0,_A,_H),(0,_A,_S))
if mibBuilder.loadTexts:etsysPwaAuthSessionStatsEntry.setStatus(_B)
_EtsysPwaAuthSessionID_Type=Integer32
_EtsysPwaAuthSessionID_Object=MibTableColumn
etsysPwaAuthSessionID=_EtsysPwaAuthSessionID_Object((1,3,6,1,4,1,5624,1,2,8,4,1,1,1),_EtsysPwaAuthSessionID_Type())
etsysPwaAuthSessionID.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPwaAuthSessionID.setStatus(_B)
_EtsysPwaAuthSessionOctetsRx_Type=Counter32
_EtsysPwaAuthSessionOctetsRx_Object=MibTableColumn
etsysPwaAuthSessionOctetsRx=_EtsysPwaAuthSessionOctetsRx_Object((1,3,6,1,4,1,5624,1,2,8,4,1,1,2),_EtsysPwaAuthSessionOctetsRx_Type())
etsysPwaAuthSessionOctetsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPwaAuthSessionOctetsRx.setStatus(_B)
_EtsysPwaAuthSessionOctetsRxOverflow_Type=Counter32
_EtsysPwaAuthSessionOctetsRxOverflow_Object=MibTableColumn
etsysPwaAuthSessionOctetsRxOverflow=_EtsysPwaAuthSessionOctetsRxOverflow_Object((1,3,6,1,4,1,5624,1,2,8,4,1,1,3),_EtsysPwaAuthSessionOctetsRxOverflow_Type())
etsysPwaAuthSessionOctetsRxOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPwaAuthSessionOctetsRxOverflow.setStatus(_B)
_EtsysPwaAuthSessionOctetsTx_Type=Counter32
_EtsysPwaAuthSessionOctetsTx_Object=MibTableColumn
etsysPwaAuthSessionOctetsTx=_EtsysPwaAuthSessionOctetsTx_Object((1,3,6,1,4,1,5624,1,2,8,4,1,1,4),_EtsysPwaAuthSessionOctetsTx_Type())
etsysPwaAuthSessionOctetsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPwaAuthSessionOctetsTx.setStatus(_B)
_EtsysPwaAuthSessionOctetsTxOverflow_Type=Counter32
_EtsysPwaAuthSessionOctetsTxOverflow_Object=MibTableColumn
etsysPwaAuthSessionOctetsTxOverflow=_EtsysPwaAuthSessionOctetsTxOverflow_Object((1,3,6,1,4,1,5624,1,2,8,4,1,1,5),_EtsysPwaAuthSessionOctetsTxOverflow_Type())
etsysPwaAuthSessionOctetsTxOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPwaAuthSessionOctetsTxOverflow.setStatus(_B)
_EtsysPwaAuthSessionFramesRx_Type=Counter32
_EtsysPwaAuthSessionFramesRx_Object=MibTableColumn
etsysPwaAuthSessionFramesRx=_EtsysPwaAuthSessionFramesRx_Object((1,3,6,1,4,1,5624,1,2,8,4,1,1,6),_EtsysPwaAuthSessionFramesRx_Type())
etsysPwaAuthSessionFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPwaAuthSessionFramesRx.setStatus(_B)
_EtsysPwaAuthSessionFramesTx_Type=Counter32
_EtsysPwaAuthSessionFramesTx_Object=MibTableColumn
etsysPwaAuthSessionFramesTx=_EtsysPwaAuthSessionFramesTx_Object((1,3,6,1,4,1,5624,1,2,8,4,1,1,7),_EtsysPwaAuthSessionFramesTx_Type())
etsysPwaAuthSessionFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPwaAuthSessionFramesTx.setStatus(_B)
_EtsysPwaAuthSessionStartTime_Type=TimeStamp
_EtsysPwaAuthSessionStartTime_Object=MibTableColumn
etsysPwaAuthSessionStartTime=_EtsysPwaAuthSessionStartTime_Object((1,3,6,1,4,1,5624,1,2,8,4,1,1,8),_EtsysPwaAuthSessionStartTime_Type())
etsysPwaAuthSessionStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPwaAuthSessionStartTime.setStatus(_B)
_EtsysPwaAuthSessionDuration_Type=TimeInterval
_EtsysPwaAuthSessionDuration_Object=MibTableColumn
etsysPwaAuthSessionDuration=_EtsysPwaAuthSessionDuration_Object((1,3,6,1,4,1,5624,1,2,8,4,1,1,9),_EtsysPwaAuthSessionDuration_Type())
etsysPwaAuthSessionDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPwaAuthSessionDuration.setStatus(_B)
class _EtsysPwaAuthSessionTerminateCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,999)));namedValues=NamedValues(*(('linkDown',1),('logoff',2),('authControlForceUnauth',3),('portReInit',4),('portDisabled',5),('notTerminatedYet',999)))
_EtsysPwaAuthSessionTerminateCause_Type.__name__=_E
_EtsysPwaAuthSessionTerminateCause_Object=MibTableColumn
etsysPwaAuthSessionTerminateCause=_EtsysPwaAuthSessionTerminateCause_Object((1,3,6,1,4,1,5624,1,2,8,4,1,1,10),_EtsysPwaAuthSessionTerminateCause_Type())
etsysPwaAuthSessionTerminateCause.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPwaAuthSessionTerminateCause.setStatus(_B)
_EtsysPwaAuthSessionMacAddress_Type=MacAddress
_EtsysPwaAuthSessionMacAddress_Object=MibTableColumn
etsysPwaAuthSessionMacAddress=_EtsysPwaAuthSessionMacAddress_Object((1,3,6,1,4,1,5624,1,2,8,4,1,1,11),_EtsysPwaAuthSessionMacAddress_Type())
etsysPwaAuthSessionMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPwaAuthSessionMacAddress.setStatus(_B)
_EtsysPwaAuthSessionIPAddressType_Type=InetAddressType
_EtsysPwaAuthSessionIPAddressType_Object=MibTableColumn
etsysPwaAuthSessionIPAddressType=_EtsysPwaAuthSessionIPAddressType_Object((1,3,6,1,4,1,5624,1,2,8,4,1,1,12),_EtsysPwaAuthSessionIPAddressType_Type())
etsysPwaAuthSessionIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPwaAuthSessionIPAddressType.setStatus(_B)
_EtsysPwaAuthSessionIPAddress_Type=InetAddress
_EtsysPwaAuthSessionIPAddress_Object=MibTableColumn
etsysPwaAuthSessionIPAddress=_EtsysPwaAuthSessionIPAddress_Object((1,3,6,1,4,1,5624,1,2,8,4,1,1,13),_EtsysPwaAuthSessionIPAddress_Type())
etsysPwaAuthSessionIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPwaAuthSessionIPAddress.setStatus(_B)
_EtsysPwaAuthSessionUserName_Type=SnmpAdminString
_EtsysPwaAuthSessionUserName_Object=MibTableColumn
etsysPwaAuthSessionUserName=_EtsysPwaAuthSessionUserName_Object((1,3,6,1,4,1,5624,1,2,8,4,1,1,14),_EtsysPwaAuthSessionUserName_Type())
etsysPwaAuthSessionUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPwaAuthSessionUserName.setStatus(_B)
_EtsysPwaAuthSessionStatsHCTable_Object=MibTable
etsysPwaAuthSessionStatsHCTable=_EtsysPwaAuthSessionStatsHCTable_Object((1,3,6,1,4,1,5624,1,2,8,4,2))
if mibBuilder.loadTexts:etsysPwaAuthSessionStatsHCTable.setStatus(_B)
_EtsysPwaAuthSessionStatsHCEntry_Object=MibTableRow
etsysPwaAuthSessionStatsHCEntry=_EtsysPwaAuthSessionStatsHCEntry_Object((1,3,6,1,4,1,5624,1,2,8,4,2,1))
etsysPwaAuthSessionStatsHCEntry.setIndexNames((0,_A,_H),(0,_A,_T))
if mibBuilder.loadTexts:etsysPwaAuthSessionStatsHCEntry.setStatus(_B)
_EtsysPwaAuthSessionHCID_Type=Integer32
_EtsysPwaAuthSessionHCID_Object=MibTableColumn
etsysPwaAuthSessionHCID=_EtsysPwaAuthSessionHCID_Object((1,3,6,1,4,1,5624,1,2,8,4,2,1,1),_EtsysPwaAuthSessionHCID_Type())
etsysPwaAuthSessionHCID.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPwaAuthSessionHCID.setStatus(_B)
_EtsysPwaAuthSessionOctetsRxHc_Type=Counter64
_EtsysPwaAuthSessionOctetsRxHc_Object=MibTableColumn
etsysPwaAuthSessionOctetsRxHc=_EtsysPwaAuthSessionOctetsRxHc_Object((1,3,6,1,4,1,5624,1,2,8,4,2,1,2),_EtsysPwaAuthSessionOctetsRxHc_Type())
etsysPwaAuthSessionOctetsRxHc.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPwaAuthSessionOctetsRxHc.setStatus(_B)
_EtsysPwaAuthSessionOctetsTxHc_Type=Counter64
_EtsysPwaAuthSessionOctetsTxHc_Object=MibTableColumn
etsysPwaAuthSessionOctetsTxHc=_EtsysPwaAuthSessionOctetsTxHc_Object((1,3,6,1,4,1,5624,1,2,8,4,2,1,3),_EtsysPwaAuthSessionOctetsTxHc_Type())
etsysPwaAuthSessionOctetsTxHc.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPwaAuthSessionOctetsTxHc.setStatus(_B)
_EtsysPwaMIBGroups_ObjectIdentity=ObjectIdentity
etsysPwaMIBGroups=_EtsysPwaMIBGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,8,5))
_EtsysPwaMIBCompliances_ObjectIdentity=ObjectIdentity
etsysPwaMIBCompliances=_EtsysPwaMIBCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,8,6))
etsysPwaSystemGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,8,5,1))
etsysPwaSystemGroup.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_f),(_A,_g),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:etsysPwaSystemGroup.setStatus(_G)
etsysPwaPortConfigurationGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,8,5,2))
etsysPwaPortConfigurationGroup.setObjects(*((_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:etsysPwaPortConfigurationGroup.setStatus(_B)
etsysPwaPortStatusGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,8,5,3))
etsysPwaPortStatusGroup.setObjects(*((_A,_l),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:etsysPwaPortStatusGroup.setStatus(_B)
etsysPwaSessionGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,8,5,4))
etsysPwaSessionGroup.setObjects(*((_A,_S),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:etsysPwaSessionGroup.setStatus(_B)
etsysPwaSessionHCGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,8,5,5))
etsysPwaSessionHCGroup.setObjects(*((_A,_T),(_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:etsysPwaSessionHCGroup.setStatus(_B)
etsysPwaSystemGroupI=ObjectGroup((1,3,6,1,4,1,5624,1,2,8,5,6))
etsysPwaSystemGroupI.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:etsysPwaSystemGroupI.setStatus(_G)
etsysPwaSystemAuthEnhancedGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,8,5,7))
etsysPwaSystemAuthEnhancedGroup.setObjects((_A,_A4))
if mibBuilder.loadTexts:etsysPwaSystemAuthEnhancedGroup.setStatus(_B)
etsysPwaSystemGroup2=ObjectGroup((1,3,6,1,4,1,5624,1,2,8,5,8))
etsysPwaSystemGroup2.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_A5)))
if mibBuilder.loadTexts:etsysPwaSystemGroup2.setStatus(_B)
etsysPwaMIBCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,8,6,1))
etsysPwaMIBCompliance.setObjects(*((_A,_A6),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:etsysPwaMIBCompliance.setStatus(_G)
etsysPwaMIBComplianceI=ModuleCompliance((1,3,6,1,4,1,5624,1,2,8,6,2))
etsysPwaMIBComplianceI.setObjects(*((_A,_A7),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:etsysPwaMIBComplianceI.setStatus(_G)
etsysPwaMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,5624,1,2,8,6,3))
etsysPwaMIBCompliance2.setObjects(*((_A,_A8),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:etsysPwaMIBCompliance2.setStatus(_B)
etsysPwaMIBHighCapacityCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,8,6,4))
etsysPwaMIBHighCapacityCompliance.setObjects((_A,_A9))
if mibBuilder.loadTexts:etsysPwaMIBHighCapacityCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'etsysPwaMIB':etsysPwaMIB,'etsysPwaSystem':etsysPwaSystem,_J:etsysPwaSystemAuthControl,_K:etsysPwaSystemAuthHostName,_L:etsysPwaSystemAuthBanner,_M:etsysPwaSystemPwaNameServicesEnable,_f:etsysPwaSystemAuthIPAddressType,_g:etsysPwaSystemAuthIPAddress,_N:etsysPwaSystemAuthProtocol,_O:etsysPwaSystemAuthDomain,_U:etsysPwaSystemAuthInetAddressType,_V:etsysPwaSystemAuthInetAddress,_A4:etsysPwaSystemAuthEnhancedMode,_W:etsysPwaLogoDisplayStatus,_X:etsysPwaSystemGuestUsername,_Y:etsysPwaSystemGuestPassword,_Z:etsysPwaSystemGuestPasswordValid,_a:etsysPwaSystemGuestNetworkingStatus,_b:etsysPwaSystemEnhancedModeRefreshTime,_A5:etsysPwaSystemAccountEnable,'etsysPwaPortConfiguration':etsysPwaPortConfiguration,'etsysPwaPortConfigurationTable':etsysPwaPortConfigurationTable,'etsysPwaPortConfigurationEntry':etsysPwaPortConfigurationEntry,_H:etsysPwaPortNumber,_h:etsysPwaInitializePort,_i:etsysPwaAuthQuietPeriod,_j:etsysPwaAuthMaxReq,_k:etsysPwaControlledPortControl,'etsysPwaPortStatus':etsysPwaPortStatus,'etsysPwaAuthStatusTable':etsysPwaAuthStatusTable,'etsysPwaAuthStatusEntry':etsysPwaAuthStatusEntry,_l:etsysPwaAuthPwaState,_m:etsysPwaMaxFailedAttempts,_n:etsysPwaFailedAttemptsSinceLogon,_o:etsysPwaLastLogonResult,'etsysPwaSession':etsysPwaSession,'etsysPwaAuthSessionStatsTable':etsysPwaAuthSessionStatsTable,'etsysPwaAuthSessionStatsEntry':etsysPwaAuthSessionStatsEntry,_S:etsysPwaAuthSessionID,_p:etsysPwaAuthSessionOctetsRx,_q:etsysPwaAuthSessionOctetsRxOverflow,_r:etsysPwaAuthSessionOctetsTx,_s:etsysPwaAuthSessionOctetsTxOverflow,_t:etsysPwaAuthSessionFramesRx,_u:etsysPwaAuthSessionFramesTx,_v:etsysPwaAuthSessionStartTime,_w:etsysPwaAuthSessionDuration,_x:etsysPwaAuthSessionTerminateCause,_y:etsysPwaAuthSessionMacAddress,_z:etsysPwaAuthSessionIPAddressType,_A0:etsysPwaAuthSessionIPAddress,_A1:etsysPwaAuthSessionUserName,'etsysPwaAuthSessionStatsHCTable':etsysPwaAuthSessionStatsHCTable,'etsysPwaAuthSessionStatsHCEntry':etsysPwaAuthSessionStatsHCEntry,_T:etsysPwaAuthSessionHCID,_A2:etsysPwaAuthSessionOctetsRxHc,_A3:etsysPwaAuthSessionOctetsTxHc,'etsysPwaMIBGroups':etsysPwaMIBGroups,_A6:etsysPwaSystemGroup,_P:etsysPwaPortConfigurationGroup,_Q:etsysPwaPortStatusGroup,_R:etsysPwaSessionGroup,_A9:etsysPwaSessionHCGroup,_A7:etsysPwaSystemGroupI,'etsysPwaSystemAuthEnhancedGroup':etsysPwaSystemAuthEnhancedGroup,_A8:etsysPwaSystemGroup2,'etsysPwaMIBCompliances':etsysPwaMIBCompliances,'etsysPwaMIBCompliance':etsysPwaMIBCompliance,'etsysPwaMIBComplianceI':etsysPwaMIBComplianceI,'etsysPwaMIBCompliance2':etsysPwaMIBCompliance2,'etsysPwaMIBHighCapacityCompliance':etsysPwaMIBHighCapacityCompliance})