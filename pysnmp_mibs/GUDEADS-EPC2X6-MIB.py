_k='epc2x6FuseEvt'
_j='epc2x6TempEvt'
_i='epc2x6witchEvt12'
_h='epc2x6witchEvt11'
_g='epc2x6witchEvt10'
_f='epc2x6witchEvt9'
_e='epc2x6witchEvt8'
_d='epc2x6witchEvt7'
_c='epc2x6witchEvt6'
_b='epc2x6witchEvt5'
_a='epc2x6witchEvt4'
_Z='epc2x6witchEvt3'
_Y='epc2x6witchEvt2'
_X='epc2x6witchEvt1'
_W='epc2x6PortRepowerTime'
_V='epc2x6PortStartupDelay'
_U='epc2x6PortStartupMode'
_T='epc2x6TrapIPPort'
_S='epc2x6TrapIPAddr'
_R='epc2x6TrapCtrl'
_Q='epc2x6portNumber'
_P='seconds'
_O='epc2x6PortIndex'
_N='not-accessible'
_M='epc2x6TrapIPIndex'
_L='IpAddress'
_K='OctetString'
_J='epc2x6portFuses'
_I='epc2x6Temperature'
_H='read-only'
_G='read-write'
_F='Integer32'
_E='epc2x6PortSwitchCount'
_D='epc2x6PortState'
_C='epc2x6PortName'
_B='current'
_A='GUDEADS-EPC2X6-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,_L,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-03-05 13:56',))
_Events_ObjectIdentity=ObjectIdentity
events=_Events_ObjectIdentity((1,3,6,1,4,1,28507,0))
_GadsEPC2x6_ObjectIdentity=ObjectIdentity
gadsEPC2x6=_GadsEPC2x6_ObjectIdentity((1,3,6,1,4,1,28507,6))
_Epc2x6Objects_ObjectIdentity=ObjectIdentity
epc2x6Objects=_Epc2x6Objects_ObjectIdentity((1,3,6,1,4,1,28507,6,1))
_Epc2x6SNMPaccess_ObjectIdentity=ObjectIdentity
epc2x6SNMPaccess=_Epc2x6SNMPaccess_ObjectIdentity((1,3,6,1,4,1,28507,6,1,1))
class _Epc2x6TrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_Epc2x6TrapCtrl_Type.__name__=_F
_Epc2x6TrapCtrl_Object=MibScalar
epc2x6TrapCtrl=_Epc2x6TrapCtrl_Object((1,3,6,1,4,1,28507,6,1,1,1),_Epc2x6TrapCtrl_Type())
epc2x6TrapCtrl.setMaxAccess(_G)
if mibBuilder.loadTexts:epc2x6TrapCtrl.setStatus(_B)
_Epc2x6TrapIPTable_Object=MibTable
epc2x6TrapIPTable=_Epc2x6TrapIPTable_Object((1,3,6,1,4,1,28507,6,1,1,2))
if mibBuilder.loadTexts:epc2x6TrapIPTable.setStatus(_B)
_Epc2x6TrapIPEntry_Object=MibTableRow
epc2x6TrapIPEntry=_Epc2x6TrapIPEntry_Object((1,3,6,1,4,1,28507,6,1,1,2,1))
epc2x6TrapIPEntry.setIndexNames((0,_A,_M))
if mibBuilder.loadTexts:epc2x6TrapIPEntry.setStatus(_B)
class _Epc2x6TrapIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Epc2x6TrapIPIndex_Type.__name__=_F
_Epc2x6TrapIPIndex_Object=MibTableColumn
epc2x6TrapIPIndex=_Epc2x6TrapIPIndex_Object((1,3,6,1,4,1,28507,6,1,1,2,1,1),_Epc2x6TrapIPIndex_Type())
epc2x6TrapIPIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:epc2x6TrapIPIndex.setStatus(_B)
class _Epc2x6TrapIPAddr_Type(IpAddress):defaultHexValue='00000000'
_Epc2x6TrapIPAddr_Type.__name__=_L
_Epc2x6TrapIPAddr_Object=MibTableColumn
epc2x6TrapIPAddr=_Epc2x6TrapIPAddr_Object((1,3,6,1,4,1,28507,6,1,1,2,1,2),_Epc2x6TrapIPAddr_Type())
epc2x6TrapIPAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:epc2x6TrapIPAddr.setStatus(_B)
class _Epc2x6TrapIPPort_Type(Integer32):defaultValue=162;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_Epc2x6TrapIPPort_Type.__name__=_F
_Epc2x6TrapIPPort_Object=MibTableColumn
epc2x6TrapIPPort=_Epc2x6TrapIPPort_Object((1,3,6,1,4,1,28507,6,1,1,2,1,3),_Epc2x6TrapIPPort_Type())
epc2x6TrapIPPort.setMaxAccess(_G)
if mibBuilder.loadTexts:epc2x6TrapIPPort.setStatus(_B)
_Epc2x6powerports_ObjectIdentity=ObjectIdentity
epc2x6powerports=_Epc2x6powerports_ObjectIdentity((1,3,6,1,4,1,28507,6,1,2))
class _Epc2x6portNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_Epc2x6portNumber_Type.__name__=_F
_Epc2x6portNumber_Object=MibScalar
epc2x6portNumber=_Epc2x6portNumber_Object((1,3,6,1,4,1,28507,6,1,2,1),_Epc2x6portNumber_Type())
epc2x6portNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:epc2x6portNumber.setStatus(_B)
_Epc2x6portTable_Object=MibTable
epc2x6portTable=_Epc2x6portTable_Object((1,3,6,1,4,1,28507,6,1,2,2))
if mibBuilder.loadTexts:epc2x6portTable.setStatus(_B)
_Epc2x6portEntry_Object=MibTableRow
epc2x6portEntry=_Epc2x6portEntry_Object((1,3,6,1,4,1,28507,6,1,2,2,1))
epc2x6portEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:epc2x6portEntry.setStatus(_B)
class _Epc2x6PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_Epc2x6PortIndex_Type.__name__=_F
_Epc2x6PortIndex_Object=MibTableColumn
epc2x6PortIndex=_Epc2x6PortIndex_Object((1,3,6,1,4,1,28507,6,1,2,2,1,1),_Epc2x6PortIndex_Type())
epc2x6PortIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:epc2x6PortIndex.setStatus(_B)
class _Epc2x6PortName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_Epc2x6PortName_Type.__name__=_K
_Epc2x6PortName_Object=MibTableColumn
epc2x6PortName=_Epc2x6PortName_Object((1,3,6,1,4,1,28507,6,1,2,2,1,2),_Epc2x6PortName_Type())
epc2x6PortName.setMaxAccess(_H)
if mibBuilder.loadTexts:epc2x6PortName.setStatus(_B)
class _Epc2x6PortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_Epc2x6PortState_Type.__name__=_F
_Epc2x6PortState_Object=MibTableColumn
epc2x6PortState=_Epc2x6PortState_Object((1,3,6,1,4,1,28507,6,1,2,2,1,3),_Epc2x6PortState_Type())
epc2x6PortState.setMaxAccess(_G)
if mibBuilder.loadTexts:epc2x6PortState.setStatus(_B)
_Epc2x6PortSwitchCount_Type=Counter32
_Epc2x6PortSwitchCount_Object=MibTableColumn
epc2x6PortSwitchCount=_Epc2x6PortSwitchCount_Object((1,3,6,1,4,1,28507,6,1,2,2,1,4),_Epc2x6PortSwitchCount_Type())
epc2x6PortSwitchCount.setMaxAccess(_H)
if mibBuilder.loadTexts:epc2x6PortSwitchCount.setStatus(_B)
class _Epc2x6PortStartupMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('off',0),('on',1),('laststate',2)))
_Epc2x6PortStartupMode_Type.__name__=_F
_Epc2x6PortStartupMode_Object=MibTableColumn
epc2x6PortStartupMode=_Epc2x6PortStartupMode_Object((1,3,6,1,4,1,28507,6,1,2,2,1,5),_Epc2x6PortStartupMode_Type())
epc2x6PortStartupMode.setMaxAccess(_G)
if mibBuilder.loadTexts:epc2x6PortStartupMode.setStatus(_B)
class _Epc2x6PortStartupDelay_Type(Integer32):defaultValue=0
_Epc2x6PortStartupDelay_Type.__name__=_F
_Epc2x6PortStartupDelay_Object=MibTableColumn
epc2x6PortStartupDelay=_Epc2x6PortStartupDelay_Object((1,3,6,1,4,1,28507,6,1,2,2,1,6),_Epc2x6PortStartupDelay_Type())
epc2x6PortStartupDelay.setMaxAccess(_G)
if mibBuilder.loadTexts:epc2x6PortStartupDelay.setStatus(_B)
if mibBuilder.loadTexts:epc2x6PortStartupDelay.setUnits(_P)
class _Epc2x6PortRepowerTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Epc2x6PortRepowerTime_Type.__name__=_F
_Epc2x6PortRepowerTime_Object=MibTableColumn
epc2x6PortRepowerTime=_Epc2x6PortRepowerTime_Object((1,3,6,1,4,1,28507,6,1,2,2,1,7),_Epc2x6PortRepowerTime_Type())
epc2x6PortRepowerTime.setMaxAccess(_G)
if mibBuilder.loadTexts:epc2x6PortRepowerTime.setStatus(_B)
if mibBuilder.loadTexts:epc2x6PortRepowerTime.setUnits(_P)
class _Epc2x6portFuses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Epc2x6portFuses_Type.__name__=_F
_Epc2x6portFuses_Object=MibScalar
epc2x6portFuses=_Epc2x6portFuses_Object((1,3,6,1,4,1,28507,6,1,2,3),_Epc2x6portFuses_Type())
epc2x6portFuses.setMaxAccess(_H)
if mibBuilder.loadTexts:epc2x6portFuses.setStatus(_B)
_Epc2x6Temperature_Type=Integer32
_Epc2x6Temperature_Object=MibScalar
epc2x6Temperature=_Epc2x6Temperature_Object((1,3,6,1,4,1,28507,6,1,3),_Epc2x6Temperature_Type())
epc2x6Temperature.setMaxAccess(_H)
if mibBuilder.loadTexts:epc2x6Temperature.setStatus(_B)
if mibBuilder.loadTexts:epc2x6Temperature.setUnits('10th of degree Celsius')
_Epc2x6Conf_ObjectIdentity=ObjectIdentity
epc2x6Conf=_Epc2x6Conf_ObjectIdentity((1,3,6,1,4,1,28507,6,3))
_Epc2x6Groups_ObjectIdentity=ObjectIdentity
epc2x6Groups=_Epc2x6Groups_ObjectIdentity((1,3,6,1,4,1,28507,6,3,1))
_Epc2x6Compls_ObjectIdentity=ObjectIdentity
epc2x6Compls=_Epc2x6Compls_ObjectIdentity((1,3,6,1,4,1,28507,6,3,2))
epc2x6BasicGroup=ObjectGroup((1,3,6,1,4,1,28507,6,3,1,1))
epc2x6BasicGroup.setObjects(*((_A,_Q),(_A,_C),(_A,_D),(_A,_E),(_A,_R),(_A,_S),(_A,_T),(_A,_I),(_A,_J),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:epc2x6BasicGroup.setStatus(_B)
epc2x6witchEvt1=NotificationType((1,3,6,1,4,1,28507,0,1))
epc2x6witchEvt1.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:epc2x6witchEvt1.setStatus(_B)
epc2x6witchEvt2=NotificationType((1,3,6,1,4,1,28507,0,2))
epc2x6witchEvt2.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:epc2x6witchEvt2.setStatus(_B)
epc2x6witchEvt3=NotificationType((1,3,6,1,4,1,28507,0,3))
epc2x6witchEvt3.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:epc2x6witchEvt3.setStatus(_B)
epc2x6witchEvt4=NotificationType((1,3,6,1,4,1,28507,0,4))
epc2x6witchEvt4.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:epc2x6witchEvt4.setStatus(_B)
epc2x6witchEvt5=NotificationType((1,3,6,1,4,1,28507,0,5))
epc2x6witchEvt5.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:epc2x6witchEvt5.setStatus(_B)
epc2x6witchEvt6=NotificationType((1,3,6,1,4,1,28507,0,6))
epc2x6witchEvt6.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:epc2x6witchEvt6.setStatus(_B)
epc2x6witchEvt7=NotificationType((1,3,6,1,4,1,28507,0,7))
epc2x6witchEvt7.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:epc2x6witchEvt7.setStatus(_B)
epc2x6witchEvt8=NotificationType((1,3,6,1,4,1,28507,0,8))
epc2x6witchEvt8.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:epc2x6witchEvt8.setStatus(_B)
epc2x6witchEvt9=NotificationType((1,3,6,1,4,1,28507,0,9))
epc2x6witchEvt9.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:epc2x6witchEvt9.setStatus(_B)
epc2x6witchEvt10=NotificationType((1,3,6,1,4,1,28507,0,10))
epc2x6witchEvt10.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:epc2x6witchEvt10.setStatus(_B)
epc2x6witchEvt11=NotificationType((1,3,6,1,4,1,28507,0,11))
epc2x6witchEvt11.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:epc2x6witchEvt11.setStatus(_B)
epc2x6witchEvt12=NotificationType((1,3,6,1,4,1,28507,0,12))
epc2x6witchEvt12.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:epc2x6witchEvt12.setStatus(_B)
epc2x6FuseEvt=NotificationType((1,3,6,1,4,1,28507,0,13))
epc2x6FuseEvt.setObjects((_A,_J))
if mibBuilder.loadTexts:epc2x6FuseEvt.setStatus(_B)
epc2x6TempEvt=NotificationType((1,3,6,1,4,1,28507,0,14))
epc2x6TempEvt.setObjects((_A,_I))
if mibBuilder.loadTexts:epc2x6TempEvt.setStatus(_B)
epc2x6NotificationGroup=NotificationGroup((1,3,6,1,4,1,28507,6,3,1,2))
epc2x6NotificationGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:epc2x6NotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'gudeads':gudeads,'events':events,_X:epc2x6witchEvt1,_Y:epc2x6witchEvt2,_Z:epc2x6witchEvt3,_a:epc2x6witchEvt4,_b:epc2x6witchEvt5,_c:epc2x6witchEvt6,_d:epc2x6witchEvt7,_e:epc2x6witchEvt8,_f:epc2x6witchEvt9,_g:epc2x6witchEvt10,_h:epc2x6witchEvt11,_i:epc2x6witchEvt12,_k:epc2x6FuseEvt,_j:epc2x6TempEvt,'gadsEPC2x6':gadsEPC2x6,'epc2x6Objects':epc2x6Objects,'epc2x6SNMPaccess':epc2x6SNMPaccess,_R:epc2x6TrapCtrl,'epc2x6TrapIPTable':epc2x6TrapIPTable,'epc2x6TrapIPEntry':epc2x6TrapIPEntry,_M:epc2x6TrapIPIndex,_S:epc2x6TrapIPAddr,_T:epc2x6TrapIPPort,'epc2x6powerports':epc2x6powerports,_Q:epc2x6portNumber,'epc2x6portTable':epc2x6portTable,'epc2x6portEntry':epc2x6portEntry,_O:epc2x6PortIndex,_C:epc2x6PortName,_D:epc2x6PortState,_E:epc2x6PortSwitchCount,_U:epc2x6PortStartupMode,_V:epc2x6PortStartupDelay,_W:epc2x6PortRepowerTime,_J:epc2x6portFuses,_I:epc2x6Temperature,'epc2x6Conf':epc2x6Conf,'epc2x6Groups':epc2x6Groups,'epc2x6BasicGroup':epc2x6BasicGroup,'epc2x6NotificationGroup':epc2x6NotificationGroup,'epc2x6Compls':epc2x6Compls})