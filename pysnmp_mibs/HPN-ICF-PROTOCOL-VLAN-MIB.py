_b='hpnicfProtocolVlanPortGroup'
_a='hpnicfProtocolVlanProtocolGroup'
_Z='hpnicfProtocolVlanOperateGroup'
_Y='hpnicfProtocolVlanPortRowStatus'
_X='hpnicfProtocolVlanPortTypeValue'
_W='hpnicfProtocolVlanPortProtocolSubType'
_V='hpnicfProtocolVlanPortProtocolType'
_U='hpnicfProtocolVlanRowStatus'
_T='hpnicfProtocolVlanProtocolTypeValue'
_S='hpnicfProtocolVlanProtocolSubType'
_R='hpnicfProtocolVlanProtocolType'
_Q='hpnicfDifferentProtocolNumAllPort'
_P='hpnicfProtocolNumPerPort'
_O='hpnicfProtocolNumAllPort'
_N='hpnicfProtocolNumPerVlan'
_M='hpnicfProtocolNumAllVlan'
_L='hpnicfProtocolVlanPortProtocolId'
_K='hpnicfProtocolVlanPortVlanId'
_J='hpnicfProtocolVlanPortIndex'
_I='hpnicfProtocolVlanProtocolIndex'
_H='hpnicfProtocolVlanVlanId'
_G='Integer32'
_F='OctetString'
_E='read-create'
_D='not-accessible'
_C='read-only'
_B='HPN-ICF-PROTOCOL-VLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfProtocolVlan=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,16))
if mibBuilder.loadTexts:hpnicfProtocolVlan.setRevisions(('2004-08-31 19:38',))
class HpnicfvProtocolVlanProtocolType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,101,102,103,201)));namedValues=NamedValues(*(('ip',1),('ipx',2),('at',3),('ipv6',4),('mode-llc',101),('mode-snap',102),('mode-ethernetii',103),('notConfigure',201)))
class HpnicfvProtocolVlanProtocolSubType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('notused',1),('ethernetii',2),('llc',3),('raw',4),('snap',5),('etype',6)))
_HpnicfProtocolVlanOperate_ObjectIdentity=ObjectIdentity
hpnicfProtocolVlanOperate=_HpnicfProtocolVlanOperate_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,16,1))
_HpnicfProtocolNumAllVlan_Type=Integer32
_HpnicfProtocolNumAllVlan_Object=MibScalar
hpnicfProtocolNumAllVlan=_HpnicfProtocolNumAllVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,1),_HpnicfProtocolNumAllVlan_Type())
hpnicfProtocolNumAllVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfProtocolNumAllVlan.setStatus(_A)
_HpnicfProtocolNumPerVlan_Type=Integer32
_HpnicfProtocolNumPerVlan_Object=MibScalar
hpnicfProtocolNumPerVlan=_HpnicfProtocolNumPerVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,2),_HpnicfProtocolNumPerVlan_Type())
hpnicfProtocolNumPerVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfProtocolNumPerVlan.setStatus(_A)
_HpnicfProtocolNumAllPort_Type=Integer32
_HpnicfProtocolNumAllPort_Object=MibScalar
hpnicfProtocolNumAllPort=_HpnicfProtocolNumAllPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,3),_HpnicfProtocolNumAllPort_Type())
hpnicfProtocolNumAllPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfProtocolNumAllPort.setStatus(_A)
_HpnicfProtocolNumPerPort_Type=Integer32
_HpnicfProtocolNumPerPort_Object=MibScalar
hpnicfProtocolNumPerPort=_HpnicfProtocolNumPerPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,4),_HpnicfProtocolNumPerPort_Type())
hpnicfProtocolNumPerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfProtocolNumPerPort.setStatus(_A)
_HpnicfProtocolVlanTable_Object=MibTable
hpnicfProtocolVlanTable=_HpnicfProtocolVlanTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,5))
if mibBuilder.loadTexts:hpnicfProtocolVlanTable.setStatus(_A)
_HpnicfProtocolVlanEntry_Object=MibTableRow
hpnicfProtocolVlanEntry=_HpnicfProtocolVlanEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,5,1))
hpnicfProtocolVlanEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:hpnicfProtocolVlanEntry.setStatus(_A)
_HpnicfProtocolVlanVlanId_Type=Integer32
_HpnicfProtocolVlanVlanId_Object=MibTableColumn
hpnicfProtocolVlanVlanId=_HpnicfProtocolVlanVlanId_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,5,1,1),_HpnicfProtocolVlanVlanId_Type())
hpnicfProtocolVlanVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfProtocolVlanVlanId.setStatus(_A)
_HpnicfProtocolVlanProtocolIndex_Type=Integer32
_HpnicfProtocolVlanProtocolIndex_Object=MibTableColumn
hpnicfProtocolVlanProtocolIndex=_HpnicfProtocolVlanProtocolIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,5,1,2),_HpnicfProtocolVlanProtocolIndex_Type())
hpnicfProtocolVlanProtocolIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfProtocolVlanProtocolIndex.setStatus(_A)
_HpnicfProtocolVlanProtocolType_Type=HpnicfvProtocolVlanProtocolType
_HpnicfProtocolVlanProtocolType_Object=MibTableColumn
hpnicfProtocolVlanProtocolType=_HpnicfProtocolVlanProtocolType_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,5,1,3),_HpnicfProtocolVlanProtocolType_Type())
hpnicfProtocolVlanProtocolType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfProtocolVlanProtocolType.setStatus(_A)
_HpnicfProtocolVlanProtocolSubType_Type=HpnicfvProtocolVlanProtocolSubType
_HpnicfProtocolVlanProtocolSubType_Object=MibTableColumn
hpnicfProtocolVlanProtocolSubType=_HpnicfProtocolVlanProtocolSubType_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,5,1,4),_HpnicfProtocolVlanProtocolSubType_Type())
hpnicfProtocolVlanProtocolSubType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfProtocolVlanProtocolSubType.setStatus(_A)
class _HpnicfProtocolVlanProtocolTypeValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfProtocolVlanProtocolTypeValue_Type.__name__=_F
_HpnicfProtocolVlanProtocolTypeValue_Object=MibTableColumn
hpnicfProtocolVlanProtocolTypeValue=_HpnicfProtocolVlanProtocolTypeValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,5,1,5),_HpnicfProtocolVlanProtocolTypeValue_Type())
hpnicfProtocolVlanProtocolTypeValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfProtocolVlanProtocolTypeValue.setStatus(_A)
_HpnicfProtocolVlanRowStatus_Type=RowStatus
_HpnicfProtocolVlanRowStatus_Object=MibTableColumn
hpnicfProtocolVlanRowStatus=_HpnicfProtocolVlanRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,5,1,6),_HpnicfProtocolVlanRowStatus_Type())
hpnicfProtocolVlanRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfProtocolVlanRowStatus.setStatus(_A)
_HpnicfProtocolVlanPortTable_Object=MibTable
hpnicfProtocolVlanPortTable=_HpnicfProtocolVlanPortTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,6))
if mibBuilder.loadTexts:hpnicfProtocolVlanPortTable.setStatus(_A)
_HpnicfProtocolVlanPortEntry_Object=MibTableRow
hpnicfProtocolVlanPortEntry=_HpnicfProtocolVlanPortEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,6,1))
hpnicfProtocolVlanPortEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:hpnicfProtocolVlanPortEntry.setStatus(_A)
_HpnicfProtocolVlanPortIndex_Type=Integer32
_HpnicfProtocolVlanPortIndex_Object=MibTableColumn
hpnicfProtocolVlanPortIndex=_HpnicfProtocolVlanPortIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,6,1,1),_HpnicfProtocolVlanPortIndex_Type())
hpnicfProtocolVlanPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfProtocolVlanPortIndex.setStatus(_A)
_HpnicfProtocolVlanPortVlanId_Type=Integer32
_HpnicfProtocolVlanPortVlanId_Object=MibTableColumn
hpnicfProtocolVlanPortVlanId=_HpnicfProtocolVlanPortVlanId_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,6,1,2),_HpnicfProtocolVlanPortVlanId_Type())
hpnicfProtocolVlanPortVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfProtocolVlanPortVlanId.setStatus(_A)
_HpnicfProtocolVlanPortProtocolId_Type=Integer32
_HpnicfProtocolVlanPortProtocolId_Object=MibTableColumn
hpnicfProtocolVlanPortProtocolId=_HpnicfProtocolVlanPortProtocolId_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,6,1,3),_HpnicfProtocolVlanPortProtocolId_Type())
hpnicfProtocolVlanPortProtocolId.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfProtocolVlanPortProtocolId.setStatus(_A)
_HpnicfProtocolVlanPortProtocolType_Type=HpnicfvProtocolVlanProtocolType
_HpnicfProtocolVlanPortProtocolType_Object=MibTableColumn
hpnicfProtocolVlanPortProtocolType=_HpnicfProtocolVlanPortProtocolType_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,6,1,4),_HpnicfProtocolVlanPortProtocolType_Type())
hpnicfProtocolVlanPortProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfProtocolVlanPortProtocolType.setStatus(_A)
_HpnicfProtocolVlanPortProtocolSubType_Type=HpnicfvProtocolVlanProtocolSubType
_HpnicfProtocolVlanPortProtocolSubType_Object=MibTableColumn
hpnicfProtocolVlanPortProtocolSubType=_HpnicfProtocolVlanPortProtocolSubType_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,6,1,5),_HpnicfProtocolVlanPortProtocolSubType_Type())
hpnicfProtocolVlanPortProtocolSubType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfProtocolVlanPortProtocolSubType.setStatus(_A)
_HpnicfProtocolVlanPortTypeValue_Type=OctetString
_HpnicfProtocolVlanPortTypeValue_Object=MibTableColumn
hpnicfProtocolVlanPortTypeValue=_HpnicfProtocolVlanPortTypeValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,6,1,6),_HpnicfProtocolVlanPortTypeValue_Type())
hpnicfProtocolVlanPortTypeValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfProtocolVlanPortTypeValue.setStatus(_A)
_HpnicfProtocolVlanPortRowStatus_Type=RowStatus
_HpnicfProtocolVlanPortRowStatus_Object=MibTableColumn
hpnicfProtocolVlanPortRowStatus=_HpnicfProtocolVlanPortRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,6,1,7),_HpnicfProtocolVlanPortRowStatus_Type())
hpnicfProtocolVlanPortRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfProtocolVlanPortRowStatus.setStatus(_A)
class _HpnicfProtocolVlanPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_HpnicfProtocolVlanPortStatus_Type.__name__=_G
_HpnicfProtocolVlanPortStatus_Object=MibTableColumn
hpnicfProtocolVlanPortStatus=_HpnicfProtocolVlanPortStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,6,1,8),_HpnicfProtocolVlanPortStatus_Type())
hpnicfProtocolVlanPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfProtocolVlanPortStatus.setStatus(_A)
_HpnicfDifferentProtocolNumAllPort_Type=Integer32
_HpnicfDifferentProtocolNumAllPort_Object=MibScalar
hpnicfDifferentProtocolNumAllPort=_HpnicfDifferentProtocolNumAllPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,16,1,7),_HpnicfDifferentProtocolNumAllPort_Type())
hpnicfDifferentProtocolNumAllPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDifferentProtocolNumAllPort.setStatus(_A)
_HpnicfProtocolVlanConformance_ObjectIdentity=ObjectIdentity
hpnicfProtocolVlanConformance=_HpnicfProtocolVlanConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,16,2))
_HpnicfProtocolVlanCompliances_ObjectIdentity=ObjectIdentity
hpnicfProtocolVlanCompliances=_HpnicfProtocolVlanCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,16,2,1))
_HpnicfProtocolVlanGroups_ObjectIdentity=ObjectIdentity
hpnicfProtocolVlanGroups=_HpnicfProtocolVlanGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,16,2,2))
hpnicfProtocolVlanOperateGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,16,2,2,1))
hpnicfProtocolVlanOperateGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:hpnicfProtocolVlanOperateGroup.setStatus(_A)
hpnicfProtocolVlanProtocolGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,16,2,2,2))
hpnicfProtocolVlanProtocolGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:hpnicfProtocolVlanProtocolGroup.setStatus(_A)
hpnicfProtocolVlanPortGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,16,2,2,3))
hpnicfProtocolVlanPortGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:hpnicfProtocolVlanPortGroup.setStatus(_A)
hpnicfProtocolVlanCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,16,2,1,1))
hpnicfProtocolVlanCompliance.setObjects(*((_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:hpnicfProtocolVlanCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'HpnicfvProtocolVlanProtocolType':HpnicfvProtocolVlanProtocolType,'HpnicfvProtocolVlanProtocolSubType':HpnicfvProtocolVlanProtocolSubType,'hpnicfProtocolVlan':hpnicfProtocolVlan,'hpnicfProtocolVlanOperate':hpnicfProtocolVlanOperate,_M:hpnicfProtocolNumAllVlan,_N:hpnicfProtocolNumPerVlan,_O:hpnicfProtocolNumAllPort,_P:hpnicfProtocolNumPerPort,'hpnicfProtocolVlanTable':hpnicfProtocolVlanTable,'hpnicfProtocolVlanEntry':hpnicfProtocolVlanEntry,_H:hpnicfProtocolVlanVlanId,_I:hpnicfProtocolVlanProtocolIndex,_R:hpnicfProtocolVlanProtocolType,_S:hpnicfProtocolVlanProtocolSubType,_T:hpnicfProtocolVlanProtocolTypeValue,_U:hpnicfProtocolVlanRowStatus,'hpnicfProtocolVlanPortTable':hpnicfProtocolVlanPortTable,'hpnicfProtocolVlanPortEntry':hpnicfProtocolVlanPortEntry,_J:hpnicfProtocolVlanPortIndex,_K:hpnicfProtocolVlanPortVlanId,_L:hpnicfProtocolVlanPortProtocolId,_V:hpnicfProtocolVlanPortProtocolType,_W:hpnicfProtocolVlanPortProtocolSubType,_X:hpnicfProtocolVlanPortTypeValue,_Y:hpnicfProtocolVlanPortRowStatus,'hpnicfProtocolVlanPortStatus':hpnicfProtocolVlanPortStatus,_Q:hpnicfDifferentProtocolNumAllPort,'hpnicfProtocolVlanConformance':hpnicfProtocolVlanConformance,'hpnicfProtocolVlanCompliances':hpnicfProtocolVlanCompliances,'hpnicfProtocolVlanCompliance':hpnicfProtocolVlanCompliance,'hpnicfProtocolVlanGroups':hpnicfProtocolVlanGroups,_Z:hpnicfProtocolVlanOperateGroup,_a:hpnicfProtocolVlanProtocolGroup,_b:hpnicfProtocolVlanPortGroup})