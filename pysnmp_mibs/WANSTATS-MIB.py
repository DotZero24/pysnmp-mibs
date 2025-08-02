_r='wanAal5PvcHistorySampleIndex'
_q='wanAal5PvcHistoryIndex'
_p='wanFrPvcHistorySampleIndex'
_o='wanFrPvcHistoryIndex'
_n='wanX25PvcHistorySampleIndex'
_m='wanX25PvcHistoryIndex'
_l='wanPppHistorySampleIndex'
_k='wanPppHistoryIndex'
_j='wanAal5HistorySampleIndex'
_i='wanAal5HistoryIndex'
_h='wanFrHistorySampleIndex'
_g='wanFrHistoryIndex'
_f='wanX25HistorySampleIndex'
_e='wanX25HistoryIndex'
_d='wanAtmHistorySampleIndex'
_c='wanAtmHistoryIndex'
_b='wanT3E3HistorySampleIndex'
_a='wanT3E3HistoryIndex'
_Z='wanHssiHistorySampleIndex'
_Y='wanHssiHistoryIndex'
_X='wanVSeriesHistorySampleIndex'
_W='wanVSeriesHistoryIndex'
_V='wanT1E1HistorySampleIndex'
_U='wanT1E1HistoryIndex'
_T='wanAal5PvcStatsIndex'
_S='wanFrPvcStatsIndex'
_R='wanPppStatsIndex'
_Q='wanAal5StatsIndex'
_P='wanFrStatsIndex'
_O='wanAtmStatsIndex'
_N='wanT3E3StatsIndex'
_M='wanHssiStatsIndex'
_L='wanVSeriesStatsIndex'
_K='wanT1E1StatsIndex'
_J='unknown'
_I='down'
_H='wanX25StatsIndex'
_G='read-create'
_F='not-accessible'
_E='WANSTATS-MIB'
_D='deprecated'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
OwnerString,=mibBuilder.importSymbols('RMON-MIB','OwnerString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
wanStatsMIB=ModuleIdentity((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8))
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_System_ObjectIdentity=ObjectIdentity
system=_System_ObjectIdentity((1,3,6,1,4,1,11,2,3))
_NetElement_ObjectIdentity=ObjectIdentity
netElement=_NetElement_ObjectIdentity((1,3,6,1,4,1,11,2,3,7))
_Lanprobe_ObjectIdentity=ObjectIdentity
lanprobe=_Lanprobe_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,6))
_General_ObjectIdentity=ObjectIdentity
general=_General_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,6,1))
_RmonExtension_ObjectIdentity=ObjectIdentity
rmonExtension=_RmonExtension_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,6,1,5))
_StatsExtension_ObjectIdentity=ObjectIdentity
statsExtension=_StatsExtension_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,6,1,5,1))
_WanStatsMIBObjects_ObjectIdentity=ObjectIdentity
wanStatsMIBObjects=_WanStatsMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1))
_WanSignalingStats_ObjectIdentity=ObjectIdentity
wanSignalingStats=_WanSignalingStats_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1))
_WanT1E1StatsTable_Object=MibTable
wanT1E1StatsTable=_WanT1E1StatsTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1))
if mibBuilder.loadTexts:wanT1E1StatsTable.setStatus(_A)
_WanT1E1StatsEntry_Object=MibTableRow
wanT1E1StatsEntry=_WanT1E1StatsEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1))
wanT1E1StatsEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:wanT1E1StatsEntry.setStatus(_A)
class _WanT1E1StatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanT1E1StatsIndex_Type.__name__=_C
_WanT1E1StatsIndex_Object=MibTableColumn
wanT1E1StatsIndex=_WanT1E1StatsIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,1),_WanT1E1StatsIndex_Type())
wanT1E1StatsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanT1E1StatsIndex.setStatus(_A)
_WanT1E1StatsDataSource_Type=ObjectIdentifier
_WanT1E1StatsDataSource_Object=MibTableColumn
wanT1E1StatsDataSource=_WanT1E1StatsDataSource_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,2),_WanT1E1StatsDataSource_Type())
wanT1E1StatsDataSource.setMaxAccess(_G)
if mibBuilder.loadTexts:wanT1E1StatsDataSource.setStatus(_A)
_WanT1E1StatsDropEvents_Type=Counter64
_WanT1E1StatsDropEvents_Object=MibTableColumn
wanT1E1StatsDropEvents=_WanT1E1StatsDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,3),_WanT1E1StatsDropEvents_Type())
wanT1E1StatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsDropEvents.setStatus(_A)
_WanT1E1StatsInFrames_Type=Counter64
_WanT1E1StatsInFrames_Object=MibTableColumn
wanT1E1StatsInFrames=_WanT1E1StatsInFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,4),_WanT1E1StatsInFrames_Type())
wanT1E1StatsInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsInFrames.setStatus(_A)
_WanT1E1StatsOutFrames_Type=Counter64
_WanT1E1StatsOutFrames_Object=MibTableColumn
wanT1E1StatsOutFrames=_WanT1E1StatsOutFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,5),_WanT1E1StatsOutFrames_Type())
wanT1E1StatsOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsOutFrames.setStatus(_A)
_WanT1E1StatsInOctets_Type=Counter64
_WanT1E1StatsInOctets_Object=MibTableColumn
wanT1E1StatsInOctets=_WanT1E1StatsInOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,6),_WanT1E1StatsInOctets_Type())
wanT1E1StatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsInOctets.setStatus(_A)
_WanT1E1StatsOutOctets_Type=Counter64
_WanT1E1StatsOutOctets_Object=MibTableColumn
wanT1E1StatsOutOctets=_WanT1E1StatsOutOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,7),_WanT1E1StatsOutOctets_Type())
wanT1E1StatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsOutOctets.setStatus(_A)
_WanT1E1StatsESs_Type=Counter64
_WanT1E1StatsESs_Object=MibTableColumn
wanT1E1StatsESs=_WanT1E1StatsESs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,8),_WanT1E1StatsESs_Type())
wanT1E1StatsESs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsESs.setStatus(_A)
_WanT1E1StatsSESs_Type=Counter64
_WanT1E1StatsSESs_Object=MibTableColumn
wanT1E1StatsSESs=_WanT1E1StatsSESs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,9),_WanT1E1StatsSESs_Type())
wanT1E1StatsSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsSESs.setStatus(_A)
_WanT1E1StatsSEFSs_Type=Counter64
_WanT1E1StatsSEFSs_Object=MibTableColumn
wanT1E1StatsSEFSs=_WanT1E1StatsSEFSs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,10),_WanT1E1StatsSEFSs_Type())
wanT1E1StatsSEFSs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsSEFSs.setStatus(_A)
_WanT1E1StatsOOFs_Type=Counter64
_WanT1E1StatsOOFs_Object=MibTableColumn
wanT1E1StatsOOFs=_WanT1E1StatsOOFs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,11),_WanT1E1StatsOOFs_Type())
wanT1E1StatsOOFs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsOOFs.setStatus(_A)
_WanT1E1StatsUASs_Type=Counter64
_WanT1E1StatsUASs_Object=MibTableColumn
wanT1E1StatsUASs=_WanT1E1StatsUASs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,12),_WanT1E1StatsUASs_Type())
wanT1E1StatsUASs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsUASs.setStatus(_A)
_WanT1E1StatsCSSs_Type=Counter64
_WanT1E1StatsCSSs_Object=MibTableColumn
wanT1E1StatsCSSs=_WanT1E1StatsCSSs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,13),_WanT1E1StatsCSSs_Type())
wanT1E1StatsCSSs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsCSSs.setStatus(_A)
_WanT1E1StatsPCVs_Type=Counter64
_WanT1E1StatsPCVs_Object=MibTableColumn
wanT1E1StatsPCVs=_WanT1E1StatsPCVs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,14),_WanT1E1StatsPCVs_Type())
wanT1E1StatsPCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsPCVs.setStatus(_A)
_WanT1E1StatsLESs_Type=Counter64
_WanT1E1StatsLESs_Object=MibTableColumn
wanT1E1StatsLESs=_WanT1E1StatsLESs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,15),_WanT1E1StatsLESs_Type())
wanT1E1StatsLESs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsLESs.setStatus(_A)
_WanT1E1StatsBESs_Type=Counter64
_WanT1E1StatsBESs_Object=MibTableColumn
wanT1E1StatsBESs=_WanT1E1StatsBESs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,16),_WanT1E1StatsBESs_Type())
wanT1E1StatsBESs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsBESs.setStatus(_A)
_WanT1E1StatsDMs_Type=Counter64
_WanT1E1StatsDMs_Object=MibTableColumn
wanT1E1StatsDMs=_WanT1E1StatsDMs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,17),_WanT1E1StatsDMs_Type())
wanT1E1StatsDMs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsDMs.setStatus(_A)
_WanT1E1StatsLCVs_Type=Counter64
_WanT1E1StatsLCVs_Object=MibTableColumn
wanT1E1StatsLCVs=_WanT1E1StatsLCVs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,18),_WanT1E1StatsLCVs_Type())
wanT1E1StatsLCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsLCVs.setStatus(_A)
_WanT1E1StatsLOFs_Type=Counter64
_WanT1E1StatsLOFs_Object=MibTableColumn
wanT1E1StatsLOFs=_WanT1E1StatsLOFs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,19),_WanT1E1StatsLOFs_Type())
wanT1E1StatsLOFs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsLOFs.setStatus(_A)
_WanT1E1StatsLOSs_Type=Counter64
_WanT1E1StatsLOSs_Object=MibTableColumn
wanT1E1StatsLOSs=_WanT1E1StatsLOSs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,20),_WanT1E1StatsLOSs_Type())
wanT1E1StatsLOSs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsLOSs.setStatus(_A)
_WanT1E1StatsRAIs_Type=Counter64
_WanT1E1StatsRAIs_Object=MibTableColumn
wanT1E1StatsRAIs=_WanT1E1StatsRAIs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,21),_WanT1E1StatsRAIs_Type())
wanT1E1StatsRAIs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsRAIs.setStatus(_A)
_WanT1E1StatsAISs_Type=Counter64
_WanT1E1StatsAISs_Object=MibTableColumn
wanT1E1StatsAISs=_WanT1E1StatsAISs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,22),_WanT1E1StatsAISs_Type())
wanT1E1StatsAISs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsAISs.setStatus(_A)
_WanT1E1StatsTS16AISs_Type=Counter64
_WanT1E1StatsTS16AISs_Object=MibTableColumn
wanT1E1StatsTS16AISs=_WanT1E1StatsTS16AISs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,23),_WanT1E1StatsTS16AISs_Type())
wanT1E1StatsTS16AISs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsTS16AISs.setStatus(_A)
_WanT1E1StatsLOMFs_Type=Counter64
_WanT1E1StatsLOMFs_Object=MibTableColumn
wanT1E1StatsLOMFs=_WanT1E1StatsLOMFs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,24),_WanT1E1StatsLOMFs_Type())
wanT1E1StatsLOMFs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsLOMFs.setStatus(_A)
_WanT1E1StatsFarLOMFs_Type=Counter64
_WanT1E1StatsFarLOMFs_Object=MibTableColumn
wanT1E1StatsFarLOMFs=_WanT1E1StatsFarLOMFs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,25),_WanT1E1StatsFarLOMFs_Type())
wanT1E1StatsFarLOMFs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1StatsFarLOMFs.setStatus(_A)
_WanT1E1StatsOwner_Type=OwnerString
_WanT1E1StatsOwner_Object=MibTableColumn
wanT1E1StatsOwner=_WanT1E1StatsOwner_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,26),_WanT1E1StatsOwner_Type())
wanT1E1StatsOwner.setMaxAccess(_G)
if mibBuilder.loadTexts:wanT1E1StatsOwner.setStatus(_A)
_WanT1E1StatsStatus_Type=RowStatus
_WanT1E1StatsStatus_Object=MibTableColumn
wanT1E1StatsStatus=_WanT1E1StatsStatus_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,1,1,27),_WanT1E1StatsStatus_Type())
wanT1E1StatsStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wanT1E1StatsStatus.setStatus(_A)
_WanVSeriesStatsTable_Object=MibTable
wanVSeriesStatsTable=_WanVSeriesStatsTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,2))
if mibBuilder.loadTexts:wanVSeriesStatsTable.setStatus(_A)
_WanVSeriesStatsEntry_Object=MibTableRow
wanVSeriesStatsEntry=_WanVSeriesStatsEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,2,1))
wanVSeriesStatsEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:wanVSeriesStatsEntry.setStatus(_A)
class _WanVSeriesStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanVSeriesStatsIndex_Type.__name__=_C
_WanVSeriesStatsIndex_Object=MibTableColumn
wanVSeriesStatsIndex=_WanVSeriesStatsIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,2,1,1),_WanVSeriesStatsIndex_Type())
wanVSeriesStatsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanVSeriesStatsIndex.setStatus(_A)
_WanVSeriesStatsDataSource_Type=ObjectIdentifier
_WanVSeriesStatsDataSource_Object=MibTableColumn
wanVSeriesStatsDataSource=_WanVSeriesStatsDataSource_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,2,1,2),_WanVSeriesStatsDataSource_Type())
wanVSeriesStatsDataSource.setMaxAccess(_G)
if mibBuilder.loadTexts:wanVSeriesStatsDataSource.setStatus(_A)
_WanVSeriesStatsDropEvents_Type=Counter64
_WanVSeriesStatsDropEvents_Object=MibTableColumn
wanVSeriesStatsDropEvents=_WanVSeriesStatsDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,2,1,3),_WanVSeriesStatsDropEvents_Type())
wanVSeriesStatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesStatsDropEvents.setStatus(_A)
_WanVSeriesStatsInFrames_Type=Counter64
_WanVSeriesStatsInFrames_Object=MibTableColumn
wanVSeriesStatsInFrames=_WanVSeriesStatsInFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,2,1,4),_WanVSeriesStatsInFrames_Type())
wanVSeriesStatsInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesStatsInFrames.setStatus(_A)
_WanVSeriesStatsOutFrames_Type=Counter64
_WanVSeriesStatsOutFrames_Object=MibTableColumn
wanVSeriesStatsOutFrames=_WanVSeriesStatsOutFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,2,1,5),_WanVSeriesStatsOutFrames_Type())
wanVSeriesStatsOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesStatsOutFrames.setStatus(_A)
_WanVSeriesStatsInOctets_Type=Counter64
_WanVSeriesStatsInOctets_Object=MibTableColumn
wanVSeriesStatsInOctets=_WanVSeriesStatsInOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,2,1,6),_WanVSeriesStatsInOctets_Type())
wanVSeriesStatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesStatsInOctets.setStatus(_A)
_WanVSeriesStatsOutOctets_Type=Counter64
_WanVSeriesStatsOutOctets_Object=MibTableColumn
wanVSeriesStatsOutOctets=_WanVSeriesStatsOutOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,2,1,7),_WanVSeriesStatsOutOctets_Type())
wanVSeriesStatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesStatsOutOctets.setStatus(_A)
_WanVSeriesStatsInFCSs_Type=Counter64
_WanVSeriesStatsInFCSs_Object=MibTableColumn
wanVSeriesStatsInFCSs=_WanVSeriesStatsInFCSs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,2,1,8),_WanVSeriesStatsInFCSs_Type())
wanVSeriesStatsInFCSs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesStatsInFCSs.setStatus(_A)
_WanVSeriesStatsOutFCSs_Type=Counter64
_WanVSeriesStatsOutFCSs_Object=MibTableColumn
wanVSeriesStatsOutFCSs=_WanVSeriesStatsOutFCSs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,2,1,9),_WanVSeriesStatsOutFCSs_Type())
wanVSeriesStatsOutFCSs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesStatsOutFCSs.setStatus(_A)
_WanVSeriesStatsInOverruns_Type=Counter64
_WanVSeriesStatsInOverruns_Object=MibTableColumn
wanVSeriesStatsInOverruns=_WanVSeriesStatsInOverruns_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,2,1,10),_WanVSeriesStatsInOverruns_Type())
wanVSeriesStatsInOverruns.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesStatsInOverruns.setStatus(_A)
_WanVSeriesStatsOutOverruns_Type=Counter64
_WanVSeriesStatsOutOverruns_Object=MibTableColumn
wanVSeriesStatsOutOverruns=_WanVSeriesStatsOutOverruns_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,2,1,11),_WanVSeriesStatsOutOverruns_Type())
wanVSeriesStatsOutOverruns.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesStatsOutOverruns.setStatus(_A)
_WanVSeriesStatsInterruptedFrames_Type=Counter64
_WanVSeriesStatsInterruptedFrames_Object=MibTableColumn
wanVSeriesStatsInterruptedFrames=_WanVSeriesStatsInterruptedFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,2,1,12),_WanVSeriesStatsInterruptedFrames_Type())
wanVSeriesStatsInterruptedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesStatsInterruptedFrames.setStatus(_A)
_WanVSeriesStatsInAbortedFrames_Type=Counter64
_WanVSeriesStatsInAbortedFrames_Object=MibTableColumn
wanVSeriesStatsInAbortedFrames=_WanVSeriesStatsInAbortedFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,2,1,13),_WanVSeriesStatsInAbortedFrames_Type())
wanVSeriesStatsInAbortedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesStatsInAbortedFrames.setStatus(_A)
_WanVSeriesStatsOutAbortedFrames_Type=Counter64
_WanVSeriesStatsOutAbortedFrames_Object=MibTableColumn
wanVSeriesStatsOutAbortedFrames=_WanVSeriesStatsOutAbortedFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,2,1,14),_WanVSeriesStatsOutAbortedFrames_Type())
wanVSeriesStatsOutAbortedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesStatsOutAbortedFrames.setStatus(_A)
_WanVSeriesStatsOwner_Type=OwnerString
_WanVSeriesStatsOwner_Object=MibTableColumn
wanVSeriesStatsOwner=_WanVSeriesStatsOwner_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,2,1,15),_WanVSeriesStatsOwner_Type())
wanVSeriesStatsOwner.setMaxAccess(_G)
if mibBuilder.loadTexts:wanVSeriesStatsOwner.setStatus(_A)
_WanVSeriesStatsStatus_Type=RowStatus
_WanVSeriesStatsStatus_Object=MibTableColumn
wanVSeriesStatsStatus=_WanVSeriesStatsStatus_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,2,1,16),_WanVSeriesStatsStatus_Type())
wanVSeriesStatsStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wanVSeriesStatsStatus.setStatus(_A)
_WanHssiStatsTable_Object=MibTable
wanHssiStatsTable=_WanHssiStatsTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,3))
if mibBuilder.loadTexts:wanHssiStatsTable.setStatus(_D)
_WanHssiStatsEntry_Object=MibTableRow
wanHssiStatsEntry=_WanHssiStatsEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,3,1))
wanHssiStatsEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:wanHssiStatsEntry.setStatus(_D)
class _WanHssiStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanHssiStatsIndex_Type.__name__=_C
_WanHssiStatsIndex_Object=MibTableColumn
wanHssiStatsIndex=_WanHssiStatsIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,3,1,1),_WanHssiStatsIndex_Type())
wanHssiStatsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanHssiStatsIndex.setStatus(_D)
_WanHssiStatsDataSource_Type=ObjectIdentifier
_WanHssiStatsDataSource_Object=MibTableColumn
wanHssiStatsDataSource=_WanHssiStatsDataSource_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,3,1,2),_WanHssiStatsDataSource_Type())
wanHssiStatsDataSource.setMaxAccess(_G)
if mibBuilder.loadTexts:wanHssiStatsDataSource.setStatus(_D)
_WanHssiStatsDropEvents_Type=Counter64
_WanHssiStatsDropEvents_Object=MibTableColumn
wanHssiStatsDropEvents=_WanHssiStatsDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,3,1,3),_WanHssiStatsDropEvents_Type())
wanHssiStatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiStatsDropEvents.setStatus(_D)
_WanHssiStatsInFrames_Type=Counter64
_WanHssiStatsInFrames_Object=MibTableColumn
wanHssiStatsInFrames=_WanHssiStatsInFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,3,1,4),_WanHssiStatsInFrames_Type())
wanHssiStatsInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiStatsInFrames.setStatus(_D)
_WanHssiStatsOutFrames_Type=Counter64
_WanHssiStatsOutFrames_Object=MibTableColumn
wanHssiStatsOutFrames=_WanHssiStatsOutFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,3,1,5),_WanHssiStatsOutFrames_Type())
wanHssiStatsOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiStatsOutFrames.setStatus(_D)
_WanHssiStatsInOctets_Type=Counter64
_WanHssiStatsInOctets_Object=MibTableColumn
wanHssiStatsInOctets=_WanHssiStatsInOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,3,1,6),_WanHssiStatsInOctets_Type())
wanHssiStatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiStatsInOctets.setStatus(_D)
_WanHssiStatsOutOctets_Type=Counter64
_WanHssiStatsOutOctets_Object=MibTableColumn
wanHssiStatsOutOctets=_WanHssiStatsOutOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,3,1,7),_WanHssiStatsOutOctets_Type())
wanHssiStatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiStatsOutOctets.setStatus(_D)
_WanHssiStatsRxLongFrames_Type=Counter64
_WanHssiStatsRxLongFrames_Object=MibTableColumn
wanHssiStatsRxLongFrames=_WanHssiStatsRxLongFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,3,1,8),_WanHssiStatsRxLongFrames_Type())
wanHssiStatsRxLongFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiStatsRxLongFrames.setStatus(_D)
_WanHssiStatsRxCrcErrors_Type=Counter64
_WanHssiStatsRxCrcErrors_Object=MibTableColumn
wanHssiStatsRxCrcErrors=_WanHssiStatsRxCrcErrors_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,3,1,9),_WanHssiStatsRxCrcErrors_Type())
wanHssiStatsRxCrcErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiStatsRxCrcErrors.setStatus(_D)
_WanHssiStatsRxOverruns_Type=Counter64
_WanHssiStatsRxOverruns_Object=MibTableColumn
wanHssiStatsRxOverruns=_WanHssiStatsRxOverruns_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,3,1,10),_WanHssiStatsRxOverruns_Type())
wanHssiStatsRxOverruns.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiStatsRxOverruns.setStatus(_D)
_WanHssiStatsRxAborts_Type=Counter64
_WanHssiStatsRxAborts_Object=MibTableColumn
wanHssiStatsRxAborts=_WanHssiStatsRxAborts_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,3,1,11),_WanHssiStatsRxAborts_Type())
wanHssiStatsRxAborts.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiStatsRxAborts.setStatus(_D)
_WanHssiStatsTxAborts_Type=Counter64
_WanHssiStatsTxAborts_Object=MibTableColumn
wanHssiStatsTxAborts=_WanHssiStatsTxAborts_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,3,1,12),_WanHssiStatsTxAborts_Type())
wanHssiStatsTxAborts.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiStatsTxAborts.setStatus(_D)
_WanHssiStatsTxUnderruns_Type=Counter64
_WanHssiStatsTxUnderruns_Object=MibTableColumn
wanHssiStatsTxUnderruns=_WanHssiStatsTxUnderruns_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,3,1,13),_WanHssiStatsTxUnderruns_Type())
wanHssiStatsTxUnderruns.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiStatsTxUnderruns.setStatus(_D)
_WanHssiStatsRxRingErrors_Type=Counter64
_WanHssiStatsRxRingErrors_Object=MibTableColumn
wanHssiStatsRxRingErrors=_WanHssiStatsRxRingErrors_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,3,1,14),_WanHssiStatsRxRingErrors_Type())
wanHssiStatsRxRingErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiStatsRxRingErrors.setStatus(_D)
_WanHssiStatsRxRingOverruns_Type=Counter64
_WanHssiStatsRxRingOverruns_Object=MibTableColumn
wanHssiStatsRxRingOverruns=_WanHssiStatsRxRingOverruns_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,3,1,15),_WanHssiStatsRxRingOverruns_Type())
wanHssiStatsRxRingOverruns.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiStatsRxRingOverruns.setStatus(_D)
_WanHssiStatsTxRingErrors_Type=Counter64
_WanHssiStatsTxRingErrors_Object=MibTableColumn
wanHssiStatsTxRingErrors=_WanHssiStatsTxRingErrors_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,3,1,16),_WanHssiStatsTxRingErrors_Type())
wanHssiStatsTxRingErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiStatsTxRingErrors.setStatus(_D)
_WanHssiStatsPortOpErrors_Type=Counter64
_WanHssiStatsPortOpErrors_Object=MibTableColumn
wanHssiStatsPortOpErrors=_WanHssiStatsPortOpErrors_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,3,1,17),_WanHssiStatsPortOpErrors_Type())
wanHssiStatsPortOpErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiStatsPortOpErrors.setStatus(_D)
_WanHssiStatsTxCmplProcessings_Type=Counter64
_WanHssiStatsTxCmplProcessings_Object=MibTableColumn
wanHssiStatsTxCmplProcessings=_WanHssiStatsTxCmplProcessings_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,3,1,18),_WanHssiStatsTxCmplProcessings_Type())
wanHssiStatsTxCmplProcessings.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiStatsTxCmplProcessings.setStatus(_D)
_WanHssiStatsOwner_Type=OwnerString
_WanHssiStatsOwner_Object=MibTableColumn
wanHssiStatsOwner=_WanHssiStatsOwner_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,3,1,19),_WanHssiStatsOwner_Type())
wanHssiStatsOwner.setMaxAccess(_G)
if mibBuilder.loadTexts:wanHssiStatsOwner.setStatus(_D)
_WanHssiStatsStatus_Type=RowStatus
_WanHssiStatsStatus_Object=MibTableColumn
wanHssiStatsStatus=_WanHssiStatsStatus_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,3,1,20),_WanHssiStatsStatus_Type())
wanHssiStatsStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wanHssiStatsStatus.setStatus(_D)
_WanT3E3StatsTable_Object=MibTable
wanT3E3StatsTable=_WanT3E3StatsTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4))
if mibBuilder.loadTexts:wanT3E3StatsTable.setStatus(_A)
_WanT3E3StatsEntry_Object=MibTableRow
wanT3E3StatsEntry=_WanT3E3StatsEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1))
wanT3E3StatsEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:wanT3E3StatsEntry.setStatus(_A)
class _WanT3E3StatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanT3E3StatsIndex_Type.__name__=_C
_WanT3E3StatsIndex_Object=MibTableColumn
wanT3E3StatsIndex=_WanT3E3StatsIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,1),_WanT3E3StatsIndex_Type())
wanT3E3StatsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanT3E3StatsIndex.setStatus(_A)
_WanT3E3StatsDataSource_Type=ObjectIdentifier
_WanT3E3StatsDataSource_Object=MibTableColumn
wanT3E3StatsDataSource=_WanT3E3StatsDataSource_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,2),_WanT3E3StatsDataSource_Type())
wanT3E3StatsDataSource.setMaxAccess(_G)
if mibBuilder.loadTexts:wanT3E3StatsDataSource.setStatus(_A)
_WanT3E3StatsDropEvents_Type=Counter64
_WanT3E3StatsDropEvents_Object=MibTableColumn
wanT3E3StatsDropEvents=_WanT3E3StatsDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,3),_WanT3E3StatsDropEvents_Type())
wanT3E3StatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3StatsDropEvents.setStatus(_A)
_WanT3E3StatsInFrames_Type=Counter64
_WanT3E3StatsInFrames_Object=MibTableColumn
wanT3E3StatsInFrames=_WanT3E3StatsInFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,4),_WanT3E3StatsInFrames_Type())
wanT3E3StatsInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3StatsInFrames.setStatus(_A)
_WanT3E3StatsOutFrames_Type=Counter64
_WanT3E3StatsOutFrames_Object=MibTableColumn
wanT3E3StatsOutFrames=_WanT3E3StatsOutFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,5),_WanT3E3StatsOutFrames_Type())
wanT3E3StatsOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3StatsOutFrames.setStatus(_A)
_WanT3E3StatsInOctets_Type=Counter64
_WanT3E3StatsInOctets_Object=MibTableColumn
wanT3E3StatsInOctets=_WanT3E3StatsInOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,6),_WanT3E3StatsInOctets_Type())
wanT3E3StatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3StatsInOctets.setStatus(_A)
_WanT3E3StatsOutOctets_Type=Counter64
_WanT3E3StatsOutOctets_Object=MibTableColumn
wanT3E3StatsOutOctets=_WanT3E3StatsOutOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,7),_WanT3E3StatsOutOctets_Type())
wanT3E3StatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3StatsOutOctets.setStatus(_A)
_WanT3E3StatsPESs_Type=Counter64
_WanT3E3StatsPESs_Object=MibTableColumn
wanT3E3StatsPESs=_WanT3E3StatsPESs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,8),_WanT3E3StatsPESs_Type())
wanT3E3StatsPESs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3StatsPESs.setStatus(_A)
_WanT3E3StatsPSESs_Type=Counter64
_WanT3E3StatsPSESs_Object=MibTableColumn
wanT3E3StatsPSESs=_WanT3E3StatsPSESs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,9),_WanT3E3StatsPSESs_Type())
wanT3E3StatsPSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3StatsPSESs.setStatus(_A)
_WanT3E3StatsOOFs_Type=Counter64
_WanT3E3StatsOOFs_Object=MibTableColumn
wanT3E3StatsOOFs=_WanT3E3StatsOOFs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,10),_WanT3E3StatsOOFs_Type())
wanT3E3StatsOOFs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3StatsOOFs.setStatus(_A)
_WanT3E3StatsSEFSs_Type=Counter64
_WanT3E3StatsSEFSs_Object=MibTableColumn
wanT3E3StatsSEFSs=_WanT3E3StatsSEFSs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,11),_WanT3E3StatsSEFSs_Type())
wanT3E3StatsSEFSs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3StatsSEFSs.setStatus(_A)
_WanT3E3StatsUASs_Type=Counter64
_WanT3E3StatsUASs_Object=MibTableColumn
wanT3E3StatsUASs=_WanT3E3StatsUASs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,12),_WanT3E3StatsUASs_Type())
wanT3E3StatsUASs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3StatsUASs.setStatus(_A)
_WanT3E3StatsLCVs_Type=Counter64
_WanT3E3StatsLCVs_Object=MibTableColumn
wanT3E3StatsLCVs=_WanT3E3StatsLCVs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,13),_WanT3E3StatsLCVs_Type())
wanT3E3StatsLCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3StatsLCVs.setStatus(_A)
_WanT3E3StatsPCVs_Type=Counter64
_WanT3E3StatsPCVs_Object=MibTableColumn
wanT3E3StatsPCVs=_WanT3E3StatsPCVs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,14),_WanT3E3StatsPCVs_Type())
wanT3E3StatsPCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3StatsPCVs.setStatus(_A)
_WanT3E3StatsLESs_Type=Counter64
_WanT3E3StatsLESs_Object=MibTableColumn
wanT3E3StatsLESs=_WanT3E3StatsLESs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,15),_WanT3E3StatsLESs_Type())
wanT3E3StatsLESs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3StatsLESs.setStatus(_A)
_WanT3E3StatsCCVs_Type=Counter64
_WanT3E3StatsCCVs_Object=MibTableColumn
wanT3E3StatsCCVs=_WanT3E3StatsCCVs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,16),_WanT3E3StatsCCVs_Type())
wanT3E3StatsCCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3StatsCCVs.setStatus(_A)
_WanT3E3StatsCESs_Type=Counter64
_WanT3E3StatsCESs_Object=MibTableColumn
wanT3E3StatsCESs=_WanT3E3StatsCESs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,17),_WanT3E3StatsCESs_Type())
wanT3E3StatsCESs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3StatsCESs.setStatus(_A)
_WanT3E3StatsCSESs_Type=Counter64
_WanT3E3StatsCSESs_Object=MibTableColumn
wanT3E3StatsCSESs=_WanT3E3StatsCSESs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,18),_WanT3E3StatsCSESs_Type())
wanT3E3StatsCSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3StatsCSESs.setStatus(_A)
_WanT3E3StatsRAIs_Type=Counter64
_WanT3E3StatsRAIs_Object=MibTableColumn
wanT3E3StatsRAIs=_WanT3E3StatsRAIs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,19),_WanT3E3StatsRAIs_Type())
wanT3E3StatsRAIs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3StatsRAIs.setStatus(_A)
_WanT3E3StatsAISs_Type=Counter64
_WanT3E3StatsAISs_Object=MibTableColumn
wanT3E3StatsAISs=_WanT3E3StatsAISs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,20),_WanT3E3StatsAISs_Type())
wanT3E3StatsAISs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3StatsAISs.setStatus(_A)
_WanT3E3StatsLOFs_Type=Counter64
_WanT3E3StatsLOFs_Object=MibTableColumn
wanT3E3StatsLOFs=_WanT3E3StatsLOFs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,21),_WanT3E3StatsLOFs_Type())
wanT3E3StatsLOFs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3StatsLOFs.setStatus(_A)
_WanT3E3StatsLOSs_Type=Counter64
_WanT3E3StatsLOSs_Object=MibTableColumn
wanT3E3StatsLOSs=_WanT3E3StatsLOSs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,22),_WanT3E3StatsLOSs_Type())
wanT3E3StatsLOSs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3StatsLOSs.setStatus(_A)
_WanT3E3StatsOwner_Type=OwnerString
_WanT3E3StatsOwner_Object=MibTableColumn
wanT3E3StatsOwner=_WanT3E3StatsOwner_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,23),_WanT3E3StatsOwner_Type())
wanT3E3StatsOwner.setMaxAccess(_G)
if mibBuilder.loadTexts:wanT3E3StatsOwner.setStatus(_A)
_WanT3E3StatsStatus_Type=RowStatus
_WanT3E3StatsStatus_Object=MibTableColumn
wanT3E3StatsStatus=_WanT3E3StatsStatus_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,4,1,24),_WanT3E3StatsStatus_Type())
wanT3E3StatsStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wanT3E3StatsStatus.setStatus(_A)
_WanAtmStatsTable_Object=MibTable
wanAtmStatsTable=_WanAtmStatsTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5))
if mibBuilder.loadTexts:wanAtmStatsTable.setStatus(_A)
_WanAtmStatsEntry_Object=MibTableRow
wanAtmStatsEntry=_WanAtmStatsEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1))
wanAtmStatsEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:wanAtmStatsEntry.setStatus(_A)
class _WanAtmStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanAtmStatsIndex_Type.__name__=_C
_WanAtmStatsIndex_Object=MibTableColumn
wanAtmStatsIndex=_WanAtmStatsIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,1),_WanAtmStatsIndex_Type())
wanAtmStatsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanAtmStatsIndex.setStatus(_A)
_WanAtmStatsDataSource_Type=ObjectIdentifier
_WanAtmStatsDataSource_Object=MibTableColumn
wanAtmStatsDataSource=_WanAtmStatsDataSource_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,2),_WanAtmStatsDataSource_Type())
wanAtmStatsDataSource.setMaxAccess(_G)
if mibBuilder.loadTexts:wanAtmStatsDataSource.setStatus(_A)
_WanAtmStatsDropEvents_Type=Counter64
_WanAtmStatsDropEvents_Object=MibTableColumn
wanAtmStatsDropEvents=_WanAtmStatsDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,3),_WanAtmStatsDropEvents_Type())
wanAtmStatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsDropEvents.setStatus(_A)
_WanAtmStatsInCells_Type=Counter64
_WanAtmStatsInCells_Object=MibTableColumn
wanAtmStatsInCells=_WanAtmStatsInCells_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,4),_WanAtmStatsInCells_Type())
wanAtmStatsInCells.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsInCells.setStatus(_A)
_WanAtmStatsOutCells_Type=Counter64
_WanAtmStatsOutCells_Object=MibTableColumn
wanAtmStatsOutCells=_WanAtmStatsOutCells_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,5),_WanAtmStatsOutCells_Type())
wanAtmStatsOutCells.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsOutCells.setStatus(_A)
_WanAtmStatsInCLP1_Type=Counter64
_WanAtmStatsInCLP1_Object=MibTableColumn
wanAtmStatsInCLP1=_WanAtmStatsInCLP1_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,6),_WanAtmStatsInCLP1_Type())
wanAtmStatsInCLP1.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsInCLP1.setStatus(_A)
_WanAtmStatsOutCLP1_Type=Counter64
_WanAtmStatsOutCLP1_Object=MibTableColumn
wanAtmStatsOutCLP1=_WanAtmStatsOutCLP1_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,7),_WanAtmStatsOutCLP1_Type())
wanAtmStatsOutCLP1.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsOutCLP1.setStatus(_A)
_WanAtmStatsConnectionEvents_Type=Counter64
_WanAtmStatsConnectionEvents_Object=MibTableColumn
wanAtmStatsConnectionEvents=_WanAtmStatsConnectionEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,8),_WanAtmStatsConnectionEvents_Type())
wanAtmStatsConnectionEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsConnectionEvents.setStatus(_A)
_WanAtmStatsErroredPDUs_Type=Counter64
_WanAtmStatsErroredPDUs_Object=MibTableColumn
wanAtmStatsErroredPDUs=_WanAtmStatsErroredPDUs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,9),_WanAtmStatsErroredPDUs_Type())
wanAtmStatsErroredPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsErroredPDUs.setStatus(_A)
_WanAtmStatsSetupAttempts_Type=Counter64
_WanAtmStatsSetupAttempts_Object=MibTableColumn
wanAtmStatsSetupAttempts=_WanAtmStatsSetupAttempts_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,10),_WanAtmStatsSetupAttempts_Type())
wanAtmStatsSetupAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsSetupAttempts.setStatus(_A)
_WanAtmStatsInRoutesUnavailable_Type=Counter64
_WanAtmStatsInRoutesUnavailable_Object=MibTableColumn
wanAtmStatsInRoutesUnavailable=_WanAtmStatsInRoutesUnavailable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,11),_WanAtmStatsInRoutesUnavailable_Type())
wanAtmStatsInRoutesUnavailable.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsInRoutesUnavailable.setStatus(_A)
_WanAtmStatsOutRoutesUnavailable_Type=Counter64
_WanAtmStatsOutRoutesUnavailable_Object=MibTableColumn
wanAtmStatsOutRoutesUnavailable=_WanAtmStatsOutRoutesUnavailable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,12),_WanAtmStatsOutRoutesUnavailable_Type())
wanAtmStatsOutRoutesUnavailable.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsOutRoutesUnavailable.setStatus(_A)
_WanAtmStatsInResourcesUnavailable_Type=Counter64
_WanAtmStatsInResourcesUnavailable_Object=MibTableColumn
wanAtmStatsInResourcesUnavailable=_WanAtmStatsInResourcesUnavailable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,13),_WanAtmStatsInResourcesUnavailable_Type())
wanAtmStatsInResourcesUnavailable.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsInResourcesUnavailable.setStatus(_A)
_WanAtmStatsOutResourcesUnavailable_Type=Counter64
_WanAtmStatsOutResourcesUnavailable_Object=MibTableColumn
wanAtmStatsOutResourcesUnavailable=_WanAtmStatsOutResourcesUnavailable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,14),_WanAtmStatsOutResourcesUnavailable_Type())
wanAtmStatsOutResourcesUnavailable.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsOutResourcesUnavailable.setStatus(_A)
_WanAtmStatsInUnsuccessfulCalls_Type=Counter64
_WanAtmStatsInUnsuccessfulCalls_Object=MibTableColumn
wanAtmStatsInUnsuccessfulCalls=_WanAtmStatsInUnsuccessfulCalls_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,15),_WanAtmStatsInUnsuccessfulCalls_Type())
wanAtmStatsInUnsuccessfulCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsInUnsuccessfulCalls.setStatus(_A)
_WanAtmStatsOutUnsuccessfulCalls_Type=Counter64
_WanAtmStatsOutUnsuccessfulCalls_Object=MibTableColumn
wanAtmStatsOutUnsuccessfulCalls=_WanAtmStatsOutUnsuccessfulCalls_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,16),_WanAtmStatsOutUnsuccessfulCalls_Type())
wanAtmStatsOutUnsuccessfulCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsOutUnsuccessfulCalls.setStatus(_A)
_WanAtmStatsInIncorrectMsgs_Type=Counter64
_WanAtmStatsInIncorrectMsgs_Object=MibTableColumn
wanAtmStatsInIncorrectMsgs=_WanAtmStatsInIncorrectMsgs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,17),_WanAtmStatsInIncorrectMsgs_Type())
wanAtmStatsInIncorrectMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsInIncorrectMsgs.setStatus(_A)
_WanAtmStatsOutIncorrectMsgs_Type=Counter64
_WanAtmStatsOutIncorrectMsgs_Object=MibTableColumn
wanAtmStatsOutIncorrectMsgs=_WanAtmStatsOutIncorrectMsgs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,18),_WanAtmStatsOutIncorrectMsgs_Type())
wanAtmStatsOutIncorrectMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsOutIncorrectMsgs.setStatus(_A)
_WanAtmStatsInPartyEvents_Type=Counter64
_WanAtmStatsInPartyEvents_Object=MibTableColumn
wanAtmStatsInPartyEvents=_WanAtmStatsInPartyEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,19),_WanAtmStatsInPartyEvents_Type())
wanAtmStatsInPartyEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsInPartyEvents.setStatus(_A)
_WanAtmStatsOutPartyEvents_Type=Counter64
_WanAtmStatsOutPartyEvents_Object=MibTableColumn
wanAtmStatsOutPartyEvents=_WanAtmStatsOutPartyEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,20),_WanAtmStatsOutPartyEvents_Type())
wanAtmStatsOutPartyEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsOutPartyEvents.setStatus(_A)
_WanAtmStatsInExpiries_Type=Counter64
_WanAtmStatsInExpiries_Object=MibTableColumn
wanAtmStatsInExpiries=_WanAtmStatsInExpiries_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,21),_WanAtmStatsInExpiries_Type())
wanAtmStatsInExpiries.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsInExpiries.setStatus(_A)
_WanAtmStatsOutExpiries_Type=Counter64
_WanAtmStatsOutExpiries_Object=MibTableColumn
wanAtmStatsOutExpiries=_WanAtmStatsOutExpiries_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,22),_WanAtmStatsOutExpiries_Type())
wanAtmStatsOutExpiries.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsOutExpiries.setStatus(_A)
_WanAtmStatsInRestartErrors_Type=Counter64
_WanAtmStatsInRestartErrors_Object=MibTableColumn
wanAtmStatsInRestartErrors=_WanAtmStatsInRestartErrors_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,23),_WanAtmStatsInRestartErrors_Type())
wanAtmStatsInRestartErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsInRestartErrors.setStatus(_A)
_WanAtmStatsOutRestartErrors_Type=Counter64
_WanAtmStatsOutRestartErrors_Object=MibTableColumn
wanAtmStatsOutRestartErrors=_WanAtmStatsOutRestartErrors_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,24),_WanAtmStatsOutRestartErrors_Type())
wanAtmStatsOutRestartErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsOutRestartErrors.setStatus(_A)
_WanAtmStatsInSVCs_Type=Counter64
_WanAtmStatsInSVCs_Object=MibTableColumn
wanAtmStatsInSVCs=_WanAtmStatsInSVCs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,25),_WanAtmStatsInSVCs_Type())
wanAtmStatsInSVCs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsInSVCs.setStatus(_A)
_WanAtmStatsOutSVCs_Type=Counter64
_WanAtmStatsOutSVCs_Object=MibTableColumn
wanAtmStatsOutSVCs=_WanAtmStatsOutSVCs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,26),_WanAtmStatsOutSVCs_Type())
wanAtmStatsOutSVCs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsOutSVCs.setStatus(_A)
_WanAtmStatsInOCDs_Type=Counter64
_WanAtmStatsInOCDs_Object=MibTableColumn
wanAtmStatsInOCDs=_WanAtmStatsInOCDs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,27),_WanAtmStatsInOCDs_Type())
wanAtmStatsInOCDs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsInOCDs.setStatus(_A)
_WanAtmStatsOutOCDs_Type=Counter64
_WanAtmStatsOutOCDs_Object=MibTableColumn
wanAtmStatsOutOCDs=_WanAtmStatsOutOCDs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,28),_WanAtmStatsOutOCDs_Type())
wanAtmStatsOutOCDs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsOutOCDs.setStatus(_A)
_WanAtmStatsInLOCs_Type=Counter64
_WanAtmStatsInLOCs_Object=MibTableColumn
wanAtmStatsInLOCs=_WanAtmStatsInLOCs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,29),_WanAtmStatsInLOCs_Type())
wanAtmStatsInLOCs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsInLOCs.setStatus(_A)
_WanAtmStatsOutLOCs_Type=Counter64
_WanAtmStatsOutLOCs_Object=MibTableColumn
wanAtmStatsOutLOCs=_WanAtmStatsOutLOCs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,30),_WanAtmStatsOutLOCs_Type())
wanAtmStatsOutLOCs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsOutLOCs.setStatus(_A)
_WanAtmStatsInLOFs_Type=Counter64
_WanAtmStatsInLOFs_Object=MibTableColumn
wanAtmStatsInLOFs=_WanAtmStatsInLOFs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,31),_WanAtmStatsInLOFs_Type())
wanAtmStatsInLOFs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsInLOFs.setStatus(_A)
_WanAtmStatsOutLOFs_Type=Counter64
_WanAtmStatsOutLOFs_Object=MibTableColumn
wanAtmStatsOutLOFs=_WanAtmStatsOutLOFs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,32),_WanAtmStatsOutLOFs_Type())
wanAtmStatsOutLOFs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsOutLOFs.setStatus(_A)
_WanAtmStatsInLOPs_Type=Counter64
_WanAtmStatsInLOPs_Object=MibTableColumn
wanAtmStatsInLOPs=_WanAtmStatsInLOPs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,33),_WanAtmStatsInLOPs_Type())
wanAtmStatsInLOPs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsInLOPs.setStatus(_A)
_WanAtmStatsOutLOPs_Type=Counter64
_WanAtmStatsOutLOPs_Object=MibTableColumn
wanAtmStatsOutLOPs=_WanAtmStatsOutLOPs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,34),_WanAtmStatsOutLOPs_Type())
wanAtmStatsOutLOPs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsOutLOPs.setStatus(_A)
_WanAtmStatsInLOSs_Type=Counter64
_WanAtmStatsInLOSs_Object=MibTableColumn
wanAtmStatsInLOSs=_WanAtmStatsInLOSs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,35),_WanAtmStatsInLOSs_Type())
wanAtmStatsInLOSs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsInLOSs.setStatus(_A)
_WanAtmStatsOutLOSs_Type=Counter64
_WanAtmStatsOutLOSs_Object=MibTableColumn
wanAtmStatsOutLOSs=_WanAtmStatsOutLOSs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,36),_WanAtmStatsOutLOSs_Type())
wanAtmStatsOutLOSs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmStatsOutLOSs.setStatus(_A)
_WanAtmStatsOwner_Type=OwnerString
_WanAtmStatsOwner_Object=MibTableColumn
wanAtmStatsOwner=_WanAtmStatsOwner_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,37),_WanAtmStatsOwner_Type())
wanAtmStatsOwner.setMaxAccess(_G)
if mibBuilder.loadTexts:wanAtmStatsOwner.setStatus(_A)
_WanAtmStatsStatus_Type=RowStatus
_WanAtmStatsStatus_Object=MibTableColumn
wanAtmStatsStatus=_WanAtmStatsStatus_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,1,5,1,38),_WanAtmStatsStatus_Type())
wanAtmStatsStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wanAtmStatsStatus.setStatus(_A)
_WanProtocolStats_ObjectIdentity=ObjectIdentity
wanProtocolStats=_WanProtocolStats_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2))
_WanX25StatsTable_Object=MibTable
wanX25StatsTable=_WanX25StatsTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1))
if mibBuilder.loadTexts:wanX25StatsTable.setStatus(_A)
_WanX25StatsEntry_Object=MibTableRow
wanX25StatsEntry=_WanX25StatsEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1))
wanX25StatsEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:wanX25StatsEntry.setStatus(_A)
class _WanX25StatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanX25StatsIndex_Type.__name__=_C
_WanX25StatsIndex_Object=MibTableColumn
wanX25StatsIndex=_WanX25StatsIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,1),_WanX25StatsIndex_Type())
wanX25StatsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanX25StatsIndex.setStatus(_A)
_WanX25StatsDataSource_Type=ObjectIdentifier
_WanX25StatsDataSource_Object=MibTableColumn
wanX25StatsDataSource=_WanX25StatsDataSource_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,2),_WanX25StatsDataSource_Type())
wanX25StatsDataSource.setMaxAccess(_G)
if mibBuilder.loadTexts:wanX25StatsDataSource.setStatus(_A)
_WanX25StatsDropEvents_Type=Counter64
_WanX25StatsDropEvents_Object=MibTableColumn
wanX25StatsDropEvents=_WanX25StatsDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,3),_WanX25StatsDropEvents_Type())
wanX25StatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25StatsDropEvents.setStatus(_A)
_WanX25StatsInFrames_Type=Counter64
_WanX25StatsInFrames_Object=MibTableColumn
wanX25StatsInFrames=_WanX25StatsInFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,4),_WanX25StatsInFrames_Type())
wanX25StatsInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25StatsInFrames.setStatus(_A)
_WanX25StatsOutFrames_Type=Counter64
_WanX25StatsOutFrames_Object=MibTableColumn
wanX25StatsOutFrames=_WanX25StatsOutFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,5),_WanX25StatsOutFrames_Type())
wanX25StatsOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25StatsOutFrames.setStatus(_A)
_WanX25StatsInOctets_Type=Counter64
_WanX25StatsInOctets_Object=MibTableColumn
wanX25StatsInOctets=_WanX25StatsInOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,6),_WanX25StatsInOctets_Type())
wanX25StatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25StatsInOctets.setStatus(_A)
_WanX25StatsOutOctets_Type=Counter64
_WanX25StatsOutOctets_Object=MibTableColumn
wanX25StatsOutOctets=_WanX25StatsOutOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,7),_WanX25StatsOutOctets_Type())
wanX25StatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25StatsOutOctets.setStatus(_A)
_WanX25StatsInRejects_Type=Counter64
_WanX25StatsInRejects_Object=MibTableColumn
wanX25StatsInRejects=_WanX25StatsInRejects_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,8),_WanX25StatsInRejects_Type())
wanX25StatsInRejects.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25StatsInRejects.setStatus(_A)
_WanX25StatsOutRejects_Type=Counter64
_WanX25StatsOutRejects_Object=MibTableColumn
wanX25StatsOutRejects=_WanX25StatsOutRejects_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,9),_WanX25StatsOutRejects_Type())
wanX25StatsOutRejects.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25StatsOutRejects.setStatus(_A)
_WanX25StatsInAttempts_Type=Counter64
_WanX25StatsInAttempts_Object=MibTableColumn
wanX25StatsInAttempts=_WanX25StatsInAttempts_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,10),_WanX25StatsInAttempts_Type())
wanX25StatsInAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25StatsInAttempts.setStatus(_A)
_WanX25StatsOutAttempts_Type=Counter64
_WanX25StatsOutAttempts_Object=MibTableColumn
wanX25StatsOutAttempts=_WanX25StatsOutAttempts_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,11),_WanX25StatsOutAttempts_Type())
wanX25StatsOutAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25StatsOutAttempts.setStatus(_A)
_WanX25StatsInFailures_Type=Counter64
_WanX25StatsInFailures_Object=MibTableColumn
wanX25StatsInFailures=_WanX25StatsInFailures_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,12),_WanX25StatsInFailures_Type())
wanX25StatsInFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25StatsInFailures.setStatus(_A)
_WanX25StatsOutFailures_Type=Counter64
_WanX25StatsOutFailures_Object=MibTableColumn
wanX25StatsOutFailures=_WanX25StatsOutFailures_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,13),_WanX25StatsOutFailures_Type())
wanX25StatsOutFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25StatsOutFailures.setStatus(_A)
_WanX25StatsProviderClears_Type=Counter64
_WanX25StatsProviderClears_Object=MibTableColumn
wanX25StatsProviderClears=_WanX25StatsProviderClears_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,14),_WanX25StatsProviderClears_Type())
wanX25StatsProviderClears.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25StatsProviderClears.setStatus(_A)
_WanX25StatsInResets_Type=Counter64
_WanX25StatsInResets_Object=MibTableColumn
wanX25StatsInResets=_WanX25StatsInResets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,15),_WanX25StatsInResets_Type())
wanX25StatsInResets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25StatsInResets.setStatus(_A)
_WanX25StatsOutResets_Type=Counter64
_WanX25StatsOutResets_Object=MibTableColumn
wanX25StatsOutResets=_WanX25StatsOutResets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,16),_WanX25StatsOutResets_Type())
wanX25StatsOutResets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25StatsOutResets.setStatus(_A)
_WanX25StatsProviderResets_Type=Counter64
_WanX25StatsProviderResets_Object=MibTableColumn
wanX25StatsProviderResets=_WanX25StatsProviderResets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,17),_WanX25StatsProviderResets_Type())
wanX25StatsProviderResets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25StatsProviderResets.setStatus(_A)
_WanX25StatsInAccusedErrors_Type=Counter64
_WanX25StatsInAccusedErrors_Object=MibTableColumn
wanX25StatsInAccusedErrors=_WanX25StatsInAccusedErrors_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,18),_WanX25StatsInAccusedErrors_Type())
wanX25StatsInAccusedErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25StatsInAccusedErrors.setStatus(_A)
_WanX25StatsOutAccusedErrors_Type=Counter64
_WanX25StatsOutAccusedErrors_Object=MibTableColumn
wanX25StatsOutAccusedErrors=_WanX25StatsOutAccusedErrors_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,19),_WanX25StatsOutAccusedErrors_Type())
wanX25StatsOutAccusedErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25StatsOutAccusedErrors.setStatus(_A)
_WanX25StatsInInterrupts_Type=Counter64
_WanX25StatsInInterrupts_Object=MibTableColumn
wanX25StatsInInterrupts=_WanX25StatsInInterrupts_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,20),_WanX25StatsInInterrupts_Type())
wanX25StatsInInterrupts.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25StatsInInterrupts.setStatus(_A)
_WanX25StatsOutInterrupts_Type=Counter64
_WanX25StatsOutInterrupts_Object=MibTableColumn
wanX25StatsOutInterrupts=_WanX25StatsOutInterrupts_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,21),_WanX25StatsOutInterrupts_Type())
wanX25StatsOutInterrupts.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25StatsOutInterrupts.setStatus(_A)
_WanX25StatsOwner_Type=OwnerString
_WanX25StatsOwner_Object=MibTableColumn
wanX25StatsOwner=_WanX25StatsOwner_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,22),_WanX25StatsOwner_Type())
wanX25StatsOwner.setMaxAccess(_G)
if mibBuilder.loadTexts:wanX25StatsOwner.setStatus(_A)
_WanX25StatsStatus_Type=RowStatus
_WanX25StatsStatus_Object=MibTableColumn
wanX25StatsStatus=_WanX25StatsStatus_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,1,1,23),_WanX25StatsStatus_Type())
wanX25StatsStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wanX25StatsStatus.setStatus(_A)
_WanFrStatsTable_Object=MibTable
wanFrStatsTable=_WanFrStatsTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,2))
if mibBuilder.loadTexts:wanFrStatsTable.setStatus(_A)
_WanFrStatsEntry_Object=MibTableRow
wanFrStatsEntry=_WanFrStatsEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,2,1))
wanFrStatsEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:wanFrStatsEntry.setStatus(_A)
class _WanFrStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanFrStatsIndex_Type.__name__=_C
_WanFrStatsIndex_Object=MibTableColumn
wanFrStatsIndex=_WanFrStatsIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,2,1,1),_WanFrStatsIndex_Type())
wanFrStatsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanFrStatsIndex.setStatus(_A)
_WanFrStatsDataSource_Type=ObjectIdentifier
_WanFrStatsDataSource_Object=MibTableColumn
wanFrStatsDataSource=_WanFrStatsDataSource_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,2,1,2),_WanFrStatsDataSource_Type())
wanFrStatsDataSource.setMaxAccess(_G)
if mibBuilder.loadTexts:wanFrStatsDataSource.setStatus(_A)
_WanFrStatsDropEvents_Type=Counter64
_WanFrStatsDropEvents_Object=MibTableColumn
wanFrStatsDropEvents=_WanFrStatsDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,2,1,3),_WanFrStatsDropEvents_Type())
wanFrStatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrStatsDropEvents.setStatus(_A)
_WanFrStatsInFrames_Type=Counter64
_WanFrStatsInFrames_Object=MibTableColumn
wanFrStatsInFrames=_WanFrStatsInFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,2,1,4),_WanFrStatsInFrames_Type())
wanFrStatsInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrStatsInFrames.setStatus(_A)
_WanFrStatsOutFrames_Type=Counter64
_WanFrStatsOutFrames_Object=MibTableColumn
wanFrStatsOutFrames=_WanFrStatsOutFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,2,1,5),_WanFrStatsOutFrames_Type())
wanFrStatsOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrStatsOutFrames.setStatus(_A)
_WanFrStatsInOctets_Type=Counter64
_WanFrStatsInOctets_Object=MibTableColumn
wanFrStatsInOctets=_WanFrStatsInOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,2,1,6),_WanFrStatsInOctets_Type())
wanFrStatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrStatsInOctets.setStatus(_A)
_WanFrStatsOutOctets_Type=Counter64
_WanFrStatsOutOctets_Object=MibTableColumn
wanFrStatsOutOctets=_WanFrStatsOutOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,2,1,7),_WanFrStatsOutOctets_Type())
wanFrStatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrStatsOutOctets.setStatus(_A)
_WanFrStatsInFECNs_Type=Counter64
_WanFrStatsInFECNs_Object=MibTableColumn
wanFrStatsInFECNs=_WanFrStatsInFECNs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,2,1,8),_WanFrStatsInFECNs_Type())
wanFrStatsInFECNs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrStatsInFECNs.setStatus(_A)
_WanFrStatsOutFECNs_Type=Counter64
_WanFrStatsOutFECNs_Object=MibTableColumn
wanFrStatsOutFECNs=_WanFrStatsOutFECNs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,2,1,9),_WanFrStatsOutFECNs_Type())
wanFrStatsOutFECNs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrStatsOutFECNs.setStatus(_A)
_WanFrStatsInBECNs_Type=Counter64
_WanFrStatsInBECNs_Object=MibTableColumn
wanFrStatsInBECNs=_WanFrStatsInBECNs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,2,1,10),_WanFrStatsInBECNs_Type())
wanFrStatsInBECNs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrStatsInBECNs.setStatus(_A)
_WanFrStatsOutBECNs_Type=Counter64
_WanFrStatsOutBECNs_Object=MibTableColumn
wanFrStatsOutBECNs=_WanFrStatsOutBECNs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,2,1,11),_WanFrStatsOutBECNs_Type())
wanFrStatsOutBECNs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrStatsOutBECNs.setStatus(_A)
_WanFrStatsInDEs_Type=Counter64
_WanFrStatsInDEs_Object=MibTableColumn
wanFrStatsInDEs=_WanFrStatsInDEs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,2,1,12),_WanFrStatsInDEs_Type())
wanFrStatsInDEs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrStatsInDEs.setStatus(_A)
_WanFrStatsOutDEs_Type=Counter64
_WanFrStatsOutDEs_Object=MibTableColumn
wanFrStatsOutDEs=_WanFrStatsOutDEs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,2,1,13),_WanFrStatsOutDEs_Type())
wanFrStatsOutDEs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrStatsOutDEs.setStatus(_A)
_WanFrStatsOwner_Type=OwnerString
_WanFrStatsOwner_Object=MibTableColumn
wanFrStatsOwner=_WanFrStatsOwner_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,2,1,14),_WanFrStatsOwner_Type())
wanFrStatsOwner.setMaxAccess(_G)
if mibBuilder.loadTexts:wanFrStatsOwner.setStatus(_A)
_WanFrStatsStatus_Type=RowStatus
_WanFrStatsStatus_Object=MibTableColumn
wanFrStatsStatus=_WanFrStatsStatus_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,2,1,15),_WanFrStatsStatus_Type())
wanFrStatsStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wanFrStatsStatus.setStatus(_A)
_WanAal5StatsTable_Object=MibTable
wanAal5StatsTable=_WanAal5StatsTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,3))
if mibBuilder.loadTexts:wanAal5StatsTable.setStatus(_A)
_WanAal5StatsEntry_Object=MibTableRow
wanAal5StatsEntry=_WanAal5StatsEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,3,1))
wanAal5StatsEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:wanAal5StatsEntry.setStatus(_A)
class _WanAal5StatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanAal5StatsIndex_Type.__name__=_C
_WanAal5StatsIndex_Object=MibTableColumn
wanAal5StatsIndex=_WanAal5StatsIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,3,1,1),_WanAal5StatsIndex_Type())
wanAal5StatsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanAal5StatsIndex.setStatus(_A)
_WanAal5StatsDataSource_Type=ObjectIdentifier
_WanAal5StatsDataSource_Object=MibTableColumn
wanAal5StatsDataSource=_WanAal5StatsDataSource_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,3,1,2),_WanAal5StatsDataSource_Type())
wanAal5StatsDataSource.setMaxAccess(_G)
if mibBuilder.loadTexts:wanAal5StatsDataSource.setStatus(_A)
_WanAal5StatsDropEvents_Type=Counter64
_WanAal5StatsDropEvents_Object=MibTableColumn
wanAal5StatsDropEvents=_WanAal5StatsDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,3,1,3),_WanAal5StatsDropEvents_Type())
wanAal5StatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5StatsDropEvents.setStatus(_A)
_WanAal5StatsInCells_Type=Counter64
_WanAal5StatsInCells_Object=MibTableColumn
wanAal5StatsInCells=_WanAal5StatsInCells_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,3,1,4),_WanAal5StatsInCells_Type())
wanAal5StatsInCells.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5StatsInCells.setStatus(_A)
_WanAal5StatsOutCells_Type=Counter64
_WanAal5StatsOutCells_Object=MibTableColumn
wanAal5StatsOutCells=_WanAal5StatsOutCells_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,3,1,5),_WanAal5StatsOutCells_Type())
wanAal5StatsOutCells.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5StatsOutCells.setStatus(_A)
_WanAal5StatsInPDUs_Type=Counter64
_WanAal5StatsInPDUs_Object=MibTableColumn
wanAal5StatsInPDUs=_WanAal5StatsInPDUs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,3,1,6),_WanAal5StatsInPDUs_Type())
wanAal5StatsInPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5StatsInPDUs.setStatus(_A)
_WanAal5StatsOutPDUs_Type=Counter64
_WanAal5StatsOutPDUs_Object=MibTableColumn
wanAal5StatsOutPDUs=_WanAal5StatsOutPDUs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,3,1,7),_WanAal5StatsOutPDUs_Type())
wanAal5StatsOutPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5StatsOutPDUs.setStatus(_A)
_WanAal5StatsInOctets_Type=Counter64
_WanAal5StatsInOctets_Object=MibTableColumn
wanAal5StatsInOctets=_WanAal5StatsInOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,3,1,8),_WanAal5StatsInOctets_Type())
wanAal5StatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5StatsInOctets.setStatus(_A)
_WanAal5StatsOutOctets_Type=Counter64
_WanAal5StatsOutOctets_Object=MibTableColumn
wanAal5StatsOutOctets=_WanAal5StatsOutOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,3,1,9),_WanAal5StatsOutOctets_Type())
wanAal5StatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5StatsOutOctets.setStatus(_A)
_WanAal5StatsInCLP1_Type=Counter64
_WanAal5StatsInCLP1_Object=MibTableColumn
wanAal5StatsInCLP1=_WanAal5StatsInCLP1_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,3,1,10),_WanAal5StatsInCLP1_Type())
wanAal5StatsInCLP1.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5StatsInCLP1.setStatus(_A)
_WanAal5StatsOutCLP1_Type=Counter64
_WanAal5StatsOutCLP1_Object=MibTableColumn
wanAal5StatsOutCLP1=_WanAal5StatsOutCLP1_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,3,1,11),_WanAal5StatsOutCLP1_Type())
wanAal5StatsOutCLP1.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5StatsOutCLP1.setStatus(_A)
_WanAal5StatsInCRCs_Type=Counter64
_WanAal5StatsInCRCs_Object=MibTableColumn
wanAal5StatsInCRCs=_WanAal5StatsInCRCs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,3,1,12),_WanAal5StatsInCRCs_Type())
wanAal5StatsInCRCs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5StatsInCRCs.setStatus(_A)
_WanAal5StatsOutCRCs_Type=Counter64
_WanAal5StatsOutCRCs_Object=MibTableColumn
wanAal5StatsOutCRCs=_WanAal5StatsOutCRCs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,3,1,13),_WanAal5StatsOutCRCs_Type())
wanAal5StatsOutCRCs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5StatsOutCRCs.setStatus(_A)
_WanAal5StatsInOversizedSDUs_Type=Counter64
_WanAal5StatsInOversizedSDUs_Object=MibTableColumn
wanAal5StatsInOversizedSDUs=_WanAal5StatsInOversizedSDUs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,3,1,14),_WanAal5StatsInOversizedSDUs_Type())
wanAal5StatsInOversizedSDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5StatsInOversizedSDUs.setStatus(_A)
_WanAal5StatsOutOversizedSDUs_Type=Counter64
_WanAal5StatsOutOversizedSDUs_Object=MibTableColumn
wanAal5StatsOutOversizedSDUs=_WanAal5StatsOutOversizedSDUs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,3,1,15),_WanAal5StatsOutOversizedSDUs_Type())
wanAal5StatsOutOversizedSDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5StatsOutOversizedSDUs.setStatus(_A)
_WanAal5StatsInSVCs_Type=Counter64
_WanAal5StatsInSVCs_Object=MibTableColumn
wanAal5StatsInSVCs=_WanAal5StatsInSVCs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,3,1,16),_WanAal5StatsInSVCs_Type())
wanAal5StatsInSVCs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5StatsInSVCs.setStatus(_A)
_WanAal5StatsOutSVCs_Type=Counter64
_WanAal5StatsOutSVCs_Object=MibTableColumn
wanAal5StatsOutSVCs=_WanAal5StatsOutSVCs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,3,1,17),_WanAal5StatsOutSVCs_Type())
wanAal5StatsOutSVCs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5StatsOutSVCs.setStatus(_A)
_WanAal5StatsOwner_Type=OwnerString
_WanAal5StatsOwner_Object=MibTableColumn
wanAal5StatsOwner=_WanAal5StatsOwner_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,3,1,18),_WanAal5StatsOwner_Type())
wanAal5StatsOwner.setMaxAccess(_G)
if mibBuilder.loadTexts:wanAal5StatsOwner.setStatus(_A)
_WanAal5StatsStatus_Type=RowStatus
_WanAal5StatsStatus_Object=MibTableColumn
wanAal5StatsStatus=_WanAal5StatsStatus_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,3,1,19),_WanAal5StatsStatus_Type())
wanAal5StatsStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wanAal5StatsStatus.setStatus(_A)
_WanPppStatsTable_Object=MibTable
wanPppStatsTable=_WanPppStatsTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,4))
if mibBuilder.loadTexts:wanPppStatsTable.setStatus(_A)
_WanPppStatsEntry_Object=MibTableRow
wanPppStatsEntry=_WanPppStatsEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,4,1))
wanPppStatsEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:wanPppStatsEntry.setStatus(_A)
class _WanPppStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanPppStatsIndex_Type.__name__=_C
_WanPppStatsIndex_Object=MibTableColumn
wanPppStatsIndex=_WanPppStatsIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,4,1,1),_WanPppStatsIndex_Type())
wanPppStatsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanPppStatsIndex.setStatus(_A)
_WanPppStatsDataSource_Type=ObjectIdentifier
_WanPppStatsDataSource_Object=MibTableColumn
wanPppStatsDataSource=_WanPppStatsDataSource_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,4,1,2),_WanPppStatsDataSource_Type())
wanPppStatsDataSource.setMaxAccess(_G)
if mibBuilder.loadTexts:wanPppStatsDataSource.setStatus(_A)
_WanPppStatsDropEvents_Type=Counter64
_WanPppStatsDropEvents_Object=MibTableColumn
wanPppStatsDropEvents=_WanPppStatsDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,4,1,3),_WanPppStatsDropEvents_Type())
wanPppStatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppStatsDropEvents.setStatus(_A)
_WanPppStatsInFrames_Type=Counter64
_WanPppStatsInFrames_Object=MibTableColumn
wanPppStatsInFrames=_WanPppStatsInFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,4,1,4),_WanPppStatsInFrames_Type())
wanPppStatsInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppStatsInFrames.setStatus(_A)
_WanPppStatsOutFrames_Type=Counter64
_WanPppStatsOutFrames_Object=MibTableColumn
wanPppStatsOutFrames=_WanPppStatsOutFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,4,1,5),_WanPppStatsOutFrames_Type())
wanPppStatsOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppStatsOutFrames.setStatus(_A)
_WanPppStatsInOctets_Type=Counter64
_WanPppStatsInOctets_Object=MibTableColumn
wanPppStatsInOctets=_WanPppStatsInOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,4,1,6),_WanPppStatsInOctets_Type())
wanPppStatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppStatsInOctets.setStatus(_A)
_WanPppStatsOutOctets_Type=Counter64
_WanPppStatsOutOctets_Object=MibTableColumn
wanPppStatsOutOctets=_WanPppStatsOutOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,4,1,7),_WanPppStatsOutOctets_Type())
wanPppStatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppStatsOutOctets.setStatus(_A)
_WanPppStatsInBadAddresses_Type=Counter64
_WanPppStatsInBadAddresses_Object=MibTableColumn
wanPppStatsInBadAddresses=_WanPppStatsInBadAddresses_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,4,1,8),_WanPppStatsInBadAddresses_Type())
wanPppStatsInBadAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppStatsInBadAddresses.setStatus(_A)
_WanPppStatsOutBadAddresses_Type=Counter64
_WanPppStatsOutBadAddresses_Object=MibTableColumn
wanPppStatsOutBadAddresses=_WanPppStatsOutBadAddresses_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,4,1,9),_WanPppStatsOutBadAddresses_Type())
wanPppStatsOutBadAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppStatsOutBadAddresses.setStatus(_A)
_WanPppStatsInBadControls_Type=Counter64
_WanPppStatsInBadControls_Object=MibTableColumn
wanPppStatsInBadControls=_WanPppStatsInBadControls_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,4,1,10),_WanPppStatsInBadControls_Type())
wanPppStatsInBadControls.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppStatsInBadControls.setStatus(_A)
_WanPppStatsOutBadControls_Type=Counter64
_WanPppStatsOutBadControls_Object=MibTableColumn
wanPppStatsOutBadControls=_WanPppStatsOutBadControls_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,4,1,11),_WanPppStatsOutBadControls_Type())
wanPppStatsOutBadControls.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppStatsOutBadControls.setStatus(_A)
_WanPppStatsInLongFrames_Type=Counter64
_WanPppStatsInLongFrames_Object=MibTableColumn
wanPppStatsInLongFrames=_WanPppStatsInLongFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,4,1,12),_WanPppStatsInLongFrames_Type())
wanPppStatsInLongFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppStatsInLongFrames.setStatus(_A)
_WanPppStatsOutLongFrames_Type=Counter64
_WanPppStatsOutLongFrames_Object=MibTableColumn
wanPppStatsOutLongFrames=_WanPppStatsOutLongFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,4,1,13),_WanPppStatsOutLongFrames_Type())
wanPppStatsOutLongFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppStatsOutLongFrames.setStatus(_A)
_WanPppStatsInBadFCSs_Type=Counter64
_WanPppStatsInBadFCSs_Object=MibTableColumn
wanPppStatsInBadFCSs=_WanPppStatsInBadFCSs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,4,1,14),_WanPppStatsInBadFCSs_Type())
wanPppStatsInBadFCSs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppStatsInBadFCSs.setStatus(_A)
_WanPppStatsOutBadFCSs_Type=Counter64
_WanPppStatsOutBadFCSs_Object=MibTableColumn
wanPppStatsOutBadFCSs=_WanPppStatsOutBadFCSs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,4,1,15),_WanPppStatsOutBadFCSs_Type())
wanPppStatsOutBadFCSs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppStatsOutBadFCSs.setStatus(_A)
_WanPppStatsOwner_Type=OwnerString
_WanPppStatsOwner_Object=MibTableColumn
wanPppStatsOwner=_WanPppStatsOwner_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,4,1,16),_WanPppStatsOwner_Type())
wanPppStatsOwner.setMaxAccess(_G)
if mibBuilder.loadTexts:wanPppStatsOwner.setStatus(_A)
_WanPppStatsStatus_Type=RowStatus
_WanPppStatsStatus_Object=MibTableColumn
wanPppStatsStatus=_WanPppStatsStatus_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,2,4,1,17),_WanPppStatsStatus_Type())
wanPppStatsStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wanPppStatsStatus.setStatus(_A)
_WanPvcStats_ObjectIdentity=ObjectIdentity
wanPvcStats=_WanPvcStats_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3))
_WanX25PvcStatsTable_Object=MibTable
wanX25PvcStatsTable=_WanX25PvcStatsTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,1))
if mibBuilder.loadTexts:wanX25PvcStatsTable.setStatus(_A)
_WanX25PvcStatsEntry_Object=MibTableRow
wanX25PvcStatsEntry=_WanX25PvcStatsEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,1,1))
wanX25PvcStatsEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:wanX25PvcStatsEntry.setStatus(_A)
class _WanX25PvcStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanX25PvcStatsIndex_Type.__name__=_C
_WanX25PvcStatsIndex_Object=MibTableColumn
wanX25PvcStatsIndex=_WanX25PvcStatsIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,1,1,1),_WanX25PvcStatsIndex_Type())
wanX25PvcStatsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanX25PvcStatsIndex.setStatus(_A)
_WanX25PvcStatsDataSource_Type=ObjectIdentifier
_WanX25PvcStatsDataSource_Object=MibTableColumn
wanX25PvcStatsDataSource=_WanX25PvcStatsDataSource_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,1,1,2),_WanX25PvcStatsDataSource_Type())
wanX25PvcStatsDataSource.setMaxAccess(_G)
if mibBuilder.loadTexts:wanX25PvcStatsDataSource.setStatus(_A)
_WanX25PvcStatsDropEvents_Type=Counter64
_WanX25PvcStatsDropEvents_Object=MibTableColumn
wanX25PvcStatsDropEvents=_WanX25PvcStatsDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,1,1,3),_WanX25PvcStatsDropEvents_Type())
wanX25PvcStatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcStatsDropEvents.setStatus(_A)
_WanX25PvcStatsInFrames_Type=Counter64
_WanX25PvcStatsInFrames_Object=MibTableColumn
wanX25PvcStatsInFrames=_WanX25PvcStatsInFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,1,1,4),_WanX25PvcStatsInFrames_Type())
wanX25PvcStatsInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcStatsInFrames.setStatus(_A)
_WanX25PvcStatsOutFrames_Type=Counter64
_WanX25PvcStatsOutFrames_Object=MibTableColumn
wanX25PvcStatsOutFrames=_WanX25PvcStatsOutFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,1,1,5),_WanX25PvcStatsOutFrames_Type())
wanX25PvcStatsOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcStatsOutFrames.setStatus(_A)
_WanX25PvcStatsInOctets_Type=Counter64
_WanX25PvcStatsInOctets_Object=MibTableColumn
wanX25PvcStatsInOctets=_WanX25PvcStatsInOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,1,1,6),_WanX25PvcStatsInOctets_Type())
wanX25PvcStatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcStatsInOctets.setStatus(_A)
_WanX25PvcStatsOutOctets_Type=Counter64
_WanX25PvcStatsOutOctets_Object=MibTableColumn
wanX25PvcStatsOutOctets=_WanX25PvcStatsOutOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,1,1,7),_WanX25PvcStatsOutOctets_Type())
wanX25PvcStatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcStatsOutOctets.setStatus(_A)
_WanX25PvcStatsInResets_Type=Counter64
_WanX25PvcStatsInResets_Object=MibTableColumn
wanX25PvcStatsInResets=_WanX25PvcStatsInResets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,1,1,8),_WanX25PvcStatsInResets_Type())
wanX25PvcStatsInResets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcStatsInResets.setStatus(_A)
_WanX25PvcStatsOutResets_Type=Counter64
_WanX25PvcStatsOutResets_Object=MibTableColumn
wanX25PvcStatsOutResets=_WanX25PvcStatsOutResets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,1,1,9),_WanX25PvcStatsOutResets_Type())
wanX25PvcStatsOutResets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcStatsOutResets.setStatus(_A)
_WanX25PvcStatsProviderResets_Type=Counter64
_WanX25PvcStatsProviderResets_Object=MibTableColumn
wanX25PvcStatsProviderResets=_WanX25PvcStatsProviderResets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,1,1,10),_WanX25PvcStatsProviderResets_Type())
wanX25PvcStatsProviderResets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcStatsProviderResets.setStatus(_A)
_WanX25PvcStatsInAccusedErrors_Type=Counter64
_WanX25PvcStatsInAccusedErrors_Object=MibTableColumn
wanX25PvcStatsInAccusedErrors=_WanX25PvcStatsInAccusedErrors_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,1,1,11),_WanX25PvcStatsInAccusedErrors_Type())
wanX25PvcStatsInAccusedErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcStatsInAccusedErrors.setStatus(_A)
_WanX25PvcStatsOutAccusedErrors_Type=Counter64
_WanX25PvcStatsOutAccusedErrors_Object=MibTableColumn
wanX25PvcStatsOutAccusedErrors=_WanX25PvcStatsOutAccusedErrors_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,1,1,12),_WanX25PvcStatsOutAccusedErrors_Type())
wanX25PvcStatsOutAccusedErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcStatsOutAccusedErrors.setStatus(_A)
_WanX25PvcStatsInInterrupts_Type=Counter64
_WanX25PvcStatsInInterrupts_Object=MibTableColumn
wanX25PvcStatsInInterrupts=_WanX25PvcStatsInInterrupts_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,1,1,13),_WanX25PvcStatsInInterrupts_Type())
wanX25PvcStatsInInterrupts.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcStatsInInterrupts.setStatus(_A)
_WanX25PvcStatsOutInterrupts_Type=Counter64
_WanX25PvcStatsOutInterrupts_Object=MibTableColumn
wanX25PvcStatsOutInterrupts=_WanX25PvcStatsOutInterrupts_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,1,1,14),_WanX25PvcStatsOutInterrupts_Type())
wanX25PvcStatsOutInterrupts.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcStatsOutInterrupts.setStatus(_A)
_WanX25PvcStatsUpTime_Type=TimeTicks
_WanX25PvcStatsUpTime_Object=MibTableColumn
wanX25PvcStatsUpTime=_WanX25PvcStatsUpTime_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,1,1,15),_WanX25PvcStatsUpTime_Type())
wanX25PvcStatsUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcStatsUpTime.setStatus(_A)
_WanX25PvcStatsDownTime_Type=TimeTicks
_WanX25PvcStatsDownTime_Object=MibTableColumn
wanX25PvcStatsDownTime=_WanX25PvcStatsDownTime_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,1,1,16),_WanX25PvcStatsDownTime_Type())
wanX25PvcStatsDownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcStatsDownTime.setStatus(_A)
class _WanX25PvcStatsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),(_I,2),(_J,3)))
_WanX25PvcStatsState_Type.__name__=_C
_WanX25PvcStatsState_Object=MibTableColumn
wanX25PvcStatsState=_WanX25PvcStatsState_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,1,1,17),_WanX25PvcStatsState_Type())
wanX25PvcStatsState.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcStatsState.setStatus(_A)
_WanX25PvcStatsStateChanges_Type=Counter64
_WanX25PvcStatsStateChanges_Object=MibTableColumn
wanX25PvcStatsStateChanges=_WanX25PvcStatsStateChanges_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,1,1,18),_WanX25PvcStatsStateChanges_Type())
wanX25PvcStatsStateChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcStatsStateChanges.setStatus(_A)
_WanX25PvcStatsOwner_Type=OwnerString
_WanX25PvcStatsOwner_Object=MibTableColumn
wanX25PvcStatsOwner=_WanX25PvcStatsOwner_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,1,1,19),_WanX25PvcStatsOwner_Type())
wanX25PvcStatsOwner.setMaxAccess(_G)
if mibBuilder.loadTexts:wanX25PvcStatsOwner.setStatus(_A)
_WanX25PvcStatsStatus_Type=RowStatus
_WanX25PvcStatsStatus_Object=MibTableColumn
wanX25PvcStatsStatus=_WanX25PvcStatsStatus_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,1,1,20),_WanX25PvcStatsStatus_Type())
wanX25PvcStatsStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wanX25PvcStatsStatus.setStatus(_A)
_WanFrPvcStatsTable_Object=MibTable
wanFrPvcStatsTable=_WanFrPvcStatsTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,2))
if mibBuilder.loadTexts:wanFrPvcStatsTable.setStatus(_A)
_WanFrPvcStatsEntry_Object=MibTableRow
wanFrPvcStatsEntry=_WanFrPvcStatsEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,2,1))
wanFrPvcStatsEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:wanFrPvcStatsEntry.setStatus(_A)
class _WanFrPvcStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanFrPvcStatsIndex_Type.__name__=_C
_WanFrPvcStatsIndex_Object=MibTableColumn
wanFrPvcStatsIndex=_WanFrPvcStatsIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,2,1,1),_WanFrPvcStatsIndex_Type())
wanFrPvcStatsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanFrPvcStatsIndex.setStatus(_A)
_WanFrPvcStatsDataSource_Type=ObjectIdentifier
_WanFrPvcStatsDataSource_Object=MibTableColumn
wanFrPvcStatsDataSource=_WanFrPvcStatsDataSource_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,2,1,2),_WanFrPvcStatsDataSource_Type())
wanFrPvcStatsDataSource.setMaxAccess(_G)
if mibBuilder.loadTexts:wanFrPvcStatsDataSource.setStatus(_A)
_WanFrPvcStatsDropEvents_Type=Counter64
_WanFrPvcStatsDropEvents_Object=MibTableColumn
wanFrPvcStatsDropEvents=_WanFrPvcStatsDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,2,1,3),_WanFrPvcStatsDropEvents_Type())
wanFrPvcStatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcStatsDropEvents.setStatus(_A)
_WanFrPvcStatsInFrames_Type=Counter64
_WanFrPvcStatsInFrames_Object=MibTableColumn
wanFrPvcStatsInFrames=_WanFrPvcStatsInFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,2,1,4),_WanFrPvcStatsInFrames_Type())
wanFrPvcStatsInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcStatsInFrames.setStatus(_A)
_WanFrPvcStatsOutFrames_Type=Counter64
_WanFrPvcStatsOutFrames_Object=MibTableColumn
wanFrPvcStatsOutFrames=_WanFrPvcStatsOutFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,2,1,5),_WanFrPvcStatsOutFrames_Type())
wanFrPvcStatsOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcStatsOutFrames.setStatus(_A)
_WanFrPvcStatsInOctets_Type=Counter64
_WanFrPvcStatsInOctets_Object=MibTableColumn
wanFrPvcStatsInOctets=_WanFrPvcStatsInOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,2,1,6),_WanFrPvcStatsInOctets_Type())
wanFrPvcStatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcStatsInOctets.setStatus(_A)
_WanFrPvcStatsOutOctets_Type=Counter64
_WanFrPvcStatsOutOctets_Object=MibTableColumn
wanFrPvcStatsOutOctets=_WanFrPvcStatsOutOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,2,1,7),_WanFrPvcStatsOutOctets_Type())
wanFrPvcStatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcStatsOutOctets.setStatus(_A)
_WanFrPvcStatsInFECNs_Type=Counter64
_WanFrPvcStatsInFECNs_Object=MibTableColumn
wanFrPvcStatsInFECNs=_WanFrPvcStatsInFECNs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,2,1,8),_WanFrPvcStatsInFECNs_Type())
wanFrPvcStatsInFECNs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcStatsInFECNs.setStatus(_A)
_WanFrPvcStatsOutFECNs_Type=Counter64
_WanFrPvcStatsOutFECNs_Object=MibTableColumn
wanFrPvcStatsOutFECNs=_WanFrPvcStatsOutFECNs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,2,1,9),_WanFrPvcStatsOutFECNs_Type())
wanFrPvcStatsOutFECNs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcStatsOutFECNs.setStatus(_A)
_WanFrPvcStatsInBECNs_Type=Counter64
_WanFrPvcStatsInBECNs_Object=MibTableColumn
wanFrPvcStatsInBECNs=_WanFrPvcStatsInBECNs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,2,1,10),_WanFrPvcStatsInBECNs_Type())
wanFrPvcStatsInBECNs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcStatsInBECNs.setStatus(_A)
_WanFrPvcStatsOutBECNs_Type=Counter64
_WanFrPvcStatsOutBECNs_Object=MibTableColumn
wanFrPvcStatsOutBECNs=_WanFrPvcStatsOutBECNs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,2,1,11),_WanFrPvcStatsOutBECNs_Type())
wanFrPvcStatsOutBECNs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcStatsOutBECNs.setStatus(_A)
_WanFrPvcStatsInDEs_Type=Counter64
_WanFrPvcStatsInDEs_Object=MibTableColumn
wanFrPvcStatsInDEs=_WanFrPvcStatsInDEs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,2,1,12),_WanFrPvcStatsInDEs_Type())
wanFrPvcStatsInDEs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcStatsInDEs.setStatus(_A)
_WanFrPvcStatsOutDEs_Type=Counter64
_WanFrPvcStatsOutDEs_Object=MibTableColumn
wanFrPvcStatsOutDEs=_WanFrPvcStatsOutDEs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,2,1,13),_WanFrPvcStatsOutDEs_Type())
wanFrPvcStatsOutDEs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcStatsOutDEs.setStatus(_A)
_WanFrPvcStatsUpTime_Type=TimeTicks
_WanFrPvcStatsUpTime_Object=MibTableColumn
wanFrPvcStatsUpTime=_WanFrPvcStatsUpTime_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,2,1,14),_WanFrPvcStatsUpTime_Type())
wanFrPvcStatsUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcStatsUpTime.setStatus(_A)
_WanFrPvcStatsDownTime_Type=TimeTicks
_WanFrPvcStatsDownTime_Object=MibTableColumn
wanFrPvcStatsDownTime=_WanFrPvcStatsDownTime_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,2,1,15),_WanFrPvcStatsDownTime_Type())
wanFrPvcStatsDownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcStatsDownTime.setStatus(_A)
class _WanFrPvcStatsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),(_I,2),(_J,3)))
_WanFrPvcStatsState_Type.__name__=_C
_WanFrPvcStatsState_Object=MibTableColumn
wanFrPvcStatsState=_WanFrPvcStatsState_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,2,1,16),_WanFrPvcStatsState_Type())
wanFrPvcStatsState.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcStatsState.setStatus(_A)
_WanFrPvcStatsStateChanges_Type=Counter64
_WanFrPvcStatsStateChanges_Object=MibTableColumn
wanFrPvcStatsStateChanges=_WanFrPvcStatsStateChanges_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,2,1,17),_WanFrPvcStatsStateChanges_Type())
wanFrPvcStatsStateChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcStatsStateChanges.setStatus(_A)
_WanFrPvcStatsOwner_Type=OwnerString
_WanFrPvcStatsOwner_Object=MibTableColumn
wanFrPvcStatsOwner=_WanFrPvcStatsOwner_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,2,1,18),_WanFrPvcStatsOwner_Type())
wanFrPvcStatsOwner.setMaxAccess(_G)
if mibBuilder.loadTexts:wanFrPvcStatsOwner.setStatus(_A)
_WanFrPvcStatsStatus_Type=RowStatus
_WanFrPvcStatsStatus_Object=MibTableColumn
wanFrPvcStatsStatus=_WanFrPvcStatsStatus_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,2,1,19),_WanFrPvcStatsStatus_Type())
wanFrPvcStatsStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wanFrPvcStatsStatus.setStatus(_A)
_WanAal5PvcStatsTable_Object=MibTable
wanAal5PvcStatsTable=_WanAal5PvcStatsTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3))
if mibBuilder.loadTexts:wanAal5PvcStatsTable.setStatus(_A)
_WanAal5PvcStatsEntry_Object=MibTableRow
wanAal5PvcStatsEntry=_WanAal5PvcStatsEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3,1))
wanAal5PvcStatsEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:wanAal5PvcStatsEntry.setStatus(_A)
class _WanAal5PvcStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanAal5PvcStatsIndex_Type.__name__=_C
_WanAal5PvcStatsIndex_Object=MibTableColumn
wanAal5PvcStatsIndex=_WanAal5PvcStatsIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3,1,1),_WanAal5PvcStatsIndex_Type())
wanAal5PvcStatsIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanAal5PvcStatsIndex.setStatus(_A)
_WanAal5PvcStatsDataSource_Type=ObjectIdentifier
_WanAal5PvcStatsDataSource_Object=MibTableColumn
wanAal5PvcStatsDataSource=_WanAal5PvcStatsDataSource_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3,1,2),_WanAal5PvcStatsDataSource_Type())
wanAal5PvcStatsDataSource.setMaxAccess(_G)
if mibBuilder.loadTexts:wanAal5PvcStatsDataSource.setStatus(_A)
_WanAal5PvcStatsDropEvents_Type=Counter64
_WanAal5PvcStatsDropEvents_Object=MibTableColumn
wanAal5PvcStatsDropEvents=_WanAal5PvcStatsDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3,1,3),_WanAal5PvcStatsDropEvents_Type())
wanAal5PvcStatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcStatsDropEvents.setStatus(_A)
_WanAal5PvcStatsInCells_Type=Counter64
_WanAal5PvcStatsInCells_Object=MibTableColumn
wanAal5PvcStatsInCells=_WanAal5PvcStatsInCells_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3,1,4),_WanAal5PvcStatsInCells_Type())
wanAal5PvcStatsInCells.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcStatsInCells.setStatus(_A)
_WanAal5PvcStatsOutCells_Type=Counter64
_WanAal5PvcStatsOutCells_Object=MibTableColumn
wanAal5PvcStatsOutCells=_WanAal5PvcStatsOutCells_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3,1,5),_WanAal5PvcStatsOutCells_Type())
wanAal5PvcStatsOutCells.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcStatsOutCells.setStatus(_A)
_WanAal5PvcStatsInPDUs_Type=Counter64
_WanAal5PvcStatsInPDUs_Object=MibTableColumn
wanAal5PvcStatsInPDUs=_WanAal5PvcStatsInPDUs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3,1,6),_WanAal5PvcStatsInPDUs_Type())
wanAal5PvcStatsInPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcStatsInPDUs.setStatus(_A)
_WanAal5PvcStatsOutPDUs_Type=Counter64
_WanAal5PvcStatsOutPDUs_Object=MibTableColumn
wanAal5PvcStatsOutPDUs=_WanAal5PvcStatsOutPDUs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3,1,7),_WanAal5PvcStatsOutPDUs_Type())
wanAal5PvcStatsOutPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcStatsOutPDUs.setStatus(_A)
_WanAal5PvcStatsInOctets_Type=Counter64
_WanAal5PvcStatsInOctets_Object=MibTableColumn
wanAal5PvcStatsInOctets=_WanAal5PvcStatsInOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3,1,8),_WanAal5PvcStatsInOctets_Type())
wanAal5PvcStatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcStatsInOctets.setStatus(_A)
_WanAal5PvcStatsOutOctets_Type=Counter64
_WanAal5PvcStatsOutOctets_Object=MibTableColumn
wanAal5PvcStatsOutOctets=_WanAal5PvcStatsOutOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3,1,9),_WanAal5PvcStatsOutOctets_Type())
wanAal5PvcStatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcStatsOutOctets.setStatus(_A)
_WanAal5PvcStatsInCLP1_Type=Counter64
_WanAal5PvcStatsInCLP1_Object=MibTableColumn
wanAal5PvcStatsInCLP1=_WanAal5PvcStatsInCLP1_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3,1,10),_WanAal5PvcStatsInCLP1_Type())
wanAal5PvcStatsInCLP1.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcStatsInCLP1.setStatus(_A)
_WanAal5PvcStatsOutCLP1_Type=Counter64
_WanAal5PvcStatsOutCLP1_Object=MibTableColumn
wanAal5PvcStatsOutCLP1=_WanAal5PvcStatsOutCLP1_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3,1,11),_WanAal5PvcStatsOutCLP1_Type())
wanAal5PvcStatsOutCLP1.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcStatsOutCLP1.setStatus(_A)
_WanAal5PvcStatsInCRCs_Type=Counter64
_WanAal5PvcStatsInCRCs_Object=MibTableColumn
wanAal5PvcStatsInCRCs=_WanAal5PvcStatsInCRCs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3,1,12),_WanAal5PvcStatsInCRCs_Type())
wanAal5PvcStatsInCRCs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcStatsInCRCs.setStatus(_A)
_WanAal5PvcStatsOutCRCs_Type=Counter64
_WanAal5PvcStatsOutCRCs_Object=MibTableColumn
wanAal5PvcStatsOutCRCs=_WanAal5PvcStatsOutCRCs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3,1,13),_WanAal5PvcStatsOutCRCs_Type())
wanAal5PvcStatsOutCRCs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcStatsOutCRCs.setStatus(_A)
_WanAal5PvcStatsInOversizedSDUs_Type=Counter64
_WanAal5PvcStatsInOversizedSDUs_Object=MibTableColumn
wanAal5PvcStatsInOversizedSDUs=_WanAal5PvcStatsInOversizedSDUs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3,1,14),_WanAal5PvcStatsInOversizedSDUs_Type())
wanAal5PvcStatsInOversizedSDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcStatsInOversizedSDUs.setStatus(_A)
_WanAal5PvcStatsOutOversizedSDUs_Type=Counter64
_WanAal5PvcStatsOutOversizedSDUs_Object=MibTableColumn
wanAal5PvcStatsOutOversizedSDUs=_WanAal5PvcStatsOutOversizedSDUs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3,1,15),_WanAal5PvcStatsOutOversizedSDUs_Type())
wanAal5PvcStatsOutOversizedSDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcStatsOutOversizedSDUs.setStatus(_A)
_WanAal5PvcStatsUpTime_Type=TimeTicks
_WanAal5PvcStatsUpTime_Object=MibTableColumn
wanAal5PvcStatsUpTime=_WanAal5PvcStatsUpTime_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3,1,16),_WanAal5PvcStatsUpTime_Type())
wanAal5PvcStatsUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcStatsUpTime.setStatus(_A)
_WanAal5PvcStatsDownTime_Type=TimeTicks
_WanAal5PvcStatsDownTime_Object=MibTableColumn
wanAal5PvcStatsDownTime=_WanAal5PvcStatsDownTime_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3,1,17),_WanAal5PvcStatsDownTime_Type())
wanAal5PvcStatsDownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcStatsDownTime.setStatus(_A)
class _WanAal5PvcStatsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),(_I,2),(_J,3)))
_WanAal5PvcStatsState_Type.__name__=_C
_WanAal5PvcStatsState_Object=MibTableColumn
wanAal5PvcStatsState=_WanAal5PvcStatsState_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3,1,18),_WanAal5PvcStatsState_Type())
wanAal5PvcStatsState.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcStatsState.setStatus(_A)
_WanAal5PvcStatsStateChanges_Type=Counter64
_WanAal5PvcStatsStateChanges_Object=MibTableColumn
wanAal5PvcStatsStateChanges=_WanAal5PvcStatsStateChanges_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3,1,19),_WanAal5PvcStatsStateChanges_Type())
wanAal5PvcStatsStateChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcStatsStateChanges.setStatus(_A)
_WanAal5PvcStatsOwner_Type=OwnerString
_WanAal5PvcStatsOwner_Object=MibTableColumn
wanAal5PvcStatsOwner=_WanAal5PvcStatsOwner_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3,1,20),_WanAal5PvcStatsOwner_Type())
wanAal5PvcStatsOwner.setMaxAccess(_G)
if mibBuilder.loadTexts:wanAal5PvcStatsOwner.setStatus(_A)
_WanAal5PvcStatsStatus_Type=RowStatus
_WanAal5PvcStatsStatus_Object=MibTableColumn
wanAal5PvcStatsStatus=_WanAal5PvcStatsStatus_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,1,3,3,1,21),_WanAal5PvcStatsStatus_Type())
wanAal5PvcStatsStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wanAal5PvcStatsStatus.setStatus(_A)
_WanHistoryMIBObjects_ObjectIdentity=ObjectIdentity
wanHistoryMIBObjects=_WanHistoryMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2))
_WanSignalingHistory_ObjectIdentity=ObjectIdentity
wanSignalingHistory=_WanSignalingHistory_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1))
_WanT1E1HistoryTable_Object=MibTable
wanT1E1HistoryTable=_WanT1E1HistoryTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1))
if mibBuilder.loadTexts:wanT1E1HistoryTable.setStatus(_A)
_WanT1E1HistoryEntry_Object=MibTableRow
wanT1E1HistoryEntry=_WanT1E1HistoryEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1))
wanT1E1HistoryEntry.setIndexNames((0,_E,_U),(0,_E,_V))
if mibBuilder.loadTexts:wanT1E1HistoryEntry.setStatus(_A)
class _WanT1E1HistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanT1E1HistoryIndex_Type.__name__=_C
_WanT1E1HistoryIndex_Object=MibTableColumn
wanT1E1HistoryIndex=_WanT1E1HistoryIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,1),_WanT1E1HistoryIndex_Type())
wanT1E1HistoryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanT1E1HistoryIndex.setStatus(_A)
class _WanT1E1HistorySampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WanT1E1HistorySampleIndex_Type.__name__=_C
_WanT1E1HistorySampleIndex_Object=MibTableColumn
wanT1E1HistorySampleIndex=_WanT1E1HistorySampleIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,2),_WanT1E1HistorySampleIndex_Type())
wanT1E1HistorySampleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanT1E1HistorySampleIndex.setStatus(_A)
_WanT1E1HistoryIntervalStart_Type=TimeTicks
_WanT1E1HistoryIntervalStart_Object=MibTableColumn
wanT1E1HistoryIntervalStart=_WanT1E1HistoryIntervalStart_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,3),_WanT1E1HistoryIntervalStart_Type())
wanT1E1HistoryIntervalStart.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryIntervalStart.setStatus(_A)
_WanT1E1HistoryDropEvents_Type=Counter64
_WanT1E1HistoryDropEvents_Object=MibTableColumn
wanT1E1HistoryDropEvents=_WanT1E1HistoryDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,4),_WanT1E1HistoryDropEvents_Type())
wanT1E1HistoryDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryDropEvents.setStatus(_A)
_WanT1E1HistoryInFrames_Type=Counter64
_WanT1E1HistoryInFrames_Object=MibTableColumn
wanT1E1HistoryInFrames=_WanT1E1HistoryInFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,5),_WanT1E1HistoryInFrames_Type())
wanT1E1HistoryInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryInFrames.setStatus(_A)
_WanT1E1HistoryOutFrames_Type=Counter64
_WanT1E1HistoryOutFrames_Object=MibTableColumn
wanT1E1HistoryOutFrames=_WanT1E1HistoryOutFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,6),_WanT1E1HistoryOutFrames_Type())
wanT1E1HistoryOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryOutFrames.setStatus(_A)
_WanT1E1HistoryInOctets_Type=Counter64
_WanT1E1HistoryInOctets_Object=MibTableColumn
wanT1E1HistoryInOctets=_WanT1E1HistoryInOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,7),_WanT1E1HistoryInOctets_Type())
wanT1E1HistoryInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryInOctets.setStatus(_A)
_WanT1E1HistoryOutOctets_Type=Counter64
_WanT1E1HistoryOutOctets_Object=MibTableColumn
wanT1E1HistoryOutOctets=_WanT1E1HistoryOutOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,8),_WanT1E1HistoryOutOctets_Type())
wanT1E1HistoryOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryOutOctets.setStatus(_A)
_WanT1E1HistoryESs_Type=Counter64
_WanT1E1HistoryESs_Object=MibTableColumn
wanT1E1HistoryESs=_WanT1E1HistoryESs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,9),_WanT1E1HistoryESs_Type())
wanT1E1HistoryESs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryESs.setStatus(_A)
_WanT1E1HistorySESs_Type=Counter64
_WanT1E1HistorySESs_Object=MibTableColumn
wanT1E1HistorySESs=_WanT1E1HistorySESs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,10),_WanT1E1HistorySESs_Type())
wanT1E1HistorySESs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistorySESs.setStatus(_A)
_WanT1E1HistorySEFSs_Type=Counter64
_WanT1E1HistorySEFSs_Object=MibTableColumn
wanT1E1HistorySEFSs=_WanT1E1HistorySEFSs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,11),_WanT1E1HistorySEFSs_Type())
wanT1E1HistorySEFSs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistorySEFSs.setStatus(_A)
_WanT1E1HistoryOOFs_Type=Counter64
_WanT1E1HistoryOOFs_Object=MibTableColumn
wanT1E1HistoryOOFs=_WanT1E1HistoryOOFs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,12),_WanT1E1HistoryOOFs_Type())
wanT1E1HistoryOOFs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryOOFs.setStatus(_A)
_WanT1E1HistoryUASs_Type=Counter64
_WanT1E1HistoryUASs_Object=MibTableColumn
wanT1E1HistoryUASs=_WanT1E1HistoryUASs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,13),_WanT1E1HistoryUASs_Type())
wanT1E1HistoryUASs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryUASs.setStatus(_A)
_WanT1E1HistoryCSSs_Type=Counter64
_WanT1E1HistoryCSSs_Object=MibTableColumn
wanT1E1HistoryCSSs=_WanT1E1HistoryCSSs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,14),_WanT1E1HistoryCSSs_Type())
wanT1E1HistoryCSSs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryCSSs.setStatus(_A)
_WanT1E1HistoryPCVs_Type=Counter64
_WanT1E1HistoryPCVs_Object=MibTableColumn
wanT1E1HistoryPCVs=_WanT1E1HistoryPCVs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,15),_WanT1E1HistoryPCVs_Type())
wanT1E1HistoryPCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryPCVs.setStatus(_A)
_WanT1E1HistoryLESs_Type=Counter64
_WanT1E1HistoryLESs_Object=MibTableColumn
wanT1E1HistoryLESs=_WanT1E1HistoryLESs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,16),_WanT1E1HistoryLESs_Type())
wanT1E1HistoryLESs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryLESs.setStatus(_A)
_WanT1E1HistoryBESs_Type=Counter64
_WanT1E1HistoryBESs_Object=MibTableColumn
wanT1E1HistoryBESs=_WanT1E1HistoryBESs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,17),_WanT1E1HistoryBESs_Type())
wanT1E1HistoryBESs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryBESs.setStatus(_A)
_WanT1E1HistoryDMs_Type=Counter64
_WanT1E1HistoryDMs_Object=MibTableColumn
wanT1E1HistoryDMs=_WanT1E1HistoryDMs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,18),_WanT1E1HistoryDMs_Type())
wanT1E1HistoryDMs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryDMs.setStatus(_A)
_WanT1E1HistoryLCVs_Type=Counter64
_WanT1E1HistoryLCVs_Object=MibTableColumn
wanT1E1HistoryLCVs=_WanT1E1HistoryLCVs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,19),_WanT1E1HistoryLCVs_Type())
wanT1E1HistoryLCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryLCVs.setStatus(_A)
_WanT1E1HistoryLOFs_Type=Counter64
_WanT1E1HistoryLOFs_Object=MibTableColumn
wanT1E1HistoryLOFs=_WanT1E1HistoryLOFs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,20),_WanT1E1HistoryLOFs_Type())
wanT1E1HistoryLOFs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryLOFs.setStatus(_A)
_WanT1E1HistoryLOSs_Type=Counter64
_WanT1E1HistoryLOSs_Object=MibTableColumn
wanT1E1HistoryLOSs=_WanT1E1HistoryLOSs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,21),_WanT1E1HistoryLOSs_Type())
wanT1E1HistoryLOSs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryLOSs.setStatus(_A)
_WanT1E1HistoryRAIs_Type=Counter64
_WanT1E1HistoryRAIs_Object=MibTableColumn
wanT1E1HistoryRAIs=_WanT1E1HistoryRAIs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,22),_WanT1E1HistoryRAIs_Type())
wanT1E1HistoryRAIs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryRAIs.setStatus(_A)
_WanT1E1HistoryAISs_Type=Counter64
_WanT1E1HistoryAISs_Object=MibTableColumn
wanT1E1HistoryAISs=_WanT1E1HistoryAISs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,23),_WanT1E1HistoryAISs_Type())
wanT1E1HistoryAISs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryAISs.setStatus(_A)
_WanT1E1HistoryTS16AISs_Type=Counter64
_WanT1E1HistoryTS16AISs_Object=MibTableColumn
wanT1E1HistoryTS16AISs=_WanT1E1HistoryTS16AISs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,24),_WanT1E1HistoryTS16AISs_Type())
wanT1E1HistoryTS16AISs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryTS16AISs.setStatus(_A)
_WanT1E1HistoryLOMFs_Type=Counter64
_WanT1E1HistoryLOMFs_Object=MibTableColumn
wanT1E1HistoryLOMFs=_WanT1E1HistoryLOMFs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,25),_WanT1E1HistoryLOMFs_Type())
wanT1E1HistoryLOMFs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryLOMFs.setStatus(_A)
_WanT1E1HistoryFarLOMFs_Type=Counter64
_WanT1E1HistoryFarLOMFs_Object=MibTableColumn
wanT1E1HistoryFarLOMFs=_WanT1E1HistoryFarLOMFs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,26),_WanT1E1HistoryFarLOMFs_Type())
wanT1E1HistoryFarLOMFs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryFarLOMFs.setStatus(_A)
class _WanT1E1HistoryInUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanT1E1HistoryInUtilization_Type.__name__=_C
_WanT1E1HistoryInUtilization_Object=MibTableColumn
wanT1E1HistoryInUtilization=_WanT1E1HistoryInUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,27),_WanT1E1HistoryInUtilization_Type())
wanT1E1HistoryInUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryInUtilization.setStatus(_A)
class _WanT1E1HistoryOutUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanT1E1HistoryOutUtilization_Type.__name__=_C
_WanT1E1HistoryOutUtilization_Object=MibTableColumn
wanT1E1HistoryOutUtilization=_WanT1E1HistoryOutUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,1,1,28),_WanT1E1HistoryOutUtilization_Type())
wanT1E1HistoryOutUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT1E1HistoryOutUtilization.setStatus(_A)
_WanVSeriesHistoryTable_Object=MibTable
wanVSeriesHistoryTable=_WanVSeriesHistoryTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,2))
if mibBuilder.loadTexts:wanVSeriesHistoryTable.setStatus(_A)
_WanVSeriesHistoryEntry_Object=MibTableRow
wanVSeriesHistoryEntry=_WanVSeriesHistoryEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,2,1))
wanVSeriesHistoryEntry.setIndexNames((0,_E,_W),(0,_E,_X))
if mibBuilder.loadTexts:wanVSeriesHistoryEntry.setStatus(_A)
class _WanVSeriesHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanVSeriesHistoryIndex_Type.__name__=_C
_WanVSeriesHistoryIndex_Object=MibTableColumn
wanVSeriesHistoryIndex=_WanVSeriesHistoryIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,2,1,1),_WanVSeriesHistoryIndex_Type())
wanVSeriesHistoryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanVSeriesHistoryIndex.setStatus(_A)
class _WanVSeriesHistorySampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WanVSeriesHistorySampleIndex_Type.__name__=_C
_WanVSeriesHistorySampleIndex_Object=MibTableColumn
wanVSeriesHistorySampleIndex=_WanVSeriesHistorySampleIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,2,1,2),_WanVSeriesHistorySampleIndex_Type())
wanVSeriesHistorySampleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanVSeriesHistorySampleIndex.setStatus(_A)
_WanVSeriesHistoryIntervalStart_Type=TimeTicks
_WanVSeriesHistoryIntervalStart_Object=MibTableColumn
wanVSeriesHistoryIntervalStart=_WanVSeriesHistoryIntervalStart_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,2,1,3),_WanVSeriesHistoryIntervalStart_Type())
wanVSeriesHistoryIntervalStart.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesHistoryIntervalStart.setStatus(_A)
_WanVSeriesHistoryDropEvents_Type=Counter64
_WanVSeriesHistoryDropEvents_Object=MibTableColumn
wanVSeriesHistoryDropEvents=_WanVSeriesHistoryDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,2,1,4),_WanVSeriesHistoryDropEvents_Type())
wanVSeriesHistoryDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesHistoryDropEvents.setStatus(_A)
_WanVSeriesHistoryInFrames_Type=Counter64
_WanVSeriesHistoryInFrames_Object=MibTableColumn
wanVSeriesHistoryInFrames=_WanVSeriesHistoryInFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,2,1,5),_WanVSeriesHistoryInFrames_Type())
wanVSeriesHistoryInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesHistoryInFrames.setStatus(_A)
_WanVSeriesHistoryOutFrames_Type=Counter64
_WanVSeriesHistoryOutFrames_Object=MibTableColumn
wanVSeriesHistoryOutFrames=_WanVSeriesHistoryOutFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,2,1,6),_WanVSeriesHistoryOutFrames_Type())
wanVSeriesHistoryOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesHistoryOutFrames.setStatus(_A)
_WanVSeriesHistoryInOctets_Type=Counter64
_WanVSeriesHistoryInOctets_Object=MibTableColumn
wanVSeriesHistoryInOctets=_WanVSeriesHistoryInOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,2,1,7),_WanVSeriesHistoryInOctets_Type())
wanVSeriesHistoryInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesHistoryInOctets.setStatus(_A)
_WanVSeriesHistoryOutOctets_Type=Counter64
_WanVSeriesHistoryOutOctets_Object=MibTableColumn
wanVSeriesHistoryOutOctets=_WanVSeriesHistoryOutOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,2,1,8),_WanVSeriesHistoryOutOctets_Type())
wanVSeriesHistoryOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesHistoryOutOctets.setStatus(_A)
_WanVSeriesHistoryInFCSs_Type=Counter64
_WanVSeriesHistoryInFCSs_Object=MibTableColumn
wanVSeriesHistoryInFCSs=_WanVSeriesHistoryInFCSs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,2,1,9),_WanVSeriesHistoryInFCSs_Type())
wanVSeriesHistoryInFCSs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesHistoryInFCSs.setStatus(_A)
_WanVSeriesHistoryOutFCSs_Type=Counter64
_WanVSeriesHistoryOutFCSs_Object=MibTableColumn
wanVSeriesHistoryOutFCSs=_WanVSeriesHistoryOutFCSs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,2,1,10),_WanVSeriesHistoryOutFCSs_Type())
wanVSeriesHistoryOutFCSs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesHistoryOutFCSs.setStatus(_A)
_WanVSeriesHistoryInOverruns_Type=Counter64
_WanVSeriesHistoryInOverruns_Object=MibTableColumn
wanVSeriesHistoryInOverruns=_WanVSeriesHistoryInOverruns_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,2,1,11),_WanVSeriesHistoryInOverruns_Type())
wanVSeriesHistoryInOverruns.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesHistoryInOverruns.setStatus(_A)
_WanVSeriesHistoryOutOverruns_Type=Counter64
_WanVSeriesHistoryOutOverruns_Object=MibTableColumn
wanVSeriesHistoryOutOverruns=_WanVSeriesHistoryOutOverruns_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,2,1,12),_WanVSeriesHistoryOutOverruns_Type())
wanVSeriesHistoryOutOverruns.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesHistoryOutOverruns.setStatus(_A)
_WanVSeriesHistoryInterruptedFrames_Type=Counter64
_WanVSeriesHistoryInterruptedFrames_Object=MibTableColumn
wanVSeriesHistoryInterruptedFrames=_WanVSeriesHistoryInterruptedFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,2,1,13),_WanVSeriesHistoryInterruptedFrames_Type())
wanVSeriesHistoryInterruptedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesHistoryInterruptedFrames.setStatus(_A)
_WanVSeriesHistoryInAbortedFrames_Type=Counter64
_WanVSeriesHistoryInAbortedFrames_Object=MibTableColumn
wanVSeriesHistoryInAbortedFrames=_WanVSeriesHistoryInAbortedFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,2,1,14),_WanVSeriesHistoryInAbortedFrames_Type())
wanVSeriesHistoryInAbortedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesHistoryInAbortedFrames.setStatus(_A)
_WanVSeriesHistoryOutAbortedFrames_Type=Counter64
_WanVSeriesHistoryOutAbortedFrames_Object=MibTableColumn
wanVSeriesHistoryOutAbortedFrames=_WanVSeriesHistoryOutAbortedFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,2,1,15),_WanVSeriesHistoryOutAbortedFrames_Type())
wanVSeriesHistoryOutAbortedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesHistoryOutAbortedFrames.setStatus(_A)
class _WanVSeriesHistoryInUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanVSeriesHistoryInUtilization_Type.__name__=_C
_WanVSeriesHistoryInUtilization_Object=MibTableColumn
wanVSeriesHistoryInUtilization=_WanVSeriesHistoryInUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,2,1,16),_WanVSeriesHistoryInUtilization_Type())
wanVSeriesHistoryInUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesHistoryInUtilization.setStatus(_A)
class _WanVSeriesHistoryOutUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanVSeriesHistoryOutUtilization_Type.__name__=_C
_WanVSeriesHistoryOutUtilization_Object=MibTableColumn
wanVSeriesHistoryOutUtilization=_WanVSeriesHistoryOutUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,2,1,17),_WanVSeriesHistoryOutUtilization_Type())
wanVSeriesHistoryOutUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanVSeriesHistoryOutUtilization.setStatus(_A)
_WanHssiHistoryTable_Object=MibTable
wanHssiHistoryTable=_WanHssiHistoryTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3))
if mibBuilder.loadTexts:wanHssiHistoryTable.setStatus(_D)
_WanHssiHistoryEntry_Object=MibTableRow
wanHssiHistoryEntry=_WanHssiHistoryEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3,1))
wanHssiHistoryEntry.setIndexNames((0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:wanHssiHistoryEntry.setStatus(_D)
class _WanHssiHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanHssiHistoryIndex_Type.__name__=_C
_WanHssiHistoryIndex_Object=MibTableColumn
wanHssiHistoryIndex=_WanHssiHistoryIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3,1,1),_WanHssiHistoryIndex_Type())
wanHssiHistoryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanHssiHistoryIndex.setStatus(_D)
class _WanHssiHistorySampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WanHssiHistorySampleIndex_Type.__name__=_C
_WanHssiHistorySampleIndex_Object=MibTableColumn
wanHssiHistorySampleIndex=_WanHssiHistorySampleIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3,1,2),_WanHssiHistorySampleIndex_Type())
wanHssiHistorySampleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanHssiHistorySampleIndex.setStatus(_D)
_WanHssiHistoryIntervalStart_Type=TimeTicks
_WanHssiHistoryIntervalStart_Object=MibTableColumn
wanHssiHistoryIntervalStart=_WanHssiHistoryIntervalStart_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3,1,3),_WanHssiHistoryIntervalStart_Type())
wanHssiHistoryIntervalStart.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiHistoryIntervalStart.setStatus(_D)
_WanHssiHistoryDropEvents_Type=Counter64
_WanHssiHistoryDropEvents_Object=MibTableColumn
wanHssiHistoryDropEvents=_WanHssiHistoryDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3,1,4),_WanHssiHistoryDropEvents_Type())
wanHssiHistoryDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiHistoryDropEvents.setStatus(_D)
_WanHssiHistoryInFrames_Type=Counter64
_WanHssiHistoryInFrames_Object=MibTableColumn
wanHssiHistoryInFrames=_WanHssiHistoryInFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3,1,5),_WanHssiHistoryInFrames_Type())
wanHssiHistoryInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiHistoryInFrames.setStatus(_D)
_WanHssiHistoryOutFrames_Type=Counter64
_WanHssiHistoryOutFrames_Object=MibTableColumn
wanHssiHistoryOutFrames=_WanHssiHistoryOutFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3,1,6),_WanHssiHistoryOutFrames_Type())
wanHssiHistoryOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiHistoryOutFrames.setStatus(_D)
_WanHssiHistoryInOctets_Type=Counter64
_WanHssiHistoryInOctets_Object=MibTableColumn
wanHssiHistoryInOctets=_WanHssiHistoryInOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3,1,7),_WanHssiHistoryInOctets_Type())
wanHssiHistoryInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiHistoryInOctets.setStatus(_D)
_WanHssiHistoryOutOctets_Type=Counter64
_WanHssiHistoryOutOctets_Object=MibTableColumn
wanHssiHistoryOutOctets=_WanHssiHistoryOutOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3,1,8),_WanHssiHistoryOutOctets_Type())
wanHssiHistoryOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiHistoryOutOctets.setStatus(_D)
_WanHssiHistoryRxLongFrames_Type=Counter64
_WanHssiHistoryRxLongFrames_Object=MibTableColumn
wanHssiHistoryRxLongFrames=_WanHssiHistoryRxLongFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3,1,9),_WanHssiHistoryRxLongFrames_Type())
wanHssiHistoryRxLongFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiHistoryRxLongFrames.setStatus(_D)
_WanHssiHistoryRxCrcErrors_Type=Counter64
_WanHssiHistoryRxCrcErrors_Object=MibTableColumn
wanHssiHistoryRxCrcErrors=_WanHssiHistoryRxCrcErrors_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3,1,10),_WanHssiHistoryRxCrcErrors_Type())
wanHssiHistoryRxCrcErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiHistoryRxCrcErrors.setStatus(_D)
_WanHssiHistoryRxOverruns_Type=Counter64
_WanHssiHistoryRxOverruns_Object=MibTableColumn
wanHssiHistoryRxOverruns=_WanHssiHistoryRxOverruns_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3,1,11),_WanHssiHistoryRxOverruns_Type())
wanHssiHistoryRxOverruns.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiHistoryRxOverruns.setStatus(_D)
_WanHssiHistoryRxAborts_Type=Counter64
_WanHssiHistoryRxAborts_Object=MibTableColumn
wanHssiHistoryRxAborts=_WanHssiHistoryRxAborts_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3,1,12),_WanHssiHistoryRxAborts_Type())
wanHssiHistoryRxAborts.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiHistoryRxAborts.setStatus(_D)
_WanHssiHistoryTxAborts_Type=Counter64
_WanHssiHistoryTxAborts_Object=MibTableColumn
wanHssiHistoryTxAborts=_WanHssiHistoryTxAborts_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3,1,13),_WanHssiHistoryTxAborts_Type())
wanHssiHistoryTxAborts.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiHistoryTxAborts.setStatus(_D)
_WanHssiHistoryTxUnderruns_Type=Counter64
_WanHssiHistoryTxUnderruns_Object=MibTableColumn
wanHssiHistoryTxUnderruns=_WanHssiHistoryTxUnderruns_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3,1,14),_WanHssiHistoryTxUnderruns_Type())
wanHssiHistoryTxUnderruns.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiHistoryTxUnderruns.setStatus(_D)
_WanHssiHistoryRxRingErrors_Type=Counter64
_WanHssiHistoryRxRingErrors_Object=MibTableColumn
wanHssiHistoryRxRingErrors=_WanHssiHistoryRxRingErrors_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3,1,15),_WanHssiHistoryRxRingErrors_Type())
wanHssiHistoryRxRingErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiHistoryRxRingErrors.setStatus(_D)
_WanHssiHistoryRxRingOverruns_Type=Counter64
_WanHssiHistoryRxRingOverruns_Object=MibTableColumn
wanHssiHistoryRxRingOverruns=_WanHssiHistoryRxRingOverruns_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3,1,16),_WanHssiHistoryRxRingOverruns_Type())
wanHssiHistoryRxRingOverruns.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiHistoryRxRingOverruns.setStatus(_D)
_WanHssiHistoryTxRingErrors_Type=Counter64
_WanHssiHistoryTxRingErrors_Object=MibTableColumn
wanHssiHistoryTxRingErrors=_WanHssiHistoryTxRingErrors_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3,1,17),_WanHssiHistoryTxRingErrors_Type())
wanHssiHistoryTxRingErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiHistoryTxRingErrors.setStatus(_D)
_WanHssiHistoryPortOpErrors_Type=Counter64
_WanHssiHistoryPortOpErrors_Object=MibTableColumn
wanHssiHistoryPortOpErrors=_WanHssiHistoryPortOpErrors_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3,1,18),_WanHssiHistoryPortOpErrors_Type())
wanHssiHistoryPortOpErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiHistoryPortOpErrors.setStatus(_D)
_WanHssiHistoryTxCmplProcessings_Type=Counter64
_WanHssiHistoryTxCmplProcessings_Object=MibTableColumn
wanHssiHistoryTxCmplProcessings=_WanHssiHistoryTxCmplProcessings_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3,1,19),_WanHssiHistoryTxCmplProcessings_Type())
wanHssiHistoryTxCmplProcessings.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiHistoryTxCmplProcessings.setStatus(_D)
class _WanHssiHistoryInUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanHssiHistoryInUtilization_Type.__name__=_C
_WanHssiHistoryInUtilization_Object=MibTableColumn
wanHssiHistoryInUtilization=_WanHssiHistoryInUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3,1,20),_WanHssiHistoryInUtilization_Type())
wanHssiHistoryInUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiHistoryInUtilization.setStatus(_D)
class _WanHssiHistoryOutUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanHssiHistoryOutUtilization_Type.__name__=_C
_WanHssiHistoryOutUtilization_Object=MibTableColumn
wanHssiHistoryOutUtilization=_WanHssiHistoryOutUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,3,1,21),_WanHssiHistoryOutUtilization_Type())
wanHssiHistoryOutUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanHssiHistoryOutUtilization.setStatus(_D)
_WanT3E3HistoryTable_Object=MibTable
wanT3E3HistoryTable=_WanT3E3HistoryTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4))
if mibBuilder.loadTexts:wanT3E3HistoryTable.setStatus(_A)
_WanT3E3HistoryEntry_Object=MibTableRow
wanT3E3HistoryEntry=_WanT3E3HistoryEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1))
wanT3E3HistoryEntry.setIndexNames((0,_E,_a),(0,_E,_b))
if mibBuilder.loadTexts:wanT3E3HistoryEntry.setStatus(_A)
class _WanT3E3HistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanT3E3HistoryIndex_Type.__name__=_C
_WanT3E3HistoryIndex_Object=MibTableColumn
wanT3E3HistoryIndex=_WanT3E3HistoryIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,1),_WanT3E3HistoryIndex_Type())
wanT3E3HistoryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanT3E3HistoryIndex.setStatus(_A)
class _WanT3E3HistorySampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WanT3E3HistorySampleIndex_Type.__name__=_C
_WanT3E3HistorySampleIndex_Object=MibTableColumn
wanT3E3HistorySampleIndex=_WanT3E3HistorySampleIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,2),_WanT3E3HistorySampleIndex_Type())
wanT3E3HistorySampleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanT3E3HistorySampleIndex.setStatus(_A)
_WanT3E3HistoryIntervalStart_Type=TimeTicks
_WanT3E3HistoryIntervalStart_Object=MibTableColumn
wanT3E3HistoryIntervalStart=_WanT3E3HistoryIntervalStart_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,3),_WanT3E3HistoryIntervalStart_Type())
wanT3E3HistoryIntervalStart.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistoryIntervalStart.setStatus(_A)
_WanT3E3HistoryDropEvents_Type=Counter64
_WanT3E3HistoryDropEvents_Object=MibTableColumn
wanT3E3HistoryDropEvents=_WanT3E3HistoryDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,4),_WanT3E3HistoryDropEvents_Type())
wanT3E3HistoryDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistoryDropEvents.setStatus(_A)
_WanT3E3HistoryInFrames_Type=Counter64
_WanT3E3HistoryInFrames_Object=MibTableColumn
wanT3E3HistoryInFrames=_WanT3E3HistoryInFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,5),_WanT3E3HistoryInFrames_Type())
wanT3E3HistoryInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistoryInFrames.setStatus(_A)
_WanT3E3HistoryOutFrames_Type=Counter64
_WanT3E3HistoryOutFrames_Object=MibTableColumn
wanT3E3HistoryOutFrames=_WanT3E3HistoryOutFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,6),_WanT3E3HistoryOutFrames_Type())
wanT3E3HistoryOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistoryOutFrames.setStatus(_A)
_WanT3E3HistoryInOctets_Type=Counter64
_WanT3E3HistoryInOctets_Object=MibTableColumn
wanT3E3HistoryInOctets=_WanT3E3HistoryInOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,7),_WanT3E3HistoryInOctets_Type())
wanT3E3HistoryInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistoryInOctets.setStatus(_A)
_WanT3E3HistoryOutOctets_Type=Counter64
_WanT3E3HistoryOutOctets_Object=MibTableColumn
wanT3E3HistoryOutOctets=_WanT3E3HistoryOutOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,8),_WanT3E3HistoryOutOctets_Type())
wanT3E3HistoryOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistoryOutOctets.setStatus(_A)
_WanT3E3HistoryPESs_Type=Counter64
_WanT3E3HistoryPESs_Object=MibTableColumn
wanT3E3HistoryPESs=_WanT3E3HistoryPESs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,9),_WanT3E3HistoryPESs_Type())
wanT3E3HistoryPESs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistoryPESs.setStatus(_A)
_WanT3E3HistoryPSESs_Type=Counter64
_WanT3E3HistoryPSESs_Object=MibTableColumn
wanT3E3HistoryPSESs=_WanT3E3HistoryPSESs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,10),_WanT3E3HistoryPSESs_Type())
wanT3E3HistoryPSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistoryPSESs.setStatus(_A)
_WanT3E3HistoryOOFs_Type=Counter64
_WanT3E3HistoryOOFs_Object=MibTableColumn
wanT3E3HistoryOOFs=_WanT3E3HistoryOOFs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,11),_WanT3E3HistoryOOFs_Type())
wanT3E3HistoryOOFs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistoryOOFs.setStatus(_A)
_WanT3E3HistorySEFSs_Type=Counter64
_WanT3E3HistorySEFSs_Object=MibTableColumn
wanT3E3HistorySEFSs=_WanT3E3HistorySEFSs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,12),_WanT3E3HistorySEFSs_Type())
wanT3E3HistorySEFSs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistorySEFSs.setStatus(_A)
_WanT3E3HistoryUASs_Type=Counter64
_WanT3E3HistoryUASs_Object=MibTableColumn
wanT3E3HistoryUASs=_WanT3E3HistoryUASs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,13),_WanT3E3HistoryUASs_Type())
wanT3E3HistoryUASs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistoryUASs.setStatus(_A)
_WanT3E3HistoryLCVs_Type=Counter64
_WanT3E3HistoryLCVs_Object=MibTableColumn
wanT3E3HistoryLCVs=_WanT3E3HistoryLCVs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,14),_WanT3E3HistoryLCVs_Type())
wanT3E3HistoryLCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistoryLCVs.setStatus(_A)
_WanT3E3HistoryPCVs_Type=Counter64
_WanT3E3HistoryPCVs_Object=MibTableColumn
wanT3E3HistoryPCVs=_WanT3E3HistoryPCVs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,15),_WanT3E3HistoryPCVs_Type())
wanT3E3HistoryPCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistoryPCVs.setStatus(_A)
_WanT3E3HistoryLESs_Type=Counter64
_WanT3E3HistoryLESs_Object=MibTableColumn
wanT3E3HistoryLESs=_WanT3E3HistoryLESs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,16),_WanT3E3HistoryLESs_Type())
wanT3E3HistoryLESs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistoryLESs.setStatus(_A)
_WanT3E3HistoryCCVs_Type=Counter64
_WanT3E3HistoryCCVs_Object=MibTableColumn
wanT3E3HistoryCCVs=_WanT3E3HistoryCCVs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,17),_WanT3E3HistoryCCVs_Type())
wanT3E3HistoryCCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistoryCCVs.setStatus(_A)
_WanT3E3HistoryCESs_Type=Counter64
_WanT3E3HistoryCESs_Object=MibTableColumn
wanT3E3HistoryCESs=_WanT3E3HistoryCESs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,18),_WanT3E3HistoryCESs_Type())
wanT3E3HistoryCESs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistoryCESs.setStatus(_A)
_WanT3E3HistoryCSESs_Type=Counter64
_WanT3E3HistoryCSESs_Object=MibTableColumn
wanT3E3HistoryCSESs=_WanT3E3HistoryCSESs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,19),_WanT3E3HistoryCSESs_Type())
wanT3E3HistoryCSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistoryCSESs.setStatus(_A)
_WanT3E3HistoryRAIs_Type=Counter64
_WanT3E3HistoryRAIs_Object=MibTableColumn
wanT3E3HistoryRAIs=_WanT3E3HistoryRAIs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,20),_WanT3E3HistoryRAIs_Type())
wanT3E3HistoryRAIs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistoryRAIs.setStatus(_A)
_WanT3E3HistoryAISs_Type=Counter64
_WanT3E3HistoryAISs_Object=MibTableColumn
wanT3E3HistoryAISs=_WanT3E3HistoryAISs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,21),_WanT3E3HistoryAISs_Type())
wanT3E3HistoryAISs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistoryAISs.setStatus(_A)
_WanT3E3HistoryLOFs_Type=Counter64
_WanT3E3HistoryLOFs_Object=MibTableColumn
wanT3E3HistoryLOFs=_WanT3E3HistoryLOFs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,22),_WanT3E3HistoryLOFs_Type())
wanT3E3HistoryLOFs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistoryLOFs.setStatus(_A)
_WanT3E3HistoryLOSs_Type=Counter64
_WanT3E3HistoryLOSs_Object=MibTableColumn
wanT3E3HistoryLOSs=_WanT3E3HistoryLOSs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,23),_WanT3E3HistoryLOSs_Type())
wanT3E3HistoryLOSs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistoryLOSs.setStatus(_A)
class _WanT3E3HistoryInUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanT3E3HistoryInUtilization_Type.__name__=_C
_WanT3E3HistoryInUtilization_Object=MibTableColumn
wanT3E3HistoryInUtilization=_WanT3E3HistoryInUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,24),_WanT3E3HistoryInUtilization_Type())
wanT3E3HistoryInUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistoryInUtilization.setStatus(_A)
class _WanT3E3HistoryOutUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanT3E3HistoryOutUtilization_Type.__name__=_C
_WanT3E3HistoryOutUtilization_Object=MibTableColumn
wanT3E3HistoryOutUtilization=_WanT3E3HistoryOutUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,4,1,25),_WanT3E3HistoryOutUtilization_Type())
wanT3E3HistoryOutUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanT3E3HistoryOutUtilization.setStatus(_A)
_WanAtmHistoryTable_Object=MibTable
wanAtmHistoryTable=_WanAtmHistoryTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5))
if mibBuilder.loadTexts:wanAtmHistoryTable.setStatus(_A)
_WanAtmHistoryEntry_Object=MibTableRow
wanAtmHistoryEntry=_WanAtmHistoryEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1))
wanAtmHistoryEntry.setIndexNames((0,_E,_c),(0,_E,_d))
if mibBuilder.loadTexts:wanAtmHistoryEntry.setStatus(_A)
class _WanAtmHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanAtmHistoryIndex_Type.__name__=_C
_WanAtmHistoryIndex_Object=MibTableColumn
wanAtmHistoryIndex=_WanAtmHistoryIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,1),_WanAtmHistoryIndex_Type())
wanAtmHistoryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanAtmHistoryIndex.setStatus(_A)
class _WanAtmHistorySampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WanAtmHistorySampleIndex_Type.__name__=_C
_WanAtmHistorySampleIndex_Object=MibTableColumn
wanAtmHistorySampleIndex=_WanAtmHistorySampleIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,2),_WanAtmHistorySampleIndex_Type())
wanAtmHistorySampleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanAtmHistorySampleIndex.setStatus(_A)
_WanAtmHistoryIntervalStart_Type=TimeTicks
_WanAtmHistoryIntervalStart_Object=MibTableColumn
wanAtmHistoryIntervalStart=_WanAtmHistoryIntervalStart_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,3),_WanAtmHistoryIntervalStart_Type())
wanAtmHistoryIntervalStart.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryIntervalStart.setStatus(_A)
_WanAtmHistoryDropEvents_Type=Counter64
_WanAtmHistoryDropEvents_Object=MibTableColumn
wanAtmHistoryDropEvents=_WanAtmHistoryDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,4),_WanAtmHistoryDropEvents_Type())
wanAtmHistoryDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryDropEvents.setStatus(_A)
_WanAtmHistoryInCells_Type=Counter64
_WanAtmHistoryInCells_Object=MibTableColumn
wanAtmHistoryInCells=_WanAtmHistoryInCells_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,5),_WanAtmHistoryInCells_Type())
wanAtmHistoryInCells.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryInCells.setStatus(_A)
_WanAtmHistoryOutCells_Type=Counter64
_WanAtmHistoryOutCells_Object=MibTableColumn
wanAtmHistoryOutCells=_WanAtmHistoryOutCells_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,6),_WanAtmHistoryOutCells_Type())
wanAtmHistoryOutCells.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryOutCells.setStatus(_A)
_WanAtmHistoryInCLP1_Type=Counter64
_WanAtmHistoryInCLP1_Object=MibTableColumn
wanAtmHistoryInCLP1=_WanAtmHistoryInCLP1_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,7),_WanAtmHistoryInCLP1_Type())
wanAtmHistoryInCLP1.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryInCLP1.setStatus(_A)
_WanAtmHistoryOutCLP1_Type=Counter64
_WanAtmHistoryOutCLP1_Object=MibTableColumn
wanAtmHistoryOutCLP1=_WanAtmHistoryOutCLP1_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,8),_WanAtmHistoryOutCLP1_Type())
wanAtmHistoryOutCLP1.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryOutCLP1.setStatus(_A)
_WanAtmHistoryConnectionEvents_Type=Counter64
_WanAtmHistoryConnectionEvents_Object=MibTableColumn
wanAtmHistoryConnectionEvents=_WanAtmHistoryConnectionEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,9),_WanAtmHistoryConnectionEvents_Type())
wanAtmHistoryConnectionEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryConnectionEvents.setStatus(_A)
_WanAtmHistoryErroredPDUs_Type=Counter64
_WanAtmHistoryErroredPDUs_Object=MibTableColumn
wanAtmHistoryErroredPDUs=_WanAtmHistoryErroredPDUs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,10),_WanAtmHistoryErroredPDUs_Type())
wanAtmHistoryErroredPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryErroredPDUs.setStatus(_A)
_WanAtmHistorySetupAttempts_Type=Counter64
_WanAtmHistorySetupAttempts_Object=MibTableColumn
wanAtmHistorySetupAttempts=_WanAtmHistorySetupAttempts_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,11),_WanAtmHistorySetupAttempts_Type())
wanAtmHistorySetupAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistorySetupAttempts.setStatus(_A)
_WanAtmHistoryInRoutesUnavailable_Type=Counter64
_WanAtmHistoryInRoutesUnavailable_Object=MibTableColumn
wanAtmHistoryInRoutesUnavailable=_WanAtmHistoryInRoutesUnavailable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,12),_WanAtmHistoryInRoutesUnavailable_Type())
wanAtmHistoryInRoutesUnavailable.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryInRoutesUnavailable.setStatus(_A)
_WanAtmHistoryOutRoutesUnavailable_Type=Counter64
_WanAtmHistoryOutRoutesUnavailable_Object=MibTableColumn
wanAtmHistoryOutRoutesUnavailable=_WanAtmHistoryOutRoutesUnavailable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,13),_WanAtmHistoryOutRoutesUnavailable_Type())
wanAtmHistoryOutRoutesUnavailable.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryOutRoutesUnavailable.setStatus(_A)
_WanAtmHistoryInResourcesUnavailable_Type=Counter64
_WanAtmHistoryInResourcesUnavailable_Object=MibTableColumn
wanAtmHistoryInResourcesUnavailable=_WanAtmHistoryInResourcesUnavailable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,14),_WanAtmHistoryInResourcesUnavailable_Type())
wanAtmHistoryInResourcesUnavailable.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryInResourcesUnavailable.setStatus(_A)
_WanAtmHistoryOutResourcesUnavailable_Type=Counter64
_WanAtmHistoryOutResourcesUnavailable_Object=MibTableColumn
wanAtmHistoryOutResourcesUnavailable=_WanAtmHistoryOutResourcesUnavailable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,15),_WanAtmHistoryOutResourcesUnavailable_Type())
wanAtmHistoryOutResourcesUnavailable.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryOutResourcesUnavailable.setStatus(_A)
_WanAtmHistoryInUnsuccessfulCalls_Type=Counter64
_WanAtmHistoryInUnsuccessfulCalls_Object=MibTableColumn
wanAtmHistoryInUnsuccessfulCalls=_WanAtmHistoryInUnsuccessfulCalls_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,16),_WanAtmHistoryInUnsuccessfulCalls_Type())
wanAtmHistoryInUnsuccessfulCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryInUnsuccessfulCalls.setStatus(_A)
_WanAtmHistoryOutUnsuccessfulCalls_Type=Counter64
_WanAtmHistoryOutUnsuccessfulCalls_Object=MibTableColumn
wanAtmHistoryOutUnsuccessfulCalls=_WanAtmHistoryOutUnsuccessfulCalls_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,17),_WanAtmHistoryOutUnsuccessfulCalls_Type())
wanAtmHistoryOutUnsuccessfulCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryOutUnsuccessfulCalls.setStatus(_A)
_WanAtmHistoryInIncorrectMsgs_Type=Counter64
_WanAtmHistoryInIncorrectMsgs_Object=MibTableColumn
wanAtmHistoryInIncorrectMsgs=_WanAtmHistoryInIncorrectMsgs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,18),_WanAtmHistoryInIncorrectMsgs_Type())
wanAtmHistoryInIncorrectMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryInIncorrectMsgs.setStatus(_A)
_WanAtmHistoryOutIncorrectMsgs_Type=Counter64
_WanAtmHistoryOutIncorrectMsgs_Object=MibTableColumn
wanAtmHistoryOutIncorrectMsgs=_WanAtmHistoryOutIncorrectMsgs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,19),_WanAtmHistoryOutIncorrectMsgs_Type())
wanAtmHistoryOutIncorrectMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryOutIncorrectMsgs.setStatus(_A)
_WanAtmHistoryInPartyEvents_Type=Counter64
_WanAtmHistoryInPartyEvents_Object=MibTableColumn
wanAtmHistoryInPartyEvents=_WanAtmHistoryInPartyEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,20),_WanAtmHistoryInPartyEvents_Type())
wanAtmHistoryInPartyEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryInPartyEvents.setStatus(_A)
_WanAtmHistoryOutPartyEvents_Type=Counter64
_WanAtmHistoryOutPartyEvents_Object=MibTableColumn
wanAtmHistoryOutPartyEvents=_WanAtmHistoryOutPartyEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,21),_WanAtmHistoryOutPartyEvents_Type())
wanAtmHistoryOutPartyEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryOutPartyEvents.setStatus(_A)
_WanAtmHistoryInExpiries_Type=Counter64
_WanAtmHistoryInExpiries_Object=MibTableColumn
wanAtmHistoryInExpiries=_WanAtmHistoryInExpiries_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,22),_WanAtmHistoryInExpiries_Type())
wanAtmHistoryInExpiries.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryInExpiries.setStatus(_A)
_WanAtmHistoryOutExpiries_Type=Counter64
_WanAtmHistoryOutExpiries_Object=MibTableColumn
wanAtmHistoryOutExpiries=_WanAtmHistoryOutExpiries_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,23),_WanAtmHistoryOutExpiries_Type())
wanAtmHistoryOutExpiries.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryOutExpiries.setStatus(_A)
_WanAtmHistoryInRestartErrors_Type=Counter64
_WanAtmHistoryInRestartErrors_Object=MibTableColumn
wanAtmHistoryInRestartErrors=_WanAtmHistoryInRestartErrors_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,24),_WanAtmHistoryInRestartErrors_Type())
wanAtmHistoryInRestartErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryInRestartErrors.setStatus(_A)
_WanAtmHistoryOutRestartErrors_Type=Counter64
_WanAtmHistoryOutRestartErrors_Object=MibTableColumn
wanAtmHistoryOutRestartErrors=_WanAtmHistoryOutRestartErrors_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,25),_WanAtmHistoryOutRestartErrors_Type())
wanAtmHistoryOutRestartErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryOutRestartErrors.setStatus(_A)
_WanAtmHistoryInSVCs_Type=Counter64
_WanAtmHistoryInSVCs_Object=MibTableColumn
wanAtmHistoryInSVCs=_WanAtmHistoryInSVCs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,26),_WanAtmHistoryInSVCs_Type())
wanAtmHistoryInSVCs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryInSVCs.setStatus(_A)
_WanAtmHistoryOutSVCs_Type=Counter64
_WanAtmHistoryOutSVCs_Object=MibTableColumn
wanAtmHistoryOutSVCs=_WanAtmHistoryOutSVCs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,27),_WanAtmHistoryOutSVCs_Type())
wanAtmHistoryOutSVCs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryOutSVCs.setStatus(_A)
_WanAtmHistoryInOCDs_Type=Counter64
_WanAtmHistoryInOCDs_Object=MibTableColumn
wanAtmHistoryInOCDs=_WanAtmHistoryInOCDs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,28),_WanAtmHistoryInOCDs_Type())
wanAtmHistoryInOCDs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryInOCDs.setStatus(_A)
_WanAtmHistoryOutOCDs_Type=Counter64
_WanAtmHistoryOutOCDs_Object=MibTableColumn
wanAtmHistoryOutOCDs=_WanAtmHistoryOutOCDs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,29),_WanAtmHistoryOutOCDs_Type())
wanAtmHistoryOutOCDs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryOutOCDs.setStatus(_A)
_WanAtmHistoryInLOCs_Type=Counter64
_WanAtmHistoryInLOCs_Object=MibTableColumn
wanAtmHistoryInLOCs=_WanAtmHistoryInLOCs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,30),_WanAtmHistoryInLOCs_Type())
wanAtmHistoryInLOCs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryInLOCs.setStatus(_A)
_WanAtmHistoryOutLOCs_Type=Counter64
_WanAtmHistoryOutLOCs_Object=MibTableColumn
wanAtmHistoryOutLOCs=_WanAtmHistoryOutLOCs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,31),_WanAtmHistoryOutLOCs_Type())
wanAtmHistoryOutLOCs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryOutLOCs.setStatus(_A)
_WanAtmHistoryInLOFs_Type=Counter64
_WanAtmHistoryInLOFs_Object=MibTableColumn
wanAtmHistoryInLOFs=_WanAtmHistoryInLOFs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,32),_WanAtmHistoryInLOFs_Type())
wanAtmHistoryInLOFs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryInLOFs.setStatus(_A)
_WanAtmHistoryOutLOFs_Type=Counter64
_WanAtmHistoryOutLOFs_Object=MibTableColumn
wanAtmHistoryOutLOFs=_WanAtmHistoryOutLOFs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,33),_WanAtmHistoryOutLOFs_Type())
wanAtmHistoryOutLOFs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryOutLOFs.setStatus(_A)
_WanAtmHistoryInLOPs_Type=Counter64
_WanAtmHistoryInLOPs_Object=MibTableColumn
wanAtmHistoryInLOPs=_WanAtmHistoryInLOPs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,34),_WanAtmHistoryInLOPs_Type())
wanAtmHistoryInLOPs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryInLOPs.setStatus(_A)
_WanAtmHistoryOutLOPs_Type=Counter64
_WanAtmHistoryOutLOPs_Object=MibTableColumn
wanAtmHistoryOutLOPs=_WanAtmHistoryOutLOPs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,35),_WanAtmHistoryOutLOPs_Type())
wanAtmHistoryOutLOPs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryOutLOPs.setStatus(_A)
_WanAtmHistoryInLOSs_Type=Counter64
_WanAtmHistoryInLOSs_Object=MibTableColumn
wanAtmHistoryInLOSs=_WanAtmHistoryInLOSs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,36),_WanAtmHistoryInLOSs_Type())
wanAtmHistoryInLOSs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryInLOSs.setStatus(_A)
_WanAtmHistoryOutLOSs_Type=Counter64
_WanAtmHistoryOutLOSs_Object=MibTableColumn
wanAtmHistoryOutLOSs=_WanAtmHistoryOutLOSs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,37),_WanAtmHistoryOutLOSs_Type())
wanAtmHistoryOutLOSs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryOutLOSs.setStatus(_A)
class _WanAtmHistoryInUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanAtmHistoryInUtilization_Type.__name__=_C
_WanAtmHistoryInUtilization_Object=MibTableColumn
wanAtmHistoryInUtilization=_WanAtmHistoryInUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,38),_WanAtmHistoryInUtilization_Type())
wanAtmHistoryInUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryInUtilization.setStatus(_A)
class _WanAtmHistoryOutUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanAtmHistoryOutUtilization_Type.__name__=_C
_WanAtmHistoryOutUtilization_Object=MibTableColumn
wanAtmHistoryOutUtilization=_WanAtmHistoryOutUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,1,5,1,39),_WanAtmHistoryOutUtilization_Type())
wanAtmHistoryOutUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAtmHistoryOutUtilization.setStatus(_A)
_WanProtocolHistory_ObjectIdentity=ObjectIdentity
wanProtocolHistory=_WanProtocolHistory_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2))
_WanX25HistoryTable_Object=MibTable
wanX25HistoryTable=_WanX25HistoryTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1))
if mibBuilder.loadTexts:wanX25HistoryTable.setStatus(_A)
_WanX25HistoryEntry_Object=MibTableRow
wanX25HistoryEntry=_WanX25HistoryEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1))
wanX25HistoryEntry.setIndexNames((0,_E,_e),(0,_E,_f))
if mibBuilder.loadTexts:wanX25HistoryEntry.setStatus(_A)
class _WanX25HistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanX25HistoryIndex_Type.__name__=_C
_WanX25HistoryIndex_Object=MibTableColumn
wanX25HistoryIndex=_WanX25HistoryIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,1),_WanX25HistoryIndex_Type())
wanX25HistoryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanX25HistoryIndex.setStatus(_A)
class _WanX25HistorySampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WanX25HistorySampleIndex_Type.__name__=_C
_WanX25HistorySampleIndex_Object=MibTableColumn
wanX25HistorySampleIndex=_WanX25HistorySampleIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,2),_WanX25HistorySampleIndex_Type())
wanX25HistorySampleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanX25HistorySampleIndex.setStatus(_A)
_WanX25HistoryIntervalStart_Type=TimeTicks
_WanX25HistoryIntervalStart_Object=MibTableColumn
wanX25HistoryIntervalStart=_WanX25HistoryIntervalStart_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,3),_WanX25HistoryIntervalStart_Type())
wanX25HistoryIntervalStart.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25HistoryIntervalStart.setStatus(_A)
_WanX25HistoryDropEvents_Type=Counter64
_WanX25HistoryDropEvents_Object=MibTableColumn
wanX25HistoryDropEvents=_WanX25HistoryDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,4),_WanX25HistoryDropEvents_Type())
wanX25HistoryDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25HistoryDropEvents.setStatus(_A)
_WanX25HistoryInFrames_Type=Counter64
_WanX25HistoryInFrames_Object=MibTableColumn
wanX25HistoryInFrames=_WanX25HistoryInFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,5),_WanX25HistoryInFrames_Type())
wanX25HistoryInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25HistoryInFrames.setStatus(_A)
_WanX25HistoryOutFrames_Type=Counter64
_WanX25HistoryOutFrames_Object=MibTableColumn
wanX25HistoryOutFrames=_WanX25HistoryOutFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,6),_WanX25HistoryOutFrames_Type())
wanX25HistoryOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25HistoryOutFrames.setStatus(_A)
_WanX25HistoryInOctets_Type=Counter64
_WanX25HistoryInOctets_Object=MibTableColumn
wanX25HistoryInOctets=_WanX25HistoryInOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,7),_WanX25HistoryInOctets_Type())
wanX25HistoryInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25HistoryInOctets.setStatus(_A)
_WanX25HistoryOutOctets_Type=Counter64
_WanX25HistoryOutOctets_Object=MibTableColumn
wanX25HistoryOutOctets=_WanX25HistoryOutOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,8),_WanX25HistoryOutOctets_Type())
wanX25HistoryOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25HistoryOutOctets.setStatus(_A)
_WanX25HistoryInRejects_Type=Counter64
_WanX25HistoryInRejects_Object=MibTableColumn
wanX25HistoryInRejects=_WanX25HistoryInRejects_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,9),_WanX25HistoryInRejects_Type())
wanX25HistoryInRejects.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25HistoryInRejects.setStatus(_A)
_WanX25HistoryOutRejects_Type=Counter64
_WanX25HistoryOutRejects_Object=MibTableColumn
wanX25HistoryOutRejects=_WanX25HistoryOutRejects_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,10),_WanX25HistoryOutRejects_Type())
wanX25HistoryOutRejects.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25HistoryOutRejects.setStatus(_A)
_WanX25HistoryInAttempts_Type=Counter64
_WanX25HistoryInAttempts_Object=MibTableColumn
wanX25HistoryInAttempts=_WanX25HistoryInAttempts_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,11),_WanX25HistoryInAttempts_Type())
wanX25HistoryInAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25HistoryInAttempts.setStatus(_A)
_WanX25HistoryOutAttempts_Type=Counter64
_WanX25HistoryOutAttempts_Object=MibTableColumn
wanX25HistoryOutAttempts=_WanX25HistoryOutAttempts_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,12),_WanX25HistoryOutAttempts_Type())
wanX25HistoryOutAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25HistoryOutAttempts.setStatus(_A)
_WanX25HistoryInFailures_Type=Counter64
_WanX25HistoryInFailures_Object=MibTableColumn
wanX25HistoryInFailures=_WanX25HistoryInFailures_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,13),_WanX25HistoryInFailures_Type())
wanX25HistoryInFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25HistoryInFailures.setStatus(_A)
_WanX25HistoryOutFailures_Type=Counter64
_WanX25HistoryOutFailures_Object=MibTableColumn
wanX25HistoryOutFailures=_WanX25HistoryOutFailures_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,14),_WanX25HistoryOutFailures_Type())
wanX25HistoryOutFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25HistoryOutFailures.setStatus(_A)
_WanX25HistoryProviderClears_Type=Counter64
_WanX25HistoryProviderClears_Object=MibTableColumn
wanX25HistoryProviderClears=_WanX25HistoryProviderClears_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,15),_WanX25HistoryProviderClears_Type())
wanX25HistoryProviderClears.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25HistoryProviderClears.setStatus(_A)
_WanX25HistoryInResets_Type=Counter64
_WanX25HistoryInResets_Object=MibTableColumn
wanX25HistoryInResets=_WanX25HistoryInResets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,16),_WanX25HistoryInResets_Type())
wanX25HistoryInResets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25HistoryInResets.setStatus(_A)
_WanX25HistoryOutResets_Type=Counter64
_WanX25HistoryOutResets_Object=MibTableColumn
wanX25HistoryOutResets=_WanX25HistoryOutResets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,17),_WanX25HistoryOutResets_Type())
wanX25HistoryOutResets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25HistoryOutResets.setStatus(_A)
_WanX25HistoryProviderResets_Type=Counter64
_WanX25HistoryProviderResets_Object=MibTableColumn
wanX25HistoryProviderResets=_WanX25HistoryProviderResets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,18),_WanX25HistoryProviderResets_Type())
wanX25HistoryProviderResets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25HistoryProviderResets.setStatus(_A)
_WanX25HistoryInAccusedErrors_Type=Counter64
_WanX25HistoryInAccusedErrors_Object=MibTableColumn
wanX25HistoryInAccusedErrors=_WanX25HistoryInAccusedErrors_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,19),_WanX25HistoryInAccusedErrors_Type())
wanX25HistoryInAccusedErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25HistoryInAccusedErrors.setStatus(_A)
_WanX25HistoryOutAccusedErrors_Type=Counter64
_WanX25HistoryOutAccusedErrors_Object=MibTableColumn
wanX25HistoryOutAccusedErrors=_WanX25HistoryOutAccusedErrors_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,20),_WanX25HistoryOutAccusedErrors_Type())
wanX25HistoryOutAccusedErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25HistoryOutAccusedErrors.setStatus(_A)
_WanX25HistoryInInterrupts_Type=Counter64
_WanX25HistoryInInterrupts_Object=MibTableColumn
wanX25HistoryInInterrupts=_WanX25HistoryInInterrupts_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,21),_WanX25HistoryInInterrupts_Type())
wanX25HistoryInInterrupts.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25HistoryInInterrupts.setStatus(_A)
_WanX25HistoryOutInterrupts_Type=Counter64
_WanX25HistoryOutInterrupts_Object=MibTableColumn
wanX25HistoryOutInterrupts=_WanX25HistoryOutInterrupts_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,22),_WanX25HistoryOutInterrupts_Type())
wanX25HistoryOutInterrupts.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25HistoryOutInterrupts.setStatus(_A)
class _WanX25HistoryInUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanX25HistoryInUtilization_Type.__name__=_C
_WanX25HistoryInUtilization_Object=MibTableColumn
wanX25HistoryInUtilization=_WanX25HistoryInUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,23),_WanX25HistoryInUtilization_Type())
wanX25HistoryInUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25HistoryInUtilization.setStatus(_A)
class _WanX25HistoryOutUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanX25HistoryOutUtilization_Type.__name__=_C
_WanX25HistoryOutUtilization_Object=MibTableColumn
wanX25HistoryOutUtilization=_WanX25HistoryOutUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,1,1,24),_WanX25HistoryOutUtilization_Type())
wanX25HistoryOutUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25HistoryOutUtilization.setStatus(_A)
_WanFrHistoryTable_Object=MibTable
wanFrHistoryTable=_WanFrHistoryTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,2))
if mibBuilder.loadTexts:wanFrHistoryTable.setStatus(_A)
_WanFrHistoryEntry_Object=MibTableRow
wanFrHistoryEntry=_WanFrHistoryEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,2,1))
wanFrHistoryEntry.setIndexNames((0,_E,_g),(0,_E,_h))
if mibBuilder.loadTexts:wanFrHistoryEntry.setStatus(_A)
class _WanFrHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanFrHistoryIndex_Type.__name__=_C
_WanFrHistoryIndex_Object=MibTableColumn
wanFrHistoryIndex=_WanFrHistoryIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,2,1,1),_WanFrHistoryIndex_Type())
wanFrHistoryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanFrHistoryIndex.setStatus(_A)
class _WanFrHistorySampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WanFrHistorySampleIndex_Type.__name__=_C
_WanFrHistorySampleIndex_Object=MibTableColumn
wanFrHistorySampleIndex=_WanFrHistorySampleIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,2,1,2),_WanFrHistorySampleIndex_Type())
wanFrHistorySampleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanFrHistorySampleIndex.setStatus(_A)
_WanFrHistoryIntervalStart_Type=TimeTicks
_WanFrHistoryIntervalStart_Object=MibTableColumn
wanFrHistoryIntervalStart=_WanFrHistoryIntervalStart_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,2,1,3),_WanFrHistoryIntervalStart_Type())
wanFrHistoryIntervalStart.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrHistoryIntervalStart.setStatus(_A)
_WanFrHistoryDropEvents_Type=Counter64
_WanFrHistoryDropEvents_Object=MibTableColumn
wanFrHistoryDropEvents=_WanFrHistoryDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,2,1,4),_WanFrHistoryDropEvents_Type())
wanFrHistoryDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrHistoryDropEvents.setStatus(_A)
_WanFrHistoryInFrames_Type=Counter64
_WanFrHistoryInFrames_Object=MibTableColumn
wanFrHistoryInFrames=_WanFrHistoryInFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,2,1,5),_WanFrHistoryInFrames_Type())
wanFrHistoryInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrHistoryInFrames.setStatus(_A)
_WanFrHistoryOutFrames_Type=Counter64
_WanFrHistoryOutFrames_Object=MibTableColumn
wanFrHistoryOutFrames=_WanFrHistoryOutFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,2,1,6),_WanFrHistoryOutFrames_Type())
wanFrHistoryOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrHistoryOutFrames.setStatus(_A)
_WanFrHistoryInOctets_Type=Counter64
_WanFrHistoryInOctets_Object=MibTableColumn
wanFrHistoryInOctets=_WanFrHistoryInOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,2,1,7),_WanFrHistoryInOctets_Type())
wanFrHistoryInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrHistoryInOctets.setStatus(_A)
_WanFrHistoryOutOctets_Type=Counter64
_WanFrHistoryOutOctets_Object=MibTableColumn
wanFrHistoryOutOctets=_WanFrHistoryOutOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,2,1,8),_WanFrHistoryOutOctets_Type())
wanFrHistoryOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrHistoryOutOctets.setStatus(_A)
_WanFrHistoryInFECNs_Type=Counter64
_WanFrHistoryInFECNs_Object=MibTableColumn
wanFrHistoryInFECNs=_WanFrHistoryInFECNs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,2,1,9),_WanFrHistoryInFECNs_Type())
wanFrHistoryInFECNs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrHistoryInFECNs.setStatus(_A)
_WanFrHistoryOutFECNs_Type=Counter64
_WanFrHistoryOutFECNs_Object=MibTableColumn
wanFrHistoryOutFECNs=_WanFrHistoryOutFECNs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,2,1,10),_WanFrHistoryOutFECNs_Type())
wanFrHistoryOutFECNs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrHistoryOutFECNs.setStatus(_A)
_WanFrHistoryInBECNs_Type=Counter64
_WanFrHistoryInBECNs_Object=MibTableColumn
wanFrHistoryInBECNs=_WanFrHistoryInBECNs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,2,1,11),_WanFrHistoryInBECNs_Type())
wanFrHistoryInBECNs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrHistoryInBECNs.setStatus(_A)
_WanFrHistoryOutBECNs_Type=Counter64
_WanFrHistoryOutBECNs_Object=MibTableColumn
wanFrHistoryOutBECNs=_WanFrHistoryOutBECNs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,2,1,12),_WanFrHistoryOutBECNs_Type())
wanFrHistoryOutBECNs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrHistoryOutBECNs.setStatus(_A)
_WanFrHistoryInDEs_Type=Counter64
_WanFrHistoryInDEs_Object=MibTableColumn
wanFrHistoryInDEs=_WanFrHistoryInDEs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,2,1,13),_WanFrHistoryInDEs_Type())
wanFrHistoryInDEs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrHistoryInDEs.setStatus(_A)
_WanFrHistoryOutDEs_Type=Counter64
_WanFrHistoryOutDEs_Object=MibTableColumn
wanFrHistoryOutDEs=_WanFrHistoryOutDEs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,2,1,14),_WanFrHistoryOutDEs_Type())
wanFrHistoryOutDEs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrHistoryOutDEs.setStatus(_A)
class _WanFrHistoryInUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanFrHistoryInUtilization_Type.__name__=_C
_WanFrHistoryInUtilization_Object=MibTableColumn
wanFrHistoryInUtilization=_WanFrHistoryInUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,2,1,15),_WanFrHistoryInUtilization_Type())
wanFrHistoryInUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrHistoryInUtilization.setStatus(_A)
class _WanFrHistoryOutUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanFrHistoryOutUtilization_Type.__name__=_C
_WanFrHistoryOutUtilization_Object=MibTableColumn
wanFrHistoryOutUtilization=_WanFrHistoryOutUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,2,1,16),_WanFrHistoryOutUtilization_Type())
wanFrHistoryOutUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrHistoryOutUtilization.setStatus(_A)
_WanAal5HistoryTable_Object=MibTable
wanAal5HistoryTable=_WanAal5HistoryTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,3))
if mibBuilder.loadTexts:wanAal5HistoryTable.setStatus(_A)
_WanAal5HistoryEntry_Object=MibTableRow
wanAal5HistoryEntry=_WanAal5HistoryEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,3,1))
wanAal5HistoryEntry.setIndexNames((0,_E,_i),(0,_E,_j))
if mibBuilder.loadTexts:wanAal5HistoryEntry.setStatus(_A)
class _WanAal5HistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanAal5HistoryIndex_Type.__name__=_C
_WanAal5HistoryIndex_Object=MibTableColumn
wanAal5HistoryIndex=_WanAal5HistoryIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,3,1,1),_WanAal5HistoryIndex_Type())
wanAal5HistoryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanAal5HistoryIndex.setStatus(_A)
class _WanAal5HistorySampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WanAal5HistorySampleIndex_Type.__name__=_C
_WanAal5HistorySampleIndex_Object=MibTableColumn
wanAal5HistorySampleIndex=_WanAal5HistorySampleIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,3,1,2),_WanAal5HistorySampleIndex_Type())
wanAal5HistorySampleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanAal5HistorySampleIndex.setStatus(_A)
_WanAal5HistoryIntervalStart_Type=TimeTicks
_WanAal5HistoryIntervalStart_Object=MibTableColumn
wanAal5HistoryIntervalStart=_WanAal5HistoryIntervalStart_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,3,1,3),_WanAal5HistoryIntervalStart_Type())
wanAal5HistoryIntervalStart.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5HistoryIntervalStart.setStatus(_A)
_WanAal5HistoryDropEvents_Type=Counter64
_WanAal5HistoryDropEvents_Object=MibTableColumn
wanAal5HistoryDropEvents=_WanAal5HistoryDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,3,1,4),_WanAal5HistoryDropEvents_Type())
wanAal5HistoryDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5HistoryDropEvents.setStatus(_A)
_WanAal5HistoryInCells_Type=Counter64
_WanAal5HistoryInCells_Object=MibTableColumn
wanAal5HistoryInCells=_WanAal5HistoryInCells_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,3,1,5),_WanAal5HistoryInCells_Type())
wanAal5HistoryInCells.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5HistoryInCells.setStatus(_A)
_WanAal5HistoryOutCells_Type=Counter64
_WanAal5HistoryOutCells_Object=MibTableColumn
wanAal5HistoryOutCells=_WanAal5HistoryOutCells_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,3,1,6),_WanAal5HistoryOutCells_Type())
wanAal5HistoryOutCells.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5HistoryOutCells.setStatus(_A)
_WanAal5HistoryInPDUs_Type=Counter64
_WanAal5HistoryInPDUs_Object=MibTableColumn
wanAal5HistoryInPDUs=_WanAal5HistoryInPDUs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,3,1,7),_WanAal5HistoryInPDUs_Type())
wanAal5HistoryInPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5HistoryInPDUs.setStatus(_A)
_WanAal5HistoryOutPDUs_Type=Counter64
_WanAal5HistoryOutPDUs_Object=MibTableColumn
wanAal5HistoryOutPDUs=_WanAal5HistoryOutPDUs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,3,1,8),_WanAal5HistoryOutPDUs_Type())
wanAal5HistoryOutPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5HistoryOutPDUs.setStatus(_A)
_WanAal5HistoryInOctets_Type=Counter64
_WanAal5HistoryInOctets_Object=MibTableColumn
wanAal5HistoryInOctets=_WanAal5HistoryInOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,3,1,9),_WanAal5HistoryInOctets_Type())
wanAal5HistoryInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5HistoryInOctets.setStatus(_A)
_WanAal5HistoryOutOctets_Type=Counter64
_WanAal5HistoryOutOctets_Object=MibTableColumn
wanAal5HistoryOutOctets=_WanAal5HistoryOutOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,3,1,10),_WanAal5HistoryOutOctets_Type())
wanAal5HistoryOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5HistoryOutOctets.setStatus(_A)
_WanAal5HistoryInCLP1_Type=Counter64
_WanAal5HistoryInCLP1_Object=MibTableColumn
wanAal5HistoryInCLP1=_WanAal5HistoryInCLP1_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,3,1,11),_WanAal5HistoryInCLP1_Type())
wanAal5HistoryInCLP1.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5HistoryInCLP1.setStatus(_A)
_WanAal5HistoryOutCLP1_Type=Counter64
_WanAal5HistoryOutCLP1_Object=MibTableColumn
wanAal5HistoryOutCLP1=_WanAal5HistoryOutCLP1_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,3,1,12),_WanAal5HistoryOutCLP1_Type())
wanAal5HistoryOutCLP1.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5HistoryOutCLP1.setStatus(_A)
_WanAal5HistoryInCRCs_Type=Counter64
_WanAal5HistoryInCRCs_Object=MibTableColumn
wanAal5HistoryInCRCs=_WanAal5HistoryInCRCs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,3,1,13),_WanAal5HistoryInCRCs_Type())
wanAal5HistoryInCRCs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5HistoryInCRCs.setStatus(_A)
_WanAal5HistoryOutCRCs_Type=Counter64
_WanAal5HistoryOutCRCs_Object=MibTableColumn
wanAal5HistoryOutCRCs=_WanAal5HistoryOutCRCs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,3,1,14),_WanAal5HistoryOutCRCs_Type())
wanAal5HistoryOutCRCs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5HistoryOutCRCs.setStatus(_A)
_WanAal5HistoryInOversizedSDUs_Type=Counter64
_WanAal5HistoryInOversizedSDUs_Object=MibTableColumn
wanAal5HistoryInOversizedSDUs=_WanAal5HistoryInOversizedSDUs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,3,1,15),_WanAal5HistoryInOversizedSDUs_Type())
wanAal5HistoryInOversizedSDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5HistoryInOversizedSDUs.setStatus(_A)
_WanAal5HistoryOutOversizedSDUs_Type=Counter64
_WanAal5HistoryOutOversizedSDUs_Object=MibTableColumn
wanAal5HistoryOutOversizedSDUs=_WanAal5HistoryOutOversizedSDUs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,3,1,16),_WanAal5HistoryOutOversizedSDUs_Type())
wanAal5HistoryOutOversizedSDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5HistoryOutOversizedSDUs.setStatus(_A)
_WanAal5HistoryInSVCs_Type=Counter64
_WanAal5HistoryInSVCs_Object=MibTableColumn
wanAal5HistoryInSVCs=_WanAal5HistoryInSVCs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,3,1,17),_WanAal5HistoryInSVCs_Type())
wanAal5HistoryInSVCs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5HistoryInSVCs.setStatus(_A)
_WanAal5HistoryOutSVCs_Type=Counter64
_WanAal5HistoryOutSVCs_Object=MibTableColumn
wanAal5HistoryOutSVCs=_WanAal5HistoryOutSVCs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,3,1,18),_WanAal5HistoryOutSVCs_Type())
wanAal5HistoryOutSVCs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5HistoryOutSVCs.setStatus(_A)
class _WanAal5HistoryInUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanAal5HistoryInUtilization_Type.__name__=_C
_WanAal5HistoryInUtilization_Object=MibTableColumn
wanAal5HistoryInUtilization=_WanAal5HistoryInUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,3,1,19),_WanAal5HistoryInUtilization_Type())
wanAal5HistoryInUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5HistoryInUtilization.setStatus(_A)
class _WanAal5HistoryOutUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanAal5HistoryOutUtilization_Type.__name__=_C
_WanAal5HistoryOutUtilization_Object=MibTableColumn
wanAal5HistoryOutUtilization=_WanAal5HistoryOutUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,3,1,20),_WanAal5HistoryOutUtilization_Type())
wanAal5HistoryOutUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5HistoryOutUtilization.setStatus(_A)
_WanPppHistoryTable_Object=MibTable
wanPppHistoryTable=_WanPppHistoryTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,4))
if mibBuilder.loadTexts:wanPppHistoryTable.setStatus(_A)
_WanPppHistoryEntry_Object=MibTableRow
wanPppHistoryEntry=_WanPppHistoryEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,4,1))
wanPppHistoryEntry.setIndexNames((0,_E,_k),(0,_E,_l))
if mibBuilder.loadTexts:wanPppHistoryEntry.setStatus(_A)
class _WanPppHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanPppHistoryIndex_Type.__name__=_C
_WanPppHistoryIndex_Object=MibTableColumn
wanPppHistoryIndex=_WanPppHistoryIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,4,1,1),_WanPppHistoryIndex_Type())
wanPppHistoryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanPppHistoryIndex.setStatus(_A)
class _WanPppHistorySampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WanPppHistorySampleIndex_Type.__name__=_C
_WanPppHistorySampleIndex_Object=MibTableColumn
wanPppHistorySampleIndex=_WanPppHistorySampleIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,4,1,2),_WanPppHistorySampleIndex_Type())
wanPppHistorySampleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanPppHistorySampleIndex.setStatus(_A)
_WanPppHistoryIntervalStart_Type=TimeTicks
_WanPppHistoryIntervalStart_Object=MibTableColumn
wanPppHistoryIntervalStart=_WanPppHistoryIntervalStart_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,4,1,3),_WanPppHistoryIntervalStart_Type())
wanPppHistoryIntervalStart.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppHistoryIntervalStart.setStatus(_A)
_WanPppHistoryDropEvents_Type=Counter64
_WanPppHistoryDropEvents_Object=MibTableColumn
wanPppHistoryDropEvents=_WanPppHistoryDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,4,1,4),_WanPppHistoryDropEvents_Type())
wanPppHistoryDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppHistoryDropEvents.setStatus(_A)
_WanPppHistoryInFrames_Type=Counter64
_WanPppHistoryInFrames_Object=MibTableColumn
wanPppHistoryInFrames=_WanPppHistoryInFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,4,1,5),_WanPppHistoryInFrames_Type())
wanPppHistoryInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppHistoryInFrames.setStatus(_A)
_WanPppHistoryOutFrames_Type=Counter64
_WanPppHistoryOutFrames_Object=MibTableColumn
wanPppHistoryOutFrames=_WanPppHistoryOutFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,4,1,6),_WanPppHistoryOutFrames_Type())
wanPppHistoryOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppHistoryOutFrames.setStatus(_A)
_WanPppHistoryInOctets_Type=Counter64
_WanPppHistoryInOctets_Object=MibTableColumn
wanPppHistoryInOctets=_WanPppHistoryInOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,4,1,7),_WanPppHistoryInOctets_Type())
wanPppHistoryInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppHistoryInOctets.setStatus(_A)
_WanPppHistoryOutOctets_Type=Counter64
_WanPppHistoryOutOctets_Object=MibTableColumn
wanPppHistoryOutOctets=_WanPppHistoryOutOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,4,1,8),_WanPppHistoryOutOctets_Type())
wanPppHistoryOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppHistoryOutOctets.setStatus(_A)
_WanPppHistoryInBadAddresses_Type=Counter64
_WanPppHistoryInBadAddresses_Object=MibTableColumn
wanPppHistoryInBadAddresses=_WanPppHistoryInBadAddresses_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,4,1,9),_WanPppHistoryInBadAddresses_Type())
wanPppHistoryInBadAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppHistoryInBadAddresses.setStatus(_A)
_WanPppHistoryOutBadAddresses_Type=Counter64
_WanPppHistoryOutBadAddresses_Object=MibTableColumn
wanPppHistoryOutBadAddresses=_WanPppHistoryOutBadAddresses_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,4,1,10),_WanPppHistoryOutBadAddresses_Type())
wanPppHistoryOutBadAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppHistoryOutBadAddresses.setStatus(_A)
_WanPppHistoryInBadControls_Type=Counter64
_WanPppHistoryInBadControls_Object=MibTableColumn
wanPppHistoryInBadControls=_WanPppHistoryInBadControls_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,4,1,11),_WanPppHistoryInBadControls_Type())
wanPppHistoryInBadControls.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppHistoryInBadControls.setStatus(_A)
_WanPppHistoryOutBadControls_Type=Counter64
_WanPppHistoryOutBadControls_Object=MibTableColumn
wanPppHistoryOutBadControls=_WanPppHistoryOutBadControls_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,4,1,12),_WanPppHistoryOutBadControls_Type())
wanPppHistoryOutBadControls.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppHistoryOutBadControls.setStatus(_A)
_WanPppHistoryInLongFrames_Type=Counter64
_WanPppHistoryInLongFrames_Object=MibTableColumn
wanPppHistoryInLongFrames=_WanPppHistoryInLongFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,4,1,13),_WanPppHistoryInLongFrames_Type())
wanPppHistoryInLongFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppHistoryInLongFrames.setStatus(_A)
_WanPppHistoryOutLongFrames_Type=Counter64
_WanPppHistoryOutLongFrames_Object=MibTableColumn
wanPppHistoryOutLongFrames=_WanPppHistoryOutLongFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,4,1,14),_WanPppHistoryOutLongFrames_Type())
wanPppHistoryOutLongFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppHistoryOutLongFrames.setStatus(_A)
_WanPppHistoryInBadFCSs_Type=Counter64
_WanPppHistoryInBadFCSs_Object=MibTableColumn
wanPppHistoryInBadFCSs=_WanPppHistoryInBadFCSs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,4,1,15),_WanPppHistoryInBadFCSs_Type())
wanPppHistoryInBadFCSs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppHistoryInBadFCSs.setStatus(_A)
_WanPppHistoryOutBadFCSs_Type=Counter64
_WanPppHistoryOutBadFCSs_Object=MibTableColumn
wanPppHistoryOutBadFCSs=_WanPppHistoryOutBadFCSs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,4,1,16),_WanPppHistoryOutBadFCSs_Type())
wanPppHistoryOutBadFCSs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppHistoryOutBadFCSs.setStatus(_A)
class _WanPppHistoryInUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanPppHistoryInUtilization_Type.__name__=_C
_WanPppHistoryInUtilization_Object=MibTableColumn
wanPppHistoryInUtilization=_WanPppHistoryInUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,4,1,17),_WanPppHistoryInUtilization_Type())
wanPppHistoryInUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppHistoryInUtilization.setStatus(_A)
class _WanPppHistoryOutUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanPppHistoryOutUtilization_Type.__name__=_C
_WanPppHistoryOutUtilization_Object=MibTableColumn
wanPppHistoryOutUtilization=_WanPppHistoryOutUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,2,4,1,18),_WanPppHistoryOutUtilization_Type())
wanPppHistoryOutUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanPppHistoryOutUtilization.setStatus(_A)
_WanPvcHistory_ObjectIdentity=ObjectIdentity
wanPvcHistory=_WanPvcHistory_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3))
_WanX25PvcHistoryTable_Object=MibTable
wanX25PvcHistoryTable=_WanX25PvcHistoryTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,1))
if mibBuilder.loadTexts:wanX25PvcHistoryTable.setStatus(_A)
_WanX25PvcHistoryEntry_Object=MibTableRow
wanX25PvcHistoryEntry=_WanX25PvcHistoryEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,1,1))
wanX25PvcHistoryEntry.setIndexNames((0,_E,_m),(0,_E,_n))
if mibBuilder.loadTexts:wanX25PvcHistoryEntry.setStatus(_A)
class _WanX25PvcHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanX25PvcHistoryIndex_Type.__name__=_C
_WanX25PvcHistoryIndex_Object=MibTableColumn
wanX25PvcHistoryIndex=_WanX25PvcHistoryIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,1,1,1),_WanX25PvcHistoryIndex_Type())
wanX25PvcHistoryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanX25PvcHistoryIndex.setStatus(_A)
class _WanX25PvcHistorySampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WanX25PvcHistorySampleIndex_Type.__name__=_C
_WanX25PvcHistorySampleIndex_Object=MibTableColumn
wanX25PvcHistorySampleIndex=_WanX25PvcHistorySampleIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,1,1,2),_WanX25PvcHistorySampleIndex_Type())
wanX25PvcHistorySampleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanX25PvcHistorySampleIndex.setStatus(_A)
_WanX25PvcHistoryIntervalStart_Type=TimeTicks
_WanX25PvcHistoryIntervalStart_Object=MibTableColumn
wanX25PvcHistoryIntervalStart=_WanX25PvcHistoryIntervalStart_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,1,1,3),_WanX25PvcHistoryIntervalStart_Type())
wanX25PvcHistoryIntervalStart.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcHistoryIntervalStart.setStatus(_A)
_WanX25PvcHistoryDropEvents_Type=Counter64
_WanX25PvcHistoryDropEvents_Object=MibTableColumn
wanX25PvcHistoryDropEvents=_WanX25PvcHistoryDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,1,1,4),_WanX25PvcHistoryDropEvents_Type())
wanX25PvcHistoryDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcHistoryDropEvents.setStatus(_A)
_WanX25PvcHistoryInFrames_Type=Counter64
_WanX25PvcHistoryInFrames_Object=MibTableColumn
wanX25PvcHistoryInFrames=_WanX25PvcHistoryInFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,1,1,5),_WanX25PvcHistoryInFrames_Type())
wanX25PvcHistoryInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcHistoryInFrames.setStatus(_A)
_WanX25PvcHistoryOutFrames_Type=Counter64
_WanX25PvcHistoryOutFrames_Object=MibTableColumn
wanX25PvcHistoryOutFrames=_WanX25PvcHistoryOutFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,1,1,6),_WanX25PvcHistoryOutFrames_Type())
wanX25PvcHistoryOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcHistoryOutFrames.setStatus(_A)
_WanX25PvcHistoryInOctets_Type=Counter64
_WanX25PvcHistoryInOctets_Object=MibTableColumn
wanX25PvcHistoryInOctets=_WanX25PvcHistoryInOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,1,1,7),_WanX25PvcHistoryInOctets_Type())
wanX25PvcHistoryInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcHistoryInOctets.setStatus(_A)
_WanX25PvcHistoryOutOctets_Type=Counter64
_WanX25PvcHistoryOutOctets_Object=MibTableColumn
wanX25PvcHistoryOutOctets=_WanX25PvcHistoryOutOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,1,1,8),_WanX25PvcHistoryOutOctets_Type())
wanX25PvcHistoryOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcHistoryOutOctets.setStatus(_A)
_WanX25PvcHistoryInResets_Type=Counter64
_WanX25PvcHistoryInResets_Object=MibTableColumn
wanX25PvcHistoryInResets=_WanX25PvcHistoryInResets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,1,1,9),_WanX25PvcHistoryInResets_Type())
wanX25PvcHistoryInResets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcHistoryInResets.setStatus(_A)
_WanX25PvcHistoryOutResets_Type=Counter64
_WanX25PvcHistoryOutResets_Object=MibTableColumn
wanX25PvcHistoryOutResets=_WanX25PvcHistoryOutResets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,1,1,10),_WanX25PvcHistoryOutResets_Type())
wanX25PvcHistoryOutResets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcHistoryOutResets.setStatus(_A)
_WanX25PvcHistoryProviderResets_Type=Counter64
_WanX25PvcHistoryProviderResets_Object=MibTableColumn
wanX25PvcHistoryProviderResets=_WanX25PvcHistoryProviderResets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,1,1,11),_WanX25PvcHistoryProviderResets_Type())
wanX25PvcHistoryProviderResets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcHistoryProviderResets.setStatus(_A)
_WanX25PvcHistoryInAccusedErrors_Type=Counter64
_WanX25PvcHistoryInAccusedErrors_Object=MibTableColumn
wanX25PvcHistoryInAccusedErrors=_WanX25PvcHistoryInAccusedErrors_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,1,1,12),_WanX25PvcHistoryInAccusedErrors_Type())
wanX25PvcHistoryInAccusedErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcHistoryInAccusedErrors.setStatus(_A)
_WanX25PvcHistoryOutAccusedErrors_Type=Counter64
_WanX25PvcHistoryOutAccusedErrors_Object=MibTableColumn
wanX25PvcHistoryOutAccusedErrors=_WanX25PvcHistoryOutAccusedErrors_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,1,1,13),_WanX25PvcHistoryOutAccusedErrors_Type())
wanX25PvcHistoryOutAccusedErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcHistoryOutAccusedErrors.setStatus(_A)
_WanX25PvcHistoryInInterrupts_Type=Counter64
_WanX25PvcHistoryInInterrupts_Object=MibTableColumn
wanX25PvcHistoryInInterrupts=_WanX25PvcHistoryInInterrupts_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,1,1,14),_WanX25PvcHistoryInInterrupts_Type())
wanX25PvcHistoryInInterrupts.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcHistoryInInterrupts.setStatus(_A)
_WanX25PvcHistoryOutInterrupts_Type=Counter64
_WanX25PvcHistoryOutInterrupts_Object=MibTableColumn
wanX25PvcHistoryOutInterrupts=_WanX25PvcHistoryOutInterrupts_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,1,1,15),_WanX25PvcHistoryOutInterrupts_Type())
wanX25PvcHistoryOutInterrupts.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcHistoryOutInterrupts.setStatus(_A)
_WanX25PvcHistoryUpTime_Type=TimeTicks
_WanX25PvcHistoryUpTime_Object=MibTableColumn
wanX25PvcHistoryUpTime=_WanX25PvcHistoryUpTime_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,1,1,16),_WanX25PvcHistoryUpTime_Type())
wanX25PvcHistoryUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcHistoryUpTime.setStatus(_A)
_WanX25PvcHistoryDownTime_Type=TimeTicks
_WanX25PvcHistoryDownTime_Object=MibTableColumn
wanX25PvcHistoryDownTime=_WanX25PvcHistoryDownTime_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,1,1,17),_WanX25PvcHistoryDownTime_Type())
wanX25PvcHistoryDownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcHistoryDownTime.setStatus(_A)
_WanX25PvcHistoryStateChanges_Type=Counter64
_WanX25PvcHistoryStateChanges_Object=MibTableColumn
wanX25PvcHistoryStateChanges=_WanX25PvcHistoryStateChanges_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,1,1,18),_WanX25PvcHistoryStateChanges_Type())
wanX25PvcHistoryStateChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcHistoryStateChanges.setStatus(_A)
class _WanX25PvcHistoryInUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanX25PvcHistoryInUtilization_Type.__name__=_C
_WanX25PvcHistoryInUtilization_Object=MibTableColumn
wanX25PvcHistoryInUtilization=_WanX25PvcHistoryInUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,1,1,19),_WanX25PvcHistoryInUtilization_Type())
wanX25PvcHistoryInUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcHistoryInUtilization.setStatus(_A)
class _WanX25PvcHistoryOutUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanX25PvcHistoryOutUtilization_Type.__name__=_C
_WanX25PvcHistoryOutUtilization_Object=MibTableColumn
wanX25PvcHistoryOutUtilization=_WanX25PvcHistoryOutUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,1,1,20),_WanX25PvcHistoryOutUtilization_Type())
wanX25PvcHistoryOutUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanX25PvcHistoryOutUtilization.setStatus(_A)
_WanFrPvcHistoryTable_Object=MibTable
wanFrPvcHistoryTable=_WanFrPvcHistoryTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,2))
if mibBuilder.loadTexts:wanFrPvcHistoryTable.setStatus(_A)
_WanFrPvcHistoryEntry_Object=MibTableRow
wanFrPvcHistoryEntry=_WanFrPvcHistoryEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,2,1))
wanFrPvcHistoryEntry.setIndexNames((0,_E,_o),(0,_E,_p))
if mibBuilder.loadTexts:wanFrPvcHistoryEntry.setStatus(_A)
class _WanFrPvcHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanFrPvcHistoryIndex_Type.__name__=_C
_WanFrPvcHistoryIndex_Object=MibTableColumn
wanFrPvcHistoryIndex=_WanFrPvcHistoryIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,2,1,1),_WanFrPvcHistoryIndex_Type())
wanFrPvcHistoryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanFrPvcHistoryIndex.setStatus(_A)
class _WanFrPvcHistorySampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WanFrPvcHistorySampleIndex_Type.__name__=_C
_WanFrPvcHistorySampleIndex_Object=MibTableColumn
wanFrPvcHistorySampleIndex=_WanFrPvcHistorySampleIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,2,1,2),_WanFrPvcHistorySampleIndex_Type())
wanFrPvcHistorySampleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanFrPvcHistorySampleIndex.setStatus(_A)
_WanFrPvcHistoryIntervalStart_Type=TimeTicks
_WanFrPvcHistoryIntervalStart_Object=MibTableColumn
wanFrPvcHistoryIntervalStart=_WanFrPvcHistoryIntervalStart_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,2,1,3),_WanFrPvcHistoryIntervalStart_Type())
wanFrPvcHistoryIntervalStart.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcHistoryIntervalStart.setStatus(_A)
_WanFrPvcHistoryDropEvents_Type=Counter64
_WanFrPvcHistoryDropEvents_Object=MibTableColumn
wanFrPvcHistoryDropEvents=_WanFrPvcHistoryDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,2,1,4),_WanFrPvcHistoryDropEvents_Type())
wanFrPvcHistoryDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcHistoryDropEvents.setStatus(_A)
_WanFrPvcHistoryInFrames_Type=Counter64
_WanFrPvcHistoryInFrames_Object=MibTableColumn
wanFrPvcHistoryInFrames=_WanFrPvcHistoryInFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,2,1,5),_WanFrPvcHistoryInFrames_Type())
wanFrPvcHistoryInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcHistoryInFrames.setStatus(_A)
_WanFrPvcHistoryOutFrames_Type=Counter64
_WanFrPvcHistoryOutFrames_Object=MibTableColumn
wanFrPvcHistoryOutFrames=_WanFrPvcHistoryOutFrames_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,2,1,6),_WanFrPvcHistoryOutFrames_Type())
wanFrPvcHistoryOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcHistoryOutFrames.setStatus(_A)
_WanFrPvcHistoryInOctets_Type=Counter64
_WanFrPvcHistoryInOctets_Object=MibTableColumn
wanFrPvcHistoryInOctets=_WanFrPvcHistoryInOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,2,1,7),_WanFrPvcHistoryInOctets_Type())
wanFrPvcHistoryInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcHistoryInOctets.setStatus(_A)
_WanFrPvcHistoryOutOctets_Type=Counter64
_WanFrPvcHistoryOutOctets_Object=MibTableColumn
wanFrPvcHistoryOutOctets=_WanFrPvcHistoryOutOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,2,1,8),_WanFrPvcHistoryOutOctets_Type())
wanFrPvcHistoryOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcHistoryOutOctets.setStatus(_A)
_WanFrPvcHistoryInFECNs_Type=Counter64
_WanFrPvcHistoryInFECNs_Object=MibTableColumn
wanFrPvcHistoryInFECNs=_WanFrPvcHistoryInFECNs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,2,1,9),_WanFrPvcHistoryInFECNs_Type())
wanFrPvcHistoryInFECNs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcHistoryInFECNs.setStatus(_A)
_WanFrPvcHistoryOutFECNs_Type=Counter64
_WanFrPvcHistoryOutFECNs_Object=MibTableColumn
wanFrPvcHistoryOutFECNs=_WanFrPvcHistoryOutFECNs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,2,1,10),_WanFrPvcHistoryOutFECNs_Type())
wanFrPvcHistoryOutFECNs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcHistoryOutFECNs.setStatus(_A)
_WanFrPvcHistoryInBECNs_Type=Counter64
_WanFrPvcHistoryInBECNs_Object=MibTableColumn
wanFrPvcHistoryInBECNs=_WanFrPvcHistoryInBECNs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,2,1,11),_WanFrPvcHistoryInBECNs_Type())
wanFrPvcHistoryInBECNs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcHistoryInBECNs.setStatus(_A)
_WanFrPvcHistoryOutBECNs_Type=Counter64
_WanFrPvcHistoryOutBECNs_Object=MibTableColumn
wanFrPvcHistoryOutBECNs=_WanFrPvcHistoryOutBECNs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,2,1,12),_WanFrPvcHistoryOutBECNs_Type())
wanFrPvcHistoryOutBECNs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcHistoryOutBECNs.setStatus(_A)
_WanFrPvcHistoryInDEs_Type=Counter64
_WanFrPvcHistoryInDEs_Object=MibTableColumn
wanFrPvcHistoryInDEs=_WanFrPvcHistoryInDEs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,2,1,13),_WanFrPvcHistoryInDEs_Type())
wanFrPvcHistoryInDEs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcHistoryInDEs.setStatus(_A)
_WanFrPvcHistoryOutDEs_Type=Counter64
_WanFrPvcHistoryOutDEs_Object=MibTableColumn
wanFrPvcHistoryOutDEs=_WanFrPvcHistoryOutDEs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,2,1,14),_WanFrPvcHistoryOutDEs_Type())
wanFrPvcHistoryOutDEs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcHistoryOutDEs.setStatus(_A)
_WanFrPvcHistoryUpTime_Type=TimeTicks
_WanFrPvcHistoryUpTime_Object=MibTableColumn
wanFrPvcHistoryUpTime=_WanFrPvcHistoryUpTime_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,2,1,15),_WanFrPvcHistoryUpTime_Type())
wanFrPvcHistoryUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcHistoryUpTime.setStatus(_A)
_WanFrPvcHistoryDownTime_Type=TimeTicks
_WanFrPvcHistoryDownTime_Object=MibTableColumn
wanFrPvcHistoryDownTime=_WanFrPvcHistoryDownTime_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,2,1,16),_WanFrPvcHistoryDownTime_Type())
wanFrPvcHistoryDownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcHistoryDownTime.setStatus(_A)
_WanFrPvcHistoryStateChanges_Type=Counter64
_WanFrPvcHistoryStateChanges_Object=MibTableColumn
wanFrPvcHistoryStateChanges=_WanFrPvcHistoryStateChanges_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,2,1,17),_WanFrPvcHistoryStateChanges_Type())
wanFrPvcHistoryStateChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcHistoryStateChanges.setStatus(_A)
class _WanFrPvcHistoryInUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanFrPvcHistoryInUtilization_Type.__name__=_C
_WanFrPvcHistoryInUtilization_Object=MibTableColumn
wanFrPvcHistoryInUtilization=_WanFrPvcHistoryInUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,2,1,18),_WanFrPvcHistoryInUtilization_Type())
wanFrPvcHistoryInUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcHistoryInUtilization.setStatus(_A)
class _WanFrPvcHistoryOutUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanFrPvcHistoryOutUtilization_Type.__name__=_C
_WanFrPvcHistoryOutUtilization_Object=MibTableColumn
wanFrPvcHistoryOutUtilization=_WanFrPvcHistoryOutUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,2,1,19),_WanFrPvcHistoryOutUtilization_Type())
wanFrPvcHistoryOutUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanFrPvcHistoryOutUtilization.setStatus(_A)
_WanAal5PvcHistoryTable_Object=MibTable
wanAal5PvcHistoryTable=_WanAal5PvcHistoryTable_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3))
if mibBuilder.loadTexts:wanAal5PvcHistoryTable.setStatus(_A)
_WanAal5PvcHistoryEntry_Object=MibTableRow
wanAal5PvcHistoryEntry=_WanAal5PvcHistoryEntry_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3,1))
wanAal5PvcHistoryEntry.setIndexNames((0,_E,_q),(0,_E,_r))
if mibBuilder.loadTexts:wanAal5PvcHistoryEntry.setStatus(_A)
class _WanAal5PvcHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WanAal5PvcHistoryIndex_Type.__name__=_C
_WanAal5PvcHistoryIndex_Object=MibTableColumn
wanAal5PvcHistoryIndex=_WanAal5PvcHistoryIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3,1,1),_WanAal5PvcHistoryIndex_Type())
wanAal5PvcHistoryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanAal5PvcHistoryIndex.setStatus(_A)
class _WanAal5PvcHistorySampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WanAal5PvcHistorySampleIndex_Type.__name__=_C
_WanAal5PvcHistorySampleIndex_Object=MibTableColumn
wanAal5PvcHistorySampleIndex=_WanAal5PvcHistorySampleIndex_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3,1,2),_WanAal5PvcHistorySampleIndex_Type())
wanAal5PvcHistorySampleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:wanAal5PvcHistorySampleIndex.setStatus(_A)
_WanAal5PvcHistoryIntervalStart_Type=TimeTicks
_WanAal5PvcHistoryIntervalStart_Object=MibTableColumn
wanAal5PvcHistoryIntervalStart=_WanAal5PvcHistoryIntervalStart_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3,1,3),_WanAal5PvcHistoryIntervalStart_Type())
wanAal5PvcHistoryIntervalStart.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcHistoryIntervalStart.setStatus(_A)
_WanAal5PvcHistoryDropEvents_Type=Counter64
_WanAal5PvcHistoryDropEvents_Object=MibTableColumn
wanAal5PvcHistoryDropEvents=_WanAal5PvcHistoryDropEvents_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3,1,4),_WanAal5PvcHistoryDropEvents_Type())
wanAal5PvcHistoryDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcHistoryDropEvents.setStatus(_A)
_WanAal5PvcHistoryInCells_Type=Counter64
_WanAal5PvcHistoryInCells_Object=MibTableColumn
wanAal5PvcHistoryInCells=_WanAal5PvcHistoryInCells_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3,1,5),_WanAal5PvcHistoryInCells_Type())
wanAal5PvcHistoryInCells.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcHistoryInCells.setStatus(_A)
_WanAal5PvcHistoryOutCells_Type=Counter64
_WanAal5PvcHistoryOutCells_Object=MibTableColumn
wanAal5PvcHistoryOutCells=_WanAal5PvcHistoryOutCells_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3,1,6),_WanAal5PvcHistoryOutCells_Type())
wanAal5PvcHistoryOutCells.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcHistoryOutCells.setStatus(_A)
_WanAal5PvcHistoryInPDUs_Type=Counter64
_WanAal5PvcHistoryInPDUs_Object=MibTableColumn
wanAal5PvcHistoryInPDUs=_WanAal5PvcHistoryInPDUs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3,1,7),_WanAal5PvcHistoryInPDUs_Type())
wanAal5PvcHistoryInPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcHistoryInPDUs.setStatus(_A)
_WanAal5PvcHistoryOutPDUs_Type=Counter64
_WanAal5PvcHistoryOutPDUs_Object=MibTableColumn
wanAal5PvcHistoryOutPDUs=_WanAal5PvcHistoryOutPDUs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3,1,8),_WanAal5PvcHistoryOutPDUs_Type())
wanAal5PvcHistoryOutPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcHistoryOutPDUs.setStatus(_A)
_WanAal5PvcHistoryInOctets_Type=Counter64
_WanAal5PvcHistoryInOctets_Object=MibTableColumn
wanAal5PvcHistoryInOctets=_WanAal5PvcHistoryInOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3,1,9),_WanAal5PvcHistoryInOctets_Type())
wanAal5PvcHistoryInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcHistoryInOctets.setStatus(_A)
_WanAal5PvcHistoryOutOctets_Type=Counter64
_WanAal5PvcHistoryOutOctets_Object=MibTableColumn
wanAal5PvcHistoryOutOctets=_WanAal5PvcHistoryOutOctets_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3,1,10),_WanAal5PvcHistoryOutOctets_Type())
wanAal5PvcHistoryOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcHistoryOutOctets.setStatus(_A)
_WanAal5PvcHistoryInCLP1_Type=Counter64
_WanAal5PvcHistoryInCLP1_Object=MibTableColumn
wanAal5PvcHistoryInCLP1=_WanAal5PvcHistoryInCLP1_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3,1,11),_WanAal5PvcHistoryInCLP1_Type())
wanAal5PvcHistoryInCLP1.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcHistoryInCLP1.setStatus(_A)
_WanAal5PvcHistoryOutCLP1_Type=Counter64
_WanAal5PvcHistoryOutCLP1_Object=MibTableColumn
wanAal5PvcHistoryOutCLP1=_WanAal5PvcHistoryOutCLP1_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3,1,12),_WanAal5PvcHistoryOutCLP1_Type())
wanAal5PvcHistoryOutCLP1.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcHistoryOutCLP1.setStatus(_A)
_WanAal5PvcHistoryInCRCs_Type=Counter64
_WanAal5PvcHistoryInCRCs_Object=MibTableColumn
wanAal5PvcHistoryInCRCs=_WanAal5PvcHistoryInCRCs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3,1,13),_WanAal5PvcHistoryInCRCs_Type())
wanAal5PvcHistoryInCRCs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcHistoryInCRCs.setStatus(_A)
_WanAal5PvcHistoryOutCRCs_Type=Counter64
_WanAal5PvcHistoryOutCRCs_Object=MibTableColumn
wanAal5PvcHistoryOutCRCs=_WanAal5PvcHistoryOutCRCs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3,1,14),_WanAal5PvcHistoryOutCRCs_Type())
wanAal5PvcHistoryOutCRCs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcHistoryOutCRCs.setStatus(_A)
_WanAal5PvcHistoryInOversizedSDUs_Type=Counter64
_WanAal5PvcHistoryInOversizedSDUs_Object=MibTableColumn
wanAal5PvcHistoryInOversizedSDUs=_WanAal5PvcHistoryInOversizedSDUs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3,1,15),_WanAal5PvcHistoryInOversizedSDUs_Type())
wanAal5PvcHistoryInOversizedSDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcHistoryInOversizedSDUs.setStatus(_A)
_WanAal5PvcHistoryOutOversizedSDUs_Type=Counter64
_WanAal5PvcHistoryOutOversizedSDUs_Object=MibTableColumn
wanAal5PvcHistoryOutOversizedSDUs=_WanAal5PvcHistoryOutOversizedSDUs_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3,1,16),_WanAal5PvcHistoryOutOversizedSDUs_Type())
wanAal5PvcHistoryOutOversizedSDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcHistoryOutOversizedSDUs.setStatus(_A)
_WanAal5PvcHistoryUpTime_Type=TimeTicks
_WanAal5PvcHistoryUpTime_Object=MibTableColumn
wanAal5PvcHistoryUpTime=_WanAal5PvcHistoryUpTime_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3,1,17),_WanAal5PvcHistoryUpTime_Type())
wanAal5PvcHistoryUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcHistoryUpTime.setStatus(_A)
_WanAal5PvcHistoryDownTime_Type=TimeTicks
_WanAal5PvcHistoryDownTime_Object=MibTableColumn
wanAal5PvcHistoryDownTime=_WanAal5PvcHistoryDownTime_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3,1,18),_WanAal5PvcHistoryDownTime_Type())
wanAal5PvcHistoryDownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcHistoryDownTime.setStatus(_A)
_WanAal5PvcHistoryStateChanges_Type=Counter64
_WanAal5PvcHistoryStateChanges_Object=MibTableColumn
wanAal5PvcHistoryStateChanges=_WanAal5PvcHistoryStateChanges_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3,1,19),_WanAal5PvcHistoryStateChanges_Type())
wanAal5PvcHistoryStateChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcHistoryStateChanges.setStatus(_A)
class _WanAal5PvcHistoryInUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanAal5PvcHistoryInUtilization_Type.__name__=_C
_WanAal5PvcHistoryInUtilization_Object=MibTableColumn
wanAal5PvcHistoryInUtilization=_WanAal5PvcHistoryInUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3,1,20),_WanAal5PvcHistoryInUtilization_Type())
wanAal5PvcHistoryInUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcHistoryInUtilization.setStatus(_A)
class _WanAal5PvcHistoryOutUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WanAal5PvcHistoryOutUtilization_Type.__name__=_C
_WanAal5PvcHistoryOutUtilization_Object=MibTableColumn
wanAal5PvcHistoryOutUtilization=_WanAal5PvcHistoryOutUtilization_Object((1,3,6,1,4,1,11,2,3,7,6,1,5,1,8,2,3,3,1,21),_WanAal5PvcHistoryOutUtilization_Type())
wanAal5PvcHistoryOutUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:wanAal5PvcHistoryOutUtilization.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hp':hp,'nm':nm,'system':system,'netElement':netElement,'lanprobe':lanprobe,'general':general,'rmonExtension':rmonExtension,'statsExtension':statsExtension,'wanStatsMIB':wanStatsMIB,'wanStatsMIBObjects':wanStatsMIBObjects,'wanSignalingStats':wanSignalingStats,'wanT1E1StatsTable':wanT1E1StatsTable,'wanT1E1StatsEntry':wanT1E1StatsEntry,_K:wanT1E1StatsIndex,'wanT1E1StatsDataSource':wanT1E1StatsDataSource,'wanT1E1StatsDropEvents':wanT1E1StatsDropEvents,'wanT1E1StatsInFrames':wanT1E1StatsInFrames,'wanT1E1StatsOutFrames':wanT1E1StatsOutFrames,'wanT1E1StatsInOctets':wanT1E1StatsInOctets,'wanT1E1StatsOutOctets':wanT1E1StatsOutOctets,'wanT1E1StatsESs':wanT1E1StatsESs,'wanT1E1StatsSESs':wanT1E1StatsSESs,'wanT1E1StatsSEFSs':wanT1E1StatsSEFSs,'wanT1E1StatsOOFs':wanT1E1StatsOOFs,'wanT1E1StatsUASs':wanT1E1StatsUASs,'wanT1E1StatsCSSs':wanT1E1StatsCSSs,'wanT1E1StatsPCVs':wanT1E1StatsPCVs,'wanT1E1StatsLESs':wanT1E1StatsLESs,'wanT1E1StatsBESs':wanT1E1StatsBESs,'wanT1E1StatsDMs':wanT1E1StatsDMs,'wanT1E1StatsLCVs':wanT1E1StatsLCVs,'wanT1E1StatsLOFs':wanT1E1StatsLOFs,'wanT1E1StatsLOSs':wanT1E1StatsLOSs,'wanT1E1StatsRAIs':wanT1E1StatsRAIs,'wanT1E1StatsAISs':wanT1E1StatsAISs,'wanT1E1StatsTS16AISs':wanT1E1StatsTS16AISs,'wanT1E1StatsLOMFs':wanT1E1StatsLOMFs,'wanT1E1StatsFarLOMFs':wanT1E1StatsFarLOMFs,'wanT1E1StatsOwner':wanT1E1StatsOwner,'wanT1E1StatsStatus':wanT1E1StatsStatus,'wanVSeriesStatsTable':wanVSeriesStatsTable,'wanVSeriesStatsEntry':wanVSeriesStatsEntry,_L:wanVSeriesStatsIndex,'wanVSeriesStatsDataSource':wanVSeriesStatsDataSource,'wanVSeriesStatsDropEvents':wanVSeriesStatsDropEvents,'wanVSeriesStatsInFrames':wanVSeriesStatsInFrames,'wanVSeriesStatsOutFrames':wanVSeriesStatsOutFrames,'wanVSeriesStatsInOctets':wanVSeriesStatsInOctets,'wanVSeriesStatsOutOctets':wanVSeriesStatsOutOctets,'wanVSeriesStatsInFCSs':wanVSeriesStatsInFCSs,'wanVSeriesStatsOutFCSs':wanVSeriesStatsOutFCSs,'wanVSeriesStatsInOverruns':wanVSeriesStatsInOverruns,'wanVSeriesStatsOutOverruns':wanVSeriesStatsOutOverruns,'wanVSeriesStatsInterruptedFrames':wanVSeriesStatsInterruptedFrames,'wanVSeriesStatsInAbortedFrames':wanVSeriesStatsInAbortedFrames,'wanVSeriesStatsOutAbortedFrames':wanVSeriesStatsOutAbortedFrames,'wanVSeriesStatsOwner':wanVSeriesStatsOwner,'wanVSeriesStatsStatus':wanVSeriesStatsStatus,'wanHssiStatsTable':wanHssiStatsTable,'wanHssiStatsEntry':wanHssiStatsEntry,_M:wanHssiStatsIndex,'wanHssiStatsDataSource':wanHssiStatsDataSource,'wanHssiStatsDropEvents':wanHssiStatsDropEvents,'wanHssiStatsInFrames':wanHssiStatsInFrames,'wanHssiStatsOutFrames':wanHssiStatsOutFrames,'wanHssiStatsInOctets':wanHssiStatsInOctets,'wanHssiStatsOutOctets':wanHssiStatsOutOctets,'wanHssiStatsRxLongFrames':wanHssiStatsRxLongFrames,'wanHssiStatsRxCrcErrors':wanHssiStatsRxCrcErrors,'wanHssiStatsRxOverruns':wanHssiStatsRxOverruns,'wanHssiStatsRxAborts':wanHssiStatsRxAborts,'wanHssiStatsTxAborts':wanHssiStatsTxAborts,'wanHssiStatsTxUnderruns':wanHssiStatsTxUnderruns,'wanHssiStatsRxRingErrors':wanHssiStatsRxRingErrors,'wanHssiStatsRxRingOverruns':wanHssiStatsRxRingOverruns,'wanHssiStatsTxRingErrors':wanHssiStatsTxRingErrors,'wanHssiStatsPortOpErrors':wanHssiStatsPortOpErrors,'wanHssiStatsTxCmplProcessings':wanHssiStatsTxCmplProcessings,'wanHssiStatsOwner':wanHssiStatsOwner,'wanHssiStatsStatus':wanHssiStatsStatus,'wanT3E3StatsTable':wanT3E3StatsTable,'wanT3E3StatsEntry':wanT3E3StatsEntry,_N:wanT3E3StatsIndex,'wanT3E3StatsDataSource':wanT3E3StatsDataSource,'wanT3E3StatsDropEvents':wanT3E3StatsDropEvents,'wanT3E3StatsInFrames':wanT3E3StatsInFrames,'wanT3E3StatsOutFrames':wanT3E3StatsOutFrames,'wanT3E3StatsInOctets':wanT3E3StatsInOctets,'wanT3E3StatsOutOctets':wanT3E3StatsOutOctets,'wanT3E3StatsPESs':wanT3E3StatsPESs,'wanT3E3StatsPSESs':wanT3E3StatsPSESs,'wanT3E3StatsOOFs':wanT3E3StatsOOFs,'wanT3E3StatsSEFSs':wanT3E3StatsSEFSs,'wanT3E3StatsUASs':wanT3E3StatsUASs,'wanT3E3StatsLCVs':wanT3E3StatsLCVs,'wanT3E3StatsPCVs':wanT3E3StatsPCVs,'wanT3E3StatsLESs':wanT3E3StatsLESs,'wanT3E3StatsCCVs':wanT3E3StatsCCVs,'wanT3E3StatsCESs':wanT3E3StatsCESs,'wanT3E3StatsCSESs':wanT3E3StatsCSESs,'wanT3E3StatsRAIs':wanT3E3StatsRAIs,'wanT3E3StatsAISs':wanT3E3StatsAISs,'wanT3E3StatsLOFs':wanT3E3StatsLOFs,'wanT3E3StatsLOSs':wanT3E3StatsLOSs,'wanT3E3StatsOwner':wanT3E3StatsOwner,'wanT3E3StatsStatus':wanT3E3StatsStatus,'wanAtmStatsTable':wanAtmStatsTable,'wanAtmStatsEntry':wanAtmStatsEntry,_O:wanAtmStatsIndex,'wanAtmStatsDataSource':wanAtmStatsDataSource,'wanAtmStatsDropEvents':wanAtmStatsDropEvents,'wanAtmStatsInCells':wanAtmStatsInCells,'wanAtmStatsOutCells':wanAtmStatsOutCells,'wanAtmStatsInCLP1':wanAtmStatsInCLP1,'wanAtmStatsOutCLP1':wanAtmStatsOutCLP1,'wanAtmStatsConnectionEvents':wanAtmStatsConnectionEvents,'wanAtmStatsErroredPDUs':wanAtmStatsErroredPDUs,'wanAtmStatsSetupAttempts':wanAtmStatsSetupAttempts,'wanAtmStatsInRoutesUnavailable':wanAtmStatsInRoutesUnavailable,'wanAtmStatsOutRoutesUnavailable':wanAtmStatsOutRoutesUnavailable,'wanAtmStatsInResourcesUnavailable':wanAtmStatsInResourcesUnavailable,'wanAtmStatsOutResourcesUnavailable':wanAtmStatsOutResourcesUnavailable,'wanAtmStatsInUnsuccessfulCalls':wanAtmStatsInUnsuccessfulCalls,'wanAtmStatsOutUnsuccessfulCalls':wanAtmStatsOutUnsuccessfulCalls,'wanAtmStatsInIncorrectMsgs':wanAtmStatsInIncorrectMsgs,'wanAtmStatsOutIncorrectMsgs':wanAtmStatsOutIncorrectMsgs,'wanAtmStatsInPartyEvents':wanAtmStatsInPartyEvents,'wanAtmStatsOutPartyEvents':wanAtmStatsOutPartyEvents,'wanAtmStatsInExpiries':wanAtmStatsInExpiries,'wanAtmStatsOutExpiries':wanAtmStatsOutExpiries,'wanAtmStatsInRestartErrors':wanAtmStatsInRestartErrors,'wanAtmStatsOutRestartErrors':wanAtmStatsOutRestartErrors,'wanAtmStatsInSVCs':wanAtmStatsInSVCs,'wanAtmStatsOutSVCs':wanAtmStatsOutSVCs,'wanAtmStatsInOCDs':wanAtmStatsInOCDs,'wanAtmStatsOutOCDs':wanAtmStatsOutOCDs,'wanAtmStatsInLOCs':wanAtmStatsInLOCs,'wanAtmStatsOutLOCs':wanAtmStatsOutLOCs,'wanAtmStatsInLOFs':wanAtmStatsInLOFs,'wanAtmStatsOutLOFs':wanAtmStatsOutLOFs,'wanAtmStatsInLOPs':wanAtmStatsInLOPs,'wanAtmStatsOutLOPs':wanAtmStatsOutLOPs,'wanAtmStatsInLOSs':wanAtmStatsInLOSs,'wanAtmStatsOutLOSs':wanAtmStatsOutLOSs,'wanAtmStatsOwner':wanAtmStatsOwner,'wanAtmStatsStatus':wanAtmStatsStatus,'wanProtocolStats':wanProtocolStats,'wanX25StatsTable':wanX25StatsTable,'wanX25StatsEntry':wanX25StatsEntry,_H:wanX25StatsIndex,'wanX25StatsDataSource':wanX25StatsDataSource,'wanX25StatsDropEvents':wanX25StatsDropEvents,'wanX25StatsInFrames':wanX25StatsInFrames,'wanX25StatsOutFrames':wanX25StatsOutFrames,'wanX25StatsInOctets':wanX25StatsInOctets,'wanX25StatsOutOctets':wanX25StatsOutOctets,'wanX25StatsInRejects':wanX25StatsInRejects,'wanX25StatsOutRejects':wanX25StatsOutRejects,'wanX25StatsInAttempts':wanX25StatsInAttempts,'wanX25StatsOutAttempts':wanX25StatsOutAttempts,'wanX25StatsInFailures':wanX25StatsInFailures,'wanX25StatsOutFailures':wanX25StatsOutFailures,'wanX25StatsProviderClears':wanX25StatsProviderClears,'wanX25StatsInResets':wanX25StatsInResets,'wanX25StatsOutResets':wanX25StatsOutResets,'wanX25StatsProviderResets':wanX25StatsProviderResets,'wanX25StatsInAccusedErrors':wanX25StatsInAccusedErrors,'wanX25StatsOutAccusedErrors':wanX25StatsOutAccusedErrors,'wanX25StatsInInterrupts':wanX25StatsInInterrupts,'wanX25StatsOutInterrupts':wanX25StatsOutInterrupts,'wanX25StatsOwner':wanX25StatsOwner,'wanX25StatsStatus':wanX25StatsStatus,'wanFrStatsTable':wanFrStatsTable,'wanFrStatsEntry':wanFrStatsEntry,_P:wanFrStatsIndex,'wanFrStatsDataSource':wanFrStatsDataSource,'wanFrStatsDropEvents':wanFrStatsDropEvents,'wanFrStatsInFrames':wanFrStatsInFrames,'wanFrStatsOutFrames':wanFrStatsOutFrames,'wanFrStatsInOctets':wanFrStatsInOctets,'wanFrStatsOutOctets':wanFrStatsOutOctets,'wanFrStatsInFECNs':wanFrStatsInFECNs,'wanFrStatsOutFECNs':wanFrStatsOutFECNs,'wanFrStatsInBECNs':wanFrStatsInBECNs,'wanFrStatsOutBECNs':wanFrStatsOutBECNs,'wanFrStatsInDEs':wanFrStatsInDEs,'wanFrStatsOutDEs':wanFrStatsOutDEs,'wanFrStatsOwner':wanFrStatsOwner,'wanFrStatsStatus':wanFrStatsStatus,'wanAal5StatsTable':wanAal5StatsTable,'wanAal5StatsEntry':wanAal5StatsEntry,_Q:wanAal5StatsIndex,'wanAal5StatsDataSource':wanAal5StatsDataSource,'wanAal5StatsDropEvents':wanAal5StatsDropEvents,'wanAal5StatsInCells':wanAal5StatsInCells,'wanAal5StatsOutCells':wanAal5StatsOutCells,'wanAal5StatsInPDUs':wanAal5StatsInPDUs,'wanAal5StatsOutPDUs':wanAal5StatsOutPDUs,'wanAal5StatsInOctets':wanAal5StatsInOctets,'wanAal5StatsOutOctets':wanAal5StatsOutOctets,'wanAal5StatsInCLP1':wanAal5StatsInCLP1,'wanAal5StatsOutCLP1':wanAal5StatsOutCLP1,'wanAal5StatsInCRCs':wanAal5StatsInCRCs,'wanAal5StatsOutCRCs':wanAal5StatsOutCRCs,'wanAal5StatsInOversizedSDUs':wanAal5StatsInOversizedSDUs,'wanAal5StatsOutOversizedSDUs':wanAal5StatsOutOversizedSDUs,'wanAal5StatsInSVCs':wanAal5StatsInSVCs,'wanAal5StatsOutSVCs':wanAal5StatsOutSVCs,'wanAal5StatsOwner':wanAal5StatsOwner,'wanAal5StatsStatus':wanAal5StatsStatus,'wanPppStatsTable':wanPppStatsTable,'wanPppStatsEntry':wanPppStatsEntry,_R:wanPppStatsIndex,'wanPppStatsDataSource':wanPppStatsDataSource,'wanPppStatsDropEvents':wanPppStatsDropEvents,'wanPppStatsInFrames':wanPppStatsInFrames,'wanPppStatsOutFrames':wanPppStatsOutFrames,'wanPppStatsInOctets':wanPppStatsInOctets,'wanPppStatsOutOctets':wanPppStatsOutOctets,'wanPppStatsInBadAddresses':wanPppStatsInBadAddresses,'wanPppStatsOutBadAddresses':wanPppStatsOutBadAddresses,'wanPppStatsInBadControls':wanPppStatsInBadControls,'wanPppStatsOutBadControls':wanPppStatsOutBadControls,'wanPppStatsInLongFrames':wanPppStatsInLongFrames,'wanPppStatsOutLongFrames':wanPppStatsOutLongFrames,'wanPppStatsInBadFCSs':wanPppStatsInBadFCSs,'wanPppStatsOutBadFCSs':wanPppStatsOutBadFCSs,'wanPppStatsOwner':wanPppStatsOwner,'wanPppStatsStatus':wanPppStatsStatus,'wanPvcStats':wanPvcStats,'wanX25PvcStatsTable':wanX25PvcStatsTable,'wanX25PvcStatsEntry':wanX25PvcStatsEntry,'wanX25PvcStatsIndex':wanX25PvcStatsIndex,'wanX25PvcStatsDataSource':wanX25PvcStatsDataSource,'wanX25PvcStatsDropEvents':wanX25PvcStatsDropEvents,'wanX25PvcStatsInFrames':wanX25PvcStatsInFrames,'wanX25PvcStatsOutFrames':wanX25PvcStatsOutFrames,'wanX25PvcStatsInOctets':wanX25PvcStatsInOctets,'wanX25PvcStatsOutOctets':wanX25PvcStatsOutOctets,'wanX25PvcStatsInResets':wanX25PvcStatsInResets,'wanX25PvcStatsOutResets':wanX25PvcStatsOutResets,'wanX25PvcStatsProviderResets':wanX25PvcStatsProviderResets,'wanX25PvcStatsInAccusedErrors':wanX25PvcStatsInAccusedErrors,'wanX25PvcStatsOutAccusedErrors':wanX25PvcStatsOutAccusedErrors,'wanX25PvcStatsInInterrupts':wanX25PvcStatsInInterrupts,'wanX25PvcStatsOutInterrupts':wanX25PvcStatsOutInterrupts,'wanX25PvcStatsUpTime':wanX25PvcStatsUpTime,'wanX25PvcStatsDownTime':wanX25PvcStatsDownTime,'wanX25PvcStatsState':wanX25PvcStatsState,'wanX25PvcStatsStateChanges':wanX25PvcStatsStateChanges,'wanX25PvcStatsOwner':wanX25PvcStatsOwner,'wanX25PvcStatsStatus':wanX25PvcStatsStatus,'wanFrPvcStatsTable':wanFrPvcStatsTable,'wanFrPvcStatsEntry':wanFrPvcStatsEntry,_S:wanFrPvcStatsIndex,'wanFrPvcStatsDataSource':wanFrPvcStatsDataSource,'wanFrPvcStatsDropEvents':wanFrPvcStatsDropEvents,'wanFrPvcStatsInFrames':wanFrPvcStatsInFrames,'wanFrPvcStatsOutFrames':wanFrPvcStatsOutFrames,'wanFrPvcStatsInOctets':wanFrPvcStatsInOctets,'wanFrPvcStatsOutOctets':wanFrPvcStatsOutOctets,'wanFrPvcStatsInFECNs':wanFrPvcStatsInFECNs,'wanFrPvcStatsOutFECNs':wanFrPvcStatsOutFECNs,'wanFrPvcStatsInBECNs':wanFrPvcStatsInBECNs,'wanFrPvcStatsOutBECNs':wanFrPvcStatsOutBECNs,'wanFrPvcStatsInDEs':wanFrPvcStatsInDEs,'wanFrPvcStatsOutDEs':wanFrPvcStatsOutDEs,'wanFrPvcStatsUpTime':wanFrPvcStatsUpTime,'wanFrPvcStatsDownTime':wanFrPvcStatsDownTime,'wanFrPvcStatsState':wanFrPvcStatsState,'wanFrPvcStatsStateChanges':wanFrPvcStatsStateChanges,'wanFrPvcStatsOwner':wanFrPvcStatsOwner,'wanFrPvcStatsStatus':wanFrPvcStatsStatus,'wanAal5PvcStatsTable':wanAal5PvcStatsTable,'wanAal5PvcStatsEntry':wanAal5PvcStatsEntry,_T:wanAal5PvcStatsIndex,'wanAal5PvcStatsDataSource':wanAal5PvcStatsDataSource,'wanAal5PvcStatsDropEvents':wanAal5PvcStatsDropEvents,'wanAal5PvcStatsInCells':wanAal5PvcStatsInCells,'wanAal5PvcStatsOutCells':wanAal5PvcStatsOutCells,'wanAal5PvcStatsInPDUs':wanAal5PvcStatsInPDUs,'wanAal5PvcStatsOutPDUs':wanAal5PvcStatsOutPDUs,'wanAal5PvcStatsInOctets':wanAal5PvcStatsInOctets,'wanAal5PvcStatsOutOctets':wanAal5PvcStatsOutOctets,'wanAal5PvcStatsInCLP1':wanAal5PvcStatsInCLP1,'wanAal5PvcStatsOutCLP1':wanAal5PvcStatsOutCLP1,'wanAal5PvcStatsInCRCs':wanAal5PvcStatsInCRCs,'wanAal5PvcStatsOutCRCs':wanAal5PvcStatsOutCRCs,'wanAal5PvcStatsInOversizedSDUs':wanAal5PvcStatsInOversizedSDUs,'wanAal5PvcStatsOutOversizedSDUs':wanAal5PvcStatsOutOversizedSDUs,'wanAal5PvcStatsUpTime':wanAal5PvcStatsUpTime,'wanAal5PvcStatsDownTime':wanAal5PvcStatsDownTime,'wanAal5PvcStatsState':wanAal5PvcStatsState,'wanAal5PvcStatsStateChanges':wanAal5PvcStatsStateChanges,'wanAal5PvcStatsOwner':wanAal5PvcStatsOwner,'wanAal5PvcStatsStatus':wanAal5PvcStatsStatus,'wanHistoryMIBObjects':wanHistoryMIBObjects,'wanSignalingHistory':wanSignalingHistory,'wanT1E1HistoryTable':wanT1E1HistoryTable,'wanT1E1HistoryEntry':wanT1E1HistoryEntry,_U:wanT1E1HistoryIndex,_V:wanT1E1HistorySampleIndex,'wanT1E1HistoryIntervalStart':wanT1E1HistoryIntervalStart,'wanT1E1HistoryDropEvents':wanT1E1HistoryDropEvents,'wanT1E1HistoryInFrames':wanT1E1HistoryInFrames,'wanT1E1HistoryOutFrames':wanT1E1HistoryOutFrames,'wanT1E1HistoryInOctets':wanT1E1HistoryInOctets,'wanT1E1HistoryOutOctets':wanT1E1HistoryOutOctets,'wanT1E1HistoryESs':wanT1E1HistoryESs,'wanT1E1HistorySESs':wanT1E1HistorySESs,'wanT1E1HistorySEFSs':wanT1E1HistorySEFSs,'wanT1E1HistoryOOFs':wanT1E1HistoryOOFs,'wanT1E1HistoryUASs':wanT1E1HistoryUASs,'wanT1E1HistoryCSSs':wanT1E1HistoryCSSs,'wanT1E1HistoryPCVs':wanT1E1HistoryPCVs,'wanT1E1HistoryLESs':wanT1E1HistoryLESs,'wanT1E1HistoryBESs':wanT1E1HistoryBESs,'wanT1E1HistoryDMs':wanT1E1HistoryDMs,'wanT1E1HistoryLCVs':wanT1E1HistoryLCVs,'wanT1E1HistoryLOFs':wanT1E1HistoryLOFs,'wanT1E1HistoryLOSs':wanT1E1HistoryLOSs,'wanT1E1HistoryRAIs':wanT1E1HistoryRAIs,'wanT1E1HistoryAISs':wanT1E1HistoryAISs,'wanT1E1HistoryTS16AISs':wanT1E1HistoryTS16AISs,'wanT1E1HistoryLOMFs':wanT1E1HistoryLOMFs,'wanT1E1HistoryFarLOMFs':wanT1E1HistoryFarLOMFs,'wanT1E1HistoryInUtilization':wanT1E1HistoryInUtilization,'wanT1E1HistoryOutUtilization':wanT1E1HistoryOutUtilization,'wanVSeriesHistoryTable':wanVSeriesHistoryTable,'wanVSeriesHistoryEntry':wanVSeriesHistoryEntry,_W:wanVSeriesHistoryIndex,_X:wanVSeriesHistorySampleIndex,'wanVSeriesHistoryIntervalStart':wanVSeriesHistoryIntervalStart,'wanVSeriesHistoryDropEvents':wanVSeriesHistoryDropEvents,'wanVSeriesHistoryInFrames':wanVSeriesHistoryInFrames,'wanVSeriesHistoryOutFrames':wanVSeriesHistoryOutFrames,'wanVSeriesHistoryInOctets':wanVSeriesHistoryInOctets,'wanVSeriesHistoryOutOctets':wanVSeriesHistoryOutOctets,'wanVSeriesHistoryInFCSs':wanVSeriesHistoryInFCSs,'wanVSeriesHistoryOutFCSs':wanVSeriesHistoryOutFCSs,'wanVSeriesHistoryInOverruns':wanVSeriesHistoryInOverruns,'wanVSeriesHistoryOutOverruns':wanVSeriesHistoryOutOverruns,'wanVSeriesHistoryInterruptedFrames':wanVSeriesHistoryInterruptedFrames,'wanVSeriesHistoryInAbortedFrames':wanVSeriesHistoryInAbortedFrames,'wanVSeriesHistoryOutAbortedFrames':wanVSeriesHistoryOutAbortedFrames,'wanVSeriesHistoryInUtilization':wanVSeriesHistoryInUtilization,'wanVSeriesHistoryOutUtilization':wanVSeriesHistoryOutUtilization,'wanHssiHistoryTable':wanHssiHistoryTable,'wanHssiHistoryEntry':wanHssiHistoryEntry,_Y:wanHssiHistoryIndex,_Z:wanHssiHistorySampleIndex,'wanHssiHistoryIntervalStart':wanHssiHistoryIntervalStart,'wanHssiHistoryDropEvents':wanHssiHistoryDropEvents,'wanHssiHistoryInFrames':wanHssiHistoryInFrames,'wanHssiHistoryOutFrames':wanHssiHistoryOutFrames,'wanHssiHistoryInOctets':wanHssiHistoryInOctets,'wanHssiHistoryOutOctets':wanHssiHistoryOutOctets,'wanHssiHistoryRxLongFrames':wanHssiHistoryRxLongFrames,'wanHssiHistoryRxCrcErrors':wanHssiHistoryRxCrcErrors,'wanHssiHistoryRxOverruns':wanHssiHistoryRxOverruns,'wanHssiHistoryRxAborts':wanHssiHistoryRxAborts,'wanHssiHistoryTxAborts':wanHssiHistoryTxAborts,'wanHssiHistoryTxUnderruns':wanHssiHistoryTxUnderruns,'wanHssiHistoryRxRingErrors':wanHssiHistoryRxRingErrors,'wanHssiHistoryRxRingOverruns':wanHssiHistoryRxRingOverruns,'wanHssiHistoryTxRingErrors':wanHssiHistoryTxRingErrors,'wanHssiHistoryPortOpErrors':wanHssiHistoryPortOpErrors,'wanHssiHistoryTxCmplProcessings':wanHssiHistoryTxCmplProcessings,'wanHssiHistoryInUtilization':wanHssiHistoryInUtilization,'wanHssiHistoryOutUtilization':wanHssiHistoryOutUtilization,'wanT3E3HistoryTable':wanT3E3HistoryTable,'wanT3E3HistoryEntry':wanT3E3HistoryEntry,_a:wanT3E3HistoryIndex,_b:wanT3E3HistorySampleIndex,'wanT3E3HistoryIntervalStart':wanT3E3HistoryIntervalStart,'wanT3E3HistoryDropEvents':wanT3E3HistoryDropEvents,'wanT3E3HistoryInFrames':wanT3E3HistoryInFrames,'wanT3E3HistoryOutFrames':wanT3E3HistoryOutFrames,'wanT3E3HistoryInOctets':wanT3E3HistoryInOctets,'wanT3E3HistoryOutOctets':wanT3E3HistoryOutOctets,'wanT3E3HistoryPESs':wanT3E3HistoryPESs,'wanT3E3HistoryPSESs':wanT3E3HistoryPSESs,'wanT3E3HistoryOOFs':wanT3E3HistoryOOFs,'wanT3E3HistorySEFSs':wanT3E3HistorySEFSs,'wanT3E3HistoryUASs':wanT3E3HistoryUASs,'wanT3E3HistoryLCVs':wanT3E3HistoryLCVs,'wanT3E3HistoryPCVs':wanT3E3HistoryPCVs,'wanT3E3HistoryLESs':wanT3E3HistoryLESs,'wanT3E3HistoryCCVs':wanT3E3HistoryCCVs,'wanT3E3HistoryCESs':wanT3E3HistoryCESs,'wanT3E3HistoryCSESs':wanT3E3HistoryCSESs,'wanT3E3HistoryRAIs':wanT3E3HistoryRAIs,'wanT3E3HistoryAISs':wanT3E3HistoryAISs,'wanT3E3HistoryLOFs':wanT3E3HistoryLOFs,'wanT3E3HistoryLOSs':wanT3E3HistoryLOSs,'wanT3E3HistoryInUtilization':wanT3E3HistoryInUtilization,'wanT3E3HistoryOutUtilization':wanT3E3HistoryOutUtilization,'wanAtmHistoryTable':wanAtmHistoryTable,'wanAtmHistoryEntry':wanAtmHistoryEntry,_c:wanAtmHistoryIndex,_d:wanAtmHistorySampleIndex,'wanAtmHistoryIntervalStart':wanAtmHistoryIntervalStart,'wanAtmHistoryDropEvents':wanAtmHistoryDropEvents,'wanAtmHistoryInCells':wanAtmHistoryInCells,'wanAtmHistoryOutCells':wanAtmHistoryOutCells,'wanAtmHistoryInCLP1':wanAtmHistoryInCLP1,'wanAtmHistoryOutCLP1':wanAtmHistoryOutCLP1,'wanAtmHistoryConnectionEvents':wanAtmHistoryConnectionEvents,'wanAtmHistoryErroredPDUs':wanAtmHistoryErroredPDUs,'wanAtmHistorySetupAttempts':wanAtmHistorySetupAttempts,'wanAtmHistoryInRoutesUnavailable':wanAtmHistoryInRoutesUnavailable,'wanAtmHistoryOutRoutesUnavailable':wanAtmHistoryOutRoutesUnavailable,'wanAtmHistoryInResourcesUnavailable':wanAtmHistoryInResourcesUnavailable,'wanAtmHistoryOutResourcesUnavailable':wanAtmHistoryOutResourcesUnavailable,'wanAtmHistoryInUnsuccessfulCalls':wanAtmHistoryInUnsuccessfulCalls,'wanAtmHistoryOutUnsuccessfulCalls':wanAtmHistoryOutUnsuccessfulCalls,'wanAtmHistoryInIncorrectMsgs':wanAtmHistoryInIncorrectMsgs,'wanAtmHistoryOutIncorrectMsgs':wanAtmHistoryOutIncorrectMsgs,'wanAtmHistoryInPartyEvents':wanAtmHistoryInPartyEvents,'wanAtmHistoryOutPartyEvents':wanAtmHistoryOutPartyEvents,'wanAtmHistoryInExpiries':wanAtmHistoryInExpiries,'wanAtmHistoryOutExpiries':wanAtmHistoryOutExpiries,'wanAtmHistoryInRestartErrors':wanAtmHistoryInRestartErrors,'wanAtmHistoryOutRestartErrors':wanAtmHistoryOutRestartErrors,'wanAtmHistoryInSVCs':wanAtmHistoryInSVCs,'wanAtmHistoryOutSVCs':wanAtmHistoryOutSVCs,'wanAtmHistoryInOCDs':wanAtmHistoryInOCDs,'wanAtmHistoryOutOCDs':wanAtmHistoryOutOCDs,'wanAtmHistoryInLOCs':wanAtmHistoryInLOCs,'wanAtmHistoryOutLOCs':wanAtmHistoryOutLOCs,'wanAtmHistoryInLOFs':wanAtmHistoryInLOFs,'wanAtmHistoryOutLOFs':wanAtmHistoryOutLOFs,'wanAtmHistoryInLOPs':wanAtmHistoryInLOPs,'wanAtmHistoryOutLOPs':wanAtmHistoryOutLOPs,'wanAtmHistoryInLOSs':wanAtmHistoryInLOSs,'wanAtmHistoryOutLOSs':wanAtmHistoryOutLOSs,'wanAtmHistoryInUtilization':wanAtmHistoryInUtilization,'wanAtmHistoryOutUtilization':wanAtmHistoryOutUtilization,'wanProtocolHistory':wanProtocolHistory,'wanX25HistoryTable':wanX25HistoryTable,'wanX25HistoryEntry':wanX25HistoryEntry,_e:wanX25HistoryIndex,_f:wanX25HistorySampleIndex,'wanX25HistoryIntervalStart':wanX25HistoryIntervalStart,'wanX25HistoryDropEvents':wanX25HistoryDropEvents,'wanX25HistoryInFrames':wanX25HistoryInFrames,'wanX25HistoryOutFrames':wanX25HistoryOutFrames,'wanX25HistoryInOctets':wanX25HistoryInOctets,'wanX25HistoryOutOctets':wanX25HistoryOutOctets,'wanX25HistoryInRejects':wanX25HistoryInRejects,'wanX25HistoryOutRejects':wanX25HistoryOutRejects,'wanX25HistoryInAttempts':wanX25HistoryInAttempts,'wanX25HistoryOutAttempts':wanX25HistoryOutAttempts,'wanX25HistoryInFailures':wanX25HistoryInFailures,'wanX25HistoryOutFailures':wanX25HistoryOutFailures,'wanX25HistoryProviderClears':wanX25HistoryProviderClears,'wanX25HistoryInResets':wanX25HistoryInResets,'wanX25HistoryOutResets':wanX25HistoryOutResets,'wanX25HistoryProviderResets':wanX25HistoryProviderResets,'wanX25HistoryInAccusedErrors':wanX25HistoryInAccusedErrors,'wanX25HistoryOutAccusedErrors':wanX25HistoryOutAccusedErrors,'wanX25HistoryInInterrupts':wanX25HistoryInInterrupts,'wanX25HistoryOutInterrupts':wanX25HistoryOutInterrupts,'wanX25HistoryInUtilization':wanX25HistoryInUtilization,'wanX25HistoryOutUtilization':wanX25HistoryOutUtilization,'wanFrHistoryTable':wanFrHistoryTable,'wanFrHistoryEntry':wanFrHistoryEntry,_g:wanFrHistoryIndex,_h:wanFrHistorySampleIndex,'wanFrHistoryIntervalStart':wanFrHistoryIntervalStart,'wanFrHistoryDropEvents':wanFrHistoryDropEvents,'wanFrHistoryInFrames':wanFrHistoryInFrames,'wanFrHistoryOutFrames':wanFrHistoryOutFrames,'wanFrHistoryInOctets':wanFrHistoryInOctets,'wanFrHistoryOutOctets':wanFrHistoryOutOctets,'wanFrHistoryInFECNs':wanFrHistoryInFECNs,'wanFrHistoryOutFECNs':wanFrHistoryOutFECNs,'wanFrHistoryInBECNs':wanFrHistoryInBECNs,'wanFrHistoryOutBECNs':wanFrHistoryOutBECNs,'wanFrHistoryInDEs':wanFrHistoryInDEs,'wanFrHistoryOutDEs':wanFrHistoryOutDEs,'wanFrHistoryInUtilization':wanFrHistoryInUtilization,'wanFrHistoryOutUtilization':wanFrHistoryOutUtilization,'wanAal5HistoryTable':wanAal5HistoryTable,'wanAal5HistoryEntry':wanAal5HistoryEntry,_i:wanAal5HistoryIndex,_j:wanAal5HistorySampleIndex,'wanAal5HistoryIntervalStart':wanAal5HistoryIntervalStart,'wanAal5HistoryDropEvents':wanAal5HistoryDropEvents,'wanAal5HistoryInCells':wanAal5HistoryInCells,'wanAal5HistoryOutCells':wanAal5HistoryOutCells,'wanAal5HistoryInPDUs':wanAal5HistoryInPDUs,'wanAal5HistoryOutPDUs':wanAal5HistoryOutPDUs,'wanAal5HistoryInOctets':wanAal5HistoryInOctets,'wanAal5HistoryOutOctets':wanAal5HistoryOutOctets,'wanAal5HistoryInCLP1':wanAal5HistoryInCLP1,'wanAal5HistoryOutCLP1':wanAal5HistoryOutCLP1,'wanAal5HistoryInCRCs':wanAal5HistoryInCRCs,'wanAal5HistoryOutCRCs':wanAal5HistoryOutCRCs,'wanAal5HistoryInOversizedSDUs':wanAal5HistoryInOversizedSDUs,'wanAal5HistoryOutOversizedSDUs':wanAal5HistoryOutOversizedSDUs,'wanAal5HistoryInSVCs':wanAal5HistoryInSVCs,'wanAal5HistoryOutSVCs':wanAal5HistoryOutSVCs,'wanAal5HistoryInUtilization':wanAal5HistoryInUtilization,'wanAal5HistoryOutUtilization':wanAal5HistoryOutUtilization,'wanPppHistoryTable':wanPppHistoryTable,'wanPppHistoryEntry':wanPppHistoryEntry,_k:wanPppHistoryIndex,_l:wanPppHistorySampleIndex,'wanPppHistoryIntervalStart':wanPppHistoryIntervalStart,'wanPppHistoryDropEvents':wanPppHistoryDropEvents,'wanPppHistoryInFrames':wanPppHistoryInFrames,'wanPppHistoryOutFrames':wanPppHistoryOutFrames,'wanPppHistoryInOctets':wanPppHistoryInOctets,'wanPppHistoryOutOctets':wanPppHistoryOutOctets,'wanPppHistoryInBadAddresses':wanPppHistoryInBadAddresses,'wanPppHistoryOutBadAddresses':wanPppHistoryOutBadAddresses,'wanPppHistoryInBadControls':wanPppHistoryInBadControls,'wanPppHistoryOutBadControls':wanPppHistoryOutBadControls,'wanPppHistoryInLongFrames':wanPppHistoryInLongFrames,'wanPppHistoryOutLongFrames':wanPppHistoryOutLongFrames,'wanPppHistoryInBadFCSs':wanPppHistoryInBadFCSs,'wanPppHistoryOutBadFCSs':wanPppHistoryOutBadFCSs,'wanPppHistoryInUtilization':wanPppHistoryInUtilization,'wanPppHistoryOutUtilization':wanPppHistoryOutUtilization,'wanPvcHistory':wanPvcHistory,'wanX25PvcHistoryTable':wanX25PvcHistoryTable,'wanX25PvcHistoryEntry':wanX25PvcHistoryEntry,_m:wanX25PvcHistoryIndex,_n:wanX25PvcHistorySampleIndex,'wanX25PvcHistoryIntervalStart':wanX25PvcHistoryIntervalStart,'wanX25PvcHistoryDropEvents':wanX25PvcHistoryDropEvents,'wanX25PvcHistoryInFrames':wanX25PvcHistoryInFrames,'wanX25PvcHistoryOutFrames':wanX25PvcHistoryOutFrames,'wanX25PvcHistoryInOctets':wanX25PvcHistoryInOctets,'wanX25PvcHistoryOutOctets':wanX25PvcHistoryOutOctets,'wanX25PvcHistoryInResets':wanX25PvcHistoryInResets,'wanX25PvcHistoryOutResets':wanX25PvcHistoryOutResets,'wanX25PvcHistoryProviderResets':wanX25PvcHistoryProviderResets,'wanX25PvcHistoryInAccusedErrors':wanX25PvcHistoryInAccusedErrors,'wanX25PvcHistoryOutAccusedErrors':wanX25PvcHistoryOutAccusedErrors,'wanX25PvcHistoryInInterrupts':wanX25PvcHistoryInInterrupts,'wanX25PvcHistoryOutInterrupts':wanX25PvcHistoryOutInterrupts,'wanX25PvcHistoryUpTime':wanX25PvcHistoryUpTime,'wanX25PvcHistoryDownTime':wanX25PvcHistoryDownTime,'wanX25PvcHistoryStateChanges':wanX25PvcHistoryStateChanges,'wanX25PvcHistoryInUtilization':wanX25PvcHistoryInUtilization,'wanX25PvcHistoryOutUtilization':wanX25PvcHistoryOutUtilization,'wanFrPvcHistoryTable':wanFrPvcHistoryTable,'wanFrPvcHistoryEntry':wanFrPvcHistoryEntry,_o:wanFrPvcHistoryIndex,_p:wanFrPvcHistorySampleIndex,'wanFrPvcHistoryIntervalStart':wanFrPvcHistoryIntervalStart,'wanFrPvcHistoryDropEvents':wanFrPvcHistoryDropEvents,'wanFrPvcHistoryInFrames':wanFrPvcHistoryInFrames,'wanFrPvcHistoryOutFrames':wanFrPvcHistoryOutFrames,'wanFrPvcHistoryInOctets':wanFrPvcHistoryInOctets,'wanFrPvcHistoryOutOctets':wanFrPvcHistoryOutOctets,'wanFrPvcHistoryInFECNs':wanFrPvcHistoryInFECNs,'wanFrPvcHistoryOutFECNs':wanFrPvcHistoryOutFECNs,'wanFrPvcHistoryInBECNs':wanFrPvcHistoryInBECNs,'wanFrPvcHistoryOutBECNs':wanFrPvcHistoryOutBECNs,'wanFrPvcHistoryInDEs':wanFrPvcHistoryInDEs,'wanFrPvcHistoryOutDEs':wanFrPvcHistoryOutDEs,'wanFrPvcHistoryUpTime':wanFrPvcHistoryUpTime,'wanFrPvcHistoryDownTime':wanFrPvcHistoryDownTime,'wanFrPvcHistoryStateChanges':wanFrPvcHistoryStateChanges,'wanFrPvcHistoryInUtilization':wanFrPvcHistoryInUtilization,'wanFrPvcHistoryOutUtilization':wanFrPvcHistoryOutUtilization,'wanAal5PvcHistoryTable':wanAal5PvcHistoryTable,'wanAal5PvcHistoryEntry':wanAal5PvcHistoryEntry,_q:wanAal5PvcHistoryIndex,_r:wanAal5PvcHistorySampleIndex,'wanAal5PvcHistoryIntervalStart':wanAal5PvcHistoryIntervalStart,'wanAal5PvcHistoryDropEvents':wanAal5PvcHistoryDropEvents,'wanAal5PvcHistoryInCells':wanAal5PvcHistoryInCells,'wanAal5PvcHistoryOutCells':wanAal5PvcHistoryOutCells,'wanAal5PvcHistoryInPDUs':wanAal5PvcHistoryInPDUs,'wanAal5PvcHistoryOutPDUs':wanAal5PvcHistoryOutPDUs,'wanAal5PvcHistoryInOctets':wanAal5PvcHistoryInOctets,'wanAal5PvcHistoryOutOctets':wanAal5PvcHistoryOutOctets,'wanAal5PvcHistoryInCLP1':wanAal5PvcHistoryInCLP1,'wanAal5PvcHistoryOutCLP1':wanAal5PvcHistoryOutCLP1,'wanAal5PvcHistoryInCRCs':wanAal5PvcHistoryInCRCs,'wanAal5PvcHistoryOutCRCs':wanAal5PvcHistoryOutCRCs,'wanAal5PvcHistoryInOversizedSDUs':wanAal5PvcHistoryInOversizedSDUs,'wanAal5PvcHistoryOutOversizedSDUs':wanAal5PvcHistoryOutOversizedSDUs,'wanAal5PvcHistoryUpTime':wanAal5PvcHistoryUpTime,'wanAal5PvcHistoryDownTime':wanAal5PvcHistoryDownTime,'wanAal5PvcHistoryStateChanges':wanAal5PvcHistoryStateChanges,'wanAal5PvcHistoryInUtilization':wanAal5PvcHistoryInUtilization,'wanAal5PvcHistoryOutUtilization':wanAal5PvcHistoryOutUtilization})