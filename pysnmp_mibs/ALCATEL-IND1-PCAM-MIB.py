_q='alaCoroL3HreChangeObjects'
_p='alaCoroL3HrePerCoronadoObjects'
_o='alaCoroL3HrePerModeObjects'
_n='alaCoroL3HreChangeClear'
_m='alaCoroL3HreChangeHashFunction'
_l='alaCoroL3HreChangeHashTableSize'
_k='alaCoroL3HreUpdateChanges'
_j='alaCoroL3HreIpxBytesDiscarded'
_i='alaCoroL3HreIpxPacketsDiscarded'
_h='alaCoroL3HreIpxBytesForwarded'
_g='alaCoroL3HreIpxPacketsForwarded'
_f='alaCoroL3HreIpxBytesReceived'
_e='alaCoroL3HreIpxPacketsReceived'
_d='alaCoroL3HreIpPacketsFailedToFrag'
_c='alaCoroL3HreIpPacketsFragsGenerated'
_b='alaCoroL3HreIpPacketsFragmented'
_a='alaCoroL3HreIpBytesDiscarded'
_Z='alaCoroL3HreIpPacketsDiscarded'
_Y='alaCoroL3HreIpBytesForwarded'
_X='alaCoroL3HreIpPacketsForwarded'
_W='alaCoroL3HreIpBytesReceived'
_V='alaCoroL3HreIpPacketsReceived'
_U='alaCoroL3HreRouteCacheEntriesInUse'
_T='alaCoroL3HreRouteCacheEntriesTotal'
_S='alaCoroL3HreAvgCollChainLen'
_R='alaCoroL3HreMaxCollChainLen'
_Q='alaCoroL3HreModeCurrentHashFunction'
_P='alaCoroL3HreModeCollEntriesInUse'
_O='alaCoroL3HreModeHashEntriesInUse'
_N='alaCoroL3HreModeHashTableSize'
_M='alaCoroL3HreChangeModeNumber'
_L='alaCoroL3HreChangeSliceNumber'
_K='alaCoroL3HreChangeSlotNumber'
_J='alaCoroL3HreSliceNumber'
_I='alaCoroL3HreSlotNumber'
_H='alaCoroL3HrePerModeModeNumber'
_G='alaCoroL3HrePerModeSliceNumber'
_F='alaCoroL3HrePerModeSlotNumber'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='ALCATEL-IND1-PCAM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hardentIND1Pcam,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','hardentIND1Pcam')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alcatelIND1PCAMMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,1,1,4,1))
if mibBuilder.loadTexts:alcatelIND1PCAMMIB.setRevisions(('2007-04-03 00:00',))
class CoroL3HashFunction(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_AlcatelIND1PCAMMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1PCAMMIBObjects=_AlcatelIND1PCAMMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,1,1,4,1,1))
if mibBuilder.loadTexts:alcatelIND1PCAMMIBObjects.setStatus(_A)
_AlaCoroL3HrePerModeTable_Object=MibTable
alaCoroL3HrePerModeTable=_AlaCoroL3HrePerModeTable_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,1))
if mibBuilder.loadTexts:alaCoroL3HrePerModeTable.setStatus(_A)
_AlaCoroL3HrePerModeTableEntry_Object=MibTableRow
alaCoroL3HrePerModeTableEntry=_AlaCoroL3HrePerModeTableEntry_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,1,1))
alaCoroL3HrePerModeTableEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:alaCoroL3HrePerModeTableEntry.setStatus(_A)
_AlaCoroL3HrePerModeSlotNumber_Type=Unsigned32
_AlaCoroL3HrePerModeSlotNumber_Object=MibTableColumn
alaCoroL3HrePerModeSlotNumber=_AlaCoroL3HrePerModeSlotNumber_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,1,1,1),_AlaCoroL3HrePerModeSlotNumber_Type())
alaCoroL3HrePerModeSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HrePerModeSlotNumber.setStatus(_A)
_AlaCoroL3HrePerModeSliceNumber_Type=Unsigned32
_AlaCoroL3HrePerModeSliceNumber_Object=MibTableColumn
alaCoroL3HrePerModeSliceNumber=_AlaCoroL3HrePerModeSliceNumber_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,1,1,2),_AlaCoroL3HrePerModeSliceNumber_Type())
alaCoroL3HrePerModeSliceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HrePerModeSliceNumber.setStatus(_A)
class _AlaCoroL3HrePerModeModeNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AlaCoroL3HrePerModeModeNumber_Type.__name__=_D
_AlaCoroL3HrePerModeModeNumber_Object=MibTableColumn
alaCoroL3HrePerModeModeNumber=_AlaCoroL3HrePerModeModeNumber_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,1,1,3),_AlaCoroL3HrePerModeModeNumber_Type())
alaCoroL3HrePerModeModeNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HrePerModeModeNumber.setStatus(_A)
_AlaCoroL3HreModeHashTableSize_Type=Unsigned32
_AlaCoroL3HreModeHashTableSize_Object=MibTableColumn
alaCoroL3HreModeHashTableSize=_AlaCoroL3HreModeHashTableSize_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,1,1,4),_AlaCoroL3HreModeHashTableSize_Type())
alaCoroL3HreModeHashTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreModeHashTableSize.setStatus(_A)
_AlaCoroL3HreModeHashEntriesInUse_Type=Unsigned32
_AlaCoroL3HreModeHashEntriesInUse_Object=MibTableColumn
alaCoroL3HreModeHashEntriesInUse=_AlaCoroL3HreModeHashEntriesInUse_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,1,1,5),_AlaCoroL3HreModeHashEntriesInUse_Type())
alaCoroL3HreModeHashEntriesInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreModeHashEntriesInUse.setStatus(_A)
_AlaCoroL3HreModeCollEntriesInUse_Type=Unsigned32
_AlaCoroL3HreModeCollEntriesInUse_Object=MibTableColumn
alaCoroL3HreModeCollEntriesInUse=_AlaCoroL3HreModeCollEntriesInUse_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,1,1,6),_AlaCoroL3HreModeCollEntriesInUse_Type())
alaCoroL3HreModeCollEntriesInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreModeCollEntriesInUse.setStatus(_A)
_AlaCoroL3HreModeCurrentHashFunction_Type=CoroL3HashFunction
_AlaCoroL3HreModeCurrentHashFunction_Object=MibTableColumn
alaCoroL3HreModeCurrentHashFunction=_AlaCoroL3HreModeCurrentHashFunction_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,1,1,7),_AlaCoroL3HreModeCurrentHashFunction_Type())
alaCoroL3HreModeCurrentHashFunction.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreModeCurrentHashFunction.setStatus(_A)
_AlaCoroL3HreMaxCollChainLen_Type=Unsigned32
_AlaCoroL3HreMaxCollChainLen_Object=MibTableColumn
alaCoroL3HreMaxCollChainLen=_AlaCoroL3HreMaxCollChainLen_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,1,1,8),_AlaCoroL3HreMaxCollChainLen_Type())
alaCoroL3HreMaxCollChainLen.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreMaxCollChainLen.setStatus(_A)
_AlaCoroL3HreAvgCollChainLen_Type=Unsigned32
_AlaCoroL3HreAvgCollChainLen_Object=MibTableColumn
alaCoroL3HreAvgCollChainLen=_AlaCoroL3HreAvgCollChainLen_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,1,1,9),_AlaCoroL3HreAvgCollChainLen_Type())
alaCoroL3HreAvgCollChainLen.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreAvgCollChainLen.setStatus(_A)
_AlaCoroL3HrePerCoronadoStatsTable_Object=MibTable
alaCoroL3HrePerCoronadoStatsTable=_AlaCoroL3HrePerCoronadoStatsTable_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,2))
if mibBuilder.loadTexts:alaCoroL3HrePerCoronadoStatsTable.setStatus(_A)
_AlaCoroL3HrePerCoronadoStatsTableEntry_Object=MibTableRow
alaCoroL3HrePerCoronadoStatsTableEntry=_AlaCoroL3HrePerCoronadoStatsTableEntry_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,2,1))
alaCoroL3HrePerCoronadoStatsTableEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:alaCoroL3HrePerCoronadoStatsTableEntry.setStatus(_A)
_AlaCoroL3HreSlotNumber_Type=Unsigned32
_AlaCoroL3HreSlotNumber_Object=MibTableColumn
alaCoroL3HreSlotNumber=_AlaCoroL3HreSlotNumber_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,2,1,1),_AlaCoroL3HreSlotNumber_Type())
alaCoroL3HreSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreSlotNumber.setStatus(_A)
_AlaCoroL3HreSliceNumber_Type=Unsigned32
_AlaCoroL3HreSliceNumber_Object=MibTableColumn
alaCoroL3HreSliceNumber=_AlaCoroL3HreSliceNumber_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,2,1,2),_AlaCoroL3HreSliceNumber_Type())
alaCoroL3HreSliceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreSliceNumber.setStatus(_A)
_AlaCoroL3HreRouteCacheEntriesTotal_Type=Unsigned32
_AlaCoroL3HreRouteCacheEntriesTotal_Object=MibTableColumn
alaCoroL3HreRouteCacheEntriesTotal=_AlaCoroL3HreRouteCacheEntriesTotal_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,2,1,3),_AlaCoroL3HreRouteCacheEntriesTotal_Type())
alaCoroL3HreRouteCacheEntriesTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreRouteCacheEntriesTotal.setStatus(_A)
_AlaCoroL3HreRouteCacheEntriesInUse_Type=Unsigned32
_AlaCoroL3HreRouteCacheEntriesInUse_Object=MibTableColumn
alaCoroL3HreRouteCacheEntriesInUse=_AlaCoroL3HreRouteCacheEntriesInUse_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,2,1,4),_AlaCoroL3HreRouteCacheEntriesInUse_Type())
alaCoroL3HreRouteCacheEntriesInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreRouteCacheEntriesInUse.setStatus(_A)
_AlaCoroL3HreIpPacketsReceived_Type=Counter64
_AlaCoroL3HreIpPacketsReceived_Object=MibTableColumn
alaCoroL3HreIpPacketsReceived=_AlaCoroL3HreIpPacketsReceived_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,2,1,5),_AlaCoroL3HreIpPacketsReceived_Type())
alaCoroL3HreIpPacketsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreIpPacketsReceived.setStatus(_A)
_AlaCoroL3HreIpBytesReceived_Type=Counter64
_AlaCoroL3HreIpBytesReceived_Object=MibTableColumn
alaCoroL3HreIpBytesReceived=_AlaCoroL3HreIpBytesReceived_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,2,1,6),_AlaCoroL3HreIpBytesReceived_Type())
alaCoroL3HreIpBytesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreIpBytesReceived.setStatus(_A)
_AlaCoroL3HreIpPacketsForwarded_Type=Counter64
_AlaCoroL3HreIpPacketsForwarded_Object=MibTableColumn
alaCoroL3HreIpPacketsForwarded=_AlaCoroL3HreIpPacketsForwarded_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,2,1,7),_AlaCoroL3HreIpPacketsForwarded_Type())
alaCoroL3HreIpPacketsForwarded.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreIpPacketsForwarded.setStatus(_A)
_AlaCoroL3HreIpBytesForwarded_Type=Counter64
_AlaCoroL3HreIpBytesForwarded_Object=MibTableColumn
alaCoroL3HreIpBytesForwarded=_AlaCoroL3HreIpBytesForwarded_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,2,1,8),_AlaCoroL3HreIpBytesForwarded_Type())
alaCoroL3HreIpBytesForwarded.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreIpBytesForwarded.setStatus(_A)
_AlaCoroL3HreIpPacketsDiscarded_Type=Counter64
_AlaCoroL3HreIpPacketsDiscarded_Object=MibTableColumn
alaCoroL3HreIpPacketsDiscarded=_AlaCoroL3HreIpPacketsDiscarded_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,2,1,9),_AlaCoroL3HreIpPacketsDiscarded_Type())
alaCoroL3HreIpPacketsDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreIpPacketsDiscarded.setStatus(_A)
_AlaCoroL3HreIpBytesDiscarded_Type=Counter64
_AlaCoroL3HreIpBytesDiscarded_Object=MibTableColumn
alaCoroL3HreIpBytesDiscarded=_AlaCoroL3HreIpBytesDiscarded_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,2,1,10),_AlaCoroL3HreIpBytesDiscarded_Type())
alaCoroL3HreIpBytesDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreIpBytesDiscarded.setStatus(_A)
_AlaCoroL3HreIpPacketsFragmented_Type=Counter64
_AlaCoroL3HreIpPacketsFragmented_Object=MibTableColumn
alaCoroL3HreIpPacketsFragmented=_AlaCoroL3HreIpPacketsFragmented_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,2,1,11),_AlaCoroL3HreIpPacketsFragmented_Type())
alaCoroL3HreIpPacketsFragmented.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreIpPacketsFragmented.setStatus(_A)
_AlaCoroL3HreIpPacketsFragsGenerated_Type=Counter64
_AlaCoroL3HreIpPacketsFragsGenerated_Object=MibTableColumn
alaCoroL3HreIpPacketsFragsGenerated=_AlaCoroL3HreIpPacketsFragsGenerated_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,2,1,12),_AlaCoroL3HreIpPacketsFragsGenerated_Type())
alaCoroL3HreIpPacketsFragsGenerated.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreIpPacketsFragsGenerated.setStatus(_A)
_AlaCoroL3HreIpPacketsFailedToFrag_Type=Counter64
_AlaCoroL3HreIpPacketsFailedToFrag_Object=MibTableColumn
alaCoroL3HreIpPacketsFailedToFrag=_AlaCoroL3HreIpPacketsFailedToFrag_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,2,1,13),_AlaCoroL3HreIpPacketsFailedToFrag_Type())
alaCoroL3HreIpPacketsFailedToFrag.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreIpPacketsFailedToFrag.setStatus(_A)
_AlaCoroL3HreIpxPacketsReceived_Type=Counter64
_AlaCoroL3HreIpxPacketsReceived_Object=MibTableColumn
alaCoroL3HreIpxPacketsReceived=_AlaCoroL3HreIpxPacketsReceived_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,2,1,14),_AlaCoroL3HreIpxPacketsReceived_Type())
alaCoroL3HreIpxPacketsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreIpxPacketsReceived.setStatus(_A)
_AlaCoroL3HreIpxBytesReceived_Type=Counter64
_AlaCoroL3HreIpxBytesReceived_Object=MibTableColumn
alaCoroL3HreIpxBytesReceived=_AlaCoroL3HreIpxBytesReceived_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,2,1,15),_AlaCoroL3HreIpxBytesReceived_Type())
alaCoroL3HreIpxBytesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreIpxBytesReceived.setStatus(_A)
_AlaCoroL3HreIpxPacketsForwarded_Type=Counter64
_AlaCoroL3HreIpxPacketsForwarded_Object=MibTableColumn
alaCoroL3HreIpxPacketsForwarded=_AlaCoroL3HreIpxPacketsForwarded_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,2,1,16),_AlaCoroL3HreIpxPacketsForwarded_Type())
alaCoroL3HreIpxPacketsForwarded.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreIpxPacketsForwarded.setStatus(_A)
_AlaCoroL3HreIpxBytesForwarded_Type=Counter64
_AlaCoroL3HreIpxBytesForwarded_Object=MibTableColumn
alaCoroL3HreIpxBytesForwarded=_AlaCoroL3HreIpxBytesForwarded_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,2,1,17),_AlaCoroL3HreIpxBytesForwarded_Type())
alaCoroL3HreIpxBytesForwarded.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreIpxBytesForwarded.setStatus(_A)
_AlaCoroL3HreIpxPacketsDiscarded_Type=Counter64
_AlaCoroL3HreIpxPacketsDiscarded_Object=MibTableColumn
alaCoroL3HreIpxPacketsDiscarded=_AlaCoroL3HreIpxPacketsDiscarded_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,2,1,18),_AlaCoroL3HreIpxPacketsDiscarded_Type())
alaCoroL3HreIpxPacketsDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreIpxPacketsDiscarded.setStatus(_A)
_AlaCoroL3HreIpxBytesDiscarded_Type=Counter64
_AlaCoroL3HreIpxBytesDiscarded_Object=MibTableColumn
alaCoroL3HreIpxBytesDiscarded=_AlaCoroL3HreIpxBytesDiscarded_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,2,1,19),_AlaCoroL3HreIpxBytesDiscarded_Type())
alaCoroL3HreIpxBytesDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreIpxBytesDiscarded.setStatus(_A)
class _AlaCoroL3HreUpdateChanges_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('apply',0),('clear',1)))
_AlaCoroL3HreUpdateChanges_Type.__name__=_D
_AlaCoroL3HreUpdateChanges_Object=MibScalar
alaCoroL3HreUpdateChanges=_AlaCoroL3HreUpdateChanges_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,3),_AlaCoroL3HreUpdateChanges_Type())
alaCoroL3HreUpdateChanges.setMaxAccess(_E)
if mibBuilder.loadTexts:alaCoroL3HreUpdateChanges.setStatus(_A)
_AlaCoroL3HreChangeTable_Object=MibTable
alaCoroL3HreChangeTable=_AlaCoroL3HreChangeTable_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,4))
if mibBuilder.loadTexts:alaCoroL3HreChangeTable.setStatus(_A)
_AlaCoroL3HreChangeTableEntry_Object=MibTableRow
alaCoroL3HreChangeTableEntry=_AlaCoroL3HreChangeTableEntry_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,4,1))
alaCoroL3HreChangeTableEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:alaCoroL3HreChangeTableEntry.setStatus(_A)
_AlaCoroL3HreChangeSlotNumber_Type=Unsigned32
_AlaCoroL3HreChangeSlotNumber_Object=MibTableColumn
alaCoroL3HreChangeSlotNumber=_AlaCoroL3HreChangeSlotNumber_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,4,1,1),_AlaCoroL3HreChangeSlotNumber_Type())
alaCoroL3HreChangeSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreChangeSlotNumber.setStatus(_A)
_AlaCoroL3HreChangeSliceNumber_Type=Unsigned32
_AlaCoroL3HreChangeSliceNumber_Object=MibTableColumn
alaCoroL3HreChangeSliceNumber=_AlaCoroL3HreChangeSliceNumber_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,4,1,2),_AlaCoroL3HreChangeSliceNumber_Type())
alaCoroL3HreChangeSliceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreChangeSliceNumber.setStatus(_A)
class _AlaCoroL3HreChangeModeNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AlaCoroL3HreChangeModeNumber_Type.__name__=_D
_AlaCoroL3HreChangeModeNumber_Object=MibTableColumn
alaCoroL3HreChangeModeNumber=_AlaCoroL3HreChangeModeNumber_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,4,1,3),_AlaCoroL3HreChangeModeNumber_Type())
alaCoroL3HreChangeModeNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alaCoroL3HreChangeModeNumber.setStatus(_A)
_AlaCoroL3HreChangeHashTableSize_Type=Unsigned32
_AlaCoroL3HreChangeHashTableSize_Object=MibTableColumn
alaCoroL3HreChangeHashTableSize=_AlaCoroL3HreChangeHashTableSize_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,4,1,4),_AlaCoroL3HreChangeHashTableSize_Type())
alaCoroL3HreChangeHashTableSize.setMaxAccess(_E)
if mibBuilder.loadTexts:alaCoroL3HreChangeHashTableSize.setStatus(_A)
_AlaCoroL3HreChangeHashFunction_Type=CoroL3HashFunction
_AlaCoroL3HreChangeHashFunction_Object=MibTableColumn
alaCoroL3HreChangeHashFunction=_AlaCoroL3HreChangeHashFunction_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,4,1,5),_AlaCoroL3HreChangeHashFunction_Type())
alaCoroL3HreChangeHashFunction.setMaxAccess(_E)
if mibBuilder.loadTexts:alaCoroL3HreChangeHashFunction.setStatus(_A)
class _AlaCoroL3HreChangeClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('clear',0))
_AlaCoroL3HreChangeClear_Type.__name__=_D
_AlaCoroL3HreChangeClear_Object=MibTableColumn
alaCoroL3HreChangeClear=_AlaCoroL3HreChangeClear_Object((1,3,6,1,4,1,6486,800,1,1,1,4,1,1,4,1,6),_AlaCoroL3HreChangeClear_Type())
alaCoroL3HreChangeClear.setMaxAccess(_E)
if mibBuilder.loadTexts:alaCoroL3HreChangeClear.setStatus(_A)
_AlcatelIND1PCAMMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1PCAMMIBConformance=_AlcatelIND1PCAMMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,1,1,4,1,2))
if mibBuilder.loadTexts:alcatelIND1PCAMMIBConformance.setStatus(_A)
_AlcatelIND1PCAMMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1PCAMMIBGroups=_AlcatelIND1PCAMMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,1,1,4,1,2,1))
if mibBuilder.loadTexts:alcatelIND1PCAMMIBGroups.setStatus(_A)
_AlcatelIND1PCAMMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1PCAMMIBCompliances=_AlcatelIND1PCAMMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,1,1,4,1,2,2))
if mibBuilder.loadTexts:alcatelIND1PCAMMIBCompliances.setStatus(_A)
alaCoroL3HrePerModeObjects=ObjectGroup((1,3,6,1,4,1,6486,800,1,1,1,4,1,2,1,1))
alaCoroL3HrePerModeObjects.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:alaCoroL3HrePerModeObjects.setStatus(_A)
alaCoroL3HrePerCoronadoObjects=ObjectGroup((1,3,6,1,4,1,6486,800,1,1,1,4,1,2,1,2))
alaCoroL3HrePerCoronadoObjects.setObjects(*((_B,_I),(_B,_J),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:alaCoroL3HrePerCoronadoObjects.setStatus(_A)
alaCoroL3HreChangeObjects=ObjectGroup((1,3,6,1,4,1,6486,800,1,1,1,4,1,2,1,3))
alaCoroL3HreChangeObjects.setObjects(*((_B,_k),(_B,_K),(_B,_L),(_B,_M),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:alaCoroL3HreChangeObjects.setStatus(_A)
alcatelInd1PCAMMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,1,1,4,1,2,2,1))
alcatelInd1PCAMMIBCompliance.setObjects(*((_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:alcatelInd1PCAMMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CoroL3HashFunction':CoroL3HashFunction,'alcatelIND1PCAMMIB':alcatelIND1PCAMMIB,'alcatelIND1PCAMMIBObjects':alcatelIND1PCAMMIBObjects,'alaCoroL3HrePerModeTable':alaCoroL3HrePerModeTable,'alaCoroL3HrePerModeTableEntry':alaCoroL3HrePerModeTableEntry,_F:alaCoroL3HrePerModeSlotNumber,_G:alaCoroL3HrePerModeSliceNumber,_H:alaCoroL3HrePerModeModeNumber,_N:alaCoroL3HreModeHashTableSize,_O:alaCoroL3HreModeHashEntriesInUse,_P:alaCoroL3HreModeCollEntriesInUse,_Q:alaCoroL3HreModeCurrentHashFunction,_R:alaCoroL3HreMaxCollChainLen,_S:alaCoroL3HreAvgCollChainLen,'alaCoroL3HrePerCoronadoStatsTable':alaCoroL3HrePerCoronadoStatsTable,'alaCoroL3HrePerCoronadoStatsTableEntry':alaCoroL3HrePerCoronadoStatsTableEntry,_I:alaCoroL3HreSlotNumber,_J:alaCoroL3HreSliceNumber,_T:alaCoroL3HreRouteCacheEntriesTotal,_U:alaCoroL3HreRouteCacheEntriesInUse,_V:alaCoroL3HreIpPacketsReceived,_W:alaCoroL3HreIpBytesReceived,_X:alaCoroL3HreIpPacketsForwarded,_Y:alaCoroL3HreIpBytesForwarded,_Z:alaCoroL3HreIpPacketsDiscarded,_a:alaCoroL3HreIpBytesDiscarded,_b:alaCoroL3HreIpPacketsFragmented,_c:alaCoroL3HreIpPacketsFragsGenerated,_d:alaCoroL3HreIpPacketsFailedToFrag,_e:alaCoroL3HreIpxPacketsReceived,_f:alaCoroL3HreIpxBytesReceived,_g:alaCoroL3HreIpxPacketsForwarded,_h:alaCoroL3HreIpxBytesForwarded,_i:alaCoroL3HreIpxPacketsDiscarded,_j:alaCoroL3HreIpxBytesDiscarded,_k:alaCoroL3HreUpdateChanges,'alaCoroL3HreChangeTable':alaCoroL3HreChangeTable,'alaCoroL3HreChangeTableEntry':alaCoroL3HreChangeTableEntry,_K:alaCoroL3HreChangeSlotNumber,_L:alaCoroL3HreChangeSliceNumber,_M:alaCoroL3HreChangeModeNumber,_l:alaCoroL3HreChangeHashTableSize,_m:alaCoroL3HreChangeHashFunction,_n:alaCoroL3HreChangeClear,'alcatelIND1PCAMMIBConformance':alcatelIND1PCAMMIBConformance,'alcatelIND1PCAMMIBGroups':alcatelIND1PCAMMIBGroups,_o:alaCoroL3HrePerModeObjects,_p:alaCoroL3HrePerCoronadoObjects,_q:alaCoroL3HreChangeObjects,'alcatelIND1PCAMMIBCompliances':alcatelIND1PCAMMIBCompliances,'alcatelInd1PCAMMIBCompliance':alcatelInd1PCAMMIBCompliance})