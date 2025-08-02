_i='pdu8306MeasurementBoxEvt'
_h='pdu8306HygroEvtSen1'
_g='pdu8306TempEvtSen1'
_f='pdu8306InputSensor'
_e='pdu8306ResetTime'
_d='pdu8306EnergyReactiveResettable'
_c='pdu8306EnergyActiveResettable'
_b='pdu8306EnergyReactive'
_a='pdu8306PowerReactive'
_Z='pdu8306PowerApparent'
_Y='pdu8306Pangle'
_X='pdu8306PowerFactor'
_W='pdu8306Frequency'
_V='pdu8306Voltage'
_U='pdu8306Current'
_T='pdu8306PowerActive'
_S='pdu8306AbsEnergyActive'
_R='pdu8306ChanStatus'
_Q='pdu8306ActivePowerChan'
_P='pdu8306TrapAddr'
_O='pdu8306TrapCtrl'
_N='pdu8306SensorIndex'
_M='pdu8306PowerIndex'
_L='pdu8306TrapIPIndex'
_K='read-write'
_J='Unsigned32'
_I='OctetString'
_H='pdu8306HygroSensor'
_G='pdu8306TempSensor'
_F='pdu8306MeasurementBoxConnected'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='GUDEADS-PDU8306-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-03-05 13:56',))
_GadsPDU8306_ObjectIdentity=ObjectIdentity
gadsPDU8306=_GadsPDU8306_ObjectIdentity((1,3,6,1,4,1,28507,44))
_Events_ObjectIdentity=ObjectIdentity
events=_Events_ObjectIdentity((1,3,6,1,4,1,28507,44,0))
_Pdu8306Objects_ObjectIdentity=ObjectIdentity
pdu8306Objects=_Pdu8306Objects_ObjectIdentity((1,3,6,1,4,1,28507,44,1))
_Pdu8306CommonConfig_ObjectIdentity=ObjectIdentity
pdu8306CommonConfig=_Pdu8306CommonConfig_ObjectIdentity((1,3,6,1,4,1,28507,44,1,1))
_Pdu8306SNMPaccess_ObjectIdentity=ObjectIdentity
pdu8306SNMPaccess=_Pdu8306SNMPaccess_ObjectIdentity((1,3,6,1,4,1,28507,44,1,1,1))
class _Pdu8306TrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Pdu8306TrapCtrl_Type.__name__=_D
_Pdu8306TrapCtrl_Object=MibScalar
pdu8306TrapCtrl=_Pdu8306TrapCtrl_Object((1,3,6,1,4,1,28507,44,1,1,1,1),_Pdu8306TrapCtrl_Type())
pdu8306TrapCtrl.setMaxAccess(_K)
if mibBuilder.loadTexts:pdu8306TrapCtrl.setStatus(_A)
_Pdu8306TrapIPTable_Object=MibTable
pdu8306TrapIPTable=_Pdu8306TrapIPTable_Object((1,3,6,1,4,1,28507,44,1,1,1,2))
if mibBuilder.loadTexts:pdu8306TrapIPTable.setStatus(_A)
_Pdu8306TrapIPEntry_Object=MibTableRow
pdu8306TrapIPEntry=_Pdu8306TrapIPEntry_Object((1,3,6,1,4,1,28507,44,1,1,1,2,1))
pdu8306TrapIPEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:pdu8306TrapIPEntry.setStatus(_A)
class _Pdu8306TrapIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Pdu8306TrapIPIndex_Type.__name__=_D
_Pdu8306TrapIPIndex_Object=MibTableColumn
pdu8306TrapIPIndex=_Pdu8306TrapIPIndex_Object((1,3,6,1,4,1,28507,44,1,1,1,2,1,1),_Pdu8306TrapIPIndex_Type())
pdu8306TrapIPIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:pdu8306TrapIPIndex.setStatus(_A)
class _Pdu8306TrapAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Pdu8306TrapAddr_Type.__name__=_I
_Pdu8306TrapAddr_Object=MibTableColumn
pdu8306TrapAddr=_Pdu8306TrapAddr_Object((1,3,6,1,4,1,28507,44,1,1,1,2,1,2),_Pdu8306TrapAddr_Type())
pdu8306TrapAddr.setMaxAccess(_K)
if mibBuilder.loadTexts:pdu8306TrapAddr.setStatus(_A)
_Pdu8306DeviceConfig_ObjectIdentity=ObjectIdentity
pdu8306DeviceConfig=_Pdu8306DeviceConfig_ObjectIdentity((1,3,6,1,4,1,28507,44,1,2))
_Pdu8306IntActors_ObjectIdentity=ObjectIdentity
pdu8306IntActors=_Pdu8306IntActors_ObjectIdentity((1,3,6,1,4,1,28507,44,1,3))
_Pdu8306ExtActors_ObjectIdentity=ObjectIdentity
pdu8306ExtActors=_Pdu8306ExtActors_ObjectIdentity((1,3,6,1,4,1,28507,44,1,4))
_Pdu8306IntSensors_ObjectIdentity=ObjectIdentity
pdu8306IntSensors=_Pdu8306IntSensors_ObjectIdentity((1,3,6,1,4,1,28507,44,1,5))
_Pdu8306PowerChan_ObjectIdentity=ObjectIdentity
pdu8306PowerChan=_Pdu8306PowerChan_ObjectIdentity((1,3,6,1,4,1,28507,44,1,5,1))
class _Pdu8306ActivePowerChan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Pdu8306ActivePowerChan_Type.__name__=_J
_Pdu8306ActivePowerChan_Object=MibScalar
pdu8306ActivePowerChan=_Pdu8306ActivePowerChan_Object((1,3,6,1,4,1,28507,44,1,5,1,1),_Pdu8306ActivePowerChan_Type())
pdu8306ActivePowerChan.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8306ActivePowerChan.setStatus(_A)
_Pdu8306PowerTable_Object=MibTable
pdu8306PowerTable=_Pdu8306PowerTable_Object((1,3,6,1,4,1,28507,44,1,5,1,2))
if mibBuilder.loadTexts:pdu8306PowerTable.setStatus(_A)
_Pdu8306PowerEntry_Object=MibTableRow
pdu8306PowerEntry=_Pdu8306PowerEntry_Object((1,3,6,1,4,1,28507,44,1,5,1,2,1))
pdu8306PowerEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:pdu8306PowerEntry.setStatus(_A)
class _Pdu8306PowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Pdu8306PowerIndex_Type.__name__=_D
_Pdu8306PowerIndex_Object=MibTableColumn
pdu8306PowerIndex=_Pdu8306PowerIndex_Object((1,3,6,1,4,1,28507,44,1,5,1,2,1,1),_Pdu8306PowerIndex_Type())
pdu8306PowerIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:pdu8306PowerIndex.setStatus(_A)
class _Pdu8306ChanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Pdu8306ChanStatus_Type.__name__=_D
_Pdu8306ChanStatus_Object=MibTableColumn
pdu8306ChanStatus=_Pdu8306ChanStatus_Object((1,3,6,1,4,1,28507,44,1,5,1,2,1,2),_Pdu8306ChanStatus_Type())
pdu8306ChanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8306ChanStatus.setStatus(_A)
_Pdu8306AbsEnergyActive_Type=Unsigned32
_Pdu8306AbsEnergyActive_Object=MibTableColumn
pdu8306AbsEnergyActive=_Pdu8306AbsEnergyActive_Object((1,3,6,1,4,1,28507,44,1,5,1,2,1,3),_Pdu8306AbsEnergyActive_Type())
pdu8306AbsEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8306AbsEnergyActive.setStatus(_A)
if mibBuilder.loadTexts:pdu8306AbsEnergyActive.setUnits('Wh')
_Pdu8306PowerActive_Type=Integer32
_Pdu8306PowerActive_Object=MibTableColumn
pdu8306PowerActive=_Pdu8306PowerActive_Object((1,3,6,1,4,1,28507,44,1,5,1,2,1,4),_Pdu8306PowerActive_Type())
pdu8306PowerActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8306PowerActive.setStatus(_A)
if mibBuilder.loadTexts:pdu8306PowerActive.setUnits('W')
_Pdu8306Current_Type=Unsigned32
_Pdu8306Current_Object=MibTableColumn
pdu8306Current=_Pdu8306Current_Object((1,3,6,1,4,1,28507,44,1,5,1,2,1,5),_Pdu8306Current_Type())
pdu8306Current.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8306Current.setStatus(_A)
if mibBuilder.loadTexts:pdu8306Current.setUnits('mA')
_Pdu8306Voltage_Type=Unsigned32
_Pdu8306Voltage_Object=MibTableColumn
pdu8306Voltage=_Pdu8306Voltage_Object((1,3,6,1,4,1,28507,44,1,5,1,2,1,6),_Pdu8306Voltage_Type())
pdu8306Voltage.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8306Voltage.setStatus(_A)
if mibBuilder.loadTexts:pdu8306Voltage.setUnits('V')
_Pdu8306Frequency_Type=Unsigned32
_Pdu8306Frequency_Object=MibTableColumn
pdu8306Frequency=_Pdu8306Frequency_Object((1,3,6,1,4,1,28507,44,1,5,1,2,1,7),_Pdu8306Frequency_Type())
pdu8306Frequency.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8306Frequency.setStatus(_A)
if mibBuilder.loadTexts:pdu8306Frequency.setUnits('0.01 hz')
_Pdu8306PowerFactor_Type=Integer32
_Pdu8306PowerFactor_Object=MibTableColumn
pdu8306PowerFactor=_Pdu8306PowerFactor_Object((1,3,6,1,4,1,28507,44,1,5,1,2,1,8),_Pdu8306PowerFactor_Type())
pdu8306PowerFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8306PowerFactor.setStatus(_A)
if mibBuilder.loadTexts:pdu8306PowerFactor.setUnits('0.001')
_Pdu8306Pangle_Type=Integer32
_Pdu8306Pangle_Object=MibTableColumn
pdu8306Pangle=_Pdu8306Pangle_Object((1,3,6,1,4,1,28507,44,1,5,1,2,1,9),_Pdu8306Pangle_Type())
pdu8306Pangle.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8306Pangle.setStatus(_A)
if mibBuilder.loadTexts:pdu8306Pangle.setUnits('0.1 degree')
_Pdu8306PowerApparent_Type=Integer32
_Pdu8306PowerApparent_Object=MibTableColumn
pdu8306PowerApparent=_Pdu8306PowerApparent_Object((1,3,6,1,4,1,28507,44,1,5,1,2,1,10),_Pdu8306PowerApparent_Type())
pdu8306PowerApparent.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8306PowerApparent.setStatus(_A)
if mibBuilder.loadTexts:pdu8306PowerApparent.setUnits('VA')
_Pdu8306PowerReactive_Type=Integer32
_Pdu8306PowerReactive_Object=MibTableColumn
pdu8306PowerReactive=_Pdu8306PowerReactive_Object((1,3,6,1,4,1,28507,44,1,5,1,2,1,11),_Pdu8306PowerReactive_Type())
pdu8306PowerReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8306PowerReactive.setStatus(_A)
if mibBuilder.loadTexts:pdu8306PowerReactive.setUnits('VAR')
_Pdu8306EnergyReactive_Type=Unsigned32
_Pdu8306EnergyReactive_Object=MibTableColumn
pdu8306EnergyReactive=_Pdu8306EnergyReactive_Object((1,3,6,1,4,1,28507,44,1,5,1,2,1,12),_Pdu8306EnergyReactive_Type())
pdu8306EnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8306EnergyReactive.setStatus(_A)
if mibBuilder.loadTexts:pdu8306EnergyReactive.setUnits('VARh')
_Pdu8306EnergyActiveResettable_Type=Unsigned32
_Pdu8306EnergyActiveResettable_Object=MibTableColumn
pdu8306EnergyActiveResettable=_Pdu8306EnergyActiveResettable_Object((1,3,6,1,4,1,28507,44,1,5,1,2,1,13),_Pdu8306EnergyActiveResettable_Type())
pdu8306EnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8306EnergyActiveResettable.setStatus(_A)
if mibBuilder.loadTexts:pdu8306EnergyActiveResettable.setUnits('Wh')
_Pdu8306EnergyReactiveResettable_Type=Unsigned32
_Pdu8306EnergyReactiveResettable_Object=MibTableColumn
pdu8306EnergyReactiveResettable=_Pdu8306EnergyReactiveResettable_Object((1,3,6,1,4,1,28507,44,1,5,1,2,1,14),_Pdu8306EnergyReactiveResettable_Type())
pdu8306EnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8306EnergyReactiveResettable.setStatus(_A)
if mibBuilder.loadTexts:pdu8306EnergyReactiveResettable.setUnits('VARh')
_Pdu8306ResetTime_Type=Unsigned32
_Pdu8306ResetTime_Object=MibTableColumn
pdu8306ResetTime=_Pdu8306ResetTime_Object((1,3,6,1,4,1,28507,44,1,5,1,2,1,15),_Pdu8306ResetTime_Type())
pdu8306ResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8306ResetTime.setStatus(_A)
if mibBuilder.loadTexts:pdu8306ResetTime.setUnits('s')
class _Pdu8306MeasurementBoxConnected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disconnected',0),('connected',1)))
_Pdu8306MeasurementBoxConnected_Type.__name__=_D
_Pdu8306MeasurementBoxConnected_Object=MibScalar
pdu8306MeasurementBoxConnected=_Pdu8306MeasurementBoxConnected_Object((1,3,6,1,4,1,28507,44,1,5,12),_Pdu8306MeasurementBoxConnected_Type())
pdu8306MeasurementBoxConnected.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8306MeasurementBoxConnected.setStatus(_A)
_Pdu8306ExtSensors_ObjectIdentity=ObjectIdentity
pdu8306ExtSensors=_Pdu8306ExtSensors_ObjectIdentity((1,3,6,1,4,1,28507,44,1,6))
_Pdu8306SensorTable_Object=MibTable
pdu8306SensorTable=_Pdu8306SensorTable_Object((1,3,6,1,4,1,28507,44,1,6,1))
if mibBuilder.loadTexts:pdu8306SensorTable.setStatus(_A)
_Pdu8306SensorEntry_Object=MibTableRow
pdu8306SensorEntry=_Pdu8306SensorEntry_Object((1,3,6,1,4,1,28507,44,1,6,1,1))
pdu8306SensorEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:pdu8306SensorEntry.setStatus(_A)
class _Pdu8306SensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Pdu8306SensorIndex_Type.__name__=_D
_Pdu8306SensorIndex_Object=MibTableColumn
pdu8306SensorIndex=_Pdu8306SensorIndex_Object((1,3,6,1,4,1,28507,44,1,6,1,1,1),_Pdu8306SensorIndex_Type())
pdu8306SensorIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:pdu8306SensorIndex.setStatus(_A)
_Pdu8306TempSensor_Type=Integer32
_Pdu8306TempSensor_Object=MibTableColumn
pdu8306TempSensor=_Pdu8306TempSensor_Object((1,3,6,1,4,1,28507,44,1,6,1,1,2),_Pdu8306TempSensor_Type())
pdu8306TempSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8306TempSensor.setStatus(_A)
if mibBuilder.loadTexts:pdu8306TempSensor.setUnits('0.1 degree Celsius')
_Pdu8306HygroSensor_Type=Integer32
_Pdu8306HygroSensor_Object=MibTableColumn
pdu8306HygroSensor=_Pdu8306HygroSensor_Object((1,3,6,1,4,1,28507,44,1,6,1,1,3),_Pdu8306HygroSensor_Type())
pdu8306HygroSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8306HygroSensor.setStatus(_A)
if mibBuilder.loadTexts:pdu8306HygroSensor.setUnits('0.1 percent humidity')
class _Pdu8306InputSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_Pdu8306InputSensor_Type.__name__=_D
_Pdu8306InputSensor_Object=MibTableColumn
pdu8306InputSensor=_Pdu8306InputSensor_Object((1,3,6,1,4,1,28507,44,1,6,1,1,4),_Pdu8306InputSensor_Type())
pdu8306InputSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8306InputSensor.setStatus(_A)
_Pdu8306Conf_ObjectIdentity=ObjectIdentity
pdu8306Conf=_Pdu8306Conf_ObjectIdentity((1,3,6,1,4,1,28507,44,2))
_Pdu8306Groups_ObjectIdentity=ObjectIdentity
pdu8306Groups=_Pdu8306Groups_ObjectIdentity((1,3,6,1,4,1,28507,44,2,1))
_Pdu8306Compls_ObjectIdentity=ObjectIdentity
pdu8306Compls=_Pdu8306Compls_ObjectIdentity((1,3,6,1,4,1,28507,44,2,2))
pdu8306BasicGroup=ObjectGroup((1,3,6,1,4,1,28507,44,2,1,1))
pdu8306BasicGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_F),(_B,_G),(_B,_H),(_B,_f)))
if mibBuilder.loadTexts:pdu8306BasicGroup.setStatus(_A)
pdu8306TempEvtSen1=NotificationType((1,3,6,1,4,1,28507,44,0,1))
pdu8306TempEvtSen1.setObjects((_B,_G))
if mibBuilder.loadTexts:pdu8306TempEvtSen1.setStatus(_A)
pdu8306HygroEvtSen1=NotificationType((1,3,6,1,4,1,28507,44,0,2))
pdu8306HygroEvtSen1.setObjects((_B,_H))
if mibBuilder.loadTexts:pdu8306HygroEvtSen1.setStatus(_A)
pdu8306MeasurementBoxEvt=NotificationType((1,3,6,1,4,1,28507,44,0,3))
pdu8306MeasurementBoxEvt.setObjects((_B,_F))
if mibBuilder.loadTexts:pdu8306MeasurementBoxEvt.setStatus(_A)
pdu8306NotificationGroup=NotificationGroup((1,3,6,1,4,1,28507,44,2,1,2))
pdu8306NotificationGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:pdu8306NotificationGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'gudeads':gudeads,'gadsPDU8306':gadsPDU8306,'events':events,_g:pdu8306TempEvtSen1,_h:pdu8306HygroEvtSen1,_i:pdu8306MeasurementBoxEvt,'pdu8306Objects':pdu8306Objects,'pdu8306CommonConfig':pdu8306CommonConfig,'pdu8306SNMPaccess':pdu8306SNMPaccess,_O:pdu8306TrapCtrl,'pdu8306TrapIPTable':pdu8306TrapIPTable,'pdu8306TrapIPEntry':pdu8306TrapIPEntry,_L:pdu8306TrapIPIndex,_P:pdu8306TrapAddr,'pdu8306DeviceConfig':pdu8306DeviceConfig,'pdu8306IntActors':pdu8306IntActors,'pdu8306ExtActors':pdu8306ExtActors,'pdu8306IntSensors':pdu8306IntSensors,'pdu8306PowerChan':pdu8306PowerChan,_Q:pdu8306ActivePowerChan,'pdu8306PowerTable':pdu8306PowerTable,'pdu8306PowerEntry':pdu8306PowerEntry,_M:pdu8306PowerIndex,_R:pdu8306ChanStatus,_S:pdu8306AbsEnergyActive,_T:pdu8306PowerActive,_U:pdu8306Current,_V:pdu8306Voltage,_W:pdu8306Frequency,_X:pdu8306PowerFactor,_Y:pdu8306Pangle,_Z:pdu8306PowerApparent,_a:pdu8306PowerReactive,_b:pdu8306EnergyReactive,_c:pdu8306EnergyActiveResettable,_d:pdu8306EnergyReactiveResettable,_e:pdu8306ResetTime,_F:pdu8306MeasurementBoxConnected,'pdu8306ExtSensors':pdu8306ExtSensors,'pdu8306SensorTable':pdu8306SensorTable,'pdu8306SensorEntry':pdu8306SensorEntry,_N:pdu8306SensorIndex,_G:pdu8306TempSensor,_H:pdu8306HygroSensor,_f:pdu8306InputSensor,'pdu8306Conf':pdu8306Conf,'pdu8306Groups':pdu8306Groups,'pdu8306BasicGroup':pdu8306BasicGroup,'pdu8306NotificationGroup':pdu8306NotificationGroup,'pdu8306Compls':pdu8306Compls})