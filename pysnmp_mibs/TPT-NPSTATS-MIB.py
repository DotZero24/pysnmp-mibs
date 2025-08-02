_I='npstatsStackMemberIndex'
_H='npstatsTierNumber'
_G='not-accessible'
_F='npstatsRulesRank'
_E='DisplayString'
_D='OctetString'
_C='TPT-NPSTATS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
tpt_tpa_objs,=mibBuilder.importSymbols('TPT-TPAMIBS-MIB','tpt-tpa-objs')
tpt_npstats=ModuleIdentity((1,3,6,1,4,1,10734,3,3,2,10))
if mibBuilder.loadTexts:tpt_npstats.setRevisions(('2016-05-25 18:54','2016-05-03 17:26'))
_NpstatsRulesTable_Object=MibTable
npstatsRulesTable=_NpstatsRulesTable_Object((1,3,6,1,4,1,10734,3,3,2,10,1))
if mibBuilder.loadTexts:npstatsRulesTable.setStatus(_A)
_NpstatsRulesEntry_Object=MibTableRow
npstatsRulesEntry=_NpstatsRulesEntry_Object((1,3,6,1,4,1,10734,3,3,2,10,1,1))
npstatsRulesEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:npstatsRulesEntry.setStatus(_A)
_NpstatsRulesRank_Type=Unsigned32
_NpstatsRulesRank_Object=MibTableColumn
npstatsRulesRank=_NpstatsRulesRank_Object((1,3,6,1,4,1,10734,3,3,2,10,1,1,1),_NpstatsRulesRank_Type())
npstatsRulesRank.setMaxAccess(_G)
if mibBuilder.loadTexts:npstatsRulesRank.setStatus(_A)
_NpstatsRulesFilter_Type=Unsigned32
_NpstatsRulesFilter_Object=MibTableColumn
npstatsRulesFilter=_NpstatsRulesFilter_Object((1,3,6,1,4,1,10734,3,3,2,10,1,1,2),_NpstatsRulesFilter_Type())
npstatsRulesFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsRulesFilter.setStatus(_A)
_NpstatsRulesFlows_Type=Unsigned32
_NpstatsRulesFlows_Object=MibTableColumn
npstatsRulesFlows=_NpstatsRulesFlows_Object((1,3,6,1,4,1,10734,3,3,2,10,1,1,3),_NpstatsRulesFlows_Type())
npstatsRulesFlows.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsRulesFlows.setStatus(_A)
_NpstatsRulesSuccess_Type=Unsigned32
_NpstatsRulesSuccess_Object=MibTableColumn
npstatsRulesSuccess=_NpstatsRulesSuccess_Object((1,3,6,1,4,1,10734,3,3,2,10,1,1,4),_NpstatsRulesSuccess_Type())
npstatsRulesSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsRulesSuccess.setStatus(_A)
_NpstatsRulesTotalPercent_Type=Unsigned32
_NpstatsRulesTotalPercent_Object=MibTableColumn
npstatsRulesTotalPercent=_NpstatsRulesTotalPercent_Object((1,3,6,1,4,1,10734,3,3,2,10,1,1,5),_NpstatsRulesTotalPercent_Type())
npstatsRulesTotalPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsRulesTotalPercent.setStatus(_A)
_NpstatsRulesSuccessPer10K_Type=Unsigned32
_NpstatsRulesSuccessPer10K_Object=MibTableColumn
npstatsRulesSuccessPer10K=_NpstatsRulesSuccessPer10K_Object((1,3,6,1,4,1,10734,3,3,2,10,1,1,6),_NpstatsRulesSuccessPer10K_Type())
npstatsRulesSuccessPer10K.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsRulesSuccessPer10K.setStatus(_A)
_NpstatsTiersTable_Object=MibTable
npstatsTiersTable=_NpstatsTiersTable_Object((1,3,6,1,4,1,10734,3,3,2,10,2))
if mibBuilder.loadTexts:npstatsTiersTable.setStatus(_A)
_NpstatsTiersEntry_Object=MibTableRow
npstatsTiersEntry=_NpstatsTiersEntry_Object((1,3,6,1,4,1,10734,3,3,2,10,2,1))
npstatsTiersEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:npstatsTiersEntry.setStatus(_A)
_NpstatsTierNumber_Type=Unsigned32
_NpstatsTierNumber_Object=MibTableColumn
npstatsTierNumber=_NpstatsTierNumber_Object((1,3,6,1,4,1,10734,3,3,2,10,2,1,1),_NpstatsTierNumber_Type())
npstatsTierNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:npstatsTierNumber.setStatus(_A)
_NpstatsTiersReceiveMbps_Type=Unsigned32
_NpstatsTiersReceiveMbps_Object=MibTableColumn
npstatsTiersReceiveMbps=_NpstatsTiersReceiveMbps_Object((1,3,6,1,4,1,10734,3,3,2,10,2,1,2),_NpstatsTiersReceiveMbps_Type())
npstatsTiersReceiveMbps.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTiersReceiveMbps.setStatus(_A)
_NpstatsTiersTransmitMbps_Type=Unsigned32
_NpstatsTiersTransmitMbps_Object=MibTableColumn
npstatsTiersTransmitMbps=_NpstatsTiersTransmitMbps_Object((1,3,6,1,4,1,10734,3,3,2,10,2,1,3),_NpstatsTiersTransmitMbps_Type())
npstatsTiersTransmitMbps.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTiersTransmitMbps.setStatus(_A)
_NpstatsTiersRxPktsPerSec_Type=Unsigned32
_NpstatsTiersRxPktsPerSec_Object=MibTableColumn
npstatsTiersRxPktsPerSec=_NpstatsTiersRxPktsPerSec_Object((1,3,6,1,4,1,10734,3,3,2,10,2,1,4),_NpstatsTiersRxPktsPerSec_Type())
npstatsTiersRxPktsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTiersRxPktsPerSec.setStatus(_A)
_NpstatsTiersMaxPktsPerSec_Type=Unsigned32
_NpstatsTiersMaxPktsPerSec_Object=MibTableColumn
npstatsTiersMaxPktsPerSec=_NpstatsTiersMaxPktsPerSec_Object((1,3,6,1,4,1,10734,3,3,2,10,2,1,5),_NpstatsTiersMaxPktsPerSec_Type())
npstatsTiersMaxPktsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTiersMaxPktsPerSec.setStatus(_A)
_NpstatsTiersAvgBytesPerPkt_Type=Unsigned32
_NpstatsTiersAvgBytesPerPkt_Object=MibTableColumn
npstatsTiersAvgBytesPerPkt=_NpstatsTiersAvgBytesPerPkt_Object((1,3,6,1,4,1,10734,3,3,2,10,2,1,6),_NpstatsTiersAvgBytesPerPkt_Type())
npstatsTiersAvgBytesPerPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTiersAvgBytesPerPkt.setStatus(_A)
_NpstatsTiersUtilizationPercent_Type=Integer32
_NpstatsTiersUtilizationPercent_Object=MibTableColumn
npstatsTiersUtilizationPercent=_NpstatsTiersUtilizationPercent_Object((1,3,6,1,4,1,10734,3,3,2,10,2,1,7),_NpstatsTiersUtilizationPercent_Type())
npstatsTiersUtilizationPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTiersUtilizationPercent.setStatus(_A)
_NpstatsTiersRatioToNextPer10K_Type=Unsigned32
_NpstatsTiersRatioToNextPer10K_Object=MibTableColumn
npstatsTiersRatioToNextPer10K=_NpstatsTiersRatioToNextPer10K_Object((1,3,6,1,4,1,10734,3,3,2,10,2,1,8),_NpstatsTiersRatioToNextPer10K_Type())
npstatsTiersRatioToNextPer10K.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTiersRatioToNextPer10K.setStatus(_A)
_NpstatsTiersMaxReceiveMbps_Type=Unsigned32
_NpstatsTiersMaxReceiveMbps_Object=MibTableColumn
npstatsTiersMaxReceiveMbps=_NpstatsTiersMaxReceiveMbps_Object((1,3,6,1,4,1,10734,3,3,2,10,2,1,9),_NpstatsTiersMaxReceiveMbps_Type())
npstatsTiersMaxReceiveMbps.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTiersMaxReceiveMbps.setStatus(_A)
_NpstatsTiersMaxTransmitMbps_Type=Unsigned32
_NpstatsTiersMaxTransmitMbps_Object=MibTableColumn
npstatsTiersMaxTransmitMbps=_NpstatsTiersMaxTransmitMbps_Object((1,3,6,1,4,1,10734,3,3,2,10,2,1,10),_NpstatsTiersMaxTransmitMbps_Type())
npstatsTiersMaxTransmitMbps.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTiersMaxTransmitMbps.setStatus(_A)
_NpstatsTiersMaxUtilizationPercent_Type=Integer32
_NpstatsTiersMaxUtilizationPercent_Object=MibTableColumn
npstatsTiersMaxUtilizationPercent=_NpstatsTiersMaxUtilizationPercent_Object((1,3,6,1,4,1,10734,3,3,2,10,2,1,11),_NpstatsTiersMaxUtilizationPercent_Type())
npstatsTiersMaxUtilizationPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTiersMaxUtilizationPercent.setStatus(_A)
_NpstatsTiersMaxRatioToNextPer10K_Type=Unsigned32
_NpstatsTiersMaxRatioToNextPer10K_Object=MibTableColumn
npstatsTiersMaxRatioToNextPer10K=_NpstatsTiersMaxRatioToNextPer10K_Object((1,3,6,1,4,1,10734,3,3,2,10,2,1,12),_NpstatsTiersMaxRatioToNextPer10K_Type())
npstatsTiersMaxRatioToNextPer10K.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTiersMaxRatioToNextPer10K.setStatus(_A)
_NpstatsTiersExtra_ObjectIdentity=ObjectIdentity
npstatsTiersExtra=_NpstatsTiersExtra_ObjectIdentity((1,3,6,1,4,1,10734,3,3,2,10,3))
if mibBuilder.loadTexts:npstatsTiersExtra.setStatus(_A)
_NpstatsTier1BypassMbps_Type=Unsigned32
_NpstatsTier1BypassMbps_Object=MibScalar
npstatsTier1BypassMbps=_NpstatsTier1BypassMbps_Object((1,3,6,1,4,1,10734,3,3,2,10,3,1),_NpstatsTier1BypassMbps_Type())
npstatsTier1BypassMbps.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier1BypassMbps.setStatus(_A)
_NpstatsTier1Balance_Type=Unsigned32
_NpstatsTier1Balance_Object=MibScalar
npstatsTier1Balance=_NpstatsTier1Balance_Object((1,3,6,1,4,1,10734,3,3,2,10,3,2),_NpstatsTier1Balance_Type())
npstatsTier1Balance.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier1Balance.setStatus(_A)
_NpstatsTier1MaxPktsPerSecA_Type=Unsigned32
_NpstatsTier1MaxPktsPerSecA_Object=MibScalar
npstatsTier1MaxPktsPerSecA=_NpstatsTier1MaxPktsPerSecA_Object((1,3,6,1,4,1,10734,3,3,2,10,3,3),_NpstatsTier1MaxPktsPerSecA_Type())
npstatsTier1MaxPktsPerSecA.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier1MaxPktsPerSecA.setStatus(_A)
_NpstatsTier1MaxPktsPerSecB_Type=Unsigned32
_NpstatsTier1MaxPktsPerSecB_Object=MibScalar
npstatsTier1MaxPktsPerSecB=_NpstatsTier1MaxPktsPerSecB_Object((1,3,6,1,4,1,10734,3,3,2,10,3,4),_NpstatsTier1MaxPktsPerSecB_Type())
npstatsTier1MaxPktsPerSecB.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier1MaxPktsPerSecB.setStatus(_A)
_NpstatsTier4TriggerMatchPer1000_Type=Unsigned32
_NpstatsTier4TriggerMatchPer1000_Object=MibScalar
npstatsTier4TriggerMatchPer1000=_NpstatsTier4TriggerMatchPer1000_Object((1,3,6,1,4,1,10734,3,3,2,10,3,5),_NpstatsTier4TriggerMatchPer1000_Type())
npstatsTier4TriggerMatchPer1000.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier4TriggerMatchPer1000.setStatus(_A)
_NpstatsTier4ReroutePer1000_Type=Unsigned32
_NpstatsTier4ReroutePer1000_Object=MibScalar
npstatsTier4ReroutePer1000=_NpstatsTier4ReroutePer1000_Object((1,3,6,1,4,1,10734,3,3,2,10,3,6),_NpstatsTier4ReroutePer1000_Type())
npstatsTier4ReroutePer1000.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier4ReroutePer1000.setStatus(_A)
_NpstatsTier4TcpSequencePer1000_Type=Unsigned32
_NpstatsTier4TcpSequencePer1000_Object=MibScalar
npstatsTier4TcpSequencePer1000=_NpstatsTier4TcpSequencePer1000_Object((1,3,6,1,4,1,10734,3,3,2,10,3,7),_NpstatsTier4TcpSequencePer1000_Type())
npstatsTier4TcpSequencePer1000.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier4TcpSequencePer1000.setStatus(_A)
_NpstatsTier1TxPktsPerSec_Type=Unsigned32
_NpstatsTier1TxPktsPerSec_Object=MibScalar
npstatsTier1TxPktsPerSec=_NpstatsTier1TxPktsPerSec_Object((1,3,6,1,4,1,10734,3,3,2,10,3,8),_NpstatsTier1TxPktsPerSec_Type())
npstatsTier1TxPktsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier1TxPktsPerSec.setStatus(_A)
_NpstatsTier1MaxTxPktsPerSec_Type=Unsigned32
_NpstatsTier1MaxTxPktsPerSec_Object=MibScalar
npstatsTier1MaxTxPktsPerSec=_NpstatsTier1MaxTxPktsPerSec_Object((1,3,6,1,4,1,10734,3,3,2,10,3,9),_NpstatsTier1MaxTxPktsPerSec_Type())
npstatsTier1MaxTxPktsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier1MaxTxPktsPerSec.setStatus(_A)
_NpstatsTier1MaxPktsPerSecC_Type=Unsigned32
_NpstatsTier1MaxPktsPerSecC_Object=MibScalar
npstatsTier1MaxPktsPerSecC=_NpstatsTier1MaxPktsPerSecC_Object((1,3,6,1,4,1,10734,3,3,2,10,3,10),_NpstatsTier1MaxPktsPerSecC_Type())
npstatsTier1MaxPktsPerSecC.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier1MaxPktsPerSecC.setStatus(_A)
_NpstatsTier4ProtoDcdPer1000_Type=Unsigned32
_NpstatsTier4ProtoDcdPer1000_Object=MibScalar
npstatsTier4ProtoDcdPer1000=_NpstatsTier4ProtoDcdPer1000_Object((1,3,6,1,4,1,10734,3,3,2,10,3,11),_NpstatsTier4ProtoDcdPer1000_Type())
npstatsTier4ProtoDcdPer1000.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier4ProtoDcdPer1000.setStatus(_A)
_NpstatsTier2TxTrustedPktsPerSec_Type=Unsigned32
_NpstatsTier2TxTrustedPktsPerSec_Object=MibScalar
npstatsTier2TxTrustedPktsPerSec=_NpstatsTier2TxTrustedPktsPerSec_Object((1,3,6,1,4,1,10734,3,3,2,10,3,12),_NpstatsTier2TxTrustedPktsPerSec_Type())
npstatsTier2TxTrustedPktsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier2TxTrustedPktsPerSec.setStatus(_A)
_NpstatsTier3TxTrustedPktsPerSec_Type=Unsigned32
_NpstatsTier3TxTrustedPktsPerSec_Object=MibScalar
npstatsTier3TxTrustedPktsPerSec=_NpstatsTier3TxTrustedPktsPerSec_Object((1,3,6,1,4,1,10734,3,3,2,10,3,13),_NpstatsTier3TxTrustedPktsPerSec_Type())
npstatsTier3TxTrustedPktsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier3TxTrustedPktsPerSec.setStatus(_A)
_NpstatsTier4TxTrustedPktsPerSec_Type=Unsigned32
_NpstatsTier4TxTrustedPktsPerSec_Object=MibScalar
npstatsTier4TxTrustedPktsPerSec=_NpstatsTier4TxTrustedPktsPerSec_Object((1,3,6,1,4,1,10734,3,3,2,10,3,14),_NpstatsTier4TxTrustedPktsPerSec_Type())
npstatsTier4TxTrustedPktsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier4TxTrustedPktsPerSec.setStatus(_A)
_NpstatsTier1BypassPktsPerSec_Type=Unsigned32
_NpstatsTier1BypassPktsPerSec_Object=MibScalar
npstatsTier1BypassPktsPerSec=_NpstatsTier1BypassPktsPerSec_Object((1,3,6,1,4,1,10734,3,3,2,10,3,15),_NpstatsTier1BypassPktsPerSec_Type())
npstatsTier1BypassPktsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier1BypassPktsPerSec.setStatus(_A)
_NpstatsTier1MaxBypassPktsPerSec_Type=Unsigned32
_NpstatsTier1MaxBypassPktsPerSec_Object=MibScalar
npstatsTier1MaxBypassPktsPerSec=_NpstatsTier1MaxBypassPktsPerSec_Object((1,3,6,1,4,1,10734,3,3,2,10,3,16),_NpstatsTier1MaxBypassPktsPerSec_Type())
npstatsTier1MaxBypassPktsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier1MaxBypassPktsPerSec.setStatus(_A)
_NpstatsTier1BypassToRxPktsPerSecRatio_Type=Unsigned32
_NpstatsTier1BypassToRxPktsPerSecRatio_Object=MibScalar
npstatsTier1BypassToRxPktsPerSecRatio=_NpstatsTier1BypassToRxPktsPerSecRatio_Object((1,3,6,1,4,1,10734,3,3,2,10,3,17),_NpstatsTier1BypassToRxPktsPerSecRatio_Type())
npstatsTier1BypassToRxPktsPerSecRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier1BypassToRxPktsPerSecRatio.setStatus(_A)
_NpstatsTier1VlanTransPktsPerSec_Type=Unsigned32
_NpstatsTier1VlanTransPktsPerSec_Object=MibScalar
npstatsTier1VlanTransPktsPerSec=_NpstatsTier1VlanTransPktsPerSec_Object((1,3,6,1,4,1,10734,3,3,2,10,3,18),_NpstatsTier1VlanTransPktsPerSec_Type())
npstatsTier1VlanTransPktsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier1VlanTransPktsPerSec.setStatus(_A)
_NpstatsTier1MaxVlanTransPktsPerSec_Type=Unsigned32
_NpstatsTier1MaxVlanTransPktsPerSec_Object=MibScalar
npstatsTier1MaxVlanTransPktsPerSec=_NpstatsTier1MaxVlanTransPktsPerSec_Object((1,3,6,1,4,1,10734,3,3,2,10,3,19),_NpstatsTier1MaxVlanTransPktsPerSec_Type())
npstatsTier1MaxVlanTransPktsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier1MaxVlanTransPktsPerSec.setStatus(_A)
_NpstatsTier1VlanTransToRxPktsPerSecRatio_Type=Unsigned32
_NpstatsTier1VlanTransToRxPktsPerSecRatio_Object=MibScalar
npstatsTier1VlanTransToRxPktsPerSecRatio=_NpstatsTier1VlanTransToRxPktsPerSecRatio_Object((1,3,6,1,4,1,10734,3,3,2,10,3,20),_NpstatsTier1VlanTransToRxPktsPerSecRatio_Type())
npstatsTier1VlanTransToRxPktsPerSecRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier1VlanTransToRxPktsPerSecRatio.setStatus(_A)
_NpstatsTier1PatternMatchToRxPktsPerSecRatio_Type=Unsigned32
_NpstatsTier1PatternMatchToRxPktsPerSecRatio_Object=MibScalar
npstatsTier1PatternMatchToRxPktsPerSecRatio=_NpstatsTier1PatternMatchToRxPktsPerSecRatio_Object((1,3,6,1,4,1,10734,3,3,2,10,3,21),_NpstatsTier1PatternMatchToRxPktsPerSecRatio_Type())
npstatsTier1PatternMatchToRxPktsPerSecRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier1PatternMatchToRxPktsPerSecRatio.setStatus(_A)
_NpstatsTier1MaxPatternMatchToRxPktsPerSecRatio_Type=Unsigned32
_NpstatsTier1MaxPatternMatchToRxPktsPerSecRatio_Object=MibScalar
npstatsTier1MaxPatternMatchToRxPktsPerSecRatio=_NpstatsTier1MaxPatternMatchToRxPktsPerSecRatio_Object((1,3,6,1,4,1,10734,3,3,2,10,3,22),_NpstatsTier1MaxPatternMatchToRxPktsPerSecRatio_Type())
npstatsTier1MaxPatternMatchToRxPktsPerSecRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier1MaxPatternMatchToRxPktsPerSecRatio.setStatus(_A)
_NpstatsTier2MaxTxTrustedPktsPerSec_Type=Unsigned32
_NpstatsTier2MaxTxTrustedPktsPerSec_Object=MibScalar
npstatsTier2MaxTxTrustedPktsPerSec=_NpstatsTier2MaxTxTrustedPktsPerSec_Object((1,3,6,1,4,1,10734,3,3,2,10,3,23),_NpstatsTier2MaxTxTrustedPktsPerSec_Type())
npstatsTier2MaxTxTrustedPktsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier2MaxTxTrustedPktsPerSec.setStatus(_A)
_NpstatsTier3MaxTxTrustedPktsPerSec_Type=Unsigned32
_NpstatsTier3MaxTxTrustedPktsPerSec_Object=MibScalar
npstatsTier3MaxTxTrustedPktsPerSec=_NpstatsTier3MaxTxTrustedPktsPerSec_Object((1,3,6,1,4,1,10734,3,3,2,10,3,24),_NpstatsTier3MaxTxTrustedPktsPerSec_Type())
npstatsTier3MaxTxTrustedPktsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier3MaxTxTrustedPktsPerSec.setStatus(_A)
_NpstatsTier4MaxTxTrustedPktsPerSec_Type=Unsigned32
_NpstatsTier4MaxTxTrustedPktsPerSec_Object=MibScalar
npstatsTier4MaxTxTrustedPktsPerSec=_NpstatsTier4MaxTxTrustedPktsPerSec_Object((1,3,6,1,4,1,10734,3,3,2,10,3,25),_NpstatsTier4MaxTxTrustedPktsPerSec_Type())
npstatsTier4MaxTxTrustedPktsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier4MaxTxTrustedPktsPerSec.setStatus(_A)
_NpstatsTier4MaxTriggerMatchPer1000_Type=Unsigned32
_NpstatsTier4MaxTriggerMatchPer1000_Object=MibScalar
npstatsTier4MaxTriggerMatchPer1000=_NpstatsTier4MaxTriggerMatchPer1000_Object((1,3,6,1,4,1,10734,3,3,2,10,3,26),_NpstatsTier4MaxTriggerMatchPer1000_Type())
npstatsTier4MaxTriggerMatchPer1000.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier4MaxTriggerMatchPer1000.setStatus(_A)
_NpstatsTier4MaxReroutePer1000_Type=Unsigned32
_NpstatsTier4MaxReroutePer1000_Object=MibScalar
npstatsTier4MaxReroutePer1000=_NpstatsTier4MaxReroutePer1000_Object((1,3,6,1,4,1,10734,3,3,2,10,3,27),_NpstatsTier4MaxReroutePer1000_Type())
npstatsTier4MaxReroutePer1000.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier4MaxReroutePer1000.setStatus(_A)
_NpstatsTier4MaxTcpSequencePer1000_Type=Unsigned32
_NpstatsTier4MaxTcpSequencePer1000_Object=MibScalar
npstatsTier4MaxTcpSequencePer1000=_NpstatsTier4MaxTcpSequencePer1000_Object((1,3,6,1,4,1,10734,3,3,2,10,3,28),_NpstatsTier4MaxTcpSequencePer1000_Type())
npstatsTier4MaxTcpSequencePer1000.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier4MaxTcpSequencePer1000.setStatus(_A)
_NpstatsTier4MaxProtoDcdPer1000_Type=Unsigned32
_NpstatsTier4MaxProtoDcdPer1000_Object=MibScalar
npstatsTier4MaxProtoDcdPer1000=_NpstatsTier4MaxProtoDcdPer1000_Object((1,3,6,1,4,1,10734,3,3,2,10,3,29),_NpstatsTier4MaxProtoDcdPer1000_Type())
npstatsTier4MaxProtoDcdPer1000.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsTier4MaxProtoDcdPer1000.setStatus(_A)
_NpstatsMisc_ObjectIdentity=ObjectIdentity
npstatsMisc=_NpstatsMisc_ObjectIdentity((1,3,6,1,4,1,10734,3,3,2,10,4))
if mibBuilder.loadTexts:npstatsMisc.setStatus(_A)
_NpstatsMiscTxPktsBestEffort_Type=Counter64
_NpstatsMiscTxPktsBestEffort_Object=MibScalar
npstatsMiscTxPktsBestEffort=_NpstatsMiscTxPktsBestEffort_Object((1,3,6,1,4,1,10734,3,3,2,10,4,1),_NpstatsMiscTxPktsBestEffort_Type())
npstatsMiscTxPktsBestEffort.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsMiscTxPktsBestEffort.setStatus(_A)
_NpstatsSslInsp_ObjectIdentity=ObjectIdentity
npstatsSslInsp=_NpstatsSslInsp_ObjectIdentity((1,3,6,1,4,1,10734,3,3,2,10,5))
if mibBuilder.loadTexts:npstatsSslInsp.setStatus(_A)
_NpstatsSslInspCurrentSessions_Type=Counter64
_NpstatsSslInspCurrentSessions_Object=MibScalar
npstatsSslInspCurrentSessions=_NpstatsSslInspCurrentSessions_Object((1,3,6,1,4,1,10734,3,3,2,10,5,1),_NpstatsSslInspCurrentSessions_Type())
npstatsSslInspCurrentSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsSslInspCurrentSessions.setStatus(_A)
class _NpstatsSslInspConnectionRate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_NpstatsSslInspConnectionRate_Type.__name__=_E
_NpstatsSslInspConnectionRate_Object=MibScalar
npstatsSslInspConnectionRate=_NpstatsSslInspConnectionRate_Object((1,3,6,1,4,1,10734,3,3,2,10,5,2),_NpstatsSslInspConnectionRate_Type())
npstatsSslInspConnectionRate.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsSslInspConnectionRate.setStatus(_A)
_NpstatsSslInspBlockedMaxConns_Type=Counter64
_NpstatsSslInspBlockedMaxConns_Object=MibScalar
npstatsSslInspBlockedMaxConns=_NpstatsSslInspBlockedMaxConns_Object((1,3,6,1,4,1,10734,3,3,2,10,5,3),_NpstatsSslInspBlockedMaxConns_Type())
npstatsSslInspBlockedMaxConns.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsSslInspBlockedMaxConns.setStatus(_A)
_NpstatsSslInspPassedMaxConns_Type=Counter64
_NpstatsSslInspPassedMaxConns_Object=MibScalar
npstatsSslInspPassedMaxConns=_NpstatsSslInspPassedMaxConns_Object((1,3,6,1,4,1,10734,3,3,2,10,5,4),_NpstatsSslInspPassedMaxConns_Type())
npstatsSslInspPassedMaxConns.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsSslInspPassedMaxConns.setStatus(_A)
_NpstatsSslInspTotalBytesIn_Type=Counter64
_NpstatsSslInspTotalBytesIn_Object=MibScalar
npstatsSslInspTotalBytesIn=_NpstatsSslInspTotalBytesIn_Object((1,3,6,1,4,1,10734,3,3,2,10,5,5),_NpstatsSslInspTotalBytesIn_Type())
npstatsSslInspTotalBytesIn.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsSslInspTotalBytesIn.setStatus(_A)
_NpstatsSslInspTotalBytesOut_Type=Counter64
_NpstatsSslInspTotalBytesOut_Object=MibScalar
npstatsSslInspTotalBytesOut=_NpstatsSslInspTotalBytesOut_Object((1,3,6,1,4,1,10734,3,3,2,10,5,6),_NpstatsSslInspTotalBytesOut_Type())
npstatsSslInspTotalBytesOut.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsSslInspTotalBytesOut.setStatus(_A)
_NpstatsStackSegmentPorts_ObjectIdentity=ObjectIdentity
npstatsStackSegmentPorts=_NpstatsStackSegmentPorts_ObjectIdentity((1,3,6,1,4,1,10734,3,3,2,10,10))
if mibBuilder.loadTexts:npstatsStackSegmentPorts.setStatus(_A)
_NpstatsStackSegmentRecieveMbps_Type=Unsigned32
_NpstatsStackSegmentRecieveMbps_Object=MibScalar
npstatsStackSegmentRecieveMbps=_NpstatsStackSegmentRecieveMbps_Object((1,3,6,1,4,1,10734,3,3,2,10,10,1),_NpstatsStackSegmentRecieveMbps_Type())
npstatsStackSegmentRecieveMbps.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackSegmentRecieveMbps.setStatus(_A)
_NpstatsStackSegmentMaxRecieveMbps_Type=Unsigned32
_NpstatsStackSegmentMaxRecieveMbps_Object=MibScalar
npstatsStackSegmentMaxRecieveMbps=_NpstatsStackSegmentMaxRecieveMbps_Object((1,3,6,1,4,1,10734,3,3,2,10,10,2),_NpstatsStackSegmentMaxRecieveMbps_Type())
npstatsStackSegmentMaxRecieveMbps.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackSegmentMaxRecieveMbps.setStatus(_A)
_NpstatsStackSegmentTransmitMbps_Type=Unsigned32
_NpstatsStackSegmentTransmitMbps_Object=MibScalar
npstatsStackSegmentTransmitMbps=_NpstatsStackSegmentTransmitMbps_Object((1,3,6,1,4,1,10734,3,3,2,10,10,3),_NpstatsStackSegmentTransmitMbps_Type())
npstatsStackSegmentTransmitMbps.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackSegmentTransmitMbps.setStatus(_A)
_NpstatsStackSegmentMaxTransmitMbps_Type=Unsigned32
_NpstatsStackSegmentMaxTransmitMbps_Object=MibScalar
npstatsStackSegmentMaxTransmitMbps=_NpstatsStackSegmentMaxTransmitMbps_Object((1,3,6,1,4,1,10734,3,3,2,10,10,4),_NpstatsStackSegmentMaxTransmitMbps_Type())
npstatsStackSegmentMaxTransmitMbps.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackSegmentMaxTransmitMbps.setStatus(_A)
_NpstatsStackBalance_Type=Unsigned32
_NpstatsStackBalance_Object=MibScalar
npstatsStackBalance=_NpstatsStackBalance_Object((1,3,6,1,4,1,10734,3,3,2,10,10,5),_NpstatsStackBalance_Type())
npstatsStackBalance.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackBalance.setStatus(_A)
_NpstatsStackMinBalance_Type=Unsigned32
_NpstatsStackMinBalance_Object=MibScalar
npstatsStackMinBalance=_NpstatsStackMinBalance_Object((1,3,6,1,4,1,10734,3,3,2,10,10,6),_NpstatsStackMinBalance_Type())
npstatsStackMinBalance.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackMinBalance.setStatus(_A)
_NpstatsStackSegmentRatioToTier1Per10K_Type=Unsigned32
_NpstatsStackSegmentRatioToTier1Per10K_Object=MibScalar
npstatsStackSegmentRatioToTier1Per10K=_NpstatsStackSegmentRatioToTier1Per10K_Object((1,3,6,1,4,1,10734,3,3,2,10,10,7),_NpstatsStackSegmentRatioToTier1Per10K_Type())
npstatsStackSegmentRatioToTier1Per10K.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackSegmentRatioToTier1Per10K.setStatus(_A)
_NpstatsStackSegmentMaxRatioToTier1Per10K_Type=Unsigned32
_NpstatsStackSegmentMaxRatioToTier1Per10K_Object=MibScalar
npstatsStackSegmentMaxRatioToTier1Per10K=_NpstatsStackSegmentMaxRatioToTier1Per10K_Object((1,3,6,1,4,1,10734,3,3,2,10,10,8),_NpstatsStackSegmentMaxRatioToTier1Per10K_Type())
npstatsStackSegmentMaxRatioToTier1Per10K.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackSegmentMaxRatioToTier1Per10K.setStatus(_A)
_NpstatsStackSegmentPortTable_Object=MibTable
npstatsStackSegmentPortTable=_NpstatsStackSegmentPortTable_Object((1,3,6,1,4,1,10734,3,3,2,10,10,9))
if mibBuilder.loadTexts:npstatsStackSegmentPortTable.setStatus(_A)
_NpstatsStackSegmentPortEntry_Object=MibTableRow
npstatsStackSegmentPortEntry=_NpstatsStackSegmentPortEntry_Object((1,3,6,1,4,1,10734,3,3,2,10,10,9,1))
npstatsStackSegmentPortEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:npstatsStackSegmentPortEntry.setStatus(_A)
_NpstatsStackMemberIndex_Type=Unsigned32
_NpstatsStackMemberIndex_Object=MibTableColumn
npstatsStackMemberIndex=_NpstatsStackMemberIndex_Object((1,3,6,1,4,1,10734,3,3,2,10,10,9,1,1),_NpstatsStackMemberIndex_Type())
npstatsStackMemberIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackMemberIndex.setStatus(_A)
class _NpstatsStackMemberKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_NpstatsStackMemberKey_Type.__name__=_D
_NpstatsStackMemberKey_Object=MibTableColumn
npstatsStackMemberKey=_NpstatsStackMemberKey_Object((1,3,6,1,4,1,10734,3,3,2,10,10,9,1,2),_NpstatsStackMemberKey_Type())
npstatsStackMemberKey.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackMemberKey.setStatus(_A)
class _NpstatsStackMemberHostname_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NpstatsStackMemberHostname_Type.__name__=_D
_NpstatsStackMemberHostname_Object=MibTableColumn
npstatsStackMemberHostname=_NpstatsStackMemberHostname_Object((1,3,6,1,4,1,10734,3,3,2,10,10,9,1,3),_NpstatsStackMemberHostname_Type())
npstatsStackMemberHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackMemberHostname.setStatus(_A)
_NpstatsStackMemberSegmentReceiveMbps_Type=Unsigned32
_NpstatsStackMemberSegmentReceiveMbps_Object=MibTableColumn
npstatsStackMemberSegmentReceiveMbps=_NpstatsStackMemberSegmentReceiveMbps_Object((1,3,6,1,4,1,10734,3,3,2,10,10,9,1,4),_NpstatsStackMemberSegmentReceiveMbps_Type())
npstatsStackMemberSegmentReceiveMbps.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackMemberSegmentReceiveMbps.setStatus(_A)
_NpstatsStackMemberMaxSegmentReceiveMbps_Type=Unsigned32
_NpstatsStackMemberMaxSegmentReceiveMbps_Object=MibTableColumn
npstatsStackMemberMaxSegmentReceiveMbps=_NpstatsStackMemberMaxSegmentReceiveMbps_Object((1,3,6,1,4,1,10734,3,3,2,10,10,9,1,5),_NpstatsStackMemberMaxSegmentReceiveMbps_Type())
npstatsStackMemberMaxSegmentReceiveMbps.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackMemberMaxSegmentReceiveMbps.setStatus(_A)
_NpstatsStackPorts_ObjectIdentity=ObjectIdentity
npstatsStackPorts=_NpstatsStackPorts_ObjectIdentity((1,3,6,1,4,1,10734,3,3,2,10,11))
if mibBuilder.loadTexts:npstatsStackPorts.setStatus(_A)
_NpstatsStackPortsRecieveMbps_Type=Unsigned32
_NpstatsStackPortsRecieveMbps_Object=MibScalar
npstatsStackPortsRecieveMbps=_NpstatsStackPortsRecieveMbps_Object((1,3,6,1,4,1,10734,3,3,2,10,11,1),_NpstatsStackPortsRecieveMbps_Type())
npstatsStackPortsRecieveMbps.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackPortsRecieveMbps.setStatus(_A)
_NpstatsStackPortsMaxRecieveMbps_Type=Unsigned32
_NpstatsStackPortsMaxRecieveMbps_Object=MibScalar
npstatsStackPortsMaxRecieveMbps=_NpstatsStackPortsMaxRecieveMbps_Object((1,3,6,1,4,1,10734,3,3,2,10,11,2),_NpstatsStackPortsMaxRecieveMbps_Type())
npstatsStackPortsMaxRecieveMbps.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackPortsMaxRecieveMbps.setStatus(_A)
_NpstatsStackPortsTransmitMbps_Type=Unsigned32
_NpstatsStackPortsTransmitMbps_Object=MibScalar
npstatsStackPortsTransmitMbps=_NpstatsStackPortsTransmitMbps_Object((1,3,6,1,4,1,10734,3,3,2,10,11,3),_NpstatsStackPortsTransmitMbps_Type())
npstatsStackPortsTransmitMbps.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackPortsTransmitMbps.setStatus(_A)
_NpstatsStackPortsMaxTransmitMbps_Type=Unsigned32
_NpstatsStackPortsMaxTransmitMbps_Object=MibScalar
npstatsStackPortsMaxTransmitMbps=_NpstatsStackPortsMaxTransmitMbps_Object((1,3,6,1,4,1,10734,3,3,2,10,11,4),_NpstatsStackPortsMaxTransmitMbps_Type())
npstatsStackPortsMaxTransmitMbps.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackPortsMaxTransmitMbps.setStatus(_A)
_NpstatsStackRxToStackTxMbps_Type=Unsigned32
_NpstatsStackRxToStackTxMbps_Object=MibScalar
npstatsStackRxToStackTxMbps=_NpstatsStackRxToStackTxMbps_Object((1,3,6,1,4,1,10734,3,3,2,10,11,5),_NpstatsStackRxToStackTxMbps_Type())
npstatsStackRxToStackTxMbps.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackRxToStackTxMbps.setStatus(_A)
_NpstatsStackMaxRxToStackTxMbps_Type=Unsigned32
_NpstatsStackMaxRxToStackTxMbps_Object=MibScalar
npstatsStackMaxRxToStackTxMbps=_NpstatsStackMaxRxToStackTxMbps_Object((1,3,6,1,4,1,10734,3,3,2,10,11,6),_NpstatsStackMaxRxToStackTxMbps_Type())
npstatsStackMaxRxToStackTxMbps.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackMaxRxToStackTxMbps.setStatus(_A)
_NpstatsStackRxToSegmentTxMbps_Type=Unsigned32
_NpstatsStackRxToSegmentTxMbps_Object=MibScalar
npstatsStackRxToSegmentTxMbps=_NpstatsStackRxToSegmentTxMbps_Object((1,3,6,1,4,1,10734,3,3,2,10,11,7),_NpstatsStackRxToSegmentTxMbps_Type())
npstatsStackRxToSegmentTxMbps.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackRxToSegmentTxMbps.setStatus(_A)
_NpstatsStackMaxRxToSegmentTxMbps_Type=Unsigned32
_NpstatsStackMaxRxToSegmentTxMbps_Object=MibScalar
npstatsStackMaxRxToSegmentTxMbps=_NpstatsStackMaxRxToSegmentTxMbps_Object((1,3,6,1,4,1,10734,3,3,2,10,11,8),_NpstatsStackMaxRxToSegmentTxMbps_Type())
npstatsStackMaxRxToSegmentTxMbps.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackMaxRxToSegmentTxMbps.setStatus(_A)
_NpstatsStackRxToTier1_Type=Unsigned32
_NpstatsStackRxToTier1_Object=MibScalar
npstatsStackRxToTier1=_NpstatsStackRxToTier1_Object((1,3,6,1,4,1,10734,3,3,2,10,11,9),_NpstatsStackRxToTier1_Type())
npstatsStackRxToTier1.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackRxToTier1.setStatus(_A)
_NpstatsStackMaxRxToTier1_Type=Unsigned32
_NpstatsStackMaxRxToTier1_Object=MibScalar
npstatsStackMaxRxToTier1=_NpstatsStackMaxRxToTier1_Object((1,3,6,1,4,1,10734,3,3,2,10,11,10),_NpstatsStackMaxRxToTier1_Type())
npstatsStackMaxRxToTier1.setMaxAccess(_B)
if mibBuilder.loadTexts:npstatsStackMaxRxToTier1.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'tpt-npstats':tpt_npstats,'npstatsRulesTable':npstatsRulesTable,'npstatsRulesEntry':npstatsRulesEntry,_F:npstatsRulesRank,'npstatsRulesFilter':npstatsRulesFilter,'npstatsRulesFlows':npstatsRulesFlows,'npstatsRulesSuccess':npstatsRulesSuccess,'npstatsRulesTotalPercent':npstatsRulesTotalPercent,'npstatsRulesSuccessPer10K':npstatsRulesSuccessPer10K,'npstatsTiersTable':npstatsTiersTable,'npstatsTiersEntry':npstatsTiersEntry,_H:npstatsTierNumber,'npstatsTiersReceiveMbps':npstatsTiersReceiveMbps,'npstatsTiersTransmitMbps':npstatsTiersTransmitMbps,'npstatsTiersRxPktsPerSec':npstatsTiersRxPktsPerSec,'npstatsTiersMaxPktsPerSec':npstatsTiersMaxPktsPerSec,'npstatsTiersAvgBytesPerPkt':npstatsTiersAvgBytesPerPkt,'npstatsTiersUtilizationPercent':npstatsTiersUtilizationPercent,'npstatsTiersRatioToNextPer10K':npstatsTiersRatioToNextPer10K,'npstatsTiersMaxReceiveMbps':npstatsTiersMaxReceiveMbps,'npstatsTiersMaxTransmitMbps':npstatsTiersMaxTransmitMbps,'npstatsTiersMaxUtilizationPercent':npstatsTiersMaxUtilizationPercent,'npstatsTiersMaxRatioToNextPer10K':npstatsTiersMaxRatioToNextPer10K,'npstatsTiersExtra':npstatsTiersExtra,'npstatsTier1BypassMbps':npstatsTier1BypassMbps,'npstatsTier1Balance':npstatsTier1Balance,'npstatsTier1MaxPktsPerSecA':npstatsTier1MaxPktsPerSecA,'npstatsTier1MaxPktsPerSecB':npstatsTier1MaxPktsPerSecB,'npstatsTier4TriggerMatchPer1000':npstatsTier4TriggerMatchPer1000,'npstatsTier4ReroutePer1000':npstatsTier4ReroutePer1000,'npstatsTier4TcpSequencePer1000':npstatsTier4TcpSequencePer1000,'npstatsTier1TxPktsPerSec':npstatsTier1TxPktsPerSec,'npstatsTier1MaxTxPktsPerSec':npstatsTier1MaxTxPktsPerSec,'npstatsTier1MaxPktsPerSecC':npstatsTier1MaxPktsPerSecC,'npstatsTier4ProtoDcdPer1000':npstatsTier4ProtoDcdPer1000,'npstatsTier2TxTrustedPktsPerSec':npstatsTier2TxTrustedPktsPerSec,'npstatsTier3TxTrustedPktsPerSec':npstatsTier3TxTrustedPktsPerSec,'npstatsTier4TxTrustedPktsPerSec':npstatsTier4TxTrustedPktsPerSec,'npstatsTier1BypassPktsPerSec':npstatsTier1BypassPktsPerSec,'npstatsTier1MaxBypassPktsPerSec':npstatsTier1MaxBypassPktsPerSec,'npstatsTier1BypassToRxPktsPerSecRatio':npstatsTier1BypassToRxPktsPerSecRatio,'npstatsTier1VlanTransPktsPerSec':npstatsTier1VlanTransPktsPerSec,'npstatsTier1MaxVlanTransPktsPerSec':npstatsTier1MaxVlanTransPktsPerSec,'npstatsTier1VlanTransToRxPktsPerSecRatio':npstatsTier1VlanTransToRxPktsPerSecRatio,'npstatsTier1PatternMatchToRxPktsPerSecRatio':npstatsTier1PatternMatchToRxPktsPerSecRatio,'npstatsTier1MaxPatternMatchToRxPktsPerSecRatio':npstatsTier1MaxPatternMatchToRxPktsPerSecRatio,'npstatsTier2MaxTxTrustedPktsPerSec':npstatsTier2MaxTxTrustedPktsPerSec,'npstatsTier3MaxTxTrustedPktsPerSec':npstatsTier3MaxTxTrustedPktsPerSec,'npstatsTier4MaxTxTrustedPktsPerSec':npstatsTier4MaxTxTrustedPktsPerSec,'npstatsTier4MaxTriggerMatchPer1000':npstatsTier4MaxTriggerMatchPer1000,'npstatsTier4MaxReroutePer1000':npstatsTier4MaxReroutePer1000,'npstatsTier4MaxTcpSequencePer1000':npstatsTier4MaxTcpSequencePer1000,'npstatsTier4MaxProtoDcdPer1000':npstatsTier4MaxProtoDcdPer1000,'npstatsMisc':npstatsMisc,'npstatsMiscTxPktsBestEffort':npstatsMiscTxPktsBestEffort,'npstatsSslInsp':npstatsSslInsp,'npstatsSslInspCurrentSessions':npstatsSslInspCurrentSessions,'npstatsSslInspConnectionRate':npstatsSslInspConnectionRate,'npstatsSslInspBlockedMaxConns':npstatsSslInspBlockedMaxConns,'npstatsSslInspPassedMaxConns':npstatsSslInspPassedMaxConns,'npstatsSslInspTotalBytesIn':npstatsSslInspTotalBytesIn,'npstatsSslInspTotalBytesOut':npstatsSslInspTotalBytesOut,'npstatsStackSegmentPorts':npstatsStackSegmentPorts,'npstatsStackSegmentRecieveMbps':npstatsStackSegmentRecieveMbps,'npstatsStackSegmentMaxRecieveMbps':npstatsStackSegmentMaxRecieveMbps,'npstatsStackSegmentTransmitMbps':npstatsStackSegmentTransmitMbps,'npstatsStackSegmentMaxTransmitMbps':npstatsStackSegmentMaxTransmitMbps,'npstatsStackBalance':npstatsStackBalance,'npstatsStackMinBalance':npstatsStackMinBalance,'npstatsStackSegmentRatioToTier1Per10K':npstatsStackSegmentRatioToTier1Per10K,'npstatsStackSegmentMaxRatioToTier1Per10K':npstatsStackSegmentMaxRatioToTier1Per10K,'npstatsStackSegmentPortTable':npstatsStackSegmentPortTable,'npstatsStackSegmentPortEntry':npstatsStackSegmentPortEntry,_I:npstatsStackMemberIndex,'npstatsStackMemberKey':npstatsStackMemberKey,'npstatsStackMemberHostname':npstatsStackMemberHostname,'npstatsStackMemberSegmentReceiveMbps':npstatsStackMemberSegmentReceiveMbps,'npstatsStackMemberMaxSegmentReceiveMbps':npstatsStackMemberMaxSegmentReceiveMbps,'npstatsStackPorts':npstatsStackPorts,'npstatsStackPortsRecieveMbps':npstatsStackPortsRecieveMbps,'npstatsStackPortsMaxRecieveMbps':npstatsStackPortsMaxRecieveMbps,'npstatsStackPortsTransmitMbps':npstatsStackPortsTransmitMbps,'npstatsStackPortsMaxTransmitMbps':npstatsStackPortsMaxTransmitMbps,'npstatsStackRxToStackTxMbps':npstatsStackRxToStackTxMbps,'npstatsStackMaxRxToStackTxMbps':npstatsStackMaxRxToStackTxMbps,'npstatsStackRxToSegmentTxMbps':npstatsStackRxToSegmentTxMbps,'npstatsStackMaxRxToSegmentTxMbps':npstatsStackMaxRxToSegmentTxMbps,'npstatsStackRxToTier1':npstatsStackRxToTier1,'npstatsStackMaxRxToTier1':npstatsStackMaxRxToTier1})