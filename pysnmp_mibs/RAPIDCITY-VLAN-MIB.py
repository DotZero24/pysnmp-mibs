_J='rcVlanId'
_I='RAPIDCITY-VLAN-MIB'
_H='none'
_G='TruthValue'
_F='DisplayString'
_E='read-only'
_D='OctetString'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
DisplayString,MacAddress,RowStatus,TruthValue=mibBuilder.importSymbols('SNMPv2-TC-v1',_F,'MacAddress','RowStatus',_G)
_Rapidcity_ObjectIdentity=ObjectIdentity
rapidcity=_Rapidcity_ObjectIdentity((1,3,6,1,4,1,2272))
_Rapidcityfoo_ObjectIdentity=ObjectIdentity
rapidcityfoo=_Rapidcityfoo_ObjectIdentity((1,3,6,1,4,1,2272,1))
_RcVlan_ObjectIdentity=ObjectIdentity
rcVlan=_RcVlan_ObjectIdentity((1,3,6,1,4,1,2272,1,3))
class _RcVlanNumVlans_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_RcVlanNumVlans_Type.__name__=_C
_RcVlanNumVlans_Object=MibScalar
rcVlanNumVlans=_RcVlanNumVlans_Object((1,3,6,1,4,1,2272,1,3,1),_RcVlanNumVlans_Type())
rcVlanNumVlans.setMaxAccess(_E)
if mibBuilder.loadTexts:rcVlanNumVlans.setStatus(_A)
_RcVlanTable_Object=MibTable
rcVlanTable=_RcVlanTable_Object((1,3,6,1,4,1,2272,1,3,2))
if mibBuilder.loadTexts:rcVlanTable.setStatus(_A)
_RcVlanEntry_Object=MibTableRow
rcVlanEntry=_RcVlanEntry_Object((1,3,6,1,4,1,2272,1,3,2,1))
rcVlanEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:rcVlanEntry.setStatus(_A)
class _RcVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_RcVlanId_Type.__name__=_C
_RcVlanId_Object=MibTableColumn
rcVlanId=_RcVlanId_Object((1,3,6,1,4,1,2272,1,3,2,1,1),_RcVlanId_Type())
rcVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:rcVlanId.setStatus(_A)
class _RcVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RcVlanName_Type.__name__=_F
_RcVlanName_Object=MibTableColumn
rcVlanName=_RcVlanName_Object((1,3,6,1,4,1,2272,1,3,2,1,2),_RcVlanName_Type())
rcVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:rcVlanName.setStatus(_A)
class _RcVlanColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_RcVlanColor_Type.__name__=_C
_RcVlanColor_Object=MibTableColumn
rcVlanColor=_RcVlanColor_Object((1,3,6,1,4,1,2272,1,3,2,1,3),_RcVlanColor_Type())
rcVlanColor.setMaxAccess(_B)
if mibBuilder.loadTexts:rcVlanColor.setStatus(_A)
class _RcVlanHighPriority_Type(TruthValue):defaultValue=2
_RcVlanHighPriority_Type.__name__=_G
_RcVlanHighPriority_Object=MibTableColumn
rcVlanHighPriority=_RcVlanHighPriority_Object((1,3,6,1,4,1,2272,1,3,2,1,4),_RcVlanHighPriority_Type())
rcVlanHighPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:rcVlanHighPriority.setStatus(_A)
class _RcVlanRoutingEnable_Type(TruthValue):defaultValue=2
_RcVlanRoutingEnable_Type.__name__=_G
_RcVlanRoutingEnable_Object=MibTableColumn
rcVlanRoutingEnable=_RcVlanRoutingEnable_Object((1,3,6,1,4,1,2272,1,3,2,1,5),_RcVlanRoutingEnable_Type())
rcVlanRoutingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcVlanRoutingEnable.setStatus(_A)
_RcVlanIfIndex_Type=InterfaceIndex
_RcVlanIfIndex_Object=MibTableColumn
rcVlanIfIndex=_RcVlanIfIndex_Object((1,3,6,1,4,1,2272,1,3,2,1,6),_RcVlanIfIndex_Type())
rcVlanIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rcVlanIfIndex.setStatus(_A)
class _RcVlanAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),('flushMacFdb',2),('flushArp',3),('flushIp',4),('flushDynMemb',5),('all',6)))
_RcVlanAction_Type.__name__=_C
_RcVlanAction_Object=MibTableColumn
rcVlanAction=_RcVlanAction_Object((1,3,6,1,4,1,2272,1,3,2,1,7),_RcVlanAction_Type())
rcVlanAction.setMaxAccess(_B)
if mibBuilder.loadTexts:rcVlanAction.setStatus(_A)
class _RcVlanResult_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('inProgress',2),('success',3),('fail',4)))
_RcVlanResult_Type.__name__=_C
_RcVlanResult_Object=MibTableColumn
rcVlanResult=_RcVlanResult_Object((1,3,6,1,4,1,2272,1,3,2,1,8),_RcVlanResult_Type())
rcVlanResult.setMaxAccess(_E)
if mibBuilder.loadTexts:rcVlanResult.setStatus(_A)
class _RcVlanStgId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_RcVlanStgId_Type.__name__=_C
_RcVlanStgId_Object=MibTableColumn
rcVlanStgId=_RcVlanStgId_Object((1,3,6,1,4,1,2272,1,3,2,1,9),_RcVlanStgId_Type())
rcVlanStgId.setMaxAccess(_B)
if mibBuilder.loadTexts:rcVlanStgId.setStatus(_A)
class _RcVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('byPort',1),('byIpSubnet',2),('byProtocolId',3),('bySrcMac',4),('byDstMcast',5)))
_RcVlanType_Type.__name__=_C
_RcVlanType_Object=MibTableColumn
rcVlanType=_RcVlanType_Object((1,3,6,1,4,1,2272,1,3,2,1,10),_RcVlanType_Type())
rcVlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcVlanType.setStatus(_A)
class _RcVlanPortMembers_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_RcVlanPortMembers_Type.__name__=_D
_RcVlanPortMembers_Object=MibTableColumn
rcVlanPortMembers=_RcVlanPortMembers_Object((1,3,6,1,4,1,2272,1,3,2,1,11),_RcVlanPortMembers_Type())
rcVlanPortMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:rcVlanPortMembers.setStatus(_A)
class _RcVlanPotentialMembers_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_RcVlanPotentialMembers_Type.__name__=_D
_RcVlanPotentialMembers_Object=MibTableColumn
rcVlanPotentialMembers=_RcVlanPotentialMembers_Object((1,3,6,1,4,1,2272,1,3,2,1,12),_RcVlanPotentialMembers_Type())
rcVlanPotentialMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:rcVlanPotentialMembers.setStatus(_A)
class _RcVlanStaticMembers_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_RcVlanStaticMembers_Type.__name__=_D
_RcVlanStaticMembers_Object=MibTableColumn
rcVlanStaticMembers=_RcVlanStaticMembers_Object((1,3,6,1,4,1,2272,1,3,2,1,13),_RcVlanStaticMembers_Type())
rcVlanStaticMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:rcVlanStaticMembers.setStatus(_A)
class _RcVlanNotAllowToJoin_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_RcVlanNotAllowToJoin_Type.__name__=_D
_RcVlanNotAllowToJoin_Object=MibTableColumn
rcVlanNotAllowToJoin=_RcVlanNotAllowToJoin_Object((1,3,6,1,4,1,2272,1,3,2,1,14),_RcVlanNotAllowToJoin_Type())
rcVlanNotAllowToJoin.setMaxAccess(_B)
if mibBuilder.loadTexts:rcVlanNotAllowToJoin.setStatus(_A)
class _RcVlanProtocolId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_H,0),('ip',1),('ipx802dot3',2),('ipx802dot2',3),('ipxSnap',4),('ipxEthernet2',5),('appleTalk',6),('decLat',7),('decOther',8),('sna802dot2',9),('snaEthernet2',10),('netBios',11),('xns',12)))
_RcVlanProtocolId_Type.__name__=_C
_RcVlanProtocolId_Object=MibTableColumn
rcVlanProtocolId=_RcVlanProtocolId_Object((1,3,6,1,4,1,2272,1,3,2,1,15),_RcVlanProtocolId_Type())
rcVlanProtocolId.setMaxAccess(_B)
if mibBuilder.loadTexts:rcVlanProtocolId.setStatus(_A)
_RcVlanSubnetAddr_Type=IpAddress
_RcVlanSubnetAddr_Object=MibTableColumn
rcVlanSubnetAddr=_RcVlanSubnetAddr_Object((1,3,6,1,4,1,2272,1,3,2,1,16),_RcVlanSubnetAddr_Type())
rcVlanSubnetAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rcVlanSubnetAddr.setStatus(_A)
_RcVlanSubnetMask_Type=IpAddress
_RcVlanSubnetMask_Object=MibTableColumn
rcVlanSubnetMask=_RcVlanSubnetMask_Object((1,3,6,1,4,1,2272,1,3,2,1,17),_RcVlanSubnetMask_Type())
rcVlanSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rcVlanSubnetMask.setStatus(_A)
class _RcVlanAgingTime_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000000))
_RcVlanAgingTime_Type.__name__=_C
_RcVlanAgingTime_Object=MibTableColumn
rcVlanAgingTime=_RcVlanAgingTime_Object((1,3,6,1,4,1,2272,1,3,2,1,18),_RcVlanAgingTime_Type())
rcVlanAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcVlanAgingTime.setStatus(_A)
_RcVlanMacAddress_Type=MacAddress
_RcVlanMacAddress_Object=MibTableColumn
rcVlanMacAddress=_RcVlanMacAddress_Object((1,3,6,1,4,1,2272,1,3,2,1,19),_RcVlanMacAddress_Type())
rcVlanMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:rcVlanMacAddress.setStatus(_A)
_RcVlanRowStatus_Type=RowStatus
_RcVlanRowStatus_Object=MibTableColumn
rcVlanRowStatus=_RcVlanRowStatus_Object((1,3,6,1,4,1,2272,1,3,2,1,20),_RcVlanRowStatus_Type())
rcVlanRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcVlanRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'rapidcity':rapidcity,'rapidcityfoo':rapidcityfoo,'rcVlan':rcVlan,'rcVlanNumVlans':rcVlanNumVlans,'rcVlanTable':rcVlanTable,'rcVlanEntry':rcVlanEntry,_J:rcVlanId,'rcVlanName':rcVlanName,'rcVlanColor':rcVlanColor,'rcVlanHighPriority':rcVlanHighPriority,'rcVlanRoutingEnable':rcVlanRoutingEnable,'rcVlanIfIndex':rcVlanIfIndex,'rcVlanAction':rcVlanAction,'rcVlanResult':rcVlanResult,'rcVlanStgId':rcVlanStgId,'rcVlanType':rcVlanType,'rcVlanPortMembers':rcVlanPortMembers,'rcVlanPotentialMembers':rcVlanPotentialMembers,'rcVlanStaticMembers':rcVlanStaticMembers,'rcVlanNotAllowToJoin':rcVlanNotAllowToJoin,'rcVlanProtocolId':rcVlanProtocolId,'rcVlanSubnetAddr':rcVlanSubnetAddr,'rcVlanSubnetMask':rcVlanSubnetMask,'rcVlanAgingTime':rcVlanAgingTime,'rcVlanMacAddress':rcVlanMacAddress,'rcVlanRowStatus':rcVlanRowStatus})