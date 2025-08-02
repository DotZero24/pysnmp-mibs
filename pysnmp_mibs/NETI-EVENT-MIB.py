_w='netiGenericEvent'
_v='eventAlarmClear'
_u='eventAlarmUnknown'
_t='eventAlarmIndeterminate'
_s='eventAlarmWarning'
_r='eventAlarmMinor'
_q='eventAlarmMajor'
_p='eventAlarmCritical'
_o='eventIndeterminateCounter'
_n='eventWarningCounter'
_m='eventMinorCounter'
_l='eventMajorCounter'
_k='eventCriticalCounter'
_j='eventActiveAlarmCreatedTime'
_i='eventActiveAlarmAcknowledged'
_h='eventActiveAlarmLastChangedTime'
_g='eventActiveAlarmText'
_f='eventActiveAlarmSeverity'
_e='eventActiveAlarmCause'
_d='eventActiveAlarmAlarmType'
_c='eventActiveAlarmObjectName'
_b='eventActiveAlarmObject'
_a='eventAlarmCreatedTime'
_Z='eventAlarmAcknowledged'
_Y='eventAlarmLastChangedTime'
_X='eventAlarmText'
_W='eventAlarmSeverity'
_V='eventAlarmCause'
_U='eventAlarmAlarmType'
_T='eventAlarmObjectName'
_S='eventAlarmObject'
_R='eventLogLastChangedTime'
_Q='read-write'
_P='eventType'
_O='eventActiveAlarmIndex'
_N='eventAlarmIndex'
_M='unknown'
_L='eventSeverity'
_K='eventCause'
_J='eventAlarmType'
_I='eventCreatedTime'
_H='eventText'
_G='eventObjectName'
_F='eventObject'
_E='eventSequenceCounter'
_D='eventIndex'
_C='read-only'
_B='current'
_A='NETI-EVENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netiGeneric,=mibBuilder.importSymbols('NETI-COMMON-MIB','netiGeneric')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowPointer,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowPointer','TextualConvention','TruthValue')
netiEventMIB=ModuleIdentity((1,3,6,1,4,1,2928,2,1))
if mibBuilder.loadTexts:netiEventMIB.setRevisions(('2011-05-03 10:00','2009-07-09 16:00','2007-03-06 00:00','2004-09-10 00:00','2003-11-25 00:00'))
class EventType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('created',1),('modified',2),('deleted',3)))
class AlarmType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_M,0),('communication',1),('qualityOfService',2),('processingError',3),('equipment',4),('environmental',5)))
class AlarmSeverity(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_M,0),('indeterminate',1),('critical',2),('major',3),('minor',4),('warning',5),('cleared',6)))
class AlarmCause(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69)));namedValues=NamedValues(*((_M,0),('adapterError',1),('applicationSubsystemFailure',2),('bandwidthReduced',3),('callEstablishmentError',4),('communicationsProtocolError',5),('communicationsSubsystemFailure',6),('configurationOrCustomizationError',7),('congestion',8),('corruptData',9),('cpuCyclesLimitExceeded',10),('datasetOrModemError',11),('degradedSignal',12),('dTEDCEInterfaceError',13),('enclosureDoorOpen',14),('equipmentMalfunction',15),('excessiveVibration',16),('fileError',17),('fireDetected',18),('floodDetected',19),('framingError',20),('heatingOrVentilationOrCoolingSystemProblem',21),('humidityUnacceptable',22),('inputOutputDeviceError',23),('inputDeviceError',24),('lANError',25),('leakDetected',26),('localNodeTransmissionError',27),('lossOfFrame',28),('lossOfSignal',29),('materialSupplyExhausted',30),('multiplexerProblem',31),('outOfMemory',32),('outputDeviceError',33),('performanceDegraded',34),('powerProblem',35),('pressureUnacceptable',36),('processorProblem',37),('pumpFailure',38),('queueSizeExceeded',39),('receiveFailure',40),('receiverFailure',41),('remoteNodeTransmissionError',42),('resourceAtOrNearingCapacity',43),('responseTimeExcessive',44),('retransmissionRateExcessive',45),('softwareError',46),('softwareProgramAbnormallyTerminated',47),('softwareProgramError',48),('storageCapacityProblem',49),('temperatureUnacceptable',50),('thresholdCrossed',51),('timingProblem',52),('toxicLeakDetected',53),('transmitFailure',54),('transmitterFailure',55),('underlyingResourceUnavailable',56),('versionMismatch',57),('phyLossOfSignal',58),('phyLossOfFrame',59),('phyAlarmIndicationSignal',60),('phyRemoteDefectIndication',61),('phySignalFailure',62),('phySignalDegraded',63),('testmodeEntered',64),('serviceUnavailable',65),('alarmIndicationSignal',66),('remoteDefectIndication',67),('replaceableUnitMissing',68),('replaceableUnitProblem',69)))
_EventObjects_ObjectIdentity=ObjectIdentity
eventObjects=_EventObjects_ObjectIdentity((1,3,6,1,4,1,2928,2,1,1))
_EventSequenceCounter_Type=Unsigned32
_EventSequenceCounter_Object=MibScalar
eventSequenceCounter=_EventSequenceCounter_Object((1,3,6,1,4,1,2928,2,1,1,1),_EventSequenceCounter_Type())
eventSequenceCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:eventSequenceCounter.setStatus(_B)
_EventLogLastChangedTime_Type=DateAndTime
_EventLogLastChangedTime_Object=MibScalar
eventLogLastChangedTime=_EventLogLastChangedTime_Object((1,3,6,1,4,1,2928,2,1,1,2),_EventLogLastChangedTime_Type())
eventLogLastChangedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:eventLogLastChangedTime.setStatus(_B)
_EventTable_Object=MibTable
eventTable=_EventTable_Object((1,3,6,1,4,1,2928,2,1,1,3))
if mibBuilder.loadTexts:eventTable.setStatus(_B)
_EventEntry_Object=MibTableRow
eventEntry=_EventEntry_Object((1,3,6,1,4,1,2928,2,1,1,3,1))
eventEntry.setIndexNames((0,_A,_D))
if mibBuilder.loadTexts:eventEntry.setStatus(_B)
_EventIndex_Type=Unsigned32
_EventIndex_Object=MibTableColumn
eventIndex=_EventIndex_Object((1,3,6,1,4,1,2928,2,1,1,3,1,1),_EventIndex_Type())
eventIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:eventIndex.setStatus(_B)
_EventObject_Type=RowPointer
_EventObject_Object=MibTableColumn
eventObject=_EventObject_Object((1,3,6,1,4,1,2928,2,1,1,3,1,2),_EventObject_Type())
eventObject.setMaxAccess(_C)
if mibBuilder.loadTexts:eventObject.setStatus(_B)
_EventObjectName_Type=DisplayString
_EventObjectName_Object=MibTableColumn
eventObjectName=_EventObjectName_Object((1,3,6,1,4,1,2928,2,1,1,3,1,3),_EventObjectName_Type())
eventObjectName.setMaxAccess(_C)
if mibBuilder.loadTexts:eventObjectName.setStatus(_B)
_EventAlarmType_Type=AlarmType
_EventAlarmType_Object=MibTableColumn
eventAlarmType=_EventAlarmType_Object((1,3,6,1,4,1,2928,2,1,1,3,1,4),_EventAlarmType_Type())
eventAlarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:eventAlarmType.setStatus(_B)
_EventType_Type=EventType
_EventType_Object=MibTableColumn
eventType=_EventType_Object((1,3,6,1,4,1,2928,2,1,1,3,1,5),_EventType_Type())
eventType.setMaxAccess(_C)
if mibBuilder.loadTexts:eventType.setStatus(_B)
_EventCause_Type=AlarmCause
_EventCause_Object=MibTableColumn
eventCause=_EventCause_Object((1,3,6,1,4,1,2928,2,1,1,3,1,6),_EventCause_Type())
eventCause.setMaxAccess(_C)
if mibBuilder.loadTexts:eventCause.setStatus(_B)
_EventSeverity_Type=AlarmSeverity
_EventSeverity_Object=MibTableColumn
eventSeverity=_EventSeverity_Object((1,3,6,1,4,1,2928,2,1,1,3,1,7),_EventSeverity_Type())
eventSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:eventSeverity.setStatus(_B)
_EventText_Type=DisplayString
_EventText_Object=MibTableColumn
eventText=_EventText_Object((1,3,6,1,4,1,2928,2,1,1,3,1,8),_EventText_Type())
eventText.setMaxAccess(_C)
if mibBuilder.loadTexts:eventText.setStatus(_B)
_EventCreatedTime_Type=DateAndTime
_EventCreatedTime_Object=MibTableColumn
eventCreatedTime=_EventCreatedTime_Object((1,3,6,1,4,1,2928,2,1,1,3,1,9),_EventCreatedTime_Type())
eventCreatedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:eventCreatedTime.setStatus(_B)
_EventAlarmTable_Object=MibTable
eventAlarmTable=_EventAlarmTable_Object((1,3,6,1,4,1,2928,2,1,1,4))
if mibBuilder.loadTexts:eventAlarmTable.setStatus(_B)
_EventAlarmEntry_Object=MibTableRow
eventAlarmEntry=_EventAlarmEntry_Object((1,3,6,1,4,1,2928,2,1,1,4,1))
eventAlarmEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:eventAlarmEntry.setStatus(_B)
_EventAlarmIndex_Type=Unsigned32
_EventAlarmIndex_Object=MibTableColumn
eventAlarmIndex=_EventAlarmIndex_Object((1,3,6,1,4,1,2928,2,1,1,4,1,1),_EventAlarmIndex_Type())
eventAlarmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:eventAlarmIndex.setStatus(_B)
_EventAlarmObject_Type=RowPointer
_EventAlarmObject_Object=MibTableColumn
eventAlarmObject=_EventAlarmObject_Object((1,3,6,1,4,1,2928,2,1,1,4,1,2),_EventAlarmObject_Type())
eventAlarmObject.setMaxAccess(_C)
if mibBuilder.loadTexts:eventAlarmObject.setStatus(_B)
_EventAlarmObjectName_Type=DisplayString
_EventAlarmObjectName_Object=MibTableColumn
eventAlarmObjectName=_EventAlarmObjectName_Object((1,3,6,1,4,1,2928,2,1,1,4,1,3),_EventAlarmObjectName_Type())
eventAlarmObjectName.setMaxAccess(_C)
if mibBuilder.loadTexts:eventAlarmObjectName.setStatus(_B)
_EventAlarmAlarmType_Type=AlarmType
_EventAlarmAlarmType_Object=MibTableColumn
eventAlarmAlarmType=_EventAlarmAlarmType_Object((1,3,6,1,4,1,2928,2,1,1,4,1,4),_EventAlarmAlarmType_Type())
eventAlarmAlarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:eventAlarmAlarmType.setStatus(_B)
_EventAlarmCause_Type=AlarmCause
_EventAlarmCause_Object=MibTableColumn
eventAlarmCause=_EventAlarmCause_Object((1,3,6,1,4,1,2928,2,1,1,4,1,5),_EventAlarmCause_Type())
eventAlarmCause.setMaxAccess(_C)
if mibBuilder.loadTexts:eventAlarmCause.setStatus(_B)
_EventAlarmSeverity_Type=AlarmSeverity
_EventAlarmSeverity_Object=MibTableColumn
eventAlarmSeverity=_EventAlarmSeverity_Object((1,3,6,1,4,1,2928,2,1,1,4,1,6),_EventAlarmSeverity_Type())
eventAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:eventAlarmSeverity.setStatus(_B)
_EventAlarmText_Type=DisplayString
_EventAlarmText_Object=MibTableColumn
eventAlarmText=_EventAlarmText_Object((1,3,6,1,4,1,2928,2,1,1,4,1,7),_EventAlarmText_Type())
eventAlarmText.setMaxAccess(_C)
if mibBuilder.loadTexts:eventAlarmText.setStatus(_B)
_EventAlarmLastChangedTime_Type=DateAndTime
_EventAlarmLastChangedTime_Object=MibTableColumn
eventAlarmLastChangedTime=_EventAlarmLastChangedTime_Object((1,3,6,1,4,1,2928,2,1,1,4,1,8),_EventAlarmLastChangedTime_Type())
eventAlarmLastChangedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:eventAlarmLastChangedTime.setStatus(_B)
_EventAlarmAcknowledged_Type=TruthValue
_EventAlarmAcknowledged_Object=MibTableColumn
eventAlarmAcknowledged=_EventAlarmAcknowledged_Object((1,3,6,1,4,1,2928,2,1,1,4,1,9),_EventAlarmAcknowledged_Type())
eventAlarmAcknowledged.setMaxAccess(_Q)
if mibBuilder.loadTexts:eventAlarmAcknowledged.setStatus(_B)
_EventAlarmCreatedTime_Type=DateAndTime
_EventAlarmCreatedTime_Object=MibTableColumn
eventAlarmCreatedTime=_EventAlarmCreatedTime_Object((1,3,6,1,4,1,2928,2,1,1,4,1,10),_EventAlarmCreatedTime_Type())
eventAlarmCreatedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:eventAlarmCreatedTime.setStatus(_B)
_EventAlarmCountersGroup_ObjectIdentity=ObjectIdentity
eventAlarmCountersGroup=_EventAlarmCountersGroup_ObjectIdentity((1,3,6,1,4,1,2928,2,1,1,5))
_EventCriticalCounter_Type=Unsigned32
_EventCriticalCounter_Object=MibScalar
eventCriticalCounter=_EventCriticalCounter_Object((1,3,6,1,4,1,2928,2,1,1,5,1),_EventCriticalCounter_Type())
eventCriticalCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:eventCriticalCounter.setStatus(_B)
_EventMajorCounter_Type=Unsigned32
_EventMajorCounter_Object=MibScalar
eventMajorCounter=_EventMajorCounter_Object((1,3,6,1,4,1,2928,2,1,1,5,2),_EventMajorCounter_Type())
eventMajorCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:eventMajorCounter.setStatus(_B)
_EventMinorCounter_Type=Unsigned32
_EventMinorCounter_Object=MibScalar
eventMinorCounter=_EventMinorCounter_Object((1,3,6,1,4,1,2928,2,1,1,5,3),_EventMinorCounter_Type())
eventMinorCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:eventMinorCounter.setStatus(_B)
_EventWarningCounter_Type=Unsigned32
_EventWarningCounter_Object=MibScalar
eventWarningCounter=_EventWarningCounter_Object((1,3,6,1,4,1,2928,2,1,1,5,4),_EventWarningCounter_Type())
eventWarningCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:eventWarningCounter.setStatus(_B)
_EventIndeterminateCounter_Type=Unsigned32
_EventIndeterminateCounter_Object=MibScalar
eventIndeterminateCounter=_EventIndeterminateCounter_Object((1,3,6,1,4,1,2928,2,1,1,5,5),_EventIndeterminateCounter_Type())
eventIndeterminateCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:eventIndeterminateCounter.setStatus(_B)
_EventActiveAlarmTable_Object=MibTable
eventActiveAlarmTable=_EventActiveAlarmTable_Object((1,3,6,1,4,1,2928,2,1,1,6))
if mibBuilder.loadTexts:eventActiveAlarmTable.setStatus(_B)
_EventActiveAlarmEntry_Object=MibTableRow
eventActiveAlarmEntry=_EventActiveAlarmEntry_Object((1,3,6,1,4,1,2928,2,1,1,6,1))
eventActiveAlarmEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:eventActiveAlarmEntry.setStatus(_B)
_EventActiveAlarmIndex_Type=Unsigned32
_EventActiveAlarmIndex_Object=MibTableColumn
eventActiveAlarmIndex=_EventActiveAlarmIndex_Object((1,3,6,1,4,1,2928,2,1,1,6,1,1),_EventActiveAlarmIndex_Type())
eventActiveAlarmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:eventActiveAlarmIndex.setStatus(_B)
_EventActiveAlarmObject_Type=RowPointer
_EventActiveAlarmObject_Object=MibTableColumn
eventActiveAlarmObject=_EventActiveAlarmObject_Object((1,3,6,1,4,1,2928,2,1,1,6,1,2),_EventActiveAlarmObject_Type())
eventActiveAlarmObject.setMaxAccess(_C)
if mibBuilder.loadTexts:eventActiveAlarmObject.setStatus(_B)
_EventActiveAlarmObjectName_Type=DisplayString
_EventActiveAlarmObjectName_Object=MibTableColumn
eventActiveAlarmObjectName=_EventActiveAlarmObjectName_Object((1,3,6,1,4,1,2928,2,1,1,6,1,3),_EventActiveAlarmObjectName_Type())
eventActiveAlarmObjectName.setMaxAccess(_C)
if mibBuilder.loadTexts:eventActiveAlarmObjectName.setStatus(_B)
_EventActiveAlarmAlarmType_Type=AlarmType
_EventActiveAlarmAlarmType_Object=MibTableColumn
eventActiveAlarmAlarmType=_EventActiveAlarmAlarmType_Object((1,3,6,1,4,1,2928,2,1,1,6,1,4),_EventActiveAlarmAlarmType_Type())
eventActiveAlarmAlarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:eventActiveAlarmAlarmType.setStatus(_B)
_EventActiveAlarmCause_Type=AlarmCause
_EventActiveAlarmCause_Object=MibTableColumn
eventActiveAlarmCause=_EventActiveAlarmCause_Object((1,3,6,1,4,1,2928,2,1,1,6,1,5),_EventActiveAlarmCause_Type())
eventActiveAlarmCause.setMaxAccess(_C)
if mibBuilder.loadTexts:eventActiveAlarmCause.setStatus(_B)
_EventActiveAlarmSeverity_Type=AlarmSeverity
_EventActiveAlarmSeverity_Object=MibTableColumn
eventActiveAlarmSeverity=_EventActiveAlarmSeverity_Object((1,3,6,1,4,1,2928,2,1,1,6,1,6),_EventActiveAlarmSeverity_Type())
eventActiveAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:eventActiveAlarmSeverity.setStatus(_B)
_EventActiveAlarmText_Type=DisplayString
_EventActiveAlarmText_Object=MibTableColumn
eventActiveAlarmText=_EventActiveAlarmText_Object((1,3,6,1,4,1,2928,2,1,1,6,1,7),_EventActiveAlarmText_Type())
eventActiveAlarmText.setMaxAccess(_C)
if mibBuilder.loadTexts:eventActiveAlarmText.setStatus(_B)
_EventActiveAlarmLastChangedTime_Type=DateAndTime
_EventActiveAlarmLastChangedTime_Object=MibTableColumn
eventActiveAlarmLastChangedTime=_EventActiveAlarmLastChangedTime_Object((1,3,6,1,4,1,2928,2,1,1,6,1,8),_EventActiveAlarmLastChangedTime_Type())
eventActiveAlarmLastChangedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:eventActiveAlarmLastChangedTime.setStatus(_B)
_EventActiveAlarmAcknowledged_Type=TruthValue
_EventActiveAlarmAcknowledged_Object=MibTableColumn
eventActiveAlarmAcknowledged=_EventActiveAlarmAcknowledged_Object((1,3,6,1,4,1,2928,2,1,1,6,1,9),_EventActiveAlarmAcknowledged_Type())
eventActiveAlarmAcknowledged.setMaxAccess(_Q)
if mibBuilder.loadTexts:eventActiveAlarmAcknowledged.setStatus(_B)
_EventActiveAlarmCreatedTime_Type=DateAndTime
_EventActiveAlarmCreatedTime_Object=MibTableColumn
eventActiveAlarmCreatedTime=_EventActiveAlarmCreatedTime_Object((1,3,6,1,4,1,2928,2,1,1,6,1,10),_EventActiveAlarmCreatedTime_Type())
eventActiveAlarmCreatedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:eventActiveAlarmCreatedTime.setStatus(_B)
_EventNotificationObjectsGroup_ObjectIdentity=ObjectIdentity
eventNotificationObjectsGroup=_EventNotificationObjectsGroup_ObjectIdentity((1,3,6,1,4,1,2928,2,1,1,7))
_EventTrapPurpose_Type=SnmpAdminString
_EventTrapPurpose_Object=MibScalar
eventTrapPurpose=_EventTrapPurpose_Object((1,3,6,1,4,1,2928,2,1,1,7,1),_EventTrapPurpose_Type())
eventTrapPurpose.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:eventTrapPurpose.setStatus(_B)
_EventNotifications_ObjectIdentity=ObjectIdentity
eventNotifications=_EventNotifications_ObjectIdentity((1,3,6,1,4,1,2928,2,1,2))
_EventConformanceGroups_ObjectIdentity=ObjectIdentity
eventConformanceGroups=_EventConformanceGroups_ObjectIdentity((1,3,6,1,4,1,2928,2,1,3))
eventConformanceGroup=ObjectGroup((1,3,6,1,4,1,2928,2,1,3,1))
eventConformanceGroup.setObjects(*((_A,_E),(_A,_R),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_P),(_A,_K),(_A,_L),(_A,_H),(_A,_I),(_A,_N),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_O),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:eventConformanceGroup.setStatus(_B)
eventAlarmCritical=NotificationType((1,3,6,1,4,1,2928,2,1,2,1))
eventAlarmCritical.setObjects(*((_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_K),(_A,_L),(_A,_H),(_A,_I),(_A,_E)))
if mibBuilder.loadTexts:eventAlarmCritical.setStatus(_B)
eventAlarmMajor=NotificationType((1,3,6,1,4,1,2928,2,1,2,2))
eventAlarmMajor.setObjects(*((_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_K),(_A,_L),(_A,_H),(_A,_I),(_A,_E)))
if mibBuilder.loadTexts:eventAlarmMajor.setStatus(_B)
eventAlarmMinor=NotificationType((1,3,6,1,4,1,2928,2,1,2,3))
eventAlarmMinor.setObjects(*((_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_K),(_A,_L),(_A,_H),(_A,_I),(_A,_E)))
if mibBuilder.loadTexts:eventAlarmMinor.setStatus(_B)
eventAlarmWarning=NotificationType((1,3,6,1,4,1,2928,2,1,2,4))
eventAlarmWarning.setObjects(*((_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_K),(_A,_L),(_A,_H),(_A,_I),(_A,_E)))
if mibBuilder.loadTexts:eventAlarmWarning.setStatus(_B)
eventAlarmIndeterminate=NotificationType((1,3,6,1,4,1,2928,2,1,2,5))
eventAlarmIndeterminate.setObjects(*((_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_K),(_A,_L),(_A,_H),(_A,_I),(_A,_E)))
if mibBuilder.loadTexts:eventAlarmIndeterminate.setStatus(_B)
eventAlarmUnknown=NotificationType((1,3,6,1,4,1,2928,2,1,2,6))
eventAlarmUnknown.setObjects(*((_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_K),(_A,_L),(_A,_H),(_A,_I),(_A,_E)))
if mibBuilder.loadTexts:eventAlarmUnknown.setStatus(_B)
eventAlarmClear=NotificationType((1,3,6,1,4,1,2928,2,1,2,7))
eventAlarmClear.setObjects(*((_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_K),(_A,_L),(_A,_H),(_A,_I),(_A,_E)))
if mibBuilder.loadTexts:eventAlarmClear.setStatus(_B)
netiGenericEvent=NotificationType((1,3,6,1,4,1,2928,2,1,2,8))
netiGenericEvent.setObjects(*((_A,_F),(_A,_G),(_A,_P),(_A,_H),(_A,_I),(_A,_E)))
if mibBuilder.loadTexts:netiGenericEvent.setStatus(_B)
eventNotificationsGroup=NotificationGroup((1,3,6,1,4,1,2928,2,1,3,2))
eventNotificationsGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:eventNotificationsGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'EventType':EventType,'AlarmType':AlarmType,'AlarmSeverity':AlarmSeverity,'AlarmCause':AlarmCause,'netiEventMIB':netiEventMIB,'eventObjects':eventObjects,_E:eventSequenceCounter,_R:eventLogLastChangedTime,'eventTable':eventTable,'eventEntry':eventEntry,_D:eventIndex,_F:eventObject,_G:eventObjectName,_J:eventAlarmType,_P:eventType,_K:eventCause,_L:eventSeverity,_H:eventText,_I:eventCreatedTime,'eventAlarmTable':eventAlarmTable,'eventAlarmEntry':eventAlarmEntry,_N:eventAlarmIndex,_S:eventAlarmObject,_T:eventAlarmObjectName,_U:eventAlarmAlarmType,_V:eventAlarmCause,_W:eventAlarmSeverity,_X:eventAlarmText,_Y:eventAlarmLastChangedTime,_Z:eventAlarmAcknowledged,_a:eventAlarmCreatedTime,'eventAlarmCountersGroup':eventAlarmCountersGroup,_k:eventCriticalCounter,_l:eventMajorCounter,_m:eventMinorCounter,_n:eventWarningCounter,_o:eventIndeterminateCounter,'eventActiveAlarmTable':eventActiveAlarmTable,'eventActiveAlarmEntry':eventActiveAlarmEntry,_O:eventActiveAlarmIndex,_b:eventActiveAlarmObject,_c:eventActiveAlarmObjectName,_d:eventActiveAlarmAlarmType,_e:eventActiveAlarmCause,_f:eventActiveAlarmSeverity,_g:eventActiveAlarmText,_h:eventActiveAlarmLastChangedTime,_i:eventActiveAlarmAcknowledged,_j:eventActiveAlarmCreatedTime,'eventNotificationObjectsGroup':eventNotificationObjectsGroup,'eventTrapPurpose':eventTrapPurpose,'eventNotifications':eventNotifications,_p:eventAlarmCritical,_q:eventAlarmMajor,_r:eventAlarmMinor,_s:eventAlarmWarning,_t:eventAlarmIndeterminate,_u:eventAlarmUnknown,_v:eventAlarmClear,_w:netiGenericEvent,'eventConformanceGroups':eventConformanceGroups,'eventConformanceGroup':eventConformanceGroup,'eventNotificationsGroup':eventNotificationsGroup})