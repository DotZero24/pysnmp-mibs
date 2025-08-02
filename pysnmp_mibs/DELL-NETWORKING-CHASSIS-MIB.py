_BA='dellNetChassisNotificationGroup'
_B9='dellNetSystemGroup'
_B8='dellNetComponentGroup'
_B7='dellNetSysAlarmCpuCLkDegraded'
_B6='dellNetSysAlarmStackUnitRoleChanged'
_B5='dellNetSysAlarmVrrpGiveupMaster'
_B4='dellNetSysAlarmVrrpGoMaster'
_B3='dellNetSysAlarmAcDcMixedPowerSupplyDetect'
_B2='dellNetSysAlarmSRAMParityErrorDetect'
_B1='dellNetSysAlarmCutoff'
_B0='dellNetSysAlarmCardProblem'
_A_='dellNetSysAlarmCardRemove'
_Az='dellNetSysAlarmCardReset'
_Ay='dellNetSysAlarmMacStationMove'
_Ax='dellNetSysAlarmTaskTerm'
_Aw='dellNetSysAlarmTaskSuspend'
_Av='dellNetSysAlarmClrMemThreshold'
_Au='dellNetSysAlarmExdMemThreshold'
_At='dellNetSysAlarmClrCpuThreshold'
_As='dellNetSysAlarmExdCpuThreshold'
_Ar='dellNetSysAlarmPEDown'
_Aq='dellNetSysAlarmPEUp'
_Ap='dellNetSysAlarmPEUnitDown'
_Ao='dellNetSysAlarmPEUnitUp'
_An='dellNetSysAlarmUnsupportedOptic'
_Am='dellNetSysAlarmCardVersionMismatch'
_Al='dellNetSysSnmpIpAclDeny'
_Ak='dellNetSysAlarmRpmPrimary'
_Aj='dellNetSysAlarmMinorFanBad'
_Ai='dellNetSysAlarmMinorPSClr'
_Ah='dellNetSysAlarmMinorPS'
_Ag='dellNetSysAlarmMajorPSClr'
_Af='dellNetSysAlarmMajorPS'
_Ae='dellNetSysAlarmMinorFanBadClear'
_Ad='dellNetSysAlarmFanTrayClear'
_Ac='dellNetSysAlarmMajorTemperatureClear'
_Ab='dellNetSysAlarmMinorTemperatureClear'
_Aa='dellNetSysAlarmPowersupplyClear'
_AZ='dellNetSysAlarmFanTrayDown'
_AY='dellNetSysAlarmMajorTemperatureHigh'
_AX='dellNetSysAlarmMinorTemperatureHigh'
_AW='dellNetSysAlarmPowersupplyDown'
_AV='dellNetSysAlarmRpmDown'
_AU='dellNetSysAlarmRpmUp'
_AT='dellNetSysAlarmCardMismatch'
_AS='dellNetSysAlarmCardOffline'
_AR='dellNetSysAlarmCardUp'
_AQ='dellNetSysAlarmCardDown'
_AP='dellNetStackUnitMgmtStatus'
_AO='dellNetFanTrayExpressServiceCode'
_AN='dellNetFanTrayServiceTag'
_AM='dellNetFanTrayPPIDRevision'
_AL='dellNetFanTrayPiecePartID'
_AK='dellNetFanTrayOperStatus'
_AJ='dellNetPowerSupplyUsage'
_AI='dellNetPowerSupplyExpressServiceCode'
_AH='dellNetPowerSupplyServiceTag'
_AG='dellNetPowerSupplyPPIDRevision'
_AF='dellNetPowerSupplyPiecePartID'
_AE='dellNetPowerSupplyType'
_AD='dellNetPowerSupplyOperStatus'
_AC='dellNetSwModuleInPartitionBImgVers'
_AB='dellNetSwModuleInPartitionAImgVers'
_AA='dellNetSwModuleCurrentBootImage'
_A9='dellNetSwModuleNextRebootImage'
_A8='dellNetSwModuleBootSelectorImgVersion'
_A7='dellNetSwModuleBootFlashImgVersion'
_A6='dellNetSwModuleRuntimeImgDate'
_A5='dellNetSwModuleRuntimeImgVersion'
_A4='dellNetCpuUtilMemUsage'
_A3='dellNetCpuUtil5Min'
_A2='dellNetCpuUtil1Min'
_A1='dellNetCpuUtil5Sec'
_A0='dellNetProcessorMemSize'
_z='dellNetProcessorUpTime'
_y='dellNetProcessorModule'
_x='dellNetDeviceType'
_w='dellNetSysCoresInstance'
_v='dellNetFlashPartitionNumber'
_u='dellNetFanTrayIndex'
_t='dellNetFanDeviceIndex'
_s='dellNetFanDeviceType'
_r='absent'
_q='dellNetPowerSupplyIndex'
_p='dellNetPowerDeviceIndex'
_o='dellNetPowerDeviceType'
_n='networkBoot'
_m='partitionB'
_l='partitionA'
_k='dellNetPEIndex'
_j='dellNetPEBindCascadePortIfIndex'
_i='ethernet'
_h='dellNetStackPortIndex'
_g='notPresent'
_f='degrees Centigrade'
_e='dellNetCardIndex'
_d='ifIndex'
_c='IF-MIB'
_b='dellNetsysAlarmVarFanId'
_a='dellNetProcessorIndex'
_Z='unknown'
_Y='dellNetChassisIndex'
_X='dellNetProcessorDeviceIndex'
_W='dellNetProcessorDeviceType'
_V='down'
_U='up'
_T='dellNetStackUnitNumber'
_S='OctetString'
_R='percent'
_Q='Gauge32'
_P='dellNetsysAlarmVarFanTrayId'
_O='dellNetsysAlarmVarPsuId'
_N='accessible-for-notify'
_M='deprecated'
_L='not-accessible'
_K='Integer32'
_J='dellNetSysAlarmVarPort'
_I='DisplayString'
_H='dellNetSysAlarmVarPeId'
_G='dellNetSysAlarmVarSlot'
_F='dellNetSysAlarmVarChassisId'
_E='dellNetSysAlarmVarInteger'
_D='dellNetSysAlarmVarString'
_C='read-only'
_B='current'
_A='DELL-NETWORKING-CHASSIS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_S,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dellNetMgmt,=mibBuilder.importSymbols('DELL-NETWORKING-SMI','dellNetMgmt')
DellNetCardOperStatus,DellNetChassisType,DellNetDeviceType,DellNetHundredthdB,DellNetIfType,DellNetMfgDate,DellNetPEOperStatus,DellNetProcessorModuleType,DellNetSwDate,DellNetSystemCardType=mibBuilder.importSymbols('DELL-NETWORKING-TC','DellNetCardOperStatus','DellNetChassisType','DellNetDeviceType','DellNetHundredthdB','DellNetIfType','DellNetMfgDate','DellNetPEOperStatus','DellNetProcessorModuleType','DellNetSwDate','DellNetSystemCardType')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_c,'InterfaceIndex',_d)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_Q,_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_I,'MacAddress','PhysAddress','TextualConvention')
dellNetChassisMib=ModuleIdentity((1,3,6,1,4,1,6027,3,26))
if mibBuilder.loadTexts:dellNetChassisMib.setRevisions(('2014-08-05 12:00',))
_DellNetSysObject_ObjectIdentity=ObjectIdentity
dellNetSysObject=_DellNetSysObject_ObjectIdentity((1,3,6,1,4,1,6027,3,26,1))
_DellNetSysParameter_ObjectIdentity=ObjectIdentity
dellNetSysParameter=_DellNetSysParameter_ObjectIdentity((1,3,6,1,4,1,6027,3,26,1,1))
_DellNetDeviceType_Type=DellNetDeviceType
_DellNetDeviceType_Object=MibScalar
dellNetDeviceType=_DellNetDeviceType_Object((1,3,6,1,4,1,6027,3,26,1,1,1),_DellNetDeviceType_Type())
dellNetDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetDeviceType.setStatus(_B)
_DellNetChassisObject_ObjectIdentity=ObjectIdentity
dellNetChassisObject=_DellNetChassisObject_ObjectIdentity((1,3,6,1,4,1,6027,3,26,1,2))
_DellNetNumChassis_Type=Integer32
_DellNetNumChassis_Object=MibScalar
dellNetNumChassis=_DellNetNumChassis_Object((1,3,6,1,4,1,6027,3,26,1,2,1),_DellNetNumChassis_Type())
dellNetNumChassis.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetNumChassis.setStatus(_B)
_DellNetMaxNumChassis_Type=Integer32
_DellNetMaxNumChassis_Object=MibScalar
dellNetMaxNumChassis=_DellNetMaxNumChassis_Object((1,3,6,1,4,1,6027,3,26,1,2,2),_DellNetMaxNumChassis_Type())
dellNetMaxNumChassis.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetMaxNumChassis.setStatus(_B)
_DellNetChassisTable_Object=MibTable
dellNetChassisTable=_DellNetChassisTable_Object((1,3,6,1,4,1,6027,3,26,1,2,3))
if mibBuilder.loadTexts:dellNetChassisTable.setStatus(_B)
_DellNetChassisEntry_Object=MibTableRow
dellNetChassisEntry=_DellNetChassisEntry_Object((1,3,6,1,4,1,6027,3,26,1,2,3,1))
dellNetChassisEntry.setIndexNames((0,_A,_Y))
if mibBuilder.loadTexts:dellNetChassisEntry.setStatus(_B)
_DellNetChassisIndex_Type=Integer32
_DellNetChassisIndex_Object=MibTableColumn
dellNetChassisIndex=_DellNetChassisIndex_Object((1,3,6,1,4,1,6027,3,26,1,2,3,1,1),_DellNetChassisIndex_Type())
dellNetChassisIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetChassisIndex.setStatus(_B)
_DellNetChassisType_Type=DellNetChassisType
_DellNetChassisType_Object=MibTableColumn
dellNetChassisType=_DellNetChassisType_Object((1,3,6,1,4,1,6027,3,26,1,2,3,1,2),_DellNetChassisType_Type())
dellNetChassisType.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetChassisType.setStatus(_B)
_DellNetChassisMacAddr_Type=MacAddress
_DellNetChassisMacAddr_Object=MibTableColumn
dellNetChassisMacAddr=_DellNetChassisMacAddr_Object((1,3,6,1,4,1,6027,3,26,1,2,3,1,3),_DellNetChassisMacAddr_Type())
dellNetChassisMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetChassisMacAddr.setStatus(_B)
class _DellNetChassisSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_DellNetChassisSerialNumber_Type.__name__=_I
_DellNetChassisSerialNumber_Object=MibTableColumn
dellNetChassisSerialNumber=_DellNetChassisSerialNumber_Object((1,3,6,1,4,1,6027,3,26,1,2,3,1,4),_DellNetChassisSerialNumber_Type())
dellNetChassisSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetChassisSerialNumber.setStatus(_B)
class _DellNetChassisPartNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_DellNetChassisPartNum_Type.__name__=_I
_DellNetChassisPartNum_Object=MibTableColumn
dellNetChassisPartNum=_DellNetChassisPartNum_Object((1,3,6,1,4,1,6027,3,26,1,2,3,1,5),_DellNetChassisPartNum_Type())
dellNetChassisPartNum.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetChassisPartNum.setStatus(_B)
class _DellNetChassisProductRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_DellNetChassisProductRev_Type.__name__=_I
_DellNetChassisProductRev_Object=MibTableColumn
dellNetChassisProductRev=_DellNetChassisProductRev_Object((1,3,6,1,4,1,6027,3,26,1,2,3,1,6),_DellNetChassisProductRev_Type())
dellNetChassisProductRev.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetChassisProductRev.setStatus(_B)
class _DellNetChassisVendorId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_DellNetChassisVendorId_Type.__name__=_I
_DellNetChassisVendorId_Object=MibTableColumn
dellNetChassisVendorId=_DellNetChassisVendorId_Object((1,3,6,1,4,1,6027,3,26,1,2,3,1,7),_DellNetChassisVendorId_Type())
dellNetChassisVendorId.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetChassisVendorId.setStatus(_B)
_DellNetChassisMfgDate_Type=DellNetMfgDate
_DellNetChassisMfgDate_Object=MibTableColumn
dellNetChassisMfgDate=_DellNetChassisMfgDate_Object((1,3,6,1,4,1,6027,3,26,1,2,3,1,8),_DellNetChassisMfgDate_Type())
dellNetChassisMfgDate.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetChassisMfgDate.setStatus(_B)
class _DellNetChassisCountryCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_DellNetChassisCountryCode_Type.__name__=_I
_DellNetChassisCountryCode_Object=MibTableColumn
dellNetChassisCountryCode=_DellNetChassisCountryCode_Object((1,3,6,1,4,1,6027,3,26,1,2,3,1,9),_DellNetChassisCountryCode_Type())
dellNetChassisCountryCode.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetChassisCountryCode.setStatus(_B)
class _DellNetChassisPPIDRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_DellNetChassisPPIDRev_Type.__name__=_I
_DellNetChassisPPIDRev_Object=MibTableColumn
dellNetChassisPPIDRev=_DellNetChassisPPIDRev_Object((1,3,6,1,4,1,6027,3,26,1,2,3,1,10),_DellNetChassisPPIDRev_Type())
dellNetChassisPPIDRev.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetChassisPPIDRev.setStatus(_B)
class _DellNetChassisServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_DellNetChassisServiceTag_Type.__name__=_I
_DellNetChassisServiceTag_Object=MibTableColumn
dellNetChassisServiceTag=_DellNetChassisServiceTag_Object((1,3,6,1,4,1,6027,3,26,1,2,3,1,11),_DellNetChassisServiceTag_Type())
dellNetChassisServiceTag.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetChassisServiceTag.setStatus(_B)
class _DellNetChassisExpServiceCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_DellNetChassisExpServiceCode_Type.__name__=_I
_DellNetChassisExpServiceCode_Object=MibTableColumn
dellNetChassisExpServiceCode=_DellNetChassisExpServiceCode_Object((1,3,6,1,4,1,6027,3,26,1,2,3,1,12),_DellNetChassisExpServiceCode_Type())
dellNetChassisExpServiceCode.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetChassisExpServiceCode.setStatus(_B)
_DellNetChassisNumSlots_Type=Integer32
_DellNetChassisNumSlots_Object=MibTableColumn
dellNetChassisNumSlots=_DellNetChassisNumSlots_Object((1,3,6,1,4,1,6027,3,26,1,2,3,1,13),_DellNetChassisNumSlots_Type())
dellNetChassisNumSlots.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetChassisNumSlots.setStatus(_B)
_DellNetChassisNumLineCardSlots_Type=Integer32
_DellNetChassisNumLineCardSlots_Object=MibTableColumn
dellNetChassisNumLineCardSlots=_DellNetChassisNumLineCardSlots_Object((1,3,6,1,4,1,6027,3,26,1,2,3,1,14),_DellNetChassisNumLineCardSlots_Type())
dellNetChassisNumLineCardSlots.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetChassisNumLineCardSlots.setStatus(_B)
_DellNetChassisNumFanTrays_Type=Integer32
_DellNetChassisNumFanTrays_Object=MibTableColumn
dellNetChassisNumFanTrays=_DellNetChassisNumFanTrays_Object((1,3,6,1,4,1,6027,3,26,1,2,3,1,15),_DellNetChassisNumFanTrays_Type())
dellNetChassisNumFanTrays.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetChassisNumFanTrays.setStatus(_B)
_DellNetChassisNumPowerSupplies_Type=Integer32
_DellNetChassisNumPowerSupplies_Object=MibTableColumn
dellNetChassisNumPowerSupplies=_DellNetChassisNumPowerSupplies_Object((1,3,6,1,4,1,6027,3,26,1,2,3,1,16),_DellNetChassisNumPowerSupplies_Type())
dellNetChassisNumPowerSupplies.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetChassisNumPowerSupplies.setStatus(_B)
_DellNetCardTable_Object=MibTable
dellNetCardTable=_DellNetCardTable_Object((1,3,6,1,4,1,6027,3,26,1,2,4))
if mibBuilder.loadTexts:dellNetCardTable.setStatus(_B)
_DellNetCardEntry_Object=MibTableRow
dellNetCardEntry=_DellNetCardEntry_Object((1,3,6,1,4,1,6027,3,26,1,2,4,1))
dellNetCardEntry.setIndexNames((0,_A,_Y),(0,_A,_e))
if mibBuilder.loadTexts:dellNetCardEntry.setStatus(_B)
_DellNetCardIndex_Type=Integer32
_DellNetCardIndex_Object=MibTableColumn
dellNetCardIndex=_DellNetCardIndex_Object((1,3,6,1,4,1,6027,3,26,1,2,4,1,1),_DellNetCardIndex_Type())
dellNetCardIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:dellNetCardIndex.setStatus(_B)
_DellNetCardType_Type=DellNetSystemCardType
_DellNetCardType_Object=MibTableColumn
dellNetCardType=_DellNetCardType_Object((1,3,6,1,4,1,6027,3,26,1,2,4,1,2),_DellNetCardType_Type())
dellNetCardType.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetCardType.setStatus(_B)
class _DellNetCardDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_DellNetCardDescription_Type.__name__=_I
_DellNetCardDescription_Object=MibTableColumn
dellNetCardDescription=_DellNetCardDescription_Object((1,3,6,1,4,1,6027,3,26,1,2,4,1,3),_DellNetCardDescription_Type())
dellNetCardDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetCardDescription.setStatus(_B)
_DellNetCardChassisIndex_Type=Integer32
_DellNetCardChassisIndex_Object=MibTableColumn
dellNetCardChassisIndex=_DellNetCardChassisIndex_Object((1,3,6,1,4,1,6027,3,26,1,2,4,1,4),_DellNetCardChassisIndex_Type())
dellNetCardChassisIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:dellNetCardChassisIndex.setStatus(_B)
_DellNetCardStatus_Type=DellNetCardOperStatus
_DellNetCardStatus_Object=MibTableColumn
dellNetCardStatus=_DellNetCardStatus_Object((1,3,6,1,4,1,6027,3,26,1,2,4,1,5),_DellNetCardStatus_Type())
dellNetCardStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetCardStatus.setStatus(_B)
_DellNetCardTemp_Type=Integer32
_DellNetCardTemp_Object=MibTableColumn
dellNetCardTemp=_DellNetCardTemp_Object((1,3,6,1,4,1,6027,3,26,1,2,4,1,6),_DellNetCardTemp_Type())
dellNetCardTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetCardTemp.setStatus(_B)
if mibBuilder.loadTexts:dellNetCardTemp.setUnits(_f)
_DellNetCardVendorId_Type=DisplayString
_DellNetCardVendorId_Object=MibTableColumn
dellNetCardVendorId=_DellNetCardVendorId_Object((1,3,6,1,4,1,6027,3,26,1,2,4,1,7),_DellNetCardVendorId_Type())
dellNetCardVendorId.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetCardVendorId.setStatus(_B)
_DellNetCardMfgDate_Type=DellNetMfgDate
_DellNetCardMfgDate_Object=MibTableColumn
dellNetCardMfgDate=_DellNetCardMfgDate_Object((1,3,6,1,4,1,6027,3,26,1,2,4,1,8),_DellNetCardMfgDate_Type())
dellNetCardMfgDate.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetCardMfgDate.setStatus(_B)
_DellNetCardPartNum_Type=DisplayString
_DellNetCardPartNum_Object=MibTableColumn
dellNetCardPartNum=_DellNetCardPartNum_Object((1,3,6,1,4,1,6027,3,26,1,2,4,1,9),_DellNetCardPartNum_Type())
dellNetCardPartNum.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetCardPartNum.setStatus(_B)
_DellNetCardProductRev_Type=DisplayString
_DellNetCardProductRev_Object=MibTableColumn
dellNetCardProductRev=_DellNetCardProductRev_Object((1,3,6,1,4,1,6027,3,26,1,2,4,1,10),_DellNetCardProductRev_Type())
dellNetCardProductRev.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetCardProductRev.setStatus(_B)
_DellNetCardProductOrder_Type=DisplayString
_DellNetCardProductOrder_Object=MibTableColumn
dellNetCardProductOrder=_DellNetCardProductOrder_Object((1,3,6,1,4,1,6027,3,26,1,2,4,1,11),_DellNetCardProductOrder_Type())
dellNetCardProductOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetCardProductOrder.setStatus(_B)
class _DellNetCardCountryCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_DellNetCardCountryCode_Type.__name__=_S
_DellNetCardCountryCode_Object=MibTableColumn
dellNetCardCountryCode=_DellNetCardCountryCode_Object((1,3,6,1,4,1,6027,3,26,1,2,4,1,12),_DellNetCardCountryCode_Type())
dellNetCardCountryCode.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetCardCountryCode.setStatus(_B)
class _DellNetCardPiecePartID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_DellNetCardPiecePartID_Type.__name__=_I
_DellNetCardPiecePartID_Object=MibTableColumn
dellNetCardPiecePartID=_DellNetCardPiecePartID_Object((1,3,6,1,4,1,6027,3,26,1,2,4,1,13),_DellNetCardPiecePartID_Type())
dellNetCardPiecePartID.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetCardPiecePartID.setStatus(_B)
class _DellNetCardPPIDRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_DellNetCardPPIDRevision_Type.__name__=_I
_DellNetCardPPIDRevision_Object=MibTableColumn
dellNetCardPPIDRevision=_DellNetCardPPIDRevision_Object((1,3,6,1,4,1,6027,3,26,1,2,4,1,14),_DellNetCardPPIDRevision_Type())
dellNetCardPPIDRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetCardPPIDRevision.setStatus(_B)
class _DellNetCardServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_DellNetCardServiceTag_Type.__name__=_I
_DellNetCardServiceTag_Object=MibTableColumn
dellNetCardServiceTag=_DellNetCardServiceTag_Object((1,3,6,1,4,1,6027,3,26,1,2,4,1,15),_DellNetCardServiceTag_Type())
dellNetCardServiceTag.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetCardServiceTag.setStatus(_B)
class _DellNetCardExpServiceCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_DellNetCardExpServiceCode_Type.__name__=_I
_DellNetCardExpServiceCode_Object=MibTableColumn
dellNetCardExpServiceCode=_DellNetCardExpServiceCode_Object((1,3,6,1,4,1,6027,3,26,1,2,4,1,16),_DellNetCardExpServiceCode_Type())
dellNetCardExpServiceCode.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetCardExpServiceCode.setStatus(_B)
_DellNetCardNumOfPorts_Type=Integer32
_DellNetCardNumOfPorts_Object=MibTableColumn
dellNetCardNumOfPorts=_DellNetCardNumOfPorts_Object((1,3,6,1,4,1,6027,3,26,1,2,4,1,17),_DellNetCardNumOfPorts_Type())
dellNetCardNumOfPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetCardNumOfPorts.setStatus(_B)
_DellNetStackObject_ObjectIdentity=ObjectIdentity
dellNetStackObject=_DellNetStackObject_ObjectIdentity((1,3,6,1,4,1,6027,3,26,1,3))
_DellNetNumStackUnits_Type=Integer32
_DellNetNumStackUnits_Object=MibScalar
dellNetNumStackUnits=_DellNetNumStackUnits_Object((1,3,6,1,4,1,6027,3,26,1,3,1),_DellNetNumStackUnits_Type())
dellNetNumStackUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetNumStackUnits.setStatus(_B)
_DellNetMaxStackableUnits_Type=Integer32
_DellNetMaxStackableUnits_Object=MibScalar
dellNetMaxStackableUnits=_DellNetMaxStackableUnits_Object((1,3,6,1,4,1,6027,3,26,1,3,2),_DellNetMaxStackableUnits_Type())
dellNetMaxStackableUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetMaxStackableUnits.setStatus(_B)
class _DellNetStackUnitIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,16))
_DellNetStackUnitIndexNext_Type.__name__=_K
_DellNetStackUnitIndexNext_Object=MibScalar
dellNetStackUnitIndexNext=_DellNetStackUnitIndexNext_Object((1,3,6,1,4,1,6027,3,26,1,3,3),_DellNetStackUnitIndexNext_Type())
dellNetStackUnitIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitIndexNext.setStatus(_B)
_DellNetStackUnitTable_Object=MibTable
dellNetStackUnitTable=_DellNetStackUnitTable_Object((1,3,6,1,4,1,6027,3,26,1,3,4))
if mibBuilder.loadTexts:dellNetStackUnitTable.setStatus(_B)
_DellNetStackUnitEntry_Object=MibTableRow
dellNetStackUnitEntry=_DellNetStackUnitEntry_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1))
dellNetStackUnitEntry.setIndexNames((0,_A,_T))
if mibBuilder.loadTexts:dellNetStackUnitEntry.setStatus(_B)
class _DellNetStackUnitNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,12))
_DellNetStackUnitNumber_Type.__name__=_K
_DellNetStackUnitNumber_Object=MibTableColumn
dellNetStackUnitNumber=_DellNetStackUnitNumber_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,1),_DellNetStackUnitNumber_Type())
dellNetStackUnitNumber.setMaxAccess(_L)
if mibBuilder.loadTexts:dellNetStackUnitNumber.setStatus(_B)
_DellNetStackUnitIndex_Type=Integer32
_DellNetStackUnitIndex_Object=MibTableColumn
dellNetStackUnitIndex=_DellNetStackUnitIndex_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,2),_DellNetStackUnitIndex_Type())
dellNetStackUnitIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitIndex.setStatus(_B)
class _DellNetStackUnitMgmtStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('mgmtUnit',1),('standbyUnit',2),('stackUnit',3),('unassigned',4)))
_DellNetStackUnitMgmtStatus_Type.__name__=_K
_DellNetStackUnitMgmtStatus_Object=MibTableColumn
dellNetStackUnitMgmtStatus=_DellNetStackUnitMgmtStatus_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,4),_DellNetStackUnitMgmtStatus_Type())
dellNetStackUnitMgmtStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitMgmtStatus.setStatus(_B)
class _DellNetStackUnitHwMgmtPreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disabled',0),('unsassigned',1),('assigned',2)))
_DellNetStackUnitHwMgmtPreference_Type.__name__=_K
_DellNetStackUnitHwMgmtPreference_Object=MibTableColumn
dellNetStackUnitHwMgmtPreference=_DellNetStackUnitHwMgmtPreference_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,5),_DellNetStackUnitHwMgmtPreference_Type())
dellNetStackUnitHwMgmtPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitHwMgmtPreference.setStatus(_B)
class _DellNetStackUnitAdmMgmtPreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,15))
_DellNetStackUnitAdmMgmtPreference_Type.__name__=_K
_DellNetStackUnitAdmMgmtPreference_Object=MibTableColumn
dellNetStackUnitAdmMgmtPreference=_DellNetStackUnitAdmMgmtPreference_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,6),_DellNetStackUnitAdmMgmtPreference_Type())
dellNetStackUnitAdmMgmtPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitAdmMgmtPreference.setStatus(_B)
_DellNetStackUnitModelId_Type=DellNetChassisType
_DellNetStackUnitModelId_Object=MibTableColumn
dellNetStackUnitModelId=_DellNetStackUnitModelId_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,7),_DellNetStackUnitModelId_Type())
dellNetStackUnitModelId.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitModelId.setStatus(_B)
class _DellNetStackUnitStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ok',1),('unsupported',2),('codeMismatch',3),('configMismatch',4),('unitDown',5),(_g,6)))
_DellNetStackUnitStatus_Type.__name__=_K
_DellNetStackUnitStatus_Object=MibTableColumn
dellNetStackUnitStatus=_DellNetStackUnitStatus_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,8),_DellNetStackUnitStatus_Type())
dellNetStackUnitStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitStatus.setStatus(_B)
_DellNetStackUnitDescription_Type=DisplayString
_DellNetStackUnitDescription_Object=MibTableColumn
dellNetStackUnitDescription=_DellNetStackUnitDescription_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,9),_DellNetStackUnitDescription_Type())
dellNetStackUnitDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitDescription.setStatus(_B)
_DellNetStackUnitCodeVersion_Type=DisplayString
_DellNetStackUnitCodeVersion_Object=MibTableColumn
dellNetStackUnitCodeVersion=_DellNetStackUnitCodeVersion_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,10),_DellNetStackUnitCodeVersion_Type())
dellNetStackUnitCodeVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitCodeVersion.setStatus(_B)
_DellNetStackUnitSerialNumber_Type=DisplayString
_DellNetStackUnitSerialNumber_Object=MibTableColumn
dellNetStackUnitSerialNumber=_DellNetStackUnitSerialNumber_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,11),_DellNetStackUnitSerialNumber_Type())
dellNetStackUnitSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitSerialNumber.setStatus(_B)
_DellNetStackUnitUpTime_Type=TimeTicks
_DellNetStackUnitUpTime_Object=MibTableColumn
dellNetStackUnitUpTime=_DellNetStackUnitUpTime_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,12),_DellNetStackUnitUpTime_Type())
dellNetStackUnitUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitUpTime.setStatus(_B)
_DellNetStackUnitTemp_Type=Gauge32
_DellNetStackUnitTemp_Object=MibTableColumn
dellNetStackUnitTemp=_DellNetStackUnitTemp_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,13),_DellNetStackUnitTemp_Type())
dellNetStackUnitTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitTemp.setStatus(_B)
_DellNetStackUnitVendorId_Type=DisplayString
_DellNetStackUnitVendorId_Object=MibTableColumn
dellNetStackUnitVendorId=_DellNetStackUnitVendorId_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,14),_DellNetStackUnitVendorId_Type())
dellNetStackUnitVendorId.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitVendorId.setStatus(_B)
_DellNetStackUnitMfgDate_Type=DellNetMfgDate
_DellNetStackUnitMfgDate_Object=MibTableColumn
dellNetStackUnitMfgDate=_DellNetStackUnitMfgDate_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,15),_DellNetStackUnitMfgDate_Type())
dellNetStackUnitMfgDate.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitMfgDate.setStatus(_B)
_DellNetStackUnitMacAddress_Type=MacAddress
_DellNetStackUnitMacAddress_Object=MibTableColumn
dellNetStackUnitMacAddress=_DellNetStackUnitMacAddress_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,16),_DellNetStackUnitMacAddress_Type())
dellNetStackUnitMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitMacAddress.setStatus(_B)
_DellNetStackUnitPartNum_Type=DisplayString
_DellNetStackUnitPartNum_Object=MibTableColumn
dellNetStackUnitPartNum=_DellNetStackUnitPartNum_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,17),_DellNetStackUnitPartNum_Type())
dellNetStackUnitPartNum.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitPartNum.setStatus(_B)
_DellNetStackUnitProductRev_Type=DisplayString
_DellNetStackUnitProductRev_Object=MibTableColumn
dellNetStackUnitProductRev=_DellNetStackUnitProductRev_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,18),_DellNetStackUnitProductRev_Type())
dellNetStackUnitProductRev.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitProductRev.setStatus(_B)
_DellNetStackUnitProductOrder_Type=DisplayString
_DellNetStackUnitProductOrder_Object=MibTableColumn
dellNetStackUnitProductOrder=_DellNetStackUnitProductOrder_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,19),_DellNetStackUnitProductOrder_Type())
dellNetStackUnitProductOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitProductOrder.setStatus(_B)
class _DellNetStackUnitCountryCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_DellNetStackUnitCountryCode_Type.__name__=_S
_DellNetStackUnitCountryCode_Object=MibTableColumn
dellNetStackUnitCountryCode=_DellNetStackUnitCountryCode_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,20),_DellNetStackUnitCountryCode_Type())
dellNetStackUnitCountryCode.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitCountryCode.setStatus(_B)
class _DellNetStackUnitPiecePartID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_DellNetStackUnitPiecePartID_Type.__name__=_I
_DellNetStackUnitPiecePartID_Object=MibTableColumn
dellNetStackUnitPiecePartID=_DellNetStackUnitPiecePartID_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,21),_DellNetStackUnitPiecePartID_Type())
dellNetStackUnitPiecePartID.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitPiecePartID.setStatus(_B)
class _DellNetStackUnitPPIDRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_DellNetStackUnitPPIDRevision_Type.__name__=_I
_DellNetStackUnitPPIDRevision_Object=MibTableColumn
dellNetStackUnitPPIDRevision=_DellNetStackUnitPPIDRevision_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,22),_DellNetStackUnitPPIDRevision_Type())
dellNetStackUnitPPIDRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitPPIDRevision.setStatus(_B)
class _DellNetStackUnitServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_DellNetStackUnitServiceTag_Type.__name__=_I
_DellNetStackUnitServiceTag_Object=MibTableColumn
dellNetStackUnitServiceTag=_DellNetStackUnitServiceTag_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,23),_DellNetStackUnitServiceTag_Type())
dellNetStackUnitServiceTag.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitServiceTag.setStatus(_B)
class _DellNetStackUnitExpServiceCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_DellNetStackUnitExpServiceCode_Type.__name__=_I
_DellNetStackUnitExpServiceCode_Object=MibTableColumn
dellNetStackUnitExpServiceCode=_DellNetStackUnitExpServiceCode_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,24),_DellNetStackUnitExpServiceCode_Type())
dellNetStackUnitExpServiceCode.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitExpServiceCode.setStatus(_B)
_DellNetStackUnitNumOfPorts_Type=Integer32
_DellNetStackUnitNumOfPorts_Object=MibTableColumn
dellNetStackUnitNumOfPorts=_DellNetStackUnitNumOfPorts_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,25),_DellNetStackUnitNumOfPorts_Type())
dellNetStackUnitNumOfPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitNumOfPorts.setStatus(_B)
_DellNetStackUnitNumFanTrays_Type=Integer32
_DellNetStackUnitNumFanTrays_Object=MibTableColumn
dellNetStackUnitNumFanTrays=_DellNetStackUnitNumFanTrays_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,26),_DellNetStackUnitNumFanTrays_Type())
dellNetStackUnitNumFanTrays.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitNumFanTrays.setStatus(_B)
_DellNetStackUnitNumPowerSupplies_Type=Integer32
_DellNetStackUnitNumPowerSupplies_Object=MibTableColumn
dellNetStackUnitNumPowerSupplies=_DellNetStackUnitNumPowerSupplies_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,27),_DellNetStackUnitNumPowerSupplies_Type())
dellNetStackUnitNumPowerSupplies.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitNumPowerSupplies.setStatus(_B)
_DellNetStackUnitNumPluggableModules_Type=Integer32
_DellNetStackUnitNumPluggableModules_Object=MibTableColumn
dellNetStackUnitNumPluggableModules=_DellNetStackUnitNumPluggableModules_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,28),_DellNetStackUnitNumPluggableModules_Type())
dellNetStackUnitNumPluggableModules.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitNumPluggableModules.setStatus(_B)
class _DellNetStackUnitIOMMode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_DellNetStackUnitIOMMode_Type.__name__=_I
_DellNetStackUnitIOMMode_Object=MibTableColumn
dellNetStackUnitIOMMode=_DellNetStackUnitIOMMode_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,29),_DellNetStackUnitIOMMode_Type())
dellNetStackUnitIOMMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitIOMMode.setStatus(_B)
_DellNetStackUnitBladeSlotId_Type=Integer32
_DellNetStackUnitBladeSlotId_Object=MibTableColumn
dellNetStackUnitBladeSlotId=_DellNetStackUnitBladeSlotId_Object((1,3,6,1,4,1,6027,3,26,1,3,4,1,30),_DellNetStackUnitBladeSlotId_Type())
dellNetStackUnitBladeSlotId.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackUnitBladeSlotId.setStatus(_B)
_DellNetStackPortTable_Object=MibTable
dellNetStackPortTable=_DellNetStackPortTable_Object((1,3,6,1,4,1,6027,3,26,1,3,5))
if mibBuilder.loadTexts:dellNetStackPortTable.setStatus(_B)
_DellNetStackPortEntry_Object=MibTableRow
dellNetStackPortEntry=_DellNetStackPortEntry_Object((1,3,6,1,4,1,6027,3,26,1,3,5,1))
dellNetStackPortEntry.setIndexNames((0,_A,_T),(0,_A,_h))
if mibBuilder.loadTexts:dellNetStackPortEntry.setStatus(_B)
_DellNetStackPortIndex_Type=Integer32
_DellNetStackPortIndex_Object=MibTableColumn
dellNetStackPortIndex=_DellNetStackPortIndex_Object((1,3,6,1,4,1,6027,3,26,1,3,5,1,1),_DellNetStackPortIndex_Type())
dellNetStackPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackPortIndex.setStatus(_B)
class _DellNetStackPortConfiguredMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stack',1),(_i,2),(_Z,3)))
_DellNetStackPortConfiguredMode_Type.__name__=_K
_DellNetStackPortConfiguredMode_Object=MibTableColumn
dellNetStackPortConfiguredMode=_DellNetStackPortConfiguredMode_Object((1,3,6,1,4,1,6027,3,26,1,3,5,1,2),_DellNetStackPortConfiguredMode_Type())
dellNetStackPortConfiguredMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackPortConfiguredMode.setStatus(_B)
class _DellNetStackPortRunningMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stack',1),(_i,2),(_Z,3)))
_DellNetStackPortRunningMode_Type.__name__=_K
_DellNetStackPortRunningMode_Object=MibTableColumn
dellNetStackPortRunningMode=_DellNetStackPortRunningMode_Object((1,3,6,1,4,1,6027,3,26,1,3,5,1,3),_DellNetStackPortRunningMode_Type())
dellNetStackPortRunningMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackPortRunningMode.setStatus(_B)
class _DellNetStackPortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_DellNetStackPortLinkStatus_Type.__name__=_K
_DellNetStackPortLinkStatus_Object=MibTableColumn
dellNetStackPortLinkStatus=_DellNetStackPortLinkStatus_Object((1,3,6,1,4,1,6027,3,26,1,3,5,1,4),_DellNetStackPortLinkStatus_Type())
dellNetStackPortLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackPortLinkStatus.setStatus(_B)
_DellNetStackPortLinkSpeed_Type=Gauge32
_DellNetStackPortLinkSpeed_Object=MibTableColumn
dellNetStackPortLinkSpeed=_DellNetStackPortLinkSpeed_Object((1,3,6,1,4,1,6027,3,26,1,3,5,1,5),_DellNetStackPortLinkSpeed_Type())
dellNetStackPortLinkSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackPortLinkSpeed.setStatus(_B)
_DellNetStackPortRxDataRate_Type=Counter32
_DellNetStackPortRxDataRate_Object=MibTableColumn
dellNetStackPortRxDataRate=_DellNetStackPortRxDataRate_Object((1,3,6,1,4,1,6027,3,26,1,3,5,1,6),_DellNetStackPortRxDataRate_Type())
dellNetStackPortRxDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackPortRxDataRate.setStatus(_B)
_DellNetStackPortRxErrorRate_Type=Counter32
_DellNetStackPortRxErrorRate_Object=MibTableColumn
dellNetStackPortRxErrorRate=_DellNetStackPortRxErrorRate_Object((1,3,6,1,4,1,6027,3,26,1,3,5,1,7),_DellNetStackPortRxErrorRate_Type())
dellNetStackPortRxErrorRate.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackPortRxErrorRate.setStatus(_B)
_DellNetStackPortRxTotalErrors_Type=Counter32
_DellNetStackPortRxTotalErrors_Object=MibTableColumn
dellNetStackPortRxTotalErrors=_DellNetStackPortRxTotalErrors_Object((1,3,6,1,4,1,6027,3,26,1,3,5,1,8),_DellNetStackPortRxTotalErrors_Type())
dellNetStackPortRxTotalErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackPortRxTotalErrors.setStatus(_B)
_DellNetStackPortTxDataRate_Type=Counter32
_DellNetStackPortTxDataRate_Object=MibTableColumn
dellNetStackPortTxDataRate=_DellNetStackPortTxDataRate_Object((1,3,6,1,4,1,6027,3,26,1,3,5,1,9),_DellNetStackPortTxDataRate_Type())
dellNetStackPortTxDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackPortTxDataRate.setStatus(_B)
_DellNetStackPortTxErrorRate_Type=Counter32
_DellNetStackPortTxErrorRate_Object=MibTableColumn
dellNetStackPortTxErrorRate=_DellNetStackPortTxErrorRate_Object((1,3,6,1,4,1,6027,3,26,1,3,5,1,10),_DellNetStackPortTxErrorRate_Type())
dellNetStackPortTxErrorRate.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackPortTxErrorRate.setStatus(_B)
_DellNetStackPortTxTotalErrors_Type=Counter32
_DellNetStackPortTxTotalErrors_Object=MibTableColumn
dellNetStackPortTxTotalErrors=_DellNetStackPortTxTotalErrors_Object((1,3,6,1,4,1,6027,3,26,1,3,5,1,11),_DellNetStackPortTxTotalErrors_Type())
dellNetStackPortTxTotalErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetStackPortTxTotalErrors.setStatus(_B)
_DellNetWebUIURL_Type=DisplayString
_DellNetWebUIURL_Object=MibScalar
dellNetWebUIURL=_DellNetWebUIURL_Object((1,3,6,1,4,1,6027,3,26,1,3,6),_DellNetWebUIURL_Type())
dellNetWebUIURL.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetWebUIURL.setStatus(_B)
_DellNetSystemComponent_ObjectIdentity=ObjectIdentity
dellNetSystemComponent=_DellNetSystemComponent_ObjectIdentity((1,3,6,1,4,1,6027,3,26,1,4))
_DellNetPEBindingTable_Object=MibTable
dellNetPEBindingTable=_DellNetPEBindingTable_Object((1,3,6,1,4,1,6027,3,26,1,4,1))
if mibBuilder.loadTexts:dellNetPEBindingTable.setStatus(_B)
_DellNetPEBindingEntry_Object=MibTableRow
dellNetPEBindingEntry=_DellNetPEBindingEntry_Object((1,3,6,1,4,1,6027,3,26,1,4,1,1))
dellNetPEBindingEntry.setIndexNames((0,_A,_j))
if mibBuilder.loadTexts:dellNetPEBindingEntry.setStatus(_B)
_DellNetPEBindCascadePortIfIndex_Type=InterfaceIndex
_DellNetPEBindCascadePortIfIndex_Object=MibTableColumn
dellNetPEBindCascadePortIfIndex=_DellNetPEBindCascadePortIfIndex_Object((1,3,6,1,4,1,6027,3,26,1,4,1,1,1),_DellNetPEBindCascadePortIfIndex_Type())
dellNetPEBindCascadePortIfIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:dellNetPEBindCascadePortIfIndex.setStatus(_B)
_DellNetPEBindPEIndex_Type=Integer32
_DellNetPEBindPEIndex_Object=MibTableColumn
dellNetPEBindPEIndex=_DellNetPEBindPEIndex_Object((1,3,6,1,4,1,6027,3,26,1,4,1,1,2),_DellNetPEBindPEIndex_Type())
dellNetPEBindPEIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPEBindPEIndex.setStatus(_B)
_DellNetPETable_Object=MibTable
dellNetPETable=_DellNetPETable_Object((1,3,6,1,4,1,6027,3,26,1,4,2))
if mibBuilder.loadTexts:dellNetPETable.setStatus(_B)
_DellNetPEEntry_Object=MibTableRow
dellNetPEEntry=_DellNetPEEntry_Object((1,3,6,1,4,1,6027,3,26,1,4,2,1))
dellNetPEEntry.setIndexNames((0,_A,_k))
if mibBuilder.loadTexts:dellNetPEEntry.setStatus(_B)
_DellNetPEIndex_Type=Integer32
_DellNetPEIndex_Object=MibTableColumn
dellNetPEIndex=_DellNetPEIndex_Object((1,3,6,1,4,1,6027,3,26,1,4,2,1,1),_DellNetPEIndex_Type())
dellNetPEIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:dellNetPEIndex.setStatus(_B)
class _DellNetPEPEID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_DellNetPEPEID_Type.__name__=_K
_DellNetPEPEID_Object=MibTableColumn
dellNetPEPEID=_DellNetPEPEID_Object((1,3,6,1,4,1,6027,3,26,1,4,2,1,2),_DellNetPEPEID_Type())
dellNetPEPEID.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPEPEID.setStatus(_B)
class _DellNetPEUnitID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_DellNetPEUnitID_Type.__name__=_K
_DellNetPEUnitID_Object=MibTableColumn
dellNetPEUnitID=_DellNetPEUnitID_Object((1,3,6,1,4,1,6027,3,26,1,4,2,1,3),_DellNetPEUnitID_Type())
dellNetPEUnitID.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPEUnitID.setStatus(_B)
_DellNetPEType_Type=DellNetChassisType
_DellNetPEType_Object=MibTableColumn
dellNetPEType=_DellNetPEType_Object((1,3,6,1,4,1,6027,3,26,1,4,2,1,4),_DellNetPEType_Type())
dellNetPEType.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPEType.setStatus(_B)
class _DellNetPEDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_DellNetPEDescription_Type.__name__=_I
_DellNetPEDescription_Object=MibTableColumn
dellNetPEDescription=_DellNetPEDescription_Object((1,3,6,1,4,1,6027,3,26,1,4,2,1,5),_DellNetPEDescription_Type())
dellNetPEDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPEDescription.setStatus(_B)
_DellNetPEStatus_Type=DellNetPEOperStatus
_DellNetPEStatus_Object=MibTableColumn
dellNetPEStatus=_DellNetPEStatus_Object((1,3,6,1,4,1,6027,3,26,1,4,2,1,6),_DellNetPEStatus_Type())
dellNetPEStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPEStatus.setStatus(_B)
_DellNetPETemp_Type=Integer32
_DellNetPETemp_Object=MibTableColumn
dellNetPETemp=_DellNetPETemp_Object((1,3,6,1,4,1,6027,3,26,1,4,2,1,7),_DellNetPETemp_Type())
dellNetPETemp.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPETemp.setStatus(_B)
if mibBuilder.loadTexts:dellNetPETemp.setUnits(_f)
_DellNetPEVendorId_Type=DisplayString
_DellNetPEVendorId_Object=MibTableColumn
dellNetPEVendorId=_DellNetPEVendorId_Object((1,3,6,1,4,1,6027,3,26,1,4,2,1,8),_DellNetPEVendorId_Type())
dellNetPEVendorId.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPEVendorId.setStatus(_B)
_DellNetPEMfgDate_Type=DellNetMfgDate
_DellNetPEMfgDate_Object=MibTableColumn
dellNetPEMfgDate=_DellNetPEMfgDate_Object((1,3,6,1,4,1,6027,3,26,1,4,2,1,9),_DellNetPEMfgDate_Type())
dellNetPEMfgDate.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPEMfgDate.setStatus(_B)
_DellNetPEPartNum_Type=DisplayString
_DellNetPEPartNum_Object=MibTableColumn
dellNetPEPartNum=_DellNetPEPartNum_Object((1,3,6,1,4,1,6027,3,26,1,4,2,1,10),_DellNetPEPartNum_Type())
dellNetPEPartNum.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPEPartNum.setStatus(_B)
_DellNetPEProductRev_Type=DisplayString
_DellNetPEProductRev_Object=MibTableColumn
dellNetPEProductRev=_DellNetPEProductRev_Object((1,3,6,1,4,1,6027,3,26,1,4,2,1,11),_DellNetPEProductRev_Type())
dellNetPEProductRev.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPEProductRev.setStatus(_B)
_DellNetPEProductOrder_Type=DisplayString
_DellNetPEProductOrder_Object=MibTableColumn
dellNetPEProductOrder=_DellNetPEProductOrder_Object((1,3,6,1,4,1,6027,3,26,1,4,2,1,12),_DellNetPEProductOrder_Type())
dellNetPEProductOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPEProductOrder.setStatus(_B)
class _DellNetPECountryCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_DellNetPECountryCode_Type.__name__=_S
_DellNetPECountryCode_Object=MibTableColumn
dellNetPECountryCode=_DellNetPECountryCode_Object((1,3,6,1,4,1,6027,3,26,1,4,2,1,13),_DellNetPECountryCode_Type())
dellNetPECountryCode.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPECountryCode.setStatus(_B)
class _DellNetPEPiecePartID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_DellNetPEPiecePartID_Type.__name__=_I
_DellNetPEPiecePartID_Object=MibTableColumn
dellNetPEPiecePartID=_DellNetPEPiecePartID_Object((1,3,6,1,4,1,6027,3,26,1,4,2,1,14),_DellNetPEPiecePartID_Type())
dellNetPEPiecePartID.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPEPiecePartID.setStatus(_B)
class _DellNetPEPPIDRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_DellNetPEPPIDRevision_Type.__name__=_I
_DellNetPEPPIDRevision_Object=MibTableColumn
dellNetPEPPIDRevision=_DellNetPEPPIDRevision_Object((1,3,6,1,4,1,6027,3,26,1,4,2,1,15),_DellNetPEPPIDRevision_Type())
dellNetPEPPIDRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPEPPIDRevision.setStatus(_B)
class _DellNetPEServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_DellNetPEServiceTag_Type.__name__=_I
_DellNetPEServiceTag_Object=MibTableColumn
dellNetPEServiceTag=_DellNetPEServiceTag_Object((1,3,6,1,4,1,6027,3,26,1,4,2,1,16),_DellNetPEServiceTag_Type())
dellNetPEServiceTag.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPEServiceTag.setStatus(_B)
class _DellNetPEExpServiceCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_DellNetPEExpServiceCode_Type.__name__=_I
_DellNetPEExpServiceCode_Object=MibTableColumn
dellNetPEExpServiceCode=_DellNetPEExpServiceCode_Object((1,3,6,1,4,1,6027,3,26,1,4,2,1,17),_DellNetPEExpServiceCode_Type())
dellNetPEExpServiceCode.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPEExpServiceCode.setStatus(_B)
_DellNetPENumOfPorts_Type=Integer32
_DellNetPENumOfPorts_Object=MibTableColumn
dellNetPENumOfPorts=_DellNetPENumOfPorts_Object((1,3,6,1,4,1,6027,3,26,1,4,2,1,18),_DellNetPENumOfPorts_Type())
dellNetPENumOfPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPENumOfPorts.setStatus(_B)
_DellNetPENumFanTrays_Type=Integer32
_DellNetPENumFanTrays_Object=MibTableColumn
dellNetPENumFanTrays=_DellNetPENumFanTrays_Object((1,3,6,1,4,1,6027,3,26,1,4,2,1,19),_DellNetPENumFanTrays_Type())
dellNetPENumFanTrays.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPENumFanTrays.setStatus(_B)
_DellNetPENumPowerSupplies_Type=Integer32
_DellNetPENumPowerSupplies_Object=MibTableColumn
dellNetPENumPowerSupplies=_DellNetPENumPowerSupplies_Object((1,3,6,1,4,1,6027,3,26,1,4,2,1,20),_DellNetPENumPowerSupplies_Type())
dellNetPENumPowerSupplies.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPENumPowerSupplies.setStatus(_B)
_DellNetPENumPluggableModules_Type=Integer32
_DellNetPENumPluggableModules_Object=MibTableColumn
dellNetPENumPluggableModules=_DellNetPENumPluggableModules_Object((1,3,6,1,4,1,6027,3,26,1,4,2,1,21),_DellNetPENumPluggableModules_Type())
dellNetPENumPluggableModules.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPENumPluggableModules.setStatus(_B)
_DellNetProcessorTable_Object=MibTable
dellNetProcessorTable=_DellNetProcessorTable_Object((1,3,6,1,4,1,6027,3,26,1,4,3))
if mibBuilder.loadTexts:dellNetProcessorTable.setStatus(_B)
_DellNetProcessorEntry_Object=MibTableRow
dellNetProcessorEntry=_DellNetProcessorEntry_Object((1,3,6,1,4,1,6027,3,26,1,4,3,1))
dellNetProcessorEntry.setIndexNames((0,_A,_W),(0,_A,_X),(0,_A,_a))
if mibBuilder.loadTexts:dellNetProcessorEntry.setStatus(_B)
_DellNetProcessorDeviceType_Type=DellNetDeviceType
_DellNetProcessorDeviceType_Object=MibTableColumn
dellNetProcessorDeviceType=_DellNetProcessorDeviceType_Object((1,3,6,1,4,1,6027,3,26,1,4,3,1,1),_DellNetProcessorDeviceType_Type())
dellNetProcessorDeviceType.setMaxAccess(_L)
if mibBuilder.loadTexts:dellNetProcessorDeviceType.setStatus(_B)
_DellNetProcessorDeviceIndex_Type=Integer32
_DellNetProcessorDeviceIndex_Object=MibTableColumn
dellNetProcessorDeviceIndex=_DellNetProcessorDeviceIndex_Object((1,3,6,1,4,1,6027,3,26,1,4,3,1,2),_DellNetProcessorDeviceIndex_Type())
dellNetProcessorDeviceIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:dellNetProcessorDeviceIndex.setStatus(_B)
_DellNetProcessorIndex_Type=Integer32
_DellNetProcessorIndex_Object=MibTableColumn
dellNetProcessorIndex=_DellNetProcessorIndex_Object((1,3,6,1,4,1,6027,3,26,1,4,3,1,3),_DellNetProcessorIndex_Type())
dellNetProcessorIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:dellNetProcessorIndex.setStatus(_B)
_DellNetProcessorModule_Type=DellNetProcessorModuleType
_DellNetProcessorModule_Object=MibTableColumn
dellNetProcessorModule=_DellNetProcessorModule_Object((1,3,6,1,4,1,6027,3,26,1,4,3,1,4),_DellNetProcessorModule_Type())
dellNetProcessorModule.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetProcessorModule.setStatus(_B)
_DellNetProcessorUpTime_Type=TimeTicks
_DellNetProcessorUpTime_Object=MibTableColumn
dellNetProcessorUpTime=_DellNetProcessorUpTime_Object((1,3,6,1,4,1,6027,3,26,1,4,3,1,5),_DellNetProcessorUpTime_Type())
dellNetProcessorUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetProcessorUpTime.setStatus(_B)
_DellNetProcessorMemSize_Type=Integer32
_DellNetProcessorMemSize_Object=MibTableColumn
dellNetProcessorMemSize=_DellNetProcessorMemSize_Object((1,3,6,1,4,1,6027,3,26,1,4,3,1,6),_DellNetProcessorMemSize_Type())
dellNetProcessorMemSize.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetProcessorMemSize.setStatus(_B)
_DellNetProcessorResetReason_Type=DisplayString
_DellNetProcessorResetReason_Object=MibTableColumn
dellNetProcessorResetReason=_DellNetProcessorResetReason_Object((1,3,6,1,4,1,6027,3,26,1,4,3,1,7),_DellNetProcessorResetReason_Type())
dellNetProcessorResetReason.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetProcessorResetReason.setStatus(_B)
_DellNetProcessorResetTime_Type=DateAndTime
_DellNetProcessorResetTime_Object=MibTableColumn
dellNetProcessorResetTime=_DellNetProcessorResetTime_Object((1,3,6,1,4,1,6027,3,26,1,4,3,1,8),_DellNetProcessorResetTime_Type())
dellNetProcessorResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetProcessorResetTime.setStatus(_B)
_DellNetCpuUtilTable_Object=MibTable
dellNetCpuUtilTable=_DellNetCpuUtilTable_Object((1,3,6,1,4,1,6027,3,26,1,4,4))
if mibBuilder.loadTexts:dellNetCpuUtilTable.setStatus(_B)
_DellNetCpuUtilEntry_Object=MibTableRow
dellNetCpuUtilEntry=_DellNetCpuUtilEntry_Object((1,3,6,1,4,1,6027,3,26,1,4,4,1))
dellNetCpuUtilEntry.setIndexNames((0,_A,_W),(0,_A,_X),(0,_A,_a))
if mibBuilder.loadTexts:dellNetCpuUtilEntry.setStatus(_B)
class _DellNetCpuUtil5Sec_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DellNetCpuUtil5Sec_Type.__name__=_Q
_DellNetCpuUtil5Sec_Object=MibTableColumn
dellNetCpuUtil5Sec=_DellNetCpuUtil5Sec_Object((1,3,6,1,4,1,6027,3,26,1,4,4,1,1),_DellNetCpuUtil5Sec_Type())
dellNetCpuUtil5Sec.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetCpuUtil5Sec.setStatus(_B)
if mibBuilder.loadTexts:dellNetCpuUtil5Sec.setUnits(_R)
class _DellNetCpuUtil1Min_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DellNetCpuUtil1Min_Type.__name__=_Q
_DellNetCpuUtil1Min_Object=MibTableColumn
dellNetCpuUtil1Min=_DellNetCpuUtil1Min_Object((1,3,6,1,4,1,6027,3,26,1,4,4,1,4),_DellNetCpuUtil1Min_Type())
dellNetCpuUtil1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetCpuUtil1Min.setStatus(_B)
if mibBuilder.loadTexts:dellNetCpuUtil1Min.setUnits(_R)
class _DellNetCpuUtil5Min_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DellNetCpuUtil5Min_Type.__name__=_Q
_DellNetCpuUtil5Min_Object=MibTableColumn
dellNetCpuUtil5Min=_DellNetCpuUtil5Min_Object((1,3,6,1,4,1,6027,3,26,1,4,4,1,5),_DellNetCpuUtil5Min_Type())
dellNetCpuUtil5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetCpuUtil5Min.setStatus(_B)
if mibBuilder.loadTexts:dellNetCpuUtil5Min.setUnits(_R)
class _DellNetCpuUtilMemUsage_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DellNetCpuUtilMemUsage_Type.__name__=_Q
_DellNetCpuUtilMemUsage_Object=MibTableColumn
dellNetCpuUtilMemUsage=_DellNetCpuUtilMemUsage_Object((1,3,6,1,4,1,6027,3,26,1,4,4,1,6),_DellNetCpuUtilMemUsage_Type())
dellNetCpuUtilMemUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetCpuUtilMemUsage.setStatus(_B)
if mibBuilder.loadTexts:dellNetCpuUtilMemUsage.setUnits(_R)
class _DellNetCpuFlashUsage_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DellNetCpuFlashUsage_Type.__name__=_Q
_DellNetCpuFlashUsage_Object=MibTableColumn
dellNetCpuFlashUsage=_DellNetCpuFlashUsage_Object((1,3,6,1,4,1,6027,3,26,1,4,4,1,7),_DellNetCpuFlashUsage_Type())
dellNetCpuFlashUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetCpuFlashUsage.setStatus(_B)
if mibBuilder.loadTexts:dellNetCpuFlashUsage.setUnits(_R)
_DellNetSwModuleTable_Object=MibTable
dellNetSwModuleTable=_DellNetSwModuleTable_Object((1,3,6,1,4,1,6027,3,26,1,4,5))
if mibBuilder.loadTexts:dellNetSwModuleTable.setStatus(_B)
_DellNetSwModuleEntry_Object=MibTableRow
dellNetSwModuleEntry=_DellNetSwModuleEntry_Object((1,3,6,1,4,1,6027,3,26,1,4,5,1))
dellNetSwModuleEntry.setIndexNames((0,_A,_W),(0,_A,_X))
if mibBuilder.loadTexts:dellNetSwModuleEntry.setStatus(_B)
class _DellNetSwModuleRuntimeImgVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DellNetSwModuleRuntimeImgVersion_Type.__name__=_I
_DellNetSwModuleRuntimeImgVersion_Object=MibTableColumn
dellNetSwModuleRuntimeImgVersion=_DellNetSwModuleRuntimeImgVersion_Object((1,3,6,1,4,1,6027,3,26,1,4,5,1,1),_DellNetSwModuleRuntimeImgVersion_Type())
dellNetSwModuleRuntimeImgVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetSwModuleRuntimeImgVersion.setStatus(_B)
_DellNetSwModuleRuntimeImgDate_Type=DellNetSwDate
_DellNetSwModuleRuntimeImgDate_Object=MibTableColumn
dellNetSwModuleRuntimeImgDate=_DellNetSwModuleRuntimeImgDate_Object((1,3,6,1,4,1,6027,3,26,1,4,5,1,2),_DellNetSwModuleRuntimeImgDate_Type())
dellNetSwModuleRuntimeImgDate.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetSwModuleRuntimeImgDate.setStatus(_B)
class _DellNetSwModuleBootFlashImgVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DellNetSwModuleBootFlashImgVersion_Type.__name__=_I
_DellNetSwModuleBootFlashImgVersion_Object=MibTableColumn
dellNetSwModuleBootFlashImgVersion=_DellNetSwModuleBootFlashImgVersion_Object((1,3,6,1,4,1,6027,3,26,1,4,5,1,3),_DellNetSwModuleBootFlashImgVersion_Type())
dellNetSwModuleBootFlashImgVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetSwModuleBootFlashImgVersion.setStatus(_B)
class _DellNetSwModuleBootSelectorImgVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DellNetSwModuleBootSelectorImgVersion_Type.__name__=_I
_DellNetSwModuleBootSelectorImgVersion_Object=MibTableColumn
dellNetSwModuleBootSelectorImgVersion=_DellNetSwModuleBootSelectorImgVersion_Object((1,3,6,1,4,1,6027,3,26,1,4,5,1,4),_DellNetSwModuleBootSelectorImgVersion_Type())
dellNetSwModuleBootSelectorImgVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetSwModuleBootSelectorImgVersion.setStatus(_B)
class _DellNetSwModuleNextRebootImage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3)))
_DellNetSwModuleNextRebootImage_Type.__name__=_K
_DellNetSwModuleNextRebootImage_Object=MibTableColumn
dellNetSwModuleNextRebootImage=_DellNetSwModuleNextRebootImage_Object((1,3,6,1,4,1,6027,3,26,1,4,5,1,5),_DellNetSwModuleNextRebootImage_Type())
dellNetSwModuleNextRebootImage.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetSwModuleNextRebootImage.setStatus(_B)
class _DellNetSwModuleCurrentBootImage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3)))
_DellNetSwModuleCurrentBootImage_Type.__name__=_K
_DellNetSwModuleCurrentBootImage_Object=MibTableColumn
dellNetSwModuleCurrentBootImage=_DellNetSwModuleCurrentBootImage_Object((1,3,6,1,4,1,6027,3,26,1,4,5,1,6),_DellNetSwModuleCurrentBootImage_Type())
dellNetSwModuleCurrentBootImage.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetSwModuleCurrentBootImage.setStatus(_B)
class _DellNetSwModuleInPartitionAImgVers_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DellNetSwModuleInPartitionAImgVers_Type.__name__=_I
_DellNetSwModuleInPartitionAImgVers_Object=MibTableColumn
dellNetSwModuleInPartitionAImgVers=_DellNetSwModuleInPartitionAImgVers_Object((1,3,6,1,4,1,6027,3,26,1,4,5,1,7),_DellNetSwModuleInPartitionAImgVers_Type())
dellNetSwModuleInPartitionAImgVers.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetSwModuleInPartitionAImgVers.setStatus(_B)
class _DellNetSwModuleInPartitionBImgVers_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DellNetSwModuleInPartitionBImgVers_Type.__name__=_I
_DellNetSwModuleInPartitionBImgVers_Object=MibTableColumn
dellNetSwModuleInPartitionBImgVers=_DellNetSwModuleInPartitionBImgVers_Object((1,3,6,1,4,1,6027,3,26,1,4,5,1,8),_DellNetSwModuleInPartitionBImgVers_Type())
dellNetSwModuleInPartitionBImgVers.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetSwModuleInPartitionBImgVers.setStatus(_B)
_DellNetPowerSupplyTable_Object=MibTable
dellNetPowerSupplyTable=_DellNetPowerSupplyTable_Object((1,3,6,1,4,1,6027,3,26,1,4,6))
if mibBuilder.loadTexts:dellNetPowerSupplyTable.setStatus(_B)
_DellNetPowerSupplyEntry_Object=MibTableRow
dellNetPowerSupplyEntry=_DellNetPowerSupplyEntry_Object((1,3,6,1,4,1,6027,3,26,1,4,6,1))
dellNetPowerSupplyEntry.setIndexNames((0,_A,_o),(0,_A,_p),(0,_A,_q))
if mibBuilder.loadTexts:dellNetPowerSupplyEntry.setStatus(_B)
_DellNetPowerDeviceType_Type=DellNetDeviceType
_DellNetPowerDeviceType_Object=MibTableColumn
dellNetPowerDeviceType=_DellNetPowerDeviceType_Object((1,3,6,1,4,1,6027,3,26,1,4,6,1,1),_DellNetPowerDeviceType_Type())
dellNetPowerDeviceType.setMaxAccess(_L)
if mibBuilder.loadTexts:dellNetPowerDeviceType.setStatus(_B)
_DellNetPowerDeviceIndex_Type=Integer32
_DellNetPowerDeviceIndex_Object=MibTableColumn
dellNetPowerDeviceIndex=_DellNetPowerDeviceIndex_Object((1,3,6,1,4,1,6027,3,26,1,4,6,1,2),_DellNetPowerDeviceIndex_Type())
dellNetPowerDeviceIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:dellNetPowerDeviceIndex.setStatus(_B)
_DellNetPowerSupplyIndex_Type=Integer32
_DellNetPowerSupplyIndex_Object=MibTableColumn
dellNetPowerSupplyIndex=_DellNetPowerSupplyIndex_Object((1,3,6,1,4,1,6027,3,26,1,4,6,1,3),_DellNetPowerSupplyIndex_Type())
dellNetPowerSupplyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPowerSupplyIndex.setStatus(_B)
class _DellNetPowerSupplyOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),(_V,2),(_r,3)))
_DellNetPowerSupplyOperStatus_Type.__name__=_K
_DellNetPowerSupplyOperStatus_Object=MibTableColumn
dellNetPowerSupplyOperStatus=_DellNetPowerSupplyOperStatus_Object((1,3,6,1,4,1,6027,3,26,1,4,6,1,4),_DellNetPowerSupplyOperStatus_Type())
dellNetPowerSupplyOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPowerSupplyOperStatus.setStatus(_B)
class _DellNetPowerSupplyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Z,1),('ac',2),('dc',3)))
_DellNetPowerSupplyType_Type.__name__=_K
_DellNetPowerSupplyType_Object=MibTableColumn
dellNetPowerSupplyType=_DellNetPowerSupplyType_Object((1,3,6,1,4,1,6027,3,26,1,4,6,1,5),_DellNetPowerSupplyType_Type())
dellNetPowerSupplyType.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPowerSupplyType.setStatus(_B)
class _DellNetPowerSupplyPiecePartID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_DellNetPowerSupplyPiecePartID_Type.__name__=_I
_DellNetPowerSupplyPiecePartID_Object=MibTableColumn
dellNetPowerSupplyPiecePartID=_DellNetPowerSupplyPiecePartID_Object((1,3,6,1,4,1,6027,3,26,1,4,6,1,6),_DellNetPowerSupplyPiecePartID_Type())
dellNetPowerSupplyPiecePartID.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPowerSupplyPiecePartID.setStatus(_B)
class _DellNetPowerSupplyPPIDRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_DellNetPowerSupplyPPIDRevision_Type.__name__=_I
_DellNetPowerSupplyPPIDRevision_Object=MibTableColumn
dellNetPowerSupplyPPIDRevision=_DellNetPowerSupplyPPIDRevision_Object((1,3,6,1,4,1,6027,3,26,1,4,6,1,7),_DellNetPowerSupplyPPIDRevision_Type())
dellNetPowerSupplyPPIDRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPowerSupplyPPIDRevision.setStatus(_B)
class _DellNetPowerSupplyServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_DellNetPowerSupplyServiceTag_Type.__name__=_I
_DellNetPowerSupplyServiceTag_Object=MibTableColumn
dellNetPowerSupplyServiceTag=_DellNetPowerSupplyServiceTag_Object((1,3,6,1,4,1,6027,3,26,1,4,6,1,8),_DellNetPowerSupplyServiceTag_Type())
dellNetPowerSupplyServiceTag.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPowerSupplyServiceTag.setStatus(_B)
class _DellNetPowerSupplyExpressServiceCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_DellNetPowerSupplyExpressServiceCode_Type.__name__=_I
_DellNetPowerSupplyExpressServiceCode_Object=MibTableColumn
dellNetPowerSupplyExpressServiceCode=_DellNetPowerSupplyExpressServiceCode_Object((1,3,6,1,4,1,6027,3,26,1,4,6,1,9),_DellNetPowerSupplyExpressServiceCode_Type())
dellNetPowerSupplyExpressServiceCode.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPowerSupplyExpressServiceCode.setStatus(_B)
_DellNetPowerSupplyUsage_Type=Integer32
_DellNetPowerSupplyUsage_Object=MibTableColumn
dellNetPowerSupplyUsage=_DellNetPowerSupplyUsage_Object((1,3,6,1,4,1,6027,3,26,1,4,6,1,10),_DellNetPowerSupplyUsage_Type())
dellNetPowerSupplyUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPowerSupplyUsage.setStatus(_B)
_DellNetFanTrayTable_Object=MibTable
dellNetFanTrayTable=_DellNetFanTrayTable_Object((1,3,6,1,4,1,6027,3,26,1,4,7))
if mibBuilder.loadTexts:dellNetFanTrayTable.setStatus(_B)
_DellNetFanTrayEntry_Object=MibTableRow
dellNetFanTrayEntry=_DellNetFanTrayEntry_Object((1,3,6,1,4,1,6027,3,26,1,4,7,1))
dellNetFanTrayEntry.setIndexNames((0,_A,_s),(0,_A,_t),(0,_A,_u))
if mibBuilder.loadTexts:dellNetFanTrayEntry.setStatus(_B)
_DellNetFanDeviceType_Type=DellNetDeviceType
_DellNetFanDeviceType_Object=MibTableColumn
dellNetFanDeviceType=_DellNetFanDeviceType_Object((1,3,6,1,4,1,6027,3,26,1,4,7,1,1),_DellNetFanDeviceType_Type())
dellNetFanDeviceType.setMaxAccess(_L)
if mibBuilder.loadTexts:dellNetFanDeviceType.setStatus(_B)
_DellNetFanDeviceIndex_Type=Integer32
_DellNetFanDeviceIndex_Object=MibTableColumn
dellNetFanDeviceIndex=_DellNetFanDeviceIndex_Object((1,3,6,1,4,1,6027,3,26,1,4,7,1,2),_DellNetFanDeviceIndex_Type())
dellNetFanDeviceIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:dellNetFanDeviceIndex.setStatus(_B)
_DellNetFanTrayIndex_Type=Integer32
_DellNetFanTrayIndex_Object=MibTableColumn
dellNetFanTrayIndex=_DellNetFanTrayIndex_Object((1,3,6,1,4,1,6027,3,26,1,4,7,1,3),_DellNetFanTrayIndex_Type())
dellNetFanTrayIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetFanTrayIndex.setStatus(_B)
class _DellNetFanTrayOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),(_V,2),(_r,3)))
_DellNetFanTrayOperStatus_Type.__name__=_K
_DellNetFanTrayOperStatus_Object=MibTableColumn
dellNetFanTrayOperStatus=_DellNetFanTrayOperStatus_Object((1,3,6,1,4,1,6027,3,26,1,4,7,1,4),_DellNetFanTrayOperStatus_Type())
dellNetFanTrayOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetFanTrayOperStatus.setStatus(_B)
class _DellNetFanTrayPiecePartID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_DellNetFanTrayPiecePartID_Type.__name__=_I
_DellNetFanTrayPiecePartID_Object=MibTableColumn
dellNetFanTrayPiecePartID=_DellNetFanTrayPiecePartID_Object((1,3,6,1,4,1,6027,3,26,1,4,7,1,5),_DellNetFanTrayPiecePartID_Type())
dellNetFanTrayPiecePartID.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetFanTrayPiecePartID.setStatus(_B)
class _DellNetFanTrayPPIDRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_DellNetFanTrayPPIDRevision_Type.__name__=_I
_DellNetFanTrayPPIDRevision_Object=MibTableColumn
dellNetFanTrayPPIDRevision=_DellNetFanTrayPPIDRevision_Object((1,3,6,1,4,1,6027,3,26,1,4,7,1,6),_DellNetFanTrayPPIDRevision_Type())
dellNetFanTrayPPIDRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetFanTrayPPIDRevision.setStatus(_B)
class _DellNetFanTrayServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_DellNetFanTrayServiceTag_Type.__name__=_I
_DellNetFanTrayServiceTag_Object=MibTableColumn
dellNetFanTrayServiceTag=_DellNetFanTrayServiceTag_Object((1,3,6,1,4,1,6027,3,26,1,4,7,1,7),_DellNetFanTrayServiceTag_Type())
dellNetFanTrayServiceTag.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetFanTrayServiceTag.setStatus(_B)
class _DellNetFanTrayExpressServiceCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_DellNetFanTrayExpressServiceCode_Type.__name__=_I
_DellNetFanTrayExpressServiceCode_Object=MibTableColumn
dellNetFanTrayExpressServiceCode=_DellNetFanTrayExpressServiceCode_Object((1,3,6,1,4,1,6027,3,26,1,4,7,1,8),_DellNetFanTrayExpressServiceCode_Type())
dellNetFanTrayExpressServiceCode.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetFanTrayExpressServiceCode.setStatus(_B)
_DellNetFlashStorageTable_Object=MibTable
dellNetFlashStorageTable=_DellNetFlashStorageTable_Object((1,3,6,1,4,1,6027,3,26,1,4,8))
if mibBuilder.loadTexts:dellNetFlashStorageTable.setStatus(_B)
_DellNetFlashEntry_Object=MibTableRow
dellNetFlashEntry=_DellNetFlashEntry_Object((1,3,6,1,4,1,6027,3,26,1,4,8,1))
dellNetFlashEntry.setIndexNames((0,_A,_v))
if mibBuilder.loadTexts:dellNetFlashEntry.setStatus(_B)
_DellNetFlashPartitionNumber_Type=Integer32
_DellNetFlashPartitionNumber_Object=MibTableColumn
dellNetFlashPartitionNumber=_DellNetFlashPartitionNumber_Object((1,3,6,1,4,1,6027,3,26,1,4,8,1,1),_DellNetFlashPartitionNumber_Type())
dellNetFlashPartitionNumber.setMaxAccess(_L)
if mibBuilder.loadTexts:dellNetFlashPartitionNumber.setStatus(_B)
class _DellNetFlashPartitionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DellNetFlashPartitionName_Type.__name__=_I
_DellNetFlashPartitionName_Object=MibTableColumn
dellNetFlashPartitionName=_DellNetFlashPartitionName_Object((1,3,6,1,4,1,6027,3,26,1,4,8,1,2),_DellNetFlashPartitionName_Type())
dellNetFlashPartitionName.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetFlashPartitionName.setStatus(_B)
_DellNetFlashPartitionSize_Type=Integer32
_DellNetFlashPartitionSize_Object=MibTableColumn
dellNetFlashPartitionSize=_DellNetFlashPartitionSize_Object((1,3,6,1,4,1,6027,3,26,1,4,8,1,3),_DellNetFlashPartitionSize_Type())
dellNetFlashPartitionSize.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetFlashPartitionSize.setStatus(_B)
_DellNetFlashPartitionUsed_Type=Integer32
_DellNetFlashPartitionUsed_Object=MibTableColumn
dellNetFlashPartitionUsed=_DellNetFlashPartitionUsed_Object((1,3,6,1,4,1,6027,3,26,1,4,8,1,4),_DellNetFlashPartitionUsed_Type())
dellNetFlashPartitionUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetFlashPartitionUsed.setStatus(_B)
_DellNetFlashPartitionFree_Type=Integer32
_DellNetFlashPartitionFree_Object=MibTableColumn
dellNetFlashPartitionFree=_DellNetFlashPartitionFree_Object((1,3,6,1,4,1,6027,3,26,1,4,8,1,5),_DellNetFlashPartitionFree_Type())
dellNetFlashPartitionFree.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetFlashPartitionFree.setStatus(_B)
class _DellNetFlashPartitionMountPoint_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DellNetFlashPartitionMountPoint_Type.__name__=_I
_DellNetFlashPartitionMountPoint_Object=MibTableColumn
dellNetFlashPartitionMountPoint=_DellNetFlashPartitionMountPoint_Object((1,3,6,1,4,1,6027,3,26,1,4,8,1,6),_DellNetFlashPartitionMountPoint_Type())
dellNetFlashPartitionMountPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetFlashPartitionMountPoint.setStatus(_B)
_DellNetSysSwCoresTable_Object=MibTable
dellNetSysSwCoresTable=_DellNetSysSwCoresTable_Object((1,3,6,1,4,1,6027,3,26,1,4,9))
if mibBuilder.loadTexts:dellNetSysSwCoresTable.setStatus(_B)
_DellNetSysCoresEntry_Object=MibTableRow
dellNetSysCoresEntry=_DellNetSysCoresEntry_Object((1,3,6,1,4,1,6027,3,26,1,4,9,1))
dellNetSysCoresEntry.setIndexNames((0,_A,_T),(0,_A,_w))
if mibBuilder.loadTexts:dellNetSysCoresEntry.setStatus(_B)
_DellNetSysCoresInstance_Type=Integer32
_DellNetSysCoresInstance_Object=MibTableColumn
dellNetSysCoresInstance=_DellNetSysCoresInstance_Object((1,3,6,1,4,1,6027,3,26,1,4,9,1,1),_DellNetSysCoresInstance_Type())
dellNetSysCoresInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetSysCoresInstance.setStatus(_B)
_DellNetSysCoresFileName_Type=DisplayString
_DellNetSysCoresFileName_Object=MibTableColumn
dellNetSysCoresFileName=_DellNetSysCoresFileName_Object((1,3,6,1,4,1,6027,3,26,1,4,9,1,2),_DellNetSysCoresFileName_Type())
dellNetSysCoresFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetSysCoresFileName.setStatus(_B)
_DellNetSysCoresTimeCreated_Type=DellNetSwDate
_DellNetSysCoresTimeCreated_Object=MibTableColumn
dellNetSysCoresTimeCreated=_DellNetSysCoresTimeCreated_Object((1,3,6,1,4,1,6027,3,26,1,4,9,1,3),_DellNetSysCoresTimeCreated_Type())
dellNetSysCoresTimeCreated.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetSysCoresTimeCreated.setStatus(_B)
class _DellNetSysCoresStackUnitNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_DellNetSysCoresStackUnitNumber_Type.__name__=_K
_DellNetSysCoresStackUnitNumber_Object=MibTableColumn
dellNetSysCoresStackUnitNumber=_DellNetSysCoresStackUnitNumber_Object((1,3,6,1,4,1,6027,3,26,1,4,9,1,4),_DellNetSysCoresStackUnitNumber_Type())
dellNetSysCoresStackUnitNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetSysCoresStackUnitNumber.setStatus(_B)
_DellNetSysCoresProcess_Type=DisplayString
_DellNetSysCoresProcess_Object=MibTableColumn
dellNetSysCoresProcess=_DellNetSysCoresProcess_Object((1,3,6,1,4,1,6027,3,26,1,4,9,1,5),_DellNetSysCoresProcess_Type())
dellNetSysCoresProcess.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetSysCoresProcess.setStatus(_B)
_DellNetSysIfTable_Object=MibTable
dellNetSysIfTable=_DellNetSysIfTable_Object((1,3,6,1,4,1,6027,3,26,1,4,10))
if mibBuilder.loadTexts:dellNetSysIfTable.setStatus(_B)
_DellNetSysIfEntry_Object=MibTableRow
dellNetSysIfEntry=_DellNetSysIfEntry_Object((1,3,6,1,4,1,6027,3,26,1,4,10,1))
dellNetSysIfEntry.setIndexNames((0,_c,_d))
if mibBuilder.loadTexts:dellNetSysIfEntry.setStatus(_B)
_DellNetSysIfType_Type=DellNetIfType
_DellNetSysIfType_Object=MibTableColumn
dellNetSysIfType=_DellNetSysIfType_Object((1,3,6,1,4,1,6027,3,26,1,4,10,1,1),_DellNetSysIfType_Type())
dellNetSysIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetSysIfType.setStatus(_B)
_DellNetSysIfName_Type=DisplayString
_DellNetSysIfName_Object=MibTableColumn
dellNetSysIfName=_DellNetSysIfName_Object((1,3,6,1,4,1,6027,3,26,1,4,10,1,2),_DellNetSysIfName_Type())
dellNetSysIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetSysIfName.setStatus(_B)
class _DellNetSysIfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_DellNetSysIfAdminStatus_Type.__name__=_K
_DellNetSysIfAdminStatus_Object=MibTableColumn
dellNetSysIfAdminStatus=_DellNetSysIfAdminStatus_Object((1,3,6,1,4,1,6027,3,26,1,4,10,1,3),_DellNetSysIfAdminStatus_Type())
dellNetSysIfAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetSysIfAdminStatus.setStatus(_B)
class _DellNetSysIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ready',1),('portDown',2),('portProblem',3),('cardProblem',4),('cardDown',5),(_g,6)))
_DellNetSysIfOperStatus_Type.__name__=_K
_DellNetSysIfOperStatus_Object=MibTableColumn
dellNetSysIfOperStatus=_DellNetSysIfOperStatus_Object((1,3,6,1,4,1,6027,3,26,1,4,10,1,4),_DellNetSysIfOperStatus_Type())
dellNetSysIfOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetSysIfOperStatus.setStatus(_B)
_DellNetSysIfXfpRecvPower_Type=DellNetHundredthdB
_DellNetSysIfXfpRecvPower_Object=MibTableColumn
dellNetSysIfXfpRecvPower=_DellNetSysIfXfpRecvPower_Object((1,3,6,1,4,1,6027,3,26,1,4,10,1,5),_DellNetSysIfXfpRecvPower_Type())
dellNetSysIfXfpRecvPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetSysIfXfpRecvPower.setStatus(_M)
if mibBuilder.loadTexts:dellNetSysIfXfpRecvPower.setUnits('dB')
_DellNetSysIfXfpRecvTemp_Type=Integer32
_DellNetSysIfXfpRecvTemp_Object=MibTableColumn
dellNetSysIfXfpRecvTemp=_DellNetSysIfXfpRecvTemp_Object((1,3,6,1,4,1,6027,3,26,1,4,10,1,6),_DellNetSysIfXfpRecvTemp_Type())
dellNetSysIfXfpRecvTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetSysIfXfpRecvTemp.setStatus(_M)
_DellNetSysIfXfpTxPower_Type=DellNetHundredthdB
_DellNetSysIfXfpTxPower_Object=MibTableColumn
dellNetSysIfXfpTxPower=_DellNetSysIfXfpTxPower_Object((1,3,6,1,4,1,6027,3,26,1,4,10,1,7),_DellNetSysIfXfpTxPower_Type())
dellNetSysIfXfpTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetSysIfXfpTxPower.setStatus(_M)
if mibBuilder.loadTexts:dellNetSysIfXfpTxPower.setUnits('dB')
_DellNetSysAlarmObjects_ObjectIdentity=ObjectIdentity
dellNetSysAlarmObjects=_DellNetSysAlarmObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,26,1,5))
_DellNetSysAlarmMibNotifications_ObjectIdentity=ObjectIdentity
dellNetSysAlarmMibNotifications=_DellNetSysAlarmMibNotifications_ObjectIdentity((1,3,6,1,4,1,6027,3,26,1,5,1))
_DellNetSysAlarmVariable_ObjectIdentity=ObjectIdentity
dellNetSysAlarmVariable=_DellNetSysAlarmVariable_ObjectIdentity((1,3,6,1,4,1,6027,3,26,1,5,2))
_DellNetSysAlarmVarInteger_Type=Integer32
_DellNetSysAlarmVarInteger_Object=MibScalar
dellNetSysAlarmVarInteger=_DellNetSysAlarmVarInteger_Object((1,3,6,1,4,1,6027,3,26,1,5,2,1),_DellNetSysAlarmVarInteger_Type())
dellNetSysAlarmVarInteger.setMaxAccess(_N)
if mibBuilder.loadTexts:dellNetSysAlarmVarInteger.setStatus(_B)
_DellNetSysAlarmVarString_Type=OctetString
_DellNetSysAlarmVarString_Object=MibScalar
dellNetSysAlarmVarString=_DellNetSysAlarmVarString_Object((1,3,6,1,4,1,6027,3,26,1,5,2,2),_DellNetSysAlarmVarString_Type())
dellNetSysAlarmVarString.setMaxAccess(_N)
if mibBuilder.loadTexts:dellNetSysAlarmVarString.setStatus(_B)
_DellNetSysAlarmVarSlot_Type=Integer32
_DellNetSysAlarmVarSlot_Object=MibScalar
dellNetSysAlarmVarSlot=_DellNetSysAlarmVarSlot_Object((1,3,6,1,4,1,6027,3,26,1,5,2,3),_DellNetSysAlarmVarSlot_Type())
dellNetSysAlarmVarSlot.setMaxAccess(_N)
if mibBuilder.loadTexts:dellNetSysAlarmVarSlot.setStatus(_B)
_DellNetSysAlarmVarPort_Type=Integer32
_DellNetSysAlarmVarPort_Object=MibScalar
dellNetSysAlarmVarPort=_DellNetSysAlarmVarPort_Object((1,3,6,1,4,1,6027,3,26,1,5,2,4),_DellNetSysAlarmVarPort_Type())
dellNetSysAlarmVarPort.setMaxAccess(_N)
if mibBuilder.loadTexts:dellNetSysAlarmVarPort.setStatus(_B)
_DellNetSysAlarmVarChassisId_Type=Integer32
_DellNetSysAlarmVarChassisId_Object=MibScalar
dellNetSysAlarmVarChassisId=_DellNetSysAlarmVarChassisId_Object((1,3,6,1,4,1,6027,3,26,1,5,2,5),_DellNetSysAlarmVarChassisId_Type())
dellNetSysAlarmVarChassisId.setMaxAccess(_N)
if mibBuilder.loadTexts:dellNetSysAlarmVarChassisId.setStatus(_B)
_DellNetsysAlarmVarFanTrayId_Type=Integer32
_DellNetsysAlarmVarFanTrayId_Object=MibScalar
dellNetsysAlarmVarFanTrayId=_DellNetsysAlarmVarFanTrayId_Object((1,3,6,1,4,1,6027,3,26,1,5,2,6),_DellNetsysAlarmVarFanTrayId_Type())
dellNetsysAlarmVarFanTrayId.setMaxAccess(_N)
if mibBuilder.loadTexts:dellNetsysAlarmVarFanTrayId.setStatus(_B)
_DellNetsysAlarmVarPsuId_Type=Integer32
_DellNetsysAlarmVarPsuId_Object=MibScalar
dellNetsysAlarmVarPsuId=_DellNetsysAlarmVarPsuId_Object((1,3,6,1,4,1,6027,3,26,1,5,2,7),_DellNetsysAlarmVarPsuId_Type())
dellNetsysAlarmVarPsuId.setMaxAccess(_N)
if mibBuilder.loadTexts:dellNetsysAlarmVarPsuId.setStatus(_B)
_DellNetsysAlarmVarFanId_Type=Integer32
_DellNetsysAlarmVarFanId_Object=MibScalar
dellNetsysAlarmVarFanId=_DellNetsysAlarmVarFanId_Object((1,3,6,1,4,1,6027,3,26,1,5,2,8),_DellNetsysAlarmVarFanId_Type())
dellNetsysAlarmVarFanId.setMaxAccess(_N)
if mibBuilder.loadTexts:dellNetsysAlarmVarFanId.setStatus(_B)
_DellNetSysAlarmVarPeId_Type=Integer32
_DellNetSysAlarmVarPeId_Object=MibScalar
dellNetSysAlarmVarPeId=_DellNetSysAlarmVarPeId_Object((1,3,6,1,4,1,6027,3,26,1,5,2,9),_DellNetSysAlarmVarPeId_Type())
dellNetSysAlarmVarPeId.setMaxAccess(_N)
if mibBuilder.loadTexts:dellNetSysAlarmVarPeId.setStatus(_B)
_DellNetChassisMibConformance_ObjectIdentity=ObjectIdentity
dellNetChassisMibConformance=_DellNetChassisMibConformance_ObjectIdentity((1,3,6,1,4,1,6027,3,26,2))
_DellNetChassisMibCompliances_ObjectIdentity=ObjectIdentity
dellNetChassisMibCompliances=_DellNetChassisMibCompliances_ObjectIdentity((1,3,6,1,4,1,6027,3,26,2,1))
_DellNetChassisMibGroups_ObjectIdentity=ObjectIdentity
dellNetChassisMibGroups=_DellNetChassisMibGroups_ObjectIdentity((1,3,6,1,4,1,6027,3,26,2,2))
dellNetComponentGroup=ObjectGroup((1,3,6,1,4,1,6027,3,26,2,2,1))
dellNetComponentGroup.setObjects((_A,_x))
if mibBuilder.loadTexts:dellNetComponentGroup.setStatus(_B)
dellNetSystemGroup=ObjectGroup((1,3,6,1,4,1,6027,3,26,2,2,2))
dellNetSystemGroup.setObjects(*((_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:dellNetSystemGroup.setStatus(_B)
dellNetSysAlarmCardDown=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,1))
dellNetSysAlarmCardDown.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmCardDown.setStatus(_B)
dellNetSysAlarmCardUp=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,2))
dellNetSysAlarmCardUp.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmCardUp.setStatus(_B)
dellNetSysAlarmCardOffline=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,3))
dellNetSysAlarmCardOffline.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmCardOffline.setStatus(_B)
dellNetSysAlarmCardMismatch=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,4))
dellNetSysAlarmCardMismatch.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmCardMismatch.setStatus(_B)
dellNetSysAlarmRpmUp=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,5))
dellNetSysAlarmRpmUp.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmRpmUp.setStatus(_B)
dellNetSysAlarmRpmDown=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,6))
dellNetSysAlarmRpmDown.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmRpmDown.setStatus(_B)
dellNetSysAlarmPowersupplyDown=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,7))
dellNetSysAlarmPowersupplyDown.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmPowersupplyDown.setStatus(_B)
dellNetSysAlarmMinorTemperatureHigh=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,8))
dellNetSysAlarmMinorTemperatureHigh.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmMinorTemperatureHigh.setStatus(_B)
dellNetSysAlarmMajorTemperatureHigh=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,9))
dellNetSysAlarmMajorTemperatureHigh.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmMajorTemperatureHigh.setStatus(_B)
dellNetSysAlarmFanTrayDown=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,10))
dellNetSysAlarmFanTrayDown.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_P),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmFanTrayDown.setStatus(_B)
dellNetSysAlarmPowersupplyClear=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,11))
dellNetSysAlarmPowersupplyClear.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_O),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmPowersupplyClear.setStatus(_B)
dellNetSysAlarmMinorTemperatureClear=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,12))
dellNetSysAlarmMinorTemperatureClear.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmMinorTemperatureClear.setStatus(_B)
dellNetSysAlarmMajorTemperatureClear=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,13))
dellNetSysAlarmMajorTemperatureClear.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmMajorTemperatureClear.setStatus(_B)
dellNetSysAlarmFanTrayClear=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,14))
dellNetSysAlarmFanTrayClear.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_P),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmFanTrayClear.setStatus(_B)
dellNetSysAlarmMinorFanBadClear=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,15))
dellNetSysAlarmMinorFanBadClear.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_P),(_A,_b),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmMinorFanBadClear.setStatus(_B)
dellNetSysAlarmMajorPS=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,16))
dellNetSysAlarmMajorPS.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_O),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmMajorPS.setStatus(_B)
dellNetSysAlarmMajorPSClr=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,17))
dellNetSysAlarmMajorPSClr.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_O),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmMajorPSClr.setStatus(_B)
dellNetSysAlarmMinorPS=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,18))
dellNetSysAlarmMinorPS.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_O),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmMinorPS.setStatus(_B)
dellNetSysAlarmMinorPSClr=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,19))
dellNetSysAlarmMinorPSClr.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_O),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmMinorPSClr.setStatus(_B)
dellNetSysAlarmMinorFanBad=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,20))
dellNetSysAlarmMinorFanBad.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_P),(_A,_b),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmMinorFanBad.setStatus(_B)
dellNetSysAlarmRpmPrimary=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,21))
dellNetSysAlarmRpmPrimary.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmRpmPrimary.setStatus(_B)
dellNetSysSnmpIpAclDeny=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,22))
dellNetSysSnmpIpAclDeny.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysSnmpIpAclDeny.setStatus(_B)
dellNetSysAlarmCardVersionMismatch=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,23))
dellNetSysAlarmCardVersionMismatch.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmCardVersionMismatch.setStatus(_B)
dellNetSysAlarmUnsupportedOptic=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,24))
dellNetSysAlarmUnsupportedOptic.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmUnsupportedOptic.setStatus(_B)
dellNetSysAlarmFanTrayOrPsuDown=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,25))
dellNetSysAlarmFanTrayOrPsuDown.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_P),(_A,_O),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmFanTrayOrPsuDown.setStatus(_B)
dellNetSysAlarmFanTrayOrPsuClear=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,26))
dellNetSysAlarmFanTrayOrPsuClear.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_P),(_A,_O),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmFanTrayOrPsuClear.setStatus(_B)
dellNetSysAlarmPEUp=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,27))
dellNetSysAlarmPEUp.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmPEUp.setStatus(_B)
dellNetSysAlarmPEDown=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,28))
dellNetSysAlarmPEDown.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmPEDown.setStatus(_B)
dellNetSysAlarmPEUnitUp=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,29))
dellNetSysAlarmPEUnitUp.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmPEUnitUp.setStatus(_B)
dellNetSysAlarmPEUnitDown=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,30))
dellNetSysAlarmPEUnitDown.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmPEUnitDown.setStatus(_B)
dellNetSysAlarmExdCpuThreshold=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,31))
dellNetSysAlarmExdCpuThreshold.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmExdCpuThreshold.setStatus(_B)
dellNetSysAlarmClrCpuThreshold=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,32))
dellNetSysAlarmClrCpuThreshold.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmClrCpuThreshold.setStatus(_B)
dellNetSysAlarmExdMemThreshold=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,33))
dellNetSysAlarmExdMemThreshold.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmExdMemThreshold.setStatus(_B)
dellNetSysAlarmClrMemThreshold=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,34))
dellNetSysAlarmClrMemThreshold.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmClrMemThreshold.setStatus(_B)
dellNetSysAlarmTaskSuspend=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,35))
dellNetSysAlarmTaskSuspend.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmTaskSuspend.setStatus(_B)
dellNetSysAlarmTaskTerm=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,36))
dellNetSysAlarmTaskTerm.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmTaskTerm.setStatus(_B)
dellNetSysAlarmMacStationMove=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,37))
dellNetSysAlarmMacStationMove.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmMacStationMove.setStatus(_B)
dellNetSysAlarmCardReset=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,38))
dellNetSysAlarmCardReset.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmCardReset.setStatus(_M)
dellNetSysAlarmCardRemove=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,39))
dellNetSysAlarmCardRemove.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmCardRemove.setStatus(_M)
dellNetSysAlarmCardProblem=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,40))
dellNetSysAlarmCardProblem.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmCardProblem.setStatus(_M)
dellNetSysAlarmCutoff=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,41))
dellNetSysAlarmCutoff.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmCutoff.setStatus(_M)
dellNetSysAlarmSRAMParityErrorDetect=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,42))
dellNetSysAlarmSRAMParityErrorDetect.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmSRAMParityErrorDetect.setStatus(_M)
dellNetSysAlarmAcDcMixedPowerSupplyDetect=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,43))
dellNetSysAlarmAcDcMixedPowerSupplyDetect.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmAcDcMixedPowerSupplyDetect.setStatus(_M)
dellNetSysAlarmVrrpGoMaster=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,44))
dellNetSysAlarmVrrpGoMaster.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmVrrpGoMaster.setStatus(_M)
dellNetSysAlarmVrrpGiveupMaster=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,45))
dellNetSysAlarmVrrpGiveupMaster.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmVrrpGiveupMaster.setStatus(_M)
dellNetSysAlarmStackUnitRoleChanged=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,46))
dellNetSysAlarmStackUnitRoleChanged.setObjects(*((_A,_AP),(_A,_D)))
if mibBuilder.loadTexts:dellNetSysAlarmStackUnitRoleChanged.setStatus(_B)
dellNetSysAlarmCpuCLkDegraded=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,47))
dellNetSysAlarmCpuCLkDegraded.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmCpuCLkDegraded.setStatus(_B)
dellNetSysAlarmDynamicFanout=NotificationType((1,3,6,1,4,1,6027,3,26,1,5,1,48))
dellNetSysAlarmDynamicFanout.setObjects(*((_A,_E),(_A,_D),(_A,_F),(_A,_G),(_A,_J),(_A,_H)))
if mibBuilder.loadTexts:dellNetSysAlarmDynamicFanout.setStatus(_B)
dellNetChassisNotificationGroup=NotificationGroup((1,3,6,1,4,1,6027,3,26,2,2,3))
dellNetChassisNotificationGroup.setObjects(*((_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az),(_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3),(_A,_B4),(_A,_B5),(_A,_B6),(_A,_B7)))
if mibBuilder.loadTexts:dellNetChassisNotificationGroup.setStatus(_B)
dellNetChassisMibCompliance=ModuleCompliance((1,3,6,1,4,1,6027,3,26,2,1,1))
dellNetChassisMibCompliance.setObjects(*((_A,_B8),(_A,_B9),(_A,_BA)))
if mibBuilder.loadTexts:dellNetChassisMibCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'dellNetChassisMib':dellNetChassisMib,'dellNetSysObject':dellNetSysObject,'dellNetSysParameter':dellNetSysParameter,_x:dellNetDeviceType,'dellNetChassisObject':dellNetChassisObject,'dellNetNumChassis':dellNetNumChassis,'dellNetMaxNumChassis':dellNetMaxNumChassis,'dellNetChassisTable':dellNetChassisTable,'dellNetChassisEntry':dellNetChassisEntry,_Y:dellNetChassisIndex,'dellNetChassisType':dellNetChassisType,'dellNetChassisMacAddr':dellNetChassisMacAddr,'dellNetChassisSerialNumber':dellNetChassisSerialNumber,'dellNetChassisPartNum':dellNetChassisPartNum,'dellNetChassisProductRev':dellNetChassisProductRev,'dellNetChassisVendorId':dellNetChassisVendorId,'dellNetChassisMfgDate':dellNetChassisMfgDate,'dellNetChassisCountryCode':dellNetChassisCountryCode,'dellNetChassisPPIDRev':dellNetChassisPPIDRev,'dellNetChassisServiceTag':dellNetChassisServiceTag,'dellNetChassisExpServiceCode':dellNetChassisExpServiceCode,'dellNetChassisNumSlots':dellNetChassisNumSlots,'dellNetChassisNumLineCardSlots':dellNetChassisNumLineCardSlots,'dellNetChassisNumFanTrays':dellNetChassisNumFanTrays,'dellNetChassisNumPowerSupplies':dellNetChassisNumPowerSupplies,'dellNetCardTable':dellNetCardTable,'dellNetCardEntry':dellNetCardEntry,_e:dellNetCardIndex,'dellNetCardType':dellNetCardType,'dellNetCardDescription':dellNetCardDescription,'dellNetCardChassisIndex':dellNetCardChassisIndex,'dellNetCardStatus':dellNetCardStatus,'dellNetCardTemp':dellNetCardTemp,'dellNetCardVendorId':dellNetCardVendorId,'dellNetCardMfgDate':dellNetCardMfgDate,'dellNetCardPartNum':dellNetCardPartNum,'dellNetCardProductRev':dellNetCardProductRev,'dellNetCardProductOrder':dellNetCardProductOrder,'dellNetCardCountryCode':dellNetCardCountryCode,'dellNetCardPiecePartID':dellNetCardPiecePartID,'dellNetCardPPIDRevision':dellNetCardPPIDRevision,'dellNetCardServiceTag':dellNetCardServiceTag,'dellNetCardExpServiceCode':dellNetCardExpServiceCode,'dellNetCardNumOfPorts':dellNetCardNumOfPorts,'dellNetStackObject':dellNetStackObject,'dellNetNumStackUnits':dellNetNumStackUnits,'dellNetMaxStackableUnits':dellNetMaxStackableUnits,'dellNetStackUnitIndexNext':dellNetStackUnitIndexNext,'dellNetStackUnitTable':dellNetStackUnitTable,'dellNetStackUnitEntry':dellNetStackUnitEntry,_T:dellNetStackUnitNumber,'dellNetStackUnitIndex':dellNetStackUnitIndex,_AP:dellNetStackUnitMgmtStatus,'dellNetStackUnitHwMgmtPreference':dellNetStackUnitHwMgmtPreference,'dellNetStackUnitAdmMgmtPreference':dellNetStackUnitAdmMgmtPreference,'dellNetStackUnitModelId':dellNetStackUnitModelId,'dellNetStackUnitStatus':dellNetStackUnitStatus,'dellNetStackUnitDescription':dellNetStackUnitDescription,'dellNetStackUnitCodeVersion':dellNetStackUnitCodeVersion,'dellNetStackUnitSerialNumber':dellNetStackUnitSerialNumber,'dellNetStackUnitUpTime':dellNetStackUnitUpTime,'dellNetStackUnitTemp':dellNetStackUnitTemp,'dellNetStackUnitVendorId':dellNetStackUnitVendorId,'dellNetStackUnitMfgDate':dellNetStackUnitMfgDate,'dellNetStackUnitMacAddress':dellNetStackUnitMacAddress,'dellNetStackUnitPartNum':dellNetStackUnitPartNum,'dellNetStackUnitProductRev':dellNetStackUnitProductRev,'dellNetStackUnitProductOrder':dellNetStackUnitProductOrder,'dellNetStackUnitCountryCode':dellNetStackUnitCountryCode,'dellNetStackUnitPiecePartID':dellNetStackUnitPiecePartID,'dellNetStackUnitPPIDRevision':dellNetStackUnitPPIDRevision,'dellNetStackUnitServiceTag':dellNetStackUnitServiceTag,'dellNetStackUnitExpServiceCode':dellNetStackUnitExpServiceCode,'dellNetStackUnitNumOfPorts':dellNetStackUnitNumOfPorts,'dellNetStackUnitNumFanTrays':dellNetStackUnitNumFanTrays,'dellNetStackUnitNumPowerSupplies':dellNetStackUnitNumPowerSupplies,'dellNetStackUnitNumPluggableModules':dellNetStackUnitNumPluggableModules,'dellNetStackUnitIOMMode':dellNetStackUnitIOMMode,'dellNetStackUnitBladeSlotId':dellNetStackUnitBladeSlotId,'dellNetStackPortTable':dellNetStackPortTable,'dellNetStackPortEntry':dellNetStackPortEntry,_h:dellNetStackPortIndex,'dellNetStackPortConfiguredMode':dellNetStackPortConfiguredMode,'dellNetStackPortRunningMode':dellNetStackPortRunningMode,'dellNetStackPortLinkStatus':dellNetStackPortLinkStatus,'dellNetStackPortLinkSpeed':dellNetStackPortLinkSpeed,'dellNetStackPortRxDataRate':dellNetStackPortRxDataRate,'dellNetStackPortRxErrorRate':dellNetStackPortRxErrorRate,'dellNetStackPortRxTotalErrors':dellNetStackPortRxTotalErrors,'dellNetStackPortTxDataRate':dellNetStackPortTxDataRate,'dellNetStackPortTxErrorRate':dellNetStackPortTxErrorRate,'dellNetStackPortTxTotalErrors':dellNetStackPortTxTotalErrors,'dellNetWebUIURL':dellNetWebUIURL,'dellNetSystemComponent':dellNetSystemComponent,'dellNetPEBindingTable':dellNetPEBindingTable,'dellNetPEBindingEntry':dellNetPEBindingEntry,_j:dellNetPEBindCascadePortIfIndex,'dellNetPEBindPEIndex':dellNetPEBindPEIndex,'dellNetPETable':dellNetPETable,'dellNetPEEntry':dellNetPEEntry,_k:dellNetPEIndex,'dellNetPEPEID':dellNetPEPEID,'dellNetPEUnitID':dellNetPEUnitID,'dellNetPEType':dellNetPEType,'dellNetPEDescription':dellNetPEDescription,'dellNetPEStatus':dellNetPEStatus,'dellNetPETemp':dellNetPETemp,'dellNetPEVendorId':dellNetPEVendorId,'dellNetPEMfgDate':dellNetPEMfgDate,'dellNetPEPartNum':dellNetPEPartNum,'dellNetPEProductRev':dellNetPEProductRev,'dellNetPEProductOrder':dellNetPEProductOrder,'dellNetPECountryCode':dellNetPECountryCode,'dellNetPEPiecePartID':dellNetPEPiecePartID,'dellNetPEPPIDRevision':dellNetPEPPIDRevision,'dellNetPEServiceTag':dellNetPEServiceTag,'dellNetPEExpServiceCode':dellNetPEExpServiceCode,'dellNetPENumOfPorts':dellNetPENumOfPorts,'dellNetPENumFanTrays':dellNetPENumFanTrays,'dellNetPENumPowerSupplies':dellNetPENumPowerSupplies,'dellNetPENumPluggableModules':dellNetPENumPluggableModules,'dellNetProcessorTable':dellNetProcessorTable,'dellNetProcessorEntry':dellNetProcessorEntry,_W:dellNetProcessorDeviceType,_X:dellNetProcessorDeviceIndex,_a:dellNetProcessorIndex,_y:dellNetProcessorModule,_z:dellNetProcessorUpTime,_A0:dellNetProcessorMemSize,'dellNetProcessorResetReason':dellNetProcessorResetReason,'dellNetProcessorResetTime':dellNetProcessorResetTime,'dellNetCpuUtilTable':dellNetCpuUtilTable,'dellNetCpuUtilEntry':dellNetCpuUtilEntry,_A1:dellNetCpuUtil5Sec,_A2:dellNetCpuUtil1Min,_A3:dellNetCpuUtil5Min,_A4:dellNetCpuUtilMemUsage,'dellNetCpuFlashUsage':dellNetCpuFlashUsage,'dellNetSwModuleTable':dellNetSwModuleTable,'dellNetSwModuleEntry':dellNetSwModuleEntry,_A5:dellNetSwModuleRuntimeImgVersion,_A6:dellNetSwModuleRuntimeImgDate,_A7:dellNetSwModuleBootFlashImgVersion,_A8:dellNetSwModuleBootSelectorImgVersion,_A9:dellNetSwModuleNextRebootImage,_AA:dellNetSwModuleCurrentBootImage,_AB:dellNetSwModuleInPartitionAImgVers,_AC:dellNetSwModuleInPartitionBImgVers,'dellNetPowerSupplyTable':dellNetPowerSupplyTable,'dellNetPowerSupplyEntry':dellNetPowerSupplyEntry,_o:dellNetPowerDeviceType,_p:dellNetPowerDeviceIndex,_q:dellNetPowerSupplyIndex,_AD:dellNetPowerSupplyOperStatus,_AE:dellNetPowerSupplyType,_AF:dellNetPowerSupplyPiecePartID,_AG:dellNetPowerSupplyPPIDRevision,_AH:dellNetPowerSupplyServiceTag,_AI:dellNetPowerSupplyExpressServiceCode,_AJ:dellNetPowerSupplyUsage,'dellNetFanTrayTable':dellNetFanTrayTable,'dellNetFanTrayEntry':dellNetFanTrayEntry,_s:dellNetFanDeviceType,_t:dellNetFanDeviceIndex,_u:dellNetFanTrayIndex,_AK:dellNetFanTrayOperStatus,_AL:dellNetFanTrayPiecePartID,_AM:dellNetFanTrayPPIDRevision,_AN:dellNetFanTrayServiceTag,_AO:dellNetFanTrayExpressServiceCode,'dellNetFlashStorageTable':dellNetFlashStorageTable,'dellNetFlashEntry':dellNetFlashEntry,_v:dellNetFlashPartitionNumber,'dellNetFlashPartitionName':dellNetFlashPartitionName,'dellNetFlashPartitionSize':dellNetFlashPartitionSize,'dellNetFlashPartitionUsed':dellNetFlashPartitionUsed,'dellNetFlashPartitionFree':dellNetFlashPartitionFree,'dellNetFlashPartitionMountPoint':dellNetFlashPartitionMountPoint,'dellNetSysSwCoresTable':dellNetSysSwCoresTable,'dellNetSysCoresEntry':dellNetSysCoresEntry,_w:dellNetSysCoresInstance,'dellNetSysCoresFileName':dellNetSysCoresFileName,'dellNetSysCoresTimeCreated':dellNetSysCoresTimeCreated,'dellNetSysCoresStackUnitNumber':dellNetSysCoresStackUnitNumber,'dellNetSysCoresProcess':dellNetSysCoresProcess,'dellNetSysIfTable':dellNetSysIfTable,'dellNetSysIfEntry':dellNetSysIfEntry,'dellNetSysIfType':dellNetSysIfType,'dellNetSysIfName':dellNetSysIfName,'dellNetSysIfAdminStatus':dellNetSysIfAdminStatus,'dellNetSysIfOperStatus':dellNetSysIfOperStatus,'dellNetSysIfXfpRecvPower':dellNetSysIfXfpRecvPower,'dellNetSysIfXfpRecvTemp':dellNetSysIfXfpRecvTemp,'dellNetSysIfXfpTxPower':dellNetSysIfXfpTxPower,'dellNetSysAlarmObjects':dellNetSysAlarmObjects,'dellNetSysAlarmMibNotifications':dellNetSysAlarmMibNotifications,_AQ:dellNetSysAlarmCardDown,_AR:dellNetSysAlarmCardUp,_AS:dellNetSysAlarmCardOffline,_AT:dellNetSysAlarmCardMismatch,_AU:dellNetSysAlarmRpmUp,_AV:dellNetSysAlarmRpmDown,_AW:dellNetSysAlarmPowersupplyDown,_AX:dellNetSysAlarmMinorTemperatureHigh,_AY:dellNetSysAlarmMajorTemperatureHigh,_AZ:dellNetSysAlarmFanTrayDown,_Aa:dellNetSysAlarmPowersupplyClear,_Ab:dellNetSysAlarmMinorTemperatureClear,_Ac:dellNetSysAlarmMajorTemperatureClear,_Ad:dellNetSysAlarmFanTrayClear,_Ae:dellNetSysAlarmMinorFanBadClear,_Af:dellNetSysAlarmMajorPS,_Ag:dellNetSysAlarmMajorPSClr,_Ah:dellNetSysAlarmMinorPS,_Ai:dellNetSysAlarmMinorPSClr,_Aj:dellNetSysAlarmMinorFanBad,_Ak:dellNetSysAlarmRpmPrimary,_Al:dellNetSysSnmpIpAclDeny,_Am:dellNetSysAlarmCardVersionMismatch,_An:dellNetSysAlarmUnsupportedOptic,'dellNetSysAlarmFanTrayOrPsuDown':dellNetSysAlarmFanTrayOrPsuDown,'dellNetSysAlarmFanTrayOrPsuClear':dellNetSysAlarmFanTrayOrPsuClear,_Aq:dellNetSysAlarmPEUp,_Ar:dellNetSysAlarmPEDown,_Ao:dellNetSysAlarmPEUnitUp,_Ap:dellNetSysAlarmPEUnitDown,_As:dellNetSysAlarmExdCpuThreshold,_At:dellNetSysAlarmClrCpuThreshold,_Au:dellNetSysAlarmExdMemThreshold,_Av:dellNetSysAlarmClrMemThreshold,_Aw:dellNetSysAlarmTaskSuspend,_Ax:dellNetSysAlarmTaskTerm,_Ay:dellNetSysAlarmMacStationMove,_Az:dellNetSysAlarmCardReset,_A_:dellNetSysAlarmCardRemove,_B0:dellNetSysAlarmCardProblem,_B1:dellNetSysAlarmCutoff,_B2:dellNetSysAlarmSRAMParityErrorDetect,_B3:dellNetSysAlarmAcDcMixedPowerSupplyDetect,_B4:dellNetSysAlarmVrrpGoMaster,_B5:dellNetSysAlarmVrrpGiveupMaster,_B6:dellNetSysAlarmStackUnitRoleChanged,_B7:dellNetSysAlarmCpuCLkDegraded,'dellNetSysAlarmDynamicFanout':dellNetSysAlarmDynamicFanout,'dellNetSysAlarmVariable':dellNetSysAlarmVariable,_E:dellNetSysAlarmVarInteger,_D:dellNetSysAlarmVarString,_G:dellNetSysAlarmVarSlot,_J:dellNetSysAlarmVarPort,_F:dellNetSysAlarmVarChassisId,_P:dellNetsysAlarmVarFanTrayId,_O:dellNetsysAlarmVarPsuId,_b:dellNetsysAlarmVarFanId,_H:dellNetSysAlarmVarPeId,'dellNetChassisMibConformance':dellNetChassisMibConformance,'dellNetChassisMibCompliances':dellNetChassisMibCompliances,'dellNetChassisMibCompliance':dellNetChassisMibCompliance,'dellNetChassisMibGroups':dellNetChassisMibGroups,_B8:dellNetComponentGroup,_B9:dellNetSystemGroup,_BA:dellNetChassisNotificationGroup})