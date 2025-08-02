_U='neClearTerminatedAlarms'
_T='neAlarmTrapCounter'
_S='neAlarmTrapDestiPort'
_R='neAlarmTrapDestiIp'
_Q='neAlarmTrapFilter'
_P='neAlarmActivePhoto'
_O='neAlarmActiveLastTrapIndex'
_N='neAlarmStatus'
_M='neAlarmTimeStamp'
_L='neAlarmAlreadyPresent'
_K='neAlarmManagedObject'
_J='neAlarmType'
_I='neAlarmDescription'
_H='neAlarmProbableCause'
_G='neAlarmAdditionalText'
_F='neAlarmIndex'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='SPIDCOM-ALARM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
neMibAlarm,=mibBuilder.importSymbols('NE-ALARM-MIB','neMibAlarm')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
neAlarm=ModuleIdentity((1,3,6,1,4,1,22764,2,1))
class ItuAlarmProbableCause(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75)));namedValues=NamedValues(*(('other',1),('adapterError',2),('applicationSubsystemFailure',3),('bandwidthReduced',4),('callEstablishmentError',5),('communicationsProtocolError',6),('communicationsSubsystemFailure',7),('configurationOrCustomizationError',8),('congestion',9),('corruptData',10),('cpuCyclesLimitExceeded',11),('dataSetOrModemError',12),('degradedSignal',13),('dteDceInterfaceError',14),('enclosureDoorOpen',15),('equipmentMalfunction',16),('excessiveVibration',17),('fileError',18),('fireDetected',19),('floodDetected',20),('framingError',21),('heatingVentCoolingSystemProblem',22),('humidityUnacceptable',23),('inputOutputDeviceError',24),('inputDeviceError',25),('lanError',26),('leakDetected',27),('localNodeTransmissionError',28),('lossOfFrame',29),('lossOfSignal',30),('materialSupplyExhausted',31),('multiplexerProblem',32),('outOfMemory',33),('ouputDeviceError',34),('performanceDegraded',35),('powerProblem',36),('pressureUnacceptable',37),('processorProblem',38),('pumpFailure',39),('queueSizeExceeded',40),('receiveFailure',41),('receiverFailure',42),('remoteNodeTransmissionError',43),('resourceAtOrNearingCapacity',44),('responseTimeExecessive',45),('retransmissionRateExcessive',46),('softwareError',47),('softwareProgramAbnormallyTerminated',48),('softwareProgramError',49),('storageCapacityProblem',50),('temperatureUnacceptable',51),('thresholdCrossed',52),('timingProblem',53),('toxicLeakDetected',54),('transmitFailure',55),('transmitterFailure',56),('underlyingResourceUnavailable',57),('versionMismatch',58),('authenticationFailure',59),('breachOfConfidentiality',60),('cableTamper',61),('delayedInformation',62),('denialOfService',63),('duplicateInformation',64),('informationMissing',65),('informationModificationDetected',66),('informationOutOfSequence',67),('intrusionDetection',68),('keyExpired',69),('nonRepudiationFailure',70),('outOfHoursActivity',71),('outOfService',72),('proceduralError',73),('unauthorizedAccessAttempt',74),('unexpectedInformation',75)))
class ItuAlarmType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('other',1),('communicationsAlarm',2),('qualityOfServiceAlarm',3),('processingErrorAlarm',4),('equipmentAlarm',5),('environmentalAlarm',6),('integrityViolation',7),('operationalViolation',8),('physicalViolation',9),('securityServiceOrMechanismViolation',10),('timeDomainViolation',11)))
class NeAlarmPhoto(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('takePhoto',1))
class NeTrapFilter(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('trapFilterOff',0),('trapFilterOn',1)))
_NeAlarmTable_Object=MibTable
neAlarmTable=_NeAlarmTable_Object((1,3,6,1,4,1,22764,2,1,1))
if mibBuilder.loadTexts:neAlarmTable.setStatus(_A)
_NeAlarmEntry_Object=MibTableRow
neAlarmEntry=_NeAlarmEntry_Object((1,3,6,1,4,1,22764,2,1,1,1))
neAlarmEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:neAlarmEntry.setStatus(_A)
_NeAlarmIndex_Type=Unsigned32
_NeAlarmIndex_Object=MibTableColumn
neAlarmIndex=_NeAlarmIndex_Object((1,3,6,1,4,1,22764,2,1,1,1,1),_NeAlarmIndex_Type())
neAlarmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:neAlarmIndex.setStatus(_A)
_NeAlarmAdditionalText_Type=DisplayString
_NeAlarmAdditionalText_Object=MibTableColumn
neAlarmAdditionalText=_NeAlarmAdditionalText_Object((1,3,6,1,4,1,22764,2,1,1,1,2),_NeAlarmAdditionalText_Type())
neAlarmAdditionalText.setMaxAccess(_C)
if mibBuilder.loadTexts:neAlarmAdditionalText.setStatus(_A)
_NeAlarmProbableCause_Type=ItuAlarmProbableCause
_NeAlarmProbableCause_Object=MibTableColumn
neAlarmProbableCause=_NeAlarmProbableCause_Object((1,3,6,1,4,1,22764,2,1,1,1,3),_NeAlarmProbableCause_Type())
neAlarmProbableCause.setMaxAccess(_C)
if mibBuilder.loadTexts:neAlarmProbableCause.setStatus(_A)
_NeAlarmDescription_Type=DisplayString
_NeAlarmDescription_Object=MibTableColumn
neAlarmDescription=_NeAlarmDescription_Object((1,3,6,1,4,1,22764,2,1,1,1,4),_NeAlarmDescription_Type())
neAlarmDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:neAlarmDescription.setStatus(_A)
_NeAlarmType_Type=ItuAlarmType
_NeAlarmType_Object=MibTableColumn
neAlarmType=_NeAlarmType_Object((1,3,6,1,4,1,22764,2,1,1,1,5),_NeAlarmType_Type())
neAlarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:neAlarmType.setStatus(_A)
_NeAlarmManagedObject_Type=DisplayString
_NeAlarmManagedObject_Object=MibTableColumn
neAlarmManagedObject=_NeAlarmManagedObject_Object((1,3,6,1,4,1,22764,2,1,1,1,6),_NeAlarmManagedObject_Type())
neAlarmManagedObject.setMaxAccess(_C)
if mibBuilder.loadTexts:neAlarmManagedObject.setStatus(_A)
class _NeAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('inactive',2),('terminate',3)))
_NeAlarmStatus_Type.__name__=_E
_NeAlarmStatus_Object=MibTableColumn
neAlarmStatus=_NeAlarmStatus_Object((1,3,6,1,4,1,22764,2,1,1,1,7),_NeAlarmStatus_Type())
neAlarmStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:neAlarmStatus.setStatus(_A)
class _NeAlarmAlreadyPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_NeAlarmAlreadyPresent_Type.__name__=_E
_NeAlarmAlreadyPresent_Object=MibTableColumn
neAlarmAlreadyPresent=_NeAlarmAlreadyPresent_Object((1,3,6,1,4,1,22764,2,1,1,1,8),_NeAlarmAlreadyPresent_Type())
neAlarmAlreadyPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:neAlarmAlreadyPresent.setStatus(_A)
_NeAlarmTimeStamp_Type=TimeTicks
_NeAlarmTimeStamp_Object=MibTableColumn
neAlarmTimeStamp=_NeAlarmTimeStamp_Object((1,3,6,1,4,1,22764,2,1,1,1,9),_NeAlarmTimeStamp_Type())
neAlarmTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:neAlarmTimeStamp.setStatus(_A)
_NeAlarmActiveLastTrapIndex_Type=Unsigned32
_NeAlarmActiveLastTrapIndex_Object=MibScalar
neAlarmActiveLastTrapIndex=_NeAlarmActiveLastTrapIndex_Object((1,3,6,1,4,1,22764,2,1,2),_NeAlarmActiveLastTrapIndex_Type())
neAlarmActiveLastTrapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:neAlarmActiveLastTrapIndex.setStatus(_A)
class _NeClearTerminatedAlarms_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_NeClearTerminatedAlarms_Type.__name__=_E
_NeClearTerminatedAlarms_Object=MibScalar
neClearTerminatedAlarms=_NeClearTerminatedAlarms_Object((1,3,6,1,4,1,22764,2,1,3),_NeClearTerminatedAlarms_Type())
neClearTerminatedAlarms.setMaxAccess(_D)
if mibBuilder.loadTexts:neClearTerminatedAlarms.setStatus(_A)
class _NeAlarmActivePhoto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_NeAlarmActivePhoto_Type.__name__=_E
_NeAlarmActivePhoto_Object=MibScalar
neAlarmActivePhoto=_NeAlarmActivePhoto_Object((1,3,6,1,4,1,22764,2,1,4),_NeAlarmActivePhoto_Type())
neAlarmActivePhoto.setMaxAccess(_D)
if mibBuilder.loadTexts:neAlarmActivePhoto.setStatus(_A)
_NeAlarmTrap_ObjectIdentity=ObjectIdentity
neAlarmTrap=_NeAlarmTrap_ObjectIdentity((1,3,6,1,4,1,22764,2,1,10))
_NeAlarmTrapCounter_Type=Counter32
_NeAlarmTrapCounter_Object=MibScalar
neAlarmTrapCounter=_NeAlarmTrapCounter_Object((1,3,6,1,4,1,22764,2,1,10,2),_NeAlarmTrapCounter_Type())
neAlarmTrapCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:neAlarmTrapCounter.setStatus(_A)
_NeAlarmTrapFilter_Type=NeTrapFilter
_NeAlarmTrapFilter_Object=MibScalar
neAlarmTrapFilter=_NeAlarmTrapFilter_Object((1,3,6,1,4,1,22764,2,1,10,3),_NeAlarmTrapFilter_Type())
neAlarmTrapFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:neAlarmTrapFilter.setStatus(_A)
_NeAlarmTrapDestiIp_Type=IpAddress
_NeAlarmTrapDestiIp_Object=MibScalar
neAlarmTrapDestiIp=_NeAlarmTrapDestiIp_Object((1,3,6,1,4,1,22764,2,1,10,4),_NeAlarmTrapDestiIp_Type())
neAlarmTrapDestiIp.setMaxAccess(_D)
if mibBuilder.loadTexts:neAlarmTrapDestiIp.setStatus(_A)
_NeAlarmTrapDestiPort_Type=Unsigned32
_NeAlarmTrapDestiPort_Object=MibScalar
neAlarmTrapDestiPort=_NeAlarmTrapDestiPort_Object((1,3,6,1,4,1,22764,2,1,10,5),_NeAlarmTrapDestiPort_Type())
neAlarmTrapDestiPort.setMaxAccess(_D)
if mibBuilder.loadTexts:neAlarmTrapDestiPort.setStatus(_A)
neAlarmGroup=ObjectGroup((1,3,6,1,4,1,22764,2,1,11))
neAlarmGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:neAlarmGroup.setStatus(_A)
neAlarmActiveGroup=ObjectGroup((1,3,6,1,4,1,22764,2,1,13))
neAlarmActiveGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:neAlarmActiveGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ItuAlarmProbableCause':ItuAlarmProbableCause,'ItuAlarmType':ItuAlarmType,'NeAlarmPhoto':NeAlarmPhoto,'NeTrapFilter':NeTrapFilter,'neAlarm':neAlarm,'neAlarmTable':neAlarmTable,'neAlarmEntry':neAlarmEntry,_F:neAlarmIndex,_G:neAlarmAdditionalText,_H:neAlarmProbableCause,_I:neAlarmDescription,_J:neAlarmType,_K:neAlarmManagedObject,_N:neAlarmStatus,_L:neAlarmAlreadyPresent,_M:neAlarmTimeStamp,_O:neAlarmActiveLastTrapIndex,_U:neClearTerminatedAlarms,_P:neAlarmActivePhoto,'neAlarmTrap':neAlarmTrap,_T:neAlarmTrapCounter,_Q:neAlarmTrapFilter,_R:neAlarmTrapDestiIp,_S:neAlarmTrapDestiPort,'neAlarmGroup':neAlarmGroup,'neAlarmActiveGroup':neAlarmActiveGroup})