_V='h3cSubnetVlanPortCreateGroup'
_U='h3cSubnetVlanSubnetGroup'
_T='h3cSubnetVlanScalarObjectGroup'
_S='h3cSubnetVlanPortRowStatus'
_R='h3cSubnetVlanPortInfoVlanId'
_Q='h3cSubnetVlanRowStatus'
_P='h3cSubnetVlanNetMaskValue'
_O='h3cSubnetVlanIpAddressValue'
_N='h3cSubnetVlanVlanIpAddressType'
_M='h3cSubnetNumPerPort'
_L='h3cSubnetNumAllPort'
_K='h3cSubnetNumPerVlan'
_J='h3cSubnetNumAllVlan'
_I='h3cSubnetVlanPortCreateVlanId'
_H='h3cSubnetVlanPortCreateIndex'
_G='h3cSubnetVlanSubnetIndex'
_F='h3cSubnetVlanVlanId'
_E='not-accessible'
_D='read-create'
_C='read-only'
_B='A3COM-HUAWEI-SUBNET-VLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cSubnetVlan=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,61))
if mibBuilder.loadTexts:h3cSubnetVlan.setRevisions(('2005-08-02 13:53',))
_H3cSubnetVlanObjects_ObjectIdentity=ObjectIdentity
h3cSubnetVlanObjects=_H3cSubnetVlanObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,61,1))
_H3cSubnetVlanScalarObjects_ObjectIdentity=ObjectIdentity
h3cSubnetVlanScalarObjects=_H3cSubnetVlanScalarObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,61,1,1))
_H3cSubnetNumAllVlan_Type=Integer32
_H3cSubnetNumAllVlan_Object=MibScalar
h3cSubnetNumAllVlan=_H3cSubnetNumAllVlan_Object((1,3,6,1,4,1,43,45,1,10,2,61,1,1,1),_H3cSubnetNumAllVlan_Type())
h3cSubnetNumAllVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSubnetNumAllVlan.setStatus(_A)
_H3cSubnetNumPerVlan_Type=Integer32
_H3cSubnetNumPerVlan_Object=MibScalar
h3cSubnetNumPerVlan=_H3cSubnetNumPerVlan_Object((1,3,6,1,4,1,43,45,1,10,2,61,1,1,2),_H3cSubnetNumPerVlan_Type())
h3cSubnetNumPerVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSubnetNumPerVlan.setStatus(_A)
_H3cSubnetNumAllPort_Type=Integer32
_H3cSubnetNumAllPort_Object=MibScalar
h3cSubnetNumAllPort=_H3cSubnetNumAllPort_Object((1,3,6,1,4,1,43,45,1,10,2,61,1,1,3),_H3cSubnetNumAllPort_Type())
h3cSubnetNumAllPort.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSubnetNumAllPort.setStatus(_A)
_H3cSubnetNumPerPort_Type=Integer32
_H3cSubnetNumPerPort_Object=MibScalar
h3cSubnetNumPerPort=_H3cSubnetNumPerPort_Object((1,3,6,1,4,1,43,45,1,10,2,61,1,1,4),_H3cSubnetNumPerPort_Type())
h3cSubnetNumPerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSubnetNumPerPort.setStatus(_A)
_H3cSubnetVlanTable_Object=MibTable
h3cSubnetVlanTable=_H3cSubnetVlanTable_Object((1,3,6,1,4,1,43,45,1,10,2,61,1,2))
if mibBuilder.loadTexts:h3cSubnetVlanTable.setStatus(_A)
_H3cSubnetVlanEntry_Object=MibTableRow
h3cSubnetVlanEntry=_H3cSubnetVlanEntry_Object((1,3,6,1,4,1,43,45,1,10,2,61,1,2,1))
h3cSubnetVlanEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:h3cSubnetVlanEntry.setStatus(_A)
_H3cSubnetVlanVlanId_Type=Integer32
_H3cSubnetVlanVlanId_Object=MibTableColumn
h3cSubnetVlanVlanId=_H3cSubnetVlanVlanId_Object((1,3,6,1,4,1,43,45,1,10,2,61,1,2,1,1),_H3cSubnetVlanVlanId_Type())
h3cSubnetVlanVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSubnetVlanVlanId.setStatus(_A)
_H3cSubnetVlanSubnetIndex_Type=Integer32
_H3cSubnetVlanSubnetIndex_Object=MibTableColumn
h3cSubnetVlanSubnetIndex=_H3cSubnetVlanSubnetIndex_Object((1,3,6,1,4,1,43,45,1,10,2,61,1,2,1,2),_H3cSubnetVlanSubnetIndex_Type())
h3cSubnetVlanSubnetIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSubnetVlanSubnetIndex.setStatus(_A)
_H3cSubnetVlanVlanIpAddressType_Type=InetAddressType
_H3cSubnetVlanVlanIpAddressType_Object=MibTableColumn
h3cSubnetVlanVlanIpAddressType=_H3cSubnetVlanVlanIpAddressType_Object((1,3,6,1,4,1,43,45,1,10,2,61,1,2,1,3),_H3cSubnetVlanVlanIpAddressType_Type())
h3cSubnetVlanVlanIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSubnetVlanVlanIpAddressType.setStatus(_A)
_H3cSubnetVlanIpAddressValue_Type=InetAddress
_H3cSubnetVlanIpAddressValue_Object=MibTableColumn
h3cSubnetVlanIpAddressValue=_H3cSubnetVlanIpAddressValue_Object((1,3,6,1,4,1,43,45,1,10,2,61,1,2,1,4),_H3cSubnetVlanIpAddressValue_Type())
h3cSubnetVlanIpAddressValue.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSubnetVlanIpAddressValue.setStatus(_A)
_H3cSubnetVlanNetMaskValue_Type=InetAddress
_H3cSubnetVlanNetMaskValue_Object=MibTableColumn
h3cSubnetVlanNetMaskValue=_H3cSubnetVlanNetMaskValue_Object((1,3,6,1,4,1,43,45,1,10,2,61,1,2,1,5),_H3cSubnetVlanNetMaskValue_Type())
h3cSubnetVlanNetMaskValue.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSubnetVlanNetMaskValue.setStatus(_A)
_H3cSubnetVlanRowStatus_Type=RowStatus
_H3cSubnetVlanRowStatus_Object=MibTableColumn
h3cSubnetVlanRowStatus=_H3cSubnetVlanRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,61,1,2,1,6),_H3cSubnetVlanRowStatus_Type())
h3cSubnetVlanRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSubnetVlanRowStatus.setStatus(_A)
_H3cSubnetVlanPortCreateTable_Object=MibTable
h3cSubnetVlanPortCreateTable=_H3cSubnetVlanPortCreateTable_Object((1,3,6,1,4,1,43,45,1,10,2,61,1,3))
if mibBuilder.loadTexts:h3cSubnetVlanPortCreateTable.setStatus(_A)
_H3cSubnetVlanPortCreateEntry_Object=MibTableRow
h3cSubnetVlanPortCreateEntry=_H3cSubnetVlanPortCreateEntry_Object((1,3,6,1,4,1,43,45,1,10,2,61,1,3,1))
h3cSubnetVlanPortCreateEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:h3cSubnetVlanPortCreateEntry.setStatus(_A)
_H3cSubnetVlanPortCreateIndex_Type=Integer32
_H3cSubnetVlanPortCreateIndex_Object=MibTableColumn
h3cSubnetVlanPortCreateIndex=_H3cSubnetVlanPortCreateIndex_Object((1,3,6,1,4,1,43,45,1,10,2,61,1,3,1,1),_H3cSubnetVlanPortCreateIndex_Type())
h3cSubnetVlanPortCreateIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSubnetVlanPortCreateIndex.setStatus(_A)
_H3cSubnetVlanPortCreateVlanId_Type=Integer32
_H3cSubnetVlanPortCreateVlanId_Object=MibTableColumn
h3cSubnetVlanPortCreateVlanId=_H3cSubnetVlanPortCreateVlanId_Object((1,3,6,1,4,1,43,45,1,10,2,61,1,3,1,2),_H3cSubnetVlanPortCreateVlanId_Type())
h3cSubnetVlanPortCreateVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cSubnetVlanPortCreateVlanId.setStatus(_A)
_H3cSubnetVlanPortInfoVlanId_Type=Integer32
_H3cSubnetVlanPortInfoVlanId_Object=MibTableColumn
h3cSubnetVlanPortInfoVlanId=_H3cSubnetVlanPortInfoVlanId_Object((1,3,6,1,4,1,43,45,1,10,2,61,1,3,1,3),_H3cSubnetVlanPortInfoVlanId_Type())
h3cSubnetVlanPortInfoVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSubnetVlanPortInfoVlanId.setStatus(_A)
_H3cSubnetVlanPortRowStatus_Type=RowStatus
_H3cSubnetVlanPortRowStatus_Object=MibTableColumn
h3cSubnetVlanPortRowStatus=_H3cSubnetVlanPortRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,61,1,3,1,4),_H3cSubnetVlanPortRowStatus_Type())
h3cSubnetVlanPortRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cSubnetVlanPortRowStatus.setStatus(_A)
_H3cSubnetVlanConformance_ObjectIdentity=ObjectIdentity
h3cSubnetVlanConformance=_H3cSubnetVlanConformance_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,61,2))
_H3cSubnetVlanCompliances_ObjectIdentity=ObjectIdentity
h3cSubnetVlanCompliances=_H3cSubnetVlanCompliances_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,61,2,1))
_H3cSubnetVlanGroups_ObjectIdentity=ObjectIdentity
h3cSubnetVlanGroups=_H3cSubnetVlanGroups_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,61,2,2))
h3cSubnetVlanScalarObjectGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,10,2,61,2,2,1))
h3cSubnetVlanScalarObjectGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:h3cSubnetVlanScalarObjectGroup.setStatus(_A)
h3cSubnetVlanSubnetGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,10,2,61,2,2,2))
h3cSubnetVlanSubnetGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:h3cSubnetVlanSubnetGroup.setStatus(_A)
h3cSubnetVlanPortCreateGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,10,2,61,2,2,3))
h3cSubnetVlanPortCreateGroup.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:h3cSubnetVlanPortCreateGroup.setStatus(_A)
h3cSubnetVlanCompliance=ModuleCompliance((1,3,6,1,4,1,43,45,1,10,2,61,2,1,1))
h3cSubnetVlanCompliance.setObjects(*((_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:h3cSubnetVlanCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cSubnetVlan':h3cSubnetVlan,'h3cSubnetVlanObjects':h3cSubnetVlanObjects,'h3cSubnetVlanScalarObjects':h3cSubnetVlanScalarObjects,_J:h3cSubnetNumAllVlan,_K:h3cSubnetNumPerVlan,_L:h3cSubnetNumAllPort,_M:h3cSubnetNumPerPort,'h3cSubnetVlanTable':h3cSubnetVlanTable,'h3cSubnetVlanEntry':h3cSubnetVlanEntry,_F:h3cSubnetVlanVlanId,_G:h3cSubnetVlanSubnetIndex,_N:h3cSubnetVlanVlanIpAddressType,_O:h3cSubnetVlanIpAddressValue,_P:h3cSubnetVlanNetMaskValue,_Q:h3cSubnetVlanRowStatus,'h3cSubnetVlanPortCreateTable':h3cSubnetVlanPortCreateTable,'h3cSubnetVlanPortCreateEntry':h3cSubnetVlanPortCreateEntry,_H:h3cSubnetVlanPortCreateIndex,_I:h3cSubnetVlanPortCreateVlanId,_R:h3cSubnetVlanPortInfoVlanId,_S:h3cSubnetVlanPortRowStatus,'h3cSubnetVlanConformance':h3cSubnetVlanConformance,'h3cSubnetVlanCompliances':h3cSubnetVlanCompliances,'h3cSubnetVlanCompliance':h3cSubnetVlanCompliance,'h3cSubnetVlanGroups':h3cSubnetVlanGroups,_T:h3cSubnetVlanScalarObjectGroup,_U:h3cSubnetVlanSubnetGroup,_V:h3cSubnetVlanPortCreateGroup})