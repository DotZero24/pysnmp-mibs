_B8='mrtIfGroupV15'
_B7='mrtIfGroupV14'
_B6='mrtIfGroupV13'
_B5='mrtIfGroupV12'
_B4='mrtIfGroupV11'
_B3='mrtIfGroupV10'
_B2='mrtIfGroupV9'
_B1='mrtIfGroupV8'
_B0='mrtIfGroupV7'
_A_='mrtIfGroupV6'
_Az='mrtIfGroupV5'
_Ay='mrtIfGroupV3'
_Ax='mrtIfGroupV2'
_Aw='mrtGeneralGroup'
_Av='mrtIfTxSignalStatusDegraded'
_Au='mrtIfRxSignalStatus'
_At='mrtIfHighSpeed2'
_As='mrtGeneralMrtIfTableSize'
_Ar='mrtIfTruncVc4Status'
_Aq='mrtGeneralMibImplVersion'
_Ap='mrtGeneralMibSpecVersion'
_Ao='mrtGeneralTestAndIncr'
_An='TestAndIncr'
_Am='SignalFormat'
_Al='LambdaFrequency'
_Ak='BoardOrInterfaceOperStatus'
_Aj='BoardOrInterfaceAdminStatus'
_Ai='OctetString'
_Ah='mrtIfGroupV16'
_Ag='mrtIfGroupV4'
_Af='mrtIfGroup'
_Ae='mrtIfTxSignalStatusUp'
_Ad='mrtIfTxSignalStatusDown'
_Ac='mrtGeneralStateLastChangeTime'
_Ab='Gauge32'
_Aa='mrtIfLaserTempActual'
_AZ='mrtIfTxPowerLevel'
_AY='mrtIfObjectProperty'
_AX='mrtIfUnavailableSeconds'
_AW='mrtIfBackgroundBlockErrors'
_AV='mrtIfSeverelyErroredSeconds'
_AU='mrtIfErroredSeconds'
_AT='read-create'
_AS='mrtGeneralGroupV2'
_AR='mrtIfTruncAutoNegotiationMode'
_AQ='mrtGeneralLastChangeTime'
_AP='mrtIfLaserForcedOn'
_AO='mrtIfTrxMediaMismatch'
_AN='mrtIfTrxMedia'
_AM='Unsigned32'
_AL='mrtGeneralGroupV4'
_AK='mrtIfIllegalFrequency'
_AJ='mrtIfUnexpectedTxFrequency'
_AI='mrtIfTxFrequency'
_AH='mrtIfExpectedTxFrequency'
_AG='mrtIfTrxMode'
_AF='mrtIfConfigureModeCommand'
_AE='mrtIfFarEndLoopback'
_AD='enabled'
_AC='disabled'
_AB='mrtNotificationGroup'
_AA='mrtIfPowerLevelLowRelativeThreshold'
_A9='mrtIfReceiverSensitivity'
_A8='mrtIfTransmitterFailed'
_A7='mrtIfTrxClass'
_A6='mrtIfTrxMissing'
_A5='mrtIfTrxBitrateUnavailable'
_A4='mrtIfTrxCodeMismatch'
_A3='mrtIfConfigurationCommand'
_A2='mrtIfSuppressRemoteAlarms'
_A1='mrtIfForwardAls'
_A0='mrtIfMsAlarmIndicationSignalW2C'
_z='DisplayString'
_y='mrtNotificationGroupV2'
_x='mrtGeneralGroupV3'
_w='mrtIfEntityId'
_v='mrtIfTraceMismatch'
_u='mrtIfTraceAlarmMode'
_t='mrtIfTraceExpected'
_s='mrtIfTraceReceived'
_r='mrtIfTraceTransmitted'
_q='mrtIfTraceIntrusionMode'
_p='mrtIfAuLossOfPointerC2W'
_o='mrtIfAuAlarmIndicationSignalC2W'
_n='mrtIfTruncVc4'
_m='mrtIfAuLossOfPointerW2C'
_l='mrtIfAuAlarmIndicationSignalW2C'
_k='mrtIfJ0PathTrace'
_j='mrtIfLaserBiasThreshold'
_i='mrtIfLaserBias'
_h='Integer32'
_g='mrtIfTxSignalStatus'
_f='mrtIfBitrateMismatch'
_e='mrtIfLossOfSync'
_d='mrtIfRemoteDefectIndication'
_c='mrtIfMsAlarmIndicationSignalC2W'
_b='mrtIfLossOfFrame'
_a='mrtIfLaserBiasHigh'
_Z='mrtIfReceivedPowerLow'
_Y='mrtIfReceivedPowerHigh'
_X='mrtIfLossOfSignal'
_W='mrtIfOperStatus'
_V='mrtIfAdminStatus'
_U='mrtIfLaserStatus'
_T='mrtIfPowerLevelLowThreshold'
_S='mrtIfPowerLevelHighThreshold'
_R='mrtIfPowerLevel'
_Q='mrtIfHighSpeedMax'
_P='mrtIfHighSpeedMin'
_O='mrtIfHighSpeed'
_N='mrtIfFormat'
_M='mrtIfInvPhysIndexOrZero'
_L='mrtIfDescr'
_K='mrtIfRxPort'
_J='mrtIfTxPort'
_I='mrtIfSlot'
_H='mrtIfSubrack'
_G='mrtIfName'
_F='mrtIfIndex'
_E='read-write'
_D='deprecated'
_C='read-only'
_B='current'
_A='LUM-MULTIRATE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Ai,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumModules,lumMultirateMIB=mibBuilder.importSymbols('LUM-REG','lumModules','lumMultirateMIB')
BoardOrInterfaceAdminStatus,BoardOrInterfaceOperStatus,CommandString,FaultStatus,LambdaFrequency,MgmtNameString,ObjectProperty,PortNumber,SignalFormat,SlotNumber,SubrackNumber,TrxMedia=mibBuilder.importSymbols('LUM-TC',_Aj,_Ak,'CommandString','FaultStatus',_Al,'MgmtNameString','ObjectProperty','PortNumber',_Am,'SlotNumber','SubrackNumber','TrxMedia')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_Ab,_h,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_AM,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TestAndIncr=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_z,'PhysAddress','TextualConvention',_An)
lumMultirateMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,13))
if mibBuilder.loadTexts:lumMultirateMIBModule.setRevisions(('2017-06-15 00:00','2016-01-11 00:00','2011-04-12 00:00','2007-11-12 00:00','2003-01-29 00:00','2002-12-04 00:00','2002-10-01 00:00','2002-06-04 00:00','2002-05-15 00:00','2002-01-17 00:00','2001-12-03 00:00','2001-11-09 00:00','2001-10-30 00:00','2001-10-22 00:00','2001-10-18 00:00','2001-10-11 00:00','2001-09-05 00:00','2001-08-14 00:00','2001-08-08 00:00'))
_LumMultirateConfs_ObjectIdentity=ObjectIdentity
lumMultirateConfs=_LumMultirateConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,12,1))
_LumMultirateGroups_ObjectIdentity=ObjectIdentity
lumMultirateGroups=_LumMultirateGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,12,1,1))
_LumMultirateCompl_ObjectIdentity=ObjectIdentity
lumMultirateCompl=_LumMultirateCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,12,1,2))
_LumMultirateMIBObjects_ObjectIdentity=ObjectIdentity
lumMultirateMIBObjects=_LumMultirateMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,12,2))
_MrtGeneral_ObjectIdentity=ObjectIdentity
mrtGeneral=_MrtGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,12,2,1))
class _MrtGeneralTestAndIncr_Type(TestAndIncr):defaultValue=1
_MrtGeneralTestAndIncr_Type.__name__=_An
_MrtGeneralTestAndIncr_Object=MibScalar
mrtGeneralTestAndIncr=_MrtGeneralTestAndIncr_Object((1,3,6,1,4,1,8708,2,12,2,1,1),_MrtGeneralTestAndIncr_Type())
mrtGeneralTestAndIncr.setMaxAccess(_E)
if mibBuilder.loadTexts:mrtGeneralTestAndIncr.setStatus(_B)
class _MrtGeneralMibSpecVersion_Type(DisplayString):defaultValue=OctetString('')
_MrtGeneralMibSpecVersion_Type.__name__=_z
_MrtGeneralMibSpecVersion_Object=MibScalar
mrtGeneralMibSpecVersion=_MrtGeneralMibSpecVersion_Object((1,3,6,1,4,1,8708,2,12,2,1,2),_MrtGeneralMibSpecVersion_Type())
mrtGeneralMibSpecVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:mrtGeneralMibSpecVersion.setStatus(_B)
class _MrtGeneralMibImplVersion_Type(DisplayString):defaultValue=OctetString('')
_MrtGeneralMibImplVersion_Type.__name__=_z
_MrtGeneralMibImplVersion_Object=MibScalar
mrtGeneralMibImplVersion=_MrtGeneralMibImplVersion_Object((1,3,6,1,4,1,8708,2,12,2,1,3),_MrtGeneralMibImplVersion_Type())
mrtGeneralMibImplVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:mrtGeneralMibImplVersion.setStatus(_B)
_MrtGeneralLastChangeTime_Type=DateAndTime
_MrtGeneralLastChangeTime_Object=MibScalar
mrtGeneralLastChangeTime=_MrtGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,12,2,1,4),_MrtGeneralLastChangeTime_Type())
mrtGeneralLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtGeneralLastChangeTime.setStatus(_B)
_MrtGeneralStateLastChangeTime_Type=DateAndTime
_MrtGeneralStateLastChangeTime_Object=MibScalar
mrtGeneralStateLastChangeTime=_MrtGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,12,2,1,5),_MrtGeneralStateLastChangeTime_Type())
mrtGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtGeneralStateLastChangeTime.setStatus(_B)
_MrtGeneralMrtIfTableSize_Type=Unsigned32
_MrtGeneralMrtIfTableSize_Object=MibScalar
mrtGeneralMrtIfTableSize=_MrtGeneralMrtIfTableSize_Object((1,3,6,1,4,1,8708,2,12,2,1,6),_MrtGeneralMrtIfTableSize_Type())
mrtGeneralMrtIfTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtGeneralMrtIfTableSize.setStatus(_B)
_MrtIfList_ObjectIdentity=ObjectIdentity
mrtIfList=_MrtIfList_ObjectIdentity((1,3,6,1,4,1,8708,2,12,2,2))
_MrtIfTable_Object=MibTable
mrtIfTable=_MrtIfTable_Object((1,3,6,1,4,1,8708,2,12,2,2,1))
if mibBuilder.loadTexts:mrtIfTable.setStatus(_B)
_MrtIfEntry_Object=MibTableRow
mrtIfEntry=_MrtIfEntry_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1))
mrtIfEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:mrtIfEntry.setStatus(_B)
class _MrtIfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MrtIfIndex_Type.__name__=_AM
_MrtIfIndex_Object=MibTableColumn
mrtIfIndex=_MrtIfIndex_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,1),_MrtIfIndex_Type())
mrtIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfIndex.setStatus(_B)
_MrtIfName_Type=MgmtNameString
_MrtIfName_Object=MibTableColumn
mrtIfName=_MrtIfName_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,2),_MrtIfName_Type())
mrtIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfName.setStatus(_B)
class _MrtIfDescr_Type(DisplayString):defaultValue=OctetString('')
_MrtIfDescr_Type.__name__=_z
_MrtIfDescr_Object=MibTableColumn
mrtIfDescr=_MrtIfDescr_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,3),_MrtIfDescr_Type())
mrtIfDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:mrtIfDescr.setStatus(_B)
_MrtIfSubrack_Type=SubrackNumber
_MrtIfSubrack_Object=MibTableColumn
mrtIfSubrack=_MrtIfSubrack_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,4),_MrtIfSubrack_Type())
mrtIfSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfSubrack.setStatus(_B)
_MrtIfSlot_Type=SlotNumber
_MrtIfSlot_Object=MibTableColumn
mrtIfSlot=_MrtIfSlot_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,5),_MrtIfSlot_Type())
mrtIfSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfSlot.setStatus(_B)
_MrtIfTxPort_Type=PortNumber
_MrtIfTxPort_Object=MibTableColumn
mrtIfTxPort=_MrtIfTxPort_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,6),_MrtIfTxPort_Type())
mrtIfTxPort.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfTxPort.setStatus(_B)
_MrtIfRxPort_Type=PortNumber
_MrtIfRxPort_Object=MibTableColumn
mrtIfRxPort=_MrtIfRxPort_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,7),_MrtIfRxPort_Type())
mrtIfRxPort.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfRxPort.setStatus(_B)
class _MrtIfInvPhysIndexOrZero_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MrtIfInvPhysIndexOrZero_Type.__name__=_AM
_MrtIfInvPhysIndexOrZero_Object=MibTableColumn
mrtIfInvPhysIndexOrZero=_MrtIfInvPhysIndexOrZero_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,8),_MrtIfInvPhysIndexOrZero_Type())
mrtIfInvPhysIndexOrZero.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfInvPhysIndexOrZero.setStatus(_B)
class _MrtIfFormat_Type(SignalFormat):defaultValue=4
_MrtIfFormat_Type.__name__=_Am
_MrtIfFormat_Object=MibTableColumn
mrtIfFormat=_MrtIfFormat_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,9),_MrtIfFormat_Type())
mrtIfFormat.setMaxAccess(_AT)
if mibBuilder.loadTexts:mrtIfFormat.setStatus(_B)
class _MrtIfHighSpeed_Type(Gauge32):defaultValue=2500;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(125,2500))
_MrtIfHighSpeed_Type.__name__=_Ab
_MrtIfHighSpeed_Object=MibTableColumn
mrtIfHighSpeed=_MrtIfHighSpeed_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,10),_MrtIfHighSpeed_Type())
mrtIfHighSpeed.setMaxAccess(_AT)
if mibBuilder.loadTexts:mrtIfHighSpeed.setStatus(_B)
_MrtIfHighSpeedMin_Type=Gauge32
_MrtIfHighSpeedMin_Object=MibTableColumn
mrtIfHighSpeedMin=_MrtIfHighSpeedMin_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,11),_MrtIfHighSpeedMin_Type())
mrtIfHighSpeedMin.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfHighSpeedMin.setStatus(_B)
_MrtIfHighSpeedMax_Type=Gauge32
_MrtIfHighSpeedMax_Object=MibTableColumn
mrtIfHighSpeedMax=_MrtIfHighSpeedMax_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,12),_MrtIfHighSpeedMax_Type())
mrtIfHighSpeedMax.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfHighSpeedMax.setStatus(_B)
_MrtIfPowerLevel_Type=Integer32
_MrtIfPowerLevel_Object=MibTableColumn
mrtIfPowerLevel=_MrtIfPowerLevel_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,13),_MrtIfPowerLevel_Type())
mrtIfPowerLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfPowerLevel.setStatus(_B)
class _MrtIfPowerLevelHighThreshold_Type(Integer32):defaultValue=-80;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-280,0))
_MrtIfPowerLevelHighThreshold_Type.__name__=_h
_MrtIfPowerLevelHighThreshold_Object=MibTableColumn
mrtIfPowerLevelHighThreshold=_MrtIfPowerLevelHighThreshold_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,14),_MrtIfPowerLevelHighThreshold_Type())
mrtIfPowerLevelHighThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:mrtIfPowerLevelHighThreshold.setStatus(_B)
class _MrtIfPowerLevelLowThreshold_Type(Integer32):defaultValue=-200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-280,0))
_MrtIfPowerLevelLowThreshold_Type.__name__=_h
_MrtIfPowerLevelLowThreshold_Object=MibTableColumn
mrtIfPowerLevelLowThreshold=_MrtIfPowerLevelLowThreshold_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,15),_MrtIfPowerLevelLowThreshold_Type())
mrtIfPowerLevelLowThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:mrtIfPowerLevelLowThreshold.setStatus(_B)
class _MrtIfLaserStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_MrtIfLaserStatus_Type.__name__=_h
_MrtIfLaserStatus_Object=MibTableColumn
mrtIfLaserStatus=_MrtIfLaserStatus_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,16),_MrtIfLaserStatus_Type())
mrtIfLaserStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfLaserStatus.setStatus(_B)
class _MrtIfAdminStatus_Type(BoardOrInterfaceAdminStatus):defaultValue=3
_MrtIfAdminStatus_Type.__name__=_Aj
_MrtIfAdminStatus_Object=MibTableColumn
mrtIfAdminStatus=_MrtIfAdminStatus_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,17),_MrtIfAdminStatus_Type())
mrtIfAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:mrtIfAdminStatus.setStatus(_B)
class _MrtIfOperStatus_Type(BoardOrInterfaceOperStatus):defaultValue=1
_MrtIfOperStatus_Type.__name__=_Ak
_MrtIfOperStatus_Object=MibTableColumn
mrtIfOperStatus=_MrtIfOperStatus_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,18),_MrtIfOperStatus_Type())
mrtIfOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfOperStatus.setStatus(_B)
_MrtIfLossOfSignal_Type=FaultStatus
_MrtIfLossOfSignal_Object=MibTableColumn
mrtIfLossOfSignal=_MrtIfLossOfSignal_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,19),_MrtIfLossOfSignal_Type())
mrtIfLossOfSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfLossOfSignal.setStatus(_B)
_MrtIfReceivedPowerHigh_Type=FaultStatus
_MrtIfReceivedPowerHigh_Object=MibTableColumn
mrtIfReceivedPowerHigh=_MrtIfReceivedPowerHigh_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,20),_MrtIfReceivedPowerHigh_Type())
mrtIfReceivedPowerHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfReceivedPowerHigh.setStatus(_B)
_MrtIfReceivedPowerLow_Type=FaultStatus
_MrtIfReceivedPowerLow_Object=MibTableColumn
mrtIfReceivedPowerLow=_MrtIfReceivedPowerLow_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,21),_MrtIfReceivedPowerLow_Type())
mrtIfReceivedPowerLow.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfReceivedPowerLow.setStatus(_B)
_MrtIfLaserBiasHigh_Type=FaultStatus
_MrtIfLaserBiasHigh_Object=MibTableColumn
mrtIfLaserBiasHigh=_MrtIfLaserBiasHigh_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,22),_MrtIfLaserBiasHigh_Type())
mrtIfLaserBiasHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfLaserBiasHigh.setStatus(_B)
_MrtIfErroredSeconds_Type=FaultStatus
_MrtIfErroredSeconds_Object=MibTableColumn
mrtIfErroredSeconds=_MrtIfErroredSeconds_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,23),_MrtIfErroredSeconds_Type())
mrtIfErroredSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfErroredSeconds.setStatus(_D)
_MrtIfSeverelyErroredSeconds_Type=FaultStatus
_MrtIfSeverelyErroredSeconds_Object=MibTableColumn
mrtIfSeverelyErroredSeconds=_MrtIfSeverelyErroredSeconds_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,24),_MrtIfSeverelyErroredSeconds_Type())
mrtIfSeverelyErroredSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfSeverelyErroredSeconds.setStatus(_D)
_MrtIfBackgroundBlockErrors_Type=FaultStatus
_MrtIfBackgroundBlockErrors_Object=MibTableColumn
mrtIfBackgroundBlockErrors=_MrtIfBackgroundBlockErrors_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,25),_MrtIfBackgroundBlockErrors_Type())
mrtIfBackgroundBlockErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfBackgroundBlockErrors.setStatus(_D)
_MrtIfUnavailableSeconds_Type=FaultStatus
_MrtIfUnavailableSeconds_Object=MibTableColumn
mrtIfUnavailableSeconds=_MrtIfUnavailableSeconds_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,26),_MrtIfUnavailableSeconds_Type())
mrtIfUnavailableSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfUnavailableSeconds.setStatus(_D)
_MrtIfLossOfFrame_Type=FaultStatus
_MrtIfLossOfFrame_Object=MibTableColumn
mrtIfLossOfFrame=_MrtIfLossOfFrame_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,27),_MrtIfLossOfFrame_Type())
mrtIfLossOfFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfLossOfFrame.setStatus(_B)
_MrtIfMsAlarmIndicationSignalC2W_Type=FaultStatus
_MrtIfMsAlarmIndicationSignalC2W_Object=MibTableColumn
mrtIfMsAlarmIndicationSignalC2W=_MrtIfMsAlarmIndicationSignalC2W_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,28),_MrtIfMsAlarmIndicationSignalC2W_Type())
mrtIfMsAlarmIndicationSignalC2W.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfMsAlarmIndicationSignalC2W.setStatus(_B)
_MrtIfRemoteDefectIndication_Type=FaultStatus
_MrtIfRemoteDefectIndication_Object=MibTableColumn
mrtIfRemoteDefectIndication=_MrtIfRemoteDefectIndication_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,29),_MrtIfRemoteDefectIndication_Type())
mrtIfRemoteDefectIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfRemoteDefectIndication.setStatus(_B)
_MrtIfLossOfSync_Type=FaultStatus
_MrtIfLossOfSync_Object=MibTableColumn
mrtIfLossOfSync=_MrtIfLossOfSync_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,30),_MrtIfLossOfSync_Type())
mrtIfLossOfSync.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfLossOfSync.setStatus(_B)
_MrtIfBitrateMismatch_Type=FaultStatus
_MrtIfBitrateMismatch_Object=MibTableColumn
mrtIfBitrateMismatch=_MrtIfBitrateMismatch_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,31),_MrtIfBitrateMismatch_Type())
mrtIfBitrateMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfBitrateMismatch.setStatus(_B)
_MrtIfLaserBias_Type=Unsigned32
_MrtIfLaserBias_Object=MibTableColumn
mrtIfLaserBias=_MrtIfLaserBias_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,32),_MrtIfLaserBias_Type())
mrtIfLaserBias.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfLaserBias.setStatus(_B)
class _MrtIfLaserBiasThreshold_Type(Unsigned32):defaultValue=200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_MrtIfLaserBiasThreshold_Type.__name__=_AM
_MrtIfLaserBiasThreshold_Object=MibTableColumn
mrtIfLaserBiasThreshold=_MrtIfLaserBiasThreshold_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,33),_MrtIfLaserBiasThreshold_Type())
mrtIfLaserBiasThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:mrtIfLaserBiasThreshold.setStatus(_B)
class _MrtIfJ0PathTrace_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1),ValueSizeConstraint(16,16))
_MrtIfJ0PathTrace_Type.__name__=_Ai
_MrtIfJ0PathTrace_Object=MibTableColumn
mrtIfJ0PathTrace=_MrtIfJ0PathTrace_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,34),_MrtIfJ0PathTrace_Type())
mrtIfJ0PathTrace.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfJ0PathTrace.setStatus(_B)
_MrtIfAuAlarmIndicationSignalW2C_Type=FaultStatus
_MrtIfAuAlarmIndicationSignalW2C_Object=MibTableColumn
mrtIfAuAlarmIndicationSignalW2C=_MrtIfAuAlarmIndicationSignalW2C_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,35),_MrtIfAuAlarmIndicationSignalW2C_Type())
mrtIfAuAlarmIndicationSignalW2C.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfAuAlarmIndicationSignalW2C.setStatus(_B)
_MrtIfAuLossOfPointerW2C_Type=FaultStatus
_MrtIfAuLossOfPointerW2C_Object=MibTableColumn
mrtIfAuLossOfPointerW2C=_MrtIfAuLossOfPointerW2C_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,36),_MrtIfAuLossOfPointerW2C_Type())
mrtIfAuLossOfPointerW2C.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfAuLossOfPointerW2C.setStatus(_B)
class _MrtIfTxSignalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('down',1),('degraded',2),('up',3)))
_MrtIfTxSignalStatus_Type.__name__=_h
_MrtIfTxSignalStatus_Object=MibTableColumn
mrtIfTxSignalStatus=_MrtIfTxSignalStatus_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,37),_MrtIfTxSignalStatus_Type())
mrtIfTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfTxSignalStatus.setStatus(_B)
class _MrtIfTruncVc4_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_MrtIfTruncVc4_Type.__name__=_AM
_MrtIfTruncVc4_Object=MibTableColumn
mrtIfTruncVc4=_MrtIfTruncVc4_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,38),_MrtIfTruncVc4_Type())
mrtIfTruncVc4.setMaxAccess(_E)
if mibBuilder.loadTexts:mrtIfTruncVc4.setStatus(_B)
_MrtIfAuAlarmIndicationSignalC2W_Type=FaultStatus
_MrtIfAuAlarmIndicationSignalC2W_Object=MibTableColumn
mrtIfAuAlarmIndicationSignalC2W=_MrtIfAuAlarmIndicationSignalC2W_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,39),_MrtIfAuAlarmIndicationSignalC2W_Type())
mrtIfAuAlarmIndicationSignalC2W.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfAuAlarmIndicationSignalC2W.setStatus(_B)
_MrtIfAuLossOfPointerC2W_Type=FaultStatus
_MrtIfAuLossOfPointerC2W_Object=MibTableColumn
mrtIfAuLossOfPointerC2W=_MrtIfAuLossOfPointerC2W_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,40),_MrtIfAuLossOfPointerC2W_Type())
mrtIfAuLossOfPointerC2W.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfAuLossOfPointerC2W.setStatus(_B)
class _MrtIfTraceIntrusionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AC,1),(_AD,2)))
_MrtIfTraceIntrusionMode_Type.__name__=_h
_MrtIfTraceIntrusionMode_Object=MibTableColumn
mrtIfTraceIntrusionMode=_MrtIfTraceIntrusionMode_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,41),_MrtIfTraceIntrusionMode_Type())
mrtIfTraceIntrusionMode.setMaxAccess(_E)
if mibBuilder.loadTexts:mrtIfTraceIntrusionMode.setStatus(_B)
class _MrtIfTraceTransmitted_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_MrtIfTraceTransmitted_Type.__name__=_z
_MrtIfTraceTransmitted_Object=MibTableColumn
mrtIfTraceTransmitted=_MrtIfTraceTransmitted_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,42),_MrtIfTraceTransmitted_Type())
mrtIfTraceTransmitted.setMaxAccess(_E)
if mibBuilder.loadTexts:mrtIfTraceTransmitted.setStatus(_B)
class _MrtIfTraceReceived_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_MrtIfTraceReceived_Type.__name__=_z
_MrtIfTraceReceived_Object=MibTableColumn
mrtIfTraceReceived=_MrtIfTraceReceived_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,43),_MrtIfTraceReceived_Type())
mrtIfTraceReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfTraceReceived.setStatus(_B)
class _MrtIfTraceExpected_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_MrtIfTraceExpected_Type.__name__=_z
_MrtIfTraceExpected_Object=MibTableColumn
mrtIfTraceExpected=_MrtIfTraceExpected_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,44),_MrtIfTraceExpected_Type())
mrtIfTraceExpected.setMaxAccess(_E)
if mibBuilder.loadTexts:mrtIfTraceExpected.setStatus(_B)
class _MrtIfTraceAlarmMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AC,1),(_AD,2)))
_MrtIfTraceAlarmMode_Type.__name__=_h
_MrtIfTraceAlarmMode_Object=MibTableColumn
mrtIfTraceAlarmMode=_MrtIfTraceAlarmMode_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,45),_MrtIfTraceAlarmMode_Type())
mrtIfTraceAlarmMode.setMaxAccess(_E)
if mibBuilder.loadTexts:mrtIfTraceAlarmMode.setStatus(_B)
_MrtIfTraceMismatch_Type=FaultStatus
_MrtIfTraceMismatch_Object=MibTableColumn
mrtIfTraceMismatch=_MrtIfTraceMismatch_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,46),_MrtIfTraceMismatch_Type())
mrtIfTraceMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfTraceMismatch.setStatus(_B)
class _MrtIfTruncVc4Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('undefined',0),('addDrop',1),('passThrough',2),('unconnected',3)))
_MrtIfTruncVc4Status_Type.__name__=_h
_MrtIfTruncVc4Status_Object=MibTableColumn
mrtIfTruncVc4Status=_MrtIfTruncVc4Status_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,47),_MrtIfTruncVc4Status_Type())
mrtIfTruncVc4Status.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfTruncVc4Status.setStatus(_D)
_MrtIfMsAlarmIndicationSignalW2C_Type=FaultStatus
_MrtIfMsAlarmIndicationSignalW2C_Object=MibTableColumn
mrtIfMsAlarmIndicationSignalW2C=_MrtIfMsAlarmIndicationSignalW2C_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,48),_MrtIfMsAlarmIndicationSignalW2C_Type())
mrtIfMsAlarmIndicationSignalW2C.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfMsAlarmIndicationSignalW2C.setStatus(_B)
class _MrtIfForwardAls_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AC,1),(_AD,2)))
_MrtIfForwardAls_Type.__name__=_h
_MrtIfForwardAls_Object=MibTableColumn
mrtIfForwardAls=_MrtIfForwardAls_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,49),_MrtIfForwardAls_Type())
mrtIfForwardAls.setMaxAccess(_E)
if mibBuilder.loadTexts:mrtIfForwardAls.setStatus(_B)
class _MrtIfSuppressRemoteAlarms_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AC,1),(_AD,2)))
_MrtIfSuppressRemoteAlarms_Type.__name__=_h
_MrtIfSuppressRemoteAlarms_Object=MibTableColumn
mrtIfSuppressRemoteAlarms=_MrtIfSuppressRemoteAlarms_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,50),_MrtIfSuppressRemoteAlarms_Type())
mrtIfSuppressRemoteAlarms.setMaxAccess(_E)
if mibBuilder.loadTexts:mrtIfSuppressRemoteAlarms.setStatus(_B)
_MrtIfConfigurationCommand_Type=CommandString
_MrtIfConfigurationCommand_Object=MibTableColumn
mrtIfConfigurationCommand=_MrtIfConfigurationCommand_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,51),_MrtIfConfigurationCommand_Type())
mrtIfConfigurationCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfConfigurationCommand.setStatus(_B)
_MrtIfTrxCodeMismatch_Type=FaultStatus
_MrtIfTrxCodeMismatch_Object=MibTableColumn
mrtIfTrxCodeMismatch=_MrtIfTrxCodeMismatch_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,52),_MrtIfTrxCodeMismatch_Type())
mrtIfTrxCodeMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfTrxCodeMismatch.setStatus(_B)
_MrtIfTrxBitrateUnavailable_Type=FaultStatus
_MrtIfTrxBitrateUnavailable_Object=MibTableColumn
mrtIfTrxBitrateUnavailable=_MrtIfTrxBitrateUnavailable_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,53),_MrtIfTrxBitrateUnavailable_Type())
mrtIfTrxBitrateUnavailable.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfTrxBitrateUnavailable.setStatus(_B)
_MrtIfTrxMissing_Type=FaultStatus
_MrtIfTrxMissing_Object=MibTableColumn
mrtIfTrxMissing=_MrtIfTrxMissing_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,54),_MrtIfTrxMissing_Type())
mrtIfTrxMissing.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfTrxMissing.setStatus(_B)
class _MrtIfTrxClass_Type(DisplayString):defaultValue=OctetString('')
_MrtIfTrxClass_Type.__name__=_z
_MrtIfTrxClass_Object=MibTableColumn
mrtIfTrxClass=_MrtIfTrxClass_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,55),_MrtIfTrxClass_Type())
mrtIfTrxClass.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfTrxClass.setStatus(_B)
class _MrtIfEntityId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MrtIfEntityId_Type.__name__=_AM
_MrtIfEntityId_Object=MibTableColumn
mrtIfEntityId=_MrtIfEntityId_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,56),_MrtIfEntityId_Type())
mrtIfEntityId.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfEntityId.setStatus(_B)
_MrtIfTransmitterFailed_Type=FaultStatus
_MrtIfTransmitterFailed_Object=MibTableColumn
mrtIfTransmitterFailed=_MrtIfTransmitterFailed_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,57),_MrtIfTransmitterFailed_Type())
mrtIfTransmitterFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfTransmitterFailed.setStatus(_B)
_MrtIfReceiverSensitivity_Type=Integer32
_MrtIfReceiverSensitivity_Object=MibTableColumn
mrtIfReceiverSensitivity=_MrtIfReceiverSensitivity_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,58),_MrtIfReceiverSensitivity_Type())
mrtIfReceiverSensitivity.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfReceiverSensitivity.setStatus(_B)
class _MrtIfPowerLevelLowRelativeThreshold_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,100))
_MrtIfPowerLevelLowRelativeThreshold_Type.__name__=_h
_MrtIfPowerLevelLowRelativeThreshold_Object=MibTableColumn
mrtIfPowerLevelLowRelativeThreshold=_MrtIfPowerLevelLowRelativeThreshold_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,59),_MrtIfPowerLevelLowRelativeThreshold_Type())
mrtIfPowerLevelLowRelativeThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:mrtIfPowerLevelLowRelativeThreshold.setStatus(_B)
class _MrtIfFarEndLoopback_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AC,1),(_AD,2)))
_MrtIfFarEndLoopback_Type.__name__=_h
_MrtIfFarEndLoopback_Object=MibTableColumn
mrtIfFarEndLoopback=_MrtIfFarEndLoopback_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,60),_MrtIfFarEndLoopback_Type())
mrtIfFarEndLoopback.setMaxAccess(_E)
if mibBuilder.loadTexts:mrtIfFarEndLoopback.setStatus(_B)
_MrtIfConfigureModeCommand_Type=CommandString
_MrtIfConfigureModeCommand_Object=MibTableColumn
mrtIfConfigureModeCommand=_MrtIfConfigureModeCommand_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,61),_MrtIfConfigureModeCommand_Type())
mrtIfConfigureModeCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfConfigureModeCommand.setStatus(_B)
class _MrtIfTrxMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('client',1),('line',2)))
_MrtIfTrxMode_Type.__name__=_h
_MrtIfTrxMode_Object=MibTableColumn
mrtIfTrxMode=_MrtIfTrxMode_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,62),_MrtIfTrxMode_Type())
mrtIfTrxMode.setMaxAccess(_AT)
if mibBuilder.loadTexts:mrtIfTrxMode.setStatus(_B)
class _MrtIfExpectedTxFrequency_Type(LambdaFrequency):defaultValue=0
_MrtIfExpectedTxFrequency_Type.__name__=_Al
_MrtIfExpectedTxFrequency_Object=MibTableColumn
mrtIfExpectedTxFrequency=_MrtIfExpectedTxFrequency_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,63),_MrtIfExpectedTxFrequency_Type())
mrtIfExpectedTxFrequency.setMaxAccess(_E)
if mibBuilder.loadTexts:mrtIfExpectedTxFrequency.setStatus(_B)
_MrtIfTxFrequency_Type=LambdaFrequency
_MrtIfTxFrequency_Object=MibTableColumn
mrtIfTxFrequency=_MrtIfTxFrequency_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,64),_MrtIfTxFrequency_Type())
mrtIfTxFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfTxFrequency.setStatus(_B)
_MrtIfUnexpectedTxFrequency_Type=FaultStatus
_MrtIfUnexpectedTxFrequency_Object=MibTableColumn
mrtIfUnexpectedTxFrequency=_MrtIfUnexpectedTxFrequency_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,65),_MrtIfUnexpectedTxFrequency_Type())
mrtIfUnexpectedTxFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfUnexpectedTxFrequency.setStatus(_B)
_MrtIfIllegalFrequency_Type=FaultStatus
_MrtIfIllegalFrequency_Object=MibTableColumn
mrtIfIllegalFrequency=_MrtIfIllegalFrequency_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,66),_MrtIfIllegalFrequency_Type())
mrtIfIllegalFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfIllegalFrequency.setStatus(_B)
class _MrtIfTrxMedia_Type(TrxMedia):defaultValue=1
_MrtIfTrxMedia_Type.__name__='TrxMedia'
_MrtIfTrxMedia_Object=MibTableColumn
mrtIfTrxMedia=_MrtIfTrxMedia_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,67),_MrtIfTrxMedia_Type())
mrtIfTrxMedia.setMaxAccess(_AT)
if mibBuilder.loadTexts:mrtIfTrxMedia.setStatus(_B)
_MrtIfTrxMediaMismatch_Type=FaultStatus
_MrtIfTrxMediaMismatch_Object=MibTableColumn
mrtIfTrxMediaMismatch=_MrtIfTrxMediaMismatch_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,68),_MrtIfTrxMediaMismatch_Type())
mrtIfTrxMediaMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfTrxMediaMismatch.setStatus(_B)
class _MrtIfLaserForcedOn_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AC,1),(_AD,2)))
_MrtIfLaserForcedOn_Type.__name__=_h
_MrtIfLaserForcedOn_Object=MibTableColumn
mrtIfLaserForcedOn=_MrtIfLaserForcedOn_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,69),_MrtIfLaserForcedOn_Type())
mrtIfLaserForcedOn.setMaxAccess(_E)
if mibBuilder.loadTexts:mrtIfLaserForcedOn.setStatus(_B)
class _MrtIfTruncAutoNegotiationMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AC,1),(_AD,2)))
_MrtIfTruncAutoNegotiationMode_Type.__name__=_h
_MrtIfTruncAutoNegotiationMode_Object=MibTableColumn
mrtIfTruncAutoNegotiationMode=_MrtIfTruncAutoNegotiationMode_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,70),_MrtIfTruncAutoNegotiationMode_Type())
mrtIfTruncAutoNegotiationMode.setMaxAccess(_E)
if mibBuilder.loadTexts:mrtIfTruncAutoNegotiationMode.setStatus(_B)
_MrtIfObjectProperty_Type=ObjectProperty
_MrtIfObjectProperty_Object=MibTableColumn
mrtIfObjectProperty=_MrtIfObjectProperty_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,71),_MrtIfObjectProperty_Type())
mrtIfObjectProperty.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfObjectProperty.setStatus(_B)
_MrtIfTxPowerLevel_Type=Integer32
_MrtIfTxPowerLevel_Object=MibTableColumn
mrtIfTxPowerLevel=_MrtIfTxPowerLevel_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,72),_MrtIfTxPowerLevel_Type())
mrtIfTxPowerLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfTxPowerLevel.setStatus(_B)
_MrtIfLaserTempActual_Type=Integer32
_MrtIfLaserTempActual_Object=MibTableColumn
mrtIfLaserTempActual=_MrtIfLaserTempActual_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,73),_MrtIfLaserTempActual_Type())
mrtIfLaserTempActual.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfLaserTempActual.setStatus(_B)
class _MrtIfHighSpeed2_Type(Gauge32):defaultValue=250000;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(12500,250000))
_MrtIfHighSpeed2_Type.__name__=_Ab
_MrtIfHighSpeed2_Object=MibTableColumn
mrtIfHighSpeed2=_MrtIfHighSpeed2_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,74),_MrtIfHighSpeed2_Type())
mrtIfHighSpeed2.setMaxAccess(_E)
if mibBuilder.loadTexts:mrtIfHighSpeed2.setStatus(_B)
class _MrtIfRxSignalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('down',1),('degraded',2),('up',3)))
_MrtIfRxSignalStatus_Type.__name__=_h
_MrtIfRxSignalStatus_Object=MibTableColumn
mrtIfRxSignalStatus=_MrtIfRxSignalStatus_Object((1,3,6,1,4,1,8708,2,12,2,2,1,1,75),_MrtIfRxSignalStatus_Type())
mrtIfRxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mrtIfRxSignalStatus.setStatus(_B)
_LumentisMrtNotifications_ObjectIdentity=ObjectIdentity
lumentisMrtNotifications=_LumentisMrtNotifications_ObjectIdentity((1,3,6,1,4,1,8708,2,12,2,3))
_MrtNotifyPrefix_ObjectIdentity=ObjectIdentity
mrtNotifyPrefix=_MrtNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,8708,2,12,2,3,0))
mrtGeneralGroup=ObjectGroup((1,3,6,1,4,1,8708,2,12,1,1,1))
mrtGeneralGroup.setObjects(*((_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_AQ)))
if mibBuilder.loadTexts:mrtGeneralGroup.setStatus(_D)
mrtIfGroup=ObjectGroup((1,3,6,1,4,1,8708,2,12,1,1,2))
mrtIfGroup.setObjects(*((_A,_F),(_A,_G),(_A,_L),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:mrtIfGroup.setStatus(_D)
mrtGeneralGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,12,1,1,3))
mrtGeneralGroupV2.setObjects((_A,_AQ))
if mibBuilder.loadTexts:mrtGeneralGroupV2.setStatus(_D)
mrtIfGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,12,1,1,4))
mrtIfGroupV2.setObjects(*((_A,_F),(_A,_G),(_A,_L),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:mrtIfGroupV2.setStatus(_D)
mrtIfGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,12,1,1,5))
mrtIfGroupV3.setObjects(*((_A,_F),(_A,_G),(_A,_L),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:mrtIfGroupV3.setStatus(_D)
mrtIfGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,12,1,1,6))
mrtIfGroupV4.setObjects(*((_A,_F),(_A,_G),(_A,_L),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_g)))
if mibBuilder.loadTexts:mrtIfGroupV4.setStatus(_D)
mrtGeneralGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,12,1,1,8))
mrtGeneralGroupV3.setObjects(*((_A,_AQ),(_A,_Ac)))
if mibBuilder.loadTexts:mrtGeneralGroupV3.setStatus(_D)
mrtIfGroupV5=ObjectGroup((1,3,6,1,4,1,8708,2,12,1,1,9))
mrtIfGroupV5.setObjects(*((_A,_F),(_A,_G),(_A,_L),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_g),(_A,_n)))
if mibBuilder.loadTexts:mrtIfGroupV5.setStatus(_D)
mrtIfGroupV6=ObjectGroup((1,3,6,1,4,1,8708,2,12,1,1,10))
mrtIfGroupV6.setObjects(*((_A,_F),(_A,_G),(_A,_L),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_g),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:mrtIfGroupV6.setStatus(_B)
mrtIfGroupV7=ObjectGroup((1,3,6,1,4,1,8708,2,12,1,1,11))
mrtIfGroupV7.setObjects(*((_A,_F),(_A,_G),(_A,_L),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_g),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:mrtIfGroupV7.setStatus(_D)
mrtIfGroupV8=ObjectGroup((1,3,6,1,4,1,8708,2,12,1,1,12))
mrtIfGroupV8.setObjects(*((_A,_F),(_A,_G),(_A,_L),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_g),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_Ar)))
if mibBuilder.loadTexts:mrtIfGroupV8.setStatus(_D)
mrtIfGroupV9=ObjectGroup((1,3,6,1,4,1,8708,2,12,1,1,13))
mrtIfGroupV9.setObjects(*((_A,_F),(_A,_G),(_A,_L),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_g),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:mrtIfGroupV9.setStatus(_D)
mrtIfGroupV10=ObjectGroup((1,3,6,1,4,1,8708,2,12,1,1,14))
mrtIfGroupV10.setObjects(*((_A,_F),(_A,_G),(_A,_L),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_A0),(_A,_d),(_A,_e),(_A,_f),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_g),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_w),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:mrtIfGroupV10.setStatus(_D)
mrtIfGroupV11=ObjectGroup((1,3,6,1,4,1,8708,2,12,1,1,16))
mrtIfGroupV11.setObjects(*((_A,_F),(_A,_G),(_A,_L),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_A0),(_A,_d),(_A,_e),(_A,_f),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_g),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_w),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:mrtIfGroupV11.setStatus(_D)
mrtIfGroupV12=ObjectGroup((1,3,6,1,4,1,8708,2,12,1,1,17))
mrtIfGroupV12.setObjects(*((_A,_F),(_A,_G),(_A,_L),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_A0),(_A,_d),(_A,_e),(_A,_f),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_g),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_w),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AN),(_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:mrtIfGroupV12.setStatus(_D)
mrtGeneralGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,12,1,1,18))
mrtGeneralGroupV4.setObjects(*((_A,_AQ),(_A,_Ac),(_A,_As)))
if mibBuilder.loadTexts:mrtGeneralGroupV4.setStatus(_B)
mrtIfGroupV13=ObjectGroup((1,3,6,1,4,1,8708,2,12,1,1,19))
mrtIfGroupV13.setObjects(*((_A,_F),(_A,_G),(_A,_L),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_A0),(_A,_d),(_A,_e),(_A,_f),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_g),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_w),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AR)))
if mibBuilder.loadTexts:mrtIfGroupV13.setStatus(_D)
mrtIfGroupV14=ObjectGroup((1,3,6,1,4,1,8708,2,12,1,1,20))
mrtIfGroupV14.setObjects(*((_A,_F),(_A,_G),(_A,_L),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_A0),(_A,_d),(_A,_e),(_A,_f),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_g),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_w),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AR),(_A,_AY),(_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:mrtIfGroupV14.setStatus(_D)
mrtIfGroupV15=ObjectGroup((1,3,6,1,4,1,8708,2,12,1,1,21))
mrtIfGroupV15.setObjects(*((_A,_F),(_A,_G),(_A,_L),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_A0),(_A,_d),(_A,_e),(_A,_f),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_g),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_w),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AR),(_A,_AY),(_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:mrtIfGroupV15.setStatus(_D)
mrtIfGroupV16=ObjectGroup((1,3,6,1,4,1,8708,2,12,1,1,22))
mrtIfGroupV16.setObjects(*((_A,_F),(_A,_G),(_A,_L),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_A0),(_A,_d),(_A,_e),(_A,_f),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_g),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_w),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AR),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_At),(_A,_Au)))
if mibBuilder.loadTexts:mrtIfGroupV16.setStatus(_B)
mrtIfTxSignalStatusDown=NotificationType((1,3,6,1,4,1,8708,2,12,2,3,0,1))
mrtIfTxSignalStatusDown.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_w),(_A,_g)))
if mibBuilder.loadTexts:mrtIfTxSignalStatusDown.setStatus(_B)
mrtIfTxSignalStatusUp=NotificationType((1,3,6,1,4,1,8708,2,12,2,3,0,2))
mrtIfTxSignalStatusUp.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_w),(_A,_g)))
if mibBuilder.loadTexts:mrtIfTxSignalStatusUp.setStatus(_B)
mrtIfTxSignalStatusDegraded=NotificationType((1,3,6,1,4,1,8708,2,12,2,3,0,3))
mrtIfTxSignalStatusDegraded.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_w),(_A,_g)))
if mibBuilder.loadTexts:mrtIfTxSignalStatusDegraded.setStatus(_B)
mrtNotificationGroup=NotificationGroup((1,3,6,1,4,1,8708,2,12,1,1,7))
mrtNotificationGroup.setObjects(*((_A,_Ad),(_A,_Ae)))
if mibBuilder.loadTexts:mrtNotificationGroup.setStatus(_D)
mrtNotificationGroupV2=NotificationGroup((1,3,6,1,4,1,8708,2,12,1,1,15))
mrtNotificationGroupV2.setObjects(*((_A,_Ad),(_A,_Ae),(_A,_Av)))
if mibBuilder.loadTexts:mrtNotificationGroupV2.setStatus(_B)
lumMultirateBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,12,1,2,1))
lumMultirateBasicComplV1.setObjects(*((_A,_Aw),(_A,_Af)))
if mibBuilder.loadTexts:lumMultirateBasicComplV1.setStatus(_D)
lumMultirateBasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,12,1,2,2))
lumMultirateBasicComplV2.setObjects(*((_A,_AS),(_A,_Af)))
if mibBuilder.loadTexts:lumMultirateBasicComplV2.setStatus(_D)
lumMultirateBasicComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,12,1,2,3))
lumMultirateBasicComplV3.setObjects(*((_A,_AS),(_A,_Ax)))
if mibBuilder.loadTexts:lumMultirateBasicComplV3.setStatus(_D)
lumMultirateBasicComplV4=ModuleCompliance((1,3,6,1,4,1,8708,2,12,1,2,4))
lumMultirateBasicComplV4.setObjects(*((_A,_AS),(_A,_Ay)))
if mibBuilder.loadTexts:lumMultirateBasicComplV4.setStatus(_D)
lumMultirateBasicComplV5=ModuleCompliance((1,3,6,1,4,1,8708,2,12,1,2,5))
lumMultirateBasicComplV5.setObjects(*((_A,_AS),(_A,_Ag),(_A,_AB)))
if mibBuilder.loadTexts:lumMultirateBasicComplV5.setStatus(_D)
lumMultirateBasicComplV6=ModuleCompliance((1,3,6,1,4,1,8708,2,12,1,2,6))
lumMultirateBasicComplV6.setObjects(*((_A,_x),(_A,_Ag),(_A,_AB)))
if mibBuilder.loadTexts:lumMultirateBasicComplV6.setStatus(_D)
lumMultirateBasicComplV7=ModuleCompliance((1,3,6,1,4,1,8708,2,12,1,2,7))
lumMultirateBasicComplV7.setObjects(*((_A,_x),(_A,_Az),(_A,_AB)))
if mibBuilder.loadTexts:lumMultirateBasicComplV7.setStatus(_D)
lumMultirateBasicComplV8=ModuleCompliance((1,3,6,1,4,1,8708,2,12,1,2,8))
lumMultirateBasicComplV8.setObjects(*((_A,_x),(_A,_A_),(_A,_AB)))
if mibBuilder.loadTexts:lumMultirateBasicComplV8.setStatus(_D)
lumMultirateBasicComplV9=ModuleCompliance((1,3,6,1,4,1,8708,2,12,1,2,9))
lumMultirateBasicComplV9.setObjects(*((_A,_x),(_A,_B0),(_A,_AB)))
if mibBuilder.loadTexts:lumMultirateBasicComplV9.setStatus(_D)
lumMultirateBasicComplV10=ModuleCompliance((1,3,6,1,4,1,8708,2,12,1,2,10))
lumMultirateBasicComplV10.setObjects(*((_A,_x),(_A,_B1),(_A,_AB)))
if mibBuilder.loadTexts:lumMultirateBasicComplV10.setStatus(_D)
lumMultirateBasicComplV11=ModuleCompliance((1,3,6,1,4,1,8708,2,12,1,2,11))
lumMultirateBasicComplV11.setObjects(*((_A,_x),(_A,_B2),(_A,_AB)))
if mibBuilder.loadTexts:lumMultirateBasicComplV11.setStatus(_D)
lumMultirateBasicComplV12=ModuleCompliance((1,3,6,1,4,1,8708,2,12,1,2,12))
lumMultirateBasicComplV12.setObjects(*((_A,_x),(_A,_B3),(_A,_y)))
if mibBuilder.loadTexts:lumMultirateBasicComplV12.setStatus(_D)
lumMultirateBasicComplV13=ModuleCompliance((1,3,6,1,4,1,8708,2,12,1,2,13))
lumMultirateBasicComplV13.setObjects(*((_A,_x),(_A,_B4),(_A,_y)))
if mibBuilder.loadTexts:lumMultirateBasicComplV13.setStatus(_D)
lumMultirateBasicComplV14=ModuleCompliance((1,3,6,1,4,1,8708,2,12,1,2,14))
lumMultirateBasicComplV14.setObjects(*((_A,_AL),(_A,_B5),(_A,_y)))
if mibBuilder.loadTexts:lumMultirateBasicComplV14.setStatus(_D)
lumMultirateBasicComplV15=ModuleCompliance((1,3,6,1,4,1,8708,2,12,1,2,15))
lumMultirateBasicComplV15.setObjects(*((_A,_AL),(_A,_B6),(_A,_y)))
if mibBuilder.loadTexts:lumMultirateBasicComplV15.setStatus(_D)
lumMultirateBasicComplV16=ModuleCompliance((1,3,6,1,4,1,8708,2,12,1,2,16))
lumMultirateBasicComplV16.setObjects(*((_A,_AL),(_A,_B7),(_A,_y)))
if mibBuilder.loadTexts:lumMultirateBasicComplV16.setStatus(_D)
lumMultirateBasicComplV17=ModuleCompliance((1,3,6,1,4,1,8708,2,12,1,2,17))
lumMultirateBasicComplV17.setObjects(*((_A,_AL),(_A,_B8),(_A,_y)))
if mibBuilder.loadTexts:lumMultirateBasicComplV17.setStatus(_D)
lumMultirateBasicComplV18=ModuleCompliance((1,3,6,1,4,1,8708,2,12,1,2,18))
lumMultirateBasicComplV18.setObjects(*((_A,_AL),(_A,_Ah),(_A,_y)))
if mibBuilder.loadTexts:lumMultirateBasicComplV18.setStatus(_D)
lumMultirateBasicComplV19=ModuleCompliance((1,3,6,1,4,1,8708,2,12,1,2,19))
lumMultirateBasicComplV19.setObjects(*((_A,_AL),(_A,_Ah),(_A,_y)))
if mibBuilder.loadTexts:lumMultirateBasicComplV19.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumMultirateMIBModule':lumMultirateMIBModule,'lumMultirateConfs':lumMultirateConfs,'lumMultirateGroups':lumMultirateGroups,_Aw:mrtGeneralGroup,_Af:mrtIfGroup,_AS:mrtGeneralGroupV2,_Ax:mrtIfGroupV2,_Ay:mrtIfGroupV3,_Ag:mrtIfGroupV4,_AB:mrtNotificationGroup,_x:mrtGeneralGroupV3,_Az:mrtIfGroupV5,_A_:mrtIfGroupV6,_B0:mrtIfGroupV7,_B1:mrtIfGroupV8,_B2:mrtIfGroupV9,_B3:mrtIfGroupV10,_y:mrtNotificationGroupV2,_B4:mrtIfGroupV11,_B5:mrtIfGroupV12,_AL:mrtGeneralGroupV4,_B6:mrtIfGroupV13,_B7:mrtIfGroupV14,_B8:mrtIfGroupV15,_Ah:mrtIfGroupV16,'lumMultirateCompl':lumMultirateCompl,'lumMultirateBasicComplV1':lumMultirateBasicComplV1,'lumMultirateBasicComplV2':lumMultirateBasicComplV2,'lumMultirateBasicComplV3':lumMultirateBasicComplV3,'lumMultirateBasicComplV4':lumMultirateBasicComplV4,'lumMultirateBasicComplV5':lumMultirateBasicComplV5,'lumMultirateBasicComplV6':lumMultirateBasicComplV6,'lumMultirateBasicComplV7':lumMultirateBasicComplV7,'lumMultirateBasicComplV8':lumMultirateBasicComplV8,'lumMultirateBasicComplV9':lumMultirateBasicComplV9,'lumMultirateBasicComplV10':lumMultirateBasicComplV10,'lumMultirateBasicComplV11':lumMultirateBasicComplV11,'lumMultirateBasicComplV12':lumMultirateBasicComplV12,'lumMultirateBasicComplV13':lumMultirateBasicComplV13,'lumMultirateBasicComplV14':lumMultirateBasicComplV14,'lumMultirateBasicComplV15':lumMultirateBasicComplV15,'lumMultirateBasicComplV16':lumMultirateBasicComplV16,'lumMultirateBasicComplV17':lumMultirateBasicComplV17,'lumMultirateBasicComplV18':lumMultirateBasicComplV18,'lumMultirateBasicComplV19':lumMultirateBasicComplV19,'lumMultirateMIBObjects':lumMultirateMIBObjects,'mrtGeneral':mrtGeneral,_Ao:mrtGeneralTestAndIncr,_Ap:mrtGeneralMibSpecVersion,_Aq:mrtGeneralMibImplVersion,_AQ:mrtGeneralLastChangeTime,_Ac:mrtGeneralStateLastChangeTime,_As:mrtGeneralMrtIfTableSize,'mrtIfList':mrtIfList,'mrtIfTable':mrtIfTable,'mrtIfEntry':mrtIfEntry,_F:mrtIfIndex,_G:mrtIfName,_L:mrtIfDescr,_H:mrtIfSubrack,_I:mrtIfSlot,_J:mrtIfTxPort,_K:mrtIfRxPort,_M:mrtIfInvPhysIndexOrZero,_N:mrtIfFormat,_O:mrtIfHighSpeed,_P:mrtIfHighSpeedMin,_Q:mrtIfHighSpeedMax,_R:mrtIfPowerLevel,_S:mrtIfPowerLevelHighThreshold,_T:mrtIfPowerLevelLowThreshold,_U:mrtIfLaserStatus,_V:mrtIfAdminStatus,_W:mrtIfOperStatus,_X:mrtIfLossOfSignal,_Y:mrtIfReceivedPowerHigh,_Z:mrtIfReceivedPowerLow,_a:mrtIfLaserBiasHigh,_AU:mrtIfErroredSeconds,_AV:mrtIfSeverelyErroredSeconds,_AW:mrtIfBackgroundBlockErrors,_AX:mrtIfUnavailableSeconds,_b:mrtIfLossOfFrame,_c:mrtIfMsAlarmIndicationSignalC2W,_d:mrtIfRemoteDefectIndication,_e:mrtIfLossOfSync,_f:mrtIfBitrateMismatch,_i:mrtIfLaserBias,_j:mrtIfLaserBiasThreshold,_k:mrtIfJ0PathTrace,_l:mrtIfAuAlarmIndicationSignalW2C,_m:mrtIfAuLossOfPointerW2C,_g:mrtIfTxSignalStatus,_n:mrtIfTruncVc4,_o:mrtIfAuAlarmIndicationSignalC2W,_p:mrtIfAuLossOfPointerC2W,_q:mrtIfTraceIntrusionMode,_r:mrtIfTraceTransmitted,_s:mrtIfTraceReceived,_t:mrtIfTraceExpected,_u:mrtIfTraceAlarmMode,_v:mrtIfTraceMismatch,_Ar:mrtIfTruncVc4Status,_A0:mrtIfMsAlarmIndicationSignalW2C,_A1:mrtIfForwardAls,_A2:mrtIfSuppressRemoteAlarms,_A3:mrtIfConfigurationCommand,_A4:mrtIfTrxCodeMismatch,_A5:mrtIfTrxBitrateUnavailable,_A6:mrtIfTrxMissing,_A7:mrtIfTrxClass,_w:mrtIfEntityId,_A8:mrtIfTransmitterFailed,_A9:mrtIfReceiverSensitivity,_AA:mrtIfPowerLevelLowRelativeThreshold,_AE:mrtIfFarEndLoopback,_AF:mrtIfConfigureModeCommand,_AG:mrtIfTrxMode,_AH:mrtIfExpectedTxFrequency,_AI:mrtIfTxFrequency,_AJ:mrtIfUnexpectedTxFrequency,_AK:mrtIfIllegalFrequency,_AN:mrtIfTrxMedia,_AO:mrtIfTrxMediaMismatch,_AP:mrtIfLaserForcedOn,_AR:mrtIfTruncAutoNegotiationMode,_AY:mrtIfObjectProperty,_AZ:mrtIfTxPowerLevel,_Aa:mrtIfLaserTempActual,_At:mrtIfHighSpeed2,_Au:mrtIfRxSignalStatus,'lumentisMrtNotifications':lumentisMrtNotifications,'mrtNotifyPrefix':mrtNotifyPrefix,_Ad:mrtIfTxSignalStatusDown,_Ae:mrtIfTxSignalStatusUp,_Av:mrtIfTxSignalStatusDegraded})