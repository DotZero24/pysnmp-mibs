_z='pdu8340LineAmperageEvt'
_y='pdu8340DewPtDiffEvtSen'
_x='pdu8340AirPressureEvtSen'
_w='pdu8340InputEvtSen'
_v='pdu8340HygroEvtSen'
_u='pdu8340TempEvtSen'
_t='pdu8340DewPoint'
_s='pdu8340ResidualCurrent'
_r='pdu8340RevEnergyReactiveResettable'
_q='pdu8340RevEnergyActiveResettable'
_p='pdu8340RevEnergyReactive'
_o='pdu8340RevEnergyActive'
_n='pdu8340ForwEnergyReactiveResettable'
_m='pdu8340ForwEnergyActiveResettable'
_l='pdu8340ForwEnergyReactive'
_k='pdu8340ForwEnergyActive'
_j='pdu8340ResetTime'
_i='pdu8340AbsEnergyReactiveResettable'
_h='pdu8340AbsEnergyActiveResettable'
_g='pdu8340AbsEnergyReactive'
_f='pdu8340Pangle'
_e='pdu8340PowerFactor'
_d='pdu8340AbsEnergyActive'
_c='pdu8340ChanStatus'
_b='pdu8340ActivePowerChan'
_a='pdu8340Buzzer'
_Z='pdu8340TrapAddr'
_Y='pdu8340TrapCtrl'
_X='Unsigned32'
_W='OctetString'
_V='pdu8340DewPointDiff'
_U='pdu8340AirPressure'
_T='pdu8340InputSensor'
_S='pdu8340HygroSensor'
_R='pdu8340TempSensor'
_Q='pdu8340PowerReactive'
_P='pdu8340PowerApparent'
_O='pdu8340Frequency'
_N='pdu8340Voltage'
_M='pdu8340Current'
_L='pdu8340PowerActive'
_K='0.1 degree Celsius'
_J='pdu8340TrapIPIndex'
_I='pdu8340PowerIndex'
_H='read-write'
_G='VARh'
_F='Wh'
_E='pdu8340SensorIndex'
_D='Integer32'
_C='read-only'
_B='current'
_A='GUDEADS-PDU8340-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_W,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_X,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-03-05 13:56',))
_GadsPDU8340_ObjectIdentity=ObjectIdentity
gadsPDU8340=_GadsPDU8340_ObjectIdentity((1,3,6,1,4,1,28507,54))
_Pdu8340Objects_ObjectIdentity=ObjectIdentity
pdu8340Objects=_Pdu8340Objects_ObjectIdentity((1,3,6,1,4,1,28507,54,1))
_Pdu8340CommonConfig_ObjectIdentity=ObjectIdentity
pdu8340CommonConfig=_Pdu8340CommonConfig_ObjectIdentity((1,3,6,1,4,1,28507,54,1,1))
_Pdu8340SNMPaccess_ObjectIdentity=ObjectIdentity
pdu8340SNMPaccess=_Pdu8340SNMPaccess_ObjectIdentity((1,3,6,1,4,1,28507,54,1,1,1))
class _Pdu8340TrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Pdu8340TrapCtrl_Type.__name__=_D
_Pdu8340TrapCtrl_Object=MibScalar
pdu8340TrapCtrl=_Pdu8340TrapCtrl_Object((1,3,6,1,4,1,28507,54,1,1,1,1),_Pdu8340TrapCtrl_Type())
pdu8340TrapCtrl.setMaxAccess(_H)
if mibBuilder.loadTexts:pdu8340TrapCtrl.setStatus(_B)
_Pdu8340TrapIPTable_Object=MibTable
pdu8340TrapIPTable=_Pdu8340TrapIPTable_Object((1,3,6,1,4,1,28507,54,1,1,1,2))
if mibBuilder.loadTexts:pdu8340TrapIPTable.setStatus(_B)
_Pdu8340TrapIPEntry_Object=MibTableRow
pdu8340TrapIPEntry=_Pdu8340TrapIPEntry_Object((1,3,6,1,4,1,28507,54,1,1,1,2,1))
pdu8340TrapIPEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:pdu8340TrapIPEntry.setStatus(_B)
class _Pdu8340TrapIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Pdu8340TrapIPIndex_Type.__name__=_D
_Pdu8340TrapIPIndex_Object=MibTableColumn
pdu8340TrapIPIndex=_Pdu8340TrapIPIndex_Object((1,3,6,1,4,1,28507,54,1,1,1,2,1,1),_Pdu8340TrapIPIndex_Type())
pdu8340TrapIPIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340TrapIPIndex.setStatus(_B)
class _Pdu8340TrapAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Pdu8340TrapAddr_Type.__name__=_W
_Pdu8340TrapAddr_Object=MibTableColumn
pdu8340TrapAddr=_Pdu8340TrapAddr_Object((1,3,6,1,4,1,28507,54,1,1,1,2,1,2),_Pdu8340TrapAddr_Type())
pdu8340TrapAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:pdu8340TrapAddr.setStatus(_B)
_Pdu8340DeviceConfig_ObjectIdentity=ObjectIdentity
pdu8340DeviceConfig=_Pdu8340DeviceConfig_ObjectIdentity((1,3,6,1,4,1,28507,54,1,2))
_Pdu8340IntActors_ObjectIdentity=ObjectIdentity
pdu8340IntActors=_Pdu8340IntActors_ObjectIdentity((1,3,6,1,4,1,28507,54,1,3))
class _Pdu8340Buzzer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Pdu8340Buzzer_Type.__name__=_D
_Pdu8340Buzzer_Object=MibScalar
pdu8340Buzzer=_Pdu8340Buzzer_Object((1,3,6,1,4,1,28507,54,1,3,10),_Pdu8340Buzzer_Type())
pdu8340Buzzer.setMaxAccess(_H)
if mibBuilder.loadTexts:pdu8340Buzzer.setStatus(_B)
if mibBuilder.loadTexts:pdu8340Buzzer.setUnits('0 = Off, 1 = On')
_Pdu8340ExtActors_ObjectIdentity=ObjectIdentity
pdu8340ExtActors=_Pdu8340ExtActors_ObjectIdentity((1,3,6,1,4,1,28507,54,1,4))
_Pdu8340IntSensors_ObjectIdentity=ObjectIdentity
pdu8340IntSensors=_Pdu8340IntSensors_ObjectIdentity((1,3,6,1,4,1,28507,54,1,5))
_Pdu8340PowerChan_ObjectIdentity=ObjectIdentity
pdu8340PowerChan=_Pdu8340PowerChan_ObjectIdentity((1,3,6,1,4,1,28507,54,1,5,1))
class _Pdu8340ActivePowerChan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Pdu8340ActivePowerChan_Type.__name__=_X
_Pdu8340ActivePowerChan_Object=MibScalar
pdu8340ActivePowerChan=_Pdu8340ActivePowerChan_Object((1,3,6,1,4,1,28507,54,1,5,1,1),_Pdu8340ActivePowerChan_Type())
pdu8340ActivePowerChan.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340ActivePowerChan.setStatus(_B)
_Pdu8340PowerTable_Object=MibTable
pdu8340PowerTable=_Pdu8340PowerTable_Object((1,3,6,1,4,1,28507,54,1,5,1,2))
if mibBuilder.loadTexts:pdu8340PowerTable.setStatus(_B)
_Pdu8340PowerEntry_Object=MibTableRow
pdu8340PowerEntry=_Pdu8340PowerEntry_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1))
pdu8340PowerEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:pdu8340PowerEntry.setStatus(_B)
class _Pdu8340PowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Pdu8340PowerIndex_Type.__name__=_D
_Pdu8340PowerIndex_Object=MibTableColumn
pdu8340PowerIndex=_Pdu8340PowerIndex_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,1),_Pdu8340PowerIndex_Type())
pdu8340PowerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340PowerIndex.setStatus(_B)
class _Pdu8340ChanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Pdu8340ChanStatus_Type.__name__=_D
_Pdu8340ChanStatus_Object=MibTableColumn
pdu8340ChanStatus=_Pdu8340ChanStatus_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,2),_Pdu8340ChanStatus_Type())
pdu8340ChanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340ChanStatus.setStatus(_B)
_Pdu8340AbsEnergyActive_Type=Unsigned32
_Pdu8340AbsEnergyActive_Object=MibTableColumn
pdu8340AbsEnergyActive=_Pdu8340AbsEnergyActive_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,3),_Pdu8340AbsEnergyActive_Type())
pdu8340AbsEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340AbsEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:pdu8340AbsEnergyActive.setUnits(_F)
_Pdu8340PowerActive_Type=Integer32
_Pdu8340PowerActive_Object=MibTableColumn
pdu8340PowerActive=_Pdu8340PowerActive_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,4),_Pdu8340PowerActive_Type())
pdu8340PowerActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340PowerActive.setStatus(_B)
if mibBuilder.loadTexts:pdu8340PowerActive.setUnits('W')
_Pdu8340Current_Type=Unsigned32
_Pdu8340Current_Object=MibTableColumn
pdu8340Current=_Pdu8340Current_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,5),_Pdu8340Current_Type())
pdu8340Current.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340Current.setStatus(_B)
if mibBuilder.loadTexts:pdu8340Current.setUnits('mA')
_Pdu8340Voltage_Type=Unsigned32
_Pdu8340Voltage_Object=MibTableColumn
pdu8340Voltage=_Pdu8340Voltage_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,6),_Pdu8340Voltage_Type())
pdu8340Voltage.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340Voltage.setStatus(_B)
if mibBuilder.loadTexts:pdu8340Voltage.setUnits('V')
_Pdu8340Frequency_Type=Unsigned32
_Pdu8340Frequency_Object=MibTableColumn
pdu8340Frequency=_Pdu8340Frequency_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,7),_Pdu8340Frequency_Type())
pdu8340Frequency.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340Frequency.setStatus(_B)
if mibBuilder.loadTexts:pdu8340Frequency.setUnits('0.01 hz')
_Pdu8340PowerFactor_Type=Integer32
_Pdu8340PowerFactor_Object=MibTableColumn
pdu8340PowerFactor=_Pdu8340PowerFactor_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,8),_Pdu8340PowerFactor_Type())
pdu8340PowerFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340PowerFactor.setStatus(_B)
if mibBuilder.loadTexts:pdu8340PowerFactor.setUnits('0.001')
_Pdu8340Pangle_Type=Integer32
_Pdu8340Pangle_Object=MibTableColumn
pdu8340Pangle=_Pdu8340Pangle_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,9),_Pdu8340Pangle_Type())
pdu8340Pangle.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340Pangle.setStatus(_B)
if mibBuilder.loadTexts:pdu8340Pangle.setUnits('0.1 degree')
_Pdu8340PowerApparent_Type=Integer32
_Pdu8340PowerApparent_Object=MibTableColumn
pdu8340PowerApparent=_Pdu8340PowerApparent_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,10),_Pdu8340PowerApparent_Type())
pdu8340PowerApparent.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340PowerApparent.setStatus(_B)
if mibBuilder.loadTexts:pdu8340PowerApparent.setUnits('VA')
_Pdu8340PowerReactive_Type=Integer32
_Pdu8340PowerReactive_Object=MibTableColumn
pdu8340PowerReactive=_Pdu8340PowerReactive_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,11),_Pdu8340PowerReactive_Type())
pdu8340PowerReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340PowerReactive.setStatus(_B)
if mibBuilder.loadTexts:pdu8340PowerReactive.setUnits('VAR')
_Pdu8340AbsEnergyReactive_Type=Unsigned32
_Pdu8340AbsEnergyReactive_Object=MibTableColumn
pdu8340AbsEnergyReactive=_Pdu8340AbsEnergyReactive_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,12),_Pdu8340AbsEnergyReactive_Type())
pdu8340AbsEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340AbsEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:pdu8340AbsEnergyReactive.setUnits(_G)
_Pdu8340AbsEnergyActiveResettable_Type=Unsigned32
_Pdu8340AbsEnergyActiveResettable_Object=MibTableColumn
pdu8340AbsEnergyActiveResettable=_Pdu8340AbsEnergyActiveResettable_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,13),_Pdu8340AbsEnergyActiveResettable_Type())
pdu8340AbsEnergyActiveResettable.setMaxAccess(_H)
if mibBuilder.loadTexts:pdu8340AbsEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu8340AbsEnergyActiveResettable.setUnits(_F)
_Pdu8340AbsEnergyReactiveResettable_Type=Unsigned32
_Pdu8340AbsEnergyReactiveResettable_Object=MibTableColumn
pdu8340AbsEnergyReactiveResettable=_Pdu8340AbsEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,14),_Pdu8340AbsEnergyReactiveResettable_Type())
pdu8340AbsEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340AbsEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu8340AbsEnergyReactiveResettable.setUnits(_G)
_Pdu8340ResetTime_Type=Unsigned32
_Pdu8340ResetTime_Object=MibTableColumn
pdu8340ResetTime=_Pdu8340ResetTime_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,15),_Pdu8340ResetTime_Type())
pdu8340ResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340ResetTime.setStatus(_B)
if mibBuilder.loadTexts:pdu8340ResetTime.setUnits('s')
_Pdu8340ForwEnergyActive_Type=Unsigned32
_Pdu8340ForwEnergyActive_Object=MibTableColumn
pdu8340ForwEnergyActive=_Pdu8340ForwEnergyActive_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,16),_Pdu8340ForwEnergyActive_Type())
pdu8340ForwEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340ForwEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:pdu8340ForwEnergyActive.setUnits(_F)
_Pdu8340ForwEnergyReactive_Type=Unsigned32
_Pdu8340ForwEnergyReactive_Object=MibTableColumn
pdu8340ForwEnergyReactive=_Pdu8340ForwEnergyReactive_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,17),_Pdu8340ForwEnergyReactive_Type())
pdu8340ForwEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340ForwEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:pdu8340ForwEnergyReactive.setUnits(_G)
_Pdu8340ForwEnergyActiveResettable_Type=Unsigned32
_Pdu8340ForwEnergyActiveResettable_Object=MibTableColumn
pdu8340ForwEnergyActiveResettable=_Pdu8340ForwEnergyActiveResettable_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,18),_Pdu8340ForwEnergyActiveResettable_Type())
pdu8340ForwEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340ForwEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu8340ForwEnergyActiveResettable.setUnits(_F)
_Pdu8340ForwEnergyReactiveResettable_Type=Unsigned32
_Pdu8340ForwEnergyReactiveResettable_Object=MibTableColumn
pdu8340ForwEnergyReactiveResettable=_Pdu8340ForwEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,19),_Pdu8340ForwEnergyReactiveResettable_Type())
pdu8340ForwEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340ForwEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu8340ForwEnergyReactiveResettable.setUnits(_G)
_Pdu8340RevEnergyActive_Type=Unsigned32
_Pdu8340RevEnergyActive_Object=MibTableColumn
pdu8340RevEnergyActive=_Pdu8340RevEnergyActive_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,20),_Pdu8340RevEnergyActive_Type())
pdu8340RevEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340RevEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:pdu8340RevEnergyActive.setUnits(_F)
_Pdu8340RevEnergyReactive_Type=Unsigned32
_Pdu8340RevEnergyReactive_Object=MibTableColumn
pdu8340RevEnergyReactive=_Pdu8340RevEnergyReactive_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,21),_Pdu8340RevEnergyReactive_Type())
pdu8340RevEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340RevEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:pdu8340RevEnergyReactive.setUnits(_G)
_Pdu8340RevEnergyActiveResettable_Type=Unsigned32
_Pdu8340RevEnergyActiveResettable_Object=MibTableColumn
pdu8340RevEnergyActiveResettable=_Pdu8340RevEnergyActiveResettable_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,22),_Pdu8340RevEnergyActiveResettable_Type())
pdu8340RevEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340RevEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu8340RevEnergyActiveResettable.setUnits(_F)
_Pdu8340RevEnergyReactiveResettable_Type=Unsigned32
_Pdu8340RevEnergyReactiveResettable_Object=MibTableColumn
pdu8340RevEnergyReactiveResettable=_Pdu8340RevEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,23),_Pdu8340RevEnergyReactiveResettable_Type())
pdu8340RevEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340RevEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu8340RevEnergyReactiveResettable.setUnits(_G)
_Pdu8340ResidualCurrent_Type=Unsigned32
_Pdu8340ResidualCurrent_Object=MibTableColumn
pdu8340ResidualCurrent=_Pdu8340ResidualCurrent_Object((1,3,6,1,4,1,28507,54,1,5,1,2,1,24),_Pdu8340ResidualCurrent_Type())
pdu8340ResidualCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340ResidualCurrent.setStatus(_B)
if mibBuilder.loadTexts:pdu8340ResidualCurrent.setUnits('mA')
_Pdu8340ExtSensors_ObjectIdentity=ObjectIdentity
pdu8340ExtSensors=_Pdu8340ExtSensors_ObjectIdentity((1,3,6,1,4,1,28507,54,1,6))
_Pdu8340SensorTable_Object=MibTable
pdu8340SensorTable=_Pdu8340SensorTable_Object((1,3,6,1,4,1,28507,54,1,6,1))
if mibBuilder.loadTexts:pdu8340SensorTable.setStatus(_B)
_Pdu8340SensorEntry_Object=MibTableRow
pdu8340SensorEntry=_Pdu8340SensorEntry_Object((1,3,6,1,4,1,28507,54,1,6,1,1))
pdu8340SensorEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:pdu8340SensorEntry.setStatus(_B)
class _Pdu8340SensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Pdu8340SensorIndex_Type.__name__=_D
_Pdu8340SensorIndex_Object=MibTableColumn
pdu8340SensorIndex=_Pdu8340SensorIndex_Object((1,3,6,1,4,1,28507,54,1,6,1,1,1),_Pdu8340SensorIndex_Type())
pdu8340SensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340SensorIndex.setStatus(_B)
_Pdu8340TempSensor_Type=Integer32
_Pdu8340TempSensor_Object=MibTableColumn
pdu8340TempSensor=_Pdu8340TempSensor_Object((1,3,6,1,4,1,28507,54,1,6,1,1,2),_Pdu8340TempSensor_Type())
pdu8340TempSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340TempSensor.setStatus(_B)
if mibBuilder.loadTexts:pdu8340TempSensor.setUnits(_K)
_Pdu8340HygroSensor_Type=Integer32
_Pdu8340HygroSensor_Object=MibTableColumn
pdu8340HygroSensor=_Pdu8340HygroSensor_Object((1,3,6,1,4,1,28507,54,1,6,1,1,3),_Pdu8340HygroSensor_Type())
pdu8340HygroSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340HygroSensor.setStatus(_B)
if mibBuilder.loadTexts:pdu8340HygroSensor.setUnits('0.1 percent humidity')
class _Pdu8340InputSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_Pdu8340InputSensor_Type.__name__=_D
_Pdu8340InputSensor_Object=MibTableColumn
pdu8340InputSensor=_Pdu8340InputSensor_Object((1,3,6,1,4,1,28507,54,1,6,1,1,4),_Pdu8340InputSensor_Type())
pdu8340InputSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340InputSensor.setStatus(_B)
_Pdu8340AirPressure_Type=Integer32
_Pdu8340AirPressure_Object=MibTableColumn
pdu8340AirPressure=_Pdu8340AirPressure_Object((1,3,6,1,4,1,28507,54,1,6,1,1,5),_Pdu8340AirPressure_Type())
pdu8340AirPressure.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340AirPressure.setStatus(_B)
if mibBuilder.loadTexts:pdu8340AirPressure.setUnits('1 hPA (hectopascal) ~ 1 milibar')
_Pdu8340DewPoint_Type=Integer32
_Pdu8340DewPoint_Object=MibTableColumn
pdu8340DewPoint=_Pdu8340DewPoint_Object((1,3,6,1,4,1,28507,54,1,6,1,1,6),_Pdu8340DewPoint_Type())
pdu8340DewPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340DewPoint.setStatus(_B)
if mibBuilder.loadTexts:pdu8340DewPoint.setUnits(_K)
_Pdu8340DewPointDiff_Type=Integer32
_Pdu8340DewPointDiff_Object=MibTableColumn
pdu8340DewPointDiff=_Pdu8340DewPointDiff_Object((1,3,6,1,4,1,28507,54,1,6,1,1,7),_Pdu8340DewPointDiff_Type())
pdu8340DewPointDiff.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu8340DewPointDiff.setStatus(_B)
if mibBuilder.loadTexts:pdu8340DewPointDiff.setUnits(_K)
_Pdu8340Conf_ObjectIdentity=ObjectIdentity
pdu8340Conf=_Pdu8340Conf_ObjectIdentity((1,3,6,1,4,1,28507,54,2))
_Pdu8340Groups_ObjectIdentity=ObjectIdentity
pdu8340Groups=_Pdu8340Groups_ObjectIdentity((1,3,6,1,4,1,28507,54,2,1))
_Pdu8340Compls_ObjectIdentity=ObjectIdentity
pdu8340Compls=_Pdu8340Compls_ObjectIdentity((1,3,6,1,4,1,28507,54,2,2))
_Events_ObjectIdentity=ObjectIdentity
events=_Events_ObjectIdentity((1,3,6,1,4,1,28507,54,3))
pdu8340BasicGroup=ObjectGroup((1,3,6,1,4,1,28507,54,2,1,1))
pdu8340BasicGroup.setObjects(*((_A,_Y),(_A,_J),(_A,_Z),(_A,_a),(_A,_b),(_A,_I),(_A,_c),(_A,_d),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_e),(_A,_f),(_A,_P),(_A,_Q),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_E),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_t),(_A,_V)))
if mibBuilder.loadTexts:pdu8340BasicGroup.setStatus(_B)
pdu8340TempEvtSen=NotificationType((1,3,6,1,4,1,28507,54,3,1))
pdu8340TempEvtSen.setObjects(*((_A,_E),(_A,_R)))
if mibBuilder.loadTexts:pdu8340TempEvtSen.setStatus(_B)
pdu8340HygroEvtSen=NotificationType((1,3,6,1,4,1,28507,54,3,2))
pdu8340HygroEvtSen.setObjects(*((_A,_E),(_A,_S)))
if mibBuilder.loadTexts:pdu8340HygroEvtSen.setStatus(_B)
pdu8340InputEvtSen=NotificationType((1,3,6,1,4,1,28507,54,3,3))
pdu8340InputEvtSen.setObjects(*((_A,_E),(_A,_T)))
if mibBuilder.loadTexts:pdu8340InputEvtSen.setStatus(_B)
pdu8340AirPressureEvtSen=NotificationType((1,3,6,1,4,1,28507,54,3,4))
pdu8340AirPressureEvtSen.setObjects(*((_A,_E),(_A,_U)))
if mibBuilder.loadTexts:pdu8340AirPressureEvtSen.setStatus(_B)
pdu8340DewPtDiffEvtSen=NotificationType((1,3,6,1,4,1,28507,54,3,5))
pdu8340DewPtDiffEvtSen.setObjects(*((_A,_E),(_A,_V)))
if mibBuilder.loadTexts:pdu8340DewPtDiffEvtSen.setStatus(_B)
pdu8340LineAmperageEvt=NotificationType((1,3,6,1,4,1,28507,54,3,6))
pdu8340LineAmperageEvt.setObjects(*((_A,_I),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:pdu8340LineAmperageEvt.setStatus(_B)
pdu8340NotificationGroup=NotificationGroup((1,3,6,1,4,1,28507,54,2,1,2))
pdu8340NotificationGroup.setObjects(*((_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:pdu8340NotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'gudeads':gudeads,'gadsPDU8340':gadsPDU8340,'pdu8340Objects':pdu8340Objects,'pdu8340CommonConfig':pdu8340CommonConfig,'pdu8340SNMPaccess':pdu8340SNMPaccess,_Y:pdu8340TrapCtrl,'pdu8340TrapIPTable':pdu8340TrapIPTable,'pdu8340TrapIPEntry':pdu8340TrapIPEntry,_J:pdu8340TrapIPIndex,_Z:pdu8340TrapAddr,'pdu8340DeviceConfig':pdu8340DeviceConfig,'pdu8340IntActors':pdu8340IntActors,_a:pdu8340Buzzer,'pdu8340ExtActors':pdu8340ExtActors,'pdu8340IntSensors':pdu8340IntSensors,'pdu8340PowerChan':pdu8340PowerChan,_b:pdu8340ActivePowerChan,'pdu8340PowerTable':pdu8340PowerTable,'pdu8340PowerEntry':pdu8340PowerEntry,_I:pdu8340PowerIndex,_c:pdu8340ChanStatus,_d:pdu8340AbsEnergyActive,_L:pdu8340PowerActive,_M:pdu8340Current,_N:pdu8340Voltage,_O:pdu8340Frequency,_e:pdu8340PowerFactor,_f:pdu8340Pangle,_P:pdu8340PowerApparent,_Q:pdu8340PowerReactive,_g:pdu8340AbsEnergyReactive,_h:pdu8340AbsEnergyActiveResettable,_i:pdu8340AbsEnergyReactiveResettable,_j:pdu8340ResetTime,_k:pdu8340ForwEnergyActive,_l:pdu8340ForwEnergyReactive,_m:pdu8340ForwEnergyActiveResettable,_n:pdu8340ForwEnergyReactiveResettable,_o:pdu8340RevEnergyActive,_p:pdu8340RevEnergyReactive,_q:pdu8340RevEnergyActiveResettable,_r:pdu8340RevEnergyReactiveResettable,_s:pdu8340ResidualCurrent,'pdu8340ExtSensors':pdu8340ExtSensors,'pdu8340SensorTable':pdu8340SensorTable,'pdu8340SensorEntry':pdu8340SensorEntry,_E:pdu8340SensorIndex,_R:pdu8340TempSensor,_S:pdu8340HygroSensor,_T:pdu8340InputSensor,_U:pdu8340AirPressure,_t:pdu8340DewPoint,_V:pdu8340DewPointDiff,'pdu8340Conf':pdu8340Conf,'pdu8340Groups':pdu8340Groups,'pdu8340BasicGroup':pdu8340BasicGroup,'pdu8340NotificationGroup':pdu8340NotificationGroup,'pdu8340Compls':pdu8340Compls,'events':events,_u:pdu8340TempEvtSen,_v:pdu8340HygroEvtSen,_w:pdu8340InputEvtSen,_x:pdu8340AirPressureEvtSen,_y:pdu8340DewPtDiffEvtSen,_z:pdu8340LineAmperageEvt})