_AO='etherPfcGroup'
_AN='etherExtensionMacCtrlGroup'
_AM='etherSlowProtocolsGroup'
_AL='etherHCStatsLpiGroup'
_AK='etherCollisionTableGroup'
_AJ='etherHCControlPauseGroup'
_AI='etherControlPauseGroup'
_AH='etherHCControlGroup'
_AG='etherControlGroup'
_AF='etherHCStatsGroup'
_AE='etherStatsHalfDuplexGroup'
_AD='etherStatsHighSpeedGroup'
_AC='etherStatsLowSpeedGroup'
_AB='etherRateControlGroup'
_AA='etherDuplexGroup'
_A9='etherStatsBaseGroup2'
_A8='dot3HCOutPFCFrames'
_A7='dot3HCInPFCFrames'
_A6='dot3PFCOperMode'
_A5='dot3PFCAdminMode'
_A4='dot3ExtensionMacCtrlStatus'
_A3='dot3HCOutExtensionFrames'
_A2='dot3HCInExtensionFrames'
_A1='dot3SlowProtocolFrameLimit'
_A0='dot3HCStatsReceiveLPITransitions'
_z='dot3HCStatsTransmitLPITransitions'
_y='dot3HCStatsReceiveLPIMicroseconds'
_x='dot3HCStatsTransmitLPIMicroseconds'
_w='dot3StatsRateControlStatus'
_v='dot3StatsRateControlAbility'
_u='dot3HCOutPauseFrames'
_t='dot3HCInPauseFrames'
_s='dot3HCControlInUnknownOpcodes'
_r='dot3HCStatsSymbolErrors'
_q='dot3HCStatsInternalMacReceiveErrors'
_p='dot3HCStatsFrameTooLongs'
_o='dot3HCStatsInternalMacTransmitErrors'
_n='dot3HCStatsFCSErrors'
_m='dot3HCStatsAlignmentErrors'
_l='dot3StatsCarrierSenseErrors'
_k='dot3StatsExcessiveCollisions'
_j='dot3StatsLateCollisions'
_i='dot3StatsDeferredTransmissions'
_h='dot3StatsMultipleCollisionFrames'
_g='dot3StatsSingleCollisionFrames'
_f='dot3StatsMaxFrameLength'
_e='dot3StatsInternalMacReceiveErrors'
_d='dot3StatsFrameTooLongs'
_c='dot3StatsInternalMacTransmitErrors'
_b='dot3StatsFCSErrors'
_a='dot3StatsAlignmentErrors'
_Z='dot3OutPauseFrames'
_Y='dot3InPauseFrames'
_X='dot3PauseOperMode'
_W='dot3PauseAdminMode'
_V='dot3ControlInUnknownOpcodes'
_U='dot3ControlFunctionsSupported'
_T='dot3StatsDuplexStatus'
_S='dot3StatsSymbolErrors'
_R='dot3StatsSQETestErrors'
_Q='dot3CollFrequencies'
_P='enabled'
_O='enabledXmitAndRcv'
_N='enabledRcv'
_M='enabledXmit'
_L='dot3CollCount'
_K='not-accessible'
_J='ifIndex'
_I='IF-MIB'
_H='read-write'
_G='unknown'
_F='disabled'
_E='dot3StatsIndex'
_D='Integer32'
_C='read-only'
_B='IEEE8023-EtherLike-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_I,'InterfaceIndex',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,org=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','org')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ieee8023etherMIB=ModuleIdentity((1,3,111,2,802,3,1,10))
if mibBuilder.loadTexts:ieee8023etherMIB.setRevisions(('2013-04-11 00:00','2011-02-02 00:00'))
_Ieee8023etherMIBObjects_ObjectIdentity=ObjectIdentity
ieee8023etherMIBObjects=_Ieee8023etherMIBObjects_ObjectIdentity((1,3,111,2,802,3,1,10,1))
_Dot3StatsTable_Object=MibTable
dot3StatsTable=_Dot3StatsTable_Object((1,3,111,2,802,3,1,10,1,2))
if mibBuilder.loadTexts:dot3StatsTable.setStatus(_A)
_Dot3StatsEntry_Object=MibTableRow
dot3StatsEntry=_Dot3StatsEntry_Object((1,3,111,2,802,3,1,10,1,2,1))
dot3StatsEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:dot3StatsEntry.setStatus(_A)
_Dot3StatsIndex_Type=InterfaceIndex
_Dot3StatsIndex_Object=MibTableColumn
dot3StatsIndex=_Dot3StatsIndex_Object((1,3,111,2,802,3,1,10,1,2,1,1),_Dot3StatsIndex_Type())
dot3StatsIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:dot3StatsIndex.setStatus(_A)
_Dot3StatsAlignmentErrors_Type=Counter32
_Dot3StatsAlignmentErrors_Object=MibTableColumn
dot3StatsAlignmentErrors=_Dot3StatsAlignmentErrors_Object((1,3,111,2,802,3,1,10,1,2,1,2),_Dot3StatsAlignmentErrors_Type())
dot3StatsAlignmentErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3StatsAlignmentErrors.setStatus(_A)
_Dot3StatsFCSErrors_Type=Counter32
_Dot3StatsFCSErrors_Object=MibTableColumn
dot3StatsFCSErrors=_Dot3StatsFCSErrors_Object((1,3,111,2,802,3,1,10,1,2,1,3),_Dot3StatsFCSErrors_Type())
dot3StatsFCSErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3StatsFCSErrors.setStatus(_A)
_Dot3StatsSingleCollisionFrames_Type=Counter32
_Dot3StatsSingleCollisionFrames_Object=MibTableColumn
dot3StatsSingleCollisionFrames=_Dot3StatsSingleCollisionFrames_Object((1,3,111,2,802,3,1,10,1,2,1,4),_Dot3StatsSingleCollisionFrames_Type())
dot3StatsSingleCollisionFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3StatsSingleCollisionFrames.setStatus(_A)
_Dot3StatsMultipleCollisionFrames_Type=Counter32
_Dot3StatsMultipleCollisionFrames_Object=MibTableColumn
dot3StatsMultipleCollisionFrames=_Dot3StatsMultipleCollisionFrames_Object((1,3,111,2,802,3,1,10,1,2,1,5),_Dot3StatsMultipleCollisionFrames_Type())
dot3StatsMultipleCollisionFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3StatsMultipleCollisionFrames.setStatus(_A)
_Dot3StatsSQETestErrors_Type=Counter32
_Dot3StatsSQETestErrors_Object=MibTableColumn
dot3StatsSQETestErrors=_Dot3StatsSQETestErrors_Object((1,3,111,2,802,3,1,10,1,2,1,6),_Dot3StatsSQETestErrors_Type())
dot3StatsSQETestErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3StatsSQETestErrors.setStatus(_A)
_Dot3StatsDeferredTransmissions_Type=Counter32
_Dot3StatsDeferredTransmissions_Object=MibTableColumn
dot3StatsDeferredTransmissions=_Dot3StatsDeferredTransmissions_Object((1,3,111,2,802,3,1,10,1,2,1,7),_Dot3StatsDeferredTransmissions_Type())
dot3StatsDeferredTransmissions.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3StatsDeferredTransmissions.setStatus(_A)
_Dot3StatsLateCollisions_Type=Counter32
_Dot3StatsLateCollisions_Object=MibTableColumn
dot3StatsLateCollisions=_Dot3StatsLateCollisions_Object((1,3,111,2,802,3,1,10,1,2,1,8),_Dot3StatsLateCollisions_Type())
dot3StatsLateCollisions.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3StatsLateCollisions.setStatus(_A)
_Dot3StatsExcessiveCollisions_Type=Counter32
_Dot3StatsExcessiveCollisions_Object=MibTableColumn
dot3StatsExcessiveCollisions=_Dot3StatsExcessiveCollisions_Object((1,3,111,2,802,3,1,10,1,2,1,9),_Dot3StatsExcessiveCollisions_Type())
dot3StatsExcessiveCollisions.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3StatsExcessiveCollisions.setStatus(_A)
_Dot3StatsInternalMacTransmitErrors_Type=Counter32
_Dot3StatsInternalMacTransmitErrors_Object=MibTableColumn
dot3StatsInternalMacTransmitErrors=_Dot3StatsInternalMacTransmitErrors_Object((1,3,111,2,802,3,1,10,1,2,1,10),_Dot3StatsInternalMacTransmitErrors_Type())
dot3StatsInternalMacTransmitErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3StatsInternalMacTransmitErrors.setStatus(_A)
_Dot3StatsCarrierSenseErrors_Type=Counter32
_Dot3StatsCarrierSenseErrors_Object=MibTableColumn
dot3StatsCarrierSenseErrors=_Dot3StatsCarrierSenseErrors_Object((1,3,111,2,802,3,1,10,1,2,1,11),_Dot3StatsCarrierSenseErrors_Type())
dot3StatsCarrierSenseErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3StatsCarrierSenseErrors.setStatus(_A)
_Dot3StatsFrameTooLongs_Type=Counter32
_Dot3StatsFrameTooLongs_Object=MibTableColumn
dot3StatsFrameTooLongs=_Dot3StatsFrameTooLongs_Object((1,3,111,2,802,3,1,10,1,2,1,13),_Dot3StatsFrameTooLongs_Type())
dot3StatsFrameTooLongs.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3StatsFrameTooLongs.setStatus(_A)
_Dot3StatsInternalMacReceiveErrors_Type=Counter32
_Dot3StatsInternalMacReceiveErrors_Object=MibTableColumn
dot3StatsInternalMacReceiveErrors=_Dot3StatsInternalMacReceiveErrors_Object((1,3,111,2,802,3,1,10,1,2,1,16),_Dot3StatsInternalMacReceiveErrors_Type())
dot3StatsInternalMacReceiveErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3StatsInternalMacReceiveErrors.setStatus(_A)
_Dot3StatsSymbolErrors_Type=Counter32
_Dot3StatsSymbolErrors_Object=MibTableColumn
dot3StatsSymbolErrors=_Dot3StatsSymbolErrors_Object((1,3,111,2,802,3,1,10,1,2,1,17),_Dot3StatsSymbolErrors_Type())
dot3StatsSymbolErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3StatsSymbolErrors.setStatus(_A)
class _Dot3StatsDuplexStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('halfDuplex',2),('fullDuplex',3)))
_Dot3StatsDuplexStatus_Type.__name__=_D
_Dot3StatsDuplexStatus_Object=MibTableColumn
dot3StatsDuplexStatus=_Dot3StatsDuplexStatus_Object((1,3,111,2,802,3,1,10,1,2,1,18),_Dot3StatsDuplexStatus_Type())
dot3StatsDuplexStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3StatsDuplexStatus.setStatus(_A)
_Dot3StatsRateControlAbility_Type=TruthValue
_Dot3StatsRateControlAbility_Object=MibTableColumn
dot3StatsRateControlAbility=_Dot3StatsRateControlAbility_Object((1,3,111,2,802,3,1,10,1,2,1,19),_Dot3StatsRateControlAbility_Type())
dot3StatsRateControlAbility.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3StatsRateControlAbility.setStatus(_A)
class _Dot3StatsRateControlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rateControlOff',1),('rateControlOn',2),(_G,3)))
_Dot3StatsRateControlStatus_Type.__name__=_D
_Dot3StatsRateControlStatus_Object=MibTableColumn
dot3StatsRateControlStatus=_Dot3StatsRateControlStatus_Object((1,3,111,2,802,3,1,10,1,2,1,20),_Dot3StatsRateControlStatus_Type())
dot3StatsRateControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3StatsRateControlStatus.setStatus(_A)
class _Dot3StatsMaxFrameLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('baseFrame',2),('qTaggedFrame',3),('envelopeFrame',4)))
_Dot3StatsMaxFrameLength_Type.__name__=_D
_Dot3StatsMaxFrameLength_Object=MibTableColumn
dot3StatsMaxFrameLength=_Dot3StatsMaxFrameLength_Object((1,3,111,2,802,3,1,10,1,2,1,21),_Dot3StatsMaxFrameLength_Type())
dot3StatsMaxFrameLength.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3StatsMaxFrameLength.setStatus(_A)
_Dot3CollTable_Object=MibTable
dot3CollTable=_Dot3CollTable_Object((1,3,111,2,802,3,1,10,1,5))
if mibBuilder.loadTexts:dot3CollTable.setStatus(_A)
_Dot3CollEntry_Object=MibTableRow
dot3CollEntry=_Dot3CollEntry_Object((1,3,111,2,802,3,1,10,1,5,1))
dot3CollEntry.setIndexNames((0,_I,_J),(0,_B,_L))
if mibBuilder.loadTexts:dot3CollEntry.setStatus(_A)
class _Dot3CollCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Dot3CollCount_Type.__name__=_D
_Dot3CollCount_Object=MibTableColumn
dot3CollCount=_Dot3CollCount_Object((1,3,111,2,802,3,1,10,1,5,1,2),_Dot3CollCount_Type())
dot3CollCount.setMaxAccess(_K)
if mibBuilder.loadTexts:dot3CollCount.setStatus(_A)
_Dot3CollFrequencies_Type=Counter32
_Dot3CollFrequencies_Object=MibTableColumn
dot3CollFrequencies=_Dot3CollFrequencies_Object((1,3,111,2,802,3,1,10,1,5,1,3),_Dot3CollFrequencies_Type())
dot3CollFrequencies.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3CollFrequencies.setStatus(_A)
_Dot3ControlTable_Object=MibTable
dot3ControlTable=_Dot3ControlTable_Object((1,3,111,2,802,3,1,10,1,9))
if mibBuilder.loadTexts:dot3ControlTable.setStatus(_A)
_Dot3ControlEntry_Object=MibTableRow
dot3ControlEntry=_Dot3ControlEntry_Object((1,3,111,2,802,3,1,10,1,9,1))
dot3ControlEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:dot3ControlEntry.setStatus(_A)
class _Dot3ControlFunctionsSupported_Type(Bits):namedValues=NamedValues(*(('pause',0),('mpcp',1),('pfc',2)))
_Dot3ControlFunctionsSupported_Type.__name__='Bits'
_Dot3ControlFunctionsSupported_Object=MibTableColumn
dot3ControlFunctionsSupported=_Dot3ControlFunctionsSupported_Object((1,3,111,2,802,3,1,10,1,9,1,1),_Dot3ControlFunctionsSupported_Type())
dot3ControlFunctionsSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3ControlFunctionsSupported.setStatus(_A)
_Dot3ControlInUnknownOpcodes_Type=Counter32
_Dot3ControlInUnknownOpcodes_Object=MibTableColumn
dot3ControlInUnknownOpcodes=_Dot3ControlInUnknownOpcodes_Object((1,3,111,2,802,3,1,10,1,9,1,2),_Dot3ControlInUnknownOpcodes_Type())
dot3ControlInUnknownOpcodes.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3ControlInUnknownOpcodes.setStatus(_A)
_Dot3HCControlInUnknownOpcodes_Type=Counter64
_Dot3HCControlInUnknownOpcodes_Object=MibTableColumn
dot3HCControlInUnknownOpcodes=_Dot3HCControlInUnknownOpcodes_Object((1,3,111,2,802,3,1,10,1,9,1,3),_Dot3HCControlInUnknownOpcodes_Type())
dot3HCControlInUnknownOpcodes.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3HCControlInUnknownOpcodes.setStatus(_A)
_Dot3PauseTable_Object=MibTable
dot3PauseTable=_Dot3PauseTable_Object((1,3,111,2,802,3,1,10,1,10))
if mibBuilder.loadTexts:dot3PauseTable.setStatus(_A)
_Dot3PauseEntry_Object=MibTableRow
dot3PauseEntry=_Dot3PauseEntry_Object((1,3,111,2,802,3,1,10,1,10,1))
dot3PauseEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:dot3PauseEntry.setStatus(_A)
class _Dot3PauseAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_M,2),(_N,3),(_O,4)))
_Dot3PauseAdminMode_Type.__name__=_D
_Dot3PauseAdminMode_Object=MibTableColumn
dot3PauseAdminMode=_Dot3PauseAdminMode_Object((1,3,111,2,802,3,1,10,1,10,1,1),_Dot3PauseAdminMode_Type())
dot3PauseAdminMode.setMaxAccess(_H)
if mibBuilder.loadTexts:dot3PauseAdminMode.setStatus(_A)
class _Dot3PauseOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_M,2),(_N,3),(_O,4)))
_Dot3PauseOperMode_Type.__name__=_D
_Dot3PauseOperMode_Object=MibTableColumn
dot3PauseOperMode=_Dot3PauseOperMode_Object((1,3,111,2,802,3,1,10,1,10,1,2),_Dot3PauseOperMode_Type())
dot3PauseOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3PauseOperMode.setStatus(_A)
_Dot3InPauseFrames_Type=Counter32
_Dot3InPauseFrames_Object=MibTableColumn
dot3InPauseFrames=_Dot3InPauseFrames_Object((1,3,111,2,802,3,1,10,1,10,1,3),_Dot3InPauseFrames_Type())
dot3InPauseFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3InPauseFrames.setStatus(_A)
_Dot3OutPauseFrames_Type=Counter32
_Dot3OutPauseFrames_Object=MibTableColumn
dot3OutPauseFrames=_Dot3OutPauseFrames_Object((1,3,111,2,802,3,1,10,1,10,1,4),_Dot3OutPauseFrames_Type())
dot3OutPauseFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3OutPauseFrames.setStatus(_A)
_Dot3HCInPauseFrames_Type=Counter64
_Dot3HCInPauseFrames_Object=MibTableColumn
dot3HCInPauseFrames=_Dot3HCInPauseFrames_Object((1,3,111,2,802,3,1,10,1,10,1,5),_Dot3HCInPauseFrames_Type())
dot3HCInPauseFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3HCInPauseFrames.setStatus(_A)
_Dot3HCOutPauseFrames_Type=Counter64
_Dot3HCOutPauseFrames_Object=MibTableColumn
dot3HCOutPauseFrames=_Dot3HCOutPauseFrames_Object((1,3,111,2,802,3,1,10,1,10,1,6),_Dot3HCOutPauseFrames_Type())
dot3HCOutPauseFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3HCOutPauseFrames.setStatus(_A)
_Dot3HCStatsTable_Object=MibTable
dot3HCStatsTable=_Dot3HCStatsTable_Object((1,3,111,2,802,3,1,10,1,11))
if mibBuilder.loadTexts:dot3HCStatsTable.setStatus(_A)
_Dot3HCStatsEntry_Object=MibTableRow
dot3HCStatsEntry=_Dot3HCStatsEntry_Object((1,3,111,2,802,3,1,10,1,11,1))
dot3HCStatsEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:dot3HCStatsEntry.setStatus(_A)
_Dot3HCStatsAlignmentErrors_Type=Counter64
_Dot3HCStatsAlignmentErrors_Object=MibTableColumn
dot3HCStatsAlignmentErrors=_Dot3HCStatsAlignmentErrors_Object((1,3,111,2,802,3,1,10,1,11,1,1),_Dot3HCStatsAlignmentErrors_Type())
dot3HCStatsAlignmentErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3HCStatsAlignmentErrors.setStatus(_A)
_Dot3HCStatsFCSErrors_Type=Counter64
_Dot3HCStatsFCSErrors_Object=MibTableColumn
dot3HCStatsFCSErrors=_Dot3HCStatsFCSErrors_Object((1,3,111,2,802,3,1,10,1,11,1,2),_Dot3HCStatsFCSErrors_Type())
dot3HCStatsFCSErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3HCStatsFCSErrors.setStatus(_A)
_Dot3HCStatsInternalMacTransmitErrors_Type=Counter64
_Dot3HCStatsInternalMacTransmitErrors_Object=MibTableColumn
dot3HCStatsInternalMacTransmitErrors=_Dot3HCStatsInternalMacTransmitErrors_Object((1,3,111,2,802,3,1,10,1,11,1,3),_Dot3HCStatsInternalMacTransmitErrors_Type())
dot3HCStatsInternalMacTransmitErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3HCStatsInternalMacTransmitErrors.setStatus(_A)
_Dot3HCStatsFrameTooLongs_Type=Counter64
_Dot3HCStatsFrameTooLongs_Object=MibTableColumn
dot3HCStatsFrameTooLongs=_Dot3HCStatsFrameTooLongs_Object((1,3,111,2,802,3,1,10,1,11,1,4),_Dot3HCStatsFrameTooLongs_Type())
dot3HCStatsFrameTooLongs.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3HCStatsFrameTooLongs.setStatus(_A)
_Dot3HCStatsInternalMacReceiveErrors_Type=Counter64
_Dot3HCStatsInternalMacReceiveErrors_Object=MibTableColumn
dot3HCStatsInternalMacReceiveErrors=_Dot3HCStatsInternalMacReceiveErrors_Object((1,3,111,2,802,3,1,10,1,11,1,5),_Dot3HCStatsInternalMacReceiveErrors_Type())
dot3HCStatsInternalMacReceiveErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3HCStatsInternalMacReceiveErrors.setStatus(_A)
_Dot3HCStatsSymbolErrors_Type=Counter64
_Dot3HCStatsSymbolErrors_Object=MibTableColumn
dot3HCStatsSymbolErrors=_Dot3HCStatsSymbolErrors_Object((1,3,111,2,802,3,1,10,1,11,1,6),_Dot3HCStatsSymbolErrors_Type())
dot3HCStatsSymbolErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3HCStatsSymbolErrors.setStatus(_A)
_Dot3HCStatsTransmitLPIMicroseconds_Type=Counter64
_Dot3HCStatsTransmitLPIMicroseconds_Object=MibTableColumn
dot3HCStatsTransmitLPIMicroseconds=_Dot3HCStatsTransmitLPIMicroseconds_Object((1,3,111,2,802,3,1,10,1,11,1,7),_Dot3HCStatsTransmitLPIMicroseconds_Type())
dot3HCStatsTransmitLPIMicroseconds.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3HCStatsTransmitLPIMicroseconds.setStatus(_A)
_Dot3HCStatsReceiveLPIMicroseconds_Type=Counter64
_Dot3HCStatsReceiveLPIMicroseconds_Object=MibTableColumn
dot3HCStatsReceiveLPIMicroseconds=_Dot3HCStatsReceiveLPIMicroseconds_Object((1,3,111,2,802,3,1,10,1,11,1,8),_Dot3HCStatsReceiveLPIMicroseconds_Type())
dot3HCStatsReceiveLPIMicroseconds.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3HCStatsReceiveLPIMicroseconds.setStatus(_A)
_Dot3HCStatsTransmitLPITransitions_Type=Counter64
_Dot3HCStatsTransmitLPITransitions_Object=MibTableColumn
dot3HCStatsTransmitLPITransitions=_Dot3HCStatsTransmitLPITransitions_Object((1,3,111,2,802,3,1,10,1,11,1,9),_Dot3HCStatsTransmitLPITransitions_Type())
dot3HCStatsTransmitLPITransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3HCStatsTransmitLPITransitions.setStatus(_A)
_Dot3HCStatsReceiveLPITransitions_Type=Counter64
_Dot3HCStatsReceiveLPITransitions_Object=MibTableColumn
dot3HCStatsReceiveLPITransitions=_Dot3HCStatsReceiveLPITransitions_Object((1,3,111,2,802,3,1,10,1,11,1,10),_Dot3HCStatsReceiveLPITransitions_Type())
dot3HCStatsReceiveLPITransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3HCStatsReceiveLPITransitions.setStatus(_A)
class _Dot3SlowProtocolFrameLimit_Type(Integer32):defaultValue=10
_Dot3SlowProtocolFrameLimit_Type.__name__=_D
_Dot3SlowProtocolFrameLimit_Object=MibScalar
dot3SlowProtocolFrameLimit=_Dot3SlowProtocolFrameLimit_Object((1,3,111,2,802,3,1,10,1,12),_Dot3SlowProtocolFrameLimit_Type())
dot3SlowProtocolFrameLimit.setMaxAccess(_H)
if mibBuilder.loadTexts:dot3SlowProtocolFrameLimit.setStatus(_A)
_Dot3ExtensionTable_Object=MibTable
dot3ExtensionTable=_Dot3ExtensionTable_Object((1,3,111,2,802,3,1,10,1,13))
if mibBuilder.loadTexts:dot3ExtensionTable.setStatus(_A)
_Dot3ExtensionEntry_Object=MibTableRow
dot3ExtensionEntry=_Dot3ExtensionEntry_Object((1,3,111,2,802,3,1,10,1,13,1))
dot3ExtensionEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:dot3ExtensionEntry.setStatus(_A)
_Dot3HCInExtensionFrames_Type=Counter64
_Dot3HCInExtensionFrames_Object=MibTableColumn
dot3HCInExtensionFrames=_Dot3HCInExtensionFrames_Object((1,3,111,2,802,3,1,10,1,13,1,1),_Dot3HCInExtensionFrames_Type())
dot3HCInExtensionFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3HCInExtensionFrames.setStatus(_A)
_Dot3HCOutExtensionFrames_Type=Counter64
_Dot3HCOutExtensionFrames_Object=MibTableColumn
dot3HCOutExtensionFrames=_Dot3HCOutExtensionFrames_Object((1,3,111,2,802,3,1,10,1,13,1,2),_Dot3HCOutExtensionFrames_Type())
dot3HCOutExtensionFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3HCOutExtensionFrames.setStatus(_A)
_Dot3ExtensionMacCtrlStatus_Type=Unsigned32
_Dot3ExtensionMacCtrlStatus_Object=MibTableColumn
dot3ExtensionMacCtrlStatus=_Dot3ExtensionMacCtrlStatus_Object((1,3,111,2,802,3,1,10,1,13,1,3),_Dot3ExtensionMacCtrlStatus_Type())
dot3ExtensionMacCtrlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3ExtensionMacCtrlStatus.setStatus(_A)
_Dot3PFCTable_Object=MibTable
dot3PFCTable=_Dot3PFCTable_Object((1,3,111,2,802,3,1,10,1,14))
if mibBuilder.loadTexts:dot3PFCTable.setStatus(_A)
_Dot3PFCEntry_Object=MibTableRow
dot3PFCEntry=_Dot3PFCEntry_Object((1,3,111,2,802,3,1,10,1,14,1))
dot3PFCEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:dot3PFCEntry.setStatus(_A)
class _Dot3PFCAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_P,2)))
_Dot3PFCAdminMode_Type.__name__=_D
_Dot3PFCAdminMode_Object=MibTableColumn
dot3PFCAdminMode=_Dot3PFCAdminMode_Object((1,3,111,2,802,3,1,10,1,14,1,1),_Dot3PFCAdminMode_Type())
dot3PFCAdminMode.setMaxAccess(_H)
if mibBuilder.loadTexts:dot3PFCAdminMode.setStatus(_A)
class _Dot3PFCOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_P,2)))
_Dot3PFCOperMode_Type.__name__=_D
_Dot3PFCOperMode_Object=MibTableColumn
dot3PFCOperMode=_Dot3PFCOperMode_Object((1,3,111,2,802,3,1,10,1,14,1,2),_Dot3PFCOperMode_Type())
dot3PFCOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3PFCOperMode.setStatus(_A)
_Dot3HCInPFCFrames_Type=Counter64
_Dot3HCInPFCFrames_Object=MibTableColumn
dot3HCInPFCFrames=_Dot3HCInPFCFrames_Object((1,3,111,2,802,3,1,10,1,14,1,3),_Dot3HCInPFCFrames_Type())
dot3HCInPFCFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3HCInPFCFrames.setStatus(_A)
_Dot3HCOutPFCFrames_Type=Counter64
_Dot3HCOutPFCFrames_Object=MibTableColumn
dot3HCOutPFCFrames=_Dot3HCOutPFCFrames_Object((1,3,111,2,802,3,1,10,1,14,1,4),_Dot3HCOutPFCFrames_Type())
dot3HCOutPFCFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:dot3HCOutPFCFrames.setStatus(_A)
_EtherConformance_ObjectIdentity=ObjectIdentity
etherConformance=_EtherConformance_ObjectIdentity((1,3,111,2,802,3,1,10,2))
_EtherGroups_ObjectIdentity=ObjectIdentity
etherGroups=_EtherGroups_ObjectIdentity((1,3,111,2,802,3,1,10,2,1))
_EtherCompliances_ObjectIdentity=ObjectIdentity
etherCompliances=_EtherCompliances_ObjectIdentity((1,3,111,2,802,3,1,10,2,2))
etherCollisionTableGroup=ObjectGroup((1,3,111,2,802,3,1,10,2,1,1))
etherCollisionTableGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:etherCollisionTableGroup.setStatus(_A)
etherStatsLowSpeedGroup=ObjectGroup((1,3,111,2,802,3,1,10,2,1,2))
etherStatsLowSpeedGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:etherStatsLowSpeedGroup.setStatus(_A)
etherStatsHighSpeedGroup=ObjectGroup((1,3,111,2,802,3,1,10,2,1,3))
etherStatsHighSpeedGroup.setObjects((_B,_S))
if mibBuilder.loadTexts:etherStatsHighSpeedGroup.setStatus(_A)
etherDuplexGroup=ObjectGroup((1,3,111,2,802,3,1,10,2,1,4))
etherDuplexGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:etherDuplexGroup.setStatus(_A)
etherControlGroup=ObjectGroup((1,3,111,2,802,3,1,10,2,1,5))
etherControlGroup.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:etherControlGroup.setStatus(_A)
etherControlPauseGroup=ObjectGroup((1,3,111,2,802,3,1,10,2,1,6))
etherControlPauseGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:etherControlPauseGroup.setStatus(_A)
etherStatsBaseGroup2=ObjectGroup((1,3,111,2,802,3,1,10,2,1,7))
etherStatsBaseGroup2.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:etherStatsBaseGroup2.setStatus(_A)
etherStatsHalfDuplexGroup=ObjectGroup((1,3,111,2,802,3,1,10,2,1,8))
etherStatsHalfDuplexGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:etherStatsHalfDuplexGroup.setStatus(_A)
etherHCStatsGroup=ObjectGroup((1,3,111,2,802,3,1,10,2,1,9))
etherHCStatsGroup.setObjects(*((_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:etherHCStatsGroup.setStatus(_A)
etherHCControlGroup=ObjectGroup((1,3,111,2,802,3,1,10,2,1,10))
etherHCControlGroup.setObjects((_B,_s))
if mibBuilder.loadTexts:etherHCControlGroup.setStatus(_A)
etherHCControlPauseGroup=ObjectGroup((1,3,111,2,802,3,1,10,2,1,11))
etherHCControlPauseGroup.setObjects(*((_B,_t),(_B,_u)))
if mibBuilder.loadTexts:etherHCControlPauseGroup.setStatus(_A)
etherRateControlGroup=ObjectGroup((1,3,111,2,802,3,1,10,2,1,12))
etherRateControlGroup.setObjects(*((_B,_v),(_B,_w)))
if mibBuilder.loadTexts:etherRateControlGroup.setStatus(_A)
etherHCStatsLpiGroup=ObjectGroup((1,3,111,2,802,3,1,10,2,1,13))
etherHCStatsLpiGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:etherHCStatsLpiGroup.setStatus(_A)
etherSlowProtocolsGroup=ObjectGroup((1,3,111,2,802,3,1,10,2,1,14))
etherSlowProtocolsGroup.setObjects((_B,_A1))
if mibBuilder.loadTexts:etherSlowProtocolsGroup.setStatus(_A)
etherExtensionMacCtrlGroup=ObjectGroup((1,3,111,2,802,3,1,10,2,1,15))
etherExtensionMacCtrlGroup.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:etherExtensionMacCtrlGroup.setStatus(_A)
etherPfcGroup=ObjectGroup((1,3,111,2,802,3,1,10,2,1,16))
etherPfcGroup.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:etherPfcGroup.setStatus(_A)
dot3Compliance2=ModuleCompliance((1,3,111,2,802,3,1,10,2,2,1))
dot3Compliance2.setObjects(*((_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO)))
if mibBuilder.loadTexts:dot3Compliance2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ieee8023etherMIB':ieee8023etherMIB,'ieee8023etherMIBObjects':ieee8023etherMIBObjects,'dot3StatsTable':dot3StatsTable,'dot3StatsEntry':dot3StatsEntry,_E:dot3StatsIndex,_a:dot3StatsAlignmentErrors,_b:dot3StatsFCSErrors,_g:dot3StatsSingleCollisionFrames,_h:dot3StatsMultipleCollisionFrames,_R:dot3StatsSQETestErrors,_i:dot3StatsDeferredTransmissions,_j:dot3StatsLateCollisions,_k:dot3StatsExcessiveCollisions,_c:dot3StatsInternalMacTransmitErrors,_l:dot3StatsCarrierSenseErrors,_d:dot3StatsFrameTooLongs,_e:dot3StatsInternalMacReceiveErrors,_S:dot3StatsSymbolErrors,_T:dot3StatsDuplexStatus,_v:dot3StatsRateControlAbility,_w:dot3StatsRateControlStatus,_f:dot3StatsMaxFrameLength,'dot3CollTable':dot3CollTable,'dot3CollEntry':dot3CollEntry,_L:dot3CollCount,_Q:dot3CollFrequencies,'dot3ControlTable':dot3ControlTable,'dot3ControlEntry':dot3ControlEntry,_U:dot3ControlFunctionsSupported,_V:dot3ControlInUnknownOpcodes,_s:dot3HCControlInUnknownOpcodes,'dot3PauseTable':dot3PauseTable,'dot3PauseEntry':dot3PauseEntry,_W:dot3PauseAdminMode,_X:dot3PauseOperMode,_Y:dot3InPauseFrames,_Z:dot3OutPauseFrames,_t:dot3HCInPauseFrames,_u:dot3HCOutPauseFrames,'dot3HCStatsTable':dot3HCStatsTable,'dot3HCStatsEntry':dot3HCStatsEntry,_m:dot3HCStatsAlignmentErrors,_n:dot3HCStatsFCSErrors,_o:dot3HCStatsInternalMacTransmitErrors,_p:dot3HCStatsFrameTooLongs,_q:dot3HCStatsInternalMacReceiveErrors,_r:dot3HCStatsSymbolErrors,_x:dot3HCStatsTransmitLPIMicroseconds,_y:dot3HCStatsReceiveLPIMicroseconds,_z:dot3HCStatsTransmitLPITransitions,_A0:dot3HCStatsReceiveLPITransitions,_A1:dot3SlowProtocolFrameLimit,'dot3ExtensionTable':dot3ExtensionTable,'dot3ExtensionEntry':dot3ExtensionEntry,_A2:dot3HCInExtensionFrames,_A3:dot3HCOutExtensionFrames,_A4:dot3ExtensionMacCtrlStatus,'dot3PFCTable':dot3PFCTable,'dot3PFCEntry':dot3PFCEntry,_A5:dot3PFCAdminMode,_A6:dot3PFCOperMode,_A7:dot3HCInPFCFrames,_A8:dot3HCOutPFCFrames,'etherConformance':etherConformance,'etherGroups':etherGroups,_AK:etherCollisionTableGroup,_AC:etherStatsLowSpeedGroup,_AD:etherStatsHighSpeedGroup,_AA:etherDuplexGroup,_AG:etherControlGroup,_AI:etherControlPauseGroup,_A9:etherStatsBaseGroup2,_AE:etherStatsHalfDuplexGroup,_AF:etherHCStatsGroup,_AH:etherHCControlGroup,_AJ:etherHCControlPauseGroup,_AB:etherRateControlGroup,_AL:etherHCStatsLpiGroup,_AM:etherSlowProtocolsGroup,_AN:etherExtensionMacCtrlGroup,_AO:etherPfcGroup,'etherCompliances':etherCompliances,'dot3Compliance2':dot3Compliance2})