_F='wwpPortStatsPortalPortId'
_E='wwpPortStatsPortId'
_D='WWP-PORT-STATS-MIB'
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
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpPortStatsMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,16))
if mibBuilder.loadTexts:wwpPortStatsMIB.setRevisions(('2001-04-03 17:00',))
_WwpPortStatsMIBObjects_ObjectIdentity=ObjectIdentity
wwpPortStatsMIBObjects=_WwpPortStatsMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,16,1))
_WwpPortStats_ObjectIdentity=ObjectIdentity
wwpPortStats=_WwpPortStats_ObjectIdentity((1,3,6,1,4,1,6141,2,16,1,1))
class _WwpPortStatsReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('reset',1)))
_WwpPortStatsReset_Type.__name__=_C
_WwpPortStatsReset_Object=MibScalar
wwpPortStatsReset=_WwpPortStatsReset_Object((1,3,6,1,4,1,6141,2,16,1,1,1),_WwpPortStatsReset_Type())
wwpPortStatsReset.setMaxAccess('read-write')
if mibBuilder.loadTexts:wwpPortStatsReset.setStatus('deprecated')
_WwpPortStatsTable_Object=MibTable
wwpPortStatsTable=_WwpPortStatsTable_Object((1,3,6,1,4,1,6141,2,16,1,1,2))
if mibBuilder.loadTexts:wwpPortStatsTable.setStatus(_A)
_WwpPortStatsEntry_Object=MibTableRow
wwpPortStatsEntry=_WwpPortStatsEntry_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1))
wwpPortStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:wwpPortStatsEntry.setStatus(_A)
class _WwpPortStatsPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpPortStatsPortId_Type.__name__=_C
_WwpPortStatsPortId_Object=MibTableColumn
wwpPortStatsPortId=_WwpPortStatsPortId_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,1),_WwpPortStatsPortId_Type())
wwpPortStatsPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortId.setStatus(_A)
_WwpPortStatsRxBytes_Type=Counter32
_WwpPortStatsRxBytes_Object=MibTableColumn
wwpPortStatsRxBytes=_WwpPortStatsRxBytes_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,2),_WwpPortStatsRxBytes_Type())
wwpPortStatsRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsRxBytes.setStatus(_A)
_WwpPortStatsRxPkts_Type=Counter32
_WwpPortStatsRxPkts_Object=MibTableColumn
wwpPortStatsRxPkts=_WwpPortStatsRxPkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,3),_WwpPortStatsRxPkts_Type())
wwpPortStatsRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsRxPkts.setStatus(_A)
_WwpPortStatsRxCrcErrorPkts_Type=Counter32
_WwpPortStatsRxCrcErrorPkts_Object=MibTableColumn
wwpPortStatsRxCrcErrorPkts=_WwpPortStatsRxCrcErrorPkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,4),_WwpPortStatsRxCrcErrorPkts_Type())
wwpPortStatsRxCrcErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsRxCrcErrorPkts.setStatus(_A)
_WwpPortStatsRxBcastPkts_Type=Counter32
_WwpPortStatsRxBcastPkts_Object=MibTableColumn
wwpPortStatsRxBcastPkts=_WwpPortStatsRxBcastPkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,5),_WwpPortStatsRxBcastPkts_Type())
wwpPortStatsRxBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsRxBcastPkts.setStatus(_A)
_WwpPortStatsUndersizePkts_Type=Counter32
_WwpPortStatsUndersizePkts_Object=MibTableColumn
wwpPortStatsUndersizePkts=_WwpPortStatsUndersizePkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,6),_WwpPortStatsUndersizePkts_Type())
wwpPortStatsUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsUndersizePkts.setStatus(_A)
_WwpPortStatsOversizePkts_Type=Counter32
_WwpPortStatsOversizePkts_Object=MibTableColumn
wwpPortStatsOversizePkts=_WwpPortStatsOversizePkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,7),_WwpPortStatsOversizePkts_Type())
wwpPortStatsOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsOversizePkts.setStatus(_A)
_WwpPortStatsFragmentPkts_Type=Counter32
_WwpPortStatsFragmentPkts_Object=MibTableColumn
wwpPortStatsFragmentPkts=_WwpPortStatsFragmentPkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,8),_WwpPortStatsFragmentPkts_Type())
wwpPortStatsFragmentPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsFragmentPkts.setStatus(_A)
_WwpPortStatsJabberPkts_Type=Counter32
_WwpPortStatsJabberPkts_Object=MibTableColumn
wwpPortStatsJabberPkts=_WwpPortStatsJabberPkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,9),_WwpPortStatsJabberPkts_Type())
wwpPortStatsJabberPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsJabberPkts.setStatus(_A)
_WwpPortStats64BytePkts_Type=Counter32
_WwpPortStats64BytePkts_Object=MibTableColumn
wwpPortStats64BytePkts=_WwpPortStats64BytePkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,10),_WwpPortStats64BytePkts_Type())
wwpPortStats64BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStats64BytePkts.setStatus(_A)
_WwpPortStats65To127BytePkts_Type=Counter32
_WwpPortStats65To127BytePkts_Object=MibTableColumn
wwpPortStats65To127BytePkts=_WwpPortStats65To127BytePkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,11),_WwpPortStats65To127BytePkts_Type())
wwpPortStats65To127BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStats65To127BytePkts.setStatus(_A)
_WwpPortStats128To255BytePkts_Type=Counter32
_WwpPortStats128To255BytePkts_Object=MibTableColumn
wwpPortStats128To255BytePkts=_WwpPortStats128To255BytePkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,12),_WwpPortStats128To255BytePkts_Type())
wwpPortStats128To255BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStats128To255BytePkts.setStatus(_A)
_WwpPortStats256To511BytePkts_Type=Counter32
_WwpPortStats256To511BytePkts_Object=MibTableColumn
wwpPortStats256To511BytePkts=_WwpPortStats256To511BytePkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,13),_WwpPortStats256To511BytePkts_Type())
wwpPortStats256To511BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStats256To511BytePkts.setStatus(_A)
_WwpPortStats512To1023BytePkts_Type=Counter32
_WwpPortStats512To1023BytePkts_Object=MibTableColumn
wwpPortStats512To1023BytePkts=_WwpPortStats512To1023BytePkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,14),_WwpPortStats512To1023BytePkts_Type())
wwpPortStats512To1023BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStats512To1023BytePkts.setStatus(_A)
_WwpPortStats1024To1518BytePkts_Type=Counter32
_WwpPortStats1024To1518BytePkts_Object=MibTableColumn
wwpPortStats1024To1518BytePkts=_WwpPortStats1024To1518BytePkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,15),_WwpPortStats1024To1518BytePkts_Type())
wwpPortStats1024To1518BytePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStats1024To1518BytePkts.setStatus(_A)
_WwpPortStatsTxBytes_Type=Counter32
_WwpPortStatsTxBytes_Object=MibTableColumn
wwpPortStatsTxBytes=_WwpPortStatsTxBytes_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,16),_WwpPortStatsTxBytes_Type())
wwpPortStatsTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsTxBytes.setStatus(_A)
_WwpPortStatsTxTBytes_Type=Counter32
_WwpPortStatsTxTBytes_Object=MibTableColumn
wwpPortStatsTxTBytes=_WwpPortStatsTxTBytes_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,17),_WwpPortStatsTxTBytes_Type())
wwpPortStatsTxTBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsTxTBytes.setStatus(_A)
_WwpPortStatsTxPkts_Type=Counter32
_WwpPortStatsTxPkts_Object=MibTableColumn
wwpPortStatsTxPkts=_WwpPortStatsTxPkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,18),_WwpPortStatsTxPkts_Type())
wwpPortStatsTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsTxPkts.setStatus(_A)
_WwpPortStatsTxExDeferPkts_Type=Counter32
_WwpPortStatsTxExDeferPkts_Object=MibTableColumn
wwpPortStatsTxExDeferPkts=_WwpPortStatsTxExDeferPkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,19),_WwpPortStatsTxExDeferPkts_Type())
wwpPortStatsTxExDeferPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsTxExDeferPkts.setStatus(_A)
_WwpPortStatsTxGiantPkts_Type=Counter32
_WwpPortStatsTxGiantPkts_Object=MibTableColumn
wwpPortStatsTxGiantPkts=_WwpPortStatsTxGiantPkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,20),_WwpPortStatsTxGiantPkts_Type())
wwpPortStatsTxGiantPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsTxGiantPkts.setStatus(_A)
_WwpPortStatsTxUnderRunPkts_Type=Counter32
_WwpPortStatsTxUnderRunPkts_Object=MibTableColumn
wwpPortStatsTxUnderRunPkts=_WwpPortStatsTxUnderRunPkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,21),_WwpPortStatsTxUnderRunPkts_Type())
wwpPortStatsTxUnderRunPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsTxUnderRunPkts.setStatus(_A)
_WwpPortStatsTxCrcErrorPkts_Type=Counter32
_WwpPortStatsTxCrcErrorPkts_Object=MibTableColumn
wwpPortStatsTxCrcErrorPkts=_WwpPortStatsTxCrcErrorPkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,22),_WwpPortStatsTxCrcErrorPkts_Type())
wwpPortStatsTxCrcErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsTxCrcErrorPkts.setStatus(_A)
_WwpPortStatsTxLCheckErrorPkts_Type=Counter32
_WwpPortStatsTxLCheckErrorPkts_Object=MibTableColumn
wwpPortStatsTxLCheckErrorPkts=_WwpPortStatsTxLCheckErrorPkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,23),_WwpPortStatsTxLCheckErrorPkts_Type())
wwpPortStatsTxLCheckErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsTxLCheckErrorPkts.setStatus(_A)
_WwpPortStatsTxLOutRangePkts_Type=Counter32
_WwpPortStatsTxLOutRangePkts_Object=MibTableColumn
wwpPortStatsTxLOutRangePkts=_WwpPortStatsTxLOutRangePkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,24),_WwpPortStatsTxLOutRangePkts_Type())
wwpPortStatsTxLOutRangePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsTxLOutRangePkts.setStatus(_A)
_WwpPortStatsTxLateCollPkts_Type=Counter32
_WwpPortStatsTxLateCollPkts_Object=MibTableColumn
wwpPortStatsTxLateCollPkts=_WwpPortStatsTxLateCollPkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,25),_WwpPortStatsTxLateCollPkts_Type())
wwpPortStatsTxLateCollPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsTxLateCollPkts.setStatus(_A)
_WwpPortStatsTxExCollPkts_Type=Counter32
_WwpPortStatsTxExCollPkts_Object=MibTableColumn
wwpPortStatsTxExCollPkts=_WwpPortStatsTxExCollPkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,26),_WwpPortStatsTxExCollPkts_Type())
wwpPortStatsTxExCollPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsTxExCollPkts.setStatus(_A)
_WwpPortStatsTxSingleCollPkts_Type=Counter32
_WwpPortStatsTxSingleCollPkts_Object=MibTableColumn
wwpPortStatsTxSingleCollPkts=_WwpPortStatsTxSingleCollPkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,27),_WwpPortStatsTxSingleCollPkts_Type())
wwpPortStatsTxSingleCollPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsTxSingleCollPkts.setStatus(_A)
_WwpPortStatsTxCollPkts_Type=Counter32
_WwpPortStatsTxCollPkts_Object=MibTableColumn
wwpPortStatsTxCollPkts=_WwpPortStatsTxCollPkts_Object((1,3,6,1,4,1,6141,2,16,1,1,2,1,28),_WwpPortStatsTxCollPkts_Type())
wwpPortStatsTxCollPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsTxCollPkts.setStatus(_A)
_WwpPortStatsXTable_Object=MibTable
wwpPortStatsXTable=_WwpPortStatsXTable_Object((1,3,6,1,4,1,6141,2,16,1,1,3))
if mibBuilder.loadTexts:wwpPortStatsXTable.setStatus(_A)
_WwpPortStatsXEntry_Object=MibTableRow
wwpPortStatsXEntry=_WwpPortStatsXEntry_Object((1,3,6,1,4,1,6141,2,16,1,1,3,1))
wwpPortStatsXEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:wwpPortStatsXEntry.setStatus(_A)
_WwpPortStatsXRxBytes_Type=Counter64
_WwpPortStatsXRxBytes_Object=MibTableColumn
wwpPortStatsXRxBytes=_WwpPortStatsXRxBytes_Object((1,3,6,1,4,1,6141,2,16,1,1,3,1,1),_WwpPortStatsXRxBytes_Type())
wwpPortStatsXRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsXRxBytes.setStatus(_A)
_WwpPortStatsXRxPkts_Type=Counter64
_WwpPortStatsXRxPkts_Object=MibTableColumn
wwpPortStatsXRxPkts=_WwpPortStatsXRxPkts_Object((1,3,6,1,4,1,6141,2,16,1,1,3,1,2),_WwpPortStatsXRxPkts_Type())
wwpPortStatsXRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsXRxPkts.setStatus(_A)
_WwpPortStatsXTxBytes_Type=Counter64
_WwpPortStatsXTxBytes_Object=MibTableColumn
wwpPortStatsXTxBytes=_WwpPortStatsXTxBytes_Object((1,3,6,1,4,1,6141,2,16,1,1,3,1,3),_WwpPortStatsXTxBytes_Type())
wwpPortStatsXTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsXTxBytes.setStatus(_A)
_WwpPortStatsXTxPkts_Type=Counter64
_WwpPortStatsXTxPkts_Object=MibTableColumn
wwpPortStatsXTxPkts=_WwpPortStatsXTxPkts_Object((1,3,6,1,4,1,6141,2,16,1,1,3,1,4),_WwpPortStatsXTxPkts_Type())
wwpPortStatsXTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsXTxPkts.setStatus(_A)
_WwpPortStatsPortalTable_Object=MibTable
wwpPortStatsPortalTable=_WwpPortStatsPortalTable_Object((1,3,6,1,4,1,6141,2,16,1,1,4))
if mibBuilder.loadTexts:wwpPortStatsPortalTable.setStatus(_A)
_WwpPortStatsPortalEntry_Object=MibTableRow
wwpPortStatsPortalEntry=_WwpPortStatsPortalEntry_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1))
wwpPortStatsPortalEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:wwpPortStatsPortalEntry.setStatus(_A)
class _WwpPortStatsPortalPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpPortStatsPortalPortId_Type.__name__=_C
_WwpPortStatsPortalPortId_Object=MibTableColumn
wwpPortStatsPortalPortId=_WwpPortStatsPortalPortId_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,1),_WwpPortStatsPortalPortId_Type())
wwpPortStatsPortalPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalPortId.setStatus(_A)
_WwpPortStatsPortalBytesSentHi_Type=Counter32
_WwpPortStatsPortalBytesSentHi_Object=MibTableColumn
wwpPortStatsPortalBytesSentHi=_WwpPortStatsPortalBytesSentHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,2),_WwpPortStatsPortalBytesSentHi_Type())
wwpPortStatsPortalBytesSentHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalBytesSentHi.setStatus(_A)
_WwpPortStatsPortalBytesSentLo_Type=Counter32
_WwpPortStatsPortalBytesSentLo_Object=MibTableColumn
wwpPortStatsPortalBytesSentLo=_WwpPortStatsPortalBytesSentLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,3),_WwpPortStatsPortalBytesSentLo_Type())
wwpPortStatsPortalBytesSentLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalBytesSentLo.setStatus(_A)
_WwpPortStatsPortalFlowControlHi_Type=Counter32
_WwpPortStatsPortalFlowControlHi_Object=MibTableColumn
wwpPortStatsPortalFlowControlHi=_WwpPortStatsPortalFlowControlHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,4),_WwpPortStatsPortalFlowControlHi_Type())
wwpPortStatsPortalFlowControlHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalFlowControlHi.setStatus(_A)
_WwpPortStatsPortalFlowControlLo_Type=Counter32
_WwpPortStatsPortalFlowControlLo_Object=MibTableColumn
wwpPortStatsPortalFlowControlLo=_WwpPortStatsPortalFlowControlLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,5),_WwpPortStatsPortalFlowControlLo_Type())
wwpPortStatsPortalFlowControlLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalFlowControlLo.setStatus(_A)
_WwpPortStatsPortalUnicastFramesSentHi_Type=Counter32
_WwpPortStatsPortalUnicastFramesSentHi_Object=MibTableColumn
wwpPortStatsPortalUnicastFramesSentHi=_WwpPortStatsPortalUnicastFramesSentHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,6),_WwpPortStatsPortalUnicastFramesSentHi_Type())
wwpPortStatsPortalUnicastFramesSentHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalUnicastFramesSentHi.setStatus(_A)
_WwpPortStatsPortalUnicastFramesSentLo_Type=Counter32
_WwpPortStatsPortalUnicastFramesSentLo_Object=MibTableColumn
wwpPortStatsPortalUnicastFramesSentLo=_WwpPortStatsPortalUnicastFramesSentLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,7),_WwpPortStatsPortalUnicastFramesSentLo_Type())
wwpPortStatsPortalUnicastFramesSentLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalUnicastFramesSentLo.setStatus(_A)
_WwpPortStatsPortalAlignmentErrorHi_Type=Counter32
_WwpPortStatsPortalAlignmentErrorHi_Object=MibTableColumn
wwpPortStatsPortalAlignmentErrorHi=_WwpPortStatsPortalAlignmentErrorHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,8),_WwpPortStatsPortalAlignmentErrorHi_Type())
wwpPortStatsPortalAlignmentErrorHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalAlignmentErrorHi.setStatus(_A)
_WwpPortStatsPortalAlignmentErrorLo_Type=Counter32
_WwpPortStatsPortalAlignmentErrorLo_Object=MibTableColumn
wwpPortStatsPortalAlignmentErrorLo=_WwpPortStatsPortalAlignmentErrorLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,9),_WwpPortStatsPortalAlignmentErrorLo_Type())
wwpPortStatsPortalAlignmentErrorLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalAlignmentErrorLo.setStatus(_A)
_WwpPortStatsPortalNonUnicastFramesSentHi_Type=Counter32
_WwpPortStatsPortalNonUnicastFramesSentHi_Object=MibTableColumn
wwpPortStatsPortalNonUnicastFramesSentHi=_WwpPortStatsPortalNonUnicastFramesSentHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,10),_WwpPortStatsPortalNonUnicastFramesSentHi_Type())
wwpPortStatsPortalNonUnicastFramesSentHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalNonUnicastFramesSentHi.setStatus(_A)
_WwpPortStatsPortalNonUnicastFramesSentLo_Type=Counter32
_WwpPortStatsPortalNonUnicastFramesSentLo_Object=MibTableColumn
wwpPortStatsPortalNonUnicastFramesSentLo=_WwpPortStatsPortalNonUnicastFramesSentLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,11),_WwpPortStatsPortalNonUnicastFramesSentLo_Type())
wwpPortStatsPortalNonUnicastFramesSentLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalNonUnicastFramesSentLo.setStatus(_A)
_WwpPortStatsPortalTotalBytesRecievedHi_Type=Counter32
_WwpPortStatsPortalTotalBytesRecievedHi_Object=MibTableColumn
wwpPortStatsPortalTotalBytesRecievedHi=_WwpPortStatsPortalTotalBytesRecievedHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,12),_WwpPortStatsPortalTotalBytesRecievedHi_Type())
wwpPortStatsPortalTotalBytesRecievedHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalTotalBytesRecievedHi.setStatus(_A)
_WwpPortStatsPortalTotalBytesRecievedLo_Type=Counter32
_WwpPortStatsPortalTotalBytesRecievedLo_Object=MibTableColumn
wwpPortStatsPortalTotalBytesRecievedLo=_WwpPortStatsPortalTotalBytesRecievedLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,13),_WwpPortStatsPortalTotalBytesRecievedLo_Type())
wwpPortStatsPortalTotalBytesRecievedLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalTotalBytesRecievedLo.setStatus(_A)
_WwpPortStatsPortalFlowControlFramesRecievedHi_Type=Counter32
_WwpPortStatsPortalFlowControlFramesRecievedHi_Object=MibTableColumn
wwpPortStatsPortalFlowControlFramesRecievedHi=_WwpPortStatsPortalFlowControlFramesRecievedHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,14),_WwpPortStatsPortalFlowControlFramesRecievedHi_Type())
wwpPortStatsPortalFlowControlFramesRecievedHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalFlowControlFramesRecievedHi.setStatus(_A)
_WwpPortStatsPortalFlowControlFramesRecievedLo_Type=Counter32
_WwpPortStatsPortalFlowControlFramesRecievedLo_Object=MibTableColumn
wwpPortStatsPortalFlowControlFramesRecievedLo=_WwpPortStatsPortalFlowControlFramesRecievedLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,15),_WwpPortStatsPortalFlowControlFramesRecievedLo_Type())
wwpPortStatsPortalFlowControlFramesRecievedLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalFlowControlFramesRecievedLo.setStatus(_A)
_WwpPortStatsPortalTotalFramesRecievedHi_Type=Counter32
_WwpPortStatsPortalTotalFramesRecievedHi_Object=MibTableColumn
wwpPortStatsPortalTotalFramesRecievedHi=_WwpPortStatsPortalTotalFramesRecievedHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,16),_WwpPortStatsPortalTotalFramesRecievedHi_Type())
wwpPortStatsPortalTotalFramesRecievedHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalTotalFramesRecievedHi.setStatus(_A)
_WwpPortStatsPortalTotalFramesRecievedLo_Type=Counter32
_WwpPortStatsPortalTotalFramesRecievedLo_Object=MibTableColumn
wwpPortStatsPortalTotalFramesRecievedLo=_WwpPortStatsPortalTotalFramesRecievedLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,17),_WwpPortStatsPortalTotalFramesRecievedLo_Type())
wwpPortStatsPortalTotalFramesRecievedLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalTotalFramesRecievedLo.setStatus(_A)
_WwpPortStatsPortalBroadcastFramesRecievedHi_Type=Counter32
_WwpPortStatsPortalBroadcastFramesRecievedHi_Object=MibTableColumn
wwpPortStatsPortalBroadcastFramesRecievedHi=_WwpPortStatsPortalBroadcastFramesRecievedHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,18),_WwpPortStatsPortalBroadcastFramesRecievedHi_Type())
wwpPortStatsPortalBroadcastFramesRecievedHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalBroadcastFramesRecievedHi.setStatus(_A)
_WwpPortStatsPortalBroadcastFramesRecievedLo_Type=Counter32
_WwpPortStatsPortalBroadcastFramesRecievedLo_Object=MibTableColumn
wwpPortStatsPortalBroadcastFramesRecievedLo=_WwpPortStatsPortalBroadcastFramesRecievedLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,19),_WwpPortStatsPortalBroadcastFramesRecievedLo_Type())
wwpPortStatsPortalBroadcastFramesRecievedLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalBroadcastFramesRecievedLo.setStatus(_A)
_WwpPortStatsPortalMulticastFramesRecievedHi_Type=Counter32
_WwpPortStatsPortalMulticastFramesRecievedHi_Object=MibTableColumn
wwpPortStatsPortalMulticastFramesRecievedHi=_WwpPortStatsPortalMulticastFramesRecievedHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,20),_WwpPortStatsPortalMulticastFramesRecievedHi_Type())
wwpPortStatsPortalMulticastFramesRecievedHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalMulticastFramesRecievedHi.setStatus(_A)
_WwpPortStatsPortalMulticastFramesRecievedLo_Type=Counter32
_WwpPortStatsPortalMulticastFramesRecievedLo_Object=MibTableColumn
wwpPortStatsPortalMulticastFramesRecievedLo=_WwpPortStatsPortalMulticastFramesRecievedLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,21),_WwpPortStatsPortalMulticastFramesRecievedLo_Type())
wwpPortStatsPortalMulticastFramesRecievedLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalMulticastFramesRecievedLo.setStatus(_A)
_WwpPortStatsPortalJabberFramesHi_Type=Counter32
_WwpPortStatsPortalJabberFramesHi_Object=MibTableColumn
wwpPortStatsPortalJabberFramesHi=_WwpPortStatsPortalJabberFramesHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,22),_WwpPortStatsPortalJabberFramesHi_Type())
wwpPortStatsPortalJabberFramesHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalJabberFramesHi.setStatus(_A)
_WwpPortStatsPortalJabberFramesLo_Type=Counter32
_WwpPortStatsPortalJabberFramesLo_Object=MibTableColumn
wwpPortStatsPortalJabberFramesLo=_WwpPortStatsPortalJabberFramesLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,23),_WwpPortStatsPortalJabberFramesLo_Type())
wwpPortStatsPortalJabberFramesLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalJabberFramesLo.setStatus(_A)
_WwpPortStatsPortal64ByteFramesHi_Type=Counter32
_WwpPortStatsPortal64ByteFramesHi_Object=MibTableColumn
wwpPortStatsPortal64ByteFramesHi=_WwpPortStatsPortal64ByteFramesHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,24),_WwpPortStatsPortal64ByteFramesHi_Type())
wwpPortStatsPortal64ByteFramesHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortal64ByteFramesHi.setStatus(_A)
_WwpPortStatsPortal64ByteFramesLo_Type=Counter32
_WwpPortStatsPortal64ByteFramesLo_Object=MibTableColumn
wwpPortStatsPortal64ByteFramesLo=_WwpPortStatsPortal64ByteFramesLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,25),_WwpPortStatsPortal64ByteFramesLo_Type())
wwpPortStatsPortal64ByteFramesLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortal64ByteFramesLo.setStatus(_A)
_WwpPortStatsPortalOversizeFramesHi_Type=Counter32
_WwpPortStatsPortalOversizeFramesHi_Object=MibTableColumn
wwpPortStatsPortalOversizeFramesHi=_WwpPortStatsPortalOversizeFramesHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,26),_WwpPortStatsPortalOversizeFramesHi_Type())
wwpPortStatsPortalOversizeFramesHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalOversizeFramesHi.setStatus(_A)
_WwpPortStatsPortalOversizeFramesLo_Type=Counter32
_WwpPortStatsPortalOversizeFramesLo_Object=MibTableColumn
wwpPortStatsPortalOversizeFramesLo=_WwpPortStatsPortalOversizeFramesLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,27),_WwpPortStatsPortalOversizeFramesLo_Type())
wwpPortStatsPortalOversizeFramesLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalOversizeFramesLo.setStatus(_A)
_WwpPortStatsPortal65To127ByteFramesHi_Type=Counter32
_WwpPortStatsPortal65To127ByteFramesHi_Object=MibTableColumn
wwpPortStatsPortal65To127ByteFramesHi=_WwpPortStatsPortal65To127ByteFramesHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,28),_WwpPortStatsPortal65To127ByteFramesHi_Type())
wwpPortStatsPortal65To127ByteFramesHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortal65To127ByteFramesHi.setStatus(_A)
_WwpPortStatsPortal65To127ByteFramesLo_Type=Counter32
_WwpPortStatsPortal65To127ByteFramesLo_Object=MibTableColumn
wwpPortStatsPortal65To127ByteFramesLo=_WwpPortStatsPortal65To127ByteFramesLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,29),_WwpPortStatsPortal65To127ByteFramesLo_Type())
wwpPortStatsPortal65To127ByteFramesLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortal65To127ByteFramesLo.setStatus(_A)
_WwpPortStatsPortal256To511ByteFramesHi_Type=Counter32
_WwpPortStatsPortal256To511ByteFramesHi_Object=MibTableColumn
wwpPortStatsPortal256To511ByteFramesHi=_WwpPortStatsPortal256To511ByteFramesHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,30),_WwpPortStatsPortal256To511ByteFramesHi_Type())
wwpPortStatsPortal256To511ByteFramesHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortal256To511ByteFramesHi.setStatus(_A)
_WwpPortStatsPortal256To511ByteFramesLo_Type=Counter32
_WwpPortStatsPortal256To511ByteFramesLo_Object=MibTableColumn
wwpPortStatsPortal256To511ByteFramesLo=_WwpPortStatsPortal256To511ByteFramesLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,31),_WwpPortStatsPortal256To511ByteFramesLo_Type())
wwpPortStatsPortal256To511ByteFramesLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortal256To511ByteFramesLo.setStatus(_A)
_WwpPortStatsPortal128To255ByteFramesHi_Type=Counter32
_WwpPortStatsPortal128To255ByteFramesHi_Object=MibTableColumn
wwpPortStatsPortal128To255ByteFramesHi=_WwpPortStatsPortal128To255ByteFramesHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,32),_WwpPortStatsPortal128To255ByteFramesHi_Type())
wwpPortStatsPortal128To255ByteFramesHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortal128To255ByteFramesHi.setStatus(_A)
_WwpPortStatsPortal128To255ByteFramesLo_Type=Counter32
_WwpPortStatsPortal128To255ByteFramesLo_Object=MibTableColumn
wwpPortStatsPortal128To255ByteFramesLo=_WwpPortStatsPortal128To255ByteFramesLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,33),_WwpPortStatsPortal128To255ByteFramesLo_Type())
wwpPortStatsPortal128To255ByteFramesLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortal128To255ByteFramesLo.setStatus(_A)
_WwpPortStatsPortal1024To1528ByteFramesHi_Type=Counter32
_WwpPortStatsPortal1024To1528ByteFramesHi_Object=MibTableColumn
wwpPortStatsPortal1024To1528ByteFramesHi=_WwpPortStatsPortal1024To1528ByteFramesHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,34),_WwpPortStatsPortal1024To1528ByteFramesHi_Type())
wwpPortStatsPortal1024To1528ByteFramesHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortal1024To1528ByteFramesHi.setStatus(_A)
_WwpPortStatsPortal1024To1528ByteFramesLo_Type=Counter32
_WwpPortStatsPortal1024To1528ByteFramesLo_Object=MibTableColumn
wwpPortStatsPortal1024To1528ByteFramesLo=_WwpPortStatsPortal1024To1528ByteFramesLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,35),_WwpPortStatsPortal1024To1528ByteFramesLo_Type())
wwpPortStatsPortal1024To1528ByteFramesLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortal1024To1528ByteFramesLo.setStatus(_A)
_WwpPortStatsPortal512To1023ByteFramesHi_Type=Counter32
_WwpPortStatsPortal512To1023ByteFramesHi_Object=MibTableColumn
wwpPortStatsPortal512To1023ByteFramesHi=_WwpPortStatsPortal512To1023ByteFramesHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,36),_WwpPortStatsPortal512To1023ByteFramesHi_Type())
wwpPortStatsPortal512To1023ByteFramesHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortal512To1023ByteFramesHi.setStatus(_A)
_WwpPortStatsPortal512To1023ByteFrameslo_Type=Counter32
_WwpPortStatsPortal512To1023ByteFrameslo_Object=MibTableColumn
wwpPortStatsPortal512To1023ByteFrameslo=_WwpPortStatsPortal512To1023ByteFrameslo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,37),_WwpPortStatsPortal512To1023ByteFrameslo_Type())
wwpPortStatsPortal512To1023ByteFrameslo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortal512To1023ByteFrameslo.setStatus(_A)
_WwpPortStatsPortalFragmentHi_Type=Counter32
_WwpPortStatsPortalFragmentHi_Object=MibTableColumn
wwpPortStatsPortalFragmentHi=_WwpPortStatsPortalFragmentHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,38),_WwpPortStatsPortalFragmentHi_Type())
wwpPortStatsPortalFragmentHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalFragmentHi.setStatus(_A)
_WwpPortStatsPortalFragmentLo_Type=Counter32
_WwpPortStatsPortalFragmentLo_Object=MibTableColumn
wwpPortStatsPortalFragmentLo=_WwpPortStatsPortalFragmentLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,39),_WwpPortStatsPortalFragmentLo_Type())
wwpPortStatsPortalFragmentLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalFragmentLo.setStatus(_A)
_WwpPortStatsPortalUndersizeFramesHi_Type=Counter32
_WwpPortStatsPortalUndersizeFramesHi_Object=MibTableColumn
wwpPortStatsPortalUndersizeFramesHi=_WwpPortStatsPortalUndersizeFramesHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,40),_WwpPortStatsPortalUndersizeFramesHi_Type())
wwpPortStatsPortalUndersizeFramesHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalUndersizeFramesHi.setStatus(_A)
_WwpPortStatsPortalUndersizeFramesLo_Type=Counter32
_WwpPortStatsPortalUndersizeFramesLo_Object=MibTableColumn
wwpPortStatsPortalUndersizeFramesLo=_WwpPortStatsPortalUndersizeFramesLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,41),_WwpPortStatsPortalUndersizeFramesLo_Type())
wwpPortStatsPortalUndersizeFramesLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalUndersizeFramesLo.setStatus(_A)
_WwpPortStatsPortalShortEventHi_Type=Counter32
_WwpPortStatsPortalShortEventHi_Object=MibTableColumn
wwpPortStatsPortalShortEventHi=_WwpPortStatsPortalShortEventHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,42),_WwpPortStatsPortalShortEventHi_Type())
wwpPortStatsPortalShortEventHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalShortEventHi.setStatus(_A)
_WwpPortStatsPortalShortEventLo_Type=Counter32
_WwpPortStatsPortalShortEventLo_Object=MibTableColumn
wwpPortStatsPortalShortEventLo=_WwpPortStatsPortalShortEventLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,43),_WwpPortStatsPortalShortEventLo_Type())
wwpPortStatsPortalShortEventLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalShortEventLo.setStatus(_A)
_WwpPortStatsPortalCRCHi_Type=Counter32
_WwpPortStatsPortalCRCHi_Object=MibTableColumn
wwpPortStatsPortalCRCHi=_WwpPortStatsPortalCRCHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,44),_WwpPortStatsPortalCRCHi_Type())
wwpPortStatsPortalCRCHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalCRCHi.setStatus(_A)
_WwpPortStatsPortalCRCLo_Type=Counter32
_WwpPortStatsPortalCRCLo_Object=MibTableColumn
wwpPortStatsPortalCRCLo=_WwpPortStatsPortalCRCLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,45),_WwpPortStatsPortalCRCLo_Type())
wwpPortStatsPortalCRCLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalCRCLo.setStatus(_A)
_WwpPortStatsPortalDroppedFramesHi_Type=Counter32
_WwpPortStatsPortalDroppedFramesHi_Object=MibTableColumn
wwpPortStatsPortalDroppedFramesHi=_WwpPortStatsPortalDroppedFramesHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,46),_WwpPortStatsPortalDroppedFramesHi_Type())
wwpPortStatsPortalDroppedFramesHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalDroppedFramesHi.setStatus(_A)
_WwpPortStatsPortalDroppedFramesLo_Type=Counter32
_WwpPortStatsPortalDroppedFramesLo_Object=MibTableColumn
wwpPortStatsPortalDroppedFramesLo=_WwpPortStatsPortalDroppedFramesLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,47),_WwpPortStatsPortalDroppedFramesLo_Type())
wwpPortStatsPortalDroppedFramesLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalDroppedFramesLo.setStatus(_A)
_WwpPortStatsPortalCollisionHi_Type=Counter32
_WwpPortStatsPortalCollisionHi_Object=MibTableColumn
wwpPortStatsPortalCollisionHi=_WwpPortStatsPortalCollisionHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,48),_WwpPortStatsPortalCollisionHi_Type())
wwpPortStatsPortalCollisionHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalCollisionHi.setStatus(_A)
_WwpPortStatsPortalCollisionLo_Type=Counter32
_WwpPortStatsPortalCollisionLo_Object=MibTableColumn
wwpPortStatsPortalCollisionLo=_WwpPortStatsPortalCollisionLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,49),_WwpPortStatsPortalCollisionLo_Type())
wwpPortStatsPortalCollisionLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalCollisionLo.setStatus(_A)
_WwpPortStatsPortalLateCollisionHi_Type=Counter32
_WwpPortStatsPortalLateCollisionHi_Object=MibTableColumn
wwpPortStatsPortalLateCollisionHi=_WwpPortStatsPortalLateCollisionHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,50),_WwpPortStatsPortalLateCollisionHi_Type())
wwpPortStatsPortalLateCollisionHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalLateCollisionHi.setStatus(_A)
_WwpPortStatsPortalLateCollisionLo_Type=Counter32
_WwpPortStatsPortalLateCollisionLo_Object=MibTableColumn
wwpPortStatsPortalLateCollisionLo=_WwpPortStatsPortalLateCollisionLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,51),_WwpPortStatsPortalLateCollisionLo_Type())
wwpPortStatsPortalLateCollisionLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalLateCollisionLo.setStatus(_A)
_WwpPortStatsPortalFilteringCounterHi_Type=Counter32
_WwpPortStatsPortalFilteringCounterHi_Object=MibTableColumn
wwpPortStatsPortalFilteringCounterHi=_WwpPortStatsPortalFilteringCounterHi_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,52),_WwpPortStatsPortalFilteringCounterHi_Type())
wwpPortStatsPortalFilteringCounterHi.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalFilteringCounterHi.setStatus(_A)
_WwpPortStatsPortalFilteringCounterLo_Type=Counter32
_WwpPortStatsPortalFilteringCounterLo_Object=MibTableColumn
wwpPortStatsPortalFilteringCounterLo=_WwpPortStatsPortalFilteringCounterLo_Object((1,3,6,1,4,1,6141,2,16,1,1,4,1,53),_WwpPortStatsPortalFilteringCounterLo_Type())
wwpPortStatsPortalFilteringCounterLo.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpPortStatsPortalFilteringCounterLo.setStatus(_A)
_WwpPortStatsMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpPortStatsMIBNotificationPrefix=_WwpPortStatsMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,16,2))
_WwpPortStatsMIBNotifications_ObjectIdentity=ObjectIdentity
wwpPortStatsMIBNotifications=_WwpPortStatsMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,16,2,0))
_WwpPortStatsMIBConformance_ObjectIdentity=ObjectIdentity
wwpPortStatsMIBConformance=_WwpPortStatsMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,16,3))
_WwpPortStatsMIBCompliances_ObjectIdentity=ObjectIdentity
wwpPortStatsMIBCompliances=_WwpPortStatsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,16,3,1))
_WwpPortStatsMIBGroups_ObjectIdentity=ObjectIdentity
wwpPortStatsMIBGroups=_WwpPortStatsMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,16,3,2))
mibBuilder.exportSymbols(_D,**{'wwpPortStatsMIB':wwpPortStatsMIB,'wwpPortStatsMIBObjects':wwpPortStatsMIBObjects,'wwpPortStats':wwpPortStats,'wwpPortStatsReset':wwpPortStatsReset,'wwpPortStatsTable':wwpPortStatsTable,'wwpPortStatsEntry':wwpPortStatsEntry,_E:wwpPortStatsPortId,'wwpPortStatsRxBytes':wwpPortStatsRxBytes,'wwpPortStatsRxPkts':wwpPortStatsRxPkts,'wwpPortStatsRxCrcErrorPkts':wwpPortStatsRxCrcErrorPkts,'wwpPortStatsRxBcastPkts':wwpPortStatsRxBcastPkts,'wwpPortStatsUndersizePkts':wwpPortStatsUndersizePkts,'wwpPortStatsOversizePkts':wwpPortStatsOversizePkts,'wwpPortStatsFragmentPkts':wwpPortStatsFragmentPkts,'wwpPortStatsJabberPkts':wwpPortStatsJabberPkts,'wwpPortStats64BytePkts':wwpPortStats64BytePkts,'wwpPortStats65To127BytePkts':wwpPortStats65To127BytePkts,'wwpPortStats128To255BytePkts':wwpPortStats128To255BytePkts,'wwpPortStats256To511BytePkts':wwpPortStats256To511BytePkts,'wwpPortStats512To1023BytePkts':wwpPortStats512To1023BytePkts,'wwpPortStats1024To1518BytePkts':wwpPortStats1024To1518BytePkts,'wwpPortStatsTxBytes':wwpPortStatsTxBytes,'wwpPortStatsTxTBytes':wwpPortStatsTxTBytes,'wwpPortStatsTxPkts':wwpPortStatsTxPkts,'wwpPortStatsTxExDeferPkts':wwpPortStatsTxExDeferPkts,'wwpPortStatsTxGiantPkts':wwpPortStatsTxGiantPkts,'wwpPortStatsTxUnderRunPkts':wwpPortStatsTxUnderRunPkts,'wwpPortStatsTxCrcErrorPkts':wwpPortStatsTxCrcErrorPkts,'wwpPortStatsTxLCheckErrorPkts':wwpPortStatsTxLCheckErrorPkts,'wwpPortStatsTxLOutRangePkts':wwpPortStatsTxLOutRangePkts,'wwpPortStatsTxLateCollPkts':wwpPortStatsTxLateCollPkts,'wwpPortStatsTxExCollPkts':wwpPortStatsTxExCollPkts,'wwpPortStatsTxSingleCollPkts':wwpPortStatsTxSingleCollPkts,'wwpPortStatsTxCollPkts':wwpPortStatsTxCollPkts,'wwpPortStatsXTable':wwpPortStatsXTable,'wwpPortStatsXEntry':wwpPortStatsXEntry,'wwpPortStatsXRxBytes':wwpPortStatsXRxBytes,'wwpPortStatsXRxPkts':wwpPortStatsXRxPkts,'wwpPortStatsXTxBytes':wwpPortStatsXTxBytes,'wwpPortStatsXTxPkts':wwpPortStatsXTxPkts,'wwpPortStatsPortalTable':wwpPortStatsPortalTable,'wwpPortStatsPortalEntry':wwpPortStatsPortalEntry,_F:wwpPortStatsPortalPortId,'wwpPortStatsPortalBytesSentHi':wwpPortStatsPortalBytesSentHi,'wwpPortStatsPortalBytesSentLo':wwpPortStatsPortalBytesSentLo,'wwpPortStatsPortalFlowControlHi':wwpPortStatsPortalFlowControlHi,'wwpPortStatsPortalFlowControlLo':wwpPortStatsPortalFlowControlLo,'wwpPortStatsPortalUnicastFramesSentHi':wwpPortStatsPortalUnicastFramesSentHi,'wwpPortStatsPortalUnicastFramesSentLo':wwpPortStatsPortalUnicastFramesSentLo,'wwpPortStatsPortalAlignmentErrorHi':wwpPortStatsPortalAlignmentErrorHi,'wwpPortStatsPortalAlignmentErrorLo':wwpPortStatsPortalAlignmentErrorLo,'wwpPortStatsPortalNonUnicastFramesSentHi':wwpPortStatsPortalNonUnicastFramesSentHi,'wwpPortStatsPortalNonUnicastFramesSentLo':wwpPortStatsPortalNonUnicastFramesSentLo,'wwpPortStatsPortalTotalBytesRecievedHi':wwpPortStatsPortalTotalBytesRecievedHi,'wwpPortStatsPortalTotalBytesRecievedLo':wwpPortStatsPortalTotalBytesRecievedLo,'wwpPortStatsPortalFlowControlFramesRecievedHi':wwpPortStatsPortalFlowControlFramesRecievedHi,'wwpPortStatsPortalFlowControlFramesRecievedLo':wwpPortStatsPortalFlowControlFramesRecievedLo,'wwpPortStatsPortalTotalFramesRecievedHi':wwpPortStatsPortalTotalFramesRecievedHi,'wwpPortStatsPortalTotalFramesRecievedLo':wwpPortStatsPortalTotalFramesRecievedLo,'wwpPortStatsPortalBroadcastFramesRecievedHi':wwpPortStatsPortalBroadcastFramesRecievedHi,'wwpPortStatsPortalBroadcastFramesRecievedLo':wwpPortStatsPortalBroadcastFramesRecievedLo,'wwpPortStatsPortalMulticastFramesRecievedHi':wwpPortStatsPortalMulticastFramesRecievedHi,'wwpPortStatsPortalMulticastFramesRecievedLo':wwpPortStatsPortalMulticastFramesRecievedLo,'wwpPortStatsPortalJabberFramesHi':wwpPortStatsPortalJabberFramesHi,'wwpPortStatsPortalJabberFramesLo':wwpPortStatsPortalJabberFramesLo,'wwpPortStatsPortal64ByteFramesHi':wwpPortStatsPortal64ByteFramesHi,'wwpPortStatsPortal64ByteFramesLo':wwpPortStatsPortal64ByteFramesLo,'wwpPortStatsPortalOversizeFramesHi':wwpPortStatsPortalOversizeFramesHi,'wwpPortStatsPortalOversizeFramesLo':wwpPortStatsPortalOversizeFramesLo,'wwpPortStatsPortal65To127ByteFramesHi':wwpPortStatsPortal65To127ByteFramesHi,'wwpPortStatsPortal65To127ByteFramesLo':wwpPortStatsPortal65To127ByteFramesLo,'wwpPortStatsPortal256To511ByteFramesHi':wwpPortStatsPortal256To511ByteFramesHi,'wwpPortStatsPortal256To511ByteFramesLo':wwpPortStatsPortal256To511ByteFramesLo,'wwpPortStatsPortal128To255ByteFramesHi':wwpPortStatsPortal128To255ByteFramesHi,'wwpPortStatsPortal128To255ByteFramesLo':wwpPortStatsPortal128To255ByteFramesLo,'wwpPortStatsPortal1024To1528ByteFramesHi':wwpPortStatsPortal1024To1528ByteFramesHi,'wwpPortStatsPortal1024To1528ByteFramesLo':wwpPortStatsPortal1024To1528ByteFramesLo,'wwpPortStatsPortal512To1023ByteFramesHi':wwpPortStatsPortal512To1023ByteFramesHi,'wwpPortStatsPortal512To1023ByteFrameslo':wwpPortStatsPortal512To1023ByteFrameslo,'wwpPortStatsPortalFragmentHi':wwpPortStatsPortalFragmentHi,'wwpPortStatsPortalFragmentLo':wwpPortStatsPortalFragmentLo,'wwpPortStatsPortalUndersizeFramesHi':wwpPortStatsPortalUndersizeFramesHi,'wwpPortStatsPortalUndersizeFramesLo':wwpPortStatsPortalUndersizeFramesLo,'wwpPortStatsPortalShortEventHi':wwpPortStatsPortalShortEventHi,'wwpPortStatsPortalShortEventLo':wwpPortStatsPortalShortEventLo,'wwpPortStatsPortalCRCHi':wwpPortStatsPortalCRCHi,'wwpPortStatsPortalCRCLo':wwpPortStatsPortalCRCLo,'wwpPortStatsPortalDroppedFramesHi':wwpPortStatsPortalDroppedFramesHi,'wwpPortStatsPortalDroppedFramesLo':wwpPortStatsPortalDroppedFramesLo,'wwpPortStatsPortalCollisionHi':wwpPortStatsPortalCollisionHi,'wwpPortStatsPortalCollisionLo':wwpPortStatsPortalCollisionLo,'wwpPortStatsPortalLateCollisionHi':wwpPortStatsPortalLateCollisionHi,'wwpPortStatsPortalLateCollisionLo':wwpPortStatsPortalLateCollisionLo,'wwpPortStatsPortalFilteringCounterHi':wwpPortStatsPortalFilteringCounterHi,'wwpPortStatsPortalFilteringCounterLo':wwpPortStatsPortalFilteringCounterLo,'wwpPortStatsMIBNotificationPrefix':wwpPortStatsMIBNotificationPrefix,'wwpPortStatsMIBNotifications':wwpPortStatsMIBNotifications,'wwpPortStatsMIBConformance':wwpPortStatsMIBConformance,'wwpPortStatsMIBCompliances':wwpPortStatsMIBCompliances,'wwpPortStatsMIBGroups':wwpPortStatsMIBGroups})