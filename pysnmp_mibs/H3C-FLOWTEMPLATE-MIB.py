_L='h3cFTExtendGroupOffsetType'
_K='not-accessible'
_J='read-only'
_I='ifIndex'
_H='IF-MIB'
_G='OctetString'
_F='Integer32'
_E='Bits'
_D='h3cFTGroupIndex'
_C='H3C-FLOWTEMPLATE-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_E,'Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
h3cFlowTemplate=ModuleIdentity((1,3,6,1,4,1,2011,10,2,64))
_H3cFlowTemplateMibObject_ObjectIdentity=ObjectIdentity
h3cFlowTemplateMibObject=_H3cFlowTemplateMibObject_ObjectIdentity((1,3,6,1,4,1,2011,10,2,64,1))
_H3cFTConfigGroup_ObjectIdentity=ObjectIdentity
h3cFTConfigGroup=_H3cFTConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,64,1,1))
_H3cFTGroupNextIndex_Type=Integer32
_H3cFTGroupNextIndex_Object=MibScalar
h3cFTGroupNextIndex=_H3cFTGroupNextIndex_Object((1,3,6,1,4,1,2011,10,2,64,1,1,1),_H3cFTGroupNextIndex_Type())
h3cFTGroupNextIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cFTGroupNextIndex.setStatus(_A)
_H3cFTGroupTable_Object=MibTable
h3cFTGroupTable=_H3cFTGroupTable_Object((1,3,6,1,4,1,2011,10,2,64,1,1,2))
if mibBuilder.loadTexts:h3cFTGroupTable.setStatus(_A)
_H3cFTGroupEntry_Object=MibTableRow
h3cFTGroupEntry=_H3cFTGroupEntry_Object((1,3,6,1,4,1,2011,10,2,64,1,1,2,1))
h3cFTGroupEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:h3cFTGroupEntry.setStatus(_A)
_H3cFTGroupIndex_Type=Integer32
_H3cFTGroupIndex_Object=MibTableColumn
h3cFTGroupIndex=_H3cFTGroupIndex_Object((1,3,6,1,4,1,2011,10,2,64,1,1,2,1,1),_H3cFTGroupIndex_Type())
h3cFTGroupIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cFTGroupIndex.setStatus(_A)
class _H3cFTGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_H3cFTGroupName_Type.__name__=_G
_H3cFTGroupName_Object=MibTableColumn
h3cFTGroupName=_H3cFTGroupName_Object((1,3,6,1,4,1,2011,10,2,64,1,1,2,1,2),_H3cFTGroupName_Type())
h3cFTGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFTGroupName.setStatus(_A)
class _H3cFTGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('basic',1),('extend',2)))
_H3cFTGroupType_Type.__name__=_F
_H3cFTGroupType_Object=MibTableColumn
h3cFTGroupType=_H3cFTGroupType_Object((1,3,6,1,4,1,2011,10,2,64,1,1,2,1,3),_H3cFTGroupType_Type())
h3cFTGroupType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFTGroupType.setStatus(_A)
_H3cFTGroupRowStatus_Type=RowStatus
_H3cFTGroupRowStatus_Object=MibTableColumn
h3cFTGroupRowStatus=_H3cFTGroupRowStatus_Object((1,3,6,1,4,1,2011,10,2,64,1,1,2,1,4),_H3cFTGroupRowStatus_Type())
h3cFTGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFTGroupRowStatus.setStatus(_A)
_H3cFTBasicGroupTable_Object=MibTable
h3cFTBasicGroupTable=_H3cFTBasicGroupTable_Object((1,3,6,1,4,1,2011,10,2,64,1,1,3))
if mibBuilder.loadTexts:h3cFTBasicGroupTable.setStatus(_A)
_H3cFTBasicGroupEntry_Object=MibTableRow
h3cFTBasicGroupEntry=_H3cFTBasicGroupEntry_Object((1,3,6,1,4,1,2011,10,2,64,1,1,3,1))
h3cFTBasicGroupEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:h3cFTBasicGroupEntry.setStatus(_A)
class _H3cFTBasicGroupAddressType_Type(Bits):namedValues=NamedValues(*(('sourceIpv4Address',0),('destIPv4Address',1),('sourceIPv6Address',2),('destIPv6Address',3),('sourceMacAddress',4),('destMacAddress',5)))
_H3cFTBasicGroupAddressType_Type.__name__=_E
_H3cFTBasicGroupAddressType_Object=MibTableColumn
h3cFTBasicGroupAddressType=_H3cFTBasicGroupAddressType_Object((1,3,6,1,4,1,2011,10,2,64,1,1,3,1,1),_H3cFTBasicGroupAddressType_Type())
h3cFTBasicGroupAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFTBasicGroupAddressType.setStatus(_A)
class _H3cFTBasicGroupPriorityType_Type(Bits):namedValues=NamedValues(*(('vlanID',0),('cos',1),('topVlanID',2),('topCos',3),('fragment',4),('tcpFlag',5),('tos',6),('dscp',7),('ipprecedence',8)))
_H3cFTBasicGroupPriorityType_Type.__name__=_E
_H3cFTBasicGroupPriorityType_Object=MibTableColumn
h3cFTBasicGroupPriorityType=_H3cFTBasicGroupPriorityType_Object((1,3,6,1,4,1,2011,10,2,64,1,1,3,1,2),_H3cFTBasicGroupPriorityType_Type())
h3cFTBasicGroupPriorityType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFTBasicGroupPriorityType.setStatus(_A)
class _H3cFTBasicGroupProtocolType_Type(Bits):namedValues=NamedValues(*(('l2Potocol',0),('ipv4L3Protocol',1),('ipv6L3Protocol',2),('icmpProtocolType',3),('icmpProtocolCode',4),('icmpv6ProtocolType',5),('icmpv6ProtocolCode',6),('sourceL4Port',7),('destL4Port',8)))
_H3cFTBasicGroupProtocolType_Type.__name__=_E
_H3cFTBasicGroupProtocolType_Object=MibTableColumn
h3cFTBasicGroupProtocolType=_H3cFTBasicGroupProtocolType_Object((1,3,6,1,4,1,2011,10,2,64,1,1,3,1,3),_H3cFTBasicGroupProtocolType_Type())
h3cFTBasicGroupProtocolType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFTBasicGroupProtocolType.setStatus(_A)
_H3cFTBasicGroupSMacWildCard_Type=MacAddress
_H3cFTBasicGroupSMacWildCard_Object=MibTableColumn
h3cFTBasicGroupSMacWildCard=_H3cFTBasicGroupSMacWildCard_Object((1,3,6,1,4,1,2011,10,2,64,1,1,3,1,4),_H3cFTBasicGroupSMacWildCard_Type())
h3cFTBasicGroupSMacWildCard.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFTBasicGroupSMacWildCard.setStatus(_A)
_H3cFTBasicGroupDMacWildCard_Type=MacAddress
_H3cFTBasicGroupDMacWildCard_Object=MibTableColumn
h3cFTBasicGroupDMacWildCard=_H3cFTBasicGroupDMacWildCard_Object((1,3,6,1,4,1,2011,10,2,64,1,1,3,1,5),_H3cFTBasicGroupDMacWildCard_Type())
h3cFTBasicGroupDMacWildCard.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFTBasicGroupDMacWildCard.setStatus(_A)
_H3cFTBasicGroupRowStatus_Type=RowStatus
_H3cFTBasicGroupRowStatus_Object=MibTableColumn
h3cFTBasicGroupRowStatus=_H3cFTBasicGroupRowStatus_Object((1,3,6,1,4,1,2011,10,2,64,1,1,3,1,6),_H3cFTBasicGroupRowStatus_Type())
h3cFTBasicGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFTBasicGroupRowStatus.setStatus(_A)
_H3cFTExtendGroupTable_Object=MibTable
h3cFTExtendGroupTable=_H3cFTExtendGroupTable_Object((1,3,6,1,4,1,2011,10,2,64,1,1,4))
if mibBuilder.loadTexts:h3cFTExtendGroupTable.setStatus(_A)
_H3cFTExtendGroupEntry_Object=MibTableRow
h3cFTExtendGroupEntry=_H3cFTExtendGroupEntry_Object((1,3,6,1,4,1,2011,10,2,64,1,1,4,1))
h3cFTExtendGroupEntry.setIndexNames((0,_C,_D),(0,_C,_L))
if mibBuilder.loadTexts:h3cFTExtendGroupEntry.setStatus(_A)
class _H3cFTExtendGroupOffsetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('start',1),('mpls',2),('l2',3),('l4',4),('l5',5),('ipv4',6),('ipv6',7)))
_H3cFTExtendGroupOffsetType_Type.__name__=_F
_H3cFTExtendGroupOffsetType_Object=MibTableColumn
h3cFTExtendGroupOffsetType=_H3cFTExtendGroupOffsetType_Object((1,3,6,1,4,1,2011,10,2,64,1,1,4,1,1),_H3cFTExtendGroupOffsetType_Type())
h3cFTExtendGroupOffsetType.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cFTExtendGroupOffsetType.setStatus(_A)
_H3cFTExtendGroupOffsetMaxValue_Type=Integer32
_H3cFTExtendGroupOffsetMaxValue_Object=MibTableColumn
h3cFTExtendGroupOffsetMaxValue=_H3cFTExtendGroupOffsetMaxValue_Object((1,3,6,1,4,1,2011,10,2,64,1,1,4,1,2),_H3cFTExtendGroupOffsetMaxValue_Type())
h3cFTExtendGroupOffsetMaxValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFTExtendGroupOffsetMaxValue.setStatus(_A)
_H3cFTExtendGroupLengthMaxValue_Type=Integer32
_H3cFTExtendGroupLengthMaxValue_Object=MibTableColumn
h3cFTExtendGroupLengthMaxValue=_H3cFTExtendGroupLengthMaxValue_Object((1,3,6,1,4,1,2011,10,2,64,1,1,4,1,3),_H3cFTExtendGroupLengthMaxValue_Type())
h3cFTExtendGroupLengthMaxValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFTExtendGroupLengthMaxValue.setStatus(_A)
_H3cFTExtendGroupRowStatus_Type=RowStatus
_H3cFTExtendGroupRowStatus_Object=MibTableColumn
h3cFTExtendGroupRowStatus=_H3cFTExtendGroupRowStatus_Object((1,3,6,1,4,1,2011,10,2,64,1,1,4,1,4),_H3cFTExtendGroupRowStatus_Type())
h3cFTExtendGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFTExtendGroupRowStatus.setStatus(_A)
_H3cFTApplyGroup_ObjectIdentity=ObjectIdentity
h3cFTApplyGroup=_H3cFTApplyGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,64,1,2))
_H3cFTIfApplyTable_Object=MibTable
h3cFTIfApplyTable=_H3cFTIfApplyTable_Object((1,3,6,1,4,1,2011,10,2,64,1,2,1))
if mibBuilder.loadTexts:h3cFTIfApplyTable.setStatus(_A)
_H3cFTIfApplyEntry_Object=MibTableRow
h3cFTIfApplyEntry=_H3cFTIfApplyEntry_Object((1,3,6,1,4,1,2011,10,2,64,1,2,1,1))
h3cFTIfApplyEntry.setIndexNames((0,_H,_I),(0,_C,_D))
if mibBuilder.loadTexts:h3cFTIfApplyEntry.setStatus(_A)
_H3cFTIfApplyGroupName_Type=OctetString
_H3cFTIfApplyGroupName_Object=MibTableColumn
h3cFTIfApplyGroupName=_H3cFTIfApplyGroupName_Object((1,3,6,1,4,1,2011,10,2,64,1,2,1,1,1),_H3cFTIfApplyGroupName_Type())
h3cFTIfApplyGroupName.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cFTIfApplyGroupName.setStatus(_A)
_H3cFTIfApplyRowStatus_Type=RowStatus
_H3cFTIfApplyRowStatus_Object=MibTableColumn
h3cFTIfApplyRowStatus=_H3cFTIfApplyRowStatus_Object((1,3,6,1,4,1,2011,10,2,64,1,2,1,1,2),_H3cFTIfApplyRowStatus_Type())
h3cFTIfApplyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFTIfApplyRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'h3cFlowTemplate':h3cFlowTemplate,'h3cFlowTemplateMibObject':h3cFlowTemplateMibObject,'h3cFTConfigGroup':h3cFTConfigGroup,'h3cFTGroupNextIndex':h3cFTGroupNextIndex,'h3cFTGroupTable':h3cFTGroupTable,'h3cFTGroupEntry':h3cFTGroupEntry,_D:h3cFTGroupIndex,'h3cFTGroupName':h3cFTGroupName,'h3cFTGroupType':h3cFTGroupType,'h3cFTGroupRowStatus':h3cFTGroupRowStatus,'h3cFTBasicGroupTable':h3cFTBasicGroupTable,'h3cFTBasicGroupEntry':h3cFTBasicGroupEntry,'h3cFTBasicGroupAddressType':h3cFTBasicGroupAddressType,'h3cFTBasicGroupPriorityType':h3cFTBasicGroupPriorityType,'h3cFTBasicGroupProtocolType':h3cFTBasicGroupProtocolType,'h3cFTBasicGroupSMacWildCard':h3cFTBasicGroupSMacWildCard,'h3cFTBasicGroupDMacWildCard':h3cFTBasicGroupDMacWildCard,'h3cFTBasicGroupRowStatus':h3cFTBasicGroupRowStatus,'h3cFTExtendGroupTable':h3cFTExtendGroupTable,'h3cFTExtendGroupEntry':h3cFTExtendGroupEntry,_L:h3cFTExtendGroupOffsetType,'h3cFTExtendGroupOffsetMaxValue':h3cFTExtendGroupOffsetMaxValue,'h3cFTExtendGroupLengthMaxValue':h3cFTExtendGroupLengthMaxValue,'h3cFTExtendGroupRowStatus':h3cFTExtendGroupRowStatus,'h3cFTApplyGroup':h3cFTApplyGroup,'h3cFTIfApplyTable':h3cFTIfApplyTable,'h3cFTIfApplyEntry':h3cFTIfApplyEntry,'h3cFTIfApplyGroupName':h3cFTIfApplyGroupName,'h3cFTIfApplyRowStatus':h3cFTIfApplyRowStatus})