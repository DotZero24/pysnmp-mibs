_M='lgpSysEventDescription'
_L='lgpSysDeviceComponentIndex'
_K='lgpAgentDeviceIndex'
_J='lgpAgentConnectedDeviceCount'
_I='LIEBERT-GP-SYSTEM-MIB'
_H='sysUpTime'
_G='SNMPv2-MIB'
_F='LIEBERT-GP-AGENT-MIB'
_E='read-write'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lgpAgentConnectedDeviceCount,lgpAgentDeviceIndex=mibBuilder.importSymbols(_F,_J,_K)
lgpSystem,liebertSystemModuleReg=mibBuilder.importSymbols('LIEBERT-GP-REGISTRATION-MIB','lgpSystem','liebertSystemModuleReg')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysUpTime,=mibBuilder.importSymbols(_G,_H)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
liebertSystemModule=ModuleIdentity((1,3,6,1,4,1,476,1,42,1,8,1))
if mibBuilder.loadTexts:liebertSystemModule.setRevisions(('2008-11-17 00:00','2008-07-02 00:00','2008-01-10 00:00','2007-05-29 00:00','2006-02-22 00:00'))
_LgpSysStatistics_ObjectIdentity=ObjectIdentity
lgpSysStatistics=_LgpSysStatistics_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,7,1))
if mibBuilder.loadTexts:lgpSysStatistics.setStatus(_A)
_LgpSysStatisticsRunHrs_Type=Unsigned32
_LgpSysStatisticsRunHrs_Object=MibScalar
lgpSysStatisticsRunHrs=_LgpSysStatisticsRunHrs_Object((1,3,6,1,4,1,476,1,42,3,7,1,1),_LgpSysStatisticsRunHrs_Type())
lgpSysStatisticsRunHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpSysStatisticsRunHrs.setStatus(_A)
if mibBuilder.loadTexts:lgpSysStatisticsRunHrs.setUnits('hours')
_LgpSysStatus_ObjectIdentity=ObjectIdentity
lgpSysStatus=_LgpSysStatus_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,7,2))
if mibBuilder.loadTexts:lgpSysStatus.setStatus(_A)
class _LgpSysSelfTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',1),('passed',2),('failed',3),('inProgress',4),('sysFailure',5),('inhibited',6)))
_LgpSysSelfTestResult_Type.__name__=_C
_LgpSysSelfTestResult_Object=MibScalar
lgpSysSelfTestResult=_LgpSysSelfTestResult_Object((1,3,6,1,4,1,476,1,42,3,7,2,1),_LgpSysSelfTestResult_Type())
lgpSysSelfTestResult.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpSysSelfTestResult.setStatus(_A)
class _LgpSysState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('normalOperation',1),('startUp',2),('normalWithWarning',3),('normalWithAlarm',4),('abnormalOperation',5)))
_LgpSysState_Type.__name__=_C
_LgpSysState_Object=MibScalar
lgpSysState=_LgpSysState_Object((1,3,6,1,4,1,476,1,42,3,7,2,2),_LgpSysState_Type())
lgpSysState.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpSysState.setStatus(_A)
_LgpSysSettings_ObjectIdentity=ObjectIdentity
lgpSysSettings=_LgpSysSettings_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,7,3))
if mibBuilder.loadTexts:lgpSysSettings.setStatus(_A)
class _LgpSysAudibleAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_LgpSysAudibleAlarm_Type.__name__=_C
_LgpSysAudibleAlarm_Object=MibScalar
lgpSysAudibleAlarm=_LgpSysAudibleAlarm_Object((1,3,6,1,4,1,476,1,42,3,7,3,1),_LgpSysAudibleAlarm_Type())
lgpSysAudibleAlarm.setMaxAccess(_E)
if mibBuilder.loadTexts:lgpSysAudibleAlarm.setStatus(_A)
_LgpSysControl_ObjectIdentity=ObjectIdentity
lgpSysControl=_LgpSysControl_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,7,4))
if mibBuilder.loadTexts:lgpSysControl.setStatus(_A)
_LgpSysSelfTest_Type=Integer32
_LgpSysSelfTest_Object=MibScalar
lgpSysSelfTest=_LgpSysSelfTest_Object((1,3,6,1,4,1,476,1,42,3,7,4,1),_LgpSysSelfTest_Type())
lgpSysSelfTest.setMaxAccess(_E)
if mibBuilder.loadTexts:lgpSysSelfTest.setStatus(_A)
class _LgpSysControlOperationOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_LgpSysControlOperationOnOff_Type.__name__=_C
_LgpSysControlOperationOnOff_Object=MibScalar
lgpSysControlOperationOnOff=_LgpSysControlOperationOnOff_Object((1,3,6,1,4,1,476,1,42,3,7,4,2),_LgpSysControlOperationOnOff_Type())
lgpSysControlOperationOnOff.setMaxAccess(_E)
if mibBuilder.loadTexts:lgpSysControlOperationOnOff.setStatus(_A)
_LgpSysTime_ObjectIdentity=ObjectIdentity
lgpSysTime=_LgpSysTime_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,7,5))
if mibBuilder.loadTexts:lgpSysTime.setStatus(_A)
_LgpSysTimeEpoch_Type=Unsigned32
_LgpSysTimeEpoch_Object=MibScalar
lgpSysTimeEpoch=_LgpSysTimeEpoch_Object((1,3,6,1,4,1,476,1,42,3,7,5,1),_LgpSysTimeEpoch_Type())
lgpSysTimeEpoch.setMaxAccess(_E)
if mibBuilder.loadTexts:lgpSysTimeEpoch.setStatus(_A)
if mibBuilder.loadTexts:lgpSysTimeEpoch.setUnits('seconds')
_LgpSysMaintenance_ObjectIdentity=ObjectIdentity
lgpSysMaintenance=_LgpSysMaintenance_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,7,6))
if mibBuilder.loadTexts:lgpSysMaintenance.setStatus(_A)
_LgpSysMaintenanceCapacity_Type=Unsigned32
_LgpSysMaintenanceCapacity_Object=MibScalar
lgpSysMaintenanceCapacity=_LgpSysMaintenanceCapacity_Object((1,3,6,1,4,1,476,1,42,3,7,6,1),_LgpSysMaintenanceCapacity_Type())
lgpSysMaintenanceCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpSysMaintenanceCapacity.setStatus(_A)
if mibBuilder.loadTexts:lgpSysMaintenanceCapacity.setUnits('percent')
_LgpSysMaintenanceYear_Type=Unsigned32
_LgpSysMaintenanceYear_Object=MibScalar
lgpSysMaintenanceYear=_LgpSysMaintenanceYear_Object((1,3,6,1,4,1,476,1,42,3,7,6,2),_LgpSysMaintenanceYear_Type())
lgpSysMaintenanceYear.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpSysMaintenanceYear.setStatus(_A)
if mibBuilder.loadTexts:lgpSysMaintenanceYear.setUnits('year')
_LgpSysMaintenanceMonth_Type=Unsigned32
_LgpSysMaintenanceMonth_Object=MibScalar
lgpSysMaintenanceMonth=_LgpSysMaintenanceMonth_Object((1,3,6,1,4,1,476,1,42,3,7,6,3),_LgpSysMaintenanceMonth_Type())
lgpSysMaintenanceMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpSysMaintenanceMonth.setStatus(_A)
if mibBuilder.loadTexts:lgpSysMaintenanceMonth.setUnits('month')
class _LgpSysEventDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(255,255));fixedLength=255
_LgpSysEventDescription_Type.__name__=_D
_LgpSysEventDescription_Object=MibScalar
lgpSysEventDescription=_LgpSysEventDescription_Object((1,3,6,1,4,1,476,1,42,3,7,7),_LgpSysEventDescription_Type())
lgpSysEventDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpSysEventDescription.setStatus(_A)
_LgpSysEventNotifications_ObjectIdentity=ObjectIdentity
lgpSysEventNotifications=_LgpSysEventNotifications_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,7,8))
if mibBuilder.loadTexts:lgpSysEventNotifications.setStatus(_A)
_LgpSysDeviceComponentGroup_ObjectIdentity=ObjectIdentity
lgpSysDeviceComponentGroup=_LgpSysDeviceComponentGroup_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,7,9))
if mibBuilder.loadTexts:lgpSysDeviceComponentGroup.setStatus(_A)
_LgpSysDeviceComponentTable_Object=MibTable
lgpSysDeviceComponentTable=_LgpSysDeviceComponentTable_Object((1,3,6,1,4,1,476,1,42,3,7,9,1))
if mibBuilder.loadTexts:lgpSysDeviceComponentTable.setStatus(_A)
_LgpSysDeviceComponentEntry_Object=MibTableRow
lgpSysDeviceComponentEntry=_LgpSysDeviceComponentEntry_Object((1,3,6,1,4,1,476,1,42,3,7,9,1,1))
lgpSysDeviceComponentEntry.setIndexNames((0,_F,_K),(0,_I,_L))
if mibBuilder.loadTexts:lgpSysDeviceComponentEntry.setStatus(_A)
_LgpSysDeviceComponentIndex_Type=Unsigned32
_LgpSysDeviceComponentIndex_Object=MibTableColumn
lgpSysDeviceComponentIndex=_LgpSysDeviceComponentIndex_Object((1,3,6,1,4,1,476,1,42,3,7,9,1,1,1),_LgpSysDeviceComponentIndex_Type())
lgpSysDeviceComponentIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:lgpSysDeviceComponentIndex.setStatus(_A)
_LgpSysDeviceComponentDescr_Type=ObjectIdentifier
_LgpSysDeviceComponentDescr_Object=MibTableColumn
lgpSysDeviceComponentDescr=_LgpSysDeviceComponentDescr_Object((1,3,6,1,4,1,476,1,42,3,7,9,1,1,2),_LgpSysDeviceComponentDescr_Type())
lgpSysDeviceComponentDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpSysDeviceComponentDescr.setStatus(_A)
class _LgpSysDeviceComponentSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(255,255));fixedLength=255
_LgpSysDeviceComponentSerialNum_Type.__name__=_D
_LgpSysDeviceComponentSerialNum_Object=MibTableColumn
lgpSysDeviceComponentSerialNum=_LgpSysDeviceComponentSerialNum_Object((1,3,6,1,4,1,476,1,42,3,7,9,1,1,3),_LgpSysDeviceComponentSerialNum_Type())
lgpSysDeviceComponentSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpSysDeviceComponentSerialNum.setStatus(_A)
class _LgpSysDeviceComponentModelNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(255,255));fixedLength=255
_LgpSysDeviceComponentModelNum_Type.__name__=_D
_LgpSysDeviceComponentModelNum_Object=MibTableColumn
lgpSysDeviceComponentModelNum=_LgpSysDeviceComponentModelNum_Object((1,3,6,1,4,1,476,1,42,3,7,9,1,1,4),_LgpSysDeviceComponentModelNum_Type())
lgpSysDeviceComponentModelNum.setMaxAccess(_B)
if mibBuilder.loadTexts:lgpSysDeviceComponentModelNum.setStatus(_A)
_LgpSysDeviceComponentWellknown_ObjectIdentity=ObjectIdentity
lgpSysDeviceComponentWellknown=_LgpSysDeviceComponentWellknown_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,7,9,5))
if mibBuilder.loadTexts:lgpSysDeviceComponentWellknown.setStatus(_A)
_LgpSysDeviceBatCabinet_ObjectIdentity=ObjectIdentity
lgpSysDeviceBatCabinet=_LgpSysDeviceBatCabinet_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,7,9,5,5))
if mibBuilder.loadTexts:lgpSysDeviceBatCabinet.setStatus(_A)
_LgpSysDeviceParallelCabinet_ObjectIdentity=ObjectIdentity
lgpSysDeviceParallelCabinet=_LgpSysDeviceParallelCabinet_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,7,9,5,6))
if mibBuilder.loadTexts:lgpSysDeviceParallelCabinet.setStatus(_A)
_LgpSysDeviceMaintBypass_ObjectIdentity=ObjectIdentity
lgpSysDeviceMaintBypass=_LgpSysDeviceMaintBypass_ObjectIdentity((1,3,6,1,4,1,476,1,42,3,7,9,5,7))
if mibBuilder.loadTexts:lgpSysDeviceMaintBypass.setStatus(_A)
lgpSysNotification=NotificationType((1,3,6,1,4,1,476,1,42,3,7,8,1))
lgpSysNotification.setObjects(*((_G,_H),(_I,_M)))
if mibBuilder.loadTexts:lgpSysNotification.setStatus(_A)
lgpSysNormal=NotificationType((1,3,6,1,4,1,476,1,42,3,7,8,2))
lgpSysNormal.setObjects(*((_G,_H),(_F,_J)))
if mibBuilder.loadTexts:lgpSysNormal.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'liebertSystemModule':liebertSystemModule,'lgpSysStatistics':lgpSysStatistics,'lgpSysStatisticsRunHrs':lgpSysStatisticsRunHrs,'lgpSysStatus':lgpSysStatus,'lgpSysSelfTestResult':lgpSysSelfTestResult,'lgpSysState':lgpSysState,'lgpSysSettings':lgpSysSettings,'lgpSysAudibleAlarm':lgpSysAudibleAlarm,'lgpSysControl':lgpSysControl,'lgpSysSelfTest':lgpSysSelfTest,'lgpSysControlOperationOnOff':lgpSysControlOperationOnOff,'lgpSysTime':lgpSysTime,'lgpSysTimeEpoch':lgpSysTimeEpoch,'lgpSysMaintenance':lgpSysMaintenance,'lgpSysMaintenanceCapacity':lgpSysMaintenanceCapacity,'lgpSysMaintenanceYear':lgpSysMaintenanceYear,'lgpSysMaintenanceMonth':lgpSysMaintenanceMonth,_M:lgpSysEventDescription,'lgpSysEventNotifications':lgpSysEventNotifications,'lgpSysNotification':lgpSysNotification,'lgpSysNormal':lgpSysNormal,'lgpSysDeviceComponentGroup':lgpSysDeviceComponentGroup,'lgpSysDeviceComponentTable':lgpSysDeviceComponentTable,'lgpSysDeviceComponentEntry':lgpSysDeviceComponentEntry,_L:lgpSysDeviceComponentIndex,'lgpSysDeviceComponentDescr':lgpSysDeviceComponentDescr,'lgpSysDeviceComponentSerialNum':lgpSysDeviceComponentSerialNum,'lgpSysDeviceComponentModelNum':lgpSysDeviceComponentModelNum,'lgpSysDeviceComponentWellknown':lgpSysDeviceComponentWellknown,'lgpSysDeviceBatCabinet':lgpSysDeviceBatCabinet,'lgpSysDeviceParallelCabinet':lgpSysDeviceParallelCabinet,'lgpSysDeviceMaintBypass':lgpSysDeviceMaintBypass})