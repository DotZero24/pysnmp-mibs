_I='acModularGWAnalogPortIndex'
_H='acModularGWTrunkIndex'
_G='acModularGWModuleIndex'
_F='not-accessible'
_E='AC-ModularGW-MIB'
_D='current'
_C='read-only'
_B='deprecated'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TAddress','TextualConvention')
acModularGateway=ModuleIdentity((1,3,6,1,4,1,5003,9,10,11))
_AudioCodes_ObjectIdentity=ObjectIdentity
audioCodes=_AudioCodes_ObjectIdentity((1,3,6,1,4,1,5003))
_AcRegistrations_ObjectIdentity=ObjectIdentity
acRegistrations=_AcRegistrations_ObjectIdentity((1,3,6,1,4,1,5003,7))
_AcGeneric_ObjectIdentity=ObjectIdentity
acGeneric=_AcGeneric_ObjectIdentity((1,3,6,1,4,1,5003,8))
_AcProducts_ObjectIdentity=ObjectIdentity
acProducts=_AcProducts_ObjectIdentity((1,3,6,1,4,1,5003,9))
_AcBoardMibs_ObjectIdentity=ObjectIdentity
acBoardMibs=_AcBoardMibs_ObjectIdentity((1,3,6,1,4,1,5003,9,10))
_AcModularGatewayConfiguration_ObjectIdentity=ObjectIdentity
acModularGatewayConfiguration=_AcModularGatewayConfiguration_ObjectIdentity((1,3,6,1,4,1,5003,9,10,11,1))
_AcModularGatewayStatus_ObjectIdentity=ObjectIdentity
acModularGatewayStatus=_AcModularGatewayStatus_ObjectIdentity((1,3,6,1,4,1,5003,9,10,11,2))
_AcModularGWModules_ObjectIdentity=ObjectIdentity
acModularGWModules=_AcModularGWModules_ObjectIdentity((1,3,6,1,4,1,5003,9,10,11,2,1))
_AcModularGWModuleTable_Object=MibTable
acModularGWModuleTable=_AcModularGWModuleTable_Object((1,3,6,1,4,1,5003,9,10,11,2,1,20))
if mibBuilder.loadTexts:acModularGWModuleTable.setStatus(_D)
_AcModularGWModuleEntry_Object=MibTableRow
acModularGWModuleEntry=_AcModularGWModuleEntry_Object((1,3,6,1,4,1,5003,9,10,11,2,1,20,1))
acModularGWModuleEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:acModularGWModuleEntry.setStatus(_D)
class _AcModularGWModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_AcModularGWModuleIndex_Type.__name__=_A
_AcModularGWModuleIndex_Object=MibTableColumn
acModularGWModuleIndex=_AcModularGWModuleIndex_Object((1,3,6,1,4,1,5003,9,10,11,2,1,20,1,1),_AcModularGWModuleIndex_Type())
acModularGWModuleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:acModularGWModuleIndex.setStatus(_B)
class _AcModularGWModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4)));namedValues=NamedValues(*(('e1-t1-QUAD',0),('fxs',1),('fxo',2),('e1-t1-FALC56',4)))
_AcModularGWModuleType_Type.__name__=_A
_AcModularGWModuleType_Object=MibTableColumn
acModularGWModuleType=_AcModularGWModuleType_Object((1,3,6,1,4,1,5003,9,10,11,2,1,20,1,2),_AcModularGWModuleType_Type())
acModularGWModuleType.setMaxAccess(_C)
if mibBuilder.loadTexts:acModularGWModuleType.setStatus(_B)
class _AcModularGWModuleNumOfPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AcModularGWModuleNumOfPorts_Type.__name__=_A
_AcModularGWModuleNumOfPorts_Object=MibTableColumn
acModularGWModuleNumOfPorts=_AcModularGWModuleNumOfPorts_Object((1,3,6,1,4,1,5003,9,10,11,2,1,20,1,3),_AcModularGWModuleNumOfPorts_Type())
acModularGWModuleNumOfPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:acModularGWModuleNumOfPorts.setStatus(_B)
class _AcModularGWModuleFirstPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,19))
_AcModularGWModuleFirstPortNum_Type.__name__=_A
_AcModularGWModuleFirstPortNum_Object=MibTableColumn
acModularGWModuleFirstPortNum=_AcModularGWModuleFirstPortNum_Object((1,3,6,1,4,1,5003,9,10,11,2,1,20,1,4),_AcModularGWModuleFirstPortNum_Type())
acModularGWModuleFirstPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:acModularGWModuleFirstPortNum.setStatus(_B)
_AcModularGWCrossReference_ObjectIdentity=ObjectIdentity
acModularGWCrossReference=_AcModularGWCrossReference_ObjectIdentity((1,3,6,1,4,1,5003,9,10,11,2,2))
_AcModularGWTrunkTable_Object=MibTable
acModularGWTrunkTable=_AcModularGWTrunkTable_Object((1,3,6,1,4,1,5003,9,10,11,2,2,20))
if mibBuilder.loadTexts:acModularGWTrunkTable.setStatus(_D)
_AcModularGWTrunkEntry_Object=MibTableRow
acModularGWTrunkEntry=_AcModularGWTrunkEntry_Object((1,3,6,1,4,1,5003,9,10,11,2,2,20,1))
acModularGWTrunkEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:acModularGWTrunkEntry.setStatus(_D)
class _AcModularGWTrunkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_AcModularGWTrunkIndex_Type.__name__=_A
_AcModularGWTrunkIndex_Object=MibTableColumn
acModularGWTrunkIndex=_AcModularGWTrunkIndex_Object((1,3,6,1,4,1,5003,9,10,11,2,2,20,1,1),_AcModularGWTrunkIndex_Type())
acModularGWTrunkIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:acModularGWTrunkIndex.setStatus(_B)
class _AcModularGWTrunkOnModuleNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_AcModularGWTrunkOnModuleNum_Type.__name__=_A
_AcModularGWTrunkOnModuleNum_Object=MibTableColumn
acModularGWTrunkOnModuleNum=_AcModularGWTrunkOnModuleNum_Object((1,3,6,1,4,1,5003,9,10,11,2,2,20,1,2),_AcModularGWTrunkOnModuleNum_Type())
acModularGWTrunkOnModuleNum.setMaxAccess(_C)
if mibBuilder.loadTexts:acModularGWTrunkOnModuleNum.setStatus(_B)
class _AcModularGWTrunkOnPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AcModularGWTrunkOnPortNum_Type.__name__=_A
_AcModularGWTrunkOnPortNum_Object=MibTableColumn
acModularGWTrunkOnPortNum=_AcModularGWTrunkOnPortNum_Object((1,3,6,1,4,1,5003,9,10,11,2,2,20,1,3),_AcModularGWTrunkOnPortNum_Type())
acModularGWTrunkOnPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:acModularGWTrunkOnPortNum.setStatus(_B)
_AcModularGWAnalogPortTable_Object=MibTable
acModularGWAnalogPortTable=_AcModularGWAnalogPortTable_Object((1,3,6,1,4,1,5003,9,10,11,2,2,21))
if mibBuilder.loadTexts:acModularGWAnalogPortTable.setStatus(_D)
_AcModularGWAnalogPortEntry_Object=MibTableRow
acModularGWAnalogPortEntry=_AcModularGWAnalogPortEntry_Object((1,3,6,1,4,1,5003,9,10,11,2,2,21,1))
acModularGWAnalogPortEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:acModularGWAnalogPortEntry.setStatus(_D)
class _AcModularGWAnalogPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_AcModularGWAnalogPortIndex_Type.__name__=_A
_AcModularGWAnalogPortIndex_Object=MibTableColumn
acModularGWAnalogPortIndex=_AcModularGWAnalogPortIndex_Object((1,3,6,1,4,1,5003,9,10,11,2,2,21,1,1),_AcModularGWAnalogPortIndex_Type())
acModularGWAnalogPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:acModularGWAnalogPortIndex.setStatus(_B)
class _AcModularGWAnalogPortOnModuleNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_AcModularGWAnalogPortOnModuleNum_Type.__name__=_A
_AcModularGWAnalogPortOnModuleNum_Object=MibTableColumn
acModularGWAnalogPortOnModuleNum=_AcModularGWAnalogPortOnModuleNum_Object((1,3,6,1,4,1,5003,9,10,11,2,2,21,1,2),_AcModularGWAnalogPortOnModuleNum_Type())
acModularGWAnalogPortOnModuleNum.setMaxAccess(_C)
if mibBuilder.loadTexts:acModularGWAnalogPortOnModuleNum.setStatus(_B)
class _AcModularGWAnalogPortOnPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AcModularGWAnalogPortOnPortNum_Type.__name__=_A
_AcModularGWAnalogPortOnPortNum_Object=MibTableColumn
acModularGWAnalogPortOnPortNum=_AcModularGWAnalogPortOnPortNum_Object((1,3,6,1,4,1,5003,9,10,11,2,2,21,1,3),_AcModularGWAnalogPortOnPortNum_Type())
acModularGWAnalogPortOnPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:acModularGWAnalogPortOnPortNum.setStatus(_B)
_AcModularGatewayAction_ObjectIdentity=ObjectIdentity
acModularGatewayAction=_AcModularGatewayAction_ObjectIdentity((1,3,6,1,4,1,5003,9,10,11,3))
mibBuilder.exportSymbols(_E,**{'audioCodes':audioCodes,'acRegistrations':acRegistrations,'acGeneric':acGeneric,'acProducts':acProducts,'acBoardMibs':acBoardMibs,'acModularGateway':acModularGateway,'acModularGatewayConfiguration':acModularGatewayConfiguration,'acModularGatewayStatus':acModularGatewayStatus,'acModularGWModules':acModularGWModules,'acModularGWModuleTable':acModularGWModuleTable,'acModularGWModuleEntry':acModularGWModuleEntry,_G:acModularGWModuleIndex,'acModularGWModuleType':acModularGWModuleType,'acModularGWModuleNumOfPorts':acModularGWModuleNumOfPorts,'acModularGWModuleFirstPortNum':acModularGWModuleFirstPortNum,'acModularGWCrossReference':acModularGWCrossReference,'acModularGWTrunkTable':acModularGWTrunkTable,'acModularGWTrunkEntry':acModularGWTrunkEntry,_H:acModularGWTrunkIndex,'acModularGWTrunkOnModuleNum':acModularGWTrunkOnModuleNum,'acModularGWTrunkOnPortNum':acModularGWTrunkOnPortNum,'acModularGWAnalogPortTable':acModularGWAnalogPortTable,'acModularGWAnalogPortEntry':acModularGWAnalogPortEntry,_I:acModularGWAnalogPortIndex,'acModularGWAnalogPortOnModuleNum':acModularGWAnalogPortOnModuleNum,'acModularGWAnalogPortOnPortNum':acModularGWAnalogPortOnPortNum,'acModularGatewayAction':acModularGatewayAction})