_M='sfpsPacketQPriorityQ'
_L='sfpsPacketSizeSize'
_K='sfpsPacketSizeSwitchInstance'
_J='sfpsPacketListSize'
_I='sfpsPacketListPacketType'
_H='sfpsPacketMgrPacketType'
_G='sfpsPacketMgrSwitchID'
_F='other'
_E='read-write'
_D='Integer32'
_C='CTRON-SFPS-PKTMGR-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sfpsCSPPacket,sfpsPktDispatchStats,sfpsSwitchSfpsPacket=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','sfpsCSPPacket','sfpsPktDispatchStats','sfpsSwitchSfpsPacket')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class SfpsSwitchInstance(Integer32):0
class HexInteger(Integer32):0
_SfpsPacketMgrTable_Object=MibTable
sfpsPacketMgrTable=_SfpsPacketMgrTable_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,1))
if mibBuilder.loadTexts:sfpsPacketMgrTable.setStatus(_A)
_SfpsPacketMgrEntry_Object=MibTableRow
sfpsPacketMgrEntry=_SfpsPacketMgrEntry_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,1,1))
sfpsPacketMgrEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:sfpsPacketMgrEntry.setStatus(_A)
_SfpsPacketMgrSwitchID_Type=Integer32
_SfpsPacketMgrSwitchID_Object=MibTableColumn
sfpsPacketMgrSwitchID=_SfpsPacketMgrSwitchID_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,1,1,1),_SfpsPacketMgrSwitchID_Type())
sfpsPacketMgrSwitchID.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketMgrSwitchID.setStatus(_A)
_SfpsPacketMgrPacketType_Type=HexInteger
_SfpsPacketMgrPacketType_Object=MibTableColumn
sfpsPacketMgrPacketType=_SfpsPacketMgrPacketType_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,1,1,2),_SfpsPacketMgrPacketType_Type())
sfpsPacketMgrPacketType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketMgrPacketType.setStatus(_A)
_SfpsPacketMgrTotalPackets_Type=Integer32
_SfpsPacketMgrTotalPackets_Object=MibTableColumn
sfpsPacketMgrTotalPackets=_SfpsPacketMgrTotalPackets_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,1,1,3),_SfpsPacketMgrTotalPackets_Type())
sfpsPacketMgrTotalPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketMgrTotalPackets.setStatus(_A)
_SfpsPacketMgrPktsUsed_Type=Integer32
_SfpsPacketMgrPktsUsed_Object=MibTableColumn
sfpsPacketMgrPktsUsed=_SfpsPacketMgrPktsUsed_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,1,1,4),_SfpsPacketMgrPktsUsed_Type())
sfpsPacketMgrPktsUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketMgrPktsUsed.setStatus(_A)
_SfpsPacketMgrPktsAvailable_Type=Integer32
_SfpsPacketMgrPktsAvailable_Object=MibTableColumn
sfpsPacketMgrPktsAvailable=_SfpsPacketMgrPktsAvailable_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,1,1,5),_SfpsPacketMgrPktsAvailable_Type())
sfpsPacketMgrPktsAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketMgrPktsAvailable.setStatus(_A)
_SfpsPacketMgrPktsInUse_Type=Integer32
_SfpsPacketMgrPktsInUse_Object=MibTableColumn
sfpsPacketMgrPktsInUse=_SfpsPacketMgrPktsInUse_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,1,1,6),_SfpsPacketMgrPktsInUse_Type())
sfpsPacketMgrPktsInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketMgrPktsInUse.setStatus(_A)
_SfpsPacketMgrNotFound_Type=Integer32
_SfpsPacketMgrNotFound_Object=MibTableColumn
sfpsPacketMgrNotFound=_SfpsPacketMgrNotFound_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,1,1,8),_SfpsPacketMgrNotFound_Type())
sfpsPacketMgrNotFound.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketMgrNotFound.setStatus(_A)
_SfpsPacketMgrTooLarge_Type=Integer32
_SfpsPacketMgrTooLarge_Object=MibTableColumn
sfpsPacketMgrTooLarge=_SfpsPacketMgrTooLarge_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,1,1,9),_SfpsPacketMgrTooLarge_Type())
sfpsPacketMgrTooLarge.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketMgrTooLarge.setStatus(_A)
_SfpsPacketMgrToCreate_Type=Integer32
_SfpsPacketMgrToCreate_Object=MibTableColumn
sfpsPacketMgrToCreate=_SfpsPacketMgrToCreate_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,1,1,10),_SfpsPacketMgrToCreate_Type())
sfpsPacketMgrToCreate.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsPacketMgrToCreate.setStatus(_A)
class _SfpsPacketMgrReInit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('reinit',2)))
_SfpsPacketMgrReInit_Type.__name__=_D
_SfpsPacketMgrReInit_Object=MibTableColumn
sfpsPacketMgrReInit=_SfpsPacketMgrReInit_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,1,1,11),_SfpsPacketMgrReInit_Type())
sfpsPacketMgrReInit.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsPacketMgrReInit.setStatus(_A)
_SfpsPacketListTable_Object=MibTable
sfpsPacketListTable=_SfpsPacketListTable_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,2))
if mibBuilder.loadTexts:sfpsPacketListTable.setStatus(_A)
_SfpsPacketListEntry_Object=MibTableRow
sfpsPacketListEntry=_SfpsPacketListEntry_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,2,1))
sfpsPacketListEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:sfpsPacketListEntry.setStatus(_A)
_SfpsPacketListPacketType_Type=HexInteger
_SfpsPacketListPacketType_Object=MibTableColumn
sfpsPacketListPacketType=_SfpsPacketListPacketType_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,2,1,1),_SfpsPacketListPacketType_Type())
sfpsPacketListPacketType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketListPacketType.setStatus(_A)
_SfpsPacketListSize_Type=Integer32
_SfpsPacketListSize_Object=MibTableColumn
sfpsPacketListSize=_SfpsPacketListSize_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,2,1,2),_SfpsPacketListSize_Type())
sfpsPacketListSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketListSize.setStatus(_A)
_SfpsPacketListTotalPackets_Type=Integer32
_SfpsPacketListTotalPackets_Object=MibTableColumn
sfpsPacketListTotalPackets=_SfpsPacketListTotalPackets_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,2,1,3),_SfpsPacketListTotalPackets_Type())
sfpsPacketListTotalPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketListTotalPackets.setStatus(_A)
_SfpsPacketListPktsUsed_Type=Integer32
_SfpsPacketListPktsUsed_Object=MibTableColumn
sfpsPacketListPktsUsed=_SfpsPacketListPktsUsed_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,2,1,4),_SfpsPacketListPktsUsed_Type())
sfpsPacketListPktsUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketListPktsUsed.setStatus(_A)
_SfpsPacketListPktsLeft_Type=Integer32
_SfpsPacketListPktsLeft_Object=MibTableColumn
sfpsPacketListPktsLeft=_SfpsPacketListPktsLeft_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,2,1,5),_SfpsPacketListPktsLeft_Type())
sfpsPacketListPktsLeft.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketListPktsLeft.setStatus(_A)
_SfpsPacketListPktsInUse_Type=Integer32
_SfpsPacketListPktsInUse_Object=MibTableColumn
sfpsPacketListPktsInUse=_SfpsPacketListPktsInUse_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,2,1,6),_SfpsPacketListPktsInUse_Type())
sfpsPacketListPktsInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketListPktsInUse.setStatus(_A)
_SfpsPacketListLowWater_Type=Integer32
_SfpsPacketListLowWater_Object=MibTableColumn
sfpsPacketListLowWater=_SfpsPacketListLowWater_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,2,1,7),_SfpsPacketListLowWater_Type())
sfpsPacketListLowWater.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketListLowWater.setStatus(_A)
_SfpsPacketListNotFound_Type=Integer32
_SfpsPacketListNotFound_Object=MibTableColumn
sfpsPacketListNotFound=_SfpsPacketListNotFound_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,2,1,8),_SfpsPacketListNotFound_Type())
sfpsPacketListNotFound.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketListNotFound.setStatus(_A)
class _SfpsPacketListStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('enabled',2),('disabled',3)))
_SfpsPacketListStatus_Type.__name__=_D
_SfpsPacketListStatus_Object=MibTableColumn
sfpsPacketListStatus=_SfpsPacketListStatus_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,2,1,9),_SfpsPacketListStatus_Type())
sfpsPacketListStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketListStatus.setStatus(_A)
_SfpsPacketSizeTable_Object=MibTable
sfpsPacketSizeTable=_SfpsPacketSizeTable_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,3))
if mibBuilder.loadTexts:sfpsPacketSizeTable.setStatus(_A)
_SfpsPacketSizeEntry_Object=MibTableRow
sfpsPacketSizeEntry=_SfpsPacketSizeEntry_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,3,1))
sfpsPacketSizeEntry.setIndexNames((0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:sfpsPacketSizeEntry.setStatus(_A)
_SfpsPacketSizeSwitchInstance_Type=SfpsSwitchInstance
_SfpsPacketSizeSwitchInstance_Object=MibTableColumn
sfpsPacketSizeSwitchInstance=_SfpsPacketSizeSwitchInstance_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,3,1,1),_SfpsPacketSizeSwitchInstance_Type())
sfpsPacketSizeSwitchInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketSizeSwitchInstance.setStatus(_A)
_SfpsPacketSizeSize_Type=Integer32
_SfpsPacketSizeSize_Object=MibTableColumn
sfpsPacketSizeSize=_SfpsPacketSizeSize_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,3,1,2),_SfpsPacketSizeSize_Type())
sfpsPacketSizeSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketSizeSize.setStatus(_A)
_SfpsPacketSizePktsUsed_Type=Integer32
_SfpsPacketSizePktsUsed_Object=MibTableColumn
sfpsPacketSizePktsUsed=_SfpsPacketSizePktsUsed_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,3,1,3),_SfpsPacketSizePktsUsed_Type())
sfpsPacketSizePktsUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketSizePktsUsed.setStatus(_A)
_SfpsPacketSizeNotFound_Type=Integer32
_SfpsPacketSizeNotFound_Object=MibTableColumn
sfpsPacketSizeNotFound=_SfpsPacketSizeNotFound_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,3,1,4),_SfpsPacketSizeNotFound_Type())
sfpsPacketSizeNotFound.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketSizeNotFound.setStatus(_A)
_SfpsPacketQTable_Object=MibTable
sfpsPacketQTable=_SfpsPacketQTable_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,4))
if mibBuilder.loadTexts:sfpsPacketQTable.setStatus(_A)
_SfpsPacketQEntry_Object=MibTableRow
sfpsPacketQEntry=_SfpsPacketQEntry_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,4,1))
sfpsPacketQEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:sfpsPacketQEntry.setStatus(_A)
class _SfpsPacketQPriorityQ_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('low',1),('medium',2),('high',3)))
_SfpsPacketQPriorityQ_Type.__name__=_D
_SfpsPacketQPriorityQ_Object=MibTableColumn
sfpsPacketQPriorityQ=_SfpsPacketQPriorityQ_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,4,1,1),_SfpsPacketQPriorityQ_Type())
sfpsPacketQPriorityQ.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketQPriorityQ.setStatus(_A)
_SfpsPacketQTotalPackets_Type=Integer32
_SfpsPacketQTotalPackets_Object=MibTableColumn
sfpsPacketQTotalPackets=_SfpsPacketQTotalPackets_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,4,1,2),_SfpsPacketQTotalPackets_Type())
sfpsPacketQTotalPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketQTotalPackets.setStatus(_A)
_SfpsPacketQCurrent_Type=Integer32
_SfpsPacketQCurrent_Object=MibTableColumn
sfpsPacketQCurrent=_SfpsPacketQCurrent_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,4,1,3),_SfpsPacketQCurrent_Type())
sfpsPacketQCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketQCurrent.setStatus(_A)
_SfpsPacketQHighWater_Type=Integer32
_SfpsPacketQHighWater_Object=MibTableColumn
sfpsPacketQHighWater=_SfpsPacketQHighWater_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,4,1,4),_SfpsPacketQHighWater_Type())
sfpsPacketQHighWater.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPacketQHighWater.setStatus(_A)
class _SfpsPktDispatchStatsVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('resetAllStats',2)))
_SfpsPktDispatchStatsVerb_Type.__name__=_D
_SfpsPktDispatchStatsVerb_Object=MibScalar
sfpsPktDispatchStatsVerb=_SfpsPktDispatchStatsVerb_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,1),_SfpsPktDispatchStatsVerb_Type())
sfpsPktDispatchStatsVerb.setMaxAccess(_E)
if mibBuilder.loadTexts:sfpsPktDispatchStatsVerb.setStatus(_A)
_NumHPMInvalidFrameTypeDrops_Type=Integer32
_NumHPMInvalidFrameTypeDrops_Object=MibScalar
numHPMInvalidFrameTypeDrops=_NumHPMInvalidFrameTypeDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,2),_NumHPMInvalidFrameTypeDrops_Type())
numHPMInvalidFrameTypeDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numHPMInvalidFrameTypeDrops.setStatus(_A)
_NumHPMFilterMgtPortDrops_Type=Integer32
_NumHPMFilterMgtPortDrops_Object=MibScalar
numHPMFilterMgtPortDrops=_NumHPMFilterMgtPortDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,3),_NumHPMFilterMgtPortDrops_Type())
numHPMFilterMgtPortDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numHPMFilterMgtPortDrops.setStatus(_A)
_NumHPMPhysToLogPortDrops_Type=Integer32
_NumHPMPhysToLogPortDrops_Object=MibScalar
numHPMPhysToLogPortDrops=_NumHPMPhysToLogPortDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,4),_NumHPMPhysToLogPortDrops_Type())
numHPMPhysToLogPortDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numHPMPhysToLogPortDrops.setStatus(_A)
_NumHPMNullSFPSPktDrops_Type=Integer32
_NumHPMNullSFPSPktDrops_Object=MibScalar
numHPMNullSFPSPktDrops=_NumHPMNullSFPSPktDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,5),_NumHPMNullSFPSPktDrops_Type())
numHPMNullSFPSPktDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numHPMNullSFPSPktDrops.setStatus(_A)
_NumHPM81fdThrottleDrops_Type=Integer32
_NumHPM81fdThrottleDrops_Object=MibScalar
numHPM81fdThrottleDrops=_NumHPM81fdThrottleDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,6),_NumHPM81fdThrottleDrops_Type())
numHPM81fdThrottleDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numHPM81fdThrottleDrops.setStatus(_A)
_NumHPM81ffThrottleDrops_Type=Integer32
_NumHPM81ffThrottleDrops_Object=MibScalar
numHPM81ffThrottleDrops=_NumHPM81ffThrottleDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,7),_NumHPM81ffThrottleDrops_Type())
numHPM81ffThrottleDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numHPM81ffThrottleDrops.setStatus(_A)
_NumHPMPhysStandbyMaskDrops_Type=Integer32
_NumHPMPhysStandbyMaskDrops_Object=MibScalar
numHPMPhysStandbyMaskDrops=_NumHPMPhysStandbyMaskDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,8),_NumHPMPhysStandbyMaskDrops_Type())
numHPMPhysStandbyMaskDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numHPMPhysStandbyMaskDrops.setStatus(_A)
_NumBSInvSrcPortDrops_Type=Integer32
_NumBSInvSrcPortDrops_Object=MibScalar
numBSInvSrcPortDrops=_NumBSInvSrcPortDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,9),_NumBSInvSrcPortDrops_Type())
numBSInvSrcPortDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numBSInvSrcPortDrops.setStatus(_A)
_NumBSSourceBlockDrops_Type=Integer32
_NumBSSourceBlockDrops_Object=MibScalar
numBSSourceBlockDrops=_NumBSSourceBlockDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,10),_NumBSSourceBlockDrops_Type())
numBSSourceBlockDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numBSSourceBlockDrops.setStatus(_A)
_NumBSViolationDrops_Type=Integer32
_NumBSViolationDrops_Object=MibScalar
numBSViolationDrops=_NumBSViolationDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,11),_NumBSViolationDrops_Type())
numBSViolationDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numBSViolationDrops.setStatus(_A)
_NumBSUnknownPortDrops_Type=Integer32
_NumBSUnknownPortDrops_Object=MibScalar
numBSUnknownPortDrops=_NumBSUnknownPortDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,12),_NumBSUnknownPortDrops_Type())
numBSUnknownPortDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numBSUnknownPortDrops.setStatus(_A)
_NumBSStandbyPortDrops_Type=Integer32
_NumBSStandbyPortDrops_Object=MibScalar
numBSStandbyPortDrops=_NumBSStandbyPortDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,13),_NumBSStandbyPortDrops_Type())
numBSStandbyPortDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numBSStandbyPortDrops.setStatus(_A)
_NumBSFabricNghbrPortDrops_Type=Integer32
_NumBSFabricNghbrPortDrops_Object=MibScalar
numBSFabricNghbrPortDrops=_NumBSFabricNghbrPortDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,14),_NumBSFabricNghbrPortDrops_Type())
numBSFabricNghbrPortDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numBSFabricNghbrPortDrops.setStatus(_A)
_NumBSGoingToAccessPortDrops_Type=Integer32
_NumBSGoingToAccessPortDrops_Object=MibScalar
numBSGoingToAccessPortDrops=_NumBSGoingToAccessPortDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,15),_NumBSGoingToAccessPortDrops_Type())
numBSGoingToAccessPortDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numBSGoingToAccessPortDrops.setStatus(_A)
_NumBSInvPortTypeDrops_Type=Integer32
_NumBSInvPortTypeDrops_Object=MibScalar
numBSInvPortTypeDrops=_NumBSInvPortTypeDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,16),_NumBSInvPortTypeDrops_Type())
numBSInvPortTypeDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numBSInvPortTypeDrops.setStatus(_A)
_NumBSNullCallDrops_Type=Integer32
_NumBSNullCallDrops_Object=MibScalar
numBSNullCallDrops=_NumBSNullCallDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,17),_NumBSNullCallDrops_Type())
numBSNullCallDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numBSNullCallDrops.setStatus(_A)
_NumBSNullBottomCPDrops_Type=Integer32
_NumBSNullBottomCPDrops_Object=MibScalar
numBSNullBottomCPDrops=_NumBSNullBottomCPDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,18),_NumBSNullBottomCPDrops_Type())
numBSNullBottomCPDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numBSNullBottomCPDrops.setStatus(_A)
_NumBSInvCSPTypeDrops_Type=Integer32
_NumBSInvCSPTypeDrops_Object=MibScalar
numBSInvCSPTypeDrops=_NumBSInvCSPTypeDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,19),_NumBSInvCSPTypeDrops_Type())
numBSInvCSPTypeDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numBSInvCSPTypeDrops.setStatus(_A)
_NumBSNonHello81fdDrops_Type=Integer32
_NumBSNonHello81fdDrops_Object=MibScalar
numBSNonHello81fdDrops=_NumBSNonHello81fdDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,20),_NumBSNonHello81fdDrops_Type())
numBSNonHello81fdDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numBSNonHello81fdDrops.setStatus(_A)
_NumBSCSPCtrlDisableDrops_Type=Integer32
_NumBSCSPCtrlDisableDrops_Object=MibScalar
numBSCSPCtrlDisableDrops=_NumBSCSPCtrlDisableDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,21),_NumBSCSPCtrlDisableDrops_Type())
numBSCSPCtrlDisableDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numBSCSPCtrlDisableDrops.setStatus(_A)
_NumBSCSPCtrlIndexDrops_Type=Integer32
_NumBSCSPCtrlIndexDrops_Object=MibScalar
numBSCSPCtrlIndexDrops=_NumBSCSPCtrlIndexDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,22),_NumBSCSPCtrlIndexDrops_Type())
numBSCSPCtrlIndexDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numBSCSPCtrlIndexDrops.setStatus(_A)
_NumBCPNullCallDrops_Type=Integer32
_NumBCPNullCallDrops_Object=MibScalar
numBCPNullCallDrops=_NumBCPNullCallDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,23),_NumBCPNullCallDrops_Type())
numBCPNullCallDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numBCPNullCallDrops.setStatus(_A)
_NumBCPCPFaultedDrops_Type=Integer32
_NumBCPCPFaultedDrops_Object=MibScalar
numBCPCPFaultedDrops=_NumBCPCPFaultedDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,24),_NumBCPCPFaultedDrops_Type())
numBCPCPFaultedDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numBCPCPFaultedDrops.setStatus(_A)
_NumBCPGleanFailDrops_Type=Integer32
_NumBCPGleanFailDrops_Object=MibScalar
numBCPGleanFailDrops=_NumBCPGleanFailDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,25),_NumBCPGleanFailDrops_Type())
numBCPGleanFailDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numBCPGleanFailDrops.setStatus(_A)
_NumBCPCPHaltedDrops_Type=Integer32
_NumBCPCPHaltedDrops_Object=MibScalar
numBCPCPHaltedDrops=_NumBCPCPHaltedDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,26),_NumBCPCPHaltedDrops_Type())
numBCPCPHaltedDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numBCPCPHaltedDrops.setStatus(_A)
_NumBCPSwitchedBCADrops_Type=Integer32
_NumBCPSwitchedBCADrops_Object=MibScalar
numBCPSwitchedBCADrops=_NumBCPSwitchedBCADrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,27),_NumBCPSwitchedBCADrops_Type())
numBCPSwitchedBCADrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numBCPSwitchedBCADrops.setStatus(_A)
_NumBCPCallNotAcceptedDrops_Type=Integer32
_NumBCPCallNotAcceptedDrops_Object=MibScalar
numBCPCallNotAcceptedDrops=_NumBCPCallNotAcceptedDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,28),_NumBCPCallNotAcceptedDrops_Type())
numBCPCallNotAcceptedDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numBCPCallNotAcceptedDrops.setStatus(_A)
_NumHPM81fdNullPktDrops_Type=Integer32
_NumHPM81fdNullPktDrops_Object=MibScalar
numHPM81fdNullPktDrops=_NumHPM81fdNullPktDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,29),_NumHPM81fdNullPktDrops_Type())
numHPM81fdNullPktDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numHPM81fdNullPktDrops.setStatus(_A)
_NumHPM81fdHelloNullPktDrops_Type=Integer32
_NumHPM81fdHelloNullPktDrops_Object=MibScalar
numHPM81fdHelloNullPktDrops=_NumHPM81fdHelloNullPktDrops_Object((1,3,6,1,4,1,52,4,2,4,2,1,7,5,30),_NumHPM81fdHelloNullPktDrops_Type())
numHPM81fdHelloNullPktDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:numHPM81fdHelloNullPktDrops.setStatus(_A)
_SfpsCSPPacketStatsPacketsSentBad_Type=Integer32
_SfpsCSPPacketStatsPacketsSentBad_Object=MibScalar
sfpsCSPPacketStatsPacketsSentBad=_SfpsCSPPacketStatsPacketsSentBad_Object((1,3,6,1,4,1,52,4,2,4,2,1,10,1),_SfpsCSPPacketStatsPacketsSentBad_Type())
sfpsCSPPacketStatsPacketsSentBad.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCSPPacketStatsPacketsSentBad.setStatus(_A)
_SfpsCSPPacketStatsPacketsSentGood_Type=Integer32
_SfpsCSPPacketStatsPacketsSentGood_Object=MibScalar
sfpsCSPPacketStatsPacketsSentGood=_SfpsCSPPacketStatsPacketsSentGood_Object((1,3,6,1,4,1,52,4,2,4,2,1,10,2),_SfpsCSPPacketStatsPacketsSentGood_Type())
sfpsCSPPacketStatsPacketsSentGood.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCSPPacketStatsPacketsSentGood.setStatus(_A)
_SfpsCSPPacketStatsPacketsReceivedBad_Type=Integer32
_SfpsCSPPacketStatsPacketsReceivedBad_Object=MibScalar
sfpsCSPPacketStatsPacketsReceivedBad=_SfpsCSPPacketStatsPacketsReceivedBad_Object((1,3,6,1,4,1,52,4,2,4,2,1,10,3),_SfpsCSPPacketStatsPacketsReceivedBad_Type())
sfpsCSPPacketStatsPacketsReceivedBad.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCSPPacketStatsPacketsReceivedBad.setStatus(_A)
_SfpsCSPPacketStatsPacketsReceivedGood_Type=Integer32
_SfpsCSPPacketStatsPacketsReceivedGood_Object=MibScalar
sfpsCSPPacketStatsPacketsReceivedGood=_SfpsCSPPacketStatsPacketsReceivedGood_Object((1,3,6,1,4,1,52,4,2,4,2,1,10,4),_SfpsCSPPacketStatsPacketsReceivedGood_Type())
sfpsCSPPacketStatsPacketsReceivedGood.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsCSPPacketStatsPacketsReceivedGood.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'SfpsSwitchInstance':SfpsSwitchInstance,'HexInteger':HexInteger,'sfpsPacketMgrTable':sfpsPacketMgrTable,'sfpsPacketMgrEntry':sfpsPacketMgrEntry,_G:sfpsPacketMgrSwitchID,_H:sfpsPacketMgrPacketType,'sfpsPacketMgrTotalPackets':sfpsPacketMgrTotalPackets,'sfpsPacketMgrPktsUsed':sfpsPacketMgrPktsUsed,'sfpsPacketMgrPktsAvailable':sfpsPacketMgrPktsAvailable,'sfpsPacketMgrPktsInUse':sfpsPacketMgrPktsInUse,'sfpsPacketMgrNotFound':sfpsPacketMgrNotFound,'sfpsPacketMgrTooLarge':sfpsPacketMgrTooLarge,'sfpsPacketMgrToCreate':sfpsPacketMgrToCreate,'sfpsPacketMgrReInit':sfpsPacketMgrReInit,'sfpsPacketListTable':sfpsPacketListTable,'sfpsPacketListEntry':sfpsPacketListEntry,_I:sfpsPacketListPacketType,_J:sfpsPacketListSize,'sfpsPacketListTotalPackets':sfpsPacketListTotalPackets,'sfpsPacketListPktsUsed':sfpsPacketListPktsUsed,'sfpsPacketListPktsLeft':sfpsPacketListPktsLeft,'sfpsPacketListPktsInUse':sfpsPacketListPktsInUse,'sfpsPacketListLowWater':sfpsPacketListLowWater,'sfpsPacketListNotFound':sfpsPacketListNotFound,'sfpsPacketListStatus':sfpsPacketListStatus,'sfpsPacketSizeTable':sfpsPacketSizeTable,'sfpsPacketSizeEntry':sfpsPacketSizeEntry,_K:sfpsPacketSizeSwitchInstance,_L:sfpsPacketSizeSize,'sfpsPacketSizePktsUsed':sfpsPacketSizePktsUsed,'sfpsPacketSizeNotFound':sfpsPacketSizeNotFound,'sfpsPacketQTable':sfpsPacketQTable,'sfpsPacketQEntry':sfpsPacketQEntry,_M:sfpsPacketQPriorityQ,'sfpsPacketQTotalPackets':sfpsPacketQTotalPackets,'sfpsPacketQCurrent':sfpsPacketQCurrent,'sfpsPacketQHighWater':sfpsPacketQHighWater,'sfpsPktDispatchStatsVerb':sfpsPktDispatchStatsVerb,'numHPMInvalidFrameTypeDrops':numHPMInvalidFrameTypeDrops,'numHPMFilterMgtPortDrops':numHPMFilterMgtPortDrops,'numHPMPhysToLogPortDrops':numHPMPhysToLogPortDrops,'numHPMNullSFPSPktDrops':numHPMNullSFPSPktDrops,'numHPM81fdThrottleDrops':numHPM81fdThrottleDrops,'numHPM81ffThrottleDrops':numHPM81ffThrottleDrops,'numHPMPhysStandbyMaskDrops':numHPMPhysStandbyMaskDrops,'numBSInvSrcPortDrops':numBSInvSrcPortDrops,'numBSSourceBlockDrops':numBSSourceBlockDrops,'numBSViolationDrops':numBSViolationDrops,'numBSUnknownPortDrops':numBSUnknownPortDrops,'numBSStandbyPortDrops':numBSStandbyPortDrops,'numBSFabricNghbrPortDrops':numBSFabricNghbrPortDrops,'numBSGoingToAccessPortDrops':numBSGoingToAccessPortDrops,'numBSInvPortTypeDrops':numBSInvPortTypeDrops,'numBSNullCallDrops':numBSNullCallDrops,'numBSNullBottomCPDrops':numBSNullBottomCPDrops,'numBSInvCSPTypeDrops':numBSInvCSPTypeDrops,'numBSNonHello81fdDrops':numBSNonHello81fdDrops,'numBSCSPCtrlDisableDrops':numBSCSPCtrlDisableDrops,'numBSCSPCtrlIndexDrops':numBSCSPCtrlIndexDrops,'numBCPNullCallDrops':numBCPNullCallDrops,'numBCPCPFaultedDrops':numBCPCPFaultedDrops,'numBCPGleanFailDrops':numBCPGleanFailDrops,'numBCPCPHaltedDrops':numBCPCPHaltedDrops,'numBCPSwitchedBCADrops':numBCPSwitchedBCADrops,'numBCPCallNotAcceptedDrops':numBCPCallNotAcceptedDrops,'numHPM81fdNullPktDrops':numHPM81fdNullPktDrops,'numHPM81fdHelloNullPktDrops':numHPM81fdHelloNullPktDrops,'sfpsCSPPacketStatsPacketsSentBad':sfpsCSPPacketStatsPacketsSentBad,'sfpsCSPPacketStatsPacketsSentGood':sfpsCSPPacketStatsPacketsSentGood,'sfpsCSPPacketStatsPacketsReceivedBad':sfpsCSPPacketStatsPacketsReceivedBad,'sfpsCSPPacketStatsPacketsReceivedGood':sfpsCSPPacketStatsPacketsReceivedGood})