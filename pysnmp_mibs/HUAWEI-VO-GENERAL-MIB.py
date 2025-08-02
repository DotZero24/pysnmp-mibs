_T='hwVoOutgoingCalledNumSubstIndex'
_S='hwVoOutgoingCallingNumSubstIndex'
_R='hwVoIncomingCalledNumSubstIndex'
_Q='hwVoIncomingCallingNumSubstIndex'
_P='hwVoMaxCallTableIndex'
_O='hwVoNumSubstRuleIndex'
_N='hwVoDialExpansionSource'
_M='hwVoDialExpansionType'
_L='hwVoLtoPChannel'
_K='hwVoNumSubstIndex'
_J='disable'
_I='enable'
_H='fast'
_G='normal'
_F='OctetString'
_E='HUAWEI-VO-GENERAL-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
voice,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','voice')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hwVoiceGeneralMIB=ModuleIdentity((1,3,6,1,4,1,2011,5,25,1,1))
if mibBuilder.loadTexts:hwVoiceGeneralMIB.setRevisions(('2004-04-08 13:45',))
class EntryStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('valid',1),('createRequest',2),('underCreation',3),('invalid',4)))
_HwVoiceGeneralObjects_ObjectIdentity=ObjectIdentity
hwVoiceGeneralObjects=_HwVoiceGeneralObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,25,1,1,1))
_HwVoiceGeneralGroup_ObjectIdentity=ObjectIdentity
hwVoiceGeneralGroup=_HwVoiceGeneralGroup_ObjectIdentity((1,3,6,1,4,1,2011,5,25,1,1,1,1))
class _HwVoGeneralJitterLen_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_HwVoGeneralJitterLen_Type.__name__=_C
_HwVoGeneralJitterLen_Object=MibScalar
hwVoGeneralJitterLen=_HwVoGeneralJitterLen_Object((1,3,6,1,4,1,2011,5,25,1,1,1,1,1),_HwVoGeneralJitterLen_Type())
hwVoGeneralJitterLen.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoGeneralJitterLen.setStatus(_A)
class _HwVoGeneralMatchPolicy_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('long',1),('short',2)))
_HwVoGeneralMatchPolicy_Type.__name__=_C
_HwVoGeneralMatchPolicy_Object=MibScalar
hwVoGeneralMatchPolicy=_HwVoGeneralMatchPolicy_Object((1,3,6,1,4,1,2011,5,25,1,1,1,1,2),_HwVoGeneralMatchPolicy_Type())
hwVoGeneralMatchPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoGeneralMatchPolicy.setStatus(_A)
class _HwVoGeneralSendPerformance_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_HwVoGeneralSendPerformance_Type.__name__=_C
_HwVoGeneralSendPerformance_Object=MibScalar
hwVoGeneralSendPerformance=_HwVoGeneralSendPerformance_Object((1,3,6,1,4,1,2011,5,25,1,1,1,1,3),_HwVoGeneralSendPerformance_Type())
hwVoGeneralSendPerformance.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoGeneralSendPerformance.setStatus(_A)
class _HwVoGeneralReceivePerformance_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_HwVoGeneralReceivePerformance_Type.__name__=_C
_HwVoGeneralReceivePerformance_Object=MibScalar
hwVoGeneralReceivePerformance=_HwVoGeneralReceivePerformance_Object((1,3,6,1,4,1,2011,5,25,1,1,1,1,4),_HwVoGeneralReceivePerformance_Type())
hwVoGeneralReceivePerformance.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoGeneralReceivePerformance.setStatus(_A)
class _HwVoGeneralDataStatistics_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_HwVoGeneralDataStatistics_Type.__name__=_C
_HwVoGeneralDataStatistics_Object=MibScalar
hwVoGeneralDataStatistics=_HwVoGeneralDataStatistics_Object((1,3,6,1,4,1,2011,5,25,1,1,1,1,5),_HwVoGeneralDataStatistics_Type())
hwVoGeneralDataStatistics.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoGeneralDataStatistics.setStatus(_A)
class _HwVoGeneralPacketPrecedence_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HwVoGeneralPacketPrecedence_Type.__name__=_C
_HwVoGeneralPacketPrecedence_Object=MibScalar
hwVoGeneralPacketPrecedence=_HwVoGeneralPacketPrecedence_Object((1,3,6,1,4,1,2011,5,25,1,1,1,1,6),_HwVoGeneralPacketPrecedence_Type())
hwVoGeneralPacketPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoGeneralPacketPrecedence.setStatus(_A)
class _HwVoGeneralDialTerminator_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1))
_HwVoGeneralDialTerminator_Type.__name__=_F
_HwVoGeneralDialTerminator_Object=MibScalar
hwVoGeneralDialTerminator=_HwVoGeneralDialTerminator_Object((1,3,6,1,4,1,2011,5,25,1,1,1,1,7),_HwVoGeneralDialTerminator_Type())
hwVoGeneralDialTerminator.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoGeneralDialTerminator.setStatus(_A)
class _HwVoGeneralCallStart_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_HwVoGeneralCallStart_Type.__name__=_C
_HwVoGeneralCallStart_Object=MibScalar
hwVoGeneralCallStart=_HwVoGeneralCallStart_Object((1,3,6,1,4,1,2011,5,25,1,1,1,1,8),_HwVoGeneralCallStart_Type())
hwVoGeneralCallStart.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoGeneralCallStart.setStatus(_A)
class _HwVoGeneralCalledTunnel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_HwVoGeneralCalledTunnel_Type.__name__=_C
_HwVoGeneralCalledTunnel_Object=MibScalar
hwVoGeneralCalledTunnel=_HwVoGeneralCalledTunnel_Object((1,3,6,1,4,1,2011,5,25,1,1,1,1,9),_HwVoGeneralCalledTunnel_Type())
hwVoGeneralCalledTunnel.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoGeneralCalledTunnel.setStatus(_A)
class _HwVoGeneralSpecialServiceEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_HwVoGeneralSpecialServiceEnable_Type.__name__=_C
_HwVoGeneralSpecialServiceEnable_Object=MibScalar
hwVoGeneralSpecialServiceEnable=_HwVoGeneralSpecialServiceEnable_Object((1,3,6,1,4,1,2011,5,25,1,1,1,1,10),_HwVoGeneralSpecialServiceEnable_Type())
hwVoGeneralSpecialServiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoGeneralSpecialServiceEnable.setStatus(_A)
class _HwVoGeneralCallTransferSpecialServiceNumber_Type(OctetString):defaultValue=OctetString('*12*');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_HwVoGeneralCallTransferSpecialServiceNumber_Type.__name__=_F
_HwVoGeneralCallTransferSpecialServiceNumber_Object=MibScalar
hwVoGeneralCallTransferSpecialServiceNumber=_HwVoGeneralCallTransferSpecialServiceNumber_Object((1,3,6,1,4,1,2011,5,25,1,1,1,1,11),_HwVoGeneralCallTransferSpecialServiceNumber_Type())
hwVoGeneralCallTransferSpecialServiceNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoGeneralCallTransferSpecialServiceNumber.setStatus(_A)
class _HwVoGeneralPeerSearchStop_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_HwVoGeneralPeerSearchStop_Type.__name__=_C
_HwVoGeneralPeerSearchStop_Object=MibScalar
hwVoGeneralPeerSearchStop=_HwVoGeneralPeerSearchStop_Object((1,3,6,1,4,1,2011,5,25,1,1,1,1,12),_HwVoGeneralPeerSearchStop_Type())
hwVoGeneralPeerSearchStop.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoGeneralPeerSearchStop.setStatus(_A)
class _HwVoGeneralPeerSelectOrderRule_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,18))
_HwVoGeneralPeerSelectOrderRule_Type.__name__=_C
_HwVoGeneralPeerSelectOrderRule_Object=MibScalar
hwVoGeneralPeerSelectOrderRule=_HwVoGeneralPeerSelectOrderRule_Object((1,3,6,1,4,1,2011,5,25,1,1,1,1,13),_HwVoGeneralPeerSelectOrderRule_Type())
hwVoGeneralPeerSelectOrderRule.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoGeneralPeerSelectOrderRule.setStatus(_A)
class _HwVoGeneralPeerSelectTypePriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_HwVoGeneralPeerSelectTypePriority_Type.__name__=_C
_HwVoGeneralPeerSelectTypePriority_Object=MibScalar
hwVoGeneralPeerSelectTypePriority=_HwVoGeneralPeerSelectTypePriority_Object((1,3,6,1,4,1,2011,5,25,1,1,1,1,14),_HwVoGeneralPeerSelectTypePriority_Type())
hwVoGeneralPeerSelectTypePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoGeneralPeerSelectTypePriority.setStatus(_A)
_HwVoLtoPTable_Object=MibTable
hwVoLtoPTable=_HwVoLtoPTable_Object((1,3,6,1,4,1,2011,5,25,1,1,1,2))
if mibBuilder.loadTexts:hwVoLtoPTable.setStatus(_A)
_HwVoLtoPEntry_Object=MibTableRow
hwVoLtoPEntry=_HwVoLtoPEntry_Object((1,3,6,1,4,1,2011,5,25,1,1,1,2,1))
hwVoLtoPEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:hwVoLtoPEntry.setStatus(_A)
_HwVoLtoPChannel_Type=Integer32
_HwVoLtoPChannel_Object=MibTableColumn
hwVoLtoPChannel=_HwVoLtoPChannel_Object((1,3,6,1,4,1,2011,5,25,1,1,1,2,1,1),_HwVoLtoPChannel_Type())
hwVoLtoPChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoLtoPChannel.setStatus(_A)
_HwVoLtoPSlot_Type=Integer32
_HwVoLtoPSlot_Object=MibTableColumn
hwVoLtoPSlot=_HwVoLtoPSlot_Object((1,3,6,1,4,1,2011,5,25,1,1,1,2,1,2),_HwVoLtoPSlot_Type())
hwVoLtoPSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoLtoPSlot.setStatus(_A)
_HwVoLtoPPort_Type=Integer32
_HwVoLtoPPort_Object=MibTableColumn
hwVoLtoPPort=_HwVoLtoPPort_Object((1,3,6,1,4,1,2011,5,25,1,1,1,2,1,3),_HwVoLtoPPort_Type())
hwVoLtoPPort.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoLtoPPort.setStatus(_A)
_HwVoLtoPTimeSlot_Type=Integer32
_HwVoLtoPTimeSlot_Object=MibTableColumn
hwVoLtoPTimeSlot=_HwVoLtoPTimeSlot_Object((1,3,6,1,4,1,2011,5,25,1,1,1,2,1,4),_HwVoLtoPTimeSlot_Type())
hwVoLtoPTimeSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoLtoPTimeSlot.setStatus(_A)
class _HwVoLtoPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_HwVoLtoPStatus_Type.__name__=_C
_HwVoLtoPStatus_Object=MibTableColumn
hwVoLtoPStatus=_HwVoLtoPStatus_Object((1,3,6,1,4,1,2011,5,25,1,1,1,2,1,5),_HwVoLtoPStatus_Type())
hwVoLtoPStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoLtoPStatus.setStatus(_A)
class _HwVoLtoPBoardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('fxs2',1),('fxo2',2),('em2',3),('fxs4',4),('fxo4',5),('em4',6),('e1vi',7),('t1vi',8),('sic-fxs1',9),('sic-fxo1',10),('sic-fxs2',11),('sic-fxo2',12)))
_HwVoLtoPBoardType_Type.__name__=_C
_HwVoLtoPBoardType_Object=MibTableColumn
hwVoLtoPBoardType=_HwVoLtoPBoardType_Object((1,3,6,1,4,1,2011,5,25,1,1,1,2,1,6),_HwVoLtoPBoardType_Type())
hwVoLtoPBoardType.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoLtoPBoardType.setStatus(_A)
_HwVoLtoPPortNumber_Type=Integer32
_HwVoLtoPPortNumber_Object=MibTableColumn
hwVoLtoPPortNumber=_HwVoLtoPPortNumber_Object((1,3,6,1,4,1,2011,5,25,1,1,1,2,1,7),_HwVoLtoPPortNumber_Type())
hwVoLtoPPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoLtoPPortNumber.setStatus(_A)
class _HwVoLtoPGroupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,30),ValueRangeConstraint(255,255))
_HwVoLtoPGroupNumber_Type.__name__=_C
_HwVoLtoPGroupNumber_Object=MibTableColumn
hwVoLtoPGroupNumber=_HwVoLtoPGroupNumber_Object((1,3,6,1,4,1,2011,5,25,1,1,1,2,1,8),_HwVoLtoPGroupNumber_Type())
hwVoLtoPGroupNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoLtoPGroupNumber.setStatus(_A)
_HwVoDialExpansionTable_Object=MibTable
hwVoDialExpansionTable=_HwVoDialExpansionTable_Object((1,3,6,1,4,1,2011,5,25,1,1,1,3))
if mibBuilder.loadTexts:hwVoDialExpansionTable.setStatus(_A)
_HwVoDialExpansionEntry_Object=MibTableRow
hwVoDialExpansionEntry=_HwVoDialExpansionEntry_Object((1,3,6,1,4,1,2011,5,25,1,1,1,3,1))
hwVoDialExpansionEntry.setIndexNames((0,_E,_M),(0,_E,_N))
if mibBuilder.loadTexts:hwVoDialExpansionEntry.setStatus(_A)
class _HwVoDialExpansionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('callin',0),('callout',1)))
_HwVoDialExpansionType_Type.__name__=_C
_HwVoDialExpansionType_Object=MibTableColumn
hwVoDialExpansionType=_HwVoDialExpansionType_Object((1,3,6,1,4,1,2011,5,25,1,1,1,3,1,1),_HwVoDialExpansionType_Type())
hwVoDialExpansionType.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoDialExpansionType.setStatus(_A)
class _HwVoDialExpansionSource_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HwVoDialExpansionSource_Type.__name__=_F
_HwVoDialExpansionSource_Object=MibTableColumn
hwVoDialExpansionSource=_HwVoDialExpansionSource_Object((1,3,6,1,4,1,2011,5,25,1,1,1,3,1,2),_HwVoDialExpansionSource_Type())
hwVoDialExpansionSource.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoDialExpansionSource.setStatus(_A)
class _HwVoDialExpansionTarget_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HwVoDialExpansionTarget_Type.__name__=_F
_HwVoDialExpansionTarget_Object=MibTableColumn
hwVoDialExpansionTarget=_HwVoDialExpansionTarget_Object((1,3,6,1,4,1,2011,5,25,1,1,1,3,1,3),_HwVoDialExpansionTarget_Type())
hwVoDialExpansionTarget.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDialExpansionTarget.setStatus(_A)
_HwVoDialExpansionRowStatus_Type=EntryStatus
_HwVoDialExpansionRowStatus_Object=MibTableColumn
hwVoDialExpansionRowStatus=_HwVoDialExpansionRowStatus_Object((1,3,6,1,4,1,2011,5,25,1,1,1,3,1,4),_HwVoDialExpansionRowStatus_Type())
hwVoDialExpansionRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoDialExpansionRowStatus.setStatus(_A)
_HwVoiceNumberSubstGroup_ObjectIdentity=ObjectIdentity
hwVoiceNumberSubstGroup=_HwVoiceNumberSubstGroup_ObjectIdentity((1,3,6,1,4,1,2011,5,25,1,1,1,4))
_HwVoNumSubstTable_Object=MibTable
hwVoNumSubstTable=_HwVoNumSubstTable_Object((1,3,6,1,4,1,2011,5,25,1,1,1,4,1))
if mibBuilder.loadTexts:hwVoNumSubstTable.setStatus(_A)
_HwVoNumSubstEntry_Object=MibTableRow
hwVoNumSubstEntry=_HwVoNumSubstEntry_Object((1,3,6,1,4,1,2011,5,25,1,1,1,4,1,1))
hwVoNumSubstEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:hwVoNumSubstEntry.setStatus(_A)
class _HwVoNumSubstIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HwVoNumSubstIndex_Type.__name__=_C
_HwVoNumSubstIndex_Object=MibTableColumn
hwVoNumSubstIndex=_HwVoNumSubstIndex_Object((1,3,6,1,4,1,2011,5,25,1,1,1,4,1,1,1),_HwVoNumSubstIndex_Type())
hwVoNumSubstIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoNumSubstIndex.setStatus(_A)
class _HwVoNumSubstFirstRule_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127),ValueRangeConstraint(65535,65535))
_HwVoNumSubstFirstRule_Type.__name__=_C
_HwVoNumSubstFirstRule_Object=MibTableColumn
hwVoNumSubstFirstRule=_HwVoNumSubstFirstRule_Object((1,3,6,1,4,1,2011,5,25,1,1,1,4,1,1,2),_HwVoNumSubstFirstRule_Type())
hwVoNumSubstFirstRule.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoNumSubstFirstRule.setStatus(_A)
class _HwVoNumSubstDotMatchRule_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('end-only',1),('left-right',2),('right-left',3)))
_HwVoNumSubstDotMatchRule_Type.__name__=_C
_HwVoNumSubstDotMatchRule_Object=MibTableColumn
hwVoNumSubstDotMatchRule=_HwVoNumSubstDotMatchRule_Object((1,3,6,1,4,1,2011,5,25,1,1,1,4,1,1,3),_HwVoNumSubstDotMatchRule_Type())
hwVoNumSubstDotMatchRule.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoNumSubstDotMatchRule.setStatus(_A)
_HwVoNumSubstRowStatus_Type=EntryStatus
_HwVoNumSubstRowStatus_Object=MibTableColumn
hwVoNumSubstRowStatus=_HwVoNumSubstRowStatus_Object((1,3,6,1,4,1,2011,5,25,1,1,1,4,1,1,4),_HwVoNumSubstRowStatus_Type())
hwVoNumSubstRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoNumSubstRowStatus.setStatus(_A)
_HwVoNumSubstRuleTable_Object=MibTable
hwVoNumSubstRuleTable=_HwVoNumSubstRuleTable_Object((1,3,6,1,4,1,2011,5,25,1,1,1,4,2))
if mibBuilder.loadTexts:hwVoNumSubstRuleTable.setStatus(_A)
_HwVoNumSubstRuleEntry_Object=MibTableRow
hwVoNumSubstRuleEntry=_HwVoNumSubstRuleEntry_Object((1,3,6,1,4,1,2011,5,25,1,1,1,4,2,1))
hwVoNumSubstRuleEntry.setIndexNames((0,_E,_K),(0,_E,_O))
if mibBuilder.loadTexts:hwVoNumSubstRuleEntry.setStatus(_A)
class _HwVoNumSubstRuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_HwVoNumSubstRuleIndex_Type.__name__=_C
_HwVoNumSubstRuleIndex_Object=MibTableColumn
hwVoNumSubstRuleIndex=_HwVoNumSubstRuleIndex_Object((1,3,6,1,4,1,2011,5,25,1,1,1,4,2,1,1),_HwVoNumSubstRuleIndex_Type())
hwVoNumSubstRuleIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoNumSubstRuleIndex.setStatus(_A)
class _HwVoNumSubstRuleInputFormat_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HwVoNumSubstRuleInputFormat_Type.__name__=_F
_HwVoNumSubstRuleInputFormat_Object=MibTableColumn
hwVoNumSubstRuleInputFormat=_HwVoNumSubstRuleInputFormat_Object((1,3,6,1,4,1,2011,5,25,1,1,1,4,2,1,2),_HwVoNumSubstRuleInputFormat_Type())
hwVoNumSubstRuleInputFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoNumSubstRuleInputFormat.setStatus(_A)
class _HwVoNumSubstRuleOutputFormat_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HwVoNumSubstRuleOutputFormat_Type.__name__=_F
_HwVoNumSubstRuleOutputFormat_Object=MibTableColumn
hwVoNumSubstRuleOutputFormat=_HwVoNumSubstRuleOutputFormat_Object((1,3,6,1,4,1,2011,5,25,1,1,1,4,2,1,3),_HwVoNumSubstRuleOutputFormat_Type())
hwVoNumSubstRuleOutputFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoNumSubstRuleOutputFormat.setStatus(_A)
_HwVoNumSubstRuleRowStatus_Type=EntryStatus
_HwVoNumSubstRuleRowStatus_Object=MibTableColumn
hwVoNumSubstRuleRowStatus=_HwVoNumSubstRuleRowStatus_Object((1,3,6,1,4,1,2011,5,25,1,1,1,4,2,1,4),_HwVoNumSubstRuleRowStatus_Type())
hwVoNumSubstRuleRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoNumSubstRuleRowStatus.setStatus(_A)
_HwVoMaxCallTable_Object=MibTable
hwVoMaxCallTable=_HwVoMaxCallTable_Object((1,3,6,1,4,1,2011,5,25,1,1,1,5))
if mibBuilder.loadTexts:hwVoMaxCallTable.setStatus(_A)
_HwVoMaxCallEntry_Object=MibTableRow
hwVoMaxCallEntry=_HwVoMaxCallEntry_Object((1,3,6,1,4,1,2011,5,25,1,1,1,5,1))
hwVoMaxCallEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:hwVoMaxCallEntry.setStatus(_A)
class _HwVoMaxCallTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HwVoMaxCallTableIndex_Type.__name__=_C
_HwVoMaxCallTableIndex_Object=MibTableColumn
hwVoMaxCallTableIndex=_HwVoMaxCallTableIndex_Object((1,3,6,1,4,1,2011,5,25,1,1,1,5,1,1),_HwVoMaxCallTableIndex_Type())
hwVoMaxCallTableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoMaxCallTableIndex.setStatus(_A)
class _HwVoMaxCallValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_HwVoMaxCallValue_Type.__name__=_C
_HwVoMaxCallValue_Object=MibTableColumn
hwVoMaxCallValue=_HwVoMaxCallValue_Object((1,3,6,1,4,1,2011,5,25,1,1,1,5,1,2),_HwVoMaxCallValue_Type())
hwVoMaxCallValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoMaxCallValue.setStatus(_A)
_HwVoMaxCallTableRowStatus_Type=EntryStatus
_HwVoMaxCallTableRowStatus_Object=MibTableColumn
hwVoMaxCallTableRowStatus=_HwVoMaxCallTableRowStatus_Object((1,3,6,1,4,1,2011,5,25,1,1,1,5,1,3),_HwVoMaxCallTableRowStatus_Type())
hwVoMaxCallTableRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoMaxCallTableRowStatus.setStatus(_A)
_HwVoIncomingCallingNumSubstTable_Object=MibTable
hwVoIncomingCallingNumSubstTable=_HwVoIncomingCallingNumSubstTable_Object((1,3,6,1,4,1,2011,5,25,1,1,1,6))
if mibBuilder.loadTexts:hwVoIncomingCallingNumSubstTable.setStatus(_A)
_HwVoIncomingCallingNumSubstEntry_Object=MibTableRow
hwVoIncomingCallingNumSubstEntry=_HwVoIncomingCallingNumSubstEntry_Object((1,3,6,1,4,1,2011,5,25,1,1,1,6,1))
hwVoIncomingCallingNumSubstEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:hwVoIncomingCallingNumSubstEntry.setStatus(_A)
class _HwVoIncomingCallingNumSubstIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HwVoIncomingCallingNumSubstIndex_Type.__name__=_C
_HwVoIncomingCallingNumSubstIndex_Object=MibTableColumn
hwVoIncomingCallingNumSubstIndex=_HwVoIncomingCallingNumSubstIndex_Object((1,3,6,1,4,1,2011,5,25,1,1,1,6,1,1),_HwVoIncomingCallingNumSubstIndex_Type())
hwVoIncomingCallingNumSubstIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoIncomingCallingNumSubstIndex.setStatus(_A)
_HwVoIncomingCallingNumSubstRowStatus_Type=EntryStatus
_HwVoIncomingCallingNumSubstRowStatus_Object=MibTableColumn
hwVoIncomingCallingNumSubstRowStatus=_HwVoIncomingCallingNumSubstRowStatus_Object((1,3,6,1,4,1,2011,5,25,1,1,1,6,1,2),_HwVoIncomingCallingNumSubstRowStatus_Type())
hwVoIncomingCallingNumSubstRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoIncomingCallingNumSubstRowStatus.setStatus(_A)
_HwVoIncomingCalledNumSubstTable_Object=MibTable
hwVoIncomingCalledNumSubstTable=_HwVoIncomingCalledNumSubstTable_Object((1,3,6,1,4,1,2011,5,25,1,1,1,7))
if mibBuilder.loadTexts:hwVoIncomingCalledNumSubstTable.setStatus(_A)
_HwVoIncomingCalledNumSubstEntry_Object=MibTableRow
hwVoIncomingCalledNumSubstEntry=_HwVoIncomingCalledNumSubstEntry_Object((1,3,6,1,4,1,2011,5,25,1,1,1,7,1))
hwVoIncomingCalledNumSubstEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:hwVoIncomingCalledNumSubstEntry.setStatus(_A)
class _HwVoIncomingCalledNumSubstIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HwVoIncomingCalledNumSubstIndex_Type.__name__=_C
_HwVoIncomingCalledNumSubstIndex_Object=MibTableColumn
hwVoIncomingCalledNumSubstIndex=_HwVoIncomingCalledNumSubstIndex_Object((1,3,6,1,4,1,2011,5,25,1,1,1,7,1,1),_HwVoIncomingCalledNumSubstIndex_Type())
hwVoIncomingCalledNumSubstIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoIncomingCalledNumSubstIndex.setStatus(_A)
_HwVoIncomingCalledNumSubstRowStatus_Type=EntryStatus
_HwVoIncomingCalledNumSubstRowStatus_Object=MibTableColumn
hwVoIncomingCalledNumSubstRowStatus=_HwVoIncomingCalledNumSubstRowStatus_Object((1,3,6,1,4,1,2011,5,25,1,1,1,7,1,2),_HwVoIncomingCalledNumSubstRowStatus_Type())
hwVoIncomingCalledNumSubstRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoIncomingCalledNumSubstRowStatus.setStatus(_A)
_HwVoOutgoingCallingNumSubstTable_Object=MibTable
hwVoOutgoingCallingNumSubstTable=_HwVoOutgoingCallingNumSubstTable_Object((1,3,6,1,4,1,2011,5,25,1,1,1,8))
if mibBuilder.loadTexts:hwVoOutgoingCallingNumSubstTable.setStatus(_A)
_HwVoOutgoingCallingNumSubstEntry_Object=MibTableRow
hwVoOutgoingCallingNumSubstEntry=_HwVoOutgoingCallingNumSubstEntry_Object((1,3,6,1,4,1,2011,5,25,1,1,1,8,1))
hwVoOutgoingCallingNumSubstEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:hwVoOutgoingCallingNumSubstEntry.setStatus(_A)
class _HwVoOutgoingCallingNumSubstIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HwVoOutgoingCallingNumSubstIndex_Type.__name__=_C
_HwVoOutgoingCallingNumSubstIndex_Object=MibTableColumn
hwVoOutgoingCallingNumSubstIndex=_HwVoOutgoingCallingNumSubstIndex_Object((1,3,6,1,4,1,2011,5,25,1,1,1,8,1,1),_HwVoOutgoingCallingNumSubstIndex_Type())
hwVoOutgoingCallingNumSubstIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoOutgoingCallingNumSubstIndex.setStatus(_A)
_HwVoOutgoingCallingNumSubstRowStatus_Type=EntryStatus
_HwVoOutgoingCallingNumSubstRowStatus_Object=MibTableColumn
hwVoOutgoingCallingNumSubstRowStatus=_HwVoOutgoingCallingNumSubstRowStatus_Object((1,3,6,1,4,1,2011,5,25,1,1,1,8,1,2),_HwVoOutgoingCallingNumSubstRowStatus_Type())
hwVoOutgoingCallingNumSubstRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoOutgoingCallingNumSubstRowStatus.setStatus(_A)
_HwVoOutgoingCalledNumSubstTable_Object=MibTable
hwVoOutgoingCalledNumSubstTable=_HwVoOutgoingCalledNumSubstTable_Object((1,3,6,1,4,1,2011,5,25,1,1,1,9))
if mibBuilder.loadTexts:hwVoOutgoingCalledNumSubstTable.setStatus(_A)
_HwVoOutgoingCalledNumSubstEntry_Object=MibTableRow
hwVoOutgoingCalledNumSubstEntry=_HwVoOutgoingCalledNumSubstEntry_Object((1,3,6,1,4,1,2011,5,25,1,1,1,9,1))
hwVoOutgoingCalledNumSubstEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:hwVoOutgoingCalledNumSubstEntry.setStatus(_A)
class _HwVoOutgoingCalledNumSubstIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HwVoOutgoingCalledNumSubstIndex_Type.__name__=_C
_HwVoOutgoingCalledNumSubstIndex_Object=MibTableColumn
hwVoOutgoingCalledNumSubstIndex=_HwVoOutgoingCalledNumSubstIndex_Object((1,3,6,1,4,1,2011,5,25,1,1,1,9,1,1),_HwVoOutgoingCalledNumSubstIndex_Type())
hwVoOutgoingCalledNumSubstIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hwVoOutgoingCalledNumSubstIndex.setStatus(_A)
_HwVoOutgoingCalledNumSubstRowStatus_Type=EntryStatus
_HwVoOutgoingCalledNumSubstRowStatus_Object=MibTableColumn
hwVoOutgoingCalledNumSubstRowStatus=_HwVoOutgoingCalledNumSubstRowStatus_Object((1,3,6,1,4,1,2011,5,25,1,1,1,9,1,2),_HwVoOutgoingCalledNumSubstRowStatus_Type())
hwVoOutgoingCalledNumSubstRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVoOutgoingCalledNumSubstRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'EntryStatus':EntryStatus,'hwVoiceGeneralMIB':hwVoiceGeneralMIB,'hwVoiceGeneralObjects':hwVoiceGeneralObjects,'hwVoiceGeneralGroup':hwVoiceGeneralGroup,'hwVoGeneralJitterLen':hwVoGeneralJitterLen,'hwVoGeneralMatchPolicy':hwVoGeneralMatchPolicy,'hwVoGeneralSendPerformance':hwVoGeneralSendPerformance,'hwVoGeneralReceivePerformance':hwVoGeneralReceivePerformance,'hwVoGeneralDataStatistics':hwVoGeneralDataStatistics,'hwVoGeneralPacketPrecedence':hwVoGeneralPacketPrecedence,'hwVoGeneralDialTerminator':hwVoGeneralDialTerminator,'hwVoGeneralCallStart':hwVoGeneralCallStart,'hwVoGeneralCalledTunnel':hwVoGeneralCalledTunnel,'hwVoGeneralSpecialServiceEnable':hwVoGeneralSpecialServiceEnable,'hwVoGeneralCallTransferSpecialServiceNumber':hwVoGeneralCallTransferSpecialServiceNumber,'hwVoGeneralPeerSearchStop':hwVoGeneralPeerSearchStop,'hwVoGeneralPeerSelectOrderRule':hwVoGeneralPeerSelectOrderRule,'hwVoGeneralPeerSelectTypePriority':hwVoGeneralPeerSelectTypePriority,'hwVoLtoPTable':hwVoLtoPTable,'hwVoLtoPEntry':hwVoLtoPEntry,_L:hwVoLtoPChannel,'hwVoLtoPSlot':hwVoLtoPSlot,'hwVoLtoPPort':hwVoLtoPPort,'hwVoLtoPTimeSlot':hwVoLtoPTimeSlot,'hwVoLtoPStatus':hwVoLtoPStatus,'hwVoLtoPBoardType':hwVoLtoPBoardType,'hwVoLtoPPortNumber':hwVoLtoPPortNumber,'hwVoLtoPGroupNumber':hwVoLtoPGroupNumber,'hwVoDialExpansionTable':hwVoDialExpansionTable,'hwVoDialExpansionEntry':hwVoDialExpansionEntry,_M:hwVoDialExpansionType,_N:hwVoDialExpansionSource,'hwVoDialExpansionTarget':hwVoDialExpansionTarget,'hwVoDialExpansionRowStatus':hwVoDialExpansionRowStatus,'hwVoiceNumberSubstGroup':hwVoiceNumberSubstGroup,'hwVoNumSubstTable':hwVoNumSubstTable,'hwVoNumSubstEntry':hwVoNumSubstEntry,_K:hwVoNumSubstIndex,'hwVoNumSubstFirstRule':hwVoNumSubstFirstRule,'hwVoNumSubstDotMatchRule':hwVoNumSubstDotMatchRule,'hwVoNumSubstRowStatus':hwVoNumSubstRowStatus,'hwVoNumSubstRuleTable':hwVoNumSubstRuleTable,'hwVoNumSubstRuleEntry':hwVoNumSubstRuleEntry,_O:hwVoNumSubstRuleIndex,'hwVoNumSubstRuleInputFormat':hwVoNumSubstRuleInputFormat,'hwVoNumSubstRuleOutputFormat':hwVoNumSubstRuleOutputFormat,'hwVoNumSubstRuleRowStatus':hwVoNumSubstRuleRowStatus,'hwVoMaxCallTable':hwVoMaxCallTable,'hwVoMaxCallEntry':hwVoMaxCallEntry,_P:hwVoMaxCallTableIndex,'hwVoMaxCallValue':hwVoMaxCallValue,'hwVoMaxCallTableRowStatus':hwVoMaxCallTableRowStatus,'hwVoIncomingCallingNumSubstTable':hwVoIncomingCallingNumSubstTable,'hwVoIncomingCallingNumSubstEntry':hwVoIncomingCallingNumSubstEntry,_Q:hwVoIncomingCallingNumSubstIndex,'hwVoIncomingCallingNumSubstRowStatus':hwVoIncomingCallingNumSubstRowStatus,'hwVoIncomingCalledNumSubstTable':hwVoIncomingCalledNumSubstTable,'hwVoIncomingCalledNumSubstEntry':hwVoIncomingCalledNumSubstEntry,_R:hwVoIncomingCalledNumSubstIndex,'hwVoIncomingCalledNumSubstRowStatus':hwVoIncomingCalledNumSubstRowStatus,'hwVoOutgoingCallingNumSubstTable':hwVoOutgoingCallingNumSubstTable,'hwVoOutgoingCallingNumSubstEntry':hwVoOutgoingCallingNumSubstEntry,_S:hwVoOutgoingCallingNumSubstIndex,'hwVoOutgoingCallingNumSubstRowStatus':hwVoOutgoingCallingNumSubstRowStatus,'hwVoOutgoingCalledNumSubstTable':hwVoOutgoingCalledNumSubstTable,'hwVoOutgoingCalledNumSubstEntry':hwVoOutgoingCalledNumSubstEntry,_T:hwVoOutgoingCalledNumSubstIndex,'hwVoOutgoingCalledNumSubstRowStatus':hwVoOutgoingCalledNumSubstRowStatus})