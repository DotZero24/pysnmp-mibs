_AS='wwpLeosFlowMacMotionAttrMacAddr'
_AR='wwpLeosFlowMacMotionAttrNewVlan'
_AQ='wwpLeosFlowMacMotionAttrNewPort'
_AP='wwpLeosFlowMacMotionAttrOldVlan'
_AO='wwpLeosFlowMacMotionAttrOldPort'
_AN='wwpLeosFlowPortServiceLevelPort'
_AM='wwpLeosFlowCpuRateLimitStatsClearPort'
_AL='wwpLeosFlowCpuRateLimitStatsPort'
_AK='wwpLeosFlowCpuRateLimitPort'
_AJ='wwpLeosFlowCosMap1dToPCPMapFrom'
_AI='wwpLeosFlowCosMapPCPTo1dMapFrom'
_AH='wwpLeosFlowCos1dToRedCurveOffset1dValue'
_AG='wwpLeosFlowServiceRedCurveIndex'
_AF='wwpLeosFlowCosSyncStdPhbTo1dMapFrom'
_AE='wwpLeosFlowCosSyncIpPrecTo1dMapFrom'
_AD='wwpLeosFlowCosSyncExpTo1dMapFrom'
_AC='wwpLeosFlowCosSync1dToExpMapFrom'
_AB='wwpLeosFlowUserPri'
_AA='wwpLeosFlowMacFindMacAddr'
_A9='wwpLeosFlowMacFindVlanId'
_A8='wwpLeosFlowLearnAddrType'
_A7='wwpLeosFlowLearnSrcPri'
_A6='wwpLeosFlowLearnSrcTag'
_A5='wwpLeosFlowLearnSrcPort'
_A4='wwpLeosFlowLearnAddr'
_A3='wwpLeosFlowLearnVid'
_A2='wwpLeosFlowSMMacAddr'
_A1='wwpLeosFlowSMVid'
_A0='wwpLeosFlowServiceACVid'
_z='wwpLeosFlowServiceACPortId'
_y='disable'
_x='enable'
_w='size4MB'
_v='size2MB'
_u='size1MB'
_t='size512KB'
_s='size256KB'
_r='size0KB'
_q='wwpLeosFlowServiceLevelDirection'
_p='wwpLeosFlowServiceLevelId'
_o='DisplayString'
_n='not-accessible'
_m='drop'
_l='forward'
_k='wwpLeosFlowServiceMapProtocolPortNum'
_j='wwpLeosFlowServiceMapProtocolType'
_i='wwpLeosFlowServiceMapSrcPri'
_h='wwpLeosFlowServiceMapDstTag'
_g='wwpLeosFlowServiceMapDstPort'
_f='wwpLeosFlowServiceMapSrcTag'
_e='wwpLeosFlowServiceMapSrcPort'
_d='wwpLeosFlowServiceMapVid'
_c='wwpLeosFlowSacNetValue'
_b='wwpLeosFlowL2SacNetType'
_a='wwpLeosFlowL2SacPortId'
_Z='wwpLeosFlowSMappingCosValue'
_Y='wwpLeosFlowSMappingCosType'
_X='wwpLeosFlowSMappingDstValue'
_W='wwpLeosFlowSMappingDstType'
_V='wwpLeosFlowSMappingSrcValue'
_U='wwpLeosFlowSMappingSrcType'
_T='wwpLeosFlowSMappingNetValue'
_S='wwpLeosFlowSMappingNetType'
_R='wwpLeosFlowServiceLevelPort'
_Q='TruthValue'
_P='accessible-for-notify'
_O='none'
_N='size128KB'
_M='size64KB'
_L='size32KB'
_K='size16KB'
_J='Unsigned32'
_I='disabled'
_H='enabled'
_G='deprecated'
_F='read-create'
_E='read-write'
_D='WWP-LEOS-FLOW-MIB'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_o,'MacAddress','PhysAddress','RowStatus','TextualConvention',_Q)
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosFlowMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,6))
if mibBuilder.loadTexts:wwpLeosFlowMIB.setRevisions(('2012-03-29 00:00','2011-02-02 00:00','2008-06-16 17:00','2001-04-03 17:00'))
class PriorityMapping(TextualConvention,OctetString):status=_A;displayHint='1x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_WwpLeosFlowMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosFlowMIBObjects=_WwpLeosFlowMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,6,1))
_WwpLeosFlow_ObjectIdentity=ObjectIdentity
wwpLeosFlow=_WwpLeosFlow_ObjectIdentity((1,3,6,1,4,1,6141,2,60,6,1,1))
class _WwpLeosFlowAgeTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000000))
_WwpLeosFlowAgeTime_Type.__name__=_B
_WwpLeosFlowAgeTime_Object=MibScalar
wwpLeosFlowAgeTime=_WwpLeosFlowAgeTime_Object((1,3,6,1,4,1,6141,2,60,6,1,1,1),_WwpLeosFlowAgeTime_Type())
wwpLeosFlowAgeTime.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowAgeTime.setStatus(_A)
class _WwpLeosFlowAgeTimeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_WwpLeosFlowAgeTimeState_Type.__name__=_B
_WwpLeosFlowAgeTimeState_Object=MibScalar
wwpLeosFlowAgeTimeState=_WwpLeosFlowAgeTimeState_Object((1,3,6,1,4,1,6141,2,60,6,1,1,2),_WwpLeosFlowAgeTimeState_Type())
wwpLeosFlowAgeTimeState.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowAgeTimeState.setStatus(_A)
_WwpLeosFlowServiceLevelTable_Object=MibTable
wwpLeosFlowServiceLevelTable=_WwpLeosFlowServiceLevelTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,3))
if mibBuilder.loadTexts:wwpLeosFlowServiceLevelTable.setStatus(_A)
_WwpLeosFlowServiceLevelEntry_Object=MibTableRow
wwpLeosFlowServiceLevelEntry=_WwpLeosFlowServiceLevelEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,3,1))
wwpLeosFlowServiceLevelEntry.setIndexNames((0,_D,_R),(0,_D,_p),(0,_D,_q))
if mibBuilder.loadTexts:wwpLeosFlowServiceLevelEntry.setStatus(_A)
class _WwpLeosFlowServiceLevelDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ingress',1),('egress',2)))
_WwpLeosFlowServiceLevelDirection_Type.__name__=_B
_WwpLeosFlowServiceLevelDirection_Object=MibTableColumn
wwpLeosFlowServiceLevelDirection=_WwpLeosFlowServiceLevelDirection_Object((1,3,6,1,4,1,6141,2,60,6,1,1,3,1,1),_WwpLeosFlowServiceLevelDirection_Type())
wwpLeosFlowServiceLevelDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceLevelDirection.setStatus(_A)
class _WwpLeosFlowServiceLevelPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosFlowServiceLevelPort_Type.__name__=_B
_WwpLeosFlowServiceLevelPort_Object=MibTableColumn
wwpLeosFlowServiceLevelPort=_WwpLeosFlowServiceLevelPort_Object((1,3,6,1,4,1,6141,2,60,6,1,1,3,1,2),_WwpLeosFlowServiceLevelPort_Type())
wwpLeosFlowServiceLevelPort.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceLevelPort.setStatus(_A)
class _WwpLeosFlowServiceLevelId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosFlowServiceLevelId_Type.__name__=_B
_WwpLeosFlowServiceLevelId_Object=MibTableColumn
wwpLeosFlowServiceLevelId=_WwpLeosFlowServiceLevelId_Object((1,3,6,1,4,1,6141,2,60,6,1,1,3,1,3),_WwpLeosFlowServiceLevelId_Type())
wwpLeosFlowServiceLevelId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceLevelId.setStatus(_A)
_WwpLeosFlowServiceLevelName_Type=DisplayString
_WwpLeosFlowServiceLevelName_Object=MibTableColumn
wwpLeosFlowServiceLevelName=_WwpLeosFlowServiceLevelName_Object((1,3,6,1,4,1,6141,2,60,6,1,1,3,1,4),_WwpLeosFlowServiceLevelName_Type())
wwpLeosFlowServiceLevelName.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowServiceLevelName.setStatus(_A)
class _WwpLeosFlowServiceLevelPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosFlowServiceLevelPriority_Type.__name__=_B
_WwpLeosFlowServiceLevelPriority_Object=MibTableColumn
wwpLeosFlowServiceLevelPriority=_WwpLeosFlowServiceLevelPriority_Object((1,3,6,1,4,1,6141,2,60,6,1,1,3,1,5),_WwpLeosFlowServiceLevelPriority_Type())
wwpLeosFlowServiceLevelPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowServiceLevelPriority.setStatus(_A)
class _WwpLeosFlowServiceLevelQueueSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_r,0),('small',1),('medium',2),('large',3),('jumbo',4),('x5',5),('x6',6),('x7',7),('x8',8),(_K,9),(_L,10),(_M,11),(_N,12),(_s,13),(_t,14),(_u,15),(_v,16),(_w,17)))
_WwpLeosFlowServiceLevelQueueSize_Type.__name__=_B
_WwpLeosFlowServiceLevelQueueSize_Object=MibTableColumn
wwpLeosFlowServiceLevelQueueSize=_WwpLeosFlowServiceLevelQueueSize_Object((1,3,6,1,4,1,6141,2,60,6,1,1,3,1,6),_WwpLeosFlowServiceLevelQueueSize_Type())
wwpLeosFlowServiceLevelQueueSize.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowServiceLevelQueueSize.setStatus(_A)
class _WwpLeosFlowServiceLevelDropEligibility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_WwpLeosFlowServiceLevelDropEligibility_Type.__name__=_B
_WwpLeosFlowServiceLevelDropEligibility_Object=MibTableColumn
wwpLeosFlowServiceLevelDropEligibility=_WwpLeosFlowServiceLevelDropEligibility_Object((1,3,6,1,4,1,6141,2,60,6,1,1,3,1,7),_WwpLeosFlowServiceLevelDropEligibility_Type())
wwpLeosFlowServiceLevelDropEligibility.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowServiceLevelDropEligibility.setStatus(_A)
class _WwpLeosFlowServiceLevelShareEligibility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_WwpLeosFlowServiceLevelShareEligibility_Type.__name__=_B
_WwpLeosFlowServiceLevelShareEligibility_Object=MibTableColumn
wwpLeosFlowServiceLevelShareEligibility=_WwpLeosFlowServiceLevelShareEligibility_Object((1,3,6,1,4,1,6141,2,60,6,1,1,3,1,8),_WwpLeosFlowServiceLevelShareEligibility_Type())
wwpLeosFlowServiceLevelShareEligibility.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowServiceLevelShareEligibility.setStatus(_A)
class _WwpLeosFlowServiceLevelCirBW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpLeosFlowServiceLevelCirBW_Type.__name__=_B
_WwpLeosFlowServiceLevelCirBW_Object=MibTableColumn
wwpLeosFlowServiceLevelCirBW=_WwpLeosFlowServiceLevelCirBW_Object((1,3,6,1,4,1,6141,2,60,6,1,1,3,1,9),_WwpLeosFlowServiceLevelCirBW_Type())
wwpLeosFlowServiceLevelCirBW.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowServiceLevelCirBW.setStatus(_A)
class _WwpLeosFlowServiceLevelPirBW_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpLeosFlowServiceLevelPirBW_Type.__name__=_B
_WwpLeosFlowServiceLevelPirBW_Object=MibTableColumn
wwpLeosFlowServiceLevelPirBW=_WwpLeosFlowServiceLevelPirBW_Object((1,3,6,1,4,1,6141,2,60,6,1,1,3,1,10),_WwpLeosFlowServiceLevelPirBW_Type())
wwpLeosFlowServiceLevelPirBW.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowServiceLevelPirBW.setStatus(_A)
_WwpLeosFlowServiceStatus_Type=RowStatus
_WwpLeosFlowServiceStatus_Object=MibTableColumn
wwpLeosFlowServiceStatus=_WwpLeosFlowServiceStatus_Object((1,3,6,1,4,1,6141,2,60,6,1,1,3,1,11),_WwpLeosFlowServiceStatus_Type())
wwpLeosFlowServiceStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowServiceStatus.setStatus(_A)
class _WwpLeosFlowServiceRedCurveId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,64))
_WwpLeosFlowServiceRedCurveId_Type.__name__=_J
_WwpLeosFlowServiceRedCurveId_Object=MibTableColumn
wwpLeosFlowServiceRedCurveId=_WwpLeosFlowServiceRedCurveId_Object((1,3,6,1,4,1,6141,2,60,6,1,1,3,1,12),_WwpLeosFlowServiceRedCurveId_Type())
wwpLeosFlowServiceRedCurveId.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowServiceRedCurveId.setStatus(_A)
class _WwpLeosFlowServiceLevelQueueSizeYellow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4)))
_WwpLeosFlowServiceLevelQueueSizeYellow_Type.__name__=_B
_WwpLeosFlowServiceLevelQueueSizeYellow_Object=MibTableColumn
wwpLeosFlowServiceLevelQueueSizeYellow=_WwpLeosFlowServiceLevelQueueSizeYellow_Object((1,3,6,1,4,1,6141,2,60,6,1,1,3,1,13),_WwpLeosFlowServiceLevelQueueSizeYellow_Type())
wwpLeosFlowServiceLevelQueueSizeYellow.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowServiceLevelQueueSizeYellow.setStatus(_A)
class _WwpLeosFlowServiceLevelQueueSizeRed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4)))
_WwpLeosFlowServiceLevelQueueSizeRed_Type.__name__=_B
_WwpLeosFlowServiceLevelQueueSizeRed_Object=MibTableColumn
wwpLeosFlowServiceLevelQueueSizeRed=_WwpLeosFlowServiceLevelQueueSizeRed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,3,1,14),_WwpLeosFlowServiceLevelQueueSizeRed_Type())
wwpLeosFlowServiceLevelQueueSizeRed.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowServiceLevelQueueSizeRed.setStatus(_A)
class _WwpLeosFlowServiceLevelFlowGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_x,1),(_y,2)))
_WwpLeosFlowServiceLevelFlowGroup_Type.__name__=_B
_WwpLeosFlowServiceLevelFlowGroup_Object=MibTableColumn
wwpLeosFlowServiceLevelFlowGroup=_WwpLeosFlowServiceLevelFlowGroup_Object((1,3,6,1,4,1,6141,2,60,6,1,1,3,1,15),_WwpLeosFlowServiceLevelFlowGroup_Type())
wwpLeosFlowServiceLevelFlowGroup.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowServiceLevelFlowGroup.setStatus(_A)
_WwpLeosFlowServiceMappingTable_Object=MibTable
wwpLeosFlowServiceMappingTable=_WwpLeosFlowServiceMappingTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,4))
if mibBuilder.loadTexts:wwpLeosFlowServiceMappingTable.setStatus(_G)
_WwpLeosFlowServiceMappingEntry_Object=MibTableRow
wwpLeosFlowServiceMappingEntry=_WwpLeosFlowServiceMappingEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,4,1))
wwpLeosFlowServiceMappingEntry.setIndexNames((0,_D,_d),(0,_D,_e),(0,_D,_f),(0,_D,_g),(0,_D,_h),(0,_D,_i),(0,_D,_j),(0,_D,_k))
if mibBuilder.loadTexts:wwpLeosFlowServiceMappingEntry.setStatus(_G)
class _WwpLeosFlowServiceMapVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24576))
_WwpLeosFlowServiceMapVid_Type.__name__=_B
_WwpLeosFlowServiceMapVid_Object=MibTableColumn
wwpLeosFlowServiceMapVid=_WwpLeosFlowServiceMapVid_Object((1,3,6,1,4,1,6141,2,60,6,1,1,4,1,1),_WwpLeosFlowServiceMapVid_Type())
wwpLeosFlowServiceMapVid.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceMapVid.setStatus(_G)
class _WwpLeosFlowServiceMapSrcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosFlowServiceMapSrcPort_Type.__name__=_B
_WwpLeosFlowServiceMapSrcPort_Object=MibTableColumn
wwpLeosFlowServiceMapSrcPort=_WwpLeosFlowServiceMapSrcPort_Object((1,3,6,1,4,1,6141,2,60,6,1,1,4,1,2),_WwpLeosFlowServiceMapSrcPort_Type())
wwpLeosFlowServiceMapSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceMapSrcPort.setStatus(_G)
class _WwpLeosFlowServiceMapSrcTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_WwpLeosFlowServiceMapSrcTag_Type.__name__=_B
_WwpLeosFlowServiceMapSrcTag_Object=MibTableColumn
wwpLeosFlowServiceMapSrcTag=_WwpLeosFlowServiceMapSrcTag_Object((1,3,6,1,4,1,6141,2,60,6,1,1,4,1,3),_WwpLeosFlowServiceMapSrcTag_Type())
wwpLeosFlowServiceMapSrcTag.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceMapSrcTag.setStatus(_G)
class _WwpLeosFlowServiceMapDstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosFlowServiceMapDstPort_Type.__name__=_B
_WwpLeosFlowServiceMapDstPort_Object=MibTableColumn
wwpLeosFlowServiceMapDstPort=_WwpLeosFlowServiceMapDstPort_Object((1,3,6,1,4,1,6141,2,60,6,1,1,4,1,4),_WwpLeosFlowServiceMapDstPort_Type())
wwpLeosFlowServiceMapDstPort.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceMapDstPort.setStatus(_G)
class _WwpLeosFlowServiceMapDstTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_WwpLeosFlowServiceMapDstTag_Type.__name__=_B
_WwpLeosFlowServiceMapDstTag_Object=MibTableColumn
wwpLeosFlowServiceMapDstTag=_WwpLeosFlowServiceMapDstTag_Object((1,3,6,1,4,1,6141,2,60,6,1,1,4,1,5),_WwpLeosFlowServiceMapDstTag_Type())
wwpLeosFlowServiceMapDstTag.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceMapDstTag.setStatus(_G)
class _WwpLeosFlowServiceMapSrcPri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_WwpLeosFlowServiceMapSrcPri_Type.__name__=_B
_WwpLeosFlowServiceMapSrcPri_Object=MibTableColumn
wwpLeosFlowServiceMapSrcPri=_WwpLeosFlowServiceMapSrcPri_Object((1,3,6,1,4,1,6141,2,60,6,1,1,4,1,6),_WwpLeosFlowServiceMapSrcPri_Type())
wwpLeosFlowServiceMapSrcPri.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceMapSrcPri.setStatus(_G)
class _WwpLeosFlowServiceMapProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),('tcp',2),('udp',3)))
_WwpLeosFlowServiceMapProtocolType_Type.__name__=_B
_WwpLeosFlowServiceMapProtocolType_Object=MibTableColumn
wwpLeosFlowServiceMapProtocolType=_WwpLeosFlowServiceMapProtocolType_Object((1,3,6,1,4,1,6141,2,60,6,1,1,4,1,7),_WwpLeosFlowServiceMapProtocolType_Type())
wwpLeosFlowServiceMapProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceMapProtocolType.setStatus(_G)
class _WwpLeosFlowServiceMapProtocolPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosFlowServiceMapProtocolPortNum_Type.__name__=_B
_WwpLeosFlowServiceMapProtocolPortNum_Object=MibTableColumn
wwpLeosFlowServiceMapProtocolPortNum=_WwpLeosFlowServiceMapProtocolPortNum_Object((1,3,6,1,4,1,6141,2,60,6,1,1,4,1,8),_WwpLeosFlowServiceMapProtocolPortNum_Type())
wwpLeosFlowServiceMapProtocolPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceMapProtocolPortNum.setStatus(_G)
class _WwpLeosFlowServiceMapDstSlidId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_WwpLeosFlowServiceMapDstSlidId_Type.__name__=_B
_WwpLeosFlowServiceMapDstSlidId_Object=MibTableColumn
wwpLeosFlowServiceMapDstSlidId=_WwpLeosFlowServiceMapDstSlidId_Object((1,3,6,1,4,1,6141,2,60,6,1,1,4,1,9),_WwpLeosFlowServiceMapDstSlidId_Type())
wwpLeosFlowServiceMapDstSlidId.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowServiceMapDstSlidId.setStatus(_G)
class _WwpLeosFlowServiceMapSrcSlidId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_WwpLeosFlowServiceMapSrcSlidId_Type.__name__=_B
_WwpLeosFlowServiceMapSrcSlidId_Object=MibTableColumn
wwpLeosFlowServiceMapSrcSlidId=_WwpLeosFlowServiceMapSrcSlidId_Object((1,3,6,1,4,1,6141,2,60,6,1,1,4,1,10),_WwpLeosFlowServiceMapSrcSlidId_Type())
wwpLeosFlowServiceMapSrcSlidId.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowServiceMapSrcSlidId.setStatus(_G)
_WwpLeosFlowServiceMapPriRemarkStatus_Type=TruthValue
_WwpLeosFlowServiceMapPriRemarkStatus_Object=MibTableColumn
wwpLeosFlowServiceMapPriRemarkStatus=_WwpLeosFlowServiceMapPriRemarkStatus_Object((1,3,6,1,4,1,6141,2,60,6,1,1,4,1,11),_WwpLeosFlowServiceMapPriRemarkStatus_Type())
wwpLeosFlowServiceMapPriRemarkStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowServiceMapPriRemarkStatus.setStatus(_G)
class _WwpLeosFlowServiceMapRemarkPri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_WwpLeosFlowServiceMapRemarkPri_Type.__name__=_B
_WwpLeosFlowServiceMapRemarkPri_Object=MibTableColumn
wwpLeosFlowServiceMapRemarkPri=_WwpLeosFlowServiceMapRemarkPri_Object((1,3,6,1,4,1,6141,2,60,6,1,1,4,1,12),_WwpLeosFlowServiceMapRemarkPri_Type())
wwpLeosFlowServiceMapRemarkPri.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowServiceMapRemarkPri.setStatus(_G)
_WwpLeosFlowServiceMapStatus_Type=RowStatus
_WwpLeosFlowServiceMapStatus_Object=MibTableColumn
wwpLeosFlowServiceMapStatus=_WwpLeosFlowServiceMapStatus_Object((1,3,6,1,4,1,6141,2,60,6,1,1,4,1,13),_WwpLeosFlowServiceMapStatus_Type())
wwpLeosFlowServiceMapStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowServiceMapStatus.setStatus(_G)
_WwpLeosFlowServiceACTable_Object=MibTable
wwpLeosFlowServiceACTable=_WwpLeosFlowServiceACTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,5))
if mibBuilder.loadTexts:wwpLeosFlowServiceACTable.setStatus(_A)
_WwpLeosFlowServiceACEntry_Object=MibTableRow
wwpLeosFlowServiceACEntry=_WwpLeosFlowServiceACEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,5,1))
wwpLeosFlowServiceACEntry.setIndexNames((0,_D,_z),(0,_D,_A0))
if mibBuilder.loadTexts:wwpLeosFlowServiceACEntry.setStatus(_A)
class _WwpLeosFlowServiceACPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosFlowServiceACPortId_Type.__name__=_B
_WwpLeosFlowServiceACPortId_Object=MibTableColumn
wwpLeosFlowServiceACPortId=_WwpLeosFlowServiceACPortId_Object((1,3,6,1,4,1,6141,2,60,6,1,1,5,1,1),_WwpLeosFlowServiceACPortId_Type())
wwpLeosFlowServiceACPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceACPortId.setStatus(_A)
class _WwpLeosFlowServiceACVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24576))
_WwpLeosFlowServiceACVid_Type.__name__=_B
_WwpLeosFlowServiceACVid_Object=MibTableColumn
wwpLeosFlowServiceACVid=_WwpLeosFlowServiceACVid_Object((1,3,6,1,4,1,6141,2,60,6,1,1,5,1,2),_WwpLeosFlowServiceACVid_Type())
wwpLeosFlowServiceACVid.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceACVid.setStatus(_A)
class _WwpLeosFlowServiceACMaxDynamicMacCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpLeosFlowServiceACMaxDynamicMacCount_Type.__name__=_B
_WwpLeosFlowServiceACMaxDynamicMacCount_Object=MibTableColumn
wwpLeosFlowServiceACMaxDynamicMacCount=_WwpLeosFlowServiceACMaxDynamicMacCount_Object((1,3,6,1,4,1,6141,2,60,6,1,1,5,1,3),_WwpLeosFlowServiceACMaxDynamicMacCount_Type())
wwpLeosFlowServiceACMaxDynamicMacCount.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowServiceACMaxDynamicMacCount.setStatus(_A)
class _WwpLeosFlowServiceACDynamicNonFilteredMacCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpLeosFlowServiceACDynamicNonFilteredMacCount_Type.__name__=_B
_WwpLeosFlowServiceACDynamicNonFilteredMacCount_Object=MibTableColumn
wwpLeosFlowServiceACDynamicNonFilteredMacCount=_WwpLeosFlowServiceACDynamicNonFilteredMacCount_Object((1,3,6,1,4,1,6141,2,60,6,1,1,5,1,4),_WwpLeosFlowServiceACDynamicNonFilteredMacCount_Type())
wwpLeosFlowServiceACDynamicNonFilteredMacCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceACDynamicNonFilteredMacCount.setStatus(_A)
class _WwpLeosFlowServiceACDynamicFilteredMacCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpLeosFlowServiceACDynamicFilteredMacCount_Type.__name__=_B
_WwpLeosFlowServiceACDynamicFilteredMacCount_Object=MibTableColumn
wwpLeosFlowServiceACDynamicFilteredMacCount=_WwpLeosFlowServiceACDynamicFilteredMacCount_Object((1,3,6,1,4,1,6141,2,60,6,1,1,5,1,5),_WwpLeosFlowServiceACDynamicFilteredMacCount_Type())
wwpLeosFlowServiceACDynamicFilteredMacCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceACDynamicFilteredMacCount.setStatus(_A)
_WwpLeosFlowServiceACStatus_Type=RowStatus
_WwpLeosFlowServiceACStatus_Object=MibTableColumn
wwpLeosFlowServiceACStatus=_WwpLeosFlowServiceACStatus_Object((1,3,6,1,4,1,6141,2,60,6,1,1,5,1,7),_WwpLeosFlowServiceACStatus_Type())
wwpLeosFlowServiceACStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowServiceACStatus.setStatus(_A)
class _WwpLeosFlowServiceACForwardLearning_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_WwpLeosFlowServiceACForwardLearning_Type.__name__=_B
_WwpLeosFlowServiceACForwardLearning_Object=MibTableColumn
wwpLeosFlowServiceACForwardLearning=_WwpLeosFlowServiceACForwardLearning_Object((1,3,6,1,4,1,6141,2,60,6,1,1,5,1,50),_WwpLeosFlowServiceACForwardLearning_Type())
wwpLeosFlowServiceACForwardLearning.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowServiceACForwardLearning.setStatus(_A)
_WwpLeosFlowStaticMacTable_Object=MibTable
wwpLeosFlowStaticMacTable=_WwpLeosFlowStaticMacTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,6))
if mibBuilder.loadTexts:wwpLeosFlowStaticMacTable.setStatus(_A)
_WwpLeosFlowStaticMacEntry_Object=MibTableRow
wwpLeosFlowStaticMacEntry=_WwpLeosFlowStaticMacEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,6,1))
wwpLeosFlowStaticMacEntry.setIndexNames((0,_D,_A1),(0,_D,_A2))
if mibBuilder.loadTexts:wwpLeosFlowStaticMacEntry.setStatus(_A)
class _WwpLeosFlowSMVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24576))
_WwpLeosFlowSMVid_Type.__name__=_B
_WwpLeosFlowSMVid_Object=MibTableColumn
wwpLeosFlowSMVid=_WwpLeosFlowSMVid_Object((1,3,6,1,4,1,6141,2,60,6,1,1,6,1,1),_WwpLeosFlowSMVid_Type())
wwpLeosFlowSMVid.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowSMVid.setStatus(_A)
_WwpLeosFlowSMMacAddr_Type=MacAddress
_WwpLeosFlowSMMacAddr_Object=MibTableColumn
wwpLeosFlowSMMacAddr=_WwpLeosFlowSMMacAddr_Object((1,3,6,1,4,1,6141,2,60,6,1,1,6,1,2),_WwpLeosFlowSMMacAddr_Type())
wwpLeosFlowSMMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowSMMacAddr.setStatus(_A)
class _WwpLeosFlowSMPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosFlowSMPortId_Type.__name__=_B
_WwpLeosFlowSMPortId_Object=MibTableColumn
wwpLeosFlowSMPortId=_WwpLeosFlowSMPortId_Object((1,3,6,1,4,1,6141,2,60,6,1,1,6,1,3),_WwpLeosFlowSMPortId_Type())
wwpLeosFlowSMPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowSMPortId.setStatus(_A)
class _WwpLeosFlowSMTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_WwpLeosFlowSMTag_Type.__name__=_B
_WwpLeosFlowSMTag_Object=MibTableColumn
wwpLeosFlowSMTag=_WwpLeosFlowSMTag_Object((1,3,6,1,4,1,6141,2,60,6,1,1,6,1,4),_WwpLeosFlowSMTag_Type())
wwpLeosFlowSMTag.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowSMTag.setStatus(_A)
_WwpLeosFlowSMStatus_Type=RowStatus
_WwpLeosFlowSMStatus_Object=MibTableColumn
wwpLeosFlowSMStatus=_WwpLeosFlowSMStatus_Object((1,3,6,1,4,1,6141,2,60,6,1,1,6,1,5),_WwpLeosFlowSMStatus_Type())
wwpLeosFlowSMStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowSMStatus.setStatus(_A)
_WwpLeosFlowLearnTable_Object=MibTable
wwpLeosFlowLearnTable=_WwpLeosFlowLearnTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,7))
if mibBuilder.loadTexts:wwpLeosFlowLearnTable.setStatus(_A)
_WwpLeosFlowLearnEntry_Object=MibTableRow
wwpLeosFlowLearnEntry=_WwpLeosFlowLearnEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,7,1))
wwpLeosFlowLearnEntry.setIndexNames((0,_D,_A3),(0,_D,_A4),(0,_D,_A5),(0,_D,_A6),(0,_D,_A7),(0,_D,_A8))
if mibBuilder.loadTexts:wwpLeosFlowLearnEntry.setStatus(_A)
class _WwpLeosFlowLearnVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24576))
_WwpLeosFlowLearnVid_Type.__name__=_B
_WwpLeosFlowLearnVid_Object=MibTableColumn
wwpLeosFlowLearnVid=_WwpLeosFlowLearnVid_Object((1,3,6,1,4,1,6141,2,60,6,1,1,7,1,1),_WwpLeosFlowLearnVid_Type())
wwpLeosFlowLearnVid.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowLearnVid.setStatus(_A)
_WwpLeosFlowLearnAddr_Type=MacAddress
_WwpLeosFlowLearnAddr_Object=MibTableColumn
wwpLeosFlowLearnAddr=_WwpLeosFlowLearnAddr_Object((1,3,6,1,4,1,6141,2,60,6,1,1,7,1,2),_WwpLeosFlowLearnAddr_Type())
wwpLeosFlowLearnAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowLearnAddr.setStatus(_A)
class _WwpLeosFlowLearnSrcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosFlowLearnSrcPort_Type.__name__=_B
_WwpLeosFlowLearnSrcPort_Object=MibTableColumn
wwpLeosFlowLearnSrcPort=_WwpLeosFlowLearnSrcPort_Object((1,3,6,1,4,1,6141,2,60,6,1,1,7,1,3),_WwpLeosFlowLearnSrcPort_Type())
wwpLeosFlowLearnSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowLearnSrcPort.setStatus(_A)
class _WwpLeosFlowLearnSrcTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_WwpLeosFlowLearnSrcTag_Type.__name__=_B
_WwpLeosFlowLearnSrcTag_Object=MibTableColumn
wwpLeosFlowLearnSrcTag=_WwpLeosFlowLearnSrcTag_Object((1,3,6,1,4,1,6141,2,60,6,1,1,7,1,4),_WwpLeosFlowLearnSrcTag_Type())
wwpLeosFlowLearnSrcTag.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowLearnSrcTag.setStatus(_A)
class _WwpLeosFlowLearnSrcPri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosFlowLearnSrcPri_Type.__name__=_B
_WwpLeosFlowLearnSrcPri_Object=MibTableColumn
wwpLeosFlowLearnSrcPri=_WwpLeosFlowLearnSrcPri_Object((1,3,6,1,4,1,6141,2,60,6,1,1,7,1,5),_WwpLeosFlowLearnSrcPri_Type())
wwpLeosFlowLearnSrcPri.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowLearnSrcPri.setStatus(_A)
class _WwpLeosFlowLearnAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('layer2',1),('layer3',2)))
_WwpLeosFlowLearnAddrType_Type.__name__=_B
_WwpLeosFlowLearnAddrType_Object=MibTableColumn
wwpLeosFlowLearnAddrType=_WwpLeosFlowLearnAddrType_Object((1,3,6,1,4,1,6141,2,60,6,1,1,7,1,6),_WwpLeosFlowLearnAddrType_Type())
wwpLeosFlowLearnAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowLearnAddrType.setStatus(_A)
class _WwpLeosFlowLearnDstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosFlowLearnDstPort_Type.__name__=_B
_WwpLeosFlowLearnDstPort_Object=MibTableColumn
wwpLeosFlowLearnDstPort=_WwpLeosFlowLearnDstPort_Object((1,3,6,1,4,1,6141,2,60,6,1,1,7,1,7),_WwpLeosFlowLearnDstPort_Type())
wwpLeosFlowLearnDstPort.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowLearnDstPort.setStatus(_A)
class _WwpLeosFlowLearnDstTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_WwpLeosFlowLearnDstTag_Type.__name__=_B
_WwpLeosFlowLearnDstTag_Object=MibTableColumn
wwpLeosFlowLearnDstTag=_WwpLeosFlowLearnDstTag_Object((1,3,6,1,4,1,6141,2,60,6,1,1,7,1,8),_WwpLeosFlowLearnDstTag_Type())
wwpLeosFlowLearnDstTag.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowLearnDstTag.setStatus(_A)
class _WwpLeosFlowLearnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dynamic',1),('static',2)))
_WwpLeosFlowLearnType_Type.__name__=_B
_WwpLeosFlowLearnType_Object=MibTableColumn
wwpLeosFlowLearnType=_WwpLeosFlowLearnType_Object((1,3,6,1,4,1,6141,2,60,6,1,1,7,1,9),_WwpLeosFlowLearnType_Type())
wwpLeosFlowLearnType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowLearnType.setStatus(_A)
_WwpLeosFlowLearnIsFiltered_Type=TruthValue
_WwpLeosFlowLearnIsFiltered_Object=MibTableColumn
wwpLeosFlowLearnIsFiltered=_WwpLeosFlowLearnIsFiltered_Object((1,3,6,1,4,1,6141,2,60,6,1,1,7,1,10),_WwpLeosFlowLearnIsFiltered_Type())
wwpLeosFlowLearnIsFiltered.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowLearnIsFiltered.setStatus(_A)
_WwpLeosFlowServiceStatsTable_Object=MibTable
wwpLeosFlowServiceStatsTable=_WwpLeosFlowServiceStatsTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,8))
if mibBuilder.loadTexts:wwpLeosFlowServiceStatsTable.setStatus(_G)
_WwpLeosFlowServiceStatsEntry_Object=MibTableRow
wwpLeosFlowServiceStatsEntry=_WwpLeosFlowServiceStatsEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,8,1))
wwpLeosFlowServiceStatsEntry.setIndexNames((0,_D,_d),(0,_D,_e),(0,_D,_f),(0,_D,_g),(0,_D,_h),(0,_D,_i),(0,_D,_j),(0,_D,_k))
if mibBuilder.loadTexts:wwpLeosFlowServiceStatsEntry.setStatus(_G)
_WwpLeosFlowServiceStatsRxHi_Type=Counter32
_WwpLeosFlowServiceStatsRxHi_Object=MibTableColumn
wwpLeosFlowServiceStatsRxHi=_WwpLeosFlowServiceStatsRxHi_Object((1,3,6,1,4,1,6141,2,60,6,1,1,8,1,1),_WwpLeosFlowServiceStatsRxHi_Type())
wwpLeosFlowServiceStatsRxHi.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceStatsRxHi.setStatus(_G)
_WwpLeosFlowServiceStatsRxLo_Type=Counter32
_WwpLeosFlowServiceStatsRxLo_Object=MibTableColumn
wwpLeosFlowServiceStatsRxLo=_WwpLeosFlowServiceStatsRxLo_Object((1,3,6,1,4,1,6141,2,60,6,1,1,8,1,2),_WwpLeosFlowServiceStatsRxLo_Type())
wwpLeosFlowServiceStatsRxLo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceStatsRxLo.setStatus(_G)
_WwpLeosFlowServiceStatsTxHi_Type=Counter32
_WwpLeosFlowServiceStatsTxHi_Object=MibTableColumn
wwpLeosFlowServiceStatsTxHi=_WwpLeosFlowServiceStatsTxHi_Object((1,3,6,1,4,1,6141,2,60,6,1,1,8,1,3),_WwpLeosFlowServiceStatsTxHi_Type())
wwpLeosFlowServiceStatsTxHi.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceStatsTxHi.setStatus(_G)
_WwpLeosFlowServiceStatsTxLo_Type=Counter32
_WwpLeosFlowServiceStatsTxLo_Object=MibTableColumn
wwpLeosFlowServiceStatsTxLo=_WwpLeosFlowServiceStatsTxLo_Object((1,3,6,1,4,1,6141,2,60,6,1,1,8,1,4),_WwpLeosFlowServiceStatsTxLo_Type())
wwpLeosFlowServiceStatsTxLo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceStatsTxLo.setStatus(_G)
class _WwpLeosFlowServiceStatsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_WwpLeosFlowServiceStatsType_Type.__name__=_B
_WwpLeosFlowServiceStatsType_Object=MibTableColumn
wwpLeosFlowServiceStatsType=_WwpLeosFlowServiceStatsType_Object((1,3,6,1,4,1,6141,2,60,6,1,1,8,1,5),_WwpLeosFlowServiceStatsType_Type())
wwpLeosFlowServiceStatsType.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowServiceStatsType.setStatus(_G)
_WwpLeosFlowMacFindTable_Object=MibTable
wwpLeosFlowMacFindTable=_WwpLeosFlowMacFindTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,9))
if mibBuilder.loadTexts:wwpLeosFlowMacFindTable.setStatus(_A)
_WwpLeosFlowMacFindEntry_Object=MibTableRow
wwpLeosFlowMacFindEntry=_WwpLeosFlowMacFindEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,9,1))
wwpLeosFlowMacFindEntry.setIndexNames((0,_D,_A9),(0,_D,_AA))
if mibBuilder.loadTexts:wwpLeosFlowMacFindEntry.setStatus(_A)
_WwpLeosFlowMacFindMacAddr_Type=MacAddress
_WwpLeosFlowMacFindMacAddr_Object=MibTableColumn
wwpLeosFlowMacFindMacAddr=_WwpLeosFlowMacFindMacAddr_Object((1,3,6,1,4,1,6141,2,60,6,1,1,9,1,1),_WwpLeosFlowMacFindMacAddr_Type())
wwpLeosFlowMacFindMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowMacFindMacAddr.setStatus(_A)
class _WwpLeosFlowMacFindVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24576))
_WwpLeosFlowMacFindVlanId_Type.__name__=_B
_WwpLeosFlowMacFindVlanId_Object=MibTableColumn
wwpLeosFlowMacFindVlanId=_WwpLeosFlowMacFindVlanId_Object((1,3,6,1,4,1,6141,2,60,6,1,1,9,1,2),_WwpLeosFlowMacFindVlanId_Type())
wwpLeosFlowMacFindVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowMacFindVlanId.setStatus(_A)
class _WwpLeosFlowMacFindPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosFlowMacFindPort_Type.__name__=_B
_WwpLeosFlowMacFindPort_Object=MibTableColumn
wwpLeosFlowMacFindPort=_WwpLeosFlowMacFindPort_Object((1,3,6,1,4,1,6141,2,60,6,1,1,9,1,3),_WwpLeosFlowMacFindPort_Type())
wwpLeosFlowMacFindPort.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowMacFindPort.setStatus(_A)
class _WwpLeosFlowMacFindVlanTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24576))
_WwpLeosFlowMacFindVlanTag_Type.__name__=_B
_WwpLeosFlowMacFindVlanTag_Object=MibTableColumn
wwpLeosFlowMacFindVlanTag=_WwpLeosFlowMacFindVlanTag_Object((1,3,6,1,4,1,6141,2,60,6,1,1,9,1,4),_WwpLeosFlowMacFindVlanTag_Type())
wwpLeosFlowMacFindVlanTag.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowMacFindVlanTag.setStatus(_A)
_WwpLeosFlowPriRemapTable_Object=MibTable
wwpLeosFlowPriRemapTable=_WwpLeosFlowPriRemapTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,10))
if mibBuilder.loadTexts:wwpLeosFlowPriRemapTable.setStatus(_A)
_WwpLeosFlowPriRemapEntry_Object=MibTableRow
wwpLeosFlowPriRemapEntry=_WwpLeosFlowPriRemapEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,10,1))
wwpLeosFlowPriRemapEntry.setIndexNames((0,_D,_AB))
if mibBuilder.loadTexts:wwpLeosFlowPriRemapEntry.setStatus(_A)
class _WwpLeosFlowUserPri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosFlowUserPri_Type.__name__=_B
_WwpLeosFlowUserPri_Object=MibTableColumn
wwpLeosFlowUserPri=_WwpLeosFlowUserPri_Object((1,3,6,1,4,1,6141,2,60,6,1,1,10,1,1),_WwpLeosFlowUserPri_Type())
wwpLeosFlowUserPri.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowUserPri.setStatus(_A)
class _WwpLeosFlowRemappedPri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosFlowRemappedPri_Type.__name__=_B
_WwpLeosFlowRemappedPri_Object=MibTableColumn
wwpLeosFlowRemappedPri=_WwpLeosFlowRemappedPri_Object((1,3,6,1,4,1,6141,2,60,6,1,1,10,1,2),_WwpLeosFlowRemappedPri_Type())
wwpLeosFlowRemappedPri.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowRemappedPri.setStatus(_A)
_WwpLeosFlowSMappingTable_Object=MibTable
wwpLeosFlowSMappingTable=_WwpLeosFlowSMappingTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,13))
if mibBuilder.loadTexts:wwpLeosFlowSMappingTable.setStatus(_A)
_WwpLeosFlowSMappingEntry_Object=MibTableRow
wwpLeosFlowSMappingEntry=_WwpLeosFlowSMappingEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,13,1))
wwpLeosFlowSMappingEntry.setIndexNames((0,_D,_S),(0,_D,_T),(0,_D,_U),(0,_D,_V),(0,_D,_W),(0,_D,_X),(0,_D,_Y),(0,_D,_Z))
if mibBuilder.loadTexts:wwpLeosFlowSMappingEntry.setStatus(_A)
class _WwpLeosFlowSMappingNetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),('vlan',2),('vsi',3),('vsiMpls',4)))
_WwpLeosFlowSMappingNetType_Type.__name__=_B
_WwpLeosFlowSMappingNetType_Object=MibTableColumn
wwpLeosFlowSMappingNetType=_WwpLeosFlowSMappingNetType_Object((1,3,6,1,4,1,6141,2,60,6,1,1,13,1,1),_WwpLeosFlowSMappingNetType_Type())
wwpLeosFlowSMappingNetType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowSMappingNetType.setStatus(_A)
_WwpLeosFlowSMappingNetValue_Type=Unsigned32
_WwpLeosFlowSMappingNetValue_Object=MibTableColumn
wwpLeosFlowSMappingNetValue=_WwpLeosFlowSMappingNetValue_Object((1,3,6,1,4,1,6141,2,60,6,1,1,13,1,2),_WwpLeosFlowSMappingNetValue_Type())
wwpLeosFlowSMappingNetValue.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowSMappingNetValue.setStatus(_A)
class _WwpLeosFlowSMappingSrcType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),('port',2),('mplsVc',3)))
_WwpLeosFlowSMappingSrcType_Type.__name__=_B
_WwpLeosFlowSMappingSrcType_Object=MibTableColumn
wwpLeosFlowSMappingSrcType=_WwpLeosFlowSMappingSrcType_Object((1,3,6,1,4,1,6141,2,60,6,1,1,13,1,3),_WwpLeosFlowSMappingSrcType_Type())
wwpLeosFlowSMappingSrcType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowSMappingSrcType.setStatus(_A)
_WwpLeosFlowSMappingSrcValue_Type=Unsigned32
_WwpLeosFlowSMappingSrcValue_Object=MibTableColumn
wwpLeosFlowSMappingSrcValue=_WwpLeosFlowSMappingSrcValue_Object((1,3,6,1,4,1,6141,2,60,6,1,1,13,1,4),_WwpLeosFlowSMappingSrcValue_Type())
wwpLeosFlowSMappingSrcValue.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowSMappingSrcValue.setStatus(_A)
class _WwpLeosFlowSMappingDstType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),('port',2),('mplsVc',3)))
_WwpLeosFlowSMappingDstType_Type.__name__=_B
_WwpLeosFlowSMappingDstType_Object=MibTableColumn
wwpLeosFlowSMappingDstType=_WwpLeosFlowSMappingDstType_Object((1,3,6,1,4,1,6141,2,60,6,1,1,13,1,5),_WwpLeosFlowSMappingDstType_Type())
wwpLeosFlowSMappingDstType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowSMappingDstType.setStatus(_A)
_WwpLeosFlowSMappingDstValue_Type=Unsigned32
_WwpLeosFlowSMappingDstValue_Object=MibTableColumn
wwpLeosFlowSMappingDstValue=_WwpLeosFlowSMappingDstValue_Object((1,3,6,1,4,1,6141,2,60,6,1,1,13,1,6),_WwpLeosFlowSMappingDstValue_Type())
wwpLeosFlowSMappingDstValue.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowSMappingDstValue.setStatus(_A)
class _WwpLeosFlowSMappingCosType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_O,1),('phb',2),('dscp',3),('ipPrec',4),('dot1dPri',5),('mplsExp',6),('tcpSrcPort',7),('tcpDstPort',8),('udpSrcPort',9),('udpDstPort',10),('pcp',11),('cvlan',12)))
_WwpLeosFlowSMappingCosType_Type.__name__=_B
_WwpLeosFlowSMappingCosType_Object=MibTableColumn
wwpLeosFlowSMappingCosType=_WwpLeosFlowSMappingCosType_Object((1,3,6,1,4,1,6141,2,60,6,1,1,13,1,7),_WwpLeosFlowSMappingCosType_Type())
wwpLeosFlowSMappingCosType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowSMappingCosType.setStatus(_A)
_WwpLeosFlowSMappingCosValue_Type=Unsigned32
_WwpLeosFlowSMappingCosValue_Object=MibTableColumn
wwpLeosFlowSMappingCosValue=_WwpLeosFlowSMappingCosValue_Object((1,3,6,1,4,1,6141,2,60,6,1,1,13,1,8),_WwpLeosFlowSMappingCosValue_Type())
wwpLeosFlowSMappingCosValue.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowSMappingCosValue.setStatus(_A)
_WwpLeosFlowSMappingDstSlid_Type=Unsigned32
_WwpLeosFlowSMappingDstSlid_Object=MibTableColumn
wwpLeosFlowSMappingDstSlid=_WwpLeosFlowSMappingDstSlid_Object((1,3,6,1,4,1,6141,2,60,6,1,1,13,1,9),_WwpLeosFlowSMappingDstSlid_Type())
wwpLeosFlowSMappingDstSlid.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowSMappingDstSlid.setStatus(_A)
_WwpLeosFlowSMappingSrcSlid_Type=Unsigned32
_WwpLeosFlowSMappingSrcSlid_Object=MibTableColumn
wwpLeosFlowSMappingSrcSlid=_WwpLeosFlowSMappingSrcSlid_Object((1,3,6,1,4,1,6141,2,60,6,1,1,13,1,10),_WwpLeosFlowSMappingSrcSlid_Type())
wwpLeosFlowSMappingSrcSlid.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowSMappingSrcSlid.setStatus(_A)
_WwpLeosFlowSMappingStatus_Type=RowStatus
_WwpLeosFlowSMappingStatus_Object=MibTableColumn
wwpLeosFlowSMappingStatus=_WwpLeosFlowSMappingStatus_Object((1,3,6,1,4,1,6141,2,60,6,1,1,13,1,11),_WwpLeosFlowSMappingStatus_Type())
wwpLeosFlowSMappingStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowSMappingStatus.setStatus(_A)
class _WwpLeosFlowSMappingRedCurveOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_WwpLeosFlowSMappingRedCurveOffset_Type.__name__=_B
_WwpLeosFlowSMappingRedCurveOffset_Object=MibTableColumn
wwpLeosFlowSMappingRedCurveOffset=_WwpLeosFlowSMappingRedCurveOffset_Object((1,3,6,1,4,1,6141,2,60,6,1,1,13,1,12),_WwpLeosFlowSMappingRedCurveOffset_Type())
wwpLeosFlowSMappingRedCurveOffset.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowSMappingRedCurveOffset.setStatus(_A)
class _WwpLeosFlowSMappingCpuPort_Type(TruthValue):defaultValue=2
_WwpLeosFlowSMappingCpuPort_Type.__name__=_Q
_WwpLeosFlowSMappingCpuPort_Object=MibTableColumn
wwpLeosFlowSMappingCpuPort=_WwpLeosFlowSMappingCpuPort_Object((1,3,6,1,4,1,6141,2,60,6,1,1,13,1,13),_WwpLeosFlowSMappingCpuPort_Type())
wwpLeosFlowSMappingCpuPort.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowSMappingCpuPort.setStatus(_A)
_WwpLeosFlowSMappingStatsTable_Object=MibTable
wwpLeosFlowSMappingStatsTable=_WwpLeosFlowSMappingStatsTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,14))
if mibBuilder.loadTexts:wwpLeosFlowSMappingStatsTable.setStatus(_A)
_WwpLeosFlowSMappingStatsEntry_Object=MibTableRow
wwpLeosFlowSMappingStatsEntry=_WwpLeosFlowSMappingStatsEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,14,1))
wwpLeosFlowSMappingStatsEntry.setIndexNames((0,_D,_S),(0,_D,_T),(0,_D,_U),(0,_D,_V),(0,_D,_W),(0,_D,_X),(0,_D,_Y),(0,_D,_Z))
if mibBuilder.loadTexts:wwpLeosFlowSMappingStatsEntry.setStatus(_A)
_WwpLeosFlowSMappingStatsRxHi_Type=Counter32
_WwpLeosFlowSMappingStatsRxHi_Object=MibTableColumn
wwpLeosFlowSMappingStatsRxHi=_WwpLeosFlowSMappingStatsRxHi_Object((1,3,6,1,4,1,6141,2,60,6,1,1,14,1,1),_WwpLeosFlowSMappingStatsRxHi_Type())
wwpLeosFlowSMappingStatsRxHi.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowSMappingStatsRxHi.setStatus(_A)
_WwpLeosFlowSMappingStatsRxLo_Type=Counter32
_WwpLeosFlowSMappingStatsRxLo_Object=MibTableColumn
wwpLeosFlowSMappingStatsRxLo=_WwpLeosFlowSMappingStatsRxLo_Object((1,3,6,1,4,1,6141,2,60,6,1,1,14,1,2),_WwpLeosFlowSMappingStatsRxLo_Type())
wwpLeosFlowSMappingStatsRxLo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowSMappingStatsRxLo.setStatus(_A)
_WwpLeosFlowSMappingStatsTxHi_Type=Counter32
_WwpLeosFlowSMappingStatsTxHi_Object=MibTableColumn
wwpLeosFlowSMappingStatsTxHi=_WwpLeosFlowSMappingStatsTxHi_Object((1,3,6,1,4,1,6141,2,60,6,1,1,14,1,3),_WwpLeosFlowSMappingStatsTxHi_Type())
wwpLeosFlowSMappingStatsTxHi.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowSMappingStatsTxHi.setStatus(_A)
_WwpLeosFlowSMappingStatsTxLo_Type=Counter32
_WwpLeosFlowSMappingStatsTxLo_Object=MibTableColumn
wwpLeosFlowSMappingStatsTxLo=_WwpLeosFlowSMappingStatsTxLo_Object((1,3,6,1,4,1,6141,2,60,6,1,1,14,1,4),_WwpLeosFlowSMappingStatsTxLo_Type())
wwpLeosFlowSMappingStatsTxLo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowSMappingStatsTxLo.setStatus(_A)
class _WwpLeosFlowSMappingStatsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_WwpLeosFlowSMappingStatsType_Type.__name__=_B
_WwpLeosFlowSMappingStatsType_Object=MibTableColumn
wwpLeosFlowSMappingStatsType=_WwpLeosFlowSMappingStatsType_Object((1,3,6,1,4,1,6141,2,60,6,1,1,14,1,5),_WwpLeosFlowSMappingStatsType_Type())
wwpLeosFlowSMappingStatsType.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowSMappingStatsType.setStatus(_A)
_WwpLeosFlowCosSync1dToExpTable_Object=MibTable
wwpLeosFlowCosSync1dToExpTable=_WwpLeosFlowCosSync1dToExpTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,15))
if mibBuilder.loadTexts:wwpLeosFlowCosSync1dToExpTable.setStatus(_A)
_WwpLeosFlowCosSync1dToExpEntry_Object=MibTableRow
wwpLeosFlowCosSync1dToExpEntry=_WwpLeosFlowCosSync1dToExpEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,15,1))
wwpLeosFlowCosSync1dToExpEntry.setIndexNames((0,_D,_AC))
if mibBuilder.loadTexts:wwpLeosFlowCosSync1dToExpEntry.setStatus(_A)
class _WwpLeosFlowCosSync1dToExpMapFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosFlowCosSync1dToExpMapFrom_Type.__name__=_B
_WwpLeosFlowCosSync1dToExpMapFrom_Object=MibTableColumn
wwpLeosFlowCosSync1dToExpMapFrom=_WwpLeosFlowCosSync1dToExpMapFrom_Object((1,3,6,1,4,1,6141,2,60,6,1,1,15,1,1),_WwpLeosFlowCosSync1dToExpMapFrom_Type())
wwpLeosFlowCosSync1dToExpMapFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCosSync1dToExpMapFrom.setStatus(_A)
class _WwpLeosFlowCosSync1dToExpMapTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosFlowCosSync1dToExpMapTo_Type.__name__=_B
_WwpLeosFlowCosSync1dToExpMapTo_Object=MibTableColumn
wwpLeosFlowCosSync1dToExpMapTo=_WwpLeosFlowCosSync1dToExpMapTo_Object((1,3,6,1,4,1,6141,2,60,6,1,1,15,1,2),_WwpLeosFlowCosSync1dToExpMapTo_Type())
wwpLeosFlowCosSync1dToExpMapTo.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCosSync1dToExpMapTo.setStatus(_A)
_WwpLeosFlowCosSyncExpTo1dTable_Object=MibTable
wwpLeosFlowCosSyncExpTo1dTable=_WwpLeosFlowCosSyncExpTo1dTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,16))
if mibBuilder.loadTexts:wwpLeosFlowCosSyncExpTo1dTable.setStatus(_A)
_WwpLeosFlowCosSyncExpTo1dEntry_Object=MibTableRow
wwpLeosFlowCosSyncExpTo1dEntry=_WwpLeosFlowCosSyncExpTo1dEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,16,1))
wwpLeosFlowCosSyncExpTo1dEntry.setIndexNames((0,_D,_AD))
if mibBuilder.loadTexts:wwpLeosFlowCosSyncExpTo1dEntry.setStatus(_A)
class _WwpLeosFlowCosSyncExpTo1dMapFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosFlowCosSyncExpTo1dMapFrom_Type.__name__=_B
_WwpLeosFlowCosSyncExpTo1dMapFrom_Object=MibTableColumn
wwpLeosFlowCosSyncExpTo1dMapFrom=_WwpLeosFlowCosSyncExpTo1dMapFrom_Object((1,3,6,1,4,1,6141,2,60,6,1,1,16,1,1),_WwpLeosFlowCosSyncExpTo1dMapFrom_Type())
wwpLeosFlowCosSyncExpTo1dMapFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCosSyncExpTo1dMapFrom.setStatus(_A)
class _WwpLeosFlowCosSyncExpTo1dMapTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosFlowCosSyncExpTo1dMapTo_Type.__name__=_B
_WwpLeosFlowCosSyncExpTo1dMapTo_Object=MibTableColumn
wwpLeosFlowCosSyncExpTo1dMapTo=_WwpLeosFlowCosSyncExpTo1dMapTo_Object((1,3,6,1,4,1,6141,2,60,6,1,1,16,1,2),_WwpLeosFlowCosSyncExpTo1dMapTo_Type())
wwpLeosFlowCosSyncExpTo1dMapTo.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCosSyncExpTo1dMapTo.setStatus(_A)
_WwpLeosFlowCosSyncIpPrecTo1dTable_Object=MibTable
wwpLeosFlowCosSyncIpPrecTo1dTable=_WwpLeosFlowCosSyncIpPrecTo1dTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,17))
if mibBuilder.loadTexts:wwpLeosFlowCosSyncIpPrecTo1dTable.setStatus(_A)
_WwpLeosFlowCosSyncIpPrecTo1dEntry_Object=MibTableRow
wwpLeosFlowCosSyncIpPrecTo1dEntry=_WwpLeosFlowCosSyncIpPrecTo1dEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,17,1))
wwpLeosFlowCosSyncIpPrecTo1dEntry.setIndexNames((0,_D,_AE))
if mibBuilder.loadTexts:wwpLeosFlowCosSyncIpPrecTo1dEntry.setStatus(_A)
class _WwpLeosFlowCosSyncIpPrecTo1dMapFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosFlowCosSyncIpPrecTo1dMapFrom_Type.__name__=_B
_WwpLeosFlowCosSyncIpPrecTo1dMapFrom_Object=MibTableColumn
wwpLeosFlowCosSyncIpPrecTo1dMapFrom=_WwpLeosFlowCosSyncIpPrecTo1dMapFrom_Object((1,3,6,1,4,1,6141,2,60,6,1,1,17,1,1),_WwpLeosFlowCosSyncIpPrecTo1dMapFrom_Type())
wwpLeosFlowCosSyncIpPrecTo1dMapFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCosSyncIpPrecTo1dMapFrom.setStatus(_A)
class _WwpLeosFlowCosSyncIpPrecTo1dMapTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosFlowCosSyncIpPrecTo1dMapTo_Type.__name__=_B
_WwpLeosFlowCosSyncIpPrecTo1dMapTo_Object=MibTableColumn
wwpLeosFlowCosSyncIpPrecTo1dMapTo=_WwpLeosFlowCosSyncIpPrecTo1dMapTo_Object((1,3,6,1,4,1,6141,2,60,6,1,1,17,1,2),_WwpLeosFlowCosSyncIpPrecTo1dMapTo_Type())
wwpLeosFlowCosSyncIpPrecTo1dMapTo.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCosSyncIpPrecTo1dMapTo.setStatus(_A)
_WwpLeosFlowCosSyncStdPhbTo1dTable_Object=MibTable
wwpLeosFlowCosSyncStdPhbTo1dTable=_WwpLeosFlowCosSyncStdPhbTo1dTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,18))
if mibBuilder.loadTexts:wwpLeosFlowCosSyncStdPhbTo1dTable.setStatus(_A)
_WwpLeosFlowCosSyncStdPhbTo1dEntry_Object=MibTableRow
wwpLeosFlowCosSyncStdPhbTo1dEntry=_WwpLeosFlowCosSyncStdPhbTo1dEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,18,1))
wwpLeosFlowCosSyncStdPhbTo1dEntry.setIndexNames((0,_D,_AF))
if mibBuilder.loadTexts:wwpLeosFlowCosSyncStdPhbTo1dEntry.setStatus(_A)
class _WwpLeosFlowCosSyncStdPhbTo1dMapFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('cs0',1),('cs1',2),('cs2',3),('cs3',4),('cs4',5),('cs5',6),('cs6',7),('cs7',8),('af1',9),('af2',10),('af3',11),('af4',12),('ef',13)))
_WwpLeosFlowCosSyncStdPhbTo1dMapFrom_Type.__name__=_B
_WwpLeosFlowCosSyncStdPhbTo1dMapFrom_Object=MibTableColumn
wwpLeosFlowCosSyncStdPhbTo1dMapFrom=_WwpLeosFlowCosSyncStdPhbTo1dMapFrom_Object((1,3,6,1,4,1,6141,2,60,6,1,1,18,1,1),_WwpLeosFlowCosSyncStdPhbTo1dMapFrom_Type())
wwpLeosFlowCosSyncStdPhbTo1dMapFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCosSyncStdPhbTo1dMapFrom.setStatus(_A)
class _WwpLeosFlowCosSyncStdPhbTo1dMapTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosFlowCosSyncStdPhbTo1dMapTo_Type.__name__=_B
_WwpLeosFlowCosSyncStdPhbTo1dMapTo_Object=MibTableColumn
wwpLeosFlowCosSyncStdPhbTo1dMapTo=_WwpLeosFlowCosSyncStdPhbTo1dMapTo_Object((1,3,6,1,4,1,6141,2,60,6,1,1,18,1,2),_WwpLeosFlowCosSyncStdPhbTo1dMapTo_Type())
wwpLeosFlowCosSyncStdPhbTo1dMapTo.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCosSyncStdPhbTo1dMapTo.setStatus(_A)
_WwpLeosFlowL2SacTable_Object=MibTable
wwpLeosFlowL2SacTable=_WwpLeosFlowL2SacTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,19))
if mibBuilder.loadTexts:wwpLeosFlowL2SacTable.setStatus(_A)
_WwpLeosFlowL2SacEntry_Object=MibTableRow
wwpLeosFlowL2SacEntry=_WwpLeosFlowL2SacEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,19,1))
wwpLeosFlowL2SacEntry.setIndexNames((0,_D,_a),(0,_D,_b),(0,_D,_c))
if mibBuilder.loadTexts:wwpLeosFlowL2SacEntry.setStatus(_A)
class _WwpLeosFlowL2SacPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosFlowL2SacPortId_Type.__name__=_B
_WwpLeosFlowL2SacPortId_Object=MibTableColumn
wwpLeosFlowL2SacPortId=_WwpLeosFlowL2SacPortId_Object((1,3,6,1,4,1,6141,2,60,6,1,1,19,1,1),_WwpLeosFlowL2SacPortId_Type())
wwpLeosFlowL2SacPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowL2SacPortId.setStatus(_A)
class _WwpLeosFlowL2SacNetType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),('vlan',2),('vsiEth',3),('vsiMpls',4)))
_WwpLeosFlowL2SacNetType_Type.__name__=_B
_WwpLeosFlowL2SacNetType_Object=MibTableColumn
wwpLeosFlowL2SacNetType=_WwpLeosFlowL2SacNetType_Object((1,3,6,1,4,1,6141,2,60,6,1,1,19,1,2),_WwpLeosFlowL2SacNetType_Type())
wwpLeosFlowL2SacNetType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowL2SacNetType.setStatus(_A)
class _WwpLeosFlowSacNetValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosFlowSacNetValue_Type.__name__=_B
_WwpLeosFlowSacNetValue_Object=MibTableColumn
wwpLeosFlowSacNetValue=_WwpLeosFlowSacNetValue_Object((1,3,6,1,4,1,6141,2,60,6,1,1,19,1,3),_WwpLeosFlowSacNetValue_Type())
wwpLeosFlowSacNetValue.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowSacNetValue.setStatus(_A)
class _WwpLeosFlowL2SacLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpLeosFlowL2SacLimit_Type.__name__=_B
_WwpLeosFlowL2SacLimit_Object=MibTableColumn
wwpLeosFlowL2SacLimit=_WwpLeosFlowL2SacLimit_Object((1,3,6,1,4,1,6141,2,60,6,1,1,19,1,4),_WwpLeosFlowL2SacLimit_Type())
wwpLeosFlowL2SacLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowL2SacLimit.setStatus(_A)
_WwpLeosFlowL2SacCurMac_Type=Counter32
_WwpLeosFlowL2SacCurMac_Object=MibTableColumn
wwpLeosFlowL2SacCurMac=_WwpLeosFlowL2SacCurMac_Object((1,3,6,1,4,1,6141,2,60,6,1,1,19,1,5),_WwpLeosFlowL2SacCurMac_Type())
wwpLeosFlowL2SacCurMac.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowL2SacCurMac.setStatus(_A)
_WwpLeosFlowL2SacCurFilteredMac_Type=Counter32
_WwpLeosFlowL2SacCurFilteredMac_Object=MibTableColumn
wwpLeosFlowL2SacCurFilteredMac=_WwpLeosFlowL2SacCurFilteredMac_Object((1,3,6,1,4,1,6141,2,60,6,1,1,19,1,6),_WwpLeosFlowL2SacCurFilteredMac_Type())
wwpLeosFlowL2SacCurFilteredMac.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowL2SacCurFilteredMac.setStatus(_A)
class _WwpLeosFlowL2SacOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_WwpLeosFlowL2SacOperState_Type.__name__=_B
_WwpLeosFlowL2SacOperState_Object=MibTableColumn
wwpLeosFlowL2SacOperState=_WwpLeosFlowL2SacOperState_Object((1,3,6,1,4,1,6141,2,60,6,1,1,19,1,7),_WwpLeosFlowL2SacOperState_Type())
wwpLeosFlowL2SacOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowL2SacOperState.setStatus(_A)
_WwpLeosFlowL2SacRowStatus_Type=RowStatus
_WwpLeosFlowL2SacRowStatus_Object=MibTableColumn
wwpLeosFlowL2SacRowStatus=_WwpLeosFlowL2SacRowStatus_Object((1,3,6,1,4,1,6141,2,60,6,1,1,19,1,8),_WwpLeosFlowL2SacRowStatus_Type())
wwpLeosFlowL2SacRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowL2SacRowStatus.setStatus(_A)
class _WwpLeosFlowL2SacTrapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_WwpLeosFlowL2SacTrapState_Type.__name__=_B
_WwpLeosFlowL2SacTrapState_Object=MibScalar
wwpLeosFlowL2SacTrapState=_WwpLeosFlowL2SacTrapState_Object((1,3,6,1,4,1,6141,2,60,6,1,1,20),_WwpLeosFlowL2SacTrapState_Type())
wwpLeosFlowL2SacTrapState.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowL2SacTrapState.setStatus(_A)
class _WwpLeosFlowStrictQueuingState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_WwpLeosFlowStrictQueuingState_Type.__name__=_B
_WwpLeosFlowStrictQueuingState_Object=MibScalar
wwpLeosFlowStrictQueuingState=_WwpLeosFlowStrictQueuingState_Object((1,3,6,1,4,1,6141,2,60,6,1,1,21),_WwpLeosFlowStrictQueuingState_Type())
wwpLeosFlowStrictQueuingState.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowStrictQueuingState.setStatus(_A)
class _WwpLeosFlowBwCalcMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('transport',1),('payload',2)))
_WwpLeosFlowBwCalcMode_Type.__name__=_B
_WwpLeosFlowBwCalcMode_Object=MibScalar
wwpLeosFlowBwCalcMode=_WwpLeosFlowBwCalcMode_Object((1,3,6,1,4,1,6141,2,60,6,1,1,22),_WwpLeosFlowBwCalcMode_Type())
wwpLeosFlowBwCalcMode.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowBwCalcMode.setStatus(_A)
_WwpLeosFlowGlobal_ObjectIdentity=ObjectIdentity
wwpLeosFlowGlobal=_WwpLeosFlowGlobal_ObjectIdentity((1,3,6,1,4,1,6141,2,60,6,1,1,23))
class _WwpLeosFlowServiceLevelFlowGroupState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_WwpLeosFlowServiceLevelFlowGroupState_Type.__name__=_B
_WwpLeosFlowServiceLevelFlowGroupState_Object=MibScalar
wwpLeosFlowServiceLevelFlowGroupState=_WwpLeosFlowServiceLevelFlowGroupState_Object((1,3,6,1,4,1,6141,2,60,6,1,1,23,1),_WwpLeosFlowServiceLevelFlowGroupState_Type())
wwpLeosFlowServiceLevelFlowGroupState.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowServiceLevelFlowGroupState.setStatus(_A)
class _WwpLeosFlowServiceMappingCosRedMappingState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_WwpLeosFlowServiceMappingCosRedMappingState_Type.__name__=_B
_WwpLeosFlowServiceMappingCosRedMappingState_Object=MibScalar
wwpLeosFlowServiceMappingCosRedMappingState=_WwpLeosFlowServiceMappingCosRedMappingState_Object((1,3,6,1,4,1,6141,2,60,6,1,1,23,2),_WwpLeosFlowServiceMappingCosRedMappingState_Type())
wwpLeosFlowServiceMappingCosRedMappingState.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowServiceMappingCosRedMappingState.setStatus(_A)
class _WwpLeosFlowServiceAllRedCurveUnset_Type(TruthValue):defaultValue=2
_WwpLeosFlowServiceAllRedCurveUnset_Type.__name__=_Q
_WwpLeosFlowServiceAllRedCurveUnset_Object=MibScalar
wwpLeosFlowServiceAllRedCurveUnset=_WwpLeosFlowServiceAllRedCurveUnset_Object((1,3,6,1,4,1,6141,2,60,6,1,1,23,3),_WwpLeosFlowServiceAllRedCurveUnset_Type())
wwpLeosFlowServiceAllRedCurveUnset.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowServiceAllRedCurveUnset.setStatus(_A)
_WwpLeosFlowServiceRedCurveTable_Object=MibTable
wwpLeosFlowServiceRedCurveTable=_WwpLeosFlowServiceRedCurveTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,24))
if mibBuilder.loadTexts:wwpLeosFlowServiceRedCurveTable.setStatus(_A)
_WwpLeosFlowServiceRedCurveEntry_Object=MibTableRow
wwpLeosFlowServiceRedCurveEntry=_WwpLeosFlowServiceRedCurveEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,24,1))
wwpLeosFlowServiceRedCurveEntry.setIndexNames((0,_D,_AG))
if mibBuilder.loadTexts:wwpLeosFlowServiceRedCurveEntry.setStatus(_A)
class _WwpLeosFlowServiceRedCurveIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,64))
_WwpLeosFlowServiceRedCurveIndex_Type.__name__=_J
_WwpLeosFlowServiceRedCurveIndex_Object=MibTableColumn
wwpLeosFlowServiceRedCurveIndex=_WwpLeosFlowServiceRedCurveIndex_Object((1,3,6,1,4,1,6141,2,60,6,1,1,24,1,1),_WwpLeosFlowServiceRedCurveIndex_Type())
wwpLeosFlowServiceRedCurveIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceRedCurveIndex.setStatus(_A)
class _WwpLeosFlowServiceRedCurveName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_WwpLeosFlowServiceRedCurveName_Type.__name__=_o
_WwpLeosFlowServiceRedCurveName_Object=MibTableColumn
wwpLeosFlowServiceRedCurveName=_WwpLeosFlowServiceRedCurveName_Object((1,3,6,1,4,1,6141,2,60,6,1,1,24,1,2),_WwpLeosFlowServiceRedCurveName_Type())
wwpLeosFlowServiceRedCurveName.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowServiceRedCurveName.setStatus(_A)
class _WwpLeosFlowServiceRedCurveState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_WwpLeosFlowServiceRedCurveState_Type.__name__=_B
_WwpLeosFlowServiceRedCurveState_Object=MibTableColumn
wwpLeosFlowServiceRedCurveState=_WwpLeosFlowServiceRedCurveState_Object((1,3,6,1,4,1,6141,2,60,6,1,1,24,1,3),_WwpLeosFlowServiceRedCurveState_Type())
wwpLeosFlowServiceRedCurveState.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowServiceRedCurveState.setStatus(_A)
class _WwpLeosFlowServiceRedCurveMinThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosFlowServiceRedCurveMinThreshold_Type.__name__=_J
_WwpLeosFlowServiceRedCurveMinThreshold_Object=MibTableColumn
wwpLeosFlowServiceRedCurveMinThreshold=_WwpLeosFlowServiceRedCurveMinThreshold_Object((1,3,6,1,4,1,6141,2,60,6,1,1,24,1,4),_WwpLeosFlowServiceRedCurveMinThreshold_Type())
wwpLeosFlowServiceRedCurveMinThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowServiceRedCurveMinThreshold.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosFlowServiceRedCurveMinThreshold.setUnits('kbps')
class _WwpLeosFlowServiceRedCurveMaxThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosFlowServiceRedCurveMaxThreshold_Type.__name__=_J
_WwpLeosFlowServiceRedCurveMaxThreshold_Object=MibTableColumn
wwpLeosFlowServiceRedCurveMaxThreshold=_WwpLeosFlowServiceRedCurveMaxThreshold_Object((1,3,6,1,4,1,6141,2,60,6,1,1,24,1,5),_WwpLeosFlowServiceRedCurveMaxThreshold_Type())
wwpLeosFlowServiceRedCurveMaxThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowServiceRedCurveMaxThreshold.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosFlowServiceRedCurveMaxThreshold.setUnits('kbps')
class _WwpLeosFlowServiceRedCurveDropProbability_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_WwpLeosFlowServiceRedCurveDropProbability_Type.__name__=_J
_WwpLeosFlowServiceRedCurveDropProbability_Object=MibTableColumn
wwpLeosFlowServiceRedCurveDropProbability=_WwpLeosFlowServiceRedCurveDropProbability_Object((1,3,6,1,4,1,6141,2,60,6,1,1,24,1,6),_WwpLeosFlowServiceRedCurveDropProbability_Type())
wwpLeosFlowServiceRedCurveDropProbability.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowServiceRedCurveDropProbability.setStatus(_A)
class _WwpLeosFlowServiceRedCurveUnset_Type(TruthValue):defaultValue=2
_WwpLeosFlowServiceRedCurveUnset_Type.__name__=_Q
_WwpLeosFlowServiceRedCurveUnset_Object=MibTableColumn
wwpLeosFlowServiceRedCurveUnset=_WwpLeosFlowServiceRedCurveUnset_Object((1,3,6,1,4,1,6141,2,60,6,1,1,24,1,7),_WwpLeosFlowServiceRedCurveUnset_Type())
wwpLeosFlowServiceRedCurveUnset.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowServiceRedCurveUnset.setStatus(_A)
_WwpLeosFlowCos1dToRedCurveOffsetTable_Object=MibTable
wwpLeosFlowCos1dToRedCurveOffsetTable=_WwpLeosFlowCos1dToRedCurveOffsetTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,25))
if mibBuilder.loadTexts:wwpLeosFlowCos1dToRedCurveOffsetTable.setStatus(_A)
_WwpLeosFlowCos1dToRedCurveOffsetEntry_Object=MibTableRow
wwpLeosFlowCos1dToRedCurveOffsetEntry=_WwpLeosFlowCos1dToRedCurveOffsetEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,25,1))
wwpLeosFlowCos1dToRedCurveOffsetEntry.setIndexNames((0,_D,_AH))
if mibBuilder.loadTexts:wwpLeosFlowCos1dToRedCurveOffsetEntry.setStatus(_A)
class _WwpLeosFlowCos1dToRedCurveOffset1dValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosFlowCos1dToRedCurveOffset1dValue_Type.__name__=_J
_WwpLeosFlowCos1dToRedCurveOffset1dValue_Object=MibTableColumn
wwpLeosFlowCos1dToRedCurveOffset1dValue=_WwpLeosFlowCos1dToRedCurveOffset1dValue_Object((1,3,6,1,4,1,6141,2,60,6,1,1,25,1,1),_WwpLeosFlowCos1dToRedCurveOffset1dValue_Type())
wwpLeosFlowCos1dToRedCurveOffset1dValue.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCos1dToRedCurveOffset1dValue.setStatus(_A)
class _WwpLeosFlowCos1dToRedCurveOffsetValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_WwpLeosFlowCos1dToRedCurveOffsetValue_Type.__name__=_J
_WwpLeosFlowCos1dToRedCurveOffsetValue_Object=MibTableColumn
wwpLeosFlowCos1dToRedCurveOffsetValue=_WwpLeosFlowCos1dToRedCurveOffsetValue_Object((1,3,6,1,4,1,6141,2,60,6,1,1,25,1,2),_WwpLeosFlowCos1dToRedCurveOffsetValue_Type())
wwpLeosFlowCos1dToRedCurveOffsetValue.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCos1dToRedCurveOffsetValue.setStatus(_A)
_WwpLeosFlowCosMapPCPTo1dTable_Object=MibTable
wwpLeosFlowCosMapPCPTo1dTable=_WwpLeosFlowCosMapPCPTo1dTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,26))
if mibBuilder.loadTexts:wwpLeosFlowCosMapPCPTo1dTable.setStatus(_A)
_WwpLeosFlowCosMapPCPTo1dEntry_Object=MibTableRow
wwpLeosFlowCosMapPCPTo1dEntry=_WwpLeosFlowCosMapPCPTo1dEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,26,1))
wwpLeosFlowCosMapPCPTo1dEntry.setIndexNames((0,_D,_AI))
if mibBuilder.loadTexts:wwpLeosFlowCosMapPCPTo1dEntry.setStatus(_A)
class _WwpLeosFlowCosMapPCPTo1dMapFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosFlowCosMapPCPTo1dMapFrom_Type.__name__=_B
_WwpLeosFlowCosMapPCPTo1dMapFrom_Object=MibTableColumn
wwpLeosFlowCosMapPCPTo1dMapFrom=_WwpLeosFlowCosMapPCPTo1dMapFrom_Object((1,3,6,1,4,1,6141,2,60,6,1,1,26,1,1),_WwpLeosFlowCosMapPCPTo1dMapFrom_Type())
wwpLeosFlowCosMapPCPTo1dMapFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCosMapPCPTo1dMapFrom.setStatus(_A)
class _WwpLeosFlowCosMapPCPTo1dMapTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosFlowCosMapPCPTo1dMapTo_Type.__name__=_B
_WwpLeosFlowCosMapPCPTo1dMapTo_Object=MibTableColumn
wwpLeosFlowCosMapPCPTo1dMapTo=_WwpLeosFlowCosMapPCPTo1dMapTo_Object((1,3,6,1,4,1,6141,2,60,6,1,1,26,1,2),_WwpLeosFlowCosMapPCPTo1dMapTo_Type())
wwpLeosFlowCosMapPCPTo1dMapTo.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCosMapPCPTo1dMapTo.setStatus(_A)
_WwpLeosFlowCosMap1dToPCPTable_Object=MibTable
wwpLeosFlowCosMap1dToPCPTable=_WwpLeosFlowCosMap1dToPCPTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,27))
if mibBuilder.loadTexts:wwpLeosFlowCosMap1dToPCPTable.setStatus(_A)
_WwpLeosFlowCosMap1dToPCPEntry_Object=MibTableRow
wwpLeosFlowCosMap1dToPCPEntry=_WwpLeosFlowCosMap1dToPCPEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,27,1))
wwpLeosFlowCosMap1dToPCPEntry.setIndexNames((0,_D,_AJ))
if mibBuilder.loadTexts:wwpLeosFlowCosMap1dToPCPEntry.setStatus(_A)
class _WwpLeosFlowCosMap1dToPCPMapFrom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosFlowCosMap1dToPCPMapFrom_Type.__name__=_B
_WwpLeosFlowCosMap1dToPCPMapFrom_Object=MibTableColumn
wwpLeosFlowCosMap1dToPCPMapFrom=_WwpLeosFlowCosMap1dToPCPMapFrom_Object((1,3,6,1,4,1,6141,2,60,6,1,1,27,1,1),_WwpLeosFlowCosMap1dToPCPMapFrom_Type())
wwpLeosFlowCosMap1dToPCPMapFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCosMap1dToPCPMapFrom.setStatus(_A)
class _WwpLeosFlowCosMap1dToPCPMapTo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosFlowCosMap1dToPCPMapTo_Type.__name__=_B
_WwpLeosFlowCosMap1dToPCPMapTo_Object=MibTableColumn
wwpLeosFlowCosMap1dToPCPMapTo=_WwpLeosFlowCosMap1dToPCPMapTo_Object((1,3,6,1,4,1,6141,2,60,6,1,1,27,1,2),_WwpLeosFlowCosMap1dToPCPMapTo_Type())
wwpLeosFlowCosMap1dToPCPMapTo.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCosMap1dToPCPMapTo.setStatus(_A)
class _WwpLeosFlowMacMotionEventsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_WwpLeosFlowMacMotionEventsEnable_Type.__name__=_B
_WwpLeosFlowMacMotionEventsEnable_Object=MibScalar
wwpLeosFlowMacMotionEventsEnable=_WwpLeosFlowMacMotionEventsEnable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,28),_WwpLeosFlowMacMotionEventsEnable_Type())
wwpLeosFlowMacMotionEventsEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowMacMotionEventsEnable.setStatus(_A)
class _WwpLeosFlowMacMotionEventsInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,300))
_WwpLeosFlowMacMotionEventsInterval_Type.__name__=_B
_WwpLeosFlowMacMotionEventsInterval_Object=MibScalar
wwpLeosFlowMacMotionEventsInterval=_WwpLeosFlowMacMotionEventsInterval_Object((1,3,6,1,4,1,6141,2,60,6,1,1,29),_WwpLeosFlowMacMotionEventsInterval_Type())
wwpLeosFlowMacMotionEventsInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowMacMotionEventsInterval.setStatus(_A)
class _WwpLeosFlowCpuRateLimitsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_WwpLeosFlowCpuRateLimitsEnable_Type.__name__=_B
_WwpLeosFlowCpuRateLimitsEnable_Object=MibScalar
wwpLeosFlowCpuRateLimitsEnable=_WwpLeosFlowCpuRateLimitsEnable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,30),_WwpLeosFlowCpuRateLimitsEnable_Type())
wwpLeosFlowCpuRateLimitsEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitsEnable.setStatus(_A)
_WwpLeosFlowCpuRateLimitTable_Object=MibTable
wwpLeosFlowCpuRateLimitTable=_WwpLeosFlowCpuRateLimitTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31))
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitTable.setStatus(_A)
_WwpLeosFlowCpuRateLimitEntry_Object=MibTableRow
wwpLeosFlowCpuRateLimitEntry=_WwpLeosFlowCpuRateLimitEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1))
wwpLeosFlowCpuRateLimitEntry.setIndexNames((0,_D,_AK))
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitEntry.setStatus(_A)
class _WwpLeosFlowCpuRateLimitPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_WwpLeosFlowCpuRateLimitPort_Type.__name__=_B
_WwpLeosFlowCpuRateLimitPort_Object=MibTableColumn
wwpLeosFlowCpuRateLimitPort=_WwpLeosFlowCpuRateLimitPort_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,1),_WwpLeosFlowCpuRateLimitPort_Type())
wwpLeosFlowCpuRateLimitPort.setMaxAccess(_n)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitPort.setStatus(_A)
class _WwpLeosFlowCpuRateLimitEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_WwpLeosFlowCpuRateLimitEnable_Type.__name__=_B
_WwpLeosFlowCpuRateLimitEnable_Object=MibTableColumn
wwpLeosFlowCpuRateLimitEnable=_WwpLeosFlowCpuRateLimitEnable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,2),_WwpLeosFlowCpuRateLimitEnable_Type())
wwpLeosFlowCpuRateLimitEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitEnable.setStatus(_A)
class _WwpLeosFlowCpuRateLimitBootp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_WwpLeosFlowCpuRateLimitBootp_Type.__name__=_B
_WwpLeosFlowCpuRateLimitBootp_Object=MibTableColumn
wwpLeosFlowCpuRateLimitBootp=_WwpLeosFlowCpuRateLimitBootp_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,3),_WwpLeosFlowCpuRateLimitBootp_Type())
wwpLeosFlowCpuRateLimitBootp.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitBootp.setStatus(_A)
class _WwpLeosFlowCpuRateLimitCfm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_WwpLeosFlowCpuRateLimitCfm_Type.__name__=_B
_WwpLeosFlowCpuRateLimitCfm_Object=MibTableColumn
wwpLeosFlowCpuRateLimitCfm=_WwpLeosFlowCpuRateLimitCfm_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,4),_WwpLeosFlowCpuRateLimitCfm_Type())
wwpLeosFlowCpuRateLimitCfm.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitCfm.setStatus(_A)
class _WwpLeosFlowCpuRateLimitCft_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_WwpLeosFlowCpuRateLimitCft_Type.__name__=_B
_WwpLeosFlowCpuRateLimitCft_Object=MibTableColumn
wwpLeosFlowCpuRateLimitCft=_WwpLeosFlowCpuRateLimitCft_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,5),_WwpLeosFlowCpuRateLimitCft_Type())
wwpLeosFlowCpuRateLimitCft.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitCft.setStatus(_A)
class _WwpLeosFlowCpuRateLimitDot1x_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_WwpLeosFlowCpuRateLimitDot1x_Type.__name__=_B
_WwpLeosFlowCpuRateLimitDot1x_Object=MibTableColumn
wwpLeosFlowCpuRateLimitDot1x=_WwpLeosFlowCpuRateLimitDot1x_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,6),_WwpLeosFlowCpuRateLimitDot1x_Type())
wwpLeosFlowCpuRateLimitDot1x.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitDot1x.setStatus(_A)
class _WwpLeosFlowCpuRateLimitOam_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_WwpLeosFlowCpuRateLimitOam_Type.__name__=_B
_WwpLeosFlowCpuRateLimitOam_Object=MibTableColumn
wwpLeosFlowCpuRateLimitOam=_WwpLeosFlowCpuRateLimitOam_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,7),_WwpLeosFlowCpuRateLimitOam_Type())
wwpLeosFlowCpuRateLimitOam.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitOam.setStatus(_A)
class _WwpLeosFlowCpuRateLimitEprArp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_WwpLeosFlowCpuRateLimitEprArp_Type.__name__=_B
_WwpLeosFlowCpuRateLimitEprArp_Object=MibTableColumn
wwpLeosFlowCpuRateLimitEprArp=_WwpLeosFlowCpuRateLimitEprArp_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,8),_WwpLeosFlowCpuRateLimitEprArp_Type())
wwpLeosFlowCpuRateLimitEprArp.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitEprArp.setStatus(_A)
class _WwpLeosFlowCpuRateLimitIgmp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_WwpLeosFlowCpuRateLimitIgmp_Type.__name__=_B
_WwpLeosFlowCpuRateLimitIgmp_Object=MibTableColumn
wwpLeosFlowCpuRateLimitIgmp=_WwpLeosFlowCpuRateLimitIgmp_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,9),_WwpLeosFlowCpuRateLimitIgmp_Type())
wwpLeosFlowCpuRateLimitIgmp.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitIgmp.setStatus(_A)
class _WwpLeosFlowCpuRateLimitInet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_WwpLeosFlowCpuRateLimitInet_Type.__name__=_B
_WwpLeosFlowCpuRateLimitInet_Object=MibTableColumn
wwpLeosFlowCpuRateLimitInet=_WwpLeosFlowCpuRateLimitInet_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,10),_WwpLeosFlowCpuRateLimitInet_Type())
wwpLeosFlowCpuRateLimitInet.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitInet.setStatus(_A)
class _WwpLeosFlowCpuRateLimitLacp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_WwpLeosFlowCpuRateLimitLacp_Type.__name__=_B
_WwpLeosFlowCpuRateLimitLacp_Object=MibTableColumn
wwpLeosFlowCpuRateLimitLacp=_WwpLeosFlowCpuRateLimitLacp_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,11),_WwpLeosFlowCpuRateLimitLacp_Type())
wwpLeosFlowCpuRateLimitLacp.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitLacp.setStatus(_A)
class _WwpLeosFlowCpuRateLimitLldp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_WwpLeosFlowCpuRateLimitLldp_Type.__name__=_B
_WwpLeosFlowCpuRateLimitLldp_Object=MibTableColumn
wwpLeosFlowCpuRateLimitLldp=_WwpLeosFlowCpuRateLimitLldp_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,12),_WwpLeosFlowCpuRateLimitLldp_Type())
wwpLeosFlowCpuRateLimitLldp.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitLldp.setStatus(_A)
class _WwpLeosFlowCpuRateLimitMpls_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_WwpLeosFlowCpuRateLimitMpls_Type.__name__=_B
_WwpLeosFlowCpuRateLimitMpls_Object=MibTableColumn
wwpLeosFlowCpuRateLimitMpls=_WwpLeosFlowCpuRateLimitMpls_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,13),_WwpLeosFlowCpuRateLimitMpls_Type())
wwpLeosFlowCpuRateLimitMpls.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitMpls.setStatus(_A)
class _WwpLeosFlowCpuRateLimitMstp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_WwpLeosFlowCpuRateLimitMstp_Type.__name__=_B
_WwpLeosFlowCpuRateLimitMstp_Object=MibTableColumn
wwpLeosFlowCpuRateLimitMstp=_WwpLeosFlowCpuRateLimitMstp_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,14),_WwpLeosFlowCpuRateLimitMstp_Type())
wwpLeosFlowCpuRateLimitMstp.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitMstp.setStatus(_A)
class _WwpLeosFlowCpuRateLimitPeArp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_WwpLeosFlowCpuRateLimitPeArp_Type.__name__=_B
_WwpLeosFlowCpuRateLimitPeArp_Object=MibTableColumn
wwpLeosFlowCpuRateLimitPeArp=_WwpLeosFlowCpuRateLimitPeArp_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,15),_WwpLeosFlowCpuRateLimitPeArp_Type())
wwpLeosFlowCpuRateLimitPeArp.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitPeArp.setStatus(_A)
class _WwpLeosFlowCpuRateLimitPvst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_WwpLeosFlowCpuRateLimitPvst_Type.__name__=_B
_WwpLeosFlowCpuRateLimitPvst_Object=MibTableColumn
wwpLeosFlowCpuRateLimitPvst=_WwpLeosFlowCpuRateLimitPvst_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,16),_WwpLeosFlowCpuRateLimitPvst_Type())
wwpLeosFlowCpuRateLimitPvst.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitPvst.setStatus(_A)
class _WwpLeosFlowCpuRateLimitRstp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_WwpLeosFlowCpuRateLimitRstp_Type.__name__=_B
_WwpLeosFlowCpuRateLimitRstp_Object=MibTableColumn
wwpLeosFlowCpuRateLimitRstp=_WwpLeosFlowCpuRateLimitRstp_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,17),_WwpLeosFlowCpuRateLimitRstp_Type())
wwpLeosFlowCpuRateLimitRstp.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitRstp.setStatus(_A)
class _WwpLeosFlowCpuRateLimitLpbk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_WwpLeosFlowCpuRateLimitLpbk_Type.__name__=_B
_WwpLeosFlowCpuRateLimitLpbk_Object=MibTableColumn
wwpLeosFlowCpuRateLimitLpbk=_WwpLeosFlowCpuRateLimitLpbk_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,18),_WwpLeosFlowCpuRateLimitLpbk_Type())
wwpLeosFlowCpuRateLimitLpbk.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitLpbk.setStatus(_A)
class _WwpLeosFlowCpuRateLimitRmtLpbk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_WwpLeosFlowCpuRateLimitRmtLpbk_Type.__name__=_B
_WwpLeosFlowCpuRateLimitRmtLpbk_Object=MibTableColumn
wwpLeosFlowCpuRateLimitRmtLpbk=_WwpLeosFlowCpuRateLimitRmtLpbk_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,19),_WwpLeosFlowCpuRateLimitRmtLpbk_Type())
wwpLeosFlowCpuRateLimitRmtLpbk.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitRmtLpbk.setStatus(_A)
class _WwpLeosFlowCpuRateLimitCxeRx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_WwpLeosFlowCpuRateLimitCxeRx_Type.__name__=_B
_WwpLeosFlowCpuRateLimitCxeRx_Object=MibTableColumn
wwpLeosFlowCpuRateLimitCxeRx=_WwpLeosFlowCpuRateLimitCxeRx_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,20),_WwpLeosFlowCpuRateLimitCxeRx_Type())
wwpLeosFlowCpuRateLimitCxeRx.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitCxeRx.setStatus(_A)
class _WwpLeosFlowCpuRateLimitCxeTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_WwpLeosFlowCpuRateLimitCxeTx_Type.__name__=_B
_WwpLeosFlowCpuRateLimitCxeTx_Object=MibTableColumn
wwpLeosFlowCpuRateLimitCxeTx=_WwpLeosFlowCpuRateLimitCxeTx_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,21),_WwpLeosFlowCpuRateLimitCxeTx_Type())
wwpLeosFlowCpuRateLimitCxeTx.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitCxeTx.setStatus(_A)
class _WwpLeosFlowCpuRateLimitTwamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_WwpLeosFlowCpuRateLimitTwamp_Type.__name__=_B
_WwpLeosFlowCpuRateLimitTwamp_Object=MibTableColumn
wwpLeosFlowCpuRateLimitTwamp=_WwpLeosFlowCpuRateLimitTwamp_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,22),_WwpLeosFlowCpuRateLimitTwamp_Type())
wwpLeosFlowCpuRateLimitTwamp.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitTwamp.setStatus(_A)
class _WwpLeosFlowCpuRateLimitDflt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WwpLeosFlowCpuRateLimitDflt_Type.__name__=_B
_WwpLeosFlowCpuRateLimitDflt_Object=MibTableColumn
wwpLeosFlowCpuRateLimitDflt=_WwpLeosFlowCpuRateLimitDflt_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,23),_WwpLeosFlowCpuRateLimitDflt_Type())
wwpLeosFlowCpuRateLimitDflt.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitDflt.setStatus(_A)
class _WwpLeosFlowCpuRateLimitTwampRsp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_WwpLeosFlowCpuRateLimitTwampRsp_Type.__name__=_B
_WwpLeosFlowCpuRateLimitTwampRsp_Object=MibTableColumn
wwpLeosFlowCpuRateLimitTwampRsp=_WwpLeosFlowCpuRateLimitTwampRsp_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,24),_WwpLeosFlowCpuRateLimitTwampRsp_Type())
wwpLeosFlowCpuRateLimitTwampRsp.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitTwampRsp.setStatus(_A)
class _WwpLeosFlowCpuRateLimitMultiCast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_WwpLeosFlowCpuRateLimitMultiCast_Type.__name__=_B
_WwpLeosFlowCpuRateLimitMultiCast_Object=MibTableColumn
wwpLeosFlowCpuRateLimitMultiCast=_WwpLeosFlowCpuRateLimitMultiCast_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,25),_WwpLeosFlowCpuRateLimitMultiCast_Type())
wwpLeosFlowCpuRateLimitMultiCast.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitMultiCast.setStatus(_A)
class _WwpLeosFlowCpuRateLimitBroadCast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_WwpLeosFlowCpuRateLimitBroadCast_Type.__name__=_B
_WwpLeosFlowCpuRateLimitBroadCast_Object=MibTableColumn
wwpLeosFlowCpuRateLimitBroadCast=_WwpLeosFlowCpuRateLimitBroadCast_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,26),_WwpLeosFlowCpuRateLimitBroadCast_Type())
wwpLeosFlowCpuRateLimitBroadCast.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitBroadCast.setStatus(_A)
class _WwpLeosFlowCpuRateLimitArp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_WwpLeosFlowCpuRateLimitArp_Type.__name__=_B
_WwpLeosFlowCpuRateLimitArp_Object=MibTableColumn
wwpLeosFlowCpuRateLimitArp=_WwpLeosFlowCpuRateLimitArp_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,27),_WwpLeosFlowCpuRateLimitArp_Type())
wwpLeosFlowCpuRateLimitArp.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitArp.setStatus(_A)
class _WwpLeosFlowCpuRateLimitIcmp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_WwpLeosFlowCpuRateLimitIcmp_Type.__name__=_B
_WwpLeosFlowCpuRateLimitIcmp_Object=MibTableColumn
wwpLeosFlowCpuRateLimitIcmp=_WwpLeosFlowCpuRateLimitIcmp_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,28),_WwpLeosFlowCpuRateLimitIcmp_Type())
wwpLeosFlowCpuRateLimitIcmp.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitIcmp.setStatus(_A)
class _WwpLeosFlowCpuRateLimitTcpSyn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_WwpLeosFlowCpuRateLimitTcpSyn_Type.__name__=_B
_WwpLeosFlowCpuRateLimitTcpSyn_Object=MibTableColumn
wwpLeosFlowCpuRateLimitTcpSyn=_WwpLeosFlowCpuRateLimitTcpSyn_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,29),_WwpLeosFlowCpuRateLimitTcpSyn_Type())
wwpLeosFlowCpuRateLimitTcpSyn.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitTcpSyn.setStatus(_A)
class _WwpLeosFlowCpuRateLimitRaps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500))
_WwpLeosFlowCpuRateLimitRaps_Type.__name__=_B
_WwpLeosFlowCpuRateLimitRaps_Object=MibTableColumn
wwpLeosFlowCpuRateLimitRaps=_WwpLeosFlowCpuRateLimitRaps_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,30),_WwpLeosFlowCpuRateLimitRaps_Type())
wwpLeosFlowCpuRateLimitRaps.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitRaps.setStatus(_A)
class _WwpLeosFlowCpuRateLimitIpMgmt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_WwpLeosFlowCpuRateLimitIpMgmt_Type.__name__=_B
_WwpLeosFlowCpuRateLimitIpMgmt_Object=MibTableColumn
wwpLeosFlowCpuRateLimitIpMgmt=_WwpLeosFlowCpuRateLimitIpMgmt_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,31),_WwpLeosFlowCpuRateLimitIpMgmt_Type())
wwpLeosFlowCpuRateLimitIpMgmt.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitIpMgmt.setStatus(_A)
class _WwpLeosFlowCpuRateLimitIpControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_WwpLeosFlowCpuRateLimitIpControl_Type.__name__=_B
_WwpLeosFlowCpuRateLimitIpControl_Object=MibTableColumn
wwpLeosFlowCpuRateLimitIpControl=_WwpLeosFlowCpuRateLimitIpControl_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,32),_WwpLeosFlowCpuRateLimitIpControl_Type())
wwpLeosFlowCpuRateLimitIpControl.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitIpControl.setStatus(_A)
class _WwpLeosFlowCpuRateLimitIpV6Mgmt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_WwpLeosFlowCpuRateLimitIpV6Mgmt_Type.__name__=_B
_WwpLeosFlowCpuRateLimitIpV6Mgmt_Object=MibTableColumn
wwpLeosFlowCpuRateLimitIpV6Mgmt=_WwpLeosFlowCpuRateLimitIpV6Mgmt_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,33),_WwpLeosFlowCpuRateLimitIpV6Mgmt_Type())
wwpLeosFlowCpuRateLimitIpV6Mgmt.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitIpV6Mgmt.setStatus(_A)
class _WwpLeosFlowCpuRateLimitInet6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_WwpLeosFlowCpuRateLimitInet6_Type.__name__=_B
_WwpLeosFlowCpuRateLimitInet6_Object=MibTableColumn
wwpLeosFlowCpuRateLimitInet6=_WwpLeosFlowCpuRateLimitInet6_Object((1,3,6,1,4,1,6141,2,60,6,1,1,31,1,34),_WwpLeosFlowCpuRateLimitInet6_Type())
wwpLeosFlowCpuRateLimitInet6.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitInet6.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsTable_Object=MibTable
wwpLeosFlowCpuRateLimitStatsTable=_WwpLeosFlowCpuRateLimitStatsTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32))
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsTable.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsEntry_Object=MibTableRow
wwpLeosFlowCpuRateLimitStatsEntry=_WwpLeosFlowCpuRateLimitStatsEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1))
wwpLeosFlowCpuRateLimitStatsEntry.setIndexNames((0,_D,_AL))
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsEntry.setStatus(_A)
class _WwpLeosFlowCpuRateLimitStatsPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_WwpLeosFlowCpuRateLimitStatsPort_Type.__name__=_B
_WwpLeosFlowCpuRateLimitStatsPort_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsPort=_WwpLeosFlowCpuRateLimitStatsPort_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,1),_WwpLeosFlowCpuRateLimitStatsPort_Type())
wwpLeosFlowCpuRateLimitStatsPort.setMaxAccess(_n)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsPort.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsBootpPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsBootpPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsBootpPassed=_WwpLeosFlowCpuRateLimitStatsBootpPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,2),_WwpLeosFlowCpuRateLimitStatsBootpPassed_Type())
wwpLeosFlowCpuRateLimitStatsBootpPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsBootpPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsCfmPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsCfmPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsCfmPassed=_WwpLeosFlowCpuRateLimitStatsCfmPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,3),_WwpLeosFlowCpuRateLimitStatsCfmPassed_Type())
wwpLeosFlowCpuRateLimitStatsCfmPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsCfmPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsCftPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsCftPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsCftPassed=_WwpLeosFlowCpuRateLimitStatsCftPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,4),_WwpLeosFlowCpuRateLimitStatsCftPassed_Type())
wwpLeosFlowCpuRateLimitStatsCftPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsCftPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsDot1xPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsDot1xPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsDot1xPassed=_WwpLeosFlowCpuRateLimitStatsDot1xPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,5),_WwpLeosFlowCpuRateLimitStatsDot1xPassed_Type())
wwpLeosFlowCpuRateLimitStatsDot1xPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsDot1xPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsOamPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsOamPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsOamPassed=_WwpLeosFlowCpuRateLimitStatsOamPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,6),_WwpLeosFlowCpuRateLimitStatsOamPassed_Type())
wwpLeosFlowCpuRateLimitStatsOamPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsOamPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsEprArpPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsEprArpPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsEprArpPassed=_WwpLeosFlowCpuRateLimitStatsEprArpPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,7),_WwpLeosFlowCpuRateLimitStatsEprArpPassed_Type())
wwpLeosFlowCpuRateLimitStatsEprArpPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsEprArpPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsIgmpPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsIgmpPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsIgmpPassed=_WwpLeosFlowCpuRateLimitStatsIgmpPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,8),_WwpLeosFlowCpuRateLimitStatsIgmpPassed_Type())
wwpLeosFlowCpuRateLimitStatsIgmpPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsIgmpPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsInetPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsInetPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsInetPassed=_WwpLeosFlowCpuRateLimitStatsInetPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,9),_WwpLeosFlowCpuRateLimitStatsInetPassed_Type())
wwpLeosFlowCpuRateLimitStatsInetPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsInetPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsLacpPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsLacpPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsLacpPassed=_WwpLeosFlowCpuRateLimitStatsLacpPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,10),_WwpLeosFlowCpuRateLimitStatsLacpPassed_Type())
wwpLeosFlowCpuRateLimitStatsLacpPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsLacpPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsLldpPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsLldpPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsLldpPassed=_WwpLeosFlowCpuRateLimitStatsLldpPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,11),_WwpLeosFlowCpuRateLimitStatsLldpPassed_Type())
wwpLeosFlowCpuRateLimitStatsLldpPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsLldpPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsMplsPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsMplsPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsMplsPassed=_WwpLeosFlowCpuRateLimitStatsMplsPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,12),_WwpLeosFlowCpuRateLimitStatsMplsPassed_Type())
wwpLeosFlowCpuRateLimitStatsMplsPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsMplsPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsMstpPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsMstpPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsMstpPassed=_WwpLeosFlowCpuRateLimitStatsMstpPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,13),_WwpLeosFlowCpuRateLimitStatsMstpPassed_Type())
wwpLeosFlowCpuRateLimitStatsMstpPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsMstpPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsPeArpPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsPeArpPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsPeArpPassed=_WwpLeosFlowCpuRateLimitStatsPeArpPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,14),_WwpLeosFlowCpuRateLimitStatsPeArpPassed_Type())
wwpLeosFlowCpuRateLimitStatsPeArpPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsPeArpPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsPvstPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsPvstPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsPvstPassed=_WwpLeosFlowCpuRateLimitStatsPvstPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,15),_WwpLeosFlowCpuRateLimitStatsPvstPassed_Type())
wwpLeosFlowCpuRateLimitStatsPvstPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsPvstPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsRstpPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsRstpPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsRstpPassed=_WwpLeosFlowCpuRateLimitStatsRstpPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,16),_WwpLeosFlowCpuRateLimitStatsRstpPassed_Type())
wwpLeosFlowCpuRateLimitStatsRstpPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsRstpPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsLpbkPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsLpbkPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsLpbkPassed=_WwpLeosFlowCpuRateLimitStatsLpbkPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,17),_WwpLeosFlowCpuRateLimitStatsLpbkPassed_Type())
wwpLeosFlowCpuRateLimitStatsLpbkPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsLpbkPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsRmtLpbkPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsRmtLpbkPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsRmtLpbkPassed=_WwpLeosFlowCpuRateLimitStatsRmtLpbkPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,18),_WwpLeosFlowCpuRateLimitStatsRmtLpbkPassed_Type())
wwpLeosFlowCpuRateLimitStatsRmtLpbkPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsRmtLpbkPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsCxeRxPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsCxeRxPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsCxeRxPassed=_WwpLeosFlowCpuRateLimitStatsCxeRxPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,19),_WwpLeosFlowCpuRateLimitStatsCxeRxPassed_Type())
wwpLeosFlowCpuRateLimitStatsCxeRxPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsCxeRxPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsCxeTxPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsCxeTxPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsCxeTxPassed=_WwpLeosFlowCpuRateLimitStatsCxeTxPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,20),_WwpLeosFlowCpuRateLimitStatsCxeTxPassed_Type())
wwpLeosFlowCpuRateLimitStatsCxeTxPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsCxeTxPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsTwampPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsTwampPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsTwampPassed=_WwpLeosFlowCpuRateLimitStatsTwampPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,21),_WwpLeosFlowCpuRateLimitStatsTwampPassed_Type())
wwpLeosFlowCpuRateLimitStatsTwampPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsTwampPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsDfltPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsDfltPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsDfltPassed=_WwpLeosFlowCpuRateLimitStatsDfltPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,22),_WwpLeosFlowCpuRateLimitStatsDfltPassed_Type())
wwpLeosFlowCpuRateLimitStatsDfltPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsDfltPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsBootpDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsBootpDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsBootpDropped=_WwpLeosFlowCpuRateLimitStatsBootpDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,23),_WwpLeosFlowCpuRateLimitStatsBootpDropped_Type())
wwpLeosFlowCpuRateLimitStatsBootpDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsBootpDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsCfmDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsCfmDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsCfmDropped=_WwpLeosFlowCpuRateLimitStatsCfmDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,24),_WwpLeosFlowCpuRateLimitStatsCfmDropped_Type())
wwpLeosFlowCpuRateLimitStatsCfmDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsCfmDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsCftDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsCftDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsCftDropped=_WwpLeosFlowCpuRateLimitStatsCftDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,25),_WwpLeosFlowCpuRateLimitStatsCftDropped_Type())
wwpLeosFlowCpuRateLimitStatsCftDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsCftDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsDot1xDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsDot1xDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsDot1xDropped=_WwpLeosFlowCpuRateLimitStatsDot1xDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,26),_WwpLeosFlowCpuRateLimitStatsDot1xDropped_Type())
wwpLeosFlowCpuRateLimitStatsDot1xDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsDot1xDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsOamDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsOamDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsOamDropped=_WwpLeosFlowCpuRateLimitStatsOamDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,27),_WwpLeosFlowCpuRateLimitStatsOamDropped_Type())
wwpLeosFlowCpuRateLimitStatsOamDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsOamDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsEprArpDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsEprArpDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsEprArpDropped=_WwpLeosFlowCpuRateLimitStatsEprArpDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,28),_WwpLeosFlowCpuRateLimitStatsEprArpDropped_Type())
wwpLeosFlowCpuRateLimitStatsEprArpDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsEprArpDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsIgmpDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsIgmpDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsIgmpDropped=_WwpLeosFlowCpuRateLimitStatsIgmpDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,29),_WwpLeosFlowCpuRateLimitStatsIgmpDropped_Type())
wwpLeosFlowCpuRateLimitStatsIgmpDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsIgmpDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsInetDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsInetDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsInetDropped=_WwpLeosFlowCpuRateLimitStatsInetDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,30),_WwpLeosFlowCpuRateLimitStatsInetDropped_Type())
wwpLeosFlowCpuRateLimitStatsInetDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsInetDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsLacpDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsLacpDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsLacpDropped=_WwpLeosFlowCpuRateLimitStatsLacpDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,31),_WwpLeosFlowCpuRateLimitStatsLacpDropped_Type())
wwpLeosFlowCpuRateLimitStatsLacpDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsLacpDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsLldpDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsLldpDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsLldpDropped=_WwpLeosFlowCpuRateLimitStatsLldpDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,32),_WwpLeosFlowCpuRateLimitStatsLldpDropped_Type())
wwpLeosFlowCpuRateLimitStatsLldpDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsLldpDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsMplsDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsMplsDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsMplsDropped=_WwpLeosFlowCpuRateLimitStatsMplsDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,33),_WwpLeosFlowCpuRateLimitStatsMplsDropped_Type())
wwpLeosFlowCpuRateLimitStatsMplsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsMplsDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsMstpDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsMstpDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsMstpDropped=_WwpLeosFlowCpuRateLimitStatsMstpDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,34),_WwpLeosFlowCpuRateLimitStatsMstpDropped_Type())
wwpLeosFlowCpuRateLimitStatsMstpDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsMstpDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsPeArpDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsPeArpDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsPeArpDropped=_WwpLeosFlowCpuRateLimitStatsPeArpDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,35),_WwpLeosFlowCpuRateLimitStatsPeArpDropped_Type())
wwpLeosFlowCpuRateLimitStatsPeArpDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsPeArpDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsPvstDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsPvstDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsPvstDropped=_WwpLeosFlowCpuRateLimitStatsPvstDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,36),_WwpLeosFlowCpuRateLimitStatsPvstDropped_Type())
wwpLeosFlowCpuRateLimitStatsPvstDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsPvstDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsRstpDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsRstpDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsRstpDropped=_WwpLeosFlowCpuRateLimitStatsRstpDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,37),_WwpLeosFlowCpuRateLimitStatsRstpDropped_Type())
wwpLeosFlowCpuRateLimitStatsRstpDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsRstpDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsLpbkDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsLpbkDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsLpbkDropped=_WwpLeosFlowCpuRateLimitStatsLpbkDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,38),_WwpLeosFlowCpuRateLimitStatsLpbkDropped_Type())
wwpLeosFlowCpuRateLimitStatsLpbkDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsLpbkDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsRmtLpbkDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsRmtLpbkDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsRmtLpbkDropped=_WwpLeosFlowCpuRateLimitStatsRmtLpbkDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,39),_WwpLeosFlowCpuRateLimitStatsRmtLpbkDropped_Type())
wwpLeosFlowCpuRateLimitStatsRmtLpbkDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsRmtLpbkDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsCxeRxDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsCxeRxDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsCxeRxDropped=_WwpLeosFlowCpuRateLimitStatsCxeRxDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,40),_WwpLeosFlowCpuRateLimitStatsCxeRxDropped_Type())
wwpLeosFlowCpuRateLimitStatsCxeRxDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsCxeRxDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsCxeTxDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsCxeTxDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsCxeTxDropped=_WwpLeosFlowCpuRateLimitStatsCxeTxDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,41),_WwpLeosFlowCpuRateLimitStatsCxeTxDropped_Type())
wwpLeosFlowCpuRateLimitStatsCxeTxDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsCxeTxDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsTwampDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsTwampDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsTwampDropped=_WwpLeosFlowCpuRateLimitStatsTwampDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,42),_WwpLeosFlowCpuRateLimitStatsTwampDropped_Type())
wwpLeosFlowCpuRateLimitStatsTwampDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsTwampDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsDfltDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsDfltDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsDfltDropped=_WwpLeosFlowCpuRateLimitStatsDfltDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,43),_WwpLeosFlowCpuRateLimitStatsDfltDropped_Type())
wwpLeosFlowCpuRateLimitStatsDfltDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsDfltDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsTwampRspPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsTwampRspPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsTwampRspPassed=_WwpLeosFlowCpuRateLimitStatsTwampRspPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,44),_WwpLeosFlowCpuRateLimitStatsTwampRspPassed_Type())
wwpLeosFlowCpuRateLimitStatsTwampRspPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsTwampRspPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsTwampRspDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsTwampRspDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsTwampRspDropped=_WwpLeosFlowCpuRateLimitStatsTwampRspDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,45),_WwpLeosFlowCpuRateLimitStatsTwampRspDropped_Type())
wwpLeosFlowCpuRateLimitStatsTwampRspDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsTwampRspDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsMultiCastPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsMultiCastPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsMultiCastPassed=_WwpLeosFlowCpuRateLimitStatsMultiCastPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,46),_WwpLeosFlowCpuRateLimitStatsMultiCastPassed_Type())
wwpLeosFlowCpuRateLimitStatsMultiCastPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsMultiCastPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsMultiCastDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsMultiCastDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsMultiCastDropped=_WwpLeosFlowCpuRateLimitStatsMultiCastDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,47),_WwpLeosFlowCpuRateLimitStatsMultiCastDropped_Type())
wwpLeosFlowCpuRateLimitStatsMultiCastDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsMultiCastDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsBroadCastPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsBroadCastPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsBroadCastPassed=_WwpLeosFlowCpuRateLimitStatsBroadCastPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,48),_WwpLeosFlowCpuRateLimitStatsBroadCastPassed_Type())
wwpLeosFlowCpuRateLimitStatsBroadCastPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsBroadCastPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsBroadCastDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsBroadCastDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsBroadCastDropped=_WwpLeosFlowCpuRateLimitStatsBroadCastDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,49),_WwpLeosFlowCpuRateLimitStatsBroadCastDropped_Type())
wwpLeosFlowCpuRateLimitStatsBroadCastDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsBroadCastDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsArpPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsArpPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsArpPassed=_WwpLeosFlowCpuRateLimitStatsArpPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,50),_WwpLeosFlowCpuRateLimitStatsArpPassed_Type())
wwpLeosFlowCpuRateLimitStatsArpPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsArpPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsArpDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsArpDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsArpDropped=_WwpLeosFlowCpuRateLimitStatsArpDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,51),_WwpLeosFlowCpuRateLimitStatsArpDropped_Type())
wwpLeosFlowCpuRateLimitStatsArpDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsArpDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsIcmpPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsIcmpPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsIcmpPassed=_WwpLeosFlowCpuRateLimitStatsIcmpPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,52),_WwpLeosFlowCpuRateLimitStatsIcmpPassed_Type())
wwpLeosFlowCpuRateLimitStatsIcmpPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsIcmpPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsIcmpDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsIcmpDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsIcmpDropped=_WwpLeosFlowCpuRateLimitStatsIcmpDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,53),_WwpLeosFlowCpuRateLimitStatsIcmpDropped_Type())
wwpLeosFlowCpuRateLimitStatsIcmpDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsIcmpDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsTcpSynPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsTcpSynPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsTcpSynPassed=_WwpLeosFlowCpuRateLimitStatsTcpSynPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,54),_WwpLeosFlowCpuRateLimitStatsTcpSynPassed_Type())
wwpLeosFlowCpuRateLimitStatsTcpSynPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsTcpSynPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsTcpSynDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsTcpSynDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsTcpSynDropped=_WwpLeosFlowCpuRateLimitStatsTcpSynDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,55),_WwpLeosFlowCpuRateLimitStatsTcpSynDropped_Type())
wwpLeosFlowCpuRateLimitStatsTcpSynDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsTcpSynDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsRapsPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsRapsPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsRapsPassed=_WwpLeosFlowCpuRateLimitStatsRapsPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,56),_WwpLeosFlowCpuRateLimitStatsRapsPassed_Type())
wwpLeosFlowCpuRateLimitStatsRapsPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsRapsPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsRapsDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsRapsDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsRapsDropped=_WwpLeosFlowCpuRateLimitStatsRapsDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,57),_WwpLeosFlowCpuRateLimitStatsRapsDropped_Type())
wwpLeosFlowCpuRateLimitStatsRapsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsRapsDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsIpMgmtPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsIpMgmtPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsIpMgmtPassed=_WwpLeosFlowCpuRateLimitStatsIpMgmtPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,58),_WwpLeosFlowCpuRateLimitStatsIpMgmtPassed_Type())
wwpLeosFlowCpuRateLimitStatsIpMgmtPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsIpMgmtPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsIpMgmtDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsIpMgmtDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsIpMgmtDropped=_WwpLeosFlowCpuRateLimitStatsIpMgmtDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,59),_WwpLeosFlowCpuRateLimitStatsIpMgmtDropped_Type())
wwpLeosFlowCpuRateLimitStatsIpMgmtDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsIpMgmtDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsIpControlPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsIpControlPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsIpControlPassed=_WwpLeosFlowCpuRateLimitStatsIpControlPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,60),_WwpLeosFlowCpuRateLimitStatsIpControlPassed_Type())
wwpLeosFlowCpuRateLimitStatsIpControlPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsIpControlPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsIpControlDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsIpControlDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsIpControlDropped=_WwpLeosFlowCpuRateLimitStatsIpControlDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,61),_WwpLeosFlowCpuRateLimitStatsIpControlDropped_Type())
wwpLeosFlowCpuRateLimitStatsIpControlDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsIpControlDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsIpV6MgmtPassed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsIpV6MgmtPassed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsIpV6MgmtPassed=_WwpLeosFlowCpuRateLimitStatsIpV6MgmtPassed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,62),_WwpLeosFlowCpuRateLimitStatsIpV6MgmtPassed_Type())
wwpLeosFlowCpuRateLimitStatsIpV6MgmtPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsIpV6MgmtPassed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsIpV6MgmtDropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsIpV6MgmtDropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsIpV6MgmtDropped=_WwpLeosFlowCpuRateLimitStatsIpV6MgmtDropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,63),_WwpLeosFlowCpuRateLimitStatsIpV6MgmtDropped_Type())
wwpLeosFlowCpuRateLimitStatsIpV6MgmtDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsIpV6MgmtDropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsInet6Passed_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsInet6Passed_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsInet6Passed=_WwpLeosFlowCpuRateLimitStatsInet6Passed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,64),_WwpLeosFlowCpuRateLimitStatsInet6Passed_Type())
wwpLeosFlowCpuRateLimitStatsInet6Passed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsInet6Passed.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsInet6Dropped_Type=Gauge32
_WwpLeosFlowCpuRateLimitStatsInet6Dropped_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsInet6Dropped=_WwpLeosFlowCpuRateLimitStatsInet6Dropped_Object((1,3,6,1,4,1,6141,2,60,6,1,1,32,1,65),_WwpLeosFlowCpuRateLimitStatsInet6Dropped_Type())
wwpLeosFlowCpuRateLimitStatsInet6Dropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsInet6Dropped.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsClearTable_Object=MibTable
wwpLeosFlowCpuRateLimitStatsClearTable=_WwpLeosFlowCpuRateLimitStatsClearTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,33))
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsClearTable.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsClearEntry_Object=MibTableRow
wwpLeosFlowCpuRateLimitStatsClearEntry=_WwpLeosFlowCpuRateLimitStatsClearEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,33,1))
wwpLeosFlowCpuRateLimitStatsClearEntry.setIndexNames((0,_D,_AM))
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsClearEntry.setStatus(_A)
class _WwpLeosFlowCpuRateLimitStatsClearPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_WwpLeosFlowCpuRateLimitStatsClearPort_Type.__name__=_B
_WwpLeosFlowCpuRateLimitStatsClearPort_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsClearPort=_WwpLeosFlowCpuRateLimitStatsClearPort_Object((1,3,6,1,4,1,6141,2,60,6,1,1,33,1,1),_WwpLeosFlowCpuRateLimitStatsClearPort_Type())
wwpLeosFlowCpuRateLimitStatsClearPort.setMaxAccess(_n)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsClearPort.setStatus(_A)
_WwpLeosFlowCpuRateLimitStatsClear_Type=TruthValue
_WwpLeosFlowCpuRateLimitStatsClear_Object=MibTableColumn
wwpLeosFlowCpuRateLimitStatsClear=_WwpLeosFlowCpuRateLimitStatsClear_Object((1,3,6,1,4,1,6141,2,60,6,1,1,33,1,2),_WwpLeosFlowCpuRateLimitStatsClear_Type())
wwpLeosFlowCpuRateLimitStatsClear.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowCpuRateLimitStatsClear.setStatus(_A)
_WwpLeosFlowServiceTotalStatsTable_Object=MibTable
wwpLeosFlowServiceTotalStatsTable=_WwpLeosFlowServiceTotalStatsTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,34))
if mibBuilder.loadTexts:wwpLeosFlowServiceTotalStatsTable.setStatus(_A)
_WwpLeosFlowServiceTotalStatsEntry_Object=MibTableRow
wwpLeosFlowServiceTotalStatsEntry=_WwpLeosFlowServiceTotalStatsEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,34,1))
wwpLeosFlowServiceTotalStatsEntry.setIndexNames((0,_D,_S),(0,_D,_T),(0,_D,_U),(0,_D,_V),(0,_D,_W),(0,_D,_X),(0,_D,_Y),(0,_D,_Z))
if mibBuilder.loadTexts:wwpLeosFlowServiceTotalStatsEntry.setStatus(_A)
_WwpLeosFlowServiceTotalStatsRxHi_Type=Counter32
_WwpLeosFlowServiceTotalStatsRxHi_Object=MibTableColumn
wwpLeosFlowServiceTotalStatsRxHi=_WwpLeosFlowServiceTotalStatsRxHi_Object((1,3,6,1,4,1,6141,2,60,6,1,1,34,1,1),_WwpLeosFlowServiceTotalStatsRxHi_Type())
wwpLeosFlowServiceTotalStatsRxHi.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceTotalStatsRxHi.setStatus(_A)
_WwpLeosFlowServiceTotalStatsRxLo_Type=Counter32
_WwpLeosFlowServiceTotalStatsRxLo_Object=MibTableColumn
wwpLeosFlowServiceTotalStatsRxLo=_WwpLeosFlowServiceTotalStatsRxLo_Object((1,3,6,1,4,1,6141,2,60,6,1,1,34,1,2),_WwpLeosFlowServiceTotalStatsRxLo_Type())
wwpLeosFlowServiceTotalStatsRxLo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceTotalStatsRxLo.setStatus(_A)
_WwpLeosFlowServiceTotalStatsTxHi_Type=Counter32
_WwpLeosFlowServiceTotalStatsTxHi_Object=MibTableColumn
wwpLeosFlowServiceTotalStatsTxHi=_WwpLeosFlowServiceTotalStatsTxHi_Object((1,3,6,1,4,1,6141,2,60,6,1,1,34,1,3),_WwpLeosFlowServiceTotalStatsTxHi_Type())
wwpLeosFlowServiceTotalStatsTxHi.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceTotalStatsTxHi.setStatus(_A)
_WwpLeosFlowServiceTotalStatsTxLo_Type=Counter32
_WwpLeosFlowServiceTotalStatsTxLo_Object=MibTableColumn
wwpLeosFlowServiceTotalStatsTxLo=_WwpLeosFlowServiceTotalStatsTxLo_Object((1,3,6,1,4,1,6141,2,60,6,1,1,34,1,4),_WwpLeosFlowServiceTotalStatsTxLo_Type())
wwpLeosFlowServiceTotalStatsTxLo.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceTotalStatsTxLo.setStatus(_A)
class _WwpLeosFlowServiceTotalStatsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_WwpLeosFlowServiceTotalStatsType_Type.__name__=_B
_WwpLeosFlowServiceTotalStatsType_Object=MibTableColumn
wwpLeosFlowServiceTotalStatsType=_WwpLeosFlowServiceTotalStatsType_Object((1,3,6,1,4,1,6141,2,60,6,1,1,34,1,5),_WwpLeosFlowServiceTotalStatsType_Type())
wwpLeosFlowServiceTotalStatsType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowServiceTotalStatsType.setStatus(_A)
_WwpLeosFlowPortServiceLevelTable_Object=MibTable
wwpLeosFlowPortServiceLevelTable=_WwpLeosFlowPortServiceLevelTable_Object((1,3,6,1,4,1,6141,2,60,6,1,1,40))
if mibBuilder.loadTexts:wwpLeosFlowPortServiceLevelTable.setStatus(_A)
_WwpLeosFlowPortServiceLevelEntry_Object=MibTableRow
wwpLeosFlowPortServiceLevelEntry=_WwpLeosFlowPortServiceLevelEntry_Object((1,3,6,1,4,1,6141,2,60,6,1,1,40,1))
wwpLeosFlowPortServiceLevelEntry.setIndexNames((0,_D,_AN))
if mibBuilder.loadTexts:wwpLeosFlowPortServiceLevelEntry.setStatus(_A)
class _WwpLeosFlowPortServiceLevelPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosFlowPortServiceLevelPort_Type.__name__=_B
_WwpLeosFlowPortServiceLevelPort_Object=MibTableColumn
wwpLeosFlowPortServiceLevelPort=_WwpLeosFlowPortServiceLevelPort_Object((1,3,6,1,4,1,6141,2,60,6,1,1,40,1,1),_WwpLeosFlowPortServiceLevelPort_Type())
wwpLeosFlowPortServiceLevelPort.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFlowPortServiceLevelPort.setStatus(_A)
class _WwpLeosFlowPortServiceLevelMaxBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8000000))
_WwpLeosFlowPortServiceLevelMaxBandwidth_Type.__name__=_B
_WwpLeosFlowPortServiceLevelMaxBandwidth_Object=MibTableColumn
wwpLeosFlowPortServiceLevelMaxBandwidth=_WwpLeosFlowPortServiceLevelMaxBandwidth_Object((1,3,6,1,4,1,6141,2,60,6,1,1,40,1,2),_WwpLeosFlowPortServiceLevelMaxBandwidth_Type())
wwpLeosFlowPortServiceLevelMaxBandwidth.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowPortServiceLevelMaxBandwidth.setStatus(_A)
class _WwpLeosFlowPortServiceLevelQueueSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_r,0),(_K,1),(_L,2),(_M,3),(_N,4),(_s,5),(_t,6),(_u,7),(_v,8),(_w,9)))
_WwpLeosFlowPortServiceLevelQueueSize_Type.__name__=_B
_WwpLeosFlowPortServiceLevelQueueSize_Object=MibTableColumn
wwpLeosFlowPortServiceLevelQueueSize=_WwpLeosFlowPortServiceLevelQueueSize_Object((1,3,6,1,4,1,6141,2,60,6,1,1,40,1,3),_WwpLeosFlowPortServiceLevelQueueSize_Type())
wwpLeosFlowPortServiceLevelQueueSize.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowPortServiceLevelQueueSize.setStatus(_A)
class _WwpLeosFlowPortServiceLevelQueueSizeYellow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4)))
_WwpLeosFlowPortServiceLevelQueueSizeYellow_Type.__name__=_B
_WwpLeosFlowPortServiceLevelQueueSizeYellow_Object=MibTableColumn
wwpLeosFlowPortServiceLevelQueueSizeYellow=_WwpLeosFlowPortServiceLevelQueueSizeYellow_Object((1,3,6,1,4,1,6141,2,60,6,1,1,40,1,4),_WwpLeosFlowPortServiceLevelQueueSizeYellow_Type())
wwpLeosFlowPortServiceLevelQueueSizeYellow.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowPortServiceLevelQueueSizeYellow.setStatus(_A)
class _WwpLeosFlowPortServiceLevelQueueSizeRed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_L,2),(_M,3),(_N,4)))
_WwpLeosFlowPortServiceLevelQueueSizeRed_Type.__name__=_B
_WwpLeosFlowPortServiceLevelQueueSizeRed_Object=MibTableColumn
wwpLeosFlowPortServiceLevelQueueSizeRed=_WwpLeosFlowPortServiceLevelQueueSizeRed_Object((1,3,6,1,4,1,6141,2,60,6,1,1,40,1,5),_WwpLeosFlowPortServiceLevelQueueSizeRed_Type())
wwpLeosFlowPortServiceLevelQueueSizeRed.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowPortServiceLevelQueueSizeRed.setStatus(_A)
class _WwpLeosFlowPortServiceLevelFlowGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_x,1),(_y,2)))
_WwpLeosFlowPortServiceLevelFlowGroup_Type.__name__=_B
_WwpLeosFlowPortServiceLevelFlowGroup_Object=MibTableColumn
wwpLeosFlowPortServiceLevelFlowGroup=_WwpLeosFlowPortServiceLevelFlowGroup_Object((1,3,6,1,4,1,6141,2,60,6,1,1,40,1,6),_WwpLeosFlowPortServiceLevelFlowGroup_Type())
wwpLeosFlowPortServiceLevelFlowGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowPortServiceLevelFlowGroup.setStatus(_A)
class _WwpLeosFlowPortServiceLevelRedCurve_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_WwpLeosFlowPortServiceLevelRedCurve_Type.__name__=_J
_WwpLeosFlowPortServiceLevelRedCurve_Object=MibTableColumn
wwpLeosFlowPortServiceLevelRedCurve=_WwpLeosFlowPortServiceLevelRedCurve_Object((1,3,6,1,4,1,6141,2,60,6,1,1,40,1,7),_WwpLeosFlowPortServiceLevelRedCurve_Type())
wwpLeosFlowPortServiceLevelRedCurve.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosFlowPortServiceLevelRedCurve.setStatus(_A)
class _WwpLeosFlowBurstConfigBacklogLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,131072))
_WwpLeosFlowBurstConfigBacklogLimit_Type.__name__=_J
_WwpLeosFlowBurstConfigBacklogLimit_Object=MibScalar
wwpLeosFlowBurstConfigBacklogLimit=_WwpLeosFlowBurstConfigBacklogLimit_Object((1,3,6,1,4,1,6141,2,60,6,1,1,41),_WwpLeosFlowBurstConfigBacklogLimit_Type())
wwpLeosFlowBurstConfigBacklogLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowBurstConfigBacklogLimit.setStatus(_A)
class _WwpLeosFlowBurstConfigMulticastLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,131072))
_WwpLeosFlowBurstConfigMulticastLimit_Type.__name__=_J
_WwpLeosFlowBurstConfigMulticastLimit_Object=MibScalar
wwpLeosFlowBurstConfigMulticastLimit=_WwpLeosFlowBurstConfigMulticastLimit_Object((1,3,6,1,4,1,6141,2,60,6,1,1,42),_WwpLeosFlowBurstConfigMulticastLimit_Type())
wwpLeosFlowBurstConfigMulticastLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowBurstConfigMulticastLimit.setStatus(_A)
class _WwpLeosFlowBurstConfigVlanPriFltrOnThld_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_WwpLeosFlowBurstConfigVlanPriFltrOnThld_Type.__name__=_B
_WwpLeosFlowBurstConfigVlanPriFltrOnThld_Object=MibScalar
wwpLeosFlowBurstConfigVlanPriFltrOnThld=_WwpLeosFlowBurstConfigVlanPriFltrOnThld_Object((1,3,6,1,4,1,6141,2,60,6,1,1,43),_WwpLeosFlowBurstConfigVlanPriFltrOnThld_Type())
wwpLeosFlowBurstConfigVlanPriFltrOnThld.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowBurstConfigVlanPriFltrOnThld.setStatus(_A)
class _WwpLeosFlowBurstConfigVlanPriFltrOffThld_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_WwpLeosFlowBurstConfigVlanPriFltrOffThld_Type.__name__=_B
_WwpLeosFlowBurstConfigVlanPriFltrOffThld_Object=MibScalar
wwpLeosFlowBurstConfigVlanPriFltrOffThld=_WwpLeosFlowBurstConfigVlanPriFltrOffThld_Object((1,3,6,1,4,1,6141,2,60,6,1,1,44),_WwpLeosFlowBurstConfigVlanPriFltrOffThld_Type())
wwpLeosFlowBurstConfigVlanPriFltrOffThld.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowBurstConfigVlanPriFltrOffThld.setStatus(_A)
class _WwpLeosFlowBurstConfigVlanPriFltrPriMatch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosFlowBurstConfigVlanPriFltrPriMatch_Type.__name__=_B
_WwpLeosFlowBurstConfigVlanPriFltrPriMatch_Object=MibScalar
wwpLeosFlowBurstConfigVlanPriFltrPriMatch=_WwpLeosFlowBurstConfigVlanPriFltrPriMatch_Object((1,3,6,1,4,1,6141,2,60,6,1,1,45),_WwpLeosFlowBurstConfigVlanPriFltrPriMatch_Type())
wwpLeosFlowBurstConfigVlanPriFltrPriMatch.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowBurstConfigVlanPriFltrPriMatch.setStatus(_A)
class _WwpLeosFlowBurstConfigVlanPriFltrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_WwpLeosFlowBurstConfigVlanPriFltrState_Type.__name__=_B
_WwpLeosFlowBurstConfigVlanPriFltrState_Object=MibScalar
wwpLeosFlowBurstConfigVlanPriFltrState=_WwpLeosFlowBurstConfigVlanPriFltrState_Object((1,3,6,1,4,1,6141,2,60,6,1,1,46),_WwpLeosFlowBurstConfigVlanPriFltrState_Type())
wwpLeosFlowBurstConfigVlanPriFltrState.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosFlowBurstConfigVlanPriFltrState.setStatus(_A)
_WwpLeosFlowNotifAttrs_ObjectIdentity=ObjectIdentity
wwpLeosFlowNotifAttrs=_WwpLeosFlowNotifAttrs_ObjectIdentity((1,3,6,1,4,1,6141,2,60,6,1,2))
class _WwpLeosFlowMacMotionAttrOldPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_WwpLeosFlowMacMotionAttrOldPort_Type.__name__=_B
_WwpLeosFlowMacMotionAttrOldPort_Object=MibScalar
wwpLeosFlowMacMotionAttrOldPort=_WwpLeosFlowMacMotionAttrOldPort_Object((1,3,6,1,4,1,6141,2,60,6,1,2,1),_WwpLeosFlowMacMotionAttrOldPort_Type())
wwpLeosFlowMacMotionAttrOldPort.setMaxAccess(_P)
if mibBuilder.loadTexts:wwpLeosFlowMacMotionAttrOldPort.setStatus(_A)
class _WwpLeosFlowMacMotionAttrOldVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_WwpLeosFlowMacMotionAttrOldVlan_Type.__name__=_B
_WwpLeosFlowMacMotionAttrOldVlan_Object=MibScalar
wwpLeosFlowMacMotionAttrOldVlan=_WwpLeosFlowMacMotionAttrOldVlan_Object((1,3,6,1,4,1,6141,2,60,6,1,2,2),_WwpLeosFlowMacMotionAttrOldVlan_Type())
wwpLeosFlowMacMotionAttrOldVlan.setMaxAccess(_P)
if mibBuilder.loadTexts:wwpLeosFlowMacMotionAttrOldVlan.setStatus(_A)
class _WwpLeosFlowMacMotionAttrNewPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_WwpLeosFlowMacMotionAttrNewPort_Type.__name__=_B
_WwpLeosFlowMacMotionAttrNewPort_Object=MibScalar
wwpLeosFlowMacMotionAttrNewPort=_WwpLeosFlowMacMotionAttrNewPort_Object((1,3,6,1,4,1,6141,2,60,6,1,2,3),_WwpLeosFlowMacMotionAttrNewPort_Type())
wwpLeosFlowMacMotionAttrNewPort.setMaxAccess(_P)
if mibBuilder.loadTexts:wwpLeosFlowMacMotionAttrNewPort.setStatus(_A)
class _WwpLeosFlowMacMotionAttrNewVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_WwpLeosFlowMacMotionAttrNewVlan_Type.__name__=_B
_WwpLeosFlowMacMotionAttrNewVlan_Object=MibScalar
wwpLeosFlowMacMotionAttrNewVlan=_WwpLeosFlowMacMotionAttrNewVlan_Object((1,3,6,1,4,1,6141,2,60,6,1,2,4),_WwpLeosFlowMacMotionAttrNewVlan_Type())
wwpLeosFlowMacMotionAttrNewVlan.setMaxAccess(_P)
if mibBuilder.loadTexts:wwpLeosFlowMacMotionAttrNewVlan.setStatus(_A)
_WwpLeosFlowMacMotionAttrMacAddr_Type=MacAddress
_WwpLeosFlowMacMotionAttrMacAddr_Object=MibScalar
wwpLeosFlowMacMotionAttrMacAddr=_WwpLeosFlowMacMotionAttrMacAddr_Object((1,3,6,1,4,1,6141,2,60,6,1,2,5),_WwpLeosFlowMacMotionAttrMacAddr_Type())
wwpLeosFlowMacMotionAttrMacAddr.setMaxAccess(_P)
if mibBuilder.loadTexts:wwpLeosFlowMacMotionAttrMacAddr.setStatus(_A)
_WwpLeosFlowNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosFlowNotificationPrefix=_WwpLeosFlowNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,6,2))
_WwpLeosFlowNotifications_ObjectIdentity=ObjectIdentity
wwpLeosFlowNotifications=_WwpLeosFlowNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,6,2,0))
_WwpLeosFlowMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosFlowMIBConformance=_WwpLeosFlowMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,6,3))
_WwpLeosFlowMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosFlowMIBCompliances=_WwpLeosFlowMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,6,3,1))
_WwpLeosFlowMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosFlowMIBGroups=_WwpLeosFlowMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,6,3,2))
wwpLeosFlowServiceLevelPortOverProvisionedTrap=NotificationType((1,3,6,1,4,1,6141,2,60,6,2,0,1))
wwpLeosFlowServiceLevelPortOverProvisionedTrap.setObjects((_D,_R))
if mibBuilder.loadTexts:wwpLeosFlowServiceLevelPortOverProvisionedTrap.setStatus(_A)
wwpLeosFlowServiceLevelPortUnderProvisionedTrap=NotificationType((1,3,6,1,4,1,6141,2,60,6,2,0,2))
wwpLeosFlowServiceLevelPortUnderProvisionedTrap.setObjects((_D,_R))
if mibBuilder.loadTexts:wwpLeosFlowServiceLevelPortUnderProvisionedTrap.setStatus(_A)
wwpLeosFlowL2SacHighThreshold=NotificationType((1,3,6,1,4,1,6141,2,60,6,2,0,3))
wwpLeosFlowL2SacHighThreshold.setObjects(*((_D,_a),(_D,_b),(_D,_c)))
if mibBuilder.loadTexts:wwpLeosFlowL2SacHighThreshold.setStatus(_A)
wwpLeosFlowL2SacNormalThreshold=NotificationType((1,3,6,1,4,1,6141,2,60,6,2,0,4))
wwpLeosFlowL2SacNormalThreshold.setObjects(*((_D,_a),(_D,_b),(_D,_c)))
if mibBuilder.loadTexts:wwpLeosFlowL2SacNormalThreshold.setStatus(_A)
wwpLeosFlowMacMotionNotification=NotificationType((1,3,6,1,4,1,6141,2,60,6,2,0,5))
wwpLeosFlowMacMotionNotification.setObjects(*((_D,_AO),(_D,_AP),(_D,_AQ),(_D,_AR),(_D,_AS)))
if mibBuilder.loadTexts:wwpLeosFlowMacMotionNotification.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'PriorityMapping':PriorityMapping,'wwpLeosFlowMIB':wwpLeosFlowMIB,'wwpLeosFlowMIBObjects':wwpLeosFlowMIBObjects,'wwpLeosFlow':wwpLeosFlow,'wwpLeosFlowAgeTime':wwpLeosFlowAgeTime,'wwpLeosFlowAgeTimeState':wwpLeosFlowAgeTimeState,'wwpLeosFlowServiceLevelTable':wwpLeosFlowServiceLevelTable,'wwpLeosFlowServiceLevelEntry':wwpLeosFlowServiceLevelEntry,_q:wwpLeosFlowServiceLevelDirection,_R:wwpLeosFlowServiceLevelPort,_p:wwpLeosFlowServiceLevelId,'wwpLeosFlowServiceLevelName':wwpLeosFlowServiceLevelName,'wwpLeosFlowServiceLevelPriority':wwpLeosFlowServiceLevelPriority,'wwpLeosFlowServiceLevelQueueSize':wwpLeosFlowServiceLevelQueueSize,'wwpLeosFlowServiceLevelDropEligibility':wwpLeosFlowServiceLevelDropEligibility,'wwpLeosFlowServiceLevelShareEligibility':wwpLeosFlowServiceLevelShareEligibility,'wwpLeosFlowServiceLevelCirBW':wwpLeosFlowServiceLevelCirBW,'wwpLeosFlowServiceLevelPirBW':wwpLeosFlowServiceLevelPirBW,'wwpLeosFlowServiceStatus':wwpLeosFlowServiceStatus,'wwpLeosFlowServiceRedCurveId':wwpLeosFlowServiceRedCurveId,'wwpLeosFlowServiceLevelQueueSizeYellow':wwpLeosFlowServiceLevelQueueSizeYellow,'wwpLeosFlowServiceLevelQueueSizeRed':wwpLeosFlowServiceLevelQueueSizeRed,'wwpLeosFlowServiceLevelFlowGroup':wwpLeosFlowServiceLevelFlowGroup,'wwpLeosFlowServiceMappingTable':wwpLeosFlowServiceMappingTable,'wwpLeosFlowServiceMappingEntry':wwpLeosFlowServiceMappingEntry,_d:wwpLeosFlowServiceMapVid,_e:wwpLeosFlowServiceMapSrcPort,_f:wwpLeosFlowServiceMapSrcTag,_g:wwpLeosFlowServiceMapDstPort,_h:wwpLeosFlowServiceMapDstTag,_i:wwpLeosFlowServiceMapSrcPri,_j:wwpLeosFlowServiceMapProtocolType,_k:wwpLeosFlowServiceMapProtocolPortNum,'wwpLeosFlowServiceMapDstSlidId':wwpLeosFlowServiceMapDstSlidId,'wwpLeosFlowServiceMapSrcSlidId':wwpLeosFlowServiceMapSrcSlidId,'wwpLeosFlowServiceMapPriRemarkStatus':wwpLeosFlowServiceMapPriRemarkStatus,'wwpLeosFlowServiceMapRemarkPri':wwpLeosFlowServiceMapRemarkPri,'wwpLeosFlowServiceMapStatus':wwpLeosFlowServiceMapStatus,'wwpLeosFlowServiceACTable':wwpLeosFlowServiceACTable,'wwpLeosFlowServiceACEntry':wwpLeosFlowServiceACEntry,_z:wwpLeosFlowServiceACPortId,_A0:wwpLeosFlowServiceACVid,'wwpLeosFlowServiceACMaxDynamicMacCount':wwpLeosFlowServiceACMaxDynamicMacCount,'wwpLeosFlowServiceACDynamicNonFilteredMacCount':wwpLeosFlowServiceACDynamicNonFilteredMacCount,'wwpLeosFlowServiceACDynamicFilteredMacCount':wwpLeosFlowServiceACDynamicFilteredMacCount,'wwpLeosFlowServiceACStatus':wwpLeosFlowServiceACStatus,'wwpLeosFlowServiceACForwardLearning':wwpLeosFlowServiceACForwardLearning,'wwpLeosFlowStaticMacTable':wwpLeosFlowStaticMacTable,'wwpLeosFlowStaticMacEntry':wwpLeosFlowStaticMacEntry,_A1:wwpLeosFlowSMVid,_A2:wwpLeosFlowSMMacAddr,'wwpLeosFlowSMPortId':wwpLeosFlowSMPortId,'wwpLeosFlowSMTag':wwpLeosFlowSMTag,'wwpLeosFlowSMStatus':wwpLeosFlowSMStatus,'wwpLeosFlowLearnTable':wwpLeosFlowLearnTable,'wwpLeosFlowLearnEntry':wwpLeosFlowLearnEntry,_A3:wwpLeosFlowLearnVid,_A4:wwpLeosFlowLearnAddr,_A5:wwpLeosFlowLearnSrcPort,_A6:wwpLeosFlowLearnSrcTag,_A7:wwpLeosFlowLearnSrcPri,_A8:wwpLeosFlowLearnAddrType,'wwpLeosFlowLearnDstPort':wwpLeosFlowLearnDstPort,'wwpLeosFlowLearnDstTag':wwpLeosFlowLearnDstTag,'wwpLeosFlowLearnType':wwpLeosFlowLearnType,'wwpLeosFlowLearnIsFiltered':wwpLeosFlowLearnIsFiltered,'wwpLeosFlowServiceStatsTable':wwpLeosFlowServiceStatsTable,'wwpLeosFlowServiceStatsEntry':wwpLeosFlowServiceStatsEntry,'wwpLeosFlowServiceStatsRxHi':wwpLeosFlowServiceStatsRxHi,'wwpLeosFlowServiceStatsRxLo':wwpLeosFlowServiceStatsRxLo,'wwpLeosFlowServiceStatsTxHi':wwpLeosFlowServiceStatsTxHi,'wwpLeosFlowServiceStatsTxLo':wwpLeosFlowServiceStatsTxLo,'wwpLeosFlowServiceStatsType':wwpLeosFlowServiceStatsType,'wwpLeosFlowMacFindTable':wwpLeosFlowMacFindTable,'wwpLeosFlowMacFindEntry':wwpLeosFlowMacFindEntry,_AA:wwpLeosFlowMacFindMacAddr,_A9:wwpLeosFlowMacFindVlanId,'wwpLeosFlowMacFindPort':wwpLeosFlowMacFindPort,'wwpLeosFlowMacFindVlanTag':wwpLeosFlowMacFindVlanTag,'wwpLeosFlowPriRemapTable':wwpLeosFlowPriRemapTable,'wwpLeosFlowPriRemapEntry':wwpLeosFlowPriRemapEntry,_AB:wwpLeosFlowUserPri,'wwpLeosFlowRemappedPri':wwpLeosFlowRemappedPri,'wwpLeosFlowSMappingTable':wwpLeosFlowSMappingTable,'wwpLeosFlowSMappingEntry':wwpLeosFlowSMappingEntry,_S:wwpLeosFlowSMappingNetType,_T:wwpLeosFlowSMappingNetValue,_U:wwpLeosFlowSMappingSrcType,_V:wwpLeosFlowSMappingSrcValue,_W:wwpLeosFlowSMappingDstType,_X:wwpLeosFlowSMappingDstValue,_Y:wwpLeosFlowSMappingCosType,_Z:wwpLeosFlowSMappingCosValue,'wwpLeosFlowSMappingDstSlid':wwpLeosFlowSMappingDstSlid,'wwpLeosFlowSMappingSrcSlid':wwpLeosFlowSMappingSrcSlid,'wwpLeosFlowSMappingStatus':wwpLeosFlowSMappingStatus,'wwpLeosFlowSMappingRedCurveOffset':wwpLeosFlowSMappingRedCurveOffset,'wwpLeosFlowSMappingCpuPort':wwpLeosFlowSMappingCpuPort,'wwpLeosFlowSMappingStatsTable':wwpLeosFlowSMappingStatsTable,'wwpLeosFlowSMappingStatsEntry':wwpLeosFlowSMappingStatsEntry,'wwpLeosFlowSMappingStatsRxHi':wwpLeosFlowSMappingStatsRxHi,'wwpLeosFlowSMappingStatsRxLo':wwpLeosFlowSMappingStatsRxLo,'wwpLeosFlowSMappingStatsTxHi':wwpLeosFlowSMappingStatsTxHi,'wwpLeosFlowSMappingStatsTxLo':wwpLeosFlowSMappingStatsTxLo,'wwpLeosFlowSMappingStatsType':wwpLeosFlowSMappingStatsType,'wwpLeosFlowCosSync1dToExpTable':wwpLeosFlowCosSync1dToExpTable,'wwpLeosFlowCosSync1dToExpEntry':wwpLeosFlowCosSync1dToExpEntry,_AC:wwpLeosFlowCosSync1dToExpMapFrom,'wwpLeosFlowCosSync1dToExpMapTo':wwpLeosFlowCosSync1dToExpMapTo,'wwpLeosFlowCosSyncExpTo1dTable':wwpLeosFlowCosSyncExpTo1dTable,'wwpLeosFlowCosSyncExpTo1dEntry':wwpLeosFlowCosSyncExpTo1dEntry,_AD:wwpLeosFlowCosSyncExpTo1dMapFrom,'wwpLeosFlowCosSyncExpTo1dMapTo':wwpLeosFlowCosSyncExpTo1dMapTo,'wwpLeosFlowCosSyncIpPrecTo1dTable':wwpLeosFlowCosSyncIpPrecTo1dTable,'wwpLeosFlowCosSyncIpPrecTo1dEntry':wwpLeosFlowCosSyncIpPrecTo1dEntry,_AE:wwpLeosFlowCosSyncIpPrecTo1dMapFrom,'wwpLeosFlowCosSyncIpPrecTo1dMapTo':wwpLeosFlowCosSyncIpPrecTo1dMapTo,'wwpLeosFlowCosSyncStdPhbTo1dTable':wwpLeosFlowCosSyncStdPhbTo1dTable,'wwpLeosFlowCosSyncStdPhbTo1dEntry':wwpLeosFlowCosSyncStdPhbTo1dEntry,_AF:wwpLeosFlowCosSyncStdPhbTo1dMapFrom,'wwpLeosFlowCosSyncStdPhbTo1dMapTo':wwpLeosFlowCosSyncStdPhbTo1dMapTo,'wwpLeosFlowL2SacTable':wwpLeosFlowL2SacTable,'wwpLeosFlowL2SacEntry':wwpLeosFlowL2SacEntry,_a:wwpLeosFlowL2SacPortId,_b:wwpLeosFlowL2SacNetType,_c:wwpLeosFlowSacNetValue,'wwpLeosFlowL2SacLimit':wwpLeosFlowL2SacLimit,'wwpLeosFlowL2SacCurMac':wwpLeosFlowL2SacCurMac,'wwpLeosFlowL2SacCurFilteredMac':wwpLeosFlowL2SacCurFilteredMac,'wwpLeosFlowL2SacOperState':wwpLeosFlowL2SacOperState,'wwpLeosFlowL2SacRowStatus':wwpLeosFlowL2SacRowStatus,'wwpLeosFlowL2SacTrapState':wwpLeosFlowL2SacTrapState,'wwpLeosFlowStrictQueuingState':wwpLeosFlowStrictQueuingState,'wwpLeosFlowBwCalcMode':wwpLeosFlowBwCalcMode,'wwpLeosFlowGlobal':wwpLeosFlowGlobal,'wwpLeosFlowServiceLevelFlowGroupState':wwpLeosFlowServiceLevelFlowGroupState,'wwpLeosFlowServiceMappingCosRedMappingState':wwpLeosFlowServiceMappingCosRedMappingState,'wwpLeosFlowServiceAllRedCurveUnset':wwpLeosFlowServiceAllRedCurveUnset,'wwpLeosFlowServiceRedCurveTable':wwpLeosFlowServiceRedCurveTable,'wwpLeosFlowServiceRedCurveEntry':wwpLeosFlowServiceRedCurveEntry,_AG:wwpLeosFlowServiceRedCurveIndex,'wwpLeosFlowServiceRedCurveName':wwpLeosFlowServiceRedCurveName,'wwpLeosFlowServiceRedCurveState':wwpLeosFlowServiceRedCurveState,'wwpLeosFlowServiceRedCurveMinThreshold':wwpLeosFlowServiceRedCurveMinThreshold,'wwpLeosFlowServiceRedCurveMaxThreshold':wwpLeosFlowServiceRedCurveMaxThreshold,'wwpLeosFlowServiceRedCurveDropProbability':wwpLeosFlowServiceRedCurveDropProbability,'wwpLeosFlowServiceRedCurveUnset':wwpLeosFlowServiceRedCurveUnset,'wwpLeosFlowCos1dToRedCurveOffsetTable':wwpLeosFlowCos1dToRedCurveOffsetTable,'wwpLeosFlowCos1dToRedCurveOffsetEntry':wwpLeosFlowCos1dToRedCurveOffsetEntry,_AH:wwpLeosFlowCos1dToRedCurveOffset1dValue,'wwpLeosFlowCos1dToRedCurveOffsetValue':wwpLeosFlowCos1dToRedCurveOffsetValue,'wwpLeosFlowCosMapPCPTo1dTable':wwpLeosFlowCosMapPCPTo1dTable,'wwpLeosFlowCosMapPCPTo1dEntry':wwpLeosFlowCosMapPCPTo1dEntry,_AI:wwpLeosFlowCosMapPCPTo1dMapFrom,'wwpLeosFlowCosMapPCPTo1dMapTo':wwpLeosFlowCosMapPCPTo1dMapTo,'wwpLeosFlowCosMap1dToPCPTable':wwpLeosFlowCosMap1dToPCPTable,'wwpLeosFlowCosMap1dToPCPEntry':wwpLeosFlowCosMap1dToPCPEntry,_AJ:wwpLeosFlowCosMap1dToPCPMapFrom,'wwpLeosFlowCosMap1dToPCPMapTo':wwpLeosFlowCosMap1dToPCPMapTo,'wwpLeosFlowMacMotionEventsEnable':wwpLeosFlowMacMotionEventsEnable,'wwpLeosFlowMacMotionEventsInterval':wwpLeosFlowMacMotionEventsInterval,'wwpLeosFlowCpuRateLimitsEnable':wwpLeosFlowCpuRateLimitsEnable,'wwpLeosFlowCpuRateLimitTable':wwpLeosFlowCpuRateLimitTable,'wwpLeosFlowCpuRateLimitEntry':wwpLeosFlowCpuRateLimitEntry,_AK:wwpLeosFlowCpuRateLimitPort,'wwpLeosFlowCpuRateLimitEnable':wwpLeosFlowCpuRateLimitEnable,'wwpLeosFlowCpuRateLimitBootp':wwpLeosFlowCpuRateLimitBootp,'wwpLeosFlowCpuRateLimitCfm':wwpLeosFlowCpuRateLimitCfm,'wwpLeosFlowCpuRateLimitCft':wwpLeosFlowCpuRateLimitCft,'wwpLeosFlowCpuRateLimitDot1x':wwpLeosFlowCpuRateLimitDot1x,'wwpLeosFlowCpuRateLimitOam':wwpLeosFlowCpuRateLimitOam,'wwpLeosFlowCpuRateLimitEprArp':wwpLeosFlowCpuRateLimitEprArp,'wwpLeosFlowCpuRateLimitIgmp':wwpLeosFlowCpuRateLimitIgmp,'wwpLeosFlowCpuRateLimitInet':wwpLeosFlowCpuRateLimitInet,'wwpLeosFlowCpuRateLimitLacp':wwpLeosFlowCpuRateLimitLacp,'wwpLeosFlowCpuRateLimitLldp':wwpLeosFlowCpuRateLimitLldp,'wwpLeosFlowCpuRateLimitMpls':wwpLeosFlowCpuRateLimitMpls,'wwpLeosFlowCpuRateLimitMstp':wwpLeosFlowCpuRateLimitMstp,'wwpLeosFlowCpuRateLimitPeArp':wwpLeosFlowCpuRateLimitPeArp,'wwpLeosFlowCpuRateLimitPvst':wwpLeosFlowCpuRateLimitPvst,'wwpLeosFlowCpuRateLimitRstp':wwpLeosFlowCpuRateLimitRstp,'wwpLeosFlowCpuRateLimitLpbk':wwpLeosFlowCpuRateLimitLpbk,'wwpLeosFlowCpuRateLimitRmtLpbk':wwpLeosFlowCpuRateLimitRmtLpbk,'wwpLeosFlowCpuRateLimitCxeRx':wwpLeosFlowCpuRateLimitCxeRx,'wwpLeosFlowCpuRateLimitCxeTx':wwpLeosFlowCpuRateLimitCxeTx,'wwpLeosFlowCpuRateLimitTwamp':wwpLeosFlowCpuRateLimitTwamp,'wwpLeosFlowCpuRateLimitDflt':wwpLeosFlowCpuRateLimitDflt,'wwpLeosFlowCpuRateLimitTwampRsp':wwpLeosFlowCpuRateLimitTwampRsp,'wwpLeosFlowCpuRateLimitMultiCast':wwpLeosFlowCpuRateLimitMultiCast,'wwpLeosFlowCpuRateLimitBroadCast':wwpLeosFlowCpuRateLimitBroadCast,'wwpLeosFlowCpuRateLimitArp':wwpLeosFlowCpuRateLimitArp,'wwpLeosFlowCpuRateLimitIcmp':wwpLeosFlowCpuRateLimitIcmp,'wwpLeosFlowCpuRateLimitTcpSyn':wwpLeosFlowCpuRateLimitTcpSyn,'wwpLeosFlowCpuRateLimitRaps':wwpLeosFlowCpuRateLimitRaps,'wwpLeosFlowCpuRateLimitIpMgmt':wwpLeosFlowCpuRateLimitIpMgmt,'wwpLeosFlowCpuRateLimitIpControl':wwpLeosFlowCpuRateLimitIpControl,'wwpLeosFlowCpuRateLimitIpV6Mgmt':wwpLeosFlowCpuRateLimitIpV6Mgmt,'wwpLeosFlowCpuRateLimitInet6':wwpLeosFlowCpuRateLimitInet6,'wwpLeosFlowCpuRateLimitStatsTable':wwpLeosFlowCpuRateLimitStatsTable,'wwpLeosFlowCpuRateLimitStatsEntry':wwpLeosFlowCpuRateLimitStatsEntry,_AL:wwpLeosFlowCpuRateLimitStatsPort,'wwpLeosFlowCpuRateLimitStatsBootpPassed':wwpLeosFlowCpuRateLimitStatsBootpPassed,'wwpLeosFlowCpuRateLimitStatsCfmPassed':wwpLeosFlowCpuRateLimitStatsCfmPassed,'wwpLeosFlowCpuRateLimitStatsCftPassed':wwpLeosFlowCpuRateLimitStatsCftPassed,'wwpLeosFlowCpuRateLimitStatsDot1xPassed':wwpLeosFlowCpuRateLimitStatsDot1xPassed,'wwpLeosFlowCpuRateLimitStatsOamPassed':wwpLeosFlowCpuRateLimitStatsOamPassed,'wwpLeosFlowCpuRateLimitStatsEprArpPassed':wwpLeosFlowCpuRateLimitStatsEprArpPassed,'wwpLeosFlowCpuRateLimitStatsIgmpPassed':wwpLeosFlowCpuRateLimitStatsIgmpPassed,'wwpLeosFlowCpuRateLimitStatsInetPassed':wwpLeosFlowCpuRateLimitStatsInetPassed,'wwpLeosFlowCpuRateLimitStatsLacpPassed':wwpLeosFlowCpuRateLimitStatsLacpPassed,'wwpLeosFlowCpuRateLimitStatsLldpPassed':wwpLeosFlowCpuRateLimitStatsLldpPassed,'wwpLeosFlowCpuRateLimitStatsMplsPassed':wwpLeosFlowCpuRateLimitStatsMplsPassed,'wwpLeosFlowCpuRateLimitStatsMstpPassed':wwpLeosFlowCpuRateLimitStatsMstpPassed,'wwpLeosFlowCpuRateLimitStatsPeArpPassed':wwpLeosFlowCpuRateLimitStatsPeArpPassed,'wwpLeosFlowCpuRateLimitStatsPvstPassed':wwpLeosFlowCpuRateLimitStatsPvstPassed,'wwpLeosFlowCpuRateLimitStatsRstpPassed':wwpLeosFlowCpuRateLimitStatsRstpPassed,'wwpLeosFlowCpuRateLimitStatsLpbkPassed':wwpLeosFlowCpuRateLimitStatsLpbkPassed,'wwpLeosFlowCpuRateLimitStatsRmtLpbkPassed':wwpLeosFlowCpuRateLimitStatsRmtLpbkPassed,'wwpLeosFlowCpuRateLimitStatsCxeRxPassed':wwpLeosFlowCpuRateLimitStatsCxeRxPassed,'wwpLeosFlowCpuRateLimitStatsCxeTxPassed':wwpLeosFlowCpuRateLimitStatsCxeTxPassed,'wwpLeosFlowCpuRateLimitStatsTwampPassed':wwpLeosFlowCpuRateLimitStatsTwampPassed,'wwpLeosFlowCpuRateLimitStatsDfltPassed':wwpLeosFlowCpuRateLimitStatsDfltPassed,'wwpLeosFlowCpuRateLimitStatsBootpDropped':wwpLeosFlowCpuRateLimitStatsBootpDropped,'wwpLeosFlowCpuRateLimitStatsCfmDropped':wwpLeosFlowCpuRateLimitStatsCfmDropped,'wwpLeosFlowCpuRateLimitStatsCftDropped':wwpLeosFlowCpuRateLimitStatsCftDropped,'wwpLeosFlowCpuRateLimitStatsDot1xDropped':wwpLeosFlowCpuRateLimitStatsDot1xDropped,'wwpLeosFlowCpuRateLimitStatsOamDropped':wwpLeosFlowCpuRateLimitStatsOamDropped,'wwpLeosFlowCpuRateLimitStatsEprArpDropped':wwpLeosFlowCpuRateLimitStatsEprArpDropped,'wwpLeosFlowCpuRateLimitStatsIgmpDropped':wwpLeosFlowCpuRateLimitStatsIgmpDropped,'wwpLeosFlowCpuRateLimitStatsInetDropped':wwpLeosFlowCpuRateLimitStatsInetDropped,'wwpLeosFlowCpuRateLimitStatsLacpDropped':wwpLeosFlowCpuRateLimitStatsLacpDropped,'wwpLeosFlowCpuRateLimitStatsLldpDropped':wwpLeosFlowCpuRateLimitStatsLldpDropped,'wwpLeosFlowCpuRateLimitStatsMplsDropped':wwpLeosFlowCpuRateLimitStatsMplsDropped,'wwpLeosFlowCpuRateLimitStatsMstpDropped':wwpLeosFlowCpuRateLimitStatsMstpDropped,'wwpLeosFlowCpuRateLimitStatsPeArpDropped':wwpLeosFlowCpuRateLimitStatsPeArpDropped,'wwpLeosFlowCpuRateLimitStatsPvstDropped':wwpLeosFlowCpuRateLimitStatsPvstDropped,'wwpLeosFlowCpuRateLimitStatsRstpDropped':wwpLeosFlowCpuRateLimitStatsRstpDropped,'wwpLeosFlowCpuRateLimitStatsLpbkDropped':wwpLeosFlowCpuRateLimitStatsLpbkDropped,'wwpLeosFlowCpuRateLimitStatsRmtLpbkDropped':wwpLeosFlowCpuRateLimitStatsRmtLpbkDropped,'wwpLeosFlowCpuRateLimitStatsCxeRxDropped':wwpLeosFlowCpuRateLimitStatsCxeRxDropped,'wwpLeosFlowCpuRateLimitStatsCxeTxDropped':wwpLeosFlowCpuRateLimitStatsCxeTxDropped,'wwpLeosFlowCpuRateLimitStatsTwampDropped':wwpLeosFlowCpuRateLimitStatsTwampDropped,'wwpLeosFlowCpuRateLimitStatsDfltDropped':wwpLeosFlowCpuRateLimitStatsDfltDropped,'wwpLeosFlowCpuRateLimitStatsTwampRspPassed':wwpLeosFlowCpuRateLimitStatsTwampRspPassed,'wwpLeosFlowCpuRateLimitStatsTwampRspDropped':wwpLeosFlowCpuRateLimitStatsTwampRspDropped,'wwpLeosFlowCpuRateLimitStatsMultiCastPassed':wwpLeosFlowCpuRateLimitStatsMultiCastPassed,'wwpLeosFlowCpuRateLimitStatsMultiCastDropped':wwpLeosFlowCpuRateLimitStatsMultiCastDropped,'wwpLeosFlowCpuRateLimitStatsBroadCastPassed':wwpLeosFlowCpuRateLimitStatsBroadCastPassed,'wwpLeosFlowCpuRateLimitStatsBroadCastDropped':wwpLeosFlowCpuRateLimitStatsBroadCastDropped,'wwpLeosFlowCpuRateLimitStatsArpPassed':wwpLeosFlowCpuRateLimitStatsArpPassed,'wwpLeosFlowCpuRateLimitStatsArpDropped':wwpLeosFlowCpuRateLimitStatsArpDropped,'wwpLeosFlowCpuRateLimitStatsIcmpPassed':wwpLeosFlowCpuRateLimitStatsIcmpPassed,'wwpLeosFlowCpuRateLimitStatsIcmpDropped':wwpLeosFlowCpuRateLimitStatsIcmpDropped,'wwpLeosFlowCpuRateLimitStatsTcpSynPassed':wwpLeosFlowCpuRateLimitStatsTcpSynPassed,'wwpLeosFlowCpuRateLimitStatsTcpSynDropped':wwpLeosFlowCpuRateLimitStatsTcpSynDropped,'wwpLeosFlowCpuRateLimitStatsRapsPassed':wwpLeosFlowCpuRateLimitStatsRapsPassed,'wwpLeosFlowCpuRateLimitStatsRapsDropped':wwpLeosFlowCpuRateLimitStatsRapsDropped,'wwpLeosFlowCpuRateLimitStatsIpMgmtPassed':wwpLeosFlowCpuRateLimitStatsIpMgmtPassed,'wwpLeosFlowCpuRateLimitStatsIpMgmtDropped':wwpLeosFlowCpuRateLimitStatsIpMgmtDropped,'wwpLeosFlowCpuRateLimitStatsIpControlPassed':wwpLeosFlowCpuRateLimitStatsIpControlPassed,'wwpLeosFlowCpuRateLimitStatsIpControlDropped':wwpLeosFlowCpuRateLimitStatsIpControlDropped,'wwpLeosFlowCpuRateLimitStatsIpV6MgmtPassed':wwpLeosFlowCpuRateLimitStatsIpV6MgmtPassed,'wwpLeosFlowCpuRateLimitStatsIpV6MgmtDropped':wwpLeosFlowCpuRateLimitStatsIpV6MgmtDropped,'wwpLeosFlowCpuRateLimitStatsInet6Passed':wwpLeosFlowCpuRateLimitStatsInet6Passed,'wwpLeosFlowCpuRateLimitStatsInet6Dropped':wwpLeosFlowCpuRateLimitStatsInet6Dropped,'wwpLeosFlowCpuRateLimitStatsClearTable':wwpLeosFlowCpuRateLimitStatsClearTable,'wwpLeosFlowCpuRateLimitStatsClearEntry':wwpLeosFlowCpuRateLimitStatsClearEntry,_AM:wwpLeosFlowCpuRateLimitStatsClearPort,'wwpLeosFlowCpuRateLimitStatsClear':wwpLeosFlowCpuRateLimitStatsClear,'wwpLeosFlowServiceTotalStatsTable':wwpLeosFlowServiceTotalStatsTable,'wwpLeosFlowServiceTotalStatsEntry':wwpLeosFlowServiceTotalStatsEntry,'wwpLeosFlowServiceTotalStatsRxHi':wwpLeosFlowServiceTotalStatsRxHi,'wwpLeosFlowServiceTotalStatsRxLo':wwpLeosFlowServiceTotalStatsRxLo,'wwpLeosFlowServiceTotalStatsTxHi':wwpLeosFlowServiceTotalStatsTxHi,'wwpLeosFlowServiceTotalStatsTxLo':wwpLeosFlowServiceTotalStatsTxLo,'wwpLeosFlowServiceTotalStatsType':wwpLeosFlowServiceTotalStatsType,'wwpLeosFlowPortServiceLevelTable':wwpLeosFlowPortServiceLevelTable,'wwpLeosFlowPortServiceLevelEntry':wwpLeosFlowPortServiceLevelEntry,_AN:wwpLeosFlowPortServiceLevelPort,'wwpLeosFlowPortServiceLevelMaxBandwidth':wwpLeosFlowPortServiceLevelMaxBandwidth,'wwpLeosFlowPortServiceLevelQueueSize':wwpLeosFlowPortServiceLevelQueueSize,'wwpLeosFlowPortServiceLevelQueueSizeYellow':wwpLeosFlowPortServiceLevelQueueSizeYellow,'wwpLeosFlowPortServiceLevelQueueSizeRed':wwpLeosFlowPortServiceLevelQueueSizeRed,'wwpLeosFlowPortServiceLevelFlowGroup':wwpLeosFlowPortServiceLevelFlowGroup,'wwpLeosFlowPortServiceLevelRedCurve':wwpLeosFlowPortServiceLevelRedCurve,'wwpLeosFlowBurstConfigBacklogLimit':wwpLeosFlowBurstConfigBacklogLimit,'wwpLeosFlowBurstConfigMulticastLimit':wwpLeosFlowBurstConfigMulticastLimit,'wwpLeosFlowBurstConfigVlanPriFltrOnThld':wwpLeosFlowBurstConfigVlanPriFltrOnThld,'wwpLeosFlowBurstConfigVlanPriFltrOffThld':wwpLeosFlowBurstConfigVlanPriFltrOffThld,'wwpLeosFlowBurstConfigVlanPriFltrPriMatch':wwpLeosFlowBurstConfigVlanPriFltrPriMatch,'wwpLeosFlowBurstConfigVlanPriFltrState':wwpLeosFlowBurstConfigVlanPriFltrState,'wwpLeosFlowNotifAttrs':wwpLeosFlowNotifAttrs,_AO:wwpLeosFlowMacMotionAttrOldPort,_AP:wwpLeosFlowMacMotionAttrOldVlan,_AQ:wwpLeosFlowMacMotionAttrNewPort,_AR:wwpLeosFlowMacMotionAttrNewVlan,_AS:wwpLeosFlowMacMotionAttrMacAddr,'wwpLeosFlowNotificationPrefix':wwpLeosFlowNotificationPrefix,'wwpLeosFlowNotifications':wwpLeosFlowNotifications,'wwpLeosFlowServiceLevelPortOverProvisionedTrap':wwpLeosFlowServiceLevelPortOverProvisionedTrap,'wwpLeosFlowServiceLevelPortUnderProvisionedTrap':wwpLeosFlowServiceLevelPortUnderProvisionedTrap,'wwpLeosFlowL2SacHighThreshold':wwpLeosFlowL2SacHighThreshold,'wwpLeosFlowL2SacNormalThreshold':wwpLeosFlowL2SacNormalThreshold,'wwpLeosFlowMacMotionNotification':wwpLeosFlowMacMotionNotification,'wwpLeosFlowMIBConformance':wwpLeosFlowMIBConformance,'wwpLeosFlowMIBCompliances':wwpLeosFlowMIBCompliances,'wwpLeosFlowMIBGroups':wwpLeosFlowMIBGroups})