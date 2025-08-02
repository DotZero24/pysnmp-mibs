_k='epc8HygroEvtSen2'
_j='epc8TempEvtSen2'
_i='epc8HygroEvtSen1'
_h='epc8TempEvtSen1'
_g='epcSwitchEvtPort8'
_f='epcSwitchEvtPort7'
_e='epcSwitchEvtPort6'
_d='epcSwitchEvtPort5'
_c='epcSwitchEvtPort4'
_b='epcSwitchEvtPort3'
_a='epcSwitchEvtPort2'
_Z='epcSwitchEvtPort1'
_Y='epc8Irms'
_X='epc8PortRepowerTime'
_W='epc8PortStartupDelay'
_V='epc8PortStartupMode'
_U='epc8TrapIPPort'
_T='epc8TrapIPAddr'
_S='epc8TrapCtrl'
_R='epc8portNumber'
_Q='epc8SensorIndex'
_P='seconds'
_O='epc8PortIndex'
_N='epc8TrapIPIndex'
_M='IpAddress'
_L='OctetString'
_K='not-accessible'
_J='epc8HygroSensor'
_I='epc8TempSensor'
_H='read-only'
_G='read-write'
_F='epc8PortSwitchCount'
_E='epc8PortState'
_D='epc8PortName'
_C='Integer32'
_B='current'
_A='GUDEADS-EPC8X-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,_M,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-03-05 13:56',))
_GadsEPC8_ObjectIdentity=ObjectIdentity
gadsEPC8=_GadsEPC8_ObjectIdentity((1,3,6,1,4,1,28507,1))
_Events_ObjectIdentity=ObjectIdentity
events=_Events_ObjectIdentity((1,3,6,1,4,1,28507,1,0))
_Epc8Objects_ObjectIdentity=ObjectIdentity
epc8Objects=_Epc8Objects_ObjectIdentity((1,3,6,1,4,1,28507,1,1))
_Epc8SNMPaccess_ObjectIdentity=ObjectIdentity
epc8SNMPaccess=_Epc8SNMPaccess_ObjectIdentity((1,3,6,1,4,1,28507,1,1,1))
class _Epc8TrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Epc8TrapCtrl_Type.__name__=_C
_Epc8TrapCtrl_Object=MibScalar
epc8TrapCtrl=_Epc8TrapCtrl_Object((1,3,6,1,4,1,28507,1,1,1,1),_Epc8TrapCtrl_Type())
epc8TrapCtrl.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8TrapCtrl.setStatus(_B)
_Epc8TrapIPTable_Object=MibTable
epc8TrapIPTable=_Epc8TrapIPTable_Object((1,3,6,1,4,1,28507,1,1,1,2))
if mibBuilder.loadTexts:epc8TrapIPTable.setStatus(_B)
_Epc8TrapIPEntry_Object=MibTableRow
epc8TrapIPEntry=_Epc8TrapIPEntry_Object((1,3,6,1,4,1,28507,1,1,1,2,1))
epc8TrapIPEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:epc8TrapIPEntry.setStatus(_B)
class _Epc8TrapIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Epc8TrapIPIndex_Type.__name__=_C
_Epc8TrapIPIndex_Object=MibTableColumn
epc8TrapIPIndex=_Epc8TrapIPIndex_Object((1,3,6,1,4,1,28507,1,1,1,2,1,1),_Epc8TrapIPIndex_Type())
epc8TrapIPIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:epc8TrapIPIndex.setStatus(_B)
class _Epc8TrapIPAddr_Type(IpAddress):defaultHexValue='00000000'
_Epc8TrapIPAddr_Type.__name__=_M
_Epc8TrapIPAddr_Object=MibTableColumn
epc8TrapIPAddr=_Epc8TrapIPAddr_Object((1,3,6,1,4,1,28507,1,1,1,2,1,2),_Epc8TrapIPAddr_Type())
epc8TrapIPAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8TrapIPAddr.setStatus(_B)
class _Epc8TrapIPPort_Type(Integer32):defaultValue=162;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_Epc8TrapIPPort_Type.__name__=_C
_Epc8TrapIPPort_Object=MibTableColumn
epc8TrapIPPort=_Epc8TrapIPPort_Object((1,3,6,1,4,1,28507,1,1,1,2,1,3),_Epc8TrapIPPort_Type())
epc8TrapIPPort.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8TrapIPPort.setStatus(_B)
_Epc8powerports_ObjectIdentity=ObjectIdentity
epc8powerports=_Epc8powerports_ObjectIdentity((1,3,6,1,4,1,28507,1,1,2))
class _Epc8portNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Epc8portNumber_Type.__name__=_C
_Epc8portNumber_Object=MibScalar
epc8portNumber=_Epc8portNumber_Object((1,3,6,1,4,1,28507,1,1,2,1),_Epc8portNumber_Type())
epc8portNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:epc8portNumber.setStatus(_B)
_Epc8portTable_Object=MibTable
epc8portTable=_Epc8portTable_Object((1,3,6,1,4,1,28507,1,1,2,2))
if mibBuilder.loadTexts:epc8portTable.setStatus(_B)
_Epc8portEntry_Object=MibTableRow
epc8portEntry=_Epc8portEntry_Object((1,3,6,1,4,1,28507,1,1,2,2,1))
epc8portEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:epc8portEntry.setStatus(_B)
class _Epc8PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Epc8PortIndex_Type.__name__=_C
_Epc8PortIndex_Object=MibTableColumn
epc8PortIndex=_Epc8PortIndex_Object((1,3,6,1,4,1,28507,1,1,2,2,1,1),_Epc8PortIndex_Type())
epc8PortIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:epc8PortIndex.setStatus(_B)
class _Epc8PortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_Epc8PortName_Type.__name__=_L
_Epc8PortName_Object=MibTableColumn
epc8PortName=_Epc8PortName_Object((1,3,6,1,4,1,28507,1,1,2,2,1,2),_Epc8PortName_Type())
epc8PortName.setMaxAccess(_H)
if mibBuilder.loadTexts:epc8PortName.setStatus(_B)
class _Epc8PortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_Epc8PortState_Type.__name__=_C
_Epc8PortState_Object=MibTableColumn
epc8PortState=_Epc8PortState_Object((1,3,6,1,4,1,28507,1,1,2,2,1,3),_Epc8PortState_Type())
epc8PortState.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8PortState.setStatus(_B)
_Epc8PortSwitchCount_Type=Counter32
_Epc8PortSwitchCount_Object=MibTableColumn
epc8PortSwitchCount=_Epc8PortSwitchCount_Object((1,3,6,1,4,1,28507,1,1,2,2,1,4),_Epc8PortSwitchCount_Type())
epc8PortSwitchCount.setMaxAccess(_H)
if mibBuilder.loadTexts:epc8PortSwitchCount.setStatus(_B)
class _Epc8PortStartupMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('off',0),('on',1),('laststate',2)))
_Epc8PortStartupMode_Type.__name__=_C
_Epc8PortStartupMode_Object=MibTableColumn
epc8PortStartupMode=_Epc8PortStartupMode_Object((1,3,6,1,4,1,28507,1,1,2,2,1,5),_Epc8PortStartupMode_Type())
epc8PortStartupMode.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8PortStartupMode.setStatus(_B)
class _Epc8PortStartupDelay_Type(Integer32):defaultValue=0
_Epc8PortStartupDelay_Type.__name__=_C
_Epc8PortStartupDelay_Object=MibTableColumn
epc8PortStartupDelay=_Epc8PortStartupDelay_Object((1,3,6,1,4,1,28507,1,1,2,2,1,6),_Epc8PortStartupDelay_Type())
epc8PortStartupDelay.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8PortStartupDelay.setStatus(_B)
if mibBuilder.loadTexts:epc8PortStartupDelay.setUnits(_P)
class _Epc8PortRepowerTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Epc8PortRepowerTime_Type.__name__=_C
_Epc8PortRepowerTime_Object=MibTableColumn
epc8PortRepowerTime=_Epc8PortRepowerTime_Object((1,3,6,1,4,1,28507,1,1,2,2,1,7),_Epc8PortRepowerTime_Type())
epc8PortRepowerTime.setMaxAccess(_G)
if mibBuilder.loadTexts:epc8PortRepowerTime.setStatus(_B)
if mibBuilder.loadTexts:epc8PortRepowerTime.setUnits(_P)
_Epc8Sensors_ObjectIdentity=ObjectIdentity
epc8Sensors=_Epc8Sensors_ObjectIdentity((1,3,6,1,4,1,28507,1,1,3))
_Epc8Irms_Type=Integer32
_Epc8Irms_Object=MibScalar
epc8Irms=_Epc8Irms_Object((1,3,6,1,4,1,28507,1,1,3,1),_Epc8Irms_Type())
epc8Irms.setMaxAccess(_H)
if mibBuilder.loadTexts:epc8Irms.setStatus(_B)
if mibBuilder.loadTexts:epc8Irms.setUnits('mA')
_Epc8SensorTable_Object=MibTable
epc8SensorTable=_Epc8SensorTable_Object((1,3,6,1,4,1,28507,1,1,3,2))
if mibBuilder.loadTexts:epc8SensorTable.setStatus(_B)
_Epc8SensorEntry_Object=MibTableRow
epc8SensorEntry=_Epc8SensorEntry_Object((1,3,6,1,4,1,28507,1,1,3,2,1))
epc8SensorEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:epc8SensorEntry.setStatus(_B)
class _Epc8SensorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Epc8SensorIndex_Type.__name__=_C
_Epc8SensorIndex_Object=MibTableColumn
epc8SensorIndex=_Epc8SensorIndex_Object((1,3,6,1,4,1,28507,1,1,3,2,1,1),_Epc8SensorIndex_Type())
epc8SensorIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:epc8SensorIndex.setStatus(_B)
_Epc8TempSensor_Type=Integer32
_Epc8TempSensor_Object=MibTableColumn
epc8TempSensor=_Epc8TempSensor_Object((1,3,6,1,4,1,28507,1,1,3,2,1,2),_Epc8TempSensor_Type())
epc8TempSensor.setMaxAccess(_H)
if mibBuilder.loadTexts:epc8TempSensor.setStatus(_B)
if mibBuilder.loadTexts:epc8TempSensor.setUnits('10th of degree Celsius')
_Epc8HygroSensor_Type=Integer32
_Epc8HygroSensor_Object=MibTableColumn
epc8HygroSensor=_Epc8HygroSensor_Object((1,3,6,1,4,1,28507,1,1,3,2,1,3),_Epc8HygroSensor_Type())
epc8HygroSensor.setMaxAccess(_H)
if mibBuilder.loadTexts:epc8HygroSensor.setStatus(_B)
if mibBuilder.loadTexts:epc8HygroSensor.setUnits('10th of percentage humidity')
_Epc8Conf_ObjectIdentity=ObjectIdentity
epc8Conf=_Epc8Conf_ObjectIdentity((1,3,6,1,4,1,28507,1,3))
_Epc8Groups_ObjectIdentity=ObjectIdentity
epc8Groups=_Epc8Groups_ObjectIdentity((1,3,6,1,4,1,28507,1,3,1))
_Epc8Compls_ObjectIdentity=ObjectIdentity
epc8Compls=_Epc8Compls_ObjectIdentity((1,3,6,1,4,1,28507,1,3,2))
epc8BasicGroup=ObjectGroup((1,3,6,1,4,1,28507,1,3,1,1))
epc8BasicGroup.setObjects(*((_A,_R),(_A,_D),(_A,_E),(_A,_F),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:epc8BasicGroup.setStatus(_B)
epcSwitchEvtPort1=NotificationType((1,3,6,1,4,1,28507,1,0,1))
epcSwitchEvtPort1.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:epcSwitchEvtPort1.setStatus(_B)
epcSwitchEvtPort2=NotificationType((1,3,6,1,4,1,28507,1,0,2))
epcSwitchEvtPort2.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:epcSwitchEvtPort2.setStatus(_B)
epcSwitchEvtPort3=NotificationType((1,3,6,1,4,1,28507,1,0,3))
epcSwitchEvtPort3.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:epcSwitchEvtPort3.setStatus(_B)
epcSwitchEvtPort4=NotificationType((1,3,6,1,4,1,28507,1,0,4))
epcSwitchEvtPort4.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:epcSwitchEvtPort4.setStatus(_B)
epcSwitchEvtPort5=NotificationType((1,3,6,1,4,1,28507,1,0,5))
epcSwitchEvtPort5.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:epcSwitchEvtPort5.setStatus(_B)
epcSwitchEvtPort6=NotificationType((1,3,6,1,4,1,28507,1,0,6))
epcSwitchEvtPort6.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:epcSwitchEvtPort6.setStatus(_B)
epcSwitchEvtPort7=NotificationType((1,3,6,1,4,1,28507,1,0,7))
epcSwitchEvtPort7.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:epcSwitchEvtPort7.setStatus(_B)
epcSwitchEvtPort8=NotificationType((1,3,6,1,4,1,28507,1,0,8))
epcSwitchEvtPort8.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:epcSwitchEvtPort8.setStatus(_B)
epc8TempEvtSen1=NotificationType((1,3,6,1,4,1,28507,1,0,9))
epc8TempEvtSen1.setObjects((_A,_I))
if mibBuilder.loadTexts:epc8TempEvtSen1.setStatus(_B)
epc8TempEvtSen2=NotificationType((1,3,6,1,4,1,28507,1,0,10))
epc8TempEvtSen2.setObjects((_A,_I))
if mibBuilder.loadTexts:epc8TempEvtSen2.setStatus(_B)
epc8HygroEvtSen1=NotificationType((1,3,6,1,4,1,28507,1,0,11))
epc8HygroEvtSen1.setObjects((_A,_J))
if mibBuilder.loadTexts:epc8HygroEvtSen1.setStatus(_B)
epc8HygroEvtSen2=NotificationType((1,3,6,1,4,1,28507,1,0,12))
epc8HygroEvtSen2.setObjects((_A,_J))
if mibBuilder.loadTexts:epc8HygroEvtSen2.setStatus(_B)
epc8NotificationGroup=NotificationGroup((1,3,6,1,4,1,28507,1,3,1,2))
epc8NotificationGroup.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:epc8NotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'gudeads':gudeads,'gadsEPC8':gadsEPC8,'events':events,_Z:epcSwitchEvtPort1,_a:epcSwitchEvtPort2,_b:epcSwitchEvtPort3,_c:epcSwitchEvtPort4,_d:epcSwitchEvtPort5,_e:epcSwitchEvtPort6,_f:epcSwitchEvtPort7,_g:epcSwitchEvtPort8,_h:epc8TempEvtSen1,_j:epc8TempEvtSen2,_i:epc8HygroEvtSen1,_k:epc8HygroEvtSen2,'epc8Objects':epc8Objects,'epc8SNMPaccess':epc8SNMPaccess,_S:epc8TrapCtrl,'epc8TrapIPTable':epc8TrapIPTable,'epc8TrapIPEntry':epc8TrapIPEntry,_N:epc8TrapIPIndex,_T:epc8TrapIPAddr,_U:epc8TrapIPPort,'epc8powerports':epc8powerports,_R:epc8portNumber,'epc8portTable':epc8portTable,'epc8portEntry':epc8portEntry,_O:epc8PortIndex,_D:epc8PortName,_E:epc8PortState,_F:epc8PortSwitchCount,_V:epc8PortStartupMode,_W:epc8PortStartupDelay,_X:epc8PortRepowerTime,'epc8Sensors':epc8Sensors,_Y:epc8Irms,'epc8SensorTable':epc8SensorTable,'epc8SensorEntry':epc8SensorEntry,_Q:epc8SensorIndex,_I:epc8TempSensor,_J:epc8HygroSensor,'epc8Conf':epc8Conf,'epc8Groups':epc8Groups,'epc8BasicGroup':epc8BasicGroup,'epc8NotificationGroup':epc8NotificationGroup,'epc8Compls':epc8Compls})