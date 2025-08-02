_W='heCommonNotificationsGroup'
_V='heCommonLogGroup'
_U='heCommonAlarmEvent'
_T='heCommonLogLastIndex'
_S='heCommonLogNumberOfEntries'
_R='heCommonAlarmDetectionControl'
_Q='heCommonSoftwareReset'
_P='heCommonTemperature'
_O='heCommonTime'
_N='heCommonLogIndex'
_M='entPhysicalIndex'
_L='SCTE-HMS-PROPERTY-MIB'
_K='heCommonLogText'
_J='heCommonLogTime'
_I='heCommonLogState'
_H='heCommonLogValue'
_G='heCommonLogOID'
_F='read-write'
_E='ENTITY-MIB'
_D='read-only'
_C='Integer32'
_B='SCTE-HMS-HE-COMMON-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_E,_M)
HeTenthCentigrade,heCommon=mibBuilder.importSymbols('SCTE-HMS-HEADENDIDENT-MIB','HeTenthCentigrade','heCommon')
scteHmsTree,=mibBuilder.importSymbols('SCTE-ROOT','scteHmsTree')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
heCommonMib=ModuleIdentity((1,3,6,1,4,1,5591,1,11,2,1,1))
if mibBuilder.loadTexts:heCommonMib.setRevisions(('2003-02-17 00:00',))
_HeCommonTrapPrefix_ObjectIdentity=ObjectIdentity
heCommonTrapPrefix=_HeCommonTrapPrefix_ObjectIdentity((1,3,6,1,4,1,5591,1,0))
_HeCommonObjects_ObjectIdentity=ObjectIdentity
heCommonObjects=_HeCommonObjects_ObjectIdentity((1,3,6,1,4,1,5591,1,11,2,1,1,1))
_HeCommonParams_ObjectIdentity=ObjectIdentity
heCommonParams=_HeCommonParams_ObjectIdentity((1,3,6,1,4,1,5591,1,11,2,1,1,1,1))
_HeCommonTable_Object=MibTable
heCommonTable=_HeCommonTable_Object((1,3,6,1,4,1,5591,1,11,2,1,1,1,1,1))
if mibBuilder.loadTexts:heCommonTable.setStatus(_A)
_HeCommonEntry_Object=MibTableRow
heCommonEntry=_HeCommonEntry_Object((1,3,6,1,4,1,5591,1,11,2,1,1,1,1,1,1))
heCommonEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:heCommonEntry.setStatus(_A)
_HeCommonTime_Type=DateAndTime
_HeCommonTime_Object=MibTableColumn
heCommonTime=_HeCommonTime_Object((1,3,6,1,4,1,5591,1,11,2,1,1,1,1,1,1,1),_HeCommonTime_Type())
heCommonTime.setMaxAccess(_F)
if mibBuilder.loadTexts:heCommonTime.setStatus(_A)
_HeCommonTemperature_Type=HeTenthCentigrade
_HeCommonTemperature_Object=MibTableColumn
heCommonTemperature=_HeCommonTemperature_Object((1,3,6,1,4,1,5591,1,11,2,1,1,1,1,1,1,2),_HeCommonTemperature_Type())
heCommonTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:heCommonTemperature.setStatus(_A)
class _HeCommonSoftwareReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_HeCommonSoftwareReset_Type.__name__=_C
_HeCommonSoftwareReset_Object=MibTableColumn
heCommonSoftwareReset=_HeCommonSoftwareReset_Object((1,3,6,1,4,1,5591,1,11,2,1,1,1,1,1,1,3),_HeCommonSoftwareReset_Type())
heCommonSoftwareReset.setMaxAccess(_F)
if mibBuilder.loadTexts:heCommonSoftwareReset.setStatus(_A)
class _HeCommonAlarmDetectionControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('detectionDisabled',1),('detectionEnabled',2),('detectionEnabledAndRegenerate',3)))
_HeCommonAlarmDetectionControl_Type.__name__=_C
_HeCommonAlarmDetectionControl_Object=MibTableColumn
heCommonAlarmDetectionControl=_HeCommonAlarmDetectionControl_Object((1,3,6,1,4,1,5591,1,11,2,1,1,1,1,1,1,4),_HeCommonAlarmDetectionControl_Type())
heCommonAlarmDetectionControl.setMaxAccess(_F)
if mibBuilder.loadTexts:heCommonAlarmDetectionControl.setStatus(_A)
_HeCommonLog_ObjectIdentity=ObjectIdentity
heCommonLog=_HeCommonLog_ObjectIdentity((1,3,6,1,4,1,5591,1,11,2,1,1,1,2))
class _HeCommonLogNumberOfEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HeCommonLogNumberOfEntries_Type.__name__=_C
_HeCommonLogNumberOfEntries_Object=MibScalar
heCommonLogNumberOfEntries=_HeCommonLogNumberOfEntries_Object((1,3,6,1,4,1,5591,1,11,2,1,1,1,2,1),_HeCommonLogNumberOfEntries_Type())
heCommonLogNumberOfEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:heCommonLogNumberOfEntries.setStatus(_A)
class _HeCommonLogLastIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HeCommonLogLastIndex_Type.__name__=_C
_HeCommonLogLastIndex_Object=MibScalar
heCommonLogLastIndex=_HeCommonLogLastIndex_Object((1,3,6,1,4,1,5591,1,11,2,1,1,1,2,2),_HeCommonLogLastIndex_Type())
heCommonLogLastIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:heCommonLogLastIndex.setStatus(_A)
_HeCommonLogTable_Object=MibTable
heCommonLogTable=_HeCommonLogTable_Object((1,3,6,1,4,1,5591,1,11,2,1,1,1,2,3))
if mibBuilder.loadTexts:heCommonLogTable.setStatus(_A)
_HeCommonLogEntry_Object=MibTableRow
heCommonLogEntry=_HeCommonLogEntry_Object((1,3,6,1,4,1,5591,1,11,2,1,1,1,2,3,1))
heCommonLogEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:heCommonLogEntry.setStatus(_A)
class _HeCommonLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HeCommonLogIndex_Type.__name__=_C
_HeCommonLogIndex_Object=MibTableColumn
heCommonLogIndex=_HeCommonLogIndex_Object((1,3,6,1,4,1,5591,1,11,2,1,1,1,2,3,1,1),_HeCommonLogIndex_Type())
heCommonLogIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:heCommonLogIndex.setStatus(_A)
_HeCommonLogOID_Type=ObjectIdentifier
_HeCommonLogOID_Object=MibTableColumn
heCommonLogOID=_HeCommonLogOID_Object((1,3,6,1,4,1,5591,1,11,2,1,1,1,2,3,1,2),_HeCommonLogOID_Type())
heCommonLogOID.setMaxAccess(_D)
if mibBuilder.loadTexts:heCommonLogOID.setStatus(_A)
class _HeCommonLogValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_HeCommonLogValue_Type.__name__=_C
_HeCommonLogValue_Object=MibTableColumn
heCommonLogValue=_HeCommonLogValue_Object((1,3,6,1,4,1,5591,1,11,2,1,1,1,2,3,1,3),_HeCommonLogValue_Type())
heCommonLogValue.setMaxAccess(_D)
if mibBuilder.loadTexts:heCommonLogValue.setStatus(_A)
class _HeCommonLogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('heCommonNominal',1),('heCommonHIHI',2),('heCommonHI',3),('heCommonLO',4),('heCommonLOLO',5),('heCommonDiscreteMajor',6),('heCommonDiscreteMinor',7)))
_HeCommonLogState_Type.__name__=_C
_HeCommonLogState_Object=MibTableColumn
heCommonLogState=_HeCommonLogState_Object((1,3,6,1,4,1,5591,1,11,2,1,1,1,2,3,1,4),_HeCommonLogState_Type())
heCommonLogState.setMaxAccess(_D)
if mibBuilder.loadTexts:heCommonLogState.setStatus(_A)
_HeCommonLogTime_Type=DateAndTime
_HeCommonLogTime_Object=MibTableColumn
heCommonLogTime=_HeCommonLogTime_Object((1,3,6,1,4,1,5591,1,11,2,1,1,1,2,3,1,5),_HeCommonLogTime_Type())
heCommonLogTime.setMaxAccess(_D)
if mibBuilder.loadTexts:heCommonLogTime.setStatus(_A)
_HeCommonLogText_Type=DisplayString
_HeCommonLogText_Object=MibTableColumn
heCommonLogText=_HeCommonLogText_Object((1,3,6,1,4,1,5591,1,11,2,1,1,1,2,3,1,6),_HeCommonLogText_Type())
heCommonLogText.setMaxAccess(_D)
if mibBuilder.loadTexts:heCommonLogText.setStatus(_A)
_HeCommonTraps_ObjectIdentity=ObjectIdentity
heCommonTraps=_HeCommonTraps_ObjectIdentity((1,3,6,1,4,1,5591,1,11,2,1,1,2))
_HeCommonConformance_ObjectIdentity=ObjectIdentity
heCommonConformance=_HeCommonConformance_ObjectIdentity((1,3,6,1,4,1,5591,1,11,2,1,1,3))
_HeCommonCompliances_ObjectIdentity=ObjectIdentity
heCommonCompliances=_HeCommonCompliances_ObjectIdentity((1,3,6,1,4,1,5591,1,11,2,1,1,3,1))
_HeCommonGroups_ObjectIdentity=ObjectIdentity
heCommonGroups=_HeCommonGroups_ObjectIdentity((1,3,6,1,4,1,5591,1,11,2,1,1,3,2))
heCommonParamsGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,2,1,1,3,2,1))
heCommonParamsGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:heCommonParamsGroup.setStatus(_A)
heCommonLogGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,2,1,1,3,2,2))
heCommonLogGroup.setObjects(*((_B,_S),(_B,_T),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:heCommonLogGroup.setStatus(_A)
heCommonAlarmEvent=NotificationType((1,3,6,1,4,1,5591,1,0,5))
heCommonAlarmEvent.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:heCommonAlarmEvent.setStatus(_A)
heCommonNotificationsGroup=NotificationGroup((1,3,6,1,4,1,5591,1,11,2,1,1,3,2,3))
heCommonNotificationsGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:heCommonNotificationsGroup.setStatus(_A)
heCommonCompliance=ModuleCompliance((1,3,6,1,4,1,5591,1,11,2,1,1,3,1,1))
heCommonCompliance.setObjects(*((_B,_V),(_B,_W),(_E,'entityPhysicalGroup'),(_E,'entityPhysical2Group'),(_E,'entityGeneralGroup'),(_E,'entityNotificationsGroup'),('SNMP-TARGET-MIB','snmpTargetBasicGroup'),('SNMP-NOTIFICATION-MIB','snmpNotifyGroup'),('SNMPv2-MIB','systemGroup'),(_L,'analogAlarmsGroup'),(_L,'discreteAlarmsGroup'),(_L,'currentAlarmsGroup')))
if mibBuilder.loadTexts:heCommonCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'heCommonTrapPrefix':heCommonTrapPrefix,_U:heCommonAlarmEvent,'heCommonMib':heCommonMib,'heCommonObjects':heCommonObjects,'heCommonParams':heCommonParams,'heCommonTable':heCommonTable,'heCommonEntry':heCommonEntry,_O:heCommonTime,_P:heCommonTemperature,_Q:heCommonSoftwareReset,_R:heCommonAlarmDetectionControl,'heCommonLog':heCommonLog,_S:heCommonLogNumberOfEntries,_T:heCommonLogLastIndex,'heCommonLogTable':heCommonLogTable,'heCommonLogEntry':heCommonLogEntry,_N:heCommonLogIndex,_G:heCommonLogOID,_H:heCommonLogValue,_I:heCommonLogState,_J:heCommonLogTime,_K:heCommonLogText,'heCommonTraps':heCommonTraps,'heCommonConformance':heCommonConformance,'heCommonCompliances':heCommonCompliances,'heCommonCompliance':heCommonCompliance,'heCommonGroups':heCommonGroups,'heCommonParamsGroup':heCommonParamsGroup,_V:heCommonLogGroup,_W:heCommonNotificationsGroup})