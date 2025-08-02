_k='fsMIDot1qFutureUnicastMacLearningLimit'
_j='fsMIDot1qFutureVlanOldTpFdbPort'
_i='fsMIDot1qFutureVlanFid'
_h='fsMIDot1qFutureVlanUnicastMacLimit'
_g='fsMIDot1qFuturePortVlanExtEntry'
_f='fsMIDot1qFutureStVlanExtEntry'
_e='fsMIDot1qFutureStaticUnicastExtnEntry'
_d='fsMIDot1qFutureVlanTpFdbEntry'
_c='fsMIDot1qFutureVlanPortSubnetMapExtMask'
_b='fsMIDot1qFutureVlanPortSubnetMapExtAddr'
_a='fsMIDot1qFutureVlanPortSubnetMapAddr'
_Z='MacLearningStatus'
_Y='fsMIDot1qFutureVlanPortMacMapAddr'
_X='default'
_W='disabled'
_V='enabled'
_U='fsDot1qTpPort'
_T='fsDot1qTpFdbPort'
_S='DisplayString'
_R='VlanIdOrNone'
_Q='OctetString'
_P='fsMIDot1qFutureVlanWildCardMacAddress'
_O='SUPERMICROQ-BRIDGE-MIB'
_N='fsMIDot1qFutureVlanContextName'
_M='fsMIDot1qFutureVlanPort'
_L='fsMIDot1qFutureVlanIndex'
_K='Unsigned32'
_J='not-accessible'
_I='EnabledStatus'
_H='fsMIDot1qFutureVlanContextId'
_G='TruthValue'
_F='Integer32'
_E='deprecated'
_D='SUPERMICRO-MIVlan-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Q,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
VlanIdOrNone,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_R)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_S,'MacAddress','PhysAddress','RowStatus','TextualConvention',_G)
fsDot1qStaticUnicastEntry,fsDot1qTpFdbEntry,fsDot1qTpFdbPort,fsDot1qTpPort,fsDot1qVlanStaticEntry,fsDot1qVlanStaticPortConfigEntry=mibBuilder.importSymbols(_O,'fsDot1qStaticUnicastEntry','fsDot1qTpFdbEntry',_T,_U,'fsDot1qVlanStaticEntry','fsDot1qVlanStaticPortConfigEntry')
futureMIVlanMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,1,120))
if mibBuilder.loadTexts:futureMIVlanMIB.setRevisions(('2012-09-05 00:00',))
class VlanId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_W,2)))
class MacLearningStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3)))
_FsMIDot1qFutureVlan_ObjectIdentity=ObjectIdentity
fsMIDot1qFutureVlan=_FsMIDot1qFutureVlan_ObjectIdentity((1,3,6,1,4,1,10876,101,1,120,1))
_FsMIDot1qFutureVlanGlobalTrace_Type=TruthValue
_FsMIDot1qFutureVlanGlobalTrace_Object=MibScalar
fsMIDot1qFutureVlanGlobalTrace=_FsMIDot1qFutureVlanGlobalTrace_Object((1,3,6,1,4,1,10876,101,1,120,1,1),_FsMIDot1qFutureVlanGlobalTrace_Type())
fsMIDot1qFutureVlanGlobalTrace.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanGlobalTrace.setStatus(_A)
_FsMIDot1qFutureVlanGlobalsTable_Object=MibTable
fsMIDot1qFutureVlanGlobalsTable=_FsMIDot1qFutureVlanGlobalsTable_Object((1,3,6,1,4,1,10876,101,1,120,1,2))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanGlobalsTable.setStatus(_A)
_FsMIDot1qFutureVlanGlobalsEntry_Object=MibTableRow
fsMIDot1qFutureVlanGlobalsEntry=_FsMIDot1qFutureVlanGlobalsEntry_Object((1,3,6,1,4,1,10876,101,1,120,1,2,1))
fsMIDot1qFutureVlanGlobalsEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanGlobalsEntry.setStatus(_A)
class _FsMIDot1qFutureVlanContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIDot1qFutureVlanContextId_Type.__name__=_F
_FsMIDot1qFutureVlanContextId_Object=MibTableColumn
fsMIDot1qFutureVlanContextId=_FsMIDot1qFutureVlanContextId_Object((1,3,6,1,4,1,10876,101,1,120,1,2,1,1),_FsMIDot1qFutureVlanContextId_Type())
fsMIDot1qFutureVlanContextId.setMaxAccess(_J)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanContextId.setStatus(_A)
_FsMIDot1qFutureVlanStatus_Type=EnabledStatus
_FsMIDot1qFutureVlanStatus_Object=MibTableColumn
fsMIDot1qFutureVlanStatus=_FsMIDot1qFutureVlanStatus_Object((1,3,6,1,4,1,10876,101,1,120,1,2,1,2),_FsMIDot1qFutureVlanStatus_Type())
fsMIDot1qFutureVlanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanStatus.setStatus(_A)
_FsMIDot1qFutureVlanMacBasedOnAllPorts_Type=EnabledStatus
_FsMIDot1qFutureVlanMacBasedOnAllPorts_Object=MibTableColumn
fsMIDot1qFutureVlanMacBasedOnAllPorts=_FsMIDot1qFutureVlanMacBasedOnAllPorts_Object((1,3,6,1,4,1,10876,101,1,120,1,2,1,3),_FsMIDot1qFutureVlanMacBasedOnAllPorts_Type())
fsMIDot1qFutureVlanMacBasedOnAllPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanMacBasedOnAllPorts.setStatus(_A)
_FsMIDot1qFutureVlanPortProtoBasedOnAllPorts_Type=EnabledStatus
_FsMIDot1qFutureVlanPortProtoBasedOnAllPorts_Object=MibTableColumn
fsMIDot1qFutureVlanPortProtoBasedOnAllPorts=_FsMIDot1qFutureVlanPortProtoBasedOnAllPorts_Object((1,3,6,1,4,1,10876,101,1,120,1,2,1,4),_FsMIDot1qFutureVlanPortProtoBasedOnAllPorts_Type())
fsMIDot1qFutureVlanPortProtoBasedOnAllPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortProtoBasedOnAllPorts.setStatus(_A)
class _FsMIDot1qFutureVlanShutdownStatus_Type(TruthValue):defaultValue=2
_FsMIDot1qFutureVlanShutdownStatus_Type.__name__=_G
_FsMIDot1qFutureVlanShutdownStatus_Object=MibTableColumn
fsMIDot1qFutureVlanShutdownStatus=_FsMIDot1qFutureVlanShutdownStatus_Object((1,3,6,1,4,1,10876,101,1,120,1,2,1,5),_FsMIDot1qFutureVlanShutdownStatus_Type())
fsMIDot1qFutureVlanShutdownStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanShutdownStatus.setStatus(_A)
_FsMIDot1qFutureGarpShutdownStatus_Type=TruthValue
_FsMIDot1qFutureGarpShutdownStatus_Object=MibTableColumn
fsMIDot1qFutureGarpShutdownStatus=_FsMIDot1qFutureGarpShutdownStatus_Object((1,3,6,1,4,1,10876,101,1,120,1,2,1,6),_FsMIDot1qFutureGarpShutdownStatus_Type())
fsMIDot1qFutureGarpShutdownStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureGarpShutdownStatus.setStatus(_A)
class _FsMIDot1qFutureVlanDebug_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,524287))
_FsMIDot1qFutureVlanDebug_Type.__name__=_F
_FsMIDot1qFutureVlanDebug_Object=MibTableColumn
fsMIDot1qFutureVlanDebug=_FsMIDot1qFutureVlanDebug_Object((1,3,6,1,4,1,10876,101,1,120,1,2,1,7),_FsMIDot1qFutureVlanDebug_Type())
fsMIDot1qFutureVlanDebug.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanDebug.setStatus(_A)
class _FsMIDot1qFutureVlanLearningMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ivl',1),('svl',2),('hybrid',3)))
_FsMIDot1qFutureVlanLearningMode_Type.__name__=_F
_FsMIDot1qFutureVlanLearningMode_Object=MibTableColumn
fsMIDot1qFutureVlanLearningMode=_FsMIDot1qFutureVlanLearningMode_Object((1,3,6,1,4,1,10876,101,1,120,1,2,1,8),_FsMIDot1qFutureVlanLearningMode_Type())
fsMIDot1qFutureVlanLearningMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanLearningMode.setStatus(_A)
class _FsMIDot1qFutureVlanHybridTypeDefault_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ivl',1),('svl',2)))
_FsMIDot1qFutureVlanHybridTypeDefault_Type.__name__=_F
_FsMIDot1qFutureVlanHybridTypeDefault_Object=MibTableColumn
fsMIDot1qFutureVlanHybridTypeDefault=_FsMIDot1qFutureVlanHybridTypeDefault_Object((1,3,6,1,4,1,10876,101,1,120,1,2,1,9),_FsMIDot1qFutureVlanHybridTypeDefault_Type())
fsMIDot1qFutureVlanHybridTypeDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanHybridTypeDefault.setStatus(_A)
_FsMIDot1qFutureVlanOperStatus_Type=EnabledStatus
_FsMIDot1qFutureVlanOperStatus_Object=MibTableColumn
fsMIDot1qFutureVlanOperStatus=_FsMIDot1qFutureVlanOperStatus_Object((1,3,6,1,4,1,10876,101,1,120,1,2,1,10),_FsMIDot1qFutureVlanOperStatus_Type())
fsMIDot1qFutureVlanOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanOperStatus.setStatus(_A)
_FsMIDot1qFutureGvrpOperStatus_Type=EnabledStatus
_FsMIDot1qFutureGvrpOperStatus_Object=MibTableColumn
fsMIDot1qFutureGvrpOperStatus=_FsMIDot1qFutureGvrpOperStatus_Object((1,3,6,1,4,1,10876,101,1,120,1,2,1,11),_FsMIDot1qFutureGvrpOperStatus_Type())
fsMIDot1qFutureGvrpOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureGvrpOperStatus.setStatus(_A)
_FsMIDot1qFutureGmrpOperStatus_Type=EnabledStatus
_FsMIDot1qFutureGmrpOperStatus_Object=MibTableColumn
fsMIDot1qFutureGmrpOperStatus=_FsMIDot1qFutureGmrpOperStatus_Object((1,3,6,1,4,1,10876,101,1,120,1,2,1,12),_FsMIDot1qFutureGmrpOperStatus_Type())
fsMIDot1qFutureGmrpOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureGmrpOperStatus.setStatus(_A)
class _FsMIDot1qFutureVlanContextName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsMIDot1qFutureVlanContextName_Type.__name__=_S
_FsMIDot1qFutureVlanContextName_Object=MibTableColumn
fsMIDot1qFutureVlanContextName=_FsMIDot1qFutureVlanContextName_Object((1,3,6,1,4,1,10876,101,1,120,1,2,1,13),_FsMIDot1qFutureVlanContextName_Type())
fsMIDot1qFutureVlanContextName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanContextName.setStatus(_A)
class _FsMIDot1qFutureGarpDebug_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048575))
_FsMIDot1qFutureGarpDebug_Type.__name__=_F
_FsMIDot1qFutureGarpDebug_Object=MibTableColumn
fsMIDot1qFutureGarpDebug=_FsMIDot1qFutureGarpDebug_Object((1,3,6,1,4,1,10876,101,1,120,1,2,1,14),_FsMIDot1qFutureGarpDebug_Type())
fsMIDot1qFutureGarpDebug.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureGarpDebug.setStatus(_A)
class _FsMIDot1qFutureUnicastMacLearningLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsMIDot1qFutureUnicastMacLearningLimit_Type.__name__=_K
_FsMIDot1qFutureUnicastMacLearningLimit_Object=MibTableColumn
fsMIDot1qFutureUnicastMacLearningLimit=_FsMIDot1qFutureUnicastMacLearningLimit_Object((1,3,6,1,4,1,10876,101,1,120,1,2,1,15),_FsMIDot1qFutureUnicastMacLearningLimit_Type())
fsMIDot1qFutureUnicastMacLearningLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureUnicastMacLearningLimit.setStatus(_A)
class _FsMIDot1qFutureBaseBridgeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dot1dTransparentMode',1),('dot1qVlanMode',2)))
_FsMIDot1qFutureBaseBridgeMode_Type.__name__=_F
_FsMIDot1qFutureBaseBridgeMode_Object=MibTableColumn
fsMIDot1qFutureBaseBridgeMode=_FsMIDot1qFutureBaseBridgeMode_Object((1,3,6,1,4,1,10876,101,1,120,1,2,1,16),_FsMIDot1qFutureBaseBridgeMode_Type())
fsMIDot1qFutureBaseBridgeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureBaseBridgeMode.setStatus(_A)
_FsMIDot1qFutureVlanSubnetBasedOnAllPorts_Type=EnabledStatus
_FsMIDot1qFutureVlanSubnetBasedOnAllPorts_Object=MibTableColumn
fsMIDot1qFutureVlanSubnetBasedOnAllPorts=_FsMIDot1qFutureVlanSubnetBasedOnAllPorts_Object((1,3,6,1,4,1,10876,101,1,120,1,2,1,17),_FsMIDot1qFutureVlanSubnetBasedOnAllPorts_Type())
fsMIDot1qFutureVlanSubnetBasedOnAllPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanSubnetBasedOnAllPorts.setStatus(_A)
class _FsMIDot1qFutureVlanGlobalMacLearningStatus_Type(EnabledStatus):defaultValue=1
_FsMIDot1qFutureVlanGlobalMacLearningStatus_Type.__name__=_I
_FsMIDot1qFutureVlanGlobalMacLearningStatus_Object=MibTableColumn
fsMIDot1qFutureVlanGlobalMacLearningStatus=_FsMIDot1qFutureVlanGlobalMacLearningStatus_Object((1,3,6,1,4,1,10876,101,1,120,1,2,1,18),_FsMIDot1qFutureVlanGlobalMacLearningStatus_Type())
fsMIDot1qFutureVlanGlobalMacLearningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanGlobalMacLearningStatus.setStatus(_A)
class _FsMIDot1qFutureVlanApplyEnhancedFilteringCriteria_Type(TruthValue):defaultValue=1
_FsMIDot1qFutureVlanApplyEnhancedFilteringCriteria_Type.__name__=_G
_FsMIDot1qFutureVlanApplyEnhancedFilteringCriteria_Object=MibTableColumn
fsMIDot1qFutureVlanApplyEnhancedFilteringCriteria=_FsMIDot1qFutureVlanApplyEnhancedFilteringCriteria_Object((1,3,6,1,4,1,10876,101,1,120,1,2,1,19),_FsMIDot1qFutureVlanApplyEnhancedFilteringCriteria_Type())
fsMIDot1qFutureVlanApplyEnhancedFilteringCriteria.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanApplyEnhancedFilteringCriteria.setStatus(_A)
class _FsMIDot1qFutureVlanGlobalsFdbFlush_Type(TruthValue):defaultValue=2
_FsMIDot1qFutureVlanGlobalsFdbFlush_Type.__name__=_G
_FsMIDot1qFutureVlanGlobalsFdbFlush_Object=MibTableColumn
fsMIDot1qFutureVlanGlobalsFdbFlush=_FsMIDot1qFutureVlanGlobalsFdbFlush_Object((1,3,6,1,4,1,10876,101,1,120,1,2,1,20),_FsMIDot1qFutureVlanGlobalsFdbFlush_Type())
fsMIDot1qFutureVlanGlobalsFdbFlush.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanGlobalsFdbFlush.setStatus(_A)
_FsMIDot1qFutureVlanPortTable_Object=MibTable
fsMIDot1qFutureVlanPortTable=_FsMIDot1qFutureVlanPortTable_Object((1,3,6,1,4,1,10876,101,1,120,1,3))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortTable.setStatus(_A)
_FsMIDot1qFutureVlanPortEntry_Object=MibTableRow
fsMIDot1qFutureVlanPortEntry=_FsMIDot1qFutureVlanPortEntry_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1))
fsMIDot1qFutureVlanPortEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortEntry.setStatus(_A)
class _FsMIDot1qFutureVlanPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMIDot1qFutureVlanPort_Type.__name__=_F
_FsMIDot1qFutureVlanPort_Object=MibTableColumn
fsMIDot1qFutureVlanPort=_FsMIDot1qFutureVlanPort_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,1),_FsMIDot1qFutureVlanPort_Type())
fsMIDot1qFutureVlanPort.setMaxAccess(_J)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPort.setStatus(_A)
class _FsMIDot1qFutureVlanPortType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('accessPort',1),('trunkPort',2),('hybridPort',3),('hostPort',4),('promiscuousPort',5)))
_FsMIDot1qFutureVlanPortType_Type.__name__=_F
_FsMIDot1qFutureVlanPortType_Object=MibTableColumn
fsMIDot1qFutureVlanPortType=_FsMIDot1qFutureVlanPortType_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,2),_FsMIDot1qFutureVlanPortType_Type())
fsMIDot1qFutureVlanPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortType.setStatus(_A)
_FsMIDot1qFutureVlanPortPortProtoBasedClassification_Type=EnabledStatus
_FsMIDot1qFutureVlanPortPortProtoBasedClassification_Object=MibTableColumn
fsMIDot1qFutureVlanPortPortProtoBasedClassification=_FsMIDot1qFutureVlanPortPortProtoBasedClassification_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,4),_FsMIDot1qFutureVlanPortPortProtoBasedClassification_Type())
fsMIDot1qFutureVlanPortPortProtoBasedClassification.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortPortProtoBasedClassification.setStatus(_A)
class _FsMIDot1qFutureVlanFilteringUtilityCriteria_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),('enhanced',2)))
_FsMIDot1qFutureVlanFilteringUtilityCriteria_Type.__name__=_F
_FsMIDot1qFutureVlanFilteringUtilityCriteria_Object=MibTableColumn
fsMIDot1qFutureVlanFilteringUtilityCriteria=_FsMIDot1qFutureVlanFilteringUtilityCriteria_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,5),_FsMIDot1qFutureVlanFilteringUtilityCriteria_Type())
fsMIDot1qFutureVlanFilteringUtilityCriteria.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanFilteringUtilityCriteria.setStatus(_A)
class _FsMIDot1qFutureVlanPortProtected_Type(TruthValue):defaultValue=2
_FsMIDot1qFutureVlanPortProtected_Type.__name__=_G
_FsMIDot1qFutureVlanPortProtected_Object=MibTableColumn
fsMIDot1qFutureVlanPortProtected=_FsMIDot1qFutureVlanPortProtected_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,6),_FsMIDot1qFutureVlanPortProtected_Type())
fsMIDot1qFutureVlanPortProtected.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortProtected.setStatus(_A)
class _FsMIDot1qFutureVlanPortUnicastMacLearning_Type(EnabledStatus):defaultValue=1
_FsMIDot1qFutureVlanPortUnicastMacLearning_Type.__name__=_I
_FsMIDot1qFutureVlanPortUnicastMacLearning_Object=MibTableColumn
fsMIDot1qFutureVlanPortUnicastMacLearning=_FsMIDot1qFutureVlanPortUnicastMacLearning_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,8),_FsMIDot1qFutureVlanPortUnicastMacLearning_Type())
fsMIDot1qFutureVlanPortUnicastMacLearning.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortUnicastMacLearning.setStatus(_A)
_FsMIDot1qFutureVlanPortGmrpJoinEmptyTxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGmrpJoinEmptyTxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGmrpJoinEmptyTxCount=_FsMIDot1qFutureVlanPortGmrpJoinEmptyTxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,9),_FsMIDot1qFutureVlanPortGmrpJoinEmptyTxCount_Type())
fsMIDot1qFutureVlanPortGmrpJoinEmptyTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGmrpJoinEmptyTxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGmrpJoinEmptyRxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGmrpJoinEmptyRxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGmrpJoinEmptyRxCount=_FsMIDot1qFutureVlanPortGmrpJoinEmptyRxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,10),_FsMIDot1qFutureVlanPortGmrpJoinEmptyRxCount_Type())
fsMIDot1qFutureVlanPortGmrpJoinEmptyRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGmrpJoinEmptyRxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGmrpJoinInTxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGmrpJoinInTxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGmrpJoinInTxCount=_FsMIDot1qFutureVlanPortGmrpJoinInTxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,11),_FsMIDot1qFutureVlanPortGmrpJoinInTxCount_Type())
fsMIDot1qFutureVlanPortGmrpJoinInTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGmrpJoinInTxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGmrpJoinInRxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGmrpJoinInRxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGmrpJoinInRxCount=_FsMIDot1qFutureVlanPortGmrpJoinInRxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,12),_FsMIDot1qFutureVlanPortGmrpJoinInRxCount_Type())
fsMIDot1qFutureVlanPortGmrpJoinInRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGmrpJoinInRxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGmrpLeaveInTxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGmrpLeaveInTxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGmrpLeaveInTxCount=_FsMIDot1qFutureVlanPortGmrpLeaveInTxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,13),_FsMIDot1qFutureVlanPortGmrpLeaveInTxCount_Type())
fsMIDot1qFutureVlanPortGmrpLeaveInTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGmrpLeaveInTxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGmrpLeaveInRxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGmrpLeaveInRxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGmrpLeaveInRxCount=_FsMIDot1qFutureVlanPortGmrpLeaveInRxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,14),_FsMIDot1qFutureVlanPortGmrpLeaveInRxCount_Type())
fsMIDot1qFutureVlanPortGmrpLeaveInRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGmrpLeaveInRxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGmrpLeaveEmptyTxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGmrpLeaveEmptyTxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGmrpLeaveEmptyTxCount=_FsMIDot1qFutureVlanPortGmrpLeaveEmptyTxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,15),_FsMIDot1qFutureVlanPortGmrpLeaveEmptyTxCount_Type())
fsMIDot1qFutureVlanPortGmrpLeaveEmptyTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGmrpLeaveEmptyTxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGmrpLeaveEmptyRxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGmrpLeaveEmptyRxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGmrpLeaveEmptyRxCount=_FsMIDot1qFutureVlanPortGmrpLeaveEmptyRxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,16),_FsMIDot1qFutureVlanPortGmrpLeaveEmptyRxCount_Type())
fsMIDot1qFutureVlanPortGmrpLeaveEmptyRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGmrpLeaveEmptyRxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGmrpEmptyTxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGmrpEmptyTxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGmrpEmptyTxCount=_FsMIDot1qFutureVlanPortGmrpEmptyTxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,17),_FsMIDot1qFutureVlanPortGmrpEmptyTxCount_Type())
fsMIDot1qFutureVlanPortGmrpEmptyTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGmrpEmptyTxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGmrpEmptyRxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGmrpEmptyRxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGmrpEmptyRxCount=_FsMIDot1qFutureVlanPortGmrpEmptyRxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,18),_FsMIDot1qFutureVlanPortGmrpEmptyRxCount_Type())
fsMIDot1qFutureVlanPortGmrpEmptyRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGmrpEmptyRxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGmrpLeaveAllTxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGmrpLeaveAllTxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGmrpLeaveAllTxCount=_FsMIDot1qFutureVlanPortGmrpLeaveAllTxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,19),_FsMIDot1qFutureVlanPortGmrpLeaveAllTxCount_Type())
fsMIDot1qFutureVlanPortGmrpLeaveAllTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGmrpLeaveAllTxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGmrpLeaveAllRxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGmrpLeaveAllRxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGmrpLeaveAllRxCount=_FsMIDot1qFutureVlanPortGmrpLeaveAllRxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,20),_FsMIDot1qFutureVlanPortGmrpLeaveAllRxCount_Type())
fsMIDot1qFutureVlanPortGmrpLeaveAllRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGmrpLeaveAllRxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGmrpDiscardCount_Type=Counter32
_FsMIDot1qFutureVlanPortGmrpDiscardCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGmrpDiscardCount=_FsMIDot1qFutureVlanPortGmrpDiscardCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,21),_FsMIDot1qFutureVlanPortGmrpDiscardCount_Type())
fsMIDot1qFutureVlanPortGmrpDiscardCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGmrpDiscardCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGvrpJoinEmptyTxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGvrpJoinEmptyTxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGvrpJoinEmptyTxCount=_FsMIDot1qFutureVlanPortGvrpJoinEmptyTxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,22),_FsMIDot1qFutureVlanPortGvrpJoinEmptyTxCount_Type())
fsMIDot1qFutureVlanPortGvrpJoinEmptyTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGvrpJoinEmptyTxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGvrpJoinEmptyRxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGvrpJoinEmptyRxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGvrpJoinEmptyRxCount=_FsMIDot1qFutureVlanPortGvrpJoinEmptyRxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,23),_FsMIDot1qFutureVlanPortGvrpJoinEmptyRxCount_Type())
fsMIDot1qFutureVlanPortGvrpJoinEmptyRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGvrpJoinEmptyRxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGvrpJoinInTxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGvrpJoinInTxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGvrpJoinInTxCount=_FsMIDot1qFutureVlanPortGvrpJoinInTxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,24),_FsMIDot1qFutureVlanPortGvrpJoinInTxCount_Type())
fsMIDot1qFutureVlanPortGvrpJoinInTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGvrpJoinInTxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGvrpJoinInRxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGvrpJoinInRxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGvrpJoinInRxCount=_FsMIDot1qFutureVlanPortGvrpJoinInRxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,25),_FsMIDot1qFutureVlanPortGvrpJoinInRxCount_Type())
fsMIDot1qFutureVlanPortGvrpJoinInRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGvrpJoinInRxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGvrpLeaveInTxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGvrpLeaveInTxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGvrpLeaveInTxCount=_FsMIDot1qFutureVlanPortGvrpLeaveInTxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,26),_FsMIDot1qFutureVlanPortGvrpLeaveInTxCount_Type())
fsMIDot1qFutureVlanPortGvrpLeaveInTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGvrpLeaveInTxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGvrpLeaveInRxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGvrpLeaveInRxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGvrpLeaveInRxCount=_FsMIDot1qFutureVlanPortGvrpLeaveInRxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,27),_FsMIDot1qFutureVlanPortGvrpLeaveInRxCount_Type())
fsMIDot1qFutureVlanPortGvrpLeaveInRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGvrpLeaveInRxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGvrpLeaveEmptyTxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGvrpLeaveEmptyTxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGvrpLeaveEmptyTxCount=_FsMIDot1qFutureVlanPortGvrpLeaveEmptyTxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,28),_FsMIDot1qFutureVlanPortGvrpLeaveEmptyTxCount_Type())
fsMIDot1qFutureVlanPortGvrpLeaveEmptyTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGvrpLeaveEmptyTxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGvrpLeaveEmptyRxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGvrpLeaveEmptyRxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGvrpLeaveEmptyRxCount=_FsMIDot1qFutureVlanPortGvrpLeaveEmptyRxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,29),_FsMIDot1qFutureVlanPortGvrpLeaveEmptyRxCount_Type())
fsMIDot1qFutureVlanPortGvrpLeaveEmptyRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGvrpLeaveEmptyRxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGvrpEmptyTxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGvrpEmptyTxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGvrpEmptyTxCount=_FsMIDot1qFutureVlanPortGvrpEmptyTxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,30),_FsMIDot1qFutureVlanPortGvrpEmptyTxCount_Type())
fsMIDot1qFutureVlanPortGvrpEmptyTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGvrpEmptyTxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGvrpEmptyRxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGvrpEmptyRxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGvrpEmptyRxCount=_FsMIDot1qFutureVlanPortGvrpEmptyRxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,31),_FsMIDot1qFutureVlanPortGvrpEmptyRxCount_Type())
fsMIDot1qFutureVlanPortGvrpEmptyRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGvrpEmptyRxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGvrpLeaveAllTxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGvrpLeaveAllTxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGvrpLeaveAllTxCount=_FsMIDot1qFutureVlanPortGvrpLeaveAllTxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,32),_FsMIDot1qFutureVlanPortGvrpLeaveAllTxCount_Type())
fsMIDot1qFutureVlanPortGvrpLeaveAllTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGvrpLeaveAllTxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGvrpLeaveAllRxCount_Type=Counter32
_FsMIDot1qFutureVlanPortGvrpLeaveAllRxCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGvrpLeaveAllRxCount=_FsMIDot1qFutureVlanPortGvrpLeaveAllRxCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,33),_FsMIDot1qFutureVlanPortGvrpLeaveAllRxCount_Type())
fsMIDot1qFutureVlanPortGvrpLeaveAllRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGvrpLeaveAllRxCount.setStatus(_A)
_FsMIDot1qFutureVlanPortGvrpDiscardCount_Type=Counter32
_FsMIDot1qFutureVlanPortGvrpDiscardCount_Object=MibTableColumn
fsMIDot1qFutureVlanPortGvrpDiscardCount=_FsMIDot1qFutureVlanPortGvrpDiscardCount_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,34),_FsMIDot1qFutureVlanPortGvrpDiscardCount_Type())
fsMIDot1qFutureVlanPortGvrpDiscardCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortGvrpDiscardCount.setStatus(_A)
class _FsMIDot1qFutureVlanPortFdbFlush_Type(TruthValue):defaultValue=2
_FsMIDot1qFutureVlanPortFdbFlush_Type.__name__=_G
_FsMIDot1qFutureVlanPortFdbFlush_Object=MibTableColumn
fsMIDot1qFutureVlanPortFdbFlush=_FsMIDot1qFutureVlanPortFdbFlush_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,35),_FsMIDot1qFutureVlanPortFdbFlush_Type())
fsMIDot1qFutureVlanPortFdbFlush.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortFdbFlush.setStatus(_A)
class _FsMIDot1qFutureVlanPortAllowedVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_FsMIDot1qFutureVlanPortAllowedVlanList_Type.__name__=_Q
_FsMIDot1qFutureVlanPortAllowedVlanList_Object=MibTableColumn
fsMIDot1qFutureVlanPortAllowedVlanList=_FsMIDot1qFutureVlanPortAllowedVlanList_Object((1,3,6,1,4,1,10876,101,1,120,1,3,1,36),_FsMIDot1qFutureVlanPortAllowedVlanList_Type())
fsMIDot1qFutureVlanPortAllowedVlanList.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortAllowedVlanList.setStatus(_A)
_FsMIDot1qFutureVlanPortMacMapTable_Object=MibTable
fsMIDot1qFutureVlanPortMacMapTable=_FsMIDot1qFutureVlanPortMacMapTable_Object((1,3,6,1,4,1,10876,101,1,120,1,4))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortMacMapTable.setStatus(_A)
_FsMIDot1qFutureVlanPortMacMapEntry_Object=MibTableRow
fsMIDot1qFutureVlanPortMacMapEntry=_FsMIDot1qFutureVlanPortMacMapEntry_Object((1,3,6,1,4,1,10876,101,1,120,1,4,1))
fsMIDot1qFutureVlanPortMacMapEntry.setIndexNames((0,_D,_Y))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortMacMapEntry.setStatus(_A)
_FsMIDot1qFutureVlanPortMacMapAddr_Type=MacAddress
_FsMIDot1qFutureVlanPortMacMapAddr_Object=MibTableColumn
fsMIDot1qFutureVlanPortMacMapAddr=_FsMIDot1qFutureVlanPortMacMapAddr_Object((1,3,6,1,4,1,10876,101,1,120,1,4,1,1),_FsMIDot1qFutureVlanPortMacMapAddr_Type())
fsMIDot1qFutureVlanPortMacMapAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortMacMapAddr.setStatus(_A)
_FsMIDot1qFutureVlanPortMacMapVid_Type=VlanId
_FsMIDot1qFutureVlanPortMacMapVid_Object=MibTableColumn
fsMIDot1qFutureVlanPortMacMapVid=_FsMIDot1qFutureVlanPortMacMapVid_Object((1,3,6,1,4,1,10876,101,1,120,1,4,1,2),_FsMIDot1qFutureVlanPortMacMapVid_Type())
fsMIDot1qFutureVlanPortMacMapVid.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortMacMapVid.setStatus(_A)
_FsMIDot1qFutureVlanPortMacMapRowStatus_Type=RowStatus
_FsMIDot1qFutureVlanPortMacMapRowStatus_Object=MibTableColumn
fsMIDot1qFutureVlanPortMacMapRowStatus=_FsMIDot1qFutureVlanPortMacMapRowStatus_Object((1,3,6,1,4,1,10876,101,1,120,1,4,1,5),_FsMIDot1qFutureVlanPortMacMapRowStatus_Type())
fsMIDot1qFutureVlanPortMacMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortMacMapRowStatus.setStatus(_A)
_FsMIDot1qFutureVlanFidMapTable_Object=MibTable
fsMIDot1qFutureVlanFidMapTable=_FsMIDot1qFutureVlanFidMapTable_Object((1,3,6,1,4,1,10876,101,1,120,1,5))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanFidMapTable.setStatus(_A)
_FsMIDot1qFutureVlanFidMapEntry_Object=MibTableRow
fsMIDot1qFutureVlanFidMapEntry=_FsMIDot1qFutureVlanFidMapEntry_Object((1,3,6,1,4,1,10876,101,1,120,1,5,1))
fsMIDot1qFutureVlanFidMapEntry.setIndexNames((0,_D,_H),(0,_D,_L))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanFidMapEntry.setStatus(_A)
class _FsMIDot1qFutureVlanIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsMIDot1qFutureVlanIndex_Type.__name__=_K
_FsMIDot1qFutureVlanIndex_Object=MibTableColumn
fsMIDot1qFutureVlanIndex=_FsMIDot1qFutureVlanIndex_Object((1,3,6,1,4,1,10876,101,1,120,1,5,1,1),_FsMIDot1qFutureVlanIndex_Type())
fsMIDot1qFutureVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanIndex.setStatus(_A)
class _FsMIDot1qFutureVlanFid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsMIDot1qFutureVlanFid_Type.__name__=_K
_FsMIDot1qFutureVlanFid_Object=MibTableColumn
fsMIDot1qFutureVlanFid=_FsMIDot1qFutureVlanFid_Object((1,3,6,1,4,1,10876,101,1,120,1,5,1,2),_FsMIDot1qFutureVlanFid_Type())
fsMIDot1qFutureVlanFid.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanFid.setStatus(_A)
_FsMIDot1qFutureVlanCounterTable_Object=MibTable
fsMIDot1qFutureVlanCounterTable=_FsMIDot1qFutureVlanCounterTable_Object((1,3,6,1,4,1,10876,101,1,120,1,6))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanCounterTable.setStatus(_A)
_FsMIDot1qFutureVlanCounterEntry_Object=MibTableRow
fsMIDot1qFutureVlanCounterEntry=_FsMIDot1qFutureVlanCounterEntry_Object((1,3,6,1,4,1,10876,101,1,120,1,6,1))
fsMIDot1qFutureVlanCounterEntry.setIndexNames((0,_D,_H),(0,_D,_L))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanCounterEntry.setStatus(_A)
_FsMIDot1qFutureVlanCounterRxUcast_Type=Counter32
_FsMIDot1qFutureVlanCounterRxUcast_Object=MibTableColumn
fsMIDot1qFutureVlanCounterRxUcast=_FsMIDot1qFutureVlanCounterRxUcast_Object((1,3,6,1,4,1,10876,101,1,120,1,6,1,1),_FsMIDot1qFutureVlanCounterRxUcast_Type())
fsMIDot1qFutureVlanCounterRxUcast.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanCounterRxUcast.setStatus(_A)
_FsMIDot1qFutureVlanCounterRxMcastBcast_Type=Counter32
_FsMIDot1qFutureVlanCounterRxMcastBcast_Object=MibTableColumn
fsMIDot1qFutureVlanCounterRxMcastBcast=_FsMIDot1qFutureVlanCounterRxMcastBcast_Object((1,3,6,1,4,1,10876,101,1,120,1,6,1,2),_FsMIDot1qFutureVlanCounterRxMcastBcast_Type())
fsMIDot1qFutureVlanCounterRxMcastBcast.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanCounterRxMcastBcast.setStatus(_A)
_FsMIDot1qFutureVlanCounterTxUnknUcast_Type=Counter32
_FsMIDot1qFutureVlanCounterTxUnknUcast_Object=MibTableColumn
fsMIDot1qFutureVlanCounterTxUnknUcast=_FsMIDot1qFutureVlanCounterTxUnknUcast_Object((1,3,6,1,4,1,10876,101,1,120,1,6,1,3),_FsMIDot1qFutureVlanCounterTxUnknUcast_Type())
fsMIDot1qFutureVlanCounterTxUnknUcast.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanCounterTxUnknUcast.setStatus(_A)
_FsMIDot1qFutureVlanCounterTxUcast_Type=Counter32
_FsMIDot1qFutureVlanCounterTxUcast_Object=MibTableColumn
fsMIDot1qFutureVlanCounterTxUcast=_FsMIDot1qFutureVlanCounterTxUcast_Object((1,3,6,1,4,1,10876,101,1,120,1,6,1,4),_FsMIDot1qFutureVlanCounterTxUcast_Type())
fsMIDot1qFutureVlanCounterTxUcast.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanCounterTxUcast.setStatus(_A)
_FsMIDot1qFutureVlanCounterTxBcast_Type=Counter32
_FsMIDot1qFutureVlanCounterTxBcast_Object=MibTableColumn
fsMIDot1qFutureVlanCounterTxBcast=_FsMIDot1qFutureVlanCounterTxBcast_Object((1,3,6,1,4,1,10876,101,1,120,1,6,1,5),_FsMIDot1qFutureVlanCounterTxBcast_Type())
fsMIDot1qFutureVlanCounterTxBcast.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanCounterTxBcast.setStatus(_A)
class _FsMIDot1qFutureVlanCounterStatus_Type(EnabledStatus):defaultValue=2
_FsMIDot1qFutureVlanCounterStatus_Type.__name__=_I
_FsMIDot1qFutureVlanCounterStatus_Object=MibTableColumn
fsMIDot1qFutureVlanCounterStatus=_FsMIDot1qFutureVlanCounterStatus_Object((1,3,6,1,4,1,10876,101,1,120,1,6,1,6),_FsMIDot1qFutureVlanCounterStatus_Type())
fsMIDot1qFutureVlanCounterStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanCounterStatus.setStatus(_A)
_FsMIDot1qFutureVlanUnicastMacControlTable_Object=MibTable
fsMIDot1qFutureVlanUnicastMacControlTable=_FsMIDot1qFutureVlanUnicastMacControlTable_Object((1,3,6,1,4,1,10876,101,1,120,1,7))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanUnicastMacControlTable.setStatus(_A)
_FsMIDot1qFutureVlanUnicastMacControlEntry_Object=MibTableRow
fsMIDot1qFutureVlanUnicastMacControlEntry=_FsMIDot1qFutureVlanUnicastMacControlEntry_Object((1,3,6,1,4,1,10876,101,1,120,1,7,1))
fsMIDot1qFutureVlanUnicastMacControlEntry.setIndexNames((0,_D,_H),(0,_D,_L))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanUnicastMacControlEntry.setStatus(_A)
class _FsMIDot1qFutureVlanUnicastMacLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_FsMIDot1qFutureVlanUnicastMacLimit_Type.__name__=_K
_FsMIDot1qFutureVlanUnicastMacLimit_Object=MibTableColumn
fsMIDot1qFutureVlanUnicastMacLimit=_FsMIDot1qFutureVlanUnicastMacLimit_Object((1,3,6,1,4,1,10876,101,1,120,1,7,1,1),_FsMIDot1qFutureVlanUnicastMacLimit_Type())
fsMIDot1qFutureVlanUnicastMacLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanUnicastMacLimit.setStatus(_A)
class _FsMIDot1qFutureVlanAdminMacLearningStatus_Type(MacLearningStatus):defaultValue=3
_FsMIDot1qFutureVlanAdminMacLearningStatus_Type.__name__=_Z
_FsMIDot1qFutureVlanAdminMacLearningStatus_Object=MibTableColumn
fsMIDot1qFutureVlanAdminMacLearningStatus=_FsMIDot1qFutureVlanAdminMacLearningStatus_Object((1,3,6,1,4,1,10876,101,1,120,1,7,1,2),_FsMIDot1qFutureVlanAdminMacLearningStatus_Type())
fsMIDot1qFutureVlanAdminMacLearningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanAdminMacLearningStatus.setStatus(_A)
_FsMIDot1qFutureVlanOperMacLearningStatus_Type=EnabledStatus
_FsMIDot1qFutureVlanOperMacLearningStatus_Object=MibTableColumn
fsMIDot1qFutureVlanOperMacLearningStatus=_FsMIDot1qFutureVlanOperMacLearningStatus_Object((1,3,6,1,4,1,10876,101,1,120,1,7,1,3),_FsMIDot1qFutureVlanOperMacLearningStatus_Type())
fsMIDot1qFutureVlanOperMacLearningStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanOperMacLearningStatus.setStatus(_A)
_FsMIDot1qFutureGarpGlobalTrace_Type=TruthValue
_FsMIDot1qFutureGarpGlobalTrace_Object=MibScalar
fsMIDot1qFutureGarpGlobalTrace=_FsMIDot1qFutureGarpGlobalTrace_Object((1,3,6,1,4,1,10876,101,1,120,1,8),_FsMIDot1qFutureGarpGlobalTrace_Type())
fsMIDot1qFutureGarpGlobalTrace.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureGarpGlobalTrace.setStatus(_A)
_FsMIDot1qFutureVlanTpFdbTable_Object=MibTable
fsMIDot1qFutureVlanTpFdbTable=_FsMIDot1qFutureVlanTpFdbTable_Object((1,3,6,1,4,1,10876,101,1,120,1,9))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanTpFdbTable.setStatus(_A)
_FsMIDot1qFutureVlanTpFdbEntry_Object=MibTableRow
fsMIDot1qFutureVlanTpFdbEntry=_FsMIDot1qFutureVlanTpFdbEntry_Object((1,3,6,1,4,1,10876,101,1,120,1,9,1))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanTpFdbEntry.setStatus(_A)
class _FsMIDot1qFutureVlanOldTpFdbPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIDot1qFutureVlanOldTpFdbPort_Type.__name__=_F
_FsMIDot1qFutureVlanOldTpFdbPort_Object=MibTableColumn
fsMIDot1qFutureVlanOldTpFdbPort=_FsMIDot1qFutureVlanOldTpFdbPort_Object((1,3,6,1,4,1,10876,101,1,120,1,9,1,1),_FsMIDot1qFutureVlanOldTpFdbPort_Type())
fsMIDot1qFutureVlanOldTpFdbPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanOldTpFdbPort.setStatus(_A)
_FsMIDot1qFutureConnectionIdentifier_Type=MacAddress
_FsMIDot1qFutureConnectionIdentifier_Object=MibTableColumn
fsMIDot1qFutureConnectionIdentifier=_FsMIDot1qFutureConnectionIdentifier_Object((1,3,6,1,4,1,10876,101,1,120,1,9,1,2),_FsMIDot1qFutureConnectionIdentifier_Type())
fsMIDot1qFutureConnectionIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureConnectionIdentifier.setStatus(_A)
_FsMIDot1qFutureVlanWildCardTable_Object=MibTable
fsMIDot1qFutureVlanWildCardTable=_FsMIDot1qFutureVlanWildCardTable_Object((1,3,6,1,4,1,10876,101,1,120,1,10))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanWildCardTable.setStatus(_A)
_FsMIDot1qFutureVlanWildCardEntry_Object=MibTableRow
fsMIDot1qFutureVlanWildCardEntry=_FsMIDot1qFutureVlanWildCardEntry_Object((1,3,6,1,4,1,10876,101,1,120,1,10,1))
fsMIDot1qFutureVlanWildCardEntry.setIndexNames((0,_D,_H),(0,_D,_P))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanWildCardEntry.setStatus(_A)
_FsMIDot1qFutureVlanWildCardMacAddress_Type=MacAddress
_FsMIDot1qFutureVlanWildCardMacAddress_Object=MibTableColumn
fsMIDot1qFutureVlanWildCardMacAddress=_FsMIDot1qFutureVlanWildCardMacAddress_Object((1,3,6,1,4,1,10876,101,1,120,1,10,1,1),_FsMIDot1qFutureVlanWildCardMacAddress_Type())
fsMIDot1qFutureVlanWildCardMacAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanWildCardMacAddress.setStatus(_A)
_FsMIDot1qFutureVlanWildCardRowStatus_Type=RowStatus
_FsMIDot1qFutureVlanWildCardRowStatus_Object=MibTableColumn
fsMIDot1qFutureVlanWildCardRowStatus=_FsMIDot1qFutureVlanWildCardRowStatus_Object((1,3,6,1,4,1,10876,101,1,120,1,10,1,2),_FsMIDot1qFutureVlanWildCardRowStatus_Type())
fsMIDot1qFutureVlanWildCardRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanWildCardRowStatus.setStatus(_A)
_FsMIDot1qFutureVlanWildCardPortTable_Object=MibTable
fsMIDot1qFutureVlanWildCardPortTable=_FsMIDot1qFutureVlanWildCardPortTable_Object((1,3,6,1,4,1,10876,101,1,120,1,11))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanWildCardPortTable.setStatus(_A)
_FsMIDot1qFutureVlanWildCardPortEntry_Object=MibTableRow
fsMIDot1qFutureVlanWildCardPortEntry=_FsMIDot1qFutureVlanWildCardPortEntry_Object((1,3,6,1,4,1,10876,101,1,120,1,11,1))
fsMIDot1qFutureVlanWildCardPortEntry.setIndexNames((0,_D,_H),(0,_D,_P),(0,_O,_U))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanWildCardPortEntry.setStatus(_A)
_FsMIDot1qFutureVlanIsWildCardEgressPort_Type=TruthValue
_FsMIDot1qFutureVlanIsWildCardEgressPort_Object=MibTableColumn
fsMIDot1qFutureVlanIsWildCardEgressPort=_FsMIDot1qFutureVlanIsWildCardEgressPort_Object((1,3,6,1,4,1,10876,101,1,120,1,11,1,1),_FsMIDot1qFutureVlanIsWildCardEgressPort_Type())
fsMIDot1qFutureVlanIsWildCardEgressPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanIsWildCardEgressPort.setStatus(_A)
_FsMIDot1qFutureStaticUnicastExtnTable_Object=MibTable
fsMIDot1qFutureStaticUnicastExtnTable=_FsMIDot1qFutureStaticUnicastExtnTable_Object((1,3,6,1,4,1,10876,101,1,120,1,12))
if mibBuilder.loadTexts:fsMIDot1qFutureStaticUnicastExtnTable.setStatus(_A)
_FsMIDot1qFutureStaticUnicastExtnEntry_Object=MibTableRow
fsMIDot1qFutureStaticUnicastExtnEntry=_FsMIDot1qFutureStaticUnicastExtnEntry_Object((1,3,6,1,4,1,10876,101,1,120,1,12,1))
if mibBuilder.loadTexts:fsMIDot1qFutureStaticUnicastExtnEntry.setStatus(_A)
_FsMIDot1qFutureStaticConnectionIdentifier_Type=MacAddress
_FsMIDot1qFutureStaticConnectionIdentifier_Object=MibTableColumn
fsMIDot1qFutureStaticConnectionIdentifier=_FsMIDot1qFutureStaticConnectionIdentifier_Object((1,3,6,1,4,1,10876,101,1,120,1,12,1,1),_FsMIDot1qFutureStaticConnectionIdentifier_Type())
fsMIDot1qFutureStaticConnectionIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureStaticConnectionIdentifier.setStatus(_A)
_FsMIDot1qFutureVlanPortSubnetMapTable_Object=MibTable
fsMIDot1qFutureVlanPortSubnetMapTable=_FsMIDot1qFutureVlanPortSubnetMapTable_Object((1,3,6,1,4,1,10876,101,1,120,1,13))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortSubnetMapTable.setStatus(_A)
_FsMIDot1qFutureVlanPortSubnetMapEntry_Object=MibTableRow
fsMIDot1qFutureVlanPortSubnetMapEntry=_FsMIDot1qFutureVlanPortSubnetMapEntry_Object((1,3,6,1,4,1,10876,101,1,120,1,13,1))
fsMIDot1qFutureVlanPortSubnetMapEntry.setIndexNames((0,_D,_a))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortSubnetMapEntry.setStatus(_A)
_FsMIDot1qFutureVlanPortSubnetMapAddr_Type=IpAddress
_FsMIDot1qFutureVlanPortSubnetMapAddr_Object=MibTableColumn
fsMIDot1qFutureVlanPortSubnetMapAddr=_FsMIDot1qFutureVlanPortSubnetMapAddr_Object((1,3,6,1,4,1,10876,101,1,120,1,13,1,1),_FsMIDot1qFutureVlanPortSubnetMapAddr_Type())
fsMIDot1qFutureVlanPortSubnetMapAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortSubnetMapAddr.setStatus(_A)
_FsMIDot1qFutureVlanPortSubnetMapVid_Type=VlanId
_FsMIDot1qFutureVlanPortSubnetMapVid_Object=MibTableColumn
fsMIDot1qFutureVlanPortSubnetMapVid=_FsMIDot1qFutureVlanPortSubnetMapVid_Object((1,3,6,1,4,1,10876,101,1,120,1,13,1,2),_FsMIDot1qFutureVlanPortSubnetMapVid_Type())
fsMIDot1qFutureVlanPortSubnetMapVid.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortSubnetMapVid.setStatus(_A)
_FsMIDot1qFutureVlanPortSubnetMapRowStatus_Type=RowStatus
_FsMIDot1qFutureVlanPortSubnetMapRowStatus_Object=MibTableColumn
fsMIDot1qFutureVlanPortSubnetMapRowStatus=_FsMIDot1qFutureVlanPortSubnetMapRowStatus_Object((1,3,6,1,4,1,10876,101,1,120,1,13,1,4),_FsMIDot1qFutureVlanPortSubnetMapRowStatus_Type())
fsMIDot1qFutureVlanPortSubnetMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortSubnetMapRowStatus.setStatus(_A)
_FsMIDot1qFutureVlanSwStatsEnabled_Type=TruthValue
_FsMIDot1qFutureVlanSwStatsEnabled_Object=MibScalar
fsMIDot1qFutureVlanSwStatsEnabled=_FsMIDot1qFutureVlanSwStatsEnabled_Object((1,3,6,1,4,1,10876,101,1,120,1,14),_FsMIDot1qFutureVlanSwStatsEnabled_Type())
fsMIDot1qFutureVlanSwStatsEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanSwStatsEnabled.setStatus(_A)
_FsMIDot1qFutureStVlanExtTable_Object=MibTable
fsMIDot1qFutureStVlanExtTable=_FsMIDot1qFutureStVlanExtTable_Object((1,3,6,1,4,1,10876,101,1,120,1,15))
if mibBuilder.loadTexts:fsMIDot1qFutureStVlanExtTable.setStatus(_A)
_FsMIDot1qFutureStVlanExtEntry_Object=MibTableRow
fsMIDot1qFutureStVlanExtEntry=_FsMIDot1qFutureStVlanExtEntry_Object((1,3,6,1,4,1,10876,101,1,120,1,15,1))
if mibBuilder.loadTexts:fsMIDot1qFutureStVlanExtEntry.setStatus(_A)
class _FsMIDot1qFutureStVlanPVlanType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),('primary',2),('isolated',3),('community',4)))
_FsMIDot1qFutureStVlanPVlanType_Type.__name__=_F
_FsMIDot1qFutureStVlanPVlanType_Object=MibTableColumn
fsMIDot1qFutureStVlanPVlanType=_FsMIDot1qFutureStVlanPVlanType_Object((1,3,6,1,4,1,10876,101,1,120,1,15,1,1),_FsMIDot1qFutureStVlanPVlanType_Type())
fsMIDot1qFutureStVlanPVlanType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureStVlanPVlanType.setStatus(_A)
class _FsMIDot1qFutureStVlanPrimaryVid_Type(VlanIdOrNone):defaultValue=0
_FsMIDot1qFutureStVlanPrimaryVid_Type.__name__=_R
_FsMIDot1qFutureStVlanPrimaryVid_Object=MibTableColumn
fsMIDot1qFutureStVlanPrimaryVid=_FsMIDot1qFutureStVlanPrimaryVid_Object((1,3,6,1,4,1,10876,101,1,120,1,15,1,2),_FsMIDot1qFutureStVlanPrimaryVid_Type())
fsMIDot1qFutureStVlanPrimaryVid.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureStVlanPrimaryVid.setStatus(_A)
class _FsMIDot1qFutureStVlanFdbFlush_Type(TruthValue):defaultValue=2
_FsMIDot1qFutureStVlanFdbFlush_Type.__name__=_G
_FsMIDot1qFutureStVlanFdbFlush_Object=MibTableColumn
fsMIDot1qFutureStVlanFdbFlush=_FsMIDot1qFutureStVlanFdbFlush_Object((1,3,6,1,4,1,10876,101,1,120,1,15,1,3),_FsMIDot1qFutureStVlanFdbFlush_Type())
fsMIDot1qFutureStVlanFdbFlush.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureStVlanFdbFlush.setStatus(_A)
_FsMIDot1qFutureVlanPortSubnetMapExtTable_Object=MibTable
fsMIDot1qFutureVlanPortSubnetMapExtTable=_FsMIDot1qFutureVlanPortSubnetMapExtTable_Object((1,3,6,1,4,1,10876,101,1,120,1,16))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortSubnetMapExtTable.setStatus(_A)
_FsMIDot1qFutureVlanPortSubnetMapExtEntry_Object=MibTableRow
fsMIDot1qFutureVlanPortSubnetMapExtEntry=_FsMIDot1qFutureVlanPortSubnetMapExtEntry_Object((1,3,6,1,4,1,10876,101,1,120,1,16,1))
fsMIDot1qFutureVlanPortSubnetMapExtEntry.setIndexNames((0,_D,_b),(0,_D,_c))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortSubnetMapExtEntry.setStatus(_A)
_FsMIDot1qFutureVlanPortSubnetMapExtAddr_Type=IpAddress
_FsMIDot1qFutureVlanPortSubnetMapExtAddr_Object=MibTableColumn
fsMIDot1qFutureVlanPortSubnetMapExtAddr=_FsMIDot1qFutureVlanPortSubnetMapExtAddr_Object((1,3,6,1,4,1,10876,101,1,120,1,16,1,1),_FsMIDot1qFutureVlanPortSubnetMapExtAddr_Type())
fsMIDot1qFutureVlanPortSubnetMapExtAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortSubnetMapExtAddr.setStatus(_A)
_FsMIDot1qFutureVlanPortSubnetMapExtMask_Type=IpAddress
_FsMIDot1qFutureVlanPortSubnetMapExtMask_Object=MibTableColumn
fsMIDot1qFutureVlanPortSubnetMapExtMask=_FsMIDot1qFutureVlanPortSubnetMapExtMask_Object((1,3,6,1,4,1,10876,101,1,120,1,16,1,2),_FsMIDot1qFutureVlanPortSubnetMapExtMask_Type())
fsMIDot1qFutureVlanPortSubnetMapExtMask.setMaxAccess(_J)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortSubnetMapExtMask.setStatus(_A)
_FsMIDot1qFutureVlanPortSubnetMapExtVid_Type=VlanId
_FsMIDot1qFutureVlanPortSubnetMapExtVid_Object=MibTableColumn
fsMIDot1qFutureVlanPortSubnetMapExtVid=_FsMIDot1qFutureVlanPortSubnetMapExtVid_Object((1,3,6,1,4,1,10876,101,1,120,1,16,1,3),_FsMIDot1qFutureVlanPortSubnetMapExtVid_Type())
fsMIDot1qFutureVlanPortSubnetMapExtVid.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortSubnetMapExtVid.setStatus(_A)
_FsMIDot1qFutureVlanPortSubnetMapExtRowStatus_Type=RowStatus
_FsMIDot1qFutureVlanPortSubnetMapExtRowStatus_Object=MibTableColumn
fsMIDot1qFutureVlanPortSubnetMapExtRowStatus=_FsMIDot1qFutureVlanPortSubnetMapExtRowStatus_Object((1,3,6,1,4,1,10876,101,1,120,1,16,1,5),_FsMIDot1qFutureVlanPortSubnetMapExtRowStatus_Type())
fsMIDot1qFutureVlanPortSubnetMapExtRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanPortSubnetMapExtRowStatus.setStatus(_A)
_FsMIDot1qFuturePortVlanExtTable_Object=MibTable
fsMIDot1qFuturePortVlanExtTable=_FsMIDot1qFuturePortVlanExtTable_Object((1,3,6,1,4,1,10876,101,1,120,1,17))
if mibBuilder.loadTexts:fsMIDot1qFuturePortVlanExtTable.setStatus(_A)
_FsMIDot1qFuturePortVlanExtEntry_Object=MibTableRow
fsMIDot1qFuturePortVlanExtEntry=_FsMIDot1qFuturePortVlanExtEntry_Object((1,3,6,1,4,1,10876,101,1,120,1,17,1))
if mibBuilder.loadTexts:fsMIDot1qFuturePortVlanExtEntry.setStatus(_A)
class _FsMIDot1qFuturePortVlanFdbFlush_Type(TruthValue):defaultValue=2
_FsMIDot1qFuturePortVlanFdbFlush_Type.__name__=_G
_FsMIDot1qFuturePortVlanFdbFlush_Object=MibTableColumn
fsMIDot1qFuturePortVlanFdbFlush=_FsMIDot1qFuturePortVlanFdbFlush_Object((1,3,6,1,4,1,10876,101,1,120,1,17,1,1),_FsMIDot1qFuturePortVlanFdbFlush_Type())
fsMIDot1qFuturePortVlanFdbFlush.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFuturePortVlanFdbFlush.setStatus(_A)
_FsMIDot1qFutureVlanTunnelConfig_ObjectIdentity=ObjectIdentity
fsMIDot1qFutureVlanTunnelConfig=_FsMIDot1qFutureVlanTunnelConfig_ObjectIdentity((1,3,6,1,4,1,10876,101,1,120,2))
_FsMIDot1qFutureVlanTunnelConfigTable_Object=MibTable
fsMIDot1qFutureVlanTunnelConfigTable=_FsMIDot1qFutureVlanTunnelConfigTable_Object((1,3,6,1,4,1,10876,101,1,120,2,1))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanTunnelConfigTable.setStatus(_E)
_FsMIDot1qFutureVlanTunnelConfigEntry_Object=MibTableRow
fsMIDot1qFutureVlanTunnelConfigEntry=_FsMIDot1qFutureVlanTunnelConfigEntry_Object((1,3,6,1,4,1,10876,101,1,120,2,1,1))
fsMIDot1qFutureVlanTunnelConfigEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanTunnelConfigEntry.setStatus(_E)
class _FsMIDot1qFutureVlanBridgeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('customerBridge',1),('providerBridge',2),('providerCoreBridge',3),('providerEdgeBridge',4),('invalidBridgeMode',5)))
_FsMIDot1qFutureVlanBridgeMode_Type.__name__=_F
_FsMIDot1qFutureVlanBridgeMode_Object=MibTableColumn
fsMIDot1qFutureVlanBridgeMode=_FsMIDot1qFutureVlanBridgeMode_Object((1,3,6,1,4,1,10876,101,1,120,2,1,1,1),_FsMIDot1qFutureVlanBridgeMode_Type())
fsMIDot1qFutureVlanBridgeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanBridgeMode.setStatus(_E)
class _FsMIDot1qFutureVlanTunnelBpduPri_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsMIDot1qFutureVlanTunnelBpduPri_Type.__name__=_F
_FsMIDot1qFutureVlanTunnelBpduPri_Object=MibTableColumn
fsMIDot1qFutureVlanTunnelBpduPri=_FsMIDot1qFutureVlanTunnelBpduPri_Object((1,3,6,1,4,1,10876,101,1,120,2,1,1,2),_FsMIDot1qFutureVlanTunnelBpduPri_Type())
fsMIDot1qFutureVlanTunnelBpduPri.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanTunnelBpduPri.setStatus(_E)
_FsMIDot1qFutureVlanTunnelTable_Object=MibTable
fsMIDot1qFutureVlanTunnelTable=_FsMIDot1qFutureVlanTunnelTable_Object((1,3,6,1,4,1,10876,101,1,120,2,2))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanTunnelTable.setStatus(_E)
_FsMIDot1qFutureVlanTunnelEntry_Object=MibTableRow
fsMIDot1qFutureVlanTunnelEntry=_FsMIDot1qFutureVlanTunnelEntry_Object((1,3,6,1,4,1,10876,101,1,120,2,2,1))
fsMIDot1qFutureVlanTunnelEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanTunnelEntry.setStatus(_E)
class _FsMIDot1qFutureVlanTunnelStatus_Type(EnabledStatus):defaultValue=2
_FsMIDot1qFutureVlanTunnelStatus_Type.__name__=_I
_FsMIDot1qFutureVlanTunnelStatus_Object=MibTableColumn
fsMIDot1qFutureVlanTunnelStatus=_FsMIDot1qFutureVlanTunnelStatus_Object((1,3,6,1,4,1,10876,101,1,120,2,2,1,1),_FsMIDot1qFutureVlanTunnelStatus_Type())
fsMIDot1qFutureVlanTunnelStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanTunnelStatus.setStatus(_E)
_FsMIDot1qFutureVlanTunnelProtocolTable_Object=MibTable
fsMIDot1qFutureVlanTunnelProtocolTable=_FsMIDot1qFutureVlanTunnelProtocolTable_Object((1,3,6,1,4,1,10876,101,1,120,2,3))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanTunnelProtocolTable.setStatus(_E)
_FsMIDot1qFutureVlanTunnelProtocolEntry_Object=MibTableRow
fsMIDot1qFutureVlanTunnelProtocolEntry=_FsMIDot1qFutureVlanTunnelProtocolEntry_Object((1,3,6,1,4,1,10876,101,1,120,2,3,1))
fsMIDot1qFutureVlanTunnelProtocolEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:fsMIDot1qFutureVlanTunnelProtocolEntry.setStatus(_E)
class _FsMIDot1qFutureVlanTunnelStpPDUs_Type(EnabledStatus):defaultValue=2
_FsMIDot1qFutureVlanTunnelStpPDUs_Type.__name__=_I
_FsMIDot1qFutureVlanTunnelStpPDUs_Object=MibTableColumn
fsMIDot1qFutureVlanTunnelStpPDUs=_FsMIDot1qFutureVlanTunnelStpPDUs_Object((1,3,6,1,4,1,10876,101,1,120,2,3,1,1),_FsMIDot1qFutureVlanTunnelStpPDUs_Type())
fsMIDot1qFutureVlanTunnelStpPDUs.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanTunnelStpPDUs.setStatus(_E)
_FsMIDot1qFutureVlanTunnelStpPDUsRecvd_Type=Counter32
_FsMIDot1qFutureVlanTunnelStpPDUsRecvd_Object=MibTableColumn
fsMIDot1qFutureVlanTunnelStpPDUsRecvd=_FsMIDot1qFutureVlanTunnelStpPDUsRecvd_Object((1,3,6,1,4,1,10876,101,1,120,2,3,1,2),_FsMIDot1qFutureVlanTunnelStpPDUsRecvd_Type())
fsMIDot1qFutureVlanTunnelStpPDUsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanTunnelStpPDUsRecvd.setStatus(_E)
_FsMIDot1qFutureVlanTunnelStpPDUsSent_Type=Counter32
_FsMIDot1qFutureVlanTunnelStpPDUsSent_Object=MibTableColumn
fsMIDot1qFutureVlanTunnelStpPDUsSent=_FsMIDot1qFutureVlanTunnelStpPDUsSent_Object((1,3,6,1,4,1,10876,101,1,120,2,3,1,3),_FsMIDot1qFutureVlanTunnelStpPDUsSent_Type())
fsMIDot1qFutureVlanTunnelStpPDUsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanTunnelStpPDUsSent.setStatus(_E)
class _FsMIDot1qFutureVlanTunnelGvrpPDUs_Type(EnabledStatus):defaultValue=1
_FsMIDot1qFutureVlanTunnelGvrpPDUs_Type.__name__=_I
_FsMIDot1qFutureVlanTunnelGvrpPDUs_Object=MibTableColumn
fsMIDot1qFutureVlanTunnelGvrpPDUs=_FsMIDot1qFutureVlanTunnelGvrpPDUs_Object((1,3,6,1,4,1,10876,101,1,120,2,3,1,4),_FsMIDot1qFutureVlanTunnelGvrpPDUs_Type())
fsMIDot1qFutureVlanTunnelGvrpPDUs.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanTunnelGvrpPDUs.setStatus(_E)
_FsMIDot1qFutureVlanTunnelGvrpPDUsRecvd_Type=Counter32
_FsMIDot1qFutureVlanTunnelGvrpPDUsRecvd_Object=MibTableColumn
fsMIDot1qFutureVlanTunnelGvrpPDUsRecvd=_FsMIDot1qFutureVlanTunnelGvrpPDUsRecvd_Object((1,3,6,1,4,1,10876,101,1,120,2,3,1,5),_FsMIDot1qFutureVlanTunnelGvrpPDUsRecvd_Type())
fsMIDot1qFutureVlanTunnelGvrpPDUsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanTunnelGvrpPDUsRecvd.setStatus(_E)
_FsMIDot1qFutureVlanTunnelGvrpPDUsSent_Type=Counter32
_FsMIDot1qFutureVlanTunnelGvrpPDUsSent_Object=MibTableColumn
fsMIDot1qFutureVlanTunnelGvrpPDUsSent=_FsMIDot1qFutureVlanTunnelGvrpPDUsSent_Object((1,3,6,1,4,1,10876,101,1,120,2,3,1,6),_FsMIDot1qFutureVlanTunnelGvrpPDUsSent_Type())
fsMIDot1qFutureVlanTunnelGvrpPDUsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanTunnelGvrpPDUsSent.setStatus(_E)
class _FsMIDot1qFutureVlanTunnelIgmpPkts_Type(EnabledStatus):defaultValue=1
_FsMIDot1qFutureVlanTunnelIgmpPkts_Type.__name__=_I
_FsMIDot1qFutureVlanTunnelIgmpPkts_Object=MibTableColumn
fsMIDot1qFutureVlanTunnelIgmpPkts=_FsMIDot1qFutureVlanTunnelIgmpPkts_Object((1,3,6,1,4,1,10876,101,1,120,2,3,1,7),_FsMIDot1qFutureVlanTunnelIgmpPkts_Type())
fsMIDot1qFutureVlanTunnelIgmpPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanTunnelIgmpPkts.setStatus(_E)
_FsMIDot1qFutureVlanTunnelIgmpPktsRecvd_Type=Counter32
_FsMIDot1qFutureVlanTunnelIgmpPktsRecvd_Object=MibTableColumn
fsMIDot1qFutureVlanTunnelIgmpPktsRecvd=_FsMIDot1qFutureVlanTunnelIgmpPktsRecvd_Object((1,3,6,1,4,1,10876,101,1,120,2,3,1,8),_FsMIDot1qFutureVlanTunnelIgmpPktsRecvd_Type())
fsMIDot1qFutureVlanTunnelIgmpPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanTunnelIgmpPktsRecvd.setStatus(_E)
_FsMIDot1qFutureVlanTunnelIgmpPktsSent_Type=Counter32
_FsMIDot1qFutureVlanTunnelIgmpPktsSent_Object=MibTableColumn
fsMIDot1qFutureVlanTunnelIgmpPktsSent=_FsMIDot1qFutureVlanTunnelIgmpPktsSent_Object((1,3,6,1,4,1,10876,101,1,120,2,3,1,9),_FsMIDot1qFutureVlanTunnelIgmpPktsSent_Type())
fsMIDot1qFutureVlanTunnelIgmpPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDot1qFutureVlanTunnelIgmpPktsSent.setStatus(_E)
_FsMIDot1qFutureVlanTraps_ObjectIdentity=ObjectIdentity
fsMIDot1qFutureVlanTraps=_FsMIDot1qFutureVlanTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,120,3))
_FsMIDot1qVlanTraps_ObjectIdentity=ObjectIdentity
fsMIDot1qVlanTraps=_FsMIDot1qVlanTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,120,3,0))
_FsMIDot1qFutureVlanTrapControl_ObjectIdentity=ObjectIdentity
fsMIDot1qFutureVlanTrapControl=_FsMIDot1qFutureVlanTrapControl_ObjectIdentity((1,3,6,1,4,1,10876,101,1,120,4))
fsDot1qTpFdbEntry.registerAugmentions((_D,_d))
fsMIDot1qFutureVlanTpFdbEntry.setIndexNames(*fsDot1qTpFdbEntry.getIndexNames())
fsDot1qStaticUnicastEntry.registerAugmentions((_D,_e))
fsMIDot1qFutureStaticUnicastExtnEntry.setIndexNames(*fsDot1qStaticUnicastEntry.getIndexNames())
fsDot1qVlanStaticEntry.registerAugmentions((_D,_f))
fsMIDot1qFutureStVlanExtEntry.setIndexNames(*fsDot1qVlanStaticEntry.getIndexNames())
fsDot1qVlanStaticPortConfigEntry.registerAugmentions((_D,_g))
fsMIDot1qFuturePortVlanExtEntry.setIndexNames(*fsDot1qVlanStaticPortConfigEntry.getIndexNames())
fsMIDot1qFutureMacThresholdTrap=NotificationType((1,3,6,1,4,1,10876,101,1,120,3,0,1))
fsMIDot1qFutureMacThresholdTrap.setObjects(*((_D,_N),(_D,_L),(_D,_h)))
if mibBuilder.loadTexts:fsMIDot1qFutureMacThresholdTrap.setStatus(_A)
fsMIDot1qFutureSrcRelearnTrap=NotificationType((1,3,6,1,4,1,10876,101,1,120,3,0,2))
fsMIDot1qFutureSrcRelearnTrap.setObjects(*((_D,_N),(_D,_i),(_O,_T),(_D,_j)))
if mibBuilder.loadTexts:fsMIDot1qFutureSrcRelearnTrap.setStatus(_A)
fsMIDot1qFutureSwitchMacLimitTrap=NotificationType((1,3,6,1,4,1,10876,101,1,120,3,0,3))
fsMIDot1qFutureSwitchMacLimitTrap.setObjects(*((_D,_N),(_D,_k)))
if mibBuilder.loadTexts:fsMIDot1qFutureSwitchMacLimitTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'VlanId':VlanId,_I:EnabledStatus,_Z:MacLearningStatus,'futureMIVlanMIB':futureMIVlanMIB,'fsMIDot1qFutureVlan':fsMIDot1qFutureVlan,'fsMIDot1qFutureVlanGlobalTrace':fsMIDot1qFutureVlanGlobalTrace,'fsMIDot1qFutureVlanGlobalsTable':fsMIDot1qFutureVlanGlobalsTable,'fsMIDot1qFutureVlanGlobalsEntry':fsMIDot1qFutureVlanGlobalsEntry,_H:fsMIDot1qFutureVlanContextId,'fsMIDot1qFutureVlanStatus':fsMIDot1qFutureVlanStatus,'fsMIDot1qFutureVlanMacBasedOnAllPorts':fsMIDot1qFutureVlanMacBasedOnAllPorts,'fsMIDot1qFutureVlanPortProtoBasedOnAllPorts':fsMIDot1qFutureVlanPortProtoBasedOnAllPorts,'fsMIDot1qFutureVlanShutdownStatus':fsMIDot1qFutureVlanShutdownStatus,'fsMIDot1qFutureGarpShutdownStatus':fsMIDot1qFutureGarpShutdownStatus,'fsMIDot1qFutureVlanDebug':fsMIDot1qFutureVlanDebug,'fsMIDot1qFutureVlanLearningMode':fsMIDot1qFutureVlanLearningMode,'fsMIDot1qFutureVlanHybridTypeDefault':fsMIDot1qFutureVlanHybridTypeDefault,'fsMIDot1qFutureVlanOperStatus':fsMIDot1qFutureVlanOperStatus,'fsMIDot1qFutureGvrpOperStatus':fsMIDot1qFutureGvrpOperStatus,'fsMIDot1qFutureGmrpOperStatus':fsMIDot1qFutureGmrpOperStatus,_N:fsMIDot1qFutureVlanContextName,'fsMIDot1qFutureGarpDebug':fsMIDot1qFutureGarpDebug,_k:fsMIDot1qFutureUnicastMacLearningLimit,'fsMIDot1qFutureBaseBridgeMode':fsMIDot1qFutureBaseBridgeMode,'fsMIDot1qFutureVlanSubnetBasedOnAllPorts':fsMIDot1qFutureVlanSubnetBasedOnAllPorts,'fsMIDot1qFutureVlanGlobalMacLearningStatus':fsMIDot1qFutureVlanGlobalMacLearningStatus,'fsMIDot1qFutureVlanApplyEnhancedFilteringCriteria':fsMIDot1qFutureVlanApplyEnhancedFilteringCriteria,'fsMIDot1qFutureVlanGlobalsFdbFlush':fsMIDot1qFutureVlanGlobalsFdbFlush,'fsMIDot1qFutureVlanPortTable':fsMIDot1qFutureVlanPortTable,'fsMIDot1qFutureVlanPortEntry':fsMIDot1qFutureVlanPortEntry,_M:fsMIDot1qFutureVlanPort,'fsMIDot1qFutureVlanPortType':fsMIDot1qFutureVlanPortType,'fsMIDot1qFutureVlanPortPortProtoBasedClassification':fsMIDot1qFutureVlanPortPortProtoBasedClassification,'fsMIDot1qFutureVlanFilteringUtilityCriteria':fsMIDot1qFutureVlanFilteringUtilityCriteria,'fsMIDot1qFutureVlanPortProtected':fsMIDot1qFutureVlanPortProtected,'fsMIDot1qFutureVlanPortUnicastMacLearning':fsMIDot1qFutureVlanPortUnicastMacLearning,'fsMIDot1qFutureVlanPortGmrpJoinEmptyTxCount':fsMIDot1qFutureVlanPortGmrpJoinEmptyTxCount,'fsMIDot1qFutureVlanPortGmrpJoinEmptyRxCount':fsMIDot1qFutureVlanPortGmrpJoinEmptyRxCount,'fsMIDot1qFutureVlanPortGmrpJoinInTxCount':fsMIDot1qFutureVlanPortGmrpJoinInTxCount,'fsMIDot1qFutureVlanPortGmrpJoinInRxCount':fsMIDot1qFutureVlanPortGmrpJoinInRxCount,'fsMIDot1qFutureVlanPortGmrpLeaveInTxCount':fsMIDot1qFutureVlanPortGmrpLeaveInTxCount,'fsMIDot1qFutureVlanPortGmrpLeaveInRxCount':fsMIDot1qFutureVlanPortGmrpLeaveInRxCount,'fsMIDot1qFutureVlanPortGmrpLeaveEmptyTxCount':fsMIDot1qFutureVlanPortGmrpLeaveEmptyTxCount,'fsMIDot1qFutureVlanPortGmrpLeaveEmptyRxCount':fsMIDot1qFutureVlanPortGmrpLeaveEmptyRxCount,'fsMIDot1qFutureVlanPortGmrpEmptyTxCount':fsMIDot1qFutureVlanPortGmrpEmptyTxCount,'fsMIDot1qFutureVlanPortGmrpEmptyRxCount':fsMIDot1qFutureVlanPortGmrpEmptyRxCount,'fsMIDot1qFutureVlanPortGmrpLeaveAllTxCount':fsMIDot1qFutureVlanPortGmrpLeaveAllTxCount,'fsMIDot1qFutureVlanPortGmrpLeaveAllRxCount':fsMIDot1qFutureVlanPortGmrpLeaveAllRxCount,'fsMIDot1qFutureVlanPortGmrpDiscardCount':fsMIDot1qFutureVlanPortGmrpDiscardCount,'fsMIDot1qFutureVlanPortGvrpJoinEmptyTxCount':fsMIDot1qFutureVlanPortGvrpJoinEmptyTxCount,'fsMIDot1qFutureVlanPortGvrpJoinEmptyRxCount':fsMIDot1qFutureVlanPortGvrpJoinEmptyRxCount,'fsMIDot1qFutureVlanPortGvrpJoinInTxCount':fsMIDot1qFutureVlanPortGvrpJoinInTxCount,'fsMIDot1qFutureVlanPortGvrpJoinInRxCount':fsMIDot1qFutureVlanPortGvrpJoinInRxCount,'fsMIDot1qFutureVlanPortGvrpLeaveInTxCount':fsMIDot1qFutureVlanPortGvrpLeaveInTxCount,'fsMIDot1qFutureVlanPortGvrpLeaveInRxCount':fsMIDot1qFutureVlanPortGvrpLeaveInRxCount,'fsMIDot1qFutureVlanPortGvrpLeaveEmptyTxCount':fsMIDot1qFutureVlanPortGvrpLeaveEmptyTxCount,'fsMIDot1qFutureVlanPortGvrpLeaveEmptyRxCount':fsMIDot1qFutureVlanPortGvrpLeaveEmptyRxCount,'fsMIDot1qFutureVlanPortGvrpEmptyTxCount':fsMIDot1qFutureVlanPortGvrpEmptyTxCount,'fsMIDot1qFutureVlanPortGvrpEmptyRxCount':fsMIDot1qFutureVlanPortGvrpEmptyRxCount,'fsMIDot1qFutureVlanPortGvrpLeaveAllTxCount':fsMIDot1qFutureVlanPortGvrpLeaveAllTxCount,'fsMIDot1qFutureVlanPortGvrpLeaveAllRxCount':fsMIDot1qFutureVlanPortGvrpLeaveAllRxCount,'fsMIDot1qFutureVlanPortGvrpDiscardCount':fsMIDot1qFutureVlanPortGvrpDiscardCount,'fsMIDot1qFutureVlanPortFdbFlush':fsMIDot1qFutureVlanPortFdbFlush,'fsMIDot1qFutureVlanPortAllowedVlanList':fsMIDot1qFutureVlanPortAllowedVlanList,'fsMIDot1qFutureVlanPortMacMapTable':fsMIDot1qFutureVlanPortMacMapTable,'fsMIDot1qFutureVlanPortMacMapEntry':fsMIDot1qFutureVlanPortMacMapEntry,_Y:fsMIDot1qFutureVlanPortMacMapAddr,'fsMIDot1qFutureVlanPortMacMapVid':fsMIDot1qFutureVlanPortMacMapVid,'fsMIDot1qFutureVlanPortMacMapRowStatus':fsMIDot1qFutureVlanPortMacMapRowStatus,'fsMIDot1qFutureVlanFidMapTable':fsMIDot1qFutureVlanFidMapTable,'fsMIDot1qFutureVlanFidMapEntry':fsMIDot1qFutureVlanFidMapEntry,_L:fsMIDot1qFutureVlanIndex,_i:fsMIDot1qFutureVlanFid,'fsMIDot1qFutureVlanCounterTable':fsMIDot1qFutureVlanCounterTable,'fsMIDot1qFutureVlanCounterEntry':fsMIDot1qFutureVlanCounterEntry,'fsMIDot1qFutureVlanCounterRxUcast':fsMIDot1qFutureVlanCounterRxUcast,'fsMIDot1qFutureVlanCounterRxMcastBcast':fsMIDot1qFutureVlanCounterRxMcastBcast,'fsMIDot1qFutureVlanCounterTxUnknUcast':fsMIDot1qFutureVlanCounterTxUnknUcast,'fsMIDot1qFutureVlanCounterTxUcast':fsMIDot1qFutureVlanCounterTxUcast,'fsMIDot1qFutureVlanCounterTxBcast':fsMIDot1qFutureVlanCounterTxBcast,'fsMIDot1qFutureVlanCounterStatus':fsMIDot1qFutureVlanCounterStatus,'fsMIDot1qFutureVlanUnicastMacControlTable':fsMIDot1qFutureVlanUnicastMacControlTable,'fsMIDot1qFutureVlanUnicastMacControlEntry':fsMIDot1qFutureVlanUnicastMacControlEntry,_h:fsMIDot1qFutureVlanUnicastMacLimit,'fsMIDot1qFutureVlanAdminMacLearningStatus':fsMIDot1qFutureVlanAdminMacLearningStatus,'fsMIDot1qFutureVlanOperMacLearningStatus':fsMIDot1qFutureVlanOperMacLearningStatus,'fsMIDot1qFutureGarpGlobalTrace':fsMIDot1qFutureGarpGlobalTrace,'fsMIDot1qFutureVlanTpFdbTable':fsMIDot1qFutureVlanTpFdbTable,_d:fsMIDot1qFutureVlanTpFdbEntry,_j:fsMIDot1qFutureVlanOldTpFdbPort,'fsMIDot1qFutureConnectionIdentifier':fsMIDot1qFutureConnectionIdentifier,'fsMIDot1qFutureVlanWildCardTable':fsMIDot1qFutureVlanWildCardTable,'fsMIDot1qFutureVlanWildCardEntry':fsMIDot1qFutureVlanWildCardEntry,_P:fsMIDot1qFutureVlanWildCardMacAddress,'fsMIDot1qFutureVlanWildCardRowStatus':fsMIDot1qFutureVlanWildCardRowStatus,'fsMIDot1qFutureVlanWildCardPortTable':fsMIDot1qFutureVlanWildCardPortTable,'fsMIDot1qFutureVlanWildCardPortEntry':fsMIDot1qFutureVlanWildCardPortEntry,'fsMIDot1qFutureVlanIsWildCardEgressPort':fsMIDot1qFutureVlanIsWildCardEgressPort,'fsMIDot1qFutureStaticUnicastExtnTable':fsMIDot1qFutureStaticUnicastExtnTable,_e:fsMIDot1qFutureStaticUnicastExtnEntry,'fsMIDot1qFutureStaticConnectionIdentifier':fsMIDot1qFutureStaticConnectionIdentifier,'fsMIDot1qFutureVlanPortSubnetMapTable':fsMIDot1qFutureVlanPortSubnetMapTable,'fsMIDot1qFutureVlanPortSubnetMapEntry':fsMIDot1qFutureVlanPortSubnetMapEntry,_a:fsMIDot1qFutureVlanPortSubnetMapAddr,'fsMIDot1qFutureVlanPortSubnetMapVid':fsMIDot1qFutureVlanPortSubnetMapVid,'fsMIDot1qFutureVlanPortSubnetMapRowStatus':fsMIDot1qFutureVlanPortSubnetMapRowStatus,'fsMIDot1qFutureVlanSwStatsEnabled':fsMIDot1qFutureVlanSwStatsEnabled,'fsMIDot1qFutureStVlanExtTable':fsMIDot1qFutureStVlanExtTable,_f:fsMIDot1qFutureStVlanExtEntry,'fsMIDot1qFutureStVlanPVlanType':fsMIDot1qFutureStVlanPVlanType,'fsMIDot1qFutureStVlanPrimaryVid':fsMIDot1qFutureStVlanPrimaryVid,'fsMIDot1qFutureStVlanFdbFlush':fsMIDot1qFutureStVlanFdbFlush,'fsMIDot1qFutureVlanPortSubnetMapExtTable':fsMIDot1qFutureVlanPortSubnetMapExtTable,'fsMIDot1qFutureVlanPortSubnetMapExtEntry':fsMIDot1qFutureVlanPortSubnetMapExtEntry,_b:fsMIDot1qFutureVlanPortSubnetMapExtAddr,_c:fsMIDot1qFutureVlanPortSubnetMapExtMask,'fsMIDot1qFutureVlanPortSubnetMapExtVid':fsMIDot1qFutureVlanPortSubnetMapExtVid,'fsMIDot1qFutureVlanPortSubnetMapExtRowStatus':fsMIDot1qFutureVlanPortSubnetMapExtRowStatus,'fsMIDot1qFuturePortVlanExtTable':fsMIDot1qFuturePortVlanExtTable,_g:fsMIDot1qFuturePortVlanExtEntry,'fsMIDot1qFuturePortVlanFdbFlush':fsMIDot1qFuturePortVlanFdbFlush,'fsMIDot1qFutureVlanTunnelConfig':fsMIDot1qFutureVlanTunnelConfig,'fsMIDot1qFutureVlanTunnelConfigTable':fsMIDot1qFutureVlanTunnelConfigTable,'fsMIDot1qFutureVlanTunnelConfigEntry':fsMIDot1qFutureVlanTunnelConfigEntry,'fsMIDot1qFutureVlanBridgeMode':fsMIDot1qFutureVlanBridgeMode,'fsMIDot1qFutureVlanTunnelBpduPri':fsMIDot1qFutureVlanTunnelBpduPri,'fsMIDot1qFutureVlanTunnelTable':fsMIDot1qFutureVlanTunnelTable,'fsMIDot1qFutureVlanTunnelEntry':fsMIDot1qFutureVlanTunnelEntry,'fsMIDot1qFutureVlanTunnelStatus':fsMIDot1qFutureVlanTunnelStatus,'fsMIDot1qFutureVlanTunnelProtocolTable':fsMIDot1qFutureVlanTunnelProtocolTable,'fsMIDot1qFutureVlanTunnelProtocolEntry':fsMIDot1qFutureVlanTunnelProtocolEntry,'fsMIDot1qFutureVlanTunnelStpPDUs':fsMIDot1qFutureVlanTunnelStpPDUs,'fsMIDot1qFutureVlanTunnelStpPDUsRecvd':fsMIDot1qFutureVlanTunnelStpPDUsRecvd,'fsMIDot1qFutureVlanTunnelStpPDUsSent':fsMIDot1qFutureVlanTunnelStpPDUsSent,'fsMIDot1qFutureVlanTunnelGvrpPDUs':fsMIDot1qFutureVlanTunnelGvrpPDUs,'fsMIDot1qFutureVlanTunnelGvrpPDUsRecvd':fsMIDot1qFutureVlanTunnelGvrpPDUsRecvd,'fsMIDot1qFutureVlanTunnelGvrpPDUsSent':fsMIDot1qFutureVlanTunnelGvrpPDUsSent,'fsMIDot1qFutureVlanTunnelIgmpPkts':fsMIDot1qFutureVlanTunnelIgmpPkts,'fsMIDot1qFutureVlanTunnelIgmpPktsRecvd':fsMIDot1qFutureVlanTunnelIgmpPktsRecvd,'fsMIDot1qFutureVlanTunnelIgmpPktsSent':fsMIDot1qFutureVlanTunnelIgmpPktsSent,'fsMIDot1qFutureVlanTraps':fsMIDot1qFutureVlanTraps,'fsMIDot1qVlanTraps':fsMIDot1qVlanTraps,'fsMIDot1qFutureMacThresholdTrap':fsMIDot1qFutureMacThresholdTrap,'fsMIDot1qFutureSrcRelearnTrap':fsMIDot1qFutureSrcRelearnTrap,'fsMIDot1qFutureSwitchMacLimitTrap':fsMIDot1qFutureSwitchMacLimitTrap,'fsMIDot1qFutureVlanTrapControl':fsMIDot1qFutureVlanTrapControl})