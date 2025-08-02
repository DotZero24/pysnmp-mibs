_e='qosOutputCirIndex'
_d='qosInputCirIndex'
_c='qosREDCfgPreValue'
_b='Kilobits/second'
_a='qosCbQosCMAPMatchIndex'
_Z='qosPriorityQueueItemIndex'
_Y='set-exp-transmit'
_X='set-dscp-transmit'
_W='set-prec-transmit'
_V='transmit'
_U='DisplayString'
_T='qosPriorityQueueIndex'
_S='match-address-MAc'
_R='match-qos-group'
_Q='match-vlanId'
_P='match-802dot1p'
_O='match-mpls-exp'
_N='match-dscp'
_M='match-precedence'
_L='match-acl'
_K='qoscbQosPMapIndex'
_J='Integer32'
_I='qoscbQosCMapIndex'
_H='read-write'
_G='Gauge32'
_F='ifIndex'
_E='IF-MIB'
_D='ZXR10-QOS-MIB'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_G,_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_U,'PhysAddress','TextualConvention')
zxr10qos=ModuleIdentity((1,3,6,1,4,1,3902,3,101,6))
class DisplayString(OctetString):0
class QosCirMatchType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6,7,8,9,36,37)));namedValues=NamedValues(*(('match-localport',3),(_L,4),(_M,5),(_N,6),(_O,7),(_P,8),(_Q,9),(_R,36),(_S,37)))
class QosCirAction(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,9,10)));namedValues=NamedValues(*(('drop',0),('continue',1),(_V,2),('set-prec-continue',3),(_W,4),('set-dscp-continue',5),(_X,6),('set-exp-continue',9),(_Y,10)))
class QosCBQCarAction(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,4,6,10)));namedValues=NamedValues(*(('drop',0),(_V,2),(_W,4),(_X,6),(_Y,10)))
class QosPQMatchType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5,6,7,8,9,36,37)));namedValues=NamedValues(*(('match-default',1),('match-interface',3),(_L,4),(_M,5),(_N,6),(_O,7),(_P,8),(_Q,9),(_R,36),(_S,37)))
class QosPQQueueType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('high',0),('medium',1),('normal',2),('low',3)))
class QosCMAPMatchType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,5,6,7,8,9,19,21,36,37)));namedValues=NamedValues(*(('match-not',1),(_L,4),(_M,5),(_N,6),(_O,7),(_P,8),(_Q,9),('match-any',19),('match-classmap',21),(_R,36),(_S,37)))
class TrafficDirection(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('output',2))
class QueueingBandwidthUnits(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('percentage',1),('kbps',2)))
class EntryStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('valid',1),('createRequest',2),('underCreation',3),('invalid',4)))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_Zxr10_ObjectIdentity=ObjectIdentity
zxr10=_Zxr10_ObjectIdentity((1,3,6,1,4,1,3902,3))
_Zxr10protocol_ObjectIdentity=ObjectIdentity
zxr10protocol=_Zxr10protocol_ObjectIdentity((1,3,6,1,4,1,3902,3,101))
_QosModuleStart_Type=Integer32
_QosModuleStart_Object=MibScalar
qosModuleStart=_QosModuleStart_Object((1,3,6,1,4,1,3902,3,101,6,1),_QosModuleStart_Type())
qosModuleStart.setMaxAccess(_H)
if mibBuilder.loadTexts:qosModuleStart.setStatus(_A)
_QosPQconfig_ObjectIdentity=ObjectIdentity
qosPQconfig=_QosPQconfig_ObjectIdentity((1,3,6,1,4,1,3902,3,101,6,2))
_QosPriorityQueueCfgTable_Object=MibTable
qosPriorityQueueCfgTable=_QosPriorityQueueCfgTable_Object((1,3,6,1,4,1,3902,3,101,6,2,1))
if mibBuilder.loadTexts:qosPriorityQueueCfgTable.setStatus(_A)
_QosPriorityQueueCfgEntry_Object=MibTableRow
qosPriorityQueueCfgEntry=_QosPriorityQueueCfgEntry_Object((1,3,6,1,4,1,3902,3,101,6,2,1,1))
qosPriorityQueueCfgEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:qosPriorityQueueCfgEntry.setStatus(_A)
_QosPriorityQueueIndex_Type=Integer32
_QosPriorityQueueIndex_Object=MibTableColumn
qosPriorityQueueIndex=_QosPriorityQueueIndex_Object((1,3,6,1,4,1,3902,3,101,6,2,1,1,1),_QosPriorityQueueIndex_Type())
qosPriorityQueueIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPriorityQueueIndex.setStatus(_A)
class _QosPriorityQueueItemTotal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_QosPriorityQueueItemTotal_Type.__name__=_J
_QosPriorityQueueItemTotal_Object=MibTableColumn
qosPriorityQueueItemTotal=_QosPriorityQueueItemTotal_Object((1,3,6,1,4,1,3902,3,101,6,2,1,1,2),_QosPriorityQueueItemTotal_Type())
qosPriorityQueueItemTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPriorityQueueItemTotal.setStatus(_A)
_QosPriorityQueueDefault_Type=QosPQQueueType
_QosPriorityQueueDefault_Object=MibTableColumn
qosPriorityQueueDefault=_QosPriorityQueueDefault_Object((1,3,6,1,4,1,3902,3,101,6,2,1,1,3),_QosPriorityQueueDefault_Type())
qosPriorityQueueDefault.setMaxAccess(_H)
if mibBuilder.loadTexts:qosPriorityQueueDefault.setStatus(_A)
_QosPriorityQueueLimitHigh_Type=Integer32
_QosPriorityQueueLimitHigh_Object=MibTableColumn
qosPriorityQueueLimitHigh=_QosPriorityQueueLimitHigh_Object((1,3,6,1,4,1,3902,3,101,6,2,1,1,4),_QosPriorityQueueLimitHigh_Type())
qosPriorityQueueLimitHigh.setMaxAccess(_H)
if mibBuilder.loadTexts:qosPriorityQueueLimitHigh.setStatus(_A)
_QosPriorityQueueLimitMedium_Type=Integer32
_QosPriorityQueueLimitMedium_Object=MibTableColumn
qosPriorityQueueLimitMedium=_QosPriorityQueueLimitMedium_Object((1,3,6,1,4,1,3902,3,101,6,2,1,1,5),_QosPriorityQueueLimitMedium_Type())
qosPriorityQueueLimitMedium.setMaxAccess(_H)
if mibBuilder.loadTexts:qosPriorityQueueLimitMedium.setStatus(_A)
_QosPriorityQueueLimitNormal_Type=Integer32
_QosPriorityQueueLimitNormal_Object=MibTableColumn
qosPriorityQueueLimitNormal=_QosPriorityQueueLimitNormal_Object((1,3,6,1,4,1,3902,3,101,6,2,1,1,6),_QosPriorityQueueLimitNormal_Type())
qosPriorityQueueLimitNormal.setMaxAccess(_H)
if mibBuilder.loadTexts:qosPriorityQueueLimitNormal.setStatus(_A)
_QosPriorityQueueLimitLow_Type=Integer32
_QosPriorityQueueLimitLow_Object=MibTableColumn
qosPriorityQueueLimitLow=_QosPriorityQueueLimitLow_Object((1,3,6,1,4,1,3902,3,101,6,2,1,1,7),_QosPriorityQueueLimitLow_Type())
qosPriorityQueueLimitLow.setMaxAccess(_H)
if mibBuilder.loadTexts:qosPriorityQueueLimitLow.setStatus(_A)
_QosPriorityQueueRowStatus_Type=EntryStatus
_QosPriorityQueueRowStatus_Object=MibTableColumn
qosPriorityQueueRowStatus=_QosPriorityQueueRowStatus_Object((1,3,6,1,4,1,3902,3,101,6,2,1,1,8),_QosPriorityQueueRowStatus_Type())
qosPriorityQueueRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:qosPriorityQueueRowStatus.setStatus(_A)
_QosPriorityQueueCfgTableLastchange_Type=TimeTicks
_QosPriorityQueueCfgTableLastchange_Object=MibScalar
qosPriorityQueueCfgTableLastchange=_QosPriorityQueueCfgTableLastchange_Object((1,3,6,1,4,1,3902,3,101,6,2,2),_QosPriorityQueueCfgTableLastchange_Type())
qosPriorityQueueCfgTableLastchange.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPriorityQueueCfgTableLastchange.setStatus(_A)
_QosPriorityQueueItemTable_Object=MibTable
qosPriorityQueueItemTable=_QosPriorityQueueItemTable_Object((1,3,6,1,4,1,3902,3,101,6,2,3))
if mibBuilder.loadTexts:qosPriorityQueueItemTable.setStatus(_A)
_QosPriorityQueueItemEntry_Object=MibTableRow
qosPriorityQueueItemEntry=_QosPriorityQueueItemEntry_Object((1,3,6,1,4,1,3902,3,101,6,2,3,1))
qosPriorityQueueItemEntry.setIndexNames((0,_D,_T),(0,_D,_Z))
if mibBuilder.loadTexts:qosPriorityQueueItemEntry.setStatus(_A)
_QosPriorityQueueItemIndex_Type=Integer32
_QosPriorityQueueItemIndex_Object=MibTableColumn
qosPriorityQueueItemIndex=_QosPriorityQueueItemIndex_Object((1,3,6,1,4,1,3902,3,101,6,2,3,1,1),_QosPriorityQueueItemIndex_Type())
qosPriorityQueueItemIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPriorityQueueItemIndex.setStatus(_A)
_QosPriorityQueueItemMatchType_Type=QosPQMatchType
_QosPriorityQueueItemMatchType_Object=MibTableColumn
qosPriorityQueueItemMatchType=_QosPriorityQueueItemMatchType_Object((1,3,6,1,4,1,3902,3,101,6,2,3,1,2),_QosPriorityQueueItemMatchType_Type())
qosPriorityQueueItemMatchType.setMaxAccess(_B)
if mibBuilder.loadTexts:qosPriorityQueueItemMatchType.setStatus(_A)
_QosPriorityQueueItemMatchValue_Type=DisplayString
_QosPriorityQueueItemMatchValue_Object=MibTableColumn
qosPriorityQueueItemMatchValue=_QosPriorityQueueItemMatchValue_Object((1,3,6,1,4,1,3902,3,101,6,2,3,1,3),_QosPriorityQueueItemMatchValue_Type())
qosPriorityQueueItemMatchValue.setMaxAccess(_B)
if mibBuilder.loadTexts:qosPriorityQueueItemMatchValue.setStatus(_A)
_QosPriorityQueueItemQueueNum_Type=QosPQQueueType
_QosPriorityQueueItemQueueNum_Object=MibTableColumn
qosPriorityQueueItemQueueNum=_QosPriorityQueueItemQueueNum_Object((1,3,6,1,4,1,3902,3,101,6,2,3,1,4),_QosPriorityQueueItemQueueNum_Type())
qosPriorityQueueItemQueueNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qosPriorityQueueItemQueueNum.setStatus(_A)
_QosPriorityQueueItemRowStatus_Type=EntryStatus
_QosPriorityQueueItemRowStatus_Object=MibTableColumn
qosPriorityQueueItemRowStatus=_QosPriorityQueueItemRowStatus_Object((1,3,6,1,4,1,3902,3,101,6,2,3,1,5),_QosPriorityQueueItemRowStatus_Type())
qosPriorityQueueItemRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qosPriorityQueueItemRowStatus.setStatus(_A)
_QosPriorityQueueItemDescription_Type=DisplayString
_QosPriorityQueueItemDescription_Object=MibTableColumn
qosPriorityQueueItemDescription=_QosPriorityQueueItemDescription_Object((1,3,6,1,4,1,3902,3,101,6,2,3,1,6),_QosPriorityQueueItemDescription_Type())
qosPriorityQueueItemDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:qosPriorityQueueItemDescription.setStatus(_A)
_QosPriorityGroupTable_Object=MibTable
qosPriorityGroupTable=_QosPriorityGroupTable_Object((1,3,6,1,4,1,3902,3,101,6,2,4))
if mibBuilder.loadTexts:qosPriorityGroupTable.setStatus(_A)
_QosPriorityGroupEntry_Object=MibTableRow
qosPriorityGroupEntry=_QosPriorityGroupEntry_Object((1,3,6,1,4,1,3902,3,101,6,2,4,1))
qosPriorityGroupEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:qosPriorityGroupEntry.setStatus(_A)
_QosPriorityGroupifname_Type=DisplayString
_QosPriorityGroupifname_Object=MibTableColumn
qosPriorityGroupifname=_QosPriorityGroupifname_Object((1,3,6,1,4,1,3902,3,101,6,2,4,1,1),_QosPriorityGroupifname_Type())
qosPriorityGroupifname.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPriorityGroupifname.setStatus(_A)
_QosPriorityGroupNum_Type=Integer32
_QosPriorityGroupNum_Object=MibTableColumn
qosPriorityGroupNum=_QosPriorityGroupNum_Object((1,3,6,1,4,1,3902,3,101,6,2,4,1,2),_QosPriorityGroupNum_Type())
qosPriorityGroupNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qosPriorityGroupNum.setStatus(_A)
_QosPriorityGroupRowStatus_Type=EntryStatus
_QosPriorityGroupRowStatus_Object=MibTableColumn
qosPriorityGroupRowStatus=_QosPriorityGroupRowStatus_Object((1,3,6,1,4,1,3902,3,101,6,2,4,1,3),_QosPriorityGroupRowStatus_Type())
qosPriorityGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qosPriorityGroupRowStatus.setStatus(_A)
_QosCQconfig_ObjectIdentity=ObjectIdentity
qosCQconfig=_QosCQconfig_ObjectIdentity((1,3,6,1,4,1,3902,3,101,6,3))
_QosCBQconfig_ObjectIdentity=ObjectIdentity
qosCBQconfig=_QosCBQconfig_ObjectIdentity((1,3,6,1,4,1,3902,3,101,6,4))
_QosCBQosServicePolicyTable_Object=MibTable
qosCBQosServicePolicyTable=_QosCBQosServicePolicyTable_Object((1,3,6,1,4,1,3902,3,101,6,4,1))
if mibBuilder.loadTexts:qosCBQosServicePolicyTable.setStatus(_A)
_QosCBQosServicePolicyEntry_Object=MibTableRow
qosCBQosServicePolicyEntry=_QosCBQosServicePolicyEntry_Object((1,3,6,1,4,1,3902,3,101,6,4,1,1))
qosCBQosServicePolicyEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:qosCBQosServicePolicyEntry.setStatus(_A)
_QosCbQosPolicyifname_Type=DisplayString
_QosCbQosPolicyifname_Object=MibTableColumn
qosCbQosPolicyifname=_QosCbQosPolicyifname_Object((1,3,6,1,4,1,3902,3,101,6,4,1,1,1),_QosCbQosPolicyifname_Type())
qosCbQosPolicyifname.setMaxAccess(_C)
if mibBuilder.loadTexts:qosCbQosPolicyifname.setStatus(_A)
_QosCbQosPolicyDirection_Type=TrafficDirection
_QosCbQosPolicyDirection_Object=MibTableColumn
qosCbQosPolicyDirection=_QosCbQosPolicyDirection_Object((1,3,6,1,4,1,3902,3,101,6,4,1,1,2),_QosCbQosPolicyDirection_Type())
qosCbQosPolicyDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosPolicyDirection.setStatus(_A)
_QosCbQosServicePolicyName_Type=DisplayString
_QosCbQosServicePolicyName_Object=MibTableColumn
qosCbQosServicePolicyName=_QosCbQosServicePolicyName_Object((1,3,6,1,4,1,3902,3,101,6,4,1,1,3),_QosCbQosServicePolicyName_Type())
qosCbQosServicePolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosServicePolicyName.setStatus(_A)
_QosCbQosServicePolicyRowStatus_Type=EntryStatus
_QosCbQosServicePolicyRowStatus_Object=MibTableColumn
qosCbQosServicePolicyRowStatus=_QosCbQosServicePolicyRowStatus_Object((1,3,6,1,4,1,3902,3,101,6,4,1,1,4),_QosCbQosServicePolicyRowStatus_Type())
qosCbQosServicePolicyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosServicePolicyRowStatus.setStatus(_A)
_QosCbQosPolicyMapCfgTable_Object=MibTable
qosCbQosPolicyMapCfgTable=_QosCbQosPolicyMapCfgTable_Object((1,3,6,1,4,1,3902,3,101,6,4,2))
if mibBuilder.loadTexts:qosCbQosPolicyMapCfgTable.setStatus(_A)
_QosCbQosPolicyMapCfgEntry_Object=MibTableRow
qosCbQosPolicyMapCfgEntry=_QosCbQosPolicyMapCfgEntry_Object((1,3,6,1,4,1,3902,3,101,6,4,2,1))
qosCbQosPolicyMapCfgEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:qosCbQosPolicyMapCfgEntry.setStatus(_A)
_QoscbQosPMapIndex_Type=Integer32
_QoscbQosPMapIndex_Object=MibTableColumn
qoscbQosPMapIndex=_QoscbQosPMapIndex_Object((1,3,6,1,4,1,3902,3,101,6,4,2,1,1),_QoscbQosPMapIndex_Type())
qoscbQosPMapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qoscbQosPMapIndex.setStatus(_A)
_QoscbQosPolicyMapName_Type=DisplayString
_QoscbQosPolicyMapName_Object=MibTableColumn
qoscbQosPolicyMapName=_QoscbQosPolicyMapName_Object((1,3,6,1,4,1,3902,3,101,6,4,2,1,2),_QoscbQosPolicyMapName_Type())
qoscbQosPolicyMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:qoscbQosPolicyMapName.setStatus(_A)
_QosCbQosPolicyMapRowStatus_Type=EntryStatus
_QosCbQosPolicyMapRowStatus_Object=MibTableColumn
qosCbQosPolicyMapRowStatus=_QosCbQosPolicyMapRowStatus_Object((1,3,6,1,4,1,3902,3,101,6,4,2,1,3),_QosCbQosPolicyMapRowStatus_Type())
qosCbQosPolicyMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosPolicyMapRowStatus.setStatus(_A)
_QoscbQosPolicyMapDescription_Type=DisplayString
_QoscbQosPolicyMapDescription_Object=MibTableColumn
qoscbQosPolicyMapDescription=_QoscbQosPolicyMapDescription_Object((1,3,6,1,4,1,3902,3,101,6,4,2,1,4),_QoscbQosPolicyMapDescription_Type())
qoscbQosPolicyMapDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:qoscbQosPolicyMapDescription.setStatus(_A)
_QosCbQosClassMapCfgTable_Object=MibTable
qosCbQosClassMapCfgTable=_QosCbQosClassMapCfgTable_Object((1,3,6,1,4,1,3902,3,101,6,4,3))
if mibBuilder.loadTexts:qosCbQosClassMapCfgTable.setStatus(_A)
_QosCbQosClassMapCfgEntry_Object=MibTableRow
qosCbQosClassMapCfgEntry=_QosCbQosClassMapCfgEntry_Object((1,3,6,1,4,1,3902,3,101,6,4,3,1))
qosCbQosClassMapCfgEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:qosCbQosClassMapCfgEntry.setStatus(_A)
_QoscbQosCMapIndex_Type=Integer32
_QoscbQosCMapIndex_Object=MibTableColumn
qoscbQosCMapIndex=_QoscbQosCMapIndex_Object((1,3,6,1,4,1,3902,3,101,6,4,3,1,1),_QoscbQosCMapIndex_Type())
qoscbQosCMapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qoscbQosCMapIndex.setStatus(_A)
_QosCbQosClassMapName_Type=DisplayString
_QosCbQosClassMapName_Object=MibTableColumn
qosCbQosClassMapName=_QosCbQosClassMapName_Object((1,3,6,1,4,1,3902,3,101,6,4,3,1,2),_QosCbQosClassMapName_Type())
qosCbQosClassMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosClassMapName.setStatus(_A)
_QosCbQosClassMapRowStatus_Type=EntryStatus
_QosCbQosClassMapRowStatus_Object=MibTableColumn
qosCbQosClassMapRowStatus=_QosCbQosClassMapRowStatus_Object((1,3,6,1,4,1,3902,3,101,6,4,3,1,3),_QosCbQosClassMapRowStatus_Type())
qosCbQosClassMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosClassMapRowStatus.setStatus(_A)
_QoscbQosClassMapDescription_Type=DisplayString
_QoscbQosClassMapDescription_Object=MibTableColumn
qoscbQosClassMapDescription=_QoscbQosClassMapDescription_Object((1,3,6,1,4,1,3902,3,101,6,4,3,1,4),_QoscbQosClassMapDescription_Type())
qoscbQosClassMapDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:qoscbQosClassMapDescription.setStatus(_A)
_QosCbQosCMAPMatchCfgTable_Object=MibTable
qosCbQosCMAPMatchCfgTable=_QosCbQosCMAPMatchCfgTable_Object((1,3,6,1,4,1,3902,3,101,6,4,4))
if mibBuilder.loadTexts:qosCbQosCMAPMatchCfgTable.setStatus(_A)
_QosCbQosCMAPMatchCfgEntry_Object=MibTableRow
qosCbQosCMAPMatchCfgEntry=_QosCbQosCMAPMatchCfgEntry_Object((1,3,6,1,4,1,3902,3,101,6,4,4,1))
qosCbQosCMAPMatchCfgEntry.setIndexNames((0,_D,_I),(0,_D,_a))
if mibBuilder.loadTexts:qosCbQosCMAPMatchCfgEntry.setStatus(_A)
_QosCbQosCMAPMatchIndex_Type=Integer32
_QosCbQosCMAPMatchIndex_Object=MibTableColumn
qosCbQosCMAPMatchIndex=_QosCbQosCMAPMatchIndex_Object((1,3,6,1,4,1,3902,3,101,6,4,4,1,1),_QosCbQosCMAPMatchIndex_Type())
qosCbQosCMAPMatchIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosCMAPMatchIndex.setStatus(_A)
_QosCbQosCMAPMatchType_Type=QosCMAPMatchType
_QosCbQosCMAPMatchType_Object=MibTableColumn
qosCbQosCMAPMatchType=_QosCbQosCMAPMatchType_Object((1,3,6,1,4,1,3902,3,101,6,4,4,1,2),_QosCbQosCMAPMatchType_Type())
qosCbQosCMAPMatchType.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosCMAPMatchType.setStatus(_A)
_QosCbQosCMAPMatchValue_Type=DisplayString
_QosCbQosCMAPMatchValue_Object=MibTableColumn
qosCbQosCMAPMatchValue=_QosCbQosCMAPMatchValue_Object((1,3,6,1,4,1,3902,3,101,6,4,4,1,3),_QosCbQosCMAPMatchValue_Type())
qosCbQosCMAPMatchValue.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosCMAPMatchValue.setStatus(_A)
_QosCbQosCMAPMatchRowStatus_Type=EntryStatus
_QosCbQosCMAPMatchRowStatus_Object=MibTableColumn
qosCbQosCMAPMatchRowStatus=_QosCbQosCMAPMatchRowStatus_Object((1,3,6,1,4,1,3902,3,101,6,4,4,1,4),_QosCbQosCMAPMatchRowStatus_Type())
qosCbQosCMAPMatchRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosCMAPMatchRowStatus.setStatus(_A)
_QosCbQosPolicyClassCfgTable_Object=MibTable
qosCbQosPolicyClassCfgTable=_QosCbQosPolicyClassCfgTable_Object((1,3,6,1,4,1,3902,3,101,6,4,5))
if mibBuilder.loadTexts:qosCbQosPolicyClassCfgTable.setStatus(_A)
_QosCbQosPolicyClassCfgEntry_Object=MibTableRow
qosCbQosPolicyClassCfgEntry=_QosCbQosPolicyClassCfgEntry_Object((1,3,6,1,4,1,3902,3,101,6,4,5,1))
qosCbQosPolicyClassCfgEntry.setIndexNames((0,_D,_K),(0,_D,_I))
if mibBuilder.loadTexts:qosCbQosPolicyClassCfgEntry.setStatus(_A)
_QosCbQosPolicyClassName_Type=DisplayString
_QosCbQosPolicyClassName_Object=MibTableColumn
qosCbQosPolicyClassName=_QosCbQosPolicyClassName_Object((1,3,6,1,4,1,3902,3,101,6,4,5,1,1),_QosCbQosPolicyClassName_Type())
qosCbQosPolicyClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosPolicyClassName.setStatus(_A)
_QosCbQosPolicyClassRowStatus_Type=EntryStatus
_QosCbQosPolicyClassRowStatus_Object=MibTableColumn
qosCbQosPolicyClassRowStatus=_QosCbQosPolicyClassRowStatus_Object((1,3,6,1,4,1,3902,3,101,6,4,5,1,2),_QosCbQosPolicyClassRowStatus_Type())
qosCbQosPolicyClassRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosPolicyClassRowStatus.setStatus(_A)
_QosCbQosqueueCfgTable_Object=MibTable
qosCbQosqueueCfgTable=_QosCbQosqueueCfgTable_Object((1,3,6,1,4,1,3902,3,101,6,4,6))
if mibBuilder.loadTexts:qosCbQosqueueCfgTable.setStatus(_A)
_QosCbQosqueueCfgEntry_Object=MibTableRow
qosCbQosqueueCfgEntry=_QosCbQosqueueCfgEntry_Object((1,3,6,1,4,1,3902,3,101,6,4,6,1))
qosCbQosqueueCfgEntry.setIndexNames((0,_D,_K),(0,_D,_I))
if mibBuilder.loadTexts:qosCbQosqueueCfgEntry.setStatus(_A)
_QosCbQosQueueingCfgPriorityQueueNo_Type=QosPQQueueType
_QosCbQosQueueingCfgPriorityQueueNo_Object=MibTableColumn
qosCbQosQueueingCfgPriorityQueueNo=_QosCbQosQueueingCfgPriorityQueueNo_Object((1,3,6,1,4,1,3902,3,101,6,4,6,1,1),_QosCbQosQueueingCfgPriorityQueueNo_Type())
qosCbQosQueueingCfgPriorityQueueNo.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosQueueingCfgPriorityQueueNo.setStatus(_A)
_QosCbQosqueueRowStatus_Type=EntryStatus
_QosCbQosqueueRowStatus_Object=MibTableColumn
qosCbQosqueueRowStatus=_QosCbQosqueueRowStatus_Object((1,3,6,1,4,1,3902,3,101,6,4,6,1,2),_QosCbQosqueueRowStatus_Type())
qosCbQosqueueRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosqueueRowStatus.setStatus(_A)
_QosCbQosbandwidthCfgTable_Object=MibTable
qosCbQosbandwidthCfgTable=_QosCbQosbandwidthCfgTable_Object((1,3,6,1,4,1,3902,3,101,6,4,7))
if mibBuilder.loadTexts:qosCbQosbandwidthCfgTable.setStatus(_A)
_QosCbQosbindwidthCfgEntry_Object=MibTableRow
qosCbQosbindwidthCfgEntry=_QosCbQosbindwidthCfgEntry_Object((1,3,6,1,4,1,3902,3,101,6,4,7,1))
qosCbQosbindwidthCfgEntry.setIndexNames((0,_D,_K),(0,_D,_I))
if mibBuilder.loadTexts:qosCbQosbindwidthCfgEntry.setStatus(_A)
_QosCbQosQueueingCfgBandwidth_Type=Integer32
_QosCbQosQueueingCfgBandwidth_Object=MibTableColumn
qosCbQosQueueingCfgBandwidth=_QosCbQosQueueingCfgBandwidth_Object((1,3,6,1,4,1,3902,3,101,6,4,7,1,1),_QosCbQosQueueingCfgBandwidth_Type())
qosCbQosQueueingCfgBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosQueueingCfgBandwidth.setStatus(_A)
_QosCbQosQueueingCfgBandwidthUnits_Type=QueueingBandwidthUnits
_QosCbQosQueueingCfgBandwidthUnits_Object=MibTableColumn
qosCbQosQueueingCfgBandwidthUnits=_QosCbQosQueueingCfgBandwidthUnits_Object((1,3,6,1,4,1,3902,3,101,6,4,7,1,2),_QosCbQosQueueingCfgBandwidthUnits_Type())
qosCbQosQueueingCfgBandwidthUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosQueueingCfgBandwidthUnits.setStatus(_A)
_QosCbQosActionRowStatus_Type=EntryStatus
_QosCbQosActionRowStatus_Object=MibTableColumn
qosCbQosActionRowStatus=_QosCbQosActionRowStatus_Object((1,3,6,1,4,1,3902,3,101,6,4,7,1,3),_QosCbQosActionRowStatus_Type())
qosCbQosActionRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosActionRowStatus.setStatus(_A)
_QosCbQosPoliceCfgTable_Object=MibTable
qosCbQosPoliceCfgTable=_QosCbQosPoliceCfgTable_Object((1,3,6,1,4,1,3902,3,101,6,4,8))
if mibBuilder.loadTexts:qosCbQosPoliceCfgTable.setStatus(_A)
_QosCbQosPoliceCfgEntry_Object=MibTableRow
qosCbQosPoliceCfgEntry=_QosCbQosPoliceCfgEntry_Object((1,3,6,1,4,1,3902,3,101,6,4,8,1))
qosCbQosPoliceCfgEntry.setIndexNames((0,_D,_K),(0,_D,_I))
if mibBuilder.loadTexts:qosCbQosPoliceCfgEntry.setStatus(_A)
class _QosCbQosPoliceCfgCir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2000000))
_QosCbQosPoliceCfgCir_Type.__name__=_J
_QosCbQosPoliceCfgCir_Object=MibTableColumn
qosCbQosPoliceCfgCir=_QosCbQosPoliceCfgCir_Object((1,3,6,1,4,1,3902,3,101,6,4,8,1,1),_QosCbQosPoliceCfgCir_Type())
qosCbQosPoliceCfgCir.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosPoliceCfgCir.setStatus(_A)
if mibBuilder.loadTexts:qosCbQosPoliceCfgCir.setUnits(_b)
class _QosCbQosPoliceCfgBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,512000000))
_QosCbQosPoliceCfgBurstSize_Type.__name__=_J
_QosCbQosPoliceCfgBurstSize_Object=MibTableColumn
qosCbQosPoliceCfgBurstSize=_QosCbQosPoliceCfgBurstSize_Object((1,3,6,1,4,1,3902,3,101,6,4,8,1,2),_QosCbQosPoliceCfgBurstSize_Type())
qosCbQosPoliceCfgBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosPoliceCfgBurstSize.setStatus(_A)
if mibBuilder.loadTexts:qosCbQosPoliceCfgBurstSize.setUnits('bytes')
class _QosCbQosPoliceCfgPir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2000000))
_QosCbQosPoliceCfgPir_Type.__name__=_J
_QosCbQosPoliceCfgPir_Object=MibTableColumn
qosCbQosPoliceCfgPir=_QosCbQosPoliceCfgPir_Object((1,3,6,1,4,1,3902,3,101,6,4,8,1,3),_QosCbQosPoliceCfgPir_Type())
qosCbQosPoliceCfgPir.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosPoliceCfgPir.setStatus(_A)
if mibBuilder.loadTexts:qosCbQosPoliceCfgPir.setUnits(_b)
class _QosCbQosPoliceCfgExtBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,512000000))
_QosCbQosPoliceCfgExtBurstSize_Type.__name__=_J
_QosCbQosPoliceCfgExtBurstSize_Object=MibTableColumn
qosCbQosPoliceCfgExtBurstSize=_QosCbQosPoliceCfgExtBurstSize_Object((1,3,6,1,4,1,3902,3,101,6,4,8,1,4),_QosCbQosPoliceCfgExtBurstSize_Type())
qosCbQosPoliceCfgExtBurstSize.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosPoliceCfgExtBurstSize.setStatus(_A)
if mibBuilder.loadTexts:qosCbQosPoliceCfgExtBurstSize.setUnits('bytes')
_QosCbQosPoliceCfgConformAction_Type=QosCBQCarAction
_QosCbQosPoliceCfgConformAction_Object=MibTableColumn
qosCbQosPoliceCfgConformAction=_QosCbQosPoliceCfgConformAction_Object((1,3,6,1,4,1,3902,3,101,6,4,8,1,5),_QosCbQosPoliceCfgConformAction_Type())
qosCbQosPoliceCfgConformAction.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosPoliceCfgConformAction.setStatus(_A)
_QosCbQosPoliceCfgConformSetValue_Type=Gauge32
_QosCbQosPoliceCfgConformSetValue_Object=MibTableColumn
qosCbQosPoliceCfgConformSetValue=_QosCbQosPoliceCfgConformSetValue_Object((1,3,6,1,4,1,3902,3,101,6,4,8,1,6),_QosCbQosPoliceCfgConformSetValue_Type())
qosCbQosPoliceCfgConformSetValue.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosPoliceCfgConformSetValue.setStatus(_A)
_QosCbQosPoliceCfgExceedAction_Type=QosCBQCarAction
_QosCbQosPoliceCfgExceedAction_Object=MibTableColumn
qosCbQosPoliceCfgExceedAction=_QosCbQosPoliceCfgExceedAction_Object((1,3,6,1,4,1,3902,3,101,6,4,8,1,7),_QosCbQosPoliceCfgExceedAction_Type())
qosCbQosPoliceCfgExceedAction.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosPoliceCfgExceedAction.setStatus(_A)
_QosCbQosPoliceCfgExceedSetValue_Type=Gauge32
_QosCbQosPoliceCfgExceedSetValue_Object=MibTableColumn
qosCbQosPoliceCfgExceedSetValue=_QosCbQosPoliceCfgExceedSetValue_Object((1,3,6,1,4,1,3902,3,101,6,4,8,1,8),_QosCbQosPoliceCfgExceedSetValue_Type())
qosCbQosPoliceCfgExceedSetValue.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosPoliceCfgExceedSetValue.setStatus(_A)
_QosCbQosPoliceCfgViolateAction_Type=QosCBQCarAction
_QosCbQosPoliceCfgViolateAction_Object=MibTableColumn
qosCbQosPoliceCfgViolateAction=_QosCbQosPoliceCfgViolateAction_Object((1,3,6,1,4,1,3902,3,101,6,4,8,1,9),_QosCbQosPoliceCfgViolateAction_Type())
qosCbQosPoliceCfgViolateAction.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosPoliceCfgViolateAction.setStatus(_A)
_QosCbQosPoliceCfgViolateSetValue_Type=Gauge32
_QosCbQosPoliceCfgViolateSetValue_Object=MibTableColumn
qosCbQosPoliceCfgViolateSetValue=_QosCbQosPoliceCfgViolateSetValue_Object((1,3,6,1,4,1,3902,3,101,6,4,8,1,10),_QosCbQosPoliceCfgViolateSetValue_Type())
qosCbQosPoliceCfgViolateSetValue.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosPoliceCfgViolateSetValue.setStatus(_A)
_QosCbQosPoliceCfgRowStatus_Type=EntryStatus
_QosCbQosPoliceCfgRowStatus_Object=MibTableColumn
qosCbQosPoliceCfgRowStatus=_QosCbQosPoliceCfgRowStatus_Object((1,3,6,1,4,1,3902,3,101,6,4,8,1,11),_QosCbQosPoliceCfgRowStatus_Type())
qosCbQosPoliceCfgRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCbQosPoliceCfgRowStatus.setStatus(_A)
_QosWREDconfig_ObjectIdentity=ObjectIdentity
qosWREDconfig=_QosWREDconfig_ObjectIdentity((1,3,6,1,4,1,3902,3,101,6,5))
_QosWREDprecedenceCfgTable_Object=MibTable
qosWREDprecedenceCfgTable=_QosWREDprecedenceCfgTable_Object((1,3,6,1,4,1,3902,3,101,6,5,1))
if mibBuilder.loadTexts:qosWREDprecedenceCfgTable.setStatus(_A)
_QosWREDprecedenceCfgEntry_Object=MibTableRow
qosWREDprecedenceCfgEntry=_QosWREDprecedenceCfgEntry_Object((1,3,6,1,4,1,3902,3,101,6,5,1,1))
qosWREDprecedenceCfgEntry.setIndexNames((0,_E,_F),(0,_D,_c))
if mibBuilder.loadTexts:qosWREDprecedenceCfgEntry.setStatus(_A)
_QosREDCfgPreValue_Type=Integer32
_QosREDCfgPreValue_Object=MibTableColumn
qosREDCfgPreValue=_QosREDCfgPreValue_Object((1,3,6,1,4,1,3902,3,101,6,5,1,1,1),_QosREDCfgPreValue_Type())
qosREDCfgPreValue.setMaxAccess(_B)
if mibBuilder.loadTexts:qosREDCfgPreValue.setStatus(_A)
_QosREDprecedenceCfgMinThreshold_Type=Integer32
_QosREDprecedenceCfgMinThreshold_Object=MibTableColumn
qosREDprecedenceCfgMinThreshold=_QosREDprecedenceCfgMinThreshold_Object((1,3,6,1,4,1,3902,3,101,6,5,1,1,2),_QosREDprecedenceCfgMinThreshold_Type())
qosREDprecedenceCfgMinThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:qosREDprecedenceCfgMinThreshold.setStatus(_A)
_QosREDprecedenceCfgMaxThreshold_Type=Integer32
_QosREDprecedenceCfgMaxThreshold_Object=MibTableColumn
qosREDprecedenceCfgMaxThreshold=_QosREDprecedenceCfgMaxThreshold_Object((1,3,6,1,4,1,3902,3,101,6,5,1,1,3),_QosREDprecedenceCfgMaxThreshold_Type())
qosREDprecedenceCfgMaxThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:qosREDprecedenceCfgMaxThreshold.setStatus(_A)
_QosREDprecedenceCfgPktDropProb_Type=Integer32
_QosREDprecedenceCfgPktDropProb_Object=MibTableColumn
qosREDprecedenceCfgPktDropProb=_QosREDprecedenceCfgPktDropProb_Object((1,3,6,1,4,1,3902,3,101,6,5,1,1,4),_QosREDprecedenceCfgPktDropProb_Type())
qosREDprecedenceCfgPktDropProb.setMaxAccess(_B)
if mibBuilder.loadTexts:qosREDprecedenceCfgPktDropProb.setStatus(_A)
_QosREDCfgprecedenceRowStatus_Type=EntryStatus
_QosREDCfgprecedenceRowStatus_Object=MibTableColumn
qosREDCfgprecedenceRowStatus=_QosREDCfgprecedenceRowStatus_Object((1,3,6,1,4,1,3902,3,101,6,5,1,1,5),_QosREDCfgprecedenceRowStatus_Type())
qosREDCfgprecedenceRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qosREDCfgprecedenceRowStatus.setStatus(_A)
_QosWREDweightCfgTable_Object=MibTable
qosWREDweightCfgTable=_QosWREDweightCfgTable_Object((1,3,6,1,4,1,3902,3,101,6,5,2))
if mibBuilder.loadTexts:qosWREDweightCfgTable.setStatus(_A)
_QosWREDweightCfgEntry_Object=MibTableRow
qosWREDweightCfgEntry=_QosWREDweightCfgEntry_Object((1,3,6,1,4,1,3902,3,101,6,5,2,1))
qosWREDweightCfgEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:qosWREDweightCfgEntry.setStatus(_A)
_QosREDCfgweightValue_Type=Integer32
_QosREDCfgweightValue_Object=MibTableColumn
qosREDCfgweightValue=_QosREDCfgweightValue_Object((1,3,6,1,4,1,3902,3,101,6,5,2,1,1),_QosREDCfgweightValue_Type())
qosREDCfgweightValue.setMaxAccess(_B)
if mibBuilder.loadTexts:qosREDCfgweightValue.setStatus(_A)
_QosREDCfgweightRowStatus_Type=EntryStatus
_QosREDCfgweightRowStatus_Object=MibTableColumn
qosREDCfgweightRowStatus=_QosREDCfgweightRowStatus_Object((1,3,6,1,4,1,3902,3,101,6,5,2,1,2),_QosREDCfgweightRowStatus_Type())
qosREDCfgweightRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qosREDCfgweightRowStatus.setStatus(_A)
_QosWFQconfig_ObjectIdentity=ObjectIdentity
qosWFQconfig=_QosWFQconfig_ObjectIdentity((1,3,6,1,4,1,3902,3,101,6,6))
_QosWFQCfgTable_Object=MibTable
qosWFQCfgTable=_QosWFQCfgTable_Object((1,3,6,1,4,1,3902,3,101,6,6,1))
if mibBuilder.loadTexts:qosWFQCfgTable.setStatus(_A)
_QosWFQCfgEntry_Object=MibTableRow
qosWFQCfgEntry=_QosWFQCfgEntry_Object((1,3,6,1,4,1,3902,3,101,6,6,1,1))
qosWFQCfgEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:qosWFQCfgEntry.setStatus(_A)
_QosWFQCfgTotalQueueNum_Type=Integer32
_QosWFQCfgTotalQueueNum_Object=MibTableColumn
qosWFQCfgTotalQueueNum=_QosWFQCfgTotalQueueNum_Object((1,3,6,1,4,1,3902,3,101,6,6,1,1,1),_QosWFQCfgTotalQueueNum_Type())
qosWFQCfgTotalQueueNum.setMaxAccess(_B)
if mibBuilder.loadTexts:qosWFQCfgTotalQueueNum.setStatus(_A)
_QosWFQCfgQueueLimit_Type=Integer32
_QosWFQCfgQueueLimit_Object=MibTableColumn
qosWFQCfgQueueLimit=_QosWFQCfgQueueLimit_Object((1,3,6,1,4,1,3902,3,101,6,6,1,1,2),_QosWFQCfgQueueLimit_Type())
qosWFQCfgQueueLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:qosWFQCfgQueueLimit.setStatus(_A)
_QosWFQCfgRowStatus_Type=EntryStatus
_QosWFQCfgRowStatus_Object=MibTableColumn
qosWFQCfgRowStatus=_QosWFQCfgRowStatus_Object((1,3,6,1,4,1,3902,3,101,6,6,1,1,3),_QosWFQCfgRowStatus_Type())
qosWFQCfgRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qosWFQCfgRowStatus.setStatus(_A)
_QosCARconfig_ObjectIdentity=ObjectIdentity
qosCARconfig=_QosCARconfig_ObjectIdentity((1,3,6,1,4,1,3902,3,101,6,7))
_QosFreeCirIndex_Type=Integer32
_QosFreeCirIndex_Object=MibScalar
qosFreeCirIndex=_QosFreeCirIndex_Object((1,3,6,1,4,1,3902,3,101,6,7,1),_QosFreeCirIndex_Type())
qosFreeCirIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qosFreeCirIndex.setStatus(_A)
_QosInputCirIfTable_Object=MibTable
qosInputCirIfTable=_QosInputCirIfTable_Object((1,3,6,1,4,1,3902,3,101,6,7,2))
if mibBuilder.loadTexts:qosInputCirIfTable.setStatus(_A)
_QosInputCirIfEntry_Object=MibTableRow
qosInputCirIfEntry=_QosInputCirIfEntry_Object((1,3,6,1,4,1,3902,3,101,6,7,2,1))
qosInputCirIfEntry.setIndexNames((0,_E,_F),(0,_D,_d))
if mibBuilder.loadTexts:qosInputCirIfEntry.setStatus(_A)
_QosInputCirIndex_Type=Integer32
_QosInputCirIndex_Object=MibTableColumn
qosInputCirIndex=_QosInputCirIndex_Object((1,3,6,1,4,1,3902,3,101,6,7,2,1,1),_QosInputCirIndex_Type())
qosInputCirIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qosInputCirIndex.setStatus(_A)
_QosInputCirMatchType_Type=QosCirMatchType
_QosInputCirMatchType_Object=MibTableColumn
qosInputCirMatchType=_QosInputCirMatchType_Object((1,3,6,1,4,1,3902,3,101,6,7,2,1,2),_QosInputCirMatchType_Type())
qosInputCirMatchType.setMaxAccess(_B)
if mibBuilder.loadTexts:qosInputCirMatchType.setStatus(_A)
_QosInputCirMatchValue_Type=DisplayString
_QosInputCirMatchValue_Object=MibTableColumn
qosInputCirMatchValue=_QosInputCirMatchValue_Object((1,3,6,1,4,1,3902,3,101,6,7,2,1,3),_QosInputCirMatchValue_Type())
qosInputCirMatchValue.setMaxAccess(_B)
if mibBuilder.loadTexts:qosInputCirMatchValue.setStatus(_A)
class _QosInputCirCir_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2000000))
_QosInputCirCir_Type.__name__=_G
_QosInputCirCir_Object=MibTableColumn
qosInputCirCir=_QosInputCirCir_Object((1,3,6,1,4,1,3902,3,101,6,7,2,1,4),_QosInputCirCir_Type())
qosInputCirCir.setMaxAccess(_B)
if mibBuilder.loadTexts:qosInputCirCir.setStatus(_A)
class _QosInputCirNormalBurstRate_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,512000000))
_QosInputCirNormalBurstRate_Type.__name__=_G
_QosInputCirNormalBurstRate_Object=MibTableColumn
qosInputCirNormalBurstRate=_QosInputCirNormalBurstRate_Object((1,3,6,1,4,1,3902,3,101,6,7,2,1,5),_QosInputCirNormalBurstRate_Type())
qosInputCirNormalBurstRate.setMaxAccess(_B)
if mibBuilder.loadTexts:qosInputCirNormalBurstRate.setStatus(_A)
class _QosInputCirPir_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2000000))
_QosInputCirPir_Type.__name__=_G
_QosInputCirPir_Object=MibTableColumn
qosInputCirPir=_QosInputCirPir_Object((1,3,6,1,4,1,3902,3,101,6,7,2,1,6),_QosInputCirPir_Type())
qosInputCirPir.setMaxAccess(_B)
if mibBuilder.loadTexts:qosInputCirPir.setStatus(_A)
class _QosInputCirMaxBurstRate_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,512000000))
_QosInputCirMaxBurstRate_Type.__name__=_G
_QosInputCirMaxBurstRate_Object=MibTableColumn
qosInputCirMaxBurstRate=_QosInputCirMaxBurstRate_Object((1,3,6,1,4,1,3902,3,101,6,7,2,1,7),_QosInputCirMaxBurstRate_Type())
qosInputCirMaxBurstRate.setMaxAccess(_B)
if mibBuilder.loadTexts:qosInputCirMaxBurstRate.setStatus(_A)
_QosInputCirConformAction_Type=QosCirAction
_QosInputCirConformAction_Object=MibTableColumn
qosInputCirConformAction=_QosInputCirConformAction_Object((1,3,6,1,4,1,3902,3,101,6,7,2,1,8),_QosInputCirConformAction_Type())
qosInputCirConformAction.setMaxAccess(_B)
if mibBuilder.loadTexts:qosInputCirConformAction.setStatus(_A)
_QosInputCirConformValue_Type=Gauge32
_QosInputCirConformValue_Object=MibTableColumn
qosInputCirConformValue=_QosInputCirConformValue_Object((1,3,6,1,4,1,3902,3,101,6,7,2,1,9),_QosInputCirConformValue_Type())
qosInputCirConformValue.setMaxAccess(_B)
if mibBuilder.loadTexts:qosInputCirConformValue.setStatus(_A)
_QosInputCirExceedAction_Type=QosCirAction
_QosInputCirExceedAction_Object=MibTableColumn
qosInputCirExceedAction=_QosInputCirExceedAction_Object((1,3,6,1,4,1,3902,3,101,6,7,2,1,10),_QosInputCirExceedAction_Type())
qosInputCirExceedAction.setMaxAccess(_B)
if mibBuilder.loadTexts:qosInputCirExceedAction.setStatus(_A)
_QosInputCirExceedValue_Type=Gauge32
_QosInputCirExceedValue_Object=MibTableColumn
qosInputCirExceedValue=_QosInputCirExceedValue_Object((1,3,6,1,4,1,3902,3,101,6,7,2,1,11),_QosInputCirExceedValue_Type())
qosInputCirExceedValue.setMaxAccess(_B)
if mibBuilder.loadTexts:qosInputCirExceedValue.setStatus(_A)
_QosInputCirViolateAction_Type=QosCirAction
_QosInputCirViolateAction_Object=MibTableColumn
qosInputCirViolateAction=_QosInputCirViolateAction_Object((1,3,6,1,4,1,3902,3,101,6,7,2,1,12),_QosInputCirViolateAction_Type())
qosInputCirViolateAction.setMaxAccess(_B)
if mibBuilder.loadTexts:qosInputCirViolateAction.setStatus(_A)
_QosInputCirViolateValue_Type=Gauge32
_QosInputCirViolateValue_Object=MibTableColumn
qosInputCirViolateValue=_QosInputCirViolateValue_Object((1,3,6,1,4,1,3902,3,101,6,7,2,1,13),_QosInputCirViolateValue_Type())
qosInputCirViolateValue.setMaxAccess(_B)
if mibBuilder.loadTexts:qosInputCirViolateValue.setStatus(_A)
_QosInputCirRowStatus_Type=EntryStatus
_QosInputCirRowStatus_Object=MibTableColumn
qosInputCirRowStatus=_QosInputCirRowStatus_Object((1,3,6,1,4,1,3902,3,101,6,7,2,1,14),_QosInputCirRowStatus_Type())
qosInputCirRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qosInputCirRowStatus.setStatus(_A)
_QosInputCirDescription_Type=DisplayString
_QosInputCirDescription_Object=MibTableColumn
qosInputCirDescription=_QosInputCirDescription_Object((1,3,6,1,4,1,3902,3,101,6,7,2,1,15),_QosInputCirDescription_Type())
qosInputCirDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:qosInputCirDescription.setStatus(_A)
_QosInputCirIfTableLastchange_Type=TimeTicks
_QosInputCirIfTableLastchange_Object=MibScalar
qosInputCirIfTableLastchange=_QosInputCirIfTableLastchange_Object((1,3,6,1,4,1,3902,3,101,6,7,3),_QosInputCirIfTableLastchange_Type())
qosInputCirIfTableLastchange.setMaxAccess(_C)
if mibBuilder.loadTexts:qosInputCirIfTableLastchange.setStatus(_A)
_QosOutputCirIfTable_Object=MibTable
qosOutputCirIfTable=_QosOutputCirIfTable_Object((1,3,6,1,4,1,3902,3,101,6,7,4))
if mibBuilder.loadTexts:qosOutputCirIfTable.setStatus(_A)
_QosOutputCirIfEntry_Object=MibTableRow
qosOutputCirIfEntry=_QosOutputCirIfEntry_Object((1,3,6,1,4,1,3902,3,101,6,7,4,1))
qosOutputCirIfEntry.setIndexNames((0,_E,_F),(0,_D,_e))
if mibBuilder.loadTexts:qosOutputCirIfEntry.setStatus(_A)
_QosOutputCirIndex_Type=Integer32
_QosOutputCirIndex_Object=MibTableColumn
qosOutputCirIndex=_QosOutputCirIndex_Object((1,3,6,1,4,1,3902,3,101,6,7,4,1,1),_QosOutputCirIndex_Type())
qosOutputCirIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qosOutputCirIndex.setStatus(_A)
_QosOutputCirMatchType_Type=QosCirMatchType
_QosOutputCirMatchType_Object=MibTableColumn
qosOutputCirMatchType=_QosOutputCirMatchType_Object((1,3,6,1,4,1,3902,3,101,6,7,4,1,2),_QosOutputCirMatchType_Type())
qosOutputCirMatchType.setMaxAccess(_B)
if mibBuilder.loadTexts:qosOutputCirMatchType.setStatus(_A)
_QosOutputCirMatchValue_Type=DisplayString
_QosOutputCirMatchValue_Object=MibTableColumn
qosOutputCirMatchValue=_QosOutputCirMatchValue_Object((1,3,6,1,4,1,3902,3,101,6,7,4,1,3),_QosOutputCirMatchValue_Type())
qosOutputCirMatchValue.setMaxAccess(_B)
if mibBuilder.loadTexts:qosOutputCirMatchValue.setStatus(_A)
class _QosOutputCirCir_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2000000))
_QosOutputCirCir_Type.__name__=_G
_QosOutputCirCir_Object=MibTableColumn
qosOutputCirCir=_QosOutputCirCir_Object((1,3,6,1,4,1,3902,3,101,6,7,4,1,4),_QosOutputCirCir_Type())
qosOutputCirCir.setMaxAccess(_B)
if mibBuilder.loadTexts:qosOutputCirCir.setStatus(_A)
class _QosOutputCirNormalBurstRate_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,512000000))
_QosOutputCirNormalBurstRate_Type.__name__=_G
_QosOutputCirNormalBurstRate_Object=MibTableColumn
qosOutputCirNormalBurstRate=_QosOutputCirNormalBurstRate_Object((1,3,6,1,4,1,3902,3,101,6,7,4,1,5),_QosOutputCirNormalBurstRate_Type())
qosOutputCirNormalBurstRate.setMaxAccess(_B)
if mibBuilder.loadTexts:qosOutputCirNormalBurstRate.setStatus(_A)
class _QosOutputCirPir_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,2000000))
_QosOutputCirPir_Type.__name__=_G
_QosOutputCirPir_Object=MibTableColumn
qosOutputCirPir=_QosOutputCirPir_Object((1,3,6,1,4,1,3902,3,101,6,7,4,1,6),_QosOutputCirPir_Type())
qosOutputCirPir.setMaxAccess(_B)
if mibBuilder.loadTexts:qosOutputCirPir.setStatus(_A)
class _QosOutputCirMaxBurstRate_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,512000000))
_QosOutputCirMaxBurstRate_Type.__name__=_G
_QosOutputCirMaxBurstRate_Object=MibTableColumn
qosOutputCirMaxBurstRate=_QosOutputCirMaxBurstRate_Object((1,3,6,1,4,1,3902,3,101,6,7,4,1,7),_QosOutputCirMaxBurstRate_Type())
qosOutputCirMaxBurstRate.setMaxAccess(_B)
if mibBuilder.loadTexts:qosOutputCirMaxBurstRate.setStatus(_A)
_QosOutputCirConformAction_Type=QosCirAction
_QosOutputCirConformAction_Object=MibTableColumn
qosOutputCirConformAction=_QosOutputCirConformAction_Object((1,3,6,1,4,1,3902,3,101,6,7,4,1,8),_QosOutputCirConformAction_Type())
qosOutputCirConformAction.setMaxAccess(_B)
if mibBuilder.loadTexts:qosOutputCirConformAction.setStatus(_A)
_QosOutputCirConformValue_Type=Gauge32
_QosOutputCirConformValue_Object=MibTableColumn
qosOutputCirConformValue=_QosOutputCirConformValue_Object((1,3,6,1,4,1,3902,3,101,6,7,4,1,9),_QosOutputCirConformValue_Type())
qosOutputCirConformValue.setMaxAccess(_B)
if mibBuilder.loadTexts:qosOutputCirConformValue.setStatus(_A)
_QosOutputCirExceedAction_Type=QosCirAction
_QosOutputCirExceedAction_Object=MibTableColumn
qosOutputCirExceedAction=_QosOutputCirExceedAction_Object((1,3,6,1,4,1,3902,3,101,6,7,4,1,10),_QosOutputCirExceedAction_Type())
qosOutputCirExceedAction.setMaxAccess(_B)
if mibBuilder.loadTexts:qosOutputCirExceedAction.setStatus(_A)
_QosOutputCirExceedValue_Type=Gauge32
_QosOutputCirExceedValue_Object=MibTableColumn
qosOutputCirExceedValue=_QosOutputCirExceedValue_Object((1,3,6,1,4,1,3902,3,101,6,7,4,1,11),_QosOutputCirExceedValue_Type())
qosOutputCirExceedValue.setMaxAccess(_B)
if mibBuilder.loadTexts:qosOutputCirExceedValue.setStatus(_A)
_QosOutputCirViolateAction_Type=QosCirAction
_QosOutputCirViolateAction_Object=MibTableColumn
qosOutputCirViolateAction=_QosOutputCirViolateAction_Object((1,3,6,1,4,1,3902,3,101,6,7,4,1,12),_QosOutputCirViolateAction_Type())
qosOutputCirViolateAction.setMaxAccess(_B)
if mibBuilder.loadTexts:qosOutputCirViolateAction.setStatus(_A)
_QosOutputCirViolateValue_Type=Gauge32
_QosOutputCirViolateValue_Object=MibTableColumn
qosOutputCirViolateValue=_QosOutputCirViolateValue_Object((1,3,6,1,4,1,3902,3,101,6,7,4,1,13),_QosOutputCirViolateValue_Type())
qosOutputCirViolateValue.setMaxAccess(_B)
if mibBuilder.loadTexts:qosOutputCirViolateValue.setStatus(_A)
_QosOutputCirRowStatus_Type=EntryStatus
_QosOutputCirRowStatus_Object=MibTableColumn
qosOutputCirRowStatus=_QosOutputCirRowStatus_Object((1,3,6,1,4,1,3902,3,101,6,7,4,1,14),_QosOutputCirRowStatus_Type())
qosOutputCirRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:qosOutputCirRowStatus.setStatus(_A)
_QosOutputCirDescription_Type=DisplayString
_QosOutputCirDescription_Object=MibTableColumn
qosOutputCirDescription=_QosOutputCirDescription_Object((1,3,6,1,4,1,3902,3,101,6,7,4,1,15),_QosOutputCirDescription_Type())
qosOutputCirDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:qosOutputCirDescription.setStatus(_A)
_QosOutputCirIfTableLastchange_Type=TimeTicks
_QosOutputCirIfTableLastchange_Object=MibScalar
qosOutputCirIfTableLastchange=_QosOutputCirIfTableLastchange_Object((1,3,6,1,4,1,3902,3,101,6,7,5),_QosOutputCirIfTableLastchange_Type())
qosOutputCirIfTableLastchange.setMaxAccess(_C)
if mibBuilder.loadTexts:qosOutputCirIfTableLastchange.setStatus(_A)
_QosIntfCarStat_ObjectIdentity=ObjectIdentity
qosIntfCarStat=_QosIntfCarStat_ObjectIdentity((1,3,6,1,4,1,3902,3,101,6,8))
_QosIfTraffStatInfoTable_Object=MibTable
qosIfTraffStatInfoTable=_QosIfTraffStatInfoTable_Object((1,3,6,1,4,1,3902,3,101,6,8,1))
if mibBuilder.loadTexts:qosIfTraffStatInfoTable.setStatus(_A)
_QosIfTraffStatInfoEntry_Object=MibTableRow
qosIfTraffStatInfoEntry=_QosIfTraffStatInfoEntry_Object((1,3,6,1,4,1,3902,3,101,6,8,1,1))
qosIfTraffStatInfoEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:qosIfTraffStatInfoEntry.setStatus(_A)
_QosIntfName_Type=DisplayString
_QosIntfName_Object=MibTableColumn
qosIntfName=_QosIntfName_Object((1,3,6,1,4,1,3902,3,101,6,8,1,1,1),_QosIntfName_Type())
qosIntfName.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIntfName.setStatus(_A)
_QosIntfInUtilization_Type=DisplayString
_QosIntfInUtilization_Object=MibTableColumn
qosIntfInUtilization=_QosIntfInUtilization_Object((1,3,6,1,4,1,3902,3,101,6,8,1,1,2),_QosIntfInUtilization_Type())
qosIntfInUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIntfInUtilization.setStatus(_A)
_QosIntfInCarTotalPackets_Type=DisplayString
_QosIntfInCarTotalPackets_Object=MibTableColumn
qosIntfInCarTotalPackets=_QosIntfInCarTotalPackets_Object((1,3,6,1,4,1,3902,3,101,6,8,1,1,3),_QosIntfInCarTotalPackets_Type())
qosIntfInCarTotalPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIntfInCarTotalPackets.setStatus(_A)
_QosIntfInCarTranPackets_Type=DisplayString
_QosIntfInCarTranPackets_Object=MibTableColumn
qosIntfInCarTranPackets=_QosIntfInCarTranPackets_Object((1,3,6,1,4,1,3902,3,101,6,8,1,1,4),_QosIntfInCarTranPackets_Type())
qosIntfInCarTranPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIntfInCarTranPackets.setStatus(_A)
_QosIntfInCarDropPackets_Type=DisplayString
_QosIntfInCarDropPackets_Object=MibTableColumn
qosIntfInCarDropPackets=_QosIntfInCarDropPackets_Object((1,3,6,1,4,1,3902,3,101,6,8,1,1,5),_QosIntfInCarDropPackets_Type())
qosIntfInCarDropPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIntfInCarDropPackets.setStatus(_A)
_QosIntfInCarTotalBytes_Type=DisplayString
_QosIntfInCarTotalBytes_Object=MibTableColumn
qosIntfInCarTotalBytes=_QosIntfInCarTotalBytes_Object((1,3,6,1,4,1,3902,3,101,6,8,1,1,6),_QosIntfInCarTotalBytes_Type())
qosIntfInCarTotalBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIntfInCarTotalBytes.setStatus(_A)
_QosIntfInCarTranBytes_Type=DisplayString
_QosIntfInCarTranBytes_Object=MibTableColumn
qosIntfInCarTranBytes=_QosIntfInCarTranBytes_Object((1,3,6,1,4,1,3902,3,101,6,8,1,1,7),_QosIntfInCarTranBytes_Type())
qosIntfInCarTranBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIntfInCarTranBytes.setStatus(_A)
_QosIntfInCarDropBytes_Type=DisplayString
_QosIntfInCarDropBytes_Object=MibTableColumn
qosIntfInCarDropBytes=_QosIntfInCarDropBytes_Object((1,3,6,1,4,1,3902,3,101,6,8,1,1,8),_QosIntfInCarDropBytes_Type())
qosIntfInCarDropBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIntfInCarDropBytes.setStatus(_A)
_QosIntfOutUtilization_Type=DisplayString
_QosIntfOutUtilization_Object=MibTableColumn
qosIntfOutUtilization=_QosIntfOutUtilization_Object((1,3,6,1,4,1,3902,3,101,6,8,1,1,9),_QosIntfOutUtilization_Type())
qosIntfOutUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIntfOutUtilization.setStatus(_A)
_QosIntfOutCarTotalPackets_Type=DisplayString
_QosIntfOutCarTotalPackets_Object=MibTableColumn
qosIntfOutCarTotalPackets=_QosIntfOutCarTotalPackets_Object((1,3,6,1,4,1,3902,3,101,6,8,1,1,10),_QosIntfOutCarTotalPackets_Type())
qosIntfOutCarTotalPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIntfOutCarTotalPackets.setStatus(_A)
_QosIntfOutCarTranPackets_Type=DisplayString
_QosIntfOutCarTranPackets_Object=MibTableColumn
qosIntfOutCarTranPackets=_QosIntfOutCarTranPackets_Object((1,3,6,1,4,1,3902,3,101,6,8,1,1,11),_QosIntfOutCarTranPackets_Type())
qosIntfOutCarTranPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIntfOutCarTranPackets.setStatus(_A)
_QosIntfOutCarDropPackets_Type=DisplayString
_QosIntfOutCarDropPackets_Object=MibTableColumn
qosIntfOutCarDropPackets=_QosIntfOutCarDropPackets_Object((1,3,6,1,4,1,3902,3,101,6,8,1,1,12),_QosIntfOutCarDropPackets_Type())
qosIntfOutCarDropPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIntfOutCarDropPackets.setStatus(_A)
_QosIntfOutCarTotalBytes_Type=DisplayString
_QosIntfOutCarTotalBytes_Object=MibTableColumn
qosIntfOutCarTotalBytes=_QosIntfOutCarTotalBytes_Object((1,3,6,1,4,1,3902,3,101,6,8,1,1,13),_QosIntfOutCarTotalBytes_Type())
qosIntfOutCarTotalBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIntfOutCarTotalBytes.setStatus(_A)
_QosIntfOutCarTranBytes_Type=DisplayString
_QosIntfOutCarTranBytes_Object=MibTableColumn
qosIntfOutCarTranBytes=_QosIntfOutCarTranBytes_Object((1,3,6,1,4,1,3902,3,101,6,8,1,1,14),_QosIntfOutCarTranBytes_Type())
qosIntfOutCarTranBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIntfOutCarTranBytes.setStatus(_A)
_QosIntfOutCarDropBytes_Type=DisplayString
_QosIntfOutCarDropBytes_Object=MibTableColumn
qosIntfOutCarDropBytes=_QosIntfOutCarDropBytes_Object((1,3,6,1,4,1,3902,3,101,6,8,1,1,15),_QosIntfOutCarDropBytes_Type())
qosIntfOutCarDropBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qosIntfOutCarDropBytes.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_U:DisplayString,'QosCirMatchType':QosCirMatchType,'QosCirAction':QosCirAction,'QosCBQCarAction':QosCBQCarAction,'QosPQMatchType':QosPQMatchType,'QosPQQueueType':QosPQQueueType,'QosCMAPMatchType':QosCMAPMatchType,'TrafficDirection':TrafficDirection,'QueueingBandwidthUnits':QueueingBandwidthUnits,'EntryStatus':EntryStatus,'zte':zte,'zxr10':zxr10,'zxr10protocol':zxr10protocol,'zxr10qos':zxr10qos,'qosModuleStart':qosModuleStart,'qosPQconfig':qosPQconfig,'qosPriorityQueueCfgTable':qosPriorityQueueCfgTable,'qosPriorityQueueCfgEntry':qosPriorityQueueCfgEntry,_T:qosPriorityQueueIndex,'qosPriorityQueueItemTotal':qosPriorityQueueItemTotal,'qosPriorityQueueDefault':qosPriorityQueueDefault,'qosPriorityQueueLimitHigh':qosPriorityQueueLimitHigh,'qosPriorityQueueLimitMedium':qosPriorityQueueLimitMedium,'qosPriorityQueueLimitNormal':qosPriorityQueueLimitNormal,'qosPriorityQueueLimitLow':qosPriorityQueueLimitLow,'qosPriorityQueueRowStatus':qosPriorityQueueRowStatus,'qosPriorityQueueCfgTableLastchange':qosPriorityQueueCfgTableLastchange,'qosPriorityQueueItemTable':qosPriorityQueueItemTable,'qosPriorityQueueItemEntry':qosPriorityQueueItemEntry,_Z:qosPriorityQueueItemIndex,'qosPriorityQueueItemMatchType':qosPriorityQueueItemMatchType,'qosPriorityQueueItemMatchValue':qosPriorityQueueItemMatchValue,'qosPriorityQueueItemQueueNum':qosPriorityQueueItemQueueNum,'qosPriorityQueueItemRowStatus':qosPriorityQueueItemRowStatus,'qosPriorityQueueItemDescription':qosPriorityQueueItemDescription,'qosPriorityGroupTable':qosPriorityGroupTable,'qosPriorityGroupEntry':qosPriorityGroupEntry,'qosPriorityGroupifname':qosPriorityGroupifname,'qosPriorityGroupNum':qosPriorityGroupNum,'qosPriorityGroupRowStatus':qosPriorityGroupRowStatus,'qosCQconfig':qosCQconfig,'qosCBQconfig':qosCBQconfig,'qosCBQosServicePolicyTable':qosCBQosServicePolicyTable,'qosCBQosServicePolicyEntry':qosCBQosServicePolicyEntry,'qosCbQosPolicyifname':qosCbQosPolicyifname,'qosCbQosPolicyDirection':qosCbQosPolicyDirection,'qosCbQosServicePolicyName':qosCbQosServicePolicyName,'qosCbQosServicePolicyRowStatus':qosCbQosServicePolicyRowStatus,'qosCbQosPolicyMapCfgTable':qosCbQosPolicyMapCfgTable,'qosCbQosPolicyMapCfgEntry':qosCbQosPolicyMapCfgEntry,_K:qoscbQosPMapIndex,'qoscbQosPolicyMapName':qoscbQosPolicyMapName,'qosCbQosPolicyMapRowStatus':qosCbQosPolicyMapRowStatus,'qoscbQosPolicyMapDescription':qoscbQosPolicyMapDescription,'qosCbQosClassMapCfgTable':qosCbQosClassMapCfgTable,'qosCbQosClassMapCfgEntry':qosCbQosClassMapCfgEntry,_I:qoscbQosCMapIndex,'qosCbQosClassMapName':qosCbQosClassMapName,'qosCbQosClassMapRowStatus':qosCbQosClassMapRowStatus,'qoscbQosClassMapDescription':qoscbQosClassMapDescription,'qosCbQosCMAPMatchCfgTable':qosCbQosCMAPMatchCfgTable,'qosCbQosCMAPMatchCfgEntry':qosCbQosCMAPMatchCfgEntry,_a:qosCbQosCMAPMatchIndex,'qosCbQosCMAPMatchType':qosCbQosCMAPMatchType,'qosCbQosCMAPMatchValue':qosCbQosCMAPMatchValue,'qosCbQosCMAPMatchRowStatus':qosCbQosCMAPMatchRowStatus,'qosCbQosPolicyClassCfgTable':qosCbQosPolicyClassCfgTable,'qosCbQosPolicyClassCfgEntry':qosCbQosPolicyClassCfgEntry,'qosCbQosPolicyClassName':qosCbQosPolicyClassName,'qosCbQosPolicyClassRowStatus':qosCbQosPolicyClassRowStatus,'qosCbQosqueueCfgTable':qosCbQosqueueCfgTable,'qosCbQosqueueCfgEntry':qosCbQosqueueCfgEntry,'qosCbQosQueueingCfgPriorityQueueNo':qosCbQosQueueingCfgPriorityQueueNo,'qosCbQosqueueRowStatus':qosCbQosqueueRowStatus,'qosCbQosbandwidthCfgTable':qosCbQosbandwidthCfgTable,'qosCbQosbindwidthCfgEntry':qosCbQosbindwidthCfgEntry,'qosCbQosQueueingCfgBandwidth':qosCbQosQueueingCfgBandwidth,'qosCbQosQueueingCfgBandwidthUnits':qosCbQosQueueingCfgBandwidthUnits,'qosCbQosActionRowStatus':qosCbQosActionRowStatus,'qosCbQosPoliceCfgTable':qosCbQosPoliceCfgTable,'qosCbQosPoliceCfgEntry':qosCbQosPoliceCfgEntry,'qosCbQosPoliceCfgCir':qosCbQosPoliceCfgCir,'qosCbQosPoliceCfgBurstSize':qosCbQosPoliceCfgBurstSize,'qosCbQosPoliceCfgPir':qosCbQosPoliceCfgPir,'qosCbQosPoliceCfgExtBurstSize':qosCbQosPoliceCfgExtBurstSize,'qosCbQosPoliceCfgConformAction':qosCbQosPoliceCfgConformAction,'qosCbQosPoliceCfgConformSetValue':qosCbQosPoliceCfgConformSetValue,'qosCbQosPoliceCfgExceedAction':qosCbQosPoliceCfgExceedAction,'qosCbQosPoliceCfgExceedSetValue':qosCbQosPoliceCfgExceedSetValue,'qosCbQosPoliceCfgViolateAction':qosCbQosPoliceCfgViolateAction,'qosCbQosPoliceCfgViolateSetValue':qosCbQosPoliceCfgViolateSetValue,'qosCbQosPoliceCfgRowStatus':qosCbQosPoliceCfgRowStatus,'qosWREDconfig':qosWREDconfig,'qosWREDprecedenceCfgTable':qosWREDprecedenceCfgTable,'qosWREDprecedenceCfgEntry':qosWREDprecedenceCfgEntry,_c:qosREDCfgPreValue,'qosREDprecedenceCfgMinThreshold':qosREDprecedenceCfgMinThreshold,'qosREDprecedenceCfgMaxThreshold':qosREDprecedenceCfgMaxThreshold,'qosREDprecedenceCfgPktDropProb':qosREDprecedenceCfgPktDropProb,'qosREDCfgprecedenceRowStatus':qosREDCfgprecedenceRowStatus,'qosWREDweightCfgTable':qosWREDweightCfgTable,'qosWREDweightCfgEntry':qosWREDweightCfgEntry,'qosREDCfgweightValue':qosREDCfgweightValue,'qosREDCfgweightRowStatus':qosREDCfgweightRowStatus,'qosWFQconfig':qosWFQconfig,'qosWFQCfgTable':qosWFQCfgTable,'qosWFQCfgEntry':qosWFQCfgEntry,'qosWFQCfgTotalQueueNum':qosWFQCfgTotalQueueNum,'qosWFQCfgQueueLimit':qosWFQCfgQueueLimit,'qosWFQCfgRowStatus':qosWFQCfgRowStatus,'qosCARconfig':qosCARconfig,'qosFreeCirIndex':qosFreeCirIndex,'qosInputCirIfTable':qosInputCirIfTable,'qosInputCirIfEntry':qosInputCirIfEntry,_d:qosInputCirIndex,'qosInputCirMatchType':qosInputCirMatchType,'qosInputCirMatchValue':qosInputCirMatchValue,'qosInputCirCir':qosInputCirCir,'qosInputCirNormalBurstRate':qosInputCirNormalBurstRate,'qosInputCirPir':qosInputCirPir,'qosInputCirMaxBurstRate':qosInputCirMaxBurstRate,'qosInputCirConformAction':qosInputCirConformAction,'qosInputCirConformValue':qosInputCirConformValue,'qosInputCirExceedAction':qosInputCirExceedAction,'qosInputCirExceedValue':qosInputCirExceedValue,'qosInputCirViolateAction':qosInputCirViolateAction,'qosInputCirViolateValue':qosInputCirViolateValue,'qosInputCirRowStatus':qosInputCirRowStatus,'qosInputCirDescription':qosInputCirDescription,'qosInputCirIfTableLastchange':qosInputCirIfTableLastchange,'qosOutputCirIfTable':qosOutputCirIfTable,'qosOutputCirIfEntry':qosOutputCirIfEntry,_e:qosOutputCirIndex,'qosOutputCirMatchType':qosOutputCirMatchType,'qosOutputCirMatchValue':qosOutputCirMatchValue,'qosOutputCirCir':qosOutputCirCir,'qosOutputCirNormalBurstRate':qosOutputCirNormalBurstRate,'qosOutputCirPir':qosOutputCirPir,'qosOutputCirMaxBurstRate':qosOutputCirMaxBurstRate,'qosOutputCirConformAction':qosOutputCirConformAction,'qosOutputCirConformValue':qosOutputCirConformValue,'qosOutputCirExceedAction':qosOutputCirExceedAction,'qosOutputCirExceedValue':qosOutputCirExceedValue,'qosOutputCirViolateAction':qosOutputCirViolateAction,'qosOutputCirViolateValue':qosOutputCirViolateValue,'qosOutputCirRowStatus':qosOutputCirRowStatus,'qosOutputCirDescription':qosOutputCirDescription,'qosOutputCirIfTableLastchange':qosOutputCirIfTableLastchange,'qosIntfCarStat':qosIntfCarStat,'qosIfTraffStatInfoTable':qosIfTraffStatInfoTable,'qosIfTraffStatInfoEntry':qosIfTraffStatInfoEntry,'qosIntfName':qosIntfName,'qosIntfInUtilization':qosIntfInUtilization,'qosIntfInCarTotalPackets':qosIntfInCarTotalPackets,'qosIntfInCarTranPackets':qosIntfInCarTranPackets,'qosIntfInCarDropPackets':qosIntfInCarDropPackets,'qosIntfInCarTotalBytes':qosIntfInCarTotalBytes,'qosIntfInCarTranBytes':qosIntfInCarTranBytes,'qosIntfInCarDropBytes':qosIntfInCarDropBytes,'qosIntfOutUtilization':qosIntfOutUtilization,'qosIntfOutCarTotalPackets':qosIntfOutCarTotalPackets,'qosIntfOutCarTranPackets':qosIntfOutCarTranPackets,'qosIntfOutCarDropPackets':qosIntfOutCarDropPackets,'qosIntfOutCarTotalBytes':qosIntfOutCarTotalBytes,'qosIntfOutCarTranBytes':qosIntfOutCarTranBytes,'qosIntfOutCarDropBytes':qosIntfOutCarDropBytes})