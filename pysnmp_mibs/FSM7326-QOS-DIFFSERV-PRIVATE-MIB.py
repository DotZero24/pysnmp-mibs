_Z='agentDiffServServicePerfEntry'
_Y='agentDiffServServiceIfDirection'
_X='agentDiffServServiceIfIndex'
_W='QosBurstSize'
_V='percentage'
_U='agentDiffServPolicyAttrIndex'
_T='agentDiffServClassRuleIndex'
_S='send'
_R='markprec'
_Q='markdscp'
_P='drop'
_O='agentDiffServClassIndex'
_N='DisplayString'
_M='ifIndex'
_L='IF-MIB'
_K='OctetString'
_J='agentDiffServPolicyInstIndex'
_I='agentDiffServPolicyIndex'
_H='not-accessible'
_G='StorageType'
_F='Integer32'
_E='FSM7326-QOS-DIFFSERV-PRIVATE-MIB'
_D='Unsigned32'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsm7326QOS,=mibBuilder.importSymbols('FSM7326-QOS-MIB','fsm7326QOS')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_L,'InterfaceIndex',_M)
InetPortNumber,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetPortNumber')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,RowPointer,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_N,'MacAddress','PhysAddress','RowPointer','RowStatus',_G,'TextualConvention','TruthValue')
fsm7326QOSDiffServPrivate=ModuleIdentity((1,3,6,1,4,1,4526,1,9,3,4))
if mibBuilder.loadTexts:fsm7326QOSDiffServPrivate.setRevisions(('2003-11-10 12:00',))
class QosBurstSize(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
class IntfDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
_AgentDiffServGenStatusGroup_ObjectIdentity=ObjectIdentity
agentDiffServGenStatusGroup=_AgentDiffServGenStatusGroup_ObjectIdentity((1,3,6,1,4,1,4526,1,9,3,4,1))
class _AgentDiffServGenStatusAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AgentDiffServGenStatusAdminMode_Type.__name__=_F
_AgentDiffServGenStatusAdminMode_Object=MibScalar
agentDiffServGenStatusAdminMode=_AgentDiffServGenStatusAdminMode_Object((1,3,6,1,4,1,4526,1,9,3,4,1,1),_AgentDiffServGenStatusAdminMode_Type())
agentDiffServGenStatusAdminMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:agentDiffServGenStatusAdminMode.setStatus(_A)
_AgentDiffServGenStatusClassTableSize_Type=Unsigned32
_AgentDiffServGenStatusClassTableSize_Object=MibScalar
agentDiffServGenStatusClassTableSize=_AgentDiffServGenStatusClassTableSize_Object((1,3,6,1,4,1,4526,1,9,3,4,1,2),_AgentDiffServGenStatusClassTableSize_Type())
agentDiffServGenStatusClassTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServGenStatusClassTableSize.setStatus(_A)
_AgentDiffServGenStatusClassTableMax_Type=Unsigned32
_AgentDiffServGenStatusClassTableMax_Object=MibScalar
agentDiffServGenStatusClassTableMax=_AgentDiffServGenStatusClassTableMax_Object((1,3,6,1,4,1,4526,1,9,3,4,1,3),_AgentDiffServGenStatusClassTableMax_Type())
agentDiffServGenStatusClassTableMax.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServGenStatusClassTableMax.setStatus(_A)
_AgentDiffServGenStatusClassRuleTableSize_Type=Unsigned32
_AgentDiffServGenStatusClassRuleTableSize_Object=MibScalar
agentDiffServGenStatusClassRuleTableSize=_AgentDiffServGenStatusClassRuleTableSize_Object((1,3,6,1,4,1,4526,1,9,3,4,1,4),_AgentDiffServGenStatusClassRuleTableSize_Type())
agentDiffServGenStatusClassRuleTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServGenStatusClassRuleTableSize.setStatus(_A)
_AgentDiffServGenStatusClassRuleTableMax_Type=Unsigned32
_AgentDiffServGenStatusClassRuleTableMax_Object=MibScalar
agentDiffServGenStatusClassRuleTableMax=_AgentDiffServGenStatusClassRuleTableMax_Object((1,3,6,1,4,1,4526,1,9,3,4,1,5),_AgentDiffServGenStatusClassRuleTableMax_Type())
agentDiffServGenStatusClassRuleTableMax.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServGenStatusClassRuleTableMax.setStatus(_A)
_AgentDiffServGenStatusPolicyTableSize_Type=Unsigned32
_AgentDiffServGenStatusPolicyTableSize_Object=MibScalar
agentDiffServGenStatusPolicyTableSize=_AgentDiffServGenStatusPolicyTableSize_Object((1,3,6,1,4,1,4526,1,9,3,4,1,6),_AgentDiffServGenStatusPolicyTableSize_Type())
agentDiffServGenStatusPolicyTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServGenStatusPolicyTableSize.setStatus(_A)
_AgentDiffServGenStatusPolicyTableMax_Type=Unsigned32
_AgentDiffServGenStatusPolicyTableMax_Object=MibScalar
agentDiffServGenStatusPolicyTableMax=_AgentDiffServGenStatusPolicyTableMax_Object((1,3,6,1,4,1,4526,1,9,3,4,1,7),_AgentDiffServGenStatusPolicyTableMax_Type())
agentDiffServGenStatusPolicyTableMax.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServGenStatusPolicyTableMax.setStatus(_A)
_AgentDiffServGenStatusPolicyInstTableSize_Type=Unsigned32
_AgentDiffServGenStatusPolicyInstTableSize_Object=MibScalar
agentDiffServGenStatusPolicyInstTableSize=_AgentDiffServGenStatusPolicyInstTableSize_Object((1,3,6,1,4,1,4526,1,9,3,4,1,8),_AgentDiffServGenStatusPolicyInstTableSize_Type())
agentDiffServGenStatusPolicyInstTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServGenStatusPolicyInstTableSize.setStatus(_A)
_AgentDiffServGenStatusPolicyInstTableMax_Type=Unsigned32
_AgentDiffServGenStatusPolicyInstTableMax_Object=MibScalar
agentDiffServGenStatusPolicyInstTableMax=_AgentDiffServGenStatusPolicyInstTableMax_Object((1,3,6,1,4,1,4526,1,9,3,4,1,9),_AgentDiffServGenStatusPolicyInstTableMax_Type())
agentDiffServGenStatusPolicyInstTableMax.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServGenStatusPolicyInstTableMax.setStatus(_A)
_AgentDiffServGenStatusPolicyAttrTableSize_Type=Unsigned32
_AgentDiffServGenStatusPolicyAttrTableSize_Object=MibScalar
agentDiffServGenStatusPolicyAttrTableSize=_AgentDiffServGenStatusPolicyAttrTableSize_Object((1,3,6,1,4,1,4526,1,9,3,4,1,10),_AgentDiffServGenStatusPolicyAttrTableSize_Type())
agentDiffServGenStatusPolicyAttrTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServGenStatusPolicyAttrTableSize.setStatus(_A)
_AgentDiffServGenStatusPolicyAttrTableMax_Type=Unsigned32
_AgentDiffServGenStatusPolicyAttrTableMax_Object=MibScalar
agentDiffServGenStatusPolicyAttrTableMax=_AgentDiffServGenStatusPolicyAttrTableMax_Object((1,3,6,1,4,1,4526,1,9,3,4,1,11),_AgentDiffServGenStatusPolicyAttrTableMax_Type())
agentDiffServGenStatusPolicyAttrTableMax.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServGenStatusPolicyAttrTableMax.setStatus(_A)
_AgentDiffServGenStatusServiceTableSize_Type=Unsigned32
_AgentDiffServGenStatusServiceTableSize_Object=MibScalar
agentDiffServGenStatusServiceTableSize=_AgentDiffServGenStatusServiceTableSize_Object((1,3,6,1,4,1,4526,1,9,3,4,1,12),_AgentDiffServGenStatusServiceTableSize_Type())
agentDiffServGenStatusServiceTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServGenStatusServiceTableSize.setStatus(_A)
_AgentDiffServGenStatusServiceTableMax_Type=Unsigned32
_AgentDiffServGenStatusServiceTableMax_Object=MibScalar
agentDiffServGenStatusServiceTableMax=_AgentDiffServGenStatusServiceTableMax_Object((1,3,6,1,4,1,4526,1,9,3,4,1,13),_AgentDiffServGenStatusServiceTableMax_Type())
agentDiffServGenStatusServiceTableMax.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServGenStatusServiceTableMax.setStatus(_A)
_AgentDiffServClassGroup_ObjectIdentity=ObjectIdentity
agentDiffServClassGroup=_AgentDiffServClassGroup_ObjectIdentity((1,3,6,1,4,1,4526,1,9,3,4,2))
_AgentDiffServClassIndexNextFree_Type=Unsigned32
_AgentDiffServClassIndexNextFree_Object=MibScalar
agentDiffServClassIndexNextFree=_AgentDiffServClassIndexNextFree_Object((1,3,6,1,4,1,4526,1,9,3,4,2,1),_AgentDiffServClassIndexNextFree_Type())
agentDiffServClassIndexNextFree.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServClassIndexNextFree.setStatus(_A)
_AgentDiffServClassTable_Object=MibTable
agentDiffServClassTable=_AgentDiffServClassTable_Object((1,3,6,1,4,1,4526,1,9,3,4,2,2))
if mibBuilder.loadTexts:agentDiffServClassTable.setStatus(_A)
_AgentDiffServClassEntry_Object=MibTableRow
agentDiffServClassEntry=_AgentDiffServClassEntry_Object((1,3,6,1,4,1,4526,1,9,3,4,2,2,1))
agentDiffServClassEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:agentDiffServClassEntry.setStatus(_A)
_AgentDiffServClassIndex_Type=Unsigned32
_AgentDiffServClassIndex_Object=MibTableColumn
agentDiffServClassIndex=_AgentDiffServClassIndex_Object((1,3,6,1,4,1,4526,1,9,3,4,2,2,1,1),_AgentDiffServClassIndex_Type())
agentDiffServClassIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:agentDiffServClassIndex.setStatus(_A)
class _AgentDiffServClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AgentDiffServClassName_Type.__name__=_N
_AgentDiffServClassName_Object=MibTableColumn
agentDiffServClassName=_AgentDiffServClassName_Object((1,3,6,1,4,1,4526,1,9,3,4,2,2,1,2),_AgentDiffServClassName_Type())
agentDiffServClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassName.setStatus(_A)
class _AgentDiffServClassType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('all',1),('any',2),('acl',3)))
_AgentDiffServClassType_Type.__name__=_F
_AgentDiffServClassType_Object=MibTableColumn
agentDiffServClassType=_AgentDiffServClassType_Object((1,3,6,1,4,1,4526,1,9,3,4,2,2,1,3),_AgentDiffServClassType_Type())
agentDiffServClassType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassType.setStatus(_A)
_AgentDiffServClassAclNum_Type=Unsigned32
_AgentDiffServClassAclNum_Object=MibTableColumn
agentDiffServClassAclNum=_AgentDiffServClassAclNum_Object((1,3,6,1,4,1,4526,1,9,3,4,2,2,1,4),_AgentDiffServClassAclNum_Type())
agentDiffServClassAclNum.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassAclNum.setStatus(_A)
_AgentDiffServClassRuleIndexNextFree_Type=Unsigned32
_AgentDiffServClassRuleIndexNextFree_Object=MibTableColumn
agentDiffServClassRuleIndexNextFree=_AgentDiffServClassRuleIndexNextFree_Object((1,3,6,1,4,1,4526,1,9,3,4,2,2,1,5),_AgentDiffServClassRuleIndexNextFree_Type())
agentDiffServClassRuleIndexNextFree.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServClassRuleIndexNextFree.setStatus(_A)
class _AgentDiffServClassStorageType_Type(StorageType):defaultValue=3
_AgentDiffServClassStorageType_Type.__name__=_G
_AgentDiffServClassStorageType_Object=MibTableColumn
agentDiffServClassStorageType=_AgentDiffServClassStorageType_Object((1,3,6,1,4,1,4526,1,9,3,4,2,2,1,6),_AgentDiffServClassStorageType_Type())
agentDiffServClassStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassStorageType.setStatus(_A)
_AgentDiffServClassRowStatus_Type=RowStatus
_AgentDiffServClassRowStatus_Object=MibTableColumn
agentDiffServClassRowStatus=_AgentDiffServClassRowStatus_Object((1,3,6,1,4,1,4526,1,9,3,4,2,2,1,7),_AgentDiffServClassRowStatus_Type())
agentDiffServClassRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRowStatus.setStatus(_A)
_AgentDiffServClassRuleTable_Object=MibTable
agentDiffServClassRuleTable=_AgentDiffServClassRuleTable_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3))
if mibBuilder.loadTexts:agentDiffServClassRuleTable.setStatus(_A)
_AgentDiffServClassRuleEntry_Object=MibTableRow
agentDiffServClassRuleEntry=_AgentDiffServClassRuleEntry_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1))
agentDiffServClassRuleEntry.setIndexNames((0,_E,_O),(0,_E,_T))
if mibBuilder.loadTexts:agentDiffServClassRuleEntry.setStatus(_A)
_AgentDiffServClassRuleIndex_Type=Unsigned32
_AgentDiffServClassRuleIndex_Object=MibTableColumn
agentDiffServClassRuleIndex=_AgentDiffServClassRuleIndex_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,1),_AgentDiffServClassRuleIndex_Type())
agentDiffServClassRuleIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:agentDiffServClassRuleIndex.setStatus(_A)
class _AgentDiffServClassRuleMatchEntryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('cos',1),('dstip',2),('dstl4port',3),('dstmac',4),('every',5),('ipdscp',6),('ipprecedence',7),('iptos',8),('protocol',9),('refclass',10),('srcip',11),('srcl4port',12),('srcmac',13),('vlan',14)))
_AgentDiffServClassRuleMatchEntryType_Type.__name__=_F
_AgentDiffServClassRuleMatchEntryType_Object=MibTableColumn
agentDiffServClassRuleMatchEntryType=_AgentDiffServClassRuleMatchEntryType_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,2),_AgentDiffServClassRuleMatchEntryType_Type())
agentDiffServClassRuleMatchEntryType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchEntryType.setStatus(_A)
class _AgentDiffServClassRuleMatchCos_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AgentDiffServClassRuleMatchCos_Type.__name__=_D
_AgentDiffServClassRuleMatchCos_Object=MibTableColumn
agentDiffServClassRuleMatchCos=_AgentDiffServClassRuleMatchCos_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,3),_AgentDiffServClassRuleMatchCos_Type())
agentDiffServClassRuleMatchCos.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchCos.setStatus(_A)
_AgentDiffServClassRuleMatchDstIpAddr_Type=IpAddress
_AgentDiffServClassRuleMatchDstIpAddr_Object=MibTableColumn
agentDiffServClassRuleMatchDstIpAddr=_AgentDiffServClassRuleMatchDstIpAddr_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,4),_AgentDiffServClassRuleMatchDstIpAddr_Type())
agentDiffServClassRuleMatchDstIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchDstIpAddr.setStatus(_A)
_AgentDiffServClassRuleMatchDstIpMask_Type=IpAddress
_AgentDiffServClassRuleMatchDstIpMask_Object=MibTableColumn
agentDiffServClassRuleMatchDstIpMask=_AgentDiffServClassRuleMatchDstIpMask_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,5),_AgentDiffServClassRuleMatchDstIpMask_Type())
agentDiffServClassRuleMatchDstIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchDstIpMask.setStatus(_A)
_AgentDiffServClassRuleMatchDstL4PortStart_Type=InetPortNumber
_AgentDiffServClassRuleMatchDstL4PortStart_Object=MibTableColumn
agentDiffServClassRuleMatchDstL4PortStart=_AgentDiffServClassRuleMatchDstL4PortStart_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,6),_AgentDiffServClassRuleMatchDstL4PortStart_Type())
agentDiffServClassRuleMatchDstL4PortStart.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchDstL4PortStart.setStatus(_A)
_AgentDiffServClassRuleMatchDstL4PortEnd_Type=InetPortNumber
_AgentDiffServClassRuleMatchDstL4PortEnd_Object=MibTableColumn
agentDiffServClassRuleMatchDstL4PortEnd=_AgentDiffServClassRuleMatchDstL4PortEnd_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,7),_AgentDiffServClassRuleMatchDstL4PortEnd_Type())
agentDiffServClassRuleMatchDstL4PortEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchDstL4PortEnd.setStatus(_A)
_AgentDiffServClassRuleMatchDstMacAddr_Type=MacAddress
_AgentDiffServClassRuleMatchDstMacAddr_Object=MibTableColumn
agentDiffServClassRuleMatchDstMacAddr=_AgentDiffServClassRuleMatchDstMacAddr_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,8),_AgentDiffServClassRuleMatchDstMacAddr_Type())
agentDiffServClassRuleMatchDstMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchDstMacAddr.setStatus(_A)
_AgentDiffServClassRuleMatchDstMacMask_Type=MacAddress
_AgentDiffServClassRuleMatchDstMacMask_Object=MibTableColumn
agentDiffServClassRuleMatchDstMacMask=_AgentDiffServClassRuleMatchDstMacMask_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,9),_AgentDiffServClassRuleMatchDstMacMask_Type())
agentDiffServClassRuleMatchDstMacMask.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchDstMacMask.setStatus(_A)
_AgentDiffServClassRuleMatchEvery_Type=TruthValue
_AgentDiffServClassRuleMatchEvery_Object=MibTableColumn
agentDiffServClassRuleMatchEvery=_AgentDiffServClassRuleMatchEvery_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,10),_AgentDiffServClassRuleMatchEvery_Type())
agentDiffServClassRuleMatchEvery.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchEvery.setStatus(_A)
class _AgentDiffServClassRuleMatchIpDscp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AgentDiffServClassRuleMatchIpDscp_Type.__name__=_D
_AgentDiffServClassRuleMatchIpDscp_Object=MibTableColumn
agentDiffServClassRuleMatchIpDscp=_AgentDiffServClassRuleMatchIpDscp_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,11),_AgentDiffServClassRuleMatchIpDscp_Type())
agentDiffServClassRuleMatchIpDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchIpDscp.setStatus(_A)
class _AgentDiffServClassRuleMatchIpPrecedence_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AgentDiffServClassRuleMatchIpPrecedence_Type.__name__=_D
_AgentDiffServClassRuleMatchIpPrecedence_Object=MibTableColumn
agentDiffServClassRuleMatchIpPrecedence=_AgentDiffServClassRuleMatchIpPrecedence_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,12),_AgentDiffServClassRuleMatchIpPrecedence_Type())
agentDiffServClassRuleMatchIpPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchIpPrecedence.setStatus(_A)
class _AgentDiffServClassRuleMatchIpTosBits_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_AgentDiffServClassRuleMatchIpTosBits_Type.__name__=_K
_AgentDiffServClassRuleMatchIpTosBits_Object=MibTableColumn
agentDiffServClassRuleMatchIpTosBits=_AgentDiffServClassRuleMatchIpTosBits_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,13),_AgentDiffServClassRuleMatchIpTosBits_Type())
agentDiffServClassRuleMatchIpTosBits.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchIpTosBits.setStatus(_A)
class _AgentDiffServClassRuleMatchIpTosMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_AgentDiffServClassRuleMatchIpTosMask_Type.__name__=_K
_AgentDiffServClassRuleMatchIpTosMask_Object=MibTableColumn
agentDiffServClassRuleMatchIpTosMask=_AgentDiffServClassRuleMatchIpTosMask_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,14),_AgentDiffServClassRuleMatchIpTosMask_Type())
agentDiffServClassRuleMatchIpTosMask.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchIpTosMask.setStatus(_A)
class _AgentDiffServClassRuleMatchProtocolNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentDiffServClassRuleMatchProtocolNum_Type.__name__=_D
_AgentDiffServClassRuleMatchProtocolNum_Object=MibTableColumn
agentDiffServClassRuleMatchProtocolNum=_AgentDiffServClassRuleMatchProtocolNum_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,15),_AgentDiffServClassRuleMatchProtocolNum_Type())
agentDiffServClassRuleMatchProtocolNum.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchProtocolNum.setStatus(_A)
_AgentDiffServClassRuleMatchRefClassIndex_Type=Unsigned32
_AgentDiffServClassRuleMatchRefClassIndex_Object=MibTableColumn
agentDiffServClassRuleMatchRefClassIndex=_AgentDiffServClassRuleMatchRefClassIndex_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,16),_AgentDiffServClassRuleMatchRefClassIndex_Type())
agentDiffServClassRuleMatchRefClassIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchRefClassIndex.setStatus(_A)
_AgentDiffServClassRuleMatchSrcIpAddr_Type=IpAddress
_AgentDiffServClassRuleMatchSrcIpAddr_Object=MibTableColumn
agentDiffServClassRuleMatchSrcIpAddr=_AgentDiffServClassRuleMatchSrcIpAddr_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,17),_AgentDiffServClassRuleMatchSrcIpAddr_Type())
agentDiffServClassRuleMatchSrcIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchSrcIpAddr.setStatus(_A)
_AgentDiffServClassRuleMatchSrcIpMask_Type=IpAddress
_AgentDiffServClassRuleMatchSrcIpMask_Object=MibTableColumn
agentDiffServClassRuleMatchSrcIpMask=_AgentDiffServClassRuleMatchSrcIpMask_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,18),_AgentDiffServClassRuleMatchSrcIpMask_Type())
agentDiffServClassRuleMatchSrcIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchSrcIpMask.setStatus(_A)
_AgentDiffServClassRuleMatchSrcL4PortStart_Type=InetPortNumber
_AgentDiffServClassRuleMatchSrcL4PortStart_Object=MibTableColumn
agentDiffServClassRuleMatchSrcL4PortStart=_AgentDiffServClassRuleMatchSrcL4PortStart_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,19),_AgentDiffServClassRuleMatchSrcL4PortStart_Type())
agentDiffServClassRuleMatchSrcL4PortStart.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchSrcL4PortStart.setStatus(_A)
_AgentDiffServClassRuleMatchSrcL4PortEnd_Type=InetPortNumber
_AgentDiffServClassRuleMatchSrcL4PortEnd_Object=MibTableColumn
agentDiffServClassRuleMatchSrcL4PortEnd=_AgentDiffServClassRuleMatchSrcL4PortEnd_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,20),_AgentDiffServClassRuleMatchSrcL4PortEnd_Type())
agentDiffServClassRuleMatchSrcL4PortEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchSrcL4PortEnd.setStatus(_A)
_AgentDiffServClassRuleMatchSrcMacAddr_Type=MacAddress
_AgentDiffServClassRuleMatchSrcMacAddr_Object=MibTableColumn
agentDiffServClassRuleMatchSrcMacAddr=_AgentDiffServClassRuleMatchSrcMacAddr_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,21),_AgentDiffServClassRuleMatchSrcMacAddr_Type())
agentDiffServClassRuleMatchSrcMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchSrcMacAddr.setStatus(_A)
_AgentDiffServClassRuleMatchSrcMacMask_Type=MacAddress
_AgentDiffServClassRuleMatchSrcMacMask_Object=MibTableColumn
agentDiffServClassRuleMatchSrcMacMask=_AgentDiffServClassRuleMatchSrcMacMask_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,22),_AgentDiffServClassRuleMatchSrcMacMask_Type())
agentDiffServClassRuleMatchSrcMacMask.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchSrcMacMask.setStatus(_A)
class _AgentDiffServClassRuleMatchVlanId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_AgentDiffServClassRuleMatchVlanId_Type.__name__=_D
_AgentDiffServClassRuleMatchVlanId_Object=MibTableColumn
agentDiffServClassRuleMatchVlanId=_AgentDiffServClassRuleMatchVlanId_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,23),_AgentDiffServClassRuleMatchVlanId_Type())
agentDiffServClassRuleMatchVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchVlanId.setStatus(_A)
_AgentDiffServClassRuleMatchExcludeFlag_Type=TruthValue
_AgentDiffServClassRuleMatchExcludeFlag_Object=MibTableColumn
agentDiffServClassRuleMatchExcludeFlag=_AgentDiffServClassRuleMatchExcludeFlag_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,24),_AgentDiffServClassRuleMatchExcludeFlag_Type())
agentDiffServClassRuleMatchExcludeFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleMatchExcludeFlag.setStatus(_A)
class _AgentDiffServClassRuleStorageType_Type(StorageType):defaultValue=3
_AgentDiffServClassRuleStorageType_Type.__name__=_G
_AgentDiffServClassRuleStorageType_Object=MibTableColumn
agentDiffServClassRuleStorageType=_AgentDiffServClassRuleStorageType_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,25),_AgentDiffServClassRuleStorageType_Type())
agentDiffServClassRuleStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleStorageType.setStatus(_A)
_AgentDiffServClassRuleRowStatus_Type=RowStatus
_AgentDiffServClassRuleRowStatus_Object=MibTableColumn
agentDiffServClassRuleRowStatus=_AgentDiffServClassRuleRowStatus_Object((1,3,6,1,4,1,4526,1,9,3,4,2,3,1,26),_AgentDiffServClassRuleRowStatus_Type())
agentDiffServClassRuleRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServClassRuleRowStatus.setStatus(_A)
_AgentDiffServPolicyGroup_ObjectIdentity=ObjectIdentity
agentDiffServPolicyGroup=_AgentDiffServPolicyGroup_ObjectIdentity((1,3,6,1,4,1,4526,1,9,3,4,3))
_AgentDiffServPolicyIndexNextFree_Type=Unsigned32
_AgentDiffServPolicyIndexNextFree_Object=MibScalar
agentDiffServPolicyIndexNextFree=_AgentDiffServPolicyIndexNextFree_Object((1,3,6,1,4,1,4526,1,9,3,4,3,1),_AgentDiffServPolicyIndexNextFree_Type())
agentDiffServPolicyIndexNextFree.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyIndexNextFree.setStatus(_A)
_AgentDiffServPolicyTable_Object=MibTable
agentDiffServPolicyTable=_AgentDiffServPolicyTable_Object((1,3,6,1,4,1,4526,1,9,3,4,3,2))
if mibBuilder.loadTexts:agentDiffServPolicyTable.setStatus(_A)
_AgentDiffServPolicyEntry_Object=MibTableRow
agentDiffServPolicyEntry=_AgentDiffServPolicyEntry_Object((1,3,6,1,4,1,4526,1,9,3,4,3,2,1))
agentDiffServPolicyEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:agentDiffServPolicyEntry.setStatus(_A)
_AgentDiffServPolicyIndex_Type=Unsigned32
_AgentDiffServPolicyIndex_Object=MibTableColumn
agentDiffServPolicyIndex=_AgentDiffServPolicyIndex_Object((1,3,6,1,4,1,4526,1,9,3,4,3,2,1,1),_AgentDiffServPolicyIndex_Type())
agentDiffServPolicyIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:agentDiffServPolicyIndex.setStatus(_A)
class _AgentDiffServPolicyName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AgentDiffServPolicyName_Type.__name__=_N
_AgentDiffServPolicyName_Object=MibTableColumn
agentDiffServPolicyName=_AgentDiffServPolicyName_Object((1,3,6,1,4,1,4526,1,9,3,4,3,2,1,2),_AgentDiffServPolicyName_Type())
agentDiffServPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyName.setStatus(_A)
_AgentDiffServPolicyType_Type=IntfDirection
_AgentDiffServPolicyType_Object=MibTableColumn
agentDiffServPolicyType=_AgentDiffServPolicyType_Object((1,3,6,1,4,1,4526,1,9,3,4,3,2,1,3),_AgentDiffServPolicyType_Type())
agentDiffServPolicyType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyType.setStatus(_A)
_AgentDiffServPolicyInstIndexNextFree_Type=Unsigned32
_AgentDiffServPolicyInstIndexNextFree_Object=MibTableColumn
agentDiffServPolicyInstIndexNextFree=_AgentDiffServPolicyInstIndexNextFree_Object((1,3,6,1,4,1,4526,1,9,3,4,3,2,1,4),_AgentDiffServPolicyInstIndexNextFree_Type())
agentDiffServPolicyInstIndexNextFree.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyInstIndexNextFree.setStatus(_A)
class _AgentDiffServPolicyStorageType_Type(StorageType):defaultValue=3
_AgentDiffServPolicyStorageType_Type.__name__=_G
_AgentDiffServPolicyStorageType_Object=MibTableColumn
agentDiffServPolicyStorageType=_AgentDiffServPolicyStorageType_Object((1,3,6,1,4,1,4526,1,9,3,4,3,2,1,5),_AgentDiffServPolicyStorageType_Type())
agentDiffServPolicyStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyStorageType.setStatus(_A)
_AgentDiffServPolicyRowStatus_Type=RowStatus
_AgentDiffServPolicyRowStatus_Object=MibTableColumn
agentDiffServPolicyRowStatus=_AgentDiffServPolicyRowStatus_Object((1,3,6,1,4,1,4526,1,9,3,4,3,2,1,6),_AgentDiffServPolicyRowStatus_Type())
agentDiffServPolicyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyRowStatus.setStatus(_A)
_AgentDiffServPolicyInstTable_Object=MibTable
agentDiffServPolicyInstTable=_AgentDiffServPolicyInstTable_Object((1,3,6,1,4,1,4526,1,9,3,4,3,3))
if mibBuilder.loadTexts:agentDiffServPolicyInstTable.setStatus(_A)
_AgentDiffServPolicyInstEntry_Object=MibTableRow
agentDiffServPolicyInstEntry=_AgentDiffServPolicyInstEntry_Object((1,3,6,1,4,1,4526,1,9,3,4,3,3,1))
agentDiffServPolicyInstEntry.setIndexNames((0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:agentDiffServPolicyInstEntry.setStatus(_A)
_AgentDiffServPolicyInstIndex_Type=Unsigned32
_AgentDiffServPolicyInstIndex_Object=MibTableColumn
agentDiffServPolicyInstIndex=_AgentDiffServPolicyInstIndex_Object((1,3,6,1,4,1,4526,1,9,3,4,3,3,1,1),_AgentDiffServPolicyInstIndex_Type())
agentDiffServPolicyInstIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:agentDiffServPolicyInstIndex.setStatus(_A)
_AgentDiffServPolicyInstClassIndex_Type=Unsigned32
_AgentDiffServPolicyInstClassIndex_Object=MibTableColumn
agentDiffServPolicyInstClassIndex=_AgentDiffServPolicyInstClassIndex_Object((1,3,6,1,4,1,4526,1,9,3,4,3,3,1,2),_AgentDiffServPolicyInstClassIndex_Type())
agentDiffServPolicyInstClassIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyInstClassIndex.setStatus(_A)
_AgentDiffServPolicyInstAttrIndexNextFree_Type=Unsigned32
_AgentDiffServPolicyInstAttrIndexNextFree_Object=MibTableColumn
agentDiffServPolicyInstAttrIndexNextFree=_AgentDiffServPolicyInstAttrIndexNextFree_Object((1,3,6,1,4,1,4526,1,9,3,4,3,3,1,3),_AgentDiffServPolicyInstAttrIndexNextFree_Type())
agentDiffServPolicyInstAttrIndexNextFree.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyInstAttrIndexNextFree.setStatus(_A)
class _AgentDiffServPolicyInstStorageType_Type(StorageType):defaultValue=3
_AgentDiffServPolicyInstStorageType_Type.__name__=_G
_AgentDiffServPolicyInstStorageType_Object=MibTableColumn
agentDiffServPolicyInstStorageType=_AgentDiffServPolicyInstStorageType_Object((1,3,6,1,4,1,4526,1,9,3,4,3,3,1,4),_AgentDiffServPolicyInstStorageType_Type())
agentDiffServPolicyInstStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyInstStorageType.setStatus(_A)
_AgentDiffServPolicyInstRowStatus_Type=RowStatus
_AgentDiffServPolicyInstRowStatus_Object=MibTableColumn
agentDiffServPolicyInstRowStatus=_AgentDiffServPolicyInstRowStatus_Object((1,3,6,1,4,1,4526,1,9,3,4,3,3,1,5),_AgentDiffServPolicyInstRowStatus_Type())
agentDiffServPolicyInstRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyInstRowStatus.setStatus(_A)
_AgentDiffServPolicyAttrTable_Object=MibTable
agentDiffServPolicyAttrTable=_AgentDiffServPolicyAttrTable_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4))
if mibBuilder.loadTexts:agentDiffServPolicyAttrTable.setStatus(_A)
_AgentDiffServPolicyAttrEntry_Object=MibTableRow
agentDiffServPolicyAttrEntry=_AgentDiffServPolicyAttrEntry_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1))
agentDiffServPolicyAttrEntry.setIndexNames((0,_E,_I),(0,_E,_J),(0,_E,_U))
if mibBuilder.loadTexts:agentDiffServPolicyAttrEntry.setStatus(_A)
_AgentDiffServPolicyAttrIndex_Type=Unsigned32
_AgentDiffServPolicyAttrIndex_Object=MibTableColumn
agentDiffServPolicyAttrIndex=_AgentDiffServPolicyAttrIndex_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,1),_AgentDiffServPolicyAttrIndex_Type())
agentDiffServPolicyAttrIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:agentDiffServPolicyAttrIndex.setStatus(_A)
class _AgentDiffServPolicyAttrStmtEntryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('bandwidth',1),('expedite',2),('markCosVal',3),('markIpDscpVal',4),('markIpPrecedenceVal',5),('policeSimple',6),('policeSinglerate',7),('policeTworate',8),('randomdrop',9),('shapeAverage',10),('shapePeak',11)))
_AgentDiffServPolicyAttrStmtEntryType_Type.__name__=_F
_AgentDiffServPolicyAttrStmtEntryType_Object=MibTableColumn
agentDiffServPolicyAttrStmtEntryType=_AgentDiffServPolicyAttrStmtEntryType_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,2),_AgentDiffServPolicyAttrStmtEntryType_Type())
agentDiffServPolicyAttrStmtEntryType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtEntryType.setStatus(_A)
_AgentDiffServPolicyAttrStmtBandwidthCrate_Type=Unsigned32
_AgentDiffServPolicyAttrStmtBandwidthCrate_Object=MibTableColumn
agentDiffServPolicyAttrStmtBandwidthCrate=_AgentDiffServPolicyAttrStmtBandwidthCrate_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,3),_AgentDiffServPolicyAttrStmtBandwidthCrate_Type())
agentDiffServPolicyAttrStmtBandwidthCrate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtBandwidthCrate.setStatus(_A)
class _AgentDiffServPolicyAttrStmtBandwidthCrateUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('kbps',1),(_V,2)))
_AgentDiffServPolicyAttrStmtBandwidthCrateUnits_Type.__name__=_F
_AgentDiffServPolicyAttrStmtBandwidthCrateUnits_Object=MibTableColumn
agentDiffServPolicyAttrStmtBandwidthCrateUnits=_AgentDiffServPolicyAttrStmtBandwidthCrateUnits_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,4),_AgentDiffServPolicyAttrStmtBandwidthCrateUnits_Type())
agentDiffServPolicyAttrStmtBandwidthCrateUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtBandwidthCrateUnits.setStatus(_A)
_AgentDiffServPolicyAttrStmtExpediteCrate_Type=Unsigned32
_AgentDiffServPolicyAttrStmtExpediteCrate_Object=MibTableColumn
agentDiffServPolicyAttrStmtExpediteCrate=_AgentDiffServPolicyAttrStmtExpediteCrate_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,5),_AgentDiffServPolicyAttrStmtExpediteCrate_Type())
agentDiffServPolicyAttrStmtExpediteCrate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtExpediteCrate.setStatus(_A)
class _AgentDiffServPolicyAttrStmtExpediteCrateUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('kbps',1),(_V,2)))
_AgentDiffServPolicyAttrStmtExpediteCrateUnits_Type.__name__=_F
_AgentDiffServPolicyAttrStmtExpediteCrateUnits_Object=MibTableColumn
agentDiffServPolicyAttrStmtExpediteCrateUnits=_AgentDiffServPolicyAttrStmtExpediteCrateUnits_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,6),_AgentDiffServPolicyAttrStmtExpediteCrateUnits_Type())
agentDiffServPolicyAttrStmtExpediteCrateUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtExpediteCrateUnits.setStatus(_A)
class _AgentDiffServPolicyAttrStmtExpediteCburst_Type(QosBurstSize):defaultValue=4
_AgentDiffServPolicyAttrStmtExpediteCburst_Type.__name__=_W
_AgentDiffServPolicyAttrStmtExpediteCburst_Object=MibTableColumn
agentDiffServPolicyAttrStmtExpediteCburst=_AgentDiffServPolicyAttrStmtExpediteCburst_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,7),_AgentDiffServPolicyAttrStmtExpediteCburst_Type())
agentDiffServPolicyAttrStmtExpediteCburst.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtExpediteCburst.setStatus(_A)
class _AgentDiffServPolicyAttrStmtMarkCosVal_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AgentDiffServPolicyAttrStmtMarkCosVal_Type.__name__=_D
_AgentDiffServPolicyAttrStmtMarkCosVal_Object=MibTableColumn
agentDiffServPolicyAttrStmtMarkCosVal=_AgentDiffServPolicyAttrStmtMarkCosVal_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,8),_AgentDiffServPolicyAttrStmtMarkCosVal_Type())
agentDiffServPolicyAttrStmtMarkCosVal.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtMarkCosVal.setStatus(_A)
class _AgentDiffServPolicyAttrStmtMarkIpDscpVal_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AgentDiffServPolicyAttrStmtMarkIpDscpVal_Type.__name__=_D
_AgentDiffServPolicyAttrStmtMarkIpDscpVal_Object=MibTableColumn
agentDiffServPolicyAttrStmtMarkIpDscpVal=_AgentDiffServPolicyAttrStmtMarkIpDscpVal_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,9),_AgentDiffServPolicyAttrStmtMarkIpDscpVal_Type())
agentDiffServPolicyAttrStmtMarkIpDscpVal.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtMarkIpDscpVal.setStatus(_A)
class _AgentDiffServPolicyAttrStmtMarkIpPrecedenceVal_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AgentDiffServPolicyAttrStmtMarkIpPrecedenceVal_Type.__name__=_D
_AgentDiffServPolicyAttrStmtMarkIpPrecedenceVal_Object=MibTableColumn
agentDiffServPolicyAttrStmtMarkIpPrecedenceVal=_AgentDiffServPolicyAttrStmtMarkIpPrecedenceVal_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,10),_AgentDiffServPolicyAttrStmtMarkIpPrecedenceVal_Type())
agentDiffServPolicyAttrStmtMarkIpPrecedenceVal.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtMarkIpPrecedenceVal.setStatus(_A)
class _AgentDiffServPolicyAttrStmtPoliceConformAct_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4)))
_AgentDiffServPolicyAttrStmtPoliceConformAct_Type.__name__=_F
_AgentDiffServPolicyAttrStmtPoliceConformAct_Object=MibTableColumn
agentDiffServPolicyAttrStmtPoliceConformAct=_AgentDiffServPolicyAttrStmtPoliceConformAct_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,11),_AgentDiffServPolicyAttrStmtPoliceConformAct_Type())
agentDiffServPolicyAttrStmtPoliceConformAct.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtPoliceConformAct.setStatus(_A)
class _AgentDiffServPolicyAttrStmtPoliceConformVal_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AgentDiffServPolicyAttrStmtPoliceConformVal_Type.__name__=_D
_AgentDiffServPolicyAttrStmtPoliceConformVal_Object=MibTableColumn
agentDiffServPolicyAttrStmtPoliceConformVal=_AgentDiffServPolicyAttrStmtPoliceConformVal_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,12),_AgentDiffServPolicyAttrStmtPoliceConformVal_Type())
agentDiffServPolicyAttrStmtPoliceConformVal.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtPoliceConformVal.setStatus(_A)
class _AgentDiffServPolicyAttrStmtPoliceExceedAct_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4)))
_AgentDiffServPolicyAttrStmtPoliceExceedAct_Type.__name__=_F
_AgentDiffServPolicyAttrStmtPoliceExceedAct_Object=MibTableColumn
agentDiffServPolicyAttrStmtPoliceExceedAct=_AgentDiffServPolicyAttrStmtPoliceExceedAct_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,13),_AgentDiffServPolicyAttrStmtPoliceExceedAct_Type())
agentDiffServPolicyAttrStmtPoliceExceedAct.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtPoliceExceedAct.setStatus(_A)
class _AgentDiffServPolicyAttrStmtPoliceExceedVal_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AgentDiffServPolicyAttrStmtPoliceExceedVal_Type.__name__=_D
_AgentDiffServPolicyAttrStmtPoliceExceedVal_Object=MibTableColumn
agentDiffServPolicyAttrStmtPoliceExceedVal=_AgentDiffServPolicyAttrStmtPoliceExceedVal_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,14),_AgentDiffServPolicyAttrStmtPoliceExceedVal_Type())
agentDiffServPolicyAttrStmtPoliceExceedVal.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtPoliceExceedVal.setStatus(_A)
class _AgentDiffServPolicyAttrStmtPoliceNonconformAct_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),(_Q,2),(_R,3),(_S,4)))
_AgentDiffServPolicyAttrStmtPoliceNonconformAct_Type.__name__=_F
_AgentDiffServPolicyAttrStmtPoliceNonconformAct_Object=MibTableColumn
agentDiffServPolicyAttrStmtPoliceNonconformAct=_AgentDiffServPolicyAttrStmtPoliceNonconformAct_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,15),_AgentDiffServPolicyAttrStmtPoliceNonconformAct_Type())
agentDiffServPolicyAttrStmtPoliceNonconformAct.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtPoliceNonconformAct.setStatus(_A)
class _AgentDiffServPolicyAttrStmtPoliceNonconformVal_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AgentDiffServPolicyAttrStmtPoliceNonconformVal_Type.__name__=_D
_AgentDiffServPolicyAttrStmtPoliceNonconformVal_Object=MibTableColumn
agentDiffServPolicyAttrStmtPoliceNonconformVal=_AgentDiffServPolicyAttrStmtPoliceNonconformVal_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,16),_AgentDiffServPolicyAttrStmtPoliceNonconformVal_Type())
agentDiffServPolicyAttrStmtPoliceNonconformVal.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtPoliceNonconformVal.setStatus(_A)
_AgentDiffServPolicyAttrStmtPoliceSimpleCrate_Type=Unsigned32
_AgentDiffServPolicyAttrStmtPoliceSimpleCrate_Object=MibTableColumn
agentDiffServPolicyAttrStmtPoliceSimpleCrate=_AgentDiffServPolicyAttrStmtPoliceSimpleCrate_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,17),_AgentDiffServPolicyAttrStmtPoliceSimpleCrate_Type())
agentDiffServPolicyAttrStmtPoliceSimpleCrate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtPoliceSimpleCrate.setStatus(_A)
_AgentDiffServPolicyAttrStmtPoliceSimpleCburst_Type=QosBurstSize
_AgentDiffServPolicyAttrStmtPoliceSimpleCburst_Object=MibTableColumn
agentDiffServPolicyAttrStmtPoliceSimpleCburst=_AgentDiffServPolicyAttrStmtPoliceSimpleCburst_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,18),_AgentDiffServPolicyAttrStmtPoliceSimpleCburst_Type())
agentDiffServPolicyAttrStmtPoliceSimpleCburst.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtPoliceSimpleCburst.setStatus(_A)
_AgentDiffServPolicyAttrStmtPoliceSinglerateCrate_Type=Unsigned32
_AgentDiffServPolicyAttrStmtPoliceSinglerateCrate_Object=MibTableColumn
agentDiffServPolicyAttrStmtPoliceSinglerateCrate=_AgentDiffServPolicyAttrStmtPoliceSinglerateCrate_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,19),_AgentDiffServPolicyAttrStmtPoliceSinglerateCrate_Type())
agentDiffServPolicyAttrStmtPoliceSinglerateCrate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtPoliceSinglerateCrate.setStatus(_A)
_AgentDiffServPolicyAttrStmtPoliceSinglerateCburst_Type=QosBurstSize
_AgentDiffServPolicyAttrStmtPoliceSinglerateCburst_Object=MibTableColumn
agentDiffServPolicyAttrStmtPoliceSinglerateCburst=_AgentDiffServPolicyAttrStmtPoliceSinglerateCburst_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,20),_AgentDiffServPolicyAttrStmtPoliceSinglerateCburst_Type())
agentDiffServPolicyAttrStmtPoliceSinglerateCburst.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtPoliceSinglerateCburst.setStatus(_A)
_AgentDiffServPolicyAttrStmtPoliceSinglerateEburst_Type=QosBurstSize
_AgentDiffServPolicyAttrStmtPoliceSinglerateEburst_Object=MibTableColumn
agentDiffServPolicyAttrStmtPoliceSinglerateEburst=_AgentDiffServPolicyAttrStmtPoliceSinglerateEburst_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,21),_AgentDiffServPolicyAttrStmtPoliceSinglerateEburst_Type())
agentDiffServPolicyAttrStmtPoliceSinglerateEburst.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtPoliceSinglerateEburst.setStatus(_A)
_AgentDiffServPolicyAttrStmtPoliceTworateCrate_Type=Unsigned32
_AgentDiffServPolicyAttrStmtPoliceTworateCrate_Object=MibTableColumn
agentDiffServPolicyAttrStmtPoliceTworateCrate=_AgentDiffServPolicyAttrStmtPoliceTworateCrate_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,22),_AgentDiffServPolicyAttrStmtPoliceTworateCrate_Type())
agentDiffServPolicyAttrStmtPoliceTworateCrate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtPoliceTworateCrate.setStatus(_A)
_AgentDiffServPolicyAttrStmtPoliceTworateCburst_Type=QosBurstSize
_AgentDiffServPolicyAttrStmtPoliceTworateCburst_Object=MibTableColumn
agentDiffServPolicyAttrStmtPoliceTworateCburst=_AgentDiffServPolicyAttrStmtPoliceTworateCburst_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,23),_AgentDiffServPolicyAttrStmtPoliceTworateCburst_Type())
agentDiffServPolicyAttrStmtPoliceTworateCburst.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtPoliceTworateCburst.setStatus(_A)
_AgentDiffServPolicyAttrStmtPoliceTworatePrate_Type=Unsigned32
_AgentDiffServPolicyAttrStmtPoliceTworatePrate_Object=MibTableColumn
agentDiffServPolicyAttrStmtPoliceTworatePrate=_AgentDiffServPolicyAttrStmtPoliceTworatePrate_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,24),_AgentDiffServPolicyAttrStmtPoliceTworatePrate_Type())
agentDiffServPolicyAttrStmtPoliceTworatePrate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtPoliceTworatePrate.setStatus(_A)
_AgentDiffServPolicyAttrStmtPoliceTworatePburst_Type=QosBurstSize
_AgentDiffServPolicyAttrStmtPoliceTworatePburst_Object=MibTableColumn
agentDiffServPolicyAttrStmtPoliceTworatePburst=_AgentDiffServPolicyAttrStmtPoliceTworatePburst_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,25),_AgentDiffServPolicyAttrStmtPoliceTworatePburst_Type())
agentDiffServPolicyAttrStmtPoliceTworatePburst.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtPoliceTworatePburst.setStatus(_A)
class _AgentDiffServPolicyAttrStmtRandomdropMinThresh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,250000))
_AgentDiffServPolicyAttrStmtRandomdropMinThresh_Type.__name__=_D
_AgentDiffServPolicyAttrStmtRandomdropMinThresh_Object=MibTableColumn
agentDiffServPolicyAttrStmtRandomdropMinThresh=_AgentDiffServPolicyAttrStmtRandomdropMinThresh_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,26),_AgentDiffServPolicyAttrStmtRandomdropMinThresh_Type())
agentDiffServPolicyAttrStmtRandomdropMinThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtRandomdropMinThresh.setStatus(_A)
class _AgentDiffServPolicyAttrStmtRandomdropMaxThresh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,500000))
_AgentDiffServPolicyAttrStmtRandomdropMaxThresh_Type.__name__=_D
_AgentDiffServPolicyAttrStmtRandomdropMaxThresh_Object=MibTableColumn
agentDiffServPolicyAttrStmtRandomdropMaxThresh=_AgentDiffServPolicyAttrStmtRandomdropMaxThresh_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,27),_AgentDiffServPolicyAttrStmtRandomdropMaxThresh_Type())
agentDiffServPolicyAttrStmtRandomdropMaxThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtRandomdropMaxThresh.setStatus(_A)
class _AgentDiffServPolicyAttrStmtRandomdropMaxDropProb_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AgentDiffServPolicyAttrStmtRandomdropMaxDropProb_Type.__name__=_D
_AgentDiffServPolicyAttrStmtRandomdropMaxDropProb_Object=MibTableColumn
agentDiffServPolicyAttrStmtRandomdropMaxDropProb=_AgentDiffServPolicyAttrStmtRandomdropMaxDropProb_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,28),_AgentDiffServPolicyAttrStmtRandomdropMaxDropProb_Type())
agentDiffServPolicyAttrStmtRandomdropMaxDropProb.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtRandomdropMaxDropProb.setStatus(_A)
class _AgentDiffServPolicyAttrStmtRandomdropSamplingRate_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_AgentDiffServPolicyAttrStmtRandomdropSamplingRate_Type.__name__=_D
_AgentDiffServPolicyAttrStmtRandomdropSamplingRate_Object=MibTableColumn
agentDiffServPolicyAttrStmtRandomdropSamplingRate=_AgentDiffServPolicyAttrStmtRandomdropSamplingRate_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,29),_AgentDiffServPolicyAttrStmtRandomdropSamplingRate_Type())
agentDiffServPolicyAttrStmtRandomdropSamplingRate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtRandomdropSamplingRate.setStatus(_A)
class _AgentDiffServPolicyAttrStmtRandomdropDecayExponent_Type(Unsigned32):defaultValue=9;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AgentDiffServPolicyAttrStmtRandomdropDecayExponent_Type.__name__=_D
_AgentDiffServPolicyAttrStmtRandomdropDecayExponent_Object=MibTableColumn
agentDiffServPolicyAttrStmtRandomdropDecayExponent=_AgentDiffServPolicyAttrStmtRandomdropDecayExponent_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,30),_AgentDiffServPolicyAttrStmtRandomdropDecayExponent_Type())
agentDiffServPolicyAttrStmtRandomdropDecayExponent.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtRandomdropDecayExponent.setStatus(_A)
_AgentDiffServPolicyAttrStmtShapeAverageCrate_Type=Unsigned32
_AgentDiffServPolicyAttrStmtShapeAverageCrate_Object=MibTableColumn
agentDiffServPolicyAttrStmtShapeAverageCrate=_AgentDiffServPolicyAttrStmtShapeAverageCrate_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,31),_AgentDiffServPolicyAttrStmtShapeAverageCrate_Type())
agentDiffServPolicyAttrStmtShapeAverageCrate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtShapeAverageCrate.setStatus(_A)
_AgentDiffServPolicyAttrStmtShapePeakCrate_Type=Unsigned32
_AgentDiffServPolicyAttrStmtShapePeakCrate_Object=MibTableColumn
agentDiffServPolicyAttrStmtShapePeakCrate=_AgentDiffServPolicyAttrStmtShapePeakCrate_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,32),_AgentDiffServPolicyAttrStmtShapePeakCrate_Type())
agentDiffServPolicyAttrStmtShapePeakCrate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtShapePeakCrate.setStatus(_A)
_AgentDiffServPolicyAttrStmtShapePeakPrate_Type=Unsigned32
_AgentDiffServPolicyAttrStmtShapePeakPrate_Object=MibTableColumn
agentDiffServPolicyAttrStmtShapePeakPrate=_AgentDiffServPolicyAttrStmtShapePeakPrate_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,33),_AgentDiffServPolicyAttrStmtShapePeakPrate_Type())
agentDiffServPolicyAttrStmtShapePeakPrate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStmtShapePeakPrate.setStatus(_A)
class _AgentDiffServPolicyAttrStorageType_Type(StorageType):defaultValue=3
_AgentDiffServPolicyAttrStorageType_Type.__name__=_G
_AgentDiffServPolicyAttrStorageType_Object=MibTableColumn
agentDiffServPolicyAttrStorageType=_AgentDiffServPolicyAttrStorageType_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,34),_AgentDiffServPolicyAttrStorageType_Type())
agentDiffServPolicyAttrStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrStorageType.setStatus(_A)
_AgentDiffServPolicyAttrRowStatus_Type=RowStatus
_AgentDiffServPolicyAttrRowStatus_Object=MibTableColumn
agentDiffServPolicyAttrRowStatus=_AgentDiffServPolicyAttrRowStatus_Object((1,3,6,1,4,1,4526,1,9,3,4,3,4,1,35),_AgentDiffServPolicyAttrRowStatus_Type())
agentDiffServPolicyAttrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServPolicyAttrRowStatus.setStatus(_A)
_AgentDiffServPolicyPerfInTable_Object=MibTable
agentDiffServPolicyPerfInTable=_AgentDiffServPolicyPerfInTable_Object((1,3,6,1,4,1,4526,1,9,3,4,3,5))
if mibBuilder.loadTexts:agentDiffServPolicyPerfInTable.setStatus(_A)
_AgentDiffServPolicyPerfInEntry_Object=MibTableRow
agentDiffServPolicyPerfInEntry=_AgentDiffServPolicyPerfInEntry_Object((1,3,6,1,4,1,4526,1,9,3,4,3,5,1))
agentDiffServPolicyPerfInEntry.setIndexNames((0,_E,_I),(0,_E,_J),(0,_L,_M))
if mibBuilder.loadTexts:agentDiffServPolicyPerfInEntry.setStatus(_A)
_AgentDiffServPolicyPerfInOfferedOctets_Type=Counter32
_AgentDiffServPolicyPerfInOfferedOctets_Object=MibTableColumn
agentDiffServPolicyPerfInOfferedOctets=_AgentDiffServPolicyPerfInOfferedOctets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,5,1,1),_AgentDiffServPolicyPerfInOfferedOctets_Type())
agentDiffServPolicyPerfInOfferedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfInOfferedOctets.setStatus(_A)
_AgentDiffServPolicyPerfInOfferedPackets_Type=Counter32
_AgentDiffServPolicyPerfInOfferedPackets_Object=MibTableColumn
agentDiffServPolicyPerfInOfferedPackets=_AgentDiffServPolicyPerfInOfferedPackets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,5,1,2),_AgentDiffServPolicyPerfInOfferedPackets_Type())
agentDiffServPolicyPerfInOfferedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfInOfferedPackets.setStatus(_A)
_AgentDiffServPolicyPerfInDiscardedOctets_Type=Counter32
_AgentDiffServPolicyPerfInDiscardedOctets_Object=MibTableColumn
agentDiffServPolicyPerfInDiscardedOctets=_AgentDiffServPolicyPerfInDiscardedOctets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,5,1,3),_AgentDiffServPolicyPerfInDiscardedOctets_Type())
agentDiffServPolicyPerfInDiscardedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfInDiscardedOctets.setStatus(_A)
_AgentDiffServPolicyPerfInDiscardedPackets_Type=Counter32
_AgentDiffServPolicyPerfInDiscardedPackets_Object=MibTableColumn
agentDiffServPolicyPerfInDiscardedPackets=_AgentDiffServPolicyPerfInDiscardedPackets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,5,1,4),_AgentDiffServPolicyPerfInDiscardedPackets_Type())
agentDiffServPolicyPerfInDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfInDiscardedPackets.setStatus(_A)
_AgentDiffServPolicyPerfInHCOfferedOctets_Type=Counter64
_AgentDiffServPolicyPerfInHCOfferedOctets_Object=MibTableColumn
agentDiffServPolicyPerfInHCOfferedOctets=_AgentDiffServPolicyPerfInHCOfferedOctets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,5,1,5),_AgentDiffServPolicyPerfInHCOfferedOctets_Type())
agentDiffServPolicyPerfInHCOfferedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfInHCOfferedOctets.setStatus(_A)
_AgentDiffServPolicyPerfInHCOfferedPackets_Type=Counter64
_AgentDiffServPolicyPerfInHCOfferedPackets_Object=MibTableColumn
agentDiffServPolicyPerfInHCOfferedPackets=_AgentDiffServPolicyPerfInHCOfferedPackets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,5,1,6),_AgentDiffServPolicyPerfInHCOfferedPackets_Type())
agentDiffServPolicyPerfInHCOfferedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfInHCOfferedPackets.setStatus(_A)
_AgentDiffServPolicyPerfInHCDiscardedOctets_Type=Counter64
_AgentDiffServPolicyPerfInHCDiscardedOctets_Object=MibTableColumn
agentDiffServPolicyPerfInHCDiscardedOctets=_AgentDiffServPolicyPerfInHCDiscardedOctets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,5,1,7),_AgentDiffServPolicyPerfInHCDiscardedOctets_Type())
agentDiffServPolicyPerfInHCDiscardedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfInHCDiscardedOctets.setStatus(_A)
_AgentDiffServPolicyPerfInHCDiscardedPackets_Type=Counter64
_AgentDiffServPolicyPerfInHCDiscardedPackets_Object=MibTableColumn
agentDiffServPolicyPerfInHCDiscardedPackets=_AgentDiffServPolicyPerfInHCDiscardedPackets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,5,1,8),_AgentDiffServPolicyPerfInHCDiscardedPackets_Type())
agentDiffServPolicyPerfInHCDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfInHCDiscardedPackets.setStatus(_A)
class _AgentDiffServPolicyPerfInStorageType_Type(StorageType):defaultValue=3
_AgentDiffServPolicyPerfInStorageType_Type.__name__=_G
_AgentDiffServPolicyPerfInStorageType_Object=MibTableColumn
agentDiffServPolicyPerfInStorageType=_AgentDiffServPolicyPerfInStorageType_Object((1,3,6,1,4,1,4526,1,9,3,4,3,5,1,9),_AgentDiffServPolicyPerfInStorageType_Type())
agentDiffServPolicyPerfInStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfInStorageType.setStatus(_A)
_AgentDiffServPolicyPerfInRowStatus_Type=RowStatus
_AgentDiffServPolicyPerfInRowStatus_Object=MibTableColumn
agentDiffServPolicyPerfInRowStatus=_AgentDiffServPolicyPerfInRowStatus_Object((1,3,6,1,4,1,4526,1,9,3,4,3,5,1,10),_AgentDiffServPolicyPerfInRowStatus_Type())
agentDiffServPolicyPerfInRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfInRowStatus.setStatus(_A)
_AgentDiffServPolicyPerfOutTable_Object=MibTable
agentDiffServPolicyPerfOutTable=_AgentDiffServPolicyPerfOutTable_Object((1,3,6,1,4,1,4526,1,9,3,4,3,6))
if mibBuilder.loadTexts:agentDiffServPolicyPerfOutTable.setStatus(_A)
_AgentDiffServPolicyPerfOutEntry_Object=MibTableRow
agentDiffServPolicyPerfOutEntry=_AgentDiffServPolicyPerfOutEntry_Object((1,3,6,1,4,1,4526,1,9,3,4,3,6,1))
agentDiffServPolicyPerfOutEntry.setIndexNames((0,_E,_I),(0,_E,_J),(0,_L,_M))
if mibBuilder.loadTexts:agentDiffServPolicyPerfOutEntry.setStatus(_A)
_AgentDiffServPolicyPerfOutTailDroppedOctets_Type=Counter32
_AgentDiffServPolicyPerfOutTailDroppedOctets_Object=MibTableColumn
agentDiffServPolicyPerfOutTailDroppedOctets=_AgentDiffServPolicyPerfOutTailDroppedOctets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,6,1,1),_AgentDiffServPolicyPerfOutTailDroppedOctets_Type())
agentDiffServPolicyPerfOutTailDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfOutTailDroppedOctets.setStatus(_A)
_AgentDiffServPolicyPerfOutTailDroppedPackets_Type=Counter32
_AgentDiffServPolicyPerfOutTailDroppedPackets_Object=MibTableColumn
agentDiffServPolicyPerfOutTailDroppedPackets=_AgentDiffServPolicyPerfOutTailDroppedPackets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,6,1,2),_AgentDiffServPolicyPerfOutTailDroppedPackets_Type())
agentDiffServPolicyPerfOutTailDroppedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfOutTailDroppedPackets.setStatus(_A)
_AgentDiffServPolicyPerfOutRandomDroppedOctets_Type=Counter32
_AgentDiffServPolicyPerfOutRandomDroppedOctets_Object=MibTableColumn
agentDiffServPolicyPerfOutRandomDroppedOctets=_AgentDiffServPolicyPerfOutRandomDroppedOctets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,6,1,3),_AgentDiffServPolicyPerfOutRandomDroppedOctets_Type())
agentDiffServPolicyPerfOutRandomDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfOutRandomDroppedOctets.setStatus(_A)
_AgentDiffServPolicyPerfOutRandomDroppedPackets_Type=Counter32
_AgentDiffServPolicyPerfOutRandomDroppedPackets_Object=MibTableColumn
agentDiffServPolicyPerfOutRandomDroppedPackets=_AgentDiffServPolicyPerfOutRandomDroppedPackets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,6,1,4),_AgentDiffServPolicyPerfOutRandomDroppedPackets_Type())
agentDiffServPolicyPerfOutRandomDroppedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfOutRandomDroppedPackets.setStatus(_A)
_AgentDiffServPolicyPerfOutShapeDelayedOctets_Type=Counter32
_AgentDiffServPolicyPerfOutShapeDelayedOctets_Object=MibTableColumn
agentDiffServPolicyPerfOutShapeDelayedOctets=_AgentDiffServPolicyPerfOutShapeDelayedOctets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,6,1,5),_AgentDiffServPolicyPerfOutShapeDelayedOctets_Type())
agentDiffServPolicyPerfOutShapeDelayedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfOutShapeDelayedOctets.setStatus(_A)
_AgentDiffServPolicyPerfOutShapeDelayedPackets_Type=Counter32
_AgentDiffServPolicyPerfOutShapeDelayedPackets_Object=MibTableColumn
agentDiffServPolicyPerfOutShapeDelayedPackets=_AgentDiffServPolicyPerfOutShapeDelayedPackets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,6,1,6),_AgentDiffServPolicyPerfOutShapeDelayedPackets_Type())
agentDiffServPolicyPerfOutShapeDelayedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfOutShapeDelayedPackets.setStatus(_A)
_AgentDiffServPolicyPerfOutSentOctets_Type=Counter32
_AgentDiffServPolicyPerfOutSentOctets_Object=MibTableColumn
agentDiffServPolicyPerfOutSentOctets=_AgentDiffServPolicyPerfOutSentOctets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,6,1,7),_AgentDiffServPolicyPerfOutSentOctets_Type())
agentDiffServPolicyPerfOutSentOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfOutSentOctets.setStatus(_A)
_AgentDiffServPolicyPerfOutSentPackets_Type=Counter32
_AgentDiffServPolicyPerfOutSentPackets_Object=MibTableColumn
agentDiffServPolicyPerfOutSentPackets=_AgentDiffServPolicyPerfOutSentPackets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,6,1,8),_AgentDiffServPolicyPerfOutSentPackets_Type())
agentDiffServPolicyPerfOutSentPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfOutSentPackets.setStatus(_A)
_AgentDiffServPolicyPerfOutHCTailDroppedOctets_Type=Counter64
_AgentDiffServPolicyPerfOutHCTailDroppedOctets_Object=MibTableColumn
agentDiffServPolicyPerfOutHCTailDroppedOctets=_AgentDiffServPolicyPerfOutHCTailDroppedOctets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,6,1,9),_AgentDiffServPolicyPerfOutHCTailDroppedOctets_Type())
agentDiffServPolicyPerfOutHCTailDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfOutHCTailDroppedOctets.setStatus(_A)
_AgentDiffServPolicyPerfOutHCTailDroppedPackets_Type=Counter64
_AgentDiffServPolicyPerfOutHCTailDroppedPackets_Object=MibTableColumn
agentDiffServPolicyPerfOutHCTailDroppedPackets=_AgentDiffServPolicyPerfOutHCTailDroppedPackets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,6,1,10),_AgentDiffServPolicyPerfOutHCTailDroppedPackets_Type())
agentDiffServPolicyPerfOutHCTailDroppedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfOutHCTailDroppedPackets.setStatus(_A)
_AgentDiffServPolicyPerfOutHCRandomDroppedOctets_Type=Counter64
_AgentDiffServPolicyPerfOutHCRandomDroppedOctets_Object=MibTableColumn
agentDiffServPolicyPerfOutHCRandomDroppedOctets=_AgentDiffServPolicyPerfOutHCRandomDroppedOctets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,6,1,11),_AgentDiffServPolicyPerfOutHCRandomDroppedOctets_Type())
agentDiffServPolicyPerfOutHCRandomDroppedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfOutHCRandomDroppedOctets.setStatus(_A)
_AgentDiffServPolicyPerfOutHCRandomDroppedPackets_Type=Counter64
_AgentDiffServPolicyPerfOutHCRandomDroppedPackets_Object=MibTableColumn
agentDiffServPolicyPerfOutHCRandomDroppedPackets=_AgentDiffServPolicyPerfOutHCRandomDroppedPackets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,6,1,12),_AgentDiffServPolicyPerfOutHCRandomDroppedPackets_Type())
agentDiffServPolicyPerfOutHCRandomDroppedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfOutHCRandomDroppedPackets.setStatus(_A)
_AgentDiffServPolicyPerfOutHCShapeDelayedOctets_Type=Counter64
_AgentDiffServPolicyPerfOutHCShapeDelayedOctets_Object=MibTableColumn
agentDiffServPolicyPerfOutHCShapeDelayedOctets=_AgentDiffServPolicyPerfOutHCShapeDelayedOctets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,6,1,13),_AgentDiffServPolicyPerfOutHCShapeDelayedOctets_Type())
agentDiffServPolicyPerfOutHCShapeDelayedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfOutHCShapeDelayedOctets.setStatus(_A)
_AgentDiffServPolicyPerfOutHCShapeDelayedPackets_Type=Counter64
_AgentDiffServPolicyPerfOutHCShapeDelayedPackets_Object=MibTableColumn
agentDiffServPolicyPerfOutHCShapeDelayedPackets=_AgentDiffServPolicyPerfOutHCShapeDelayedPackets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,6,1,14),_AgentDiffServPolicyPerfOutHCShapeDelayedPackets_Type())
agentDiffServPolicyPerfOutHCShapeDelayedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfOutHCShapeDelayedPackets.setStatus(_A)
_AgentDiffServPolicyPerfOutHCSentOctets_Type=Counter64
_AgentDiffServPolicyPerfOutHCSentOctets_Object=MibTableColumn
agentDiffServPolicyPerfOutHCSentOctets=_AgentDiffServPolicyPerfOutHCSentOctets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,6,1,15),_AgentDiffServPolicyPerfOutHCSentOctets_Type())
agentDiffServPolicyPerfOutHCSentOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfOutHCSentOctets.setStatus(_A)
_AgentDiffServPolicyPerfOutHCSentPackets_Type=Counter64
_AgentDiffServPolicyPerfOutHCSentPackets_Object=MibTableColumn
agentDiffServPolicyPerfOutHCSentPackets=_AgentDiffServPolicyPerfOutHCSentPackets_Object((1,3,6,1,4,1,4526,1,9,3,4,3,6,1,16),_AgentDiffServPolicyPerfOutHCSentPackets_Type())
agentDiffServPolicyPerfOutHCSentPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfOutHCSentPackets.setStatus(_A)
class _AgentDiffServPolicyPerfOutStorageType_Type(StorageType):defaultValue=3
_AgentDiffServPolicyPerfOutStorageType_Type.__name__=_G
_AgentDiffServPolicyPerfOutStorageType_Object=MibTableColumn
agentDiffServPolicyPerfOutStorageType=_AgentDiffServPolicyPerfOutStorageType_Object((1,3,6,1,4,1,4526,1,9,3,4,3,6,1,17),_AgentDiffServPolicyPerfOutStorageType_Type())
agentDiffServPolicyPerfOutStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfOutStorageType.setStatus(_A)
_AgentDiffServPolicyPerfOutRowStatus_Type=RowStatus
_AgentDiffServPolicyPerfOutRowStatus_Object=MibTableColumn
agentDiffServPolicyPerfOutRowStatus=_AgentDiffServPolicyPerfOutRowStatus_Object((1,3,6,1,4,1,4526,1,9,3,4,3,6,1,18),_AgentDiffServPolicyPerfOutRowStatus_Type())
agentDiffServPolicyPerfOutRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServPolicyPerfOutRowStatus.setStatus(_A)
_AgentDiffServServiceGroup_ObjectIdentity=ObjectIdentity
agentDiffServServiceGroup=_AgentDiffServServiceGroup_ObjectIdentity((1,3,6,1,4,1,4526,1,9,3,4,4))
_AgentDiffServServiceTable_Object=MibTable
agentDiffServServiceTable=_AgentDiffServServiceTable_Object((1,3,6,1,4,1,4526,1,9,3,4,4,1))
if mibBuilder.loadTexts:agentDiffServServiceTable.setStatus(_A)
_AgentDiffServServiceEntry_Object=MibTableRow
agentDiffServServiceEntry=_AgentDiffServServiceEntry_Object((1,3,6,1,4,1,4526,1,9,3,4,4,1,1))
agentDiffServServiceEntry.setIndexNames((0,_E,_X),(0,_E,_Y))
if mibBuilder.loadTexts:agentDiffServServiceEntry.setStatus(_A)
_AgentDiffServServiceIfIndex_Type=InterfaceIndex
_AgentDiffServServiceIfIndex_Object=MibTableColumn
agentDiffServServiceIfIndex=_AgentDiffServServiceIfIndex_Object((1,3,6,1,4,1,4526,1,9,3,4,4,1,1,1),_AgentDiffServServiceIfIndex_Type())
agentDiffServServiceIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:agentDiffServServiceIfIndex.setStatus(_A)
_AgentDiffServServiceIfDirection_Type=IntfDirection
_AgentDiffServServiceIfDirection_Object=MibTableColumn
agentDiffServServiceIfDirection=_AgentDiffServServiceIfDirection_Object((1,3,6,1,4,1,4526,1,9,3,4,4,1,1,2),_AgentDiffServServiceIfDirection_Type())
agentDiffServServiceIfDirection.setMaxAccess(_H)
if mibBuilder.loadTexts:agentDiffServServiceIfDirection.setStatus(_A)
_AgentDiffServServicePolicyIndex_Type=Unsigned32
_AgentDiffServServicePolicyIndex_Object=MibTableColumn
agentDiffServServicePolicyIndex=_AgentDiffServServicePolicyIndex_Object((1,3,6,1,4,1,4526,1,9,3,4,4,1,1,3),_AgentDiffServServicePolicyIndex_Type())
agentDiffServServicePolicyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServServicePolicyIndex.setStatus(_A)
class _AgentDiffServServiceIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_AgentDiffServServiceIfOperStatus_Type.__name__=_F
_AgentDiffServServiceIfOperStatus_Object=MibTableColumn
agentDiffServServiceIfOperStatus=_AgentDiffServServiceIfOperStatus_Object((1,3,6,1,4,1,4526,1,9,3,4,4,1,1,4),_AgentDiffServServiceIfOperStatus_Type())
agentDiffServServiceIfOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServServiceIfOperStatus.setStatus(_A)
class _AgentDiffServServiceStorageType_Type(StorageType):defaultValue=3
_AgentDiffServServiceStorageType_Type.__name__=_G
_AgentDiffServServiceStorageType_Object=MibTableColumn
agentDiffServServiceStorageType=_AgentDiffServServiceStorageType_Object((1,3,6,1,4,1,4526,1,9,3,4,4,1,1,5),_AgentDiffServServiceStorageType_Type())
agentDiffServServiceStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServServiceStorageType.setStatus(_A)
_AgentDiffServServiceRowStatus_Type=RowStatus
_AgentDiffServServiceRowStatus_Object=MibTableColumn
agentDiffServServiceRowStatus=_AgentDiffServServiceRowStatus_Object((1,3,6,1,4,1,4526,1,9,3,4,4,1,1,6),_AgentDiffServServiceRowStatus_Type())
agentDiffServServiceRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDiffServServiceRowStatus.setStatus(_A)
_AgentDiffServServicePerfTable_Object=MibTable
agentDiffServServicePerfTable=_AgentDiffServServicePerfTable_Object((1,3,6,1,4,1,4526,1,9,3,4,4,2))
if mibBuilder.loadTexts:agentDiffServServicePerfTable.setStatus(_A)
_AgentDiffServServicePerfEntry_Object=MibTableRow
agentDiffServServicePerfEntry=_AgentDiffServServicePerfEntry_Object((1,3,6,1,4,1,4526,1,9,3,4,4,2,1))
if mibBuilder.loadTexts:agentDiffServServicePerfEntry.setStatus(_A)
_AgentDiffServServicePerfOfferedOctets_Type=Counter32
_AgentDiffServServicePerfOfferedOctets_Object=MibTableColumn
agentDiffServServicePerfOfferedOctets=_AgentDiffServServicePerfOfferedOctets_Object((1,3,6,1,4,1,4526,1,9,3,4,4,2,1,1),_AgentDiffServServicePerfOfferedOctets_Type())
agentDiffServServicePerfOfferedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServServicePerfOfferedOctets.setStatus(_A)
_AgentDiffServServicePerfOfferedPackets_Type=Counter32
_AgentDiffServServicePerfOfferedPackets_Object=MibTableColumn
agentDiffServServicePerfOfferedPackets=_AgentDiffServServicePerfOfferedPackets_Object((1,3,6,1,4,1,4526,1,9,3,4,4,2,1,2),_AgentDiffServServicePerfOfferedPackets_Type())
agentDiffServServicePerfOfferedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServServicePerfOfferedPackets.setStatus(_A)
_AgentDiffServServicePerfDiscardedOctets_Type=Counter32
_AgentDiffServServicePerfDiscardedOctets_Object=MibTableColumn
agentDiffServServicePerfDiscardedOctets=_AgentDiffServServicePerfDiscardedOctets_Object((1,3,6,1,4,1,4526,1,9,3,4,4,2,1,3),_AgentDiffServServicePerfDiscardedOctets_Type())
agentDiffServServicePerfDiscardedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServServicePerfDiscardedOctets.setStatus(_A)
_AgentDiffServServicePerfDiscardedPackets_Type=Counter32
_AgentDiffServServicePerfDiscardedPackets_Object=MibTableColumn
agentDiffServServicePerfDiscardedPackets=_AgentDiffServServicePerfDiscardedPackets_Object((1,3,6,1,4,1,4526,1,9,3,4,4,2,1,4),_AgentDiffServServicePerfDiscardedPackets_Type())
agentDiffServServicePerfDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServServicePerfDiscardedPackets.setStatus(_A)
_AgentDiffServServicePerfSentOctets_Type=Counter32
_AgentDiffServServicePerfSentOctets_Object=MibTableColumn
agentDiffServServicePerfSentOctets=_AgentDiffServServicePerfSentOctets_Object((1,3,6,1,4,1,4526,1,9,3,4,4,2,1,5),_AgentDiffServServicePerfSentOctets_Type())
agentDiffServServicePerfSentOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServServicePerfSentOctets.setStatus(_A)
_AgentDiffServServicePerfSentPackets_Type=Counter32
_AgentDiffServServicePerfSentPackets_Object=MibTableColumn
agentDiffServServicePerfSentPackets=_AgentDiffServServicePerfSentPackets_Object((1,3,6,1,4,1,4526,1,9,3,4,4,2,1,6),_AgentDiffServServicePerfSentPackets_Type())
agentDiffServServicePerfSentPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServServicePerfSentPackets.setStatus(_A)
_AgentDiffServServicePerfHCOfferedOctets_Type=Counter64
_AgentDiffServServicePerfHCOfferedOctets_Object=MibTableColumn
agentDiffServServicePerfHCOfferedOctets=_AgentDiffServServicePerfHCOfferedOctets_Object((1,3,6,1,4,1,4526,1,9,3,4,4,2,1,7),_AgentDiffServServicePerfHCOfferedOctets_Type())
agentDiffServServicePerfHCOfferedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServServicePerfHCOfferedOctets.setStatus(_A)
_AgentDiffServServicePerfHCOfferedPackets_Type=Counter64
_AgentDiffServServicePerfHCOfferedPackets_Object=MibTableColumn
agentDiffServServicePerfHCOfferedPackets=_AgentDiffServServicePerfHCOfferedPackets_Object((1,3,6,1,4,1,4526,1,9,3,4,4,2,1,8),_AgentDiffServServicePerfHCOfferedPackets_Type())
agentDiffServServicePerfHCOfferedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServServicePerfHCOfferedPackets.setStatus(_A)
_AgentDiffServServicePerfHCDiscardedOctets_Type=Counter64
_AgentDiffServServicePerfHCDiscardedOctets_Object=MibTableColumn
agentDiffServServicePerfHCDiscardedOctets=_AgentDiffServServicePerfHCDiscardedOctets_Object((1,3,6,1,4,1,4526,1,9,3,4,4,2,1,9),_AgentDiffServServicePerfHCDiscardedOctets_Type())
agentDiffServServicePerfHCDiscardedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServServicePerfHCDiscardedOctets.setStatus(_A)
_AgentDiffServServicePerfHCDiscardedPackets_Type=Counter64
_AgentDiffServServicePerfHCDiscardedPackets_Object=MibTableColumn
agentDiffServServicePerfHCDiscardedPackets=_AgentDiffServServicePerfHCDiscardedPackets_Object((1,3,6,1,4,1,4526,1,9,3,4,4,2,1,10),_AgentDiffServServicePerfHCDiscardedPackets_Type())
agentDiffServServicePerfHCDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServServicePerfHCDiscardedPackets.setStatus(_A)
_AgentDiffServServicePerfHCSentOctets_Type=Counter64
_AgentDiffServServicePerfHCSentOctets_Object=MibTableColumn
agentDiffServServicePerfHCSentOctets=_AgentDiffServServicePerfHCSentOctets_Object((1,3,6,1,4,1,4526,1,9,3,4,4,2,1,11),_AgentDiffServServicePerfHCSentOctets_Type())
agentDiffServServicePerfHCSentOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServServicePerfHCSentOctets.setStatus(_A)
_AgentDiffServServicePerfHCSentPackets_Type=Counter64
_AgentDiffServServicePerfHCSentPackets_Object=MibTableColumn
agentDiffServServicePerfHCSentPackets=_AgentDiffServServicePerfHCSentPackets_Object((1,3,6,1,4,1,4526,1,9,3,4,4,2,1,12),_AgentDiffServServicePerfHCSentPackets_Type())
agentDiffServServicePerfHCSentPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDiffServServicePerfHCSentPackets.setStatus(_A)
agentDiffServServiceEntry.registerAugmentions((_E,_Z))
agentDiffServServicePerfEntry.setIndexNames(*agentDiffServServiceEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{_W:QosBurstSize,'IntfDirection':IntfDirection,'fsm7326QOSDiffServPrivate':fsm7326QOSDiffServPrivate,'agentDiffServGenStatusGroup':agentDiffServGenStatusGroup,'agentDiffServGenStatusAdminMode':agentDiffServGenStatusAdminMode,'agentDiffServGenStatusClassTableSize':agentDiffServGenStatusClassTableSize,'agentDiffServGenStatusClassTableMax':agentDiffServGenStatusClassTableMax,'agentDiffServGenStatusClassRuleTableSize':agentDiffServGenStatusClassRuleTableSize,'agentDiffServGenStatusClassRuleTableMax':agentDiffServGenStatusClassRuleTableMax,'agentDiffServGenStatusPolicyTableSize':agentDiffServGenStatusPolicyTableSize,'agentDiffServGenStatusPolicyTableMax':agentDiffServGenStatusPolicyTableMax,'agentDiffServGenStatusPolicyInstTableSize':agentDiffServGenStatusPolicyInstTableSize,'agentDiffServGenStatusPolicyInstTableMax':agentDiffServGenStatusPolicyInstTableMax,'agentDiffServGenStatusPolicyAttrTableSize':agentDiffServGenStatusPolicyAttrTableSize,'agentDiffServGenStatusPolicyAttrTableMax':agentDiffServGenStatusPolicyAttrTableMax,'agentDiffServGenStatusServiceTableSize':agentDiffServGenStatusServiceTableSize,'agentDiffServGenStatusServiceTableMax':agentDiffServGenStatusServiceTableMax,'agentDiffServClassGroup':agentDiffServClassGroup,'agentDiffServClassIndexNextFree':agentDiffServClassIndexNextFree,'agentDiffServClassTable':agentDiffServClassTable,'agentDiffServClassEntry':agentDiffServClassEntry,_O:agentDiffServClassIndex,'agentDiffServClassName':agentDiffServClassName,'agentDiffServClassType':agentDiffServClassType,'agentDiffServClassAclNum':agentDiffServClassAclNum,'agentDiffServClassRuleIndexNextFree':agentDiffServClassRuleIndexNextFree,'agentDiffServClassStorageType':agentDiffServClassStorageType,'agentDiffServClassRowStatus':agentDiffServClassRowStatus,'agentDiffServClassRuleTable':agentDiffServClassRuleTable,'agentDiffServClassRuleEntry':agentDiffServClassRuleEntry,_T:agentDiffServClassRuleIndex,'agentDiffServClassRuleMatchEntryType':agentDiffServClassRuleMatchEntryType,'agentDiffServClassRuleMatchCos':agentDiffServClassRuleMatchCos,'agentDiffServClassRuleMatchDstIpAddr':agentDiffServClassRuleMatchDstIpAddr,'agentDiffServClassRuleMatchDstIpMask':agentDiffServClassRuleMatchDstIpMask,'agentDiffServClassRuleMatchDstL4PortStart':agentDiffServClassRuleMatchDstL4PortStart,'agentDiffServClassRuleMatchDstL4PortEnd':agentDiffServClassRuleMatchDstL4PortEnd,'agentDiffServClassRuleMatchDstMacAddr':agentDiffServClassRuleMatchDstMacAddr,'agentDiffServClassRuleMatchDstMacMask':agentDiffServClassRuleMatchDstMacMask,'agentDiffServClassRuleMatchEvery':agentDiffServClassRuleMatchEvery,'agentDiffServClassRuleMatchIpDscp':agentDiffServClassRuleMatchIpDscp,'agentDiffServClassRuleMatchIpPrecedence':agentDiffServClassRuleMatchIpPrecedence,'agentDiffServClassRuleMatchIpTosBits':agentDiffServClassRuleMatchIpTosBits,'agentDiffServClassRuleMatchIpTosMask':agentDiffServClassRuleMatchIpTosMask,'agentDiffServClassRuleMatchProtocolNum':agentDiffServClassRuleMatchProtocolNum,'agentDiffServClassRuleMatchRefClassIndex':agentDiffServClassRuleMatchRefClassIndex,'agentDiffServClassRuleMatchSrcIpAddr':agentDiffServClassRuleMatchSrcIpAddr,'agentDiffServClassRuleMatchSrcIpMask':agentDiffServClassRuleMatchSrcIpMask,'agentDiffServClassRuleMatchSrcL4PortStart':agentDiffServClassRuleMatchSrcL4PortStart,'agentDiffServClassRuleMatchSrcL4PortEnd':agentDiffServClassRuleMatchSrcL4PortEnd,'agentDiffServClassRuleMatchSrcMacAddr':agentDiffServClassRuleMatchSrcMacAddr,'agentDiffServClassRuleMatchSrcMacMask':agentDiffServClassRuleMatchSrcMacMask,'agentDiffServClassRuleMatchVlanId':agentDiffServClassRuleMatchVlanId,'agentDiffServClassRuleMatchExcludeFlag':agentDiffServClassRuleMatchExcludeFlag,'agentDiffServClassRuleStorageType':agentDiffServClassRuleStorageType,'agentDiffServClassRuleRowStatus':agentDiffServClassRuleRowStatus,'agentDiffServPolicyGroup':agentDiffServPolicyGroup,'agentDiffServPolicyIndexNextFree':agentDiffServPolicyIndexNextFree,'agentDiffServPolicyTable':agentDiffServPolicyTable,'agentDiffServPolicyEntry':agentDiffServPolicyEntry,_I:agentDiffServPolicyIndex,'agentDiffServPolicyName':agentDiffServPolicyName,'agentDiffServPolicyType':agentDiffServPolicyType,'agentDiffServPolicyInstIndexNextFree':agentDiffServPolicyInstIndexNextFree,'agentDiffServPolicyStorageType':agentDiffServPolicyStorageType,'agentDiffServPolicyRowStatus':agentDiffServPolicyRowStatus,'agentDiffServPolicyInstTable':agentDiffServPolicyInstTable,'agentDiffServPolicyInstEntry':agentDiffServPolicyInstEntry,_J:agentDiffServPolicyInstIndex,'agentDiffServPolicyInstClassIndex':agentDiffServPolicyInstClassIndex,'agentDiffServPolicyInstAttrIndexNextFree':agentDiffServPolicyInstAttrIndexNextFree,'agentDiffServPolicyInstStorageType':agentDiffServPolicyInstStorageType,'agentDiffServPolicyInstRowStatus':agentDiffServPolicyInstRowStatus,'agentDiffServPolicyAttrTable':agentDiffServPolicyAttrTable,'agentDiffServPolicyAttrEntry':agentDiffServPolicyAttrEntry,_U:agentDiffServPolicyAttrIndex,'agentDiffServPolicyAttrStmtEntryType':agentDiffServPolicyAttrStmtEntryType,'agentDiffServPolicyAttrStmtBandwidthCrate':agentDiffServPolicyAttrStmtBandwidthCrate,'agentDiffServPolicyAttrStmtBandwidthCrateUnits':agentDiffServPolicyAttrStmtBandwidthCrateUnits,'agentDiffServPolicyAttrStmtExpediteCrate':agentDiffServPolicyAttrStmtExpediteCrate,'agentDiffServPolicyAttrStmtExpediteCrateUnits':agentDiffServPolicyAttrStmtExpediteCrateUnits,'agentDiffServPolicyAttrStmtExpediteCburst':agentDiffServPolicyAttrStmtExpediteCburst,'agentDiffServPolicyAttrStmtMarkCosVal':agentDiffServPolicyAttrStmtMarkCosVal,'agentDiffServPolicyAttrStmtMarkIpDscpVal':agentDiffServPolicyAttrStmtMarkIpDscpVal,'agentDiffServPolicyAttrStmtMarkIpPrecedenceVal':agentDiffServPolicyAttrStmtMarkIpPrecedenceVal,'agentDiffServPolicyAttrStmtPoliceConformAct':agentDiffServPolicyAttrStmtPoliceConformAct,'agentDiffServPolicyAttrStmtPoliceConformVal':agentDiffServPolicyAttrStmtPoliceConformVal,'agentDiffServPolicyAttrStmtPoliceExceedAct':agentDiffServPolicyAttrStmtPoliceExceedAct,'agentDiffServPolicyAttrStmtPoliceExceedVal':agentDiffServPolicyAttrStmtPoliceExceedVal,'agentDiffServPolicyAttrStmtPoliceNonconformAct':agentDiffServPolicyAttrStmtPoliceNonconformAct,'agentDiffServPolicyAttrStmtPoliceNonconformVal':agentDiffServPolicyAttrStmtPoliceNonconformVal,'agentDiffServPolicyAttrStmtPoliceSimpleCrate':agentDiffServPolicyAttrStmtPoliceSimpleCrate,'agentDiffServPolicyAttrStmtPoliceSimpleCburst':agentDiffServPolicyAttrStmtPoliceSimpleCburst,'agentDiffServPolicyAttrStmtPoliceSinglerateCrate':agentDiffServPolicyAttrStmtPoliceSinglerateCrate,'agentDiffServPolicyAttrStmtPoliceSinglerateCburst':agentDiffServPolicyAttrStmtPoliceSinglerateCburst,'agentDiffServPolicyAttrStmtPoliceSinglerateEburst':agentDiffServPolicyAttrStmtPoliceSinglerateEburst,'agentDiffServPolicyAttrStmtPoliceTworateCrate':agentDiffServPolicyAttrStmtPoliceTworateCrate,'agentDiffServPolicyAttrStmtPoliceTworateCburst':agentDiffServPolicyAttrStmtPoliceTworateCburst,'agentDiffServPolicyAttrStmtPoliceTworatePrate':agentDiffServPolicyAttrStmtPoliceTworatePrate,'agentDiffServPolicyAttrStmtPoliceTworatePburst':agentDiffServPolicyAttrStmtPoliceTworatePburst,'agentDiffServPolicyAttrStmtRandomdropMinThresh':agentDiffServPolicyAttrStmtRandomdropMinThresh,'agentDiffServPolicyAttrStmtRandomdropMaxThresh':agentDiffServPolicyAttrStmtRandomdropMaxThresh,'agentDiffServPolicyAttrStmtRandomdropMaxDropProb':agentDiffServPolicyAttrStmtRandomdropMaxDropProb,'agentDiffServPolicyAttrStmtRandomdropSamplingRate':agentDiffServPolicyAttrStmtRandomdropSamplingRate,'agentDiffServPolicyAttrStmtRandomdropDecayExponent':agentDiffServPolicyAttrStmtRandomdropDecayExponent,'agentDiffServPolicyAttrStmtShapeAverageCrate':agentDiffServPolicyAttrStmtShapeAverageCrate,'agentDiffServPolicyAttrStmtShapePeakCrate':agentDiffServPolicyAttrStmtShapePeakCrate,'agentDiffServPolicyAttrStmtShapePeakPrate':agentDiffServPolicyAttrStmtShapePeakPrate,'agentDiffServPolicyAttrStorageType':agentDiffServPolicyAttrStorageType,'agentDiffServPolicyAttrRowStatus':agentDiffServPolicyAttrRowStatus,'agentDiffServPolicyPerfInTable':agentDiffServPolicyPerfInTable,'agentDiffServPolicyPerfInEntry':agentDiffServPolicyPerfInEntry,'agentDiffServPolicyPerfInOfferedOctets':agentDiffServPolicyPerfInOfferedOctets,'agentDiffServPolicyPerfInOfferedPackets':agentDiffServPolicyPerfInOfferedPackets,'agentDiffServPolicyPerfInDiscardedOctets':agentDiffServPolicyPerfInDiscardedOctets,'agentDiffServPolicyPerfInDiscardedPackets':agentDiffServPolicyPerfInDiscardedPackets,'agentDiffServPolicyPerfInHCOfferedOctets':agentDiffServPolicyPerfInHCOfferedOctets,'agentDiffServPolicyPerfInHCOfferedPackets':agentDiffServPolicyPerfInHCOfferedPackets,'agentDiffServPolicyPerfInHCDiscardedOctets':agentDiffServPolicyPerfInHCDiscardedOctets,'agentDiffServPolicyPerfInHCDiscardedPackets':agentDiffServPolicyPerfInHCDiscardedPackets,'agentDiffServPolicyPerfInStorageType':agentDiffServPolicyPerfInStorageType,'agentDiffServPolicyPerfInRowStatus':agentDiffServPolicyPerfInRowStatus,'agentDiffServPolicyPerfOutTable':agentDiffServPolicyPerfOutTable,'agentDiffServPolicyPerfOutEntry':agentDiffServPolicyPerfOutEntry,'agentDiffServPolicyPerfOutTailDroppedOctets':agentDiffServPolicyPerfOutTailDroppedOctets,'agentDiffServPolicyPerfOutTailDroppedPackets':agentDiffServPolicyPerfOutTailDroppedPackets,'agentDiffServPolicyPerfOutRandomDroppedOctets':agentDiffServPolicyPerfOutRandomDroppedOctets,'agentDiffServPolicyPerfOutRandomDroppedPackets':agentDiffServPolicyPerfOutRandomDroppedPackets,'agentDiffServPolicyPerfOutShapeDelayedOctets':agentDiffServPolicyPerfOutShapeDelayedOctets,'agentDiffServPolicyPerfOutShapeDelayedPackets':agentDiffServPolicyPerfOutShapeDelayedPackets,'agentDiffServPolicyPerfOutSentOctets':agentDiffServPolicyPerfOutSentOctets,'agentDiffServPolicyPerfOutSentPackets':agentDiffServPolicyPerfOutSentPackets,'agentDiffServPolicyPerfOutHCTailDroppedOctets':agentDiffServPolicyPerfOutHCTailDroppedOctets,'agentDiffServPolicyPerfOutHCTailDroppedPackets':agentDiffServPolicyPerfOutHCTailDroppedPackets,'agentDiffServPolicyPerfOutHCRandomDroppedOctets':agentDiffServPolicyPerfOutHCRandomDroppedOctets,'agentDiffServPolicyPerfOutHCRandomDroppedPackets':agentDiffServPolicyPerfOutHCRandomDroppedPackets,'agentDiffServPolicyPerfOutHCShapeDelayedOctets':agentDiffServPolicyPerfOutHCShapeDelayedOctets,'agentDiffServPolicyPerfOutHCShapeDelayedPackets':agentDiffServPolicyPerfOutHCShapeDelayedPackets,'agentDiffServPolicyPerfOutHCSentOctets':agentDiffServPolicyPerfOutHCSentOctets,'agentDiffServPolicyPerfOutHCSentPackets':agentDiffServPolicyPerfOutHCSentPackets,'agentDiffServPolicyPerfOutStorageType':agentDiffServPolicyPerfOutStorageType,'agentDiffServPolicyPerfOutRowStatus':agentDiffServPolicyPerfOutRowStatus,'agentDiffServServiceGroup':agentDiffServServiceGroup,'agentDiffServServiceTable':agentDiffServServiceTable,'agentDiffServServiceEntry':agentDiffServServiceEntry,_X:agentDiffServServiceIfIndex,_Y:agentDiffServServiceIfDirection,'agentDiffServServicePolicyIndex':agentDiffServServicePolicyIndex,'agentDiffServServiceIfOperStatus':agentDiffServServiceIfOperStatus,'agentDiffServServiceStorageType':agentDiffServServiceStorageType,'agentDiffServServiceRowStatus':agentDiffServServiceRowStatus,'agentDiffServServicePerfTable':agentDiffServServicePerfTable,_Z:agentDiffServServicePerfEntry,'agentDiffServServicePerfOfferedOctets':agentDiffServServicePerfOfferedOctets,'agentDiffServServicePerfOfferedPackets':agentDiffServServicePerfOfferedPackets,'agentDiffServServicePerfDiscardedOctets':agentDiffServServicePerfDiscardedOctets,'agentDiffServServicePerfDiscardedPackets':agentDiffServServicePerfDiscardedPackets,'agentDiffServServicePerfSentOctets':agentDiffServServicePerfSentOctets,'agentDiffServServicePerfSentPackets':agentDiffServServicePerfSentPackets,'agentDiffServServicePerfHCOfferedOctets':agentDiffServServicePerfHCOfferedOctets,'agentDiffServServicePerfHCOfferedPackets':agentDiffServServicePerfHCOfferedPackets,'agentDiffServServicePerfHCDiscardedOctets':agentDiffServServicePerfHCDiscardedOctets,'agentDiffServServicePerfHCDiscardedPackets':agentDiffServServicePerfHCDiscardedPackets,'agentDiffServServicePerfHCSentOctets':agentDiffServServicePerfHCSentOctets,'agentDiffServServicePerfHCSentPackets':agentDiffServServicePerfHCSentPackets})