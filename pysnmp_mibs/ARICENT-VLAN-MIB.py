_g='dot1qFutureUnicastMacLearningLimit'
_f='dot1qTpOldFdbPort'
_e='dot1qFutureVlanFid'
_d='dot1qFutureVlanUnicastMacLimit'
_c='dot1qFutureStVlanExtEntry'
_b='dot1qFutureStaticUnicastExtnEntry'
_a='dot1qFutureVlanTpFdbEntry'
_Z='dot1qFutureVlanPortSubnetMapExtMask'
_Y='dot1qFutureVlanPortSubnetMapExtAddr'
_X='dot1qFutureVlanPortSubnetMapAddr'
_W='dot1qFutureVlanWildCardMacAddress'
_V='MacLearningStatus'
_U='dot1qFutureVlanPortMacMapAddr'
_T='default'
_S='disabled'
_R='enabled'
_Q='dot1qTpFdbPort'
_P='VlanIdOrNone'
_O='Q-BRIDGE-MIB'
_N='suppress'
_M='allow'
_L='Unsigned32'
_K='dot1qFutureVlanIndex'
_J='not-accessible'
_I='dot1qFutureVlanPort'
_H='TruthValue'
_G='EnabledStatus'
_F='deprecated'
_E='ARICENT-VLAN-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,VlanIdOrNone,dot1qStaticUnicastEntry,dot1qTpFdbEntry,dot1qTpFdbPort,dot1qVlanStaticEntry=mibBuilder.importSymbols(_O,'PortList',_P,'dot1qStaticUnicastEntry','dot1qTpFdbEntry',_Q,'dot1qVlanStaticEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_H)
futureVlanMIB=ModuleIdentity((1,3,6,1,4,1,2076,65))
if mibBuilder.loadTexts:futureVlanMIB.setRevisions(('2012-09-05 00:00',))
class VlanId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
class MacLearningStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,3)))
_Dot1qFutureVlan_ObjectIdentity=ObjectIdentity
dot1qFutureVlan=_Dot1qFutureVlan_ObjectIdentity((1,3,6,1,4,1,2076,65,1))
_Dot1qFutureVlanStatus_Type=EnabledStatus
_Dot1qFutureVlanStatus_Object=MibScalar
dot1qFutureVlanStatus=_Dot1qFutureVlanStatus_Object((1,3,6,1,4,1,2076,65,1,1),_Dot1qFutureVlanStatus_Type())
dot1qFutureVlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanStatus.setStatus(_A)
_Dot1qFutureVlanMacBasedOnAllPorts_Type=EnabledStatus
_Dot1qFutureVlanMacBasedOnAllPorts_Object=MibScalar
dot1qFutureVlanMacBasedOnAllPorts=_Dot1qFutureVlanMacBasedOnAllPorts_Object((1,3,6,1,4,1,2076,65,1,2),_Dot1qFutureVlanMacBasedOnAllPorts_Type())
dot1qFutureVlanMacBasedOnAllPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanMacBasedOnAllPorts.setStatus(_A)
_Dot1qFutureVlanPortProtoBasedOnAllPorts_Type=EnabledStatus
_Dot1qFutureVlanPortProtoBasedOnAllPorts_Object=MibScalar
dot1qFutureVlanPortProtoBasedOnAllPorts=_Dot1qFutureVlanPortProtoBasedOnAllPorts_Object((1,3,6,1,4,1,2076,65,1,3),_Dot1qFutureVlanPortProtoBasedOnAllPorts_Type())
dot1qFutureVlanPortProtoBasedOnAllPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortProtoBasedOnAllPorts.setStatus(_A)
class _Dot1qFutureVlanShutdownStatus_Type(TruthValue):defaultValue=2
_Dot1qFutureVlanShutdownStatus_Type.__name__=_H
_Dot1qFutureVlanShutdownStatus_Object=MibScalar
dot1qFutureVlanShutdownStatus=_Dot1qFutureVlanShutdownStatus_Object((1,3,6,1,4,1,2076,65,1,5),_Dot1qFutureVlanShutdownStatus_Type())
dot1qFutureVlanShutdownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanShutdownStatus.setStatus(_F)
class _Dot1qFutureGarpShutdownStatus_Type(TruthValue):defaultValue=2
_Dot1qFutureGarpShutdownStatus_Type.__name__=_H
_Dot1qFutureGarpShutdownStatus_Object=MibScalar
dot1qFutureGarpShutdownStatus=_Dot1qFutureGarpShutdownStatus_Object((1,3,6,1,4,1,2076,65,1,6),_Dot1qFutureGarpShutdownStatus_Type())
dot1qFutureGarpShutdownStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureGarpShutdownStatus.setStatus(_A)
class _Dot1qFutureVlanDebug_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,524287))
_Dot1qFutureVlanDebug_Type.__name__=_C
_Dot1qFutureVlanDebug_Object=MibScalar
dot1qFutureVlanDebug=_Dot1qFutureVlanDebug_Object((1,3,6,1,4,1,2076,65,1,7),_Dot1qFutureVlanDebug_Type())
dot1qFutureVlanDebug.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanDebug.setStatus(_A)
class _Dot1qFutureVlanLearningMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ivl',1),('svl',2),('hybrid',3)))
_Dot1qFutureVlanLearningMode_Type.__name__=_C
_Dot1qFutureVlanLearningMode_Object=MibScalar
dot1qFutureVlanLearningMode=_Dot1qFutureVlanLearningMode_Object((1,3,6,1,4,1,2076,65,1,8),_Dot1qFutureVlanLearningMode_Type())
dot1qFutureVlanLearningMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanLearningMode.setStatus(_A)
class _Dot1qFutureVlanHybridTypeDefault_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ivl',1),('svl',2)))
_Dot1qFutureVlanHybridTypeDefault_Type.__name__=_C
_Dot1qFutureVlanHybridTypeDefault_Object=MibScalar
dot1qFutureVlanHybridTypeDefault=_Dot1qFutureVlanHybridTypeDefault_Object((1,3,6,1,4,1,2076,65,1,9),_Dot1qFutureVlanHybridTypeDefault_Type())
dot1qFutureVlanHybridTypeDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanHybridTypeDefault.setStatus(_A)
_Dot1qFutureVlanPortTable_Object=MibTable
dot1qFutureVlanPortTable=_Dot1qFutureVlanPortTable_Object((1,3,6,1,4,1,2076,65,1,10))
if mibBuilder.loadTexts:dot1qFutureVlanPortTable.setStatus(_A)
_Dot1qFutureVlanPortEntry_Object=MibTableRow
dot1qFutureVlanPortEntry=_Dot1qFutureVlanPortEntry_Object((1,3,6,1,4,1,2076,65,1,10,1))
dot1qFutureVlanPortEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:dot1qFutureVlanPortEntry.setStatus(_A)
class _Dot1qFutureVlanPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1qFutureVlanPort_Type.__name__=_C
_Dot1qFutureVlanPort_Object=MibTableColumn
dot1qFutureVlanPort=_Dot1qFutureVlanPort_Object((1,3,6,1,4,1,2076,65,1,10,1,1),_Dot1qFutureVlanPort_Type())
dot1qFutureVlanPort.setMaxAccess(_J)
if mibBuilder.loadTexts:dot1qFutureVlanPort.setStatus(_A)
class _Dot1qFutureVlanPortType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('accessPort',1),('trunkPort',2),('hybridPort',3),('hostPort',4),('promiscuousPort',5)))
_Dot1qFutureVlanPortType_Type.__name__=_C
_Dot1qFutureVlanPortType_Object=MibTableColumn
dot1qFutureVlanPortType=_Dot1qFutureVlanPortType_Object((1,3,6,1,4,1,2076,65,1,10,1,2),_Dot1qFutureVlanPortType_Type())
dot1qFutureVlanPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortType.setStatus(_A)
_Dot1qFutureVlanPortMacBasedClassification_Type=EnabledStatus
_Dot1qFutureVlanPortMacBasedClassification_Object=MibTableColumn
dot1qFutureVlanPortMacBasedClassification=_Dot1qFutureVlanPortMacBasedClassification_Object((1,3,6,1,4,1,2076,65,1,10,1,3),_Dot1qFutureVlanPortMacBasedClassification_Type())
dot1qFutureVlanPortMacBasedClassification.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortMacBasedClassification.setStatus(_A)
_Dot1qFutureVlanPortPortProtoBasedClassification_Type=EnabledStatus
_Dot1qFutureVlanPortPortProtoBasedClassification_Object=MibTableColumn
dot1qFutureVlanPortPortProtoBasedClassification=_Dot1qFutureVlanPortPortProtoBasedClassification_Object((1,3,6,1,4,1,2076,65,1,10,1,4),_Dot1qFutureVlanPortPortProtoBasedClassification_Type())
dot1qFutureVlanPortPortProtoBasedClassification.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortPortProtoBasedClassification.setStatus(_A)
class _Dot1qFutureVlanFilteringUtilityCriteria_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),('enhanced',2)))
_Dot1qFutureVlanFilteringUtilityCriteria_Type.__name__=_C
_Dot1qFutureVlanFilteringUtilityCriteria_Object=MibTableColumn
dot1qFutureVlanFilteringUtilityCriteria=_Dot1qFutureVlanFilteringUtilityCriteria_Object((1,3,6,1,4,1,2076,65,1,10,1,5),_Dot1qFutureVlanFilteringUtilityCriteria_Type())
dot1qFutureVlanFilteringUtilityCriteria.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanFilteringUtilityCriteria.setStatus(_A)
class _Dot1qFutureVlanPortProtected_Type(TruthValue):defaultValue=2
_Dot1qFutureVlanPortProtected_Type.__name__=_H
_Dot1qFutureVlanPortProtected_Object=MibTableColumn
dot1qFutureVlanPortProtected=_Dot1qFutureVlanPortProtected_Object((1,3,6,1,4,1,2076,65,1,10,1,6),_Dot1qFutureVlanPortProtected_Type())
dot1qFutureVlanPortProtected.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortProtected.setStatus(_A)
_Dot1qFutureVlanPortSubnetBasedClassification_Type=EnabledStatus
_Dot1qFutureVlanPortSubnetBasedClassification_Object=MibTableColumn
dot1qFutureVlanPortSubnetBasedClassification=_Dot1qFutureVlanPortSubnetBasedClassification_Object((1,3,6,1,4,1,2076,65,1,10,1,7),_Dot1qFutureVlanPortSubnetBasedClassification_Type())
dot1qFutureVlanPortSubnetBasedClassification.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetBasedClassification.setStatus(_A)
class _Dot1qFutureVlanPortUnicastMacLearning_Type(EnabledStatus):defaultValue=1
_Dot1qFutureVlanPortUnicastMacLearning_Type.__name__=_G
_Dot1qFutureVlanPortUnicastMacLearning_Object=MibTableColumn
dot1qFutureVlanPortUnicastMacLearning=_Dot1qFutureVlanPortUnicastMacLearning_Object((1,3,6,1,4,1,2076,65,1,10,1,8),_Dot1qFutureVlanPortUnicastMacLearning_Type())
dot1qFutureVlanPortUnicastMacLearning.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortUnicastMacLearning.setStatus(_A)
class _Dot1qFutureVlanPortIngressEtherType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1qFutureVlanPortIngressEtherType_Type.__name__=_C
_Dot1qFutureVlanPortIngressEtherType_Object=MibTableColumn
dot1qFutureVlanPortIngressEtherType=_Dot1qFutureVlanPortIngressEtherType_Object((1,3,6,1,4,1,2076,65,1,10,1,9),_Dot1qFutureVlanPortIngressEtherType_Type())
dot1qFutureVlanPortIngressEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortIngressEtherType.setStatus(_A)
class _Dot1qFutureVlanPortEgressEtherType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1qFutureVlanPortEgressEtherType_Type.__name__=_C
_Dot1qFutureVlanPortEgressEtherType_Object=MibTableColumn
dot1qFutureVlanPortEgressEtherType=_Dot1qFutureVlanPortEgressEtherType_Object((1,3,6,1,4,1,2076,65,1,10,1,10),_Dot1qFutureVlanPortEgressEtherType_Type())
dot1qFutureVlanPortEgressEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortEgressEtherType.setStatus(_A)
class _Dot1qFutureVlanPortEgressTPIDType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('portbased',1),('vlanbased',2)))
_Dot1qFutureVlanPortEgressTPIDType_Type.__name__=_C
_Dot1qFutureVlanPortEgressTPIDType_Object=MibTableColumn
dot1qFutureVlanPortEgressTPIDType=_Dot1qFutureVlanPortEgressTPIDType_Object((1,3,6,1,4,1,2076,65,1,10,1,11),_Dot1qFutureVlanPortEgressTPIDType_Type())
dot1qFutureVlanPortEgressTPIDType.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortEgressTPIDType.setStatus(_A)
class _Dot1qFutureVlanPortAllowableTPID1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot1qFutureVlanPortAllowableTPID1_Type.__name__=_C
_Dot1qFutureVlanPortAllowableTPID1_Object=MibTableColumn
dot1qFutureVlanPortAllowableTPID1=_Dot1qFutureVlanPortAllowableTPID1_Object((1,3,6,1,4,1,2076,65,1,10,1,12),_Dot1qFutureVlanPortAllowableTPID1_Type())
dot1qFutureVlanPortAllowableTPID1.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortAllowableTPID1.setStatus(_A)
class _Dot1qFutureVlanPortAllowableTPID2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot1qFutureVlanPortAllowableTPID2_Type.__name__=_C
_Dot1qFutureVlanPortAllowableTPID2_Object=MibTableColumn
dot1qFutureVlanPortAllowableTPID2=_Dot1qFutureVlanPortAllowableTPID2_Object((1,3,6,1,4,1,2076,65,1,10,1,13),_Dot1qFutureVlanPortAllowableTPID2_Type())
dot1qFutureVlanPortAllowableTPID2.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortAllowableTPID2.setStatus(_A)
class _Dot1qFutureVlanPortAllowableTPID3_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot1qFutureVlanPortAllowableTPID3_Type.__name__=_C
_Dot1qFutureVlanPortAllowableTPID3_Object=MibTableColumn
dot1qFutureVlanPortAllowableTPID3=_Dot1qFutureVlanPortAllowableTPID3_Object((1,3,6,1,4,1,2076,65,1,10,1,14),_Dot1qFutureVlanPortAllowableTPID3_Type())
dot1qFutureVlanPortAllowableTPID3.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortAllowableTPID3.setStatus(_A)
class _Dot1qFutureVlanPortUnicastMacSecType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sav',1),('shv',2),('off',3)))
_Dot1qFutureVlanPortUnicastMacSecType_Type.__name__=_C
_Dot1qFutureVlanPortUnicastMacSecType_Object=MibTableColumn
dot1qFutureVlanPortUnicastMacSecType=_Dot1qFutureVlanPortUnicastMacSecType_Object((1,3,6,1,4,1,2076,65,1,10,1,15),_Dot1qFutureVlanPortUnicastMacSecType_Type())
dot1qFutureVlanPortUnicastMacSecType.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortUnicastMacSecType.setStatus(_A)
class _Dot1qFuturePortPacketReflectionStatus_Type(TruthValue):defaultValue=2
_Dot1qFuturePortPacketReflectionStatus_Type.__name__=_H
_Dot1qFuturePortPacketReflectionStatus_Object=MibTableColumn
dot1qFuturePortPacketReflectionStatus=_Dot1qFuturePortPacketReflectionStatus_Object((1,3,6,1,4,1,2076,65,1,10,1,16),_Dot1qFuturePortPacketReflectionStatus_Type())
dot1qFuturePortPacketReflectionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFuturePortPacketReflectionStatus.setStatus(_A)
_Dot1qFutureVlanPortMacMapTable_Object=MibTable
dot1qFutureVlanPortMacMapTable=_Dot1qFutureVlanPortMacMapTable_Object((1,3,6,1,4,1,2076,65,1,11))
if mibBuilder.loadTexts:dot1qFutureVlanPortMacMapTable.setStatus(_A)
_Dot1qFutureVlanPortMacMapEntry_Object=MibTableRow
dot1qFutureVlanPortMacMapEntry=_Dot1qFutureVlanPortMacMapEntry_Object((1,3,6,1,4,1,2076,65,1,11,1))
dot1qFutureVlanPortMacMapEntry.setIndexNames((0,_E,_I),(0,_E,_U))
if mibBuilder.loadTexts:dot1qFutureVlanPortMacMapEntry.setStatus(_A)
_Dot1qFutureVlanPortMacMapAddr_Type=MacAddress
_Dot1qFutureVlanPortMacMapAddr_Object=MibTableColumn
dot1qFutureVlanPortMacMapAddr=_Dot1qFutureVlanPortMacMapAddr_Object((1,3,6,1,4,1,2076,65,1,11,1,1),_Dot1qFutureVlanPortMacMapAddr_Type())
dot1qFutureVlanPortMacMapAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:dot1qFutureVlanPortMacMapAddr.setStatus(_A)
_Dot1qFutureVlanPortMacMapVid_Type=VlanId
_Dot1qFutureVlanPortMacMapVid_Object=MibTableColumn
dot1qFutureVlanPortMacMapVid=_Dot1qFutureVlanPortMacMapVid_Object((1,3,6,1,4,1,2076,65,1,11,1,2),_Dot1qFutureVlanPortMacMapVid_Type())
dot1qFutureVlanPortMacMapVid.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortMacMapVid.setStatus(_A)
_Dot1qFutureVlanPortMacMapName_Type=DisplayString
_Dot1qFutureVlanPortMacMapName_Object=MibTableColumn
dot1qFutureVlanPortMacMapName=_Dot1qFutureVlanPortMacMapName_Object((1,3,6,1,4,1,2076,65,1,11,1,3),_Dot1qFutureVlanPortMacMapName_Type())
dot1qFutureVlanPortMacMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortMacMapName.setStatus(_A)
class _Dot1qFutureVlanPortMacMapMcastBcastOption_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_Dot1qFutureVlanPortMacMapMcastBcastOption_Type.__name__=_C
_Dot1qFutureVlanPortMacMapMcastBcastOption_Object=MibTableColumn
dot1qFutureVlanPortMacMapMcastBcastOption=_Dot1qFutureVlanPortMacMapMcastBcastOption_Object((1,3,6,1,4,1,2076,65,1,11,1,4),_Dot1qFutureVlanPortMacMapMcastBcastOption_Type())
dot1qFutureVlanPortMacMapMcastBcastOption.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortMacMapMcastBcastOption.setStatus(_A)
_Dot1qFutureVlanPortMacMapRowStatus_Type=RowStatus
_Dot1qFutureVlanPortMacMapRowStatus_Object=MibTableColumn
dot1qFutureVlanPortMacMapRowStatus=_Dot1qFutureVlanPortMacMapRowStatus_Object((1,3,6,1,4,1,2076,65,1,11,1,5),_Dot1qFutureVlanPortMacMapRowStatus_Type())
dot1qFutureVlanPortMacMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortMacMapRowStatus.setStatus(_A)
_Dot1qFutureVlanFidMapTable_Object=MibTable
dot1qFutureVlanFidMapTable=_Dot1qFutureVlanFidMapTable_Object((1,3,6,1,4,1,2076,65,1,12))
if mibBuilder.loadTexts:dot1qFutureVlanFidMapTable.setStatus(_A)
_Dot1qFutureVlanFidMapEntry_Object=MibTableRow
dot1qFutureVlanFidMapEntry=_Dot1qFutureVlanFidMapEntry_Object((1,3,6,1,4,1,2076,65,1,12,1))
dot1qFutureVlanFidMapEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:dot1qFutureVlanFidMapEntry.setStatus(_A)
class _Dot1qFutureVlanIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Dot1qFutureVlanIndex_Type.__name__=_L
_Dot1qFutureVlanIndex_Object=MibTableColumn
dot1qFutureVlanIndex=_Dot1qFutureVlanIndex_Object((1,3,6,1,4,1,2076,65,1,12,1,1),_Dot1qFutureVlanIndex_Type())
dot1qFutureVlanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureVlanIndex.setStatus(_A)
class _Dot1qFutureVlanFid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Dot1qFutureVlanFid_Type.__name__=_L
_Dot1qFutureVlanFid_Object=MibTableColumn
dot1qFutureVlanFid=_Dot1qFutureVlanFid_Object((1,3,6,1,4,1,2076,65,1,12,1,2),_Dot1qFutureVlanFid_Type())
dot1qFutureVlanFid.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanFid.setStatus(_A)
_Dot1qFutureVlanOperStatus_Type=EnabledStatus
_Dot1qFutureVlanOperStatus_Object=MibScalar
dot1qFutureVlanOperStatus=_Dot1qFutureVlanOperStatus_Object((1,3,6,1,4,1,2076,65,1,13),_Dot1qFutureVlanOperStatus_Type())
dot1qFutureVlanOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureVlanOperStatus.setStatus(_A)
_Dot1qFutureGvrpOperStatus_Type=EnabledStatus
_Dot1qFutureGvrpOperStatus_Object=MibScalar
dot1qFutureGvrpOperStatus=_Dot1qFutureGvrpOperStatus_Object((1,3,6,1,4,1,2076,65,1,14),_Dot1qFutureGvrpOperStatus_Type())
dot1qFutureGvrpOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureGvrpOperStatus.setStatus(_A)
_Dot1qFutureGmrpOperStatus_Type=EnabledStatus
_Dot1qFutureGmrpOperStatus_Object=MibScalar
dot1qFutureGmrpOperStatus=_Dot1qFutureGmrpOperStatus_Object((1,3,6,1,4,1,2076,65,1,15),_Dot1qFutureGmrpOperStatus_Type())
dot1qFutureGmrpOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureGmrpOperStatus.setStatus(_A)
_Dot1qFutureVlanCounterTable_Object=MibTable
dot1qFutureVlanCounterTable=_Dot1qFutureVlanCounterTable_Object((1,3,6,1,4,1,2076,65,1,16))
if mibBuilder.loadTexts:dot1qFutureVlanCounterTable.setStatus(_A)
_Dot1qFutureVlanCounterEntry_Object=MibTableRow
dot1qFutureVlanCounterEntry=_Dot1qFutureVlanCounterEntry_Object((1,3,6,1,4,1,2076,65,1,16,1))
dot1qFutureVlanCounterEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:dot1qFutureVlanCounterEntry.setStatus(_A)
_Dot1qFutureVlanCounterRxUcast_Type=Counter32
_Dot1qFutureVlanCounterRxUcast_Object=MibTableColumn
dot1qFutureVlanCounterRxUcast=_Dot1qFutureVlanCounterRxUcast_Object((1,3,6,1,4,1,2076,65,1,16,1,1),_Dot1qFutureVlanCounterRxUcast_Type())
dot1qFutureVlanCounterRxUcast.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureVlanCounterRxUcast.setStatus(_A)
_Dot1qFutureVlanCounterRxMcastBcast_Type=Counter32
_Dot1qFutureVlanCounterRxMcastBcast_Object=MibTableColumn
dot1qFutureVlanCounterRxMcastBcast=_Dot1qFutureVlanCounterRxMcastBcast_Object((1,3,6,1,4,1,2076,65,1,16,1,2),_Dot1qFutureVlanCounterRxMcastBcast_Type())
dot1qFutureVlanCounterRxMcastBcast.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureVlanCounterRxMcastBcast.setStatus(_A)
_Dot1qFutureVlanCounterTxUnknUcast_Type=Counter32
_Dot1qFutureVlanCounterTxUnknUcast_Object=MibTableColumn
dot1qFutureVlanCounterTxUnknUcast=_Dot1qFutureVlanCounterTxUnknUcast_Object((1,3,6,1,4,1,2076,65,1,16,1,3),_Dot1qFutureVlanCounterTxUnknUcast_Type())
dot1qFutureVlanCounterTxUnknUcast.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureVlanCounterTxUnknUcast.setStatus(_A)
_Dot1qFutureVlanCounterTxUcast_Type=Counter32
_Dot1qFutureVlanCounterTxUcast_Object=MibTableColumn
dot1qFutureVlanCounterTxUcast=_Dot1qFutureVlanCounterTxUcast_Object((1,3,6,1,4,1,2076,65,1,16,1,4),_Dot1qFutureVlanCounterTxUcast_Type())
dot1qFutureVlanCounterTxUcast.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureVlanCounterTxUcast.setStatus(_A)
_Dot1qFutureVlanCounterTxBcast_Type=Counter32
_Dot1qFutureVlanCounterTxBcast_Object=MibTableColumn
dot1qFutureVlanCounterTxBcast=_Dot1qFutureVlanCounterTxBcast_Object((1,3,6,1,4,1,2076,65,1,16,1,5),_Dot1qFutureVlanCounterTxBcast_Type())
dot1qFutureVlanCounterTxBcast.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureVlanCounterTxBcast.setStatus(_A)
_Dot1qFutureVlanCounterRxFrames_Type=Counter32
_Dot1qFutureVlanCounterRxFrames_Object=MibTableColumn
dot1qFutureVlanCounterRxFrames=_Dot1qFutureVlanCounterRxFrames_Object((1,3,6,1,4,1,2076,65,1,16,1,6),_Dot1qFutureVlanCounterRxFrames_Type())
dot1qFutureVlanCounterRxFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureVlanCounterRxFrames.setStatus(_A)
_Dot1qFutureVlanCounterRxBytes_Type=Counter32
_Dot1qFutureVlanCounterRxBytes_Object=MibTableColumn
dot1qFutureVlanCounterRxBytes=_Dot1qFutureVlanCounterRxBytes_Object((1,3,6,1,4,1,2076,65,1,16,1,7),_Dot1qFutureVlanCounterRxBytes_Type())
dot1qFutureVlanCounterRxBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureVlanCounterRxBytes.setStatus(_A)
_Dot1qFutureVlanCounterTxFrames_Type=Counter32
_Dot1qFutureVlanCounterTxFrames_Object=MibTableColumn
dot1qFutureVlanCounterTxFrames=_Dot1qFutureVlanCounterTxFrames_Object((1,3,6,1,4,1,2076,65,1,16,1,8),_Dot1qFutureVlanCounterTxFrames_Type())
dot1qFutureVlanCounterTxFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureVlanCounterTxFrames.setStatus(_A)
_Dot1qFutureVlanCounterTxBytes_Type=Counter32
_Dot1qFutureVlanCounterTxBytes_Object=MibTableColumn
dot1qFutureVlanCounterTxBytes=_Dot1qFutureVlanCounterTxBytes_Object((1,3,6,1,4,1,2076,65,1,16,1,9),_Dot1qFutureVlanCounterTxBytes_Type())
dot1qFutureVlanCounterTxBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureVlanCounterTxBytes.setStatus(_A)
_Dot1qFutureVlanCounterDiscardFrames_Type=Counter32
_Dot1qFutureVlanCounterDiscardFrames_Object=MibTableColumn
dot1qFutureVlanCounterDiscardFrames=_Dot1qFutureVlanCounterDiscardFrames_Object((1,3,6,1,4,1,2076,65,1,16,1,10),_Dot1qFutureVlanCounterDiscardFrames_Type())
dot1qFutureVlanCounterDiscardFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureVlanCounterDiscardFrames.setStatus(_A)
_Dot1qFutureVlanCounterDiscardBytes_Type=Counter32
_Dot1qFutureVlanCounterDiscardBytes_Object=MibTableColumn
dot1qFutureVlanCounterDiscardBytes=_Dot1qFutureVlanCounterDiscardBytes_Object((1,3,6,1,4,1,2076,65,1,16,1,11),_Dot1qFutureVlanCounterDiscardBytes_Type())
dot1qFutureVlanCounterDiscardBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureVlanCounterDiscardBytes.setStatus(_A)
class _Dot1qFutureVlanCounterStatus_Type(EnabledStatus):defaultValue=2
_Dot1qFutureVlanCounterStatus_Type.__name__=_G
_Dot1qFutureVlanCounterStatus_Object=MibTableColumn
dot1qFutureVlanCounterStatus=_Dot1qFutureVlanCounterStatus_Object((1,3,6,1,4,1,2076,65,1,16,1,12),_Dot1qFutureVlanCounterStatus_Type())
dot1qFutureVlanCounterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanCounterStatus.setStatus(_A)
_Dot1qFutureVlanUnicastMacControlTable_Object=MibTable
dot1qFutureVlanUnicastMacControlTable=_Dot1qFutureVlanUnicastMacControlTable_Object((1,3,6,1,4,1,2076,65,1,17))
if mibBuilder.loadTexts:dot1qFutureVlanUnicastMacControlTable.setStatus(_A)
_Dot1qFutureVlanUnicastMacControlEntry_Object=MibTableRow
dot1qFutureVlanUnicastMacControlEntry=_Dot1qFutureVlanUnicastMacControlEntry_Object((1,3,6,1,4,1,2076,65,1,17,1))
dot1qFutureVlanUnicastMacControlEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:dot1qFutureVlanUnicastMacControlEntry.setStatus(_A)
class _Dot1qFutureVlanUnicastMacLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Dot1qFutureVlanUnicastMacLimit_Type.__name__=_L
_Dot1qFutureVlanUnicastMacLimit_Object=MibTableColumn
dot1qFutureVlanUnicastMacLimit=_Dot1qFutureVlanUnicastMacLimit_Object((1,3,6,1,4,1,2076,65,1,17,1,1),_Dot1qFutureVlanUnicastMacLimit_Type())
dot1qFutureVlanUnicastMacLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanUnicastMacLimit.setStatus(_A)
class _Dot1qFutureVlanAdminMacLearningStatus_Type(MacLearningStatus):defaultValue=3
_Dot1qFutureVlanAdminMacLearningStatus_Type.__name__=_V
_Dot1qFutureVlanAdminMacLearningStatus_Object=MibTableColumn
dot1qFutureVlanAdminMacLearningStatus=_Dot1qFutureVlanAdminMacLearningStatus_Object((1,3,6,1,4,1,2076,65,1,17,1,2),_Dot1qFutureVlanAdminMacLearningStatus_Type())
dot1qFutureVlanAdminMacLearningStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanAdminMacLearningStatus.setStatus(_A)
_Dot1qFutureVlanOperMacLearningStatus_Type=EnabledStatus
_Dot1qFutureVlanOperMacLearningStatus_Object=MibTableColumn
dot1qFutureVlanOperMacLearningStatus=_Dot1qFutureVlanOperMacLearningStatus_Object((1,3,6,1,4,1,2076,65,1,17,1,3),_Dot1qFutureVlanOperMacLearningStatus_Type())
dot1qFutureVlanOperMacLearningStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureVlanOperMacLearningStatus.setStatus(_A)
class _Dot1qFutureVlanPortFdbFlush_Type(TruthValue):defaultValue=2
_Dot1qFutureVlanPortFdbFlush_Type.__name__=_H
_Dot1qFutureVlanPortFdbFlush_Object=MibTableColumn
dot1qFutureVlanPortFdbFlush=_Dot1qFutureVlanPortFdbFlush_Object((1,3,6,1,4,1,2076,65,1,17,1,4),_Dot1qFutureVlanPortFdbFlush_Type())
dot1qFutureVlanPortFdbFlush.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortFdbFlush.setStatus(_A)
class _Dot1qFutureGarpDebug_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048575))
_Dot1qFutureGarpDebug_Type.__name__=_C
_Dot1qFutureGarpDebug_Object=MibScalar
dot1qFutureGarpDebug=_Dot1qFutureGarpDebug_Object((1,3,6,1,4,1,2076,65,1,18),_Dot1qFutureGarpDebug_Type())
dot1qFutureGarpDebug.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureGarpDebug.setStatus(_A)
_Dot1qFutureVlanTpFdbTable_Object=MibTable
dot1qFutureVlanTpFdbTable=_Dot1qFutureVlanTpFdbTable_Object((1,3,6,1,4,1,2076,65,1,19))
if mibBuilder.loadTexts:dot1qFutureVlanTpFdbTable.setStatus(_A)
_Dot1qFutureVlanTpFdbEntry_Object=MibTableRow
dot1qFutureVlanTpFdbEntry=_Dot1qFutureVlanTpFdbEntry_Object((1,3,6,1,4,1,2076,65,1,19,1))
if mibBuilder.loadTexts:dot1qFutureVlanTpFdbEntry.setStatus(_A)
_Dot1qFutureVlanTpFdbPw_Type=Unsigned32
_Dot1qFutureVlanTpFdbPw_Object=MibTableColumn
dot1qFutureVlanTpFdbPw=_Dot1qFutureVlanTpFdbPw_Object((1,3,6,1,4,1,2076,65,1,19,1,1),_Dot1qFutureVlanTpFdbPw_Type())
dot1qFutureVlanTpFdbPw.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureVlanTpFdbPw.setStatus(_A)
class _Dot1qTpOldFdbPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot1qTpOldFdbPort_Type.__name__=_C
_Dot1qTpOldFdbPort_Object=MibTableColumn
dot1qTpOldFdbPort=_Dot1qTpOldFdbPort_Object((1,3,6,1,4,1,2076,65,1,19,1,2),_Dot1qTpOldFdbPort_Type())
dot1qTpOldFdbPort.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qTpOldFdbPort.setStatus(_A)
_Dot1qFutureConnectionIdentifier_Type=MacAddress
_Dot1qFutureConnectionIdentifier_Object=MibTableColumn
dot1qFutureConnectionIdentifier=_Dot1qFutureConnectionIdentifier_Object((1,3,6,1,4,1,2076,65,1,19,1,3),_Dot1qFutureConnectionIdentifier_Type())
dot1qFutureConnectionIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureConnectionIdentifier.setStatus(_A)
_Dot1qFutureVlanWildCardTable_Object=MibTable
dot1qFutureVlanWildCardTable=_Dot1qFutureVlanWildCardTable_Object((1,3,6,1,4,1,2076,65,1,20))
if mibBuilder.loadTexts:dot1qFutureVlanWildCardTable.setStatus(_A)
_Dot1qFutureVlanWildCardEntry_Object=MibTableRow
dot1qFutureVlanWildCardEntry=_Dot1qFutureVlanWildCardEntry_Object((1,3,6,1,4,1,2076,65,1,20,1))
dot1qFutureVlanWildCardEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:dot1qFutureVlanWildCardEntry.setStatus(_A)
_Dot1qFutureVlanWildCardMacAddress_Type=MacAddress
_Dot1qFutureVlanWildCardMacAddress_Object=MibTableColumn
dot1qFutureVlanWildCardMacAddress=_Dot1qFutureVlanWildCardMacAddress_Object((1,3,6,1,4,1,2076,65,1,20,1,1),_Dot1qFutureVlanWildCardMacAddress_Type())
dot1qFutureVlanWildCardMacAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:dot1qFutureVlanWildCardMacAddress.setStatus(_A)
_Dot1qFutureVlanWildCardEgressPorts_Type=PortList
_Dot1qFutureVlanWildCardEgressPorts_Object=MibTableColumn
dot1qFutureVlanWildCardEgressPorts=_Dot1qFutureVlanWildCardEgressPorts_Object((1,3,6,1,4,1,2076,65,1,20,1,2),_Dot1qFutureVlanWildCardEgressPorts_Type())
dot1qFutureVlanWildCardEgressPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanWildCardEgressPorts.setStatus(_A)
_Dot1qFutureVlanWildCardRowStatus_Type=RowStatus
_Dot1qFutureVlanWildCardRowStatus_Object=MibTableColumn
dot1qFutureVlanWildCardRowStatus=_Dot1qFutureVlanWildCardRowStatus_Object((1,3,6,1,4,1,2076,65,1,20,1,3),_Dot1qFutureVlanWildCardRowStatus_Type())
dot1qFutureVlanWildCardRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanWildCardRowStatus.setStatus(_A)
_Dot1qFutureStaticUnicastExtnTable_Object=MibTable
dot1qFutureStaticUnicastExtnTable=_Dot1qFutureStaticUnicastExtnTable_Object((1,3,6,1,4,1,2076,65,1,21))
if mibBuilder.loadTexts:dot1qFutureStaticUnicastExtnTable.setStatus(_A)
_Dot1qFutureStaticUnicastExtnEntry_Object=MibTableRow
dot1qFutureStaticUnicastExtnEntry=_Dot1qFutureStaticUnicastExtnEntry_Object((1,3,6,1,4,1,2076,65,1,21,1))
if mibBuilder.loadTexts:dot1qFutureStaticUnicastExtnEntry.setStatus(_A)
_Dot1qFutureStaticConnectionIdentifier_Type=MacAddress
_Dot1qFutureStaticConnectionIdentifier_Object=MibTableColumn
dot1qFutureStaticConnectionIdentifier=_Dot1qFutureStaticConnectionIdentifier_Object((1,3,6,1,4,1,2076,65,1,21,1,1),_Dot1qFutureStaticConnectionIdentifier_Type())
dot1qFutureStaticConnectionIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureStaticConnectionIdentifier.setStatus(_A)
class _Dot1qFutureUnicastMacLearningLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Dot1qFutureUnicastMacLearningLimit_Type.__name__=_L
_Dot1qFutureUnicastMacLearningLimit_Object=MibScalar
dot1qFutureUnicastMacLearningLimit=_Dot1qFutureUnicastMacLearningLimit_Object((1,3,6,1,4,1,2076,65,1,22),_Dot1qFutureUnicastMacLearningLimit_Type())
dot1qFutureUnicastMacLearningLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureUnicastMacLearningLimit.setStatus(_A)
class _Dot1qFutureVlanBaseBridgeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dot1dTransparentMode',1),('dot1qVlanMode',2)))
_Dot1qFutureVlanBaseBridgeMode_Type.__name__=_C
_Dot1qFutureVlanBaseBridgeMode_Object=MibScalar
dot1qFutureVlanBaseBridgeMode=_Dot1qFutureVlanBaseBridgeMode_Object((1,3,6,1,4,1,2076,65,1,23),_Dot1qFutureVlanBaseBridgeMode_Type())
dot1qFutureVlanBaseBridgeMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanBaseBridgeMode.setStatus(_A)
_Dot1qFutureVlanSubnetBasedOnAllPorts_Type=EnabledStatus
_Dot1qFutureVlanSubnetBasedOnAllPorts_Object=MibScalar
dot1qFutureVlanSubnetBasedOnAllPorts=_Dot1qFutureVlanSubnetBasedOnAllPorts_Object((1,3,6,1,4,1,2076,65,1,24),_Dot1qFutureVlanSubnetBasedOnAllPorts_Type())
dot1qFutureVlanSubnetBasedOnAllPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanSubnetBasedOnAllPorts.setStatus(_A)
_Dot1qFutureVlanPortSubnetMapTable_Object=MibTable
dot1qFutureVlanPortSubnetMapTable=_Dot1qFutureVlanPortSubnetMapTable_Object((1,3,6,1,4,1,2076,65,1,25))
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapTable.setStatus(_A)
_Dot1qFutureVlanPortSubnetMapEntry_Object=MibTableRow
dot1qFutureVlanPortSubnetMapEntry=_Dot1qFutureVlanPortSubnetMapEntry_Object((1,3,6,1,4,1,2076,65,1,25,1))
dot1qFutureVlanPortSubnetMapEntry.setIndexNames((0,_E,_I),(0,_E,_X))
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapEntry.setStatus(_A)
_Dot1qFutureVlanPortSubnetMapAddr_Type=IpAddress
_Dot1qFutureVlanPortSubnetMapAddr_Object=MibTableColumn
dot1qFutureVlanPortSubnetMapAddr=_Dot1qFutureVlanPortSubnetMapAddr_Object((1,3,6,1,4,1,2076,65,1,25,1,1),_Dot1qFutureVlanPortSubnetMapAddr_Type())
dot1qFutureVlanPortSubnetMapAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapAddr.setStatus(_A)
_Dot1qFutureVlanPortSubnetMapVid_Type=VlanId
_Dot1qFutureVlanPortSubnetMapVid_Object=MibTableColumn
dot1qFutureVlanPortSubnetMapVid=_Dot1qFutureVlanPortSubnetMapVid_Object((1,3,6,1,4,1,2076,65,1,25,1,2),_Dot1qFutureVlanPortSubnetMapVid_Type())
dot1qFutureVlanPortSubnetMapVid.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapVid.setStatus(_A)
class _Dot1qFutureVlanPortSubnetMapARPOption_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_Dot1qFutureVlanPortSubnetMapARPOption_Type.__name__=_C
_Dot1qFutureVlanPortSubnetMapARPOption_Object=MibTableColumn
dot1qFutureVlanPortSubnetMapARPOption=_Dot1qFutureVlanPortSubnetMapARPOption_Object((1,3,6,1,4,1,2076,65,1,25,1,3),_Dot1qFutureVlanPortSubnetMapARPOption_Type())
dot1qFutureVlanPortSubnetMapARPOption.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapARPOption.setStatus(_A)
_Dot1qFutureVlanPortSubnetMapRowStatus_Type=RowStatus
_Dot1qFutureVlanPortSubnetMapRowStatus_Object=MibTableColumn
dot1qFutureVlanPortSubnetMapRowStatus=_Dot1qFutureVlanPortSubnetMapRowStatus_Object((1,3,6,1,4,1,2076,65,1,25,1,4),_Dot1qFutureVlanPortSubnetMapRowStatus_Type())
dot1qFutureVlanPortSubnetMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapRowStatus.setStatus(_A)
class _Dot1qFutureVlanGlobalMacLearningStatus_Type(EnabledStatus):defaultValue=1
_Dot1qFutureVlanGlobalMacLearningStatus_Type.__name__=_G
_Dot1qFutureVlanGlobalMacLearningStatus_Object=MibScalar
dot1qFutureVlanGlobalMacLearningStatus=_Dot1qFutureVlanGlobalMacLearningStatus_Object((1,3,6,1,4,1,2076,65,1,26),_Dot1qFutureVlanGlobalMacLearningStatus_Type())
dot1qFutureVlanGlobalMacLearningStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanGlobalMacLearningStatus.setStatus(_A)
class _Dot1qFutureVlanApplyEnhancedFilteringCriteria_Type(TruthValue):defaultValue=1
_Dot1qFutureVlanApplyEnhancedFilteringCriteria_Type.__name__=_H
_Dot1qFutureVlanApplyEnhancedFilteringCriteria_Object=MibScalar
dot1qFutureVlanApplyEnhancedFilteringCriteria=_Dot1qFutureVlanApplyEnhancedFilteringCriteria_Object((1,3,6,1,4,1,2076,65,1,27),_Dot1qFutureVlanApplyEnhancedFilteringCriteria_Type())
dot1qFutureVlanApplyEnhancedFilteringCriteria.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanApplyEnhancedFilteringCriteria.setStatus(_A)
_Dot1qFutureVlanSwStatsEnabled_Type=TruthValue
_Dot1qFutureVlanSwStatsEnabled_Object=MibScalar
dot1qFutureVlanSwStatsEnabled=_Dot1qFutureVlanSwStatsEnabled_Object((1,3,6,1,4,1,2076,65,1,28),_Dot1qFutureVlanSwStatsEnabled_Type())
dot1qFutureVlanSwStatsEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanSwStatsEnabled.setStatus(_A)
_Dot1qFutureStVlanExtTable_Object=MibTable
dot1qFutureStVlanExtTable=_Dot1qFutureStVlanExtTable_Object((1,3,6,1,4,1,2076,65,1,29))
if mibBuilder.loadTexts:dot1qFutureStVlanExtTable.setStatus(_A)
_Dot1qFutureStVlanExtEntry_Object=MibTableRow
dot1qFutureStVlanExtEntry=_Dot1qFutureStVlanExtEntry_Object((1,3,6,1,4,1,2076,65,1,29,1))
if mibBuilder.loadTexts:dot1qFutureStVlanExtEntry.setStatus(_A)
class _Dot1qFutureStVlanPVlanType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),('primary',2),('isolated',3),('community',4)))
_Dot1qFutureStVlanPVlanType_Type.__name__=_C
_Dot1qFutureStVlanPVlanType_Object=MibTableColumn
dot1qFutureStVlanPVlanType=_Dot1qFutureStVlanPVlanType_Object((1,3,6,1,4,1,2076,65,1,29,1,1),_Dot1qFutureStVlanPVlanType_Type())
dot1qFutureStVlanPVlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureStVlanPVlanType.setStatus(_A)
class _Dot1qFutureStVlanPrimaryVid_Type(VlanIdOrNone):defaultValue=0
_Dot1qFutureStVlanPrimaryVid_Type.__name__=_P
_Dot1qFutureStVlanPrimaryVid_Object=MibTableColumn
dot1qFutureStVlanPrimaryVid=_Dot1qFutureStVlanPrimaryVid_Object((1,3,6,1,4,1,2076,65,1,29,1,2),_Dot1qFutureStVlanPrimaryVid_Type())
dot1qFutureStVlanPrimaryVid.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureStVlanPrimaryVid.setStatus(_A)
class _Dot1qFutureStVlanEgressEthertype_Type(Integer32):defaultValue=33024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot1qFutureStVlanEgressEthertype_Type.__name__=_C
_Dot1qFutureStVlanEgressEthertype_Object=MibTableColumn
dot1qFutureStVlanEgressEthertype=_Dot1qFutureStVlanEgressEthertype_Object((1,3,6,1,4,1,2076,65,1,29,1,3),_Dot1qFutureStVlanEgressEthertype_Type())
dot1qFutureStVlanEgressEthertype.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureStVlanEgressEthertype.setStatus(_A)
_Dot1qFutureVlanPortSubnetMapExtTable_Object=MibTable
dot1qFutureVlanPortSubnetMapExtTable=_Dot1qFutureVlanPortSubnetMapExtTable_Object((1,3,6,1,4,1,2076,65,1,30))
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapExtTable.setStatus(_A)
_Dot1qFutureVlanPortSubnetMapExtEntry_Object=MibTableRow
dot1qFutureVlanPortSubnetMapExtEntry=_Dot1qFutureVlanPortSubnetMapExtEntry_Object((1,3,6,1,4,1,2076,65,1,30,1))
dot1qFutureVlanPortSubnetMapExtEntry.setIndexNames((0,_E,_I),(0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapExtEntry.setStatus(_A)
_Dot1qFutureVlanPortSubnetMapExtAddr_Type=IpAddress
_Dot1qFutureVlanPortSubnetMapExtAddr_Object=MibTableColumn
dot1qFutureVlanPortSubnetMapExtAddr=_Dot1qFutureVlanPortSubnetMapExtAddr_Object((1,3,6,1,4,1,2076,65,1,30,1,1),_Dot1qFutureVlanPortSubnetMapExtAddr_Type())
dot1qFutureVlanPortSubnetMapExtAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapExtAddr.setStatus(_A)
_Dot1qFutureVlanPortSubnetMapExtMask_Type=IpAddress
_Dot1qFutureVlanPortSubnetMapExtMask_Object=MibTableColumn
dot1qFutureVlanPortSubnetMapExtMask=_Dot1qFutureVlanPortSubnetMapExtMask_Object((1,3,6,1,4,1,2076,65,1,30,1,2),_Dot1qFutureVlanPortSubnetMapExtMask_Type())
dot1qFutureVlanPortSubnetMapExtMask.setMaxAccess(_J)
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapExtMask.setStatus(_A)
_Dot1qFutureVlanPortSubnetMapExtVid_Type=VlanId
_Dot1qFutureVlanPortSubnetMapExtVid_Object=MibTableColumn
dot1qFutureVlanPortSubnetMapExtVid=_Dot1qFutureVlanPortSubnetMapExtVid_Object((1,3,6,1,4,1,2076,65,1,30,1,3),_Dot1qFutureVlanPortSubnetMapExtVid_Type())
dot1qFutureVlanPortSubnetMapExtVid.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapExtVid.setStatus(_A)
class _Dot1qFutureVlanPortSubnetMapExtARPOption_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_Dot1qFutureVlanPortSubnetMapExtARPOption_Type.__name__=_C
_Dot1qFutureVlanPortSubnetMapExtARPOption_Object=MibTableColumn
dot1qFutureVlanPortSubnetMapExtARPOption=_Dot1qFutureVlanPortSubnetMapExtARPOption_Object((1,3,6,1,4,1,2076,65,1,30,1,4),_Dot1qFutureVlanPortSubnetMapExtARPOption_Type())
dot1qFutureVlanPortSubnetMapExtARPOption.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapExtARPOption.setStatus(_A)
_Dot1qFutureVlanPortSubnetMapExtRowStatus_Type=RowStatus
_Dot1qFutureVlanPortSubnetMapExtRowStatus_Object=MibTableColumn
dot1qFutureVlanPortSubnetMapExtRowStatus=_Dot1qFutureVlanPortSubnetMapExtRowStatus_Object((1,3,6,1,4,1,2076,65,1,30,1,5),_Dot1qFutureVlanPortSubnetMapExtRowStatus_Type())
dot1qFutureVlanPortSubnetMapExtRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanPortSubnetMapExtRowStatus.setStatus(_A)
_Dot1qFutureVlanGlobalsFdbFlush_Type=TruthValue
_Dot1qFutureVlanGlobalsFdbFlush_Object=MibScalar
dot1qFutureVlanGlobalsFdbFlush=_Dot1qFutureVlanGlobalsFdbFlush_Object((1,3,6,1,4,1,2076,65,1,31),_Dot1qFutureVlanGlobalsFdbFlush_Type())
dot1qFutureVlanGlobalsFdbFlush.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanGlobalsFdbFlush.setStatus(_A)
class _Dot1qFutureVlanUserDefinedTPID_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot1qFutureVlanUserDefinedTPID_Type.__name__=_C
_Dot1qFutureVlanUserDefinedTPID_Object=MibScalar
dot1qFutureVlanUserDefinedTPID=_Dot1qFutureVlanUserDefinedTPID_Object((1,3,6,1,4,1,2076,65,1,32),_Dot1qFutureVlanUserDefinedTPID_Type())
dot1qFutureVlanUserDefinedTPID.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanUserDefinedTPID.setStatus(_A)
_Dot1qFutureVlanLoopbackTable_Object=MibTable
dot1qFutureVlanLoopbackTable=_Dot1qFutureVlanLoopbackTable_Object((1,3,6,1,4,1,2076,65,1,33))
if mibBuilder.loadTexts:dot1qFutureVlanLoopbackTable.setStatus(_A)
_Dot1qFutureVlanLoopbackEntry_Object=MibTableRow
dot1qFutureVlanLoopbackEntry=_Dot1qFutureVlanLoopbackEntry_Object((1,3,6,1,4,1,2076,65,1,33,1))
dot1qFutureVlanLoopbackEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:dot1qFutureVlanLoopbackEntry.setStatus(_A)
class _Dot1qFutureVlanLoopbackStatus_Type(EnabledStatus):defaultValue=2
_Dot1qFutureVlanLoopbackStatus_Type.__name__=_G
_Dot1qFutureVlanLoopbackStatus_Object=MibTableColumn
dot1qFutureVlanLoopbackStatus=_Dot1qFutureVlanLoopbackStatus_Object((1,3,6,1,4,1,2076,65,1,33,1,1),_Dot1qFutureVlanLoopbackStatus_Type())
dot1qFutureVlanLoopbackStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanLoopbackStatus.setStatus(_A)
_Dot1qFutureVlanTunnelConfig_ObjectIdentity=ObjectIdentity
dot1qFutureVlanTunnelConfig=_Dot1qFutureVlanTunnelConfig_ObjectIdentity((1,3,6,1,4,1,2076,65,2))
class _Dot1qFutureVlanBridgeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('customerBridge',1),('providerBridge',2),('providerCoreBridge',3),('providerEdgeBridge',4)))
_Dot1qFutureVlanBridgeMode_Type.__name__=_C
_Dot1qFutureVlanBridgeMode_Object=MibScalar
dot1qFutureVlanBridgeMode=_Dot1qFutureVlanBridgeMode_Object((1,3,6,1,4,1,2076,65,2,1),_Dot1qFutureVlanBridgeMode_Type())
dot1qFutureVlanBridgeMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanBridgeMode.setStatus(_F)
class _Dot1qFutureVlanTunnelBpduPri_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot1qFutureVlanTunnelBpduPri_Type.__name__=_C
_Dot1qFutureVlanTunnelBpduPri_Object=MibScalar
dot1qFutureVlanTunnelBpduPri=_Dot1qFutureVlanTunnelBpduPri_Object((1,3,6,1,4,1,2076,65,2,2),_Dot1qFutureVlanTunnelBpduPri_Type())
dot1qFutureVlanTunnelBpduPri.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanTunnelBpduPri.setStatus(_F)
_Dot1qFutureVlanTunnelTable_Object=MibTable
dot1qFutureVlanTunnelTable=_Dot1qFutureVlanTunnelTable_Object((1,3,6,1,4,1,2076,65,2,3))
if mibBuilder.loadTexts:dot1qFutureVlanTunnelTable.setStatus(_F)
_Dot1qFutureVlanTunnelEntry_Object=MibTableRow
dot1qFutureVlanTunnelEntry=_Dot1qFutureVlanTunnelEntry_Object((1,3,6,1,4,1,2076,65,2,3,1))
dot1qFutureVlanTunnelEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:dot1qFutureVlanTunnelEntry.setStatus(_F)
class _Dot1qFutureVlanTunnelStatus_Type(EnabledStatus):defaultValue=2
_Dot1qFutureVlanTunnelStatus_Type.__name__=_G
_Dot1qFutureVlanTunnelStatus_Object=MibTableColumn
dot1qFutureVlanTunnelStatus=_Dot1qFutureVlanTunnelStatus_Object((1,3,6,1,4,1,2076,65,2,3,1,1),_Dot1qFutureVlanTunnelStatus_Type())
dot1qFutureVlanTunnelStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanTunnelStatus.setStatus(_F)
_Dot1qFutureVlanTunnelProtocolTable_Object=MibTable
dot1qFutureVlanTunnelProtocolTable=_Dot1qFutureVlanTunnelProtocolTable_Object((1,3,6,1,4,1,2076,65,2,4))
if mibBuilder.loadTexts:dot1qFutureVlanTunnelProtocolTable.setStatus(_F)
_Dot1qFutureVlanTunnelProtocolEntry_Object=MibTableRow
dot1qFutureVlanTunnelProtocolEntry=_Dot1qFutureVlanTunnelProtocolEntry_Object((1,3,6,1,4,1,2076,65,2,4,1))
dot1qFutureVlanTunnelProtocolEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:dot1qFutureVlanTunnelProtocolEntry.setStatus(_F)
class _Dot1qFutureVlanTunnelStpPDUs_Type(EnabledStatus):defaultValue=2
_Dot1qFutureVlanTunnelStpPDUs_Type.__name__=_G
_Dot1qFutureVlanTunnelStpPDUs_Object=MibTableColumn
dot1qFutureVlanTunnelStpPDUs=_Dot1qFutureVlanTunnelStpPDUs_Object((1,3,6,1,4,1,2076,65,2,4,1,1),_Dot1qFutureVlanTunnelStpPDUs_Type())
dot1qFutureVlanTunnelStpPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanTunnelStpPDUs.setStatus(_F)
_Dot1qFutureVlanTunnelStpPDUsRecvd_Type=Counter32
_Dot1qFutureVlanTunnelStpPDUsRecvd_Object=MibTableColumn
dot1qFutureVlanTunnelStpPDUsRecvd=_Dot1qFutureVlanTunnelStpPDUsRecvd_Object((1,3,6,1,4,1,2076,65,2,4,1,2),_Dot1qFutureVlanTunnelStpPDUsRecvd_Type())
dot1qFutureVlanTunnelStpPDUsRecvd.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureVlanTunnelStpPDUsRecvd.setStatus(_F)
_Dot1qFutureVlanTunnelStpPDUsSent_Type=Counter32
_Dot1qFutureVlanTunnelStpPDUsSent_Object=MibTableColumn
dot1qFutureVlanTunnelStpPDUsSent=_Dot1qFutureVlanTunnelStpPDUsSent_Object((1,3,6,1,4,1,2076,65,2,4,1,3),_Dot1qFutureVlanTunnelStpPDUsSent_Type())
dot1qFutureVlanTunnelStpPDUsSent.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureVlanTunnelStpPDUsSent.setStatus(_F)
class _Dot1qFutureVlanTunnelGvrpPDUs_Type(EnabledStatus):defaultValue=1
_Dot1qFutureVlanTunnelGvrpPDUs_Type.__name__=_G
_Dot1qFutureVlanTunnelGvrpPDUs_Object=MibTableColumn
dot1qFutureVlanTunnelGvrpPDUs=_Dot1qFutureVlanTunnelGvrpPDUs_Object((1,3,6,1,4,1,2076,65,2,4,1,4),_Dot1qFutureVlanTunnelGvrpPDUs_Type())
dot1qFutureVlanTunnelGvrpPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanTunnelGvrpPDUs.setStatus(_F)
_Dot1qFutureVlanTunnelGvrpPDUsRecvd_Type=Counter32
_Dot1qFutureVlanTunnelGvrpPDUsRecvd_Object=MibTableColumn
dot1qFutureVlanTunnelGvrpPDUsRecvd=_Dot1qFutureVlanTunnelGvrpPDUsRecvd_Object((1,3,6,1,4,1,2076,65,2,4,1,5),_Dot1qFutureVlanTunnelGvrpPDUsRecvd_Type())
dot1qFutureVlanTunnelGvrpPDUsRecvd.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureVlanTunnelGvrpPDUsRecvd.setStatus(_F)
_Dot1qFutureVlanTunnelGvrpPDUsSent_Type=Counter32
_Dot1qFutureVlanTunnelGvrpPDUsSent_Object=MibTableColumn
dot1qFutureVlanTunnelGvrpPDUsSent=_Dot1qFutureVlanTunnelGvrpPDUsSent_Object((1,3,6,1,4,1,2076,65,2,4,1,6),_Dot1qFutureVlanTunnelGvrpPDUsSent_Type())
dot1qFutureVlanTunnelGvrpPDUsSent.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureVlanTunnelGvrpPDUsSent.setStatus(_F)
class _Dot1qFutureVlanTunnelIgmpPkts_Type(EnabledStatus):defaultValue=1
_Dot1qFutureVlanTunnelIgmpPkts_Type.__name__=_G
_Dot1qFutureVlanTunnelIgmpPkts_Object=MibTableColumn
dot1qFutureVlanTunnelIgmpPkts=_Dot1qFutureVlanTunnelIgmpPkts_Object((1,3,6,1,4,1,2076,65,2,4,1,7),_Dot1qFutureVlanTunnelIgmpPkts_Type())
dot1qFutureVlanTunnelIgmpPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qFutureVlanTunnelIgmpPkts.setStatus(_F)
_Dot1qFutureVlanTunnelIgmpPktsRecvd_Type=Counter32
_Dot1qFutureVlanTunnelIgmpPktsRecvd_Object=MibTableColumn
dot1qFutureVlanTunnelIgmpPktsRecvd=_Dot1qFutureVlanTunnelIgmpPktsRecvd_Object((1,3,6,1,4,1,2076,65,2,4,1,8),_Dot1qFutureVlanTunnelIgmpPktsRecvd_Type())
dot1qFutureVlanTunnelIgmpPktsRecvd.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureVlanTunnelIgmpPktsRecvd.setStatus(_F)
_Dot1qFutureVlanTunnelIgmpPktsSent_Type=Counter32
_Dot1qFutureVlanTunnelIgmpPktsSent_Object=MibTableColumn
dot1qFutureVlanTunnelIgmpPktsSent=_Dot1qFutureVlanTunnelIgmpPktsSent_Object((1,3,6,1,4,1,2076,65,2,4,1,9),_Dot1qFutureVlanTunnelIgmpPktsSent_Type())
dot1qFutureVlanTunnelIgmpPktsSent.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1qFutureVlanTunnelIgmpPktsSent.setStatus(_F)
_Dot1qFutureVlanTraps_ObjectIdentity=ObjectIdentity
dot1qFutureVlanTraps=_Dot1qFutureVlanTraps_ObjectIdentity((1,3,6,1,4,1,2076,65,3))
_Dot1qVlanTraps_ObjectIdentity=ObjectIdentity
dot1qVlanTraps=_Dot1qVlanTraps_ObjectIdentity((1,3,6,1,4,1,2076,65,3,0))
dot1qTpFdbEntry.registerAugmentions((_E,_a))
dot1qFutureVlanTpFdbEntry.setIndexNames(*dot1qTpFdbEntry.getIndexNames())
dot1qStaticUnicastEntry.registerAugmentions((_E,_b))
dot1qFutureStaticUnicastExtnEntry.setIndexNames(*dot1qStaticUnicastEntry.getIndexNames())
dot1qVlanStaticEntry.registerAugmentions((_E,_c))
dot1qFutureStVlanExtEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())
dot1qFutureMacThresholdTrap=NotificationType((1,3,6,1,4,1,2076,65,3,0,1))
dot1qFutureMacThresholdTrap.setObjects(*((_E,_K),(_E,_d)))
if mibBuilder.loadTexts:dot1qFutureMacThresholdTrap.setStatus(_A)
dot1qFutureSrcRelearnTrap=NotificationType((1,3,6,1,4,1,2076,65,3,0,2))
dot1qFutureSrcRelearnTrap.setObjects(*((_E,_e),(_O,_Q),(_E,_f)))
if mibBuilder.loadTexts:dot1qFutureSrcRelearnTrap.setStatus(_A)
dot1qFutureSwitchMacLimitTrap=NotificationType((1,3,6,1,4,1,2076,65,3,0,3))
dot1qFutureSwitchMacLimitTrap.setObjects((_E,_g))
if mibBuilder.loadTexts:dot1qFutureSwitchMacLimitTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'VlanId':VlanId,_G:EnabledStatus,_V:MacLearningStatus,'futureVlanMIB':futureVlanMIB,'dot1qFutureVlan':dot1qFutureVlan,'dot1qFutureVlanStatus':dot1qFutureVlanStatus,'dot1qFutureVlanMacBasedOnAllPorts':dot1qFutureVlanMacBasedOnAllPorts,'dot1qFutureVlanPortProtoBasedOnAllPorts':dot1qFutureVlanPortProtoBasedOnAllPorts,'dot1qFutureVlanShutdownStatus':dot1qFutureVlanShutdownStatus,'dot1qFutureGarpShutdownStatus':dot1qFutureGarpShutdownStatus,'dot1qFutureVlanDebug':dot1qFutureVlanDebug,'dot1qFutureVlanLearningMode':dot1qFutureVlanLearningMode,'dot1qFutureVlanHybridTypeDefault':dot1qFutureVlanHybridTypeDefault,'dot1qFutureVlanPortTable':dot1qFutureVlanPortTable,'dot1qFutureVlanPortEntry':dot1qFutureVlanPortEntry,_I:dot1qFutureVlanPort,'dot1qFutureVlanPortType':dot1qFutureVlanPortType,'dot1qFutureVlanPortMacBasedClassification':dot1qFutureVlanPortMacBasedClassification,'dot1qFutureVlanPortPortProtoBasedClassification':dot1qFutureVlanPortPortProtoBasedClassification,'dot1qFutureVlanFilteringUtilityCriteria':dot1qFutureVlanFilteringUtilityCriteria,'dot1qFutureVlanPortProtected':dot1qFutureVlanPortProtected,'dot1qFutureVlanPortSubnetBasedClassification':dot1qFutureVlanPortSubnetBasedClassification,'dot1qFutureVlanPortUnicastMacLearning':dot1qFutureVlanPortUnicastMacLearning,'dot1qFutureVlanPortIngressEtherType':dot1qFutureVlanPortIngressEtherType,'dot1qFutureVlanPortEgressEtherType':dot1qFutureVlanPortEgressEtherType,'dot1qFutureVlanPortEgressTPIDType':dot1qFutureVlanPortEgressTPIDType,'dot1qFutureVlanPortAllowableTPID1':dot1qFutureVlanPortAllowableTPID1,'dot1qFutureVlanPortAllowableTPID2':dot1qFutureVlanPortAllowableTPID2,'dot1qFutureVlanPortAllowableTPID3':dot1qFutureVlanPortAllowableTPID3,'dot1qFutureVlanPortUnicastMacSecType':dot1qFutureVlanPortUnicastMacSecType,'dot1qFuturePortPacketReflectionStatus':dot1qFuturePortPacketReflectionStatus,'dot1qFutureVlanPortMacMapTable':dot1qFutureVlanPortMacMapTable,'dot1qFutureVlanPortMacMapEntry':dot1qFutureVlanPortMacMapEntry,_U:dot1qFutureVlanPortMacMapAddr,'dot1qFutureVlanPortMacMapVid':dot1qFutureVlanPortMacMapVid,'dot1qFutureVlanPortMacMapName':dot1qFutureVlanPortMacMapName,'dot1qFutureVlanPortMacMapMcastBcastOption':dot1qFutureVlanPortMacMapMcastBcastOption,'dot1qFutureVlanPortMacMapRowStatus':dot1qFutureVlanPortMacMapRowStatus,'dot1qFutureVlanFidMapTable':dot1qFutureVlanFidMapTable,'dot1qFutureVlanFidMapEntry':dot1qFutureVlanFidMapEntry,_K:dot1qFutureVlanIndex,_e:dot1qFutureVlanFid,'dot1qFutureVlanOperStatus':dot1qFutureVlanOperStatus,'dot1qFutureGvrpOperStatus':dot1qFutureGvrpOperStatus,'dot1qFutureGmrpOperStatus':dot1qFutureGmrpOperStatus,'dot1qFutureVlanCounterTable':dot1qFutureVlanCounterTable,'dot1qFutureVlanCounterEntry':dot1qFutureVlanCounterEntry,'dot1qFutureVlanCounterRxUcast':dot1qFutureVlanCounterRxUcast,'dot1qFutureVlanCounterRxMcastBcast':dot1qFutureVlanCounterRxMcastBcast,'dot1qFutureVlanCounterTxUnknUcast':dot1qFutureVlanCounterTxUnknUcast,'dot1qFutureVlanCounterTxUcast':dot1qFutureVlanCounterTxUcast,'dot1qFutureVlanCounterTxBcast':dot1qFutureVlanCounterTxBcast,'dot1qFutureVlanCounterRxFrames':dot1qFutureVlanCounterRxFrames,'dot1qFutureVlanCounterRxBytes':dot1qFutureVlanCounterRxBytes,'dot1qFutureVlanCounterTxFrames':dot1qFutureVlanCounterTxFrames,'dot1qFutureVlanCounterTxBytes':dot1qFutureVlanCounterTxBytes,'dot1qFutureVlanCounterDiscardFrames':dot1qFutureVlanCounterDiscardFrames,'dot1qFutureVlanCounterDiscardBytes':dot1qFutureVlanCounterDiscardBytes,'dot1qFutureVlanCounterStatus':dot1qFutureVlanCounterStatus,'dot1qFutureVlanUnicastMacControlTable':dot1qFutureVlanUnicastMacControlTable,'dot1qFutureVlanUnicastMacControlEntry':dot1qFutureVlanUnicastMacControlEntry,_d:dot1qFutureVlanUnicastMacLimit,'dot1qFutureVlanAdminMacLearningStatus':dot1qFutureVlanAdminMacLearningStatus,'dot1qFutureVlanOperMacLearningStatus':dot1qFutureVlanOperMacLearningStatus,'dot1qFutureVlanPortFdbFlush':dot1qFutureVlanPortFdbFlush,'dot1qFutureGarpDebug':dot1qFutureGarpDebug,'dot1qFutureVlanTpFdbTable':dot1qFutureVlanTpFdbTable,_a:dot1qFutureVlanTpFdbEntry,'dot1qFutureVlanTpFdbPw':dot1qFutureVlanTpFdbPw,_f:dot1qTpOldFdbPort,'dot1qFutureConnectionIdentifier':dot1qFutureConnectionIdentifier,'dot1qFutureVlanWildCardTable':dot1qFutureVlanWildCardTable,'dot1qFutureVlanWildCardEntry':dot1qFutureVlanWildCardEntry,_W:dot1qFutureVlanWildCardMacAddress,'dot1qFutureVlanWildCardEgressPorts':dot1qFutureVlanWildCardEgressPorts,'dot1qFutureVlanWildCardRowStatus':dot1qFutureVlanWildCardRowStatus,'dot1qFutureStaticUnicastExtnTable':dot1qFutureStaticUnicastExtnTable,_b:dot1qFutureStaticUnicastExtnEntry,'dot1qFutureStaticConnectionIdentifier':dot1qFutureStaticConnectionIdentifier,_g:dot1qFutureUnicastMacLearningLimit,'dot1qFutureVlanBaseBridgeMode':dot1qFutureVlanBaseBridgeMode,'dot1qFutureVlanSubnetBasedOnAllPorts':dot1qFutureVlanSubnetBasedOnAllPorts,'dot1qFutureVlanPortSubnetMapTable':dot1qFutureVlanPortSubnetMapTable,'dot1qFutureVlanPortSubnetMapEntry':dot1qFutureVlanPortSubnetMapEntry,_X:dot1qFutureVlanPortSubnetMapAddr,'dot1qFutureVlanPortSubnetMapVid':dot1qFutureVlanPortSubnetMapVid,'dot1qFutureVlanPortSubnetMapARPOption':dot1qFutureVlanPortSubnetMapARPOption,'dot1qFutureVlanPortSubnetMapRowStatus':dot1qFutureVlanPortSubnetMapRowStatus,'dot1qFutureVlanGlobalMacLearningStatus':dot1qFutureVlanGlobalMacLearningStatus,'dot1qFutureVlanApplyEnhancedFilteringCriteria':dot1qFutureVlanApplyEnhancedFilteringCriteria,'dot1qFutureVlanSwStatsEnabled':dot1qFutureVlanSwStatsEnabled,'dot1qFutureStVlanExtTable':dot1qFutureStVlanExtTable,_c:dot1qFutureStVlanExtEntry,'dot1qFutureStVlanPVlanType':dot1qFutureStVlanPVlanType,'dot1qFutureStVlanPrimaryVid':dot1qFutureStVlanPrimaryVid,'dot1qFutureStVlanEgressEthertype':dot1qFutureStVlanEgressEthertype,'dot1qFutureVlanPortSubnetMapExtTable':dot1qFutureVlanPortSubnetMapExtTable,'dot1qFutureVlanPortSubnetMapExtEntry':dot1qFutureVlanPortSubnetMapExtEntry,_Y:dot1qFutureVlanPortSubnetMapExtAddr,_Z:dot1qFutureVlanPortSubnetMapExtMask,'dot1qFutureVlanPortSubnetMapExtVid':dot1qFutureVlanPortSubnetMapExtVid,'dot1qFutureVlanPortSubnetMapExtARPOption':dot1qFutureVlanPortSubnetMapExtARPOption,'dot1qFutureVlanPortSubnetMapExtRowStatus':dot1qFutureVlanPortSubnetMapExtRowStatus,'dot1qFutureVlanGlobalsFdbFlush':dot1qFutureVlanGlobalsFdbFlush,'dot1qFutureVlanUserDefinedTPID':dot1qFutureVlanUserDefinedTPID,'dot1qFutureVlanLoopbackTable':dot1qFutureVlanLoopbackTable,'dot1qFutureVlanLoopbackEntry':dot1qFutureVlanLoopbackEntry,'dot1qFutureVlanLoopbackStatus':dot1qFutureVlanLoopbackStatus,'dot1qFutureVlanTunnelConfig':dot1qFutureVlanTunnelConfig,'dot1qFutureVlanBridgeMode':dot1qFutureVlanBridgeMode,'dot1qFutureVlanTunnelBpduPri':dot1qFutureVlanTunnelBpduPri,'dot1qFutureVlanTunnelTable':dot1qFutureVlanTunnelTable,'dot1qFutureVlanTunnelEntry':dot1qFutureVlanTunnelEntry,'dot1qFutureVlanTunnelStatus':dot1qFutureVlanTunnelStatus,'dot1qFutureVlanTunnelProtocolTable':dot1qFutureVlanTunnelProtocolTable,'dot1qFutureVlanTunnelProtocolEntry':dot1qFutureVlanTunnelProtocolEntry,'dot1qFutureVlanTunnelStpPDUs':dot1qFutureVlanTunnelStpPDUs,'dot1qFutureVlanTunnelStpPDUsRecvd':dot1qFutureVlanTunnelStpPDUsRecvd,'dot1qFutureVlanTunnelStpPDUsSent':dot1qFutureVlanTunnelStpPDUsSent,'dot1qFutureVlanTunnelGvrpPDUs':dot1qFutureVlanTunnelGvrpPDUs,'dot1qFutureVlanTunnelGvrpPDUsRecvd':dot1qFutureVlanTunnelGvrpPDUsRecvd,'dot1qFutureVlanTunnelGvrpPDUsSent':dot1qFutureVlanTunnelGvrpPDUsSent,'dot1qFutureVlanTunnelIgmpPkts':dot1qFutureVlanTunnelIgmpPkts,'dot1qFutureVlanTunnelIgmpPktsRecvd':dot1qFutureVlanTunnelIgmpPktsRecvd,'dot1qFutureVlanTunnelIgmpPktsSent':dot1qFutureVlanTunnelIgmpPktsSent,'dot1qFutureVlanTraps':dot1qFutureVlanTraps,'dot1qVlanTraps':dot1qVlanTraps,'dot1qFutureMacThresholdTrap':dot1qFutureMacThresholdTrap,'dot1qFutureSrcRelearnTrap':dot1qFutureSrcRelearnTrap,'dot1qFutureSwitchMacLimitTrap':dot1qFutureSwitchMacLimitTrap})