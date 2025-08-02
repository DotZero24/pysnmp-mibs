_t='aristaEcnQueueCounterGroup'
_s='aristaEcnCounterGroup'
_r='aristaServicePolicyGroup'
_q='aristaPolicyMapActionGroup'
_p='aristaPolicyMapGroup'
_o='aristaClassMapGroup'
_n='aristaEcnQueuePktsMarked'
_m='aristaEcnQueueCounterEnabled'
_l='aristaEcnCounterEntity'
_k='aristaEcnCounterValue'
_j='aristaServicePolicyMapType'
_i='aristaServicePolicyMapId'
_h='aristaPolicyMapActionValue'
_g='aristaPolicyMapActionRateUnit'
_f='aristaPolicyMapName'
_e='aristaQosBytesSent'
_d='aristaQosBytesMatched'
_c='aristaQosBytesDropped'
_b='aristaQosPolicerPktsSent'
_a='aristaQosPolicerPktsDropped'
_Z='aristaQosPktsSent'
_Y='aristaQosPktsMatched'
_X='aristaQosPktsDropped'
_W='aristaPolicyMapClassId'
_V='aristaClassMapMatchName'
_U='aristaClassMapMatchType'
_T='aristaClassMapMatchCondition'
_S='aristaClassMapName'
_R='aristaEcnEgressQueueIndex'
_Q='aristaEcnIfIndex'
_P='aristaEcnCounterDescriptor'
_O='aristaPolicyMapActionType'
_N='aristaPolicyMapClassIndex'
_M='aristaClassMapMatchIndex'
_L='aristaServicePolicyIfIndex'
_K='aristaClassMapType'
_J='aristaServicePolicyDirection'
_I='DisplayString'
_H='aristaPolicyMapType'
_G='aristaPolicyMapId'
_F='aristaClassMapId'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='ARISTA-QOS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
QueueIndex,=mibBuilder.importSymbols('ARISTA-QUEUE-MIB','QueueIndex')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
PhysicalIndexOrZero,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndexOrZero')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention','TruthValue')
aristaQosMib=ModuleIdentity((1,3,6,1,4,1,30065,3,13))
if mibBuilder.loadTexts:aristaQosMib.setRevisions(('2022-01-11 00:00','2020-05-26 00:00','2018-05-04 00:00','2017-05-24 00:00','2016-11-11 00:00','2016-07-22 00:00','2016-03-21 00:00','2014-08-15 00:00','2014-05-22 00:00','2013-06-01 00:00'))
class AristaQosMapType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('controlPlane',1),('dataPlane',2)))
class AristaQosShortId(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_AristaQosMibObjects_ObjectIdentity=ObjectIdentity
aristaQosMibObjects=_AristaQosMibObjects_ObjectIdentity((1,3,6,1,4,1,30065,3,13,1))
_AristaClassMapTable_Object=MibTable
aristaClassMapTable=_AristaClassMapTable_Object((1,3,6,1,4,1,30065,3,13,1,1))
if mibBuilder.loadTexts:aristaClassMapTable.setStatus(_A)
_AristaClassMapEntry_Object=MibTableRow
aristaClassMapEntry=_AristaClassMapEntry_Object((1,3,6,1,4,1,30065,3,13,1,1,1))
aristaClassMapEntry.setIndexNames((0,_B,_F),(0,_B,_K))
if mibBuilder.loadTexts:aristaClassMapEntry.setStatus(_A)
_AristaClassMapId_Type=AristaQosShortId
_AristaClassMapId_Object=MibTableColumn
aristaClassMapId=_AristaClassMapId_Object((1,3,6,1,4,1,30065,3,13,1,1,1,1),_AristaClassMapId_Type())
aristaClassMapId.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaClassMapId.setStatus(_A)
_AristaClassMapType_Type=AristaQosMapType
_AristaClassMapType_Object=MibTableColumn
aristaClassMapType=_AristaClassMapType_Object((1,3,6,1,4,1,30065,3,13,1,1,1,2),_AristaClassMapType_Type())
aristaClassMapType.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaClassMapType.setStatus(_A)
class _AristaClassMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AristaClassMapName_Type.__name__=_I
_AristaClassMapName_Object=MibTableColumn
aristaClassMapName=_AristaClassMapName_Object((1,3,6,1,4,1,30065,3,13,1,1,1,3),_AristaClassMapName_Type())
aristaClassMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaClassMapName.setStatus(_A)
class _AristaClassMapMatchCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('matchConditionAny',1),('matchConditionAll',2)))
_AristaClassMapMatchCondition_Type.__name__=_E
_AristaClassMapMatchCondition_Object=MibTableColumn
aristaClassMapMatchCondition=_AristaClassMapMatchCondition_Object((1,3,6,1,4,1,30065,3,13,1,1,1,4),_AristaClassMapMatchCondition_Type())
aristaClassMapMatchCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaClassMapMatchCondition.setStatus(_A)
_AristaClassMapMatchTable_Object=MibTable
aristaClassMapMatchTable=_AristaClassMapMatchTable_Object((1,3,6,1,4,1,30065,3,13,1,2))
if mibBuilder.loadTexts:aristaClassMapMatchTable.setStatus(_A)
_AristaClassMapMatchEntry_Object=MibTableRow
aristaClassMapMatchEntry=_AristaClassMapMatchEntry_Object((1,3,6,1,4,1,30065,3,13,1,2,1))
aristaClassMapMatchEntry.setIndexNames((0,_B,_F),(0,_B,_K),(0,_B,_M))
if mibBuilder.loadTexts:aristaClassMapMatchEntry.setStatus(_A)
class _AristaClassMapMatchIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AristaClassMapMatchIndex_Type.__name__=_E
_AristaClassMapMatchIndex_Object=MibTableColumn
aristaClassMapMatchIndex=_AristaClassMapMatchIndex_Object((1,3,6,1,4,1,30065,3,13,1,2,1,1),_AristaClassMapMatchIndex_Type())
aristaClassMapMatchIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaClassMapMatchIndex.setStatus(_A)
class _AristaClassMapMatchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ipv4AccessGroup',1),('ipv6AccessGroup',2),('vlan',3),('dscpEcn',4),('mplsTrafficClass',5),('macAccessGroup',6)))
_AristaClassMapMatchType_Type.__name__=_E
_AristaClassMapMatchType_Object=MibTableColumn
aristaClassMapMatchType=_AristaClassMapMatchType_Object((1,3,6,1,4,1,30065,3,13,1,2,1,2),_AristaClassMapMatchType_Type())
aristaClassMapMatchType.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaClassMapMatchType.setStatus(_A)
class _AristaClassMapMatchName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_AristaClassMapMatchName_Type.__name__=_I
_AristaClassMapMatchName_Object=MibTableColumn
aristaClassMapMatchName=_AristaClassMapMatchName_Object((1,3,6,1,4,1,30065,3,13,1,2,1,3),_AristaClassMapMatchName_Type())
aristaClassMapMatchName.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaClassMapMatchName.setStatus(_A)
_AristaPolicyMapTable_Object=MibTable
aristaPolicyMapTable=_AristaPolicyMapTable_Object((1,3,6,1,4,1,30065,3,13,1,3))
if mibBuilder.loadTexts:aristaPolicyMapTable.setStatus(_A)
_AristaPolicyMapEntry_Object=MibTableRow
aristaPolicyMapEntry=_AristaPolicyMapEntry_Object((1,3,6,1,4,1,30065,3,13,1,3,1))
aristaPolicyMapEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:aristaPolicyMapEntry.setStatus(_A)
_AristaPolicyMapId_Type=AristaQosShortId
_AristaPolicyMapId_Object=MibTableColumn
aristaPolicyMapId=_AristaPolicyMapId_Object((1,3,6,1,4,1,30065,3,13,1,3,1,1),_AristaPolicyMapId_Type())
aristaPolicyMapId.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaPolicyMapId.setStatus(_A)
_AristaPolicyMapType_Type=AristaQosMapType
_AristaPolicyMapType_Object=MibTableColumn
aristaPolicyMapType=_AristaPolicyMapType_Object((1,3,6,1,4,1,30065,3,13,1,3,1,2),_AristaPolicyMapType_Type())
aristaPolicyMapType.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaPolicyMapType.setStatus(_A)
class _AristaPolicyMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AristaPolicyMapName_Type.__name__=_I
_AristaPolicyMapName_Object=MibTableColumn
aristaPolicyMapName=_AristaPolicyMapName_Object((1,3,6,1,4,1,30065,3,13,1,3,1,3),_AristaPolicyMapName_Type())
aristaPolicyMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaPolicyMapName.setStatus(_A)
_AristaPolicyMapClassTable_Object=MibTable
aristaPolicyMapClassTable=_AristaPolicyMapClassTable_Object((1,3,6,1,4,1,30065,3,13,1,4))
if mibBuilder.loadTexts:aristaPolicyMapClassTable.setStatus(_A)
_AristaPolicyMapClassEntry_Object=MibTableRow
aristaPolicyMapClassEntry=_AristaPolicyMapClassEntry_Object((1,3,6,1,4,1,30065,3,13,1,4,1))
aristaPolicyMapClassEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_N))
if mibBuilder.loadTexts:aristaPolicyMapClassEntry.setStatus(_A)
class _AristaPolicyMapClassIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AristaPolicyMapClassIndex_Type.__name__=_E
_AristaPolicyMapClassIndex_Object=MibTableColumn
aristaPolicyMapClassIndex=_AristaPolicyMapClassIndex_Object((1,3,6,1,4,1,30065,3,13,1,4,1,1),_AristaPolicyMapClassIndex_Type())
aristaPolicyMapClassIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaPolicyMapClassIndex.setStatus(_A)
_AristaPolicyMapClassId_Type=AristaQosShortId
_AristaPolicyMapClassId_Object=MibTableColumn
aristaPolicyMapClassId=_AristaPolicyMapClassId_Object((1,3,6,1,4,1,30065,3,13,1,4,1,2),_AristaPolicyMapClassId_Type())
aristaPolicyMapClassId.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaPolicyMapClassId.setStatus(_A)
_AristaPolicyMapActionTable_Object=MibTable
aristaPolicyMapActionTable=_AristaPolicyMapActionTable_Object((1,3,6,1,4,1,30065,3,13,1,5))
if mibBuilder.loadTexts:aristaPolicyMapActionTable.setStatus(_A)
_AristaPolicyMapActionEntry_Object=MibTableRow
aristaPolicyMapActionEntry=_AristaPolicyMapActionEntry_Object((1,3,6,1,4,1,30065,3,13,1,5,1))
aristaPolicyMapActionEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_F),(0,_B,_O))
if mibBuilder.loadTexts:aristaPolicyMapActionEntry.setStatus(_A)
class _AristaPolicyMapActionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('actionSetShape',1),('actionSetBandwidth',2),('actionSetCos',3),('actionSetDscp',4),('actionSetTc',5),('actionSetDrop',6),('actionSetDropPrecedence',7)))
_AristaPolicyMapActionType_Type.__name__=_E
_AristaPolicyMapActionType_Object=MibTableColumn
aristaPolicyMapActionType=_AristaPolicyMapActionType_Object((1,3,6,1,4,1,30065,3,13,1,5,1,1),_AristaPolicyMapActionType_Type())
aristaPolicyMapActionType.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaPolicyMapActionType.setStatus(_A)
class _AristaPolicyMapActionRateUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('rateUnitNone',0),('rateUnitPps',1),('rateUnitKbps',2)))
_AristaPolicyMapActionRateUnit_Type.__name__=_E
_AristaPolicyMapActionRateUnit_Object=MibTableColumn
aristaPolicyMapActionRateUnit=_AristaPolicyMapActionRateUnit_Object((1,3,6,1,4,1,30065,3,13,1,5,1,2),_AristaPolicyMapActionRateUnit_Type())
aristaPolicyMapActionRateUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaPolicyMapActionRateUnit.setStatus(_A)
_AristaPolicyMapActionValue_Type=Integer32
_AristaPolicyMapActionValue_Object=MibTableColumn
aristaPolicyMapActionValue=_AristaPolicyMapActionValue_Object((1,3,6,1,4,1,30065,3,13,1,5,1,3),_AristaPolicyMapActionValue_Type())
aristaPolicyMapActionValue.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaPolicyMapActionValue.setStatus(_A)
_AristaServicePolicyTable_Object=MibTable
aristaServicePolicyTable=_AristaServicePolicyTable_Object((1,3,6,1,4,1,30065,3,13,1,6))
if mibBuilder.loadTexts:aristaServicePolicyTable.setStatus(_A)
_AristaServicePolicyEntry_Object=MibTableRow
aristaServicePolicyEntry=_AristaServicePolicyEntry_Object((1,3,6,1,4,1,30065,3,13,1,6,1))
aristaServicePolicyEntry.setIndexNames((0,_B,_L),(0,_B,_J))
if mibBuilder.loadTexts:aristaServicePolicyEntry.setStatus(_A)
_AristaServicePolicyIfIndex_Type=InterfaceIndex
_AristaServicePolicyIfIndex_Object=MibTableColumn
aristaServicePolicyIfIndex=_AristaServicePolicyIfIndex_Object((1,3,6,1,4,1,30065,3,13,1,6,1,1),_AristaServicePolicyIfIndex_Type())
aristaServicePolicyIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaServicePolicyIfIndex.setStatus(_A)
class _AristaServicePolicyDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('input',1),('output',2)))
_AristaServicePolicyDirection_Type.__name__=_E
_AristaServicePolicyDirection_Object=MibTableColumn
aristaServicePolicyDirection=_AristaServicePolicyDirection_Object((1,3,6,1,4,1,30065,3,13,1,6,1,2),_AristaServicePolicyDirection_Type())
aristaServicePolicyDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaServicePolicyDirection.setStatus(_A)
_AristaServicePolicyMapId_Type=AristaQosShortId
_AristaServicePolicyMapId_Object=MibTableColumn
aristaServicePolicyMapId=_AristaServicePolicyMapId_Object((1,3,6,1,4,1,30065,3,13,1,6,1,3),_AristaServicePolicyMapId_Type())
aristaServicePolicyMapId.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaServicePolicyMapId.setStatus(_A)
_AristaServicePolicyMapType_Type=AristaQosMapType
_AristaServicePolicyMapType_Object=MibTableColumn
aristaServicePolicyMapType=_AristaServicePolicyMapType_Object((1,3,6,1,4,1,30065,3,13,1,6,1,4),_AristaServicePolicyMapType_Type())
aristaServicePolicyMapType.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaServicePolicyMapType.setStatus(_A)
_AristaQosStatsTable_Object=MibTable
aristaQosStatsTable=_AristaQosStatsTable_Object((1,3,6,1,4,1,30065,3,13,1,7))
if mibBuilder.loadTexts:aristaQosStatsTable.setStatus(_A)
_AristaQosStatsEntry_Object=MibTableRow
aristaQosStatsEntry=_AristaQosStatsEntry_Object((1,3,6,1,4,1,30065,3,13,1,7,1))
aristaQosStatsEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_F),(0,_B,_J))
if mibBuilder.loadTexts:aristaQosStatsEntry.setStatus(_A)
_AristaQosPktsDropped_Type=Counter64
_AristaQosPktsDropped_Object=MibTableColumn
aristaQosPktsDropped=_AristaQosPktsDropped_Object((1,3,6,1,4,1,30065,3,13,1,7,1,1),_AristaQosPktsDropped_Type())
aristaQosPktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaQosPktsDropped.setStatus(_A)
_AristaQosPktsSent_Type=Counter64
_AristaQosPktsSent_Object=MibTableColumn
aristaQosPktsSent=_AristaQosPktsSent_Object((1,3,6,1,4,1,30065,3,13,1,7,1,2),_AristaQosPktsSent_Type())
aristaQosPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaQosPktsSent.setStatus(_A)
_AristaQosPktsMatched_Type=Counter64
_AristaQosPktsMatched_Object=MibTableColumn
aristaQosPktsMatched=_AristaQosPktsMatched_Object((1,3,6,1,4,1,30065,3,13,1,7,1,3),_AristaQosPktsMatched_Type())
aristaQosPktsMatched.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaQosPktsMatched.setStatus(_A)
_AristaQosBytesDropped_Type=Counter64
_AristaQosBytesDropped_Object=MibTableColumn
aristaQosBytesDropped=_AristaQosBytesDropped_Object((1,3,6,1,4,1,30065,3,13,1,7,1,4),_AristaQosBytesDropped_Type())
aristaQosBytesDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaQosBytesDropped.setStatus(_A)
_AristaQosBytesSent_Type=Counter64
_AristaQosBytesSent_Object=MibTableColumn
aristaQosBytesSent=_AristaQosBytesSent_Object((1,3,6,1,4,1,30065,3,13,1,7,1,5),_AristaQosBytesSent_Type())
aristaQosBytesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaQosBytesSent.setStatus(_A)
_AristaQosBytesMatched_Type=Counter64
_AristaQosBytesMatched_Object=MibTableColumn
aristaQosBytesMatched=_AristaQosBytesMatched_Object((1,3,6,1,4,1,30065,3,13,1,7,1,6),_AristaQosBytesMatched_Type())
aristaQosBytesMatched.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaQosBytesMatched.setStatus(_A)
_AristaEcnCounterTable_Object=MibTable
aristaEcnCounterTable=_AristaEcnCounterTable_Object((1,3,6,1,4,1,30065,3,13,1,8))
if mibBuilder.loadTexts:aristaEcnCounterTable.setStatus(_A)
_AristaEcnCounterEntry_Object=MibTableRow
aristaEcnCounterEntry=_AristaEcnCounterEntry_Object((1,3,6,1,4,1,30065,3,13,1,8,1))
aristaEcnCounterEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:aristaEcnCounterEntry.setStatus(_A)
class _AristaEcnCounterDescriptor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AristaEcnCounterDescriptor_Type.__name__=_I
_AristaEcnCounterDescriptor_Object=MibTableColumn
aristaEcnCounterDescriptor=_AristaEcnCounterDescriptor_Object((1,3,6,1,4,1,30065,3,13,1,8,1,1),_AristaEcnCounterDescriptor_Type())
aristaEcnCounterDescriptor.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaEcnCounterDescriptor.setStatus(_A)
_AristaEcnCounterValue_Type=Counter64
_AristaEcnCounterValue_Object=MibTableColumn
aristaEcnCounterValue=_AristaEcnCounterValue_Object((1,3,6,1,4,1,30065,3,13,1,8,1,2),_AristaEcnCounterValue_Type())
aristaEcnCounterValue.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaEcnCounterValue.setStatus(_A)
_AristaEcnCounterEntity_Type=PhysicalIndexOrZero
_AristaEcnCounterEntity_Object=MibTableColumn
aristaEcnCounterEntity=_AristaEcnCounterEntity_Object((1,3,6,1,4,1,30065,3,13,1,8,1,3),_AristaEcnCounterEntity_Type())
aristaEcnCounterEntity.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaEcnCounterEntity.setStatus(_A)
_AristaEcnQueueCounterTable_Object=MibTable
aristaEcnQueueCounterTable=_AristaEcnQueueCounterTable_Object((1,3,6,1,4,1,30065,3,13,1,9))
if mibBuilder.loadTexts:aristaEcnQueueCounterTable.setStatus(_A)
_AristaEcnQueueCounterEntry_Object=MibTableRow
aristaEcnQueueCounterEntry=_AristaEcnQueueCounterEntry_Object((1,3,6,1,4,1,30065,3,13,1,9,1))
aristaEcnQueueCounterEntry.setIndexNames((0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:aristaEcnQueueCounterEntry.setStatus(_A)
_AristaEcnIfIndex_Type=InterfaceIndex
_AristaEcnIfIndex_Object=MibTableColumn
aristaEcnIfIndex=_AristaEcnIfIndex_Object((1,3,6,1,4,1,30065,3,13,1,9,1,1),_AristaEcnIfIndex_Type())
aristaEcnIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaEcnIfIndex.setStatus(_A)
_AristaEcnEgressQueueIndex_Type=QueueIndex
_AristaEcnEgressQueueIndex_Object=MibTableColumn
aristaEcnEgressQueueIndex=_AristaEcnEgressQueueIndex_Object((1,3,6,1,4,1,30065,3,13,1,9,1,2),_AristaEcnEgressQueueIndex_Type())
aristaEcnEgressQueueIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaEcnEgressQueueIndex.setStatus(_A)
_AristaEcnQueueCounterEnabled_Type=TruthValue
_AristaEcnQueueCounterEnabled_Object=MibTableColumn
aristaEcnQueueCounterEnabled=_AristaEcnQueueCounterEnabled_Object((1,3,6,1,4,1,30065,3,13,1,9,1,3),_AristaEcnQueueCounterEnabled_Type())
aristaEcnQueueCounterEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaEcnQueueCounterEnabled.setStatus(_A)
_AristaEcnQueuePktsMarked_Type=Counter64
_AristaEcnQueuePktsMarked_Object=MibTableColumn
aristaEcnQueuePktsMarked=_AristaEcnQueuePktsMarked_Object((1,3,6,1,4,1,30065,3,13,1,9,1,4),_AristaEcnQueuePktsMarked_Type())
aristaEcnQueuePktsMarked.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaEcnQueuePktsMarked.setStatus(_A)
_AristaQosPolicerStatsTable_Object=MibTable
aristaQosPolicerStatsTable=_AristaQosPolicerStatsTable_Object((1,3,6,1,4,1,30065,3,13,1,10))
if mibBuilder.loadTexts:aristaQosPolicerStatsTable.setStatus(_A)
_AristaQosPolicerStatsEntry_Object=MibTableRow
aristaQosPolicerStatsEntry=_AristaQosPolicerStatsEntry_Object((1,3,6,1,4,1,30065,3,13,1,10,1))
aristaQosPolicerStatsEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_F),(0,_B,_J),(0,_B,_L))
if mibBuilder.loadTexts:aristaQosPolicerStatsEntry.setStatus(_A)
_AristaQosPolicerPktsDropped_Type=Counter64
_AristaQosPolicerPktsDropped_Object=MibTableColumn
aristaQosPolicerPktsDropped=_AristaQosPolicerPktsDropped_Object((1,3,6,1,4,1,30065,3,13,1,10,1,1),_AristaQosPolicerPktsDropped_Type())
aristaQosPolicerPktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaQosPolicerPktsDropped.setStatus(_A)
_AristaQosPolicerPktsSent_Type=Counter64
_AristaQosPolicerPktsSent_Object=MibTableColumn
aristaQosPolicerPktsSent=_AristaQosPolicerPktsSent_Object((1,3,6,1,4,1,30065,3,13,1,10,1,2),_AristaQosPolicerPktsSent_Type())
aristaQosPolicerPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaQosPolicerPktsSent.setStatus(_A)
_AristaQosMibConformance_ObjectIdentity=ObjectIdentity
aristaQosMibConformance=_AristaQosMibConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,13,2))
_AristaQosMibCompliances_ObjectIdentity=ObjectIdentity
aristaQosMibCompliances=_AristaQosMibCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,13,2,1))
_AristaQosMibGroups_ObjectIdentity=ObjectIdentity
aristaQosMibGroups=_AristaQosMibGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,13,2,2))
aristaClassMapGroup=ObjectGroup((1,3,6,1,4,1,30065,3,13,2,2,1))
aristaClassMapGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:aristaClassMapGroup.setStatus(_A)
aristaPolicyMapGroup=ObjectGroup((1,3,6,1,4,1,30065,3,13,2,2,2))
aristaPolicyMapGroup.setObjects((_B,_f))
if mibBuilder.loadTexts:aristaPolicyMapGroup.setStatus(_A)
aristaPolicyMapActionGroup=ObjectGroup((1,3,6,1,4,1,30065,3,13,2,2,3))
aristaPolicyMapActionGroup.setObjects(*((_B,_g),(_B,_h)))
if mibBuilder.loadTexts:aristaPolicyMapActionGroup.setStatus(_A)
aristaServicePolicyGroup=ObjectGroup((1,3,6,1,4,1,30065,3,13,2,2,4))
aristaServicePolicyGroup.setObjects(*((_B,_i),(_B,_j)))
if mibBuilder.loadTexts:aristaServicePolicyGroup.setStatus(_A)
aristaEcnCounterGroup=ObjectGroup((1,3,6,1,4,1,30065,3,13,2,2,5))
aristaEcnCounterGroup.setObjects(*((_B,_k),(_B,_l)))
if mibBuilder.loadTexts:aristaEcnCounterGroup.setStatus(_A)
aristaEcnQueueCounterGroup=ObjectGroup((1,3,6,1,4,1,30065,3,13,2,2,6))
aristaEcnQueueCounterGroup.setObjects(*((_B,_m),(_B,_n)))
if mibBuilder.loadTexts:aristaEcnQueueCounterGroup.setStatus(_A)
aristaQosMibCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,13,2,1,1))
aristaQosMibCompliance.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:aristaQosMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AristaQosMapType':AristaQosMapType,'AristaQosShortId':AristaQosShortId,'aristaQosMib':aristaQosMib,'aristaQosMibObjects':aristaQosMibObjects,'aristaClassMapTable':aristaClassMapTable,'aristaClassMapEntry':aristaClassMapEntry,_F:aristaClassMapId,_K:aristaClassMapType,_S:aristaClassMapName,_T:aristaClassMapMatchCondition,'aristaClassMapMatchTable':aristaClassMapMatchTable,'aristaClassMapMatchEntry':aristaClassMapMatchEntry,_M:aristaClassMapMatchIndex,_U:aristaClassMapMatchType,_V:aristaClassMapMatchName,'aristaPolicyMapTable':aristaPolicyMapTable,'aristaPolicyMapEntry':aristaPolicyMapEntry,_G:aristaPolicyMapId,_H:aristaPolicyMapType,_f:aristaPolicyMapName,'aristaPolicyMapClassTable':aristaPolicyMapClassTable,'aristaPolicyMapClassEntry':aristaPolicyMapClassEntry,_N:aristaPolicyMapClassIndex,_W:aristaPolicyMapClassId,'aristaPolicyMapActionTable':aristaPolicyMapActionTable,'aristaPolicyMapActionEntry':aristaPolicyMapActionEntry,_O:aristaPolicyMapActionType,_g:aristaPolicyMapActionRateUnit,_h:aristaPolicyMapActionValue,'aristaServicePolicyTable':aristaServicePolicyTable,'aristaServicePolicyEntry':aristaServicePolicyEntry,_L:aristaServicePolicyIfIndex,_J:aristaServicePolicyDirection,_i:aristaServicePolicyMapId,_j:aristaServicePolicyMapType,'aristaQosStatsTable':aristaQosStatsTable,'aristaQosStatsEntry':aristaQosStatsEntry,_X:aristaQosPktsDropped,_Z:aristaQosPktsSent,_Y:aristaQosPktsMatched,_c:aristaQosBytesDropped,_e:aristaQosBytesSent,_d:aristaQosBytesMatched,'aristaEcnCounterTable':aristaEcnCounterTable,'aristaEcnCounterEntry':aristaEcnCounterEntry,_P:aristaEcnCounterDescriptor,_k:aristaEcnCounterValue,_l:aristaEcnCounterEntity,'aristaEcnQueueCounterTable':aristaEcnQueueCounterTable,'aristaEcnQueueCounterEntry':aristaEcnQueueCounterEntry,_Q:aristaEcnIfIndex,_R:aristaEcnEgressQueueIndex,_m:aristaEcnQueueCounterEnabled,_n:aristaEcnQueuePktsMarked,'aristaQosPolicerStatsTable':aristaQosPolicerStatsTable,'aristaQosPolicerStatsEntry':aristaQosPolicerStatsEntry,_a:aristaQosPolicerPktsDropped,_b:aristaQosPolicerPktsSent,'aristaQosMibConformance':aristaQosMibConformance,'aristaQosMibCompliances':aristaQosMibCompliances,'aristaQosMibCompliance':aristaQosMibCompliance,'aristaQosMibGroups':aristaQosMibGroups,_o:aristaClassMapGroup,_p:aristaPolicyMapGroup,_q:aristaPolicyMapActionGroup,_r:aristaServicePolicyGroup,_s:aristaEcnCounterGroup,_t:aristaEcnQueueCounterGroup})