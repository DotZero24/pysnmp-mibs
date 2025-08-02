_a='pdu818XPowerDataEvt4'
_Z='pdu818XPowerDataEvt3'
_Y='pdu818XPowerDataEvt2'
_X='pdu818XPowerDataEvt1'
_W='pdu818XHygroEvtSen1'
_V='pdu818XTempEvtSen1'
_U='pdu818XChanStatus'
_T='pdu818XActivePowerChan'
_S='pdu818XTrapAddr'
_R='pdu818XTrapCtrl'
_Q='pdu818XSensorIndex'
_P='pdu818XPowerIndex'
_O='pdu818XTrapIPIndex'
_N='read-write'
_M='Unsigned32'
_L='OctetString'
_K='pdu818XHygroSensor'
_J='pdu818XTempSensor'
_I='not-accessible'
_H='pdu818XVoltage'
_G='pdu818XCurrent'
_F='pdu818XPowerActive'
_E='pdu818XEnergyActive'
_D='Integer32'
_C='read-only'
_B='current'
_A='GUDEADS-PDU818X-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-03-05 13:56',))
_GadsPDU818X_ObjectIdentity=ObjectIdentity
gadsPDU818X=_GadsPDU818X_ObjectIdentity((1,3,6,1,4,1,28507,35))
_Events_ObjectIdentity=ObjectIdentity
events=_Events_ObjectIdentity((1,3,6,1,4,1,28507,35,0))
_Pdu818XObjects_ObjectIdentity=ObjectIdentity
pdu818XObjects=_Pdu818XObjects_ObjectIdentity((1,3,6,1,4,1,28507,35,1))
_Pdu818XCommonConfig_ObjectIdentity=ObjectIdentity
pdu818XCommonConfig=_Pdu818XCommonConfig_ObjectIdentity((1,3,6,1,4,1,28507,35,1,1))
_Pdu818XSNMPaccess_ObjectIdentity=ObjectIdentity
pdu818XSNMPaccess=_Pdu818XSNMPaccess_ObjectIdentity((1,3,6,1,4,1,28507,35,1,1,1))
class _Pdu818XTrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Pdu818XTrapCtrl_Type.__name__=_D
_Pdu818XTrapCtrl_Object=MibScalar
pdu818XTrapCtrl=_Pdu818XTrapCtrl_Object((1,3,6,1,4,1,28507,35,1,1,1,1),_Pdu818XTrapCtrl_Type())
pdu818XTrapCtrl.setMaxAccess(_N)
if mibBuilder.loadTexts:pdu818XTrapCtrl.setStatus(_B)
_Pdu818XTrapIPTable_Object=MibTable
pdu818XTrapIPTable=_Pdu818XTrapIPTable_Object((1,3,6,1,4,1,28507,35,1,1,1,2))
if mibBuilder.loadTexts:pdu818XTrapIPTable.setStatus(_B)
_Pdu818XTrapIPEntry_Object=MibTableRow
pdu818XTrapIPEntry=_Pdu818XTrapIPEntry_Object((1,3,6,1,4,1,28507,35,1,1,1,2,1))
pdu818XTrapIPEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:pdu818XTrapIPEntry.setStatus(_B)
class _Pdu818XTrapIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Pdu818XTrapIPIndex_Type.__name__=_D
_Pdu818XTrapIPIndex_Object=MibTableColumn
pdu818XTrapIPIndex=_Pdu818XTrapIPIndex_Object((1,3,6,1,4,1,28507,35,1,1,1,2,1,1),_Pdu818XTrapIPIndex_Type())
pdu818XTrapIPIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:pdu818XTrapIPIndex.setStatus(_B)
class _Pdu818XTrapAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,99))
_Pdu818XTrapAddr_Type.__name__=_L
_Pdu818XTrapAddr_Object=MibTableColumn
pdu818XTrapAddr=_Pdu818XTrapAddr_Object((1,3,6,1,4,1,28507,35,1,1,1,2,1,2),_Pdu818XTrapAddr_Type())
pdu818XTrapAddr.setMaxAccess(_N)
if mibBuilder.loadTexts:pdu818XTrapAddr.setStatus(_B)
_Pdu818XDeviceConfig_ObjectIdentity=ObjectIdentity
pdu818XDeviceConfig=_Pdu818XDeviceConfig_ObjectIdentity((1,3,6,1,4,1,28507,35,1,2))
_Pdu818XIntActors_ObjectIdentity=ObjectIdentity
pdu818XIntActors=_Pdu818XIntActors_ObjectIdentity((1,3,6,1,4,1,28507,35,1,3))
_Pdu818XExtActors_ObjectIdentity=ObjectIdentity
pdu818XExtActors=_Pdu818XExtActors_ObjectIdentity((1,3,6,1,4,1,28507,35,1,4))
_Pdu818XIntSensors_ObjectIdentity=ObjectIdentity
pdu818XIntSensors=_Pdu818XIntSensors_ObjectIdentity((1,3,6,1,4,1,28507,35,1,5))
_Pdu818XPowerChan_ObjectIdentity=ObjectIdentity
pdu818XPowerChan=_Pdu818XPowerChan_ObjectIdentity((1,3,6,1,4,1,28507,35,1,5,1))
class _Pdu818XActivePowerChan_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Pdu818XActivePowerChan_Type.__name__=_M
_Pdu818XActivePowerChan_Object=MibScalar
pdu818XActivePowerChan=_Pdu818XActivePowerChan_Object((1,3,6,1,4,1,28507,35,1,5,1,1),_Pdu818XActivePowerChan_Type())
pdu818XActivePowerChan.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu818XActivePowerChan.setStatus(_B)
_Pdu818XPowerTable_Object=MibTable
pdu818XPowerTable=_Pdu818XPowerTable_Object((1,3,6,1,4,1,28507,35,1,5,1,2))
if mibBuilder.loadTexts:pdu818XPowerTable.setStatus(_B)
_Pdu818XPowerEntry_Object=MibTableRow
pdu818XPowerEntry=_Pdu818XPowerEntry_Object((1,3,6,1,4,1,28507,35,1,5,1,2,1))
pdu818XPowerEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:pdu818XPowerEntry.setStatus(_B)
class _Pdu818XPowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_Pdu818XPowerIndex_Type.__name__=_D
_Pdu818XPowerIndex_Object=MibTableColumn
pdu818XPowerIndex=_Pdu818XPowerIndex_Object((1,3,6,1,4,1,28507,35,1,5,1,2,1,1),_Pdu818XPowerIndex_Type())
pdu818XPowerIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:pdu818XPowerIndex.setStatus(_B)
class _Pdu818XChanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Pdu818XChanStatus_Type.__name__=_D
_Pdu818XChanStatus_Object=MibTableColumn
pdu818XChanStatus=_Pdu818XChanStatus_Object((1,3,6,1,4,1,28507,35,1,5,1,2,1,2),_Pdu818XChanStatus_Type())
pdu818XChanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu818XChanStatus.setStatus(_B)
_Pdu818XEnergyActive_Type=Unsigned32
_Pdu818XEnergyActive_Object=MibTableColumn
pdu818XEnergyActive=_Pdu818XEnergyActive_Object((1,3,6,1,4,1,28507,35,1,5,1,2,1,3),_Pdu818XEnergyActive_Type())
pdu818XEnergyActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu818XEnergyActive.setStatus(_B)
if mibBuilder.loadTexts:pdu818XEnergyActive.setUnits('Wh')
_Pdu818XPowerActive_Type=Unsigned32
_Pdu818XPowerActive_Object=MibTableColumn
pdu818XPowerActive=_Pdu818XPowerActive_Object((1,3,6,1,4,1,28507,35,1,5,1,2,1,4),_Pdu818XPowerActive_Type())
pdu818XPowerActive.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu818XPowerActive.setStatus(_B)
if mibBuilder.loadTexts:pdu818XPowerActive.setUnits('W')
_Pdu818XCurrent_Type=Unsigned32
_Pdu818XCurrent_Object=MibTableColumn
pdu818XCurrent=_Pdu818XCurrent_Object((1,3,6,1,4,1,28507,35,1,5,1,2,1,5),_Pdu818XCurrent_Type())
pdu818XCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu818XCurrent.setStatus(_B)
if mibBuilder.loadTexts:pdu818XCurrent.setUnits('mA')
_Pdu818XVoltage_Type=Unsigned32
_Pdu818XVoltage_Object=MibTableColumn
pdu818XVoltage=_Pdu818XVoltage_Object((1,3,6,1,4,1,28507,35,1,5,1,2,1,6),_Pdu818XVoltage_Type())
pdu818XVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu818XVoltage.setStatus(_B)
if mibBuilder.loadTexts:pdu818XVoltage.setUnits('V')
_Pdu818XExtSensors_ObjectIdentity=ObjectIdentity
pdu818XExtSensors=_Pdu818XExtSensors_ObjectIdentity((1,3,6,1,4,1,28507,35,1,6))
_Pdu818XSensorTable_Object=MibTable
pdu818XSensorTable=_Pdu818XSensorTable_Object((1,3,6,1,4,1,28507,35,1,6,1))
if mibBuilder.loadTexts:pdu818XSensorTable.setStatus(_B)
_Pdu818XSensorEntry_Object=MibTableRow
pdu818XSensorEntry=_Pdu818XSensorEntry_Object((1,3,6,1,4,1,28507,35,1,6,1,1))
pdu818XSensorEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:pdu818XSensorEntry.setStatus(_B)
class _Pdu818XSensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Pdu818XSensorIndex_Type.__name__=_D
_Pdu818XSensorIndex_Object=MibTableColumn
pdu818XSensorIndex=_Pdu818XSensorIndex_Object((1,3,6,1,4,1,28507,35,1,6,1,1,1),_Pdu818XSensorIndex_Type())
pdu818XSensorIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:pdu818XSensorIndex.setStatus(_B)
_Pdu818XTempSensor_Type=Integer32
_Pdu818XTempSensor_Object=MibTableColumn
pdu818XTempSensor=_Pdu818XTempSensor_Object((1,3,6,1,4,1,28507,35,1,6,1,1,2),_Pdu818XTempSensor_Type())
pdu818XTempSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu818XTempSensor.setStatus(_B)
if mibBuilder.loadTexts:pdu818XTempSensor.setUnits('10th of degree Celsius')
_Pdu818XHygroSensor_Type=Integer32
_Pdu818XHygroSensor_Object=MibTableColumn
pdu818XHygroSensor=_Pdu818XHygroSensor_Object((1,3,6,1,4,1,28507,35,1,6,1,1,3),_Pdu818XHygroSensor_Type())
pdu818XHygroSensor.setMaxAccess(_C)
if mibBuilder.loadTexts:pdu818XHygroSensor.setStatus(_B)
if mibBuilder.loadTexts:pdu818XHygroSensor.setUnits('10th of percentage humidity')
_Pdu818XConf_ObjectIdentity=ObjectIdentity
pdu818XConf=_Pdu818XConf_ObjectIdentity((1,3,6,1,4,1,28507,35,2))
_Pdu818XGroups_ObjectIdentity=ObjectIdentity
pdu818XGroups=_Pdu818XGroups_ObjectIdentity((1,3,6,1,4,1,28507,35,2,1))
_Pdu818XCompls_ObjectIdentity=ObjectIdentity
pdu818XCompls=_Pdu818XCompls_ObjectIdentity((1,3,6,1,4,1,28507,35,2,2))
pdu818XBasicGroup=ObjectGroup((1,3,6,1,4,1,28507,35,2,1,1))
pdu818XBasicGroup.setObjects(*((_A,_R),(_A,_S),(_A,_J),(_A,_K),(_A,_T),(_A,_U),(_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:pdu818XBasicGroup.setStatus(_B)
pdu818XPowerDataEvt1=NotificationType((1,3,6,1,4,1,28507,35,0,1))
pdu818XPowerDataEvt1.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:pdu818XPowerDataEvt1.setStatus(_B)
pdu818XPowerDataEvt2=NotificationType((1,3,6,1,4,1,28507,35,0,2))
pdu818XPowerDataEvt2.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:pdu818XPowerDataEvt2.setStatus(_B)
pdu818XPowerDataEvt3=NotificationType((1,3,6,1,4,1,28507,35,0,3))
pdu818XPowerDataEvt3.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:pdu818XPowerDataEvt3.setStatus(_B)
pdu818XPowerDataEvt4=NotificationType((1,3,6,1,4,1,28507,35,0,4))
pdu818XPowerDataEvt4.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:pdu818XPowerDataEvt4.setStatus(_B)
pdu818XTempEvtSen1=NotificationType((1,3,6,1,4,1,28507,35,0,6))
pdu818XTempEvtSen1.setObjects((_A,_J))
if mibBuilder.loadTexts:pdu818XTempEvtSen1.setStatus(_B)
pdu818XHygroEvtSen1=NotificationType((1,3,6,1,4,1,28507,35,0,7))
pdu818XHygroEvtSen1.setObjects((_A,_K))
if mibBuilder.loadTexts:pdu818XHygroEvtSen1.setStatus(_B)
pdu818XNotificationGroup=NotificationGroup((1,3,6,1,4,1,28507,35,2,1,2))
pdu818XNotificationGroup.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:pdu818XNotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'gudeads':gudeads,'gadsPDU818X':gadsPDU818X,'events':events,_X:pdu818XPowerDataEvt1,_Y:pdu818XPowerDataEvt2,_Z:pdu818XPowerDataEvt3,_a:pdu818XPowerDataEvt4,_V:pdu818XTempEvtSen1,_W:pdu818XHygroEvtSen1,'pdu818XObjects':pdu818XObjects,'pdu818XCommonConfig':pdu818XCommonConfig,'pdu818XSNMPaccess':pdu818XSNMPaccess,_R:pdu818XTrapCtrl,'pdu818XTrapIPTable':pdu818XTrapIPTable,'pdu818XTrapIPEntry':pdu818XTrapIPEntry,_O:pdu818XTrapIPIndex,_S:pdu818XTrapAddr,'pdu818XDeviceConfig':pdu818XDeviceConfig,'pdu818XIntActors':pdu818XIntActors,'pdu818XExtActors':pdu818XExtActors,'pdu818XIntSensors':pdu818XIntSensors,'pdu818XPowerChan':pdu818XPowerChan,_T:pdu818XActivePowerChan,'pdu818XPowerTable':pdu818XPowerTable,'pdu818XPowerEntry':pdu818XPowerEntry,_P:pdu818XPowerIndex,_U:pdu818XChanStatus,_E:pdu818XEnergyActive,_F:pdu818XPowerActive,_G:pdu818XCurrent,_H:pdu818XVoltage,'pdu818XExtSensors':pdu818XExtSensors,'pdu818XSensorTable':pdu818XSensorTable,'pdu818XSensorEntry':pdu818XSensorEntry,_Q:pdu818XSensorIndex,_J:pdu818XTempSensor,_K:pdu818XHygroSensor,'pdu818XConf':pdu818XConf,'pdu818XGroups':pdu818XGroups,'pdu818XBasicGroup':pdu818XBasicGroup,'pdu818XNotificationGroup':pdu818XNotificationGroup,'pdu818XCompls':pdu818XCompls})