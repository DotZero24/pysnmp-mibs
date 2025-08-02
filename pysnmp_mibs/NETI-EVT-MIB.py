_R='nevtEventType'
_Q='nevtActiveAlarmIndex'
_P='read-write'
_O='nevtAlarmIndex'
_N='unknown'
_M='nevtEventSeverity'
_L='nevtEventCause'
_K='nevtEventAlarmType'
_J='nevtEventPurpose'
_I='nevtSequenceCounter'
_H='nevtEventCreatedTime'
_G='nevtEventText'
_F='nevtEventObjectName'
_E='nevtEventObject'
_D='nevtEventIndex'
_C='read-only'
_B='current'
_A='NETI-EVT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowPointer,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowPointer','TextualConvention','TruthValue')
nevtMIB=ModuleIdentity((1,3,6,1,4,1,2928,2,1))
if mibBuilder.loadTexts:nevtMIB.setRevisions(('2015-03-03 16:00','2013-06-03 11:00'))
class NevtEventType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('created',1),('modified',2),('deleted',3)))
class NevtAlarmType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_N,0),('communication',1),('qualityOfService',2),('processingError',3),('equipment',4),('environmental',5)))
class NevtAlarmSeverity(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_N,0),('indeterminate',1),('critical',2),('major',3),('minor',4),('warning',5),('cleared',6)))
class NevtAlarmCause(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69)));namedValues=NamedValues(*((_N,0),('adapterError',1),('applicationSubsystemFailure',2),('bandwidthReduced',3),('callEstablishmentError',4),('communicationsProtocolError',5),('communicationsSubsystemFailure',6),('configurationOrCustomizationError',7),('congestion',8),('corruptData',9),('cpuCyclesLimitExceeded',10),('datasetOrModemError',11),('degradedSignal',12),('dTEDCEInterfaceError',13),('enclosureDoorOpen',14),('equipmentMalfunction',15),('excessiveVibration',16),('fileError',17),('fireDetected',18),('floodDetected',19),('framingError',20),('heatingOrVentilationOrCoolingSystemProblem',21),('humidityUnacceptable',22),('inputOutputDeviceError',23),('inputDeviceError',24),('lANError',25),('leakDetected',26),('localNodeTransmissionError',27),('lossOfFrame',28),('lossOfSignal',29),('materialSupplyExhausted',30),('multiplexerProblem',31),('outOfMemory',32),('outputDeviceError',33),('performanceDegraded',34),('powerProblem',35),('pressureUnacceptable',36),('processorProblem',37),('pumpFailure',38),('queueSizeExceeded',39),('receiveFailure',40),('receiverFailure',41),('remoteNodeTransmissionError',42),('resourceAtOrNearingCapacity',43),('responseTimeExcessive',44),('retransmissionRateExcessive',45),('softwareError',46),('softwareProgramAbnormallyTerminated',47),('softwareProgramError',48),('storageCapacityProblem',49),('temperatureUnacceptable',50),('thresholdCrossed',51),('timingProblem',52),('toxicLeakDetected',53),('transmitFailure',54),('transmitterFailure',55),('underlyingResourceUnavailable',56),('versionMismatch',57),('phyLossOfSignal',58),('phyLossOfFrame',59),('phyAlarmIndicationSignal',60),('phyRemoteDefectIndication',61),('phySignalFailure',62),('phySignalDegraded',63),('testmodeEntered',64),('serviceUnavailable',65),('alarmIndicationSignal',66),('remoteDefectIndication',67),('replaceableUnitMissing',68),('replaceableUnitProblem',69)))
_Netinsight_ObjectIdentity=ObjectIdentity
netinsight=_Netinsight_ObjectIdentity((1,3,6,1,4,1,2928))
_NetiGeneric_ObjectIdentity=ObjectIdentity
netiGeneric=_NetiGeneric_ObjectIdentity((1,3,6,1,4,1,2928,2))
_NevtObjects_ObjectIdentity=ObjectIdentity
nevtObjects=_NevtObjects_ObjectIdentity((1,3,6,1,4,1,2928,2,1,1))
_NevtSequenceCounter_Type=Unsigned32
_NevtSequenceCounter_Object=MibScalar
nevtSequenceCounter=_NevtSequenceCounter_Object((1,3,6,1,4,1,2928,2,1,1,1),_NevtSequenceCounter_Type())
nevtSequenceCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtSequenceCounter.setStatus(_B)
_NevtLastChangedTime_Type=DateAndTime
_NevtLastChangedTime_Object=MibScalar
nevtLastChangedTime=_NevtLastChangedTime_Object((1,3,6,1,4,1,2928,2,1,1,2),_NevtLastChangedTime_Type())
nevtLastChangedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtLastChangedTime.setStatus(_B)
_NevtEventTable_Object=MibTable
nevtEventTable=_NevtEventTable_Object((1,3,6,1,4,1,2928,2,1,1,3))
if mibBuilder.loadTexts:nevtEventTable.setStatus(_B)
_NevtEventEntry_Object=MibTableRow
nevtEventEntry=_NevtEventEntry_Object((1,3,6,1,4,1,2928,2,1,1,3,1))
nevtEventEntry.setIndexNames((0,_A,_D))
if mibBuilder.loadTexts:nevtEventEntry.setStatus(_B)
_NevtEventIndex_Type=Unsigned32
_NevtEventIndex_Object=MibTableColumn
nevtEventIndex=_NevtEventIndex_Object((1,3,6,1,4,1,2928,2,1,1,3,1,1),_NevtEventIndex_Type())
nevtEventIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtEventIndex.setStatus(_B)
_NevtEventObject_Type=RowPointer
_NevtEventObject_Object=MibTableColumn
nevtEventObject=_NevtEventObject_Object((1,3,6,1,4,1,2928,2,1,1,3,1,2),_NevtEventObject_Type())
nevtEventObject.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtEventObject.setStatus(_B)
_NevtEventObjectName_Type=DisplayString
_NevtEventObjectName_Object=MibTableColumn
nevtEventObjectName=_NevtEventObjectName_Object((1,3,6,1,4,1,2928,2,1,1,3,1,3),_NevtEventObjectName_Type())
nevtEventObjectName.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtEventObjectName.setStatus(_B)
_NevtEventAlarmType_Type=NevtAlarmType
_NevtEventAlarmType_Object=MibTableColumn
nevtEventAlarmType=_NevtEventAlarmType_Object((1,3,6,1,4,1,2928,2,1,1,3,1,4),_NevtEventAlarmType_Type())
nevtEventAlarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtEventAlarmType.setStatus(_B)
_NevtEventType_Type=NevtEventType
_NevtEventType_Object=MibTableColumn
nevtEventType=_NevtEventType_Object((1,3,6,1,4,1,2928,2,1,1,3,1,5),_NevtEventType_Type())
nevtEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtEventType.setStatus(_B)
_NevtEventCause_Type=NevtAlarmCause
_NevtEventCause_Object=MibTableColumn
nevtEventCause=_NevtEventCause_Object((1,3,6,1,4,1,2928,2,1,1,3,1,6),_NevtEventCause_Type())
nevtEventCause.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtEventCause.setStatus(_B)
_NevtEventSeverity_Type=NevtAlarmSeverity
_NevtEventSeverity_Object=MibTableColumn
nevtEventSeverity=_NevtEventSeverity_Object((1,3,6,1,4,1,2928,2,1,1,3,1,7),_NevtEventSeverity_Type())
nevtEventSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtEventSeverity.setStatus(_B)
_NevtEventText_Type=DisplayString
_NevtEventText_Object=MibTableColumn
nevtEventText=_NevtEventText_Object((1,3,6,1,4,1,2928,2,1,1,3,1,8),_NevtEventText_Type())
nevtEventText.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtEventText.setStatus(_B)
_NevtEventCreatedTime_Type=DateAndTime
_NevtEventCreatedTime_Object=MibTableColumn
nevtEventCreatedTime=_NevtEventCreatedTime_Object((1,3,6,1,4,1,2928,2,1,1,3,1,9),_NevtEventCreatedTime_Type())
nevtEventCreatedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtEventCreatedTime.setStatus(_B)
_NevtEventPurpose_Type=SnmpAdminString
_NevtEventPurpose_Object=MibTableColumn
nevtEventPurpose=_NevtEventPurpose_Object((1,3,6,1,4,1,2928,2,1,1,3,1,10),_NevtEventPurpose_Type())
nevtEventPurpose.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtEventPurpose.setStatus(_B)
_NevtAlarmTable_Object=MibTable
nevtAlarmTable=_NevtAlarmTable_Object((1,3,6,1,4,1,2928,2,1,1,4))
if mibBuilder.loadTexts:nevtAlarmTable.setStatus(_B)
_NevtAlarmEntry_Object=MibTableRow
nevtAlarmEntry=_NevtAlarmEntry_Object((1,3,6,1,4,1,2928,2,1,1,4,1))
nevtAlarmEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:nevtAlarmEntry.setStatus(_B)
_NevtAlarmIndex_Type=Unsigned32
_NevtAlarmIndex_Object=MibTableColumn
nevtAlarmIndex=_NevtAlarmIndex_Object((1,3,6,1,4,1,2928,2,1,1,4,1,1),_NevtAlarmIndex_Type())
nevtAlarmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtAlarmIndex.setStatus(_B)
_NevtAlarmObject_Type=RowPointer
_NevtAlarmObject_Object=MibTableColumn
nevtAlarmObject=_NevtAlarmObject_Object((1,3,6,1,4,1,2928,2,1,1,4,1,2),_NevtAlarmObject_Type())
nevtAlarmObject.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtAlarmObject.setStatus(_B)
_NevtAlarmObjectName_Type=DisplayString
_NevtAlarmObjectName_Object=MibTableColumn
nevtAlarmObjectName=_NevtAlarmObjectName_Object((1,3,6,1,4,1,2928,2,1,1,4,1,3),_NevtAlarmObjectName_Type())
nevtAlarmObjectName.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtAlarmObjectName.setStatus(_B)
_NevtAlarmAlarmType_Type=NevtAlarmType
_NevtAlarmAlarmType_Object=MibTableColumn
nevtAlarmAlarmType=_NevtAlarmAlarmType_Object((1,3,6,1,4,1,2928,2,1,1,4,1,4),_NevtAlarmAlarmType_Type())
nevtAlarmAlarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtAlarmAlarmType.setStatus(_B)
_NevtAlarmCause_Type=NevtAlarmCause
_NevtAlarmCause_Object=MibTableColumn
nevtAlarmCause=_NevtAlarmCause_Object((1,3,6,1,4,1,2928,2,1,1,4,1,5),_NevtAlarmCause_Type())
nevtAlarmCause.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtAlarmCause.setStatus(_B)
_NevtAlarmSeverity_Type=NevtAlarmSeverity
_NevtAlarmSeverity_Object=MibTableColumn
nevtAlarmSeverity=_NevtAlarmSeverity_Object((1,3,6,1,4,1,2928,2,1,1,4,1,6),_NevtAlarmSeverity_Type())
nevtAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtAlarmSeverity.setStatus(_B)
_NevtAlarmText_Type=DisplayString
_NevtAlarmText_Object=MibTableColumn
nevtAlarmText=_NevtAlarmText_Object((1,3,6,1,4,1,2928,2,1,1,4,1,7),_NevtAlarmText_Type())
nevtAlarmText.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtAlarmText.setStatus(_B)
_NevtAlarmLastChangedTime_Type=DateAndTime
_NevtAlarmLastChangedTime_Object=MibTableColumn
nevtAlarmLastChangedTime=_NevtAlarmLastChangedTime_Object((1,3,6,1,4,1,2928,2,1,1,4,1,8),_NevtAlarmLastChangedTime_Type())
nevtAlarmLastChangedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtAlarmLastChangedTime.setStatus(_B)
_NevtAlarmAcknowledged_Type=TruthValue
_NevtAlarmAcknowledged_Object=MibTableColumn
nevtAlarmAcknowledged=_NevtAlarmAcknowledged_Object((1,3,6,1,4,1,2928,2,1,1,4,1,9),_NevtAlarmAcknowledged_Type())
nevtAlarmAcknowledged.setMaxAccess(_P)
if mibBuilder.loadTexts:nevtAlarmAcknowledged.setStatus(_B)
_NevtAlarmCreatedTime_Type=DateAndTime
_NevtAlarmCreatedTime_Object=MibTableColumn
nevtAlarmCreatedTime=_NevtAlarmCreatedTime_Object((1,3,6,1,4,1,2928,2,1,1,4,1,10),_NevtAlarmCreatedTime_Type())
nevtAlarmCreatedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtAlarmCreatedTime.setStatus(_B)
_NevtAlarmPurpose_Type=SnmpAdminString
_NevtAlarmPurpose_Object=MibTableColumn
nevtAlarmPurpose=_NevtAlarmPurpose_Object((1,3,6,1,4,1,2928,2,1,1,4,1,11),_NevtAlarmPurpose_Type())
nevtAlarmPurpose.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtAlarmPurpose.setStatus(_B)
_NevtAlarmCountersGroup_ObjectIdentity=ObjectIdentity
nevtAlarmCountersGroup=_NevtAlarmCountersGroup_ObjectIdentity((1,3,6,1,4,1,2928,2,1,1,5))
_NevtCriticalCounter_Type=Unsigned32
_NevtCriticalCounter_Object=MibScalar
nevtCriticalCounter=_NevtCriticalCounter_Object((1,3,6,1,4,1,2928,2,1,1,5,1),_NevtCriticalCounter_Type())
nevtCriticalCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtCriticalCounter.setStatus(_B)
_NevtMajorCounter_Type=Unsigned32
_NevtMajorCounter_Object=MibScalar
nevtMajorCounter=_NevtMajorCounter_Object((1,3,6,1,4,1,2928,2,1,1,5,2),_NevtMajorCounter_Type())
nevtMajorCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtMajorCounter.setStatus(_B)
_NevtMinorCounter_Type=Unsigned32
_NevtMinorCounter_Object=MibScalar
nevtMinorCounter=_NevtMinorCounter_Object((1,3,6,1,4,1,2928,2,1,1,5,3),_NevtMinorCounter_Type())
nevtMinorCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtMinorCounter.setStatus(_B)
_NevtWarningCounter_Type=Unsigned32
_NevtWarningCounter_Object=MibScalar
nevtWarningCounter=_NevtWarningCounter_Object((1,3,6,1,4,1,2928,2,1,1,5,4),_NevtWarningCounter_Type())
nevtWarningCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtWarningCounter.setStatus(_B)
_NevtIndeterminateCounter_Type=Unsigned32
_NevtIndeterminateCounter_Object=MibScalar
nevtIndeterminateCounter=_NevtIndeterminateCounter_Object((1,3,6,1,4,1,2928,2,1,1,5,5),_NevtIndeterminateCounter_Type())
nevtIndeterminateCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtIndeterminateCounter.setStatus(_B)
_NevtActiveAlarmTable_Object=MibTable
nevtActiveAlarmTable=_NevtActiveAlarmTable_Object((1,3,6,1,4,1,2928,2,1,1,6))
if mibBuilder.loadTexts:nevtActiveAlarmTable.setStatus(_B)
_NevtActiveAlarmEntry_Object=MibTableRow
nevtActiveAlarmEntry=_NevtActiveAlarmEntry_Object((1,3,6,1,4,1,2928,2,1,1,6,1))
nevtActiveAlarmEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:nevtActiveAlarmEntry.setStatus(_B)
_NevtActiveAlarmIndex_Type=Unsigned32
_NevtActiveAlarmIndex_Object=MibTableColumn
nevtActiveAlarmIndex=_NevtActiveAlarmIndex_Object((1,3,6,1,4,1,2928,2,1,1,6,1,1),_NevtActiveAlarmIndex_Type())
nevtActiveAlarmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtActiveAlarmIndex.setStatus(_B)
_NevtActiveAlarmObject_Type=RowPointer
_NevtActiveAlarmObject_Object=MibTableColumn
nevtActiveAlarmObject=_NevtActiveAlarmObject_Object((1,3,6,1,4,1,2928,2,1,1,6,1,2),_NevtActiveAlarmObject_Type())
nevtActiveAlarmObject.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtActiveAlarmObject.setStatus(_B)
_NevtActiveAlarmObjectName_Type=DisplayString
_NevtActiveAlarmObjectName_Object=MibTableColumn
nevtActiveAlarmObjectName=_NevtActiveAlarmObjectName_Object((1,3,6,1,4,1,2928,2,1,1,6,1,3),_NevtActiveAlarmObjectName_Type())
nevtActiveAlarmObjectName.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtActiveAlarmObjectName.setStatus(_B)
_NevtActiveAlarmAlarmType_Type=NevtAlarmType
_NevtActiveAlarmAlarmType_Object=MibTableColumn
nevtActiveAlarmAlarmType=_NevtActiveAlarmAlarmType_Object((1,3,6,1,4,1,2928,2,1,1,6,1,4),_NevtActiveAlarmAlarmType_Type())
nevtActiveAlarmAlarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtActiveAlarmAlarmType.setStatus(_B)
_NevtActiveAlarmCause_Type=NevtAlarmCause
_NevtActiveAlarmCause_Object=MibTableColumn
nevtActiveAlarmCause=_NevtActiveAlarmCause_Object((1,3,6,1,4,1,2928,2,1,1,6,1,5),_NevtActiveAlarmCause_Type())
nevtActiveAlarmCause.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtActiveAlarmCause.setStatus(_B)
_NevtActiveAlarmSeverity_Type=NevtAlarmSeverity
_NevtActiveAlarmSeverity_Object=MibTableColumn
nevtActiveAlarmSeverity=_NevtActiveAlarmSeverity_Object((1,3,6,1,4,1,2928,2,1,1,6,1,6),_NevtActiveAlarmSeverity_Type())
nevtActiveAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtActiveAlarmSeverity.setStatus(_B)
_NevtActiveAlarmText_Type=DisplayString
_NevtActiveAlarmText_Object=MibTableColumn
nevtActiveAlarmText=_NevtActiveAlarmText_Object((1,3,6,1,4,1,2928,2,1,1,6,1,7),_NevtActiveAlarmText_Type())
nevtActiveAlarmText.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtActiveAlarmText.setStatus(_B)
_NevtActiveAlarmLastChangedTime_Type=DateAndTime
_NevtActiveAlarmLastChangedTime_Object=MibTableColumn
nevtActiveAlarmLastChangedTime=_NevtActiveAlarmLastChangedTime_Object((1,3,6,1,4,1,2928,2,1,1,6,1,8),_NevtActiveAlarmLastChangedTime_Type())
nevtActiveAlarmLastChangedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtActiveAlarmLastChangedTime.setStatus(_B)
_NevtActiveAlarmAcknowledged_Type=TruthValue
_NevtActiveAlarmAcknowledged_Object=MibTableColumn
nevtActiveAlarmAcknowledged=_NevtActiveAlarmAcknowledged_Object((1,3,6,1,4,1,2928,2,1,1,6,1,9),_NevtActiveAlarmAcknowledged_Type())
nevtActiveAlarmAcknowledged.setMaxAccess(_P)
if mibBuilder.loadTexts:nevtActiveAlarmAcknowledged.setStatus(_B)
_NevtActiveAlarmCreatedTime_Type=DateAndTime
_NevtActiveAlarmCreatedTime_Object=MibTableColumn
nevtActiveAlarmCreatedTime=_NevtActiveAlarmCreatedTime_Object((1,3,6,1,4,1,2928,2,1,1,6,1,10),_NevtActiveAlarmCreatedTime_Type())
nevtActiveAlarmCreatedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtActiveAlarmCreatedTime.setStatus(_B)
_NevtActiveAlarmPurpose_Type=SnmpAdminString
_NevtActiveAlarmPurpose_Object=MibTableColumn
nevtActiveAlarmPurpose=_NevtActiveAlarmPurpose_Object((1,3,6,1,4,1,2928,2,1,1,6,1,11),_NevtActiveAlarmPurpose_Type())
nevtActiveAlarmPurpose.setMaxAccess(_C)
if mibBuilder.loadTexts:nevtActiveAlarmPurpose.setStatus(_B)
_NevtNotificationObjectsGroup_ObjectIdentity=ObjectIdentity
nevtNotificationObjectsGroup=_NevtNotificationObjectsGroup_ObjectIdentity((1,3,6,1,4,1,2928,2,1,1,7))
_NevtTrapPurpose_Type=SnmpAdminString
_NevtTrapPurpose_Object=MibScalar
nevtTrapPurpose=_NevtTrapPurpose_Object((1,3,6,1,4,1,2928,2,1,1,7,1),_NevtTrapPurpose_Type())
nevtTrapPurpose.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:nevtTrapPurpose.setStatus('obsolete')
_NevtNotifications_ObjectIdentity=ObjectIdentity
nevtNotifications=_NevtNotifications_ObjectIdentity((1,3,6,1,4,1,2928,2,1,2))
_NevtConformanceGroups_ObjectIdentity=ObjectIdentity
nevtConformanceGroups=_NevtConformanceGroups_ObjectIdentity((1,3,6,1,4,1,2928,2,1,3))
nevtAlarmCritical=NotificationType((1,3,6,1,4,1,2928,2,1,2,1))
nevtAlarmCritical.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_K),(_A,_L),(_A,_M),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:nevtAlarmCritical.setStatus(_B)
nevtAlarmMajor=NotificationType((1,3,6,1,4,1,2928,2,1,2,2))
nevtAlarmMajor.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_K),(_A,_L),(_A,_M),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:nevtAlarmMajor.setStatus(_B)
nevtAlarmMinor=NotificationType((1,3,6,1,4,1,2928,2,1,2,3))
nevtAlarmMinor.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_K),(_A,_L),(_A,_M),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:nevtAlarmMinor.setStatus(_B)
nevtAlarmWarning=NotificationType((1,3,6,1,4,1,2928,2,1,2,4))
nevtAlarmWarning.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_K),(_A,_L),(_A,_M),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:nevtAlarmWarning.setStatus(_B)
nevtAlarmIndeterminate=NotificationType((1,3,6,1,4,1,2928,2,1,2,5))
nevtAlarmIndeterminate.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_K),(_A,_L),(_A,_M),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:nevtAlarmIndeterminate.setStatus(_B)
nevtAlarmUnknown=NotificationType((1,3,6,1,4,1,2928,2,1,2,6))
nevtAlarmUnknown.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_K),(_A,_L),(_A,_M),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:nevtAlarmUnknown.setStatus(_B)
nevtAlarmClear=NotificationType((1,3,6,1,4,1,2928,2,1,2,7))
nevtAlarmClear.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_K),(_A,_L),(_A,_M),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:nevtAlarmClear.setStatus(_B)
nevtGenericEvent=NotificationType((1,3,6,1,4,1,2928,2,1,2,8))
nevtGenericEvent.setObjects(*((_A,_E),(_A,_F),(_A,_R),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:nevtGenericEvent.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'NevtEventType':NevtEventType,'NevtAlarmType':NevtAlarmType,'NevtAlarmSeverity':NevtAlarmSeverity,'NevtAlarmCause':NevtAlarmCause,'netinsight':netinsight,'netiGeneric':netiGeneric,'nevtMIB':nevtMIB,'nevtObjects':nevtObjects,_I:nevtSequenceCounter,'nevtLastChangedTime':nevtLastChangedTime,'nevtEventTable':nevtEventTable,'nevtEventEntry':nevtEventEntry,_D:nevtEventIndex,_E:nevtEventObject,_F:nevtEventObjectName,_K:nevtEventAlarmType,_R:nevtEventType,_L:nevtEventCause,_M:nevtEventSeverity,_G:nevtEventText,_H:nevtEventCreatedTime,_J:nevtEventPurpose,'nevtAlarmTable':nevtAlarmTable,'nevtAlarmEntry':nevtAlarmEntry,_O:nevtAlarmIndex,'nevtAlarmObject':nevtAlarmObject,'nevtAlarmObjectName':nevtAlarmObjectName,'nevtAlarmAlarmType':nevtAlarmAlarmType,'nevtAlarmCause':nevtAlarmCause,'nevtAlarmSeverity':nevtAlarmSeverity,'nevtAlarmText':nevtAlarmText,'nevtAlarmLastChangedTime':nevtAlarmLastChangedTime,'nevtAlarmAcknowledged':nevtAlarmAcknowledged,'nevtAlarmCreatedTime':nevtAlarmCreatedTime,'nevtAlarmPurpose':nevtAlarmPurpose,'nevtAlarmCountersGroup':nevtAlarmCountersGroup,'nevtCriticalCounter':nevtCriticalCounter,'nevtMajorCounter':nevtMajorCounter,'nevtMinorCounter':nevtMinorCounter,'nevtWarningCounter':nevtWarningCounter,'nevtIndeterminateCounter':nevtIndeterminateCounter,'nevtActiveAlarmTable':nevtActiveAlarmTable,'nevtActiveAlarmEntry':nevtActiveAlarmEntry,_Q:nevtActiveAlarmIndex,'nevtActiveAlarmObject':nevtActiveAlarmObject,'nevtActiveAlarmObjectName':nevtActiveAlarmObjectName,'nevtActiveAlarmAlarmType':nevtActiveAlarmAlarmType,'nevtActiveAlarmCause':nevtActiveAlarmCause,'nevtActiveAlarmSeverity':nevtActiveAlarmSeverity,'nevtActiveAlarmText':nevtActiveAlarmText,'nevtActiveAlarmLastChangedTime':nevtActiveAlarmLastChangedTime,'nevtActiveAlarmAcknowledged':nevtActiveAlarmAcknowledged,'nevtActiveAlarmCreatedTime':nevtActiveAlarmCreatedTime,'nevtActiveAlarmPurpose':nevtActiveAlarmPurpose,'nevtNotificationObjectsGroup':nevtNotificationObjectsGroup,'nevtTrapPurpose':nevtTrapPurpose,'nevtNotifications':nevtNotifications,'nevtAlarmCritical':nevtAlarmCritical,'nevtAlarmMajor':nevtAlarmMajor,'nevtAlarmMinor':nevtAlarmMinor,'nevtAlarmWarning':nevtAlarmWarning,'nevtAlarmIndeterminate':nevtAlarmIndeterminate,'nevtAlarmUnknown':nevtAlarmUnknown,'nevtAlarmClear':nevtAlarmClear,'nevtGenericEvent':nevtGenericEvent,'nevtConformanceGroups':nevtConformanceGroups})