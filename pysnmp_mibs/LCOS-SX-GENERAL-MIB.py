_T='lcsNotificationTemperatureStatusPrevious'
_S='lcsNotificationTemperatureStatusCurrent'
_R='lcsLMCTransportStatusTransportNumberIndex'
_Q='lcsMonitoringPSUUnitIndex'
_P='lcsMonitoringFanUnitIndex'
_O='lcsMonitoringTempSensorIndex'
_N='lcsMonitoringTempSensorUnitIndex'
_M='warning'
_L='notpresent'
_K='lcsNotificationStateChangeEvent'
_J='lcsMonitoringPSUIndex'
_I='lcsMonitoringFanIndex'
_H='lcsMonitoringTempUnitIndex'
_G='accessible-for-notify'
_F='Integer32'
_E='read-write'
_D='Unsigned32'
_C='LCOS-SX-GENERAL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
lcosSXGeneral=ModuleIdentity((1,3,6,1,4,1,2356,100))
if mibBuilder.loadTexts:lcosSXGeneral.setRevisions(('2020-06-23 00:00',))
class MonitoringSensorType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('fixed',1),('removable',2),('fixedAC',3),('removableDC',4),('fixedDC',5),('removableAC',6)))
class MonitoringModuleStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_L,1),('operational',2),('failed',3),('powering',4),('nopower',5),('notpowering',6),('incompatible',7),(_M,8),('present',9)))
class MonitoringTempSensorStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('low',0),('normal',1),(_M,2),('critical',3),('shutdown',4),(_L,5),('notoperational',6)))
class LMCStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('unpaired',0),('paired',1),('disabled',2),('disabledByWLC',3),('operating',4),('httpProtocolError',5),('httpConnectionError',6),('dnsError',7),('memoryError',8),('notYet',9),('redirect',10),('authenticationError',11),('error',12),('certificateStorageError',13),('pairedAndClaimed',14),('certificateError',15),('deactivatedNoActivationCode',16)))
_LcsNotificationGrp_ObjectIdentity=ObjectIdentity
lcsNotificationGrp=_LcsNotificationGrp_ObjectIdentity((1,3,6,1,4,1,2356,100,0))
_LcsTraps_ObjectIdentity=ObjectIdentity
lcsTraps=_LcsTraps_ObjectIdentity((1,3,6,1,4,1,2356,100,0,1))
_LcsNotificationVars_ObjectIdentity=ObjectIdentity
lcsNotificationVars=_LcsNotificationVars_ObjectIdentity((1,3,6,1,4,1,2356,100,0,2))
class _LcsNotificationStateChangeEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('insertion',1),('removal',2),('becomeoperational',3),('failure',4),('losepower',5)))
_LcsNotificationStateChangeEvent_Type.__name__=_F
_LcsNotificationStateChangeEvent_Object=MibScalar
lcsNotificationStateChangeEvent=_LcsNotificationStateChangeEvent_Object((1,3,6,1,4,1,2356,100,0,2,100),_LcsNotificationStateChangeEvent_Type())
lcsNotificationStateChangeEvent.setMaxAccess(_G)
if mibBuilder.loadTexts:lcsNotificationStateChangeEvent.setStatus(_A)
_LcsNotificationTemperatureStatusCurrent_Type=MonitoringTempSensorStatus
_LcsNotificationTemperatureStatusCurrent_Object=MibScalar
lcsNotificationTemperatureStatusCurrent=_LcsNotificationTemperatureStatusCurrent_Object((1,3,6,1,4,1,2356,100,0,2,101),_LcsNotificationTemperatureStatusCurrent_Type())
lcsNotificationTemperatureStatusCurrent.setMaxAccess(_G)
if mibBuilder.loadTexts:lcsNotificationTemperatureStatusCurrent.setStatus(_A)
_LcsNotificationTemperatureStatusPrevious_Type=MonitoringTempSensorStatus
_LcsNotificationTemperatureStatusPrevious_Object=MibScalar
lcsNotificationTemperatureStatusPrevious=_LcsNotificationTemperatureStatusPrevious_Object((1,3,6,1,4,1,2356,100,0,2,102),_LcsNotificationTemperatureStatusPrevious_Type())
lcsNotificationTemperatureStatusPrevious.setMaxAccess(_G)
if mibBuilder.loadTexts:lcsNotificationTemperatureStatusPrevious.setStatus(_A)
_LcsStatus_ObjectIdentity=ObjectIdentity
lcsStatus=_LcsStatus_ObjectIdentity((1,3,6,1,4,1,2356,100,1))
_LcsMonitoring_ObjectIdentity=ObjectIdentity
lcsMonitoring=_LcsMonitoring_ObjectIdentity((1,3,6,1,4,1,2356,100,1,1))
_LcsMonitoringTempSensorsTable_Object=MibTable
lcsMonitoringTempSensorsTable=_LcsMonitoringTempSensorsTable_Object((1,3,6,1,4,1,2356,100,1,1,1))
if mibBuilder.loadTexts:lcsMonitoringTempSensorsTable.setStatus(_A)
_LcsMonitoringTempSensorsTableEntry_Object=MibTableRow
lcsMonitoringTempSensorsTableEntry=_LcsMonitoringTempSensorsTableEntry_Object((1,3,6,1,4,1,2356,100,1,1,1,1))
lcsMonitoringTempSensorsTableEntry.setIndexNames((0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:lcsMonitoringTempSensorsTableEntry.setStatus(_A)
class _LcsMonitoringTempSensorUnitIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_LcsMonitoringTempSensorUnitIndex_Type.__name__=_D
_LcsMonitoringTempSensorUnitIndex_Object=MibTableColumn
lcsMonitoringTempSensorUnitIndex=_LcsMonitoringTempSensorUnitIndex_Object((1,3,6,1,4,1,2356,100,1,1,1,1,1),_LcsMonitoringTempSensorUnitIndex_Type())
lcsMonitoringTempSensorUnitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsMonitoringTempSensorUnitIndex.setStatus(_A)
class _LcsMonitoringTempSensorIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_LcsMonitoringTempSensorIndex_Type.__name__=_D
_LcsMonitoringTempSensorIndex_Object=MibTableColumn
lcsMonitoringTempSensorIndex=_LcsMonitoringTempSensorIndex_Object((1,3,6,1,4,1,2356,100,1,1,1,1,2),_LcsMonitoringTempSensorIndex_Type())
lcsMonitoringTempSensorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsMonitoringTempSensorIndex.setStatus(_A)
_LcsMonitoringTempSensorDescription_Type=DisplayString
_LcsMonitoringTempSensorDescription_Object=MibTableColumn
lcsMonitoringTempSensorDescription=_LcsMonitoringTempSensorDescription_Object((1,3,6,1,4,1,2356,100,1,1,1,1,3),_LcsMonitoringTempSensorDescription_Type())
lcsMonitoringTempSensorDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsMonitoringTempSensorDescription.setStatus(_A)
_LcsMonitoringTempSensorType_Type=MonitoringSensorType
_LcsMonitoringTempSensorType_Object=MibTableColumn
lcsMonitoringTempSensorType=_LcsMonitoringTempSensorType_Object((1,3,6,1,4,1,2356,100,1,1,1,1,4),_LcsMonitoringTempSensorType_Type())
lcsMonitoringTempSensorType.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsMonitoringTempSensorType.setStatus(_A)
_LcsMonitoringTempSensorState_Type=MonitoringTempSensorStatus
_LcsMonitoringTempSensorState_Object=MibTableColumn
lcsMonitoringTempSensorState=_LcsMonitoringTempSensorState_Object((1,3,6,1,4,1,2356,100,1,1,1,1,5),_LcsMonitoringTempSensorState_Type())
lcsMonitoringTempSensorState.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsMonitoringTempSensorState.setStatus(_A)
_LcsMonitoringTempSensorTemperature_Type=Integer32
_LcsMonitoringTempSensorTemperature_Object=MibTableColumn
lcsMonitoringTempSensorTemperature=_LcsMonitoringTempSensorTemperature_Object((1,3,6,1,4,1,2356,100,1,1,1,1,6),_LcsMonitoringTempSensorTemperature_Type())
lcsMonitoringTempSensorTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsMonitoringTempSensorTemperature.setStatus(_A)
_LcsMonitoringTempUnitTable_Object=MibTable
lcsMonitoringTempUnitTable=_LcsMonitoringTempUnitTable_Object((1,3,6,1,4,1,2356,100,1,1,2))
if mibBuilder.loadTexts:lcsMonitoringTempUnitTable.setStatus(_A)
_LcsMonitoringTempUnitEntry_Object=MibTableRow
lcsMonitoringTempUnitEntry=_LcsMonitoringTempUnitEntry_Object((1,3,6,1,4,1,2356,100,1,1,2,1))
lcsMonitoringTempUnitEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:lcsMonitoringTempUnitEntry.setStatus(_A)
class _LcsMonitoringTempUnitIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_LcsMonitoringTempUnitIndex_Type.__name__=_D
_LcsMonitoringTempUnitIndex_Object=MibTableColumn
lcsMonitoringTempUnitIndex=_LcsMonitoringTempUnitIndex_Object((1,3,6,1,4,1,2356,100,1,1,2,1,1),_LcsMonitoringTempUnitIndex_Type())
lcsMonitoringTempUnitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsMonitoringTempUnitIndex.setStatus(_A)
_LcsMonitoringTempUnitState_Type=MonitoringTempSensorStatus
_LcsMonitoringTempUnitState_Object=MibTableColumn
lcsMonitoringTempUnitState=_LcsMonitoringTempUnitState_Object((1,3,6,1,4,1,2356,100,1,1,2,1,2),_LcsMonitoringTempUnitState_Type())
lcsMonitoringTempUnitState.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsMonitoringTempUnitState.setStatus(_A)
_LcsMonitoringTempUnitTemperature_Type=Integer32
_LcsMonitoringTempUnitTemperature_Object=MibTableColumn
lcsMonitoringTempUnitTemperature=_LcsMonitoringTempUnitTemperature_Object((1,3,6,1,4,1,2356,100,1,1,2,1,3),_LcsMonitoringTempUnitTemperature_Type())
lcsMonitoringTempUnitTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsMonitoringTempUnitTemperature.setStatus(_A)
_LcsMonitoringFansTable_Object=MibTable
lcsMonitoringFansTable=_LcsMonitoringFansTable_Object((1,3,6,1,4,1,2356,100,1,1,3))
if mibBuilder.loadTexts:lcsMonitoringFansTable.setStatus(_A)
_LcsMonitoringFansTableEntry_Object=MibTableRow
lcsMonitoringFansTableEntry=_LcsMonitoringFansTableEntry_Object((1,3,6,1,4,1,2356,100,1,1,3,1))
lcsMonitoringFansTableEntry.setIndexNames((0,_C,_P),(0,_C,_I))
if mibBuilder.loadTexts:lcsMonitoringFansTableEntry.setStatus(_A)
class _LcsMonitoringFanUnitIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_LcsMonitoringFanUnitIndex_Type.__name__=_D
_LcsMonitoringFanUnitIndex_Object=MibTableColumn
lcsMonitoringFanUnitIndex=_LcsMonitoringFanUnitIndex_Object((1,3,6,1,4,1,2356,100,1,1,3,1,1),_LcsMonitoringFanUnitIndex_Type())
lcsMonitoringFanUnitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsMonitoringFanUnitIndex.setStatus(_A)
class _LcsMonitoringFanIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_LcsMonitoringFanIndex_Type.__name__=_D
_LcsMonitoringFanIndex_Object=MibTableColumn
lcsMonitoringFanIndex=_LcsMonitoringFanIndex_Object((1,3,6,1,4,1,2356,100,1,1,3,1,2),_LcsMonitoringFanIndex_Type())
lcsMonitoringFanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsMonitoringFanIndex.setStatus(_A)
_LcsMonitoringFanDescription_Type=DisplayString
_LcsMonitoringFanDescription_Object=MibTableColumn
lcsMonitoringFanDescription=_LcsMonitoringFanDescription_Object((1,3,6,1,4,1,2356,100,1,1,3,1,3),_LcsMonitoringFanDescription_Type())
lcsMonitoringFanDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsMonitoringFanDescription.setStatus(_A)
_LcsMonitoringFanType_Type=MonitoringSensorType
_LcsMonitoringFanType_Object=MibTableColumn
lcsMonitoringFanType=_LcsMonitoringFanType_Object((1,3,6,1,4,1,2356,100,1,1,3,1,4),_LcsMonitoringFanType_Type())
lcsMonitoringFanType.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsMonitoringFanType.setStatus(_A)
_LcsMonitoringFanState_Type=MonitoringModuleStatus
_LcsMonitoringFanState_Object=MibTableColumn
lcsMonitoringFanState=_LcsMonitoringFanState_Object((1,3,6,1,4,1,2356,100,1,1,3,1,5),_LcsMonitoringFanState_Type())
lcsMonitoringFanState.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsMonitoringFanState.setStatus(_A)
_LcsMonitoringFanSpeed_Type=Gauge32
_LcsMonitoringFanSpeed_Object=MibScalar
lcsMonitoringFanSpeed=_LcsMonitoringFanSpeed_Object((1,3,6,1,4,1,2356,100,1,1,3,1,6),_LcsMonitoringFanSpeed_Type())
lcsMonitoringFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsMonitoringFanSpeed.setStatus(_A)
_LcsMonitoringPSUTable_Object=MibTable
lcsMonitoringPSUTable=_LcsMonitoringPSUTable_Object((1,3,6,1,4,1,2356,100,1,1,4))
if mibBuilder.loadTexts:lcsMonitoringPSUTable.setStatus(_A)
_LcsMonitoringPSUTableEntry_Object=MibTableRow
lcsMonitoringPSUTableEntry=_LcsMonitoringPSUTableEntry_Object((1,3,6,1,4,1,2356,100,1,1,4,1))
lcsMonitoringPSUTableEntry.setIndexNames((0,_C,_Q),(0,_C,_J))
if mibBuilder.loadTexts:lcsMonitoringPSUTableEntry.setStatus(_A)
class _LcsMonitoringPSUUnitIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_LcsMonitoringPSUUnitIndex_Type.__name__=_D
_LcsMonitoringPSUUnitIndex_Object=MibTableColumn
lcsMonitoringPSUUnitIndex=_LcsMonitoringPSUUnitIndex_Object((1,3,6,1,4,1,2356,100,1,1,4,1,1),_LcsMonitoringPSUUnitIndex_Type())
lcsMonitoringPSUUnitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsMonitoringPSUUnitIndex.setStatus(_A)
class _LcsMonitoringPSUIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_LcsMonitoringPSUIndex_Type.__name__=_D
_LcsMonitoringPSUIndex_Object=MibTableColumn
lcsMonitoringPSUIndex=_LcsMonitoringPSUIndex_Object((1,3,6,1,4,1,2356,100,1,1,4,1,2),_LcsMonitoringPSUIndex_Type())
lcsMonitoringPSUIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsMonitoringPSUIndex.setStatus(_A)
_LcsMonitoringPSUDescription_Type=DisplayString
_LcsMonitoringPSUDescription_Object=MibTableColumn
lcsMonitoringPSUDescription=_LcsMonitoringPSUDescription_Object((1,3,6,1,4,1,2356,100,1,1,4,1,3),_LcsMonitoringPSUDescription_Type())
lcsMonitoringPSUDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsMonitoringPSUDescription.setStatus(_A)
_LcsMonitoringPSUType_Type=MonitoringSensorType
_LcsMonitoringPSUType_Object=MibTableColumn
lcsMonitoringPSUType=_LcsMonitoringPSUType_Object((1,3,6,1,4,1,2356,100,1,1,4,1,4),_LcsMonitoringPSUType_Type())
lcsMonitoringPSUType.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsMonitoringPSUType.setStatus(_A)
_LcsMonitoringPSUState_Type=MonitoringModuleStatus
_LcsMonitoringPSUState_Object=MibTableColumn
lcsMonitoringPSUState=_LcsMonitoringPSUState_Object((1,3,6,1,4,1,2356,100,1,1,4,1,5),_LcsMonitoringPSUState_Type())
lcsMonitoringPSUState.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsMonitoringPSUState.setStatus(_A)
_LcsConfiguration_ObjectIdentity=ObjectIdentity
lcsConfiguration=_LcsConfiguration_ObjectIdentity((1,3,6,1,4,1,2356,100,2))
_LcsLMC_ObjectIdentity=ObjectIdentity
lcsLMC=_LcsLMC_ObjectIdentity((1,3,6,1,4,1,2356,100,2,1500))
_LcsLMCOperating_Type=Unsigned32
_LcsLMCOperating_Object=MibScalar
lcsLMCOperating=_LcsLMCOperating_Object((1,3,6,1,4,1,2356,100,2,1500,1),_LcsLMCOperating_Type())
lcsLMCOperating.setMaxAccess(_E)
if mibBuilder.loadTexts:lcsLMCOperating.setStatus(_A)
_LcsLMCConfigViaDHCP_Type=Unsigned32
_LcsLMCConfigViaDHCP_Object=MibScalar
lcsLMCConfigViaDHCP=_LcsLMCConfigViaDHCP_Object((1,3,6,1,4,1,2356,100,2,1500,2),_LcsLMCConfigViaDHCP_Type())
lcsLMCConfigViaDHCP.setMaxAccess(_E)
if mibBuilder.loadTexts:lcsLMCConfigViaDHCP.setStatus(_A)
_LcsLMCDomain_Type=DisplayString
_LcsLMCDomain_Object=MibScalar
lcsLMCDomain=_LcsLMCDomain_Object((1,3,6,1,4,1,2356,100,2,1500,3),_LcsLMCDomain_Type())
lcsLMCDomain.setMaxAccess(_E)
if mibBuilder.loadTexts:lcsLMCDomain.setStatus(_A)
_LcsLMCAutoRenew_Type=Unsigned32
_LcsLMCAutoRenew_Object=MibScalar
lcsLMCAutoRenew=_LcsLMCAutoRenew_Object((1,3,6,1,4,1,2356,100,2,1500,4),_LcsLMCAutoRenew_Type())
lcsLMCAutoRenew.setMaxAccess(_E)
if mibBuilder.loadTexts:lcsLMCAutoRenew.setStatus(_A)
_LcsLMCRolloutProjectID_Type=DisplayString
_LcsLMCRolloutProjectID_Object=MibScalar
lcsLMCRolloutProjectID=_LcsLMCRolloutProjectID_Object((1,3,6,1,4,1,2356,100,2,1500,5),_LcsLMCRolloutProjectID_Type())
lcsLMCRolloutProjectID.setMaxAccess(_E)
if mibBuilder.loadTexts:lcsLMCRolloutProjectID.setStatus(_A)
_LcsLMCRolloutLocationID_Type=DisplayString
_LcsLMCRolloutLocationID_Object=MibScalar
lcsLMCRolloutLocationID=_LcsLMCRolloutLocationID_Object((1,3,6,1,4,1,2356,100,2,1500,6),_LcsLMCRolloutLocationID_Type())
lcsLMCRolloutLocationID.setMaxAccess(_E)
if mibBuilder.loadTexts:lcsLMCRolloutLocationID.setStatus(_A)
_LcsLMCRolloutRole_Type=DisplayString
_LcsLMCRolloutRole_Object=MibScalar
lcsLMCRolloutRole=_LcsLMCRolloutRole_Object((1,3,6,1,4,1,2356,100,2,1500,7),_LcsLMCRolloutRole_Type())
lcsLMCRolloutRole.setMaxAccess(_E)
if mibBuilder.loadTexts:lcsLMCRolloutRole.setStatus(_A)
_LcsLMCZeroTouchSupport_Type=Unsigned32
_LcsLMCZeroTouchSupport_Object=MibScalar
lcsLMCZeroTouchSupport=_LcsLMCZeroTouchSupport_Object((1,3,6,1,4,1,2356,100,2,1500,50),_LcsLMCZeroTouchSupport_Type())
lcsLMCZeroTouchSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsLMCZeroTouchSupport.setStatus(_A)
_LcsLMCPairingTokenPresent_Type=Unsigned32
_LcsLMCPairingTokenPresent_Object=MibScalar
lcsLMCPairingTokenPresent=_LcsLMCPairingTokenPresent_Object((1,3,6,1,4,1,2356,100,2,1500,51),_LcsLMCPairingTokenPresent_Type())
lcsLMCPairingTokenPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsLMCPairingTokenPresent.setStatus(_A)
_LcsLMCManagementStatus_Type=LMCStatus
_LcsLMCManagementStatus_Object=MibScalar
lcsLMCManagementStatus=_LcsLMCManagementStatus_Object((1,3,6,1,4,1,2356,100,2,1500,53),_LcsLMCManagementStatus_Type())
lcsLMCManagementStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsLMCManagementStatus.setStatus(_A)
_LcsLMCControlStatus_Type=LMCStatus
_LcsLMCControlStatus_Object=MibScalar
lcsLMCControlStatus=_LcsLMCControlStatus_Object((1,3,6,1,4,1,2356,100,2,1500,54),_LcsLMCControlStatus_Type())
lcsLMCControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsLMCControlStatus.setStatus(_A)
_LcsLMCMonitoringStatus_Type=LMCStatus
_LcsLMCMonitoringStatus_Object=MibScalar
lcsLMCMonitoringStatus=_LcsLMCMonitoringStatus_Object((1,3,6,1,4,1,2356,100,2,1500,55),_LcsLMCMonitoringStatus_Type())
lcsLMCMonitoringStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsLMCMonitoringStatus.setStatus(_A)
_LcsLMCConfigModified_Type=Unsigned32
_LcsLMCConfigModified_Object=MibScalar
lcsLMCConfigModified=_LcsLMCConfigModified_Object((1,3,6,1,4,1,2356,100,2,1500,57),_LcsLMCConfigModified_Type())
lcsLMCConfigModified.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsLMCConfigModified.setStatus(_A)
_LcsLMCDeviceID_Type=DisplayString
_LcsLMCDeviceID_Object=MibScalar
lcsLMCDeviceID=_LcsLMCDeviceID_Object((1,3,6,1,4,1,2356,100,2,1500,58),_LcsLMCDeviceID_Type())
lcsLMCDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsLMCDeviceID.setStatus(_A)
_LcsLMCStackingStatus_Type=Unsigned32
_LcsLMCStackingStatus_Object=MibScalar
lcsLMCStackingStatus=_LcsLMCStackingStatus_Object((1,3,6,1,4,1,2356,100,2,1500,59),_LcsLMCStackingStatus_Type())
lcsLMCStackingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsLMCStackingStatus.setStatus(_A)
_LcsLMCStatusRTT_Type=Unsigned32
_LcsLMCStatusRTT_Object=MibScalar
lcsLMCStatusRTT=_LcsLMCStatusRTT_Object((1,3,6,1,4,1,2356,100,2,1500,100),_LcsLMCStatusRTT_Type())
lcsLMCStatusRTT.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsLMCStatusRTT.setStatus(_A)
_LcsLMCTransportStatusTable_Object=MibTable
lcsLMCTransportStatusTable=_LcsLMCTransportStatusTable_Object((1,3,6,1,4,1,2356,100,2,1500,101))
if mibBuilder.loadTexts:lcsLMCTransportStatusTable.setStatus(_A)
_LcsLMCTransportStatusTableEntry_Object=MibTableRow
lcsLMCTransportStatusTableEntry=_LcsLMCTransportStatusTableEntry_Object((1,3,6,1,4,1,2356,100,2,1500,101,1))
lcsLMCTransportStatusTableEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:lcsLMCTransportStatusTableEntry.setStatus(_A)
class _LcsLMCTransportStatusTransportNumberIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_LcsLMCTransportStatusTransportNumberIndex_Type.__name__=_F
_LcsLMCTransportStatusTransportNumberIndex_Object=MibTableColumn
lcsLMCTransportStatusTransportNumberIndex=_LcsLMCTransportStatusTransportNumberIndex_Object((1,3,6,1,4,1,2356,100,2,1500,101,1,1),_LcsLMCTransportStatusTransportNumberIndex_Type())
lcsLMCTransportStatusTransportNumberIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:lcsLMCTransportStatusTransportNumberIndex.setStatus(_A)
_LcsLMCTransportStatusServiceName_Type=DisplayString
_LcsLMCTransportStatusServiceName_Object=MibTableColumn
lcsLMCTransportStatusServiceName=_LcsLMCTransportStatusServiceName_Object((1,3,6,1,4,1,2356,100,2,1500,101,1,2),_LcsLMCTransportStatusServiceName_Type())
lcsLMCTransportStatusServiceName.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsLMCTransportStatusServiceName.setStatus(_A)
_LcsLMCTransportStatusHttpRequests_Type=Counter64
_LcsLMCTransportStatusHttpRequests_Object=MibTableColumn
lcsLMCTransportStatusHttpRequests=_LcsLMCTransportStatusHttpRequests_Object((1,3,6,1,4,1,2356,100,2,1500,101,1,3),_LcsLMCTransportStatusHttpRequests_Type())
lcsLMCTransportStatusHttpRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsLMCTransportStatusHttpRequests.setStatus(_A)
_LcsLMCTransportStatusHttpRequestsErrors_Type=Counter64
_LcsLMCTransportStatusHttpRequestsErrors_Object=MibTableColumn
lcsLMCTransportStatusHttpRequestsErrors=_LcsLMCTransportStatusHttpRequestsErrors_Object((1,3,6,1,4,1,2356,100,2,1500,101,1,4),_LcsLMCTransportStatusHttpRequestsErrors_Type())
lcsLMCTransportStatusHttpRequestsErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsLMCTransportStatusHttpRequestsErrors.setStatus(_A)
_LcsLMCTransportStatusTXBytes_Type=Counter64
_LcsLMCTransportStatusTXBytes_Object=MibTableColumn
lcsLMCTransportStatusTXBytes=_LcsLMCTransportStatusTXBytes_Object((1,3,6,1,4,1,2356,100,2,1500,101,1,5),_LcsLMCTransportStatusTXBytes_Type())
lcsLMCTransportStatusTXBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsLMCTransportStatusTXBytes.setStatus(_A)
_LcsLMCTransportStatusRXBytes_Type=Counter64
_LcsLMCTransportStatusRXBytes_Object=MibTableColumn
lcsLMCTransportStatusRXBytes=_LcsLMCTransportStatusRXBytes_Object((1,3,6,1,4,1,2356,100,2,1500,101,1,7),_LcsLMCTransportStatusRXBytes_Type())
lcsLMCTransportStatusRXBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:lcsLMCTransportStatusRXBytes.setStatus(_A)
lcsTrapsTemperatureStateChange=NotificationType((1,3,6,1,4,1,2356,100,0,1,100))
lcsTrapsTemperatureStateChange.setObjects(*((_C,_H),(_C,_S),(_C,_T)))
if mibBuilder.loadTexts:lcsTrapsTemperatureStateChange.setStatus(_A)
lcsTrapsFanStateChange=NotificationType((1,3,6,1,4,1,2356,100,0,1,101))
lcsTrapsFanStateChange.setObjects(*((_C,_I),(_C,_K)))
if mibBuilder.loadTexts:lcsTrapsFanStateChange.setStatus(_A)
lcsTrapsPSUStateChange=NotificationType((1,3,6,1,4,1,2356,100,0,1,102))
lcsTrapsPSUStateChange.setObjects(*((_C,_J),(_C,_K)))
if mibBuilder.loadTexts:lcsTrapsPSUStateChange.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'MonitoringSensorType':MonitoringSensorType,'MonitoringModuleStatus':MonitoringModuleStatus,'MonitoringTempSensorStatus':MonitoringTempSensorStatus,'LMCStatus':LMCStatus,'lcosSXGeneral':lcosSXGeneral,'lcsNotificationGrp':lcsNotificationGrp,'lcsTraps':lcsTraps,'lcsTrapsTemperatureStateChange':lcsTrapsTemperatureStateChange,'lcsTrapsFanStateChange':lcsTrapsFanStateChange,'lcsTrapsPSUStateChange':lcsTrapsPSUStateChange,'lcsNotificationVars':lcsNotificationVars,_K:lcsNotificationStateChangeEvent,_S:lcsNotificationTemperatureStatusCurrent,_T:lcsNotificationTemperatureStatusPrevious,'lcsStatus':lcsStatus,'lcsMonitoring':lcsMonitoring,'lcsMonitoringTempSensorsTable':lcsMonitoringTempSensorsTable,'lcsMonitoringTempSensorsTableEntry':lcsMonitoringTempSensorsTableEntry,_N:lcsMonitoringTempSensorUnitIndex,_O:lcsMonitoringTempSensorIndex,'lcsMonitoringTempSensorDescription':lcsMonitoringTempSensorDescription,'lcsMonitoringTempSensorType':lcsMonitoringTempSensorType,'lcsMonitoringTempSensorState':lcsMonitoringTempSensorState,'lcsMonitoringTempSensorTemperature':lcsMonitoringTempSensorTemperature,'lcsMonitoringTempUnitTable':lcsMonitoringTempUnitTable,'lcsMonitoringTempUnitEntry':lcsMonitoringTempUnitEntry,_H:lcsMonitoringTempUnitIndex,'lcsMonitoringTempUnitState':lcsMonitoringTempUnitState,'lcsMonitoringTempUnitTemperature':lcsMonitoringTempUnitTemperature,'lcsMonitoringFansTable':lcsMonitoringFansTable,'lcsMonitoringFansTableEntry':lcsMonitoringFansTableEntry,_P:lcsMonitoringFanUnitIndex,_I:lcsMonitoringFanIndex,'lcsMonitoringFanDescription':lcsMonitoringFanDescription,'lcsMonitoringFanType':lcsMonitoringFanType,'lcsMonitoringFanState':lcsMonitoringFanState,'lcsMonitoringFanSpeed':lcsMonitoringFanSpeed,'lcsMonitoringPSUTable':lcsMonitoringPSUTable,'lcsMonitoringPSUTableEntry':lcsMonitoringPSUTableEntry,_Q:lcsMonitoringPSUUnitIndex,_J:lcsMonitoringPSUIndex,'lcsMonitoringPSUDescription':lcsMonitoringPSUDescription,'lcsMonitoringPSUType':lcsMonitoringPSUType,'lcsMonitoringPSUState':lcsMonitoringPSUState,'lcsConfiguration':lcsConfiguration,'lcsLMC':lcsLMC,'lcsLMCOperating':lcsLMCOperating,'lcsLMCConfigViaDHCP':lcsLMCConfigViaDHCP,'lcsLMCDomain':lcsLMCDomain,'lcsLMCAutoRenew':lcsLMCAutoRenew,'lcsLMCRolloutProjectID':lcsLMCRolloutProjectID,'lcsLMCRolloutLocationID':lcsLMCRolloutLocationID,'lcsLMCRolloutRole':lcsLMCRolloutRole,'lcsLMCZeroTouchSupport':lcsLMCZeroTouchSupport,'lcsLMCPairingTokenPresent':lcsLMCPairingTokenPresent,'lcsLMCManagementStatus':lcsLMCManagementStatus,'lcsLMCControlStatus':lcsLMCControlStatus,'lcsLMCMonitoringStatus':lcsLMCMonitoringStatus,'lcsLMCConfigModified':lcsLMCConfigModified,'lcsLMCDeviceID':lcsLMCDeviceID,'lcsLMCStackingStatus':lcsLMCStackingStatus,'lcsLMCStatusRTT':lcsLMCStatusRTT,'lcsLMCTransportStatusTable':lcsLMCTransportStatusTable,'lcsLMCTransportStatusTableEntry':lcsLMCTransportStatusTableEntry,_R:lcsLMCTransportStatusTransportNumberIndex,'lcsLMCTransportStatusServiceName':lcsLMCTransportStatusServiceName,'lcsLMCTransportStatusHttpRequests':lcsLMCTransportStatusHttpRequests,'lcsLMCTransportStatusHttpRequestsErrors':lcsLMCTransportStatusHttpRequestsErrors,'lcsLMCTransportStatusTXBytes':lcsLMCTransportStatusTXBytes,'lcsLMCTransportStatusRXBytes':lcsLMCTransportStatusRXBytes})