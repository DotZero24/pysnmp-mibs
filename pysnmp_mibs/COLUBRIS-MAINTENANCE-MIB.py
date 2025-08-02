_A0='colubrisMaintenanceNotificationGroup'
_z='colubrisMaintenanceMIBGroup'
_y='certificateExpiredNotification'
_x='certificateAboutToExpireNotification'
_w='configurationLocalUpdateNotification'
_v='configurationUpdateNotification'
_u='firmwareUpdateNotification'
_t='certificateExpiredNotificationEnabled'
_s='certificateAboutToExpireNotificationEnabled'
_r='configurationUpdateStatus'
_q='configurationLocalUpdateNotificationEnabled'
_p='configurationRestart'
_o='configurationFactoryDefaults'
_n='configurationUpdateNotificationEnabled'
_m='configurationUpdateOperation'
_l='configurationUpdateInitiate'
_k='configurationUpdateLocation'
_j='configurationUpdateTime'
_i='configurationUpdateDay'
_h='configurationPeriodicUpdate'
_g='firmwareUpdateStatus'
_f='firmwareUpdateNotificationEnabled'
_e='firmwareUpdateInitiate'
_d='firmwareUpdateLocation'
_c='firmwareUpdateTime'
_b='firmwareUpdateDay'
_a='firmwarePeriodicUpdate'
_Z='failure'
_Y='success'
_X='inprogress'
_W='update'
_V='everyday'
_U='sunday'
_T='saturday'
_S='friday'
_R='thursday'
_Q='wednesday'
_P='tuesday'
_O='monday'
_N='systemFirmwareRevision'
_M='systemConfigurationVersion'
_L='firmwareUpdateInfo'
_K='COLUBRIS-SYSTEM-MIB'
_J='OctetString'
_I='certificateExpiryDate'
_H='configurationUpdateInfo'
_G='read-only'
_F='idle'
_E='ColubrisNotificationEnable'
_D='Integer32'
_C='read-write'
_B='current'
_A='COLUBRIS-MAINTENANCE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
colubrisMgmtV2,=mibBuilder.importSymbols('COLUBRIS-SMI','colubrisMgmtV2')
systemConfigurationVersion,systemFirmwareRevision=mibBuilder.importSymbols(_K,_M,_N)
ColubrisNotificationEnable,=mibBuilder.importSymbols('COLUBRIS-TC',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
colubrisMaintenanceMIB=ModuleIdentity((1,3,6,1,4,1,8744,5,2))
_ColubrisMaintenanceMIBObjects_ObjectIdentity=ObjectIdentity
colubrisMaintenanceMIBObjects=_ColubrisMaintenanceMIBObjects_ObjectIdentity((1,3,6,1,4,1,8744,5,2,1))
_FirmwareUpdate_ObjectIdentity=ObjectIdentity
firmwareUpdate=_FirmwareUpdate_ObjectIdentity((1,3,6,1,4,1,8744,5,2,1,1))
_FirmwarePeriodicUpdate_Type=TruthValue
_FirmwarePeriodicUpdate_Object=MibScalar
firmwarePeriodicUpdate=_FirmwarePeriodicUpdate_Object((1,3,6,1,4,1,8744,5,2,1,1,1),_FirmwarePeriodicUpdate_Type())
firmwarePeriodicUpdate.setMaxAccess(_C)
if mibBuilder.loadTexts:firmwarePeriodicUpdate.setStatus(_B)
class _FirmwareUpdateDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8)))
_FirmwareUpdateDay_Type.__name__=_D
_FirmwareUpdateDay_Object=MibScalar
firmwareUpdateDay=_FirmwareUpdateDay_Object((1,3,6,1,4,1,8744,5,2,1,1,2),_FirmwareUpdateDay_Type())
firmwareUpdateDay.setMaxAccess(_C)
if mibBuilder.loadTexts:firmwareUpdateDay.setStatus(_B)
class _FirmwareUpdateTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_FirmwareUpdateTime_Type.__name__=_J
_FirmwareUpdateTime_Object=MibScalar
firmwareUpdateTime=_FirmwareUpdateTime_Object((1,3,6,1,4,1,8744,5,2,1,1,3),_FirmwareUpdateTime_Type())
firmwareUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:firmwareUpdateTime.setStatus(_B)
_FirmwareUpdateLocation_Type=DisplayString
_FirmwareUpdateLocation_Object=MibScalar
firmwareUpdateLocation=_FirmwareUpdateLocation_Object((1,3,6,1,4,1,8744,5,2,1,1,4),_FirmwareUpdateLocation_Type())
firmwareUpdateLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:firmwareUpdateLocation.setStatus(_B)
class _FirmwareUpdateInitiate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_W,1)))
_FirmwareUpdateInitiate_Type.__name__=_D
_FirmwareUpdateInitiate_Object=MibScalar
firmwareUpdateInitiate=_FirmwareUpdateInitiate_Object((1,3,6,1,4,1,8744,5,2,1,1,5),_FirmwareUpdateInitiate_Type())
firmwareUpdateInitiate.setMaxAccess(_C)
if mibBuilder.loadTexts:firmwareUpdateInitiate.setStatus(_B)
class _FirmwareUpdateNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=1
_FirmwareUpdateNotificationEnabled_Type.__name__=_E
_FirmwareUpdateNotificationEnabled_Object=MibScalar
firmwareUpdateNotificationEnabled=_FirmwareUpdateNotificationEnabled_Object((1,3,6,1,4,1,8744,5,2,1,1,6),_FirmwareUpdateNotificationEnabled_Type())
firmwareUpdateNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:firmwareUpdateNotificationEnabled.setStatus(_B)
_FirmwareUpdateInfo_Type=DisplayString
_FirmwareUpdateInfo_Object=MibScalar
firmwareUpdateInfo=_FirmwareUpdateInfo_Object((1,3,6,1,4,1,8744,5,2,1,1,7),_FirmwareUpdateInfo_Type())
firmwareUpdateInfo.setMaxAccess(_G)
if mibBuilder.loadTexts:firmwareUpdateInfo.setStatus(_B)
class _FirmwareUpdateStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_X,2),(_Y,3),(_Z,4)))
_FirmwareUpdateStatus_Type.__name__=_D
_FirmwareUpdateStatus_Object=MibScalar
firmwareUpdateStatus=_FirmwareUpdateStatus_Object((1,3,6,1,4,1,8744,5,2,1,1,8),_FirmwareUpdateStatus_Type())
firmwareUpdateStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:firmwareUpdateStatus.setStatus(_B)
_ConfigurationUpdate_ObjectIdentity=ObjectIdentity
configurationUpdate=_ConfigurationUpdate_ObjectIdentity((1,3,6,1,4,1,8744,5,2,1,2))
_ConfigurationPeriodicUpdate_Type=TruthValue
_ConfigurationPeriodicUpdate_Object=MibScalar
configurationPeriodicUpdate=_ConfigurationPeriodicUpdate_Object((1,3,6,1,4,1,8744,5,2,1,2,1),_ConfigurationPeriodicUpdate_Type())
configurationPeriodicUpdate.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationPeriodicUpdate.setStatus(_B)
class _ConfigurationUpdateDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8)))
_ConfigurationUpdateDay_Type.__name__=_D
_ConfigurationUpdateDay_Object=MibScalar
configurationUpdateDay=_ConfigurationUpdateDay_Object((1,3,6,1,4,1,8744,5,2,1,2,2),_ConfigurationUpdateDay_Type())
configurationUpdateDay.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationUpdateDay.setStatus(_B)
class _ConfigurationUpdateTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_ConfigurationUpdateTime_Type.__name__=_J
_ConfigurationUpdateTime_Object=MibScalar
configurationUpdateTime=_ConfigurationUpdateTime_Object((1,3,6,1,4,1,8744,5,2,1,2,3),_ConfigurationUpdateTime_Type())
configurationUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationUpdateTime.setStatus(_B)
_ConfigurationUpdateLocation_Type=DisplayString
_ConfigurationUpdateLocation_Object=MibScalar
configurationUpdateLocation=_ConfigurationUpdateLocation_Object((1,3,6,1,4,1,8744,5,2,1,2,4),_ConfigurationUpdateLocation_Type())
configurationUpdateLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationUpdateLocation.setStatus(_B)
class _ConfigurationUpdateInitiate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_W,1)))
_ConfigurationUpdateInitiate_Type.__name__=_D
_ConfigurationUpdateInitiate_Object=MibScalar
configurationUpdateInitiate=_ConfigurationUpdateInitiate_Object((1,3,6,1,4,1,8744,5,2,1,2,5),_ConfigurationUpdateInitiate_Type())
configurationUpdateInitiate.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationUpdateInitiate.setStatus(_B)
class _ConfigurationUpdateOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('backup',1),('restore',2)))
_ConfigurationUpdateOperation_Type.__name__=_D
_ConfigurationUpdateOperation_Object=MibScalar
configurationUpdateOperation=_ConfigurationUpdateOperation_Object((1,3,6,1,4,1,8744,5,2,1,2,6),_ConfigurationUpdateOperation_Type())
configurationUpdateOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationUpdateOperation.setStatus(_B)
class _ConfigurationUpdateNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=1
_ConfigurationUpdateNotificationEnabled_Type.__name__=_E
_ConfigurationUpdateNotificationEnabled_Object=MibScalar
configurationUpdateNotificationEnabled=_ConfigurationUpdateNotificationEnabled_Object((1,3,6,1,4,1,8744,5,2,1,2,7),_ConfigurationUpdateNotificationEnabled_Type())
configurationUpdateNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationUpdateNotificationEnabled.setStatus(_B)
class _ConfigurationLocalUpdateNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=1
_ConfigurationLocalUpdateNotificationEnabled_Type.__name__=_E
_ConfigurationLocalUpdateNotificationEnabled_Object=MibScalar
configurationLocalUpdateNotificationEnabled=_ConfigurationLocalUpdateNotificationEnabled_Object((1,3,6,1,4,1,8744,5,2,1,2,8),_ConfigurationLocalUpdateNotificationEnabled_Type())
configurationLocalUpdateNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationLocalUpdateNotificationEnabled.setStatus(_B)
_ConfigurationUpdateInfo_Type=DisplayString
_ConfigurationUpdateInfo_Object=MibScalar
configurationUpdateInfo=_ConfigurationUpdateInfo_Object((1,3,6,1,4,1,8744,5,2,1,2,9),_ConfigurationUpdateInfo_Type())
configurationUpdateInfo.setMaxAccess(_G)
if mibBuilder.loadTexts:configurationUpdateInfo.setStatus(_B)
class _ConfigurationFactoryDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),('resetToFactoryDefaults',1)))
_ConfigurationFactoryDefaults_Type.__name__=_D
_ConfigurationFactoryDefaults_Object=MibScalar
configurationFactoryDefaults=_ConfigurationFactoryDefaults_Object((1,3,6,1,4,1,8744,5,2,1,2,10),_ConfigurationFactoryDefaults_Type())
configurationFactoryDefaults.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationFactoryDefaults.setStatus(_B)
class _ConfigurationRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),('restart',1)))
_ConfigurationRestart_Type.__name__=_D
_ConfigurationRestart_Object=MibScalar
configurationRestart=_ConfigurationRestart_Object((1,3,6,1,4,1,8744,5,2,1,2,11),_ConfigurationRestart_Type())
configurationRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationRestart.setStatus(_B)
class _ConfigurationUpdateStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_X,2),(_Y,3),(_Z,4)))
_ConfigurationUpdateStatus_Type.__name__=_D
_ConfigurationUpdateStatus_Object=MibScalar
configurationUpdateStatus=_ConfigurationUpdateStatus_Object((1,3,6,1,4,1,8744,5,2,1,2,12),_ConfigurationUpdateStatus_Type())
configurationUpdateStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:configurationUpdateStatus.setStatus(_B)
_Certificate_ObjectIdentity=ObjectIdentity
certificate=_Certificate_ObjectIdentity((1,3,6,1,4,1,8744,5,2,1,3))
class _CertificateAboutToExpireNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=1
_CertificateAboutToExpireNotificationEnabled_Type.__name__=_E
_CertificateAboutToExpireNotificationEnabled_Object=MibScalar
certificateAboutToExpireNotificationEnabled=_CertificateAboutToExpireNotificationEnabled_Object((1,3,6,1,4,1,8744,5,2,1,3,1),_CertificateAboutToExpireNotificationEnabled_Type())
certificateAboutToExpireNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:certificateAboutToExpireNotificationEnabled.setStatus(_B)
class _CertificateExpiredNotificationEnabled_Type(ColubrisNotificationEnable):defaultValue=1
_CertificateExpiredNotificationEnabled_Type.__name__=_E
_CertificateExpiredNotificationEnabled_Object=MibScalar
certificateExpiredNotificationEnabled=_CertificateExpiredNotificationEnabled_Object((1,3,6,1,4,1,8744,5,2,1,3,2),_CertificateExpiredNotificationEnabled_Type())
certificateExpiredNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:certificateExpiredNotificationEnabled.setStatus(_B)
_CertificateExpiryDate_Type=DisplayString
_CertificateExpiryDate_Object=MibScalar
certificateExpiryDate=_CertificateExpiryDate_Object((1,3,6,1,4,1,8744,5,2,1,3,3),_CertificateExpiryDate_Type())
certificateExpiryDate.setMaxAccess(_G)
if mibBuilder.loadTexts:certificateExpiryDate.setStatus(_B)
_ColubrisMaintenanceMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
colubrisMaintenanceMIBNotificationPrefix=_ColubrisMaintenanceMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,8744,5,2,2))
_ColubrisMaintenanceMIBNotifications_ObjectIdentity=ObjectIdentity
colubrisMaintenanceMIBNotifications=_ColubrisMaintenanceMIBNotifications_ObjectIdentity((1,3,6,1,4,1,8744,5,2,2,0))
_ColubrisMaintenanceMIBConformance_ObjectIdentity=ObjectIdentity
colubrisMaintenanceMIBConformance=_ColubrisMaintenanceMIBConformance_ObjectIdentity((1,3,6,1,4,1,8744,5,2,3))
_ColubrisMaintenanceMIBCompliances_ObjectIdentity=ObjectIdentity
colubrisMaintenanceMIBCompliances=_ColubrisMaintenanceMIBCompliances_ObjectIdentity((1,3,6,1,4,1,8744,5,2,3,1))
_ColubrisMaintenanceMIBGroups_ObjectIdentity=ObjectIdentity
colubrisMaintenanceMIBGroups=_ColubrisMaintenanceMIBGroups_ObjectIdentity((1,3,6,1,4,1,8744,5,2,3,2))
colubrisMaintenanceMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,2,3,2,1))
colubrisMaintenanceMIBGroup.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_L),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_H),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_I)))
if mibBuilder.loadTexts:colubrisMaintenanceMIBGroup.setStatus(_B)
configurationUpdateNotification=NotificationType((1,3,6,1,4,1,8744,5,2,2,0,1))
configurationUpdateNotification.setObjects(*((_A,_H),(_K,_M)))
if mibBuilder.loadTexts:configurationUpdateNotification.setStatus(_B)
configurationLocalUpdateNotification=NotificationType((1,3,6,1,4,1,8744,5,2,2,0,2))
configurationLocalUpdateNotification.setObjects((_A,_H))
if mibBuilder.loadTexts:configurationLocalUpdateNotification.setStatus(_B)
certificateAboutToExpireNotification=NotificationType((1,3,6,1,4,1,8744,5,2,2,0,3))
certificateAboutToExpireNotification.setObjects((_A,_I))
if mibBuilder.loadTexts:certificateAboutToExpireNotification.setStatus(_B)
certificateExpiredNotification=NotificationType((1,3,6,1,4,1,8744,5,2,2,0,4))
certificateExpiredNotification.setObjects((_A,_I))
if mibBuilder.loadTexts:certificateExpiredNotification.setStatus(_B)
firmwareUpdateNotification=NotificationType((1,3,6,1,4,1,8744,5,2,2,0,5))
firmwareUpdateNotification.setObjects(*((_A,_L),(_K,_N)))
if mibBuilder.loadTexts:firmwareUpdateNotification.setStatus(_B)
colubrisMaintenanceNotificationGroup=NotificationGroup((1,3,6,1,4,1,8744,5,2,3,2,2))
colubrisMaintenanceNotificationGroup.setObjects(*((_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:colubrisMaintenanceNotificationGroup.setStatus(_B)
colubrisMaintenanceMIBCompliance=ModuleCompliance((1,3,6,1,4,1,8744,5,2,3,1,1))
colubrisMaintenanceMIBCompliance.setObjects(*((_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:colubrisMaintenanceMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'colubrisMaintenanceMIB':colubrisMaintenanceMIB,'colubrisMaintenanceMIBObjects':colubrisMaintenanceMIBObjects,'firmwareUpdate':firmwareUpdate,_a:firmwarePeriodicUpdate,_b:firmwareUpdateDay,_c:firmwareUpdateTime,_d:firmwareUpdateLocation,_e:firmwareUpdateInitiate,_f:firmwareUpdateNotificationEnabled,_L:firmwareUpdateInfo,_g:firmwareUpdateStatus,'configurationUpdate':configurationUpdate,_h:configurationPeriodicUpdate,_i:configurationUpdateDay,_j:configurationUpdateTime,_k:configurationUpdateLocation,_l:configurationUpdateInitiate,_m:configurationUpdateOperation,_n:configurationUpdateNotificationEnabled,_q:configurationLocalUpdateNotificationEnabled,_H:configurationUpdateInfo,_o:configurationFactoryDefaults,_p:configurationRestart,_r:configurationUpdateStatus,'certificate':certificate,_s:certificateAboutToExpireNotificationEnabled,_t:certificateExpiredNotificationEnabled,_I:certificateExpiryDate,'colubrisMaintenanceMIBNotificationPrefix':colubrisMaintenanceMIBNotificationPrefix,'colubrisMaintenanceMIBNotifications':colubrisMaintenanceMIBNotifications,_v:configurationUpdateNotification,_w:configurationLocalUpdateNotification,_x:certificateAboutToExpireNotification,_y:certificateExpiredNotification,_u:firmwareUpdateNotification,'colubrisMaintenanceMIBConformance':colubrisMaintenanceMIBConformance,'colubrisMaintenanceMIBCompliances':colubrisMaintenanceMIBCompliances,'colubrisMaintenanceMIBCompliance':colubrisMaintenanceMIBCompliance,'colubrisMaintenanceMIBGroups':colubrisMaintenanceMIBGroups,_z:colubrisMaintenanceMIBGroup,_A0:colubrisMaintenanceNotificationGroup})