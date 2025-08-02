_i='rbnPingIpGroup'
_h='rbnPingCtlGroup'
_g='rbnPingResultsGroup'
_f='rbnPingGlobalsGroup'
_e='rbnPingCtlIpTtl'
_d='rbnPingCtlIpDontFragment'
_c='rbnPingCtlMaxHistoryRows'
_b='rbnPingHistoryJitter'
_a='rbnPingHistoryLastGoodProbe'
_Z='rbnPingHistoryRttSumOfSquares'
_Y='rbnPingHistorySentProbes'
_X='rbnPingHistoryProbeResponses'
_W='rbnPingHistoryAverageRtt'
_V='rbnPingHistoryMaxRtt'
_U='rbnPingHistoryMinRtt'
_T='rbnPingHistoryIpTargetAddress'
_S='rbnPingHistoryIpTargetAddressType'
_R='rbnPingResultsJitter'
_Q='rbnPingNumTests'
_P='rbnPingCtlIpEntry'
_O='rbnPingCtlEntry'
_N='rbnPingResultsEntry'
_M='rbnPingHistoryIndex'
_L='TruthValue'
_K='InetAddressType'
_J='InetAddress'
_I='pingCtlTestName'
_H='pingCtlOwnerIndex'
_G='read-create'
_F='DISMAN-PING-MIB'
_E='Unsigned32'
_D='milliseconds'
_C='read-only'
_B='RBN-PING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pingCtlEntry,pingCtlOwnerIndex,pingCtlTestName,pingResultsEntry=mibBuilder.importSymbols(_F,'pingCtlEntry',_H,_I,'pingResultsEntry')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_J,_K)
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention',_L)
rbnPingMib=ModuleIdentity((1,3,6,1,4,1,2352,2,46))
if mibBuilder.loadTexts:rbnPingMib.setRevisions(('2008-07-30 00:00',))
_RbnPingObjects_ObjectIdentity=ObjectIdentity
rbnPingObjects=_RbnPingObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,46,1))
_RbnPingGlobals_ObjectIdentity=ObjectIdentity
rbnPingGlobals=_RbnPingGlobals_ObjectIdentity((1,3,6,1,4,1,2352,2,46,1,1))
_RbnPingNumTests_Type=Gauge32
_RbnPingNumTests_Object=MibScalar
rbnPingNumTests=_RbnPingNumTests_Object((1,3,6,1,4,1,2352,2,46,1,1,1),_RbnPingNumTests_Type())
rbnPingNumTests.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnPingNumTests.setStatus(_A)
_RbnPingResults_ObjectIdentity=ObjectIdentity
rbnPingResults=_RbnPingResults_ObjectIdentity((1,3,6,1,4,1,2352,2,46,1,2))
_RbnPingResultsTable_Object=MibTable
rbnPingResultsTable=_RbnPingResultsTable_Object((1,3,6,1,4,1,2352,2,46,1,2,1))
if mibBuilder.loadTexts:rbnPingResultsTable.setStatus(_A)
_RbnPingResultsEntry_Object=MibTableRow
rbnPingResultsEntry=_RbnPingResultsEntry_Object((1,3,6,1,4,1,2352,2,46,1,2,1,1))
if mibBuilder.loadTexts:rbnPingResultsEntry.setStatus(_A)
_RbnPingResultsJitter_Type=Gauge32
_RbnPingResultsJitter_Object=MibTableColumn
rbnPingResultsJitter=_RbnPingResultsJitter_Object((1,3,6,1,4,1,2352,2,46,1,2,1,1,1),_RbnPingResultsJitter_Type())
rbnPingResultsJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnPingResultsJitter.setStatus(_A)
if mibBuilder.loadTexts:rbnPingResultsJitter.setUnits(_D)
_RbnPingHistoryTable_Object=MibTable
rbnPingHistoryTable=_RbnPingHistoryTable_Object((1,3,6,1,4,1,2352,2,46,1,2,2))
if mibBuilder.loadTexts:rbnPingHistoryTable.setStatus(_A)
_RbnPingHistoryEntry_Object=MibTableRow
rbnPingHistoryEntry=_RbnPingHistoryEntry_Object((1,3,6,1,4,1,2352,2,46,1,2,2,1))
rbnPingHistoryEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_B,_M))
if mibBuilder.loadTexts:rbnPingHistoryEntry.setStatus(_A)
class _RbnPingHistoryIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RbnPingHistoryIndex_Type.__name__=_E
_RbnPingHistoryIndex_Object=MibTableColumn
rbnPingHistoryIndex=_RbnPingHistoryIndex_Object((1,3,6,1,4,1,2352,2,46,1,2,2,1,1),_RbnPingHistoryIndex_Type())
rbnPingHistoryIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rbnPingHistoryIndex.setStatus(_A)
class _RbnPingHistoryIpTargetAddressType_Type(InetAddressType):defaultValue=0
_RbnPingHistoryIpTargetAddressType_Type.__name__=_K
_RbnPingHistoryIpTargetAddressType_Object=MibTableColumn
rbnPingHistoryIpTargetAddressType=_RbnPingHistoryIpTargetAddressType_Object((1,3,6,1,4,1,2352,2,46,1,2,2,1,2),_RbnPingHistoryIpTargetAddressType_Type())
rbnPingHistoryIpTargetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnPingHistoryIpTargetAddressType.setStatus(_A)
class _RbnPingHistoryIpTargetAddress_Type(InetAddress):defaultHexValue=''
_RbnPingHistoryIpTargetAddress_Type.__name__=_J
_RbnPingHistoryIpTargetAddress_Object=MibTableColumn
rbnPingHistoryIpTargetAddress=_RbnPingHistoryIpTargetAddress_Object((1,3,6,1,4,1,2352,2,46,1,2,2,1,3),_RbnPingHistoryIpTargetAddress_Type())
rbnPingHistoryIpTargetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnPingHistoryIpTargetAddress.setStatus(_A)
_RbnPingHistoryMinRtt_Type=Unsigned32
_RbnPingHistoryMinRtt_Object=MibTableColumn
rbnPingHistoryMinRtt=_RbnPingHistoryMinRtt_Object((1,3,6,1,4,1,2352,2,46,1,2,2,1,4),_RbnPingHistoryMinRtt_Type())
rbnPingHistoryMinRtt.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnPingHistoryMinRtt.setStatus(_A)
if mibBuilder.loadTexts:rbnPingHistoryMinRtt.setUnits(_D)
_RbnPingHistoryMaxRtt_Type=Unsigned32
_RbnPingHistoryMaxRtt_Object=MibTableColumn
rbnPingHistoryMaxRtt=_RbnPingHistoryMaxRtt_Object((1,3,6,1,4,1,2352,2,46,1,2,2,1,5),_RbnPingHistoryMaxRtt_Type())
rbnPingHistoryMaxRtt.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnPingHistoryMaxRtt.setStatus(_A)
if mibBuilder.loadTexts:rbnPingHistoryMaxRtt.setUnits(_D)
_RbnPingHistoryAverageRtt_Type=Unsigned32
_RbnPingHistoryAverageRtt_Object=MibTableColumn
rbnPingHistoryAverageRtt=_RbnPingHistoryAverageRtt_Object((1,3,6,1,4,1,2352,2,46,1,2,2,1,6),_RbnPingHistoryAverageRtt_Type())
rbnPingHistoryAverageRtt.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnPingHistoryAverageRtt.setStatus(_A)
if mibBuilder.loadTexts:rbnPingHistoryAverageRtt.setUnits(_D)
_RbnPingHistoryProbeResponses_Type=Gauge32
_RbnPingHistoryProbeResponses_Object=MibTableColumn
rbnPingHistoryProbeResponses=_RbnPingHistoryProbeResponses_Object((1,3,6,1,4,1,2352,2,46,1,2,2,1,7),_RbnPingHistoryProbeResponses_Type())
rbnPingHistoryProbeResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnPingHistoryProbeResponses.setStatus(_A)
if mibBuilder.loadTexts:rbnPingHistoryProbeResponses.setUnits('responses')
_RbnPingHistorySentProbes_Type=Gauge32
_RbnPingHistorySentProbes_Object=MibTableColumn
rbnPingHistorySentProbes=_RbnPingHistorySentProbes_Object((1,3,6,1,4,1,2352,2,46,1,2,2,1,8),_RbnPingHistorySentProbes_Type())
rbnPingHistorySentProbes.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnPingHistorySentProbes.setStatus(_A)
if mibBuilder.loadTexts:rbnPingHistorySentProbes.setUnits('probes')
_RbnPingHistoryRttSumOfSquares_Type=Unsigned32
_RbnPingHistoryRttSumOfSquares_Object=MibTableColumn
rbnPingHistoryRttSumOfSquares=_RbnPingHistoryRttSumOfSquares_Object((1,3,6,1,4,1,2352,2,46,1,2,2,1,9),_RbnPingHistoryRttSumOfSquares_Type())
rbnPingHistoryRttSumOfSquares.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnPingHistoryRttSumOfSquares.setStatus(_A)
if mibBuilder.loadTexts:rbnPingHistoryRttSumOfSquares.setUnits(_D)
_RbnPingHistoryLastGoodProbe_Type=DateAndTime
_RbnPingHistoryLastGoodProbe_Object=MibTableColumn
rbnPingHistoryLastGoodProbe=_RbnPingHistoryLastGoodProbe_Object((1,3,6,1,4,1,2352,2,46,1,2,2,1,10),_RbnPingHistoryLastGoodProbe_Type())
rbnPingHistoryLastGoodProbe.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnPingHistoryLastGoodProbe.setStatus(_A)
_RbnPingHistoryJitter_Type=Gauge32
_RbnPingHistoryJitter_Object=MibTableColumn
rbnPingHistoryJitter=_RbnPingHistoryJitter_Object((1,3,6,1,4,1,2352,2,46,1,2,2,1,11),_RbnPingHistoryJitter_Type())
rbnPingHistoryJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnPingHistoryJitter.setStatus(_A)
if mibBuilder.loadTexts:rbnPingHistoryJitter.setUnits(_D)
_RbnPingControl_ObjectIdentity=ObjectIdentity
rbnPingControl=_RbnPingControl_ObjectIdentity((1,3,6,1,4,1,2352,2,46,1,3))
_RbnPingCtlTable_Object=MibTable
rbnPingCtlTable=_RbnPingCtlTable_Object((1,3,6,1,4,1,2352,2,46,1,3,1))
if mibBuilder.loadTexts:rbnPingCtlTable.setStatus(_A)
_RbnPingCtlEntry_Object=MibTableRow
rbnPingCtlEntry=_RbnPingCtlEntry_Object((1,3,6,1,4,1,2352,2,46,1,3,1,1))
if mibBuilder.loadTexts:rbnPingCtlEntry.setStatus(_A)
class _RbnPingCtlMaxHistoryRows_Type(Unsigned32):defaultValue=12
_RbnPingCtlMaxHistoryRows_Type.__name__=_E
_RbnPingCtlMaxHistoryRows_Object=MibTableColumn
rbnPingCtlMaxHistoryRows=_RbnPingCtlMaxHistoryRows_Object((1,3,6,1,4,1,2352,2,46,1,3,1,1,1),_RbnPingCtlMaxHistoryRows_Type())
rbnPingCtlMaxHistoryRows.setMaxAccess(_G)
if mibBuilder.loadTexts:rbnPingCtlMaxHistoryRows.setStatus(_A)
_RbnPingIp_ObjectIdentity=ObjectIdentity
rbnPingIp=_RbnPingIp_ObjectIdentity((1,3,6,1,4,1,2352,2,46,1,4))
_RbnPingCtlIpTable_Object=MibTable
rbnPingCtlIpTable=_RbnPingCtlIpTable_Object((1,3,6,1,4,1,2352,2,46,1,4,1))
if mibBuilder.loadTexts:rbnPingCtlIpTable.setStatus(_A)
_RbnPingCtlIpEntry_Object=MibTableRow
rbnPingCtlIpEntry=_RbnPingCtlIpEntry_Object((1,3,6,1,4,1,2352,2,46,1,4,1,1))
if mibBuilder.loadTexts:rbnPingCtlIpEntry.setStatus(_A)
class _RbnPingCtlIpDontFragment_Type(TruthValue):defaultValue=2
_RbnPingCtlIpDontFragment_Type.__name__=_L
_RbnPingCtlIpDontFragment_Object=MibTableColumn
rbnPingCtlIpDontFragment=_RbnPingCtlIpDontFragment_Object((1,3,6,1,4,1,2352,2,46,1,4,1,1,1),_RbnPingCtlIpDontFragment_Type())
rbnPingCtlIpDontFragment.setMaxAccess(_G)
if mibBuilder.loadTexts:rbnPingCtlIpDontFragment.setStatus(_A)
class _RbnPingCtlIpTtl_Type(Unsigned32):defaultValue=255;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_RbnPingCtlIpTtl_Type.__name__=_E
_RbnPingCtlIpTtl_Object=MibTableColumn
rbnPingCtlIpTtl=_RbnPingCtlIpTtl_Object((1,3,6,1,4,1,2352,2,46,1,4,1,1,2),_RbnPingCtlIpTtl_Type())
rbnPingCtlIpTtl.setMaxAccess(_G)
if mibBuilder.loadTexts:rbnPingCtlIpTtl.setStatus(_A)
_RbnPingConformance_ObjectIdentity=ObjectIdentity
rbnPingConformance=_RbnPingConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,46,2))
_RbnPingCompliances_ObjectIdentity=ObjectIdentity
rbnPingCompliances=_RbnPingCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,46,2,1))
_RbnPingGroups_ObjectIdentity=ObjectIdentity
rbnPingGroups=_RbnPingGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,46,2,2))
_RbnPingNotifications_ObjectIdentity=ObjectIdentity
rbnPingNotifications=_RbnPingNotifications_ObjectIdentity((1,3,6,1,4,1,2352,2,46,3))
pingResultsEntry.registerAugmentions((_B,_N))
rbnPingResultsEntry.setIndexNames(*pingResultsEntry.getIndexNames())
pingCtlEntry.registerAugmentions((_B,_O))
rbnPingCtlEntry.setIndexNames(*pingCtlEntry.getIndexNames())
pingCtlEntry.registerAugmentions((_B,_P))
rbnPingCtlIpEntry.setIndexNames(*pingCtlEntry.getIndexNames())
rbnPingGlobalsGroup=ObjectGroup((1,3,6,1,4,1,2352,2,46,2,2,1))
rbnPingGlobalsGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:rbnPingGlobalsGroup.setStatus(_A)
rbnPingResultsGroup=ObjectGroup((1,3,6,1,4,1,2352,2,46,2,2,2))
rbnPingResultsGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:rbnPingResultsGroup.setStatus(_A)
rbnPingCtlGroup=ObjectGroup((1,3,6,1,4,1,2352,2,46,2,2,3))
rbnPingCtlGroup.setObjects((_B,_c))
if mibBuilder.loadTexts:rbnPingCtlGroup.setStatus(_A)
rbnPingIpGroup=ObjectGroup((1,3,6,1,4,1,2352,2,46,2,2,4))
rbnPingIpGroup.setObjects(*((_B,_d),(_B,_e)))
if mibBuilder.loadTexts:rbnPingIpGroup.setStatus(_A)
rbnPingIpCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,46,2,1,1))
rbnPingIpCompliance.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:rbnPingIpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rbnPingMib':rbnPingMib,'rbnPingObjects':rbnPingObjects,'rbnPingGlobals':rbnPingGlobals,_Q:rbnPingNumTests,'rbnPingResults':rbnPingResults,'rbnPingResultsTable':rbnPingResultsTable,_N:rbnPingResultsEntry,_R:rbnPingResultsJitter,'rbnPingHistoryTable':rbnPingHistoryTable,'rbnPingHistoryEntry':rbnPingHistoryEntry,_M:rbnPingHistoryIndex,_S:rbnPingHistoryIpTargetAddressType,_T:rbnPingHistoryIpTargetAddress,_U:rbnPingHistoryMinRtt,_V:rbnPingHistoryMaxRtt,_W:rbnPingHistoryAverageRtt,_X:rbnPingHistoryProbeResponses,_Y:rbnPingHistorySentProbes,_Z:rbnPingHistoryRttSumOfSquares,_a:rbnPingHistoryLastGoodProbe,_b:rbnPingHistoryJitter,'rbnPingControl':rbnPingControl,'rbnPingCtlTable':rbnPingCtlTable,_O:rbnPingCtlEntry,_c:rbnPingCtlMaxHistoryRows,'rbnPingIp':rbnPingIp,'rbnPingCtlIpTable':rbnPingCtlIpTable,_P:rbnPingCtlIpEntry,_d:rbnPingCtlIpDontFragment,_e:rbnPingCtlIpTtl,'rbnPingConformance':rbnPingConformance,'rbnPingCompliances':rbnPingCompliances,'rbnPingIpCompliance':rbnPingIpCompliance,'rbnPingGroups':rbnPingGroups,_f:rbnPingGlobalsGroup,_g:rbnPingResultsGroup,_h:rbnPingCtlGroup,_i:rbnPingIpGroup,'rbnPingNotifications':rbnPingNotifications})