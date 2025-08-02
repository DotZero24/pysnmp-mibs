_Am='interfaceTopNGroup'
_Al='interfaceTopNValue64'
_Ak='interfaceTopNValue'
_Aj='interfaceTopNDataSourceIndex'
_Ai='interfaceTopNRowStatus'
_Ah='interfaceTopNLastCompletionTime'
_Ag='interfaceTopNOwner'
_Af='interfaceTopNStartTime'
_Ae='interfaceTopNGrantedSize'
_Ad='interfaceTopNRequestedSize'
_Ac='interfaceTopNDuration'
_Ab='interfaceTopNTimeRemaining'
_Aa='interfaceTopNNormalizationFactor'
_AZ='interfaceTopNNormalizationReq'
_AY='interfaceTopNObjectSampleType'
_AX='interfaceTopNObjectVariable'
_AW='interfaceTopNCaps'
_AV='interfaceTopNIndex'
_AU='not-accessible'
_AT='dot1dTpPortInDiscards'
_AS='dot1dTpPortOutFrames'
_AR='dot1dTpPortInFrames'
_AQ='etherStatsPkts1024to1518Octets'
_AP='etherStatsPkts512to1023Octets'
_AO='etherStatsPkts256to511Octets'
_AN='etherStatsPkts128to255Octets'
_AM='etherStatsPkts65to127Octets'
_AL='etherStatsPkts64Octets'
_AK='etherStatsCollisions'
_AJ='etherStatsJabbers'
_AI='etherStatsFragments'
_AH='etherStatsOversizePkts'
_AG='etherStatsUndersizePkts'
_AF='etherStatsCRCAlignErrors'
_AE='etherStatsMulticastPkts'
_AD='etherStatsBroadcastPkts'
_AC='etherStatsPkts'
_AB='etherStatsOctets'
_AA='etherStatsDropEvents'
_A9='dot5StatsFreqErrors'
_A8='dot5StatsSingles'
_A7='dot5StatsRemoves'
_A6='dot5StatsLobeWires'
_A5='dot5StatsRecoverys'
_A4='dot5StatsTransmitBeacons'
_A3='dot5StatsSignalLoss'
_A2='dot5StatsHardErrors'
_A1='dot5StatsSoftErrors'
_A0='dot5StatsTokenErrors'
_z='dot5StatsFrameCopiedErrors'
_y='dot5StatsReceiveCongestions'
_x='dot5StatsLostFrameErrors'
_w='dot5StatsInternalErrors'
_v='dot5StatsAbortTransErrors'
_u='dot5StatsACErrors'
_t='dot5StatsBurstErrors'
_s='dot5StatsLineErrors'
_r='dot3OutPauseFrames'
_q='dot3InPauseFrames'
_p='dot3StatsSymbolErrors'
_o='dot3StatsInternalMacRxErrors'
_n='dot3StatsFrameTooLongs'
_m='dot3StatsCarrierSenseErrors'
_l='dot3StatsInternalMacTxErrors'
_k='dot3StatsExcessiveCollisions'
_j='dot3StatsLateCollisions'
_i='dot3StatsDeferredTransmissions'
_h='dot3StatsSQETestErrors'
_g='dot3StatsMultipleCollisionFrames'
_f='dot3StatsSingleCollisionFrames'
_e='dot3StatsFCSErrors'
_d='dot3StatsAlignmentErrors'
_c='ifHCOutBroadcastPkts'
_b='ifHCOutMulticastPkts'
_a='ifHCOutUcastPkts'
_Z='ifHCOutOctets'
_Y='ifHCInBroadcastPkts'
_X='ifHCInMulticastPkts'
_W='ifHCInUcastPkts'
_V='ifHCInOctets'
_U='ifOutBroadcastPkts'
_T='ifOutMulticastPkts'
_S='ifInBroadcastPkts'
_R='ifInMulticastPkts'
_Q='ifOutErrors'
_P='ifOutDiscards'
_O='ifOutNUcastPkts'
_N='ifOutUcastPkts'
_M='ifOutOctets'
_L='ifInUnknownProtos'
_K='ifInErrors'
_J='ifInDiscards'
_I='ifInNUcastPkts'
_H='ifInUcastPkts'
_G='ifInOctets'
_F='interfaceTopNControlIndex'
_E='read-create'
_D='read-only'
_C='Integer32'
_B='INTERFACETOPN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
OwnerString,rmon=mibBuilder.importSymbols('RMON-MIB','OwnerString','rmon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
interfaceTopNMIB=ModuleIdentity((1,3,6,1,2,1,16,27))
_InterfaceTopNObjects_ObjectIdentity=ObjectIdentity
interfaceTopNObjects=_InterfaceTopNObjects_ObjectIdentity((1,3,6,1,2,1,16,27,1))
class _InterfaceTopNCaps_Type(Bits):namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8),(_P,9),(_Q,10),(_R,11),(_S,12),(_T,13),(_U,14),(_V,15),(_W,16),(_X,17),(_Y,18),(_Z,19),(_a,20),(_b,21),(_c,22),(_d,23),(_e,24),(_f,25),(_g,26),(_h,27),(_i,28),(_j,29),(_k,30),(_l,31),(_m,32),(_n,33),(_o,34),(_p,35),(_q,36),(_r,37),(_s,38),(_t,39),(_u,40),(_v,41),(_w,42),(_x,43),(_y,44),(_z,45),(_A0,46),(_A1,47),(_A2,48),(_A3,49),(_A4,50),(_A5,51),(_A6,52),(_A7,53),(_A8,54),(_A9,55),(_AA,56),(_AB,57),(_AC,58),(_AD,59),(_AE,60),(_AF,61),(_AG,62),(_AH,63),(_AI,64),(_AJ,65),(_AK,66),(_AL,67),(_AM,68),(_AN,69),(_AO,70),(_AP,71),(_AQ,72),(_AR,73),(_AS,74),(_AT,75)))
_InterfaceTopNCaps_Type.__name__='Bits'
_InterfaceTopNCaps_Object=MibScalar
interfaceTopNCaps=_InterfaceTopNCaps_Object((1,3,6,1,2,1,16,27,1,1),_InterfaceTopNCaps_Type())
interfaceTopNCaps.setMaxAccess(_D)
if mibBuilder.loadTexts:interfaceTopNCaps.setStatus(_A)
_InterfaceTopNControlTable_Object=MibTable
interfaceTopNControlTable=_InterfaceTopNControlTable_Object((1,3,6,1,2,1,16,27,1,2))
if mibBuilder.loadTexts:interfaceTopNControlTable.setStatus(_A)
_InterfaceTopNControlEntry_Object=MibTableRow
interfaceTopNControlEntry=_InterfaceTopNControlEntry_Object((1,3,6,1,2,1,16,27,1,2,1))
interfaceTopNControlEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:interfaceTopNControlEntry.setStatus(_A)
class _InterfaceTopNControlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_InterfaceTopNControlIndex_Type.__name__=_C
_InterfaceTopNControlIndex_Object=MibTableColumn
interfaceTopNControlIndex=_InterfaceTopNControlIndex_Object((1,3,6,1,2,1,16,27,1,2,1,1),_InterfaceTopNControlIndex_Type())
interfaceTopNControlIndex.setMaxAccess(_AU)
if mibBuilder.loadTexts:interfaceTopNControlIndex.setStatus(_A)
class _InterfaceTopNObjectVariable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7),(_O,8),(_P,9),(_Q,10),(_R,11),(_S,12),(_T,13),(_U,14),(_V,15),(_W,16),(_X,17),(_Y,18),(_Z,19),(_a,20),(_b,21),(_c,22),(_d,23),(_e,24),(_f,25),(_g,26),(_h,27),(_i,28),(_j,29),(_k,30),(_l,31),(_m,32),(_n,33),(_o,34),(_p,35),(_q,36),(_r,37),(_s,38),(_t,39),(_u,40),(_v,41),(_w,42),(_x,43),(_y,44),(_z,45),(_A0,46),(_A1,47),(_A2,48),(_A3,49),(_A4,50),(_A5,51),(_A6,52),(_A7,53),(_A8,54),(_A9,55),(_AA,56),(_AB,57),(_AC,58),(_AD,59),(_AE,60),(_AF,61),(_AG,62),(_AH,63),(_AI,64),(_AJ,65),(_AK,66),(_AL,67),(_AM,68),(_AN,69),(_AO,70),(_AP,71),(_AQ,72),(_AR,73),(_AS,74),(_AT,75)))
_InterfaceTopNObjectVariable_Type.__name__=_C
_InterfaceTopNObjectVariable_Object=MibTableColumn
interfaceTopNObjectVariable=_InterfaceTopNObjectVariable_Object((1,3,6,1,2,1,16,27,1,2,1,2),_InterfaceTopNObjectVariable_Type())
interfaceTopNObjectVariable.setMaxAccess(_E)
if mibBuilder.loadTexts:interfaceTopNObjectVariable.setStatus(_A)
class _InterfaceTopNObjectSampleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('absoluteValue',1),('deltaValue',2),('bandwidthPercentage',3)))
_InterfaceTopNObjectSampleType_Type.__name__=_C
_InterfaceTopNObjectSampleType_Object=MibTableColumn
interfaceTopNObjectSampleType=_InterfaceTopNObjectSampleType_Object((1,3,6,1,2,1,16,27,1,2,1,3),_InterfaceTopNObjectSampleType_Type())
interfaceTopNObjectSampleType.setMaxAccess(_E)
if mibBuilder.loadTexts:interfaceTopNObjectSampleType.setStatus(_A)
_InterfaceTopNNormalizationReq_Type=TruthValue
_InterfaceTopNNormalizationReq_Object=MibTableColumn
interfaceTopNNormalizationReq=_InterfaceTopNNormalizationReq_Object((1,3,6,1,2,1,16,27,1,2,1,4),_InterfaceTopNNormalizationReq_Type())
interfaceTopNNormalizationReq.setMaxAccess(_E)
if mibBuilder.loadTexts:interfaceTopNNormalizationReq.setStatus(_A)
class _InterfaceTopNNormalizationFactor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_InterfaceTopNNormalizationFactor_Type.__name__=_C
_InterfaceTopNNormalizationFactor_Object=MibTableColumn
interfaceTopNNormalizationFactor=_InterfaceTopNNormalizationFactor_Object((1,3,6,1,2,1,16,27,1,2,1,5),_InterfaceTopNNormalizationFactor_Type())
interfaceTopNNormalizationFactor.setMaxAccess(_E)
if mibBuilder.loadTexts:interfaceTopNNormalizationFactor.setStatus(_A)
class _InterfaceTopNTimeRemaining_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_InterfaceTopNTimeRemaining_Type.__name__=_C
_InterfaceTopNTimeRemaining_Object=MibTableColumn
interfaceTopNTimeRemaining=_InterfaceTopNTimeRemaining_Object((1,3,6,1,2,1,16,27,1,2,1,6),_InterfaceTopNTimeRemaining_Type())
interfaceTopNTimeRemaining.setMaxAccess(_E)
if mibBuilder.loadTexts:interfaceTopNTimeRemaining.setStatus(_A)
class _InterfaceTopNDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_InterfaceTopNDuration_Type.__name__=_C
_InterfaceTopNDuration_Object=MibTableColumn
interfaceTopNDuration=_InterfaceTopNDuration_Object((1,3,6,1,2,1,16,27,1,2,1,7),_InterfaceTopNDuration_Type())
interfaceTopNDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:interfaceTopNDuration.setStatus(_A)
class _InterfaceTopNRequestedSize_Type(Integer32):defaultValue=10
_InterfaceTopNRequestedSize_Type.__name__=_C
_InterfaceTopNRequestedSize_Object=MibTableColumn
interfaceTopNRequestedSize=_InterfaceTopNRequestedSize_Object((1,3,6,1,2,1,16,27,1,2,1,8),_InterfaceTopNRequestedSize_Type())
interfaceTopNRequestedSize.setMaxAccess(_E)
if mibBuilder.loadTexts:interfaceTopNRequestedSize.setStatus(_A)
class _InterfaceTopNGrantedSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_InterfaceTopNGrantedSize_Type.__name__=_C
_InterfaceTopNGrantedSize_Object=MibTableColumn
interfaceTopNGrantedSize=_InterfaceTopNGrantedSize_Object((1,3,6,1,2,1,16,27,1,2,1,9),_InterfaceTopNGrantedSize_Type())
interfaceTopNGrantedSize.setMaxAccess(_D)
if mibBuilder.loadTexts:interfaceTopNGrantedSize.setStatus(_A)
_InterfaceTopNStartTime_Type=TimeStamp
_InterfaceTopNStartTime_Object=MibTableColumn
interfaceTopNStartTime=_InterfaceTopNStartTime_Object((1,3,6,1,2,1,16,27,1,2,1,10),_InterfaceTopNStartTime_Type())
interfaceTopNStartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:interfaceTopNStartTime.setStatus(_A)
_InterfaceTopNOwner_Type=OwnerString
_InterfaceTopNOwner_Object=MibTableColumn
interfaceTopNOwner=_InterfaceTopNOwner_Object((1,3,6,1,2,1,16,27,1,2,1,11),_InterfaceTopNOwner_Type())
interfaceTopNOwner.setMaxAccess(_E)
if mibBuilder.loadTexts:interfaceTopNOwner.setStatus(_A)
_InterfaceTopNLastCompletionTime_Type=TimeStamp
_InterfaceTopNLastCompletionTime_Object=MibTableColumn
interfaceTopNLastCompletionTime=_InterfaceTopNLastCompletionTime_Object((1,3,6,1,2,1,16,27,1,2,1,12),_InterfaceTopNLastCompletionTime_Type())
interfaceTopNLastCompletionTime.setMaxAccess(_D)
if mibBuilder.loadTexts:interfaceTopNLastCompletionTime.setStatus(_A)
_InterfaceTopNRowStatus_Type=RowStatus
_InterfaceTopNRowStatus_Object=MibTableColumn
interfaceTopNRowStatus=_InterfaceTopNRowStatus_Object((1,3,6,1,2,1,16,27,1,2,1,13),_InterfaceTopNRowStatus_Type())
interfaceTopNRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:interfaceTopNRowStatus.setStatus(_A)
_InterfaceTopNTable_Object=MibTable
interfaceTopNTable=_InterfaceTopNTable_Object((1,3,6,1,2,1,16,27,1,3))
if mibBuilder.loadTexts:interfaceTopNTable.setStatus(_A)
_InterfaceTopNEntry_Object=MibTableRow
interfaceTopNEntry=_InterfaceTopNEntry_Object((1,3,6,1,2,1,16,27,1,3,1))
interfaceTopNEntry.setIndexNames((0,_B,_F),(0,_B,_AV))
if mibBuilder.loadTexts:interfaceTopNEntry.setStatus(_A)
class _InterfaceTopNIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_InterfaceTopNIndex_Type.__name__=_C
_InterfaceTopNIndex_Object=MibTableColumn
interfaceTopNIndex=_InterfaceTopNIndex_Object((1,3,6,1,2,1,16,27,1,3,1,1),_InterfaceTopNIndex_Type())
interfaceTopNIndex.setMaxAccess(_AU)
if mibBuilder.loadTexts:interfaceTopNIndex.setStatus(_A)
class _InterfaceTopNDataSourceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_InterfaceTopNDataSourceIndex_Type.__name__=_C
_InterfaceTopNDataSourceIndex_Object=MibTableColumn
interfaceTopNDataSourceIndex=_InterfaceTopNDataSourceIndex_Object((1,3,6,1,2,1,16,27,1,3,1,2),_InterfaceTopNDataSourceIndex_Type())
interfaceTopNDataSourceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:interfaceTopNDataSourceIndex.setStatus(_A)
_InterfaceTopNValue_Type=Gauge32
_InterfaceTopNValue_Object=MibTableColumn
interfaceTopNValue=_InterfaceTopNValue_Object((1,3,6,1,2,1,16,27,1,3,1,3),_InterfaceTopNValue_Type())
interfaceTopNValue.setMaxAccess(_D)
if mibBuilder.loadTexts:interfaceTopNValue.setStatus(_A)
_InterfaceTopNValue64_Type=CounterBasedGauge64
_InterfaceTopNValue64_Object=MibTableColumn
interfaceTopNValue64=_InterfaceTopNValue64_Object((1,3,6,1,2,1,16,27,1,3,1,4),_InterfaceTopNValue64_Type())
interfaceTopNValue64.setMaxAccess(_D)
if mibBuilder.loadTexts:interfaceTopNValue64.setStatus(_A)
_InterfaceTopNNotifications_ObjectIdentity=ObjectIdentity
interfaceTopNNotifications=_InterfaceTopNNotifications_ObjectIdentity((1,3,6,1,2,1,16,27,2))
_InterfaceTopNConformance_ObjectIdentity=ObjectIdentity
interfaceTopNConformance=_InterfaceTopNConformance_ObjectIdentity((1,3,6,1,2,1,16,27,3))
_InterfaceTopNCompliances_ObjectIdentity=ObjectIdentity
interfaceTopNCompliances=_InterfaceTopNCompliances_ObjectIdentity((1,3,6,1,2,1,16,27,3,1))
_InterfaceTopNGroups_ObjectIdentity=ObjectIdentity
interfaceTopNGroups=_InterfaceTopNGroups_ObjectIdentity((1,3,6,1,2,1,16,27,3,2))
interfaceTopNGroup=ObjectGroup((1,3,6,1,2,1,16,27,3,2,1))
interfaceTopNGroup.setObjects(*((_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al)))
if mibBuilder.loadTexts:interfaceTopNGroup.setStatus(_A)
interfaceTopNCompliance=ModuleCompliance((1,3,6,1,2,1,16,27,3,1,1))
interfaceTopNCompliance.setObjects((_B,_Am))
if mibBuilder.loadTexts:interfaceTopNCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'interfaceTopNMIB':interfaceTopNMIB,'interfaceTopNObjects':interfaceTopNObjects,_AW:interfaceTopNCaps,'interfaceTopNControlTable':interfaceTopNControlTable,'interfaceTopNControlEntry':interfaceTopNControlEntry,_F:interfaceTopNControlIndex,_AX:interfaceTopNObjectVariable,_AY:interfaceTopNObjectSampleType,_AZ:interfaceTopNNormalizationReq,_Aa:interfaceTopNNormalizationFactor,_Ab:interfaceTopNTimeRemaining,_Ac:interfaceTopNDuration,_Ad:interfaceTopNRequestedSize,_Ae:interfaceTopNGrantedSize,_Af:interfaceTopNStartTime,_Ag:interfaceTopNOwner,_Ah:interfaceTopNLastCompletionTime,_Ai:interfaceTopNRowStatus,'interfaceTopNTable':interfaceTopNTable,'interfaceTopNEntry':interfaceTopNEntry,_AV:interfaceTopNIndex,_Aj:interfaceTopNDataSourceIndex,_Ak:interfaceTopNValue,_Al:interfaceTopNValue64,'interfaceTopNNotifications':interfaceTopNNotifications,'interfaceTopNConformance':interfaceTopNConformance,'interfaceTopNCompliances':interfaceTopNCompliances,'interfaceTopNCompliance':interfaceTopNCompliance,'interfaceTopNGroups':interfaceTopNGroups,_Am:interfaceTopNGroup})