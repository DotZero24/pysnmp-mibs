_a='wioTrapPlcLogout'
_Z='wioTrapPlcLogin'
_Y='wioTrapPlcDownload'
_X='wioTrapPlcOnlineChange'
_W='wioTrapPlcDivideByZero'
_V='wioTrapPlcSoftwareWatchdog'
_U='wioTrapPlcReset'
_T='wioTrapPlcStop'
_S='wioTrapPlcStart'
_R='wioTrapKbusError'
_Q='wioPlcDataIndex'
_P='wioModuleNumber'
_O='wioModbusConnectionIndex'
_N='PrivacyKey'
_M='AuthenticationKey'
_L='SecurityName'
_K='wioTrapReceiverIndex'
_J='wioIecTaskId'
_I='http://www.wago.com/wagoweb/documentation/navigate/nm0dc__e.htm#ethernet'
_H='NotificationType'
_G='IpAddress'
_F='WAGO-MIB'
_E='Integer32'
_D='DisplayString'
_C='read-only'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,_G,'ModuleIdentity','MibIdentifier',_H,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_H,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Wago_ObjectIdentity=ObjectIdentity
wago=_Wago_ObjectIdentity((1,3,6,1,4,1,13576))
_WagoCompany_ObjectIdentity=ObjectIdentity
wagoCompany=_WagoCompany_ObjectIdentity((1,3,6,1,4,1,13576,1))
class _WagoName_Type(DisplayString):defaultValue=OctetString('WAGO Kontakttechnik GmbH & Co. KG');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WagoName_Type.__name__=_D
_WagoName_Object=MibScalar
wagoName=_WagoName_Object((1,3,6,1,4,1,13576,1,1),_WagoName_Type())
wagoName.setMaxAccess(_C)
if mibBuilder.loadTexts:wagoName.setStatus(_A)
class _WagoDescrition_Type(DisplayString):defaultValue=OctetString('WAGO Kontakttechnik GmbH & Co. KG, Hansastr. 27, D-32423 Minden');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WagoDescrition_Type.__name__=_D
_WagoDescrition_Object=MibScalar
wagoDescrition=_WagoDescrition_Object((1,3,6,1,4,1,13576,1,2),_WagoDescrition_Type())
wagoDescrition.setMaxAccess(_C)
if mibBuilder.loadTexts:wagoDescrition.setStatus(_A)
class _WagoURL_Type(DisplayString):defaultValue=OctetString('www.wago.com');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WagoURL_Type.__name__=_D
_WagoURL_Object=MibScalar
wagoURL=_WagoURL_Object((1,3,6,1,4,1,13576,1,3),_WagoURL_Type())
wagoURL.setMaxAccess(_C)
if mibBuilder.loadTexts:wagoURL.setStatus(_A)
_WagoIOProducts_ObjectIdentity=ObjectIdentity
wagoIOProducts=_WagoIOProducts_ObjectIdentity((1,3,6,1,4,1,13576,10))
_WioCommon_ObjectIdentity=ObjectIdentity
wioCommon=_WioCommon_ObjectIdentity((1,3,6,1,4,1,13576,10,1))
class _WioArticleName_Type(DisplayString):defaultValue=OctetString('750-841/000-000');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioArticleName_Type.__name__=_D
_WioArticleName_Object=MibScalar
wioArticleName=_WioArticleName_Object((1,3,6,1,4,1,13576,10,1,1),_WioArticleName_Type())
wioArticleName.setMaxAccess(_C)
if mibBuilder.loadTexts:wioArticleName.setStatus(_A)
class _WioArticleDescription_Type(DisplayString):defaultValue=OctetString('WAGO Ethernet(10/100MBit)-FBC');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WioArticleDescription_Type.__name__=_D
_WioArticleDescription_Object=MibScalar
wioArticleDescription=_WioArticleDescription_Object((1,3,6,1,4,1,13576,10,1,2),_WioArticleDescription_Type())
wioArticleDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:wioArticleDescription.setStatus(_A)
class _WioSerialNumber_Type(DisplayString):defaultValue=OctetString('SNxxxxxxxx-Txxxxxx-mac|0030DExxxxxx');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WioSerialNumber_Type.__name__=_D
_WioSerialNumber_Object=MibScalar
wioSerialNumber=_WioSerialNumber_Object((1,3,6,1,4,1,13576,10,1,3),_WioSerialNumber_Type())
wioSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:wioSerialNumber.setStatus(_A)
class _WioMacAddress_Type(DisplayString):defaultValue=OctetString('0030DExxxxxx');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioMacAddress_Type.__name__=_D
_WioMacAddress_Object=MibScalar
wioMacAddress=_WioMacAddress_Object((1,3,6,1,4,1,13576,10,1,4),_WioMacAddress_Type())
wioMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:wioMacAddress.setStatus(_A)
class _WioURLDatasheet_Type(DisplayString):defaultValue=OctetString(_I);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WioURLDatasheet_Type.__name__=_D
_WioURLDatasheet_Object=MibScalar
wioURLDatasheet=_WioURLDatasheet_Object((1,3,6,1,4,1,13576,10,1,5),_WioURLDatasheet_Type())
wioURLDatasheet.setMaxAccess(_C)
if mibBuilder.loadTexts:wioURLDatasheet.setStatus(_A)
class _WioURLManual_Type(DisplayString):defaultValue=OctetString(_I);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WioURLManual_Type.__name__=_D
_WioURLManual_Object=MibScalar
wioURLManual=_WioURLManual_Object((1,3,6,1,4,1,13576,10,1,6),_WioURLManual_Type())
wioURLManual.setMaxAccess(_C)
if mibBuilder.loadTexts:wioURLManual.setStatus(_A)
_WioDeviceClass_Type=Integer32
_WioDeviceClass_Object=MibScalar
wioDeviceClass=_WioDeviceClass_Object((1,3,6,1,4,1,13576,10,1,7),_WioDeviceClass_Type())
wioDeviceClass.setMaxAccess(_C)
if mibBuilder.loadTexts:wioDeviceClass.setStatus(_A)
_WioDeviceGroup_Type=Integer32
_WioDeviceGroup_Object=MibScalar
wioDeviceGroup=_WioDeviceGroup_Object((1,3,6,1,4,1,13576,10,1,8),_WioDeviceGroup_Type())
wioDeviceGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:wioDeviceGroup.setStatus(_A)
_WioVersion_ObjectIdentity=ObjectIdentity
wioVersion=_WioVersion_ObjectIdentity((1,3,6,1,4,1,13576,10,1,10))
_WioFirmwareIndex_Type=Integer32
_WioFirmwareIndex_Object=MibScalar
wioFirmwareIndex=_WioFirmwareIndex_Object((1,3,6,1,4,1,13576,10,1,10,1),_WioFirmwareIndex_Type())
wioFirmwareIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wioFirmwareIndex.setStatus(_A)
_WioHardwareIndex_Type=Integer32
_WioHardwareIndex_Object=MibScalar
wioHardwareIndex=_WioHardwareIndex_Object((1,3,6,1,4,1,13576,10,1,10,2),_WioHardwareIndex_Type())
wioHardwareIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wioHardwareIndex.setStatus(_A)
_WioFwlIndex_Type=Integer32
_WioFwlIndex_Object=MibScalar
wioFwlIndex=_WioFwlIndex_Object((1,3,6,1,4,1,13576,10,1,10,3),_WioFwlIndex_Type())
wioFwlIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wioFwlIndex.setStatus(_A)
class _WioFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioFirmwareVersion_Type.__name__=_D
_WioFirmwareVersion_Object=MibScalar
wioFirmwareVersion=_WioFirmwareVersion_Object((1,3,6,1,4,1,13576,10,1,10,4),_WioFirmwareVersion_Type())
wioFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:wioFirmwareVersion.setStatus(_A)
_WioRealTimeClock_ObjectIdentity=ObjectIdentity
wioRealTimeClock=_WioRealTimeClock_ObjectIdentity((1,3,6,1,4,1,13576,10,1,11))
class _WioRtcDateTime_Type(DisplayString):defaultValue=OctetString('time xx:xx:xx date xx-xx-xxxx (UTC)');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,35))
_WioRtcDateTime_Type.__name__=_D
_WioRtcDateTime_Object=MibScalar
wioRtcDateTime=_WioRtcDateTime_Object((1,3,6,1,4,1,13576,10,1,11,1),_WioRtcDateTime_Type())
wioRtcDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wioRtcDateTime.setStatus(_A)
_WioRtcTime_Type=Integer32
_WioRtcTime_Object=MibScalar
wioRtcTime=_WioRtcTime_Object((1,3,6,1,4,1,13576,10,1,11,2),_WioRtcTime_Type())
wioRtcTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wioRtcTime.setStatus(_A)
class _WioTimezone_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-12,12))
_WioTimezone_Type.__name__=_E
_WioTimezone_Object=MibScalar
wioTimezone=_WioTimezone_Object((1,3,6,1,4,1,13576,10,1,11,3),_WioTimezone_Type())
wioTimezone.setMaxAccess(_B)
if mibBuilder.loadTexts:wioTimezone.setStatus(_A)
class _WioRtcHourMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WioRtcHourMode_Type.__name__=_E
_WioRtcHourMode_Object=MibScalar
wioRtcHourMode=_WioRtcHourMode_Object((1,3,6,1,4,1,13576,10,1,11,4),_WioRtcHourMode_Type())
wioRtcHourMode.setMaxAccess(_C)
if mibBuilder.loadTexts:wioRtcHourMode.setStatus(_A)
class _WioRtcBatteryStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WioRtcBatteryStatus_Type.__name__=_E
_WioRtcBatteryStatus_Object=MibScalar
wioRtcBatteryStatus=_WioRtcBatteryStatus_Object((1,3,6,1,4,1,13576,10,1,11,5),_WioRtcBatteryStatus_Type())
wioRtcBatteryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wioRtcBatteryStatus.setStatus(_A)
class _WioRtcDayLightSaving_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WioRtcDayLightSaving_Type.__name__=_E
_WioRtcDayLightSaving_Object=MibScalar
wioRtcDayLightSaving=_WioRtcDayLightSaving_Object((1,3,6,1,4,1,13576,10,1,11,6),_WioRtcDayLightSaving_Type())
wioRtcDayLightSaving.setMaxAccess(_B)
if mibBuilder.loadTexts:wioRtcDayLightSaving.setStatus(_A)
_WioEthernet_ObjectIdentity=ObjectIdentity
wioEthernet=_WioEthernet_ObjectIdentity((1,3,6,1,4,1,13576,10,1,12))
class _WioEthernetMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_WioEthernetMode_Type.__name__=_E
_WioEthernetMode_Object=MibScalar
wioEthernetMode=_WioEthernetMode_Object((1,3,6,1,4,1,13576,10,1,12,1),_WioEthernetMode_Type())
wioEthernetMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wioEthernetMode.setStatus(_A)
_WioIp_Type=IpAddress
_WioIp_Object=MibScalar
wioIp=_WioIp_Object((1,3,6,1,4,1,13576,10,1,12,2),_WioIp_Type())
wioIp.setMaxAccess(_B)
if mibBuilder.loadTexts:wioIp.setStatus(_A)
_WioSubnetMask_Type=IpAddress
_WioSubnetMask_Object=MibScalar
wioSubnetMask=_WioSubnetMask_Object((1,3,6,1,4,1,13576,10,1,12,3),_WioSubnetMask_Type())
wioSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSubnetMask.setStatus(_A)
_WioGateway_Type=IpAddress
_WioGateway_Object=MibScalar
wioGateway=_WioGateway_Object((1,3,6,1,4,1,13576,10,1,12,4),_WioGateway_Type())
wioGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:wioGateway.setStatus(_A)
class _WioHostname_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioHostname_Type.__name__=_D
_WioHostname_Object=MibScalar
wioHostname=_WioHostname_Object((1,3,6,1,4,1,13576,10,1,12,5),_WioHostname_Type())
wioHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:wioHostname.setStatus(_A)
class _WioDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioDomainName_Type.__name__=_D
_WioDomainName_Object=MibScalar
wioDomainName=_WioDomainName_Object((1,3,6,1,4,1,13576,10,1,12,6),_WioDomainName_Type())
wioDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:wioDomainName.setStatus(_A)
_WioDnsServer1_Type=IpAddress
_WioDnsServer1_Object=MibScalar
wioDnsServer1=_WioDnsServer1_Object((1,3,6,1,4,1,13576,10,1,12,7),_WioDnsServer1_Type())
wioDnsServer1.setMaxAccess(_B)
if mibBuilder.loadTexts:wioDnsServer1.setStatus(_A)
_WioDnsServer2_Type=IpAddress
_WioDnsServer2_Object=MibScalar
wioDnsServer2=_WioDnsServer2_Object((1,3,6,1,4,1,13576,10,1,12,8),_WioDnsServer2_Type())
wioDnsServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:wioDnsServer2.setStatus(_A)
_WioActualStatus_ObjectIdentity=ObjectIdentity
wioActualStatus=_WioActualStatus_ObjectIdentity((1,3,6,1,4,1,13576,10,1,20))
_WioErrorGroup_Type=Integer32
_WioErrorGroup_Object=MibScalar
wioErrorGroup=_WioErrorGroup_Object((1,3,6,1,4,1,13576,10,1,20,1),_WioErrorGroup_Type())
wioErrorGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:wioErrorGroup.setStatus(_A)
_WioErrorCode_Type=Integer32
_WioErrorCode_Object=MibScalar
wioErrorCode=_WioErrorCode_Object((1,3,6,1,4,1,13576,10,1,20,2),_WioErrorCode_Type())
wioErrorCode.setMaxAccess(_C)
if mibBuilder.loadTexts:wioErrorCode.setStatus(_A)
_WioErrorArgument_Type=Integer32
_WioErrorArgument_Object=MibScalar
wioErrorArgument=_WioErrorArgument_Object((1,3,6,1,4,1,13576,10,1,20,3),_WioErrorArgument_Type())
wioErrorArgument.setMaxAccess(_C)
if mibBuilder.loadTexts:wioErrorArgument.setStatus(_A)
class _WioErrorDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_WioErrorDescription_Type.__name__=_D
_WioErrorDescription_Object=MibScalar
wioErrorDescription=_WioErrorDescription_Object((1,3,6,1,4,1,13576,10,1,20,4),_WioErrorDescription_Type())
wioErrorDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:wioErrorDescription.setStatus(_A)
_WioPlcBrowser_ObjectIdentity=ObjectIdentity
wioPlcBrowser=_WioPlcBrowser_ObjectIdentity((1,3,6,1,4,1,13576,10,1,30))
_WioProjectId_Type=Integer32
_WioProjectId_Object=MibScalar
wioProjectId=_WioProjectId_Object((1,3,6,1,4,1,13576,10,1,30,1),_WioProjectId_Type())
wioProjectId.setMaxAccess(_C)
if mibBuilder.loadTexts:wioProjectId.setStatus(_A)
_WioProjectDate_Type=Integer32
_WioProjectDate_Object=MibScalar
wioProjectDate=_WioProjectDate_Object((1,3,6,1,4,1,13576,10,1,30,2),_WioProjectDate_Type())
wioProjectDate.setMaxAccess(_C)
if mibBuilder.loadTexts:wioProjectDate.setStatus(_A)
class _WioProjectName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioProjectName_Type.__name__=_D
_WioProjectName_Object=MibScalar
wioProjectName=_WioProjectName_Object((1,3,6,1,4,1,13576,10,1,30,3),_WioProjectName_Type())
wioProjectName.setMaxAccess(_C)
if mibBuilder.loadTexts:wioProjectName.setStatus(_A)
class _WioProjectTitle_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioProjectTitle_Type.__name__=_D
_WioProjectTitle_Object=MibScalar
wioProjectTitle=_WioProjectTitle_Object((1,3,6,1,4,1,13576,10,1,30,4),_WioProjectTitle_Type())
wioProjectTitle.setMaxAccess(_C)
if mibBuilder.loadTexts:wioProjectTitle.setStatus(_A)
class _WioProjectVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioProjectVersion_Type.__name__=_D
_WioProjectVersion_Object=MibScalar
wioProjectVersion=_WioProjectVersion_Object((1,3,6,1,4,1,13576,10,1,30,5),_WioProjectVersion_Type())
wioProjectVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:wioProjectVersion.setStatus(_A)
class _WioProjectAuthor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioProjectAuthor_Type.__name__=_D
_WioProjectAuthor_Object=MibScalar
wioProjectAuthor=_WioProjectAuthor_Object((1,3,6,1,4,1,13576,10,1,30,6),_WioProjectAuthor_Type())
wioProjectAuthor.setMaxAccess(_C)
if mibBuilder.loadTexts:wioProjectAuthor.setStatus(_A)
class _WioProjectDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioProjectDescription_Type.__name__=_D
_WioProjectDescription_Object=MibScalar
wioProjectDescription=_WioProjectDescription_Object((1,3,6,1,4,1,13576,10,1,30,7),_WioProjectDescription_Type())
wioProjectDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:wioProjectDescription.setStatus(_A)
_WioNumberOfIecTasks_Type=Integer32
_WioNumberOfIecTasks_Object=MibScalar
wioNumberOfIecTasks=_WioNumberOfIecTasks_Object((1,3,6,1,4,1,13576,10,1,30,8),_WioNumberOfIecTasks_Type())
wioNumberOfIecTasks.setMaxAccess(_C)
if mibBuilder.loadTexts:wioNumberOfIecTasks.setStatus(_A)
_WioIecTaskTable_Object=MibTable
wioIecTaskTable=_WioIecTaskTable_Object((1,3,6,1,4,1,13576,10,1,30,9))
if mibBuilder.loadTexts:wioIecTaskTable.setStatus(_A)
_WioIecTaskEntry_Object=MibTableRow
wioIecTaskEntry=_WioIecTaskEntry_Object((1,3,6,1,4,1,13576,10,1,30,9,1))
wioIecTaskEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:wioIecTaskEntry.setStatus(_A)
class _WioIecTaskId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,29))
_WioIecTaskId_Type.__name__=_E
_WioIecTaskId_Object=MibTableColumn
wioIecTaskId=_WioIecTaskId_Object((1,3,6,1,4,1,13576,10,1,30,9,1,1),_WioIecTaskId_Type())
wioIecTaskId.setMaxAccess(_C)
if mibBuilder.loadTexts:wioIecTaskId.setStatus(_A)
class _WioIecTaskName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioIecTaskName_Type.__name__=_D
_WioIecTaskName_Object=MibTableColumn
wioIecTaskName=_WioIecTaskName_Object((1,3,6,1,4,1,13576,10,1,30,9,1,2),_WioIecTaskName_Type())
wioIecTaskName.setMaxAccess(_C)
if mibBuilder.loadTexts:wioIecTaskName.setStatus(_A)
_WioIecTaskStatus_Type=Integer32
_WioIecTaskStatus_Object=MibTableColumn
wioIecTaskStatus=_WioIecTaskStatus_Object((1,3,6,1,4,1,13576,10,1,30,9,1,3),_WioIecTaskStatus_Type())
wioIecTaskStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wioIecTaskStatus.setStatus(_A)
_WioIecTaskMode_Type=Integer32
_WioIecTaskMode_Object=MibTableColumn
wioIecTaskMode=_WioIecTaskMode_Object((1,3,6,1,4,1,13576,10,1,30,9,1,4),_WioIecTaskMode_Type())
wioIecTaskMode.setMaxAccess(_C)
if mibBuilder.loadTexts:wioIecTaskMode.setStatus(_A)
_WioIecTaskPriority_Type=Integer32
_WioIecTaskPriority_Object=MibTableColumn
wioIecTaskPriority=_WioIecTaskPriority_Object((1,3,6,1,4,1,13576,10,1,30,9,1,5),_WioIecTaskPriority_Type())
wioIecTaskPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:wioIecTaskPriority.setStatus(_A)
_WioIecTaskInterval_Type=Integer32
_WioIecTaskInterval_Object=MibTableColumn
wioIecTaskInterval=_WioIecTaskInterval_Object((1,3,6,1,4,1,13576,10,1,30,9,1,6),_WioIecTaskInterval_Type())
wioIecTaskInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:wioIecTaskInterval.setStatus(_A)
_WioIecTaskEvent_Type=Integer32
_WioIecTaskEvent_Object=MibTableColumn
wioIecTaskEvent=_WioIecTaskEvent_Object((1,3,6,1,4,1,13576,10,1,30,9,1,7),_WioIecTaskEvent_Type())
wioIecTaskEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:wioIecTaskEvent.setStatus(_A)
_WioIecTaskCycleCount_Type=Integer32
_WioIecTaskCycleCount_Object=MibTableColumn
wioIecTaskCycleCount=_WioIecTaskCycleCount_Object((1,3,6,1,4,1,13576,10,1,30,9,1,8),_WioIecTaskCycleCount_Type())
wioIecTaskCycleCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wioIecTaskCycleCount.setStatus(_A)
_WioIecTaskCycleTime_Type=Integer32
_WioIecTaskCycleTime_Object=MibTableColumn
wioIecTaskCycleTime=_WioIecTaskCycleTime_Object((1,3,6,1,4,1,13576,10,1,30,9,1,9),_WioIecTaskCycleTime_Type())
wioIecTaskCycleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:wioIecTaskCycleTime.setStatus(_A)
_WioIecTaskCycleTimeMin_Type=Integer32
_WioIecTaskCycleTimeMin_Object=MibTableColumn
wioIecTaskCycleTimeMin=_WioIecTaskCycleTimeMin_Object((1,3,6,1,4,1,13576,10,1,30,9,1,10),_WioIecTaskCycleTimeMin_Type())
wioIecTaskCycleTimeMin.setMaxAccess(_C)
if mibBuilder.loadTexts:wioIecTaskCycleTimeMin.setStatus(_A)
_WioIecTaskCycleTimeMax_Type=Integer32
_WioIecTaskCycleTimeMax_Object=MibTableColumn
wioIecTaskCycleTimeMax=_WioIecTaskCycleTimeMax_Object((1,3,6,1,4,1,13576,10,1,30,9,1,11),_WioIecTaskCycleTimeMax_Type())
wioIecTaskCycleTimeMax.setMaxAccess(_C)
if mibBuilder.loadTexts:wioIecTaskCycleTimeMax.setStatus(_A)
_WioIecTaskCycleTimeAvg_Type=Integer32
_WioIecTaskCycleTimeAvg_Object=MibTableColumn
wioIecTaskCycleTimeAvg=_WioIecTaskCycleTimeAvg_Object((1,3,6,1,4,1,13576,10,1,30,9,1,12),_WioIecTaskCycleTimeAvg_Type())
wioIecTaskCycleTimeAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:wioIecTaskCycleTimeAvg.setStatus(_A)
_WioEthernetProtocols_ObjectIdentity=ObjectIdentity
wioEthernetProtocols=_WioEthernetProtocols_ObjectIdentity((1,3,6,1,4,1,13576,10,1,40))
_WioHttp_ObjectIdentity=ObjectIdentity
wioHttp=_WioHttp_ObjectIdentity((1,3,6,1,4,1,13576,10,1,40,1))
class _WioHttpEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WioHttpEnable_Type.__name__=_E
_WioHttpEnable_Object=MibScalar
wioHttpEnable=_WioHttpEnable_Object((1,3,6,1,4,1,13576,10,1,40,1,1),_WioHttpEnable_Type())
wioHttpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wioHttpEnable.setStatus(_A)
class _WioHttpAuthenticationEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WioHttpAuthenticationEnable_Type.__name__=_E
_WioHttpAuthenticationEnable_Object=MibScalar
wioHttpAuthenticationEnable=_WioHttpAuthenticationEnable_Object((1,3,6,1,4,1,13576,10,1,40,1,2),_WioHttpAuthenticationEnable_Type())
wioHttpAuthenticationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wioHttpAuthenticationEnable.setStatus(_A)
class _WioHttpPort_Type(Integer32):defaultValue=80
_WioHttpPort_Type.__name__=_E
_WioHttpPort_Object=MibScalar
wioHttpPort=_WioHttpPort_Object((1,3,6,1,4,1,13576,10,1,40,1,3),_WioHttpPort_Type())
wioHttpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:wioHttpPort.setStatus(_A)
_WioFtp_ObjectIdentity=ObjectIdentity
wioFtp=_WioFtp_ObjectIdentity((1,3,6,1,4,1,13576,10,1,40,2))
class _WioFtpEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WioFtpEnable_Type.__name__=_E
_WioFtpEnable_Object=MibScalar
wioFtpEnable=_WioFtpEnable_Object((1,3,6,1,4,1,13576,10,1,40,2,1),_WioFtpEnable_Type())
wioFtpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wioFtpEnable.setStatus(_A)
_WioSntp_ObjectIdentity=ObjectIdentity
wioSntp=_WioSntp_ObjectIdentity((1,3,6,1,4,1,13576,10,1,40,3))
class _WioSntpEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WioSntpEnable_Type.__name__=_E
_WioSntpEnable_Object=MibScalar
wioSntpEnable=_WioSntpEnable_Object((1,3,6,1,4,1,13576,10,1,40,3,1),_WioSntpEnable_Type())
wioSntpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSntpEnable.setStatus(_A)
_WioSntpServerAddress_Type=IpAddress
_WioSntpServerAddress_Object=MibScalar
wioSntpServerAddress=_WioSntpServerAddress_Object((1,3,6,1,4,1,13576,10,1,40,3,2),_WioSntpServerAddress_Type())
wioSntpServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSntpServerAddress.setStatus(_A)
class _WioSntpClientIntervall_Type(Integer32):defaultValue=0
_WioSntpClientIntervall_Type.__name__=_E
_WioSntpClientIntervall_Object=MibScalar
wioSntpClientIntervall=_WioSntpClientIntervall_Object((1,3,6,1,4,1,13576,10,1,40,3,3),_WioSntpClientIntervall_Type())
wioSntpClientIntervall.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSntpClientIntervall.setStatus(_A)
class _WioSntpClientTimeout_Type(Integer32):defaultValue=2000
_WioSntpClientTimeout_Type.__name__=_E
_WioSntpClientTimeout_Object=MibScalar
wioSntpClientTimeout=_WioSntpClientTimeout_Object((1,3,6,1,4,1,13576,10,1,40,3,4),_WioSntpClientTimeout_Type())
wioSntpClientTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSntpClientTimeout.setStatus(_A)
class _WioSntpClientDayLightSaving_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WioSntpClientDayLightSaving_Type.__name__=_E
_WioSntpClientDayLightSaving_Object=MibScalar
wioSntpClientDayLightSaving=_WioSntpClientDayLightSaving_Object((1,3,6,1,4,1,13576,10,1,40,3,5),_WioSntpClientDayLightSaving_Type())
wioSntpClientDayLightSaving.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSntpClientDayLightSaving.setStatus(_A)
_WioSnmp_ObjectIdentity=ObjectIdentity
wioSnmp=_WioSnmp_ObjectIdentity((1,3,6,1,4,1,13576,10,1,40,4))
class _WioSnmpEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WioSnmpEnable_Type.__name__=_E
_WioSnmpEnable_Object=MibScalar
wioSnmpEnable=_WioSnmpEnable_Object((1,3,6,1,4,1,13576,10,1,40,4,1),_WioSnmpEnable_Type())
wioSnmpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSnmpEnable.setStatus(_A)
_WioSnmpV1V2c_ObjectIdentity=ObjectIdentity
wioSnmpV1V2c=_WioSnmpV1V2c_ObjectIdentity((1,3,6,1,4,1,13576,10,1,40,4,2))
class _WioSnmpEnableV1V2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WioSnmpEnableV1V2_Type.__name__=_E
_WioSnmpEnableV1V2_Object=MibScalar
wioSnmpEnableV1V2=_WioSnmpEnableV1V2_Object((1,3,6,1,4,1,13576,10,1,40,4,2,1),_WioSnmpEnableV1V2_Type())
wioSnmpEnableV1V2.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSnmpEnableV1V2.setStatus(_A)
class _WioLocalCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioLocalCommunity_Type.__name__=_D
_WioLocalCommunity_Object=MibScalar
wioLocalCommunity=_WioLocalCommunity_Object((1,3,6,1,4,1,13576,10,1,40,4,2,2),_WioLocalCommunity_Type())
wioLocalCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:wioLocalCommunity.setStatus(_A)
_WioTrapReceiverV1V2Table_Object=MibTable
wioTrapReceiverV1V2Table=_WioTrapReceiverV1V2Table_Object((1,3,6,1,4,1,13576,10,1,40,4,2,3))
if mibBuilder.loadTexts:wioTrapReceiverV1V2Table.setStatus(_A)
_WioTrapReceiverV1V2Entry_Object=MibTableRow
wioTrapReceiverV1V2Entry=_WioTrapReceiverV1V2Entry_Object((1,3,6,1,4,1,13576,10,1,40,4,2,3,1))
wioTrapReceiverV1V2Entry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:wioTrapReceiverV1V2Entry.setStatus(_A)
_WioTrapReceiverIndex_Type=Integer32
_WioTrapReceiverIndex_Object=MibTableColumn
wioTrapReceiverIndex=_WioTrapReceiverIndex_Object((1,3,6,1,4,1,13576,10,1,40,4,2,3,1,1),_WioTrapReceiverIndex_Type())
wioTrapReceiverIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wioTrapReceiverIndex.setStatus(_A)
_WioTrapReceiverIpAddress_Type=IpAddress
_WioTrapReceiverIpAddress_Object=MibTableColumn
wioTrapReceiverIpAddress=_WioTrapReceiverIpAddress_Object((1,3,6,1,4,1,13576,10,1,40,4,2,3,1,2),_WioTrapReceiverIpAddress_Type())
wioTrapReceiverIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wioTrapReceiverIpAddress.setStatus(_A)
class _WioTrapReceiverCommunityName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioTrapReceiverCommunityName_Type.__name__=_D
_WioTrapReceiverCommunityName_Object=MibTableColumn
wioTrapReceiverCommunityName=_WioTrapReceiverCommunityName_Object((1,3,6,1,4,1,13576,10,1,40,4,2,3,1,3),_WioTrapReceiverCommunityName_Type())
wioTrapReceiverCommunityName.setMaxAccess(_B)
if mibBuilder.loadTexts:wioTrapReceiverCommunityName.setStatus(_A)
class _WioTrapReceiverTrapVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_WioTrapReceiverTrapVersion_Type.__name__=_E
_WioTrapReceiverTrapVersion_Object=MibTableColumn
wioTrapReceiverTrapVersion=_WioTrapReceiverTrapVersion_Object((1,3,6,1,4,1,13576,10,1,40,4,2,3,1,4),_WioTrapReceiverTrapVersion_Type())
wioTrapReceiverTrapVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:wioTrapReceiverTrapVersion.setStatus(_A)
_WioSnmpV3Usm_ObjectIdentity=ObjectIdentity
wioSnmpV3Usm=_WioSnmpV3Usm_ObjectIdentity((1,3,6,1,4,1,13576,10,1,40,4,3))
class _WioSnmp1UserEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WioSnmp1UserEnable_Type.__name__=_E
_WioSnmp1UserEnable_Object=MibScalar
wioSnmp1UserEnable=_WioSnmp1UserEnable_Object((1,3,6,1,4,1,13576,10,1,40,4,3,1),_WioSnmp1UserEnable_Type())
wioSnmp1UserEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSnmp1UserEnable.setStatus(_A)
class _WioSnmp1AuthenticationTyp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_WioSnmp1AuthenticationTyp_Type.__name__=_E
_WioSnmp1AuthenticationTyp_Object=MibScalar
wioSnmp1AuthenticationTyp=_WioSnmp1AuthenticationTyp_Object((1,3,6,1,4,1,13576,10,1,40,4,3,2),_WioSnmp1AuthenticationTyp_Type())
wioSnmp1AuthenticationTyp.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSnmp1AuthenticationTyp.setStatus(_A)
class _WioSnmp1AuthenticationName_Type(DisplayString):defaultValue=OctetString(_L);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioSnmp1AuthenticationName_Type.__name__=_D
_WioSnmp1AuthenticationName_Object=MibScalar
wioSnmp1AuthenticationName=_WioSnmp1AuthenticationName_Object((1,3,6,1,4,1,13576,10,1,40,4,3,3),_WioSnmp1AuthenticationName_Type())
wioSnmp1AuthenticationName.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSnmp1AuthenticationName.setStatus(_A)
class _WioSnmp1AuthenticationKey_Type(DisplayString):defaultValue=OctetString(_M);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioSnmp1AuthenticationKey_Type.__name__=_D
_WioSnmp1AuthenticationKey_Object=MibScalar
wioSnmp1AuthenticationKey=_WioSnmp1AuthenticationKey_Object((1,3,6,1,4,1,13576,10,1,40,4,3,4),_WioSnmp1AuthenticationKey_Type())
wioSnmp1AuthenticationKey.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSnmp1AuthenticationKey.setStatus(_A)
class _WioSnmp1PrivacyEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WioSnmp1PrivacyEnable_Type.__name__=_E
_WioSnmp1PrivacyEnable_Object=MibScalar
wioSnmp1PrivacyEnable=_WioSnmp1PrivacyEnable_Object((1,3,6,1,4,1,13576,10,1,40,4,3,5),_WioSnmp1PrivacyEnable_Type())
wioSnmp1PrivacyEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSnmp1PrivacyEnable.setStatus(_A)
class _WioSnmp1PrivacyKey_Type(DisplayString):defaultValue=OctetString(_N);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioSnmp1PrivacyKey_Type.__name__=_D
_WioSnmp1PrivacyKey_Object=MibScalar
wioSnmp1PrivacyKey=_WioSnmp1PrivacyKey_Object((1,3,6,1,4,1,13576,10,1,40,4,3,6),_WioSnmp1PrivacyKey_Type())
wioSnmp1PrivacyKey.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSnmp1PrivacyKey.setStatus(_A)
class _WioSnmp1NotificationEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WioSnmp1NotificationEnable_Type.__name__=_E
_WioSnmp1NotificationEnable_Object=MibScalar
wioSnmp1NotificationEnable=_WioSnmp1NotificationEnable_Object((1,3,6,1,4,1,13576,10,1,40,4,3,7),_WioSnmp1NotificationEnable_Type())
wioSnmp1NotificationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSnmp1NotificationEnable.setStatus(_A)
class _WioSnmp1NotificationReceiverIP_Type(IpAddress):defaultHexValue='C0A80101'
_WioSnmp1NotificationReceiverIP_Type.__name__=_G
_WioSnmp1NotificationReceiverIP_Object=MibScalar
wioSnmp1NotificationReceiverIP=_WioSnmp1NotificationReceiverIP_Object((1,3,6,1,4,1,13576,10,1,40,4,3,8),_WioSnmp1NotificationReceiverIP_Type())
wioSnmp1NotificationReceiverIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSnmp1NotificationReceiverIP.setStatus(_A)
class _WioSnmp2UserEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WioSnmp2UserEnable_Type.__name__=_E
_WioSnmp2UserEnable_Object=MibScalar
wioSnmp2UserEnable=_WioSnmp2UserEnable_Object((1,3,6,1,4,1,13576,10,1,40,4,3,9),_WioSnmp2UserEnable_Type())
wioSnmp2UserEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSnmp2UserEnable.setStatus(_A)
class _WioSnmp2AuthenticationTyp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_WioSnmp2AuthenticationTyp_Type.__name__=_E
_WioSnmp2AuthenticationTyp_Object=MibScalar
wioSnmp2AuthenticationTyp=_WioSnmp2AuthenticationTyp_Object((1,3,6,1,4,1,13576,10,1,40,4,3,10),_WioSnmp2AuthenticationTyp_Type())
wioSnmp2AuthenticationTyp.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSnmp2AuthenticationTyp.setStatus(_A)
class _WioSnmp2AuthenticationName_Type(DisplayString):defaultValue=OctetString(_L);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioSnmp2AuthenticationName_Type.__name__=_D
_WioSnmp2AuthenticationName_Object=MibScalar
wioSnmp2AuthenticationName=_WioSnmp2AuthenticationName_Object((1,3,6,1,4,1,13576,10,1,40,4,3,11),_WioSnmp2AuthenticationName_Type())
wioSnmp2AuthenticationName.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSnmp2AuthenticationName.setStatus(_A)
class _WioSnmp2AuthenticationKey_Type(DisplayString):defaultValue=OctetString(_M);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioSnmp2AuthenticationKey_Type.__name__=_D
_WioSnmp2AuthenticationKey_Object=MibScalar
wioSnmp2AuthenticationKey=_WioSnmp2AuthenticationKey_Object((1,3,6,1,4,1,13576,10,1,40,4,3,12),_WioSnmp2AuthenticationKey_Type())
wioSnmp2AuthenticationKey.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSnmp2AuthenticationKey.setStatus(_A)
class _WioSnmp2PrivacyEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WioSnmp2PrivacyEnable_Type.__name__=_E
_WioSnmp2PrivacyEnable_Object=MibScalar
wioSnmp2PrivacyEnable=_WioSnmp2PrivacyEnable_Object((1,3,6,1,4,1,13576,10,1,40,4,3,13),_WioSnmp2PrivacyEnable_Type())
wioSnmp2PrivacyEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSnmp2PrivacyEnable.setStatus(_A)
class _WioSnmp2PrivacyKey_Type(DisplayString):defaultValue=OctetString(_N);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioSnmp2PrivacyKey_Type.__name__=_D
_WioSnmp2PrivacyKey_Object=MibScalar
wioSnmp2PrivacyKey=_WioSnmp2PrivacyKey_Object((1,3,6,1,4,1,13576,10,1,40,4,3,14),_WioSnmp2PrivacyKey_Type())
wioSnmp2PrivacyKey.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSnmp2PrivacyKey.setStatus(_A)
class _WioSnmp2NotificationEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WioSnmp2NotificationEnable_Type.__name__=_E
_WioSnmp2NotificationEnable_Object=MibScalar
wioSnmp2NotificationEnable=_WioSnmp2NotificationEnable_Object((1,3,6,1,4,1,13576,10,1,40,4,3,15),_WioSnmp2NotificationEnable_Type())
wioSnmp2NotificationEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSnmp2NotificationEnable.setStatus(_A)
class _WioSnmp2NotificationReceiverIP_Type(IpAddress):defaultHexValue='00000000'
_WioSnmp2NotificationReceiverIP_Type.__name__=_G
_WioSnmp2NotificationReceiverIP_Object=MibScalar
wioSnmp2NotificationReceiverIP=_WioSnmp2NotificationReceiverIP_Object((1,3,6,1,4,1,13576,10,1,40,4,3,16),_WioSnmp2NotificationReceiverIP_Type())
wioSnmp2NotificationReceiverIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wioSnmp2NotificationReceiverIP.setStatus(_A)
_WioTrapMessages_ObjectIdentity=ObjectIdentity
wioTrapMessages=_WioTrapMessages_ObjectIdentity((1,3,6,1,4,1,13576,10,1,40,4,4))
class _WioTrapKbusError_Type(DisplayString):defaultValue=OctetString('Kbus Error');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioTrapKbusError_Type.__name__=_D
_WioTrapKbusError_Object=MibScalar
wioTrapKbusError=_WioTrapKbusError_Object((1,3,6,1,4,1,13576,10,1,40,4,4,1),_WioTrapKbusError_Type())
wioTrapKbusError.setMaxAccess(_B)
if mibBuilder.loadTexts:wioTrapKbusError.setStatus(_A)
class _WioTrapPlcStart_Type(DisplayString):defaultValue=OctetString('Plc Start');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioTrapPlcStart_Type.__name__=_D
_WioTrapPlcStart_Object=MibScalar
wioTrapPlcStart=_WioTrapPlcStart_Object((1,3,6,1,4,1,13576,10,1,40,4,4,2),_WioTrapPlcStart_Type())
wioTrapPlcStart.setMaxAccess(_B)
if mibBuilder.loadTexts:wioTrapPlcStart.setStatus(_A)
class _WioTrapPlcStop_Type(DisplayString):defaultValue=OctetString('Plc Stop');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioTrapPlcStop_Type.__name__=_D
_WioTrapPlcStop_Object=MibScalar
wioTrapPlcStop=_WioTrapPlcStop_Object((1,3,6,1,4,1,13576,10,1,40,4,4,3),_WioTrapPlcStop_Type())
wioTrapPlcStop.setMaxAccess(_B)
if mibBuilder.loadTexts:wioTrapPlcStop.setStatus(_A)
class _WioTrapPlcReset_Type(DisplayString):defaultValue=OctetString('Plc Reset');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioTrapPlcReset_Type.__name__=_D
_WioTrapPlcReset_Object=MibScalar
wioTrapPlcReset=_WioTrapPlcReset_Object((1,3,6,1,4,1,13576,10,1,40,4,4,4),_WioTrapPlcReset_Type())
wioTrapPlcReset.setMaxAccess(_B)
if mibBuilder.loadTexts:wioTrapPlcReset.setStatus(_A)
class _WioTrapPlcSoftwareWatchdog_Type(DisplayString):defaultValue=OctetString('Plc Software Watchdog');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioTrapPlcSoftwareWatchdog_Type.__name__=_D
_WioTrapPlcSoftwareWatchdog_Object=MibScalar
wioTrapPlcSoftwareWatchdog=_WioTrapPlcSoftwareWatchdog_Object((1,3,6,1,4,1,13576,10,1,40,4,4,5),_WioTrapPlcSoftwareWatchdog_Type())
wioTrapPlcSoftwareWatchdog.setMaxAccess(_B)
if mibBuilder.loadTexts:wioTrapPlcSoftwareWatchdog.setStatus(_A)
class _WioTrapPlcDivideByZero_Type(DisplayString):defaultValue=OctetString('Plc Division By Zero');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioTrapPlcDivideByZero_Type.__name__=_D
_WioTrapPlcDivideByZero_Object=MibScalar
wioTrapPlcDivideByZero=_WioTrapPlcDivideByZero_Object((1,3,6,1,4,1,13576,10,1,40,4,4,6),_WioTrapPlcDivideByZero_Type())
wioTrapPlcDivideByZero.setMaxAccess(_B)
if mibBuilder.loadTexts:wioTrapPlcDivideByZero.setStatus(_A)
class _WioTrapPlcOnlineChange_Type(DisplayString):defaultValue=OctetString('Plc Online Change');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioTrapPlcOnlineChange_Type.__name__=_D
_WioTrapPlcOnlineChange_Object=MibScalar
wioTrapPlcOnlineChange=_WioTrapPlcOnlineChange_Object((1,3,6,1,4,1,13576,10,1,40,4,4,7),_WioTrapPlcOnlineChange_Type())
wioTrapPlcOnlineChange.setMaxAccess(_B)
if mibBuilder.loadTexts:wioTrapPlcOnlineChange.setStatus(_A)
class _WioTrapPlcDownload_Type(DisplayString):defaultValue=OctetString('Plc Download Programm');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioTrapPlcDownload_Type.__name__=_D
_WioTrapPlcDownload_Object=MibScalar
wioTrapPlcDownload=_WioTrapPlcDownload_Object((1,3,6,1,4,1,13576,10,1,40,4,4,8),_WioTrapPlcDownload_Type())
wioTrapPlcDownload.setMaxAccess(_B)
if mibBuilder.loadTexts:wioTrapPlcDownload.setStatus(_A)
class _WioTrapPlcLogin_Type(DisplayString):defaultValue=OctetString('Plc Login');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioTrapPlcLogin_Type.__name__=_D
_WioTrapPlcLogin_Object=MibScalar
wioTrapPlcLogin=_WioTrapPlcLogin_Object((1,3,6,1,4,1,13576,10,1,40,4,4,9),_WioTrapPlcLogin_Type())
wioTrapPlcLogin.setMaxAccess(_B)
if mibBuilder.loadTexts:wioTrapPlcLogin.setStatus(_A)
class _WioTrapPlcLogout_Type(DisplayString):defaultValue=OctetString('Plc Logout');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioTrapPlcLogout_Type.__name__=_D
_WioTrapPlcLogout_Object=MibScalar
wioTrapPlcLogout=_WioTrapPlcLogout_Object((1,3,6,1,4,1,13576,10,1,40,4,4,10),_WioTrapPlcLogout_Type())
wioTrapPlcLogout.setMaxAccess(_B)
if mibBuilder.loadTexts:wioTrapPlcLogout.setStatus(_A)
_WioUserTrapMessages_ObjectIdentity=ObjectIdentity
wioUserTrapMessages=_WioUserTrapMessages_ObjectIdentity((1,3,6,1,4,1,13576,10,1,40,4,5))
class _WioUserTrapMsg1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WioUserTrapMsg1_Type.__name__=_D
_WioUserTrapMsg1_Object=MibScalar
wioUserTrapMsg1=_WioUserTrapMsg1_Object((1,3,6,1,4,1,13576,10,1,40,4,5,1),_WioUserTrapMsg1_Type())
wioUserTrapMsg1.setMaxAccess(_B)
if mibBuilder.loadTexts:wioUserTrapMsg1.setStatus(_A)
class _WioUserTrapMsg2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WioUserTrapMsg2_Type.__name__=_D
_WioUserTrapMsg2_Object=MibScalar
wioUserTrapMsg2=_WioUserTrapMsg2_Object((1,3,6,1,4,1,13576,10,1,40,4,5,2),_WioUserTrapMsg2_Type())
wioUserTrapMsg2.setMaxAccess(_B)
if mibBuilder.loadTexts:wioUserTrapMsg2.setStatus(_A)
class _WioUserTrapMsg3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WioUserTrapMsg3_Type.__name__=_D
_WioUserTrapMsg3_Object=MibScalar
wioUserTrapMsg3=_WioUserTrapMsg3_Object((1,3,6,1,4,1,13576,10,1,40,4,5,3),_WioUserTrapMsg3_Type())
wioUserTrapMsg3.setMaxAccess(_B)
if mibBuilder.loadTexts:wioUserTrapMsg3.setStatus(_A)
class _WioUserTrapMsg4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WioUserTrapMsg4_Type.__name__=_D
_WioUserTrapMsg4_Object=MibScalar
wioUserTrapMsg4=_WioUserTrapMsg4_Object((1,3,6,1,4,1,13576,10,1,40,4,5,4),_WioUserTrapMsg4_Type())
wioUserTrapMsg4.setMaxAccess(_B)
if mibBuilder.loadTexts:wioUserTrapMsg4.setStatus(_A)
class _WioUserTrapMsg5_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WioUserTrapMsg5_Type.__name__=_D
_WioUserTrapMsg5_Object=MibScalar
wioUserTrapMsg5=_WioUserTrapMsg5_Object((1,3,6,1,4,1,13576,10,1,40,4,5,5),_WioUserTrapMsg5_Type())
wioUserTrapMsg5.setMaxAccess(_B)
if mibBuilder.loadTexts:wioUserTrapMsg5.setStatus(_A)
class _WioUserTrapMsg6_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WioUserTrapMsg6_Type.__name__=_D
_WioUserTrapMsg6_Object=MibScalar
wioUserTrapMsg6=_WioUserTrapMsg6_Object((1,3,6,1,4,1,13576,10,1,40,4,5,6),_WioUserTrapMsg6_Type())
wioUserTrapMsg6.setMaxAccess(_B)
if mibBuilder.loadTexts:wioUserTrapMsg6.setStatus(_A)
class _WioUserTrapMsg7_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WioUserTrapMsg7_Type.__name__=_D
_WioUserTrapMsg7_Object=MibScalar
wioUserTrapMsg7=_WioUserTrapMsg7_Object((1,3,6,1,4,1,13576,10,1,40,4,5,7),_WioUserTrapMsg7_Type())
wioUserTrapMsg7.setMaxAccess(_B)
if mibBuilder.loadTexts:wioUserTrapMsg7.setStatus(_A)
class _WioUserTrapMsg8_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WioUserTrapMsg8_Type.__name__=_D
_WioUserTrapMsg8_Object=MibScalar
wioUserTrapMsg8=_WioUserTrapMsg8_Object((1,3,6,1,4,1,13576,10,1,40,4,5,8),_WioUserTrapMsg8_Type())
wioUserTrapMsg8.setMaxAccess(_B)
if mibBuilder.loadTexts:wioUserTrapMsg8.setStatus(_A)
class _WioUserTrapMsg9_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WioUserTrapMsg9_Type.__name__=_D
_WioUserTrapMsg9_Object=MibScalar
wioUserTrapMsg9=_WioUserTrapMsg9_Object((1,3,6,1,4,1,13576,10,1,40,4,5,9),_WioUserTrapMsg9_Type())
wioUserTrapMsg9.setMaxAccess(_B)
if mibBuilder.loadTexts:wioUserTrapMsg9.setStatus(_A)
class _WioUserTrapMsg10_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_WioUserTrapMsg10_Type.__name__=_D
_WioUserTrapMsg10_Object=MibScalar
wioUserTrapMsg10=_WioUserTrapMsg10_Object((1,3,6,1,4,1,13576,10,1,40,4,5,10),_WioUserTrapMsg10_Type())
wioUserTrapMsg10.setMaxAccess(_B)
if mibBuilder.loadTexts:wioUserTrapMsg10.setStatus(_A)
_WioCoDeSys_ObjectIdentity=ObjectIdentity
wioCoDeSys=_WioCoDeSys_ObjectIdentity((1,3,6,1,4,1,13576,10,1,40,5))
class _WioCoDeSysEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WioCoDeSysEnable_Type.__name__=_E
_WioCoDeSysEnable_Object=MibScalar
wioCoDeSysEnable=_WioCoDeSysEnable_Object((1,3,6,1,4,1,13576,10,1,40,5,1),_WioCoDeSysEnable_Type())
wioCoDeSysEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wioCoDeSysEnable.setStatus(_A)
_WioModbus_ObjectIdentity=ObjectIdentity
wioModbus=_WioModbus_ObjectIdentity((1,3,6,1,4,1,13576,10,1,40,6))
class _WioModbusTcpEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WioModbusTcpEnable_Type.__name__=_E
_WioModbusTcpEnable_Object=MibScalar
wioModbusTcpEnable=_WioModbusTcpEnable_Object((1,3,6,1,4,1,13576,10,1,40,6,1),_WioModbusTcpEnable_Type())
wioModbusTcpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wioModbusTcpEnable.setStatus(_A)
class _WioModbusUdbEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WioModbusUdbEnable_Type.__name__=_E
_WioModbusUdbEnable_Object=MibScalar
wioModbusUdbEnable=_WioModbusUdbEnable_Object((1,3,6,1,4,1,13576,10,1,40,6,2),_WioModbusUdbEnable_Type())
wioModbusUdbEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wioModbusUdbEnable.setStatus(_A)
class _WioMaxConnections_Type(Integer32):defaultValue=15
_WioMaxConnections_Type.__name__=_E
_WioMaxConnections_Object=MibScalar
wioMaxConnections=_WioMaxConnections_Object((1,3,6,1,4,1,13576,10,1,40,6,3),_WioMaxConnections_Type())
wioMaxConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:wioMaxConnections.setStatus(_A)
class _WioConnectionTimeout_Type(Integer32):defaultValue=600
_WioConnectionTimeout_Type.__name__=_E
_WioConnectionTimeout_Object=MibScalar
wioConnectionTimeout=_WioConnectionTimeout_Object((1,3,6,1,4,1,13576,10,1,40,6,4),_WioConnectionTimeout_Type())
wioConnectionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wioConnectionTimeout.setStatus(_A)
class _WioModbusWatchdogMode_Type(Integer32):defaultValue=0
_WioModbusWatchdogMode_Type.__name__=_E
_WioModbusWatchdogMode_Object=MibScalar
wioModbusWatchdogMode=_WioModbusWatchdogMode_Object((1,3,6,1,4,1,13576,10,1,40,6,5),_WioModbusWatchdogMode_Type())
wioModbusWatchdogMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wioModbusWatchdogMode.setStatus(_A)
class _WioModbusWatchdogTime_Type(Integer32):defaultValue=100
_WioModbusWatchdogTime_Type.__name__=_E
_WioModbusWatchdogTime_Object=MibScalar
wioModbusWatchdogTime=_WioModbusWatchdogTime_Object((1,3,6,1,4,1,13576,10,1,40,6,6),_WioModbusWatchdogTime_Type())
wioModbusWatchdogTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wioModbusWatchdogTime.setStatus(_A)
class _WioFreeModbusSockets_Type(Integer32):defaultValue=15
_WioFreeModbusSockets_Type.__name__=_E
_WioFreeModbusSockets_Object=MibScalar
wioFreeModbusSockets=_WioFreeModbusSockets_Object((1,3,6,1,4,1,13576,10,1,40,6,7),_WioFreeModbusSockets_Type())
wioFreeModbusSockets.setMaxAccess(_C)
if mibBuilder.loadTexts:wioFreeModbusSockets.setStatus(_A)
_WioModbusConnectionTable_Object=MibTable
wioModbusConnectionTable=_WioModbusConnectionTable_Object((1,3,6,1,4,1,13576,10,1,40,6,8))
if mibBuilder.loadTexts:wioModbusConnectionTable.setStatus(_A)
_WioModbusConnectionEntry_Object=MibTableRow
wioModbusConnectionEntry=_WioModbusConnectionEntry_Object((1,3,6,1,4,1,13576,10,1,40,6,8,1))
wioModbusConnectionEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:wioModbusConnectionEntry.setStatus(_A)
class _WioModbusConnectionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_WioModbusConnectionIndex_Type.__name__=_E
_WioModbusConnectionIndex_Object=MibTableColumn
wioModbusConnectionIndex=_WioModbusConnectionIndex_Object((1,3,6,1,4,1,13576,10,1,40,6,8,1,1),_WioModbusConnectionIndex_Type())
wioModbusConnectionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wioModbusConnectionIndex.setStatus(_A)
_WioModbusConnectionIp_Type=IpAddress
_WioModbusConnectionIp_Object=MibTableColumn
wioModbusConnectionIp=_WioModbusConnectionIp_Object((1,3,6,1,4,1,13576,10,1,40,6,8,1,2),_WioModbusConnectionIp_Type())
wioModbusConnectionIp.setMaxAccess(_C)
if mibBuilder.loadTexts:wioModbusConnectionIp.setStatus(_A)
_WioModbusConnectionPort_Type=Integer32
_WioModbusConnectionPort_Object=MibTableColumn
wioModbusConnectionPort=_WioModbusConnectionPort_Object((1,3,6,1,4,1,13576,10,1,40,6,8,1,3),_WioModbusConnectionPort_Type())
wioModbusConnectionPort.setMaxAccess(_C)
if mibBuilder.loadTexts:wioModbusConnectionPort.setStatus(_A)
_WioEthernetIp_ObjectIdentity=ObjectIdentity
wioEthernetIp=_WioEthernetIp_ObjectIdentity((1,3,6,1,4,1,13576,10,1,40,7))
class _WioEthernetIpEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WioEthernetIpEnable_Type.__name__=_E
_WioEthernetIpEnable_Object=MibScalar
wioEthernetIpEnable=_WioEthernetIpEnable_Object((1,3,6,1,4,1,13576,10,1,40,7,1),_WioEthernetIpEnable_Type())
wioEthernetIpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wioEthernetIpEnable.setStatus(_A)
_WioEthernetIpVariablesInputCount_Type=Integer32
_WioEthernetIpVariablesInputCount_Object=MibScalar
wioEthernetIpVariablesInputCount=_WioEthernetIpVariablesInputCount_Object((1,3,6,1,4,1,13576,10,1,40,7,2),_WioEthernetIpVariablesInputCount_Type())
wioEthernetIpVariablesInputCount.setMaxAccess(_B)
if mibBuilder.loadTexts:wioEthernetIpVariablesInputCount.setStatus(_A)
_WioEthernetIpVariablesOutputCount_Type=Integer32
_WioEthernetIpVariablesOutputCount_Object=MibScalar
wioEthernetIpVariablesOutputCount=_WioEthernetIpVariablesOutputCount_Object((1,3,6,1,4,1,13576,10,1,40,7,3),_WioEthernetIpVariablesOutputCount_Type())
wioEthernetIpVariablesOutputCount.setMaxAccess(_B)
if mibBuilder.loadTexts:wioEthernetIpVariablesOutputCount.setStatus(_A)
_WioEthernetIpVariablesPlcInputCount_Type=Integer32
_WioEthernetIpVariablesPlcInputCount_Object=MibScalar
wioEthernetIpVariablesPlcInputCount=_WioEthernetIpVariablesPlcInputCount_Object((1,3,6,1,4,1,13576,10,1,40,7,4),_WioEthernetIpVariablesPlcInputCount_Type())
wioEthernetIpVariablesPlcInputCount.setMaxAccess(_B)
if mibBuilder.loadTexts:wioEthernetIpVariablesPlcInputCount.setStatus(_A)
_WioEthernetIpVariablesPlcInputOffset_Type=Integer32
_WioEthernetIpVariablesPlcInputOffset_Object=MibScalar
wioEthernetIpVariablesPlcInputOffset=_WioEthernetIpVariablesPlcInputOffset_Object((1,3,6,1,4,1,13576,10,1,40,7,5),_WioEthernetIpVariablesPlcInputOffset_Type())
wioEthernetIpVariablesPlcInputOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:wioEthernetIpVariablesPlcInputOffset.setStatus(_A)
_WioEthernetIpVariablesPlcOutputCount_Type=Integer32
_WioEthernetIpVariablesPlcOutputCount_Object=MibScalar
wioEthernetIpVariablesPlcOutputCount=_WioEthernetIpVariablesPlcOutputCount_Object((1,3,6,1,4,1,13576,10,1,40,7,6),_WioEthernetIpVariablesPlcOutputCount_Type())
wioEthernetIpVariablesPlcOutputCount.setMaxAccess(_B)
if mibBuilder.loadTexts:wioEthernetIpVariablesPlcOutputCount.setStatus(_A)
_WioEthernetIpVariablesPlcOutputOffset_Type=Integer32
_WioEthernetIpVariablesPlcOutputOffset_Object=MibScalar
wioEthernetIpVariablesPlcOutputOffset=_WioEthernetIpVariablesPlcOutputOffset_Object((1,3,6,1,4,1,13576,10,1,40,7,7),_WioEthernetIpVariablesPlcOutputOffset_Type())
wioEthernetIpVariablesPlcOutputOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:wioEthernetIpVariablesPlcOutputOffset.setStatus(_A)
_WioEthernetIpRunIdleHeaderOrginatorToTarget_Type=Integer32
_WioEthernetIpRunIdleHeaderOrginatorToTarget_Object=MibScalar
wioEthernetIpRunIdleHeaderOrginatorToTarget=_WioEthernetIpRunIdleHeaderOrginatorToTarget_Object((1,3,6,1,4,1,13576,10,1,40,7,8),_WioEthernetIpRunIdleHeaderOrginatorToTarget_Type())
wioEthernetIpRunIdleHeaderOrginatorToTarget.setMaxAccess(_B)
if mibBuilder.loadTexts:wioEthernetIpRunIdleHeaderOrginatorToTarget.setStatus(_A)
_WioEthernetIpRunIdleHeaderTargetToOrginator_Type=Integer32
_WioEthernetIpRunIdleHeaderTargetToOrginator_Object=MibScalar
wioEthernetIpRunIdleHeaderTargetToOrginator=_WioEthernetIpRunIdleHeaderTargetToOrginator_Object((1,3,6,1,4,1,13576,10,1,40,7,9),_WioEthernetIpRunIdleHeaderTargetToOrginator_Type())
wioEthernetIpRunIdleHeaderTargetToOrginator.setMaxAccess(_B)
if mibBuilder.loadTexts:wioEthernetIpRunIdleHeaderTargetToOrginator.setStatus(_A)
_WioProcessImage_ObjectIdentity=ObjectIdentity
wioProcessImage=_WioProcessImage_ObjectIdentity((1,3,6,1,4,1,13576,10,1,50))
_WioModulCount_Type=Integer32
_WioModulCount_Object=MibScalar
wioModulCount=_WioModulCount_Object((1,3,6,1,4,1,13576,10,1,50,1),_WioModulCount_Type())
wioModulCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wioModulCount.setStatus(_A)
_WioAnalogOutLength_Type=Integer32
_WioAnalogOutLength_Object=MibScalar
wioAnalogOutLength=_WioAnalogOutLength_Object((1,3,6,1,4,1,13576,10,1,50,2),_WioAnalogOutLength_Type())
wioAnalogOutLength.setMaxAccess(_C)
if mibBuilder.loadTexts:wioAnalogOutLength.setStatus(_A)
_WioAnalogInLength_Type=Integer32
_WioAnalogInLength_Object=MibScalar
wioAnalogInLength=_WioAnalogInLength_Object((1,3,6,1,4,1,13576,10,1,50,3),_WioAnalogInLength_Type())
wioAnalogInLength.setMaxAccess(_C)
if mibBuilder.loadTexts:wioAnalogInLength.setStatus(_A)
_WioDigitalOutLength_Type=Integer32
_WioDigitalOutLength_Object=MibScalar
wioDigitalOutLength=_WioDigitalOutLength_Object((1,3,6,1,4,1,13576,10,1,50,4),_WioDigitalOutLength_Type())
wioDigitalOutLength.setMaxAccess(_C)
if mibBuilder.loadTexts:wioDigitalOutLength.setStatus(_A)
_WioDigitalInLength_Type=Integer32
_WioDigitalInLength_Object=MibScalar
wioDigitalInLength=_WioDigitalInLength_Object((1,3,6,1,4,1,13576,10,1,50,5),_WioDigitalInLength_Type())
wioDigitalInLength.setMaxAccess(_C)
if mibBuilder.loadTexts:wioDigitalInLength.setStatus(_A)
_WioDigitalOutOffset_Type=Integer32
_WioDigitalOutOffset_Object=MibScalar
wioDigitalOutOffset=_WioDigitalOutOffset_Object((1,3,6,1,4,1,13576,10,1,50,6),_WioDigitalOutOffset_Type())
wioDigitalOutOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:wioDigitalOutOffset.setStatus(_A)
_WioDigitalInOffset_Type=Integer32
_WioDigitalInOffset_Object=MibScalar
wioDigitalInOffset=_WioDigitalInOffset_Object((1,3,6,1,4,1,13576,10,1,50,7),_WioDigitalInOffset_Type())
wioDigitalInOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:wioDigitalInOffset.setStatus(_A)
_WioModuleTable_Object=MibTable
wioModuleTable=_WioModuleTable_Object((1,3,6,1,4,1,13576,10,1,50,8))
if mibBuilder.loadTexts:wioModuleTable.setStatus(_A)
_WioModuleEntry_Object=MibTableRow
wioModuleEntry=_WioModuleEntry_Object((1,3,6,1,4,1,13576,10,1,50,8,1))
wioModuleEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:wioModuleEntry.setStatus(_A)
class _WioModuleNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,249))
_WioModuleNumber_Type.__name__=_E
_WioModuleNumber_Object=MibTableColumn
wioModuleNumber=_WioModuleNumber_Object((1,3,6,1,4,1,13576,10,1,50,8,1,1),_WioModuleNumber_Type())
wioModuleNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:wioModuleNumber.setStatus(_A)
class _WioModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_WioModuleName_Type.__name__=_D
_WioModuleName_Object=MibTableColumn
wioModuleName=_WioModuleName_Object((1,3,6,1,4,1,13576,10,1,50,8,1,2),_WioModuleName_Type())
wioModuleName.setMaxAccess(_C)
if mibBuilder.loadTexts:wioModuleName.setStatus(_A)
_WioModuleType_Type=Integer32
_WioModuleType_Object=MibTableColumn
wioModuleType=_WioModuleType_Object((1,3,6,1,4,1,13576,10,1,50,8,1,3),_WioModuleType_Type())
wioModuleType.setMaxAccess(_C)
if mibBuilder.loadTexts:wioModuleType.setStatus(_A)
_WioModuleCount_Type=Integer32
_WioModuleCount_Object=MibTableColumn
wioModuleCount=_WioModuleCount_Object((1,3,6,1,4,1,13576,10,1,50,8,1,4),_WioModuleCount_Type())
wioModuleCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wioModuleCount.setStatus(_A)
_WioModuleAlternativeFormat_Type=Integer32
_WioModuleAlternativeFormat_Object=MibTableColumn
wioModuleAlternativeFormat=_WioModuleAlternativeFormat_Object((1,3,6,1,4,1,13576,10,1,50,8,1,5),_WioModuleAlternativeFormat_Type())
wioModuleAlternativeFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:wioModuleAlternativeFormat.setStatus(_A)
_WioModuleAnalogOutLength_Type=Integer32
_WioModuleAnalogOutLength_Object=MibTableColumn
wioModuleAnalogOutLength=_WioModuleAnalogOutLength_Object((1,3,6,1,4,1,13576,10,1,50,8,1,6),_WioModuleAnalogOutLength_Type())
wioModuleAnalogOutLength.setMaxAccess(_C)
if mibBuilder.loadTexts:wioModuleAnalogOutLength.setStatus(_A)
_WioModuleAnalogInLength_Type=Integer32
_WioModuleAnalogInLength_Object=MibTableColumn
wioModuleAnalogInLength=_WioModuleAnalogInLength_Object((1,3,6,1,4,1,13576,10,1,50,8,1,7),_WioModuleAnalogInLength_Type())
wioModuleAnalogInLength.setMaxAccess(_C)
if mibBuilder.loadTexts:wioModuleAnalogInLength.setStatus(_A)
_WioModuleDigitalOutLength_Type=Integer32
_WioModuleDigitalOutLength_Object=MibTableColumn
wioModuleDigitalOutLength=_WioModuleDigitalOutLength_Object((1,3,6,1,4,1,13576,10,1,50,8,1,8),_WioModuleDigitalOutLength_Type())
wioModuleDigitalOutLength.setMaxAccess(_C)
if mibBuilder.loadTexts:wioModuleDigitalOutLength.setStatus(_A)
_WioModuleDigitalInLength_Type=Integer32
_WioModuleDigitalInLength_Object=MibTableColumn
wioModuleDigitalInLength=_WioModuleDigitalInLength_Object((1,3,6,1,4,1,13576,10,1,50,8,1,9),_WioModuleDigitalInLength_Type())
wioModuleDigitalInLength.setMaxAccess(_C)
if mibBuilder.loadTexts:wioModuleDigitalInLength.setStatus(_A)
_WioPlcData_ObjectIdentity=ObjectIdentity
wioPlcData=_WioPlcData_ObjectIdentity((1,3,6,1,4,1,13576,10,1,100))
_WioPlcDataTable_Object=MibTable
wioPlcDataTable=_WioPlcDataTable_Object((1,3,6,1,4,1,13576,10,1,100,1))
if mibBuilder.loadTexts:wioPlcDataTable.setStatus(_A)
_WioPlcDataEntry_Object=MibTableRow
wioPlcDataEntry=_WioPlcDataEntry_Object((1,3,6,1,4,1,13576,10,1,100,1,1))
wioPlcDataEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:wioPlcDataEntry.setStatus(_A)
class _WioPlcDataIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_WioPlcDataIndex_Type.__name__=_E
_WioPlcDataIndex_Object=MibTableColumn
wioPlcDataIndex=_WioPlcDataIndex_Object((1,3,6,1,4,1,13576,10,1,100,1,1,1),_WioPlcDataIndex_Type())
wioPlcDataIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wioPlcDataIndex.setStatus(_A)
_WioPlcDataReadArea_Type=Integer32
_WioPlcDataReadArea_Object=MibTableColumn
wioPlcDataReadArea=_WioPlcDataReadArea_Object((1,3,6,1,4,1,13576,10,1,100,1,1,2),_WioPlcDataReadArea_Type())
wioPlcDataReadArea.setMaxAccess(_B)
if mibBuilder.loadTexts:wioPlcDataReadArea.setStatus(_A)
_WioPlcDataWriteArea_Type=Integer32
_WioPlcDataWriteArea_Object=MibTableColumn
wioPlcDataWriteArea=_WioPlcDataWriteArea_Object((1,3,6,1,4,1,13576,10,1,100,1,1,3),_WioPlcDataWriteArea_Type())
wioPlcDataWriteArea.setMaxAccess(_C)
if mibBuilder.loadTexts:wioPlcDataWriteArea.setStatus(_A)
wioPlcKbusError=NotificationType((1,3,6,1,4,1,13576,0,1))
wioPlcKbusError.setObjects((_F,_R))
if mibBuilder.loadTexts:wioPlcKbusError.setStatus('')
wioPlcStart=NotificationType((1,3,6,1,4,1,13576,0,2))
wioPlcStart.setObjects((_F,_S))
if mibBuilder.loadTexts:wioPlcStart.setStatus('')
wioPlcStop=NotificationType((1,3,6,1,4,1,13576,0,3))
wioPlcStop.setObjects((_F,_T))
if mibBuilder.loadTexts:wioPlcStop.setStatus('')
wioPlcReset=NotificationType((1,3,6,1,4,1,13576,0,4))
wioPlcReset.setObjects((_F,_U))
if mibBuilder.loadTexts:wioPlcReset.setStatus('')
wioPlcSoftwareWatchdog=NotificationType((1,3,6,1,4,1,13576,0,5))
wioPlcSoftwareWatchdog.setObjects((_F,_V))
if mibBuilder.loadTexts:wioPlcSoftwareWatchdog.setStatus('')
wioPlcDivideByZero=NotificationType((1,3,6,1,4,1,13576,0,6))
wioPlcDivideByZero.setObjects((_F,_W))
if mibBuilder.loadTexts:wioPlcDivideByZero.setStatus('')
wioPlcOnlineChange=NotificationType((1,3,6,1,4,1,13576,0,7))
wioPlcOnlineChange.setObjects((_F,_X))
if mibBuilder.loadTexts:wioPlcOnlineChange.setStatus('')
wioPlcDownload=NotificationType((1,3,6,1,4,1,13576,0,8))
wioPlcDownload.setObjects((_F,_Y))
if mibBuilder.loadTexts:wioPlcDownload.setStatus('')
wioPlcLogin=NotificationType((1,3,6,1,4,1,13576,0,9))
wioPlcLogin.setObjects((_F,_Z))
if mibBuilder.loadTexts:wioPlcLogin.setStatus('')
wioPlcLogout=NotificationType((1,3,6,1,4,1,13576,0,10))
wioPlcLogout.setObjects((_F,_a))
if mibBuilder.loadTexts:wioPlcLogout.setStatus('')
mibBuilder.exportSymbols(_F,**{_D:DisplayString,'wago':wago,'wioPlcKbusError':wioPlcKbusError,'wioPlcStart':wioPlcStart,'wioPlcStop':wioPlcStop,'wioPlcReset':wioPlcReset,'wioPlcSoftwareWatchdog':wioPlcSoftwareWatchdog,'wioPlcDivideByZero':wioPlcDivideByZero,'wioPlcOnlineChange':wioPlcOnlineChange,'wioPlcDownload':wioPlcDownload,'wioPlcLogin':wioPlcLogin,'wioPlcLogout':wioPlcLogout,'wagoCompany':wagoCompany,'wagoName':wagoName,'wagoDescrition':wagoDescrition,'wagoURL':wagoURL,'wagoIOProducts':wagoIOProducts,'wioCommon':wioCommon,'wioArticleName':wioArticleName,'wioArticleDescription':wioArticleDescription,'wioSerialNumber':wioSerialNumber,'wioMacAddress':wioMacAddress,'wioURLDatasheet':wioURLDatasheet,'wioURLManual':wioURLManual,'wioDeviceClass':wioDeviceClass,'wioDeviceGroup':wioDeviceGroup,'wioVersion':wioVersion,'wioFirmwareIndex':wioFirmwareIndex,'wioHardwareIndex':wioHardwareIndex,'wioFwlIndex':wioFwlIndex,'wioFirmwareVersion':wioFirmwareVersion,'wioRealTimeClock':wioRealTimeClock,'wioRtcDateTime':wioRtcDateTime,'wioRtcTime':wioRtcTime,'wioTimezone':wioTimezone,'wioRtcHourMode':wioRtcHourMode,'wioRtcBatteryStatus':wioRtcBatteryStatus,'wioRtcDayLightSaving':wioRtcDayLightSaving,'wioEthernet':wioEthernet,'wioEthernetMode':wioEthernetMode,'wioIp':wioIp,'wioSubnetMask':wioSubnetMask,'wioGateway':wioGateway,'wioHostname':wioHostname,'wioDomainName':wioDomainName,'wioDnsServer1':wioDnsServer1,'wioDnsServer2':wioDnsServer2,'wioActualStatus':wioActualStatus,'wioErrorGroup':wioErrorGroup,'wioErrorCode':wioErrorCode,'wioErrorArgument':wioErrorArgument,'wioErrorDescription':wioErrorDescription,'wioPlcBrowser':wioPlcBrowser,'wioProjectId':wioProjectId,'wioProjectDate':wioProjectDate,'wioProjectName':wioProjectName,'wioProjectTitle':wioProjectTitle,'wioProjectVersion':wioProjectVersion,'wioProjectAuthor':wioProjectAuthor,'wioProjectDescription':wioProjectDescription,'wioNumberOfIecTasks':wioNumberOfIecTasks,'wioIecTaskTable':wioIecTaskTable,'wioIecTaskEntry':wioIecTaskEntry,_J:wioIecTaskId,'wioIecTaskName':wioIecTaskName,'wioIecTaskStatus':wioIecTaskStatus,'wioIecTaskMode':wioIecTaskMode,'wioIecTaskPriority':wioIecTaskPriority,'wioIecTaskInterval':wioIecTaskInterval,'wioIecTaskEvent':wioIecTaskEvent,'wioIecTaskCycleCount':wioIecTaskCycleCount,'wioIecTaskCycleTime':wioIecTaskCycleTime,'wioIecTaskCycleTimeMin':wioIecTaskCycleTimeMin,'wioIecTaskCycleTimeMax':wioIecTaskCycleTimeMax,'wioIecTaskCycleTimeAvg':wioIecTaskCycleTimeAvg,'wioEthernetProtocols':wioEthernetProtocols,'wioHttp':wioHttp,'wioHttpEnable':wioHttpEnable,'wioHttpAuthenticationEnable':wioHttpAuthenticationEnable,'wioHttpPort':wioHttpPort,'wioFtp':wioFtp,'wioFtpEnable':wioFtpEnable,'wioSntp':wioSntp,'wioSntpEnable':wioSntpEnable,'wioSntpServerAddress':wioSntpServerAddress,'wioSntpClientIntervall':wioSntpClientIntervall,'wioSntpClientTimeout':wioSntpClientTimeout,'wioSntpClientDayLightSaving':wioSntpClientDayLightSaving,'wioSnmp':wioSnmp,'wioSnmpEnable':wioSnmpEnable,'wioSnmpV1V2c':wioSnmpV1V2c,'wioSnmpEnableV1V2':wioSnmpEnableV1V2,'wioLocalCommunity':wioLocalCommunity,'wioTrapReceiverV1V2Table':wioTrapReceiverV1V2Table,'wioTrapReceiverV1V2Entry':wioTrapReceiverV1V2Entry,_K:wioTrapReceiverIndex,'wioTrapReceiverIpAddress':wioTrapReceiverIpAddress,'wioTrapReceiverCommunityName':wioTrapReceiverCommunityName,'wioTrapReceiverTrapVersion':wioTrapReceiverTrapVersion,'wioSnmpV3Usm':wioSnmpV3Usm,'wioSnmp1UserEnable':wioSnmp1UserEnable,'wioSnmp1AuthenticationTyp':wioSnmp1AuthenticationTyp,'wioSnmp1AuthenticationName':wioSnmp1AuthenticationName,'wioSnmp1AuthenticationKey':wioSnmp1AuthenticationKey,'wioSnmp1PrivacyEnable':wioSnmp1PrivacyEnable,'wioSnmp1PrivacyKey':wioSnmp1PrivacyKey,'wioSnmp1NotificationEnable':wioSnmp1NotificationEnable,'wioSnmp1NotificationReceiverIP':wioSnmp1NotificationReceiverIP,'wioSnmp2UserEnable':wioSnmp2UserEnable,'wioSnmp2AuthenticationTyp':wioSnmp2AuthenticationTyp,'wioSnmp2AuthenticationName':wioSnmp2AuthenticationName,'wioSnmp2AuthenticationKey':wioSnmp2AuthenticationKey,'wioSnmp2PrivacyEnable':wioSnmp2PrivacyEnable,'wioSnmp2PrivacyKey':wioSnmp2PrivacyKey,'wioSnmp2NotificationEnable':wioSnmp2NotificationEnable,'wioSnmp2NotificationReceiverIP':wioSnmp2NotificationReceiverIP,'wioTrapMessages':wioTrapMessages,_R:wioTrapKbusError,_S:wioTrapPlcStart,_T:wioTrapPlcStop,_U:wioTrapPlcReset,_V:wioTrapPlcSoftwareWatchdog,_W:wioTrapPlcDivideByZero,_X:wioTrapPlcOnlineChange,_Y:wioTrapPlcDownload,_Z:wioTrapPlcLogin,_a:wioTrapPlcLogout,'wioUserTrapMessages':wioUserTrapMessages,'wioUserTrapMsg1':wioUserTrapMsg1,'wioUserTrapMsg2':wioUserTrapMsg2,'wioUserTrapMsg3':wioUserTrapMsg3,'wioUserTrapMsg4':wioUserTrapMsg4,'wioUserTrapMsg5':wioUserTrapMsg5,'wioUserTrapMsg6':wioUserTrapMsg6,'wioUserTrapMsg7':wioUserTrapMsg7,'wioUserTrapMsg8':wioUserTrapMsg8,'wioUserTrapMsg9':wioUserTrapMsg9,'wioUserTrapMsg10':wioUserTrapMsg10,'wioCoDeSys':wioCoDeSys,'wioCoDeSysEnable':wioCoDeSysEnable,'wioModbus':wioModbus,'wioModbusTcpEnable':wioModbusTcpEnable,'wioModbusUdbEnable':wioModbusUdbEnable,'wioMaxConnections':wioMaxConnections,'wioConnectionTimeout':wioConnectionTimeout,'wioModbusWatchdogMode':wioModbusWatchdogMode,'wioModbusWatchdogTime':wioModbusWatchdogTime,'wioFreeModbusSockets':wioFreeModbusSockets,'wioModbusConnectionTable':wioModbusConnectionTable,'wioModbusConnectionEntry':wioModbusConnectionEntry,_O:wioModbusConnectionIndex,'wioModbusConnectionIp':wioModbusConnectionIp,'wioModbusConnectionPort':wioModbusConnectionPort,'wioEthernetIp':wioEthernetIp,'wioEthernetIpEnable':wioEthernetIpEnable,'wioEthernetIpVariablesInputCount':wioEthernetIpVariablesInputCount,'wioEthernetIpVariablesOutputCount':wioEthernetIpVariablesOutputCount,'wioEthernetIpVariablesPlcInputCount':wioEthernetIpVariablesPlcInputCount,'wioEthernetIpVariablesPlcInputOffset':wioEthernetIpVariablesPlcInputOffset,'wioEthernetIpVariablesPlcOutputCount':wioEthernetIpVariablesPlcOutputCount,'wioEthernetIpVariablesPlcOutputOffset':wioEthernetIpVariablesPlcOutputOffset,'wioEthernetIpRunIdleHeaderOrginatorToTarget':wioEthernetIpRunIdleHeaderOrginatorToTarget,'wioEthernetIpRunIdleHeaderTargetToOrginator':wioEthernetIpRunIdleHeaderTargetToOrginator,'wioProcessImage':wioProcessImage,'wioModulCount':wioModulCount,'wioAnalogOutLength':wioAnalogOutLength,'wioAnalogInLength':wioAnalogInLength,'wioDigitalOutLength':wioDigitalOutLength,'wioDigitalInLength':wioDigitalInLength,'wioDigitalOutOffset':wioDigitalOutOffset,'wioDigitalInOffset':wioDigitalInOffset,'wioModuleTable':wioModuleTable,'wioModuleEntry':wioModuleEntry,_P:wioModuleNumber,'wioModuleName':wioModuleName,'wioModuleType':wioModuleType,'wioModuleCount':wioModuleCount,'wioModuleAlternativeFormat':wioModuleAlternativeFormat,'wioModuleAnalogOutLength':wioModuleAnalogOutLength,'wioModuleAnalogInLength':wioModuleAnalogInLength,'wioModuleDigitalOutLength':wioModuleDigitalOutLength,'wioModuleDigitalInLength':wioModuleDigitalInLength,'wioPlcData':wioPlcData,'wioPlcDataTable':wioPlcDataTable,'wioPlcDataEntry':wioPlcDataEntry,_Q:wioPlcDataIndex,'wioPlcDataReadArea':wioPlcDataReadArea,'wioPlcDataWriteArea':wioPlcDataWriteArea})