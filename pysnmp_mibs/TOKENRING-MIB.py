_l='dot5StatsGroup'
_k='dot5StateGroup'
_j='dot5StatsFreqErrors'
_i='dot5StatsSingles'
_h='dot5StatsRemoves'
_g='dot5StatsLobeWires'
_f='dot5StatsRecoverys'
_e='dot5StatsTransmitBeacons'
_d='dot5StatsSignalLoss'
_c='dot5StatsHardErrors'
_b='dot5StatsSoftErrors'
_a='dot5StatsTokenErrors'
_Z='dot5StatsFrameCopiedErrors'
_Y='dot5StatsReceiveCongestions'
_X='dot5StatsLostFrameErrors'
_W='dot5StatsInternalErrors'
_V='dot5StatsAbortTransErrors'
_U='dot5StatsACErrors'
_T='dot5StatsBurstErrors'
_S='dot5StatsLineErrors'
_R='dot5LastBeaconSent'
_Q='dot5Functional'
_P='dot5ActMonParticipate'
_O='dot5UpStream'
_N='dot5RingSpeed'
_M='dot5RingOpenStatus'
_L='dot5RingState'
_K='dot5RingStatus'
_J='dot5Commands'
_I='dot5TimerIfIndex'
_H='dot5StatsIfIndex'
_G='dot5IfIndex'
_F='read-write'
_E='Integer32'
_D='obsolete'
_C='TOKENRING-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeStamp')
dot5=ModuleIdentity((1,3,6,1,2,1,10,9))
_Dot5Table_Object=MibTable
dot5Table=_Dot5Table_Object((1,3,6,1,2,1,10,9,1))
if mibBuilder.loadTexts:dot5Table.setStatus(_A)
_Dot5Entry_Object=MibTableRow
dot5Entry=_Dot5Entry_Object((1,3,6,1,2,1,10,9,1,1))
dot5Entry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:dot5Entry.setStatus(_A)
_Dot5IfIndex_Type=Integer32
_Dot5IfIndex_Object=MibTableColumn
dot5IfIndex=_Dot5IfIndex_Object((1,3,6,1,2,1,10,9,1,1,1),_Dot5IfIndex_Type())
dot5IfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5IfIndex.setStatus(_A)
class _Dot5Commands_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noop',1),('open',2),('reset',3),('close',4)))
_Dot5Commands_Type.__name__=_E
_Dot5Commands_Object=MibTableColumn
dot5Commands=_Dot5Commands_Object((1,3,6,1,2,1,10,9,1,1,2),_Dot5Commands_Type())
dot5Commands.setMaxAccess(_F)
if mibBuilder.loadTexts:dot5Commands.setStatus(_A)
class _Dot5RingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,262143))
_Dot5RingStatus_Type.__name__=_E
_Dot5RingStatus_Object=MibTableColumn
dot5RingStatus=_Dot5RingStatus_Object((1,3,6,1,2,1,10,9,1,1,3),_Dot5RingStatus_Type())
dot5RingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5RingStatus.setStatus(_A)
class _Dot5RingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('opened',1),('closed',2),('opening',3),('closing',4),('openFailure',5),('ringFailure',6)))
_Dot5RingState_Type.__name__=_E
_Dot5RingState_Object=MibTableColumn
dot5RingState=_Dot5RingState_Object((1,3,6,1,2,1,10,9,1,1,4),_Dot5RingState_Type())
dot5RingState.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5RingState.setStatus(_A)
class _Dot5RingOpenStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('noOpen',1),('badParam',2),('lobeFailed',3),('signalLoss',4),('insertionTimeout',5),('ringFailed',6),('beaconing',7),('duplicateMAC',8),('requestFailed',9),('removeReceived',10),('open',11)))
_Dot5RingOpenStatus_Type.__name__=_E
_Dot5RingOpenStatus_Object=MibTableColumn
dot5RingOpenStatus=_Dot5RingOpenStatus_Object((1,3,6,1,2,1,10,9,1,1,5),_Dot5RingOpenStatus_Type())
dot5RingOpenStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5RingOpenStatus.setStatus(_A)
class _Dot5RingSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('oneMegabit',2),('fourMegabit',3),('sixteenMegabit',4)))
_Dot5RingSpeed_Type.__name__=_E
_Dot5RingSpeed_Object=MibTableColumn
dot5RingSpeed=_Dot5RingSpeed_Object((1,3,6,1,2,1,10,9,1,1,6),_Dot5RingSpeed_Type())
dot5RingSpeed.setMaxAccess(_F)
if mibBuilder.loadTexts:dot5RingSpeed.setStatus(_A)
_Dot5UpStream_Type=MacAddress
_Dot5UpStream_Object=MibTableColumn
dot5UpStream=_Dot5UpStream_Object((1,3,6,1,2,1,10,9,1,1,7),_Dot5UpStream_Type())
dot5UpStream.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5UpStream.setStatus(_A)
class _Dot5ActMonParticipate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_Dot5ActMonParticipate_Type.__name__=_E
_Dot5ActMonParticipate_Object=MibTableColumn
dot5ActMonParticipate=_Dot5ActMonParticipate_Object((1,3,6,1,2,1,10,9,1,1,8),_Dot5ActMonParticipate_Type())
dot5ActMonParticipate.setMaxAccess(_F)
if mibBuilder.loadTexts:dot5ActMonParticipate.setStatus(_A)
_Dot5Functional_Type=MacAddress
_Dot5Functional_Object=MibTableColumn
dot5Functional=_Dot5Functional_Object((1,3,6,1,2,1,10,9,1,1,9),_Dot5Functional_Type())
dot5Functional.setMaxAccess(_F)
if mibBuilder.loadTexts:dot5Functional.setStatus(_A)
_Dot5LastBeaconSent_Type=TimeStamp
_Dot5LastBeaconSent_Object=MibTableColumn
dot5LastBeaconSent=_Dot5LastBeaconSent_Object((1,3,6,1,2,1,10,9,1,1,10),_Dot5LastBeaconSent_Type())
dot5LastBeaconSent.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5LastBeaconSent.setStatus(_A)
_Dot5StatsTable_Object=MibTable
dot5StatsTable=_Dot5StatsTable_Object((1,3,6,1,2,1,10,9,2))
if mibBuilder.loadTexts:dot5StatsTable.setStatus(_A)
_Dot5StatsEntry_Object=MibTableRow
dot5StatsEntry=_Dot5StatsEntry_Object((1,3,6,1,2,1,10,9,2,1))
dot5StatsEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:dot5StatsEntry.setStatus(_A)
_Dot5StatsIfIndex_Type=Integer32
_Dot5StatsIfIndex_Object=MibTableColumn
dot5StatsIfIndex=_Dot5StatsIfIndex_Object((1,3,6,1,2,1,10,9,2,1,1),_Dot5StatsIfIndex_Type())
dot5StatsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5StatsIfIndex.setStatus(_A)
_Dot5StatsLineErrors_Type=Counter32
_Dot5StatsLineErrors_Object=MibTableColumn
dot5StatsLineErrors=_Dot5StatsLineErrors_Object((1,3,6,1,2,1,10,9,2,1,2),_Dot5StatsLineErrors_Type())
dot5StatsLineErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5StatsLineErrors.setStatus(_A)
_Dot5StatsBurstErrors_Type=Counter32
_Dot5StatsBurstErrors_Object=MibTableColumn
dot5StatsBurstErrors=_Dot5StatsBurstErrors_Object((1,3,6,1,2,1,10,9,2,1,3),_Dot5StatsBurstErrors_Type())
dot5StatsBurstErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5StatsBurstErrors.setStatus(_A)
_Dot5StatsACErrors_Type=Counter32
_Dot5StatsACErrors_Object=MibTableColumn
dot5StatsACErrors=_Dot5StatsACErrors_Object((1,3,6,1,2,1,10,9,2,1,4),_Dot5StatsACErrors_Type())
dot5StatsACErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5StatsACErrors.setStatus(_A)
_Dot5StatsAbortTransErrors_Type=Counter32
_Dot5StatsAbortTransErrors_Object=MibTableColumn
dot5StatsAbortTransErrors=_Dot5StatsAbortTransErrors_Object((1,3,6,1,2,1,10,9,2,1,5),_Dot5StatsAbortTransErrors_Type())
dot5StatsAbortTransErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5StatsAbortTransErrors.setStatus(_A)
_Dot5StatsInternalErrors_Type=Counter32
_Dot5StatsInternalErrors_Object=MibTableColumn
dot5StatsInternalErrors=_Dot5StatsInternalErrors_Object((1,3,6,1,2,1,10,9,2,1,6),_Dot5StatsInternalErrors_Type())
dot5StatsInternalErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5StatsInternalErrors.setStatus(_A)
_Dot5StatsLostFrameErrors_Type=Counter32
_Dot5StatsLostFrameErrors_Object=MibTableColumn
dot5StatsLostFrameErrors=_Dot5StatsLostFrameErrors_Object((1,3,6,1,2,1,10,9,2,1,7),_Dot5StatsLostFrameErrors_Type())
dot5StatsLostFrameErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5StatsLostFrameErrors.setStatus(_A)
_Dot5StatsReceiveCongestions_Type=Counter32
_Dot5StatsReceiveCongestions_Object=MibTableColumn
dot5StatsReceiveCongestions=_Dot5StatsReceiveCongestions_Object((1,3,6,1,2,1,10,9,2,1,8),_Dot5StatsReceiveCongestions_Type())
dot5StatsReceiveCongestions.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5StatsReceiveCongestions.setStatus(_A)
_Dot5StatsFrameCopiedErrors_Type=Counter32
_Dot5StatsFrameCopiedErrors_Object=MibTableColumn
dot5StatsFrameCopiedErrors=_Dot5StatsFrameCopiedErrors_Object((1,3,6,1,2,1,10,9,2,1,9),_Dot5StatsFrameCopiedErrors_Type())
dot5StatsFrameCopiedErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5StatsFrameCopiedErrors.setStatus(_A)
_Dot5StatsTokenErrors_Type=Counter32
_Dot5StatsTokenErrors_Object=MibTableColumn
dot5StatsTokenErrors=_Dot5StatsTokenErrors_Object((1,3,6,1,2,1,10,9,2,1,10),_Dot5StatsTokenErrors_Type())
dot5StatsTokenErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5StatsTokenErrors.setStatus(_A)
_Dot5StatsSoftErrors_Type=Counter32
_Dot5StatsSoftErrors_Object=MibTableColumn
dot5StatsSoftErrors=_Dot5StatsSoftErrors_Object((1,3,6,1,2,1,10,9,2,1,11),_Dot5StatsSoftErrors_Type())
dot5StatsSoftErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5StatsSoftErrors.setStatus(_A)
_Dot5StatsHardErrors_Type=Counter32
_Dot5StatsHardErrors_Object=MibTableColumn
dot5StatsHardErrors=_Dot5StatsHardErrors_Object((1,3,6,1,2,1,10,9,2,1,12),_Dot5StatsHardErrors_Type())
dot5StatsHardErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5StatsHardErrors.setStatus(_A)
_Dot5StatsSignalLoss_Type=Counter32
_Dot5StatsSignalLoss_Object=MibTableColumn
dot5StatsSignalLoss=_Dot5StatsSignalLoss_Object((1,3,6,1,2,1,10,9,2,1,13),_Dot5StatsSignalLoss_Type())
dot5StatsSignalLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5StatsSignalLoss.setStatus(_A)
_Dot5StatsTransmitBeacons_Type=Counter32
_Dot5StatsTransmitBeacons_Object=MibTableColumn
dot5StatsTransmitBeacons=_Dot5StatsTransmitBeacons_Object((1,3,6,1,2,1,10,9,2,1,14),_Dot5StatsTransmitBeacons_Type())
dot5StatsTransmitBeacons.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5StatsTransmitBeacons.setStatus(_A)
_Dot5StatsRecoverys_Type=Counter32
_Dot5StatsRecoverys_Object=MibTableColumn
dot5StatsRecoverys=_Dot5StatsRecoverys_Object((1,3,6,1,2,1,10,9,2,1,15),_Dot5StatsRecoverys_Type())
dot5StatsRecoverys.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5StatsRecoverys.setStatus(_A)
_Dot5StatsLobeWires_Type=Counter32
_Dot5StatsLobeWires_Object=MibTableColumn
dot5StatsLobeWires=_Dot5StatsLobeWires_Object((1,3,6,1,2,1,10,9,2,1,16),_Dot5StatsLobeWires_Type())
dot5StatsLobeWires.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5StatsLobeWires.setStatus(_A)
_Dot5StatsRemoves_Type=Counter32
_Dot5StatsRemoves_Object=MibTableColumn
dot5StatsRemoves=_Dot5StatsRemoves_Object((1,3,6,1,2,1,10,9,2,1,17),_Dot5StatsRemoves_Type())
dot5StatsRemoves.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5StatsRemoves.setStatus(_A)
_Dot5StatsSingles_Type=Counter32
_Dot5StatsSingles_Object=MibTableColumn
dot5StatsSingles=_Dot5StatsSingles_Object((1,3,6,1,2,1,10,9,2,1,18),_Dot5StatsSingles_Type())
dot5StatsSingles.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5StatsSingles.setStatus(_A)
_Dot5StatsFreqErrors_Type=Counter32
_Dot5StatsFreqErrors_Object=MibTableColumn
dot5StatsFreqErrors=_Dot5StatsFreqErrors_Object((1,3,6,1,2,1,10,9,2,1,19),_Dot5StatsFreqErrors_Type())
dot5StatsFreqErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5StatsFreqErrors.setStatus(_A)
_Dot5Tests_ObjectIdentity=ObjectIdentity
dot5Tests=_Dot5Tests_ObjectIdentity((1,3,6,1,2,1,10,9,3))
_Dot5TestInsertFunc_ObjectIdentity=ObjectIdentity
dot5TestInsertFunc=_Dot5TestInsertFunc_ObjectIdentity((1,3,6,1,2,1,10,9,3,1))
if mibBuilder.loadTexts:dot5TestInsertFunc.setStatus(_A)
_Dot5TestFullDuplexLoopBack_ObjectIdentity=ObjectIdentity
dot5TestFullDuplexLoopBack=_Dot5TestFullDuplexLoopBack_ObjectIdentity((1,3,6,1,2,1,10,9,3,2))
if mibBuilder.loadTexts:dot5TestFullDuplexLoopBack.setStatus(_A)
_Dot5ChipSets_ObjectIdentity=ObjectIdentity
dot5ChipSets=_Dot5ChipSets_ObjectIdentity((1,3,6,1,2,1,10,9,4))
_Dot5ChipSetIBM16_ObjectIdentity=ObjectIdentity
dot5ChipSetIBM16=_Dot5ChipSetIBM16_ObjectIdentity((1,3,6,1,2,1,10,9,4,1))
if mibBuilder.loadTexts:dot5ChipSetIBM16.setStatus(_A)
_Dot5ChipSetTItms380_ObjectIdentity=ObjectIdentity
dot5ChipSetTItms380=_Dot5ChipSetTItms380_ObjectIdentity((1,3,6,1,2,1,10,9,4,2))
if mibBuilder.loadTexts:dot5ChipSetTItms380.setStatus(_A)
_Dot5ChipSetTItms380c16_ObjectIdentity=ObjectIdentity
dot5ChipSetTItms380c16=_Dot5ChipSetTItms380c16_ObjectIdentity((1,3,6,1,2,1,10,9,4,3))
if mibBuilder.loadTexts:dot5ChipSetTItms380c16.setStatus(_A)
_Dot5TimerTable_Object=MibTable
dot5TimerTable=_Dot5TimerTable_Object((1,3,6,1,2,1,10,9,5))
if mibBuilder.loadTexts:dot5TimerTable.setStatus(_D)
_Dot5TimerEntry_Object=MibTableRow
dot5TimerEntry=_Dot5TimerEntry_Object((1,3,6,1,2,1,10,9,5,1))
dot5TimerEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:dot5TimerEntry.setStatus(_D)
_Dot5TimerIfIndex_Type=Integer32
_Dot5TimerIfIndex_Object=MibTableColumn
dot5TimerIfIndex=_Dot5TimerIfIndex_Object((1,3,6,1,2,1,10,9,5,1,1),_Dot5TimerIfIndex_Type())
dot5TimerIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5TimerIfIndex.setStatus(_D)
_Dot5TimerReturnRepeat_Type=Integer32
_Dot5TimerReturnRepeat_Object=MibTableColumn
dot5TimerReturnRepeat=_Dot5TimerReturnRepeat_Object((1,3,6,1,2,1,10,9,5,1,2),_Dot5TimerReturnRepeat_Type())
dot5TimerReturnRepeat.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5TimerReturnRepeat.setStatus(_D)
_Dot5TimerHolding_Type=Integer32
_Dot5TimerHolding_Object=MibTableColumn
dot5TimerHolding=_Dot5TimerHolding_Object((1,3,6,1,2,1,10,9,5,1,3),_Dot5TimerHolding_Type())
dot5TimerHolding.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5TimerHolding.setStatus(_D)
_Dot5TimerQueuePDU_Type=Integer32
_Dot5TimerQueuePDU_Object=MibTableColumn
dot5TimerQueuePDU=_Dot5TimerQueuePDU_Object((1,3,6,1,2,1,10,9,5,1,4),_Dot5TimerQueuePDU_Type())
dot5TimerQueuePDU.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5TimerQueuePDU.setStatus(_D)
_Dot5TimerValidTransmit_Type=Integer32
_Dot5TimerValidTransmit_Object=MibTableColumn
dot5TimerValidTransmit=_Dot5TimerValidTransmit_Object((1,3,6,1,2,1,10,9,5,1,5),_Dot5TimerValidTransmit_Type())
dot5TimerValidTransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5TimerValidTransmit.setStatus(_D)
_Dot5TimerNoToken_Type=Integer32
_Dot5TimerNoToken_Object=MibTableColumn
dot5TimerNoToken=_Dot5TimerNoToken_Object((1,3,6,1,2,1,10,9,5,1,6),_Dot5TimerNoToken_Type())
dot5TimerNoToken.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5TimerNoToken.setStatus(_D)
_Dot5TimerActiveMon_Type=Integer32
_Dot5TimerActiveMon_Object=MibTableColumn
dot5TimerActiveMon=_Dot5TimerActiveMon_Object((1,3,6,1,2,1,10,9,5,1,7),_Dot5TimerActiveMon_Type())
dot5TimerActiveMon.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5TimerActiveMon.setStatus(_D)
_Dot5TimerStandbyMon_Type=Integer32
_Dot5TimerStandbyMon_Object=MibTableColumn
dot5TimerStandbyMon=_Dot5TimerStandbyMon_Object((1,3,6,1,2,1,10,9,5,1,8),_Dot5TimerStandbyMon_Type())
dot5TimerStandbyMon.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5TimerStandbyMon.setStatus(_D)
_Dot5TimerErrorReport_Type=Integer32
_Dot5TimerErrorReport_Object=MibTableColumn
dot5TimerErrorReport=_Dot5TimerErrorReport_Object((1,3,6,1,2,1,10,9,5,1,9),_Dot5TimerErrorReport_Type())
dot5TimerErrorReport.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5TimerErrorReport.setStatus(_D)
_Dot5TimerBeaconTransmit_Type=Integer32
_Dot5TimerBeaconTransmit_Object=MibTableColumn
dot5TimerBeaconTransmit=_Dot5TimerBeaconTransmit_Object((1,3,6,1,2,1,10,9,5,1,10),_Dot5TimerBeaconTransmit_Type())
dot5TimerBeaconTransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5TimerBeaconTransmit.setStatus(_D)
_Dot5TimerBeaconReceive_Type=Integer32
_Dot5TimerBeaconReceive_Object=MibTableColumn
dot5TimerBeaconReceive=_Dot5TimerBeaconReceive_Object((1,3,6,1,2,1,10,9,5,1,11),_Dot5TimerBeaconReceive_Type())
dot5TimerBeaconReceive.setMaxAccess(_B)
if mibBuilder.loadTexts:dot5TimerBeaconReceive.setStatus(_D)
_Dot5Conformance_ObjectIdentity=ObjectIdentity
dot5Conformance=_Dot5Conformance_ObjectIdentity((1,3,6,1,2,1,10,9,6))
_Dot5Groups_ObjectIdentity=ObjectIdentity
dot5Groups=_Dot5Groups_ObjectIdentity((1,3,6,1,2,1,10,9,6,1))
_Dot5Compliances_ObjectIdentity=ObjectIdentity
dot5Compliances=_Dot5Compliances_ObjectIdentity((1,3,6,1,2,1,10,9,6,2))
dot5StateGroup=ObjectGroup((1,3,6,1,2,1,10,9,6,1,1))
dot5StateGroup.setObjects(*((_C,_J),(_C,_K),(_C,_L),(_C,_M),(_C,_N),(_C,_O),(_C,_P),(_C,_Q),(_C,_R)))
if mibBuilder.loadTexts:dot5StateGroup.setStatus(_A)
dot5StatsGroup=ObjectGroup((1,3,6,1,2,1,10,9,6,1,2))
dot5StatsGroup.setObjects(*((_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_W),(_C,_X),(_C,_Y),(_C,_Z),(_C,_a),(_C,_b),(_C,_c),(_C,_d),(_C,_e),(_C,_f),(_C,_g),(_C,_h),(_C,_i),(_C,_j)))
if mibBuilder.loadTexts:dot5StatsGroup.setStatus(_A)
dot5Compliance=ModuleCompliance((1,3,6,1,2,1,10,9,6,2,1))
dot5Compliance.setObjects(*((_C,_k),(_C,_l)))
if mibBuilder.loadTexts:dot5Compliance.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'dot5':dot5,'dot5Table':dot5Table,'dot5Entry':dot5Entry,_G:dot5IfIndex,_J:dot5Commands,_K:dot5RingStatus,_L:dot5RingState,_M:dot5RingOpenStatus,_N:dot5RingSpeed,_O:dot5UpStream,_P:dot5ActMonParticipate,_Q:dot5Functional,_R:dot5LastBeaconSent,'dot5StatsTable':dot5StatsTable,'dot5StatsEntry':dot5StatsEntry,_H:dot5StatsIfIndex,_S:dot5StatsLineErrors,_T:dot5StatsBurstErrors,_U:dot5StatsACErrors,_V:dot5StatsAbortTransErrors,_W:dot5StatsInternalErrors,_X:dot5StatsLostFrameErrors,_Y:dot5StatsReceiveCongestions,_Z:dot5StatsFrameCopiedErrors,_a:dot5StatsTokenErrors,_b:dot5StatsSoftErrors,_c:dot5StatsHardErrors,_d:dot5StatsSignalLoss,_e:dot5StatsTransmitBeacons,_f:dot5StatsRecoverys,_g:dot5StatsLobeWires,_h:dot5StatsRemoves,_i:dot5StatsSingles,_j:dot5StatsFreqErrors,'dot5Tests':dot5Tests,'dot5TestInsertFunc':dot5TestInsertFunc,'dot5TestFullDuplexLoopBack':dot5TestFullDuplexLoopBack,'dot5ChipSets':dot5ChipSets,'dot5ChipSetIBM16':dot5ChipSetIBM16,'dot5ChipSetTItms380':dot5ChipSetTItms380,'dot5ChipSetTItms380c16':dot5ChipSetTItms380c16,'dot5TimerTable':dot5TimerTable,'dot5TimerEntry':dot5TimerEntry,_I:dot5TimerIfIndex,'dot5TimerReturnRepeat':dot5TimerReturnRepeat,'dot5TimerHolding':dot5TimerHolding,'dot5TimerQueuePDU':dot5TimerQueuePDU,'dot5TimerValidTransmit':dot5TimerValidTransmit,'dot5TimerNoToken':dot5TimerNoToken,'dot5TimerActiveMon':dot5TimerActiveMon,'dot5TimerStandbyMon':dot5TimerStandbyMon,'dot5TimerErrorReport':dot5TimerErrorReport,'dot5TimerBeaconTransmit':dot5TimerBeaconTransmit,'dot5TimerBeaconReceive':dot5TimerBeaconReceive,'dot5Conformance':dot5Conformance,'dot5Groups':dot5Groups,_k:dot5StateGroup,_l:dot5StatsGroup,'dot5Compliances':dot5Compliances,'dot5Compliance':dot5Compliance})