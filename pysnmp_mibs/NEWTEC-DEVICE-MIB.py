_AS='ntcDevConfGrpV1Standard'
_AR='ntcDevRestEnable'
_AQ='ntcDevActCfgState'
_AP='ntcDevAutoSave'
_AO='ntcDevIdLatitude'
_AN='ntcDevIdLongitude'
_AM='ntcDevCarrId'
_AL='ntcDevTelephoneext'
_AK='ntcDevTelephonenbr'
_AJ='ntcDevReset'
_AI='ntcDevAlmLicenseUpgradeFailure'
_AH='ntcDevAlmInternalError'
_AG='ntcDevAlmHardwareFailure'
_AF='ntcDevAlmHardwareInventory'
_AE='ntcDevAlmLicenseExpireFile'
_AD='ntcDevAlmNtpNoPeerFailure'
_AC='ntcDevAlmUpgradeFailure'
_AB='ntcDevAlmFrontPanelFailure'
_AA='ntcDevAlmInvalidLicenseFile'
_A9='ntcDevAlmTemperature'
_A8='ntcDevAlmGenInterfaceAlarm'
_A7='ntcDevAlmGenBootConfigFailure'
_A6='ntcDevAlmGenDeviceAlarm'
_A5='ntcDevMonGlobalCpuLoad'
_A4='ntcDevMonInternalErrorCause'
_A3='ntcDevMonHwFailureCause'
_A2='ntcDevMonSensorsValue'
_A1='ntcDevMonUptime'
_A0='ntcDevMonMemoryUse'
_z='ntcDevMonCpuLoad'
_y='ntcDevMonPowerSupply'
_x='ntcDevMonTemperature'
_w='ntcDevDtNtpPeerIpAddress'
_v='ntcDevDtNtpEnable'
_u='ntcDevDtTime'
_t='ntcDevDtDate'
_s='ntcDevLogFilterLevel'
_r='ntcDevLogRemUdpPort'
_q='ntcDevLogRemIpAddress'
_p='ntcDevLogRemEnable'
_o='ntcDevLogLocEnable'
_n='ntcDevFtpAnonymousEnable'
_m='ntcDevFtpEnable'
_l='ntcDevGuiEnable'
_k='ntcDevCliInactivityTimeout'
_j='ntcDevCliRemoteEnable'
_i='ntcDevSnmpNotifDestCommunity'
_h='ntcDevSnmpNotifDestType'
_g='ntcDevSnmpNotifDestIpAddress'
_f='ntcDevFpiAccessLevel'
_e='ntcDevFpEnable'
_d='ntcDevIdLicenseTimeRemain'
_c='ntcDevIdLicenseType'
_b='ntcDevIdDeviceOptionsDescription'
_a='ntcDevIdSoftwareVersion'
_Z='ntcDevIdSoftwareId'
_Y='ntcDevIdHardwareRevision'
_X='ntcDevIdTypeId'
_W='ntcDevIdDeviceDescription'
_V='ntcDevIdProduct'
_U='ntcDevIdUniqueId'
_T='ntcDevIdSerialNumber'
_S='ntcDevIdLabel'
_R='ntcDevMonSensorsSensor'
_Q='ntcDevDtNtpPeerPeer'
_P='ntcDevLogFilterFacility'
_O='ntcDevSnmpNotifDestDestination'
_N='ntcDevIdDeviceOptionsSalesCode'
_M='OctetString'
_L='Float32TC'
_K='IpAddress'
_J='00000000'
_I='not-accessible'
_H='Unsigned32'
_G='Integer32'
_F='NtcEnable'
_E='DisplayString'
_D='read-write'
_C='read-only'
_B='NEWTEC-DEVICE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Float32TC,=mibBuilder.importSymbols('FLOAT-TC-MIB',_L)
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,NtcEnable=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,_K,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
ntcDevice=ModuleIdentity((1,3,6,1,4,1,5835,5,2,100))
if mibBuilder.loadTexts:ntcDevice.setRevisions(('2017-10-23 12:00','2017-07-10 12:00','2016-08-05 08:00','2016-05-17 09:00','2015-10-19 11:00','2015-09-25 11:00','2015-04-13 07:00','2014-09-09 09:00','2014-07-08 09:00','2014-03-18 12:00','2013-05-22 06:00','2013-01-08 12:00','2012-06-28 12:00'))
_NtcDevObjects_ObjectIdentity=ObjectIdentity
ntcDevObjects=_NtcDevObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,100,1))
if mibBuilder.loadTexts:ntcDevObjects.setStatus(_A)
_NtcDevIdentification_ObjectIdentity=ObjectIdentity
ntcDevIdentification=_NtcDevIdentification_ObjectIdentity((1,3,6,1,4,1,5835,5,2,100,1,1))
if mibBuilder.loadTexts:ntcDevIdentification.setStatus(_A)
class _NtcDevIdLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NtcDevIdLabel_Type.__name__=_E
_NtcDevIdLabel_Object=MibScalar
ntcDevIdLabel=_NtcDevIdLabel_Object((1,3,6,1,4,1,5835,5,2,100,1,1,1),_NtcDevIdLabel_Type())
ntcDevIdLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevIdLabel.setStatus(_A)
class _NtcDevIdSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NtcDevIdSerialNumber_Type.__name__=_E
_NtcDevIdSerialNumber_Object=MibScalar
ntcDevIdSerialNumber=_NtcDevIdSerialNumber_Object((1,3,6,1,4,1,5835,5,2,100,1,1,2),_NtcDevIdSerialNumber_Type())
ntcDevIdSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevIdSerialNumber.setStatus(_A)
class _NtcDevIdUniqueId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NtcDevIdUniqueId_Type.__name__=_E
_NtcDevIdUniqueId_Object=MibScalar
ntcDevIdUniqueId=_NtcDevIdUniqueId_Object((1,3,6,1,4,1,5835,5,2,100,1,1,3),_NtcDevIdUniqueId_Type())
ntcDevIdUniqueId.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevIdUniqueId.setStatus(_A)
class _NtcDevIdProduct_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NtcDevIdProduct_Type.__name__=_E
_NtcDevIdProduct_Object=MibScalar
ntcDevIdProduct=_NtcDevIdProduct_Object((1,3,6,1,4,1,5835,5,2,100,1,1,4),_NtcDevIdProduct_Type())
ntcDevIdProduct.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevIdProduct.setStatus(_A)
class _NtcDevIdDeviceDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NtcDevIdDeviceDescription_Type.__name__=_E
_NtcDevIdDeviceDescription_Object=MibScalar
ntcDevIdDeviceDescription=_NtcDevIdDeviceDescription_Object((1,3,6,1,4,1,5835,5,2,100,1,1,5),_NtcDevIdDeviceDescription_Type())
ntcDevIdDeviceDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevIdDeviceDescription.setStatus(_A)
class _NtcDevIdTypeId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NtcDevIdTypeId_Type.__name__=_E
_NtcDevIdTypeId_Object=MibScalar
ntcDevIdTypeId=_NtcDevIdTypeId_Object((1,3,6,1,4,1,5835,5,2,100,1,1,6),_NtcDevIdTypeId_Type())
ntcDevIdTypeId.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevIdTypeId.setStatus(_A)
class _NtcDevIdHardwareRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NtcDevIdHardwareRevision_Type.__name__=_E
_NtcDevIdHardwareRevision_Object=MibScalar
ntcDevIdHardwareRevision=_NtcDevIdHardwareRevision_Object((1,3,6,1,4,1,5835,5,2,100,1,1,7),_NtcDevIdHardwareRevision_Type())
ntcDevIdHardwareRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevIdHardwareRevision.setStatus(_A)
class _NtcDevIdSoftwareId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NtcDevIdSoftwareId_Type.__name__=_E
_NtcDevIdSoftwareId_Object=MibScalar
ntcDevIdSoftwareId=_NtcDevIdSoftwareId_Object((1,3,6,1,4,1,5835,5,2,100,1,1,8),_NtcDevIdSoftwareId_Type())
ntcDevIdSoftwareId.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevIdSoftwareId.setStatus(_A)
class _NtcDevIdSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NtcDevIdSoftwareVersion_Type.__name__=_E
_NtcDevIdSoftwareVersion_Object=MibScalar
ntcDevIdSoftwareVersion=_NtcDevIdSoftwareVersion_Object((1,3,6,1,4,1,5835,5,2,100,1,1,9),_NtcDevIdSoftwareVersion_Type())
ntcDevIdSoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevIdSoftwareVersion.setStatus(_A)
_NtcDevIdDeviceOptionsTable_Object=MibTable
ntcDevIdDeviceOptionsTable=_NtcDevIdDeviceOptionsTable_Object((1,3,6,1,4,1,5835,5,2,100,1,1,10))
if mibBuilder.loadTexts:ntcDevIdDeviceOptionsTable.setStatus(_A)
_NtcDevIdDeviceOptionsEntry_Object=MibTableRow
ntcDevIdDeviceOptionsEntry=_NtcDevIdDeviceOptionsEntry_Object((1,3,6,1,4,1,5835,5,2,100,1,1,10,1))
ntcDevIdDeviceOptionsEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:ntcDevIdDeviceOptionsEntry.setStatus(_A)
class _NtcDevIdDeviceOptionsSalesCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,66))
_NtcDevIdDeviceOptionsSalesCode_Type.__name__=_E
_NtcDevIdDeviceOptionsSalesCode_Object=MibTableColumn
ntcDevIdDeviceOptionsSalesCode=_NtcDevIdDeviceOptionsSalesCode_Object((1,3,6,1,4,1,5835,5,2,100,1,1,10,1,1),_NtcDevIdDeviceOptionsSalesCode_Type())
ntcDevIdDeviceOptionsSalesCode.setMaxAccess(_I)
if mibBuilder.loadTexts:ntcDevIdDeviceOptionsSalesCode.setStatus(_A)
class _NtcDevIdDeviceOptionsDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtcDevIdDeviceOptionsDescription_Type.__name__=_E
_NtcDevIdDeviceOptionsDescription_Object=MibTableColumn
ntcDevIdDeviceOptionsDescription=_NtcDevIdDeviceOptionsDescription_Object((1,3,6,1,4,1,5835,5,2,100,1,1,10,1,2),_NtcDevIdDeviceOptionsDescription_Type())
ntcDevIdDeviceOptionsDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevIdDeviceOptionsDescription.setStatus(_A)
class _NtcDevIdLicenseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('permanent',0),('temporaryEndDate',1),('temporaryCredits',2),('temporaryCreditsUnderRedundancy',3)))
_NtcDevIdLicenseType_Type.__name__=_G
_NtcDevIdLicenseType_Object=MibScalar
ntcDevIdLicenseType=_NtcDevIdLicenseType_Object((1,3,6,1,4,1,5835,5,2,100,1,1,11),_NtcDevIdLicenseType_Type())
ntcDevIdLicenseType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevIdLicenseType.setStatus(_A)
class _NtcDevIdLicenseTimeRemain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NtcDevIdLicenseTimeRemain_Type.__name__=_E
_NtcDevIdLicenseTimeRemain_Object=MibScalar
ntcDevIdLicenseTimeRemain=_NtcDevIdLicenseTimeRemain_Object((1,3,6,1,4,1,5835,5,2,100,1,1,12),_NtcDevIdLicenseTimeRemain_Type())
ntcDevIdLicenseTimeRemain.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevIdLicenseTimeRemain.setStatus(_A)
_NtcDevFrontPanel_ObjectIdentity=ObjectIdentity
ntcDevFrontPanel=_NtcDevFrontPanel_ObjectIdentity((1,3,6,1,4,1,5835,5,2,100,1,2))
if mibBuilder.loadTexts:ntcDevFrontPanel.setStatus(_A)
class _NtcDevFpEnable_Type(NtcEnable):defaultValue=1
_NtcDevFpEnable_Type.__name__=_F
_NtcDevFpEnable_Object=MibScalar
ntcDevFpEnable=_NtcDevFpEnable_Object((1,3,6,1,4,1,5835,5,2,100,1,2,1),_NtcDevFpEnable_Type())
ntcDevFpEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevFpEnable.setStatus(_A)
class _NtcDevFpiAccessLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('readonly',0),('operator',1),('expert',2)))
_NtcDevFpiAccessLevel_Type.__name__=_G
_NtcDevFpiAccessLevel_Object=MibScalar
ntcDevFpiAccessLevel=_NtcDevFpiAccessLevel_Object((1,3,6,1,4,1,5835,5,2,100,1,2,2),_NtcDevFpiAccessLevel_Type())
ntcDevFpiAccessLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevFpiAccessLevel.setStatus(_A)
_NtcDevSnmp_ObjectIdentity=ObjectIdentity
ntcDevSnmp=_NtcDevSnmp_ObjectIdentity((1,3,6,1,4,1,5835,5,2,100,1,3))
if mibBuilder.loadTexts:ntcDevSnmp.setStatus(_A)
_NtcDevSnmpNotification_ObjectIdentity=ObjectIdentity
ntcDevSnmpNotification=_NtcDevSnmpNotification_ObjectIdentity((1,3,6,1,4,1,5835,5,2,100,1,3,1))
if mibBuilder.loadTexts:ntcDevSnmpNotification.setStatus(_A)
_NtcDevSnmpNotifDestTable_Object=MibTable
ntcDevSnmpNotifDestTable=_NtcDevSnmpNotifDestTable_Object((1,3,6,1,4,1,5835,5,2,100,1,3,1,1))
if mibBuilder.loadTexts:ntcDevSnmpNotifDestTable.setStatus(_A)
_NtcDevSnmpNotifDestEntry_Object=MibTableRow
ntcDevSnmpNotifDestEntry=_NtcDevSnmpNotifDestEntry_Object((1,3,6,1,4,1,5835,5,2,100,1,3,1,1,1))
ntcDevSnmpNotifDestEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:ntcDevSnmpNotifDestEntry.setStatus(_A)
class _NtcDevSnmpNotifDestDestination_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_NtcDevSnmpNotifDestDestination_Type.__name__=_H
_NtcDevSnmpNotifDestDestination_Object=MibTableColumn
ntcDevSnmpNotifDestDestination=_NtcDevSnmpNotifDestDestination_Object((1,3,6,1,4,1,5835,5,2,100,1,3,1,1,1,1),_NtcDevSnmpNotifDestDestination_Type())
ntcDevSnmpNotifDestDestination.setMaxAccess(_I)
if mibBuilder.loadTexts:ntcDevSnmpNotifDestDestination.setStatus(_A)
class _NtcDevSnmpNotifDestIpAddress_Type(IpAddress):defaultHexValue=_J
_NtcDevSnmpNotifDestIpAddress_Type.__name__=_K
_NtcDevSnmpNotifDestIpAddress_Object=MibTableColumn
ntcDevSnmpNotifDestIpAddress=_NtcDevSnmpNotifDestIpAddress_Object((1,3,6,1,4,1,5835,5,2,100,1,3,1,1,1,2),_NtcDevSnmpNotifDestIpAddress_Type())
ntcDevSnmpNotifDestIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevSnmpNotifDestIpAddress.setStatus(_A)
class _NtcDevSnmpNotifDestType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('trapV1',0),('trapV2',1),('inform',2)))
_NtcDevSnmpNotifDestType_Type.__name__=_G
_NtcDevSnmpNotifDestType_Object=MibTableColumn
ntcDevSnmpNotifDestType=_NtcDevSnmpNotifDestType_Object((1,3,6,1,4,1,5835,5,2,100,1,3,1,1,1,3),_NtcDevSnmpNotifDestType_Type())
ntcDevSnmpNotifDestType.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevSnmpNotifDestType.setStatus(_A)
class _NtcDevSnmpNotifDestCommunity_Type(DisplayString):defaultValue=OctetString('trapcom');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_NtcDevSnmpNotifDestCommunity_Type.__name__=_E
_NtcDevSnmpNotifDestCommunity_Object=MibTableColumn
ntcDevSnmpNotifDestCommunity=_NtcDevSnmpNotifDestCommunity_Object((1,3,6,1,4,1,5835,5,2,100,1,3,1,1,1,4),_NtcDevSnmpNotifDestCommunity_Type())
ntcDevSnmpNotifDestCommunity.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevSnmpNotifDestCommunity.setStatus(_A)
_NtcDevCli_ObjectIdentity=ObjectIdentity
ntcDevCli=_NtcDevCli_ObjectIdentity((1,3,6,1,4,1,5835,5,2,100,1,4))
if mibBuilder.loadTexts:ntcDevCli.setStatus(_A)
class _NtcDevCliRemoteEnable_Type(NtcEnable):defaultValue=1
_NtcDevCliRemoteEnable_Type.__name__=_F
_NtcDevCliRemoteEnable_Object=MibScalar
ntcDevCliRemoteEnable=_NtcDevCliRemoteEnable_Object((1,3,6,1,4,1,5835,5,2,100,1,4,1),_NtcDevCliRemoteEnable_Type())
ntcDevCliRemoteEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevCliRemoteEnable.setStatus(_A)
class _NtcDevCliInactivityTimeout_Type(Unsigned32):defaultValue=600
_NtcDevCliInactivityTimeout_Type.__name__=_H
_NtcDevCliInactivityTimeout_Object=MibScalar
ntcDevCliInactivityTimeout=_NtcDevCliInactivityTimeout_Object((1,3,6,1,4,1,5835,5,2,100,1,4,2),_NtcDevCliInactivityTimeout_Type())
ntcDevCliInactivityTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevCliInactivityTimeout.setStatus(_A)
if mibBuilder.loadTexts:ntcDevCliInactivityTimeout.setUnits('s')
_NtcDevGui_ObjectIdentity=ObjectIdentity
ntcDevGui=_NtcDevGui_ObjectIdentity((1,3,6,1,4,1,5835,5,2,100,1,5))
if mibBuilder.loadTexts:ntcDevGui.setStatus(_A)
class _NtcDevGuiEnable_Type(NtcEnable):defaultValue=1
_NtcDevGuiEnable_Type.__name__=_F
_NtcDevGuiEnable_Object=MibScalar
ntcDevGuiEnable=_NtcDevGuiEnable_Object((1,3,6,1,4,1,5835,5,2,100,1,5,1),_NtcDevGuiEnable_Type())
ntcDevGuiEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevGuiEnable.setStatus(_A)
_NtcDevFtp_ObjectIdentity=ObjectIdentity
ntcDevFtp=_NtcDevFtp_ObjectIdentity((1,3,6,1,4,1,5835,5,2,100,1,6))
if mibBuilder.loadTexts:ntcDevFtp.setStatus(_A)
class _NtcDevFtpEnable_Type(NtcEnable):defaultValue=1
_NtcDevFtpEnable_Type.__name__=_F
_NtcDevFtpEnable_Object=MibScalar
ntcDevFtpEnable=_NtcDevFtpEnable_Object((1,3,6,1,4,1,5835,5,2,100,1,6,1),_NtcDevFtpEnable_Type())
ntcDevFtpEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevFtpEnable.setStatus(_A)
class _NtcDevFtpAnonymousEnable_Type(NtcEnable):defaultValue=1
_NtcDevFtpAnonymousEnable_Type.__name__=_F
_NtcDevFtpAnonymousEnable_Object=MibScalar
ntcDevFtpAnonymousEnable=_NtcDevFtpAnonymousEnable_Object((1,3,6,1,4,1,5835,5,2,100,1,6,2),_NtcDevFtpAnonymousEnable_Type())
ntcDevFtpAnonymousEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevFtpAnonymousEnable.setStatus(_A)
_NtcDevLog_ObjectIdentity=ObjectIdentity
ntcDevLog=_NtcDevLog_ObjectIdentity((1,3,6,1,4,1,5835,5,2,100,1,7))
if mibBuilder.loadTexts:ntcDevLog.setStatus(_A)
_NtcDevLogLocal_ObjectIdentity=ObjectIdentity
ntcDevLogLocal=_NtcDevLogLocal_ObjectIdentity((1,3,6,1,4,1,5835,5,2,100,1,7,1))
if mibBuilder.loadTexts:ntcDevLogLocal.setStatus(_A)
class _NtcDevLogLocEnable_Type(NtcEnable):defaultValue=1
_NtcDevLogLocEnable_Type.__name__=_F
_NtcDevLogLocEnable_Object=MibScalar
ntcDevLogLocEnable=_NtcDevLogLocEnable_Object((1,3,6,1,4,1,5835,5,2,100,1,7,1,1),_NtcDevLogLocEnable_Type())
ntcDevLogLocEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevLogLocEnable.setStatus(_A)
_NtcDevLogRemote_ObjectIdentity=ObjectIdentity
ntcDevLogRemote=_NtcDevLogRemote_ObjectIdentity((1,3,6,1,4,1,5835,5,2,100,1,7,2))
if mibBuilder.loadTexts:ntcDevLogRemote.setStatus(_A)
class _NtcDevLogRemEnable_Type(NtcEnable):defaultValue=0
_NtcDevLogRemEnable_Type.__name__=_F
_NtcDevLogRemEnable_Object=MibScalar
ntcDevLogRemEnable=_NtcDevLogRemEnable_Object((1,3,6,1,4,1,5835,5,2,100,1,7,2,1),_NtcDevLogRemEnable_Type())
ntcDevLogRemEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevLogRemEnable.setStatus(_A)
class _NtcDevLogRemIpAddress_Type(IpAddress):defaultHexValue=_J
_NtcDevLogRemIpAddress_Type.__name__=_K
_NtcDevLogRemIpAddress_Object=MibScalar
ntcDevLogRemIpAddress=_NtcDevLogRemIpAddress_Object((1,3,6,1,4,1,5835,5,2,100,1,7,2,2),_NtcDevLogRemIpAddress_Type())
ntcDevLogRemIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevLogRemIpAddress.setStatus(_A)
class _NtcDevLogRemUdpPort_Type(Unsigned32):defaultValue=514;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NtcDevLogRemUdpPort_Type.__name__=_H
_NtcDevLogRemUdpPort_Object=MibScalar
ntcDevLogRemUdpPort=_NtcDevLogRemUdpPort_Object((1,3,6,1,4,1,5835,5,2,100,1,7,2,3),_NtcDevLogRemUdpPort_Type())
ntcDevLogRemUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevLogRemUdpPort.setStatus(_A)
_NtcDevLogFilterTable_Object=MibTable
ntcDevLogFilterTable=_NtcDevLogFilterTable_Object((1,3,6,1,4,1,5835,5,2,100,1,7,3))
if mibBuilder.loadTexts:ntcDevLogFilterTable.setStatus(_A)
_NtcDevLogFilterEntry_Object=MibTableRow
ntcDevLogFilterEntry=_NtcDevLogFilterEntry_Object((1,3,6,1,4,1,5835,5,2,100,1,7,3,1))
ntcDevLogFilterEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:ntcDevLogFilterEntry.setStatus(_A)
class _NtcDevLogFilterFacility_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtcDevLogFilterFacility_Type.__name__=_E
_NtcDevLogFilterFacility_Object=MibTableColumn
ntcDevLogFilterFacility=_NtcDevLogFilterFacility_Object((1,3,6,1,4,1,5835,5,2,100,1,7,3,1,1),_NtcDevLogFilterFacility_Type())
ntcDevLogFilterFacility.setMaxAccess(_I)
if mibBuilder.loadTexts:ntcDevLogFilterFacility.setStatus(_A)
class _NtcDevLogFilterLevel_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('off',0),('trace',1),('debug',2),('info',3),('notice',4),('warn',5),('error',6),('alert',7),('emerg',8)))
_NtcDevLogFilterLevel_Type.__name__=_G
_NtcDevLogFilterLevel_Object=MibTableColumn
ntcDevLogFilterLevel=_NtcDevLogFilterLevel_Object((1,3,6,1,4,1,5835,5,2,100,1,7,3,1,2),_NtcDevLogFilterLevel_Type())
ntcDevLogFilterLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevLogFilterLevel.setStatus(_A)
_NtcDevDateTime_ObjectIdentity=ObjectIdentity
ntcDevDateTime=_NtcDevDateTime_ObjectIdentity((1,3,6,1,4,1,5835,5,2,100,1,8))
if mibBuilder.loadTexts:ntcDevDateTime.setStatus(_A)
class _NtcDevDtDate_Type(DisplayString):defaultValue=OctetString('01/01/2001');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_NtcDevDtDate_Type.__name__=_E
_NtcDevDtDate_Object=MibScalar
ntcDevDtDate=_NtcDevDtDate_Object((1,3,6,1,4,1,5835,5,2,100,1,8,1),_NtcDevDtDate_Type())
ntcDevDtDate.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevDtDate.setStatus(_A)
class _NtcDevDtTime_Type(DisplayString):defaultValue=OctetString('00:00:00');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_NtcDevDtTime_Type.__name__=_E
_NtcDevDtTime_Object=MibScalar
ntcDevDtTime=_NtcDevDtTime_Object((1,3,6,1,4,1,5835,5,2,100,1,8,2),_NtcDevDtTime_Type())
ntcDevDtTime.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevDtTime.setStatus(_A)
_NtcDevDtNtp_ObjectIdentity=ObjectIdentity
ntcDevDtNtp=_NtcDevDtNtp_ObjectIdentity((1,3,6,1,4,1,5835,5,2,100,1,8,3))
if mibBuilder.loadTexts:ntcDevDtNtp.setStatus(_A)
class _NtcDevDtNtpEnable_Type(NtcEnable):defaultValue=0
_NtcDevDtNtpEnable_Type.__name__=_F
_NtcDevDtNtpEnable_Object=MibScalar
ntcDevDtNtpEnable=_NtcDevDtNtpEnable_Object((1,3,6,1,4,1,5835,5,2,100,1,8,3,1),_NtcDevDtNtpEnable_Type())
ntcDevDtNtpEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevDtNtpEnable.setStatus(_A)
_NtcDevDtNtpPeerTable_Object=MibTable
ntcDevDtNtpPeerTable=_NtcDevDtNtpPeerTable_Object((1,3,6,1,4,1,5835,5,2,100,1,8,3,2))
if mibBuilder.loadTexts:ntcDevDtNtpPeerTable.setStatus(_A)
_NtcDevDtNtpPeerEntry_Object=MibTableRow
ntcDevDtNtpPeerEntry=_NtcDevDtNtpPeerEntry_Object((1,3,6,1,4,1,5835,5,2,100,1,8,3,2,1))
ntcDevDtNtpPeerEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:ntcDevDtNtpPeerEntry.setStatus(_A)
_NtcDevDtNtpPeerPeer_Type=Unsigned32
_NtcDevDtNtpPeerPeer_Object=MibTableColumn
ntcDevDtNtpPeerPeer=_NtcDevDtNtpPeerPeer_Object((1,3,6,1,4,1,5835,5,2,100,1,8,3,2,1,1),_NtcDevDtNtpPeerPeer_Type())
ntcDevDtNtpPeerPeer.setMaxAccess(_I)
if mibBuilder.loadTexts:ntcDevDtNtpPeerPeer.setStatus(_A)
class _NtcDevDtNtpPeerIpAddress_Type(IpAddress):defaultHexValue=_J
_NtcDevDtNtpPeerIpAddress_Type.__name__=_K
_NtcDevDtNtpPeerIpAddress_Object=MibTableColumn
ntcDevDtNtpPeerIpAddress=_NtcDevDtNtpPeerIpAddress_Object((1,3,6,1,4,1,5835,5,2,100,1,8,3,2,1,2),_NtcDevDtNtpPeerIpAddress_Type())
ntcDevDtNtpPeerIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevDtNtpPeerIpAddress.setStatus(_A)
_NtcDevMonitor_ObjectIdentity=ObjectIdentity
ntcDevMonitor=_NtcDevMonitor_ObjectIdentity((1,3,6,1,4,1,5835,5,2,100,1,9))
if mibBuilder.loadTexts:ntcDevMonitor.setStatus(_A)
_NtcDevMonTemperature_Type=Integer32
_NtcDevMonTemperature_Object=MibScalar
ntcDevMonTemperature=_NtcDevMonTemperature_Object((1,3,6,1,4,1,5835,5,2,100,1,9,1),_NtcDevMonTemperature_Type())
ntcDevMonTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevMonTemperature.setStatus(_A)
if mibBuilder.loadTexts:ntcDevMonTemperature.setUnits('Celsius')
_NtcDevMonPowerSupply_Type=Integer32
_NtcDevMonPowerSupply_Object=MibScalar
ntcDevMonPowerSupply=_NtcDevMonPowerSupply_Object((1,3,6,1,4,1,5835,5,2,100,1,9,2),_NtcDevMonPowerSupply_Type())
ntcDevMonPowerSupply.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevMonPowerSupply.setStatus(_A)
if mibBuilder.loadTexts:ntcDevMonPowerSupply.setUnits('V')
class _NtcDevMonCpuLoad_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1000))
_NtcDevMonCpuLoad_Type.__name__=_E
_NtcDevMonCpuLoad_Object=MibScalar
ntcDevMonCpuLoad=_NtcDevMonCpuLoad_Object((1,3,6,1,4,1,5835,5,2,100,1,9,3),_NtcDevMonCpuLoad_Type())
ntcDevMonCpuLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevMonCpuLoad.setStatus(_A)
class _NtcDevMonMemoryUse_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_NtcDevMonMemoryUse_Type.__name__=_H
_NtcDevMonMemoryUse_Object=MibScalar
ntcDevMonMemoryUse=_NtcDevMonMemoryUse_Object((1,3,6,1,4,1,5835,5,2,100,1,9,4),_NtcDevMonMemoryUse_Type())
ntcDevMonMemoryUse.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevMonMemoryUse.setStatus(_A)
if mibBuilder.loadTexts:ntcDevMonMemoryUse.setUnits('%')
class _NtcDevMonUptime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NtcDevMonUptime_Type.__name__=_E
_NtcDevMonUptime_Object=MibScalar
ntcDevMonUptime=_NtcDevMonUptime_Object((1,3,6,1,4,1,5835,5,2,100,1,9,5),_NtcDevMonUptime_Type())
ntcDevMonUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevMonUptime.setStatus(_A)
_NtcDevMonSensorsTable_Object=MibTable
ntcDevMonSensorsTable=_NtcDevMonSensorsTable_Object((1,3,6,1,4,1,5835,5,2,100,1,9,6))
if mibBuilder.loadTexts:ntcDevMonSensorsTable.setStatus(_A)
_NtcDevMonSensorsEntry_Object=MibTableRow
ntcDevMonSensorsEntry=_NtcDevMonSensorsEntry_Object((1,3,6,1,4,1,5835,5,2,100,1,9,6,1))
ntcDevMonSensorsEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:ntcDevMonSensorsEntry.setStatus(_A)
class _NtcDevMonSensorsSensor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtcDevMonSensorsSensor_Type.__name__=_E
_NtcDevMonSensorsSensor_Object=MibTableColumn
ntcDevMonSensorsSensor=_NtcDevMonSensorsSensor_Object((1,3,6,1,4,1,5835,5,2,100,1,9,6,1,1),_NtcDevMonSensorsSensor_Type())
ntcDevMonSensorsSensor.setMaxAccess(_I)
if mibBuilder.loadTexts:ntcDevMonSensorsSensor.setStatus(_A)
class _NtcDevMonSensorsValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtcDevMonSensorsValue_Type.__name__=_E
_NtcDevMonSensorsValue_Object=MibTableColumn
ntcDevMonSensorsValue=_NtcDevMonSensorsValue_Object((1,3,6,1,4,1,5835,5,2,100,1,9,6,1,2),_NtcDevMonSensorsValue_Type())
ntcDevMonSensorsValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevMonSensorsValue.setStatus(_A)
class _NtcDevMonHwFailureCause_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NtcDevMonHwFailureCause_Type.__name__=_E
_NtcDevMonHwFailureCause_Object=MibScalar
ntcDevMonHwFailureCause=_NtcDevMonHwFailureCause_Object((1,3,6,1,4,1,5835,5,2,100,1,9,7),_NtcDevMonHwFailureCause_Type())
ntcDevMonHwFailureCause.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevMonHwFailureCause.setStatus(_A)
class _NtcDevMonInternalErrorCause_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NtcDevMonInternalErrorCause_Type.__name__=_E
_NtcDevMonInternalErrorCause_Object=MibScalar
ntcDevMonInternalErrorCause=_NtcDevMonInternalErrorCause_Object((1,3,6,1,4,1,5835,5,2,100,1,9,8),_NtcDevMonInternalErrorCause_Type())
ntcDevMonInternalErrorCause.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevMonInternalErrorCause.setStatus(_A)
class _NtcDevMonGlobalCpuLoad_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1000))
_NtcDevMonGlobalCpuLoad_Type.__name__=_M
_NtcDevMonGlobalCpuLoad_Object=MibScalar
ntcDevMonGlobalCpuLoad=_NtcDevMonGlobalCpuLoad_Object((1,3,6,1,4,1,5835,5,2,100,1,9,9),_NtcDevMonGlobalCpuLoad_Type())
ntcDevMonGlobalCpuLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevMonGlobalCpuLoad.setStatus(_A)
_NtcDevAlarm_ObjectIdentity=ObjectIdentity
ntcDevAlarm=_NtcDevAlarm_ObjectIdentity((1,3,6,1,4,1,5835,5,2,100,1,10))
if mibBuilder.loadTexts:ntcDevAlarm.setStatus(_A)
_NtcDevAlmGenDeviceAlarm_Type=NtcAlarmState
_NtcDevAlmGenDeviceAlarm_Object=MibScalar
ntcDevAlmGenDeviceAlarm=_NtcDevAlmGenDeviceAlarm_Object((1,3,6,1,4,1,5835,5,2,100,1,10,1),_NtcDevAlmGenDeviceAlarm_Type())
ntcDevAlmGenDeviceAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevAlmGenDeviceAlarm.setStatus(_A)
_NtcDevAlmGenBootConfigFailure_Type=NtcAlarmState
_NtcDevAlmGenBootConfigFailure_Object=MibScalar
ntcDevAlmGenBootConfigFailure=_NtcDevAlmGenBootConfigFailure_Object((1,3,6,1,4,1,5835,5,2,100,1,10,2),_NtcDevAlmGenBootConfigFailure_Type())
ntcDevAlmGenBootConfigFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevAlmGenBootConfigFailure.setStatus(_A)
_NtcDevAlmGenInterfaceAlarm_Type=NtcAlarmState
_NtcDevAlmGenInterfaceAlarm_Object=MibScalar
ntcDevAlmGenInterfaceAlarm=_NtcDevAlmGenInterfaceAlarm_Object((1,3,6,1,4,1,5835,5,2,100,1,10,3),_NtcDevAlmGenInterfaceAlarm_Type())
ntcDevAlmGenInterfaceAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevAlmGenInterfaceAlarm.setStatus(_A)
_NtcDevAlmTemperature_Type=NtcAlarmState
_NtcDevAlmTemperature_Object=MibScalar
ntcDevAlmTemperature=_NtcDevAlmTemperature_Object((1,3,6,1,4,1,5835,5,2,100,1,10,4),_NtcDevAlmTemperature_Type())
ntcDevAlmTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevAlmTemperature.setStatus(_A)
_NtcDevAlmInvalidLicenseFile_Type=NtcAlarmState
_NtcDevAlmInvalidLicenseFile_Object=MibScalar
ntcDevAlmInvalidLicenseFile=_NtcDevAlmInvalidLicenseFile_Object((1,3,6,1,4,1,5835,5,2,100,1,10,5),_NtcDevAlmInvalidLicenseFile_Type())
ntcDevAlmInvalidLicenseFile.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevAlmInvalidLicenseFile.setStatus(_A)
_NtcDevAlmFrontPanelFailure_Type=NtcAlarmState
_NtcDevAlmFrontPanelFailure_Object=MibScalar
ntcDevAlmFrontPanelFailure=_NtcDevAlmFrontPanelFailure_Object((1,3,6,1,4,1,5835,5,2,100,1,10,6),_NtcDevAlmFrontPanelFailure_Type())
ntcDevAlmFrontPanelFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevAlmFrontPanelFailure.setStatus(_A)
_NtcDevAlmUpgradeFailure_Type=NtcAlarmState
_NtcDevAlmUpgradeFailure_Object=MibScalar
ntcDevAlmUpgradeFailure=_NtcDevAlmUpgradeFailure_Object((1,3,6,1,4,1,5835,5,2,100,1,10,7),_NtcDevAlmUpgradeFailure_Type())
ntcDevAlmUpgradeFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevAlmUpgradeFailure.setStatus(_A)
_NtcDevAlmNtpNoPeerFailure_Type=NtcAlarmState
_NtcDevAlmNtpNoPeerFailure_Object=MibScalar
ntcDevAlmNtpNoPeerFailure=_NtcDevAlmNtpNoPeerFailure_Object((1,3,6,1,4,1,5835,5,2,100,1,10,8),_NtcDevAlmNtpNoPeerFailure_Type())
ntcDevAlmNtpNoPeerFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevAlmNtpNoPeerFailure.setStatus(_A)
_NtcDevAlmLicenseExpireFile_Type=NtcAlarmState
_NtcDevAlmLicenseExpireFile_Object=MibScalar
ntcDevAlmLicenseExpireFile=_NtcDevAlmLicenseExpireFile_Object((1,3,6,1,4,1,5835,5,2,100,1,10,9),_NtcDevAlmLicenseExpireFile_Type())
ntcDevAlmLicenseExpireFile.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevAlmLicenseExpireFile.setStatus(_A)
_NtcDevAlmHardwareInventory_Type=NtcAlarmState
_NtcDevAlmHardwareInventory_Object=MibScalar
ntcDevAlmHardwareInventory=_NtcDevAlmHardwareInventory_Object((1,3,6,1,4,1,5835,5,2,100,1,10,10),_NtcDevAlmHardwareInventory_Type())
ntcDevAlmHardwareInventory.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevAlmHardwareInventory.setStatus(_A)
_NtcDevAlmHardwareFailure_Type=NtcAlarmState
_NtcDevAlmHardwareFailure_Object=MibScalar
ntcDevAlmHardwareFailure=_NtcDevAlmHardwareFailure_Object((1,3,6,1,4,1,5835,5,2,100,1,10,11),_NtcDevAlmHardwareFailure_Type())
ntcDevAlmHardwareFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevAlmHardwareFailure.setStatus(_A)
_NtcDevAlmInternalError_Type=NtcAlarmState
_NtcDevAlmInternalError_Object=MibScalar
ntcDevAlmInternalError=_NtcDevAlmInternalError_Object((1,3,6,1,4,1,5835,5,2,100,1,10,12),_NtcDevAlmInternalError_Type())
ntcDevAlmInternalError.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevAlmInternalError.setStatus(_A)
_NtcDevAlmLicenseUpgradeFailure_Type=NtcAlarmState
_NtcDevAlmLicenseUpgradeFailure_Object=MibScalar
ntcDevAlmLicenseUpgradeFailure=_NtcDevAlmLicenseUpgradeFailure_Object((1,3,6,1,4,1,5835,5,2,100,1,10,13),_NtcDevAlmLicenseUpgradeFailure_Type())
ntcDevAlmLicenseUpgradeFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevAlmLicenseUpgradeFailure.setStatus(_A)
class _NtcDevReset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('running',0),('hardware',1),('software',2),('configs',3)))
_NtcDevReset_Type.__name__=_G
_NtcDevReset_Object=MibScalar
ntcDevReset=_NtcDevReset_Object((1,3,6,1,4,1,5835,5,2,100,1,11),_NtcDevReset_Type())
ntcDevReset.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevReset.setStatus(_A)
_NtcDevOperatorIdentification_ObjectIdentity=ObjectIdentity
ntcDevOperatorIdentification=_NtcDevOperatorIdentification_ObjectIdentity((1,3,6,1,4,1,5835,5,2,100,1,12))
if mibBuilder.loadTexts:ntcDevOperatorIdentification.setStatus(_A)
class _NtcDevTelephonenbr_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_NtcDevTelephonenbr_Type.__name__=_E
_NtcDevTelephonenbr_Object=MibScalar
ntcDevTelephonenbr=_NtcDevTelephonenbr_Object((1,3,6,1,4,1,5835,5,2,100,1,12,1),_NtcDevTelephonenbr_Type())
ntcDevTelephonenbr.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevTelephonenbr.setStatus(_A)
class _NtcDevTelephoneext_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_NtcDevTelephoneext_Type.__name__=_E
_NtcDevTelephoneext_Object=MibScalar
ntcDevTelephoneext=_NtcDevTelephoneext_Object((1,3,6,1,4,1,5835,5,2,100,1,12,2),_NtcDevTelephoneext_Type())
ntcDevTelephoneext.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevTelephoneext.setStatus(_A)
class _NtcDevCarrId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_NtcDevCarrId_Type.__name__=_E
_NtcDevCarrId_Object=MibScalar
ntcDevCarrId=_NtcDevCarrId_Object((1,3,6,1,4,1,5835,5,2,100,1,12,3),_NtcDevCarrId_Type())
ntcDevCarrId.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevCarrId.setStatus(_A)
_NtcDevLocation_ObjectIdentity=ObjectIdentity
ntcDevLocation=_NtcDevLocation_ObjectIdentity((1,3,6,1,4,1,5835,5,2,100,1,13))
if mibBuilder.loadTexts:ntcDevLocation.setStatus(_A)
class _NtcDevIdLongitude_Type(Float32TC):defaultHexValue=_J
_NtcDevIdLongitude_Type.__name__=_L
_NtcDevIdLongitude_Object=MibScalar
ntcDevIdLongitude=_NtcDevIdLongitude_Object((1,3,6,1,4,1,5835,5,2,100,1,13,1),_NtcDevIdLongitude_Type())
ntcDevIdLongitude.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevIdLongitude.setStatus(_A)
if mibBuilder.loadTexts:ntcDevIdLongitude.setUnits('deg.')
class _NtcDevIdLatitude_Type(Float32TC):defaultHexValue=_J
_NtcDevIdLatitude_Type.__name__=_L
_NtcDevIdLatitude_Object=MibScalar
ntcDevIdLatitude=_NtcDevIdLatitude_Object((1,3,6,1,4,1,5835,5,2,100,1,13,2),_NtcDevIdLatitude_Type())
ntcDevIdLatitude.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevIdLatitude.setStatus(_A)
if mibBuilder.loadTexts:ntcDevIdLatitude.setUnits('deg.')
_NtcDevConfiguration_ObjectIdentity=ObjectIdentity
ntcDevConfiguration=_NtcDevConfiguration_ObjectIdentity((1,3,6,1,4,1,5835,5,2,100,1,14))
if mibBuilder.loadTexts:ntcDevConfiguration.setStatus(_A)
class _NtcDevAutoSave_Type(NtcEnable):defaultValue=0
_NtcDevAutoSave_Type.__name__=_F
_NtcDevAutoSave_Object=MibScalar
ntcDevAutoSave=_NtcDevAutoSave_Object((1,3,6,1,4,1,5835,5,2,100,1,14,1),_NtcDevAutoSave_Type())
ntcDevAutoSave.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevAutoSave.setStatus(_A)
class _NtcDevActCfgState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('saved',0),('updatedNotSaved',1)))
_NtcDevActCfgState_Type.__name__=_G
_NtcDevActCfgState_Object=MibScalar
ntcDevActCfgState=_NtcDevActCfgState_Object((1,3,6,1,4,1,5835,5,2,100,1,14,2),_NtcDevActCfgState_Type())
ntcDevActCfgState.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDevActCfgState.setStatus(_A)
_NtcDevRest_ObjectIdentity=ObjectIdentity
ntcDevRest=_NtcDevRest_ObjectIdentity((1,3,6,1,4,1,5835,5,2,100,1,15))
if mibBuilder.loadTexts:ntcDevRest.setStatus(_A)
class _NtcDevRestEnable_Type(NtcEnable):defaultValue=1
_NtcDevRestEnable_Type.__name__=_F
_NtcDevRestEnable_Object=MibScalar
ntcDevRestEnable=_NtcDevRestEnable_Object((1,3,6,1,4,1,5835,5,2,100,1,15,1),_NtcDevRestEnable_Type())
ntcDevRestEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcDevRestEnable.setStatus(_A)
_NtcDevConformance_ObjectIdentity=ObjectIdentity
ntcDevConformance=_NtcDevConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,100,2))
if mibBuilder.loadTexts:ntcDevConformance.setStatus(_A)
_NtcDevConfCompliance_ObjectIdentity=ObjectIdentity
ntcDevConfCompliance=_NtcDevConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,100,2,1))
if mibBuilder.loadTexts:ntcDevConfCompliance.setStatus(_A)
_NtcDevConfGroup_ObjectIdentity=ObjectIdentity
ntcDevConfGroup=_NtcDevConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,100,2,2))
if mibBuilder.loadTexts:ntcDevConfGroup.setStatus(_A)
ntcDevConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,100,2,2,1))
ntcDevConfGrpV1Standard.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:ntcDevConfGrpV1Standard.setStatus(_A)
ntcDevConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,100,2,1,1))
ntcDevConfCompV1Standard.setObjects((_B,_AS))
if mibBuilder.loadTexts:ntcDevConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcDevice':ntcDevice,'ntcDevObjects':ntcDevObjects,'ntcDevIdentification':ntcDevIdentification,_S:ntcDevIdLabel,_T:ntcDevIdSerialNumber,_U:ntcDevIdUniqueId,_V:ntcDevIdProduct,_W:ntcDevIdDeviceDescription,_X:ntcDevIdTypeId,_Y:ntcDevIdHardwareRevision,_Z:ntcDevIdSoftwareId,_a:ntcDevIdSoftwareVersion,'ntcDevIdDeviceOptionsTable':ntcDevIdDeviceOptionsTable,'ntcDevIdDeviceOptionsEntry':ntcDevIdDeviceOptionsEntry,_N:ntcDevIdDeviceOptionsSalesCode,_b:ntcDevIdDeviceOptionsDescription,_c:ntcDevIdLicenseType,_d:ntcDevIdLicenseTimeRemain,'ntcDevFrontPanel':ntcDevFrontPanel,_e:ntcDevFpEnable,_f:ntcDevFpiAccessLevel,'ntcDevSnmp':ntcDevSnmp,'ntcDevSnmpNotification':ntcDevSnmpNotification,'ntcDevSnmpNotifDestTable':ntcDevSnmpNotifDestTable,'ntcDevSnmpNotifDestEntry':ntcDevSnmpNotifDestEntry,_O:ntcDevSnmpNotifDestDestination,_g:ntcDevSnmpNotifDestIpAddress,_h:ntcDevSnmpNotifDestType,_i:ntcDevSnmpNotifDestCommunity,'ntcDevCli':ntcDevCli,_j:ntcDevCliRemoteEnable,_k:ntcDevCliInactivityTimeout,'ntcDevGui':ntcDevGui,_l:ntcDevGuiEnable,'ntcDevFtp':ntcDevFtp,_m:ntcDevFtpEnable,_n:ntcDevFtpAnonymousEnable,'ntcDevLog':ntcDevLog,'ntcDevLogLocal':ntcDevLogLocal,_o:ntcDevLogLocEnable,'ntcDevLogRemote':ntcDevLogRemote,_p:ntcDevLogRemEnable,_q:ntcDevLogRemIpAddress,_r:ntcDevLogRemUdpPort,'ntcDevLogFilterTable':ntcDevLogFilterTable,'ntcDevLogFilterEntry':ntcDevLogFilterEntry,_P:ntcDevLogFilterFacility,_s:ntcDevLogFilterLevel,'ntcDevDateTime':ntcDevDateTime,_t:ntcDevDtDate,_u:ntcDevDtTime,'ntcDevDtNtp':ntcDevDtNtp,_v:ntcDevDtNtpEnable,'ntcDevDtNtpPeerTable':ntcDevDtNtpPeerTable,'ntcDevDtNtpPeerEntry':ntcDevDtNtpPeerEntry,_Q:ntcDevDtNtpPeerPeer,_w:ntcDevDtNtpPeerIpAddress,'ntcDevMonitor':ntcDevMonitor,_x:ntcDevMonTemperature,_y:ntcDevMonPowerSupply,_z:ntcDevMonCpuLoad,_A0:ntcDevMonMemoryUse,_A1:ntcDevMonUptime,'ntcDevMonSensorsTable':ntcDevMonSensorsTable,'ntcDevMonSensorsEntry':ntcDevMonSensorsEntry,_R:ntcDevMonSensorsSensor,_A2:ntcDevMonSensorsValue,_A3:ntcDevMonHwFailureCause,_A4:ntcDevMonInternalErrorCause,_A5:ntcDevMonGlobalCpuLoad,'ntcDevAlarm':ntcDevAlarm,_A6:ntcDevAlmGenDeviceAlarm,_A7:ntcDevAlmGenBootConfigFailure,_A8:ntcDevAlmGenInterfaceAlarm,_A9:ntcDevAlmTemperature,_AA:ntcDevAlmInvalidLicenseFile,_AB:ntcDevAlmFrontPanelFailure,_AC:ntcDevAlmUpgradeFailure,_AD:ntcDevAlmNtpNoPeerFailure,_AE:ntcDevAlmLicenseExpireFile,_AF:ntcDevAlmHardwareInventory,_AG:ntcDevAlmHardwareFailure,_AH:ntcDevAlmInternalError,_AI:ntcDevAlmLicenseUpgradeFailure,_AJ:ntcDevReset,'ntcDevOperatorIdentification':ntcDevOperatorIdentification,_AK:ntcDevTelephonenbr,_AL:ntcDevTelephoneext,_AM:ntcDevCarrId,'ntcDevLocation':ntcDevLocation,_AN:ntcDevIdLongitude,_AO:ntcDevIdLatitude,'ntcDevConfiguration':ntcDevConfiguration,_AP:ntcDevAutoSave,_AQ:ntcDevActCfgState,'ntcDevRest':ntcDevRest,_AR:ntcDevRestEnable,'ntcDevConformance':ntcDevConformance,'ntcDevConfCompliance':ntcDevConfCompliance,'ntcDevConfCompV1Standard':ntcDevConfCompV1Standard,'ntcDevConfGroup':ntcDevConfGroup,_AS:ntcDevConfGrpV1Standard})