_AH='ciscoIpslaVideoStatsGroup'
_AG='cipslaVideoAggOWSumSDHigh'
_AF='cipslaVideoAggUnSyncRTs'
_AE='cipslaVideoAggPktLateArrival'
_AD='cipslaVideoAggIAJIn'
_AC='cipslaVideoAggIAJOut'
_AB='cipslaVideoAggAvgJSD'
_AA='cipslaVideoAggNumOWSD'
_A9='cipslaVideoAggOWMaxSD'
_A8='cipslaVideoAggOWMinSD'
_A7='cipslaVideoAggOWSum2SDHigh'
_A6='cipslaVideoAggOWSum2SDLow'
_A5='cipslaVideoAggOWSumSD'
_A4='cipslaVideoAggBusies'
_A3='cipslaVideoAggErrors'
_A2='cipslaVideoAggPktSkipped'
_A1='cipslaVideoAggPktOutSeq'
_A0='cipslaVideoAggPktLossSD'
_z='cipslaVideoAggSum2NegSDHigh'
_y='cipslaVideoAggSum2NegSDLow'
_x='cipslaVideoAggSumNegSD'
_w='cipslaVideoAggNumNegSD'
_v='cipslaVideoAggMaxNegSD'
_u='cipslaVideoAggMinNegSD'
_t='cipslaVideoAggSum2PosSDHigh'
_s='cipslaVideoAggSum2PosSDLow'
_r='cipslaVideoAggSumPosSD'
_q='cipslaVideoAggNumPosSD'
_p='cipslaVideoAggMaxPosSD'
_o='cipslaVideoAggMinPosSD'
_n='cipslaVideoAggOverThresholds'
_m='cipslaVideoAggCompletions'
_l='cipslaLatestVideoPktLateArrival'
_k='cipslaLatestVideoOWAvgSD'
_j='cipslaLatestVideoIPDVAvgSDJ'
_i='cipslaLatestVideoNTPState'
_h='cipslaLatestVideoOWSum2SDHigh'
_g='cipslaLatestVideoOWSumSDHigh'
_f='cipslaLatestVideoUnSyncRTs'
_e='cipslaLatestVideoErrSenseDescr'
_d='cipslaLatestVideoIAJOut'
_c='cipslaLatestVideoAvgJitterSD'
_b='cipslaLatestVideoNumOWSD'
_a='cipslaLatestVideoOWMaxSD'
_Z='cipslaLatestVideoOWMinSD'
_Y='cipslaLatestVideoOWSum2SD'
_X='cipslaLatestVideoOWSumSD'
_W='cipslaLatestVideoSense'
_V='cipslaLatestVideoPktOutSeq'
_U='cipslaLatestVideoPktLossSD'
_T='cipslaLatestVideoSum2NegSD'
_S='cipslaLatestVideoSumNegSD'
_R='cipslaLatestVideoNumNegSD'
_Q='cipslaLatestVideoMaxNegSD'
_P='cipslaLatestVideoMinNegSD'
_O='cipslaLatestVideoSum2PosSD'
_N='cipslaLatestVideoSumPosSD'
_M='cipslaLatestVideoNumPosSD'
_L='cipslaLatestVideoMaxPosSD'
_K='cipslaLatestVideoMinPosSD'
_J='cipslaVideoAggStartTimeId'
_I='Integer32'
_H='rttMonCtrlAdminIndex'
_G='CISCO-RTTMON-MIB'
_F='occurrences'
_E='packets'
_D='milliseconds'
_C='read-only'
_B='CISCO-IPSLA-VIDEO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rttMonCtrlAdminIndex,=mibBuilder.importSymbols(_G,_H)
RttResponseSense,=mibBuilder.importSymbols('CISCO-RTTMON-TC-MIB','RttResponseSense')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
ciscoIpslaVideoMIB=ModuleIdentity((1,3,6,1,4,1,9,9,744))
if mibBuilder.loadTexts:ciscoIpslaVideoMIB.setRevisions(('2010-06-11 00:00',))
_CiscoIpslaVideoMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoIpslaVideoMIBNotifs=_CiscoIpslaVideoMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,744,0))
_CiscoIpslaVideoMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIpslaVideoMIBObjects=_CiscoIpslaVideoMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,744,1))
_CipslaVideoLatestOper_ObjectIdentity=ObjectIdentity
cipslaVideoLatestOper=_CipslaVideoLatestOper_ObjectIdentity((1,3,6,1,4,1,9,9,744,1,1))
_CipslaLatestVideoStatsTable_Object=MibTable
cipslaLatestVideoStatsTable=_CipslaLatestVideoStatsTable_Object((1,3,6,1,4,1,9,9,744,1,1,1))
if mibBuilder.loadTexts:cipslaLatestVideoStatsTable.setStatus(_A)
_CipslaLatestVideoStatsEntry_Object=MibTableRow
cipslaLatestVideoStatsEntry=_CipslaLatestVideoStatsEntry_Object((1,3,6,1,4,1,9,9,744,1,1,1,1))
cipslaLatestVideoStatsEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cipslaLatestVideoStatsEntry.setStatus(_A)
_CipslaLatestVideoMinPosSD_Type=Gauge32
_CipslaLatestVideoMinPosSD_Object=MibTableColumn
cipslaLatestVideoMinPosSD=_CipslaLatestVideoMinPosSD_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,1),_CipslaLatestVideoMinPosSD_Type())
cipslaLatestVideoMinPosSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoMinPosSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaLatestVideoMinPosSD.setUnits(_D)
_CipslaLatestVideoMaxPosSD_Type=Gauge32
_CipslaLatestVideoMaxPosSD_Object=MibTableColumn
cipslaLatestVideoMaxPosSD=_CipslaLatestVideoMaxPosSD_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,2),_CipslaLatestVideoMaxPosSD_Type())
cipslaLatestVideoMaxPosSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoMaxPosSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaLatestVideoMaxPosSD.setUnits(_D)
_CipslaLatestVideoNumPosSD_Type=Gauge32
_CipslaLatestVideoNumPosSD_Object=MibTableColumn
cipslaLatestVideoNumPosSD=_CipslaLatestVideoNumPosSD_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,3),_CipslaLatestVideoNumPosSD_Type())
cipslaLatestVideoNumPosSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoNumPosSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaLatestVideoNumPosSD.setUnits(_F)
_CipslaLatestVideoSumPosSD_Type=Gauge32
_CipslaLatestVideoSumPosSD_Object=MibTableColumn
cipslaLatestVideoSumPosSD=_CipslaLatestVideoSumPosSD_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,4),_CipslaLatestVideoSumPosSD_Type())
cipslaLatestVideoSumPosSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoSumPosSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaLatestVideoSumPosSD.setUnits(_D)
_CipslaLatestVideoSum2PosSD_Type=Gauge32
_CipslaLatestVideoSum2PosSD_Object=MibTableColumn
cipslaLatestVideoSum2PosSD=_CipslaLatestVideoSum2PosSD_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,5),_CipslaLatestVideoSum2PosSD_Type())
cipslaLatestVideoSum2PosSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoSum2PosSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaLatestVideoSum2PosSD.setUnits(_D)
_CipslaLatestVideoMinNegSD_Type=Gauge32
_CipslaLatestVideoMinNegSD_Object=MibTableColumn
cipslaLatestVideoMinNegSD=_CipslaLatestVideoMinNegSD_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,6),_CipslaLatestVideoMinNegSD_Type())
cipslaLatestVideoMinNegSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoMinNegSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaLatestVideoMinNegSD.setUnits(_D)
_CipslaLatestVideoMaxNegSD_Type=Gauge32
_CipslaLatestVideoMaxNegSD_Object=MibTableColumn
cipslaLatestVideoMaxNegSD=_CipslaLatestVideoMaxNegSD_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,7),_CipslaLatestVideoMaxNegSD_Type())
cipslaLatestVideoMaxNegSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoMaxNegSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaLatestVideoMaxNegSD.setUnits(_D)
_CipslaLatestVideoNumNegSD_Type=Gauge32
_CipslaLatestVideoNumNegSD_Object=MibTableColumn
cipslaLatestVideoNumNegSD=_CipslaLatestVideoNumNegSD_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,8),_CipslaLatestVideoNumNegSD_Type())
cipslaLatestVideoNumNegSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoNumNegSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaLatestVideoNumNegSD.setUnits(_F)
_CipslaLatestVideoSumNegSD_Type=Gauge32
_CipslaLatestVideoSumNegSD_Object=MibTableColumn
cipslaLatestVideoSumNegSD=_CipslaLatestVideoSumNegSD_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,9),_CipslaLatestVideoSumNegSD_Type())
cipslaLatestVideoSumNegSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoSumNegSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaLatestVideoSumNegSD.setUnits(_D)
_CipslaLatestVideoSum2NegSD_Type=Gauge32
_CipslaLatestVideoSum2NegSD_Object=MibTableColumn
cipslaLatestVideoSum2NegSD=_CipslaLatestVideoSum2NegSD_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,10),_CipslaLatestVideoSum2NegSD_Type())
cipslaLatestVideoSum2NegSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoSum2NegSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaLatestVideoSum2NegSD.setUnits(_D)
_CipslaLatestVideoPktLossSD_Type=Gauge32
_CipslaLatestVideoPktLossSD_Object=MibTableColumn
cipslaLatestVideoPktLossSD=_CipslaLatestVideoPktLossSD_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,11),_CipslaLatestVideoPktLossSD_Type())
cipslaLatestVideoPktLossSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoPktLossSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaLatestVideoPktLossSD.setUnits(_E)
_CipslaLatestVideoPktOutSeq_Type=Gauge32
_CipslaLatestVideoPktOutSeq_Object=MibTableColumn
cipslaLatestVideoPktOutSeq=_CipslaLatestVideoPktOutSeq_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,12),_CipslaLatestVideoPktOutSeq_Type())
cipslaLatestVideoPktOutSeq.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoPktOutSeq.setStatus(_A)
if mibBuilder.loadTexts:cipslaLatestVideoPktOutSeq.setUnits(_E)
_CipslaLatestVideoSense_Type=RttResponseSense
_CipslaLatestVideoSense_Object=MibTableColumn
cipslaLatestVideoSense=_CipslaLatestVideoSense_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,13),_CipslaLatestVideoSense_Type())
cipslaLatestVideoSense.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoSense.setStatus(_A)
_CipslaLatestVideoOWSumSD_Type=Gauge32
_CipslaLatestVideoOWSumSD_Object=MibTableColumn
cipslaLatestVideoOWSumSD=_CipslaLatestVideoOWSumSD_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,14),_CipslaLatestVideoOWSumSD_Type())
cipslaLatestVideoOWSumSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoOWSumSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaLatestVideoOWSumSD.setUnits(_D)
_CipslaLatestVideoOWSum2SD_Type=Gauge32
_CipslaLatestVideoOWSum2SD_Object=MibTableColumn
cipslaLatestVideoOWSum2SD=_CipslaLatestVideoOWSum2SD_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,15),_CipslaLatestVideoOWSum2SD_Type())
cipslaLatestVideoOWSum2SD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoOWSum2SD.setStatus(_A)
if mibBuilder.loadTexts:cipslaLatestVideoOWSum2SD.setUnits(_D)
_CipslaLatestVideoOWMinSD_Type=Gauge32
_CipslaLatestVideoOWMinSD_Object=MibTableColumn
cipslaLatestVideoOWMinSD=_CipslaLatestVideoOWMinSD_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,16),_CipslaLatestVideoOWMinSD_Type())
cipslaLatestVideoOWMinSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoOWMinSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaLatestVideoOWMinSD.setUnits(_D)
_CipslaLatestVideoOWMaxSD_Type=Gauge32
_CipslaLatestVideoOWMaxSD_Object=MibTableColumn
cipslaLatestVideoOWMaxSD=_CipslaLatestVideoOWMaxSD_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,17),_CipslaLatestVideoOWMaxSD_Type())
cipslaLatestVideoOWMaxSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoOWMaxSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaLatestVideoOWMaxSD.setUnits(_D)
_CipslaLatestVideoNumOWSD_Type=Gauge32
_CipslaLatestVideoNumOWSD_Object=MibTableColumn
cipslaLatestVideoNumOWSD=_CipslaLatestVideoNumOWSD_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,18),_CipslaLatestVideoNumOWSD_Type())
cipslaLatestVideoNumOWSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoNumOWSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaLatestVideoNumOWSD.setUnits(_E)
_CipslaLatestVideoAvgJitterSD_Type=Gauge32
_CipslaLatestVideoAvgJitterSD_Object=MibTableColumn
cipslaLatestVideoAvgJitterSD=_CipslaLatestVideoAvgJitterSD_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,19),_CipslaLatestVideoAvgJitterSD_Type())
cipslaLatestVideoAvgJitterSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoAvgJitterSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaLatestVideoAvgJitterSD.setUnits(_D)
_CipslaLatestVideoIAJOut_Type=Gauge32
_CipslaLatestVideoIAJOut_Object=MibTableColumn
cipslaLatestVideoIAJOut=_CipslaLatestVideoIAJOut_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,20),_CipslaLatestVideoIAJOut_Type())
cipslaLatestVideoIAJOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoIAJOut.setStatus(_A)
if mibBuilder.loadTexts:cipslaLatestVideoIAJOut.setUnits(_D)
_CipslaLatestVideoErrSenseDescr_Type=SnmpAdminString
_CipslaLatestVideoErrSenseDescr_Object=MibTableColumn
cipslaLatestVideoErrSenseDescr=_CipslaLatestVideoErrSenseDescr_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,21),_CipslaLatestVideoErrSenseDescr_Type())
cipslaLatestVideoErrSenseDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoErrSenseDescr.setStatus(_A)
_CipslaLatestVideoUnSyncRTs_Type=Counter32
_CipslaLatestVideoUnSyncRTs_Object=MibTableColumn
cipslaLatestVideoUnSyncRTs=_CipslaLatestVideoUnSyncRTs_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,22),_CipslaLatestVideoUnSyncRTs_Type())
cipslaLatestVideoUnSyncRTs.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoUnSyncRTs.setStatus(_A)
_CipslaLatestVideoOWSumSDHigh_Type=Gauge32
_CipslaLatestVideoOWSumSDHigh_Object=MibTableColumn
cipslaLatestVideoOWSumSDHigh=_CipslaLatestVideoOWSumSDHigh_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,23),_CipslaLatestVideoOWSumSDHigh_Type())
cipslaLatestVideoOWSumSDHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoOWSumSDHigh.setStatus(_A)
_CipslaLatestVideoOWSum2SDHigh_Type=Gauge32
_CipslaLatestVideoOWSum2SDHigh_Object=MibTableColumn
cipslaLatestVideoOWSum2SDHigh=_CipslaLatestVideoOWSum2SDHigh_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,24),_CipslaLatestVideoOWSum2SDHigh_Type())
cipslaLatestVideoOWSum2SDHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoOWSum2SDHigh.setStatus(_A)
class _CipslaLatestVideoNTPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sync',1),('outOfSync',2)))
_CipslaLatestVideoNTPState_Type.__name__=_I
_CipslaLatestVideoNTPState_Object=MibTableColumn
cipslaLatestVideoNTPState=_CipslaLatestVideoNTPState_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,25),_CipslaLatestVideoNTPState_Type())
cipslaLatestVideoNTPState.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoNTPState.setStatus(_A)
_CipslaLatestVideoIPDVAvgSDJ_Type=Gauge32
_CipslaLatestVideoIPDVAvgSDJ_Object=MibTableColumn
cipslaLatestVideoIPDVAvgSDJ=_CipslaLatestVideoIPDVAvgSDJ_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,26),_CipslaLatestVideoIPDVAvgSDJ_Type())
cipslaLatestVideoIPDVAvgSDJ.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoIPDVAvgSDJ.setStatus(_A)
if mibBuilder.loadTexts:cipslaLatestVideoIPDVAvgSDJ.setUnits(_D)
_CipslaLatestVideoOWAvgSD_Type=Gauge32
_CipslaLatestVideoOWAvgSD_Object=MibTableColumn
cipslaLatestVideoOWAvgSD=_CipslaLatestVideoOWAvgSD_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,27),_CipslaLatestVideoOWAvgSD_Type())
cipslaLatestVideoOWAvgSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoOWAvgSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaLatestVideoOWAvgSD.setUnits(_D)
_CipslaLatestVideoPktLateArrival_Type=Gauge32
_CipslaLatestVideoPktLateArrival_Object=MibTableColumn
cipslaLatestVideoPktLateArrival=_CipslaLatestVideoPktLateArrival_Object((1,3,6,1,4,1,9,9,744,1,1,1,1,28),_CipslaLatestVideoPktLateArrival_Type())
cipslaLatestVideoPktLateArrival.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaLatestVideoPktLateArrival.setStatus(_A)
if mibBuilder.loadTexts:cipslaLatestVideoPktLateArrival.setUnits(_E)
_CipslaVideoStats_ObjectIdentity=ObjectIdentity
cipslaVideoStats=_CipslaVideoStats_ObjectIdentity((1,3,6,1,4,1,9,9,744,1,2))
_CipslaVideoAggStatsTable_Object=MibTable
cipslaVideoAggStatsTable=_CipslaVideoAggStatsTable_Object((1,3,6,1,4,1,9,9,744,1,2,1))
if mibBuilder.loadTexts:cipslaVideoAggStatsTable.setStatus(_A)
_CipslaVideoAggStatsEntry_Object=MibTableRow
cipslaVideoAggStatsEntry=_CipslaVideoAggStatsEntry_Object((1,3,6,1,4,1,9,9,744,1,2,1,1))
cipslaVideoAggStatsEntry.setIndexNames((0,_G,_H),(0,_B,_J))
if mibBuilder.loadTexts:cipslaVideoAggStatsEntry.setStatus(_A)
_CipslaVideoAggStartTimeId_Type=TimeStamp
_CipslaVideoAggStartTimeId_Object=MibTableColumn
cipslaVideoAggStartTimeId=_CipslaVideoAggStartTimeId_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,1),_CipslaVideoAggStartTimeId_Type())
cipslaVideoAggStartTimeId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cipslaVideoAggStartTimeId.setStatus(_A)
_CipslaVideoAggCompletions_Type=Counter32
_CipslaVideoAggCompletions_Object=MibTableColumn
cipslaVideoAggCompletions=_CipslaVideoAggCompletions_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,2),_CipslaVideoAggCompletions_Type())
cipslaVideoAggCompletions.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggCompletions.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggCompletions.setUnits('completions')
_CipslaVideoAggOverThresholds_Type=Counter32
_CipslaVideoAggOverThresholds_Object=MibTableColumn
cipslaVideoAggOverThresholds=_CipslaVideoAggOverThresholds_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,3),_CipslaVideoAggOverThresholds_Type())
cipslaVideoAggOverThresholds.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggOverThresholds.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggOverThresholds.setUnits('operations')
_CipslaVideoAggMinPosSD_Type=Gauge32
_CipslaVideoAggMinPosSD_Object=MibTableColumn
cipslaVideoAggMinPosSD=_CipslaVideoAggMinPosSD_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,4),_CipslaVideoAggMinPosSD_Type())
cipslaVideoAggMinPosSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggMinPosSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggMinPosSD.setUnits(_D)
_CipslaVideoAggMaxPosSD_Type=Gauge32
_CipslaVideoAggMaxPosSD_Object=MibTableColumn
cipslaVideoAggMaxPosSD=_CipslaVideoAggMaxPosSD_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,5),_CipslaVideoAggMaxPosSD_Type())
cipslaVideoAggMaxPosSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggMaxPosSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggMaxPosSD.setUnits(_D)
_CipslaVideoAggNumPosSD_Type=Counter32
_CipslaVideoAggNumPosSD_Object=MibTableColumn
cipslaVideoAggNumPosSD=_CipslaVideoAggNumPosSD_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,6),_CipslaVideoAggNumPosSD_Type())
cipslaVideoAggNumPosSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggNumPosSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggNumPosSD.setUnits(_F)
_CipslaVideoAggSumPosSD_Type=Counter32
_CipslaVideoAggSumPosSD_Object=MibTableColumn
cipslaVideoAggSumPosSD=_CipslaVideoAggSumPosSD_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,7),_CipslaVideoAggSumPosSD_Type())
cipslaVideoAggSumPosSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggSumPosSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggSumPosSD.setUnits(_D)
_CipslaVideoAggSum2PosSDLow_Type=Counter32
_CipslaVideoAggSum2PosSDLow_Object=MibTableColumn
cipslaVideoAggSum2PosSDLow=_CipslaVideoAggSum2PosSDLow_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,8),_CipslaVideoAggSum2PosSDLow_Type())
cipslaVideoAggSum2PosSDLow.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggSum2PosSDLow.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggSum2PosSDLow.setUnits(_D)
_CipslaVideoAggSum2PosSDHigh_Type=Counter32
_CipslaVideoAggSum2PosSDHigh_Object=MibTableColumn
cipslaVideoAggSum2PosSDHigh=_CipslaVideoAggSum2PosSDHigh_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,9),_CipslaVideoAggSum2PosSDHigh_Type())
cipslaVideoAggSum2PosSDHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggSum2PosSDHigh.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggSum2PosSDHigh.setUnits(_D)
_CipslaVideoAggMinNegSD_Type=Gauge32
_CipslaVideoAggMinNegSD_Object=MibTableColumn
cipslaVideoAggMinNegSD=_CipslaVideoAggMinNegSD_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,10),_CipslaVideoAggMinNegSD_Type())
cipslaVideoAggMinNegSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggMinNegSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggMinNegSD.setUnits(_D)
_CipslaVideoAggMaxNegSD_Type=Gauge32
_CipslaVideoAggMaxNegSD_Object=MibTableColumn
cipslaVideoAggMaxNegSD=_CipslaVideoAggMaxNegSD_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,11),_CipslaVideoAggMaxNegSD_Type())
cipslaVideoAggMaxNegSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggMaxNegSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggMaxNegSD.setUnits(_D)
_CipslaVideoAggNumNegSD_Type=Counter32
_CipslaVideoAggNumNegSD_Object=MibTableColumn
cipslaVideoAggNumNegSD=_CipslaVideoAggNumNegSD_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,12),_CipslaVideoAggNumNegSD_Type())
cipslaVideoAggNumNegSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggNumNegSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggNumNegSD.setUnits(_F)
_CipslaVideoAggSumNegSD_Type=Counter32
_CipslaVideoAggSumNegSD_Object=MibTableColumn
cipslaVideoAggSumNegSD=_CipslaVideoAggSumNegSD_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,13),_CipslaVideoAggSumNegSD_Type())
cipslaVideoAggSumNegSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggSumNegSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggSumNegSD.setUnits(_D)
_CipslaVideoAggSum2NegSDLow_Type=Counter32
_CipslaVideoAggSum2NegSDLow_Object=MibTableColumn
cipslaVideoAggSum2NegSDLow=_CipslaVideoAggSum2NegSDLow_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,14),_CipslaVideoAggSum2NegSDLow_Type())
cipslaVideoAggSum2NegSDLow.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggSum2NegSDLow.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggSum2NegSDLow.setUnits(_D)
_CipslaVideoAggSum2NegSDHigh_Type=Counter32
_CipslaVideoAggSum2NegSDHigh_Object=MibTableColumn
cipslaVideoAggSum2NegSDHigh=_CipslaVideoAggSum2NegSDHigh_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,15),_CipslaVideoAggSum2NegSDHigh_Type())
cipslaVideoAggSum2NegSDHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggSum2NegSDHigh.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggSum2NegSDHigh.setUnits(_D)
_CipslaVideoAggPktLossSD_Type=Counter32
_CipslaVideoAggPktLossSD_Object=MibTableColumn
cipslaVideoAggPktLossSD=_CipslaVideoAggPktLossSD_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,16),_CipslaVideoAggPktLossSD_Type())
cipslaVideoAggPktLossSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggPktLossSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggPktLossSD.setUnits(_E)
_CipslaVideoAggPktOutSeq_Type=Counter32
_CipslaVideoAggPktOutSeq_Object=MibTableColumn
cipslaVideoAggPktOutSeq=_CipslaVideoAggPktOutSeq_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,17),_CipslaVideoAggPktOutSeq_Type())
cipslaVideoAggPktOutSeq.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggPktOutSeq.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggPktOutSeq.setUnits(_E)
_CipslaVideoAggPktSkipped_Type=Counter32
_CipslaVideoAggPktSkipped_Object=MibTableColumn
cipslaVideoAggPktSkipped=_CipslaVideoAggPktSkipped_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,18),_CipslaVideoAggPktSkipped_Type())
cipslaVideoAggPktSkipped.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggPktSkipped.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggPktSkipped.setUnits(_E)
_CipslaVideoAggErrors_Type=Counter32
_CipslaVideoAggErrors_Object=MibTableColumn
cipslaVideoAggErrors=_CipslaVideoAggErrors_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,19),_CipslaVideoAggErrors_Type())
cipslaVideoAggErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggErrors.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggErrors.setUnits('errors')
_CipslaVideoAggBusies_Type=Counter32
_CipslaVideoAggBusies_Object=MibTableColumn
cipslaVideoAggBusies=_CipslaVideoAggBusies_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,20),_CipslaVideoAggBusies_Type())
cipslaVideoAggBusies.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggBusies.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggBusies.setUnits('busies')
_CipslaVideoAggOWSumSD_Type=Counter32
_CipslaVideoAggOWSumSD_Object=MibTableColumn
cipslaVideoAggOWSumSD=_CipslaVideoAggOWSumSD_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,21),_CipslaVideoAggOWSumSD_Type())
cipslaVideoAggOWSumSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggOWSumSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggOWSumSD.setUnits(_D)
_CipslaVideoAggOWSum2SDLow_Type=Counter32
_CipslaVideoAggOWSum2SDLow_Object=MibTableColumn
cipslaVideoAggOWSum2SDLow=_CipslaVideoAggOWSum2SDLow_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,22),_CipslaVideoAggOWSum2SDLow_Type())
cipslaVideoAggOWSum2SDLow.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggOWSum2SDLow.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggOWSum2SDLow.setUnits(_D)
_CipslaVideoAggOWSum2SDHigh_Type=Counter32
_CipslaVideoAggOWSum2SDHigh_Object=MibTableColumn
cipslaVideoAggOWSum2SDHigh=_CipslaVideoAggOWSum2SDHigh_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,23),_CipslaVideoAggOWSum2SDHigh_Type())
cipslaVideoAggOWSum2SDHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggOWSum2SDHigh.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggOWSum2SDHigh.setUnits(_D)
_CipslaVideoAggOWMinSD_Type=Gauge32
_CipslaVideoAggOWMinSD_Object=MibTableColumn
cipslaVideoAggOWMinSD=_CipslaVideoAggOWMinSD_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,24),_CipslaVideoAggOWMinSD_Type())
cipslaVideoAggOWMinSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggOWMinSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggOWMinSD.setUnits(_D)
_CipslaVideoAggOWMaxSD_Type=Gauge32
_CipslaVideoAggOWMaxSD_Object=MibTableColumn
cipslaVideoAggOWMaxSD=_CipslaVideoAggOWMaxSD_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,25),_CipslaVideoAggOWMaxSD_Type())
cipslaVideoAggOWMaxSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggOWMaxSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggOWMaxSD.setUnits(_D)
_CipslaVideoAggNumOWSD_Type=Counter32
_CipslaVideoAggNumOWSD_Object=MibTableColumn
cipslaVideoAggNumOWSD=_CipslaVideoAggNumOWSD_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,26),_CipslaVideoAggNumOWSD_Type())
cipslaVideoAggNumOWSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggNumOWSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggNumOWSD.setUnits(_E)
_CipslaVideoAggAvgJSD_Type=Gauge32
_CipslaVideoAggAvgJSD_Object=MibTableColumn
cipslaVideoAggAvgJSD=_CipslaVideoAggAvgJSD_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,27),_CipslaVideoAggAvgJSD_Type())
cipslaVideoAggAvgJSD.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggAvgJSD.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggAvgJSD.setUnits(_D)
_CipslaVideoAggIAJOut_Type=Gauge32
_CipslaVideoAggIAJOut_Object=MibTableColumn
cipslaVideoAggIAJOut=_CipslaVideoAggIAJOut_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,28),_CipslaVideoAggIAJOut_Type())
cipslaVideoAggIAJOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggIAJOut.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggIAJOut.setUnits(_D)
_CipslaVideoAggIAJIn_Type=Gauge32
_CipslaVideoAggIAJIn_Object=MibTableColumn
cipslaVideoAggIAJIn=_CipslaVideoAggIAJIn_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,29),_CipslaVideoAggIAJIn_Type())
cipslaVideoAggIAJIn.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggIAJIn.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggIAJIn.setUnits(_D)
_CipslaVideoAggPktLateArrival_Type=Counter32
_CipslaVideoAggPktLateArrival_Object=MibTableColumn
cipslaVideoAggPktLateArrival=_CipslaVideoAggPktLateArrival_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,30),_CipslaVideoAggPktLateArrival_Type())
cipslaVideoAggPktLateArrival.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggPktLateArrival.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggPktLateArrival.setUnits(_E)
_CipslaVideoAggUnSyncRTs_Type=Counter32
_CipslaVideoAggUnSyncRTs_Object=MibTableColumn
cipslaVideoAggUnSyncRTs=_CipslaVideoAggUnSyncRTs_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,31),_CipslaVideoAggUnSyncRTs_Type())
cipslaVideoAggUnSyncRTs.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggUnSyncRTs.setStatus(_A)
_CipslaVideoAggOWSumSDHigh_Type=Counter32
_CipslaVideoAggOWSumSDHigh_Object=MibTableColumn
cipslaVideoAggOWSumSDHigh=_CipslaVideoAggOWSumSDHigh_Object((1,3,6,1,4,1,9,9,744,1,2,1,1,32),_CipslaVideoAggOWSumSDHigh_Type())
cipslaVideoAggOWSumSDHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaVideoAggOWSumSDHigh.setStatus(_A)
if mibBuilder.loadTexts:cipslaVideoAggOWSumSDHigh.setUnits(_E)
_CiscoIpslaVideoMIBConform_ObjectIdentity=ObjectIdentity
ciscoIpslaVideoMIBConform=_CiscoIpslaVideoMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,744,2))
_CiscoIpslaVideoMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoIpslaVideoMIBCompliances=_CiscoIpslaVideoMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,744,2,1))
_CiscoIpslaVideoMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIpslaVideoMIBGroups=_CiscoIpslaVideoMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,744,2,2))
ciscoIpslaVideoStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,744,2,2,1))
ciscoIpslaVideoStatsGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:ciscoIpslaVideoStatsGroup.setStatus(_A)
ciscoIpslaVideoMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,744,2,1,1))
ciscoIpslaVideoMIBCompliance.setObjects((_B,_AH))
if mibBuilder.loadTexts:ciscoIpslaVideoMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoIpslaVideoMIB':ciscoIpslaVideoMIB,'ciscoIpslaVideoMIBNotifs':ciscoIpslaVideoMIBNotifs,'ciscoIpslaVideoMIBObjects':ciscoIpslaVideoMIBObjects,'cipslaVideoLatestOper':cipslaVideoLatestOper,'cipslaLatestVideoStatsTable':cipslaLatestVideoStatsTable,'cipslaLatestVideoStatsEntry':cipslaLatestVideoStatsEntry,_K:cipslaLatestVideoMinPosSD,_L:cipslaLatestVideoMaxPosSD,_M:cipslaLatestVideoNumPosSD,_N:cipslaLatestVideoSumPosSD,_O:cipslaLatestVideoSum2PosSD,_P:cipslaLatestVideoMinNegSD,_Q:cipslaLatestVideoMaxNegSD,_R:cipslaLatestVideoNumNegSD,_S:cipslaLatestVideoSumNegSD,_T:cipslaLatestVideoSum2NegSD,_U:cipslaLatestVideoPktLossSD,_V:cipslaLatestVideoPktOutSeq,_W:cipslaLatestVideoSense,_X:cipslaLatestVideoOWSumSD,_Y:cipslaLatestVideoOWSum2SD,_Z:cipslaLatestVideoOWMinSD,_a:cipslaLatestVideoOWMaxSD,_b:cipslaLatestVideoNumOWSD,_c:cipslaLatestVideoAvgJitterSD,_d:cipslaLatestVideoIAJOut,_e:cipslaLatestVideoErrSenseDescr,_f:cipslaLatestVideoUnSyncRTs,_g:cipslaLatestVideoOWSumSDHigh,_h:cipslaLatestVideoOWSum2SDHigh,_i:cipslaLatestVideoNTPState,_j:cipslaLatestVideoIPDVAvgSDJ,_k:cipslaLatestVideoOWAvgSD,_l:cipslaLatestVideoPktLateArrival,'cipslaVideoStats':cipslaVideoStats,'cipslaVideoAggStatsTable':cipslaVideoAggStatsTable,'cipslaVideoAggStatsEntry':cipslaVideoAggStatsEntry,_J:cipslaVideoAggStartTimeId,_m:cipslaVideoAggCompletions,_n:cipslaVideoAggOverThresholds,_o:cipslaVideoAggMinPosSD,_p:cipslaVideoAggMaxPosSD,_q:cipslaVideoAggNumPosSD,_r:cipslaVideoAggSumPosSD,_s:cipslaVideoAggSum2PosSDLow,_t:cipslaVideoAggSum2PosSDHigh,_u:cipslaVideoAggMinNegSD,_v:cipslaVideoAggMaxNegSD,_w:cipslaVideoAggNumNegSD,_x:cipslaVideoAggSumNegSD,_y:cipslaVideoAggSum2NegSDLow,_z:cipslaVideoAggSum2NegSDHigh,_A0:cipslaVideoAggPktLossSD,_A1:cipslaVideoAggPktOutSeq,_A2:cipslaVideoAggPktSkipped,_A3:cipslaVideoAggErrors,_A4:cipslaVideoAggBusies,_A5:cipslaVideoAggOWSumSD,_A6:cipslaVideoAggOWSum2SDLow,_A7:cipslaVideoAggOWSum2SDHigh,_A8:cipslaVideoAggOWMinSD,_A9:cipslaVideoAggOWMaxSD,_AA:cipslaVideoAggNumOWSD,_AB:cipslaVideoAggAvgJSD,_AC:cipslaVideoAggIAJOut,_AD:cipslaVideoAggIAJIn,_AE:cipslaVideoAggPktLateArrival,_AF:cipslaVideoAggUnSyncRTs,_AG:cipslaVideoAggOWSumSDHigh,'ciscoIpslaVideoMIBConform':ciscoIpslaVideoMIBConform,'ciscoIpslaVideoMIBCompliances':ciscoIpslaVideoMIBCompliances,'ciscoIpslaVideoMIBCompliance':ciscoIpslaVideoMIBCompliance,'ciscoIpslaVideoMIBGroups':ciscoIpslaVideoMIBGroups,_AH:ciscoIpslaVideoStatsGroup})