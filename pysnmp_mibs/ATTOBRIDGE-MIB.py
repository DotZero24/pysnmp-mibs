_c='errorsSinceUpdate'
_b='errorASCQ'
_a='errorASC'
_Z='errorSenseKey'
_Y='errorOpCode'
_X='errorSource'
_W='deviceState'
_V='deviceSource'
_U='voltage'
_T='voltageSensorStatus'
_S='temperature'
_R='tempSensorStatus'
_Q='trapClientIndex'
_P='errorIndex'
_O='unknown'
_N='normal'
_M='OctetString'
_L='deviceCacheIndex'
_K='voltageSensorIndex'
_J='critical'
_I='warning'
_H='tempSensorIndex'
_G='enabled'
_F='disabled'
_E='DisplayString'
_D='Integer32'
_C='ATTOBRIDGE-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','experimental','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
bridge=ModuleIdentity((1,3,6,1,4,1,4547,1,2))
_Attotech_ObjectIdentity=ObjectIdentity
attotech=_Attotech_ObjectIdentity((1,3,6,1,4,1,4547))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,4547,1))
_BridgeConfig_ObjectIdentity=ObjectIdentity
bridgeConfig=_BridgeConfig_ObjectIdentity((1,3,6,1,4,1,4547,1,2,1))
class _TrapsEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_TrapsEnabled_Type.__name__=_D
_TrapsEnabled_Object=MibScalar
trapsEnabled=_TrapsEnabled_Object((1,3,6,1,4,1,4547,1,2,1,1),_TrapsEnabled_Type())
trapsEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:trapsEnabled.setStatus(_A)
class _SnmpUpdatesEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SnmpUpdatesEnabled_Type.__name__=_D
_SnmpUpdatesEnabled_Object=MibScalar
snmpUpdatesEnabled=_SnmpUpdatesEnabled_Object((1,3,6,1,4,1,4547,1,2,1,2),_SnmpUpdatesEnabled_Type())
snmpUpdatesEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpUpdatesEnabled.setStatus(_A)
class _SnmpExtendedEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SnmpExtendedEnabled_Type.__name__=_D
_SnmpExtendedEnabled_Object=MibScalar
snmpExtendedEnabled=_SnmpExtendedEnabled_Object((1,3,6,1,4,1,4547,1,2,1,3),_SnmpExtendedEnabled_Type())
snmpExtendedEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpExtendedEnabled.setStatus(_A)
_BridgeStatus_ObjectIdentity=ObjectIdentity
bridgeStatus=_BridgeStatus_ObjectIdentity((1,3,6,1,4,1,4547,1,2,2))
_TempSensorTable_Object=MibTable
tempSensorTable=_TempSensorTable_Object((1,3,6,1,4,1,4547,1,2,2,1))
if mibBuilder.loadTexts:tempSensorTable.setStatus(_A)
_TempSensorEntry_Object=MibTableRow
tempSensorEntry=_TempSensorEntry_Object((1,3,6,1,4,1,4547,1,2,2,1,1))
tempSensorEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:tempSensorEntry.setStatus(_A)
class _TempSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_TempSensorIndex_Type.__name__=_D
_TempSensorIndex_Object=MibTableColumn
tempSensorIndex=_TempSensorIndex_Object((1,3,6,1,4,1,4547,1,2,2,1,1,1),_TempSensorIndex_Type())
tempSensorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:tempSensorIndex.setStatus(_A)
class _TempSensorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),(_I,2),(_J,3),(_O,4)))
_TempSensorStatus_Type.__name__=_D
_TempSensorStatus_Object=MibTableColumn
tempSensorStatus=_TempSensorStatus_Object((1,3,6,1,4,1,4547,1,2,2,1,1,2),_TempSensorStatus_Type())
tempSensorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tempSensorStatus.setStatus(_A)
_Temperature_Type=Integer32
_Temperature_Object=MibTableColumn
temperature=_Temperature_Object((1,3,6,1,4,1,4547,1,2,2,1,1,3),_Temperature_Type())
temperature.setMaxAccess(_B)
if mibBuilder.loadTexts:temperature.setStatus(_A)
_VoltageSensorTable_Object=MibTable
voltageSensorTable=_VoltageSensorTable_Object((1,3,6,1,4,1,4547,1,2,2,2))
if mibBuilder.loadTexts:voltageSensorTable.setStatus(_A)
_VoltageSensorEntry_Object=MibTableRow
voltageSensorEntry=_VoltageSensorEntry_Object((1,3,6,1,4,1,4547,1,2,2,2,1))
voltageSensorEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:voltageSensorEntry.setStatus(_A)
class _VoltageSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_VoltageSensorIndex_Type.__name__=_D
_VoltageSensorIndex_Object=MibTableColumn
voltageSensorIndex=_VoltageSensorIndex_Object((1,3,6,1,4,1,4547,1,2,2,2,1,1),_VoltageSensorIndex_Type())
voltageSensorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:voltageSensorIndex.setStatus(_A)
class _VoltageSensorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),(_I,2),(_J,3),(_O,4)))
_VoltageSensorStatus_Type.__name__=_D
_VoltageSensorStatus_Object=MibTableColumn
voltageSensorStatus=_VoltageSensorStatus_Object((1,3,6,1,4,1,4547,1,2,2,2,1,2),_VoltageSensorStatus_Type())
voltageSensorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:voltageSensorStatus.setStatus(_A)
_Voltage_Type=Integer32
_Voltage_Object=MibTableColumn
voltage=_Voltage_Object((1,3,6,1,4,1,4547,1,2,2,2,1,3),_Voltage_Type())
voltage.setMaxAccess(_B)
if mibBuilder.loadTexts:voltage.setStatus(_A)
_DeviceCount_Type=Counter32
_DeviceCount_Object=MibScalar
deviceCount=_DeviceCount_Object((1,3,6,1,4,1,4547,1,2,2,4),_DeviceCount_Type())
deviceCount.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceCount.setStatus(_A)
_DeviceCacheTable_Object=MibTable
deviceCacheTable=_DeviceCacheTable_Object((1,3,6,1,4,1,4547,1,2,2,5))
if mibBuilder.loadTexts:deviceCacheTable.setStatus(_A)
_DeviceEntry_Object=MibTableRow
deviceEntry=_DeviceEntry_Object((1,3,6,1,4,1,4547,1,2,2,5,1))
deviceEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:deviceEntry.setStatus(_A)
class _DeviceCacheIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_DeviceCacheIndex_Type.__name__=_D
_DeviceCacheIndex_Object=MibTableColumn
deviceCacheIndex=_DeviceCacheIndex_Object((1,3,6,1,4,1,4547,1,2,2,5,1,1),_DeviceCacheIndex_Type())
deviceCacheIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceCacheIndex.setStatus(_A)
class _DeviceSource_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_DeviceSource_Type.__name__=_E
_DeviceSource_Object=MibTableColumn
deviceSource=_DeviceSource_Object((1,3,6,1,4,1,4547,1,2,2,5,1,2),_DeviceSource_Type())
deviceSource.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceSource.setStatus(_A)
class _DeviceDestination_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_DeviceDestination_Type.__name__=_E
_DeviceDestination_Object=MibTableColumn
deviceDestination=_DeviceDestination_Object((1,3,6,1,4,1,4547,1,2,2,5,1,3),_DeviceDestination_Type())
deviceDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceDestination.setStatus(_A)
class _DeviceType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_DeviceType_Type.__name__=_E
_DeviceType_Object=MibTableColumn
deviceType=_DeviceType_Object((1,3,6,1,4,1,4547,1,2,2,5,1,4),_DeviceType_Type())
deviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceType.setStatus(_A)
class _DeviceVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_DeviceVendor_Type.__name__=_E
_DeviceVendor_Object=MibTableColumn
deviceVendor=_DeviceVendor_Object((1,3,6,1,4,1,4547,1,2,2,5,1,5),_DeviceVendor_Type())
deviceVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceVendor.setStatus(_A)
class _DeviceProduct_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_DeviceProduct_Type.__name__=_E
_DeviceProduct_Object=MibTableColumn
deviceProduct=_DeviceProduct_Object((1,3,6,1,4,1,4547,1,2,2,5,1,6),_DeviceProduct_Type())
deviceProduct.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceProduct.setStatus(_A)
class _DeviceRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_DeviceRevision_Type.__name__=_E
_DeviceRevision_Object=MibTableColumn
deviceRevision=_DeviceRevision_Object((1,3,6,1,4,1,4547,1,2,2,5,1,7),_DeviceRevision_Type())
deviceRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceRevision.setStatus(_A)
class _DeviceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('offline',0),('online',1)))
_DeviceState_Type.__name__=_D
_DeviceState_Object=MibTableColumn
deviceState=_DeviceState_Object((1,3,6,1,4,1,4547,1,2,2,5,1,8),_DeviceState_Type())
deviceState.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceState.setStatus(_A)
_ErrorCount_Type=Counter32
_ErrorCount_Object=MibScalar
errorCount=_ErrorCount_Object((1,3,6,1,4,1,4547,1,2,2,6),_ErrorCount_Type())
errorCount.setMaxAccess(_B)
if mibBuilder.loadTexts:errorCount.setStatus(_A)
_ErrorsSinceUpdate_Type=Counter32
_ErrorsSinceUpdate_Object=MibScalar
errorsSinceUpdate=_ErrorsSinceUpdate_Object((1,3,6,1,4,1,4547,1,2,2,7),_ErrorsSinceUpdate_Type())
errorsSinceUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:errorsSinceUpdate.setStatus(_A)
_ErrorTable_Object=MibTable
errorTable=_ErrorTable_Object((1,3,6,1,4,1,4547,1,2,2,8))
if mibBuilder.loadTexts:errorTable.setStatus(_A)
_ErrorEntry_Object=MibTableRow
errorEntry=_ErrorEntry_Object((1,3,6,1,4,1,4547,1,2,2,8,1))
errorEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:errorEntry.setStatus(_A)
_ErrorIndex_Type=Integer32
_ErrorIndex_Object=MibTableColumn
errorIndex=_ErrorIndex_Object((1,3,6,1,4,1,4547,1,2,2,8,1,1),_ErrorIndex_Type())
errorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:errorIndex.setStatus(_A)
class _ErrorDateStamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_ErrorDateStamp_Type.__name__=_E
_ErrorDateStamp_Object=MibTableColumn
errorDateStamp=_ErrorDateStamp_Object((1,3,6,1,4,1,4547,1,2,2,8,1,2),_ErrorDateStamp_Type())
errorDateStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:errorDateStamp.setStatus(_A)
class _ErrorTimeStamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_ErrorTimeStamp_Type.__name__=_E
_ErrorTimeStamp_Object=MibTableColumn
errorTimeStamp=_ErrorTimeStamp_Object((1,3,6,1,4,1,4547,1,2,2,8,1,3),_ErrorTimeStamp_Type())
errorTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:errorTimeStamp.setStatus(_A)
class _ErrorInitiator_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ErrorInitiator_Type.__name__=_E
_ErrorInitiator_Object=MibTableColumn
errorInitiator=_ErrorInitiator_Object((1,3,6,1,4,1,4547,1,2,2,8,1,4),_ErrorInitiator_Type())
errorInitiator.setMaxAccess(_B)
if mibBuilder.loadTexts:errorInitiator.setStatus(_A)
class _ErrorSource_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ErrorSource_Type.__name__=_E
_ErrorSource_Object=MibTableColumn
errorSource=_ErrorSource_Object((1,3,6,1,4,1,4547,1,2,2,8,1,5),_ErrorSource_Type())
errorSource.setMaxAccess(_B)
if mibBuilder.loadTexts:errorSource.setStatus(_A)
_ErrorOpCode_Type=Integer32
_ErrorOpCode_Object=MibTableColumn
errorOpCode=_ErrorOpCode_Object((1,3,6,1,4,1,4547,1,2,2,8,1,6),_ErrorOpCode_Type())
errorOpCode.setMaxAccess(_B)
if mibBuilder.loadTexts:errorOpCode.setStatus(_A)
_ErrorSenseKey_Type=Integer32
_ErrorSenseKey_Object=MibTableColumn
errorSenseKey=_ErrorSenseKey_Object((1,3,6,1,4,1,4547,1,2,2,8,1,7),_ErrorSenseKey_Type())
errorSenseKey.setMaxAccess(_B)
if mibBuilder.loadTexts:errorSenseKey.setStatus(_A)
_ErrorASC_Type=Integer32
_ErrorASC_Object=MibTableColumn
errorASC=_ErrorASC_Object((1,3,6,1,4,1,4547,1,2,2,8,1,8),_ErrorASC_Type())
errorASC.setMaxAccess(_B)
if mibBuilder.loadTexts:errorASC.setStatus(_A)
_ErrorASCQ_Type=Integer32
_ErrorASCQ_Object=MibTableColumn
errorASCQ=_ErrorASCQ_Object((1,3,6,1,4,1,4547,1,2,2,8,1,9),_ErrorASCQ_Type())
errorASCQ.setMaxAccess(_B)
if mibBuilder.loadTexts:errorASCQ.setStatus(_A)
class _ErrorLogSense_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_ErrorLogSense_Type.__name__=_M
_ErrorLogSense_Object=MibTableColumn
errorLogSense=_ErrorLogSense_Object((1,3,6,1,4,1,4547,1,2,2,8,1,10),_ErrorLogSense_Type())
errorLogSense.setMaxAccess(_B)
if mibBuilder.loadTexts:errorLogSense.setStatus(_A)
_BridgeTrapInfo_ObjectIdentity=ObjectIdentity
bridgeTrapInfo=_BridgeTrapInfo_ObjectIdentity((1,3,6,1,4,1,4547,1,2,3))
_TrapMaxClients_Type=Integer32
_TrapMaxClients_Object=MibScalar
trapMaxClients=_TrapMaxClients_Object((1,3,6,1,4,1,4547,1,2,3,1),_TrapMaxClients_Type())
trapMaxClients.setMaxAccess(_B)
if mibBuilder.loadTexts:trapMaxClients.setStatus(_A)
_TrapClientTable_Object=MibTable
trapClientTable=_TrapClientTable_Object((1,3,6,1,4,1,4547,1,2,3,3))
if mibBuilder.loadTexts:trapClientTable.setStatus(_A)
_TrapClientEntry_Object=MibTableRow
trapClientEntry=_TrapClientEntry_Object((1,3,6,1,4,1,4547,1,2,3,3,1))
trapClientEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:trapClientEntry.setStatus(_A)
_TrapClientIndex_Type=Integer32
_TrapClientIndex_Object=MibTableColumn
trapClientIndex=_TrapClientIndex_Object((1,3,6,1,4,1,4547,1,2,3,3,1,1),_TrapClientIndex_Type())
trapClientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:trapClientIndex.setStatus(_A)
_TrapClientIpAddress_Type=IpAddress
_TrapClientIpAddress_Object=MibTableColumn
trapClientIpAddress=_TrapClientIpAddress_Object((1,3,6,1,4,1,4547,1,2,3,3,1,2),_TrapClientIpAddress_Type())
trapClientIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:trapClientIpAddress.setStatus(_A)
class _TrapClientPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TrapClientPort_Type.__name__=_D
_TrapClientPort_Object=MibTableColumn
trapClientPort=_TrapClientPort_Object((1,3,6,1,4,1,4547,1,2,3,3,1,3),_TrapClientPort_Type())
trapClientPort.setMaxAccess(_B)
if mibBuilder.loadTexts:trapClientPort.setStatus(_A)
class _TrapClientFilter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),(_J,2),(_I,3),('informational',4),('all',5)))
_TrapClientFilter_Type.__name__=_D
_TrapClientFilter_Object=MibTableColumn
trapClientFilter=_TrapClientFilter_Object((1,3,6,1,4,1,4547,1,2,3,3,1,4),_TrapClientFilter_Type())
trapClientFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:trapClientFilter.setStatus(_A)
class _TrapClientRowState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rowDestroy',1),('rowInactive',2),('rowActive',3)))
_TrapClientRowState_Type.__name__=_D
_TrapClientRowState_Object=MibTableColumn
trapClientRowState=_TrapClientRowState_Object((1,3,6,1,4,1,4547,1,2,3,3,1,5),_TrapClientRowState_Type())
trapClientRowState.setMaxAccess('read-write')
if mibBuilder.loadTexts:trapClientRowState.setStatus(_A)
bridgeTempStatusChanged=NotificationType((1,3,6,1,4,1,4547,0,1))
bridgeTempStatusChanged.setObjects(*((_C,_H),(_C,_R),(_C,_S)))
if mibBuilder.loadTexts:bridgeTempStatusChanged.setStatus('')
bridgeVoltageStatusChanged=NotificationType((1,3,6,1,4,1,4547,0,2))
bridgeVoltageStatusChanged.setObjects(*((_C,_K),(_C,_T),(_C,_U)))
if mibBuilder.loadTexts:bridgeVoltageStatusChanged.setStatus('')
bridgeDeviceTransition=NotificationType((1,3,6,1,4,1,4547,0,4))
bridgeDeviceTransition.setObjects(*((_C,_L),(_C,_V),(_C,_W)))
if mibBuilder.loadTexts:bridgeDeviceTransition.setStatus('')
bridgeDeviceError=NotificationType((1,3,6,1,4,1,4547,0,5))
bridgeDeviceError.setObjects(*((_C,_X),(_C,_Y),(_C,_Z),(_C,_a),(_C,_b),(_C,_c)))
if mibBuilder.loadTexts:bridgeDeviceError.setStatus('')
mibBuilder.exportSymbols(_C,**{'attotech':attotech,'bridgeTempStatusChanged':bridgeTempStatusChanged,'bridgeVoltageStatusChanged':bridgeVoltageStatusChanged,'bridgeDeviceTransition':bridgeDeviceTransition,'bridgeDeviceError':bridgeDeviceError,'products':products,'bridge':bridge,'bridgeConfig':bridgeConfig,'trapsEnabled':trapsEnabled,'snmpUpdatesEnabled':snmpUpdatesEnabled,'snmpExtendedEnabled':snmpExtendedEnabled,'bridgeStatus':bridgeStatus,'tempSensorTable':tempSensorTable,'tempSensorEntry':tempSensorEntry,_H:tempSensorIndex,_R:tempSensorStatus,_S:temperature,'voltageSensorTable':voltageSensorTable,'voltageSensorEntry':voltageSensorEntry,_K:voltageSensorIndex,_T:voltageSensorStatus,_U:voltage,'deviceCount':deviceCount,'deviceCacheTable':deviceCacheTable,'deviceEntry':deviceEntry,_L:deviceCacheIndex,_V:deviceSource,'deviceDestination':deviceDestination,'deviceType':deviceType,'deviceVendor':deviceVendor,'deviceProduct':deviceProduct,'deviceRevision':deviceRevision,_W:deviceState,'errorCount':errorCount,_c:errorsSinceUpdate,'errorTable':errorTable,'errorEntry':errorEntry,_P:errorIndex,'errorDateStamp':errorDateStamp,'errorTimeStamp':errorTimeStamp,'errorInitiator':errorInitiator,_X:errorSource,_Y:errorOpCode,_Z:errorSenseKey,_a:errorASC,_b:errorASCQ,'errorLogSense':errorLogSense,'bridgeTrapInfo':bridgeTrapInfo,'trapMaxClients':trapMaxClients,'trapClientTable':trapClientTable,'trapClientEntry':trapClientEntry,_Q:trapClientIndex,'trapClientIpAddress':trapClientIpAddress,'trapClientPort':trapClientPort,'trapClientFilter':trapClientFilter,'trapClientRowState':trapClientRowState})