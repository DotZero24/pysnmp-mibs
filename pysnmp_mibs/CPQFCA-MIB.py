_As='cpqFcaHostCntlrWorldWidePortName'
_Ar='cpqFcaHostCntlrSerialNumber'
_Aq='cpqFcaHostCntlrHwLocation'
_Ap='cpqFcaLogDrvSize'
_Ao='cpqFcaLogDrvFaultTol'
_An='cpqFcaLogDrvOsName'
_Am='cpqFcaCntlrSerialNumber'
_Al='cpqFcaAccelErrCode'
_Ak='cpqFcaPhyDrvFailureCode'
_Aj='cpqFcaPhyDrvFWRev'
_Ai='cpqFcaPhyDrvSerialNum'
_Ah='cpqFcaPhyDrvModel'
_Ag='cpqFcTapeCntlrStatus'
_Af='cpqFcaSpareStatus'
_Ae='cpqFcaSpareBay'
_Ad='cpqFcaSpareBusNumber'
_Ac='cpqFcSwitchIndex'
_Ab='cpqFcTapeCountersScsiLun'
_Aa='cpqFcTapeCountersScsiTarget'
_AZ='cpqFcTapeCountersScsiBus'
_AY='cpqFcTapeCountersCntlrIndex'
_AX='notCapable'
_AW='cpqFcTapeCntlrIndex'
_AV='cpqExtArrSnapshotIndex'
_AU='cpqExtArrSnapshotRsrcVolIndex'
_AT='cpqExtArrSnapshotBoxIndex'
_AS='cpqExtArrRsrcVolIndex'
_AR='cpqExtArrRsrcVolBoxIndex'
_AQ='cpqFcaPhyDrvThrIndex'
_AP='cpqFcaPhyDrvThrBoxIndex'
_AO='asynchronous'
_AN='nonHotPlug'
_AM='cpqFcaPhyDrvIndex'
_AL='cpqFcaPhyDrvBoxIndex'
_AK='cpqFcaSparePhyDrvIndex'
_AJ='cpqFcaSpareBoxIndex'
_AI='notAvailable'
_AH='unconfigured'
_AG='cpqFcaAccelBoxIndex'
_AF='expandInProgress'
_AE='cpqFcaCntlrBoxIndex'
_AD='cpqFcaOsCommonModuleIndex'
_AC='NotificationType'
_AB='cpqFcTapeLibraryLocation'
_AA='cpqFcTapeLibrarySerialNumber'
_A9='cpqFcTapeLibraryFWRev'
_A8='cpqFcTapeLibraryModel'
_A7='cpqFcaHostCntlrWorldWideName'
_A6='cpqFcaHostCntlrModel'
_A5='cpqFcaHostCntlrSlot'
_A4='cpqFcTapeDriveStatus'
_A3='cpqFcTapeLibraryDoorStatus'
_A2='cpqFcTapeLibraryStatus'
_A1='cpqFcaCntlrStatus'
_A0='cpqFcaAccelStatus'
_z='cpqFcaPhyDrvStatus'
_y='cpqFcaPhyDrvBay'
_x='cpqFcaPhyDrvBusNumber'
_w='cpqFcaLogDrvStatus'
_v='cpqFcaHostCntlrIndex'
_u='cpqFcaLogDrvBoxIndex'
_t='notConnected'
_s='cpqFcTapeDriveLocation'
_r='cpqFcTapeDriveSerialNumber'
_q='cpqFcTapeDriveFWRev'
_p='cpqFcTapeDriveModel'
_o='cpqFcaAccelSerialNumber'
_n='cpqFcaHostCntlrStatus'
_m='notSupported'
_l='cpqFcTapeLibraryCntlrIndex'
_k='cpqFcaLogDrvIndex'
_j='active'
_i='read-write'
_h='cpqFcaAccelTotalMemory'
_g='cpqFcaCntlrModel'
_f='cpqFcTapeDriveCntlrIndex'
_e='unknown'
_d='offline'
_c='cpqFcaCntlrBoxIoSlot'
_b='cpqFcTapeLibraryScsiLun'
_a='cpqFcTapeLibraryScsiTarget'
_Z='cpqFcTapeLibraryScsiBus'
_Y='cpqFcTapeCntlrWWN'
_X='cpqFcTapeDriveScsiLun'
_W='cpqFcTapeDriveScsiTarget'
_V='cpqFcTapeDriveScsiBus'
_U='cpqFcaAccelBoxIoSlot'
_T='OctetString'
_S='true'
_R='false'
_Q='degraded'
_P='deprecated'
_O='cpqSsChassisTime'
_N='cpqSsChassisName'
_M='failed'
_L='ok'
_K='sysName'
_J='SNMPv2-MIB'
_I='CPQSTSYS-MIB'
_H='cpqHoTrapFlags'
_G='CPQHOST-MIB'
_F='DisplayString'
_E='other'
_D='Integer32'
_C='CPQFCA-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_T,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,cpqHoTrapFlags=mibBuilder.importSymbols(_G,'compaq',_H)
cpqSsChassisName,cpqSsChassisTime=mibBuilder.importSymbols(_I,_N,_O)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_J,_K)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_AC,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_AC,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
_CpqFibreArray_ObjectIdentity=ObjectIdentity
cpqFibreArray=_CpqFibreArray_ObjectIdentity((1,3,6,1,4,1,232,16))
_CpqFcaMibRev_ObjectIdentity=ObjectIdentity
cpqFcaMibRev=_CpqFcaMibRev_ObjectIdentity((1,3,6,1,4,1,232,16,1))
class _CpqFcaMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqFcaMibRevMajor_Type.__name__=_D
_CpqFcaMibRevMajor_Object=MibScalar
cpqFcaMibRevMajor=_CpqFcaMibRevMajor_Object((1,3,6,1,4,1,232,16,1,1),_CpqFcaMibRevMajor_Type())
cpqFcaMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaMibRevMajor.setStatus(_A)
class _CpqFcaMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqFcaMibRevMinor_Type.__name__=_D
_CpqFcaMibRevMinor_Object=MibScalar
cpqFcaMibRevMinor=_CpqFcaMibRevMinor_Object((1,3,6,1,4,1,232,16,1,2),_CpqFcaMibRevMinor_Type())
cpqFcaMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaMibRevMinor.setStatus(_A)
class _CpqFcaMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_L,2),(_Q,3),(_M,4)))
_CpqFcaMibCondition_Type.__name__=_D
_CpqFcaMibCondition_Object=MibScalar
cpqFcaMibCondition=_CpqFcaMibCondition_Object((1,3,6,1,4,1,232,16,1,3),_CpqFcaMibCondition_Type())
cpqFcaMibCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaMibCondition.setStatus(_A)
_CpqFcaComponent_ObjectIdentity=ObjectIdentity
cpqFcaComponent=_CpqFcaComponent_ObjectIdentity((1,3,6,1,4,1,232,16,2))
_CpqFcaInterface_ObjectIdentity=ObjectIdentity
cpqFcaInterface=_CpqFcaInterface_ObjectIdentity((1,3,6,1,4,1,232,16,2,1))
_CpqFcaOsCommon_ObjectIdentity=ObjectIdentity
cpqFcaOsCommon=_CpqFcaOsCommon_ObjectIdentity((1,3,6,1,4,1,232,16,2,1,4))
class _CpqFcaOsCommonPollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqFcaOsCommonPollFreq_Type.__name__=_D
_CpqFcaOsCommonPollFreq_Object=MibScalar
cpqFcaOsCommonPollFreq=_CpqFcaOsCommonPollFreq_Object((1,3,6,1,4,1,232,16,2,1,4,1),_CpqFcaOsCommonPollFreq_Type())
cpqFcaOsCommonPollFreq.setMaxAccess(_i)
if mibBuilder.loadTexts:cpqFcaOsCommonPollFreq.setStatus(_A)
_CpqFcaOsCommonModuleTable_Object=MibTable
cpqFcaOsCommonModuleTable=_CpqFcaOsCommonModuleTable_Object((1,3,6,1,4,1,232,16,2,1,4,2))
if mibBuilder.loadTexts:cpqFcaOsCommonModuleTable.setStatus(_P)
_CpqFcaOsCommonModuleEntry_Object=MibTableRow
cpqFcaOsCommonModuleEntry=_CpqFcaOsCommonModuleEntry_Object((1,3,6,1,4,1,232,16,2,1,4,2,1))
cpqFcaOsCommonModuleEntry.setIndexNames((0,_C,_AD))
if mibBuilder.loadTexts:cpqFcaOsCommonModuleEntry.setStatus(_P)
class _CpqFcaOsCommonModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqFcaOsCommonModuleIndex_Type.__name__=_D
_CpqFcaOsCommonModuleIndex_Object=MibTableColumn
cpqFcaOsCommonModuleIndex=_CpqFcaOsCommonModuleIndex_Object((1,3,6,1,4,1,232,16,2,1,4,2,1,1),_CpqFcaOsCommonModuleIndex_Type())
cpqFcaOsCommonModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaOsCommonModuleIndex.setStatus(_P)
class _CpqFcaOsCommonModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqFcaOsCommonModuleName_Type.__name__=_F
_CpqFcaOsCommonModuleName_Object=MibTableColumn
cpqFcaOsCommonModuleName=_CpqFcaOsCommonModuleName_Object((1,3,6,1,4,1,232,16,2,1,4,2,1,2),_CpqFcaOsCommonModuleName_Type())
cpqFcaOsCommonModuleName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaOsCommonModuleName.setStatus(_P)
class _CpqFcaOsCommonModuleVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqFcaOsCommonModuleVersion_Type.__name__=_F
_CpqFcaOsCommonModuleVersion_Object=MibTableColumn
cpqFcaOsCommonModuleVersion=_CpqFcaOsCommonModuleVersion_Object((1,3,6,1,4,1,232,16,2,1,4,2,1,3),_CpqFcaOsCommonModuleVersion_Type())
cpqFcaOsCommonModuleVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaOsCommonModuleVersion.setStatus(_P)
class _CpqFcaOsCommonModuleDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqFcaOsCommonModuleDate_Type.__name__=_T
_CpqFcaOsCommonModuleDate_Object=MibTableColumn
cpqFcaOsCommonModuleDate=_CpqFcaOsCommonModuleDate_Object((1,3,6,1,4,1,232,16,2,1,4,2,1,4),_CpqFcaOsCommonModuleDate_Type())
cpqFcaOsCommonModuleDate.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaOsCommonModuleDate.setStatus(_P)
class _CpqFcaOsCommonModulePurpose_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqFcaOsCommonModulePurpose_Type.__name__=_F
_CpqFcaOsCommonModulePurpose_Object=MibTableColumn
cpqFcaOsCommonModulePurpose=_CpqFcaOsCommonModulePurpose_Object((1,3,6,1,4,1,232,16,2,1,4,2,1,5),_CpqFcaOsCommonModulePurpose_Type())
cpqFcaOsCommonModulePurpose.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaOsCommonModulePurpose.setStatus(_P)
_CpqFcaCntlr_ObjectIdentity=ObjectIdentity
cpqFcaCntlr=_CpqFcaCntlr_ObjectIdentity((1,3,6,1,4,1,232,16,2,2))
_CpqFcaCntlrTable_Object=MibTable
cpqFcaCntlrTable=_CpqFcaCntlrTable_Object((1,3,6,1,4,1,232,16,2,2,1))
if mibBuilder.loadTexts:cpqFcaCntlrTable.setStatus(_A)
_CpqFcaCntlrEntry_Object=MibTableRow
cpqFcaCntlrEntry=_CpqFcaCntlrEntry_Object((1,3,6,1,4,1,232,16,2,2,1,1))
cpqFcaCntlrEntry.setIndexNames((0,_C,_AE),(0,_C,_c))
if mibBuilder.loadTexts:cpqFcaCntlrEntry.setStatus(_A)
class _CpqFcaCntlrBoxIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqFcaCntlrBoxIndex_Type.__name__=_D
_CpqFcaCntlrBoxIndex_Object=MibTableColumn
cpqFcaCntlrBoxIndex=_CpqFcaCntlrBoxIndex_Object((1,3,6,1,4,1,232,16,2,2,1,1,1),_CpqFcaCntlrBoxIndex_Type())
cpqFcaCntlrBoxIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaCntlrBoxIndex.setStatus(_A)
class _CpqFcaCntlrBoxIoSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqFcaCntlrBoxIoSlot_Type.__name__=_D
_CpqFcaCntlrBoxIoSlot_Object=MibTableColumn
cpqFcaCntlrBoxIoSlot=_CpqFcaCntlrBoxIoSlot_Object((1,3,6,1,4,1,232,16,2,2,1,1,2),_CpqFcaCntlrBoxIoSlot_Type())
cpqFcaCntlrBoxIoSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaCntlrBoxIoSlot.setStatus(_A)
class _CpqFcaCntlrModel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_E,1),('fibreArray',2),('msa1000',3),('smartArrayClusterStorage',4),('hsg80',5),('hsv110',6),('msa500G2',7),('msa20',8),('msa1510i',9)))
_CpqFcaCntlrModel_Type.__name__=_D
_CpqFcaCntlrModel_Object=MibTableColumn
cpqFcaCntlrModel=_CpqFcaCntlrModel_Object((1,3,6,1,4,1,232,16,2,2,1,1,3),_CpqFcaCntlrModel_Type())
cpqFcaCntlrModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaCntlrModel.setStatus(_A)
class _CpqFcaCntlrFWRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqFcaCntlrFWRev_Type.__name__=_F
_CpqFcaCntlrFWRev_Object=MibTableColumn
cpqFcaCntlrFWRev=_CpqFcaCntlrFWRev_Object((1,3,6,1,4,1,232,16,2,2,1,1,4),_CpqFcaCntlrFWRev_Type())
cpqFcaCntlrFWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaCntlrFWRev.setStatus(_A)
class _CpqFcaCntlrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_L,2),(_M,3),(_d,4),('redundantPathOffline',5),(_t,6)))
_CpqFcaCntlrStatus_Type.__name__=_D
_CpqFcaCntlrStatus_Object=MibTableColumn
cpqFcaCntlrStatus=_CpqFcaCntlrStatus_Object((1,3,6,1,4,1,232,16,2,2,1,1,5),_CpqFcaCntlrStatus_Type())
cpqFcaCntlrStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaCntlrStatus.setStatus(_A)
class _CpqFcaCntlrCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_L,2),(_Q,3),(_M,4)))
_CpqFcaCntlrCondition_Type.__name__=_D
_CpqFcaCntlrCondition_Object=MibTableColumn
cpqFcaCntlrCondition=_CpqFcaCntlrCondition_Object((1,3,6,1,4,1,232,16,2,2,1,1,6),_CpqFcaCntlrCondition_Type())
cpqFcaCntlrCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaCntlrCondition.setStatus(_A)
class _CpqFcaCntlrProductRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1))
_CpqFcaCntlrProductRev_Type.__name__=_F
_CpqFcaCntlrProductRev_Object=MibTableColumn
cpqFcaCntlrProductRev=_CpqFcaCntlrProductRev_Object((1,3,6,1,4,1,232,16,2,2,1,1,7),_CpqFcaCntlrProductRev_Type())
cpqFcaCntlrProductRev.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaCntlrProductRev.setStatus(_A)
class _CpqFcaCntlrWorldWideName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CpqFcaCntlrWorldWideName_Type.__name__=_F
_CpqFcaCntlrWorldWideName_Object=MibTableColumn
cpqFcaCntlrWorldWideName=_CpqFcaCntlrWorldWideName_Object((1,3,6,1,4,1,232,16,2,2,1,1,8),_CpqFcaCntlrWorldWideName_Type())
cpqFcaCntlrWorldWideName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaCntlrWorldWideName.setStatus(_A)
class _CpqFcaCntlrSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CpqFcaCntlrSerialNumber_Type.__name__=_F
_CpqFcaCntlrSerialNumber_Object=MibTableColumn
cpqFcaCntlrSerialNumber=_CpqFcaCntlrSerialNumber_Object((1,3,6,1,4,1,232,16,2,2,1,1,9),_CpqFcaCntlrSerialNumber_Type())
cpqFcaCntlrSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaCntlrSerialNumber.setStatus(_A)
class _CpqFcaCntlrCurrentRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('notDuplexed',2),(_j,3),('backup',4)))
_CpqFcaCntlrCurrentRole_Type.__name__=_D
_CpqFcaCntlrCurrentRole_Object=MibTableColumn
cpqFcaCntlrCurrentRole=_CpqFcaCntlrCurrentRole_Object((1,3,6,1,4,1,232,16,2,2,1,1,10),_CpqFcaCntlrCurrentRole_Type())
cpqFcaCntlrCurrentRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaCntlrCurrentRole.setStatus(_A)
class _CpqFcaCntlrRedundancyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('notRedundant',2),('fwActiveStandby',3),('fwPrimarySecondary',4),('fwActiveActive',5)))
_CpqFcaCntlrRedundancyType_Type.__name__=_D
_CpqFcaCntlrRedundancyType_Object=MibTableColumn
cpqFcaCntlrRedundancyType=_CpqFcaCntlrRedundancyType_Object((1,3,6,1,4,1,232,16,2,2,1,1,11),_CpqFcaCntlrRedundancyType_Type())
cpqFcaCntlrRedundancyType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaCntlrRedundancyType.setStatus(_A)
class _CpqFcaCntlrRedundancyError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_E,1),('noFailure',2),('noRedundantController',3),('differentHardware',4),('noLink',5),('differentFirmware',6),('differentCache',7),('otherCacheFailure',8),('noDrives',9),('otherNoDrives',10),('unsupportedDrives',11),(_AF,12)))
_CpqFcaCntlrRedundancyError_Type.__name__=_D
_CpqFcaCntlrRedundancyError_Object=MibTableColumn
cpqFcaCntlrRedundancyError=_CpqFcaCntlrRedundancyError_Object((1,3,6,1,4,1,232,16,2,2,1,1,12),_CpqFcaCntlrRedundancyError_Type())
cpqFcaCntlrRedundancyError.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaCntlrRedundancyError.setStatus(_A)
_CpqFcaCntlrBlinkTime_Type=Counter32
_CpqFcaCntlrBlinkTime_Object=MibTableColumn
cpqFcaCntlrBlinkTime=_CpqFcaCntlrBlinkTime_Object((1,3,6,1,4,1,232,16,2,2,1,1,13),_CpqFcaCntlrBlinkTime_Type())
cpqFcaCntlrBlinkTime.setMaxAccess(_i)
if mibBuilder.loadTexts:cpqFcaCntlrBlinkTime.setStatus(_A)
class _CpqFcaCntlrWorldWideNodeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CpqFcaCntlrWorldWideNodeName_Type.__name__=_F
_CpqFcaCntlrWorldWideNodeName_Object=MibTableColumn
cpqFcaCntlrWorldWideNodeName=_CpqFcaCntlrWorldWideNodeName_Object((1,3,6,1,4,1,232,16,2,2,1,1,14),_CpqFcaCntlrWorldWideNodeName_Type())
cpqFcaCntlrWorldWideNodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaCntlrWorldWideNodeName.setStatus(_A)
class _CpqFcaCntlrRebuildPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('low',2),('medium',3),('high',4)))
_CpqFcaCntlrRebuildPriority_Type.__name__=_D
_CpqFcaCntlrRebuildPriority_Object=MibTableColumn
cpqFcaCntlrRebuildPriority=_CpqFcaCntlrRebuildPriority_Object((1,3,6,1,4,1,232,16,2,2,1,1,15),_CpqFcaCntlrRebuildPriority_Type())
cpqFcaCntlrRebuildPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaCntlrRebuildPriority.setStatus(_A)
class _CpqFcaCntlrExpandPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('low',2),('medium',3),('high',4)))
_CpqFcaCntlrExpandPriority_Type.__name__=_D
_CpqFcaCntlrExpandPriority_Object=MibTableColumn
cpqFcaCntlrExpandPriority=_CpqFcaCntlrExpandPriority_Object((1,3,6,1,4,1,232,16,2,2,1,1,16),_CpqFcaCntlrExpandPriority_Type())
cpqFcaCntlrExpandPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaCntlrExpandPriority.setStatus(_A)
_CpqFcaAccelTable_Object=MibTable
cpqFcaAccelTable=_CpqFcaAccelTable_Object((1,3,6,1,4,1,232,16,2,2,2))
if mibBuilder.loadTexts:cpqFcaAccelTable.setStatus(_A)
_CpqFcaAccelEntry_Object=MibTableRow
cpqFcaAccelEntry=_CpqFcaAccelEntry_Object((1,3,6,1,4,1,232,16,2,2,2,1))
cpqFcaAccelEntry.setIndexNames((0,_C,_AG),(0,_C,_U))
if mibBuilder.loadTexts:cpqFcaAccelEntry.setStatus(_A)
class _CpqFcaAccelBoxIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqFcaAccelBoxIndex_Type.__name__=_D
_CpqFcaAccelBoxIndex_Object=MibTableColumn
cpqFcaAccelBoxIndex=_CpqFcaAccelBoxIndex_Object((1,3,6,1,4,1,232,16,2,2,2,1,1),_CpqFcaAccelBoxIndex_Type())
cpqFcaAccelBoxIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaAccelBoxIndex.setStatus(_A)
class _CpqFcaAccelBoxIoSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqFcaAccelBoxIoSlot_Type.__name__=_D
_CpqFcaAccelBoxIoSlot_Object=MibTableColumn
cpqFcaAccelBoxIoSlot=_CpqFcaAccelBoxIoSlot_Object((1,3,6,1,4,1,232,16,2,2,2,1,2),_CpqFcaAccelBoxIoSlot_Type())
cpqFcaAccelBoxIoSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaAccelBoxIoSlot.setStatus(_A)
class _CpqFcaAccelStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('invalid',2),('enabled',3),('tmpDisabled',4),('permDisabled',5)))
_CpqFcaAccelStatus_Type.__name__=_D
_CpqFcaAccelStatus_Object=MibTableColumn
cpqFcaAccelStatus=_CpqFcaAccelStatus_Object((1,3,6,1,4,1,232,16,2,2,2,1,3),_CpqFcaAccelStatus_Type())
cpqFcaAccelStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaAccelStatus.setStatus(_A)
class _CpqFcaAccelBadData_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('none',2),('possible',3)))
_CpqFcaAccelBadData_Type.__name__=_D
_CpqFcaAccelBadData_Object=MibTableColumn
cpqFcaAccelBadData=_CpqFcaAccelBadData_Object((1,3,6,1,4,1,232,16,2,2,2,1,4),_CpqFcaAccelBadData_Type())
cpqFcaAccelBadData.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaAccelBadData.setStatus(_A)
class _CpqFcaAccelErrCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19)));namedValues=NamedValues(*((_E,1),('invalid',2),('badConfig',3),('lowBattery',4),('disableCmd',5),('noResources',6),(_t,7),('badMirrorData',8),('readErr',9),('writeErr',10),('configCmd',11),(_AF,12),('snapshotInProgress',13),('redundantLowBattery',14),('redundantSizeMismatch',15),('redundantCacheFailure',16),('excessiveEccErrors',17),('postEccErrors',19)))
_CpqFcaAccelErrCode_Type.__name__=_D
_CpqFcaAccelErrCode_Object=MibTableColumn
cpqFcaAccelErrCode=_CpqFcaAccelErrCode_Object((1,3,6,1,4,1,232,16,2,2,2,1,5),_CpqFcaAccelErrCode_Type())
cpqFcaAccelErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaAccelErrCode.setStatus(_A)
class _CpqFcaAccelBatteryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_L,2),('recharging',3),(_M,4),(_Q,5),('notPresent',6)))
_CpqFcaAccelBatteryStatus_Type.__name__=_D
_CpqFcaAccelBatteryStatus_Object=MibTableColumn
cpqFcaAccelBatteryStatus=_CpqFcaAccelBatteryStatus_Object((1,3,6,1,4,1,232,16,2,2,2,1,6),_CpqFcaAccelBatteryStatus_Type())
cpqFcaAccelBatteryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaAccelBatteryStatus.setStatus(_A)
_CpqFcaAccelReadErrs_Type=Counter32
_CpqFcaAccelReadErrs_Object=MibTableColumn
cpqFcaAccelReadErrs=_CpqFcaAccelReadErrs_Object((1,3,6,1,4,1,232,16,2,2,2,1,7),_CpqFcaAccelReadErrs_Type())
cpqFcaAccelReadErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaAccelReadErrs.setStatus(_A)
_CpqFcaAccelWriteErrs_Type=Counter32
_CpqFcaAccelWriteErrs_Object=MibTableColumn
cpqFcaAccelWriteErrs=_CpqFcaAccelWriteErrs_Object((1,3,6,1,4,1,232,16,2,2,2,1,8),_CpqFcaAccelWriteErrs_Type())
cpqFcaAccelWriteErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaAccelWriteErrs.setStatus(_A)
class _CpqFcaAccelCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_L,2),(_Q,3),(_M,4)))
_CpqFcaAccelCondition_Type.__name__=_D
_CpqFcaAccelCondition_Object=MibTableColumn
cpqFcaAccelCondition=_CpqFcaAccelCondition_Object((1,3,6,1,4,1,232,16,2,2,2,1,9),_CpqFcaAccelCondition_Type())
cpqFcaAccelCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaAccelCondition.setStatus(_A)
_CpqFcaAccelWriteCache_Type=Integer32
_CpqFcaAccelWriteCache_Object=MibTableColumn
cpqFcaAccelWriteCache=_CpqFcaAccelWriteCache_Object((1,3,6,1,4,1,232,16,2,2,2,1,10),_CpqFcaAccelWriteCache_Type())
cpqFcaAccelWriteCache.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaAccelWriteCache.setStatus(_A)
_CpqFcaAccelReadCache_Type=Integer32
_CpqFcaAccelReadCache_Object=MibTableColumn
cpqFcaAccelReadCache=_CpqFcaAccelReadCache_Object((1,3,6,1,4,1,232,16,2,2,2,1,11),_CpqFcaAccelReadCache_Type())
cpqFcaAccelReadCache.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaAccelReadCache.setStatus(_A)
class _CpqFcaAccelSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CpqFcaAccelSerialNumber_Type.__name__=_F
_CpqFcaAccelSerialNumber_Object=MibTableColumn
cpqFcaAccelSerialNumber=_CpqFcaAccelSerialNumber_Object((1,3,6,1,4,1,232,16,2,2,2,1,12),_CpqFcaAccelSerialNumber_Type())
cpqFcaAccelSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaAccelSerialNumber.setStatus(_A)
_CpqFcaAccelTotalMemory_Type=Integer32
_CpqFcaAccelTotalMemory_Object=MibTableColumn
cpqFcaAccelTotalMemory=_CpqFcaAccelTotalMemory_Object((1,3,6,1,4,1,232,16,2,2,2,1,13),_CpqFcaAccelTotalMemory_Type())
cpqFcaAccelTotalMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaAccelTotalMemory.setStatus(_A)
class _CpqFcaAccelFailedBatteries_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CpqFcaAccelFailedBatteries_Type.__name__=_T
_CpqFcaAccelFailedBatteries_Object=MibTableColumn
cpqFcaAccelFailedBatteries=_CpqFcaAccelFailedBatteries_Object((1,3,6,1,4,1,232,16,2,2,2,1,14),_CpqFcaAccelFailedBatteries_Type())
cpqFcaAccelFailedBatteries.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaAccelFailedBatteries.setStatus(_A)
_CpqFcaLogDrv_ObjectIdentity=ObjectIdentity
cpqFcaLogDrv=_CpqFcaLogDrv_ObjectIdentity((1,3,6,1,4,1,232,16,2,3))
_CpqFcaLogDrvTable_Object=MibTable
cpqFcaLogDrvTable=_CpqFcaLogDrvTable_Object((1,3,6,1,4,1,232,16,2,3,1))
if mibBuilder.loadTexts:cpqFcaLogDrvTable.setStatus(_A)
_CpqFcaLogDrvEntry_Object=MibTableRow
cpqFcaLogDrvEntry=_CpqFcaLogDrvEntry_Object((1,3,6,1,4,1,232,16,2,3,1,1))
cpqFcaLogDrvEntry.setIndexNames((0,_C,_u),(0,_C,_k))
if mibBuilder.loadTexts:cpqFcaLogDrvEntry.setStatus(_A)
class _CpqFcaLogDrvBoxIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqFcaLogDrvBoxIndex_Type.__name__=_D
_CpqFcaLogDrvBoxIndex_Object=MibTableColumn
cpqFcaLogDrvBoxIndex=_CpqFcaLogDrvBoxIndex_Object((1,3,6,1,4,1,232,16,2,3,1,1,1),_CpqFcaLogDrvBoxIndex_Type())
cpqFcaLogDrvBoxIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaLogDrvBoxIndex.setStatus(_A)
class _CpqFcaLogDrvIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqFcaLogDrvIndex_Type.__name__=_D
_CpqFcaLogDrvIndex_Object=MibTableColumn
cpqFcaLogDrvIndex=_CpqFcaLogDrvIndex_Object((1,3,6,1,4,1,232,16,2,3,1,1,2),_CpqFcaLogDrvIndex_Type())
cpqFcaLogDrvIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaLogDrvIndex.setStatus(_A)
class _CpqFcaLogDrvFaultTol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,7)));namedValues=NamedValues(*((_E,1),('none',2),('mirroring',3),('dataGuard',4),('distribDataGuard',5),('advancedDataGuard',7)))
_CpqFcaLogDrvFaultTol_Type.__name__=_D
_CpqFcaLogDrvFaultTol_Object=MibTableColumn
cpqFcaLogDrvFaultTol=_CpqFcaLogDrvFaultTol_Object((1,3,6,1,4,1,232,16,2,3,1,1,3),_CpqFcaLogDrvFaultTol_Type())
cpqFcaLogDrvFaultTol.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaLogDrvFaultTol.setStatus(_A)
class _CpqFcaLogDrvStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_E,1),(_L,2),(_M,3),(_AH,4),('recovering',5),('readyForRebuild',6),('rebuilding',7),('wrongDrive',8),('badConnect',9),('overheating',10),('shutdown',11),('expanding',12),(_AI,13),('queuedForExpansion',14),('hardError',15)))
_CpqFcaLogDrvStatus_Type.__name__=_D
_CpqFcaLogDrvStatus_Object=MibTableColumn
cpqFcaLogDrvStatus=_CpqFcaLogDrvStatus_Object((1,3,6,1,4,1,232,16,2,3,1,1,4),_CpqFcaLogDrvStatus_Type())
cpqFcaLogDrvStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaLogDrvStatus.setStatus(_A)
_CpqFcaLogDrvAutoRel_Type=Integer32
_CpqFcaLogDrvAutoRel_Object=MibTableColumn
cpqFcaLogDrvAutoRel=_CpqFcaLogDrvAutoRel_Object((1,3,6,1,4,1,232,16,2,3,1,1,5),_CpqFcaLogDrvAutoRel_Type())
cpqFcaLogDrvAutoRel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaLogDrvAutoRel.setStatus(_A)
_CpqFcaLogDrvPercentRebuild_Type=Gauge32
_CpqFcaLogDrvPercentRebuild_Object=MibTableColumn
cpqFcaLogDrvPercentRebuild=_CpqFcaLogDrvPercentRebuild_Object((1,3,6,1,4,1,232,16,2,3,1,1,6),_CpqFcaLogDrvPercentRebuild_Type())
cpqFcaLogDrvPercentRebuild.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaLogDrvPercentRebuild.setStatus(_A)
class _CpqFcaLogDrvHasAccel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('unavailable',2),('enabled',3),('disabled',4)))
_CpqFcaLogDrvHasAccel_Type.__name__=_D
_CpqFcaLogDrvHasAccel_Object=MibTableColumn
cpqFcaLogDrvHasAccel=_CpqFcaLogDrvHasAccel_Object((1,3,6,1,4,1,232,16,2,3,1,1,7),_CpqFcaLogDrvHasAccel_Type())
cpqFcaLogDrvHasAccel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaLogDrvHasAccel.setStatus(_A)
class _CpqFcaLogDrvAvailSpares_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqFcaLogDrvAvailSpares_Type.__name__=_T
_CpqFcaLogDrvAvailSpares_Object=MibTableColumn
cpqFcaLogDrvAvailSpares=_CpqFcaLogDrvAvailSpares_Object((1,3,6,1,4,1,232,16,2,3,1,1,8),_CpqFcaLogDrvAvailSpares_Type())
cpqFcaLogDrvAvailSpares.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaLogDrvAvailSpares.setStatus(_A)
class _CpqFcaLogDrvSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqFcaLogDrvSize_Type.__name__=_D
_CpqFcaLogDrvSize_Object=MibTableColumn
cpqFcaLogDrvSize=_CpqFcaLogDrvSize_Object((1,3,6,1,4,1,232,16,2,3,1,1,9),_CpqFcaLogDrvSize_Type())
cpqFcaLogDrvSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaLogDrvSize.setStatus(_A)
class _CpqFcaLogDrvPhyDrvIDs_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqFcaLogDrvPhyDrvIDs_Type.__name__=_T
_CpqFcaLogDrvPhyDrvIDs_Object=MibTableColumn
cpqFcaLogDrvPhyDrvIDs=_CpqFcaLogDrvPhyDrvIDs_Object((1,3,6,1,4,1,232,16,2,3,1,1,10),_CpqFcaLogDrvPhyDrvIDs_Type())
cpqFcaLogDrvPhyDrvIDs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaLogDrvPhyDrvIDs.setStatus(_A)
class _CpqFcaLogDrvCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_L,2),(_Q,3),(_M,4)))
_CpqFcaLogDrvCondition_Type.__name__=_D
_CpqFcaLogDrvCondition_Object=MibTableColumn
cpqFcaLogDrvCondition=_CpqFcaLogDrvCondition_Object((1,3,6,1,4,1,232,16,2,3,1,1,11),_CpqFcaLogDrvCondition_Type())
cpqFcaLogDrvCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaLogDrvCondition.setStatus(_A)
_CpqFcaLogDrvStripeSize_Type=Integer32
_CpqFcaLogDrvStripeSize_Object=MibTableColumn
cpqFcaLogDrvStripeSize=_CpqFcaLogDrvStripeSize_Object((1,3,6,1,4,1,232,16,2,3,1,1,12),_CpqFcaLogDrvStripeSize_Type())
cpqFcaLogDrvStripeSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaLogDrvStripeSize.setStatus(_A)
class _CpqFcaLogDrvOsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqFcaLogDrvOsName_Type.__name__=_F
_CpqFcaLogDrvOsName_Object=MibTableColumn
cpqFcaLogDrvOsName=_CpqFcaLogDrvOsName_Object((1,3,6,1,4,1,232,16,2,3,1,1,13),_CpqFcaLogDrvOsName_Type())
cpqFcaLogDrvOsName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaLogDrvOsName.setStatus(_A)
_CpqFcaLogDrvBlinkTime_Type=Counter32
_CpqFcaLogDrvBlinkTime_Object=MibTableColumn
cpqFcaLogDrvBlinkTime=_CpqFcaLogDrvBlinkTime_Object((1,3,6,1,4,1,232,16,2,3,1,1,14),_CpqFcaLogDrvBlinkTime_Type())
cpqFcaLogDrvBlinkTime.setMaxAccess(_i)
if mibBuilder.loadTexts:cpqFcaLogDrvBlinkTime.setStatus(_A)
class _CpqFcaLogDrvSpareReplaceMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CpqFcaLogDrvSpareReplaceMap_Type.__name__=_T
_CpqFcaLogDrvSpareReplaceMap_Object=MibTableColumn
cpqFcaLogDrvSpareReplaceMap=_CpqFcaLogDrvSpareReplaceMap_Object((1,3,6,1,4,1,232,16,2,3,1,1,15),_CpqFcaLogDrvSpareReplaceMap_Type())
cpqFcaLogDrvSpareReplaceMap.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaLogDrvSpareReplaceMap.setStatus(_A)
_CpqFcaLogDrvRebuildingPhyDrv_Type=Integer32
_CpqFcaLogDrvRebuildingPhyDrv_Object=MibTableColumn
cpqFcaLogDrvRebuildingPhyDrv=_CpqFcaLogDrvRebuildingPhyDrv_Object((1,3,6,1,4,1,232,16,2,3,1,1,16),_CpqFcaLogDrvRebuildingPhyDrv_Type())
cpqFcaLogDrvRebuildingPhyDrv.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaLogDrvRebuildingPhyDrv.setStatus(_A)
_CpqFcaLogDrvSnapshotResourceDrvIndex_Type=Integer32
_CpqFcaLogDrvSnapshotResourceDrvIndex_Object=MibTableColumn
cpqFcaLogDrvSnapshotResourceDrvIndex=_CpqFcaLogDrvSnapshotResourceDrvIndex_Object((1,3,6,1,4,1,232,16,2,3,1,1,17),_CpqFcaLogDrvSnapshotResourceDrvIndex_Type())
cpqFcaLogDrvSnapshotResourceDrvIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaLogDrvSnapshotResourceDrvIndex.setStatus(_A)
_CpqFcaLogDrvSnapshotSourceDrvIndex_Type=Integer32
_CpqFcaLogDrvSnapshotSourceDrvIndex_Object=MibTableColumn
cpqFcaLogDrvSnapshotSourceDrvIndex=_CpqFcaLogDrvSnapshotSourceDrvIndex_Object((1,3,6,1,4,1,232,16,2,3,1,1,18),_CpqFcaLogDrvSnapshotSourceDrvIndex_Type())
cpqFcaLogDrvSnapshotSourceDrvIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaLogDrvSnapshotSourceDrvIndex.setStatus(_A)
_CpqFcaLogDrvPreferredPath_Type=Integer32
_CpqFcaLogDrvPreferredPath_Object=MibTableColumn
cpqFcaLogDrvPreferredPath=_CpqFcaLogDrvPreferredPath_Object((1,3,6,1,4,1,232,16,2,3,1,1,19),_CpqFcaLogDrvPreferredPath_Type())
cpqFcaLogDrvPreferredPath.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaLogDrvPreferredPath.setStatus(_A)
_CpqFcaLogDrvCurrentPath_Type=Integer32
_CpqFcaLogDrvCurrentPath_Object=MibTableColumn
cpqFcaLogDrvCurrentPath=_CpqFcaLogDrvCurrentPath_Object((1,3,6,1,4,1,232,16,2,3,1,1,20),_CpqFcaLogDrvCurrentPath_Type())
cpqFcaLogDrvCurrentPath.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaLogDrvCurrentPath.setStatus(_A)
_CpqFcaSpareDrv_ObjectIdentity=ObjectIdentity
cpqFcaSpareDrv=_CpqFcaSpareDrv_ObjectIdentity((1,3,6,1,4,1,232,16,2,4))
_CpqFcaSpareTable_Object=MibTable
cpqFcaSpareTable=_CpqFcaSpareTable_Object((1,3,6,1,4,1,232,16,2,4,1))
if mibBuilder.loadTexts:cpqFcaSpareTable.setStatus(_A)
_CpqFcaSpareEntry_Object=MibTableRow
cpqFcaSpareEntry=_CpqFcaSpareEntry_Object((1,3,6,1,4,1,232,16,2,4,1,1))
cpqFcaSpareEntry.setIndexNames((0,_C,_AJ),(0,_C,_AK))
if mibBuilder.loadTexts:cpqFcaSpareEntry.setStatus(_A)
class _CpqFcaSpareBoxIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqFcaSpareBoxIndex_Type.__name__=_D
_CpqFcaSpareBoxIndex_Object=MibTableColumn
cpqFcaSpareBoxIndex=_CpqFcaSpareBoxIndex_Object((1,3,6,1,4,1,232,16,2,4,1,1,1),_CpqFcaSpareBoxIndex_Type())
cpqFcaSpareBoxIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaSpareBoxIndex.setStatus(_A)
class _CpqFcaSparePhyDrvIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqFcaSparePhyDrvIndex_Type.__name__=_D
_CpqFcaSparePhyDrvIndex_Object=MibTableColumn
cpqFcaSparePhyDrvIndex=_CpqFcaSparePhyDrvIndex_Object((1,3,6,1,4,1,232,16,2,4,1,1,2),_CpqFcaSparePhyDrvIndex_Type())
cpqFcaSparePhyDrvIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaSparePhyDrvIndex.setStatus(_A)
class _CpqFcaSpareStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('inactive',2),(_M,3),('building',4),(_j,5)))
_CpqFcaSpareStatus_Type.__name__=_D
_CpqFcaSpareStatus_Object=MibTableColumn
cpqFcaSpareStatus=_CpqFcaSpareStatus_Object((1,3,6,1,4,1,232,16,2,4,1,1,3),_CpqFcaSpareStatus_Type())
cpqFcaSpareStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaSpareStatus.setStatus(_A)
_CpqFcaSpareReplacedDrvBay_Type=Integer32
_CpqFcaSpareReplacedDrvBay_Object=MibTableColumn
cpqFcaSpareReplacedDrvBay=_CpqFcaSpareReplacedDrvBay_Object((1,3,6,1,4,1,232,16,2,4,1,1,4),_CpqFcaSpareReplacedDrvBay_Type())
cpqFcaSpareReplacedDrvBay.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaSpareReplacedDrvBay.setStatus(_A)
_CpqFcaSparePercentRebuild_Type=Gauge32
_CpqFcaSparePercentRebuild_Object=MibTableColumn
cpqFcaSparePercentRebuild=_CpqFcaSparePercentRebuild_Object((1,3,6,1,4,1,232,16,2,4,1,1,5),_CpqFcaSparePercentRebuild_Type())
cpqFcaSparePercentRebuild.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaSparePercentRebuild.setStatus(_A)
class _CpqFcaSpareCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_L,2),(_Q,3),(_M,4)))
_CpqFcaSpareCondition_Type.__name__=_D
_CpqFcaSpareCondition_Object=MibTableColumn
cpqFcaSpareCondition=_CpqFcaSpareCondition_Object((1,3,6,1,4,1,232,16,2,4,1,1,6),_CpqFcaSpareCondition_Type())
cpqFcaSpareCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaSpareCondition.setStatus(_A)
_CpqFcaSpareBusNumber_Type=Integer32
_CpqFcaSpareBusNumber_Object=MibTableColumn
cpqFcaSpareBusNumber=_CpqFcaSpareBusNumber_Object((1,3,6,1,4,1,232,16,2,4,1,1,7),_CpqFcaSpareBusNumber_Type())
cpqFcaSpareBusNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaSpareBusNumber.setStatus(_A)
class _CpqFcaSpareBay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqFcaSpareBay_Type.__name__=_D
_CpqFcaSpareBay_Object=MibTableColumn
cpqFcaSpareBay=_CpqFcaSpareBay_Object((1,3,6,1,4,1,232,16,2,4,1,1,8),_CpqFcaSpareBay_Type())
cpqFcaSpareBay.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaSpareBay.setStatus(_A)
_CpqFcaSpareReplacedDrvBusNumber_Type=Integer32
_CpqFcaSpareReplacedDrvBusNumber_Object=MibTableColumn
cpqFcaSpareReplacedDrvBusNumber=_CpqFcaSpareReplacedDrvBusNumber_Object((1,3,6,1,4,1,232,16,2,4,1,1,9),_CpqFcaSpareReplacedDrvBusNumber_Type())
cpqFcaSpareReplacedDrvBusNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaSpareReplacedDrvBusNumber.setStatus(_A)
class _CpqFcaSpareLocationString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqFcaSpareLocationString_Type.__name__=_F
_CpqFcaSpareLocationString_Object=MibTableColumn
cpqFcaSpareLocationString=_CpqFcaSpareLocationString_Object((1,3,6,1,4,1,232,16,2,4,1,1,10),_CpqFcaSpareLocationString_Type())
cpqFcaSpareLocationString.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaSpareLocationString.setStatus(_A)
_CpqFcaPhyDrv_ObjectIdentity=ObjectIdentity
cpqFcaPhyDrv=_CpqFcaPhyDrv_ObjectIdentity((1,3,6,1,4,1,232,16,2,5))
_CpqFcaPhyDrvTable_Object=MibTable
cpqFcaPhyDrvTable=_CpqFcaPhyDrvTable_Object((1,3,6,1,4,1,232,16,2,5,1))
if mibBuilder.loadTexts:cpqFcaPhyDrvTable.setStatus(_A)
_CpqFcaPhyDrvEntry_Object=MibTableRow
cpqFcaPhyDrvEntry=_CpqFcaPhyDrvEntry_Object((1,3,6,1,4,1,232,16,2,5,1,1))
cpqFcaPhyDrvEntry.setIndexNames((0,_C,_AL),(0,_C,_AM))
if mibBuilder.loadTexts:cpqFcaPhyDrvEntry.setStatus(_A)
class _CpqFcaPhyDrvBoxIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqFcaPhyDrvBoxIndex_Type.__name__=_D
_CpqFcaPhyDrvBoxIndex_Object=MibTableColumn
cpqFcaPhyDrvBoxIndex=_CpqFcaPhyDrvBoxIndex_Object((1,3,6,1,4,1,232,16,2,5,1,1,1),_CpqFcaPhyDrvBoxIndex_Type())
cpqFcaPhyDrvBoxIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvBoxIndex.setStatus(_A)
class _CpqFcaPhyDrvIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqFcaPhyDrvIndex_Type.__name__=_D
_CpqFcaPhyDrvIndex_Object=MibTableColumn
cpqFcaPhyDrvIndex=_CpqFcaPhyDrvIndex_Object((1,3,6,1,4,1,232,16,2,5,1,1,2),_CpqFcaPhyDrvIndex_Type())
cpqFcaPhyDrvIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvIndex.setStatus(_A)
class _CpqFcaPhyDrvModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,41))
_CpqFcaPhyDrvModel_Type.__name__=_F
_CpqFcaPhyDrvModel_Object=MibTableColumn
cpqFcaPhyDrvModel=_CpqFcaPhyDrvModel_Object((1,3,6,1,4,1,232,16,2,5,1,1,3),_CpqFcaPhyDrvModel_Type())
cpqFcaPhyDrvModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvModel.setStatus(_A)
class _CpqFcaPhyDrvFWRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqFcaPhyDrvFWRev_Type.__name__=_F
_CpqFcaPhyDrvFWRev_Object=MibTableColumn
cpqFcaPhyDrvFWRev=_CpqFcaPhyDrvFWRev_Object((1,3,6,1,4,1,232,16,2,5,1,1,4),_CpqFcaPhyDrvFWRev_Type())
cpqFcaPhyDrvFWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvFWRev.setStatus(_A)
class _CpqFcaPhyDrvBay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqFcaPhyDrvBay_Type.__name__=_D
_CpqFcaPhyDrvBay_Object=MibTableColumn
cpqFcaPhyDrvBay=_CpqFcaPhyDrvBay_Object((1,3,6,1,4,1,232,16,2,5,1,1,5),_CpqFcaPhyDrvBay_Type())
cpqFcaPhyDrvBay.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvBay.setStatus(_A)
class _CpqFcaPhyDrvStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),(_AH,2),(_L,3),('threshExceeded',4),('predictiveFailure',5),(_M,6),('unsupportedDrive',7)))
_CpqFcaPhyDrvStatus_Type.__name__=_D
_CpqFcaPhyDrvStatus_Object=MibTableColumn
cpqFcaPhyDrvStatus=_CpqFcaPhyDrvStatus_Object((1,3,6,1,4,1,232,16,2,5,1,1,6),_CpqFcaPhyDrvStatus_Type())
cpqFcaPhyDrvStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvStatus.setStatus(_A)
_CpqFcaPhyDrvUsedReallocs_Type=Counter32
_CpqFcaPhyDrvUsedReallocs_Object=MibTableColumn
cpqFcaPhyDrvUsedReallocs=_CpqFcaPhyDrvUsedReallocs_Object((1,3,6,1,4,1,232,16,2,5,1,1,7),_CpqFcaPhyDrvUsedReallocs_Type())
cpqFcaPhyDrvUsedReallocs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvUsedReallocs.setStatus(_A)
_CpqFcaPhyDrvRefHours_Type=Counter32
_CpqFcaPhyDrvRefHours_Object=MibTableColumn
cpqFcaPhyDrvRefHours=_CpqFcaPhyDrvRefHours_Object((1,3,6,1,4,1,232,16,2,5,1,1,8),_CpqFcaPhyDrvRefHours_Type())
cpqFcaPhyDrvRefHours.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvRefHours.setStatus(_A)
_CpqFcaPhyDrvHReads_Type=Counter32
_CpqFcaPhyDrvHReads_Object=MibTableColumn
cpqFcaPhyDrvHReads=_CpqFcaPhyDrvHReads_Object((1,3,6,1,4,1,232,16,2,5,1,1,9),_CpqFcaPhyDrvHReads_Type())
cpqFcaPhyDrvHReads.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvHReads.setStatus(_A)
_CpqFcaPhyDrvReads_Type=Counter32
_CpqFcaPhyDrvReads_Object=MibTableColumn
cpqFcaPhyDrvReads=_CpqFcaPhyDrvReads_Object((1,3,6,1,4,1,232,16,2,5,1,1,10),_CpqFcaPhyDrvReads_Type())
cpqFcaPhyDrvReads.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvReads.setStatus(_A)
_CpqFcaPhyDrvHWrites_Type=Counter32
_CpqFcaPhyDrvHWrites_Object=MibTableColumn
cpqFcaPhyDrvHWrites=_CpqFcaPhyDrvHWrites_Object((1,3,6,1,4,1,232,16,2,5,1,1,11),_CpqFcaPhyDrvHWrites_Type())
cpqFcaPhyDrvHWrites.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvHWrites.setStatus(_A)
_CpqFcaPhyDrvWrites_Type=Counter32
_CpqFcaPhyDrvWrites_Object=MibTableColumn
cpqFcaPhyDrvWrites=_CpqFcaPhyDrvWrites_Object((1,3,6,1,4,1,232,16,2,5,1,1,12),_CpqFcaPhyDrvWrites_Type())
cpqFcaPhyDrvWrites.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvWrites.setStatus(_A)
_CpqFcaPhyDrvHSeeks_Type=Counter32
_CpqFcaPhyDrvHSeeks_Object=MibTableColumn
cpqFcaPhyDrvHSeeks=_CpqFcaPhyDrvHSeeks_Object((1,3,6,1,4,1,232,16,2,5,1,1,13),_CpqFcaPhyDrvHSeeks_Type())
cpqFcaPhyDrvHSeeks.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvHSeeks.setStatus(_A)
_CpqFcaPhyDrvSeeks_Type=Counter32
_CpqFcaPhyDrvSeeks_Object=MibTableColumn
cpqFcaPhyDrvSeeks=_CpqFcaPhyDrvSeeks_Object((1,3,6,1,4,1,232,16,2,5,1,1,14),_CpqFcaPhyDrvSeeks_Type())
cpqFcaPhyDrvSeeks.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvSeeks.setStatus(_A)
_CpqFcaPhyDrvHardReadErrs_Type=Counter32
_CpqFcaPhyDrvHardReadErrs_Object=MibTableColumn
cpqFcaPhyDrvHardReadErrs=_CpqFcaPhyDrvHardReadErrs_Object((1,3,6,1,4,1,232,16,2,5,1,1,15),_CpqFcaPhyDrvHardReadErrs_Type())
cpqFcaPhyDrvHardReadErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvHardReadErrs.setStatus(_A)
_CpqFcaPhyDrvRecvReadErrs_Type=Counter32
_CpqFcaPhyDrvRecvReadErrs_Object=MibTableColumn
cpqFcaPhyDrvRecvReadErrs=_CpqFcaPhyDrvRecvReadErrs_Object((1,3,6,1,4,1,232,16,2,5,1,1,16),_CpqFcaPhyDrvRecvReadErrs_Type())
cpqFcaPhyDrvRecvReadErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvRecvReadErrs.setStatus(_A)
_CpqFcaPhyDrvHardWriteErrs_Type=Counter32
_CpqFcaPhyDrvHardWriteErrs_Object=MibTableColumn
cpqFcaPhyDrvHardWriteErrs=_CpqFcaPhyDrvHardWriteErrs_Object((1,3,6,1,4,1,232,16,2,5,1,1,17),_CpqFcaPhyDrvHardWriteErrs_Type())
cpqFcaPhyDrvHardWriteErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvHardWriteErrs.setStatus(_A)
_CpqFcaPhyDrvRecvWriteErrs_Type=Counter32
_CpqFcaPhyDrvRecvWriteErrs_Object=MibTableColumn
cpqFcaPhyDrvRecvWriteErrs=_CpqFcaPhyDrvRecvWriteErrs_Object((1,3,6,1,4,1,232,16,2,5,1,1,18),_CpqFcaPhyDrvRecvWriteErrs_Type())
cpqFcaPhyDrvRecvWriteErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvRecvWriteErrs.setStatus(_A)
_CpqFcaPhyDrvHSeekErrs_Type=Counter32
_CpqFcaPhyDrvHSeekErrs_Object=MibTableColumn
cpqFcaPhyDrvHSeekErrs=_CpqFcaPhyDrvHSeekErrs_Object((1,3,6,1,4,1,232,16,2,5,1,1,19),_CpqFcaPhyDrvHSeekErrs_Type())
cpqFcaPhyDrvHSeekErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvHSeekErrs.setStatus(_A)
_CpqFcaPhyDrvSeekErrs_Type=Counter32
_CpqFcaPhyDrvSeekErrs_Object=MibTableColumn
cpqFcaPhyDrvSeekErrs=_CpqFcaPhyDrvSeekErrs_Object((1,3,6,1,4,1,232,16,2,5,1,1,20),_CpqFcaPhyDrvSeekErrs_Type())
cpqFcaPhyDrvSeekErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvSeekErrs.setStatus(_A)
_CpqFcaPhyDrvSpinupTime_Type=Integer32
_CpqFcaPhyDrvSpinupTime_Object=MibTableColumn
cpqFcaPhyDrvSpinupTime=_CpqFcaPhyDrvSpinupTime_Object((1,3,6,1,4,1,232,16,2,5,1,1,21),_CpqFcaPhyDrvSpinupTime_Type())
cpqFcaPhyDrvSpinupTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvSpinupTime.setStatus(_A)
_CpqFcaPhyDrvFunctTest1_Type=Gauge32
_CpqFcaPhyDrvFunctTest1_Object=MibTableColumn
cpqFcaPhyDrvFunctTest1=_CpqFcaPhyDrvFunctTest1_Object((1,3,6,1,4,1,232,16,2,5,1,1,22),_CpqFcaPhyDrvFunctTest1_Type())
cpqFcaPhyDrvFunctTest1.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvFunctTest1.setStatus(_P)
_CpqFcaPhyDrvFunctTest2_Type=Gauge32
_CpqFcaPhyDrvFunctTest2_Object=MibTableColumn
cpqFcaPhyDrvFunctTest2=_CpqFcaPhyDrvFunctTest2_Object((1,3,6,1,4,1,232,16,2,5,1,1,23),_CpqFcaPhyDrvFunctTest2_Type())
cpqFcaPhyDrvFunctTest2.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvFunctTest2.setStatus(_P)
_CpqFcaPhyDrvFunctTest3_Type=Gauge32
_CpqFcaPhyDrvFunctTest3_Object=MibTableColumn
cpqFcaPhyDrvFunctTest3=_CpqFcaPhyDrvFunctTest3_Object((1,3,6,1,4,1,232,16,2,5,1,1,24),_CpqFcaPhyDrvFunctTest3_Type())
cpqFcaPhyDrvFunctTest3.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvFunctTest3.setStatus(_P)
_CpqFcaPhyDrvOtherTimeouts_Type=Counter32
_CpqFcaPhyDrvOtherTimeouts_Object=MibTableColumn
cpqFcaPhyDrvOtherTimeouts=_CpqFcaPhyDrvOtherTimeouts_Object((1,3,6,1,4,1,232,16,2,5,1,1,25),_CpqFcaPhyDrvOtherTimeouts_Type())
cpqFcaPhyDrvOtherTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvOtherTimeouts.setStatus(_A)
_CpqFcaPhyDrvBadRecvReads_Type=Counter32
_CpqFcaPhyDrvBadRecvReads_Object=MibTableColumn
cpqFcaPhyDrvBadRecvReads=_CpqFcaPhyDrvBadRecvReads_Object((1,3,6,1,4,1,232,16,2,5,1,1,26),_CpqFcaPhyDrvBadRecvReads_Type())
cpqFcaPhyDrvBadRecvReads.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvBadRecvReads.setStatus(_A)
_CpqFcaPhyDrvBadRecvWrites_Type=Counter32
_CpqFcaPhyDrvBadRecvWrites_Object=MibTableColumn
cpqFcaPhyDrvBadRecvWrites=_CpqFcaPhyDrvBadRecvWrites_Object((1,3,6,1,4,1,232,16,2,5,1,1,27),_CpqFcaPhyDrvBadRecvWrites_Type())
cpqFcaPhyDrvBadRecvWrites.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvBadRecvWrites.setStatus(_A)
_CpqFcaPhyDrvFormatErrs_Type=Counter32
_CpqFcaPhyDrvFormatErrs_Object=MibTableColumn
cpqFcaPhyDrvFormatErrs=_CpqFcaPhyDrvFormatErrs_Object((1,3,6,1,4,1,232,16,2,5,1,1,28),_CpqFcaPhyDrvFormatErrs_Type())
cpqFcaPhyDrvFormatErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvFormatErrs.setStatus(_A)
_CpqFcaPhyDrvNotReadyErrs_Type=Counter32
_CpqFcaPhyDrvNotReadyErrs_Object=MibTableColumn
cpqFcaPhyDrvNotReadyErrs=_CpqFcaPhyDrvNotReadyErrs_Object((1,3,6,1,4,1,232,16,2,5,1,1,29),_CpqFcaPhyDrvNotReadyErrs_Type())
cpqFcaPhyDrvNotReadyErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvNotReadyErrs.setStatus(_A)
class _CpqFcaPhyDrvHasMonInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_CpqFcaPhyDrvHasMonInfo_Type.__name__=_D
_CpqFcaPhyDrvHasMonInfo_Object=MibTableColumn
cpqFcaPhyDrvHasMonInfo=_CpqFcaPhyDrvHasMonInfo_Object((1,3,6,1,4,1,232,16,2,5,1,1,30),_CpqFcaPhyDrvHasMonInfo_Type())
cpqFcaPhyDrvHasMonInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvHasMonInfo.setStatus(_A)
class _CpqFcaPhyDrvCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_L,2),(_Q,3),(_M,4)))
_CpqFcaPhyDrvCondition_Type.__name__=_D
_CpqFcaPhyDrvCondition_Object=MibTableColumn
cpqFcaPhyDrvCondition=_CpqFcaPhyDrvCondition_Object((1,3,6,1,4,1,232,16,2,5,1,1,31),_CpqFcaPhyDrvCondition_Type())
cpqFcaPhyDrvCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvCondition.setStatus(_A)
_CpqFcaPhyDrvHotPlugs_Type=Counter32
_CpqFcaPhyDrvHotPlugs_Object=MibTableColumn
cpqFcaPhyDrvHotPlugs=_CpqFcaPhyDrvHotPlugs_Object((1,3,6,1,4,1,232,16,2,5,1,1,32),_CpqFcaPhyDrvHotPlugs_Type())
cpqFcaPhyDrvHotPlugs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvHotPlugs.setStatus(_A)
_CpqFcaPhyDrvMediaErrs_Type=Counter32
_CpqFcaPhyDrvMediaErrs_Object=MibTableColumn
cpqFcaPhyDrvMediaErrs=_CpqFcaPhyDrvMediaErrs_Object((1,3,6,1,4,1,232,16,2,5,1,1,33),_CpqFcaPhyDrvMediaErrs_Type())
cpqFcaPhyDrvMediaErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvMediaErrs.setStatus(_A)
_CpqFcaPhyDrvHardwareErrs_Type=Counter32
_CpqFcaPhyDrvHardwareErrs_Object=MibTableColumn
cpqFcaPhyDrvHardwareErrs=_CpqFcaPhyDrvHardwareErrs_Object((1,3,6,1,4,1,232,16,2,5,1,1,34),_CpqFcaPhyDrvHardwareErrs_Type())
cpqFcaPhyDrvHardwareErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvHardwareErrs.setStatus(_A)
_CpqFcaPhyDrvAbortedCmds_Type=Counter32
_CpqFcaPhyDrvAbortedCmds_Object=MibTableColumn
cpqFcaPhyDrvAbortedCmds=_CpqFcaPhyDrvAbortedCmds_Object((1,3,6,1,4,1,232,16,2,5,1,1,35),_CpqFcaPhyDrvAbortedCmds_Type())
cpqFcaPhyDrvAbortedCmds.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvAbortedCmds.setStatus(_A)
_CpqFcaPhyDrvSpinUpErrs_Type=Counter32
_CpqFcaPhyDrvSpinUpErrs_Object=MibTableColumn
cpqFcaPhyDrvSpinUpErrs=_CpqFcaPhyDrvSpinUpErrs_Object((1,3,6,1,4,1,232,16,2,5,1,1,36),_CpqFcaPhyDrvSpinUpErrs_Type())
cpqFcaPhyDrvSpinUpErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvSpinUpErrs.setStatus(_A)
_CpqFcaPhyDrvBadTargetErrs_Type=Counter32
_CpqFcaPhyDrvBadTargetErrs_Object=MibTableColumn
cpqFcaPhyDrvBadTargetErrs=_CpqFcaPhyDrvBadTargetErrs_Object((1,3,6,1,4,1,232,16,2,5,1,1,37),_CpqFcaPhyDrvBadTargetErrs_Type())
cpqFcaPhyDrvBadTargetErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvBadTargetErrs.setStatus(_A)
_CpqFcaPhyDrvSize_Type=Integer32
_CpqFcaPhyDrvSize_Object=MibTableColumn
cpqFcaPhyDrvSize=_CpqFcaPhyDrvSize_Object((1,3,6,1,4,1,232,16,2,5,1,1,38),_CpqFcaPhyDrvSize_Type())
cpqFcaPhyDrvSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvSize.setStatus(_A)
_CpqFcaPhyDrvBusFaults_Type=Counter32
_CpqFcaPhyDrvBusFaults_Object=MibTableColumn
cpqFcaPhyDrvBusFaults=_CpqFcaPhyDrvBusFaults_Object((1,3,6,1,4,1,232,16,2,5,1,1,39),_CpqFcaPhyDrvBusFaults_Type())
cpqFcaPhyDrvBusFaults.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvBusFaults.setStatus(_A)
class _CpqFcaPhyDrvHotPlug_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('hotPlug',2),(_AN,3)))
_CpqFcaPhyDrvHotPlug_Type.__name__=_D
_CpqFcaPhyDrvHotPlug_Object=MibTableColumn
cpqFcaPhyDrvHotPlug=_CpqFcaPhyDrvHotPlug_Object((1,3,6,1,4,1,232,16,2,5,1,1,40),_CpqFcaPhyDrvHotPlug_Type())
cpqFcaPhyDrvHotPlug.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvHotPlug.setStatus(_A)
class _CpqFcaPhyDrvPlacement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('internal',2),('external',3)))
_CpqFcaPhyDrvPlacement_Type.__name__=_D
_CpqFcaPhyDrvPlacement_Object=MibTableColumn
cpqFcaPhyDrvPlacement=_CpqFcaPhyDrvPlacement_Object((1,3,6,1,4,1,232,16,2,5,1,1,41),_CpqFcaPhyDrvPlacement_Type())
cpqFcaPhyDrvPlacement.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvPlacement.setStatus(_A)
_CpqFcaPhyDrvBusNumber_Type=Integer32
_CpqFcaPhyDrvBusNumber_Object=MibTableColumn
cpqFcaPhyDrvBusNumber=_CpqFcaPhyDrvBusNumber_Object((1,3,6,1,4,1,232,16,2,5,1,1,42),_CpqFcaPhyDrvBusNumber_Type())
cpqFcaPhyDrvBusNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvBusNumber.setStatus(_A)
class _CpqFcaPhyDrvSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_CpqFcaPhyDrvSerialNum_Type.__name__=_F
_CpqFcaPhyDrvSerialNum_Object=MibTableColumn
cpqFcaPhyDrvSerialNum=_CpqFcaPhyDrvSerialNum_Object((1,3,6,1,4,1,232,16,2,5,1,1,43),_CpqFcaPhyDrvSerialNum_Type())
cpqFcaPhyDrvSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvSerialNum.setStatus(_A)
class _CpqFcaPhyDrvPreFailMonitoring_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_AI,2),('available',3)))
_CpqFcaPhyDrvPreFailMonitoring_Type.__name__=_D
_CpqFcaPhyDrvPreFailMonitoring_Object=MibTableColumn
cpqFcaPhyDrvPreFailMonitoring=_CpqFcaPhyDrvPreFailMonitoring_Object((1,3,6,1,4,1,232,16,2,5,1,1,44),_CpqFcaPhyDrvPreFailMonitoring_Type())
cpqFcaPhyDrvPreFailMonitoring.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvPreFailMonitoring.setStatus(_A)
class _CpqFcaPhyDrvCurrentWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('narrow',2),('wide16',3)))
_CpqFcaPhyDrvCurrentWidth_Type.__name__=_D
_CpqFcaPhyDrvCurrentWidth_Object=MibTableColumn
cpqFcaPhyDrvCurrentWidth=_CpqFcaPhyDrvCurrentWidth_Object((1,3,6,1,4,1,232,16,2,5,1,1,45),_CpqFcaPhyDrvCurrentWidth_Type())
cpqFcaPhyDrvCurrentWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvCurrentWidth.setStatus(_A)
class _CpqFcaPhyDrvCurrentSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),(_AO,2),('fast',3),('ultra',4),('ultra2',5),('ultra3',6),('ultra320',7)))
_CpqFcaPhyDrvCurrentSpeed_Type.__name__=_D
_CpqFcaPhyDrvCurrentSpeed_Object=MibTableColumn
cpqFcaPhyDrvCurrentSpeed=_CpqFcaPhyDrvCurrentSpeed_Object((1,3,6,1,4,1,232,16,2,5,1,1,46),_CpqFcaPhyDrvCurrentSpeed_Type())
cpqFcaPhyDrvCurrentSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvCurrentSpeed.setStatus(_A)
_CpqFcaPhyDrvFailureCode_Type=Integer32
_CpqFcaPhyDrvFailureCode_Object=MibTableColumn
cpqFcaPhyDrvFailureCode=_CpqFcaPhyDrvFailureCode_Object((1,3,6,1,4,1,232,16,2,5,1,1,47),_CpqFcaPhyDrvFailureCode_Type())
cpqFcaPhyDrvFailureCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvFailureCode.setStatus(_A)
_CpqFcaPhyDrvBlinkTime_Type=Counter32
_CpqFcaPhyDrvBlinkTime_Object=MibTableColumn
cpqFcaPhyDrvBlinkTime=_CpqFcaPhyDrvBlinkTime_Object((1,3,6,1,4,1,232,16,2,5,1,1,48),_CpqFcaPhyDrvBlinkTime_Type())
cpqFcaPhyDrvBlinkTime.setMaxAccess(_i)
if mibBuilder.loadTexts:cpqFcaPhyDrvBlinkTime.setStatus(_A)
class _CpqFcaPhyDrvSmartStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),('replaceDrive',3)))
_CpqFcaPhyDrvSmartStatus_Type.__name__=_D
_CpqFcaPhyDrvSmartStatus_Object=MibTableColumn
cpqFcaPhyDrvSmartStatus=_CpqFcaPhyDrvSmartStatus_Object((1,3,6,1,4,1,232,16,2,5,1,1,49),_CpqFcaPhyDrvSmartStatus_Type())
cpqFcaPhyDrvSmartStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvSmartStatus.setStatus(_A)
class _CpqFcaPhyDrvRotationalSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('rpm7200',2),('rpm10K',3),('rpm15K',4)))
_CpqFcaPhyDrvRotationalSpeed_Type.__name__=_D
_CpqFcaPhyDrvRotationalSpeed_Object=MibTableColumn
cpqFcaPhyDrvRotationalSpeed=_CpqFcaPhyDrvRotationalSpeed_Object((1,3,6,1,4,1,232,16,2,5,1,1,50),_CpqFcaPhyDrvRotationalSpeed_Type())
cpqFcaPhyDrvRotationalSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvRotationalSpeed.setStatus(_A)
class _CpqFcaPhyDrvType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('parallelScsi',2),('sata',3),('sas',4)))
_CpqFcaPhyDrvType_Type.__name__=_D
_CpqFcaPhyDrvType_Object=MibTableColumn
cpqFcaPhyDrvType=_CpqFcaPhyDrvType_Object((1,3,6,1,4,1,232,16,2,5,1,1,51),_CpqFcaPhyDrvType_Type())
cpqFcaPhyDrvType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvType.setStatus(_A)
class _CpqFcaPhyDrvSataVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('sataOne',2),('sataTwo',3)))
_CpqFcaPhyDrvSataVersion_Type.__name__=_D
_CpqFcaPhyDrvSataVersion_Object=MibTableColumn
cpqFcaPhyDrvSataVersion=_CpqFcaPhyDrvSataVersion_Object((1,3,6,1,4,1,232,16,2,5,1,1,52),_CpqFcaPhyDrvSataVersion_Type())
cpqFcaPhyDrvSataVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvSataVersion.setStatus(_A)
class _CpqFcaPhyDrvBoxConnector_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_CpqFcaPhyDrvBoxConnector_Type.__name__=_F
_CpqFcaPhyDrvBoxConnector_Object=MibTableColumn
cpqFcaPhyDrvBoxConnector=_CpqFcaPhyDrvBoxConnector_Object((1,3,6,1,4,1,232,16,2,5,1,1,53),_CpqFcaPhyDrvBoxConnector_Type())
cpqFcaPhyDrvBoxConnector.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvBoxConnector.setStatus(_A)
_CpqFcaPhyDrvBoxOnConnector_Type=Integer32
_CpqFcaPhyDrvBoxOnConnector_Object=MibTableColumn
cpqFcaPhyDrvBoxOnConnector=_CpqFcaPhyDrvBoxOnConnector_Object((1,3,6,1,4,1,232,16,2,5,1,1,54),_CpqFcaPhyDrvBoxOnConnector_Type())
cpqFcaPhyDrvBoxOnConnector.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvBoxOnConnector.setStatus(_A)
class _CpqFcaPhyDrvLocationString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqFcaPhyDrvLocationString_Type.__name__=_F
_CpqFcaPhyDrvLocationString_Object=MibTableColumn
cpqFcaPhyDrvLocationString=_CpqFcaPhyDrvLocationString_Object((1,3,6,1,4,1,232,16,2,5,1,1,55),_CpqFcaPhyDrvLocationString_Type())
cpqFcaPhyDrvLocationString.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvLocationString.setStatus(_A)
class _CpqFcaPhyDrvNegotiatedLinkRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('rate-1-5',2),('rate-3-0',3)))
_CpqFcaPhyDrvNegotiatedLinkRate_Type.__name__=_D
_CpqFcaPhyDrvNegotiatedLinkRate_Object=MibTableColumn
cpqFcaPhyDrvNegotiatedLinkRate=_CpqFcaPhyDrvNegotiatedLinkRate_Object((1,3,6,1,4,1,232,16,2,5,1,1,56),_CpqFcaPhyDrvNegotiatedLinkRate_Type())
cpqFcaPhyDrvNegotiatedLinkRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvNegotiatedLinkRate.setStatus(_A)
_CpqFcaPhyDrvPhyCount_Type=Integer32
_CpqFcaPhyDrvPhyCount_Object=MibTableColumn
cpqFcaPhyDrvPhyCount=_CpqFcaPhyDrvPhyCount_Object((1,3,6,1,4,1,232,16,2,5,1,1,57),_CpqFcaPhyDrvPhyCount_Type())
cpqFcaPhyDrvPhyCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvPhyCount.setStatus(_A)
class _CpqFcaPhyDrvUnsupportedDrive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('supported',2),('unsupported-SinglePorted',3),('unsupported-SATA',4),('unsupported-TooSmall',5)))
_CpqFcaPhyDrvUnsupportedDrive_Type.__name__=_D
_CpqFcaPhyDrvUnsupportedDrive_Object=MibTableColumn
cpqFcaPhyDrvUnsupportedDrive=_CpqFcaPhyDrvUnsupportedDrive_Object((1,3,6,1,4,1,232,16,2,5,1,1,58),_CpqFcaPhyDrvUnsupportedDrive_Type())
cpqFcaPhyDrvUnsupportedDrive.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvUnsupportedDrive.setStatus(_A)
_CpqFcaPhyDrvThr_ObjectIdentity=ObjectIdentity
cpqFcaPhyDrvThr=_CpqFcaPhyDrvThr_ObjectIdentity((1,3,6,1,4,1,232,16,2,6))
_CpqFcaPhyDrvThrTable_Object=MibTable
cpqFcaPhyDrvThrTable=_CpqFcaPhyDrvThrTable_Object((1,3,6,1,4,1,232,16,2,6,1))
if mibBuilder.loadTexts:cpqFcaPhyDrvThrTable.setStatus(_A)
_CpqFcaPhyDrvThrEntry_Object=MibTableRow
cpqFcaPhyDrvThrEntry=_CpqFcaPhyDrvThrEntry_Object((1,3,6,1,4,1,232,16,2,6,1,1))
cpqFcaPhyDrvThrEntry.setIndexNames((0,_C,_AP),(0,_C,_AQ))
if mibBuilder.loadTexts:cpqFcaPhyDrvThrEntry.setStatus(_A)
class _CpqFcaPhyDrvThrBoxIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqFcaPhyDrvThrBoxIndex_Type.__name__=_D
_CpqFcaPhyDrvThrBoxIndex_Object=MibTableColumn
cpqFcaPhyDrvThrBoxIndex=_CpqFcaPhyDrvThrBoxIndex_Object((1,3,6,1,4,1,232,16,2,6,1,1,1),_CpqFcaPhyDrvThrBoxIndex_Type())
cpqFcaPhyDrvThrBoxIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvThrBoxIndex.setStatus(_A)
class _CpqFcaPhyDrvThrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqFcaPhyDrvThrIndex_Type.__name__=_D
_CpqFcaPhyDrvThrIndex_Object=MibTableColumn
cpqFcaPhyDrvThrIndex=_CpqFcaPhyDrvThrIndex_Object((1,3,6,1,4,1,232,16,2,6,1,1,2),_CpqFcaPhyDrvThrIndex_Type())
cpqFcaPhyDrvThrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvThrIndex.setStatus(_A)
_CpqFcaPhyDrvThrUsedReallocs_Type=Integer32
_CpqFcaPhyDrvThrUsedReallocs_Object=MibTableColumn
cpqFcaPhyDrvThrUsedReallocs=_CpqFcaPhyDrvThrUsedReallocs_Object((1,3,6,1,4,1,232,16,2,6,1,1,3),_CpqFcaPhyDrvThrUsedReallocs_Type())
cpqFcaPhyDrvThrUsedReallocs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvThrUsedReallocs.setStatus(_A)
_CpqFcaPhyDrvThrSpinupTime_Type=Integer32
_CpqFcaPhyDrvThrSpinupTime_Object=MibTableColumn
cpqFcaPhyDrvThrSpinupTime=_CpqFcaPhyDrvThrSpinupTime_Object((1,3,6,1,4,1,232,16,2,6,1,1,4),_CpqFcaPhyDrvThrSpinupTime_Type())
cpqFcaPhyDrvThrSpinupTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvThrSpinupTime.setStatus(_A)
_CpqFcaPhyDrvThrFunctTest1_Type=Integer32
_CpqFcaPhyDrvThrFunctTest1_Object=MibTableColumn
cpqFcaPhyDrvThrFunctTest1=_CpqFcaPhyDrvThrFunctTest1_Object((1,3,6,1,4,1,232,16,2,6,1,1,5),_CpqFcaPhyDrvThrFunctTest1_Type())
cpqFcaPhyDrvThrFunctTest1.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvThrFunctTest1.setStatus(_P)
_CpqFcaPhyDrvThrFunctTest2_Type=Integer32
_CpqFcaPhyDrvThrFunctTest2_Object=MibTableColumn
cpqFcaPhyDrvThrFunctTest2=_CpqFcaPhyDrvThrFunctTest2_Object((1,3,6,1,4,1,232,16,2,6,1,1,6),_CpqFcaPhyDrvThrFunctTest2_Type())
cpqFcaPhyDrvThrFunctTest2.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvThrFunctTest2.setStatus(_P)
_CpqFcaPhyDrvThrFunctTest3_Type=Integer32
_CpqFcaPhyDrvThrFunctTest3_Object=MibTableColumn
cpqFcaPhyDrvThrFunctTest3=_CpqFcaPhyDrvThrFunctTest3_Object((1,3,6,1,4,1,232,16,2,6,1,1,7),_CpqFcaPhyDrvThrFunctTest3_Type())
cpqFcaPhyDrvThrFunctTest3.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvThrFunctTest3.setStatus(_P)
class _CpqFcaPhyDrvThrViUsedReallocs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),(_e,3)))
_CpqFcaPhyDrvThrViUsedReallocs_Type.__name__=_D
_CpqFcaPhyDrvThrViUsedReallocs_Object=MibTableColumn
cpqFcaPhyDrvThrViUsedReallocs=_CpqFcaPhyDrvThrViUsedReallocs_Object((1,3,6,1,4,1,232,16,2,6,1,1,8),_CpqFcaPhyDrvThrViUsedReallocs_Type())
cpqFcaPhyDrvThrViUsedReallocs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvThrViUsedReallocs.setStatus(_A)
class _CpqFcaPhyDrvThrViSpinupTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),(_e,3)))
_CpqFcaPhyDrvThrViSpinupTime_Type.__name__=_D
_CpqFcaPhyDrvThrViSpinupTime_Object=MibTableColumn
cpqFcaPhyDrvThrViSpinupTime=_CpqFcaPhyDrvThrViSpinupTime_Object((1,3,6,1,4,1,232,16,2,6,1,1,9),_CpqFcaPhyDrvThrViSpinupTime_Type())
cpqFcaPhyDrvThrViSpinupTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvThrViSpinupTime.setStatus(_A)
class _CpqFcaPhyDrvThrViFunctTest1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),(_e,3)))
_CpqFcaPhyDrvThrViFunctTest1_Type.__name__=_D
_CpqFcaPhyDrvThrViFunctTest1_Object=MibTableColumn
cpqFcaPhyDrvThrViFunctTest1=_CpqFcaPhyDrvThrViFunctTest1_Object((1,3,6,1,4,1,232,16,2,6,1,1,10),_CpqFcaPhyDrvThrViFunctTest1_Type())
cpqFcaPhyDrvThrViFunctTest1.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvThrViFunctTest1.setStatus(_A)
class _CpqFcaPhyDrvThrViFunctTest2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),(_e,3)))
_CpqFcaPhyDrvThrViFunctTest2_Type.__name__=_D
_CpqFcaPhyDrvThrViFunctTest2_Object=MibTableColumn
cpqFcaPhyDrvThrViFunctTest2=_CpqFcaPhyDrvThrViFunctTest2_Object((1,3,6,1,4,1,232,16,2,6,1,1,11),_CpqFcaPhyDrvThrViFunctTest2_Type())
cpqFcaPhyDrvThrViFunctTest2.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvThrViFunctTest2.setStatus(_A)
class _CpqFcaPhyDrvThrViFunctTest3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_S,2),(_e,3)))
_CpqFcaPhyDrvThrViFunctTest3_Type.__name__=_D
_CpqFcaPhyDrvThrViFunctTest3_Object=MibTableColumn
cpqFcaPhyDrvThrViFunctTest3=_CpqFcaPhyDrvThrViFunctTest3_Object((1,3,6,1,4,1,232,16,2,6,1,1,12),_CpqFcaPhyDrvThrViFunctTest3_Type())
cpqFcaPhyDrvThrViFunctTest3.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaPhyDrvThrViFunctTest3.setStatus(_A)
_CpqFcaHostCntlr_ObjectIdentity=ObjectIdentity
cpqFcaHostCntlr=_CpqFcaHostCntlr_ObjectIdentity((1,3,6,1,4,1,232,16,2,7))
_CpqFcaHostCntlrTable_Object=MibTable
cpqFcaHostCntlrTable=_CpqFcaHostCntlrTable_Object((1,3,6,1,4,1,232,16,2,7,1))
if mibBuilder.loadTexts:cpqFcaHostCntlrTable.setStatus(_A)
_CpqFcaHostCntlrEntry_Object=MibTableRow
cpqFcaHostCntlrEntry=_CpqFcaHostCntlrEntry_Object((1,3,6,1,4,1,232,16,2,7,1,1))
cpqFcaHostCntlrEntry.setIndexNames((0,_C,_v))
if mibBuilder.loadTexts:cpqFcaHostCntlrEntry.setStatus(_A)
_CpqFcaHostCntlrIndex_Type=Integer32
_CpqFcaHostCntlrIndex_Object=MibTableColumn
cpqFcaHostCntlrIndex=_CpqFcaHostCntlrIndex_Object((1,3,6,1,4,1,232,16,2,7,1,1,1),_CpqFcaHostCntlrIndex_Type())
cpqFcaHostCntlrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaHostCntlrIndex.setStatus(_A)
class _CpqFcaHostCntlrSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqFcaHostCntlrSlot_Type.__name__=_D
_CpqFcaHostCntlrSlot_Object=MibTableColumn
cpqFcaHostCntlrSlot=_CpqFcaHostCntlrSlot_Object((1,3,6,1,4,1,232,16,2,7,1,1,2),_CpqFcaHostCntlrSlot_Type())
cpqFcaHostCntlrSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaHostCntlrSlot.setStatus(_A)
class _CpqFcaHostCntlrModel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98)));namedValues=NamedValues(*((_E,1),('fchc-p',2),('fchc-e',3),('fchc64',4),('sa-sam',5),('fca-2101',6),('sw64-33',7),('fca-221x',8),('dpfcmc',9),('fca-2404',10),('fca-2214',11),('a7298a',12),('fca-2214dc',13),('a6826a',14),('fcmcG3',15),('fcmcG4',16),('ab46xa',17),('fc-generic',18),('fca-1143',19),('fca-1243',20),('fca-2143',21),('fca-2243',22),('fca-1050',23),('fca-lpe1105',24),('fca-qmh2462',25),('fca-1142sr',26),('fca-1242sr',27),('fca-2142sr',28),('fca-2242sr',29),('fcmc20pe',30),('fca-81q',31),('fca-82q',32),('fca-qmh2562',33),('fca-81e',34),('fca-82e',35),('fca-1205',36),('fca-sn1000esp',37),('fca-sn1000edp',38),('fca-sn1000qsp',39),('fca-sn1000qdp',40),('fca-sn1100esp',41),('fca-sn1100edp',42),('fca-81b',43),('fca-82b',44),('fca-cn1100e',45),('fca-554flb',46),('fca-554m',47),('fca-554flr',48),('fca-lpe1205a',49),('fca-cn1000q',50),('fca-qmh2572',51),('fca-526flr',52),('fca-qmh2672',53),('fca-534flb',54),('fca-534flr',55),('fca-534m',56),('fca-cn1100r',57),('fca-lpe1605',58),('fca-630flb',59),('fca-630m',60),('fca-556flr',61),('fca-650m',62),('fca-650flb',63),('fca-cn1200e',64),('fca-536flb',65),('fca-533flr-t',66),('fca-556flr-t',67),('fca-cn1100r-t',68),('fca-cn1200e-t',69),('fca-536flr-t',70),('fca-556flb',71),('fca-synergy2820c',72),('fca-synergy3520c',73),('fca-synergy3530c',74),('fca-synergy3820c',75),('fca-synergy3830c',76),('fca-84Q',77),('fca-sn1100Q-1P',78),('fca-sn1100Q-2P',79),('fca-84E',80),('fca-sn1100e',81),('fca-sn1600q-1p',82),('fca-sn1600q-2p',83),('fca-sn1600e-1p',84),('fca-sn1600e-2p',85),('fca-sn1200e-1p',86),('fca-sn1200e-2p',87),('fca-ql4820c-2p',88),('fca-cn1200rt-2p',89),('fca-cn1300r-2p',90),('fca-622flr-2p',91),('fca-5330c',92),('fca-5830c',93),('fca-6820c',94),('fca-sn1610e-1p',95),('fca-sn1610e-2p',96),('fca-sn1610q-1p',97),('fca-sn1610q-2p',98)))
_CpqFcaHostCntlrModel_Type.__name__=_D
_CpqFcaHostCntlrModel_Object=MibTableColumn
cpqFcaHostCntlrModel=_CpqFcaHostCntlrModel_Object((1,3,6,1,4,1,232,16,2,7,1,1,3),_CpqFcaHostCntlrModel_Type())
cpqFcaHostCntlrModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaHostCntlrModel.setStatus(_A)
class _CpqFcaHostCntlrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),(_L,2),(_M,3),('shutdown',4),('loopDegraded',5),('loopFailed',6),(_t,7)))
_CpqFcaHostCntlrStatus_Type.__name__=_D
_CpqFcaHostCntlrStatus_Object=MibTableColumn
cpqFcaHostCntlrStatus=_CpqFcaHostCntlrStatus_Object((1,3,6,1,4,1,232,16,2,7,1,1,4),_CpqFcaHostCntlrStatus_Type())
cpqFcaHostCntlrStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaHostCntlrStatus.setStatus(_A)
class _CpqFcaHostCntlrCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_L,2),(_Q,3),(_M,4)))
_CpqFcaHostCntlrCondition_Type.__name__=_D
_CpqFcaHostCntlrCondition_Object=MibTableColumn
cpqFcaHostCntlrCondition=_CpqFcaHostCntlrCondition_Object((1,3,6,1,4,1,232,16,2,7,1,1,5),_CpqFcaHostCntlrCondition_Type())
cpqFcaHostCntlrCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaHostCntlrCondition.setStatus(_A)
class _CpqFcaHostCntlrWorldWideName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CpqFcaHostCntlrWorldWideName_Type.__name__=_F
_CpqFcaHostCntlrWorldWideName_Object=MibTableColumn
cpqFcaHostCntlrWorldWideName=_CpqFcaHostCntlrWorldWideName_Object((1,3,6,1,4,1,232,16,2,7,1,1,6),_CpqFcaHostCntlrWorldWideName_Type())
cpqFcaHostCntlrWorldWideName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaHostCntlrWorldWideName.setStatus(_A)
_CpqFcaHostCntlrStorBoxList_Type=OctetString
_CpqFcaHostCntlrStorBoxList_Object=MibTableColumn
cpqFcaHostCntlrStorBoxList=_CpqFcaHostCntlrStorBoxList_Object((1,3,6,1,4,1,232,16,2,7,1,1,7),_CpqFcaHostCntlrStorBoxList_Type())
cpqFcaHostCntlrStorBoxList.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaHostCntlrStorBoxList.setStatus(_A)
class _CpqFcaHostCntlrOverallCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_L,2),(_Q,3),(_M,4)))
_CpqFcaHostCntlrOverallCondition_Type.__name__=_D
_CpqFcaHostCntlrOverallCondition_Object=MibTableColumn
cpqFcaHostCntlrOverallCondition=_CpqFcaHostCntlrOverallCondition_Object((1,3,6,1,4,1,232,16,2,7,1,1,8),_CpqFcaHostCntlrOverallCondition_Type())
cpqFcaHostCntlrOverallCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaHostCntlrOverallCondition.setStatus(_A)
_CpqFcaHostCntlrTapeCntlrList_Type=OctetString
_CpqFcaHostCntlrTapeCntlrList_Object=MibTableColumn
cpqFcaHostCntlrTapeCntlrList=_CpqFcaHostCntlrTapeCntlrList_Object((1,3,6,1,4,1,232,16,2,7,1,1,9),_CpqFcaHostCntlrTapeCntlrList_Type())
cpqFcaHostCntlrTapeCntlrList.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaHostCntlrTapeCntlrList.setStatus(_A)
class _CpqFcaHostCntlrSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CpqFcaHostCntlrSerialNumber_Type.__name__=_F
_CpqFcaHostCntlrSerialNumber_Object=MibTableColumn
cpqFcaHostCntlrSerialNumber=_CpqFcaHostCntlrSerialNumber_Object((1,3,6,1,4,1,232,16,2,7,1,1,10),_CpqFcaHostCntlrSerialNumber_Type())
cpqFcaHostCntlrSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaHostCntlrSerialNumber.setStatus(_A)
class _CpqFcaHostCntlrHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqFcaHostCntlrHwLocation_Type.__name__=_F
_CpqFcaHostCntlrHwLocation_Object=MibTableColumn
cpqFcaHostCntlrHwLocation=_CpqFcaHostCntlrHwLocation_Object((1,3,6,1,4,1,232,16,2,7,1,1,11),_CpqFcaHostCntlrHwLocation_Type())
cpqFcaHostCntlrHwLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaHostCntlrHwLocation.setStatus('optional')
class _CpqFcaHostCntlrWorldWidePortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CpqFcaHostCntlrWorldWidePortName_Type.__name__=_F
_CpqFcaHostCntlrWorldWidePortName_Object=MibTableColumn
cpqFcaHostCntlrWorldWidePortName=_CpqFcaHostCntlrWorldWidePortName_Object((1,3,6,1,4,1,232,16,2,7,1,1,12),_CpqFcaHostCntlrWorldWidePortName_Type())
cpqFcaHostCntlrWorldWidePortName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaHostCntlrWorldWidePortName.setStatus(_A)
_CpqFcaHostCntlrFirmwareVersion_Type=DisplayString
_CpqFcaHostCntlrFirmwareVersion_Object=MibTableColumn
cpqFcaHostCntlrFirmwareVersion=_CpqFcaHostCntlrFirmwareVersion_Object((1,3,6,1,4,1,232,16,2,7,1,1,13),_CpqFcaHostCntlrFirmwareVersion_Type())
cpqFcaHostCntlrFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaHostCntlrFirmwareVersion.setStatus(_A)
_CpqFcaHostCntlrOptionRomVersion_Type=DisplayString
_CpqFcaHostCntlrOptionRomVersion_Object=MibTableColumn
cpqFcaHostCntlrOptionRomVersion=_CpqFcaHostCntlrOptionRomVersion_Object((1,3,6,1,4,1,232,16,2,7,1,1,14),_CpqFcaHostCntlrOptionRomVersion_Type())
cpqFcaHostCntlrOptionRomVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaHostCntlrOptionRomVersion.setStatus(_A)
class _CpqFcaHostCntlrPciLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqFcaHostCntlrPciLocation_Type.__name__=_F
_CpqFcaHostCntlrPciLocation_Object=MibTableColumn
cpqFcaHostCntlrPciLocation=_CpqFcaHostCntlrPciLocation_Object((1,3,6,1,4,1,232,16,2,7,1,1,15),_CpqFcaHostCntlrPciLocation_Type())
cpqFcaHostCntlrPciLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcaHostCntlrPciLocation.setStatus('optional')
_CpqExtArrRsrcVol_ObjectIdentity=ObjectIdentity
cpqExtArrRsrcVol=_CpqExtArrRsrcVol_ObjectIdentity((1,3,6,1,4,1,232,16,2,8))
_CpqExtArrRsrcVolTable_Object=MibTable
cpqExtArrRsrcVolTable=_CpqExtArrRsrcVolTable_Object((1,3,6,1,4,1,232,16,2,8,1))
if mibBuilder.loadTexts:cpqExtArrRsrcVolTable.setStatus(_A)
_CpqExtArrRsrcVolEntry_Object=MibTableRow
cpqExtArrRsrcVolEntry=_CpqExtArrRsrcVolEntry_Object((1,3,6,1,4,1,232,16,2,8,1,1))
cpqExtArrRsrcVolEntry.setIndexNames((0,_C,_AR),(0,_C,_AS))
if mibBuilder.loadTexts:cpqExtArrRsrcVolEntry.setStatus(_A)
class _CpqExtArrRsrcVolBoxIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqExtArrRsrcVolBoxIndex_Type.__name__=_D
_CpqExtArrRsrcVolBoxIndex_Object=MibTableColumn
cpqExtArrRsrcVolBoxIndex=_CpqExtArrRsrcVolBoxIndex_Object((1,3,6,1,4,1,232,16,2,8,1,1,1),_CpqExtArrRsrcVolBoxIndex_Type())
cpqExtArrRsrcVolBoxIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqExtArrRsrcVolBoxIndex.setStatus(_A)
class _CpqExtArrRsrcVolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqExtArrRsrcVolIndex_Type.__name__=_D
_CpqExtArrRsrcVolIndex_Object=MibTableColumn
cpqExtArrRsrcVolIndex=_CpqExtArrRsrcVolIndex_Object((1,3,6,1,4,1,232,16,2,8,1,1,2),_CpqExtArrRsrcVolIndex_Type())
cpqExtArrRsrcVolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqExtArrRsrcVolIndex.setStatus(_A)
_CpqExtArrRsrcVolActiveInstances_Type=Integer32
_CpqExtArrRsrcVolActiveInstances_Object=MibTableColumn
cpqExtArrRsrcVolActiveInstances=_CpqExtArrRsrcVolActiveInstances_Object((1,3,6,1,4,1,232,16,2,8,1,1,3),_CpqExtArrRsrcVolActiveInstances_Type())
cpqExtArrRsrcVolActiveInstances.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqExtArrRsrcVolActiveInstances.setStatus(_A)
_CpqExtArrRsrcVolDisabledInstances_Type=Integer32
_CpqExtArrRsrcVolDisabledInstances_Object=MibTableColumn
cpqExtArrRsrcVolDisabledInstances=_CpqExtArrRsrcVolDisabledInstances_Object((1,3,6,1,4,1,232,16,2,8,1,1,4),_CpqExtArrRsrcVolDisabledInstances_Type())
cpqExtArrRsrcVolDisabledInstances.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqExtArrRsrcVolDisabledInstances.setStatus(_A)
class _CpqExtArrRsrcVolAllowCreation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('allowed',2),('notAllowed',3)))
_CpqExtArrRsrcVolAllowCreation_Type.__name__=_D
_CpqExtArrRsrcVolAllowCreation_Object=MibTableColumn
cpqExtArrRsrcVolAllowCreation=_CpqExtArrRsrcVolAllowCreation_Object((1,3,6,1,4,1,232,16,2,8,1,1,5),_CpqExtArrRsrcVolAllowCreation_Type())
cpqExtArrRsrcVolAllowCreation.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqExtArrRsrcVolAllowCreation.setStatus(_A)
class _CpqExtArrRsrcVolVolumeId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CpqExtArrRsrcVolVolumeId_Type.__name__=_F
_CpqExtArrRsrcVolVolumeId_Object=MibTableColumn
cpqExtArrRsrcVolVolumeId=_CpqExtArrRsrcVolVolumeId_Object((1,3,6,1,4,1,232,16,2,8,1,1,6),_CpqExtArrRsrcVolVolumeId_Type())
cpqExtArrRsrcVolVolumeId.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqExtArrRsrcVolVolumeId.setStatus(_A)
class _CpqExtArrRsrcVolSourceVolumeId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CpqExtArrRsrcVolSourceVolumeId_Type.__name__=_F
_CpqExtArrRsrcVolSourceVolumeId_Object=MibTableColumn
cpqExtArrRsrcVolSourceVolumeId=_CpqExtArrRsrcVolSourceVolumeId_Object((1,3,6,1,4,1,232,16,2,8,1,1,7),_CpqExtArrRsrcVolSourceVolumeId_Type())
cpqExtArrRsrcVolSourceVolumeId.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqExtArrRsrcVolSourceVolumeId.setStatus(_A)
_CpqExtArrRsrcVolTotalSpace_Type=Counter32
_CpqExtArrRsrcVolTotalSpace_Object=MibTableColumn
cpqExtArrRsrcVolTotalSpace=_CpqExtArrRsrcVolTotalSpace_Object((1,3,6,1,4,1,232,16,2,8,1,1,8),_CpqExtArrRsrcVolTotalSpace_Type())
cpqExtArrRsrcVolTotalSpace.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqExtArrRsrcVolTotalSpace.setStatus(_A)
_CpqExtArrRsrcVolFreeActiveSpace_Type=Counter32
_CpqExtArrRsrcVolFreeActiveSpace_Object=MibTableColumn
cpqExtArrRsrcVolFreeActiveSpace=_CpqExtArrRsrcVolFreeActiveSpace_Object((1,3,6,1,4,1,232,16,2,8,1,1,9),_CpqExtArrRsrcVolFreeActiveSpace_Type())
cpqExtArrRsrcVolFreeActiveSpace.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqExtArrRsrcVolFreeActiveSpace.setStatus(_A)
_CpqExtArrRsrcVolFreeNewSpace_Type=Counter32
_CpqExtArrRsrcVolFreeNewSpace_Object=MibTableColumn
cpqExtArrRsrcVolFreeNewSpace=_CpqExtArrRsrcVolFreeNewSpace_Object((1,3,6,1,4,1,232,16,2,8,1,1,10),_CpqExtArrRsrcVolFreeNewSpace_Type())
cpqExtArrRsrcVolFreeNewSpace.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqExtArrRsrcVolFreeNewSpace.setStatus(_A)
class _CpqExtArrRsrcVolStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_E,1),(_L,2),('unknownFailure',3),('resourceVolDisconnected',4),('sourceVolNotLocated',5),('resourceVolNotLocated',6),('sourceVolFailed',7),('resourceVolFailed',8),('sourceVolNotAvail',9),('resourceVolNotAvail',10),('resourceVolObsolete',11),('resourceVolObsoleteFailed',12)))
_CpqExtArrRsrcVolStatus_Type.__name__=_D
_CpqExtArrRsrcVolStatus_Object=MibTableColumn
cpqExtArrRsrcVolStatus=_CpqExtArrRsrcVolStatus_Object((1,3,6,1,4,1,232,16,2,8,1,1,11),_CpqExtArrRsrcVolStatus_Type())
cpqExtArrRsrcVolStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqExtArrRsrcVolStatus.setStatus(_A)
_CpqExtArrSnapshot_ObjectIdentity=ObjectIdentity
cpqExtArrSnapshot=_CpqExtArrSnapshot_ObjectIdentity((1,3,6,1,4,1,232,16,2,9))
_CpqExtArrSnapshotTable_Object=MibTable
cpqExtArrSnapshotTable=_CpqExtArrSnapshotTable_Object((1,3,6,1,4,1,232,16,2,9,1))
if mibBuilder.loadTexts:cpqExtArrSnapshotTable.setStatus(_A)
_CpqExtArrSnapshotEntry_Object=MibTableRow
cpqExtArrSnapshotEntry=_CpqExtArrSnapshotEntry_Object((1,3,6,1,4,1,232,16,2,9,1,1))
cpqExtArrSnapshotEntry.setIndexNames((0,_C,_AT),(0,_C,_AU),(0,_C,_AV))
if mibBuilder.loadTexts:cpqExtArrSnapshotEntry.setStatus(_A)
class _CpqExtArrSnapshotBoxIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqExtArrSnapshotBoxIndex_Type.__name__=_D
_CpqExtArrSnapshotBoxIndex_Object=MibTableColumn
cpqExtArrSnapshotBoxIndex=_CpqExtArrSnapshotBoxIndex_Object((1,3,6,1,4,1,232,16,2,9,1,1,1),_CpqExtArrSnapshotBoxIndex_Type())
cpqExtArrSnapshotBoxIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqExtArrSnapshotBoxIndex.setStatus(_A)
class _CpqExtArrSnapshotRsrcVolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqExtArrSnapshotRsrcVolIndex_Type.__name__=_D
_CpqExtArrSnapshotRsrcVolIndex_Object=MibTableColumn
cpqExtArrSnapshotRsrcVolIndex=_CpqExtArrSnapshotRsrcVolIndex_Object((1,3,6,1,4,1,232,16,2,9,1,1,2),_CpqExtArrSnapshotRsrcVolIndex_Type())
cpqExtArrSnapshotRsrcVolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqExtArrSnapshotRsrcVolIndex.setStatus(_A)
_CpqExtArrSnapshotIndex_Type=Integer32
_CpqExtArrSnapshotIndex_Object=MibTableColumn
cpqExtArrSnapshotIndex=_CpqExtArrSnapshotIndex_Object((1,3,6,1,4,1,232,16,2,9,1,1,3),_CpqExtArrSnapshotIndex_Type())
cpqExtArrSnapshotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqExtArrSnapshotIndex.setStatus(_A)
class _CpqExtArrSnapshotInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqExtArrSnapshotInstance_Type.__name__=_D
_CpqExtArrSnapshotInstance_Object=MibTableColumn
cpqExtArrSnapshotInstance=_CpqExtArrSnapshotInstance_Object((1,3,6,1,4,1,232,16,2,9,1,1,4),_CpqExtArrSnapshotInstance_Type())
cpqExtArrSnapshotInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqExtArrSnapshotInstance.setStatus(_A)
_CpqExtArrSnapshotUsedSpace_Type=Counter32
_CpqExtArrSnapshotUsedSpace_Object=MibTableColumn
cpqExtArrSnapshotUsedSpace=_CpqExtArrSnapshotUsedSpace_Object((1,3,6,1,4,1,232,16,2,9,1,1,5),_CpqExtArrSnapshotUsedSpace_Type())
cpqExtArrSnapshotUsedSpace.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqExtArrSnapshotUsedSpace.setStatus(_A)
class _CpqExtArrSnapshotDateTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqExtArrSnapshotDateTime_Type.__name__=_T
_CpqExtArrSnapshotDateTime_Object=MibTableColumn
cpqExtArrSnapshotDateTime=_CpqExtArrSnapshotDateTime_Object((1,3,6,1,4,1,232,16,2,9,1,1,6),_CpqExtArrSnapshotDateTime_Type())
cpqExtArrSnapshotDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqExtArrSnapshotDateTime.setStatus(_P)
class _CpqExtArrSnapshotType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),('cow',2)))
_CpqExtArrSnapshotType_Type.__name__=_D
_CpqExtArrSnapshotType_Object=MibTableColumn
cpqExtArrSnapshotType=_CpqExtArrSnapshotType_Object((1,3,6,1,4,1,232,16,2,9,1,1,7),_CpqExtArrSnapshotType_Type())
cpqExtArrSnapshotType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqExtArrSnapshotType.setStatus(_A)
class _CpqExtArrSnapshotMounted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('mounted',2),('notMounted',3)))
_CpqExtArrSnapshotMounted_Type.__name__=_D
_CpqExtArrSnapshotMounted_Object=MibTableColumn
cpqExtArrSnapshotMounted=_CpqExtArrSnapshotMounted_Object((1,3,6,1,4,1,232,16,2,9,1,1,8),_CpqExtArrSnapshotMounted_Type())
cpqExtArrSnapshotMounted.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqExtArrSnapshotMounted.setStatus(_A)
class _CpqExtArrSnapshotAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('readWrite',2),('readOnly',3)))
_CpqExtArrSnapshotAccess_Type.__name__=_D
_CpqExtArrSnapshotAccess_Object=MibTableColumn
cpqExtArrSnapshotAccess=_CpqExtArrSnapshotAccess_Object((1,3,6,1,4,1,232,16,2,9,1,1,9),_CpqExtArrSnapshotAccess_Type())
cpqExtArrSnapshotAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqExtArrSnapshotAccess.setStatus(_A)
_CpqFcTapeComponent_ObjectIdentity=ObjectIdentity
cpqFcTapeComponent=_CpqFcTapeComponent_ObjectIdentity((1,3,6,1,4,1,232,16,3))
_CpqFcTapeCntlr_ObjectIdentity=ObjectIdentity
cpqFcTapeCntlr=_CpqFcTapeCntlr_ObjectIdentity((1,3,6,1,4,1,232,16,3,1))
_CpqFcTapeCntlrTable_Object=MibTable
cpqFcTapeCntlrTable=_CpqFcTapeCntlrTable_Object((1,3,6,1,4,1,232,16,3,1,1))
if mibBuilder.loadTexts:cpqFcTapeCntlrTable.setStatus(_A)
_CpqFcTapeCntlrEntry_Object=MibTableRow
cpqFcTapeCntlrEntry=_CpqFcTapeCntlrEntry_Object((1,3,6,1,4,1,232,16,3,1,1,1))
cpqFcTapeCntlrEntry.setIndexNames((0,_C,_AW))
if mibBuilder.loadTexts:cpqFcTapeCntlrEntry.setStatus(_A)
class _CpqFcTapeCntlrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqFcTapeCntlrIndex_Type.__name__=_D
_CpqFcTapeCntlrIndex_Object=MibTableColumn
cpqFcTapeCntlrIndex=_CpqFcTapeCntlrIndex_Object((1,3,6,1,4,1,232,16,3,1,1,1,1),_CpqFcTapeCntlrIndex_Type())
cpqFcTapeCntlrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeCntlrIndex.setStatus(_A)
class _CpqFcTapeCntlrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),(_d,3)))
_CpqFcTapeCntlrStatus_Type.__name__=_D
_CpqFcTapeCntlrStatus_Object=MibTableColumn
cpqFcTapeCntlrStatus=_CpqFcTapeCntlrStatus_Object((1,3,6,1,4,1,232,16,3,1,1,1,2),_CpqFcTapeCntlrStatus_Type())
cpqFcTapeCntlrStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeCntlrStatus.setStatus(_A)
class _CpqFcTapeCntlrCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_L,2),(_Q,3),(_M,4)))
_CpqFcTapeCntlrCondition_Type.__name__=_D
_CpqFcTapeCntlrCondition_Object=MibTableColumn
cpqFcTapeCntlrCondition=_CpqFcTapeCntlrCondition_Object((1,3,6,1,4,1,232,16,3,1,1,1,3),_CpqFcTapeCntlrCondition_Type())
cpqFcTapeCntlrCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeCntlrCondition.setStatus(_A)
class _CpqFcTapeCntlrOverallCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_L,2),(_Q,3),(_M,4)))
_CpqFcTapeCntlrOverallCondition_Type.__name__=_D
_CpqFcTapeCntlrOverallCondition_Object=MibTableColumn
cpqFcTapeCntlrOverallCondition=_CpqFcTapeCntlrOverallCondition_Object((1,3,6,1,4,1,232,16,3,1,1,1,4),_CpqFcTapeCntlrOverallCondition_Type())
cpqFcTapeCntlrOverallCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeCntlrOverallCondition.setStatus(_A)
class _CpqFcTapeCntlrWWN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CpqFcTapeCntlrWWN_Type.__name__=_F
_CpqFcTapeCntlrWWN_Object=MibTableColumn
cpqFcTapeCntlrWWN=_CpqFcTapeCntlrWWN_Object((1,3,6,1,4,1,232,16,3,1,1,1,5),_CpqFcTapeCntlrWWN_Type())
cpqFcTapeCntlrWWN.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeCntlrWWN.setStatus(_A)
class _CpqFcTapeCntlrFWRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqFcTapeCntlrFWRev_Type.__name__=_F
_CpqFcTapeCntlrFWRev_Object=MibTableColumn
cpqFcTapeCntlrFWRev=_CpqFcTapeCntlrFWRev_Object((1,3,6,1,4,1,232,16,3,1,1,1,6),_CpqFcTapeCntlrFWRev_Type())
cpqFcTapeCntlrFWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeCntlrFWRev.setStatus(_A)
class _CpqFcTapeCntlrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('fiberTape',2),('modularDataRouter',3),('extended',4)))
_CpqFcTapeCntlrType_Type.__name__=_D
_CpqFcTapeCntlrType_Object=MibTableColumn
cpqFcTapeCntlrType=_CpqFcTapeCntlrType_Object((1,3,6,1,4,1,232,16,3,1,1,1,7),_CpqFcTapeCntlrType_Type())
cpqFcTapeCntlrType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeCntlrType.setStatus(_A)
class _CpqFcTapeCntlrModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CpqFcTapeCntlrModel_Type.__name__=_F
_CpqFcTapeCntlrModel_Object=MibTableColumn
cpqFcTapeCntlrModel=_CpqFcTapeCntlrModel_Object((1,3,6,1,4,1,232,16,3,1,1,1,8),_CpqFcTapeCntlrModel_Type())
cpqFcTapeCntlrModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeCntlrModel.setStatus(_A)
class _CpqFcTapeCntlrSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqFcTapeCntlrSerialNumber_Type.__name__=_F
_CpqFcTapeCntlrSerialNumber_Object=MibTableColumn
cpqFcTapeCntlrSerialNumber=_CpqFcTapeCntlrSerialNumber_Object((1,3,6,1,4,1,232,16,3,1,1,1,9),_CpqFcTapeCntlrSerialNumber_Type())
cpqFcTapeCntlrSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeCntlrSerialNumber.setStatus(_A)
_CpqFcTapeLibrary_ObjectIdentity=ObjectIdentity
cpqFcTapeLibrary=_CpqFcTapeLibrary_ObjectIdentity((1,3,6,1,4,1,232,16,3,2))
_CpqFcTapeLibraryTable_Object=MibTable
cpqFcTapeLibraryTable=_CpqFcTapeLibraryTable_Object((1,3,6,1,4,1,232,16,3,2,1))
if mibBuilder.loadTexts:cpqFcTapeLibraryTable.setStatus(_A)
_CpqFcTapeLibraryEntry_Object=MibTableRow
cpqFcTapeLibraryEntry=_CpqFcTapeLibraryEntry_Object((1,3,6,1,4,1,232,16,3,2,1,1))
cpqFcTapeLibraryEntry.setIndexNames((0,_C,_l),(0,_C,_Z),(0,_C,_a),(0,_C,_b))
if mibBuilder.loadTexts:cpqFcTapeLibraryEntry.setStatus(_A)
class _CpqFcTapeLibraryCntlrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqFcTapeLibraryCntlrIndex_Type.__name__=_D
_CpqFcTapeLibraryCntlrIndex_Object=MibTableColumn
cpqFcTapeLibraryCntlrIndex=_CpqFcTapeLibraryCntlrIndex_Object((1,3,6,1,4,1,232,16,3,2,1,1,1),_CpqFcTapeLibraryCntlrIndex_Type())
cpqFcTapeLibraryCntlrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeLibraryCntlrIndex.setStatus(_A)
class _CpqFcTapeLibraryScsiBus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqFcTapeLibraryScsiBus_Type.__name__=_D
_CpqFcTapeLibraryScsiBus_Object=MibTableColumn
cpqFcTapeLibraryScsiBus=_CpqFcTapeLibraryScsiBus_Object((1,3,6,1,4,1,232,16,3,2,1,1,2),_CpqFcTapeLibraryScsiBus_Type())
cpqFcTapeLibraryScsiBus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeLibraryScsiBus.setStatus(_A)
class _CpqFcTapeLibraryScsiTarget_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqFcTapeLibraryScsiTarget_Type.__name__=_D
_CpqFcTapeLibraryScsiTarget_Object=MibTableColumn
cpqFcTapeLibraryScsiTarget=_CpqFcTapeLibraryScsiTarget_Object((1,3,6,1,4,1,232,16,3,2,1,1,3),_CpqFcTapeLibraryScsiTarget_Type())
cpqFcTapeLibraryScsiTarget.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeLibraryScsiTarget.setStatus(_A)
class _CpqFcTapeLibraryScsiLun_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqFcTapeLibraryScsiLun_Type.__name__=_D
_CpqFcTapeLibraryScsiLun_Object=MibTableColumn
cpqFcTapeLibraryScsiLun=_CpqFcTapeLibraryScsiLun_Object((1,3,6,1,4,1,232,16,3,2,1,1,4),_CpqFcTapeLibraryScsiLun_Type())
cpqFcTapeLibraryScsiLun.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeLibraryScsiLun.setStatus(_A)
class _CpqFcTapeLibrarySerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqFcTapeLibrarySerialNumber_Type.__name__=_F
_CpqFcTapeLibrarySerialNumber_Object=MibTableColumn
cpqFcTapeLibrarySerialNumber=_CpqFcTapeLibrarySerialNumber_Object((1,3,6,1,4,1,232,16,3,2,1,1,5),_CpqFcTapeLibrarySerialNumber_Type())
cpqFcTapeLibrarySerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeLibrarySerialNumber.setStatus(_A)
class _CpqFcTapeLibraryModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CpqFcTapeLibraryModel_Type.__name__=_F
_CpqFcTapeLibraryModel_Object=MibTableColumn
cpqFcTapeLibraryModel=_CpqFcTapeLibraryModel_Object((1,3,6,1,4,1,232,16,3,2,1,1,6),_CpqFcTapeLibraryModel_Type())
cpqFcTapeLibraryModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeLibraryModel.setStatus(_A)
class _CpqFcTapeLibraryFWRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqFcTapeLibraryFWRev_Type.__name__=_F
_CpqFcTapeLibraryFWRev_Object=MibTableColumn
cpqFcTapeLibraryFWRev=_CpqFcTapeLibraryFWRev_Object((1,3,6,1,4,1,232,16,3,2,1,1,7),_CpqFcTapeLibraryFWRev_Type())
cpqFcTapeLibraryFWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeLibraryFWRev.setStatus(_A)
class _CpqFcTapeLibraryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_L,2),(_Q,3),(_M,4),(_d,5)))
_CpqFcTapeLibraryStatus_Type.__name__=_D
_CpqFcTapeLibraryStatus_Object=MibTableColumn
cpqFcTapeLibraryStatus=_CpqFcTapeLibraryStatus_Object((1,3,6,1,4,1,232,16,3,2,1,1,8),_CpqFcTapeLibraryStatus_Type())
cpqFcTapeLibraryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeLibraryStatus.setStatus(_A)
class _CpqFcTapeLibraryDoorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_m,2),('closed',3),('open',4)))
_CpqFcTapeLibraryDoorStatus_Type.__name__=_D
_CpqFcTapeLibraryDoorStatus_Object=MibTableColumn
cpqFcTapeLibraryDoorStatus=_CpqFcTapeLibraryDoorStatus_Object((1,3,6,1,4,1,232,16,3,2,1,1,9),_CpqFcTapeLibraryDoorStatus_Type())
cpqFcTapeLibraryDoorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeLibraryDoorStatus.setStatus(_A)
_CpqFcTapeLibraryCondition_Type=Integer32
_CpqFcTapeLibraryCondition_Object=MibTableColumn
cpqFcTapeLibraryCondition=_CpqFcTapeLibraryCondition_Object((1,3,6,1,4,1,232,16,3,2,1,1,10),_CpqFcTapeLibraryCondition_Type())
cpqFcTapeLibraryCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeLibraryCondition.setStatus(_A)
_CpqFcTapeLibraryOverallCondition_Type=Integer32
_CpqFcTapeLibraryOverallCondition_Object=MibTableColumn
cpqFcTapeLibraryOverallCondition=_CpqFcTapeLibraryOverallCondition_Object((1,3,6,1,4,1,232,16,3,2,1,1,11),_CpqFcTapeLibraryOverallCondition_Type())
cpqFcTapeLibraryOverallCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeLibraryOverallCondition.setStatus(_A)
class _CpqFcTapeLibraryLastError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqFcTapeLibraryLastError_Type.__name__=_D
_CpqFcTapeLibraryLastError_Object=MibTableColumn
cpqFcTapeLibraryLastError=_CpqFcTapeLibraryLastError_Object((1,3,6,1,4,1,232,16,3,2,1,1,12),_CpqFcTapeLibraryLastError_Type())
cpqFcTapeLibraryLastError.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeLibraryLastError.setStatus(_A)
_CpqFcTapeLibraryStatHours_Type=Counter32
_CpqFcTapeLibraryStatHours_Object=MibTableColumn
cpqFcTapeLibraryStatHours=_CpqFcTapeLibraryStatHours_Object((1,3,6,1,4,1,232,16,3,2,1,1,13),_CpqFcTapeLibraryStatHours_Type())
cpqFcTapeLibraryStatHours.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeLibraryStatHours.setStatus(_A)
_CpqFcTapeLibraryStatMoves_Type=Counter32
_CpqFcTapeLibraryStatMoves_Object=MibTableColumn
cpqFcTapeLibraryStatMoves=_CpqFcTapeLibraryStatMoves_Object((1,3,6,1,4,1,232,16,3,2,1,1,14),_CpqFcTapeLibraryStatMoves_Type())
cpqFcTapeLibraryStatMoves.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeLibraryStatMoves.setStatus(_A)
class _CpqFcTapeLibraryDriveList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,60))
_CpqFcTapeLibraryDriveList_Type.__name__=_T
_CpqFcTapeLibraryDriveList_Object=MibTableColumn
cpqFcTapeLibraryDriveList=_CpqFcTapeLibraryDriveList_Object((1,3,6,1,4,1,232,16,3,2,1,1,15),_CpqFcTapeLibraryDriveList_Type())
cpqFcTapeLibraryDriveList.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeLibraryDriveList.setStatus(_A)
class _CpqFcTapeLibraryLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CpqFcTapeLibraryLocation_Type.__name__=_F
_CpqFcTapeLibraryLocation_Object=MibTableColumn
cpqFcTapeLibraryLocation=_CpqFcTapeLibraryLocation_Object((1,3,6,1,4,1,232,16,3,2,1,1,16),_CpqFcTapeLibraryLocation_Type())
cpqFcTapeLibraryLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeLibraryLocation.setStatus(_A)
class _CpqFcTapeLibraryTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_m,2),(_L,3),('safeTempExceeded',4),('maxTempExceeded',5)))
_CpqFcTapeLibraryTemperature_Type.__name__=_D
_CpqFcTapeLibraryTemperature_Object=MibTableColumn
cpqFcTapeLibraryTemperature=_CpqFcTapeLibraryTemperature_Object((1,3,6,1,4,1,232,16,3,2,1,1,17),_CpqFcTapeLibraryTemperature_Type())
cpqFcTapeLibraryTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeLibraryTemperature.setStatus(_A)
class _CpqFcTapeLibraryRedundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_m,2),('capable',3),(_AX,4),(_j,5)))
_CpqFcTapeLibraryRedundancy_Type.__name__=_D
_CpqFcTapeLibraryRedundancy_Object=MibTableColumn
cpqFcTapeLibraryRedundancy=_CpqFcTapeLibraryRedundancy_Object((1,3,6,1,4,1,232,16,3,2,1,1,18),_CpqFcTapeLibraryRedundancy_Type())
cpqFcTapeLibraryRedundancy.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeLibraryRedundancy.setStatus(_A)
class _CpqFcTapeLibraryHotSwap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_m,2),('capable',3),(_AX,4)))
_CpqFcTapeLibraryHotSwap_Type.__name__=_D
_CpqFcTapeLibraryHotSwap_Object=MibTableColumn
cpqFcTapeLibraryHotSwap=_CpqFcTapeLibraryHotSwap_Object((1,3,6,1,4,1,232,16,3,2,1,1,19),_CpqFcTapeLibraryHotSwap_Type())
cpqFcTapeLibraryHotSwap.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeLibraryHotSwap.setStatus(_A)
_CpqFcTapeDrive_ObjectIdentity=ObjectIdentity
cpqFcTapeDrive=_CpqFcTapeDrive_ObjectIdentity((1,3,6,1,4,1,232,16,3,3))
_CpqFcTapeDriveTable_Object=MibTable
cpqFcTapeDriveTable=_CpqFcTapeDriveTable_Object((1,3,6,1,4,1,232,16,3,3,1))
if mibBuilder.loadTexts:cpqFcTapeDriveTable.setStatus(_A)
_CpqFcTapeDriveEntry_Object=MibTableRow
cpqFcTapeDriveEntry=_CpqFcTapeDriveEntry_Object((1,3,6,1,4,1,232,16,3,3,1,1))
cpqFcTapeDriveEntry.setIndexNames((0,_C,_f),(0,_C,_V),(0,_C,_W),(0,_C,_X))
if mibBuilder.loadTexts:cpqFcTapeDriveEntry.setStatus(_A)
class _CpqFcTapeDriveCntlrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqFcTapeDriveCntlrIndex_Type.__name__=_D
_CpqFcTapeDriveCntlrIndex_Object=MibTableColumn
cpqFcTapeDriveCntlrIndex=_CpqFcTapeDriveCntlrIndex_Object((1,3,6,1,4,1,232,16,3,3,1,1,1),_CpqFcTapeDriveCntlrIndex_Type())
cpqFcTapeDriveCntlrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeDriveCntlrIndex.setStatus(_A)
class _CpqFcTapeDriveScsiBus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqFcTapeDriveScsiBus_Type.__name__=_D
_CpqFcTapeDriveScsiBus_Object=MibTableColumn
cpqFcTapeDriveScsiBus=_CpqFcTapeDriveScsiBus_Object((1,3,6,1,4,1,232,16,3,3,1,1,2),_CpqFcTapeDriveScsiBus_Type())
cpqFcTapeDriveScsiBus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeDriveScsiBus.setStatus(_A)
class _CpqFcTapeDriveScsiTarget_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqFcTapeDriveScsiTarget_Type.__name__=_D
_CpqFcTapeDriveScsiTarget_Object=MibTableColumn
cpqFcTapeDriveScsiTarget=_CpqFcTapeDriveScsiTarget_Object((1,3,6,1,4,1,232,16,3,3,1,1,3),_CpqFcTapeDriveScsiTarget_Type())
cpqFcTapeDriveScsiTarget.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeDriveScsiTarget.setStatus(_A)
class _CpqFcTapeDriveScsiLun_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqFcTapeDriveScsiLun_Type.__name__=_D
_CpqFcTapeDriveScsiLun_Object=MibTableColumn
cpqFcTapeDriveScsiLun=_CpqFcTapeDriveScsiLun_Object((1,3,6,1,4,1,232,16,3,3,1,1,4),_CpqFcTapeDriveScsiLun_Type())
cpqFcTapeDriveScsiLun.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeDriveScsiLun.setStatus(_A)
class _CpqFcTapeDriveSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqFcTapeDriveSerialNumber_Type.__name__=_F
_CpqFcTapeDriveSerialNumber_Object=MibTableColumn
cpqFcTapeDriveSerialNumber=_CpqFcTapeDriveSerialNumber_Object((1,3,6,1,4,1,232,16,3,3,1,1,5),_CpqFcTapeDriveSerialNumber_Type())
cpqFcTapeDriveSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeDriveSerialNumber.setStatus(_A)
class _CpqFcTapeDriveModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CpqFcTapeDriveModel_Type.__name__=_F
_CpqFcTapeDriveModel_Object=MibTableColumn
cpqFcTapeDriveModel=_CpqFcTapeDriveModel_Object((1,3,6,1,4,1,232,16,3,3,1,1,6),_CpqFcTapeDriveModel_Type())
cpqFcTapeDriveModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeDriveModel.setStatus(_A)
class _CpqFcTapeDriveFWRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqFcTapeDriveFWRev_Type.__name__=_F
_CpqFcTapeDriveFWRev_Object=MibTableColumn
cpqFcTapeDriveFWRev=_CpqFcTapeDriveFWRev_Object((1,3,6,1,4,1,232,16,3,3,1,1,7),_CpqFcTapeDriveFWRev_Type())
cpqFcTapeDriveFWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeDriveFWRev.setStatus(_A)
class _CpqFcTapeDriveType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),('cpqDlt35-70',2)))
_CpqFcTapeDriveType_Type.__name__=_D
_CpqFcTapeDriveType_Object=MibTableColumn
cpqFcTapeDriveType=_CpqFcTapeDriveType_Object((1,3,6,1,4,1,232,16,3,3,1,1,8),_CpqFcTapeDriveType_Type())
cpqFcTapeDriveType.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeDriveType.setStatus(_P)
class _CpqFcTapeDriveFWSubtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqFcTapeDriveFWSubtype_Type.__name__=_D
_CpqFcTapeDriveFWSubtype_Object=MibTableColumn
cpqFcTapeDriveFWSubtype=_CpqFcTapeDriveFWSubtype_Object((1,3,6,1,4,1,232,16,3,3,1,1,9),_CpqFcTapeDriveFWSubtype_Type())
cpqFcTapeDriveFWSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeDriveFWSubtype.setStatus(_A)
class _CpqFcTapeDriveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),(_L,2),(_Q,3),(_M,4),(_d,5),('missingWasOk',6),('missingWasOffline',7)))
_CpqFcTapeDriveStatus_Type.__name__=_D
_CpqFcTapeDriveStatus_Object=MibTableColumn
cpqFcTapeDriveStatus=_CpqFcTapeDriveStatus_Object((1,3,6,1,4,1,232,16,3,3,1,1,10),_CpqFcTapeDriveStatus_Type())
cpqFcTapeDriveStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeDriveStatus.setStatus(_A)
class _CpqFcTapeDriveCleanReq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_S,2),(_R,3)))
_CpqFcTapeDriveCleanReq_Type.__name__=_D
_CpqFcTapeDriveCleanReq_Object=MibTableColumn
cpqFcTapeDriveCleanReq=_CpqFcTapeDriveCleanReq_Object((1,3,6,1,4,1,232,16,3,3,1,1,11),_CpqFcTapeDriveCleanReq_Type())
cpqFcTapeDriveCleanReq.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeDriveCleanReq.setStatus(_A)
class _CpqFcTapeDriveCleanTapeRepl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_S,2),(_R,3)))
_CpqFcTapeDriveCleanTapeRepl_Type.__name__=_D
_CpqFcTapeDriveCleanTapeRepl_Object=MibTableColumn
cpqFcTapeDriveCleanTapeRepl=_CpqFcTapeDriveCleanTapeRepl_Object((1,3,6,1,4,1,232,16,3,3,1,1,12),_CpqFcTapeDriveCleanTapeRepl_Type())
cpqFcTapeDriveCleanTapeRepl.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeDriveCleanTapeRepl.setStatus(_A)
_CpqFcTapeDriveCondition_Type=Integer32
_CpqFcTapeDriveCondition_Object=MibTableColumn
cpqFcTapeDriveCondition=_CpqFcTapeDriveCondition_Object((1,3,6,1,4,1,232,16,3,3,1,1,13),_CpqFcTapeDriveCondition_Type())
cpqFcTapeDriveCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeDriveCondition.setStatus(_A)
_CpqFcTapeDriveCleanTapeCount_Type=Integer32
_CpqFcTapeDriveCleanTapeCount_Object=MibTableColumn
cpqFcTapeDriveCleanTapeCount=_CpqFcTapeDriveCleanTapeCount_Object((1,3,6,1,4,1,232,16,3,3,1,1,14),_CpqFcTapeDriveCleanTapeCount_Type())
cpqFcTapeDriveCleanTapeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeDriveCleanTapeCount.setStatus(_A)
class _CpqFcTapeDriveLibraryDrive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_S,2),(_R,3)))
_CpqFcTapeDriveLibraryDrive_Type.__name__=_D
_CpqFcTapeDriveLibraryDrive_Object=MibTableColumn
cpqFcTapeDriveLibraryDrive=_CpqFcTapeDriveLibraryDrive_Object((1,3,6,1,4,1,232,16,3,3,1,1,15),_CpqFcTapeDriveLibraryDrive_Type())
cpqFcTapeDriveLibraryDrive.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeDriveLibraryDrive.setStatus(_A)
class _CpqFcTapeDriveLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CpqFcTapeDriveLocation_Type.__name__=_F
_CpqFcTapeDriveLocation_Object=MibTableColumn
cpqFcTapeDriveLocation=_CpqFcTapeDriveLocation_Object((1,3,6,1,4,1,232,16,3,3,1,1,16),_CpqFcTapeDriveLocation_Type())
cpqFcTapeDriveLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeDriveLocation.setStatus(_A)
class _CpqFcTapeDriveHotPlug_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('hotPlug',2),(_AN,3)))
_CpqFcTapeDriveHotPlug_Type.__name__=_D
_CpqFcTapeDriveHotPlug_Object=MibTableColumn
cpqFcTapeDriveHotPlug=_CpqFcTapeDriveHotPlug_Object((1,3,6,1,4,1,232,16,3,3,1,1,17),_CpqFcTapeDriveHotPlug_Type())
cpqFcTapeDriveHotPlug.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeDriveHotPlug.setStatus(_A)
_CpqFcTapeDriveBay_Type=Integer32
_CpqFcTapeDriveBay_Object=MibTableColumn
cpqFcTapeDriveBay=_CpqFcTapeDriveBay_Object((1,3,6,1,4,1,232,16,3,3,1,1,18),_CpqFcTapeDriveBay_Type())
cpqFcTapeDriveBay.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeDriveBay.setStatus(_A)
class _CpqFcTapeDriveCurrentWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('narrow',2),('wide16',3)))
_CpqFcTapeDriveCurrentWidth_Type.__name__=_D
_CpqFcTapeDriveCurrentWidth_Object=MibTableColumn
cpqFcTapeDriveCurrentWidth=_CpqFcTapeDriveCurrentWidth_Object((1,3,6,1,4,1,232,16,3,3,1,1,19),_CpqFcTapeDriveCurrentWidth_Type())
cpqFcTapeDriveCurrentWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeDriveCurrentWidth.setStatus(_A)
class _CpqFcTapeDriveCurrentSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_AO,2),('fast',3),('ultra',4),('ultra2',5),('ultra3',6)))
_CpqFcTapeDriveCurrentSpeed_Type.__name__=_D
_CpqFcTapeDriveCurrentSpeed_Object=MibTableColumn
cpqFcTapeDriveCurrentSpeed=_CpqFcTapeDriveCurrentSpeed_Object((1,3,6,1,4,1,232,16,3,3,1,1,20),_CpqFcTapeDriveCurrentSpeed_Type())
cpqFcTapeDriveCurrentSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeDriveCurrentSpeed.setStatus(_A)
_CpqFcTapeCounters_ObjectIdentity=ObjectIdentity
cpqFcTapeCounters=_CpqFcTapeCounters_ObjectIdentity((1,3,6,1,4,1,232,16,3,4))
_CpqFcTapeCountersTable_Object=MibTable
cpqFcTapeCountersTable=_CpqFcTapeCountersTable_Object((1,3,6,1,4,1,232,16,3,4,1))
if mibBuilder.loadTexts:cpqFcTapeCountersTable.setStatus(_A)
_CpqFcTapeCountersEntry_Object=MibTableRow
cpqFcTapeCountersEntry=_CpqFcTapeCountersEntry_Object((1,3,6,1,4,1,232,16,3,4,1,1))
cpqFcTapeCountersEntry.setIndexNames((0,_C,_AY),(0,_C,_AZ),(0,_C,_Aa),(0,_C,_Ab))
if mibBuilder.loadTexts:cpqFcTapeCountersEntry.setStatus(_A)
class _CpqFcTapeCountersCntlrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqFcTapeCountersCntlrIndex_Type.__name__=_D
_CpqFcTapeCountersCntlrIndex_Object=MibTableColumn
cpqFcTapeCountersCntlrIndex=_CpqFcTapeCountersCntlrIndex_Object((1,3,6,1,4,1,232,16,3,4,1,1,1),_CpqFcTapeCountersCntlrIndex_Type())
cpqFcTapeCountersCntlrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeCountersCntlrIndex.setStatus(_A)
class _CpqFcTapeCountersScsiBus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqFcTapeCountersScsiBus_Type.__name__=_D
_CpqFcTapeCountersScsiBus_Object=MibTableColumn
cpqFcTapeCountersScsiBus=_CpqFcTapeCountersScsiBus_Object((1,3,6,1,4,1,232,16,3,4,1,1,2),_CpqFcTapeCountersScsiBus_Type())
cpqFcTapeCountersScsiBus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeCountersScsiBus.setStatus(_A)
class _CpqFcTapeCountersScsiTarget_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqFcTapeCountersScsiTarget_Type.__name__=_D
_CpqFcTapeCountersScsiTarget_Object=MibTableColumn
cpqFcTapeCountersScsiTarget=_CpqFcTapeCountersScsiTarget_Object((1,3,6,1,4,1,232,16,3,4,1,1,3),_CpqFcTapeCountersScsiTarget_Type())
cpqFcTapeCountersScsiTarget.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeCountersScsiTarget.setStatus(_A)
class _CpqFcTapeCountersScsiLun_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqFcTapeCountersScsiLun_Type.__name__=_D
_CpqFcTapeCountersScsiLun_Object=MibTableColumn
cpqFcTapeCountersScsiLun=_CpqFcTapeCountersScsiLun_Object((1,3,6,1,4,1,232,16,3,4,1,1,4),_CpqFcTapeCountersScsiLun_Type())
cpqFcTapeCountersScsiLun.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeCountersScsiLun.setStatus(_A)
_CpqFcTapeCountersReWrites_Type=Counter32
_CpqFcTapeCountersReWrites_Object=MibTableColumn
cpqFcTapeCountersReWrites=_CpqFcTapeCountersReWrites_Object((1,3,6,1,4,1,232,16,3,4,1,1,5),_CpqFcTapeCountersReWrites_Type())
cpqFcTapeCountersReWrites.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeCountersReWrites.setStatus(_A)
_CpqFcTapeCountersReReads_Type=Counter32
_CpqFcTapeCountersReReads_Object=MibTableColumn
cpqFcTapeCountersReReads=_CpqFcTapeCountersReReads_Object((1,3,6,1,4,1,232,16,3,4,1,1,6),_CpqFcTapeCountersReReads_Type())
cpqFcTapeCountersReReads.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeCountersReReads.setStatus(_A)
_CpqFcTapeCountersTotalErrors_Type=Counter32
_CpqFcTapeCountersTotalErrors_Object=MibTableColumn
cpqFcTapeCountersTotalErrors=_CpqFcTapeCountersTotalErrors_Object((1,3,6,1,4,1,232,16,3,4,1,1,7),_CpqFcTapeCountersTotalErrors_Type())
cpqFcTapeCountersTotalErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeCountersTotalErrors.setStatus(_A)
_CpqFcTapeCountersTotalUncorrectable_Type=Counter32
_CpqFcTapeCountersTotalUncorrectable_Object=MibTableColumn
cpqFcTapeCountersTotalUncorrectable=_CpqFcTapeCountersTotalUncorrectable_Object((1,3,6,1,4,1,232,16,3,4,1,1,8),_CpqFcTapeCountersTotalUncorrectable_Type())
cpqFcTapeCountersTotalUncorrectable.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeCountersTotalUncorrectable.setStatus(_A)
_CpqFcTapeCountersTotalBytes_Type=Counter32
_CpqFcTapeCountersTotalBytes_Object=MibTableColumn
cpqFcTapeCountersTotalBytes=_CpqFcTapeCountersTotalBytes_Object((1,3,6,1,4,1,232,16,3,4,1,1,9),_CpqFcTapeCountersTotalBytes_Type())
cpqFcTapeCountersTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcTapeCountersTotalBytes.setStatus(_A)
_CpqFcSwitchComponent_ObjectIdentity=ObjectIdentity
cpqFcSwitchComponent=_CpqFcSwitchComponent_ObjectIdentity((1,3,6,1,4,1,232,16,4))
_CpqFcSwitch_ObjectIdentity=ObjectIdentity
cpqFcSwitch=_CpqFcSwitch_ObjectIdentity((1,3,6,1,4,1,232,16,4,1))
_CpqFcSwitchTable_Object=MibTable
cpqFcSwitchTable=_CpqFcSwitchTable_Object((1,3,6,1,4,1,232,16,4,1,1))
if mibBuilder.loadTexts:cpqFcSwitchTable.setStatus(_A)
_CpqFcSwitchEntry_Object=MibTableRow
cpqFcSwitchEntry=_CpqFcSwitchEntry_Object((1,3,6,1,4,1,232,16,4,1,1,1))
cpqFcSwitchEntry.setIndexNames((0,_C,_Ac))
if mibBuilder.loadTexts:cpqFcSwitchEntry.setStatus(_A)
class _CpqFcSwitchIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqFcSwitchIndex_Type.__name__=_D
_CpqFcSwitchIndex_Object=MibTableColumn
cpqFcSwitchIndex=_CpqFcSwitchIndex_Object((1,3,6,1,4,1,232,16,4,1,1,1,1),_CpqFcSwitchIndex_Type())
cpqFcSwitchIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcSwitchIndex.setStatus(_A)
class _CpqFcSwitchLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('internal',2),('external',3)))
_CpqFcSwitchLocation_Type.__name__=_D
_CpqFcSwitchLocation_Object=MibTableColumn
cpqFcSwitchLocation=_CpqFcSwitchLocation_Object((1,3,6,1,4,1,232,16,4,1,1,1,2),_CpqFcSwitchLocation_Type())
cpqFcSwitchLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcSwitchLocation.setStatus(_A)
class _CpqFcSwitchChassisIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqFcSwitchChassisIndex_Type.__name__=_D
_CpqFcSwitchChassisIndex_Object=MibTableColumn
cpqFcSwitchChassisIndex=_CpqFcSwitchChassisIndex_Object((1,3,6,1,4,1,232,16,4,1,1,1,3),_CpqFcSwitchChassisIndex_Type())
cpqFcSwitchChassisIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcSwitchChassisIndex.setStatus(_A)
class _CpqFcSwitchChassisSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqFcSwitchChassisSlot_Type.__name__=_D
_CpqFcSwitchChassisSlot_Object=MibTableColumn
cpqFcSwitchChassisSlot=_CpqFcSwitchChassisSlot_Object((1,3,6,1,4,1,232,16,4,1,1,1,4),_CpqFcSwitchChassisSlot_Type())
cpqFcSwitchChassisSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcSwitchChassisSlot.setStatus(_A)
class _CpqFcSwitchWorldWideNodeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CpqFcSwitchWorldWideNodeName_Type.__name__=_F
_CpqFcSwitchWorldWideNodeName_Object=MibTableColumn
cpqFcSwitchWorldWideNodeName=_CpqFcSwitchWorldWideNodeName_Object((1,3,6,1,4,1,232,16,4,1,1,1,5),_CpqFcSwitchWorldWideNodeName_Type())
cpqFcSwitchWorldWideNodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcSwitchWorldWideNodeName.setStatus(_A)
class _CpqFcSwitchWorldWidePortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CpqFcSwitchWorldWidePortName_Type.__name__=_F
_CpqFcSwitchWorldWidePortName_Object=MibTableColumn
cpqFcSwitchWorldWidePortName=_CpqFcSwitchWorldWidePortName_Object((1,3,6,1,4,1,232,16,4,1,1,1,6),_CpqFcSwitchWorldWidePortName_Type())
cpqFcSwitchWorldWidePortName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcSwitchWorldWidePortName.setStatus(_A)
class _CpqFcSwitchIpAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CpqFcSwitchIpAddress_Type.__name__=_F
_CpqFcSwitchIpAddress_Object=MibTableColumn
cpqFcSwitchIpAddress=_CpqFcSwitchIpAddress_Object((1,3,6,1,4,1,232,16,4,1,1,1,7),_CpqFcSwitchIpAddress_Type())
cpqFcSwitchIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcSwitchIpAddress.setStatus(_A)
class _CpqFcSwitchIpGateway_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CpqFcSwitchIpGateway_Type.__name__=_F
_CpqFcSwitchIpGateway_Object=MibTableColumn
cpqFcSwitchIpGateway=_CpqFcSwitchIpGateway_Object((1,3,6,1,4,1,232,16,4,1,1,1,8),_CpqFcSwitchIpGateway_Type())
cpqFcSwitchIpGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcSwitchIpGateway.setStatus(_A)
class _CpqFcSwitchIpSubnet_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CpqFcSwitchIpSubnet_Type.__name__=_F
_CpqFcSwitchIpSubnet_Object=MibTableColumn
cpqFcSwitchIpSubnet=_CpqFcSwitchIpSubnet_Object((1,3,6,1,4,1,232,16,4,1,1,1,9),_CpqFcSwitchIpSubnet_Type())
cpqFcSwitchIpSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcSwitchIpSubnet.setStatus(_A)
class _CpqFcSwitchName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqFcSwitchName_Type.__name__=_F
_CpqFcSwitchName_Object=MibTableColumn
cpqFcSwitchName=_CpqFcSwitchName_Object((1,3,6,1,4,1,232,16,4,1,1,1,10),_CpqFcSwitchName_Type())
cpqFcSwitchName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcSwitchName.setStatus(_A)
class _CpqFcSwitchNetworkLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_j,2),('notActive',3)))
_CpqFcSwitchNetworkLinkStatus_Type.__name__=_D
_CpqFcSwitchNetworkLinkStatus_Object=MibTableColumn
cpqFcSwitchNetworkLinkStatus=_CpqFcSwitchNetworkLinkStatus_Object((1,3,6,1,4,1,232,16,4,1,1,1,11),_CpqFcSwitchNetworkLinkStatus_Type())
cpqFcSwitchNetworkLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcSwitchNetworkLinkStatus.setStatus(_A)
class _CpqFcSwitchFibreConnectStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),(_d,3)))
_CpqFcSwitchFibreConnectStatus_Type.__name__=_D
_CpqFcSwitchFibreConnectStatus_Object=MibTableColumn
cpqFcSwitchFibreConnectStatus=_CpqFcSwitchFibreConnectStatus_Object((1,3,6,1,4,1,232,16,4,1,1,1,12),_CpqFcSwitchFibreConnectStatus_Type())
cpqFcSwitchFibreConnectStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcSwitchFibreConnectStatus.setStatus(_A)
class _CpqFcSwitchFWRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqFcSwitchFWRev_Type.__name__=_F
_CpqFcSwitchFWRev_Object=MibTableColumn
cpqFcSwitchFWRev=_CpqFcSwitchFWRev_Object((1,3,6,1,4,1,232,16,4,1,1,1,13),_CpqFcSwitchFWRev_Type())
cpqFcSwitchFWRev.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqFcSwitchFWRev.setStatus(_A)
cpqFcaLogDrvStatusChange=NotificationType((1,3,6,1,4,1,232,0,16001))
cpqFcaLogDrvStatusChange.setObjects(*((_J,_K),(_G,_H),(_I,_N),(_I,_O),(_C,_k),(_C,_w)))
if mibBuilder.loadTexts:cpqFcaLogDrvStatusChange.setStatus('')
cpqFcaSpareStatusChange=NotificationType((1,3,6,1,4,1,232,0,16002))
cpqFcaSpareStatusChange.setObjects(*((_J,_K),(_G,_H),(_I,_N),(_I,_O),(_C,_Ad),(_C,_Ae),(_C,_Af)))
if mibBuilder.loadTexts:cpqFcaSpareStatusChange.setStatus('')
cpqFcaPhyDrvStatusChange=NotificationType((1,3,6,1,4,1,232,0,16003))
cpqFcaPhyDrvStatusChange.setObjects(*((_J,_K),(_G,_H),(_I,_N),(_I,_O),(_C,_x),(_C,_y),(_C,_z)))
if mibBuilder.loadTexts:cpqFcaPhyDrvStatusChange.setStatus('')
cpqFcaAccelStatusChange=NotificationType((1,3,6,1,4,1,232,0,16004))
cpqFcaAccelStatusChange.setObjects(*((_J,_K),(_G,_H),(_I,_N),(_I,_O),(_C,_U),(_C,_A0)))
if mibBuilder.loadTexts:cpqFcaAccelStatusChange.setStatus('')
cpqFcaAccelBadDataTrap=NotificationType((1,3,6,1,4,1,232,0,16005))
cpqFcaAccelBadDataTrap.setObjects(*((_J,_K),(_G,_H),(_I,_N),(_I,_O),(_C,_U)))
if mibBuilder.loadTexts:cpqFcaAccelBadDataTrap.setStatus('')
cpqFcaAccelBatteryFailed=NotificationType((1,3,6,1,4,1,232,0,16006))
cpqFcaAccelBatteryFailed.setObjects(*((_J,_K),(_G,_H),(_I,_N),(_I,_O),(_C,_U)))
if mibBuilder.loadTexts:cpqFcaAccelBatteryFailed.setStatus('')
cpqFcaCntlrStatusChange=NotificationType((1,3,6,1,4,1,232,0,16007))
cpqFcaCntlrStatusChange.setObjects(*((_J,_K),(_G,_H),(_I,_N),(_I,_O),(_C,_c),(_C,_A1)))
if mibBuilder.loadTexts:cpqFcaCntlrStatusChange.setStatus('')
cpqFcTapeCntlrStatusChange=NotificationType((1,3,6,1,4,1,232,0,16008))
cpqFcTapeCntlrStatusChange.setObjects(*((_J,_K),(_G,_H),(_C,_Y),(_C,_Ag)))
if mibBuilder.loadTexts:cpqFcTapeCntlrStatusChange.setStatus('')
cpqFcTapeLibraryStatusChange=NotificationType((1,3,6,1,4,1,232,0,16009))
cpqFcTapeLibraryStatusChange.setObjects(*((_J,_K),(_G,_H),(_C,_Y),(_C,_Z),(_C,_a),(_C,_b),(_C,_A2)))
if mibBuilder.loadTexts:cpqFcTapeLibraryStatusChange.setStatus('')
cpqFcTapeLibraryDoorStatusChange=NotificationType((1,3,6,1,4,1,232,0,16010))
cpqFcTapeLibraryDoorStatusChange.setObjects(*((_J,_K),(_G,_H),(_C,_Y),(_C,_Z),(_C,_a),(_C,_b),(_C,_A3)))
if mibBuilder.loadTexts:cpqFcTapeLibraryDoorStatusChange.setStatus('')
cpqFcTapeDriveStatusChange=NotificationType((1,3,6,1,4,1,232,0,16011))
cpqFcTapeDriveStatusChange.setObjects(*((_J,_K),(_G,_H),(_C,_Y),(_C,_V),(_C,_W),(_C,_X),(_C,_A4)))
if mibBuilder.loadTexts:cpqFcTapeDriveStatusChange.setStatus('')
cpqFcTapeDriveCleaningRequired=NotificationType((1,3,6,1,4,1,232,0,16012))
cpqFcTapeDriveCleaningRequired.setObjects(*((_J,_K),(_G,_H),(_C,_Y),(_C,_V),(_C,_W),(_C,_X)))
if mibBuilder.loadTexts:cpqFcTapeDriveCleaningRequired.setStatus('')
cpqFcTapeDriveCleanTapeReplace=NotificationType((1,3,6,1,4,1,232,0,16013))
cpqFcTapeDriveCleanTapeReplace.setObjects(*((_J,_K),(_G,_H),(_C,_Y),(_C,_V),(_C,_W),(_C,_X)))
if mibBuilder.loadTexts:cpqFcTapeDriveCleanTapeReplace.setStatus('')
cpqFcaCntlrActive=NotificationType((1,3,6,1,4,1,232,0,16014))
cpqFcaCntlrActive.setObjects(*((_J,_K),(_G,_H),(_I,_N),(_I,_O),(_C,_c)))
if mibBuilder.loadTexts:cpqFcaCntlrActive.setStatus('')
cpqFcaHostCntlrStatusChange=NotificationType((1,3,6,1,4,1,232,0,16015))
cpqFcaHostCntlrStatusChange.setObjects(*((_J,_K),(_G,_H),(_C,_A5),(_C,_n)))
if mibBuilder.loadTexts:cpqFcaHostCntlrStatusChange.setStatus('')
cpqFca2PhyDrvStatusChange=NotificationType((1,3,6,1,4,1,232,0,16016))
cpqFca2PhyDrvStatusChange.setObjects(*((_J,_K),(_G,_H),(_I,_N),(_I,_O),(_C,_x),(_C,_y),(_C,_z),(_C,_Ah),(_C,_Ai),(_C,_Aj),(_C,_Ak)))
if mibBuilder.loadTexts:cpqFca2PhyDrvStatusChange.setStatus('')
cpqFca2AccelStatusChange=NotificationType((1,3,6,1,4,1,232,0,16017))
cpqFca2AccelStatusChange.setObjects(*((_J,_K),(_G,_H),(_I,_N),(_I,_O),(_C,_U),(_C,_A0),(_C,_g),(_C,_o),(_C,_h),(_C,_Al)))
if mibBuilder.loadTexts:cpqFca2AccelStatusChange.setStatus('')
cpqFca2AccelBadDataTrap=NotificationType((1,3,6,1,4,1,232,0,16018))
cpqFca2AccelBadDataTrap.setObjects(*((_J,_K),(_G,_H),(_I,_N),(_I,_O),(_C,_U),(_C,_g),(_C,_o),(_C,_h)))
if mibBuilder.loadTexts:cpqFca2AccelBadDataTrap.setStatus('')
cpqFca2AccelBatteryFailed=NotificationType((1,3,6,1,4,1,232,0,16019))
cpqFca2AccelBatteryFailed.setObjects(*((_J,_K),(_G,_H),(_I,_N),(_I,_O),(_C,_U),(_C,_g),(_C,_o),(_C,_h)))
if mibBuilder.loadTexts:cpqFca2AccelBatteryFailed.setStatus('')
cpqFca2CntlrStatusChange=NotificationType((1,3,6,1,4,1,232,0,16020))
cpqFca2CntlrStatusChange.setObjects(*((_J,_K),(_G,_H),(_I,_N),(_I,_O),(_C,_c),(_C,_A1),(_C,_g),(_C,_Am),(_C,_h)))
if mibBuilder.loadTexts:cpqFca2CntlrStatusChange.setStatus('')
cpqFca2HostCntlrStatusChange=NotificationType((1,3,6,1,4,1,232,0,16021))
cpqFca2HostCntlrStatusChange.setObjects(*((_J,_K),(_G,_H),(_C,_A5),(_C,_n),(_C,_A6),(_C,_A7)))
if mibBuilder.loadTexts:cpqFca2HostCntlrStatusChange.setStatus('')
cpqExtArrayLogDrvStatusChange=NotificationType((1,3,6,1,4,1,232,0,16022))
cpqExtArrayLogDrvStatusChange.setObjects(*((_J,_K),(_G,_H),(_I,_N),(_I,_O),(_C,_u),(_C,_k),(_C,_w),(_C,_An),(_C,_Ao),(_C,_Ap)))
if mibBuilder.loadTexts:cpqExtArrayLogDrvStatusChange.setStatus('')
cpqExtTapeDriveStatusChange=NotificationType((1,3,6,1,4,1,232,0,16023))
cpqExtTapeDriveStatusChange.setObjects(*((_J,_K),(_G,_H),(_C,_f),(_C,_V),(_C,_W),(_C,_X),(_C,_p),(_C,_q),(_C,_r),(_C,_s),(_C,_A4)))
if mibBuilder.loadTexts:cpqExtTapeDriveStatusChange.setStatus('')
cpqExtTapeDriveCleaningRequired=NotificationType((1,3,6,1,4,1,232,0,16024))
cpqExtTapeDriveCleaningRequired.setObjects(*((_J,_K),(_G,_H),(_C,_f),(_C,_V),(_C,_W),(_C,_X),(_C,_p),(_C,_q),(_C,_r),(_C,_s)))
if mibBuilder.loadTexts:cpqExtTapeDriveCleaningRequired.setStatus('')
cpqExtTapeDriveCleanTapeReplace=NotificationType((1,3,6,1,4,1,232,0,16025))
cpqExtTapeDriveCleanTapeReplace.setObjects(*((_J,_K),(_G,_H),(_C,_f),(_C,_V),(_C,_W),(_C,_X),(_C,_p),(_C,_q),(_C,_r),(_C,_s)))
if mibBuilder.loadTexts:cpqExtTapeDriveCleanTapeReplace.setStatus('')
cpqExtTapeLibraryStatusChange=NotificationType((1,3,6,1,4,1,232,0,16026))
cpqExtTapeLibraryStatusChange.setObjects(*((_J,_K),(_G,_H),(_C,_l),(_C,_Z),(_C,_a),(_C,_b),(_C,_A8),(_C,_A9),(_C,_AA),(_C,_AB),(_C,_A2)))
if mibBuilder.loadTexts:cpqExtTapeLibraryStatusChange.setStatus('')
cpqExtTapeLibraryDoorStatusChange=NotificationType((1,3,6,1,4,1,232,0,16027))
cpqExtTapeLibraryDoorStatusChange.setObjects(*((_J,_K),(_G,_H),(_C,_l),(_C,_Z),(_C,_a),(_C,_b),(_C,_A8),(_C,_A9),(_C,_AA),(_C,_AB),(_C,_A3)))
if mibBuilder.loadTexts:cpqExtTapeLibraryDoorStatusChange.setStatus('')
cpqFca3HostCntlrStatusChange=NotificationType((1,3,6,1,4,1,232,0,16028))
cpqFca3HostCntlrStatusChange.setObjects(*((_J,_K),(_G,_H),(_C,_Aq),(_C,_v),(_C,_n),(_C,_A6),(_C,_Ar),(_C,_A7),(_C,_As)))
if mibBuilder.loadTexts:cpqFca3HostCntlrStatusChange.setStatus('')
mibBuilder.exportSymbols(_C,**{'cpqFcaLogDrvStatusChange':cpqFcaLogDrvStatusChange,'cpqFcaSpareStatusChange':cpqFcaSpareStatusChange,'cpqFcaPhyDrvStatusChange':cpqFcaPhyDrvStatusChange,'cpqFcaAccelStatusChange':cpqFcaAccelStatusChange,'cpqFcaAccelBadDataTrap':cpqFcaAccelBadDataTrap,'cpqFcaAccelBatteryFailed':cpqFcaAccelBatteryFailed,'cpqFcaCntlrStatusChange':cpqFcaCntlrStatusChange,'cpqFcTapeCntlrStatusChange':cpqFcTapeCntlrStatusChange,'cpqFcTapeLibraryStatusChange':cpqFcTapeLibraryStatusChange,'cpqFcTapeLibraryDoorStatusChange':cpqFcTapeLibraryDoorStatusChange,'cpqFcTapeDriveStatusChange':cpqFcTapeDriveStatusChange,'cpqFcTapeDriveCleaningRequired':cpqFcTapeDriveCleaningRequired,'cpqFcTapeDriveCleanTapeReplace':cpqFcTapeDriveCleanTapeReplace,'cpqFcaCntlrActive':cpqFcaCntlrActive,'cpqFcaHostCntlrStatusChange':cpqFcaHostCntlrStatusChange,'cpqFca2PhyDrvStatusChange':cpqFca2PhyDrvStatusChange,'cpqFca2AccelStatusChange':cpqFca2AccelStatusChange,'cpqFca2AccelBadDataTrap':cpqFca2AccelBadDataTrap,'cpqFca2AccelBatteryFailed':cpqFca2AccelBatteryFailed,'cpqFca2CntlrStatusChange':cpqFca2CntlrStatusChange,'cpqFca2HostCntlrStatusChange':cpqFca2HostCntlrStatusChange,'cpqExtArrayLogDrvStatusChange':cpqExtArrayLogDrvStatusChange,'cpqExtTapeDriveStatusChange':cpqExtTapeDriveStatusChange,'cpqExtTapeDriveCleaningRequired':cpqExtTapeDriveCleaningRequired,'cpqExtTapeDriveCleanTapeReplace':cpqExtTapeDriveCleanTapeReplace,'cpqExtTapeLibraryStatusChange':cpqExtTapeLibraryStatusChange,'cpqExtTapeLibraryDoorStatusChange':cpqExtTapeLibraryDoorStatusChange,'cpqFca3HostCntlrStatusChange':cpqFca3HostCntlrStatusChange,'cpqFibreArray':cpqFibreArray,'cpqFcaMibRev':cpqFcaMibRev,'cpqFcaMibRevMajor':cpqFcaMibRevMajor,'cpqFcaMibRevMinor':cpqFcaMibRevMinor,'cpqFcaMibCondition':cpqFcaMibCondition,'cpqFcaComponent':cpqFcaComponent,'cpqFcaInterface':cpqFcaInterface,'cpqFcaOsCommon':cpqFcaOsCommon,'cpqFcaOsCommonPollFreq':cpqFcaOsCommonPollFreq,'cpqFcaOsCommonModuleTable':cpqFcaOsCommonModuleTable,'cpqFcaOsCommonModuleEntry':cpqFcaOsCommonModuleEntry,_AD:cpqFcaOsCommonModuleIndex,'cpqFcaOsCommonModuleName':cpqFcaOsCommonModuleName,'cpqFcaOsCommonModuleVersion':cpqFcaOsCommonModuleVersion,'cpqFcaOsCommonModuleDate':cpqFcaOsCommonModuleDate,'cpqFcaOsCommonModulePurpose':cpqFcaOsCommonModulePurpose,'cpqFcaCntlr':cpqFcaCntlr,'cpqFcaCntlrTable':cpqFcaCntlrTable,'cpqFcaCntlrEntry':cpqFcaCntlrEntry,_AE:cpqFcaCntlrBoxIndex,_c:cpqFcaCntlrBoxIoSlot,_g:cpqFcaCntlrModel,'cpqFcaCntlrFWRev':cpqFcaCntlrFWRev,_A1:cpqFcaCntlrStatus,'cpqFcaCntlrCondition':cpqFcaCntlrCondition,'cpqFcaCntlrProductRev':cpqFcaCntlrProductRev,'cpqFcaCntlrWorldWideName':cpqFcaCntlrWorldWideName,_Am:cpqFcaCntlrSerialNumber,'cpqFcaCntlrCurrentRole':cpqFcaCntlrCurrentRole,'cpqFcaCntlrRedundancyType':cpqFcaCntlrRedundancyType,'cpqFcaCntlrRedundancyError':cpqFcaCntlrRedundancyError,'cpqFcaCntlrBlinkTime':cpqFcaCntlrBlinkTime,'cpqFcaCntlrWorldWideNodeName':cpqFcaCntlrWorldWideNodeName,'cpqFcaCntlrRebuildPriority':cpqFcaCntlrRebuildPriority,'cpqFcaCntlrExpandPriority':cpqFcaCntlrExpandPriority,'cpqFcaAccelTable':cpqFcaAccelTable,'cpqFcaAccelEntry':cpqFcaAccelEntry,_AG:cpqFcaAccelBoxIndex,_U:cpqFcaAccelBoxIoSlot,_A0:cpqFcaAccelStatus,'cpqFcaAccelBadData':cpqFcaAccelBadData,_Al:cpqFcaAccelErrCode,'cpqFcaAccelBatteryStatus':cpqFcaAccelBatteryStatus,'cpqFcaAccelReadErrs':cpqFcaAccelReadErrs,'cpqFcaAccelWriteErrs':cpqFcaAccelWriteErrs,'cpqFcaAccelCondition':cpqFcaAccelCondition,'cpqFcaAccelWriteCache':cpqFcaAccelWriteCache,'cpqFcaAccelReadCache':cpqFcaAccelReadCache,_o:cpqFcaAccelSerialNumber,_h:cpqFcaAccelTotalMemory,'cpqFcaAccelFailedBatteries':cpqFcaAccelFailedBatteries,'cpqFcaLogDrv':cpqFcaLogDrv,'cpqFcaLogDrvTable':cpqFcaLogDrvTable,'cpqFcaLogDrvEntry':cpqFcaLogDrvEntry,_u:cpqFcaLogDrvBoxIndex,_k:cpqFcaLogDrvIndex,_Ao:cpqFcaLogDrvFaultTol,_w:cpqFcaLogDrvStatus,'cpqFcaLogDrvAutoRel':cpqFcaLogDrvAutoRel,'cpqFcaLogDrvPercentRebuild':cpqFcaLogDrvPercentRebuild,'cpqFcaLogDrvHasAccel':cpqFcaLogDrvHasAccel,'cpqFcaLogDrvAvailSpares':cpqFcaLogDrvAvailSpares,_Ap:cpqFcaLogDrvSize,'cpqFcaLogDrvPhyDrvIDs':cpqFcaLogDrvPhyDrvIDs,'cpqFcaLogDrvCondition':cpqFcaLogDrvCondition,'cpqFcaLogDrvStripeSize':cpqFcaLogDrvStripeSize,_An:cpqFcaLogDrvOsName,'cpqFcaLogDrvBlinkTime':cpqFcaLogDrvBlinkTime,'cpqFcaLogDrvSpareReplaceMap':cpqFcaLogDrvSpareReplaceMap,'cpqFcaLogDrvRebuildingPhyDrv':cpqFcaLogDrvRebuildingPhyDrv,'cpqFcaLogDrvSnapshotResourceDrvIndex':cpqFcaLogDrvSnapshotResourceDrvIndex,'cpqFcaLogDrvSnapshotSourceDrvIndex':cpqFcaLogDrvSnapshotSourceDrvIndex,'cpqFcaLogDrvPreferredPath':cpqFcaLogDrvPreferredPath,'cpqFcaLogDrvCurrentPath':cpqFcaLogDrvCurrentPath,'cpqFcaSpareDrv':cpqFcaSpareDrv,'cpqFcaSpareTable':cpqFcaSpareTable,'cpqFcaSpareEntry':cpqFcaSpareEntry,_AJ:cpqFcaSpareBoxIndex,_AK:cpqFcaSparePhyDrvIndex,_Af:cpqFcaSpareStatus,'cpqFcaSpareReplacedDrvBay':cpqFcaSpareReplacedDrvBay,'cpqFcaSparePercentRebuild':cpqFcaSparePercentRebuild,'cpqFcaSpareCondition':cpqFcaSpareCondition,_Ad:cpqFcaSpareBusNumber,_Ae:cpqFcaSpareBay,'cpqFcaSpareReplacedDrvBusNumber':cpqFcaSpareReplacedDrvBusNumber,'cpqFcaSpareLocationString':cpqFcaSpareLocationString,'cpqFcaPhyDrv':cpqFcaPhyDrv,'cpqFcaPhyDrvTable':cpqFcaPhyDrvTable,'cpqFcaPhyDrvEntry':cpqFcaPhyDrvEntry,_AL:cpqFcaPhyDrvBoxIndex,_AM:cpqFcaPhyDrvIndex,_Ah:cpqFcaPhyDrvModel,_Aj:cpqFcaPhyDrvFWRev,_y:cpqFcaPhyDrvBay,_z:cpqFcaPhyDrvStatus,'cpqFcaPhyDrvUsedReallocs':cpqFcaPhyDrvUsedReallocs,'cpqFcaPhyDrvRefHours':cpqFcaPhyDrvRefHours,'cpqFcaPhyDrvHReads':cpqFcaPhyDrvHReads,'cpqFcaPhyDrvReads':cpqFcaPhyDrvReads,'cpqFcaPhyDrvHWrites':cpqFcaPhyDrvHWrites,'cpqFcaPhyDrvWrites':cpqFcaPhyDrvWrites,'cpqFcaPhyDrvHSeeks':cpqFcaPhyDrvHSeeks,'cpqFcaPhyDrvSeeks':cpqFcaPhyDrvSeeks,'cpqFcaPhyDrvHardReadErrs':cpqFcaPhyDrvHardReadErrs,'cpqFcaPhyDrvRecvReadErrs':cpqFcaPhyDrvRecvReadErrs,'cpqFcaPhyDrvHardWriteErrs':cpqFcaPhyDrvHardWriteErrs,'cpqFcaPhyDrvRecvWriteErrs':cpqFcaPhyDrvRecvWriteErrs,'cpqFcaPhyDrvHSeekErrs':cpqFcaPhyDrvHSeekErrs,'cpqFcaPhyDrvSeekErrs':cpqFcaPhyDrvSeekErrs,'cpqFcaPhyDrvSpinupTime':cpqFcaPhyDrvSpinupTime,'cpqFcaPhyDrvFunctTest1':cpqFcaPhyDrvFunctTest1,'cpqFcaPhyDrvFunctTest2':cpqFcaPhyDrvFunctTest2,'cpqFcaPhyDrvFunctTest3':cpqFcaPhyDrvFunctTest3,'cpqFcaPhyDrvOtherTimeouts':cpqFcaPhyDrvOtherTimeouts,'cpqFcaPhyDrvBadRecvReads':cpqFcaPhyDrvBadRecvReads,'cpqFcaPhyDrvBadRecvWrites':cpqFcaPhyDrvBadRecvWrites,'cpqFcaPhyDrvFormatErrs':cpqFcaPhyDrvFormatErrs,'cpqFcaPhyDrvNotReadyErrs':cpqFcaPhyDrvNotReadyErrs,'cpqFcaPhyDrvHasMonInfo':cpqFcaPhyDrvHasMonInfo,'cpqFcaPhyDrvCondition':cpqFcaPhyDrvCondition,'cpqFcaPhyDrvHotPlugs':cpqFcaPhyDrvHotPlugs,'cpqFcaPhyDrvMediaErrs':cpqFcaPhyDrvMediaErrs,'cpqFcaPhyDrvHardwareErrs':cpqFcaPhyDrvHardwareErrs,'cpqFcaPhyDrvAbortedCmds':cpqFcaPhyDrvAbortedCmds,'cpqFcaPhyDrvSpinUpErrs':cpqFcaPhyDrvSpinUpErrs,'cpqFcaPhyDrvBadTargetErrs':cpqFcaPhyDrvBadTargetErrs,'cpqFcaPhyDrvSize':cpqFcaPhyDrvSize,'cpqFcaPhyDrvBusFaults':cpqFcaPhyDrvBusFaults,'cpqFcaPhyDrvHotPlug':cpqFcaPhyDrvHotPlug,'cpqFcaPhyDrvPlacement':cpqFcaPhyDrvPlacement,_x:cpqFcaPhyDrvBusNumber,_Ai:cpqFcaPhyDrvSerialNum,'cpqFcaPhyDrvPreFailMonitoring':cpqFcaPhyDrvPreFailMonitoring,'cpqFcaPhyDrvCurrentWidth':cpqFcaPhyDrvCurrentWidth,'cpqFcaPhyDrvCurrentSpeed':cpqFcaPhyDrvCurrentSpeed,_Ak:cpqFcaPhyDrvFailureCode,'cpqFcaPhyDrvBlinkTime':cpqFcaPhyDrvBlinkTime,'cpqFcaPhyDrvSmartStatus':cpqFcaPhyDrvSmartStatus,'cpqFcaPhyDrvRotationalSpeed':cpqFcaPhyDrvRotationalSpeed,'cpqFcaPhyDrvType':cpqFcaPhyDrvType,'cpqFcaPhyDrvSataVersion':cpqFcaPhyDrvSataVersion,'cpqFcaPhyDrvBoxConnector':cpqFcaPhyDrvBoxConnector,'cpqFcaPhyDrvBoxOnConnector':cpqFcaPhyDrvBoxOnConnector,'cpqFcaPhyDrvLocationString':cpqFcaPhyDrvLocationString,'cpqFcaPhyDrvNegotiatedLinkRate':cpqFcaPhyDrvNegotiatedLinkRate,'cpqFcaPhyDrvPhyCount':cpqFcaPhyDrvPhyCount,'cpqFcaPhyDrvUnsupportedDrive':cpqFcaPhyDrvUnsupportedDrive,'cpqFcaPhyDrvThr':cpqFcaPhyDrvThr,'cpqFcaPhyDrvThrTable':cpqFcaPhyDrvThrTable,'cpqFcaPhyDrvThrEntry':cpqFcaPhyDrvThrEntry,_AP:cpqFcaPhyDrvThrBoxIndex,_AQ:cpqFcaPhyDrvThrIndex,'cpqFcaPhyDrvThrUsedReallocs':cpqFcaPhyDrvThrUsedReallocs,'cpqFcaPhyDrvThrSpinupTime':cpqFcaPhyDrvThrSpinupTime,'cpqFcaPhyDrvThrFunctTest1':cpqFcaPhyDrvThrFunctTest1,'cpqFcaPhyDrvThrFunctTest2':cpqFcaPhyDrvThrFunctTest2,'cpqFcaPhyDrvThrFunctTest3':cpqFcaPhyDrvThrFunctTest3,'cpqFcaPhyDrvThrViUsedReallocs':cpqFcaPhyDrvThrViUsedReallocs,'cpqFcaPhyDrvThrViSpinupTime':cpqFcaPhyDrvThrViSpinupTime,'cpqFcaPhyDrvThrViFunctTest1':cpqFcaPhyDrvThrViFunctTest1,'cpqFcaPhyDrvThrViFunctTest2':cpqFcaPhyDrvThrViFunctTest2,'cpqFcaPhyDrvThrViFunctTest3':cpqFcaPhyDrvThrViFunctTest3,'cpqFcaHostCntlr':cpqFcaHostCntlr,'cpqFcaHostCntlrTable':cpqFcaHostCntlrTable,'cpqFcaHostCntlrEntry':cpqFcaHostCntlrEntry,_v:cpqFcaHostCntlrIndex,_A5:cpqFcaHostCntlrSlot,_A6:cpqFcaHostCntlrModel,_n:cpqFcaHostCntlrStatus,'cpqFcaHostCntlrCondition':cpqFcaHostCntlrCondition,_A7:cpqFcaHostCntlrWorldWideName,'cpqFcaHostCntlrStorBoxList':cpqFcaHostCntlrStorBoxList,'cpqFcaHostCntlrOverallCondition':cpqFcaHostCntlrOverallCondition,'cpqFcaHostCntlrTapeCntlrList':cpqFcaHostCntlrTapeCntlrList,_Ar:cpqFcaHostCntlrSerialNumber,_Aq:cpqFcaHostCntlrHwLocation,_As:cpqFcaHostCntlrWorldWidePortName,'cpqFcaHostCntlrFirmwareVersion':cpqFcaHostCntlrFirmwareVersion,'cpqFcaHostCntlrOptionRomVersion':cpqFcaHostCntlrOptionRomVersion,'cpqFcaHostCntlrPciLocation':cpqFcaHostCntlrPciLocation,'cpqExtArrRsrcVol':cpqExtArrRsrcVol,'cpqExtArrRsrcVolTable':cpqExtArrRsrcVolTable,'cpqExtArrRsrcVolEntry':cpqExtArrRsrcVolEntry,_AR:cpqExtArrRsrcVolBoxIndex,_AS:cpqExtArrRsrcVolIndex,'cpqExtArrRsrcVolActiveInstances':cpqExtArrRsrcVolActiveInstances,'cpqExtArrRsrcVolDisabledInstances':cpqExtArrRsrcVolDisabledInstances,'cpqExtArrRsrcVolAllowCreation':cpqExtArrRsrcVolAllowCreation,'cpqExtArrRsrcVolVolumeId':cpqExtArrRsrcVolVolumeId,'cpqExtArrRsrcVolSourceVolumeId':cpqExtArrRsrcVolSourceVolumeId,'cpqExtArrRsrcVolTotalSpace':cpqExtArrRsrcVolTotalSpace,'cpqExtArrRsrcVolFreeActiveSpace':cpqExtArrRsrcVolFreeActiveSpace,'cpqExtArrRsrcVolFreeNewSpace':cpqExtArrRsrcVolFreeNewSpace,'cpqExtArrRsrcVolStatus':cpqExtArrRsrcVolStatus,'cpqExtArrSnapshot':cpqExtArrSnapshot,'cpqExtArrSnapshotTable':cpqExtArrSnapshotTable,'cpqExtArrSnapshotEntry':cpqExtArrSnapshotEntry,_AT:cpqExtArrSnapshotBoxIndex,_AU:cpqExtArrSnapshotRsrcVolIndex,_AV:cpqExtArrSnapshotIndex,'cpqExtArrSnapshotInstance':cpqExtArrSnapshotInstance,'cpqExtArrSnapshotUsedSpace':cpqExtArrSnapshotUsedSpace,'cpqExtArrSnapshotDateTime':cpqExtArrSnapshotDateTime,'cpqExtArrSnapshotType':cpqExtArrSnapshotType,'cpqExtArrSnapshotMounted':cpqExtArrSnapshotMounted,'cpqExtArrSnapshotAccess':cpqExtArrSnapshotAccess,'cpqFcTapeComponent':cpqFcTapeComponent,'cpqFcTapeCntlr':cpqFcTapeCntlr,'cpqFcTapeCntlrTable':cpqFcTapeCntlrTable,'cpqFcTapeCntlrEntry':cpqFcTapeCntlrEntry,_AW:cpqFcTapeCntlrIndex,_Ag:cpqFcTapeCntlrStatus,'cpqFcTapeCntlrCondition':cpqFcTapeCntlrCondition,'cpqFcTapeCntlrOverallCondition':cpqFcTapeCntlrOverallCondition,_Y:cpqFcTapeCntlrWWN,'cpqFcTapeCntlrFWRev':cpqFcTapeCntlrFWRev,'cpqFcTapeCntlrType':cpqFcTapeCntlrType,'cpqFcTapeCntlrModel':cpqFcTapeCntlrModel,'cpqFcTapeCntlrSerialNumber':cpqFcTapeCntlrSerialNumber,'cpqFcTapeLibrary':cpqFcTapeLibrary,'cpqFcTapeLibraryTable':cpqFcTapeLibraryTable,'cpqFcTapeLibraryEntry':cpqFcTapeLibraryEntry,_l:cpqFcTapeLibraryCntlrIndex,_Z:cpqFcTapeLibraryScsiBus,_a:cpqFcTapeLibraryScsiTarget,_b:cpqFcTapeLibraryScsiLun,_AA:cpqFcTapeLibrarySerialNumber,_A8:cpqFcTapeLibraryModel,_A9:cpqFcTapeLibraryFWRev,_A2:cpqFcTapeLibraryStatus,_A3:cpqFcTapeLibraryDoorStatus,'cpqFcTapeLibraryCondition':cpqFcTapeLibraryCondition,'cpqFcTapeLibraryOverallCondition':cpqFcTapeLibraryOverallCondition,'cpqFcTapeLibraryLastError':cpqFcTapeLibraryLastError,'cpqFcTapeLibraryStatHours':cpqFcTapeLibraryStatHours,'cpqFcTapeLibraryStatMoves':cpqFcTapeLibraryStatMoves,'cpqFcTapeLibraryDriveList':cpqFcTapeLibraryDriveList,_AB:cpqFcTapeLibraryLocation,'cpqFcTapeLibraryTemperature':cpqFcTapeLibraryTemperature,'cpqFcTapeLibraryRedundancy':cpqFcTapeLibraryRedundancy,'cpqFcTapeLibraryHotSwap':cpqFcTapeLibraryHotSwap,'cpqFcTapeDrive':cpqFcTapeDrive,'cpqFcTapeDriveTable':cpqFcTapeDriveTable,'cpqFcTapeDriveEntry':cpqFcTapeDriveEntry,_f:cpqFcTapeDriveCntlrIndex,_V:cpqFcTapeDriveScsiBus,_W:cpqFcTapeDriveScsiTarget,_X:cpqFcTapeDriveScsiLun,_r:cpqFcTapeDriveSerialNumber,_p:cpqFcTapeDriveModel,_q:cpqFcTapeDriveFWRev,'cpqFcTapeDriveType':cpqFcTapeDriveType,'cpqFcTapeDriveFWSubtype':cpqFcTapeDriveFWSubtype,_A4:cpqFcTapeDriveStatus,'cpqFcTapeDriveCleanReq':cpqFcTapeDriveCleanReq,'cpqFcTapeDriveCleanTapeRepl':cpqFcTapeDriveCleanTapeRepl,'cpqFcTapeDriveCondition':cpqFcTapeDriveCondition,'cpqFcTapeDriveCleanTapeCount':cpqFcTapeDriveCleanTapeCount,'cpqFcTapeDriveLibraryDrive':cpqFcTapeDriveLibraryDrive,_s:cpqFcTapeDriveLocation,'cpqFcTapeDriveHotPlug':cpqFcTapeDriveHotPlug,'cpqFcTapeDriveBay':cpqFcTapeDriveBay,'cpqFcTapeDriveCurrentWidth':cpqFcTapeDriveCurrentWidth,'cpqFcTapeDriveCurrentSpeed':cpqFcTapeDriveCurrentSpeed,'cpqFcTapeCounters':cpqFcTapeCounters,'cpqFcTapeCountersTable':cpqFcTapeCountersTable,'cpqFcTapeCountersEntry':cpqFcTapeCountersEntry,_AY:cpqFcTapeCountersCntlrIndex,_AZ:cpqFcTapeCountersScsiBus,_Aa:cpqFcTapeCountersScsiTarget,_Ab:cpqFcTapeCountersScsiLun,'cpqFcTapeCountersReWrites':cpqFcTapeCountersReWrites,'cpqFcTapeCountersReReads':cpqFcTapeCountersReReads,'cpqFcTapeCountersTotalErrors':cpqFcTapeCountersTotalErrors,'cpqFcTapeCountersTotalUncorrectable':cpqFcTapeCountersTotalUncorrectable,'cpqFcTapeCountersTotalBytes':cpqFcTapeCountersTotalBytes,'cpqFcSwitchComponent':cpqFcSwitchComponent,'cpqFcSwitch':cpqFcSwitch,'cpqFcSwitchTable':cpqFcSwitchTable,'cpqFcSwitchEntry':cpqFcSwitchEntry,_Ac:cpqFcSwitchIndex,'cpqFcSwitchLocation':cpqFcSwitchLocation,'cpqFcSwitchChassisIndex':cpqFcSwitchChassisIndex,'cpqFcSwitchChassisSlot':cpqFcSwitchChassisSlot,'cpqFcSwitchWorldWideNodeName':cpqFcSwitchWorldWideNodeName,'cpqFcSwitchWorldWidePortName':cpqFcSwitchWorldWidePortName,'cpqFcSwitchIpAddress':cpqFcSwitchIpAddress,'cpqFcSwitchIpGateway':cpqFcSwitchIpGateway,'cpqFcSwitchIpSubnet':cpqFcSwitchIpSubnet,'cpqFcSwitchName':cpqFcSwitchName,'cpqFcSwitchNetworkLinkStatus':cpqFcSwitchNetworkLinkStatus,'cpqFcSwitchFibreConnectStatus':cpqFcSwitchFibreConnectStatus,'cpqFcSwitchFWRev':cpqFcSwitchFWRev})