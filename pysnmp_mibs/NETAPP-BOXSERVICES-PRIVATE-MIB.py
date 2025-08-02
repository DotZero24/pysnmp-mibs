_j='boxsTemperatureStatusPreviousEvent'
_i='boxsTemperatureStatusCurrentEvent'
_h='boxServicesThermalShutdownTemperature'
_g='boxServicesThermalShutdownSensor'
_f='boxsTemperatureChangeEvent'
_e='not-accessible'
_d='boxsPwrUsageHistoryUnitSampleIndex'
_c='boxsPwrUsageHistoryUnitIndex'
_b='obsolete'
_a='incompatible'
_Z='notpowering'
_Y='powering'
_X='nopower'
_W='failed'
_V='operational'
_U='DisplayString'
_T='boxsItemStateChangeEvent'
_S='boxServicesTempUnitIndex'
_R='boxServicesTempSensorIndex'
_Q='boxServicesPowSupplyIndex'
_P='removableAC'
_O='fixedDC'
_N='removableDC'
_M='fixedAC'
_L='removable'
_K='fixed'
_J='boxServicesFansIndex'
_I='notpresent'
_H='disable'
_G='enable'
_F='accessible-for-notify'
_E='read-write'
_D='NETAPP-BOXSERVICES-PRIVATE-MIB'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fastPath,=mibBuilder.importSymbols('NETAPP-REF-MIB','fastPath')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_U,'PhysAddress','TextualConvention')
fastPathBoxServices=ModuleIdentity((1,3,6,1,4,1,789,4413,1,1,43))
if mibBuilder.loadTexts:fastPathBoxServices.setRevisions(('2011-01-26 00:00','2008-02-22 00:00'))
class BoxsTemperatureStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('low',0),('normal',1),('warning',2),('critical',3),('shutdown',4),(_I,5),('notoperational',6)))
_FastPathBoxServicesTraps_ObjectIdentity=ObjectIdentity
fastPathBoxServicesTraps=_FastPathBoxServicesTraps_ObjectIdentity((1,3,6,1,4,1,789,4413,1,1,43,0))
_BoxServicesGroup_ObjectIdentity=ObjectIdentity
boxServicesGroup=_BoxServicesGroup_ObjectIdentity((1,3,6,1,4,1,789,4413,1,1,43,1))
class _BoxServicesNormalTempRangeMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_BoxServicesNormalTempRangeMin_Type.__name__=_B
_BoxServicesNormalTempRangeMin_Object=MibScalar
boxServicesNormalTempRangeMin=_BoxServicesNormalTempRangeMin_Object((1,3,6,1,4,1,789,4413,1,1,43,1,1),_BoxServicesNormalTempRangeMin_Type())
boxServicesNormalTempRangeMin.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesNormalTempRangeMin.setStatus(_A)
class _BoxServicesNormalTempRangeMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_BoxServicesNormalTempRangeMax_Type.__name__=_B
_BoxServicesNormalTempRangeMax_Object=MibScalar
boxServicesNormalTempRangeMax=_BoxServicesNormalTempRangeMax_Object((1,3,6,1,4,1,789,4413,1,1,43,1,2),_BoxServicesNormalTempRangeMax_Type())
boxServicesNormalTempRangeMax.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesNormalTempRangeMax.setStatus(_A)
class _BoxServicesTemperatureTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_BoxServicesTemperatureTrapEnable_Type.__name__=_B
_BoxServicesTemperatureTrapEnable_Object=MibScalar
boxServicesTemperatureTrapEnable=_BoxServicesTemperatureTrapEnable_Object((1,3,6,1,4,1,789,4413,1,1,43,1,3),_BoxServicesTemperatureTrapEnable_Type())
boxServicesTemperatureTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:boxServicesTemperatureTrapEnable.setStatus(_A)
class _BoxServicesPSMStateTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_BoxServicesPSMStateTrapEnable_Type.__name__=_B
_BoxServicesPSMStateTrapEnable_Object=MibScalar
boxServicesPSMStateTrapEnable=_BoxServicesPSMStateTrapEnable_Object((1,3,6,1,4,1,789,4413,1,1,43,1,4),_BoxServicesPSMStateTrapEnable_Type())
boxServicesPSMStateTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:boxServicesPSMStateTrapEnable.setStatus(_A)
class _BoxServicesFanStateTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_BoxServicesFanStateTrapEnable_Type.__name__=_B
_BoxServicesFanStateTrapEnable_Object=MibScalar
boxServicesFanStateTrapEnable=_BoxServicesFanStateTrapEnable_Object((1,3,6,1,4,1,789,4413,1,1,43,1,5),_BoxServicesFanStateTrapEnable_Type())
boxServicesFanStateTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:boxServicesFanStateTrapEnable.setStatus(_A)
_BoxServicesFansTable_Object=MibTable
boxServicesFansTable=_BoxServicesFansTable_Object((1,3,6,1,4,1,789,4413,1,1,43,1,6))
if mibBuilder.loadTexts:boxServicesFansTable.setStatus(_A)
_BoxServicesFansEntry_Object=MibTableRow
boxServicesFansEntry=_BoxServicesFansEntry_Object((1,3,6,1,4,1,789,4413,1,1,43,1,6,1))
boxServicesFansEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:boxServicesFansEntry.setStatus(_A)
class _BoxServicesFansIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BoxServicesFansIndex_Type.__name__=_B
_BoxServicesFansIndex_Object=MibTableColumn
boxServicesFansIndex=_BoxServicesFansIndex_Object((1,3,6,1,4,1,789,4413,1,1,43,1,6,1,1),_BoxServicesFansIndex_Type())
boxServicesFansIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesFansIndex.setStatus(_A)
class _BoxServicesFanItemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6)))
_BoxServicesFanItemType_Type.__name__=_B
_BoxServicesFanItemType_Object=MibTableColumn
boxServicesFanItemType=_BoxServicesFanItemType_Object((1,3,6,1,4,1,789,4413,1,1,43,1,6,1,2),_BoxServicesFanItemType_Type())
boxServicesFanItemType.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesFanItemType.setStatus(_A)
class _BoxServicesFanItemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,1),(_V,2),(_W,3),(_X,4),(_Y,5),(_Z,6),(_a,7)))
_BoxServicesFanItemState_Type.__name__=_B
_BoxServicesFanItemState_Object=MibTableColumn
boxServicesFanItemState=_BoxServicesFanItemState_Object((1,3,6,1,4,1,789,4413,1,1,43,1,6,1,3),_BoxServicesFanItemState_Type())
boxServicesFanItemState.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesFanItemState.setStatus(_A)
_BoxServicesFanSpeed_Type=Integer32
_BoxServicesFanSpeed_Object=MibTableColumn
boxServicesFanSpeed=_BoxServicesFanSpeed_Object((1,3,6,1,4,1,789,4413,1,1,43,1,6,1,4),_BoxServicesFanSpeed_Type())
boxServicesFanSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesFanSpeed.setStatus(_A)
_BoxServicesFanDutyLevel_Type=Integer32
_BoxServicesFanDutyLevel_Object=MibTableColumn
boxServicesFanDutyLevel=_BoxServicesFanDutyLevel_Object((1,3,6,1,4,1,789,4413,1,1,43,1,6,1,5),_BoxServicesFanDutyLevel_Type())
boxServicesFanDutyLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesFanDutyLevel.setStatus(_A)
_BoxServicesPowSuppliesTable_Object=MibTable
boxServicesPowSuppliesTable=_BoxServicesPowSuppliesTable_Object((1,3,6,1,4,1,789,4413,1,1,43,1,7))
if mibBuilder.loadTexts:boxServicesPowSuppliesTable.setStatus(_A)
_BoxServicesPowSuppliesEntry_Object=MibTableRow
boxServicesPowSuppliesEntry=_BoxServicesPowSuppliesEntry_Object((1,3,6,1,4,1,789,4413,1,1,43,1,7,1))
boxServicesPowSuppliesEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:boxServicesPowSuppliesEntry.setStatus(_A)
class _BoxServicesPowSupplyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BoxServicesPowSupplyIndex_Type.__name__=_B
_BoxServicesPowSupplyIndex_Object=MibTableColumn
boxServicesPowSupplyIndex=_BoxServicesPowSupplyIndex_Object((1,3,6,1,4,1,789,4413,1,1,43,1,7,1,1),_BoxServicesPowSupplyIndex_Type())
boxServicesPowSupplyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesPowSupplyIndex.setStatus(_A)
class _BoxServicesPowSupplyItemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6)))
_BoxServicesPowSupplyItemType_Type.__name__=_B
_BoxServicesPowSupplyItemType_Object=MibTableColumn
boxServicesPowSupplyItemType=_BoxServicesPowSupplyItemType_Object((1,3,6,1,4,1,789,4413,1,1,43,1,7,1,2),_BoxServicesPowSupplyItemType_Type())
boxServicesPowSupplyItemType.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesPowSupplyItemType.setStatus(_A)
class _BoxServicesPowSupplyItemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,1),(_V,2),(_W,3),(_X,4),(_Y,5),(_Z,6),(_a,7)))
_BoxServicesPowSupplyItemState_Type.__name__=_B
_BoxServicesPowSupplyItemState_Object=MibTableColumn
boxServicesPowSupplyItemState=_BoxServicesPowSupplyItemState_Object((1,3,6,1,4,1,789,4413,1,1,43,1,7,1,3),_BoxServicesPowSupplyItemState_Type())
boxServicesPowSupplyItemState.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesPowSupplyItemState.setStatus(_A)
_BoxServicesTempSensorsTable_Object=MibTable
boxServicesTempSensorsTable=_BoxServicesTempSensorsTable_Object((1,3,6,1,4,1,789,4413,1,1,43,1,8))
if mibBuilder.loadTexts:boxServicesTempSensorsTable.setStatus(_A)
_BoxServicesTempSensorsEntry_Object=MibTableRow
boxServicesTempSensorsEntry=_BoxServicesTempSensorsEntry_Object((1,3,6,1,4,1,789,4413,1,1,43,1,8,1))
boxServicesTempSensorsEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:boxServicesTempSensorsEntry.setStatus(_A)
class _BoxServicesTempSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BoxServicesTempSensorIndex_Type.__name__=_B
_BoxServicesTempSensorIndex_Object=MibTableColumn
boxServicesTempSensorIndex=_BoxServicesTempSensorIndex_Object((1,3,6,1,4,1,789,4413,1,1,43,1,8,1,1),_BoxServicesTempSensorIndex_Type())
boxServicesTempSensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesTempSensorIndex.setStatus(_A)
class _BoxServicesTempSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4),(_O,5),(_P,6)))
_BoxServicesTempSensorType_Type.__name__=_B
_BoxServicesTempSensorType_Object=MibTableColumn
boxServicesTempSensorType=_BoxServicesTempSensorType_Object((1,3,6,1,4,1,789,4413,1,1,43,1,8,1,2),_BoxServicesTempSensorType_Type())
boxServicesTempSensorType.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesTempSensorType.setStatus(_A)
_BoxServicesTempSensorState_Type=BoxsTemperatureStatus
_BoxServicesTempSensorState_Object=MibTableColumn
boxServicesTempSensorState=_BoxServicesTempSensorState_Object((1,3,6,1,4,1,789,4413,1,1,43,1,8,1,3),_BoxServicesTempSensorState_Type())
boxServicesTempSensorState.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesTempSensorState.setStatus(_b)
_BoxServicesTempSensorTemperature_Type=Integer32
_BoxServicesTempSensorTemperature_Object=MibTableColumn
boxServicesTempSensorTemperature=_BoxServicesTempSensorTemperature_Object((1,3,6,1,4,1,789,4413,1,1,43,1,8,1,4),_BoxServicesTempSensorTemperature_Type())
boxServicesTempSensorTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesTempSensorTemperature.setStatus(_A)
_BoxsUnitPwrUsageHistoryTable_Object=MibTable
boxsUnitPwrUsageHistoryTable=_BoxsUnitPwrUsageHistoryTable_Object((1,3,6,1,4,1,789,4413,1,1,43,1,9))
if mibBuilder.loadTexts:boxsUnitPwrUsageHistoryTable.setStatus(_A)
_BoxsUnitPwrUsageHistoryEntry_Object=MibTableRow
boxsUnitPwrUsageHistoryEntry=_BoxsUnitPwrUsageHistoryEntry_Object((1,3,6,1,4,1,789,4413,1,1,43,1,9,1))
boxsUnitPwrUsageHistoryEntry.setIndexNames((0,_D,_c),(0,_D,_d))
if mibBuilder.loadTexts:boxsUnitPwrUsageHistoryEntry.setStatus(_A)
class _BoxsPwrUsageHistoryUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_BoxsPwrUsageHistoryUnitIndex_Type.__name__=_B
_BoxsPwrUsageHistoryUnitIndex_Object=MibTableColumn
boxsPwrUsageHistoryUnitIndex=_BoxsPwrUsageHistoryUnitIndex_Object((1,3,6,1,4,1,789,4413,1,1,43,1,9,1,1),_BoxsPwrUsageHistoryUnitIndex_Type())
boxsPwrUsageHistoryUnitIndex.setMaxAccess(_e)
if mibBuilder.loadTexts:boxsPwrUsageHistoryUnitIndex.setStatus(_A)
class _BoxsPwrUsageHistoryUnitSampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BoxsPwrUsageHistoryUnitSampleIndex_Type.__name__=_B
_BoxsPwrUsageHistoryUnitSampleIndex_Object=MibTableColumn
boxsPwrUsageHistoryUnitSampleIndex=_BoxsPwrUsageHistoryUnitSampleIndex_Object((1,3,6,1,4,1,789,4413,1,1,43,1,9,1,2),_BoxsPwrUsageHistoryUnitSampleIndex_Type())
boxsPwrUsageHistoryUnitSampleIndex.setMaxAccess(_e)
if mibBuilder.loadTexts:boxsPwrUsageHistoryUnitSampleIndex.setStatus(_A)
class _BoxsPwrUsageHistoryUnitSampleTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_BoxsPwrUsageHistoryUnitSampleTime_Type.__name__=_U
_BoxsPwrUsageHistoryUnitSampleTime_Object=MibTableColumn
boxsPwrUsageHistoryUnitSampleTime=_BoxsPwrUsageHistoryUnitSampleTime_Object((1,3,6,1,4,1,789,4413,1,1,43,1,9,1,3),_BoxsPwrUsageHistoryUnitSampleTime_Type())
boxsPwrUsageHistoryUnitSampleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:boxsPwrUsageHistoryUnitSampleTime.setStatus(_A)
_BoxsPwrUsageHistoryUnitPowerConsumption_Type=Integer32
_BoxsPwrUsageHistoryUnitPowerConsumption_Object=MibTableColumn
boxsPwrUsageHistoryUnitPowerConsumption=_BoxsPwrUsageHistoryUnitPowerConsumption_Object((1,3,6,1,4,1,789,4413,1,1,43,1,9,1,4),_BoxsPwrUsageHistoryUnitPowerConsumption_Type())
boxsPwrUsageHistoryUnitPowerConsumption.setMaxAccess(_C)
if mibBuilder.loadTexts:boxsPwrUsageHistoryUnitPowerConsumption.setStatus(_A)
_BoxsPwrUsageHistoryStackPowerConsumption_Type=Integer32
_BoxsPwrUsageHistoryStackPowerConsumption_Object=MibTableColumn
boxsPwrUsageHistoryStackPowerConsumption=_BoxsPwrUsageHistoryStackPowerConsumption_Object((1,3,6,1,4,1,789,4413,1,1,43,1,9,1,5),_BoxsPwrUsageHistoryStackPowerConsumption_Type())
boxsPwrUsageHistoryStackPowerConsumption.setMaxAccess(_C)
if mibBuilder.loadTexts:boxsPwrUsageHistoryStackPowerConsumption.setStatus(_A)
class _BoxsPwrUsageHistoryUnitSampleInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,86400))
_BoxsPwrUsageHistoryUnitSampleInterval_Type.__name__=_B
_BoxsPwrUsageHistoryUnitSampleInterval_Object=MibScalar
boxsPwrUsageHistoryUnitSampleInterval=_BoxsPwrUsageHistoryUnitSampleInterval_Object((1,3,6,1,4,1,789,4413,1,1,43,1,10),_BoxsPwrUsageHistoryUnitSampleInterval_Type())
boxsPwrUsageHistoryUnitSampleInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:boxsPwrUsageHistoryUnitSampleInterval.setStatus(_A)
class _BoxsPwrUsageHistoryUnitMaxSamples_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,168))
_BoxsPwrUsageHistoryUnitMaxSamples_Type.__name__=_B
_BoxsPwrUsageHistoryUnitMaxSamples_Object=MibScalar
boxsPwrUsageHistoryUnitMaxSamples=_BoxsPwrUsageHistoryUnitMaxSamples_Object((1,3,6,1,4,1,789,4413,1,1,43,1,11),_BoxsPwrUsageHistoryUnitMaxSamples_Type())
boxsPwrUsageHistoryUnitMaxSamples.setMaxAccess(_E)
if mibBuilder.loadTexts:boxsPwrUsageHistoryUnitMaxSamples.setStatus(_A)
_BoxServicesThermalShutdownSensor_Type=Unsigned32
_BoxServicesThermalShutdownSensor_Object=MibScalar
boxServicesThermalShutdownSensor=_BoxServicesThermalShutdownSensor_Object((1,3,6,1,4,1,789,4413,1,1,43,1,13),_BoxServicesThermalShutdownSensor_Type())
boxServicesThermalShutdownSensor.setMaxAccess(_F)
if mibBuilder.loadTexts:boxServicesThermalShutdownSensor.setStatus(_A)
_BoxServicesThermalShutdownTemperature_Type=Unsigned32
_BoxServicesThermalShutdownTemperature_Object=MibScalar
boxServicesThermalShutdownTemperature=_BoxServicesThermalShutdownTemperature_Object((1,3,6,1,4,1,789,4413,1,1,43,1,14),_BoxServicesThermalShutdownTemperature_Type())
boxServicesThermalShutdownTemperature.setMaxAccess(_F)
if mibBuilder.loadTexts:boxServicesThermalShutdownTemperature.setStatus(_A)
_BoxServicesTempUnitTable_Object=MibTable
boxServicesTempUnitTable=_BoxServicesTempUnitTable_Object((1,3,6,1,4,1,789,4413,1,1,43,1,15))
if mibBuilder.loadTexts:boxServicesTempUnitTable.setStatus(_A)
_BoxServicesTempUnitEntry_Object=MibTableRow
boxServicesTempUnitEntry=_BoxServicesTempUnitEntry_Object((1,3,6,1,4,1,789,4413,1,1,43,1,15,1))
boxServicesTempUnitEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:boxServicesTempUnitEntry.setStatus(_A)
_BoxServicesTempUnitIndex_Type=Unsigned32
_BoxServicesTempUnitIndex_Object=MibTableColumn
boxServicesTempUnitIndex=_BoxServicesTempUnitIndex_Object((1,3,6,1,4,1,789,4413,1,1,43,1,15,1,1),_BoxServicesTempUnitIndex_Type())
boxServicesTempUnitIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesTempUnitIndex.setStatus(_A)
_BoxServicesTempUnitState_Type=BoxsTemperatureStatus
_BoxServicesTempUnitState_Object=MibTableColumn
boxServicesTempUnitState=_BoxServicesTempUnitState_Object((1,3,6,1,4,1,789,4413,1,1,43,1,15,1,2),_BoxServicesTempUnitState_Type())
boxServicesTempUnitState.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesTempUnitState.setStatus(_A)
_BoxServicesTempUnitTemperature_Type=Integer32
_BoxServicesTempUnitTemperature_Object=MibTableColumn
boxServicesTempUnitTemperature=_BoxServicesTempUnitTemperature_Object((1,3,6,1,4,1,789,4413,1,1,43,1,15,1,3),_BoxServicesTempUnitTemperature_Type())
boxServicesTempUnitTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:boxServicesTempUnitTemperature.setStatus(_A)
_BoxServicesNotificationsGroup_ObjectIdentity=ObjectIdentity
boxServicesNotificationsGroup=_BoxServicesNotificationsGroup_ObjectIdentity((1,3,6,1,4,1,789,4413,1,1,43,2))
class _BoxsItemStateChangeEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('insertion',1),('removal',2),('becomeoperational',3),('failure',4),('losepower',5)))
_BoxsItemStateChangeEvent_Type.__name__=_B
_BoxsItemStateChangeEvent_Object=MibScalar
boxsItemStateChangeEvent=_BoxsItemStateChangeEvent_Object((1,3,6,1,4,1,789,4413,1,1,43,2,1),_BoxsItemStateChangeEvent_Type())
boxsItemStateChangeEvent.setMaxAccess(_F)
if mibBuilder.loadTexts:boxsItemStateChangeEvent.setStatus(_A)
class _BoxsTemperatureChangeEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('abovethreshold',1),('belowthreshold',2),('withinnormalrange',3)))
_BoxsTemperatureChangeEvent_Type.__name__=_B
_BoxsTemperatureChangeEvent_Object=MibScalar
boxsTemperatureChangeEvent=_BoxsTemperatureChangeEvent_Object((1,3,6,1,4,1,789,4413,1,1,43,2,2),_BoxsTemperatureChangeEvent_Type())
boxsTemperatureChangeEvent.setMaxAccess(_F)
if mibBuilder.loadTexts:boxsTemperatureChangeEvent.setStatus(_A)
_BoxsTemperatureStatusCurrentEvent_Type=BoxsTemperatureStatus
_BoxsTemperatureStatusCurrentEvent_Object=MibScalar
boxsTemperatureStatusCurrentEvent=_BoxsTemperatureStatusCurrentEvent_Object((1,3,6,1,4,1,789,4413,1,1,43,2,3),_BoxsTemperatureStatusCurrentEvent_Type())
boxsTemperatureStatusCurrentEvent.setMaxAccess(_F)
if mibBuilder.loadTexts:boxsTemperatureStatusCurrentEvent.setStatus(_A)
_BoxsTemperatureStatusPreviousEvent_Type=BoxsTemperatureStatus
_BoxsTemperatureStatusPreviousEvent_Object=MibScalar
boxsTemperatureStatusPreviousEvent=_BoxsTemperatureStatusPreviousEvent_Object((1,3,6,1,4,1,789,4413,1,1,43,2,4),_BoxsTemperatureStatusPreviousEvent_Type())
boxsTemperatureStatusPreviousEvent.setMaxAccess(_F)
if mibBuilder.loadTexts:boxsTemperatureStatusPreviousEvent.setStatus(_A)
_BoxsLocatorLedConfigGroup_ObjectIdentity=ObjectIdentity
boxsLocatorLedConfigGroup=_BoxsLocatorLedConfigGroup_ObjectIdentity((1,3,6,1,4,1,789,4413,1,1,43,4))
_BoxsLocatorLedUnit_Type=Integer32
_BoxsLocatorLedUnit_Object=MibScalar
boxsLocatorLedUnit=_BoxsLocatorLedUnit_Object((1,3,6,1,4,1,789,4413,1,1,43,4,1),_BoxsLocatorLedUnit_Type())
boxsLocatorLedUnit.setMaxAccess(_E)
if mibBuilder.loadTexts:boxsLocatorLedUnit.setStatus(_A)
class _BoxsLocatorLedTime_Type(Integer32):defaultValue=20
_BoxsLocatorLedTime_Type.__name__=_B
_BoxsLocatorLedTime_Object=MibScalar
boxsLocatorLedTime=_BoxsLocatorLedTime_Object((1,3,6,1,4,1,789,4413,1,1,43,4,2),_BoxsLocatorLedTime_Type())
boxsLocatorLedTime.setMaxAccess(_E)
if mibBuilder.loadTexts:boxsLocatorLedTime.setStatus(_A)
class _BoxsLocatorLedEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_G,1)))
_BoxsLocatorLedEnable_Type.__name__=_B
_BoxsLocatorLedEnable_Object=MibScalar
boxsLocatorLedEnable=_BoxsLocatorLedEnable_Object((1,3,6,1,4,1,789,4413,1,1,43,4,3),_BoxsLocatorLedEnable_Type())
boxsLocatorLedEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:boxsLocatorLedEnable.setStatus(_A)
boxsFanStateChange=NotificationType((1,3,6,1,4,1,789,4413,1,1,43,0,1))
boxsFanStateChange.setObjects(*((_D,_J),(_D,_T)))
if mibBuilder.loadTexts:boxsFanStateChange.setStatus(_A)
boxsPowSupplyStateChange=NotificationType((1,3,6,1,4,1,789,4413,1,1,43,0,2))
boxsPowSupplyStateChange.setObjects(*((_D,_Q),(_D,_T)))
if mibBuilder.loadTexts:boxsPowSupplyStateChange.setStatus(_A)
boxsTemperatureChange=NotificationType((1,3,6,1,4,1,789,4413,1,1,43,0,3))
boxsTemperatureChange.setObjects(*((_D,_R),(_D,_f)))
if mibBuilder.loadTexts:boxsTemperatureChange.setStatus(_b)
boxsThermalShutdown=NotificationType((1,3,6,1,4,1,789,4413,1,1,43,0,4))
boxsThermalShutdown.setObjects(*((_D,_g),(_D,_h)))
if mibBuilder.loadTexts:boxsThermalShutdown.setStatus(_A)
boxsTemperatureStateChange=NotificationType((1,3,6,1,4,1,789,4413,1,1,43,0,5))
boxsTemperatureStateChange.setObjects(*((_D,_S),(_D,_i),(_D,_j)))
if mibBuilder.loadTexts:boxsTemperatureStateChange.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'BoxsTemperatureStatus':BoxsTemperatureStatus,'fastPathBoxServices':fastPathBoxServices,'fastPathBoxServicesTraps':fastPathBoxServicesTraps,'boxsFanStateChange':boxsFanStateChange,'boxsPowSupplyStateChange':boxsPowSupplyStateChange,'boxsTemperatureChange':boxsTemperatureChange,'boxsThermalShutdown':boxsThermalShutdown,'boxsTemperatureStateChange':boxsTemperatureStateChange,'boxServicesGroup':boxServicesGroup,'boxServicesNormalTempRangeMin':boxServicesNormalTempRangeMin,'boxServicesNormalTempRangeMax':boxServicesNormalTempRangeMax,'boxServicesTemperatureTrapEnable':boxServicesTemperatureTrapEnable,'boxServicesPSMStateTrapEnable':boxServicesPSMStateTrapEnable,'boxServicesFanStateTrapEnable':boxServicesFanStateTrapEnable,'boxServicesFansTable':boxServicesFansTable,'boxServicesFansEntry':boxServicesFansEntry,_J:boxServicesFansIndex,'boxServicesFanItemType':boxServicesFanItemType,'boxServicesFanItemState':boxServicesFanItemState,'boxServicesFanSpeed':boxServicesFanSpeed,'boxServicesFanDutyLevel':boxServicesFanDutyLevel,'boxServicesPowSuppliesTable':boxServicesPowSuppliesTable,'boxServicesPowSuppliesEntry':boxServicesPowSuppliesEntry,_Q:boxServicesPowSupplyIndex,'boxServicesPowSupplyItemType':boxServicesPowSupplyItemType,'boxServicesPowSupplyItemState':boxServicesPowSupplyItemState,'boxServicesTempSensorsTable':boxServicesTempSensorsTable,'boxServicesTempSensorsEntry':boxServicesTempSensorsEntry,_R:boxServicesTempSensorIndex,'boxServicesTempSensorType':boxServicesTempSensorType,'boxServicesTempSensorState':boxServicesTempSensorState,'boxServicesTempSensorTemperature':boxServicesTempSensorTemperature,'boxsUnitPwrUsageHistoryTable':boxsUnitPwrUsageHistoryTable,'boxsUnitPwrUsageHistoryEntry':boxsUnitPwrUsageHistoryEntry,_c:boxsPwrUsageHistoryUnitIndex,_d:boxsPwrUsageHistoryUnitSampleIndex,'boxsPwrUsageHistoryUnitSampleTime':boxsPwrUsageHistoryUnitSampleTime,'boxsPwrUsageHistoryUnitPowerConsumption':boxsPwrUsageHistoryUnitPowerConsumption,'boxsPwrUsageHistoryStackPowerConsumption':boxsPwrUsageHistoryStackPowerConsumption,'boxsPwrUsageHistoryUnitSampleInterval':boxsPwrUsageHistoryUnitSampleInterval,'boxsPwrUsageHistoryUnitMaxSamples':boxsPwrUsageHistoryUnitMaxSamples,_g:boxServicesThermalShutdownSensor,_h:boxServicesThermalShutdownTemperature,'boxServicesTempUnitTable':boxServicesTempUnitTable,'boxServicesTempUnitEntry':boxServicesTempUnitEntry,_S:boxServicesTempUnitIndex,'boxServicesTempUnitState':boxServicesTempUnitState,'boxServicesTempUnitTemperature':boxServicesTempUnitTemperature,'boxServicesNotificationsGroup':boxServicesNotificationsGroup,_T:boxsItemStateChangeEvent,_f:boxsTemperatureChangeEvent,_i:boxsTemperatureStatusCurrentEvent,_j:boxsTemperatureStatusPreviousEvent,'boxsLocatorLedConfigGroup':boxsLocatorLedConfigGroup,'boxsLocatorLedUnit':boxsLocatorLedUnit,'boxsLocatorLedTime':boxsLocatorLedTime,'boxsLocatorLedEnable':boxsLocatorLedEnable})