_F='ligoAthPeerIndex'
_E='LIGO-ATHDRV-STATS-MIB'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ligoMgmt,=mibBuilder.importSymbols('LIGOWAVE-MIB','ligoMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
ligoAthDrvStatsMIB=ModuleIdentity((1,3,6,1,4,1,32750,3,7))
if mibBuilder.loadTexts:ligoAthDrvStatsMIB.setRevisions(('2008-12-12 00:00',))
_LigoAthDrvStatsMIBObjects_ObjectIdentity=ObjectIdentity
ligoAthDrvStatsMIBObjects=_LigoAthDrvStatsMIBObjects_ObjectIdentity((1,3,6,1,4,1,32750,3,7,1))
_LigoAthStatsTable_Object=MibTable
ligoAthStatsTable=_LigoAthStatsTable_Object((1,3,6,1,4,1,32750,3,7,1,1))
if mibBuilder.loadTexts:ligoAthStatsTable.setStatus(_A)
_LigoAthStatsEntry_Object=MibTableRow
ligoAthStatsEntry=_LigoAthStatsEntry_Object((1,3,6,1,4,1,32750,3,7,1,1,1))
ligoAthStatsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ligoAthStatsEntry.setStatus(_A)
_LigoAthWatchdogTimeouts_Type=Counter32
_LigoAthWatchdogTimeouts_Object=MibTableColumn
ligoAthWatchdogTimeouts=_LigoAthWatchdogTimeouts_Object((1,3,6,1,4,1,32750,3,7,1,1,1,1),_LigoAthWatchdogTimeouts_Type())
ligoAthWatchdogTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthWatchdogTimeouts.setStatus(_A)
_LigoAthHardwareErrorInterrupts_Type=Counter32
_LigoAthHardwareErrorInterrupts_Object=MibTableColumn
ligoAthHardwareErrorInterrupts=_LigoAthHardwareErrorInterrupts_Object((1,3,6,1,4,1,32750,3,7,1,1,1,2),_LigoAthHardwareErrorInterrupts_Type())
ligoAthHardwareErrorInterrupts.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthHardwareErrorInterrupts.setStatus(_A)
_LigoAthBeaconMissInterrupts_Type=Counter32
_LigoAthBeaconMissInterrupts_Object=MibTableColumn
ligoAthBeaconMissInterrupts=_LigoAthBeaconMissInterrupts_Object((1,3,6,1,4,1,32750,3,7,1,1,1,3),_LigoAthBeaconMissInterrupts_Type())
ligoAthBeaconMissInterrupts.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthBeaconMissInterrupts.setStatus(_A)
_LigoAthRecvOverrunInterrupts_Type=Counter32
_LigoAthRecvOverrunInterrupts_Object=MibTableColumn
ligoAthRecvOverrunInterrupts=_LigoAthRecvOverrunInterrupts_Object((1,3,6,1,4,1,32750,3,7,1,1,1,4),_LigoAthRecvOverrunInterrupts_Type())
ligoAthRecvOverrunInterrupts.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthRecvOverrunInterrupts.setStatus(_A)
_LigoAthRecvEolInterrupts_Type=Counter32
_LigoAthRecvEolInterrupts_Object=MibTableColumn
ligoAthRecvEolInterrupts=_LigoAthRecvEolInterrupts_Object((1,3,6,1,4,1,32750,3,7,1,1,1,5),_LigoAthRecvEolInterrupts_Type())
ligoAthRecvEolInterrupts.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthRecvEolInterrupts.setStatus(_A)
_LigoAthTxmitUnderrunInterrupts_Type=Counter32
_LigoAthTxmitUnderrunInterrupts_Object=MibTableColumn
ligoAthTxmitUnderrunInterrupts=_LigoAthTxmitUnderrunInterrupts_Object((1,3,6,1,4,1,32750,3,7,1,1,1,6),_LigoAthTxmitUnderrunInterrupts_Type())
ligoAthTxmitUnderrunInterrupts.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxmitUnderrunInterrupts.setStatus(_A)
_LigoAthTxManagementFrames_Type=Counter32
_LigoAthTxManagementFrames_Object=MibTableColumn
ligoAthTxManagementFrames=_LigoAthTxManagementFrames_Object((1,3,6,1,4,1,32750,3,7,1,1,1,7),_LigoAthTxManagementFrames_Type())
ligoAthTxManagementFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxManagementFrames.setStatus(_A)
_LigoAthTxFramesDiscQueueDepth_Type=Counter32
_LigoAthTxFramesDiscQueueDepth_Object=MibTableColumn
ligoAthTxFramesDiscQueueDepth=_LigoAthTxFramesDiscQueueDepth_Object((1,3,6,1,4,1,32750,3,7,1,1,1,8),_LigoAthTxFramesDiscQueueDepth_Type())
ligoAthTxFramesDiscQueueDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxFramesDiscQueueDepth.setStatus(_A)
_LigoAthTxFramesDiscDeviceGone_Type=Counter32
_LigoAthTxFramesDiscDeviceGone_Object=MibTableColumn
ligoAthTxFramesDiscDeviceGone=_LigoAthTxFramesDiscDeviceGone_Object((1,3,6,1,4,1,32750,3,7,1,1,1,9),_LigoAthTxFramesDiscDeviceGone_Type())
ligoAthTxFramesDiscDeviceGone.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxFramesDiscDeviceGone.setStatus(_A)
_LigoAthTxQueueFull_Type=Counter32
_LigoAthTxQueueFull_Object=MibTableColumn
ligoAthTxQueueFull=_LigoAthTxQueueFull_Object((1,3,6,1,4,1,32750,3,7,1,1,1,10),_LigoAthTxQueueFull_Type())
ligoAthTxQueueFull.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxQueueFull.setStatus(_A)
_LigoAthTxEncapsulationFailed_Type=Counter32
_LigoAthTxEncapsulationFailed_Object=MibTableColumn
ligoAthTxEncapsulationFailed=_LigoAthTxEncapsulationFailed_Object((1,3,6,1,4,1,32750,3,7,1,1,1,11),_LigoAthTxEncapsulationFailed_Type())
ligoAthTxEncapsulationFailed.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxEncapsulationFailed.setStatus(_A)
_LigoAthTxFailedNoNode_Type=Counter32
_LigoAthTxFailedNoNode_Object=MibTableColumn
ligoAthTxFailedNoNode=_LigoAthTxFailedNoNode_Object((1,3,6,1,4,1,32750,3,7,1,1,1,12),_LigoAthTxFailedNoNode_Type())
ligoAthTxFailedNoNode.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxFailedNoNode.setStatus(_A)
_LigoAthTxFailedNoDataTxBuffer_Type=Counter32
_LigoAthTxFailedNoDataTxBuffer_Object=MibTableColumn
ligoAthTxFailedNoDataTxBuffer=_LigoAthTxFailedNoDataTxBuffer_Object((1,3,6,1,4,1,32750,3,7,1,1,1,13),_LigoAthTxFailedNoDataTxBuffer_Type())
ligoAthTxFailedNoDataTxBuffer.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxFailedNoDataTxBuffer.setStatus(_A)
_LigoAthTxFailedNoMgtTxBuffer_Type=Counter32
_LigoAthTxFailedNoMgtTxBuffer_Object=MibTableColumn
ligoAthTxFailedNoMgtTxBuffer=_LigoAthTxFailedNoMgtTxBuffer_Object((1,3,6,1,4,1,32750,3,7,1,1,1,14),_LigoAthTxFailedNoMgtTxBuffer_Type())
ligoAthTxFailedNoMgtTxBuffer.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxFailedNoMgtTxBuffer.setStatus(_A)
_LigoAthTxFailedTooManyRetries_Type=Counter32
_LigoAthTxFailedTooManyRetries_Object=MibTableColumn
ligoAthTxFailedTooManyRetries=_LigoAthTxFailedTooManyRetries_Object((1,3,6,1,4,1,32750,3,7,1,1,1,15),_LigoAthTxFailedTooManyRetries_Type())
ligoAthTxFailedTooManyRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxFailedTooManyRetries.setStatus(_A)
_LigoAthTxFailedFifoUnderrun_Type=Counter32
_LigoAthTxFailedFifoUnderrun_Object=MibTableColumn
ligoAthTxFailedFifoUnderrun=_LigoAthTxFailedFifoUnderrun_Object((1,3,6,1,4,1,32750,3,7,1,1,1,16),_LigoAthTxFailedFifoUnderrun_Type())
ligoAthTxFailedFifoUnderrun.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxFailedFifoUnderrun.setStatus(_A)
_LigoAthTxFailedXmitFiltered_Type=Counter32
_LigoAthTxFailedXmitFiltered_Object=MibTableColumn
ligoAthTxFailedXmitFiltered=_LigoAthTxFailedXmitFiltered_Object((1,3,6,1,4,1,32750,3,7,1,1,1,17),_LigoAthTxFailedXmitFiltered_Type())
ligoAthTxFailedXmitFiltered.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxFailedXmitFiltered.setStatus(_A)
_LigoAthShortOnchipTxRetries_Type=Counter32
_LigoAthShortOnchipTxRetries_Object=MibTableColumn
ligoAthShortOnchipTxRetries=_LigoAthShortOnchipTxRetries_Object((1,3,6,1,4,1,32750,3,7,1,1,1,18),_LigoAthShortOnchipTxRetries_Type())
ligoAthShortOnchipTxRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthShortOnchipTxRetries.setStatus(_A)
_LigoAthLongOnchipTxRetries_Type=Counter32
_LigoAthLongOnchipTxRetries_Object=MibTableColumn
ligoAthLongOnchipTxRetries=_LigoAthLongOnchipTxRetries_Object((1,3,6,1,4,1,32750,3,7,1,1,1,19),_LigoAthLongOnchipTxRetries_Type())
ligoAthLongOnchipTxRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthLongOnchipTxRetries.setStatus(_A)
_LigoAthTxFailedBogusXmitRate_Type=Counter32
_LigoAthTxFailedBogusXmitRate_Object=MibTableColumn
ligoAthTxFailedBogusXmitRate=_LigoAthTxFailedBogusXmitRate_Object((1,3,6,1,4,1,32750,3,7,1,1,1,20),_LigoAthTxFailedBogusXmitRate_Type())
ligoAthTxFailedBogusXmitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxFailedBogusXmitRate.setStatus(_A)
_LigoAthTxFramesNoAckMarked_Type=Counter32
_LigoAthTxFramesNoAckMarked_Object=MibTableColumn
ligoAthTxFramesNoAckMarked=_LigoAthTxFramesNoAckMarked_Object((1,3,6,1,4,1,32750,3,7,1,1,1,21),_LigoAthTxFramesNoAckMarked_Type())
ligoAthTxFramesNoAckMarked.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxFramesNoAckMarked.setStatus(_A)
_LigoAthTxFramesRtsEnabled_Type=Counter32
_LigoAthTxFramesRtsEnabled_Object=MibTableColumn
ligoAthTxFramesRtsEnabled=_LigoAthTxFramesRtsEnabled_Object((1,3,6,1,4,1,32750,3,7,1,1,1,22),_LigoAthTxFramesRtsEnabled_Type())
ligoAthTxFramesRtsEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxFramesRtsEnabled.setStatus(_A)
_LigoAthTxFramesCtsEnabled_Type=Counter32
_LigoAthTxFramesCtsEnabled_Object=MibTableColumn
ligoAthTxFramesCtsEnabled=_LigoAthTxFramesCtsEnabled_Object((1,3,6,1,4,1,32750,3,7,1,1,1,23),_LigoAthTxFramesCtsEnabled_Type())
ligoAthTxFramesCtsEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxFramesCtsEnabled.setStatus(_A)
_LigoAthTxFramesShortPreamble_Type=Counter32
_LigoAthTxFramesShortPreamble_Object=MibTableColumn
ligoAthTxFramesShortPreamble=_LigoAthTxFramesShortPreamble_Object((1,3,6,1,4,1,32750,3,7,1,1,1,24),_LigoAthTxFramesShortPreamble_Type())
ligoAthTxFramesShortPreamble.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxFramesShortPreamble.setStatus(_A)
_LigoAthTxFramesAlternateRate_Type=Counter32
_LigoAthTxFramesAlternateRate_Object=MibTableColumn
ligoAthTxFramesAlternateRate=_LigoAthTxFramesAlternateRate_Object((1,3,6,1,4,1,32750,3,7,1,1,1,25),_LigoAthTxFramesAlternateRate_Type())
ligoAthTxFramesAlternateRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxFramesAlternateRate.setStatus(_A)
_LigoAthTxFrames11gProtection_Type=Counter32
_LigoAthTxFrames11gProtection_Object=MibTableColumn
ligoAthTxFrames11gProtection=_LigoAthTxFrames11gProtection_Object((1,3,6,1,4,1,32750,3,7,1,1,1,26),_LigoAthTxFrames11gProtection_Type())
ligoAthTxFrames11gProtection.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxFrames11gProtection.setStatus(_A)
_LigoAthRxFailedDescOverrun_Type=Counter32
_LigoAthRxFailedDescOverrun_Object=MibTableColumn
ligoAthRxFailedDescOverrun=_LigoAthRxFailedDescOverrun_Object((1,3,6,1,4,1,32750,3,7,1,1,1,27),_LigoAthRxFailedDescOverrun_Type())
ligoAthRxFailedDescOverrun.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthRxFailedDescOverrun.setStatus(_A)
_LigoAthRxFailedBadCrc_Type=Counter32
_LigoAthRxFailedBadCrc_Object=MibTableColumn
ligoAthRxFailedBadCrc=_LigoAthRxFailedBadCrc_Object((1,3,6,1,4,1,32750,3,7,1,1,1,28),_LigoAthRxFailedBadCrc_Type())
ligoAthRxFailedBadCrc.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthRxFailedBadCrc.setStatus(_A)
_LigoAthRxFailedFifoOverrun_Type=Counter32
_LigoAthRxFailedFifoOverrun_Object=MibTableColumn
ligoAthRxFailedFifoOverrun=_LigoAthRxFailedFifoOverrun_Object((1,3,6,1,4,1,32750,3,7,1,1,1,29),_LigoAthRxFailedFifoOverrun_Type())
ligoAthRxFailedFifoOverrun.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthRxFailedFifoOverrun.setStatus(_A)
_LigoAthRxFailedDecryptErrors_Type=Counter32
_LigoAthRxFailedDecryptErrors_Object=MibTableColumn
ligoAthRxFailedDecryptErrors=_LigoAthRxFailedDecryptErrors_Object((1,3,6,1,4,1,32750,3,7,1,1,1,30),_LigoAthRxFailedDecryptErrors_Type())
ligoAthRxFailedDecryptErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthRxFailedDecryptErrors.setStatus(_A)
_LigoAthRxFailedMicFailure_Type=Counter32
_LigoAthRxFailedMicFailure_Object=MibTableColumn
ligoAthRxFailedMicFailure=_LigoAthRxFailedMicFailure_Object((1,3,6,1,4,1,32750,3,7,1,1,1,31),_LigoAthRxFailedMicFailure_Type())
ligoAthRxFailedMicFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthRxFailedMicFailure.setStatus(_A)
_LigoAthRxFailedFrameTooShort_Type=Counter32
_LigoAthRxFailedFrameTooShort_Object=MibTableColumn
ligoAthRxFailedFrameTooShort=_LigoAthRxFailedFrameTooShort_Object((1,3,6,1,4,1,32750,3,7,1,1,1,32),_LigoAthRxFailedFrameTooShort_Type())
ligoAthRxFailedFrameTooShort.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthRxFailedFrameTooShort.setStatus(_A)
_LigoAthRxSetupFailedNoSkbuff_Type=Counter32
_LigoAthRxSetupFailedNoSkbuff_Object=MibTableColumn
ligoAthRxSetupFailedNoSkbuff=_LigoAthRxSetupFailedNoSkbuff_Object((1,3,6,1,4,1,32750,3,7,1,1,1,33),_LigoAthRxSetupFailedNoSkbuff_Type())
ligoAthRxSetupFailedNoSkbuff.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthRxSetupFailedNoSkbuff.setStatus(_A)
_LigoAthRxManagementFrames_Type=Counter32
_LigoAthRxManagementFrames_Object=MibTableColumn
ligoAthRxManagementFrames=_LigoAthRxManagementFrames_Object((1,3,6,1,4,1,32750,3,7,1,1,1,34),_LigoAthRxManagementFrames_Type())
ligoAthRxManagementFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthRxManagementFrames.setStatus(_A)
_LigoAthRxControlFrames_Type=Counter32
_LigoAthRxControlFrames_Object=MibTableColumn
ligoAthRxControlFrames=_LigoAthRxControlFrames_Object((1,3,6,1,4,1,32750,3,7,1,1,1,35),_LigoAthRxControlFrames_Type())
ligoAthRxControlFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthRxControlFrames.setStatus(_A)
_LigoAthNoSkbuffForBeacon_Type=Counter32
_LigoAthNoSkbuffForBeacon_Object=MibTableColumn
ligoAthNoSkbuffForBeacon=_LigoAthNoSkbuffForBeacon_Object((1,3,6,1,4,1,32750,3,7,1,1,1,36),_LigoAthNoSkbuffForBeacon_Type())
ligoAthNoSkbuffForBeacon.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthNoSkbuffForBeacon.setStatus(_A)
_LigoAthBeaconsTransmitted_Type=Counter32
_LigoAthBeaconsTransmitted_Object=MibTableColumn
ligoAthBeaconsTransmitted=_LigoAthBeaconsTransmitted_Object((1,3,6,1,4,1,32750,3,7,1,1,1,37),_LigoAthBeaconsTransmitted_Type())
ligoAthBeaconsTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthBeaconsTransmitted.setStatus(_A)
_LigoAthPeriodicCalibrations_Type=Counter32
_LigoAthPeriodicCalibrations_Object=MibTableColumn
ligoAthPeriodicCalibrations=_LigoAthPeriodicCalibrations_Object((1,3,6,1,4,1,32750,3,7,1,1,1,38),_LigoAthPeriodicCalibrations_Type())
ligoAthPeriodicCalibrations.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeriodicCalibrations.setStatus(_A)
_LigoAthPeriodicCalibrFailures_Type=Counter32
_LigoAthPeriodicCalibrFailures_Object=MibTableColumn
ligoAthPeriodicCalibrFailures=_LigoAthPeriodicCalibrFailures_Object((1,3,6,1,4,1,32750,3,7,1,1,1,39),_LigoAthPeriodicCalibrFailures_Type())
ligoAthPeriodicCalibrFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeriodicCalibrFailures.setStatus(_A)
_LigoAthRfgainValueChange_Type=Counter32
_LigoAthRfgainValueChange_Object=MibTableColumn
ligoAthRfgainValueChange=_LigoAthRfgainValueChange_Object((1,3,6,1,4,1,32750,3,7,1,1,1,40),_LigoAthRfgainValueChange_Type())
ligoAthRfgainValueChange.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthRfgainValueChange.setStatus(_A)
_LigoAthRateControlChecks_Type=Counter32
_LigoAthRateControlChecks_Object=MibTableColumn
ligoAthRateControlChecks=_LigoAthRateControlChecks_Object((1,3,6,1,4,1,32750,3,7,1,1,1,41),_LigoAthRateControlChecks_Type())
ligoAthRateControlChecks.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthRateControlChecks.setStatus(_A)
_LigoAthRateCtrlRaisedXmitRate_Type=Counter32
_LigoAthRateCtrlRaisedXmitRate_Object=MibTableColumn
ligoAthRateCtrlRaisedXmitRate=_LigoAthRateCtrlRaisedXmitRate_Object((1,3,6,1,4,1,32750,3,7,1,1,1,42),_LigoAthRateCtrlRaisedXmitRate_Type())
ligoAthRateCtrlRaisedXmitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthRateCtrlRaisedXmitRate.setStatus(_A)
_LigoAthRateCtrlDroppedXmitRate_Type=Counter32
_LigoAthRateCtrlDroppedXmitRate_Object=MibTableColumn
ligoAthRateCtrlDroppedXmitRate=_LigoAthRateCtrlDroppedXmitRate_Object((1,3,6,1,4,1,32750,3,7,1,1,1,43),_LigoAthRateCtrlDroppedXmitRate_Type())
ligoAthRateCtrlDroppedXmitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthRateCtrlDroppedXmitRate.setStatus(_A)
_LigoAthRssiOfLastAck_Type=Gauge32
_LigoAthRssiOfLastAck_Object=MibTableColumn
ligoAthRssiOfLastAck=_LigoAthRssiOfLastAck_Object((1,3,6,1,4,1,32750,3,7,1,1,1,44),_LigoAthRssiOfLastAck_Type())
ligoAthRssiOfLastAck.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthRssiOfLastAck.setStatus(_A)
_LigoAthRssiOfLastRcv_Type=Gauge32
_LigoAthRssiOfLastRcv_Object=MibTableColumn
ligoAthRssiOfLastRcv=_LigoAthRssiOfLastRcv_Object((1,3,6,1,4,1,32750,3,7,1,1,1,45),_LigoAthRssiOfLastRcv_Type())
ligoAthRssiOfLastRcv.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthRssiOfLastRcv.setStatus(_A)
_LigoAthPhyErrorsTable_Object=MibTable
ligoAthPhyErrorsTable=_LigoAthPhyErrorsTable_Object((1,3,6,1,4,1,32750,3,7,1,2))
if mibBuilder.loadTexts:ligoAthPhyErrorsTable.setStatus(_A)
_LigoAthPhyErrorsEntry_Object=MibTableRow
ligoAthPhyErrorsEntry=_LigoAthPhyErrorsEntry_Object((1,3,6,1,4,1,32750,3,7,1,2,1))
ligoAthPhyErrorsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ligoAthPhyErrorsEntry.setStatus(_A)
_LigoAthPhyTransmitUnderrun_Type=Counter32
_LigoAthPhyTransmitUnderrun_Object=MibTableColumn
ligoAthPhyTransmitUnderrun=_LigoAthPhyTransmitUnderrun_Object((1,3,6,1,4,1,32750,3,7,1,2,1,1),_LigoAthPhyTransmitUnderrun_Type())
ligoAthPhyTransmitUnderrun.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPhyTransmitUnderrun.setStatus(_A)
_LigoAthPhyTimingError_Type=Counter32
_LigoAthPhyTimingError_Object=MibTableColumn
ligoAthPhyTimingError=_LigoAthPhyTimingError_Object((1,3,6,1,4,1,32750,3,7,1,2,1,2),_LigoAthPhyTimingError_Type())
ligoAthPhyTimingError.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPhyTimingError.setStatus(_A)
_LigoAthPhyIllegalParity_Type=Counter32
_LigoAthPhyIllegalParity_Object=MibTableColumn
ligoAthPhyIllegalParity=_LigoAthPhyIllegalParity_Object((1,3,6,1,4,1,32750,3,7,1,2,1,3),_LigoAthPhyIllegalParity_Type())
ligoAthPhyIllegalParity.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPhyIllegalParity.setStatus(_A)
_LigoAthPhyIllegalRate_Type=Counter32
_LigoAthPhyIllegalRate_Object=MibTableColumn
ligoAthPhyIllegalRate=_LigoAthPhyIllegalRate_Object((1,3,6,1,4,1,32750,3,7,1,2,1,4),_LigoAthPhyIllegalRate_Type())
ligoAthPhyIllegalRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPhyIllegalRate.setStatus(_A)
_LigoAthPhyIllegalLength_Type=Counter32
_LigoAthPhyIllegalLength_Object=MibTableColumn
ligoAthPhyIllegalLength=_LigoAthPhyIllegalLength_Object((1,3,6,1,4,1,32750,3,7,1,2,1,5),_LigoAthPhyIllegalLength_Type())
ligoAthPhyIllegalLength.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPhyIllegalLength.setStatus(_A)
_LigoAthPhyRadarDetect_Type=Counter32
_LigoAthPhyRadarDetect_Object=MibTableColumn
ligoAthPhyRadarDetect=_LigoAthPhyRadarDetect_Object((1,3,6,1,4,1,32750,3,7,1,2,1,6),_LigoAthPhyRadarDetect_Type())
ligoAthPhyRadarDetect.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPhyRadarDetect.setStatus(_A)
_LigoAthPhyIllegalService_Type=Counter32
_LigoAthPhyIllegalService_Object=MibTableColumn
ligoAthPhyIllegalService=_LigoAthPhyIllegalService_Object((1,3,6,1,4,1,32750,3,7,1,2,1,7),_LigoAthPhyIllegalService_Type())
ligoAthPhyIllegalService.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPhyIllegalService.setStatus(_A)
_LigoAthPhyTxmitOverrideRecv_Type=Counter32
_LigoAthPhyTxmitOverrideRecv_Object=MibTableColumn
ligoAthPhyTxmitOverrideRecv=_LigoAthPhyTxmitOverrideRecv_Object((1,3,6,1,4,1,32750,3,7,1,2,1,8),_LigoAthPhyTxmitOverrideRecv_Type())
ligoAthPhyTxmitOverrideRecv.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPhyTxmitOverrideRecv.setStatus(_A)
_LigoAthPhyOfdmTiming_Type=Counter32
_LigoAthPhyOfdmTiming_Object=MibTableColumn
ligoAthPhyOfdmTiming=_LigoAthPhyOfdmTiming_Object((1,3,6,1,4,1,32750,3,7,1,2,1,9),_LigoAthPhyOfdmTiming_Type())
ligoAthPhyOfdmTiming.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPhyOfdmTiming.setStatus(_A)
_LigoAthPhyOfdmIllegalParity_Type=Counter32
_LigoAthPhyOfdmIllegalParity_Object=MibTableColumn
ligoAthPhyOfdmIllegalParity=_LigoAthPhyOfdmIllegalParity_Object((1,3,6,1,4,1,32750,3,7,1,2,1,10),_LigoAthPhyOfdmIllegalParity_Type())
ligoAthPhyOfdmIllegalParity.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPhyOfdmIllegalParity.setStatus(_A)
_LigoAthPhyOfdmIllegalRate_Type=Counter32
_LigoAthPhyOfdmIllegalRate_Object=MibTableColumn
ligoAthPhyOfdmIllegalRate=_LigoAthPhyOfdmIllegalRate_Object((1,3,6,1,4,1,32750,3,7,1,2,1,11),_LigoAthPhyOfdmIllegalRate_Type())
ligoAthPhyOfdmIllegalRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPhyOfdmIllegalRate.setStatus(_A)
_LigoAthPhyOfdmIllegalLength_Type=Counter32
_LigoAthPhyOfdmIllegalLength_Object=MibTableColumn
ligoAthPhyOfdmIllegalLength=_LigoAthPhyOfdmIllegalLength_Object((1,3,6,1,4,1,32750,3,7,1,2,1,12),_LigoAthPhyOfdmIllegalLength_Type())
ligoAthPhyOfdmIllegalLength.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPhyOfdmIllegalLength.setStatus(_A)
_LigoAthPhyOfdmPowerDrop_Type=Counter32
_LigoAthPhyOfdmPowerDrop_Object=MibTableColumn
ligoAthPhyOfdmPowerDrop=_LigoAthPhyOfdmPowerDrop_Object((1,3,6,1,4,1,32750,3,7,1,2,1,13),_LigoAthPhyOfdmPowerDrop_Type())
ligoAthPhyOfdmPowerDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPhyOfdmPowerDrop.setStatus(_A)
_LigoAthPhyOfdmIllegalService_Type=Counter32
_LigoAthPhyOfdmIllegalService_Object=MibTableColumn
ligoAthPhyOfdmIllegalService=_LigoAthPhyOfdmIllegalService_Object((1,3,6,1,4,1,32750,3,7,1,2,1,14),_LigoAthPhyOfdmIllegalService_Type())
ligoAthPhyOfdmIllegalService.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPhyOfdmIllegalService.setStatus(_A)
_LigoAthPhyOfdmRestart_Type=Counter32
_LigoAthPhyOfdmRestart_Object=MibTableColumn
ligoAthPhyOfdmRestart=_LigoAthPhyOfdmRestart_Object((1,3,6,1,4,1,32750,3,7,1,2,1,15),_LigoAthPhyOfdmRestart_Type())
ligoAthPhyOfdmRestart.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPhyOfdmRestart.setStatus(_A)
_LigoAthPhyCckTiming_Type=Counter32
_LigoAthPhyCckTiming_Object=MibTableColumn
ligoAthPhyCckTiming=_LigoAthPhyCckTiming_Object((1,3,6,1,4,1,32750,3,7,1,2,1,16),_LigoAthPhyCckTiming_Type())
ligoAthPhyCckTiming.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPhyCckTiming.setStatus(_A)
_LigoAthPhyCckHeaderCrc_Type=Counter32
_LigoAthPhyCckHeaderCrc_Object=MibTableColumn
ligoAthPhyCckHeaderCrc=_LigoAthPhyCckHeaderCrc_Object((1,3,6,1,4,1,32750,3,7,1,2,1,17),_LigoAthPhyCckHeaderCrc_Type())
ligoAthPhyCckHeaderCrc.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPhyCckHeaderCrc.setStatus(_A)
_LigoAthPhyCckIllegalRate_Type=Counter32
_LigoAthPhyCckIllegalRate_Object=MibTableColumn
ligoAthPhyCckIllegalRate=_LigoAthPhyCckIllegalRate_Object((1,3,6,1,4,1,32750,3,7,1,2,1,18),_LigoAthPhyCckIllegalRate_Type())
ligoAthPhyCckIllegalRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPhyCckIllegalRate.setStatus(_A)
_LigoAthPhyCckIllegalService_Type=Counter32
_LigoAthPhyCckIllegalService_Object=MibTableColumn
ligoAthPhyCckIllegalService=_LigoAthPhyCckIllegalService_Object((1,3,6,1,4,1,32750,3,7,1,2,1,19),_LigoAthPhyCckIllegalService_Type())
ligoAthPhyCckIllegalService.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPhyCckIllegalService.setStatus(_A)
_LigoAthPhyCckRestart_Type=Counter32
_LigoAthPhyCckRestart_Object=MibTableColumn
ligoAthPhyCckRestart=_LigoAthPhyCckRestart_Object((1,3,6,1,4,1,32750,3,7,1,2,1,20),_LigoAthPhyCckRestart_Type())
ligoAthPhyCckRestart.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPhyCckRestart.setStatus(_A)
_LigoAthAntennaStatsTable_Object=MibTable
ligoAthAntennaStatsTable=_LigoAthAntennaStatsTable_Object((1,3,6,1,4,1,32750,3,7,1,3))
if mibBuilder.loadTexts:ligoAthAntennaStatsTable.setStatus(_A)
_LigoAthAntennaStatsEntry_Object=MibTableRow
ligoAthAntennaStatsEntry=_LigoAthAntennaStatsEntry_Object((1,3,6,1,4,1,32750,3,7,1,3,1))
ligoAthAntennaStatsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ligoAthAntennaStatsEntry.setStatus(_A)
_LigoAthSwitchedDefaultRxAntenna_Type=Counter32
_LigoAthSwitchedDefaultRxAntenna_Object=MibTableColumn
ligoAthSwitchedDefaultRxAntenna=_LigoAthSwitchedDefaultRxAntenna_Object((1,3,6,1,4,1,32750,3,7,1,3,1,1),_LigoAthSwitchedDefaultRxAntenna_Type())
ligoAthSwitchedDefaultRxAntenna.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthSwitchedDefaultRxAntenna.setStatus(_A)
_LigoAthTxUsedAlternateAntenna_Type=Counter32
_LigoAthTxUsedAlternateAntenna_Object=MibTableColumn
ligoAthTxUsedAlternateAntenna=_LigoAthTxUsedAlternateAntenna_Object((1,3,6,1,4,1,32750,3,7,1,3,1,2),_LigoAthTxUsedAlternateAntenna_Type())
ligoAthTxUsedAlternateAntenna.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxUsedAlternateAntenna.setStatus(_A)
_LigoAthTxFramesAntenna1_Type=Counter32
_LigoAthTxFramesAntenna1_Object=MibTableColumn
ligoAthTxFramesAntenna1=_LigoAthTxFramesAntenna1_Object((1,3,6,1,4,1,32750,3,7,1,3,1,3),_LigoAthTxFramesAntenna1_Type())
ligoAthTxFramesAntenna1.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxFramesAntenna1.setStatus(_A)
_LigoAthRxFramesAntenna1_Type=Counter32
_LigoAthRxFramesAntenna1_Object=MibTableColumn
ligoAthRxFramesAntenna1=_LigoAthRxFramesAntenna1_Object((1,3,6,1,4,1,32750,3,7,1,3,1,4),_LigoAthRxFramesAntenna1_Type())
ligoAthRxFramesAntenna1.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthRxFramesAntenna1.setStatus(_A)
_LigoAthTxFramesAntenna2_Type=Counter32
_LigoAthTxFramesAntenna2_Object=MibTableColumn
ligoAthTxFramesAntenna2=_LigoAthTxFramesAntenna2_Object((1,3,6,1,4,1,32750,3,7,1,3,1,5),_LigoAthTxFramesAntenna2_Type())
ligoAthTxFramesAntenna2.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxFramesAntenna2.setStatus(_A)
_LigoAthRxFramesAntenna2_Type=Counter32
_LigoAthRxFramesAntenna2_Object=MibTableColumn
ligoAthRxFramesAntenna2=_LigoAthRxFramesAntenna2_Object((1,3,6,1,4,1,32750,3,7,1,3,1,6),_LigoAthRxFramesAntenna2_Type())
ligoAthRxFramesAntenna2.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthRxFramesAntenna2.setStatus(_A)
_LigoAthTxFramesAntenna3_Type=Counter32
_LigoAthTxFramesAntenna3_Object=MibTableColumn
ligoAthTxFramesAntenna3=_LigoAthTxFramesAntenna3_Object((1,3,6,1,4,1,32750,3,7,1,3,1,7),_LigoAthTxFramesAntenna3_Type())
ligoAthTxFramesAntenna3.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthTxFramesAntenna3.setStatus(_A)
_LigoAthRxFramesAntenna3_Type=Counter32
_LigoAthRxFramesAntenna3_Object=MibTableColumn
ligoAthRxFramesAntenna3=_LigoAthRxFramesAntenna3_Object((1,3,6,1,4,1,32750,3,7,1,3,1,8),_LigoAthRxFramesAntenna3_Type())
ligoAthRxFramesAntenna3.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthRxFramesAntenna3.setStatus(_A)
_LigoAthDot11StatsTable_Object=MibTable
ligoAthDot11StatsTable=_LigoAthDot11StatsTable_Object((1,3,6,1,4,1,32750,3,7,1,4))
if mibBuilder.loadTexts:ligoAthDot11StatsTable.setStatus(_A)
_LigoAthDot11StatsEntry_Object=MibTableRow
ligoAthDot11StatsEntry=_LigoAthDot11StatsEntry_Object((1,3,6,1,4,1,32750,3,7,1,4,1))
ligoAthDot11StatsEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:ligoAthDot11StatsEntry.setStatus(_A)
_LigoAthDot11RxBadVersion_Type=Counter32
_LigoAthDot11RxBadVersion_Object=MibTableColumn
ligoAthDot11RxBadVersion=_LigoAthDot11RxBadVersion_Object((1,3,6,1,4,1,32750,3,7,1,4,1,1),_LigoAthDot11RxBadVersion_Type())
ligoAthDot11RxBadVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxBadVersion.setStatus(_A)
_LigoAthDot11RxTooShort_Type=Counter32
_LigoAthDot11RxTooShort_Object=MibTableColumn
ligoAthDot11RxTooShort=_LigoAthDot11RxTooShort_Object((1,3,6,1,4,1,32750,3,7,1,4,1,2),_LigoAthDot11RxTooShort_Type())
ligoAthDot11RxTooShort.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxTooShort.setStatus(_A)
_LigoAthDot11RxWrongBssid_Type=Counter32
_LigoAthDot11RxWrongBssid_Object=MibTableColumn
ligoAthDot11RxWrongBssid=_LigoAthDot11RxWrongBssid_Object((1,3,6,1,4,1,32750,3,7,1,4,1,3),_LigoAthDot11RxWrongBssid_Type())
ligoAthDot11RxWrongBssid.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxWrongBssid.setStatus(_A)
_LigoAthDot11RxDup_Type=Counter32
_LigoAthDot11RxDup_Object=MibTableColumn
ligoAthDot11RxDup=_LigoAthDot11RxDup_Object((1,3,6,1,4,1,32750,3,7,1,4,1,4),_LigoAthDot11RxDup_Type())
ligoAthDot11RxDup.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxDup.setStatus(_A)
_LigoAthDot11RxWrongDirection_Type=Counter32
_LigoAthDot11RxWrongDirection_Object=MibTableColumn
ligoAthDot11RxWrongDirection=_LigoAthDot11RxWrongDirection_Object((1,3,6,1,4,1,32750,3,7,1,4,1,5),_LigoAthDot11RxWrongDirection_Type())
ligoAthDot11RxWrongDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxWrongDirection.setStatus(_A)
_LigoAthDot11RxMcastEcho_Type=Counter32
_LigoAthDot11RxMcastEcho_Object=MibTableColumn
ligoAthDot11RxMcastEcho=_LigoAthDot11RxMcastEcho_Object((1,3,6,1,4,1,32750,3,7,1,4,1,6),_LigoAthDot11RxMcastEcho_Type())
ligoAthDot11RxMcastEcho.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxMcastEcho.setStatus(_A)
_LigoAthDot11RxNotAssoc_Type=Counter32
_LigoAthDot11RxNotAssoc_Object=MibTableColumn
ligoAthDot11RxNotAssoc=_LigoAthDot11RxNotAssoc_Object((1,3,6,1,4,1,32750,3,7,1,4,1,7),_LigoAthDot11RxNotAssoc_Type())
ligoAthDot11RxNotAssoc.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxNotAssoc.setStatus(_A)
_LigoAthDot11RxNoPrivacy_Type=Counter32
_LigoAthDot11RxNoPrivacy_Object=MibTableColumn
ligoAthDot11RxNoPrivacy=_LigoAthDot11RxNoPrivacy_Object((1,3,6,1,4,1,32750,3,7,1,4,1,8),_LigoAthDot11RxNoPrivacy_Type())
ligoAthDot11RxNoPrivacy.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxNoPrivacy.setStatus(_A)
_LigoAthDot11RxUnencrypted_Type=Counter32
_LigoAthDot11RxUnencrypted_Object=MibTableColumn
ligoAthDot11RxUnencrypted=_LigoAthDot11RxUnencrypted_Object((1,3,6,1,4,1,32750,3,7,1,4,1,9),_LigoAthDot11RxUnencrypted_Type())
ligoAthDot11RxUnencrypted.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxUnencrypted.setStatus(_A)
_LigoAthDot11RxWepFail_Type=Counter32
_LigoAthDot11RxWepFail_Object=MibTableColumn
ligoAthDot11RxWepFail=_LigoAthDot11RxWepFail_Object((1,3,6,1,4,1,32750,3,7,1,4,1,10),_LigoAthDot11RxWepFail_Type())
ligoAthDot11RxWepFail.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxWepFail.setStatus(_A)
_LigoAthDot11RxDecapFail_Type=Counter32
_LigoAthDot11RxDecapFail_Object=MibTableColumn
ligoAthDot11RxDecapFail=_LigoAthDot11RxDecapFail_Object((1,3,6,1,4,1,32750,3,7,1,4,1,11),_LigoAthDot11RxDecapFail_Type())
ligoAthDot11RxDecapFail.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxDecapFail.setStatus(_A)
_LigoAthDot11RxDiscardMgt_Type=Counter32
_LigoAthDot11RxDiscardMgt_Object=MibTableColumn
ligoAthDot11RxDiscardMgt=_LigoAthDot11RxDiscardMgt_Object((1,3,6,1,4,1,32750,3,7,1,4,1,12),_LigoAthDot11RxDiscardMgt_Type())
ligoAthDot11RxDiscardMgt.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxDiscardMgt.setStatus(_A)
_LigoAthDot11RxDiscardCtrl_Type=Counter32
_LigoAthDot11RxDiscardCtrl_Object=MibTableColumn
ligoAthDot11RxDiscardCtrl=_LigoAthDot11RxDiscardCtrl_Object((1,3,6,1,4,1,32750,3,7,1,4,1,13),_LigoAthDot11RxDiscardCtrl_Type())
ligoAthDot11RxDiscardCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxDiscardCtrl.setStatus(_A)
_LigoAthDot11RxBeaconFrames_Type=Counter32
_LigoAthDot11RxBeaconFrames_Object=MibTableColumn
ligoAthDot11RxBeaconFrames=_LigoAthDot11RxBeaconFrames_Object((1,3,6,1,4,1,32750,3,7,1,4,1,14),_LigoAthDot11RxBeaconFrames_Type())
ligoAthDot11RxBeaconFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxBeaconFrames.setStatus(_A)
_LigoAthDot11RxRateSetTrunc_Type=Counter32
_LigoAthDot11RxRateSetTrunc_Object=MibTableColumn
ligoAthDot11RxRateSetTrunc=_LigoAthDot11RxRateSetTrunc_Object((1,3,6,1,4,1,32750,3,7,1,4,1,15),_LigoAthDot11RxRateSetTrunc_Type())
ligoAthDot11RxRateSetTrunc.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxRateSetTrunc.setStatus(_A)
_LigoAthDot11RxReqElemMissing_Type=Counter32
_LigoAthDot11RxReqElemMissing_Object=MibTableColumn
ligoAthDot11RxReqElemMissing=_LigoAthDot11RxReqElemMissing_Object((1,3,6,1,4,1,32750,3,7,1,4,1,16),_LigoAthDot11RxReqElemMissing_Type())
ligoAthDot11RxReqElemMissing.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxReqElemMissing.setStatus(_A)
_LigoAthDot11RxElementTooBig_Type=Counter32
_LigoAthDot11RxElementTooBig_Object=MibTableColumn
ligoAthDot11RxElementTooBig=_LigoAthDot11RxElementTooBig_Object((1,3,6,1,4,1,32750,3,7,1,4,1,17),_LigoAthDot11RxElementTooBig_Type())
ligoAthDot11RxElementTooBig.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxElementTooBig.setStatus(_A)
_LigoAthDot11RxElementTooSmall_Type=Counter32
_LigoAthDot11RxElementTooSmall_Object=MibTableColumn
ligoAthDot11RxElementTooSmall=_LigoAthDot11RxElementTooSmall_Object((1,3,6,1,4,1,32750,3,7,1,4,1,18),_LigoAthDot11RxElementTooSmall_Type())
ligoAthDot11RxElementTooSmall.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxElementTooSmall.setStatus(_A)
_LigoAthDot11RxElementUnknown_Type=Counter32
_LigoAthDot11RxElementUnknown_Object=MibTableColumn
ligoAthDot11RxElementUnknown=_LigoAthDot11RxElementUnknown_Object((1,3,6,1,4,1,32750,3,7,1,4,1,19),_LigoAthDot11RxElementUnknown_Type())
ligoAthDot11RxElementUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxElementUnknown.setStatus(_A)
_LigoAthDot11RxInvalidChannel_Type=Counter32
_LigoAthDot11RxInvalidChannel_Object=MibTableColumn
ligoAthDot11RxInvalidChannel=_LigoAthDot11RxInvalidChannel_Object((1,3,6,1,4,1,32750,3,7,1,4,1,20),_LigoAthDot11RxInvalidChannel_Type())
ligoAthDot11RxInvalidChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxInvalidChannel.setStatus(_A)
_LigoAthDot11RxChannelMismatch_Type=Counter32
_LigoAthDot11RxChannelMismatch_Object=MibTableColumn
ligoAthDot11RxChannelMismatch=_LigoAthDot11RxChannelMismatch_Object((1,3,6,1,4,1,32750,3,7,1,4,1,21),_LigoAthDot11RxChannelMismatch_Type())
ligoAthDot11RxChannelMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxChannelMismatch.setStatus(_A)
_LigoAthDot11RxNodesAllocated_Type=Counter32
_LigoAthDot11RxNodesAllocated_Object=MibTableColumn
ligoAthDot11RxNodesAllocated=_LigoAthDot11RxNodesAllocated_Object((1,3,6,1,4,1,32750,3,7,1,4,1,22),_LigoAthDot11RxNodesAllocated_Type())
ligoAthDot11RxNodesAllocated.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxNodesAllocated.setStatus(_A)
_LigoAthDot11RxSsidMismatch_Type=Counter32
_LigoAthDot11RxSsidMismatch_Object=MibTableColumn
ligoAthDot11RxSsidMismatch=_LigoAthDot11RxSsidMismatch_Object((1,3,6,1,4,1,32750,3,7,1,4,1,23),_LigoAthDot11RxSsidMismatch_Type())
ligoAthDot11RxSsidMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxSsidMismatch.setStatus(_A)
_LigoAthDot11RxUnsupportedAuthAlg_Type=Counter32
_LigoAthDot11RxUnsupportedAuthAlg_Object=MibTableColumn
ligoAthDot11RxUnsupportedAuthAlg=_LigoAthDot11RxUnsupportedAuthAlg_Object((1,3,6,1,4,1,32750,3,7,1,4,1,24),_LigoAthDot11RxUnsupportedAuthAlg_Type())
ligoAthDot11RxUnsupportedAuthAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxUnsupportedAuthAlg.setStatus(_A)
_LigoAthDot11RxAuthFail_Type=Counter32
_LigoAthDot11RxAuthFail_Object=MibTableColumn
ligoAthDot11RxAuthFail=_LigoAthDot11RxAuthFail_Object((1,3,6,1,4,1,32750,3,7,1,4,1,25),_LigoAthDot11RxAuthFail_Type())
ligoAthDot11RxAuthFail.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxAuthFail.setStatus(_A)
_LigoAthDot11RxTkipCtrm_Type=Counter32
_LigoAthDot11RxTkipCtrm_Object=MibTableColumn
ligoAthDot11RxTkipCtrm=_LigoAthDot11RxTkipCtrm_Object((1,3,6,1,4,1,32750,3,7,1,4,1,26),_LigoAthDot11RxTkipCtrm_Type())
ligoAthDot11RxTkipCtrm.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxTkipCtrm.setStatus(_A)
_LigoAthDot11RxAssocWrongBssid_Type=Counter32
_LigoAthDot11RxAssocWrongBssid_Object=MibTableColumn
ligoAthDot11RxAssocWrongBssid=_LigoAthDot11RxAssocWrongBssid_Object((1,3,6,1,4,1,32750,3,7,1,4,1,27),_LigoAthDot11RxAssocWrongBssid_Type())
ligoAthDot11RxAssocWrongBssid.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxAssocWrongBssid.setStatus(_A)
_LigoAthDot11RxAssocNotAuth_Type=Counter32
_LigoAthDot11RxAssocNotAuth_Object=MibTableColumn
ligoAthDot11RxAssocNotAuth=_LigoAthDot11RxAssocNotAuth_Object((1,3,6,1,4,1,32750,3,7,1,4,1,28),_LigoAthDot11RxAssocNotAuth_Type())
ligoAthDot11RxAssocNotAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxAssocNotAuth.setStatus(_A)
_LigoAthDot11RxAssocCapMismatch_Type=Counter32
_LigoAthDot11RxAssocCapMismatch_Object=MibTableColumn
ligoAthDot11RxAssocCapMismatch=_LigoAthDot11RxAssocCapMismatch_Object((1,3,6,1,4,1,32750,3,7,1,4,1,29),_LigoAthDot11RxAssocCapMismatch_Type())
ligoAthDot11RxAssocCapMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxAssocCapMismatch.setStatus(_A)
_LigoAthDot11RxAssocNoRateMatch_Type=Counter32
_LigoAthDot11RxAssocNoRateMatch_Object=MibTableColumn
ligoAthDot11RxAssocNoRateMatch=_LigoAthDot11RxAssocNoRateMatch_Object((1,3,6,1,4,1,32750,3,7,1,4,1,30),_LigoAthDot11RxAssocNoRateMatch_Type())
ligoAthDot11RxAssocNoRateMatch.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxAssocNoRateMatch.setStatus(_A)
_LigoAthDot11RxAssocBadWpaIe_Type=Counter32
_LigoAthDot11RxAssocBadWpaIe_Object=MibTableColumn
ligoAthDot11RxAssocBadWpaIe=_LigoAthDot11RxAssocBadWpaIe_Object((1,3,6,1,4,1,32750,3,7,1,4,1,31),_LigoAthDot11RxAssocBadWpaIe_Type())
ligoAthDot11RxAssocBadWpaIe.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxAssocBadWpaIe.setStatus(_A)
_LigoAthDot11RxDeauth_Type=Counter32
_LigoAthDot11RxDeauth_Object=MibTableColumn
ligoAthDot11RxDeauth=_LigoAthDot11RxDeauth_Object((1,3,6,1,4,1,32750,3,7,1,4,1,32),_LigoAthDot11RxDeauth_Type())
ligoAthDot11RxDeauth.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxDeauth.setStatus(_A)
_LigoAthDot11RxDisassoc_Type=Counter32
_LigoAthDot11RxDisassoc_Object=MibTableColumn
ligoAthDot11RxDisassoc=_LigoAthDot11RxDisassoc_Object((1,3,6,1,4,1,32750,3,7,1,4,1,33),_LigoAthDot11RxDisassoc_Type())
ligoAthDot11RxDisassoc.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxDisassoc.setStatus(_A)
_LigoAthDot11RxUnknownSubtype_Type=Counter32
_LigoAthDot11RxUnknownSubtype_Object=MibTableColumn
ligoAthDot11RxUnknownSubtype=_LigoAthDot11RxUnknownSubtype_Object((1,3,6,1,4,1,32750,3,7,1,4,1,34),_LigoAthDot11RxUnknownSubtype_Type())
ligoAthDot11RxUnknownSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxUnknownSubtype.setStatus(_A)
_LigoAthDot11RxNoBuffer_Type=Counter32
_LigoAthDot11RxNoBuffer_Object=MibTableColumn
ligoAthDot11RxNoBuffer=_LigoAthDot11RxNoBuffer_Object((1,3,6,1,4,1,32750,3,7,1,4,1,35),_LigoAthDot11RxNoBuffer_Type())
ligoAthDot11RxNoBuffer.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxNoBuffer.setStatus(_A)
_LigoAthDot11RxDecryptCrcError_Type=Counter32
_LigoAthDot11RxDecryptCrcError_Object=MibTableColumn
ligoAthDot11RxDecryptCrcError=_LigoAthDot11RxDecryptCrcError_Object((1,3,6,1,4,1,32750,3,7,1,4,1,36),_LigoAthDot11RxDecryptCrcError_Type())
ligoAthDot11RxDecryptCrcError.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxDecryptCrcError.setStatus(_A)
_LigoAthDot11RxMgmtInAhdocDemo_Type=Counter32
_LigoAthDot11RxMgmtInAhdocDemo_Object=MibTableColumn
ligoAthDot11RxMgmtInAhdocDemo=_LigoAthDot11RxMgmtInAhdocDemo_Object((1,3,6,1,4,1,32750,3,7,1,4,1,37),_LigoAthDot11RxMgmtInAhdocDemo_Type())
ligoAthDot11RxMgmtInAhdocDemo.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxMgmtInAhdocDemo.setStatus(_A)
_LigoAthDot11RxBadAuthRequest_Type=Counter32
_LigoAthDot11RxBadAuthRequest_Object=MibTableColumn
ligoAthDot11RxBadAuthRequest=_LigoAthDot11RxBadAuthRequest_Object((1,3,6,1,4,1,32750,3,7,1,4,1,38),_LigoAthDot11RxBadAuthRequest_Type())
ligoAthDot11RxBadAuthRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxBadAuthRequest.setStatus(_A)
_LigoAthDot11RxPortUnauth_Type=Counter32
_LigoAthDot11RxPortUnauth_Object=MibTableColumn
ligoAthDot11RxPortUnauth=_LigoAthDot11RxPortUnauth_Object((1,3,6,1,4,1,32750,3,7,1,4,1,39),_LigoAthDot11RxPortUnauth_Type())
ligoAthDot11RxPortUnauth.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxPortUnauth.setStatus(_A)
_LigoAthDot11RxBadKeyId_Type=Counter32
_LigoAthDot11RxBadKeyId_Object=MibTableColumn
ligoAthDot11RxBadKeyId=_LigoAthDot11RxBadKeyId_Object((1,3,6,1,4,1,32750,3,7,1,4,1,40),_LigoAthDot11RxBadKeyId_Type())
ligoAthDot11RxBadKeyId.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxBadKeyId.setStatus(_A)
_LigoAthDot11RxCcmpBadSeqNum_Type=Counter32
_LigoAthDot11RxCcmpBadSeqNum_Object=MibTableColumn
ligoAthDot11RxCcmpBadSeqNum=_LigoAthDot11RxCcmpBadSeqNum_Object((1,3,6,1,4,1,32750,3,7,1,4,1,41),_LigoAthDot11RxCcmpBadSeqNum_Type())
ligoAthDot11RxCcmpBadSeqNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxCcmpBadSeqNum.setStatus(_A)
_LigoAthDot11RxCcmpBadFormat_Type=Counter32
_LigoAthDot11RxCcmpBadFormat_Object=MibTableColumn
ligoAthDot11RxCcmpBadFormat=_LigoAthDot11RxCcmpBadFormat_Object((1,3,6,1,4,1,32750,3,7,1,4,1,42),_LigoAthDot11RxCcmpBadFormat_Type())
ligoAthDot11RxCcmpBadFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxCcmpBadFormat.setStatus(_A)
_LigoAthDot11RxCcmpMicCheck_Type=Counter32
_LigoAthDot11RxCcmpMicCheck_Object=MibTableColumn
ligoAthDot11RxCcmpMicCheck=_LigoAthDot11RxCcmpMicCheck_Object((1,3,6,1,4,1,32750,3,7,1,4,1,43),_LigoAthDot11RxCcmpMicCheck_Type())
ligoAthDot11RxCcmpMicCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxCcmpMicCheck.setStatus(_A)
_LigoAthDot11RxTkipBadSeqNum_Type=Counter32
_LigoAthDot11RxTkipBadSeqNum_Object=MibTableColumn
ligoAthDot11RxTkipBadSeqNum=_LigoAthDot11RxTkipBadSeqNum_Object((1,3,6,1,4,1,32750,3,7,1,4,1,44),_LigoAthDot11RxTkipBadSeqNum_Type())
ligoAthDot11RxTkipBadSeqNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxTkipBadSeqNum.setStatus(_A)
_LigoAthDot11RxTkipBadFormat_Type=Counter32
_LigoAthDot11RxTkipBadFormat_Object=MibTableColumn
ligoAthDot11RxTkipBadFormat=_LigoAthDot11RxTkipBadFormat_Object((1,3,6,1,4,1,32750,3,7,1,4,1,45),_LigoAthDot11RxTkipBadFormat_Type())
ligoAthDot11RxTkipBadFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxTkipBadFormat.setStatus(_A)
_LigoAthDot11RxTkipMicCheck_Type=Counter32
_LigoAthDot11RxTkipMicCheck_Object=MibTableColumn
ligoAthDot11RxTkipMicCheck=_LigoAthDot11RxTkipMicCheck_Object((1,3,6,1,4,1,32750,3,7,1,4,1,46),_LigoAthDot11RxTkipMicCheck_Type())
ligoAthDot11RxTkipMicCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxTkipMicCheck.setStatus(_A)
_LigoAthDot11RxTkipIcvCheck_Type=Counter32
_LigoAthDot11RxTkipIcvCheck_Object=MibTableColumn
ligoAthDot11RxTkipIcvCheck=_LigoAthDot11RxTkipIcvCheck_Object((1,3,6,1,4,1,32750,3,7,1,4,1,47),_LigoAthDot11RxTkipIcvCheck_Type())
ligoAthDot11RxTkipIcvCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxTkipIcvCheck.setStatus(_A)
_LigoAthDot11RxBadCipherKeyType_Type=Counter32
_LigoAthDot11RxBadCipherKeyType_Object=MibTableColumn
ligoAthDot11RxBadCipherKeyType=_LigoAthDot11RxBadCipherKeyType_Object((1,3,6,1,4,1,32750,3,7,1,4,1,48),_LigoAthDot11RxBadCipherKeyType_Type())
ligoAthDot11RxBadCipherKeyType.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxBadCipherKeyType.setStatus(_A)
_LigoAthDot11RxCipherKeyNotSet_Type=Counter32
_LigoAthDot11RxCipherKeyNotSet_Object=MibTableColumn
ligoAthDot11RxCipherKeyNotSet=_LigoAthDot11RxCipherKeyNotSet_Object((1,3,6,1,4,1,32750,3,7,1,4,1,49),_LigoAthDot11RxCipherKeyNotSet_Type())
ligoAthDot11RxCipherKeyNotSet.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxCipherKeyNotSet.setStatus(_A)
_LigoAthDot11RxAclPolicy_Type=Counter32
_LigoAthDot11RxAclPolicy_Object=MibTableColumn
ligoAthDot11RxAclPolicy=_LigoAthDot11RxAclPolicy_Object((1,3,6,1,4,1,32750,3,7,1,4,1,50),_LigoAthDot11RxAclPolicy_Type())
ligoAthDot11RxAclPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxAclPolicy.setStatus(_A)
_LigoAthDot11RxFastFrames_Type=Counter32
_LigoAthDot11RxFastFrames_Object=MibTableColumn
ligoAthDot11RxFastFrames=_LigoAthDot11RxFastFrames_Object((1,3,6,1,4,1,32750,3,7,1,4,1,51),_LigoAthDot11RxFastFrames_Type())
ligoAthDot11RxFastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxFastFrames.setStatus(_A)
_LigoAthDot11RxFfBadTunnelHdr_Type=Counter32
_LigoAthDot11RxFfBadTunnelHdr_Object=MibTableColumn
ligoAthDot11RxFfBadTunnelHdr=_LigoAthDot11RxFfBadTunnelHdr_Object((1,3,6,1,4,1,32750,3,7,1,4,1,52),_LigoAthDot11RxFfBadTunnelHdr_Type())
ligoAthDot11RxFfBadTunnelHdr.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11RxFfBadTunnelHdr.setStatus(_A)
_LigoAthDot11TxNoBuffer_Type=Counter32
_LigoAthDot11TxNoBuffer_Object=MibTableColumn
ligoAthDot11TxNoBuffer=_LigoAthDot11TxNoBuffer_Object((1,3,6,1,4,1,32750,3,7,1,4,1,53),_LigoAthDot11TxNoBuffer_Type())
ligoAthDot11TxNoBuffer.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11TxNoBuffer.setStatus(_A)
_LigoAthDot11TxNoNode_Type=Counter32
_LigoAthDot11TxNoNode_Object=MibTableColumn
ligoAthDot11TxNoNode=_LigoAthDot11TxNoNode_Object((1,3,6,1,4,1,32750,3,7,1,4,1,54),_LigoAthDot11TxNoNode_Type())
ligoAthDot11TxNoNode.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11TxNoNode.setStatus(_A)
_LigoAthDot11TxBadMgtFrames_Type=Counter32
_LigoAthDot11TxBadMgtFrames_Object=MibTableColumn
ligoAthDot11TxBadMgtFrames=_LigoAthDot11TxBadMgtFrames_Object((1,3,6,1,4,1,32750,3,7,1,4,1,55),_LigoAthDot11TxBadMgtFrames_Type())
ligoAthDot11TxBadMgtFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11TxBadMgtFrames.setStatus(_A)
_LigoAthDot11TxBadCipherKeyType_Type=Counter32
_LigoAthDot11TxBadCipherKeyType_Object=MibTableColumn
ligoAthDot11TxBadCipherKeyType=_LigoAthDot11TxBadCipherKeyType_Object((1,3,6,1,4,1,32750,3,7,1,4,1,56),_LigoAthDot11TxBadCipherKeyType_Type())
ligoAthDot11TxBadCipherKeyType.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11TxBadCipherKeyType.setStatus(_A)
_LigoAthDot11TxNoDefKey_Type=Counter32
_LigoAthDot11TxNoDefKey_Object=MibTableColumn
ligoAthDot11TxNoDefKey=_LigoAthDot11TxNoDefKey_Object((1,3,6,1,4,1,32750,3,7,1,4,1,57),_LigoAthDot11TxNoDefKey_Type())
ligoAthDot11TxNoDefKey.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11TxNoDefKey.setStatus(_A)
_LigoAthDot11TxNoCryptoHeadroom_Type=Counter32
_LigoAthDot11TxNoCryptoHeadroom_Object=MibTableColumn
ligoAthDot11TxNoCryptoHeadroom=_LigoAthDot11TxNoCryptoHeadroom_Object((1,3,6,1,4,1,32750,3,7,1,4,1,58),_LigoAthDot11TxNoCryptoHeadroom_Type())
ligoAthDot11TxNoCryptoHeadroom.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11TxNoCryptoHeadroom.setStatus(_A)
_LigoAthDot11TxGoodFastFrames_Type=Counter32
_LigoAthDot11TxGoodFastFrames_Object=MibTableColumn
ligoAthDot11TxGoodFastFrames=_LigoAthDot11TxGoodFastFrames_Object((1,3,6,1,4,1,32750,3,7,1,4,1,59),_LigoAthDot11TxGoodFastFrames_Type())
ligoAthDot11TxGoodFastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11TxGoodFastFrames.setStatus(_A)
_LigoAthDot11TxBadFastFrames_Type=Counter32
_LigoAthDot11TxBadFastFrames_Object=MibTableColumn
ligoAthDot11TxBadFastFrames=_LigoAthDot11TxBadFastFrames_Object((1,3,6,1,4,1,32750,3,7,1,4,1,60),_LigoAthDot11TxBadFastFrames_Type())
ligoAthDot11TxBadFastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11TxBadFastFrames.setStatus(_A)
_LigoAthDot11ActiveScans_Type=Counter32
_LigoAthDot11ActiveScans_Object=MibTableColumn
ligoAthDot11ActiveScans=_LigoAthDot11ActiveScans_Object((1,3,6,1,4,1,32750,3,7,1,4,1,61),_LigoAthDot11ActiveScans_Type())
ligoAthDot11ActiveScans.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11ActiveScans.setStatus(_A)
_LigoAthDot11PassiveScans_Type=Counter32
_LigoAthDot11PassiveScans_Object=MibTableColumn
ligoAthDot11PassiveScans=_LigoAthDot11PassiveScans_Object((1,3,6,1,4,1,32750,3,7,1,4,1,62),_LigoAthDot11PassiveScans_Type())
ligoAthDot11PassiveScans.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11PassiveScans.setStatus(_A)
_LigoAthDot11NodesTimeout_Type=Counter32
_LigoAthDot11NodesTimeout_Object=MibTableColumn
ligoAthDot11NodesTimeout=_LigoAthDot11NodesTimeout_Object((1,3,6,1,4,1,32750,3,7,1,4,1,63),_LigoAthDot11NodesTimeout_Type())
ligoAthDot11NodesTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11NodesTimeout.setStatus(_A)
_LigoAthDot11CryptoCipherMalloc_Type=Counter32
_LigoAthDot11CryptoCipherMalloc_Object=MibTableColumn
ligoAthDot11CryptoCipherMalloc=_LigoAthDot11CryptoCipherMalloc_Object((1,3,6,1,4,1,32750,3,7,1,4,1,64),_LigoAthDot11CryptoCipherMalloc_Type())
ligoAthDot11CryptoCipherMalloc.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11CryptoCipherMalloc.setStatus(_A)
_LigoAthDot11CryptoSwTkip_Type=Counter32
_LigoAthDot11CryptoSwTkip_Object=MibTableColumn
ligoAthDot11CryptoSwTkip=_LigoAthDot11CryptoSwTkip_Object((1,3,6,1,4,1,32750,3,7,1,4,1,65),_LigoAthDot11CryptoSwTkip_Type())
ligoAthDot11CryptoSwTkip.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11CryptoSwTkip.setStatus(_A)
_LigoAthDot11CryptoTkipSwMicEnc_Type=Counter32
_LigoAthDot11CryptoTkipSwMicEnc_Object=MibTableColumn
ligoAthDot11CryptoTkipSwMicEnc=_LigoAthDot11CryptoTkipSwMicEnc_Object((1,3,6,1,4,1,32750,3,7,1,4,1,66),_LigoAthDot11CryptoTkipSwMicEnc_Type())
ligoAthDot11CryptoTkipSwMicEnc.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11CryptoTkipSwMicEnc.setStatus(_A)
_LigoAthDot11CryptoTkipSwMicDec_Type=Counter32
_LigoAthDot11CryptoTkipSwMicDec_Object=MibTableColumn
ligoAthDot11CryptoTkipSwMicDec=_LigoAthDot11CryptoTkipSwMicDec_Object((1,3,6,1,4,1,32750,3,7,1,4,1,67),_LigoAthDot11CryptoTkipSwMicDec_Type())
ligoAthDot11CryptoTkipSwMicDec.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11CryptoTkipSwMicDec.setStatus(_A)
_LigoAthDot11CryptoTkipCtrm_Type=Counter32
_LigoAthDot11CryptoTkipCtrm_Object=MibTableColumn
ligoAthDot11CryptoTkipCtrm=_LigoAthDot11CryptoTkipCtrm_Object((1,3,6,1,4,1,32750,3,7,1,4,1,68),_LigoAthDot11CryptoTkipCtrm_Type())
ligoAthDot11CryptoTkipCtrm.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11CryptoTkipCtrm.setStatus(_A)
_LigoAthDot11CryptoSwCcmp_Type=Counter32
_LigoAthDot11CryptoSwCcmp_Object=MibTableColumn
ligoAthDot11CryptoSwCcmp=_LigoAthDot11CryptoSwCcmp_Object((1,3,6,1,4,1,32750,3,7,1,4,1,69),_LigoAthDot11CryptoSwCcmp_Type())
ligoAthDot11CryptoSwCcmp.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11CryptoSwCcmp.setStatus(_A)
_LigoAthDot11CryptoSwWep_Type=Counter32
_LigoAthDot11CryptoSwWep_Object=MibTableColumn
ligoAthDot11CryptoSwWep=_LigoAthDot11CryptoSwWep_Object((1,3,6,1,4,1,32750,3,7,1,4,1,70),_LigoAthDot11CryptoSwWep_Type())
ligoAthDot11CryptoSwWep.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11CryptoSwWep.setStatus(_A)
_LigoAthDot11CryptoCipherRej_Type=Counter32
_LigoAthDot11CryptoCipherRej_Object=MibTableColumn
ligoAthDot11CryptoCipherRej=_LigoAthDot11CryptoCipherRej_Object((1,3,6,1,4,1,32750,3,7,1,4,1,71),_LigoAthDot11CryptoCipherRej_Type())
ligoAthDot11CryptoCipherRej.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11CryptoCipherRej.setStatus(_A)
_LigoAthDot11CryptoNoKey_Type=Counter32
_LigoAthDot11CryptoNoKey_Object=MibTableColumn
ligoAthDot11CryptoNoKey=_LigoAthDot11CryptoNoKey_Object((1,3,6,1,4,1,32750,3,7,1,4,1,72),_LigoAthDot11CryptoNoKey_Type())
ligoAthDot11CryptoNoKey.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11CryptoNoKey.setStatus(_A)
_LigoAthDot11CryptoDelKey_Type=Counter32
_LigoAthDot11CryptoDelKey_Object=MibTableColumn
ligoAthDot11CryptoDelKey=_LigoAthDot11CryptoDelKey_Object((1,3,6,1,4,1,32750,3,7,1,4,1,73),_LigoAthDot11CryptoDelKey_Type())
ligoAthDot11CryptoDelKey.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11CryptoDelKey.setStatus(_A)
_LigoAthDot11CryptoBadCipher_Type=Counter32
_LigoAthDot11CryptoBadCipher_Object=MibTableColumn
ligoAthDot11CryptoBadCipher=_LigoAthDot11CryptoBadCipher_Object((1,3,6,1,4,1,32750,3,7,1,4,1,74),_LigoAthDot11CryptoBadCipher_Type())
ligoAthDot11CryptoBadCipher.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11CryptoBadCipher.setStatus(_A)
_LigoAthDot11CryptoNoCipher_Type=Counter32
_LigoAthDot11CryptoNoCipher_Object=MibTableColumn
ligoAthDot11CryptoNoCipher=_LigoAthDot11CryptoNoCipher_Object((1,3,6,1,4,1,32750,3,7,1,4,1,75),_LigoAthDot11CryptoNoCipher_Type())
ligoAthDot11CryptoNoCipher.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11CryptoNoCipher.setStatus(_A)
_LigoAthDot11CryptoAttachFail_Type=Counter32
_LigoAthDot11CryptoAttachFail_Object=MibTableColumn
ligoAthDot11CryptoAttachFail=_LigoAthDot11CryptoAttachFail_Object((1,3,6,1,4,1,32750,3,7,1,4,1,76),_LigoAthDot11CryptoAttachFail_Type())
ligoAthDot11CryptoAttachFail.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11CryptoAttachFail.setStatus(_A)
_LigoAthDot11CryptoSwFallback_Type=Counter32
_LigoAthDot11CryptoSwFallback_Object=MibTableColumn
ligoAthDot11CryptoSwFallback=_LigoAthDot11CryptoSwFallback_Object((1,3,6,1,4,1,32750,3,7,1,4,1,77),_LigoAthDot11CryptoSwFallback_Type())
ligoAthDot11CryptoSwFallback.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11CryptoSwFallback.setStatus(_A)
_LigoAthDot11CryptoKeyFail_Type=Counter32
_LigoAthDot11CryptoKeyFail_Object=MibTableColumn
ligoAthDot11CryptoKeyFail=_LigoAthDot11CryptoKeyFail_Object((1,3,6,1,4,1,32750,3,7,1,4,1,78),_LigoAthDot11CryptoKeyFail_Type())
ligoAthDot11CryptoKeyFail.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11CryptoKeyFail.setStatus(_A)
_LigoAthDot11SnoopMcastPass_Type=Counter32
_LigoAthDot11SnoopMcastPass_Object=MibTableColumn
ligoAthDot11SnoopMcastPass=_LigoAthDot11SnoopMcastPass_Object((1,3,6,1,4,1,32750,3,7,1,4,1,79),_LigoAthDot11SnoopMcastPass_Type())
ligoAthDot11SnoopMcastPass.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11SnoopMcastPass.setStatus(_A)
_LigoAthDot11SnoopMcastDrop_Type=Counter32
_LigoAthDot11SnoopMcastDrop_Object=MibTableColumn
ligoAthDot11SnoopMcastDrop=_LigoAthDot11SnoopMcastDrop_Object((1,3,6,1,4,1,32750,3,7,1,4,1,80),_LigoAthDot11SnoopMcastDrop_Type())
ligoAthDot11SnoopMcastDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthDot11SnoopMcastDrop.setStatus(_A)
_LigoAthPeerStatsTable_Object=MibTable
ligoAthPeerStatsTable=_LigoAthPeerStatsTable_Object((1,3,6,1,4,1,32750,3,7,1,5))
if mibBuilder.loadTexts:ligoAthPeerStatsTable.setStatus(_A)
_LigoAthPeerStatsEntry_Object=MibTableRow
ligoAthPeerStatsEntry=_LigoAthPeerStatsEntry_Object((1,3,6,1,4,1,32750,3,7,1,5,1))
ligoAthPeerStatsEntry.setIndexNames((0,_C,_D),(0,_E,_F))
if mibBuilder.loadTexts:ligoAthPeerStatsEntry.setStatus(_A)
_LigoAthPeerIndex_Type=Integer32
_LigoAthPeerIndex_Object=MibTableColumn
ligoAthPeerIndex=_LigoAthPeerIndex_Object((1,3,6,1,4,1,32750,3,7,1,5,1,1),_LigoAthPeerIndex_Type())
ligoAthPeerIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ligoAthPeerIndex.setStatus(_A)
_LigoAthPeerMacAddr_Type=MacAddress
_LigoAthPeerMacAddr_Object=MibTableColumn
ligoAthPeerMacAddr=_LigoAthPeerMacAddr_Object((1,3,6,1,4,1,32750,3,7,1,5,1,2),_LigoAthPeerMacAddr_Type())
ligoAthPeerMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerMacAddr.setStatus(_A)
_LigoAthPeerRxData_Type=Counter32
_LigoAthPeerRxData_Object=MibTableColumn
ligoAthPeerRxData=_LigoAthPeerRxData_Object((1,3,6,1,4,1,32750,3,7,1,5,1,3),_LigoAthPeerRxData_Type())
ligoAthPeerRxData.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerRxData.setStatus(_A)
_LigoAthPeerRxMgmt_Type=Counter32
_LigoAthPeerRxMgmt_Object=MibTableColumn
ligoAthPeerRxMgmt=_LigoAthPeerRxMgmt_Object((1,3,6,1,4,1,32750,3,7,1,5,1,4),_LigoAthPeerRxMgmt_Type())
ligoAthPeerRxMgmt.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerRxMgmt.setStatus(_A)
_LigoAthPeerRxCtrl_Type=Counter32
_LigoAthPeerRxCtrl_Object=MibTableColumn
ligoAthPeerRxCtrl=_LigoAthPeerRxCtrl_Object((1,3,6,1,4,1,32750,3,7,1,5,1,5),_LigoAthPeerRxCtrl_Type())
ligoAthPeerRxCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerRxCtrl.setStatus(_A)
_LigoAthPeerRxBeacons_Type=Counter64
_LigoAthPeerRxBeacons_Object=MibTableColumn
ligoAthPeerRxBeacons=_LigoAthPeerRxBeacons_Object((1,3,6,1,4,1,32750,3,7,1,5,1,6),_LigoAthPeerRxBeacons_Type())
ligoAthPeerRxBeacons.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerRxBeacons.setStatus(_A)
_LigoAthPeerRxProbeResponse_Type=Counter32
_LigoAthPeerRxProbeResponse_Object=MibTableColumn
ligoAthPeerRxProbeResponse=_LigoAthPeerRxProbeResponse_Object((1,3,6,1,4,1,32750,3,7,1,5,1,7),_LigoAthPeerRxProbeResponse_Type())
ligoAthPeerRxProbeResponse.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerRxProbeResponse.setStatus(_A)
_LigoAthPeerRxUcast_Type=Counter32
_LigoAthPeerRxUcast_Object=MibTableColumn
ligoAthPeerRxUcast=_LigoAthPeerRxUcast_Object((1,3,6,1,4,1,32750,3,7,1,5,1,8),_LigoAthPeerRxUcast_Type())
ligoAthPeerRxUcast.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerRxUcast.setStatus(_A)
_LigoAthPeerRxMcast_Type=Counter32
_LigoAthPeerRxMcast_Object=MibTableColumn
ligoAthPeerRxMcast=_LigoAthPeerRxMcast_Object((1,3,6,1,4,1,32750,3,7,1,5,1,9),_LigoAthPeerRxMcast_Type())
ligoAthPeerRxMcast.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerRxMcast.setStatus(_A)
_LigoAthPeerRxBytes_Type=Counter64
_LigoAthPeerRxBytes_Object=MibTableColumn
ligoAthPeerRxBytes=_LigoAthPeerRxBytes_Object((1,3,6,1,4,1,32750,3,7,1,5,1,10),_LigoAthPeerRxBytes_Type())
ligoAthPeerRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerRxBytes.setStatus(_A)
_LigoAthPeerRxDup_Type=Counter32
_LigoAthPeerRxDup_Object=MibTableColumn
ligoAthPeerRxDup=_LigoAthPeerRxDup_Object((1,3,6,1,4,1,32750,3,7,1,5,1,11),_LigoAthPeerRxDup_Type())
ligoAthPeerRxDup.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerRxDup.setStatus(_A)
_LigoAthPeerRxNoPrivacy_Type=Counter32
_LigoAthPeerRxNoPrivacy_Object=MibTableColumn
ligoAthPeerRxNoPrivacy=_LigoAthPeerRxNoPrivacy_Object((1,3,6,1,4,1,32750,3,7,1,5,1,12),_LigoAthPeerRxNoPrivacy_Type())
ligoAthPeerRxNoPrivacy.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerRxNoPrivacy.setStatus(_A)
_LigoAthPeerRxWepFail_Type=Counter32
_LigoAthPeerRxWepFail_Object=MibTableColumn
ligoAthPeerRxWepFail=_LigoAthPeerRxWepFail_Object((1,3,6,1,4,1,32750,3,7,1,5,1,13),_LigoAthPeerRxWepFail_Type())
ligoAthPeerRxWepFail.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerRxWepFail.setStatus(_A)
_LigoAthPeerRxDemicFail_Type=Counter32
_LigoAthPeerRxDemicFail_Object=MibTableColumn
ligoAthPeerRxDemicFail=_LigoAthPeerRxDemicFail_Object((1,3,6,1,4,1,32750,3,7,1,5,1,14),_LigoAthPeerRxDemicFail_Type())
ligoAthPeerRxDemicFail.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerRxDemicFail.setStatus(_A)
_LigoAthPeerRxDecapFail_Type=Counter32
_LigoAthPeerRxDecapFail_Object=MibTableColumn
ligoAthPeerRxDecapFail=_LigoAthPeerRxDecapFail_Object((1,3,6,1,4,1,32750,3,7,1,5,1,15),_LigoAthPeerRxDecapFail_Type())
ligoAthPeerRxDecapFail.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerRxDecapFail.setStatus(_A)
_LigoAthPeerRxDefragFail_Type=Counter32
_LigoAthPeerRxDefragFail_Object=MibTableColumn
ligoAthPeerRxDefragFail=_LigoAthPeerRxDefragFail_Object((1,3,6,1,4,1,32750,3,7,1,5,1,16),_LigoAthPeerRxDefragFail_Type())
ligoAthPeerRxDefragFail.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerRxDefragFail.setStatus(_A)
_LigoAthPeerRxDissasoc_Type=Counter32
_LigoAthPeerRxDissasoc_Object=MibTableColumn
ligoAthPeerRxDissasoc=_LigoAthPeerRxDissasoc_Object((1,3,6,1,4,1,32750,3,7,1,5,1,17),_LigoAthPeerRxDissasoc_Type())
ligoAthPeerRxDissasoc.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerRxDissasoc.setStatus(_A)
_LigoAthPeerRxDeauth_Type=Counter32
_LigoAthPeerRxDeauth_Object=MibTableColumn
ligoAthPeerRxDeauth=_LigoAthPeerRxDeauth_Object((1,3,6,1,4,1,32750,3,7,1,5,1,18),_LigoAthPeerRxDeauth_Type())
ligoAthPeerRxDeauth.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerRxDeauth.setStatus(_A)
_LigoAthPeerRxDecryptCrc_Type=Counter32
_LigoAthPeerRxDecryptCrc_Object=MibTableColumn
ligoAthPeerRxDecryptCrc=_LigoAthPeerRxDecryptCrc_Object((1,3,6,1,4,1,32750,3,7,1,5,1,19),_LigoAthPeerRxDecryptCrc_Type())
ligoAthPeerRxDecryptCrc.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerRxDecryptCrc.setStatus(_A)
_LigoAthPeerRxUnauth_Type=Counter32
_LigoAthPeerRxUnauth_Object=MibTableColumn
ligoAthPeerRxUnauth=_LigoAthPeerRxUnauth_Object((1,3,6,1,4,1,32750,3,7,1,5,1,20),_LigoAthPeerRxUnauth_Type())
ligoAthPeerRxUnauth.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerRxUnauth.setStatus(_A)
_LigoAthPeerRxUnencrypted_Type=Counter32
_LigoAthPeerRxUnencrypted_Object=MibTableColumn
ligoAthPeerRxUnencrypted=_LigoAthPeerRxUnencrypted_Object((1,3,6,1,4,1,32750,3,7,1,5,1,21),_LigoAthPeerRxUnencrypted_Type())
ligoAthPeerRxUnencrypted.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerRxUnencrypted.setStatus(_A)
_LigoAthPeerTxData_Type=Counter32
_LigoAthPeerTxData_Object=MibTableColumn
ligoAthPeerTxData=_LigoAthPeerTxData_Object((1,3,6,1,4,1,32750,3,7,1,5,1,22),_LigoAthPeerTxData_Type())
ligoAthPeerTxData.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerTxData.setStatus(_A)
_LigoAthPeerTxMgmt_Type=Counter32
_LigoAthPeerTxMgmt_Object=MibTableColumn
ligoAthPeerTxMgmt=_LigoAthPeerTxMgmt_Object((1,3,6,1,4,1,32750,3,7,1,5,1,23),_LigoAthPeerTxMgmt_Type())
ligoAthPeerTxMgmt.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerTxMgmt.setStatus(_A)
_LigoAthPeerTxProbeReq_Type=Counter32
_LigoAthPeerTxProbeReq_Object=MibTableColumn
ligoAthPeerTxProbeReq=_LigoAthPeerTxProbeReq_Object((1,3,6,1,4,1,32750,3,7,1,5,1,24),_LigoAthPeerTxProbeReq_Type())
ligoAthPeerTxProbeReq.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerTxProbeReq.setStatus(_A)
_LigoAthPeerTxUcast_Type=Counter32
_LigoAthPeerTxUcast_Object=MibTableColumn
ligoAthPeerTxUcast=_LigoAthPeerTxUcast_Object((1,3,6,1,4,1,32750,3,7,1,5,1,25),_LigoAthPeerTxUcast_Type())
ligoAthPeerTxUcast.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerTxUcast.setStatus(_A)
_LigoAthPeerTxMcast_Type=Counter32
_LigoAthPeerTxMcast_Object=MibTableColumn
ligoAthPeerTxMcast=_LigoAthPeerTxMcast_Object((1,3,6,1,4,1,32750,3,7,1,5,1,26),_LigoAthPeerTxMcast_Type())
ligoAthPeerTxMcast.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerTxMcast.setStatus(_A)
_LigoAthPeerTxBytes_Type=Counter64
_LigoAthPeerTxBytes_Object=MibTableColumn
ligoAthPeerTxBytes=_LigoAthPeerTxBytes_Object((1,3,6,1,4,1,32750,3,7,1,5,1,27),_LigoAthPeerTxBytes_Type())
ligoAthPeerTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerTxBytes.setStatus(_A)
_LigoAthPeerTxNoVlanTag_Type=Counter32
_LigoAthPeerTxNoVlanTag_Object=MibTableColumn
ligoAthPeerTxNoVlanTag=_LigoAthPeerTxNoVlanTag_Object((1,3,6,1,4,1,32750,3,7,1,5,1,28),_LigoAthPeerTxNoVlanTag_Type())
ligoAthPeerTxNoVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerTxNoVlanTag.setStatus(_A)
_LigoAthPeerTxVlanMismatch_Type=Counter32
_LigoAthPeerTxVlanMismatch_Object=MibTableColumn
ligoAthPeerTxVlanMismatch=_LigoAthPeerTxVlanMismatch_Object((1,3,6,1,4,1,32750,3,7,1,5,1,29),_LigoAthPeerTxVlanMismatch_Type())
ligoAthPeerTxVlanMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerTxVlanMismatch.setStatus(_A)
_LigoAthPeerTxUapsd_Type=Counter32
_LigoAthPeerTxUapsd_Object=MibTableColumn
ligoAthPeerTxUapsd=_LigoAthPeerTxUapsd_Object((1,3,6,1,4,1,32750,3,7,1,5,1,30),_LigoAthPeerTxUapsd_Type())
ligoAthPeerTxUapsd.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerTxUapsd.setStatus(_A)
_LigoAthPeerUapsdTriggers_Type=Counter32
_LigoAthPeerUapsdTriggers_Object=MibTableColumn
ligoAthPeerUapsdTriggers=_LigoAthPeerUapsdTriggers_Object((1,3,6,1,4,1,32750,3,7,1,5,1,31),_LigoAthPeerUapsdTriggers_Type())
ligoAthPeerUapsdTriggers.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerUapsdTriggers.setStatus(_A)
_LigoAthPeerTxEospLost_Type=Counter32
_LigoAthPeerTxEospLost_Object=MibTableColumn
ligoAthPeerTxEospLost=_LigoAthPeerTxEospLost_Object((1,3,6,1,4,1,32750,3,7,1,5,1,32),_LigoAthPeerTxEospLost_Type())
ligoAthPeerTxEospLost.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerTxEospLost.setStatus(_A)
_LigoAthPeerTxAssoc_Type=Counter32
_LigoAthPeerTxAssoc_Object=MibTableColumn
ligoAthPeerTxAssoc=_LigoAthPeerTxAssoc_Object((1,3,6,1,4,1,32750,3,7,1,5,1,33),_LigoAthPeerTxAssoc_Type())
ligoAthPeerTxAssoc.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerTxAssoc.setStatus(_A)
_LigoAthPeerTxAssocFail_Type=Counter32
_LigoAthPeerTxAssocFail_Object=MibTableColumn
ligoAthPeerTxAssocFail=_LigoAthPeerTxAssocFail_Object((1,3,6,1,4,1,32750,3,7,1,5,1,34),_LigoAthPeerTxAssocFail_Type())
ligoAthPeerTxAssocFail.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerTxAssocFail.setStatus(_A)
_LigoAthPeerTxAuth_Type=Counter32
_LigoAthPeerTxAuth_Object=MibTableColumn
ligoAthPeerTxAuth=_LigoAthPeerTxAuth_Object((1,3,6,1,4,1,32750,3,7,1,5,1,35),_LigoAthPeerTxAuth_Type())
ligoAthPeerTxAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerTxAuth.setStatus(_A)
_LigoAthPeerTxAuthFail_Type=Counter32
_LigoAthPeerTxAuthFail_Object=MibTableColumn
ligoAthPeerTxAuthFail=_LigoAthPeerTxAuthFail_Object((1,3,6,1,4,1,32750,3,7,1,5,1,36),_LigoAthPeerTxAuthFail_Type())
ligoAthPeerTxAuthFail.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerTxAuthFail.setStatus(_A)
_LigoAthPeerTxDeauth_Type=Counter32
_LigoAthPeerTxDeauth_Object=MibTableColumn
ligoAthPeerTxDeauth=_LigoAthPeerTxDeauth_Object((1,3,6,1,4,1,32750,3,7,1,5,1,37),_LigoAthPeerTxDeauth_Type())
ligoAthPeerTxDeauth.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerTxDeauth.setStatus(_A)
_LigoAthPeerTxDeauthCode_Type=Counter32
_LigoAthPeerTxDeauthCode_Object=MibTableColumn
ligoAthPeerTxDeauthCode=_LigoAthPeerTxDeauthCode_Object((1,3,6,1,4,1,32750,3,7,1,5,1,38),_LigoAthPeerTxDeauthCode_Type())
ligoAthPeerTxDeauthCode.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerTxDeauthCode.setStatus(_A)
_LigoAthPeerTxDisassoc_Type=Counter32
_LigoAthPeerTxDisassoc_Object=MibTableColumn
ligoAthPeerTxDisassoc=_LigoAthPeerTxDisassoc_Object((1,3,6,1,4,1,32750,3,7,1,5,1,39),_LigoAthPeerTxDisassoc_Type())
ligoAthPeerTxDisassoc.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerTxDisassoc.setStatus(_A)
_LigoAthPeerTxDisassocCode_Type=Counter32
_LigoAthPeerTxDisassocCode_Object=MibTableColumn
ligoAthPeerTxDisassocCode=_LigoAthPeerTxDisassocCode_Object((1,3,6,1,4,1,32750,3,7,1,5,1,40),_LigoAthPeerTxDisassocCode_Type())
ligoAthPeerTxDisassocCode.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerTxDisassocCode.setStatus(_A)
_LigoAthPeerPsqDrops_Type=Counter32
_LigoAthPeerPsqDrops_Object=MibTableColumn
ligoAthPeerPsqDrops=_LigoAthPeerPsqDrops_Object((1,3,6,1,4,1,32750,3,7,1,5,1,41),_LigoAthPeerPsqDrops_Type())
ligoAthPeerPsqDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerPsqDrops.setStatus(_A)
_LigoAthPeerMcastSnoop_Type=Counter32
_LigoAthPeerMcastSnoop_Object=MibTableColumn
ligoAthPeerMcastSnoop=_LigoAthPeerMcastSnoop_Object((1,3,6,1,4,1,32750,3,7,1,5,1,42),_LigoAthPeerMcastSnoop_Type())
ligoAthPeerMcastSnoop.setMaxAccess(_B)
if mibBuilder.loadTexts:ligoAthPeerMcastSnoop.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ligoAthDrvStatsMIB':ligoAthDrvStatsMIB,'ligoAthDrvStatsMIBObjects':ligoAthDrvStatsMIBObjects,'ligoAthStatsTable':ligoAthStatsTable,'ligoAthStatsEntry':ligoAthStatsEntry,'ligoAthWatchdogTimeouts':ligoAthWatchdogTimeouts,'ligoAthHardwareErrorInterrupts':ligoAthHardwareErrorInterrupts,'ligoAthBeaconMissInterrupts':ligoAthBeaconMissInterrupts,'ligoAthRecvOverrunInterrupts':ligoAthRecvOverrunInterrupts,'ligoAthRecvEolInterrupts':ligoAthRecvEolInterrupts,'ligoAthTxmitUnderrunInterrupts':ligoAthTxmitUnderrunInterrupts,'ligoAthTxManagementFrames':ligoAthTxManagementFrames,'ligoAthTxFramesDiscQueueDepth':ligoAthTxFramesDiscQueueDepth,'ligoAthTxFramesDiscDeviceGone':ligoAthTxFramesDiscDeviceGone,'ligoAthTxQueueFull':ligoAthTxQueueFull,'ligoAthTxEncapsulationFailed':ligoAthTxEncapsulationFailed,'ligoAthTxFailedNoNode':ligoAthTxFailedNoNode,'ligoAthTxFailedNoDataTxBuffer':ligoAthTxFailedNoDataTxBuffer,'ligoAthTxFailedNoMgtTxBuffer':ligoAthTxFailedNoMgtTxBuffer,'ligoAthTxFailedTooManyRetries':ligoAthTxFailedTooManyRetries,'ligoAthTxFailedFifoUnderrun':ligoAthTxFailedFifoUnderrun,'ligoAthTxFailedXmitFiltered':ligoAthTxFailedXmitFiltered,'ligoAthShortOnchipTxRetries':ligoAthShortOnchipTxRetries,'ligoAthLongOnchipTxRetries':ligoAthLongOnchipTxRetries,'ligoAthTxFailedBogusXmitRate':ligoAthTxFailedBogusXmitRate,'ligoAthTxFramesNoAckMarked':ligoAthTxFramesNoAckMarked,'ligoAthTxFramesRtsEnabled':ligoAthTxFramesRtsEnabled,'ligoAthTxFramesCtsEnabled':ligoAthTxFramesCtsEnabled,'ligoAthTxFramesShortPreamble':ligoAthTxFramesShortPreamble,'ligoAthTxFramesAlternateRate':ligoAthTxFramesAlternateRate,'ligoAthTxFrames11gProtection':ligoAthTxFrames11gProtection,'ligoAthRxFailedDescOverrun':ligoAthRxFailedDescOverrun,'ligoAthRxFailedBadCrc':ligoAthRxFailedBadCrc,'ligoAthRxFailedFifoOverrun':ligoAthRxFailedFifoOverrun,'ligoAthRxFailedDecryptErrors':ligoAthRxFailedDecryptErrors,'ligoAthRxFailedMicFailure':ligoAthRxFailedMicFailure,'ligoAthRxFailedFrameTooShort':ligoAthRxFailedFrameTooShort,'ligoAthRxSetupFailedNoSkbuff':ligoAthRxSetupFailedNoSkbuff,'ligoAthRxManagementFrames':ligoAthRxManagementFrames,'ligoAthRxControlFrames':ligoAthRxControlFrames,'ligoAthNoSkbuffForBeacon':ligoAthNoSkbuffForBeacon,'ligoAthBeaconsTransmitted':ligoAthBeaconsTransmitted,'ligoAthPeriodicCalibrations':ligoAthPeriodicCalibrations,'ligoAthPeriodicCalibrFailures':ligoAthPeriodicCalibrFailures,'ligoAthRfgainValueChange':ligoAthRfgainValueChange,'ligoAthRateControlChecks':ligoAthRateControlChecks,'ligoAthRateCtrlRaisedXmitRate':ligoAthRateCtrlRaisedXmitRate,'ligoAthRateCtrlDroppedXmitRate':ligoAthRateCtrlDroppedXmitRate,'ligoAthRssiOfLastAck':ligoAthRssiOfLastAck,'ligoAthRssiOfLastRcv':ligoAthRssiOfLastRcv,'ligoAthPhyErrorsTable':ligoAthPhyErrorsTable,'ligoAthPhyErrorsEntry':ligoAthPhyErrorsEntry,'ligoAthPhyTransmitUnderrun':ligoAthPhyTransmitUnderrun,'ligoAthPhyTimingError':ligoAthPhyTimingError,'ligoAthPhyIllegalParity':ligoAthPhyIllegalParity,'ligoAthPhyIllegalRate':ligoAthPhyIllegalRate,'ligoAthPhyIllegalLength':ligoAthPhyIllegalLength,'ligoAthPhyRadarDetect':ligoAthPhyRadarDetect,'ligoAthPhyIllegalService':ligoAthPhyIllegalService,'ligoAthPhyTxmitOverrideRecv':ligoAthPhyTxmitOverrideRecv,'ligoAthPhyOfdmTiming':ligoAthPhyOfdmTiming,'ligoAthPhyOfdmIllegalParity':ligoAthPhyOfdmIllegalParity,'ligoAthPhyOfdmIllegalRate':ligoAthPhyOfdmIllegalRate,'ligoAthPhyOfdmIllegalLength':ligoAthPhyOfdmIllegalLength,'ligoAthPhyOfdmPowerDrop':ligoAthPhyOfdmPowerDrop,'ligoAthPhyOfdmIllegalService':ligoAthPhyOfdmIllegalService,'ligoAthPhyOfdmRestart':ligoAthPhyOfdmRestart,'ligoAthPhyCckTiming':ligoAthPhyCckTiming,'ligoAthPhyCckHeaderCrc':ligoAthPhyCckHeaderCrc,'ligoAthPhyCckIllegalRate':ligoAthPhyCckIllegalRate,'ligoAthPhyCckIllegalService':ligoAthPhyCckIllegalService,'ligoAthPhyCckRestart':ligoAthPhyCckRestart,'ligoAthAntennaStatsTable':ligoAthAntennaStatsTable,'ligoAthAntennaStatsEntry':ligoAthAntennaStatsEntry,'ligoAthSwitchedDefaultRxAntenna':ligoAthSwitchedDefaultRxAntenna,'ligoAthTxUsedAlternateAntenna':ligoAthTxUsedAlternateAntenna,'ligoAthTxFramesAntenna1':ligoAthTxFramesAntenna1,'ligoAthRxFramesAntenna1':ligoAthRxFramesAntenna1,'ligoAthTxFramesAntenna2':ligoAthTxFramesAntenna2,'ligoAthRxFramesAntenna2':ligoAthRxFramesAntenna2,'ligoAthTxFramesAntenna3':ligoAthTxFramesAntenna3,'ligoAthRxFramesAntenna3':ligoAthRxFramesAntenna3,'ligoAthDot11StatsTable':ligoAthDot11StatsTable,'ligoAthDot11StatsEntry':ligoAthDot11StatsEntry,'ligoAthDot11RxBadVersion':ligoAthDot11RxBadVersion,'ligoAthDot11RxTooShort':ligoAthDot11RxTooShort,'ligoAthDot11RxWrongBssid':ligoAthDot11RxWrongBssid,'ligoAthDot11RxDup':ligoAthDot11RxDup,'ligoAthDot11RxWrongDirection':ligoAthDot11RxWrongDirection,'ligoAthDot11RxMcastEcho':ligoAthDot11RxMcastEcho,'ligoAthDot11RxNotAssoc':ligoAthDot11RxNotAssoc,'ligoAthDot11RxNoPrivacy':ligoAthDot11RxNoPrivacy,'ligoAthDot11RxUnencrypted':ligoAthDot11RxUnencrypted,'ligoAthDot11RxWepFail':ligoAthDot11RxWepFail,'ligoAthDot11RxDecapFail':ligoAthDot11RxDecapFail,'ligoAthDot11RxDiscardMgt':ligoAthDot11RxDiscardMgt,'ligoAthDot11RxDiscardCtrl':ligoAthDot11RxDiscardCtrl,'ligoAthDot11RxBeaconFrames':ligoAthDot11RxBeaconFrames,'ligoAthDot11RxRateSetTrunc':ligoAthDot11RxRateSetTrunc,'ligoAthDot11RxReqElemMissing':ligoAthDot11RxReqElemMissing,'ligoAthDot11RxElementTooBig':ligoAthDot11RxElementTooBig,'ligoAthDot11RxElementTooSmall':ligoAthDot11RxElementTooSmall,'ligoAthDot11RxElementUnknown':ligoAthDot11RxElementUnknown,'ligoAthDot11RxInvalidChannel':ligoAthDot11RxInvalidChannel,'ligoAthDot11RxChannelMismatch':ligoAthDot11RxChannelMismatch,'ligoAthDot11RxNodesAllocated':ligoAthDot11RxNodesAllocated,'ligoAthDot11RxSsidMismatch':ligoAthDot11RxSsidMismatch,'ligoAthDot11RxUnsupportedAuthAlg':ligoAthDot11RxUnsupportedAuthAlg,'ligoAthDot11RxAuthFail':ligoAthDot11RxAuthFail,'ligoAthDot11RxTkipCtrm':ligoAthDot11RxTkipCtrm,'ligoAthDot11RxAssocWrongBssid':ligoAthDot11RxAssocWrongBssid,'ligoAthDot11RxAssocNotAuth':ligoAthDot11RxAssocNotAuth,'ligoAthDot11RxAssocCapMismatch':ligoAthDot11RxAssocCapMismatch,'ligoAthDot11RxAssocNoRateMatch':ligoAthDot11RxAssocNoRateMatch,'ligoAthDot11RxAssocBadWpaIe':ligoAthDot11RxAssocBadWpaIe,'ligoAthDot11RxDeauth':ligoAthDot11RxDeauth,'ligoAthDot11RxDisassoc':ligoAthDot11RxDisassoc,'ligoAthDot11RxUnknownSubtype':ligoAthDot11RxUnknownSubtype,'ligoAthDot11RxNoBuffer':ligoAthDot11RxNoBuffer,'ligoAthDot11RxDecryptCrcError':ligoAthDot11RxDecryptCrcError,'ligoAthDot11RxMgmtInAhdocDemo':ligoAthDot11RxMgmtInAhdocDemo,'ligoAthDot11RxBadAuthRequest':ligoAthDot11RxBadAuthRequest,'ligoAthDot11RxPortUnauth':ligoAthDot11RxPortUnauth,'ligoAthDot11RxBadKeyId':ligoAthDot11RxBadKeyId,'ligoAthDot11RxCcmpBadSeqNum':ligoAthDot11RxCcmpBadSeqNum,'ligoAthDot11RxCcmpBadFormat':ligoAthDot11RxCcmpBadFormat,'ligoAthDot11RxCcmpMicCheck':ligoAthDot11RxCcmpMicCheck,'ligoAthDot11RxTkipBadSeqNum':ligoAthDot11RxTkipBadSeqNum,'ligoAthDot11RxTkipBadFormat':ligoAthDot11RxTkipBadFormat,'ligoAthDot11RxTkipMicCheck':ligoAthDot11RxTkipMicCheck,'ligoAthDot11RxTkipIcvCheck':ligoAthDot11RxTkipIcvCheck,'ligoAthDot11RxBadCipherKeyType':ligoAthDot11RxBadCipherKeyType,'ligoAthDot11RxCipherKeyNotSet':ligoAthDot11RxCipherKeyNotSet,'ligoAthDot11RxAclPolicy':ligoAthDot11RxAclPolicy,'ligoAthDot11RxFastFrames':ligoAthDot11RxFastFrames,'ligoAthDot11RxFfBadTunnelHdr':ligoAthDot11RxFfBadTunnelHdr,'ligoAthDot11TxNoBuffer':ligoAthDot11TxNoBuffer,'ligoAthDot11TxNoNode':ligoAthDot11TxNoNode,'ligoAthDot11TxBadMgtFrames':ligoAthDot11TxBadMgtFrames,'ligoAthDot11TxBadCipherKeyType':ligoAthDot11TxBadCipherKeyType,'ligoAthDot11TxNoDefKey':ligoAthDot11TxNoDefKey,'ligoAthDot11TxNoCryptoHeadroom':ligoAthDot11TxNoCryptoHeadroom,'ligoAthDot11TxGoodFastFrames':ligoAthDot11TxGoodFastFrames,'ligoAthDot11TxBadFastFrames':ligoAthDot11TxBadFastFrames,'ligoAthDot11ActiveScans':ligoAthDot11ActiveScans,'ligoAthDot11PassiveScans':ligoAthDot11PassiveScans,'ligoAthDot11NodesTimeout':ligoAthDot11NodesTimeout,'ligoAthDot11CryptoCipherMalloc':ligoAthDot11CryptoCipherMalloc,'ligoAthDot11CryptoSwTkip':ligoAthDot11CryptoSwTkip,'ligoAthDot11CryptoTkipSwMicEnc':ligoAthDot11CryptoTkipSwMicEnc,'ligoAthDot11CryptoTkipSwMicDec':ligoAthDot11CryptoTkipSwMicDec,'ligoAthDot11CryptoTkipCtrm':ligoAthDot11CryptoTkipCtrm,'ligoAthDot11CryptoSwCcmp':ligoAthDot11CryptoSwCcmp,'ligoAthDot11CryptoSwWep':ligoAthDot11CryptoSwWep,'ligoAthDot11CryptoCipherRej':ligoAthDot11CryptoCipherRej,'ligoAthDot11CryptoNoKey':ligoAthDot11CryptoNoKey,'ligoAthDot11CryptoDelKey':ligoAthDot11CryptoDelKey,'ligoAthDot11CryptoBadCipher':ligoAthDot11CryptoBadCipher,'ligoAthDot11CryptoNoCipher':ligoAthDot11CryptoNoCipher,'ligoAthDot11CryptoAttachFail':ligoAthDot11CryptoAttachFail,'ligoAthDot11CryptoSwFallback':ligoAthDot11CryptoSwFallback,'ligoAthDot11CryptoKeyFail':ligoAthDot11CryptoKeyFail,'ligoAthDot11SnoopMcastPass':ligoAthDot11SnoopMcastPass,'ligoAthDot11SnoopMcastDrop':ligoAthDot11SnoopMcastDrop,'ligoAthPeerStatsTable':ligoAthPeerStatsTable,'ligoAthPeerStatsEntry':ligoAthPeerStatsEntry,_F:ligoAthPeerIndex,'ligoAthPeerMacAddr':ligoAthPeerMacAddr,'ligoAthPeerRxData':ligoAthPeerRxData,'ligoAthPeerRxMgmt':ligoAthPeerRxMgmt,'ligoAthPeerRxCtrl':ligoAthPeerRxCtrl,'ligoAthPeerRxBeacons':ligoAthPeerRxBeacons,'ligoAthPeerRxProbeResponse':ligoAthPeerRxProbeResponse,'ligoAthPeerRxUcast':ligoAthPeerRxUcast,'ligoAthPeerRxMcast':ligoAthPeerRxMcast,'ligoAthPeerRxBytes':ligoAthPeerRxBytes,'ligoAthPeerRxDup':ligoAthPeerRxDup,'ligoAthPeerRxNoPrivacy':ligoAthPeerRxNoPrivacy,'ligoAthPeerRxWepFail':ligoAthPeerRxWepFail,'ligoAthPeerRxDemicFail':ligoAthPeerRxDemicFail,'ligoAthPeerRxDecapFail':ligoAthPeerRxDecapFail,'ligoAthPeerRxDefragFail':ligoAthPeerRxDefragFail,'ligoAthPeerRxDissasoc':ligoAthPeerRxDissasoc,'ligoAthPeerRxDeauth':ligoAthPeerRxDeauth,'ligoAthPeerRxDecryptCrc':ligoAthPeerRxDecryptCrc,'ligoAthPeerRxUnauth':ligoAthPeerRxUnauth,'ligoAthPeerRxUnencrypted':ligoAthPeerRxUnencrypted,'ligoAthPeerTxData':ligoAthPeerTxData,'ligoAthPeerTxMgmt':ligoAthPeerTxMgmt,'ligoAthPeerTxProbeReq':ligoAthPeerTxProbeReq,'ligoAthPeerTxUcast':ligoAthPeerTxUcast,'ligoAthPeerTxMcast':ligoAthPeerTxMcast,'ligoAthPeerTxBytes':ligoAthPeerTxBytes,'ligoAthPeerTxNoVlanTag':ligoAthPeerTxNoVlanTag,'ligoAthPeerTxVlanMismatch':ligoAthPeerTxVlanMismatch,'ligoAthPeerTxUapsd':ligoAthPeerTxUapsd,'ligoAthPeerUapsdTriggers':ligoAthPeerUapsdTriggers,'ligoAthPeerTxEospLost':ligoAthPeerTxEospLost,'ligoAthPeerTxAssoc':ligoAthPeerTxAssoc,'ligoAthPeerTxAssocFail':ligoAthPeerTxAssocFail,'ligoAthPeerTxAuth':ligoAthPeerTxAuth,'ligoAthPeerTxAuthFail':ligoAthPeerTxAuthFail,'ligoAthPeerTxDeauth':ligoAthPeerTxDeauth,'ligoAthPeerTxDeauthCode':ligoAthPeerTxDeauthCode,'ligoAthPeerTxDisassoc':ligoAthPeerTxDisassoc,'ligoAthPeerTxDisassocCode':ligoAthPeerTxDisassocCode,'ligoAthPeerPsqDrops':ligoAthPeerPsqDrops,'ligoAthPeerMcastSnoop':ligoAthPeerMcastSnoop})