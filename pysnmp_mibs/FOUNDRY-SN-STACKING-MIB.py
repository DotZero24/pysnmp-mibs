_c='snStackingNeighborPortStackPort'
_b='snStackingNeighborPortUnit'
_a='snStackingConfigPeriTrunkPort2'
_Z='snStackingConfigPeriTrunkPort1'
_Y='snStackingConfigPeriTrunkUnit'
_X='snStackingConfigPeriPortPort'
_W='snStackingConfigPeriPortUnit'
_V='snStackingConfigStackTrunkPort2'
_U='snStackingConfigStackTrunkPort1'
_T='snStackingConfigStackTrunkUnit'
_S='snStackingOperUnitIndex'
_R='reserved'
_Q='remote'
_P='snStackingConfigUnitIndex'
_O='standalone'
_N='disabled'
_M='create'
_L='enabled'
_K='delete'
_J='valid'
_I='DisplayString'
_H='other'
_G='not-accessible'
_F='FOUNDRY-SN-STACKING-MIB'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='deprecated'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayString,=mibBuilder.importSymbols('FOUNDRY-SN-AGENT-MIB',_I)
snSwitch,=mibBuilder.importSymbols('FOUNDRY-SN-SWITCH-GROUP-MIB','snSwitch')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'MacAddress','PhysAddress','TextualConvention')
snStacking=ModuleIdentity((1,3,6,1,4,1,1991,1,1,3,31))
if mibBuilder.loadTexts:snStacking.setRevisions(('2008-05-05 00:00','2017-08-07 00:00','2018-09-06 00:00'))
_SnStackingGlobalObjects_ObjectIdentity=ObjectIdentity
snStackingGlobalObjects=_SnStackingGlobalObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,31,1))
class _SnStackingGlobalConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),(_L,1),(_N,2)))
_SnStackingGlobalConfigState_Type.__name__=_D
_SnStackingGlobalConfigState_Object=MibScalar
snStackingGlobalConfigState=_SnStackingGlobalConfigState_Object((1,3,6,1,4,1,1991,1,1,3,31,1,1),_SnStackingGlobalConfigState_Type())
snStackingGlobalConfigState.setMaxAccess(_E)
if mibBuilder.loadTexts:snStackingGlobalConfigState.setStatus(_A)
_SnStackingGlobalMacAddress_Type=MacAddress
_SnStackingGlobalMacAddress_Object=MibScalar
snStackingGlobalMacAddress=_SnStackingGlobalMacAddress_Object((1,3,6,1,4,1,1991,1,1,3,31,1,2),_SnStackingGlobalMacAddress_Type())
snStackingGlobalMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:snStackingGlobalMacAddress.setStatus(_A)
class _SnStackingGlobalPersistentMacTimerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_N,1)))
_SnStackingGlobalPersistentMacTimerState_Type.__name__=_D
_SnStackingGlobalPersistentMacTimerState_Object=MibScalar
snStackingGlobalPersistentMacTimerState=_SnStackingGlobalPersistentMacTimerState_Object((1,3,6,1,4,1,1991,1,1,3,31,1,3),_SnStackingGlobalPersistentMacTimerState_Type())
snStackingGlobalPersistentMacTimerState.setMaxAccess(_E)
if mibBuilder.loadTexts:snStackingGlobalPersistentMacTimerState.setStatus(_B)
_SnStackingGlobalPersistentMacTimer_Type=Integer32
_SnStackingGlobalPersistentMacTimer_Object=MibScalar
snStackingGlobalPersistentMacTimer=_SnStackingGlobalPersistentMacTimer_Object((1,3,6,1,4,1,1991,1,1,3,31,1,4),_SnStackingGlobalPersistentMacTimer_Type())
snStackingGlobalPersistentMacTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:snStackingGlobalPersistentMacTimer.setStatus(_B)
class _SnStackingGlobalTopology_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('chain',2),('ring',3),(_O,4)))
_SnStackingGlobalTopology_Type.__name__=_D
_SnStackingGlobalTopology_Object=MibScalar
snStackingGlobalTopology=_SnStackingGlobalTopology_Object((1,3,6,1,4,1,1991,1,1,3,31,1,5),_SnStackingGlobalTopology_Type())
snStackingGlobalTopology.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingGlobalTopology.setStatus(_A)
class _SnStackingGlobalMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stackingMode',1),('nonStackingMode',2)))
_SnStackingGlobalMode_Type.__name__=_D
_SnStackingGlobalMode_Object=MibScalar
snStackingGlobalMode=_SnStackingGlobalMode_Object((1,3,6,1,4,1,1991,1,1,3,31,1,6),_SnStackingGlobalMode_Type())
snStackingGlobalMode.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingGlobalMode.setStatus(_A)
class _SnStackingGlobalMixedMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mixedStackingMode',1),('classicStackingMode',2)))
_SnStackingGlobalMixedMode_Type.__name__=_D
_SnStackingGlobalMixedMode_Object=MibScalar
snStackingGlobalMixedMode=_SnStackingGlobalMixedMode_Object((1,3,6,1,4,1,1991,1,1,3,31,1,7),_SnStackingGlobalMixedMode_Type())
snStackingGlobalMixedMode.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingGlobalMixedMode.setStatus(_A)
_SnStackingGlobalMaxUnitNumber_Type=Integer32
_SnStackingGlobalMaxUnitNumber_Object=MibScalar
snStackingGlobalMaxUnitNumber=_SnStackingGlobalMaxUnitNumber_Object((1,3,6,1,4,1,1991,1,1,3,31,1,8),_SnStackingGlobalMaxUnitNumber_Type())
snStackingGlobalMaxUnitNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingGlobalMaxUnitNumber.setStatus(_A)
_SnStackingGlobalHighestPriority_Type=Integer32
_SnStackingGlobalHighestPriority_Object=MibScalar
snStackingGlobalHighestPriority=_SnStackingGlobalHighestPriority_Object((1,3,6,1,4,1,1991,1,1,3,31,1,9),_SnStackingGlobalHighestPriority_Type())
snStackingGlobalHighestPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingGlobalHighestPriority.setStatus(_A)
class _SnStackingGlobalZeroTouchEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),(_L,1)))
_SnStackingGlobalZeroTouchEnable_Type.__name__=_D
_SnStackingGlobalZeroTouchEnable_Object=MibScalar
snStackingGlobalZeroTouchEnable=_SnStackingGlobalZeroTouchEnable_Object((1,3,6,1,4,1,1991,1,1,3,31,1,10),_SnStackingGlobalZeroTouchEnable_Type())
snStackingGlobalZeroTouchEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:snStackingGlobalZeroTouchEnable.setStatus(_A)
_SnStackingTableObjects_ObjectIdentity=ObjectIdentity
snStackingTableObjects=_SnStackingTableObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,31,2))
_SnStackingConfigUnitTable_Object=MibTable
snStackingConfigUnitTable=_SnStackingConfigUnitTable_Object((1,3,6,1,4,1,1991,1,1,3,31,2,1))
if mibBuilder.loadTexts:snStackingConfigUnitTable.setStatus(_A)
_SnStackingConfigUnitEntry_Object=MibTableRow
snStackingConfigUnitEntry=_SnStackingConfigUnitEntry_Object((1,3,6,1,4,1,1991,1,1,3,31,2,1,1))
snStackingConfigUnitEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:snStackingConfigUnitEntry.setStatus(_A)
_SnStackingConfigUnitIndex_Type=Integer32
_SnStackingConfigUnitIndex_Object=MibTableColumn
snStackingConfigUnitIndex=_SnStackingConfigUnitIndex_Object((1,3,6,1,4,1,1991,1,1,3,31,2,1,1,1),_SnStackingConfigUnitIndex_Type())
snStackingConfigUnitIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:snStackingConfigUnitIndex.setStatus(_A)
class _SnStackingConfigUnitPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnStackingConfigUnitPriority_Type.__name__=_D
_SnStackingConfigUnitPriority_Object=MibTableColumn
snStackingConfigUnitPriority=_SnStackingConfigUnitPriority_Object((1,3,6,1,4,1,1991,1,1,3,31,2,1,1,2),_SnStackingConfigUnitPriority_Type())
snStackingConfigUnitPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:snStackingConfigUnitPriority.setStatus(_A)
_SnStackingConfigUnitConfigStackPort_Type=InterfaceIndexOrZero
_SnStackingConfigUnitConfigStackPort_Object=MibTableColumn
snStackingConfigUnitConfigStackPort=_SnStackingConfigUnitConfigStackPort_Object((1,3,6,1,4,1,1991,1,1,3,31,2,1,1,3),_SnStackingConfigUnitConfigStackPort_Type())
snStackingConfigUnitConfigStackPort.setMaxAccess(_E)
if mibBuilder.loadTexts:snStackingConfigUnitConfigStackPort.setStatus(_B)
class _SnStackingConfigUnitRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_J,2),(_K,3)))
_SnStackingConfigUnitRowStatus_Type.__name__=_D
_SnStackingConfigUnitRowStatus_Object=MibTableColumn
snStackingConfigUnitRowStatus=_SnStackingConfigUnitRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,31,2,1,1,4),_SnStackingConfigUnitRowStatus_Type())
snStackingConfigUnitRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:snStackingConfigUnitRowStatus.setStatus(_A)
_SnStackingConfigUnitType_Type=DisplayString
_SnStackingConfigUnitType_Object=MibTableColumn
snStackingConfigUnitType=_SnStackingConfigUnitType_Object((1,3,6,1,4,1,1991,1,1,3,31,2,1,1,5),_SnStackingConfigUnitType_Type())
snStackingConfigUnitType.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingConfigUnitType.setStatus(_A)
class _SnStackingConfigUnitState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('local',1),(_Q,2),(_R,3),('empty',4)))
_SnStackingConfigUnitState_Type.__name__=_D
_SnStackingConfigUnitState_Object=MibTableColumn
snStackingConfigUnitState=_SnStackingConfigUnitState_Object((1,3,6,1,4,1,1991,1,1,3,31,2,1,1,6),_SnStackingConfigUnitState_Type())
snStackingConfigUnitState.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingConfigUnitState.setStatus(_A)
_SnStackingConfigUnitStackPort1_Type=InterfaceIndexOrZero
_SnStackingConfigUnitStackPort1_Object=MibTableColumn
snStackingConfigUnitStackPort1=_SnStackingConfigUnitStackPort1_Object((1,3,6,1,4,1,1991,1,1,3,31,2,1,1,7),_SnStackingConfigUnitStackPort1_Type())
snStackingConfigUnitStackPort1.setMaxAccess(_E)
if mibBuilder.loadTexts:snStackingConfigUnitStackPort1.setStatus(_A)
_SnStackingConfigUnitStackPort2_Type=InterfaceIndexOrZero
_SnStackingConfigUnitStackPort2_Object=MibTableColumn
snStackingConfigUnitStackPort2=_SnStackingConfigUnitStackPort2_Object((1,3,6,1,4,1,1991,1,1,3,31,2,1,1,8),_SnStackingConfigUnitStackPort2_Type())
snStackingConfigUnitStackPort2.setMaxAccess(_E)
if mibBuilder.loadTexts:snStackingConfigUnitStackPort2.setStatus(_A)
_SnStackingConfigUnitConnectPort1_Type=InterfaceIndexOrZero
_SnStackingConfigUnitConnectPort1_Object=MibTableColumn
snStackingConfigUnitConnectPort1=_SnStackingConfigUnitConnectPort1_Object((1,3,6,1,4,1,1991,1,1,3,31,2,1,1,9),_SnStackingConfigUnitConnectPort1_Type())
snStackingConfigUnitConnectPort1.setMaxAccess(_E)
if mibBuilder.loadTexts:snStackingConfigUnitConnectPort1.setStatus(_B)
_SnStackingConfigUnitConnectPort2_Type=InterfaceIndexOrZero
_SnStackingConfigUnitConnectPort2_Object=MibTableColumn
snStackingConfigUnitConnectPort2=_SnStackingConfigUnitConnectPort2_Object((1,3,6,1,4,1,1991,1,1,3,31,2,1,1,10),_SnStackingConfigUnitConnectPort2_Type())
snStackingConfigUnitConnectPort2.setMaxAccess(_E)
if mibBuilder.loadTexts:snStackingConfigUnitConnectPort2.setStatus(_B)
_SnStackingConfigUnitStackTrunk1_Type=OctetString
_SnStackingConfigUnitStackTrunk1_Object=MibTableColumn
snStackingConfigUnitStackTrunk1=_SnStackingConfigUnitStackTrunk1_Object((1,3,6,1,4,1,1991,1,1,3,31,2,1,1,11),_SnStackingConfigUnitStackTrunk1_Type())
snStackingConfigUnitStackTrunk1.setMaxAccess(_E)
if mibBuilder.loadTexts:snStackingConfigUnitStackTrunk1.setStatus(_A)
_SnStackingConfigUnitStackTrunk2_Type=OctetString
_SnStackingConfigUnitStackTrunk2_Object=MibTableColumn
snStackingConfigUnitStackTrunk2=_SnStackingConfigUnitStackTrunk2_Object((1,3,6,1,4,1,1991,1,1,3,31,2,1,1,12),_SnStackingConfigUnitStackTrunk2_Type())
snStackingConfigUnitStackTrunk2.setMaxAccess(_E)
if mibBuilder.loadTexts:snStackingConfigUnitStackTrunk2.setStatus(_A)
class _SnStackingConfigUnitName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SnStackingConfigUnitName_Type.__name__=_I
_SnStackingConfigUnitName_Object=MibTableColumn
snStackingConfigUnitName=_SnStackingConfigUnitName_Object((1,3,6,1,4,1,1991,1,1,3,31,2,1,1,13),_SnStackingConfigUnitName_Type())
snStackingConfigUnitName.setMaxAccess(_E)
if mibBuilder.loadTexts:snStackingConfigUnitName.setStatus(_A)
_SnStackingOperUnitTable_Object=MibTable
snStackingOperUnitTable=_SnStackingOperUnitTable_Object((1,3,6,1,4,1,1991,1,1,3,31,2,2))
if mibBuilder.loadTexts:snStackingOperUnitTable.setStatus(_A)
_SnStackingOperUnitEntry_Object=MibTableRow
snStackingOperUnitEntry=_SnStackingOperUnitEntry_Object((1,3,6,1,4,1,1991,1,1,3,31,2,2,1))
snStackingOperUnitEntry.setIndexNames((0,_F,_S))
if mibBuilder.loadTexts:snStackingOperUnitEntry.setStatus(_A)
_SnStackingOperUnitIndex_Type=Integer32
_SnStackingOperUnitIndex_Object=MibTableColumn
snStackingOperUnitIndex=_SnStackingOperUnitIndex_Object((1,3,6,1,4,1,1991,1,1,3,31,2,2,1,1),_SnStackingOperUnitIndex_Type())
snStackingOperUnitIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:snStackingOperUnitIndex.setStatus(_A)
class _SnStackingOperUnitRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),('active',2),('standby',3),('member',4),(_O,5)))
_SnStackingOperUnitRole_Type.__name__=_D
_SnStackingOperUnitRole_Object=MibTableColumn
snStackingOperUnitRole=_SnStackingOperUnitRole_Object((1,3,6,1,4,1,1991,1,1,3,31,2,2,1,2),_SnStackingOperUnitRole_Type())
snStackingOperUnitRole.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingOperUnitRole.setStatus(_A)
_SnStackingOperUnitMac_Type=MacAddress
_SnStackingOperUnitMac_Object=MibTableColumn
snStackingOperUnitMac=_SnStackingOperUnitMac_Object((1,3,6,1,4,1,1991,1,1,3,31,2,2,1,3),_SnStackingOperUnitMac_Type())
snStackingOperUnitMac.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingOperUnitMac.setStatus(_A)
class _SnStackingOperUnitPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnStackingOperUnitPriority_Type.__name__=_D
_SnStackingOperUnitPriority_Object=MibTableColumn
snStackingOperUnitPriority=_SnStackingOperUnitPriority_Object((1,3,6,1,4,1,1991,1,1,3,31,2,2,1,4),_SnStackingOperUnitPriority_Type())
snStackingOperUnitPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingOperUnitPriority.setStatus(_A)
class _SnStackingOperUnitState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('local',1),(_Q,2),(_R,3),('empty',4)))
_SnStackingOperUnitState_Type.__name__=_D
_SnStackingOperUnitState_Object=MibTableColumn
snStackingOperUnitState=_SnStackingOperUnitState_Object((1,3,6,1,4,1,1991,1,1,3,31,2,2,1,5),_SnStackingOperUnitState_Type())
snStackingOperUnitState.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingOperUnitState.setStatus(_A)
class _SnStackingOperUnitDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SnStackingOperUnitDescription_Type.__name__=_I
_SnStackingOperUnitDescription_Object=MibTableColumn
snStackingOperUnitDescription=_SnStackingOperUnitDescription_Object((1,3,6,1,4,1,1991,1,1,3,31,2,2,1,6),_SnStackingOperUnitDescription_Type())
snStackingOperUnitDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingOperUnitDescription.setStatus(_A)
_SnStackingOperUnitStackPort1_Type=InterfaceIndexOrZero
_SnStackingOperUnitStackPort1_Object=MibTableColumn
snStackingOperUnitStackPort1=_SnStackingOperUnitStackPort1_Object((1,3,6,1,4,1,1991,1,1,3,31,2,2,1,7),_SnStackingOperUnitStackPort1_Type())
snStackingOperUnitStackPort1.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingOperUnitStackPort1.setStatus(_A)
class _SnStackingOperUnitStackPort1State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('up',2),('down',3)))
_SnStackingOperUnitStackPort1State_Type.__name__=_D
_SnStackingOperUnitStackPort1State_Object=MibTableColumn
snStackingOperUnitStackPort1State=_SnStackingOperUnitStackPort1State_Object((1,3,6,1,4,1,1991,1,1,3,31,2,2,1,8),_SnStackingOperUnitStackPort1State_Type())
snStackingOperUnitStackPort1State.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingOperUnitStackPort1State.setStatus(_A)
_SnStackingOperUnitStackPort2_Type=InterfaceIndexOrZero
_SnStackingOperUnitStackPort2_Object=MibTableColumn
snStackingOperUnitStackPort2=_SnStackingOperUnitStackPort2_Object((1,3,6,1,4,1,1991,1,1,3,31,2,2,1,9),_SnStackingOperUnitStackPort2_Type())
snStackingOperUnitStackPort2.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingOperUnitStackPort2.setStatus(_A)
class _SnStackingOperUnitStackPort2State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('up',2),('down',3)))
_SnStackingOperUnitStackPort2State_Type.__name__=_D
_SnStackingOperUnitStackPort2State_Object=MibTableColumn
snStackingOperUnitStackPort2State=_SnStackingOperUnitStackPort2State_Object((1,3,6,1,4,1,1991,1,1,3,31,2,2,1,10),_SnStackingOperUnitStackPort2State_Type())
snStackingOperUnitStackPort2State.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingOperUnitStackPort2State.setStatus(_A)
_SnStackingOperUnitNeighbor1_Type=Integer32
_SnStackingOperUnitNeighbor1_Object=MibTableColumn
snStackingOperUnitNeighbor1=_SnStackingOperUnitNeighbor1_Object((1,3,6,1,4,1,1991,1,1,3,31,2,2,1,11),_SnStackingOperUnitNeighbor1_Type())
snStackingOperUnitNeighbor1.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingOperUnitNeighbor1.setStatus(_A)
_SnStackingOperUnitNeighbor2_Type=Integer32
_SnStackingOperUnitNeighbor2_Object=MibTableColumn
snStackingOperUnitNeighbor2=_SnStackingOperUnitNeighbor2_Object((1,3,6,1,4,1,1991,1,1,3,31,2,2,1,12),_SnStackingOperUnitNeighbor2_Type())
snStackingOperUnitNeighbor2.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingOperUnitNeighbor2.setStatus(_A)
class _SnStackingOperUnitImgVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnStackingOperUnitImgVer_Type.__name__=_I
_SnStackingOperUnitImgVer_Object=MibTableColumn
snStackingOperUnitImgVer=_SnStackingOperUnitImgVer_Object((1,3,6,1,4,1,1991,1,1,3,31,2,2,1,13),_SnStackingOperUnitImgVer_Type())
snStackingOperUnitImgVer.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingOperUnitImgVer.setStatus(_A)
class _SnStackingOperUnitBuildlVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SnStackingOperUnitBuildlVer_Type.__name__=_I
_SnStackingOperUnitBuildlVer_Object=MibTableColumn
snStackingOperUnitBuildlVer=_SnStackingOperUnitBuildlVer_Object((1,3,6,1,4,1,1991,1,1,3,31,2,2,1,14),_SnStackingOperUnitBuildlVer_Type())
snStackingOperUnitBuildlVer.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingOperUnitBuildlVer.setStatus(_A)
_SnStackingConfigStackTrunkTable_Object=MibTable
snStackingConfigStackTrunkTable=_SnStackingConfigStackTrunkTable_Object((1,3,6,1,4,1,1991,1,1,3,31,2,3))
if mibBuilder.loadTexts:snStackingConfigStackTrunkTable.setStatus(_B)
_SnStackingConfigStackTrunkEntry_Object=MibTableRow
snStackingConfigStackTrunkEntry=_SnStackingConfigStackTrunkEntry_Object((1,3,6,1,4,1,1991,1,1,3,31,2,3,1))
snStackingConfigStackTrunkEntry.setIndexNames((0,_F,_T),(0,_F,_U),(0,_F,_V))
if mibBuilder.loadTexts:snStackingConfigStackTrunkEntry.setStatus(_B)
_SnStackingConfigStackTrunkUnit_Type=Integer32
_SnStackingConfigStackTrunkUnit_Object=MibTableColumn
snStackingConfigStackTrunkUnit=_SnStackingConfigStackTrunkUnit_Object((1,3,6,1,4,1,1991,1,1,3,31,2,3,1,1),_SnStackingConfigStackTrunkUnit_Type())
snStackingConfigStackTrunkUnit.setMaxAccess(_G)
if mibBuilder.loadTexts:snStackingConfigStackTrunkUnit.setStatus(_B)
_SnStackingConfigStackTrunkPort1_Type=InterfaceIndexOrZero
_SnStackingConfigStackTrunkPort1_Object=MibTableColumn
snStackingConfigStackTrunkPort1=_SnStackingConfigStackTrunkPort1_Object((1,3,6,1,4,1,1991,1,1,3,31,2,3,1,2),_SnStackingConfigStackTrunkPort1_Type())
snStackingConfigStackTrunkPort1.setMaxAccess(_G)
if mibBuilder.loadTexts:snStackingConfigStackTrunkPort1.setStatus(_B)
_SnStackingConfigStackTrunkPort2_Type=InterfaceIndexOrZero
_SnStackingConfigStackTrunkPort2_Object=MibTableColumn
snStackingConfigStackTrunkPort2=_SnStackingConfigStackTrunkPort2_Object((1,3,6,1,4,1,1991,1,1,3,31,2,3,1,3),_SnStackingConfigStackTrunkPort2_Type())
snStackingConfigStackTrunkPort2.setMaxAccess(_G)
if mibBuilder.loadTexts:snStackingConfigStackTrunkPort2.setStatus(_B)
class _SnStackingConfigStackTrunkRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_J,2),(_K,3),(_M,4)))
_SnStackingConfigStackTrunkRowStatus_Type.__name__=_D
_SnStackingConfigStackTrunkRowStatus_Object=MibTableColumn
snStackingConfigStackTrunkRowStatus=_SnStackingConfigStackTrunkRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,31,2,3,1,4),_SnStackingConfigStackTrunkRowStatus_Type())
snStackingConfigStackTrunkRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:snStackingConfigStackTrunkRowStatus.setStatus(_B)
_SnStackingConfigStackTrunkNumPort1_Type=Integer32
_SnStackingConfigStackTrunkNumPort1_Object=MibTableColumn
snStackingConfigStackTrunkNumPort1=_SnStackingConfigStackTrunkNumPort1_Object((1,3,6,1,4,1,1991,1,1,3,31,2,3,1,5),_SnStackingConfigStackTrunkNumPort1_Type())
snStackingConfigStackTrunkNumPort1.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingConfigStackTrunkNumPort1.setStatus(_B)
_SnStackingConfigStackTrunkNumPort2_Type=Integer32
_SnStackingConfigStackTrunkNumPort2_Object=MibTableColumn
snStackingConfigStackTrunkNumPort2=_SnStackingConfigStackTrunkNumPort2_Object((1,3,6,1,4,1,1991,1,1,3,31,2,3,1,6),_SnStackingConfigStackTrunkNumPort2_Type())
snStackingConfigStackTrunkNumPort2.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingConfigStackTrunkNumPort2.setStatus(_B)
_SnStackingConfigPeriPortTable_Object=MibTable
snStackingConfigPeriPortTable=_SnStackingConfigPeriPortTable_Object((1,3,6,1,4,1,1991,1,1,3,31,2,4))
if mibBuilder.loadTexts:snStackingConfigPeriPortTable.setStatus(_B)
_SnStackingConfigPeriPortEntry_Object=MibTableRow
snStackingConfigPeriPortEntry=_SnStackingConfigPeriPortEntry_Object((1,3,6,1,4,1,1991,1,1,3,31,2,4,1))
snStackingConfigPeriPortEntry.setIndexNames((0,_F,_W),(0,_F,_X))
if mibBuilder.loadTexts:snStackingConfigPeriPortEntry.setStatus(_B)
_SnStackingConfigPeriPortUnit_Type=Integer32
_SnStackingConfigPeriPortUnit_Object=MibTableColumn
snStackingConfigPeriPortUnit=_SnStackingConfigPeriPortUnit_Object((1,3,6,1,4,1,1991,1,1,3,31,2,4,1,1),_SnStackingConfigPeriPortUnit_Type())
snStackingConfigPeriPortUnit.setMaxAccess(_G)
if mibBuilder.loadTexts:snStackingConfigPeriPortUnit.setStatus(_B)
_SnStackingConfigPeriPortPort_Type=InterfaceIndexOrZero
_SnStackingConfigPeriPortPort_Object=MibTableColumn
snStackingConfigPeriPortPort=_SnStackingConfigPeriPortPort_Object((1,3,6,1,4,1,1991,1,1,3,31,2,4,1,2),_SnStackingConfigPeriPortPort_Type())
snStackingConfigPeriPortPort.setMaxAccess(_G)
if mibBuilder.loadTexts:snStackingConfigPeriPortPort.setStatus(_B)
class _SnStackingConfigPeriPortRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_J,2),(_K,3),(_M,4)))
_SnStackingConfigPeriPortRowStatus_Type.__name__=_D
_SnStackingConfigPeriPortRowStatus_Object=MibTableColumn
snStackingConfigPeriPortRowStatus=_SnStackingConfigPeriPortRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,31,2,4,1,3),_SnStackingConfigPeriPortRowStatus_Type())
snStackingConfigPeriPortRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:snStackingConfigPeriPortRowStatus.setStatus(_B)
_SnStackingConfigPeriTrunkTable_Object=MibTable
snStackingConfigPeriTrunkTable=_SnStackingConfigPeriTrunkTable_Object((1,3,6,1,4,1,1991,1,1,3,31,2,5))
if mibBuilder.loadTexts:snStackingConfigPeriTrunkTable.setStatus(_B)
_SnStackingConfigPeriTrunkEntry_Object=MibTableRow
snStackingConfigPeriTrunkEntry=_SnStackingConfigPeriTrunkEntry_Object((1,3,6,1,4,1,1991,1,1,3,31,2,5,1))
snStackingConfigPeriTrunkEntry.setIndexNames((0,_F,_Y),(0,_F,_Z),(0,_F,_a))
if mibBuilder.loadTexts:snStackingConfigPeriTrunkEntry.setStatus(_B)
_SnStackingConfigPeriTrunkUnit_Type=Integer32
_SnStackingConfigPeriTrunkUnit_Object=MibTableColumn
snStackingConfigPeriTrunkUnit=_SnStackingConfigPeriTrunkUnit_Object((1,3,6,1,4,1,1991,1,1,3,31,2,5,1,1),_SnStackingConfigPeriTrunkUnit_Type())
snStackingConfigPeriTrunkUnit.setMaxAccess(_G)
if mibBuilder.loadTexts:snStackingConfigPeriTrunkUnit.setStatus(_B)
_SnStackingConfigPeriTrunkPort1_Type=InterfaceIndexOrZero
_SnStackingConfigPeriTrunkPort1_Object=MibTableColumn
snStackingConfigPeriTrunkPort1=_SnStackingConfigPeriTrunkPort1_Object((1,3,6,1,4,1,1991,1,1,3,31,2,5,1,2),_SnStackingConfigPeriTrunkPort1_Type())
snStackingConfigPeriTrunkPort1.setMaxAccess(_G)
if mibBuilder.loadTexts:snStackingConfigPeriTrunkPort1.setStatus(_B)
_SnStackingConfigPeriTrunkPort2_Type=InterfaceIndexOrZero
_SnStackingConfigPeriTrunkPort2_Object=MibTableColumn
snStackingConfigPeriTrunkPort2=_SnStackingConfigPeriTrunkPort2_Object((1,3,6,1,4,1,1991,1,1,3,31,2,5,1,3),_SnStackingConfigPeriTrunkPort2_Type())
snStackingConfigPeriTrunkPort2.setMaxAccess(_G)
if mibBuilder.loadTexts:snStackingConfigPeriTrunkPort2.setStatus(_B)
class _SnStackingConfigPeriTrunkRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_J,2),(_K,3),(_M,4)))
_SnStackingConfigPeriTrunkRowStatus_Type.__name__=_D
_SnStackingConfigPeriTrunkRowStatus_Object=MibTableColumn
snStackingConfigPeriTrunkRowStatus=_SnStackingConfigPeriTrunkRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,31,2,5,1,4),_SnStackingConfigPeriTrunkRowStatus_Type())
snStackingConfigPeriTrunkRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:snStackingConfigPeriTrunkRowStatus.setStatus(_A)
_SnStackingNeighborPortTable_Object=MibTable
snStackingNeighborPortTable=_SnStackingNeighborPortTable_Object((1,3,6,1,4,1,1991,1,1,3,31,2,6))
if mibBuilder.loadTexts:snStackingNeighborPortTable.setStatus(_A)
_SnStackingNeighborPortEntry_Object=MibTableRow
snStackingNeighborPortEntry=_SnStackingNeighborPortEntry_Object((1,3,6,1,4,1,1991,1,1,3,31,2,6,1))
snStackingNeighborPortEntry.setIndexNames((0,_F,_b),(0,_F,_c))
if mibBuilder.loadTexts:snStackingNeighborPortEntry.setStatus(_A)
_SnStackingNeighborPortUnit_Type=Integer32
_SnStackingNeighborPortUnit_Object=MibTableColumn
snStackingNeighborPortUnit=_SnStackingNeighborPortUnit_Object((1,3,6,1,4,1,1991,1,1,3,31,2,6,1,1),_SnStackingNeighborPortUnit_Type())
snStackingNeighborPortUnit.setMaxAccess(_G)
if mibBuilder.loadTexts:snStackingNeighborPortUnit.setStatus(_A)
_SnStackingNeighborPortStackPort_Type=InterfaceIndexOrZero
_SnStackingNeighborPortStackPort_Object=MibTableColumn
snStackingNeighborPortStackPort=_SnStackingNeighborPortStackPort_Object((1,3,6,1,4,1,1991,1,1,3,31,2,6,1,2),_SnStackingNeighborPortStackPort_Type())
snStackingNeighborPortStackPort.setMaxAccess(_G)
if mibBuilder.loadTexts:snStackingNeighborPortStackPort.setStatus(_A)
_SnStackingNeighborPortNeighborPort_Type=InterfaceIndexOrZero
_SnStackingNeighborPortNeighborPort_Object=MibTableColumn
snStackingNeighborPortNeighborPort=_SnStackingNeighborPortNeighborPort_Object((1,3,6,1,4,1,1991,1,1,3,31,2,6,1,3),_SnStackingNeighborPortNeighborPort_Type())
snStackingNeighborPortNeighborPort.setMaxAccess(_C)
if mibBuilder.loadTexts:snStackingNeighborPortNeighborPort.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'snStacking':snStacking,'snStackingGlobalObjects':snStackingGlobalObjects,'snStackingGlobalConfigState':snStackingGlobalConfigState,'snStackingGlobalMacAddress':snStackingGlobalMacAddress,'snStackingGlobalPersistentMacTimerState':snStackingGlobalPersistentMacTimerState,'snStackingGlobalPersistentMacTimer':snStackingGlobalPersistentMacTimer,'snStackingGlobalTopology':snStackingGlobalTopology,'snStackingGlobalMode':snStackingGlobalMode,'snStackingGlobalMixedMode':snStackingGlobalMixedMode,'snStackingGlobalMaxUnitNumber':snStackingGlobalMaxUnitNumber,'snStackingGlobalHighestPriority':snStackingGlobalHighestPriority,'snStackingGlobalZeroTouchEnable':snStackingGlobalZeroTouchEnable,'snStackingTableObjects':snStackingTableObjects,'snStackingConfigUnitTable':snStackingConfigUnitTable,'snStackingConfigUnitEntry':snStackingConfigUnitEntry,_P:snStackingConfigUnitIndex,'snStackingConfigUnitPriority':snStackingConfigUnitPriority,'snStackingConfigUnitConfigStackPort':snStackingConfigUnitConfigStackPort,'snStackingConfigUnitRowStatus':snStackingConfigUnitRowStatus,'snStackingConfigUnitType':snStackingConfigUnitType,'snStackingConfigUnitState':snStackingConfigUnitState,'snStackingConfigUnitStackPort1':snStackingConfigUnitStackPort1,'snStackingConfigUnitStackPort2':snStackingConfigUnitStackPort2,'snStackingConfigUnitConnectPort1':snStackingConfigUnitConnectPort1,'snStackingConfigUnitConnectPort2':snStackingConfigUnitConnectPort2,'snStackingConfigUnitStackTrunk1':snStackingConfigUnitStackTrunk1,'snStackingConfigUnitStackTrunk2':snStackingConfigUnitStackTrunk2,'snStackingConfigUnitName':snStackingConfigUnitName,'snStackingOperUnitTable':snStackingOperUnitTable,'snStackingOperUnitEntry':snStackingOperUnitEntry,_S:snStackingOperUnitIndex,'snStackingOperUnitRole':snStackingOperUnitRole,'snStackingOperUnitMac':snStackingOperUnitMac,'snStackingOperUnitPriority':snStackingOperUnitPriority,'snStackingOperUnitState':snStackingOperUnitState,'snStackingOperUnitDescription':snStackingOperUnitDescription,'snStackingOperUnitStackPort1':snStackingOperUnitStackPort1,'snStackingOperUnitStackPort1State':snStackingOperUnitStackPort1State,'snStackingOperUnitStackPort2':snStackingOperUnitStackPort2,'snStackingOperUnitStackPort2State':snStackingOperUnitStackPort2State,'snStackingOperUnitNeighbor1':snStackingOperUnitNeighbor1,'snStackingOperUnitNeighbor2':snStackingOperUnitNeighbor2,'snStackingOperUnitImgVer':snStackingOperUnitImgVer,'snStackingOperUnitBuildlVer':snStackingOperUnitBuildlVer,'snStackingConfigStackTrunkTable':snStackingConfigStackTrunkTable,'snStackingConfigStackTrunkEntry':snStackingConfigStackTrunkEntry,_T:snStackingConfigStackTrunkUnit,_U:snStackingConfigStackTrunkPort1,_V:snStackingConfigStackTrunkPort2,'snStackingConfigStackTrunkRowStatus':snStackingConfigStackTrunkRowStatus,'snStackingConfigStackTrunkNumPort1':snStackingConfigStackTrunkNumPort1,'snStackingConfigStackTrunkNumPort2':snStackingConfigStackTrunkNumPort2,'snStackingConfigPeriPortTable':snStackingConfigPeriPortTable,'snStackingConfigPeriPortEntry':snStackingConfigPeriPortEntry,_W:snStackingConfigPeriPortUnit,_X:snStackingConfigPeriPortPort,'snStackingConfigPeriPortRowStatus':snStackingConfigPeriPortRowStatus,'snStackingConfigPeriTrunkTable':snStackingConfigPeriTrunkTable,'snStackingConfigPeriTrunkEntry':snStackingConfigPeriTrunkEntry,_Y:snStackingConfigPeriTrunkUnit,_Z:snStackingConfigPeriTrunkPort1,_a:snStackingConfigPeriTrunkPort2,'snStackingConfigPeriTrunkRowStatus':snStackingConfigPeriTrunkRowStatus,'snStackingNeighborPortTable':snStackingNeighborPortTable,'snStackingNeighborPortEntry':snStackingNeighborPortEntry,_b:snStackingNeighborPortUnit,_c:snStackingNeighborPortStackPort,'snStackingNeighborPortNeighborPort':snStackingNeighborPortNeighborPort})