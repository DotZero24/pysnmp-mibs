_L='wwpLeosPortTotalHCStatsPortId'
_K='wwpLeosPortHCStatsPortId'
_J='wwpLeosPortTotalStatsPortId'
_I='wwpLeosPortStatsPortId'
_H='deprecated'
_G='WWP-LEOS-PORT-STATS-MIB'
_F='read-write'
_E='reset'
_D='none'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
wwpModules,wwpModulesLeos=mibBuilder.importSymbols('WWP-SMI','wwpModules','wwpModulesLeos')
wwpLeosPortStatsMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,3))
if mibBuilder.loadTexts:wwpLeosPortStatsMIB.setRevisions(('2012-11-16 00:00','2010-02-12 00:00','2001-04-03 17:00'))
_WwpLeosPortStatsMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosPortStatsMIBObjects=_WwpLeosPortStatsMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,3,1))
_WwpLeosPortStats_ObjectIdentity=ObjectIdentity
wwpLeosPortStats=_WwpLeosPortStats_ObjectIdentity((1,3,6,1,4,1,6141,2,60,3,1,1))
class _WwpLeosPortStatsReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_WwpLeosPortStatsReset_Type.__name__=_C
_WwpLeosPortStatsReset_Object=MibScalar
wwpLeosPortStatsReset=_WwpLeosPortStatsReset_Object((1,3,6,1,4,1,6141,2,60,3,1,1,1),_WwpLeosPortStatsReset_Type())
wwpLeosPortStatsReset.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosPortStatsReset.setStatus(_A)
_WwpLeosPortStatsTable_Object=MibTable
wwpLeosPortStatsTable=_WwpLeosPortStatsTable_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2))
if mibBuilder.loadTexts:wwpLeosPortStatsTable.setStatus(_A)
_WwpLeosPortStatsEntry_Object=MibTableRow
wwpLeosPortStatsEntry=_WwpLeosPortStatsEntry_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1))
wwpLeosPortStatsEntry.setIndexNames((0,_G,_I))
if mibBuilder.loadTexts:wwpLeosPortStatsEntry.setStatus(_A)
class _WwpLeosPortStatsPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortStatsPortId_Type.__name__=_C
_WwpLeosPortStatsPortId_Object=MibTableColumn
wwpLeosPortStatsPortId=_WwpLeosPortStatsPortId_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,1),_WwpLeosPortStatsPortId_Type())
wwpLeosPortStatsPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsPortId.setStatus(_A)
_WwpLeosPortStatsRxBytes_Type=Counter32
_WwpLeosPortStatsRxBytes_Object=MibTableColumn
wwpLeosPortStatsRxBytes=_WwpLeosPortStatsRxBytes_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,2),_WwpLeosPortStatsRxBytes_Type())
wwpLeosPortStatsRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsRxBytes.setStatus(_A)
_WwpLeosPortStatsRxPkts_Type=Counter32
_WwpLeosPortStatsRxPkts_Object=MibTableColumn
wwpLeosPortStatsRxPkts=_WwpLeosPortStatsRxPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,3),_WwpLeosPortStatsRxPkts_Type())
wwpLeosPortStatsRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsRxPkts.setStatus(_A)
_WwpLeosPortStatsRxCrcErrorPkts_Type=Counter32
_WwpLeosPortStatsRxCrcErrorPkts_Object=MibTableColumn
wwpLeosPortStatsRxCrcErrorPkts=_WwpLeosPortStatsRxCrcErrorPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,4),_WwpLeosPortStatsRxCrcErrorPkts_Type())
wwpLeosPortStatsRxCrcErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsRxCrcErrorPkts.setStatus(_A)
_WwpLeosPortStatsRxBcastPkts_Type=Counter32
_WwpLeosPortStatsRxBcastPkts_Object=MibTableColumn
wwpLeosPortStatsRxBcastPkts=_WwpLeosPortStatsRxBcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,5),_WwpLeosPortStatsRxBcastPkts_Type())
wwpLeosPortStatsRxBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsRxBcastPkts.setStatus(_A)
_WwpLeosPortStatsUndersizePkts_Type=Counter32
_WwpLeosPortStatsUndersizePkts_Object=MibTableColumn
wwpLeosPortStatsUndersizePkts=_WwpLeosPortStatsUndersizePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,6),_WwpLeosPortStatsUndersizePkts_Type())
wwpLeosPortStatsUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsUndersizePkts.setStatus(_A)
_WwpLeosPortStatsOversizePkts_Type=Counter32
_WwpLeosPortStatsOversizePkts_Object=MibTableColumn
wwpLeosPortStatsOversizePkts=_WwpLeosPortStatsOversizePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,7),_WwpLeosPortStatsOversizePkts_Type())
wwpLeosPortStatsOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsOversizePkts.setStatus(_A)
_WwpLeosPortStatsFragmentPkts_Type=Counter32
_WwpLeosPortStatsFragmentPkts_Object=MibTableColumn
wwpLeosPortStatsFragmentPkts=_WwpLeosPortStatsFragmentPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,8),_WwpLeosPortStatsFragmentPkts_Type())
wwpLeosPortStatsFragmentPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsFragmentPkts.setStatus(_A)
_WwpLeosPortStatsJabberPkts_Type=Counter32
_WwpLeosPortStatsJabberPkts_Object=MibTableColumn
wwpLeosPortStatsJabberPkts=_WwpLeosPortStatsJabberPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,9),_WwpLeosPortStatsJabberPkts_Type())
wwpLeosPortStatsJabberPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsJabberPkts.setStatus(_A)
_WwpLeosPortStats64BytePkts_Type=Counter32
_WwpLeosPortStats64BytePkts_Object=MibTableColumn
wwpLeosPortStats64BytePkts=_WwpLeosPortStats64BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,10),_WwpLeosPortStats64BytePkts_Type())
wwpLeosPortStats64BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStats64BytePkts.setStatus(_A)
_WwpLeosPortStats65To127BytePkts_Type=Counter32
_WwpLeosPortStats65To127BytePkts_Object=MibTableColumn
wwpLeosPortStats65To127BytePkts=_WwpLeosPortStats65To127BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,11),_WwpLeosPortStats65To127BytePkts_Type())
wwpLeosPortStats65To127BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStats65To127BytePkts.setStatus(_A)
_WwpLeosPortStats128To255BytePkts_Type=Counter32
_WwpLeosPortStats128To255BytePkts_Object=MibTableColumn
wwpLeosPortStats128To255BytePkts=_WwpLeosPortStats128To255BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,12),_WwpLeosPortStats128To255BytePkts_Type())
wwpLeosPortStats128To255BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStats128To255BytePkts.setStatus(_A)
_WwpLeosPortStats256To511BytePkts_Type=Counter32
_WwpLeosPortStats256To511BytePkts_Object=MibTableColumn
wwpLeosPortStats256To511BytePkts=_WwpLeosPortStats256To511BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,13),_WwpLeosPortStats256To511BytePkts_Type())
wwpLeosPortStats256To511BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStats256To511BytePkts.setStatus(_A)
_WwpLeosPortStats512To1023BytePkts_Type=Counter32
_WwpLeosPortStats512To1023BytePkts_Object=MibTableColumn
wwpLeosPortStats512To1023BytePkts=_WwpLeosPortStats512To1023BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,14),_WwpLeosPortStats512To1023BytePkts_Type())
wwpLeosPortStats512To1023BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStats512To1023BytePkts.setStatus(_A)
_WwpLeosPortStats1024To1518BytePkts_Type=Counter32
_WwpLeosPortStats1024To1518BytePkts_Object=MibTableColumn
wwpLeosPortStats1024To1518BytePkts=_WwpLeosPortStats1024To1518BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,15),_WwpLeosPortStats1024To1518BytePkts_Type())
wwpLeosPortStats1024To1518BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStats1024To1518BytePkts.setStatus(_A)
_WwpLeosPortStatsTxBytes_Type=Counter32
_WwpLeosPortStatsTxBytes_Object=MibTableColumn
wwpLeosPortStatsTxBytes=_WwpLeosPortStatsTxBytes_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,16),_WwpLeosPortStatsTxBytes_Type())
wwpLeosPortStatsTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTxBytes.setStatus(_A)
_WwpLeosPortStatsTxTBytes_Type=Counter32
_WwpLeosPortStatsTxTBytes_Object=MibTableColumn
wwpLeosPortStatsTxTBytes=_WwpLeosPortStatsTxTBytes_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,17),_WwpLeosPortStatsTxTBytes_Type())
wwpLeosPortStatsTxTBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTxTBytes.setStatus(_H)
_WwpLeosPortStatsTxPkts_Type=Counter32
_WwpLeosPortStatsTxPkts_Object=MibTableColumn
wwpLeosPortStatsTxPkts=_WwpLeosPortStatsTxPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,18),_WwpLeosPortStatsTxPkts_Type())
wwpLeosPortStatsTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTxPkts.setStatus(_A)
_WwpLeosPortStatsTxExDeferPkts_Type=Counter32
_WwpLeosPortStatsTxExDeferPkts_Object=MibTableColumn
wwpLeosPortStatsTxExDeferPkts=_WwpLeosPortStatsTxExDeferPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,19),_WwpLeosPortStatsTxExDeferPkts_Type())
wwpLeosPortStatsTxExDeferPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTxExDeferPkts.setStatus(_A)
_WwpLeosPortStatsTxGiantPkts_Type=Counter32
_WwpLeosPortStatsTxGiantPkts_Object=MibTableColumn
wwpLeosPortStatsTxGiantPkts=_WwpLeosPortStatsTxGiantPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,20),_WwpLeosPortStatsTxGiantPkts_Type())
wwpLeosPortStatsTxGiantPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTxGiantPkts.setStatus(_A)
_WwpLeosPortStatsTxUnderRunPkts_Type=Counter32
_WwpLeosPortStatsTxUnderRunPkts_Object=MibTableColumn
wwpLeosPortStatsTxUnderRunPkts=_WwpLeosPortStatsTxUnderRunPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,21),_WwpLeosPortStatsTxUnderRunPkts_Type())
wwpLeosPortStatsTxUnderRunPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTxUnderRunPkts.setStatus(_A)
_WwpLeosPortStatsTxCrcErrorPkts_Type=Counter32
_WwpLeosPortStatsTxCrcErrorPkts_Object=MibTableColumn
wwpLeosPortStatsTxCrcErrorPkts=_WwpLeosPortStatsTxCrcErrorPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,22),_WwpLeosPortStatsTxCrcErrorPkts_Type())
wwpLeosPortStatsTxCrcErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTxCrcErrorPkts.setStatus(_A)
_WwpLeosPortStatsTxLCheckErrorPkts_Type=Counter32
_WwpLeosPortStatsTxLCheckErrorPkts_Object=MibTableColumn
wwpLeosPortStatsTxLCheckErrorPkts=_WwpLeosPortStatsTxLCheckErrorPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,23),_WwpLeosPortStatsTxLCheckErrorPkts_Type())
wwpLeosPortStatsTxLCheckErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTxLCheckErrorPkts.setStatus(_A)
_WwpLeosPortStatsTxLOutRangePkts_Type=Counter32
_WwpLeosPortStatsTxLOutRangePkts_Object=MibTableColumn
wwpLeosPortStatsTxLOutRangePkts=_WwpLeosPortStatsTxLOutRangePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,24),_WwpLeosPortStatsTxLOutRangePkts_Type())
wwpLeosPortStatsTxLOutRangePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTxLOutRangePkts.setStatus(_A)
_WwpLeosPortStatsTxLateCollPkts_Type=Counter32
_WwpLeosPortStatsTxLateCollPkts_Object=MibTableColumn
wwpLeosPortStatsTxLateCollPkts=_WwpLeosPortStatsTxLateCollPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,25),_WwpLeosPortStatsTxLateCollPkts_Type())
wwpLeosPortStatsTxLateCollPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTxLateCollPkts.setStatus(_A)
_WwpLeosPortStatsTxExCollPkts_Type=Counter32
_WwpLeosPortStatsTxExCollPkts_Object=MibTableColumn
wwpLeosPortStatsTxExCollPkts=_WwpLeosPortStatsTxExCollPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,26),_WwpLeosPortStatsTxExCollPkts_Type())
wwpLeosPortStatsTxExCollPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTxExCollPkts.setStatus(_A)
_WwpLeosPortStatsTxSingleCollPkts_Type=Counter32
_WwpLeosPortStatsTxSingleCollPkts_Object=MibTableColumn
wwpLeosPortStatsTxSingleCollPkts=_WwpLeosPortStatsTxSingleCollPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,27),_WwpLeosPortStatsTxSingleCollPkts_Type())
wwpLeosPortStatsTxSingleCollPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTxSingleCollPkts.setStatus(_A)
_WwpLeosPortStatsTxCollPkts_Type=Counter32
_WwpLeosPortStatsTxCollPkts_Object=MibTableColumn
wwpLeosPortStatsTxCollPkts=_WwpLeosPortStatsTxCollPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,28),_WwpLeosPortStatsTxCollPkts_Type())
wwpLeosPortStatsTxCollPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTxCollPkts.setStatus(_A)
_WwpLeosPortStatsTxPausePkts_Type=Counter32
_WwpLeosPortStatsTxPausePkts_Object=MibTableColumn
wwpLeosPortStatsTxPausePkts=_WwpLeosPortStatsTxPausePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,29),_WwpLeosPortStatsTxPausePkts_Type())
wwpLeosPortStatsTxPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTxPausePkts.setStatus(_A)
_WwpLeosPortStatsTxMcastPkts_Type=Counter32
_WwpLeosPortStatsTxMcastPkts_Object=MibTableColumn
wwpLeosPortStatsTxMcastPkts=_WwpLeosPortStatsTxMcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,30),_WwpLeosPortStatsTxMcastPkts_Type())
wwpLeosPortStatsTxMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTxMcastPkts.setStatus(_A)
_WwpLeosPortStatsTxBcastPkts_Type=Counter32
_WwpLeosPortStatsTxBcastPkts_Object=MibTableColumn
wwpLeosPortStatsTxBcastPkts=_WwpLeosPortStatsTxBcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,31),_WwpLeosPortStatsTxBcastPkts_Type())
wwpLeosPortStatsTxBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTxBcastPkts.setStatus(_A)
class _WwpLeosPortStatsPortReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_WwpLeosPortStatsPortReset_Type.__name__=_C
_WwpLeosPortStatsPortReset_Object=MibTableColumn
wwpLeosPortStatsPortReset=_WwpLeosPortStatsPortReset_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,32),_WwpLeosPortStatsPortReset_Type())
wwpLeosPortStatsPortReset.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosPortStatsPortReset.setStatus(_A)
_WwpLeosPortStatsRxMcastPkts_Type=Counter32
_WwpLeosPortStatsRxMcastPkts_Object=MibTableColumn
wwpLeosPortStatsRxMcastPkts=_WwpLeosPortStatsRxMcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,33),_WwpLeosPortStatsRxMcastPkts_Type())
wwpLeosPortStatsRxMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsRxMcastPkts.setStatus(_A)
_WwpLeosPortStatsRxPausePkts_Type=Counter32
_WwpLeosPortStatsRxPausePkts_Object=MibTableColumn
wwpLeosPortStatsRxPausePkts=_WwpLeosPortStatsRxPausePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,34),_WwpLeosPortStatsRxPausePkts_Type())
wwpLeosPortStatsRxPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsRxPausePkts.setStatus(_A)
_WwpLeosPortStats1519To2047BytePkts_Type=Counter32
_WwpLeosPortStats1519To2047BytePkts_Object=MibTableColumn
wwpLeosPortStats1519To2047BytePkts=_WwpLeosPortStats1519To2047BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,35),_WwpLeosPortStats1519To2047BytePkts_Type())
wwpLeosPortStats1519To2047BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStats1519To2047BytePkts.setStatus(_A)
_WwpLeosPortStats2048To4095BytePkts_Type=Counter32
_WwpLeosPortStats2048To4095BytePkts_Object=MibTableColumn
wwpLeosPortStats2048To4095BytePkts=_WwpLeosPortStats2048To4095BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,36),_WwpLeosPortStats2048To4095BytePkts_Type())
wwpLeosPortStats2048To4095BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStats2048To4095BytePkts.setStatus(_A)
_WwpLeosPortStats4096To9216BytePkts_Type=Counter32
_WwpLeosPortStats4096To9216BytePkts_Object=MibTableColumn
wwpLeosPortStats4096To9216BytePkts=_WwpLeosPortStats4096To9216BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,37),_WwpLeosPortStats4096To9216BytePkts_Type())
wwpLeosPortStats4096To9216BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStats4096To9216BytePkts.setStatus(_A)
_WwpLeosPortStatsTxDeferPkts_Type=Counter32
_WwpLeosPortStatsTxDeferPkts_Object=MibTableColumn
wwpLeosPortStatsTxDeferPkts=_WwpLeosPortStatsTxDeferPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,38),_WwpLeosPortStatsTxDeferPkts_Type())
wwpLeosPortStatsTxDeferPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTxDeferPkts.setStatus(_A)
_WwpLeosPortStatsTx64BytePkts_Type=Counter32
_WwpLeosPortStatsTx64BytePkts_Object=MibTableColumn
wwpLeosPortStatsTx64BytePkts=_WwpLeosPortStatsTx64BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,39),_WwpLeosPortStatsTx64BytePkts_Type())
wwpLeosPortStatsTx64BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTx64BytePkts.setStatus(_A)
_WwpLeosPortStatsTx65To127BytePkts_Type=Counter32
_WwpLeosPortStatsTx65To127BytePkts_Object=MibTableColumn
wwpLeosPortStatsTx65To127BytePkts=_WwpLeosPortStatsTx65To127BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,40),_WwpLeosPortStatsTx65To127BytePkts_Type())
wwpLeosPortStatsTx65To127BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTx65To127BytePkts.setStatus(_A)
_WwpLeosPortStatsTx128To255BytePkts_Type=Counter32
_WwpLeosPortStatsTx128To255BytePkts_Object=MibTableColumn
wwpLeosPortStatsTx128To255BytePkts=_WwpLeosPortStatsTx128To255BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,41),_WwpLeosPortStatsTx128To255BytePkts_Type())
wwpLeosPortStatsTx128To255BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTx128To255BytePkts.setStatus(_A)
_WwpLeosPortStatsTx256To511BytePkts_Type=Counter32
_WwpLeosPortStatsTx256To511BytePkts_Object=MibTableColumn
wwpLeosPortStatsTx256To511BytePkts=_WwpLeosPortStatsTx256To511BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,42),_WwpLeosPortStatsTx256To511BytePkts_Type())
wwpLeosPortStatsTx256To511BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTx256To511BytePkts.setStatus(_A)
_WwpLeosPortStatsTx512To1023BytePkts_Type=Counter32
_WwpLeosPortStatsTx512To1023BytePkts_Object=MibTableColumn
wwpLeosPortStatsTx512To1023BytePkts=_WwpLeosPortStatsTx512To1023BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,43),_WwpLeosPortStatsTx512To1023BytePkts_Type())
wwpLeosPortStatsTx512To1023BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTx512To1023BytePkts.setStatus(_A)
_WwpLeosPortStatsTx1024To1518BytePkts_Type=Counter32
_WwpLeosPortStatsTx1024To1518BytePkts_Object=MibTableColumn
wwpLeosPortStatsTx1024To1518BytePkts=_WwpLeosPortStatsTx1024To1518BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,44),_WwpLeosPortStatsTx1024To1518BytePkts_Type())
wwpLeosPortStatsTx1024To1518BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTx1024To1518BytePkts.setStatus(_A)
_WwpLeosPortStatsTx1519To2047BytePkts_Type=Counter32
_WwpLeosPortStatsTx1519To2047BytePkts_Object=MibTableColumn
wwpLeosPortStatsTx1519To2047BytePkts=_WwpLeosPortStatsTx1519To2047BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,45),_WwpLeosPortStatsTx1519To2047BytePkts_Type())
wwpLeosPortStatsTx1519To2047BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTx1519To2047BytePkts.setStatus(_A)
_WwpLeosPortStatsTx2048To4095BytePkts_Type=Counter32
_WwpLeosPortStatsTx2048To4095BytePkts_Object=MibTableColumn
wwpLeosPortStatsTx2048To4095BytePkts=_WwpLeosPortStatsTx2048To4095BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,46),_WwpLeosPortStatsTx2048To4095BytePkts_Type())
wwpLeosPortStatsTx2048To4095BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTx2048To4095BytePkts.setStatus(_A)
_WwpLeosPortStatsTx4096To9216BytePkts_Type=Counter32
_WwpLeosPortStatsTx4096To9216BytePkts_Object=MibTableColumn
wwpLeosPortStatsTx4096To9216BytePkts=_WwpLeosPortStatsTx4096To9216BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,47),_WwpLeosPortStatsTx4096To9216BytePkts_Type())
wwpLeosPortStatsTx4096To9216BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTx4096To9216BytePkts.setStatus(_A)
_WwpLeosPortStatsRxFpgaDropPkts_Type=Counter32
_WwpLeosPortStatsRxFpgaDropPkts_Object=MibTableColumn
wwpLeosPortStatsRxFpgaDropPkts=_WwpLeosPortStatsRxFpgaDropPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,48),_WwpLeosPortStatsRxFpgaDropPkts_Type())
wwpLeosPortStatsRxFpgaDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsRxFpgaDropPkts.setStatus(_A)
_WwpLeosPortStatsPortLinkUp_Type=Counter32
_WwpLeosPortStatsPortLinkUp_Object=MibTableColumn
wwpLeosPortStatsPortLinkUp=_WwpLeosPortStatsPortLinkUp_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,49),_WwpLeosPortStatsPortLinkUp_Type())
wwpLeosPortStatsPortLinkUp.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsPortLinkUp.setStatus(_A)
_WwpLeosPortStatsPortLinkDown_Type=Counter32
_WwpLeosPortStatsPortLinkDown_Object=MibTableColumn
wwpLeosPortStatsPortLinkDown=_WwpLeosPortStatsPortLinkDown_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,50),_WwpLeosPortStatsPortLinkDown_Type())
wwpLeosPortStatsPortLinkDown.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsPortLinkDown.setStatus(_A)
_WwpLeosPortStatsPortLinkFlap_Type=Counter32
_WwpLeosPortStatsPortLinkFlap_Object=MibTableColumn
wwpLeosPortStatsPortLinkFlap=_WwpLeosPortStatsPortLinkFlap_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,51),_WwpLeosPortStatsPortLinkFlap_Type())
wwpLeosPortStatsPortLinkFlap.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsPortLinkFlap.setStatus(_A)
_WwpLeosPortStatsRxUcastPkts_Type=Counter32
_WwpLeosPortStatsRxUcastPkts_Object=MibTableColumn
wwpLeosPortStatsRxUcastPkts=_WwpLeosPortStatsRxUcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,52),_WwpLeosPortStatsRxUcastPkts_Type())
wwpLeosPortStatsRxUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsRxUcastPkts.setStatus(_A)
_WwpLeosPortStatsTxUcastPkts_Type=Counter32
_WwpLeosPortStatsTxUcastPkts_Object=MibTableColumn
wwpLeosPortStatsTxUcastPkts=_WwpLeosPortStatsTxUcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,53),_WwpLeosPortStatsTxUcastPkts_Type())
wwpLeosPortStatsTxUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTxUcastPkts.setStatus(_A)
_WwpLeosPortStatsRxDropPkts_Type=Counter32
_WwpLeosPortStatsRxDropPkts_Object=MibTableColumn
wwpLeosPortStatsRxDropPkts=_WwpLeosPortStatsRxDropPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,54),_WwpLeosPortStatsRxDropPkts_Type())
wwpLeosPortStatsRxDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsRxDropPkts.setStatus(_A)
_WwpLeosPortStatsRxDiscardPkts_Type=Counter32
_WwpLeosPortStatsRxDiscardPkts_Object=MibTableColumn
wwpLeosPortStatsRxDiscardPkts=_WwpLeosPortStatsRxDiscardPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,55),_WwpLeosPortStatsRxDiscardPkts_Type())
wwpLeosPortStatsRxDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsRxDiscardPkts.setStatus(_A)
_WwpLeosPortStatsRxLOutRangePkts_Type=Counter32
_WwpLeosPortStatsRxLOutRangePkts_Object=MibTableColumn
wwpLeosPortStatsRxLOutRangePkts=_WwpLeosPortStatsRxLOutRangePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,56),_WwpLeosPortStatsRxLOutRangePkts_Type())
wwpLeosPortStatsRxLOutRangePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsRxLOutRangePkts.setStatus(_A)
_WwpLeosPortStatsRxFpgaBufferDropPkts_Type=Counter32
_WwpLeosPortStatsRxFpgaBufferDropPkts_Object=MibTableColumn
wwpLeosPortStatsRxFpgaBufferDropPkts=_WwpLeosPortStatsRxFpgaBufferDropPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,57),_WwpLeosPortStatsRxFpgaBufferDropPkts_Type())
wwpLeosPortStatsRxFpgaBufferDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsRxFpgaBufferDropPkts.setStatus(_A)
_WwpLeosPortStatsTxFpgaBufferDropPkts_Type=Counter32
_WwpLeosPortStatsTxFpgaBufferDropPkts_Object=MibTableColumn
wwpLeosPortStatsTxFpgaBufferDropPkts=_WwpLeosPortStatsTxFpgaBufferDropPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,58),_WwpLeosPortStatsTxFpgaBufferDropPkts_Type())
wwpLeosPortStatsTxFpgaBufferDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsTxFpgaBufferDropPkts.setStatus(_A)
_WwpLeosPortStatsFpgaVlanPriFilterDropPkts_Type=Counter32
_WwpLeosPortStatsFpgaVlanPriFilterDropPkts_Object=MibTableColumn
wwpLeosPortStatsFpgaVlanPriFilterDropPkts=_WwpLeosPortStatsFpgaVlanPriFilterDropPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,59),_WwpLeosPortStatsFpgaVlanPriFilterDropPkts_Type())
wwpLeosPortStatsFpgaVlanPriFilterDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsFpgaVlanPriFilterDropPkts.setStatus(_A)
_WwpLeosPortStatsFpgaRxErrorPkts_Type=Counter32
_WwpLeosPortStatsFpgaRxErrorPkts_Object=MibTableColumn
wwpLeosPortStatsFpgaRxErrorPkts=_WwpLeosPortStatsFpgaRxErrorPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,60),_WwpLeosPortStatsFpgaRxErrorPkts_Type())
wwpLeosPortStatsFpgaRxErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsFpgaRxErrorPkts.setStatus(_A)
_WwpLeosPortStatsFpgaRxCrcErrorPkts_Type=Counter32
_WwpLeosPortStatsFpgaRxCrcErrorPkts_Object=MibTableColumn
wwpLeosPortStatsFpgaRxCrcErrorPkts=_WwpLeosPortStatsFpgaRxCrcErrorPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,61),_WwpLeosPortStatsFpgaRxCrcErrorPkts_Type())
wwpLeosPortStatsFpgaRxCrcErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsFpgaRxCrcErrorPkts.setStatus(_A)
_WwpLeosPortStatsFpgaRxIpCrcErrorPkts_Type=Counter32
_WwpLeosPortStatsFpgaRxIpCrcErrorPkts_Object=MibTableColumn
wwpLeosPortStatsFpgaRxIpCrcErrorPkts=_WwpLeosPortStatsFpgaRxIpCrcErrorPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,62),_WwpLeosPortStatsFpgaRxIpCrcErrorPkts_Type())
wwpLeosPortStatsFpgaRxIpCrcErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsFpgaRxIpCrcErrorPkts.setStatus(_A)
_WwpLeosPortStatsRxInErrorPkts_Type=Counter32
_WwpLeosPortStatsRxInErrorPkts_Object=MibTableColumn
wwpLeosPortStatsRxInErrorPkts=_WwpLeosPortStatsRxInErrorPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,2,1,63),_WwpLeosPortStatsRxInErrorPkts_Type())
wwpLeosPortStatsRxInErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortStatsRxInErrorPkts.setStatus(_A)
_WwpLeosPortTotalStatsTable_Object=MibTable
wwpLeosPortTotalStatsTable=_WwpLeosPortTotalStatsTable_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3))
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTable.setStatus(_A)
_WwpLeosPortTotalStatsEntry_Object=MibTableRow
wwpLeosPortTotalStatsEntry=_WwpLeosPortTotalStatsEntry_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1))
wwpLeosPortTotalStatsEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:wwpLeosPortTotalStatsEntry.setStatus(_A)
class _WwpLeosPortTotalStatsPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortTotalStatsPortId_Type.__name__=_C
_WwpLeosPortTotalStatsPortId_Object=MibTableColumn
wwpLeosPortTotalStatsPortId=_WwpLeosPortTotalStatsPortId_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,1),_WwpLeosPortTotalStatsPortId_Type())
wwpLeosPortTotalStatsPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsPortId.setStatus(_A)
_WwpLeosPortTotalStatsRxBytes_Type=Counter32
_WwpLeosPortTotalStatsRxBytes_Object=MibTableColumn
wwpLeosPortTotalStatsRxBytes=_WwpLeosPortTotalStatsRxBytes_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,2),_WwpLeosPortTotalStatsRxBytes_Type())
wwpLeosPortTotalStatsRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsRxBytes.setStatus(_A)
_WwpLeosPortTotalStatsRxPkts_Type=Counter32
_WwpLeosPortTotalStatsRxPkts_Object=MibTableColumn
wwpLeosPortTotalStatsRxPkts=_WwpLeosPortTotalStatsRxPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,3),_WwpLeosPortTotalStatsRxPkts_Type())
wwpLeosPortTotalStatsRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsRxPkts.setStatus(_A)
_WwpLeosPortTotalStatsRxCrcErrorPkts_Type=Counter32
_WwpLeosPortTotalStatsRxCrcErrorPkts_Object=MibTableColumn
wwpLeosPortTotalStatsRxCrcErrorPkts=_WwpLeosPortTotalStatsRxCrcErrorPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,4),_WwpLeosPortTotalStatsRxCrcErrorPkts_Type())
wwpLeosPortTotalStatsRxCrcErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsRxCrcErrorPkts.setStatus(_A)
_WwpLeosPortTotalStatsRxBcastPkts_Type=Counter32
_WwpLeosPortTotalStatsRxBcastPkts_Object=MibTableColumn
wwpLeosPortTotalStatsRxBcastPkts=_WwpLeosPortTotalStatsRxBcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,5),_WwpLeosPortTotalStatsRxBcastPkts_Type())
wwpLeosPortTotalStatsRxBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsRxBcastPkts.setStatus(_A)
_WwpLeosPortTotalStatsUndersizePkts_Type=Counter32
_WwpLeosPortTotalStatsUndersizePkts_Object=MibTableColumn
wwpLeosPortTotalStatsUndersizePkts=_WwpLeosPortTotalStatsUndersizePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,6),_WwpLeosPortTotalStatsUndersizePkts_Type())
wwpLeosPortTotalStatsUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsUndersizePkts.setStatus(_A)
_WwpLeosPortTotalStatsOversizePkts_Type=Counter32
_WwpLeosPortTotalStatsOversizePkts_Object=MibTableColumn
wwpLeosPortTotalStatsOversizePkts=_WwpLeosPortTotalStatsOversizePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,7),_WwpLeosPortTotalStatsOversizePkts_Type())
wwpLeosPortTotalStatsOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsOversizePkts.setStatus(_A)
_WwpLeosPortTotalStatsFragmentPkts_Type=Counter32
_WwpLeosPortTotalStatsFragmentPkts_Object=MibTableColumn
wwpLeosPortTotalStatsFragmentPkts=_WwpLeosPortTotalStatsFragmentPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,8),_WwpLeosPortTotalStatsFragmentPkts_Type())
wwpLeosPortTotalStatsFragmentPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsFragmentPkts.setStatus(_A)
_WwpLeosPortTotalStatsJabberPkts_Type=Counter32
_WwpLeosPortTotalStatsJabberPkts_Object=MibTableColumn
wwpLeosPortTotalStatsJabberPkts=_WwpLeosPortTotalStatsJabberPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,9),_WwpLeosPortTotalStatsJabberPkts_Type())
wwpLeosPortTotalStatsJabberPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsJabberPkts.setStatus(_A)
_WwpLeosPortTotalStats64BytePkts_Type=Counter32
_WwpLeosPortTotalStats64BytePkts_Object=MibTableColumn
wwpLeosPortTotalStats64BytePkts=_WwpLeosPortTotalStats64BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,10),_WwpLeosPortTotalStats64BytePkts_Type())
wwpLeosPortTotalStats64BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStats64BytePkts.setStatus(_A)
_WwpLeosPortTotalStats65To127BytePkts_Type=Counter32
_WwpLeosPortTotalStats65To127BytePkts_Object=MibTableColumn
wwpLeosPortTotalStats65To127BytePkts=_WwpLeosPortTotalStats65To127BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,11),_WwpLeosPortTotalStats65To127BytePkts_Type())
wwpLeosPortTotalStats65To127BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStats65To127BytePkts.setStatus(_A)
_WwpLeosPortTotalStats128To255BytePkts_Type=Counter32
_WwpLeosPortTotalStats128To255BytePkts_Object=MibTableColumn
wwpLeosPortTotalStats128To255BytePkts=_WwpLeosPortTotalStats128To255BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,12),_WwpLeosPortTotalStats128To255BytePkts_Type())
wwpLeosPortTotalStats128To255BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStats128To255BytePkts.setStatus(_A)
_WwpLeosPortTotalStats256To511BytePkts_Type=Counter32
_WwpLeosPortTotalStats256To511BytePkts_Object=MibTableColumn
wwpLeosPortTotalStats256To511BytePkts=_WwpLeosPortTotalStats256To511BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,13),_WwpLeosPortTotalStats256To511BytePkts_Type())
wwpLeosPortTotalStats256To511BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStats256To511BytePkts.setStatus(_A)
_WwpLeosPortTotalStats512To1023BytePkts_Type=Counter32
_WwpLeosPortTotalStats512To1023BytePkts_Object=MibTableColumn
wwpLeosPortTotalStats512To1023BytePkts=_WwpLeosPortTotalStats512To1023BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,14),_WwpLeosPortTotalStats512To1023BytePkts_Type())
wwpLeosPortTotalStats512To1023BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStats512To1023BytePkts.setStatus(_A)
_WwpLeosPortTotalStats1024To1518BytePkts_Type=Counter32
_WwpLeosPortTotalStats1024To1518BytePkts_Object=MibTableColumn
wwpLeosPortTotalStats1024To1518BytePkts=_WwpLeosPortTotalStats1024To1518BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,15),_WwpLeosPortTotalStats1024To1518BytePkts_Type())
wwpLeosPortTotalStats1024To1518BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStats1024To1518BytePkts.setStatus(_A)
_WwpLeosPortTotalStatsTxBytes_Type=Counter32
_WwpLeosPortTotalStatsTxBytes_Object=MibTableColumn
wwpLeosPortTotalStatsTxBytes=_WwpLeosPortTotalStatsTxBytes_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,16),_WwpLeosPortTotalStatsTxBytes_Type())
wwpLeosPortTotalStatsTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTxBytes.setStatus(_A)
_WwpLeosPortTotalStatsTxTBytes_Type=Counter32
_WwpLeosPortTotalStatsTxTBytes_Object=MibTableColumn
wwpLeosPortTotalStatsTxTBytes=_WwpLeosPortTotalStatsTxTBytes_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,17),_WwpLeosPortTotalStatsTxTBytes_Type())
wwpLeosPortTotalStatsTxTBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTxTBytes.setStatus(_H)
_WwpLeosPortTotalStatsTxPkts_Type=Counter32
_WwpLeosPortTotalStatsTxPkts_Object=MibTableColumn
wwpLeosPortTotalStatsTxPkts=_WwpLeosPortTotalStatsTxPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,18),_WwpLeosPortTotalStatsTxPkts_Type())
wwpLeosPortTotalStatsTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTxPkts.setStatus(_A)
_WwpLeosPortTotalStatsTxExDeferPkts_Type=Counter32
_WwpLeosPortTotalStatsTxExDeferPkts_Object=MibTableColumn
wwpLeosPortTotalStatsTxExDeferPkts=_WwpLeosPortTotalStatsTxExDeferPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,19),_WwpLeosPortTotalStatsTxExDeferPkts_Type())
wwpLeosPortTotalStatsTxExDeferPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTxExDeferPkts.setStatus(_A)
_WwpLeosPortTotalStatsTxGiantPkts_Type=Counter32
_WwpLeosPortTotalStatsTxGiantPkts_Object=MibTableColumn
wwpLeosPortTotalStatsTxGiantPkts=_WwpLeosPortTotalStatsTxGiantPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,20),_WwpLeosPortTotalStatsTxGiantPkts_Type())
wwpLeosPortTotalStatsTxGiantPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTxGiantPkts.setStatus(_A)
_WwpLeosPortTotalStatsTxUnderRunPkts_Type=Counter32
_WwpLeosPortTotalStatsTxUnderRunPkts_Object=MibTableColumn
wwpLeosPortTotalStatsTxUnderRunPkts=_WwpLeosPortTotalStatsTxUnderRunPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,21),_WwpLeosPortTotalStatsTxUnderRunPkts_Type())
wwpLeosPortTotalStatsTxUnderRunPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTxUnderRunPkts.setStatus(_A)
_WwpLeosPortTotalStatsTxCrcErrorPkts_Type=Counter32
_WwpLeosPortTotalStatsTxCrcErrorPkts_Object=MibTableColumn
wwpLeosPortTotalStatsTxCrcErrorPkts=_WwpLeosPortTotalStatsTxCrcErrorPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,22),_WwpLeosPortTotalStatsTxCrcErrorPkts_Type())
wwpLeosPortTotalStatsTxCrcErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTxCrcErrorPkts.setStatus(_A)
_WwpLeosPortTotalStatsTxLCheckErrorPkts_Type=Counter32
_WwpLeosPortTotalStatsTxLCheckErrorPkts_Object=MibTableColumn
wwpLeosPortTotalStatsTxLCheckErrorPkts=_WwpLeosPortTotalStatsTxLCheckErrorPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,23),_WwpLeosPortTotalStatsTxLCheckErrorPkts_Type())
wwpLeosPortTotalStatsTxLCheckErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTxLCheckErrorPkts.setStatus(_A)
_WwpLeosPortTotalStatsTxLOutRangePkts_Type=Counter32
_WwpLeosPortTotalStatsTxLOutRangePkts_Object=MibTableColumn
wwpLeosPortTotalStatsTxLOutRangePkts=_WwpLeosPortTotalStatsTxLOutRangePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,24),_WwpLeosPortTotalStatsTxLOutRangePkts_Type())
wwpLeosPortTotalStatsTxLOutRangePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTxLOutRangePkts.setStatus(_A)
_WwpLeosPortTotalStatsTxLateCollPkts_Type=Counter32
_WwpLeosPortTotalStatsTxLateCollPkts_Object=MibTableColumn
wwpLeosPortTotalStatsTxLateCollPkts=_WwpLeosPortTotalStatsTxLateCollPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,25),_WwpLeosPortTotalStatsTxLateCollPkts_Type())
wwpLeosPortTotalStatsTxLateCollPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTxLateCollPkts.setStatus(_A)
_WwpLeosPortTotalStatsTxExCollPkts_Type=Counter32
_WwpLeosPortTotalStatsTxExCollPkts_Object=MibTableColumn
wwpLeosPortTotalStatsTxExCollPkts=_WwpLeosPortTotalStatsTxExCollPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,26),_WwpLeosPortTotalStatsTxExCollPkts_Type())
wwpLeosPortTotalStatsTxExCollPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTxExCollPkts.setStatus(_A)
_WwpLeosPortTotalStatsTxSingleCollPkts_Type=Counter32
_WwpLeosPortTotalStatsTxSingleCollPkts_Object=MibTableColumn
wwpLeosPortTotalStatsTxSingleCollPkts=_WwpLeosPortTotalStatsTxSingleCollPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,27),_WwpLeosPortTotalStatsTxSingleCollPkts_Type())
wwpLeosPortTotalStatsTxSingleCollPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTxSingleCollPkts.setStatus(_A)
_WwpLeosPortTotalStatsTxCollPkts_Type=Counter32
_WwpLeosPortTotalStatsTxCollPkts_Object=MibTableColumn
wwpLeosPortTotalStatsTxCollPkts=_WwpLeosPortTotalStatsTxCollPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,28),_WwpLeosPortTotalStatsTxCollPkts_Type())
wwpLeosPortTotalStatsTxCollPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTxCollPkts.setStatus(_A)
_WwpLeosPortTotalStatsTxPausePkts_Type=Counter32
_WwpLeosPortTotalStatsTxPausePkts_Object=MibTableColumn
wwpLeosPortTotalStatsTxPausePkts=_WwpLeosPortTotalStatsTxPausePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,29),_WwpLeosPortTotalStatsTxPausePkts_Type())
wwpLeosPortTotalStatsTxPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTxPausePkts.setStatus(_A)
_WwpLeosPortTotalStatsTxMcastPkts_Type=Counter32
_WwpLeosPortTotalStatsTxMcastPkts_Object=MibTableColumn
wwpLeosPortTotalStatsTxMcastPkts=_WwpLeosPortTotalStatsTxMcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,30),_WwpLeosPortTotalStatsTxMcastPkts_Type())
wwpLeosPortTotalStatsTxMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTxMcastPkts.setStatus(_A)
_WwpLeosPortTotalStatsTxBcastPkts_Type=Counter32
_WwpLeosPortTotalStatsTxBcastPkts_Object=MibTableColumn
wwpLeosPortTotalStatsTxBcastPkts=_WwpLeosPortTotalStatsTxBcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,31),_WwpLeosPortTotalStatsTxBcastPkts_Type())
wwpLeosPortTotalStatsTxBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTxBcastPkts.setStatus(_A)
class _WwpLeosPortTotalStatsPortReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_WwpLeosPortTotalStatsPortReset_Type.__name__=_C
_WwpLeosPortTotalStatsPortReset_Object=MibTableColumn
wwpLeosPortTotalStatsPortReset=_WwpLeosPortTotalStatsPortReset_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,32),_WwpLeosPortTotalStatsPortReset_Type())
wwpLeosPortTotalStatsPortReset.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsPortReset.setStatus(_A)
_WwpLeosPortTotalStatsRxMcastPkts_Type=Counter32
_WwpLeosPortTotalStatsRxMcastPkts_Object=MibTableColumn
wwpLeosPortTotalStatsRxMcastPkts=_WwpLeosPortTotalStatsRxMcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,33),_WwpLeosPortTotalStatsRxMcastPkts_Type())
wwpLeosPortTotalStatsRxMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsRxMcastPkts.setStatus(_A)
_WwpLeosPortTotalStatsRxPausePkts_Type=Counter32
_WwpLeosPortTotalStatsRxPausePkts_Object=MibTableColumn
wwpLeosPortTotalStatsRxPausePkts=_WwpLeosPortTotalStatsRxPausePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,34),_WwpLeosPortTotalStatsRxPausePkts_Type())
wwpLeosPortTotalStatsRxPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsRxPausePkts.setStatus(_A)
_WwpLeosPortTotalStats1519To2047BytePkts_Type=Counter32
_WwpLeosPortTotalStats1519To2047BytePkts_Object=MibTableColumn
wwpLeosPortTotalStats1519To2047BytePkts=_WwpLeosPortTotalStats1519To2047BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,35),_WwpLeosPortTotalStats1519To2047BytePkts_Type())
wwpLeosPortTotalStats1519To2047BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStats1519To2047BytePkts.setStatus(_A)
_WwpLeosPortTotalStats2048To4095BytePkts_Type=Counter32
_WwpLeosPortTotalStats2048To4095BytePkts_Object=MibTableColumn
wwpLeosPortTotalStats2048To4095BytePkts=_WwpLeosPortTotalStats2048To4095BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,36),_WwpLeosPortTotalStats2048To4095BytePkts_Type())
wwpLeosPortTotalStats2048To4095BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStats2048To4095BytePkts.setStatus(_A)
_WwpLeosPortTotalStats4096To9216BytePkts_Type=Counter32
_WwpLeosPortTotalStats4096To9216BytePkts_Object=MibTableColumn
wwpLeosPortTotalStats4096To9216BytePkts=_WwpLeosPortTotalStats4096To9216BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,37),_WwpLeosPortTotalStats4096To9216BytePkts_Type())
wwpLeosPortTotalStats4096To9216BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStats4096To9216BytePkts.setStatus(_A)
_WwpLeosPortTotalStatsTxDeferPkts_Type=Counter32
_WwpLeosPortTotalStatsTxDeferPkts_Object=MibTableColumn
wwpLeosPortTotalStatsTxDeferPkts=_WwpLeosPortTotalStatsTxDeferPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,38),_WwpLeosPortTotalStatsTxDeferPkts_Type())
wwpLeosPortTotalStatsTxDeferPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTxDeferPkts.setStatus(_A)
_WwpLeosPortTotalStatsTx64BytePkts_Type=Counter32
_WwpLeosPortTotalStatsTx64BytePkts_Object=MibTableColumn
wwpLeosPortTotalStatsTx64BytePkts=_WwpLeosPortTotalStatsTx64BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,39),_WwpLeosPortTotalStatsTx64BytePkts_Type())
wwpLeosPortTotalStatsTx64BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTx64BytePkts.setStatus(_A)
_WwpLeosPortTotalStatsTx65To127BytePkts_Type=Counter32
_WwpLeosPortTotalStatsTx65To127BytePkts_Object=MibTableColumn
wwpLeosPortTotalStatsTx65To127BytePkts=_WwpLeosPortTotalStatsTx65To127BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,40),_WwpLeosPortTotalStatsTx65To127BytePkts_Type())
wwpLeosPortTotalStatsTx65To127BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTx65To127BytePkts.setStatus(_A)
_WwpLeosPortTotalStatsTx128To255BytePkts_Type=Counter32
_WwpLeosPortTotalStatsTx128To255BytePkts_Object=MibTableColumn
wwpLeosPortTotalStatsTx128To255BytePkts=_WwpLeosPortTotalStatsTx128To255BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,41),_WwpLeosPortTotalStatsTx128To255BytePkts_Type())
wwpLeosPortTotalStatsTx128To255BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTx128To255BytePkts.setStatus(_A)
_WwpLeosPortTotalStatsTx256To511BytePkts_Type=Counter32
_WwpLeosPortTotalStatsTx256To511BytePkts_Object=MibTableColumn
wwpLeosPortTotalStatsTx256To511BytePkts=_WwpLeosPortTotalStatsTx256To511BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,42),_WwpLeosPortTotalStatsTx256To511BytePkts_Type())
wwpLeosPortTotalStatsTx256To511BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTx256To511BytePkts.setStatus(_A)
_WwpLeosPortTotalStatsTx512To1023BytePkts_Type=Counter32
_WwpLeosPortTotalStatsTx512To1023BytePkts_Object=MibTableColumn
wwpLeosPortTotalStatsTx512To1023BytePkts=_WwpLeosPortTotalStatsTx512To1023BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,43),_WwpLeosPortTotalStatsTx512To1023BytePkts_Type())
wwpLeosPortTotalStatsTx512To1023BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTx512To1023BytePkts.setStatus(_A)
_WwpLeosPortTotalStatsTx1024To1518BytePkts_Type=Counter32
_WwpLeosPortTotalStatsTx1024To1518BytePkts_Object=MibTableColumn
wwpLeosPortTotalStatsTx1024To1518BytePkts=_WwpLeosPortTotalStatsTx1024To1518BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,44),_WwpLeosPortTotalStatsTx1024To1518BytePkts_Type())
wwpLeosPortTotalStatsTx1024To1518BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTx1024To1518BytePkts.setStatus(_A)
_WwpLeosPortTotalStatsTx1519To2047BytePkts_Type=Counter32
_WwpLeosPortTotalStatsTx1519To2047BytePkts_Object=MibTableColumn
wwpLeosPortTotalStatsTx1519To2047BytePkts=_WwpLeosPortTotalStatsTx1519To2047BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,45),_WwpLeosPortTotalStatsTx1519To2047BytePkts_Type())
wwpLeosPortTotalStatsTx1519To2047BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTx1519To2047BytePkts.setStatus(_A)
_WwpLeosPortTotalStatsTx2048To4095BytePkts_Type=Counter32
_WwpLeosPortTotalStatsTx2048To4095BytePkts_Object=MibTableColumn
wwpLeosPortTotalStatsTx2048To4095BytePkts=_WwpLeosPortTotalStatsTx2048To4095BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,46),_WwpLeosPortTotalStatsTx2048To4095BytePkts_Type())
wwpLeosPortTotalStatsTx2048To4095BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTx2048To4095BytePkts.setStatus(_A)
_WwpLeosPortTotalStatsTx4096To9216BytePkts_Type=Counter32
_WwpLeosPortTotalStatsTx4096To9216BytePkts_Object=MibTableColumn
wwpLeosPortTotalStatsTx4096To9216BytePkts=_WwpLeosPortTotalStatsTx4096To9216BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,47),_WwpLeosPortTotalStatsTx4096To9216BytePkts_Type())
wwpLeosPortTotalStatsTx4096To9216BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTx4096To9216BytePkts.setStatus(_A)
_WwpLeosPortTotalStatsRxFpgaDropPkts_Type=Counter32
_WwpLeosPortTotalStatsRxFpgaDropPkts_Object=MibTableColumn
wwpLeosPortTotalStatsRxFpgaDropPkts=_WwpLeosPortTotalStatsRxFpgaDropPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,48),_WwpLeosPortTotalStatsRxFpgaDropPkts_Type())
wwpLeosPortTotalStatsRxFpgaDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsRxFpgaDropPkts.setStatus(_A)
_WwpLeosPortTotalStatsPortLinkUp_Type=Counter32
_WwpLeosPortTotalStatsPortLinkUp_Object=MibTableColumn
wwpLeosPortTotalStatsPortLinkUp=_WwpLeosPortTotalStatsPortLinkUp_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,49),_WwpLeosPortTotalStatsPortLinkUp_Type())
wwpLeosPortTotalStatsPortLinkUp.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsPortLinkUp.setStatus(_A)
_WwpLeosPortTotalStatsPortLinkDown_Type=Counter32
_WwpLeosPortTotalStatsPortLinkDown_Object=MibTableColumn
wwpLeosPortTotalStatsPortLinkDown=_WwpLeosPortTotalStatsPortLinkDown_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,50),_WwpLeosPortTotalStatsPortLinkDown_Type())
wwpLeosPortTotalStatsPortLinkDown.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsPortLinkDown.setStatus(_A)
_WwpLeosPortTotalStatsPortLinkFlap_Type=Counter32
_WwpLeosPortTotalStatsPortLinkFlap_Object=MibTableColumn
wwpLeosPortTotalStatsPortLinkFlap=_WwpLeosPortTotalStatsPortLinkFlap_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,51),_WwpLeosPortTotalStatsPortLinkFlap_Type())
wwpLeosPortTotalStatsPortLinkFlap.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsPortLinkFlap.setStatus(_A)
_WwpLeosPortTotalStatsRxUcastPkts_Type=Counter32
_WwpLeosPortTotalStatsRxUcastPkts_Object=MibTableColumn
wwpLeosPortTotalStatsRxUcastPkts=_WwpLeosPortTotalStatsRxUcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,52),_WwpLeosPortTotalStatsRxUcastPkts_Type())
wwpLeosPortTotalStatsRxUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsRxUcastPkts.setStatus(_A)
_WwpLeosPortTotalStatsTxUcastPkts_Type=Counter32
_WwpLeosPortTotalStatsTxUcastPkts_Object=MibTableColumn
wwpLeosPortTotalStatsTxUcastPkts=_WwpLeosPortTotalStatsTxUcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,53),_WwpLeosPortTotalStatsTxUcastPkts_Type())
wwpLeosPortTotalStatsTxUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTxUcastPkts.setStatus(_A)
_WwpLeosPortTotalStatsRxDropPkts_Type=Counter32
_WwpLeosPortTotalStatsRxDropPkts_Object=MibTableColumn
wwpLeosPortTotalStatsRxDropPkts=_WwpLeosPortTotalStatsRxDropPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,54),_WwpLeosPortTotalStatsRxDropPkts_Type())
wwpLeosPortTotalStatsRxDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsRxDropPkts.setStatus(_A)
_WwpLeosPortTotalStatsRxDiscardPkts_Type=Counter32
_WwpLeosPortTotalStatsRxDiscardPkts_Object=MibTableColumn
wwpLeosPortTotalStatsRxDiscardPkts=_WwpLeosPortTotalStatsRxDiscardPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,55),_WwpLeosPortTotalStatsRxDiscardPkts_Type())
wwpLeosPortTotalStatsRxDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsRxDiscardPkts.setStatus(_A)
_WwpLeosPortTotalStatsRxLOutRangePkts_Type=Counter32
_WwpLeosPortTotalStatsRxLOutRangePkts_Object=MibTableColumn
wwpLeosPortTotalStatsRxLOutRangePkts=_WwpLeosPortTotalStatsRxLOutRangePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,56),_WwpLeosPortTotalStatsRxLOutRangePkts_Type())
wwpLeosPortTotalStatsRxLOutRangePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsRxLOutRangePkts.setStatus(_A)
_WwpLeosPortTotalStatsRxFpgaBufferDropPkts_Type=Counter32
_WwpLeosPortTotalStatsRxFpgaBufferDropPkts_Object=MibTableColumn
wwpLeosPortTotalStatsRxFpgaBufferDropPkts=_WwpLeosPortTotalStatsRxFpgaBufferDropPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,57),_WwpLeosPortTotalStatsRxFpgaBufferDropPkts_Type())
wwpLeosPortTotalStatsRxFpgaBufferDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsRxFpgaBufferDropPkts.setStatus(_A)
_WwpLeosPortTotalStatsTxFpgaBufferDropPkts_Type=Counter32
_WwpLeosPortTotalStatsTxFpgaBufferDropPkts_Object=MibTableColumn
wwpLeosPortTotalStatsTxFpgaBufferDropPkts=_WwpLeosPortTotalStatsTxFpgaBufferDropPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,58),_WwpLeosPortTotalStatsTxFpgaBufferDropPkts_Type())
wwpLeosPortTotalStatsTxFpgaBufferDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsTxFpgaBufferDropPkts.setStatus(_A)
_WwpLeosPortTotalStatsFpgaVlanPriFilterDropPkts_Type=Counter32
_WwpLeosPortTotalStatsFpgaVlanPriFilterDropPkts_Object=MibTableColumn
wwpLeosPortTotalStatsFpgaVlanPriFilterDropPkts=_WwpLeosPortTotalStatsFpgaVlanPriFilterDropPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,59),_WwpLeosPortTotalStatsFpgaVlanPriFilterDropPkts_Type())
wwpLeosPortTotalStatsFpgaVlanPriFilterDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsFpgaVlanPriFilterDropPkts.setStatus(_A)
_WwpLeosPortTotalStatsFpgaRxErrorPkts_Type=Counter32
_WwpLeosPortTotalStatsFpgaRxErrorPkts_Object=MibTableColumn
wwpLeosPortTotalStatsFpgaRxErrorPkts=_WwpLeosPortTotalStatsFpgaRxErrorPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,60),_WwpLeosPortTotalStatsFpgaRxErrorPkts_Type())
wwpLeosPortTotalStatsFpgaRxErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsFpgaRxErrorPkts.setStatus(_A)
_WwpLeosPortTotalStatsFpgaRxCrcErrorPkts_Type=Counter32
_WwpLeosPortTotalStatsFpgaRxCrcErrorPkts_Object=MibTableColumn
wwpLeosPortTotalStatsFpgaRxCrcErrorPkts=_WwpLeosPortTotalStatsFpgaRxCrcErrorPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,61),_WwpLeosPortTotalStatsFpgaRxCrcErrorPkts_Type())
wwpLeosPortTotalStatsFpgaRxCrcErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsFpgaRxCrcErrorPkts.setStatus(_A)
_WwpLeosPortTotalStatsFpgaRxIpCrcErrorPkts_Type=Counter32
_WwpLeosPortTotalStatsFpgaRxIpCrcErrorPkts_Object=MibTableColumn
wwpLeosPortTotalStatsFpgaRxIpCrcErrorPkts=_WwpLeosPortTotalStatsFpgaRxIpCrcErrorPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,62),_WwpLeosPortTotalStatsFpgaRxIpCrcErrorPkts_Type())
wwpLeosPortTotalStatsFpgaRxIpCrcErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsFpgaRxIpCrcErrorPkts.setStatus(_A)
_WwpLeosPortTotalStatsRxInErrorPkts_Type=Counter32
_WwpLeosPortTotalStatsRxInErrorPkts_Object=MibTableColumn
wwpLeosPortTotalStatsRxInErrorPkts=_WwpLeosPortTotalStatsRxInErrorPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,3,1,63),_WwpLeosPortTotalStatsRxInErrorPkts_Type())
wwpLeosPortTotalStatsRxInErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalStatsRxInErrorPkts.setStatus(_A)
_WwpLeosPortHCStatsTable_Object=MibTable
wwpLeosPortHCStatsTable=_WwpLeosPortHCStatsTable_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4))
if mibBuilder.loadTexts:wwpLeosPortHCStatsTable.setStatus(_A)
_WwpLeosPortHCStatsEntry_Object=MibTableRow
wwpLeosPortHCStatsEntry=_WwpLeosPortHCStatsEntry_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1))
wwpLeosPortHCStatsEntry.setIndexNames((0,_G,_K))
if mibBuilder.loadTexts:wwpLeosPortHCStatsEntry.setStatus(_A)
class _WwpLeosPortHCStatsPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortHCStatsPortId_Type.__name__=_C
_WwpLeosPortHCStatsPortId_Object=MibTableColumn
wwpLeosPortHCStatsPortId=_WwpLeosPortHCStatsPortId_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,1),_WwpLeosPortHCStatsPortId_Type())
wwpLeosPortHCStatsPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsPortId.setStatus(_A)
_WwpLeosPortHCStatsRxBytes_Type=Counter64
_WwpLeosPortHCStatsRxBytes_Object=MibTableColumn
wwpLeosPortHCStatsRxBytes=_WwpLeosPortHCStatsRxBytes_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,2),_WwpLeosPortHCStatsRxBytes_Type())
wwpLeosPortHCStatsRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsRxBytes.setStatus(_A)
_WwpLeosPortHCStatsRxPkts_Type=Counter64
_WwpLeosPortHCStatsRxPkts_Object=MibTableColumn
wwpLeosPortHCStatsRxPkts=_WwpLeosPortHCStatsRxPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,3),_WwpLeosPortHCStatsRxPkts_Type())
wwpLeosPortHCStatsRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsRxPkts.setStatus(_A)
_WwpLeosPortHCStatsRxCrcErrorPkts_Type=Counter64
_WwpLeosPortHCStatsRxCrcErrorPkts_Object=MibTableColumn
wwpLeosPortHCStatsRxCrcErrorPkts=_WwpLeosPortHCStatsRxCrcErrorPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,4),_WwpLeosPortHCStatsRxCrcErrorPkts_Type())
wwpLeosPortHCStatsRxCrcErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsRxCrcErrorPkts.setStatus(_A)
_WwpLeosPortHCStatsRxBcastPkts_Type=Counter64
_WwpLeosPortHCStatsRxBcastPkts_Object=MibTableColumn
wwpLeosPortHCStatsRxBcastPkts=_WwpLeosPortHCStatsRxBcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,5),_WwpLeosPortHCStatsRxBcastPkts_Type())
wwpLeosPortHCStatsRxBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsRxBcastPkts.setStatus(_A)
_WwpLeosPortHCStatsUndersizePkts_Type=Counter64
_WwpLeosPortHCStatsUndersizePkts_Object=MibTableColumn
wwpLeosPortHCStatsUndersizePkts=_WwpLeosPortHCStatsUndersizePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,6),_WwpLeosPortHCStatsUndersizePkts_Type())
wwpLeosPortHCStatsUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsUndersizePkts.setStatus(_A)
_WwpLeosPortHCStatsOversizePkts_Type=Counter64
_WwpLeosPortHCStatsOversizePkts_Object=MibTableColumn
wwpLeosPortHCStatsOversizePkts=_WwpLeosPortHCStatsOversizePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,7),_WwpLeosPortHCStatsOversizePkts_Type())
wwpLeosPortHCStatsOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsOversizePkts.setStatus(_A)
_WwpLeosPortHCStatsFragmentPkts_Type=Counter64
_WwpLeosPortHCStatsFragmentPkts_Object=MibTableColumn
wwpLeosPortHCStatsFragmentPkts=_WwpLeosPortHCStatsFragmentPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,8),_WwpLeosPortHCStatsFragmentPkts_Type())
wwpLeosPortHCStatsFragmentPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsFragmentPkts.setStatus(_A)
_WwpLeosPortHCStatsJabberPkts_Type=Counter64
_WwpLeosPortHCStatsJabberPkts_Object=MibTableColumn
wwpLeosPortHCStatsJabberPkts=_WwpLeosPortHCStatsJabberPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,9),_WwpLeosPortHCStatsJabberPkts_Type())
wwpLeosPortHCStatsJabberPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsJabberPkts.setStatus(_A)
_WwpLeosPortHCStats64BytePkts_Type=Counter64
_WwpLeosPortHCStats64BytePkts_Object=MibTableColumn
wwpLeosPortHCStats64BytePkts=_WwpLeosPortHCStats64BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,10),_WwpLeosPortHCStats64BytePkts_Type())
wwpLeosPortHCStats64BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStats64BytePkts.setStatus(_A)
_WwpLeosPortHCStats65To127BytePkts_Type=Counter64
_WwpLeosPortHCStats65To127BytePkts_Object=MibTableColumn
wwpLeosPortHCStats65To127BytePkts=_WwpLeosPortHCStats65To127BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,11),_WwpLeosPortHCStats65To127BytePkts_Type())
wwpLeosPortHCStats65To127BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStats65To127BytePkts.setStatus(_A)
_WwpLeosPortHCStats128To255BytePkts_Type=Counter64
_WwpLeosPortHCStats128To255BytePkts_Object=MibTableColumn
wwpLeosPortHCStats128To255BytePkts=_WwpLeosPortHCStats128To255BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,12),_WwpLeosPortHCStats128To255BytePkts_Type())
wwpLeosPortHCStats128To255BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStats128To255BytePkts.setStatus(_A)
_WwpLeosPortHCStats256To511BytePkts_Type=Counter64
_WwpLeosPortHCStats256To511BytePkts_Object=MibTableColumn
wwpLeosPortHCStats256To511BytePkts=_WwpLeosPortHCStats256To511BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,13),_WwpLeosPortHCStats256To511BytePkts_Type())
wwpLeosPortHCStats256To511BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStats256To511BytePkts.setStatus(_A)
_WwpLeosPortHCStats512To1023BytePkts_Type=Counter64
_WwpLeosPortHCStats512To1023BytePkts_Object=MibTableColumn
wwpLeosPortHCStats512To1023BytePkts=_WwpLeosPortHCStats512To1023BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,14),_WwpLeosPortHCStats512To1023BytePkts_Type())
wwpLeosPortHCStats512To1023BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStats512To1023BytePkts.setStatus(_A)
_WwpLeosPortHCStats1024To1518BytePkts_Type=Counter64
_WwpLeosPortHCStats1024To1518BytePkts_Object=MibTableColumn
wwpLeosPortHCStats1024To1518BytePkts=_WwpLeosPortHCStats1024To1518BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,15),_WwpLeosPortHCStats1024To1518BytePkts_Type())
wwpLeosPortHCStats1024To1518BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStats1024To1518BytePkts.setStatus(_A)
_WwpLeosPortHCStatsTxBytes_Type=Counter64
_WwpLeosPortHCStatsTxBytes_Object=MibTableColumn
wwpLeosPortHCStatsTxBytes=_WwpLeosPortHCStatsTxBytes_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,16),_WwpLeosPortHCStatsTxBytes_Type())
wwpLeosPortHCStatsTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTxBytes.setStatus(_A)
_WwpLeosPortHCStatsTxTBytes_Type=Counter64
_WwpLeosPortHCStatsTxTBytes_Object=MibTableColumn
wwpLeosPortHCStatsTxTBytes=_WwpLeosPortHCStatsTxTBytes_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,17),_WwpLeosPortHCStatsTxTBytes_Type())
wwpLeosPortHCStatsTxTBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTxTBytes.setStatus(_H)
_WwpLeosPortHCStatsTxPkts_Type=Counter64
_WwpLeosPortHCStatsTxPkts_Object=MibTableColumn
wwpLeosPortHCStatsTxPkts=_WwpLeosPortHCStatsTxPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,18),_WwpLeosPortHCStatsTxPkts_Type())
wwpLeosPortHCStatsTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTxPkts.setStatus(_A)
_WwpLeosPortHCStatsTxExDeferPkts_Type=Counter64
_WwpLeosPortHCStatsTxExDeferPkts_Object=MibTableColumn
wwpLeosPortHCStatsTxExDeferPkts=_WwpLeosPortHCStatsTxExDeferPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,19),_WwpLeosPortHCStatsTxExDeferPkts_Type())
wwpLeosPortHCStatsTxExDeferPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTxExDeferPkts.setStatus(_A)
_WwpLeosPortHCStatsTxGiantPkts_Type=Counter64
_WwpLeosPortHCStatsTxGiantPkts_Object=MibTableColumn
wwpLeosPortHCStatsTxGiantPkts=_WwpLeosPortHCStatsTxGiantPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,20),_WwpLeosPortHCStatsTxGiantPkts_Type())
wwpLeosPortHCStatsTxGiantPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTxGiantPkts.setStatus(_A)
_WwpLeosPortHCStatsTxUnderRunPkts_Type=Counter64
_WwpLeosPortHCStatsTxUnderRunPkts_Object=MibTableColumn
wwpLeosPortHCStatsTxUnderRunPkts=_WwpLeosPortHCStatsTxUnderRunPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,21),_WwpLeosPortHCStatsTxUnderRunPkts_Type())
wwpLeosPortHCStatsTxUnderRunPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTxUnderRunPkts.setStatus(_A)
_WwpLeosPortHCStatsTxCrcErrorPkts_Type=Counter64
_WwpLeosPortHCStatsTxCrcErrorPkts_Object=MibTableColumn
wwpLeosPortHCStatsTxCrcErrorPkts=_WwpLeosPortHCStatsTxCrcErrorPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,22),_WwpLeosPortHCStatsTxCrcErrorPkts_Type())
wwpLeosPortHCStatsTxCrcErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTxCrcErrorPkts.setStatus(_A)
_WwpLeosPortHCStatsTxLCheckErrorPkts_Type=Counter64
_WwpLeosPortHCStatsTxLCheckErrorPkts_Object=MibTableColumn
wwpLeosPortHCStatsTxLCheckErrorPkts=_WwpLeosPortHCStatsTxLCheckErrorPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,23),_WwpLeosPortHCStatsTxLCheckErrorPkts_Type())
wwpLeosPortHCStatsTxLCheckErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTxLCheckErrorPkts.setStatus(_A)
_WwpLeosPortHCStatsTxLOutRangePkts_Type=Counter64
_WwpLeosPortHCStatsTxLOutRangePkts_Object=MibTableColumn
wwpLeosPortHCStatsTxLOutRangePkts=_WwpLeosPortHCStatsTxLOutRangePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,24),_WwpLeosPortHCStatsTxLOutRangePkts_Type())
wwpLeosPortHCStatsTxLOutRangePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTxLOutRangePkts.setStatus(_A)
_WwpLeosPortHCStatsTxLateCollPkts_Type=Counter64
_WwpLeosPortHCStatsTxLateCollPkts_Object=MibTableColumn
wwpLeosPortHCStatsTxLateCollPkts=_WwpLeosPortHCStatsTxLateCollPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,25),_WwpLeosPortHCStatsTxLateCollPkts_Type())
wwpLeosPortHCStatsTxLateCollPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTxLateCollPkts.setStatus(_A)
_WwpLeosPortHCStatsTxExCollPkts_Type=Counter64
_WwpLeosPortHCStatsTxExCollPkts_Object=MibTableColumn
wwpLeosPortHCStatsTxExCollPkts=_WwpLeosPortHCStatsTxExCollPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,26),_WwpLeosPortHCStatsTxExCollPkts_Type())
wwpLeosPortHCStatsTxExCollPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTxExCollPkts.setStatus(_A)
_WwpLeosPortHCStatsTxSingleCollPkts_Type=Counter64
_WwpLeosPortHCStatsTxSingleCollPkts_Object=MibTableColumn
wwpLeosPortHCStatsTxSingleCollPkts=_WwpLeosPortHCStatsTxSingleCollPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,27),_WwpLeosPortHCStatsTxSingleCollPkts_Type())
wwpLeosPortHCStatsTxSingleCollPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTxSingleCollPkts.setStatus(_A)
_WwpLeosPortHCStatsTxCollPkts_Type=Counter64
_WwpLeosPortHCStatsTxCollPkts_Object=MibTableColumn
wwpLeosPortHCStatsTxCollPkts=_WwpLeosPortHCStatsTxCollPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,28),_WwpLeosPortHCStatsTxCollPkts_Type())
wwpLeosPortHCStatsTxCollPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTxCollPkts.setStatus(_A)
_WwpLeosPortHCStatsTxPausePkts_Type=Counter64
_WwpLeosPortHCStatsTxPausePkts_Object=MibTableColumn
wwpLeosPortHCStatsTxPausePkts=_WwpLeosPortHCStatsTxPausePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,29),_WwpLeosPortHCStatsTxPausePkts_Type())
wwpLeosPortHCStatsTxPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTxPausePkts.setStatus(_A)
_WwpLeosPortHCStatsTxMcastPkts_Type=Counter64
_WwpLeosPortHCStatsTxMcastPkts_Object=MibTableColumn
wwpLeosPortHCStatsTxMcastPkts=_WwpLeosPortHCStatsTxMcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,30),_WwpLeosPortHCStatsTxMcastPkts_Type())
wwpLeosPortHCStatsTxMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTxMcastPkts.setStatus(_A)
_WwpLeosPortHCStatsTxBcastPkts_Type=Counter64
_WwpLeosPortHCStatsTxBcastPkts_Object=MibTableColumn
wwpLeosPortHCStatsTxBcastPkts=_WwpLeosPortHCStatsTxBcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,31),_WwpLeosPortHCStatsTxBcastPkts_Type())
wwpLeosPortHCStatsTxBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTxBcastPkts.setStatus(_A)
class _WwpLeosPortHCStatsPortReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_WwpLeosPortHCStatsPortReset_Type.__name__=_C
_WwpLeosPortHCStatsPortReset_Object=MibTableColumn
wwpLeosPortHCStatsPortReset=_WwpLeosPortHCStatsPortReset_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,32),_WwpLeosPortHCStatsPortReset_Type())
wwpLeosPortHCStatsPortReset.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosPortHCStatsPortReset.setStatus(_A)
_WwpLeosPortHCStatsRxMcastPkts_Type=Counter64
_WwpLeosPortHCStatsRxMcastPkts_Object=MibTableColumn
wwpLeosPortHCStatsRxMcastPkts=_WwpLeosPortHCStatsRxMcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,33),_WwpLeosPortHCStatsRxMcastPkts_Type())
wwpLeosPortHCStatsRxMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsRxMcastPkts.setStatus(_A)
_WwpLeosPortHCStatsRxPausePkts_Type=Counter64
_WwpLeosPortHCStatsRxPausePkts_Object=MibTableColumn
wwpLeosPortHCStatsRxPausePkts=_WwpLeosPortHCStatsRxPausePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,34),_WwpLeosPortHCStatsRxPausePkts_Type())
wwpLeosPortHCStatsRxPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsRxPausePkts.setStatus(_A)
_WwpLeosPortHCStats1519To2047BytePkts_Type=Counter64
_WwpLeosPortHCStats1519To2047BytePkts_Object=MibTableColumn
wwpLeosPortHCStats1519To2047BytePkts=_WwpLeosPortHCStats1519To2047BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,35),_WwpLeosPortHCStats1519To2047BytePkts_Type())
wwpLeosPortHCStats1519To2047BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStats1519To2047BytePkts.setStatus(_A)
_WwpLeosPortHCStats2048To4095BytePkts_Type=Counter64
_WwpLeosPortHCStats2048To4095BytePkts_Object=MibTableColumn
wwpLeosPortHCStats2048To4095BytePkts=_WwpLeosPortHCStats2048To4095BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,36),_WwpLeosPortHCStats2048To4095BytePkts_Type())
wwpLeosPortHCStats2048To4095BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStats2048To4095BytePkts.setStatus(_A)
_WwpLeosPortHCStats4096To9216BytePkts_Type=Counter64
_WwpLeosPortHCStats4096To9216BytePkts_Object=MibTableColumn
wwpLeosPortHCStats4096To9216BytePkts=_WwpLeosPortHCStats4096To9216BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,37),_WwpLeosPortHCStats4096To9216BytePkts_Type())
wwpLeosPortHCStats4096To9216BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStats4096To9216BytePkts.setStatus(_A)
_WwpLeosPortHCStatsTxDeferPkts_Type=Counter64
_WwpLeosPortHCStatsTxDeferPkts_Object=MibTableColumn
wwpLeosPortHCStatsTxDeferPkts=_WwpLeosPortHCStatsTxDeferPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,38),_WwpLeosPortHCStatsTxDeferPkts_Type())
wwpLeosPortHCStatsTxDeferPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTxDeferPkts.setStatus(_A)
_WwpLeosPortHCStatsTx64BytePkts_Type=Counter64
_WwpLeosPortHCStatsTx64BytePkts_Object=MibTableColumn
wwpLeosPortHCStatsTx64BytePkts=_WwpLeosPortHCStatsTx64BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,39),_WwpLeosPortHCStatsTx64BytePkts_Type())
wwpLeosPortHCStatsTx64BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTx64BytePkts.setStatus(_A)
_WwpLeosPortHCStatsTx65To127BytePkts_Type=Counter64
_WwpLeosPortHCStatsTx65To127BytePkts_Object=MibTableColumn
wwpLeosPortHCStatsTx65To127BytePkts=_WwpLeosPortHCStatsTx65To127BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,40),_WwpLeosPortHCStatsTx65To127BytePkts_Type())
wwpLeosPortHCStatsTx65To127BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTx65To127BytePkts.setStatus(_A)
_WwpLeosPortHCStatsTx128To255BytePkts_Type=Counter64
_WwpLeosPortHCStatsTx128To255BytePkts_Object=MibTableColumn
wwpLeosPortHCStatsTx128To255BytePkts=_WwpLeosPortHCStatsTx128To255BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,41),_WwpLeosPortHCStatsTx128To255BytePkts_Type())
wwpLeosPortHCStatsTx128To255BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTx128To255BytePkts.setStatus(_A)
_WwpLeosPortHCStatsTx256To511BytePkts_Type=Counter64
_WwpLeosPortHCStatsTx256To511BytePkts_Object=MibTableColumn
wwpLeosPortHCStatsTx256To511BytePkts=_WwpLeosPortHCStatsTx256To511BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,42),_WwpLeosPortHCStatsTx256To511BytePkts_Type())
wwpLeosPortHCStatsTx256To511BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTx256To511BytePkts.setStatus(_A)
_WwpLeosPortHCStatsTx512To1023BytePkts_Type=Counter64
_WwpLeosPortHCStatsTx512To1023BytePkts_Object=MibTableColumn
wwpLeosPortHCStatsTx512To1023BytePkts=_WwpLeosPortHCStatsTx512To1023BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,43),_WwpLeosPortHCStatsTx512To1023BytePkts_Type())
wwpLeosPortHCStatsTx512To1023BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTx512To1023BytePkts.setStatus(_A)
_WwpLeosPortHCStatsTx1024To1518BytePkts_Type=Counter64
_WwpLeosPortHCStatsTx1024To1518BytePkts_Object=MibTableColumn
wwpLeosPortHCStatsTx1024To1518BytePkts=_WwpLeosPortHCStatsTx1024To1518BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,44),_WwpLeosPortHCStatsTx1024To1518BytePkts_Type())
wwpLeosPortHCStatsTx1024To1518BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTx1024To1518BytePkts.setStatus(_A)
_WwpLeosPortHCStatsTx1519To2047BytePkts_Type=Counter64
_WwpLeosPortHCStatsTx1519To2047BytePkts_Object=MibTableColumn
wwpLeosPortHCStatsTx1519To2047BytePkts=_WwpLeosPortHCStatsTx1519To2047BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,45),_WwpLeosPortHCStatsTx1519To2047BytePkts_Type())
wwpLeosPortHCStatsTx1519To2047BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTx1519To2047BytePkts.setStatus(_A)
_WwpLeosPortHCStatsTx2048To4095BytePkts_Type=Counter64
_WwpLeosPortHCStatsTx2048To4095BytePkts_Object=MibTableColumn
wwpLeosPortHCStatsTx2048To4095BytePkts=_WwpLeosPortHCStatsTx2048To4095BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,46),_WwpLeosPortHCStatsTx2048To4095BytePkts_Type())
wwpLeosPortHCStatsTx2048To4095BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTx2048To4095BytePkts.setStatus(_A)
_WwpLeosPortHCStatsTx4096To9216BytePkts_Type=Counter64
_WwpLeosPortHCStatsTx4096To9216BytePkts_Object=MibTableColumn
wwpLeosPortHCStatsTx4096To9216BytePkts=_WwpLeosPortHCStatsTx4096To9216BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,47),_WwpLeosPortHCStatsTx4096To9216BytePkts_Type())
wwpLeosPortHCStatsTx4096To9216BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTx4096To9216BytePkts.setStatus(_A)
_WwpLeosPortHCStatsRxUcastPkts_Type=Counter64
_WwpLeosPortHCStatsRxUcastPkts_Object=MibTableColumn
wwpLeosPortHCStatsRxUcastPkts=_WwpLeosPortHCStatsRxUcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,48),_WwpLeosPortHCStatsRxUcastPkts_Type())
wwpLeosPortHCStatsRxUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsRxUcastPkts.setStatus(_A)
_WwpLeosPortHCStatsTxUcastPkts_Type=Counter64
_WwpLeosPortHCStatsTxUcastPkts_Object=MibTableColumn
wwpLeosPortHCStatsTxUcastPkts=_WwpLeosPortHCStatsTxUcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,49),_WwpLeosPortHCStatsTxUcastPkts_Type())
wwpLeosPortHCStatsTxUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsTxUcastPkts.setStatus(_A)
_WwpLeosPortHCStatsRxDropPkts_Type=Counter64
_WwpLeosPortHCStatsRxDropPkts_Object=MibTableColumn
wwpLeosPortHCStatsRxDropPkts=_WwpLeosPortHCStatsRxDropPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,50),_WwpLeosPortHCStatsRxDropPkts_Type())
wwpLeosPortHCStatsRxDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsRxDropPkts.setStatus(_A)
_WwpLeosPortHCStatsRxDiscardPkts_Type=Counter64
_WwpLeosPortHCStatsRxDiscardPkts_Object=MibTableColumn
wwpLeosPortHCStatsRxDiscardPkts=_WwpLeosPortHCStatsRxDiscardPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,51),_WwpLeosPortHCStatsRxDiscardPkts_Type())
wwpLeosPortHCStatsRxDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsRxDiscardPkts.setStatus(_A)
_WwpLeosPortHCStatsRxLOutRangePkts_Type=Counter64
_WwpLeosPortHCStatsRxLOutRangePkts_Object=MibTableColumn
wwpLeosPortHCStatsRxLOutRangePkts=_WwpLeosPortHCStatsRxLOutRangePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,52),_WwpLeosPortHCStatsRxLOutRangePkts_Type())
wwpLeosPortHCStatsRxLOutRangePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsRxLOutRangePkts.setStatus(_A)
_WwpLeosPortHCStatsRxInErrorPkts_Type=Counter64
_WwpLeosPortHCStatsRxInErrorPkts_Object=MibTableColumn
wwpLeosPortHCStatsRxInErrorPkts=_WwpLeosPortHCStatsRxInErrorPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,53),_WwpLeosPortHCStatsRxInErrorPkts_Type())
wwpLeosPortHCStatsRxInErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsRxInErrorPkts.setStatus(_A)
_WwpLeosPortHCStatsLastRefresh_Type=TimeTicks
_WwpLeosPortHCStatsLastRefresh_Object=MibTableColumn
wwpLeosPortHCStatsLastRefresh=_WwpLeosPortHCStatsLastRefresh_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,54),_WwpLeosPortHCStatsLastRefresh_Type())
wwpLeosPortHCStatsLastRefresh.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsLastRefresh.setStatus(_A)
_WwpLeosPortHCStatsLastChange_Type=TimeTicks
_WwpLeosPortHCStatsLastChange_Object=MibTableColumn
wwpLeosPortHCStatsLastChange=_WwpLeosPortHCStatsLastChange_Object((1,3,6,1,4,1,6141,2,60,3,1,1,4,1,55),_WwpLeosPortHCStatsLastChange_Type())
wwpLeosPortHCStatsLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortHCStatsLastChange.setStatus(_A)
_WwpLeosPortTotalHCStatsTable_Object=MibTable
wwpLeosPortTotalHCStatsTable=_WwpLeosPortTotalHCStatsTable_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5))
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTable.setStatus(_A)
_WwpLeosPortTotalHCStatsEntry_Object=MibTableRow
wwpLeosPortTotalHCStatsEntry=_WwpLeosPortTotalHCStatsEntry_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1))
wwpLeosPortTotalHCStatsEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsEntry.setStatus(_A)
class _WwpLeosPortTotalHCStatsPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosPortTotalHCStatsPortId_Type.__name__=_C
_WwpLeosPortTotalHCStatsPortId_Object=MibTableColumn
wwpLeosPortTotalHCStatsPortId=_WwpLeosPortTotalHCStatsPortId_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,1),_WwpLeosPortTotalHCStatsPortId_Type())
wwpLeosPortTotalHCStatsPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsPortId.setStatus(_A)
_WwpLeosPortTotalHCStatsRxBytes_Type=Counter64
_WwpLeosPortTotalHCStatsRxBytes_Object=MibTableColumn
wwpLeosPortTotalHCStatsRxBytes=_WwpLeosPortTotalHCStatsRxBytes_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,2),_WwpLeosPortTotalHCStatsRxBytes_Type())
wwpLeosPortTotalHCStatsRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsRxBytes.setStatus(_A)
_WwpLeosPortTotalHCStatsRxPkts_Type=Counter64
_WwpLeosPortTotalHCStatsRxPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsRxPkts=_WwpLeosPortTotalHCStatsRxPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,3),_WwpLeosPortTotalHCStatsRxPkts_Type())
wwpLeosPortTotalHCStatsRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsRxPkts.setStatus(_A)
_WwpLeosPortTotalHCStatsRxCrcErrorPkts_Type=Counter64
_WwpLeosPortTotalHCStatsRxCrcErrorPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsRxCrcErrorPkts=_WwpLeosPortTotalHCStatsRxCrcErrorPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,4),_WwpLeosPortTotalHCStatsRxCrcErrorPkts_Type())
wwpLeosPortTotalHCStatsRxCrcErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsRxCrcErrorPkts.setStatus(_A)
_WwpLeosPortTotalHCStatsRxBcastPkts_Type=Counter64
_WwpLeosPortTotalHCStatsRxBcastPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsRxBcastPkts=_WwpLeosPortTotalHCStatsRxBcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,5),_WwpLeosPortTotalHCStatsRxBcastPkts_Type())
wwpLeosPortTotalHCStatsRxBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsRxBcastPkts.setStatus(_A)
_WwpLeosPortTotalHCStatsUndersizePkts_Type=Counter64
_WwpLeosPortTotalHCStatsUndersizePkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsUndersizePkts=_WwpLeosPortTotalHCStatsUndersizePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,6),_WwpLeosPortTotalHCStatsUndersizePkts_Type())
wwpLeosPortTotalHCStatsUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsUndersizePkts.setStatus(_A)
_WwpLeosPortTotalHCStatsOversizePkts_Type=Counter64
_WwpLeosPortTotalHCStatsOversizePkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsOversizePkts=_WwpLeosPortTotalHCStatsOversizePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,7),_WwpLeosPortTotalHCStatsOversizePkts_Type())
wwpLeosPortTotalHCStatsOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsOversizePkts.setStatus(_A)
_WwpLeosPortTotalHCStatsFragmentPkts_Type=Counter64
_WwpLeosPortTotalHCStatsFragmentPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsFragmentPkts=_WwpLeosPortTotalHCStatsFragmentPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,8),_WwpLeosPortTotalHCStatsFragmentPkts_Type())
wwpLeosPortTotalHCStatsFragmentPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsFragmentPkts.setStatus(_A)
_WwpLeosPortTotalHCStatsJabberPkts_Type=Counter64
_WwpLeosPortTotalHCStatsJabberPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsJabberPkts=_WwpLeosPortTotalHCStatsJabberPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,9),_WwpLeosPortTotalHCStatsJabberPkts_Type())
wwpLeosPortTotalHCStatsJabberPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsJabberPkts.setStatus(_A)
_WwpLeosPortTotalHCStats64BytePkts_Type=Counter64
_WwpLeosPortTotalHCStats64BytePkts_Object=MibTableColumn
wwpLeosPortTotalHCStats64BytePkts=_WwpLeosPortTotalHCStats64BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,10),_WwpLeosPortTotalHCStats64BytePkts_Type())
wwpLeosPortTotalHCStats64BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStats64BytePkts.setStatus(_A)
_WwpLeosPortTotalHCStats65To127BytePkts_Type=Counter64
_WwpLeosPortTotalHCStats65To127BytePkts_Object=MibTableColumn
wwpLeosPortTotalHCStats65To127BytePkts=_WwpLeosPortTotalHCStats65To127BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,11),_WwpLeosPortTotalHCStats65To127BytePkts_Type())
wwpLeosPortTotalHCStats65To127BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStats65To127BytePkts.setStatus(_A)
_WwpLeosPortTotalHCStats128To255BytePkts_Type=Counter64
_WwpLeosPortTotalHCStats128To255BytePkts_Object=MibTableColumn
wwpLeosPortTotalHCStats128To255BytePkts=_WwpLeosPortTotalHCStats128To255BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,12),_WwpLeosPortTotalHCStats128To255BytePkts_Type())
wwpLeosPortTotalHCStats128To255BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStats128To255BytePkts.setStatus(_A)
_WwpLeosPortTotalHCStats256To511BytePkts_Type=Counter64
_WwpLeosPortTotalHCStats256To511BytePkts_Object=MibTableColumn
wwpLeosPortTotalHCStats256To511BytePkts=_WwpLeosPortTotalHCStats256To511BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,13),_WwpLeosPortTotalHCStats256To511BytePkts_Type())
wwpLeosPortTotalHCStats256To511BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStats256To511BytePkts.setStatus(_A)
_WwpLeosPortTotalHCStats512To1023BytePkts_Type=Counter64
_WwpLeosPortTotalHCStats512To1023BytePkts_Object=MibTableColumn
wwpLeosPortTotalHCStats512To1023BytePkts=_WwpLeosPortTotalHCStats512To1023BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,14),_WwpLeosPortTotalHCStats512To1023BytePkts_Type())
wwpLeosPortTotalHCStats512To1023BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStats512To1023BytePkts.setStatus(_A)
_WwpLeosPortTotalHCStats1024To1518BytePkts_Type=Counter64
_WwpLeosPortTotalHCStats1024To1518BytePkts_Object=MibTableColumn
wwpLeosPortTotalHCStats1024To1518BytePkts=_WwpLeosPortTotalHCStats1024To1518BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,15),_WwpLeosPortTotalHCStats1024To1518BytePkts_Type())
wwpLeosPortTotalHCStats1024To1518BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStats1024To1518BytePkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTxBytes_Type=Counter64
_WwpLeosPortTotalHCStatsTxBytes_Object=MibTableColumn
wwpLeosPortTotalHCStatsTxBytes=_WwpLeosPortTotalHCStatsTxBytes_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,16),_WwpLeosPortTotalHCStatsTxBytes_Type())
wwpLeosPortTotalHCStatsTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTxBytes.setStatus(_A)
_WwpLeosPortTotalHCStatsTxTBytes_Type=Counter64
_WwpLeosPortTotalHCStatsTxTBytes_Object=MibTableColumn
wwpLeosPortTotalHCStatsTxTBytes=_WwpLeosPortTotalHCStatsTxTBytes_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,17),_WwpLeosPortTotalHCStatsTxTBytes_Type())
wwpLeosPortTotalHCStatsTxTBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTxTBytes.setStatus(_H)
_WwpLeosPortTotalHCStatsTxPkts_Type=Counter64
_WwpLeosPortTotalHCStatsTxPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTxPkts=_WwpLeosPortTotalHCStatsTxPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,18),_WwpLeosPortTotalHCStatsTxPkts_Type())
wwpLeosPortTotalHCStatsTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTxPkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTxExDeferPkts_Type=Counter64
_WwpLeosPortTotalHCStatsTxExDeferPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTxExDeferPkts=_WwpLeosPortTotalHCStatsTxExDeferPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,19),_WwpLeosPortTotalHCStatsTxExDeferPkts_Type())
wwpLeosPortTotalHCStatsTxExDeferPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTxExDeferPkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTxGiantPkts_Type=Counter64
_WwpLeosPortTotalHCStatsTxGiantPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTxGiantPkts=_WwpLeosPortTotalHCStatsTxGiantPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,20),_WwpLeosPortTotalHCStatsTxGiantPkts_Type())
wwpLeosPortTotalHCStatsTxGiantPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTxGiantPkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTxUnderRunPkts_Type=Counter64
_WwpLeosPortTotalHCStatsTxUnderRunPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTxUnderRunPkts=_WwpLeosPortTotalHCStatsTxUnderRunPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,21),_WwpLeosPortTotalHCStatsTxUnderRunPkts_Type())
wwpLeosPortTotalHCStatsTxUnderRunPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTxUnderRunPkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTxCrcErrorPkts_Type=Counter64
_WwpLeosPortTotalHCStatsTxCrcErrorPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTxCrcErrorPkts=_WwpLeosPortTotalHCStatsTxCrcErrorPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,22),_WwpLeosPortTotalHCStatsTxCrcErrorPkts_Type())
wwpLeosPortTotalHCStatsTxCrcErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTxCrcErrorPkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTxLCheckErrorPkts_Type=Counter64
_WwpLeosPortTotalHCStatsTxLCheckErrorPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTxLCheckErrorPkts=_WwpLeosPortTotalHCStatsTxLCheckErrorPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,23),_WwpLeosPortTotalHCStatsTxLCheckErrorPkts_Type())
wwpLeosPortTotalHCStatsTxLCheckErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTxLCheckErrorPkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTxLOutRangePkts_Type=Counter64
_WwpLeosPortTotalHCStatsTxLOutRangePkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTxLOutRangePkts=_WwpLeosPortTotalHCStatsTxLOutRangePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,24),_WwpLeosPortTotalHCStatsTxLOutRangePkts_Type())
wwpLeosPortTotalHCStatsTxLOutRangePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTxLOutRangePkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTxLateCollPkts_Type=Counter64
_WwpLeosPortTotalHCStatsTxLateCollPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTxLateCollPkts=_WwpLeosPortTotalHCStatsTxLateCollPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,25),_WwpLeosPortTotalHCStatsTxLateCollPkts_Type())
wwpLeosPortTotalHCStatsTxLateCollPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTxLateCollPkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTxExCollPkts_Type=Counter64
_WwpLeosPortTotalHCStatsTxExCollPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTxExCollPkts=_WwpLeosPortTotalHCStatsTxExCollPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,26),_WwpLeosPortTotalHCStatsTxExCollPkts_Type())
wwpLeosPortTotalHCStatsTxExCollPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTxExCollPkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTxSingleCollPkts_Type=Counter64
_WwpLeosPortTotalHCStatsTxSingleCollPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTxSingleCollPkts=_WwpLeosPortTotalHCStatsTxSingleCollPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,27),_WwpLeosPortTotalHCStatsTxSingleCollPkts_Type())
wwpLeosPortTotalHCStatsTxSingleCollPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTxSingleCollPkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTxCollPkts_Type=Counter64
_WwpLeosPortTotalHCStatsTxCollPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTxCollPkts=_WwpLeosPortTotalHCStatsTxCollPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,28),_WwpLeosPortTotalHCStatsTxCollPkts_Type())
wwpLeosPortTotalHCStatsTxCollPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTxCollPkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTxPausePkts_Type=Counter64
_WwpLeosPortTotalHCStatsTxPausePkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTxPausePkts=_WwpLeosPortTotalHCStatsTxPausePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,29),_WwpLeosPortTotalHCStatsTxPausePkts_Type())
wwpLeosPortTotalHCStatsTxPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTxPausePkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTxMcastPkts_Type=Counter64
_WwpLeosPortTotalHCStatsTxMcastPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTxMcastPkts=_WwpLeosPortTotalHCStatsTxMcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,30),_WwpLeosPortTotalHCStatsTxMcastPkts_Type())
wwpLeosPortTotalHCStatsTxMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTxMcastPkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTxBcastPkts_Type=Counter64
_WwpLeosPortTotalHCStatsTxBcastPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTxBcastPkts=_WwpLeosPortTotalHCStatsTxBcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,31),_WwpLeosPortTotalHCStatsTxBcastPkts_Type())
wwpLeosPortTotalHCStatsTxBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTxBcastPkts.setStatus(_A)
class _WwpLeosPortTotalHCStatsPortReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_WwpLeosPortTotalHCStatsPortReset_Type.__name__=_C
_WwpLeosPortTotalHCStatsPortReset_Object=MibTableColumn
wwpLeosPortTotalHCStatsPortReset=_WwpLeosPortTotalHCStatsPortReset_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,32),_WwpLeosPortTotalHCStatsPortReset_Type())
wwpLeosPortTotalHCStatsPortReset.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsPortReset.setStatus(_A)
_WwpLeosPortTotalHCStatsRxMcastPkts_Type=Counter64
_WwpLeosPortTotalHCStatsRxMcastPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsRxMcastPkts=_WwpLeosPortTotalHCStatsRxMcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,33),_WwpLeosPortTotalHCStatsRxMcastPkts_Type())
wwpLeosPortTotalHCStatsRxMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsRxMcastPkts.setStatus(_A)
_WwpLeosPortTotalHCStatsRxPausePkts_Type=Counter64
_WwpLeosPortTotalHCStatsRxPausePkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsRxPausePkts=_WwpLeosPortTotalHCStatsRxPausePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,34),_WwpLeosPortTotalHCStatsRxPausePkts_Type())
wwpLeosPortTotalHCStatsRxPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsRxPausePkts.setStatus(_A)
_WwpLeosPortTotalHCStats1519To2047BytePkts_Type=Counter64
_WwpLeosPortTotalHCStats1519To2047BytePkts_Object=MibTableColumn
wwpLeosPortTotalHCStats1519To2047BytePkts=_WwpLeosPortTotalHCStats1519To2047BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,35),_WwpLeosPortTotalHCStats1519To2047BytePkts_Type())
wwpLeosPortTotalHCStats1519To2047BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStats1519To2047BytePkts.setStatus(_A)
_WwpLeosPortTotalHCStats2048To4095BytePkts_Type=Counter64
_WwpLeosPortTotalHCStats2048To4095BytePkts_Object=MibTableColumn
wwpLeosPortTotalHCStats2048To4095BytePkts=_WwpLeosPortTotalHCStats2048To4095BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,36),_WwpLeosPortTotalHCStats2048To4095BytePkts_Type())
wwpLeosPortTotalHCStats2048To4095BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStats2048To4095BytePkts.setStatus(_A)
_WwpLeosPortTotalHCStats4096To9216BytePkts_Type=Counter64
_WwpLeosPortTotalHCStats4096To9216BytePkts_Object=MibTableColumn
wwpLeosPortTotalHCStats4096To9216BytePkts=_WwpLeosPortTotalHCStats4096To9216BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,37),_WwpLeosPortTotalHCStats4096To9216BytePkts_Type())
wwpLeosPortTotalHCStats4096To9216BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStats4096To9216BytePkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTxDeferPkts_Type=Counter64
_WwpLeosPortTotalHCStatsTxDeferPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTxDeferPkts=_WwpLeosPortTotalHCStatsTxDeferPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,38),_WwpLeosPortTotalHCStatsTxDeferPkts_Type())
wwpLeosPortTotalHCStatsTxDeferPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTxDeferPkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTx64BytePkts_Type=Counter64
_WwpLeosPortTotalHCStatsTx64BytePkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTx64BytePkts=_WwpLeosPortTotalHCStatsTx64BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,39),_WwpLeosPortTotalHCStatsTx64BytePkts_Type())
wwpLeosPortTotalHCStatsTx64BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTx64BytePkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTx65To127BytePkts_Type=Counter64
_WwpLeosPortTotalHCStatsTx65To127BytePkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTx65To127BytePkts=_WwpLeosPortTotalHCStatsTx65To127BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,40),_WwpLeosPortTotalHCStatsTx65To127BytePkts_Type())
wwpLeosPortTotalHCStatsTx65To127BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTx65To127BytePkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTx128To255BytePkts_Type=Counter64
_WwpLeosPortTotalHCStatsTx128To255BytePkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTx128To255BytePkts=_WwpLeosPortTotalHCStatsTx128To255BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,41),_WwpLeosPortTotalHCStatsTx128To255BytePkts_Type())
wwpLeosPortTotalHCStatsTx128To255BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTx128To255BytePkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTx256To511BytePkts_Type=Counter64
_WwpLeosPortTotalHCStatsTx256To511BytePkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTx256To511BytePkts=_WwpLeosPortTotalHCStatsTx256To511BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,42),_WwpLeosPortTotalHCStatsTx256To511BytePkts_Type())
wwpLeosPortTotalHCStatsTx256To511BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTx256To511BytePkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTx512To1023BytePkts_Type=Counter64
_WwpLeosPortTotalHCStatsTx512To1023BytePkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTx512To1023BytePkts=_WwpLeosPortTotalHCStatsTx512To1023BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,43),_WwpLeosPortTotalHCStatsTx512To1023BytePkts_Type())
wwpLeosPortTotalHCStatsTx512To1023BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTx512To1023BytePkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTx1024To1518BytePkts_Type=Counter64
_WwpLeosPortTotalHCStatsTx1024To1518BytePkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTx1024To1518BytePkts=_WwpLeosPortTotalHCStatsTx1024To1518BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,44),_WwpLeosPortTotalHCStatsTx1024To1518BytePkts_Type())
wwpLeosPortTotalHCStatsTx1024To1518BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTx1024To1518BytePkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTx1519To2047BytePkts_Type=Counter64
_WwpLeosPortTotalHCStatsTx1519To2047BytePkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTx1519To2047BytePkts=_WwpLeosPortTotalHCStatsTx1519To2047BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,45),_WwpLeosPortTotalHCStatsTx1519To2047BytePkts_Type())
wwpLeosPortTotalHCStatsTx1519To2047BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTx1519To2047BytePkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTx2048To4095BytePkts_Type=Counter64
_WwpLeosPortTotalHCStatsTx2048To4095BytePkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTx2048To4095BytePkts=_WwpLeosPortTotalHCStatsTx2048To4095BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,46),_WwpLeosPortTotalHCStatsTx2048To4095BytePkts_Type())
wwpLeosPortTotalHCStatsTx2048To4095BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTx2048To4095BytePkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTx4096To9216BytePkts_Type=Counter64
_WwpLeosPortTotalHCStatsTx4096To9216BytePkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTx4096To9216BytePkts=_WwpLeosPortTotalHCStatsTx4096To9216BytePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,47),_WwpLeosPortTotalHCStatsTx4096To9216BytePkts_Type())
wwpLeosPortTotalHCStatsTx4096To9216BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTx4096To9216BytePkts.setStatus(_A)
_WwpLeosPortTotalHCStatsRxUcastPkts_Type=Counter64
_WwpLeosPortTotalHCStatsRxUcastPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsRxUcastPkts=_WwpLeosPortTotalHCStatsRxUcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,48),_WwpLeosPortTotalHCStatsRxUcastPkts_Type())
wwpLeosPortTotalHCStatsRxUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsRxUcastPkts.setStatus(_A)
_WwpLeosPortTotalHCStatsTxUcastPkts_Type=Counter64
_WwpLeosPortTotalHCStatsTxUcastPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsTxUcastPkts=_WwpLeosPortTotalHCStatsTxUcastPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,49),_WwpLeosPortTotalHCStatsTxUcastPkts_Type())
wwpLeosPortTotalHCStatsTxUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsTxUcastPkts.setStatus(_A)
_WwpLeosPortTotalHCStatsRxDropPkts_Type=Counter64
_WwpLeosPortTotalHCStatsRxDropPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsRxDropPkts=_WwpLeosPortTotalHCStatsRxDropPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,50),_WwpLeosPortTotalHCStatsRxDropPkts_Type())
wwpLeosPortTotalHCStatsRxDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsRxDropPkts.setStatus(_A)
_WwpLeosPortTotalHCStatsRxDiscardPkts_Type=Counter64
_WwpLeosPortTotalHCStatsRxDiscardPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsRxDiscardPkts=_WwpLeosPortTotalHCStatsRxDiscardPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,51),_WwpLeosPortTotalHCStatsRxDiscardPkts_Type())
wwpLeosPortTotalHCStatsRxDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsRxDiscardPkts.setStatus(_A)
_WwpLeosPortTotalHCStatsRxLOutRangePkts_Type=Counter64
_WwpLeosPortTotalHCStatsRxLOutRangePkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsRxLOutRangePkts=_WwpLeosPortTotalHCStatsRxLOutRangePkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,52),_WwpLeosPortTotalHCStatsRxLOutRangePkts_Type())
wwpLeosPortTotalHCStatsRxLOutRangePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsRxLOutRangePkts.setStatus(_A)
_WwpLeosPortTotalHCStatsRxInErrorPkts_Type=Counter64
_WwpLeosPortTotalHCStatsRxInErrorPkts_Object=MibTableColumn
wwpLeosPortTotalHCStatsRxInErrorPkts=_WwpLeosPortTotalHCStatsRxInErrorPkts_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,53),_WwpLeosPortTotalHCStatsRxInErrorPkts_Type())
wwpLeosPortTotalHCStatsRxInErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsRxInErrorPkts.setStatus(_A)
_WwpLeosPortTotalHCStatsLastRefresh_Type=TimeTicks
_WwpLeosPortTotalHCStatsLastRefresh_Object=MibTableColumn
wwpLeosPortTotalHCStatsLastRefresh=_WwpLeosPortTotalHCStatsLastRefresh_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,54),_WwpLeosPortTotalHCStatsLastRefresh_Type())
wwpLeosPortTotalHCStatsLastRefresh.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsLastRefresh.setStatus(_A)
_WwpLeosPortTotalHCStatsLastChange_Type=TimeTicks
_WwpLeosPortTotalHCStatsLastChange_Object=MibTableColumn
wwpLeosPortTotalHCStatsLastChange=_WwpLeosPortTotalHCStatsLastChange_Object((1,3,6,1,4,1,6141,2,60,3,1,1,5,1,55),_WwpLeosPortTotalHCStatsLastChange_Type())
wwpLeosPortTotalHCStatsLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosPortTotalHCStatsLastChange.setStatus(_A)
_WwpLeosPortStatsMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosPortStatsMIBNotificationPrefix=_WwpLeosPortStatsMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,3,2))
_WwpLeosPortStatsMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosPortStatsMIBNotifications=_WwpLeosPortStatsMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,3,2,0))
_WwpLeosPortStatsMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosPortStatsMIBConformance=_WwpLeosPortStatsMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,3,3))
_WwpLeosPortStatsMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosPortStatsMIBCompliances=_WwpLeosPortStatsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,3,3,1))
_WwpLeosPortStatsMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosPortStatsMIBGroups=_WwpLeosPortStatsMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,3,3,2))
mibBuilder.exportSymbols(_G,**{'wwpLeosPortStatsMIB':wwpLeosPortStatsMIB,'wwpLeosPortStatsMIBObjects':wwpLeosPortStatsMIBObjects,'wwpLeosPortStats':wwpLeosPortStats,'wwpLeosPortStatsReset':wwpLeosPortStatsReset,'wwpLeosPortStatsTable':wwpLeosPortStatsTable,'wwpLeosPortStatsEntry':wwpLeosPortStatsEntry,_I:wwpLeosPortStatsPortId,'wwpLeosPortStatsRxBytes':wwpLeosPortStatsRxBytes,'wwpLeosPortStatsRxPkts':wwpLeosPortStatsRxPkts,'wwpLeosPortStatsRxCrcErrorPkts':wwpLeosPortStatsRxCrcErrorPkts,'wwpLeosPortStatsRxBcastPkts':wwpLeosPortStatsRxBcastPkts,'wwpLeosPortStatsUndersizePkts':wwpLeosPortStatsUndersizePkts,'wwpLeosPortStatsOversizePkts':wwpLeosPortStatsOversizePkts,'wwpLeosPortStatsFragmentPkts':wwpLeosPortStatsFragmentPkts,'wwpLeosPortStatsJabberPkts':wwpLeosPortStatsJabberPkts,'wwpLeosPortStats64BytePkts':wwpLeosPortStats64BytePkts,'wwpLeosPortStats65To127BytePkts':wwpLeosPortStats65To127BytePkts,'wwpLeosPortStats128To255BytePkts':wwpLeosPortStats128To255BytePkts,'wwpLeosPortStats256To511BytePkts':wwpLeosPortStats256To511BytePkts,'wwpLeosPortStats512To1023BytePkts':wwpLeosPortStats512To1023BytePkts,'wwpLeosPortStats1024To1518BytePkts':wwpLeosPortStats1024To1518BytePkts,'wwpLeosPortStatsTxBytes':wwpLeosPortStatsTxBytes,'wwpLeosPortStatsTxTBytes':wwpLeosPortStatsTxTBytes,'wwpLeosPortStatsTxPkts':wwpLeosPortStatsTxPkts,'wwpLeosPortStatsTxExDeferPkts':wwpLeosPortStatsTxExDeferPkts,'wwpLeosPortStatsTxGiantPkts':wwpLeosPortStatsTxGiantPkts,'wwpLeosPortStatsTxUnderRunPkts':wwpLeosPortStatsTxUnderRunPkts,'wwpLeosPortStatsTxCrcErrorPkts':wwpLeosPortStatsTxCrcErrorPkts,'wwpLeosPortStatsTxLCheckErrorPkts':wwpLeosPortStatsTxLCheckErrorPkts,'wwpLeosPortStatsTxLOutRangePkts':wwpLeosPortStatsTxLOutRangePkts,'wwpLeosPortStatsTxLateCollPkts':wwpLeosPortStatsTxLateCollPkts,'wwpLeosPortStatsTxExCollPkts':wwpLeosPortStatsTxExCollPkts,'wwpLeosPortStatsTxSingleCollPkts':wwpLeosPortStatsTxSingleCollPkts,'wwpLeosPortStatsTxCollPkts':wwpLeosPortStatsTxCollPkts,'wwpLeosPortStatsTxPausePkts':wwpLeosPortStatsTxPausePkts,'wwpLeosPortStatsTxMcastPkts':wwpLeosPortStatsTxMcastPkts,'wwpLeosPortStatsTxBcastPkts':wwpLeosPortStatsTxBcastPkts,'wwpLeosPortStatsPortReset':wwpLeosPortStatsPortReset,'wwpLeosPortStatsRxMcastPkts':wwpLeosPortStatsRxMcastPkts,'wwpLeosPortStatsRxPausePkts':wwpLeosPortStatsRxPausePkts,'wwpLeosPortStats1519To2047BytePkts':wwpLeosPortStats1519To2047BytePkts,'wwpLeosPortStats2048To4095BytePkts':wwpLeosPortStats2048To4095BytePkts,'wwpLeosPortStats4096To9216BytePkts':wwpLeosPortStats4096To9216BytePkts,'wwpLeosPortStatsTxDeferPkts':wwpLeosPortStatsTxDeferPkts,'wwpLeosPortStatsTx64BytePkts':wwpLeosPortStatsTx64BytePkts,'wwpLeosPortStatsTx65To127BytePkts':wwpLeosPortStatsTx65To127BytePkts,'wwpLeosPortStatsTx128To255BytePkts':wwpLeosPortStatsTx128To255BytePkts,'wwpLeosPortStatsTx256To511BytePkts':wwpLeosPortStatsTx256To511BytePkts,'wwpLeosPortStatsTx512To1023BytePkts':wwpLeosPortStatsTx512To1023BytePkts,'wwpLeosPortStatsTx1024To1518BytePkts':wwpLeosPortStatsTx1024To1518BytePkts,'wwpLeosPortStatsTx1519To2047BytePkts':wwpLeosPortStatsTx1519To2047BytePkts,'wwpLeosPortStatsTx2048To4095BytePkts':wwpLeosPortStatsTx2048To4095BytePkts,'wwpLeosPortStatsTx4096To9216BytePkts':wwpLeosPortStatsTx4096To9216BytePkts,'wwpLeosPortStatsRxFpgaDropPkts':wwpLeosPortStatsRxFpgaDropPkts,'wwpLeosPortStatsPortLinkUp':wwpLeosPortStatsPortLinkUp,'wwpLeosPortStatsPortLinkDown':wwpLeosPortStatsPortLinkDown,'wwpLeosPortStatsPortLinkFlap':wwpLeosPortStatsPortLinkFlap,'wwpLeosPortStatsRxUcastPkts':wwpLeosPortStatsRxUcastPkts,'wwpLeosPortStatsTxUcastPkts':wwpLeosPortStatsTxUcastPkts,'wwpLeosPortStatsRxDropPkts':wwpLeosPortStatsRxDropPkts,'wwpLeosPortStatsRxDiscardPkts':wwpLeosPortStatsRxDiscardPkts,'wwpLeosPortStatsRxLOutRangePkts':wwpLeosPortStatsRxLOutRangePkts,'wwpLeosPortStatsRxFpgaBufferDropPkts':wwpLeosPortStatsRxFpgaBufferDropPkts,'wwpLeosPortStatsTxFpgaBufferDropPkts':wwpLeosPortStatsTxFpgaBufferDropPkts,'wwpLeosPortStatsFpgaVlanPriFilterDropPkts':wwpLeosPortStatsFpgaVlanPriFilterDropPkts,'wwpLeosPortStatsFpgaRxErrorPkts':wwpLeosPortStatsFpgaRxErrorPkts,'wwpLeosPortStatsFpgaRxCrcErrorPkts':wwpLeosPortStatsFpgaRxCrcErrorPkts,'wwpLeosPortStatsFpgaRxIpCrcErrorPkts':wwpLeosPortStatsFpgaRxIpCrcErrorPkts,'wwpLeosPortStatsRxInErrorPkts':wwpLeosPortStatsRxInErrorPkts,'wwpLeosPortTotalStatsTable':wwpLeosPortTotalStatsTable,'wwpLeosPortTotalStatsEntry':wwpLeosPortTotalStatsEntry,_J:wwpLeosPortTotalStatsPortId,'wwpLeosPortTotalStatsRxBytes':wwpLeosPortTotalStatsRxBytes,'wwpLeosPortTotalStatsRxPkts':wwpLeosPortTotalStatsRxPkts,'wwpLeosPortTotalStatsRxCrcErrorPkts':wwpLeosPortTotalStatsRxCrcErrorPkts,'wwpLeosPortTotalStatsRxBcastPkts':wwpLeosPortTotalStatsRxBcastPkts,'wwpLeosPortTotalStatsUndersizePkts':wwpLeosPortTotalStatsUndersizePkts,'wwpLeosPortTotalStatsOversizePkts':wwpLeosPortTotalStatsOversizePkts,'wwpLeosPortTotalStatsFragmentPkts':wwpLeosPortTotalStatsFragmentPkts,'wwpLeosPortTotalStatsJabberPkts':wwpLeosPortTotalStatsJabberPkts,'wwpLeosPortTotalStats64BytePkts':wwpLeosPortTotalStats64BytePkts,'wwpLeosPortTotalStats65To127BytePkts':wwpLeosPortTotalStats65To127BytePkts,'wwpLeosPortTotalStats128To255BytePkts':wwpLeosPortTotalStats128To255BytePkts,'wwpLeosPortTotalStats256To511BytePkts':wwpLeosPortTotalStats256To511BytePkts,'wwpLeosPortTotalStats512To1023BytePkts':wwpLeosPortTotalStats512To1023BytePkts,'wwpLeosPortTotalStats1024To1518BytePkts':wwpLeosPortTotalStats1024To1518BytePkts,'wwpLeosPortTotalStatsTxBytes':wwpLeosPortTotalStatsTxBytes,'wwpLeosPortTotalStatsTxTBytes':wwpLeosPortTotalStatsTxTBytes,'wwpLeosPortTotalStatsTxPkts':wwpLeosPortTotalStatsTxPkts,'wwpLeosPortTotalStatsTxExDeferPkts':wwpLeosPortTotalStatsTxExDeferPkts,'wwpLeosPortTotalStatsTxGiantPkts':wwpLeosPortTotalStatsTxGiantPkts,'wwpLeosPortTotalStatsTxUnderRunPkts':wwpLeosPortTotalStatsTxUnderRunPkts,'wwpLeosPortTotalStatsTxCrcErrorPkts':wwpLeosPortTotalStatsTxCrcErrorPkts,'wwpLeosPortTotalStatsTxLCheckErrorPkts':wwpLeosPortTotalStatsTxLCheckErrorPkts,'wwpLeosPortTotalStatsTxLOutRangePkts':wwpLeosPortTotalStatsTxLOutRangePkts,'wwpLeosPortTotalStatsTxLateCollPkts':wwpLeosPortTotalStatsTxLateCollPkts,'wwpLeosPortTotalStatsTxExCollPkts':wwpLeosPortTotalStatsTxExCollPkts,'wwpLeosPortTotalStatsTxSingleCollPkts':wwpLeosPortTotalStatsTxSingleCollPkts,'wwpLeosPortTotalStatsTxCollPkts':wwpLeosPortTotalStatsTxCollPkts,'wwpLeosPortTotalStatsTxPausePkts':wwpLeosPortTotalStatsTxPausePkts,'wwpLeosPortTotalStatsTxMcastPkts':wwpLeosPortTotalStatsTxMcastPkts,'wwpLeosPortTotalStatsTxBcastPkts':wwpLeosPortTotalStatsTxBcastPkts,'wwpLeosPortTotalStatsPortReset':wwpLeosPortTotalStatsPortReset,'wwpLeosPortTotalStatsRxMcastPkts':wwpLeosPortTotalStatsRxMcastPkts,'wwpLeosPortTotalStatsRxPausePkts':wwpLeosPortTotalStatsRxPausePkts,'wwpLeosPortTotalStats1519To2047BytePkts':wwpLeosPortTotalStats1519To2047BytePkts,'wwpLeosPortTotalStats2048To4095BytePkts':wwpLeosPortTotalStats2048To4095BytePkts,'wwpLeosPortTotalStats4096To9216BytePkts':wwpLeosPortTotalStats4096To9216BytePkts,'wwpLeosPortTotalStatsTxDeferPkts':wwpLeosPortTotalStatsTxDeferPkts,'wwpLeosPortTotalStatsTx64BytePkts':wwpLeosPortTotalStatsTx64BytePkts,'wwpLeosPortTotalStatsTx65To127BytePkts':wwpLeosPortTotalStatsTx65To127BytePkts,'wwpLeosPortTotalStatsTx128To255BytePkts':wwpLeosPortTotalStatsTx128To255BytePkts,'wwpLeosPortTotalStatsTx256To511BytePkts':wwpLeosPortTotalStatsTx256To511BytePkts,'wwpLeosPortTotalStatsTx512To1023BytePkts':wwpLeosPortTotalStatsTx512To1023BytePkts,'wwpLeosPortTotalStatsTx1024To1518BytePkts':wwpLeosPortTotalStatsTx1024To1518BytePkts,'wwpLeosPortTotalStatsTx1519To2047BytePkts':wwpLeosPortTotalStatsTx1519To2047BytePkts,'wwpLeosPortTotalStatsTx2048To4095BytePkts':wwpLeosPortTotalStatsTx2048To4095BytePkts,'wwpLeosPortTotalStatsTx4096To9216BytePkts':wwpLeosPortTotalStatsTx4096To9216BytePkts,'wwpLeosPortTotalStatsRxFpgaDropPkts':wwpLeosPortTotalStatsRxFpgaDropPkts,'wwpLeosPortTotalStatsPortLinkUp':wwpLeosPortTotalStatsPortLinkUp,'wwpLeosPortTotalStatsPortLinkDown':wwpLeosPortTotalStatsPortLinkDown,'wwpLeosPortTotalStatsPortLinkFlap':wwpLeosPortTotalStatsPortLinkFlap,'wwpLeosPortTotalStatsRxUcastPkts':wwpLeosPortTotalStatsRxUcastPkts,'wwpLeosPortTotalStatsTxUcastPkts':wwpLeosPortTotalStatsTxUcastPkts,'wwpLeosPortTotalStatsRxDropPkts':wwpLeosPortTotalStatsRxDropPkts,'wwpLeosPortTotalStatsRxDiscardPkts':wwpLeosPortTotalStatsRxDiscardPkts,'wwpLeosPortTotalStatsRxLOutRangePkts':wwpLeosPortTotalStatsRxLOutRangePkts,'wwpLeosPortTotalStatsRxFpgaBufferDropPkts':wwpLeosPortTotalStatsRxFpgaBufferDropPkts,'wwpLeosPortTotalStatsTxFpgaBufferDropPkts':wwpLeosPortTotalStatsTxFpgaBufferDropPkts,'wwpLeosPortTotalStatsFpgaVlanPriFilterDropPkts':wwpLeosPortTotalStatsFpgaVlanPriFilterDropPkts,'wwpLeosPortTotalStatsFpgaRxErrorPkts':wwpLeosPortTotalStatsFpgaRxErrorPkts,'wwpLeosPortTotalStatsFpgaRxCrcErrorPkts':wwpLeosPortTotalStatsFpgaRxCrcErrorPkts,'wwpLeosPortTotalStatsFpgaRxIpCrcErrorPkts':wwpLeosPortTotalStatsFpgaRxIpCrcErrorPkts,'wwpLeosPortTotalStatsRxInErrorPkts':wwpLeosPortTotalStatsRxInErrorPkts,'wwpLeosPortHCStatsTable':wwpLeosPortHCStatsTable,'wwpLeosPortHCStatsEntry':wwpLeosPortHCStatsEntry,_K:wwpLeosPortHCStatsPortId,'wwpLeosPortHCStatsRxBytes':wwpLeosPortHCStatsRxBytes,'wwpLeosPortHCStatsRxPkts':wwpLeosPortHCStatsRxPkts,'wwpLeosPortHCStatsRxCrcErrorPkts':wwpLeosPortHCStatsRxCrcErrorPkts,'wwpLeosPortHCStatsRxBcastPkts':wwpLeosPortHCStatsRxBcastPkts,'wwpLeosPortHCStatsUndersizePkts':wwpLeosPortHCStatsUndersizePkts,'wwpLeosPortHCStatsOversizePkts':wwpLeosPortHCStatsOversizePkts,'wwpLeosPortHCStatsFragmentPkts':wwpLeosPortHCStatsFragmentPkts,'wwpLeosPortHCStatsJabberPkts':wwpLeosPortHCStatsJabberPkts,'wwpLeosPortHCStats64BytePkts':wwpLeosPortHCStats64BytePkts,'wwpLeosPortHCStats65To127BytePkts':wwpLeosPortHCStats65To127BytePkts,'wwpLeosPortHCStats128To255BytePkts':wwpLeosPortHCStats128To255BytePkts,'wwpLeosPortHCStats256To511BytePkts':wwpLeosPortHCStats256To511BytePkts,'wwpLeosPortHCStats512To1023BytePkts':wwpLeosPortHCStats512To1023BytePkts,'wwpLeosPortHCStats1024To1518BytePkts':wwpLeosPortHCStats1024To1518BytePkts,'wwpLeosPortHCStatsTxBytes':wwpLeosPortHCStatsTxBytes,'wwpLeosPortHCStatsTxTBytes':wwpLeosPortHCStatsTxTBytes,'wwpLeosPortHCStatsTxPkts':wwpLeosPortHCStatsTxPkts,'wwpLeosPortHCStatsTxExDeferPkts':wwpLeosPortHCStatsTxExDeferPkts,'wwpLeosPortHCStatsTxGiantPkts':wwpLeosPortHCStatsTxGiantPkts,'wwpLeosPortHCStatsTxUnderRunPkts':wwpLeosPortHCStatsTxUnderRunPkts,'wwpLeosPortHCStatsTxCrcErrorPkts':wwpLeosPortHCStatsTxCrcErrorPkts,'wwpLeosPortHCStatsTxLCheckErrorPkts':wwpLeosPortHCStatsTxLCheckErrorPkts,'wwpLeosPortHCStatsTxLOutRangePkts':wwpLeosPortHCStatsTxLOutRangePkts,'wwpLeosPortHCStatsTxLateCollPkts':wwpLeosPortHCStatsTxLateCollPkts,'wwpLeosPortHCStatsTxExCollPkts':wwpLeosPortHCStatsTxExCollPkts,'wwpLeosPortHCStatsTxSingleCollPkts':wwpLeosPortHCStatsTxSingleCollPkts,'wwpLeosPortHCStatsTxCollPkts':wwpLeosPortHCStatsTxCollPkts,'wwpLeosPortHCStatsTxPausePkts':wwpLeosPortHCStatsTxPausePkts,'wwpLeosPortHCStatsTxMcastPkts':wwpLeosPortHCStatsTxMcastPkts,'wwpLeosPortHCStatsTxBcastPkts':wwpLeosPortHCStatsTxBcastPkts,'wwpLeosPortHCStatsPortReset':wwpLeosPortHCStatsPortReset,'wwpLeosPortHCStatsRxMcastPkts':wwpLeosPortHCStatsRxMcastPkts,'wwpLeosPortHCStatsRxPausePkts':wwpLeosPortHCStatsRxPausePkts,'wwpLeosPortHCStats1519To2047BytePkts':wwpLeosPortHCStats1519To2047BytePkts,'wwpLeosPortHCStats2048To4095BytePkts':wwpLeosPortHCStats2048To4095BytePkts,'wwpLeosPortHCStats4096To9216BytePkts':wwpLeosPortHCStats4096To9216BytePkts,'wwpLeosPortHCStatsTxDeferPkts':wwpLeosPortHCStatsTxDeferPkts,'wwpLeosPortHCStatsTx64BytePkts':wwpLeosPortHCStatsTx64BytePkts,'wwpLeosPortHCStatsTx65To127BytePkts':wwpLeosPortHCStatsTx65To127BytePkts,'wwpLeosPortHCStatsTx128To255BytePkts':wwpLeosPortHCStatsTx128To255BytePkts,'wwpLeosPortHCStatsTx256To511BytePkts':wwpLeosPortHCStatsTx256To511BytePkts,'wwpLeosPortHCStatsTx512To1023BytePkts':wwpLeosPortHCStatsTx512To1023BytePkts,'wwpLeosPortHCStatsTx1024To1518BytePkts':wwpLeosPortHCStatsTx1024To1518BytePkts,'wwpLeosPortHCStatsTx1519To2047BytePkts':wwpLeosPortHCStatsTx1519To2047BytePkts,'wwpLeosPortHCStatsTx2048To4095BytePkts':wwpLeosPortHCStatsTx2048To4095BytePkts,'wwpLeosPortHCStatsTx4096To9216BytePkts':wwpLeosPortHCStatsTx4096To9216BytePkts,'wwpLeosPortHCStatsRxUcastPkts':wwpLeosPortHCStatsRxUcastPkts,'wwpLeosPortHCStatsTxUcastPkts':wwpLeosPortHCStatsTxUcastPkts,'wwpLeosPortHCStatsRxDropPkts':wwpLeosPortHCStatsRxDropPkts,'wwpLeosPortHCStatsRxDiscardPkts':wwpLeosPortHCStatsRxDiscardPkts,'wwpLeosPortHCStatsRxLOutRangePkts':wwpLeosPortHCStatsRxLOutRangePkts,'wwpLeosPortHCStatsRxInErrorPkts':wwpLeosPortHCStatsRxInErrorPkts,'wwpLeosPortHCStatsLastRefresh':wwpLeosPortHCStatsLastRefresh,'wwpLeosPortHCStatsLastChange':wwpLeosPortHCStatsLastChange,'wwpLeosPortTotalHCStatsTable':wwpLeosPortTotalHCStatsTable,'wwpLeosPortTotalHCStatsEntry':wwpLeosPortTotalHCStatsEntry,_L:wwpLeosPortTotalHCStatsPortId,'wwpLeosPortTotalHCStatsRxBytes':wwpLeosPortTotalHCStatsRxBytes,'wwpLeosPortTotalHCStatsRxPkts':wwpLeosPortTotalHCStatsRxPkts,'wwpLeosPortTotalHCStatsRxCrcErrorPkts':wwpLeosPortTotalHCStatsRxCrcErrorPkts,'wwpLeosPortTotalHCStatsRxBcastPkts':wwpLeosPortTotalHCStatsRxBcastPkts,'wwpLeosPortTotalHCStatsUndersizePkts':wwpLeosPortTotalHCStatsUndersizePkts,'wwpLeosPortTotalHCStatsOversizePkts':wwpLeosPortTotalHCStatsOversizePkts,'wwpLeosPortTotalHCStatsFragmentPkts':wwpLeosPortTotalHCStatsFragmentPkts,'wwpLeosPortTotalHCStatsJabberPkts':wwpLeosPortTotalHCStatsJabberPkts,'wwpLeosPortTotalHCStats64BytePkts':wwpLeosPortTotalHCStats64BytePkts,'wwpLeosPortTotalHCStats65To127BytePkts':wwpLeosPortTotalHCStats65To127BytePkts,'wwpLeosPortTotalHCStats128To255BytePkts':wwpLeosPortTotalHCStats128To255BytePkts,'wwpLeosPortTotalHCStats256To511BytePkts':wwpLeosPortTotalHCStats256To511BytePkts,'wwpLeosPortTotalHCStats512To1023BytePkts':wwpLeosPortTotalHCStats512To1023BytePkts,'wwpLeosPortTotalHCStats1024To1518BytePkts':wwpLeosPortTotalHCStats1024To1518BytePkts,'wwpLeosPortTotalHCStatsTxBytes':wwpLeosPortTotalHCStatsTxBytes,'wwpLeosPortTotalHCStatsTxTBytes':wwpLeosPortTotalHCStatsTxTBytes,'wwpLeosPortTotalHCStatsTxPkts':wwpLeosPortTotalHCStatsTxPkts,'wwpLeosPortTotalHCStatsTxExDeferPkts':wwpLeosPortTotalHCStatsTxExDeferPkts,'wwpLeosPortTotalHCStatsTxGiantPkts':wwpLeosPortTotalHCStatsTxGiantPkts,'wwpLeosPortTotalHCStatsTxUnderRunPkts':wwpLeosPortTotalHCStatsTxUnderRunPkts,'wwpLeosPortTotalHCStatsTxCrcErrorPkts':wwpLeosPortTotalHCStatsTxCrcErrorPkts,'wwpLeosPortTotalHCStatsTxLCheckErrorPkts':wwpLeosPortTotalHCStatsTxLCheckErrorPkts,'wwpLeosPortTotalHCStatsTxLOutRangePkts':wwpLeosPortTotalHCStatsTxLOutRangePkts,'wwpLeosPortTotalHCStatsTxLateCollPkts':wwpLeosPortTotalHCStatsTxLateCollPkts,'wwpLeosPortTotalHCStatsTxExCollPkts':wwpLeosPortTotalHCStatsTxExCollPkts,'wwpLeosPortTotalHCStatsTxSingleCollPkts':wwpLeosPortTotalHCStatsTxSingleCollPkts,'wwpLeosPortTotalHCStatsTxCollPkts':wwpLeosPortTotalHCStatsTxCollPkts,'wwpLeosPortTotalHCStatsTxPausePkts':wwpLeosPortTotalHCStatsTxPausePkts,'wwpLeosPortTotalHCStatsTxMcastPkts':wwpLeosPortTotalHCStatsTxMcastPkts,'wwpLeosPortTotalHCStatsTxBcastPkts':wwpLeosPortTotalHCStatsTxBcastPkts,'wwpLeosPortTotalHCStatsPortReset':wwpLeosPortTotalHCStatsPortReset,'wwpLeosPortTotalHCStatsRxMcastPkts':wwpLeosPortTotalHCStatsRxMcastPkts,'wwpLeosPortTotalHCStatsRxPausePkts':wwpLeosPortTotalHCStatsRxPausePkts,'wwpLeosPortTotalHCStats1519To2047BytePkts':wwpLeosPortTotalHCStats1519To2047BytePkts,'wwpLeosPortTotalHCStats2048To4095BytePkts':wwpLeosPortTotalHCStats2048To4095BytePkts,'wwpLeosPortTotalHCStats4096To9216BytePkts':wwpLeosPortTotalHCStats4096To9216BytePkts,'wwpLeosPortTotalHCStatsTxDeferPkts':wwpLeosPortTotalHCStatsTxDeferPkts,'wwpLeosPortTotalHCStatsTx64BytePkts':wwpLeosPortTotalHCStatsTx64BytePkts,'wwpLeosPortTotalHCStatsTx65To127BytePkts':wwpLeosPortTotalHCStatsTx65To127BytePkts,'wwpLeosPortTotalHCStatsTx128To255BytePkts':wwpLeosPortTotalHCStatsTx128To255BytePkts,'wwpLeosPortTotalHCStatsTx256To511BytePkts':wwpLeosPortTotalHCStatsTx256To511BytePkts,'wwpLeosPortTotalHCStatsTx512To1023BytePkts':wwpLeosPortTotalHCStatsTx512To1023BytePkts,'wwpLeosPortTotalHCStatsTx1024To1518BytePkts':wwpLeosPortTotalHCStatsTx1024To1518BytePkts,'wwpLeosPortTotalHCStatsTx1519To2047BytePkts':wwpLeosPortTotalHCStatsTx1519To2047BytePkts,'wwpLeosPortTotalHCStatsTx2048To4095BytePkts':wwpLeosPortTotalHCStatsTx2048To4095BytePkts,'wwpLeosPortTotalHCStatsTx4096To9216BytePkts':wwpLeosPortTotalHCStatsTx4096To9216BytePkts,'wwpLeosPortTotalHCStatsRxUcastPkts':wwpLeosPortTotalHCStatsRxUcastPkts,'wwpLeosPortTotalHCStatsTxUcastPkts':wwpLeosPortTotalHCStatsTxUcastPkts,'wwpLeosPortTotalHCStatsRxDropPkts':wwpLeosPortTotalHCStatsRxDropPkts,'wwpLeosPortTotalHCStatsRxDiscardPkts':wwpLeosPortTotalHCStatsRxDiscardPkts,'wwpLeosPortTotalHCStatsRxLOutRangePkts':wwpLeosPortTotalHCStatsRxLOutRangePkts,'wwpLeosPortTotalHCStatsRxInErrorPkts':wwpLeosPortTotalHCStatsRxInErrorPkts,'wwpLeosPortTotalHCStatsLastRefresh':wwpLeosPortTotalHCStatsLastRefresh,'wwpLeosPortTotalHCStatsLastChange':wwpLeosPortTotalHCStatsLastChange,'wwpLeosPortStatsMIBNotificationPrefix':wwpLeosPortStatsMIBNotificationPrefix,'wwpLeosPortStatsMIBNotifications':wwpLeosPortStatsMIBNotifications,'wwpLeosPortStatsMIBConformance':wwpLeosPortStatsMIBConformance,'wwpLeosPortStatsMIBCompliances':wwpLeosPortStatsMIBCompliances,'wwpLeosPortStatsMIBGroups':wwpLeosPortStatsMIBGroups})