_S='extremeClearflowPortName'
_R='extremeClearflowVlanName'
_Q='extremeClearflowRuleInterval'
_P='extremeClearflowRuleThreshold'
_O='extremeClearflowRuleValue'
_N='extremeClearflowRuleName'
_M='extremeClearflowPolicyName'
_L='extremeClearflowMsg'
_K='extremeClearflowMsgId'
_J='extremeUtilTrafficQueueName'
_I='extremeTrafficQueueName'
_H='extremeAclPortIfIndex'
_G='extremeAclVlanIfIndex'
_F='Integer32'
_E='accessible-for-notify'
_D='DisplayString'
_C='EXTREME-CLEARFLOW-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
extremeClearflow=ModuleIdentity((1,3,6,1,4,1,1916,1,30))
_ExtremeClearflowTraps_ObjectIdentity=ObjectIdentity
extremeClearflowTraps=_ExtremeClearflowTraps_ObjectIdentity((1,3,6,1,4,1,1916,1,30,0))
_ExtremeClearflowTrapsPrefix_ObjectIdentity=ObjectIdentity
extremeClearflowTrapsPrefix=_ExtremeClearflowTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,1916,1,30,0,0))
_ExtremeClearflowMsgId_Type=Unsigned32
_ExtremeClearflowMsgId_Object=MibScalar
extremeClearflowMsgId=_ExtremeClearflowMsgId_Object((1,3,6,1,4,1,1916,1,30,1),_ExtremeClearflowMsgId_Type())
extremeClearflowMsgId.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeClearflowMsgId.setStatus(_A)
class _ExtremeClearflowMsg_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_ExtremeClearflowMsg_Type.__name__=_D
_ExtremeClearflowMsg_Object=MibScalar
extremeClearflowMsg=_ExtremeClearflowMsg_Object((1,3,6,1,4,1,1916,1,30,2),_ExtremeClearflowMsg_Type())
extremeClearflowMsg.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeClearflowMsg.setStatus(_A)
class _ExtremeClearflowPolicyName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ExtremeClearflowPolicyName_Type.__name__=_D
_ExtremeClearflowPolicyName_Object=MibScalar
extremeClearflowPolicyName=_ExtremeClearflowPolicyName_Object((1,3,6,1,4,1,1916,1,30,3),_ExtremeClearflowPolicyName_Type())
extremeClearflowPolicyName.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeClearflowPolicyName.setStatus(_A)
class _ExtremeClearflowRuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ExtremeClearflowRuleName_Type.__name__=_D
_ExtremeClearflowRuleName_Object=MibScalar
extremeClearflowRuleName=_ExtremeClearflowRuleName_Object((1,3,6,1,4,1,1916,1,30,4),_ExtremeClearflowRuleName_Type())
extremeClearflowRuleName.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeClearflowRuleName.setStatus(_A)
_ExtremeClearflowRuleValue_Type=Counter64
_ExtremeClearflowRuleValue_Object=MibScalar
extremeClearflowRuleValue=_ExtremeClearflowRuleValue_Object((1,3,6,1,4,1,1916,1,30,5),_ExtremeClearflowRuleValue_Type())
extremeClearflowRuleValue.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeClearflowRuleValue.setStatus(_A)
_ExtremeClearflowRuleThreshold_Type=Counter64
_ExtremeClearflowRuleThreshold_Object=MibScalar
extremeClearflowRuleThreshold=_ExtremeClearflowRuleThreshold_Object((1,3,6,1,4,1,1916,1,30,6),_ExtremeClearflowRuleThreshold_Type())
extremeClearflowRuleThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeClearflowRuleThreshold.setStatus(_A)
_ExtremeClearflowRuleInterval_Type=Unsigned32
_ExtremeClearflowRuleInterval_Object=MibScalar
extremeClearflowRuleInterval=_ExtremeClearflowRuleInterval_Object((1,3,6,1,4,1,1916,1,30,7),_ExtremeClearflowRuleInterval_Type())
extremeClearflowRuleInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeClearflowRuleInterval.setStatus(_A)
class _ExtremeClearflowVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ExtremeClearflowVlanName_Type.__name__=_D
_ExtremeClearflowVlanName_Object=MibScalar
extremeClearflowVlanName=_ExtremeClearflowVlanName_Object((1,3,6,1,4,1,1916,1,30,8),_ExtremeClearflowVlanName_Type())
extremeClearflowVlanName.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeClearflowVlanName.setStatus(_A)
class _ExtremeClearflowPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ExtremeClearflowPortName_Type.__name__=_D
_ExtremeClearflowPortName_Object=MibScalar
extremeClearflowPortName=_ExtremeClearflowPortName_Object((1,3,6,1,4,1,1916,1,30,9),_ExtremeClearflowPortName_Type())
extremeClearflowPortName.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeClearflowPortName.setStatus(_A)
_ExtremeAclListTable_Object=MibTable
extremeAclListTable=_ExtremeAclListTable_Object((1,3,6,1,4,1,1916,1,30,10))
if mibBuilder.loadTexts:extremeAclListTable.setStatus(_A)
_ExtremeAclListEntry_Object=MibTableRow
extremeAclListEntry=_ExtremeAclListEntry_Object((1,3,6,1,4,1,1916,1,30,10,1))
extremeAclListEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:extremeAclListEntry.setStatus(_A)
class _ExtremeAclPortIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeAclPortIfIndex_Type.__name__=_F
_ExtremeAclPortIfIndex_Object=MibTableColumn
extremeAclPortIfIndex=_ExtremeAclPortIfIndex_Object((1,3,6,1,4,1,1916,1,30,10,1,1),_ExtremeAclPortIfIndex_Type())
extremeAclPortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeAclPortIfIndex.setStatus(_A)
_ExtremeAclVlanIfIndex_Type=Integer32
_ExtremeAclVlanIfIndex_Object=MibTableColumn
extremeAclVlanIfIndex=_ExtremeAclVlanIfIndex_Object((1,3,6,1,4,1,1916,1,30,10,1,2),_ExtremeAclVlanIfIndex_Type())
extremeAclVlanIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeAclVlanIfIndex.setStatus(_A)
class _ExtremeAclCounterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_ExtremeAclCounterName_Type.__name__=_D
_ExtremeAclCounterName_Object=MibTableColumn
extremeAclCounterName=_ExtremeAclCounterName_Object((1,3,6,1,4,1,1916,1,30,10,1,3),_ExtremeAclCounterName_Type())
extremeAclCounterName.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeAclCounterName.setStatus(_A)
class _ExtremeAclVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ExtremeAclVlanName_Type.__name__=_D
_ExtremeAclVlanName_Object=MibTableColumn
extremeAclVlanName=_ExtremeAclVlanName_Object((1,3,6,1,4,1,1916,1,30,10,1,4),_ExtremeAclVlanName_Type())
extremeAclVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeAclVlanName.setStatus(_A)
_ExtremeAclPolicyName_Type=DisplayString
_ExtremeAclPolicyName_Object=MibTableColumn
extremeAclPolicyName=_ExtremeAclPolicyName_Object((1,3,6,1,4,1,1916,1,30,10,1,5),_ExtremeAclPolicyName_Type())
extremeAclPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeAclPolicyName.setStatus(_A)
_ExtremeAclDirection_Type=Integer32
_ExtremeAclDirection_Object=MibTableColumn
extremeAclDirection=_ExtremeAclDirection_Object((1,3,6,1,4,1,1916,1,30,10,1,6),_ExtremeAclDirection_Type())
extremeAclDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeAclDirection.setStatus(_A)
_ExtremeAclPktCount_Type=Counter64
_ExtremeAclPktCount_Object=MibTableColumn
extremeAclPktCount=_ExtremeAclPktCount_Object((1,3,6,1,4,1,1916,1,30,10,1,7),_ExtremeAclPktCount_Type())
extremeAclPktCount.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeAclPktCount.setStatus(_A)
_ExtremeAclByteCount_Type=Counter64
_ExtremeAclByteCount_Object=MibTableColumn
extremeAclByteCount=_ExtremeAclByteCount_Object((1,3,6,1,4,1,1916,1,30,10,1,8),_ExtremeAclByteCount_Type())
extremeAclByteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeAclByteCount.setStatus(_A)
_ExtremeTrafficQueueStatsTable_Object=MibTable
extremeTrafficQueueStatsTable=_ExtremeTrafficQueueStatsTable_Object((1,3,6,1,4,1,1916,1,30,11))
if mibBuilder.loadTexts:extremeTrafficQueueStatsTable.setStatus(_A)
_ExtremeTrafficQueueStatsTableEntry_Object=MibTableRow
extremeTrafficQueueStatsTableEntry=_ExtremeTrafficQueueStatsTableEntry_Object((1,3,6,1,4,1,1916,1,30,11,1))
extremeTrafficQueueStatsTableEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:extremeTrafficQueueStatsTableEntry.setStatus(_A)
class _ExtremeTrafficQueueName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_ExtremeTrafficQueueName_Type.__name__=_D
_ExtremeTrafficQueueName_Object=MibTableColumn
extremeTrafficQueueName=_ExtremeTrafficQueueName_Object((1,3,6,1,4,1,1916,1,30,11,1,1),_ExtremeTrafficQueueName_Type())
extremeTrafficQueueName.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTrafficQueueName.setStatus(_A)
_ExtremeTrafficQueueDirection_Type=Integer32
_ExtremeTrafficQueueDirection_Object=MibTableColumn
extremeTrafficQueueDirection=_ExtremeTrafficQueueDirection_Object((1,3,6,1,4,1,1916,1,30,11,1,2),_ExtremeTrafficQueueDirection_Type())
extremeTrafficQueueDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTrafficQueueDirection.setStatus(_A)
_ExtremeTrafficQueueHighPassedPkts_Type=Counter64
_ExtremeTrafficQueueHighPassedPkts_Object=MibTableColumn
extremeTrafficQueueHighPassedPkts=_ExtremeTrafficQueueHighPassedPkts_Object((1,3,6,1,4,1,1916,1,30,11,1,3),_ExtremeTrafficQueueHighPassedPkts_Type())
extremeTrafficQueueHighPassedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTrafficQueueHighPassedPkts.setStatus(_A)
_ExtremeTrafficQueueHighPassedBytes_Type=Counter64
_ExtremeTrafficQueueHighPassedBytes_Object=MibTableColumn
extremeTrafficQueueHighPassedBytes=_ExtremeTrafficQueueHighPassedBytes_Object((1,3,6,1,4,1,1916,1,30,11,1,4),_ExtremeTrafficQueueHighPassedBytes_Type())
extremeTrafficQueueHighPassedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTrafficQueueHighPassedBytes.setStatus(_A)
_ExtremeTrafficQueueHighDroppedPkts_Type=Counter64
_ExtremeTrafficQueueHighDroppedPkts_Object=MibTableColumn
extremeTrafficQueueHighDroppedPkts=_ExtremeTrafficQueueHighDroppedPkts_Object((1,3,6,1,4,1,1916,1,30,11,1,5),_ExtremeTrafficQueueHighDroppedPkts_Type())
extremeTrafficQueueHighDroppedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTrafficQueueHighDroppedPkts.setStatus(_A)
_ExtremeTrafficQueueHighDroppedBytes_Type=Counter64
_ExtremeTrafficQueueHighDroppedBytes_Object=MibTableColumn
extremeTrafficQueueHighDroppedBytes=_ExtremeTrafficQueueHighDroppedBytes_Object((1,3,6,1,4,1,1916,1,30,11,1,6),_ExtremeTrafficQueueHighDroppedBytes_Type())
extremeTrafficQueueHighDroppedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTrafficQueueHighDroppedBytes.setStatus(_A)
_ExtremeTrafficQueueMedPassedPkts_Type=Counter64
_ExtremeTrafficQueueMedPassedPkts_Object=MibTableColumn
extremeTrafficQueueMedPassedPkts=_ExtremeTrafficQueueMedPassedPkts_Object((1,3,6,1,4,1,1916,1,30,11,1,7),_ExtremeTrafficQueueMedPassedPkts_Type())
extremeTrafficQueueMedPassedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTrafficQueueMedPassedPkts.setStatus(_A)
_ExtremeTrafficQueueMedPassedBytes_Type=Counter64
_ExtremeTrafficQueueMedPassedBytes_Object=MibTableColumn
extremeTrafficQueueMedPassedBytes=_ExtremeTrafficQueueMedPassedBytes_Object((1,3,6,1,4,1,1916,1,30,11,1,8),_ExtremeTrafficQueueMedPassedBytes_Type())
extremeTrafficQueueMedPassedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTrafficQueueMedPassedBytes.setStatus(_A)
_ExtremeTrafficQueueMedDroppedPkts_Type=Counter64
_ExtremeTrafficQueueMedDroppedPkts_Object=MibTableColumn
extremeTrafficQueueMedDroppedPkts=_ExtremeTrafficQueueMedDroppedPkts_Object((1,3,6,1,4,1,1916,1,30,11,1,9),_ExtremeTrafficQueueMedDroppedPkts_Type())
extremeTrafficQueueMedDroppedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTrafficQueueMedDroppedPkts.setStatus(_A)
_ExtremeTrafficQueueMedDroppedBytes_Type=Counter64
_ExtremeTrafficQueueMedDroppedBytes_Object=MibTableColumn
extremeTrafficQueueMedDroppedBytes=_ExtremeTrafficQueueMedDroppedBytes_Object((1,3,6,1,4,1,1916,1,30,11,1,10),_ExtremeTrafficQueueMedDroppedBytes_Type())
extremeTrafficQueueMedDroppedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTrafficQueueMedDroppedBytes.setStatus(_A)
_ExtremeTrafficQueueLowPassedPkts_Type=Counter64
_ExtremeTrafficQueueLowPassedPkts_Object=MibTableColumn
extremeTrafficQueueLowPassedPkts=_ExtremeTrafficQueueLowPassedPkts_Object((1,3,6,1,4,1,1916,1,30,11,1,11),_ExtremeTrafficQueueLowPassedPkts_Type())
extremeTrafficQueueLowPassedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTrafficQueueLowPassedPkts.setStatus(_A)
_ExtremeTrafficQueueLowPassedBytes_Type=Counter64
_ExtremeTrafficQueueLowPassedBytes_Object=MibTableColumn
extremeTrafficQueueLowPassedBytes=_ExtremeTrafficQueueLowPassedBytes_Object((1,3,6,1,4,1,1916,1,30,11,1,12),_ExtremeTrafficQueueLowPassedBytes_Type())
extremeTrafficQueueLowPassedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTrafficQueueLowPassedBytes.setStatus(_A)
_ExtremeTrafficQueueLowDroppedPkts_Type=Counter64
_ExtremeTrafficQueueLowDroppedPkts_Object=MibTableColumn
extremeTrafficQueueLowDroppedPkts=_ExtremeTrafficQueueLowDroppedPkts_Object((1,3,6,1,4,1,1916,1,30,11,1,13),_ExtremeTrafficQueueLowDroppedPkts_Type())
extremeTrafficQueueLowDroppedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTrafficQueueLowDroppedPkts.setStatus(_A)
_ExtremeTrafficQueueLowDroppedBytes_Type=Counter64
_ExtremeTrafficQueueLowDroppedBytes_Object=MibTableColumn
extremeTrafficQueueLowDroppedBytes=_ExtremeTrafficQueueLowDroppedBytes_Object((1,3,6,1,4,1,1916,1,30,11,1,14),_ExtremeTrafficQueueLowDroppedBytes_Type())
extremeTrafficQueueLowDroppedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTrafficQueueLowDroppedBytes.setStatus(_A)
_ExtremeTrafficQueueAggPassedPkts_Type=Counter64
_ExtremeTrafficQueueAggPassedPkts_Object=MibTableColumn
extremeTrafficQueueAggPassedPkts=_ExtremeTrafficQueueAggPassedPkts_Object((1,3,6,1,4,1,1916,1,30,11,1,15),_ExtremeTrafficQueueAggPassedPkts_Type())
extremeTrafficQueueAggPassedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTrafficQueueAggPassedPkts.setStatus(_A)
_ExtremeTrafficQueueAggPassedBytes_Type=Counter64
_ExtremeTrafficQueueAggPassedBytes_Object=MibTableColumn
extremeTrafficQueueAggPassedBytes=_ExtremeTrafficQueueAggPassedBytes_Object((1,3,6,1,4,1,1916,1,30,11,1,16),_ExtremeTrafficQueueAggPassedBytes_Type())
extremeTrafficQueueAggPassedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTrafficQueueAggPassedBytes.setStatus(_A)
_ExtremeTrafficQueueAggDroppedPkts_Type=Counter64
_ExtremeTrafficQueueAggDroppedPkts_Object=MibTableColumn
extremeTrafficQueueAggDroppedPkts=_ExtremeTrafficQueueAggDroppedPkts_Object((1,3,6,1,4,1,1916,1,30,11,1,17),_ExtremeTrafficQueueAggDroppedPkts_Type())
extremeTrafficQueueAggDroppedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTrafficQueueAggDroppedPkts.setStatus(_A)
_ExtremeTrafficQueueAggDroppedBytes_Type=Counter64
_ExtremeTrafficQueueAggDroppedBytes_Object=MibTableColumn
extremeTrafficQueueAggDroppedBytes=_ExtremeTrafficQueueAggDroppedBytes_Object((1,3,6,1,4,1,1916,1,30,11,1,18),_ExtremeTrafficQueueAggDroppedBytes_Type())
extremeTrafficQueueAggDroppedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTrafficQueueAggDroppedBytes.setStatus(_A)
_ExtremeTrafficQueueUtilTable_Object=MibTable
extremeTrafficQueueUtilTable=_ExtremeTrafficQueueUtilTable_Object((1,3,6,1,4,1,1916,1,30,12))
if mibBuilder.loadTexts:extremeTrafficQueueUtilTable.setStatus(_A)
_ExtremeTrafficQueueUtilTableEntry_Object=MibTableRow
extremeTrafficQueueUtilTableEntry=_ExtremeTrafficQueueUtilTableEntry_Object((1,3,6,1,4,1,1916,1,30,12,1))
extremeTrafficQueueUtilTableEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:extremeTrafficQueueUtilTableEntry.setStatus(_A)
class _ExtremeUtilTrafficQueueName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,33))
_ExtremeUtilTrafficQueueName_Type.__name__=_D
_ExtremeUtilTrafficQueueName_Object=MibTableColumn
extremeUtilTrafficQueueName=_ExtremeUtilTrafficQueueName_Object((1,3,6,1,4,1,1916,1,30,12,1,1),_ExtremeUtilTrafficQueueName_Type())
extremeUtilTrafficQueueName.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeUtilTrafficQueueName.setStatus(_A)
_ExtremeUtilTrafficQueueDirection_Type=Integer32
_ExtremeUtilTrafficQueueDirection_Object=MibTableColumn
extremeUtilTrafficQueueDirection=_ExtremeUtilTrafficQueueDirection_Object((1,3,6,1,4,1,1916,1,30,12,1,2),_ExtremeUtilTrafficQueueDirection_Type())
extremeUtilTrafficQueueDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeUtilTrafficQueueDirection.setStatus(_A)
_ExtremeTrafficQueueHighUtilization_Type=DisplayString
_ExtremeTrafficQueueHighUtilization_Object=MibTableColumn
extremeTrafficQueueHighUtilization=_ExtremeTrafficQueueHighUtilization_Object((1,3,6,1,4,1,1916,1,30,12,1,3),_ExtremeTrafficQueueHighUtilization_Type())
extremeTrafficQueueHighUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTrafficQueueHighUtilization.setStatus(_A)
_ExtremeTrafficQueueMedUtilization_Type=DisplayString
_ExtremeTrafficQueueMedUtilization_Object=MibTableColumn
extremeTrafficQueueMedUtilization=_ExtremeTrafficQueueMedUtilization_Object((1,3,6,1,4,1,1916,1,30,12,1,4),_ExtremeTrafficQueueMedUtilization_Type())
extremeTrafficQueueMedUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTrafficQueueMedUtilization.setStatus(_A)
_ExtremeTrafficQueueLowUtilization_Type=DisplayString
_ExtremeTrafficQueueLowUtilization_Object=MibTableColumn
extremeTrafficQueueLowUtilization=_ExtremeTrafficQueueLowUtilization_Object((1,3,6,1,4,1,1916,1,30,12,1,5),_ExtremeTrafficQueueLowUtilization_Type())
extremeTrafficQueueLowUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeTrafficQueueLowUtilization.setStatus(_A)
extremeClearflowMessage=NotificationType((1,3,6,1,4,1,1916,1,30,0,0,1))
extremeClearflowMessage.setObjects(*((_C,_K),(_C,_L),(_C,_M),(_C,_N),(_C,_O),(_C,_P),(_C,_Q),(_C,_R),(_C,_S)))
if mibBuilder.loadTexts:extremeClearflowMessage.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'extremeClearflow':extremeClearflow,'extremeClearflowTraps':extremeClearflowTraps,'extremeClearflowTrapsPrefix':extremeClearflowTrapsPrefix,'extremeClearflowMessage':extremeClearflowMessage,_K:extremeClearflowMsgId,_L:extremeClearflowMsg,_M:extremeClearflowPolicyName,_N:extremeClearflowRuleName,_O:extremeClearflowRuleValue,_P:extremeClearflowRuleThreshold,_Q:extremeClearflowRuleInterval,_R:extremeClearflowVlanName,_S:extremeClearflowPortName,'extremeAclListTable':extremeAclListTable,'extremeAclListEntry':extremeAclListEntry,_H:extremeAclPortIfIndex,_G:extremeAclVlanIfIndex,'extremeAclCounterName':extremeAclCounterName,'extremeAclVlanName':extremeAclVlanName,'extremeAclPolicyName':extremeAclPolicyName,'extremeAclDirection':extremeAclDirection,'extremeAclPktCount':extremeAclPktCount,'extremeAclByteCount':extremeAclByteCount,'extremeTrafficQueueStatsTable':extremeTrafficQueueStatsTable,'extremeTrafficQueueStatsTableEntry':extremeTrafficQueueStatsTableEntry,_I:extremeTrafficQueueName,'extremeTrafficQueueDirection':extremeTrafficQueueDirection,'extremeTrafficQueueHighPassedPkts':extremeTrafficQueueHighPassedPkts,'extremeTrafficQueueHighPassedBytes':extremeTrafficQueueHighPassedBytes,'extremeTrafficQueueHighDroppedPkts':extremeTrafficQueueHighDroppedPkts,'extremeTrafficQueueHighDroppedBytes':extremeTrafficQueueHighDroppedBytes,'extremeTrafficQueueMedPassedPkts':extremeTrafficQueueMedPassedPkts,'extremeTrafficQueueMedPassedBytes':extremeTrafficQueueMedPassedBytes,'extremeTrafficQueueMedDroppedPkts':extremeTrafficQueueMedDroppedPkts,'extremeTrafficQueueMedDroppedBytes':extremeTrafficQueueMedDroppedBytes,'extremeTrafficQueueLowPassedPkts':extremeTrafficQueueLowPassedPkts,'extremeTrafficQueueLowPassedBytes':extremeTrafficQueueLowPassedBytes,'extremeTrafficQueueLowDroppedPkts':extremeTrafficQueueLowDroppedPkts,'extremeTrafficQueueLowDroppedBytes':extremeTrafficQueueLowDroppedBytes,'extremeTrafficQueueAggPassedPkts':extremeTrafficQueueAggPassedPkts,'extremeTrafficQueueAggPassedBytes':extremeTrafficQueueAggPassedBytes,'extremeTrafficQueueAggDroppedPkts':extremeTrafficQueueAggDroppedPkts,'extremeTrafficQueueAggDroppedBytes':extremeTrafficQueueAggDroppedBytes,'extremeTrafficQueueUtilTable':extremeTrafficQueueUtilTable,'extremeTrafficQueueUtilTableEntry':extremeTrafficQueueUtilTableEntry,_J:extremeUtilTrafficQueueName,'extremeUtilTrafficQueueDirection':extremeUtilTrafficQueueDirection,'extremeTrafficQueueHighUtilization':extremeTrafficQueueHighUtilization,'extremeTrafficQueueMedUtilization':extremeTrafficQueueMedUtilization,'extremeTrafficQueueLowUtilization':extremeTrafficQueueLowUtilization})