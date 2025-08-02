_a='qAtmIfIndexVpiVciEntryGroup'
_Z='dot1qAggregateGroup'
_Y='dot1qPortGroup'
_X='qAtmIfIndexVpiVciForceTagInternal'
_W='qAtmIfIndexVpiVciAcceptableFrameTypes'
_V='qAtmIfIndexVpiVciVlanDescription'
_U='qAtmIfIndexVpiVciVlanAction'
_T='qAggregateVlanDescription'
_S='qAggregateVlanStatus'
_R='qPortVlanForceTagInternal'
_Q='qPortVlanDescription'
_P='qPortVlanStatus'
_O='qAtmIfIndexVpiVciVlanTagValue'
_N='qAtmVciValue'
_M='qAtmVpiValue'
_L='qAtmIfIndex'
_K='qAggregateVlanTagValue'
_J='qAggregateVlanAggregateId'
_I='qPortVlanTagValue'
_H='qPortVlanPort'
_G='qPortVlanSlot'
_F='DisplayString'
_E='read-create'
_D='read-write'
_C='Integer32'
_B='ALCATEL-IND1-DOT1Q-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1Dot1Q,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1Dot1Q')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
alcatelIND1Dot1QMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,21,1))
if mibBuilder.loadTexts:alcatelIND1Dot1QMIB.setRevisions(('2007-04-03 00:00',))
_AlcatelIND1Dot1QMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1Dot1QMIBObjects=_AlcatelIND1Dot1QMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,21,1,1))
if mibBuilder.loadTexts:alcatelIND1Dot1QMIBObjects.setStatus(_A)
_V8021Q_ObjectIdentity=ObjectIdentity
v8021Q=_V8021Q_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1))
_QPortVlanTable_Object=MibTable
qPortVlanTable=_QPortVlanTable_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,1))
if mibBuilder.loadTexts:qPortVlanTable.setStatus(_A)
_QPortVlanEntry_Object=MibTableRow
qPortVlanEntry=_QPortVlanEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,1,1))
qPortVlanEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:qPortVlanEntry.setStatus(_A)
class _QPortVlanSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_QPortVlanSlot_Type.__name__=_C
_QPortVlanSlot_Object=MibTableColumn
qPortVlanSlot=_QPortVlanSlot_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,1,1,1),_QPortVlanSlot_Type())
qPortVlanSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:qPortVlanSlot.setStatus(_A)
class _QPortVlanPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_QPortVlanPort_Type.__name__=_C
_QPortVlanPort_Object=MibTableColumn
qPortVlanPort=_QPortVlanPort_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,1,1,2),_QPortVlanPort_Type())
qPortVlanPort.setMaxAccess(_D)
if mibBuilder.loadTexts:qPortVlanPort.setStatus(_A)
class _QPortVlanTagValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_QPortVlanTagValue_Type.__name__=_C
_QPortVlanTagValue_Object=MibTableColumn
qPortVlanTagValue=_QPortVlanTagValue_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,1,1,3),_QPortVlanTagValue_Type())
qPortVlanTagValue.setMaxAccess(_D)
if mibBuilder.loadTexts:qPortVlanTagValue.setStatus(_A)
_QPortVlanStatus_Type=RowStatus
_QPortVlanStatus_Object=MibTableColumn
qPortVlanStatus=_QPortVlanStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,1,1,4),_QPortVlanStatus_Type())
qPortVlanStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:qPortVlanStatus.setStatus(_A)
class _QPortVlanDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QPortVlanDescription_Type.__name__=_F
_QPortVlanDescription_Object=MibTableColumn
qPortVlanDescription=_QPortVlanDescription_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,1,1,5),_QPortVlanDescription_Type())
qPortVlanDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:qPortVlanDescription.setStatus(_A)
class _QPortVlanForceTagInternal_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('off',0),('on',1),('na',2)))
_QPortVlanForceTagInternal_Type.__name__=_C
_QPortVlanForceTagInternal_Object=MibTableColumn
qPortVlanForceTagInternal=_QPortVlanForceTagInternal_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,1,1,6),_QPortVlanForceTagInternal_Type())
qPortVlanForceTagInternal.setMaxAccess(_E)
if mibBuilder.loadTexts:qPortVlanForceTagInternal.setStatus(_A)
_QAggregateVlanTable_Object=MibTable
qAggregateVlanTable=_QAggregateVlanTable_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,2))
if mibBuilder.loadTexts:qAggregateVlanTable.setStatus(_A)
_QAggregateVlanEntry_Object=MibTableRow
qAggregateVlanEntry=_QAggregateVlanEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,2,1))
qAggregateVlanEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:qAggregateVlanEntry.setStatus(_A)
class _QAggregateVlanAggregateId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_QAggregateVlanAggregateId_Type.__name__=_C
_QAggregateVlanAggregateId_Object=MibTableColumn
qAggregateVlanAggregateId=_QAggregateVlanAggregateId_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,2,1,1),_QAggregateVlanAggregateId_Type())
qAggregateVlanAggregateId.setMaxAccess(_D)
if mibBuilder.loadTexts:qAggregateVlanAggregateId.setStatus(_A)
class _QAggregateVlanTagValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_QAggregateVlanTagValue_Type.__name__=_C
_QAggregateVlanTagValue_Object=MibTableColumn
qAggregateVlanTagValue=_QAggregateVlanTagValue_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,2,1,2),_QAggregateVlanTagValue_Type())
qAggregateVlanTagValue.setMaxAccess(_D)
if mibBuilder.loadTexts:qAggregateVlanTagValue.setStatus(_A)
_QAggregateVlanStatus_Type=RowStatus
_QAggregateVlanStatus_Object=MibTableColumn
qAggregateVlanStatus=_QAggregateVlanStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,2,1,3),_QAggregateVlanStatus_Type())
qAggregateVlanStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:qAggregateVlanStatus.setStatus(_A)
class _QAggregateVlanDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QAggregateVlanDescription_Type.__name__=_F
_QAggregateVlanDescription_Object=MibTableColumn
qAggregateVlanDescription=_QAggregateVlanDescription_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,2,1,4),_QAggregateVlanDescription_Type())
qAggregateVlanDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:qAggregateVlanDescription.setStatus(_A)
_QAtmIfIndexVpiVciTable_Object=MibTable
qAtmIfIndexVpiVciTable=_QAtmIfIndexVpiVciTable_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,3))
if mibBuilder.loadTexts:qAtmIfIndexVpiVciTable.setStatus(_A)
_QAtmIfIndexVpiVciEntry_Object=MibTableRow
qAtmIfIndexVpiVciEntry=_QAtmIfIndexVpiVciEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,3,1))
qAtmIfIndexVpiVciEntry.setIndexNames((0,_B,_L),(0,_B,_M),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:qAtmIfIndexVpiVciEntry.setStatus(_A)
class _QAtmIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4259841,2147483647))
_QAtmIfIndex_Type.__name__=_C
_QAtmIfIndex_Object=MibTableColumn
qAtmIfIndex=_QAtmIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,3,1,1),_QAtmIfIndex_Type())
qAtmIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qAtmIfIndex.setStatus(_A)
class _QAtmVpiValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_QAtmVpiValue_Type.__name__=_C
_QAtmVpiValue_Object=MibTableColumn
qAtmVpiValue=_QAtmVpiValue_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,3,1,2),_QAtmVpiValue_Type())
qAtmVpiValue.setMaxAccess(_D)
if mibBuilder.loadTexts:qAtmVpiValue.setStatus(_A)
class _QAtmVciValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_QAtmVciValue_Type.__name__=_C
_QAtmVciValue_Object=MibTableColumn
qAtmVciValue=_QAtmVciValue_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,3,1,3),_QAtmVciValue_Type())
qAtmVciValue.setMaxAccess(_D)
if mibBuilder.loadTexts:qAtmVciValue.setStatus(_A)
class _QAtmIfIndexVpiVciVlanTagValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_QAtmIfIndexVpiVciVlanTagValue_Type.__name__=_C
_QAtmIfIndexVpiVciVlanTagValue_Object=MibTableColumn
qAtmIfIndexVpiVciVlanTagValue=_QAtmIfIndexVpiVciVlanTagValue_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,3,1,4),_QAtmIfIndexVpiVciVlanTagValue_Type())
qAtmIfIndexVpiVciVlanTagValue.setMaxAccess(_D)
if mibBuilder.loadTexts:qAtmIfIndexVpiVciVlanTagValue.setStatus(_A)
_QAtmIfIndexVpiVciVlanAction_Type=RowStatus
_QAtmIfIndexVpiVciVlanAction_Object=MibTableColumn
qAtmIfIndexVpiVciVlanAction=_QAtmIfIndexVpiVciVlanAction_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,3,1,5),_QAtmIfIndexVpiVciVlanAction_Type())
qAtmIfIndexVpiVciVlanAction.setMaxAccess(_E)
if mibBuilder.loadTexts:qAtmIfIndexVpiVciVlanAction.setStatus(_A)
class _QAtmIfIndexVpiVciVlanDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QAtmIfIndexVpiVciVlanDescription_Type.__name__=_F
_QAtmIfIndexVpiVciVlanDescription_Object=MibTableColumn
qAtmIfIndexVpiVciVlanDescription=_QAtmIfIndexVpiVciVlanDescription_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,3,1,6),_QAtmIfIndexVpiVciVlanDescription_Type())
qAtmIfIndexVpiVciVlanDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:qAtmIfIndexVpiVciVlanDescription.setStatus(_A)
class _QAtmIfIndexVpiVciAcceptableFrameTypes_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('admitAll',1),('admitOnlyVlanTagged',2)))
_QAtmIfIndexVpiVciAcceptableFrameTypes_Type.__name__=_C
_QAtmIfIndexVpiVciAcceptableFrameTypes_Object=MibTableColumn
qAtmIfIndexVpiVciAcceptableFrameTypes=_QAtmIfIndexVpiVciAcceptableFrameTypes_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,3,1,7),_QAtmIfIndexVpiVciAcceptableFrameTypes_Type())
qAtmIfIndexVpiVciAcceptableFrameTypes.setMaxAccess(_E)
if mibBuilder.loadTexts:qAtmIfIndexVpiVciAcceptableFrameTypes.setStatus(_A)
class _QAtmIfIndexVpiVciForceTagInternal_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('off',0),('on',1),('na',2)))
_QAtmIfIndexVpiVciForceTagInternal_Type.__name__=_C
_QAtmIfIndexVpiVciForceTagInternal_Object=MibTableColumn
qAtmIfIndexVpiVciForceTagInternal=_QAtmIfIndexVpiVciForceTagInternal_Object((1,3,6,1,4,1,6486,800,1,2,1,21,1,1,1,3,1,8),_QAtmIfIndexVpiVciForceTagInternal_Type())
qAtmIfIndexVpiVciForceTagInternal.setMaxAccess(_E)
if mibBuilder.loadTexts:qAtmIfIndexVpiVciForceTagInternal.setStatus(_A)
_AlcatelIND1Dot1QMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1Dot1QMIBConformance=_AlcatelIND1Dot1QMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,21,1,2))
if mibBuilder.loadTexts:alcatelIND1Dot1QMIBConformance.setStatus(_A)
_AlcatelIND1Dot1QMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1Dot1QMIBGroups=_AlcatelIND1Dot1QMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,21,1,2,1))
if mibBuilder.loadTexts:alcatelIND1Dot1QMIBGroups.setStatus(_A)
_AlcatelIND1Dot1QMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1Dot1QMIBCompliances=_AlcatelIND1Dot1QMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,21,1,2,2))
if mibBuilder.loadTexts:alcatelIND1Dot1QMIBCompliances.setStatus(_A)
dot1qPortGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,21,1,2,1,1))
dot1qPortGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:dot1qPortGroup.setStatus(_A)
dot1qAggregateGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,21,1,2,1,2))
dot1qAggregateGroup.setObjects(*((_B,_J),(_B,_K),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:dot1qAggregateGroup.setStatus(_A)
qAtmIfIndexVpiVciEntryGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,21,1,2,1,3))
qAtmIfIndexVpiVciEntryGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:qAtmIfIndexVpiVciEntryGroup.setStatus(_A)
alcatelIND1Dot1QMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,21,1,2,2,1))
alcatelIND1Dot1QMIBCompliance.setObjects(*((_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:alcatelIND1Dot1QMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1Dot1QMIB':alcatelIND1Dot1QMIB,'alcatelIND1Dot1QMIBObjects':alcatelIND1Dot1QMIBObjects,'v8021Q':v8021Q,'qPortVlanTable':qPortVlanTable,'qPortVlanEntry':qPortVlanEntry,_G:qPortVlanSlot,_H:qPortVlanPort,_I:qPortVlanTagValue,_P:qPortVlanStatus,_Q:qPortVlanDescription,_R:qPortVlanForceTagInternal,'qAggregateVlanTable':qAggregateVlanTable,'qAggregateVlanEntry':qAggregateVlanEntry,_J:qAggregateVlanAggregateId,_K:qAggregateVlanTagValue,_S:qAggregateVlanStatus,_T:qAggregateVlanDescription,'qAtmIfIndexVpiVciTable':qAtmIfIndexVpiVciTable,'qAtmIfIndexVpiVciEntry':qAtmIfIndexVpiVciEntry,_L:qAtmIfIndex,_M:qAtmVpiValue,_N:qAtmVciValue,_O:qAtmIfIndexVpiVciVlanTagValue,_U:qAtmIfIndexVpiVciVlanAction,_V:qAtmIfIndexVpiVciVlanDescription,_W:qAtmIfIndexVpiVciAcceptableFrameTypes,_X:qAtmIfIndexVpiVciForceTagInternal,'alcatelIND1Dot1QMIBConformance':alcatelIND1Dot1QMIBConformance,'alcatelIND1Dot1QMIBGroups':alcatelIND1Dot1QMIBGroups,_Y:dot1qPortGroup,_Z:dot1qAggregateGroup,_a:qAtmIfIndexVpiVciEntryGroup,'alcatelIND1Dot1QMIBCompliances':alcatelIND1Dot1QMIBCompliances,'alcatelIND1Dot1QMIBCompliance':alcatelIND1Dot1QMIBCompliance})