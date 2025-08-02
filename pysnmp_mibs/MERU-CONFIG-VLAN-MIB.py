_I='mwVlanPoolTableIndex'
_H='mwVlanMgmtTableIndex'
_G='mwVlanTableIndex'
_F='not-accessible'
_E='read-only'
_D='MERU-CONFIG-VLAN-MIB'
_C='DisplayString'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
mwConfiguration,=mibBuilder.importSymbols('MERU-SMI','mwConfiguration')
MwlAddressIfAssignmentType,MwlArrayDataTypeAction,MwlNmsInterfaceType,MwlOnOffSwitch,MwlProfileOwner=mibBuilder.importSymbols('MERU-TC','MwlAddressIfAssignmentType','MwlArrayDataTypeAction','MwlNmsInterfaceType','MwlOnOffSwitch','MwlProfileOwner')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_C,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
mwConfigVlan=ModuleIdentity((1,3,6,1,4,1,15983,1,1,4,5))
_MwVlanTable_Object=MibTable
mwVlanTable=_MwVlanTable_Object((1,3,6,1,4,1,15983,1,1,4,5,1))
if mibBuilder.loadTexts:mwVlanTable.setStatus(_A)
_MwVlanEntry_Object=MibTableRow
mwVlanEntry=_MwVlanEntry_Object((1,3,6,1,4,1,15983,1,1,4,5,1,1))
mwVlanEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:mwVlanEntry.setStatus(_A)
_MwVlanTableIndex_Type=Integer32
_MwVlanTableIndex_Object=MibTableColumn
mwVlanTableIndex=_MwVlanTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,5,1,1,1),_MwVlanTableIndex_Type())
mwVlanTableIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mwVlanTableIndex.setStatus(_A)
_MwVlanTag_Type=Unsigned32
_MwVlanTag_Object=MibTableColumn
mwVlanTag=_MwVlanTag_Object((1,3,6,1,4,1,15983,1,1,4,5,1,1,2),_MwVlanTag_Type())
mwVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVlanTag.setStatus(_A)
class _MwVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MwVlanName_Type.__name__=_C
_MwVlanName_Object=MibTableColumn
mwVlanName=_MwVlanName_Object((1,3,6,1,4,1,15983,1,1,4,5,1,1,3),_MwVlanName_Type())
mwVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVlanName.setStatus(_A)
_MwVlanNetMask_Type=IpAddress
_MwVlanNetMask_Object=MibTableColumn
mwVlanNetMask=_MwVlanNetMask_Object((1,3,6,1,4,1,15983,1,1,4,5,1,1,4),_MwVlanNetMask_Type())
mwVlanNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVlanNetMask.setStatus(_A)
_MwVlanIpAddress_Type=IpAddress
_MwVlanIpAddress_Object=MibTableColumn
mwVlanIpAddress=_MwVlanIpAddress_Object((1,3,6,1,4,1,15983,1,1,4,5,1,1,5),_MwVlanIpAddress_Type())
mwVlanIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVlanIpAddress.setStatus(_A)
_MwVlanInterfaceIndex_Type=Unsigned32
_MwVlanInterfaceIndex_Object=MibTableColumn
mwVlanInterfaceIndex=_MwVlanInterfaceIndex_Object((1,3,6,1,4,1,15983,1,1,4,5,1,1,6),_MwVlanInterfaceIndex_Type())
mwVlanInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVlanInterfaceIndex.setStatus(_A)
_MwVlanDefaultGateway_Type=IpAddress
_MwVlanDefaultGateway_Object=MibTableColumn
mwVlanDefaultGateway=_MwVlanDefaultGateway_Object((1,3,6,1,4,1,15983,1,1,4,5,1,1,7),_MwVlanDefaultGateway_Type())
mwVlanDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVlanDefaultGateway.setStatus(_A)
_MwVlanDHCPServerIpAddress_Type=IpAddress
_MwVlanDHCPServerIpAddress_Object=MibTableColumn
mwVlanDHCPServerIpAddress=_MwVlanDHCPServerIpAddress_Object((1,3,6,1,4,1,15983,1,1,4,5,1,1,8),_MwVlanDHCPServerIpAddress_Type())
mwVlanDHCPServerIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVlanDHCPServerIpAddress.setStatus(_A)
_MwVlanDhcpRelayPassThroughFlag_Type=MwlOnOffSwitch
_MwVlanDhcpRelayPassThroughFlag_Object=MibTableColumn
mwVlanDhcpRelayPassThroughFlag=_MwVlanDhcpRelayPassThroughFlag_Object((1,3,6,1,4,1,15983,1,1,4,5,1,1,9),_MwVlanDhcpRelayPassThroughFlag_Type())
mwVlanDhcpRelayPassThroughFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVlanDhcpRelayPassThroughFlag.setStatus(_A)
_MwVlanOverrideDefaultDHCPServer_Type=MwlOnOffSwitch
_MwVlanOverrideDefaultDHCPServer_Object=MibTableColumn
mwVlanOverrideDefaultDHCPServer=_MwVlanOverrideDefaultDHCPServer_Object((1,3,6,1,4,1,15983,1,1,4,5,1,1,10),_MwVlanOverrideDefaultDHCPServer_Type())
mwVlanOverrideDefaultDHCPServer.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVlanOverrideDefaultDHCPServer.setStatus(_A)
_MwVlanOwner_Type=MwlProfileOwner
_MwVlanOwner_Object=MibTableColumn
mwVlanOwner=_MwVlanOwner_Object((1,3,6,1,4,1,15983,1,1,4,5,1,1,11),_MwVlanOwner_Type())
mwVlanOwner.setMaxAccess(_E)
if mibBuilder.loadTexts:mwVlanOwner.setStatus(_A)
_MwVlanMaxNumberOfClients_Type=Unsigned32
_MwVlanMaxNumberOfClients_Object=MibTableColumn
mwVlanMaxNumberOfClients=_MwVlanMaxNumberOfClients_Object((1,3,6,1,4,1,15983,1,1,4,5,1,1,13),_MwVlanMaxNumberOfClients_Type())
mwVlanMaxNumberOfClients.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVlanMaxNumberOfClients.setStatus(_A)
_MwVlanRowStatus_Type=RowStatus
_MwVlanRowStatus_Object=MibTableColumn
mwVlanRowStatus=_MwVlanRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,5,1,1,15),_MwVlanRowStatus_Type())
mwVlanRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVlanRowStatus.setStatus(_A)
_MwVlanMgmtTable_Object=MibTable
mwVlanMgmtTable=_MwVlanMgmtTable_Object((1,3,6,1,4,1,15983,1,1,4,5,2))
if mibBuilder.loadTexts:mwVlanMgmtTable.setStatus(_A)
_MwVlanMgmtEntry_Object=MibTableRow
mwVlanMgmtEntry=_MwVlanMgmtEntry_Object((1,3,6,1,4,1,15983,1,1,4,5,2,1))
mwVlanMgmtEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:mwVlanMgmtEntry.setStatus(_A)
_MwVlanMgmtTableIndex_Type=Integer32
_MwVlanMgmtTableIndex_Object=MibTableColumn
mwVlanMgmtTableIndex=_MwVlanMgmtTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,5,2,1,1),_MwVlanMgmtTableIndex_Type())
mwVlanMgmtTableIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mwVlanMgmtTableIndex.setStatus(_A)
_MwVlanMgmtTag_Type=Unsigned32
_MwVlanMgmtTag_Object=MibTableColumn
mwVlanMgmtTag=_MwVlanMgmtTag_Object((1,3,6,1,4,1,15983,1,1,4,5,2,1,2),_MwVlanMgmtTag_Type())
mwVlanMgmtTag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVlanMgmtTag.setStatus(_A)
class _MwVlanMgmtName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MwVlanMgmtName_Type.__name__=_C
_MwVlanMgmtName_Object=MibTableColumn
mwVlanMgmtName=_MwVlanMgmtName_Object((1,3,6,1,4,1,15983,1,1,4,5,2,1,3),_MwVlanMgmtName_Type())
mwVlanMgmtName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVlanMgmtName.setStatus(_A)
_MwVlanMgmtInterfaceIndex_Type=Unsigned32
_MwVlanMgmtInterfaceIndex_Object=MibTableColumn
mwVlanMgmtInterfaceIndex=_MwVlanMgmtInterfaceIndex_Object((1,3,6,1,4,1,15983,1,1,4,5,2,1,4),_MwVlanMgmtInterfaceIndex_Type())
mwVlanMgmtInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVlanMgmtInterfaceIndex.setStatus(_A)
_MwVlanMgmtIpAddress_Type=IpAddress
_MwVlanMgmtIpAddress_Object=MibTableColumn
mwVlanMgmtIpAddress=_MwVlanMgmtIpAddress_Object((1,3,6,1,4,1,15983,1,1,4,5,2,1,5),_MwVlanMgmtIpAddress_Type())
mwVlanMgmtIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVlanMgmtIpAddress.setStatus(_A)
_MwVlanMgmtNetMask_Type=IpAddress
_MwVlanMgmtNetMask_Object=MibTableColumn
mwVlanMgmtNetMask=_MwVlanMgmtNetMask_Object((1,3,6,1,4,1,15983,1,1,4,5,2,1,6),_MwVlanMgmtNetMask_Type())
mwVlanMgmtNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVlanMgmtNetMask.setStatus(_A)
_MwVlanMgmtDefaultGateway_Type=IpAddress
_MwVlanMgmtDefaultGateway_Object=MibTableColumn
mwVlanMgmtDefaultGateway=_MwVlanMgmtDefaultGateway_Object((1,3,6,1,4,1,15983,1,1,4,5,2,1,7),_MwVlanMgmtDefaultGateway_Type())
mwVlanMgmtDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVlanMgmtDefaultGateway.setStatus(_A)
_MwVlanMgmtAssignedType_Type=MwlAddressIfAssignmentType
_MwVlanMgmtAssignedType_Object=MibTableColumn
mwVlanMgmtAssignedType=_MwVlanMgmtAssignedType_Object((1,3,6,1,4,1,15983,1,1,4,5,2,1,8),_MwVlanMgmtAssignedType_Type())
mwVlanMgmtAssignedType.setMaxAccess(_E)
if mibBuilder.loadTexts:mwVlanMgmtAssignedType.setStatus(_A)
_MwVlanMgmtInterfaceType_Type=MwlNmsInterfaceType
_MwVlanMgmtInterfaceType_Object=MibTableColumn
mwVlanMgmtInterfaceType=_MwVlanMgmtInterfaceType_Object((1,3,6,1,4,1,15983,1,1,4,5,2,1,9),_MwVlanMgmtInterfaceType_Type())
mwVlanMgmtInterfaceType.setMaxAccess(_E)
if mibBuilder.loadTexts:mwVlanMgmtInterfaceType.setStatus(_A)
_MwVlanMgmtRowStatus_Type=RowStatus
_MwVlanMgmtRowStatus_Object=MibTableColumn
mwVlanMgmtRowStatus=_MwVlanMgmtRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,5,2,1,11),_MwVlanMgmtRowStatus_Type())
mwVlanMgmtRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVlanMgmtRowStatus.setStatus(_A)
_MwVlanPoolTable_Object=MibTable
mwVlanPoolTable=_MwVlanPoolTable_Object((1,3,6,1,4,1,15983,1,1,4,5,3))
if mibBuilder.loadTexts:mwVlanPoolTable.setStatus(_A)
_MwVlanPoolEntry_Object=MibTableRow
mwVlanPoolEntry=_MwVlanPoolEntry_Object((1,3,6,1,4,1,15983,1,1,4,5,3,1))
mwVlanPoolEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:mwVlanPoolEntry.setStatus(_A)
_MwVlanPoolTableIndex_Type=Integer32
_MwVlanPoolTableIndex_Object=MibTableColumn
mwVlanPoolTableIndex=_MwVlanPoolTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,5,3,1,1),_MwVlanPoolTableIndex_Type())
mwVlanPoolTableIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mwVlanPoolTableIndex.setStatus(_A)
class _MwVlanPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_MwVlanPoolName_Type.__name__=_C
_MwVlanPoolName_Object=MibTableColumn
mwVlanPoolName=_MwVlanPoolName_Object((1,3,6,1,4,1,15983,1,1,4,5,3,1,3),_MwVlanPoolName_Type())
mwVlanPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVlanPoolName.setStatus(_A)
_MwVlanPoolTagList_Type=DisplayString
_MwVlanPoolTagList_Object=MibTableColumn
mwVlanPoolTagList=_MwVlanPoolTagList_Object((1,3,6,1,4,1,15983,1,1,4,5,3,1,4),_MwVlanPoolTagList_Type())
mwVlanPoolTagList.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVlanPoolTagList.setStatus(_A)
_MwVlanPoolOwner_Type=MwlProfileOwner
_MwVlanPoolOwner_Object=MibTableColumn
mwVlanPoolOwner=_MwVlanPoolOwner_Object((1,3,6,1,4,1,15983,1,1,4,5,3,1,5),_MwVlanPoolOwner_Type())
mwVlanPoolOwner.setMaxAccess(_E)
if mibBuilder.loadTexts:mwVlanPoolOwner.setStatus(_A)
_MwVlanPoolRowStatus_Type=RowStatus
_MwVlanPoolRowStatus_Object=MibTableColumn
mwVlanPoolRowStatus=_MwVlanPoolRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,5,3,1,6),_MwVlanPoolRowStatus_Type())
mwVlanPoolRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwVlanPoolRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'mwConfigVlan':mwConfigVlan,'mwVlanTable':mwVlanTable,'mwVlanEntry':mwVlanEntry,_G:mwVlanTableIndex,'mwVlanTag':mwVlanTag,'mwVlanName':mwVlanName,'mwVlanNetMask':mwVlanNetMask,'mwVlanIpAddress':mwVlanIpAddress,'mwVlanInterfaceIndex':mwVlanInterfaceIndex,'mwVlanDefaultGateway':mwVlanDefaultGateway,'mwVlanDHCPServerIpAddress':mwVlanDHCPServerIpAddress,'mwVlanDhcpRelayPassThroughFlag':mwVlanDhcpRelayPassThroughFlag,'mwVlanOverrideDefaultDHCPServer':mwVlanOverrideDefaultDHCPServer,'mwVlanOwner':mwVlanOwner,'mwVlanMaxNumberOfClients':mwVlanMaxNumberOfClients,'mwVlanRowStatus':mwVlanRowStatus,'mwVlanMgmtTable':mwVlanMgmtTable,'mwVlanMgmtEntry':mwVlanMgmtEntry,_H:mwVlanMgmtTableIndex,'mwVlanMgmtTag':mwVlanMgmtTag,'mwVlanMgmtName':mwVlanMgmtName,'mwVlanMgmtInterfaceIndex':mwVlanMgmtInterfaceIndex,'mwVlanMgmtIpAddress':mwVlanMgmtIpAddress,'mwVlanMgmtNetMask':mwVlanMgmtNetMask,'mwVlanMgmtDefaultGateway':mwVlanMgmtDefaultGateway,'mwVlanMgmtAssignedType':mwVlanMgmtAssignedType,'mwVlanMgmtInterfaceType':mwVlanMgmtInterfaceType,'mwVlanMgmtRowStatus':mwVlanMgmtRowStatus,'mwVlanPoolTable':mwVlanPoolTable,'mwVlanPoolEntry':mwVlanPoolEntry,_I:mwVlanPoolTableIndex,'mwVlanPoolName':mwVlanPoolName,'mwVlanPoolTagList':mwVlanPoolTagList,'mwVlanPoolOwner':mwVlanPoolOwner,'mwVlanPoolRowStatus':mwVlanPoolRowStatus})