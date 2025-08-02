_H='ioIndex'
_G='hssIndex'
_F='mIndex'
_E='TELTONIKA-MIB'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Opaque,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','Opaque','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention','TruthValue')
teltonika=ModuleIdentity((1,3,6,1,4,1,48690))
if mibBuilder.loadTexts:teltonika.setRevisions(('2019-05-15 00:00',))
_Device_ObjectIdentity=ObjectIdentity
device=_Device_ObjectIdentity((1,3,6,1,4,1,48690,1))
class _Serial_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Serial_Type.__name__=_C
_Serial_Object=MibScalar
serial=_Serial_Object((1,3,6,1,4,1,48690,1,1),_Serial_Type())
serial.setMaxAccess(_B)
if mibBuilder.loadTexts:serial.setStatus(_A)
class _RouterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RouterName_Type.__name__=_C
_RouterName_Object=MibScalar
routerName=_RouterName_Object((1,3,6,1,4,1,48690,1,2),_RouterName_Type())
routerName.setMaxAccess(_B)
if mibBuilder.loadTexts:routerName.setStatus(_A)
class _ProductCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ProductCode_Type.__name__=_C
_ProductCode_Object=MibScalar
productCode=_ProductCode_Object((1,3,6,1,4,1,48690,1,3),_ProductCode_Type())
productCode.setMaxAccess(_B)
if mibBuilder.loadTexts:productCode.setStatus(_A)
class _BatchNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BatchNumber_Type.__name__=_C
_BatchNumber_Object=MibScalar
batchNumber=_BatchNumber_Object((1,3,6,1,4,1,48690,1,4),_BatchNumber_Type())
batchNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:batchNumber.setStatus(_A)
class _HardwareRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HardwareRevision_Type.__name__=_C
_HardwareRevision_Object=MibScalar
hardwareRevision=_HardwareRevision_Object((1,3,6,1,4,1,48690,1,5),_HardwareRevision_Type())
hardwareRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:hardwareRevision.setStatus(_A)
class _FwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FwVersion_Type.__name__=_C
_FwVersion_Object=MibScalar
fwVersion=_FwVersion_Object((1,3,6,1,4,1,48690,1,6),_FwVersion_Type())
fwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fwVersion.setStatus(_A)
_Mobile_ObjectIdentity=ObjectIdentity
mobile=_Mobile_ObjectIdentity((1,3,6,1,4,1,48690,2))
_ModemNum_Type=Integer32
_ModemNum_Object=MibScalar
modemNum=_ModemNum_Object((1,3,6,1,4,1,48690,2,1),_ModemNum_Type())
modemNum.setMaxAccess(_B)
if mibBuilder.loadTexts:modemNum.setStatus(_A)
_ModemTable_Object=MibTable
modemTable=_ModemTable_Object((1,3,6,1,4,1,48690,2,2))
if mibBuilder.loadTexts:modemTable.setStatus(_A)
_ModemEntry_Object=MibTableRow
modemEntry=_ModemEntry_Object((1,3,6,1,4,1,48690,2,2,1))
modemEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:modemEntry.setStatus(_A)
class _MIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MIndex_Type.__name__=_D
_MIndex_Object=MibTableColumn
mIndex=_MIndex_Object((1,3,6,1,4,1,48690,2,2,1,1),_MIndex_Type())
mIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mIndex.setStatus(_A)
class _MDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MDescr_Type.__name__=_C
_MDescr_Object=MibTableColumn
mDescr=_MDescr_Object((1,3,6,1,4,1,48690,2,2,1,2),_MDescr_Type())
mDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:mDescr.setStatus(_A)
class _MImei_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MImei_Type.__name__=_C
_MImei_Object=MibTableColumn
mImei=_MImei_Object((1,3,6,1,4,1,48690,2,2,1,3),_MImei_Type())
mImei.setMaxAccess(_B)
if mibBuilder.loadTexts:mImei.setStatus(_A)
class _MModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MModel_Type.__name__=_C
_MModel_Object=MibTableColumn
mModel=_MModel_Object((1,3,6,1,4,1,48690,2,2,1,4),_MModel_Type())
mModel.setMaxAccess(_B)
if mibBuilder.loadTexts:mModel.setStatus(_A)
class _MManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MManufacturer_Type.__name__=_C
_MManufacturer_Object=MibTableColumn
mManufacturer=_MManufacturer_Object((1,3,6,1,4,1,48690,2,2,1,5),_MManufacturer_Type())
mManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:mManufacturer.setStatus(_A)
class _MRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MRevision_Type.__name__=_C
_MRevision_Object=MibTableColumn
mRevision=_MRevision_Object((1,3,6,1,4,1,48690,2,2,1,6),_MRevision_Type())
mRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:mRevision.setStatus(_A)
class _MSerial_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MSerial_Type.__name__=_C
_MSerial_Object=MibTableColumn
mSerial=_MSerial_Object((1,3,6,1,4,1,48690,2,2,1,7),_MSerial_Type())
mSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:mSerial.setStatus(_A)
class _MIMSI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MIMSI_Type.__name__=_C
_MIMSI_Object=MibTableColumn
mIMSI=_MIMSI_Object((1,3,6,1,4,1,48690,2,2,1,8),_MIMSI_Type())
mIMSI.setMaxAccess(_B)
if mibBuilder.loadTexts:mIMSI.setStatus(_A)
class _MSimState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MSimState_Type.__name__=_C
_MSimState_Object=MibTableColumn
mSimState=_MSimState_Object((1,3,6,1,4,1,48690,2,2,1,9),_MSimState_Type())
mSimState.setMaxAccess(_B)
if mibBuilder.loadTexts:mSimState.setStatus(_A)
class _MPinState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MPinState_Type.__name__=_C
_MPinState_Object=MibTableColumn
mPinState=_MPinState_Object((1,3,6,1,4,1,48690,2,2,1,10),_MPinState_Type())
mPinState.setMaxAccess(_B)
if mibBuilder.loadTexts:mPinState.setStatus(_A)
class _MNetState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MNetState_Type.__name__=_C
_MNetState_Object=MibTableColumn
mNetState=_MNetState_Object((1,3,6,1,4,1,48690,2,2,1,11),_MNetState_Type())
mNetState.setMaxAccess(_B)
if mibBuilder.loadTexts:mNetState.setStatus(_A)
_MSignal_Type=Integer32
_MSignal_Object=MibTableColumn
mSignal=_MSignal_Object((1,3,6,1,4,1,48690,2,2,1,12),_MSignal_Type())
mSignal.setMaxAccess(_B)
if mibBuilder.loadTexts:mSignal.setStatus(_A)
class _MOperator_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MOperator_Type.__name__=_C
_MOperator_Object=MibTableColumn
mOperator=_MOperator_Object((1,3,6,1,4,1,48690,2,2,1,13),_MOperator_Type())
mOperator.setMaxAccess(_B)
if mibBuilder.loadTexts:mOperator.setStatus(_A)
class _MOperatorNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MOperatorNumber_Type.__name__=_C
_MOperatorNumber_Object=MibTableColumn
mOperatorNumber=_MOperatorNumber_Object((1,3,6,1,4,1,48690,2,2,1,14),_MOperatorNumber_Type())
mOperatorNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:mOperatorNumber.setStatus(_A)
class _MConnectionState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MConnectionState_Type.__name__=_C
_MConnectionState_Object=MibTableColumn
mConnectionState=_MConnectionState_Object((1,3,6,1,4,1,48690,2,2,1,15),_MConnectionState_Type())
mConnectionState.setMaxAccess(_B)
if mibBuilder.loadTexts:mConnectionState.setStatus(_A)
class _MConnectionType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MConnectionType_Type.__name__=_C
_MConnectionType_Object=MibTableColumn
mConnectionType=_MConnectionType_Object((1,3,6,1,4,1,48690,2,2,1,16),_MConnectionType_Type())
mConnectionType.setMaxAccess(_B)
if mibBuilder.loadTexts:mConnectionType.setStatus(_A)
_MTemperature_Type=Integer32
_MTemperature_Object=MibTableColumn
mTemperature=_MTemperature_Object((1,3,6,1,4,1,48690,2,2,1,17),_MTemperature_Type())
mTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:mTemperature.setStatus(_A)
class _MCellID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MCellID_Type.__name__=_C
_MCellID_Object=MibTableColumn
mCellID=_MCellID_Object((1,3,6,1,4,1,48690,2,2,1,18),_MCellID_Type())
mCellID.setMaxAccess(_B)
if mibBuilder.loadTexts:mCellID.setStatus(_A)
class _MSINR_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MSINR_Type.__name__=_C
_MSINR_Object=MibTableColumn
mSINR=_MSINR_Object((1,3,6,1,4,1,48690,2,2,1,19),_MSINR_Type())
mSINR.setMaxAccess(_B)
if mibBuilder.loadTexts:mSINR.setStatus(_A)
class _MRSRP_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MRSRP_Type.__name__=_C
_MRSRP_Object=MibTableColumn
mRSRP=_MRSRP_Object((1,3,6,1,4,1,48690,2,2,1,20),_MRSRP_Type())
mRSRP.setMaxAccess(_B)
if mibBuilder.loadTexts:mRSRP.setStatus(_A)
class _MRSRQ_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MRSRQ_Type.__name__=_C
_MRSRQ_Object=MibTableColumn
mRSRQ=_MRSRQ_Object((1,3,6,1,4,1,48690,2,2,1,21),_MRSRQ_Type())
mRSRQ.setMaxAccess(_B)
if mibBuilder.loadTexts:mRSRQ.setStatus(_A)
_MSent_Type=Counter64
_MSent_Object=MibTableColumn
mSent=_MSent_Object((1,3,6,1,4,1,48690,2,2,1,22),_MSent_Type())
mSent.setMaxAccess(_B)
if mibBuilder.loadTexts:mSent.setStatus(_A)
_MReceived_Type=Counter64
_MReceived_Object=MibTableColumn
mReceived=_MReceived_Object((1,3,6,1,4,1,48690,2,2,1,23),_MReceived_Type())
mReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:mReceived.setStatus(_A)
class _MIP_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MIP_Type.__name__=_C
_MIP_Object=MibTableColumn
mIP=_MIP_Object((1,3,6,1,4,1,48690,2,2,1,24),_MIP_Type())
mIP.setMaxAccess(_B)
if mibBuilder.loadTexts:mIP.setStatus(_A)
_MSentToday_Type=Counter64
_MSentToday_Object=MibTableColumn
mSentToday=_MSentToday_Object((1,3,6,1,4,1,48690,2,2,1,25),_MSentToday_Type())
mSentToday.setMaxAccess(_B)
if mibBuilder.loadTexts:mSentToday.setStatus(_A)
_MReceivedToday_Type=Counter64
_MReceivedToday_Object=MibTableColumn
mReceivedToday=_MReceivedToday_Object((1,3,6,1,4,1,48690,2,2,1,26),_MReceivedToday_Type())
mReceivedToday.setMaxAccess(_B)
if mibBuilder.loadTexts:mReceivedToday.setStatus(_A)
_Gps_ObjectIdentity=ObjectIdentity
gps=_Gps_ObjectIdentity((1,3,6,1,4,1,48690,3))
class _Latitude_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Latitude_Type.__name__=_C
_Latitude_Object=MibScalar
latitude=_Latitude_Object((1,3,6,1,4,1,48690,3,1),_Latitude_Type())
latitude.setMaxAccess(_B)
if mibBuilder.loadTexts:latitude.setStatus(_A)
class _Longtitude_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Longtitude_Type.__name__=_C
_Longtitude_Object=MibScalar
longtitude=_Longtitude_Object((1,3,6,1,4,1,48690,3,2),_Longtitude_Type())
longtitude.setMaxAccess(_B)
if mibBuilder.loadTexts:longtitude.setStatus(_A)
class _Accuracy_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Accuracy_Type.__name__=_C
_Accuracy_Object=MibScalar
accuracy=_Accuracy_Object((1,3,6,1,4,1,48690,3,3),_Accuracy_Type())
accuracy.setMaxAccess(_B)
if mibBuilder.loadTexts:accuracy.setStatus(_A)
class _Datetime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Datetime_Type.__name__=_C
_Datetime_Object=MibScalar
datetime=_Datetime_Object((1,3,6,1,4,1,48690,3,4),_Datetime_Type())
datetime.setMaxAccess(_B)
if mibBuilder.loadTexts:datetime.setStatus(_A)
_NumSatellites_Type=Integer32
_NumSatellites_Object=MibScalar
numSatellites=_NumSatellites_Object((1,3,6,1,4,1,48690,3,5),_NumSatellites_Type())
numSatellites.setMaxAccess(_B)
if mibBuilder.loadTexts:numSatellites.setStatus(_A)
_Notifications_ObjectIdentity=ObjectIdentity
notifications=_Notifications_ObjectIdentity((1,3,6,1,4,1,48690,4))
_MobileNotifications_ObjectIdentity=ObjectIdentity
mobileNotifications=_MobileNotifications_ObjectIdentity((1,3,6,1,4,1,48690,4,1))
_IoNotifications_ObjectIdentity=ObjectIdentity
ioNotifications=_IoNotifications_ObjectIdentity((1,3,6,1,4,1,48690,4,2))
_Hotspot_ObjectIdentity=ObjectIdentity
hotspot=_Hotspot_ObjectIdentity((1,3,6,1,4,1,48690,5))
class _HsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_HsState_Type.__name__=_D
_HsState_Object=MibScalar
hsState=_HsState_Object((1,3,6,1,4,1,48690,5,1),_HsState_Type())
hsState.setMaxAccess(_B)
if mibBuilder.loadTexts:hsState.setStatus(_A)
_HsIP_Type=IpAddress
_HsIP_Object=MibScalar
hsIP=_HsIP_Object((1,3,6,1,4,1,48690,5,2),_HsIP_Type())
hsIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hsIP.setStatus(_A)
class _HsNet_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HsNet_Type.__name__=_C
_HsNet_Object=MibScalar
hsNet=_HsNet_Object((1,3,6,1,4,1,48690,5,3),_HsNet_Type())
hsNet.setMaxAccess(_B)
if mibBuilder.loadTexts:hsNet.setStatus(_A)
class _HsAuth_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HsAuth_Type.__name__=_C
_HsAuth_Object=MibScalar
hsAuth=_HsAuth_Object((1,3,6,1,4,1,48690,5,4),_HsAuth_Type())
hsAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:hsAuth.setStatus(_A)
_HsSessionCount_Type=Counter64
_HsSessionCount_Object=MibScalar
hsSessionCount=_HsSessionCount_Object((1,3,6,1,4,1,48690,5,5),_HsSessionCount_Type())
hsSessionCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hsSessionCount.setStatus(_A)
_HsSessionTable_Object=MibTable
hsSessionTable=_HsSessionTable_Object((1,3,6,1,4,1,48690,5,6))
if mibBuilder.loadTexts:hsSessionTable.setStatus(_A)
_HsSessionEntry_Object=MibTableRow
hsSessionEntry=_HsSessionEntry_Object((1,3,6,1,4,1,48690,5,6,1))
hsSessionEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:hsSessionEntry.setStatus(_A)
_HssIndex_Type=Integer32
_HssIndex_Object=MibTableColumn
hssIndex=_HssIndex_Object((1,3,6,1,4,1,48690,5,6,1,1),_HssIndex_Type())
hssIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hssIndex.setStatus(_A)
_HssMAC_Type=PhysAddress
_HssMAC_Object=MibTableColumn
hssMAC=_HssMAC_Object((1,3,6,1,4,1,48690,5,6,1,2),_HssMAC_Type())
hssMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:hssMAC.setStatus(_A)
_HssIP_Type=IpAddress
_HssIP_Object=MibTableColumn
hssIP=_HssIP_Object((1,3,6,1,4,1,48690,5,6,1,3),_HssIP_Type())
hssIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hssIP.setStatus(_A)
_HssID_Type=DisplayString
_HssID_Object=MibTableColumn
hssID=_HssID_Object((1,3,6,1,4,1,48690,5,6,1,4),_HssID_Type())
hssID.setMaxAccess(_B)
if mibBuilder.loadTexts:hssID.setStatus(_A)
class _HssUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HssUsername_Type.__name__=_C
_HssUsername_Object=MibTableColumn
hssUsername=_HssUsername_Object((1,3,6,1,4,1,48690,5,6,1,5),_HssUsername_Type())
hssUsername.setMaxAccess(_B)
if mibBuilder.loadTexts:hssUsername.setStatus(_A)
class _HssState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notAuthorized',0),('authorized',1)))
_HssState_Type.__name__=_D
_HssState_Object=MibTableColumn
hssState=_HssState_Object((1,3,6,1,4,1,48690,5,6,1,6),_HssState_Type())
hssState.setMaxAccess(_B)
if mibBuilder.loadTexts:hssState.setStatus(_A)
_HssDwLimit_Type=Counter64
_HssDwLimit_Object=MibTableColumn
hssDwLimit=_HssDwLimit_Object((1,3,6,1,4,1,48690,5,6,1,7),_HssDwLimit_Type())
hssDwLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hssDwLimit.setStatus(_A)
_HssUpLimit_Type=Counter64
_HssUpLimit_Object=MibTableColumn
hssUpLimit=_HssUpLimit_Object((1,3,6,1,4,1,48690,5,6,1,8),_HssUpLimit_Type())
hssUpLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hssUpLimit.setStatus(_A)
_HssTimeLimit_Type=Counter64
_HssTimeLimit_Object=MibTableColumn
hssTimeLimit=_HssTimeLimit_Object((1,3,6,1,4,1,48690,5,6,1,9),_HssTimeLimit_Type())
hssTimeLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hssTimeLimit.setStatus(_A)
_HssIdleTimeout_Type=Integer32
_HssIdleTimeout_Object=MibTableColumn
hssIdleTimeout=_HssIdleTimeout_Object((1,3,6,1,4,1,48690,5,6,1,10),_HssIdleTimeout_Type())
hssIdleTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hssIdleTimeout.setStatus(_A)
_HssDwBandwidth_Type=Counter64
_HssDwBandwidth_Object=MibTableColumn
hssDwBandwidth=_HssDwBandwidth_Object((1,3,6,1,4,1,48690,5,6,1,11),_HssDwBandwidth_Type())
hssDwBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:hssDwBandwidth.setStatus(_A)
_HssUpBandwidth_Type=Counter64
_HssUpBandwidth_Object=MibTableColumn
hssUpBandwidth=_HssUpBandwidth_Object((1,3,6,1,4,1,48690,5,6,1,12),_HssUpBandwidth_Type())
hssUpBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:hssUpBandwidth.setStatus(_A)
_HssURL_Type=DisplayString
_HssURL_Object=MibTableColumn
hssURL=_HssURL_Object((1,3,6,1,4,1,48690,5,6,1,13),_HssURL_Type())
hssURL.setMaxAccess(_B)
if mibBuilder.loadTexts:hssURL.setStatus(_A)
_Io_ObjectIdentity=ObjectIdentity
io=_Io_ObjectIdentity((1,3,6,1,4,1,48690,6))
_IoCount_Type=Integer32
_IoCount_Object=MibScalar
ioCount=_IoCount_Object((1,3,6,1,4,1,48690,6,1),_IoCount_Type())
ioCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ioCount.setStatus(_A)
_IoTable_Object=MibTable
ioTable=_IoTable_Object((1,3,6,1,4,1,48690,6,2))
if mibBuilder.loadTexts:ioTable.setStatus(_A)
_IoEntry_Object=MibTableRow
ioEntry=_IoEntry_Object((1,3,6,1,4,1,48690,6,2,1))
ioEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:ioEntry.setStatus(_A)
_IoIndex_Type=Integer32
_IoIndex_Object=MibTableColumn
ioIndex=_IoIndex_Object((1,3,6,1,4,1,48690,6,2,1,1),_IoIndex_Type())
ioIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ioIndex.setStatus(_A)
_IoSystemName_Type=DisplayString
_IoSystemName_Object=MibTableColumn
ioSystemName=_IoSystemName_Object((1,3,6,1,4,1,48690,6,2,1,2),_IoSystemName_Type())
ioSystemName.setMaxAccess(_B)
if mibBuilder.loadTexts:ioSystemName.setStatus(_A)
_IoName_Type=DisplayString
_IoName_Object=MibTableColumn
ioName=_IoName_Object((1,3,6,1,4,1,48690,6,2,1,3),_IoName_Type())
ioName.setMaxAccess(_B)
if mibBuilder.loadTexts:ioName.setStatus(_A)
_IoType_Type=DisplayString
_IoType_Object=MibTableColumn
ioType=_IoType_Object((1,3,6,1,4,1,48690,6,2,1,4),_IoType_Type())
ioType.setMaxAccess(_B)
if mibBuilder.loadTexts:ioType.setStatus(_A)
_IoBidirectional_Type=Integer32
_IoBidirectional_Object=MibTableColumn
ioBidirectional=_IoBidirectional_Object((1,3,6,1,4,1,48690,6,2,1,5),_IoBidirectional_Type())
ioBidirectional.setMaxAccess(_B)
if mibBuilder.loadTexts:ioBidirectional.setStatus(_A)
_IoState_Type=DisplayString
_IoState_Object=MibTableColumn
ioState=_IoState_Object((1,3,6,1,4,1,48690,6,2,1,6),_IoState_Type())
ioState.setMaxAccess(_B)
if mibBuilder.loadTexts:ioState.setStatus(_A)
_IoInput_Type=Integer32
_IoInput_Object=MibTableColumn
ioInput=_IoInput_Object((1,3,6,1,4,1,48690,6,2,1,7),_IoInput_Type())
ioInput.setMaxAccess(_B)
if mibBuilder.loadTexts:ioInput.setStatus(_A)
_IoInverted_Type=Integer32
_IoInverted_Object=MibTableColumn
ioInverted=_IoInverted_Object((1,3,6,1,4,1,48690,6,2,1,8),_IoInverted_Type())
ioInverted.setMaxAccess(_B)
if mibBuilder.loadTexts:ioInverted.setStatus(_A)
_IoCurrent_Type=DisplayString
_IoCurrent_Object=MibTableColumn
ioCurrent=_IoCurrent_Object((1,3,6,1,4,1,48690,6,2,1,9),_IoCurrent_Type())
ioCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:ioCurrent.setStatus(_A)
_IoPercentage_Type=DisplayString
_IoPercentage_Object=MibTableColumn
ioPercentage=_IoPercentage_Object((1,3,6,1,4,1,48690,6,2,1,10),_IoPercentage_Type())
ioPercentage.setMaxAccess(_B)
if mibBuilder.loadTexts:ioPercentage.setStatus(_A)
signalChangeNotification=NotificationType((1,3,6,1,4,1,48690,4,1,1))
if mibBuilder.loadTexts:signalChangeNotification.setStatus(_A)
connectionTypeNotification=NotificationType((1,3,6,1,4,1,48690,4,1,2))
if mibBuilder.loadTexts:connectionTypeNotification.setStatus(_A)
digitalInputNotification=NotificationType((1,3,6,1,4,1,48690,4,2,1))
if mibBuilder.loadTexts:digitalInputNotification.setStatus(_A)
digitalOutputNotification=NotificationType((1,3,6,1,4,1,48690,4,2,2))
if mibBuilder.loadTexts:digitalOutputNotification.setStatus(_A)
relay0Notification=NotificationType((1,3,6,1,4,1,48690,4,2,8))
if mibBuilder.loadTexts:relay0Notification.setStatus(_A)
digitalInput2Notification=NotificationType((1,3,6,1,4,1,48690,4,2,12))
if mibBuilder.loadTexts:digitalInput2Notification.setStatus(_A)
digitalIioNotification=NotificationType((1,3,6,1,4,1,48690,4,2,13))
if mibBuilder.loadTexts:digitalIioNotification.setStatus(_A)
digitalOutput2Notification=NotificationType((1,3,6,1,4,1,48690,4,2,14))
if mibBuilder.loadTexts:digitalOutput2Notification.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'teltonika':teltonika,'device':device,'serial':serial,'routerName':routerName,'productCode':productCode,'batchNumber':batchNumber,'hardwareRevision':hardwareRevision,'fwVersion':fwVersion,'mobile':mobile,'modemNum':modemNum,'modemTable':modemTable,'modemEntry':modemEntry,_F:mIndex,'mDescr':mDescr,'mImei':mImei,'mModel':mModel,'mManufacturer':mManufacturer,'mRevision':mRevision,'mSerial':mSerial,'mIMSI':mIMSI,'mSimState':mSimState,'mPinState':mPinState,'mNetState':mNetState,'mSignal':mSignal,'mOperator':mOperator,'mOperatorNumber':mOperatorNumber,'mConnectionState':mConnectionState,'mConnectionType':mConnectionType,'mTemperature':mTemperature,'mCellID':mCellID,'mSINR':mSINR,'mRSRP':mRSRP,'mRSRQ':mRSRQ,'mSent':mSent,'mReceived':mReceived,'mIP':mIP,'mSentToday':mSentToday,'mReceivedToday':mReceivedToday,'gps':gps,'latitude':latitude,'longtitude':longtitude,'accuracy':accuracy,'datetime':datetime,'numSatellites':numSatellites,'notifications':notifications,'mobileNotifications':mobileNotifications,'signalChangeNotification':signalChangeNotification,'connectionTypeNotification':connectionTypeNotification,'ioNotifications':ioNotifications,'digitalInputNotification':digitalInputNotification,'digitalOutputNotification':digitalOutputNotification,'relay0Notification':relay0Notification,'digitalInput2Notification':digitalInput2Notification,'digitalIioNotification':digitalIioNotification,'digitalOutput2Notification':digitalOutput2Notification,'hotspot':hotspot,'hsState':hsState,'hsIP':hsIP,'hsNet':hsNet,'hsAuth':hsAuth,'hsSessionCount':hsSessionCount,'hsSessionTable':hsSessionTable,'hsSessionEntry':hsSessionEntry,_G:hssIndex,'hssMAC':hssMAC,'hssIP':hssIP,'hssID':hssID,'hssUsername':hssUsername,'hssState':hssState,'hssDwLimit':hssDwLimit,'hssUpLimit':hssUpLimit,'hssTimeLimit':hssTimeLimit,'hssIdleTimeout':hssIdleTimeout,'hssDwBandwidth':hssDwBandwidth,'hssUpBandwidth':hssUpBandwidth,'hssURL':hssURL,'io':io,'ioCount':ioCount,'ioTable':ioTable,'ioEntry':ioEntry,_H:ioIndex,'ioSystemName':ioSystemName,'ioName':ioName,'ioType':ioType,'ioBidirectional':ioBidirectional,'ioState':ioState,'ioInput':ioInput,'ioInverted':ioInverted,'ioCurrent':ioCurrent,'ioPercentage':ioPercentage})