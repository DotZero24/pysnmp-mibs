_A6='alvarionTimeNotificationGroup'
_A5='alvarionAdminAccessNotificationGroup'
_A4='alvarionAdminAccessProfileGroup'
_A3='alvarionSystemNotificationGroup'
_A2='alvarionSystemMIBGroup'
_A1='timeServerFailure'
_A0='adminAccessLogoutNotification'
_z='adminAccessLoginNotification'
_y='adminAccessAuthFailureNotification'
_x='systemHeartbeatNotification'
_w='systemColdStart'
_v='adminAccessLogoutNotificationEnabled'
_u='adminAccessAdministrativeRights'
_t='adminAccessUserName'
_s='adminAccessAuthenProfileIndex'
_r='adminAccessAuthFailureNotificationEnabled'
_q='adminAccessLoginNotificationEnabled'
_p='adminAccessLockOutPeriod'
_o='adminAccessMaxLoginAttempts'
_n='adminAccessAuthenMode'
_m='heartbeatNotificationEnabled'
_l='heartbeatPeriod'
_k='systemTimeServerNotificationEnabled'
_j='systemTimeZone'
_i='systemTimeOfDay'
_h='systemDate'
_g='systemTimeDSTOn'
_f='systemTimeLostWhenRebooting'
_e='systemTimeUpdateMode'
_d='systemDeviceIdentification'
_c='systemProductFlavor'
_b='systemHardwareRevision'
_a='systemBootRevision'
_Z='adminAccessProfileIndex'
_Y='not-accessible'
_X='systemTimeServerIndex'
_W='seconds'
_V='systemTimeServerAddress'
_U='systemWanPortIpAddress'
_T='systemMacAddress'
_S='systemUpTime'
_R='systemConfigurationVersion'
_Q='systemFirmwareRevision'
_P='systemProductName'
_O='accessible-for-notify'
_N='adminAccessInfo'
_M='systemSerialNumber'
_L='ifOutUcastPkts'
_K='ifOutErrors'
_J='ifInUcastPkts'
_I='ifInErrors'
_H='AlvarionNotificationEnable'
_G='OctetString'
_F='Integer32'
_E='read-only'
_D='IF-MIB'
_C='read-write'
_B='current'
_A='ALVARION-SYSTEM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alvarionMgmtV2,=mibBuilder.importSymbols('ALVARION-SMI','alvarionMgmtV2')
AlvarionAuthenticationMode,AlvarionNotificationEnable,AlvarionProfileIndexOrZero=mibBuilder.importSymbols('ALVARION-TC','AlvarionAuthenticationMode',_H,'AlvarionProfileIndexOrZero')
ifInErrors,ifInUcastPkts,ifOutErrors,ifOutUcastPkts=mibBuilder.importSymbols(_D,_I,_J,_K,_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
alvarionSystemMIB=ModuleIdentity((1,3,6,1,4,1,12394,1,10,5,6))
_AlvarionSystemMIBObjects_ObjectIdentity=ObjectIdentity
alvarionSystemMIBObjects=_AlvarionSystemMIBObjects_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,6,1))
_SystemInfo_ObjectIdentity=ObjectIdentity
systemInfo=_SystemInfo_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,6,1,1))
_SystemProductName_Type=DisplayString
_SystemProductName_Object=MibScalar
systemProductName=_SystemProductName_Object((1,3,6,1,4,1,12394,1,10,5,6,1,1,1),_SystemProductName_Type())
systemProductName.setMaxAccess(_E)
if mibBuilder.loadTexts:systemProductName.setStatus(_B)
_SystemFirmwareRevision_Type=DisplayString
_SystemFirmwareRevision_Object=MibScalar
systemFirmwareRevision=_SystemFirmwareRevision_Object((1,3,6,1,4,1,12394,1,10,5,6,1,1,2),_SystemFirmwareRevision_Type())
systemFirmwareRevision.setMaxAccess(_E)
if mibBuilder.loadTexts:systemFirmwareRevision.setStatus(_B)
_SystemBootRevision_Type=DisplayString
_SystemBootRevision_Object=MibScalar
systemBootRevision=_SystemBootRevision_Object((1,3,6,1,4,1,12394,1,10,5,6,1,1,3),_SystemBootRevision_Type())
systemBootRevision.setMaxAccess(_E)
if mibBuilder.loadTexts:systemBootRevision.setStatus(_B)
_SystemHardwareRevision_Type=DisplayString
_SystemHardwareRevision_Object=MibScalar
systemHardwareRevision=_SystemHardwareRevision_Object((1,3,6,1,4,1,12394,1,10,5,6,1,1,4),_SystemHardwareRevision_Type())
systemHardwareRevision.setMaxAccess(_E)
if mibBuilder.loadTexts:systemHardwareRevision.setStatus(_B)
_SystemSerialNumber_Type=DisplayString
_SystemSerialNumber_Object=MibScalar
systemSerialNumber=_SystemSerialNumber_Object((1,3,6,1,4,1,12394,1,10,5,6,1,1,5),_SystemSerialNumber_Type())
systemSerialNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:systemSerialNumber.setStatus(_B)
_SystemConfigurationVersion_Type=DisplayString
_SystemConfigurationVersion_Object=MibScalar
systemConfigurationVersion=_SystemConfigurationVersion_Object((1,3,6,1,4,1,12394,1,10,5,6,1,1,6),_SystemConfigurationVersion_Type())
systemConfigurationVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:systemConfigurationVersion.setStatus(_B)
_SystemUpTime_Type=Counter32
_SystemUpTime_Object=MibScalar
systemUpTime=_SystemUpTime_Object((1,3,6,1,4,1,12394,1,10,5,6,1,1,7),_SystemUpTime_Type())
systemUpTime.setMaxAccess(_E)
if mibBuilder.loadTexts:systemUpTime.setStatus(_B)
if mibBuilder.loadTexts:systemUpTime.setUnits(_W)
_SystemMacAddress_Type=MacAddress
_SystemMacAddress_Object=MibScalar
systemMacAddress=_SystemMacAddress_Object((1,3,6,1,4,1,12394,1,10,5,6,1,1,8),_SystemMacAddress_Type())
systemMacAddress.setMaxAccess(_O)
if mibBuilder.loadTexts:systemMacAddress.setStatus(_B)
_SystemWanPortIpAddress_Type=IpAddress
_SystemWanPortIpAddress_Object=MibScalar
systemWanPortIpAddress=_SystemWanPortIpAddress_Object((1,3,6,1,4,1,12394,1,10,5,6,1,1,9),_SystemWanPortIpAddress_Type())
systemWanPortIpAddress.setMaxAccess(_O)
if mibBuilder.loadTexts:systemWanPortIpAddress.setStatus(_B)
_SystemProductFlavor_Type=DisplayString
_SystemProductFlavor_Object=MibScalar
systemProductFlavor=_SystemProductFlavor_Object((1,3,6,1,4,1,12394,1,10,5,6,1,1,10),_SystemProductFlavor_Type())
systemProductFlavor.setMaxAccess(_E)
if mibBuilder.loadTexts:systemProductFlavor.setStatus(_B)
_SystemDeviceIdentification_Type=MacAddress
_SystemDeviceIdentification_Object=MibScalar
systemDeviceIdentification=_SystemDeviceIdentification_Object((1,3,6,1,4,1,12394,1,10,5,6,1,1,11),_SystemDeviceIdentification_Type())
systemDeviceIdentification.setMaxAccess(_E)
if mibBuilder.loadTexts:systemDeviceIdentification.setStatus(_B)
_SystemTime_ObjectIdentity=ObjectIdentity
systemTime=_SystemTime_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,6,1,2))
class _SystemTimeUpdateMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('manual',1),('sntpUdp',2),('tp',3)))
_SystemTimeUpdateMode_Type.__name__=_F
_SystemTimeUpdateMode_Object=MibScalar
systemTimeUpdateMode=_SystemTimeUpdateMode_Object((1,3,6,1,4,1,12394,1,10,5,6,1,2,1),_SystemTimeUpdateMode_Type())
systemTimeUpdateMode.setMaxAccess(_C)
if mibBuilder.loadTexts:systemTimeUpdateMode.setStatus(_B)
_SystemTimeLostWhenRebooting_Type=TruthValue
_SystemTimeLostWhenRebooting_Object=MibScalar
systemTimeLostWhenRebooting=_SystemTimeLostWhenRebooting_Object((1,3,6,1,4,1,12394,1,10,5,6,1,2,2),_SystemTimeLostWhenRebooting_Type())
systemTimeLostWhenRebooting.setMaxAccess(_E)
if mibBuilder.loadTexts:systemTimeLostWhenRebooting.setStatus(_B)
_SystemTimeDSTOn_Type=TruthValue
_SystemTimeDSTOn_Object=MibScalar
systemTimeDSTOn=_SystemTimeDSTOn_Object((1,3,6,1,4,1,12394,1,10,5,6,1,2,3),_SystemTimeDSTOn_Type())
systemTimeDSTOn.setMaxAccess(_C)
if mibBuilder.loadTexts:systemTimeDSTOn.setStatus(_B)
class _SystemDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_SystemDate_Type.__name__=_G
_SystemDate_Object=MibScalar
systemDate=_SystemDate_Object((1,3,6,1,4,1,12394,1,10,5,6,1,2,4),_SystemDate_Type())
systemDate.setMaxAccess(_C)
if mibBuilder.loadTexts:systemDate.setStatus(_B)
class _SystemTimeOfDay_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SystemTimeOfDay_Type.__name__=_G
_SystemTimeOfDay_Object=MibScalar
systemTimeOfDay=_SystemTimeOfDay_Object((1,3,6,1,4,1,12394,1,10,5,6,1,2,5),_SystemTimeOfDay_Type())
systemTimeOfDay.setMaxAccess(_C)
if mibBuilder.loadTexts:systemTimeOfDay.setStatus(_B)
class _SystemTimeZone_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SystemTimeZone_Type.__name__=_G
_SystemTimeZone_Object=MibScalar
systemTimeZone=_SystemTimeZone_Object((1,3,6,1,4,1,12394,1,10,5,6,1,2,6),_SystemTimeZone_Type())
systemTimeZone.setMaxAccess(_C)
if mibBuilder.loadTexts:systemTimeZone.setStatus(_B)
_SystemTimeServerTable_Object=MibTable
systemTimeServerTable=_SystemTimeServerTable_Object((1,3,6,1,4,1,12394,1,10,5,6,1,2,7))
if mibBuilder.loadTexts:systemTimeServerTable.setStatus(_B)
_SystemTimeServerEntry_Object=MibTableRow
systemTimeServerEntry=_SystemTimeServerEntry_Object((1,3,6,1,4,1,12394,1,10,5,6,1,2,7,1))
systemTimeServerEntry.setIndexNames((0,_A,_X))
if mibBuilder.loadTexts:systemTimeServerEntry.setStatus(_B)
class _SystemTimeServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_SystemTimeServerIndex_Type.__name__=_F
_SystemTimeServerIndex_Object=MibTableColumn
systemTimeServerIndex=_SystemTimeServerIndex_Object((1,3,6,1,4,1,12394,1,10,5,6,1,2,7,1,1),_SystemTimeServerIndex_Type())
systemTimeServerIndex.setMaxAccess(_Y)
if mibBuilder.loadTexts:systemTimeServerIndex.setStatus(_B)
_SystemTimeServerAddress_Type=DisplayString
_SystemTimeServerAddress_Object=MibTableColumn
systemTimeServerAddress=_SystemTimeServerAddress_Object((1,3,6,1,4,1,12394,1,10,5,6,1,2,7,1,2),_SystemTimeServerAddress_Type())
systemTimeServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:systemTimeServerAddress.setStatus(_B)
_SystemTimeServerNotificationEnabled_Type=AlvarionNotificationEnable
_SystemTimeServerNotificationEnabled_Object=MibScalar
systemTimeServerNotificationEnabled=_SystemTimeServerNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,6,1,2,8),_SystemTimeServerNotificationEnabled_Type())
systemTimeServerNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:systemTimeServerNotificationEnabled.setStatus(_B)
_AdminAccess_ObjectIdentity=ObjectIdentity
adminAccess=_AdminAccess_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,6,1,3))
_AdminAccessAuthenMode_Type=AlvarionAuthenticationMode
_AdminAccessAuthenMode_Object=MibScalar
adminAccessAuthenMode=_AdminAccessAuthenMode_Object((1,3,6,1,4,1,12394,1,10,5,6,1,3,1),_AdminAccessAuthenMode_Type())
adminAccessAuthenMode.setMaxAccess(_C)
if mibBuilder.loadTexts:adminAccessAuthenMode.setStatus(_B)
_AdminAccessAuthenProfileIndex_Type=AlvarionProfileIndexOrZero
_AdminAccessAuthenProfileIndex_Object=MibScalar
adminAccessAuthenProfileIndex=_AdminAccessAuthenProfileIndex_Object((1,3,6,1,4,1,12394,1,10,5,6,1,3,2),_AdminAccessAuthenProfileIndex_Type())
adminAccessAuthenProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:adminAccessAuthenProfileIndex.setStatus(_B)
class _AdminAccessMaxLoginAttempts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_AdminAccessMaxLoginAttempts_Type.__name__=_F
_AdminAccessMaxLoginAttempts_Object=MibScalar
adminAccessMaxLoginAttempts=_AdminAccessMaxLoginAttempts_Object((1,3,6,1,4,1,12394,1,10,5,6,1,3,3),_AdminAccessMaxLoginAttempts_Type())
adminAccessMaxLoginAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:adminAccessMaxLoginAttempts.setStatus(_B)
class _AdminAccessLockOutPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_AdminAccessLockOutPeriod_Type.__name__=_F
_AdminAccessLockOutPeriod_Object=MibScalar
adminAccessLockOutPeriod=_AdminAccessLockOutPeriod_Object((1,3,6,1,4,1,12394,1,10,5,6,1,3,4),_AdminAccessLockOutPeriod_Type())
adminAccessLockOutPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:adminAccessLockOutPeriod.setStatus(_B)
if mibBuilder.loadTexts:adminAccessLockOutPeriod.setUnits('minutes')
class _AdminAccessLoginNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=1
_AdminAccessLoginNotificationEnabled_Type.__name__=_H
_AdminAccessLoginNotificationEnabled_Object=MibScalar
adminAccessLoginNotificationEnabled=_AdminAccessLoginNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,6,1,3,5),_AdminAccessLoginNotificationEnabled_Type())
adminAccessLoginNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:adminAccessLoginNotificationEnabled.setStatus(_B)
class _AdminAccessAuthFailureNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=1
_AdminAccessAuthFailureNotificationEnabled_Type.__name__=_H
_AdminAccessAuthFailureNotificationEnabled_Object=MibScalar
adminAccessAuthFailureNotificationEnabled=_AdminAccessAuthFailureNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,6,1,3,6),_AdminAccessAuthFailureNotificationEnabled_Type())
adminAccessAuthFailureNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:adminAccessAuthFailureNotificationEnabled.setStatus(_B)
_AdminAccessInfo_Type=DisplayString
_AdminAccessInfo_Object=MibScalar
adminAccessInfo=_AdminAccessInfo_Object((1,3,6,1,4,1,12394,1,10,5,6,1,3,7),_AdminAccessInfo_Type())
adminAccessInfo.setMaxAccess(_O)
if mibBuilder.loadTexts:adminAccessInfo.setStatus(_B)
_AdminAccessProfileTable_Object=MibTable
adminAccessProfileTable=_AdminAccessProfileTable_Object((1,3,6,1,4,1,12394,1,10,5,6,1,3,8))
if mibBuilder.loadTexts:adminAccessProfileTable.setStatus(_B)
_AdminAccessProfileEntry_Object=MibTableRow
adminAccessProfileEntry=_AdminAccessProfileEntry_Object((1,3,6,1,4,1,12394,1,10,5,6,1,3,8,1))
adminAccessProfileEntry.setIndexNames((0,_A,_Z))
if mibBuilder.loadTexts:adminAccessProfileEntry.setStatus(_B)
class _AdminAccessProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AdminAccessProfileIndex_Type.__name__=_F
_AdminAccessProfileIndex_Object=MibTableColumn
adminAccessProfileIndex=_AdminAccessProfileIndex_Object((1,3,6,1,4,1,12394,1,10,5,6,1,3,8,1,1),_AdminAccessProfileIndex_Type())
adminAccessProfileIndex.setMaxAccess(_Y)
if mibBuilder.loadTexts:adminAccessProfileIndex.setStatus(_B)
class _AdminAccessUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,253))
_AdminAccessUserName_Type.__name__=_G
_AdminAccessUserName_Object=MibTableColumn
adminAccessUserName=_AdminAccessUserName_Object((1,3,6,1,4,1,12394,1,10,5,6,1,3,8,1,2),_AdminAccessUserName_Type())
adminAccessUserName.setMaxAccess(_E)
if mibBuilder.loadTexts:adminAccessUserName.setStatus(_B)
class _AdminAccessAdministrativeRights_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('readOnly',1),('readWrite',2)))
_AdminAccessAdministrativeRights_Type.__name__=_F
_AdminAccessAdministrativeRights_Object=MibTableColumn
adminAccessAdministrativeRights=_AdminAccessAdministrativeRights_Object((1,3,6,1,4,1,12394,1,10,5,6,1,3,8,1,3),_AdminAccessAdministrativeRights_Type())
adminAccessAdministrativeRights.setMaxAccess(_E)
if mibBuilder.loadTexts:adminAccessAdministrativeRights.setStatus(_B)
class _AdminAccessLogoutNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=1
_AdminAccessLogoutNotificationEnabled_Type.__name__=_H
_AdminAccessLogoutNotificationEnabled_Object=MibScalar
adminAccessLogoutNotificationEnabled=_AdminAccessLogoutNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,6,1,3,9),_AdminAccessLogoutNotificationEnabled_Type())
adminAccessLogoutNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:adminAccessLogoutNotificationEnabled.setStatus(_B)
_Heartbeat_ObjectIdentity=ObjectIdentity
heartbeat=_Heartbeat_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,6,1,4))
class _HeartbeatPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,31536000))
_HeartbeatPeriod_Type.__name__=_F
_HeartbeatPeriod_Object=MibScalar
heartbeatPeriod=_HeartbeatPeriod_Object((1,3,6,1,4,1,12394,1,10,5,6,1,4,1),_HeartbeatPeriod_Type())
heartbeatPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:heartbeatPeriod.setStatus(_B)
if mibBuilder.loadTexts:heartbeatPeriod.setUnits(_W)
class _HeartbeatNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=1
_HeartbeatNotificationEnabled_Type.__name__=_H
_HeartbeatNotificationEnabled_Object=MibScalar
heartbeatNotificationEnabled=_HeartbeatNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,6,1,4,2),_HeartbeatNotificationEnabled_Type())
heartbeatNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:heartbeatNotificationEnabled.setStatus(_B)
_AlvarionSystemMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
alvarionSystemMIBNotificationPrefix=_AlvarionSystemMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,6,2))
_AlvarionSystemMIBNotifications_ObjectIdentity=ObjectIdentity
alvarionSystemMIBNotifications=_AlvarionSystemMIBNotifications_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,6,2,0))
_AlvarionSystemMIBConformance_ObjectIdentity=ObjectIdentity
alvarionSystemMIBConformance=_AlvarionSystemMIBConformance_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,6,3))
_AlvarionSystemMIBCompliances_ObjectIdentity=ObjectIdentity
alvarionSystemMIBCompliances=_AlvarionSystemMIBCompliances_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,6,3,1))
_AlvarionSystemMIBGroups_ObjectIdentity=ObjectIdentity
alvarionSystemMIBGroups=_AlvarionSystemMIBGroups_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,6,3,2))
alvarionSystemMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,6,3,2,1))
alvarionSystemMIBGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_a),(_A,_b),(_A,_M),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_V),(_A,_k),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:alvarionSystemMIBGroup.setStatus(_B)
alvarionAdminAccessProfileGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,6,3,2,2))
alvarionAdminAccessProfileGroup.setObjects(*((_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_N),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:alvarionAdminAccessProfileGroup.setStatus(_B)
adminAccessAuthFailureNotification=NotificationType((1,3,6,1,4,1,12394,1,10,5,6,2,0,1))
adminAccessAuthFailureNotification.setObjects((_A,_N))
if mibBuilder.loadTexts:adminAccessAuthFailureNotification.setStatus(_B)
adminAccessLoginNotification=NotificationType((1,3,6,1,4,1,12394,1,10,5,6,2,0,2))
if mibBuilder.loadTexts:adminAccessLoginNotification.setStatus(_B)
systemColdStart=NotificationType((1,3,6,1,4,1,12394,1,10,5,6,2,0,3))
systemColdStart.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_M)))
if mibBuilder.loadTexts:systemColdStart.setStatus(_B)
systemHeartbeatNotification=NotificationType((1,3,6,1,4,1,12394,1,10,5,6,2,0,4))
systemHeartbeatNotification.setObjects(*((_A,_M),(_A,_T),(_A,_U),(_A,_S),(_D,_L),(_D,_J),(_D,_K),(_D,_I),(_D,_L),(_D,_J),(_D,_K),(_D,_I),(_D,_L),(_D,_J),(_D,_K),(_D,_I)))
if mibBuilder.loadTexts:systemHeartbeatNotification.setStatus(_B)
adminAccessLogoutNotification=NotificationType((1,3,6,1,4,1,12394,1,10,5,6,2,0,5))
adminAccessLogoutNotification.setObjects((_A,_N))
if mibBuilder.loadTexts:adminAccessLogoutNotification.setStatus(_B)
timeServerFailure=NotificationType((1,3,6,1,4,1,12394,1,10,5,6,2,0,6))
timeServerFailure.setObjects((_A,_V))
if mibBuilder.loadTexts:timeServerFailure.setStatus(_B)
alvarionSystemNotificationGroup=NotificationGroup((1,3,6,1,4,1,12394,1,10,5,6,3,2,3))
alvarionSystemNotificationGroup.setObjects(*((_A,_w),(_A,_x)))
if mibBuilder.loadTexts:alvarionSystemNotificationGroup.setStatus(_B)
alvarionAdminAccessNotificationGroup=NotificationGroup((1,3,6,1,4,1,12394,1,10,5,6,3,2,4))
alvarionAdminAccessNotificationGroup.setObjects(*((_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:alvarionAdminAccessNotificationGroup.setStatus(_B)
alvarionTimeNotificationGroup=NotificationGroup((1,3,6,1,4,1,12394,1,10,5,6,3,2,5))
alvarionTimeNotificationGroup.setObjects((_A,_A1))
if mibBuilder.loadTexts:alvarionTimeNotificationGroup.setStatus(_B)
alvarionSystemMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12394,1,10,5,6,3,1,1))
alvarionSystemMIBCompliance.setObjects(*((_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:alvarionSystemMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'alvarionSystemMIB':alvarionSystemMIB,'alvarionSystemMIBObjects':alvarionSystemMIBObjects,'systemInfo':systemInfo,_P:systemProductName,_Q:systemFirmwareRevision,_a:systemBootRevision,_b:systemHardwareRevision,_M:systemSerialNumber,_R:systemConfigurationVersion,_S:systemUpTime,_T:systemMacAddress,_U:systemWanPortIpAddress,_c:systemProductFlavor,_d:systemDeviceIdentification,'systemTime':systemTime,_e:systemTimeUpdateMode,_f:systemTimeLostWhenRebooting,_g:systemTimeDSTOn,_h:systemDate,_i:systemTimeOfDay,_j:systemTimeZone,'systemTimeServerTable':systemTimeServerTable,'systemTimeServerEntry':systemTimeServerEntry,_X:systemTimeServerIndex,_V:systemTimeServerAddress,_k:systemTimeServerNotificationEnabled,'adminAccess':adminAccess,_n:adminAccessAuthenMode,_s:adminAccessAuthenProfileIndex,_o:adminAccessMaxLoginAttempts,_p:adminAccessLockOutPeriod,_q:adminAccessLoginNotificationEnabled,_r:adminAccessAuthFailureNotificationEnabled,_N:adminAccessInfo,'adminAccessProfileTable':adminAccessProfileTable,'adminAccessProfileEntry':adminAccessProfileEntry,_Z:adminAccessProfileIndex,_t:adminAccessUserName,_u:adminAccessAdministrativeRights,_v:adminAccessLogoutNotificationEnabled,'heartbeat':heartbeat,_l:heartbeatPeriod,_m:heartbeatNotificationEnabled,'alvarionSystemMIBNotificationPrefix':alvarionSystemMIBNotificationPrefix,'alvarionSystemMIBNotifications':alvarionSystemMIBNotifications,_y:adminAccessAuthFailureNotification,_z:adminAccessLoginNotification,_w:systemColdStart,_x:systemHeartbeatNotification,_A0:adminAccessLogoutNotification,_A1:timeServerFailure,'alvarionSystemMIBConformance':alvarionSystemMIBConformance,'alvarionSystemMIBCompliances':alvarionSystemMIBCompliances,'alvarionSystemMIBCompliance':alvarionSystemMIBCompliance,'alvarionSystemMIBGroups':alvarionSystemMIBGroups,_A2:alvarionSystemMIBGroup,_A4:alvarionAdminAccessProfileGroup,_A3:alvarionSystemNotificationGroup,_A5:alvarionAdminAccessNotificationGroup,_A6:alvarionTimeNotificationGroup})