_T='a3ComPortFilterBridgePortPort'
_S='a3ComPortFilterBridgePortType'
_R='a3ComPortFilterBridgeNumber'
_Q='a3ComPortFilterId'
_P='a3ComBridgeFilterBridgeNumber'
_O='a3ComBridgeFilterId'
_N='a3ComFilterPortPort'
_M='a3ComFilterPortType'
_L='a3ComFilterPortId'
_K='a3ComFilterPortGroupId'
_J='a3ComFilterAddressAddress'
_I='a3ComFilterAddressId'
_H='a3ComFilterAddressGroupId'
_G='OctetString'
_F='DisplayString'
_E='Integer32'
_D='read-write'
_C='A3COM-SWITCHING-SYSTEMS-FILTER-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
class RowStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('active',1),('notInService',2),('notReady',3),('createAndGo',4),('createAndWait',5),('destroy',6)))
class A3ComFilterPortType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_A3Com_ObjectIdentity=ObjectIdentity
a3Com=_A3Com_ObjectIdentity((1,3,6,1,4,1,43))
_SwitchingSystemsMibs_ObjectIdentity=ObjectIdentity
switchingSystemsMibs=_SwitchingSystemsMibs_ObjectIdentity((1,3,6,1,4,1,43,29))
_A3ComSwitchingSystemsMib_ObjectIdentity=ObjectIdentity
a3ComSwitchingSystemsMib=_A3ComSwitchingSystemsMib_ObjectIdentity((1,3,6,1,4,1,43,29,4))
_A3ComFilterGroup_ObjectIdentity=ObjectIdentity
a3ComFilterGroup=_A3ComFilterGroup_ObjectIdentity((1,3,6,1,4,1,43,29,4,20))
_A3ComFilterAddressGroup_ObjectIdentity=ObjectIdentity
a3ComFilterAddressGroup=_A3ComFilterAddressGroup_ObjectIdentity((1,3,6,1,4,1,43,29,4,20,1))
_A3ComFilterAddressGroupNextAvailableIndex_Type=Integer32
_A3ComFilterAddressGroupNextAvailableIndex_Object=MibScalar
a3ComFilterAddressGroupNextAvailableIndex=_A3ComFilterAddressGroupNextAvailableIndex_Object((1,3,6,1,4,1,43,29,4,20,1,1),_A3ComFilterAddressGroupNextAvailableIndex_Type())
a3ComFilterAddressGroupNextAvailableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComFilterAddressGroupNextAvailableIndex.setStatus(_A)
_A3ComFilterAddressGroupCount_Type=Integer32
_A3ComFilterAddressGroupCount_Object=MibScalar
a3ComFilterAddressGroupCount=_A3ComFilterAddressGroupCount_Object((1,3,6,1,4,1,43,29,4,20,1,2),_A3ComFilterAddressGroupCount_Type())
a3ComFilterAddressGroupCount.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComFilterAddressGroupCount.setStatus(_A)
_A3ComFilterAddressGroupTable_Object=MibTable
a3ComFilterAddressGroupTable=_A3ComFilterAddressGroupTable_Object((1,3,6,1,4,1,43,29,4,20,1,3))
if mibBuilder.loadTexts:a3ComFilterAddressGroupTable.setStatus(_A)
_A3ComFilterAddressGroupEntry_Object=MibTableRow
a3ComFilterAddressGroupEntry=_A3ComFilterAddressGroupEntry_Object((1,3,6,1,4,1,43,29,4,20,1,3,1))
a3ComFilterAddressGroupEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:a3ComFilterAddressGroupEntry.setStatus(_A)
class _A3ComFilterAddressGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComFilterAddressGroupId_Type.__name__=_E
_A3ComFilterAddressGroupId_Object=MibTableColumn
a3ComFilterAddressGroupId=_A3ComFilterAddressGroupId_Object((1,3,6,1,4,1,43,29,4,20,1,3,1,1),_A3ComFilterAddressGroupId_Type())
a3ComFilterAddressGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComFilterAddressGroupId.setStatus(_A)
_A3ComFilterAddressGroupMaskId_Type=Integer32
_A3ComFilterAddressGroupMaskId_Object=MibTableColumn
a3ComFilterAddressGroupMaskId=_A3ComFilterAddressGroupMaskId_Object((1,3,6,1,4,1,43,29,4,20,1,3,1,2),_A3ComFilterAddressGroupMaskId_Type())
a3ComFilterAddressGroupMaskId.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComFilterAddressGroupMaskId.setStatus(_A)
class _A3ComFilterAddressGroupBridgeMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_A3ComFilterAddressGroupBridgeMask_Type.__name__=_G
_A3ComFilterAddressGroupBridgeMask_Object=MibTableColumn
a3ComFilterAddressGroupBridgeMask=_A3ComFilterAddressGroupBridgeMask_Object((1,3,6,1,4,1,43,29,4,20,1,3,1,3),_A3ComFilterAddressGroupBridgeMask_Type())
a3ComFilterAddressGroupBridgeMask.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComFilterAddressGroupBridgeMask.setStatus(_A)
class _A3ComFilterAddressGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_A3ComFilterAddressGroupName_Type.__name__=_F
_A3ComFilterAddressGroupName_Object=MibTableColumn
a3ComFilterAddressGroupName=_A3ComFilterAddressGroupName_Object((1,3,6,1,4,1,43,29,4,20,1,3,1,4),_A3ComFilterAddressGroupName_Type())
a3ComFilterAddressGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComFilterAddressGroupName.setStatus(_A)
_A3ComFilterAddressGroupStatus_Type=RowStatus
_A3ComFilterAddressGroupStatus_Object=MibTableColumn
a3ComFilterAddressGroupStatus=_A3ComFilterAddressGroupStatus_Object((1,3,6,1,4,1,43,29,4,20,1,3,1,5),_A3ComFilterAddressGroupStatus_Type())
a3ComFilterAddressGroupStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComFilterAddressGroupStatus.setStatus(_A)
_A3ComFilterAddressTable_Object=MibTable
a3ComFilterAddressTable=_A3ComFilterAddressTable_Object((1,3,6,1,4,1,43,29,4,20,1,4))
if mibBuilder.loadTexts:a3ComFilterAddressTable.setStatus(_A)
_A3ComFilterAddressEntry_Object=MibTableRow
a3ComFilterAddressEntry=_A3ComFilterAddressEntry_Object((1,3,6,1,4,1,43,29,4,20,1,4,1))
a3ComFilterAddressEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:a3ComFilterAddressEntry.setStatus(_A)
class _A3ComFilterAddressId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComFilterAddressId_Type.__name__=_E
_A3ComFilterAddressId_Object=MibTableColumn
a3ComFilterAddressId=_A3ComFilterAddressId_Object((1,3,6,1,4,1,43,29,4,20,1,4,1,1),_A3ComFilterAddressId_Type())
a3ComFilterAddressId.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComFilterAddressId.setStatus(_A)
_A3ComFilterAddressAddress_Type=PhysAddress
_A3ComFilterAddressAddress_Object=MibTableColumn
a3ComFilterAddressAddress=_A3ComFilterAddressAddress_Object((1,3,6,1,4,1,43,29,4,20,1,4,1,2),_A3ComFilterAddressAddress_Type())
a3ComFilterAddressAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComFilterAddressAddress.setStatus(_A)
_A3ComFilterAddressStatus_Type=RowStatus
_A3ComFilterAddressStatus_Object=MibTableColumn
a3ComFilterAddressStatus=_A3ComFilterAddressStatus_Object((1,3,6,1,4,1,43,29,4,20,1,4,1,3),_A3ComFilterAddressStatus_Type())
a3ComFilterAddressStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComFilterAddressStatus.setStatus(_A)
_A3ComFilterPortGroup_ObjectIdentity=ObjectIdentity
a3ComFilterPortGroup=_A3ComFilterPortGroup_ObjectIdentity((1,3,6,1,4,1,43,29,4,20,2))
_A3ComFilterPortGroupNextAvailableIndex_Type=Integer32
_A3ComFilterPortGroupNextAvailableIndex_Object=MibScalar
a3ComFilterPortGroupNextAvailableIndex=_A3ComFilterPortGroupNextAvailableIndex_Object((1,3,6,1,4,1,43,29,4,20,2,1),_A3ComFilterPortGroupNextAvailableIndex_Type())
a3ComFilterPortGroupNextAvailableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComFilterPortGroupNextAvailableIndex.setStatus(_A)
_A3ComFilterPortGroupCount_Type=Integer32
_A3ComFilterPortGroupCount_Object=MibScalar
a3ComFilterPortGroupCount=_A3ComFilterPortGroupCount_Object((1,3,6,1,4,1,43,29,4,20,2,2),_A3ComFilterPortGroupCount_Type())
a3ComFilterPortGroupCount.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComFilterPortGroupCount.setStatus(_A)
_A3ComFilterPortGroupTable_Object=MibTable
a3ComFilterPortGroupTable=_A3ComFilterPortGroupTable_Object((1,3,6,1,4,1,43,29,4,20,2,3))
if mibBuilder.loadTexts:a3ComFilterPortGroupTable.setStatus(_A)
_A3ComFilterPortGroupEntry_Object=MibTableRow
a3ComFilterPortGroupEntry=_A3ComFilterPortGroupEntry_Object((1,3,6,1,4,1,43,29,4,20,2,3,1))
a3ComFilterPortGroupEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:a3ComFilterPortGroupEntry.setStatus(_A)
class _A3ComFilterPortGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComFilterPortGroupId_Type.__name__=_E
_A3ComFilterPortGroupId_Object=MibTableColumn
a3ComFilterPortGroupId=_A3ComFilterPortGroupId_Object((1,3,6,1,4,1,43,29,4,20,2,3,1,1),_A3ComFilterPortGroupId_Type())
a3ComFilterPortGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComFilterPortGroupId.setStatus(_A)
_A3ComFilterPortGroupMaskId_Type=Integer32
_A3ComFilterPortGroupMaskId_Object=MibTableColumn
a3ComFilterPortGroupMaskId=_A3ComFilterPortGroupMaskId_Object((1,3,6,1,4,1,43,29,4,20,2,3,1,2),_A3ComFilterPortGroupMaskId_Type())
a3ComFilterPortGroupMaskId.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComFilterPortGroupMaskId.setStatus(_A)
_A3ComFilterPortGroupBridgeNumber_Type=Integer32
_A3ComFilterPortGroupBridgeNumber_Object=MibTableColumn
a3ComFilterPortGroupBridgeNumber=_A3ComFilterPortGroupBridgeNumber_Object((1,3,6,1,4,1,43,29,4,20,2,3,1,3),_A3ComFilterPortGroupBridgeNumber_Type())
a3ComFilterPortGroupBridgeNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComFilterPortGroupBridgeNumber.setStatus(_A)
class _A3ComFilterPortGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_A3ComFilterPortGroupName_Type.__name__=_F
_A3ComFilterPortGroupName_Object=MibTableColumn
a3ComFilterPortGroupName=_A3ComFilterPortGroupName_Object((1,3,6,1,4,1,43,29,4,20,2,3,1,4),_A3ComFilterPortGroupName_Type())
a3ComFilterPortGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComFilterPortGroupName.setStatus(_A)
_A3ComFilterPortGroupStatus_Type=RowStatus
_A3ComFilterPortGroupStatus_Object=MibTableColumn
a3ComFilterPortGroupStatus=_A3ComFilterPortGroupStatus_Object((1,3,6,1,4,1,43,29,4,20,2,3,1,5),_A3ComFilterPortGroupStatus_Type())
a3ComFilterPortGroupStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComFilterPortGroupStatus.setStatus(_A)
_A3ComFilterPortTable_Object=MibTable
a3ComFilterPortTable=_A3ComFilterPortTable_Object((1,3,6,1,4,1,43,29,4,20,2,4))
if mibBuilder.loadTexts:a3ComFilterPortTable.setStatus(_A)
_A3ComFilterPortEntry_Object=MibTableRow
a3ComFilterPortEntry=_A3ComFilterPortEntry_Object((1,3,6,1,4,1,43,29,4,20,2,4,1))
a3ComFilterPortEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:a3ComFilterPortEntry.setStatus(_A)
class _A3ComFilterPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComFilterPortId_Type.__name__=_E
_A3ComFilterPortId_Object=MibTableColumn
a3ComFilterPortId=_A3ComFilterPortId_Object((1,3,6,1,4,1,43,29,4,20,2,4,1,1),_A3ComFilterPortId_Type())
a3ComFilterPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComFilterPortId.setStatus(_A)
_A3ComFilterPortType_Type=A3ComFilterPortType
_A3ComFilterPortType_Object=MibTableColumn
a3ComFilterPortType=_A3ComFilterPortType_Object((1,3,6,1,4,1,43,29,4,20,2,4,1,2),_A3ComFilterPortType_Type())
a3ComFilterPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComFilterPortType.setStatus(_A)
class _A3ComFilterPortPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComFilterPortPort_Type.__name__=_E
_A3ComFilterPortPort_Object=MibTableColumn
a3ComFilterPortPort=_A3ComFilterPortPort_Object((1,3,6,1,4,1,43,29,4,20,2,4,1,3),_A3ComFilterPortPort_Type())
a3ComFilterPortPort.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComFilterPortPort.setStatus(_A)
_A3ComFilterPortStatus_Type=RowStatus
_A3ComFilterPortStatus_Object=MibTableColumn
a3ComFilterPortStatus=_A3ComFilterPortStatus_Object((1,3,6,1,4,1,43,29,4,20,2,4,1,4),_A3ComFilterPortStatus_Type())
a3ComFilterPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComFilterPortStatus.setStatus(_A)
_A3ComBridgeFilterGroup_ObjectIdentity=ObjectIdentity
a3ComBridgeFilterGroup=_A3ComBridgeFilterGroup_ObjectIdentity((1,3,6,1,4,1,43,29,4,20,3))
_A3ComBridgeFilterNextAvailableIndex_Type=Integer32
_A3ComBridgeFilterNextAvailableIndex_Object=MibScalar
a3ComBridgeFilterNextAvailableIndex=_A3ComBridgeFilterNextAvailableIndex_Object((1,3,6,1,4,1,43,29,4,20,3,1),_A3ComBridgeFilterNextAvailableIndex_Type())
a3ComBridgeFilterNextAvailableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComBridgeFilterNextAvailableIndex.setStatus(_A)
_A3ComBridgeFilterCount_Type=Integer32
_A3ComBridgeFilterCount_Object=MibScalar
a3ComBridgeFilterCount=_A3ComBridgeFilterCount_Object((1,3,6,1,4,1,43,29,4,20,3,2),_A3ComBridgeFilterCount_Type())
a3ComBridgeFilterCount.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComBridgeFilterCount.setStatus(_A)
_A3ComBridgeFilterTable_Object=MibTable
a3ComBridgeFilterTable=_A3ComBridgeFilterTable_Object((1,3,6,1,4,1,43,29,4,20,3,3))
if mibBuilder.loadTexts:a3ComBridgeFilterTable.setStatus(_A)
_A3ComBridgeFilterEntry_Object=MibTableRow
a3ComBridgeFilterEntry=_A3ComBridgeFilterEntry_Object((1,3,6,1,4,1,43,29,4,20,3,3,1))
a3ComBridgeFilterEntry.setIndexNames((0,_C,_O),(0,_C,_P))
if mibBuilder.loadTexts:a3ComBridgeFilterEntry.setStatus(_A)
class _A3ComBridgeFilterId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComBridgeFilterId_Type.__name__=_E
_A3ComBridgeFilterId_Object=MibTableColumn
a3ComBridgeFilterId=_A3ComBridgeFilterId_Object((1,3,6,1,4,1,43,29,4,20,3,3,1,1),_A3ComBridgeFilterId_Type())
a3ComBridgeFilterId.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComBridgeFilterId.setStatus(_A)
class _A3ComBridgeFilterBridgeNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComBridgeFilterBridgeNumber_Type.__name__=_E
_A3ComBridgeFilterBridgeNumber_Object=MibTableColumn
a3ComBridgeFilterBridgeNumber=_A3ComBridgeFilterBridgeNumber_Object((1,3,6,1,4,1,43,29,4,20,3,3,1,2),_A3ComBridgeFilterBridgeNumber_Type())
a3ComBridgeFilterBridgeNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComBridgeFilterBridgeNumber.setStatus(_A)
class _A3ComBridgeFilterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_A3ComBridgeFilterName_Type.__name__=_F
_A3ComBridgeFilterName_Object=MibTableColumn
a3ComBridgeFilterName=_A3ComBridgeFilterName_Object((1,3,6,1,4,1,43,29,4,20,3,3,1,3),_A3ComBridgeFilterName_Type())
a3ComBridgeFilterName.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComBridgeFilterName.setStatus(_A)
class _A3ComBridgeFilterProgram_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(255,255));fixedLength=255
_A3ComBridgeFilterProgram_Type.__name__=_F
_A3ComBridgeFilterProgram_Object=MibTableColumn
a3ComBridgeFilterProgram=_A3ComBridgeFilterProgram_Object((1,3,6,1,4,1,43,29,4,20,3,3,1,4),_A3ComBridgeFilterProgram_Type())
a3ComBridgeFilterProgram.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComBridgeFilterProgram.setStatus(_A)
_A3ComBridgeFilterStatus_Type=RowStatus
_A3ComBridgeFilterStatus_Object=MibTableColumn
a3ComBridgeFilterStatus=_A3ComBridgeFilterStatus_Object((1,3,6,1,4,1,43,29,4,20,3,3,1,5),_A3ComBridgeFilterStatus_Type())
a3ComBridgeFilterStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComBridgeFilterStatus.setStatus(_A)
_A3ComPortFilterTable_Object=MibTable
a3ComPortFilterTable=_A3ComPortFilterTable_Object((1,3,6,1,4,1,43,29,4,20,3,4))
if mibBuilder.loadTexts:a3ComPortFilterTable.setStatus(_A)
_A3ComPortFilterEntry_Object=MibTableRow
a3ComPortFilterEntry=_A3ComPortFilterEntry_Object((1,3,6,1,4,1,43,29,4,20,3,4,1))
a3ComPortFilterEntry.setIndexNames((0,_C,_Q),(0,_C,_R),(0,_C,_S),(0,_C,_T))
if mibBuilder.loadTexts:a3ComPortFilterEntry.setStatus(_A)
class _A3ComPortFilterId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComPortFilterId_Type.__name__=_E
_A3ComPortFilterId_Object=MibTableColumn
a3ComPortFilterId=_A3ComPortFilterId_Object((1,3,6,1,4,1,43,29,4,20,3,4,1,1),_A3ComPortFilterId_Type())
a3ComPortFilterId.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComPortFilterId.setStatus(_A)
class _A3ComPortFilterBridgeNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComPortFilterBridgeNumber_Type.__name__=_E
_A3ComPortFilterBridgeNumber_Object=MibTableColumn
a3ComPortFilterBridgeNumber=_A3ComPortFilterBridgeNumber_Object((1,3,6,1,4,1,43,29,4,20,3,4,1,2),_A3ComPortFilterBridgeNumber_Type())
a3ComPortFilterBridgeNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComPortFilterBridgeNumber.setStatus(_A)
_A3ComPortFilterBridgePortType_Type=A3ComFilterPortType
_A3ComPortFilterBridgePortType_Object=MibTableColumn
a3ComPortFilterBridgePortType=_A3ComPortFilterBridgePortType_Object((1,3,6,1,4,1,43,29,4,20,3,4,1,3),_A3ComPortFilterBridgePortType_Type())
a3ComPortFilterBridgePortType.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComPortFilterBridgePortType.setStatus(_A)
class _A3ComPortFilterBridgePortPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_A3ComPortFilterBridgePortPort_Type.__name__=_E
_A3ComPortFilterBridgePortPort_Object=MibTableColumn
a3ComPortFilterBridgePortPort=_A3ComPortFilterBridgePortPort_Object((1,3,6,1,4,1,43,29,4,20,3,4,1,4),_A3ComPortFilterBridgePortPort_Type())
a3ComPortFilterBridgePortPort.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComPortFilterBridgePortPort.setStatus(_A)
_A3ComPortFilterPktProcessPath_Type=Integer32
_A3ComPortFilterPktProcessPath_Object=MibTableColumn
a3ComPortFilterPktProcessPath=_A3ComPortFilterPktProcessPath_Object((1,3,6,1,4,1,43,29,4,20,3,4,1,5),_A3ComPortFilterPktProcessPath_Type())
a3ComPortFilterPktProcessPath.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComPortFilterPktProcessPath.setStatus(_A)
_A3ComPortFilterStatus_Type=RowStatus
_A3ComPortFilterStatus_Object=MibTableColumn
a3ComPortFilterStatus=_A3ComPortFilterStatus_Object((1,3,6,1,4,1,43,29,4,20,3,4,1,6),_A3ComPortFilterStatus_Type())
a3ComPortFilterStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComPortFilterStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'RowStatus':RowStatus,'A3ComFilterPortType':A3ComFilterPortType,'a3Com':a3Com,'switchingSystemsMibs':switchingSystemsMibs,'a3ComSwitchingSystemsMib':a3ComSwitchingSystemsMib,'a3ComFilterGroup':a3ComFilterGroup,'a3ComFilterAddressGroup':a3ComFilterAddressGroup,'a3ComFilterAddressGroupNextAvailableIndex':a3ComFilterAddressGroupNextAvailableIndex,'a3ComFilterAddressGroupCount':a3ComFilterAddressGroupCount,'a3ComFilterAddressGroupTable':a3ComFilterAddressGroupTable,'a3ComFilterAddressGroupEntry':a3ComFilterAddressGroupEntry,_H:a3ComFilterAddressGroupId,'a3ComFilterAddressGroupMaskId':a3ComFilterAddressGroupMaskId,'a3ComFilterAddressGroupBridgeMask':a3ComFilterAddressGroupBridgeMask,'a3ComFilterAddressGroupName':a3ComFilterAddressGroupName,'a3ComFilterAddressGroupStatus':a3ComFilterAddressGroupStatus,'a3ComFilterAddressTable':a3ComFilterAddressTable,'a3ComFilterAddressEntry':a3ComFilterAddressEntry,_I:a3ComFilterAddressId,_J:a3ComFilterAddressAddress,'a3ComFilterAddressStatus':a3ComFilterAddressStatus,'a3ComFilterPortGroup':a3ComFilterPortGroup,'a3ComFilterPortGroupNextAvailableIndex':a3ComFilterPortGroupNextAvailableIndex,'a3ComFilterPortGroupCount':a3ComFilterPortGroupCount,'a3ComFilterPortGroupTable':a3ComFilterPortGroupTable,'a3ComFilterPortGroupEntry':a3ComFilterPortGroupEntry,_K:a3ComFilterPortGroupId,'a3ComFilterPortGroupMaskId':a3ComFilterPortGroupMaskId,'a3ComFilterPortGroupBridgeNumber':a3ComFilterPortGroupBridgeNumber,'a3ComFilterPortGroupName':a3ComFilterPortGroupName,'a3ComFilterPortGroupStatus':a3ComFilterPortGroupStatus,'a3ComFilterPortTable':a3ComFilterPortTable,'a3ComFilterPortEntry':a3ComFilterPortEntry,_L:a3ComFilterPortId,_M:a3ComFilterPortType,_N:a3ComFilterPortPort,'a3ComFilterPortStatus':a3ComFilterPortStatus,'a3ComBridgeFilterGroup':a3ComBridgeFilterGroup,'a3ComBridgeFilterNextAvailableIndex':a3ComBridgeFilterNextAvailableIndex,'a3ComBridgeFilterCount':a3ComBridgeFilterCount,'a3ComBridgeFilterTable':a3ComBridgeFilterTable,'a3ComBridgeFilterEntry':a3ComBridgeFilterEntry,_O:a3ComBridgeFilterId,_P:a3ComBridgeFilterBridgeNumber,'a3ComBridgeFilterName':a3ComBridgeFilterName,'a3ComBridgeFilterProgram':a3ComBridgeFilterProgram,'a3ComBridgeFilterStatus':a3ComBridgeFilterStatus,'a3ComPortFilterTable':a3ComPortFilterTable,'a3ComPortFilterEntry':a3ComPortFilterEntry,_Q:a3ComPortFilterId,_R:a3ComPortFilterBridgeNumber,_S:a3ComPortFilterBridgePortType,_T:a3ComPortFilterBridgePortPort,'a3ComPortFilterPktProcessPath':a3ComPortFilterPktProcessPath,'a3ComPortFilterStatus':a3ComPortFilterStatus})