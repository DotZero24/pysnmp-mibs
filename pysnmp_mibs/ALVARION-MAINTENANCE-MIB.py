_v='alvarionMaintenanceNotificationGroup'
_u='alvarionMaintenanceMIBGroup'
_t='certificateExpiredNotification'
_s='certificateAboutToExpireNotification'
_r='configurationLocalUpdateNotification'
_q='configurationUpdateNotification'
_p='firmwareUpdateNotification'
_o='certificateExpiredNotificationEnabled'
_n='certificateAboutToExpireNotificationEnabled'
_m='configurationLocalUpdateNotificationEnabled'
_l='configurationRestart'
_k='configurationFactoryDefaults'
_j='configurationUpdateNotificationEnabled'
_i='configurationUpdateOperation'
_h='configurationUpdateInitiate'
_g='configurationUpdateLocation'
_f='configurationUpdateTime'
_e='configurationUpdateDay'
_d='configurationPeriodicUpdate'
_c='firmwareUpdateNotificationEnabled'
_b='firmwareUpdateInitiate'
_a='firmwareUpdateLocation'
_Z='firmwareUpdateTime'
_Y='firmwareUpdateDay'
_X='firmwarePeriodicUpdate'
_W='accessible-for-notify'
_V='update'
_U='everyday'
_T='sunday'
_S='saturday'
_R='friday'
_Q='thursday'
_P='wednesday'
_O='tuesday'
_N='monday'
_M='systemFirmwareRevision'
_L='systemConfigurationVersion'
_K='firmwareUpdateInfo'
_J='ALVARION-SYSTEM-MIB'
_I='OctetString'
_H='certificateExpiryDate'
_G='configurationUpdateInfo'
_F='idle'
_E='AlvarionNotificationEnable'
_D='Integer32'
_C='read-write'
_B='current'
_A='ALVARION-MAINTENANCE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alvarionMgmtV2,=mibBuilder.importSymbols('ALVARION-SMI','alvarionMgmtV2')
systemConfigurationVersion,systemFirmwareRevision=mibBuilder.importSymbols(_J,_L,_M)
AlvarionNotificationEnable,=mibBuilder.importSymbols('ALVARION-TC',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
alvarionMaintenanceMIB=ModuleIdentity((1,3,6,1,4,1,12394,1,10,5,2))
_AlvarionMaintenanceMIBObjects_ObjectIdentity=ObjectIdentity
alvarionMaintenanceMIBObjects=_AlvarionMaintenanceMIBObjects_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,2,1))
_FirmwareUpdate_ObjectIdentity=ObjectIdentity
firmwareUpdate=_FirmwareUpdate_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,2,1,1))
_FirmwarePeriodicUpdate_Type=TruthValue
_FirmwarePeriodicUpdate_Object=MibScalar
firmwarePeriodicUpdate=_FirmwarePeriodicUpdate_Object((1,3,6,1,4,1,12394,1,10,5,2,1,1,1),_FirmwarePeriodicUpdate_Type())
firmwarePeriodicUpdate.setMaxAccess(_C)
if mibBuilder.loadTexts:firmwarePeriodicUpdate.setStatus(_B)
class _FirmwareUpdateDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6),(_T,7),(_U,8)))
_FirmwareUpdateDay_Type.__name__=_D
_FirmwareUpdateDay_Object=MibScalar
firmwareUpdateDay=_FirmwareUpdateDay_Object((1,3,6,1,4,1,12394,1,10,5,2,1,1,2),_FirmwareUpdateDay_Type())
firmwareUpdateDay.setMaxAccess(_C)
if mibBuilder.loadTexts:firmwareUpdateDay.setStatus(_B)
class _FirmwareUpdateTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_FirmwareUpdateTime_Type.__name__=_I
_FirmwareUpdateTime_Object=MibScalar
firmwareUpdateTime=_FirmwareUpdateTime_Object((1,3,6,1,4,1,12394,1,10,5,2,1,1,3),_FirmwareUpdateTime_Type())
firmwareUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:firmwareUpdateTime.setStatus(_B)
_FirmwareUpdateLocation_Type=DisplayString
_FirmwareUpdateLocation_Object=MibScalar
firmwareUpdateLocation=_FirmwareUpdateLocation_Object((1,3,6,1,4,1,12394,1,10,5,2,1,1,4),_FirmwareUpdateLocation_Type())
firmwareUpdateLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:firmwareUpdateLocation.setStatus(_B)
class _FirmwareUpdateInitiate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_V,1)))
_FirmwareUpdateInitiate_Type.__name__=_D
_FirmwareUpdateInitiate_Object=MibScalar
firmwareUpdateInitiate=_FirmwareUpdateInitiate_Object((1,3,6,1,4,1,12394,1,10,5,2,1,1,5),_FirmwareUpdateInitiate_Type())
firmwareUpdateInitiate.setMaxAccess(_C)
if mibBuilder.loadTexts:firmwareUpdateInitiate.setStatus(_B)
class _FirmwareUpdateNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=1
_FirmwareUpdateNotificationEnabled_Type.__name__=_E
_FirmwareUpdateNotificationEnabled_Object=MibScalar
firmwareUpdateNotificationEnabled=_FirmwareUpdateNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,2,1,1,6),_FirmwareUpdateNotificationEnabled_Type())
firmwareUpdateNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:firmwareUpdateNotificationEnabled.setStatus(_B)
_FirmwareUpdateInfo_Type=DisplayString
_FirmwareUpdateInfo_Object=MibScalar
firmwareUpdateInfo=_FirmwareUpdateInfo_Object((1,3,6,1,4,1,12394,1,10,5,2,1,1,7),_FirmwareUpdateInfo_Type())
firmwareUpdateInfo.setMaxAccess(_W)
if mibBuilder.loadTexts:firmwareUpdateInfo.setStatus(_B)
_ConfigurationUpdate_ObjectIdentity=ObjectIdentity
configurationUpdate=_ConfigurationUpdate_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,2,1,2))
_ConfigurationPeriodicUpdate_Type=TruthValue
_ConfigurationPeriodicUpdate_Object=MibScalar
configurationPeriodicUpdate=_ConfigurationPeriodicUpdate_Object((1,3,6,1,4,1,12394,1,10,5,2,1,2,1),_ConfigurationPeriodicUpdate_Type())
configurationPeriodicUpdate.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationPeriodicUpdate.setStatus(_B)
class _ConfigurationUpdateDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6),(_T,7),(_U,8)))
_ConfigurationUpdateDay_Type.__name__=_D
_ConfigurationUpdateDay_Object=MibScalar
configurationUpdateDay=_ConfigurationUpdateDay_Object((1,3,6,1,4,1,12394,1,10,5,2,1,2,2),_ConfigurationUpdateDay_Type())
configurationUpdateDay.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationUpdateDay.setStatus(_B)
class _ConfigurationUpdateTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_ConfigurationUpdateTime_Type.__name__=_I
_ConfigurationUpdateTime_Object=MibScalar
configurationUpdateTime=_ConfigurationUpdateTime_Object((1,3,6,1,4,1,12394,1,10,5,2,1,2,3),_ConfigurationUpdateTime_Type())
configurationUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationUpdateTime.setStatus(_B)
_ConfigurationUpdateLocation_Type=DisplayString
_ConfigurationUpdateLocation_Object=MibScalar
configurationUpdateLocation=_ConfigurationUpdateLocation_Object((1,3,6,1,4,1,12394,1,10,5,2,1,2,4),_ConfigurationUpdateLocation_Type())
configurationUpdateLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationUpdateLocation.setStatus(_B)
class _ConfigurationUpdateInitiate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_V,1)))
_ConfigurationUpdateInitiate_Type.__name__=_D
_ConfigurationUpdateInitiate_Object=MibScalar
configurationUpdateInitiate=_ConfigurationUpdateInitiate_Object((1,3,6,1,4,1,12394,1,10,5,2,1,2,5),_ConfigurationUpdateInitiate_Type())
configurationUpdateInitiate.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationUpdateInitiate.setStatus(_B)
class _ConfigurationUpdateOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('backup',1),('restore',2)))
_ConfigurationUpdateOperation_Type.__name__=_D
_ConfigurationUpdateOperation_Object=MibScalar
configurationUpdateOperation=_ConfigurationUpdateOperation_Object((1,3,6,1,4,1,12394,1,10,5,2,1,2,6),_ConfigurationUpdateOperation_Type())
configurationUpdateOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationUpdateOperation.setStatus(_B)
class _ConfigurationUpdateNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=1
_ConfigurationUpdateNotificationEnabled_Type.__name__=_E
_ConfigurationUpdateNotificationEnabled_Object=MibScalar
configurationUpdateNotificationEnabled=_ConfigurationUpdateNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,2,1,2,7),_ConfigurationUpdateNotificationEnabled_Type())
configurationUpdateNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationUpdateNotificationEnabled.setStatus(_B)
class _ConfigurationLocalUpdateNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=1
_ConfigurationLocalUpdateNotificationEnabled_Type.__name__=_E
_ConfigurationLocalUpdateNotificationEnabled_Object=MibScalar
configurationLocalUpdateNotificationEnabled=_ConfigurationLocalUpdateNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,2,1,2,8),_ConfigurationLocalUpdateNotificationEnabled_Type())
configurationLocalUpdateNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationLocalUpdateNotificationEnabled.setStatus(_B)
_ConfigurationUpdateInfo_Type=DisplayString
_ConfigurationUpdateInfo_Object=MibScalar
configurationUpdateInfo=_ConfigurationUpdateInfo_Object((1,3,6,1,4,1,12394,1,10,5,2,1,2,9),_ConfigurationUpdateInfo_Type())
configurationUpdateInfo.setMaxAccess(_W)
if mibBuilder.loadTexts:configurationUpdateInfo.setStatus(_B)
class _ConfigurationFactoryDefaults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),('resetToFactoryDefaults',1)))
_ConfigurationFactoryDefaults_Type.__name__=_D
_ConfigurationFactoryDefaults_Object=MibScalar
configurationFactoryDefaults=_ConfigurationFactoryDefaults_Object((1,3,6,1,4,1,12394,1,10,5,2,1,2,10),_ConfigurationFactoryDefaults_Type())
configurationFactoryDefaults.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationFactoryDefaults.setStatus(_B)
class _ConfigurationRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),('restart',1)))
_ConfigurationRestart_Type.__name__=_D
_ConfigurationRestart_Object=MibScalar
configurationRestart=_ConfigurationRestart_Object((1,3,6,1,4,1,12394,1,10,5,2,1,2,11),_ConfigurationRestart_Type())
configurationRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationRestart.setStatus(_B)
_Certificate_ObjectIdentity=ObjectIdentity
certificate=_Certificate_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,2,1,3))
class _CertificateAboutToExpireNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=1
_CertificateAboutToExpireNotificationEnabled_Type.__name__=_E
_CertificateAboutToExpireNotificationEnabled_Object=MibScalar
certificateAboutToExpireNotificationEnabled=_CertificateAboutToExpireNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,2,1,3,1),_CertificateAboutToExpireNotificationEnabled_Type())
certificateAboutToExpireNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:certificateAboutToExpireNotificationEnabled.setStatus(_B)
class _CertificateExpiredNotificationEnabled_Type(AlvarionNotificationEnable):defaultValue=1
_CertificateExpiredNotificationEnabled_Type.__name__=_E
_CertificateExpiredNotificationEnabled_Object=MibScalar
certificateExpiredNotificationEnabled=_CertificateExpiredNotificationEnabled_Object((1,3,6,1,4,1,12394,1,10,5,2,1,3,2),_CertificateExpiredNotificationEnabled_Type())
certificateExpiredNotificationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:certificateExpiredNotificationEnabled.setStatus(_B)
_CertificateExpiryDate_Type=DisplayString
_CertificateExpiryDate_Object=MibScalar
certificateExpiryDate=_CertificateExpiryDate_Object((1,3,6,1,4,1,12394,1,10,5,2,1,3,3),_CertificateExpiryDate_Type())
certificateExpiryDate.setMaxAccess('read-only')
if mibBuilder.loadTexts:certificateExpiryDate.setStatus(_B)
_AlvarionMaintenanceMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
alvarionMaintenanceMIBNotificationPrefix=_AlvarionMaintenanceMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,2,2))
_AlvarionMaintenanceMIBNotifications_ObjectIdentity=ObjectIdentity
alvarionMaintenanceMIBNotifications=_AlvarionMaintenanceMIBNotifications_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,2,2,0))
_AlvarionMaintenanceMIBConformance_ObjectIdentity=ObjectIdentity
alvarionMaintenanceMIBConformance=_AlvarionMaintenanceMIBConformance_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,2,3))
_AlvarionMaintenanceMIBCompliances_ObjectIdentity=ObjectIdentity
alvarionMaintenanceMIBCompliances=_AlvarionMaintenanceMIBCompliances_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,2,3,1))
_AlvarionMaintenanceMIBGroups_ObjectIdentity=ObjectIdentity
alvarionMaintenanceMIBGroups=_AlvarionMaintenanceMIBGroups_ObjectIdentity((1,3,6,1,4,1,12394,1,10,5,2,3,2))
alvarionMaintenanceMIBGroup=ObjectGroup((1,3,6,1,4,1,12394,1,10,5,2,3,2,1))
alvarionMaintenanceMIBGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_K),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_G),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_H)))
if mibBuilder.loadTexts:alvarionMaintenanceMIBGroup.setStatus(_B)
configurationUpdateNotification=NotificationType((1,3,6,1,4,1,12394,1,10,5,2,2,0,1))
configurationUpdateNotification.setObjects(*((_A,_G),(_J,_L)))
if mibBuilder.loadTexts:configurationUpdateNotification.setStatus(_B)
configurationLocalUpdateNotification=NotificationType((1,3,6,1,4,1,12394,1,10,5,2,2,0,2))
configurationLocalUpdateNotification.setObjects((_A,_G))
if mibBuilder.loadTexts:configurationLocalUpdateNotification.setStatus(_B)
certificateAboutToExpireNotification=NotificationType((1,3,6,1,4,1,12394,1,10,5,2,2,0,3))
certificateAboutToExpireNotification.setObjects((_A,_H))
if mibBuilder.loadTexts:certificateAboutToExpireNotification.setStatus(_B)
certificateExpiredNotification=NotificationType((1,3,6,1,4,1,12394,1,10,5,2,2,0,4))
certificateExpiredNotification.setObjects((_A,_H))
if mibBuilder.loadTexts:certificateExpiredNotification.setStatus(_B)
firmwareUpdateNotification=NotificationType((1,3,6,1,4,1,12394,1,10,5,2,2,0,5))
firmwareUpdateNotification.setObjects(*((_A,_K),(_J,_M)))
if mibBuilder.loadTexts:firmwareUpdateNotification.setStatus(_B)
alvarionMaintenanceNotificationGroup=NotificationGroup((1,3,6,1,4,1,12394,1,10,5,2,3,2,2))
alvarionMaintenanceNotificationGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:alvarionMaintenanceNotificationGroup.setStatus(_B)
alvarionMaintenanceMIBCompliance=ModuleCompliance((1,3,6,1,4,1,12394,1,10,5,2,3,1,1))
alvarionMaintenanceMIBCompliance.setObjects(*((_A,_u),(_A,_v)))
if mibBuilder.loadTexts:alvarionMaintenanceMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'alvarionMaintenanceMIB':alvarionMaintenanceMIB,'alvarionMaintenanceMIBObjects':alvarionMaintenanceMIBObjects,'firmwareUpdate':firmwareUpdate,_X:firmwarePeriodicUpdate,_Y:firmwareUpdateDay,_Z:firmwareUpdateTime,_a:firmwareUpdateLocation,_b:firmwareUpdateInitiate,_c:firmwareUpdateNotificationEnabled,_K:firmwareUpdateInfo,'configurationUpdate':configurationUpdate,_d:configurationPeriodicUpdate,_e:configurationUpdateDay,_f:configurationUpdateTime,_g:configurationUpdateLocation,_h:configurationUpdateInitiate,_i:configurationUpdateOperation,_j:configurationUpdateNotificationEnabled,_m:configurationLocalUpdateNotificationEnabled,_G:configurationUpdateInfo,_k:configurationFactoryDefaults,_l:configurationRestart,'certificate':certificate,_n:certificateAboutToExpireNotificationEnabled,_o:certificateExpiredNotificationEnabled,_H:certificateExpiryDate,'alvarionMaintenanceMIBNotificationPrefix':alvarionMaintenanceMIBNotificationPrefix,'alvarionMaintenanceMIBNotifications':alvarionMaintenanceMIBNotifications,_q:configurationUpdateNotification,_r:configurationLocalUpdateNotification,_s:certificateAboutToExpireNotification,_t:certificateExpiredNotification,_p:firmwareUpdateNotification,'alvarionMaintenanceMIBConformance':alvarionMaintenanceMIBConformance,'alvarionMaintenanceMIBCompliances':alvarionMaintenanceMIBCompliances,'alvarionMaintenanceMIBCompliance':alvarionMaintenanceMIBCompliance,'alvarionMaintenanceMIBGroups':alvarionMaintenanceMIBGroups,_u:alvarionMaintenanceMIBGroup,_v:alvarionMaintenanceNotificationGroup})