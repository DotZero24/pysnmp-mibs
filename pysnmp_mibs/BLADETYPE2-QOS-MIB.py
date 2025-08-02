_X='aclNewCfgAclRemarkIndex'
_W='aclNewCfgPortRemarkConfigIndex'
_V='aclCurCfgAclRemarkIndex'
_U='aclCurCfgPortRemarkConfigIndex'
_T='aclNewCfgAclMeterIndex'
_S='aclNewCfgPortMeterConfigIndex'
_R='aclCurCfgAclMeterIndex'
_Q='aclCurCfgPortMeterConfigIndex'
_P='aclNewCfgPortIndex'
_O='aclCurCfgPortIndex'
_N='qosNewCfgCosIndex'
_M='qosCurCfgCosIndex'
_L='qosNewCfgPriorityIndex'
_K='qosCurCfgPriorityIndex'
_J='qosNewCfgPortIndex'
_I='qosCurCfgPortIndex'
_H='disabled'
_G='enabled'
_F='BLADETYPE2-QOS-MIB'
_E='OctetString'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId')
hpSwitchBladeType2_Mgmt,=mibBuilder.importSymbols('HP-SWITCH-PL-MIB','hpSwitchBladeType2-Mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qos=ModuleIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8))
_QosConfigs_ObjectIdentity=ObjectIdentity
qosConfigs=_QosConfigs_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1))
_Qos8021p_ObjectIdentity=ObjectIdentity
qos8021p=_Qos8021p_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1))
_QosCurCfgPortPriorityTable_Object=MibTable
qosCurCfgPortPriorityTable=_QosCurCfgPortPriorityTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,1))
if mibBuilder.loadTexts:qosCurCfgPortPriorityTable.setStatus(_A)
_QosCurCfgPortPriorityEntry_Object=MibTableRow
qosCurCfgPortPriorityEntry=_QosCurCfgPortPriorityEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,1,1))
qosCurCfgPortPriorityEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:qosCurCfgPortPriorityEntry.setStatus(_A)
_QosCurCfgPortIndex_Type=Integer32
_QosCurCfgPortIndex_Object=MibTableColumn
qosCurCfgPortIndex=_QosCurCfgPortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,1,1,1),_QosCurCfgPortIndex_Type())
qosCurCfgPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCurCfgPortIndex.setStatus(_A)
class _QosCurCfgPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosCurCfgPortPriority_Type.__name__=_D
_QosCurCfgPortPriority_Object=MibTableColumn
qosCurCfgPortPriority=_QosCurCfgPortPriority_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,1,1,2),_QosCurCfgPortPriority_Type())
qosCurCfgPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCurCfgPortPriority.setStatus(_A)
_QosNewCfgPortPriorityTable_Object=MibTable
qosNewCfgPortPriorityTable=_QosNewCfgPortPriorityTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,2))
if mibBuilder.loadTexts:qosNewCfgPortPriorityTable.setStatus(_A)
_QosNewCfgPortPriorityEntry_Object=MibTableRow
qosNewCfgPortPriorityEntry=_QosNewCfgPortPriorityEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,2,1))
qosNewCfgPortPriorityEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:qosNewCfgPortPriorityEntry.setStatus(_A)
_QosNewCfgPortIndex_Type=Integer32
_QosNewCfgPortIndex_Object=MibTableColumn
qosNewCfgPortIndex=_QosNewCfgPortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,2,1,1),_QosNewCfgPortIndex_Type())
qosNewCfgPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qosNewCfgPortIndex.setStatus(_A)
class _QosNewCfgPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosNewCfgPortPriority_Type.__name__=_D
_QosNewCfgPortPriority_Object=MibTableColumn
qosNewCfgPortPriority=_QosNewCfgPortPriority_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,2,1,2),_QosNewCfgPortPriority_Type())
qosNewCfgPortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:qosNewCfgPortPriority.setStatus(_A)
_QosCurCfgPriorityCoSTable_Object=MibTable
qosCurCfgPriorityCoSTable=_QosCurCfgPriorityCoSTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,3))
if mibBuilder.loadTexts:qosCurCfgPriorityCoSTable.setStatus(_A)
_QosCurCfgPriorityCoSEntry_Object=MibTableRow
qosCurCfgPriorityCoSEntry=_QosCurCfgPriorityCoSEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,3,1))
qosCurCfgPriorityCoSEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:qosCurCfgPriorityCoSEntry.setStatus(_A)
class _QosCurCfgPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosCurCfgPriorityIndex_Type.__name__=_D
_QosCurCfgPriorityIndex_Object=MibTableColumn
qosCurCfgPriorityIndex=_QosCurCfgPriorityIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,3,1,1),_QosCurCfgPriorityIndex_Type())
qosCurCfgPriorityIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCurCfgPriorityIndex.setStatus(_A)
class _QosCurCfgPriorityCoSq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosCurCfgPriorityCoSq_Type.__name__=_D
_QosCurCfgPriorityCoSq_Object=MibTableColumn
qosCurCfgPriorityCoSq=_QosCurCfgPriorityCoSq_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,3,1,2),_QosCurCfgPriorityCoSq_Type())
qosCurCfgPriorityCoSq.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCurCfgPriorityCoSq.setStatus(_A)
_QosNewCfgPriorityCoSTable_Object=MibTable
qosNewCfgPriorityCoSTable=_QosNewCfgPriorityCoSTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,4))
if mibBuilder.loadTexts:qosNewCfgPriorityCoSTable.setStatus(_A)
_QosNewCfgPriorityCoSEntry_Object=MibTableRow
qosNewCfgPriorityCoSEntry=_QosNewCfgPriorityCoSEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,4,1))
qosNewCfgPriorityCoSEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:qosNewCfgPriorityCoSEntry.setStatus(_A)
class _QosNewCfgPriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosNewCfgPriorityIndex_Type.__name__=_D
_QosNewCfgPriorityIndex_Object=MibTableColumn
qosNewCfgPriorityIndex=_QosNewCfgPriorityIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,4,1,1),_QosNewCfgPriorityIndex_Type())
qosNewCfgPriorityIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qosNewCfgPriorityIndex.setStatus(_A)
class _QosNewCfgPriorityCoSq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosNewCfgPriorityCoSq_Type.__name__=_D
_QosNewCfgPriorityCoSq_Object=MibTableColumn
qosNewCfgPriorityCoSq=_QosNewCfgPriorityCoSq_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,4,1,2),_QosNewCfgPriorityCoSq_Type())
qosNewCfgPriorityCoSq.setMaxAccess(_C)
if mibBuilder.loadTexts:qosNewCfgPriorityCoSq.setStatus(_A)
_QosCurCfgCosWeightTable_Object=MibTable
qosCurCfgCosWeightTable=_QosCurCfgCosWeightTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,5))
if mibBuilder.loadTexts:qosCurCfgCosWeightTable.setStatus(_A)
_QosCurCfgCosWeightEntry_Object=MibTableRow
qosCurCfgCosWeightEntry=_QosCurCfgCosWeightEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,5,1))
qosCurCfgCosWeightEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:qosCurCfgCosWeightEntry.setStatus(_A)
class _QosCurCfgCosIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosCurCfgCosIndex_Type.__name__=_D
_QosCurCfgCosIndex_Object=MibTableColumn
qosCurCfgCosIndex=_QosCurCfgCosIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,5,1,1),_QosCurCfgCosIndex_Type())
qosCurCfgCosIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCurCfgCosIndex.setStatus(_A)
class _QosCurCfgCosWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_QosCurCfgCosWeight_Type.__name__=_D
_QosCurCfgCosWeight_Object=MibTableColumn
qosCurCfgCosWeight=_QosCurCfgCosWeight_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,5,1,2),_QosCurCfgCosWeight_Type())
qosCurCfgCosWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCurCfgCosWeight.setStatus(_A)
_QosNewCfgCosWeightTable_Object=MibTable
qosNewCfgCosWeightTable=_QosNewCfgCosWeightTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,6))
if mibBuilder.loadTexts:qosNewCfgCosWeightTable.setStatus(_A)
_QosNewCfgCosWeightEntry_Object=MibTableRow
qosNewCfgCosWeightEntry=_QosNewCfgCosWeightEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,6,1))
qosNewCfgCosWeightEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:qosNewCfgCosWeightEntry.setStatus(_A)
class _QosNewCfgCosIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_QosNewCfgCosIndex_Type.__name__=_D
_QosNewCfgCosIndex_Object=MibTableColumn
qosNewCfgCosIndex=_QosNewCfgCosIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,6,1,1),_QosNewCfgCosIndex_Type())
qosNewCfgCosIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qosNewCfgCosIndex.setStatus(_A)
class _QosNewCfgCosWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_QosNewCfgCosWeight_Type.__name__=_D
_QosNewCfgCosWeight_Object=MibTableColumn
qosNewCfgCosWeight=_QosNewCfgCosWeight_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,6,1,2),_QosNewCfgCosWeight_Type())
qosNewCfgCosWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:qosNewCfgCosWeight.setStatus(_A)
class _QosCurCfgCosNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,8)));namedValues=NamedValues(*(('num2',2),('num8',8)))
_QosCurCfgCosNum_Type.__name__=_D
_QosCurCfgCosNum_Object=MibScalar
qosCurCfgCosNum=_QosCurCfgCosNum_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,7),_QosCurCfgCosNum_Type())
qosCurCfgCosNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCurCfgCosNum.setStatus(_A)
class _QosNewCfgCosNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,8)));namedValues=NamedValues(*(('num2',2),('num8',8)))
_QosNewCfgCosNum_Type.__name__=_D
_QosNewCfgCosNum_Object=MibScalar
qosNewCfgCosNum=_QosNewCfgCosNum_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,1,8),_QosNewCfgCosNum_Type())
qosNewCfgCosNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qosNewCfgCosNum.setStatus(_A)
_AclCfg_ObjectIdentity=ObjectIdentity
aclCfg=_AclCfg_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2))
_AclCurCfgPortTable_Object=MibTable
aclCurCfgPortTable=_AclCurCfgPortTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,1))
if mibBuilder.loadTexts:aclCurCfgPortTable.setStatus(_A)
_AclCurCfgPortTableEntry_Object=MibTableRow
aclCurCfgPortTableEntry=_AclCurCfgPortTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,1,1))
aclCurCfgPortTableEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:aclCurCfgPortTableEntry.setStatus(_A)
_AclCurCfgPortIndex_Type=Integer32
_AclCurCfgPortIndex_Object=MibTableColumn
aclCurCfgPortIndex=_AclCurCfgPortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,1,1,1),_AclCurCfgPortIndex_Type())
aclCurCfgPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:aclCurCfgPortIndex.setStatus(_A)
class _AclCurCfgPortAclBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_AclCurCfgPortAclBmap_Type.__name__=_E
_AclCurCfgPortAclBmap_Object=MibTableColumn
aclCurCfgPortAclBmap=_AclCurCfgPortAclBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,1,1,2),_AclCurCfgPortAclBmap_Type())
aclCurCfgPortAclBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:aclCurCfgPortAclBmap.setStatus(_A)
class _AclCurCfgPortAclBlkBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_AclCurCfgPortAclBlkBmap_Type.__name__=_E
_AclCurCfgPortAclBlkBmap_Object=MibTableColumn
aclCurCfgPortAclBlkBmap=_AclCurCfgPortAclBlkBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,1,1,3),_AclCurCfgPortAclBlkBmap_Type())
aclCurCfgPortAclBlkBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:aclCurCfgPortAclBlkBmap.setStatus(_A)
class _AclCurCfgPortAclGrpBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_AclCurCfgPortAclGrpBmap_Type.__name__=_E
_AclCurCfgPortAclGrpBmap_Object=MibTableColumn
aclCurCfgPortAclGrpBmap=_AclCurCfgPortAclGrpBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,1,1,4),_AclCurCfgPortAclGrpBmap_Type())
aclCurCfgPortAclGrpBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:aclCurCfgPortAclGrpBmap.setStatus(_A)
_AclNewCfgPortTable_Object=MibTable
aclNewCfgPortTable=_AclNewCfgPortTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,2))
if mibBuilder.loadTexts:aclNewCfgPortTable.setStatus(_A)
_AclNewCfgPortTableEntry_Object=MibTableRow
aclNewCfgPortTableEntry=_AclNewCfgPortTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,2,1))
aclNewCfgPortTableEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:aclNewCfgPortTableEntry.setStatus(_A)
_AclNewCfgPortIndex_Type=Integer32
_AclNewCfgPortIndex_Object=MibTableColumn
aclNewCfgPortIndex=_AclNewCfgPortIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,2,1,1),_AclNewCfgPortIndex_Type())
aclNewCfgPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:aclNewCfgPortIndex.setStatus(_A)
_AclNewCfgPortAddAcl_Type=Unsigned32
_AclNewCfgPortAddAcl_Object=MibTableColumn
aclNewCfgPortAddAcl=_AclNewCfgPortAddAcl_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,2,1,2),_AclNewCfgPortAddAcl_Type())
aclNewCfgPortAddAcl.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgPortAddAcl.setStatus(_A)
_AclNewCfgPortAddAclBlk_Type=Unsigned32
_AclNewCfgPortAddAclBlk_Object=MibTableColumn
aclNewCfgPortAddAclBlk=_AclNewCfgPortAddAclBlk_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,2,1,3),_AclNewCfgPortAddAclBlk_Type())
aclNewCfgPortAddAclBlk.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgPortAddAclBlk.setStatus(_A)
_AclNewCfgPortAddAclGrp_Type=Unsigned32
_AclNewCfgPortAddAclGrp_Object=MibTableColumn
aclNewCfgPortAddAclGrp=_AclNewCfgPortAddAclGrp_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,2,1,4),_AclNewCfgPortAddAclGrp_Type())
aclNewCfgPortAddAclGrp.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgPortAddAclGrp.setStatus(_A)
_AclNewCfgPortRemoveAcl_Type=Unsigned32
_AclNewCfgPortRemoveAcl_Object=MibTableColumn
aclNewCfgPortRemoveAcl=_AclNewCfgPortRemoveAcl_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,2,1,5),_AclNewCfgPortRemoveAcl_Type())
aclNewCfgPortRemoveAcl.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgPortRemoveAcl.setStatus(_A)
_AclNewCfgPortRemoveAclBlk_Type=Unsigned32
_AclNewCfgPortRemoveAclBlk_Object=MibTableColumn
aclNewCfgPortRemoveAclBlk=_AclNewCfgPortRemoveAclBlk_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,2,1,6),_AclNewCfgPortRemoveAclBlk_Type())
aclNewCfgPortRemoveAclBlk.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgPortRemoveAclBlk.setStatus(_A)
_AclNewCfgPortRemoveAclGrp_Type=Unsigned32
_AclNewCfgPortRemoveAclGrp_Object=MibTableColumn
aclNewCfgPortRemoveAclGrp=_AclNewCfgPortRemoveAclGrp_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,2,1,7),_AclNewCfgPortRemoveAclGrp_Type())
aclNewCfgPortRemoveAclGrp.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgPortRemoveAclGrp.setStatus(_A)
class _AclNewCfgPortAclBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_AclNewCfgPortAclBmap_Type.__name__=_E
_AclNewCfgPortAclBmap_Object=MibTableColumn
aclNewCfgPortAclBmap=_AclNewCfgPortAclBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,2,1,8),_AclNewCfgPortAclBmap_Type())
aclNewCfgPortAclBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:aclNewCfgPortAclBmap.setStatus(_A)
class _AclNewCfgPortAclBlkBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_AclNewCfgPortAclBlkBmap_Type.__name__=_E
_AclNewCfgPortAclBlkBmap_Object=MibTableColumn
aclNewCfgPortAclBlkBmap=_AclNewCfgPortAclBlkBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,2,1,9),_AclNewCfgPortAclBlkBmap_Type())
aclNewCfgPortAclBlkBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:aclNewCfgPortAclBlkBmap.setStatus(_A)
class _AclNewCfgPortAclGrpBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_AclNewCfgPortAclGrpBmap_Type.__name__=_E
_AclNewCfgPortAclGrpBmap_Object=MibTableColumn
aclNewCfgPortAclGrpBmap=_AclNewCfgPortAclGrpBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,2,1,10),_AclNewCfgPortAclGrpBmap_Type())
aclNewCfgPortAclGrpBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:aclNewCfgPortAclGrpBmap.setStatus(_A)
_AclCurCfgPortAclMeterTable_Object=MibTable
aclCurCfgPortAclMeterTable=_AclCurCfgPortAclMeterTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,3))
if mibBuilder.loadTexts:aclCurCfgPortAclMeterTable.setStatus(_A)
_AclCurCfgPortAclMeterTableEntry_Object=MibTableRow
aclCurCfgPortAclMeterTableEntry=_AclCurCfgPortAclMeterTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,3,1))
aclCurCfgPortAclMeterTableEntry.setIndexNames((0,_F,_Q),(0,_F,_R))
if mibBuilder.loadTexts:aclCurCfgPortAclMeterTableEntry.setStatus(_A)
_AclCurCfgPortMeterConfigIndex_Type=Integer32
_AclCurCfgPortMeterConfigIndex_Object=MibTableColumn
aclCurCfgPortMeterConfigIndex=_AclCurCfgPortMeterConfigIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,3,1,1),_AclCurCfgPortMeterConfigIndex_Type())
aclCurCfgPortMeterConfigIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:aclCurCfgPortMeterConfigIndex.setStatus(_A)
_AclCurCfgAclMeterIndex_Type=Integer32
_AclCurCfgAclMeterIndex_Object=MibTableColumn
aclCurCfgAclMeterIndex=_AclCurCfgAclMeterIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,3,1,2),_AclCurCfgAclMeterIndex_Type())
aclCurCfgAclMeterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:aclCurCfgAclMeterIndex.setStatus(_A)
class _AclCurCfgAclMeterCommitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,1000000))
_AclCurCfgAclMeterCommitRate_Type.__name__=_D
_AclCurCfgAclMeterCommitRate_Object=MibTableColumn
aclCurCfgAclMeterCommitRate=_AclCurCfgAclMeterCommitRate_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,3,1,3),_AclCurCfgAclMeterCommitRate_Type())
aclCurCfgAclMeterCommitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:aclCurCfgAclMeterCommitRate.setStatus(_A)
class _AclCurCfgAclMeterMaxBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(32,64,128,256,512,1024,2048,4096)));namedValues=NamedValues(*(('k32',32),('k64',64),('k128',128),('k256',256),('k512',512),('k1024',1024),('k2048',2048),('k4096',4096)))
_AclCurCfgAclMeterMaxBurstSize_Type.__name__=_D
_AclCurCfgAclMeterMaxBurstSize_Object=MibTableColumn
aclCurCfgAclMeterMaxBurstSize=_AclCurCfgAclMeterMaxBurstSize_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,3,1,4),_AclCurCfgAclMeterMaxBurstSize_Type())
aclCurCfgAclMeterMaxBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:aclCurCfgAclMeterMaxBurstSize.setStatus(_A)
class _AclCurCfgAclMeterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AclCurCfgAclMeterStatus_Type.__name__=_D
_AclCurCfgAclMeterStatus_Object=MibTableColumn
aclCurCfgAclMeterStatus=_AclCurCfgAclMeterStatus_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,3,1,5),_AclCurCfgAclMeterStatus_Type())
aclCurCfgAclMeterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:aclCurCfgAclMeterStatus.setStatus(_A)
class _AclCurCfgAclMeterDropOrPass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('drop',2),('pass',3)))
_AclCurCfgAclMeterDropOrPass_Type.__name__=_D
_AclCurCfgAclMeterDropOrPass_Object=MibTableColumn
aclCurCfgAclMeterDropOrPass=_AclCurCfgAclMeterDropOrPass_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,3,1,6),_AclCurCfgAclMeterDropOrPass_Type())
aclCurCfgAclMeterDropOrPass.setMaxAccess(_B)
if mibBuilder.loadTexts:aclCurCfgAclMeterDropOrPass.setStatus(_A)
class _AclCurCfgAclMeterAclBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_AclCurCfgAclMeterAclBmap_Type.__name__=_E
_AclCurCfgAclMeterAclBmap_Object=MibTableColumn
aclCurCfgAclMeterAclBmap=_AclCurCfgAclMeterAclBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,3,1,7),_AclCurCfgAclMeterAclBmap_Type())
aclCurCfgAclMeterAclBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:aclCurCfgAclMeterAclBmap.setStatus(_A)
class _AclCurCfgAclMeterAclBlkBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_AclCurCfgAclMeterAclBlkBmap_Type.__name__=_E
_AclCurCfgAclMeterAclBlkBmap_Object=MibTableColumn
aclCurCfgAclMeterAclBlkBmap=_AclCurCfgAclMeterAclBlkBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,3,1,8),_AclCurCfgAclMeterAclBlkBmap_Type())
aclCurCfgAclMeterAclBlkBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:aclCurCfgAclMeterAclBlkBmap.setStatus(_A)
class _AclCurCfgAclMeterAclGrpBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_AclCurCfgAclMeterAclGrpBmap_Type.__name__=_E
_AclCurCfgAclMeterAclGrpBmap_Object=MibTableColumn
aclCurCfgAclMeterAclGrpBmap=_AclCurCfgAclMeterAclGrpBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,3,1,9),_AclCurCfgAclMeterAclGrpBmap_Type())
aclCurCfgAclMeterAclGrpBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:aclCurCfgAclMeterAclGrpBmap.setStatus(_A)
_AclNewCfgPortAclMeterTable_Object=MibTable
aclNewCfgPortAclMeterTable=_AclNewCfgPortAclMeterTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,4))
if mibBuilder.loadTexts:aclNewCfgPortAclMeterTable.setStatus(_A)
_AclNewCfgPortAclMeterTableEntry_Object=MibTableRow
aclNewCfgPortAclMeterTableEntry=_AclNewCfgPortAclMeterTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,4,1))
aclNewCfgPortAclMeterTableEntry.setIndexNames((0,_F,_S),(0,_F,_T))
if mibBuilder.loadTexts:aclNewCfgPortAclMeterTableEntry.setStatus(_A)
_AclNewCfgPortMeterConfigIndex_Type=Integer32
_AclNewCfgPortMeterConfigIndex_Object=MibTableColumn
aclNewCfgPortMeterConfigIndex=_AclNewCfgPortMeterConfigIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,4,1,1),_AclNewCfgPortMeterConfigIndex_Type())
aclNewCfgPortMeterConfigIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:aclNewCfgPortMeterConfigIndex.setStatus(_A)
_AclNewCfgAclMeterIndex_Type=Integer32
_AclNewCfgAclMeterIndex_Object=MibTableColumn
aclNewCfgAclMeterIndex=_AclNewCfgAclMeterIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,4,1,2),_AclNewCfgAclMeterIndex_Type())
aclNewCfgAclMeterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:aclNewCfgAclMeterIndex.setStatus(_A)
class _AclNewCfgAclMeterCommitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,1000000))
_AclNewCfgAclMeterCommitRate_Type.__name__=_D
_AclNewCfgAclMeterCommitRate_Object=MibTableColumn
aclNewCfgAclMeterCommitRate=_AclNewCfgAclMeterCommitRate_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,4,1,3),_AclNewCfgAclMeterCommitRate_Type())
aclNewCfgAclMeterCommitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgAclMeterCommitRate.setStatus(_A)
class _AclNewCfgAclMeterMaxBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(32,64,128,256,512,1024,2048,4096)));namedValues=NamedValues(*(('k32',32),('k64',64),('k128',128),('k256',256),('k512',512),('k1024',1024),('k2048',2048),('k4096',4096)))
_AclNewCfgAclMeterMaxBurstSize_Type.__name__=_D
_AclNewCfgAclMeterMaxBurstSize_Object=MibTableColumn
aclNewCfgAclMeterMaxBurstSize=_AclNewCfgAclMeterMaxBurstSize_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,4,1,4),_AclNewCfgAclMeterMaxBurstSize_Type())
aclNewCfgAclMeterMaxBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgAclMeterMaxBurstSize.setStatus(_A)
class _AclNewCfgAclMeterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AclNewCfgAclMeterStatus_Type.__name__=_D
_AclNewCfgAclMeterStatus_Object=MibTableColumn
aclNewCfgAclMeterStatus=_AclNewCfgAclMeterStatus_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,4,1,5),_AclNewCfgAclMeterStatus_Type())
aclNewCfgAclMeterStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgAclMeterStatus.setStatus(_A)
class _AclNewCfgAclMeterDropOrPass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('drop',2),('pass',3)))
_AclNewCfgAclMeterDropOrPass_Type.__name__=_D
_AclNewCfgAclMeterDropOrPass_Object=MibTableColumn
aclNewCfgAclMeterDropOrPass=_AclNewCfgAclMeterDropOrPass_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,4,1,6),_AclNewCfgAclMeterDropOrPass_Type())
aclNewCfgAclMeterDropOrPass.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgAclMeterDropOrPass.setStatus(_A)
_AclNewCfgAclMeterAssignAcl_Type=Unsigned32
_AclNewCfgAclMeterAssignAcl_Object=MibTableColumn
aclNewCfgAclMeterAssignAcl=_AclNewCfgAclMeterAssignAcl_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,4,1,7),_AclNewCfgAclMeterAssignAcl_Type())
aclNewCfgAclMeterAssignAcl.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgAclMeterAssignAcl.setStatus(_A)
_AclNewCfgAclMeterAssignAclBlk_Type=Unsigned32
_AclNewCfgAclMeterAssignAclBlk_Object=MibTableColumn
aclNewCfgAclMeterAssignAclBlk=_AclNewCfgAclMeterAssignAclBlk_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,4,1,8),_AclNewCfgAclMeterAssignAclBlk_Type())
aclNewCfgAclMeterAssignAclBlk.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgAclMeterAssignAclBlk.setStatus(_A)
_AclNewCfgAclMeterAssignAclGrp_Type=Unsigned32
_AclNewCfgAclMeterAssignAclGrp_Object=MibTableColumn
aclNewCfgAclMeterAssignAclGrp=_AclNewCfgAclMeterAssignAclGrp_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,4,1,9),_AclNewCfgAclMeterAssignAclGrp_Type())
aclNewCfgAclMeterAssignAclGrp.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgAclMeterAssignAclGrp.setStatus(_A)
_AclNewCfgAclMeterUnAssignAcl_Type=Unsigned32
_AclNewCfgAclMeterUnAssignAcl_Object=MibTableColumn
aclNewCfgAclMeterUnAssignAcl=_AclNewCfgAclMeterUnAssignAcl_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,4,1,10),_AclNewCfgAclMeterUnAssignAcl_Type())
aclNewCfgAclMeterUnAssignAcl.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgAclMeterUnAssignAcl.setStatus(_A)
_AclNewCfgAclMeterUnAssignAclBlk_Type=Unsigned32
_AclNewCfgAclMeterUnAssignAclBlk_Object=MibTableColumn
aclNewCfgAclMeterUnAssignAclBlk=_AclNewCfgAclMeterUnAssignAclBlk_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,4,1,11),_AclNewCfgAclMeterUnAssignAclBlk_Type())
aclNewCfgAclMeterUnAssignAclBlk.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgAclMeterUnAssignAclBlk.setStatus(_A)
_AclNewCfgAclMeterUnAssignAclGrp_Type=Unsigned32
_AclNewCfgAclMeterUnAssignAclGrp_Object=MibTableColumn
aclNewCfgAclMeterUnAssignAclGrp=_AclNewCfgAclMeterUnAssignAclGrp_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,4,1,12),_AclNewCfgAclMeterUnAssignAclGrp_Type())
aclNewCfgAclMeterUnAssignAclGrp.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgAclMeterUnAssignAclGrp.setStatus(_A)
class _AclNewCfgAclMeterAclBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_AclNewCfgAclMeterAclBmap_Type.__name__=_E
_AclNewCfgAclMeterAclBmap_Object=MibTableColumn
aclNewCfgAclMeterAclBmap=_AclNewCfgAclMeterAclBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,4,1,13),_AclNewCfgAclMeterAclBmap_Type())
aclNewCfgAclMeterAclBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:aclNewCfgAclMeterAclBmap.setStatus(_A)
class _AclNewCfgAclMeterAclBlkBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_AclNewCfgAclMeterAclBlkBmap_Type.__name__=_E
_AclNewCfgAclMeterAclBlkBmap_Object=MibTableColumn
aclNewCfgAclMeterAclBlkBmap=_AclNewCfgAclMeterAclBlkBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,4,1,14),_AclNewCfgAclMeterAclBlkBmap_Type())
aclNewCfgAclMeterAclBlkBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:aclNewCfgAclMeterAclBlkBmap.setStatus(_A)
class _AclNewCfgAclMeterAclGrpBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_AclNewCfgAclMeterAclGrpBmap_Type.__name__=_E
_AclNewCfgAclMeterAclGrpBmap_Object=MibTableColumn
aclNewCfgAclMeterAclGrpBmap=_AclNewCfgAclMeterAclGrpBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,4,1,15),_AclNewCfgAclMeterAclGrpBmap_Type())
aclNewCfgAclMeterAclGrpBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:aclNewCfgAclMeterAclGrpBmap.setStatus(_A)
_AclCurCfgPortAclRemarkTable_Object=MibTable
aclCurCfgPortAclRemarkTable=_AclCurCfgPortAclRemarkTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,5))
if mibBuilder.loadTexts:aclCurCfgPortAclRemarkTable.setStatus(_A)
_AclCurCfgPortAclRemarkTableEntry_Object=MibTableRow
aclCurCfgPortAclRemarkTableEntry=_AclCurCfgPortAclRemarkTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,5,1))
aclCurCfgPortAclRemarkTableEntry.setIndexNames((0,_F,_U),(0,_F,_V))
if mibBuilder.loadTexts:aclCurCfgPortAclRemarkTableEntry.setStatus(_A)
_AclCurCfgPortRemarkConfigIndex_Type=Integer32
_AclCurCfgPortRemarkConfigIndex_Object=MibTableColumn
aclCurCfgPortRemarkConfigIndex=_AclCurCfgPortRemarkConfigIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,5,1,1),_AclCurCfgPortRemarkConfigIndex_Type())
aclCurCfgPortRemarkConfigIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:aclCurCfgPortRemarkConfigIndex.setStatus(_A)
_AclCurCfgAclRemarkIndex_Type=Integer32
_AclCurCfgAclRemarkIndex_Object=MibTableColumn
aclCurCfgAclRemarkIndex=_AclCurCfgAclRemarkIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,5,1,2),_AclCurCfgAclRemarkIndex_Type())
aclCurCfgAclRemarkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:aclCurCfgAclRemarkIndex.setStatus(_A)
class _AclCurCfgAclRemarkInProfUpdatePri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AclCurCfgAclRemarkInProfUpdatePri_Type.__name__=_D
_AclCurCfgAclRemarkInProfUpdatePri_Object=MibTableColumn
aclCurCfgAclRemarkInProfUpdatePri=_AclCurCfgAclRemarkInProfUpdatePri_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,5,1,3),_AclCurCfgAclRemarkInProfUpdatePri_Type())
aclCurCfgAclRemarkInProfUpdatePri.setMaxAccess(_B)
if mibBuilder.loadTexts:aclCurCfgAclRemarkInProfUpdatePri.setStatus(_A)
class _AclCurCfgAclRemarkInProfUpdateTosPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AclCurCfgAclRemarkInProfUpdateTosPrec_Type.__name__=_D
_AclCurCfgAclRemarkInProfUpdateTosPrec_Object=MibTableColumn
aclCurCfgAclRemarkInProfUpdateTosPrec=_AclCurCfgAclRemarkInProfUpdateTosPrec_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,5,1,4),_AclCurCfgAclRemarkInProfUpdateTosPrec_Type())
aclCurCfgAclRemarkInProfUpdateTosPrec.setMaxAccess(_B)
if mibBuilder.loadTexts:aclCurCfgAclRemarkInProfUpdateTosPrec.setStatus(_A)
class _AclCurCfgAclRemarkInProfUpdateDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AclCurCfgAclRemarkInProfUpdateDscp_Type.__name__=_D
_AclCurCfgAclRemarkInProfUpdateDscp_Object=MibTableColumn
aclCurCfgAclRemarkInProfUpdateDscp=_AclCurCfgAclRemarkInProfUpdateDscp_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,5,1,5),_AclCurCfgAclRemarkInProfUpdateDscp_Type())
aclCurCfgAclRemarkInProfUpdateDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:aclCurCfgAclRemarkInProfUpdateDscp.setStatus(_A)
class _AclCurCfgAclRemarkOutProfUpdateDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AclCurCfgAclRemarkOutProfUpdateDscp_Type.__name__=_D
_AclCurCfgAclRemarkOutProfUpdateDscp_Object=MibTableColumn
aclCurCfgAclRemarkOutProfUpdateDscp=_AclCurCfgAclRemarkOutProfUpdateDscp_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,5,1,6),_AclCurCfgAclRemarkOutProfUpdateDscp_Type())
aclCurCfgAclRemarkOutProfUpdateDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:aclCurCfgAclRemarkOutProfUpdateDscp.setStatus(_A)
class _AclCurCfgAclRemarkAclBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_AclCurCfgAclRemarkAclBmap_Type.__name__=_E
_AclCurCfgAclRemarkAclBmap_Object=MibTableColumn
aclCurCfgAclRemarkAclBmap=_AclCurCfgAclRemarkAclBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,5,1,7),_AclCurCfgAclRemarkAclBmap_Type())
aclCurCfgAclRemarkAclBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:aclCurCfgAclRemarkAclBmap.setStatus(_A)
class _AclCurCfgAclRemarkAclBlkBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_AclCurCfgAclRemarkAclBlkBmap_Type.__name__=_E
_AclCurCfgAclRemarkAclBlkBmap_Object=MibTableColumn
aclCurCfgAclRemarkAclBlkBmap=_AclCurCfgAclRemarkAclBlkBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,5,1,8),_AclCurCfgAclRemarkAclBlkBmap_Type())
aclCurCfgAclRemarkAclBlkBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:aclCurCfgAclRemarkAclBlkBmap.setStatus(_A)
class _AclCurCfgAclRemarkAclGrpBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_AclCurCfgAclRemarkAclGrpBmap_Type.__name__=_E
_AclCurCfgAclRemarkAclGrpBmap_Object=MibTableColumn
aclCurCfgAclRemarkAclGrpBmap=_AclCurCfgAclRemarkAclGrpBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,5,1,9),_AclCurCfgAclRemarkAclGrpBmap_Type())
aclCurCfgAclRemarkAclGrpBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:aclCurCfgAclRemarkAclGrpBmap.setStatus(_A)
_AclNewCfgPortAclRemarkTable_Object=MibTable
aclNewCfgPortAclRemarkTable=_AclNewCfgPortAclRemarkTable_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,6))
if mibBuilder.loadTexts:aclNewCfgPortAclRemarkTable.setStatus(_A)
_AclNewCfgPortAclRemarkTableEntry_Object=MibTableRow
aclNewCfgPortAclRemarkTableEntry=_AclNewCfgPortAclRemarkTableEntry_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,6,1))
aclNewCfgPortAclRemarkTableEntry.setIndexNames((0,_F,_W),(0,_F,_X))
if mibBuilder.loadTexts:aclNewCfgPortAclRemarkTableEntry.setStatus(_A)
_AclNewCfgPortRemarkConfigIndex_Type=Integer32
_AclNewCfgPortRemarkConfigIndex_Object=MibTableColumn
aclNewCfgPortRemarkConfigIndex=_AclNewCfgPortRemarkConfigIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,6,1,1),_AclNewCfgPortRemarkConfigIndex_Type())
aclNewCfgPortRemarkConfigIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:aclNewCfgPortRemarkConfigIndex.setStatus(_A)
_AclNewCfgAclRemarkIndex_Type=Integer32
_AclNewCfgAclRemarkIndex_Object=MibTableColumn
aclNewCfgAclRemarkIndex=_AclNewCfgAclRemarkIndex_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,6,1,2),_AclNewCfgAclRemarkIndex_Type())
aclNewCfgAclRemarkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:aclNewCfgAclRemarkIndex.setStatus(_A)
class _AclNewCfgAclRemarkInProfUpdatePri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AclNewCfgAclRemarkInProfUpdatePri_Type.__name__=_D
_AclNewCfgAclRemarkInProfUpdatePri_Object=MibTableColumn
aclNewCfgAclRemarkInProfUpdatePri=_AclNewCfgAclRemarkInProfUpdatePri_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,6,1,3),_AclNewCfgAclRemarkInProfUpdatePri_Type())
aclNewCfgAclRemarkInProfUpdatePri.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgAclRemarkInProfUpdatePri.setStatus(_A)
class _AclNewCfgAclRemarkInProfUpdateTosPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AclNewCfgAclRemarkInProfUpdateTosPrec_Type.__name__=_D
_AclNewCfgAclRemarkInProfUpdateTosPrec_Object=MibTableColumn
aclNewCfgAclRemarkInProfUpdateTosPrec=_AclNewCfgAclRemarkInProfUpdateTosPrec_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,6,1,4),_AclNewCfgAclRemarkInProfUpdateTosPrec_Type())
aclNewCfgAclRemarkInProfUpdateTosPrec.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgAclRemarkInProfUpdateTosPrec.setStatus(_A)
class _AclNewCfgAclRemarkInProfUpdateDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AclNewCfgAclRemarkInProfUpdateDscp_Type.__name__=_D
_AclNewCfgAclRemarkInProfUpdateDscp_Object=MibTableColumn
aclNewCfgAclRemarkInProfUpdateDscp=_AclNewCfgAclRemarkInProfUpdateDscp_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,6,1,5),_AclNewCfgAclRemarkInProfUpdateDscp_Type())
aclNewCfgAclRemarkInProfUpdateDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgAclRemarkInProfUpdateDscp.setStatus(_A)
class _AclNewCfgAclRemarkOutProfUpdateDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AclNewCfgAclRemarkOutProfUpdateDscp_Type.__name__=_D
_AclNewCfgAclRemarkOutProfUpdateDscp_Object=MibTableColumn
aclNewCfgAclRemarkOutProfUpdateDscp=_AclNewCfgAclRemarkOutProfUpdateDscp_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,6,1,6),_AclNewCfgAclRemarkOutProfUpdateDscp_Type())
aclNewCfgAclRemarkOutProfUpdateDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgAclRemarkOutProfUpdateDscp.setStatus(_A)
_AclNewCfgAclRemarkAssignAcl_Type=Unsigned32
_AclNewCfgAclRemarkAssignAcl_Object=MibTableColumn
aclNewCfgAclRemarkAssignAcl=_AclNewCfgAclRemarkAssignAcl_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,6,1,7),_AclNewCfgAclRemarkAssignAcl_Type())
aclNewCfgAclRemarkAssignAcl.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgAclRemarkAssignAcl.setStatus(_A)
_AclNewCfgAclRemarkAssignAclBlk_Type=Unsigned32
_AclNewCfgAclRemarkAssignAclBlk_Object=MibTableColumn
aclNewCfgAclRemarkAssignAclBlk=_AclNewCfgAclRemarkAssignAclBlk_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,6,1,8),_AclNewCfgAclRemarkAssignAclBlk_Type())
aclNewCfgAclRemarkAssignAclBlk.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgAclRemarkAssignAclBlk.setStatus(_A)
_AclNewCfgAclRemarkAssignAclGrp_Type=Unsigned32
_AclNewCfgAclRemarkAssignAclGrp_Object=MibTableColumn
aclNewCfgAclRemarkAssignAclGrp=_AclNewCfgAclRemarkAssignAclGrp_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,6,1,9),_AclNewCfgAclRemarkAssignAclGrp_Type())
aclNewCfgAclRemarkAssignAclGrp.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgAclRemarkAssignAclGrp.setStatus(_A)
_AclNewCfgAclRemarkUnAssignAcl_Type=Unsigned32
_AclNewCfgAclRemarkUnAssignAcl_Object=MibTableColumn
aclNewCfgAclRemarkUnAssignAcl=_AclNewCfgAclRemarkUnAssignAcl_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,6,1,10),_AclNewCfgAclRemarkUnAssignAcl_Type())
aclNewCfgAclRemarkUnAssignAcl.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgAclRemarkUnAssignAcl.setStatus(_A)
_AclNewCfgAclRemarkUnAssignAclBlk_Type=Unsigned32
_AclNewCfgAclRemarkUnAssignAclBlk_Object=MibTableColumn
aclNewCfgAclRemarkUnAssignAclBlk=_AclNewCfgAclRemarkUnAssignAclBlk_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,6,1,11),_AclNewCfgAclRemarkUnAssignAclBlk_Type())
aclNewCfgAclRemarkUnAssignAclBlk.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgAclRemarkUnAssignAclBlk.setStatus(_A)
_AclNewCfgAclRemarkUnAssignAclGrp_Type=Unsigned32
_AclNewCfgAclRemarkUnAssignAclGrp_Object=MibTableColumn
aclNewCfgAclRemarkUnAssignAclGrp=_AclNewCfgAclRemarkUnAssignAclGrp_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,6,1,12),_AclNewCfgAclRemarkUnAssignAclGrp_Type())
aclNewCfgAclRemarkUnAssignAclGrp.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgAclRemarkUnAssignAclGrp.setStatus(_A)
class _AclNewCfgAclRemarkAclBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_AclNewCfgAclRemarkAclBmap_Type.__name__=_E
_AclNewCfgAclRemarkAclBmap_Object=MibTableColumn
aclNewCfgAclRemarkAclBmap=_AclNewCfgAclRemarkAclBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,6,1,13),_AclNewCfgAclRemarkAclBmap_Type())
aclNewCfgAclRemarkAclBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:aclNewCfgAclRemarkAclBmap.setStatus(_A)
class _AclNewCfgAclRemarkAclBlkBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_AclNewCfgAclRemarkAclBlkBmap_Type.__name__=_E
_AclNewCfgAclRemarkAclBlkBmap_Object=MibTableColumn
aclNewCfgAclRemarkAclBlkBmap=_AclNewCfgAclRemarkAclBlkBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,6,1,14),_AclNewCfgAclRemarkAclBlkBmap_Type())
aclNewCfgAclRemarkAclBlkBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:aclNewCfgAclRemarkAclBlkBmap.setStatus(_A)
class _AclNewCfgAclRemarkAclGrpBmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_AclNewCfgAclRemarkAclGrpBmap_Type.__name__=_E
_AclNewCfgAclRemarkAclGrpBmap_Object=MibTableColumn
aclNewCfgAclRemarkAclGrpBmap=_AclNewCfgAclRemarkAclGrpBmap_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,6,1,15),_AclNewCfgAclRemarkAclGrpBmap_Type())
aclNewCfgAclRemarkAclGrpBmap.setMaxAccess(_B)
if mibBuilder.loadTexts:aclNewCfgAclRemarkAclGrpBmap.setStatus(_A)
class _AclNewCfgAclRemarkReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('reset',2)))
_AclNewCfgAclRemarkReset_Type.__name__=_D
_AclNewCfgAclRemarkReset_Object=MibTableColumn
aclNewCfgAclRemarkReset=_AclNewCfgAclRemarkReset_Object((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,1,2,6,1,16),_AclNewCfgAclRemarkReset_Type())
aclNewCfgAclRemarkReset.setMaxAccess(_C)
if mibBuilder.loadTexts:aclNewCfgAclRemarkReset.setStatus(_A)
_QosStats_ObjectIdentity=ObjectIdentity
qosStats=_QosStats_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,2))
_QosInfo_ObjectIdentity=ObjectIdentity
qosInfo=_QosInfo_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,3))
_QosOper_ObjectIdentity=ObjectIdentity
qosOper=_QosOper_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,33,1,2,8,4))
mibBuilder.exportSymbols(_F,**{'qos':qos,'qosConfigs':qosConfigs,'qos8021p':qos8021p,'qosCurCfgPortPriorityTable':qosCurCfgPortPriorityTable,'qosCurCfgPortPriorityEntry':qosCurCfgPortPriorityEntry,_I:qosCurCfgPortIndex,'qosCurCfgPortPriority':qosCurCfgPortPriority,'qosNewCfgPortPriorityTable':qosNewCfgPortPriorityTable,'qosNewCfgPortPriorityEntry':qosNewCfgPortPriorityEntry,_J:qosNewCfgPortIndex,'qosNewCfgPortPriority':qosNewCfgPortPriority,'qosCurCfgPriorityCoSTable':qosCurCfgPriorityCoSTable,'qosCurCfgPriorityCoSEntry':qosCurCfgPriorityCoSEntry,_K:qosCurCfgPriorityIndex,'qosCurCfgPriorityCoSq':qosCurCfgPriorityCoSq,'qosNewCfgPriorityCoSTable':qosNewCfgPriorityCoSTable,'qosNewCfgPriorityCoSEntry':qosNewCfgPriorityCoSEntry,_L:qosNewCfgPriorityIndex,'qosNewCfgPriorityCoSq':qosNewCfgPriorityCoSq,'qosCurCfgCosWeightTable':qosCurCfgCosWeightTable,'qosCurCfgCosWeightEntry':qosCurCfgCosWeightEntry,_M:qosCurCfgCosIndex,'qosCurCfgCosWeight':qosCurCfgCosWeight,'qosNewCfgCosWeightTable':qosNewCfgCosWeightTable,'qosNewCfgCosWeightEntry':qosNewCfgCosWeightEntry,_N:qosNewCfgCosIndex,'qosNewCfgCosWeight':qosNewCfgCosWeight,'qosCurCfgCosNum':qosCurCfgCosNum,'qosNewCfgCosNum':qosNewCfgCosNum,'aclCfg':aclCfg,'aclCurCfgPortTable':aclCurCfgPortTable,'aclCurCfgPortTableEntry':aclCurCfgPortTableEntry,_O:aclCurCfgPortIndex,'aclCurCfgPortAclBmap':aclCurCfgPortAclBmap,'aclCurCfgPortAclBlkBmap':aclCurCfgPortAclBlkBmap,'aclCurCfgPortAclGrpBmap':aclCurCfgPortAclGrpBmap,'aclNewCfgPortTable':aclNewCfgPortTable,'aclNewCfgPortTableEntry':aclNewCfgPortTableEntry,_P:aclNewCfgPortIndex,'aclNewCfgPortAddAcl':aclNewCfgPortAddAcl,'aclNewCfgPortAddAclBlk':aclNewCfgPortAddAclBlk,'aclNewCfgPortAddAclGrp':aclNewCfgPortAddAclGrp,'aclNewCfgPortRemoveAcl':aclNewCfgPortRemoveAcl,'aclNewCfgPortRemoveAclBlk':aclNewCfgPortRemoveAclBlk,'aclNewCfgPortRemoveAclGrp':aclNewCfgPortRemoveAclGrp,'aclNewCfgPortAclBmap':aclNewCfgPortAclBmap,'aclNewCfgPortAclBlkBmap':aclNewCfgPortAclBlkBmap,'aclNewCfgPortAclGrpBmap':aclNewCfgPortAclGrpBmap,'aclCurCfgPortAclMeterTable':aclCurCfgPortAclMeterTable,'aclCurCfgPortAclMeterTableEntry':aclCurCfgPortAclMeterTableEntry,_Q:aclCurCfgPortMeterConfigIndex,_R:aclCurCfgAclMeterIndex,'aclCurCfgAclMeterCommitRate':aclCurCfgAclMeterCommitRate,'aclCurCfgAclMeterMaxBurstSize':aclCurCfgAclMeterMaxBurstSize,'aclCurCfgAclMeterStatus':aclCurCfgAclMeterStatus,'aclCurCfgAclMeterDropOrPass':aclCurCfgAclMeterDropOrPass,'aclCurCfgAclMeterAclBmap':aclCurCfgAclMeterAclBmap,'aclCurCfgAclMeterAclBlkBmap':aclCurCfgAclMeterAclBlkBmap,'aclCurCfgAclMeterAclGrpBmap':aclCurCfgAclMeterAclGrpBmap,'aclNewCfgPortAclMeterTable':aclNewCfgPortAclMeterTable,'aclNewCfgPortAclMeterTableEntry':aclNewCfgPortAclMeterTableEntry,_S:aclNewCfgPortMeterConfigIndex,_T:aclNewCfgAclMeterIndex,'aclNewCfgAclMeterCommitRate':aclNewCfgAclMeterCommitRate,'aclNewCfgAclMeterMaxBurstSize':aclNewCfgAclMeterMaxBurstSize,'aclNewCfgAclMeterStatus':aclNewCfgAclMeterStatus,'aclNewCfgAclMeterDropOrPass':aclNewCfgAclMeterDropOrPass,'aclNewCfgAclMeterAssignAcl':aclNewCfgAclMeterAssignAcl,'aclNewCfgAclMeterAssignAclBlk':aclNewCfgAclMeterAssignAclBlk,'aclNewCfgAclMeterAssignAclGrp':aclNewCfgAclMeterAssignAclGrp,'aclNewCfgAclMeterUnAssignAcl':aclNewCfgAclMeterUnAssignAcl,'aclNewCfgAclMeterUnAssignAclBlk':aclNewCfgAclMeterUnAssignAclBlk,'aclNewCfgAclMeterUnAssignAclGrp':aclNewCfgAclMeterUnAssignAclGrp,'aclNewCfgAclMeterAclBmap':aclNewCfgAclMeterAclBmap,'aclNewCfgAclMeterAclBlkBmap':aclNewCfgAclMeterAclBlkBmap,'aclNewCfgAclMeterAclGrpBmap':aclNewCfgAclMeterAclGrpBmap,'aclCurCfgPortAclRemarkTable':aclCurCfgPortAclRemarkTable,'aclCurCfgPortAclRemarkTableEntry':aclCurCfgPortAclRemarkTableEntry,_U:aclCurCfgPortRemarkConfigIndex,_V:aclCurCfgAclRemarkIndex,'aclCurCfgAclRemarkInProfUpdatePri':aclCurCfgAclRemarkInProfUpdatePri,'aclCurCfgAclRemarkInProfUpdateTosPrec':aclCurCfgAclRemarkInProfUpdateTosPrec,'aclCurCfgAclRemarkInProfUpdateDscp':aclCurCfgAclRemarkInProfUpdateDscp,'aclCurCfgAclRemarkOutProfUpdateDscp':aclCurCfgAclRemarkOutProfUpdateDscp,'aclCurCfgAclRemarkAclBmap':aclCurCfgAclRemarkAclBmap,'aclCurCfgAclRemarkAclBlkBmap':aclCurCfgAclRemarkAclBlkBmap,'aclCurCfgAclRemarkAclGrpBmap':aclCurCfgAclRemarkAclGrpBmap,'aclNewCfgPortAclRemarkTable':aclNewCfgPortAclRemarkTable,'aclNewCfgPortAclRemarkTableEntry':aclNewCfgPortAclRemarkTableEntry,_W:aclNewCfgPortRemarkConfigIndex,_X:aclNewCfgAclRemarkIndex,'aclNewCfgAclRemarkInProfUpdatePri':aclNewCfgAclRemarkInProfUpdatePri,'aclNewCfgAclRemarkInProfUpdateTosPrec':aclNewCfgAclRemarkInProfUpdateTosPrec,'aclNewCfgAclRemarkInProfUpdateDscp':aclNewCfgAclRemarkInProfUpdateDscp,'aclNewCfgAclRemarkOutProfUpdateDscp':aclNewCfgAclRemarkOutProfUpdateDscp,'aclNewCfgAclRemarkAssignAcl':aclNewCfgAclRemarkAssignAcl,'aclNewCfgAclRemarkAssignAclBlk':aclNewCfgAclRemarkAssignAclBlk,'aclNewCfgAclRemarkAssignAclGrp':aclNewCfgAclRemarkAssignAclGrp,'aclNewCfgAclRemarkUnAssignAcl':aclNewCfgAclRemarkUnAssignAcl,'aclNewCfgAclRemarkUnAssignAclBlk':aclNewCfgAclRemarkUnAssignAclBlk,'aclNewCfgAclRemarkUnAssignAclGrp':aclNewCfgAclRemarkUnAssignAclGrp,'aclNewCfgAclRemarkAclBmap':aclNewCfgAclRemarkAclBmap,'aclNewCfgAclRemarkAclBlkBmap':aclNewCfgAclRemarkAclBlkBmap,'aclNewCfgAclRemarkAclGrpBmap':aclNewCfgAclRemarkAclGrpBmap,'aclNewCfgAclRemarkReset':aclNewCfgAclRemarkReset,'qosStats':qosStats,'qosInfo':qosInfo,'qosOper':qosOper})