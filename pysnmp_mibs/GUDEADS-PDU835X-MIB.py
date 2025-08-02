_A8='pdu835XMeasurementBoxEvt2'
_A7='pdu835XMeasurementBoxEvt1'
_A6='pdu835XAmperageEvt6'
_A5='pdu835XAmperageEvt5'
_A4='pdu835XAmperageEvt4'
_A3='pdu835XAmperageEvt3'
_A2='pdu835XAmperageEvt2'
_A1='pdu835XAmperageEvt1'
_A0='pdu835XInputEvtSen2'
_z='pdu835XInputEvtSen1'
_y='pdu835XHygroEvtSen2'
_x='pdu835XHygroEvtSen1'
_w='pdu835XTempEvtSen2'
_v='pdu835XTempEvtSen1'
_u='pdu835XActivePowerGroups'
_t='pdu835XRCurrent3P'
_s='pdu835XNCurrent3P'
_r='pdu835XBuzzer'
_q='pdu835XRevEnergyReactiveResettable'
_p='pdu835XRevEnergyActiveResettable'
_o='pdu835XRevEnergyReactive'
_n='pdu835XRevEnergyActive'
_m='pdu835XForwEnergyReactiveResettable'
_l='pdu835XForwEnergyActiveResettable'
_k='pdu835XForwEnergyReactive'
_j='pdu835XForwEnergyActive'
_i='pdu835XResetTime'
_h='pdu835XAbsEnergyReactiveResettable'
_g='pdu835XAbsEnergyActiveResettable'
_f='pdu835XAbsEnergyReactive'
_e='pdu835XPangle'
_d='pdu835XPowerFactor'
_c='pdu835XAbsEnergyActive'
_b='pdu835XChanStatus'
_a='pdu835XActivePowerChan'
_Z='pdu835XTrapAddr'
_Y='pdu835XTrapCtrl'
_X='pdu835XSensorIndex'
_W='pdu835XPowerGroupIndex'
_V='pdu835XPowerIndex'
_U='pdu835XTrapIPIndex'
_T='OctetString'
_S='pdu835XMeasurementBoxConnected'
_R='read-write'
_Q='Unsigned32'
_P='pdu835XInputSensor'
_O='pdu835XHygroSensor'
_N='pdu835XTempSensor'
_M='not-accessible'
_L='VARh'
_K='Wh'
_J='pdu835XPowerReactive'
_I='pdu835XPowerApparent'
_H='pdu835XFrequency'
_G='pdu835XVoltage'
_F='pdu835XCurrent'
_E='pdu835XPowerActive'
_D='Integer32'
_C='read-only'
_B='current'
_A='GUDEADS-PDU835X-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_T,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Q,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-03-05 13:56',))
_GadsPDU835X_ObjectIdentity=ObjectIdentity
gadsPDU835X=_GadsPDU835X_ObjectIdentity((1,3,6,1,4,1,28507,52))
_Events_ObjectIdentity=ObjectIdentity
events=_Events_ObjectIdentity((1,3,6,1,4,1,28507,52,0))
_Pdu835XObjects_ObjectIdentity=ObjectIdentity
pdu835XObjects=_Pdu835XObjects_ObjectIdentity((1,3,6,1,4,1,28507,52,1))
_Pdu835XCommonConfig_ObjectIdentity=ObjectIdentity
pdu835XCommonConfig=_Pdu835XCommonConfig_ObjectIdentity((1,3,6,1,4,1,28507,52,1,1))
_Pdu835XSNMPaccess_ObjectIdentity=ObjectIdentity
pdu835XSNMPaccess=_Pdu835XSNMPaccess_ObjectIdentity((1,3,6,1,4,1,28507,52,1,1,1))
class _Pdu835XTrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Pdu835XTrapCtrl_Type.__name__=_D
_Pdu835XTrapCtrl_Object=MibScalar
pdu835XTrapCtrl=_Pdu835XTrapCtrl_Object((1,3,6,1,4,1,28507,52,1,1,1,1),_Pdu835XTrapCtrl_Type())
pdu835XTrapCtrl.setMaxAccess(_R)
if mibBuilder.loadTexts:pdu835XTrapCtrl.setStatus(_B)
_Pdu835XTrapIPTable_Object=MibTable
pdu835XTrapIPTable=_Pdu835XTrapIPTable_Object((1,3,6,1,4,1,28507,52,1,1,1,2))
if mibBuilder.loadTexts:pdu835XTrapIPTable.setStatus(_B)
_Pdu835XTrapIPEntry_Object=MibTableRow
pdu835XTrapIPEntry=_Pdu835XTrapIPEntry_Object((1,3,6,1,4,1,28507,52,1,1,1,2,1))
pdu835XTrapIPEntry.setIndexNames((0,_A,_U))
if mibBuilder.loadTexts:pdu835XTrapIPEntry.setStatus(_B)
class _Pdu835XTrapIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Pdu835XTrapIPIndex_Type.__name__=_D
_Pdu835XTrapIPIndex_Object=MibTableColumn
pdu835XTrapIPIndex=_Pdu835XTrapIPIndex_Object((1,3,6,1,4,1,28507,52,1,1,1,2,1,1),_Pdu835XTrapIPIndex_Type())
pdu835XTrapIPIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:pdu835XTrapIPIndex.setStatus(_B)
class _Pdu835XTrapAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Pdu835XTrapAddr_Type.__name__=_T
_Pdu835XTrapAddr_Object=MibTableColumn
pdu835XTrapAddr=_Pdu835XTrapAddr_Object((1,3,6,1,4,1,28507,52,1,1,1,2,1,2),_Pdu835XTrapAddr_Type())
pdu835XTrapAddr.setMaxAccess(_R)
if mibBuilder.loadTexts:pdu835XTrapAddr.setStatus(_B)
_Pdu835XDeviceConfig_ObjectIdentity=ObjectIdentity
pdu835XDeviceConfig=_Pdu835XDeviceConfig_ObjectIdentity((1,3,6,1,4,1,28507,52,1,2))
_Pdu835XIntActors_ObjectIdentity=ObjectIdentity
pdu835XIntActors=_Pdu835XIntActors_ObjectIdentity((1,3,6,1,4,1,28507,52,1,3))
class _Pdu835XBuzzer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Pdu835XBuzzer_Type.__name__=_D
_Pdu835XBuzzer_Object=MibScalar
pdu835XBuzzer=_Pdu835XBuzzer_Object((1,3,6,1,4,1,28507,52,1,3,10),_Pdu835XBuzzer_Type())
pdu835XBuzzer.setMaxAccess(_R)
if mibBuilder.loadTexts:pdu835XBuzzer.setStatus(_B)
if mibBuilder.loadTexts:pdu835XBuzzer.setUnits('0 = Off, 1 = On')
_Pdu835XExtActors_ObjectIdentity=ObjectIdentity
pdu835XExtActors=_Pdu835XExtActors_ObjectIdentity((1,3,6,1,4,1,28507,52,1,4))
_Pdu835XIntSensors_ObjectIdentity=ObjectIdentity
pdu835XIntSensors=_Pdu835XIntSensors_ObjectIdentity((1,3,6,1,4,1,28507,52,1,5))
_Pdu835XPowerChan_ObjectIdentity=ObjectIdentity
pdu835XPowerChan=_Pdu835XPowerChan_ObjectIdentity((1,3,6,1,4,1,28507,52,1,5,1))
class _Pdu835XActivePowerChan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_Pdu835XActivePowerChan_Type.__name__=_Q
_Pdu835XActivePowerChan_Object=MibScalar
pdu835XActivePowerChan=_Pdu835XActivePowerChan_Object((1,3,6,1,4,1,28507,52,1,5,1,1),_Pdu835XActivePowerChan_Type())
pdu835XActivePowerChan.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XActivePowerChan.setStatus(_B)
_Pdu835XPowerTable_Object=MibTable
pdu835XPowerTable=_Pdu835XPowerTable_Object((1,3,6,1,4,1,28507,52,1,5,1,2))
if mibBuilder.loadTexts:pdu835XPowerTable.setStatus(_B)
_Pdu835XPowerEntry_Object=MibTableRow
pdu835XPowerEntry=_Pdu835XPowerEntry_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1))
pdu835XPowerEntry.setIndexNames((0,_A,_V))
if mibBuilder.loadTexts:pdu835XPowerEntry.setStatus(_B)
class _Pdu835XPowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_Pdu835XPowerIndex_Type.__name__=_D
_Pdu835XPowerIndex_Object=MibTableColumn
pdu835XPowerIndex=_Pdu835XPowerIndex_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,1),_Pdu835XPowerIndex_Type())
pdu835XPowerIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:pdu835XPowerIndex.setStatus(_B)
class _Pdu835XChanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Pdu835XChanStatus_Type.__name__=_D
_Pdu835XChanStatus_Object=MibTableColumn
pdu835XChanStatus=_Pdu835XChanStatus_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,2),_Pdu835XChanStatus_Type())
pdu835XChanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XChanStatus.setStatus(_B)
_Pdu835XAbsEnergyActive_Type=Unsigned32
_Pdu835XAbsEnergyActive_Object=MibTableColumn
pdu835XAbsEnergyActive=_Pdu835XAbsEnergyActive_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,3),_Pdu835XAbsEnergyActive_Type())
pdu835XAbsEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XAbsEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:pdu835XAbsEnergyActive.setUnits(_K)
_Pdu835XPowerActive_Type=Integer32
_Pdu835XPowerActive_Object=MibTableColumn
pdu835XPowerActive=_Pdu835XPowerActive_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,4),_Pdu835XPowerActive_Type())
pdu835XPowerActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XPowerActive.setStatus(_B)
if mibBuilder.loadTexts:pdu835XPowerActive.setUnits('W')
_Pdu835XCurrent_Type=Unsigned32
_Pdu835XCurrent_Object=MibTableColumn
pdu835XCurrent=_Pdu835XCurrent_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,5),_Pdu835XCurrent_Type())
pdu835XCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XCurrent.setStatus(_B)
if mibBuilder.loadTexts:pdu835XCurrent.setUnits('mA')
_Pdu835XVoltage_Type=Unsigned32
_Pdu835XVoltage_Object=MibTableColumn
pdu835XVoltage=_Pdu835XVoltage_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,6),_Pdu835XVoltage_Type())
pdu835XVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XVoltage.setStatus(_B)
if mibBuilder.loadTexts:pdu835XVoltage.setUnits('V')
_Pdu835XFrequency_Type=Unsigned32
_Pdu835XFrequency_Object=MibTableColumn
pdu835XFrequency=_Pdu835XFrequency_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,7),_Pdu835XFrequency_Type())
pdu835XFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XFrequency.setStatus(_B)
if mibBuilder.loadTexts:pdu835XFrequency.setUnits('0.01 hz')
_Pdu835XPowerFactor_Type=Integer32
_Pdu835XPowerFactor_Object=MibTableColumn
pdu835XPowerFactor=_Pdu835XPowerFactor_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,8),_Pdu835XPowerFactor_Type())
pdu835XPowerFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XPowerFactor.setStatus(_B)
if mibBuilder.loadTexts:pdu835XPowerFactor.setUnits('0.001')
_Pdu835XPangle_Type=Integer32
_Pdu835XPangle_Object=MibTableColumn
pdu835XPangle=_Pdu835XPangle_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,9),_Pdu835XPangle_Type())
pdu835XPangle.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XPangle.setStatus(_B)
if mibBuilder.loadTexts:pdu835XPangle.setUnits('0.1 degree')
_Pdu835XPowerApparent_Type=Integer32
_Pdu835XPowerApparent_Object=MibTableColumn
pdu835XPowerApparent=_Pdu835XPowerApparent_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,10),_Pdu835XPowerApparent_Type())
pdu835XPowerApparent.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XPowerApparent.setStatus(_B)
if mibBuilder.loadTexts:pdu835XPowerApparent.setUnits('VA')
_Pdu835XPowerReactive_Type=Integer32
_Pdu835XPowerReactive_Object=MibTableColumn
pdu835XPowerReactive=_Pdu835XPowerReactive_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,11),_Pdu835XPowerReactive_Type())
pdu835XPowerReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XPowerReactive.setStatus(_B)
if mibBuilder.loadTexts:pdu835XPowerReactive.setUnits('VAR')
_Pdu835XAbsEnergyReactive_Type=Unsigned32
_Pdu835XAbsEnergyReactive_Object=MibTableColumn
pdu835XAbsEnergyReactive=_Pdu835XAbsEnergyReactive_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,12),_Pdu835XAbsEnergyReactive_Type())
pdu835XAbsEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XAbsEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:pdu835XAbsEnergyReactive.setUnits(_L)
_Pdu835XAbsEnergyActiveResettable_Type=Unsigned32
_Pdu835XAbsEnergyActiveResettable_Object=MibTableColumn
pdu835XAbsEnergyActiveResettable=_Pdu835XAbsEnergyActiveResettable_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,13),_Pdu835XAbsEnergyActiveResettable_Type())
pdu835XAbsEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XAbsEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu835XAbsEnergyActiveResettable.setUnits(_K)
_Pdu835XAbsEnergyReactiveResettable_Type=Unsigned32
_Pdu835XAbsEnergyReactiveResettable_Object=MibTableColumn
pdu835XAbsEnergyReactiveResettable=_Pdu835XAbsEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,14),_Pdu835XAbsEnergyReactiveResettable_Type())
pdu835XAbsEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XAbsEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu835XAbsEnergyReactiveResettable.setUnits(_L)
_Pdu835XResetTime_Type=Unsigned32
_Pdu835XResetTime_Object=MibTableColumn
pdu835XResetTime=_Pdu835XResetTime_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,15),_Pdu835XResetTime_Type())
pdu835XResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XResetTime.setStatus(_B)
if mibBuilder.loadTexts:pdu835XResetTime.setUnits('s')
_Pdu835XForwEnergyActive_Type=Unsigned32
_Pdu835XForwEnergyActive_Object=MibTableColumn
pdu835XForwEnergyActive=_Pdu835XForwEnergyActive_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,16),_Pdu835XForwEnergyActive_Type())
pdu835XForwEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XForwEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:pdu835XForwEnergyActive.setUnits(_K)
_Pdu835XForwEnergyReactive_Type=Unsigned32
_Pdu835XForwEnergyReactive_Object=MibTableColumn
pdu835XForwEnergyReactive=_Pdu835XForwEnergyReactive_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,17),_Pdu835XForwEnergyReactive_Type())
pdu835XForwEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XForwEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:pdu835XForwEnergyReactive.setUnits(_L)
_Pdu835XForwEnergyActiveResettable_Type=Unsigned32
_Pdu835XForwEnergyActiveResettable_Object=MibTableColumn
pdu835XForwEnergyActiveResettable=_Pdu835XForwEnergyActiveResettable_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,18),_Pdu835XForwEnergyActiveResettable_Type())
pdu835XForwEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XForwEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu835XForwEnergyActiveResettable.setUnits(_K)
_Pdu835XForwEnergyReactiveResettable_Type=Unsigned32
_Pdu835XForwEnergyReactiveResettable_Object=MibTableColumn
pdu835XForwEnergyReactiveResettable=_Pdu835XForwEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,19),_Pdu835XForwEnergyReactiveResettable_Type())
pdu835XForwEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XForwEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu835XForwEnergyReactiveResettable.setUnits(_L)
_Pdu835XRevEnergyActive_Type=Unsigned32
_Pdu835XRevEnergyActive_Object=MibTableColumn
pdu835XRevEnergyActive=_Pdu835XRevEnergyActive_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,20),_Pdu835XRevEnergyActive_Type())
pdu835XRevEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XRevEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:pdu835XRevEnergyActive.setUnits(_K)
_Pdu835XRevEnergyReactive_Type=Unsigned32
_Pdu835XRevEnergyReactive_Object=MibTableColumn
pdu835XRevEnergyReactive=_Pdu835XRevEnergyReactive_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,21),_Pdu835XRevEnergyReactive_Type())
pdu835XRevEnergyReactive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XRevEnergyReactive.setStatus(_B)
if mibBuilder.loadTexts:pdu835XRevEnergyReactive.setUnits(_L)
_Pdu835XRevEnergyActiveResettable_Type=Unsigned32
_Pdu835XRevEnergyActiveResettable_Object=MibTableColumn
pdu835XRevEnergyActiveResettable=_Pdu835XRevEnergyActiveResettable_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,22),_Pdu835XRevEnergyActiveResettable_Type())
pdu835XRevEnergyActiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XRevEnergyActiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu835XRevEnergyActiveResettable.setUnits(_K)
_Pdu835XRevEnergyReactiveResettable_Type=Unsigned32
_Pdu835XRevEnergyReactiveResettable_Object=MibTableColumn
pdu835XRevEnergyReactiveResettable=_Pdu835XRevEnergyReactiveResettable_Object((1,3,6,1,4,1,28507,52,1,5,1,2,1,23),_Pdu835XRevEnergyReactiveResettable_Type())
pdu835XRevEnergyReactiveResettable.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XRevEnergyReactiveResettable.setStatus(_B)
if mibBuilder.loadTexts:pdu835XRevEnergyReactiveResettable.setUnits(_L)
_Pdu835XPowerGroup_ObjectIdentity=ObjectIdentity
pdu835XPowerGroup=_Pdu835XPowerGroup_ObjectIdentity((1,3,6,1,4,1,28507,52,1,5,3))
class _Pdu835XActivePowerGroups_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Pdu835XActivePowerGroups_Type.__name__=_Q
_Pdu835XActivePowerGroups_Object=MibScalar
pdu835XActivePowerGroups=_Pdu835XActivePowerGroups_Object((1,3,6,1,4,1,28507,52,1,5,3,1),_Pdu835XActivePowerGroups_Type())
pdu835XActivePowerGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XActivePowerGroups.setStatus(_B)
_Pdu835XPowerGroupTable_Object=MibTable
pdu835XPowerGroupTable=_Pdu835XPowerGroupTable_Object((1,3,6,1,4,1,28507,52,1,5,3,2))
if mibBuilder.loadTexts:pdu835XPowerGroupTable.setStatus(_B)
_Pdu835XEntry_Object=MibTableRow
pdu835XEntry=_Pdu835XEntry_Object((1,3,6,1,4,1,28507,52,1,5,3,2,1))
pdu835XEntry.setIndexNames((0,_A,_W))
if mibBuilder.loadTexts:pdu835XEntry.setStatus(_B)
class _Pdu835XPowerGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Pdu835XPowerGroupIndex_Type.__name__=_D
_Pdu835XPowerGroupIndex_Object=MibTableColumn
pdu835XPowerGroupIndex=_Pdu835XPowerGroupIndex_Object((1,3,6,1,4,1,28507,52,1,5,3,2,1,1),_Pdu835XPowerGroupIndex_Type())
pdu835XPowerGroupIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:pdu835XPowerGroupIndex.setStatus(_B)
_Pdu835XRCurrent3P_Type=Unsigned32
_Pdu835XRCurrent3P_Object=MibTableColumn
pdu835XRCurrent3P=_Pdu835XRCurrent3P_Object((1,3,6,1,4,1,28507,52,1,5,3,2,1,2),_Pdu835XRCurrent3P_Type())
pdu835XRCurrent3P.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XRCurrent3P.setStatus(_B)
if mibBuilder.loadTexts:pdu835XRCurrent3P.setUnits('mA')
_Pdu835XNCurrent3P_Type=Unsigned32
_Pdu835XNCurrent3P_Object=MibTableColumn
pdu835XNCurrent3P=_Pdu835XNCurrent3P_Object((1,3,6,1,4,1,28507,52,1,5,3,2,1,3),_Pdu835XNCurrent3P_Type())
pdu835XNCurrent3P.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XNCurrent3P.setStatus(_B)
if mibBuilder.loadTexts:pdu835XNCurrent3P.setUnits('mA')
class _Pdu835XMeasurementBoxConnected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disconnected',0),('connected',1)))
_Pdu835XMeasurementBoxConnected_Type.__name__=_D
_Pdu835XMeasurementBoxConnected_Object=MibTableColumn
pdu835XMeasurementBoxConnected=_Pdu835XMeasurementBoxConnected_Object((1,3,6,1,4,1,28507,52,1,5,3,2,1,4),_Pdu835XMeasurementBoxConnected_Type())
pdu835XMeasurementBoxConnected.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XMeasurementBoxConnected.setStatus(_B)
_Pdu835XExtSensors_ObjectIdentity=ObjectIdentity
pdu835XExtSensors=_Pdu835XExtSensors_ObjectIdentity((1,3,6,1,4,1,28507,52,1,6))
_Pdu835XSensorTable_Object=MibTable
pdu835XSensorTable=_Pdu835XSensorTable_Object((1,3,6,1,4,1,28507,52,1,6,1))
if mibBuilder.loadTexts:pdu835XSensorTable.setStatus(_B)
_Pdu835XSensorEntry_Object=MibTableRow
pdu835XSensorEntry=_Pdu835XSensorEntry_Object((1,3,6,1,4,1,28507,52,1,6,1,1))
pdu835XSensorEntry.setIndexNames((0,_A,_X))
if mibBuilder.loadTexts:pdu835XSensorEntry.setStatus(_B)
class _Pdu835XSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Pdu835XSensorIndex_Type.__name__=_D
_Pdu835XSensorIndex_Object=MibTableColumn
pdu835XSensorIndex=_Pdu835XSensorIndex_Object((1,3,6,1,4,1,28507,52,1,6,1,1,1),_Pdu835XSensorIndex_Type())
pdu835XSensorIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:pdu835XSensorIndex.setStatus(_B)
_Pdu835XTempSensor_Type=Integer32
_Pdu835XTempSensor_Object=MibTableColumn
pdu835XTempSensor=_Pdu835XTempSensor_Object((1,3,6,1,4,1,28507,52,1,6,1,1,2),_Pdu835XTempSensor_Type())
pdu835XTempSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XTempSensor.setStatus(_B)
if mibBuilder.loadTexts:pdu835XTempSensor.setUnits('0.1 degree Celsius')
_Pdu835XHygroSensor_Type=Integer32
_Pdu835XHygroSensor_Object=MibTableColumn
pdu835XHygroSensor=_Pdu835XHygroSensor_Object((1,3,6,1,4,1,28507,52,1,6,1,1,3),_Pdu835XHygroSensor_Type())
pdu835XHygroSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XHygroSensor.setStatus(_B)
if mibBuilder.loadTexts:pdu835XHygroSensor.setUnits('0.1 percent humidity')
class _Pdu835XInputSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_Pdu835XInputSensor_Type.__name__=_D
_Pdu835XInputSensor_Object=MibTableColumn
pdu835XInputSensor=_Pdu835XInputSensor_Object((1,3,6,1,4,1,28507,52,1,6,1,1,4),_Pdu835XInputSensor_Type())
pdu835XInputSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu835XInputSensor.setStatus(_B)
_Pdu835XConf_ObjectIdentity=ObjectIdentity
pdu835XConf=_Pdu835XConf_ObjectIdentity((1,3,6,1,4,1,28507,52,2))
_Pdu835XGroups_ObjectIdentity=ObjectIdentity
pdu835XGroups=_Pdu835XGroups_ObjectIdentity((1,3,6,1,4,1,28507,52,2,1))
_Pdu835XCompls_ObjectIdentity=ObjectIdentity
pdu835XCompls=_Pdu835XCompls_ObjectIdentity((1,3,6,1,4,1,28507,52,2,2))
pdu835XBasicGroup=ObjectGroup((1,3,6,1,4,1,28507,52,2,1,1))
pdu835XBasicGroup.setObjects(*((_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_d),(_A,_e),(_A,_I),(_A,_J),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_N),(_A,_O),(_A,_P),(_A,_r),(_A,_s),(_A,_t),(_A,_S),(_A,_u)))
if mibBuilder.loadTexts:pdu835XBasicGroup.setStatus(_B)
pdu835XTempEvtSen1=NotificationType((1,3,6,1,4,1,28507,52,0,1))
pdu835XTempEvtSen1.setObjects((_A,_N))
if mibBuilder.loadTexts:pdu835XTempEvtSen1.setStatus(_B)
pdu835XTempEvtSen2=NotificationType((1,3,6,1,4,1,28507,52,0,2))
pdu835XTempEvtSen2.setObjects((_A,_N))
if mibBuilder.loadTexts:pdu835XTempEvtSen2.setStatus(_B)
pdu835XHygroEvtSen1=NotificationType((1,3,6,1,4,1,28507,52,0,3))
pdu835XHygroEvtSen1.setObjects((_A,_O))
if mibBuilder.loadTexts:pdu835XHygroEvtSen1.setStatus(_B)
pdu835XHygroEvtSen2=NotificationType((1,3,6,1,4,1,28507,52,0,4))
pdu835XHygroEvtSen2.setObjects((_A,_O))
if mibBuilder.loadTexts:pdu835XHygroEvtSen2.setStatus(_B)
pdu835XInputEvtSen1=NotificationType((1,3,6,1,4,1,28507,52,0,5))
pdu835XInputEvtSen1.setObjects((_A,_P))
if mibBuilder.loadTexts:pdu835XInputEvtSen1.setStatus(_B)
pdu835XInputEvtSen2=NotificationType((1,3,6,1,4,1,28507,52,0,6))
pdu835XInputEvtSen2.setObjects((_A,_P))
if mibBuilder.loadTexts:pdu835XInputEvtSen2.setStatus(_B)
pdu835XMeasurementBoxEvt1=NotificationType((1,3,6,1,4,1,28507,52,0,7))
pdu835XMeasurementBoxEvt1.setObjects((_A,_S))
if mibBuilder.loadTexts:pdu835XMeasurementBoxEvt1.setStatus(_B)
pdu835XMeasurementBoxEvt2=NotificationType((1,3,6,1,4,1,28507,52,0,8))
if mibBuilder.loadTexts:pdu835XMeasurementBoxEvt2.setStatus(_B)
pdu835XAmperageEvt1=NotificationType((1,3,6,1,4,1,28507,52,0,9))
pdu835XAmperageEvt1.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:pdu835XAmperageEvt1.setStatus(_B)
pdu835XAmperageEvt2=NotificationType((1,3,6,1,4,1,28507,52,0,10))
pdu835XAmperageEvt2.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:pdu835XAmperageEvt2.setStatus(_B)
pdu835XAmperageEvt3=NotificationType((1,3,6,1,4,1,28507,52,0,11))
pdu835XAmperageEvt3.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:pdu835XAmperageEvt3.setStatus(_B)
pdu835XAmperageEvt4=NotificationType((1,3,6,1,4,1,28507,52,0,12))
pdu835XAmperageEvt4.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:pdu835XAmperageEvt4.setStatus(_B)
pdu835XAmperageEvt5=NotificationType((1,3,6,1,4,1,28507,52,0,13))
pdu835XAmperageEvt5.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:pdu835XAmperageEvt5.setStatus(_B)
pdu835XAmperageEvt6=NotificationType((1,3,6,1,4,1,28507,52,0,14))
pdu835XAmperageEvt6.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:pdu835XAmperageEvt6.setStatus(_B)
pdu835XNotificationGroup=NotificationGroup((1,3,6,1,4,1,28507,52,2,1,2))
pdu835XNotificationGroup.setObjects(*((_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:pdu835XNotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'gudeads':gudeads,'gadsPDU835X':gadsPDU835X,'events':events,_v:pdu835XTempEvtSen1,_w:pdu835XTempEvtSen2,_x:pdu835XHygroEvtSen1,_y:pdu835XHygroEvtSen2,_z:pdu835XInputEvtSen1,_A0:pdu835XInputEvtSen2,_A7:pdu835XMeasurementBoxEvt1,_A8:pdu835XMeasurementBoxEvt2,_A1:pdu835XAmperageEvt1,_A2:pdu835XAmperageEvt2,_A3:pdu835XAmperageEvt3,_A4:pdu835XAmperageEvt4,_A5:pdu835XAmperageEvt5,_A6:pdu835XAmperageEvt6,'pdu835XObjects':pdu835XObjects,'pdu835XCommonConfig':pdu835XCommonConfig,'pdu835XSNMPaccess':pdu835XSNMPaccess,_Y:pdu835XTrapCtrl,'pdu835XTrapIPTable':pdu835XTrapIPTable,'pdu835XTrapIPEntry':pdu835XTrapIPEntry,_U:pdu835XTrapIPIndex,_Z:pdu835XTrapAddr,'pdu835XDeviceConfig':pdu835XDeviceConfig,'pdu835XIntActors':pdu835XIntActors,_r:pdu835XBuzzer,'pdu835XExtActors':pdu835XExtActors,'pdu835XIntSensors':pdu835XIntSensors,'pdu835XPowerChan':pdu835XPowerChan,_a:pdu835XActivePowerChan,'pdu835XPowerTable':pdu835XPowerTable,'pdu835XPowerEntry':pdu835XPowerEntry,_V:pdu835XPowerIndex,_b:pdu835XChanStatus,_c:pdu835XAbsEnergyActive,_E:pdu835XPowerActive,_F:pdu835XCurrent,_G:pdu835XVoltage,_H:pdu835XFrequency,_d:pdu835XPowerFactor,_e:pdu835XPangle,_I:pdu835XPowerApparent,_J:pdu835XPowerReactive,_f:pdu835XAbsEnergyReactive,_g:pdu835XAbsEnergyActiveResettable,_h:pdu835XAbsEnergyReactiveResettable,_i:pdu835XResetTime,_j:pdu835XForwEnergyActive,_k:pdu835XForwEnergyReactive,_l:pdu835XForwEnergyActiveResettable,_m:pdu835XForwEnergyReactiveResettable,_n:pdu835XRevEnergyActive,_o:pdu835XRevEnergyReactive,_p:pdu835XRevEnergyActiveResettable,_q:pdu835XRevEnergyReactiveResettable,'pdu835XPowerGroup':pdu835XPowerGroup,_u:pdu835XActivePowerGroups,'pdu835XPowerGroupTable':pdu835XPowerGroupTable,'pdu835XEntry':pdu835XEntry,_W:pdu835XPowerGroupIndex,_t:pdu835XRCurrent3P,_s:pdu835XNCurrent3P,_S:pdu835XMeasurementBoxConnected,'pdu835XExtSensors':pdu835XExtSensors,'pdu835XSensorTable':pdu835XSensorTable,'pdu835XSensorEntry':pdu835XSensorEntry,_X:pdu835XSensorIndex,_N:pdu835XTempSensor,_O:pdu835XHygroSensor,_P:pdu835XInputSensor,'pdu835XConf':pdu835XConf,'pdu835XGroups':pdu835XGroups,'pdu835XBasicGroup':pdu835XBasicGroup,'pdu835XNotificationGroup':pdu835XNotificationGroup,'pdu835XCompls':pdu835XCompls})