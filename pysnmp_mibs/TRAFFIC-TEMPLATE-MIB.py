_Z='hpicfTrafficGroup2'
_Y='hpicfTrafficTemplateGroup2'
_X='hpicfTrafficGroup'
_W='hpicfTrafficTemplateGroup'
_V='hpSwitchTrafficGroupEgressDiscardThreshold'
_U='hpSwitchTrafficTemplatePredefined'
_T='hpSwitchTrafficTemplateNumQueues'
_S='hpSwitchTrafficTemplateSystemDefaultName'
_R='hpSwitchTrafficQueue'
_Q='read-create'
_P='not-accessible'
_O='DisplayString'
_N='hpicfTrafficTemplateScalarGroup'
_M='hpSwitchTrafficGroupLossless'
_L='hpSwitchTrafficGroupPriorityMap'
_K='hpSwitchTrafficGroupName'
_J='hpSwitchTrafficGroupID'
_I='deprecated'
_H='hpSwitchTrafficTemplateRowStatus'
_G='hpSwitchTrafficTemplateMappedPorts'
_F='hpSwitchTrafficTemplateName'
_E='OctetString'
_D='Integer32'
_C='read-write'
_B='current'
_A='TRAFFIC-TEMPLATE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_O,'PhysAddress','RowStatus','TextualConvention','TruthValue')
hpicfTrafficTemplateMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,72))
if mibBuilder.loadTexts:hpicfTrafficTemplateMIB.setRevisions(('2012-02-02 00:00','2010-03-04 12:30'))
_HpicfTrafficTemplateObjects_ObjectIdentity=ObjectIdentity
hpicfTrafficTemplateObjects=_HpicfTrafficTemplateObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,72,1))
_HpicfTrafficTemplateScalars_ObjectIdentity=ObjectIdentity
hpicfTrafficTemplateScalars=_HpicfTrafficTemplateScalars_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,72,1,1))
class _HpSwitchTrafficTemplateSystemDefaultName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpSwitchTrafficTemplateSystemDefaultName_Type.__name__=_E
_HpSwitchTrafficTemplateSystemDefaultName_Object=MibScalar
hpSwitchTrafficTemplateSystemDefaultName=_HpSwitchTrafficTemplateSystemDefaultName_Object((1,3,6,1,4,1,11,2,14,11,5,1,72,1,1,1),_HpSwitchTrafficTemplateSystemDefaultName_Type())
hpSwitchTrafficTemplateSystemDefaultName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchTrafficTemplateSystemDefaultName.setStatus(_B)
_HpSwitchTrafficTemplate_ObjectIdentity=ObjectIdentity
hpSwitchTrafficTemplate=_HpSwitchTrafficTemplate_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,72,1,2))
_HpSwitchTrafficTemplateTable_Object=MibTable
hpSwitchTrafficTemplateTable=_HpSwitchTrafficTemplateTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,72,1,2,1))
if mibBuilder.loadTexts:hpSwitchTrafficTemplateTable.setStatus(_B)
_HpSwitchTrafficTemplateEntry_Object=MibTableRow
hpSwitchTrafficTemplateEntry=_HpSwitchTrafficTemplateEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,72,1,2,1,1))
hpSwitchTrafficTemplateEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:hpSwitchTrafficTemplateEntry.setStatus(_B)
class _HpSwitchTrafficTemplateName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_HpSwitchTrafficTemplateName_Type.__name__=_O
_HpSwitchTrafficTemplateName_Object=MibTableColumn
hpSwitchTrafficTemplateName=_HpSwitchTrafficTemplateName_Object((1,3,6,1,4,1,11,2,14,11,5,1,72,1,2,1,1,1),_HpSwitchTrafficTemplateName_Type())
hpSwitchTrafficTemplateName.setMaxAccess(_P)
if mibBuilder.loadTexts:hpSwitchTrafficTemplateName.setStatus(_B)
_HpSwitchTrafficTemplateMappedPorts_Type=PortList
_HpSwitchTrafficTemplateMappedPorts_Object=MibTableColumn
hpSwitchTrafficTemplateMappedPorts=_HpSwitchTrafficTemplateMappedPorts_Object((1,3,6,1,4,1,11,2,14,11,5,1,72,1,2,1,1,2),_HpSwitchTrafficTemplateMappedPorts_Type())
hpSwitchTrafficTemplateMappedPorts.setMaxAccess(_Q)
if mibBuilder.loadTexts:hpSwitchTrafficTemplateMappedPorts.setStatus(_B)
_HpSwitchTrafficTemplateRowStatus_Type=RowStatus
_HpSwitchTrafficTemplateRowStatus_Object=MibTableColumn
hpSwitchTrafficTemplateRowStatus=_HpSwitchTrafficTemplateRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,72,1,2,1,1,3),_HpSwitchTrafficTemplateRowStatus_Type())
hpSwitchTrafficTemplateRowStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:hpSwitchTrafficTemplateRowStatus.setStatus(_B)
class _HpSwitchTrafficTemplateNumQueues_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9000))
_HpSwitchTrafficTemplateNumQueues_Type.__name__=_D
_HpSwitchTrafficTemplateNumQueues_Object=MibTableColumn
hpSwitchTrafficTemplateNumQueues=_HpSwitchTrafficTemplateNumQueues_Object((1,3,6,1,4,1,11,2,14,11,5,1,72,1,2,1,1,4),_HpSwitchTrafficTemplateNumQueues_Type())
hpSwitchTrafficTemplateNumQueues.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchTrafficTemplateNumQueues.setStatus(_B)
_HpSwitchTrafficTemplatePredefined_Type=TruthValue
_HpSwitchTrafficTemplatePredefined_Object=MibTableColumn
hpSwitchTrafficTemplatePredefined=_HpSwitchTrafficTemplatePredefined_Object((1,3,6,1,4,1,11,2,14,11,5,1,72,1,2,1,1,5),_HpSwitchTrafficTemplatePredefined_Type())
hpSwitchTrafficTemplatePredefined.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpSwitchTrafficTemplatePredefined.setStatus(_B)
_HpSwitchTrafficGroupTable_Object=MibTable
hpSwitchTrafficGroupTable=_HpSwitchTrafficGroupTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,72,1,2,2))
if mibBuilder.loadTexts:hpSwitchTrafficGroupTable.setStatus(_B)
_HpSwitchTrafficGroupEntry_Object=MibTableRow
hpSwitchTrafficGroupEntry=_HpSwitchTrafficGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,72,1,2,2,1))
hpSwitchTrafficGroupEntry.setIndexNames((0,_A,_F),(0,_A,_R))
if mibBuilder.loadTexts:hpSwitchTrafficGroupEntry.setStatus(_B)
class _HpSwitchTrafficQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9000))
_HpSwitchTrafficQueue_Type.__name__=_D
_HpSwitchTrafficQueue_Object=MibTableColumn
hpSwitchTrafficQueue=_HpSwitchTrafficQueue_Object((1,3,6,1,4,1,11,2,14,11,5,1,72,1,2,2,1,1),_HpSwitchTrafficQueue_Type())
hpSwitchTrafficQueue.setMaxAccess(_P)
if mibBuilder.loadTexts:hpSwitchTrafficQueue.setStatus(_B)
class _HpSwitchTrafficGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_HpSwitchTrafficGroupID_Type.__name__=_D
_HpSwitchTrafficGroupID_Object=MibTableColumn
hpSwitchTrafficGroupID=_HpSwitchTrafficGroupID_Object((1,3,6,1,4,1,11,2,14,11,5,1,72,1,2,2,1,2),_HpSwitchTrafficGroupID_Type())
hpSwitchTrafficGroupID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchTrafficGroupID.setStatus(_B)
class _HpSwitchTrafficGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpSwitchTrafficGroupName_Type.__name__=_E
_HpSwitchTrafficGroupName_Object=MibTableColumn
hpSwitchTrafficGroupName=_HpSwitchTrafficGroupName_Object((1,3,6,1,4,1,11,2,14,11,5,1,72,1,2,2,1,3),_HpSwitchTrafficGroupName_Type())
hpSwitchTrafficGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchTrafficGroupName.setStatus(_B)
class _HpSwitchTrafficGroupPriorityMap_Type(Bits):namedValues=NamedValues(*(('priority0',0),('priority1',1),('priority2',2),('priority3',3),('priority4',4),('priority5',5),('priority6',6),('priority7',7),('priority8',8),('priority9',9),('priority10',10),('priority11',11),('priority12',12),('priority13',13),('priority14',14),('priority15',15)))
_HpSwitchTrafficGroupPriorityMap_Type.__name__='Bits'
_HpSwitchTrafficGroupPriorityMap_Object=MibTableColumn
hpSwitchTrafficGroupPriorityMap=_HpSwitchTrafficGroupPriorityMap_Object((1,3,6,1,4,1,11,2,14,11,5,1,72,1,2,2,1,4),_HpSwitchTrafficGroupPriorityMap_Type())
hpSwitchTrafficGroupPriorityMap.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchTrafficGroupPriorityMap.setStatus(_B)
_HpSwitchTrafficGroupLossless_Type=TruthValue
_HpSwitchTrafficGroupLossless_Object=MibTableColumn
hpSwitchTrafficGroupLossless=_HpSwitchTrafficGroupLossless_Object((1,3,6,1,4,1,11,2,14,11,5,1,72,1,2,2,1,5),_HpSwitchTrafficGroupLossless_Type())
hpSwitchTrafficGroupLossless.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchTrafficGroupLossless.setStatus(_B)
class _HpSwitchTrafficGroupEgressDiscardThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('low',1),('medium',2),('high',3)))
_HpSwitchTrafficGroupEgressDiscardThreshold_Type.__name__=_D
_HpSwitchTrafficGroupEgressDiscardThreshold_Object=MibTableColumn
hpSwitchTrafficGroupEgressDiscardThreshold=_HpSwitchTrafficGroupEgressDiscardThreshold_Object((1,3,6,1,4,1,11,2,14,11,5,1,72,1,2,2,1,6),_HpSwitchTrafficGroupEgressDiscardThreshold_Type())
hpSwitchTrafficGroupEgressDiscardThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchTrafficGroupEgressDiscardThreshold.setStatus(_B)
_HpicfTrafficTempalteConformance_ObjectIdentity=ObjectIdentity
hpicfTrafficTempalteConformance=_HpicfTrafficTempalteConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,72,2))
_HpicfTrafficTemplateGroups_ObjectIdentity=ObjectIdentity
hpicfTrafficTemplateGroups=_HpicfTrafficTemplateGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,72,2,1))
_HpicfTrafficTemplateCompliances_ObjectIdentity=ObjectIdentity
hpicfTrafficTemplateCompliances=_HpicfTrafficTemplateCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,72,2,2))
hpicfTrafficTemplateScalarGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,72,2,1,1))
hpicfTrafficTemplateScalarGroup.setObjects((_A,_S))
if mibBuilder.loadTexts:hpicfTrafficTemplateScalarGroup.setStatus(_B)
hpicfTrafficTemplateGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,72,2,1,2))
hpicfTrafficTemplateGroup.setObjects(*((_A,_G),(_A,_H)))
if mibBuilder.loadTexts:hpicfTrafficTemplateGroup.setStatus(_I)
hpicfTrafficGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,72,2,1,3))
hpicfTrafficGroup.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:hpicfTrafficGroup.setStatus(_I)
hpicfTrafficTemplateGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,72,2,1,4))
hpicfTrafficTemplateGroup2.setObjects(*((_A,_G),(_A,_H),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:hpicfTrafficTemplateGroup2.setStatus(_B)
hpicfTrafficGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,72,2,1,5))
hpicfTrafficGroup2.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_V)))
if mibBuilder.loadTexts:hpicfTrafficGroup2.setStatus(_B)
hpicfTrafficTemplateCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,72,2,2,1))
hpicfTrafficTemplateCompliance.setObjects(*((_A,_N),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:hpicfTrafficTemplateCompliance.setStatus(_I)
hpicfTrafficTemplateCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,72,2,2,2))
hpicfTrafficTemplateCompliance2.setObjects(*((_A,_N),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:hpicfTrafficTemplateCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfTrafficTemplateMIB':hpicfTrafficTemplateMIB,'hpicfTrafficTemplateObjects':hpicfTrafficTemplateObjects,'hpicfTrafficTemplateScalars':hpicfTrafficTemplateScalars,_S:hpSwitchTrafficTemplateSystemDefaultName,'hpSwitchTrafficTemplate':hpSwitchTrafficTemplate,'hpSwitchTrafficTemplateTable':hpSwitchTrafficTemplateTable,'hpSwitchTrafficTemplateEntry':hpSwitchTrafficTemplateEntry,_F:hpSwitchTrafficTemplateName,_G:hpSwitchTrafficTemplateMappedPorts,_H:hpSwitchTrafficTemplateRowStatus,_T:hpSwitchTrafficTemplateNumQueues,_U:hpSwitchTrafficTemplatePredefined,'hpSwitchTrafficGroupTable':hpSwitchTrafficGroupTable,'hpSwitchTrafficGroupEntry':hpSwitchTrafficGroupEntry,_R:hpSwitchTrafficQueue,_J:hpSwitchTrafficGroupID,_K:hpSwitchTrafficGroupName,_L:hpSwitchTrafficGroupPriorityMap,_M:hpSwitchTrafficGroupLossless,_V:hpSwitchTrafficGroupEgressDiscardThreshold,'hpicfTrafficTempalteConformance':hpicfTrafficTempalteConformance,'hpicfTrafficTemplateGroups':hpicfTrafficTemplateGroups,_N:hpicfTrafficTemplateScalarGroup,_W:hpicfTrafficTemplateGroup,_X:hpicfTrafficGroup,_Y:hpicfTrafficTemplateGroup2,_Z:hpicfTrafficGroup2,'hpicfTrafficTemplateCompliances':hpicfTrafficTemplateCompliances,'hpicfTrafficTemplateCompliance':hpicfTrafficTemplateCompliance,'hpicfTrafficTemplateCompliance2':hpicfTrafficTemplateCompliance2})