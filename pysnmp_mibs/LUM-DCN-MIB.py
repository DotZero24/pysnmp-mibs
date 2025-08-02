_BS='dcnPppGroupV8'
_BR='dcnEthGroupV1'
_BQ='dcnIfGroupV3'
_BP='dcnIfGroupV2'
_BO='dcnPppGroupV4'
_BN='dcnPppGroupV3'
_BM='dcnPppGroup'
_BL='dcnIfTxSignalStatusUp'
_BK='dcnIfTxSignalStatusDown'
_BJ='dcnPppRxIfNo'
_BI='dcnPppTxIfNo'
_BH='dcnEthOperStatus'
_BG='dcnEthAdminStatus'
_BF='dcnIfPhysicalLocation'
_BE='dcnCcConfigurationMismatch'
_BD='dcnCcTrxNotSupportCommChannel'
_BC='dcnCcFecFailure'
_BB='dcnCcResetCounter'
_BA='dcnCcErrorCounter'
_B9='dcnCcChannelStatus'
_B8='dcnCcAdminStatus'
_B7='dcnCcRxPort'
_B6='dcnCcTxPort'
_B5='dcnCcSlot'
_B4='dcnCcSubrack'
_B3='dcnCcDescr'
_B2='dcnCcName'
_B1='dcnAddressNextPppAddress'
_B0='dcnAddressCurrentPppAddress'
_A_='DcnOscMode'
_Az='LambdaFrequency'
_Ay='dcnPppGroupV7'
_Ax='dcnPppGroupV2'
_Aw='dcnPppVlanEtherType'
_Av='dcnPppVlanId'
_Au='dcnEthChangeSpeedCommand'
_At='dcnIfLinkSupervisionFailure'
_As='dcnIfLaserMode'
_Ar='dcnIfTraceMismatch'
_Aq='dcnIfTraceAlarmMode'
_Ap='dcnIfTraceExpected'
_Ao='dcnIfTraceReceived'
_An='dcnIfTraceTransmitted'
_Am='dcnIfRemoteDefectIndication'
_Al='dcnIfProtocolVersionMismatch'
_Ak='dcnGeneralDcnPppTableSize'
_Aj='dcnGeneralDcnIfTableSize'
_Ai='dcnCcIndex'
_Ah='dcnEthGroupV3'
_Ag='dcnEthGroupV2'
_Af='dcnPppGroupV5'
_Ae='dcnEthObjectProperty'
_Ad='dcnEthFlowControlMode'
_Ac='dcnEthRateLimit'
_Ab='dcnEthDuplexCapability'
_Aa='dcnEthSpeed'
_AZ='dcnEthLinkStatus'
_AY='dcnEthAutoNegotiationMode'
_AX='dcnEthPort'
_AW='dcnEthSlot'
_AV='dcnEthSubrack'
_AU='dcnEthDescr'
_AT='dcnEthName'
_AS='dcnPppGccChannel'
_AR='dcnIfTrxMediaMismatch'
_AQ='dcnIfReceivedPowerLow'
_AP='dcnIfReceivedPowerHigh'
_AO='dcnIfUnexpectedTxFrequency'
_AN='dcnIfIllegalFrequency'
_AM='dcnIfTransmitterFailed'
_AL='dcnIfTrxCodeMismatch'
_AK='dcnIfTrxMissing'
_AJ='dcnIfTrxBitrateUnavailable'
_AI='dcnIfLossOfSignal'
_AH='dcnIfLaserBias'
_AG='dcnIfExpectedTxFrequency'
_AF='dcnIfLaserTempActual'
_AE='dcnIfTxPowerLevel'
_AD='dcnIfPowerLevel'
_AC='dcnIfPowerLevelLowRelativeThreshold'
_AB='dcnIfReceiverSensitivity'
_AA='dcnIfTrxClass'
_A9='dcnIfHighSpeedMax'
_A8='dcnIfHighSpeedMin'
_A7='dcnIfLaserStatus'
_A6='dcnGeneralStateLastChangeTime'
_A5='dcnGeneralLastChangeTime'
_A4='BoardOrInterfaceOperStatus'
_A3='dcnIfGroupV5'
_A2='dcnPppObjectProperty'
_A1='dcnPppRouteName'
_A0='dcnIfObjectProperty'
_z='dcnIfTxFrequency'
_y='dcnEthIndex'
_x='BoardOrInterfaceAdminStatus'
_w='dcnCcGroup'
_v='dcnPppGroupV6'
_u='dcnIfGroupV4'
_t='dcnGeneralGroup'
_s='dcnPppLogicalLinkId'
_r='dcnIfLinkDown'
_q='dcnIfOperStatus'
_p='dcnIfAdminStatus'
_o='dcnIfOscMode'
_n='dcnIfMaxSpeed'
_m='dcnIfType'
_l='dcnIfInvPhysIndexOrZero'
_k='dcnIfDescr'
_j='dcnGeneralGroupV3'
_i='dcnGeneralGroupV2'
_h='dcnIfGroup'
_g='dcnPppAcceptCommand'
_f='dcnPppDialCommand'
_e='Unsigned32'
_d='dcnPppOperStatus'
_c='dcnIfTxSignalStatus'
_b='dcnIfRxPort'
_a='dcnIfTxPort'
_Z='dcnIfSlot'
_Y='dcnIfSubrack'
_X='dcnIfName'
_W='DisplayString'
_V='dcnPppAdminStatus'
_U='dcnPppType'
_T='dcnPppInvPhysIndexOrZero'
_S='dcnPppRxPort'
_R='dcnPppRxSlot'
_Q='dcnPppRxSubrack'
_P='dcnPppTxPort'
_O='dcnPppTxSlot'
_N='dcnPppTxSubrack'
_M='dcnPppDescr'
_L='dcnPppName'
_K='dcnIfIndex'
_J='dcnPppIndex'
_I='read-create'
_H='dcnAddressGroup'
_G='dcnNotificationGroup'
_F='Integer32'
_E='read-write'
_D='deprecated'
_C='read-only'
_B='current'
_A='LUM-DCN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumDcnMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumDcnMIB','lumModules')
BoardOrInterfaceAdminStatus,BoardOrInterfaceOperStatus,CommandString,FaultStatus,LambdaFrequency,MgmtNameString,ObjectProperty,PortNumber,SlotNumber,SubrackNumber=mibBuilder.importSymbols('LUM-TC',_x,_A4,'CommandString','FaultStatus',_Az,'MgmtNameString','ObjectProperty','PortNumber','SlotNumber','SubrackNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_e,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_W,'PhysAddress','TextualConvention')
lumDcnMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,21))
if mibBuilder.loadTexts:lumDcnMIBModule.setRevisions(('2018-06-29 00:00','2017-12-08 00:00','2017-06-15 00:00','2016-11-30 00:00','2016-01-11 00:00','2015-11-30 00:00','2015-05-29 00:00','2011-12-20 09:45','2011-08-16 09:45','2010-02-01 00:00','2003-02-12 00:00','2002-11-15 00:00'))
class DcnSignalType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('undefined',0),('electrical',1),('optical',2)))
class DcnOscMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('icn',0),('dcn',1),('customer',2),('mixed',3),('unused',4),('lan',5),('customerOpto',6),('mixedOpto',7)))
_LumDcnConfs_ObjectIdentity=ObjectIdentity
lumDcnConfs=_LumDcnConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,20,1))
_LumDcnGroups_ObjectIdentity=ObjectIdentity
lumDcnGroups=_LumDcnGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,20,1,1))
_LumDcnCompl_ObjectIdentity=ObjectIdentity
lumDcnCompl=_LumDcnCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,20,1,2))
_LumDcnMIBObjects_ObjectIdentity=ObjectIdentity
lumDcnMIBObjects=_LumDcnMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,20,2))
_DcnGeneral_ObjectIdentity=ObjectIdentity
dcnGeneral=_DcnGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,20,2,1))
_DcnGeneralLastChangeTime_Type=DateAndTime
_DcnGeneralLastChangeTime_Object=MibScalar
dcnGeneralLastChangeTime=_DcnGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,20,2,1,1),_DcnGeneralLastChangeTime_Type())
dcnGeneralLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnGeneralLastChangeTime.setStatus(_B)
_DcnGeneralStateLastChangeTime_Type=DateAndTime
_DcnGeneralStateLastChangeTime_Object=MibScalar
dcnGeneralStateLastChangeTime=_DcnGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,20,2,1,2),_DcnGeneralStateLastChangeTime_Type())
dcnGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnGeneralStateLastChangeTime.setStatus(_B)
_DcnGeneralDcnIfTableSize_Type=Unsigned32
_DcnGeneralDcnIfTableSize_Object=MibScalar
dcnGeneralDcnIfTableSize=_DcnGeneralDcnIfTableSize_Object((1,3,6,1,4,1,8708,2,20,2,1,3),_DcnGeneralDcnIfTableSize_Type())
dcnGeneralDcnIfTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnGeneralDcnIfTableSize.setStatus(_B)
_DcnGeneralDcnPppTableSize_Type=Unsigned32
_DcnGeneralDcnPppTableSize_Object=MibScalar
dcnGeneralDcnPppTableSize=_DcnGeneralDcnPppTableSize_Object((1,3,6,1,4,1,8708,2,20,2,1,4),_DcnGeneralDcnPppTableSize_Type())
dcnGeneralDcnPppTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnGeneralDcnPppTableSize.setStatus(_B)
_DcnGeneralDcnEthTableSize_Type=Unsigned32
_DcnGeneralDcnEthTableSize_Object=MibScalar
dcnGeneralDcnEthTableSize=_DcnGeneralDcnEthTableSize_Object((1,3,6,1,4,1,8708,2,20,2,1,5),_DcnGeneralDcnEthTableSize_Type())
dcnGeneralDcnEthTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnGeneralDcnEthTableSize.setStatus(_B)
_DcnGeneralDcnCcTableSize_Type=Unsigned32
_DcnGeneralDcnCcTableSize_Object=MibScalar
dcnGeneralDcnCcTableSize=_DcnGeneralDcnCcTableSize_Object((1,3,6,1,4,1,8708,2,20,2,1,6),_DcnGeneralDcnCcTableSize_Type())
dcnGeneralDcnCcTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnGeneralDcnCcTableSize.setStatus(_B)
_DcnIfList_ObjectIdentity=ObjectIdentity
dcnIfList=_DcnIfList_ObjectIdentity((1,3,6,1,4,1,8708,2,20,2,2))
_DcnIfTable_Object=MibTable
dcnIfTable=_DcnIfTable_Object((1,3,6,1,4,1,8708,2,20,2,2,1))
if mibBuilder.loadTexts:dcnIfTable.setStatus(_B)
_DcnIfEntry_Object=MibTableRow
dcnIfEntry=_DcnIfEntry_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1))
dcnIfEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:dcnIfEntry.setStatus(_B)
class _DcnIfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DcnIfIndex_Type.__name__=_e
_DcnIfIndex_Object=MibTableColumn
dcnIfIndex=_DcnIfIndex_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,1),_DcnIfIndex_Type())
dcnIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfIndex.setStatus(_B)
_DcnIfName_Type=MgmtNameString
_DcnIfName_Object=MibTableColumn
dcnIfName=_DcnIfName_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,2),_DcnIfName_Type())
dcnIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfName.setStatus(_B)
class _DcnIfDescr_Type(DisplayString):defaultValue=OctetString('')
_DcnIfDescr_Type.__name__=_W
_DcnIfDescr_Object=MibTableColumn
dcnIfDescr=_DcnIfDescr_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,3),_DcnIfDescr_Type())
dcnIfDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:dcnIfDescr.setStatus(_B)
_DcnIfSubrack_Type=SubrackNumber
_DcnIfSubrack_Object=MibTableColumn
dcnIfSubrack=_DcnIfSubrack_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,4),_DcnIfSubrack_Type())
dcnIfSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfSubrack.setStatus(_B)
_DcnIfSlot_Type=SlotNumber
_DcnIfSlot_Object=MibTableColumn
dcnIfSlot=_DcnIfSlot_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,5),_DcnIfSlot_Type())
dcnIfSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfSlot.setStatus(_B)
_DcnIfTxPort_Type=PortNumber
_DcnIfTxPort_Object=MibTableColumn
dcnIfTxPort=_DcnIfTxPort_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,6),_DcnIfTxPort_Type())
dcnIfTxPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfTxPort.setStatus(_B)
_DcnIfRxPort_Type=PortNumber
_DcnIfRxPort_Object=MibTableColumn
dcnIfRxPort=_DcnIfRxPort_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,7),_DcnIfRxPort_Type())
dcnIfRxPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfRxPort.setStatus(_B)
class _DcnIfInvPhysIndexOrZero_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DcnIfInvPhysIndexOrZero_Type.__name__=_e
_DcnIfInvPhysIndexOrZero_Object=MibTableColumn
dcnIfInvPhysIndexOrZero=_DcnIfInvPhysIndexOrZero_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,8),_DcnIfInvPhysIndexOrZero_Type())
dcnIfInvPhysIndexOrZero.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfInvPhysIndexOrZero.setStatus(_B)
_DcnIfType_Type=DcnSignalType
_DcnIfType_Object=MibTableColumn
dcnIfType=_DcnIfType_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,9),_DcnIfType_Type())
dcnIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfType.setStatus(_B)
class _DcnIfMaxSpeed_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100))
_DcnIfMaxSpeed_Type.__name__='Gauge32'
_DcnIfMaxSpeed_Object=MibTableColumn
dcnIfMaxSpeed=_DcnIfMaxSpeed_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,10),_DcnIfMaxSpeed_Type())
dcnIfMaxSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfMaxSpeed.setStatus(_B)
class _DcnIfOscMode_Type(DcnOscMode):defaultValue=1
_DcnIfOscMode_Type.__name__=_A_
_DcnIfOscMode_Object=MibTableColumn
dcnIfOscMode=_DcnIfOscMode_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,11),_DcnIfOscMode_Type())
dcnIfOscMode.setMaxAccess(_E)
if mibBuilder.loadTexts:dcnIfOscMode.setStatus(_B)
class _DcnIfAdminStatus_Type(BoardOrInterfaceAdminStatus):defaultValue=1
_DcnIfAdminStatus_Type.__name__=_x
_DcnIfAdminStatus_Object=MibTableColumn
dcnIfAdminStatus=_DcnIfAdminStatus_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,12),_DcnIfAdminStatus_Type())
dcnIfAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dcnIfAdminStatus.setStatus(_B)
class _DcnIfOperStatus_Type(BoardOrInterfaceOperStatus):defaultValue=1
_DcnIfOperStatus_Type.__name__=_A4
_DcnIfOperStatus_Object=MibTableColumn
dcnIfOperStatus=_DcnIfOperStatus_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,13),_DcnIfOperStatus_Type())
dcnIfOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfOperStatus.setStatus(_B)
class _DcnIfTxSignalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('down',1),('degraded',2),('up',3)))
_DcnIfTxSignalStatus_Type.__name__=_F
_DcnIfTxSignalStatus_Object=MibTableColumn
dcnIfTxSignalStatus=_DcnIfTxSignalStatus_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,14),_DcnIfTxSignalStatus_Type())
dcnIfTxSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfTxSignalStatus.setStatus(_B)
_DcnIfLinkDown_Type=FaultStatus
_DcnIfLinkDown_Object=MibTableColumn
dcnIfLinkDown=_DcnIfLinkDown_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,15),_DcnIfLinkDown_Type())
dcnIfLinkDown.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfLinkDown.setStatus(_B)
_DcnIfTxFrequency_Type=LambdaFrequency
_DcnIfTxFrequency_Object=MibTableColumn
dcnIfTxFrequency=_DcnIfTxFrequency_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,16),_DcnIfTxFrequency_Type())
dcnIfTxFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfTxFrequency.setStatus(_B)
_DcnIfObjectProperty_Type=ObjectProperty
_DcnIfObjectProperty_Object=MibTableColumn
dcnIfObjectProperty=_DcnIfObjectProperty_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,17),_DcnIfObjectProperty_Type())
dcnIfObjectProperty.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfObjectProperty.setStatus(_B)
class _DcnIfLaserStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_DcnIfLaserStatus_Type.__name__=_F
_DcnIfLaserStatus_Object=MibTableColumn
dcnIfLaserStatus=_DcnIfLaserStatus_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,18),_DcnIfLaserStatus_Type())
dcnIfLaserStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfLaserStatus.setStatus(_B)
_DcnIfPowerLevel_Type=Integer32
_DcnIfPowerLevel_Object=MibTableColumn
dcnIfPowerLevel=_DcnIfPowerLevel_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,19),_DcnIfPowerLevel_Type())
dcnIfPowerLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfPowerLevel.setStatus(_B)
_DcnIfTxPowerLevel_Type=Integer32
_DcnIfTxPowerLevel_Object=MibTableColumn
dcnIfTxPowerLevel=_DcnIfTxPowerLevel_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,20),_DcnIfTxPowerLevel_Type())
dcnIfTxPowerLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfTxPowerLevel.setStatus(_B)
_DcnIfReceiverSensitivity_Type=Integer32
_DcnIfReceiverSensitivity_Object=MibTableColumn
dcnIfReceiverSensitivity=_DcnIfReceiverSensitivity_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,21),_DcnIfReceiverSensitivity_Type())
dcnIfReceiverSensitivity.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfReceiverSensitivity.setStatus(_B)
class _DcnIfPowerLevelLowRelativeThreshold_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-50,100))
_DcnIfPowerLevelLowRelativeThreshold_Type.__name__=_F
_DcnIfPowerLevelLowRelativeThreshold_Object=MibTableColumn
dcnIfPowerLevelLowRelativeThreshold=_DcnIfPowerLevelLowRelativeThreshold_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,22),_DcnIfPowerLevelLowRelativeThreshold_Type())
dcnIfPowerLevelLowRelativeThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:dcnIfPowerLevelLowRelativeThreshold.setStatus(_B)
_DcnIfLaserTempActual_Type=Integer32
_DcnIfLaserTempActual_Object=MibTableColumn
dcnIfLaserTempActual=_DcnIfLaserTempActual_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,23),_DcnIfLaserTempActual_Type())
dcnIfLaserTempActual.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfLaserTempActual.setStatus(_B)
class _DcnIfTrxClass_Type(DisplayString):defaultValue=OctetString('')
_DcnIfTrxClass_Type.__name__=_W
_DcnIfTrxClass_Object=MibTableColumn
dcnIfTrxClass=_DcnIfTrxClass_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,24),_DcnIfTrxClass_Type())
dcnIfTrxClass.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfTrxClass.setStatus(_B)
_DcnIfHighSpeedMin_Type=Gauge32
_DcnIfHighSpeedMin_Object=MibTableColumn
dcnIfHighSpeedMin=_DcnIfHighSpeedMin_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,25),_DcnIfHighSpeedMin_Type())
dcnIfHighSpeedMin.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfHighSpeedMin.setStatus(_B)
_DcnIfHighSpeedMax_Type=Gauge32
_DcnIfHighSpeedMax_Object=MibTableColumn
dcnIfHighSpeedMax=_DcnIfHighSpeedMax_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,26),_DcnIfHighSpeedMax_Type())
dcnIfHighSpeedMax.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfHighSpeedMax.setStatus(_B)
class _DcnIfExpectedTxFrequency_Type(LambdaFrequency):defaultValue=0
_DcnIfExpectedTxFrequency_Type.__name__=_Az
_DcnIfExpectedTxFrequency_Object=MibTableColumn
dcnIfExpectedTxFrequency=_DcnIfExpectedTxFrequency_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,27),_DcnIfExpectedTxFrequency_Type())
dcnIfExpectedTxFrequency.setMaxAccess(_E)
if mibBuilder.loadTexts:dcnIfExpectedTxFrequency.setStatus(_B)
_DcnIfLaserBias_Type=Unsigned32
_DcnIfLaserBias_Object=MibTableColumn
dcnIfLaserBias=_DcnIfLaserBias_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,28),_DcnIfLaserBias_Type())
dcnIfLaserBias.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfLaserBias.setStatus(_B)
_DcnIfLossOfSignal_Type=FaultStatus
_DcnIfLossOfSignal_Object=MibTableColumn
dcnIfLossOfSignal=_DcnIfLossOfSignal_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,29),_DcnIfLossOfSignal_Type())
dcnIfLossOfSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfLossOfSignal.setStatus(_B)
_DcnIfTrxCodeMismatch_Type=FaultStatus
_DcnIfTrxCodeMismatch_Object=MibTableColumn
dcnIfTrxCodeMismatch=_DcnIfTrxCodeMismatch_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,30),_DcnIfTrxCodeMismatch_Type())
dcnIfTrxCodeMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfTrxCodeMismatch.setStatus(_B)
_DcnIfTrxBitrateUnavailable_Type=FaultStatus
_DcnIfTrxBitrateUnavailable_Object=MibTableColumn
dcnIfTrxBitrateUnavailable=_DcnIfTrxBitrateUnavailable_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,31),_DcnIfTrxBitrateUnavailable_Type())
dcnIfTrxBitrateUnavailable.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfTrxBitrateUnavailable.setStatus(_B)
_DcnIfTrxMissing_Type=FaultStatus
_DcnIfTrxMissing_Object=MibTableColumn
dcnIfTrxMissing=_DcnIfTrxMissing_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,32),_DcnIfTrxMissing_Type())
dcnIfTrxMissing.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfTrxMissing.setStatus(_B)
_DcnIfTransmitterFailed_Type=FaultStatus
_DcnIfTransmitterFailed_Object=MibTableColumn
dcnIfTransmitterFailed=_DcnIfTransmitterFailed_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,33),_DcnIfTransmitterFailed_Type())
dcnIfTransmitterFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfTransmitterFailed.setStatus(_B)
_DcnIfIllegalFrequency_Type=FaultStatus
_DcnIfIllegalFrequency_Object=MibTableColumn
dcnIfIllegalFrequency=_DcnIfIllegalFrequency_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,34),_DcnIfIllegalFrequency_Type())
dcnIfIllegalFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfIllegalFrequency.setStatus(_B)
_DcnIfUnexpectedTxFrequency_Type=FaultStatus
_DcnIfUnexpectedTxFrequency_Object=MibTableColumn
dcnIfUnexpectedTxFrequency=_DcnIfUnexpectedTxFrequency_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,35),_DcnIfUnexpectedTxFrequency_Type())
dcnIfUnexpectedTxFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfUnexpectedTxFrequency.setStatus(_B)
_DcnIfReceivedPowerHigh_Type=FaultStatus
_DcnIfReceivedPowerHigh_Object=MibTableColumn
dcnIfReceivedPowerHigh=_DcnIfReceivedPowerHigh_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,36),_DcnIfReceivedPowerHigh_Type())
dcnIfReceivedPowerHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfReceivedPowerHigh.setStatus(_B)
_DcnIfReceivedPowerLow_Type=FaultStatus
_DcnIfReceivedPowerLow_Object=MibTableColumn
dcnIfReceivedPowerLow=_DcnIfReceivedPowerLow_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,37),_DcnIfReceivedPowerLow_Type())
dcnIfReceivedPowerLow.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfReceivedPowerLow.setStatus(_B)
_DcnIfTrxMediaMismatch_Type=FaultStatus
_DcnIfTrxMediaMismatch_Object=MibTableColumn
dcnIfTrxMediaMismatch=_DcnIfTrxMediaMismatch_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,38),_DcnIfTrxMediaMismatch_Type())
dcnIfTrxMediaMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfTrxMediaMismatch.setStatus(_B)
_DcnIfProtocolVersionMismatch_Type=FaultStatus
_DcnIfProtocolVersionMismatch_Object=MibTableColumn
dcnIfProtocolVersionMismatch=_DcnIfProtocolVersionMismatch_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,39),_DcnIfProtocolVersionMismatch_Type())
dcnIfProtocolVersionMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfProtocolVersionMismatch.setStatus(_B)
_DcnIfRemoteDefectIndication_Type=FaultStatus
_DcnIfRemoteDefectIndication_Object=MibTableColumn
dcnIfRemoteDefectIndication=_DcnIfRemoteDefectIndication_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,40),_DcnIfRemoteDefectIndication_Type())
dcnIfRemoteDefectIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfRemoteDefectIndication.setStatus(_B)
class _DcnIfTraceTransmitted_Type(DisplayString):defaultValue=OctetString('')
_DcnIfTraceTransmitted_Type.__name__=_W
_DcnIfTraceTransmitted_Object=MibTableColumn
dcnIfTraceTransmitted=_DcnIfTraceTransmitted_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,41),_DcnIfTraceTransmitted_Type())
dcnIfTraceTransmitted.setMaxAccess(_E)
if mibBuilder.loadTexts:dcnIfTraceTransmitted.setStatus(_B)
_DcnIfTraceReceived_Type=DisplayString
_DcnIfTraceReceived_Object=MibTableColumn
dcnIfTraceReceived=_DcnIfTraceReceived_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,42),_DcnIfTraceReceived_Type())
dcnIfTraceReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfTraceReceived.setStatus(_B)
class _DcnIfTraceExpected_Type(DisplayString):defaultValue=OctetString('')
_DcnIfTraceExpected_Type.__name__=_W
_DcnIfTraceExpected_Object=MibTableColumn
dcnIfTraceExpected=_DcnIfTraceExpected_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,43),_DcnIfTraceExpected_Type())
dcnIfTraceExpected.setMaxAccess(_E)
if mibBuilder.loadTexts:dcnIfTraceExpected.setStatus(_B)
class _DcnIfTraceAlarmMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_DcnIfTraceAlarmMode_Type.__name__=_F
_DcnIfTraceAlarmMode_Object=MibTableColumn
dcnIfTraceAlarmMode=_DcnIfTraceAlarmMode_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,44),_DcnIfTraceAlarmMode_Type())
dcnIfTraceAlarmMode.setMaxAccess(_E)
if mibBuilder.loadTexts:dcnIfTraceAlarmMode.setStatus(_B)
_DcnIfTraceMismatch_Type=FaultStatus
_DcnIfTraceMismatch_Object=MibTableColumn
dcnIfTraceMismatch=_DcnIfTraceMismatch_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,55),_DcnIfTraceMismatch_Type())
dcnIfTraceMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfTraceMismatch.setStatus(_B)
class _DcnIfLaserMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('als',2)))
_DcnIfLaserMode_Type.__name__=_F
_DcnIfLaserMode_Object=MibTableColumn
dcnIfLaserMode=_DcnIfLaserMode_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,56),_DcnIfLaserMode_Type())
dcnIfLaserMode.setMaxAccess(_E)
if mibBuilder.loadTexts:dcnIfLaserMode.setStatus(_B)
_DcnIfLinkSupervisionFailure_Type=FaultStatus
_DcnIfLinkSupervisionFailure_Object=MibTableColumn
dcnIfLinkSupervisionFailure=_DcnIfLinkSupervisionFailure_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,57),_DcnIfLinkSupervisionFailure_Type())
dcnIfLinkSupervisionFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfLinkSupervisionFailure.setStatus(_B)
_DcnIfAid_Type=DisplayString
_DcnIfAid_Object=MibTableColumn
dcnIfAid=_DcnIfAid_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,58),_DcnIfAid_Type())
dcnIfAid.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfAid.setStatus(_B)
_DcnIfPhysicalLocation_Type=DisplayString
_DcnIfPhysicalLocation_Object=MibTableColumn
dcnIfPhysicalLocation=_DcnIfPhysicalLocation_Object((1,3,6,1,4,1,8708,2,20,2,2,1,1,59),_DcnIfPhysicalLocation_Type())
dcnIfPhysicalLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnIfPhysicalLocation.setStatus(_B)
_LumentisDcnNotifications_ObjectIdentity=ObjectIdentity
lumentisDcnNotifications=_LumentisDcnNotifications_ObjectIdentity((1,3,6,1,4,1,8708,2,20,2,3))
_DcnNotifyPrefix_ObjectIdentity=ObjectIdentity
dcnNotifyPrefix=_DcnNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,8708,2,20,2,3,0))
_DcnPppList_ObjectIdentity=ObjectIdentity
dcnPppList=_DcnPppList_ObjectIdentity((1,3,6,1,4,1,8708,2,20,2,4))
_DcnPppTable_Object=MibTable
dcnPppTable=_DcnPppTable_Object((1,3,6,1,4,1,8708,2,20,2,4,1))
if mibBuilder.loadTexts:dcnPppTable.setStatus(_B)
_DcnPppEntry_Object=MibTableRow
dcnPppEntry=_DcnPppEntry_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1))
dcnPppEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:dcnPppEntry.setStatus(_B)
class _DcnPppIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DcnPppIndex_Type.__name__=_e
_DcnPppIndex_Object=MibTableColumn
dcnPppIndex=_DcnPppIndex_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,1),_DcnPppIndex_Type())
dcnPppIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnPppIndex.setStatus(_B)
_DcnPppName_Type=MgmtNameString
_DcnPppName_Object=MibTableColumn
dcnPppName=_DcnPppName_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,2),_DcnPppName_Type())
dcnPppName.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnPppName.setStatus(_B)
class _DcnPppDescr_Type(DisplayString):defaultValue=OctetString('')
_DcnPppDescr_Type.__name__=_W
_DcnPppDescr_Object=MibTableColumn
dcnPppDescr=_DcnPppDescr_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,3),_DcnPppDescr_Type())
dcnPppDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:dcnPppDescr.setStatus(_B)
_DcnPppTxSubrack_Type=SubrackNumber
_DcnPppTxSubrack_Object=MibTableColumn
dcnPppTxSubrack=_DcnPppTxSubrack_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,4),_DcnPppTxSubrack_Type())
dcnPppTxSubrack.setMaxAccess(_I)
if mibBuilder.loadTexts:dcnPppTxSubrack.setStatus(_B)
_DcnPppTxSlot_Type=SlotNumber
_DcnPppTxSlot_Object=MibTableColumn
dcnPppTxSlot=_DcnPppTxSlot_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,5),_DcnPppTxSlot_Type())
dcnPppTxSlot.setMaxAccess(_I)
if mibBuilder.loadTexts:dcnPppTxSlot.setStatus(_B)
_DcnPppTxPort_Type=PortNumber
_DcnPppTxPort_Object=MibTableColumn
dcnPppTxPort=_DcnPppTxPort_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,6),_DcnPppTxPort_Type())
dcnPppTxPort.setMaxAccess(_I)
if mibBuilder.loadTexts:dcnPppTxPort.setStatus(_B)
_DcnPppRxSubrack_Type=SubrackNumber
_DcnPppRxSubrack_Object=MibTableColumn
dcnPppRxSubrack=_DcnPppRxSubrack_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,7),_DcnPppRxSubrack_Type())
dcnPppRxSubrack.setMaxAccess(_I)
if mibBuilder.loadTexts:dcnPppRxSubrack.setStatus(_B)
_DcnPppRxSlot_Type=SlotNumber
_DcnPppRxSlot_Object=MibTableColumn
dcnPppRxSlot=_DcnPppRxSlot_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,8),_DcnPppRxSlot_Type())
dcnPppRxSlot.setMaxAccess(_I)
if mibBuilder.loadTexts:dcnPppRxSlot.setStatus(_B)
_DcnPppRxPort_Type=PortNumber
_DcnPppRxPort_Object=MibTableColumn
dcnPppRxPort=_DcnPppRxPort_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,9),_DcnPppRxPort_Type())
dcnPppRxPort.setMaxAccess(_I)
if mibBuilder.loadTexts:dcnPppRxPort.setStatus(_B)
class _DcnPppInvPhysIndexOrZero_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DcnPppInvPhysIndexOrZero_Type.__name__=_e
_DcnPppInvPhysIndexOrZero_Object=MibTableColumn
dcnPppInvPhysIndexOrZero=_DcnPppInvPhysIndexOrZero_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,10),_DcnPppInvPhysIndexOrZero_Type())
dcnPppInvPhysIndexOrZero.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnPppInvPhysIndexOrZero.setStatus(_B)
class _DcnPppType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('proprietary',1),('osc',2),('sdh',3),('g709',4),('sonet',5)))
_DcnPppType_Type.__name__=_F
_DcnPppType_Object=MibTableColumn
dcnPppType=_DcnPppType_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,11),_DcnPppType_Type())
dcnPppType.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnPppType.setStatus(_B)
class _DcnPppAdminStatus_Type(BoardOrInterfaceAdminStatus):defaultValue=3
_DcnPppAdminStatus_Type.__name__=_x
_DcnPppAdminStatus_Object=MibTableColumn
dcnPppAdminStatus=_DcnPppAdminStatus_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,12),_DcnPppAdminStatus_Type())
dcnPppAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dcnPppAdminStatus.setStatus(_B)
class _DcnPppOperStatus_Type(BoardOrInterfaceOperStatus):defaultValue=1
_DcnPppOperStatus_Type.__name__=_A4
_DcnPppOperStatus_Object=MibTableColumn
dcnPppOperStatus=_DcnPppOperStatus_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,13),_DcnPppOperStatus_Type())
dcnPppOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnPppOperStatus.setStatus(_B)
_DcnPppRouteName_Type=MgmtNameString
_DcnPppRouteName_Object=MibTableColumn
dcnPppRouteName=_DcnPppRouteName_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,14),_DcnPppRouteName_Type())
dcnPppRouteName.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnPppRouteName.setStatus(_B)
_DcnPppDialCommand_Type=CommandString
_DcnPppDialCommand_Object=MibTableColumn
dcnPppDialCommand=_DcnPppDialCommand_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,15),_DcnPppDialCommand_Type())
dcnPppDialCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnPppDialCommand.setStatus(_B)
_DcnPppAcceptCommand_Type=CommandString
_DcnPppAcceptCommand_Object=MibTableColumn
dcnPppAcceptCommand=_DcnPppAcceptCommand_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,16),_DcnPppAcceptCommand_Type())
dcnPppAcceptCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnPppAcceptCommand.setStatus(_B)
class _DcnPppLogicalLinkId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,11))
_DcnPppLogicalLinkId_Type.__name__=_F
_DcnPppLogicalLinkId_Object=MibTableColumn
dcnPppLogicalLinkId=_DcnPppLogicalLinkId_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,17),_DcnPppLogicalLinkId_Type())
dcnPppLogicalLinkId.setMaxAccess(_I)
if mibBuilder.loadTexts:dcnPppLogicalLinkId.setStatus(_B)
_DcnPppObjectProperty_Type=ObjectProperty
_DcnPppObjectProperty_Object=MibTableColumn
dcnPppObjectProperty=_DcnPppObjectProperty_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,18),_DcnPppObjectProperty_Type())
dcnPppObjectProperty.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnPppObjectProperty.setStatus(_B)
class _DcnPppGccChannel_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2))
_DcnPppGccChannel_Type.__name__=_F
_DcnPppGccChannel_Object=MibTableColumn
dcnPppGccChannel=_DcnPppGccChannel_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,19),_DcnPppGccChannel_Type())
dcnPppGccChannel.setMaxAccess(_I)
if mibBuilder.loadTexts:dcnPppGccChannel.setStatus(_B)
class _DcnPppVlanId_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,4095))
_DcnPppVlanId_Type.__name__=_F
_DcnPppVlanId_Object=MibTableColumn
dcnPppVlanId=_DcnPppVlanId_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,20),_DcnPppVlanId_Type())
dcnPppVlanId.setMaxAccess(_I)
if mibBuilder.loadTexts:dcnPppVlanId.setStatus(_B)
class _DcnPppVlanEtherType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('qTag0x8100',1),('sTag0x88a8',2)))
_DcnPppVlanEtherType_Type.__name__=_F
_DcnPppVlanEtherType_Object=MibTableColumn
dcnPppVlanEtherType=_DcnPppVlanEtherType_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,21),_DcnPppVlanEtherType_Type())
dcnPppVlanEtherType.setMaxAccess(_E)
if mibBuilder.loadTexts:dcnPppVlanEtherType.setStatus(_B)
_DcnPppTxIfNo_Type=PortNumber
_DcnPppTxIfNo_Object=MibTableColumn
dcnPppTxIfNo=_DcnPppTxIfNo_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,22),_DcnPppTxIfNo_Type())
dcnPppTxIfNo.setMaxAccess(_I)
if mibBuilder.loadTexts:dcnPppTxIfNo.setStatus(_B)
_DcnPppRxIfNo_Type=PortNumber
_DcnPppRxIfNo_Object=MibTableColumn
dcnPppRxIfNo=_DcnPppRxIfNo_Object((1,3,6,1,4,1,8708,2,20,2,4,1,1,23),_DcnPppRxIfNo_Type())
dcnPppRxIfNo.setMaxAccess(_I)
if mibBuilder.loadTexts:dcnPppRxIfNo.setStatus(_B)
_DcnAddress_ObjectIdentity=ObjectIdentity
dcnAddress=_DcnAddress_ObjectIdentity((1,3,6,1,4,1,8708,2,20,2,5))
_DcnAddressCurrentPppAddress_Type=IpAddress
_DcnAddressCurrentPppAddress_Object=MibScalar
dcnAddressCurrentPppAddress=_DcnAddressCurrentPppAddress_Object((1,3,6,1,4,1,8708,2,20,2,5,1),_DcnAddressCurrentPppAddress_Type())
dcnAddressCurrentPppAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnAddressCurrentPppAddress.setStatus(_B)
_DcnAddressNextPppAddress_Type=IpAddress
_DcnAddressNextPppAddress_Object=MibScalar
dcnAddressNextPppAddress=_DcnAddressNextPppAddress_Object((1,3,6,1,4,1,8708,2,20,2,5,2),_DcnAddressNextPppAddress_Type())
dcnAddressNextPppAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:dcnAddressNextPppAddress.setStatus(_B)
_DcnEthList_ObjectIdentity=ObjectIdentity
dcnEthList=_DcnEthList_ObjectIdentity((1,3,6,1,4,1,8708,2,20,2,6))
_DcnEthTable_Object=MibTable
dcnEthTable=_DcnEthTable_Object((1,3,6,1,4,1,8708,2,20,2,6,1))
if mibBuilder.loadTexts:dcnEthTable.setStatus(_B)
_DcnEthEntry_Object=MibTableRow
dcnEthEntry=_DcnEthEntry_Object((1,3,6,1,4,1,8708,2,20,2,6,1,1))
dcnEthEntry.setIndexNames((0,_A,_y))
if mibBuilder.loadTexts:dcnEthEntry.setStatus(_B)
class _DcnEthIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DcnEthIndex_Type.__name__=_e
_DcnEthIndex_Object=MibTableColumn
dcnEthIndex=_DcnEthIndex_Object((1,3,6,1,4,1,8708,2,20,2,6,1,1,1),_DcnEthIndex_Type())
dcnEthIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnEthIndex.setStatus(_B)
_DcnEthName_Type=MgmtNameString
_DcnEthName_Object=MibTableColumn
dcnEthName=_DcnEthName_Object((1,3,6,1,4,1,8708,2,20,2,6,1,1,2),_DcnEthName_Type())
dcnEthName.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnEthName.setStatus(_B)
class _DcnEthDescr_Type(DisplayString):defaultValue=OctetString('')
_DcnEthDescr_Type.__name__=_W
_DcnEthDescr_Object=MibTableColumn
dcnEthDescr=_DcnEthDescr_Object((1,3,6,1,4,1,8708,2,20,2,6,1,1,3),_DcnEthDescr_Type())
dcnEthDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:dcnEthDescr.setStatus(_B)
_DcnEthSubrack_Type=SubrackNumber
_DcnEthSubrack_Object=MibTableColumn
dcnEthSubrack=_DcnEthSubrack_Object((1,3,6,1,4,1,8708,2,20,2,6,1,1,4),_DcnEthSubrack_Type())
dcnEthSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnEthSubrack.setStatus(_B)
_DcnEthSlot_Type=SlotNumber
_DcnEthSlot_Object=MibTableColumn
dcnEthSlot=_DcnEthSlot_Object((1,3,6,1,4,1,8708,2,20,2,6,1,1,5),_DcnEthSlot_Type())
dcnEthSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnEthSlot.setStatus(_B)
_DcnEthPort_Type=PortNumber
_DcnEthPort_Object=MibTableColumn
dcnEthPort=_DcnEthPort_Object((1,3,6,1,4,1,8708,2,20,2,6,1,1,6),_DcnEthPort_Type())
dcnEthPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnEthPort.setStatus(_B)
class _DcnEthAutoNegotiationMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_DcnEthAutoNegotiationMode_Type.__name__=_F
_DcnEthAutoNegotiationMode_Object=MibTableColumn
dcnEthAutoNegotiationMode=_DcnEthAutoNegotiationMode_Object((1,3,6,1,4,1,8708,2,20,2,6,1,1,7),_DcnEthAutoNegotiationMode_Type())
dcnEthAutoNegotiationMode.setMaxAccess(_I)
if mibBuilder.loadTexts:dcnEthAutoNegotiationMode.setStatus(_B)
class _DcnEthLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('up',0),('down',1),('unknown',2)))
_DcnEthLinkStatus_Type.__name__=_F
_DcnEthLinkStatus_Object=MibTableColumn
dcnEthLinkStatus=_DcnEthLinkStatus_Object((1,3,6,1,4,1,8708,2,20,2,6,1,1,8),_DcnEthLinkStatus_Type())
dcnEthLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnEthLinkStatus.setStatus(_B)
class _DcnEthSpeed_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('mbps10',0),('mbps100',1),('auto',2),('mbps1000',3)))
_DcnEthSpeed_Type.__name__=_F
_DcnEthSpeed_Object=MibTableColumn
dcnEthSpeed=_DcnEthSpeed_Object((1,3,6,1,4,1,8708,2,20,2,6,1,1,9),_DcnEthSpeed_Type())
dcnEthSpeed.setMaxAccess(_I)
if mibBuilder.loadTexts:dcnEthSpeed.setStatus(_B)
class _DcnEthDuplexCapability_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('half',1),('full',2),('both',3)))
_DcnEthDuplexCapability_Type.__name__=_F
_DcnEthDuplexCapability_Object=MibTableColumn
dcnEthDuplexCapability=_DcnEthDuplexCapability_Object((1,3,6,1,4,1,8708,2,20,2,6,1,1,10),_DcnEthDuplexCapability_Type())
dcnEthDuplexCapability.setMaxAccess(_I)
if mibBuilder.loadTexts:dcnEthDuplexCapability.setStatus(_B)
class _DcnEthRateLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,125))
_DcnEthRateLimit_Type.__name__=_F
_DcnEthRateLimit_Object=MibTableColumn
dcnEthRateLimit=_DcnEthRateLimit_Object((1,3,6,1,4,1,8708,2,20,2,6,1,1,11),_DcnEthRateLimit_Type())
dcnEthRateLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:dcnEthRateLimit.setStatus(_B)
class _DcnEthFlowControlMode_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noPause',1),('rxPause',2),('txPause',3),('bothPause',4)))
_DcnEthFlowControlMode_Type.__name__=_F
_DcnEthFlowControlMode_Object=MibTableColumn
dcnEthFlowControlMode=_DcnEthFlowControlMode_Object((1,3,6,1,4,1,8708,2,20,2,6,1,1,12),_DcnEthFlowControlMode_Type())
dcnEthFlowControlMode.setMaxAccess(_E)
if mibBuilder.loadTexts:dcnEthFlowControlMode.setStatus(_B)
_DcnEthObjectProperty_Type=ObjectProperty
_DcnEthObjectProperty_Object=MibTableColumn
dcnEthObjectProperty=_DcnEthObjectProperty_Object((1,3,6,1,4,1,8708,2,20,2,6,1,1,13),_DcnEthObjectProperty_Type())
dcnEthObjectProperty.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnEthObjectProperty.setStatus(_B)
_DcnEthChangeSpeedCommand_Type=CommandString
_DcnEthChangeSpeedCommand_Object=MibTableColumn
dcnEthChangeSpeedCommand=_DcnEthChangeSpeedCommand_Object((1,3,6,1,4,1,8708,2,20,2,6,1,1,15),_DcnEthChangeSpeedCommand_Type())
dcnEthChangeSpeedCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnEthChangeSpeedCommand.setStatus(_B)
class _DcnEthAdminStatus_Type(BoardOrInterfaceAdminStatus):defaultValue=3
_DcnEthAdminStatus_Type.__name__=_x
_DcnEthAdminStatus_Object=MibTableColumn
dcnEthAdminStatus=_DcnEthAdminStatus_Object((1,3,6,1,4,1,8708,2,20,2,6,1,1,16),_DcnEthAdminStatus_Type())
dcnEthAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dcnEthAdminStatus.setStatus(_B)
class _DcnEthOperStatus_Type(BoardOrInterfaceOperStatus):defaultValue=1
_DcnEthOperStatus_Type.__name__=_A4
_DcnEthOperStatus_Object=MibTableColumn
dcnEthOperStatus=_DcnEthOperStatus_Object((1,3,6,1,4,1,8708,2,20,2,6,1,1,17),_DcnEthOperStatus_Type())
dcnEthOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnEthOperStatus.setStatus(_B)
_DcnCcList_ObjectIdentity=ObjectIdentity
dcnCcList=_DcnCcList_ObjectIdentity((1,3,6,1,4,1,8708,2,20,2,7))
_DcnCcTable_Object=MibTable
dcnCcTable=_DcnCcTable_Object((1,3,6,1,4,1,8708,2,20,2,7,1))
if mibBuilder.loadTexts:dcnCcTable.setStatus(_B)
_DcnCcEntry_Object=MibTableRow
dcnCcEntry=_DcnCcEntry_Object((1,3,6,1,4,1,8708,2,20,2,7,1,1))
dcnCcEntry.setIndexNames((0,_A,_Ai))
if mibBuilder.loadTexts:dcnCcEntry.setStatus(_B)
class _DcnCcIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DcnCcIndex_Type.__name__=_e
_DcnCcIndex_Object=MibTableColumn
dcnCcIndex=_DcnCcIndex_Object((1,3,6,1,4,1,8708,2,20,2,7,1,1,1),_DcnCcIndex_Type())
dcnCcIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnCcIndex.setStatus(_B)
_DcnCcName_Type=MgmtNameString
_DcnCcName_Object=MibTableColumn
dcnCcName=_DcnCcName_Object((1,3,6,1,4,1,8708,2,20,2,7,1,1,2),_DcnCcName_Type())
dcnCcName.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnCcName.setStatus(_B)
class _DcnCcDescr_Type(DisplayString):defaultValue=OctetString('')
_DcnCcDescr_Type.__name__=_W
_DcnCcDescr_Object=MibTableColumn
dcnCcDescr=_DcnCcDescr_Object((1,3,6,1,4,1,8708,2,20,2,7,1,1,3),_DcnCcDescr_Type())
dcnCcDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:dcnCcDescr.setStatus(_B)
_DcnCcSubrack_Type=SubrackNumber
_DcnCcSubrack_Object=MibTableColumn
dcnCcSubrack=_DcnCcSubrack_Object((1,3,6,1,4,1,8708,2,20,2,7,1,1,4),_DcnCcSubrack_Type())
dcnCcSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnCcSubrack.setStatus(_B)
_DcnCcSlot_Type=SlotNumber
_DcnCcSlot_Object=MibTableColumn
dcnCcSlot=_DcnCcSlot_Object((1,3,6,1,4,1,8708,2,20,2,7,1,1,5),_DcnCcSlot_Type())
dcnCcSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnCcSlot.setStatus(_B)
_DcnCcTxPort_Type=PortNumber
_DcnCcTxPort_Object=MibTableColumn
dcnCcTxPort=_DcnCcTxPort_Object((1,3,6,1,4,1,8708,2,20,2,7,1,1,6),_DcnCcTxPort_Type())
dcnCcTxPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnCcTxPort.setStatus(_B)
_DcnCcRxPort_Type=PortNumber
_DcnCcRxPort_Object=MibTableColumn
dcnCcRxPort=_DcnCcRxPort_Object((1,3,6,1,4,1,8708,2,20,2,7,1,1,7),_DcnCcRxPort_Type())
dcnCcRxPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnCcRxPort.setStatus(_B)
class _DcnCcAdminStatus_Type(BoardOrInterfaceAdminStatus):defaultValue=1
_DcnCcAdminStatus_Type.__name__=_x
_DcnCcAdminStatus_Object=MibTableColumn
dcnCcAdminStatus=_DcnCcAdminStatus_Object((1,3,6,1,4,1,8708,2,20,2,7,1,1,8),_DcnCcAdminStatus_Type())
dcnCcAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dcnCcAdminStatus.setStatus(_B)
class _DcnCcChannelStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('notPresent',1),('down',2),('calling',3),('up',4),('waitToHangup',5),('broken',6),('restarting',7)))
_DcnCcChannelStatus_Type.__name__=_F
_DcnCcChannelStatus_Object=MibTableColumn
dcnCcChannelStatus=_DcnCcChannelStatus_Object((1,3,6,1,4,1,8708,2,20,2,7,1,1,9),_DcnCcChannelStatus_Type())
dcnCcChannelStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnCcChannelStatus.setStatus(_B)
_DcnCcErrorCounter_Type=Counter32
_DcnCcErrorCounter_Object=MibTableColumn
dcnCcErrorCounter=_DcnCcErrorCounter_Object((1,3,6,1,4,1,8708,2,20,2,7,1,1,10),_DcnCcErrorCounter_Type())
dcnCcErrorCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnCcErrorCounter.setStatus(_B)
class _DcnCcResetCounter_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('reset',2)))
_DcnCcResetCounter_Type.__name__=_F
_DcnCcResetCounter_Object=MibTableColumn
dcnCcResetCounter=_DcnCcResetCounter_Object((1,3,6,1,4,1,8708,2,20,2,7,1,1,11),_DcnCcResetCounter_Type())
dcnCcResetCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:dcnCcResetCounter.setStatus(_B)
_DcnCcFecFailure_Type=FaultStatus
_DcnCcFecFailure_Object=MibTableColumn
dcnCcFecFailure=_DcnCcFecFailure_Object((1,3,6,1,4,1,8708,2,20,2,7,1,1,12),_DcnCcFecFailure_Type())
dcnCcFecFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnCcFecFailure.setStatus(_B)
_DcnCcTrxNotSupportCommChannel_Type=FaultStatus
_DcnCcTrxNotSupportCommChannel_Object=MibTableColumn
dcnCcTrxNotSupportCommChannel=_DcnCcTrxNotSupportCommChannel_Object((1,3,6,1,4,1,8708,2,20,2,7,1,1,13),_DcnCcTrxNotSupportCommChannel_Type())
dcnCcTrxNotSupportCommChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnCcTrxNotSupportCommChannel.setStatus(_B)
_DcnCcConfigurationMismatch_Type=FaultStatus
_DcnCcConfigurationMismatch_Object=MibTableColumn
dcnCcConfigurationMismatch=_DcnCcConfigurationMismatch_Object((1,3,6,1,4,1,8708,2,20,2,7,1,1,14),_DcnCcConfigurationMismatch_Type())
dcnCcConfigurationMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:dcnCcConfigurationMismatch.setStatus(_B)
dcnGeneralGroup=ObjectGroup((1,3,6,1,4,1,8708,2,20,1,1,1))
dcnGeneralGroup.setObjects(*((_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:dcnGeneralGroup.setStatus(_D)
dcnIfGroup=ObjectGroup((1,3,6,1,4,1,8708,2,20,1,1,2))
dcnIfGroup.setObjects(*((_A,_K),(_A,_X),(_A,_k),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_c),(_A,_r)))
if mibBuilder.loadTexts:dcnIfGroup.setStatus(_D)
dcnPppGroup=ObjectGroup((1,3,6,1,4,1,8708,2,20,1,1,4))
dcnPppGroup.setObjects(*((_A,_J),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:dcnPppGroup.setStatus(_D)
dcnPppGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,20,1,1,5))
dcnPppGroupV2.setObjects(*((_A,_J),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_d)))
if mibBuilder.loadTexts:dcnPppGroupV2.setStatus(_D)
dcnAddressGroup=ObjectGroup((1,3,6,1,4,1,8708,2,20,1,1,6))
dcnAddressGroup.setObjects(*((_A,_B0),(_A,_B1)))
if mibBuilder.loadTexts:dcnAddressGroup.setStatus(_B)
dcnPppGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,20,1,1,7))
dcnPppGroupV3.setObjects(*((_A,_J),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_d),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:dcnPppGroupV3.setStatus(_D)
dcnPppGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,20,1,1,8))
dcnPppGroupV4.setObjects(*((_A,_J),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_d),(_A,_f),(_A,_g),(_A,_s)))
if mibBuilder.loadTexts:dcnPppGroupV4.setStatus(_D)
dcnGeneralGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,20,1,1,9))
dcnGeneralGroupV2.setObjects(*((_A,_A5),(_A,_A6),(_A,_Aj),(_A,_Ak)))
if mibBuilder.loadTexts:dcnGeneralGroupV2.setStatus(_D)
dcnIfGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,20,1,1,10))
dcnIfGroupV2.setObjects(*((_A,_K),(_A,_X),(_A,_k),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_c),(_A,_r),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:dcnIfGroupV2.setStatus(_D)
dcnPppGroupV5=ObjectGroup((1,3,6,1,4,1,8708,2,20,1,1,11))
dcnPppGroupV5.setObjects(*((_A,_J),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_d),(_A,_A1),(_A,_f),(_A,_g),(_A,_s),(_A,_A2)))
if mibBuilder.loadTexts:dcnPppGroupV5.setStatus(_D)
dcnIfGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,20,1,1,12))
dcnIfGroupV3.setObjects(*((_A,_K),(_A,_X),(_A,_k),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_c),(_A,_r),(_A,_z),(_A,_A0),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR)))
if mibBuilder.loadTexts:dcnIfGroupV3.setStatus(_D)
dcnIfGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,20,1,1,13))
dcnIfGroupV4.setObjects(*((_A,_K),(_A,_X),(_A,_k),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_c),(_A,_r),(_A,_z),(_A,_A0),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At)))
if mibBuilder.loadTexts:dcnIfGroupV4.setStatus(_D)
dcnPppGroupV6=ObjectGroup((1,3,6,1,4,1,8708,2,20,1,1,14))
dcnPppGroupV6.setObjects(*((_A,_J),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_d),(_A,_A1),(_A,_f),(_A,_g),(_A,_s),(_A,_A2),(_A,_AS)))
if mibBuilder.loadTexts:dcnPppGroupV6.setStatus(_D)
dcnEthGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,20,1,1,15))
dcnEthGroupV1.setObjects(*((_A,_y),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae)))
if mibBuilder.loadTexts:dcnEthGroupV1.setStatus(_D)
dcnGeneralGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,20,1,1,16))
dcnGeneralGroupV3.setObjects(*((_A,_A5),(_A,_A6),(_A,_Aj),(_A,_Ak)))
if mibBuilder.loadTexts:dcnGeneralGroupV3.setStatus(_B)
dcnEthGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,20,1,1,17))
dcnEthGroupV2.setObjects(*((_A,_y),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Au)))
if mibBuilder.loadTexts:dcnEthGroupV2.setStatus(_D)
dcnCcGroup=ObjectGroup((1,3,6,1,4,1,8708,2,20,1,1,18))
dcnCcGroup.setObjects(*((_A,_Ai),(_A,_B2),(_A,_B3),(_A,_B4),(_A,_B5),(_A,_B6),(_A,_B7),(_A,_B8),(_A,_B9),(_A,_BA),(_A,_BB),(_A,_BC),(_A,_BD),(_A,_BE)))
if mibBuilder.loadTexts:dcnCcGroup.setStatus(_B)
dcnIfGroupV5=ObjectGroup((1,3,6,1,4,1,8708,2,20,1,1,19))
dcnIfGroupV5.setObjects(*((_A,_K),(_A,_X),(_A,_k),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_c),(_A,_r),(_A,_z),(_A,_A0),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,'dcnIfAid'),(_A,_BF)))
if mibBuilder.loadTexts:dcnIfGroupV5.setStatus(_B)
dcnPppGroupV7=ObjectGroup((1,3,6,1,4,1,8708,2,20,1,1,20))
dcnPppGroupV7.setObjects(*((_A,_J),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_d),(_A,_A1),(_A,_f),(_A,_g),(_A,_s),(_A,_A2),(_A,_AS),(_A,_Av),(_A,_Aw)))
if mibBuilder.loadTexts:dcnPppGroupV7.setStatus(_D)
dcnEthGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,20,1,1,21))
dcnEthGroupV3.setObjects(*((_A,_y),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Au),(_A,_BG),(_A,_BH)))
if mibBuilder.loadTexts:dcnEthGroupV3.setStatus(_B)
dcnPppGroupV8=ObjectGroup((1,3,6,1,4,1,8708,2,20,1,1,22))
dcnPppGroupV8.setObjects(*((_A,_J),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_BI),(_A,_P),(_A,_Q),(_A,_R),(_A,_BJ),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_d),(_A,_A1),(_A,_f),(_A,_g),(_A,_s),(_A,_A2),(_A,_AS),(_A,_Av),(_A,_Aw)))
if mibBuilder.loadTexts:dcnPppGroupV8.setStatus(_B)
dcnIfTxSignalStatusDown=NotificationType((1,3,6,1,4,1,8708,2,20,2,3,0,1))
dcnIfTxSignalStatusDown.setObjects(*((_A,_K),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:dcnIfTxSignalStatusDown.setStatus(_B)
dcnIfTxSignalStatusUp=NotificationType((1,3,6,1,4,1,8708,2,20,2,3,0,2))
dcnIfTxSignalStatusUp.setObjects(*((_A,_K),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:dcnIfTxSignalStatusUp.setStatus(_B)
dcnNotificationGroup=NotificationGroup((1,3,6,1,4,1,8708,2,20,1,1,3))
dcnNotificationGroup.setObjects(*((_A,_BK),(_A,_BL)))
if mibBuilder.loadTexts:dcnNotificationGroup.setStatus(_B)
lumDcnBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,20,1,2,1))
lumDcnBasicComplV1.setObjects(*((_A,_t),(_A,_h),(_A,_G)))
if mibBuilder.loadTexts:lumDcnBasicComplV1.setStatus(_D)
lumDcnBasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,20,1,2,2))
lumDcnBasicComplV2.setObjects(*((_A,_t),(_A,_h),(_A,_G),(_A,_BM)))
if mibBuilder.loadTexts:lumDcnBasicComplV2.setStatus(_D)
lumDcnBasicComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,20,1,2,3))
lumDcnBasicComplV3.setObjects(*((_A,_t),(_A,_h),(_A,_G),(_A,_Ax)))
if mibBuilder.loadTexts:lumDcnBasicComplV3.setStatus(_D)
lumDcnBasicComplV4=ModuleCompliance((1,3,6,1,4,1,8708,2,20,1,2,4))
lumDcnBasicComplV4.setObjects(*((_A,_t),(_A,_h),(_A,_G),(_A,_Ax),(_A,_H)))
if mibBuilder.loadTexts:lumDcnBasicComplV4.setStatus(_D)
lumDcnBasicComplV5=ModuleCompliance((1,3,6,1,4,1,8708,2,20,1,2,5))
lumDcnBasicComplV5.setObjects(*((_A,_t),(_A,_h),(_A,_G),(_A,_BN),(_A,_H)))
if mibBuilder.loadTexts:lumDcnBasicComplV5.setStatus(_D)
lumDcnBasicComplV6=ModuleCompliance((1,3,6,1,4,1,8708,2,20,1,2,6))
lumDcnBasicComplV6.setObjects(*((_A,_i),(_A,_h),(_A,_G),(_A,_BO),(_A,_H)))
if mibBuilder.loadTexts:lumDcnBasicComplV6.setStatus(_D)
lumDcnBasicComplV7=ModuleCompliance((1,3,6,1,4,1,8708,2,20,1,2,7))
lumDcnBasicComplV7.setObjects(*((_A,_i),(_A,_BP),(_A,_G),(_A,_Af),(_A,_H)))
if mibBuilder.loadTexts:lumDcnBasicComplV7.setStatus(_D)
lumDcnBasicComplV8=ModuleCompliance((1,3,6,1,4,1,8708,2,20,1,2,8))
lumDcnBasicComplV8.setObjects(*((_A,_i),(_A,_BQ),(_A,_G),(_A,_Af),(_A,_H)))
if mibBuilder.loadTexts:lumDcnBasicComplV8.setStatus(_D)
lumDcnBasicComplV9=ModuleCompliance((1,3,6,1,4,1,8708,2,20,1,2,9))
lumDcnBasicComplV9.setObjects(*((_A,_i),(_A,_u),(_A,_G),(_A,_Af),(_A,_H)))
if mibBuilder.loadTexts:lumDcnBasicComplV9.setStatus(_D)
lumDcnBasicComplV10=ModuleCompliance((1,3,6,1,4,1,8708,2,20,1,2,10))
lumDcnBasicComplV10.setObjects(*((_A,_i),(_A,_u),(_A,_G),(_A,_v),(_A,_H)))
if mibBuilder.loadTexts:lumDcnBasicComplV10.setStatus(_D)
lumDcnBasicComplV11=ModuleCompliance((1,3,6,1,4,1,8708,2,20,1,2,11))
lumDcnBasicComplV11.setObjects(*((_A,_i),(_A,_u),(_A,_G),(_A,_v),(_A,_H),(_A,_BR)))
if mibBuilder.loadTexts:lumDcnBasicComplV11.setStatus(_D)
lumDcnBasicComplV12=ModuleCompliance((1,3,6,1,4,1,8708,2,20,1,2,12))
lumDcnBasicComplV12.setObjects(*((_A,_j),(_A,_u),(_A,_G),(_A,_v),(_A,_H),(_A,_Ag)))
if mibBuilder.loadTexts:lumDcnBasicComplV12.setStatus(_D)
lumDcnBasicComplV13=ModuleCompliance((1,3,6,1,4,1,8708,2,20,1,2,13))
lumDcnBasicComplV13.setObjects(*((_A,_j),(_A,_u),(_A,_G),(_A,_v),(_A,_H),(_A,_Ag),(_A,_w)))
if mibBuilder.loadTexts:lumDcnBasicComplV13.setStatus(_D)
lumDcnBasicComplV14=ModuleCompliance((1,3,6,1,4,1,8708,2,20,1,2,14))
lumDcnBasicComplV14.setObjects(*((_A,_j),(_A,_A3),(_A,_G),(_A,_v),(_A,_H),(_A,_Ag),(_A,_w)))
if mibBuilder.loadTexts:lumDcnBasicComplV14.setStatus(_D)
lumDcnBasicComplV15=ModuleCompliance((1,3,6,1,4,1,8708,2,20,1,2,15))
lumDcnBasicComplV15.setObjects(*((_A,_j),(_A,_A3),(_A,_G),(_A,_Ay),(_A,_H),(_A,_Ah),(_A,_w)))
if mibBuilder.loadTexts:lumDcnBasicComplV15.setStatus(_D)
lumDcnBasicComplV16=ModuleCompliance((1,3,6,1,4,1,8708,2,20,1,2,16))
lumDcnBasicComplV16.setObjects(*((_A,_j),(_A,_A3),(_A,_G),(_A,_Ay),(_A,_H),(_A,_Ah),(_A,_w)))
if mibBuilder.loadTexts:lumDcnBasicComplV16.setStatus(_D)
lumDcnBasicComplV17=ModuleCompliance((1,3,6,1,4,1,8708,2,20,1,2,17))
lumDcnBasicComplV17.setObjects(*((_A,_j),(_A,_A3),(_A,_G),(_A,_BS),(_A,_H),(_A,_Ah),(_A,_w)))
if mibBuilder.loadTexts:lumDcnBasicComplV17.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'DcnSignalType':DcnSignalType,_A_:DcnOscMode,'lumDcnMIBModule':lumDcnMIBModule,'lumDcnConfs':lumDcnConfs,'lumDcnGroups':lumDcnGroups,_t:dcnGeneralGroup,_h:dcnIfGroup,_G:dcnNotificationGroup,_BM:dcnPppGroup,_Ax:dcnPppGroupV2,_H:dcnAddressGroup,_BN:dcnPppGroupV3,_BO:dcnPppGroupV4,_i:dcnGeneralGroupV2,_BP:dcnIfGroupV2,_Af:dcnPppGroupV5,_BQ:dcnIfGroupV3,_u:dcnIfGroupV4,_v:dcnPppGroupV6,_BR:dcnEthGroupV1,_j:dcnGeneralGroupV3,_Ag:dcnEthGroupV2,_w:dcnCcGroup,_A3:dcnIfGroupV5,_Ay:dcnPppGroupV7,_Ah:dcnEthGroupV3,_BS:dcnPppGroupV8,'lumDcnCompl':lumDcnCompl,'lumDcnBasicComplV1':lumDcnBasicComplV1,'lumDcnBasicComplV2':lumDcnBasicComplV2,'lumDcnBasicComplV3':lumDcnBasicComplV3,'lumDcnBasicComplV4':lumDcnBasicComplV4,'lumDcnBasicComplV5':lumDcnBasicComplV5,'lumDcnBasicComplV6':lumDcnBasicComplV6,'lumDcnBasicComplV7':lumDcnBasicComplV7,'lumDcnBasicComplV8':lumDcnBasicComplV8,'lumDcnBasicComplV9':lumDcnBasicComplV9,'lumDcnBasicComplV10':lumDcnBasicComplV10,'lumDcnBasicComplV11':lumDcnBasicComplV11,'lumDcnBasicComplV12':lumDcnBasicComplV12,'lumDcnBasicComplV13':lumDcnBasicComplV13,'lumDcnBasicComplV14':lumDcnBasicComplV14,'lumDcnBasicComplV15':lumDcnBasicComplV15,'lumDcnBasicComplV16':lumDcnBasicComplV16,'lumDcnBasicComplV17':lumDcnBasicComplV17,'lumDcnMIBObjects':lumDcnMIBObjects,'dcnGeneral':dcnGeneral,_A5:dcnGeneralLastChangeTime,_A6:dcnGeneralStateLastChangeTime,_Aj:dcnGeneralDcnIfTableSize,_Ak:dcnGeneralDcnPppTableSize,'dcnGeneralDcnEthTableSize':dcnGeneralDcnEthTableSize,'dcnGeneralDcnCcTableSize':dcnGeneralDcnCcTableSize,'dcnIfList':dcnIfList,'dcnIfTable':dcnIfTable,'dcnIfEntry':dcnIfEntry,_K:dcnIfIndex,_X:dcnIfName,_k:dcnIfDescr,_Y:dcnIfSubrack,_Z:dcnIfSlot,_a:dcnIfTxPort,_b:dcnIfRxPort,_l:dcnIfInvPhysIndexOrZero,_m:dcnIfType,_n:dcnIfMaxSpeed,_o:dcnIfOscMode,_p:dcnIfAdminStatus,_q:dcnIfOperStatus,_c:dcnIfTxSignalStatus,_r:dcnIfLinkDown,_z:dcnIfTxFrequency,_A0:dcnIfObjectProperty,_A7:dcnIfLaserStatus,_AD:dcnIfPowerLevel,_AE:dcnIfTxPowerLevel,_AB:dcnIfReceiverSensitivity,_AC:dcnIfPowerLevelLowRelativeThreshold,_AF:dcnIfLaserTempActual,_AA:dcnIfTrxClass,_A8:dcnIfHighSpeedMin,_A9:dcnIfHighSpeedMax,_AG:dcnIfExpectedTxFrequency,_AH:dcnIfLaserBias,_AI:dcnIfLossOfSignal,_AL:dcnIfTrxCodeMismatch,_AJ:dcnIfTrxBitrateUnavailable,_AK:dcnIfTrxMissing,_AM:dcnIfTransmitterFailed,_AN:dcnIfIllegalFrequency,_AO:dcnIfUnexpectedTxFrequency,_AP:dcnIfReceivedPowerHigh,_AQ:dcnIfReceivedPowerLow,_AR:dcnIfTrxMediaMismatch,_Al:dcnIfProtocolVersionMismatch,_Am:dcnIfRemoteDefectIndication,_An:dcnIfTraceTransmitted,_Ao:dcnIfTraceReceived,_Ap:dcnIfTraceExpected,_Aq:dcnIfTraceAlarmMode,_Ar:dcnIfTraceMismatch,_As:dcnIfLaserMode,_At:dcnIfLinkSupervisionFailure,'dcnIfAid':dcnIfAid,_BF:dcnIfPhysicalLocation,'lumentisDcnNotifications':lumentisDcnNotifications,'dcnNotifyPrefix':dcnNotifyPrefix,_BK:dcnIfTxSignalStatusDown,_BL:dcnIfTxSignalStatusUp,'dcnPppList':dcnPppList,'dcnPppTable':dcnPppTable,'dcnPppEntry':dcnPppEntry,_J:dcnPppIndex,_L:dcnPppName,_M:dcnPppDescr,_N:dcnPppTxSubrack,_O:dcnPppTxSlot,_P:dcnPppTxPort,_Q:dcnPppRxSubrack,_R:dcnPppRxSlot,_S:dcnPppRxPort,_T:dcnPppInvPhysIndexOrZero,_U:dcnPppType,_V:dcnPppAdminStatus,_d:dcnPppOperStatus,_A1:dcnPppRouteName,_f:dcnPppDialCommand,_g:dcnPppAcceptCommand,_s:dcnPppLogicalLinkId,_A2:dcnPppObjectProperty,_AS:dcnPppGccChannel,_Av:dcnPppVlanId,_Aw:dcnPppVlanEtherType,_BI:dcnPppTxIfNo,_BJ:dcnPppRxIfNo,'dcnAddress':dcnAddress,_B0:dcnAddressCurrentPppAddress,_B1:dcnAddressNextPppAddress,'dcnEthList':dcnEthList,'dcnEthTable':dcnEthTable,'dcnEthEntry':dcnEthEntry,_y:dcnEthIndex,_AT:dcnEthName,_AU:dcnEthDescr,_AV:dcnEthSubrack,_AW:dcnEthSlot,_AX:dcnEthPort,_AY:dcnEthAutoNegotiationMode,_AZ:dcnEthLinkStatus,_Aa:dcnEthSpeed,_Ab:dcnEthDuplexCapability,_Ac:dcnEthRateLimit,_Ad:dcnEthFlowControlMode,_Ae:dcnEthObjectProperty,_Au:dcnEthChangeSpeedCommand,_BG:dcnEthAdminStatus,_BH:dcnEthOperStatus,'dcnCcList':dcnCcList,'dcnCcTable':dcnCcTable,'dcnCcEntry':dcnCcEntry,_Ai:dcnCcIndex,_B2:dcnCcName,_B3:dcnCcDescr,_B4:dcnCcSubrack,_B5:dcnCcSlot,_B6:dcnCcTxPort,_B7:dcnCcRxPort,_B8:dcnCcAdminStatus,_B9:dcnCcChannelStatus,_BA:dcnCcErrorCounter,_BB:dcnCcResetCounter,_BC:dcnCcFecFailure,_BD:dcnCcTrxNotSupportCommChannel,_BE:dcnCcConfigurationMismatch})