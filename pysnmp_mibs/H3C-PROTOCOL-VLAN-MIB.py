_b='h3cProtocolVlanPortGroup'
_a='h3cProtocolVlanProtocolGroup'
_Z='h3cProtocolVlanOperateGroup'
_Y='h3cProtocolVlanPortRowStatus'
_X='h3cProtocolVlanPortTypeValue'
_W='h3cProtocolVlanPortProtocolSubType'
_V='h3cProtocolVlanPortProtocolType'
_U='h3cProtocolVlanRowStatus'
_T='h3cProtocolVlanProtocolTypeValue'
_S='h3cProtocolVlanProtocolSubType'
_R='h3cProtocolVlanProtocolType'
_Q='h3cDifferentProtocolNumAllPort'
_P='h3cProtocolNumPerPort'
_O='h3cProtocolNumAllPort'
_N='h3cProtocolNumPerVlan'
_M='h3cProtocolNumAllVlan'
_L='h3cProtocolVlanPortProtocolId'
_K='h3cProtocolVlanPortVlanId'
_J='h3cProtocolVlanPortIndex'
_I='h3cProtocolVlanProtocolIndex'
_H='h3cProtocolVlanVlanId'
_G='Integer32'
_F='OctetString'
_E='read-create'
_D='not-accessible'
_C='read-only'
_B='H3C-PROTOCOL-VLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cProtocolVlan=ModuleIdentity((1,3,6,1,4,1,2011,10,2,16))
if mibBuilder.loadTexts:h3cProtocolVlan.setRevisions(('2004-08-31 19:38',))
class H3cvProtocolVlanProtocolType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,101,102,103,201)));namedValues=NamedValues(*(('ip',1),('ipx',2),('at',3),('ipv6',4),('mode-llc',101),('mode-snap',102),('mode-ethernetii',103),('notConfigure',201)))
class H3cvProtocolVlanProtocolSubType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('notused',1),('ethernetii',2),('llc',3),('raw',4),('snap',5),('etype',6)))
_H3cProtocolVlanOperate_ObjectIdentity=ObjectIdentity
h3cProtocolVlanOperate=_H3cProtocolVlanOperate_ObjectIdentity((1,3,6,1,4,1,2011,10,2,16,1))
_H3cProtocolNumAllVlan_Type=Integer32
_H3cProtocolNumAllVlan_Object=MibScalar
h3cProtocolNumAllVlan=_H3cProtocolNumAllVlan_Object((1,3,6,1,4,1,2011,10,2,16,1,1),_H3cProtocolNumAllVlan_Type())
h3cProtocolNumAllVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cProtocolNumAllVlan.setStatus(_A)
_H3cProtocolNumPerVlan_Type=Integer32
_H3cProtocolNumPerVlan_Object=MibScalar
h3cProtocolNumPerVlan=_H3cProtocolNumPerVlan_Object((1,3,6,1,4,1,2011,10,2,16,1,2),_H3cProtocolNumPerVlan_Type())
h3cProtocolNumPerVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cProtocolNumPerVlan.setStatus(_A)
_H3cProtocolNumAllPort_Type=Integer32
_H3cProtocolNumAllPort_Object=MibScalar
h3cProtocolNumAllPort=_H3cProtocolNumAllPort_Object((1,3,6,1,4,1,2011,10,2,16,1,3),_H3cProtocolNumAllPort_Type())
h3cProtocolNumAllPort.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cProtocolNumAllPort.setStatus(_A)
_H3cProtocolNumPerPort_Type=Integer32
_H3cProtocolNumPerPort_Object=MibScalar
h3cProtocolNumPerPort=_H3cProtocolNumPerPort_Object((1,3,6,1,4,1,2011,10,2,16,1,4),_H3cProtocolNumPerPort_Type())
h3cProtocolNumPerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cProtocolNumPerPort.setStatus(_A)
_H3cProtocolVlanTable_Object=MibTable
h3cProtocolVlanTable=_H3cProtocolVlanTable_Object((1,3,6,1,4,1,2011,10,2,16,1,5))
if mibBuilder.loadTexts:h3cProtocolVlanTable.setStatus(_A)
_H3cProtocolVlanEntry_Object=MibTableRow
h3cProtocolVlanEntry=_H3cProtocolVlanEntry_Object((1,3,6,1,4,1,2011,10,2,16,1,5,1))
h3cProtocolVlanEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:h3cProtocolVlanEntry.setStatus(_A)
_H3cProtocolVlanVlanId_Type=Integer32
_H3cProtocolVlanVlanId_Object=MibTableColumn
h3cProtocolVlanVlanId=_H3cProtocolVlanVlanId_Object((1,3,6,1,4,1,2011,10,2,16,1,5,1,1),_H3cProtocolVlanVlanId_Type())
h3cProtocolVlanVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cProtocolVlanVlanId.setStatus(_A)
_H3cProtocolVlanProtocolIndex_Type=Integer32
_H3cProtocolVlanProtocolIndex_Object=MibTableColumn
h3cProtocolVlanProtocolIndex=_H3cProtocolVlanProtocolIndex_Object((1,3,6,1,4,1,2011,10,2,16,1,5,1,2),_H3cProtocolVlanProtocolIndex_Type())
h3cProtocolVlanProtocolIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cProtocolVlanProtocolIndex.setStatus(_A)
_H3cProtocolVlanProtocolType_Type=H3cvProtocolVlanProtocolType
_H3cProtocolVlanProtocolType_Object=MibTableColumn
h3cProtocolVlanProtocolType=_H3cProtocolVlanProtocolType_Object((1,3,6,1,4,1,2011,10,2,16,1,5,1,3),_H3cProtocolVlanProtocolType_Type())
h3cProtocolVlanProtocolType.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cProtocolVlanProtocolType.setStatus(_A)
_H3cProtocolVlanProtocolSubType_Type=H3cvProtocolVlanProtocolSubType
_H3cProtocolVlanProtocolSubType_Object=MibTableColumn
h3cProtocolVlanProtocolSubType=_H3cProtocolVlanProtocolSubType_Object((1,3,6,1,4,1,2011,10,2,16,1,5,1,4),_H3cProtocolVlanProtocolSubType_Type())
h3cProtocolVlanProtocolSubType.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cProtocolVlanProtocolSubType.setStatus(_A)
class _H3cProtocolVlanProtocolTypeValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cProtocolVlanProtocolTypeValue_Type.__name__=_F
_H3cProtocolVlanProtocolTypeValue_Object=MibTableColumn
h3cProtocolVlanProtocolTypeValue=_H3cProtocolVlanProtocolTypeValue_Object((1,3,6,1,4,1,2011,10,2,16,1,5,1,5),_H3cProtocolVlanProtocolTypeValue_Type())
h3cProtocolVlanProtocolTypeValue.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cProtocolVlanProtocolTypeValue.setStatus(_A)
_H3cProtocolVlanRowStatus_Type=RowStatus
_H3cProtocolVlanRowStatus_Object=MibTableColumn
h3cProtocolVlanRowStatus=_H3cProtocolVlanRowStatus_Object((1,3,6,1,4,1,2011,10,2,16,1,5,1,6),_H3cProtocolVlanRowStatus_Type())
h3cProtocolVlanRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cProtocolVlanRowStatus.setStatus(_A)
_H3cProtocolVlanPortTable_Object=MibTable
h3cProtocolVlanPortTable=_H3cProtocolVlanPortTable_Object((1,3,6,1,4,1,2011,10,2,16,1,6))
if mibBuilder.loadTexts:h3cProtocolVlanPortTable.setStatus(_A)
_H3cProtocolVlanPortEntry_Object=MibTableRow
h3cProtocolVlanPortEntry=_H3cProtocolVlanPortEntry_Object((1,3,6,1,4,1,2011,10,2,16,1,6,1))
h3cProtocolVlanPortEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:h3cProtocolVlanPortEntry.setStatus(_A)
_H3cProtocolVlanPortIndex_Type=Integer32
_H3cProtocolVlanPortIndex_Object=MibTableColumn
h3cProtocolVlanPortIndex=_H3cProtocolVlanPortIndex_Object((1,3,6,1,4,1,2011,10,2,16,1,6,1,1),_H3cProtocolVlanPortIndex_Type())
h3cProtocolVlanPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cProtocolVlanPortIndex.setStatus(_A)
_H3cProtocolVlanPortVlanId_Type=Integer32
_H3cProtocolVlanPortVlanId_Object=MibTableColumn
h3cProtocolVlanPortVlanId=_H3cProtocolVlanPortVlanId_Object((1,3,6,1,4,1,2011,10,2,16,1,6,1,2),_H3cProtocolVlanPortVlanId_Type())
h3cProtocolVlanPortVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cProtocolVlanPortVlanId.setStatus(_A)
_H3cProtocolVlanPortProtocolId_Type=Integer32
_H3cProtocolVlanPortProtocolId_Object=MibTableColumn
h3cProtocolVlanPortProtocolId=_H3cProtocolVlanPortProtocolId_Object((1,3,6,1,4,1,2011,10,2,16,1,6,1,3),_H3cProtocolVlanPortProtocolId_Type())
h3cProtocolVlanPortProtocolId.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cProtocolVlanPortProtocolId.setStatus(_A)
_H3cProtocolVlanPortProtocolType_Type=H3cvProtocolVlanProtocolType
_H3cProtocolVlanPortProtocolType_Object=MibTableColumn
h3cProtocolVlanPortProtocolType=_H3cProtocolVlanPortProtocolType_Object((1,3,6,1,4,1,2011,10,2,16,1,6,1,4),_H3cProtocolVlanPortProtocolType_Type())
h3cProtocolVlanPortProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cProtocolVlanPortProtocolType.setStatus(_A)
_H3cProtocolVlanPortProtocolSubType_Type=H3cvProtocolVlanProtocolSubType
_H3cProtocolVlanPortProtocolSubType_Object=MibTableColumn
h3cProtocolVlanPortProtocolSubType=_H3cProtocolVlanPortProtocolSubType_Object((1,3,6,1,4,1,2011,10,2,16,1,6,1,5),_H3cProtocolVlanPortProtocolSubType_Type())
h3cProtocolVlanPortProtocolSubType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cProtocolVlanPortProtocolSubType.setStatus(_A)
_H3cProtocolVlanPortTypeValue_Type=OctetString
_H3cProtocolVlanPortTypeValue_Object=MibTableColumn
h3cProtocolVlanPortTypeValue=_H3cProtocolVlanPortTypeValue_Object((1,3,6,1,4,1,2011,10,2,16,1,6,1,6),_H3cProtocolVlanPortTypeValue_Type())
h3cProtocolVlanPortTypeValue.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cProtocolVlanPortTypeValue.setStatus(_A)
_H3cProtocolVlanPortRowStatus_Type=RowStatus
_H3cProtocolVlanPortRowStatus_Object=MibTableColumn
h3cProtocolVlanPortRowStatus=_H3cProtocolVlanPortRowStatus_Object((1,3,6,1,4,1,2011,10,2,16,1,6,1,7),_H3cProtocolVlanPortRowStatus_Type())
h3cProtocolVlanPortRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cProtocolVlanPortRowStatus.setStatus(_A)
class _H3cProtocolVlanPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_H3cProtocolVlanPortStatus_Type.__name__=_G
_H3cProtocolVlanPortStatus_Object=MibTableColumn
h3cProtocolVlanPortStatus=_H3cProtocolVlanPortStatus_Object((1,3,6,1,4,1,2011,10,2,16,1,6,1,8),_H3cProtocolVlanPortStatus_Type())
h3cProtocolVlanPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cProtocolVlanPortStatus.setStatus(_A)
_H3cDifferentProtocolNumAllPort_Type=Integer32
_H3cDifferentProtocolNumAllPort_Object=MibScalar
h3cDifferentProtocolNumAllPort=_H3cDifferentProtocolNumAllPort_Object((1,3,6,1,4,1,2011,10,2,16,1,7),_H3cDifferentProtocolNumAllPort_Type())
h3cDifferentProtocolNumAllPort.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDifferentProtocolNumAllPort.setStatus(_A)
_H3cProtocolVlanConformance_ObjectIdentity=ObjectIdentity
h3cProtocolVlanConformance=_H3cProtocolVlanConformance_ObjectIdentity((1,3,6,1,4,1,2011,10,2,16,2))
_H3cProtocolVlanCompliances_ObjectIdentity=ObjectIdentity
h3cProtocolVlanCompliances=_H3cProtocolVlanCompliances_ObjectIdentity((1,3,6,1,4,1,2011,10,2,16,2,1))
_H3cProtocolVlanGroups_ObjectIdentity=ObjectIdentity
h3cProtocolVlanGroups=_H3cProtocolVlanGroups_ObjectIdentity((1,3,6,1,4,1,2011,10,2,16,2,2))
h3cProtocolVlanOperateGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,16,2,2,1))
h3cProtocolVlanOperateGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:h3cProtocolVlanOperateGroup.setStatus(_A)
h3cProtocolVlanProtocolGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,16,2,2,2))
h3cProtocolVlanProtocolGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:h3cProtocolVlanProtocolGroup.setStatus(_A)
h3cProtocolVlanPortGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,16,2,2,3))
h3cProtocolVlanPortGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:h3cProtocolVlanPortGroup.setStatus(_A)
h3cProtocolVlanCompliance=ModuleCompliance((1,3,6,1,4,1,2011,10,2,16,2,1,1))
h3cProtocolVlanCompliance.setObjects(*((_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:h3cProtocolVlanCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'H3cvProtocolVlanProtocolType':H3cvProtocolVlanProtocolType,'H3cvProtocolVlanProtocolSubType':H3cvProtocolVlanProtocolSubType,'h3cProtocolVlan':h3cProtocolVlan,'h3cProtocolVlanOperate':h3cProtocolVlanOperate,_M:h3cProtocolNumAllVlan,_N:h3cProtocolNumPerVlan,_O:h3cProtocolNumAllPort,_P:h3cProtocolNumPerPort,'h3cProtocolVlanTable':h3cProtocolVlanTable,'h3cProtocolVlanEntry':h3cProtocolVlanEntry,_H:h3cProtocolVlanVlanId,_I:h3cProtocolVlanProtocolIndex,_R:h3cProtocolVlanProtocolType,_S:h3cProtocolVlanProtocolSubType,_T:h3cProtocolVlanProtocolTypeValue,_U:h3cProtocolVlanRowStatus,'h3cProtocolVlanPortTable':h3cProtocolVlanPortTable,'h3cProtocolVlanPortEntry':h3cProtocolVlanPortEntry,_J:h3cProtocolVlanPortIndex,_K:h3cProtocolVlanPortVlanId,_L:h3cProtocolVlanPortProtocolId,_V:h3cProtocolVlanPortProtocolType,_W:h3cProtocolVlanPortProtocolSubType,_X:h3cProtocolVlanPortTypeValue,_Y:h3cProtocolVlanPortRowStatus,'h3cProtocolVlanPortStatus':h3cProtocolVlanPortStatus,_Q:h3cDifferentProtocolNumAllPort,'h3cProtocolVlanConformance':h3cProtocolVlanConformance,'h3cProtocolVlanCompliances':h3cProtocolVlanCompliances,'h3cProtocolVlanCompliance':h3cProtocolVlanCompliance,'h3cProtocolVlanGroups':h3cProtocolVlanGroups,_Z:h3cProtocolVlanOperateGroup,_a:h3cProtocolVlanProtocolGroup,_b:h3cProtocolVlanPortGroup})