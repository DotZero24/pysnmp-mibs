_o='totalBuffers'
_n='freeMemory'
_m='acceleratorTemperatureStatus'
_l='sbTempSettableThreshold'
_k='sbTempSettableThresholdStatus'
_j='sbTempFixedThreshold'
_i='sbTempFixedThresholdStatus'
_h='generalTemperatureThreshold'
_g='generalTemperatureActualTemp'
_f='generalTemperatureStatus'
_e='restartCause'
_d='fanAndPsAccelFanStatus'
_c='fanAndPsMainMonitoringStatus'
_b='fanAndPsFanTrayStatus'
_a='fanAndPsFanTrayPresent'
_Z='fanAndPsTemperatureStatus'
_Y='fanAndPsRedundantFanStatus'
_X='fanAndPsMainFanStatus'
_W='fanAndPsRedundantPSUStatus'
_V='fanAndPsMainPSUStatus'
_U='fanAndPsRpsConnectionStatus'
_T='atPortInfoTransceiverifIndex'
_S='crossover'
_R='sbTempIndex'
_Q='supported'
_P='unknown'
_O='fanAndPsPsuNumber'
_N='DisplayStringUnsized'
_M='sbTempActualTemperature'
_L='normal'
_K='off'
_J='notMonitoring'
_I='notPresent'
_H='read-write'
_G='notOk'
_F='ok'
_E='notSupported'
_D='AT-SYSINFO-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,atRouter=mibBuilder.importSymbols('AT-SMI-MIB',_N,'atRouter')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sysinfo=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,3))
if mibBuilder.loadTexts:sysinfo.setRevisions(('2006-06-14 00:00','2008-02-26 00:00','2010-06-04 00:00','2010-06-15 00:15','2010-08-16 00:16','2010-08-31 00:31','2010-09-07 00:00'))
_FanAndPs_ObjectIdentity=ObjectIdentity
fanAndPs=_FanAndPs_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,1))
_FanAndPsTrap_ObjectIdentity=ObjectIdentity
fanAndPsTrap=_FanAndPsTrap_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,1,0))
class _FanAndPsRpsConnectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_E,0),('connected',1),('notConnected',2),(_J,3)))
_FanAndPsRpsConnectionStatus_Type.__name__=_C
_FanAndPsRpsConnectionStatus_Object=MibScalar
fanAndPsRpsConnectionStatus=_FanAndPsRpsConnectionStatus_Object((1,3,6,1,4,1,207,8,4,4,3,1,1),_FanAndPsRpsConnectionStatus_Type())
fanAndPsRpsConnectionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fanAndPsRpsConnectionStatus.setStatus(_A)
class _FanAndPsMainPSUStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('on',1),(_K,2),('faulty',3)))
_FanAndPsMainPSUStatus_Type.__name__=_C
_FanAndPsMainPSUStatus_Object=MibScalar
fanAndPsMainPSUStatus=_FanAndPsMainPSUStatus_Object((1,3,6,1,4,1,207,8,4,4,3,1,2),_FanAndPsMainPSUStatus_Type())
fanAndPsMainPSUStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fanAndPsMainPSUStatus.setStatus(_A)
class _FanAndPsRedundantPSUStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_E,0),('on',1),(_K,2),(_J,3)))
_FanAndPsRedundantPSUStatus_Type.__name__=_C
_FanAndPsRedundantPSUStatus_Object=MibScalar
fanAndPsRedundantPSUStatus=_FanAndPsRedundantPSUStatus_Object((1,3,6,1,4,1,207,8,4,4,3,1,3),_FanAndPsRedundantPSUStatus_Type())
fanAndPsRedundantPSUStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fanAndPsRedundantPSUStatus.setStatus(_A)
class _FanAndPsRpsMonitoringStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('on',1),(_K,2)))
_FanAndPsRpsMonitoringStatus_Type.__name__=_C
_FanAndPsRpsMonitoringStatus_Object=MibScalar
fanAndPsRpsMonitoringStatus=_FanAndPsRpsMonitoringStatus_Object((1,3,6,1,4,1,207,8,4,4,3,1,4),_FanAndPsRpsMonitoringStatus_Type())
fanAndPsRpsMonitoringStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:fanAndPsRpsMonitoringStatus.setStatus(_A)
class _FanAndPsMainFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_E,0),(_F,1),(_G,2),('warning',3)))
_FanAndPsMainFanStatus_Type.__name__=_C
_FanAndPsMainFanStatus_Object=MibScalar
fanAndPsMainFanStatus=_FanAndPsMainFanStatus_Object((1,3,6,1,4,1,207,8,4,4,3,1,5),_FanAndPsMainFanStatus_Type())
fanAndPsMainFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fanAndPsMainFanStatus.setStatus(_A)
class _FanAndPsRedundantFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_E,0),(_F,1),(_G,2),(_J,3)))
_FanAndPsRedundantFanStatus_Type.__name__=_C
_FanAndPsRedundantFanStatus_Object=MibScalar
fanAndPsRedundantFanStatus=_FanAndPsRedundantFanStatus_Object((1,3,6,1,4,1,207,8,4,4,3,1,6),_FanAndPsRedundantFanStatus_Type())
fanAndPsRedundantFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fanAndPsRedundantFanStatus.setStatus(_A)
class _FanAndPsTemperatureStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FanAndPsTemperatureStatus_Type.__name__=_C
_FanAndPsTemperatureStatus_Object=MibScalar
fanAndPsTemperatureStatus=_FanAndPsTemperatureStatus_Object((1,3,6,1,4,1,207,8,4,4,3,1,7),_FanAndPsTemperatureStatus_Type())
fanAndPsTemperatureStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fanAndPsTemperatureStatus.setStatus(_A)
class _FanAndPsFanTrayPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('present',1),(_I,2)))
_FanAndPsFanTrayPresent_Type.__name__=_C
_FanAndPsFanTrayPresent_Object=MibScalar
fanAndPsFanTrayPresent=_FanAndPsFanTrayPresent_Object((1,3,6,1,4,1,207,8,4,4,3,1,8),_FanAndPsFanTrayPresent_Type())
fanAndPsFanTrayPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:fanAndPsFanTrayPresent.setStatus(_A)
class _FanAndPsFanTrayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_F,1),(_G,2)))
_FanAndPsFanTrayStatus_Type.__name__=_C
_FanAndPsFanTrayStatus_Object=MibScalar
fanAndPsFanTrayStatus=_FanAndPsFanTrayStatus_Object((1,3,6,1,4,1,207,8,4,4,3,1,9),_FanAndPsFanTrayStatus_Type())
fanAndPsFanTrayStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fanAndPsFanTrayStatus.setStatus(_A)
class _FanAndPsMainMonitoringStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_F,1),(_G,2)))
_FanAndPsMainMonitoringStatus_Type.__name__=_C
_FanAndPsMainMonitoringStatus_Object=MibScalar
fanAndPsMainMonitoringStatus=_FanAndPsMainMonitoringStatus_Object((1,3,6,1,4,1,207,8,4,4,3,1,10),_FanAndPsMainMonitoringStatus_Type())
fanAndPsMainMonitoringStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fanAndPsMainMonitoringStatus.setStatus(_A)
_FanAndPsPsuStatusTable_Object=MibTable
fanAndPsPsuStatusTable=_FanAndPsPsuStatusTable_Object((1,3,6,1,4,1,207,8,4,4,3,1,11))
if mibBuilder.loadTexts:fanAndPsPsuStatusTable.setStatus(_A)
_FanAndPsPsuStatusEntry_Object=MibTableRow
fanAndPsPsuStatusEntry=_FanAndPsPsuStatusEntry_Object((1,3,6,1,4,1,207,8,4,4,3,1,11,1))
fanAndPsPsuStatusEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:fanAndPsPsuStatusEntry.setStatus(_A)
class _FanAndPsPsuNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FanAndPsPsuNumber_Type.__name__=_C
_FanAndPsPsuNumber_Object=MibTableColumn
fanAndPsPsuNumber=_FanAndPsPsuNumber_Object((1,3,6,1,4,1,207,8,4,4,3,1,11,1,1),_FanAndPsPsuNumber_Type())
fanAndPsPsuNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fanAndPsPsuNumber.setStatus(_A)
class _FanAndPsPsuPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('yes',0),('no',1)))
_FanAndPsPsuPresent_Type.__name__=_C
_FanAndPsPsuPresent_Object=MibTableColumn
fanAndPsPsuPresent=_FanAndPsPsuPresent_Object((1,3,6,1,4,1,207,8,4,4,3,1,11,1,2),_FanAndPsPsuPresent_Type())
fanAndPsPsuPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:fanAndPsPsuPresent.setStatus(_A)
class _FanAndPsPsuType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('ac',0),('dc',1),('fan',2),(_I,3),(_E,4)))
_FanAndPsPsuType_Type.__name__=_C
_FanAndPsPsuType_Object=MibTableColumn
fanAndPsPsuType=_FanAndPsPsuType_Object((1,3,6,1,4,1,207,8,4,4,3,1,11,1,3),_FanAndPsPsuType_Type())
fanAndPsPsuType.setMaxAccess(_B)
if mibBuilder.loadTexts:fanAndPsPsuType.setStatus(_A)
class _FanAndPsPsuFan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),('fail',1),(_I,2),(_E,3)))
_FanAndPsPsuFan_Type.__name__=_C
_FanAndPsPsuFan_Object=MibTableColumn
fanAndPsPsuFan=_FanAndPsPsuFan_Object((1,3,6,1,4,1,207,8,4,4,3,1,11,1,4),_FanAndPsPsuFan_Type())
fanAndPsPsuFan.setMaxAccess(_B)
if mibBuilder.loadTexts:fanAndPsPsuFan.setStatus(_A)
class _FanAndPsPsuTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('good',0),('high',1),(_I,2),(_E,3)))
_FanAndPsPsuTemperature_Type.__name__=_C
_FanAndPsPsuTemperature_Object=MibTableColumn
fanAndPsPsuTemperature=_FanAndPsPsuTemperature_Object((1,3,6,1,4,1,207,8,4,4,3,1,11,1,5),_FanAndPsPsuTemperature_Type())
fanAndPsPsuTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:fanAndPsPsuTemperature.setStatus(_A)
class _FanAndPsPsuPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('good',0),('bad',1),(_I,2),(_E,3)))
_FanAndPsPsuPower_Type.__name__=_C
_FanAndPsPsuPower_Object=MibTableColumn
fanAndPsPsuPower=_FanAndPsPsuPower_Object((1,3,6,1,4,1,207,8,4,4,3,1,11,1,6),_FanAndPsPsuPower_Type())
fanAndPsPsuPower.setMaxAccess(_B)
if mibBuilder.loadTexts:fanAndPsPsuPower.setStatus(_A)
class _FanAndPsAccelFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_F,1),(_G,2)))
_FanAndPsAccelFanStatus_Type.__name__=_C
_FanAndPsAccelFanStatus_Object=MibScalar
fanAndPsAccelFanStatus=_FanAndPsAccelFanStatus_Object((1,3,6,1,4,1,207,8,4,4,3,1,12),_FanAndPsAccelFanStatus_Type())
fanAndPsAccelFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fanAndPsAccelFanStatus.setStatus(_A)
_RestartGroup_ObjectIdentity=ObjectIdentity
restartGroup=_RestartGroup_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,2))
class _Restart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('restartNone',0),('restartWarm',1),('restartCold',2)))
_Restart_Type.__name__=_C
_Restart_Object=MibScalar
restart=_Restart_Object((1,3,6,1,4,1,207,8,4,4,3,2,1),_Restart_Type())
restart.setMaxAccess(_H)
if mibBuilder.loadTexts:restart.setStatus(_A)
class _RestartCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_P,0),('hardwareReset',1),('hardwareWatchdog',2),('softwareRequest',3),('softwareException',4),('softwareInvalidImage',5),('softwareLicenceCheckFailure',6),('powerOnSelfTestfailure',7)))
_RestartCause_Type.__name__=_C
_RestartCause_Object=MibScalar
restartCause=_RestartCause_Object((1,3,6,1,4,1,207,8,4,4,3,2,2),_RestartCause_Type())
restartCause.setMaxAccess(_B)
if mibBuilder.loadTexts:restartCause.setStatus(_A)
class _RestartLog_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,500))
_RestartLog_Type.__name__=_N
_RestartLog_Object=MibScalar
restartLog=_RestartLog_Object((1,3,6,1,4,1,207,8,4,4,3,2,3),_RestartLog_Type())
restartLog.setMaxAccess(_B)
if mibBuilder.loadTexts:restartLog.setStatus(_A)
_Cpu_ObjectIdentity=ObjectIdentity
cpu=_Cpu_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,3))
class _CpuUtilisationMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CpuUtilisationMax_Type.__name__=_C
_CpuUtilisationMax_Object=MibScalar
cpuUtilisationMax=_CpuUtilisationMax_Object((1,3,6,1,4,1,207,8,4,4,3,3,1),_CpuUtilisationMax_Type())
cpuUtilisationMax.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuUtilisationMax.setStatus(_A)
class _CpuUtilisationAvg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CpuUtilisationAvg_Type.__name__=_C
_CpuUtilisationAvg_Object=MibScalar
cpuUtilisationAvg=_CpuUtilisationAvg_Object((1,3,6,1,4,1,207,8,4,4,3,3,2),_CpuUtilisationAvg_Type())
cpuUtilisationAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuUtilisationAvg.setStatus(_A)
class _CpuUtilisationAvgLastMinute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CpuUtilisationAvgLastMinute_Type.__name__=_C
_CpuUtilisationAvgLastMinute_Object=MibScalar
cpuUtilisationAvgLastMinute=_CpuUtilisationAvgLastMinute_Object((1,3,6,1,4,1,207,8,4,4,3,3,3),_CpuUtilisationAvgLastMinute_Type())
cpuUtilisationAvgLastMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuUtilisationAvgLastMinute.setStatus(_A)
class _CpuUtilisationAvgLast10Seconds_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CpuUtilisationAvgLast10Seconds_Type.__name__=_C
_CpuUtilisationAvgLast10Seconds_Object=MibScalar
cpuUtilisationAvgLast10Seconds=_CpuUtilisationAvgLast10Seconds_Object((1,3,6,1,4,1,207,8,4,4,3,3,4),_CpuUtilisationAvgLast10Seconds_Type())
cpuUtilisationAvgLast10Seconds.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuUtilisationAvgLast10Seconds.setStatus(_A)
class _CpuUtilisationAvgLastSecond_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CpuUtilisationAvgLastSecond_Type.__name__=_C
_CpuUtilisationAvgLastSecond_Object=MibScalar
cpuUtilisationAvgLastSecond=_CpuUtilisationAvgLastSecond_Object((1,3,6,1,4,1,207,8,4,4,3,3,5),_CpuUtilisationAvgLastSecond_Type())
cpuUtilisationAvgLastSecond.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuUtilisationAvgLastSecond.setStatus(_A)
class _CpuUtilisationMaxLast5Minutes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CpuUtilisationMaxLast5Minutes_Type.__name__=_C
_CpuUtilisationMaxLast5Minutes_Object=MibScalar
cpuUtilisationMaxLast5Minutes=_CpuUtilisationMaxLast5Minutes_Object((1,3,6,1,4,1,207,8,4,4,3,3,6),_CpuUtilisationMaxLast5Minutes_Type())
cpuUtilisationMaxLast5Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuUtilisationMaxLast5Minutes.setStatus(_A)
class _CpuUtilisationAvgLast5Minutes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CpuUtilisationAvgLast5Minutes_Type.__name__=_C
_CpuUtilisationAvgLast5Minutes_Object=MibScalar
cpuUtilisationAvgLast5Minutes=_CpuUtilisationAvgLast5Minutes_Object((1,3,6,1,4,1,207,8,4,4,3,3,7),_CpuUtilisationAvgLast5Minutes_Type())
cpuUtilisationAvgLast5Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuUtilisationAvgLast5Minutes.setStatus(_A)
_SysTemperature_ObjectIdentity=ObjectIdentity
sysTemperature=_SysTemperature_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,4))
_GeneralTemperature_ObjectIdentity=ObjectIdentity
generalTemperature=_GeneralTemperature_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,4,1))
_GeneralTemperatureTrap_ObjectIdentity=ObjectIdentity
generalTemperatureTrap=_GeneralTemperatureTrap_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,4,1,0))
class _GeneralTemperatureSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_Q,1)))
_GeneralTemperatureSupported_Type.__name__=_C
_GeneralTemperatureSupported_Object=MibScalar
generalTemperatureSupported=_GeneralTemperatureSupported_Object((1,3,6,1,4,1,207,8,4,4,3,4,1,1),_GeneralTemperatureSupported_Type())
generalTemperatureSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:generalTemperatureSupported.setStatus(_A)
_GeneralTemperatureActualTemp_Type=Integer32
_GeneralTemperatureActualTemp_Object=MibScalar
generalTemperatureActualTemp=_GeneralTemperatureActualTemp_Object((1,3,6,1,4,1,207,8,4,4,3,4,1,2),_GeneralTemperatureActualTemp_Type())
generalTemperatureActualTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:generalTemperatureActualTemp.setStatus(_A)
class _GeneralTemperatureStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_GeneralTemperatureStatus_Type.__name__=_C
_GeneralTemperatureStatus_Object=MibScalar
generalTemperatureStatus=_GeneralTemperatureStatus_Object((1,3,6,1,4,1,207,8,4,4,3,4,1,3),_GeneralTemperatureStatus_Type())
generalTemperatureStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:generalTemperatureStatus.setStatus(_A)
_GeneralTemperatureThreshold_Type=Integer32
_GeneralTemperatureThreshold_Object=MibScalar
generalTemperatureThreshold=_GeneralTemperatureThreshold_Object((1,3,6,1,4,1,207,8,4,4,3,4,1,4),_GeneralTemperatureThreshold_Type())
generalTemperatureThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:generalTemperatureThreshold.setStatus(_A)
_SbTemperature_ObjectIdentity=ObjectIdentity
sbTemperature=_SbTemperature_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,4,2))
_SbTemperatureTrap_ObjectIdentity=ObjectIdentity
sbTemperatureTrap=_SbTemperatureTrap_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,4,2,0))
_SbTempTable_Object=MibTable
sbTempTable=_SbTempTable_Object((1,3,6,1,4,1,207,8,4,4,3,4,2,1))
if mibBuilder.loadTexts:sbTempTable.setStatus(_A)
_SbTempEntry_Object=MibTableRow
sbTempEntry=_SbTempEntry_Object((1,3,6,1,4,1,207,8,4,4,3,4,2,1,1))
sbTempEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:sbTempEntry.setStatus(_A)
class _SbTempIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('master',1),('slave',2)))
_SbTempIndex_Type.__name__=_C
_SbTempIndex_Object=MibTableColumn
sbTempIndex=_SbTempIndex_Object((1,3,6,1,4,1,207,8,4,4,3,4,2,1,1,1),_SbTempIndex_Type())
sbTempIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sbTempIndex.setStatus(_A)
_SbTempActualTemperature_Type=Integer32
_SbTempActualTemperature_Object=MibTableColumn
sbTempActualTemperature=_SbTempActualTemperature_Object((1,3,6,1,4,1,207,8,4,4,3,4,2,1,1,2),_SbTempActualTemperature_Type())
sbTempActualTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:sbTempActualTemperature.setStatus(_A)
class _SbTempFixedThresholdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_S,2)))
_SbTempFixedThresholdStatus_Type.__name__=_C
_SbTempFixedThresholdStatus_Object=MibTableColumn
sbTempFixedThresholdStatus=_SbTempFixedThresholdStatus_Object((1,3,6,1,4,1,207,8,4,4,3,4,2,1,1,3),_SbTempFixedThresholdStatus_Type())
sbTempFixedThresholdStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sbTempFixedThresholdStatus.setStatus(_A)
class _SbTempSettableThresholdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_S,2),('undefined',3)))
_SbTempSettableThresholdStatus_Type.__name__=_C
_SbTempSettableThresholdStatus_Object=MibTableColumn
sbTempSettableThresholdStatus=_SbTempSettableThresholdStatus_Object((1,3,6,1,4,1,207,8,4,4,3,4,2,1,1,4),_SbTempSettableThresholdStatus_Type())
sbTempSettableThresholdStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sbTempSettableThresholdStatus.setStatus(_A)
class _SbTempSettableThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,100))
_SbTempSettableThreshold_Type.__name__=_C
_SbTempSettableThreshold_Object=MibTableColumn
sbTempSettableThreshold=_SbTempSettableThreshold_Object((1,3,6,1,4,1,207,8,4,4,3,4,2,1,1,5),_SbTempSettableThreshold_Type())
sbTempSettableThreshold.setMaxAccess(_H)
if mibBuilder.loadTexts:sbTempSettableThreshold.setStatus(_A)
_SbTempFixedThreshold_Type=Integer32
_SbTempFixedThreshold_Object=MibScalar
sbTempFixedThreshold=_SbTempFixedThreshold_Object((1,3,6,1,4,1,207,8,4,4,3,4,2,2),_SbTempFixedThreshold_Type())
sbTempFixedThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:sbTempFixedThreshold.setStatus(_A)
_AcceleratorTemperature_ObjectIdentity=ObjectIdentity
acceleratorTemperature=_AcceleratorTemperature_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,4,3))
_AcceleratorTemperatureTrap_ObjectIdentity=ObjectIdentity
acceleratorTemperatureTrap=_AcceleratorTemperatureTrap_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,4,3,0))
class _AcceleratorTemperatureSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_Q,1)))
_AcceleratorTemperatureSupported_Type.__name__=_C
_AcceleratorTemperatureSupported_Object=MibScalar
acceleratorTemperatureSupported=_AcceleratorTemperatureSupported_Object((1,3,6,1,4,1,207,8,4,4,3,4,3,1),_AcceleratorTemperatureSupported_Type())
acceleratorTemperatureSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:acceleratorTemperatureSupported.setStatus(_A)
_AcceleratorTemperatureActualTemp_Type=Integer32
_AcceleratorTemperatureActualTemp_Object=MibScalar
acceleratorTemperatureActualTemp=_AcceleratorTemperatureActualTemp_Object((1,3,6,1,4,1,207,8,4,4,3,4,3,2),_AcceleratorTemperatureActualTemp_Type())
acceleratorTemperatureActualTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:acceleratorTemperatureActualTemp.setStatus(_A)
class _AcceleratorTemperatureStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AcceleratorTemperatureStatus_Type.__name__=_C
_AcceleratorTemperatureStatus_Object=MibScalar
acceleratorTemperatureStatus=_AcceleratorTemperatureStatus_Object((1,3,6,1,4,1,207,8,4,4,3,4,3,3),_AcceleratorTemperatureStatus_Type())
acceleratorTemperatureStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:acceleratorTemperatureStatus.setStatus(_A)
_AcceleratorTemperatureThreshold_Type=Integer32
_AcceleratorTemperatureThreshold_Object=MibScalar
acceleratorTemperatureThreshold=_AcceleratorTemperatureThreshold_Object((1,3,6,1,4,1,207,8,4,4,3,4,3,4),_AcceleratorTemperatureThreshold_Type())
acceleratorTemperatureThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:acceleratorTemperatureThreshold.setStatus(_A)
_AtContactDetails_Type=DisplayString
_AtContactDetails_Object=MibScalar
atContactDetails=_AtContactDetails_Object((1,3,6,1,4,1,207,8,4,4,3,5),_AtContactDetails_Type())
atContactDetails.setMaxAccess(_B)
if mibBuilder.loadTexts:atContactDetails.setStatus(_A)
_BbrNvs_ObjectIdentity=ObjectIdentity
bbrNvs=_BbrNvs_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,6))
_BbrNvsTrap_ObjectIdentity=ObjectIdentity
bbrNvsTrap=_BbrNvsTrap_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,6,0))
_Memory_ObjectIdentity=ObjectIdentity
memory=_Memory_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,7))
class _FreeMemory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FreeMemory_Type.__name__=_C
_FreeMemory_Object=MibScalar
freeMemory=_FreeMemory_Object((1,3,6,1,4,1,207,8,4,4,3,7,1),_FreeMemory_Type())
freeMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:freeMemory.setStatus(_A)
_TotalBuffers_Type=Integer32
_TotalBuffers_Object=MibScalar
totalBuffers=_TotalBuffers_Object((1,3,6,1,4,1,207,8,4,4,3,7,2),_TotalBuffers_Type())
totalBuffers.setMaxAccess(_B)
if mibBuilder.loadTexts:totalBuffers.setStatus(_A)
class _RealTimeClockStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('invalid',0),(_L,1)))
_RealTimeClockStatus_Type.__name__=_C
_RealTimeClockStatus_Object=MibScalar
realTimeClockStatus=_RealTimeClockStatus_Object((1,3,6,1,4,1,207,8,4,4,3,8),_RealTimeClockStatus_Type())
realTimeClockStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:realTimeClockStatus.setStatus(_A)
class _HostId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_HostId_Type.__name__=_C
_HostId_Object=MibScalar
hostId=_HostId_Object((1,3,6,1,4,1,207,8,4,4,3,9),_HostId_Type())
hostId.setMaxAccess(_H)
if mibBuilder.loadTexts:hostId.setStatus(_A)
_AtPortInfo_ObjectIdentity=ObjectIdentity
atPortInfo=_AtPortInfo_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,14))
_AtPortInfoTransceiverTable_Object=MibTable
atPortInfoTransceiverTable=_AtPortInfoTransceiverTable_Object((1,3,6,1,4,1,207,8,4,4,3,14,1))
if mibBuilder.loadTexts:atPortInfoTransceiverTable.setStatus(_A)
_AtPortInfoTransceiverEntry_Object=MibTableRow
atPortInfoTransceiverEntry=_AtPortInfoTransceiverEntry_Object((1,3,6,1,4,1,207,8,4,4,3,14,1,1))
atPortInfoTransceiverEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:atPortInfoTransceiverEntry.setStatus(_A)
_AtPortInfoTransceiverifIndex_Type=InterfaceIndex
_AtPortInfoTransceiverifIndex_Object=MibTableColumn
atPortInfoTransceiverifIndex=_AtPortInfoTransceiverifIndex_Object((1,3,6,1,4,1,207,8,4,4,3,14,1,1,1),_AtPortInfoTransceiverifIndex_Type())
atPortInfoTransceiverifIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atPortInfoTransceiverifIndex.setStatus(_A)
class _AtPortInfoTransceiverType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33)));namedValues=NamedValues(*(('rj45',1),('sfp-px',2),('sfp-bx10',3),('sfp-fx',4),('sfp-100base-lx',5),('sfp-t',6),('sfp-cx',7),('sfp-zx-cwdm',8),('sfp-lx',9),('sfp-sx',10),('sfp-oc3-lr',11),('sfp-oc3-ir',12),('sfp-oc3-mm',13),('xfp-srsw',14),('xfp-lrlw',15),('xfp-erew',16),('xfp-sr',17),('xfp-lr',18),('xfp-er',19),('xfp-lrm',20),('xfp-sw',21),('xfp-lw',22),('xfp-ew',23),(_P,24),('empty',25),('sfpp-sr',26),('sfpp-lr',27),('sfpp-er',28),('sfpp-lrm',29),('inf-1-x-copper-pasv',30),('inf-1-x-copper-actv',31),('inf-1-x-lx',32),('inf-1-x-sx',33)))
_AtPortInfoTransceiverType_Type.__name__=_C
_AtPortInfoTransceiverType_Object=MibTableColumn
atPortInfoTransceiverType=_AtPortInfoTransceiverType_Object((1,3,6,1,4,1,207,8,4,4,3,14,1,1,2),_AtPortInfoTransceiverType_Type())
atPortInfoTransceiverType.setMaxAccess(_B)
if mibBuilder.loadTexts:atPortInfoTransceiverType.setStatus(_A)
_AtPortRenumberEvents_Type=Integer32
_AtPortRenumberEvents_Object=MibScalar
atPortRenumberEvents=_AtPortRenumberEvents_Object((1,3,6,1,4,1,207,8,4,4,3,14,2),_AtPortRenumberEvents_Type())
atPortRenumberEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:atPortRenumberEvents.setStatus(_A)
fanAndPsRpsConnectionTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,3,1,0,1))
fanAndPsRpsConnectionTrap.setObjects((_D,_U))
if mibBuilder.loadTexts:fanAndPsRpsConnectionTrap.setStatus(_A)
fanAndPsMainPSUStatusTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,3,1,0,2))
fanAndPsMainPSUStatusTrap.setObjects((_D,_V))
if mibBuilder.loadTexts:fanAndPsMainPSUStatusTrap.setStatus(_A)
fanAndPsRedundantPSUStatusTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,3,1,0,3))
fanAndPsRedundantPSUStatusTrap.setObjects((_D,_W))
if mibBuilder.loadTexts:fanAndPsRedundantPSUStatusTrap.setStatus(_A)
fanAndPsMainFanStatusTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,3,1,0,4))
fanAndPsMainFanStatusTrap.setObjects((_D,_X))
if mibBuilder.loadTexts:fanAndPsMainFanStatusTrap.setStatus(_A)
fanAndPsRedundantFanStatusTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,3,1,0,5))
fanAndPsRedundantFanStatusTrap.setObjects((_D,_Y))
if mibBuilder.loadTexts:fanAndPsRedundantFanStatusTrap.setStatus(_A)
fanAndPsTemperatureStatusTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,3,1,0,6))
fanAndPsTemperatureStatusTrap.setObjects((_D,_Z))
if mibBuilder.loadTexts:fanAndPsTemperatureStatusTrap.setStatus(_A)
fanAndPsFanTrayPresentTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,3,1,0,7))
fanAndPsFanTrayPresentTrap.setObjects((_D,_a))
if mibBuilder.loadTexts:fanAndPsFanTrayPresentTrap.setStatus(_A)
fanAndPsFanTrayStatusTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,3,1,0,8))
fanAndPsFanTrayStatusTrap.setObjects((_D,_b))
if mibBuilder.loadTexts:fanAndPsFanTrayStatusTrap.setStatus(_A)
fanAndPsMainMonitoringStatusTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,3,1,0,9))
fanAndPsMainMonitoringStatusTrap.setObjects((_D,_c))
if mibBuilder.loadTexts:fanAndPsMainMonitoringStatusTrap.setStatus(_A)
fanAndPsAccelFanStatusTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,3,1,0,10))
fanAndPsAccelFanStatusTrap.setObjects((_D,_d))
if mibBuilder.loadTexts:fanAndPsAccelFanStatusTrap.setStatus(_A)
restartNotification=NotificationType((1,3,6,1,4,1,207,8,4,4,3,2,11))
restartNotification.setObjects((_D,_e))
if mibBuilder.loadTexts:restartNotification.setStatus(_A)
generalTemperatureStatusTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,3,4,1,0,1))
generalTemperatureStatusTrap.setObjects(*((_D,_f),(_D,_g),(_D,_h)))
if mibBuilder.loadTexts:generalTemperatureStatusTrap.setStatus(_A)
sbTempFixedThresholdTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,3,4,2,0,1))
sbTempFixedThresholdTrap.setObjects(*((_D,_i),(_D,_M),(_D,_j)))
if mibBuilder.loadTexts:sbTempFixedThresholdTrap.setStatus(_A)
sbTempSettableThresholdTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,3,4,2,0,2))
sbTempSettableThresholdTrap.setObjects(*((_D,_k),(_D,_M),(_D,_l)))
if mibBuilder.loadTexts:sbTempSettableThresholdTrap.setStatus(_A)
acceleratorTemperatureStatusTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,3,4,3,0,1))
acceleratorTemperatureStatusTrap.setObjects((_D,_m))
if mibBuilder.loadTexts:acceleratorTemperatureStatusTrap.setStatus(_A)
bbrNvsReinitialiseTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,3,6,0,1))
if mibBuilder.loadTexts:bbrNvsReinitialiseTrap.setStatus(_A)
lowMemoryTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,3,7,11))
lowMemoryTrap.setObjects(*((_D,_n),(_D,_o)))
if mibBuilder.loadTexts:lowMemoryTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'sysinfo':sysinfo,'fanAndPs':fanAndPs,'fanAndPsTrap':fanAndPsTrap,'fanAndPsRpsConnectionTrap':fanAndPsRpsConnectionTrap,'fanAndPsMainPSUStatusTrap':fanAndPsMainPSUStatusTrap,'fanAndPsRedundantPSUStatusTrap':fanAndPsRedundantPSUStatusTrap,'fanAndPsMainFanStatusTrap':fanAndPsMainFanStatusTrap,'fanAndPsRedundantFanStatusTrap':fanAndPsRedundantFanStatusTrap,'fanAndPsTemperatureStatusTrap':fanAndPsTemperatureStatusTrap,'fanAndPsFanTrayPresentTrap':fanAndPsFanTrayPresentTrap,'fanAndPsFanTrayStatusTrap':fanAndPsFanTrayStatusTrap,'fanAndPsMainMonitoringStatusTrap':fanAndPsMainMonitoringStatusTrap,'fanAndPsAccelFanStatusTrap':fanAndPsAccelFanStatusTrap,_U:fanAndPsRpsConnectionStatus,_V:fanAndPsMainPSUStatus,_W:fanAndPsRedundantPSUStatus,'fanAndPsRpsMonitoringStatus':fanAndPsRpsMonitoringStatus,_X:fanAndPsMainFanStatus,_Y:fanAndPsRedundantFanStatus,_Z:fanAndPsTemperatureStatus,_a:fanAndPsFanTrayPresent,_b:fanAndPsFanTrayStatus,_c:fanAndPsMainMonitoringStatus,'fanAndPsPsuStatusTable':fanAndPsPsuStatusTable,'fanAndPsPsuStatusEntry':fanAndPsPsuStatusEntry,_O:fanAndPsPsuNumber,'fanAndPsPsuPresent':fanAndPsPsuPresent,'fanAndPsPsuType':fanAndPsPsuType,'fanAndPsPsuFan':fanAndPsPsuFan,'fanAndPsPsuTemperature':fanAndPsPsuTemperature,'fanAndPsPsuPower':fanAndPsPsuPower,_d:fanAndPsAccelFanStatus,'restartGroup':restartGroup,'restart':restart,_e:restartCause,'restartLog':restartLog,'restartNotification':restartNotification,'cpu':cpu,'cpuUtilisationMax':cpuUtilisationMax,'cpuUtilisationAvg':cpuUtilisationAvg,'cpuUtilisationAvgLastMinute':cpuUtilisationAvgLastMinute,'cpuUtilisationAvgLast10Seconds':cpuUtilisationAvgLast10Seconds,'cpuUtilisationAvgLastSecond':cpuUtilisationAvgLastSecond,'cpuUtilisationMaxLast5Minutes':cpuUtilisationMaxLast5Minutes,'cpuUtilisationAvgLast5Minutes':cpuUtilisationAvgLast5Minutes,'sysTemperature':sysTemperature,'generalTemperature':generalTemperature,'generalTemperatureTrap':generalTemperatureTrap,'generalTemperatureStatusTrap':generalTemperatureStatusTrap,'generalTemperatureSupported':generalTemperatureSupported,_g:generalTemperatureActualTemp,_f:generalTemperatureStatus,_h:generalTemperatureThreshold,'sbTemperature':sbTemperature,'sbTemperatureTrap':sbTemperatureTrap,'sbTempFixedThresholdTrap':sbTempFixedThresholdTrap,'sbTempSettableThresholdTrap':sbTempSettableThresholdTrap,'sbTempTable':sbTempTable,'sbTempEntry':sbTempEntry,_R:sbTempIndex,_M:sbTempActualTemperature,_i:sbTempFixedThresholdStatus,_k:sbTempSettableThresholdStatus,_l:sbTempSettableThreshold,_j:sbTempFixedThreshold,'acceleratorTemperature':acceleratorTemperature,'acceleratorTemperatureTrap':acceleratorTemperatureTrap,'acceleratorTemperatureStatusTrap':acceleratorTemperatureStatusTrap,'acceleratorTemperatureSupported':acceleratorTemperatureSupported,'acceleratorTemperatureActualTemp':acceleratorTemperatureActualTemp,_m:acceleratorTemperatureStatus,'acceleratorTemperatureThreshold':acceleratorTemperatureThreshold,'atContactDetails':atContactDetails,'bbrNvs':bbrNvs,'bbrNvsTrap':bbrNvsTrap,'bbrNvsReinitialiseTrap':bbrNvsReinitialiseTrap,'memory':memory,_n:freeMemory,_o:totalBuffers,'lowMemoryTrap':lowMemoryTrap,'realTimeClockStatus':realTimeClockStatus,'hostId':hostId,'atPortInfo':atPortInfo,'atPortInfoTransceiverTable':atPortInfoTransceiverTable,'atPortInfoTransceiverEntry':atPortInfoTransceiverEntry,_T:atPortInfoTransceiverifIndex,'atPortInfoTransceiverType':atPortInfoTransceiverType,'atPortRenumberEvents':atPortRenumberEvents})