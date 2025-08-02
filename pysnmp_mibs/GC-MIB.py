_H='cpuIndivIndex'
_G='not-accessible'
_F='procIndex'
_E='Integer32'
_D='procName'
_C='GC-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
products,=mibBuilder.importSymbols('RBT-MIB','products')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
gc=ModuleIdentity((1,3,6,1,4,1,17163,1,100))
if mibBuilder.loadTexts:gc.setRevisions(('2014-12-09 00:00',))
_System_ObjectIdentity=ObjectIdentity
system=_System_ObjectIdentity((1,3,6,1,4,1,17163,1,100,1))
_Model_Type=OctetString
_Model_Object=MibScalar
model=_Model_Object((1,3,6,1,4,1,17163,1,100,1,1),_Model_Type())
model.setMaxAccess(_B)
if mibBuilder.loadTexts:model.setStatus(_A)
_SerialNumber_Type=OctetString
_SerialNumber_Object=MibScalar
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,17163,1,100,1,2),_SerialNumber_Type())
serialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:serialNumber.setStatus(_A)
_SystemVersion_Type=OctetString
_SystemVersion_Object=MibScalar
systemVersion=_SystemVersion_Object((1,3,6,1,4,1,17163,1,100,1,3),_SystemVersion_Type())
systemVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:systemVersion.setStatus(_A)
_Status_ObjectIdentity=ObjectIdentity
status=_Status_ObjectIdentity((1,3,6,1,4,1,17163,1,100,2))
_SystemClock_Type=DateAndTime
_SystemClock_Object=MibScalar
systemClock=_SystemClock_Object((1,3,6,1,4,1,17163,1,100,2,1),_SystemClock_Type())
systemClock.setMaxAccess(_B)
if mibBuilder.loadTexts:systemClock.setStatus(_A)
_Health_Type=OctetString
_Health_Object=MibScalar
health=_Health_Object((1,3,6,1,4,1,17163,1,100,2,2),_Health_Type())
health.setMaxAccess(_B)
if mibBuilder.loadTexts:health.setStatus(_A)
class _SystemHealth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10000,30000,50000)));namedValues=NamedValues(*(('healthy',10000),('degraded',30000),('critical',50000)))
_SystemHealth_Type.__name__=_E
_SystemHealth_Object=MibScalar
systemHealth=_SystemHealth_Object((1,3,6,1,4,1,17163,1,100,2,3),_SystemHealth_Type())
systemHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:systemHealth.setStatus(_A)
_SystemTemperature_Type=Unsigned32
_SystemTemperature_Object=MibScalar
systemTemperature=_SystemTemperature_Object((1,3,6,1,4,1,17163,1,100,2,4),_SystemTemperature_Type())
systemTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:systemTemperature.setStatus(_A)
_ProcTable_Object=MibTable
procTable=_ProcTable_Object((1,3,6,1,4,1,17163,1,100,2,11))
if mibBuilder.loadTexts:procTable.setStatus(_A)
_ProcEntry_Object=MibTableRow
procEntry=_ProcEntry_Object((1,3,6,1,4,1,17163,1,100,2,11,1))
procEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:procEntry.setStatus(_A)
_ProcIndex_Type=Unsigned32
_ProcIndex_Object=MibTableColumn
procIndex=_ProcIndex_Object((1,3,6,1,4,1,17163,1,100,2,11,1,1),_ProcIndex_Type())
procIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:procIndex.setStatus(_A)
_ProcName_Type=OctetString
_ProcName_Object=MibTableColumn
procName=_ProcName_Object((1,3,6,1,4,1,17163,1,100,2,11,1,2),_ProcName_Type())
procName.setMaxAccess(_B)
if mibBuilder.loadTexts:procName.setStatus(_A)
_ProcStatus_Type=OctetString
_ProcStatus_Object=MibTableColumn
procStatus=_ProcStatus_Object((1,3,6,1,4,1,17163,1,100,2,11,1,3),_ProcStatus_Type())
procStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:procStatus.setStatus(_A)
_ProcNumFailures_Type=Unsigned32
_ProcNumFailures_Object=MibTableColumn
procNumFailures=_ProcNumFailures_Object((1,3,6,1,4,1,17163,1,100,2,11,1,4),_ProcNumFailures_Type())
procNumFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:procNumFailures.setStatus(_A)
_Config_ObjectIdentity=ObjectIdentity
config=_Config_ObjectIdentity((1,3,6,1,4,1,17163,1,100,3))
_ActiveConfig_Type=OctetString
_ActiveConfig_Object=MibScalar
activeConfig=_ActiveConfig_Object((1,3,6,1,4,1,17163,1,100,3,1),_ActiveConfig_Type())
activeConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:activeConfig.setStatus(_A)
_Alarms_ObjectIdentity=ObjectIdentity
alarms=_Alarms_ObjectIdentity((1,3,6,1,4,1,17163,1,100,4))
_AlarmsPrefix_ObjectIdentity=ObjectIdentity
alarmsPrefix=_AlarmsPrefix_ObjectIdentity((1,3,6,1,4,1,17163,1,100,4,0))
_Statistics_ObjectIdentity=ObjectIdentity
statistics=_Statistics_ObjectIdentity((1,3,6,1,4,1,17163,1,100,5))
_CpuLoad_ObjectIdentity=ObjectIdentity
cpuLoad=_CpuLoad_ObjectIdentity((1,3,6,1,4,1,17163,1,100,5,1))
_CpuLoad1_Type=Unsigned32
_CpuLoad1_Object=MibScalar
cpuLoad1=_CpuLoad1_Object((1,3,6,1,4,1,17163,1,100,5,1,1),_CpuLoad1_Type())
cpuLoad1.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuLoad1.setStatus(_A)
_CpuLoad5_Type=Unsigned32
_CpuLoad5_Object=MibScalar
cpuLoad5=_CpuLoad5_Object((1,3,6,1,4,1,17163,1,100,5,1,2),_CpuLoad5_Type())
cpuLoad5.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuLoad5.setStatus(_A)
_CpuLoad15_Type=Unsigned32
_CpuLoad15_Object=MibScalar
cpuLoad15=_CpuLoad15_Object((1,3,6,1,4,1,17163,1,100,5,1,3),_CpuLoad15_Type())
cpuLoad15.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuLoad15.setStatus(_A)
_CpuUtil1_Type=Unsigned32
_CpuUtil1_Object=MibScalar
cpuUtil1=_CpuUtil1_Object((1,3,6,1,4,1,17163,1,100,5,1,4),_CpuUtil1_Type())
cpuUtil1.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuUtil1.setStatus(_A)
_CpuIndivUtilTable_Object=MibTable
cpuIndivUtilTable=_CpuIndivUtilTable_Object((1,3,6,1,4,1,17163,1,100,5,1,5))
if mibBuilder.loadTexts:cpuIndivUtilTable.setStatus(_A)
_CpuIndivUtilEntry_Object=MibTableRow
cpuIndivUtilEntry=_CpuIndivUtilEntry_Object((1,3,6,1,4,1,17163,1,100,5,1,5,1))
cpuIndivUtilEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cpuIndivUtilEntry.setStatus(_A)
_CpuIndivIndex_Type=Unsigned32
_CpuIndivIndex_Object=MibTableColumn
cpuIndivIndex=_CpuIndivIndex_Object((1,3,6,1,4,1,17163,1,100,5,1,5,1,1),_CpuIndivIndex_Type())
cpuIndivIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cpuIndivIndex.setStatus(_A)
_CpuIndivId_Type=Unsigned32
_CpuIndivId_Object=MibTableColumn
cpuIndivId=_CpuIndivId_Object((1,3,6,1,4,1,17163,1,100,5,1,5,1,2),_CpuIndivId_Type())
cpuIndivId.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuIndivId.setStatus(_A)
_CpuIndivIdleTime_Type=Unsigned32
_CpuIndivIdleTime_Object=MibTableColumn
cpuIndivIdleTime=_CpuIndivIdleTime_Object((1,3,6,1,4,1,17163,1,100,5,1,5,1,3),_CpuIndivIdleTime_Type())
cpuIndivIdleTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuIndivIdleTime.setStatus(_A)
_CpuIndivSystemTime_Type=Unsigned32
_CpuIndivSystemTime_Object=MibTableColumn
cpuIndivSystemTime=_CpuIndivSystemTime_Object((1,3,6,1,4,1,17163,1,100,5,1,5,1,4),_CpuIndivSystemTime_Type())
cpuIndivSystemTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuIndivSystemTime.setStatus(_A)
_CpuIndivUserTime_Type=Unsigned32
_CpuIndivUserTime_Object=MibTableColumn
cpuIndivUserTime=_CpuIndivUserTime_Object((1,3,6,1,4,1,17163,1,100,5,1,5,1,5),_CpuIndivUserTime_Type())
cpuIndivUserTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuIndivUserTime.setStatus(_A)
procCrash=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,1))
procCrash.setObjects((_C,_D))
if mibBuilder.loadTexts:procCrash.setStatus(_A)
procExit=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,2))
procExit.setObjects((_C,_D))
if mibBuilder.loadTexts:procExit.setStatus(_A)
configChange=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,3))
if mibBuilder.loadTexts:configChange.setStatus(_A)
cpuUtil=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,4))
if mibBuilder.loadTexts:cpuUtil.setStatus(_A)
pagingActivity=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,5))
if mibBuilder.loadTexts:pagingActivity.setStatus(_A)
linkError=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,6))
if mibBuilder.loadTexts:linkError.setStatus(_A)
powerSupplyError=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,7))
if mibBuilder.loadTexts:powerSupplyError.setStatus(_A)
fanError=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,8))
if mibBuilder.loadTexts:fanError.setStatus(_A)
memoryError=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,9))
if mibBuilder.loadTexts:memoryError.setStatus(_A)
ipmi=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,10))
if mibBuilder.loadTexts:ipmi.setStatus(_A)
localFSFull=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,11))
if mibBuilder.loadTexts:localFSFull.setStatus(_A)
temperatureCritical=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,12))
if mibBuilder.loadTexts:temperatureCritical.setStatus(_A)
temperatureWarning=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,13))
if mibBuilder.loadTexts:temperatureWarning.setStatus(_A)
scheduledJobError=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,14))
if mibBuilder.loadTexts:scheduledJobError.setStatus(_A)
confModeEnter=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,15))
if mibBuilder.loadTexts:confModeEnter.setStatus(_A)
confModeExit=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,16))
if mibBuilder.loadTexts:confModeExit.setStatus(_A)
secureVaultLocked=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,17))
if mibBuilder.loadTexts:secureVaultLocked.setStatus(_A)
procRestart=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,18))
procRestart.setObjects((_C,_D))
if mibBuilder.loadTexts:procRestart.setStatus(_A)
testTrap=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,19))
testTrap.setObjects((_C,_D))
if mibBuilder.loadTexts:testTrap.setStatus(_A)
cpuUtilClear=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,1004))
if mibBuilder.loadTexts:cpuUtilClear.setStatus(_A)
pagingActivityClear=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,1005))
if mibBuilder.loadTexts:pagingActivityClear.setStatus(_A)
linkErrorClear=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,1006))
if mibBuilder.loadTexts:linkErrorClear.setStatus(_A)
powerSupplyErrorClear=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,1007))
if mibBuilder.loadTexts:powerSupplyErrorClear.setStatus(_A)
fanErrorClear=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,1008))
if mibBuilder.loadTexts:fanErrorClear.setStatus(_A)
memoryErrorClear=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,1009))
if mibBuilder.loadTexts:memoryErrorClear.setStatus(_A)
ipmiClear=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,1010))
if mibBuilder.loadTexts:ipmiClear.setStatus(_A)
localFSFullClear=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,1011))
if mibBuilder.loadTexts:localFSFullClear.setStatus(_A)
temperatureNonCritical=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,1012))
if mibBuilder.loadTexts:temperatureNonCritical.setStatus(_A)
temperatureNormal=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,1013))
if mibBuilder.loadTexts:temperatureNormal.setStatus(_A)
secureVaultUnlocked=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,1017))
if mibBuilder.loadTexts:secureVaultUnlocked.setStatus(_A)
edgeError=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,10500))
if mibBuilder.loadTexts:edgeError.setStatus(_A)
highAvailabilityError=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,10501))
if mibBuilder.loadTexts:highAvailabilityError.setStatus(_A)
lunError=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,10502))
if mibBuilder.loadTexts:lunError.setStatus(_A)
iscsiError=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,10503))
if mibBuilder.loadTexts:iscsiError.setStatus(_A)
snapshotError=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,10505))
if mibBuilder.loadTexts:snapshotError.setStatus(_A)
applianceUnlicensedError=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,10506))
if mibBuilder.loadTexts:applianceUnlicensedError.setStatus(_A)
modelUnlicensedError=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,10507))
if mibBuilder.loadTexts:modelUnlicensedError.setStatus(_A)
blkdiskError=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,10508))
if mibBuilder.loadTexts:blkdiskError.setStatus(_A)
backupIntegrationError=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,10509))
if mibBuilder.loadTexts:backupIntegrationError.setStatus(_A)
otherHardwareError=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,10510))
if mibBuilder.loadTexts:otherHardwareError.setStatus(_A)
edgeClear=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,11500))
if mibBuilder.loadTexts:edgeClear.setStatus(_A)
highAvailabilityClear=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,11501))
if mibBuilder.loadTexts:highAvailabilityClear.setStatus(_A)
lunClear=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,11502))
if mibBuilder.loadTexts:lunClear.setStatus(_A)
iscsiClear=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,11503))
if mibBuilder.loadTexts:iscsiClear.setStatus(_A)
snapshotClear=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,11505))
if mibBuilder.loadTexts:snapshotClear.setStatus(_A)
applianceUnlicensedClear=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,11506))
if mibBuilder.loadTexts:applianceUnlicensedClear.setStatus(_A)
modelUnlicensedClear=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,11507))
if mibBuilder.loadTexts:modelUnlicensedClear.setStatus(_A)
blkdiskClear=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,11508))
if mibBuilder.loadTexts:blkdiskClear.setStatus(_A)
backupIntegrationClear=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,11509))
if mibBuilder.loadTexts:backupIntegrationClear.setStatus(_A)
otherHardwareClear=NotificationType((1,3,6,1,4,1,17163,1,100,4,0,11510))
if mibBuilder.loadTexts:otherHardwareClear.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'gc':gc,'system':system,'model':model,'serialNumber':serialNumber,'systemVersion':systemVersion,'status':status,'systemClock':systemClock,'health':health,'systemHealth':systemHealth,'systemTemperature':systemTemperature,'procTable':procTable,'procEntry':procEntry,_F:procIndex,_D:procName,'procStatus':procStatus,'procNumFailures':procNumFailures,'config':config,'activeConfig':activeConfig,'alarms':alarms,'alarmsPrefix':alarmsPrefix,'procCrash':procCrash,'procExit':procExit,'configChange':configChange,'cpuUtil':cpuUtil,'pagingActivity':pagingActivity,'linkError':linkError,'powerSupplyError':powerSupplyError,'fanError':fanError,'memoryError':memoryError,'ipmi':ipmi,'localFSFull':localFSFull,'temperatureCritical':temperatureCritical,'temperatureWarning':temperatureWarning,'scheduledJobError':scheduledJobError,'confModeEnter':confModeEnter,'confModeExit':confModeExit,'secureVaultLocked':secureVaultLocked,'procRestart':procRestart,'testTrap':testTrap,'cpuUtilClear':cpuUtilClear,'pagingActivityClear':pagingActivityClear,'linkErrorClear':linkErrorClear,'powerSupplyErrorClear':powerSupplyErrorClear,'fanErrorClear':fanErrorClear,'memoryErrorClear':memoryErrorClear,'ipmiClear':ipmiClear,'localFSFullClear':localFSFullClear,'temperatureNonCritical':temperatureNonCritical,'temperatureNormal':temperatureNormal,'secureVaultUnlocked':secureVaultUnlocked,'edgeError':edgeError,'highAvailabilityError':highAvailabilityError,'lunError':lunError,'iscsiError':iscsiError,'snapshotError':snapshotError,'applianceUnlicensedError':applianceUnlicensedError,'modelUnlicensedError':modelUnlicensedError,'blkdiskError':blkdiskError,'backupIntegrationError':backupIntegrationError,'otherHardwareError':otherHardwareError,'edgeClear':edgeClear,'highAvailabilityClear':highAvailabilityClear,'lunClear':lunClear,'iscsiClear':iscsiClear,'snapshotClear':snapshotClear,'applianceUnlicensedClear':applianceUnlicensedClear,'modelUnlicensedClear':modelUnlicensedClear,'blkdiskClear':blkdiskClear,'backupIntegrationClear':backupIntegrationClear,'otherHardwareClear':otherHardwareClear,'statistics':statistics,'cpuLoad':cpuLoad,'cpuLoad1':cpuLoad1,'cpuLoad5':cpuLoad5,'cpuLoad15':cpuLoad15,'cpuUtil1':cpuUtil1,'cpuIndivUtilTable':cpuIndivUtilTable,'cpuIndivUtilEntry':cpuIndivUtilEntry,_H:cpuIndivIndex,'cpuIndivId':cpuIndivId,'cpuIndivIdleTime':cpuIndivIdleTime,'cpuIndivSystemTime':cpuIndivSystemTime,'cpuIndivUserTime':cpuIndivUserTime})