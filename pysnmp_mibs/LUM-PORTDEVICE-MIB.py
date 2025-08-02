_BJ='portDevGenericGroupV2'
_BI='portDevEquipmentGroupV4'
_BH='portDevEquipmentGroupV3'
_BG='portDevEquipmentGroupV2'
_BF='portDevEquipmentGroupV1'
_BE='portDevGenericCreateNewPortDeviceAdvanced'
_BD='portDevEquipmentLosCsf'
_BC='portDevIwfPmE1ChannelId'
_BB='portDevIwfDestMacAddress'
_BA='portDevIwfE1ChannelKLM'
_B9='portDevIwfE1ChannelId'
_B8='portDevIwfVlanPriority'
_B7='portDevIwfVlanId'
_B6='portDevIwfSignalFormat'
_B5='portDevIwfEtherType'
_B4='portDevIwfDescr'
_B3='portDevIwfOperStatus'
_B2='portDevIwfAdminStatus'
_B1='portDevIwfMultiplexSectionRDI'
_B0='portDevIwfMultiplexSectionAlarm'
_A_='portDevIwfTributaryUnitAlarm'
_Az='portDevFwUpgradeStatus'
_Ay='portDevFwGetAllFiles'
_Ax='portDevFwActivateFw'
_Aw='portDevFwInstallFw'
_Av='portDevFwImgSlotTwoDate'
_Au='portDevFwImgSlotTwoState'
_At='portDevFwImgSlotTwoVersion'
_As='portDevFwImgSlotTwoNr'
_Ar='portDevFwImgSlotOneDate'
_Aq='portDevFwImgSlotOneState'
_Ap='portDevFwImgSlotOneVersion'
_Ao='portDevFwImgSlotOneNr'
_An='portDevFwPortDevId'
_Am='portDevFwName'
_Al='portDevFwSlot'
_Ak='portDevFwSubrack'
_Aj='portDevGeneralIwfPmTableSize'
_Ai='portDevGeneralIwfTableSize'
_Ah='portDevGeneralFwTableSize'
_Ag='portDevGeneralEquipmentTableSize'
_Af='portDevGeneralGenericTableSize'
_Ae='portDevGeneralStateLastChangeTime'
_Ad='portDevGeneralLastChangeTime'
_Ac='PortDeviceEquipmentType'
_Ab='undefined'
_Aa='portDevEquipmentGroupV5'
_AZ='portDevIwfPmInternalReference'
_AY='portDevIwfPmReset'
_AX='portDevIwfPmJbUnderrun'
_AW='portDevIwfPmJbOverrun'
_AV='portDevIwfPmPlayedOutPackets'
_AU='portDevIwfPmMissingPackets'
_AT='portDevIwfPmMisorderedDroppedPackets'
_AS='portDevIwfPmReorderedPackets'
_AR='portDevIwfPmMalformedPackets'
_AQ='portDevIwfPmTxPackets'
_AP='portDevIwfPmRxPackets'
_AO='portDevIwfPmName'
_AN='portDevIwfLocalPacketLost'
_AM='portDevIwfRemotePacketLost'
_AL='portDevIwfNoTdmPayload'
_AK='portDevIwfEquipmentFailure'
_AJ='portDevIwfLossOfFrame'
_AI='portDevIwfLossOfSignal'
_AH='portDevIwfLocalPortIndex'
_AG='portDevIwfInternalReference'
_AF='portDevIwfJitterBufferRecenter'
_AE='portDevIwfRtpClockSource'
_AD='portDevIwfName'
_AC='portDevGenericRestartPortDevice'
_AB='portDevGenericCreateMeg'
_AA='portDevGenericCreateMep'
_A9='portDevGenericAutoDiscoverInterval'
_A8='portDevGenericSlot'
_A7='portDevGenericSubrack'
_A6='portDevGenericName'
_A5='portDevFwIndex'
_A4='PortSelection'
_A3='EnableDisable'
_A2='BoardOrInterfaceOperStatus'
_A1='portDevIwfPmGroupV2'
_A0='portDevIwfGroupV2'
_z='portDevIwfPmGroupV1'
_y='portDevIwfGroupV1'
_x='portDevEquipmentDyingGasp'
_w='portDevEquipmentDestMacAddress'
_v='portDevIwfPmIndex'
_u='portDevIwfIndex'
_t='portDevGenericIndex'
_s='portDevEquipmentActivePort'
_r='portDevEquipmentDeviceVersionType'
_q='portDevGenericCreateNewPortDevice'
_p='DisplayString'
_o='AdminStatus'
_n='portDevGenericGroupV1'
_m='portDevEquipmentFwUpgradeStatus'
_l='portDevEquipmentDestMacAddressCheck'
_k='portDevEquipmentAdminPowerB'
_j='portDevEquipmentAdminPowerA'
_i='portDevEquipmentLocalPortIndex'
_h='portDevEquipmentMacAddress'
_g='portDevEquipmentInternalReference'
_f='portDevEquipmentPowerBMissing'
_e='portDevEquipmentPowerAMissing'
_d='portDevEquipmentConfigurationFault'
_c='portDevEquipmentDeviceNotReachable'
_b='portDevEquipmentDeviceNotManageable'
_a='portDevEquipmentMultiDeviceFound'
_Z='portDevEquipmentNoDeviceFound'
_Y='portDevEquipmentRowStatus'
_X='portDevEquipmentVlanId'
_W='portDevEquipmentSlot'
_V='portDevEquipmentSubrack'
_U='portDevEquipmentSelectedPort'
_T='portDevEquipmentLinkPassThrough'
_S='portDevEquipmentFwVersion'
_R='portDevEquipmentActualType'
_Q='portDevEquipmentExpectedType'
_P='portDevEquipmentOperStatus'
_O='portDevEquipmentAdminStatus'
_N='portDevEquipmentLocation'
_M='portDevEquipmentDescr'
_L='portDevEquipmentName'
_K='portDevFwGroupV1'
_J='portDevGeneralGroupV1'
_I='portDevEquipmentIndex'
_H='Integer32'
_G='read-create'
_F='deprecated'
_E='read-write'
_D='Unsigned32'
_C='read-only'
_B='current'
_A='LUM-PORTDEVICE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumModules,lumPortdeviceMIB=mibBuilder.importSymbols('LUM-REG','lumModules','lumPortdeviceMIB')
AdminStatus,BoardOrInterfaceOperStatus,CommandString,EnableDisable,FaultStatus,MgmtNameString,SlotNumber,SubrackNumber=mibBuilder.importSymbols('LUM-TC',_o,_A2,'CommandString',_A3,'FaultStatus','MgmtNameString','SlotNumber','SubrackNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_p,'MacAddress','PhysAddress','RowStatus','TextualConvention')
lumPortdeviceMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,57))
if mibBuilder.loadTexts:lumPortdeviceMIBModule.setRevisions(('2017-06-15 00:00','2015-07-07 00:00','2014-05-16 00:00','2013-05-31 00:00'))
class PortDeviceEquipmentType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_Ab,0),('nidGe',1),('iSfp155',2),('iSfp622',3),('iSfpVc12',4),('iSfp2488',5)))
class PortDeviceVersionType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3,4,5,8,10,11,12,24,25,31,32,258,259)));namedValues=NamedValues(*((_Ab,0),('tpmrPmR11S',1),('ex12NidR22S',3),('tsop155GeConvPmR12',4),('tsop622GeConvPmR12',5),('tpmrPmR15RespS',8),('tpmrPmR15InitS',10),('ex14NidR10S',11),('tpmrPmR11L',12),('tsop155GeConvPmR15',24),('tsop622GeConvPmR15',25),('ex14NidR20S',31),('ex14NidR40S',32),('tsopStm1eGeConvPmR15',258),('tpmrPmR20TranspS',259)))
class PortDevFwImgState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unknown',0),('inactive',1),('active',2),('empty',3)))
class PortSelection(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('cifa',0),('cifb',1),('auto',2)))
_LumPortdeviceConfs_ObjectIdentity=ObjectIdentity
lumPortdeviceConfs=_LumPortdeviceConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,57,1))
_LumPortdeviceGroups_ObjectIdentity=ObjectIdentity
lumPortdeviceGroups=_LumPortdeviceGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,57,1,1))
_LumPortdeviceCompl_ObjectIdentity=ObjectIdentity
lumPortdeviceCompl=_LumPortdeviceCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,57,1,2))
_LumPortdeviceMIBObjects_ObjectIdentity=ObjectIdentity
lumPortdeviceMIBObjects=_LumPortdeviceMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,57,2))
_PortDevGeneral_ObjectIdentity=ObjectIdentity
portDevGeneral=_PortDevGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,57,2,1))
_PortDevGeneralLastChangeTime_Type=DateAndTime
_PortDevGeneralLastChangeTime_Object=MibScalar
portDevGeneralLastChangeTime=_PortDevGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,57,2,1,1),_PortDevGeneralLastChangeTime_Type())
portDevGeneralLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevGeneralLastChangeTime.setStatus(_B)
_PortDevGeneralStateLastChangeTime_Type=DateAndTime
_PortDevGeneralStateLastChangeTime_Object=MibScalar
portDevGeneralStateLastChangeTime=_PortDevGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,57,2,1,2),_PortDevGeneralStateLastChangeTime_Type())
portDevGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevGeneralStateLastChangeTime.setStatus(_B)
_PortDevGeneralGenericTableSize_Type=Unsigned32
_PortDevGeneralGenericTableSize_Object=MibScalar
portDevGeneralGenericTableSize=_PortDevGeneralGenericTableSize_Object((1,3,6,1,4,1,8708,2,57,2,1,3),_PortDevGeneralGenericTableSize_Type())
portDevGeneralGenericTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevGeneralGenericTableSize.setStatus(_B)
_PortDevGeneralEquipmentTableSize_Type=Unsigned32
_PortDevGeneralEquipmentTableSize_Object=MibScalar
portDevGeneralEquipmentTableSize=_PortDevGeneralEquipmentTableSize_Object((1,3,6,1,4,1,8708,2,57,2,1,4),_PortDevGeneralEquipmentTableSize_Type())
portDevGeneralEquipmentTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevGeneralEquipmentTableSize.setStatus(_B)
_PortDevGeneralFwTableSize_Type=Unsigned32
_PortDevGeneralFwTableSize_Object=MibScalar
portDevGeneralFwTableSize=_PortDevGeneralFwTableSize_Object((1,3,6,1,4,1,8708,2,57,2,1,5),_PortDevGeneralFwTableSize_Type())
portDevGeneralFwTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevGeneralFwTableSize.setStatus(_B)
_PortDevGeneralIwfTableSize_Type=Unsigned32
_PortDevGeneralIwfTableSize_Object=MibScalar
portDevGeneralIwfTableSize=_PortDevGeneralIwfTableSize_Object((1,3,6,1,4,1,8708,2,57,2,1,6),_PortDevGeneralIwfTableSize_Type())
portDevGeneralIwfTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevGeneralIwfTableSize.setStatus(_B)
_PortDevGeneralIwfPmTableSize_Type=Unsigned32
_PortDevGeneralIwfPmTableSize_Object=MibScalar
portDevGeneralIwfPmTableSize=_PortDevGeneralIwfPmTableSize_Object((1,3,6,1,4,1,8708,2,57,2,1,7),_PortDevGeneralIwfPmTableSize_Type())
portDevGeneralIwfPmTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevGeneralIwfPmTableSize.setStatus(_B)
_PortDevGenericList_ObjectIdentity=ObjectIdentity
portDevGenericList=_PortDevGenericList_ObjectIdentity((1,3,6,1,4,1,8708,2,57,2,2))
_PortDevGenericTable_Object=MibTable
portDevGenericTable=_PortDevGenericTable_Object((1,3,6,1,4,1,8708,2,57,2,2,1))
if mibBuilder.loadTexts:portDevGenericTable.setStatus(_B)
_PortDevGenericEntry_Object=MibTableRow
portDevGenericEntry=_PortDevGenericEntry_Object((1,3,6,1,4,1,8708,2,57,2,2,1,1))
portDevGenericEntry.setIndexNames((0,_A,_t))
if mibBuilder.loadTexts:portDevGenericEntry.setStatus(_B)
class _PortDevGenericIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortDevGenericIndex_Type.__name__=_D
_PortDevGenericIndex_Object=MibTableColumn
portDevGenericIndex=_PortDevGenericIndex_Object((1,3,6,1,4,1,8708,2,57,2,2,1,1,1),_PortDevGenericIndex_Type())
portDevGenericIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevGenericIndex.setStatus(_B)
_PortDevGenericName_Type=MgmtNameString
_PortDevGenericName_Object=MibTableColumn
portDevGenericName=_PortDevGenericName_Object((1,3,6,1,4,1,8708,2,57,2,2,1,1,2),_PortDevGenericName_Type())
portDevGenericName.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevGenericName.setStatus(_B)
class _PortDevGenericSubrack_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortDevGenericSubrack_Type.__name__=_D
_PortDevGenericSubrack_Object=MibTableColumn
portDevGenericSubrack=_PortDevGenericSubrack_Object((1,3,6,1,4,1,8708,2,57,2,2,1,1,3),_PortDevGenericSubrack_Type())
portDevGenericSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevGenericSubrack.setStatus(_B)
class _PortDevGenericSlot_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortDevGenericSlot_Type.__name__=_D
_PortDevGenericSlot_Object=MibTableColumn
portDevGenericSlot=_PortDevGenericSlot_Object((1,3,6,1,4,1,8708,2,57,2,2,1,1,4),_PortDevGenericSlot_Type())
portDevGenericSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevGenericSlot.setStatus(_B)
class _PortDevGenericAutoDiscoverInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_PortDevGenericAutoDiscoverInterval_Type.__name__=_D
_PortDevGenericAutoDiscoverInterval_Object=MibTableColumn
portDevGenericAutoDiscoverInterval=_PortDevGenericAutoDiscoverInterval_Object((1,3,6,1,4,1,8708,2,57,2,2,1,1,5),_PortDevGenericAutoDiscoverInterval_Type())
portDevGenericAutoDiscoverInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:portDevGenericAutoDiscoverInterval.setStatus(_B)
_PortDevGenericCreateNewPortDevice_Type=CommandString
_PortDevGenericCreateNewPortDevice_Object=MibTableColumn
portDevGenericCreateNewPortDevice=_PortDevGenericCreateNewPortDevice_Object((1,3,6,1,4,1,8708,2,57,2,2,1,1,6),_PortDevGenericCreateNewPortDevice_Type())
portDevGenericCreateNewPortDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevGenericCreateNewPortDevice.setStatus(_B)
_PortDevGenericRestartPortDevice_Type=CommandString
_PortDevGenericRestartPortDevice_Object=MibTableColumn
portDevGenericRestartPortDevice=_PortDevGenericRestartPortDevice_Object((1,3,6,1,4,1,8708,2,57,2,2,1,1,7),_PortDevGenericRestartPortDevice_Type())
portDevGenericRestartPortDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevGenericRestartPortDevice.setStatus(_B)
_PortDevGenericCreateMep_Type=CommandString
_PortDevGenericCreateMep_Object=MibTableColumn
portDevGenericCreateMep=_PortDevGenericCreateMep_Object((1,3,6,1,4,1,8708,2,57,2,2,1,1,8),_PortDevGenericCreateMep_Type())
portDevGenericCreateMep.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevGenericCreateMep.setStatus(_B)
_PortDevGenericCreateMeg_Type=CommandString
_PortDevGenericCreateMeg_Object=MibTableColumn
portDevGenericCreateMeg=_PortDevGenericCreateMeg_Object((1,3,6,1,4,1,8708,2,57,2,2,1,1,9),_PortDevGenericCreateMeg_Type())
portDevGenericCreateMeg.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevGenericCreateMeg.setStatus(_B)
_PortDevGenericCreateNewPortDeviceAdvanced_Type=CommandString
_PortDevGenericCreateNewPortDeviceAdvanced_Object=MibTableColumn
portDevGenericCreateNewPortDeviceAdvanced=_PortDevGenericCreateNewPortDeviceAdvanced_Object((1,3,6,1,4,1,8708,2,57,2,2,1,1,10),_PortDevGenericCreateNewPortDeviceAdvanced_Type())
portDevGenericCreateNewPortDeviceAdvanced.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevGenericCreateNewPortDeviceAdvanced.setStatus(_B)
_PortDevEquipmentList_ObjectIdentity=ObjectIdentity
portDevEquipmentList=_PortDevEquipmentList_ObjectIdentity((1,3,6,1,4,1,8708,2,57,2,3))
_PortDevEquipmentTable_Object=MibTable
portDevEquipmentTable=_PortDevEquipmentTable_Object((1,3,6,1,4,1,8708,2,57,2,3,1))
if mibBuilder.loadTexts:portDevEquipmentTable.setStatus(_B)
_PortDevEquipmentEntry_Object=MibTableRow
portDevEquipmentEntry=_PortDevEquipmentEntry_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1))
portDevEquipmentEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:portDevEquipmentEntry.setStatus(_B)
class _PortDevEquipmentIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortDevEquipmentIndex_Type.__name__=_D
_PortDevEquipmentIndex_Object=MibTableColumn
portDevEquipmentIndex=_PortDevEquipmentIndex_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,1),_PortDevEquipmentIndex_Type())
portDevEquipmentIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevEquipmentIndex.setStatus(_B)
_PortDevEquipmentName_Type=MgmtNameString
_PortDevEquipmentName_Object=MibTableColumn
portDevEquipmentName=_PortDevEquipmentName_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,2),_PortDevEquipmentName_Type())
portDevEquipmentName.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevEquipmentName.setStatus(_B)
class _PortDevEquipmentDescr_Type(DisplayString):defaultValue=OctetString('')
_PortDevEquipmentDescr_Type.__name__=_p
_PortDevEquipmentDescr_Object=MibTableColumn
portDevEquipmentDescr=_PortDevEquipmentDescr_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,3),_PortDevEquipmentDescr_Type())
portDevEquipmentDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:portDevEquipmentDescr.setStatus(_B)
class _PortDevEquipmentLocation_Type(DisplayString):defaultValue=OctetString('')
_PortDevEquipmentLocation_Type.__name__=_p
_PortDevEquipmentLocation_Object=MibTableColumn
portDevEquipmentLocation=_PortDevEquipmentLocation_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,4),_PortDevEquipmentLocation_Type())
portDevEquipmentLocation.setMaxAccess(_E)
if mibBuilder.loadTexts:portDevEquipmentLocation.setStatus(_B)
class _PortDevEquipmentAdminStatus_Type(AdminStatus):defaultValue=2
_PortDevEquipmentAdminStatus_Type.__name__=_o
_PortDevEquipmentAdminStatus_Object=MibTableColumn
portDevEquipmentAdminStatus=_PortDevEquipmentAdminStatus_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,5),_PortDevEquipmentAdminStatus_Type())
portDevEquipmentAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:portDevEquipmentAdminStatus.setStatus(_B)
class _PortDevEquipmentOperStatus_Type(BoardOrInterfaceOperStatus):defaultValue=3
_PortDevEquipmentOperStatus_Type.__name__=_A2
_PortDevEquipmentOperStatus_Object=MibTableColumn
portDevEquipmentOperStatus=_PortDevEquipmentOperStatus_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,6),_PortDevEquipmentOperStatus_Type())
portDevEquipmentOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevEquipmentOperStatus.setStatus(_B)
class _PortDevEquipmentExpectedType_Type(PortDeviceEquipmentType):defaultValue=0
_PortDevEquipmentExpectedType_Type.__name__=_Ac
_PortDevEquipmentExpectedType_Object=MibTableColumn
portDevEquipmentExpectedType=_PortDevEquipmentExpectedType_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,7),_PortDevEquipmentExpectedType_Type())
portDevEquipmentExpectedType.setMaxAccess(_G)
if mibBuilder.loadTexts:portDevEquipmentExpectedType.setStatus(_B)
_PortDevEquipmentActualType_Type=PortDeviceEquipmentType
_PortDevEquipmentActualType_Object=MibTableColumn
portDevEquipmentActualType=_PortDevEquipmentActualType_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,8),_PortDevEquipmentActualType_Type())
portDevEquipmentActualType.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevEquipmentActualType.setStatus(_B)
_PortDevEquipmentFwVersion_Type=DisplayString
_PortDevEquipmentFwVersion_Object=MibTableColumn
portDevEquipmentFwVersion=_PortDevEquipmentFwVersion_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,9),_PortDevEquipmentFwVersion_Type())
portDevEquipmentFwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevEquipmentFwVersion.setStatus(_B)
_PortDevEquipmentFwUpgradeStatus_Type=DisplayString
_PortDevEquipmentFwUpgradeStatus_Object=MibTableColumn
portDevEquipmentFwUpgradeStatus=_PortDevEquipmentFwUpgradeStatus_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,10),_PortDevEquipmentFwUpgradeStatus_Type())
portDevEquipmentFwUpgradeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevEquipmentFwUpgradeStatus.setStatus(_B)
class _PortDevEquipmentLinkPassThrough_Type(EnableDisable):defaultValue=1
_PortDevEquipmentLinkPassThrough_Type.__name__=_A3
_PortDevEquipmentLinkPassThrough_Object=MibTableColumn
portDevEquipmentLinkPassThrough=_PortDevEquipmentLinkPassThrough_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,11),_PortDevEquipmentLinkPassThrough_Type())
portDevEquipmentLinkPassThrough.setMaxAccess(_E)
if mibBuilder.loadTexts:portDevEquipmentLinkPassThrough.setStatus(_B)
_PortDevEquipmentSubrack_Type=SubrackNumber
_PortDevEquipmentSubrack_Object=MibTableColumn
portDevEquipmentSubrack=_PortDevEquipmentSubrack_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,12),_PortDevEquipmentSubrack_Type())
portDevEquipmentSubrack.setMaxAccess(_G)
if mibBuilder.loadTexts:portDevEquipmentSubrack.setStatus(_B)
_PortDevEquipmentSlot_Type=SlotNumber
_PortDevEquipmentSlot_Object=MibTableColumn
portDevEquipmentSlot=_PortDevEquipmentSlot_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,13),_PortDevEquipmentSlot_Type())
portDevEquipmentSlot.setMaxAccess(_G)
if mibBuilder.loadTexts:portDevEquipmentSlot.setStatus(_B)
class _PortDevEquipmentVlanId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_PortDevEquipmentVlanId_Type.__name__=_D
_PortDevEquipmentVlanId_Object=MibTableColumn
portDevEquipmentVlanId=_PortDevEquipmentVlanId_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,14),_PortDevEquipmentVlanId_Type())
portDevEquipmentVlanId.setMaxAccess(_G)
if mibBuilder.loadTexts:portDevEquipmentVlanId.setStatus(_B)
_PortDevEquipmentRowStatus_Type=RowStatus
_PortDevEquipmentRowStatus_Object=MibTableColumn
portDevEquipmentRowStatus=_PortDevEquipmentRowStatus_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,15),_PortDevEquipmentRowStatus_Type())
portDevEquipmentRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:portDevEquipmentRowStatus.setStatus(_B)
_PortDevEquipmentNoDeviceFound_Type=FaultStatus
_PortDevEquipmentNoDeviceFound_Object=MibTableColumn
portDevEquipmentNoDeviceFound=_PortDevEquipmentNoDeviceFound_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,16),_PortDevEquipmentNoDeviceFound_Type())
portDevEquipmentNoDeviceFound.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevEquipmentNoDeviceFound.setStatus(_B)
_PortDevEquipmentMultiDeviceFound_Type=FaultStatus
_PortDevEquipmentMultiDeviceFound_Object=MibTableColumn
portDevEquipmentMultiDeviceFound=_PortDevEquipmentMultiDeviceFound_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,17),_PortDevEquipmentMultiDeviceFound_Type())
portDevEquipmentMultiDeviceFound.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevEquipmentMultiDeviceFound.setStatus(_B)
_PortDevEquipmentDeviceNotManageable_Type=FaultStatus
_PortDevEquipmentDeviceNotManageable_Object=MibTableColumn
portDevEquipmentDeviceNotManageable=_PortDevEquipmentDeviceNotManageable_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,18),_PortDevEquipmentDeviceNotManageable_Type())
portDevEquipmentDeviceNotManageable.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevEquipmentDeviceNotManageable.setStatus(_B)
_PortDevEquipmentDeviceNotReachable_Type=FaultStatus
_PortDevEquipmentDeviceNotReachable_Object=MibTableColumn
portDevEquipmentDeviceNotReachable=_PortDevEquipmentDeviceNotReachable_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,19),_PortDevEquipmentDeviceNotReachable_Type())
portDevEquipmentDeviceNotReachable.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevEquipmentDeviceNotReachable.setStatus(_B)
_PortDevEquipmentConfigurationFault_Type=FaultStatus
_PortDevEquipmentConfigurationFault_Object=MibTableColumn
portDevEquipmentConfigurationFault=_PortDevEquipmentConfigurationFault_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,20),_PortDevEquipmentConfigurationFault_Type())
portDevEquipmentConfigurationFault.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevEquipmentConfigurationFault.setStatus(_B)
_PortDevEquipmentPowerAMissing_Type=FaultStatus
_PortDevEquipmentPowerAMissing_Object=MibTableColumn
portDevEquipmentPowerAMissing=_PortDevEquipmentPowerAMissing_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,21),_PortDevEquipmentPowerAMissing_Type())
portDevEquipmentPowerAMissing.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevEquipmentPowerAMissing.setStatus(_B)
_PortDevEquipmentPowerBMissing_Type=FaultStatus
_PortDevEquipmentPowerBMissing_Object=MibTableColumn
portDevEquipmentPowerBMissing=_PortDevEquipmentPowerBMissing_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,22),_PortDevEquipmentPowerBMissing_Type())
portDevEquipmentPowerBMissing.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevEquipmentPowerBMissing.setStatus(_B)
class _PortDevEquipmentInternalReference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PortDevEquipmentInternalReference_Type.__name__=_D
_PortDevEquipmentInternalReference_Object=MibTableColumn
portDevEquipmentInternalReference=_PortDevEquipmentInternalReference_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,23),_PortDevEquipmentInternalReference_Type())
portDevEquipmentInternalReference.setMaxAccess(_G)
if mibBuilder.loadTexts:portDevEquipmentInternalReference.setStatus(_B)
_PortDevEquipmentMacAddress_Type=DisplayString
_PortDevEquipmentMacAddress_Object=MibTableColumn
portDevEquipmentMacAddress=_PortDevEquipmentMacAddress_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,24),_PortDevEquipmentMacAddress_Type())
portDevEquipmentMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevEquipmentMacAddress.setStatus(_B)
class _PortDevEquipmentLocalPortIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortDevEquipmentLocalPortIndex_Type.__name__=_D
_PortDevEquipmentLocalPortIndex_Object=MibTableColumn
portDevEquipmentLocalPortIndex=_PortDevEquipmentLocalPortIndex_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,25),_PortDevEquipmentLocalPortIndex_Type())
portDevEquipmentLocalPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:portDevEquipmentLocalPortIndex.setStatus(_B)
class _PortDevEquipmentAdminPowerA_Type(AdminStatus):defaultValue=1
_PortDevEquipmentAdminPowerA_Type.__name__=_o
_PortDevEquipmentAdminPowerA_Object=MibTableColumn
portDevEquipmentAdminPowerA=_PortDevEquipmentAdminPowerA_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,26),_PortDevEquipmentAdminPowerA_Type())
portDevEquipmentAdminPowerA.setMaxAccess(_E)
if mibBuilder.loadTexts:portDevEquipmentAdminPowerA.setStatus(_B)
class _PortDevEquipmentAdminPowerB_Type(AdminStatus):defaultValue=1
_PortDevEquipmentAdminPowerB_Type.__name__=_o
_PortDevEquipmentAdminPowerB_Object=MibTableColumn
portDevEquipmentAdminPowerB=_PortDevEquipmentAdminPowerB_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,27),_PortDevEquipmentAdminPowerB_Type())
portDevEquipmentAdminPowerB.setMaxAccess(_E)
if mibBuilder.loadTexts:portDevEquipmentAdminPowerB.setStatus(_B)
class _PortDevEquipmentSelectedPort_Type(PortSelection):defaultValue=2
_PortDevEquipmentSelectedPort_Type.__name__=_A4
_PortDevEquipmentSelectedPort_Object=MibTableColumn
portDevEquipmentSelectedPort=_PortDevEquipmentSelectedPort_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,28),_PortDevEquipmentSelectedPort_Type())
portDevEquipmentSelectedPort.setMaxAccess(_E)
if mibBuilder.loadTexts:portDevEquipmentSelectedPort.setStatus(_B)
_PortDevEquipmentDestMacAddress_Type=MacAddress
_PortDevEquipmentDestMacAddress_Object=MibTableColumn
portDevEquipmentDestMacAddress=_PortDevEquipmentDestMacAddress_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,29),_PortDevEquipmentDestMacAddress_Type())
portDevEquipmentDestMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:portDevEquipmentDestMacAddress.setStatus(_F)
class _PortDevEquipmentDestMacAddressCheck_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_PortDevEquipmentDestMacAddressCheck_Type.__name__=_H
_PortDevEquipmentDestMacAddressCheck_Object=MibTableColumn
portDevEquipmentDestMacAddressCheck=_PortDevEquipmentDestMacAddressCheck_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,30),_PortDevEquipmentDestMacAddressCheck_Type())
portDevEquipmentDestMacAddressCheck.setMaxAccess(_E)
if mibBuilder.loadTexts:portDevEquipmentDestMacAddressCheck.setStatus(_B)
_PortDevEquipmentDeviceVersionType_Type=PortDeviceVersionType
_PortDevEquipmentDeviceVersionType_Object=MibTableColumn
portDevEquipmentDeviceVersionType=_PortDevEquipmentDeviceVersionType_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,31),_PortDevEquipmentDeviceVersionType_Type())
portDevEquipmentDeviceVersionType.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevEquipmentDeviceVersionType.setStatus(_B)
class _PortDevEquipmentActivePort_Type(PortSelection):defaultValue=2
_PortDevEquipmentActivePort_Type.__name__=_A4
_PortDevEquipmentActivePort_Object=MibTableColumn
portDevEquipmentActivePort=_PortDevEquipmentActivePort_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,32),_PortDevEquipmentActivePort_Type())
portDevEquipmentActivePort.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevEquipmentActivePort.setStatus(_B)
_PortDevEquipmentDyingGasp_Type=FaultStatus
_PortDevEquipmentDyingGasp_Object=MibTableColumn
portDevEquipmentDyingGasp=_PortDevEquipmentDyingGasp_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,33),_PortDevEquipmentDyingGasp_Type())
portDevEquipmentDyingGasp.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevEquipmentDyingGasp.setStatus(_B)
class _PortDevEquipmentLosCsf_Type(EnableDisable):defaultValue=1
_PortDevEquipmentLosCsf_Type.__name__=_A3
_PortDevEquipmentLosCsf_Object=MibTableColumn
portDevEquipmentLosCsf=_PortDevEquipmentLosCsf_Object((1,3,6,1,4,1,8708,2,57,2,3,1,1,34),_PortDevEquipmentLosCsf_Type())
portDevEquipmentLosCsf.setMaxAccess(_E)
if mibBuilder.loadTexts:portDevEquipmentLosCsf.setStatus(_B)
_PortDevFwList_ObjectIdentity=ObjectIdentity
portDevFwList=_PortDevFwList_ObjectIdentity((1,3,6,1,4,1,8708,2,57,2,4))
_PortDevFwTable_Object=MibTable
portDevFwTable=_PortDevFwTable_Object((1,3,6,1,4,1,8708,2,57,2,4,1))
if mibBuilder.loadTexts:portDevFwTable.setStatus(_B)
_PortDevFwEntry_Object=MibTableRow
portDevFwEntry=_PortDevFwEntry_Object((1,3,6,1,4,1,8708,2,57,2,4,1,1))
portDevFwEntry.setIndexNames((0,_A,_A5))
if mibBuilder.loadTexts:portDevFwEntry.setStatus(_B)
class _PortDevFwIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortDevFwIndex_Type.__name__=_D
_PortDevFwIndex_Object=MibTableColumn
portDevFwIndex=_PortDevFwIndex_Object((1,3,6,1,4,1,8708,2,57,2,4,1,1,1),_PortDevFwIndex_Type())
portDevFwIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevFwIndex.setStatus(_B)
class _PortDevFwSubrack_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortDevFwSubrack_Type.__name__=_D
_PortDevFwSubrack_Object=MibTableColumn
portDevFwSubrack=_PortDevFwSubrack_Object((1,3,6,1,4,1,8708,2,57,2,4,1,1,2),_PortDevFwSubrack_Type())
portDevFwSubrack.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevFwSubrack.setStatus(_B)
class _PortDevFwSlot_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortDevFwSlot_Type.__name__=_D
_PortDevFwSlot_Object=MibTableColumn
portDevFwSlot=_PortDevFwSlot_Object((1,3,6,1,4,1,8708,2,57,2,4,1,1,3),_PortDevFwSlot_Type())
portDevFwSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevFwSlot.setStatus(_B)
_PortDevFwName_Type=DisplayString
_PortDevFwName_Object=MibTableColumn
portDevFwName=_PortDevFwName_Object((1,3,6,1,4,1,8708,2,57,2,4,1,1,4),_PortDevFwName_Type())
portDevFwName.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevFwName.setStatus(_B)
class _PortDevFwPortDevId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortDevFwPortDevId_Type.__name__=_D
_PortDevFwPortDevId_Object=MibTableColumn
portDevFwPortDevId=_PortDevFwPortDevId_Object((1,3,6,1,4,1,8708,2,57,2,4,1,1,5),_PortDevFwPortDevId_Type())
portDevFwPortDevId.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevFwPortDevId.setStatus(_B)
class _PortDevFwImgSlotOneNr_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortDevFwImgSlotOneNr_Type.__name__=_D
_PortDevFwImgSlotOneNr_Object=MibTableColumn
portDevFwImgSlotOneNr=_PortDevFwImgSlotOneNr_Object((1,3,6,1,4,1,8708,2,57,2,4,1,1,6),_PortDevFwImgSlotOneNr_Type())
portDevFwImgSlotOneNr.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevFwImgSlotOneNr.setStatus(_B)
_PortDevFwImgSlotOneVersion_Type=DisplayString
_PortDevFwImgSlotOneVersion_Object=MibTableColumn
portDevFwImgSlotOneVersion=_PortDevFwImgSlotOneVersion_Object((1,3,6,1,4,1,8708,2,57,2,4,1,1,7),_PortDevFwImgSlotOneVersion_Type())
portDevFwImgSlotOneVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevFwImgSlotOneVersion.setStatus(_B)
_PortDevFwImgSlotOneState_Type=PortDevFwImgState
_PortDevFwImgSlotOneState_Object=MibTableColumn
portDevFwImgSlotOneState=_PortDevFwImgSlotOneState_Object((1,3,6,1,4,1,8708,2,57,2,4,1,1,8),_PortDevFwImgSlotOneState_Type())
portDevFwImgSlotOneState.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevFwImgSlotOneState.setStatus(_B)
_PortDevFwImgSlotOneDate_Type=DisplayString
_PortDevFwImgSlotOneDate_Object=MibTableColumn
portDevFwImgSlotOneDate=_PortDevFwImgSlotOneDate_Object((1,3,6,1,4,1,8708,2,57,2,4,1,1,9),_PortDevFwImgSlotOneDate_Type())
portDevFwImgSlotOneDate.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevFwImgSlotOneDate.setStatus(_B)
class _PortDevFwImgSlotTwoNr_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortDevFwImgSlotTwoNr_Type.__name__=_D
_PortDevFwImgSlotTwoNr_Object=MibTableColumn
portDevFwImgSlotTwoNr=_PortDevFwImgSlotTwoNr_Object((1,3,6,1,4,1,8708,2,57,2,4,1,1,10),_PortDevFwImgSlotTwoNr_Type())
portDevFwImgSlotTwoNr.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevFwImgSlotTwoNr.setStatus(_B)
_PortDevFwImgSlotTwoVersion_Type=DisplayString
_PortDevFwImgSlotTwoVersion_Object=MibTableColumn
portDevFwImgSlotTwoVersion=_PortDevFwImgSlotTwoVersion_Object((1,3,6,1,4,1,8708,2,57,2,4,1,1,11),_PortDevFwImgSlotTwoVersion_Type())
portDevFwImgSlotTwoVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevFwImgSlotTwoVersion.setStatus(_B)
_PortDevFwImgSlotTwoState_Type=PortDevFwImgState
_PortDevFwImgSlotTwoState_Object=MibTableColumn
portDevFwImgSlotTwoState=_PortDevFwImgSlotTwoState_Object((1,3,6,1,4,1,8708,2,57,2,4,1,1,12),_PortDevFwImgSlotTwoState_Type())
portDevFwImgSlotTwoState.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevFwImgSlotTwoState.setStatus(_B)
_PortDevFwImgSlotTwoDate_Type=DisplayString
_PortDevFwImgSlotTwoDate_Object=MibTableColumn
portDevFwImgSlotTwoDate=_PortDevFwImgSlotTwoDate_Object((1,3,6,1,4,1,8708,2,57,2,4,1,1,13),_PortDevFwImgSlotTwoDate_Type())
portDevFwImgSlotTwoDate.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevFwImgSlotTwoDate.setStatus(_B)
_PortDevFwInstallFw_Type=CommandString
_PortDevFwInstallFw_Object=MibTableColumn
portDevFwInstallFw=_PortDevFwInstallFw_Object((1,3,6,1,4,1,8708,2,57,2,4,1,1,14),_PortDevFwInstallFw_Type())
portDevFwInstallFw.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevFwInstallFw.setStatus(_B)
_PortDevFwActivateFw_Type=CommandString
_PortDevFwActivateFw_Object=MibTableColumn
portDevFwActivateFw=_PortDevFwActivateFw_Object((1,3,6,1,4,1,8708,2,57,2,4,1,1,15),_PortDevFwActivateFw_Type())
portDevFwActivateFw.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevFwActivateFw.setStatus(_B)
_PortDevFwGetAllFiles_Type=CommandString
_PortDevFwGetAllFiles_Object=MibTableColumn
portDevFwGetAllFiles=_PortDevFwGetAllFiles_Object((1,3,6,1,4,1,8708,2,57,2,4,1,1,16),_PortDevFwGetAllFiles_Type())
portDevFwGetAllFiles.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevFwGetAllFiles.setStatus(_B)
_PortDevFwUpgradeStatus_Type=DisplayString
_PortDevFwUpgradeStatus_Object=MibTableColumn
portDevFwUpgradeStatus=_PortDevFwUpgradeStatus_Object((1,3,6,1,4,1,8708,2,57,2,4,1,1,17),_PortDevFwUpgradeStatus_Type())
portDevFwUpgradeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevFwUpgradeStatus.setStatus(_B)
_PortDevIwfList_ObjectIdentity=ObjectIdentity
portDevIwfList=_PortDevIwfList_ObjectIdentity((1,3,6,1,4,1,8708,2,57,2,5))
_PortDevIwfTable_Object=MibTable
portDevIwfTable=_PortDevIwfTable_Object((1,3,6,1,4,1,8708,2,57,2,5,1))
if mibBuilder.loadTexts:portDevIwfTable.setStatus(_B)
_PortDevIwfEntry_Object=MibTableRow
portDevIwfEntry=_PortDevIwfEntry_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1))
portDevIwfEntry.setIndexNames((0,_A,_u))
if mibBuilder.loadTexts:portDevIwfEntry.setStatus(_B)
class _PortDevIwfIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortDevIwfIndex_Type.__name__=_D
_PortDevIwfIndex_Object=MibTableColumn
portDevIwfIndex=_PortDevIwfIndex_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,1),_PortDevIwfIndex_Type())
portDevIwfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfIndex.setStatus(_B)
_PortDevIwfName_Type=MgmtNameString
_PortDevIwfName_Object=MibTableColumn
portDevIwfName=_PortDevIwfName_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,2),_PortDevIwfName_Type())
portDevIwfName.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfName.setStatus(_B)
class _PortDevIwfRtpClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ethernet',1),('tdm',2)))
_PortDevIwfRtpClockSource_Type.__name__=_H
_PortDevIwfRtpClockSource_Object=MibTableColumn
portDevIwfRtpClockSource=_PortDevIwfRtpClockSource_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,3),_PortDevIwfRtpClockSource_Type())
portDevIwfRtpClockSource.setMaxAccess(_E)
if mibBuilder.loadTexts:portDevIwfRtpClockSource.setStatus(_B)
class _PortDevIwfJitterBufferRecenter_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('recenter',2)))
_PortDevIwfJitterBufferRecenter_Type.__name__=_H
_PortDevIwfJitterBufferRecenter_Object=MibTableColumn
portDevIwfJitterBufferRecenter=_PortDevIwfJitterBufferRecenter_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,4),_PortDevIwfJitterBufferRecenter_Type())
portDevIwfJitterBufferRecenter.setMaxAccess(_E)
if mibBuilder.loadTexts:portDevIwfJitterBufferRecenter.setStatus(_B)
class _PortDevIwfInternalReference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PortDevIwfInternalReference_Type.__name__=_D
_PortDevIwfInternalReference_Object=MibTableColumn
portDevIwfInternalReference=_PortDevIwfInternalReference_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,5),_PortDevIwfInternalReference_Type())
portDevIwfInternalReference.setMaxAccess(_G)
if mibBuilder.loadTexts:portDevIwfInternalReference.setStatus(_B)
class _PortDevIwfLocalPortIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortDevIwfLocalPortIndex_Type.__name__=_D
_PortDevIwfLocalPortIndex_Object=MibTableColumn
portDevIwfLocalPortIndex=_PortDevIwfLocalPortIndex_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,6),_PortDevIwfLocalPortIndex_Type())
portDevIwfLocalPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:portDevIwfLocalPortIndex.setStatus(_B)
_PortDevIwfLossOfSignal_Type=FaultStatus
_PortDevIwfLossOfSignal_Object=MibTableColumn
portDevIwfLossOfSignal=_PortDevIwfLossOfSignal_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,7),_PortDevIwfLossOfSignal_Type())
portDevIwfLossOfSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfLossOfSignal.setStatus(_B)
_PortDevIwfLossOfFrame_Type=FaultStatus
_PortDevIwfLossOfFrame_Object=MibTableColumn
portDevIwfLossOfFrame=_PortDevIwfLossOfFrame_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,8),_PortDevIwfLossOfFrame_Type())
portDevIwfLossOfFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfLossOfFrame.setStatus(_B)
_PortDevIwfEquipmentFailure_Type=FaultStatus
_PortDevIwfEquipmentFailure_Object=MibTableColumn
portDevIwfEquipmentFailure=_PortDevIwfEquipmentFailure_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,9),_PortDevIwfEquipmentFailure_Type())
portDevIwfEquipmentFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfEquipmentFailure.setStatus(_B)
_PortDevIwfNoTdmPayload_Type=FaultStatus
_PortDevIwfNoTdmPayload_Object=MibTableColumn
portDevIwfNoTdmPayload=_PortDevIwfNoTdmPayload_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,10),_PortDevIwfNoTdmPayload_Type())
portDevIwfNoTdmPayload.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfNoTdmPayload.setStatus(_B)
_PortDevIwfRemotePacketLost_Type=FaultStatus
_PortDevIwfRemotePacketLost_Object=MibTableColumn
portDevIwfRemotePacketLost=_PortDevIwfRemotePacketLost_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,11),_PortDevIwfRemotePacketLost_Type())
portDevIwfRemotePacketLost.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfRemotePacketLost.setStatus(_B)
_PortDevIwfLocalPacketLost_Type=FaultStatus
_PortDevIwfLocalPacketLost_Object=MibTableColumn
portDevIwfLocalPacketLost=_PortDevIwfLocalPacketLost_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,12),_PortDevIwfLocalPacketLost_Type())
portDevIwfLocalPacketLost.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfLocalPacketLost.setStatus(_B)
class _PortDevIwfAdminStatus_Type(AdminStatus):defaultValue=2
_PortDevIwfAdminStatus_Type.__name__=_o
_PortDevIwfAdminStatus_Object=MibTableColumn
portDevIwfAdminStatus=_PortDevIwfAdminStatus_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,13),_PortDevIwfAdminStatus_Type())
portDevIwfAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:portDevIwfAdminStatus.setStatus(_B)
class _PortDevIwfOperStatus_Type(BoardOrInterfaceOperStatus):defaultValue=3
_PortDevIwfOperStatus_Type.__name__=_A2
_PortDevIwfOperStatus_Object=MibTableColumn
portDevIwfOperStatus=_PortDevIwfOperStatus_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,14),_PortDevIwfOperStatus_Type())
portDevIwfOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfOperStatus.setStatus(_B)
class _PortDevIwfDescr_Type(DisplayString):defaultValue=OctetString('')
_PortDevIwfDescr_Type.__name__=_p
_PortDevIwfDescr_Object=MibTableColumn
portDevIwfDescr=_PortDevIwfDescr_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,15),_PortDevIwfDescr_Type())
portDevIwfDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:portDevIwfDescr.setStatus(_B)
class _PortDevIwfSignalFormat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,39)));namedValues=NamedValues(*(('other',1),('stm1',2),('stm4',3),('stm16',4),('e1',39)))
_PortDevIwfSignalFormat_Type.__name__=_H
_PortDevIwfSignalFormat_Object=MibTableColumn
portDevIwfSignalFormat=_PortDevIwfSignalFormat_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,16),_PortDevIwfSignalFormat_Type())
portDevIwfSignalFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfSignalFormat.setStatus(_B)
class _PortDevIwfEtherType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('qTag0x8100',1),('sTag0x88a8',2)))
_PortDevIwfEtherType_Type.__name__=_H
_PortDevIwfEtherType_Object=MibTableColumn
portDevIwfEtherType=_PortDevIwfEtherType_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,17),_PortDevIwfEtherType_Type())
portDevIwfEtherType.setMaxAccess(_E)
if mibBuilder.loadTexts:portDevIwfEtherType.setStatus(_B)
class _PortDevIwfVlanId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_PortDevIwfVlanId_Type.__name__=_D
_PortDevIwfVlanId_Object=MibTableColumn
portDevIwfVlanId=_PortDevIwfVlanId_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,18),_PortDevIwfVlanId_Type())
portDevIwfVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:portDevIwfVlanId.setStatus(_B)
class _PortDevIwfVlanPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PortDevIwfVlanPriority_Type.__name__=_D
_PortDevIwfVlanPriority_Object=MibTableColumn
portDevIwfVlanPriority=_PortDevIwfVlanPriority_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,19),_PortDevIwfVlanPriority_Type())
portDevIwfVlanPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:portDevIwfVlanPriority.setStatus(_B)
class _PortDevIwfE1ChannelId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_PortDevIwfE1ChannelId_Type.__name__=_D
_PortDevIwfE1ChannelId_Object=MibTableColumn
portDevIwfE1ChannelId=_PortDevIwfE1ChannelId_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,20),_PortDevIwfE1ChannelId_Type())
portDevIwfE1ChannelId.setMaxAccess(_G)
if mibBuilder.loadTexts:portDevIwfE1ChannelId.setStatus(_B)
class _PortDevIwfE1ChannelKLM_Type(DisplayString):defaultValue=OctetString('')
_PortDevIwfE1ChannelKLM_Type.__name__=_p
_PortDevIwfE1ChannelKLM_Object=MibTableColumn
portDevIwfE1ChannelKLM=_PortDevIwfE1ChannelKLM_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,21),_PortDevIwfE1ChannelKLM_Type())
portDevIwfE1ChannelKLM.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfE1ChannelKLM.setStatus(_B)
_PortDevIwfDestMacAddress_Type=MacAddress
_PortDevIwfDestMacAddress_Object=MibTableColumn
portDevIwfDestMacAddress=_PortDevIwfDestMacAddress_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,22),_PortDevIwfDestMacAddress_Type())
portDevIwfDestMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:portDevIwfDestMacAddress.setStatus(_B)
_PortDevIwfTributaryUnitAlarm_Type=FaultStatus
_PortDevIwfTributaryUnitAlarm_Object=MibTableColumn
portDevIwfTributaryUnitAlarm=_PortDevIwfTributaryUnitAlarm_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,23),_PortDevIwfTributaryUnitAlarm_Type())
portDevIwfTributaryUnitAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfTributaryUnitAlarm.setStatus(_B)
_PortDevIwfMultiplexSectionAlarm_Type=FaultStatus
_PortDevIwfMultiplexSectionAlarm_Object=MibTableColumn
portDevIwfMultiplexSectionAlarm=_PortDevIwfMultiplexSectionAlarm_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,24),_PortDevIwfMultiplexSectionAlarm_Type())
portDevIwfMultiplexSectionAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfMultiplexSectionAlarm.setStatus(_B)
_PortDevIwfMultiplexSectionRDI_Type=FaultStatus
_PortDevIwfMultiplexSectionRDI_Object=MibTableColumn
portDevIwfMultiplexSectionRDI=_PortDevIwfMultiplexSectionRDI_Object((1,3,6,1,4,1,8708,2,57,2,5,1,1,25),_PortDevIwfMultiplexSectionRDI_Type())
portDevIwfMultiplexSectionRDI.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfMultiplexSectionRDI.setStatus(_B)
_PortDevIwfPmList_ObjectIdentity=ObjectIdentity
portDevIwfPmList=_PortDevIwfPmList_ObjectIdentity((1,3,6,1,4,1,8708,2,57,2,6))
_PortDevIwfPmTable_Object=MibTable
portDevIwfPmTable=_PortDevIwfPmTable_Object((1,3,6,1,4,1,8708,2,57,2,6,1))
if mibBuilder.loadTexts:portDevIwfPmTable.setStatus(_B)
_PortDevIwfPmEntry_Object=MibTableRow
portDevIwfPmEntry=_PortDevIwfPmEntry_Object((1,3,6,1,4,1,8708,2,57,2,6,1,1))
portDevIwfPmEntry.setIndexNames((0,_A,_v))
if mibBuilder.loadTexts:portDevIwfPmEntry.setStatus(_B)
class _PortDevIwfPmIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortDevIwfPmIndex_Type.__name__=_D
_PortDevIwfPmIndex_Object=MibTableColumn
portDevIwfPmIndex=_PortDevIwfPmIndex_Object((1,3,6,1,4,1,8708,2,57,2,6,1,1,1),_PortDevIwfPmIndex_Type())
portDevIwfPmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfPmIndex.setStatus(_B)
_PortDevIwfPmName_Type=MgmtNameString
_PortDevIwfPmName_Object=MibTableColumn
portDevIwfPmName=_PortDevIwfPmName_Object((1,3,6,1,4,1,8708,2,57,2,6,1,1,2),_PortDevIwfPmName_Type())
portDevIwfPmName.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfPmName.setStatus(_B)
_PortDevIwfPmRxPackets_Type=Counter64
_PortDevIwfPmRxPackets_Object=MibTableColumn
portDevIwfPmRxPackets=_PortDevIwfPmRxPackets_Object((1,3,6,1,4,1,8708,2,57,2,6,1,1,3),_PortDevIwfPmRxPackets_Type())
portDevIwfPmRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfPmRxPackets.setStatus(_B)
_PortDevIwfPmTxPackets_Type=Counter64
_PortDevIwfPmTxPackets_Object=MibTableColumn
portDevIwfPmTxPackets=_PortDevIwfPmTxPackets_Object((1,3,6,1,4,1,8708,2,57,2,6,1,1,4),_PortDevIwfPmTxPackets_Type())
portDevIwfPmTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfPmTxPackets.setStatus(_B)
_PortDevIwfPmMalformedPackets_Type=Counter64
_PortDevIwfPmMalformedPackets_Object=MibTableColumn
portDevIwfPmMalformedPackets=_PortDevIwfPmMalformedPackets_Object((1,3,6,1,4,1,8708,2,57,2,6,1,1,5),_PortDevIwfPmMalformedPackets_Type())
portDevIwfPmMalformedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfPmMalformedPackets.setStatus(_B)
_PortDevIwfPmReorderedPackets_Type=Counter64
_PortDevIwfPmReorderedPackets_Object=MibTableColumn
portDevIwfPmReorderedPackets=_PortDevIwfPmReorderedPackets_Object((1,3,6,1,4,1,8708,2,57,2,6,1,1,6),_PortDevIwfPmReorderedPackets_Type())
portDevIwfPmReorderedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfPmReorderedPackets.setStatus(_B)
_PortDevIwfPmMisorderedDroppedPackets_Type=Counter64
_PortDevIwfPmMisorderedDroppedPackets_Object=MibTableColumn
portDevIwfPmMisorderedDroppedPackets=_PortDevIwfPmMisorderedDroppedPackets_Object((1,3,6,1,4,1,8708,2,57,2,6,1,1,7),_PortDevIwfPmMisorderedDroppedPackets_Type())
portDevIwfPmMisorderedDroppedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfPmMisorderedDroppedPackets.setStatus(_B)
_PortDevIwfPmMissingPackets_Type=Counter64
_PortDevIwfPmMissingPackets_Object=MibTableColumn
portDevIwfPmMissingPackets=_PortDevIwfPmMissingPackets_Object((1,3,6,1,4,1,8708,2,57,2,6,1,1,8),_PortDevIwfPmMissingPackets_Type())
portDevIwfPmMissingPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfPmMissingPackets.setStatus(_B)
_PortDevIwfPmPlayedOutPackets_Type=Counter64
_PortDevIwfPmPlayedOutPackets_Object=MibTableColumn
portDevIwfPmPlayedOutPackets=_PortDevIwfPmPlayedOutPackets_Object((1,3,6,1,4,1,8708,2,57,2,6,1,1,9),_PortDevIwfPmPlayedOutPackets_Type())
portDevIwfPmPlayedOutPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfPmPlayedOutPackets.setStatus(_B)
_PortDevIwfPmJbOverrun_Type=Counter64
_PortDevIwfPmJbOverrun_Object=MibTableColumn
portDevIwfPmJbOverrun=_PortDevIwfPmJbOverrun_Object((1,3,6,1,4,1,8708,2,57,2,6,1,1,10),_PortDevIwfPmJbOverrun_Type())
portDevIwfPmJbOverrun.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfPmJbOverrun.setStatus(_B)
_PortDevIwfPmJbUnderrun_Type=Counter64
_PortDevIwfPmJbUnderrun_Object=MibTableColumn
portDevIwfPmJbUnderrun=_PortDevIwfPmJbUnderrun_Object((1,3,6,1,4,1,8708,2,57,2,6,1,1,11),_PortDevIwfPmJbUnderrun_Type())
portDevIwfPmJbUnderrun.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfPmJbUnderrun.setStatus(_B)
class _PortDevIwfPmReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('reset',2)))
_PortDevIwfPmReset_Type.__name__=_H
_PortDevIwfPmReset_Object=MibTableColumn
portDevIwfPmReset=_PortDevIwfPmReset_Object((1,3,6,1,4,1,8708,2,57,2,6,1,1,12),_PortDevIwfPmReset_Type())
portDevIwfPmReset.setMaxAccess(_E)
if mibBuilder.loadTexts:portDevIwfPmReset.setStatus(_B)
class _PortDevIwfPmInternalReference_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PortDevIwfPmInternalReference_Type.__name__=_D
_PortDevIwfPmInternalReference_Object=MibTableColumn
portDevIwfPmInternalReference=_PortDevIwfPmInternalReference_Object((1,3,6,1,4,1,8708,2,57,2,6,1,1,13),_PortDevIwfPmInternalReference_Type())
portDevIwfPmInternalReference.setMaxAccess(_C)
if mibBuilder.loadTexts:portDevIwfPmInternalReference.setStatus(_B)
class _PortDevIwfPmE1ChannelId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_PortDevIwfPmE1ChannelId_Type.__name__=_D
_PortDevIwfPmE1ChannelId_Object=MibTableColumn
portDevIwfPmE1ChannelId=_PortDevIwfPmE1ChannelId_Object((1,3,6,1,4,1,8708,2,57,2,6,1,1,14),_PortDevIwfPmE1ChannelId_Type())
portDevIwfPmE1ChannelId.setMaxAccess(_G)
if mibBuilder.loadTexts:portDevIwfPmE1ChannelId.setStatus(_B)
portDevGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,57,1,1,1))
portDevGeneralGroupV1.setObjects(*((_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj)))
if mibBuilder.loadTexts:portDevGeneralGroupV1.setStatus(_B)
portDevGenericGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,57,1,1,2))
portDevGenericGroupV1.setObjects(*((_A,_t),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_q),(_A,_AA),(_A,_AB),(_A,_q),(_A,_AC)))
if mibBuilder.loadTexts:portDevGenericGroupV1.setStatus(_F)
portDevEquipmentGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,57,1,1,3))
portDevEquipmentGroupV1.setObjects(*((_A,_I),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_w),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:portDevEquipmentGroupV1.setStatus(_F)
portDevFwGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,57,1,1,4))
portDevFwGroupV1.setObjects(*((_A,_A5),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az)))
if mibBuilder.loadTexts:portDevFwGroupV1.setStatus(_B)
portDevIwfGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,57,1,1,5))
portDevIwfGroupV1.setObjects(*((_A,_u),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN)))
if mibBuilder.loadTexts:portDevIwfGroupV1.setStatus(_F)
portDevIwfPmGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,57,1,1,6))
portDevIwfPmGroupV1.setObjects(*((_A,_v),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:portDevIwfPmGroupV1.setStatus(_F)
portDevEquipmentGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,57,1,1,7))
portDevEquipmentGroupV2.setObjects(*((_A,_I),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_w),(_A,_l),(_A,_m),(_A,_r),(_A,_U),(_A,_s)))
if mibBuilder.loadTexts:portDevEquipmentGroupV2.setStatus(_F)
portDevEquipmentGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,57,1,1,8))
portDevEquipmentGroupV3.setObjects(*((_A,_I),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_m),(_A,_T),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_U),(_A,_w),(_A,_l),(_A,_r),(_A,_s),(_A,_x)))
if mibBuilder.loadTexts:portDevEquipmentGroupV3.setStatus(_F)
portDevIwfGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,57,1,1,9))
portDevIwfGroupV2.setObjects(*((_A,_u),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3),(_A,_B4),(_A,_B5),(_A,_B6),(_A,_B7),(_A,_B8),(_A,_B9),(_A,_BA),(_A,_BB)))
if mibBuilder.loadTexts:portDevIwfGroupV2.setStatus(_B)
portDevIwfPmGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,57,1,1,10))
portDevIwfPmGroupV2.setObjects(*((_A,_v),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_BC)))
if mibBuilder.loadTexts:portDevIwfPmGroupV2.setStatus(_B)
portDevEquipmentGroupV4=ObjectGroup((1,3,6,1,4,1,8708,2,57,1,1,11))
portDevEquipmentGroupV4.setObjects(*((_A,_I),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_m),(_A,_T),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_U),(_A,_l),(_A,_r),(_A,_s),(_A,_x)))
if mibBuilder.loadTexts:portDevEquipmentGroupV4.setStatus(_F)
portDevEquipmentGroupV5=ObjectGroup((1,3,6,1,4,1,8708,2,57,1,1,12))
portDevEquipmentGroupV5.setObjects(*((_A,_I),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_m),(_A,_T),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_U),(_A,_l),(_A,_r),(_A,_s),(_A,_x),(_A,_BD)))
if mibBuilder.loadTexts:portDevEquipmentGroupV5.setStatus(_B)
portDevGenericGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,57,1,1,13))
portDevGenericGroupV2.setObjects(*((_A,_t),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_q),(_A,_AA),(_A,_AB),(_A,_q),(_A,_AC),(_A,_BE)))
if mibBuilder.loadTexts:portDevGenericGroupV2.setStatus(_B)
lumPortdeviceBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,57,1,2,1))
lumPortdeviceBasicComplV1.setObjects(*((_A,_J),(_A,_n),(_A,_BF),(_A,_K),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:lumPortdeviceBasicComplV1.setStatus(_F)
lumPortdeviceBasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,57,1,2,2))
lumPortdeviceBasicComplV2.setObjects(*((_A,_J),(_A,_n),(_A,_BG),(_A,_K),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:lumPortdeviceBasicComplV2.setStatus(_F)
lumPortdeviceBasicComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,57,1,2,3))
lumPortdeviceBasicComplV3.setObjects(*((_A,_J),(_A,_n),(_A,_BH),(_A,_K),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:lumPortdeviceBasicComplV3.setStatus(_F)
lumPortdeviceBasicComplV4=ModuleCompliance((1,3,6,1,4,1,8708,2,57,1,2,4))
lumPortdeviceBasicComplV4.setObjects(*((_A,_J),(_A,_n),(_A,_BI),(_A,_K),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:lumPortdeviceBasicComplV4.setStatus(_F)
lumPortdeviceBasicComplV5=ModuleCompliance((1,3,6,1,4,1,8708,2,57,1,2,5))
lumPortdeviceBasicComplV5.setObjects(*((_A,_J),(_A,_n),(_A,_Aa),(_A,_K),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:lumPortdeviceBasicComplV5.setStatus(_F)
lumPortdeviceBasicComplV6=ModuleCompliance((1,3,6,1,4,1,8708,2,57,1,2,6))
lumPortdeviceBasicComplV6.setObjects(*((_A,_J),(_A,_BJ),(_A,_Aa),(_A,_K),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:lumPortdeviceBasicComplV6.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_Ac:PortDeviceEquipmentType,'PortDeviceVersionType':PortDeviceVersionType,'PortDevFwImgState':PortDevFwImgState,_A4:PortSelection,'lumPortdeviceMIBModule':lumPortdeviceMIBModule,'lumPortdeviceConfs':lumPortdeviceConfs,'lumPortdeviceGroups':lumPortdeviceGroups,_J:portDevGeneralGroupV1,_n:portDevGenericGroupV1,_BF:portDevEquipmentGroupV1,_K:portDevFwGroupV1,_y:portDevIwfGroupV1,_z:portDevIwfPmGroupV1,_BG:portDevEquipmentGroupV2,_BH:portDevEquipmentGroupV3,_A0:portDevIwfGroupV2,_A1:portDevIwfPmGroupV2,_BI:portDevEquipmentGroupV4,_Aa:portDevEquipmentGroupV5,_BJ:portDevGenericGroupV2,'lumPortdeviceCompl':lumPortdeviceCompl,'lumPortdeviceBasicComplV1':lumPortdeviceBasicComplV1,'lumPortdeviceBasicComplV2':lumPortdeviceBasicComplV2,'lumPortdeviceBasicComplV3':lumPortdeviceBasicComplV3,'lumPortdeviceBasicComplV4':lumPortdeviceBasicComplV4,'lumPortdeviceBasicComplV5':lumPortdeviceBasicComplV5,'lumPortdeviceBasicComplV6':lumPortdeviceBasicComplV6,'lumPortdeviceMIBObjects':lumPortdeviceMIBObjects,'portDevGeneral':portDevGeneral,_Ad:portDevGeneralLastChangeTime,_Ae:portDevGeneralStateLastChangeTime,_Af:portDevGeneralGenericTableSize,_Ag:portDevGeneralEquipmentTableSize,_Ah:portDevGeneralFwTableSize,_Ai:portDevGeneralIwfTableSize,_Aj:portDevGeneralIwfPmTableSize,'portDevGenericList':portDevGenericList,'portDevGenericTable':portDevGenericTable,'portDevGenericEntry':portDevGenericEntry,_t:portDevGenericIndex,_A6:portDevGenericName,_A7:portDevGenericSubrack,_A8:portDevGenericSlot,_A9:portDevGenericAutoDiscoverInterval,_q:portDevGenericCreateNewPortDevice,_AC:portDevGenericRestartPortDevice,_AA:portDevGenericCreateMep,_AB:portDevGenericCreateMeg,_BE:portDevGenericCreateNewPortDeviceAdvanced,'portDevEquipmentList':portDevEquipmentList,'portDevEquipmentTable':portDevEquipmentTable,'portDevEquipmentEntry':portDevEquipmentEntry,_I:portDevEquipmentIndex,_L:portDevEquipmentName,_M:portDevEquipmentDescr,_N:portDevEquipmentLocation,_O:portDevEquipmentAdminStatus,_P:portDevEquipmentOperStatus,_Q:portDevEquipmentExpectedType,_R:portDevEquipmentActualType,_S:portDevEquipmentFwVersion,_m:portDevEquipmentFwUpgradeStatus,_T:portDevEquipmentLinkPassThrough,_V:portDevEquipmentSubrack,_W:portDevEquipmentSlot,_X:portDevEquipmentVlanId,_Y:portDevEquipmentRowStatus,_Z:portDevEquipmentNoDeviceFound,_a:portDevEquipmentMultiDeviceFound,_b:portDevEquipmentDeviceNotManageable,_c:portDevEquipmentDeviceNotReachable,_d:portDevEquipmentConfigurationFault,_e:portDevEquipmentPowerAMissing,_f:portDevEquipmentPowerBMissing,_g:portDevEquipmentInternalReference,_h:portDevEquipmentMacAddress,_i:portDevEquipmentLocalPortIndex,_j:portDevEquipmentAdminPowerA,_k:portDevEquipmentAdminPowerB,_U:portDevEquipmentSelectedPort,_w:portDevEquipmentDestMacAddress,_l:portDevEquipmentDestMacAddressCheck,_r:portDevEquipmentDeviceVersionType,_s:portDevEquipmentActivePort,_x:portDevEquipmentDyingGasp,_BD:portDevEquipmentLosCsf,'portDevFwList':portDevFwList,'portDevFwTable':portDevFwTable,'portDevFwEntry':portDevFwEntry,_A5:portDevFwIndex,_Ak:portDevFwSubrack,_Al:portDevFwSlot,_Am:portDevFwName,_An:portDevFwPortDevId,_Ao:portDevFwImgSlotOneNr,_Ap:portDevFwImgSlotOneVersion,_Aq:portDevFwImgSlotOneState,_Ar:portDevFwImgSlotOneDate,_As:portDevFwImgSlotTwoNr,_At:portDevFwImgSlotTwoVersion,_Au:portDevFwImgSlotTwoState,_Av:portDevFwImgSlotTwoDate,_Aw:portDevFwInstallFw,_Ax:portDevFwActivateFw,_Ay:portDevFwGetAllFiles,_Az:portDevFwUpgradeStatus,'portDevIwfList':portDevIwfList,'portDevIwfTable':portDevIwfTable,'portDevIwfEntry':portDevIwfEntry,_u:portDevIwfIndex,_AD:portDevIwfName,_AE:portDevIwfRtpClockSource,_AF:portDevIwfJitterBufferRecenter,_AG:portDevIwfInternalReference,_AH:portDevIwfLocalPortIndex,_AI:portDevIwfLossOfSignal,_AJ:portDevIwfLossOfFrame,_AK:portDevIwfEquipmentFailure,_AL:portDevIwfNoTdmPayload,_AM:portDevIwfRemotePacketLost,_AN:portDevIwfLocalPacketLost,_B2:portDevIwfAdminStatus,_B3:portDevIwfOperStatus,_B4:portDevIwfDescr,_B6:portDevIwfSignalFormat,_B5:portDevIwfEtherType,_B7:portDevIwfVlanId,_B8:portDevIwfVlanPriority,_B9:portDevIwfE1ChannelId,_BA:portDevIwfE1ChannelKLM,_BB:portDevIwfDestMacAddress,_A_:portDevIwfTributaryUnitAlarm,_B0:portDevIwfMultiplexSectionAlarm,_B1:portDevIwfMultiplexSectionRDI,'portDevIwfPmList':portDevIwfPmList,'portDevIwfPmTable':portDevIwfPmTable,'portDevIwfPmEntry':portDevIwfPmEntry,_v:portDevIwfPmIndex,_AO:portDevIwfPmName,_AP:portDevIwfPmRxPackets,_AQ:portDevIwfPmTxPackets,_AR:portDevIwfPmMalformedPackets,_AS:portDevIwfPmReorderedPackets,_AT:portDevIwfPmMisorderedDroppedPackets,_AU:portDevIwfPmMissingPackets,_AV:portDevIwfPmPlayedOutPackets,_AW:portDevIwfPmJbOverrun,_AX:portDevIwfPmJbUnderrun,_AY:portDevIwfPmReset,_AZ:portDevIwfPmInternalReference,_BC:portDevIwfPmE1ChannelId})