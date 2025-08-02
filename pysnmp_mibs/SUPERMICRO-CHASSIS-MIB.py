_N='mbsmLCConfigCardName'
_M='mbsmSlotModuleStatus'
_L='mbsmSlotModuleType'
_K='mbsmLCConfigSlotId'
_J='mbsmLCPortIndex'
_I='DisplayString'
_H='mbsmLCIndex'
_G='not-accessible'
_F='mbsmSlotId'
_E='read-create'
_D='read-write'
_C='SUPERMICRO-CHASSIS-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
mbsmIssGroup=ModuleIdentity((1,3,6,1,4,1,10876,101,1,81,100))
if mibBuilder.loadTexts:mbsmIssGroup.setRevisions(('2012-09-05 00:00',))
_MbsmIssScalarGroup_ObjectIdentity=ObjectIdentity
mbsmIssScalarGroup=_MbsmIssScalarGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,81,100,1))
class _MbsmMaxNumOfLCSlots_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MbsmMaxNumOfLCSlots_Type.__name__=_B
_MbsmMaxNumOfLCSlots_Object=MibScalar
mbsmMaxNumOfLCSlots=_MbsmMaxNumOfLCSlots_Object((1,3,6,1,4,1,10876,101,1,81,100,1,1),_MbsmMaxNumOfLCSlots_Type())
mbsmMaxNumOfLCSlots.setMaxAccess(_D)
if mibBuilder.loadTexts:mbsmMaxNumOfLCSlots.setStatus(_A)
class _MbsmMaxNumOfSlots_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MbsmMaxNumOfSlots_Type.__name__=_B
_MbsmMaxNumOfSlots_Object=MibScalar
mbsmMaxNumOfSlots=_MbsmMaxNumOfSlots_Object((1,3,6,1,4,1,10876,101,1,81,100,1,2),_MbsmMaxNumOfSlots_Type())
mbsmMaxNumOfSlots.setMaxAccess(_D)
if mibBuilder.loadTexts:mbsmMaxNumOfSlots.setStatus(_A)
class _MbsmMaxNumOfPortsPerLC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MbsmMaxNumOfPortsPerLC_Type.__name__=_B
_MbsmMaxNumOfPortsPerLC_Object=MibScalar
mbsmMaxNumOfPortsPerLC=_MbsmMaxNumOfPortsPerLC_Object((1,3,6,1,4,1,10876,101,1,81,100,1,3),_MbsmMaxNumOfPortsPerLC_Type())
mbsmMaxNumOfPortsPerLC.setMaxAccess(_D)
if mibBuilder.loadTexts:mbsmMaxNumOfPortsPerLC.setStatus(_A)
class _MbsmLoadSharingFlag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_MbsmLoadSharingFlag_Type.__name__=_B
_MbsmLoadSharingFlag_Object=MibScalar
mbsmLoadSharingFlag=_MbsmLoadSharingFlag_Object((1,3,6,1,4,1,10876,101,1,81,100,1,4),_MbsmLoadSharingFlag_Type())
mbsmLoadSharingFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:mbsmLoadSharingFlag.setStatus(_A)
_MbsmSlotModuleMapTable_Object=MibTable
mbsmSlotModuleMapTable=_MbsmSlotModuleMapTable_Object((1,3,6,1,4,1,10876,101,1,81,100,2))
if mibBuilder.loadTexts:mbsmSlotModuleMapTable.setStatus(_A)
_MbsmSlotModuleMapEntry_Object=MibTableRow
mbsmSlotModuleMapEntry=_MbsmSlotModuleMapEntry_Object((1,3,6,1,4,1,10876,101,1,81,100,2,1))
mbsmSlotModuleMapEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:mbsmSlotModuleMapEntry.setStatus(_A)
class _MbsmSlotId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MbsmSlotId_Type.__name__=_B
_MbsmSlotId_Object=MibTableColumn
mbsmSlotId=_MbsmSlotId_Object((1,3,6,1,4,1,10876,101,1,81,100,2,1,1),_MbsmSlotId_Type())
mbsmSlotId.setMaxAccess(_G)
if mibBuilder.loadTexts:mbsmSlotId.setStatus(_A)
class _MbsmSlotModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lineCard',1),('controlCard',2)))
_MbsmSlotModuleType_Type.__name__=_B
_MbsmSlotModuleType_Object=MibTableColumn
mbsmSlotModuleType=_MbsmSlotModuleType_Object((1,3,6,1,4,1,10876,101,1,81,100,2,1,2),_MbsmSlotModuleType_Type())
mbsmSlotModuleType.setMaxAccess(_E)
if mibBuilder.loadTexts:mbsmSlotModuleType.setStatus(_A)
_MbsmSlotModuleStatus_Type=RowStatus
_MbsmSlotModuleStatus_Object=MibTableColumn
mbsmSlotModuleStatus=_MbsmSlotModuleStatus_Object((1,3,6,1,4,1,10876,101,1,81,100,2,1,3),_MbsmSlotModuleStatus_Type())
mbsmSlotModuleStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mbsmSlotModuleStatus.setStatus(_A)
_MbsmLCTypeTable_Object=MibTable
mbsmLCTypeTable=_MbsmLCTypeTable_Object((1,3,6,1,4,1,10876,101,1,81,100,3))
if mibBuilder.loadTexts:mbsmLCTypeTable.setStatus(_A)
_MbsmLCTypeEntry_Object=MibTableRow
mbsmLCTypeEntry=_MbsmLCTypeEntry_Object((1,3,6,1,4,1,10876,101,1,81,100,3,1))
mbsmLCTypeEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:mbsmLCTypeEntry.setStatus(_A)
class _MbsmLCIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MbsmLCIndex_Type.__name__=_B
_MbsmLCIndex_Object=MibTableColumn
mbsmLCIndex=_MbsmLCIndex_Object((1,3,6,1,4,1,10876,101,1,81,100,3,1,1),_MbsmLCIndex_Type())
mbsmLCIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mbsmLCIndex.setStatus(_A)
class _MbsmLCName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MbsmLCName_Type.__name__=_I
_MbsmLCName_Object=MibTableColumn
mbsmLCName=_MbsmLCName_Object((1,3,6,1,4,1,10876,101,1,81,100,3,1,2),_MbsmLCName_Type())
mbsmLCName.setMaxAccess(_E)
if mibBuilder.loadTexts:mbsmLCName.setStatus(_A)
class _MbsmLCMaxPorts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MbsmLCMaxPorts_Type.__name__=_B
_MbsmLCMaxPorts_Object=MibTableColumn
mbsmLCMaxPorts=_MbsmLCMaxPorts_Object((1,3,6,1,4,1,10876,101,1,81,100,3,1,3),_MbsmLCMaxPorts_Type())
mbsmLCMaxPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:mbsmLCMaxPorts.setStatus(_A)
_MbsmLCRowStatus_Type=RowStatus
_MbsmLCRowStatus_Object=MibTableColumn
mbsmLCRowStatus=_MbsmLCRowStatus_Object((1,3,6,1,4,1,10876,101,1,81,100,3,1,4),_MbsmLCRowStatus_Type())
mbsmLCRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mbsmLCRowStatus.setStatus(_A)
_MbsmLCPortInfoTable_Object=MibTable
mbsmLCPortInfoTable=_MbsmLCPortInfoTable_Object((1,3,6,1,4,1,10876,101,1,81,100,4))
if mibBuilder.loadTexts:mbsmLCPortInfoTable.setStatus(_A)
_MbsmLCPortInfoEntry_Object=MibTableRow
mbsmLCPortInfoEntry=_MbsmLCPortInfoEntry_Object((1,3,6,1,4,1,10876,101,1,81,100,4,1))
mbsmLCPortInfoEntry.setIndexNames((0,_C,_H),(0,_C,_J))
if mibBuilder.loadTexts:mbsmLCPortInfoEntry.setStatus(_A)
class _MbsmLCPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MbsmLCPortIndex_Type.__name__=_B
_MbsmLCPortIndex_Object=MibTableColumn
mbsmLCPortIndex=_MbsmLCPortIndex_Object((1,3,6,1,4,1,10876,101,1,81,100,4,1,1),_MbsmLCPortIndex_Type())
mbsmLCPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mbsmLCPortIndex.setStatus(_A)
_MbsmLCPortIfType_Type=IANAifType
_MbsmLCPortIfType_Object=MibTableColumn
mbsmLCPortIfType=_MbsmLCPortIfType_Object((1,3,6,1,4,1,10876,101,1,81,100,4,1,2),_MbsmLCPortIfType_Type())
mbsmLCPortIfType.setMaxAccess(_D)
if mibBuilder.loadTexts:mbsmLCPortIfType.setStatus(_A)
_MbsmLCPortSpeed_Type=Gauge32
_MbsmLCPortSpeed_Object=MibTableColumn
mbsmLCPortSpeed=_MbsmLCPortSpeed_Object((1,3,6,1,4,1,10876,101,1,81,100,4,1,3),_MbsmLCPortSpeed_Type())
mbsmLCPortSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:mbsmLCPortSpeed.setStatus(_A)
_MbsmLCPortHighSpeed_Type=Gauge32
_MbsmLCPortHighSpeed_Object=MibTableColumn
mbsmLCPortHighSpeed=_MbsmLCPortHighSpeed_Object((1,3,6,1,4,1,10876,101,1,81,100,4,1,4),_MbsmLCPortHighSpeed_Type())
mbsmLCPortHighSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:mbsmLCPortHighSpeed.setStatus(_A)
_MbsmLCConfigTable_Object=MibTable
mbsmLCConfigTable=_MbsmLCConfigTable_Object((1,3,6,1,4,1,10876,101,1,81,100,5))
if mibBuilder.loadTexts:mbsmLCConfigTable.setStatus(_A)
_MbsmLCConfigEntry_Object=MibTableRow
mbsmLCConfigEntry=_MbsmLCConfigEntry_Object((1,3,6,1,4,1,10876,101,1,81,100,5,1))
mbsmLCConfigEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:mbsmLCConfigEntry.setStatus(_A)
class _MbsmLCConfigSlotId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MbsmLCConfigSlotId_Type.__name__=_B
_MbsmLCConfigSlotId_Object=MibTableColumn
mbsmLCConfigSlotId=_MbsmLCConfigSlotId_Object((1,3,6,1,4,1,10876,101,1,81,100,5,1,1),_MbsmLCConfigSlotId_Type())
mbsmLCConfigSlotId.setMaxAccess(_G)
if mibBuilder.loadTexts:mbsmLCConfigSlotId.setStatus(_A)
_MbsmLCConfigCardName_Type=DisplayString
_MbsmLCConfigCardName_Object=MibTableColumn
mbsmLCConfigCardName=_MbsmLCConfigCardName_Object((1,3,6,1,4,1,10876,101,1,81,100,5,1,2),_MbsmLCConfigCardName_Type())
mbsmLCConfigCardName.setMaxAccess(_E)
if mibBuilder.loadTexts:mbsmLCConfigCardName.setStatus(_A)
class _MbsmLCConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dynamic',0),('static',1)))
_MbsmLCConfigStatus_Type.__name__=_B
_MbsmLCConfigStatus_Object=MibTableColumn
mbsmLCConfigStatus=_MbsmLCConfigStatus_Object((1,3,6,1,4,1,10876,101,1,81,100,5,1,3),_MbsmLCConfigStatus_Type())
mbsmLCConfigStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mbsmLCConfigStatus.setStatus(_A)
_MbsmIssTrapGroup_ObjectIdentity=ObjectIdentity
mbsmIssTrapGroup=_MbsmIssTrapGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,81,100,6))
mbsmConfigErrTrap=NotificationType((1,3,6,1,4,1,10876,101,1,81,100,6,1))
mbsmConfigErrTrap.setObjects(*((_C,_F),(_C,_L),(_C,_M),(_C,_N)))
if mibBuilder.loadTexts:mbsmConfigErrTrap.setStatus(_A)
mbsmCardInsertedTrap=NotificationType((1,3,6,1,4,1,10876,101,1,81,100,6,2))
mbsmCardInsertedTrap.setObjects((_C,_F))
if mibBuilder.loadTexts:mbsmCardInsertedTrap.setStatus(_A)
mbsmCardRemovedTrap=NotificationType((1,3,6,1,4,1,10876,101,1,81,100,6,3))
mbsmCardRemovedTrap.setObjects((_C,_F))
if mibBuilder.loadTexts:mbsmCardRemovedTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'mbsmIssGroup':mbsmIssGroup,'mbsmIssScalarGroup':mbsmIssScalarGroup,'mbsmMaxNumOfLCSlots':mbsmMaxNumOfLCSlots,'mbsmMaxNumOfSlots':mbsmMaxNumOfSlots,'mbsmMaxNumOfPortsPerLC':mbsmMaxNumOfPortsPerLC,'mbsmLoadSharingFlag':mbsmLoadSharingFlag,'mbsmSlotModuleMapTable':mbsmSlotModuleMapTable,'mbsmSlotModuleMapEntry':mbsmSlotModuleMapEntry,_F:mbsmSlotId,_L:mbsmSlotModuleType,_M:mbsmSlotModuleStatus,'mbsmLCTypeTable':mbsmLCTypeTable,'mbsmLCTypeEntry':mbsmLCTypeEntry,_H:mbsmLCIndex,'mbsmLCName':mbsmLCName,'mbsmLCMaxPorts':mbsmLCMaxPorts,'mbsmLCRowStatus':mbsmLCRowStatus,'mbsmLCPortInfoTable':mbsmLCPortInfoTable,'mbsmLCPortInfoEntry':mbsmLCPortInfoEntry,_J:mbsmLCPortIndex,'mbsmLCPortIfType':mbsmLCPortIfType,'mbsmLCPortSpeed':mbsmLCPortSpeed,'mbsmLCPortHighSpeed':mbsmLCPortHighSpeed,'mbsmLCConfigTable':mbsmLCConfigTable,'mbsmLCConfigEntry':mbsmLCConfigEntry,_K:mbsmLCConfigSlotId,_N:mbsmLCConfigCardName,'mbsmLCConfigStatus':mbsmLCConfigStatus,'mbsmIssTrapGroup':mbsmIssTrapGroup,'mbsmConfigErrTrap':mbsmConfigErrTrap,'mbsmCardInsertedTrap':mbsmCardInsertedTrap,'mbsmCardRemovedTrap':mbsmCardRemovedTrap})