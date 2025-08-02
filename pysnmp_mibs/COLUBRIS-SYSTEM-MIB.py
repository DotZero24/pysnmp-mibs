_AF='colubrisAdminAccessManagementConsoleGroup'
_AE='colubrisSystemMIBDeprecatedGroup'
_AD='timeServerFailure'
_AC='adminAccessLogoutNotification'
_AB='adminAccessLoginNotification'
_AA='adminAccessAuthFailureNotification'
_A9='systemHeartbeatNotification'
_A8='systemColdStart'
_A7='adminAccessManagementConsoleEnabled'
_A6='adminAccessManagementConsole'
_A5='systemTimeDSTOn'
_A4='adminAccessLogoutNotificationEnabled'
_A3='adminAccessAdministrativeRights'
_A2='adminAccessUserName'
_A1='adminAccessAuthenProfileIndex'
_A0='adminAccessAuthFailureNotificationEnabled'
_z='adminAccessLoginNotificationEnabled'
_y='adminAccessLockOutPeriod'
_x='adminAccessMaxLoginAttempts'
_w='adminAccessAuthenMode'
_v='heartbeatNotificationEnabled'
_u='heartbeatPeriod'
_t='systemTimeServerNotificationEnabled'
_s='systemTimeZone'
_r='systemTimeOfDay'
_q='systemDate'
_p='systemTimeLostWhenRebooting'
_o='systemTimeUpdateMode'
_n='systemLLDPOperState'
_m='systemCDPOperState'
_l='systemControllerMode'
_k='systemFirmwareBuildDate'
_j='systemDeviceIdentification'
_i='systemProductFlavor'
_h='systemHardwareRevision'
_g='systemBootRevision'
_f='adminAccessProfileIndex'
_e='not-accessible'
_d='systemTimeServerIndex'
_c='seconds'
_b='colubrisTimeNotificationGroup'
_a='colubrisAdminAccessNotificationGroup'
_Z='colubrisAdminAccessProfileGroup'
_Y='colubrisSystemNotificationGroup'
_X='colubrisSystemMIBGroup'
_W='systemTimeServerAddress'
_V='systemWanPortIpAddress'
_U='systemMacAddress'
_T='systemUpTime'
_S='systemConfigurationVersion'
_R='systemFirmwareRevision'
_Q='systemProductName'
_P='accessible-for-notify'
_O='adminAccessInfo'
_N='systemSerialNumber'
_M='deprecated'
_L='ifOutUcastPkts'
_K='ifOutErrors'
_J='ifInUcastPkts'
_I='ifInErrors'
_H='ColubrisNotificationEnable'
_G='OctetString'
_F='Integer32'
_E='IF-MIB'
_D='read-only'
_C='read-write'
_B='current'
_A='COLUBRIS-SYSTEM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
colubrisMgmtV2,=mibBuilder.importSymbols('COLUBRIS-SMI','colubrisMgmtV2')
ColubrisAuthenticationMode,ColubrisNotificationEnable,ColubrisProfileIndexOrZero=mibBuilder.importSymbols('COLUBRIS-TC','ColubrisAuthenticationMode',_H,'ColubrisProfileIndexOrZero')
ifInErrors,ifInUcastPkts,ifOutErrors,ifOutUcastPkts=mibBuilder.importSymbols(_E,_I,_J,_K,_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
colubrisSystemMIB=ModuleIdentity((1,3,6,1,4,1,8744,5,6))
_ColubrisSystemMIBObjects_ObjectIdentity=ObjectIdentity
colubrisSystemMIBObjects=_ColubrisSystemMIBObjects_ObjectIdentity((1,3,6,1,4,1,8744,5,6,1))
_SystemInfo_ObjectIdentity=ObjectIdentity
systemInfo=_SystemInfo_ObjectIdentity((1,3,6,1,4,1,8744,5,6,1,1))
_SystemProductName_Type=DisplayString
_SystemProductName_Object=MibScalar
systemProductName=_SystemProductName_Object((1,3,6,1,4,1,8744,5,6,1,1,1),_SystemProductName_Type())
systemProductName.setMaxAccess(_D)
if mibBuilder.loadTexts:systemProductName.setStatus(_B)
_SystemFirmwareRevision_Type=DisplayString
_SystemFirmwareRevision_Object=MibScalar
systemFirmwareRevision=_SystemFirmwareRevision_Object((1,3,6,1,4,1,8744,5,6,1,1,2),_SystemFirmwareRevision_Type())
systemFirmwareRevision.setMaxAccess(_D)
if mibBuilder.loadTexts:systemFirmwareRevision.setStatus(_B)
_SystemBootRevision_Type=DisplayString
_SystemBootRevision_Object=MibScalar
systemBootRevision=_SystemBootRevision_Object((1,3,6,1,4,1,8744,5,6,1,1,3),_SystemBootRevision_Type())
systemBootRevision.setMaxAccess(_D)
if mibBuilder.loadTexts:systemBootRevision.setStatus(_B)
_SystemHardwareRevision_Type=DisplayString
_SystemHardwareRevision_Object=MibScalar
systemHardwareRevision=_SystemHardwareRevision_Object((1,3,6,1,4,1,8744,5,6,1,1,4),_SystemHardwareRevision_Type())
systemHardwareRevision.setMaxAccess(_D)
if mibBuilder.loadTexts:systemHardwareRevision.setStatus(_B)
_SystemSerialNumber_Type=DisplayString
_SystemSerialNumber_Object=MibScalar
systemSerialNumber=_SystemSerialNumber_Object((1,3,6,1,4,1,8744,5,6,1,1,5),_SystemSerialNumber_Type())
systemSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:systemSerialNumber.setStatus(_B)
_SystemConfigurationVersion_Type=DisplayString
_SystemConfigurationVersion_Object=MibScalar
systemConfigurationVersion=_SystemConfigurationVersion_Object((1,3,6,1,4,1,8744,5,6,1,1,6),_SystemConfigurationVersion_Type())
systemConfigurationVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:systemConfigurationVersion.setStatus(_B)
_SystemUpTime_Type=Counter32
_SystemUpTime_Object=MibScalar
systemUpTime=_SystemUpTime_Object((1,3,6,1,4,1,8744,5,6,1,1,7),_SystemUpTime_Type())
systemUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:systemUpTime.setStatus(_B)
if mibBuilder.loadTexts:systemUpTime.setUnits(_c)
_SystemMacAddress_Type=MacAddress
_SystemMacAddress_Object=MibScalar
systemMacAddress=_SystemMacAddress_Object((1,3,6,1,4,1,8744,5,6,1,1,8),_SystemMacAddress_Type())
systemMacAddress.setMaxAccess(_P)
if mibBuilder.loadTexts:systemMacAddress.setStatus(_B)
_SystemWanPortIpAddress_Type=IpAddress
_SystemWanPortIpAddress_Object=MibScalar
systemWanPortIpAddress=_SystemWanPortIpAddress_Object((1,3,6,1,4,1,8744,5,6,1,1,9),_SystemWanPortIpAddress_Type())
systemWanPortIpAddress.setMaxAccess(_P)
if mibBuilder.loadTexts:systemWanPortIpAddress.setStatus(_B)
_SystemProductFlavor_Type=DisplayString
_SystemProductFlavor_Object=MibScalar
systemProductFlavor=_SystemProductFlavor_Object((1,3,6,1,4,1,8744,5,6,1,1,10),_SystemProductFlavor_Type())
systemProductFlavor.setMaxAccess(_D)
if mibBuilder.loadTexts:systemProductFlavor.setStatus(_B)
_SystemDeviceIdentification_Type=MacAddress
_SystemDeviceIdentification_Object=MibScalar
systemDeviceIdentification=_SystemDeviceIdentification_Object((1,3,6,1,4,1,8744,5,6,1,1,11),_SystemDeviceIdentification_Type())
systemDeviceIdentification.setMaxAccess(_D)
if mibBuilder.loadTexts:systemDeviceIdentification.setStatus(_B)
class _SystemFirmwareBuildDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_SystemFirmwareBuildDate_Type.__name__=_G
_SystemFirmwareBuildDate_Object=MibScalar
systemFirmwareBuildDate=_SystemFirmwareBuildDate_Object((1,3,6,1,4,1,8744,5,6,1,1,12),_SystemFirmwareBuildDate_Type())
systemFirmwareBuildDate.setMaxAccess(_D)
if mibBuilder.loadTexts:systemFirmwareBuildDate.setStatus(_B)
class _SystemControllerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('alone',2),('member',3),('manager',4),('candidate',5)))
_SystemControllerMode_Type.__name__=_F
_SystemControllerMode_Object=MibScalar
systemControllerMode=_SystemControllerMode_Object((1,3,6,1,4,1,8744,5,6,1,1,13),_SystemControllerMode_Type())
systemControllerMode.setMaxAccess(_D)
if mibBuilder.loadTexts:systemControllerMode.setStatus(_B)
_SystemCDPOperState_Type=TruthValue
_SystemCDPOperState_Object=MibScalar
systemCDPOperState=_SystemCDPOperState_Object((1,3,6,1,4,1,8744,5,6,1,1,14),_SystemCDPOperState_Type())
systemCDPOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:systemCDPOperState.setStatus(_B)
_SystemLLDPOperState_Type=TruthValue
_SystemLLDPOperState_Object=MibScalar
systemLLDPOperState=_SystemLLDPOperState_Object((1,3,6,1,4,1,8744,5,6,1,1,15),_SystemLLDPOperState_Type())
systemLLDPOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:systemLLDPOperState.setStatus(_B)
_SystemTime_ObjectIdentity=ObjectIdentity
systemTime=_SystemTime_ObjectIdentity((1,3,6,1,4,1,8744,5,6,1,2))
class _SystemTimeUpdateMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('manual',1),('sntpUdp',2),('tp',3)))
_SystemTimeUpdateMode_Type.__name__=_F
_SystemTimeUpdateMode_Object=MibScalar
systemTimeUpdateMode=_SystemTimeUpdateMode_Object((1,3,6,1,4,1,8744,5,6,1,2,1),_SystemTimeUpdateMode_Type())
systemTimeUpdateMode.setMaxAccess(_C)
if mibBuilder.loadTexts:systemTimeUpdateMode.setStatus(_B)
_SystemTimeLostWhenRebooting_Type=TruthValue
_SystemTimeLostWhenRebooting_Object=MibScalar
systemTimeLostWhenRebooting=_SystemTimeLostWhenRebooting_Object((1,3,6,1,4,1,8744,5,6,1,2,2),_SystemTimeLostWhenRebooting_Type())
systemTimeLostWhenRebooting.setMaxAccess(_D)
if mibBuilder.loadTexts:systemTimeLostWhenRebooting.setStatus(_B)
_SystemTimeDSTOn_Type=TruthValue
_SystemTimeDSTOn_Object=MibScalar
systemTimeDSTOn=_SystemTimeDSTOn_Object((1,3,6,1,4,1,8744,5,6,1,2,3),_SystemTimeDSTOn_Type())
systemTimeDSTOn.setMaxAccess(_C)
if mibBuilder.loadTexts:systemTimeDSTOn.setStatus(_M)
class _SystemDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_SystemDate_Type.__name__=_G
_SystemDate_Object=MibScalar
systemDate=_SystemDate_Object((1,3,6,1,4,1,8744,5,6,1,2,4),_SystemDate_Type())
systemDate.setMaxAccess(_C)
if mibBuilder.loadTexts:systemDate.setStatus(_B)
class _SystemTimeOfDay_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SystemTimeOfDay_Type.__name__=_G
_SystemTimeOfDay_Object=MibScalar
systemTimeOfDay=_SystemTimeOfDay_Object((1,3,6,1,4,1,8744,5,6,1,2,5),_SystemTimeOfDay_Type())
systemTimeOfDay.setMaxAccess(_C)
if mibBuilder.loadTexts:systemTimeOfDay.setStatus(_B)
class _SystemTimeZone_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SystemTimeZone_Type.__name__=_G
_SystemTimeZone_Object=MibScalar
systemTimeZone=_SystemTimeZone_Object((1,3,6,1,4,1,8744,5,6,1,2,6),_SystemTimeZone_Type())
systemTimeZone.setMaxAccess(_C)
if mibBuilder.loadTexts:systemTimeZone.setStatus(_B)
_SystemTimeServerTable_Object=MibTable
systemTimeServerTable=_SystemTimeServerTable_Object((1,3,6,1,4,1,8744,5,6,1,2,7))
if mibBuilder.loadTexts:systemTimeServerTable.setStatus(_B)
_SystemTimeServerEntry_Object=MibTableRow
systemTimeServerEntry=_SystemTimeServerEntry_Object((1,3,6,1,4,1,8744,5,6,1,2,7,1))
systemTimeServerEntry.setIndexNames((0,_A,_d))
if mibBuilder.loadTexts:systemTimeServerEntry.setStatus(_B)
class _SystemTimeServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_SystemTimeServerIndex_Type.__name__=_F
_SystemTimeServerIndex_Object=MibTableColumn
systemTimeServerIndex=_SystemTimeServerIndex_Object((1,3,6,1,4,1,8744,5,6,1,2,7,1,1),_SystemTimeServerIndex_Type())
systemTimeServerIndex.setMaxAccess(_e)
if mibBuilder.loadTexts:systemTimeServerIndex.setStatus(_B)
_SystemTimeServerAddress_Type=DisplayString
_SystemTimeServerAddress_Object=MibTableColumn
systemTimeServerAddress=_SystemTimeServerAddress_Object((1,3,6,1,4,1,8744,5,6,1,2,7,1,2),_SystemTimeServerAddress_Type())
systemTimeServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:systemTimeServerAddress.setStatus(_B)
_SystemTimeServerNotificationEnabled_Type=ColubrisNotificationEnable
_SystemTimeServerNotificationEnabled_Object=MibScalar
systemTimeServerNotificationEnabled=_SystemTimeServerNotificationEnabled_Object((1,3,6,1,4,1,8744,5,6,1,2,8),_SystemTimeServerNotificationEnabled_Type())
systemTimeServerNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:systemTimeServerNotificationEnabled.setStatus(_B)
_AdminAccess_ObjectIdentity=ObjectIdentity
adminAccess=_AdminAccess_ObjectIdentity((1,3,6,1,4,1,8744,5,6,1,3))
_AdminAccessAuthenMode_Type=ColubrisAuthenticationMode
_AdminAccessAuthenMode_Object=MibScalar
adminAccessAuthenMode=_AdminAccessAuthenMode_Object((1,3,6,1,4,1,8744,5,6,1,3,1),_AdminAccessAuthenMode_Type())
adminAccessAuthenMode.setMaxAccess(_C)
if mibBuilder.loadTexts:adminAccessAuthenMode.setStatus(_B)
_AdminAccessAuthenProfileIndex_Type=ColubrisProfileIndexOrZero
_AdminAccessAuthenProfileIndex_Object=MibScalar
adminAccessAuthenProfileIndex=_AdminAccessAuthenProfileIndex_Object((1,3,6,1,4,1,8744,5,6,1,3,2),_AdminAccessAuthenProfileIndex_Type())
adminAccessAuthenProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:adminAccessAuthenProfileIndex.setStatus(_B)
class _AdminAccessMaxLoginAttempts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_AdminAccessMaxLoginAttempts_Type.__name__=_F
_AdminAccessMaxLoginAttempts_Object=MibScalar
adminAccessMaxLoginAttempts=_AdminAccessMaxLoginAttempts_Object((1,3,6,1,4,1,8744,5,6,1,3,3),_AdminAccessMaxLoginAttempts_Type())
adminAccessMaxLoginAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:adminAccessMaxLoginAttempts.setStatus(_B)
class _AdminAccessLockOutPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_AdminAccessLockOutPeriod_Type.__name__=_F
_AdminAccessLockOutPeriod_Object=MibScalar
adminAccessLockOutPeriod=_AdminAccessLockOutPeriod_Object((1,3,6,1,4,1,8744,5,6,1,3,4),_AdminAccessLockOutPeriod_Type())
adminAccessLockOutPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:adminAccessLockOutPeriod.setStatus(_B)
if mibBuilder.loadTexts:adminAccessLockOutPeriod.setUnits('minutes')
class _AdminAccessLoginNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=1
_AdminAccessLoginNotificationEnabled_Type.__name__=_H
_AdminAccessLoginNotificationEnabled_Object=MibScalar
adminAccessLoginNotificationEnabled=_AdminAccessLoginNotificationEnabled_Object((1,3,6,1,4,1,8744,5,6,1,3,5),_AdminAccessLoginNotificationEnabled_Type())
adminAccessLoginNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:adminAccessLoginNotificationEnabled.setStatus(_B)
class _AdminAccessAuthFailureNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=1
_AdminAccessAuthFailureNotificationEnabled_Type.__name__=_H
_AdminAccessAuthFailureNotificationEnabled_Object=MibScalar
adminAccessAuthFailureNotificationEnabled=_AdminAccessAuthFailureNotificationEnabled_Object((1,3,6,1,4,1,8744,5,6,1,3,6),_AdminAccessAuthFailureNotificationEnabled_Type())
adminAccessAuthFailureNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:adminAccessAuthFailureNotificationEnabled.setStatus(_B)
_AdminAccessInfo_Type=DisplayString
_AdminAccessInfo_Object=MibScalar
adminAccessInfo=_AdminAccessInfo_Object((1,3,6,1,4,1,8744,5,6,1,3,7),_AdminAccessInfo_Type())
adminAccessInfo.setMaxAccess(_P)
if mibBuilder.loadTexts:adminAccessInfo.setStatus(_B)
_AdminAccessProfileTable_Object=MibTable
adminAccessProfileTable=_AdminAccessProfileTable_Object((1,3,6,1,4,1,8744,5,6,1,3,8))
if mibBuilder.loadTexts:adminAccessProfileTable.setStatus(_B)
_AdminAccessProfileEntry_Object=MibTableRow
adminAccessProfileEntry=_AdminAccessProfileEntry_Object((1,3,6,1,4,1,8744,5,6,1,3,8,1))
adminAccessProfileEntry.setIndexNames((0,_A,_f))
if mibBuilder.loadTexts:adminAccessProfileEntry.setStatus(_B)
class _AdminAccessProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AdminAccessProfileIndex_Type.__name__=_F
_AdminAccessProfileIndex_Object=MibTableColumn
adminAccessProfileIndex=_AdminAccessProfileIndex_Object((1,3,6,1,4,1,8744,5,6,1,3,8,1,1),_AdminAccessProfileIndex_Type())
adminAccessProfileIndex.setMaxAccess(_e)
if mibBuilder.loadTexts:adminAccessProfileIndex.setStatus(_B)
class _AdminAccessUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,253))
_AdminAccessUserName_Type.__name__=_G
_AdminAccessUserName_Object=MibTableColumn
adminAccessUserName=_AdminAccessUserName_Object((1,3,6,1,4,1,8744,5,6,1,3,8,1,2),_AdminAccessUserName_Type())
adminAccessUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:adminAccessUserName.setStatus(_B)
class _AdminAccessAdministrativeRights_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('readOnly',1),('readWrite',2)))
_AdminAccessAdministrativeRights_Type.__name__=_F
_AdminAccessAdministrativeRights_Object=MibTableColumn
adminAccessAdministrativeRights=_AdminAccessAdministrativeRights_Object((1,3,6,1,4,1,8744,5,6,1,3,8,1,3),_AdminAccessAdministrativeRights_Type())
adminAccessAdministrativeRights.setMaxAccess(_D)
if mibBuilder.loadTexts:adminAccessAdministrativeRights.setStatus(_B)
class _AdminAccessLogoutNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=1
_AdminAccessLogoutNotificationEnabled_Type.__name__=_H
_AdminAccessLogoutNotificationEnabled_Object=MibScalar
adminAccessLogoutNotificationEnabled=_AdminAccessLogoutNotificationEnabled_Object((1,3,6,1,4,1,8744,5,6,1,3,9),_AdminAccessLogoutNotificationEnabled_Type())
adminAccessLogoutNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:adminAccessLogoutNotificationEnabled.setStatus(_B)
_Heartbeat_ObjectIdentity=ObjectIdentity
heartbeat=_Heartbeat_ObjectIdentity((1,3,6,1,4,1,8744,5,6,1,4))
class _HeartbeatPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,31536000))
_HeartbeatPeriod_Type.__name__=_F
_HeartbeatPeriod_Object=MibScalar
heartbeatPeriod=_HeartbeatPeriod_Object((1,3,6,1,4,1,8744,5,6,1,4,1),_HeartbeatPeriod_Type())
heartbeatPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:heartbeatPeriod.setStatus(_B)
if mibBuilder.loadTexts:heartbeatPeriod.setUnits(_c)
class _HeartbeatNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=1
_HeartbeatNotificationEnabled_Type.__name__=_H
_HeartbeatNotificationEnabled_Object=MibScalar
heartbeatNotificationEnabled=_HeartbeatNotificationEnabled_Object((1,3,6,1,4,1,8744,5,6,1,4,2),_HeartbeatNotificationEnabled_Type())
heartbeatNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:heartbeatNotificationEnabled.setStatus(_B)
_ManagementConsole_ObjectIdentity=ObjectIdentity
managementConsole=_ManagementConsole_ObjectIdentity((1,3,6,1,4,1,8744,5,6,1,5))
_AdminAccessManagementConsole_Type=DisplayString
_AdminAccessManagementConsole_Object=MibScalar
adminAccessManagementConsole=_AdminAccessManagementConsole_Object((1,3,6,1,4,1,8744,5,6,1,5,1),_AdminAccessManagementConsole_Type())
adminAccessManagementConsole.setMaxAccess(_C)
if mibBuilder.loadTexts:adminAccessManagementConsole.setStatus(_B)
_AdminAccessManagementConsoleEnabled_Type=TruthValue
_AdminAccessManagementConsoleEnabled_Object=MibScalar
adminAccessManagementConsoleEnabled=_AdminAccessManagementConsoleEnabled_Object((1,3,6,1,4,1,8744,5,6,1,5,2),_AdminAccessManagementConsoleEnabled_Type())
adminAccessManagementConsoleEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:adminAccessManagementConsoleEnabled.setStatus(_B)
_ColubrisSystemMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
colubrisSystemMIBNotificationPrefix=_ColubrisSystemMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,8744,5,6,2))
_ColubrisSystemMIBNotifications_ObjectIdentity=ObjectIdentity
colubrisSystemMIBNotifications=_ColubrisSystemMIBNotifications_ObjectIdentity((1,3,6,1,4,1,8744,5,6,2,0))
_ColubrisSystemMIBConformance_ObjectIdentity=ObjectIdentity
colubrisSystemMIBConformance=_ColubrisSystemMIBConformance_ObjectIdentity((1,3,6,1,4,1,8744,5,6,3))
_ColubrisSystemMIBCompliances_ObjectIdentity=ObjectIdentity
colubrisSystemMIBCompliances=_ColubrisSystemMIBCompliances_ObjectIdentity((1,3,6,1,4,1,8744,5,6,3,1))
_ColubrisSystemMIBGroups_ObjectIdentity=ObjectIdentity
colubrisSystemMIBGroups=_ColubrisSystemMIBGroups_ObjectIdentity((1,3,6,1,4,1,8744,5,6,3,2))
colubrisSystemMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,6,3,2,1))
colubrisSystemMIBGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_g),(_A,_h),(_A,_N),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_W),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:colubrisSystemMIBGroup.setStatus(_B)
colubrisAdminAccessProfileGroup=ObjectGroup((1,3,6,1,4,1,8744,5,6,3,2,2))
colubrisAdminAccessProfileGroup.setObjects(*((_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_O),(_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:colubrisAdminAccessProfileGroup.setStatus(_B)
colubrisSystemMIBDeprecatedGroup=ObjectGroup((1,3,6,1,4,1,8744,5,6,3,2,6))
colubrisSystemMIBDeprecatedGroup.setObjects((_A,_A5))
if mibBuilder.loadTexts:colubrisSystemMIBDeprecatedGroup.setStatus(_M)
colubrisAdminAccessManagementConsoleGroup=ObjectGroup((1,3,6,1,4,1,8744,5,6,3,2,7))
colubrisAdminAccessManagementConsoleGroup.setObjects(*((_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:colubrisAdminAccessManagementConsoleGroup.setStatus(_B)
adminAccessAuthFailureNotification=NotificationType((1,3,6,1,4,1,8744,5,6,2,0,1))
adminAccessAuthFailureNotification.setObjects((_A,_O))
if mibBuilder.loadTexts:adminAccessAuthFailureNotification.setStatus(_B)
adminAccessLoginNotification=NotificationType((1,3,6,1,4,1,8744,5,6,2,0,2))
if mibBuilder.loadTexts:adminAccessLoginNotification.setStatus(_B)
systemColdStart=NotificationType((1,3,6,1,4,1,8744,5,6,2,0,3))
systemColdStart.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_N)))
if mibBuilder.loadTexts:systemColdStart.setStatus(_B)
systemHeartbeatNotification=NotificationType((1,3,6,1,4,1,8744,5,6,2,0,4))
systemHeartbeatNotification.setObjects(*((_A,_N),(_A,_U),(_A,_V),(_A,_T),(_E,_L),(_E,_J),(_E,_K),(_E,_I),(_E,_L),(_E,_J),(_E,_K),(_E,_I),(_E,_L),(_E,_J),(_E,_K),(_E,_I)))
if mibBuilder.loadTexts:systemHeartbeatNotification.setStatus(_B)
adminAccessLogoutNotification=NotificationType((1,3,6,1,4,1,8744,5,6,2,0,5))
adminAccessLogoutNotification.setObjects((_A,_O))
if mibBuilder.loadTexts:adminAccessLogoutNotification.setStatus(_B)
timeServerFailure=NotificationType((1,3,6,1,4,1,8744,5,6,2,0,6))
timeServerFailure.setObjects((_A,_W))
if mibBuilder.loadTexts:timeServerFailure.setStatus(_B)
colubrisSystemNotificationGroup=NotificationGroup((1,3,6,1,4,1,8744,5,6,3,2,3))
colubrisSystemNotificationGroup.setObjects(*((_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:colubrisSystemNotificationGroup.setStatus(_B)
colubrisAdminAccessNotificationGroup=NotificationGroup((1,3,6,1,4,1,8744,5,6,3,2,4))
colubrisAdminAccessNotificationGroup.setObjects(*((_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:colubrisAdminAccessNotificationGroup.setStatus(_B)
colubrisTimeNotificationGroup=NotificationGroup((1,3,6,1,4,1,8744,5,6,3,2,5))
colubrisTimeNotificationGroup.setObjects((_A,_AD))
if mibBuilder.loadTexts:colubrisTimeNotificationGroup.setStatus(_B)
colubrisSystemMIBCompliance=ModuleCompliance((1,3,6,1,4,1,8744,5,6,3,1,1))
colubrisSystemMIBCompliance.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:colubrisSystemMIBCompliance.setStatus(_M)
colubrisSystemMIBComplianceDeprecated=ModuleCompliance((1,3,6,1,4,1,8744,5,6,3,1,2))
colubrisSystemMIBComplianceDeprecated.setObjects((_A,_AE))
if mibBuilder.loadTexts:colubrisSystemMIBComplianceDeprecated.setStatus(_M)
colubrisSystemMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,8744,5,6,3,1,3))
colubrisSystemMIBCompliance2.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_AF)))
if mibBuilder.loadTexts:colubrisSystemMIBCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'colubrisSystemMIB':colubrisSystemMIB,'colubrisSystemMIBObjects':colubrisSystemMIBObjects,'systemInfo':systemInfo,_Q:systemProductName,_R:systemFirmwareRevision,_g:systemBootRevision,_h:systemHardwareRevision,_N:systemSerialNumber,_S:systemConfigurationVersion,_T:systemUpTime,_U:systemMacAddress,_V:systemWanPortIpAddress,_i:systemProductFlavor,_j:systemDeviceIdentification,_k:systemFirmwareBuildDate,_l:systemControllerMode,_m:systemCDPOperState,_n:systemLLDPOperState,'systemTime':systemTime,_o:systemTimeUpdateMode,_p:systemTimeLostWhenRebooting,_A5:systemTimeDSTOn,_q:systemDate,_r:systemTimeOfDay,_s:systemTimeZone,'systemTimeServerTable':systemTimeServerTable,'systemTimeServerEntry':systemTimeServerEntry,_d:systemTimeServerIndex,_W:systemTimeServerAddress,_t:systemTimeServerNotificationEnabled,'adminAccess':adminAccess,_w:adminAccessAuthenMode,_A1:adminAccessAuthenProfileIndex,_x:adminAccessMaxLoginAttempts,_y:adminAccessLockOutPeriod,_z:adminAccessLoginNotificationEnabled,_A0:adminAccessAuthFailureNotificationEnabled,_O:adminAccessInfo,'adminAccessProfileTable':adminAccessProfileTable,'adminAccessProfileEntry':adminAccessProfileEntry,_f:adminAccessProfileIndex,_A2:adminAccessUserName,_A3:adminAccessAdministrativeRights,_A4:adminAccessLogoutNotificationEnabled,'heartbeat':heartbeat,_u:heartbeatPeriod,_v:heartbeatNotificationEnabled,'managementConsole':managementConsole,_A6:adminAccessManagementConsole,_A7:adminAccessManagementConsoleEnabled,'colubrisSystemMIBNotificationPrefix':colubrisSystemMIBNotificationPrefix,'colubrisSystemMIBNotifications':colubrisSystemMIBNotifications,_AA:adminAccessAuthFailureNotification,_AB:adminAccessLoginNotification,_A8:systemColdStart,_A9:systemHeartbeatNotification,_AC:adminAccessLogoutNotification,_AD:timeServerFailure,'colubrisSystemMIBConformance':colubrisSystemMIBConformance,'colubrisSystemMIBCompliances':colubrisSystemMIBCompliances,'colubrisSystemMIBCompliance':colubrisSystemMIBCompliance,'colubrisSystemMIBComplianceDeprecated':colubrisSystemMIBComplianceDeprecated,'colubrisSystemMIBCompliance2':colubrisSystemMIBCompliance2,'colubrisSystemMIBGroups':colubrisSystemMIBGroups,_X:colubrisSystemMIBGroup,_Z:colubrisAdminAccessProfileGroup,_Y:colubrisSystemNotificationGroup,_a:colubrisAdminAccessNotificationGroup,_b:colubrisTimeNotificationGroup,_AE:colubrisSystemMIBDeprecatedGroup,_AF:colubrisAdminAccessManagementConsoleGroup})