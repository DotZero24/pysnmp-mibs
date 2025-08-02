_L='hpnicfFTExtendGroupOffsetType'
_K='not-accessible'
_J='read-only'
_I='ifIndex'
_H='IF-MIB'
_G='OctetString'
_F='Integer32'
_E='Bits'
_D='hpnicfFTGroupIndex'
_C='HPN-ICF-FLOWTEMPLATE-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_E,'Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
hpnicfFlowTemplate=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,64))
_HpnicfFlowTemplateMibObject_ObjectIdentity=ObjectIdentity
hpnicfFlowTemplateMibObject=_HpnicfFlowTemplateMibObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,64,1))
_HpnicfFTConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfFTConfigGroup=_HpnicfFTConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,64,1,1))
_HpnicfFTGroupNextIndex_Type=Integer32
_HpnicfFTGroupNextIndex_Object=MibScalar
hpnicfFTGroupNextIndex=_HpnicfFTGroupNextIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,1,1),_HpnicfFTGroupNextIndex_Type())
hpnicfFTGroupNextIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfFTGroupNextIndex.setStatus(_A)
_HpnicfFTGroupTable_Object=MibTable
hpnicfFTGroupTable=_HpnicfFTGroupTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,1,2))
if mibBuilder.loadTexts:hpnicfFTGroupTable.setStatus(_A)
_HpnicfFTGroupEntry_Object=MibTableRow
hpnicfFTGroupEntry=_HpnicfFTGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,1,2,1))
hpnicfFTGroupEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:hpnicfFTGroupEntry.setStatus(_A)
_HpnicfFTGroupIndex_Type=Integer32
_HpnicfFTGroupIndex_Object=MibTableColumn
hpnicfFTGroupIndex=_HpnicfFTGroupIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,1,2,1,1),_HpnicfFTGroupIndex_Type())
hpnicfFTGroupIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfFTGroupIndex.setStatus(_A)
class _HpnicfFTGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfFTGroupName_Type.__name__=_G
_HpnicfFTGroupName_Object=MibTableColumn
hpnicfFTGroupName=_HpnicfFTGroupName_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,1,2,1,2),_HpnicfFTGroupName_Type())
hpnicfFTGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFTGroupName.setStatus(_A)
class _HpnicfFTGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('basic',1),('extend',2)))
_HpnicfFTGroupType_Type.__name__=_F
_HpnicfFTGroupType_Object=MibTableColumn
hpnicfFTGroupType=_HpnicfFTGroupType_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,1,2,1,3),_HpnicfFTGroupType_Type())
hpnicfFTGroupType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFTGroupType.setStatus(_A)
_HpnicfFTGroupRowStatus_Type=RowStatus
_HpnicfFTGroupRowStatus_Object=MibTableColumn
hpnicfFTGroupRowStatus=_HpnicfFTGroupRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,1,2,1,4),_HpnicfFTGroupRowStatus_Type())
hpnicfFTGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFTGroupRowStatus.setStatus(_A)
_HpnicfFTBasicGroupTable_Object=MibTable
hpnicfFTBasicGroupTable=_HpnicfFTBasicGroupTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,1,3))
if mibBuilder.loadTexts:hpnicfFTBasicGroupTable.setStatus(_A)
_HpnicfFTBasicGroupEntry_Object=MibTableRow
hpnicfFTBasicGroupEntry=_HpnicfFTBasicGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,1,3,1))
hpnicfFTBasicGroupEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:hpnicfFTBasicGroupEntry.setStatus(_A)
class _HpnicfFTBasicGroupAddressType_Type(Bits):namedValues=NamedValues(*(('sourceIpv4Address',0),('destIPv4Address',1),('sourceIPv6Address',2),('destIPv6Address',3),('sourceMacAddress',4),('destMacAddress',5)))
_HpnicfFTBasicGroupAddressType_Type.__name__=_E
_HpnicfFTBasicGroupAddressType_Object=MibTableColumn
hpnicfFTBasicGroupAddressType=_HpnicfFTBasicGroupAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,1,3,1,1),_HpnicfFTBasicGroupAddressType_Type())
hpnicfFTBasicGroupAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFTBasicGroupAddressType.setStatus(_A)
class _HpnicfFTBasicGroupPriorityType_Type(Bits):namedValues=NamedValues(*(('vlanID',0),('cos',1),('topVlanID',2),('topCos',3),('fragment',4),('tcpFlag',5),('tos',6),('dscp',7),('ipprecedence',8)))
_HpnicfFTBasicGroupPriorityType_Type.__name__=_E
_HpnicfFTBasicGroupPriorityType_Object=MibTableColumn
hpnicfFTBasicGroupPriorityType=_HpnicfFTBasicGroupPriorityType_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,1,3,1,2),_HpnicfFTBasicGroupPriorityType_Type())
hpnicfFTBasicGroupPriorityType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFTBasicGroupPriorityType.setStatus(_A)
class _HpnicfFTBasicGroupProtocolType_Type(Bits):namedValues=NamedValues(*(('l2Potocol',0),('ipv4L3Protocol',1),('ipv6L3Protocol',2),('icmpProtocolType',3),('icmpProtocolCode',4),('icmpv6ProtocolType',5),('icmpv6ProtocolCode',6),('sourceL4Port',7),('destL4Port',8)))
_HpnicfFTBasicGroupProtocolType_Type.__name__=_E
_HpnicfFTBasicGroupProtocolType_Object=MibTableColumn
hpnicfFTBasicGroupProtocolType=_HpnicfFTBasicGroupProtocolType_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,1,3,1,3),_HpnicfFTBasicGroupProtocolType_Type())
hpnicfFTBasicGroupProtocolType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFTBasicGroupProtocolType.setStatus(_A)
_HpnicfFTBasicGroupSMacWildCard_Type=MacAddress
_HpnicfFTBasicGroupSMacWildCard_Object=MibTableColumn
hpnicfFTBasicGroupSMacWildCard=_HpnicfFTBasicGroupSMacWildCard_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,1,3,1,4),_HpnicfFTBasicGroupSMacWildCard_Type())
hpnicfFTBasicGroupSMacWildCard.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFTBasicGroupSMacWildCard.setStatus(_A)
_HpnicfFTBasicGroupDMacWildCard_Type=MacAddress
_HpnicfFTBasicGroupDMacWildCard_Object=MibTableColumn
hpnicfFTBasicGroupDMacWildCard=_HpnicfFTBasicGroupDMacWildCard_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,1,3,1,5),_HpnicfFTBasicGroupDMacWildCard_Type())
hpnicfFTBasicGroupDMacWildCard.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFTBasicGroupDMacWildCard.setStatus(_A)
_HpnicfFTBasicGroupRowStatus_Type=RowStatus
_HpnicfFTBasicGroupRowStatus_Object=MibTableColumn
hpnicfFTBasicGroupRowStatus=_HpnicfFTBasicGroupRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,1,3,1,6),_HpnicfFTBasicGroupRowStatus_Type())
hpnicfFTBasicGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFTBasicGroupRowStatus.setStatus(_A)
_HpnicfFTExtendGroupTable_Object=MibTable
hpnicfFTExtendGroupTable=_HpnicfFTExtendGroupTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,1,4))
if mibBuilder.loadTexts:hpnicfFTExtendGroupTable.setStatus(_A)
_HpnicfFTExtendGroupEntry_Object=MibTableRow
hpnicfFTExtendGroupEntry=_HpnicfFTExtendGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,1,4,1))
hpnicfFTExtendGroupEntry.setIndexNames((0,_C,_D),(0,_C,_L))
if mibBuilder.loadTexts:hpnicfFTExtendGroupEntry.setStatus(_A)
class _HpnicfFTExtendGroupOffsetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('start',1),('mpls',2),('l2',3),('l4',4),('l5',5),('ipv4',6),('ipv6',7)))
_HpnicfFTExtendGroupOffsetType_Type.__name__=_F
_HpnicfFTExtendGroupOffsetType_Object=MibTableColumn
hpnicfFTExtendGroupOffsetType=_HpnicfFTExtendGroupOffsetType_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,1,4,1,1),_HpnicfFTExtendGroupOffsetType_Type())
hpnicfFTExtendGroupOffsetType.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfFTExtendGroupOffsetType.setStatus(_A)
_HpnicfFTExtendGroupOffsetMaxValue_Type=Integer32
_HpnicfFTExtendGroupOffsetMaxValue_Object=MibTableColumn
hpnicfFTExtendGroupOffsetMaxValue=_HpnicfFTExtendGroupOffsetMaxValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,1,4,1,2),_HpnicfFTExtendGroupOffsetMaxValue_Type())
hpnicfFTExtendGroupOffsetMaxValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFTExtendGroupOffsetMaxValue.setStatus(_A)
_HpnicfFTExtendGroupLengthMaxValue_Type=Integer32
_HpnicfFTExtendGroupLengthMaxValue_Object=MibTableColumn
hpnicfFTExtendGroupLengthMaxValue=_HpnicfFTExtendGroupLengthMaxValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,1,4,1,3),_HpnicfFTExtendGroupLengthMaxValue_Type())
hpnicfFTExtendGroupLengthMaxValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFTExtendGroupLengthMaxValue.setStatus(_A)
_HpnicfFTExtendGroupRowStatus_Type=RowStatus
_HpnicfFTExtendGroupRowStatus_Object=MibTableColumn
hpnicfFTExtendGroupRowStatus=_HpnicfFTExtendGroupRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,1,4,1,4),_HpnicfFTExtendGroupRowStatus_Type())
hpnicfFTExtendGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFTExtendGroupRowStatus.setStatus(_A)
_HpnicfFTApplyGroup_ObjectIdentity=ObjectIdentity
hpnicfFTApplyGroup=_HpnicfFTApplyGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,64,1,2))
_HpnicfFTIfApplyTable_Object=MibTable
hpnicfFTIfApplyTable=_HpnicfFTIfApplyTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,2,1))
if mibBuilder.loadTexts:hpnicfFTIfApplyTable.setStatus(_A)
_HpnicfFTIfApplyEntry_Object=MibTableRow
hpnicfFTIfApplyEntry=_HpnicfFTIfApplyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,2,1,1))
hpnicfFTIfApplyEntry.setIndexNames((0,_H,_I),(0,_C,_D))
if mibBuilder.loadTexts:hpnicfFTIfApplyEntry.setStatus(_A)
_HpnicfFTIfApplyGroupName_Type=OctetString
_HpnicfFTIfApplyGroupName_Object=MibTableColumn
hpnicfFTIfApplyGroupName=_HpnicfFTIfApplyGroupName_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,2,1,1,1),_HpnicfFTIfApplyGroupName_Type())
hpnicfFTIfApplyGroupName.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfFTIfApplyGroupName.setStatus(_A)
_HpnicfFTIfApplyRowStatus_Type=RowStatus
_HpnicfFTIfApplyRowStatus_Object=MibTableColumn
hpnicfFTIfApplyRowStatus=_HpnicfFTIfApplyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,64,1,2,1,1,2),_HpnicfFTIfApplyRowStatus_Type())
hpnicfFTIfApplyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFTIfApplyRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'hpnicfFlowTemplate':hpnicfFlowTemplate,'hpnicfFlowTemplateMibObject':hpnicfFlowTemplateMibObject,'hpnicfFTConfigGroup':hpnicfFTConfigGroup,'hpnicfFTGroupNextIndex':hpnicfFTGroupNextIndex,'hpnicfFTGroupTable':hpnicfFTGroupTable,'hpnicfFTGroupEntry':hpnicfFTGroupEntry,_D:hpnicfFTGroupIndex,'hpnicfFTGroupName':hpnicfFTGroupName,'hpnicfFTGroupType':hpnicfFTGroupType,'hpnicfFTGroupRowStatus':hpnicfFTGroupRowStatus,'hpnicfFTBasicGroupTable':hpnicfFTBasicGroupTable,'hpnicfFTBasicGroupEntry':hpnicfFTBasicGroupEntry,'hpnicfFTBasicGroupAddressType':hpnicfFTBasicGroupAddressType,'hpnicfFTBasicGroupPriorityType':hpnicfFTBasicGroupPriorityType,'hpnicfFTBasicGroupProtocolType':hpnicfFTBasicGroupProtocolType,'hpnicfFTBasicGroupSMacWildCard':hpnicfFTBasicGroupSMacWildCard,'hpnicfFTBasicGroupDMacWildCard':hpnicfFTBasicGroupDMacWildCard,'hpnicfFTBasicGroupRowStatus':hpnicfFTBasicGroupRowStatus,'hpnicfFTExtendGroupTable':hpnicfFTExtendGroupTable,'hpnicfFTExtendGroupEntry':hpnicfFTExtendGroupEntry,_L:hpnicfFTExtendGroupOffsetType,'hpnicfFTExtendGroupOffsetMaxValue':hpnicfFTExtendGroupOffsetMaxValue,'hpnicfFTExtendGroupLengthMaxValue':hpnicfFTExtendGroupLengthMaxValue,'hpnicfFTExtendGroupRowStatus':hpnicfFTExtendGroupRowStatus,'hpnicfFTApplyGroup':hpnicfFTApplyGroup,'hpnicfFTIfApplyTable':hpnicfFTIfApplyTable,'hpnicfFTIfApplyEntry':hpnicfFTIfApplyEntry,'hpnicfFTIfApplyGroupName':hpnicfFTIfApplyGroupName,'hpnicfFTIfApplyRowStatus':hpnicfFTIfApplyRowStatus})