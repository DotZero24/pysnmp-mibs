_Am='cctmXHistoryGroup'
_Al='cctmHistoryGroup'
_Ak='cctmActiveGroup'
_Aj='cctmXHistoryECWindowClosures'
_Ai='cctmXHistoryV90ClientId'
_Ah='cctmXHistoryV90Failure'
_Ag='cctmXHistoryV90Status'
_Af='cctmXHistoryConstellation'
_Ae='cctmXHistoryTxLevel'
_Ad='cctmXHistoryRxLevel'
_Ac='cctmXHistoryTxECWindowSize'
_Ab='cctmXHistoryRxECWindowSize'
_Aa='cctmXHistoryTxECInfoFrameSize'
_AZ='cctmXHistoryRxECInfoFrameSize'
_AY='cctmHistoryDisconnectReasonText'
_AX='cctmHistoryDisconnectReason'
_AW='cctmHistoryRxCharLost'
_AV='cctmHistoryECLinkTimeouts'
_AU='cctmHistoryECFramesResent'
_AT='cctmHistoryRxECFramesBad'
_AS='cctmHistoryTxECNAKs'
_AR='cctmHistoryRxECNAKs'
_AQ='cctmHistoryTxECFrames'
_AP='cctmHistoryRxECFrames'
_AO='cctmHistoryTxLinkOctets'
_AN='cctmHistoryRxLinkOctets'
_AM='cctmHistoryRetrainFailures'
_AL='cctmHistoryRemoteRetrains'
_AK='cctmHistoryLocalRetrains'
_AJ='cctmHistoryRateShiftFailures'
_AI='cctmHistoryRemoteDownRateShifts'
_AH='cctmHistoryLocalDownRateShifts'
_AG='cctmHistoryRemoteUpRateShifts'
_AF='cctmHistoryLocalUpRateShifts'
_AE='cctmHistoryTxLowWatermark'
_AD='cctmHistoryTxHighWatermark'
_AC='cctmHistoryRxLowWatermark'
_AB='cctmHistoryRxHighWatermark'
_AA='cctmHistoryDataCompression'
_A9='cctmHistorySupportedDC'
_A8='cctmHistoryECProtocol'
_A7='cctmHistoryAttemptedECProtocol'
_A6='cctmHistoryFinalModulation'
_A5='cctmHistoryInitialModulation'
_A4='cctmHistoryAttemptedModulation'
_A3='cctmHistoryFinalTxRate'
_A2='cctmHistoryFinalRxRate'
_A1='cctmHistoryProjectedMaxTxRate'
_A0='cctmHistoryProjectedMaxRxRate'
_z='cctmActiveRxCharLost'
_y='cctmActiveECLinkTimeouts'
_x='cctmActiveECFramesResent'
_w='cctmActiveRxECFramesBad'
_v='cctmActiveTxECNAKs'
_u='cctmActiveRxECNAKs'
_t='cctmActiveTxECFrames'
_s='cctmActiveRxECFrames'
_r='cctmActiveTxLinkOctets'
_q='cctmActiveRxLinkOctets'
_p='cctmActiveRetrainFailures'
_o='cctmActiveRemoteRetrains'
_n='cctmActiveLocalRetrains'
_m='cctmActiveRateShiftFailures'
_l='cctmActiveRemoteDownRateShifts'
_k='cctmActiveLocalDownRateShifts'
_j='cctmActiveRemoteUpRateShifts'
_i='cctmActiveLocalUpRateShifts'
_h='cctmActiveTxLowWatermark'
_g='cctmActiveTxHighWatermark'
_f='cctmActiveRxLowWatermark'
_e='cctmActiveRxHighWatermark'
_d='cctmActiveDataCompression'
_c='cctmActiveSupportedDC'
_b='cctmActiveECProtocol'
_a='cctmActiveAttemptedECProtocol'
_Z='cctmActiveModulation'
_Y='cctmActiveInitialModulation'
_X='cctmActiveAttemptedModulation'
_W='cctmActiveTxRate'
_V='cctmActiveRxRate'
_U='cctmActiveProjectedMaxTxRate'
_T='cctmActiveProjectedMaxRxRate'
_S='cctmXHistoryEntry'
_R='frames'
_Q='octets'
_P='DisplayString'
_O='Unsigned32'
_N='cctHistoryIndex'
_M='cctActiveCallId'
_L='v44Rx'
_K='v44Tx'
_J='mnp5'
_I='v42bisRx'
_H='v42bisTx'
_G='Bits'
_F='CISCO-CALL-TRACKER-MIB'
_E='Integer32'
_D='bits per second'
_C='read-only'
_B='CISCO-CALL-TRACKER-MODEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cctActiveCallId,cctHistoryIndex=mibBuilder.importSymbols(_F,_M,_N)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_G,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_O,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_P,'PhysAddress','TextualConvention')
ciscoCallTrackerModemMIB=ModuleIdentity((1,3,6,1,4,1,9,9,165))
if mibBuilder.loadTexts:ciscoCallTrackerModemMIB.setRevisions(('2005-12-06 00:00','2001-12-14 00:00'))
class CctmModulation(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*(('other',1),('bell103a',2),('bell212a',3),('v21',4),('v22',5),('v22bis',6),('v32',7),('v32bis',8),('vfc',9),('v34',10),('v17',11),('v29',12),('v33',13),('k56flex',14),('v23',15),('v32terbo',16),('v34plus',17),('v90',18),('v27ter',19),('v110',20)))
class CctmECProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('normal',1),('direct',2),('mnp',3),('lapmV42',4),('syncMode',5),('asyncMode',6),('ara1',7),('ara2',8),('other',9)))
class CctmDataCompression(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('none',1),(_H,2),(_I,3),('v42bisBoth',4),(_J,5),(_K,6),(_L,7),('v44Both',8)))
_CctmMIBObjects_ObjectIdentity=ObjectIdentity
cctmMIBObjects=_CctmMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,165,1))
_CctmActive_ObjectIdentity=ObjectIdentity
cctmActive=_CctmActive_ObjectIdentity((1,3,6,1,4,1,9,9,165,1,1))
_CctmActiveTable_Object=MibTable
cctmActiveTable=_CctmActiveTable_Object((1,3,6,1,4,1,9,9,165,1,1,1))
if mibBuilder.loadTexts:cctmActiveTable.setStatus(_A)
_CctmActiveEntry_Object=MibTableRow
cctmActiveEntry=_CctmActiveEntry_Object((1,3,6,1,4,1,9,9,165,1,1,1,1))
cctmActiveEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:cctmActiveEntry.setStatus(_A)
_CctmActiveProjectedMaxRxRate_Type=Unsigned32
_CctmActiveProjectedMaxRxRate_Object=MibTableColumn
cctmActiveProjectedMaxRxRate=_CctmActiveProjectedMaxRxRate_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,1),_CctmActiveProjectedMaxRxRate_Type())
cctmActiveProjectedMaxRxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveProjectedMaxRxRate.setStatus(_A)
if mibBuilder.loadTexts:cctmActiveProjectedMaxRxRate.setUnits(_D)
_CctmActiveProjectedMaxTxRate_Type=Unsigned32
_CctmActiveProjectedMaxTxRate_Object=MibTableColumn
cctmActiveProjectedMaxTxRate=_CctmActiveProjectedMaxTxRate_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,2),_CctmActiveProjectedMaxTxRate_Type())
cctmActiveProjectedMaxTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveProjectedMaxTxRate.setStatus(_A)
if mibBuilder.loadTexts:cctmActiveProjectedMaxTxRate.setUnits(_D)
_CctmActiveRxRate_Type=Unsigned32
_CctmActiveRxRate_Object=MibTableColumn
cctmActiveRxRate=_CctmActiveRxRate_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,3),_CctmActiveRxRate_Type())
cctmActiveRxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveRxRate.setStatus(_A)
if mibBuilder.loadTexts:cctmActiveRxRate.setUnits(_D)
_CctmActiveTxRate_Type=Unsigned32
_CctmActiveTxRate_Object=MibTableColumn
cctmActiveTxRate=_CctmActiveTxRate_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,4),_CctmActiveTxRate_Type())
cctmActiveTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveTxRate.setStatus(_A)
if mibBuilder.loadTexts:cctmActiveTxRate.setUnits(_D)
_CctmActiveAttemptedModulation_Type=CctmModulation
_CctmActiveAttemptedModulation_Object=MibTableColumn
cctmActiveAttemptedModulation=_CctmActiveAttemptedModulation_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,5),_CctmActiveAttemptedModulation_Type())
cctmActiveAttemptedModulation.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveAttemptedModulation.setStatus(_A)
_CctmActiveInitialModulation_Type=CctmModulation
_CctmActiveInitialModulation_Object=MibTableColumn
cctmActiveInitialModulation=_CctmActiveInitialModulation_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,6),_CctmActiveInitialModulation_Type())
cctmActiveInitialModulation.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveInitialModulation.setStatus(_A)
_CctmActiveModulation_Type=CctmModulation
_CctmActiveModulation_Object=MibTableColumn
cctmActiveModulation=_CctmActiveModulation_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,7),_CctmActiveModulation_Type())
cctmActiveModulation.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveModulation.setStatus(_A)
_CctmActiveAttemptedECProtocol_Type=CctmECProtocol
_CctmActiveAttemptedECProtocol_Object=MibTableColumn
cctmActiveAttemptedECProtocol=_CctmActiveAttemptedECProtocol_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,8),_CctmActiveAttemptedECProtocol_Type())
cctmActiveAttemptedECProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveAttemptedECProtocol.setStatus(_A)
_CctmActiveECProtocol_Type=CctmECProtocol
_CctmActiveECProtocol_Object=MibTableColumn
cctmActiveECProtocol=_CctmActiveECProtocol_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,9),_CctmActiveECProtocol_Type())
cctmActiveECProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveECProtocol.setStatus(_A)
class _CctmActiveSupportedDC_Type(Bits):namedValues=NamedValues(*((_J,0),(_I,1),(_H,2),(_L,3),(_K,4)))
_CctmActiveSupportedDC_Type.__name__=_G
_CctmActiveSupportedDC_Object=MibTableColumn
cctmActiveSupportedDC=_CctmActiveSupportedDC_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,10),_CctmActiveSupportedDC_Type())
cctmActiveSupportedDC.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveSupportedDC.setStatus(_A)
_CctmActiveDataCompression_Type=CctmDataCompression
_CctmActiveDataCompression_Object=MibTableColumn
cctmActiveDataCompression=_CctmActiveDataCompression_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,11),_CctmActiveDataCompression_Type())
cctmActiveDataCompression.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveDataCompression.setStatus(_A)
_CctmActiveRxHighWatermark_Type=Gauge32
_CctmActiveRxHighWatermark_Object=MibTableColumn
cctmActiveRxHighWatermark=_CctmActiveRxHighWatermark_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,12),_CctmActiveRxHighWatermark_Type())
cctmActiveRxHighWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveRxHighWatermark.setStatus(_A)
if mibBuilder.loadTexts:cctmActiveRxHighWatermark.setUnits(_D)
_CctmActiveRxLowWatermark_Type=Gauge32
_CctmActiveRxLowWatermark_Object=MibTableColumn
cctmActiveRxLowWatermark=_CctmActiveRxLowWatermark_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,13),_CctmActiveRxLowWatermark_Type())
cctmActiveRxLowWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveRxLowWatermark.setStatus(_A)
if mibBuilder.loadTexts:cctmActiveRxLowWatermark.setUnits(_D)
_CctmActiveTxHighWatermark_Type=Gauge32
_CctmActiveTxHighWatermark_Object=MibTableColumn
cctmActiveTxHighWatermark=_CctmActiveTxHighWatermark_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,14),_CctmActiveTxHighWatermark_Type())
cctmActiveTxHighWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveTxHighWatermark.setStatus(_A)
if mibBuilder.loadTexts:cctmActiveTxHighWatermark.setUnits(_D)
_CctmActiveTxLowWatermark_Type=Gauge32
_CctmActiveTxLowWatermark_Object=MibTableColumn
cctmActiveTxLowWatermark=_CctmActiveTxLowWatermark_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,15),_CctmActiveTxLowWatermark_Type())
cctmActiveTxLowWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveTxLowWatermark.setStatus(_A)
if mibBuilder.loadTexts:cctmActiveTxLowWatermark.setUnits(_D)
_CctmActiveLocalUpRateShifts_Type=Counter32
_CctmActiveLocalUpRateShifts_Object=MibTableColumn
cctmActiveLocalUpRateShifts=_CctmActiveLocalUpRateShifts_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,16),_CctmActiveLocalUpRateShifts_Type())
cctmActiveLocalUpRateShifts.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveLocalUpRateShifts.setStatus(_A)
_CctmActiveLocalDownRateShifts_Type=Counter32
_CctmActiveLocalDownRateShifts_Object=MibTableColumn
cctmActiveLocalDownRateShifts=_CctmActiveLocalDownRateShifts_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,17),_CctmActiveLocalDownRateShifts_Type())
cctmActiveLocalDownRateShifts.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveLocalDownRateShifts.setStatus(_A)
_CctmActiveRemoteUpRateShifts_Type=Counter32
_CctmActiveRemoteUpRateShifts_Object=MibTableColumn
cctmActiveRemoteUpRateShifts=_CctmActiveRemoteUpRateShifts_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,18),_CctmActiveRemoteUpRateShifts_Type())
cctmActiveRemoteUpRateShifts.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveRemoteUpRateShifts.setStatus(_A)
_CctmActiveRemoteDownRateShifts_Type=Counter32
_CctmActiveRemoteDownRateShifts_Object=MibTableColumn
cctmActiveRemoteDownRateShifts=_CctmActiveRemoteDownRateShifts_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,19),_CctmActiveRemoteDownRateShifts_Type())
cctmActiveRemoteDownRateShifts.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveRemoteDownRateShifts.setStatus(_A)
_CctmActiveRateShiftFailures_Type=Counter32
_CctmActiveRateShiftFailures_Object=MibTableColumn
cctmActiveRateShiftFailures=_CctmActiveRateShiftFailures_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,20),_CctmActiveRateShiftFailures_Type())
cctmActiveRateShiftFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveRateShiftFailures.setStatus(_A)
_CctmActiveLocalRetrains_Type=Counter32
_CctmActiveLocalRetrains_Object=MibTableColumn
cctmActiveLocalRetrains=_CctmActiveLocalRetrains_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,21),_CctmActiveLocalRetrains_Type())
cctmActiveLocalRetrains.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveLocalRetrains.setStatus(_A)
_CctmActiveRemoteRetrains_Type=Counter32
_CctmActiveRemoteRetrains_Object=MibTableColumn
cctmActiveRemoteRetrains=_CctmActiveRemoteRetrains_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,22),_CctmActiveRemoteRetrains_Type())
cctmActiveRemoteRetrains.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveRemoteRetrains.setStatus(_A)
_CctmActiveRetrainFailures_Type=Counter32
_CctmActiveRetrainFailures_Object=MibTableColumn
cctmActiveRetrainFailures=_CctmActiveRetrainFailures_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,23),_CctmActiveRetrainFailures_Type())
cctmActiveRetrainFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveRetrainFailures.setStatus(_A)
_CctmActiveRxLinkOctets_Type=Counter32
_CctmActiveRxLinkOctets_Object=MibTableColumn
cctmActiveRxLinkOctets=_CctmActiveRxLinkOctets_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,24),_CctmActiveRxLinkOctets_Type())
cctmActiveRxLinkOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveRxLinkOctets.setStatus(_A)
_CctmActiveTxLinkOctets_Type=Counter32
_CctmActiveTxLinkOctets_Object=MibTableColumn
cctmActiveTxLinkOctets=_CctmActiveTxLinkOctets_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,25),_CctmActiveTxLinkOctets_Type())
cctmActiveTxLinkOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveTxLinkOctets.setStatus(_A)
_CctmActiveRxECFrames_Type=Counter32
_CctmActiveRxECFrames_Object=MibTableColumn
cctmActiveRxECFrames=_CctmActiveRxECFrames_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,26),_CctmActiveRxECFrames_Type())
cctmActiveRxECFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveRxECFrames.setStatus(_A)
_CctmActiveTxECFrames_Type=Counter32
_CctmActiveTxECFrames_Object=MibTableColumn
cctmActiveTxECFrames=_CctmActiveTxECFrames_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,27),_CctmActiveTxECFrames_Type())
cctmActiveTxECFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveTxECFrames.setStatus(_A)
_CctmActiveRxECNAKs_Type=Counter32
_CctmActiveRxECNAKs_Object=MibTableColumn
cctmActiveRxECNAKs=_CctmActiveRxECNAKs_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,28),_CctmActiveRxECNAKs_Type())
cctmActiveRxECNAKs.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveRxECNAKs.setStatus(_A)
_CctmActiveTxECNAKs_Type=Counter32
_CctmActiveTxECNAKs_Object=MibTableColumn
cctmActiveTxECNAKs=_CctmActiveTxECNAKs_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,29),_CctmActiveTxECNAKs_Type())
cctmActiveTxECNAKs.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveTxECNAKs.setStatus(_A)
_CctmActiveRxECFramesBad_Type=Counter32
_CctmActiveRxECFramesBad_Object=MibTableColumn
cctmActiveRxECFramesBad=_CctmActiveRxECFramesBad_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,30),_CctmActiveRxECFramesBad_Type())
cctmActiveRxECFramesBad.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveRxECFramesBad.setStatus(_A)
_CctmActiveECFramesResent_Type=Counter32
_CctmActiveECFramesResent_Object=MibTableColumn
cctmActiveECFramesResent=_CctmActiveECFramesResent_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,31),_CctmActiveECFramesResent_Type())
cctmActiveECFramesResent.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveECFramesResent.setStatus(_A)
_CctmActiveECLinkTimeouts_Type=Counter32
_CctmActiveECLinkTimeouts_Object=MibTableColumn
cctmActiveECLinkTimeouts=_CctmActiveECLinkTimeouts_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,32),_CctmActiveECLinkTimeouts_Type())
cctmActiveECLinkTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveECLinkTimeouts.setStatus(_A)
_CctmActiveRxCharLost_Type=Counter32
_CctmActiveRxCharLost_Object=MibTableColumn
cctmActiveRxCharLost=_CctmActiveRxCharLost_Object((1,3,6,1,4,1,9,9,165,1,1,1,1,33),_CctmActiveRxCharLost_Type())
cctmActiveRxCharLost.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmActiveRxCharLost.setStatus(_A)
_CctmHistory_ObjectIdentity=ObjectIdentity
cctmHistory=_CctmHistory_ObjectIdentity((1,3,6,1,4,1,9,9,165,1,2))
_CctmHistoryTable_Object=MibTable
cctmHistoryTable=_CctmHistoryTable_Object((1,3,6,1,4,1,9,9,165,1,2,1))
if mibBuilder.loadTexts:cctmHistoryTable.setStatus(_A)
_CctmHistoryEntry_Object=MibTableRow
cctmHistoryEntry=_CctmHistoryEntry_Object((1,3,6,1,4,1,9,9,165,1,2,1,1))
cctmHistoryEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:cctmHistoryEntry.setStatus(_A)
_CctmHistoryProjectedMaxRxRate_Type=Unsigned32
_CctmHistoryProjectedMaxRxRate_Object=MibTableColumn
cctmHistoryProjectedMaxRxRate=_CctmHistoryProjectedMaxRxRate_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,1),_CctmHistoryProjectedMaxRxRate_Type())
cctmHistoryProjectedMaxRxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryProjectedMaxRxRate.setStatus(_A)
if mibBuilder.loadTexts:cctmHistoryProjectedMaxRxRate.setUnits(_D)
_CctmHistoryProjectedMaxTxRate_Type=Unsigned32
_CctmHistoryProjectedMaxTxRate_Object=MibTableColumn
cctmHistoryProjectedMaxTxRate=_CctmHistoryProjectedMaxTxRate_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,2),_CctmHistoryProjectedMaxTxRate_Type())
cctmHistoryProjectedMaxTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryProjectedMaxTxRate.setStatus(_A)
if mibBuilder.loadTexts:cctmHistoryProjectedMaxTxRate.setUnits(_D)
_CctmHistoryFinalRxRate_Type=Unsigned32
_CctmHistoryFinalRxRate_Object=MibTableColumn
cctmHistoryFinalRxRate=_CctmHistoryFinalRxRate_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,3),_CctmHistoryFinalRxRate_Type())
cctmHistoryFinalRxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryFinalRxRate.setStatus(_A)
if mibBuilder.loadTexts:cctmHistoryFinalRxRate.setUnits(_D)
_CctmHistoryFinalTxRate_Type=Unsigned32
_CctmHistoryFinalTxRate_Object=MibTableColumn
cctmHistoryFinalTxRate=_CctmHistoryFinalTxRate_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,4),_CctmHistoryFinalTxRate_Type())
cctmHistoryFinalTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryFinalTxRate.setStatus(_A)
if mibBuilder.loadTexts:cctmHistoryFinalTxRate.setUnits(_D)
_CctmHistoryAttemptedModulation_Type=CctmModulation
_CctmHistoryAttemptedModulation_Object=MibTableColumn
cctmHistoryAttemptedModulation=_CctmHistoryAttemptedModulation_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,5),_CctmHistoryAttemptedModulation_Type())
cctmHistoryAttemptedModulation.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryAttemptedModulation.setStatus(_A)
_CctmHistoryInitialModulation_Type=CctmModulation
_CctmHistoryInitialModulation_Object=MibTableColumn
cctmHistoryInitialModulation=_CctmHistoryInitialModulation_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,6),_CctmHistoryInitialModulation_Type())
cctmHistoryInitialModulation.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryInitialModulation.setStatus(_A)
_CctmHistoryFinalModulation_Type=CctmModulation
_CctmHistoryFinalModulation_Object=MibTableColumn
cctmHistoryFinalModulation=_CctmHistoryFinalModulation_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,7),_CctmHistoryFinalModulation_Type())
cctmHistoryFinalModulation.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryFinalModulation.setStatus(_A)
_CctmHistoryAttemptedECProtocol_Type=CctmECProtocol
_CctmHistoryAttemptedECProtocol_Object=MibTableColumn
cctmHistoryAttemptedECProtocol=_CctmHistoryAttemptedECProtocol_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,8),_CctmHistoryAttemptedECProtocol_Type())
cctmHistoryAttemptedECProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryAttemptedECProtocol.setStatus(_A)
_CctmHistoryECProtocol_Type=CctmECProtocol
_CctmHistoryECProtocol_Object=MibTableColumn
cctmHistoryECProtocol=_CctmHistoryECProtocol_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,9),_CctmHistoryECProtocol_Type())
cctmHistoryECProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryECProtocol.setStatus(_A)
class _CctmHistorySupportedDC_Type(Bits):namedValues=NamedValues(*((_J,0),(_I,1),(_H,2),(_L,3),(_K,4)))
_CctmHistorySupportedDC_Type.__name__=_G
_CctmHistorySupportedDC_Object=MibTableColumn
cctmHistorySupportedDC=_CctmHistorySupportedDC_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,10),_CctmHistorySupportedDC_Type())
cctmHistorySupportedDC.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistorySupportedDC.setStatus(_A)
_CctmHistoryDataCompression_Type=CctmDataCompression
_CctmHistoryDataCompression_Object=MibTableColumn
cctmHistoryDataCompression=_CctmHistoryDataCompression_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,11),_CctmHistoryDataCompression_Type())
cctmHistoryDataCompression.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryDataCompression.setStatus(_A)
_CctmHistoryRxHighWatermark_Type=Gauge32
_CctmHistoryRxHighWatermark_Object=MibTableColumn
cctmHistoryRxHighWatermark=_CctmHistoryRxHighWatermark_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,12),_CctmHistoryRxHighWatermark_Type())
cctmHistoryRxHighWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryRxHighWatermark.setStatus(_A)
if mibBuilder.loadTexts:cctmHistoryRxHighWatermark.setUnits(_D)
_CctmHistoryRxLowWatermark_Type=Gauge32
_CctmHistoryRxLowWatermark_Object=MibTableColumn
cctmHistoryRxLowWatermark=_CctmHistoryRxLowWatermark_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,13),_CctmHistoryRxLowWatermark_Type())
cctmHistoryRxLowWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryRxLowWatermark.setStatus(_A)
if mibBuilder.loadTexts:cctmHistoryRxLowWatermark.setUnits(_D)
_CctmHistoryTxHighWatermark_Type=Gauge32
_CctmHistoryTxHighWatermark_Object=MibTableColumn
cctmHistoryTxHighWatermark=_CctmHistoryTxHighWatermark_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,14),_CctmHistoryTxHighWatermark_Type())
cctmHistoryTxHighWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryTxHighWatermark.setStatus(_A)
if mibBuilder.loadTexts:cctmHistoryTxHighWatermark.setUnits(_D)
_CctmHistoryTxLowWatermark_Type=Gauge32
_CctmHistoryTxLowWatermark_Object=MibTableColumn
cctmHistoryTxLowWatermark=_CctmHistoryTxLowWatermark_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,15),_CctmHistoryTxLowWatermark_Type())
cctmHistoryTxLowWatermark.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryTxLowWatermark.setStatus(_A)
if mibBuilder.loadTexts:cctmHistoryTxLowWatermark.setUnits(_D)
_CctmHistoryLocalUpRateShifts_Type=Counter32
_CctmHistoryLocalUpRateShifts_Object=MibTableColumn
cctmHistoryLocalUpRateShifts=_CctmHistoryLocalUpRateShifts_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,16),_CctmHistoryLocalUpRateShifts_Type())
cctmHistoryLocalUpRateShifts.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryLocalUpRateShifts.setStatus(_A)
_CctmHistoryLocalDownRateShifts_Type=Counter32
_CctmHistoryLocalDownRateShifts_Object=MibTableColumn
cctmHistoryLocalDownRateShifts=_CctmHistoryLocalDownRateShifts_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,17),_CctmHistoryLocalDownRateShifts_Type())
cctmHistoryLocalDownRateShifts.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryLocalDownRateShifts.setStatus(_A)
_CctmHistoryRemoteUpRateShifts_Type=Counter32
_CctmHistoryRemoteUpRateShifts_Object=MibTableColumn
cctmHistoryRemoteUpRateShifts=_CctmHistoryRemoteUpRateShifts_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,18),_CctmHistoryRemoteUpRateShifts_Type())
cctmHistoryRemoteUpRateShifts.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryRemoteUpRateShifts.setStatus(_A)
_CctmHistoryRemoteDownRateShifts_Type=Counter32
_CctmHistoryRemoteDownRateShifts_Object=MibTableColumn
cctmHistoryRemoteDownRateShifts=_CctmHistoryRemoteDownRateShifts_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,19),_CctmHistoryRemoteDownRateShifts_Type())
cctmHistoryRemoteDownRateShifts.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryRemoteDownRateShifts.setStatus(_A)
_CctmHistoryRateShiftFailures_Type=Counter32
_CctmHistoryRateShiftFailures_Object=MibTableColumn
cctmHistoryRateShiftFailures=_CctmHistoryRateShiftFailures_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,20),_CctmHistoryRateShiftFailures_Type())
cctmHistoryRateShiftFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryRateShiftFailures.setStatus(_A)
_CctmHistoryLocalRetrains_Type=Counter32
_CctmHistoryLocalRetrains_Object=MibTableColumn
cctmHistoryLocalRetrains=_CctmHistoryLocalRetrains_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,21),_CctmHistoryLocalRetrains_Type())
cctmHistoryLocalRetrains.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryLocalRetrains.setStatus(_A)
_CctmHistoryRemoteRetrains_Type=Counter32
_CctmHistoryRemoteRetrains_Object=MibTableColumn
cctmHistoryRemoteRetrains=_CctmHistoryRemoteRetrains_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,22),_CctmHistoryRemoteRetrains_Type())
cctmHistoryRemoteRetrains.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryRemoteRetrains.setStatus(_A)
_CctmHistoryRetrainFailures_Type=Counter32
_CctmHistoryRetrainFailures_Object=MibTableColumn
cctmHistoryRetrainFailures=_CctmHistoryRetrainFailures_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,23),_CctmHistoryRetrainFailures_Type())
cctmHistoryRetrainFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryRetrainFailures.setStatus(_A)
_CctmHistoryRxLinkOctets_Type=Counter32
_CctmHistoryRxLinkOctets_Object=MibTableColumn
cctmHistoryRxLinkOctets=_CctmHistoryRxLinkOctets_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,24),_CctmHistoryRxLinkOctets_Type())
cctmHistoryRxLinkOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryRxLinkOctets.setStatus(_A)
_CctmHistoryTxLinkOctets_Type=Counter32
_CctmHistoryTxLinkOctets_Object=MibTableColumn
cctmHistoryTxLinkOctets=_CctmHistoryTxLinkOctets_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,25),_CctmHistoryTxLinkOctets_Type())
cctmHistoryTxLinkOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryTxLinkOctets.setStatus(_A)
_CctmHistoryRxECFrames_Type=Counter32
_CctmHistoryRxECFrames_Object=MibTableColumn
cctmHistoryRxECFrames=_CctmHistoryRxECFrames_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,26),_CctmHistoryRxECFrames_Type())
cctmHistoryRxECFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryRxECFrames.setStatus(_A)
_CctmHistoryTxECFrames_Type=Counter32
_CctmHistoryTxECFrames_Object=MibTableColumn
cctmHistoryTxECFrames=_CctmHistoryTxECFrames_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,27),_CctmHistoryTxECFrames_Type())
cctmHistoryTxECFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryTxECFrames.setStatus(_A)
_CctmHistoryRxECNAKs_Type=Counter32
_CctmHistoryRxECNAKs_Object=MibTableColumn
cctmHistoryRxECNAKs=_CctmHistoryRxECNAKs_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,28),_CctmHistoryRxECNAKs_Type())
cctmHistoryRxECNAKs.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryRxECNAKs.setStatus(_A)
_CctmHistoryTxECNAKs_Type=Counter32
_CctmHistoryTxECNAKs_Object=MibTableColumn
cctmHistoryTxECNAKs=_CctmHistoryTxECNAKs_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,29),_CctmHistoryTxECNAKs_Type())
cctmHistoryTxECNAKs.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryTxECNAKs.setStatus(_A)
_CctmHistoryRxECFramesBad_Type=Counter32
_CctmHistoryRxECFramesBad_Object=MibTableColumn
cctmHistoryRxECFramesBad=_CctmHistoryRxECFramesBad_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,30),_CctmHistoryRxECFramesBad_Type())
cctmHistoryRxECFramesBad.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryRxECFramesBad.setStatus(_A)
_CctmHistoryECFramesResent_Type=Counter32
_CctmHistoryECFramesResent_Object=MibTableColumn
cctmHistoryECFramesResent=_CctmHistoryECFramesResent_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,31),_CctmHistoryECFramesResent_Type())
cctmHistoryECFramesResent.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryECFramesResent.setStatus(_A)
_CctmHistoryECLinkTimeouts_Type=Counter32
_CctmHistoryECLinkTimeouts_Object=MibTableColumn
cctmHistoryECLinkTimeouts=_CctmHistoryECLinkTimeouts_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,32),_CctmHistoryECLinkTimeouts_Type())
cctmHistoryECLinkTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryECLinkTimeouts.setStatus(_A)
_CctmHistoryRxCharLost_Type=Counter32
_CctmHistoryRxCharLost_Object=MibTableColumn
cctmHistoryRxCharLost=_CctmHistoryRxCharLost_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,33),_CctmHistoryRxCharLost_Type())
cctmHistoryRxCharLost.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryRxCharLost.setStatus(_A)
_CctmHistoryDisconnectReason_Type=Unsigned32
_CctmHistoryDisconnectReason_Object=MibTableColumn
cctmHistoryDisconnectReason=_CctmHistoryDisconnectReason_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,34),_CctmHistoryDisconnectReason_Type())
cctmHistoryDisconnectReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryDisconnectReason.setStatus(_A)
class _CctmHistoryDisconnectReasonText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CctmHistoryDisconnectReasonText_Type.__name__=_P
_CctmHistoryDisconnectReasonText_Object=MibTableColumn
cctmHistoryDisconnectReasonText=_CctmHistoryDisconnectReasonText_Object((1,3,6,1,4,1,9,9,165,1,2,1,1,35),_CctmHistoryDisconnectReasonText_Type())
cctmHistoryDisconnectReasonText.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmHistoryDisconnectReasonText.setStatus(_A)
_CctmXHistoryTable_Object=MibTable
cctmXHistoryTable=_CctmXHistoryTable_Object((1,3,6,1,4,1,9,9,165,1,2,2))
if mibBuilder.loadTexts:cctmXHistoryTable.setStatus(_A)
_CctmXHistoryEntry_Object=MibTableRow
cctmXHistoryEntry=_CctmXHistoryEntry_Object((1,3,6,1,4,1,9,9,165,1,2,2,1))
if mibBuilder.loadTexts:cctmXHistoryEntry.setStatus(_A)
_CctmXHistoryRxECInfoFrameSize_Type=Unsigned32
_CctmXHistoryRxECInfoFrameSize_Object=MibTableColumn
cctmXHistoryRxECInfoFrameSize=_CctmXHistoryRxECInfoFrameSize_Object((1,3,6,1,4,1,9,9,165,1,2,2,1,1),_CctmXHistoryRxECInfoFrameSize_Type())
cctmXHistoryRxECInfoFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmXHistoryRxECInfoFrameSize.setStatus(_A)
if mibBuilder.loadTexts:cctmXHistoryRxECInfoFrameSize.setUnits(_Q)
_CctmXHistoryTxECInfoFrameSize_Type=Unsigned32
_CctmXHistoryTxECInfoFrameSize_Object=MibTableColumn
cctmXHistoryTxECInfoFrameSize=_CctmXHistoryTxECInfoFrameSize_Object((1,3,6,1,4,1,9,9,165,1,2,2,1,2),_CctmXHistoryTxECInfoFrameSize_Type())
cctmXHistoryTxECInfoFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmXHistoryTxECInfoFrameSize.setStatus(_A)
if mibBuilder.loadTexts:cctmXHistoryTxECInfoFrameSize.setUnits(_Q)
_CctmXHistoryRxECWindowSize_Type=Unsigned32
_CctmXHistoryRxECWindowSize_Object=MibTableColumn
cctmXHistoryRxECWindowSize=_CctmXHistoryRxECWindowSize_Object((1,3,6,1,4,1,9,9,165,1,2,2,1,3),_CctmXHistoryRxECWindowSize_Type())
cctmXHistoryRxECWindowSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmXHistoryRxECWindowSize.setStatus(_A)
if mibBuilder.loadTexts:cctmXHistoryRxECWindowSize.setUnits(_R)
_CctmXHistoryTxECWindowSize_Type=Unsigned32
_CctmXHistoryTxECWindowSize_Object=MibTableColumn
cctmXHistoryTxECWindowSize=_CctmXHistoryTxECWindowSize_Object((1,3,6,1,4,1,9,9,165,1,2,2,1,4),_CctmXHistoryTxECWindowSize_Type())
cctmXHistoryTxECWindowSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmXHistoryTxECWindowSize.setStatus(_A)
if mibBuilder.loadTexts:cctmXHistoryTxECWindowSize.setUnits(_R)
class _CctmXHistoryRxLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,0))
_CctmXHistoryRxLevel_Type.__name__=_E
_CctmXHistoryRxLevel_Object=MibTableColumn
cctmXHistoryRxLevel=_CctmXHistoryRxLevel_Object((1,3,6,1,4,1,9,9,165,1,2,2,1,5),_CctmXHistoryRxLevel_Type())
cctmXHistoryRxLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmXHistoryRxLevel.setStatus(_A)
if mibBuilder.loadTexts:cctmXHistoryRxLevel.setUnits('dB')
class _CctmXHistoryTxLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,0))
_CctmXHistoryTxLevel_Type.__name__=_E
_CctmXHistoryTxLevel_Object=MibTableColumn
cctmXHistoryTxLevel=_CctmXHistoryTxLevel_Object((1,3,6,1,4,1,9,9,165,1,2,2,1,6),_CctmXHistoryTxLevel_Type())
cctmXHistoryTxLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmXHistoryTxLevel.setStatus(_A)
if mibBuilder.loadTexts:cctmXHistoryTxLevel.setUnits('dB')
class _CctmXHistoryConstellation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('points4',1),('points16',2)))
_CctmXHistoryConstellation_Type.__name__=_E
_CctmXHistoryConstellation_Object=MibTableColumn
cctmXHistoryConstellation=_CctmXHistoryConstellation_Object((1,3,6,1,4,1,9,9,165,1,2,2,1,7),_CctmXHistoryConstellation_Type())
cctmXHistoryConstellation.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmXHistoryConstellation.setStatus(_A)
class _CctmXHistoryV90Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notAttempted',1),('failure',2),('success',3)))
_CctmXHistoryV90Status_Type.__name__=_E
_CctmXHistoryV90Status_Object=MibTableColumn
cctmXHistoryV90Status=_CctmXHistoryV90Status_Object((1,3,6,1,4,1,9,9,165,1,2,2,1,8),_CctmXHistoryV90Status_Type())
cctmXHistoryV90Status.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmXHistoryV90Status.setStatus(_A)
class _CctmXHistoryV90Failure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noFailure',1),('clientNonPCM',2),('clientFallback',3),('serverV90Disabled',4)))
_CctmXHistoryV90Failure_Type.__name__=_E
_CctmXHistoryV90Failure_Object=MibTableColumn
cctmXHistoryV90Failure=_CctmXHistoryV90Failure_Object((1,3,6,1,4,1,9,9,165,1,2,2,1,9),_CctmXHistoryV90Failure_Type())
cctmXHistoryV90Failure.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmXHistoryV90Failure.setStatus(_A)
class _CctmXHistoryV90ClientId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CctmXHistoryV90ClientId_Type.__name__=_O
_CctmXHistoryV90ClientId_Object=MibTableColumn
cctmXHistoryV90ClientId=_CctmXHistoryV90ClientId_Object((1,3,6,1,4,1,9,9,165,1,2,2,1,10),_CctmXHistoryV90ClientId_Type())
cctmXHistoryV90ClientId.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmXHistoryV90ClientId.setStatus(_A)
_CctmXHistoryECWindowClosures_Type=Counter32
_CctmXHistoryECWindowClosures_Object=MibTableColumn
cctmXHistoryECWindowClosures=_CctmXHistoryECWindowClosures_Object((1,3,6,1,4,1,9,9,165,1,2,2,1,11),_CctmXHistoryECWindowClosures_Type())
cctmXHistoryECWindowClosures.setMaxAccess(_C)
if mibBuilder.loadTexts:cctmXHistoryECWindowClosures.setStatus(_A)
_CctmMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
cctmMIBNotificationPrefix=_CctmMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,165,2))
_CctmMIBNotifications_ObjectIdentity=ObjectIdentity
cctmMIBNotifications=_CctmMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,165,2,0))
_CctmMIBConformance_ObjectIdentity=ObjectIdentity
cctmMIBConformance=_CctmMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,165,3))
_CctmMIBCompliances_ObjectIdentity=ObjectIdentity
cctmMIBCompliances=_CctmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,165,3,1))
_CctmMIBGroups_ObjectIdentity=ObjectIdentity
cctmMIBGroups=_CctmMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,165,3,2))
cctmHistoryEntry.registerAugmentions((_B,_S))
cctmXHistoryEntry.setIndexNames(*cctmHistoryEntry.getIndexNames())
cctmActiveGroup=ObjectGroup((1,3,6,1,4,1,9,9,165,3,2,2))
cctmActiveGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:cctmActiveGroup.setStatus(_A)
cctmHistoryGroup=ObjectGroup((1,3,6,1,4,1,9,9,165,3,2,3))
cctmHistoryGroup.setObjects(*((_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY)))
if mibBuilder.loadTexts:cctmHistoryGroup.setStatus(_A)
cctmXHistoryGroup=ObjectGroup((1,3,6,1,4,1,9,9,165,3,2,4))
cctmXHistoryGroup.setObjects(*((_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj)))
if mibBuilder.loadTexts:cctmXHistoryGroup.setStatus(_A)
cctmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,165,3,1,1))
cctmMIBCompliance.setObjects(*((_B,_Ak),(_B,_Al),(_B,_Am)))
if mibBuilder.loadTexts:cctmMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CctmModulation':CctmModulation,'CctmECProtocol':CctmECProtocol,'CctmDataCompression':CctmDataCompression,'ciscoCallTrackerModemMIB':ciscoCallTrackerModemMIB,'cctmMIBObjects':cctmMIBObjects,'cctmActive':cctmActive,'cctmActiveTable':cctmActiveTable,'cctmActiveEntry':cctmActiveEntry,_T:cctmActiveProjectedMaxRxRate,_U:cctmActiveProjectedMaxTxRate,_V:cctmActiveRxRate,_W:cctmActiveTxRate,_X:cctmActiveAttemptedModulation,_Y:cctmActiveInitialModulation,_Z:cctmActiveModulation,_a:cctmActiveAttemptedECProtocol,_b:cctmActiveECProtocol,_c:cctmActiveSupportedDC,_d:cctmActiveDataCompression,_e:cctmActiveRxHighWatermark,_f:cctmActiveRxLowWatermark,_g:cctmActiveTxHighWatermark,_h:cctmActiveTxLowWatermark,_i:cctmActiveLocalUpRateShifts,_k:cctmActiveLocalDownRateShifts,_j:cctmActiveRemoteUpRateShifts,_l:cctmActiveRemoteDownRateShifts,_m:cctmActiveRateShiftFailures,_n:cctmActiveLocalRetrains,_o:cctmActiveRemoteRetrains,_p:cctmActiveRetrainFailures,_q:cctmActiveRxLinkOctets,_r:cctmActiveTxLinkOctets,_s:cctmActiveRxECFrames,_t:cctmActiveTxECFrames,_u:cctmActiveRxECNAKs,_v:cctmActiveTxECNAKs,_w:cctmActiveRxECFramesBad,_x:cctmActiveECFramesResent,_y:cctmActiveECLinkTimeouts,_z:cctmActiveRxCharLost,'cctmHistory':cctmHistory,'cctmHistoryTable':cctmHistoryTable,'cctmHistoryEntry':cctmHistoryEntry,_A0:cctmHistoryProjectedMaxRxRate,_A1:cctmHistoryProjectedMaxTxRate,_A2:cctmHistoryFinalRxRate,_A3:cctmHistoryFinalTxRate,_A4:cctmHistoryAttemptedModulation,_A5:cctmHistoryInitialModulation,_A6:cctmHistoryFinalModulation,_A7:cctmHistoryAttemptedECProtocol,_A8:cctmHistoryECProtocol,_A9:cctmHistorySupportedDC,_AA:cctmHistoryDataCompression,_AB:cctmHistoryRxHighWatermark,_AC:cctmHistoryRxLowWatermark,_AD:cctmHistoryTxHighWatermark,_AE:cctmHistoryTxLowWatermark,_AF:cctmHistoryLocalUpRateShifts,_AH:cctmHistoryLocalDownRateShifts,_AG:cctmHistoryRemoteUpRateShifts,_AI:cctmHistoryRemoteDownRateShifts,_AJ:cctmHistoryRateShiftFailures,_AK:cctmHistoryLocalRetrains,_AL:cctmHistoryRemoteRetrains,_AM:cctmHistoryRetrainFailures,_AN:cctmHistoryRxLinkOctets,_AO:cctmHistoryTxLinkOctets,_AP:cctmHistoryRxECFrames,_AQ:cctmHistoryTxECFrames,_AR:cctmHistoryRxECNAKs,_AS:cctmHistoryTxECNAKs,_AT:cctmHistoryRxECFramesBad,_AU:cctmHistoryECFramesResent,_AV:cctmHistoryECLinkTimeouts,_AW:cctmHistoryRxCharLost,_AX:cctmHistoryDisconnectReason,_AY:cctmHistoryDisconnectReasonText,'cctmXHistoryTable':cctmXHistoryTable,_S:cctmXHistoryEntry,_AZ:cctmXHistoryRxECInfoFrameSize,_Aa:cctmXHistoryTxECInfoFrameSize,_Ab:cctmXHistoryRxECWindowSize,_Ac:cctmXHistoryTxECWindowSize,_Ad:cctmXHistoryRxLevel,_Ae:cctmXHistoryTxLevel,_Af:cctmXHistoryConstellation,_Ag:cctmXHistoryV90Status,_Ah:cctmXHistoryV90Failure,_Ai:cctmXHistoryV90ClientId,_Aj:cctmXHistoryECWindowClosures,'cctmMIBNotificationPrefix':cctmMIBNotificationPrefix,'cctmMIBNotifications':cctmMIBNotifications,'cctmMIBConformance':cctmMIBConformance,'cctmMIBCompliances':cctmMIBCompliances,'cctmMIBCompliance':cctmMIBCompliance,'cctmMIBGroups':cctmMIBGroups,_Ak:cctmActiveGroup,_Al:cctmHistoryGroup,_Am:cctmXHistoryGroup})