_A5='l2ConfGroupV10'
_A4='l2PortForwardLastDetectedTime'
_A3='l2PortForwardStatus'
_A2='l2PortForwardDstPort'
_A1='l2PortForwardVlanId'
_A0='l2PortForwardSrcMacAddr'
_z='l2PortForwardDstMacAddr'
_y='l2PortOutFrames'
_x='l2PortInFrames'
_w='l2PortMaxInfo'
_v='l2PortMgmtEntries'
_u='l2PortDstEntries'
_t='l2PortSrcEntries'
_s='l2PortLearnedEntryDiscards'
_r='l2PortDemandAgeCount'
_q='l2PortDemandAgeLowBound'
_p='l2PortDemandAgeHiBound'
_o='l2PortAgingTime'
_n='l2PortAgingStatus'
_m='l2PortSecurityInPorts'
_l='l2PortSecurityVlanId'
_k='l2PortSecurityType'
_j='l2PortSecurityDesc'
_i='l2FilterOutPorts'
_h='l2FilterInPorts'
_g='l2FilterVlanId'
_f='l2FilterDstMacAddr'
_e='l2FilterSrcMacAddr'
_d='l2FilterRestrictions'
_c='l2FilterType'
_b='l2FilterDesc'
_a='l2Priority'
_Z='l2PriorityInPorts'
_Y='l2PriorityVlanId'
_X='l2PrioritySrcMacAddr'
_W='l2PriorityDstMacAddr'
_V='l2PriorityDesc'
_U='l2ForwardInPorts'
_T='l2ForwardDstPort'
_S='l2LearnedFlowEntries'
_R='l2LearnedMacEntries'
_Q='l2LearnedEntryDiscards'
_P='l2PortForwardIndex'
_O='l2PortForwardPort'
_N='l2Port'
_M='l2PortSecurityIndex'
_L='l2FilterIndex'
_K='l2PriorityIndex'
_J='l2ForwardVlanId'
_I='l2ForwardSrcMacAddr'
_H='l2ForwardDstMacAddr'
_G='l2ForwardFilterId'
_F='OctetString'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='CTRON-SSR-L2-MIB'
_A='obsolete'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ssrMibs,=mibBuilder.importSymbols('CTRON-SSR-SMI-MIB','ssrMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
l2MIB=ModuleIdentity((1,3,6,1,4,1,52,2501,1,500))
if mibBuilder.loadTexts:l2MIB.setRevisions(('1999-09-22 00:00',))
_L2Group_ObjectIdentity=ObjectIdentity
l2Group=_L2Group_ObjectIdentity((1,3,6,1,4,1,52,2501,1,2))
_L2LearnedEntryDiscards_Type=Counter32
_L2LearnedEntryDiscards_Object=MibScalar
l2LearnedEntryDiscards=_L2LearnedEntryDiscards_Object((1,3,6,1,4,1,52,2501,1,2,1),_L2LearnedEntryDiscards_Type())
l2LearnedEntryDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:l2LearnedEntryDiscards.setStatus(_A)
_L2LearnedMacEntries_Type=Counter32
_L2LearnedMacEntries_Object=MibScalar
l2LearnedMacEntries=_L2LearnedMacEntries_Object((1,3,6,1,4,1,52,2501,1,2,2),_L2LearnedMacEntries_Type())
l2LearnedMacEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:l2LearnedMacEntries.setStatus(_A)
_L2LearnedFlowEntries_Type=Counter32
_L2LearnedFlowEntries_Object=MibScalar
l2LearnedFlowEntries=_L2LearnedFlowEntries_Object((1,3,6,1,4,1,52,2501,1,2,3),_L2LearnedFlowEntries_Type())
l2LearnedFlowEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:l2LearnedFlowEntries.setStatus(_A)
_L2ForwardTable_Object=MibTable
l2ForwardTable=_L2ForwardTable_Object((1,3,6,1,4,1,52,2501,1,2,4))
if mibBuilder.loadTexts:l2ForwardTable.setStatus(_A)
_L2ForwardEntry_Object=MibTableRow
l2ForwardEntry=_L2ForwardEntry_Object((1,3,6,1,4,1,52,2501,1,2,4,1))
l2ForwardEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:l2ForwardEntry.setStatus(_A)
class _L2ForwardFilterId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_L2ForwardFilterId_Type.__name__=_D
_L2ForwardFilterId_Object=MibTableColumn
l2ForwardFilterId=_L2ForwardFilterId_Object((1,3,6,1,4,1,52,2501,1,2,4,1,1),_L2ForwardFilterId_Type())
l2ForwardFilterId.setMaxAccess(_C)
if mibBuilder.loadTexts:l2ForwardFilterId.setStatus(_A)
_L2ForwardDstMacAddr_Type=PhysAddress
_L2ForwardDstMacAddr_Object=MibTableColumn
l2ForwardDstMacAddr=_L2ForwardDstMacAddr_Object((1,3,6,1,4,1,52,2501,1,2,4,1,2),_L2ForwardDstMacAddr_Type())
l2ForwardDstMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:l2ForwardDstMacAddr.setStatus(_A)
_L2ForwardSrcMacAddr_Type=PhysAddress
_L2ForwardSrcMacAddr_Object=MibTableColumn
l2ForwardSrcMacAddr=_L2ForwardSrcMacAddr_Object((1,3,6,1,4,1,52,2501,1,2,4,1,3),_L2ForwardSrcMacAddr_Type())
l2ForwardSrcMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:l2ForwardSrcMacAddr.setStatus(_A)
class _L2ForwardVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_L2ForwardVlanId_Type.__name__=_D
_L2ForwardVlanId_Object=MibTableColumn
l2ForwardVlanId=_L2ForwardVlanId_Object((1,3,6,1,4,1,52,2501,1,2,4,1,4),_L2ForwardVlanId_Type())
l2ForwardVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:l2ForwardVlanId.setStatus(_A)
class _L2ForwardDstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_L2ForwardDstPort_Type.__name__=_D
_L2ForwardDstPort_Object=MibTableColumn
l2ForwardDstPort=_L2ForwardDstPort_Object((1,3,6,1,4,1,52,2501,1,2,4,1,5),_L2ForwardDstPort_Type())
l2ForwardDstPort.setMaxAccess(_C)
if mibBuilder.loadTexts:l2ForwardDstPort.setStatus(_A)
class _L2ForwardInPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_L2ForwardInPorts_Type.__name__=_F
_L2ForwardInPorts_Object=MibTableColumn
l2ForwardInPorts=_L2ForwardInPorts_Object((1,3,6,1,4,1,52,2501,1,2,4,1,6),_L2ForwardInPorts_Type())
l2ForwardInPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:l2ForwardInPorts.setStatus(_A)
_L2PriorityTable_Object=MibTable
l2PriorityTable=_L2PriorityTable_Object((1,3,6,1,4,1,52,2501,1,2,5))
if mibBuilder.loadTexts:l2PriorityTable.setStatus(_A)
_L2PriorityEntry_Object=MibTableRow
l2PriorityEntry=_L2PriorityEntry_Object((1,3,6,1,4,1,52,2501,1,2,5,1))
l2PriorityEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:l2PriorityEntry.setStatus(_A)
class _L2PriorityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L2PriorityIndex_Type.__name__=_D
_L2PriorityIndex_Object=MibTableColumn
l2PriorityIndex=_L2PriorityIndex_Object((1,3,6,1,4,1,52,2501,1,2,5,1,1),_L2PriorityIndex_Type())
l2PriorityIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:l2PriorityIndex.setStatus(_A)
class _L2PriorityDesc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_L2PriorityDesc_Type.__name__=_F
_L2PriorityDesc_Object=MibTableColumn
l2PriorityDesc=_L2PriorityDesc_Object((1,3,6,1,4,1,52,2501,1,2,5,1,2),_L2PriorityDesc_Type())
l2PriorityDesc.setMaxAccess(_E)
if mibBuilder.loadTexts:l2PriorityDesc.setStatus(_A)
_L2PriorityDstMacAddr_Type=PhysAddress
_L2PriorityDstMacAddr_Object=MibTableColumn
l2PriorityDstMacAddr=_L2PriorityDstMacAddr_Object((1,3,6,1,4,1,52,2501,1,2,5,1,3),_L2PriorityDstMacAddr_Type())
l2PriorityDstMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:l2PriorityDstMacAddr.setStatus(_A)
_L2PrioritySrcMacAddr_Type=PhysAddress
_L2PrioritySrcMacAddr_Object=MibTableColumn
l2PrioritySrcMacAddr=_L2PrioritySrcMacAddr_Object((1,3,6,1,4,1,52,2501,1,2,5,1,4),_L2PrioritySrcMacAddr_Type())
l2PrioritySrcMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:l2PrioritySrcMacAddr.setStatus(_A)
class _L2PriorityVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_L2PriorityVlanId_Type.__name__=_D
_L2PriorityVlanId_Object=MibTableColumn
l2PriorityVlanId=_L2PriorityVlanId_Object((1,3,6,1,4,1,52,2501,1,2,5,1,5),_L2PriorityVlanId_Type())
l2PriorityVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:l2PriorityVlanId.setStatus(_A)
class _L2PriorityInPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_L2PriorityInPorts_Type.__name__=_F
_L2PriorityInPorts_Object=MibTableColumn
l2PriorityInPorts=_L2PriorityInPorts_Object((1,3,6,1,4,1,52,2501,1,2,5,1,6),_L2PriorityInPorts_Type())
l2PriorityInPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:l2PriorityInPorts.setStatus(_A)
class _L2Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('low',1),('medium',2),('high',3),('control',4)))
_L2Priority_Type.__name__=_D
_L2Priority_Object=MibTableColumn
l2Priority=_L2Priority_Object((1,3,6,1,4,1,52,2501,1,2,5,1,7),_L2Priority_Type())
l2Priority.setMaxAccess(_E)
if mibBuilder.loadTexts:l2Priority.setStatus(_A)
_L2FilterTable_Object=MibTable
l2FilterTable=_L2FilterTable_Object((1,3,6,1,4,1,52,2501,1,2,6))
if mibBuilder.loadTexts:l2FilterTable.setStatus(_A)
_L2FilterEntry_Object=MibTableRow
l2FilterEntry=_L2FilterEntry_Object((1,3,6,1,4,1,52,2501,1,2,6,1))
l2FilterEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:l2FilterEntry.setStatus(_A)
class _L2FilterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_L2FilterIndex_Type.__name__=_D
_L2FilterIndex_Object=MibTableColumn
l2FilterIndex=_L2FilterIndex_Object((1,3,6,1,4,1,52,2501,1,2,6,1,1),_L2FilterIndex_Type())
l2FilterIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:l2FilterIndex.setStatus(_A)
class _L2FilterDesc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_L2FilterDesc_Type.__name__=_F
_L2FilterDesc_Object=MibTableColumn
l2FilterDesc=_L2FilterDesc_Object((1,3,6,1,4,1,52,2501,1,2,6,1,2),_L2FilterDesc_Type())
l2FilterDesc.setMaxAccess(_E)
if mibBuilder.loadTexts:l2FilterDesc.setStatus(_A)
class _L2FilterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('staticEntry',1),('addressFilter',2),('addressLock',3)))
_L2FilterType_Type.__name__=_D
_L2FilterType_Object=MibTableColumn
l2FilterType=_L2FilterType_Object((1,3,6,1,4,1,52,2501,1,2,6,1,3),_L2FilterType_Type())
l2FilterType.setMaxAccess(_E)
if mibBuilder.loadTexts:l2FilterType.setStatus(_A)
class _L2FilterRestrictions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('allow',1),('disallow',2),('force',3),('none',4)))
_L2FilterRestrictions_Type.__name__=_D
_L2FilterRestrictions_Object=MibTableColumn
l2FilterRestrictions=_L2FilterRestrictions_Object((1,3,6,1,4,1,52,2501,1,2,6,1,4),_L2FilterRestrictions_Type())
l2FilterRestrictions.setMaxAccess(_E)
if mibBuilder.loadTexts:l2FilterRestrictions.setStatus(_A)
_L2FilterSrcMacAddr_Type=PhysAddress
_L2FilterSrcMacAddr_Object=MibTableColumn
l2FilterSrcMacAddr=_L2FilterSrcMacAddr_Object((1,3,6,1,4,1,52,2501,1,2,6,1,5),_L2FilterSrcMacAddr_Type())
l2FilterSrcMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:l2FilterSrcMacAddr.setStatus(_A)
_L2FilterDstMacAddr_Type=PhysAddress
_L2FilterDstMacAddr_Object=MibTableColumn
l2FilterDstMacAddr=_L2FilterDstMacAddr_Object((1,3,6,1,4,1,52,2501,1,2,6,1,6),_L2FilterDstMacAddr_Type())
l2FilterDstMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:l2FilterDstMacAddr.setStatus(_A)
class _L2FilterVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_L2FilterVlanId_Type.__name__=_D
_L2FilterVlanId_Object=MibTableColumn
l2FilterVlanId=_L2FilterVlanId_Object((1,3,6,1,4,1,52,2501,1,2,6,1,7),_L2FilterVlanId_Type())
l2FilterVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:l2FilterVlanId.setStatus(_A)
class _L2FilterInPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_L2FilterInPorts_Type.__name__=_F
_L2FilterInPorts_Object=MibTableColumn
l2FilterInPorts=_L2FilterInPorts_Object((1,3,6,1,4,1,52,2501,1,2,6,1,8),_L2FilterInPorts_Type())
l2FilterInPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:l2FilterInPorts.setStatus(_A)
class _L2FilterOutPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_L2FilterOutPorts_Type.__name__=_F
_L2FilterOutPorts_Object=MibTableColumn
l2FilterOutPorts=_L2FilterOutPorts_Object((1,3,6,1,4,1,52,2501,1,2,6,1,9),_L2FilterOutPorts_Type())
l2FilterOutPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:l2FilterOutPorts.setStatus(_A)
_L2PortSecurityTable_Object=MibTable
l2PortSecurityTable=_L2PortSecurityTable_Object((1,3,6,1,4,1,52,2501,1,2,7))
if mibBuilder.loadTexts:l2PortSecurityTable.setStatus(_A)
_L2PortSecurityEntry_Object=MibTableRow
l2PortSecurityEntry=_L2PortSecurityEntry_Object((1,3,6,1,4,1,52,2501,1,2,7,1))
l2PortSecurityEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:l2PortSecurityEntry.setStatus(_A)
class _L2PortSecurityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L2PortSecurityIndex_Type.__name__=_D
_L2PortSecurityIndex_Object=MibTableColumn
l2PortSecurityIndex=_L2PortSecurityIndex_Object((1,3,6,1,4,1,52,2501,1,2,7,1,1),_L2PortSecurityIndex_Type())
l2PortSecurityIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:l2PortSecurityIndex.setStatus(_A)
class _L2PortSecurityDesc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_L2PortSecurityDesc_Type.__name__=_F
_L2PortSecurityDesc_Object=MibTableColumn
l2PortSecurityDesc=_L2PortSecurityDesc_Object((1,3,6,1,4,1,52,2501,1,2,7,1,2),_L2PortSecurityDesc_Type())
l2PortSecurityDesc.setMaxAccess(_E)
if mibBuilder.loadTexts:l2PortSecurityDesc.setStatus(_A)
class _L2PortSecurityType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sourceSecure',1),('destinationSecure',2)))
_L2PortSecurityType_Type.__name__=_D
_L2PortSecurityType_Object=MibTableColumn
l2PortSecurityType=_L2PortSecurityType_Object((1,3,6,1,4,1,52,2501,1,2,7,1,3),_L2PortSecurityType_Type())
l2PortSecurityType.setMaxAccess(_E)
if mibBuilder.loadTexts:l2PortSecurityType.setStatus(_A)
class _L2PortSecurityVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_L2PortSecurityVlanId_Type.__name__=_D
_L2PortSecurityVlanId_Object=MibTableColumn
l2PortSecurityVlanId=_L2PortSecurityVlanId_Object((1,3,6,1,4,1,52,2501,1,2,7,1,4),_L2PortSecurityVlanId_Type())
l2PortSecurityVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:l2PortSecurityVlanId.setStatus(_A)
class _L2PortSecurityInPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_L2PortSecurityInPorts_Type.__name__=_F
_L2PortSecurityInPorts_Object=MibTableColumn
l2PortSecurityInPorts=_L2PortSecurityInPorts_Object((1,3,6,1,4,1,52,2501,1,2,7,1,5),_L2PortSecurityInPorts_Type())
l2PortSecurityInPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:l2PortSecurityInPorts.setStatus(_A)
_L2PortTable_Object=MibTable
l2PortTable=_L2PortTable_Object((1,3,6,1,4,1,52,2501,1,2,8))
if mibBuilder.loadTexts:l2PortTable.setStatus(_A)
_L2PortEntry_Object=MibTableRow
l2PortEntry=_L2PortEntry_Object((1,3,6,1,4,1,52,2501,1,2,8,1))
l2PortEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:l2PortEntry.setStatus(_A)
class _L2Port_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_L2Port_Type.__name__=_D
_L2Port_Object=MibTableColumn
l2Port=_L2Port_Object((1,3,6,1,4,1,52,2501,1,2,8,1,1),_L2Port_Type())
l2Port.setMaxAccess(_C)
if mibBuilder.loadTexts:l2Port.setStatus(_A)
class _L2PortAgingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_L2PortAgingStatus_Type.__name__=_D
_L2PortAgingStatus_Object=MibTableColumn
l2PortAgingStatus=_L2PortAgingStatus_Object((1,3,6,1,4,1,52,2501,1,2,8,1,2),_L2PortAgingStatus_Type())
l2PortAgingStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:l2PortAgingStatus.setStatus(_A)
class _L2PortAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,1000000))
_L2PortAgingTime_Type.__name__=_D
_L2PortAgingTime_Object=MibTableColumn
l2PortAgingTime=_L2PortAgingTime_Object((1,3,6,1,4,1,52,2501,1,2,8,1,3),_L2PortAgingTime_Type())
l2PortAgingTime.setMaxAccess(_E)
if mibBuilder.loadTexts:l2PortAgingTime.setStatus(_A)
class _L2PortDemandAgeHiBound_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_L2PortDemandAgeHiBound_Type.__name__=_D
_L2PortDemandAgeHiBound_Object=MibTableColumn
l2PortDemandAgeHiBound=_L2PortDemandAgeHiBound_Object((1,3,6,1,4,1,52,2501,1,2,8,1,4),_L2PortDemandAgeHiBound_Type())
l2PortDemandAgeHiBound.setMaxAccess(_C)
if mibBuilder.loadTexts:l2PortDemandAgeHiBound.setStatus(_A)
class _L2PortDemandAgeLowBound_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_L2PortDemandAgeLowBound_Type.__name__=_D
_L2PortDemandAgeLowBound_Object=MibTableColumn
l2PortDemandAgeLowBound=_L2PortDemandAgeLowBound_Object((1,3,6,1,4,1,52,2501,1,2,8,1,5),_L2PortDemandAgeLowBound_Type())
l2PortDemandAgeLowBound.setMaxAccess(_C)
if mibBuilder.loadTexts:l2PortDemandAgeLowBound.setStatus(_A)
_L2PortDemandAgeCount_Type=Counter32
_L2PortDemandAgeCount_Object=MibTableColumn
l2PortDemandAgeCount=_L2PortDemandAgeCount_Object((1,3,6,1,4,1,52,2501,1,2,8,1,6),_L2PortDemandAgeCount_Type())
l2PortDemandAgeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:l2PortDemandAgeCount.setStatus(_A)
_L2PortLearnedEntryDiscards_Type=Counter32
_L2PortLearnedEntryDiscards_Object=MibTableColumn
l2PortLearnedEntryDiscards=_L2PortLearnedEntryDiscards_Object((1,3,6,1,4,1,52,2501,1,2,8,1,7),_L2PortLearnedEntryDiscards_Type())
l2PortLearnedEntryDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:l2PortLearnedEntryDiscards.setStatus(_A)
_L2PortSrcEntries_Type=Counter32
_L2PortSrcEntries_Object=MibTableColumn
l2PortSrcEntries=_L2PortSrcEntries_Object((1,3,6,1,4,1,52,2501,1,2,8,1,8),_L2PortSrcEntries_Type())
l2PortSrcEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:l2PortSrcEntries.setStatus(_A)
_L2PortDstEntries_Type=Counter32
_L2PortDstEntries_Object=MibTableColumn
l2PortDstEntries=_L2PortDstEntries_Object((1,3,6,1,4,1,52,2501,1,2,8,1,9),_L2PortDstEntries_Type())
l2PortDstEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:l2PortDstEntries.setStatus(_A)
_L2PortMgmtEntries_Type=Counter32
_L2PortMgmtEntries_Object=MibTableColumn
l2PortMgmtEntries=_L2PortMgmtEntries_Object((1,3,6,1,4,1,52,2501,1,2,8,1,10),_L2PortMgmtEntries_Type())
l2PortMgmtEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:l2PortMgmtEntries.setStatus(_A)
class _L2PortMaxInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L2PortMaxInfo_Type.__name__=_D
_L2PortMaxInfo_Object=MibTableColumn
l2PortMaxInfo=_L2PortMaxInfo_Object((1,3,6,1,4,1,52,2501,1,2,8,1,11),_L2PortMaxInfo_Type())
l2PortMaxInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:l2PortMaxInfo.setStatus(_A)
_L2PortInFrames_Type=Counter32
_L2PortInFrames_Object=MibTableColumn
l2PortInFrames=_L2PortInFrames_Object((1,3,6,1,4,1,52,2501,1,2,8,1,12),_L2PortInFrames_Type())
l2PortInFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:l2PortInFrames.setStatus(_A)
_L2PortOutFrames_Type=Counter32
_L2PortOutFrames_Object=MibTableColumn
l2PortOutFrames=_L2PortOutFrames_Object((1,3,6,1,4,1,52,2501,1,2,8,1,13),_L2PortOutFrames_Type())
l2PortOutFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:l2PortOutFrames.setStatus(_A)
_L2PortForwardTable_Object=MibTable
l2PortForwardTable=_L2PortForwardTable_Object((1,3,6,1,4,1,52,2501,1,2,9))
if mibBuilder.loadTexts:l2PortForwardTable.setStatus(_A)
_L2PortForwardEntry_Object=MibTableRow
l2PortForwardEntry=_L2PortForwardEntry_Object((1,3,6,1,4,1,52,2501,1,2,9,1))
l2PortForwardEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:l2PortForwardEntry.setStatus(_A)
class _L2PortForwardPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_L2PortForwardPort_Type.__name__=_D
_L2PortForwardPort_Object=MibTableColumn
l2PortForwardPort=_L2PortForwardPort_Object((1,3,6,1,4,1,52,2501,1,2,9,1,1),_L2PortForwardPort_Type())
l2PortForwardPort.setMaxAccess(_C)
if mibBuilder.loadTexts:l2PortForwardPort.setStatus(_A)
class _L2PortForwardIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L2PortForwardIndex_Type.__name__=_D
_L2PortForwardIndex_Object=MibTableColumn
l2PortForwardIndex=_L2PortForwardIndex_Object((1,3,6,1,4,1,52,2501,1,2,9,1,2),_L2PortForwardIndex_Type())
l2PortForwardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:l2PortForwardIndex.setStatus(_A)
_L2PortForwardDstMacAddr_Type=PhysAddress
_L2PortForwardDstMacAddr_Object=MibTableColumn
l2PortForwardDstMacAddr=_L2PortForwardDstMacAddr_Object((1,3,6,1,4,1,52,2501,1,2,9,1,3),_L2PortForwardDstMacAddr_Type())
l2PortForwardDstMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:l2PortForwardDstMacAddr.setStatus(_A)
_L2PortForwardSrcMacAddr_Type=PhysAddress
_L2PortForwardSrcMacAddr_Object=MibTableColumn
l2PortForwardSrcMacAddr=_L2PortForwardSrcMacAddr_Object((1,3,6,1,4,1,52,2501,1,2,9,1,4),_L2PortForwardSrcMacAddr_Type())
l2PortForwardSrcMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:l2PortForwardSrcMacAddr.setStatus(_A)
class _L2PortForwardVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_L2PortForwardVlanId_Type.__name__=_D
_L2PortForwardVlanId_Object=MibTableColumn
l2PortForwardVlanId=_L2PortForwardVlanId_Object((1,3,6,1,4,1,52,2501,1,2,9,1,5),_L2PortForwardVlanId_Type())
l2PortForwardVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:l2PortForwardVlanId.setStatus(_A)
class _L2PortForwardDstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_L2PortForwardDstPort_Type.__name__=_D
_L2PortForwardDstPort_Object=MibTableColumn
l2PortForwardDstPort=_L2PortForwardDstPort_Object((1,3,6,1,4,1,52,2501,1,2,9,1,6),_L2PortForwardDstPort_Type())
l2PortForwardDstPort.setMaxAccess(_C)
if mibBuilder.loadTexts:l2PortForwardDstPort.setStatus(_A)
class _L2PortForwardStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('invalid',2),('learned',3),('self',4),('mgmt',5)))
_L2PortForwardStatus_Type.__name__=_D
_L2PortForwardStatus_Object=MibTableColumn
l2PortForwardStatus=_L2PortForwardStatus_Object((1,3,6,1,4,1,52,2501,1,2,9,1,7),_L2PortForwardStatus_Type())
l2PortForwardStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:l2PortForwardStatus.setStatus(_A)
_L2PortForwardLastDetectedTime_Type=TimeTicks
_L2PortForwardLastDetectedTime_Object=MibTableColumn
l2PortForwardLastDetectedTime=_L2PortForwardLastDetectedTime_Object((1,3,6,1,4,1,52,2501,1,2,9,1,8),_L2PortForwardLastDetectedTime_Type())
l2PortForwardLastDetectedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:l2PortForwardLastDetectedTime.setStatus(_A)
_L2Conformance_ObjectIdentity=ObjectIdentity
l2Conformance=_L2Conformance_ObjectIdentity((1,3,6,1,4,1,52,2501,1,500,2))
_L2Compliances_ObjectIdentity=ObjectIdentity
l2Compliances=_L2Compliances_ObjectIdentity((1,3,6,1,4,1,52,2501,1,500,2,1))
_L2Groups_ObjectIdentity=ObjectIdentity
l2Groups=_L2Groups_ObjectIdentity((1,3,6,1,4,1,52,2501,1,500,2,2))
l2ConfGroupV10=ObjectGroup((1,3,6,1,4,1,52,2501,1,500,2,2,1))
l2ConfGroupV10.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_T),(_B,_U),(_B,_K),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_L),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_M),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_N),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_O),(_B,_P),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:l2ConfGroupV10.setStatus(_A)
l2ComplianceV10=ModuleCompliance((1,3,6,1,4,1,52,2501,1,500,2,2,1,1))
l2ComplianceV10.setObjects((_B,_A5))
if mibBuilder.loadTexts:l2ComplianceV10.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'l2Group':l2Group,_Q:l2LearnedEntryDiscards,_R:l2LearnedMacEntries,_S:l2LearnedFlowEntries,'l2ForwardTable':l2ForwardTable,'l2ForwardEntry':l2ForwardEntry,_G:l2ForwardFilterId,_H:l2ForwardDstMacAddr,_I:l2ForwardSrcMacAddr,_J:l2ForwardVlanId,_T:l2ForwardDstPort,_U:l2ForwardInPorts,'l2PriorityTable':l2PriorityTable,'l2PriorityEntry':l2PriorityEntry,_K:l2PriorityIndex,_V:l2PriorityDesc,_W:l2PriorityDstMacAddr,_X:l2PrioritySrcMacAddr,_Y:l2PriorityVlanId,_Z:l2PriorityInPorts,_a:l2Priority,'l2FilterTable':l2FilterTable,'l2FilterEntry':l2FilterEntry,_L:l2FilterIndex,_b:l2FilterDesc,_c:l2FilterType,_d:l2FilterRestrictions,_e:l2FilterSrcMacAddr,_f:l2FilterDstMacAddr,_g:l2FilterVlanId,_h:l2FilterInPorts,_i:l2FilterOutPorts,'l2PortSecurityTable':l2PortSecurityTable,'l2PortSecurityEntry':l2PortSecurityEntry,_M:l2PortSecurityIndex,_j:l2PortSecurityDesc,_k:l2PortSecurityType,_l:l2PortSecurityVlanId,_m:l2PortSecurityInPorts,'l2PortTable':l2PortTable,'l2PortEntry':l2PortEntry,_N:l2Port,_n:l2PortAgingStatus,_o:l2PortAgingTime,_p:l2PortDemandAgeHiBound,_q:l2PortDemandAgeLowBound,_r:l2PortDemandAgeCount,_s:l2PortLearnedEntryDiscards,_t:l2PortSrcEntries,_u:l2PortDstEntries,_v:l2PortMgmtEntries,_w:l2PortMaxInfo,_x:l2PortInFrames,_y:l2PortOutFrames,'l2PortForwardTable':l2PortForwardTable,'l2PortForwardEntry':l2PortForwardEntry,_O:l2PortForwardPort,_P:l2PortForwardIndex,_z:l2PortForwardDstMacAddr,_A0:l2PortForwardSrcMacAddr,_A1:l2PortForwardVlanId,_A2:l2PortForwardDstPort,_A3:l2PortForwardStatus,_A4:l2PortForwardLastDetectedTime,'l2MIB':l2MIB,'l2Conformance':l2Conformance,'l2Compliances':l2Compliances,'l2Groups':l2Groups,_A5:l2ConfGroupV10,'l2ComplianceV10':l2ComplianceV10})