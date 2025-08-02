_m='ntnQos802FilterExtGroup'
_l='ntnQosActionExtGroup'
_k='ntnQosIfDscpMappingExtGroup'
_j='ntnQosInterfaceTypeExtGroup'
_i='ntnQosIfPriAssignmentGroup'
_h='ntnQos802FilterVlanIdSet'
_g='ntnQos802FilterSrcL4PortMax'
_f='ntnQos802FilterSrcL4PortMin'
_e='ntnQos802FilterDstL4PortMax'
_d='ntnQos802FilterDstL4PortMin'
_c='ntnQos802FilterProtocol'
_b='ntnQos802FilterDscp'
_a='ntnQosActionExtMirrorDirection'
_Z='ntnQosActionExtUpdatePri'
_Y='ntnQosActionExtSetDropPrec'
_X='ntnQosActionExtMirrorFrame'
_W='ntnQosActionExtCopyToCpu'
_V='ntnQosActionExtAssignFlowId'
_U='ntnQosIfDscpMappingExtDropPrec'
_T='ntnQosInterfaceTypeExtIfClass'
_S='ntnQosIfPriAssignmentStatus'
_R='ntnQosIfPriAssignmentStorageType'
_Q='ntnQosIfPriAssignmentQueue'
_P='ntnQosIfPriAssignmentPri'
_O='ntnQosIfPriAssignmentRoles'
_N='ntnQos802FilterExtEntry'
_M='ntnQosActionExtEntry'
_L='ntnQosIfDscpMappingExtEntry'
_K='ntnQosInterfaceTypeExtEntry'
_J='useEgressMap'
_I='ignore'
_H='useDefault'
_G='ntnQosIfPriAssignmentId'
_F='StorageType'
_E='OctetString'
_D='Integer32'
_C='read-create'
_B='NTN-QOS-POLICY-EXT-PIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PolicyInstanceId,RoleCombination=mibBuilder.importSymbols('POLICY-FRAMEWORK-PIB','PolicyInstanceId','RoleCombination')
QosIeee802Cos,qos802AceEntry,qos802DscpMappingEntry=mibBuilder.importSymbols('QOS-POLICY-802-PIB','QosIeee802Cos','qos802AceEntry','qos802DscpMappingEntry')
QosInterfaceQueueCount,qosActionEntry,qosInterfaceTypeEntry=mibBuilder.importSymbols('QOS-POLICY-IP-PIB','QosInterfaceQueueCount','qosActionEntry','qosInterfaceTypeEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_F,'TextualConvention','TruthValue')
policy,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','policy')
ntnQosPolicyExtPib=ModuleIdentity((1,3,6,1,4,1,45,4,4))
if mibBuilder.loadTexts:ntnQosPolicyExtPib.setRevisions(('2004-07-20 00:00',))
class DropPrecedence(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NtnQosPolicyExtPibClasses_ObjectIdentity=ObjectIdentity
ntnQosPolicyExtPibClasses=_NtnQosPolicyExtPibClasses_ObjectIdentity((1,3,6,1,4,1,45,4,4,1))
_NtnQosIfParametersExt_ObjectIdentity=ObjectIdentity
ntnQosIfParametersExt=_NtnQosIfParametersExt_ObjectIdentity((1,3,6,1,4,1,45,4,4,1,1))
_NtnQosIfPriAssignmentTable_Object=MibTable
ntnQosIfPriAssignmentTable=_NtnQosIfPriAssignmentTable_Object((1,3,6,1,4,1,45,4,4,1,1,1))
if mibBuilder.loadTexts:ntnQosIfPriAssignmentTable.setStatus(_A)
_NtnQosIfPriAssignmentEntry_Object=MibTableRow
ntnQosIfPriAssignmentEntry=_NtnQosIfPriAssignmentEntry_Object((1,3,6,1,4,1,45,4,4,1,1,1,1))
ntnQosIfPriAssignmentEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:ntnQosIfPriAssignmentEntry.setStatus(_A)
_NtnQosIfPriAssignmentId_Type=PolicyInstanceId
_NtnQosIfPriAssignmentId_Object=MibTableColumn
ntnQosIfPriAssignmentId=_NtnQosIfPriAssignmentId_Object((1,3,6,1,4,1,45,4,4,1,1,1,1,1),_NtnQosIfPriAssignmentId_Type())
ntnQosIfPriAssignmentId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ntnQosIfPriAssignmentId.setStatus(_A)
_NtnQosIfPriAssignmentRoles_Type=RoleCombination
_NtnQosIfPriAssignmentRoles_Object=MibTableColumn
ntnQosIfPriAssignmentRoles=_NtnQosIfPriAssignmentRoles_Object((1,3,6,1,4,1,45,4,4,1,1,1,1,2),_NtnQosIfPriAssignmentRoles_Type())
ntnQosIfPriAssignmentRoles.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosIfPriAssignmentRoles.setStatus(_A)
_NtnQosIfPriAssignmentPri_Type=QosIeee802Cos
_NtnQosIfPriAssignmentPri_Object=MibTableColumn
ntnQosIfPriAssignmentPri=_NtnQosIfPriAssignmentPri_Object((1,3,6,1,4,1,45,4,4,1,1,1,1,3),_NtnQosIfPriAssignmentPri_Type())
ntnQosIfPriAssignmentPri.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosIfPriAssignmentPri.setStatus(_A)
_NtnQosIfPriAssignmentQueue_Type=QosInterfaceQueueCount
_NtnQosIfPriAssignmentQueue_Object=MibTableColumn
ntnQosIfPriAssignmentQueue=_NtnQosIfPriAssignmentQueue_Object((1,3,6,1,4,1,45,4,4,1,1,1,1,4),_NtnQosIfPriAssignmentQueue_Type())
ntnQosIfPriAssignmentQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosIfPriAssignmentQueue.setStatus(_A)
class _NtnQosIfPriAssignmentStorageType_Type(StorageType):defaultValue=2
_NtnQosIfPriAssignmentStorageType_Type.__name__=_F
_NtnQosIfPriAssignmentStorageType_Object=MibTableColumn
ntnQosIfPriAssignmentStorageType=_NtnQosIfPriAssignmentStorageType_Object((1,3,6,1,4,1,45,4,4,1,1,1,1,5),_NtnQosIfPriAssignmentStorageType_Type())
ntnQosIfPriAssignmentStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosIfPriAssignmentStorageType.setStatus(_A)
_NtnQosIfPriAssignmentStatus_Type=RowStatus
_NtnQosIfPriAssignmentStatus_Object=MibTableColumn
ntnQosIfPriAssignmentStatus=_NtnQosIfPriAssignmentStatus_Object((1,3,6,1,4,1,45,4,4,1,1,1,1,6),_NtnQosIfPriAssignmentStatus_Type())
ntnQosIfPriAssignmentStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosIfPriAssignmentStatus.setStatus(_A)
_NtnQosInterfaceTypeExtTable_Object=MibTable
ntnQosInterfaceTypeExtTable=_NtnQosInterfaceTypeExtTable_Object((1,3,6,1,4,1,45,4,4,1,1,2))
if mibBuilder.loadTexts:ntnQosInterfaceTypeExtTable.setStatus(_A)
_NtnQosInterfaceTypeExtEntry_Object=MibTableRow
ntnQosInterfaceTypeExtEntry=_NtnQosInterfaceTypeExtEntry_Object((1,3,6,1,4,1,45,4,4,1,1,2,1))
if mibBuilder.loadTexts:ntnQosInterfaceTypeExtEntry.setStatus(_A)
class _NtnQosInterfaceTypeExtIfClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('core',1),('access',2)))
_NtnQosInterfaceTypeExtIfClass_Type.__name__=_D
_NtnQosInterfaceTypeExtIfClass_Object=MibTableColumn
ntnQosInterfaceTypeExtIfClass=_NtnQosInterfaceTypeExtIfClass_Object((1,3,6,1,4,1,45,4,4,1,1,2,1,1),_NtnQosInterfaceTypeExtIfClass_Type())
ntnQosInterfaceTypeExtIfClass.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosInterfaceTypeExtIfClass.setStatus(_A)
_NtnQosIfDscpMappingExtTable_Object=MibTable
ntnQosIfDscpMappingExtTable=_NtnQosIfDscpMappingExtTable_Object((1,3,6,1,4,1,45,4,4,1,1,3))
if mibBuilder.loadTexts:ntnQosIfDscpMappingExtTable.setStatus(_A)
_NtnQosIfDscpMappingExtEntry_Object=MibTableRow
ntnQosIfDscpMappingExtEntry=_NtnQosIfDscpMappingExtEntry_Object((1,3,6,1,4,1,45,4,4,1,1,3,1))
if mibBuilder.loadTexts:ntnQosIfDscpMappingExtEntry.setStatus(_A)
_NtnQosIfDscpMappingExtDropPrec_Type=DropPrecedence
_NtnQosIfDscpMappingExtDropPrec_Object=MibTableColumn
ntnQosIfDscpMappingExtDropPrec=_NtnQosIfDscpMappingExtDropPrec_Object((1,3,6,1,4,1,45,4,4,1,1,3,1,1),_NtnQosIfDscpMappingExtDropPrec_Type())
ntnQosIfDscpMappingExtDropPrec.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosIfDscpMappingExtDropPrec.setStatus(_A)
_NtnQosActionExt_ObjectIdentity=ObjectIdentity
ntnQosActionExt=_NtnQosActionExt_ObjectIdentity((1,3,6,1,4,1,45,4,4,1,2))
_NtnQosActionExtTable_Object=MibTable
ntnQosActionExtTable=_NtnQosActionExtTable_Object((1,3,6,1,4,1,45,4,4,1,2,1))
if mibBuilder.loadTexts:ntnQosActionExtTable.setStatus(_A)
_NtnQosActionExtEntry_Object=MibTableRow
ntnQosActionExtEntry=_NtnQosActionExtEntry_Object((1,3,6,1,4,1,45,4,4,1,2,1,1))
if mibBuilder.loadTexts:ntnQosActionExtEntry.setStatus(_A)
class _NtnQosActionExtAssignFlowId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,65535))
_NtnQosActionExtAssignFlowId_Type.__name__=_D
_NtnQosActionExtAssignFlowId_Object=MibTableColumn
ntnQosActionExtAssignFlowId=_NtnQosActionExtAssignFlowId_Object((1,3,6,1,4,1,45,4,4,1,2,1,1,1),_NtnQosActionExtAssignFlowId_Type())
ntnQosActionExtAssignFlowId.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosActionExtAssignFlowId.setStatus(_A)
_NtnQosActionExtCopyToCpu_Type=TruthValue
_NtnQosActionExtCopyToCpu_Object=MibTableColumn
ntnQosActionExtCopyToCpu=_NtnQosActionExtCopyToCpu_Object((1,3,6,1,4,1,45,4,4,1,2,1,1,2),_NtnQosActionExtCopyToCpu_Type())
ntnQosActionExtCopyToCpu.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosActionExtCopyToCpu.setStatus(_A)
_NtnQosActionExtMirrorFrame_Type=TruthValue
_NtnQosActionExtMirrorFrame_Object=MibTableColumn
ntnQosActionExtMirrorFrame=_NtnQosActionExtMirrorFrame_Object((1,3,6,1,4,1,45,4,4,1,2,1,1,3),_NtnQosActionExtMirrorFrame_Type())
ntnQosActionExtMirrorFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosActionExtMirrorFrame.setStatus(_A)
class _NtnQosActionExtSetDropPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('dropPrec1',1),('dropPrec2',2),('dropPrec3',3),('dropPrec4',4),('dropPrec5',5),('dropPrec6',6),('dropPrec7',7),('dropPrec8',8),(_H,9),(_I,10),(_J,11)))
_NtnQosActionExtSetDropPrec_Type.__name__=_D
_NtnQosActionExtSetDropPrec_Object=MibTableColumn
ntnQosActionExtSetDropPrec=_NtnQosActionExtSetDropPrec_Object((1,3,6,1,4,1,45,4,4,1,2,1,1,4),_NtnQosActionExtSetDropPrec_Type())
ntnQosActionExtSetDropPrec.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosActionExtSetDropPrec.setStatus(_A)
class _NtnQosActionExtUpdatePri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('markAsPriority0',1),('markAsPriority1',2),('markAsPriority2',3),('markAsPriority3',4),('markAsPriority4',5),('markAsPriority5',6),('markAsPriority6',7),('markAsPriority7',8),(_H,9),(_I,10),(_J,11)))
_NtnQosActionExtUpdatePri_Type.__name__=_D
_NtnQosActionExtUpdatePri_Object=MibTableColumn
ntnQosActionExtUpdatePri=_NtnQosActionExtUpdatePri_Object((1,3,6,1,4,1,45,4,4,1,2,1,1,5),_NtnQosActionExtUpdatePri_Type())
ntnQosActionExtUpdatePri.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosActionExtUpdatePri.setStatus(_A)
class _NtnQosActionExtMirrorDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ingress',1),('egress',2)))
_NtnQosActionExtMirrorDirection_Type.__name__=_D
_NtnQosActionExtMirrorDirection_Object=MibTableColumn
ntnQosActionExtMirrorDirection=_NtnQosActionExtMirrorDirection_Object((1,3,6,1,4,1,45,4,4,1,2,1,1,6),_NtnQosActionExtMirrorDirection_Type())
ntnQosActionExtMirrorDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQosActionExtMirrorDirection.setStatus(_A)
_NtnQos802FilterExt_ObjectIdentity=ObjectIdentity
ntnQos802FilterExt=_NtnQos802FilterExt_ObjectIdentity((1,3,6,1,4,1,45,4,4,1,3))
_NtnQos802FilterExtTable_Object=MibTable
ntnQos802FilterExtTable=_NtnQos802FilterExtTable_Object((1,3,6,1,4,1,45,4,4,1,3,1))
if mibBuilder.loadTexts:ntnQos802FilterExtTable.setStatus(_A)
_NtnQos802FilterExtEntry_Object=MibTableRow
ntnQos802FilterExtEntry=_NtnQos802FilterExtEntry_Object((1,3,6,1,4,1,45,4,4,1,3,1,1))
if mibBuilder.loadTexts:ntnQos802FilterExtEntry.setStatus(_A)
class _NtnQos802FilterDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,63))
_NtnQos802FilterDscp_Type.__name__=_D
_NtnQos802FilterDscp_Object=MibTableColumn
ntnQos802FilterDscp=_NtnQos802FilterDscp_Object((1,3,6,1,4,1,45,4,4,1,3,1,1,1),_NtnQos802FilterDscp_Type())
ntnQos802FilterDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQos802FilterDscp.setStatus(_A)
class _NtnQos802FilterProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NtnQos802FilterProtocol_Type.__name__=_D
_NtnQos802FilterProtocol_Object=MibTableColumn
ntnQos802FilterProtocol=_NtnQos802FilterProtocol_Object((1,3,6,1,4,1,45,4,4,1,3,1,1,2),_NtnQos802FilterProtocol_Type())
ntnQos802FilterProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQos802FilterProtocol.setStatus(_A)
class _NtnQos802FilterDstL4PortMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NtnQos802FilterDstL4PortMin_Type.__name__=_D
_NtnQos802FilterDstL4PortMin_Object=MibTableColumn
ntnQos802FilterDstL4PortMin=_NtnQos802FilterDstL4PortMin_Object((1,3,6,1,4,1,45,4,4,1,3,1,1,3),_NtnQos802FilterDstL4PortMin_Type())
ntnQos802FilterDstL4PortMin.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQos802FilterDstL4PortMin.setStatus(_A)
class _NtnQos802FilterDstL4PortMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NtnQos802FilterDstL4PortMax_Type.__name__=_D
_NtnQos802FilterDstL4PortMax_Object=MibTableColumn
ntnQos802FilterDstL4PortMax=_NtnQos802FilterDstL4PortMax_Object((1,3,6,1,4,1,45,4,4,1,3,1,1,4),_NtnQos802FilterDstL4PortMax_Type())
ntnQos802FilterDstL4PortMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQos802FilterDstL4PortMax.setStatus(_A)
class _NtnQos802FilterSrcL4PortMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NtnQos802FilterSrcL4PortMin_Type.__name__=_D
_NtnQos802FilterSrcL4PortMin_Object=MibTableColumn
ntnQos802FilterSrcL4PortMin=_NtnQos802FilterSrcL4PortMin_Object((1,3,6,1,4,1,45,4,4,1,3,1,1,5),_NtnQos802FilterSrcL4PortMin_Type())
ntnQos802FilterSrcL4PortMin.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQos802FilterSrcL4PortMin.setStatus(_A)
class _NtnQos802FilterSrcL4PortMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NtnQos802FilterSrcL4PortMax_Type.__name__=_D
_NtnQos802FilterSrcL4PortMax_Object=MibTableColumn
ntnQos802FilterSrcL4PortMax=_NtnQos802FilterSrcL4PortMax_Object((1,3,6,1,4,1,45,4,4,1,3,1,1,6),_NtnQos802FilterSrcL4PortMax_Type())
ntnQos802FilterSrcL4PortMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQos802FilterSrcL4PortMax.setStatus(_A)
class _NtnQos802FilterVlanIdSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_NtnQos802FilterVlanIdSet_Type.__name__=_E
_NtnQos802FilterVlanIdSet_Object=MibTableColumn
ntnQos802FilterVlanIdSet=_NtnQos802FilterVlanIdSet_Object((1,3,6,1,4,1,45,4,4,1,3,1,1,7),_NtnQos802FilterVlanIdSet_Type())
ntnQos802FilterVlanIdSet.setMaxAccess(_C)
if mibBuilder.loadTexts:ntnQos802FilterVlanIdSet.setStatus(_A)
_NtnQosPolicyExtPibConformance_ObjectIdentity=ObjectIdentity
ntnQosPolicyExtPibConformance=_NtnQosPolicyExtPibConformance_ObjectIdentity((1,3,6,1,4,1,45,4,4,2))
_NtnQosPolicyExtPibCompliances_ObjectIdentity=ObjectIdentity
ntnQosPolicyExtPibCompliances=_NtnQosPolicyExtPibCompliances_ObjectIdentity((1,3,6,1,4,1,45,4,4,2,1))
_NtnQosPolicyExtPibGroups_ObjectIdentity=ObjectIdentity
ntnQosPolicyExtPibGroups=_NtnQosPolicyExtPibGroups_ObjectIdentity((1,3,6,1,4,1,45,4,4,2,2))
qosInterfaceTypeEntry.registerAugmentions((_B,_K))
ntnQosInterfaceTypeExtEntry.setIndexNames(*qosInterfaceTypeEntry.getIndexNames())
qos802DscpMappingEntry.registerAugmentions((_B,_L))
ntnQosIfDscpMappingExtEntry.setIndexNames(*qos802DscpMappingEntry.getIndexNames())
qosActionEntry.registerAugmentions((_B,_M))
ntnQosActionExtEntry.setIndexNames(*qosActionEntry.getIndexNames())
qos802AceEntry.registerAugmentions((_B,_N))
ntnQos802FilterExtEntry.setIndexNames(*qos802AceEntry.getIndexNames())
ntnQosIfPriAssignmentGroup=ObjectGroup((1,3,6,1,4,1,45,4,4,2,2,1))
ntnQosIfPriAssignmentGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:ntnQosIfPriAssignmentGroup.setStatus(_A)
ntnQosInterfaceTypeExtGroup=ObjectGroup((1,3,6,1,4,1,45,4,4,2,2,2))
ntnQosInterfaceTypeExtGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:ntnQosInterfaceTypeExtGroup.setStatus(_A)
ntnQosIfDscpMappingExtGroup=ObjectGroup((1,3,6,1,4,1,45,4,4,2,2,3))
ntnQosIfDscpMappingExtGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:ntnQosIfDscpMappingExtGroup.setStatus(_A)
ntnQosActionExtGroup=ObjectGroup((1,3,6,1,4,1,45,4,4,2,2,4))
ntnQosActionExtGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:ntnQosActionExtGroup.setStatus(_A)
ntnQos802FilterExtGroup=ObjectGroup((1,3,6,1,4,1,45,4,4,2,2,5))
ntnQos802FilterExtGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:ntnQos802FilterExtGroup.setStatus(_A)
ntnQosPolicyExtPibCompliance=ModuleCompliance((1,3,6,1,4,1,45,4,4,2,1,1))
ntnQosPolicyExtPibCompliance.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:ntnQosPolicyExtPibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'DropPrecedence':DropPrecedence,'ntnQosPolicyExtPib':ntnQosPolicyExtPib,'ntnQosPolicyExtPibClasses':ntnQosPolicyExtPibClasses,'ntnQosIfParametersExt':ntnQosIfParametersExt,'ntnQosIfPriAssignmentTable':ntnQosIfPriAssignmentTable,'ntnQosIfPriAssignmentEntry':ntnQosIfPriAssignmentEntry,_G:ntnQosIfPriAssignmentId,_O:ntnQosIfPriAssignmentRoles,_P:ntnQosIfPriAssignmentPri,_Q:ntnQosIfPriAssignmentQueue,_R:ntnQosIfPriAssignmentStorageType,_S:ntnQosIfPriAssignmentStatus,'ntnQosInterfaceTypeExtTable':ntnQosInterfaceTypeExtTable,_K:ntnQosInterfaceTypeExtEntry,_T:ntnQosInterfaceTypeExtIfClass,'ntnQosIfDscpMappingExtTable':ntnQosIfDscpMappingExtTable,_L:ntnQosIfDscpMappingExtEntry,_U:ntnQosIfDscpMappingExtDropPrec,'ntnQosActionExt':ntnQosActionExt,'ntnQosActionExtTable':ntnQosActionExtTable,_M:ntnQosActionExtEntry,_V:ntnQosActionExtAssignFlowId,_W:ntnQosActionExtCopyToCpu,_X:ntnQosActionExtMirrorFrame,_Y:ntnQosActionExtSetDropPrec,_Z:ntnQosActionExtUpdatePri,_a:ntnQosActionExtMirrorDirection,'ntnQos802FilterExt':ntnQos802FilterExt,'ntnQos802FilterExtTable':ntnQos802FilterExtTable,_N:ntnQos802FilterExtEntry,_b:ntnQos802FilterDscp,_c:ntnQos802FilterProtocol,_d:ntnQos802FilterDstL4PortMin,_e:ntnQos802FilterDstL4PortMax,_f:ntnQos802FilterSrcL4PortMin,_g:ntnQos802FilterSrcL4PortMax,_h:ntnQos802FilterVlanIdSet,'ntnQosPolicyExtPibConformance':ntnQosPolicyExtPibConformance,'ntnQosPolicyExtPibCompliances':ntnQosPolicyExtPibCompliances,'ntnQosPolicyExtPibCompliance':ntnQosPolicyExtPibCompliance,'ntnQosPolicyExtPibGroups':ntnQosPolicyExtPibGroups,_i:ntnQosIfPriAssignmentGroup,_j:ntnQosInterfaceTypeExtGroup,_k:ntnQosIfDscpMappingExtGroup,_l:ntnQosActionExtGroup,_m:ntnQos802FilterExtGroup})