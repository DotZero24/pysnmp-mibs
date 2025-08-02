_U='ctVlanClassifyBaseGroup'
_T='ctVlanClassifyActionStatus'
_S='ctVlanClassifyPorts'
_R='ctVlanClassifyRowInfo'
_Q='ctVlanClassifyRowStatus'
_P='ctVlanClassifyIngressList'
_O='ctVlanClassifyNumEntries'
_N='ctVlanClassifyMaxEntries'
_M='ctVlanClassifyStatus'
_L='ctVlanClassifyAbility'
_K='read-create'
_J='ctVlanClassifyDataMask'
_I='ctVlanClassifyDataVal'
_H='ctVlanClassifyDataMeaning'
_G='ctVlanClassifyVlanIndex'
_F='PortList'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='CTRON-VLAN-CLASSIFY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctVlanExt,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctVlanExt')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ctVlanClassify=ModuleIdentity((1,3,6,1,4,1,52,4,1,2,16,6))
if mibBuilder.loadTexts:ctVlanClassify.setRevisions(('2002-12-19 16:31','2002-03-27 20:55'))
class CtVlanClassifyType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34)));namedValues=NamedValues(*(('etherType',1),('llcDsapSsap',2),('ipTypeOfService',3),('ipProtocolType',4),('ipxClassOfService',5),('ipxPacketType',6),('ipAddressSource',7),('ipAddressDestination',8),('ipAddressBilateral',9),('ipxNetworkSource',10),('ipxNetworkDestination',11),('ipxNetworkBilateral',12),('ipUdpPortSource',13),('ipUdpPortDestination',14),('ipUdpPortBilateral',15),('ipTcpPortSource',16),('ipTcpPortDestination',17),('ipTcpPortBilateral',18),('ipxSocketSource',19),('ipxSocketDestination',20),('ipxSocketBilateral',21),('macAddressSource',22),('macAddressDestination',23),('macAddressBilateral',24),('ipFragments',25),('ipUdpPortSourceRange',26),('ipUdpPortDestinationRange',27),('ipUdpPortBilateralRange',28),('ipTcpPortSourceRange',29),('ipTcpPortDestinationRange',30),('ipTcpPortBilateralRange',31),('icmpType',32),('vlanId',33),('tci',34)))
class VlanIndex(TextualConvention,Unsigned32):status=_A
_CtVlanClassifyObjects_ObjectIdentity=ObjectIdentity
ctVlanClassifyObjects=_CtVlanClassifyObjects_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,16,6,1))
class _CtVlanClassifyStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_CtVlanClassifyStatus_Type.__name__=_E
_CtVlanClassifyStatus_Object=MibScalar
ctVlanClassifyStatus=_CtVlanClassifyStatus_Object((1,3,6,1,4,1,52,4,1,2,16,6,1,1),_CtVlanClassifyStatus_Type())
ctVlanClassifyStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:ctVlanClassifyStatus.setStatus(_A)
_CtVlanClassifyMaxEntries_Type=Unsigned32
_CtVlanClassifyMaxEntries_Object=MibScalar
ctVlanClassifyMaxEntries=_CtVlanClassifyMaxEntries_Object((1,3,6,1,4,1,52,4,1,2,16,6,1,2),_CtVlanClassifyMaxEntries_Type())
ctVlanClassifyMaxEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:ctVlanClassifyMaxEntries.setStatus(_A)
_CtVlanClassifyNumEntries_Type=Unsigned32
_CtVlanClassifyNumEntries_Object=MibScalar
ctVlanClassifyNumEntries=_CtVlanClassifyNumEntries_Object((1,3,6,1,4,1,52,4,1,2,16,6,1,3),_CtVlanClassifyNumEntries_Type())
ctVlanClassifyNumEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:ctVlanClassifyNumEntries.setStatus(_A)
_CtVlanClassifyTable_Object=MibTable
ctVlanClassifyTable=_CtVlanClassifyTable_Object((1,3,6,1,4,1,52,4,1,2,16,6,1,4))
if mibBuilder.loadTexts:ctVlanClassifyTable.setStatus(_A)
_CtVlanClassifyEntry_Object=MibTableRow
ctVlanClassifyEntry=_CtVlanClassifyEntry_Object((1,3,6,1,4,1,52,4,1,2,16,6,1,4,1))
ctVlanClassifyEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:ctVlanClassifyEntry.setStatus(_A)
_CtVlanClassifyVlanIndex_Type=VlanIndex
_CtVlanClassifyVlanIndex_Object=MibTableColumn
ctVlanClassifyVlanIndex=_CtVlanClassifyVlanIndex_Object((1,3,6,1,4,1,52,4,1,2,16,6,1,4,1,1),_CtVlanClassifyVlanIndex_Type())
ctVlanClassifyVlanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ctVlanClassifyVlanIndex.setStatus(_A)
_CtVlanClassifyDataMeaning_Type=CtVlanClassifyType
_CtVlanClassifyDataMeaning_Object=MibTableColumn
ctVlanClassifyDataMeaning=_CtVlanClassifyDataMeaning_Object((1,3,6,1,4,1,52,4,1,2,16,6,1,4,1,2),_CtVlanClassifyDataMeaning_Type())
ctVlanClassifyDataMeaning.setMaxAccess(_D)
if mibBuilder.loadTexts:ctVlanClassifyDataMeaning.setStatus(_A)
_CtVlanClassifyDataVal_Type=Unsigned32
_CtVlanClassifyDataVal_Object=MibTableColumn
ctVlanClassifyDataVal=_CtVlanClassifyDataVal_Object((1,3,6,1,4,1,52,4,1,2,16,6,1,4,1,3),_CtVlanClassifyDataVal_Type())
ctVlanClassifyDataVal.setMaxAccess(_D)
if mibBuilder.loadTexts:ctVlanClassifyDataVal.setStatus(_A)
_CtVlanClassifyDataMask_Type=Unsigned32
_CtVlanClassifyDataMask_Object=MibTableColumn
ctVlanClassifyDataMask=_CtVlanClassifyDataMask_Object((1,3,6,1,4,1,52,4,1,2,16,6,1,4,1,4),_CtVlanClassifyDataMask_Type())
ctVlanClassifyDataMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ctVlanClassifyDataMask.setStatus(_A)
class _CtVlanClassifyIngressList_Type(PortList):defaultHexValue='0000'
_CtVlanClassifyIngressList_Type.__name__=_F
_CtVlanClassifyIngressList_Object=MibTableColumn
ctVlanClassifyIngressList=_CtVlanClassifyIngressList_Object((1,3,6,1,4,1,52,4,1,2,16,6,1,4,1,5),_CtVlanClassifyIngressList_Type())
ctVlanClassifyIngressList.setMaxAccess(_K)
if mibBuilder.loadTexts:ctVlanClassifyIngressList.setStatus(_A)
_CtVlanClassifyRowStatus_Type=RowStatus
_CtVlanClassifyRowStatus_Object=MibTableColumn
ctVlanClassifyRowStatus=_CtVlanClassifyRowStatus_Object((1,3,6,1,4,1,52,4,1,2,16,6,1,4,1,6),_CtVlanClassifyRowStatus_Type())
ctVlanClassifyRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:ctVlanClassifyRowStatus.setStatus(_A)
_CtVlanClassifyRowInfo_Type=DisplayString
_CtVlanClassifyRowInfo_Object=MibTableColumn
ctVlanClassifyRowInfo=_CtVlanClassifyRowInfo_Object((1,3,6,1,4,1,52,4,1,2,16,6,1,4,1,7),_CtVlanClassifyRowInfo_Type())
ctVlanClassifyRowInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:ctVlanClassifyRowInfo.setStatus(_A)
_CtVlanClassifyAbilityTable_Object=MibTable
ctVlanClassifyAbilityTable=_CtVlanClassifyAbilityTable_Object((1,3,6,1,4,1,52,4,1,2,16,6,1,5))
if mibBuilder.loadTexts:ctVlanClassifyAbilityTable.setStatus(_A)
_CtVlanClassifyAbilityEntry_Object=MibTableRow
ctVlanClassifyAbilityEntry=_CtVlanClassifyAbilityEntry_Object((1,3,6,1,4,1,52,4,1,2,16,6,1,5,1))
ctVlanClassifyAbilityEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:ctVlanClassifyAbilityEntry.setStatus(_A)
_CtVlanClassifyAbility_Type=CtVlanClassifyType
_CtVlanClassifyAbility_Object=MibTableColumn
ctVlanClassifyAbility=_CtVlanClassifyAbility_Object((1,3,6,1,4,1,52,4,1,2,16,6,1,5,1,1),_CtVlanClassifyAbility_Type())
ctVlanClassifyAbility.setMaxAccess(_D)
if mibBuilder.loadTexts:ctVlanClassifyAbility.setStatus(_A)
_CtVlanClassifyPorts_Type=PortList
_CtVlanClassifyPorts_Object=MibTableColumn
ctVlanClassifyPorts=_CtVlanClassifyPorts_Object((1,3,6,1,4,1,52,4,1,2,16,6,1,5,1,2),_CtVlanClassifyPorts_Type())
ctVlanClassifyPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:ctVlanClassifyPorts.setStatus(_A)
class _CtVlanClassifyActionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forwardNoFrames',1),('forwardAllFrames',2)))
_CtVlanClassifyActionStatus_Type.__name__=_E
_CtVlanClassifyActionStatus_Object=MibTableColumn
ctVlanClassifyActionStatus=_CtVlanClassifyActionStatus_Object((1,3,6,1,4,1,52,4,1,2,16,6,1,5,1,3),_CtVlanClassifyActionStatus_Type())
ctVlanClassifyActionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctVlanClassifyActionStatus.setStatus(_A)
_CtVlanClassifyConformance_ObjectIdentity=ObjectIdentity
ctVlanClassifyConformance=_CtVlanClassifyConformance_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,16,6,2))
_CtVlanClassifyGroups_ObjectIdentity=ObjectIdentity
ctVlanClassifyGroups=_CtVlanClassifyGroups_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,16,6,2,1))
_CtVlanClassifyCompliances_ObjectIdentity=ObjectIdentity
ctVlanClassifyCompliances=_CtVlanClassifyCompliances_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,16,6,2,2))
ctVlanClassifyBaseGroup=ObjectGroup((1,3,6,1,4,1,52,4,1,2,16,6,2,1,1))
ctVlanClassifyBaseGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ctVlanClassifyBaseGroup.setStatus(_A)
ctVlanClassifyCompliance=ModuleCompliance((1,3,6,1,4,1,52,4,1,2,16,6,2,2,1))
ctVlanClassifyCompliance.setObjects((_B,_U))
if mibBuilder.loadTexts:ctVlanClassifyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CtVlanClassifyType':CtVlanClassifyType,'VlanIndex':VlanIndex,'ctVlanClassify':ctVlanClassify,'ctVlanClassifyObjects':ctVlanClassifyObjects,_M:ctVlanClassifyStatus,_N:ctVlanClassifyMaxEntries,_O:ctVlanClassifyNumEntries,'ctVlanClassifyTable':ctVlanClassifyTable,'ctVlanClassifyEntry':ctVlanClassifyEntry,_G:ctVlanClassifyVlanIndex,_H:ctVlanClassifyDataMeaning,_I:ctVlanClassifyDataVal,_J:ctVlanClassifyDataMask,_P:ctVlanClassifyIngressList,_Q:ctVlanClassifyRowStatus,_R:ctVlanClassifyRowInfo,'ctVlanClassifyAbilityTable':ctVlanClassifyAbilityTable,'ctVlanClassifyAbilityEntry':ctVlanClassifyAbilityEntry,_L:ctVlanClassifyAbility,_S:ctVlanClassifyPorts,_T:ctVlanClassifyActionStatus,'ctVlanClassifyConformance':ctVlanClassifyConformance,'ctVlanClassifyGroups':ctVlanClassifyGroups,_U:ctVlanClassifyBaseGroup,'ctVlanClassifyCompliances':ctVlanClassifyCompliances,'ctVlanClassifyCompliance':ctVlanClassifyCompliance})