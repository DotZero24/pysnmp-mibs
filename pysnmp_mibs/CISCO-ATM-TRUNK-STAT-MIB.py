_Ai='catsPvcStatGroupRev1'
_Ah='catsPvcStatGroup'
_Ag='catsPvcOamLpbkTimeoutThreshold'
_Af='catsPvcActiveOamLpbkTimeoutDur'
_Ae='catsPvcNewOamLpbkTimeoutDur'
_Ad='catsPvcOamLpbkTimeoutCnts'
_Ac='catsCidExtRAIXmtCnts'
_Ab='catsCidExtAISXmtCnts'
_Aa='catsCidExtConnRDICnts'
_AZ='catsCidExtConnAISCnts'
_AY='catsCidExtRAIRcvCnts'
_AX='catsCidExtAISRcvCnts'
_AW='catsCidExtConnRDIRcvdPkts'
_AV='catsCidExtConnAISRcvdPkts'
_AU='catsCidExtRAIRcvdPkts'
_AT='catsCidExtAISRcvdPkts'
_AS='catsCidRcvdPeakPkts'
_AR='catsCidSentPeakPkts'
_AQ='catsCidRcvdOctets'
_AP='catsCidSentOctets'
_AO='catsCidRcvdPkts'
_AN='catsCidSentPkts'
_AM='catsCidAvgRcvdPkts'
_AL='catsCidAvgSentPkts'
_AK='catsCidDiscontinuityTime'
_AJ='catsCidValidFlag'
_AI='catsAal5PvcReassemTimerExpiryPdus'
_AH='catsAal5PvcCrc32ErrorPdus'
_AG='catsAal5PvcInvLenPdus'
_AF='catsAal5PvcOverSizedSDUs'
_AE='catsAal5PvcInvCpiPdus'
_AD='catsAal5PvcPduRcvdPkts'
_AC='catsAal5PvcPduSentPkts'
_AB='catsAal5PvcDiscontinuityTime'
_AA='catsAal5PvcValidFlag'
_A9='catsAal2PvcCpsInvLenPkts'
_A8='catsAal2PvcCpsInvUuiPkts'
_A7='catsAal2PvcCpsInvCidPkts'
_A6='catsAal2PvcInvParCells'
_A5='catsAal2PvcInvOsfCells'
_A4='catsAal2PvcCrcErrors'
_A3='catsAal2PvcHecErrors'
_A2='catsAal2PvcCpsRcvdPkts'
_A1='catsAal2PvcCpsSentPkts'
_A0='catsAal2PvcDiscontinuityTime'
_z='catsAal2PvcValidFlag'
_y='deprecated'
_x='catsCidIntervalIndex'
_w='catsCid'
_v='catsCidVci'
_u='catsCidVpi'
_t='catsAal5PvcIntervalIndex'
_s='catsAal5PvcVci'
_r='catsAal5PvcVpi'
_q='catsAal2PvcIntervalIndex'
_p='catsAal2PvcVci'
_o='catsAal2PvcVpi'
_n='catsPvcIntervalIndex'
_m='catsPvcVci'
_l='catsPvcVpi'
_k='catsCidHistoryStatGroup'
_j='catsAal5PvcStatGroup'
_i='catsAal2PvcStatGroup'
_h='catsPvcRcvFerfCells'
_g='catsPvcXmtFerfCells'
_f='catsPvcRcvAisCells'
_e='catsPvcXmtAisCells'
_d='catsPvcRcvFerfCnts'
_c='catsPvcXmtFerfCnts'
_b='catsPvcRcvAisCnts'
_a='catsPvcXmtAisCnts'
_Z='catsPvcAisSuppressCnts'
_Y='catsPvcDiscardedRcvOamCells'
_X='catsPvcOamLpbkLostCells'
_W='catsPvcOamRcvSegLpbkCells'
_V='catsPvcOamXmtSegLpbkCells'
_U='catsPvcOamRcvEndLpbkCells'
_T='catsPvcOamXmtEndLpbkCells'
_S='catsPvcPeakAtmRcvCells'
_R='catsPvcPeakAtmXmtCells'
_Q='catsPvcAvgAtmRcvCells'
_P='catsPvcAvgAtmXmtCells'
_O='catsPvcAtmRcvCells'
_N='catsPvcAtmXmtCells'
_M='catsPvcDiscontinuityTime'
_L='catsPvcValidFlag'
_K='seconds'
_J='packets-per-sec'
_I='cells-per-sec'
_H='TimeStamp'
_G='ifIndex'
_F='IF-MIB'
_E='Unsigned32'
_D='not-accessible'
_C='read-only'
_B='current'
_A='CISCO-ATM-TRUNK-STAT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AtmVcIdentifier,AtmVpIdentifier=mibBuilder.importSymbols('ATM-TC-MIB','AtmVcIdentifier','AtmVpIdentifier')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_H,'TruthValue')
ciscoAtmTrunkStatMIB=ModuleIdentity((1,3,6,1,4,1,9,9,407))
if mibBuilder.loadTexts:ciscoAtmTrunkStatMIB.setRevisions(('2005-08-10 00:00','2004-05-12 00:00'))
_CiscoAtmTrunkStatNotifs_ObjectIdentity=ObjectIdentity
ciscoAtmTrunkStatNotifs=_CiscoAtmTrunkStatNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,407,0))
_CiscoAtmTrunkStatObjects_ObjectIdentity=ObjectIdentity
ciscoAtmTrunkStatObjects=_CiscoAtmTrunkStatObjects_ObjectIdentity((1,3,6,1,4,1,9,9,407,1))
_CatsStatistics_ObjectIdentity=ObjectIdentity
catsStatistics=_CatsStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,407,1,1))
_CatsPvcHistoryTable_Object=MibTable
catsPvcHistoryTable=_CatsPvcHistoryTable_Object((1,3,6,1,4,1,9,9,407,1,1,1))
if mibBuilder.loadTexts:catsPvcHistoryTable.setStatus(_B)
_CatsPvcHistoryEntry_Object=MibTableRow
catsPvcHistoryEntry=_CatsPvcHistoryEntry_Object((1,3,6,1,4,1,9,9,407,1,1,1,1))
catsPvcHistoryEntry.setIndexNames((0,_F,_G),(0,_A,_l),(0,_A,_m),(0,_A,_n))
if mibBuilder.loadTexts:catsPvcHistoryEntry.setStatus(_B)
_CatsPvcVpi_Type=AtmVpIdentifier
_CatsPvcVpi_Object=MibTableColumn
catsPvcVpi=_CatsPvcVpi_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,1),_CatsPvcVpi_Type())
catsPvcVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:catsPvcVpi.setStatus(_B)
_CatsPvcVci_Type=AtmVcIdentifier
_CatsPvcVci_Object=MibTableColumn
catsPvcVci=_CatsPvcVci_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,2),_CatsPvcVci_Type())
catsPvcVci.setMaxAccess(_D)
if mibBuilder.loadTexts:catsPvcVci.setStatus(_B)
class _CatsPvcIntervalIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_CatsPvcIntervalIndex_Type.__name__=_E
_CatsPvcIntervalIndex_Object=MibTableColumn
catsPvcIntervalIndex=_CatsPvcIntervalIndex_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,3),_CatsPvcIntervalIndex_Type())
catsPvcIntervalIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:catsPvcIntervalIndex.setStatus(_B)
_CatsPvcValidFlag_Type=TruthValue
_CatsPvcValidFlag_Object=MibTableColumn
catsPvcValidFlag=_CatsPvcValidFlag_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,4),_CatsPvcValidFlag_Type())
catsPvcValidFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcValidFlag.setStatus(_B)
class _CatsPvcDiscontinuityTime_Type(TimeStamp):defaultValue=0
_CatsPvcDiscontinuityTime_Type.__name__=_H
_CatsPvcDiscontinuityTime_Object=MibTableColumn
catsPvcDiscontinuityTime=_CatsPvcDiscontinuityTime_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,5),_CatsPvcDiscontinuityTime_Type())
catsPvcDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcDiscontinuityTime.setStatus(_B)
_CatsPvcAtmXmtCells_Type=Counter32
_CatsPvcAtmXmtCells_Object=MibTableColumn
catsPvcAtmXmtCells=_CatsPvcAtmXmtCells_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,6),_CatsPvcAtmXmtCells_Type())
catsPvcAtmXmtCells.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcAtmXmtCells.setStatus(_B)
_CatsPvcAtmRcvCells_Type=Counter32
_CatsPvcAtmRcvCells_Object=MibTableColumn
catsPvcAtmRcvCells=_CatsPvcAtmRcvCells_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,7),_CatsPvcAtmRcvCells_Type())
catsPvcAtmRcvCells.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcAtmRcvCells.setStatus(_B)
_CatsPvcAvgAtmXmtCells_Type=Counter32
_CatsPvcAvgAtmXmtCells_Object=MibTableColumn
catsPvcAvgAtmXmtCells=_CatsPvcAvgAtmXmtCells_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,8),_CatsPvcAvgAtmXmtCells_Type())
catsPvcAvgAtmXmtCells.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcAvgAtmXmtCells.setStatus(_B)
if mibBuilder.loadTexts:catsPvcAvgAtmXmtCells.setUnits(_I)
_CatsPvcAvgAtmRcvCells_Type=Counter32
_CatsPvcAvgAtmRcvCells_Object=MibTableColumn
catsPvcAvgAtmRcvCells=_CatsPvcAvgAtmRcvCells_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,9),_CatsPvcAvgAtmRcvCells_Type())
catsPvcAvgAtmRcvCells.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcAvgAtmRcvCells.setStatus(_B)
if mibBuilder.loadTexts:catsPvcAvgAtmRcvCells.setUnits(_I)
_CatsPvcPeakAtmXmtCells_Type=Counter32
_CatsPvcPeakAtmXmtCells_Object=MibTableColumn
catsPvcPeakAtmXmtCells=_CatsPvcPeakAtmXmtCells_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,10),_CatsPvcPeakAtmXmtCells_Type())
catsPvcPeakAtmXmtCells.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcPeakAtmXmtCells.setStatus(_B)
if mibBuilder.loadTexts:catsPvcPeakAtmXmtCells.setUnits(_I)
_CatsPvcPeakAtmRcvCells_Type=Counter32
_CatsPvcPeakAtmRcvCells_Object=MibTableColumn
catsPvcPeakAtmRcvCells=_CatsPvcPeakAtmRcvCells_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,11),_CatsPvcPeakAtmRcvCells_Type())
catsPvcPeakAtmRcvCells.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcPeakAtmRcvCells.setStatus(_B)
if mibBuilder.loadTexts:catsPvcPeakAtmRcvCells.setUnits(_I)
_CatsPvcOamXmtEndLpbkCells_Type=Counter32
_CatsPvcOamXmtEndLpbkCells_Object=MibTableColumn
catsPvcOamXmtEndLpbkCells=_CatsPvcOamXmtEndLpbkCells_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,12),_CatsPvcOamXmtEndLpbkCells_Type())
catsPvcOamXmtEndLpbkCells.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcOamXmtEndLpbkCells.setStatus(_B)
_CatsPvcOamRcvEndLpbkCells_Type=Counter32
_CatsPvcOamRcvEndLpbkCells_Object=MibTableColumn
catsPvcOamRcvEndLpbkCells=_CatsPvcOamRcvEndLpbkCells_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,13),_CatsPvcOamRcvEndLpbkCells_Type())
catsPvcOamRcvEndLpbkCells.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcOamRcvEndLpbkCells.setStatus(_B)
_CatsPvcOamXmtSegLpbkCells_Type=Counter32
_CatsPvcOamXmtSegLpbkCells_Object=MibTableColumn
catsPvcOamXmtSegLpbkCells=_CatsPvcOamXmtSegLpbkCells_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,14),_CatsPvcOamXmtSegLpbkCells_Type())
catsPvcOamXmtSegLpbkCells.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcOamXmtSegLpbkCells.setStatus(_B)
_CatsPvcOamRcvSegLpbkCells_Type=Counter32
_CatsPvcOamRcvSegLpbkCells_Object=MibTableColumn
catsPvcOamRcvSegLpbkCells=_CatsPvcOamRcvSegLpbkCells_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,15),_CatsPvcOamRcvSegLpbkCells_Type())
catsPvcOamRcvSegLpbkCells.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcOamRcvSegLpbkCells.setStatus(_B)
_CatsPvcOamLpbkLostCells_Type=Counter32
_CatsPvcOamLpbkLostCells_Object=MibTableColumn
catsPvcOamLpbkLostCells=_CatsPvcOamLpbkLostCells_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,16),_CatsPvcOamLpbkLostCells_Type())
catsPvcOamLpbkLostCells.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcOamLpbkLostCells.setStatus(_B)
_CatsPvcDiscardedRcvOamCells_Type=Counter32
_CatsPvcDiscardedRcvOamCells_Object=MibTableColumn
catsPvcDiscardedRcvOamCells=_CatsPvcDiscardedRcvOamCells_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,17),_CatsPvcDiscardedRcvOamCells_Type())
catsPvcDiscardedRcvOamCells.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcDiscardedRcvOamCells.setStatus(_B)
_CatsPvcAisSuppressCnts_Type=Counter32
_CatsPvcAisSuppressCnts_Object=MibTableColumn
catsPvcAisSuppressCnts=_CatsPvcAisSuppressCnts_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,18),_CatsPvcAisSuppressCnts_Type())
catsPvcAisSuppressCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcAisSuppressCnts.setStatus(_B)
_CatsPvcXmtAisCnts_Type=Counter32
_CatsPvcXmtAisCnts_Object=MibTableColumn
catsPvcXmtAisCnts=_CatsPvcXmtAisCnts_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,19),_CatsPvcXmtAisCnts_Type())
catsPvcXmtAisCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcXmtAisCnts.setStatus(_B)
_CatsPvcRcvAisCnts_Type=Counter32
_CatsPvcRcvAisCnts_Object=MibTableColumn
catsPvcRcvAisCnts=_CatsPvcRcvAisCnts_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,20),_CatsPvcRcvAisCnts_Type())
catsPvcRcvAisCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcRcvAisCnts.setStatus(_B)
_CatsPvcXmtFerfCnts_Type=Counter32
_CatsPvcXmtFerfCnts_Object=MibTableColumn
catsPvcXmtFerfCnts=_CatsPvcXmtFerfCnts_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,21),_CatsPvcXmtFerfCnts_Type())
catsPvcXmtFerfCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcXmtFerfCnts.setStatus(_B)
_CatsPvcRcvFerfCnts_Type=Counter32
_CatsPvcRcvFerfCnts_Object=MibTableColumn
catsPvcRcvFerfCnts=_CatsPvcRcvFerfCnts_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,22),_CatsPvcRcvFerfCnts_Type())
catsPvcRcvFerfCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcRcvFerfCnts.setStatus(_B)
_CatsPvcXmtAisCells_Type=Counter32
_CatsPvcXmtAisCells_Object=MibTableColumn
catsPvcXmtAisCells=_CatsPvcXmtAisCells_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,23),_CatsPvcXmtAisCells_Type())
catsPvcXmtAisCells.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcXmtAisCells.setStatus(_B)
_CatsPvcRcvAisCells_Type=Counter32
_CatsPvcRcvAisCells_Object=MibTableColumn
catsPvcRcvAisCells=_CatsPvcRcvAisCells_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,24),_CatsPvcRcvAisCells_Type())
catsPvcRcvAisCells.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcRcvAisCells.setStatus(_B)
_CatsPvcXmtFerfCells_Type=Counter32
_CatsPvcXmtFerfCells_Object=MibTableColumn
catsPvcXmtFerfCells=_CatsPvcXmtFerfCells_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,25),_CatsPvcXmtFerfCells_Type())
catsPvcXmtFerfCells.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcXmtFerfCells.setStatus(_B)
_CatsPvcRcvFerfCells_Type=Counter32
_CatsPvcRcvFerfCells_Object=MibTableColumn
catsPvcRcvFerfCells=_CatsPvcRcvFerfCells_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,26),_CatsPvcRcvFerfCells_Type())
catsPvcRcvFerfCells.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcRcvFerfCells.setStatus(_B)
_CatsPvcOamLpbkTimeoutCnts_Type=Counter32
_CatsPvcOamLpbkTimeoutCnts_Object=MibTableColumn
catsPvcOamLpbkTimeoutCnts=_CatsPvcOamLpbkTimeoutCnts_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,27),_CatsPvcOamLpbkTimeoutCnts_Type())
catsPvcOamLpbkTimeoutCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcOamLpbkTimeoutCnts.setStatus(_B)
_CatsPvcNewOamLpbkTimeoutDur_Type=Unsigned32
_CatsPvcNewOamLpbkTimeoutDur_Object=MibTableColumn
catsPvcNewOamLpbkTimeoutDur=_CatsPvcNewOamLpbkTimeoutDur_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,28),_CatsPvcNewOamLpbkTimeoutDur_Type())
catsPvcNewOamLpbkTimeoutDur.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcNewOamLpbkTimeoutDur.setStatus(_B)
if mibBuilder.loadTexts:catsPvcNewOamLpbkTimeoutDur.setUnits(_K)
_CatsPvcActiveOamLpbkTimeoutDur_Type=Unsigned32
_CatsPvcActiveOamLpbkTimeoutDur_Object=MibTableColumn
catsPvcActiveOamLpbkTimeoutDur=_CatsPvcActiveOamLpbkTimeoutDur_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,29),_CatsPvcActiveOamLpbkTimeoutDur_Type())
catsPvcActiveOamLpbkTimeoutDur.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcActiveOamLpbkTimeoutDur.setStatus(_B)
if mibBuilder.loadTexts:catsPvcActiveOamLpbkTimeoutDur.setUnits(_K)
class _CatsPvcOamLpbkTimeoutThreshold_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_CatsPvcOamLpbkTimeoutThreshold_Type.__name__=_E
_CatsPvcOamLpbkTimeoutThreshold_Object=MibTableColumn
catsPvcOamLpbkTimeoutThreshold=_CatsPvcOamLpbkTimeoutThreshold_Object((1,3,6,1,4,1,9,9,407,1,1,1,1,30),_CatsPvcOamLpbkTimeoutThreshold_Type())
catsPvcOamLpbkTimeoutThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:catsPvcOamLpbkTimeoutThreshold.setStatus(_B)
if mibBuilder.loadTexts:catsPvcOamLpbkTimeoutThreshold.setUnits(_K)
_CatsAal2PvcHistoryTable_Object=MibTable
catsAal2PvcHistoryTable=_CatsAal2PvcHistoryTable_Object((1,3,6,1,4,1,9,9,407,1,1,2))
if mibBuilder.loadTexts:catsAal2PvcHistoryTable.setStatus(_B)
_CatsAal2PvcHistoryEntry_Object=MibTableRow
catsAal2PvcHistoryEntry=_CatsAal2PvcHistoryEntry_Object((1,3,6,1,4,1,9,9,407,1,1,2,1))
catsAal2PvcHistoryEntry.setIndexNames((0,_F,_G),(0,_A,_o),(0,_A,_p),(0,_A,_q))
if mibBuilder.loadTexts:catsAal2PvcHistoryEntry.setStatus(_B)
_CatsAal2PvcVpi_Type=AtmVpIdentifier
_CatsAal2PvcVpi_Object=MibTableColumn
catsAal2PvcVpi=_CatsAal2PvcVpi_Object((1,3,6,1,4,1,9,9,407,1,1,2,1,1),_CatsAal2PvcVpi_Type())
catsAal2PvcVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:catsAal2PvcVpi.setStatus(_B)
_CatsAal2PvcVci_Type=AtmVcIdentifier
_CatsAal2PvcVci_Object=MibTableColumn
catsAal2PvcVci=_CatsAal2PvcVci_Object((1,3,6,1,4,1,9,9,407,1,1,2,1,2),_CatsAal2PvcVci_Type())
catsAal2PvcVci.setMaxAccess(_D)
if mibBuilder.loadTexts:catsAal2PvcVci.setStatus(_B)
class _CatsAal2PvcIntervalIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_CatsAal2PvcIntervalIndex_Type.__name__=_E
_CatsAal2PvcIntervalIndex_Object=MibTableColumn
catsAal2PvcIntervalIndex=_CatsAal2PvcIntervalIndex_Object((1,3,6,1,4,1,9,9,407,1,1,2,1,3),_CatsAal2PvcIntervalIndex_Type())
catsAal2PvcIntervalIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:catsAal2PvcIntervalIndex.setStatus(_B)
_CatsAal2PvcValidFlag_Type=TruthValue
_CatsAal2PvcValidFlag_Object=MibTableColumn
catsAal2PvcValidFlag=_CatsAal2PvcValidFlag_Object((1,3,6,1,4,1,9,9,407,1,1,2,1,4),_CatsAal2PvcValidFlag_Type())
catsAal2PvcValidFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:catsAal2PvcValidFlag.setStatus(_B)
class _CatsAal2PvcDiscontinuityTime_Type(TimeStamp):defaultValue=0
_CatsAal2PvcDiscontinuityTime_Type.__name__=_H
_CatsAal2PvcDiscontinuityTime_Object=MibTableColumn
catsAal2PvcDiscontinuityTime=_CatsAal2PvcDiscontinuityTime_Object((1,3,6,1,4,1,9,9,407,1,1,2,1,5),_CatsAal2PvcDiscontinuityTime_Type())
catsAal2PvcDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:catsAal2PvcDiscontinuityTime.setStatus(_B)
_CatsAal2PvcCpsSentPkts_Type=Counter32
_CatsAal2PvcCpsSentPkts_Object=MibTableColumn
catsAal2PvcCpsSentPkts=_CatsAal2PvcCpsSentPkts_Object((1,3,6,1,4,1,9,9,407,1,1,2,1,6),_CatsAal2PvcCpsSentPkts_Type())
catsAal2PvcCpsSentPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsAal2PvcCpsSentPkts.setStatus(_B)
_CatsAal2PvcCpsRcvdPkts_Type=Counter32
_CatsAal2PvcCpsRcvdPkts_Object=MibTableColumn
catsAal2PvcCpsRcvdPkts=_CatsAal2PvcCpsRcvdPkts_Object((1,3,6,1,4,1,9,9,407,1,1,2,1,7),_CatsAal2PvcCpsRcvdPkts_Type())
catsAal2PvcCpsRcvdPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsAal2PvcCpsRcvdPkts.setStatus(_B)
_CatsAal2PvcHecErrors_Type=Counter32
_CatsAal2PvcHecErrors_Object=MibTableColumn
catsAal2PvcHecErrors=_CatsAal2PvcHecErrors_Object((1,3,6,1,4,1,9,9,407,1,1,2,1,8),_CatsAal2PvcHecErrors_Type())
catsAal2PvcHecErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:catsAal2PvcHecErrors.setStatus(_B)
_CatsAal2PvcCrcErrors_Type=Counter32
_CatsAal2PvcCrcErrors_Object=MibTableColumn
catsAal2PvcCrcErrors=_CatsAal2PvcCrcErrors_Object((1,3,6,1,4,1,9,9,407,1,1,2,1,9),_CatsAal2PvcCrcErrors_Type())
catsAal2PvcCrcErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:catsAal2PvcCrcErrors.setStatus(_B)
_CatsAal2PvcInvOsfCells_Type=Counter32
_CatsAal2PvcInvOsfCells_Object=MibTableColumn
catsAal2PvcInvOsfCells=_CatsAal2PvcInvOsfCells_Object((1,3,6,1,4,1,9,9,407,1,1,2,1,10),_CatsAal2PvcInvOsfCells_Type())
catsAal2PvcInvOsfCells.setMaxAccess(_C)
if mibBuilder.loadTexts:catsAal2PvcInvOsfCells.setStatus(_B)
_CatsAal2PvcInvParCells_Type=Counter32
_CatsAal2PvcInvParCells_Object=MibTableColumn
catsAal2PvcInvParCells=_CatsAal2PvcInvParCells_Object((1,3,6,1,4,1,9,9,407,1,1,2,1,11),_CatsAal2PvcInvParCells_Type())
catsAal2PvcInvParCells.setMaxAccess(_C)
if mibBuilder.loadTexts:catsAal2PvcInvParCells.setStatus(_B)
_CatsAal2PvcCpsInvCidPkts_Type=Counter32
_CatsAal2PvcCpsInvCidPkts_Object=MibTableColumn
catsAal2PvcCpsInvCidPkts=_CatsAal2PvcCpsInvCidPkts_Object((1,3,6,1,4,1,9,9,407,1,1,2,1,12),_CatsAal2PvcCpsInvCidPkts_Type())
catsAal2PvcCpsInvCidPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsAal2PvcCpsInvCidPkts.setStatus(_B)
_CatsAal2PvcCpsInvUuiPkts_Type=Counter32
_CatsAal2PvcCpsInvUuiPkts_Object=MibTableColumn
catsAal2PvcCpsInvUuiPkts=_CatsAal2PvcCpsInvUuiPkts_Object((1,3,6,1,4,1,9,9,407,1,1,2,1,13),_CatsAal2PvcCpsInvUuiPkts_Type())
catsAal2PvcCpsInvUuiPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsAal2PvcCpsInvUuiPkts.setStatus(_B)
_CatsAal2PvcCpsInvLenPkts_Type=Counter32
_CatsAal2PvcCpsInvLenPkts_Object=MibTableColumn
catsAal2PvcCpsInvLenPkts=_CatsAal2PvcCpsInvLenPkts_Object((1,3,6,1,4,1,9,9,407,1,1,2,1,14),_CatsAal2PvcCpsInvLenPkts_Type())
catsAal2PvcCpsInvLenPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsAal2PvcCpsInvLenPkts.setStatus(_B)
_CatsAal5PvcHistoryTable_Object=MibTable
catsAal5PvcHistoryTable=_CatsAal5PvcHistoryTable_Object((1,3,6,1,4,1,9,9,407,1,1,3))
if mibBuilder.loadTexts:catsAal5PvcHistoryTable.setStatus(_B)
_CatsAal5PvcHistoryEntry_Object=MibTableRow
catsAal5PvcHistoryEntry=_CatsAal5PvcHistoryEntry_Object((1,3,6,1,4,1,9,9,407,1,1,3,1))
catsAal5PvcHistoryEntry.setIndexNames((0,_F,_G),(0,_A,_r),(0,_A,_s),(0,_A,_t))
if mibBuilder.loadTexts:catsAal5PvcHistoryEntry.setStatus(_B)
_CatsAal5PvcVpi_Type=AtmVpIdentifier
_CatsAal5PvcVpi_Object=MibTableColumn
catsAal5PvcVpi=_CatsAal5PvcVpi_Object((1,3,6,1,4,1,9,9,407,1,1,3,1,1),_CatsAal5PvcVpi_Type())
catsAal5PvcVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:catsAal5PvcVpi.setStatus(_B)
_CatsAal5PvcVci_Type=AtmVcIdentifier
_CatsAal5PvcVci_Object=MibTableColumn
catsAal5PvcVci=_CatsAal5PvcVci_Object((1,3,6,1,4,1,9,9,407,1,1,3,1,2),_CatsAal5PvcVci_Type())
catsAal5PvcVci.setMaxAccess(_D)
if mibBuilder.loadTexts:catsAal5PvcVci.setStatus(_B)
class _CatsAal5PvcIntervalIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_CatsAal5PvcIntervalIndex_Type.__name__=_E
_CatsAal5PvcIntervalIndex_Object=MibTableColumn
catsAal5PvcIntervalIndex=_CatsAal5PvcIntervalIndex_Object((1,3,6,1,4,1,9,9,407,1,1,3,1,3),_CatsAal5PvcIntervalIndex_Type())
catsAal5PvcIntervalIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:catsAal5PvcIntervalIndex.setStatus(_B)
_CatsAal5PvcValidFlag_Type=TruthValue
_CatsAal5PvcValidFlag_Object=MibTableColumn
catsAal5PvcValidFlag=_CatsAal5PvcValidFlag_Object((1,3,6,1,4,1,9,9,407,1,1,3,1,4),_CatsAal5PvcValidFlag_Type())
catsAal5PvcValidFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:catsAal5PvcValidFlag.setStatus(_B)
class _CatsAal5PvcDiscontinuityTime_Type(TimeStamp):defaultValue=0
_CatsAal5PvcDiscontinuityTime_Type.__name__=_H
_CatsAal5PvcDiscontinuityTime_Object=MibTableColumn
catsAal5PvcDiscontinuityTime=_CatsAal5PvcDiscontinuityTime_Object((1,3,6,1,4,1,9,9,407,1,1,3,1,5),_CatsAal5PvcDiscontinuityTime_Type())
catsAal5PvcDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:catsAal5PvcDiscontinuityTime.setStatus(_B)
_CatsAal5PvcPduSentPkts_Type=Counter32
_CatsAal5PvcPduSentPkts_Object=MibTableColumn
catsAal5PvcPduSentPkts=_CatsAal5PvcPduSentPkts_Object((1,3,6,1,4,1,9,9,407,1,1,3,1,6),_CatsAal5PvcPduSentPkts_Type())
catsAal5PvcPduSentPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsAal5PvcPduSentPkts.setStatus(_B)
_CatsAal5PvcPduRcvdPkts_Type=Counter32
_CatsAal5PvcPduRcvdPkts_Object=MibTableColumn
catsAal5PvcPduRcvdPkts=_CatsAal5PvcPduRcvdPkts_Object((1,3,6,1,4,1,9,9,407,1,1,3,1,7),_CatsAal5PvcPduRcvdPkts_Type())
catsAal5PvcPduRcvdPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsAal5PvcPduRcvdPkts.setStatus(_B)
_CatsAal5PvcInvCpiPdus_Type=Counter32
_CatsAal5PvcInvCpiPdus_Object=MibTableColumn
catsAal5PvcInvCpiPdus=_CatsAal5PvcInvCpiPdus_Object((1,3,6,1,4,1,9,9,407,1,1,3,1,8),_CatsAal5PvcInvCpiPdus_Type())
catsAal5PvcInvCpiPdus.setMaxAccess(_C)
if mibBuilder.loadTexts:catsAal5PvcInvCpiPdus.setStatus(_B)
_CatsAal5PvcOverSizedSDUs_Type=Counter32
_CatsAal5PvcOverSizedSDUs_Object=MibTableColumn
catsAal5PvcOverSizedSDUs=_CatsAal5PvcOverSizedSDUs_Object((1,3,6,1,4,1,9,9,407,1,1,3,1,9),_CatsAal5PvcOverSizedSDUs_Type())
catsAal5PvcOverSizedSDUs.setMaxAccess(_C)
if mibBuilder.loadTexts:catsAal5PvcOverSizedSDUs.setStatus(_B)
_CatsAal5PvcInvLenPdus_Type=Counter32
_CatsAal5PvcInvLenPdus_Object=MibTableColumn
catsAal5PvcInvLenPdus=_CatsAal5PvcInvLenPdus_Object((1,3,6,1,4,1,9,9,407,1,1,3,1,10),_CatsAal5PvcInvLenPdus_Type())
catsAal5PvcInvLenPdus.setMaxAccess(_C)
if mibBuilder.loadTexts:catsAal5PvcInvLenPdus.setStatus(_B)
_CatsAal5PvcCrc32ErrorPdus_Type=Counter32
_CatsAal5PvcCrc32ErrorPdus_Object=MibTableColumn
catsAal5PvcCrc32ErrorPdus=_CatsAal5PvcCrc32ErrorPdus_Object((1,3,6,1,4,1,9,9,407,1,1,3,1,11),_CatsAal5PvcCrc32ErrorPdus_Type())
catsAal5PvcCrc32ErrorPdus.setMaxAccess(_C)
if mibBuilder.loadTexts:catsAal5PvcCrc32ErrorPdus.setStatus(_B)
_CatsAal5PvcReassemTimerExpiryPdus_Type=Counter32
_CatsAal5PvcReassemTimerExpiryPdus_Object=MibTableColumn
catsAal5PvcReassemTimerExpiryPdus=_CatsAal5PvcReassemTimerExpiryPdus_Object((1,3,6,1,4,1,9,9,407,1,1,3,1,12),_CatsAal5PvcReassemTimerExpiryPdus_Type())
catsAal5PvcReassemTimerExpiryPdus.setMaxAccess(_C)
if mibBuilder.loadTexts:catsAal5PvcReassemTimerExpiryPdus.setStatus(_B)
_CatsCidHistoryTable_Object=MibTable
catsCidHistoryTable=_CatsCidHistoryTable_Object((1,3,6,1,4,1,9,9,407,1,1,4))
if mibBuilder.loadTexts:catsCidHistoryTable.setStatus(_B)
_CatsCidHistoryEntry_Object=MibTableRow
catsCidHistoryEntry=_CatsCidHistoryEntry_Object((1,3,6,1,4,1,9,9,407,1,1,4,1))
catsCidHistoryEntry.setIndexNames((0,_F,_G),(0,_A,_u),(0,_A,_v),(0,_A,_w),(0,_A,_x))
if mibBuilder.loadTexts:catsCidHistoryEntry.setStatus(_B)
_CatsCidVpi_Type=AtmVpIdentifier
_CatsCidVpi_Object=MibTableColumn
catsCidVpi=_CatsCidVpi_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,1),_CatsCidVpi_Type())
catsCidVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:catsCidVpi.setStatus(_B)
_CatsCidVci_Type=AtmVcIdentifier
_CatsCidVci_Object=MibTableColumn
catsCidVci=_CatsCidVci_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,2),_CatsCidVci_Type())
catsCidVci.setMaxAccess(_D)
if mibBuilder.loadTexts:catsCidVci.setStatus(_B)
class _CatsCid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CatsCid_Type.__name__=_E
_CatsCid_Object=MibTableColumn
catsCid=_CatsCid_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,3),_CatsCid_Type())
catsCid.setMaxAccess(_D)
if mibBuilder.loadTexts:catsCid.setStatus(_B)
class _CatsCidIntervalIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_CatsCidIntervalIndex_Type.__name__=_E
_CatsCidIntervalIndex_Object=MibTableColumn
catsCidIntervalIndex=_CatsCidIntervalIndex_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,4),_CatsCidIntervalIndex_Type())
catsCidIntervalIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:catsCidIntervalIndex.setStatus(_B)
_CatsCidValidFlag_Type=TruthValue
_CatsCidValidFlag_Object=MibTableColumn
catsCidValidFlag=_CatsCidValidFlag_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,5),_CatsCidValidFlag_Type())
catsCidValidFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:catsCidValidFlag.setStatus(_B)
class _CatsCidDiscontinuityTime_Type(TimeStamp):defaultValue=0
_CatsCidDiscontinuityTime_Type.__name__=_H
_CatsCidDiscontinuityTime_Object=MibTableColumn
catsCidDiscontinuityTime=_CatsCidDiscontinuityTime_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,6),_CatsCidDiscontinuityTime_Type())
catsCidDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:catsCidDiscontinuityTime.setStatus(_B)
_CatsCidAvgSentPkts_Type=Counter32
_CatsCidAvgSentPkts_Object=MibTableColumn
catsCidAvgSentPkts=_CatsCidAvgSentPkts_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,7),_CatsCidAvgSentPkts_Type())
catsCidAvgSentPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsCidAvgSentPkts.setStatus(_B)
if mibBuilder.loadTexts:catsCidAvgSentPkts.setUnits(_J)
_CatsCidAvgRcvdPkts_Type=Counter32
_CatsCidAvgRcvdPkts_Object=MibTableColumn
catsCidAvgRcvdPkts=_CatsCidAvgRcvdPkts_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,8),_CatsCidAvgRcvdPkts_Type())
catsCidAvgRcvdPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsCidAvgRcvdPkts.setStatus(_B)
if mibBuilder.loadTexts:catsCidAvgRcvdPkts.setUnits(_J)
_CatsCidSentPkts_Type=Counter32
_CatsCidSentPkts_Object=MibTableColumn
catsCidSentPkts=_CatsCidSentPkts_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,9),_CatsCidSentPkts_Type())
catsCidSentPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsCidSentPkts.setStatus(_B)
_CatsCidRcvdPkts_Type=Counter32
_CatsCidRcvdPkts_Object=MibTableColumn
catsCidRcvdPkts=_CatsCidRcvdPkts_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,10),_CatsCidRcvdPkts_Type())
catsCidRcvdPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsCidRcvdPkts.setStatus(_B)
_CatsCidSentOctets_Type=Counter32
_CatsCidSentOctets_Object=MibTableColumn
catsCidSentOctets=_CatsCidSentOctets_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,11),_CatsCidSentOctets_Type())
catsCidSentOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:catsCidSentOctets.setStatus(_B)
_CatsCidRcvdOctets_Type=Counter32
_CatsCidRcvdOctets_Object=MibTableColumn
catsCidRcvdOctets=_CatsCidRcvdOctets_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,12),_CatsCidRcvdOctets_Type())
catsCidRcvdOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:catsCidRcvdOctets.setStatus(_B)
_CatsCidSentPeakPkts_Type=Counter32
_CatsCidSentPeakPkts_Object=MibTableColumn
catsCidSentPeakPkts=_CatsCidSentPeakPkts_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,13),_CatsCidSentPeakPkts_Type())
catsCidSentPeakPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsCidSentPeakPkts.setStatus(_B)
if mibBuilder.loadTexts:catsCidSentPeakPkts.setUnits(_J)
_CatsCidRcvdPeakPkts_Type=Counter32
_CatsCidRcvdPeakPkts_Object=MibTableColumn
catsCidRcvdPeakPkts=_CatsCidRcvdPeakPkts_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,14),_CatsCidRcvdPeakPkts_Type())
catsCidRcvdPeakPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsCidRcvdPeakPkts.setStatus(_B)
if mibBuilder.loadTexts:catsCidRcvdPeakPkts.setUnits(_J)
_CatsCidExtAISRcvdPkts_Type=Counter32
_CatsCidExtAISRcvdPkts_Object=MibTableColumn
catsCidExtAISRcvdPkts=_CatsCidExtAISRcvdPkts_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,15),_CatsCidExtAISRcvdPkts_Type())
catsCidExtAISRcvdPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsCidExtAISRcvdPkts.setStatus(_B)
_CatsCidExtRAIRcvdPkts_Type=Counter32
_CatsCidExtRAIRcvdPkts_Object=MibTableColumn
catsCidExtRAIRcvdPkts=_CatsCidExtRAIRcvdPkts_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,16),_CatsCidExtRAIRcvdPkts_Type())
catsCidExtRAIRcvdPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsCidExtRAIRcvdPkts.setStatus(_B)
_CatsCidExtConnAISRcvdPkts_Type=Counter32
_CatsCidExtConnAISRcvdPkts_Object=MibTableColumn
catsCidExtConnAISRcvdPkts=_CatsCidExtConnAISRcvdPkts_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,17),_CatsCidExtConnAISRcvdPkts_Type())
catsCidExtConnAISRcvdPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsCidExtConnAISRcvdPkts.setStatus(_B)
_CatsCidExtConnRDIRcvdPkts_Type=Counter32
_CatsCidExtConnRDIRcvdPkts_Object=MibTableColumn
catsCidExtConnRDIRcvdPkts=_CatsCidExtConnRDIRcvdPkts_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,18),_CatsCidExtConnRDIRcvdPkts_Type())
catsCidExtConnRDIRcvdPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsCidExtConnRDIRcvdPkts.setStatus(_B)
_CatsCidExtAISRcvCnts_Type=Counter32
_CatsCidExtAISRcvCnts_Object=MibTableColumn
catsCidExtAISRcvCnts=_CatsCidExtAISRcvCnts_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,19),_CatsCidExtAISRcvCnts_Type())
catsCidExtAISRcvCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsCidExtAISRcvCnts.setStatus(_B)
_CatsCidExtRAIRcvCnts_Type=Counter32
_CatsCidExtRAIRcvCnts_Object=MibTableColumn
catsCidExtRAIRcvCnts=_CatsCidExtRAIRcvCnts_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,20),_CatsCidExtRAIRcvCnts_Type())
catsCidExtRAIRcvCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsCidExtRAIRcvCnts.setStatus(_B)
_CatsCidExtConnAISCnts_Type=Counter32
_CatsCidExtConnAISCnts_Object=MibTableColumn
catsCidExtConnAISCnts=_CatsCidExtConnAISCnts_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,21),_CatsCidExtConnAISCnts_Type())
catsCidExtConnAISCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsCidExtConnAISCnts.setStatus(_B)
_CatsCidExtConnRDICnts_Type=Counter32
_CatsCidExtConnRDICnts_Object=MibTableColumn
catsCidExtConnRDICnts=_CatsCidExtConnRDICnts_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,22),_CatsCidExtConnRDICnts_Type())
catsCidExtConnRDICnts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsCidExtConnRDICnts.setStatus(_B)
_CatsCidExtAISXmtCnts_Type=Counter32
_CatsCidExtAISXmtCnts_Object=MibTableColumn
catsCidExtAISXmtCnts=_CatsCidExtAISXmtCnts_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,23),_CatsCidExtAISXmtCnts_Type())
catsCidExtAISXmtCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsCidExtAISXmtCnts.setStatus(_B)
_CatsCidExtRAIXmtCnts_Type=Counter32
_CatsCidExtRAIXmtCnts_Object=MibTableColumn
catsCidExtRAIXmtCnts=_CatsCidExtRAIXmtCnts_Object((1,3,6,1,4,1,9,9,407,1,1,4,1,24),_CatsCidExtRAIXmtCnts_Type())
catsCidExtRAIXmtCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:catsCidExtRAIXmtCnts.setStatus(_B)
_CatsMIBConformance_ObjectIdentity=ObjectIdentity
catsMIBConformance=_CatsMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,407,2))
_CatsMIBGroups_ObjectIdentity=ObjectIdentity
catsMIBGroups=_CatsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,407,2,1))
_CatsMIBCompliances_ObjectIdentity=ObjectIdentity
catsMIBCompliances=_CatsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,407,2,2))
catsPvcStatGroup=ObjectGroup((1,3,6,1,4,1,9,9,407,2,1,1))
catsPvcStatGroup.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:catsPvcStatGroup.setStatus(_y)
catsAal2PvcStatGroup=ObjectGroup((1,3,6,1,4,1,9,9,407,2,1,2))
catsAal2PvcStatGroup.setObjects(*((_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:catsAal2PvcStatGroup.setStatus(_B)
catsAal5PvcStatGroup=ObjectGroup((1,3,6,1,4,1,9,9,407,2,1,3))
catsAal5PvcStatGroup.setObjects(*((_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:catsAal5PvcStatGroup.setStatus(_B)
catsCidHistoryStatGroup=ObjectGroup((1,3,6,1,4,1,9,9,407,2,1,4))
catsCidHistoryStatGroup.setObjects(*((_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac)))
if mibBuilder.loadTexts:catsCidHistoryStatGroup.setStatus(_B)
catsPvcStatGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,407,2,1,5))
catsPvcStatGroupRev1.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag)))
if mibBuilder.loadTexts:catsPvcStatGroupRev1.setStatus(_B)
ciscoAtmPvcStatMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,407,2,2,1))
ciscoAtmPvcStatMIBCompliance.setObjects(*((_A,_Ah),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:ciscoAtmPvcStatMIBCompliance.setStatus(_y)
ciscoAtmPvcStatMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,407,2,2,2))
ciscoAtmPvcStatMIBComplianceRev1.setObjects(*((_A,_Ai),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:ciscoAtmPvcStatMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoAtmTrunkStatMIB':ciscoAtmTrunkStatMIB,'ciscoAtmTrunkStatNotifs':ciscoAtmTrunkStatNotifs,'ciscoAtmTrunkStatObjects':ciscoAtmTrunkStatObjects,'catsStatistics':catsStatistics,'catsPvcHistoryTable':catsPvcHistoryTable,'catsPvcHistoryEntry':catsPvcHistoryEntry,_l:catsPvcVpi,_m:catsPvcVci,_n:catsPvcIntervalIndex,_L:catsPvcValidFlag,_M:catsPvcDiscontinuityTime,_N:catsPvcAtmXmtCells,_O:catsPvcAtmRcvCells,_P:catsPvcAvgAtmXmtCells,_Q:catsPvcAvgAtmRcvCells,_R:catsPvcPeakAtmXmtCells,_S:catsPvcPeakAtmRcvCells,_T:catsPvcOamXmtEndLpbkCells,_U:catsPvcOamRcvEndLpbkCells,_V:catsPvcOamXmtSegLpbkCells,_W:catsPvcOamRcvSegLpbkCells,_X:catsPvcOamLpbkLostCells,_Y:catsPvcDiscardedRcvOamCells,_Z:catsPvcAisSuppressCnts,_a:catsPvcXmtAisCnts,_b:catsPvcRcvAisCnts,_c:catsPvcXmtFerfCnts,_d:catsPvcRcvFerfCnts,_e:catsPvcXmtAisCells,_f:catsPvcRcvAisCells,_g:catsPvcXmtFerfCells,_h:catsPvcRcvFerfCells,_Ad:catsPvcOamLpbkTimeoutCnts,_Ae:catsPvcNewOamLpbkTimeoutDur,_Af:catsPvcActiveOamLpbkTimeoutDur,_Ag:catsPvcOamLpbkTimeoutThreshold,'catsAal2PvcHistoryTable':catsAal2PvcHistoryTable,'catsAal2PvcHistoryEntry':catsAal2PvcHistoryEntry,_o:catsAal2PvcVpi,_p:catsAal2PvcVci,_q:catsAal2PvcIntervalIndex,_z:catsAal2PvcValidFlag,_A0:catsAal2PvcDiscontinuityTime,_A1:catsAal2PvcCpsSentPkts,_A2:catsAal2PvcCpsRcvdPkts,_A3:catsAal2PvcHecErrors,_A4:catsAal2PvcCrcErrors,_A5:catsAal2PvcInvOsfCells,_A6:catsAal2PvcInvParCells,_A7:catsAal2PvcCpsInvCidPkts,_A8:catsAal2PvcCpsInvUuiPkts,_A9:catsAal2PvcCpsInvLenPkts,'catsAal5PvcHistoryTable':catsAal5PvcHistoryTable,'catsAal5PvcHistoryEntry':catsAal5PvcHistoryEntry,_r:catsAal5PvcVpi,_s:catsAal5PvcVci,_t:catsAal5PvcIntervalIndex,_AA:catsAal5PvcValidFlag,_AB:catsAal5PvcDiscontinuityTime,_AC:catsAal5PvcPduSentPkts,_AD:catsAal5PvcPduRcvdPkts,_AE:catsAal5PvcInvCpiPdus,_AF:catsAal5PvcOverSizedSDUs,_AG:catsAal5PvcInvLenPdus,_AH:catsAal5PvcCrc32ErrorPdus,_AI:catsAal5PvcReassemTimerExpiryPdus,'catsCidHistoryTable':catsCidHistoryTable,'catsCidHistoryEntry':catsCidHistoryEntry,_u:catsCidVpi,_v:catsCidVci,_w:catsCid,_x:catsCidIntervalIndex,_AJ:catsCidValidFlag,_AK:catsCidDiscontinuityTime,_AL:catsCidAvgSentPkts,_AM:catsCidAvgRcvdPkts,_AN:catsCidSentPkts,_AO:catsCidRcvdPkts,_AP:catsCidSentOctets,_AQ:catsCidRcvdOctets,_AR:catsCidSentPeakPkts,_AS:catsCidRcvdPeakPkts,_AT:catsCidExtAISRcvdPkts,_AU:catsCidExtRAIRcvdPkts,_AV:catsCidExtConnAISRcvdPkts,_AW:catsCidExtConnRDIRcvdPkts,_AX:catsCidExtAISRcvCnts,_AY:catsCidExtRAIRcvCnts,_AZ:catsCidExtConnAISCnts,_Aa:catsCidExtConnRDICnts,_Ab:catsCidExtAISXmtCnts,_Ac:catsCidExtRAIXmtCnts,'catsMIBConformance':catsMIBConformance,'catsMIBGroups':catsMIBGroups,_Ah:catsPvcStatGroup,_i:catsAal2PvcStatGroup,_j:catsAal5PvcStatGroup,_k:catsCidHistoryStatGroup,_Ai:catsPvcStatGroupRev1,'catsMIBCompliances':catsMIBCompliances,'ciscoAtmPvcStatMIBCompliance':ciscoAtmPvcStatMIBCompliance,'ciscoAtmPvcStatMIBComplianceRev1':ciscoAtmPvcStatMIBComplianceRev1})