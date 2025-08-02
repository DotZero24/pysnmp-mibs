_O='h3cVoOutCalledNumSubstIndex'
_N='h3cVoOutCallingNumSubstIndex'
_M='h3cVoInCalledNumSubstIndex'
_L='h3cVoInCallingNumSubstIndex'
_K='h3cVoMaxCallTableIndex'
_J='h3cVoNumSubstRuleIndex'
_I='h3cVoNumSubstIndex'
_H='disable'
_G='enable'
_F='not-accessible'
_E='H3C-VOGENERAL-MIB'
_D='read-create'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cVoice,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cVoice')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cVoiceGeneral=ModuleIdentity((1,3,6,1,4,1,2011,10,2,39,1))
if mibBuilder.loadTexts:h3cVoiceGeneral.setRevisions(('2005-03-15 00:00',))
_H3cVoiceGeneralObjects_ObjectIdentity=ObjectIdentity
h3cVoiceGeneralObjects=_H3cVoiceGeneralObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,39,1,1))
class _H3cVoGeneralJitterLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_H3cVoGeneralJitterLen_Type.__name__=_B
_H3cVoGeneralJitterLen_Object=MibScalar
h3cVoGeneralJitterLen=_H3cVoGeneralJitterLen_Object((1,3,6,1,4,1,2011,10,2,39,1,1,1),_H3cVoGeneralJitterLen_Type())
h3cVoGeneralJitterLen.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVoGeneralJitterLen.setStatus(_A)
class _H3cVoGeneralMatchPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('long',1),('short',2)))
_H3cVoGeneralMatchPolicy_Type.__name__=_B
_H3cVoGeneralMatchPolicy_Object=MibScalar
h3cVoGeneralMatchPolicy=_H3cVoGeneralMatchPolicy_Object((1,3,6,1,4,1,2011,10,2,39,1,1,2),_H3cVoGeneralMatchPolicy_Type())
h3cVoGeneralMatchPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVoGeneralMatchPolicy.setStatus(_A)
class _H3cVoGeneralDataStatistics_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_H3cVoGeneralDataStatistics_Type.__name__=_B
_H3cVoGeneralDataStatistics_Object=MibScalar
h3cVoGeneralDataStatistics=_H3cVoGeneralDataStatistics_Object((1,3,6,1,4,1,2011,10,2,39,1,1,5),_H3cVoGeneralDataStatistics_Type())
h3cVoGeneralDataStatistics.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVoGeneralDataStatistics.setStatus(_A)
_H3cVoGeneralDialTerminator_Type=OctetString
_H3cVoGeneralDialTerminator_Object=MibScalar
h3cVoGeneralDialTerminator=_H3cVoGeneralDialTerminator_Object((1,3,6,1,4,1,2011,10,2,39,1,1,7),_H3cVoGeneralDialTerminator_Type())
h3cVoGeneralDialTerminator.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVoGeneralDialTerminator.setStatus(_A)
class _H3cVoGeneralCallStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fast',1),('normal',2)))
_H3cVoGeneralCallStart_Type.__name__=_B
_H3cVoGeneralCallStart_Object=MibScalar
h3cVoGeneralCallStart=_H3cVoGeneralCallStart_Object((1,3,6,1,4,1,2011,10,2,39,1,1,8),_H3cVoGeneralCallStart_Type())
h3cVoGeneralCallStart.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVoGeneralCallStart.setStatus(_A)
class _H3cVoGeneralCalledTunnel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_H3cVoGeneralCalledTunnel_Type.__name__=_B
_H3cVoGeneralCalledTunnel_Object=MibScalar
h3cVoGeneralCalledTunnel=_H3cVoGeneralCalledTunnel_Object((1,3,6,1,4,1,2011,10,2,39,1,1,9),_H3cVoGeneralCalledTunnel_Type())
h3cVoGeneralCalledTunnel.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVoGeneralCalledTunnel.setStatus(_A)
class _H3cVoGeneralSpecialService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_H3cVoGeneralSpecialService_Type.__name__=_B
_H3cVoGeneralSpecialService_Object=MibScalar
h3cVoGeneralSpecialService=_H3cVoGeneralSpecialService_Object((1,3,6,1,4,1,2011,10,2,39,1,1,10),_H3cVoGeneralSpecialService_Type())
h3cVoGeneralSpecialService.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVoGeneralSpecialService.setStatus(_A)
_H3cVoGeneralPeerSearchStop_Type=Integer32
_H3cVoGeneralPeerSearchStop_Object=MibScalar
h3cVoGeneralPeerSearchStop=_H3cVoGeneralPeerSearchStop_Object((1,3,6,1,4,1,2011,10,2,39,1,1,12),_H3cVoGeneralPeerSearchStop_Type())
h3cVoGeneralPeerSearchStop.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVoGeneralPeerSearchStop.setStatus(_A)
class _H3cVoGeneralPeerSelectOrderRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)));namedValues=NamedValues(*(('epr',1),('epl',2),('elp',3),('elr',4),('per',5),('pel',6),('ple',7),('plr',8),('lep',9),('ler',10),('lpe',11),('lpr',12),('er',13),('pr',14),('lr',15),('explicitMatch',16),('priority',17),('random',18),('longestNoUse',19),('ep',20),('el',21),('pe',22),('pl',23),('le',24),('lp',25)))
_H3cVoGeneralPeerSelectOrderRule_Type.__name__=_B
_H3cVoGeneralPeerSelectOrderRule_Object=MibScalar
h3cVoGeneralPeerSelectOrderRule=_H3cVoGeneralPeerSelectOrderRule_Object((1,3,6,1,4,1,2011,10,2,39,1,1,13),_H3cVoGeneralPeerSelectOrderRule_Type())
h3cVoGeneralPeerSelectOrderRule.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVoGeneralPeerSelectOrderRule.setStatus(_A)
class _H3cVoGeneralPeerSelectTypePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('noneType',1),('voipPotsVofr',2),('voipVofrPots',3),('potsVoipVofr',4),('potsVofrVoip',5),('vofrPotsVoip',6),('vofrVoipPots',7)))
_H3cVoGeneralPeerSelectTypePriority_Type.__name__=_B
_H3cVoGeneralPeerSelectTypePriority_Object=MibScalar
h3cVoGeneralPeerSelectTypePriority=_H3cVoGeneralPeerSelectTypePriority_Object((1,3,6,1,4,1,2011,10,2,39,1,1,14),_H3cVoGeneralPeerSelectTypePriority_Type())
h3cVoGeneralPeerSelectTypePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVoGeneralPeerSelectTypePriority.setStatus(_A)
class _H3cVoGeneralDscpSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_H3cVoGeneralDscpSignal_Type.__name__=_B
_H3cVoGeneralDscpSignal_Object=MibScalar
h3cVoGeneralDscpSignal=_H3cVoGeneralDscpSignal_Object((1,3,6,1,4,1,2011,10,2,39,1,1,15),_H3cVoGeneralDscpSignal_Type())
h3cVoGeneralDscpSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVoGeneralDscpSignal.setStatus(_A)
class _H3cVoGeneralDscpMedia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_H3cVoGeneralDscpMedia_Type.__name__=_B
_H3cVoGeneralDscpMedia_Object=MibScalar
h3cVoGeneralDscpMedia=_H3cVoGeneralDscpMedia_Object((1,3,6,1,4,1,2011,10,2,39,1,1,16),_H3cVoGeneralDscpMedia_Type())
h3cVoGeneralDscpMedia.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cVoGeneralDscpMedia.setStatus(_A)
_H3cVoiceNumberSubstGroup_ObjectIdentity=ObjectIdentity
h3cVoiceNumberSubstGroup=_H3cVoiceNumberSubstGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,39,1,4))
_H3cVoNumSubstTable_Object=MibTable
h3cVoNumSubstTable=_H3cVoNumSubstTable_Object((1,3,6,1,4,1,2011,10,2,39,1,4,1))
if mibBuilder.loadTexts:h3cVoNumSubstTable.setStatus(_A)
_H3cVoNumSubstEntry_Object=MibTableRow
h3cVoNumSubstEntry=_H3cVoNumSubstEntry_Object((1,3,6,1,4,1,2011,10,2,39,1,4,1,1))
h3cVoNumSubstEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:h3cVoNumSubstEntry.setStatus(_A)
class _H3cVoNumSubstIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cVoNumSubstIndex_Type.__name__=_B
_H3cVoNumSubstIndex_Object=MibTableColumn
h3cVoNumSubstIndex=_H3cVoNumSubstIndex_Object((1,3,6,1,4,1,2011,10,2,39,1,4,1,1,1),_H3cVoNumSubstIndex_Type())
h3cVoNumSubstIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cVoNumSubstIndex.setStatus(_A)
_H3cVoNumSubstFirstRule_Type=Integer32
_H3cVoNumSubstFirstRule_Object=MibTableColumn
h3cVoNumSubstFirstRule=_H3cVoNumSubstFirstRule_Object((1,3,6,1,4,1,2011,10,2,39,1,4,1,1,2),_H3cVoNumSubstFirstRule_Type())
h3cVoNumSubstFirstRule.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVoNumSubstFirstRule.setStatus(_A)
class _H3cVoNumSubstDotMatchRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('endOnly',1),('leftRight',2),('rightLeft',3)))
_H3cVoNumSubstDotMatchRule_Type.__name__=_B
_H3cVoNumSubstDotMatchRule_Object=MibTableColumn
h3cVoNumSubstDotMatchRule=_H3cVoNumSubstDotMatchRule_Object((1,3,6,1,4,1,2011,10,2,39,1,4,1,1,3),_H3cVoNumSubstDotMatchRule_Type())
h3cVoNumSubstDotMatchRule.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVoNumSubstDotMatchRule.setStatus(_A)
_H3cVoNumSubstRowStatus_Type=RowStatus
_H3cVoNumSubstRowStatus_Object=MibTableColumn
h3cVoNumSubstRowStatus=_H3cVoNumSubstRowStatus_Object((1,3,6,1,4,1,2011,10,2,39,1,4,1,1,4),_H3cVoNumSubstRowStatus_Type())
h3cVoNumSubstRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVoNumSubstRowStatus.setStatus(_A)
_H3cVoNumSubstRuleTable_Object=MibTable
h3cVoNumSubstRuleTable=_H3cVoNumSubstRuleTable_Object((1,3,6,1,4,1,2011,10,2,39,1,4,2))
if mibBuilder.loadTexts:h3cVoNumSubstRuleTable.setStatus(_A)
_H3cVoNumSubstRuleEntry_Object=MibTableRow
h3cVoNumSubstRuleEntry=_H3cVoNumSubstRuleEntry_Object((1,3,6,1,4,1,2011,10,2,39,1,4,2,1))
h3cVoNumSubstRuleEntry.setIndexNames((0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:h3cVoNumSubstRuleEntry.setStatus(_A)
class _H3cVoNumSubstRuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_H3cVoNumSubstRuleIndex_Type.__name__=_B
_H3cVoNumSubstRuleIndex_Object=MibTableColumn
h3cVoNumSubstRuleIndex=_H3cVoNumSubstRuleIndex_Object((1,3,6,1,4,1,2011,10,2,39,1,4,2,1,1),_H3cVoNumSubstRuleIndex_Type())
h3cVoNumSubstRuleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cVoNumSubstRuleIndex.setStatus(_A)
_H3cVoNumSubstRuleInputFormat_Type=OctetString
_H3cVoNumSubstRuleInputFormat_Object=MibTableColumn
h3cVoNumSubstRuleInputFormat=_H3cVoNumSubstRuleInputFormat_Object((1,3,6,1,4,1,2011,10,2,39,1,4,2,1,2),_H3cVoNumSubstRuleInputFormat_Type())
h3cVoNumSubstRuleInputFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVoNumSubstRuleInputFormat.setStatus(_A)
_H3cVoNumSubstRuleOutputFormat_Type=OctetString
_H3cVoNumSubstRuleOutputFormat_Object=MibTableColumn
h3cVoNumSubstRuleOutputFormat=_H3cVoNumSubstRuleOutputFormat_Object((1,3,6,1,4,1,2011,10,2,39,1,4,2,1,3),_H3cVoNumSubstRuleOutputFormat_Type())
h3cVoNumSubstRuleOutputFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVoNumSubstRuleOutputFormat.setStatus(_A)
_H3cVoNumSubstRuleRowStatus_Type=RowStatus
_H3cVoNumSubstRuleRowStatus_Object=MibTableColumn
h3cVoNumSubstRuleRowStatus=_H3cVoNumSubstRuleRowStatus_Object((1,3,6,1,4,1,2011,10,2,39,1,4,2,1,4),_H3cVoNumSubstRuleRowStatus_Type())
h3cVoNumSubstRuleRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVoNumSubstRuleRowStatus.setStatus(_A)
_H3cVoMaxCallTable_Object=MibTable
h3cVoMaxCallTable=_H3cVoMaxCallTable_Object((1,3,6,1,4,1,2011,10,2,39,1,5))
if mibBuilder.loadTexts:h3cVoMaxCallTable.setStatus(_A)
_H3cVoMaxCallEntry_Object=MibTableRow
h3cVoMaxCallEntry=_H3cVoMaxCallEntry_Object((1,3,6,1,4,1,2011,10,2,39,1,5,1))
h3cVoMaxCallEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:h3cVoMaxCallEntry.setStatus(_A)
class _H3cVoMaxCallTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cVoMaxCallTableIndex_Type.__name__=_B
_H3cVoMaxCallTableIndex_Object=MibTableColumn
h3cVoMaxCallTableIndex=_H3cVoMaxCallTableIndex_Object((1,3,6,1,4,1,2011,10,2,39,1,5,1,1),_H3cVoMaxCallTableIndex_Type())
h3cVoMaxCallTableIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cVoMaxCallTableIndex.setStatus(_A)
class _H3cVoMaxCallValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_H3cVoMaxCallValue_Type.__name__=_B
_H3cVoMaxCallValue_Object=MibTableColumn
h3cVoMaxCallValue=_H3cVoMaxCallValue_Object((1,3,6,1,4,1,2011,10,2,39,1,5,1,2),_H3cVoMaxCallValue_Type())
h3cVoMaxCallValue.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVoMaxCallValue.setStatus(_A)
_H3cVoMaxCallTableRowStatus_Type=RowStatus
_H3cVoMaxCallTableRowStatus_Object=MibTableColumn
h3cVoMaxCallTableRowStatus=_H3cVoMaxCallTableRowStatus_Object((1,3,6,1,4,1,2011,10,2,39,1,5,1,3),_H3cVoMaxCallTableRowStatus_Type())
h3cVoMaxCallTableRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVoMaxCallTableRowStatus.setStatus(_A)
_H3cVoInCallingNumSubstTable_Object=MibTable
h3cVoInCallingNumSubstTable=_H3cVoInCallingNumSubstTable_Object((1,3,6,1,4,1,2011,10,2,39,1,6))
if mibBuilder.loadTexts:h3cVoInCallingNumSubstTable.setStatus(_A)
_H3cVoInCallingNumSubstEntry_Object=MibTableRow
h3cVoInCallingNumSubstEntry=_H3cVoInCallingNumSubstEntry_Object((1,3,6,1,4,1,2011,10,2,39,1,6,1))
h3cVoInCallingNumSubstEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:h3cVoInCallingNumSubstEntry.setStatus(_A)
class _H3cVoInCallingNumSubstIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cVoInCallingNumSubstIndex_Type.__name__=_B
_H3cVoInCallingNumSubstIndex_Object=MibTableColumn
h3cVoInCallingNumSubstIndex=_H3cVoInCallingNumSubstIndex_Object((1,3,6,1,4,1,2011,10,2,39,1,6,1,1),_H3cVoInCallingNumSubstIndex_Type())
h3cVoInCallingNumSubstIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cVoInCallingNumSubstIndex.setStatus(_A)
_H3cVoInCallingSubstRowStatus_Type=RowStatus
_H3cVoInCallingSubstRowStatus_Object=MibTableColumn
h3cVoInCallingSubstRowStatus=_H3cVoInCallingSubstRowStatus_Object((1,3,6,1,4,1,2011,10,2,39,1,6,1,2),_H3cVoInCallingSubstRowStatus_Type())
h3cVoInCallingSubstRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVoInCallingSubstRowStatus.setStatus(_A)
_H3cVoInCalledNumSubstTable_Object=MibTable
h3cVoInCalledNumSubstTable=_H3cVoInCalledNumSubstTable_Object((1,3,6,1,4,1,2011,10,2,39,1,7))
if mibBuilder.loadTexts:h3cVoInCalledNumSubstTable.setStatus(_A)
_H3cVoInCalledNumSubstEntry_Object=MibTableRow
h3cVoInCalledNumSubstEntry=_H3cVoInCalledNumSubstEntry_Object((1,3,6,1,4,1,2011,10,2,39,1,7,1))
h3cVoInCalledNumSubstEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:h3cVoInCalledNumSubstEntry.setStatus(_A)
class _H3cVoInCalledNumSubstIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cVoInCalledNumSubstIndex_Type.__name__=_B
_H3cVoInCalledNumSubstIndex_Object=MibTableColumn
h3cVoInCalledNumSubstIndex=_H3cVoInCalledNumSubstIndex_Object((1,3,6,1,4,1,2011,10,2,39,1,7,1,1),_H3cVoInCalledNumSubstIndex_Type())
h3cVoInCalledNumSubstIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cVoInCalledNumSubstIndex.setStatus(_A)
_H3cVoInCalledSubstRowStatus_Type=RowStatus
_H3cVoInCalledSubstRowStatus_Object=MibTableColumn
h3cVoInCalledSubstRowStatus=_H3cVoInCalledSubstRowStatus_Object((1,3,6,1,4,1,2011,10,2,39,1,7,1,2),_H3cVoInCalledSubstRowStatus_Type())
h3cVoInCalledSubstRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVoInCalledSubstRowStatus.setStatus(_A)
_H3cVoOutCallingNumSubstTable_Object=MibTable
h3cVoOutCallingNumSubstTable=_H3cVoOutCallingNumSubstTable_Object((1,3,6,1,4,1,2011,10,2,39,1,8))
if mibBuilder.loadTexts:h3cVoOutCallingNumSubstTable.setStatus(_A)
_H3cVoOutCallingNumSubstEntry_Object=MibTableRow
h3cVoOutCallingNumSubstEntry=_H3cVoOutCallingNumSubstEntry_Object((1,3,6,1,4,1,2011,10,2,39,1,8,1))
h3cVoOutCallingNumSubstEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:h3cVoOutCallingNumSubstEntry.setStatus(_A)
class _H3cVoOutCallingNumSubstIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cVoOutCallingNumSubstIndex_Type.__name__=_B
_H3cVoOutCallingNumSubstIndex_Object=MibTableColumn
h3cVoOutCallingNumSubstIndex=_H3cVoOutCallingNumSubstIndex_Object((1,3,6,1,4,1,2011,10,2,39,1,8,1,1),_H3cVoOutCallingNumSubstIndex_Type())
h3cVoOutCallingNumSubstIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cVoOutCallingNumSubstIndex.setStatus(_A)
_H3cVoOutCallingSubstRowStatus_Type=RowStatus
_H3cVoOutCallingSubstRowStatus_Object=MibTableColumn
h3cVoOutCallingSubstRowStatus=_H3cVoOutCallingSubstRowStatus_Object((1,3,6,1,4,1,2011,10,2,39,1,8,1,2),_H3cVoOutCallingSubstRowStatus_Type())
h3cVoOutCallingSubstRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVoOutCallingSubstRowStatus.setStatus(_A)
_H3cVoOutCalledNumSubstTable_Object=MibTable
h3cVoOutCalledNumSubstTable=_H3cVoOutCalledNumSubstTable_Object((1,3,6,1,4,1,2011,10,2,39,1,9))
if mibBuilder.loadTexts:h3cVoOutCalledNumSubstTable.setStatus(_A)
_H3cVoOutgoingCalledNumSubstEntry_Object=MibTableRow
h3cVoOutgoingCalledNumSubstEntry=_H3cVoOutgoingCalledNumSubstEntry_Object((1,3,6,1,4,1,2011,10,2,39,1,9,1))
h3cVoOutgoingCalledNumSubstEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:h3cVoOutgoingCalledNumSubstEntry.setStatus(_A)
class _H3cVoOutCalledNumSubstIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cVoOutCalledNumSubstIndex_Type.__name__=_B
_H3cVoOutCalledNumSubstIndex_Object=MibTableColumn
h3cVoOutCalledNumSubstIndex=_H3cVoOutCalledNumSubstIndex_Object((1,3,6,1,4,1,2011,10,2,39,1,9,1,1),_H3cVoOutCalledNumSubstIndex_Type())
h3cVoOutCalledNumSubstIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cVoOutCalledNumSubstIndex.setStatus(_A)
_H3cVoOutCalledSubstRowStatus_Type=RowStatus
_H3cVoOutCalledSubstRowStatus_Object=MibTableColumn
h3cVoOutCalledSubstRowStatus=_H3cVoOutCalledSubstRowStatus_Object((1,3,6,1,4,1,2011,10,2,39,1,9,1,2),_H3cVoOutCalledSubstRowStatus_Type())
h3cVoOutCalledSubstRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cVoOutCalledSubstRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'h3cVoiceGeneral':h3cVoiceGeneral,'h3cVoiceGeneralObjects':h3cVoiceGeneralObjects,'h3cVoGeneralJitterLen':h3cVoGeneralJitterLen,'h3cVoGeneralMatchPolicy':h3cVoGeneralMatchPolicy,'h3cVoGeneralDataStatistics':h3cVoGeneralDataStatistics,'h3cVoGeneralDialTerminator':h3cVoGeneralDialTerminator,'h3cVoGeneralCallStart':h3cVoGeneralCallStart,'h3cVoGeneralCalledTunnel':h3cVoGeneralCalledTunnel,'h3cVoGeneralSpecialService':h3cVoGeneralSpecialService,'h3cVoGeneralPeerSearchStop':h3cVoGeneralPeerSearchStop,'h3cVoGeneralPeerSelectOrderRule':h3cVoGeneralPeerSelectOrderRule,'h3cVoGeneralPeerSelectTypePriority':h3cVoGeneralPeerSelectTypePriority,'h3cVoGeneralDscpSignal':h3cVoGeneralDscpSignal,'h3cVoGeneralDscpMedia':h3cVoGeneralDscpMedia,'h3cVoiceNumberSubstGroup':h3cVoiceNumberSubstGroup,'h3cVoNumSubstTable':h3cVoNumSubstTable,'h3cVoNumSubstEntry':h3cVoNumSubstEntry,_I:h3cVoNumSubstIndex,'h3cVoNumSubstFirstRule':h3cVoNumSubstFirstRule,'h3cVoNumSubstDotMatchRule':h3cVoNumSubstDotMatchRule,'h3cVoNumSubstRowStatus':h3cVoNumSubstRowStatus,'h3cVoNumSubstRuleTable':h3cVoNumSubstRuleTable,'h3cVoNumSubstRuleEntry':h3cVoNumSubstRuleEntry,_J:h3cVoNumSubstRuleIndex,'h3cVoNumSubstRuleInputFormat':h3cVoNumSubstRuleInputFormat,'h3cVoNumSubstRuleOutputFormat':h3cVoNumSubstRuleOutputFormat,'h3cVoNumSubstRuleRowStatus':h3cVoNumSubstRuleRowStatus,'h3cVoMaxCallTable':h3cVoMaxCallTable,'h3cVoMaxCallEntry':h3cVoMaxCallEntry,_K:h3cVoMaxCallTableIndex,'h3cVoMaxCallValue':h3cVoMaxCallValue,'h3cVoMaxCallTableRowStatus':h3cVoMaxCallTableRowStatus,'h3cVoInCallingNumSubstTable':h3cVoInCallingNumSubstTable,'h3cVoInCallingNumSubstEntry':h3cVoInCallingNumSubstEntry,_L:h3cVoInCallingNumSubstIndex,'h3cVoInCallingSubstRowStatus':h3cVoInCallingSubstRowStatus,'h3cVoInCalledNumSubstTable':h3cVoInCalledNumSubstTable,'h3cVoInCalledNumSubstEntry':h3cVoInCalledNumSubstEntry,_M:h3cVoInCalledNumSubstIndex,'h3cVoInCalledSubstRowStatus':h3cVoInCalledSubstRowStatus,'h3cVoOutCallingNumSubstTable':h3cVoOutCallingNumSubstTable,'h3cVoOutCallingNumSubstEntry':h3cVoOutCallingNumSubstEntry,_N:h3cVoOutCallingNumSubstIndex,'h3cVoOutCallingSubstRowStatus':h3cVoOutCallingSubstRowStatus,'h3cVoOutCalledNumSubstTable':h3cVoOutCalledNumSubstTable,'h3cVoOutgoingCalledNumSubstEntry':h3cVoOutgoingCalledNumSubstEntry,_O:h3cVoOutCalledNumSubstIndex,'h3cVoOutCalledSubstRowStatus':h3cVoOutCalledSubstRowStatus})