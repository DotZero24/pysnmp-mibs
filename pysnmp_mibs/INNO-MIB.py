_R='trapIntegerParm'
_Q='trapDisplayStringParm'
_P='voiceIfAliasIndex'
_O='voiceIfIndex'
_N='l3Label'
_M='l1BriLabel'
_L='l1PriLabel'
_K='l2Label'
_J='NotificationType'
_I='ifIndex'
_H='IF-MIB'
_G='up'
_F='down'
_E='INNO-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_J,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_J,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_Innovaphone_ObjectIdentity=ObjectIdentity
innovaphone=_Innovaphone_ObjectIdentity((1,3,6,1,4,1,6666))
_Isdn_ObjectIdentity=ObjectIdentity
isdn=_Isdn_ObjectIdentity((1,3,6,1,4,1,6666,1))
_L2Table_Object=MibTable
l2Table=_L2Table_Object((1,3,6,1,4,1,6666,1,1))
if mibBuilder.loadTexts:l2Table.setStatus(_A)
_L2Entry_Object=MibTableRow
l2Entry=_L2Entry_Object((1,3,6,1,4,1,6666,1,1,1))
l2Entry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:l2Entry.setStatus(_A)
class _L2Label_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_L2Label_Type.__name__=_D
_L2Label_Object=MibTableColumn
l2Label=_L2Label_Object((1,3,6,1,4,1,6666,1,1,1,1),_L2Label_Type())
l2Label.setMaxAccess(_B)
if mibBuilder.loadTexts:l2Label.setStatus(_A)
class _L2State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_L2State_Type.__name__=_C
_L2State_Object=MibTableColumn
l2State=_L2State_Object((1,3,6,1,4,1,6666,1,1,1,2),_L2State_Type())
l2State.setMaxAccess(_B)
if mibBuilder.loadTexts:l2State.setStatus(_A)
class _L2Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('te',1),('nt',2)))
_L2Mode_Type.__name__=_C
_L2Mode_Object=MibTableColumn
l2Mode=_L2Mode_Object((1,3,6,1,4,1,6666,1,1,1,3),_L2Mode_Type())
l2Mode.setMaxAccess(_B)
if mibBuilder.loadTexts:l2Mode.setStatus(_A)
class _L1Label_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_L1Label_Type.__name__=_D
_L1Label_Object=MibTableColumn
l1Label=_L1Label_Object((1,3,6,1,4,1,6666,1,1,1,4),_L1Label_Type())
l1Label.setMaxAccess(_B)
if mibBuilder.loadTexts:l1Label.setStatus(_A)
_L1PriTable_Object=MibTable
l1PriTable=_L1PriTable_Object((1,3,6,1,4,1,6666,1,2))
if mibBuilder.loadTexts:l1PriTable.setStatus(_A)
_L1PriEntry_Object=MibTableRow
l1PriEntry=_L1PriEntry_Object((1,3,6,1,4,1,6666,1,2,1))
l1PriEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:l1PriEntry.setStatus(_A)
class _L1PriLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_L1PriLabel_Type.__name__=_D
_L1PriLabel_Object=MibTableColumn
l1PriLabel=_L1PriLabel_Object((1,3,6,1,4,1,6666,1,2,1,1),_L1PriLabel_Type())
l1PriLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:l1PriLabel.setStatus(_A)
class _L1PriState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_L1PriState_Type.__name__=_C
_L1PriState_Object=MibTableColumn
l1PriState=_L1PriState_Object((1,3,6,1,4,1,6666,1,2,1,2),_L1PriState_Type())
l1PriState.setMaxAccess(_B)
if mibBuilder.loadTexts:l1PriState.setStatus(_A)
_L1PriErrCrc4_Type=Counter32
_L1PriErrCrc4_Object=MibTableColumn
l1PriErrCrc4=_L1PriErrCrc4_Object((1,3,6,1,4,1,6666,1,2,1,3),_L1PriErrCrc4_Type())
l1PriErrCrc4.setMaxAccess(_B)
if mibBuilder.loadTexts:l1PriErrCrc4.setStatus(_A)
_L1PriErrRemAlarmInd_Type=Counter32
_L1PriErrRemAlarmInd_Object=MibTableColumn
l1PriErrRemAlarmInd=_L1PriErrRemAlarmInd_Object((1,3,6,1,4,1,6666,1,2,1,4),_L1PriErrRemAlarmInd_Type())
l1PriErrRemAlarmInd.setMaxAccess(_B)
if mibBuilder.loadTexts:l1PriErrRemAlarmInd.setStatus(_A)
_L1PriErrSigLoss_Type=Counter32
_L1PriErrSigLoss_Object=MibTableColumn
l1PriErrSigLoss=_L1PriErrSigLoss_Object((1,3,6,1,4,1,6666,1,2,1,5),_L1PriErrSigLoss_Type())
l1PriErrSigLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:l1PriErrSigLoss.setStatus(_A)
_L1PriErrAlarmInd_Type=Counter32
_L1PriErrAlarmInd_Object=MibTableColumn
l1PriErrAlarmInd=_L1PriErrAlarmInd_Object((1,3,6,1,4,1,6666,1,2,1,6),_L1PriErrAlarmInd_Type())
l1PriErrAlarmInd.setMaxAccess(_B)
if mibBuilder.loadTexts:l1PriErrAlarmInd.setStatus(_A)
_L1PriErrFrameAlignmentTOut_Type=Counter32
_L1PriErrFrameAlignmentTOut_Object=MibTableColumn
l1PriErrFrameAlignmentTOut=_L1PriErrFrameAlignmentTOut_Object((1,3,6,1,4,1,6666,1,2,1,7),_L1PriErrFrameAlignmentTOut_Type())
l1PriErrFrameAlignmentTOut.setMaxAccess(_B)
if mibBuilder.loadTexts:l1PriErrFrameAlignmentTOut.setStatus(_A)
_L1PriErrFrameAlignmentLoss_Type=Counter32
_L1PriErrFrameAlignmentLoss_Object=MibTableColumn
l1PriErrFrameAlignmentLoss=_L1PriErrFrameAlignmentLoss_Object((1,3,6,1,4,1,6666,1,2,1,8),_L1PriErrFrameAlignmentLoss_Type())
l1PriErrFrameAlignmentLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:l1PriErrFrameAlignmentLoss.setStatus(_A)
_L1PriErrSlip_Type=Counter32
_L1PriErrSlip_Object=MibTableColumn
l1PriErrSlip=_L1PriErrSlip_Object((1,3,6,1,4,1,6666,1,2,1,9),_L1PriErrSlip_Type())
l1PriErrSlip.setMaxAccess(_B)
if mibBuilder.loadTexts:l1PriErrSlip.setStatus(_A)
class _L1PriTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('noTest',0),('simAlarm',1),('resetAlarms',2)))
_L1PriTest_Type.__name__=_C
_L1PriTest_Object=MibTableColumn
l1PriTest=_L1PriTest_Object((1,3,6,1,4,1,6666,1,2,1,10),_L1PriTest_Type())
l1PriTest.setMaxAccess('read-write')
if mibBuilder.loadTexts:l1PriTest.setStatus(_A)
_L1BriTable_Object=MibTable
l1BriTable=_L1BriTable_Object((1,3,6,1,4,1,6666,1,3))
if mibBuilder.loadTexts:l1BriTable.setStatus(_A)
_L1BriEntry_Object=MibTableRow
l1BriEntry=_L1BriEntry_Object((1,3,6,1,4,1,6666,1,3,1))
l1BriEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:l1BriEntry.setStatus(_A)
class _L1BriLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_L1BriLabel_Type.__name__=_D
_L1BriLabel_Object=MibTableColumn
l1BriLabel=_L1BriLabel_Object((1,3,6,1,4,1,6666,1,3,1,1),_L1BriLabel_Type())
l1BriLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:l1BriLabel.setStatus(_A)
class _L1BriState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_L1BriState_Type.__name__=_C
_L1BriState_Object=MibTableColumn
l1BriState=_L1BriState_Object((1,3,6,1,4,1,6666,1,3,1,2),_L1BriState_Type())
l1BriState.setMaxAccess(_B)
if mibBuilder.loadTexts:l1BriState.setStatus(_A)
_L3Table_Object=MibTable
l3Table=_L3Table_Object((1,3,6,1,4,1,6666,1,4))
if mibBuilder.loadTexts:l3Table.setStatus(_A)
_L3Entry_Object=MibTableRow
l3Entry=_L3Entry_Object((1,3,6,1,4,1,6666,1,4,1))
l3Entry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:l3Entry.setStatus(_A)
class _L3Label_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_L3Label_Type.__name__=_D
_L3Label_Object=MibTableColumn
l3Label=_L3Label_Object((1,3,6,1,4,1,6666,1,4,1,1),_L3Label_Type())
l3Label.setMaxAccess(_B)
if mibBuilder.loadTexts:l3Label.setStatus(_A)
class _L3Protocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3,23)));namedValues=NamedValues(*(('none',0),('other',1),('etsi',3),('qsig',23)))
_L3Protocol_Type.__name__=_C
_L3Protocol_Object=MibTableColumn
l3Protocol=_L3Protocol_Object((1,3,6,1,4,1,6666,1,4,1,2),_L3Protocol_Type())
l3Protocol.setMaxAccess(_B)
if mibBuilder.loadTexts:l3Protocol.setStatus(_A)
_L3NumBchan_Type=Integer32
_L3NumBchan_Object=MibTableColumn
l3NumBchan=_L3NumBchan_Object((1,3,6,1,4,1,6666,1,4,1,3),_L3NumBchan_Type())
l3NumBchan.setMaxAccess(_B)
if mibBuilder.loadTexts:l3NumBchan.setStatus(_A)
_L3NumBchanActive_Type=Gauge32
_L3NumBchanActive_Object=MibTableColumn
l3NumBchanActive=_L3NumBchanActive_Object((1,3,6,1,4,1,6666,1,4,1,4),_L3NumBchanActive_Type())
l3NumBchanActive.setMaxAccess(_B)
if mibBuilder.loadTexts:l3NumBchanActive.setStatus(_A)
_L3CallsBoot_Type=Counter32
_L3CallsBoot_Object=MibTableColumn
l3CallsBoot=_L3CallsBoot_Object((1,3,6,1,4,1,6666,1,4,1,5),_L3CallsBoot_Type())
l3CallsBoot.setMaxAccess(_B)
if mibBuilder.loadTexts:l3CallsBoot.setStatus(_A)
_Gateway_ObjectIdentity=ObjectIdentity
gateway=_Gateway_ObjectIdentity((1,3,6,1,4,1,6666,2))
_Gatekeeper_ObjectIdentity=ObjectIdentity
gatekeeper=_Gatekeeper_ObjectIdentity((1,3,6,1,4,1,6666,2,1))
_VoiceIfTable_Object=MibTable
voiceIfTable=_VoiceIfTable_Object((1,3,6,1,4,1,6666,2,1,1))
if mibBuilder.loadTexts:voiceIfTable.setStatus(_A)
_VoiceIfEntry_Object=MibTableRow
voiceIfEntry=_VoiceIfEntry_Object((1,3,6,1,4,1,6666,2,1,1,1))
voiceIfEntry.setIndexNames((0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:voiceIfEntry.setStatus(_A)
class _VoiceIfGwName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VoiceIfGwName_Type.__name__=_D
_VoiceIfGwName_Object=MibTableColumn
voiceIfGwName=_VoiceIfGwName_Object((1,3,6,1,4,1,6666,2,1,1,1,1),_VoiceIfGwName_Type())
voiceIfGwName.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfGwName.setStatus(_A)
class _VoiceIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('unkown',0),('if',1),('ep',2),('gk',3),('gw',4)))
_VoiceIfType_Type.__name__=_C
_VoiceIfType_Object=MibTableColumn
voiceIfType=_VoiceIfType_Object((1,3,6,1,4,1,6666,2,1,1,1,2),_VoiceIfType_Type())
voiceIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfType.setStatus(_A)
_VoiceIfAddr_Type=IpAddress
_VoiceIfAddr_Object=MibTableColumn
voiceIfAddr=_VoiceIfAddr_Object((1,3,6,1,4,1,6666,2,1,1,1,3),_VoiceIfAddr_Type())
voiceIfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfAddr.setStatus(_A)
class _VoiceIfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_VoiceIfState_Type.__name__=_C
_VoiceIfState_Object=MibTableColumn
voiceIfState=_VoiceIfState_Object((1,3,6,1,4,1,6666,2,1,1,1,4),_VoiceIfState_Type())
voiceIfState.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfState.setStatus(_A)
class _VoiceIfNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VoiceIfNumber_Type.__name__=_D
_VoiceIfNumber_Object=MibTableColumn
voiceIfNumber=_VoiceIfNumber_Object((1,3,6,1,4,1,6666,2,1,1,1,5),_VoiceIfNumber_Type())
voiceIfNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfNumber.setStatus(_A)
class _VoiceIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VoiceIfName_Type.__name__=_D
_VoiceIfName_Object=MibTableColumn
voiceIfName=_VoiceIfName_Object((1,3,6,1,4,1,6666,2,1,1,1,6),_VoiceIfName_Type())
voiceIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfName.setStatus(_A)
class _VoiceIfProduct_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VoiceIfProduct_Type.__name__=_D
_VoiceIfProduct_Object=MibTableColumn
voiceIfProduct=_VoiceIfProduct_Object((1,3,6,1,4,1,6666,2,1,1,1,7),_VoiceIfProduct_Type())
voiceIfProduct.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfProduct.setStatus(_A)
class _VoiceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VoiceIfIndex_Type.__name__=_C
_VoiceIfIndex_Object=MibTableColumn
voiceIfIndex=_VoiceIfIndex_Object((1,3,6,1,4,1,6666,2,1,1,1,8),_VoiceIfIndex_Type())
voiceIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfIndex.setStatus(_A)
class _VoiceIfAliasIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VoiceIfAliasIndex_Type.__name__=_C
_VoiceIfAliasIndex_Object=MibTableColumn
voiceIfAliasIndex=_VoiceIfAliasIndex_Object((1,3,6,1,4,1,6666,2,1,1,1,9),_VoiceIfAliasIndex_Type())
voiceIfAliasIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:voiceIfAliasIndex.setStatus('optional')
_TrapDummyGroup_ObjectIdentity=ObjectIdentity
trapDummyGroup=_TrapDummyGroup_ObjectIdentity((1,3,6,1,4,1,6666,3))
class _TrapDisplayStringParm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TrapDisplayStringParm_Type.__name__=_D
_TrapDisplayStringParm_Object=MibScalar
trapDisplayStringParm=_TrapDisplayStringParm_Object((1,3,6,1,4,1,6666,3,1),_TrapDisplayStringParm_Type())
trapDisplayStringParm.setMaxAccess(_B)
if mibBuilder.loadTexts:trapDisplayStringParm.setStatus(_A)
class _TrapIntegerParm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TrapIntegerParm_Type.__name__=_C
_TrapIntegerParm_Object=MibScalar
trapIntegerParm=_TrapIntegerParm_Object((1,3,6,1,4,1,6666,3,2),_TrapIntegerParm_Type())
trapIntegerParm.setMaxAccess(_B)
if mibBuilder.loadTexts:trapIntegerParm.setStatus(_A)
innoColdStart=NotificationType((1,3,6,1,4,1,6666,0,0))
if mibBuilder.loadTexts:innoColdStart.setStatus('')
innoWarmStart=NotificationType((1,3,6,1,4,1,6666,0,1))
if mibBuilder.loadTexts:innoWarmStart.setStatus('')
innoLinkDown=NotificationType((1,3,6,1,4,1,6666,0,2))
innoLinkDown.setObjects((_H,_I))
if mibBuilder.loadTexts:innoLinkDown.setStatus('')
innoLinkUp=NotificationType((1,3,6,1,4,1,6666,0,3))
innoLinkUp.setObjects((_H,_I))
if mibBuilder.loadTexts:innoLinkUp.setStatus('')
innoAuthenticationFailure=NotificationType((1,3,6,1,4,1,6666,0,4))
if mibBuilder.loadTexts:innoAuthenticationFailure.setStatus('')
innoIsdnFailure=NotificationType((1,3,6,1,4,1,6666,0,5))
innoIsdnFailure.setObjects(*((_E,_Q),(_E,_R)))
if mibBuilder.loadTexts:innoIsdnFailure.setStatus('')
mibBuilder.exportSymbols(_E,**{_D:DisplayString,'innovaphone':innovaphone,'innoColdStart':innoColdStart,'innoWarmStart':innoWarmStart,'innoLinkDown':innoLinkDown,'innoLinkUp':innoLinkUp,'innoAuthenticationFailure':innoAuthenticationFailure,'innoIsdnFailure':innoIsdnFailure,'isdn':isdn,'l2Table':l2Table,'l2Entry':l2Entry,_K:l2Label,'l2State':l2State,'l2Mode':l2Mode,'l1Label':l1Label,'l1PriTable':l1PriTable,'l1PriEntry':l1PriEntry,_L:l1PriLabel,'l1PriState':l1PriState,'l1PriErrCrc4':l1PriErrCrc4,'l1PriErrRemAlarmInd':l1PriErrRemAlarmInd,'l1PriErrSigLoss':l1PriErrSigLoss,'l1PriErrAlarmInd':l1PriErrAlarmInd,'l1PriErrFrameAlignmentTOut':l1PriErrFrameAlignmentTOut,'l1PriErrFrameAlignmentLoss':l1PriErrFrameAlignmentLoss,'l1PriErrSlip':l1PriErrSlip,'l1PriTest':l1PriTest,'l1BriTable':l1BriTable,'l1BriEntry':l1BriEntry,_M:l1BriLabel,'l1BriState':l1BriState,'l3Table':l3Table,'l3Entry':l3Entry,_N:l3Label,'l3Protocol':l3Protocol,'l3NumBchan':l3NumBchan,'l3NumBchanActive':l3NumBchanActive,'l3CallsBoot':l3CallsBoot,'gateway':gateway,'gatekeeper':gatekeeper,'voiceIfTable':voiceIfTable,'voiceIfEntry':voiceIfEntry,'voiceIfGwName':voiceIfGwName,'voiceIfType':voiceIfType,'voiceIfAddr':voiceIfAddr,'voiceIfState':voiceIfState,'voiceIfNumber':voiceIfNumber,'voiceIfName':voiceIfName,'voiceIfProduct':voiceIfProduct,_O:voiceIfIndex,_P:voiceIfAliasIndex,'trapDummyGroup':trapDummyGroup,_Q:trapDisplayStringParm,_R:trapIntegerParm})