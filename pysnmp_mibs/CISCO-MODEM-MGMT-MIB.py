_AW='cmManagedLineInfoGroupRev2'
_AV='cmLineSpeedInfoGroupRev2'
_AU='cmManagedLineInfoGroupRev1'
_AT='cmStateNotification'
_AS='cmStateNotifyEnable'
_AR='cmSystemModemsDead'
_AQ='cmSystemModemsOffline'
_AP='cmSystemModemsUnavailable'
_AO='cmSystemModemsAvailable'
_AN='cmSystemModemsInUse'
_AM='cmWatchdogTimeouts'
_AL='cmFailedDialAttempts'
_AK='cmRingNoAnswers'
_AJ='cmHoldReset'
_AI='cmShutdown'
_AH='cmBusyOutRequest'
_AG='cmStatusPolling'
_AF='cmATModePermit'
_AE='cmCallerID'
_AD='cmCallPhoneNumber'
_AC='cmCallDuration'
_AB='cmCallDirection'
_AA='cmDisconnectReason'
_A9='cmManageable'
_A8='cmProductDetails'
_A7='cmManufacturerID'
_A6='cmInterface'
_A5='cmGroupTotalDevices'
_A4='cmLineStatisticsEntry'
_A3='cmLineConfigEntry'
_A2='cmInitialLineSpeed'
_A1='bits/second'
_A0='cmNotificationGroup'
_z='cmNotificationConfigGroup'
_y='cmLineSpeedInfoGroup'
_x='cmSystemInfoGroup'
_w='cmInitialRxLineConnections'
_v='cmInitialTxLineConnections'
_u='cmInitialLineConnections'
_t='cmGreaterThan14400Connections'
_s='cm2400To14400Connections'
_r='cm2400OrLessConnections'
_q='cmState'
_p='cmSystemMaxRetries'
_o='cmSystemStatusPollTime'
_n='cmSystemWatchdogTime'
_m='cmSystemConfiguredGroup'
_l='cmSystemInstalledModem'
_k='not-accessible'
_j='cmGroupIndex'
_i='cmLineSpeedInfoGroupRev1'
_h='cmTotalCallDuration'
_g='cmPollingTimeouts'
_f='cmProtocolErrors'
_e='cmLinkFailures'
_d='cmNoCarriers'
_c='cmDialTimeouts'
_b='cmNoDialTones'
_a='cmOutgoingConnectionCompletions'
_Z='cmOutgoingConnectionFailures'
_Y='cmIncomingConnectionCompletions'
_X='cmIncomingConnectionFailures'
_W='cmRXAnalogSignalLevel'
_V='cmTXAnalogSignalLevel'
_U='cmRXRate'
_T='cmTXRate'
_S='cmProtocolUsed'
_R='cmModulationSchemeUsed'
_Q='unknown'
_P='cmSlotIndex'
_O='cmPortIndex'
_N='DisplayString'
_M='cmSystemInfoGroupRev1'
_L='cmManagedLineInfoGroup'
_K='obsolete'
_J='TruthValue'
_I='cmGroupInfoGroup'
_H='cmLineInfoGroup'
_G='deprecated'
_F='read-write'
_E='Integer32'
_D='calls'
_C='read-only'
_B='current'
_A='CISCO-MODEM-MGMT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','TextualConvention',_J)
ciscoModemMgmtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,47))
if mibBuilder.loadTexts:ciscoModemMgmtMIB.setRevisions(('2005-12-06 00:00','2001-12-01 12:00','2001-10-01 12:00','2000-04-01 00:00','1998-12-16 00:00','1998-06-18 00:00','1997-12-22 00:00','1997-10-13 00:00','1997-07-18 00:00','1998-03-09 00:00','1997-12-16 00:00','1997-05-01 00:00','1997-04-29 00:00','1997-06-11 00:00','1997-03-21 00:00','1997-03-17 00:00','1996-01-11 00:00'))
_CiscoModemMgmtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoModemMgmtMIBObjects=_CiscoModemMgmtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,47,1))
_CmSystemInfo_ObjectIdentity=ObjectIdentity
cmSystemInfo=_CmSystemInfo_ObjectIdentity((1,3,6,1,4,1,9,9,47,1,1))
_CmSystemInstalledModem_Type=Gauge32
_CmSystemInstalledModem_Object=MibScalar
cmSystemInstalledModem=_CmSystemInstalledModem_Object((1,3,6,1,4,1,9,9,47,1,1,1),_CmSystemInstalledModem_Type())
cmSystemInstalledModem.setMaxAccess(_C)
if mibBuilder.loadTexts:cmSystemInstalledModem.setStatus(_B)
if mibBuilder.loadTexts:cmSystemInstalledModem.setUnits('modems')
_CmSystemConfiguredGroup_Type=Gauge32
_CmSystemConfiguredGroup_Object=MibScalar
cmSystemConfiguredGroup=_CmSystemConfiguredGroup_Object((1,3,6,1,4,1,9,9,47,1,1,2),_CmSystemConfiguredGroup_Type())
cmSystemConfiguredGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:cmSystemConfiguredGroup.setStatus(_B)
class _CmSystemWatchdogTime_Type(Integer32):defaultValue=6
_CmSystemWatchdogTime_Type.__name__=_E
_CmSystemWatchdogTime_Object=MibScalar
cmSystemWatchdogTime=_CmSystemWatchdogTime_Object((1,3,6,1,4,1,9,9,47,1,1,3),_CmSystemWatchdogTime_Type())
cmSystemWatchdogTime.setMaxAccess(_F)
if mibBuilder.loadTexts:cmSystemWatchdogTime.setStatus(_B)
if mibBuilder.loadTexts:cmSystemWatchdogTime.setUnits('minutes')
class _CmSystemStatusPollTime_Type(Integer32):defaultValue=12;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,120))
_CmSystemStatusPollTime_Type.__name__=_E
_CmSystemStatusPollTime_Object=MibScalar
cmSystemStatusPollTime=_CmSystemStatusPollTime_Object((1,3,6,1,4,1,9,9,47,1,1,4),_CmSystemStatusPollTime_Type())
cmSystemStatusPollTime.setMaxAccess(_F)
if mibBuilder.loadTexts:cmSystemStatusPollTime.setStatus(_B)
if mibBuilder.loadTexts:cmSystemStatusPollTime.setUnits('seconds')
class _CmSystemMaxRetries_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_CmSystemMaxRetries_Type.__name__=_E
_CmSystemMaxRetries_Object=MibScalar
cmSystemMaxRetries=_CmSystemMaxRetries_Object((1,3,6,1,4,1,9,9,47,1,1,5),_CmSystemMaxRetries_Type())
cmSystemMaxRetries.setMaxAccess(_F)
if mibBuilder.loadTexts:cmSystemMaxRetries.setStatus(_B)
_CmSystemModemsInUse_Type=Gauge32
_CmSystemModemsInUse_Object=MibScalar
cmSystemModemsInUse=_CmSystemModemsInUse_Object((1,3,6,1,4,1,9,9,47,1,1,6),_CmSystemModemsInUse_Type())
cmSystemModemsInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:cmSystemModemsInUse.setStatus(_B)
_CmSystemModemsAvailable_Type=Gauge32
_CmSystemModemsAvailable_Object=MibScalar
cmSystemModemsAvailable=_CmSystemModemsAvailable_Object((1,3,6,1,4,1,9,9,47,1,1,7),_CmSystemModemsAvailable_Type())
cmSystemModemsAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:cmSystemModemsAvailable.setStatus(_B)
_CmSystemModemsUnavailable_Type=Gauge32
_CmSystemModemsUnavailable_Object=MibScalar
cmSystemModemsUnavailable=_CmSystemModemsUnavailable_Object((1,3,6,1,4,1,9,9,47,1,1,8),_CmSystemModemsUnavailable_Type())
cmSystemModemsUnavailable.setMaxAccess(_C)
if mibBuilder.loadTexts:cmSystemModemsUnavailable.setStatus(_B)
_CmSystemModemsOffline_Type=Gauge32
_CmSystemModemsOffline_Object=MibScalar
cmSystemModemsOffline=_CmSystemModemsOffline_Object((1,3,6,1,4,1,9,9,47,1,1,9),_CmSystemModemsOffline_Type())
cmSystemModemsOffline.setMaxAccess(_C)
if mibBuilder.loadTexts:cmSystemModemsOffline.setStatus(_B)
_CmSystemModemsDead_Type=Gauge32
_CmSystemModemsDead_Object=MibScalar
cmSystemModemsDead=_CmSystemModemsDead_Object((1,3,6,1,4,1,9,9,47,1,1,10),_CmSystemModemsDead_Type())
cmSystemModemsDead.setMaxAccess(_C)
if mibBuilder.loadTexts:cmSystemModemsDead.setStatus(_B)
_CmGroupInfo_ObjectIdentity=ObjectIdentity
cmGroupInfo=_CmGroupInfo_ObjectIdentity((1,3,6,1,4,1,9,9,47,1,2))
_CmGroupTable_Object=MibTable
cmGroupTable=_CmGroupTable_Object((1,3,6,1,4,1,9,9,47,1,2,1))
if mibBuilder.loadTexts:cmGroupTable.setStatus(_B)
_CmGroupEntry_Object=MibTableRow
cmGroupEntry=_CmGroupEntry_Object((1,3,6,1,4,1,9,9,47,1,2,1,1))
cmGroupEntry.setIndexNames((0,_A,_j))
if mibBuilder.loadTexts:cmGroupEntry.setStatus(_B)
_CmGroupIndex_Type=Unsigned32
_CmGroupIndex_Object=MibTableColumn
cmGroupIndex=_CmGroupIndex_Object((1,3,6,1,4,1,9,9,47,1,2,1,1,1),_CmGroupIndex_Type())
cmGroupIndex.setMaxAccess(_k)
if mibBuilder.loadTexts:cmGroupIndex.setStatus(_B)
_CmGroupTotalDevices_Type=Integer32
_CmGroupTotalDevices_Object=MibTableColumn
cmGroupTotalDevices=_CmGroupTotalDevices_Object((1,3,6,1,4,1,9,9,47,1,2,1,1,2),_CmGroupTotalDevices_Type())
cmGroupTotalDevices.setMaxAccess(_C)
if mibBuilder.loadTexts:cmGroupTotalDevices.setStatus(_B)
_CmGroupMemberTable_Object=MibTable
cmGroupMemberTable=_CmGroupMemberTable_Object((1,3,6,1,4,1,9,9,47,1,2,2))
if mibBuilder.loadTexts:cmGroupMemberTable.setStatus(_B)
_CmGroupMemberEntry_Object=MibTableRow
cmGroupMemberEntry=_CmGroupMemberEntry_Object((1,3,6,1,4,1,9,9,47,1,2,2,1))
cmGroupMemberEntry.setIndexNames((0,_A,_j),(0,_A,_P),(0,_A,_O))
if mibBuilder.loadTexts:cmGroupMemberEntry.setStatus(_B)
_CmSlotIndex_Type=Unsigned32
_CmSlotIndex_Object=MibTableColumn
cmSlotIndex=_CmSlotIndex_Object((1,3,6,1,4,1,9,9,47,1,2,2,1,1),_CmSlotIndex_Type())
cmSlotIndex.setMaxAccess(_k)
if mibBuilder.loadTexts:cmSlotIndex.setStatus(_B)
_CmPortIndex_Type=Unsigned32
_CmPortIndex_Object=MibTableColumn
cmPortIndex=_CmPortIndex_Object((1,3,6,1,4,1,9,9,47,1,2,2,1,2),_CmPortIndex_Type())
cmPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cmPortIndex.setStatus(_B)
_CmLineInfo_ObjectIdentity=ObjectIdentity
cmLineInfo=_CmLineInfo_ObjectIdentity((1,3,6,1,4,1,9,9,47,1,3))
_CmLineStatusTable_Object=MibTable
cmLineStatusTable=_CmLineStatusTable_Object((1,3,6,1,4,1,9,9,47,1,3,1))
if mibBuilder.loadTexts:cmLineStatusTable.setStatus(_B)
_CmLineStatusEntry_Object=MibTableRow
cmLineStatusEntry=_CmLineStatusEntry_Object((1,3,6,1,4,1,9,9,47,1,3,1,1))
cmLineStatusEntry.setIndexNames((0,_A,_P),(0,_A,_O))
if mibBuilder.loadTexts:cmLineStatusEntry.setStatus(_B)
_CmInterface_Type=InterfaceIndex
_CmInterface_Object=MibTableColumn
cmInterface=_CmInterface_Object((1,3,6,1,4,1,9,9,47,1,3,1,1,1),_CmInterface_Type())
cmInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:cmInterface.setStatus(_B)
_CmGroup_Type=Integer32
_CmGroup_Object=MibTableColumn
cmGroup=_CmGroup_Object((1,3,6,1,4,1,9,9,47,1,3,1,1,2),_CmGroup_Type())
cmGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:cmGroup.setStatus(_B)
class _CmManufacturerID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_CmManufacturerID_Type.__name__=_N
_CmManufacturerID_Object=MibTableColumn
cmManufacturerID=_CmManufacturerID_Object((1,3,6,1,4,1,9,9,47,1,3,1,1,3),_CmManufacturerID_Type())
cmManufacturerID.setMaxAccess(_C)
if mibBuilder.loadTexts:cmManufacturerID.setStatus(_B)
class _CmProductDetails_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_CmProductDetails_Type.__name__=_N
_CmProductDetails_Object=MibTableColumn
cmProductDetails=_CmProductDetails_Object((1,3,6,1,4,1,9,9,47,1,3,1,1,4),_CmProductDetails_Type())
cmProductDetails.setMaxAccess(_C)
if mibBuilder.loadTexts:cmProductDetails.setStatus(_B)
_CmManageable_Type=TruthValue
_CmManageable_Object=MibTableColumn
cmManageable=_CmManageable_Object((1,3,6,1,4,1,9,9,47,1,3,1,1,5),_CmManageable_Type())
cmManageable.setMaxAccess(_C)
if mibBuilder.loadTexts:cmManageable.setStatus(_B)
class _CmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_Q,1),('onHook',2),('offHook',3),('connected',4),('busiedOut',5),('disabled',6),('bad',7),('loopback',8),('downloadFirmware',9),('downloadFirmwareFailed',10)))
_CmState_Type.__name__=_E
_CmState_Object=MibTableColumn
cmState=_CmState_Object((1,3,6,1,4,1,9,9,47,1,3,1,1,6),_CmState_Type())
cmState.setMaxAccess(_C)
if mibBuilder.loadTexts:cmState.setStatus(_B)
class _CmCallDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('incoming',1),('outgoing',2),('none',3)))
_CmCallDirection_Type.__name__=_E
_CmCallDirection_Object=MibTableColumn
cmCallDirection=_CmCallDirection_Object((1,3,6,1,4,1,9,9,47,1,3,1,1,7),_CmCallDirection_Type())
cmCallDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:cmCallDirection.setStatus(_B)
class _CmDisconnectReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103)));namedValues=NamedValues(*((_Q,1),('lostCarrier',2),('noCarrier',3),('noDialTone',4),('busy',5),('modemWatchdogTimeout',6),('dtrDrop',7),('userHangup',8),('compressionProblem',9),('retrainFailure',10),('remoteLinkDisconnect',11),('abort',12),('inactivityTimeout',13),('dialStringError',14),('linkFailure',15),('modulationError',16),('dialTimeout',17),('remoteHangup',18),('mnp10ProtocolError',19),('lapmProtocolError',20),('faxClass2Error',21),('trainupFailure',22),('fallbackTerminate',23),('excessiveEC',24),('hostDrop',25),('terminate',26),('autoLogonError',27),('ccpNotSeen',28),('callbackFailed',29),('blacklist',30),('lapmTimeout',31),('reliableLinkTxTimeout',32),('dspAccessFailure',33),('cdOffTimeout',34),('codewordSizeMismatch',35),('dspDownloadFailure',36),('modemDrNone',37),('modemDrSoftwareReset',38),('modemDrEcTerminated',39),('modemDrBadMnp5Rxdata',40),('modemDrBadV42bisRxdata',41),('modemDrBadCopState',42),('modemDrAth',43),('modemDrAborted',44),('modemDrConnectTimeout',45),('modemDrResetDsp',46),('modemDrNoCarrier',47),('modemDrNoAbtDetected',48),('modemDrTrainupFailure',49),('modemDrRetrainLimit',50),('modemDrAbtEndFailure',51),('modemDrNoLr',52),('modemDrLrParam1',53),('modemDrLrIncompat',54),('modemDrRetransmitLimit',55),('modemDrInactivity',56),('modemDrProtocolError',57),('modemDrFallbackTerminate',58),('modemDrNoXid',59),('modemDrXidIncompat',60),('modemDrDisc',61),('modemDrDm',62),('modemDrBadNr',63),('modemDrSabmeOnline',64),('modemDrXidOnline',65),('modemDrLrOnline',66),('modemDrBadCmnd',67),('modemDrFrmrBadCmnd',68),('modemDrFrmrData',69),('modemDrFrmrLength',70),('modemDrFrmrBadNr',71),('modemDrLdNoLr',72),('modemDrLdLrParam1',73),('modemDrLdLrIncompat',74),('modemDrLdRetransLimit',75),('modemDrLdInactivity',76),('modemDrLdProtocol',77),('modemDrLdUser',78),('modemDrHostNonspecific',79),('modemDrHostBusy',80),('modemDrHostNoAnswer',81),('modemDrHostDtr',82),('modemDrHostAth',83),('modemDrHostNoDialtone',84),('modemDrHostNoCarrier',85),('modemDrHostAck',86),('modemDrMohClrd',87),('modemDrMohTimeout',88),('modemDrCotAck',89),('modemDrCotNak1',90),('modemDrCotNak2',91),('modemDrCotOff',92),('modemDrCotTimeout',93),('modemDrDcIllegalCodewordStepup',94),('modemDrDcIllegalTokenEmptyNode',95),('modemDrDcIllegalTokenTooLarge',96),('modemDrDcReservedCommand',97),('modemDrDcIllegalCharacterSizeStepup',98),('modemDrDcRxDictionaryFull',99),('modemDrDcRxHistoryFull',100),('modemDrDcRxStringSizeExceeded',101),('modemDrDcNegotiationError',102),('modemDrDcCompressionError',103)))
_CmDisconnectReason_Type.__name__=_E
_CmDisconnectReason_Object=MibTableColumn
cmDisconnectReason=_CmDisconnectReason_Object((1,3,6,1,4,1,9,9,47,1,3,1,1,8),_CmDisconnectReason_Type())
cmDisconnectReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cmDisconnectReason.setStatus(_B)
_CmCallDuration_Type=TimeTicks
_CmCallDuration_Object=MibTableColumn
cmCallDuration=_CmCallDuration_Object((1,3,6,1,4,1,9,9,47,1,3,1,1,9),_CmCallDuration_Type())
cmCallDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:cmCallDuration.setStatus(_B)
class _CmCallPhoneNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CmCallPhoneNumber_Type.__name__=_N
_CmCallPhoneNumber_Object=MibTableColumn
cmCallPhoneNumber=_CmCallPhoneNumber_Object((1,3,6,1,4,1,9,9,47,1,3,1,1,10),_CmCallPhoneNumber_Type())
cmCallPhoneNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cmCallPhoneNumber.setStatus(_B)
class _CmCallerID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CmCallerID_Type.__name__=_N
_CmCallerID_Object=MibTableColumn
cmCallerID=_CmCallerID_Object((1,3,6,1,4,1,9,9,47,1,3,1,1,11),_CmCallerID_Type())
cmCallerID.setMaxAccess(_C)
if mibBuilder.loadTexts:cmCallerID.setStatus(_B)
class _CmModulationSchemeUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)));namedValues=NamedValues(*((_Q,1),('bell103a',2),('bell212a',3),('v21',4),('v22',5),('v22bis',6),('v32',7),('v32bis',8),('vfc',9),('v34',10),('v17',11),('v29',12),('v33',13),('k56flex',14),('v23',15),('v32terbo',16),('v34plus',17),('v90',18),('v27ter',19),('v110',20),('piafs',21)))
_CmModulationSchemeUsed_Type.__name__=_E
_CmModulationSchemeUsed_Object=MibTableColumn
cmModulationSchemeUsed=_CmModulationSchemeUsed_Object((1,3,6,1,4,1,9,9,47,1,3,1,1,12),_CmModulationSchemeUsed_Type())
cmModulationSchemeUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cmModulationSchemeUsed.setStatus(_B)
class _CmProtocolUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('normal',1),('direct',2),('reliableMNP',3),('reliableLAPM',4),('syncMode',5),('asyncMode',6),('ara10',7),('ara20',8),(_Q,9)))
_CmProtocolUsed_Type.__name__=_E
_CmProtocolUsed_Object=MibTableColumn
cmProtocolUsed=_CmProtocolUsed_Object((1,3,6,1,4,1,9,9,47,1,3,1,1,13),_CmProtocolUsed_Type())
cmProtocolUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cmProtocolUsed.setStatus(_B)
_CmTXRate_Type=Gauge32
_CmTXRate_Object=MibTableColumn
cmTXRate=_CmTXRate_Object((1,3,6,1,4,1,9,9,47,1,3,1,1,14),_CmTXRate_Type())
cmTXRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cmTXRate.setStatus(_B)
if mibBuilder.loadTexts:cmTXRate.setUnits(_A1)
_CmRXRate_Type=Gauge32
_CmRXRate_Object=MibTableColumn
cmRXRate=_CmRXRate_Object((1,3,6,1,4,1,9,9,47,1,3,1,1,15),_CmRXRate_Type())
cmRXRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRXRate.setStatus(_B)
if mibBuilder.loadTexts:cmRXRate.setUnits(_A1)
class _CmTXAnalogSignalLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-43,-9),ValueRangeConstraint(0,0))
_CmTXAnalogSignalLevel_Type.__name__=_E
_CmTXAnalogSignalLevel_Object=MibTableColumn
cmTXAnalogSignalLevel=_CmTXAnalogSignalLevel_Object((1,3,6,1,4,1,9,9,47,1,3,1,1,16),_CmTXAnalogSignalLevel_Type())
cmTXAnalogSignalLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:cmTXAnalogSignalLevel.setStatus(_B)
if mibBuilder.loadTexts:cmTXAnalogSignalLevel.setUnits('dBm')
class _CmRXAnalogSignalLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-128,-1),ValueRangeConstraint(0,0))
_CmRXAnalogSignalLevel_Type.__name__=_E
_CmRXAnalogSignalLevel_Object=MibTableColumn
cmRXAnalogSignalLevel=_CmRXAnalogSignalLevel_Object((1,3,6,1,4,1,9,9,47,1,3,1,1,17),_CmRXAnalogSignalLevel_Type())
cmRXAnalogSignalLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRXAnalogSignalLevel.setStatus(_B)
if mibBuilder.loadTexts:cmRXAnalogSignalLevel.setUnits('dBm')
_CmLineConfigTable_Object=MibTable
cmLineConfigTable=_CmLineConfigTable_Object((1,3,6,1,4,1,9,9,47,1,3,2))
if mibBuilder.loadTexts:cmLineConfigTable.setStatus(_B)
_CmLineConfigEntry_Object=MibTableRow
cmLineConfigEntry=_CmLineConfigEntry_Object((1,3,6,1,4,1,9,9,47,1,3,2,1))
if mibBuilder.loadTexts:cmLineConfigEntry.setStatus(_B)
class _CmATModePermit_Type(TruthValue):defaultValue=1
_CmATModePermit_Type.__name__=_J
_CmATModePermit_Object=MibTableColumn
cmATModePermit=_CmATModePermit_Object((1,3,6,1,4,1,9,9,47,1,3,2,1,1),_CmATModePermit_Type())
cmATModePermit.setMaxAccess(_F)
if mibBuilder.loadTexts:cmATModePermit.setStatus(_B)
class _CmStatusPolling_Type(TruthValue):defaultValue=1
_CmStatusPolling_Type.__name__=_J
_CmStatusPolling_Object=MibTableColumn
cmStatusPolling=_CmStatusPolling_Object((1,3,6,1,4,1,9,9,47,1,3,2,1,2),_CmStatusPolling_Type())
cmStatusPolling.setMaxAccess(_F)
if mibBuilder.loadTexts:cmStatusPolling.setStatus(_B)
class _CmBusyOutRequest_Type(TruthValue):defaultValue=2
_CmBusyOutRequest_Type.__name__=_J
_CmBusyOutRequest_Object=MibTableColumn
cmBusyOutRequest=_CmBusyOutRequest_Object((1,3,6,1,4,1,9,9,47,1,3,2,1,3),_CmBusyOutRequest_Type())
cmBusyOutRequest.setMaxAccess(_F)
if mibBuilder.loadTexts:cmBusyOutRequest.setStatus(_B)
class _CmShutdown_Type(TruthValue):defaultValue=2
_CmShutdown_Type.__name__=_J
_CmShutdown_Object=MibTableColumn
cmShutdown=_CmShutdown_Object((1,3,6,1,4,1,9,9,47,1,3,2,1,4),_CmShutdown_Type())
cmShutdown.setMaxAccess(_F)
if mibBuilder.loadTexts:cmShutdown.setStatus(_B)
class _CmHoldReset_Type(TruthValue):defaultValue=2
_CmHoldReset_Type.__name__=_J
_CmHoldReset_Object=MibTableColumn
cmHoldReset=_CmHoldReset_Object((1,3,6,1,4,1,9,9,47,1,3,2,1,5),_CmHoldReset_Type())
cmHoldReset.setMaxAccess(_F)
if mibBuilder.loadTexts:cmHoldReset.setStatus(_B)
class _CmBad_Type(TruthValue):defaultValue=2
_CmBad_Type.__name__=_J
_CmBad_Object=MibTableColumn
cmBad=_CmBad_Object((1,3,6,1,4,1,9,9,47,1,3,2,1,6),_CmBad_Type())
cmBad.setMaxAccess(_F)
if mibBuilder.loadTexts:cmBad.setStatus(_B)
_CmLineStatisticsTable_Object=MibTable
cmLineStatisticsTable=_CmLineStatisticsTable_Object((1,3,6,1,4,1,9,9,47,1,3,3))
if mibBuilder.loadTexts:cmLineStatisticsTable.setStatus(_B)
_CmLineStatisticsEntry_Object=MibTableRow
cmLineStatisticsEntry=_CmLineStatisticsEntry_Object((1,3,6,1,4,1,9,9,47,1,3,3,1))
if mibBuilder.loadTexts:cmLineStatisticsEntry.setStatus(_B)
_CmRingNoAnswers_Type=Counter32
_CmRingNoAnswers_Object=MibTableColumn
cmRingNoAnswers=_CmRingNoAnswers_Object((1,3,6,1,4,1,9,9,47,1,3,3,1,1),_CmRingNoAnswers_Type())
cmRingNoAnswers.setMaxAccess(_C)
if mibBuilder.loadTexts:cmRingNoAnswers.setStatus(_B)
if mibBuilder.loadTexts:cmRingNoAnswers.setUnits(_D)
_CmIncomingConnectionFailures_Type=Counter32
_CmIncomingConnectionFailures_Object=MibTableColumn
cmIncomingConnectionFailures=_CmIncomingConnectionFailures_Object((1,3,6,1,4,1,9,9,47,1,3,3,1,2),_CmIncomingConnectionFailures_Type())
cmIncomingConnectionFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cmIncomingConnectionFailures.setStatus(_B)
if mibBuilder.loadTexts:cmIncomingConnectionFailures.setUnits(_D)
_CmIncomingConnectionCompletions_Type=Counter32
_CmIncomingConnectionCompletions_Object=MibTableColumn
cmIncomingConnectionCompletions=_CmIncomingConnectionCompletions_Object((1,3,6,1,4,1,9,9,47,1,3,3,1,3),_CmIncomingConnectionCompletions_Type())
cmIncomingConnectionCompletions.setMaxAccess(_C)
if mibBuilder.loadTexts:cmIncomingConnectionCompletions.setStatus(_B)
if mibBuilder.loadTexts:cmIncomingConnectionCompletions.setUnits(_D)
_CmOutgoingConnectionFailures_Type=Counter32
_CmOutgoingConnectionFailures_Object=MibTableColumn
cmOutgoingConnectionFailures=_CmOutgoingConnectionFailures_Object((1,3,6,1,4,1,9,9,47,1,3,3,1,4),_CmOutgoingConnectionFailures_Type())
cmOutgoingConnectionFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cmOutgoingConnectionFailures.setStatus(_B)
if mibBuilder.loadTexts:cmOutgoingConnectionFailures.setUnits(_D)
_CmOutgoingConnectionCompletions_Type=Counter32
_CmOutgoingConnectionCompletions_Object=MibTableColumn
cmOutgoingConnectionCompletions=_CmOutgoingConnectionCompletions_Object((1,3,6,1,4,1,9,9,47,1,3,3,1,5),_CmOutgoingConnectionCompletions_Type())
cmOutgoingConnectionCompletions.setMaxAccess(_C)
if mibBuilder.loadTexts:cmOutgoingConnectionCompletions.setStatus(_B)
if mibBuilder.loadTexts:cmOutgoingConnectionCompletions.setUnits(_D)
_CmFailedDialAttempts_Type=Counter32
_CmFailedDialAttempts_Object=MibTableColumn
cmFailedDialAttempts=_CmFailedDialAttempts_Object((1,3,6,1,4,1,9,9,47,1,3,3,1,6),_CmFailedDialAttempts_Type())
cmFailedDialAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:cmFailedDialAttempts.setStatus(_B)
if mibBuilder.loadTexts:cmFailedDialAttempts.setUnits(_D)
_CmNoDialTones_Type=Counter32
_CmNoDialTones_Object=MibTableColumn
cmNoDialTones=_CmNoDialTones_Object((1,3,6,1,4,1,9,9,47,1,3,3,1,7),_CmNoDialTones_Type())
cmNoDialTones.setMaxAccess(_C)
if mibBuilder.loadTexts:cmNoDialTones.setStatus(_B)
if mibBuilder.loadTexts:cmNoDialTones.setUnits(_D)
_CmDialTimeouts_Type=Counter32
_CmDialTimeouts_Object=MibTableColumn
cmDialTimeouts=_CmDialTimeouts_Object((1,3,6,1,4,1,9,9,47,1,3,3,1,8),_CmDialTimeouts_Type())
cmDialTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:cmDialTimeouts.setStatus(_B)
if mibBuilder.loadTexts:cmDialTimeouts.setUnits(_D)
_CmWatchdogTimeouts_Type=Counter32
_CmWatchdogTimeouts_Object=MibTableColumn
cmWatchdogTimeouts=_CmWatchdogTimeouts_Object((1,3,6,1,4,1,9,9,47,1,3,3,1,9),_CmWatchdogTimeouts_Type())
cmWatchdogTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:cmWatchdogTimeouts.setStatus(_B)
if mibBuilder.loadTexts:cmWatchdogTimeouts.setUnits(_D)
_Cm2400OrLessConnections_Type=Counter32
_Cm2400OrLessConnections_Object=MibTableColumn
cm2400OrLessConnections=_Cm2400OrLessConnections_Object((1,3,6,1,4,1,9,9,47,1,3,3,1,10),_Cm2400OrLessConnections_Type())
cm2400OrLessConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:cm2400OrLessConnections.setStatus(_G)
if mibBuilder.loadTexts:cm2400OrLessConnections.setUnits(_D)
_Cm2400To14400Connections_Type=Counter32
_Cm2400To14400Connections_Object=MibTableColumn
cm2400To14400Connections=_Cm2400To14400Connections_Object((1,3,6,1,4,1,9,9,47,1,3,3,1,11),_Cm2400To14400Connections_Type())
cm2400To14400Connections.setMaxAccess(_C)
if mibBuilder.loadTexts:cm2400To14400Connections.setStatus(_G)
if mibBuilder.loadTexts:cm2400To14400Connections.setUnits(_D)
_CmGreaterThan14400Connections_Type=Counter32
_CmGreaterThan14400Connections_Object=MibTableColumn
cmGreaterThan14400Connections=_CmGreaterThan14400Connections_Object((1,3,6,1,4,1,9,9,47,1,3,3,1,12),_CmGreaterThan14400Connections_Type())
cmGreaterThan14400Connections.setMaxAccess(_C)
if mibBuilder.loadTexts:cmGreaterThan14400Connections.setStatus(_G)
if mibBuilder.loadTexts:cmGreaterThan14400Connections.setUnits(_D)
_CmNoCarriers_Type=Counter32
_CmNoCarriers_Object=MibTableColumn
cmNoCarriers=_CmNoCarriers_Object((1,3,6,1,4,1,9,9,47,1,3,3,1,13),_CmNoCarriers_Type())
cmNoCarriers.setMaxAccess(_C)
if mibBuilder.loadTexts:cmNoCarriers.setStatus(_B)
if mibBuilder.loadTexts:cmNoCarriers.setUnits(_D)
_CmLinkFailures_Type=Counter32
_CmLinkFailures_Object=MibTableColumn
cmLinkFailures=_CmLinkFailures_Object((1,3,6,1,4,1,9,9,47,1,3,3,1,14),_CmLinkFailures_Type())
cmLinkFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cmLinkFailures.setStatus(_B)
if mibBuilder.loadTexts:cmLinkFailures.setUnits(_D)
_CmProtocolErrors_Type=Counter32
_CmProtocolErrors_Object=MibTableColumn
cmProtocolErrors=_CmProtocolErrors_Object((1,3,6,1,4,1,9,9,47,1,3,3,1,15),_CmProtocolErrors_Type())
cmProtocolErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cmProtocolErrors.setStatus(_B)
if mibBuilder.loadTexts:cmProtocolErrors.setUnits('errors')
_CmPollingTimeouts_Type=Counter32
_CmPollingTimeouts_Object=MibTableColumn
cmPollingTimeouts=_CmPollingTimeouts_Object((1,3,6,1,4,1,9,9,47,1,3,3,1,16),_CmPollingTimeouts_Type())
cmPollingTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:cmPollingTimeouts.setStatus(_B)
if mibBuilder.loadTexts:cmPollingTimeouts.setUnits('errors')
_CmTotalCallDuration_Type=Counter32
_CmTotalCallDuration_Object=MibTableColumn
cmTotalCallDuration=_CmTotalCallDuration_Object((1,3,6,1,4,1,9,9,47,1,3,3,1,17),_CmTotalCallDuration_Type())
cmTotalCallDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:cmTotalCallDuration.setStatus(_B)
if mibBuilder.loadTexts:cmTotalCallDuration.setUnits('seconds')
_CmLineSpeedStatisticsTable_Object=MibTable
cmLineSpeedStatisticsTable=_CmLineSpeedStatisticsTable_Object((1,3,6,1,4,1,9,9,47,1,3,4))
if mibBuilder.loadTexts:cmLineSpeedStatisticsTable.setStatus(_B)
_CmLineSpeedStatisticsEntry_Object=MibTableRow
cmLineSpeedStatisticsEntry=_CmLineSpeedStatisticsEntry_Object((1,3,6,1,4,1,9,9,47,1,3,4,1))
cmLineSpeedStatisticsEntry.setIndexNames((0,_A,_P),(0,_A,_O),(0,_A,_A2))
if mibBuilder.loadTexts:cmLineSpeedStatisticsEntry.setStatus(_B)
_CmInitialLineSpeed_Type=Unsigned32
_CmInitialLineSpeed_Object=MibTableColumn
cmInitialLineSpeed=_CmInitialLineSpeed_Object((1,3,6,1,4,1,9,9,47,1,3,4,1,1),_CmInitialLineSpeed_Type())
cmInitialLineSpeed.setMaxAccess(_k)
if mibBuilder.loadTexts:cmInitialLineSpeed.setStatus(_B)
_CmInitialLineConnections_Type=Counter32
_CmInitialLineConnections_Object=MibTableColumn
cmInitialLineConnections=_CmInitialLineConnections_Object((1,3,6,1,4,1,9,9,47,1,3,4,1,2),_CmInitialLineConnections_Type())
cmInitialLineConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:cmInitialLineConnections.setStatus(_G)
if mibBuilder.loadTexts:cmInitialLineConnections.setUnits(_D)
_CmInitialTxLineConnections_Type=Counter32
_CmInitialTxLineConnections_Object=MibTableColumn
cmInitialTxLineConnections=_CmInitialTxLineConnections_Object((1,3,6,1,4,1,9,9,47,1,3,4,1,3),_CmInitialTxLineConnections_Type())
cmInitialTxLineConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:cmInitialTxLineConnections.setStatus(_B)
if mibBuilder.loadTexts:cmInitialTxLineConnections.setUnits(_D)
_CmInitialRxLineConnections_Type=Counter32
_CmInitialRxLineConnections_Object=MibTableColumn
cmInitialRxLineConnections=_CmInitialRxLineConnections_Object((1,3,6,1,4,1,9,9,47,1,3,4,1,4),_CmInitialRxLineConnections_Type())
cmInitialRxLineConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:cmInitialRxLineConnections.setStatus(_B)
if mibBuilder.loadTexts:cmInitialRxLineConnections.setUnits(_D)
_CmNotificationConfig_ObjectIdentity=ObjectIdentity
cmNotificationConfig=_CmNotificationConfig_ObjectIdentity((1,3,6,1,4,1,9,9,47,1,4))
_CmStateNotifyEnable_Type=TruthValue
_CmStateNotifyEnable_Object=MibScalar
cmStateNotifyEnable=_CmStateNotifyEnable_Object((1,3,6,1,4,1,9,9,47,1,4,1),_CmStateNotifyEnable_Type())
cmStateNotifyEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:cmStateNotifyEnable.setStatus(_B)
_CmMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
cmMIBNotificationPrefix=_CmMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,47,2))
_CmMIBNotifications_ObjectIdentity=ObjectIdentity
cmMIBNotifications=_CmMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,47,2,0))
_CiscoModemMgmtMIBConformance_ObjectIdentity=ObjectIdentity
ciscoModemMgmtMIBConformance=_CiscoModemMgmtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,47,3))
_CiscoModemMgmtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoModemMgmtMIBCompliances=_CiscoModemMgmtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,47,3,1))
_CiscoModemMgmtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoModemMgmtMIBGroups=_CiscoModemMgmtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,47,3,2))
cmLineStatusEntry.registerAugmentions((_A,_A3))
cmLineConfigEntry.setIndexNames(*cmLineStatusEntry.getIndexNames())
cmLineStatusEntry.registerAugmentions((_A,_A4))
cmLineStatisticsEntry.setIndexNames(*cmLineStatusEntry.getIndexNames())
cmSystemInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,47,3,2,1))
cmSystemInfoGroup.setObjects(*((_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:cmSystemInfoGroup.setStatus(_K)
cmGroupInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,47,3,2,2))
cmGroupInfoGroup.setObjects(*((_A,_A5),(_A,_O)))
if mibBuilder.loadTexts:cmGroupInfoGroup.setStatus(_B)
cmLineInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,47,3,2,3))
cmLineInfoGroup.setObjects(*((_A,_A6),(_A,'cmGroup'),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_q),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,'cmBad'),(_A,_AK),(_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:cmLineInfoGroup.setStatus(_B)
cmManagedLineInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,47,3,2,4))
cmManagedLineInfoGroup.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_r),(_A,_s),(_A,_t),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:cmManagedLineInfoGroup.setStatus(_G)
cmLineSpeedInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,47,3,2,5))
cmLineSpeedInfoGroup.setObjects((_A,_u))
if mibBuilder.loadTexts:cmLineSpeedInfoGroup.setStatus(_K)
cmSystemInfoGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,47,3,2,6))
cmSystemInfoGroupRev1.setObjects(*((_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR)))
if mibBuilder.loadTexts:cmSystemInfoGroupRev1.setStatus(_B)
cmLineSpeedInfoGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,47,3,2,7))
cmLineSpeedInfoGroupRev1.setObjects(*((_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:cmLineSpeedInfoGroupRev1.setStatus(_G)
cmManagedLineInfoGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,47,3,2,8))
cmManagedLineInfoGroupRev1.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_r),(_A,_s),(_A,_t),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:cmManagedLineInfoGroupRev1.setStatus(_G)
cmNotificationConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,47,3,2,9))
cmNotificationConfigGroup.setObjects((_A,_AS))
if mibBuilder.loadTexts:cmNotificationConfigGroup.setStatus(_B)
cmLineSpeedInfoGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,47,3,2,11))
cmLineSpeedInfoGroupRev2.setObjects(*((_A,_v),(_A,_w)))
if mibBuilder.loadTexts:cmLineSpeedInfoGroupRev2.setStatus(_B)
cmManagedLineInfoGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,47,3,2,12))
cmManagedLineInfoGroupRev2.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:cmManagedLineInfoGroupRev2.setStatus(_B)
cmStateNotification=NotificationType((1,3,6,1,4,1,9,9,47,2,0,1))
cmStateNotification.setObjects((_A,_q))
if mibBuilder.loadTexts:cmStateNotification.setStatus(_B)
cmNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,47,3,2,10))
cmNotificationGroup.setObjects((_A,_AT))
if mibBuilder.loadTexts:cmNotificationGroup.setStatus(_B)
ciscoModemMgmtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,47,3,1,1))
ciscoModemMgmtMIBCompliance.setObjects(*((_A,_x),(_A,_H),(_A,_I),(_A,_L)))
if mibBuilder.loadTexts:ciscoModemMgmtMIBCompliance.setStatus(_K)
ciscoModemMgmtMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,47,3,1,2))
ciscoModemMgmtMIBComplianceRev1.setObjects(*((_A,_x),(_A,_H),(_A,_I),(_A,_L),(_A,_y)))
if mibBuilder.loadTexts:ciscoModemMgmtMIBComplianceRev1.setStatus(_K)
ciscoModemMgmtMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,47,3,1,3))
ciscoModemMgmtMIBComplianceRev2.setObjects(*((_A,_M),(_A,_H),(_A,_I),(_A,_L),(_A,_y)))
if mibBuilder.loadTexts:ciscoModemMgmtMIBComplianceRev2.setStatus(_K)
ciscoModemMgmtMIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,47,3,1,4))
ciscoModemMgmtMIBComplianceRev3.setObjects(*((_A,_M),(_A,_H),(_A,_I),(_A,_L),(_A,_i)))
if mibBuilder.loadTexts:ciscoModemMgmtMIBComplianceRev3.setStatus(_K)
ciscoModemMgmtMIBComplianceRev4=ModuleCompliance((1,3,6,1,4,1,9,9,47,3,1,5))
ciscoModemMgmtMIBComplianceRev4.setObjects(*((_A,_I),(_A,_i),(_A,_L),(_A,_H),(_A,_M)))
if mibBuilder.loadTexts:ciscoModemMgmtMIBComplianceRev4.setStatus(_K)
ciscoModemMgmtMIBComplianceRev5=ModuleCompliance((1,3,6,1,4,1,9,9,47,3,1,6))
ciscoModemMgmtMIBComplianceRev5.setObjects(*((_A,_I),(_A,_i),(_A,_AU),(_A,_H),(_A,_M),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:ciscoModemMgmtMIBComplianceRev5.setStatus(_G)
ciscoModemMgmtMIBComplianceRev6=ModuleCompliance((1,3,6,1,4,1,9,9,47,3,1,7))
ciscoModemMgmtMIBComplianceRev6.setObjects(*((_A,_I),(_A,_AV),(_A,_AW),(_A,_H),(_A,_M),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:ciscoModemMgmtMIBComplianceRev6.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoModemMgmtMIB':ciscoModemMgmtMIB,'ciscoModemMgmtMIBObjects':ciscoModemMgmtMIBObjects,'cmSystemInfo':cmSystemInfo,_l:cmSystemInstalledModem,_m:cmSystemConfiguredGroup,_n:cmSystemWatchdogTime,_o:cmSystemStatusPollTime,_p:cmSystemMaxRetries,_AN:cmSystemModemsInUse,_AO:cmSystemModemsAvailable,_AP:cmSystemModemsUnavailable,_AQ:cmSystemModemsOffline,_AR:cmSystemModemsDead,'cmGroupInfo':cmGroupInfo,'cmGroupTable':cmGroupTable,'cmGroupEntry':cmGroupEntry,_j:cmGroupIndex,_A5:cmGroupTotalDevices,'cmGroupMemberTable':cmGroupMemberTable,'cmGroupMemberEntry':cmGroupMemberEntry,_P:cmSlotIndex,_O:cmPortIndex,'cmLineInfo':cmLineInfo,'cmLineStatusTable':cmLineStatusTable,'cmLineStatusEntry':cmLineStatusEntry,_A6:cmInterface,'cmGroup':cmGroup,_A7:cmManufacturerID,_A8:cmProductDetails,_A9:cmManageable,_q:cmState,_AB:cmCallDirection,_AA:cmDisconnectReason,_AC:cmCallDuration,_AD:cmCallPhoneNumber,_AE:cmCallerID,_R:cmModulationSchemeUsed,_S:cmProtocolUsed,_T:cmTXRate,_U:cmRXRate,_V:cmTXAnalogSignalLevel,_W:cmRXAnalogSignalLevel,'cmLineConfigTable':cmLineConfigTable,_A3:cmLineConfigEntry,_AF:cmATModePermit,_AG:cmStatusPolling,_AH:cmBusyOutRequest,_AI:cmShutdown,_AJ:cmHoldReset,'cmBad':cmBad,'cmLineStatisticsTable':cmLineStatisticsTable,_A4:cmLineStatisticsEntry,_AK:cmRingNoAnswers,_X:cmIncomingConnectionFailures,_Y:cmIncomingConnectionCompletions,_Z:cmOutgoingConnectionFailures,_a:cmOutgoingConnectionCompletions,_AL:cmFailedDialAttempts,_b:cmNoDialTones,_c:cmDialTimeouts,_AM:cmWatchdogTimeouts,_r:cm2400OrLessConnections,_s:cm2400To14400Connections,_t:cmGreaterThan14400Connections,_d:cmNoCarriers,_e:cmLinkFailures,_f:cmProtocolErrors,_g:cmPollingTimeouts,_h:cmTotalCallDuration,'cmLineSpeedStatisticsTable':cmLineSpeedStatisticsTable,'cmLineSpeedStatisticsEntry':cmLineSpeedStatisticsEntry,_A2:cmInitialLineSpeed,_u:cmInitialLineConnections,_v:cmInitialTxLineConnections,_w:cmInitialRxLineConnections,'cmNotificationConfig':cmNotificationConfig,_AS:cmStateNotifyEnable,'cmMIBNotificationPrefix':cmMIBNotificationPrefix,'cmMIBNotifications':cmMIBNotifications,_AT:cmStateNotification,'ciscoModemMgmtMIBConformance':ciscoModemMgmtMIBConformance,'ciscoModemMgmtMIBCompliances':ciscoModemMgmtMIBCompliances,'ciscoModemMgmtMIBCompliance':ciscoModemMgmtMIBCompliance,'ciscoModemMgmtMIBComplianceRev1':ciscoModemMgmtMIBComplianceRev1,'ciscoModemMgmtMIBComplianceRev2':ciscoModemMgmtMIBComplianceRev2,'ciscoModemMgmtMIBComplianceRev3':ciscoModemMgmtMIBComplianceRev3,'ciscoModemMgmtMIBComplianceRev4':ciscoModemMgmtMIBComplianceRev4,'ciscoModemMgmtMIBComplianceRev5':ciscoModemMgmtMIBComplianceRev5,'ciscoModemMgmtMIBComplianceRev6':ciscoModemMgmtMIBComplianceRev6,'ciscoModemMgmtMIBGroups':ciscoModemMgmtMIBGroups,_x:cmSystemInfoGroup,_I:cmGroupInfoGroup,_H:cmLineInfoGroup,_L:cmManagedLineInfoGroup,_y:cmLineSpeedInfoGroup,_M:cmSystemInfoGroupRev1,_i:cmLineSpeedInfoGroupRev1,_AU:cmManagedLineInfoGroupRev1,_z:cmNotificationConfigGroup,_A0:cmNotificationGroup,_AV:cmLineSpeedInfoGroupRev2,_AW:cmManagedLineInfoGroupRev2})