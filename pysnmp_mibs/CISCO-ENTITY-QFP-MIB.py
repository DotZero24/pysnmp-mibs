_AN='ceqfpThroughputGroup'
_AM='ciscoEntityQfpMemoryHCResourceGroup'
_AL='ciscoEntityQfpMemoryResourceOvrflwGroup'
_AK='ceqfpThroughputNotif'
_AJ='ceqfpMemoryResFallingThreshNotif'
_AI='ceqfpMemoryResRisingThreshNotif'
_AH='ceqfpThroughputNotifEnabled'
_AG='ceqfpThroughputThreshold'
_AF='ceqfpThroughputInterval'
_AE='ceqfpMemoryHCResLowFreeWatermark'
_AD='ceqfpMemoryHCResFree'
_AC='ceqfpMemoryHCResInUse'
_AB='ceqfpMemoryHCResTotal'
_AA='ceqfpMemoryResLowFreeWatermarkOvrflw'
_A9='ceqfpMemoryResFreeOvrflw'
_A8='ceqfpMemoryResInUseOvrflw'
_A7='ceqfpMemoryResTotalOvrflw'
_A6='ceqfpMemoryResThreshNotifEnabled'
_A5='ceqfpMemoryResFallingThreshold'
_A4='ceqfpMemoryResRisingThreshold'
_A3='ceqfpMemoryResLowFreeWatermark'
_A2='ceqfpMemoryResFree'
_A1='ceqfpMemoryResTotal'
_A0='ceqfpUtilProcessingLoad'
_z='ceqfpUtilOutputTotalBitRate'
_y='ceqfpUtilOutputTotalPktRate'
_x='ceqfpUtilOutputNonPriorityBitRate'
_w='ceqfpUtilOutputNonPriorityPktRate'
_v='ceqfpUtilOutputPriorityBitRate'
_u='ceqfpUtilOutputPriorityPktRate'
_t='ceqfpUtilInputTotalBitRate'
_s='ceqfpUtilInputTotalPktRate'
_r='ceqfpUtilInputNonPriorityBitRate'
_q='ceqfpUtilInputNonPriorityPktRate'
_p='ceqfpUtilInputPriorityBitRate'
_o='ceqfpUtilInputPriorityPktRate'
_n='ceqfpSixtyMinutesUtilAlgo'
_m='ceqfpFiveMinutesUtilAlgo'
_l='ceqfpOneMinuteUtilAlgo'
_k='ceqfpFiveSecondUtilAlgo'
_j='ceqfpSystemLastLoadTime'
_i='ceqfpNumberSystemLoads'
_h='ceqfpSystemState'
_g='ceqfpSystemTrafficDirection'
_f='accessible-for-notify'
_e='ceqfpMemoryResType'
_d='not-accessible'
_c='ceqfpUtilTimeInterval'
_b='Gauge32'
_a='ciscoEntityQfpNotifGroup'
_Z='ciscoEntityQfpMemoryResNotifGroup'
_Y='ciscoEntityQfpMemoryResourceGroup'
_X='ciscoEntityQfpUtilizationAlgoGroup'
_W='ciscoEntityQfpUtilizationGroup'
_V='ciscoEntityQfpSystemGroup'
_U='ceqfpThroughputAvgRate'
_T='ceqfpThroughputLevel'
_S='ceqfpThroughputLicensedBW'
_R='ceqfpMemoryResCurrentFallingThresh'
_Q='ceqfpMemoryResCurrentRisingThresh'
_P='fiveSecSMA'
_O='TruthValue'
_N='ceqfpMemoryResInUse'
_M='Unsigned32'
_L='unknown'
_K='entPhysicalIndex'
_J='ENTITY-MIB'
_I='read-write'
_H='percent'
_G='packets per second'
_F='bits per second'
_E='Integer32'
_D='kilo bytes'
_C='read-only'
_B='current'
_A='CISCO-ENTITY-QFP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,=mibBuilder.importSymbols(_J,_K)
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_b,_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention',_O)
ciscoEntityQfpMIB=ModuleIdentity((1,3,6,1,4,1,9,9,715))
if mibBuilder.loadTexts:ciscoEntityQfpMIB.setRevisions(('2014-06-18 00:00','2012-06-06 00:00','2009-12-02 00:00'))
class CiscoQfpPacketRate(TextualConvention,Counter64):status=_B;displayHint='d'
class CiscoQfpBitRate(TextualConvention,Counter64):status=_B;displayHint='d'
class CiscoQfpTimeInterval(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('fiveSeconds',1),('oneMinute',2),('fiveMinutes',3),('sixtyMinutes',4)))
class CiscoQfpMemoryResource(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('dram',1))
_CiscoEntityQfpMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoEntityQfpMIBNotifs=_CiscoEntityQfpMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,715,0))
_CiscoEntityQfpMIBObjects_ObjectIdentity=ObjectIdentity
ciscoEntityQfpMIBObjects=_CiscoEntityQfpMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,715,1))
_CiscoEntityQfp_ObjectIdentity=ObjectIdentity
ciscoEntityQfp=_CiscoEntityQfp_ObjectIdentity((1,3,6,1,4,1,9,9,715,1,1))
_CeqfpSystemTable_Object=MibTable
ceqfpSystemTable=_CeqfpSystemTable_Object((1,3,6,1,4,1,9,9,715,1,1,1))
if mibBuilder.loadTexts:ceqfpSystemTable.setStatus(_B)
_CeqfpSystemEntry_Object=MibTableRow
ceqfpSystemEntry=_CeqfpSystemEntry_Object((1,3,6,1,4,1,9,9,715,1,1,1,1))
ceqfpSystemEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:ceqfpSystemEntry.setStatus(_B)
class _CeqfpSystemTrafficDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('ingress',2),('egress',3),('both',4)))
_CeqfpSystemTrafficDirection_Type.__name__=_E
_CeqfpSystemTrafficDirection_Object=MibTableColumn
ceqfpSystemTrafficDirection=_CeqfpSystemTrafficDirection_Object((1,3,6,1,4,1,9,9,715,1,1,1,1,1),_CeqfpSystemTrafficDirection_Type())
ceqfpSystemTrafficDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpSystemTrafficDirection.setStatus(_B)
class _CeqfpSystemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_L,1),('reset',2),('init',3),('active',4),('activeSolo',5),('standby',6),('hotStandby',7)))
_CeqfpSystemState_Type.__name__=_E
_CeqfpSystemState_Object=MibTableColumn
ceqfpSystemState=_CeqfpSystemState_Object((1,3,6,1,4,1,9,9,715,1,1,1,1,2),_CeqfpSystemState_Type())
ceqfpSystemState.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpSystemState.setStatus(_B)
_CeqfpNumberSystemLoads_Type=Counter32
_CeqfpNumberSystemLoads_Object=MibTableColumn
ceqfpNumberSystemLoads=_CeqfpNumberSystemLoads_Object((1,3,6,1,4,1,9,9,715,1,1,1,1,3),_CeqfpNumberSystemLoads_Type())
ceqfpNumberSystemLoads.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpNumberSystemLoads.setStatus(_B)
_CeqfpSystemLastLoadTime_Type=DateAndTime
_CeqfpSystemLastLoadTime_Object=MibTableColumn
ceqfpSystemLastLoadTime=_CeqfpSystemLastLoadTime_Object((1,3,6,1,4,1,9,9,715,1,1,1,1,4),_CeqfpSystemLastLoadTime_Type())
ceqfpSystemLastLoadTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpSystemLastLoadTime.setStatus(_B)
class _CeqfpFiveSecondUtilAlgo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('fiveSecSample',2)))
_CeqfpFiveSecondUtilAlgo_Type.__name__=_E
_CeqfpFiveSecondUtilAlgo_Object=MibScalar
ceqfpFiveSecondUtilAlgo=_CeqfpFiveSecondUtilAlgo_Object((1,3,6,1,4,1,9,9,715,1,1,2),_CeqfpFiveSecondUtilAlgo_Type())
ceqfpFiveSecondUtilAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpFiveSecondUtilAlgo.setStatus(_B)
class _CeqfpOneMinuteUtilAlgo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_P,2)))
_CeqfpOneMinuteUtilAlgo_Type.__name__=_E
_CeqfpOneMinuteUtilAlgo_Object=MibScalar
ceqfpOneMinuteUtilAlgo=_CeqfpOneMinuteUtilAlgo_Object((1,3,6,1,4,1,9,9,715,1,1,3),_CeqfpOneMinuteUtilAlgo_Type())
ceqfpOneMinuteUtilAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpOneMinuteUtilAlgo.setStatus(_B)
class _CeqfpFiveMinutesUtilAlgo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_P,2)))
_CeqfpFiveMinutesUtilAlgo_Type.__name__=_E
_CeqfpFiveMinutesUtilAlgo_Object=MibScalar
ceqfpFiveMinutesUtilAlgo=_CeqfpFiveMinutesUtilAlgo_Object((1,3,6,1,4,1,9,9,715,1,1,4),_CeqfpFiveMinutesUtilAlgo_Type())
ceqfpFiveMinutesUtilAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpFiveMinutesUtilAlgo.setStatus(_B)
class _CeqfpSixtyMinutesUtilAlgo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_P,2)))
_CeqfpSixtyMinutesUtilAlgo_Type.__name__=_E
_CeqfpSixtyMinutesUtilAlgo_Object=MibScalar
ceqfpSixtyMinutesUtilAlgo=_CeqfpSixtyMinutesUtilAlgo_Object((1,3,6,1,4,1,9,9,715,1,1,5),_CeqfpSixtyMinutesUtilAlgo_Type())
ceqfpSixtyMinutesUtilAlgo.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpSixtyMinutesUtilAlgo.setStatus(_B)
_CeqfpUtilizationTable_Object=MibTable
ceqfpUtilizationTable=_CeqfpUtilizationTable_Object((1,3,6,1,4,1,9,9,715,1,1,6))
if mibBuilder.loadTexts:ceqfpUtilizationTable.setStatus(_B)
_CeqfpUtilizationEntry_Object=MibTableRow
ceqfpUtilizationEntry=_CeqfpUtilizationEntry_Object((1,3,6,1,4,1,9,9,715,1,1,6,1))
ceqfpUtilizationEntry.setIndexNames((0,_J,_K),(0,_A,_c))
if mibBuilder.loadTexts:ceqfpUtilizationEntry.setStatus(_B)
_CeqfpUtilTimeInterval_Type=CiscoQfpTimeInterval
_CeqfpUtilTimeInterval_Object=MibTableColumn
ceqfpUtilTimeInterval=_CeqfpUtilTimeInterval_Object((1,3,6,1,4,1,9,9,715,1,1,6,1,1),_CeqfpUtilTimeInterval_Type())
ceqfpUtilTimeInterval.setMaxAccess(_d)
if mibBuilder.loadTexts:ceqfpUtilTimeInterval.setStatus(_B)
_CeqfpUtilInputPriorityPktRate_Type=CiscoQfpPacketRate
_CeqfpUtilInputPriorityPktRate_Object=MibTableColumn
ceqfpUtilInputPriorityPktRate=_CeqfpUtilInputPriorityPktRate_Object((1,3,6,1,4,1,9,9,715,1,1,6,1,2),_CeqfpUtilInputPriorityPktRate_Type())
ceqfpUtilInputPriorityPktRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpUtilInputPriorityPktRate.setStatus(_B)
if mibBuilder.loadTexts:ceqfpUtilInputPriorityPktRate.setUnits(_G)
_CeqfpUtilInputPriorityBitRate_Type=CiscoQfpBitRate
_CeqfpUtilInputPriorityBitRate_Object=MibTableColumn
ceqfpUtilInputPriorityBitRate=_CeqfpUtilInputPriorityBitRate_Object((1,3,6,1,4,1,9,9,715,1,1,6,1,3),_CeqfpUtilInputPriorityBitRate_Type())
ceqfpUtilInputPriorityBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpUtilInputPriorityBitRate.setStatus(_B)
if mibBuilder.loadTexts:ceqfpUtilInputPriorityBitRate.setUnits(_F)
_CeqfpUtilInputNonPriorityPktRate_Type=CiscoQfpPacketRate
_CeqfpUtilInputNonPriorityPktRate_Object=MibTableColumn
ceqfpUtilInputNonPriorityPktRate=_CeqfpUtilInputNonPriorityPktRate_Object((1,3,6,1,4,1,9,9,715,1,1,6,1,4),_CeqfpUtilInputNonPriorityPktRate_Type())
ceqfpUtilInputNonPriorityPktRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpUtilInputNonPriorityPktRate.setStatus(_B)
if mibBuilder.loadTexts:ceqfpUtilInputNonPriorityPktRate.setUnits(_G)
_CeqfpUtilInputNonPriorityBitRate_Type=CiscoQfpBitRate
_CeqfpUtilInputNonPriorityBitRate_Object=MibTableColumn
ceqfpUtilInputNonPriorityBitRate=_CeqfpUtilInputNonPriorityBitRate_Object((1,3,6,1,4,1,9,9,715,1,1,6,1,5),_CeqfpUtilInputNonPriorityBitRate_Type())
ceqfpUtilInputNonPriorityBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpUtilInputNonPriorityBitRate.setStatus(_B)
if mibBuilder.loadTexts:ceqfpUtilInputNonPriorityBitRate.setUnits(_F)
_CeqfpUtilInputTotalPktRate_Type=CiscoQfpPacketRate
_CeqfpUtilInputTotalPktRate_Object=MibTableColumn
ceqfpUtilInputTotalPktRate=_CeqfpUtilInputTotalPktRate_Object((1,3,6,1,4,1,9,9,715,1,1,6,1,6),_CeqfpUtilInputTotalPktRate_Type())
ceqfpUtilInputTotalPktRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpUtilInputTotalPktRate.setStatus(_B)
if mibBuilder.loadTexts:ceqfpUtilInputTotalPktRate.setUnits(_G)
_CeqfpUtilInputTotalBitRate_Type=CiscoQfpBitRate
_CeqfpUtilInputTotalBitRate_Object=MibTableColumn
ceqfpUtilInputTotalBitRate=_CeqfpUtilInputTotalBitRate_Object((1,3,6,1,4,1,9,9,715,1,1,6,1,7),_CeqfpUtilInputTotalBitRate_Type())
ceqfpUtilInputTotalBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpUtilInputTotalBitRate.setStatus(_B)
if mibBuilder.loadTexts:ceqfpUtilInputTotalBitRate.setUnits(_F)
_CeqfpUtilOutputPriorityPktRate_Type=CiscoQfpPacketRate
_CeqfpUtilOutputPriorityPktRate_Object=MibTableColumn
ceqfpUtilOutputPriorityPktRate=_CeqfpUtilOutputPriorityPktRate_Object((1,3,6,1,4,1,9,9,715,1,1,6,1,8),_CeqfpUtilOutputPriorityPktRate_Type())
ceqfpUtilOutputPriorityPktRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpUtilOutputPriorityPktRate.setStatus(_B)
if mibBuilder.loadTexts:ceqfpUtilOutputPriorityPktRate.setUnits(_G)
_CeqfpUtilOutputPriorityBitRate_Type=CiscoQfpBitRate
_CeqfpUtilOutputPriorityBitRate_Object=MibTableColumn
ceqfpUtilOutputPriorityBitRate=_CeqfpUtilOutputPriorityBitRate_Object((1,3,6,1,4,1,9,9,715,1,1,6,1,9),_CeqfpUtilOutputPriorityBitRate_Type())
ceqfpUtilOutputPriorityBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpUtilOutputPriorityBitRate.setStatus(_B)
if mibBuilder.loadTexts:ceqfpUtilOutputPriorityBitRate.setUnits(_F)
_CeqfpUtilOutputNonPriorityPktRate_Type=CiscoQfpPacketRate
_CeqfpUtilOutputNonPriorityPktRate_Object=MibTableColumn
ceqfpUtilOutputNonPriorityPktRate=_CeqfpUtilOutputNonPriorityPktRate_Object((1,3,6,1,4,1,9,9,715,1,1,6,1,10),_CeqfpUtilOutputNonPriorityPktRate_Type())
ceqfpUtilOutputNonPriorityPktRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpUtilOutputNonPriorityPktRate.setStatus(_B)
if mibBuilder.loadTexts:ceqfpUtilOutputNonPriorityPktRate.setUnits(_G)
_CeqfpUtilOutputNonPriorityBitRate_Type=CiscoQfpBitRate
_CeqfpUtilOutputNonPriorityBitRate_Object=MibTableColumn
ceqfpUtilOutputNonPriorityBitRate=_CeqfpUtilOutputNonPriorityBitRate_Object((1,3,6,1,4,1,9,9,715,1,1,6,1,11),_CeqfpUtilOutputNonPriorityBitRate_Type())
ceqfpUtilOutputNonPriorityBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpUtilOutputNonPriorityBitRate.setStatus(_B)
if mibBuilder.loadTexts:ceqfpUtilOutputNonPriorityBitRate.setUnits(_F)
_CeqfpUtilOutputTotalPktRate_Type=CiscoQfpPacketRate
_CeqfpUtilOutputTotalPktRate_Object=MibTableColumn
ceqfpUtilOutputTotalPktRate=_CeqfpUtilOutputTotalPktRate_Object((1,3,6,1,4,1,9,9,715,1,1,6,1,12),_CeqfpUtilOutputTotalPktRate_Type())
ceqfpUtilOutputTotalPktRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpUtilOutputTotalPktRate.setStatus(_B)
if mibBuilder.loadTexts:ceqfpUtilOutputTotalPktRate.setUnits(_G)
_CeqfpUtilOutputTotalBitRate_Type=CiscoQfpBitRate
_CeqfpUtilOutputTotalBitRate_Object=MibTableColumn
ceqfpUtilOutputTotalBitRate=_CeqfpUtilOutputTotalBitRate_Object((1,3,6,1,4,1,9,9,715,1,1,6,1,13),_CeqfpUtilOutputTotalBitRate_Type())
ceqfpUtilOutputTotalBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpUtilOutputTotalBitRate.setStatus(_B)
if mibBuilder.loadTexts:ceqfpUtilOutputTotalBitRate.setUnits(_F)
class _CeqfpUtilProcessingLoad_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CeqfpUtilProcessingLoad_Type.__name__=_b
_CeqfpUtilProcessingLoad_Object=MibTableColumn
ceqfpUtilProcessingLoad=_CeqfpUtilProcessingLoad_Object((1,3,6,1,4,1,9,9,715,1,1,6,1,14),_CeqfpUtilProcessingLoad_Type())
ceqfpUtilProcessingLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpUtilProcessingLoad.setStatus(_B)
if mibBuilder.loadTexts:ceqfpUtilProcessingLoad.setUnits(_H)
_CeqfpMemoryResourceTable_Object=MibTable
ceqfpMemoryResourceTable=_CeqfpMemoryResourceTable_Object((1,3,6,1,4,1,9,9,715,1,1,7))
if mibBuilder.loadTexts:ceqfpMemoryResourceTable.setStatus(_B)
_CeqfpMemoryResourceEntry_Object=MibTableRow
ceqfpMemoryResourceEntry=_CeqfpMemoryResourceEntry_Object((1,3,6,1,4,1,9,9,715,1,1,7,1))
ceqfpMemoryResourceEntry.setIndexNames((0,_J,_K),(0,_A,_e))
if mibBuilder.loadTexts:ceqfpMemoryResourceEntry.setStatus(_B)
_CeqfpMemoryResType_Type=CiscoQfpMemoryResource
_CeqfpMemoryResType_Object=MibTableColumn
ceqfpMemoryResType=_CeqfpMemoryResType_Object((1,3,6,1,4,1,9,9,715,1,1,7,1,1),_CeqfpMemoryResType_Type())
ceqfpMemoryResType.setMaxAccess(_d)
if mibBuilder.loadTexts:ceqfpMemoryResType.setStatus(_B)
_CeqfpMemoryResTotal_Type=Gauge32
_CeqfpMemoryResTotal_Object=MibTableColumn
ceqfpMemoryResTotal=_CeqfpMemoryResTotal_Object((1,3,6,1,4,1,9,9,715,1,1,7,1,2),_CeqfpMemoryResTotal_Type())
ceqfpMemoryResTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpMemoryResTotal.setStatus(_B)
if mibBuilder.loadTexts:ceqfpMemoryResTotal.setUnits(_D)
_CeqfpMemoryResInUse_Type=Gauge32
_CeqfpMemoryResInUse_Object=MibTableColumn
ceqfpMemoryResInUse=_CeqfpMemoryResInUse_Object((1,3,6,1,4,1,9,9,715,1,1,7,1,3),_CeqfpMemoryResInUse_Type())
ceqfpMemoryResInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpMemoryResInUse.setStatus(_B)
if mibBuilder.loadTexts:ceqfpMemoryResInUse.setUnits(_D)
_CeqfpMemoryResFree_Type=Gauge32
_CeqfpMemoryResFree_Object=MibTableColumn
ceqfpMemoryResFree=_CeqfpMemoryResFree_Object((1,3,6,1,4,1,9,9,715,1,1,7,1,4),_CeqfpMemoryResFree_Type())
ceqfpMemoryResFree.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpMemoryResFree.setStatus(_B)
if mibBuilder.loadTexts:ceqfpMemoryResFree.setUnits(_D)
_CeqfpMemoryResLowFreeWatermark_Type=Gauge32
_CeqfpMemoryResLowFreeWatermark_Object=MibTableColumn
ceqfpMemoryResLowFreeWatermark=_CeqfpMemoryResLowFreeWatermark_Object((1,3,6,1,4,1,9,9,715,1,1,7,1,5),_CeqfpMemoryResLowFreeWatermark_Type())
ceqfpMemoryResLowFreeWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpMemoryResLowFreeWatermark.setStatus(_B)
if mibBuilder.loadTexts:ceqfpMemoryResLowFreeWatermark.setUnits(_D)
class _CeqfpMemoryResRisingThreshold_Type(Unsigned32):defaultValue=90;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CeqfpMemoryResRisingThreshold_Type.__name__=_M
_CeqfpMemoryResRisingThreshold_Object=MibTableColumn
ceqfpMemoryResRisingThreshold=_CeqfpMemoryResRisingThreshold_Object((1,3,6,1,4,1,9,9,715,1,1,7,1,6),_CeqfpMemoryResRisingThreshold_Type())
ceqfpMemoryResRisingThreshold.setMaxAccess(_I)
if mibBuilder.loadTexts:ceqfpMemoryResRisingThreshold.setStatus(_B)
if mibBuilder.loadTexts:ceqfpMemoryResRisingThreshold.setUnits(_H)
class _CeqfpMemoryResFallingThreshold_Type(Unsigned32):defaultValue=85;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CeqfpMemoryResFallingThreshold_Type.__name__=_M
_CeqfpMemoryResFallingThreshold_Object=MibTableColumn
ceqfpMemoryResFallingThreshold=_CeqfpMemoryResFallingThreshold_Object((1,3,6,1,4,1,9,9,715,1,1,7,1,7),_CeqfpMemoryResFallingThreshold_Type())
ceqfpMemoryResFallingThreshold.setMaxAccess(_I)
if mibBuilder.loadTexts:ceqfpMemoryResFallingThreshold.setStatus(_B)
if mibBuilder.loadTexts:ceqfpMemoryResFallingThreshold.setUnits(_H)
_CeqfpMemoryResTotalOvrflw_Type=Gauge32
_CeqfpMemoryResTotalOvrflw_Object=MibTableColumn
ceqfpMemoryResTotalOvrflw=_CeqfpMemoryResTotalOvrflw_Object((1,3,6,1,4,1,9,9,715,1,1,7,1,8),_CeqfpMemoryResTotalOvrflw_Type())
ceqfpMemoryResTotalOvrflw.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpMemoryResTotalOvrflw.setStatus(_B)
if mibBuilder.loadTexts:ceqfpMemoryResTotalOvrflw.setUnits(_D)
_CeqfpMemoryHCResTotal_Type=CounterBasedGauge64
_CeqfpMemoryHCResTotal_Object=MibTableColumn
ceqfpMemoryHCResTotal=_CeqfpMemoryHCResTotal_Object((1,3,6,1,4,1,9,9,715,1,1,7,1,9),_CeqfpMemoryHCResTotal_Type())
ceqfpMemoryHCResTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpMemoryHCResTotal.setStatus(_B)
if mibBuilder.loadTexts:ceqfpMemoryHCResTotal.setUnits(_D)
_CeqfpMemoryResInUseOvrflw_Type=Gauge32
_CeqfpMemoryResInUseOvrflw_Object=MibTableColumn
ceqfpMemoryResInUseOvrflw=_CeqfpMemoryResInUseOvrflw_Object((1,3,6,1,4,1,9,9,715,1,1,7,1,10),_CeqfpMemoryResInUseOvrflw_Type())
ceqfpMemoryResInUseOvrflw.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpMemoryResInUseOvrflw.setStatus(_B)
if mibBuilder.loadTexts:ceqfpMemoryResInUseOvrflw.setUnits(_D)
_CeqfpMemoryHCResInUse_Type=CounterBasedGauge64
_CeqfpMemoryHCResInUse_Object=MibTableColumn
ceqfpMemoryHCResInUse=_CeqfpMemoryHCResInUse_Object((1,3,6,1,4,1,9,9,715,1,1,7,1,11),_CeqfpMemoryHCResInUse_Type())
ceqfpMemoryHCResInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpMemoryHCResInUse.setStatus(_B)
if mibBuilder.loadTexts:ceqfpMemoryHCResInUse.setUnits(_D)
_CeqfpMemoryResFreeOvrflw_Type=Gauge32
_CeqfpMemoryResFreeOvrflw_Object=MibTableColumn
ceqfpMemoryResFreeOvrflw=_CeqfpMemoryResFreeOvrflw_Object((1,3,6,1,4,1,9,9,715,1,1,7,1,12),_CeqfpMemoryResFreeOvrflw_Type())
ceqfpMemoryResFreeOvrflw.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpMemoryResFreeOvrflw.setStatus(_B)
if mibBuilder.loadTexts:ceqfpMemoryResFreeOvrflw.setUnits(_D)
_CeqfpMemoryHCResFree_Type=CounterBasedGauge64
_CeqfpMemoryHCResFree_Object=MibTableColumn
ceqfpMemoryHCResFree=_CeqfpMemoryHCResFree_Object((1,3,6,1,4,1,9,9,715,1,1,7,1,13),_CeqfpMemoryHCResFree_Type())
ceqfpMemoryHCResFree.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpMemoryHCResFree.setStatus(_B)
if mibBuilder.loadTexts:ceqfpMemoryHCResFree.setUnits(_D)
_CeqfpMemoryResLowFreeWatermarkOvrflw_Type=Gauge32
_CeqfpMemoryResLowFreeWatermarkOvrflw_Object=MibTableColumn
ceqfpMemoryResLowFreeWatermarkOvrflw=_CeqfpMemoryResLowFreeWatermarkOvrflw_Object((1,3,6,1,4,1,9,9,715,1,1,7,1,14),_CeqfpMemoryResLowFreeWatermarkOvrflw_Type())
ceqfpMemoryResLowFreeWatermarkOvrflw.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpMemoryResLowFreeWatermarkOvrflw.setStatus(_B)
if mibBuilder.loadTexts:ceqfpMemoryResLowFreeWatermarkOvrflw.setUnits(_D)
_CeqfpMemoryHCResLowFreeWatermark_Type=CounterBasedGauge64
_CeqfpMemoryHCResLowFreeWatermark_Object=MibTableColumn
ceqfpMemoryHCResLowFreeWatermark=_CeqfpMemoryHCResLowFreeWatermark_Object((1,3,6,1,4,1,9,9,715,1,1,7,1,15),_CeqfpMemoryHCResLowFreeWatermark_Type())
ceqfpMemoryHCResLowFreeWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpMemoryHCResLowFreeWatermark.setStatus(_B)
if mibBuilder.loadTexts:ceqfpMemoryHCResLowFreeWatermark.setUnits(_D)
_CeqfpThroughputTable_Object=MibTable
ceqfpThroughputTable=_CeqfpThroughputTable_Object((1,3,6,1,4,1,9,9,715,1,1,8))
if mibBuilder.loadTexts:ceqfpThroughputTable.setStatus(_B)
_CeqfpThroughputEntry_Object=MibTableRow
ceqfpThroughputEntry=_CeqfpThroughputEntry_Object((1,3,6,1,4,1,9,9,715,1,1,8,1))
ceqfpThroughputEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:ceqfpThroughputEntry.setStatus(_B)
_CeqfpThroughputLicensedBW_Type=Counter64
_CeqfpThroughputLicensedBW_Object=MibTableColumn
ceqfpThroughputLicensedBW=_CeqfpThroughputLicensedBW_Object((1,3,6,1,4,1,9,9,715,1,1,8,1,1),_CeqfpThroughputLicensedBW_Type())
ceqfpThroughputLicensedBW.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpThroughputLicensedBW.setStatus(_B)
if mibBuilder.loadTexts:ceqfpThroughputLicensedBW.setUnits(_F)
class _CeqfpThroughputLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('warning',2),('exceed',3)))
_CeqfpThroughputLevel_Type.__name__=_E
_CeqfpThroughputLevel_Object=MibTableColumn
ceqfpThroughputLevel=_CeqfpThroughputLevel_Object((1,3,6,1,4,1,9,9,715,1,1,8,1,2),_CeqfpThroughputLevel_Type())
ceqfpThroughputLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpThroughputLevel.setStatus(_B)
class _CeqfpThroughputInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,86400))
_CeqfpThroughputInterval_Type.__name__=_E
_CeqfpThroughputInterval_Object=MibTableColumn
ceqfpThroughputInterval=_CeqfpThroughputInterval_Object((1,3,6,1,4,1,9,9,715,1,1,8,1,3),_CeqfpThroughputInterval_Type())
ceqfpThroughputInterval.setMaxAccess(_I)
if mibBuilder.loadTexts:ceqfpThroughputInterval.setStatus(_B)
if mibBuilder.loadTexts:ceqfpThroughputInterval.setUnits('seconds')
class _CeqfpThroughputThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(75,95))
_CeqfpThroughputThreshold_Type.__name__=_E
_CeqfpThroughputThreshold_Object=MibTableColumn
ceqfpThroughputThreshold=_CeqfpThroughputThreshold_Object((1,3,6,1,4,1,9,9,715,1,1,8,1,4),_CeqfpThroughputThreshold_Type())
ceqfpThroughputThreshold.setMaxAccess(_I)
if mibBuilder.loadTexts:ceqfpThroughputThreshold.setStatus(_B)
if mibBuilder.loadTexts:ceqfpThroughputThreshold.setUnits(_H)
_CeqfpThroughputAvgRate_Type=Counter64
_CeqfpThroughputAvgRate_Object=MibTableColumn
ceqfpThroughputAvgRate=_CeqfpThroughputAvgRate_Object((1,3,6,1,4,1,9,9,715,1,1,8,1,5),_CeqfpThroughputAvgRate_Type())
ceqfpThroughputAvgRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ceqfpThroughputAvgRate.setStatus(_B)
if mibBuilder.loadTexts:ceqfpThroughputAvgRate.setUnits(_F)
_CiscoEntityQfpNotif_ObjectIdentity=ObjectIdentity
ciscoEntityQfpNotif=_CiscoEntityQfpNotif_ObjectIdentity((1,3,6,1,4,1,9,9,715,1,2))
class _CeqfpMemoryResThreshNotifEnabled_Type(TruthValue):defaultValue=2
_CeqfpMemoryResThreshNotifEnabled_Type.__name__=_O
_CeqfpMemoryResThreshNotifEnabled_Object=MibScalar
ceqfpMemoryResThreshNotifEnabled=_CeqfpMemoryResThreshNotifEnabled_Object((1,3,6,1,4,1,9,9,715,1,2,1),_CeqfpMemoryResThreshNotifEnabled_Type())
ceqfpMemoryResThreshNotifEnabled.setMaxAccess(_I)
if mibBuilder.loadTexts:ceqfpMemoryResThreshNotifEnabled.setStatus(_B)
class _CeqfpMemoryResCurrentRisingThresh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CeqfpMemoryResCurrentRisingThresh_Type.__name__=_M
_CeqfpMemoryResCurrentRisingThresh_Object=MibScalar
ceqfpMemoryResCurrentRisingThresh=_CeqfpMemoryResCurrentRisingThresh_Object((1,3,6,1,4,1,9,9,715,1,2,2),_CeqfpMemoryResCurrentRisingThresh_Type())
ceqfpMemoryResCurrentRisingThresh.setMaxAccess(_f)
if mibBuilder.loadTexts:ceqfpMemoryResCurrentRisingThresh.setStatus(_B)
if mibBuilder.loadTexts:ceqfpMemoryResCurrentRisingThresh.setUnits(_H)
_CeqfpMemoryResCurrentFallingThresh_Type=Unsigned32
_CeqfpMemoryResCurrentFallingThresh_Object=MibScalar
ceqfpMemoryResCurrentFallingThresh=_CeqfpMemoryResCurrentFallingThresh_Object((1,3,6,1,4,1,9,9,715,1,2,3),_CeqfpMemoryResCurrentFallingThresh_Type())
ceqfpMemoryResCurrentFallingThresh.setMaxAccess(_f)
if mibBuilder.loadTexts:ceqfpMemoryResCurrentFallingThresh.setStatus(_B)
if mibBuilder.loadTexts:ceqfpMemoryResCurrentFallingThresh.setUnits(_H)
class _CeqfpThroughputNotifEnabled_Type(TruthValue):defaultValue=2
_CeqfpThroughputNotifEnabled_Type.__name__=_O
_CeqfpThroughputNotifEnabled_Object=MibScalar
ceqfpThroughputNotifEnabled=_CeqfpThroughputNotifEnabled_Object((1,3,6,1,4,1,9,9,715,1,2,4),_CeqfpThroughputNotifEnabled_Type())
ceqfpThroughputNotifEnabled.setMaxAccess(_I)
if mibBuilder.loadTexts:ceqfpThroughputNotifEnabled.setStatus(_B)
_CiscoEntityQfpMIBConform_ObjectIdentity=ObjectIdentity
ciscoEntityQfpMIBConform=_CiscoEntityQfpMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,715,2))
_CiscoEntityQfpMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoEntityQfpMIBCompliances=_CiscoEntityQfpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,715,2,1))
_CiscoEntityQfpMIBGroups_ObjectIdentity=ObjectIdentity
ciscoEntityQfpMIBGroups=_CiscoEntityQfpMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,715,2,2))
ciscoEntityQfpSystemGroup=ObjectGroup((1,3,6,1,4,1,9,9,715,2,2,1))
ciscoEntityQfpSystemGroup.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:ciscoEntityQfpSystemGroup.setStatus(_B)
ciscoEntityQfpUtilizationAlgoGroup=ObjectGroup((1,3,6,1,4,1,9,9,715,2,2,2))
ciscoEntityQfpUtilizationAlgoGroup.setObjects(*((_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:ciscoEntityQfpUtilizationAlgoGroup.setStatus(_B)
ciscoEntityQfpUtilizationGroup=ObjectGroup((1,3,6,1,4,1,9,9,715,2,2,3))
ciscoEntityQfpUtilizationGroup.setObjects(*((_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:ciscoEntityQfpUtilizationGroup.setStatus(_B)
ciscoEntityQfpMemoryResourceGroup=ObjectGroup((1,3,6,1,4,1,9,9,715,2,2,4))
ciscoEntityQfpMemoryResourceGroup.setObjects(*((_A,_A1),(_A,_N),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:ciscoEntityQfpMemoryResourceGroup.setStatus(_B)
ciscoEntityQfpMemoryResNotifGroup=ObjectGroup((1,3,6,1,4,1,9,9,715,2,2,6))
ciscoEntityQfpMemoryResNotifGroup.setObjects(*((_A,_A6),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:ciscoEntityQfpMemoryResNotifGroup.setStatus(_B)
ciscoEntityQfpMemoryResourceOvrflwGroup=ObjectGroup((1,3,6,1,4,1,9,9,715,2,2,7))
ciscoEntityQfpMemoryResourceOvrflwGroup.setObjects(*((_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:ciscoEntityQfpMemoryResourceOvrflwGroup.setStatus(_B)
ciscoEntityQfpMemoryHCResourceGroup=ObjectGroup((1,3,6,1,4,1,9,9,715,2,2,8))
ciscoEntityQfpMemoryHCResourceGroup.setObjects(*((_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:ciscoEntityQfpMemoryHCResourceGroup.setStatus(_B)
ceqfpThroughputGroup=ObjectGroup((1,3,6,1,4,1,9,9,715,2,2,9))
ceqfpThroughputGroup.setObjects(*((_A,_S),(_A,_T),(_A,_AF),(_A,_AG),(_A,_U),(_A,_AH)))
if mibBuilder.loadTexts:ceqfpThroughputGroup.setStatus(_B)
ceqfpMemoryResRisingThreshNotif=NotificationType((1,3,6,1,4,1,9,9,715,0,1))
ceqfpMemoryResRisingThreshNotif.setObjects(*((_A,_N),(_A,_Q)))
if mibBuilder.loadTexts:ceqfpMemoryResRisingThreshNotif.setStatus(_B)
ceqfpMemoryResFallingThreshNotif=NotificationType((1,3,6,1,4,1,9,9,715,0,2))
ceqfpMemoryResFallingThreshNotif.setObjects(*((_A,_N),(_A,_R)))
if mibBuilder.loadTexts:ceqfpMemoryResFallingThreshNotif.setStatus(_B)
ceqfpThroughputNotif=NotificationType((1,3,6,1,4,1,9,9,715,0,3))
ceqfpThroughputNotif.setObjects(*((_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:ceqfpThroughputNotif.setStatus(_B)
ciscoEntityQfpNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,715,2,2,5))
ciscoEntityQfpNotifGroup.setObjects(*((_A,_AI),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:ciscoEntityQfpNotifGroup.setStatus(_B)
ciscoEntityQfpMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,715,2,1,1))
ciscoEntityQfpMIBComplianceRev1.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:ciscoEntityQfpMIBComplianceRev1.setStatus('deprecated')
ciscoEntityQfpMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,715,2,1,2))
ciscoEntityQfpMIBComplianceRev2.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_AL),(_A,_AM),(_A,_Z),(_A,_a),(_A,_AN)))
if mibBuilder.loadTexts:ciscoEntityQfpMIBComplianceRev2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CiscoQfpPacketRate':CiscoQfpPacketRate,'CiscoQfpBitRate':CiscoQfpBitRate,'CiscoQfpTimeInterval':CiscoQfpTimeInterval,'CiscoQfpMemoryResource':CiscoQfpMemoryResource,'ciscoEntityQfpMIB':ciscoEntityQfpMIB,'ciscoEntityQfpMIBNotifs':ciscoEntityQfpMIBNotifs,_AI:ceqfpMemoryResRisingThreshNotif,_AJ:ceqfpMemoryResFallingThreshNotif,_AK:ceqfpThroughputNotif,'ciscoEntityQfpMIBObjects':ciscoEntityQfpMIBObjects,'ciscoEntityQfp':ciscoEntityQfp,'ceqfpSystemTable':ceqfpSystemTable,'ceqfpSystemEntry':ceqfpSystemEntry,_g:ceqfpSystemTrafficDirection,_h:ceqfpSystemState,_i:ceqfpNumberSystemLoads,_j:ceqfpSystemLastLoadTime,_k:ceqfpFiveSecondUtilAlgo,_l:ceqfpOneMinuteUtilAlgo,_m:ceqfpFiveMinutesUtilAlgo,_n:ceqfpSixtyMinutesUtilAlgo,'ceqfpUtilizationTable':ceqfpUtilizationTable,'ceqfpUtilizationEntry':ceqfpUtilizationEntry,_c:ceqfpUtilTimeInterval,_o:ceqfpUtilInputPriorityPktRate,_p:ceqfpUtilInputPriorityBitRate,_q:ceqfpUtilInputNonPriorityPktRate,_r:ceqfpUtilInputNonPriorityBitRate,_s:ceqfpUtilInputTotalPktRate,_t:ceqfpUtilInputTotalBitRate,_u:ceqfpUtilOutputPriorityPktRate,_v:ceqfpUtilOutputPriorityBitRate,_w:ceqfpUtilOutputNonPriorityPktRate,_x:ceqfpUtilOutputNonPriorityBitRate,_y:ceqfpUtilOutputTotalPktRate,_z:ceqfpUtilOutputTotalBitRate,_A0:ceqfpUtilProcessingLoad,'ceqfpMemoryResourceTable':ceqfpMemoryResourceTable,'ceqfpMemoryResourceEntry':ceqfpMemoryResourceEntry,_e:ceqfpMemoryResType,_A1:ceqfpMemoryResTotal,_N:ceqfpMemoryResInUse,_A2:ceqfpMemoryResFree,_A3:ceqfpMemoryResLowFreeWatermark,_A4:ceqfpMemoryResRisingThreshold,_A5:ceqfpMemoryResFallingThreshold,_A7:ceqfpMemoryResTotalOvrflw,_AB:ceqfpMemoryHCResTotal,_A8:ceqfpMemoryResInUseOvrflw,_AC:ceqfpMemoryHCResInUse,_A9:ceqfpMemoryResFreeOvrflw,_AD:ceqfpMemoryHCResFree,_AA:ceqfpMemoryResLowFreeWatermarkOvrflw,_AE:ceqfpMemoryHCResLowFreeWatermark,'ceqfpThroughputTable':ceqfpThroughputTable,'ceqfpThroughputEntry':ceqfpThroughputEntry,_S:ceqfpThroughputLicensedBW,_T:ceqfpThroughputLevel,_AF:ceqfpThroughputInterval,_AG:ceqfpThroughputThreshold,_U:ceqfpThroughputAvgRate,'ciscoEntityQfpNotif':ciscoEntityQfpNotif,_A6:ceqfpMemoryResThreshNotifEnabled,_Q:ceqfpMemoryResCurrentRisingThresh,_R:ceqfpMemoryResCurrentFallingThresh,_AH:ceqfpThroughputNotifEnabled,'ciscoEntityQfpMIBConform':ciscoEntityQfpMIBConform,'ciscoEntityQfpMIBCompliances':ciscoEntityQfpMIBCompliances,'ciscoEntityQfpMIBComplianceRev1':ciscoEntityQfpMIBComplianceRev1,'ciscoEntityQfpMIBComplianceRev2':ciscoEntityQfpMIBComplianceRev2,'ciscoEntityQfpMIBGroups':ciscoEntityQfpMIBGroups,_V:ciscoEntityQfpSystemGroup,_X:ciscoEntityQfpUtilizationAlgoGroup,_W:ciscoEntityQfpUtilizationGroup,_Y:ciscoEntityQfpMemoryResourceGroup,_a:ciscoEntityQfpNotifGroup,_Z:ciscoEntityQfpMemoryResNotifGroup,_AL:ciscoEntityQfpMemoryResourceOvrflwGroup,_AM:ciscoEntityQfpMemoryHCResourceGroup,_AN:ceqfpThroughputGroup})