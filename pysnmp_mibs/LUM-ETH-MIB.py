_AH='ethIfGroupV6'
_AG='ethIfGroupV5'
_AF='ethIfGroupV4'
_AE='ethIfGroupV3'
_AD='ethIfGroupV2'
_AC='ethIfGroup'
_AB='ethIfTxSignalStatusDegraded'
_AA='ethIfPowerLevelLowRelativeThreshold'
_A9='ethIfObjectProperty'
_A8='ethGeneralEthIfTableSize'
_A7='ethIfPowerLevelLowThreshold'
_A6='ethIfPowerLevelHighThreshold'
_A5='EthSignalFormat'
_A4='DisplayString'
_A3='BoardOrInterfaceOperStatus'
_A2='BoardOrInterfaceAdminStatus'
_A1='ethGeneralGroupV2'
_A0='ethNotificationGroup'
_z='ethIfTxSignalStatusUp'
_y='ethIfTxSignalStatusDown'
_x='ethGeneralStateLastChangeTime'
_w='ethGeneralLastChangeTime'
_v='enabled'
_u='disabled'
_t='ethIfGbeUtilization'
_s='ethIfPowerLevel'
_r='Gauge32'
_q='ethNotificationGroupV2'
_p='ethGeneralGroup'
_o='ethIfEntityId'
_n='ethIfFarEndLoopback'
_m='ethIfSuppressRemoteAlarms'
_l='ethIfForwardAls'
_k='ethIfAuAlarmIndicationSignalW2C'
_j='Unsigned32'
_i='ethIfLinkDown'
_h='ethIfBitrateMismatch'
_g='ethIfLossOfSync'
_f='ethIfLaserBiasHigh'
_e='ethIfReceivedPowerLow'
_d='ethIfReceivedPowerHigh'
_c='ethIfLossOfSignal'
_b='ethIfFrameSize'
_a='ethIfInterPacketGap'
_Z='ethIfFlowControlMode'
_Y='ethIfDuplexCapability'
_X='ethIfLaserBiasThreshold'
_W='ethIfLaserBias'
_V='ethIfAutoNegotiationStatus'
_U='ethIfAutoNegotiationMode'
_T='ethIfOperStatus'
_S='ethIfAdminStatus'
_R='ethIfLaserStatus'
_Q='ethIfHighSpeed'
_P='ethIfFormat'
_O='ethIfInvPhysIndexOrZero'
_N='ethIfDescr'
_M='ethIfTxSignalStatus'
_L='ethIfRxPort'
_K='ethIfTxPort'
_J='ethIfSlot'
_I='ethIfSubrack'
_H='ethIfName'
_G='ethIfIndex'
_F='read-write'
_E='Integer32'
_D='deprecated'
_C='read-only'
_B='current'
_A='LUM-ETH-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumEthMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumEthMIB','lumModules')
BoardOrInterfaceAdminStatus,BoardOrInterfaceOperStatus,FaultStatus,MgmtNameString,ObjectProperty,PortNumber,SlotNumber,SubrackNumber=mibBuilder.importSymbols('LUM-TC',_A2,_A3,'FaultStatus','MgmtNameString','ObjectProperty','PortNumber','SlotNumber','SubrackNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_r,_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_j,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_A4,'PhysAddress','TextualConvention')
lumEthMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,19))
if mibBuilder.loadTexts:lumEthMIBModule.setRevisions(('2017-06-15 00:00','2016-01-11 00:00','2002-12-06 00:00','2002-11-19 00:00','2002-11-13 00:00','2002-06-25 00:00'))
class EthSignalFormat(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('undefined',0),('gbE',1),('lan10GbE',2)))
_LumEthConfs_ObjectIdentity=ObjectIdentity
lumEthConfs=_LumEthConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,18,1))
_LumEthGroups_ObjectIdentity=ObjectIdentity
lumEthGroups=_LumEthGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,18,1,1))
_LumEthCompl_ObjectIdentity=ObjectIdentity
lumEthCompl=_LumEthCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,18,1,2))
_LumEthMIBObjects_ObjectIdentity=ObjectIdentity
lumEthMIBObjects=_LumEthMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,18,2))
_EthGeneral_ObjectIdentity=ObjectIdentity
ethGeneral=_EthGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,18,2,1))
_EthGeneralLastChangeTime_Type=DateAndTime
_EthGeneralLastChangeTime_Object=MibScalar
ethGeneralLastChangeTime=_EthGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,18,2,1,1),_EthGeneralLastChangeTime_Type())
ethGeneralLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ethGeneralLastChangeTime.setStatus(_B)
_EthGeneralStateLastChangeTime_Type=DateAndTime
_EthGeneralStateLastChangeTime_Object=MibScalar
ethGeneralStateLastChangeTime=_EthGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,18,2,1,2),_EthGeneralStateLastChangeTime_Type())
ethGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ethGeneralStateLastChangeTime.setStatus(_B)
_EthGeneralEthIfTableSize_Type=Unsigned32
_EthGeneralEthIfTableSize_Object=MibScalar
ethGeneralEthIfTableSize=_EthGeneralEthIfTableSize_Object((1,3,6,1,4,1,8708,2,18,2,1,3),_EthGeneralEthIfTableSize_Type())
ethGeneralEthIfTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ethGeneralEthIfTableSize.setStatus(_B)
_EthIfList_ObjectIdentity=ObjectIdentity
ethIfList=_EthIfList_ObjectIdentity((1,3,6,1,4,1,8708,2,18,2,2))
_EthIfTable_Object=MibTable
ethIfTable=_EthIfTable_Object((1,3,6,1,4,1,8708,2,18,2,2,1))
if mibBuilder.loadTexts:ethIfTable.setStatus(_B)
_EthIfEntry_Object=MibTableRow
ethIfEntry=_EthIfEntry_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1))
ethIfEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:ethIfEntry.setStatus(_B)
class _EthIfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EthIfIndex_Type.__name__=_j
_EthIfIndex_Object=MibTableColumn
ethIfIndex=_EthIfIndex_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,1),_EthIfIndex_Type())
ethIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfIndex.setStatus(_B)
_EthIfName_Type=MgmtNameString
_EthIfName_Object=MibTableColumn
ethIfName=_EthIfName_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,2),_EthIfName_Type())
ethIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfName.setStatus(_B)
class _EthIfDescr_Type(DisplayString):defaultValue=OctetString('')
_EthIfDescr_Type.__name__=_A4
_EthIfDescr_Object=MibTableColumn
ethIfDescr=_EthIfDescr_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,3),_EthIfDescr_Type())
ethIfDescr.setMaxAccess(_F)
if mibBuilder.loadTexts:ethIfDescr.setStatus(_B)
_EthIfSubrack_Type=SubrackNumber
_EthIfSubrack_Object=MibTableColumn
ethIfSubrack=_EthIfSubrack_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,4),_EthIfSubrack_Type())
ethIfSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfSubrack.setStatus(_B)
_EthIfSlot_Type=SlotNumber
_EthIfSlot_Object=MibTableColumn
ethIfSlot=_EthIfSlot_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,5),_EthIfSlot_Type())
ethIfSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfSlot.setStatus(_B)
_EthIfTxPort_Type=PortNumber
_EthIfTxPort_Object=MibTableColumn
ethIfTxPort=_EthIfTxPort_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,6),_EthIfTxPort_Type())
ethIfTxPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfTxPort.setStatus(_B)
_EthIfRxPort_Type=PortNumber
_EthIfRxPort_Object=MibTableColumn
ethIfRxPort=_EthIfRxPort_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,7),_EthIfRxPort_Type())
ethIfRxPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfRxPort.setStatus(_B)
class _EthIfInvPhysIndexOrZero_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_EthIfInvPhysIndexOrZero_Type.__name__=_j
_EthIfInvPhysIndexOrZero_Object=MibTableColumn
ethIfInvPhysIndexOrZero=_EthIfInvPhysIndexOrZero_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,8),_EthIfInvPhysIndexOrZero_Type())
ethIfInvPhysIndexOrZero.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfInvPhysIndexOrZero.setStatus(_B)
class _EthIfFormat_Type(EthSignalFormat):defaultValue=1
_EthIfFormat_Type.__name__=_A5
_EthIfFormat_Object=MibTableColumn
ethIfFormat=_EthIfFormat_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,9),_EthIfFormat_Type())
ethIfFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfFormat.setStatus(_B)
class _EthIfHighSpeed_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,10000))
_EthIfHighSpeed_Type.__name__=_r
_EthIfHighSpeed_Object=MibTableColumn
ethIfHighSpeed=_EthIfHighSpeed_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,10),_EthIfHighSpeed_Type())
ethIfHighSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfHighSpeed.setStatus(_B)
class _EthIfAdminStatus_Type(BoardOrInterfaceAdminStatus):defaultValue=3
_EthIfAdminStatus_Type.__name__=_A2
_EthIfAdminStatus_Object=MibTableColumn
ethIfAdminStatus=_EthIfAdminStatus_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,11),_EthIfAdminStatus_Type())
ethIfAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ethIfAdminStatus.setStatus(_B)
class _EthIfOperStatus_Type(BoardOrInterfaceOperStatus):defaultValue=1
_EthIfOperStatus_Type.__name__=_A3
_EthIfOperStatus_Object=MibTableColumn
ethIfOperStatus=_EthIfOperStatus_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,12),_EthIfOperStatus_Type())
ethIfOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfOperStatus.setStatus(_B)
class _EthIfLaserStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_EthIfLaserStatus_Type.__name__=_E
_EthIfLaserStatus_Object=MibTableColumn
ethIfLaserStatus=_EthIfLaserStatus_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,13),_EthIfLaserStatus_Type())
ethIfLaserStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfLaserStatus.setStatus(_B)
class _EthIfTxSignalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('down',1),('degraded',2),('up',3)))
_EthIfTxSignalStatus_Type.__name__=_E
_EthIfTxSignalStatus_Object=MibTableColumn
ethIfTxSignalStatus=_EthIfTxSignalStatus_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,14),_EthIfTxSignalStatus_Type())
ethIfTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfTxSignalStatus.setStatus(_B)
class _EthIfAutoNegotiationMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_EthIfAutoNegotiationMode_Type.__name__=_E
_EthIfAutoNegotiationMode_Object=MibTableColumn
ethIfAutoNegotiationMode=_EthIfAutoNegotiationMode_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,15),_EthIfAutoNegotiationMode_Type())
ethIfAutoNegotiationMode.setMaxAccess(_F)
if mibBuilder.loadTexts:ethIfAutoNegotiationMode.setStatus(_B)
class _EthIfAutoNegotiationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('incomplete',1),('half',2),('full',3)))
_EthIfAutoNegotiationStatus_Type.__name__=_E
_EthIfAutoNegotiationStatus_Object=MibTableColumn
ethIfAutoNegotiationStatus=_EthIfAutoNegotiationStatus_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,16),_EthIfAutoNegotiationStatus_Type())
ethIfAutoNegotiationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfAutoNegotiationStatus.setStatus(_B)
class _EthIfDuplexCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('half',2),('full',3)))
_EthIfDuplexCapability_Type.__name__=_E
_EthIfDuplexCapability_Object=MibTableColumn
ethIfDuplexCapability=_EthIfDuplexCapability_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,17),_EthIfDuplexCapability_Type())
ethIfDuplexCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfDuplexCapability.setStatus(_B)
class _EthIfFlowControlMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noPause',1),('rxPause',2),('txPause',3),('bothPause',4)))
_EthIfFlowControlMode_Type.__name__=_E
_EthIfFlowControlMode_Object=MibTableColumn
ethIfFlowControlMode=_EthIfFlowControlMode_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,18),_EthIfFlowControlMode_Type())
ethIfFlowControlMode.setMaxAccess(_F)
if mibBuilder.loadTexts:ethIfFlowControlMode.setStatus(_B)
class _EthIfInterPacketGap_Type(Gauge32):defaultValue=96;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(72,456))
_EthIfInterPacketGap_Type.__name__=_r
_EthIfInterPacketGap_Object=MibTableColumn
ethIfInterPacketGap=_EthIfInterPacketGap_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,19),_EthIfInterPacketGap_Type())
ethIfInterPacketGap.setMaxAccess(_F)
if mibBuilder.loadTexts:ethIfInterPacketGap.setStatus(_B)
class _EthIfFrameSize_Type(Gauge32):defaultValue=9600;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1518,9600))
_EthIfFrameSize_Type.__name__=_r
_EthIfFrameSize_Object=MibTableColumn
ethIfFrameSize=_EthIfFrameSize_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,20),_EthIfFrameSize_Type())
ethIfFrameSize.setMaxAccess(_F)
if mibBuilder.loadTexts:ethIfFrameSize.setStatus(_B)
_EthIfPowerLevel_Type=Integer32
_EthIfPowerLevel_Object=MibTableColumn
ethIfPowerLevel=_EthIfPowerLevel_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,21),_EthIfPowerLevel_Type())
ethIfPowerLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfPowerLevel.setStatus(_B)
class _EthIfPowerLevelHighThreshold_Type(Integer32):defaultValue=-50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-200,-10))
_EthIfPowerLevelHighThreshold_Type.__name__=_E
_EthIfPowerLevelHighThreshold_Object=MibTableColumn
ethIfPowerLevelHighThreshold=_EthIfPowerLevelHighThreshold_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,22),_EthIfPowerLevelHighThreshold_Type())
ethIfPowerLevelHighThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:ethIfPowerLevelHighThreshold.setStatus(_D)
class _EthIfPowerLevelLowThreshold_Type(Integer32):defaultValue=-160;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-200,-10))
_EthIfPowerLevelLowThreshold_Type.__name__=_E
_EthIfPowerLevelLowThreshold_Object=MibTableColumn
ethIfPowerLevelLowThreshold=_EthIfPowerLevelLowThreshold_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,23),_EthIfPowerLevelLowThreshold_Type())
ethIfPowerLevelLowThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:ethIfPowerLevelLowThreshold.setStatus(_D)
_EthIfLaserBias_Type=Unsigned32
_EthIfLaserBias_Object=MibTableColumn
ethIfLaserBias=_EthIfLaserBias_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,24),_EthIfLaserBias_Type())
ethIfLaserBias.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfLaserBias.setStatus(_B)
class _EthIfLaserBiasThreshold_Type(Unsigned32):defaultValue=200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_EthIfLaserBiasThreshold_Type.__name__=_j
_EthIfLaserBiasThreshold_Object=MibTableColumn
ethIfLaserBiasThreshold=_EthIfLaserBiasThreshold_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,25),_EthIfLaserBiasThreshold_Type())
ethIfLaserBiasThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:ethIfLaserBiasThreshold.setStatus(_B)
_EthIfLossOfSignal_Type=FaultStatus
_EthIfLossOfSignal_Object=MibTableColumn
ethIfLossOfSignal=_EthIfLossOfSignal_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,26),_EthIfLossOfSignal_Type())
ethIfLossOfSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfLossOfSignal.setStatus(_B)
_EthIfReceivedPowerHigh_Type=FaultStatus
_EthIfReceivedPowerHigh_Object=MibTableColumn
ethIfReceivedPowerHigh=_EthIfReceivedPowerHigh_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,27),_EthIfReceivedPowerHigh_Type())
ethIfReceivedPowerHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfReceivedPowerHigh.setStatus(_B)
_EthIfReceivedPowerLow_Type=FaultStatus
_EthIfReceivedPowerLow_Object=MibTableColumn
ethIfReceivedPowerLow=_EthIfReceivedPowerLow_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,28),_EthIfReceivedPowerLow_Type())
ethIfReceivedPowerLow.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfReceivedPowerLow.setStatus(_B)
_EthIfLaserBiasHigh_Type=FaultStatus
_EthIfLaserBiasHigh_Object=MibTableColumn
ethIfLaserBiasHigh=_EthIfLaserBiasHigh_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,29),_EthIfLaserBiasHigh_Type())
ethIfLaserBiasHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfLaserBiasHigh.setStatus(_B)
_EthIfLossOfSync_Type=FaultStatus
_EthIfLossOfSync_Object=MibTableColumn
ethIfLossOfSync=_EthIfLossOfSync_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,30),_EthIfLossOfSync_Type())
ethIfLossOfSync.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfLossOfSync.setStatus(_B)
_EthIfBitrateMismatch_Type=FaultStatus
_EthIfBitrateMismatch_Object=MibTableColumn
ethIfBitrateMismatch=_EthIfBitrateMismatch_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,31),_EthIfBitrateMismatch_Type())
ethIfBitrateMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfBitrateMismatch.setStatus(_B)
_EthIfLinkDown_Type=FaultStatus
_EthIfLinkDown_Object=MibTableColumn
ethIfLinkDown=_EthIfLinkDown_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,32),_EthIfLinkDown_Type())
ethIfLinkDown.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfLinkDown.setStatus(_B)
_EthIfAuAlarmIndicationSignalW2C_Type=FaultStatus
_EthIfAuAlarmIndicationSignalW2C_Object=MibTableColumn
ethIfAuAlarmIndicationSignalW2C=_EthIfAuAlarmIndicationSignalW2C_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,33),_EthIfAuAlarmIndicationSignalW2C_Type())
ethIfAuAlarmIndicationSignalW2C.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfAuAlarmIndicationSignalW2C.setStatus(_B)
class _EthIfForwardAls_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_u,1),(_v,2)))
_EthIfForwardAls_Type.__name__=_E
_EthIfForwardAls_Object=MibTableColumn
ethIfForwardAls=_EthIfForwardAls_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,34),_EthIfForwardAls_Type())
ethIfForwardAls.setMaxAccess(_F)
if mibBuilder.loadTexts:ethIfForwardAls.setStatus(_B)
class _EthIfSuppressRemoteAlarms_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_u,1),(_v,2)))
_EthIfSuppressRemoteAlarms_Type.__name__=_E
_EthIfSuppressRemoteAlarms_Object=MibTableColumn
ethIfSuppressRemoteAlarms=_EthIfSuppressRemoteAlarms_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,35),_EthIfSuppressRemoteAlarms_Type())
ethIfSuppressRemoteAlarms.setMaxAccess(_F)
if mibBuilder.loadTexts:ethIfSuppressRemoteAlarms.setStatus(_B)
class _EthIfFarEndLoopback_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_u,1),(_v,2)))
_EthIfFarEndLoopback_Type.__name__=_E
_EthIfFarEndLoopback_Object=MibTableColumn
ethIfFarEndLoopback=_EthIfFarEndLoopback_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,36),_EthIfFarEndLoopback_Type())
ethIfFarEndLoopback.setMaxAccess(_F)
if mibBuilder.loadTexts:ethIfFarEndLoopback.setStatus(_B)
class _EthIfEntityId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EthIfEntityId_Type.__name__=_j
_EthIfEntityId_Object=MibTableColumn
ethIfEntityId=_EthIfEntityId_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,37),_EthIfEntityId_Type())
ethIfEntityId.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfEntityId.setStatus(_B)
class _EthIfGbeUtilization_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_EthIfGbeUtilization_Type.__name__=_j
_EthIfGbeUtilization_Object=MibTableColumn
ethIfGbeUtilization=_EthIfGbeUtilization_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,38),_EthIfGbeUtilization_Type())
ethIfGbeUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfGbeUtilization.setStatus(_B)
_EthIfObjectProperty_Type=ObjectProperty
_EthIfObjectProperty_Object=MibTableColumn
ethIfObjectProperty=_EthIfObjectProperty_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,39),_EthIfObjectProperty_Type())
ethIfObjectProperty.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfObjectProperty.setStatus(_B)
class _EthIfPowerLevelLowRelativeThreshold_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,100))
_EthIfPowerLevelLowRelativeThreshold_Type.__name__=_E
_EthIfPowerLevelLowRelativeThreshold_Object=MibTableColumn
ethIfPowerLevelLowRelativeThreshold=_EthIfPowerLevelLowRelativeThreshold_Object((1,3,6,1,4,1,8708,2,18,2,2,1,1,40),_EthIfPowerLevelLowRelativeThreshold_Type())
ethIfPowerLevelLowRelativeThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:ethIfPowerLevelLowRelativeThreshold.setStatus(_B)
_LumentisEthNotifications_ObjectIdentity=ObjectIdentity
lumentisEthNotifications=_LumentisEthNotifications_ObjectIdentity((1,3,6,1,4,1,8708,2,18,2,3))
_EthNotifyPrefix_ObjectIdentity=ObjectIdentity
ethNotifyPrefix=_EthNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,8708,2,18,2,3,0))
ethGeneralGroup=ObjectGroup((1,3,6,1,4,1,8708,2,18,1,1,1))
ethGeneralGroup.setObjects(*((_A,_w),(_A,_x)))
if mibBuilder.loadTexts:ethGeneralGroup.setStatus(_D)
ethIfGroup=ObjectGroup((1,3,6,1,4,1,8708,2,18,1,1,2))
ethIfGroup.setObjects(*((_A,_G),(_A,_H),(_A,_N),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_O),(_A,_P),(_A,_Q),(_A,_s),(_A,_A6),(_A,_A7),(_A,_R),(_A,_S),(_A,_T),(_A,_M),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:ethIfGroup.setStatus(_D)
ethIfGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,18,1,1,4))
ethIfGroupV2.setObjects(*((_A,_G),(_A,_H),(_A,_N),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_M),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:ethIfGroupV2.setStatus(_D)
ethIfGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,18,1,1,5))
ethIfGroupV3.setObjects(*((_A,_G),(_A,_H),(_A,_N),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_M),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:ethIfGroupV3.setStatus(_D)
ethIfGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,18,1,1,7))
ethIfGroupV4.setObjects(*((_A,_G),(_A,_H),(_A,_N),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_M),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_t)))
if mibBuilder.loadTexts:ethIfGroupV4.setStatus(_D)
ethGeneralGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,18,1,1,8))
ethGeneralGroupV2.setObjects(*((_A,_w),(_A,_x),(_A,_A8)))
if mibBuilder.loadTexts:ethGeneralGroupV2.setStatus(_B)
ethIfGroupV5=ObjectGroup((1,3,6,1,4,1,8708,2,18,1,1,9))
ethIfGroupV5.setObjects(*((_A,_G),(_A,_H),(_A,_N),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_M),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_t),(_A,_s)))
if mibBuilder.loadTexts:ethIfGroupV5.setStatus(_D)
ethIfGroupV6=ObjectGroup((1,3,6,1,4,1,8708,2,18,1,1,10))
ethIfGroupV6.setObjects(*((_A,_G),(_A,_H),(_A,_N),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_M),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_t),(_A,_s),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:ethIfGroupV6.setStatus(_B)
ethIfTxSignalStatusDown=NotificationType((1,3,6,1,4,1,8708,2,18,2,3,0,1))
ethIfTxSignalStatusDown.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_o),(_A,_M)))
if mibBuilder.loadTexts:ethIfTxSignalStatusDown.setStatus(_B)
ethIfTxSignalStatusUp=NotificationType((1,3,6,1,4,1,8708,2,18,2,3,0,2))
ethIfTxSignalStatusUp.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_o),(_A,_M)))
if mibBuilder.loadTexts:ethIfTxSignalStatusUp.setStatus(_B)
ethIfTxSignalStatusDegraded=NotificationType((1,3,6,1,4,1,8708,2,18,2,3,0,3))
ethIfTxSignalStatusDegraded.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_o),(_A,_M)))
if mibBuilder.loadTexts:ethIfTxSignalStatusDegraded.setStatus(_B)
ethNotificationGroup=NotificationGroup((1,3,6,1,4,1,8708,2,18,1,1,3))
ethNotificationGroup.setObjects(*((_A,_y),(_A,_z)))
if mibBuilder.loadTexts:ethNotificationGroup.setStatus(_D)
ethNotificationGroupV2=NotificationGroup((1,3,6,1,4,1,8708,2,18,1,1,6))
ethNotificationGroupV2.setObjects(*((_A,_y),(_A,_z),(_A,_AB)))
if mibBuilder.loadTexts:ethNotificationGroupV2.setStatus(_B)
lumEthBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,18,1,2,1))
lumEthBasicComplV1.setObjects(*((_A,_p),(_A,_AC),(_A,_A0)))
if mibBuilder.loadTexts:lumEthBasicComplV1.setStatus(_D)
lumEthBasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,18,1,2,2))
lumEthBasicComplV2.setObjects(*((_A,_p),(_A,_AD),(_A,_A0)))
if mibBuilder.loadTexts:lumEthBasicComplV2.setStatus(_D)
lumEthBasicComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,18,1,2,3))
lumEthBasicComplV3.setObjects(*((_A,_p),(_A,_AE),(_A,_q)))
if mibBuilder.loadTexts:lumEthBasicComplV3.setStatus(_D)
lumEthBasicComplV4=ModuleCompliance((1,3,6,1,4,1,8708,2,18,1,2,4))
lumEthBasicComplV4.setObjects(*((_A,_p),(_A,_AF),(_A,_q)))
if mibBuilder.loadTexts:lumEthBasicComplV4.setStatus(_D)
lumEthBasicComplV5=ModuleCompliance((1,3,6,1,4,1,8708,2,18,1,2,5))
lumEthBasicComplV5.setObjects(*((_A,_A1),(_A,_AG),(_A,_q)))
if mibBuilder.loadTexts:lumEthBasicComplV5.setStatus(_D)
lumEthBasicComplV6=ModuleCompliance((1,3,6,1,4,1,8708,2,18,1,2,6))
lumEthBasicComplV6.setObjects(*((_A,_A1),(_A,_AH),(_A,_q)))
if mibBuilder.loadTexts:lumEthBasicComplV6.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_A5:EthSignalFormat,'lumEthMIBModule':lumEthMIBModule,'lumEthConfs':lumEthConfs,'lumEthGroups':lumEthGroups,_p:ethGeneralGroup,_AC:ethIfGroup,_A0:ethNotificationGroup,_AD:ethIfGroupV2,_AE:ethIfGroupV3,_q:ethNotificationGroupV2,_AF:ethIfGroupV4,_A1:ethGeneralGroupV2,_AG:ethIfGroupV5,_AH:ethIfGroupV6,'lumEthCompl':lumEthCompl,'lumEthBasicComplV1':lumEthBasicComplV1,'lumEthBasicComplV2':lumEthBasicComplV2,'lumEthBasicComplV3':lumEthBasicComplV3,'lumEthBasicComplV4':lumEthBasicComplV4,'lumEthBasicComplV5':lumEthBasicComplV5,'lumEthBasicComplV6':lumEthBasicComplV6,'lumEthMIBObjects':lumEthMIBObjects,'ethGeneral':ethGeneral,_w:ethGeneralLastChangeTime,_x:ethGeneralStateLastChangeTime,_A8:ethGeneralEthIfTableSize,'ethIfList':ethIfList,'ethIfTable':ethIfTable,'ethIfEntry':ethIfEntry,_G:ethIfIndex,_H:ethIfName,_N:ethIfDescr,_I:ethIfSubrack,_J:ethIfSlot,_K:ethIfTxPort,_L:ethIfRxPort,_O:ethIfInvPhysIndexOrZero,_P:ethIfFormat,_Q:ethIfHighSpeed,_S:ethIfAdminStatus,_T:ethIfOperStatus,_R:ethIfLaserStatus,_M:ethIfTxSignalStatus,_U:ethIfAutoNegotiationMode,_V:ethIfAutoNegotiationStatus,_Y:ethIfDuplexCapability,_Z:ethIfFlowControlMode,_a:ethIfInterPacketGap,_b:ethIfFrameSize,_s:ethIfPowerLevel,_A6:ethIfPowerLevelHighThreshold,_A7:ethIfPowerLevelLowThreshold,_W:ethIfLaserBias,_X:ethIfLaserBiasThreshold,_c:ethIfLossOfSignal,_d:ethIfReceivedPowerHigh,_e:ethIfReceivedPowerLow,_f:ethIfLaserBiasHigh,_g:ethIfLossOfSync,_h:ethIfBitrateMismatch,_i:ethIfLinkDown,_k:ethIfAuAlarmIndicationSignalW2C,_l:ethIfForwardAls,_m:ethIfSuppressRemoteAlarms,_n:ethIfFarEndLoopback,_o:ethIfEntityId,_t:ethIfGbeUtilization,_A9:ethIfObjectProperty,_AA:ethIfPowerLevelLowRelativeThreshold,'lumentisEthNotifications':lumentisEthNotifications,'ethNotifyPrefix':ethNotifyPrefix,_y:ethIfTxSignalStatusDown,_z:ethIfTxSignalStatusUp,_AB:ethIfTxSignalStatusDegraded})