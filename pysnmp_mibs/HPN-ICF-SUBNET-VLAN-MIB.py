_W='hpnicfSubnetVlanPortCreateGroup'
_V='hpnicfSubnetVlanSubnetGroup'
_U='hpnicfSubnetVlanScalarObjectGroup'
_T='hpnicfSubnetVlanPortRowStatus'
_S='hpnicfSubnetVlanPortInfoVlanId'
_R='hpnicfSubnetVlanRowStatus'
_Q='hpnicfSubnetVlanNetMaskValue'
_P='hpnicfSubnetVlanIpAddressValue'
_O='hpnicfSubnetVlanVlanIpAddressType'
_N='hpnicfSubnetNumPerPort'
_M='hpnicfSubnetNumAllPort'
_L='hpnicfSubnetNumPerVlan'
_K='hpnicfSubnetNumAllVlan'
_J='hpnicfSubnetVlanPortCreateVlanId'
_I='hpnicfSubnetVlanPortCreateIndex'
_H='hpnicfSubnetVlanSubnetIndex'
_G='hpnicfSubnetVlanVlanId'
_F='Integer32'
_E='not-accessible'
_D='read-create'
_C='read-only'
_B='HPN-ICF-SUBNET-VLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfSubnetVlan=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,61))
if mibBuilder.loadTexts:hpnicfSubnetVlan.setRevisions(('2005-08-02 13:53',))
_HpnicfSubnetVlanObjects_ObjectIdentity=ObjectIdentity
hpnicfSubnetVlanObjects=_HpnicfSubnetVlanObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,61,1))
_HpnicfSubnetVlanScalarObjects_ObjectIdentity=ObjectIdentity
hpnicfSubnetVlanScalarObjects=_HpnicfSubnetVlanScalarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,61,1,1))
_HpnicfSubnetNumAllVlan_Type=Integer32
_HpnicfSubnetNumAllVlan_Object=MibScalar
hpnicfSubnetNumAllVlan=_HpnicfSubnetNumAllVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,61,1,1,1),_HpnicfSubnetNumAllVlan_Type())
hpnicfSubnetNumAllVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSubnetNumAllVlan.setStatus(_A)
_HpnicfSubnetNumPerVlan_Type=Integer32
_HpnicfSubnetNumPerVlan_Object=MibScalar
hpnicfSubnetNumPerVlan=_HpnicfSubnetNumPerVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,61,1,1,2),_HpnicfSubnetNumPerVlan_Type())
hpnicfSubnetNumPerVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSubnetNumPerVlan.setStatus(_A)
_HpnicfSubnetNumAllPort_Type=Integer32
_HpnicfSubnetNumAllPort_Object=MibScalar
hpnicfSubnetNumAllPort=_HpnicfSubnetNumAllPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,61,1,1,3),_HpnicfSubnetNumAllPort_Type())
hpnicfSubnetNumAllPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSubnetNumAllPort.setStatus(_A)
_HpnicfSubnetNumPerPort_Type=Integer32
_HpnicfSubnetNumPerPort_Object=MibScalar
hpnicfSubnetNumPerPort=_HpnicfSubnetNumPerPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,61,1,1,4),_HpnicfSubnetNumPerPort_Type())
hpnicfSubnetNumPerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSubnetNumPerPort.setStatus(_A)
_HpnicfSubnetVlanTable_Object=MibTable
hpnicfSubnetVlanTable=_HpnicfSubnetVlanTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,61,1,2))
if mibBuilder.loadTexts:hpnicfSubnetVlanTable.setStatus(_A)
_HpnicfSubnetVlanEntry_Object=MibTableRow
hpnicfSubnetVlanEntry=_HpnicfSubnetVlanEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,61,1,2,1))
hpnicfSubnetVlanEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:hpnicfSubnetVlanEntry.setStatus(_A)
_HpnicfSubnetVlanVlanId_Type=Integer32
_HpnicfSubnetVlanVlanId_Object=MibTableColumn
hpnicfSubnetVlanVlanId=_HpnicfSubnetVlanVlanId_Object((1,3,6,1,4,1,11,2,14,11,15,2,61,1,2,1,1),_HpnicfSubnetVlanVlanId_Type())
hpnicfSubnetVlanVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSubnetVlanVlanId.setStatus(_A)
_HpnicfSubnetVlanSubnetIndex_Type=Integer32
_HpnicfSubnetVlanSubnetIndex_Object=MibTableColumn
hpnicfSubnetVlanSubnetIndex=_HpnicfSubnetVlanSubnetIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,61,1,2,1,2),_HpnicfSubnetVlanSubnetIndex_Type())
hpnicfSubnetVlanSubnetIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSubnetVlanSubnetIndex.setStatus(_A)
_HpnicfSubnetVlanVlanIpAddressType_Type=InetAddressType
_HpnicfSubnetVlanVlanIpAddressType_Object=MibTableColumn
hpnicfSubnetVlanVlanIpAddressType=_HpnicfSubnetVlanVlanIpAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,61,1,2,1,3),_HpnicfSubnetVlanVlanIpAddressType_Type())
hpnicfSubnetVlanVlanIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSubnetVlanVlanIpAddressType.setStatus(_A)
_HpnicfSubnetVlanIpAddressValue_Type=InetAddress
_HpnicfSubnetVlanIpAddressValue_Object=MibTableColumn
hpnicfSubnetVlanIpAddressValue=_HpnicfSubnetVlanIpAddressValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,61,1,2,1,4),_HpnicfSubnetVlanIpAddressValue_Type())
hpnicfSubnetVlanIpAddressValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSubnetVlanIpAddressValue.setStatus(_A)
_HpnicfSubnetVlanNetMaskValue_Type=InetAddress
_HpnicfSubnetVlanNetMaskValue_Object=MibTableColumn
hpnicfSubnetVlanNetMaskValue=_HpnicfSubnetVlanNetMaskValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,61,1,2,1,5),_HpnicfSubnetVlanNetMaskValue_Type())
hpnicfSubnetVlanNetMaskValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSubnetVlanNetMaskValue.setStatus(_A)
_HpnicfSubnetVlanRowStatus_Type=RowStatus
_HpnicfSubnetVlanRowStatus_Object=MibTableColumn
hpnicfSubnetVlanRowStatus=_HpnicfSubnetVlanRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,61,1,2,1,6),_HpnicfSubnetVlanRowStatus_Type())
hpnicfSubnetVlanRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSubnetVlanRowStatus.setStatus(_A)
_HpnicfSubnetVlanPortCreateTable_Object=MibTable
hpnicfSubnetVlanPortCreateTable=_HpnicfSubnetVlanPortCreateTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,61,1,3))
if mibBuilder.loadTexts:hpnicfSubnetVlanPortCreateTable.setStatus(_A)
_HpnicfSubnetVlanPortCreateEntry_Object=MibTableRow
hpnicfSubnetVlanPortCreateEntry=_HpnicfSubnetVlanPortCreateEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,61,1,3,1))
hpnicfSubnetVlanPortCreateEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:hpnicfSubnetVlanPortCreateEntry.setStatus(_A)
_HpnicfSubnetVlanPortCreateIndex_Type=Integer32
_HpnicfSubnetVlanPortCreateIndex_Object=MibTableColumn
hpnicfSubnetVlanPortCreateIndex=_HpnicfSubnetVlanPortCreateIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,61,1,3,1,1),_HpnicfSubnetVlanPortCreateIndex_Type())
hpnicfSubnetVlanPortCreateIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSubnetVlanPortCreateIndex.setStatus(_A)
_HpnicfSubnetVlanPortCreateVlanId_Type=Integer32
_HpnicfSubnetVlanPortCreateVlanId_Object=MibTableColumn
hpnicfSubnetVlanPortCreateVlanId=_HpnicfSubnetVlanPortCreateVlanId_Object((1,3,6,1,4,1,11,2,14,11,15,2,61,1,3,1,2),_HpnicfSubnetVlanPortCreateVlanId_Type())
hpnicfSubnetVlanPortCreateVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSubnetVlanPortCreateVlanId.setStatus(_A)
_HpnicfSubnetVlanPortInfoVlanId_Type=Integer32
_HpnicfSubnetVlanPortInfoVlanId_Object=MibTableColumn
hpnicfSubnetVlanPortInfoVlanId=_HpnicfSubnetVlanPortInfoVlanId_Object((1,3,6,1,4,1,11,2,14,11,15,2,61,1,3,1,3),_HpnicfSubnetVlanPortInfoVlanId_Type())
hpnicfSubnetVlanPortInfoVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSubnetVlanPortInfoVlanId.setStatus(_A)
_HpnicfSubnetVlanPortRowStatus_Type=RowStatus
_HpnicfSubnetVlanPortRowStatus_Object=MibTableColumn
hpnicfSubnetVlanPortRowStatus=_HpnicfSubnetVlanPortRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,61,1,3,1,4),_HpnicfSubnetVlanPortRowStatus_Type())
hpnicfSubnetVlanPortRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfSubnetVlanPortRowStatus.setStatus(_A)
class _HpnicfSubnetVlanPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_HpnicfSubnetVlanPortStatus_Type.__name__=_F
_HpnicfSubnetVlanPortStatus_Object=MibTableColumn
hpnicfSubnetVlanPortStatus=_HpnicfSubnetVlanPortStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,61,1,3,1,5),_HpnicfSubnetVlanPortStatus_Type())
hpnicfSubnetVlanPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSubnetVlanPortStatus.setStatus(_A)
_HpnicfSubnetVlanConformance_ObjectIdentity=ObjectIdentity
hpnicfSubnetVlanConformance=_HpnicfSubnetVlanConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,61,2))
_HpnicfSubnetVlanCompliances_ObjectIdentity=ObjectIdentity
hpnicfSubnetVlanCompliances=_HpnicfSubnetVlanCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,61,2,1))
_HpnicfSubnetVlanGroups_ObjectIdentity=ObjectIdentity
hpnicfSubnetVlanGroups=_HpnicfSubnetVlanGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,61,2,2))
hpnicfSubnetVlanScalarObjectGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,61,2,2,1))
hpnicfSubnetVlanScalarObjectGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:hpnicfSubnetVlanScalarObjectGroup.setStatus(_A)
hpnicfSubnetVlanSubnetGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,61,2,2,2))
hpnicfSubnetVlanSubnetGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:hpnicfSubnetVlanSubnetGroup.setStatus(_A)
hpnicfSubnetVlanPortCreateGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,61,2,2,3))
hpnicfSubnetVlanPortCreateGroup.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:hpnicfSubnetVlanPortCreateGroup.setStatus(_A)
hpnicfSubnetVlanCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,61,2,1,1))
hpnicfSubnetVlanCompliance.setObjects(*((_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:hpnicfSubnetVlanCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfSubnetVlan':hpnicfSubnetVlan,'hpnicfSubnetVlanObjects':hpnicfSubnetVlanObjects,'hpnicfSubnetVlanScalarObjects':hpnicfSubnetVlanScalarObjects,_K:hpnicfSubnetNumAllVlan,_L:hpnicfSubnetNumPerVlan,_M:hpnicfSubnetNumAllPort,_N:hpnicfSubnetNumPerPort,'hpnicfSubnetVlanTable':hpnicfSubnetVlanTable,'hpnicfSubnetVlanEntry':hpnicfSubnetVlanEntry,_G:hpnicfSubnetVlanVlanId,_H:hpnicfSubnetVlanSubnetIndex,_O:hpnicfSubnetVlanVlanIpAddressType,_P:hpnicfSubnetVlanIpAddressValue,_Q:hpnicfSubnetVlanNetMaskValue,_R:hpnicfSubnetVlanRowStatus,'hpnicfSubnetVlanPortCreateTable':hpnicfSubnetVlanPortCreateTable,'hpnicfSubnetVlanPortCreateEntry':hpnicfSubnetVlanPortCreateEntry,_I:hpnicfSubnetVlanPortCreateIndex,_J:hpnicfSubnetVlanPortCreateVlanId,_S:hpnicfSubnetVlanPortInfoVlanId,_T:hpnicfSubnetVlanPortRowStatus,'hpnicfSubnetVlanPortStatus':hpnicfSubnetVlanPortStatus,'hpnicfSubnetVlanConformance':hpnicfSubnetVlanConformance,'hpnicfSubnetVlanCompliances':hpnicfSubnetVlanCompliances,'hpnicfSubnetVlanCompliance':hpnicfSubnetVlanCompliance,'hpnicfSubnetVlanGroups':hpnicfSubnetVlanGroups,_U:hpnicfSubnetVlanScalarObjectGroup,_V:hpnicfSubnetVlanSubnetGroup,_W:hpnicfSubnetVlanPortCreateGroup})