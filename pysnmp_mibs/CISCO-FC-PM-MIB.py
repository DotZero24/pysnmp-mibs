_AG='cfcpmOptionalGroup'
_AF='cfcpmMandatoryGroup'
_AE='cfcpmPortStatusGroup'
_AD='cfcpmiPortOtherErrors'
_AC='cfcpmiPortEncDisparityErrors'
_AB='cfcpmiPortDelimiterErrors'
_AA='cfcpmiPortAddressErrors'
_A9='cfcpmiPortTruncatedFrames'
_A8='cfcpmiPortFramesTooLong'
_A7='cfcpmiPortInvalidOrderedSets'
_A6='cfcpmiPortInvalidCRCs'
_A5='cfcpmiPortInvalidTxWords'
_A4='cfcpmiPortSignalLosses'
_A3='cfcpmiPortSynchLosses'
_A2='cfcpmiPortLinkFailures'
_A1='cfcpmiPortTxOfflineSequences'
_A0='cfcpmiPortRxOfflineSequences'
_z='cfcpmiPortLinkResets'
_y='cfcpmiPortTxLinkResets'
_x='cfcpmiPortRxLinkResets'
_w='cfcpmcPortOtherErrors'
_v='cfcpmcPortEncDisparityErrors'
_u='cfcpmcPortDelimiterErrors'
_t='cfcpmcPortAddressErrors'
_s='cfcpmcPortTruncatedFrames'
_r='cfcpmcPortFramesTooLong'
_q='cfcpmcPortInvalidOrderedSets'
_p='cfcpmcPortInvalidCRCs'
_o='cfcpmcPortInvalidTxWords'
_n='cfcpmcPortSignalLosses'
_m='cfcpmcPortSynchLosses'
_l='cfcpmcPortLinkFailures'
_k='cfcpmcPortTxOfflineSequences'
_j='cfcpmcPortRxOfflineSequences'
_i='cfcpmcPortLinkResets'
_h='cfcpmcPortTxLinkResets'
_g='cfcpmcPortRxLinkResets'
_f='cfcpmtPortOtherErrors'
_e='cfcpmtPortEncDisparityErrors'
_d='cfcpmtPortDelimiterErrors'
_c='cfcpmtPortAddressErrors'
_b='cfcpmtPortTruncatedFrames'
_a='cfcpmtPortFramesTooLong'
_Z='cfcpmtPortInvalidOrderedSets'
_Y='cfcpmtPortInvalidCRCs'
_X='cfcpmtPortInvalidTxWords'
_W='cfcpmtPortSignalLosses'
_V='cfcpmtPortSynchLosses'
_U='cfcpmtPortLinkFailures'
_T='cfcpmtPortTxOfflineSequences'
_S='cfcpmtPortRxOfflineSequences'
_R='cfcpmtPortLinkResets'
_Q='cfcpmtPortTxLinkResets'
_P='cfcpmtPortRxLinkResets'
_O='cfcpmiPortValidData'
_N='cfcpmiPortPrimSeqProtocolErrors'
_M='cfcpmcPortPrimSeqProtocolErrors'
_L='cfcpmtPortPrimSeqProtocolErrors'
_K='cfcpmInvalidIntervals'
_J='cfcpmValidIntervals'
_I='cfcpmTimeElapsed'
_H='cfcpmiPortErrorIntervalNumber'
_G='Unsigned32'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='CISCO-FC-PM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_D,_E)
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoFcPmMIB=ModuleIdentity((1,3,6,1,4,1,9,9,99997))
if mibBuilder.loadTexts:ciscoFcPmMIB.setRevisions(('2005-02-06 00:00',))
_CiscoFcPmMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoFcPmMIBNotifs=_CiscoFcPmMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,99997,0))
_CiscoFcPmMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFcPmMIBObjects=_CiscoFcPmMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,99997,1))
_CfcpmPortPerfStatus_ObjectIdentity=ObjectIdentity
cfcpmPortPerfStatus=_CfcpmPortPerfStatus_ObjectIdentity((1,3,6,1,4,1,9,9,99997,1,1))
_CfcpmPortPerfStatusTable_Object=MibTable
cfcpmPortPerfStatusTable=_CfcpmPortPerfStatusTable_Object((1,3,6,1,4,1,9,9,99997,1,1,1))
if mibBuilder.loadTexts:cfcpmPortPerfStatusTable.setStatus(_A)
_CfcpmPortPerfStatusEntry_Object=MibTableRow
cfcpmPortPerfStatusEntry=_CfcpmPortPerfStatusEntry_Object((1,3,6,1,4,1,9,9,99997,1,1,1,1))
cfcpmPortPerfStatusEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cfcpmPortPerfStatusEntry.setStatus(_A)
class _CfcpmTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,899))
_CfcpmTimeElapsed_Type.__name__=_F
_CfcpmTimeElapsed_Object=MibTableColumn
cfcpmTimeElapsed=_CfcpmTimeElapsed_Object((1,3,6,1,4,1,9,9,99997,1,1,1,1,1),_CfcpmTimeElapsed_Type())
cfcpmTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmTimeElapsed.setStatus(_A)
class _CfcpmValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_CfcpmValidIntervals_Type.__name__=_F
_CfcpmValidIntervals_Object=MibTableColumn
cfcpmValidIntervals=_CfcpmValidIntervals_Object((1,3,6,1,4,1,9,9,99997,1,1,1,1,2),_CfcpmValidIntervals_Type())
cfcpmValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmValidIntervals.setStatus(_A)
class _CfcpmInvalidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_CfcpmInvalidIntervals_Type.__name__=_F
_CfcpmInvalidIntervals_Object=MibTableColumn
cfcpmInvalidIntervals=_CfcpmInvalidIntervals_Object((1,3,6,1,4,1,9,9,99997,1,1,1,1,3),_CfcpmInvalidIntervals_Type())
cfcpmInvalidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmInvalidIntervals.setStatus(_A)
_CfcpmPortErrorStatusBlock_ObjectIdentity=ObjectIdentity
cfcpmPortErrorStatusBlock=_CfcpmPortErrorStatusBlock_ObjectIdentity((1,3,6,1,4,1,9,9,99997,1,2))
_CfcpmTotalPortErrorTable_Object=MibTable
cfcpmTotalPortErrorTable=_CfcpmTotalPortErrorTable_Object((1,3,6,1,4,1,9,9,99997,1,2,1))
if mibBuilder.loadTexts:cfcpmTotalPortErrorTable.setStatus(_A)
_CfcpmTotalPortErrorEntry_Object=MibTableRow
cfcpmTotalPortErrorEntry=_CfcpmTotalPortErrorEntry_Object((1,3,6,1,4,1,9,9,99997,1,2,1,1))
cfcpmTotalPortErrorEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cfcpmTotalPortErrorEntry.setStatus(_A)
_CfcpmtPortRxLinkResets_Type=PerfTotalCount
_CfcpmtPortRxLinkResets_Object=MibTableColumn
cfcpmtPortRxLinkResets=_CfcpmtPortRxLinkResets_Object((1,3,6,1,4,1,9,9,99997,1,2,1,1,1),_CfcpmtPortRxLinkResets_Type())
cfcpmtPortRxLinkResets.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmtPortRxLinkResets.setStatus(_A)
_CfcpmtPortTxLinkResets_Type=PerfTotalCount
_CfcpmtPortTxLinkResets_Object=MibTableColumn
cfcpmtPortTxLinkResets=_CfcpmtPortTxLinkResets_Object((1,3,6,1,4,1,9,9,99997,1,2,1,1,2),_CfcpmtPortTxLinkResets_Type())
cfcpmtPortTxLinkResets.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmtPortTxLinkResets.setStatus(_A)
_CfcpmtPortLinkResets_Type=PerfTotalCount
_CfcpmtPortLinkResets_Object=MibTableColumn
cfcpmtPortLinkResets=_CfcpmtPortLinkResets_Object((1,3,6,1,4,1,9,9,99997,1,2,1,1,3),_CfcpmtPortLinkResets_Type())
cfcpmtPortLinkResets.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmtPortLinkResets.setStatus(_A)
_CfcpmtPortRxOfflineSequences_Type=PerfTotalCount
_CfcpmtPortRxOfflineSequences_Object=MibTableColumn
cfcpmtPortRxOfflineSequences=_CfcpmtPortRxOfflineSequences_Object((1,3,6,1,4,1,9,9,99997,1,2,1,1,4),_CfcpmtPortRxOfflineSequences_Type())
cfcpmtPortRxOfflineSequences.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmtPortRxOfflineSequences.setStatus(_A)
_CfcpmtPortTxOfflineSequences_Type=PerfTotalCount
_CfcpmtPortTxOfflineSequences_Object=MibTableColumn
cfcpmtPortTxOfflineSequences=_CfcpmtPortTxOfflineSequences_Object((1,3,6,1,4,1,9,9,99997,1,2,1,1,5),_CfcpmtPortTxOfflineSequences_Type())
cfcpmtPortTxOfflineSequences.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmtPortTxOfflineSequences.setStatus(_A)
_CfcpmtPortLinkFailures_Type=PerfTotalCount
_CfcpmtPortLinkFailures_Object=MibTableColumn
cfcpmtPortLinkFailures=_CfcpmtPortLinkFailures_Object((1,3,6,1,4,1,9,9,99997,1,2,1,1,6),_CfcpmtPortLinkFailures_Type())
cfcpmtPortLinkFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmtPortLinkFailures.setStatus(_A)
_CfcpmtPortSynchLosses_Type=PerfTotalCount
_CfcpmtPortSynchLosses_Object=MibTableColumn
cfcpmtPortSynchLosses=_CfcpmtPortSynchLosses_Object((1,3,6,1,4,1,9,9,99997,1,2,1,1,7),_CfcpmtPortSynchLosses_Type())
cfcpmtPortSynchLosses.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmtPortSynchLosses.setStatus(_A)
_CfcpmtPortSignalLosses_Type=PerfTotalCount
_CfcpmtPortSignalLosses_Object=MibTableColumn
cfcpmtPortSignalLosses=_CfcpmtPortSignalLosses_Object((1,3,6,1,4,1,9,9,99997,1,2,1,1,8),_CfcpmtPortSignalLosses_Type())
cfcpmtPortSignalLosses.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmtPortSignalLosses.setStatus(_A)
_CfcpmtPortPrimSeqProtocolErrors_Type=PerfTotalCount
_CfcpmtPortPrimSeqProtocolErrors_Object=MibTableColumn
cfcpmtPortPrimSeqProtocolErrors=_CfcpmtPortPrimSeqProtocolErrors_Object((1,3,6,1,4,1,9,9,99997,1,2,1,1,9),_CfcpmtPortPrimSeqProtocolErrors_Type())
cfcpmtPortPrimSeqProtocolErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmtPortPrimSeqProtocolErrors.setStatus(_A)
_CfcpmtPortInvalidTxWords_Type=PerfTotalCount
_CfcpmtPortInvalidTxWords_Object=MibTableColumn
cfcpmtPortInvalidTxWords=_CfcpmtPortInvalidTxWords_Object((1,3,6,1,4,1,9,9,99997,1,2,1,1,10),_CfcpmtPortInvalidTxWords_Type())
cfcpmtPortInvalidTxWords.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmtPortInvalidTxWords.setStatus(_A)
_CfcpmtPortInvalidCRCs_Type=PerfTotalCount
_CfcpmtPortInvalidCRCs_Object=MibTableColumn
cfcpmtPortInvalidCRCs=_CfcpmtPortInvalidCRCs_Object((1,3,6,1,4,1,9,9,99997,1,2,1,1,11),_CfcpmtPortInvalidCRCs_Type())
cfcpmtPortInvalidCRCs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmtPortInvalidCRCs.setStatus(_A)
_CfcpmtPortInvalidOrderedSets_Type=PerfTotalCount
_CfcpmtPortInvalidOrderedSets_Object=MibTableColumn
cfcpmtPortInvalidOrderedSets=_CfcpmtPortInvalidOrderedSets_Object((1,3,6,1,4,1,9,9,99997,1,2,1,1,12),_CfcpmtPortInvalidOrderedSets_Type())
cfcpmtPortInvalidOrderedSets.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmtPortInvalidOrderedSets.setStatus(_A)
_CfcpmtPortFramesTooLong_Type=PerfTotalCount
_CfcpmtPortFramesTooLong_Object=MibTableColumn
cfcpmtPortFramesTooLong=_CfcpmtPortFramesTooLong_Object((1,3,6,1,4,1,9,9,99997,1,2,1,1,13),_CfcpmtPortFramesTooLong_Type())
cfcpmtPortFramesTooLong.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmtPortFramesTooLong.setStatus(_A)
_CfcpmtPortTruncatedFrames_Type=PerfTotalCount
_CfcpmtPortTruncatedFrames_Object=MibTableColumn
cfcpmtPortTruncatedFrames=_CfcpmtPortTruncatedFrames_Object((1,3,6,1,4,1,9,9,99997,1,2,1,1,14),_CfcpmtPortTruncatedFrames_Type())
cfcpmtPortTruncatedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmtPortTruncatedFrames.setStatus(_A)
_CfcpmtPortAddressErrors_Type=PerfTotalCount
_CfcpmtPortAddressErrors_Object=MibTableColumn
cfcpmtPortAddressErrors=_CfcpmtPortAddressErrors_Object((1,3,6,1,4,1,9,9,99997,1,2,1,1,15),_CfcpmtPortAddressErrors_Type())
cfcpmtPortAddressErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmtPortAddressErrors.setStatus(_A)
_CfcpmtPortDelimiterErrors_Type=PerfTotalCount
_CfcpmtPortDelimiterErrors_Object=MibTableColumn
cfcpmtPortDelimiterErrors=_CfcpmtPortDelimiterErrors_Object((1,3,6,1,4,1,9,9,99997,1,2,1,1,16),_CfcpmtPortDelimiterErrors_Type())
cfcpmtPortDelimiterErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmtPortDelimiterErrors.setStatus(_A)
_CfcpmtPortEncDisparityErrors_Type=PerfTotalCount
_CfcpmtPortEncDisparityErrors_Object=MibTableColumn
cfcpmtPortEncDisparityErrors=_CfcpmtPortEncDisparityErrors_Object((1,3,6,1,4,1,9,9,99997,1,2,1,1,17),_CfcpmtPortEncDisparityErrors_Type())
cfcpmtPortEncDisparityErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmtPortEncDisparityErrors.setStatus(_A)
_CfcpmtPortOtherErrors_Type=PerfTotalCount
_CfcpmtPortOtherErrors_Object=MibTableColumn
cfcpmtPortOtherErrors=_CfcpmtPortOtherErrors_Object((1,3,6,1,4,1,9,9,99997,1,2,1,1,18),_CfcpmtPortOtherErrors_Type())
cfcpmtPortOtherErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmtPortOtherErrors.setStatus(_A)
_CfcpmCurrentPortErrorTable_Object=MibTable
cfcpmCurrentPortErrorTable=_CfcpmCurrentPortErrorTable_Object((1,3,6,1,4,1,9,9,99997,1,2,2))
if mibBuilder.loadTexts:cfcpmCurrentPortErrorTable.setStatus(_A)
_CfcpmCurrentPortErrorEntry_Object=MibTableRow
cfcpmCurrentPortErrorEntry=_CfcpmCurrentPortErrorEntry_Object((1,3,6,1,4,1,9,9,99997,1,2,2,1))
cfcpmCurrentPortErrorEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cfcpmCurrentPortErrorEntry.setStatus(_A)
_CfcpmcPortRxLinkResets_Type=PerfCurrentCount
_CfcpmcPortRxLinkResets_Object=MibTableColumn
cfcpmcPortRxLinkResets=_CfcpmcPortRxLinkResets_Object((1,3,6,1,4,1,9,9,99997,1,2,2,1,1),_CfcpmcPortRxLinkResets_Type())
cfcpmcPortRxLinkResets.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmcPortRxLinkResets.setStatus(_A)
_CfcpmcPortTxLinkResets_Type=PerfCurrentCount
_CfcpmcPortTxLinkResets_Object=MibTableColumn
cfcpmcPortTxLinkResets=_CfcpmcPortTxLinkResets_Object((1,3,6,1,4,1,9,9,99997,1,2,2,1,2),_CfcpmcPortTxLinkResets_Type())
cfcpmcPortTxLinkResets.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmcPortTxLinkResets.setStatus(_A)
_CfcpmcPortLinkResets_Type=PerfCurrentCount
_CfcpmcPortLinkResets_Object=MibTableColumn
cfcpmcPortLinkResets=_CfcpmcPortLinkResets_Object((1,3,6,1,4,1,9,9,99997,1,2,2,1,3),_CfcpmcPortLinkResets_Type())
cfcpmcPortLinkResets.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmcPortLinkResets.setStatus(_A)
_CfcpmcPortRxOfflineSequences_Type=PerfCurrentCount
_CfcpmcPortRxOfflineSequences_Object=MibTableColumn
cfcpmcPortRxOfflineSequences=_CfcpmcPortRxOfflineSequences_Object((1,3,6,1,4,1,9,9,99997,1,2,2,1,4),_CfcpmcPortRxOfflineSequences_Type())
cfcpmcPortRxOfflineSequences.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmcPortRxOfflineSequences.setStatus(_A)
_CfcpmcPortTxOfflineSequences_Type=PerfCurrentCount
_CfcpmcPortTxOfflineSequences_Object=MibTableColumn
cfcpmcPortTxOfflineSequences=_CfcpmcPortTxOfflineSequences_Object((1,3,6,1,4,1,9,9,99997,1,2,2,1,5),_CfcpmcPortTxOfflineSequences_Type())
cfcpmcPortTxOfflineSequences.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmcPortTxOfflineSequences.setStatus(_A)
_CfcpmcPortLinkFailures_Type=PerfCurrentCount
_CfcpmcPortLinkFailures_Object=MibTableColumn
cfcpmcPortLinkFailures=_CfcpmcPortLinkFailures_Object((1,3,6,1,4,1,9,9,99997,1,2,2,1,6),_CfcpmcPortLinkFailures_Type())
cfcpmcPortLinkFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmcPortLinkFailures.setStatus(_A)
_CfcpmcPortSynchLosses_Type=PerfCurrentCount
_CfcpmcPortSynchLosses_Object=MibTableColumn
cfcpmcPortSynchLosses=_CfcpmcPortSynchLosses_Object((1,3,6,1,4,1,9,9,99997,1,2,2,1,7),_CfcpmcPortSynchLosses_Type())
cfcpmcPortSynchLosses.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmcPortSynchLosses.setStatus(_A)
_CfcpmcPortSignalLosses_Type=PerfCurrentCount
_CfcpmcPortSignalLosses_Object=MibTableColumn
cfcpmcPortSignalLosses=_CfcpmcPortSignalLosses_Object((1,3,6,1,4,1,9,9,99997,1,2,2,1,8),_CfcpmcPortSignalLosses_Type())
cfcpmcPortSignalLosses.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmcPortSignalLosses.setStatus(_A)
_CfcpmcPortPrimSeqProtocolErrors_Type=PerfCurrentCount
_CfcpmcPortPrimSeqProtocolErrors_Object=MibTableColumn
cfcpmcPortPrimSeqProtocolErrors=_CfcpmcPortPrimSeqProtocolErrors_Object((1,3,6,1,4,1,9,9,99997,1,2,2,1,9),_CfcpmcPortPrimSeqProtocolErrors_Type())
cfcpmcPortPrimSeqProtocolErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmcPortPrimSeqProtocolErrors.setStatus(_A)
_CfcpmcPortInvalidTxWords_Type=PerfCurrentCount
_CfcpmcPortInvalidTxWords_Object=MibTableColumn
cfcpmcPortInvalidTxWords=_CfcpmcPortInvalidTxWords_Object((1,3,6,1,4,1,9,9,99997,1,2,2,1,10),_CfcpmcPortInvalidTxWords_Type())
cfcpmcPortInvalidTxWords.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmcPortInvalidTxWords.setStatus(_A)
_CfcpmcPortInvalidCRCs_Type=PerfCurrentCount
_CfcpmcPortInvalidCRCs_Object=MibTableColumn
cfcpmcPortInvalidCRCs=_CfcpmcPortInvalidCRCs_Object((1,3,6,1,4,1,9,9,99997,1,2,2,1,11),_CfcpmcPortInvalidCRCs_Type())
cfcpmcPortInvalidCRCs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmcPortInvalidCRCs.setStatus(_A)
_CfcpmcPortInvalidOrderedSets_Type=PerfCurrentCount
_CfcpmcPortInvalidOrderedSets_Object=MibTableColumn
cfcpmcPortInvalidOrderedSets=_CfcpmcPortInvalidOrderedSets_Object((1,3,6,1,4,1,9,9,99997,1,2,2,1,12),_CfcpmcPortInvalidOrderedSets_Type())
cfcpmcPortInvalidOrderedSets.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmcPortInvalidOrderedSets.setStatus(_A)
_CfcpmcPortFramesTooLong_Type=PerfCurrentCount
_CfcpmcPortFramesTooLong_Object=MibTableColumn
cfcpmcPortFramesTooLong=_CfcpmcPortFramesTooLong_Object((1,3,6,1,4,1,9,9,99997,1,2,2,1,13),_CfcpmcPortFramesTooLong_Type())
cfcpmcPortFramesTooLong.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmcPortFramesTooLong.setStatus(_A)
_CfcpmcPortTruncatedFrames_Type=PerfCurrentCount
_CfcpmcPortTruncatedFrames_Object=MibTableColumn
cfcpmcPortTruncatedFrames=_CfcpmcPortTruncatedFrames_Object((1,3,6,1,4,1,9,9,99997,1,2,2,1,14),_CfcpmcPortTruncatedFrames_Type())
cfcpmcPortTruncatedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmcPortTruncatedFrames.setStatus(_A)
_CfcpmcPortAddressErrors_Type=PerfCurrentCount
_CfcpmcPortAddressErrors_Object=MibTableColumn
cfcpmcPortAddressErrors=_CfcpmcPortAddressErrors_Object((1,3,6,1,4,1,9,9,99997,1,2,2,1,15),_CfcpmcPortAddressErrors_Type())
cfcpmcPortAddressErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmcPortAddressErrors.setStatus(_A)
_CfcpmcPortDelimiterErrors_Type=PerfCurrentCount
_CfcpmcPortDelimiterErrors_Object=MibTableColumn
cfcpmcPortDelimiterErrors=_CfcpmcPortDelimiterErrors_Object((1,3,6,1,4,1,9,9,99997,1,2,2,1,16),_CfcpmcPortDelimiterErrors_Type())
cfcpmcPortDelimiterErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmcPortDelimiterErrors.setStatus(_A)
_CfcpmcPortEncDisparityErrors_Type=PerfCurrentCount
_CfcpmcPortEncDisparityErrors_Object=MibTableColumn
cfcpmcPortEncDisparityErrors=_CfcpmcPortEncDisparityErrors_Object((1,3,6,1,4,1,9,9,99997,1,2,2,1,17),_CfcpmcPortEncDisparityErrors_Type())
cfcpmcPortEncDisparityErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmcPortEncDisparityErrors.setStatus(_A)
_CfcpmcPortOtherErrors_Type=PerfCurrentCount
_CfcpmcPortOtherErrors_Object=MibTableColumn
cfcpmcPortOtherErrors=_CfcpmcPortOtherErrors_Object((1,3,6,1,4,1,9,9,99997,1,2,2,1,18),_CfcpmcPortOtherErrors_Type())
cfcpmcPortOtherErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmcPortOtherErrors.setStatus(_A)
_CfcpmIntervalPortErrorTable_Object=MibTable
cfcpmIntervalPortErrorTable=_CfcpmIntervalPortErrorTable_Object((1,3,6,1,4,1,9,9,99997,1,2,3))
if mibBuilder.loadTexts:cfcpmIntervalPortErrorTable.setStatus(_A)
_CfcpmIntervalPortErrorEntry_Object=MibTableRow
cfcpmIntervalPortErrorEntry=_CfcpmIntervalPortErrorEntry_Object((1,3,6,1,4,1,9,9,99997,1,2,3,1))
cfcpmIntervalPortErrorEntry.setIndexNames((0,_D,_E),(0,_B,_H))
if mibBuilder.loadTexts:cfcpmIntervalPortErrorEntry.setStatus(_A)
class _CfcpmiPortErrorIntervalNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_CfcpmiPortErrorIntervalNumber_Type.__name__=_G
_CfcpmiPortErrorIntervalNumber_Object=MibTableColumn
cfcpmiPortErrorIntervalNumber=_CfcpmiPortErrorIntervalNumber_Object((1,3,6,1,4,1,9,9,99997,1,2,3,1,1),_CfcpmiPortErrorIntervalNumber_Type())
cfcpmiPortErrorIntervalNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cfcpmiPortErrorIntervalNumber.setStatus(_A)
_CfcpmiPortRxLinkResets_Type=PerfIntervalCount
_CfcpmiPortRxLinkResets_Object=MibTableColumn
cfcpmiPortRxLinkResets=_CfcpmiPortRxLinkResets_Object((1,3,6,1,4,1,9,9,99997,1,2,3,1,2),_CfcpmiPortRxLinkResets_Type())
cfcpmiPortRxLinkResets.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmiPortRxLinkResets.setStatus(_A)
_CfcpmiPortTxLinkResets_Type=PerfIntervalCount
_CfcpmiPortTxLinkResets_Object=MibTableColumn
cfcpmiPortTxLinkResets=_CfcpmiPortTxLinkResets_Object((1,3,6,1,4,1,9,9,99997,1,2,3,1,3),_CfcpmiPortTxLinkResets_Type())
cfcpmiPortTxLinkResets.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmiPortTxLinkResets.setStatus(_A)
_CfcpmiPortLinkResets_Type=PerfIntervalCount
_CfcpmiPortLinkResets_Object=MibTableColumn
cfcpmiPortLinkResets=_CfcpmiPortLinkResets_Object((1,3,6,1,4,1,9,9,99997,1,2,3,1,4),_CfcpmiPortLinkResets_Type())
cfcpmiPortLinkResets.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmiPortLinkResets.setStatus(_A)
_CfcpmiPortRxOfflineSequences_Type=PerfIntervalCount
_CfcpmiPortRxOfflineSequences_Object=MibTableColumn
cfcpmiPortRxOfflineSequences=_CfcpmiPortRxOfflineSequences_Object((1,3,6,1,4,1,9,9,99997,1,2,3,1,5),_CfcpmiPortRxOfflineSequences_Type())
cfcpmiPortRxOfflineSequences.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmiPortRxOfflineSequences.setStatus(_A)
_CfcpmiPortTxOfflineSequences_Type=PerfIntervalCount
_CfcpmiPortTxOfflineSequences_Object=MibTableColumn
cfcpmiPortTxOfflineSequences=_CfcpmiPortTxOfflineSequences_Object((1,3,6,1,4,1,9,9,99997,1,2,3,1,6),_CfcpmiPortTxOfflineSequences_Type())
cfcpmiPortTxOfflineSequences.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmiPortTxOfflineSequences.setStatus(_A)
_CfcpmiPortLinkFailures_Type=PerfIntervalCount
_CfcpmiPortLinkFailures_Object=MibTableColumn
cfcpmiPortLinkFailures=_CfcpmiPortLinkFailures_Object((1,3,6,1,4,1,9,9,99997,1,2,3,1,7),_CfcpmiPortLinkFailures_Type())
cfcpmiPortLinkFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmiPortLinkFailures.setStatus(_A)
_CfcpmiPortSynchLosses_Type=PerfIntervalCount
_CfcpmiPortSynchLosses_Object=MibTableColumn
cfcpmiPortSynchLosses=_CfcpmiPortSynchLosses_Object((1,3,6,1,4,1,9,9,99997,1,2,3,1,8),_CfcpmiPortSynchLosses_Type())
cfcpmiPortSynchLosses.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmiPortSynchLosses.setStatus(_A)
_CfcpmiPortSignalLosses_Type=PerfIntervalCount
_CfcpmiPortSignalLosses_Object=MibTableColumn
cfcpmiPortSignalLosses=_CfcpmiPortSignalLosses_Object((1,3,6,1,4,1,9,9,99997,1,2,3,1,9),_CfcpmiPortSignalLosses_Type())
cfcpmiPortSignalLosses.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmiPortSignalLosses.setStatus(_A)
_CfcpmiPortPrimSeqProtocolErrors_Type=PerfIntervalCount
_CfcpmiPortPrimSeqProtocolErrors_Object=MibTableColumn
cfcpmiPortPrimSeqProtocolErrors=_CfcpmiPortPrimSeqProtocolErrors_Object((1,3,6,1,4,1,9,9,99997,1,2,3,1,10),_CfcpmiPortPrimSeqProtocolErrors_Type())
cfcpmiPortPrimSeqProtocolErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmiPortPrimSeqProtocolErrors.setStatus(_A)
_CfcpmiPortInvalidTxWords_Type=PerfIntervalCount
_CfcpmiPortInvalidTxWords_Object=MibTableColumn
cfcpmiPortInvalidTxWords=_CfcpmiPortInvalidTxWords_Object((1,3,6,1,4,1,9,9,99997,1,2,3,1,11),_CfcpmiPortInvalidTxWords_Type())
cfcpmiPortInvalidTxWords.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmiPortInvalidTxWords.setStatus(_A)
_CfcpmiPortInvalidCRCs_Type=PerfIntervalCount
_CfcpmiPortInvalidCRCs_Object=MibTableColumn
cfcpmiPortInvalidCRCs=_CfcpmiPortInvalidCRCs_Object((1,3,6,1,4,1,9,9,99997,1,2,3,1,12),_CfcpmiPortInvalidCRCs_Type())
cfcpmiPortInvalidCRCs.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmiPortInvalidCRCs.setStatus(_A)
_CfcpmiPortInvalidOrderedSets_Type=PerfIntervalCount
_CfcpmiPortInvalidOrderedSets_Object=MibTableColumn
cfcpmiPortInvalidOrderedSets=_CfcpmiPortInvalidOrderedSets_Object((1,3,6,1,4,1,9,9,99997,1,2,3,1,13),_CfcpmiPortInvalidOrderedSets_Type())
cfcpmiPortInvalidOrderedSets.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmiPortInvalidOrderedSets.setStatus(_A)
_CfcpmiPortFramesTooLong_Type=PerfIntervalCount
_CfcpmiPortFramesTooLong_Object=MibTableColumn
cfcpmiPortFramesTooLong=_CfcpmiPortFramesTooLong_Object((1,3,6,1,4,1,9,9,99997,1,2,3,1,14),_CfcpmiPortFramesTooLong_Type())
cfcpmiPortFramesTooLong.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmiPortFramesTooLong.setStatus(_A)
_CfcpmiPortTruncatedFrames_Type=PerfIntervalCount
_CfcpmiPortTruncatedFrames_Object=MibTableColumn
cfcpmiPortTruncatedFrames=_CfcpmiPortTruncatedFrames_Object((1,3,6,1,4,1,9,9,99997,1,2,3,1,15),_CfcpmiPortTruncatedFrames_Type())
cfcpmiPortTruncatedFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmiPortTruncatedFrames.setStatus(_A)
_CfcpmiPortAddressErrors_Type=PerfIntervalCount
_CfcpmiPortAddressErrors_Object=MibTableColumn
cfcpmiPortAddressErrors=_CfcpmiPortAddressErrors_Object((1,3,6,1,4,1,9,9,99997,1,2,3,1,16),_CfcpmiPortAddressErrors_Type())
cfcpmiPortAddressErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmiPortAddressErrors.setStatus(_A)
_CfcpmiPortDelimiterErrors_Type=PerfIntervalCount
_CfcpmiPortDelimiterErrors_Object=MibTableColumn
cfcpmiPortDelimiterErrors=_CfcpmiPortDelimiterErrors_Object((1,3,6,1,4,1,9,9,99997,1,2,3,1,17),_CfcpmiPortDelimiterErrors_Type())
cfcpmiPortDelimiterErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmiPortDelimiterErrors.setStatus(_A)
_CfcpmiPortEncDisparityErrors_Type=PerfIntervalCount
_CfcpmiPortEncDisparityErrors_Object=MibTableColumn
cfcpmiPortEncDisparityErrors=_CfcpmiPortEncDisparityErrors_Object((1,3,6,1,4,1,9,9,99997,1,2,3,1,18),_CfcpmiPortEncDisparityErrors_Type())
cfcpmiPortEncDisparityErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmiPortEncDisparityErrors.setStatus(_A)
_CfcpmiPortOtherErrors_Type=PerfIntervalCount
_CfcpmiPortOtherErrors_Object=MibTableColumn
cfcpmiPortOtherErrors=_CfcpmiPortOtherErrors_Object((1,3,6,1,4,1,9,9,99997,1,2,3,1,19),_CfcpmiPortOtherErrors_Type())
cfcpmiPortOtherErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmiPortOtherErrors.setStatus(_A)
_CfcpmiPortValidData_Type=TruthValue
_CfcpmiPortValidData_Object=MibTableColumn
cfcpmiPortValidData=_CfcpmiPortValidData_Object((1,3,6,1,4,1,9,9,99997,1,2,3,1,20),_CfcpmiPortValidData_Type())
cfcpmiPortValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:cfcpmiPortValidData.setStatus(_A)
_CiscoFcPmMIBConform_ObjectIdentity=ObjectIdentity
ciscoFcPmMIBConform=_CiscoFcPmMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,99997,2))
_CfcpmMibCompliances_ObjectIdentity=ObjectIdentity
cfcpmMibCompliances=_CfcpmMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,99997,2,1))
_CfcpmMibGroups_ObjectIdentity=ObjectIdentity
cfcpmMibGroups=_CfcpmMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,99997,2,2))
cfcpmPortStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,99997,2,2,1))
cfcpmPortStatusGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:cfcpmPortStatusGroup.setStatus(_A)
cfcpmMandatoryGroup=ObjectGroup((1,3,6,1,4,1,9,9,99997,2,2,2))
cfcpmMandatoryGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:cfcpmMandatoryGroup.setStatus(_A)
cfcpmOptionalGroup=ObjectGroup((1,3,6,1,4,1,9,9,99997,2,2,3))
cfcpmOptionalGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:cfcpmOptionalGroup.setStatus(_A)
cfcpmMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,99997,2,1,1))
cfcpmMibCompliance.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:cfcpmMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoFcPmMIB':ciscoFcPmMIB,'ciscoFcPmMIBNotifs':ciscoFcPmMIBNotifs,'ciscoFcPmMIBObjects':ciscoFcPmMIBObjects,'cfcpmPortPerfStatus':cfcpmPortPerfStatus,'cfcpmPortPerfStatusTable':cfcpmPortPerfStatusTable,'cfcpmPortPerfStatusEntry':cfcpmPortPerfStatusEntry,_I:cfcpmTimeElapsed,_J:cfcpmValidIntervals,_K:cfcpmInvalidIntervals,'cfcpmPortErrorStatusBlock':cfcpmPortErrorStatusBlock,'cfcpmTotalPortErrorTable':cfcpmTotalPortErrorTable,'cfcpmTotalPortErrorEntry':cfcpmTotalPortErrorEntry,_P:cfcpmtPortRxLinkResets,_Q:cfcpmtPortTxLinkResets,_R:cfcpmtPortLinkResets,_S:cfcpmtPortRxOfflineSequences,_T:cfcpmtPortTxOfflineSequences,_U:cfcpmtPortLinkFailures,_V:cfcpmtPortSynchLosses,_W:cfcpmtPortSignalLosses,_L:cfcpmtPortPrimSeqProtocolErrors,_X:cfcpmtPortInvalidTxWords,_Y:cfcpmtPortInvalidCRCs,_Z:cfcpmtPortInvalidOrderedSets,_a:cfcpmtPortFramesTooLong,_b:cfcpmtPortTruncatedFrames,_c:cfcpmtPortAddressErrors,_d:cfcpmtPortDelimiterErrors,_e:cfcpmtPortEncDisparityErrors,_f:cfcpmtPortOtherErrors,'cfcpmCurrentPortErrorTable':cfcpmCurrentPortErrorTable,'cfcpmCurrentPortErrorEntry':cfcpmCurrentPortErrorEntry,_g:cfcpmcPortRxLinkResets,_h:cfcpmcPortTxLinkResets,_i:cfcpmcPortLinkResets,_j:cfcpmcPortRxOfflineSequences,_k:cfcpmcPortTxOfflineSequences,_l:cfcpmcPortLinkFailures,_m:cfcpmcPortSynchLosses,_n:cfcpmcPortSignalLosses,_M:cfcpmcPortPrimSeqProtocolErrors,_o:cfcpmcPortInvalidTxWords,_p:cfcpmcPortInvalidCRCs,_q:cfcpmcPortInvalidOrderedSets,_r:cfcpmcPortFramesTooLong,_s:cfcpmcPortTruncatedFrames,_t:cfcpmcPortAddressErrors,_u:cfcpmcPortDelimiterErrors,_v:cfcpmcPortEncDisparityErrors,_w:cfcpmcPortOtherErrors,'cfcpmIntervalPortErrorTable':cfcpmIntervalPortErrorTable,'cfcpmIntervalPortErrorEntry':cfcpmIntervalPortErrorEntry,_H:cfcpmiPortErrorIntervalNumber,_x:cfcpmiPortRxLinkResets,_y:cfcpmiPortTxLinkResets,_z:cfcpmiPortLinkResets,_A0:cfcpmiPortRxOfflineSequences,_A1:cfcpmiPortTxOfflineSequences,_A2:cfcpmiPortLinkFailures,_A3:cfcpmiPortSynchLosses,_A4:cfcpmiPortSignalLosses,_N:cfcpmiPortPrimSeqProtocolErrors,_A5:cfcpmiPortInvalidTxWords,_A6:cfcpmiPortInvalidCRCs,_A7:cfcpmiPortInvalidOrderedSets,_A8:cfcpmiPortFramesTooLong,_A9:cfcpmiPortTruncatedFrames,_AA:cfcpmiPortAddressErrors,_AB:cfcpmiPortDelimiterErrors,_AC:cfcpmiPortEncDisparityErrors,_AD:cfcpmiPortOtherErrors,_O:cfcpmiPortValidData,'ciscoFcPmMIBConform':ciscoFcPmMIBConform,'cfcpmMibCompliances':cfcpmMibCompliances,'cfcpmMibCompliance':cfcpmMibCompliance,'cfcpmMibGroups':cfcpmMibGroups,_AE:cfcpmPortStatusGroup,_AF:cfcpmMandatoryGroup,_AG:cfcpmOptionalGroup})