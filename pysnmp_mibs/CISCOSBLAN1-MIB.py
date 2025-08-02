_O='rlLan1x86PriorityIndex'
_N='GroupIdList'
_M='GroupId'
_L='rlLan1ModulePortIfIndex'
_K='rlLan1VfMacMappingDstMacAddress'
_J='rlLan1x86VlanMappingVlanId'
_I='VlanIdOrNone'
_H='OctetString'
_G='read-create'
_F='TruthValue'
_E='not-accessible'
_D='CISCOSBLAN1-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_F)
rlLan1=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,224))
if mibBuilder.loadTexts:rlLan1.setRevisions(('2015-06-30 00:00',))
class GroupId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1279))
class GroupIdList(TextualConvention,OctetString):status=_A
class VlanIdOrNone(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
class _RlLan1STagEtherType_Type(OctetString):defaultHexValue='0000';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_RlLan1STagEtherType_Type.__name__=_H
_RlLan1STagEtherType_Object=MibScalar
rlLan1STagEtherType=_RlLan1STagEtherType_Object((1,3,6,1,4,1,9,6,1,101,224,1),_RlLan1STagEtherType_Type())
rlLan1STagEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLan1STagEtherType.setStatus(_A)
class _RlLan1CPVlanId_Type(VlanIdOrNone):defaultValue=0
_RlLan1CPVlanId_Type.__name__=_I
_RlLan1CPVlanId_Object=MibScalar
rlLan1CPVlanId=_RlLan1CPVlanId_Object((1,3,6,1,4,1,9,6,1,101,224,2),_RlLan1CPVlanId_Type())
rlLan1CPVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLan1CPVlanId.setStatus(_A)
class _RlLan1CPVlanCos_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RlLan1CPVlanCos_Type.__name__=_C
_RlLan1CPVlanCos_Object=MibScalar
rlLan1CPVlanCos=_RlLan1CPVlanCos_Object((1,3,6,1,4,1,9,6,1,101,224,3),_RlLan1CPVlanCos_Type())
rlLan1CPVlanCos.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLan1CPVlanCos.setStatus(_A)
class _RlLan1x86Port_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_RlLan1x86Port_Type.__name__=_C
_RlLan1x86Port_Object=MibScalar
rlLan1x86Port=_RlLan1x86Port_Object((1,3,6,1,4,1,9,6,1,101,224,4),_RlLan1x86Port_Type())
rlLan1x86Port.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLan1x86Port.setStatus(_A)
_RlLan1x86VlanMappingTable_Object=MibTable
rlLan1x86VlanMappingTable=_RlLan1x86VlanMappingTable_Object((1,3,6,1,4,1,9,6,1,101,224,5))
if mibBuilder.loadTexts:rlLan1x86VlanMappingTable.setStatus(_A)
_RlLan1x86VlanMappingEntry_Object=MibTableRow
rlLan1x86VlanMappingEntry=_RlLan1x86VlanMappingEntry_Object((1,3,6,1,4,1,9,6,1,101,224,5,1))
rlLan1x86VlanMappingEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:rlLan1x86VlanMappingEntry.setStatus(_A)
_RlLan1x86VlanMappingVlanId_Type=VlanId
_RlLan1x86VlanMappingVlanId_Object=MibTableColumn
rlLan1x86VlanMappingVlanId=_RlLan1x86VlanMappingVlanId_Object((1,3,6,1,4,1,9,6,1,101,224,5,1,1),_RlLan1x86VlanMappingVlanId_Type())
rlLan1x86VlanMappingVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:rlLan1x86VlanMappingVlanId.setStatus(_A)
_RlLan1x86VlanMappingGroupId_Type=GroupId
_RlLan1x86VlanMappingGroupId_Object=MibTableColumn
rlLan1x86VlanMappingGroupId=_RlLan1x86VlanMappingGroupId_Object((1,3,6,1,4,1,9,6,1,101,224,5,1,2),_RlLan1x86VlanMappingGroupId_Type())
rlLan1x86VlanMappingGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLan1x86VlanMappingGroupId.setStatus(_A)
_RlLan1x86VlanMappingRowStatus_Type=RowStatus
_RlLan1x86VlanMappingRowStatus_Object=MibTableColumn
rlLan1x86VlanMappingRowStatus=_RlLan1x86VlanMappingRowStatus_Object((1,3,6,1,4,1,9,6,1,101,224,5,1,3),_RlLan1x86VlanMappingRowStatus_Type())
rlLan1x86VlanMappingRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rlLan1x86VlanMappingRowStatus.setStatus(_A)
_RlLan1VfMacMappingTable_Object=MibTable
rlLan1VfMacMappingTable=_RlLan1VfMacMappingTable_Object((1,3,6,1,4,1,9,6,1,101,224,6))
if mibBuilder.loadTexts:rlLan1VfMacMappingTable.setStatus(_A)
_RlLan1VfMacMappingEntry_Object=MibTableRow
rlLan1VfMacMappingEntry=_RlLan1VfMacMappingEntry_Object((1,3,6,1,4,1,9,6,1,101,224,6,1))
rlLan1VfMacMappingEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:rlLan1VfMacMappingEntry.setStatus(_A)
_RlLan1VfMacMappingDstMacAddress_Type=MacAddress
_RlLan1VfMacMappingDstMacAddress_Object=MibTableColumn
rlLan1VfMacMappingDstMacAddress=_RlLan1VfMacMappingDstMacAddress_Object((1,3,6,1,4,1,9,6,1,101,224,6,1,1),_RlLan1VfMacMappingDstMacAddress_Type())
rlLan1VfMacMappingDstMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:rlLan1VfMacMappingDstMacAddress.setStatus(_A)
_RlLan1VfMacMappingVlanId_Type=VlanId
_RlLan1VfMacMappingVlanId_Object=MibTableColumn
rlLan1VfMacMappingVlanId=_RlLan1VfMacMappingVlanId_Object((1,3,6,1,4,1,9,6,1,101,224,6,1,2),_RlLan1VfMacMappingVlanId_Type())
rlLan1VfMacMappingVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLan1VfMacMappingVlanId.setStatus(_A)
class _RlLan1VfMacMappingMulticast_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('cp',2),('noncp',3)))
_RlLan1VfMacMappingMulticast_Type.__name__=_C
_RlLan1VfMacMappingMulticast_Object=MibTableColumn
rlLan1VfMacMappingMulticast=_RlLan1VfMacMappingMulticast_Object((1,3,6,1,4,1,9,6,1,101,224,6,1,3),_RlLan1VfMacMappingMulticast_Type())
rlLan1VfMacMappingMulticast.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLan1VfMacMappingMulticast.setStatus(_A)
_RlLan1VfMacMappingRowStatus_Type=RowStatus
_RlLan1VfMacMappingRowStatus_Object=MibTableColumn
rlLan1VfMacMappingRowStatus=_RlLan1VfMacMappingRowStatus_Object((1,3,6,1,4,1,9,6,1,101,224,6,1,4),_RlLan1VfMacMappingRowStatus_Type())
rlLan1VfMacMappingRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rlLan1VfMacMappingRowStatus.setStatus(_A)
_RlLan1ModulePortTable_Object=MibTable
rlLan1ModulePortTable=_RlLan1ModulePortTable_Object((1,3,6,1,4,1,9,6,1,101,224,7))
if mibBuilder.loadTexts:rlLan1ModulePortTable.setStatus(_A)
_RlLan1ModulePortEntry_Object=MibTableRow
rlLan1ModulePortEntry=_RlLan1ModulePortEntry_Object((1,3,6,1,4,1,9,6,1,101,224,7,1))
rlLan1ModulePortEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:rlLan1ModulePortEntry.setStatus(_A)
class _RlLan1ModulePortIfIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_RlLan1ModulePortIfIndex_Type.__name__=_C
_RlLan1ModulePortIfIndex_Object=MibTableColumn
rlLan1ModulePortIfIndex=_RlLan1ModulePortIfIndex_Object((1,3,6,1,4,1,9,6,1,101,224,7,1,1),_RlLan1ModulePortIfIndex_Type())
rlLan1ModulePortIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rlLan1ModulePortIfIndex.setStatus(_A)
class _RlLan1ModulePortCPAllowed_Type(TruthValue):defaultValue=2
_RlLan1ModulePortCPAllowed_Type.__name__=_F
_RlLan1ModulePortCPAllowed_Object=MibTableColumn
rlLan1ModulePortCPAllowed=_RlLan1ModulePortCPAllowed_Object((1,3,6,1,4,1,9,6,1,101,224,7,1,2),_RlLan1ModulePortCPAllowed_Type())
rlLan1ModulePortCPAllowed.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLan1ModulePortCPAllowed.setStatus(_A)
class _RlLan1ModulePortMulticastBroadcastAllowedVlan_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('cp',2),('noncp',3)))
_RlLan1ModulePortMulticastBroadcastAllowedVlan_Type.__name__=_C
_RlLan1ModulePortMulticastBroadcastAllowedVlan_Object=MibTableColumn
rlLan1ModulePortMulticastBroadcastAllowedVlan=_RlLan1ModulePortMulticastBroadcastAllowedVlan_Object((1,3,6,1,4,1,9,6,1,101,224,7,1,3),_RlLan1ModulePortMulticastBroadcastAllowedVlan_Type())
rlLan1ModulePortMulticastBroadcastAllowedVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLan1ModulePortMulticastBroadcastAllowedVlan.setStatus(_A)
class _RlLan1ModulePortIngressGroupId_Type(GroupId):defaultValue=0
_RlLan1ModulePortIngressGroupId_Type.__name__=_M
_RlLan1ModulePortIngressGroupId_Object=MibTableColumn
rlLan1ModulePortIngressGroupId=_RlLan1ModulePortIngressGroupId_Object((1,3,6,1,4,1,9,6,1,101,224,7,1,4),_RlLan1ModulePortIngressGroupId_Type())
rlLan1ModulePortIngressGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLan1ModulePortIngressGroupId.setStatus(_A)
class _RlLan1ModulePortEgressGroupIdList_Type(GroupIdList):defaultHexValue=''
_RlLan1ModulePortEgressGroupIdList_Type.__name__=_N
_RlLan1ModulePortEgressGroupIdList_Object=MibTableColumn
rlLan1ModulePortEgressGroupIdList=_RlLan1ModulePortEgressGroupIdList_Object((1,3,6,1,4,1,9,6,1,101,224,7,1,5),_RlLan1ModulePortEgressGroupIdList_Type())
rlLan1ModulePortEgressGroupIdList.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLan1ModulePortEgressGroupIdList.setStatus(_A)
_RlLan1ModulePortRowStatus_Type=RowStatus
_RlLan1ModulePortRowStatus_Object=MibTableColumn
rlLan1ModulePortRowStatus=_RlLan1ModulePortRowStatus_Object((1,3,6,1,4,1,9,6,1,101,224,7,1,6),_RlLan1ModulePortRowStatus_Type())
rlLan1ModulePortRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rlLan1ModulePortRowStatus.setStatus(_A)
_RlLan1x86PfcTable_Object=MibTable
rlLan1x86PfcTable=_RlLan1x86PfcTable_Object((1,3,6,1,4,1,9,6,1,101,224,8))
if mibBuilder.loadTexts:rlLan1x86PfcTable.setStatus(_A)
_RlLan1x86PfcEntry_Object=MibTableRow
rlLan1x86PfcEntry=_RlLan1x86PfcEntry_Object((1,3,6,1,4,1,9,6,1,101,224,8,1))
rlLan1x86PfcEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:rlLan1x86PfcEntry.setStatus(_A)
class _RlLan1x86PriorityIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RlLan1x86PriorityIndex_Type.__name__=_C
_RlLan1x86PriorityIndex_Object=MibTableColumn
rlLan1x86PriorityIndex=_RlLan1x86PriorityIndex_Object((1,3,6,1,4,1,9,6,1,101,224,8,1,1),_RlLan1x86PriorityIndex_Type())
rlLan1x86PriorityIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rlLan1x86PriorityIndex.setStatus(_A)
class _RlLan1x86PriorityIsLossy_Type(TruthValue):defaultValue=1
_RlLan1x86PriorityIsLossy_Type.__name__=_F
_RlLan1x86PriorityIsLossy_Object=MibTableColumn
rlLan1x86PriorityIsLossy=_RlLan1x86PriorityIsLossy_Object((1,3,6,1,4,1,9,6,1,101,224,8,1,2),_RlLan1x86PriorityIsLossy_Type())
rlLan1x86PriorityIsLossy.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLan1x86PriorityIsLossy.setStatus(_A)
_RlLan1x86PriorityXoffThreshold_Type=Integer32
_RlLan1x86PriorityXoffThreshold_Object=MibTableColumn
rlLan1x86PriorityXoffThreshold=_RlLan1x86PriorityXoffThreshold_Object((1,3,6,1,4,1,9,6,1,101,224,8,1,3),_RlLan1x86PriorityXoffThreshold_Type())
rlLan1x86PriorityXoffThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLan1x86PriorityXoffThreshold.setStatus(_A)
_RlLan1x86PriorityXonThreshold_Type=Integer32
_RlLan1x86PriorityXonThreshold_Object=MibTableColumn
rlLan1x86PriorityXonThreshold=_RlLan1x86PriorityXonThreshold_Object((1,3,6,1,4,1,9,6,1,101,224,8,1,4),_RlLan1x86PriorityXonThreshold_Type())
rlLan1x86PriorityXonThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:rlLan1x86PriorityXonThreshold.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_M:GroupId,_N:GroupIdList,_I:VlanIdOrNone,'rlLan1':rlLan1,'rlLan1STagEtherType':rlLan1STagEtherType,'rlLan1CPVlanId':rlLan1CPVlanId,'rlLan1CPVlanCos':rlLan1CPVlanCos,'rlLan1x86Port':rlLan1x86Port,'rlLan1x86VlanMappingTable':rlLan1x86VlanMappingTable,'rlLan1x86VlanMappingEntry':rlLan1x86VlanMappingEntry,_J:rlLan1x86VlanMappingVlanId,'rlLan1x86VlanMappingGroupId':rlLan1x86VlanMappingGroupId,'rlLan1x86VlanMappingRowStatus':rlLan1x86VlanMappingRowStatus,'rlLan1VfMacMappingTable':rlLan1VfMacMappingTable,'rlLan1VfMacMappingEntry':rlLan1VfMacMappingEntry,_K:rlLan1VfMacMappingDstMacAddress,'rlLan1VfMacMappingVlanId':rlLan1VfMacMappingVlanId,'rlLan1VfMacMappingMulticast':rlLan1VfMacMappingMulticast,'rlLan1VfMacMappingRowStatus':rlLan1VfMacMappingRowStatus,'rlLan1ModulePortTable':rlLan1ModulePortTable,'rlLan1ModulePortEntry':rlLan1ModulePortEntry,_L:rlLan1ModulePortIfIndex,'rlLan1ModulePortCPAllowed':rlLan1ModulePortCPAllowed,'rlLan1ModulePortMulticastBroadcastAllowedVlan':rlLan1ModulePortMulticastBroadcastAllowedVlan,'rlLan1ModulePortIngressGroupId':rlLan1ModulePortIngressGroupId,'rlLan1ModulePortEgressGroupIdList':rlLan1ModulePortEgressGroupIdList,'rlLan1ModulePortRowStatus':rlLan1ModulePortRowStatus,'rlLan1x86PfcTable':rlLan1x86PfcTable,'rlLan1x86PfcEntry':rlLan1x86PfcEntry,_O:rlLan1x86PriorityIndex,'rlLan1x86PriorityIsLossy':rlLan1x86PriorityIsLossy,'rlLan1x86PriorityXoffThreshold':rlLan1x86PriorityXoffThreshold,'rlLan1x86PriorityXonThreshold':rlLan1x86PriorityXonThreshold})