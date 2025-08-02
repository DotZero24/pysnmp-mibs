_k='boxsTemperatureStatusPreviousEvent'
_j='boxsTemperatureStatusCurrentEvent'
_i='boxServicesThermalShutdownTemperature'
_h='boxServicesThermalShutdownSensor'
_g='boxsTemperatureChangeEvent'
_f='boxServicesFiberPortIndex'
_e='obsolete'
_d='boxServicesUnitIndex'
_c='boxServicesPowerSuppUnitIndex'
_b='incompatible'
_a='notpowering'
_Z='nopower'
_Y='powering'
_X='failed'
_W='operational'
_V='boxServicesFanUnitIndex'
_U='boxsItemStateChangeEvent'
_T='boxServicesTempUnitIndex'
_S='boxServicesTempSensorIndex'
_R='boxServicesPowSupplyIndex'
_Q='removableAC'
_P='fixedDC'
_O='removableDC'
_N='fixedAC'
_M='removable'
_L='fixed'
_K='boxServicesFansIndex'
_J='notpresent'
_I='OctetString'
_H='disable'
_G='enable'
_F='accessible-for-notify'
_E='read-write'
_D='Integer32'
_C='NETGEAR-BOXSERVICES-PRIVATE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ng7000managedswitch,=mibBuilder.importSymbols('NETGEAR-REF-MIB','ng7000managedswitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fastPathBoxServices=ModuleIdentity((1,3,6,1,4,1,4526,10,43))
if mibBuilder.loadTexts:fastPathBoxServices.setRevisions(('2011-01-26 00:00','2008-02-22 00:00','2019-12-23 00:00'))
class BoxsTemperatureStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('low',0),('normal',1),('warning',2),('critical',3),('shutdown',4),(_J,5),('notoperational',6)))
_FastPathBoxServicesTraps_ObjectIdentity=ObjectIdentity
fastPathBoxServicesTraps=_FastPathBoxServicesTraps_ObjectIdentity((1,3,6,1,4,1,4526,10,43,0))
_BoxServicesGroup_ObjectIdentity=ObjectIdentity
boxServicesGroup=_BoxServicesGroup_ObjectIdentity((1,3,6,1,4,1,4526,10,43,1))
class _BoxServicesNormalTempRangeMin_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_BoxServicesNormalTempRangeMin_Type.__name__=_D
_BoxServicesNormalTempRangeMin_Object=MibScalar
boxServicesNormalTempRangeMin=_BoxServicesNormalTempRangeMin_Object((1,3,6,1,4,1,4526,10,43,1,1),_BoxServicesNormalTempRangeMin_Type())
boxServicesNormalTempRangeMin.setMaxAccess(_E)
if mibBuilder.loadTexts:boxServicesNormalTempRangeMin.setStatus(_A)
class _BoxServicesNormalTempRangeMax_Type(Integer32):defaultValue=45;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_BoxServicesNormalTempRangeMax_Type.__name__=_D
_BoxServicesNormalTempRangeMax_Object=MibScalar
boxServicesNormalTempRangeMax=_BoxServicesNormalTempRangeMax_Object((1,3,6,1,4,1,4526,10,43,1,2),_BoxServicesNormalTempRangeMax_Type())
boxServicesNormalTempRangeMax.setMaxAccess(_E)
if mibBuilder.loadTexts:boxServicesNormalTempRangeMax.setStatus(_A)
class _BoxServicesTemperatureTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_BoxServicesTemperatureTrapEnable_Type.__name__=_D
_BoxServicesTemperatureTrapEnable_Object=MibScalar
boxServicesTemperatureTrapEnable=_BoxServicesTemperatureTrapEnable_Object((1,3,6,1,4,1,4526,10,43,1,3),_BoxServicesTemperatureTrapEnable_Type())
boxServicesTemperatureTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:boxServicesTemperatureTrapEnable.setStatus(_A)
class _BoxServicesPSMStateTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_BoxServicesPSMStateTrapEnable_Type.__name__=_D
_BoxServicesPSMStateTrapEnable_Object=MibScalar
boxServicesPSMStateTrapEnable=_BoxServicesPSMStateTrapEnable_Object((1,3,6,1,4,1,4526,10,43,1,4),_BoxServicesPSMStateTrapEnable_Type())
boxServicesPSMStateTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:boxServicesPSMStateTrapEnable.setStatus(_A)
class _BoxServicesFanStateTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_BoxServicesFanStateTrapEnable_Type.__name__=_D
_BoxServicesFanStateTrapEnable_Object=MibScalar
boxServicesFanStateTrapEnable=_BoxServicesFanStateTrapEnable_Object((1,3,6,1,4,1,4526,10,43,1,5),_BoxServicesFanStateTrapEnable_Type())
boxServicesFanStateTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:boxServicesFanStateTrapEnable.setStatus(_A)
_BoxServicesFansTable_Object=MibTable
boxServicesFansTable=_BoxServicesFansTable_Object((1,3,6,1,4,1,4526,10,43,1,6))
if mibBuilder.loadTexts:boxServicesFansTable.setStatus(_A)
_BoxServicesFansEntry_Object=MibTableRow
boxServicesFansEntry=_BoxServicesFansEntry_Object((1,3,6,1,4,1,4526,10,43,1,6,1))
boxServicesFansEntry.setIndexNames((0,_C,_V),(0,_C,_K))
if mibBuilder.loadTexts:boxServicesFansEntry.setStatus(_A)
class _BoxServicesFansIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BoxServicesFansIndex_Type.__name__=_D
_BoxServicesFansIndex_Object=MibTableColumn
boxServicesFansIndex=_BoxServicesFansIndex_Object((1,3,6,1,4,1,4526,10,43,1,6,1,1),_BoxServicesFansIndex_Type())
boxServicesFansIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesFansIndex.setStatus(_A)
class _BoxServicesFanItemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6)))
_BoxServicesFanItemType_Type.__name__=_D
_BoxServicesFanItemType_Object=MibTableColumn
boxServicesFanItemType=_BoxServicesFanItemType_Object((1,3,6,1,4,1,4526,10,43,1,6,1,2),_BoxServicesFanItemType_Type())
boxServicesFanItemType.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesFanItemType.setStatus(_A)
class _BoxServicesFanItemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_J,1),(_W,2),(_X,3),(_Y,4),(_Z,5),(_a,6),(_b,7)))
_BoxServicesFanItemState_Type.__name__=_D
_BoxServicesFanItemState_Object=MibTableColumn
boxServicesFanItemState=_BoxServicesFanItemState_Object((1,3,6,1,4,1,4526,10,43,1,6,1,3),_BoxServicesFanItemState_Type())
boxServicesFanItemState.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesFanItemState.setStatus(_A)
class _BoxServicesFanSpeed_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,13))
_BoxServicesFanSpeed_Type.__name__=_I
_BoxServicesFanSpeed_Object=MibTableColumn
boxServicesFanSpeed=_BoxServicesFanSpeed_Object((1,3,6,1,4,1,4526,10,43,1,6,1,4),_BoxServicesFanSpeed_Type())
boxServicesFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesFanSpeed.setStatus(_A)
class _BoxServicesFanDutyLevel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,13))
_BoxServicesFanDutyLevel_Type.__name__=_I
_BoxServicesFanDutyLevel_Object=MibTableColumn
boxServicesFanDutyLevel=_BoxServicesFanDutyLevel_Object((1,3,6,1,4,1,4526,10,43,1,6,1,5),_BoxServicesFanDutyLevel_Type())
boxServicesFanDutyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesFanDutyLevel.setStatus(_A)
_BoxServicesFanUnitIndex_Type=Unsigned32
_BoxServicesFanUnitIndex_Object=MibTableColumn
boxServicesFanUnitIndex=_BoxServicesFanUnitIndex_Object((1,3,6,1,4,1,4526,10,43,1,6,1,6),_BoxServicesFanUnitIndex_Type())
boxServicesFanUnitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesFanUnitIndex.setStatus(_A)
_BoxServicesPowSuppliesTable_Object=MibTable
boxServicesPowSuppliesTable=_BoxServicesPowSuppliesTable_Object((1,3,6,1,4,1,4526,10,43,1,7))
if mibBuilder.loadTexts:boxServicesPowSuppliesTable.setStatus(_A)
_BoxServicesPowSuppliesEntry_Object=MibTableRow
boxServicesPowSuppliesEntry=_BoxServicesPowSuppliesEntry_Object((1,3,6,1,4,1,4526,10,43,1,7,1))
boxServicesPowSuppliesEntry.setIndexNames((0,_C,_c),(0,_C,_R))
if mibBuilder.loadTexts:boxServicesPowSuppliesEntry.setStatus(_A)
class _BoxServicesPowSupplyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BoxServicesPowSupplyIndex_Type.__name__=_D
_BoxServicesPowSupplyIndex_Object=MibTableColumn
boxServicesPowSupplyIndex=_BoxServicesPowSupplyIndex_Object((1,3,6,1,4,1,4526,10,43,1,7,1,1),_BoxServicesPowSupplyIndex_Type())
boxServicesPowSupplyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesPowSupplyIndex.setStatus(_A)
class _BoxServicesPowSupplyItemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6)))
_BoxServicesPowSupplyItemType_Type.__name__=_D
_BoxServicesPowSupplyItemType_Object=MibTableColumn
boxServicesPowSupplyItemType=_BoxServicesPowSupplyItemType_Object((1,3,6,1,4,1,4526,10,43,1,7,1,2),_BoxServicesPowSupplyItemType_Type())
boxServicesPowSupplyItemType.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesPowSupplyItemType.setStatus(_A)
class _BoxServicesPowSupplyItemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_J,1),(_W,2),(_X,3),(_Y,4),(_Z,5),(_a,6),(_b,7)))
_BoxServicesPowSupplyItemState_Type.__name__=_D
_BoxServicesPowSupplyItemState_Object=MibTableColumn
boxServicesPowSupplyItemState=_BoxServicesPowSupplyItemState_Object((1,3,6,1,4,1,4526,10,43,1,7,1,3),_BoxServicesPowSupplyItemState_Type())
boxServicesPowSupplyItemState.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesPowSupplyItemState.setStatus(_A)
_BoxServicesPowerSuppUnitIndex_Type=Unsigned32
_BoxServicesPowerSuppUnitIndex_Object=MibTableColumn
boxServicesPowerSuppUnitIndex=_BoxServicesPowerSuppUnitIndex_Object((1,3,6,1,4,1,4526,10,43,1,7,1,4),_BoxServicesPowerSuppUnitIndex_Type())
boxServicesPowerSuppUnitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesPowerSuppUnitIndex.setStatus(_A)
_BoxServicesTempSensorsTable_Object=MibTable
boxServicesTempSensorsTable=_BoxServicesTempSensorsTable_Object((1,3,6,1,4,1,4526,10,43,1,8))
if mibBuilder.loadTexts:boxServicesTempSensorsTable.setStatus(_A)
_BoxServicesTempSensorsEntry_Object=MibTableRow
boxServicesTempSensorsEntry=_BoxServicesTempSensorsEntry_Object((1,3,6,1,4,1,4526,10,43,1,8,1))
boxServicesTempSensorsEntry.setIndexNames((0,_C,_d),(0,_C,_S))
if mibBuilder.loadTexts:boxServicesTempSensorsEntry.setStatus(_A)
_BoxServicesUnitIndex_Type=Unsigned32
_BoxServicesUnitIndex_Object=MibTableColumn
boxServicesUnitIndex=_BoxServicesUnitIndex_Object((1,3,6,1,4,1,4526,10,43,1,8,1,1),_BoxServicesUnitIndex_Type())
boxServicesUnitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesUnitIndex.setStatus(_A)
_BoxServicesTempSensorIndex_Type=Unsigned32
_BoxServicesTempSensorIndex_Object=MibTableColumn
boxServicesTempSensorIndex=_BoxServicesTempSensorIndex_Object((1,3,6,1,4,1,4526,10,43,1,8,1,2),_BoxServicesTempSensorIndex_Type())
boxServicesTempSensorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesTempSensorIndex.setStatus(_A)
class _BoxServicesTempSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6)))
_BoxServicesTempSensorType_Type.__name__=_D
_BoxServicesTempSensorType_Object=MibTableColumn
boxServicesTempSensorType=_BoxServicesTempSensorType_Object((1,3,6,1,4,1,4526,10,43,1,8,1,3),_BoxServicesTempSensorType_Type())
boxServicesTempSensorType.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesTempSensorType.setStatus(_A)
_BoxServicesTempSensorState_Type=BoxsTemperatureStatus
_BoxServicesTempSensorState_Object=MibTableColumn
boxServicesTempSensorState=_BoxServicesTempSensorState_Object((1,3,6,1,4,1,4526,10,43,1,8,1,4),_BoxServicesTempSensorState_Type())
boxServicesTempSensorState.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesTempSensorState.setStatus(_e)
_BoxServicesTempSensorTemperature_Type=Integer32
_BoxServicesTempSensorTemperature_Object=MibTableColumn
boxServicesTempSensorTemperature=_BoxServicesTempSensorTemperature_Object((1,3,6,1,4,1,4526,10,43,1,8,1,5),_BoxServicesTempSensorTemperature_Type())
boxServicesTempSensorTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesTempSensorTemperature.setStatus(_A)
_BoxServicesThermalShutdownSensor_Type=Unsigned32
_BoxServicesThermalShutdownSensor_Object=MibScalar
boxServicesThermalShutdownSensor=_BoxServicesThermalShutdownSensor_Object((1,3,6,1,4,1,4526,10,43,1,13),_BoxServicesThermalShutdownSensor_Type())
boxServicesThermalShutdownSensor.setMaxAccess(_F)
if mibBuilder.loadTexts:boxServicesThermalShutdownSensor.setStatus(_A)
_BoxServicesThermalShutdownTemperature_Type=Unsigned32
_BoxServicesThermalShutdownTemperature_Object=MibScalar
boxServicesThermalShutdownTemperature=_BoxServicesThermalShutdownTemperature_Object((1,3,6,1,4,1,4526,10,43,1,14),_BoxServicesThermalShutdownTemperature_Type())
boxServicesThermalShutdownTemperature.setMaxAccess(_F)
if mibBuilder.loadTexts:boxServicesThermalShutdownTemperature.setStatus(_A)
_BoxServicesTempUnitTable_Object=MibTable
boxServicesTempUnitTable=_BoxServicesTempUnitTable_Object((1,3,6,1,4,1,4526,10,43,1,15))
if mibBuilder.loadTexts:boxServicesTempUnitTable.setStatus(_A)
_BoxServicesTempUnitEntry_Object=MibTableRow
boxServicesTempUnitEntry=_BoxServicesTempUnitEntry_Object((1,3,6,1,4,1,4526,10,43,1,15,1))
boxServicesTempUnitEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:boxServicesTempUnitEntry.setStatus(_A)
_BoxServicesTempUnitIndex_Type=Unsigned32
_BoxServicesTempUnitIndex_Object=MibTableColumn
boxServicesTempUnitIndex=_BoxServicesTempUnitIndex_Object((1,3,6,1,4,1,4526,10,43,1,15,1,1),_BoxServicesTempUnitIndex_Type())
boxServicesTempUnitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesTempUnitIndex.setStatus(_A)
_BoxServicesTempUnitState_Type=BoxsTemperatureStatus
_BoxServicesTempUnitState_Object=MibTableColumn
boxServicesTempUnitState=_BoxServicesTempUnitState_Object((1,3,6,1,4,1,4526,10,43,1,15,1,2),_BoxServicesTempUnitState_Type())
boxServicesTempUnitState.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesTempUnitState.setStatus(_A)
_BoxServicesTempUnitTemperature_Type=Integer32
_BoxServicesTempUnitTemperature_Object=MibTableColumn
boxServicesTempUnitTemperature=_BoxServicesTempUnitTemperature_Object((1,3,6,1,4,1,4526,10,43,1,15,1,3),_BoxServicesTempUnitTemperature_Type())
boxServicesTempUnitTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesTempUnitTemperature.setStatus(_A)
_BoxServicesFiberPortsOpticsTable_Object=MibTable
boxServicesFiberPortsOpticsTable=_BoxServicesFiberPortsOpticsTable_Object((1,3,6,1,4,1,4526,10,43,1,16))
if mibBuilder.loadTexts:boxServicesFiberPortsOpticsTable.setStatus(_A)
_BoxServicesFiberPortsOpticsEntry_Object=MibTableRow
boxServicesFiberPortsOpticsEntry=_BoxServicesFiberPortsOpticsEntry_Object((1,3,6,1,4,1,4526,10,43,1,16,1))
boxServicesFiberPortsOpticsEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:boxServicesFiberPortsOpticsEntry.setStatus(_A)
_BoxServicesFiberPortIndex_Type=Unsigned32
_BoxServicesFiberPortIndex_Object=MibTableColumn
boxServicesFiberPortIndex=_BoxServicesFiberPortIndex_Object((1,3,6,1,4,1,4526,10,43,1,16,1,1),_BoxServicesFiberPortIndex_Type())
boxServicesFiberPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesFiberPortIndex.setStatus(_A)
_BoxServicesFiberPortOpticsTemperature_Type=DisplayString
_BoxServicesFiberPortOpticsTemperature_Object=MibTableColumn
boxServicesFiberPortOpticsTemperature=_BoxServicesFiberPortOpticsTemperature_Object((1,3,6,1,4,1,4526,10,43,1,16,1,2),_BoxServicesFiberPortOpticsTemperature_Type())
boxServicesFiberPortOpticsTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesFiberPortOpticsTemperature.setStatus(_A)
if mibBuilder.loadTexts:boxServicesFiberPortOpticsTemperature.setUnits('DEGREES')
_BoxServicesFiberPortOpticsVoltage_Type=DisplayString
_BoxServicesFiberPortOpticsVoltage_Object=MibTableColumn
boxServicesFiberPortOpticsVoltage=_BoxServicesFiberPortOpticsVoltage_Object((1,3,6,1,4,1,4526,10,43,1,16,1,3),_BoxServicesFiberPortOpticsVoltage_Type())
boxServicesFiberPortOpticsVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesFiberPortOpticsVoltage.setStatus(_A)
if mibBuilder.loadTexts:boxServicesFiberPortOpticsVoltage.setUnits('Volts')
_BoxServicesFiberPortOpticsCurrent_Type=DisplayString
_BoxServicesFiberPortOpticsCurrent_Object=MibTableColumn
boxServicesFiberPortOpticsCurrent=_BoxServicesFiberPortOpticsCurrent_Object((1,3,6,1,4,1,4526,10,43,1,16,1,4),_BoxServicesFiberPortOpticsCurrent_Type())
boxServicesFiberPortOpticsCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesFiberPortOpticsCurrent.setStatus(_A)
if mibBuilder.loadTexts:boxServicesFiberPortOpticsCurrent.setUnits('Milliamps')
_BoxServicesFiberPortOpticsPowerOut_Type=DisplayString
_BoxServicesFiberPortOpticsPowerOut_Object=MibTableColumn
boxServicesFiberPortOpticsPowerOut=_BoxServicesFiberPortOpticsPowerOut_Object((1,3,6,1,4,1,4526,10,43,1,16,1,5),_BoxServicesFiberPortOpticsPowerOut_Type())
boxServicesFiberPortOpticsPowerOut.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesFiberPortOpticsPowerOut.setStatus(_A)
if mibBuilder.loadTexts:boxServicesFiberPortOpticsPowerOut.setUnits('dBm')
_BoxServicesFiberPortOpticsPowerIn_Type=DisplayString
_BoxServicesFiberPortOpticsPowerIn_Object=MibTableColumn
boxServicesFiberPortOpticsPowerIn=_BoxServicesFiberPortOpticsPowerIn_Object((1,3,6,1,4,1,4526,10,43,1,16,1,6),_BoxServicesFiberPortOpticsPowerIn_Type())
boxServicesFiberPortOpticsPowerIn.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesFiberPortOpticsPowerIn.setStatus(_A)
if mibBuilder.loadTexts:boxServicesFiberPortOpticsPowerIn.setUnits('dBm')
_BoxServicesFiberPortOpticsTxFault_Type=DisplayString
_BoxServicesFiberPortOpticsTxFault_Object=MibTableColumn
boxServicesFiberPortOpticsTxFault=_BoxServicesFiberPortOpticsTxFault_Object((1,3,6,1,4,1,4526,10,43,1,16,1,7),_BoxServicesFiberPortOpticsTxFault_Type())
boxServicesFiberPortOpticsTxFault.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesFiberPortOpticsTxFault.setStatus(_A)
_BoxServicesFiberPortOpticsLos_Type=DisplayString
_BoxServicesFiberPortOpticsLos_Object=MibTableColumn
boxServicesFiberPortOpticsLos=_BoxServicesFiberPortOpticsLos_Object((1,3,6,1,4,1,4526,10,43,1,16,1,8),_BoxServicesFiberPortOpticsLos_Type())
boxServicesFiberPortOpticsLos.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesFiberPortOpticsLos.setStatus(_A)
_BoxServicesFiberPortOpticsFaultStatus_Type=DisplayString
_BoxServicesFiberPortOpticsFaultStatus_Object=MibTableColumn
boxServicesFiberPortOpticsFaultStatus=_BoxServicesFiberPortOpticsFaultStatus_Object((1,3,6,1,4,1,4526,10,43,1,16,1,9),_BoxServicesFiberPortOpticsFaultStatus_Type())
boxServicesFiberPortOpticsFaultStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:boxServicesFiberPortOpticsFaultStatus.setStatus(_A)
_BoxServicesNotificationsGroup_ObjectIdentity=ObjectIdentity
boxServicesNotificationsGroup=_BoxServicesNotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4526,10,43,2))
class _BoxsItemStateChangeEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('insertion',1),('removal',2),('becomeoperational',3),('failure',4),('losepower',5)))
_BoxsItemStateChangeEvent_Type.__name__=_D
_BoxsItemStateChangeEvent_Object=MibScalar
boxsItemStateChangeEvent=_BoxsItemStateChangeEvent_Object((1,3,6,1,4,1,4526,10,43,2,1),_BoxsItemStateChangeEvent_Type())
boxsItemStateChangeEvent.setMaxAccess(_F)
if mibBuilder.loadTexts:boxsItemStateChangeEvent.setStatus(_A)
class _BoxsTemperatureChangeEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('abovethreshold',1),('belowthreshold',2),('withinnormalrange',3)))
_BoxsTemperatureChangeEvent_Type.__name__=_D
_BoxsTemperatureChangeEvent_Object=MibScalar
boxsTemperatureChangeEvent=_BoxsTemperatureChangeEvent_Object((1,3,6,1,4,1,4526,10,43,2,2),_BoxsTemperatureChangeEvent_Type())
boxsTemperatureChangeEvent.setMaxAccess(_F)
if mibBuilder.loadTexts:boxsTemperatureChangeEvent.setStatus(_A)
_BoxsTemperatureStatusCurrentEvent_Type=BoxsTemperatureStatus
_BoxsTemperatureStatusCurrentEvent_Object=MibScalar
boxsTemperatureStatusCurrentEvent=_BoxsTemperatureStatusCurrentEvent_Object((1,3,6,1,4,1,4526,10,43,2,3),_BoxsTemperatureStatusCurrentEvent_Type())
boxsTemperatureStatusCurrentEvent.setMaxAccess(_F)
if mibBuilder.loadTexts:boxsTemperatureStatusCurrentEvent.setStatus(_A)
_BoxsTemperatureStatusPreviousEvent_Type=BoxsTemperatureStatus
_BoxsTemperatureStatusPreviousEvent_Object=MibScalar
boxsTemperatureStatusPreviousEvent=_BoxsTemperatureStatusPreviousEvent_Object((1,3,6,1,4,1,4526,10,43,2,4),_BoxsTemperatureStatusPreviousEvent_Type())
boxsTemperatureStatusPreviousEvent.setMaxAccess(_F)
if mibBuilder.loadTexts:boxsTemperatureStatusPreviousEvent.setStatus(_A)
_BoxsLocatorLedConfigGroup_ObjectIdentity=ObjectIdentity
boxsLocatorLedConfigGroup=_BoxsLocatorLedConfigGroup_ObjectIdentity((1,3,6,1,4,1,4526,10,43,4))
_BoxsLocatorLedUnit_Type=Integer32
_BoxsLocatorLedUnit_Object=MibScalar
boxsLocatorLedUnit=_BoxsLocatorLedUnit_Object((1,3,6,1,4,1,4526,10,43,4,1),_BoxsLocatorLedUnit_Type())
boxsLocatorLedUnit.setMaxAccess(_E)
if mibBuilder.loadTexts:boxsLocatorLedUnit.setStatus(_A)
class _BoxsLocatorLedTime_Type(Integer32):defaultValue=20
_BoxsLocatorLedTime_Type.__name__=_D
_BoxsLocatorLedTime_Object=MibScalar
boxsLocatorLedTime=_BoxsLocatorLedTime_Object((1,3,6,1,4,1,4526,10,43,4,2),_BoxsLocatorLedTime_Type())
boxsLocatorLedTime.setMaxAccess(_E)
if mibBuilder.loadTexts:boxsLocatorLedTime.setStatus(_A)
class _BoxsLocatorLedEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_G,1)))
_BoxsLocatorLedEnable_Type.__name__=_D
_BoxsLocatorLedEnable_Object=MibScalar
boxsLocatorLedEnable=_BoxsLocatorLedEnable_Object((1,3,6,1,4,1,4526,10,43,4,3),_BoxsLocatorLedEnable_Type())
boxsLocatorLedEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:boxsLocatorLedEnable.setStatus(_A)
boxsFanStateChange=NotificationType((1,3,6,1,4,1,4526,10,43,0,1))
boxsFanStateChange.setObjects(*((_C,_K),(_C,_U)))
if mibBuilder.loadTexts:boxsFanStateChange.setStatus(_A)
boxsPowSupplyStateChange=NotificationType((1,3,6,1,4,1,4526,10,43,0,2))
boxsPowSupplyStateChange.setObjects(*((_C,_R),(_C,_U)))
if mibBuilder.loadTexts:boxsPowSupplyStateChange.setStatus(_A)
boxsTemperatureChange=NotificationType((1,3,6,1,4,1,4526,10,43,0,3))
boxsTemperatureChange.setObjects(*((_C,_S),(_C,_g)))
if mibBuilder.loadTexts:boxsTemperatureChange.setStatus(_e)
boxsThermalShutdown=NotificationType((1,3,6,1,4,1,4526,10,43,0,4))
boxsThermalShutdown.setObjects(*((_C,_h),(_C,_i)))
if mibBuilder.loadTexts:boxsThermalShutdown.setStatus(_A)
boxsTemperatureStateChange=NotificationType((1,3,6,1,4,1,4526,10,43,0,5))
boxsTemperatureStateChange.setObjects(*((_C,_T),(_C,_j),(_C,_k)))
if mibBuilder.loadTexts:boxsTemperatureStateChange.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'BoxsTemperatureStatus':BoxsTemperatureStatus,'fastPathBoxServices':fastPathBoxServices,'fastPathBoxServicesTraps':fastPathBoxServicesTraps,'boxsFanStateChange':boxsFanStateChange,'boxsPowSupplyStateChange':boxsPowSupplyStateChange,'boxsTemperatureChange':boxsTemperatureChange,'boxsThermalShutdown':boxsThermalShutdown,'boxsTemperatureStateChange':boxsTemperatureStateChange,'boxServicesGroup':boxServicesGroup,'boxServicesNormalTempRangeMin':boxServicesNormalTempRangeMin,'boxServicesNormalTempRangeMax':boxServicesNormalTempRangeMax,'boxServicesTemperatureTrapEnable':boxServicesTemperatureTrapEnable,'boxServicesPSMStateTrapEnable':boxServicesPSMStateTrapEnable,'boxServicesFanStateTrapEnable':boxServicesFanStateTrapEnable,'boxServicesFansTable':boxServicesFansTable,'boxServicesFansEntry':boxServicesFansEntry,_K:boxServicesFansIndex,'boxServicesFanItemType':boxServicesFanItemType,'boxServicesFanItemState':boxServicesFanItemState,'boxServicesFanSpeed':boxServicesFanSpeed,'boxServicesFanDutyLevel':boxServicesFanDutyLevel,_V:boxServicesFanUnitIndex,'boxServicesPowSuppliesTable':boxServicesPowSuppliesTable,'boxServicesPowSuppliesEntry':boxServicesPowSuppliesEntry,_R:boxServicesPowSupplyIndex,'boxServicesPowSupplyItemType':boxServicesPowSupplyItemType,'boxServicesPowSupplyItemState':boxServicesPowSupplyItemState,_c:boxServicesPowerSuppUnitIndex,'boxServicesTempSensorsTable':boxServicesTempSensorsTable,'boxServicesTempSensorsEntry':boxServicesTempSensorsEntry,_d:boxServicesUnitIndex,_S:boxServicesTempSensorIndex,'boxServicesTempSensorType':boxServicesTempSensorType,'boxServicesTempSensorState':boxServicesTempSensorState,'boxServicesTempSensorTemperature':boxServicesTempSensorTemperature,_h:boxServicesThermalShutdownSensor,_i:boxServicesThermalShutdownTemperature,'boxServicesTempUnitTable':boxServicesTempUnitTable,'boxServicesTempUnitEntry':boxServicesTempUnitEntry,_T:boxServicesTempUnitIndex,'boxServicesTempUnitState':boxServicesTempUnitState,'boxServicesTempUnitTemperature':boxServicesTempUnitTemperature,'boxServicesFiberPortsOpticsTable':boxServicesFiberPortsOpticsTable,'boxServicesFiberPortsOpticsEntry':boxServicesFiberPortsOpticsEntry,_f:boxServicesFiberPortIndex,'boxServicesFiberPortOpticsTemperature':boxServicesFiberPortOpticsTemperature,'boxServicesFiberPortOpticsVoltage':boxServicesFiberPortOpticsVoltage,'boxServicesFiberPortOpticsCurrent':boxServicesFiberPortOpticsCurrent,'boxServicesFiberPortOpticsPowerOut':boxServicesFiberPortOpticsPowerOut,'boxServicesFiberPortOpticsPowerIn':boxServicesFiberPortOpticsPowerIn,'boxServicesFiberPortOpticsTxFault':boxServicesFiberPortOpticsTxFault,'boxServicesFiberPortOpticsLos':boxServicesFiberPortOpticsLos,'boxServicesFiberPortOpticsFaultStatus':boxServicesFiberPortOpticsFaultStatus,'boxServicesNotificationsGroup':boxServicesNotificationsGroup,_U:boxsItemStateChangeEvent,_g:boxsTemperatureChangeEvent,_j:boxsTemperatureStatusCurrentEvent,_k:boxsTemperatureStatusPreviousEvent,'boxsLocatorLedConfigGroup':boxsLocatorLedConfigGroup,'boxsLocatorLedUnit':boxsLocatorLedUnit,'boxsLocatorLedTime':boxsLocatorLedTime,'boxsLocatorLedEnable':boxsLocatorLedEnable})