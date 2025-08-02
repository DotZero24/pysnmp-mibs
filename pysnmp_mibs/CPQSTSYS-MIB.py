_Af='cpqSsBoxGSIMessages'
_Ae='cpqSsBoxGSIStatus'
_Ad='cpqSsBoxLocalManageIpAddress'
_Ac='cpqSsBoxTargetSasAddress'
_Ab='cpqSsBoxConnectionStatus'
_Aa='cpqSsChassisRsoStatus'
_AZ='cpqSsBackplaneFtpsStatus'
_AY='cpqSsBackplaneTempStatus'
_AX='cpqSsBackplaneFanStatus'
_AW='cpqSsPowerSupplyFirmwareRevision'
_AV='cpqSsPowerSupplyBoardRevision'
_AU='cpqSsPowerSupplySerialNumber'
_AT='cpqSsFanModuleBoardRevision'
_AS='cpqSsFanModuleSerialNumber'
_AR='cpqSsTempSensorCurrentValue'
_AQ='cpqSsTempSensorStatus'
_AP='cpqSsTempSensorLocation'
_AO='cpqSsPowerSupplyUpsStatus'
_AN='cpqSsRaidSystemIndex'
_AM='cpqSsSidePanelRemoved'
_AL='cpqSsSidePanelInPlace'
_AK='cpqSsTempOk'
_AJ='cpqSsTempDegraded'
_AI='cpqSsTempFailed'
_AH='cpqSs2FanStatusChange'
_AG='cpqSsFanStatusChange'
_AF='cpqSsTrapLogIndex'
_AE='cpqSsDrvBoxPathIndex'
_AD='cpqSsDrvBoxPathBoxIndex'
_AC='cpqSsDrvBoxPathCntlrIndex'
_AB='cpqSsScsiAttachmentIndex'
_AA='cpqSsFibreAttachmentIndex'
_A9='cpqSsBackplaneChassisIndex'
_A8='cpqSsTempSensorIndex'
_A7='cpqSsTempSensorChassisIndex'
_A6='cpqSsFanModuleIndex'
_A5='cpqSsFanModuleChassisIndex'
_A4='composite'
_A3='cpqSsPowerSupplyIndex'
_A2='cpqSsPowerSupplyChassisIndex'
_A1='cpqSsIoSlotIndex'
_A0='cpqSsIoSlotChassisIndex'
_z='ultra3'
_y='duplexBottom'
_x='duplexTop'
_w='notDuplexed'
_v='external'
_u='internal'
_t='noFltTolPower'
_s='noTemp'
_r='proLiant2'
_q='proLiant'
_p='NotificationType'
_o='OctetString'
_n='cpqSsPowerSupplyStatus'
_m='cpqSsFanModuleStatus'
_l='cpqSsFanModuleLocation'
_k='cpqSsChassisIndex'
_j='sasAttached'
_i='scsiAttached'
_h='cpqSsBackplaneSerialNumber'
_g='cpqSsBackplaneModel'
_f='cpqSsBackplaneVendor'
_e='cpqSsPowerSupplyBay'
_d='cpqSsBoxFltTolPwrSupplyStatus'
_c='notInstalled'
_b='cpqSsBoxSidePanelStatus'
_a='cpqSsBackplaneIndex'
_Z='notSupported'
_Y='cpqSsBoxLocationString'
_X='cpqSsBoxFanStatus'
_W='deprecated'
_V='cpqSsBoxSerialNumber'
_U='cpqSsBoxModel'
_T='cpqSsBoxVendor'
_S='cpqSsBoxCntlrHwLocation'
_R='cpqSsBoxTempStatus'
_Q='cpqSsBoxBusIndex'
_P='cpqSsBoxCntlrIndex'
_O='cpqSsChassisTime'
_N='cpqSsChassisName'
_M='sysName'
_L='SNMPv2-MIB'
_K='cpqHoTrapFlags'
_J='CPQHOST-MIB'
_I='failed'
_H='degraded'
_G='ok'
_F='DisplayString'
_E='other'
_D='Integer32'
_C='read-only'
_B='CPQSTSYS-MIB'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_o,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,cpqHoTrapFlags=mibBuilder.importSymbols(_J,'compaq',_K)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_L,_M)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_p,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_p,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
_CpqSsStorageSys_ObjectIdentity=ObjectIdentity
cpqSsStorageSys=_CpqSsStorageSys_ObjectIdentity((1,3,6,1,4,1,232,8))
_CpqSsMibRev_ObjectIdentity=ObjectIdentity
cpqSsMibRev=_CpqSsMibRev_ObjectIdentity((1,3,6,1,4,1,232,8,1))
class _CpqSsMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqSsMibRevMajor_Type.__name__=_D
_CpqSsMibRevMajor_Object=MibScalar
cpqSsMibRevMajor=_CpqSsMibRevMajor_Object((1,3,6,1,4,1,232,8,1,1),_CpqSsMibRevMajor_Type())
cpqSsMibRevMajor.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsMibRevMajor.setStatus(_A)
class _CpqSsMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSsMibRevMinor_Type.__name__=_D
_CpqSsMibRevMinor_Object=MibScalar
cpqSsMibRevMinor=_CpqSsMibRevMinor_Object((1,3,6,1,4,1,232,8,1,2),_CpqSsMibRevMinor_Type())
cpqSsMibRevMinor.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsMibRevMinor.setStatus(_A)
class _CpqSsMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),(_I,4)))
_CpqSsMibCondition_Type.__name__=_D
_CpqSsMibCondition_Object=MibScalar
cpqSsMibCondition=_CpqSsMibCondition_Object((1,3,6,1,4,1,232,8,1,3),_CpqSsMibCondition_Type())
cpqSsMibCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsMibCondition.setStatus(_A)
_CpqSsDrvBox_ObjectIdentity=ObjectIdentity
cpqSsDrvBox=_CpqSsDrvBox_ObjectIdentity((1,3,6,1,4,1,232,8,2))
_CpqSsDrvBoxTable_Object=MibTable
cpqSsDrvBoxTable=_CpqSsDrvBoxTable_Object((1,3,6,1,4,1,232,8,2,1))
if mibBuilder.loadTexts:cpqSsDrvBoxTable.setStatus(_A)
_CpqSsDrvBoxEntry_Object=MibTableRow
cpqSsDrvBoxEntry=_CpqSsDrvBoxEntry_Object((1,3,6,1,4,1,232,8,2,1,1))
cpqSsDrvBoxEntry.setIndexNames((0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:cpqSsDrvBoxEntry.setStatus(_A)
_CpqSsBoxCntlrIndex_Type=Integer32
_CpqSsBoxCntlrIndex_Object=MibTableColumn
cpqSsBoxCntlrIndex=_CpqSsBoxCntlrIndex_Object((1,3,6,1,4,1,232,8,2,1,1,1),_CpqSsBoxCntlrIndex_Type())
cpqSsBoxCntlrIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxCntlrIndex.setStatus(_A)
class _CpqSsBoxBusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSsBoxBusIndex_Type.__name__=_D
_CpqSsBoxBusIndex_Object=MibTableColumn
cpqSsBoxBusIndex=_CpqSsBoxBusIndex_Object((1,3,6,1,4,1,232,8,2,1,1,2),_CpqSsBoxBusIndex_Type())
cpqSsBoxBusIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxBusIndex.setStatus(_A)
class _CpqSsBoxType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,1),(_q,2),(_r,3),('proLiant2Internal',4),('proLiant2DuplexTop',5),('proLiant2DuplexBottom',6),('proLiant2InternalDuplexTop',7),('proLiant2InternalDuplexBottom',8)))
_CpqSsBoxType_Type.__name__=_D
_CpqSsBoxType_Object=MibTableColumn
cpqSsBoxType=_CpqSsBoxType_Object((1,3,6,1,4,1,232,8,2,1,1,3),_CpqSsBoxType_Type())
cpqSsBoxType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxType.setStatus(_W)
class _CpqSsBoxModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_CpqSsBoxModel_Type.__name__=_F
_CpqSsBoxModel_Object=MibTableColumn
cpqSsBoxModel=_CpqSsBoxModel_Object((1,3,6,1,4,1,232,8,2,1,1,4),_CpqSsBoxModel_Type())
cpqSsBoxModel.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxModel.setStatus(_A)
class _CpqSsBoxFWRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqSsBoxFWRev_Type.__name__=_F
_CpqSsBoxFWRev_Object=MibTableColumn
cpqSsBoxFWRev=_CpqSsBoxFWRev_Object((1,3,6,1,4,1,232,8,2,1,1,5),_CpqSsBoxFWRev_Type())
cpqSsBoxFWRev.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxFWRev.setStatus(_A)
class _CpqSsBoxVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_CpqSsBoxVendor_Type.__name__=_F
_CpqSsBoxVendor_Object=MibTableColumn
cpqSsBoxVendor=_CpqSsBoxVendor_Object((1,3,6,1,4,1,232,8,2,1,1,6),_CpqSsBoxVendor_Type())
cpqSsBoxVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxVendor.setStatus(_A)
class _CpqSsBoxFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_G,2),(_I,3),('noFan',4),(_H,5)))
_CpqSsBoxFanStatus_Type.__name__=_D
_CpqSsBoxFanStatus_Object=MibTableColumn
cpqSsBoxFanStatus=_CpqSsBoxFanStatus_Object((1,3,6,1,4,1,232,8,2,1,1,7),_CpqSsBoxFanStatus_Type())
cpqSsBoxFanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxFanStatus.setStatus(_A)
class _CpqSsBoxCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),(_I,4)))
_CpqSsBoxCondition_Type.__name__=_D
_CpqSsBoxCondition_Object=MibTableColumn
cpqSsBoxCondition=_CpqSsBoxCondition_Object((1,3,6,1,4,1,232,8,2,1,1,8),_CpqSsBoxCondition_Type())
cpqSsBoxCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxCondition.setStatus(_A)
class _CpqSsBoxTempStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),(_I,4),(_s,5)))
_CpqSsBoxTempStatus_Type.__name__=_D
_CpqSsBoxTempStatus_Object=MibTableColumn
cpqSsBoxTempStatus=_CpqSsBoxTempStatus_Object((1,3,6,1,4,1,232,8,2,1,1,9),_CpqSsBoxTempStatus_Type())
cpqSsBoxTempStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxTempStatus.setStatus(_A)
class _CpqSsBoxSidePanelStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('sidePanelInPlace',2),('sidePanelRemoved',3),('noSidePanelStatus',4)))
_CpqSsBoxSidePanelStatus_Type.__name__=_D
_CpqSsBoxSidePanelStatus_Object=MibTableColumn
cpqSsBoxSidePanelStatus=_CpqSsBoxSidePanelStatus_Object((1,3,6,1,4,1,232,8,2,1,1,10),_CpqSsBoxSidePanelStatus_Type())
cpqSsBoxSidePanelStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxSidePanelStatus.setStatus(_A)
class _CpqSsBoxFltTolPwrSupplyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),(_I,4),(_t,5)))
_CpqSsBoxFltTolPwrSupplyStatus_Type.__name__=_D
_CpqSsBoxFltTolPwrSupplyStatus_Object=MibTableColumn
cpqSsBoxFltTolPwrSupplyStatus=_CpqSsBoxFltTolPwrSupplyStatus_Object((1,3,6,1,4,1,232,8,2,1,1,11),_CpqSsBoxFltTolPwrSupplyStatus_Type())
cpqSsBoxFltTolPwrSupplyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxFltTolPwrSupplyStatus.setStatus(_A)
class _CpqSsBoxBackPlaneVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_q,2),(_r,3),('proLiant3',4),('proLiant4',5),('proLiant5',6)))
_CpqSsBoxBackPlaneVersion_Type.__name__=_D
_CpqSsBoxBackPlaneVersion_Object=MibTableColumn
cpqSsBoxBackPlaneVersion=_CpqSsBoxBackPlaneVersion_Object((1,3,6,1,4,1,232,8,2,1,1,12),_CpqSsBoxBackPlaneVersion_Type())
cpqSsBoxBackPlaneVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxBackPlaneVersion.setStatus(_A)
_CpqSsBoxTotalBays_Type=Integer32
_CpqSsBoxTotalBays_Object=MibTableColumn
cpqSsBoxTotalBays=_CpqSsBoxTotalBays_Object((1,3,6,1,4,1,232,8,2,1,1,13),_CpqSsBoxTotalBays_Type())
cpqSsBoxTotalBays.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxTotalBays.setStatus(_A)
class _CpqSsBoxPlacement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_u,2),(_v,3)))
_CpqSsBoxPlacement_Type.__name__=_D
_CpqSsBoxPlacement_Object=MibTableColumn
cpqSsBoxPlacement=_CpqSsBoxPlacement_Object((1,3,6,1,4,1,232,8,2,1,1,14),_CpqSsBoxPlacement_Type())
cpqSsBoxPlacement.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxPlacement.setStatus(_A)
class _CpqSsBoxDuplexOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_w,2),(_x,3),(_y,4)))
_CpqSsBoxDuplexOption_Type.__name__=_D
_CpqSsBoxDuplexOption_Object=MibTableColumn
cpqSsBoxDuplexOption=_CpqSsBoxDuplexOption_Object((1,3,6,1,4,1,232,8,2,1,1,15),_CpqSsBoxDuplexOption_Type())
cpqSsBoxDuplexOption.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxDuplexOption.setStatus(_A)
_CpqSsBoxBoardRevision_Type=Integer32
_CpqSsBoxBoardRevision_Object=MibTableColumn
cpqSsBoxBoardRevision=_CpqSsBoxBoardRevision_Object((1,3,6,1,4,1,232,8,2,1,1,16),_CpqSsBoxBoardRevision_Type())
cpqSsBoxBoardRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxBoardRevision.setStatus(_A)
class _CpqSsBoxSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_CpqSsBoxSerialNumber_Type.__name__=_F
_CpqSsBoxSerialNumber_Object=MibTableColumn
cpqSsBoxSerialNumber=_CpqSsBoxSerialNumber_Object((1,3,6,1,4,1,232,8,2,1,1,17),_CpqSsBoxSerialNumber_Type())
cpqSsBoxSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxSerialNumber.setStatus(_A)
class _CpqSsBoxCntlrHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSsBoxCntlrHwLocation_Type.__name__=_F
_CpqSsBoxCntlrHwLocation_Object=MibTableColumn
cpqSsBoxCntlrHwLocation=_CpqSsBoxCntlrHwLocation_Object((1,3,6,1,4,1,232,8,2,1,1,18),_CpqSsBoxCntlrHwLocation_Type())
cpqSsBoxCntlrHwLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxCntlrHwLocation.setStatus(_A)
class _CpqSsBoxBackplaneSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_z,2),('ultra320',3)))
_CpqSsBoxBackplaneSpeed_Type.__name__=_D
_CpqSsBoxBackplaneSpeed_Object=MibTableColumn
cpqSsBoxBackplaneSpeed=_CpqSsBoxBackplaneSpeed_Object((1,3,6,1,4,1,232,8,2,1,1,19),_CpqSsBoxBackplaneSpeed_Type())
cpqSsBoxBackplaneSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxBackplaneSpeed.setStatus(_A)
class _CpqSsBoxConnectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_i,2),(_j,3),('sataAttached',4)))
_CpqSsBoxConnectionType_Type.__name__=_D
_CpqSsBoxConnectionType_Object=MibTableColumn
cpqSsBoxConnectionType=_CpqSsBoxConnectionType_Object((1,3,6,1,4,1,232,8,2,1,1,20),_CpqSsBoxConnectionType_Type())
cpqSsBoxConnectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxConnectionType.setStatus(_A)
class _CpqSsBoxHostConnector_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_CpqSsBoxHostConnector_Type.__name__=_F
_CpqSsBoxHostConnector_Object=MibTableColumn
cpqSsBoxHostConnector=_CpqSsBoxHostConnector_Object((1,3,6,1,4,1,232,8,2,1,1,21),_CpqSsBoxHostConnector_Type())
cpqSsBoxHostConnector.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxHostConnector.setStatus(_A)
_CpqSsBoxBoxOnConnector_Type=Integer32
_CpqSsBoxBoxOnConnector_Object=MibTableColumn
cpqSsBoxBoxOnConnector=_CpqSsBoxBoxOnConnector_Object((1,3,6,1,4,1,232,8,2,1,1,22),_CpqSsBoxBoxOnConnector_Type())
cpqSsBoxBoxOnConnector.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxBoxOnConnector.setStatus(_A)
class _CpqSsBoxLocationString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSsBoxLocationString_Type.__name__=_F
_CpqSsBoxLocationString_Object=MibTableColumn
cpqSsBoxLocationString=_CpqSsBoxLocationString_Object((1,3,6,1,4,1,232,8,2,1,1,23),_CpqSsBoxLocationString_Type())
cpqSsBoxLocationString.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxLocationString.setStatus(_A)
class _CpqSsBoxInitiatorSasAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CpqSsBoxInitiatorSasAddress_Type.__name__=_F
_CpqSsBoxInitiatorSasAddress_Object=MibTableColumn
cpqSsBoxInitiatorSasAddress=_CpqSsBoxInitiatorSasAddress_Object((1,3,6,1,4,1,232,8,2,1,1,24),_CpqSsBoxInitiatorSasAddress_Type())
cpqSsBoxInitiatorSasAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxInitiatorSasAddress.setStatus(_A)
class _CpqSsBoxTargetSasAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CpqSsBoxTargetSasAddress_Type.__name__=_F
_CpqSsBoxTargetSasAddress_Object=MibTableColumn
cpqSsBoxTargetSasAddress=_CpqSsBoxTargetSasAddress_Object((1,3,6,1,4,1,232,8,2,1,1,25),_CpqSsBoxTargetSasAddress_Type())
cpqSsBoxTargetSasAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxTargetSasAddress.setStatus(_A)
class _CpqSsBoxLocalManageIpAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqSsBoxLocalManageIpAddress_Type.__name__=_F
_CpqSsBoxLocalManageIpAddress_Object=MibTableColumn
cpqSsBoxLocalManageIpAddress=_CpqSsBoxLocalManageIpAddress_Object((1,3,6,1,4,1,232,8,2,1,1,26),_CpqSsBoxLocalManageIpAddress_Type())
cpqSsBoxLocalManageIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxLocalManageIpAddress.setStatus(_A)
class _CpqSsBoxPartnerManageIpAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqSsBoxPartnerManageIpAddress_Type.__name__=_F
_CpqSsBoxPartnerManageIpAddress_Object=MibTableColumn
cpqSsBoxPartnerManageIpAddress=_CpqSsBoxPartnerManageIpAddress_Object((1,3,6,1,4,1,232,8,2,1,1,27),_CpqSsBoxPartnerManageIpAddress_Type())
cpqSsBoxPartnerManageIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxPartnerManageIpAddress.setStatus(_A)
class _CpqSsBoxConnectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_Z,2),('connected',3),('notConnected',4)))
_CpqSsBoxConnectionStatus_Type.__name__=_D
_CpqSsBoxConnectionStatus_Object=MibTableColumn
cpqSsBoxConnectionStatus=_CpqSsBoxConnectionStatus_Object((1,3,6,1,4,1,232,8,2,1,1,28),_CpqSsBoxConnectionStatus_Type())
cpqSsBoxConnectionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxConnectionStatus.setStatus(_A)
class _CpqSsBoxTargetBasedManagement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('tbmNotSupported',2),('tbmSupported',3)))
_CpqSsBoxTargetBasedManagement_Type.__name__=_D
_CpqSsBoxTargetBasedManagement_Object=MibTableColumn
cpqSsBoxTargetBasedManagement=_CpqSsBoxTargetBasedManagement_Object((1,3,6,1,4,1,232,8,2,1,1,29),_CpqSsBoxTargetBasedManagement_Type())
cpqSsBoxTargetBasedManagement.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxTargetBasedManagement.setStatus(_A)
class _CpqSsBoxGSIStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),(_I,4)))
_CpqSsBoxGSIStatus_Type.__name__=_D
_CpqSsBoxGSIStatus_Object=MibTableColumn
cpqSsBoxGSIStatus=_CpqSsBoxGSIStatus_Object((1,3,6,1,4,1,232,8,2,1,1,30),_CpqSsBoxGSIStatus_Type())
cpqSsBoxGSIStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxGSIStatus.setStatus(_A)
class _CpqSsBoxGSIMessages_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,511))
_CpqSsBoxGSIMessages_Type.__name__=_F
_CpqSsBoxGSIMessages_Object=MibTableColumn
cpqSsBoxGSIMessages=_CpqSsBoxGSIMessages_Object((1,3,6,1,4,1,232,8,2,1,1,31),_CpqSsBoxGSIMessages_Type())
cpqSsBoxGSIMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBoxGSIMessages.setStatus(_A)
_CpqSsBoxExtended_ObjectIdentity=ObjectIdentity
cpqSsBoxExtended=_CpqSsBoxExtended_ObjectIdentity((1,3,6,1,4,1,232,8,2,2))
_CpqSsChassisTable_Object=MibTable
cpqSsChassisTable=_CpqSsChassisTable_Object((1,3,6,1,4,1,232,8,2,2,1))
if mibBuilder.loadTexts:cpqSsChassisTable.setStatus(_A)
_CpqSsChassisEntry_Object=MibTableRow
cpqSsChassisEntry=_CpqSsChassisEntry_Object((1,3,6,1,4,1,232,8,2,2,1,1))
cpqSsChassisEntry.setIndexNames((0,_B,_k))
if mibBuilder.loadTexts:cpqSsChassisEntry.setStatus(_A)
class _CpqSsChassisIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSsChassisIndex_Type.__name__=_D
_CpqSsChassisIndex_Object=MibTableColumn
cpqSsChassisIndex=_CpqSsChassisIndex_Object((1,3,6,1,4,1,232,8,2,2,1,1,1),_CpqSsChassisIndex_Type())
cpqSsChassisIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisIndex.setStatus(_A)
class _CpqSsChassisConnectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('fibreAttached',2),(_i,3),('iScsiAttached',4),(_j,5)))
_CpqSsChassisConnectionType_Type.__name__=_D
_CpqSsChassisConnectionType_Object=MibTableColumn
cpqSsChassisConnectionType=_CpqSsChassisConnectionType_Object((1,3,6,1,4,1,232,8,2,2,1,1,2),_CpqSsChassisConnectionType_Type())
cpqSsChassisConnectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisConnectionType.setStatus(_A)
class _CpqSsChassisSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CpqSsChassisSerialNumber_Type.__name__=_F
_CpqSsChassisSerialNumber_Object=MibTableColumn
cpqSsChassisSerialNumber=_CpqSsChassisSerialNumber_Object((1,3,6,1,4,1,232,8,2,2,1,1,3),_CpqSsChassisSerialNumber_Type())
cpqSsChassisSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisSerialNumber.setStatus(_A)
class _CpqSsChassisName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CpqSsChassisName_Type.__name__=_F
_CpqSsChassisName_Object=MibTableColumn
cpqSsChassisName=_CpqSsChassisName_Object((1,3,6,1,4,1,232,8,2,2,1,1,4),_CpqSsChassisName_Type())
cpqSsChassisName.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisName.setStatus(_A)
class _CpqSsChassisSystemBoardSerNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_CpqSsChassisSystemBoardSerNum_Type.__name__=_F
_CpqSsChassisSystemBoardSerNum_Object=MibTableColumn
cpqSsChassisSystemBoardSerNum=_CpqSsChassisSystemBoardSerNum_Object((1,3,6,1,4,1,232,8,2,2,1,1,5),_CpqSsChassisSystemBoardSerNum_Type())
cpqSsChassisSystemBoardSerNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisSystemBoardSerNum.setStatus(_A)
class _CpqSsChassisSystemBoardRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqSsChassisSystemBoardRev_Type.__name__=_F
_CpqSsChassisSystemBoardRev_Object=MibTableColumn
cpqSsChassisSystemBoardRev=_CpqSsChassisSystemBoardRev_Object((1,3,6,1,4,1,232,8,2,2,1,1,6),_CpqSsChassisSystemBoardRev_Type())
cpqSsChassisSystemBoardRev.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisSystemBoardRev.setStatus(_A)
class _CpqSsChassisPowerBoardSerNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_CpqSsChassisPowerBoardSerNum_Type.__name__=_F
_CpqSsChassisPowerBoardSerNum_Object=MibTableColumn
cpqSsChassisPowerBoardSerNum=_CpqSsChassisPowerBoardSerNum_Object((1,3,6,1,4,1,232,8,2,2,1,1,7),_CpqSsChassisPowerBoardSerNum_Type())
cpqSsChassisPowerBoardSerNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisPowerBoardSerNum.setStatus(_A)
class _CpqSsChassisPowerBoardRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqSsChassisPowerBoardRev_Type.__name__=_F
_CpqSsChassisPowerBoardRev_Object=MibTableColumn
cpqSsChassisPowerBoardRev=_CpqSsChassisPowerBoardRev_Object((1,3,6,1,4,1,232,8,2,2,1,1,8),_CpqSsChassisPowerBoardRev_Type())
cpqSsChassisPowerBoardRev.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisPowerBoardRev.setStatus(_A)
class _CpqSsChassisScsiBoardSerNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_CpqSsChassisScsiBoardSerNum_Type.__name__=_F
_CpqSsChassisScsiBoardSerNum_Object=MibTableColumn
cpqSsChassisScsiBoardSerNum=_CpqSsChassisScsiBoardSerNum_Object((1,3,6,1,4,1,232,8,2,2,1,1,9),_CpqSsChassisScsiBoardSerNum_Type())
cpqSsChassisScsiBoardSerNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisScsiBoardSerNum.setStatus(_A)
class _CpqSsChassisScsiBoardRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqSsChassisScsiBoardRev_Type.__name__=_F
_CpqSsChassisScsiBoardRev_Object=MibTableColumn
cpqSsChassisScsiBoardRev=_CpqSsChassisScsiBoardRev_Object((1,3,6,1,4,1,232,8,2,2,1,1,10),_CpqSsChassisScsiBoardRev_Type())
cpqSsChassisScsiBoardRev.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisScsiBoardRev.setStatus(_A)
class _CpqSsChassisOverallCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),(_I,4)))
_CpqSsChassisOverallCondition_Type.__name__=_D
_CpqSsChassisOverallCondition_Object=MibTableColumn
cpqSsChassisOverallCondition=_CpqSsChassisOverallCondition_Object((1,3,6,1,4,1,232,8,2,2,1,1,11),_CpqSsChassisOverallCondition_Type())
cpqSsChassisOverallCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisOverallCondition.setStatus(_A)
class _CpqSsChassisPowerSupplyCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),(_I,4)))
_CpqSsChassisPowerSupplyCondition_Type.__name__=_D
_CpqSsChassisPowerSupplyCondition_Object=MibTableColumn
cpqSsChassisPowerSupplyCondition=_CpqSsChassisPowerSupplyCondition_Object((1,3,6,1,4,1,232,8,2,2,1,1,12),_CpqSsChassisPowerSupplyCondition_Type())
cpqSsChassisPowerSupplyCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisPowerSupplyCondition.setStatus(_A)
class _CpqSsChassisFanCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),(_I,4)))
_CpqSsChassisFanCondition_Type.__name__=_D
_CpqSsChassisFanCondition_Object=MibTableColumn
cpqSsChassisFanCondition=_CpqSsChassisFanCondition_Object((1,3,6,1,4,1,232,8,2,2,1,1,13),_CpqSsChassisFanCondition_Type())
cpqSsChassisFanCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisFanCondition.setStatus(_A)
class _CpqSsChassisTemperatureCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),(_I,4)))
_CpqSsChassisTemperatureCondition_Type.__name__=_D
_CpqSsChassisTemperatureCondition_Object=MibTableColumn
cpqSsChassisTemperatureCondition=_CpqSsChassisTemperatureCondition_Object((1,3,6,1,4,1,232,8,2,2,1,1,14),_CpqSsChassisTemperatureCondition_Type())
cpqSsChassisTemperatureCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisTemperatureCondition.setStatus(_A)
class _CpqSsChassisFcaCntlrCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),(_I,4)))
_CpqSsChassisFcaCntlrCondition_Type.__name__=_D
_CpqSsChassisFcaCntlrCondition_Object=MibTableColumn
cpqSsChassisFcaCntlrCondition=_CpqSsChassisFcaCntlrCondition_Object((1,3,6,1,4,1,232,8,2,2,1,1,15),_CpqSsChassisFcaCntlrCondition_Type())
cpqSsChassisFcaCntlrCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisFcaCntlrCondition.setStatus(_A)
class _CpqSsChassisFcaLogicalDriveCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),(_I,4)))
_CpqSsChassisFcaLogicalDriveCondition_Type.__name__=_D
_CpqSsChassisFcaLogicalDriveCondition_Object=MibTableColumn
cpqSsChassisFcaLogicalDriveCondition=_CpqSsChassisFcaLogicalDriveCondition_Object((1,3,6,1,4,1,232,8,2,2,1,1,16),_CpqSsChassisFcaLogicalDriveCondition_Type())
cpqSsChassisFcaLogicalDriveCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisFcaLogicalDriveCondition.setStatus(_A)
class _CpqSsChassisFcaPhysDrvCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),(_I,4)))
_CpqSsChassisFcaPhysDrvCondition_Type.__name__=_D
_CpqSsChassisFcaPhysDrvCondition_Object=MibTableColumn
cpqSsChassisFcaPhysDrvCondition=_CpqSsChassisFcaPhysDrvCondition_Object((1,3,6,1,4,1,232,8,2,2,1,1,17),_CpqSsChassisFcaPhysDrvCondition_Type())
cpqSsChassisFcaPhysDrvCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisFcaPhysDrvCondition.setStatus(_A)
_CpqSsChassisTime_Type=Integer32
_CpqSsChassisTime_Object=MibTableColumn
cpqSsChassisTime=_CpqSsChassisTime_Object((1,3,6,1,4,1,232,8,2,2,1,1,18),_CpqSsChassisTime_Type())
cpqSsChassisTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisTime.setStatus(_A)
class _CpqSsChassisModel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_E,1),('ra4x00',2),('msa1000',3),('smartArrayClusterStorage',4),('enterpriseModularArray',5),('enterpriseVirtualArray',6),('msa500G2',7),('msa20',8),('msa1500cs',9),('msa1510i',10)))
_CpqSsChassisModel_Type.__name__=_D
_CpqSsChassisModel_Object=MibTableColumn
cpqSsChassisModel=_CpqSsChassisModel_Object((1,3,6,1,4,1,232,8,2,2,1,1,19),_CpqSsChassisModel_Type())
cpqSsChassisModel.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisModel.setStatus(_A)
class _CpqSsChassisBackplaneCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),(_I,4)))
_CpqSsChassisBackplaneCondition_Type.__name__=_D
_CpqSsChassisBackplaneCondition_Object=MibTableColumn
cpqSsChassisBackplaneCondition=_CpqSsChassisBackplaneCondition_Object((1,3,6,1,4,1,232,8,2,2,1,1,20),_CpqSsChassisBackplaneCondition_Type())
cpqSsChassisBackplaneCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisBackplaneCondition.setStatus(_A)
class _CpqSsChassisFcaTapeDrvCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),(_I,4)))
_CpqSsChassisFcaTapeDrvCondition_Type.__name__=_D
_CpqSsChassisFcaTapeDrvCondition_Object=MibTableColumn
cpqSsChassisFcaTapeDrvCondition=_CpqSsChassisFcaTapeDrvCondition_Object((1,3,6,1,4,1,232,8,2,2,1,1,21),_CpqSsChassisFcaTapeDrvCondition_Type())
cpqSsChassisFcaTapeDrvCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisFcaTapeDrvCondition.setStatus(_A)
class _CpqSsChassisRsoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_E,1),(_Z,2),('notConfigured',3),('disabled',4),('daemonDownDisabled',5),(_G,6),('daemonDownActive',7),('noSecondary',8),('daemonDownNoSecondary',9),('linkDown',10),('daemonDownLinkDown',11),('secondaryRunningAuto',12),('secondaryRunningUser',13),('evTimeoutError',14)))
_CpqSsChassisRsoStatus_Type.__name__=_D
_CpqSsChassisRsoStatus_Object=MibTableColumn
cpqSsChassisRsoStatus=_CpqSsChassisRsoStatus_Object((1,3,6,1,4,1,232,8,2,2,1,1,22),_CpqSsChassisRsoStatus_Type())
cpqSsChassisRsoStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisRsoStatus.setStatus(_A)
class _CpqSsChassisRsoCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),(_I,4)))
_CpqSsChassisRsoCondition_Type.__name__=_D
_CpqSsChassisRsoCondition_Object=MibTableColumn
cpqSsChassisRsoCondition=_CpqSsChassisRsoCondition_Object((1,3,6,1,4,1,232,8,2,2,1,1,23),_CpqSsChassisRsoCondition_Type())
cpqSsChassisRsoCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisRsoCondition.setStatus(_A)
class _CpqSsChassisScsiIoModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),('io2port',2),('io4portUpgradeFirmware',3),('io4port',4),('io2port320',5),('io4port320',6),('io1port320',7)))
_CpqSsChassisScsiIoModuleType_Type.__name__=_D
_CpqSsChassisScsiIoModuleType_Object=MibTableColumn
cpqSsChassisScsiIoModuleType=_CpqSsChassisScsiIoModuleType_Object((1,3,6,1,4,1,232,8,2,2,1,1,24),_CpqSsChassisScsiIoModuleType_Type())
cpqSsChassisScsiIoModuleType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisScsiIoModuleType.setStatus(_A)
class _CpqSsChassisPreferredPathMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('notActiveActive',2),('automatic',3),('manual',4)))
_CpqSsChassisPreferredPathMode_Type.__name__=_D
_CpqSsChassisPreferredPathMode_Object=MibTableColumn
cpqSsChassisPreferredPathMode=_CpqSsChassisPreferredPathMode_Object((1,3,6,1,4,1,232,8,2,2,1,1,25),_CpqSsChassisPreferredPathMode_Type())
cpqSsChassisPreferredPathMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisPreferredPathMode.setStatus(_A)
class _CpqSsChassisProductId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CpqSsChassisProductId_Type.__name__=_F
_CpqSsChassisProductId_Object=MibTableColumn
cpqSsChassisProductId=_CpqSsChassisProductId_Object((1,3,6,1,4,1,232,8,2,2,1,1,26),_CpqSsChassisProductId_Type())
cpqSsChassisProductId.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsChassisProductId.setStatus(_A)
_CpqSsIoSlotTable_Object=MibTable
cpqSsIoSlotTable=_CpqSsIoSlotTable_Object((1,3,6,1,4,1,232,8,2,2,2))
if mibBuilder.loadTexts:cpqSsIoSlotTable.setStatus(_A)
_CpqSsIoSlotEntry_Object=MibTableRow
cpqSsIoSlotEntry=_CpqSsIoSlotEntry_Object((1,3,6,1,4,1,232,8,2,2,2,1))
cpqSsIoSlotEntry.setIndexNames((0,_B,_A0),(0,_B,_A1))
if mibBuilder.loadTexts:cpqSsIoSlotEntry.setStatus(_A)
class _CpqSsIoSlotChassisIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSsIoSlotChassisIndex_Type.__name__=_D
_CpqSsIoSlotChassisIndex_Object=MibTableColumn
cpqSsIoSlotChassisIndex=_CpqSsIoSlotChassisIndex_Object((1,3,6,1,4,1,232,8,2,2,2,1,1),_CpqSsIoSlotChassisIndex_Type())
cpqSsIoSlotChassisIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsIoSlotChassisIndex.setStatus(_A)
_CpqSsIoSlotIndex_Type=Integer32
_CpqSsIoSlotIndex_Object=MibTableColumn
cpqSsIoSlotIndex=_CpqSsIoSlotIndex_Object((1,3,6,1,4,1,232,8,2,2,2,1,2),_CpqSsIoSlotIndex_Type())
cpqSsIoSlotIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsIoSlotIndex.setStatus(_A)
class _CpqSsIoSlotControllerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,1),(_c,2),('unknownBoard',3),('fibreArray',4),('scsiArray',5),('noSlot',6),('iScsiArray',7),('sasArray',8)))
_CpqSsIoSlotControllerType_Type.__name__=_D
_CpqSsIoSlotControllerType_Object=MibTableColumn
cpqSsIoSlotControllerType=_CpqSsIoSlotControllerType_Object((1,3,6,1,4,1,232,8,2,2,2,1,3),_CpqSsIoSlotControllerType_Type())
cpqSsIoSlotControllerType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsIoSlotControllerType.setStatus(_A)
_CpqSsPowerSupplyTable_Object=MibTable
cpqSsPowerSupplyTable=_CpqSsPowerSupplyTable_Object((1,3,6,1,4,1,232,8,2,2,3))
if mibBuilder.loadTexts:cpqSsPowerSupplyTable.setStatus(_A)
_CpqSsPowerSupplyEntry_Object=MibTableRow
cpqSsPowerSupplyEntry=_CpqSsPowerSupplyEntry_Object((1,3,6,1,4,1,232,8,2,2,3,1))
cpqSsPowerSupplyEntry.setIndexNames((0,_B,_A2),(0,_B,_A3))
if mibBuilder.loadTexts:cpqSsPowerSupplyEntry.setStatus(_A)
class _CpqSsPowerSupplyChassisIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSsPowerSupplyChassisIndex_Type.__name__=_D
_CpqSsPowerSupplyChassisIndex_Object=MibTableColumn
cpqSsPowerSupplyChassisIndex=_CpqSsPowerSupplyChassisIndex_Object((1,3,6,1,4,1,232,8,2,2,3,1,1),_CpqSsPowerSupplyChassisIndex_Type())
cpqSsPowerSupplyChassisIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsPowerSupplyChassisIndex.setStatus(_A)
_CpqSsPowerSupplyIndex_Type=Integer32
_CpqSsPowerSupplyIndex_Object=MibTableColumn
cpqSsPowerSupplyIndex=_CpqSsPowerSupplyIndex_Object((1,3,6,1,4,1,232,8,2,2,3,1,2),_CpqSsPowerSupplyIndex_Type())
cpqSsPowerSupplyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsPowerSupplyIndex.setStatus(_A)
class _CpqSsPowerSupplyBay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('powerBay1',2),('powerBay2',3),(_A4,4)))
_CpqSsPowerSupplyBay_Type.__name__=_D
_CpqSsPowerSupplyBay_Object=MibTableColumn
cpqSsPowerSupplyBay=_CpqSsPowerSupplyBay_Object((1,3,6,1,4,1,232,8,2,2,3,1,3),_CpqSsPowerSupplyBay_Type())
cpqSsPowerSupplyBay.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsPowerSupplyBay.setStatus(_A)
class _CpqSsPowerSupplyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_c,2),(_G,3),(_I,4),(_H,5)))
_CpqSsPowerSupplyStatus_Type.__name__=_D
_CpqSsPowerSupplyStatus_Object=MibTableColumn
cpqSsPowerSupplyStatus=_CpqSsPowerSupplyStatus_Object((1,3,6,1,4,1,232,8,2,2,3,1,4),_CpqSsPowerSupplyStatus_Type())
cpqSsPowerSupplyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsPowerSupplyStatus.setStatus(_A)
class _CpqSsPowerSupplyUpsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('noUps',2),(_G,3),('powerFailed',4),('batteryLow',5)))
_CpqSsPowerSupplyUpsStatus_Type.__name__=_D
_CpqSsPowerSupplyUpsStatus_Object=MibTableColumn
cpqSsPowerSupplyUpsStatus=_CpqSsPowerSupplyUpsStatus_Object((1,3,6,1,4,1,232,8,2,2,3,1,5),_CpqSsPowerSupplyUpsStatus_Type())
cpqSsPowerSupplyUpsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsPowerSupplyUpsStatus.setStatus(_A)
class _CpqSsPowerSupplyCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),(_I,4)))
_CpqSsPowerSupplyCondition_Type.__name__=_D
_CpqSsPowerSupplyCondition_Object=MibTableColumn
cpqSsPowerSupplyCondition=_CpqSsPowerSupplyCondition_Object((1,3,6,1,4,1,232,8,2,2,3,1,6),_CpqSsPowerSupplyCondition_Type())
cpqSsPowerSupplyCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsPowerSupplyCondition.setStatus(_A)
class _CpqSsPowerSupplySerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_CpqSsPowerSupplySerialNumber_Type.__name__=_F
_CpqSsPowerSupplySerialNumber_Object=MibTableColumn
cpqSsPowerSupplySerialNumber=_CpqSsPowerSupplySerialNumber_Object((1,3,6,1,4,1,232,8,2,2,3,1,7),_CpqSsPowerSupplySerialNumber_Type())
cpqSsPowerSupplySerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsPowerSupplySerialNumber.setStatus(_A)
class _CpqSsPowerSupplyBoardRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqSsPowerSupplyBoardRevision_Type.__name__=_F
_CpqSsPowerSupplyBoardRevision_Object=MibTableColumn
cpqSsPowerSupplyBoardRevision=_CpqSsPowerSupplyBoardRevision_Object((1,3,6,1,4,1,232,8,2,2,3,1,8),_CpqSsPowerSupplyBoardRevision_Type())
cpqSsPowerSupplyBoardRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsPowerSupplyBoardRevision.setStatus(_A)
class _CpqSsPowerSupplyFirmwareRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqSsPowerSupplyFirmwareRevision_Type.__name__=_F
_CpqSsPowerSupplyFirmwareRevision_Object=MibTableColumn
cpqSsPowerSupplyFirmwareRevision=_CpqSsPowerSupplyFirmwareRevision_Object((1,3,6,1,4,1,232,8,2,2,3,1,9),_CpqSsPowerSupplyFirmwareRevision_Type())
cpqSsPowerSupplyFirmwareRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsPowerSupplyFirmwareRevision.setStatus(_A)
_CpqSsFanModuleTable_Object=MibTable
cpqSsFanModuleTable=_CpqSsFanModuleTable_Object((1,3,6,1,4,1,232,8,2,2,4))
if mibBuilder.loadTexts:cpqSsFanModuleTable.setStatus(_A)
_CpqSsFanModuleEntry_Object=MibTableRow
cpqSsFanModuleEntry=_CpqSsFanModuleEntry_Object((1,3,6,1,4,1,232,8,2,2,4,1))
cpqSsFanModuleEntry.setIndexNames((0,_B,_A5),(0,_B,_A6))
if mibBuilder.loadTexts:cpqSsFanModuleEntry.setStatus(_A)
class _CpqSsFanModuleChassisIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSsFanModuleChassisIndex_Type.__name__=_D
_CpqSsFanModuleChassisIndex_Object=MibTableColumn
cpqSsFanModuleChassisIndex=_CpqSsFanModuleChassisIndex_Object((1,3,6,1,4,1,232,8,2,2,4,1,1),_CpqSsFanModuleChassisIndex_Type())
cpqSsFanModuleChassisIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsFanModuleChassisIndex.setStatus(_A)
_CpqSsFanModuleIndex_Type=Integer32
_CpqSsFanModuleIndex_Object=MibTableColumn
cpqSsFanModuleIndex=_CpqSsFanModuleIndex_Object((1,3,6,1,4,1,232,8,2,2,4,1,2),_CpqSsFanModuleIndex_Type())
cpqSsFanModuleIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsFanModuleIndex.setStatus(_A)
class _CpqSsFanModuleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_c,2),(_G,3),(_H,4),(_I,5)))
_CpqSsFanModuleStatus_Type.__name__=_D
_CpqSsFanModuleStatus_Object=MibTableColumn
cpqSsFanModuleStatus=_CpqSsFanModuleStatus_Object((1,3,6,1,4,1,232,8,2,2,4,1,3),_CpqSsFanModuleStatus_Type())
cpqSsFanModuleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsFanModuleStatus.setStatus(_A)
class _CpqSsFanModuleCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),(_I,4)))
_CpqSsFanModuleCondition_Type.__name__=_D
_CpqSsFanModuleCondition_Object=MibTableColumn
cpqSsFanModuleCondition=_CpqSsFanModuleCondition_Object((1,3,6,1,4,1,232,8,2,2,4,1,4),_CpqSsFanModuleCondition_Type())
cpqSsFanModuleCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsFanModuleCondition.setStatus(_A)
class _CpqSsFanModuleLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('fanBay',2),(_A4,3),('fanBay2',4)))
_CpqSsFanModuleLocation_Type.__name__=_D
_CpqSsFanModuleLocation_Object=MibTableColumn
cpqSsFanModuleLocation=_CpqSsFanModuleLocation_Object((1,3,6,1,4,1,232,8,2,2,4,1,5),_CpqSsFanModuleLocation_Type())
cpqSsFanModuleLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsFanModuleLocation.setStatus(_A)
class _CpqSsFanModuleSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_CpqSsFanModuleSerialNumber_Type.__name__=_F
_CpqSsFanModuleSerialNumber_Object=MibTableColumn
cpqSsFanModuleSerialNumber=_CpqSsFanModuleSerialNumber_Object((1,3,6,1,4,1,232,8,2,2,4,1,6),_CpqSsFanModuleSerialNumber_Type())
cpqSsFanModuleSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsFanModuleSerialNumber.setStatus(_A)
class _CpqSsFanModuleBoardRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqSsFanModuleBoardRevision_Type.__name__=_F
_CpqSsFanModuleBoardRevision_Object=MibTableColumn
cpqSsFanModuleBoardRevision=_CpqSsFanModuleBoardRevision_Object((1,3,6,1,4,1,232,8,2,2,4,1,7),_CpqSsFanModuleBoardRevision_Type())
cpqSsFanModuleBoardRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsFanModuleBoardRevision.setStatus(_A)
_CpqSsTempSensorTable_Object=MibTable
cpqSsTempSensorTable=_CpqSsTempSensorTable_Object((1,3,6,1,4,1,232,8,2,2,5))
if mibBuilder.loadTexts:cpqSsTempSensorTable.setStatus(_A)
_CpqSsTempSensorEntry_Object=MibTableRow
cpqSsTempSensorEntry=_CpqSsTempSensorEntry_Object((1,3,6,1,4,1,232,8,2,2,5,1))
cpqSsTempSensorEntry.setIndexNames((0,_B,_A7),(0,_B,_A8))
if mibBuilder.loadTexts:cpqSsTempSensorEntry.setStatus(_A)
class _CpqSsTempSensorChassisIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSsTempSensorChassisIndex_Type.__name__=_D
_CpqSsTempSensorChassisIndex_Object=MibTableColumn
cpqSsTempSensorChassisIndex=_CpqSsTempSensorChassisIndex_Object((1,3,6,1,4,1,232,8,2,2,5,1,1),_CpqSsTempSensorChassisIndex_Type())
cpqSsTempSensorChassisIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsTempSensorChassisIndex.setStatus(_A)
_CpqSsTempSensorIndex_Type=Integer32
_CpqSsTempSensorIndex_Object=MibTableColumn
cpqSsTempSensorIndex=_CpqSsTempSensorIndex_Object((1,3,6,1,4,1,232,8,2,2,5,1,2),_CpqSsTempSensorIndex_Type())
cpqSsTempSensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsTempSensorIndex.setStatus(_A)
class _CpqSsTempSensorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),(_I,4)))
_CpqSsTempSensorStatus_Type.__name__=_D
_CpqSsTempSensorStatus_Object=MibTableColumn
cpqSsTempSensorStatus=_CpqSsTempSensorStatus_Object((1,3,6,1,4,1,232,8,2,2,5,1,3),_CpqSsTempSensorStatus_Type())
cpqSsTempSensorStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsTempSensorStatus.setStatus(_A)
class _CpqSsTempSensorCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),(_I,4)))
_CpqSsTempSensorCondition_Type.__name__=_D
_CpqSsTempSensorCondition_Object=MibTableColumn
cpqSsTempSensorCondition=_CpqSsTempSensorCondition_Object((1,3,6,1,4,1,232,8,2,2,5,1,4),_CpqSsTempSensorCondition_Type())
cpqSsTempSensorCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsTempSensorCondition.setStatus(_A)
class _CpqSsTempSensorLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('fanBay',2),('backplane',3)))
_CpqSsTempSensorLocation_Type.__name__=_D
_CpqSsTempSensorLocation_Object=MibTableColumn
cpqSsTempSensorLocation=_CpqSsTempSensorLocation_Object((1,3,6,1,4,1,232,8,2,2,5,1,5),_CpqSsTempSensorLocation_Type())
cpqSsTempSensorLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsTempSensorLocation.setStatus(_A)
_CpqSsTempSensorCurrentValue_Type=Integer32
_CpqSsTempSensorCurrentValue_Object=MibTableColumn
cpqSsTempSensorCurrentValue=_CpqSsTempSensorCurrentValue_Object((1,3,6,1,4,1,232,8,2,2,5,1,6),_CpqSsTempSensorCurrentValue_Type())
cpqSsTempSensorCurrentValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsTempSensorCurrentValue.setStatus(_A)
_CpqSsTempSensorLimitValue_Type=Integer32
_CpqSsTempSensorLimitValue_Object=MibTableColumn
cpqSsTempSensorLimitValue=_CpqSsTempSensorLimitValue_Object((1,3,6,1,4,1,232,8,2,2,5,1,7),_CpqSsTempSensorLimitValue_Type())
cpqSsTempSensorLimitValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsTempSensorLimitValue.setStatus(_A)
_CpqSsTempSensorHysteresisValue_Type=Integer32
_CpqSsTempSensorHysteresisValue_Object=MibTableColumn
cpqSsTempSensorHysteresisValue=_CpqSsTempSensorHysteresisValue_Object((1,3,6,1,4,1,232,8,2,2,5,1,8),_CpqSsTempSensorHysteresisValue_Type())
cpqSsTempSensorHysteresisValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsTempSensorHysteresisValue.setStatus(_A)
_CpqSsBackplaneTable_Object=MibTable
cpqSsBackplaneTable=_CpqSsBackplaneTable_Object((1,3,6,1,4,1,232,8,2,2,6))
if mibBuilder.loadTexts:cpqSsBackplaneTable.setStatus(_A)
_CpqSsBackplaneEntry_Object=MibTableRow
cpqSsBackplaneEntry=_CpqSsBackplaneEntry_Object((1,3,6,1,4,1,232,8,2,2,6,1))
cpqSsBackplaneEntry.setIndexNames((0,_B,_A9),(0,_B,_a))
if mibBuilder.loadTexts:cpqSsBackplaneEntry.setStatus(_A)
class _CpqSsBackplaneChassisIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSsBackplaneChassisIndex_Type.__name__=_D
_CpqSsBackplaneChassisIndex_Object=MibTableColumn
cpqSsBackplaneChassisIndex=_CpqSsBackplaneChassisIndex_Object((1,3,6,1,4,1,232,8,2,2,6,1,1),_CpqSsBackplaneChassisIndex_Type())
cpqSsBackplaneChassisIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBackplaneChassisIndex.setStatus(_A)
class _CpqSsBackplaneIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSsBackplaneIndex_Type.__name__=_D
_CpqSsBackplaneIndex_Object=MibTableColumn
cpqSsBackplaneIndex=_CpqSsBackplaneIndex_Object((1,3,6,1,4,1,232,8,2,2,6,1,2),_CpqSsBackplaneIndex_Type())
cpqSsBackplaneIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBackplaneIndex.setStatus(_A)
class _CpqSsBackplaneFWRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CpqSsBackplaneFWRev_Type.__name__=_F
_CpqSsBackplaneFWRev_Object=MibTableColumn
cpqSsBackplaneFWRev=_CpqSsBackplaneFWRev_Object((1,3,6,1,4,1,232,8,2,2,6,1,3),_CpqSsBackplaneFWRev_Type())
cpqSsBackplaneFWRev.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBackplaneFWRev.setStatus(_A)
class _CpqSsBackplaneDriveBays_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSsBackplaneDriveBays_Type.__name__=_D
_CpqSsBackplaneDriveBays_Object=MibTableColumn
cpqSsBackplaneDriveBays=_CpqSsBackplaneDriveBays_Object((1,3,6,1,4,1,232,8,2,2,6,1,4),_CpqSsBackplaneDriveBays_Type())
cpqSsBackplaneDriveBays.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBackplaneDriveBays.setStatus(_A)
class _CpqSsBackplaneDuplexOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_w,2),(_x,3),(_y,4)))
_CpqSsBackplaneDuplexOption_Type.__name__=_D
_CpqSsBackplaneDuplexOption_Object=MibTableColumn
cpqSsBackplaneDuplexOption=_CpqSsBackplaneDuplexOption_Object((1,3,6,1,4,1,232,8,2,2,6,1,5),_CpqSsBackplaneDuplexOption_Type())
cpqSsBackplaneDuplexOption.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBackplaneDuplexOption.setStatus(_A)
class _CpqSsBackplaneCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),(_I,4)))
_CpqSsBackplaneCondition_Type.__name__=_D
_CpqSsBackplaneCondition_Object=MibTableColumn
cpqSsBackplaneCondition=_CpqSsBackplaneCondition_Object((1,3,6,1,4,1,232,8,2,2,6,1,6),_CpqSsBackplaneCondition_Type())
cpqSsBackplaneCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBackplaneCondition.setStatus(_A)
_CpqSsBackplaneVersion_Type=Integer32
_CpqSsBackplaneVersion_Object=MibTableColumn
cpqSsBackplaneVersion=_CpqSsBackplaneVersion_Object((1,3,6,1,4,1,232,8,2,2,6,1,7),_CpqSsBackplaneVersion_Type())
cpqSsBackplaneVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBackplaneVersion.setStatus(_A)
class _CpqSsBackplaneVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_CpqSsBackplaneVendor_Type.__name__=_F
_CpqSsBackplaneVendor_Object=MibTableColumn
cpqSsBackplaneVendor=_CpqSsBackplaneVendor_Object((1,3,6,1,4,1,232,8,2,2,6,1,8),_CpqSsBackplaneVendor_Type())
cpqSsBackplaneVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBackplaneVendor.setStatus(_A)
class _CpqSsBackplaneModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_CpqSsBackplaneModel_Type.__name__=_F
_CpqSsBackplaneModel_Object=MibTableColumn
cpqSsBackplaneModel=_CpqSsBackplaneModel_Object((1,3,6,1,4,1,232,8,2,2,6,1,9),_CpqSsBackplaneModel_Type())
cpqSsBackplaneModel.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBackplaneModel.setStatus(_A)
class _CpqSsBackplaneFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,1),(_c,2),(_G,3),(_H,4),(_I,5),(_Z,6),('degraded-Fan1Failed',7),('degraded-Fan2Failed',8)))
_CpqSsBackplaneFanStatus_Type.__name__=_D
_CpqSsBackplaneFanStatus_Object=MibTableColumn
cpqSsBackplaneFanStatus=_CpqSsBackplaneFanStatus_Object((1,3,6,1,4,1,232,8,2,2,6,1,10),_CpqSsBackplaneFanStatus_Type())
cpqSsBackplaneFanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBackplaneFanStatus.setStatus(_A)
class _CpqSsBackplaneTempStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_s,2),(_G,3),(_H,4),(_I,5),(_Z,6)))
_CpqSsBackplaneTempStatus_Type.__name__=_D
_CpqSsBackplaneTempStatus_Object=MibTableColumn
cpqSsBackplaneTempStatus=_CpqSsBackplaneTempStatus_Object((1,3,6,1,4,1,232,8,2,2,6,1,11),_CpqSsBackplaneTempStatus_Type())
cpqSsBackplaneTempStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBackplaneTempStatus.setStatus(_A)
class _CpqSsBackplaneFtpsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,1),(_t,2),(_G,3),(_H,4),(_I,5),(_Z,6),('noFltTolPower-Bay1Missing',7),('noFltTolPower-Bay2Missing',8)))
_CpqSsBackplaneFtpsStatus_Type.__name__=_D
_CpqSsBackplaneFtpsStatus_Object=MibTableColumn
cpqSsBackplaneFtpsStatus=_CpqSsBackplaneFtpsStatus_Object((1,3,6,1,4,1,232,8,2,2,6,1,12),_CpqSsBackplaneFtpsStatus_Type())
cpqSsBackplaneFtpsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBackplaneFtpsStatus.setStatus(_A)
class _CpqSsBackplaneSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_CpqSsBackplaneSerialNumber_Type.__name__=_F
_CpqSsBackplaneSerialNumber_Object=MibTableColumn
cpqSsBackplaneSerialNumber=_CpqSsBackplaneSerialNumber_Object((1,3,6,1,4,1,232,8,2,2,6,1,13),_CpqSsBackplaneSerialNumber_Type())
cpqSsBackplaneSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBackplaneSerialNumber.setStatus(_A)
class _CpqSsBackplanePlacement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_u,2),(_v,3)))
_CpqSsBackplanePlacement_Type.__name__=_D
_CpqSsBackplanePlacement_Object=MibTableColumn
cpqSsBackplanePlacement=_CpqSsBackplanePlacement_Object((1,3,6,1,4,1,232,8,2,2,6,1,14),_CpqSsBackplanePlacement_Type())
cpqSsBackplanePlacement.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBackplanePlacement.setStatus(_A)
_CpqSsBackplaneBoardRevision_Type=Integer32
_CpqSsBackplaneBoardRevision_Object=MibTableColumn
cpqSsBackplaneBoardRevision=_CpqSsBackplaneBoardRevision_Object((1,3,6,1,4,1,232,8,2,2,6,1,15),_CpqSsBackplaneBoardRevision_Type())
cpqSsBackplaneBoardRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBackplaneBoardRevision.setStatus(_A)
class _CpqSsBackplaneSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_z,2),('ultra320',3),('sata',4)))
_CpqSsBackplaneSpeed_Type.__name__=_D
_CpqSsBackplaneSpeed_Object=MibTableColumn
cpqSsBackplaneSpeed=_CpqSsBackplaneSpeed_Object((1,3,6,1,4,1,232,8,2,2,6,1,16),_CpqSsBackplaneSpeed_Type())
cpqSsBackplaneSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBackplaneSpeed.setStatus(_A)
class _CpqSsBackplaneConnectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_i,2),(_j,3)))
_CpqSsBackplaneConnectionType_Type.__name__=_D
_CpqSsBackplaneConnectionType_Object=MibTableColumn
cpqSsBackplaneConnectionType=_CpqSsBackplaneConnectionType_Object((1,3,6,1,4,1,232,8,2,2,6,1,17),_CpqSsBackplaneConnectionType_Type())
cpqSsBackplaneConnectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBackplaneConnectionType.setStatus(_A)
class _CpqSsBackplaneConnector_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_CpqSsBackplaneConnector_Type.__name__=_F
_CpqSsBackplaneConnector_Object=MibTableColumn
cpqSsBackplaneConnector=_CpqSsBackplaneConnector_Object((1,3,6,1,4,1,232,8,2,2,6,1,18),_CpqSsBackplaneConnector_Type())
cpqSsBackplaneConnector.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBackplaneConnector.setStatus(_A)
_CpqSsBackplaneOnConnector_Type=Integer32
_CpqSsBackplaneOnConnector_Object=MibTableColumn
cpqSsBackplaneOnConnector=_CpqSsBackplaneOnConnector_Object((1,3,6,1,4,1,232,8,2,2,6,1,19),_CpqSsBackplaneOnConnector_Type())
cpqSsBackplaneOnConnector.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBackplaneOnConnector.setStatus(_A)
class _CpqSsBackplaneLocationString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSsBackplaneLocationString_Type.__name__=_F
_CpqSsBackplaneLocationString_Object=MibTableColumn
cpqSsBackplaneLocationString=_CpqSsBackplaneLocationString_Object((1,3,6,1,4,1,232,8,2,2,6,1,20),_CpqSsBackplaneLocationString_Type())
cpqSsBackplaneLocationString.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsBackplaneLocationString.setStatus(_A)
_CpqSsFibreAttachmentTable_Object=MibTable
cpqSsFibreAttachmentTable=_CpqSsFibreAttachmentTable_Object((1,3,6,1,4,1,232,8,2,2,7))
if mibBuilder.loadTexts:cpqSsFibreAttachmentTable.setStatus(_A)
_CpqSsFibreAttachmentEntry_Object=MibTableRow
cpqSsFibreAttachmentEntry=_CpqSsFibreAttachmentEntry_Object((1,3,6,1,4,1,232,8,2,2,7,1))
cpqSsFibreAttachmentEntry.setIndexNames((0,_B,_AA))
if mibBuilder.loadTexts:cpqSsFibreAttachmentEntry.setStatus(_A)
_CpqSsFibreAttachmentIndex_Type=Integer32
_CpqSsFibreAttachmentIndex_Object=MibTableColumn
cpqSsFibreAttachmentIndex=_CpqSsFibreAttachmentIndex_Object((1,3,6,1,4,1,232,8,2,2,7,1,1),_CpqSsFibreAttachmentIndex_Type())
cpqSsFibreAttachmentIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsFibreAttachmentIndex.setStatus(_A)
_CpqSsFibreAttachmentHostControllerIndex_Type=Integer32
_CpqSsFibreAttachmentHostControllerIndex_Object=MibTableColumn
cpqSsFibreAttachmentHostControllerIndex=_CpqSsFibreAttachmentHostControllerIndex_Object((1,3,6,1,4,1,232,8,2,2,7,1,2),_CpqSsFibreAttachmentHostControllerIndex_Type())
cpqSsFibreAttachmentHostControllerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsFibreAttachmentHostControllerIndex.setStatus(_A)
class _CpqSsFibreAttachmentHostControllerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSsFibreAttachmentHostControllerPort_Type.__name__=_D
_CpqSsFibreAttachmentHostControllerPort_Object=MibTableColumn
cpqSsFibreAttachmentHostControllerPort=_CpqSsFibreAttachmentHostControllerPort_Object((1,3,6,1,4,1,232,8,2,2,7,1,3),_CpqSsFibreAttachmentHostControllerPort_Type())
cpqSsFibreAttachmentHostControllerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsFibreAttachmentHostControllerPort.setStatus(_A)
class _CpqSsFibreAttachmentDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('storageBox',2),('tapeController',3),('fibreChannelSwitch',4)))
_CpqSsFibreAttachmentDeviceType_Type.__name__=_D
_CpqSsFibreAttachmentDeviceType_Object=MibTableColumn
cpqSsFibreAttachmentDeviceType=_CpqSsFibreAttachmentDeviceType_Object((1,3,6,1,4,1,232,8,2,2,7,1,4),_CpqSsFibreAttachmentDeviceType_Type())
cpqSsFibreAttachmentDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsFibreAttachmentDeviceType.setStatus(_A)
class _CpqSsFibreAttachmentDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSsFibreAttachmentDeviceIndex_Type.__name__=_D
_CpqSsFibreAttachmentDeviceIndex_Object=MibTableColumn
cpqSsFibreAttachmentDeviceIndex=_CpqSsFibreAttachmentDeviceIndex_Object((1,3,6,1,4,1,232,8,2,2,7,1,5),_CpqSsFibreAttachmentDeviceIndex_Type())
cpqSsFibreAttachmentDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsFibreAttachmentDeviceIndex.setStatus(_A)
class _CpqSsFibreAttachmentDevicePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSsFibreAttachmentDevicePort_Type.__name__=_D
_CpqSsFibreAttachmentDevicePort_Object=MibTableColumn
cpqSsFibreAttachmentDevicePort=_CpqSsFibreAttachmentDevicePort_Object((1,3,6,1,4,1,232,8,2,2,7,1,6),_CpqSsFibreAttachmentDevicePort_Type())
cpqSsFibreAttachmentDevicePort.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsFibreAttachmentDevicePort.setStatus(_A)
_CpqSsScsiAttachmentTable_Object=MibTable
cpqSsScsiAttachmentTable=_CpqSsScsiAttachmentTable_Object((1,3,6,1,4,1,232,8,2,2,8))
if mibBuilder.loadTexts:cpqSsScsiAttachmentTable.setStatus(_A)
_CpqSsScsiAttachmentEntry_Object=MibTableRow
cpqSsScsiAttachmentEntry=_CpqSsScsiAttachmentEntry_Object((1,3,6,1,4,1,232,8,2,2,8,1))
cpqSsScsiAttachmentEntry.setIndexNames((0,_B,_AB))
if mibBuilder.loadTexts:cpqSsScsiAttachmentEntry.setStatus(_A)
_CpqSsScsiAttachmentIndex_Type=Integer32
_CpqSsScsiAttachmentIndex_Object=MibTableColumn
cpqSsScsiAttachmentIndex=_CpqSsScsiAttachmentIndex_Object((1,3,6,1,4,1,232,8,2,2,8,1,1),_CpqSsScsiAttachmentIndex_Type())
cpqSsScsiAttachmentIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsScsiAttachmentIndex.setStatus(_A)
class _CpqSsScsiAttachmentControllerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSsScsiAttachmentControllerIndex_Type.__name__=_D
_CpqSsScsiAttachmentControllerIndex_Object=MibTableColumn
cpqSsScsiAttachmentControllerIndex=_CpqSsScsiAttachmentControllerIndex_Object((1,3,6,1,4,1,232,8,2,2,8,1,2),_CpqSsScsiAttachmentControllerIndex_Type())
cpqSsScsiAttachmentControllerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsScsiAttachmentControllerIndex.setStatus(_A)
class _CpqSsScsiAttachmentControllerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSsScsiAttachmentControllerPort_Type.__name__=_D
_CpqSsScsiAttachmentControllerPort_Object=MibTableColumn
cpqSsScsiAttachmentControllerPort=_CpqSsScsiAttachmentControllerPort_Object((1,3,6,1,4,1,232,8,2,2,8,1,3),_CpqSsScsiAttachmentControllerPort_Type())
cpqSsScsiAttachmentControllerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsScsiAttachmentControllerPort.setStatus(_A)
class _CpqSsScsiAttachmentControllerTarget_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSsScsiAttachmentControllerTarget_Type.__name__=_D
_CpqSsScsiAttachmentControllerTarget_Object=MibTableColumn
cpqSsScsiAttachmentControllerTarget=_CpqSsScsiAttachmentControllerTarget_Object((1,3,6,1,4,1,232,8,2,2,8,1,4),_CpqSsScsiAttachmentControllerTarget_Type())
cpqSsScsiAttachmentControllerTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsScsiAttachmentControllerTarget.setStatus(_A)
class _CpqSsScsiAttachmentControllerLun_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSsScsiAttachmentControllerLun_Type.__name__=_D
_CpqSsScsiAttachmentControllerLun_Object=MibTableColumn
cpqSsScsiAttachmentControllerLun=_CpqSsScsiAttachmentControllerLun_Object((1,3,6,1,4,1,232,8,2,2,8,1,5),_CpqSsScsiAttachmentControllerLun_Type())
cpqSsScsiAttachmentControllerLun.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsScsiAttachmentControllerLun.setStatus(_A)
class _CpqSsScsiAttachmentChassisIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSsScsiAttachmentChassisIndex_Type.__name__=_D
_CpqSsScsiAttachmentChassisIndex_Object=MibTableColumn
cpqSsScsiAttachmentChassisIndex=_CpqSsScsiAttachmentChassisIndex_Object((1,3,6,1,4,1,232,8,2,2,8,1,6),_CpqSsScsiAttachmentChassisIndex_Type())
cpqSsScsiAttachmentChassisIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsScsiAttachmentChassisIndex.setStatus(_A)
class _CpqSsScsiAttachmentChassisIoSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSsScsiAttachmentChassisIoSlot_Type.__name__=_D
_CpqSsScsiAttachmentChassisIoSlot_Object=MibTableColumn
cpqSsScsiAttachmentChassisIoSlot=_CpqSsScsiAttachmentChassisIoSlot_Object((1,3,6,1,4,1,232,8,2,2,8,1,7),_CpqSsScsiAttachmentChassisIoSlot_Type())
cpqSsScsiAttachmentChassisIoSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsScsiAttachmentChassisIoSlot.setStatus(_A)
class _CpqSsScsiAttachmentPathStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),('offline',3)))
_CpqSsScsiAttachmentPathStatus_Type.__name__=_D
_CpqSsScsiAttachmentPathStatus_Object=MibTableColumn
cpqSsScsiAttachmentPathStatus=_CpqSsScsiAttachmentPathStatus_Object((1,3,6,1,4,1,232,8,2,2,8,1,8),_CpqSsScsiAttachmentPathStatus_Type())
cpqSsScsiAttachmentPathStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsScsiAttachmentPathStatus.setStatus(_A)
class _CpqSsScsiAttachmentPathCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),(_I,4)))
_CpqSsScsiAttachmentPathCondition_Type.__name__=_D
_CpqSsScsiAttachmentPathCondition_Object=MibTableColumn
cpqSsScsiAttachmentPathCondition=_CpqSsScsiAttachmentPathCondition_Object((1,3,6,1,4,1,232,8,2,2,8,1,9),_CpqSsScsiAttachmentPathCondition_Type())
cpqSsScsiAttachmentPathCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsScsiAttachmentPathCondition.setStatus(_A)
_CpqSsDrvBoxPathTable_Object=MibTable
cpqSsDrvBoxPathTable=_CpqSsDrvBoxPathTable_Object((1,3,6,1,4,1,232,8,2,3))
if mibBuilder.loadTexts:cpqSsDrvBoxPathTable.setStatus(_A)
_CpqSsDrvBoxPathEntry_Object=MibTableRow
cpqSsDrvBoxPathEntry=_CpqSsDrvBoxPathEntry_Object((1,3,6,1,4,1,232,8,2,3,1))
cpqSsDrvBoxPathEntry.setIndexNames((0,_B,_AC),(0,_B,_AD),(0,_B,_AE))
if mibBuilder.loadTexts:cpqSsDrvBoxPathEntry.setStatus(_A)
_CpqSsDrvBoxPathCntlrIndex_Type=Integer32
_CpqSsDrvBoxPathCntlrIndex_Object=MibTableColumn
cpqSsDrvBoxPathCntlrIndex=_CpqSsDrvBoxPathCntlrIndex_Object((1,3,6,1,4,1,232,8,2,3,1,1),_CpqSsDrvBoxPathCntlrIndex_Type())
cpqSsDrvBoxPathCntlrIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsDrvBoxPathCntlrIndex.setStatus(_A)
_CpqSsDrvBoxPathBoxIndex_Type=Integer32
_CpqSsDrvBoxPathBoxIndex_Object=MibTableColumn
cpqSsDrvBoxPathBoxIndex=_CpqSsDrvBoxPathBoxIndex_Object((1,3,6,1,4,1,232,8,2,3,1,2),_CpqSsDrvBoxPathBoxIndex_Type())
cpqSsDrvBoxPathBoxIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsDrvBoxPathBoxIndex.setStatus(_A)
_CpqSsDrvBoxPathIndex_Type=Integer32
_CpqSsDrvBoxPathIndex_Object=MibTableColumn
cpqSsDrvBoxPathIndex=_CpqSsDrvBoxPathIndex_Object((1,3,6,1,4,1,232,8,2,3,1,3),_CpqSsDrvBoxPathIndex_Type())
cpqSsDrvBoxPathIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsDrvBoxPathIndex.setStatus(_A)
class _CpqSsDrvBoxPathStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_G,2),('linkDown',3)))
_CpqSsDrvBoxPathStatus_Type.__name__=_D
_CpqSsDrvBoxPathStatus_Object=MibTableColumn
cpqSsDrvBoxPathStatus=_CpqSsDrvBoxPathStatus_Object((1,3,6,1,4,1,232,8,2,3,1,4),_CpqSsDrvBoxPathStatus_Type())
cpqSsDrvBoxPathStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsDrvBoxPathStatus.setStatus(_A)
class _CpqSsDrvBoxPathCurrentRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('active',2),('alternate',3)))
_CpqSsDrvBoxPathCurrentRole_Type.__name__=_D
_CpqSsDrvBoxPathCurrentRole_Object=MibTableColumn
cpqSsDrvBoxPathCurrentRole=_CpqSsDrvBoxPathCurrentRole_Object((1,3,6,1,4,1,232,8,2,3,1,5),_CpqSsDrvBoxPathCurrentRole_Type())
cpqSsDrvBoxPathCurrentRole.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsDrvBoxPathCurrentRole.setStatus(_A)
class _CpqSsDrvBoxPathHostConnector_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_CpqSsDrvBoxPathHostConnector_Type.__name__=_F
_CpqSsDrvBoxPathHostConnector_Object=MibTableColumn
cpqSsDrvBoxPathHostConnector=_CpqSsDrvBoxPathHostConnector_Object((1,3,6,1,4,1,232,8,2,3,1,6),_CpqSsDrvBoxPathHostConnector_Type())
cpqSsDrvBoxPathHostConnector.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsDrvBoxPathHostConnector.setStatus(_A)
_CpqSsDrvBoxPathBoxOnConnector_Type=Integer32
_CpqSsDrvBoxPathBoxOnConnector_Object=MibTableColumn
cpqSsDrvBoxPathBoxOnConnector=_CpqSsDrvBoxPathBoxOnConnector_Object((1,3,6,1,4,1,232,8,2,3,1,7),_CpqSsDrvBoxPathBoxOnConnector_Type())
cpqSsDrvBoxPathBoxOnConnector.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsDrvBoxPathBoxOnConnector.setStatus(_A)
class _CpqSsDrvBoxPathLocationString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSsDrvBoxPathLocationString_Type.__name__=_F
_CpqSsDrvBoxPathLocationString_Object=MibTableColumn
cpqSsDrvBoxPathLocationString=_CpqSsDrvBoxPathLocationString_Object((1,3,6,1,4,1,232,8,2,3,1,8),_CpqSsDrvBoxPathLocationString_Type())
cpqSsDrvBoxPathLocationString.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsDrvBoxPathLocationString.setStatus(_A)
_CpqSsTrap_ObjectIdentity=ObjectIdentity
cpqSsTrap=_CpqSsTrap_ObjectIdentity((1,3,6,1,4,1,232,8,3))
_CpqSsTrapPkts_Type=Counter32
_CpqSsTrapPkts_Object=MibScalar
cpqSsTrapPkts=_CpqSsTrapPkts_Object((1,3,6,1,4,1,232,8,3,1),_CpqSsTrapPkts_Type())
cpqSsTrapPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsTrapPkts.setStatus(_W)
class _CpqSsTrapLogMaxSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqSsTrapLogMaxSize_Type.__name__=_D
_CpqSsTrapLogMaxSize_Object=MibScalar
cpqSsTrapLogMaxSize=_CpqSsTrapLogMaxSize_Object((1,3,6,1,4,1,232,8,3,2),_CpqSsTrapLogMaxSize_Type())
cpqSsTrapLogMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsTrapLogMaxSize.setStatus(_W)
_CpqSsTrapLogTable_Object=MibTable
cpqSsTrapLogTable=_CpqSsTrapLogTable_Object((1,3,6,1,4,1,232,8,3,3))
if mibBuilder.loadTexts:cpqSsTrapLogTable.setStatus(_W)
_CpqSsTrapLogEntry_Object=MibTableRow
cpqSsTrapLogEntry=_CpqSsTrapLogEntry_Object((1,3,6,1,4,1,232,8,3,3,1))
cpqSsTrapLogEntry.setIndexNames((0,_B,_AF))
if mibBuilder.loadTexts:cpqSsTrapLogEntry.setStatus(_W)
class _CpqSsTrapLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqSsTrapLogIndex_Type.__name__=_D
_CpqSsTrapLogIndex_Object=MibTableColumn
cpqSsTrapLogIndex=_CpqSsTrapLogIndex_Object((1,3,6,1,4,1,232,8,3,3,1,1),_CpqSsTrapLogIndex_Type())
cpqSsTrapLogIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsTrapLogIndex.setStatus(_W)
class _CpqSsTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,8001,8002,8003,8004,8005,8006)));namedValues=NamedValues(*((_AG,1),(_AH,8001),(_AI,8002),(_AJ,8003),(_AK,8004),(_AL,8005),(_AM,8006)))
_CpqSsTrapType_Type.__name__=_D
_CpqSsTrapType_Object=MibTableColumn
cpqSsTrapType=_CpqSsTrapType_Object((1,3,6,1,4,1,232,8,3,3,1,2),_CpqSsTrapType_Type())
cpqSsTrapType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsTrapType.setStatus(_W)
class _CpqSsTrapTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_CpqSsTrapTime_Type.__name__=_o
_CpqSsTrapTime_Object=MibTableColumn
cpqSsTrapTime=_CpqSsTrapTime_Object((1,3,6,1,4,1,232,8,3,3,1,3),_CpqSsTrapTime_Type())
cpqSsTrapTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsTrapTime.setStatus(_W)
_CpqSsRaidSystem_ObjectIdentity=ObjectIdentity
cpqSsRaidSystem=_CpqSsRaidSystem_ObjectIdentity((1,3,6,1,4,1,232,8,4))
_CpqSsRaidSystemTable_Object=MibTable
cpqSsRaidSystemTable=_CpqSsRaidSystemTable_Object((1,3,6,1,4,1,232,8,4,1))
if mibBuilder.loadTexts:cpqSsRaidSystemTable.setStatus(_A)
_CpqSsRaidSystemEntry_Object=MibTableRow
cpqSsRaidSystemEntry=_CpqSsRaidSystemEntry_Object((1,3,6,1,4,1,232,8,4,1,1))
cpqSsRaidSystemEntry.setIndexNames((0,_B,_AN))
if mibBuilder.loadTexts:cpqSsRaidSystemEntry.setStatus(_A)
class _CpqSsRaidSystemIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSsRaidSystemIndex_Type.__name__=_D
_CpqSsRaidSystemIndex_Object=MibTableColumn
cpqSsRaidSystemIndex=_CpqSsRaidSystemIndex_Object((1,3,6,1,4,1,232,8,4,1,1,1),_CpqSsRaidSystemIndex_Type())
cpqSsRaidSystemIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsRaidSystemIndex.setStatus(_A)
class _CpqSsRaidSystemName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSsRaidSystemName_Type.__name__=_F
_CpqSsRaidSystemName_Object=MibTableColumn
cpqSsRaidSystemName=_CpqSsRaidSystemName_Object((1,3,6,1,4,1,232,8,4,1,1,2),_CpqSsRaidSystemName_Type())
cpqSsRaidSystemName.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsRaidSystemName.setStatus(_A)
class _CpqSsRaidSystemStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('agentNotRunning',2),('good',3),('warning',4),('communicationLoss',5)))
_CpqSsRaidSystemStatus_Type.__name__=_D
_CpqSsRaidSystemStatus_Object=MibTableColumn
cpqSsRaidSystemStatus=_CpqSsRaidSystemStatus_Object((1,3,6,1,4,1,232,8,4,1,1,3),_CpqSsRaidSystemStatus_Type())
cpqSsRaidSystemStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsRaidSystemStatus.setStatus(_A)
class _CpqSsRaidSystemCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_G,2),(_H,3),(_I,4)))
_CpqSsRaidSystemCondition_Type.__name__=_D
_CpqSsRaidSystemCondition_Object=MibTableColumn
cpqSsRaidSystemCondition=_CpqSsRaidSystemCondition_Object((1,3,6,1,4,1,232,8,4,1,1,4),_CpqSsRaidSystemCondition_Type())
cpqSsRaidSystemCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsRaidSystemCondition.setStatus(_A)
class _CpqSsRaidSystemCntlr1SerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_CpqSsRaidSystemCntlr1SerialNumber_Type.__name__=_F
_CpqSsRaidSystemCntlr1SerialNumber_Object=MibTableColumn
cpqSsRaidSystemCntlr1SerialNumber=_CpqSsRaidSystemCntlr1SerialNumber_Object((1,3,6,1,4,1,232,8,4,1,1,5),_CpqSsRaidSystemCntlr1SerialNumber_Type())
cpqSsRaidSystemCntlr1SerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsRaidSystemCntlr1SerialNumber.setStatus(_A)
class _CpqSsRaidSystemCntlr2SerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_CpqSsRaidSystemCntlr2SerialNumber_Type.__name__=_F
_CpqSsRaidSystemCntlr2SerialNumber_Object=MibTableColumn
cpqSsRaidSystemCntlr2SerialNumber=_CpqSsRaidSystemCntlr2SerialNumber_Object((1,3,6,1,4,1,232,8,4,1,1,6),_CpqSsRaidSystemCntlr2SerialNumber_Type())
cpqSsRaidSystemCntlr2SerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cpqSsRaidSystemCntlr2SerialNumber.setStatus(_A)
cpqSs2FanStatusChange=NotificationType((1,3,6,1,4,1,232,0,8001))
cpqSs2FanStatusChange.setObjects((_B,_X))
if mibBuilder.loadTexts:cpqSs2FanStatusChange.setStatus('')
cpqSsTempFailed=NotificationType((1,3,6,1,4,1,232,0,8002))
cpqSsTempFailed.setObjects((_B,_R))
if mibBuilder.loadTexts:cpqSsTempFailed.setStatus('')
cpqSsTempDegraded=NotificationType((1,3,6,1,4,1,232,0,8003))
cpqSsTempDegraded.setObjects((_B,_R))
if mibBuilder.loadTexts:cpqSsTempDegraded.setStatus('')
cpqSsTempOk=NotificationType((1,3,6,1,4,1,232,0,8004))
cpqSsTempOk.setObjects((_B,_R))
if mibBuilder.loadTexts:cpqSsTempOk.setStatus('')
cpqSsSidePanelInPlace=NotificationType((1,3,6,1,4,1,232,0,8005))
cpqSsSidePanelInPlace.setObjects((_B,_b))
if mibBuilder.loadTexts:cpqSsSidePanelInPlace.setStatus('')
cpqSsSidePanelRemoved=NotificationType((1,3,6,1,4,1,232,0,8006))
cpqSsSidePanelRemoved.setObjects((_B,_b))
if mibBuilder.loadTexts:cpqSsSidePanelRemoved.setStatus('')
cpqSsPwrSupplyDegraded=NotificationType((1,3,6,1,4,1,232,0,8007))
if mibBuilder.loadTexts:cpqSsPwrSupplyDegraded.setStatus('')
cpqSs3FanStatusChange=NotificationType((1,3,6,1,4,1,232,0,8008))
cpqSs3FanStatusChange.setObjects(*((_L,_M),(_J,_K),(_B,_X)))
if mibBuilder.loadTexts:cpqSs3FanStatusChange.setStatus('')
cpqSs3TempFailed=NotificationType((1,3,6,1,4,1,232,0,8009))
cpqSs3TempFailed.setObjects(*((_L,_M),(_J,_K),(_B,_R)))
if mibBuilder.loadTexts:cpqSs3TempFailed.setStatus('')
cpqSs3TempDegraded=NotificationType((1,3,6,1,4,1,232,0,8010))
cpqSs3TempDegraded.setObjects(*((_L,_M),(_J,_K),(_B,_R)))
if mibBuilder.loadTexts:cpqSs3TempDegraded.setStatus('')
cpqSs3TempOk=NotificationType((1,3,6,1,4,1,232,0,8011))
cpqSs3TempOk.setObjects(*((_L,_M),(_J,_K),(_B,_R)))
if mibBuilder.loadTexts:cpqSs3TempOk.setStatus('')
cpqSs3SidePanelInPlace=NotificationType((1,3,6,1,4,1,232,0,8012))
cpqSs3SidePanelInPlace.setObjects(*((_L,_M),(_J,_K),(_B,_b)))
if mibBuilder.loadTexts:cpqSs3SidePanelInPlace.setStatus('')
cpqSs3SidePanelRemoved=NotificationType((1,3,6,1,4,1,232,0,8013))
cpqSs3SidePanelRemoved.setObjects(*((_L,_M),(_J,_K),(_B,_b)))
if mibBuilder.loadTexts:cpqSs3SidePanelRemoved.setStatus('')
cpqSs3PwrSupplyDegraded=NotificationType((1,3,6,1,4,1,232,0,8014))
cpqSs3PwrSupplyDegraded.setObjects(*((_L,_M),(_J,_K)))
if mibBuilder.loadTexts:cpqSs3PwrSupplyDegraded.setStatus('')
cpqSs4PwrSupplyDegraded=NotificationType((1,3,6,1,4,1,232,0,8015))
cpqSs4PwrSupplyDegraded.setObjects(*((_L,_M),(_J,_K),(_B,_d)))
if mibBuilder.loadTexts:cpqSs4PwrSupplyDegraded.setStatus('')
cpqSsExFanStatusChange=NotificationType((1,3,6,1,4,1,232,0,8016))
cpqSsExFanStatusChange.setObjects(*((_L,_M),(_J,_K),(_B,_N),(_B,_O),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:cpqSsExFanStatusChange.setStatus('')
cpqSsExPowerSupplyStatusChange=NotificationType((1,3,6,1,4,1,232,0,8017))
cpqSsExPowerSupplyStatusChange.setObjects(*((_L,_M),(_J,_K),(_B,_N),(_B,_O),(_B,_e),(_B,_n)))
if mibBuilder.loadTexts:cpqSsExPowerSupplyStatusChange.setStatus('')
cpqSsExPowerSupplyUpsStatusChange=NotificationType((1,3,6,1,4,1,232,0,8018))
cpqSsExPowerSupplyUpsStatusChange.setObjects(*((_L,_M),(_J,_K),(_B,_N),(_B,_O),(_B,_e),(_B,_AO)))
if mibBuilder.loadTexts:cpqSsExPowerSupplyUpsStatusChange.setStatus('')
cpqSsExTempSensorStatusChange=NotificationType((1,3,6,1,4,1,232,0,8019))
cpqSsExTempSensorStatusChange.setObjects(*((_L,_M),(_J,_K),(_B,_N),(_B,_O),(_B,_AP),(_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:cpqSsExTempSensorStatusChange.setStatus('')
cpqSsEx2FanStatusChange=NotificationType((1,3,6,1,4,1,232,0,8020))
cpqSsEx2FanStatusChange.setObjects(*((_L,_M),(_J,_K),(_B,_N),(_B,_O),(_B,_l),(_B,_m),(_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:cpqSsEx2FanStatusChange.setStatus('')
cpqSsEx2PowerSupplyStatusChange=NotificationType((1,3,6,1,4,1,232,0,8021))
cpqSsEx2PowerSupplyStatusChange.setObjects(*((_L,_M),(_J,_K),(_B,_N),(_B,_O),(_B,_e),(_B,_n),(_B,_AU),(_B,_AV),(_B,_AW)))
if mibBuilder.loadTexts:cpqSsEx2PowerSupplyStatusChange.setStatus('')
cpqSsExBackplaneFanStatusChange=NotificationType((1,3,6,1,4,1,232,0,8022))
cpqSsExBackplaneFanStatusChange.setObjects(*((_L,_M),(_J,_K),(_B,_N),(_B,_O),(_B,_a),(_B,_f),(_B,_g),(_B,_h),(_B,_AX)))
if mibBuilder.loadTexts:cpqSsExBackplaneFanStatusChange.setStatus('')
cpqSsExBackplaneTempStatusChange=NotificationType((1,3,6,1,4,1,232,0,8023))
cpqSsExBackplaneTempStatusChange.setObjects(*((_L,_M),(_J,_K),(_B,_N),(_B,_O),(_B,_a),(_B,_f),(_B,_g),(_B,_h),(_B,_AY)))
if mibBuilder.loadTexts:cpqSsExBackplaneTempStatusChange.setStatus('')
cpqSsExBackplanePowerSupplyStatusChange=NotificationType((1,3,6,1,4,1,232,0,8024))
cpqSsExBackplanePowerSupplyStatusChange.setObjects(*((_L,_M),(_J,_K),(_B,_N),(_B,_O),(_B,_a),(_B,_f),(_B,_g),(_B,_h),(_B,_AZ)))
if mibBuilder.loadTexts:cpqSsExBackplanePowerSupplyStatusChange.setStatus('')
cpqSsExRecoveryServerStatusChange=NotificationType((1,3,6,1,4,1,232,0,8025))
cpqSsExRecoveryServerStatusChange.setObjects(*((_L,_M),(_J,_K),(_B,_N),(_B,_O),(_B,_Aa),(_B,_k)))
if mibBuilder.loadTexts:cpqSsExRecoveryServerStatusChange.setStatus('')
cpqSs5FanStatusChange=NotificationType((1,3,6,1,4,1,232,0,8026))
cpqSs5FanStatusChange.setObjects(*((_L,_M),(_J,_K),(_B,_S),(_B,_P),(_B,_Q),(_B,_T),(_B,_U),(_B,_V),(_B,_X)))
if mibBuilder.loadTexts:cpqSs5FanStatusChange.setStatus('')
cpqSs5TempStatusChange=NotificationType((1,3,6,1,4,1,232,0,8027))
cpqSs5TempStatusChange.setObjects(*((_L,_M),(_J,_K),(_B,_S),(_B,_P),(_B,_Q),(_B,_T),(_B,_U),(_B,_V),(_B,_R)))
if mibBuilder.loadTexts:cpqSs5TempStatusChange.setStatus('')
cpqSs5PwrSupplyStatusChange=NotificationType((1,3,6,1,4,1,232,0,8028))
cpqSs5PwrSupplyStatusChange.setObjects(*((_L,_M),(_J,_K),(_B,_S),(_B,_P),(_B,_Q),(_B,_T),(_B,_U),(_B,_V),(_B,_d)))
if mibBuilder.loadTexts:cpqSs5PwrSupplyStatusChange.setStatus('')
cpqSs6FanStatusChange=NotificationType((1,3,6,1,4,1,232,0,8029))
cpqSs6FanStatusChange.setObjects(*((_L,_M),(_J,_K),(_B,_S),(_B,_P),(_B,_Q),(_B,_T),(_B,_U),(_B,_V),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:cpqSs6FanStatusChange.setStatus('')
cpqSs6TempStatusChange=NotificationType((1,3,6,1,4,1,232,0,8030))
cpqSs6TempStatusChange.setObjects(*((_L,_M),(_J,_K),(_B,_S),(_B,_P),(_B,_Q),(_B,_T),(_B,_U),(_B,_V),(_B,_R),(_B,_Y)))
if mibBuilder.loadTexts:cpqSs6TempStatusChange.setStatus('')
cpqSs6PwrSupplyStatusChange=NotificationType((1,3,6,1,4,1,232,0,8031))
cpqSs6PwrSupplyStatusChange.setObjects(*((_L,_M),(_J,_K),(_B,_S),(_B,_P),(_B,_Q),(_B,_T),(_B,_U),(_B,_V),(_B,_d),(_B,_Y)))
if mibBuilder.loadTexts:cpqSs6PwrSupplyStatusChange.setStatus('')
cpqSsConnectionStatusChange=NotificationType((1,3,6,1,4,1,232,0,8032))
cpqSsConnectionStatusChange.setObjects(*((_L,_M),(_J,_K),(_B,_S),(_B,_P),(_B,_Q),(_B,_T),(_B,_U),(_B,_V),(_B,_Ab),(_B,_Y),(_B,_Ac),(_B,_Ad)))
if mibBuilder.loadTexts:cpqSsConnectionStatusChange.setStatus('')
cpqSsGSIStatusChange=NotificationType((1,3,6,1,4,1,232,0,8033))
cpqSsGSIStatusChange.setObjects(*((_L,_M),(_J,_K),(_B,_S),(_B,_P),(_B,_Q),(_B,_T),(_B,_U),(_B,_V),(_B,_Ae),(_B,_Af),(_B,_Y)))
if mibBuilder.loadTexts:cpqSsGSIStatusChange.setStatus('')
cpqSsFanStatusChange=NotificationType((1,3,6,1,4,1,232,8,0,1))
cpqSsFanStatusChange.setObjects((_B,_X))
if mibBuilder.loadTexts:cpqSsFanStatusChange.setStatus('')
mibBuilder.exportSymbols(_B,**{_AH:cpqSs2FanStatusChange,_AI:cpqSsTempFailed,_AJ:cpqSsTempDegraded,_AK:cpqSsTempOk,_AL:cpqSsSidePanelInPlace,_AM:cpqSsSidePanelRemoved,'cpqSsPwrSupplyDegraded':cpqSsPwrSupplyDegraded,'cpqSs3FanStatusChange':cpqSs3FanStatusChange,'cpqSs3TempFailed':cpqSs3TempFailed,'cpqSs3TempDegraded':cpqSs3TempDegraded,'cpqSs3TempOk':cpqSs3TempOk,'cpqSs3SidePanelInPlace':cpqSs3SidePanelInPlace,'cpqSs3SidePanelRemoved':cpqSs3SidePanelRemoved,'cpqSs3PwrSupplyDegraded':cpqSs3PwrSupplyDegraded,'cpqSs4PwrSupplyDegraded':cpqSs4PwrSupplyDegraded,'cpqSsExFanStatusChange':cpqSsExFanStatusChange,'cpqSsExPowerSupplyStatusChange':cpqSsExPowerSupplyStatusChange,'cpqSsExPowerSupplyUpsStatusChange':cpqSsExPowerSupplyUpsStatusChange,'cpqSsExTempSensorStatusChange':cpqSsExTempSensorStatusChange,'cpqSsEx2FanStatusChange':cpqSsEx2FanStatusChange,'cpqSsEx2PowerSupplyStatusChange':cpqSsEx2PowerSupplyStatusChange,'cpqSsExBackplaneFanStatusChange':cpqSsExBackplaneFanStatusChange,'cpqSsExBackplaneTempStatusChange':cpqSsExBackplaneTempStatusChange,'cpqSsExBackplanePowerSupplyStatusChange':cpqSsExBackplanePowerSupplyStatusChange,'cpqSsExRecoveryServerStatusChange':cpqSsExRecoveryServerStatusChange,'cpqSs5FanStatusChange':cpqSs5FanStatusChange,'cpqSs5TempStatusChange':cpqSs5TempStatusChange,'cpqSs5PwrSupplyStatusChange':cpqSs5PwrSupplyStatusChange,'cpqSs6FanStatusChange':cpqSs6FanStatusChange,'cpqSs6TempStatusChange':cpqSs6TempStatusChange,'cpqSs6PwrSupplyStatusChange':cpqSs6PwrSupplyStatusChange,'cpqSsConnectionStatusChange':cpqSsConnectionStatusChange,'cpqSsGSIStatusChange':cpqSsGSIStatusChange,'cpqSsStorageSys':cpqSsStorageSys,_AG:cpqSsFanStatusChange,'cpqSsMibRev':cpqSsMibRev,'cpqSsMibRevMajor':cpqSsMibRevMajor,'cpqSsMibRevMinor':cpqSsMibRevMinor,'cpqSsMibCondition':cpqSsMibCondition,'cpqSsDrvBox':cpqSsDrvBox,'cpqSsDrvBoxTable':cpqSsDrvBoxTable,'cpqSsDrvBoxEntry':cpqSsDrvBoxEntry,_P:cpqSsBoxCntlrIndex,_Q:cpqSsBoxBusIndex,'cpqSsBoxType':cpqSsBoxType,_U:cpqSsBoxModel,'cpqSsBoxFWRev':cpqSsBoxFWRev,_T:cpqSsBoxVendor,_X:cpqSsBoxFanStatus,'cpqSsBoxCondition':cpqSsBoxCondition,_R:cpqSsBoxTempStatus,_b:cpqSsBoxSidePanelStatus,_d:cpqSsBoxFltTolPwrSupplyStatus,'cpqSsBoxBackPlaneVersion':cpqSsBoxBackPlaneVersion,'cpqSsBoxTotalBays':cpqSsBoxTotalBays,'cpqSsBoxPlacement':cpqSsBoxPlacement,'cpqSsBoxDuplexOption':cpqSsBoxDuplexOption,'cpqSsBoxBoardRevision':cpqSsBoxBoardRevision,_V:cpqSsBoxSerialNumber,_S:cpqSsBoxCntlrHwLocation,'cpqSsBoxBackplaneSpeed':cpqSsBoxBackplaneSpeed,'cpqSsBoxConnectionType':cpqSsBoxConnectionType,'cpqSsBoxHostConnector':cpqSsBoxHostConnector,'cpqSsBoxBoxOnConnector':cpqSsBoxBoxOnConnector,_Y:cpqSsBoxLocationString,'cpqSsBoxInitiatorSasAddress':cpqSsBoxInitiatorSasAddress,_Ac:cpqSsBoxTargetSasAddress,_Ad:cpqSsBoxLocalManageIpAddress,'cpqSsBoxPartnerManageIpAddress':cpqSsBoxPartnerManageIpAddress,_Ab:cpqSsBoxConnectionStatus,'cpqSsBoxTargetBasedManagement':cpqSsBoxTargetBasedManagement,_Ae:cpqSsBoxGSIStatus,_Af:cpqSsBoxGSIMessages,'cpqSsBoxExtended':cpqSsBoxExtended,'cpqSsChassisTable':cpqSsChassisTable,'cpqSsChassisEntry':cpqSsChassisEntry,_k:cpqSsChassisIndex,'cpqSsChassisConnectionType':cpqSsChassisConnectionType,'cpqSsChassisSerialNumber':cpqSsChassisSerialNumber,_N:cpqSsChassisName,'cpqSsChassisSystemBoardSerNum':cpqSsChassisSystemBoardSerNum,'cpqSsChassisSystemBoardRev':cpqSsChassisSystemBoardRev,'cpqSsChassisPowerBoardSerNum':cpqSsChassisPowerBoardSerNum,'cpqSsChassisPowerBoardRev':cpqSsChassisPowerBoardRev,'cpqSsChassisScsiBoardSerNum':cpqSsChassisScsiBoardSerNum,'cpqSsChassisScsiBoardRev':cpqSsChassisScsiBoardRev,'cpqSsChassisOverallCondition':cpqSsChassisOverallCondition,'cpqSsChassisPowerSupplyCondition':cpqSsChassisPowerSupplyCondition,'cpqSsChassisFanCondition':cpqSsChassisFanCondition,'cpqSsChassisTemperatureCondition':cpqSsChassisTemperatureCondition,'cpqSsChassisFcaCntlrCondition':cpqSsChassisFcaCntlrCondition,'cpqSsChassisFcaLogicalDriveCondition':cpqSsChassisFcaLogicalDriveCondition,'cpqSsChassisFcaPhysDrvCondition':cpqSsChassisFcaPhysDrvCondition,_O:cpqSsChassisTime,'cpqSsChassisModel':cpqSsChassisModel,'cpqSsChassisBackplaneCondition':cpqSsChassisBackplaneCondition,'cpqSsChassisFcaTapeDrvCondition':cpqSsChassisFcaTapeDrvCondition,_Aa:cpqSsChassisRsoStatus,'cpqSsChassisRsoCondition':cpqSsChassisRsoCondition,'cpqSsChassisScsiIoModuleType':cpqSsChassisScsiIoModuleType,'cpqSsChassisPreferredPathMode':cpqSsChassisPreferredPathMode,'cpqSsChassisProductId':cpqSsChassisProductId,'cpqSsIoSlotTable':cpqSsIoSlotTable,'cpqSsIoSlotEntry':cpqSsIoSlotEntry,_A0:cpqSsIoSlotChassisIndex,_A1:cpqSsIoSlotIndex,'cpqSsIoSlotControllerType':cpqSsIoSlotControllerType,'cpqSsPowerSupplyTable':cpqSsPowerSupplyTable,'cpqSsPowerSupplyEntry':cpqSsPowerSupplyEntry,_A2:cpqSsPowerSupplyChassisIndex,_A3:cpqSsPowerSupplyIndex,_e:cpqSsPowerSupplyBay,_n:cpqSsPowerSupplyStatus,_AO:cpqSsPowerSupplyUpsStatus,'cpqSsPowerSupplyCondition':cpqSsPowerSupplyCondition,_AU:cpqSsPowerSupplySerialNumber,_AV:cpqSsPowerSupplyBoardRevision,_AW:cpqSsPowerSupplyFirmwareRevision,'cpqSsFanModuleTable':cpqSsFanModuleTable,'cpqSsFanModuleEntry':cpqSsFanModuleEntry,_A5:cpqSsFanModuleChassisIndex,_A6:cpqSsFanModuleIndex,_m:cpqSsFanModuleStatus,'cpqSsFanModuleCondition':cpqSsFanModuleCondition,_l:cpqSsFanModuleLocation,_AS:cpqSsFanModuleSerialNumber,_AT:cpqSsFanModuleBoardRevision,'cpqSsTempSensorTable':cpqSsTempSensorTable,'cpqSsTempSensorEntry':cpqSsTempSensorEntry,_A7:cpqSsTempSensorChassisIndex,_A8:cpqSsTempSensorIndex,_AQ:cpqSsTempSensorStatus,'cpqSsTempSensorCondition':cpqSsTempSensorCondition,_AP:cpqSsTempSensorLocation,_AR:cpqSsTempSensorCurrentValue,'cpqSsTempSensorLimitValue':cpqSsTempSensorLimitValue,'cpqSsTempSensorHysteresisValue':cpqSsTempSensorHysteresisValue,'cpqSsBackplaneTable':cpqSsBackplaneTable,'cpqSsBackplaneEntry':cpqSsBackplaneEntry,_A9:cpqSsBackplaneChassisIndex,_a:cpqSsBackplaneIndex,'cpqSsBackplaneFWRev':cpqSsBackplaneFWRev,'cpqSsBackplaneDriveBays':cpqSsBackplaneDriveBays,'cpqSsBackplaneDuplexOption':cpqSsBackplaneDuplexOption,'cpqSsBackplaneCondition':cpqSsBackplaneCondition,'cpqSsBackplaneVersion':cpqSsBackplaneVersion,_f:cpqSsBackplaneVendor,_g:cpqSsBackplaneModel,_AX:cpqSsBackplaneFanStatus,_AY:cpqSsBackplaneTempStatus,_AZ:cpqSsBackplaneFtpsStatus,_h:cpqSsBackplaneSerialNumber,'cpqSsBackplanePlacement':cpqSsBackplanePlacement,'cpqSsBackplaneBoardRevision':cpqSsBackplaneBoardRevision,'cpqSsBackplaneSpeed':cpqSsBackplaneSpeed,'cpqSsBackplaneConnectionType':cpqSsBackplaneConnectionType,'cpqSsBackplaneConnector':cpqSsBackplaneConnector,'cpqSsBackplaneOnConnector':cpqSsBackplaneOnConnector,'cpqSsBackplaneLocationString':cpqSsBackplaneLocationString,'cpqSsFibreAttachmentTable':cpqSsFibreAttachmentTable,'cpqSsFibreAttachmentEntry':cpqSsFibreAttachmentEntry,_AA:cpqSsFibreAttachmentIndex,'cpqSsFibreAttachmentHostControllerIndex':cpqSsFibreAttachmentHostControllerIndex,'cpqSsFibreAttachmentHostControllerPort':cpqSsFibreAttachmentHostControllerPort,'cpqSsFibreAttachmentDeviceType':cpqSsFibreAttachmentDeviceType,'cpqSsFibreAttachmentDeviceIndex':cpqSsFibreAttachmentDeviceIndex,'cpqSsFibreAttachmentDevicePort':cpqSsFibreAttachmentDevicePort,'cpqSsScsiAttachmentTable':cpqSsScsiAttachmentTable,'cpqSsScsiAttachmentEntry':cpqSsScsiAttachmentEntry,_AB:cpqSsScsiAttachmentIndex,'cpqSsScsiAttachmentControllerIndex':cpqSsScsiAttachmentControllerIndex,'cpqSsScsiAttachmentControllerPort':cpqSsScsiAttachmentControllerPort,'cpqSsScsiAttachmentControllerTarget':cpqSsScsiAttachmentControllerTarget,'cpqSsScsiAttachmentControllerLun':cpqSsScsiAttachmentControllerLun,'cpqSsScsiAttachmentChassisIndex':cpqSsScsiAttachmentChassisIndex,'cpqSsScsiAttachmentChassisIoSlot':cpqSsScsiAttachmentChassisIoSlot,'cpqSsScsiAttachmentPathStatus':cpqSsScsiAttachmentPathStatus,'cpqSsScsiAttachmentPathCondition':cpqSsScsiAttachmentPathCondition,'cpqSsDrvBoxPathTable':cpqSsDrvBoxPathTable,'cpqSsDrvBoxPathEntry':cpqSsDrvBoxPathEntry,_AC:cpqSsDrvBoxPathCntlrIndex,_AD:cpqSsDrvBoxPathBoxIndex,_AE:cpqSsDrvBoxPathIndex,'cpqSsDrvBoxPathStatus':cpqSsDrvBoxPathStatus,'cpqSsDrvBoxPathCurrentRole':cpqSsDrvBoxPathCurrentRole,'cpqSsDrvBoxPathHostConnector':cpqSsDrvBoxPathHostConnector,'cpqSsDrvBoxPathBoxOnConnector':cpqSsDrvBoxPathBoxOnConnector,'cpqSsDrvBoxPathLocationString':cpqSsDrvBoxPathLocationString,'cpqSsTrap':cpqSsTrap,'cpqSsTrapPkts':cpqSsTrapPkts,'cpqSsTrapLogMaxSize':cpqSsTrapLogMaxSize,'cpqSsTrapLogTable':cpqSsTrapLogTable,'cpqSsTrapLogEntry':cpqSsTrapLogEntry,_AF:cpqSsTrapLogIndex,'cpqSsTrapType':cpqSsTrapType,'cpqSsTrapTime':cpqSsTrapTime,'cpqSsRaidSystem':cpqSsRaidSystem,'cpqSsRaidSystemTable':cpqSsRaidSystemTable,'cpqSsRaidSystemEntry':cpqSsRaidSystemEntry,_AN:cpqSsRaidSystemIndex,'cpqSsRaidSystemName':cpqSsRaidSystemName,'cpqSsRaidSystemStatus':cpqSsRaidSystemStatus,'cpqSsRaidSystemCondition':cpqSsRaidSystemCondition,'cpqSsRaidSystemCntlr1SerialNumber':cpqSsRaidSystemCntlr1SerialNumber,'cpqSsRaidSystemCntlr2SerialNumber':cpqSsRaidSystemCntlr2SerialNumber})