_E='extremeRtStatsIndex'
_D='EXTREME-RTSTATS-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
extremeRtStats=ModuleIdentity((1,3,6,1,4,1,1916,1,11))
_ExtremeRtStatsTable_Object=MibTable
extremeRtStatsTable=_ExtremeRtStatsTable_Object((1,3,6,1,4,1,1916,1,11,1))
if mibBuilder.loadTexts:extremeRtStatsTable.setStatus(_A)
_ExtremeRtStatsEntry_Object=MibTableRow
extremeRtStatsEntry=_ExtremeRtStatsEntry_Object((1,3,6,1,4,1,1916,1,11,1,1))
extremeRtStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:extremeRtStatsEntry.setStatus(_A)
class _ExtremeRtStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeRtStatsIndex_Type.__name__=_C
_ExtremeRtStatsIndex_Object=MibTableColumn
extremeRtStatsIndex=_ExtremeRtStatsIndex_Object((1,3,6,1,4,1,1916,1,11,1,1,1),_ExtremeRtStatsIndex_Type())
extremeRtStatsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeRtStatsIndex.setStatus(_A)
_ExtremeRtStatsIntervalStart_Type=TimeTicks
_ExtremeRtStatsIntervalStart_Object=MibTableColumn
extremeRtStatsIntervalStart=_ExtremeRtStatsIntervalStart_Object((1,3,6,1,4,1,1916,1,11,1,1,2),_ExtremeRtStatsIntervalStart_Type())
extremeRtStatsIntervalStart.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeRtStatsIntervalStart.setStatus(_A)
_ExtremeRtStatsCRCAlignErrors_Type=Counter32
_ExtremeRtStatsCRCAlignErrors_Object=MibTableColumn
extremeRtStatsCRCAlignErrors=_ExtremeRtStatsCRCAlignErrors_Object((1,3,6,1,4,1,1916,1,11,1,1,3),_ExtremeRtStatsCRCAlignErrors_Type())
extremeRtStatsCRCAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeRtStatsCRCAlignErrors.setStatus(_A)
_ExtremeRtStatsUndersizePkts_Type=Counter32
_ExtremeRtStatsUndersizePkts_Object=MibTableColumn
extremeRtStatsUndersizePkts=_ExtremeRtStatsUndersizePkts_Object((1,3,6,1,4,1,1916,1,11,1,1,4),_ExtremeRtStatsUndersizePkts_Type())
extremeRtStatsUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeRtStatsUndersizePkts.setStatus(_A)
_ExtremeRtStatsOversizePkts_Type=Counter32
_ExtremeRtStatsOversizePkts_Object=MibTableColumn
extremeRtStatsOversizePkts=_ExtremeRtStatsOversizePkts_Object((1,3,6,1,4,1,1916,1,11,1,1,5),_ExtremeRtStatsOversizePkts_Type())
extremeRtStatsOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeRtStatsOversizePkts.setStatus(_A)
_ExtremeRtStatsFragments_Type=Counter32
_ExtremeRtStatsFragments_Object=MibTableColumn
extremeRtStatsFragments=_ExtremeRtStatsFragments_Object((1,3,6,1,4,1,1916,1,11,1,1,6),_ExtremeRtStatsFragments_Type())
extremeRtStatsFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeRtStatsFragments.setStatus(_A)
_ExtremeRtStatsJabbers_Type=Counter32
_ExtremeRtStatsJabbers_Object=MibTableColumn
extremeRtStatsJabbers=_ExtremeRtStatsJabbers_Object((1,3,6,1,4,1,1916,1,11,1,1,7),_ExtremeRtStatsJabbers_Type())
extremeRtStatsJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeRtStatsJabbers.setStatus(_A)
_ExtremeRtStatsCollisions_Type=Counter32
_ExtremeRtStatsCollisions_Object=MibTableColumn
extremeRtStatsCollisions=_ExtremeRtStatsCollisions_Object((1,3,6,1,4,1,1916,1,11,1,1,8),_ExtremeRtStatsCollisions_Type())
extremeRtStatsCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeRtStatsCollisions.setStatus(_A)
_ExtremeRtStatsTotalErrors_Type=Counter32
_ExtremeRtStatsTotalErrors_Object=MibTableColumn
extremeRtStatsTotalErrors=_ExtremeRtStatsTotalErrors_Object((1,3,6,1,4,1,1916,1,11,1,1,9),_ExtremeRtStatsTotalErrors_Type())
extremeRtStatsTotalErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeRtStatsTotalErrors.setStatus(_A)
class _ExtremeRtStatsUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_ExtremeRtStatsUtilization_Type.__name__=_C
_ExtremeRtStatsUtilization_Object=MibTableColumn
extremeRtStatsUtilization=_ExtremeRtStatsUtilization_Object((1,3,6,1,4,1,1916,1,11,1,1,10),_ExtremeRtStatsUtilization_Type())
extremeRtStatsUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeRtStatsUtilization.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'extremeRtStats':extremeRtStats,'extremeRtStatsTable':extremeRtStatsTable,'extremeRtStatsEntry':extremeRtStatsEntry,_E:extremeRtStatsIndex,'extremeRtStatsIntervalStart':extremeRtStatsIntervalStart,'extremeRtStatsCRCAlignErrors':extremeRtStatsCRCAlignErrors,'extremeRtStatsUndersizePkts':extremeRtStatsUndersizePkts,'extremeRtStatsOversizePkts':extremeRtStatsOversizePkts,'extremeRtStatsFragments':extremeRtStatsFragments,'extremeRtStatsJabbers':extremeRtStatsJabbers,'extremeRtStatsCollisions':extremeRtStatsCollisions,'extremeRtStatsTotalErrors':extremeRtStatsTotalErrors,'extremeRtStatsUtilization':extremeRtStatsUtilization})