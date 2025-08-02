_f='dot1qFutureUnicastMacLearningLimit'
_e='dot1qTpOldFdbPort'
_d='dot1qFutureVlanFid'
_c='dot1qFutureVlanUnicastMacLimit'
_b='dot1qFutureStVlanExtEntry'
_a='dot1qFutureStaticUnicastExtnEntry'
_Z='dot1qFutureVlanTpFdbEntry'
_Y='dot1qFutureVlanPortSubnetMapExtMask'
_X='dot1qFutureVlanPortSubnetMapExtAddr'
_W='dot1qFutureVlanPortSubnetMapAddr'
_V='dot1qFutureVlanWildCardMacAddress'
_U='MacLearningStatus'
_T='dot1qFutureVlanPortMacMapAddr'
_S='default'
_R='disabled'
_Q='enabled'
_P='dot1qTpFdbPort'
_O='VlanIdOrNone'
_N='Q-BRIDGE-MIB'
_M='OctetString'
_L='dot1qFutureVlanPort'
_K='dot1qFutureVlanIndex'
_J='Unsigned32'
_I='not-accessible'
_H='TruthValue'
_G='EnabledStatus'
_F='Integer32'
_E='deprecated'
_D='SUPERMICRO-VLAN-MIB'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,VlanIdOrNone,dot1qStaticUnicastEntry,dot1qTpFdbEntry,dot1qTpFdbPort,dot1qVlanStaticEntry=mibBuilder.importSymbols(_N,'PortList',_O,'dot1qStaticUnicastEntry','dot1qTpFdbEntry',_P,'dot1qVlanStaticEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_H)
futureVlanMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,1,65))
if mibBuilder.loadTexts:futureVlanMIB.setRevisions(('2012-09-05 00:00',))
class VlanId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
class MacLearningStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3)))
_Dot1qFutureVlan_ObjectIdentity=ObjectIdentity
dot1qFutureVlan=_Dot1qFutureVlan_ObjectIdentity((1,3,6,1,4,1,10876,101,1,65,1))
_Dot1qFutureVlanStatus_Type=EnabledStatus
_Dot1qFutureVlanStatus_Object=MibScalar
dot1qFutureVlanStatus=_Dot1qFutureVlanStatus_Object((1,3,6,1,4,1,10876,101,1,65,1,1),_Dot1qFutureVlanStatus_Type())
dot1qFutureVlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanStatus.setStatus(_A)
_Dot1qFutureVlanMacBasedOnAllPorts_Type=EnabledStatus
_Dot1qFutureVlanMacBasedOnAllPorts_Object=MibScalar
dot1qFutureVlanMacBasedOnAllPorts=_Dot1qFutureVlanMacBasedOnAllPorts_Object((1,3,6,1,4,1,10876,101,1,65,1,2),_Dot1qFutureVlanMacBasedOnAllPorts_Type())
dot1qFutureVlanMacBasedOnAllPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanMacBasedOnAllPorts.setStatus(_A)
_Dot1qFutureVlanPortProtoBasedOnAllPorts_Type=EnabledStatus
_Dot1qFutureVlanPortProtoBasedOnAllPorts_Object=MibScalar
dot1qFutureVlanPortProtoBasedOnAllPorts=_Dot1qFutureVlanPortProtoBasedOnAllPorts_Object((1,3,6,1,4,1,10876,101,1,65,1,3),_Dot1qFutureVlanPortProtoBasedOnAllPorts_Type())
dot1qFutureVlanPortProtoBasedOnAllPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortProtoBasedOnAllPorts.setStatus(_A)
class _Dot1qFutureVlanShutdownStatus_Type(TruthValue):defaultValue=2
_Dot1qFutureVlanShutdownStatus_Type.__name__=_H
_Dot1qFutureVlanShutdownStatus_Object=MibScalar
dot1qFutureVlanShutdownStatus=_Dot1qFutureVlanShutdownStatus_Object((1,3,6,1,4,1,10876,101,1,65,1,5),_Dot1qFutureVlanShutdownStatus_Type())
dot1qFutureVlanShutdownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanShutdownStatus.setStatus(_A)
class _Dot1qFutureGarpShutdownStatus_Type(TruthValue):defaultValue=2
_Dot1qFutureGarpShutdownStatus_Type.__name__=_H
_Dot1qFutureGarpShutdownStatus_Object=MibScalar
dot1qFutureGarpShutdownStatus=_Dot1qFutureGarpShutdownStatus_Object((1,3,6,1,4,1,10876,101,1,65,1,6),_Dot1qFutureGarpShutdownStatus_Type())
dot1qFutureGarpShutdownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureGarpShutdownStatus.setStatus(_A)
class _Dot1qFutureVlanDebug_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,524287))
_Dot1qFutureVlanDebug_Type.__name__=_F
_Dot1qFutureVlanDebug_Object=MibScalar
dot1qFutureVlanDebug=_Dot1qFutureVlanDebug_Object((1,3,6,1,4,1,10876,101,1,65,1,7),_Dot1qFutureVlanDebug_Type())
dot1qFutureVlanDebug.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanDebug.setStatus(_A)
class _Dot1qFutureVlanLearningMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ivl',1),('svl',2),('hybrid',3)))
_Dot1qFutureVlanLearningMode_Type.__name__=_F
_Dot1qFutureVlanLearningMode_Object=MibScalar
dot1qFutureVlanLearningMode=_Dot1qFutureVlanLearningMode_Object((1,3,6,1,4,1,10876,101,1,65,1,8),_Dot1qFutureVlanLearningMode_Type())
dot1qFutureVlanLearningMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qFutureVlanLearningMode.setStatus(_A)
class _Dot1qFutureVlanHybridTypeDefault_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ivl',1),('svl',2)))
_Dot1qFutureVlanHybridTypeDefault_Type.__name__=_F
_Dot1qFutureVlanHybridTypeDefault_Object=MibScalar
dot1qFutureVlanHybridTypeDefault=_Dot1qFutureVlanHybridTypeDefault_Object((1,3,6,1,4,1,10876,101,1,65,1,9),_Dot1qFutureVlanHybridTypeDefault_Type())
dot1qFutureVlanHybridTypeDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qFutureVlanHybridTypeDefault.setStatus(_A)
_Dot1qFutureVlanPortTable_Object=MibTable
dot1qFutureVlanPortTable=_Dot1qFutureVlanPortTable_Object((1,3,6,1,4,1,10876,101,1,65,1,10))
if mibBuilder.loadTexts:dot1qFutureVlanPortTable.setStatus(_A)
_Dot1qFutureVlanPortEntry_Object=MibTableRow
dot1qFutureVlanPortEntry=_Dot1qFutureVlanPortEntry_Object((1,3,6,1,4,1,10876,101,1,65,1,10,1))
dot1qFutureVlanPortEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:dot1qFutureVlanPortEntry.setStatus(_A)
class _Dot1qFutureVlanPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1qFutureVlanPort_Type.__name__=_F
_Dot1qFutureVlanPort_Object=MibTableColumn
dot1qFutureVlanPort=_Dot1qFutureVlanPort_Object((1,3,6,1,4,1,10876,101,1,65,1,10,1,1),_Dot1qFutureVlanPort_Type())
dot1qFutureVlanPort.setMaxAccess(_I)
if mibBuilder.loadTexts:dot1qFutureVlanPort.setStatus(_A)
class _Dot1qFutureVlanPortType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('accessPort',1),('trunkPort',2),('hybridPort',3),('hostPort',4),('promiscuousPort',5)))
_Dot1qFutureVlanPortType_Type.__name__=_F
_Dot1qFutureVlanPortType_Object=MibTableColumn
dot1qFutureVlanPortType=_Dot1qFutureVlanPortType_Object((1,3,6,1,4,1,10876,101,1,65,1,10,1,2),_Dot1qFutureVlanPortType_Type())
dot1qFutureVlanPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortType.setStatus(_A)
_Dot1qFutureVlanPortPortProtoBasedClassification_Type=EnabledStatus
_Dot1qFutureVlanPortPortProtoBasedClassification_Object=MibTableColumn
dot1qFutureVlanPortPortProtoBasedClassification=_Dot1qFutureVlanPortPortProtoBasedClassification_Object((1,3,6,1,4,1,10876,101,1,65,1,10,1,4),_Dot1qFutureVlanPortPortProtoBasedClassification_Type())
dot1qFutureVlanPortPortProtoBasedClassification.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortPortProtoBasedClassification.setStatus(_A)
class _Dot1qFutureVlanFilteringUtilityCriteria_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),('enhanced',2)))
_Dot1qFutureVlanFilteringUtilityCriteria_Type.__name__=_F
_Dot1qFutureVlanFilteringUtilityCriteria_Object=MibTableColumn
dot1qFutureVlanFilteringUtilityCriteria=_Dot1qFutureVlanFilteringUtilityCriteria_Object((1,3,6,1,4,1,10876,101,1,65,1,10,1,5),_Dot1qFutureVlanFilteringUtilityCriteria_Type())
dot1qFutureVlanFilteringUtilityCriteria.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanFilteringUtilityCriteria.setStatus(_A)
class _Dot1qFutureVlanPortProtected_Type(TruthValue):defaultValue=2
_Dot1qFutureVlanPortProtected_Type.__name__=_H
_Dot1qFutureVlanPortProtected_Object=MibTableColumn
dot1qFutureVlanPortProtected=_Dot1qFutureVlanPortProtected_Object((1,3,6,1,4,1,10876,101,1,65,1,10,1,6),_Dot1qFutureVlanPortProtected_Type())
dot1qFutureVlanPortProtected.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortProtected.setStatus(_A)
class _Dot1qFutureVlanPortUnicastMacLearning_Type(EnabledStatus):defaultValue=1
_Dot1qFutureVlanPortUnicastMacLearning_Type.__name__=_G
_Dot1qFutureVlanPortUnicastMacLearning_Object=MibTableColumn
dot1qFutureVlanPortUnicastMacLearning=_Dot1qFutureVlanPortUnicastMacLearning_Object((1,3,6,1,4,1,10876,101,1,65,1,10,1,8),_Dot1qFutureVlanPortUnicastMacLearning_Type())
dot1qFutureVlanPortUnicastMacLearning.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortUnicastMacLearning.setStatus(_A)
class _Dot1qFutureVlanPortAllowedVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_Dot1qFutureVlanPortAllowedVlanList_Type.__name__=_M
_Dot1qFutureVlanPortAllowedVlanList_Object=MibTableColumn
dot1qFutureVlanPortAllowedVlanList=_Dot1qFutureVlanPortAllowedVlanList_Object((1,3,6,1,4,1,10876,101,1,65,1,10,1,9),_Dot1qFutureVlanPortAllowedVlanList_Type())
dot1qFutureVlanPortAllowedVlanList.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortAllowedVlanList.setStatus(_A)
_Dot1qFutureVlanPortMacMapTable_Object=MibTable
dot1qFutureVlanPortMacMapTable=_Dot1qFutureVlanPortMacMapTable_Object((1,3,6,1,4,1,10876,101,1,65,1,11))
if mibBuilder.loadTexts:dot1qFutureVlanPortMacMapTable.setStatus(_A)
_Dot1qFutureVlanPortMacMapEntry_Object=MibTableRow
dot1qFutureVlanPortMacMapEntry=_Dot1qFutureVlanPortMacMapEntry_Object((1,3,6,1,4,1,10876,101,1,65,1,11,1))
dot1qFutureVlanPortMacMapEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:dot1qFutureVlanPortMacMapEntry.setStatus(_A)
_Dot1qFutureVlanPortMacMapAddr_Type=MacAddress
_Dot1qFutureVlanPortMacMapAddr_Object=MibTableColumn
dot1qFutureVlanPortMacMapAddr=_Dot1qFutureVlanPortMacMapAddr_Object((1,3,6,1,4,1,10876,101,1,65,1,11,1,1),_Dot1qFutureVlanPortMacMapAddr_Type())
dot1qFutureVlanPortMacMapAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:dot1qFutureVlanPortMacMapAddr.setStatus(_A)
_Dot1qFutureVlanPortMacMapVid_Type=VlanId
_Dot1qFutureVlanPortMacMapVid_Object=MibTableColumn
dot1qFutureVlanPortMacMapVid=_Dot1qFutureVlanPortMacMapVid_Object((1,3,6,1,4,1,10876,101,1,65,1,11,1,2),_Dot1qFutureVlanPortMacMapVid_Type())
dot1qFutureVlanPortMacMapVid.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortMacMapVid.setStatus(_A)
_Dot1qFutureVlanPortMacMapRowStatus_Type=RowStatus
_Dot1qFutureVlanPortMacMapRowStatus_Object=MibTableColumn
dot1qFutureVlanPortMacMapRowStatus=_Dot1qFutureVlanPortMacMapRowStatus_Object((1,3,6,1,4,1,10876,101,1,65,1,11,1,5),_Dot1qFutureVlanPortMacMapRowStatus_Type())
dot1qFutureVlanPortMacMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortMacMapRowStatus.setStatus(_A)
_Dot1qFutureVlanFidMapTable_Object=MibTable
dot1qFutureVlanFidMapTable=_Dot1qFutureVlanFidMapTable_Object((1,3,6,1,4,1,10876,101,1,65,1,12))
if mibBuilder.loadTexts:dot1qFutureVlanFidMapTable.setStatus(_A)
_Dot1qFutureVlanFidMapEntry_Object=MibTableRow
dot1qFutureVlanFidMapEntry=_Dot1qFutureVlanFidMapEntry_Object((1,3,6,1,4,1,10876,101,1,65,1,12,1))
dot1qFutureVlanFidMapEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:dot1qFutureVlanFidMapEntry.setStatus(_A)
class _Dot1qFutureVlanIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Dot1qFutureVlanIndex_Type.__name__=_J
_Dot1qFutureVlanIndex_Object=MibTableColumn
dot1qFutureVlanIndex=_Dot1qFutureVlanIndex_Object((1,3,6,1,4,1,10876,101,1,65,1,12,1,1),_Dot1qFutureVlanIndex_Type())
dot1qFutureVlanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qFutureVlanIndex.setStatus(_A)
class _Dot1qFutureVlanFid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Dot1qFutureVlanFid_Type.__name__=_J
_Dot1qFutureVlanFid_Object=MibTableColumn
dot1qFutureVlanFid=_Dot1qFutureVlanFid_Object((1,3,6,1,4,1,10876,101,1,65,1,12,1,2),_Dot1qFutureVlanFid_Type())
dot1qFutureVlanFid.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanFid.setStatus(_A)
_Dot1qFutureVlanOperStatus_Type=EnabledStatus
_Dot1qFutureVlanOperStatus_Object=MibScalar
dot1qFutureVlanOperStatus=_Dot1qFutureVlanOperStatus_Object((1,3,6,1,4,1,10876,101,1,65,1,13),_Dot1qFutureVlanOperStatus_Type())
dot1qFutureVlanOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qFutureVlanOperStatus.setStatus(_A)
_Dot1qFutureGvrpOperStatus_Type=EnabledStatus
_Dot1qFutureGvrpOperStatus_Object=MibScalar
dot1qFutureGvrpOperStatus=_Dot1qFutureGvrpOperStatus_Object((1,3,6,1,4,1,10876,101,1,65,1,14),_Dot1qFutureGvrpOperStatus_Type())
dot1qFutureGvrpOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qFutureGvrpOperStatus.setStatus(_A)
_Dot1qFutureGmrpOperStatus_Type=EnabledStatus
_Dot1qFutureGmrpOperStatus_Object=MibScalar
dot1qFutureGmrpOperStatus=_Dot1qFutureGmrpOperStatus_Object((1,3,6,1,4,1,10876,101,1,65,1,15),_Dot1qFutureGmrpOperStatus_Type())
dot1qFutureGmrpOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qFutureGmrpOperStatus.setStatus(_A)
_Dot1qFutureVlanCounterTable_Object=MibTable
dot1qFutureVlanCounterTable=_Dot1qFutureVlanCounterTable_Object((1,3,6,1,4,1,10876,101,1,65,1,16))
if mibBuilder.loadTexts:dot1qFutureVlanCounterTable.setStatus(_A)
_Dot1qFutureVlanCounterEntry_Object=MibTableRow
dot1qFutureVlanCounterEntry=_Dot1qFutureVlanCounterEntry_Object((1,3,6,1,4,1,10876,101,1,65,1,16,1))
dot1qFutureVlanCounterEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:dot1qFutureVlanCounterEntry.setStatus(_A)
_Dot1qFutureVlanCounterRxUcast_Type=Counter32
_Dot1qFutureVlanCounterRxUcast_Object=MibTableColumn
dot1qFutureVlanCounterRxUcast=_Dot1qFutureVlanCounterRxUcast_Object((1,3,6,1,4,1,10876,101,1,65,1,16,1,1),_Dot1qFutureVlanCounterRxUcast_Type())
dot1qFutureVlanCounterRxUcast.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qFutureVlanCounterRxUcast.setStatus(_A)
_Dot1qFutureVlanCounterRxMcastBcast_Type=Counter32
_Dot1qFutureVlanCounterRxMcastBcast_Object=MibTableColumn
dot1qFutureVlanCounterRxMcastBcast=_Dot1qFutureVlanCounterRxMcastBcast_Object((1,3,6,1,4,1,10876,101,1,65,1,16,1,2),_Dot1qFutureVlanCounterRxMcastBcast_Type())
dot1qFutureVlanCounterRxMcastBcast.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qFutureVlanCounterRxMcastBcast.setStatus(_A)
_Dot1qFutureVlanCounterTxUnknUcast_Type=Counter32
_Dot1qFutureVlanCounterTxUnknUcast_Object=MibTableColumn
dot1qFutureVlanCounterTxUnknUcast=_Dot1qFutureVlanCounterTxUnknUcast_Object((1,3,6,1,4,1,10876,101,1,65,1,16,1,3),_Dot1qFutureVlanCounterTxUnknUcast_Type())
dot1qFutureVlanCounterTxUnknUcast.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qFutureVlanCounterTxUnknUcast.setStatus(_A)
_Dot1qFutureVlanCounterTxUcast_Type=Counter32
_Dot1qFutureVlanCounterTxUcast_Object=MibTableColumn
dot1qFutureVlanCounterTxUcast=_Dot1qFutureVlanCounterTxUcast_Object((1,3,6,1,4,1,10876,101,1,65,1,16,1,4),_Dot1qFutureVlanCounterTxUcast_Type())
dot1qFutureVlanCounterTxUcast.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qFutureVlanCounterTxUcast.setStatus(_A)
_Dot1qFutureVlanCounterTxBcast_Type=Counter32
_Dot1qFutureVlanCounterTxBcast_Object=MibTableColumn
dot1qFutureVlanCounterTxBcast=_Dot1qFutureVlanCounterTxBcast_Object((1,3,6,1,4,1,10876,101,1,65,1,16,1,5),_Dot1qFutureVlanCounterTxBcast_Type())
dot1qFutureVlanCounterTxBcast.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qFutureVlanCounterTxBcast.setStatus(_A)
class _Dot1qFutureVlanCounterStatus_Type(EnabledStatus):defaultValue=2
_Dot1qFutureVlanCounterStatus_Type.__name__=_G
_Dot1qFutureVlanCounterStatus_Object=MibTableColumn
dot1qFutureVlanCounterStatus=_Dot1qFutureVlanCounterStatus_Object((1,3,6,1,4,1,10876,101,1,65,1,16,1,6),_Dot1qFutureVlanCounterStatus_Type())
dot1qFutureVlanCounterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanCounterStatus.setStatus(_A)
_Dot1qFutureVlanUnicastMacControlTable_Object=MibTable
dot1qFutureVlanUnicastMacControlTable=_Dot1qFutureVlanUnicastMacControlTable_Object((1,3,6,1,4,1,10876,101,1,65,1,17))
if mibBuilder.loadTexts:dot1qFutureVlanUnicastMacControlTable.setStatus(_A)
_Dot1qFutureVlanUnicastMacControlEntry_Object=MibTableRow
dot1qFutureVlanUnicastMacControlEntry=_Dot1qFutureVlanUnicastMacControlEntry_Object((1,3,6,1,4,1,10876,101,1,65,1,17,1))
dot1qFutureVlanUnicastMacControlEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:dot1qFutureVlanUnicastMacControlEntry.setStatus(_A)
class _Dot1qFutureVlanUnicastMacLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Dot1qFutureVlanUnicastMacLimit_Type.__name__=_J
_Dot1qFutureVlanUnicastMacLimit_Object=MibTableColumn
dot1qFutureVlanUnicastMacLimit=_Dot1qFutureVlanUnicastMacLimit_Object((1,3,6,1,4,1,10876,101,1,65,1,17,1,1),_Dot1qFutureVlanUnicastMacLimit_Type())
dot1qFutureVlanUnicastMacLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanUnicastMacLimit.setStatus(_A)
class _Dot1qFutureVlanAdminMacLearningStatus_Type(MacLearningStatus):defaultValue=3
_Dot1qFutureVlanAdminMacLearningStatus_Type.__name__=_U
_Dot1qFutureVlanAdminMacLearningStatus_Object=MibTableColumn
dot1qFutureVlanAdminMacLearningStatus=_Dot1qFutureVlanAdminMacLearningStatus_Object((1,3,6,1,4,1,10876,101,1,65,1,17,1,2),_Dot1qFutureVlanAdminMacLearningStatus_Type())
dot1qFutureVlanAdminMacLearningStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanAdminMacLearningStatus.setStatus(_A)
_Dot1qFutureVlanOperMacLearningStatus_Type=EnabledStatus
_Dot1qFutureVlanOperMacLearningStatus_Object=MibTableColumn
dot1qFutureVlanOperMacLearningStatus=_Dot1qFutureVlanOperMacLearningStatus_Object((1,3,6,1,4,1,10876,101,1,65,1,17,1,3),_Dot1qFutureVlanOperMacLearningStatus_Type())
dot1qFutureVlanOperMacLearningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qFutureVlanOperMacLearningStatus.setStatus(_A)
class _Dot1qFutureVlanPortFdbFlush_Type(TruthValue):defaultValue=2
_Dot1qFutureVlanPortFdbFlush_Type.__name__=_H
_Dot1qFutureVlanPortFdbFlush_Object=MibTableColumn
dot1qFutureVlanPortFdbFlush=_Dot1qFutureVlanPortFdbFlush_Object((1,3,6,1,4,1,10876,101,1,65,1,17,1,4),_Dot1qFutureVlanPortFdbFlush_Type())
dot1qFutureVlanPortFdbFlush.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortFdbFlush.setStatus(_A)
class _Dot1qFutureGarpDebug_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048575))
_Dot1qFutureGarpDebug_Type.__name__=_F
_Dot1qFutureGarpDebug_Object=MibScalar
dot1qFutureGarpDebug=_Dot1qFutureGarpDebug_Object((1,3,6,1,4,1,10876,101,1,65,1,18),_Dot1qFutureGarpDebug_Type())
dot1qFutureGarpDebug.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureGarpDebug.setStatus(_A)
_Dot1qFutureVlanTpFdbTable_Object=MibTable
dot1qFutureVlanTpFdbTable=_Dot1qFutureVlanTpFdbTable_Object((1,3,6,1,4,1,10876,101,1,65,1,19))
if mibBuilder.loadTexts:dot1qFutureVlanTpFdbTable.setStatus(_A)
_Dot1qFutureVlanTpFdbEntry_Object=MibTableRow
dot1qFutureVlanTpFdbEntry=_Dot1qFutureVlanTpFdbEntry_Object((1,3,6,1,4,1,10876,101,1,65,1,19,1))
if mibBuilder.loadTexts:dot1qFutureVlanTpFdbEntry.setStatus(_A)
_Dot1qFutureVlanTpFdbPw_Type=Unsigned32
_Dot1qFutureVlanTpFdbPw_Object=MibTableColumn
dot1qFutureVlanTpFdbPw=_Dot1qFutureVlanTpFdbPw_Object((1,3,6,1,4,1,10876,101,1,65,1,19,1,1),_Dot1qFutureVlanTpFdbPw_Type())
dot1qFutureVlanTpFdbPw.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qFutureVlanTpFdbPw.setStatus(_A)
class _Dot1qTpOldFdbPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot1qTpOldFdbPort_Type.__name__=_F
_Dot1qTpOldFdbPort_Object=MibTableColumn
dot1qTpOldFdbPort=_Dot1qTpOldFdbPort_Object((1,3,6,1,4,1,10876,101,1,65,1,19,1,2),_Dot1qTpOldFdbPort_Type())
dot1qTpOldFdbPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qTpOldFdbPort.setStatus(_A)
_Dot1qFutureConnectionIdentifier_Type=MacAddress
_Dot1qFutureConnectionIdentifier_Object=MibTableColumn
dot1qFutureConnectionIdentifier=_Dot1qFutureConnectionIdentifier_Object((1,3,6,1,4,1,10876,101,1,65,1,19,1,3),_Dot1qFutureConnectionIdentifier_Type())
dot1qFutureConnectionIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qFutureConnectionIdentifier.setStatus(_A)
_Dot1qFutureVlanWildCardTable_Object=MibTable
dot1qFutureVlanWildCardTable=_Dot1qFutureVlanWildCardTable_Object((1,3,6,1,4,1,10876,101,1,65,1,20))
if mibBuilder.loadTexts:dot1qFutureVlanWildCardTable.setStatus(_A)
_Dot1qFutureVlanWildCardEntry_Object=MibTableRow
dot1qFutureVlanWildCardEntry=_Dot1qFutureVlanWildCardEntry_Object((1,3,6,1,4,1,10876,101,1,65,1,20,1))
dot1qFutureVlanWildCardEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:dot1qFutureVlanWildCardEntry.setStatus(_A)
_Dot1qFutureVlanWildCardMacAddress_Type=MacAddress
_Dot1qFutureVlanWildCardMacAddress_Object=MibTableColumn
dot1qFutureVlanWildCardMacAddress=_Dot1qFutureVlanWildCardMacAddress_Object((1,3,6,1,4,1,10876,101,1,65,1,20,1,1),_Dot1qFutureVlanWildCardMacAddress_Type())
dot1qFutureVlanWildCardMacAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:dot1qFutureVlanWildCardMacAddress.setStatus(_A)
_Dot1qFutureVlanWildCardEgressPorts_Type=PortList
_Dot1qFutureVlanWildCardEgressPorts_Object=MibTableColumn
dot1qFutureVlanWildCardEgressPorts=_Dot1qFutureVlanWildCardEgressPorts_Object((1,3,6,1,4,1,10876,101,1,65,1,20,1,2),_Dot1qFutureVlanWildCardEgressPorts_Type())
dot1qFutureVlanWildCardEgressPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanWildCardEgressPorts.setStatus(_A)
_Dot1qFutureVlanWildCardRowStatus_Type=RowStatus
_Dot1qFutureVlanWildCardRowStatus_Object=MibTableColumn
dot1qFutureVlanWildCardRowStatus=_Dot1qFutureVlanWildCardRowStatus_Object((1,3,6,1,4,1,10876,101,1,65,1,20,1,3),_Dot1qFutureVlanWildCardRowStatus_Type())
dot1qFutureVlanWildCardRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanWildCardRowStatus.setStatus(_A)
_Dot1qFutureStaticUnicastExtnTable_Object=MibTable
dot1qFutureStaticUnicastExtnTable=_Dot1qFutureStaticUnicastExtnTable_Object((1,3,6,1,4,1,10876,101,1,65,1,21))
if mibBuilder.loadTexts:dot1qFutureStaticUnicastExtnTable.setStatus(_A)
_Dot1qFutureStaticUnicastExtnEntry_Object=MibTableRow
dot1qFutureStaticUnicastExtnEntry=_Dot1qFutureStaticUnicastExtnEntry_Object((1,3,6,1,4,1,10876,101,1,65,1,21,1))
if mibBuilder.loadTexts:dot1qFutureStaticUnicastExtnEntry.setStatus(_A)
_Dot1qFutureStaticConnectionIdentifier_Type=MacAddress
_Dot1qFutureStaticConnectionIdentifier_Object=MibTableColumn
dot1qFutureStaticConnectionIdentifier=_Dot1qFutureStaticConnectionIdentifier_Object((1,3,6,1,4,1,10876,101,1,65,1,21,1,1),_Dot1qFutureStaticConnectionIdentifier_Type())
dot1qFutureStaticConnectionIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureStaticConnectionIdentifier.setStatus(_A)
class _Dot1qFutureUnicastMacLearningLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Dot1qFutureUnicastMacLearningLimit_Type.__name__=_J
_Dot1qFutureUnicastMacLearningLimit_Object=MibScalar
dot1qFutureUnicastMacLearningLimit=_Dot1qFutureUnicastMacLearningLimit_Object((1,3,6,1,4,1,10876,101,1,65,1,22),_Dot1qFutureUnicastMacLearningLimit_Type())
dot1qFutureUnicastMacLearningLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureUnicastMacLearningLimit.setStatus(_A)
class _Dot1qFutureVlanBaseBridgeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dot1dTransparentMode',1),('dot1qVlanMode',2)))
_Dot1qFutureVlanBaseBridgeMode_Type.__name__=_F
_Dot1qFutureVlanBaseBridgeMode_Object=MibScalar
dot1qFutureVlanBaseBridgeMode=_Dot1qFutureVlanBaseBridgeMode_Object((1,3,6,1,4,1,10876,101,1,65,1,23),_Dot1qFutureVlanBaseBridgeMode_Type())
dot1qFutureVlanBaseBridgeMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanBaseBridgeMode.setStatus(_A)
_Dot1qFutureVlanSubnetBasedOnAllPorts_Type=EnabledStatus
_Dot1qFutureVlanSubnetBasedOnAllPorts_Object=MibScalar
dot1qFutureVlanSubnetBasedOnAllPorts=_Dot1qFutureVlanSubnetBasedOnAllPorts_Object((1,3,6,1,4,1,10876,101,1,65,1,24),_Dot1qFutureVlanSubnetBasedOnAllPorts_Type())
dot1qFutureVlanSubnetBasedOnAllPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanSubnetBasedOnAllPorts.setStatus(_A)
_Dot1qFutureVlanPortSubnetMapTable_Object=MibTable
dot1qFutureVlanPortSubnetMapTable=_Dot1qFutureVlanPortSubnetMapTable_Object((1,3,6,1,4,1,10876,101,1,65,1,25))
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapTable.setStatus(_A)
_Dot1qFutureVlanPortSubnetMapEntry_Object=MibTableRow
dot1qFutureVlanPortSubnetMapEntry=_Dot1qFutureVlanPortSubnetMapEntry_Object((1,3,6,1,4,1,10876,101,1,65,1,25,1))
dot1qFutureVlanPortSubnetMapEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapEntry.setStatus(_A)
_Dot1qFutureVlanPortSubnetMapAddr_Type=IpAddress
_Dot1qFutureVlanPortSubnetMapAddr_Object=MibTableColumn
dot1qFutureVlanPortSubnetMapAddr=_Dot1qFutureVlanPortSubnetMapAddr_Object((1,3,6,1,4,1,10876,101,1,65,1,25,1,1),_Dot1qFutureVlanPortSubnetMapAddr_Type())
dot1qFutureVlanPortSubnetMapAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapAddr.setStatus(_A)
_Dot1qFutureVlanPortSubnetMapVid_Type=VlanId
_Dot1qFutureVlanPortSubnetMapVid_Object=MibTableColumn
dot1qFutureVlanPortSubnetMapVid=_Dot1qFutureVlanPortSubnetMapVid_Object((1,3,6,1,4,1,10876,101,1,65,1,25,1,2),_Dot1qFutureVlanPortSubnetMapVid_Type())
dot1qFutureVlanPortSubnetMapVid.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapVid.setStatus(_A)
_Dot1qFutureVlanPortSubnetMapRowStatus_Type=RowStatus
_Dot1qFutureVlanPortSubnetMapRowStatus_Object=MibTableColumn
dot1qFutureVlanPortSubnetMapRowStatus=_Dot1qFutureVlanPortSubnetMapRowStatus_Object((1,3,6,1,4,1,10876,101,1,65,1,25,1,4),_Dot1qFutureVlanPortSubnetMapRowStatus_Type())
dot1qFutureVlanPortSubnetMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapRowStatus.setStatus(_A)
class _Dot1qFutureVlanGlobalMacLearningStatus_Type(EnabledStatus):defaultValue=1
_Dot1qFutureVlanGlobalMacLearningStatus_Type.__name__=_G
_Dot1qFutureVlanGlobalMacLearningStatus_Object=MibScalar
dot1qFutureVlanGlobalMacLearningStatus=_Dot1qFutureVlanGlobalMacLearningStatus_Object((1,3,6,1,4,1,10876,101,1,65,1,26),_Dot1qFutureVlanGlobalMacLearningStatus_Type())
dot1qFutureVlanGlobalMacLearningStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanGlobalMacLearningStatus.setStatus(_A)
class _Dot1qFutureVlanApplyEnhancedFilteringCriteria_Type(TruthValue):defaultValue=1
_Dot1qFutureVlanApplyEnhancedFilteringCriteria_Type.__name__=_H
_Dot1qFutureVlanApplyEnhancedFilteringCriteria_Object=MibScalar
dot1qFutureVlanApplyEnhancedFilteringCriteria=_Dot1qFutureVlanApplyEnhancedFilteringCriteria_Object((1,3,6,1,4,1,10876,101,1,65,1,27),_Dot1qFutureVlanApplyEnhancedFilteringCriteria_Type())
dot1qFutureVlanApplyEnhancedFilteringCriteria.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanApplyEnhancedFilteringCriteria.setStatus(_A)
_Dot1qFutureVlanSwStatsEnabled_Type=TruthValue
_Dot1qFutureVlanSwStatsEnabled_Object=MibScalar
dot1qFutureVlanSwStatsEnabled=_Dot1qFutureVlanSwStatsEnabled_Object((1,3,6,1,4,1,10876,101,1,65,1,28),_Dot1qFutureVlanSwStatsEnabled_Type())
dot1qFutureVlanSwStatsEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanSwStatsEnabled.setStatus(_A)
_Dot1qFutureStVlanExtTable_Object=MibTable
dot1qFutureStVlanExtTable=_Dot1qFutureStVlanExtTable_Object((1,3,6,1,4,1,10876,101,1,65,1,29))
if mibBuilder.loadTexts:dot1qFutureStVlanExtTable.setStatus(_A)
_Dot1qFutureStVlanExtEntry_Object=MibTableRow
dot1qFutureStVlanExtEntry=_Dot1qFutureStVlanExtEntry_Object((1,3,6,1,4,1,10876,101,1,65,1,29,1))
if mibBuilder.loadTexts:dot1qFutureStVlanExtEntry.setStatus(_A)
class _Dot1qFutureStVlanPVlanType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),('primary',2),('isolated',3),('community',4)))
_Dot1qFutureStVlanPVlanType_Type.__name__=_F
_Dot1qFutureStVlanPVlanType_Object=MibTableColumn
dot1qFutureStVlanPVlanType=_Dot1qFutureStVlanPVlanType_Object((1,3,6,1,4,1,10876,101,1,65,1,29,1,1),_Dot1qFutureStVlanPVlanType_Type())
dot1qFutureStVlanPVlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureStVlanPVlanType.setStatus(_A)
class _Dot1qFutureStVlanPrimaryVid_Type(VlanIdOrNone):defaultValue=0
_Dot1qFutureStVlanPrimaryVid_Type.__name__=_O
_Dot1qFutureStVlanPrimaryVid_Object=MibTableColumn
dot1qFutureStVlanPrimaryVid=_Dot1qFutureStVlanPrimaryVid_Object((1,3,6,1,4,1,10876,101,1,65,1,29,1,2),_Dot1qFutureStVlanPrimaryVid_Type())
dot1qFutureStVlanPrimaryVid.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureStVlanPrimaryVid.setStatus(_A)
_Dot1qFutureVlanPortSubnetMapExtTable_Object=MibTable
dot1qFutureVlanPortSubnetMapExtTable=_Dot1qFutureVlanPortSubnetMapExtTable_Object((1,3,6,1,4,1,10876,101,1,65,1,30))
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapExtTable.setStatus(_A)
_Dot1qFutureVlanPortSubnetMapExtEntry_Object=MibTableRow
dot1qFutureVlanPortSubnetMapExtEntry=_Dot1qFutureVlanPortSubnetMapExtEntry_Object((1,3,6,1,4,1,10876,101,1,65,1,30,1))
dot1qFutureVlanPortSubnetMapExtEntry.setIndexNames((0,_D,_X),(0,_D,_Y))
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapExtEntry.setStatus(_A)
_Dot1qFutureVlanPortSubnetMapExtAddr_Type=IpAddress
_Dot1qFutureVlanPortSubnetMapExtAddr_Object=MibTableColumn
dot1qFutureVlanPortSubnetMapExtAddr=_Dot1qFutureVlanPortSubnetMapExtAddr_Object((1,3,6,1,4,1,10876,101,1,65,1,30,1,1),_Dot1qFutureVlanPortSubnetMapExtAddr_Type())
dot1qFutureVlanPortSubnetMapExtAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapExtAddr.setStatus(_A)
_Dot1qFutureVlanPortSubnetMapExtMask_Type=IpAddress
_Dot1qFutureVlanPortSubnetMapExtMask_Object=MibTableColumn
dot1qFutureVlanPortSubnetMapExtMask=_Dot1qFutureVlanPortSubnetMapExtMask_Object((1,3,6,1,4,1,10876,101,1,65,1,30,1,2),_Dot1qFutureVlanPortSubnetMapExtMask_Type())
dot1qFutureVlanPortSubnetMapExtMask.setMaxAccess(_I)
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapExtMask.setStatus(_A)
_Dot1qFutureVlanPortSubnetMapExtVid_Type=VlanId
_Dot1qFutureVlanPortSubnetMapExtVid_Object=MibTableColumn
dot1qFutureVlanPortSubnetMapExtVid=_Dot1qFutureVlanPortSubnetMapExtVid_Object((1,3,6,1,4,1,10876,101,1,65,1,30,1,3),_Dot1qFutureVlanPortSubnetMapExtVid_Type())
dot1qFutureVlanPortSubnetMapExtVid.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapExtVid.setStatus(_A)
_Dot1qFutureVlanPortSubnetMapExtRowStatus_Type=RowStatus
_Dot1qFutureVlanPortSubnetMapExtRowStatus_Object=MibTableColumn
dot1qFutureVlanPortSubnetMapExtRowStatus=_Dot1qFutureVlanPortSubnetMapExtRowStatus_Object((1,3,6,1,4,1,10876,101,1,65,1,30,1,5),_Dot1qFutureVlanPortSubnetMapExtRowStatus_Type())
dot1qFutureVlanPortSubnetMapExtRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapExtRowStatus.setStatus(_A)
_Dot1qFutureVlanGlobalsFdbFlush_Type=TruthValue
_Dot1qFutureVlanGlobalsFdbFlush_Object=MibScalar
dot1qFutureVlanGlobalsFdbFlush=_Dot1qFutureVlanGlobalsFdbFlush_Object((1,3,6,1,4,1,10876,101,1,65,1,31),_Dot1qFutureVlanGlobalsFdbFlush_Type())
dot1qFutureVlanGlobalsFdbFlush.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanGlobalsFdbFlush.setStatus(_A)
_Dot1qFutureVlanTunnelConfig_ObjectIdentity=ObjectIdentity
dot1qFutureVlanTunnelConfig=_Dot1qFutureVlanTunnelConfig_ObjectIdentity((1,3,6,1,4,1,10876,101,1,65,2))
class _Dot1qFutureVlanBridgeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('customerBridge',1),('providerBridge',2),('providerCoreBridge',3),('providerEdgeBridge',4)))
_Dot1qFutureVlanBridgeMode_Type.__name__=_F
_Dot1qFutureVlanBridgeMode_Object=MibScalar
dot1qFutureVlanBridgeMode=_Dot1qFutureVlanBridgeMode_Object((1,3,6,1,4,1,10876,101,1,65,2,1),_Dot1qFutureVlanBridgeMode_Type())
dot1qFutureVlanBridgeMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanBridgeMode.setStatus(_E)
class _Dot1qFutureVlanTunnelBpduPri_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot1qFutureVlanTunnelBpduPri_Type.__name__=_F
_Dot1qFutureVlanTunnelBpduPri_Object=MibScalar
dot1qFutureVlanTunnelBpduPri=_Dot1qFutureVlanTunnelBpduPri_Object((1,3,6,1,4,1,10876,101,1,65,2,2),_Dot1qFutureVlanTunnelBpduPri_Type())
dot1qFutureVlanTunnelBpduPri.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanTunnelBpduPri.setStatus(_E)
_Dot1qFutureVlanTunnelTable_Object=MibTable
dot1qFutureVlanTunnelTable=_Dot1qFutureVlanTunnelTable_Object((1,3,6,1,4,1,10876,101,1,65,2,3))
if mibBuilder.loadTexts:dot1qFutureVlanTunnelTable.setStatus(_E)
_Dot1qFutureVlanTunnelEntry_Object=MibTableRow
dot1qFutureVlanTunnelEntry=_Dot1qFutureVlanTunnelEntry_Object((1,3,6,1,4,1,10876,101,1,65,2,3,1))
dot1qFutureVlanTunnelEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:dot1qFutureVlanTunnelEntry.setStatus(_E)
class _Dot1qFutureVlanTunnelStatus_Type(EnabledStatus):defaultValue=2
_Dot1qFutureVlanTunnelStatus_Type.__name__=_G
_Dot1qFutureVlanTunnelStatus_Object=MibTableColumn
dot1qFutureVlanTunnelStatus=_Dot1qFutureVlanTunnelStatus_Object((1,3,6,1,4,1,10876,101,1,65,2,3,1,1),_Dot1qFutureVlanTunnelStatus_Type())
dot1qFutureVlanTunnelStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanTunnelStatus.setStatus(_E)
_Dot1qFutureVlanTunnelProtocolTable_Object=MibTable
dot1qFutureVlanTunnelProtocolTable=_Dot1qFutureVlanTunnelProtocolTable_Object((1,3,6,1,4,1,10876,101,1,65,2,4))
if mibBuilder.loadTexts:dot1qFutureVlanTunnelProtocolTable.setStatus(_E)
_Dot1qFutureVlanTunnelProtocolEntry_Object=MibTableRow
dot1qFutureVlanTunnelProtocolEntry=_Dot1qFutureVlanTunnelProtocolEntry_Object((1,3,6,1,4,1,10876,101,1,65,2,4,1))
dot1qFutureVlanTunnelProtocolEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:dot1qFutureVlanTunnelProtocolEntry.setStatus(_E)
class _Dot1qFutureVlanTunnelStpPDUs_Type(EnabledStatus):defaultValue=2
_Dot1qFutureVlanTunnelStpPDUs_Type.__name__=_G
_Dot1qFutureVlanTunnelStpPDUs_Object=MibTableColumn
dot1qFutureVlanTunnelStpPDUs=_Dot1qFutureVlanTunnelStpPDUs_Object((1,3,6,1,4,1,10876,101,1,65,2,4,1,1),_Dot1qFutureVlanTunnelStpPDUs_Type())
dot1qFutureVlanTunnelStpPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanTunnelStpPDUs.setStatus(_E)
_Dot1qFutureVlanTunnelStpPDUsRecvd_Type=Counter32
_Dot1qFutureVlanTunnelStpPDUsRecvd_Object=MibTableColumn
dot1qFutureVlanTunnelStpPDUsRecvd=_Dot1qFutureVlanTunnelStpPDUsRecvd_Object((1,3,6,1,4,1,10876,101,1,65,2,4,1,2),_Dot1qFutureVlanTunnelStpPDUsRecvd_Type())
dot1qFutureVlanTunnelStpPDUsRecvd.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qFutureVlanTunnelStpPDUsRecvd.setStatus(_E)
_Dot1qFutureVlanTunnelStpPDUsSent_Type=Counter32
_Dot1qFutureVlanTunnelStpPDUsSent_Object=MibTableColumn
dot1qFutureVlanTunnelStpPDUsSent=_Dot1qFutureVlanTunnelStpPDUsSent_Object((1,3,6,1,4,1,10876,101,1,65,2,4,1,3),_Dot1qFutureVlanTunnelStpPDUsSent_Type())
dot1qFutureVlanTunnelStpPDUsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qFutureVlanTunnelStpPDUsSent.setStatus(_E)
class _Dot1qFutureVlanTunnelGvrpPDUs_Type(EnabledStatus):defaultValue=1
_Dot1qFutureVlanTunnelGvrpPDUs_Type.__name__=_G
_Dot1qFutureVlanTunnelGvrpPDUs_Object=MibTableColumn
dot1qFutureVlanTunnelGvrpPDUs=_Dot1qFutureVlanTunnelGvrpPDUs_Object((1,3,6,1,4,1,10876,101,1,65,2,4,1,4),_Dot1qFutureVlanTunnelGvrpPDUs_Type())
dot1qFutureVlanTunnelGvrpPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanTunnelGvrpPDUs.setStatus(_E)
_Dot1qFutureVlanTunnelGvrpPDUsRecvd_Type=Counter32
_Dot1qFutureVlanTunnelGvrpPDUsRecvd_Object=MibTableColumn
dot1qFutureVlanTunnelGvrpPDUsRecvd=_Dot1qFutureVlanTunnelGvrpPDUsRecvd_Object((1,3,6,1,4,1,10876,101,1,65,2,4,1,5),_Dot1qFutureVlanTunnelGvrpPDUsRecvd_Type())
dot1qFutureVlanTunnelGvrpPDUsRecvd.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qFutureVlanTunnelGvrpPDUsRecvd.setStatus(_E)
_Dot1qFutureVlanTunnelGvrpPDUsSent_Type=Counter32
_Dot1qFutureVlanTunnelGvrpPDUsSent_Object=MibTableColumn
dot1qFutureVlanTunnelGvrpPDUsSent=_Dot1qFutureVlanTunnelGvrpPDUsSent_Object((1,3,6,1,4,1,10876,101,1,65,2,4,1,6),_Dot1qFutureVlanTunnelGvrpPDUsSent_Type())
dot1qFutureVlanTunnelGvrpPDUsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qFutureVlanTunnelGvrpPDUsSent.setStatus(_E)
class _Dot1qFutureVlanTunnelIgmpPkts_Type(EnabledStatus):defaultValue=1
_Dot1qFutureVlanTunnelIgmpPkts_Type.__name__=_G
_Dot1qFutureVlanTunnelIgmpPkts_Object=MibTableColumn
dot1qFutureVlanTunnelIgmpPkts=_Dot1qFutureVlanTunnelIgmpPkts_Object((1,3,6,1,4,1,10876,101,1,65,2,4,1,7),_Dot1qFutureVlanTunnelIgmpPkts_Type())
dot1qFutureVlanTunnelIgmpPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanTunnelIgmpPkts.setStatus(_E)
_Dot1qFutureVlanTunnelIgmpPktsRecvd_Type=Counter32
_Dot1qFutureVlanTunnelIgmpPktsRecvd_Object=MibTableColumn
dot1qFutureVlanTunnelIgmpPktsRecvd=_Dot1qFutureVlanTunnelIgmpPktsRecvd_Object((1,3,6,1,4,1,10876,101,1,65,2,4,1,8),_Dot1qFutureVlanTunnelIgmpPktsRecvd_Type())
dot1qFutureVlanTunnelIgmpPktsRecvd.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qFutureVlanTunnelIgmpPktsRecvd.setStatus(_E)
_Dot1qFutureVlanTunnelIgmpPktsSent_Type=Counter32
_Dot1qFutureVlanTunnelIgmpPktsSent_Object=MibTableColumn
dot1qFutureVlanTunnelIgmpPktsSent=_Dot1qFutureVlanTunnelIgmpPktsSent_Object((1,3,6,1,4,1,10876,101,1,65,2,4,1,9),_Dot1qFutureVlanTunnelIgmpPktsSent_Type())
dot1qFutureVlanTunnelIgmpPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1qFutureVlanTunnelIgmpPktsSent.setStatus(_E)
_Dot1qFutureVlanTraps_ObjectIdentity=ObjectIdentity
dot1qFutureVlanTraps=_Dot1qFutureVlanTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,65,3))
_Dot1qVlanTraps_ObjectIdentity=ObjectIdentity
dot1qVlanTraps=_Dot1qVlanTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,65,3,0))
dot1qTpFdbEntry.registerAugmentions((_D,_Z))
dot1qFutureVlanTpFdbEntry.setIndexNames(*dot1qTpFdbEntry.getIndexNames())
dot1qStaticUnicastEntry.registerAugmentions((_D,_a))
dot1qFutureStaticUnicastExtnEntry.setIndexNames(*dot1qStaticUnicastEntry.getIndexNames())
dot1qVlanStaticEntry.registerAugmentions((_D,_b))
dot1qFutureStVlanExtEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())
dot1qFutureMacThresholdTrap=NotificationType((1,3,6,1,4,1,10876,101,1,65,3,0,1))
dot1qFutureMacThresholdTrap.setObjects(*((_D,_K),(_D,_c)))
if mibBuilder.loadTexts:dot1qFutureMacThresholdTrap.setStatus(_A)
dot1qFutureSrcRelearnTrap=NotificationType((1,3,6,1,4,1,10876,101,1,65,3,0,2))
dot1qFutureSrcRelearnTrap.setObjects(*((_D,_d),(_N,_P),(_D,_e)))
if mibBuilder.loadTexts:dot1qFutureSrcRelearnTrap.setStatus(_A)
dot1qFutureSwitchMacLimitTrap=NotificationType((1,3,6,1,4,1,10876,101,1,65,3,0,3))
dot1qFutureSwitchMacLimitTrap.setObjects((_D,_f))
if mibBuilder.loadTexts:dot1qFutureSwitchMacLimitTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'VlanId':VlanId,_G:EnabledStatus,_U:MacLearningStatus,'futureVlanMIB':futureVlanMIB,'dot1qFutureVlan':dot1qFutureVlan,'dot1qFutureVlanStatus':dot1qFutureVlanStatus,'dot1qFutureVlanMacBasedOnAllPorts':dot1qFutureVlanMacBasedOnAllPorts,'dot1qFutureVlanPortProtoBasedOnAllPorts':dot1qFutureVlanPortProtoBasedOnAllPorts,'dot1qFutureVlanShutdownStatus':dot1qFutureVlanShutdownStatus,'dot1qFutureGarpShutdownStatus':dot1qFutureGarpShutdownStatus,'dot1qFutureVlanDebug':dot1qFutureVlanDebug,'dot1qFutureVlanLearningMode':dot1qFutureVlanLearningMode,'dot1qFutureVlanHybridTypeDefault':dot1qFutureVlanHybridTypeDefault,'dot1qFutureVlanPortTable':dot1qFutureVlanPortTable,'dot1qFutureVlanPortEntry':dot1qFutureVlanPortEntry,_L:dot1qFutureVlanPort,'dot1qFutureVlanPortType':dot1qFutureVlanPortType,'dot1qFutureVlanPortPortProtoBasedClassification':dot1qFutureVlanPortPortProtoBasedClassification,'dot1qFutureVlanFilteringUtilityCriteria':dot1qFutureVlanFilteringUtilityCriteria,'dot1qFutureVlanPortProtected':dot1qFutureVlanPortProtected,'dot1qFutureVlanPortUnicastMacLearning':dot1qFutureVlanPortUnicastMacLearning,'dot1qFutureVlanPortAllowedVlanList':dot1qFutureVlanPortAllowedVlanList,'dot1qFutureVlanPortMacMapTable':dot1qFutureVlanPortMacMapTable,'dot1qFutureVlanPortMacMapEntry':dot1qFutureVlanPortMacMapEntry,_T:dot1qFutureVlanPortMacMapAddr,'dot1qFutureVlanPortMacMapVid':dot1qFutureVlanPortMacMapVid,'dot1qFutureVlanPortMacMapRowStatus':dot1qFutureVlanPortMacMapRowStatus,'dot1qFutureVlanFidMapTable':dot1qFutureVlanFidMapTable,'dot1qFutureVlanFidMapEntry':dot1qFutureVlanFidMapEntry,_K:dot1qFutureVlanIndex,_d:dot1qFutureVlanFid,'dot1qFutureVlanOperStatus':dot1qFutureVlanOperStatus,'dot1qFutureGvrpOperStatus':dot1qFutureGvrpOperStatus,'dot1qFutureGmrpOperStatus':dot1qFutureGmrpOperStatus,'dot1qFutureVlanCounterTable':dot1qFutureVlanCounterTable,'dot1qFutureVlanCounterEntry':dot1qFutureVlanCounterEntry,'dot1qFutureVlanCounterRxUcast':dot1qFutureVlanCounterRxUcast,'dot1qFutureVlanCounterRxMcastBcast':dot1qFutureVlanCounterRxMcastBcast,'dot1qFutureVlanCounterTxUnknUcast':dot1qFutureVlanCounterTxUnknUcast,'dot1qFutureVlanCounterTxUcast':dot1qFutureVlanCounterTxUcast,'dot1qFutureVlanCounterTxBcast':dot1qFutureVlanCounterTxBcast,'dot1qFutureVlanCounterStatus':dot1qFutureVlanCounterStatus,'dot1qFutureVlanUnicastMacControlTable':dot1qFutureVlanUnicastMacControlTable,'dot1qFutureVlanUnicastMacControlEntry':dot1qFutureVlanUnicastMacControlEntry,_c:dot1qFutureVlanUnicastMacLimit,'dot1qFutureVlanAdminMacLearningStatus':dot1qFutureVlanAdminMacLearningStatus,'dot1qFutureVlanOperMacLearningStatus':dot1qFutureVlanOperMacLearningStatus,'dot1qFutureVlanPortFdbFlush':dot1qFutureVlanPortFdbFlush,'dot1qFutureGarpDebug':dot1qFutureGarpDebug,'dot1qFutureVlanTpFdbTable':dot1qFutureVlanTpFdbTable,_Z:dot1qFutureVlanTpFdbEntry,'dot1qFutureVlanTpFdbPw':dot1qFutureVlanTpFdbPw,_e:dot1qTpOldFdbPort,'dot1qFutureConnectionIdentifier':dot1qFutureConnectionIdentifier,'dot1qFutureVlanWildCardTable':dot1qFutureVlanWildCardTable,'dot1qFutureVlanWildCardEntry':dot1qFutureVlanWildCardEntry,_V:dot1qFutureVlanWildCardMacAddress,'dot1qFutureVlanWildCardEgressPorts':dot1qFutureVlanWildCardEgressPorts,'dot1qFutureVlanWildCardRowStatus':dot1qFutureVlanWildCardRowStatus,'dot1qFutureStaticUnicastExtnTable':dot1qFutureStaticUnicastExtnTable,_a:dot1qFutureStaticUnicastExtnEntry,'dot1qFutureStaticConnectionIdentifier':dot1qFutureStaticConnectionIdentifier,_f:dot1qFutureUnicastMacLearningLimit,'dot1qFutureVlanBaseBridgeMode':dot1qFutureVlanBaseBridgeMode,'dot1qFutureVlanSubnetBasedOnAllPorts':dot1qFutureVlanSubnetBasedOnAllPorts,'dot1qFutureVlanPortSubnetMapTable':dot1qFutureVlanPortSubnetMapTable,'dot1qFutureVlanPortSubnetMapEntry':dot1qFutureVlanPortSubnetMapEntry,_W:dot1qFutureVlanPortSubnetMapAddr,'dot1qFutureVlanPortSubnetMapVid':dot1qFutureVlanPortSubnetMapVid,'dot1qFutureVlanPortSubnetMapRowStatus':dot1qFutureVlanPortSubnetMapRowStatus,'dot1qFutureVlanGlobalMacLearningStatus':dot1qFutureVlanGlobalMacLearningStatus,'dot1qFutureVlanApplyEnhancedFilteringCriteria':dot1qFutureVlanApplyEnhancedFilteringCriteria,'dot1qFutureVlanSwStatsEnabled':dot1qFutureVlanSwStatsEnabled,'dot1qFutureStVlanExtTable':dot1qFutureStVlanExtTable,_b:dot1qFutureStVlanExtEntry,'dot1qFutureStVlanPVlanType':dot1qFutureStVlanPVlanType,'dot1qFutureStVlanPrimaryVid':dot1qFutureStVlanPrimaryVid,'dot1qFutureVlanPortSubnetMapExtTable':dot1qFutureVlanPortSubnetMapExtTable,'dot1qFutureVlanPortSubnetMapExtEntry':dot1qFutureVlanPortSubnetMapExtEntry,_X:dot1qFutureVlanPortSubnetMapExtAddr,_Y:dot1qFutureVlanPortSubnetMapExtMask,'dot1qFutureVlanPortSubnetMapExtVid':dot1qFutureVlanPortSubnetMapExtVid,'dot1qFutureVlanPortSubnetMapExtRowStatus':dot1qFutureVlanPortSubnetMapExtRowStatus,'dot1qFutureVlanGlobalsFdbFlush':dot1qFutureVlanGlobalsFdbFlush,'dot1qFutureVlanTunnelConfig':dot1qFutureVlanTunnelConfig,'dot1qFutureVlanBridgeMode':dot1qFutureVlanBridgeMode,'dot1qFutureVlanTunnelBpduPri':dot1qFutureVlanTunnelBpduPri,'dot1qFutureVlanTunnelTable':dot1qFutureVlanTunnelTable,'dot1qFutureVlanTunnelEntry':dot1qFutureVlanTunnelEntry,'dot1qFutureVlanTunnelStatus':dot1qFutureVlanTunnelStatus,'dot1qFutureVlanTunnelProtocolTable':dot1qFutureVlanTunnelProtocolTable,'dot1qFutureVlanTunnelProtocolEntry':dot1qFutureVlanTunnelProtocolEntry,'dot1qFutureVlanTunnelStpPDUs':dot1qFutureVlanTunnelStpPDUs,'dot1qFutureVlanTunnelStpPDUsRecvd':dot1qFutureVlanTunnelStpPDUsRecvd,'dot1qFutureVlanTunnelStpPDUsSent':dot1qFutureVlanTunnelStpPDUsSent,'dot1qFutureVlanTunnelGvrpPDUs':dot1qFutureVlanTunnelGvrpPDUs,'dot1qFutureVlanTunnelGvrpPDUsRecvd':dot1qFutureVlanTunnelGvrpPDUsRecvd,'dot1qFutureVlanTunnelGvrpPDUsSent':dot1qFutureVlanTunnelGvrpPDUsSent,'dot1qFutureVlanTunnelIgmpPkts':dot1qFutureVlanTunnelIgmpPkts,'dot1qFutureVlanTunnelIgmpPktsRecvd':dot1qFutureVlanTunnelIgmpPktsRecvd,'dot1qFutureVlanTunnelIgmpPktsSent':dot1qFutureVlanTunnelIgmpPktsSent,'dot1qFutureVlanTraps':dot1qFutureVlanTraps,'dot1qVlanTraps':dot1qVlanTraps,'dot1qFutureMacThresholdTrap':dot1qFutureMacThresholdTrap,'dot1qFutureSrcRelearnTrap':dot1qFutureSrcRelearnTrap,'dot1qFutureSwitchMacLimitTrap':dot1qFutureSwitchMacLimitTrap})