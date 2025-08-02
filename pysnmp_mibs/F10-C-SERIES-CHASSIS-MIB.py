_Av='f10CSerLineCardGroup'
_Au='f10CSerRpmGroup'
_At='f10CSerSystemGroup'
_As='f10CSerComponentGroup'
_Ar='chLineCardMemUsageUtil'
_Aq='chLineCardCpuUtil5Min'
_Ap='chLineCardCpuUtil1Min'
_Ao='chLineCardCpuUtil5Sec'
_An='chRpmMemUsageUtil'
_Am='chRpmCpuUtil5Min'
_Al='chRpmCpuUtil1Min'
_Ak='chRpmCpuUtil5Sec'
_Aj='chRpmCpuType'
_Ai='chRpmMinorAlarmStatus'
_Ah='chRpmMajorAlarmStatus'
_Ag='chRpmLastSwitchDate'
_Af='chRpmUptime'
_Ae='chRpmSlotNumber'
_Ad='chRpmNumRpms'
_Ac='chSysSfmErrorStatus'
_Ab='chSysSfmOperStatus'
_Aa='chSysSfmAdminStatus'
_AZ='chSysFanTrayOperStatus'
_AY='chSysPowerSupplyMode'
_AX='chSysPowerSupplyVersion'
_AW='chSysPowerSupplyType'
_AV='chSysPowerSupplyOperStatus'
_AU='chSysSwCurrentBootImage'
_AT='chSysSwNextRebootImage'
_AS='chSysSwBackupBootImgStatus'
_AR='chSysSwBackupBootImgDate'
_AQ='chSysSwBackupBootImgVersion'
_AP='chSysSwCurrentBootImgStatus'
_AO='chSysSwCurrentBootImgDate'
_AN='chSysSwCurrentBootImgVersion'
_AM='chSysSwRuntimeImgDate'
_AL='chSysSwRuntimeImgVersion'
_AK='chSysProcessorMemSize'
_AJ='chSysProcessorNvramSize'
_AI='chSysProcessorUpTime'
_AH='chSysProcessorModule'
_AG='chSysXfpRecvPower'
_AF='chSysPortIfIndex'
_AE='chSysPortOperStatus'
_AD='chSysPortAdminStatus'
_AC='chSysPortType'
_AB='chSysCardExpressServiceCode'
_AA='chSysCardServiceTag'
_A9='chSysCardPPIDRevision'
_A8='chSysCardPiecePartID'
_A7='chSysCardCountryCode'
_A6='chSysCardDateCode'
_A5='chSysCardVendorId'
_A4='chSysCardProductRev'
_A3='chSysCardPartNum'
_A2='chSysCardSerialNumber'
_A1='chSysCardBootFlashB'
_A0='chSysCardBootFlashA'
_z='chSysCardOperStatus'
_y='chSysCardAdminStatus'
_x='chSysCardUpTime'
_w='chSysCardTemp'
_v='chSysCardNumPorts'
_u='chSysCardType'
_t='chNumSfmSlots'
_s='chNumPowerSupplies'
_r='chNumFanTrays'
_q='chNumLinecards'
_p='chNumSlots'
_o='chExpressServiceCode'
_n='chServiceTag'
_m='chPPIDRevision'
_l='chPiecePartID'
_k='chCountryCode'
_j='chDateCode'
_i='chVendorId'
_h='chProductRev'
_g='chPartNum'
_f='chSerialNumber'
_e='chMacAddr'
_d='chSwVersion'
_c='chChassisMode'
_b='chType'
_a='chRpmCpuIndex'
_Z='chSysSfmIndex'
_Y='chSysFanTrayIndex'
_X='unknown'
_W='absent'
_V='chSysPowerSupplyIndex'
_U='bootImage-B'
_T='bootImage-A'
_S='failed'
_R='chSysSwProcessorIndex'
_Q='chSysSwSlotIndex'
_P='chSysProcessorIndex'
_O='chSysProcessorSlotIndex'
_N='chSysPortIndex'
_M='chSysPortSlotIndex'
_L='chSysCardSlotIndex'
_K='chSysCardNumber'
_J='OctetString'
_I='down'
_H='up'
_G='percent'
_F='DisplayString'
_E='Gauge32'
_D='Integer32'
_C='read-only'
_B='F10-C-SERIES-CHASSIS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
f10Mgmt,=mibBuilder.importSymbols('FORCE10-SMI','f10Mgmt')
F10CSeriesCardType,F10CSeriesPortType,F10CardOperStatus,F10ChassisMode,F10ChassisType,F10HundredthdB,F10MfgDate,F10ProcessorModuleType,F10SwDate=mibBuilder.importSymbols('FORCE10-TC','F10CSeriesCardType','F10CSeriesPortType','F10CardOperStatus','F10ChassisMode','F10ChassisType','F10HundredthdB','F10MfgDate','F10ProcessorModuleType','F10SwDate')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_E,_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'MacAddress','PhysAddress','TextualConvention')
f10CSerChassisMib=ModuleIdentity((1,3,6,1,4,1,6027,3,8))
if mibBuilder.loadTexts:f10CSerChassisMib.setRevisions(('2012-07-18 12:00','2008-09-02 12:00','2007-06-28 12:00','2007-05-22 12:00','2013-05-17 12:00','1906-05-01 00:00'))
_F10CSerChassisObject_ObjectIdentity=ObjectIdentity
f10CSerChassisObject=_F10CSerChassisObject_ObjectIdentity((1,3,6,1,4,1,6027,3,8,1))
_ChObjects_ObjectIdentity=ObjectIdentity
chObjects=_ChObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,8,1,1))
_ChType_Type=F10ChassisType
_ChType_Object=MibScalar
chType=_ChType_Object((1,3,6,1,4,1,6027,3,8,1,1,1),_ChType_Type())
chType.setMaxAccess(_C)
if mibBuilder.loadTexts:chType.setStatus(_A)
_ChChassisMode_Type=F10ChassisMode
_ChChassisMode_Object=MibScalar
chChassisMode=_ChChassisMode_Object((1,3,6,1,4,1,6027,3,8,1,1,2),_ChChassisMode_Type())
chChassisMode.setMaxAccess(_C)
if mibBuilder.loadTexts:chChassisMode.setStatus(_A)
_ChSwVersion_Type=DisplayString
_ChSwVersion_Object=MibScalar
chSwVersion=_ChSwVersion_Object((1,3,6,1,4,1,6027,3,8,1,1,3),_ChSwVersion_Type())
chSwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:chSwVersion.setStatus(_A)
_ChMacAddr_Type=MacAddress
_ChMacAddr_Object=MibScalar
chMacAddr=_ChMacAddr_Object((1,3,6,1,4,1,6027,3,8,1,1,4),_ChMacAddr_Type())
chMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:chMacAddr.setStatus(_A)
_ChSerialNumber_Type=DisplayString
_ChSerialNumber_Object=MibScalar
chSerialNumber=_ChSerialNumber_Object((1,3,6,1,4,1,6027,3,8,1,1,5),_ChSerialNumber_Type())
chSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:chSerialNumber.setStatus(_A)
_ChPartNum_Type=DisplayString
_ChPartNum_Object=MibScalar
chPartNum=_ChPartNum_Object((1,3,6,1,4,1,6027,3,8,1,1,6),_ChPartNum_Type())
chPartNum.setMaxAccess(_C)
if mibBuilder.loadTexts:chPartNum.setStatus(_A)
_ChProductRev_Type=DisplayString
_ChProductRev_Object=MibScalar
chProductRev=_ChProductRev_Object((1,3,6,1,4,1,6027,3,8,1,1,7),_ChProductRev_Type())
chProductRev.setMaxAccess(_C)
if mibBuilder.loadTexts:chProductRev.setStatus(_A)
_ChVendorId_Type=DisplayString
_ChVendorId_Object=MibScalar
chVendorId=_ChVendorId_Object((1,3,6,1,4,1,6027,3,8,1,1,8),_ChVendorId_Type())
chVendorId.setMaxAccess(_C)
if mibBuilder.loadTexts:chVendorId.setStatus(_A)
_ChDateCode_Type=F10MfgDate
_ChDateCode_Object=MibScalar
chDateCode=_ChDateCode_Object((1,3,6,1,4,1,6027,3,8,1,1,9),_ChDateCode_Type())
chDateCode.setMaxAccess(_C)
if mibBuilder.loadTexts:chDateCode.setStatus(_A)
class _ChCountryCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_ChCountryCode_Type.__name__=_J
_ChCountryCode_Object=MibScalar
chCountryCode=_ChCountryCode_Object((1,3,6,1,4,1,6027,3,8,1,1,10),_ChCountryCode_Type())
chCountryCode.setMaxAccess(_C)
if mibBuilder.loadTexts:chCountryCode.setStatus(_A)
_ChNumSlots_Type=Integer32
_ChNumSlots_Object=MibScalar
chNumSlots=_ChNumSlots_Object((1,3,6,1,4,1,6027,3,8,1,1,11),_ChNumSlots_Type())
chNumSlots.setMaxAccess(_C)
if mibBuilder.loadTexts:chNumSlots.setStatus(_A)
_ChNumLinecards_Type=Integer32
_ChNumLinecards_Object=MibScalar
chNumLinecards=_ChNumLinecards_Object((1,3,6,1,4,1,6027,3,8,1,1,12),_ChNumLinecards_Type())
chNumLinecards.setMaxAccess(_C)
if mibBuilder.loadTexts:chNumLinecards.setStatus(_A)
_ChNumFanTrays_Type=Integer32
_ChNumFanTrays_Object=MibScalar
chNumFanTrays=_ChNumFanTrays_Object((1,3,6,1,4,1,6027,3,8,1,1,13),_ChNumFanTrays_Type())
chNumFanTrays.setMaxAccess(_C)
if mibBuilder.loadTexts:chNumFanTrays.setStatus(_A)
_ChNumPowerSupplies_Type=Integer32
_ChNumPowerSupplies_Object=MibScalar
chNumPowerSupplies=_ChNumPowerSupplies_Object((1,3,6,1,4,1,6027,3,8,1,1,14),_ChNumPowerSupplies_Type())
chNumPowerSupplies.setMaxAccess(_C)
if mibBuilder.loadTexts:chNumPowerSupplies.setStatus(_A)
_ChNumSfmSlots_Type=Integer32
_ChNumSfmSlots_Object=MibScalar
chNumSfmSlots=_ChNumSfmSlots_Object((1,3,6,1,4,1,6027,3,8,1,1,15),_ChNumSfmSlots_Type())
chNumSfmSlots.setMaxAccess(_C)
if mibBuilder.loadTexts:chNumSfmSlots.setStatus(_A)
class _ChPiecePartID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_ChPiecePartID_Type.__name__=_F
_ChPiecePartID_Object=MibScalar
chPiecePartID=_ChPiecePartID_Object((1,3,6,1,4,1,6027,3,8,1,1,16),_ChPiecePartID_Type())
chPiecePartID.setMaxAccess(_C)
if mibBuilder.loadTexts:chPiecePartID.setStatus(_A)
class _ChPPIDRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_ChPPIDRevision_Type.__name__=_F
_ChPPIDRevision_Object=MibScalar
chPPIDRevision=_ChPPIDRevision_Object((1,3,6,1,4,1,6027,3,8,1,1,17),_ChPPIDRevision_Type())
chPPIDRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:chPPIDRevision.setStatus(_A)
class _ChServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_ChServiceTag_Type.__name__=_F
_ChServiceTag_Object=MibScalar
chServiceTag=_ChServiceTag_Object((1,3,6,1,4,1,6027,3,8,1,1,18),_ChServiceTag_Type())
chServiceTag.setMaxAccess(_C)
if mibBuilder.loadTexts:chServiceTag.setStatus(_A)
class _ChExpressServiceCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_ChExpressServiceCode_Type.__name__=_F
_ChExpressServiceCode_Object=MibScalar
chExpressServiceCode=_ChExpressServiceCode_Object((1,3,6,1,4,1,6027,3,8,1,1,19),_ChExpressServiceCode_Type())
chExpressServiceCode.setMaxAccess(_C)
if mibBuilder.loadTexts:chExpressServiceCode.setStatus(_A)
_ChSysObjects_ObjectIdentity=ObjectIdentity
chSysObjects=_ChSysObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,8,1,2))
_ChSysCardTable_Object=MibTable
chSysCardTable=_ChSysCardTable_Object((1,3,6,1,4,1,6027,3,8,1,2,1))
if mibBuilder.loadTexts:chSysCardTable.setStatus(_A)
_ChSysCardEntry_Object=MibTableRow
chSysCardEntry=_ChSysCardEntry_Object((1,3,6,1,4,1,6027,3,8,1,2,1,1))
chSysCardEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:chSysCardEntry.setStatus(_A)
_ChSysCardSlotIndex_Type=Integer32
_ChSysCardSlotIndex_Object=MibTableColumn
chSysCardSlotIndex=_ChSysCardSlotIndex_Object((1,3,6,1,4,1,6027,3,8,1,2,1,1,1),_ChSysCardSlotIndex_Type())
chSysCardSlotIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCardSlotIndex.setStatus(_A)
_ChSysCardType_Type=F10CSeriesCardType
_ChSysCardType_Object=MibTableColumn
chSysCardType=_ChSysCardType_Object((1,3,6,1,4,1,6027,3,8,1,2,1,1,2),_ChSysCardType_Type())
chSysCardType.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCardType.setStatus(_A)
_ChSysCardNumber_Type=Integer32
_ChSysCardNumber_Object=MibTableColumn
chSysCardNumber=_ChSysCardNumber_Object((1,3,6,1,4,1,6027,3,8,1,2,1,1,3),_ChSysCardNumber_Type())
chSysCardNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCardNumber.setStatus(_A)
_ChSysCardNumPorts_Type=Integer32
_ChSysCardNumPorts_Object=MibTableColumn
chSysCardNumPorts=_ChSysCardNumPorts_Object((1,3,6,1,4,1,6027,3,8,1,2,1,1,4),_ChSysCardNumPorts_Type())
chSysCardNumPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCardNumPorts.setStatus(_A)
_ChSysCardTemp_Type=Gauge32
_ChSysCardTemp_Object=MibTableColumn
chSysCardTemp=_ChSysCardTemp_Object((1,3,6,1,4,1,6027,3,8,1,2,1,1,5),_ChSysCardTemp_Type())
chSysCardTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCardTemp.setStatus(_A)
_ChSysCardUpTime_Type=TimeTicks
_ChSysCardUpTime_Object=MibTableColumn
chSysCardUpTime=_ChSysCardUpTime_Object((1,3,6,1,4,1,6027,3,8,1,2,1,1,6),_ChSysCardUpTime_Type())
chSysCardUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCardUpTime.setStatus(_A)
class _ChSysCardAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ChSysCardAdminStatus_Type.__name__=_D
_ChSysCardAdminStatus_Object=MibTableColumn
chSysCardAdminStatus=_ChSysCardAdminStatus_Object((1,3,6,1,4,1,6027,3,8,1,2,1,1,7),_ChSysCardAdminStatus_Type())
chSysCardAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCardAdminStatus.setStatus(_A)
_ChSysCardOperStatus_Type=F10CardOperStatus
_ChSysCardOperStatus_Object=MibTableColumn
chSysCardOperStatus=_ChSysCardOperStatus_Object((1,3,6,1,4,1,6027,3,8,1,2,1,1,8),_ChSysCardOperStatus_Type())
chSysCardOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCardOperStatus.setStatus(_A)
_ChSysCardBootFlashA_Type=DisplayString
_ChSysCardBootFlashA_Object=MibTableColumn
chSysCardBootFlashA=_ChSysCardBootFlashA_Object((1,3,6,1,4,1,6027,3,8,1,2,1,1,9),_ChSysCardBootFlashA_Type())
chSysCardBootFlashA.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCardBootFlashA.setStatus(_A)
_ChSysCardBootFlashB_Type=DisplayString
_ChSysCardBootFlashB_Object=MibTableColumn
chSysCardBootFlashB=_ChSysCardBootFlashB_Object((1,3,6,1,4,1,6027,3,8,1,2,1,1,10),_ChSysCardBootFlashB_Type())
chSysCardBootFlashB.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCardBootFlashB.setStatus(_A)
_ChSysCardSerialNumber_Type=DisplayString
_ChSysCardSerialNumber_Object=MibTableColumn
chSysCardSerialNumber=_ChSysCardSerialNumber_Object((1,3,6,1,4,1,6027,3,8,1,2,1,1,11),_ChSysCardSerialNumber_Type())
chSysCardSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCardSerialNumber.setStatus(_A)
_ChSysCardPartNum_Type=DisplayString
_ChSysCardPartNum_Object=MibTableColumn
chSysCardPartNum=_ChSysCardPartNum_Object((1,3,6,1,4,1,6027,3,8,1,2,1,1,12),_ChSysCardPartNum_Type())
chSysCardPartNum.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCardPartNum.setStatus(_A)
_ChSysCardProductRev_Type=DisplayString
_ChSysCardProductRev_Object=MibTableColumn
chSysCardProductRev=_ChSysCardProductRev_Object((1,3,6,1,4,1,6027,3,8,1,2,1,1,13),_ChSysCardProductRev_Type())
chSysCardProductRev.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCardProductRev.setStatus(_A)
_ChSysCardVendorId_Type=DisplayString
_ChSysCardVendorId_Object=MibTableColumn
chSysCardVendorId=_ChSysCardVendorId_Object((1,3,6,1,4,1,6027,3,8,1,2,1,1,14),_ChSysCardVendorId_Type())
chSysCardVendorId.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCardVendorId.setStatus(_A)
_ChSysCardDateCode_Type=F10MfgDate
_ChSysCardDateCode_Object=MibTableColumn
chSysCardDateCode=_ChSysCardDateCode_Object((1,3,6,1,4,1,6027,3,8,1,2,1,1,15),_ChSysCardDateCode_Type())
chSysCardDateCode.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCardDateCode.setStatus(_A)
class _ChSysCardCountryCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_ChSysCardCountryCode_Type.__name__=_J
_ChSysCardCountryCode_Object=MibTableColumn
chSysCardCountryCode=_ChSysCardCountryCode_Object((1,3,6,1,4,1,6027,3,8,1,2,1,1,16),_ChSysCardCountryCode_Type())
chSysCardCountryCode.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCardCountryCode.setStatus(_A)
class _ChSysCardPiecePartID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_ChSysCardPiecePartID_Type.__name__=_F
_ChSysCardPiecePartID_Object=MibTableColumn
chSysCardPiecePartID=_ChSysCardPiecePartID_Object((1,3,6,1,4,1,6027,3,8,1,2,1,1,17),_ChSysCardPiecePartID_Type())
chSysCardPiecePartID.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCardPiecePartID.setStatus(_A)
class _ChSysCardPPIDRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_ChSysCardPPIDRevision_Type.__name__=_F
_ChSysCardPPIDRevision_Object=MibTableColumn
chSysCardPPIDRevision=_ChSysCardPPIDRevision_Object((1,3,6,1,4,1,6027,3,8,1,2,1,1,18),_ChSysCardPPIDRevision_Type())
chSysCardPPIDRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCardPPIDRevision.setStatus(_A)
class _ChSysCardServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_ChSysCardServiceTag_Type.__name__=_F
_ChSysCardServiceTag_Object=MibTableColumn
chSysCardServiceTag=_ChSysCardServiceTag_Object((1,3,6,1,4,1,6027,3,8,1,2,1,1,19),_ChSysCardServiceTag_Type())
chSysCardServiceTag.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCardServiceTag.setStatus(_A)
class _ChSysCardExpressServiceCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_ChSysCardExpressServiceCode_Type.__name__=_F
_ChSysCardExpressServiceCode_Object=MibTableColumn
chSysCardExpressServiceCode=_ChSysCardExpressServiceCode_Object((1,3,6,1,4,1,6027,3,8,1,2,1,1,20),_ChSysCardExpressServiceCode_Type())
chSysCardExpressServiceCode.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCardExpressServiceCode.setStatus(_A)
_ChSysPortTable_Object=MibTable
chSysPortTable=_ChSysPortTable_Object((1,3,6,1,4,1,6027,3,8,1,2,2))
if mibBuilder.loadTexts:chSysPortTable.setStatus(_A)
_ChSysPortEntry_Object=MibTableRow
chSysPortEntry=_ChSysPortEntry_Object((1,3,6,1,4,1,6027,3,8,1,2,2,1))
chSysPortEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:chSysPortEntry.setStatus(_A)
_ChSysPortSlotIndex_Type=Integer32
_ChSysPortSlotIndex_Object=MibTableColumn
chSysPortSlotIndex=_ChSysPortSlotIndex_Object((1,3,6,1,4,1,6027,3,8,1,2,2,1,1),_ChSysPortSlotIndex_Type())
chSysPortSlotIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPortSlotIndex.setStatus(_A)
_ChSysPortIndex_Type=Integer32
_ChSysPortIndex_Object=MibTableColumn
chSysPortIndex=_ChSysPortIndex_Object((1,3,6,1,4,1,6027,3,8,1,2,2,1,2),_ChSysPortIndex_Type())
chSysPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPortIndex.setStatus(_A)
_ChSysPortType_Type=F10CSeriesPortType
_ChSysPortType_Object=MibTableColumn
chSysPortType=_ChSysPortType_Object((1,3,6,1,4,1,6027,3,8,1,2,2,1,3),_ChSysPortType_Type())
chSysPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPortType.setStatus(_A)
class _ChSysPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ChSysPortAdminStatus_Type.__name__=_D
_ChSysPortAdminStatus_Object=MibTableColumn
chSysPortAdminStatus=_ChSysPortAdminStatus_Object((1,3,6,1,4,1,6027,3,8,1,2,2,1,4),_ChSysPortAdminStatus_Type())
chSysPortAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPortAdminStatus.setStatus(_A)
class _ChSysPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ready',1),('portDown',2),('portProblem',3),('cardProblem',4),('cardDown',5),('notPresent',6)))
_ChSysPortOperStatus_Type.__name__=_D
_ChSysPortOperStatus_Object=MibTableColumn
chSysPortOperStatus=_ChSysPortOperStatus_Object((1,3,6,1,4,1,6027,3,8,1,2,2,1,5),_ChSysPortOperStatus_Type())
chSysPortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPortOperStatus.setStatus(_A)
_ChSysPortIfIndex_Type=Integer32
_ChSysPortIfIndex_Object=MibTableColumn
chSysPortIfIndex=_ChSysPortIfIndex_Object((1,3,6,1,4,1,6027,3,8,1,2,2,1,6),_ChSysPortIfIndex_Type())
chSysPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPortIfIndex.setStatus(_A)
_ChSysXfpRecvPower_Type=F10HundredthdB
_ChSysXfpRecvPower_Object=MibTableColumn
chSysXfpRecvPower=_ChSysXfpRecvPower_Object((1,3,6,1,4,1,6027,3,8,1,2,2,1,7),_ChSysXfpRecvPower_Type())
chSysXfpRecvPower.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysXfpRecvPower.setStatus(_A)
if mibBuilder.loadTexts:chSysXfpRecvPower.setUnits('dB')
_ChSysProcessorTable_Object=MibTable
chSysProcessorTable=_ChSysProcessorTable_Object((1,3,6,1,4,1,6027,3,8,1,2,3))
if mibBuilder.loadTexts:chSysProcessorTable.setStatus(_A)
_ChSysProcessorEntry_Object=MibTableRow
chSysProcessorEntry=_ChSysProcessorEntry_Object((1,3,6,1,4,1,6027,3,8,1,2,3,1))
chSysProcessorEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:chSysProcessorEntry.setStatus(_A)
_ChSysProcessorSlotIndex_Type=Integer32
_ChSysProcessorSlotIndex_Object=MibTableColumn
chSysProcessorSlotIndex=_ChSysProcessorSlotIndex_Object((1,3,6,1,4,1,6027,3,8,1,2,3,1,1),_ChSysProcessorSlotIndex_Type())
chSysProcessorSlotIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysProcessorSlotIndex.setStatus(_A)
_ChSysProcessorIndex_Type=Integer32
_ChSysProcessorIndex_Object=MibTableColumn
chSysProcessorIndex=_ChSysProcessorIndex_Object((1,3,6,1,4,1,6027,3,8,1,2,3,1,2),_ChSysProcessorIndex_Type())
chSysProcessorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysProcessorIndex.setStatus(_A)
_ChSysProcessorModule_Type=F10ProcessorModuleType
_ChSysProcessorModule_Object=MibTableColumn
chSysProcessorModule=_ChSysProcessorModule_Object((1,3,6,1,4,1,6027,3,8,1,2,3,1,3),_ChSysProcessorModule_Type())
chSysProcessorModule.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysProcessorModule.setStatus(_A)
_ChSysProcessorUpTime_Type=TimeTicks
_ChSysProcessorUpTime_Object=MibTableColumn
chSysProcessorUpTime=_ChSysProcessorUpTime_Object((1,3,6,1,4,1,6027,3,8,1,2,3,1,4),_ChSysProcessorUpTime_Type())
chSysProcessorUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysProcessorUpTime.setStatus(_A)
_ChSysProcessorNvramSize_Type=Integer32
_ChSysProcessorNvramSize_Object=MibTableColumn
chSysProcessorNvramSize=_ChSysProcessorNvramSize_Object((1,3,6,1,4,1,6027,3,8,1,2,3,1,5),_ChSysProcessorNvramSize_Type())
chSysProcessorNvramSize.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysProcessorNvramSize.setStatus(_A)
_ChSysProcessorMemSize_Type=Integer32
_ChSysProcessorMemSize_Object=MibTableColumn
chSysProcessorMemSize=_ChSysProcessorMemSize_Object((1,3,6,1,4,1,6027,3,8,1,2,3,1,6),_ChSysProcessorMemSize_Type())
chSysProcessorMemSize.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysProcessorMemSize.setStatus(_A)
_ChSysSwModuleTable_Object=MibTable
chSysSwModuleTable=_ChSysSwModuleTable_Object((1,3,6,1,4,1,6027,3,8,1,2,4))
if mibBuilder.loadTexts:chSysSwModuleTable.setStatus(_A)
_ChSysSwModuleEntry_Object=MibTableRow
chSysSwModuleEntry=_ChSysSwModuleEntry_Object((1,3,6,1,4,1,6027,3,8,1,2,4,1))
chSysSwModuleEntry.setIndexNames((0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:chSysSwModuleEntry.setStatus(_A)
_ChSysSwSlotIndex_Type=Integer32
_ChSysSwSlotIndex_Object=MibTableColumn
chSysSwSlotIndex=_ChSysSwSlotIndex_Object((1,3,6,1,4,1,6027,3,8,1,2,4,1,1),_ChSysSwSlotIndex_Type())
chSysSwSlotIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwSlotIndex.setStatus(_A)
_ChSysSwProcessorIndex_Type=Integer32
_ChSysSwProcessorIndex_Object=MibTableColumn
chSysSwProcessorIndex=_ChSysSwProcessorIndex_Object((1,3,6,1,4,1,6027,3,8,1,2,4,1,2),_ChSysSwProcessorIndex_Type())
chSysSwProcessorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwProcessorIndex.setStatus(_A)
_ChSysSwRuntimeImgVersion_Type=DisplayString
_ChSysSwRuntimeImgVersion_Object=MibTableColumn
chSysSwRuntimeImgVersion=_ChSysSwRuntimeImgVersion_Object((1,3,6,1,4,1,6027,3,8,1,2,4,1,3),_ChSysSwRuntimeImgVersion_Type())
chSysSwRuntimeImgVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwRuntimeImgVersion.setStatus(_A)
_ChSysSwRuntimeImgDate_Type=F10SwDate
_ChSysSwRuntimeImgDate_Object=MibTableColumn
chSysSwRuntimeImgDate=_ChSysSwRuntimeImgDate_Object((1,3,6,1,4,1,6027,3,8,1,2,4,1,4),_ChSysSwRuntimeImgDate_Type())
chSysSwRuntimeImgDate.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwRuntimeImgDate.setStatus(_A)
_ChSysSwCurrentBootImgVersion_Type=DisplayString
_ChSysSwCurrentBootImgVersion_Object=MibTableColumn
chSysSwCurrentBootImgVersion=_ChSysSwCurrentBootImgVersion_Object((1,3,6,1,4,1,6027,3,8,1,2,4,1,5),_ChSysSwCurrentBootImgVersion_Type())
chSysSwCurrentBootImgVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwCurrentBootImgVersion.setStatus(_A)
_ChSysSwCurrentBootImgDate_Type=DateAndTime
_ChSysSwCurrentBootImgDate_Object=MibTableColumn
chSysSwCurrentBootImgDate=_ChSysSwCurrentBootImgDate_Object((1,3,6,1,4,1,6027,3,8,1,2,4,1,6),_ChSysSwCurrentBootImgDate_Type())
chSysSwCurrentBootImgDate.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwCurrentBootImgDate.setStatus(_A)
class _ChSysSwCurrentBootImgStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),(_S,2)))
_ChSysSwCurrentBootImgStatus_Type.__name__=_D
_ChSysSwCurrentBootImgStatus_Object=MibTableColumn
chSysSwCurrentBootImgStatus=_ChSysSwCurrentBootImgStatus_Object((1,3,6,1,4,1,6027,3,8,1,2,4,1,7),_ChSysSwCurrentBootImgStatus_Type())
chSysSwCurrentBootImgStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwCurrentBootImgStatus.setStatus(_A)
_ChSysSwBackupBootImgVersion_Type=DisplayString
_ChSysSwBackupBootImgVersion_Object=MibTableColumn
chSysSwBackupBootImgVersion=_ChSysSwBackupBootImgVersion_Object((1,3,6,1,4,1,6027,3,8,1,2,4,1,8),_ChSysSwBackupBootImgVersion_Type())
chSysSwBackupBootImgVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwBackupBootImgVersion.setStatus(_A)
_ChSysSwBackupBootImgDate_Type=DateAndTime
_ChSysSwBackupBootImgDate_Object=MibTableColumn
chSysSwBackupBootImgDate=_ChSysSwBackupBootImgDate_Object((1,3,6,1,4,1,6027,3,8,1,2,4,1,9),_ChSysSwBackupBootImgDate_Type())
chSysSwBackupBootImgDate.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwBackupBootImgDate.setStatus(_A)
class _ChSysSwBackupBootImgStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),(_S,2)))
_ChSysSwBackupBootImgStatus_Type.__name__=_D
_ChSysSwBackupBootImgStatus_Object=MibTableColumn
chSysSwBackupBootImgStatus=_ChSysSwBackupBootImgStatus_Object((1,3,6,1,4,1,6027,3,8,1,2,4,1,10),_ChSysSwBackupBootImgStatus_Type())
chSysSwBackupBootImgStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwBackupBootImgStatus.setStatus(_A)
class _ChSysSwNextRebootImage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_ChSysSwNextRebootImage_Type.__name__=_D
_ChSysSwNextRebootImage_Object=MibTableColumn
chSysSwNextRebootImage=_ChSysSwNextRebootImage_Object((1,3,6,1,4,1,6027,3,8,1,2,4,1,11),_ChSysSwNextRebootImage_Type())
chSysSwNextRebootImage.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwNextRebootImage.setStatus(_A)
class _ChSysSwCurrentBootImage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_ChSysSwCurrentBootImage_Type.__name__=_D
_ChSysSwCurrentBootImage_Object=MibTableColumn
chSysSwCurrentBootImage=_ChSysSwCurrentBootImage_Object((1,3,6,1,4,1,6027,3,8,1,2,4,1,12),_ChSysSwCurrentBootImage_Type())
chSysSwCurrentBootImage.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwCurrentBootImage.setStatus(_A)
_ChSysPowerSupplyTable_Object=MibTable
chSysPowerSupplyTable=_ChSysPowerSupplyTable_Object((1,3,6,1,4,1,6027,3,8,1,2,5))
if mibBuilder.loadTexts:chSysPowerSupplyTable.setStatus(_A)
_ChSysPowerSupplyEntry_Object=MibTableRow
chSysPowerSupplyEntry=_ChSysPowerSupplyEntry_Object((1,3,6,1,4,1,6027,3,8,1,2,5,1))
chSysPowerSupplyEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:chSysPowerSupplyEntry.setStatus(_A)
_ChSysPowerSupplyIndex_Type=Integer32
_ChSysPowerSupplyIndex_Object=MibTableColumn
chSysPowerSupplyIndex=_ChSysPowerSupplyIndex_Object((1,3,6,1,4,1,6027,3,8,1,2,5,1,1),_ChSysPowerSupplyIndex_Type())
chSysPowerSupplyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPowerSupplyIndex.setStatus(_A)
class _ChSysPowerSupplyOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ChSysPowerSupplyOperStatus_Type.__name__=_D
_ChSysPowerSupplyOperStatus_Object=MibTableColumn
chSysPowerSupplyOperStatus=_ChSysPowerSupplyOperStatus_Object((1,3,6,1,4,1,6027,3,8,1,2,5,1,2),_ChSysPowerSupplyOperStatus_Type())
chSysPowerSupplyOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPowerSupplyOperStatus.setStatus(_A)
class _ChSysPowerSupplyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ac',1),('dc',2),(_W,3)))
_ChSysPowerSupplyType_Type.__name__=_D
_ChSysPowerSupplyType_Object=MibTableColumn
chSysPowerSupplyType=_ChSysPowerSupplyType_Object((1,3,6,1,4,1,6027,3,8,1,2,5,1,3),_ChSysPowerSupplyType_Type())
chSysPowerSupplyType.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPowerSupplyType.setStatus(_A)
class _ChSysPowerSupplyVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_X,1),('version1',2),('version2',3)))
_ChSysPowerSupplyVersion_Type.__name__=_D
_ChSysPowerSupplyVersion_Object=MibTableColumn
chSysPowerSupplyVersion=_ChSysPowerSupplyVersion_Object((1,3,6,1,4,1,6027,3,8,1,2,5,1,4),_ChSysPowerSupplyVersion_Type())
chSysPowerSupplyVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPowerSupplyVersion.setStatus(_A)
class _ChSysPowerSupplyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_X,1),('low',2),('high',3)))
_ChSysPowerSupplyMode_Type.__name__=_D
_ChSysPowerSupplyMode_Object=MibTableColumn
chSysPowerSupplyMode=_ChSysPowerSupplyMode_Object((1,3,6,1,4,1,6027,3,8,1,2,5,1,5),_ChSysPowerSupplyMode_Type())
chSysPowerSupplyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPowerSupplyMode.setStatus(_A)
_ChSysFanTrayTable_Object=MibTable
chSysFanTrayTable=_ChSysFanTrayTable_Object((1,3,6,1,4,1,6027,3,8,1,2,6))
if mibBuilder.loadTexts:chSysFanTrayTable.setStatus(_A)
_ChSysFanTrayEntry_Object=MibTableRow
chSysFanTrayEntry=_ChSysFanTrayEntry_Object((1,3,6,1,4,1,6027,3,8,1,2,6,1))
chSysFanTrayEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:chSysFanTrayEntry.setStatus(_A)
_ChSysFanTrayIndex_Type=Integer32
_ChSysFanTrayIndex_Object=MibTableColumn
chSysFanTrayIndex=_ChSysFanTrayIndex_Object((1,3,6,1,4,1,6027,3,8,1,2,6,1,1),_ChSysFanTrayIndex_Type())
chSysFanTrayIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysFanTrayIndex.setStatus(_A)
class _ChSysFanTrayOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ChSysFanTrayOperStatus_Type.__name__=_D
_ChSysFanTrayOperStatus_Object=MibTableColumn
chSysFanTrayOperStatus=_ChSysFanTrayOperStatus_Object((1,3,6,1,4,1,6027,3,8,1,2,6,1,2),_ChSysFanTrayOperStatus_Type())
chSysFanTrayOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysFanTrayOperStatus.setStatus(_A)
_ChSysSfmTable_Object=MibTable
chSysSfmTable=_ChSysSfmTable_Object((1,3,6,1,4,1,6027,3,8,1,2,7))
if mibBuilder.loadTexts:chSysSfmTable.setStatus(_A)
_ChSysSfmEntry_Object=MibTableRow
chSysSfmEntry=_ChSysSfmEntry_Object((1,3,6,1,4,1,6027,3,8,1,2,7,1))
chSysSfmEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:chSysSfmEntry.setStatus(_A)
_ChSysSfmIndex_Type=Integer32
_ChSysSfmIndex_Object=MibTableColumn
chSysSfmIndex=_ChSysSfmIndex_Object((1,3,6,1,4,1,6027,3,8,1,2,7,1,1),_ChSysSfmIndex_Type())
chSysSfmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSfmIndex.setStatus(_A)
class _ChSysSfmAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ChSysSfmAdminStatus_Type.__name__=_D
_ChSysSfmAdminStatus_Object=MibTableColumn
chSysSfmAdminStatus=_ChSysSfmAdminStatus_Object((1,3,6,1,4,1,6027,3,8,1,2,7,1,2),_ChSysSfmAdminStatus_Type())
chSysSfmAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSfmAdminStatus.setStatus(_A)
class _ChSysSfmOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),(_W,2),('standby',3)))
_ChSysSfmOperStatus_Type.__name__=_D
_ChSysSfmOperStatus_Object=MibTableColumn
chSysSfmOperStatus=_ChSysSfmOperStatus_Object((1,3,6,1,4,1,6027,3,8,1,2,7,1,3),_ChSysSfmOperStatus_Type())
chSysSfmOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSfmOperStatus.setStatus(_A)
class _ChSysSfmErrorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ok',1),('error',2),('not-available',3)))
_ChSysSfmErrorStatus_Type.__name__=_D
_ChSysSfmErrorStatus_Object=MibTableColumn
chSysSfmErrorStatus=_ChSysSfmErrorStatus_Object((1,3,6,1,4,1,6027,3,8,1,2,7,1,4),_ChSysSfmErrorStatus_Type())
chSysSfmErrorStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSfmErrorStatus.setStatus(_A)
_ChRpmObjects_ObjectIdentity=ObjectIdentity
chRpmObjects=_ChRpmObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,8,1,3))
_ChRpmNumRpms_Type=Integer32
_ChRpmNumRpms_Object=MibScalar
chRpmNumRpms=_ChRpmNumRpms_Object((1,3,6,1,4,1,6027,3,8,1,3,1),_ChRpmNumRpms_Type())
chRpmNumRpms.setMaxAccess(_C)
if mibBuilder.loadTexts:chRpmNumRpms.setStatus(_A)
_ChRpmSlotNumber_Type=Integer32
_ChRpmSlotNumber_Object=MibScalar
chRpmSlotNumber=_ChRpmSlotNumber_Object((1,3,6,1,4,1,6027,3,8,1,3,2),_ChRpmSlotNumber_Type())
chRpmSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:chRpmSlotNumber.setStatus(_A)
_ChRpmUptime_Type=TimeTicks
_ChRpmUptime_Object=MibScalar
chRpmUptime=_ChRpmUptime_Object((1,3,6,1,4,1,6027,3,8,1,3,3),_ChRpmUptime_Type())
chRpmUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:chRpmUptime.setStatus(_A)
_ChRpmLastSwitchDate_Type=DateAndTime
_ChRpmLastSwitchDate_Object=MibScalar
chRpmLastSwitchDate=_ChRpmLastSwitchDate_Object((1,3,6,1,4,1,6027,3,8,1,3,4),_ChRpmLastSwitchDate_Type())
chRpmLastSwitchDate.setMaxAccess(_C)
if mibBuilder.loadTexts:chRpmLastSwitchDate.setStatus(_A)
class _ChRpmMajorAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_ChRpmMajorAlarmStatus_Type.__name__=_D
_ChRpmMajorAlarmStatus_Object=MibScalar
chRpmMajorAlarmStatus=_ChRpmMajorAlarmStatus_Object((1,3,6,1,4,1,6027,3,8,1,3,5),_ChRpmMajorAlarmStatus_Type())
chRpmMajorAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chRpmMajorAlarmStatus.setStatus(_A)
class _ChRpmMinorAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_ChRpmMinorAlarmStatus_Type.__name__=_D
_ChRpmMinorAlarmStatus_Object=MibScalar
chRpmMinorAlarmStatus=_ChRpmMinorAlarmStatus_Object((1,3,6,1,4,1,6027,3,8,1,3,6),_ChRpmMinorAlarmStatus_Type())
chRpmMinorAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chRpmMinorAlarmStatus.setStatus(_A)
_ChRpmUtilTable_Object=MibTable
chRpmUtilTable=_ChRpmUtilTable_Object((1,3,6,1,4,1,6027,3,8,1,3,7))
if mibBuilder.loadTexts:chRpmUtilTable.setStatus(_A)
_ChRpmUtilEntry_Object=MibTableRow
chRpmUtilEntry=_ChRpmUtilEntry_Object((1,3,6,1,4,1,6027,3,8,1,3,7,1))
chRpmUtilEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:chRpmUtilEntry.setStatus(_A)
_ChRpmCpuIndex_Type=Integer32
_ChRpmCpuIndex_Object=MibTableColumn
chRpmCpuIndex=_ChRpmCpuIndex_Object((1,3,6,1,4,1,6027,3,8,1,3,7,1,1),_ChRpmCpuIndex_Type())
chRpmCpuIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chRpmCpuIndex.setStatus(_A)
_ChRpmCpuType_Type=F10ProcessorModuleType
_ChRpmCpuType_Object=MibTableColumn
chRpmCpuType=_ChRpmCpuType_Object((1,3,6,1,4,1,6027,3,8,1,3,7,1,2),_ChRpmCpuType_Type())
chRpmCpuType.setMaxAccess(_C)
if mibBuilder.loadTexts:chRpmCpuType.setStatus(_A)
class _ChRpmCpuUtil5Sec_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ChRpmCpuUtil5Sec_Type.__name__=_E
_ChRpmCpuUtil5Sec_Object=MibTableColumn
chRpmCpuUtil5Sec=_ChRpmCpuUtil5Sec_Object((1,3,6,1,4,1,6027,3,8,1,3,7,1,3),_ChRpmCpuUtil5Sec_Type())
chRpmCpuUtil5Sec.setMaxAccess(_C)
if mibBuilder.loadTexts:chRpmCpuUtil5Sec.setStatus(_A)
if mibBuilder.loadTexts:chRpmCpuUtil5Sec.setUnits(_G)
class _ChRpmCpuUtil1Min_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ChRpmCpuUtil1Min_Type.__name__=_E
_ChRpmCpuUtil1Min_Object=MibTableColumn
chRpmCpuUtil1Min=_ChRpmCpuUtil1Min_Object((1,3,6,1,4,1,6027,3,8,1,3,7,1,4),_ChRpmCpuUtil1Min_Type())
chRpmCpuUtil1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:chRpmCpuUtil1Min.setStatus(_A)
if mibBuilder.loadTexts:chRpmCpuUtil1Min.setUnits(_G)
class _ChRpmCpuUtil5Min_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ChRpmCpuUtil5Min_Type.__name__=_E
_ChRpmCpuUtil5Min_Object=MibTableColumn
chRpmCpuUtil5Min=_ChRpmCpuUtil5Min_Object((1,3,6,1,4,1,6027,3,8,1,3,7,1,5),_ChRpmCpuUtil5Min_Type())
chRpmCpuUtil5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:chRpmCpuUtil5Min.setStatus(_A)
if mibBuilder.loadTexts:chRpmCpuUtil5Min.setUnits(_G)
class _ChRpmMemUsageUtil_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ChRpmMemUsageUtil_Type.__name__=_E
_ChRpmMemUsageUtil_Object=MibTableColumn
chRpmMemUsageUtil=_ChRpmMemUsageUtil_Object((1,3,6,1,4,1,6027,3,8,1,3,7,1,6),_ChRpmMemUsageUtil_Type())
chRpmMemUsageUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:chRpmMemUsageUtil.setStatus(_A)
if mibBuilder.loadTexts:chRpmMemUsageUtil.setUnits(_G)
_ChAlarmObjects_ObjectIdentity=ObjectIdentity
chAlarmObjects=_ChAlarmObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,8,1,4))
_ChLineCardObjects_ObjectIdentity=ObjectIdentity
chLineCardObjects=_ChLineCardObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,8,1,5))
_ChLineCardUtilTable_Object=MibTable
chLineCardUtilTable=_ChLineCardUtilTable_Object((1,3,6,1,4,1,6027,3,8,1,5,1))
if mibBuilder.loadTexts:chLineCardUtilTable.setStatus(_A)
_ChLineCardUtilEntry_Object=MibTableRow
chLineCardUtilEntry=_ChLineCardUtilEntry_Object((1,3,6,1,4,1,6027,3,8,1,5,1,1))
chLineCardUtilEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:chLineCardUtilEntry.setStatus(_A)
class _ChLineCardCpuUtil5Sec_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ChLineCardCpuUtil5Sec_Type.__name__=_E
_ChLineCardCpuUtil5Sec_Object=MibTableColumn
chLineCardCpuUtil5Sec=_ChLineCardCpuUtil5Sec_Object((1,3,6,1,4,1,6027,3,8,1,5,1,1,1),_ChLineCardCpuUtil5Sec_Type())
chLineCardCpuUtil5Sec.setMaxAccess(_C)
if mibBuilder.loadTexts:chLineCardCpuUtil5Sec.setStatus(_A)
if mibBuilder.loadTexts:chLineCardCpuUtil5Sec.setUnits(_G)
class _ChLineCardCpuUtil1Min_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ChLineCardCpuUtil1Min_Type.__name__=_E
_ChLineCardCpuUtil1Min_Object=MibTableColumn
chLineCardCpuUtil1Min=_ChLineCardCpuUtil1Min_Object((1,3,6,1,4,1,6027,3,8,1,5,1,1,2),_ChLineCardCpuUtil1Min_Type())
chLineCardCpuUtil1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:chLineCardCpuUtil1Min.setStatus(_A)
if mibBuilder.loadTexts:chLineCardCpuUtil1Min.setUnits(_G)
class _ChLineCardCpuUtil5Min_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ChLineCardCpuUtil5Min_Type.__name__=_E
_ChLineCardCpuUtil5Min_Object=MibTableColumn
chLineCardCpuUtil5Min=_ChLineCardCpuUtil5Min_Object((1,3,6,1,4,1,6027,3,8,1,5,1,1,3),_ChLineCardCpuUtil5Min_Type())
chLineCardCpuUtil5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:chLineCardCpuUtil5Min.setStatus(_A)
if mibBuilder.loadTexts:chLineCardCpuUtil5Min.setUnits(_G)
class _ChLineCardMemUsageUtil_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ChLineCardMemUsageUtil_Type.__name__=_E
_ChLineCardMemUsageUtil_Object=MibTableColumn
chLineCardMemUsageUtil=_ChLineCardMemUsageUtil_Object((1,3,6,1,4,1,6027,3,8,1,5,1,1,4),_ChLineCardMemUsageUtil_Type())
chLineCardMemUsageUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:chLineCardMemUsageUtil.setStatus(_A)
if mibBuilder.loadTexts:chLineCardMemUsageUtil.setUnits(_G)
_F10CSerChassisMibConformance_ObjectIdentity=ObjectIdentity
f10CSerChassisMibConformance=_F10CSerChassisMibConformance_ObjectIdentity((1,3,6,1,4,1,6027,3,8,2))
_F10CSerChassisMibCompliances_ObjectIdentity=ObjectIdentity
f10CSerChassisMibCompliances=_F10CSerChassisMibCompliances_ObjectIdentity((1,3,6,1,4,1,6027,3,8,2,1))
_F10CSerChassisMibGroups_ObjectIdentity=ObjectIdentity
f10CSerChassisMibGroups=_F10CSerChassisMibGroups_ObjectIdentity((1,3,6,1,4,1,6027,3,8,2,2))
f10CSerComponentGroup=ObjectGroup((1,3,6,1,4,1,6027,3,8,2,2,1))
f10CSerComponentGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:f10CSerComponentGroup.setStatus(_A)
f10CSerSystemGroup=ObjectGroup((1,3,6,1,4,1,6027,3,8,2,2,2))
f10CSerSystemGroup.setObjects(*((_B,_u),(_B,_K),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac)))
if mibBuilder.loadTexts:f10CSerSystemGroup.setStatus(_A)
f10CSerRpmGroup=ObjectGroup((1,3,6,1,4,1,6027,3,8,2,2,3))
f10CSerRpmGroup.setObjects(*((_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An)))
if mibBuilder.loadTexts:f10CSerRpmGroup.setStatus(_A)
f10CSerLineCardGroup=ObjectGroup((1,3,6,1,4,1,6027,3,8,2,2,4))
f10CSerLineCardGroup.setObjects(*((_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar)))
if mibBuilder.loadTexts:f10CSerLineCardGroup.setStatus(_A)
f10CSerChassisMibCompliance=ModuleCompliance((1,3,6,1,4,1,6027,3,8,2,1,1))
f10CSerChassisMibCompliance.setObjects(*((_B,_As),(_B,_At),(_B,_Au),(_B,_Av)))
if mibBuilder.loadTexts:f10CSerChassisMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'f10CSerChassisMib':f10CSerChassisMib,'f10CSerChassisObject':f10CSerChassisObject,'chObjects':chObjects,_b:chType,_c:chChassisMode,_d:chSwVersion,_e:chMacAddr,_f:chSerialNumber,_g:chPartNum,_h:chProductRev,_i:chVendorId,_j:chDateCode,_k:chCountryCode,_p:chNumSlots,_q:chNumLinecards,_r:chNumFanTrays,_s:chNumPowerSupplies,_t:chNumSfmSlots,_l:chPiecePartID,_m:chPPIDRevision,_n:chServiceTag,_o:chExpressServiceCode,'chSysObjects':chSysObjects,'chSysCardTable':chSysCardTable,'chSysCardEntry':chSysCardEntry,_L:chSysCardSlotIndex,_u:chSysCardType,_K:chSysCardNumber,_v:chSysCardNumPorts,_w:chSysCardTemp,_x:chSysCardUpTime,_y:chSysCardAdminStatus,_z:chSysCardOperStatus,_A0:chSysCardBootFlashA,_A1:chSysCardBootFlashB,_A2:chSysCardSerialNumber,_A3:chSysCardPartNum,_A4:chSysCardProductRev,_A5:chSysCardVendorId,_A6:chSysCardDateCode,_A7:chSysCardCountryCode,_A8:chSysCardPiecePartID,_A9:chSysCardPPIDRevision,_AA:chSysCardServiceTag,_AB:chSysCardExpressServiceCode,'chSysPortTable':chSysPortTable,'chSysPortEntry':chSysPortEntry,_M:chSysPortSlotIndex,_N:chSysPortIndex,_AC:chSysPortType,_AD:chSysPortAdminStatus,_AE:chSysPortOperStatus,_AF:chSysPortIfIndex,_AG:chSysXfpRecvPower,'chSysProcessorTable':chSysProcessorTable,'chSysProcessorEntry':chSysProcessorEntry,_O:chSysProcessorSlotIndex,_P:chSysProcessorIndex,_AH:chSysProcessorModule,_AI:chSysProcessorUpTime,_AJ:chSysProcessorNvramSize,_AK:chSysProcessorMemSize,'chSysSwModuleTable':chSysSwModuleTable,'chSysSwModuleEntry':chSysSwModuleEntry,_Q:chSysSwSlotIndex,_R:chSysSwProcessorIndex,_AL:chSysSwRuntimeImgVersion,_AM:chSysSwRuntimeImgDate,_AN:chSysSwCurrentBootImgVersion,_AO:chSysSwCurrentBootImgDate,_AP:chSysSwCurrentBootImgStatus,_AQ:chSysSwBackupBootImgVersion,_AR:chSysSwBackupBootImgDate,_AS:chSysSwBackupBootImgStatus,_AT:chSysSwNextRebootImage,_AU:chSysSwCurrentBootImage,'chSysPowerSupplyTable':chSysPowerSupplyTable,'chSysPowerSupplyEntry':chSysPowerSupplyEntry,_V:chSysPowerSupplyIndex,_AV:chSysPowerSupplyOperStatus,_AW:chSysPowerSupplyType,_AX:chSysPowerSupplyVersion,_AY:chSysPowerSupplyMode,'chSysFanTrayTable':chSysFanTrayTable,'chSysFanTrayEntry':chSysFanTrayEntry,_Y:chSysFanTrayIndex,_AZ:chSysFanTrayOperStatus,'chSysSfmTable':chSysSfmTable,'chSysSfmEntry':chSysSfmEntry,_Z:chSysSfmIndex,_Aa:chSysSfmAdminStatus,_Ab:chSysSfmOperStatus,_Ac:chSysSfmErrorStatus,'chRpmObjects':chRpmObjects,_Ad:chRpmNumRpms,_Ae:chRpmSlotNumber,_Af:chRpmUptime,_Ag:chRpmLastSwitchDate,_Ah:chRpmMajorAlarmStatus,_Ai:chRpmMinorAlarmStatus,'chRpmUtilTable':chRpmUtilTable,'chRpmUtilEntry':chRpmUtilEntry,_a:chRpmCpuIndex,_Aj:chRpmCpuType,_Ak:chRpmCpuUtil5Sec,_Al:chRpmCpuUtil1Min,_Am:chRpmCpuUtil5Min,_An:chRpmMemUsageUtil,'chAlarmObjects':chAlarmObjects,'chLineCardObjects':chLineCardObjects,'chLineCardUtilTable':chLineCardUtilTable,'chLineCardUtilEntry':chLineCardUtilEntry,_Ao:chLineCardCpuUtil5Sec,_Ap:chLineCardCpuUtil1Min,_Aq:chLineCardCpuUtil5Min,_Ar:chLineCardMemUsageUtil,'f10CSerChassisMibConformance':f10CSerChassisMibConformance,'f10CSerChassisMibCompliances':f10CSerChassisMibCompliances,'f10CSerChassisMibCompliance':f10CSerChassisMibCompliance,'f10CSerChassisMibGroups':f10CSerChassisMibGroups,_As:f10CSerComponentGroup,_At:f10CSerSystemGroup,_Au:f10CSerRpmGroup,_Av:f10CSerLineCardGroup})