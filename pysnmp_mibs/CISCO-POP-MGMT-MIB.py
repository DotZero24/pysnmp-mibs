_BH='cpmNotificationGroupRev1'
_BG='cpmDS1LoopbackNotifyConfigGroup'
_BF='cpmNotificationGroup'
_BE='cpmDS0UsageGroupRev1'
_BD='cpmDS0UsageGroup'
_BC='cpmDS1LoopbackNotification'
_BB='cpmCallVolAnalogCallClearedNormally'
_BA='cpmCallVolSuccISDNDigital'
_B9='cpmDS1LoopbackNotifyEnable'
_B8='cpmDS0ConfigFunction'
_B7='cpmDS0BusyoutAllow'
_B6='cpmDS0BusyoutAdminStatus'
_B5='cpmDS0OperStatus'
_B4='cpmDS0BusyoutNotifyEnable'
_B3='cpmTotalISDNSyncPPPCalls'
_B2='cpmISDNCfgBChannelAnalogCalls'
_B1='cpmISDNCfgBChannelCalls'
_B0='cpmISDNCfgBChannelsTimeInUseAnlg'
_A_='cpmISDNCfgBChannelsTimeInUse'
_Az='cpmISDNCfgActiveDChannels'
_Ay='cpmDS1OutPackets'
_Ax='cpmDS1InPackets'
_Aw='cpmDS1OutOctets'
_Av='cpmDS1InOctets'
_Au='cpmDS1CurrentBusyout'
_At='cpmDS1CurrentOutOfService'
_As='cpmDS1CurrentIdle'
_Ar='cpmDS1TotalTimeInUse'
_Aq='cpmDS1TotalCalls'
_Ap='cpmDS1TotalV120Calls'
_Ao='cpmDS1TotalV110Calls'
_An='cpmDS1TotalDigitalCalls'
_Am='cpmDS1TotalAnalogCalls'
_Al='cpmCASCfgBChanInUseForVoice'
_Ak='cpmISDNCfgBChanInUseForVoice'
_Aj='cpmTTYNumber'
_Ai='cpmLocalPhoneNumber'
_Ah='cpmRemotePhoneNumber'
_Ag='cpmEntryChannel'
_Af='cpmEntryPort'
_Ae='cpmEntrySlot'
_Ad='cpmCallDuration'
_Ac='cpmModemPort'
_Ab='cpmModemSlot'
_Aa='cpmCallType'
_AZ='cpmUserIpAddr'
_AY='cpmUserID'
_AX='cpmCallHistorySummaryRetainTimer'
_AW='cpmCallHistorySummaryTableMaxLength'
_AV='cpmActiveTTYNumber'
_AU='cpmActiveLocalPhoneNumber'
_AT='cpmActiveRemotePhoneNumber'
_AS='cpmActiveEntryChannel'
_AR='cpmActiveEntryPort'
_AQ='cpmActiveEntrySlot'
_AP='cpmActiveCallDuration'
_AO='cpmActiveModemPort'
_AN='cpmActiveModemSlot'
_AM='cpmActiveUserIpAddr'
_AL='cpmActiveCallType'
_AK='cpmActiveUserID'
_AJ='cpmModemNoResource'
_AI='cpmISDNNoResource'
_AH='cpmModemCallsClearedAbnormally'
_AG='cpmISDNCallsClearedAbnormally'
_AF='cpmModemCallsRejected'
_AE='cpmISDNCallsRejected'
_AD='cpmDS0StatusEntry'
_AC='noBusyout'
_AB='cpmCallHistorySummaryIndex'
_AA='cpmCallStartTimeIndex'
_A9='cpmCallDisconnectTimeIndex'
_A8='cpmActiveCallSummaryIndex'
_A7='cpmActiveCallStartTimeIndex'
_A6='cpmDS1UsagePortIndex'
_A5='cpmDS1UsageSlotIndex'
_A4='cpmChannelIndex'
_A3='cpmDS1PortIndex'
_A2='cpmDS1SlotIndex'
_A1='dsx1LineStatus'
_A0='dsx1LineIndex'
_z='cpmCallVolumeGroup'
_y='deprecated'
_x='cpmDS0BusyoutNotification'
_w='cpmDS0InterfaceIndex'
_v='cpmDS0BusyoutTime'
_u='cpmDS0BusyoutSource'
_t='cpmDS0BusyoutStatus'
_s='cpmSW56CfgBChannelsInUse'
_r='cpmDS1ActiveDS0sHighWaterMark'
_q='cpmDS1ActiveDS0s'
_p='cpmActiveDS0sHighWaterMark'
_o='seconds'
_n='v120'
_m='v110'
_l='digital'
_k='analog'
_j='idle'
_i='DS1-MIB'
_h='cpmSystemGroup'
_g='cpmDS1UsageGroup'
_f='cpmDS0StatusGroup'
_e='cpmV110Calls'
_d='cpmV120Calls'
_c='cpmPPPCalls'
_b='cpmActiveDS0s'
_a='cpmISDNCfgBChannelsInUse'
_Z='cpmISDNCfgBChanInUseForAnalog'
_Y='cpmAssociatedInterface'
_X='cpmOutPackets'
_W='cpmInPackets'
_V='cpmOutOctets'
_U='cpmInOctets'
_T='cpmTimeInUse'
_S='cpmCallCount'
_R='cpmL2Encapsulation'
_Q='cpmDS0CallType'
_P='cpmConfiguredType'
_O='voice'
_N='cpmDS0UsageGroupRev2'
_M='obsolete'
_L='read-write'
_K='cpmCallHistorySummaryGroup'
_J='cpmActiveCallSummaryGroup'
_I='cpmCallFailureGroup'
_H='calls'
_G='unknown'
_F='DisplayString'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-POP-MGMT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
dsx1LineIndex,dsx1LineStatus=mibBuilder.importSymbols(_i,_A0,_A1)
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention','TimeStamp','TruthValue')
ciscoPopMgmtMIB=ModuleIdentity((1,3,6,1,4,1,9,10,19))
if mibBuilder.loadTexts:ciscoPopMgmtMIB.setRevisions(('2005-12-21 00:00','2002-12-26 00:00','2000-11-29 00:00','2000-03-03 00:00','1998-02-02 00:00','1997-10-21 00:00','1997-05-01 00:00'))
_CiscoPopMgmtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoPopMgmtMIBObjects=_CiscoPopMgmtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,19,1))
_CpmDS0Usage_ObjectIdentity=ObjectIdentity
cpmDS0Usage=_CpmDS0Usage_ObjectIdentity((1,3,6,1,4,1,9,10,19,1,1))
_CpmDS0UsageTable_Object=MibTable
cpmDS0UsageTable=_CpmDS0UsageTable_Object((1,3,6,1,4,1,9,10,19,1,1,1))
if mibBuilder.loadTexts:cpmDS0UsageTable.setStatus(_B)
_CpmDS0UsageEntry_Object=MibTableRow
cpmDS0UsageEntry=_CpmDS0UsageEntry_Object((1,3,6,1,4,1,9,10,19,1,1,1,1))
cpmDS0UsageEntry.setIndexNames((0,_A,_A2),(0,_A,_A3),(0,_A,_A4))
if mibBuilder.loadTexts:cpmDS0UsageEntry.setStatus(_B)
class _CpmDS1SlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpmDS1SlotIndex_Type.__name__=_D
_CpmDS1SlotIndex_Object=MibTableColumn
cpmDS1SlotIndex=_CpmDS1SlotIndex_Object((1,3,6,1,4,1,9,10,19,1,1,1,1,1),_CpmDS1SlotIndex_Type())
cpmDS1SlotIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cpmDS1SlotIndex.setStatus(_B)
class _CpmDS1PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpmDS1PortIndex_Type.__name__=_D
_CpmDS1PortIndex_Object=MibTableColumn
cpmDS1PortIndex=_CpmDS1PortIndex_Object((1,3,6,1,4,1,9,10,19,1,1,1,1,2),_CpmDS1PortIndex_Type())
cpmDS1PortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cpmDS1PortIndex.setStatus(_B)
class _CpmChannelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpmChannelIndex_Type.__name__=_D
_CpmChannelIndex_Object=MibTableColumn
cpmChannelIndex=_CpmChannelIndex_Object((1,3,6,1,4,1,9,10,19,1,1,1,1,3),_CpmChannelIndex_Type())
cpmChannelIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cpmChannelIndex.setStatus(_B)
class _CpmConfiguredType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('isdn',2),('ct1',3),('ce1',4)))
_CpmConfiguredType_Type.__name__=_D
_CpmConfiguredType_Object=MibTableColumn
cpmConfiguredType=_CpmConfiguredType_Object((1,3,6,1,4,1,9,10,19,1,1,1,1,4),_CpmConfiguredType_Type())
cpmConfiguredType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmConfiguredType.setStatus(_B)
class _CpmDS0CallType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_j,1),(_G,2),(_k,3),(_l,4),(_m,5),(_n,6),(_O,7)))
_CpmDS0CallType_Type.__name__=_D
_CpmDS0CallType_Object=MibTableColumn
cpmDS0CallType=_CpmDS0CallType_Object((1,3,6,1,4,1,9,10,19,1,1,1,1,5),_CpmDS0CallType_Type())
cpmDS0CallType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS0CallType.setStatus(_B)
class _CpmL2Encapsulation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_j,1),(_G,2),('ppp',3),('slip',4),('arap',5),('hdlc',6),('exec',7),(_O,8)))
_CpmL2Encapsulation_Type.__name__=_D
_CpmL2Encapsulation_Object=MibTableColumn
cpmL2Encapsulation=_CpmL2Encapsulation_Object((1,3,6,1,4,1,9,10,19,1,1,1,1,6),_CpmL2Encapsulation_Type())
cpmL2Encapsulation.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmL2Encapsulation.setStatus(_B)
_CpmCallCount_Type=Counter32
_CpmCallCount_Object=MibTableColumn
cpmCallCount=_CpmCallCount_Object((1,3,6,1,4,1,9,10,19,1,1,1,1,7),_CpmCallCount_Type())
cpmCallCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmCallCount.setStatus(_B)
_CpmTimeInUse_Type=TimeTicks
_CpmTimeInUse_Object=MibTableColumn
cpmTimeInUse=_CpmTimeInUse_Object((1,3,6,1,4,1,9,10,19,1,1,1,1,8),_CpmTimeInUse_Type())
cpmTimeInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmTimeInUse.setStatus(_B)
_CpmInOctets_Type=Counter32
_CpmInOctets_Object=MibTableColumn
cpmInOctets=_CpmInOctets_Object((1,3,6,1,4,1,9,10,19,1,1,1,1,9),_CpmInOctets_Type())
cpmInOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmInOctets.setStatus(_B)
_CpmOutOctets_Type=Counter32
_CpmOutOctets_Object=MibTableColumn
cpmOutOctets=_CpmOutOctets_Object((1,3,6,1,4,1,9,10,19,1,1,1,1,10),_CpmOutOctets_Type())
cpmOutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmOutOctets.setStatus(_B)
_CpmInPackets_Type=Counter32
_CpmInPackets_Object=MibTableColumn
cpmInPackets=_CpmInPackets_Object((1,3,6,1,4,1,9,10,19,1,1,1,1,11),_CpmInPackets_Type())
cpmInPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmInPackets.setStatus(_B)
_CpmOutPackets_Type=Counter32
_CpmOutPackets_Object=MibTableColumn
cpmOutPackets=_CpmOutPackets_Object((1,3,6,1,4,1,9,10,19,1,1,1,1,12),_CpmOutPackets_Type())
cpmOutPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmOutPackets.setStatus(_B)
_CpmAssociatedInterface_Type=InterfaceIndexOrZero
_CpmAssociatedInterface_Object=MibTableColumn
cpmAssociatedInterface=_CpmAssociatedInterface_Object((1,3,6,1,4,1,9,10,19,1,1,1,1,13),_CpmAssociatedInterface_Type())
cpmAssociatedInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmAssociatedInterface.setStatus(_B)
_CpmISDNCfgBChanInUseForAnalog_Type=Gauge32
_CpmISDNCfgBChanInUseForAnalog_Object=MibScalar
cpmISDNCfgBChanInUseForAnalog=_CpmISDNCfgBChanInUseForAnalog_Object((1,3,6,1,4,1,9,10,19,1,1,2),_CpmISDNCfgBChanInUseForAnalog_Type())
cpmISDNCfgBChanInUseForAnalog.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmISDNCfgBChanInUseForAnalog.setStatus(_B)
_CpmISDNCfgBChannelsInUse_Type=Gauge32
_CpmISDNCfgBChannelsInUse_Object=MibScalar
cpmISDNCfgBChannelsInUse=_CpmISDNCfgBChannelsInUse_Object((1,3,6,1,4,1,9,10,19,1,1,3),_CpmISDNCfgBChannelsInUse_Type())
cpmISDNCfgBChannelsInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmISDNCfgBChannelsInUse.setStatus(_B)
_CpmActiveDS0s_Type=Gauge32
_CpmActiveDS0s_Object=MibScalar
cpmActiveDS0s=_CpmActiveDS0s_Object((1,3,6,1,4,1,9,10,19,1,1,4),_CpmActiveDS0s_Type())
cpmActiveDS0s.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmActiveDS0s.setStatus(_B)
_CpmPPPCalls_Type=Gauge32
_CpmPPPCalls_Object=MibScalar
cpmPPPCalls=_CpmPPPCalls_Object((1,3,6,1,4,1,9,10,19,1,1,5),_CpmPPPCalls_Type())
cpmPPPCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmPPPCalls.setStatus(_B)
_CpmV120Calls_Type=Gauge32
_CpmV120Calls_Object=MibScalar
cpmV120Calls=_CpmV120Calls_Object((1,3,6,1,4,1,9,10,19,1,1,6),_CpmV120Calls_Type())
cpmV120Calls.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmV120Calls.setStatus(_B)
_CpmV110Calls_Type=Gauge32
_CpmV110Calls_Object=MibScalar
cpmV110Calls=_CpmV110Calls_Object((1,3,6,1,4,1,9,10,19,1,1,7),_CpmV110Calls_Type())
cpmV110Calls.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmV110Calls.setStatus(_B)
_CpmActiveDS0sHighWaterMark_Type=Counter32
_CpmActiveDS0sHighWaterMark_Object=MibScalar
cpmActiveDS0sHighWaterMark=_CpmActiveDS0sHighWaterMark_Object((1,3,6,1,4,1,9,10,19,1,1,8),_CpmActiveDS0sHighWaterMark_Type())
cpmActiveDS0sHighWaterMark.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmActiveDS0sHighWaterMark.setStatus(_B)
_CpmDS1DS0UsageTable_Object=MibTable
cpmDS1DS0UsageTable=_CpmDS1DS0UsageTable_Object((1,3,6,1,4,1,9,10,19,1,1,9))
if mibBuilder.loadTexts:cpmDS1DS0UsageTable.setStatus(_B)
_CpmDS1DS0UsageEntry_Object=MibTableRow
cpmDS1DS0UsageEntry=_CpmDS1DS0UsageEntry_Object((1,3,6,1,4,1,9,10,19,1,1,9,1))
cpmDS1DS0UsageEntry.setIndexNames((0,_A,_A5),(0,_A,_A6))
if mibBuilder.loadTexts:cpmDS1DS0UsageEntry.setStatus(_B)
class _CpmDS1UsageSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpmDS1UsageSlotIndex_Type.__name__=_D
_CpmDS1UsageSlotIndex_Object=MibTableColumn
cpmDS1UsageSlotIndex=_CpmDS1UsageSlotIndex_Object((1,3,6,1,4,1,9,10,19,1,1,9,1,1),_CpmDS1UsageSlotIndex_Type())
cpmDS1UsageSlotIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cpmDS1UsageSlotIndex.setStatus(_B)
class _CpmDS1UsagePortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpmDS1UsagePortIndex_Type.__name__=_D
_CpmDS1UsagePortIndex_Object=MibTableColumn
cpmDS1UsagePortIndex=_CpmDS1UsagePortIndex_Object((1,3,6,1,4,1,9,10,19,1,1,9,1,2),_CpmDS1UsagePortIndex_Type())
cpmDS1UsagePortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cpmDS1UsagePortIndex.setStatus(_B)
_CpmDS1ActiveDS0s_Type=Gauge32
_CpmDS1ActiveDS0s_Object=MibTableColumn
cpmDS1ActiveDS0s=_CpmDS1ActiveDS0s_Object((1,3,6,1,4,1,9,10,19,1,1,9,1,3),_CpmDS1ActiveDS0s_Type())
cpmDS1ActiveDS0s.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS1ActiveDS0s.setStatus(_B)
_CpmDS1ActiveDS0sHighWaterMark_Type=Counter32
_CpmDS1ActiveDS0sHighWaterMark_Object=MibTableColumn
cpmDS1ActiveDS0sHighWaterMark=_CpmDS1ActiveDS0sHighWaterMark_Object((1,3,6,1,4,1,9,10,19,1,1,9,1,4),_CpmDS1ActiveDS0sHighWaterMark_Type())
cpmDS1ActiveDS0sHighWaterMark.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS1ActiveDS0sHighWaterMark.setStatus(_B)
_CpmDS1TotalAnalogCalls_Type=Counter32
_CpmDS1TotalAnalogCalls_Object=MibTableColumn
cpmDS1TotalAnalogCalls=_CpmDS1TotalAnalogCalls_Object((1,3,6,1,4,1,9,10,19,1,1,9,1,5),_CpmDS1TotalAnalogCalls_Type())
cpmDS1TotalAnalogCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS1TotalAnalogCalls.setStatus(_B)
if mibBuilder.loadTexts:cpmDS1TotalAnalogCalls.setUnits(_H)
_CpmDS1TotalDigitalCalls_Type=Counter32
_CpmDS1TotalDigitalCalls_Object=MibTableColumn
cpmDS1TotalDigitalCalls=_CpmDS1TotalDigitalCalls_Object((1,3,6,1,4,1,9,10,19,1,1,9,1,6),_CpmDS1TotalDigitalCalls_Type())
cpmDS1TotalDigitalCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS1TotalDigitalCalls.setStatus(_B)
if mibBuilder.loadTexts:cpmDS1TotalDigitalCalls.setUnits(_H)
_CpmDS1TotalV110Calls_Type=Counter32
_CpmDS1TotalV110Calls_Object=MibTableColumn
cpmDS1TotalV110Calls=_CpmDS1TotalV110Calls_Object((1,3,6,1,4,1,9,10,19,1,1,9,1,7),_CpmDS1TotalV110Calls_Type())
cpmDS1TotalV110Calls.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS1TotalV110Calls.setStatus(_B)
if mibBuilder.loadTexts:cpmDS1TotalV110Calls.setUnits(_H)
_CpmDS1TotalV120Calls_Type=Counter32
_CpmDS1TotalV120Calls_Object=MibTableColumn
cpmDS1TotalV120Calls=_CpmDS1TotalV120Calls_Object((1,3,6,1,4,1,9,10,19,1,1,9,1,8),_CpmDS1TotalV120Calls_Type())
cpmDS1TotalV120Calls.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS1TotalV120Calls.setStatus(_B)
if mibBuilder.loadTexts:cpmDS1TotalV120Calls.setUnits(_H)
_CpmDS1TotalCalls_Type=Counter32
_CpmDS1TotalCalls_Object=MibTableColumn
cpmDS1TotalCalls=_CpmDS1TotalCalls_Object((1,3,6,1,4,1,9,10,19,1,1,9,1,9),_CpmDS1TotalCalls_Type())
cpmDS1TotalCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS1TotalCalls.setStatus(_B)
if mibBuilder.loadTexts:cpmDS1TotalCalls.setUnits(_H)
_CpmDS1TotalTimeInUse_Type=Unsigned32
_CpmDS1TotalTimeInUse_Object=MibTableColumn
cpmDS1TotalTimeInUse=_CpmDS1TotalTimeInUse_Object((1,3,6,1,4,1,9,10,19,1,1,9,1,10),_CpmDS1TotalTimeInUse_Type())
cpmDS1TotalTimeInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS1TotalTimeInUse.setStatus(_B)
if mibBuilder.loadTexts:cpmDS1TotalTimeInUse.setUnits(_o)
_CpmDS1CurrentIdle_Type=Gauge32
_CpmDS1CurrentIdle_Object=MibTableColumn
cpmDS1CurrentIdle=_CpmDS1CurrentIdle_Object((1,3,6,1,4,1,9,10,19,1,1,9,1,11),_CpmDS1CurrentIdle_Type())
cpmDS1CurrentIdle.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS1CurrentIdle.setStatus(_B)
_CpmDS1CurrentOutOfService_Type=Gauge32
_CpmDS1CurrentOutOfService_Object=MibTableColumn
cpmDS1CurrentOutOfService=_CpmDS1CurrentOutOfService_Object((1,3,6,1,4,1,9,10,19,1,1,9,1,12),_CpmDS1CurrentOutOfService_Type())
cpmDS1CurrentOutOfService.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS1CurrentOutOfService.setStatus(_B)
_CpmDS1CurrentBusyout_Type=Gauge32
_CpmDS1CurrentBusyout_Object=MibTableColumn
cpmDS1CurrentBusyout=_CpmDS1CurrentBusyout_Object((1,3,6,1,4,1,9,10,19,1,1,9,1,13),_CpmDS1CurrentBusyout_Type())
cpmDS1CurrentBusyout.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS1CurrentBusyout.setStatus(_B)
_CpmDS1InOctets_Type=Counter32
_CpmDS1InOctets_Object=MibTableColumn
cpmDS1InOctets=_CpmDS1InOctets_Object((1,3,6,1,4,1,9,10,19,1,1,9,1,14),_CpmDS1InOctets_Type())
cpmDS1InOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS1InOctets.setStatus(_B)
if mibBuilder.loadTexts:cpmDS1InOctets.setUnits('octets')
_CpmDS1OutOctets_Type=Counter32
_CpmDS1OutOctets_Object=MibTableColumn
cpmDS1OutOctets=_CpmDS1OutOctets_Object((1,3,6,1,4,1,9,10,19,1,1,9,1,15),_CpmDS1OutOctets_Type())
cpmDS1OutOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS1OutOctets.setStatus(_B)
if mibBuilder.loadTexts:cpmDS1OutOctets.setUnits('octets')
_CpmDS1InPackets_Type=Counter32
_CpmDS1InPackets_Object=MibTableColumn
cpmDS1InPackets=_CpmDS1InPackets_Object((1,3,6,1,4,1,9,10,19,1,1,9,1,16),_CpmDS1InPackets_Type())
cpmDS1InPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS1InPackets.setStatus(_B)
if mibBuilder.loadTexts:cpmDS1InPackets.setUnits('packets')
_CpmDS1OutPackets_Type=Counter32
_CpmDS1OutPackets_Object=MibTableColumn
cpmDS1OutPackets=_CpmDS1OutPackets_Object((1,3,6,1,4,1,9,10,19,1,1,9,1,17),_CpmDS1OutPackets_Type())
cpmDS1OutPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS1OutPackets.setStatus(_B)
if mibBuilder.loadTexts:cpmDS1OutPackets.setUnits('packets')
_CpmSW56CfgBChannelsInUse_Type=Gauge32
_CpmSW56CfgBChannelsInUse_Object=MibScalar
cpmSW56CfgBChannelsInUse=_CpmSW56CfgBChannelsInUse_Object((1,3,6,1,4,1,9,10,19,1,1,10),_CpmSW56CfgBChannelsInUse_Type())
cpmSW56CfgBChannelsInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmSW56CfgBChannelsInUse.setStatus(_B)
_CpmISDNCfgBChanInUseForVoice_Type=Gauge32
_CpmISDNCfgBChanInUseForVoice_Object=MibScalar
cpmISDNCfgBChanInUseForVoice=_CpmISDNCfgBChanInUseForVoice_Object((1,3,6,1,4,1,9,10,19,1,1,11),_CpmISDNCfgBChanInUseForVoice_Type())
cpmISDNCfgBChanInUseForVoice.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmISDNCfgBChanInUseForVoice.setStatus(_B)
_CpmCASCfgBChanInUseForVoice_Type=Gauge32
_CpmCASCfgBChanInUseForVoice_Object=MibScalar
cpmCASCfgBChanInUseForVoice=_CpmCASCfgBChanInUseForVoice_Object((1,3,6,1,4,1,9,10,19,1,1,12),_CpmCASCfgBChanInUseForVoice_Type())
cpmCASCfgBChanInUseForVoice.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmCASCfgBChanInUseForVoice.setStatus(_B)
_CpmISDNCfgActiveDChannels_Type=Gauge32
_CpmISDNCfgActiveDChannels_Object=MibScalar
cpmISDNCfgActiveDChannels=_CpmISDNCfgActiveDChannels_Object((1,3,6,1,4,1,9,10,19,1,1,13),_CpmISDNCfgActiveDChannels_Type())
cpmISDNCfgActiveDChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmISDNCfgActiveDChannels.setStatus(_B)
_CpmISDNCfgBChannelsTimeInUse_Type=Counter32
_CpmISDNCfgBChannelsTimeInUse_Object=MibScalar
cpmISDNCfgBChannelsTimeInUse=_CpmISDNCfgBChannelsTimeInUse_Object((1,3,6,1,4,1,9,10,19,1,1,14),_CpmISDNCfgBChannelsTimeInUse_Type())
cpmISDNCfgBChannelsTimeInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmISDNCfgBChannelsTimeInUse.setStatus(_B)
if mibBuilder.loadTexts:cpmISDNCfgBChannelsTimeInUse.setUnits(_o)
_CpmISDNCfgBChannelsTimeInUseAnlg_Type=Counter32
_CpmISDNCfgBChannelsTimeInUseAnlg_Object=MibScalar
cpmISDNCfgBChannelsTimeInUseAnlg=_CpmISDNCfgBChannelsTimeInUseAnlg_Object((1,3,6,1,4,1,9,10,19,1,1,15),_CpmISDNCfgBChannelsTimeInUseAnlg_Type())
cpmISDNCfgBChannelsTimeInUseAnlg.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmISDNCfgBChannelsTimeInUseAnlg.setStatus(_B)
if mibBuilder.loadTexts:cpmISDNCfgBChannelsTimeInUseAnlg.setUnits(_o)
_CpmISDNCfgBChannelCalls_Type=Counter32
_CpmISDNCfgBChannelCalls_Object=MibScalar
cpmISDNCfgBChannelCalls=_CpmISDNCfgBChannelCalls_Object((1,3,6,1,4,1,9,10,19,1,1,16),_CpmISDNCfgBChannelCalls_Type())
cpmISDNCfgBChannelCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmISDNCfgBChannelCalls.setStatus(_B)
if mibBuilder.loadTexts:cpmISDNCfgBChannelCalls.setUnits(_H)
_CpmISDNCfgBChannelAnalogCalls_Type=Counter32
_CpmISDNCfgBChannelAnalogCalls_Object=MibScalar
cpmISDNCfgBChannelAnalogCalls=_CpmISDNCfgBChannelAnalogCalls_Object((1,3,6,1,4,1,9,10,19,1,1,17),_CpmISDNCfgBChannelAnalogCalls_Type())
cpmISDNCfgBChannelAnalogCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmISDNCfgBChannelAnalogCalls.setStatus(_B)
if mibBuilder.loadTexts:cpmISDNCfgBChannelAnalogCalls.setUnits(_H)
_CpmTotalISDNSyncPPPCalls_Type=Counter32
_CpmTotalISDNSyncPPPCalls_Object=MibScalar
cpmTotalISDNSyncPPPCalls=_CpmTotalISDNSyncPPPCalls_Object((1,3,6,1,4,1,9,10,19,1,1,18),_CpmTotalISDNSyncPPPCalls_Type())
cpmTotalISDNSyncPPPCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmTotalISDNSyncPPPCalls.setStatus(_B)
_CpmCallFailure_ObjectIdentity=ObjectIdentity
cpmCallFailure=_CpmCallFailure_ObjectIdentity((1,3,6,1,4,1,9,10,19,1,2))
_CpmISDNCallsRejected_Type=Counter32
_CpmISDNCallsRejected_Object=MibScalar
cpmISDNCallsRejected=_CpmISDNCallsRejected_Object((1,3,6,1,4,1,9,10,19,1,2,1),_CpmISDNCallsRejected_Type())
cpmISDNCallsRejected.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmISDNCallsRejected.setStatus(_B)
_CpmModemCallsRejected_Type=Counter32
_CpmModemCallsRejected_Object=MibScalar
cpmModemCallsRejected=_CpmModemCallsRejected_Object((1,3,6,1,4,1,9,10,19,1,2,2),_CpmModemCallsRejected_Type())
cpmModemCallsRejected.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmModemCallsRejected.setStatus(_B)
_CpmISDNCallsClearedAbnormally_Type=Counter32
_CpmISDNCallsClearedAbnormally_Object=MibScalar
cpmISDNCallsClearedAbnormally=_CpmISDNCallsClearedAbnormally_Object((1,3,6,1,4,1,9,10,19,1,2,3),_CpmISDNCallsClearedAbnormally_Type())
cpmISDNCallsClearedAbnormally.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmISDNCallsClearedAbnormally.setStatus(_B)
_CpmModemCallsClearedAbnormally_Type=Counter32
_CpmModemCallsClearedAbnormally_Object=MibScalar
cpmModemCallsClearedAbnormally=_CpmModemCallsClearedAbnormally_Object((1,3,6,1,4,1,9,10,19,1,2,4),_CpmModemCallsClearedAbnormally_Type())
cpmModemCallsClearedAbnormally.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmModemCallsClearedAbnormally.setStatus(_B)
_CpmISDNNoResource_Type=Counter32
_CpmISDNNoResource_Object=MibScalar
cpmISDNNoResource=_CpmISDNNoResource_Object((1,3,6,1,4,1,9,10,19,1,2,5),_CpmISDNNoResource_Type())
cpmISDNNoResource.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmISDNNoResource.setStatus(_B)
_CpmModemNoResource_Type=Counter32
_CpmModemNoResource_Object=MibScalar
cpmModemNoResource=_CpmModemNoResource_Object((1,3,6,1,4,1,9,10,19,1,2,6),_CpmModemNoResource_Type())
cpmModemNoResource.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmModemNoResource.setStatus(_B)
_CpmActiveCallSummary_ObjectIdentity=ObjectIdentity
cpmActiveCallSummary=_CpmActiveCallSummary_ObjectIdentity((1,3,6,1,4,1,9,10,19,1,3))
_CpmActiveCallSummaryTable_Object=MibTable
cpmActiveCallSummaryTable=_CpmActiveCallSummaryTable_Object((1,3,6,1,4,1,9,10,19,1,3,1))
if mibBuilder.loadTexts:cpmActiveCallSummaryTable.setStatus(_B)
_CpmActiveCallSummaryEntry_Object=MibTableRow
cpmActiveCallSummaryEntry=_CpmActiveCallSummaryEntry_Object((1,3,6,1,4,1,9,10,19,1,3,1,1))
cpmActiveCallSummaryEntry.setIndexNames((0,_A,_A7),(0,_A,_A8))
if mibBuilder.loadTexts:cpmActiveCallSummaryEntry.setStatus(_B)
_CpmActiveCallStartTimeIndex_Type=TimeStamp
_CpmActiveCallStartTimeIndex_Object=MibTableColumn
cpmActiveCallStartTimeIndex=_CpmActiveCallStartTimeIndex_Object((1,3,6,1,4,1,9,10,19,1,3,1,1,1),_CpmActiveCallStartTimeIndex_Type())
cpmActiveCallStartTimeIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cpmActiveCallStartTimeIndex.setStatus(_B)
class _CpmActiveCallSummaryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpmActiveCallSummaryIndex_Type.__name__=_D
_CpmActiveCallSummaryIndex_Object=MibTableColumn
cpmActiveCallSummaryIndex=_CpmActiveCallSummaryIndex_Object((1,3,6,1,4,1,9,10,19,1,3,1,1,2),_CpmActiveCallSummaryIndex_Type())
cpmActiveCallSummaryIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cpmActiveCallSummaryIndex.setStatus(_B)
class _CpmActiveUserID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpmActiveUserID_Type.__name__=_F
_CpmActiveUserID_Object=MibTableColumn
cpmActiveUserID=_CpmActiveUserID_Object((1,3,6,1,4,1,9,10,19,1,3,1,1,3),_CpmActiveUserID_Type())
cpmActiveUserID.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmActiveUserID.setStatus(_B)
_CpmActiveUserIpAddr_Type=IpAddress
_CpmActiveUserIpAddr_Object=MibTableColumn
cpmActiveUserIpAddr=_CpmActiveUserIpAddr_Object((1,3,6,1,4,1,9,10,19,1,3,1,1,4),_CpmActiveUserIpAddr_Type())
cpmActiveUserIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmActiveUserIpAddr.setStatus(_B)
class _CpmActiveCallType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),(_k,2),(_l,3),(_m,4),(_n,5),(_O,6)))
_CpmActiveCallType_Type.__name__=_D
_CpmActiveCallType_Object=MibTableColumn
cpmActiveCallType=_CpmActiveCallType_Object((1,3,6,1,4,1,9,10,19,1,3,1,1,5),_CpmActiveCallType_Type())
cpmActiveCallType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmActiveCallType.setStatus(_B)
class _CpmActiveModemSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpmActiveModemSlot_Type.__name__=_D
_CpmActiveModemSlot_Object=MibTableColumn
cpmActiveModemSlot=_CpmActiveModemSlot_Object((1,3,6,1,4,1,9,10,19,1,3,1,1,6),_CpmActiveModemSlot_Type())
cpmActiveModemSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmActiveModemSlot.setStatus(_B)
class _CpmActiveModemPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpmActiveModemPort_Type.__name__=_D
_CpmActiveModemPort_Object=MibTableColumn
cpmActiveModemPort=_CpmActiveModemPort_Object((1,3,6,1,4,1,9,10,19,1,3,1,1,7),_CpmActiveModemPort_Type())
cpmActiveModemPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmActiveModemPort.setStatus(_B)
_CpmActiveCallDuration_Type=TimeTicks
_CpmActiveCallDuration_Object=MibTableColumn
cpmActiveCallDuration=_CpmActiveCallDuration_Object((1,3,6,1,4,1,9,10,19,1,3,1,1,8),_CpmActiveCallDuration_Type())
cpmActiveCallDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmActiveCallDuration.setStatus(_B)
class _CpmActiveEntrySlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpmActiveEntrySlot_Type.__name__=_D
_CpmActiveEntrySlot_Object=MibTableColumn
cpmActiveEntrySlot=_CpmActiveEntrySlot_Object((1,3,6,1,4,1,9,10,19,1,3,1,1,9),_CpmActiveEntrySlot_Type())
cpmActiveEntrySlot.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmActiveEntrySlot.setStatus(_B)
class _CpmActiveEntryPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpmActiveEntryPort_Type.__name__=_D
_CpmActiveEntryPort_Object=MibTableColumn
cpmActiveEntryPort=_CpmActiveEntryPort_Object((1,3,6,1,4,1,9,10,19,1,3,1,1,10),_CpmActiveEntryPort_Type())
cpmActiveEntryPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmActiveEntryPort.setStatus(_B)
class _CpmActiveEntryChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpmActiveEntryChannel_Type.__name__=_D
_CpmActiveEntryChannel_Object=MibTableColumn
cpmActiveEntryChannel=_CpmActiveEntryChannel_Object((1,3,6,1,4,1,9,10,19,1,3,1,1,11),_CpmActiveEntryChannel_Type())
cpmActiveEntryChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmActiveEntryChannel.setStatus(_B)
class _CpmActiveRemotePhoneNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpmActiveRemotePhoneNumber_Type.__name__=_F
_CpmActiveRemotePhoneNumber_Object=MibTableColumn
cpmActiveRemotePhoneNumber=_CpmActiveRemotePhoneNumber_Object((1,3,6,1,4,1,9,10,19,1,3,1,1,12),_CpmActiveRemotePhoneNumber_Type())
cpmActiveRemotePhoneNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmActiveRemotePhoneNumber.setStatus(_B)
class _CpmActiveLocalPhoneNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpmActiveLocalPhoneNumber_Type.__name__=_F
_CpmActiveLocalPhoneNumber_Object=MibTableColumn
cpmActiveLocalPhoneNumber=_CpmActiveLocalPhoneNumber_Object((1,3,6,1,4,1,9,10,19,1,3,1,1,13),_CpmActiveLocalPhoneNumber_Type())
cpmActiveLocalPhoneNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmActiveLocalPhoneNumber.setStatus(_B)
_CpmActiveTTYNumber_Type=Integer32
_CpmActiveTTYNumber_Object=MibTableColumn
cpmActiveTTYNumber=_CpmActiveTTYNumber_Object((1,3,6,1,4,1,9,10,19,1,3,1,1,14),_CpmActiveTTYNumber_Type())
cpmActiveTTYNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmActiveTTYNumber.setStatus(_B)
_CpmCallHistorySummary_ObjectIdentity=ObjectIdentity
cpmCallHistorySummary=_CpmCallHistorySummary_ObjectIdentity((1,3,6,1,4,1,9,10,19,1,4))
class _CpmCallHistorySummaryTableMaxLength_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_CpmCallHistorySummaryTableMaxLength_Type.__name__=_D
_CpmCallHistorySummaryTableMaxLength_Object=MibScalar
cpmCallHistorySummaryTableMaxLength=_CpmCallHistorySummaryTableMaxLength_Object((1,3,6,1,4,1,9,10,19,1,4,1),_CpmCallHistorySummaryTableMaxLength_Type())
cpmCallHistorySummaryTableMaxLength.setMaxAccess(_L)
if mibBuilder.loadTexts:cpmCallHistorySummaryTableMaxLength.setStatus(_B)
class _CpmCallHistorySummaryRetainTimer_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_CpmCallHistorySummaryRetainTimer_Type.__name__=_D
_CpmCallHistorySummaryRetainTimer_Object=MibScalar
cpmCallHistorySummaryRetainTimer=_CpmCallHistorySummaryRetainTimer_Object((1,3,6,1,4,1,9,10,19,1,4,2),_CpmCallHistorySummaryRetainTimer_Type())
cpmCallHistorySummaryRetainTimer.setMaxAccess(_L)
if mibBuilder.loadTexts:cpmCallHistorySummaryRetainTimer.setStatus(_B)
if mibBuilder.loadTexts:cpmCallHistorySummaryRetainTimer.setUnits('minutes')
_CpmCallHistorySummaryTable_Object=MibTable
cpmCallHistorySummaryTable=_CpmCallHistorySummaryTable_Object((1,3,6,1,4,1,9,10,19,1,4,3))
if mibBuilder.loadTexts:cpmCallHistorySummaryTable.setStatus(_B)
_CpmCallHistorySummaryEntry_Object=MibTableRow
cpmCallHistorySummaryEntry=_CpmCallHistorySummaryEntry_Object((1,3,6,1,4,1,9,10,19,1,4,3,1))
cpmCallHistorySummaryEntry.setIndexNames((0,_A,_A9),(0,_A,_AA),(0,_A,_AB))
if mibBuilder.loadTexts:cpmCallHistorySummaryEntry.setStatus(_B)
_CpmCallDisconnectTimeIndex_Type=TimeStamp
_CpmCallDisconnectTimeIndex_Object=MibTableColumn
cpmCallDisconnectTimeIndex=_CpmCallDisconnectTimeIndex_Object((1,3,6,1,4,1,9,10,19,1,4,3,1,1),_CpmCallDisconnectTimeIndex_Type())
cpmCallDisconnectTimeIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cpmCallDisconnectTimeIndex.setStatus(_B)
_CpmCallStartTimeIndex_Type=TimeStamp
_CpmCallStartTimeIndex_Object=MibTableColumn
cpmCallStartTimeIndex=_CpmCallStartTimeIndex_Object((1,3,6,1,4,1,9,10,19,1,4,3,1,2),_CpmCallStartTimeIndex_Type())
cpmCallStartTimeIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cpmCallStartTimeIndex.setStatus(_B)
class _CpmCallHistorySummaryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpmCallHistorySummaryIndex_Type.__name__=_D
_CpmCallHistorySummaryIndex_Object=MibTableColumn
cpmCallHistorySummaryIndex=_CpmCallHistorySummaryIndex_Object((1,3,6,1,4,1,9,10,19,1,4,3,1,3),_CpmCallHistorySummaryIndex_Type())
cpmCallHistorySummaryIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cpmCallHistorySummaryIndex.setStatus(_B)
class _CpmUserID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpmUserID_Type.__name__=_F
_CpmUserID_Object=MibTableColumn
cpmUserID=_CpmUserID_Object((1,3,6,1,4,1,9,10,19,1,4,3,1,4),_CpmUserID_Type())
cpmUserID.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmUserID.setStatus(_B)
_CpmUserIpAddr_Type=IpAddress
_CpmUserIpAddr_Object=MibTableColumn
cpmUserIpAddr=_CpmUserIpAddr_Object((1,3,6,1,4,1,9,10,19,1,4,3,1,5),_CpmUserIpAddr_Type())
cpmUserIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmUserIpAddr.setStatus(_B)
class _CpmCallType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),(_k,2),(_l,3),(_m,4),(_n,5),(_O,6)))
_CpmCallType_Type.__name__=_D
_CpmCallType_Object=MibTableColumn
cpmCallType=_CpmCallType_Object((1,3,6,1,4,1,9,10,19,1,4,3,1,6),_CpmCallType_Type())
cpmCallType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmCallType.setStatus(_B)
_CpmModemSlot_Type=Integer32
_CpmModemSlot_Object=MibTableColumn
cpmModemSlot=_CpmModemSlot_Object((1,3,6,1,4,1,9,10,19,1,4,3,1,7),_CpmModemSlot_Type())
cpmModemSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmModemSlot.setStatus(_B)
_CpmModemPort_Type=Integer32
_CpmModemPort_Object=MibTableColumn
cpmModemPort=_CpmModemPort_Object((1,3,6,1,4,1,9,10,19,1,4,3,1,8),_CpmModemPort_Type())
cpmModemPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmModemPort.setStatus(_B)
_CpmCallDuration_Type=TimeTicks
_CpmCallDuration_Object=MibTableColumn
cpmCallDuration=_CpmCallDuration_Object((1,3,6,1,4,1,9,10,19,1,4,3,1,9),_CpmCallDuration_Type())
cpmCallDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmCallDuration.setStatus(_B)
_CpmEntrySlot_Type=Integer32
_CpmEntrySlot_Object=MibTableColumn
cpmEntrySlot=_CpmEntrySlot_Object((1,3,6,1,4,1,9,10,19,1,4,3,1,10),_CpmEntrySlot_Type())
cpmEntrySlot.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmEntrySlot.setStatus(_B)
_CpmEntryPort_Type=Integer32
_CpmEntryPort_Object=MibTableColumn
cpmEntryPort=_CpmEntryPort_Object((1,3,6,1,4,1,9,10,19,1,4,3,1,11),_CpmEntryPort_Type())
cpmEntryPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmEntryPort.setStatus(_B)
_CpmEntryChannel_Type=Integer32
_CpmEntryChannel_Object=MibTableColumn
cpmEntryChannel=_CpmEntryChannel_Object((1,3,6,1,4,1,9,10,19,1,4,3,1,12),_CpmEntryChannel_Type())
cpmEntryChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmEntryChannel.setStatus(_B)
class _CpmRemotePhoneNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpmRemotePhoneNumber_Type.__name__=_F
_CpmRemotePhoneNumber_Object=MibTableColumn
cpmRemotePhoneNumber=_CpmRemotePhoneNumber_Object((1,3,6,1,4,1,9,10,19,1,4,3,1,13),_CpmRemotePhoneNumber_Type())
cpmRemotePhoneNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmRemotePhoneNumber.setStatus(_B)
class _CpmLocalPhoneNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpmLocalPhoneNumber_Type.__name__=_F
_CpmLocalPhoneNumber_Object=MibTableColumn
cpmLocalPhoneNumber=_CpmLocalPhoneNumber_Object((1,3,6,1,4,1,9,10,19,1,4,3,1,14),_CpmLocalPhoneNumber_Type())
cpmLocalPhoneNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmLocalPhoneNumber.setStatus(_B)
_CpmTTYNumber_Type=Integer32
_CpmTTYNumber_Object=MibTableColumn
cpmTTYNumber=_CpmTTYNumber_Object((1,3,6,1,4,1,9,10,19,1,4,3,1,15),_CpmTTYNumber_Type())
cpmTTYNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmTTYNumber.setStatus(_B)
_CpmDS0Status_ObjectIdentity=ObjectIdentity
cpmDS0Status=_CpmDS0Status_ObjectIdentity((1,3,6,1,4,1,9,10,19,1,5))
_CpmDS0BusyoutNotifyEnable_Type=TruthValue
_CpmDS0BusyoutNotifyEnable_Object=MibScalar
cpmDS0BusyoutNotifyEnable=_CpmDS0BusyoutNotifyEnable_Object((1,3,6,1,4,1,9,10,19,1,5,1),_CpmDS0BusyoutNotifyEnable_Type())
cpmDS0BusyoutNotifyEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:cpmDS0BusyoutNotifyEnable.setStatus(_B)
_CpmDS0StatusTable_Object=MibTable
cpmDS0StatusTable=_CpmDS0StatusTable_Object((1,3,6,1,4,1,9,10,19,1,5,2))
if mibBuilder.loadTexts:cpmDS0StatusTable.setStatus(_B)
_CpmDS0StatusEntry_Object=MibTableRow
cpmDS0StatusEntry=_CpmDS0StatusEntry_Object((1,3,6,1,4,1,9,10,19,1,5,2,1))
if mibBuilder.loadTexts:cpmDS0StatusEntry.setStatus(_B)
class _CpmDS0OperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),('down',2),(_j,3),('setup',4),('connected',5),('test',6)))
_CpmDS0OperStatus_Type.__name__=_D
_CpmDS0OperStatus_Object=MibTableColumn
cpmDS0OperStatus=_CpmDS0OperStatus_Object((1,3,6,1,4,1,9,10,19,1,5,2,1,1),_CpmDS0OperStatus_Type())
cpmDS0OperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS0OperStatus.setStatus(_B)
class _CpmDS0BusyoutAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AC,1),('busyout',2),('busyoutImmediate',3)))
_CpmDS0BusyoutAdminStatus_Type.__name__=_D
_CpmDS0BusyoutAdminStatus_Object=MibTableColumn
cpmDS0BusyoutAdminStatus=_CpmDS0BusyoutAdminStatus_Object((1,3,6,1,4,1,9,10,19,1,5,2,1,2),_CpmDS0BusyoutAdminStatus_Type())
cpmDS0BusyoutAdminStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:cpmDS0BusyoutAdminStatus.setStatus(_B)
_CpmDS0BusyoutAllow_Type=TruthValue
_CpmDS0BusyoutAllow_Object=MibTableColumn
cpmDS0BusyoutAllow=_CpmDS0BusyoutAllow_Object((1,3,6,1,4,1,9,10,19,1,5,2,1,3),_CpmDS0BusyoutAllow_Type())
cpmDS0BusyoutAllow.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS0BusyoutAllow.setStatus(_B)
class _CpmDS0BusyoutStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_AC,1),('busyoutPending',2),('busiedOut',3)))
_CpmDS0BusyoutStatus_Type.__name__=_D
_CpmDS0BusyoutStatus_Object=MibTableColumn
cpmDS0BusyoutStatus=_CpmDS0BusyoutStatus_Object((1,3,6,1,4,1,9,10,19,1,5,2,1,4),_CpmDS0BusyoutStatus_Type())
cpmDS0BusyoutStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS0BusyoutStatus.setStatus(_B)
class _CpmDS0BusyoutSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('local',2),('internal',3),('remote',4)))
_CpmDS0BusyoutSource_Type.__name__=_D
_CpmDS0BusyoutSource_Object=MibTableColumn
cpmDS0BusyoutSource=_CpmDS0BusyoutSource_Object((1,3,6,1,4,1,9,10,19,1,5,2,1,5),_CpmDS0BusyoutSource_Type())
cpmDS0BusyoutSource.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS0BusyoutSource.setStatus(_B)
_CpmDS0BusyoutTime_Type=TimeStamp
_CpmDS0BusyoutTime_Object=MibTableColumn
cpmDS0BusyoutTime=_CpmDS0BusyoutTime_Object((1,3,6,1,4,1,9,10,19,1,5,2,1,6),_CpmDS0BusyoutTime_Type())
cpmDS0BusyoutTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS0BusyoutTime.setStatus(_B)
class _CpmDS0ConfigFunction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,1),('t1CcsSignallingChan',2),('t1CcsBearerChan',3),('e1CcsSignallingChan',4),('e1CcsBearerChan',5),('t1CasChan',6),('e1CasChan',7)))
_CpmDS0ConfigFunction_Type.__name__=_D
_CpmDS0ConfigFunction_Object=MibTableColumn
cpmDS0ConfigFunction=_CpmDS0ConfigFunction_Object((1,3,6,1,4,1,9,10,19,1,5,2,1,7),_CpmDS0ConfigFunction_Type())
cpmDS0ConfigFunction.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS0ConfigFunction.setStatus(_B)
_CpmDS0InterfaceIndex_Type=InterfaceIndexOrZero
_CpmDS0InterfaceIndex_Object=MibTableColumn
cpmDS0InterfaceIndex=_CpmDS0InterfaceIndex_Object((1,3,6,1,4,1,9,10,19,1,5,2,1,8),_CpmDS0InterfaceIndex_Type())
cpmDS0InterfaceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmDS0InterfaceIndex.setStatus(_B)
_CpmDS1LoopbackNotifyConfig_ObjectIdentity=ObjectIdentity
cpmDS1LoopbackNotifyConfig=_CpmDS1LoopbackNotifyConfig_ObjectIdentity((1,3,6,1,4,1,9,10,19,1,6))
_CpmDS1LoopbackNotifyEnable_Type=TruthValue
_CpmDS1LoopbackNotifyEnable_Object=MibScalar
cpmDS1LoopbackNotifyEnable=_CpmDS1LoopbackNotifyEnable_Object((1,3,6,1,4,1,9,10,19,1,6,1),_CpmDS1LoopbackNotifyEnable_Type())
cpmDS1LoopbackNotifyEnable.setMaxAccess(_L)
if mibBuilder.loadTexts:cpmDS1LoopbackNotifyEnable.setStatus(_B)
_CpmCallVolume_ObjectIdentity=ObjectIdentity
cpmCallVolume=_CpmCallVolume_ObjectIdentity((1,3,6,1,4,1,9,10,19,1,7))
_CpmCallVolSuccISDNDigital_Type=Counter32
_CpmCallVolSuccISDNDigital_Object=MibScalar
cpmCallVolSuccISDNDigital=_CpmCallVolSuccISDNDigital_Object((1,3,6,1,4,1,9,10,19,1,7,1),_CpmCallVolSuccISDNDigital_Type())
cpmCallVolSuccISDNDigital.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmCallVolSuccISDNDigital.setStatus(_B)
_CpmCallVolAnalogCallClearedNormally_Type=Counter32
_CpmCallVolAnalogCallClearedNormally_Object=MibScalar
cpmCallVolAnalogCallClearedNormally=_CpmCallVolAnalogCallClearedNormally_Object((1,3,6,1,4,1,9,10,19,1,7,2),_CpmCallVolAnalogCallClearedNormally_Type())
cpmCallVolAnalogCallClearedNormally.setMaxAccess(_C)
if mibBuilder.loadTexts:cpmCallVolAnalogCallClearedNormally.setStatus(_B)
_CPopMgmtMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
cPopMgmtMIBNotificationPrefix=_CPopMgmtMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,19,2))
_CpmNotifications_ObjectIdentity=ObjectIdentity
cpmNotifications=_CpmNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,19,2,0))
_CpmMIBConformance_ObjectIdentity=ObjectIdentity
cpmMIBConformance=_CpmMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,19,3))
_CpmMIBCompliances_ObjectIdentity=ObjectIdentity
cpmMIBCompliances=_CpmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,19,3,1))
_CpmMIBGroups_ObjectIdentity=ObjectIdentity
cpmMIBGroups=_CpmMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,19,3,2))
cpmDS0UsageEntry.registerAugmentions((_A,_AD))
cpmDS0StatusEntry.setIndexNames(*cpmDS0UsageEntry.getIndexNames())
cpmDS0UsageGroup=ObjectGroup((1,3,6,1,4,1,9,10,19,3,2,1))
cpmDS0UsageGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:cpmDS0UsageGroup.setStatus(_M)
cpmCallFailureGroup=ObjectGroup((1,3,6,1,4,1,9,10,19,3,2,2))
cpmCallFailureGroup.setObjects(*((_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ)))
if mibBuilder.loadTexts:cpmCallFailureGroup.setStatus(_B)
cpmActiveCallSummaryGroup=ObjectGroup((1,3,6,1,4,1,9,10,19,3,2,3))
cpmActiveCallSummaryGroup.setObjects(*((_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:cpmActiveCallSummaryGroup.setStatus(_B)
cpmCallHistorySummaryGroup=ObjectGroup((1,3,6,1,4,1,9,10,19,3,2,4))
cpmCallHistorySummaryGroup.setObjects(*((_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj)))
if mibBuilder.loadTexts:cpmCallHistorySummaryGroup.setStatus(_B)
cpmDS0UsageGroupRev1=ObjectGroup((1,3,6,1,4,1,9,10,19,3,2,5))
cpmDS0UsageGroupRev1.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_p),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:cpmDS0UsageGroupRev1.setStatus(_M)
cpmDS0UsageGroupRev2=ObjectGroup((1,3,6,1,4,1,9,10,19,3,2,6))
cpmDS0UsageGroupRev2.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_Ak),(_A,_Al)))
if mibBuilder.loadTexts:cpmDS0UsageGroupRev2.setStatus(_B)
cpmDS1UsageGroup=ObjectGroup((1,3,6,1,4,1,9,10,19,3,2,7))
cpmDS1UsageGroup.setObjects(*((_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay)))
if mibBuilder.loadTexts:cpmDS1UsageGroup.setStatus(_B)
cpmSystemGroup=ObjectGroup((1,3,6,1,4,1,9,10,19,3,2,8))
cpmSystemGroup.setObjects(*((_A,_Az),(_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3)))
if mibBuilder.loadTexts:cpmSystemGroup.setStatus(_B)
cpmDS0StatusGroup=ObjectGroup((1,3,6,1,4,1,9,10,19,3,2,9))
cpmDS0StatusGroup.setObjects(*((_A,_B4),(_A,_B5),(_A,_B6),(_A,_B7),(_A,_t),(_A,_u),(_A,_v),(_A,_B8),(_A,_w)))
if mibBuilder.loadTexts:cpmDS0StatusGroup.setStatus(_B)
cpmDS1LoopbackNotifyConfigGroup=ObjectGroup((1,3,6,1,4,1,9,10,19,3,2,11))
cpmDS1LoopbackNotifyConfigGroup.setObjects((_A,_B9))
if mibBuilder.loadTexts:cpmDS1LoopbackNotifyConfigGroup.setStatus(_B)
cpmCallVolumeGroup=ObjectGroup((1,3,6,1,4,1,9,10,19,3,2,12))
cpmCallVolumeGroup.setObjects(*((_A,_BA),(_A,_BB)))
if mibBuilder.loadTexts:cpmCallVolumeGroup.setStatus(_B)
cpmDS0BusyoutNotification=NotificationType((1,3,6,1,4,1,9,10,19,2,0,1))
cpmDS0BusyoutNotification.setObjects(*((_A,_t),(_A,_v),(_A,_u),(_A,_w)))
if mibBuilder.loadTexts:cpmDS0BusyoutNotification.setStatus(_B)
cpmDS1LoopbackNotification=NotificationType((1,3,6,1,4,1,9,10,19,2,0,2))
cpmDS1LoopbackNotification.setObjects(*((_i,_A1),(_i,_A0)))
if mibBuilder.loadTexts:cpmDS1LoopbackNotification.setStatus(_B)
cpmNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,10,19,3,2,10))
cpmNotificationGroup.setObjects((_A,_x))
if mibBuilder.loadTexts:cpmNotificationGroup.setStatus(_y)
cpmNotificationGroupRev1=NotificationGroup((1,3,6,1,4,1,9,10,19,3,2,13))
cpmNotificationGroupRev1.setObjects(*((_A,_x),(_A,_BC)))
if mibBuilder.loadTexts:cpmNotificationGroupRev1.setStatus(_B)
cpmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,19,3,1,1))
cpmMIBCompliance.setObjects(*((_A,_BD),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:cpmMIBCompliance.setStatus(_M)
cpmMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,10,19,3,1,2))
cpmMIBComplianceRev1.setObjects(*((_A,_BE),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:cpmMIBComplianceRev1.setStatus(_M)
cpmComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,10,19,3,1,3))
cpmComplianceRev2.setObjects(*((_A,_N),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:cpmComplianceRev2.setStatus(_M)
cpmMIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,10,19,3,1,4))
cpmMIBComplianceRev3.setObjects(*((_A,_N),(_A,_I),(_A,_J),(_A,_K),(_A,_f),(_A,_g),(_A,_h),(_A,_BF)))
if mibBuilder.loadTexts:cpmMIBComplianceRev3.setStatus(_y)
cpmMIBComplianceRev4=ModuleCompliance((1,3,6,1,4,1,9,10,19,3,1,5))
cpmMIBComplianceRev4.setObjects(*((_A,_N),(_A,_I),(_A,_J),(_A,_K),(_A,_z),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:cpmMIBComplianceRev4.setStatus(_y)
cpmMIBComplianceRev5=ModuleCompliance((1,3,6,1,4,1,9,10,19,3,1,6))
cpmMIBComplianceRev5.setObjects(*((_A,_N),(_A,_I),(_A,_J),(_A,_K),(_A,_z),(_A,_f),(_A,_g),(_A,_h),(_A,_BG),(_A,_BH)))
if mibBuilder.loadTexts:cpmMIBComplianceRev5.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoPopMgmtMIB':ciscoPopMgmtMIB,'ciscoPopMgmtMIBObjects':ciscoPopMgmtMIBObjects,'cpmDS0Usage':cpmDS0Usage,'cpmDS0UsageTable':cpmDS0UsageTable,'cpmDS0UsageEntry':cpmDS0UsageEntry,_A2:cpmDS1SlotIndex,_A3:cpmDS1PortIndex,_A4:cpmChannelIndex,_P:cpmConfiguredType,_Q:cpmDS0CallType,_R:cpmL2Encapsulation,_S:cpmCallCount,_T:cpmTimeInUse,_U:cpmInOctets,_V:cpmOutOctets,_W:cpmInPackets,_X:cpmOutPackets,_Y:cpmAssociatedInterface,_Z:cpmISDNCfgBChanInUseForAnalog,_a:cpmISDNCfgBChannelsInUse,_b:cpmActiveDS0s,_c:cpmPPPCalls,_d:cpmV120Calls,_e:cpmV110Calls,_p:cpmActiveDS0sHighWaterMark,'cpmDS1DS0UsageTable':cpmDS1DS0UsageTable,'cpmDS1DS0UsageEntry':cpmDS1DS0UsageEntry,_A5:cpmDS1UsageSlotIndex,_A6:cpmDS1UsagePortIndex,_q:cpmDS1ActiveDS0s,_r:cpmDS1ActiveDS0sHighWaterMark,_Am:cpmDS1TotalAnalogCalls,_An:cpmDS1TotalDigitalCalls,_Ao:cpmDS1TotalV110Calls,_Ap:cpmDS1TotalV120Calls,_Aq:cpmDS1TotalCalls,_Ar:cpmDS1TotalTimeInUse,_As:cpmDS1CurrentIdle,_At:cpmDS1CurrentOutOfService,_Au:cpmDS1CurrentBusyout,_Av:cpmDS1InOctets,_Aw:cpmDS1OutOctets,_Ax:cpmDS1InPackets,_Ay:cpmDS1OutPackets,_s:cpmSW56CfgBChannelsInUse,_Ak:cpmISDNCfgBChanInUseForVoice,_Al:cpmCASCfgBChanInUseForVoice,_Az:cpmISDNCfgActiveDChannels,_A_:cpmISDNCfgBChannelsTimeInUse,_B0:cpmISDNCfgBChannelsTimeInUseAnlg,_B1:cpmISDNCfgBChannelCalls,_B2:cpmISDNCfgBChannelAnalogCalls,_B3:cpmTotalISDNSyncPPPCalls,'cpmCallFailure':cpmCallFailure,_AE:cpmISDNCallsRejected,_AF:cpmModemCallsRejected,_AG:cpmISDNCallsClearedAbnormally,_AH:cpmModemCallsClearedAbnormally,_AI:cpmISDNNoResource,_AJ:cpmModemNoResource,'cpmActiveCallSummary':cpmActiveCallSummary,'cpmActiveCallSummaryTable':cpmActiveCallSummaryTable,'cpmActiveCallSummaryEntry':cpmActiveCallSummaryEntry,_A7:cpmActiveCallStartTimeIndex,_A8:cpmActiveCallSummaryIndex,_AK:cpmActiveUserID,_AM:cpmActiveUserIpAddr,_AL:cpmActiveCallType,_AN:cpmActiveModemSlot,_AO:cpmActiveModemPort,_AP:cpmActiveCallDuration,_AQ:cpmActiveEntrySlot,_AR:cpmActiveEntryPort,_AS:cpmActiveEntryChannel,_AT:cpmActiveRemotePhoneNumber,_AU:cpmActiveLocalPhoneNumber,_AV:cpmActiveTTYNumber,'cpmCallHistorySummary':cpmCallHistorySummary,_AW:cpmCallHistorySummaryTableMaxLength,_AX:cpmCallHistorySummaryRetainTimer,'cpmCallHistorySummaryTable':cpmCallHistorySummaryTable,'cpmCallHistorySummaryEntry':cpmCallHistorySummaryEntry,_A9:cpmCallDisconnectTimeIndex,_AA:cpmCallStartTimeIndex,_AB:cpmCallHistorySummaryIndex,_AY:cpmUserID,_AZ:cpmUserIpAddr,_Aa:cpmCallType,_Ab:cpmModemSlot,_Ac:cpmModemPort,_Ad:cpmCallDuration,_Ae:cpmEntrySlot,_Af:cpmEntryPort,_Ag:cpmEntryChannel,_Ah:cpmRemotePhoneNumber,_Ai:cpmLocalPhoneNumber,_Aj:cpmTTYNumber,'cpmDS0Status':cpmDS0Status,_B4:cpmDS0BusyoutNotifyEnable,'cpmDS0StatusTable':cpmDS0StatusTable,_AD:cpmDS0StatusEntry,_B5:cpmDS0OperStatus,_B6:cpmDS0BusyoutAdminStatus,_B7:cpmDS0BusyoutAllow,_t:cpmDS0BusyoutStatus,_u:cpmDS0BusyoutSource,_v:cpmDS0BusyoutTime,_B8:cpmDS0ConfigFunction,_w:cpmDS0InterfaceIndex,'cpmDS1LoopbackNotifyConfig':cpmDS1LoopbackNotifyConfig,_B9:cpmDS1LoopbackNotifyEnable,'cpmCallVolume':cpmCallVolume,_BA:cpmCallVolSuccISDNDigital,_BB:cpmCallVolAnalogCallClearedNormally,'cPopMgmtMIBNotificationPrefix':cPopMgmtMIBNotificationPrefix,'cpmNotifications':cpmNotifications,_x:cpmDS0BusyoutNotification,_BC:cpmDS1LoopbackNotification,'cpmMIBConformance':cpmMIBConformance,'cpmMIBCompliances':cpmMIBCompliances,'cpmMIBCompliance':cpmMIBCompliance,'cpmMIBComplianceRev1':cpmMIBComplianceRev1,'cpmComplianceRev2':cpmComplianceRev2,'cpmMIBComplianceRev3':cpmMIBComplianceRev3,'cpmMIBComplianceRev4':cpmMIBComplianceRev4,'cpmMIBComplianceRev5':cpmMIBComplianceRev5,'cpmMIBGroups':cpmMIBGroups,_BD:cpmDS0UsageGroup,_I:cpmCallFailureGroup,_J:cpmActiveCallSummaryGroup,_K:cpmCallHistorySummaryGroup,_BE:cpmDS0UsageGroupRev1,_N:cpmDS0UsageGroupRev2,_g:cpmDS1UsageGroup,_h:cpmSystemGroup,_f:cpmDS0StatusGroup,_BF:cpmNotificationGroup,_BG:cpmDS1LoopbackNotifyConfigGroup,_z:cpmCallVolumeGroup,_BH:cpmNotificationGroupRev1})