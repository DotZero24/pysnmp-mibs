_T='zxAnHisPerfGlobalGroup'
_S='zxAnHisPerfThreshAlmGroup'
_R='zxAnHisPerfMgmtAutoUploadEnable'
_Q='zxAnHisPerfMgmtAlarmEnable'
_P='zxAnHisPerfMgmtSampleEnable'
_O='DisplayString'
_N='read-write'
_M='disable'
_L='enable'
_K='Integer32'
_J='zxAnHisPmFallingAlarmThreshold'
_I='zxAnHisPmFallingWarningThreshold'
_H='zxAnHisPmRisingAlarmThreshold'
_G='zxAnHisPmRisingWarningThreshold'
_F='accessible-for-notify'
_E='zxAnHisPmStatisticalValue'
_D='zxAnHisPmThresholdMetric'
_C='zxAnHisPmMetricInstIndex'
_B='current'
_A='ZTE-AN-HIS-PERF-MGMT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_O,'PhysAddress','RowStatus','TextualConvention','TruthValue')
zxAn,=mibBuilder.importSymbols('ZTE-AN-TC-MIB','zxAn')
zxAnHisPerfMgmtMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,168))
if mibBuilder.loadTexts:zxAnHisPerfMgmtMib.setRevisions(('2011-11-07 00:00',))
_ZxAnHisPerfMgmtObjects_ObjectIdentity=ObjectIdentity
zxAnHisPerfMgmtObjects=_ZxAnHisPerfMgmtObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,168,1))
_ZxAnHisPerfMgmtThreshAlmObjects_ObjectIdentity=ObjectIdentity
zxAnHisPerfMgmtThreshAlmObjects=_ZxAnHisPerfMgmtThreshAlmObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,168,1,1))
class _ZxAnHisPmMetricInstIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_ZxAnHisPmMetricInstIndex_Type.__name__=_O
_ZxAnHisPmMetricInstIndex_Object=MibScalar
zxAnHisPmMetricInstIndex=_ZxAnHisPmMetricInstIndex_Object((1,3,6,1,4,1,3902,1015,168,1,1,1),_ZxAnHisPmMetricInstIndex_Type())
zxAnHisPmMetricInstIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnHisPmMetricInstIndex.setStatus(_B)
_ZxAnHisPmThresholdMetric_Type=ObjectIdentifier
_ZxAnHisPmThresholdMetric_Object=MibScalar
zxAnHisPmThresholdMetric=_ZxAnHisPmThresholdMetric_Object((1,3,6,1,4,1,3902,1015,168,1,1,2),_ZxAnHisPmThresholdMetric_Type())
zxAnHisPmThresholdMetric.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnHisPmThresholdMetric.setStatus(_B)
_ZxAnHisPmStatisticalValue_Type=Counter64
_ZxAnHisPmStatisticalValue_Object=MibScalar
zxAnHisPmStatisticalValue=_ZxAnHisPmStatisticalValue_Object((1,3,6,1,4,1,3902,1015,168,1,1,3),_ZxAnHisPmStatisticalValue_Type())
zxAnHisPmStatisticalValue.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnHisPmStatisticalValue.setStatus(_B)
_ZxAnHisPmRisingWarningThreshold_Type=Counter64
_ZxAnHisPmRisingWarningThreshold_Object=MibScalar
zxAnHisPmRisingWarningThreshold=_ZxAnHisPmRisingWarningThreshold_Object((1,3,6,1,4,1,3902,1015,168,1,1,4),_ZxAnHisPmRisingWarningThreshold_Type())
zxAnHisPmRisingWarningThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnHisPmRisingWarningThreshold.setStatus(_B)
_ZxAnHisPmRisingAlarmThreshold_Type=Counter64
_ZxAnHisPmRisingAlarmThreshold_Object=MibScalar
zxAnHisPmRisingAlarmThreshold=_ZxAnHisPmRisingAlarmThreshold_Object((1,3,6,1,4,1,3902,1015,168,1,1,5),_ZxAnHisPmRisingAlarmThreshold_Type())
zxAnHisPmRisingAlarmThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnHisPmRisingAlarmThreshold.setStatus(_B)
_ZxAnHisPmFallingWarningThreshold_Type=Counter64
_ZxAnHisPmFallingWarningThreshold_Object=MibScalar
zxAnHisPmFallingWarningThreshold=_ZxAnHisPmFallingWarningThreshold_Object((1,3,6,1,4,1,3902,1015,168,1,1,6),_ZxAnHisPmFallingWarningThreshold_Type())
zxAnHisPmFallingWarningThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnHisPmFallingWarningThreshold.setStatus(_B)
_ZxAnHisPmFallingAlarmThreshold_Type=Counter64
_ZxAnHisPmFallingAlarmThreshold_Object=MibScalar
zxAnHisPmFallingAlarmThreshold=_ZxAnHisPmFallingAlarmThreshold_Object((1,3,6,1,4,1,3902,1015,168,1,1,7),_ZxAnHisPmFallingAlarmThreshold_Type())
zxAnHisPmFallingAlarmThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnHisPmFallingAlarmThreshold.setStatus(_B)
_ZxAnHisPerfMgmtGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnHisPerfMgmtGlobalObjects=_ZxAnHisPerfMgmtGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,168,1,2))
class _ZxAnHisPerfMgmtSampleEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_ZxAnHisPerfMgmtSampleEnable_Type.__name__=_K
_ZxAnHisPerfMgmtSampleEnable_Object=MibScalar
zxAnHisPerfMgmtSampleEnable=_ZxAnHisPerfMgmtSampleEnable_Object((1,3,6,1,4,1,3902,1015,168,1,2,1),_ZxAnHisPerfMgmtSampleEnable_Type())
zxAnHisPerfMgmtSampleEnable.setMaxAccess(_N)
if mibBuilder.loadTexts:zxAnHisPerfMgmtSampleEnable.setStatus(_B)
class _ZxAnHisPerfMgmtAlarmEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_ZxAnHisPerfMgmtAlarmEnable_Type.__name__=_K
_ZxAnHisPerfMgmtAlarmEnable_Object=MibScalar
zxAnHisPerfMgmtAlarmEnable=_ZxAnHisPerfMgmtAlarmEnable_Object((1,3,6,1,4,1,3902,1015,168,1,2,2),_ZxAnHisPerfMgmtAlarmEnable_Type())
zxAnHisPerfMgmtAlarmEnable.setMaxAccess(_N)
if mibBuilder.loadTexts:zxAnHisPerfMgmtAlarmEnable.setStatus(_B)
class _ZxAnHisPerfMgmtAutoUploadEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_ZxAnHisPerfMgmtAutoUploadEnable_Type.__name__=_K
_ZxAnHisPerfMgmtAutoUploadEnable_Object=MibScalar
zxAnHisPerfMgmtAutoUploadEnable=_ZxAnHisPerfMgmtAutoUploadEnable_Object((1,3,6,1,4,1,3902,1015,168,1,2,3),_ZxAnHisPerfMgmtAutoUploadEnable_Type())
zxAnHisPerfMgmtAutoUploadEnable.setMaxAccess(_N)
if mibBuilder.loadTexts:zxAnHisPerfMgmtAutoUploadEnable.setStatus(_B)
_ZxAnHisPerfMgmtTrapObjects_ObjectIdentity=ObjectIdentity
zxAnHisPerfMgmtTrapObjects=_ZxAnHisPerfMgmtTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,168,3))
_ZxAnHisPerfMgmtConformance_ObjectIdentity=ObjectIdentity
zxAnHisPerfMgmtConformance=_ZxAnHisPerfMgmtConformance_ObjectIdentity((1,3,6,1,4,1,3902,1015,168,4))
_ZxAnHisPerfMIBCompliances_ObjectIdentity=ObjectIdentity
zxAnHisPerfMIBCompliances=_ZxAnHisPerfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,3902,1015,168,4,1))
_ZxAnHisPerfMIBGroups_ObjectIdentity=ObjectIdentity
zxAnHisPerfMIBGroups=_ZxAnHisPerfMIBGroups_ObjectIdentity((1,3,6,1,4,1,3902,1015,168,4,2))
zxAnHisPerfThreshAlmGroup=ObjectGroup((1,3,6,1,4,1,3902,1015,168,4,2,1))
zxAnHisPerfThreshAlmGroup.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:zxAnHisPerfThreshAlmGroup.setStatus(_B)
zxAnHisPerfGlobalGroup=ObjectGroup((1,3,6,1,4,1,3902,1015,168,4,2,2))
zxAnHisPerfGlobalGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:zxAnHisPerfGlobalGroup.setStatus(_B)
zxAnPm15minRisingWarning=NotificationType((1,3,6,1,4,1,3902,1015,168,3,1))
zxAnPm15minRisingWarning.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:zxAnPm15minRisingWarning.setStatus(_B)
zxAnPm15minRisingWarningRestore=NotificationType((1,3,6,1,4,1,3902,1015,168,3,2))
zxAnPm15minRisingWarningRestore.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:zxAnPm15minRisingWarningRestore.setStatus(_B)
zxAnPm15minRisingAlarm=NotificationType((1,3,6,1,4,1,3902,1015,168,3,3))
zxAnPm15minRisingAlarm.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H)))
if mibBuilder.loadTexts:zxAnPm15minRisingAlarm.setStatus(_B)
zxAnPm15minRisingAlarmRestore=NotificationType((1,3,6,1,4,1,3902,1015,168,3,4))
zxAnPm15minRisingAlarmRestore.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H)))
if mibBuilder.loadTexts:zxAnPm15minRisingAlarmRestore.setStatus(_B)
zxAnPm24hRisingWarning=NotificationType((1,3,6,1,4,1,3902,1015,168,3,5))
zxAnPm24hRisingWarning.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:zxAnPm24hRisingWarning.setStatus(_B)
zxAnPm24hRisingWarningRestore=NotificationType((1,3,6,1,4,1,3902,1015,168,3,6))
zxAnPm24hRisingWarningRestore.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:zxAnPm24hRisingWarningRestore.setStatus(_B)
zxAnPm24hRisingAlarm=NotificationType((1,3,6,1,4,1,3902,1015,168,3,7))
zxAnPm24hRisingAlarm.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H)))
if mibBuilder.loadTexts:zxAnPm24hRisingAlarm.setStatus(_B)
zxAnPm24hRisingAlarmRestore=NotificationType((1,3,6,1,4,1,3902,1015,168,3,8))
zxAnPm24hRisingAlarmRestore.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_H)))
if mibBuilder.loadTexts:zxAnPm24hRisingAlarmRestore.setStatus(_B)
zxAnPm15minFallingWarning=NotificationType((1,3,6,1,4,1,3902,1015,168,3,9))
zxAnPm15minFallingWarning.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_I)))
if mibBuilder.loadTexts:zxAnPm15minFallingWarning.setStatus(_B)
zxAnPm15minFallingWarningRestore=NotificationType((1,3,6,1,4,1,3902,1015,168,3,10))
zxAnPm15minFallingWarningRestore.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_I)))
if mibBuilder.loadTexts:zxAnPm15minFallingWarningRestore.setStatus(_B)
zxAnPm15minFallingAlarm=NotificationType((1,3,6,1,4,1,3902,1015,168,3,11))
zxAnPm15minFallingAlarm.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:zxAnPm15minFallingAlarm.setStatus(_B)
zxAnPm15minFallingAlarmRestore=NotificationType((1,3,6,1,4,1,3902,1015,168,3,12))
zxAnPm15minFallingAlarmRestore.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:zxAnPm15minFallingAlarmRestore.setStatus(_B)
zxAnPm24hFallingWarning=NotificationType((1,3,6,1,4,1,3902,1015,168,3,13))
zxAnPm24hFallingWarning.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_I)))
if mibBuilder.loadTexts:zxAnPm24hFallingWarning.setStatus(_B)
zxAnPm24hFallingWarningRestore=NotificationType((1,3,6,1,4,1,3902,1015,168,3,14))
zxAnPm24hFallingWarningRestore.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_I)))
if mibBuilder.loadTexts:zxAnPm24hFallingWarningRestore.setStatus(_B)
zxAnPm24hFallingAlarm=NotificationType((1,3,6,1,4,1,3902,1015,168,3,15))
zxAnPm24hFallingAlarm.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:zxAnPm24hFallingAlarm.setStatus(_B)
zxAnPm24hFallingAlarmRestore=NotificationType((1,3,6,1,4,1,3902,1015,168,3,16))
zxAnPm24hFallingAlarmRestore.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:zxAnPm24hFallingAlarmRestore.setStatus(_B)
zxAnHisPerfMIBCompliance=ModuleCompliance((1,3,6,1,4,1,3902,1015,168,4,1,1))
zxAnHisPerfMIBCompliance.setObjects(*((_A,_S),(_A,_T)))
if mibBuilder.loadTexts:zxAnHisPerfMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'zxAnHisPerfMgmtMib':zxAnHisPerfMgmtMib,'zxAnHisPerfMgmtObjects':zxAnHisPerfMgmtObjects,'zxAnHisPerfMgmtThreshAlmObjects':zxAnHisPerfMgmtThreshAlmObjects,_C:zxAnHisPmMetricInstIndex,_D:zxAnHisPmThresholdMetric,_E:zxAnHisPmStatisticalValue,_G:zxAnHisPmRisingWarningThreshold,_H:zxAnHisPmRisingAlarmThreshold,_I:zxAnHisPmFallingWarningThreshold,_J:zxAnHisPmFallingAlarmThreshold,'zxAnHisPerfMgmtGlobalObjects':zxAnHisPerfMgmtGlobalObjects,_P:zxAnHisPerfMgmtSampleEnable,_Q:zxAnHisPerfMgmtAlarmEnable,_R:zxAnHisPerfMgmtAutoUploadEnable,'zxAnHisPerfMgmtTrapObjects':zxAnHisPerfMgmtTrapObjects,'zxAnPm15minRisingWarning':zxAnPm15minRisingWarning,'zxAnPm15minRisingWarningRestore':zxAnPm15minRisingWarningRestore,'zxAnPm15minRisingAlarm':zxAnPm15minRisingAlarm,'zxAnPm15minRisingAlarmRestore':zxAnPm15minRisingAlarmRestore,'zxAnPm24hRisingWarning':zxAnPm24hRisingWarning,'zxAnPm24hRisingWarningRestore':zxAnPm24hRisingWarningRestore,'zxAnPm24hRisingAlarm':zxAnPm24hRisingAlarm,'zxAnPm24hRisingAlarmRestore':zxAnPm24hRisingAlarmRestore,'zxAnPm15minFallingWarning':zxAnPm15minFallingWarning,'zxAnPm15minFallingWarningRestore':zxAnPm15minFallingWarningRestore,'zxAnPm15minFallingAlarm':zxAnPm15minFallingAlarm,'zxAnPm15minFallingAlarmRestore':zxAnPm15minFallingAlarmRestore,'zxAnPm24hFallingWarning':zxAnPm24hFallingWarning,'zxAnPm24hFallingWarningRestore':zxAnPm24hFallingWarningRestore,'zxAnPm24hFallingAlarm':zxAnPm24hFallingAlarm,'zxAnPm24hFallingAlarmRestore':zxAnPm24hFallingAlarmRestore,'zxAnHisPerfMgmtConformance':zxAnHisPerfMgmtConformance,'zxAnHisPerfMIBCompliances':zxAnHisPerfMIBCompliances,'zxAnHisPerfMIBCompliance':zxAnHisPerfMIBCompliance,'zxAnHisPerfMIBGroups':zxAnHisPerfMIBGroups,_S:zxAnHisPerfThreshAlmGroup,_T:zxAnHisPerfGlobalGroup})