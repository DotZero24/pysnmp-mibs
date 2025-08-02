_BW='f10sSeriesNotificationGroup'
_BV='f10sSeriesSystemGroup'
_BU='f10sSeriesComponentGroup'
_BT='chAlarmStackPortLinkDown'
_BS='chAlarmStackPortLinkUp'
_BR='chAlarmStackUnitCodeMismatch'
_BQ='chAlarmStackUnitOffline'
_BP='chAlarmStackUnitReset'
_BO='chAlarmStackUnitUp'
_BN='chAlarmStackUnitDown'
_BM='chSysIfXfpTxPower'
_BL='chSysIfXfpRecvTemp'
_BK='chSysIfXfpRecvPower'
_BJ='chSysIfOperStatus'
_BI='chSysIfAdminStatus'
_BH='chSysIfName'
_BG='chSysIfType'
_BF='chSysCoresProcess'
_BE='chSysCoresStackUnitNumber'
_BD='chSysCoresTimeCreated'
_BC='chSysCoresFileName'
_BB='chStackUnitFlashUsageUtil'
_BA='chStackUnitMemUsageUtil'
_B9='chStackUnitCpuUtil5Min'
_B8='chStackUnitCpuUtil1Min'
_B7='chStackUnitCpuUtil5Sec'
_B6='chStackUnitCpuType'
_B5='chSysSwInPartitionBImgVers'
_B4='chSysSwInPartitionAImgVers'
_B3='chSysSwCurrentBootImage'
_B2='chSysSwNextRebootImage'
_B1='chSysSwBackupBootImgStatus'
_B0='chSysSwBackupBootImgDate'
_A_='chSysSwBackupBootImgVersion'
_Az='chSysSwCurrentBootImgStatus'
_Ay='chSysSwCurrentBootImgDate'
_Ax='chSysSwCurrentBootImgVersion'
_Aw='chSysSwRuntimeImgDate'
_Av='chSysSwRuntimeImgVersion'
_Au='chSysProcessorMemSize'
_At='chSysProcessorNvramSize'
_As='chSysProcessorUpTime'
_Ar='chSysProcessorModule'
_Aq='chSysStackPortTxTotalErrors'
_Ap='chSysStackPortTxErrorRate'
_Ao='chSysStackPortTxDataRate'
_An='chSysStackPortRxTotalErrors'
_Am='chSysStackPortRxErrorRate'
_Al='chSysStackPortRxDataRate'
_Ak='chSysStackPortLinkSpeed'
_Aj='chSysStackPortLinkStatus'
_Ai='chSysStackPortRunningMode'
_Ah='chSysStackPortConfiguredMode'
_Ag='chSysPortXfpTxPower'
_Af='chSysPortXfpRecvTemp'
_Ae='chSysPortXfpRecvPower'
_Ad='chSysPortIfIndex'
_Ac='chSysPortOperStatus'
_Ab='chSysPortAdminStatus'
_Aa='chSysPortType'
_AZ='chSysFanTrayExpressServiceCode'
_AY='chSysFanTrayServiceTag'
_AX='chSysFanTrayPPIDRevision'
_AW='chSysFanTrayPiecePartID'
_AV='chSysFanTrayOperStatus'
_AU='chSysPowerSupplyExpressServiceCode'
_AT='chSysPowerSupplyServiceTag'
_AS='chSysPowerSupplyPPIDRevision'
_AR='chSysPowerSupplyPiecePartID'
_AQ='chSysPowerSupplyType'
_AP='chSysPowerSupplyOperStatus'
_AO='chStackUnitExpressServiceCode'
_AN='chStackUnitServiceTag'
_AM='chStackUnitPPIDRevision'
_AL='chStackUnitPiecePartID'
_AK='chStackUnitRowStatus'
_AJ='chStackUnitNumPluggableModules'
_AI='chStackUnitNumPowerSupplies'
_AH='chStackUnitNumFanTrays'
_AG='chStackUnitNumFastEtherPorts'
_AF='chStackUnitNumGigEtherPorts'
_AE='chStackUnitNum10GigEtherPorts'
_AD='chStackUnitCountryCode'
_AC='chStackUnitProductOrder'
_AB='chStackUnitProductRev'
_AA='chStackUnitPartNum'
_A9='chStackUnitMacAddress'
_A8='chStackUnitMfgDate'
_A7='chStackUnitVendorId'
_A6='chStackUnitSysType'
_A5='chStackUnitType'
_A4='chStackUnitTemp'
_A3='chStackUnitUpTime'
_A2='chStackUnitSerialNumber'
_A1='chStackUnitCodeVersionInFlash'
_A0='chStackUnitCodeVersion'
_z='chStackUnitDescription'
_y='chStackUnitStatus'
_x='chStackUnitModelID'
_w='chStackUnitAdmMgmtPreference'
_v='chStackUnitHwMgmtPreference'
_u='chStackUnitMgmtStatus'
_t='chStackUnitSID'
_s='chSwitchTypeMgmtPreference'
_r='chSwitchTypeCodeType'
_q='chSwitchTypeModelID'
_p='chStackUnitIndexNext'
_o='chNumMaxStackableUnits'
_n='chNumStackUnits'
_m='bootImage-B'
_l='bootImage-A'
_k='failed'
_j='unknown'
_i='ethernet'
_h='cardDown'
_g='cardProblem'
_f='portProblem'
_e='portDown'
_d='absent'
_c='chStackUnitIndex'
_b='ifIndex'
_a='IF-MIB'
_Z='OctetString'
_Y='chSysCoresInstance'
_X='chSysStackPortIndex'
_W='chSysPortIndex'
_V='chSysFanTrayIndex'
_U='chSysPowerSupplyIndex'
_T='notPresent'
_S='chSwitchTypeSID'
_R='dB'
_Q='percent'
_P='down'
_O='up'
_N='read-create'
_M='Gauge32'
_L='deprecated'
_K='chAlarmVarString'
_J='chAlarmVarSlot'
_I='chAlarmVarPort'
_H='chAlarmVarInteger'
_G='chStackUnitNumber'
_F='DisplayString'
_E='Integer32'
_D='F10-CHASSIS-MIB'
_C='read-only'
_B='F10-S-SERIES-CHASSIS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Z,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
chAlarmVarInteger,chAlarmVarPort,chAlarmVarSlot,chAlarmVarString=mibBuilder.importSymbols(_D,_H,_I,_J,_K)
f10Mgmt,=mibBuilder.importSymbols('FORCE10-SMI','f10Mgmt')
F10ChassisType,F10HundredthdB,F10MfgDate,F10ProcessorModuleType,F10SSeriesPortType,F10SwDate=mibBuilder.importSymbols('FORCE10-TC','F10ChassisType','F10HundredthdB','F10MfgDate','F10ProcessorModuleType','F10SSeriesPortType','F10SwDate')
ifIndex,=mibBuilder.importSymbols(_a,_b)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_M,_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention')
f10SSerChassisMib=ModuleIdentity((1,3,6,1,4,1,6027,3,10))
if mibBuilder.loadTexts:f10SSerChassisMib.setRevisions(('2013-01-01 12:00','2012-12-21 12:00','2012-11-30 12:00','2012-03-27 12:00','2007-10-03 12:00'))
class CodeType(TextualConvention,Unsigned32):status=_A;displayHint='x'
class UnitType(TextualConvention,Unsigned32):status=_A;displayHint='x'
_F10SSerChassisObject_ObjectIdentity=ObjectIdentity
f10SSerChassisObject=_F10SSerChassisObject_ObjectIdentity((1,3,6,1,4,1,6027,3,10,1))
_ChObjects_ObjectIdentity=ObjectIdentity
chObjects=_ChObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,10,1,1))
_ChNumStackUnits_Type=Integer32
_ChNumStackUnits_Object=MibScalar
chNumStackUnits=_ChNumStackUnits_Object((1,3,6,1,4,1,6027,3,10,1,1,1),_ChNumStackUnits_Type())
chNumStackUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:chNumStackUnits.setStatus(_A)
_ChNumMaxStackableUnits_Type=Integer32
_ChNumMaxStackableUnits_Object=MibScalar
chNumMaxStackableUnits=_ChNumMaxStackableUnits_Object((1,3,6,1,4,1,6027,3,10,1,1,2),_ChNumMaxStackableUnits_Type())
chNumMaxStackableUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:chNumMaxStackableUnits.setStatus(_A)
class _ChStackUnitIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,12))
_ChStackUnitIndexNext_Type.__name__=_E
_ChStackUnitIndexNext_Object=MibScalar
chStackUnitIndexNext=_ChStackUnitIndexNext_Object((1,3,6,1,4,1,6027,3,10,1,1,3),_ChStackUnitIndexNext_Type())
chStackUnitIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitIndexNext.setStatus(_A)
_ChSysObjects_ObjectIdentity=ObjectIdentity
chSysObjects=_ChSysObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,10,1,2))
_ChSwitchTypeTable_Object=MibTable
chSwitchTypeTable=_ChSwitchTypeTable_Object((1,3,6,1,4,1,6027,3,10,1,2,1))
if mibBuilder.loadTexts:chSwitchTypeTable.setStatus(_L)
_ChSwitchTypeEntry_Object=MibTableRow
chSwitchTypeEntry=_ChSwitchTypeEntry_Object((1,3,6,1,4,1,6027,3,10,1,2,1,1))
chSwitchTypeEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:chSwitchTypeEntry.setStatus(_L)
_ChSwitchTypeSID_Type=Integer32
_ChSwitchTypeSID_Object=MibTableColumn
chSwitchTypeSID=_ChSwitchTypeSID_Object((1,3,6,1,4,1,6027,3,10,1,2,1,1,1),_ChSwitchTypeSID_Type())
chSwitchTypeSID.setMaxAccess(_C)
if mibBuilder.loadTexts:chSwitchTypeSID.setStatus(_L)
_ChSwitchTypeModelID_Type=DisplayString
_ChSwitchTypeModelID_Object=MibTableColumn
chSwitchTypeModelID=_ChSwitchTypeModelID_Object((1,3,6,1,4,1,6027,3,10,1,2,1,1,2),_ChSwitchTypeModelID_Type())
chSwitchTypeModelID.setMaxAccess(_C)
if mibBuilder.loadTexts:chSwitchTypeModelID.setStatus(_L)
_ChSwitchTypeCodeType_Type=CodeType
_ChSwitchTypeCodeType_Object=MibTableColumn
chSwitchTypeCodeType=_ChSwitchTypeCodeType_Object((1,3,6,1,4,1,6027,3,10,1,2,1,1,3),_ChSwitchTypeCodeType_Type())
chSwitchTypeCodeType.setMaxAccess(_C)
if mibBuilder.loadTexts:chSwitchTypeCodeType.setStatus(_L)
class _ChSwitchTypeMgmtPreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,15))
_ChSwitchTypeMgmtPreference_Type.__name__=_E
_ChSwitchTypeMgmtPreference_Object=MibTableColumn
chSwitchTypeMgmtPreference=_ChSwitchTypeMgmtPreference_Object((1,3,6,1,4,1,6027,3,10,1,2,1,1,4),_ChSwitchTypeMgmtPreference_Type())
chSwitchTypeMgmtPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:chSwitchTypeMgmtPreference.setStatus(_L)
_ChStackUnitTable_Object=MibTable
chStackUnitTable=_ChStackUnitTable_Object((1,3,6,1,4,1,6027,3,10,1,2,2))
if mibBuilder.loadTexts:chStackUnitTable.setStatus(_A)
_ChStackUnitEntry_Object=MibTableRow
chStackUnitEntry=_ChStackUnitEntry_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1))
chStackUnitEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:chStackUnitEntry.setStatus(_A)
_ChStackUnitIndex_Type=Integer32
_ChStackUnitIndex_Object=MibTableColumn
chStackUnitIndex=_ChStackUnitIndex_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,1),_ChStackUnitIndex_Type())
chStackUnitIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:chStackUnitIndex.setStatus(_A)
class _ChStackUnitNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,12))
_ChStackUnitNumber_Type.__name__=_E
_ChStackUnitNumber_Object=MibTableColumn
chStackUnitNumber=_ChStackUnitNumber_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,2),_ChStackUnitNumber_Type())
chStackUnitNumber.setMaxAccess(_N)
if mibBuilder.loadTexts:chStackUnitNumber.setStatus(_A)
_ChStackUnitSID_Type=Integer32
_ChStackUnitSID_Object=MibTableColumn
chStackUnitSID=_ChStackUnitSID_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,3),_ChStackUnitSID_Type())
chStackUnitSID.setMaxAccess(_N)
if mibBuilder.loadTexts:chStackUnitSID.setStatus(_L)
class _ChStackUnitMgmtStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('mgmtUnit',1),('standbyUnit',2),('stackUnit',3),('unassigned',4)))
_ChStackUnitMgmtStatus_Type.__name__=_E
_ChStackUnitMgmtStatus_Object=MibTableColumn
chStackUnitMgmtStatus=_ChStackUnitMgmtStatus_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,4),_ChStackUnitMgmtStatus_Type())
chStackUnitMgmtStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:chStackUnitMgmtStatus.setStatus(_A)
class _ChStackUnitHwMgmtPreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disabled',0),('unsassigned',1),('assigned',2)))
_ChStackUnitHwMgmtPreference_Type.__name__=_E
_ChStackUnitHwMgmtPreference_Object=MibTableColumn
chStackUnitHwMgmtPreference=_ChStackUnitHwMgmtPreference_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,5),_ChStackUnitHwMgmtPreference_Type())
chStackUnitHwMgmtPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitHwMgmtPreference.setStatus(_A)
class _ChStackUnitAdmMgmtPreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,15))
_ChStackUnitAdmMgmtPreference_Type.__name__=_E
_ChStackUnitAdmMgmtPreference_Object=MibTableColumn
chStackUnitAdmMgmtPreference=_ChStackUnitAdmMgmtPreference_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,6),_ChStackUnitAdmMgmtPreference_Type())
chStackUnitAdmMgmtPreference.setMaxAccess(_N)
if mibBuilder.loadTexts:chStackUnitAdmMgmtPreference.setStatus(_A)
_ChStackUnitModelID_Type=DisplayString
_ChStackUnitModelID_Object=MibTableColumn
chStackUnitModelID=_ChStackUnitModelID_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,7),_ChStackUnitModelID_Type())
chStackUnitModelID.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitModelID.setStatus(_A)
class _ChStackUnitStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ok',1),('unsupported',2),('codeMismatch',3),('configMismatch',4),('unitDown',5),(_T,6)))
_ChStackUnitStatus_Type.__name__=_E
_ChStackUnitStatus_Object=MibTableColumn
chStackUnitStatus=_ChStackUnitStatus_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,8),_ChStackUnitStatus_Type())
chStackUnitStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitStatus.setStatus(_A)
_ChStackUnitDescription_Type=DisplayString
_ChStackUnitDescription_Object=MibTableColumn
chStackUnitDescription=_ChStackUnitDescription_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,9),_ChStackUnitDescription_Type())
chStackUnitDescription.setMaxAccess(_N)
if mibBuilder.loadTexts:chStackUnitDescription.setStatus(_A)
_ChStackUnitCodeVersion_Type=DisplayString
_ChStackUnitCodeVersion_Object=MibTableColumn
chStackUnitCodeVersion=_ChStackUnitCodeVersion_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,10),_ChStackUnitCodeVersion_Type())
chStackUnitCodeVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitCodeVersion.setStatus(_A)
_ChStackUnitCodeVersionInFlash_Type=DisplayString
_ChStackUnitCodeVersionInFlash_Object=MibTableColumn
chStackUnitCodeVersionInFlash=_ChStackUnitCodeVersionInFlash_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,11),_ChStackUnitCodeVersionInFlash_Type())
chStackUnitCodeVersionInFlash.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitCodeVersionInFlash.setStatus(_A)
_ChStackUnitSerialNumber_Type=DisplayString
_ChStackUnitSerialNumber_Object=MibTableColumn
chStackUnitSerialNumber=_ChStackUnitSerialNumber_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,12),_ChStackUnitSerialNumber_Type())
chStackUnitSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitSerialNumber.setStatus(_A)
_ChStackUnitUpTime_Type=TimeTicks
_ChStackUnitUpTime_Object=MibTableColumn
chStackUnitUpTime=_ChStackUnitUpTime_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,13),_ChStackUnitUpTime_Type())
chStackUnitUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitUpTime.setStatus(_A)
_ChStackUnitTemp_Type=Gauge32
_ChStackUnitTemp_Object=MibTableColumn
chStackUnitTemp=_ChStackUnitTemp_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,14),_ChStackUnitTemp_Type())
chStackUnitTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitTemp.setStatus(_A)
_ChStackUnitType_Type=UnitType
_ChStackUnitType_Object=MibTableColumn
chStackUnitType=_ChStackUnitType_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,15),_ChStackUnitType_Type())
chStackUnitType.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitType.setStatus(_A)
_ChStackUnitSysType_Type=F10ChassisType
_ChStackUnitSysType_Object=MibTableColumn
chStackUnitSysType=_ChStackUnitSysType_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,16),_ChStackUnitSysType_Type())
chStackUnitSysType.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitSysType.setStatus(_A)
_ChStackUnitVendorId_Type=DisplayString
_ChStackUnitVendorId_Object=MibTableColumn
chStackUnitVendorId=_ChStackUnitVendorId_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,17),_ChStackUnitVendorId_Type())
chStackUnitVendorId.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitVendorId.setStatus(_A)
_ChStackUnitMfgDate_Type=F10MfgDate
_ChStackUnitMfgDate_Object=MibTableColumn
chStackUnitMfgDate=_ChStackUnitMfgDate_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,18),_ChStackUnitMfgDate_Type())
chStackUnitMfgDate.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitMfgDate.setStatus(_A)
_ChStackUnitMacAddress_Type=MacAddress
_ChStackUnitMacAddress_Object=MibTableColumn
chStackUnitMacAddress=_ChStackUnitMacAddress_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,19),_ChStackUnitMacAddress_Type())
chStackUnitMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitMacAddress.setStatus(_A)
_ChStackUnitPartNum_Type=DisplayString
_ChStackUnitPartNum_Object=MibTableColumn
chStackUnitPartNum=_ChStackUnitPartNum_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,20),_ChStackUnitPartNum_Type())
chStackUnitPartNum.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitPartNum.setStatus(_A)
_ChStackUnitProductRev_Type=DisplayString
_ChStackUnitProductRev_Object=MibTableColumn
chStackUnitProductRev=_ChStackUnitProductRev_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,21),_ChStackUnitProductRev_Type())
chStackUnitProductRev.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitProductRev.setStatus(_A)
_ChStackUnitProductOrder_Type=DisplayString
_ChStackUnitProductOrder_Object=MibTableColumn
chStackUnitProductOrder=_ChStackUnitProductOrder_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,22),_ChStackUnitProductOrder_Type())
chStackUnitProductOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitProductOrder.setStatus(_A)
class _ChStackUnitCountryCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_ChStackUnitCountryCode_Type.__name__=_Z
_ChStackUnitCountryCode_Object=MibTableColumn
chStackUnitCountryCode=_ChStackUnitCountryCode_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,23),_ChStackUnitCountryCode_Type())
chStackUnitCountryCode.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitCountryCode.setStatus(_A)
_ChStackUnitNum10GigEtherPorts_Type=Integer32
_ChStackUnitNum10GigEtherPorts_Object=MibTableColumn
chStackUnitNum10GigEtherPorts=_ChStackUnitNum10GigEtherPorts_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,24),_ChStackUnitNum10GigEtherPorts_Type())
chStackUnitNum10GigEtherPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitNum10GigEtherPorts.setStatus(_A)
_ChStackUnitNumGigEtherPorts_Type=Integer32
_ChStackUnitNumGigEtherPorts_Object=MibTableColumn
chStackUnitNumGigEtherPorts=_ChStackUnitNumGigEtherPorts_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,25),_ChStackUnitNumGigEtherPorts_Type())
chStackUnitNumGigEtherPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitNumGigEtherPorts.setStatus(_A)
_ChStackUnitNumFastEtherPorts_Type=Integer32
_ChStackUnitNumFastEtherPorts_Object=MibTableColumn
chStackUnitNumFastEtherPorts=_ChStackUnitNumFastEtherPorts_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,26),_ChStackUnitNumFastEtherPorts_Type())
chStackUnitNumFastEtherPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitNumFastEtherPorts.setStatus(_A)
_ChStackUnitNumFanTrays_Type=Integer32
_ChStackUnitNumFanTrays_Object=MibTableColumn
chStackUnitNumFanTrays=_ChStackUnitNumFanTrays_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,27),_ChStackUnitNumFanTrays_Type())
chStackUnitNumFanTrays.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitNumFanTrays.setStatus(_A)
_ChStackUnitNumPowerSupplies_Type=Integer32
_ChStackUnitNumPowerSupplies_Object=MibTableColumn
chStackUnitNumPowerSupplies=_ChStackUnitNumPowerSupplies_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,28),_ChStackUnitNumPowerSupplies_Type())
chStackUnitNumPowerSupplies.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitNumPowerSupplies.setStatus(_A)
_ChStackUnitNumPluggableModules_Type=Integer32
_ChStackUnitNumPluggableModules_Object=MibTableColumn
chStackUnitNumPluggableModules=_ChStackUnitNumPluggableModules_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,29),_ChStackUnitNumPluggableModules_Type())
chStackUnitNumPluggableModules.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitNumPluggableModules.setStatus(_A)
_ChStackUnitNum40GigEtherPorts_Type=Integer32
_ChStackUnitNum40GigEtherPorts_Object=MibTableColumn
chStackUnitNum40GigEtherPorts=_ChStackUnitNum40GigEtherPorts_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,30),_ChStackUnitNum40GigEtherPorts_Type())
chStackUnitNum40GigEtherPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitNum40GigEtherPorts.setStatus(_A)
_ChStackUnitRowStatus_Type=RowStatus
_ChStackUnitRowStatus_Object=MibTableColumn
chStackUnitRowStatus=_ChStackUnitRowStatus_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,31),_ChStackUnitRowStatus_Type())
chStackUnitRowStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:chStackUnitRowStatus.setStatus(_A)
class _ChStackUnitPiecePartID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_ChStackUnitPiecePartID_Type.__name__=_F
_ChStackUnitPiecePartID_Object=MibTableColumn
chStackUnitPiecePartID=_ChStackUnitPiecePartID_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,32),_ChStackUnitPiecePartID_Type())
chStackUnitPiecePartID.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitPiecePartID.setStatus(_A)
class _ChStackUnitPPIDRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_ChStackUnitPPIDRevision_Type.__name__=_F
_ChStackUnitPPIDRevision_Object=MibTableColumn
chStackUnitPPIDRevision=_ChStackUnitPPIDRevision_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,33),_ChStackUnitPPIDRevision_Type())
chStackUnitPPIDRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitPPIDRevision.setStatus(_A)
class _ChStackUnitServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_ChStackUnitServiceTag_Type.__name__=_F
_ChStackUnitServiceTag_Object=MibTableColumn
chStackUnitServiceTag=_ChStackUnitServiceTag_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,34),_ChStackUnitServiceTag_Type())
chStackUnitServiceTag.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitServiceTag.setStatus(_A)
class _ChStackUnitExpressServiceCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_ChStackUnitExpressServiceCode_Type.__name__=_F
_ChStackUnitExpressServiceCode_Object=MibTableColumn
chStackUnitExpressServiceCode=_ChStackUnitExpressServiceCode_Object((1,3,6,1,4,1,6027,3,10,1,2,2,1,35),_ChStackUnitExpressServiceCode_Type())
chStackUnitExpressServiceCode.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitExpressServiceCode.setStatus(_A)
_ChSysPowerSupplyTable_Object=MibTable
chSysPowerSupplyTable=_ChSysPowerSupplyTable_Object((1,3,6,1,4,1,6027,3,10,1,2,3))
if mibBuilder.loadTexts:chSysPowerSupplyTable.setStatus(_A)
_ChSysPowerSupplyEntry_Object=MibTableRow
chSysPowerSupplyEntry=_ChSysPowerSupplyEntry_Object((1,3,6,1,4,1,6027,3,10,1,2,3,1))
chSysPowerSupplyEntry.setIndexNames((0,_B,_G),(0,_B,_U))
if mibBuilder.loadTexts:chSysPowerSupplyEntry.setStatus(_A)
_ChSysPowerSupplyIndex_Type=Integer32
_ChSysPowerSupplyIndex_Object=MibTableColumn
chSysPowerSupplyIndex=_ChSysPowerSupplyIndex_Object((1,3,6,1,4,1,6027,3,10,1,2,3,1,1),_ChSysPowerSupplyIndex_Type())
chSysPowerSupplyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPowerSupplyIndex.setStatus(_A)
class _ChSysPowerSupplyOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),(_d,3)))
_ChSysPowerSupplyOperStatus_Type.__name__=_E
_ChSysPowerSupplyOperStatus_Object=MibTableColumn
chSysPowerSupplyOperStatus=_ChSysPowerSupplyOperStatus_Object((1,3,6,1,4,1,6027,3,10,1,2,3,1,2),_ChSysPowerSupplyOperStatus_Type())
chSysPowerSupplyOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPowerSupplyOperStatus.setStatus(_A)
class _ChSysPowerSupplyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ac',1),('dc',2)))
_ChSysPowerSupplyType_Type.__name__=_E
_ChSysPowerSupplyType_Object=MibTableColumn
chSysPowerSupplyType=_ChSysPowerSupplyType_Object((1,3,6,1,4,1,6027,3,10,1,2,3,1,3),_ChSysPowerSupplyType_Type())
chSysPowerSupplyType.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPowerSupplyType.setStatus(_A)
class _ChSysPowerSupplyPiecePartID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_ChSysPowerSupplyPiecePartID_Type.__name__=_F
_ChSysPowerSupplyPiecePartID_Object=MibTableColumn
chSysPowerSupplyPiecePartID=_ChSysPowerSupplyPiecePartID_Object((1,3,6,1,4,1,6027,3,10,1,2,3,1,4),_ChSysPowerSupplyPiecePartID_Type())
chSysPowerSupplyPiecePartID.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPowerSupplyPiecePartID.setStatus(_A)
class _ChSysPowerSupplyPPIDRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_ChSysPowerSupplyPPIDRevision_Type.__name__=_F
_ChSysPowerSupplyPPIDRevision_Object=MibTableColumn
chSysPowerSupplyPPIDRevision=_ChSysPowerSupplyPPIDRevision_Object((1,3,6,1,4,1,6027,3,10,1,2,3,1,5),_ChSysPowerSupplyPPIDRevision_Type())
chSysPowerSupplyPPIDRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPowerSupplyPPIDRevision.setStatus(_A)
class _ChSysPowerSupplyServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_ChSysPowerSupplyServiceTag_Type.__name__=_F
_ChSysPowerSupplyServiceTag_Object=MibTableColumn
chSysPowerSupplyServiceTag=_ChSysPowerSupplyServiceTag_Object((1,3,6,1,4,1,6027,3,10,1,2,3,1,6),_ChSysPowerSupplyServiceTag_Type())
chSysPowerSupplyServiceTag.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPowerSupplyServiceTag.setStatus(_A)
class _ChSysPowerSupplyExpressServiceCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_ChSysPowerSupplyExpressServiceCode_Type.__name__=_F
_ChSysPowerSupplyExpressServiceCode_Object=MibTableColumn
chSysPowerSupplyExpressServiceCode=_ChSysPowerSupplyExpressServiceCode_Object((1,3,6,1,4,1,6027,3,10,1,2,3,1,7),_ChSysPowerSupplyExpressServiceCode_Type())
chSysPowerSupplyExpressServiceCode.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPowerSupplyExpressServiceCode.setStatus(_A)
_ChSysFanTrayTable_Object=MibTable
chSysFanTrayTable=_ChSysFanTrayTable_Object((1,3,6,1,4,1,6027,3,10,1,2,4))
if mibBuilder.loadTexts:chSysFanTrayTable.setStatus(_A)
_ChSysFanTrayEntry_Object=MibTableRow
chSysFanTrayEntry=_ChSysFanTrayEntry_Object((1,3,6,1,4,1,6027,3,10,1,2,4,1))
chSysFanTrayEntry.setIndexNames((0,_B,_G),(0,_B,_V))
if mibBuilder.loadTexts:chSysFanTrayEntry.setStatus(_A)
_ChSysFanTrayIndex_Type=Integer32
_ChSysFanTrayIndex_Object=MibTableColumn
chSysFanTrayIndex=_ChSysFanTrayIndex_Object((1,3,6,1,4,1,6027,3,10,1,2,4,1,1),_ChSysFanTrayIndex_Type())
chSysFanTrayIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysFanTrayIndex.setStatus(_A)
class _ChSysFanTrayOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),(_d,3)))
_ChSysFanTrayOperStatus_Type.__name__=_E
_ChSysFanTrayOperStatus_Object=MibTableColumn
chSysFanTrayOperStatus=_ChSysFanTrayOperStatus_Object((1,3,6,1,4,1,6027,3,10,1,2,4,1,2),_ChSysFanTrayOperStatus_Type())
chSysFanTrayOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysFanTrayOperStatus.setStatus(_A)
class _ChSysFanTrayPiecePartID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_ChSysFanTrayPiecePartID_Type.__name__=_F
_ChSysFanTrayPiecePartID_Object=MibTableColumn
chSysFanTrayPiecePartID=_ChSysFanTrayPiecePartID_Object((1,3,6,1,4,1,6027,3,10,1,2,4,1,3),_ChSysFanTrayPiecePartID_Type())
chSysFanTrayPiecePartID.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysFanTrayPiecePartID.setStatus(_A)
class _ChSysFanTrayPPIDRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_ChSysFanTrayPPIDRevision_Type.__name__=_F
_ChSysFanTrayPPIDRevision_Object=MibTableColumn
chSysFanTrayPPIDRevision=_ChSysFanTrayPPIDRevision_Object((1,3,6,1,4,1,6027,3,10,1,2,4,1,4),_ChSysFanTrayPPIDRevision_Type())
chSysFanTrayPPIDRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysFanTrayPPIDRevision.setStatus(_A)
class _ChSysFanTrayServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_ChSysFanTrayServiceTag_Type.__name__=_F
_ChSysFanTrayServiceTag_Object=MibTableColumn
chSysFanTrayServiceTag=_ChSysFanTrayServiceTag_Object((1,3,6,1,4,1,6027,3,10,1,2,4,1,5),_ChSysFanTrayServiceTag_Type())
chSysFanTrayServiceTag.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysFanTrayServiceTag.setStatus(_A)
class _ChSysFanTrayExpressServiceCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_ChSysFanTrayExpressServiceCode_Type.__name__=_F
_ChSysFanTrayExpressServiceCode_Object=MibTableColumn
chSysFanTrayExpressServiceCode=_ChSysFanTrayExpressServiceCode_Object((1,3,6,1,4,1,6027,3,10,1,2,4,1,6),_ChSysFanTrayExpressServiceCode_Type())
chSysFanTrayExpressServiceCode.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysFanTrayExpressServiceCode.setStatus(_A)
_ChSysPortTable_Object=MibTable
chSysPortTable=_ChSysPortTable_Object((1,3,6,1,4,1,6027,3,10,1,2,5))
if mibBuilder.loadTexts:chSysPortTable.setStatus(_A)
_ChSysPortEntry_Object=MibTableRow
chSysPortEntry=_ChSysPortEntry_Object((1,3,6,1,4,1,6027,3,10,1,2,5,1))
chSysPortEntry.setIndexNames((0,_B,_G),(0,_B,_W))
if mibBuilder.loadTexts:chSysPortEntry.setStatus(_A)
_ChSysPortIndex_Type=Integer32
_ChSysPortIndex_Object=MibTableColumn
chSysPortIndex=_ChSysPortIndex_Object((1,3,6,1,4,1,6027,3,10,1,2,5,1,1),_ChSysPortIndex_Type())
chSysPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPortIndex.setStatus(_A)
_ChSysPortType_Type=F10SSeriesPortType
_ChSysPortType_Object=MibTableColumn
chSysPortType=_ChSysPortType_Object((1,3,6,1,4,1,6027,3,10,1,2,5,1,2),_ChSysPortType_Type())
chSysPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPortType.setStatus(_A)
class _ChSysPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_ChSysPortAdminStatus_Type.__name__=_E
_ChSysPortAdminStatus_Object=MibTableColumn
chSysPortAdminStatus=_ChSysPortAdminStatus_Object((1,3,6,1,4,1,6027,3,10,1,2,5,1,3),_ChSysPortAdminStatus_Type())
chSysPortAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPortAdminStatus.setStatus(_A)
class _ChSysPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ready',1),(_e,2),(_f,3),(_g,4),(_h,5),(_T,6)))
_ChSysPortOperStatus_Type.__name__=_E
_ChSysPortOperStatus_Object=MibTableColumn
chSysPortOperStatus=_ChSysPortOperStatus_Object((1,3,6,1,4,1,6027,3,10,1,2,5,1,4),_ChSysPortOperStatus_Type())
chSysPortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPortOperStatus.setStatus(_A)
_ChSysPortIfIndex_Type=Integer32
_ChSysPortIfIndex_Object=MibTableColumn
chSysPortIfIndex=_ChSysPortIfIndex_Object((1,3,6,1,4,1,6027,3,10,1,2,5,1,5),_ChSysPortIfIndex_Type())
chSysPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPortIfIndex.setStatus(_A)
_ChSysPortXfpRecvPower_Type=F10HundredthdB
_ChSysPortXfpRecvPower_Object=MibTableColumn
chSysPortXfpRecvPower=_ChSysPortXfpRecvPower_Object((1,3,6,1,4,1,6027,3,10,1,2,5,1,6),_ChSysPortXfpRecvPower_Type())
chSysPortXfpRecvPower.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPortXfpRecvPower.setStatus(_A)
if mibBuilder.loadTexts:chSysPortXfpRecvPower.setUnits(_R)
_ChSysPortXfpRecvTemp_Type=Integer32
_ChSysPortXfpRecvTemp_Object=MibTableColumn
chSysPortXfpRecvTemp=_ChSysPortXfpRecvTemp_Object((1,3,6,1,4,1,6027,3,10,1,2,5,1,7),_ChSysPortXfpRecvTemp_Type())
chSysPortXfpRecvTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPortXfpRecvTemp.setStatus(_A)
_ChSysPortXfpTxPower_Type=F10HundredthdB
_ChSysPortXfpTxPower_Object=MibTableColumn
chSysPortXfpTxPower=_ChSysPortXfpTxPower_Object((1,3,6,1,4,1,6027,3,10,1,2,5,1,8),_ChSysPortXfpTxPower_Type())
chSysPortXfpTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPortXfpTxPower.setStatus(_A)
if mibBuilder.loadTexts:chSysPortXfpTxPower.setUnits(_R)
_ChSysStackPortTable_Object=MibTable
chSysStackPortTable=_ChSysStackPortTable_Object((1,3,6,1,4,1,6027,3,10,1,2,6))
if mibBuilder.loadTexts:chSysStackPortTable.setStatus(_A)
_ChSysStackPortEntry_Object=MibTableRow
chSysStackPortEntry=_ChSysStackPortEntry_Object((1,3,6,1,4,1,6027,3,10,1,2,6,1))
chSysStackPortEntry.setIndexNames((0,_B,_G),(0,_B,_X))
if mibBuilder.loadTexts:chSysStackPortEntry.setStatus(_A)
_ChSysStackPortIndex_Type=Integer32
_ChSysStackPortIndex_Object=MibTableColumn
chSysStackPortIndex=_ChSysStackPortIndex_Object((1,3,6,1,4,1,6027,3,10,1,2,6,1,1),_ChSysStackPortIndex_Type())
chSysStackPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysStackPortIndex.setStatus(_A)
class _ChSysStackPortConfiguredMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stack',1),(_i,2),(_j,3)))
_ChSysStackPortConfiguredMode_Type.__name__=_E
_ChSysStackPortConfiguredMode_Object=MibTableColumn
chSysStackPortConfiguredMode=_ChSysStackPortConfiguredMode_Object((1,3,6,1,4,1,6027,3,10,1,2,6,1,2),_ChSysStackPortConfiguredMode_Type())
chSysStackPortConfiguredMode.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysStackPortConfiguredMode.setStatus(_A)
class _ChSysStackPortRunningMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stack',1),(_i,2),(_j,3)))
_ChSysStackPortRunningMode_Type.__name__=_E
_ChSysStackPortRunningMode_Object=MibTableColumn
chSysStackPortRunningMode=_ChSysStackPortRunningMode_Object((1,3,6,1,4,1,6027,3,10,1,2,6,1,3),_ChSysStackPortRunningMode_Type())
chSysStackPortRunningMode.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysStackPortRunningMode.setStatus(_A)
class _ChSysStackPortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_ChSysStackPortLinkStatus_Type.__name__=_E
_ChSysStackPortLinkStatus_Object=MibTableColumn
chSysStackPortLinkStatus=_ChSysStackPortLinkStatus_Object((1,3,6,1,4,1,6027,3,10,1,2,6,1,4),_ChSysStackPortLinkStatus_Type())
chSysStackPortLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysStackPortLinkStatus.setStatus(_A)
_ChSysStackPortLinkSpeed_Type=Gauge32
_ChSysStackPortLinkSpeed_Object=MibTableColumn
chSysStackPortLinkSpeed=_ChSysStackPortLinkSpeed_Object((1,3,6,1,4,1,6027,3,10,1,2,6,1,5),_ChSysStackPortLinkSpeed_Type())
chSysStackPortLinkSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysStackPortLinkSpeed.setStatus(_A)
_ChSysStackPortRxDataRate_Type=Counter32
_ChSysStackPortRxDataRate_Object=MibTableColumn
chSysStackPortRxDataRate=_ChSysStackPortRxDataRate_Object((1,3,6,1,4,1,6027,3,10,1,2,6,1,6),_ChSysStackPortRxDataRate_Type())
chSysStackPortRxDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysStackPortRxDataRate.setStatus(_A)
_ChSysStackPortRxErrorRate_Type=Counter32
_ChSysStackPortRxErrorRate_Object=MibTableColumn
chSysStackPortRxErrorRate=_ChSysStackPortRxErrorRate_Object((1,3,6,1,4,1,6027,3,10,1,2,6,1,7),_ChSysStackPortRxErrorRate_Type())
chSysStackPortRxErrorRate.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysStackPortRxErrorRate.setStatus(_A)
_ChSysStackPortRxTotalErrors_Type=Counter32
_ChSysStackPortRxTotalErrors_Object=MibTableColumn
chSysStackPortRxTotalErrors=_ChSysStackPortRxTotalErrors_Object((1,3,6,1,4,1,6027,3,10,1,2,6,1,8),_ChSysStackPortRxTotalErrors_Type())
chSysStackPortRxTotalErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysStackPortRxTotalErrors.setStatus(_A)
_ChSysStackPortTxDataRate_Type=Counter32
_ChSysStackPortTxDataRate_Object=MibTableColumn
chSysStackPortTxDataRate=_ChSysStackPortTxDataRate_Object((1,3,6,1,4,1,6027,3,10,1,2,6,1,9),_ChSysStackPortTxDataRate_Type())
chSysStackPortTxDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysStackPortTxDataRate.setStatus(_A)
_ChSysStackPortTxErrorRate_Type=Counter32
_ChSysStackPortTxErrorRate_Object=MibTableColumn
chSysStackPortTxErrorRate=_ChSysStackPortTxErrorRate_Object((1,3,6,1,4,1,6027,3,10,1,2,6,1,10),_ChSysStackPortTxErrorRate_Type())
chSysStackPortTxErrorRate.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysStackPortTxErrorRate.setStatus(_A)
_ChSysStackPortTxTotalErrors_Type=Counter32
_ChSysStackPortTxTotalErrors_Object=MibTableColumn
chSysStackPortTxTotalErrors=_ChSysStackPortTxTotalErrors_Object((1,3,6,1,4,1,6027,3,10,1,2,6,1,11),_ChSysStackPortTxTotalErrors_Type())
chSysStackPortTxTotalErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysStackPortTxTotalErrors.setStatus(_A)
_ChSysProcessorTable_Object=MibTable
chSysProcessorTable=_ChSysProcessorTable_Object((1,3,6,1,4,1,6027,3,10,1,2,7))
if mibBuilder.loadTexts:chSysProcessorTable.setStatus(_A)
_ChSysProcessorEntry_Object=MibTableRow
chSysProcessorEntry=_ChSysProcessorEntry_Object((1,3,6,1,4,1,6027,3,10,1,2,7,1))
chSysProcessorEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:chSysProcessorEntry.setStatus(_A)
_ChSysProcessorModule_Type=F10ProcessorModuleType
_ChSysProcessorModule_Object=MibTableColumn
chSysProcessorModule=_ChSysProcessorModule_Object((1,3,6,1,4,1,6027,3,10,1,2,7,1,1),_ChSysProcessorModule_Type())
chSysProcessorModule.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysProcessorModule.setStatus(_A)
_ChSysProcessorUpTime_Type=TimeTicks
_ChSysProcessorUpTime_Object=MibTableColumn
chSysProcessorUpTime=_ChSysProcessorUpTime_Object((1,3,6,1,4,1,6027,3,10,1,2,7,1,2),_ChSysProcessorUpTime_Type())
chSysProcessorUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysProcessorUpTime.setStatus(_A)
_ChSysProcessorNvramSize_Type=Integer32
_ChSysProcessorNvramSize_Object=MibTableColumn
chSysProcessorNvramSize=_ChSysProcessorNvramSize_Object((1,3,6,1,4,1,6027,3,10,1,2,7,1,3),_ChSysProcessorNvramSize_Type())
chSysProcessorNvramSize.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysProcessorNvramSize.setStatus(_A)
_ChSysProcessorMemSize_Type=Integer32
_ChSysProcessorMemSize_Object=MibTableColumn
chSysProcessorMemSize=_ChSysProcessorMemSize_Object((1,3,6,1,4,1,6027,3,10,1,2,7,1,4),_ChSysProcessorMemSize_Type())
chSysProcessorMemSize.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysProcessorMemSize.setStatus(_A)
_ChSysSwModuleTable_Object=MibTable
chSysSwModuleTable=_ChSysSwModuleTable_Object((1,3,6,1,4,1,6027,3,10,1,2,8))
if mibBuilder.loadTexts:chSysSwModuleTable.setStatus(_A)
_ChSysSwModuleEntry_Object=MibTableRow
chSysSwModuleEntry=_ChSysSwModuleEntry_Object((1,3,6,1,4,1,6027,3,10,1,2,8,1))
chSysSwModuleEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:chSysSwModuleEntry.setStatus(_A)
_ChSysSwRuntimeImgVersion_Type=DisplayString
_ChSysSwRuntimeImgVersion_Object=MibTableColumn
chSysSwRuntimeImgVersion=_ChSysSwRuntimeImgVersion_Object((1,3,6,1,4,1,6027,3,10,1,2,8,1,1),_ChSysSwRuntimeImgVersion_Type())
chSysSwRuntimeImgVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwRuntimeImgVersion.setStatus(_A)
_ChSysSwRuntimeImgDate_Type=F10SwDate
_ChSysSwRuntimeImgDate_Object=MibTableColumn
chSysSwRuntimeImgDate=_ChSysSwRuntimeImgDate_Object((1,3,6,1,4,1,6027,3,10,1,2,8,1,2),_ChSysSwRuntimeImgDate_Type())
chSysSwRuntimeImgDate.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwRuntimeImgDate.setStatus(_A)
_ChSysSwCurrentBootImgVersion_Type=DisplayString
_ChSysSwCurrentBootImgVersion_Object=MibTableColumn
chSysSwCurrentBootImgVersion=_ChSysSwCurrentBootImgVersion_Object((1,3,6,1,4,1,6027,3,10,1,2,8,1,3),_ChSysSwCurrentBootImgVersion_Type())
chSysSwCurrentBootImgVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwCurrentBootImgVersion.setStatus(_A)
_ChSysSwCurrentBootImgDate_Type=DateAndTime
_ChSysSwCurrentBootImgDate_Object=MibTableColumn
chSysSwCurrentBootImgDate=_ChSysSwCurrentBootImgDate_Object((1,3,6,1,4,1,6027,3,10,1,2,8,1,4),_ChSysSwCurrentBootImgDate_Type())
chSysSwCurrentBootImgDate.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwCurrentBootImgDate.setStatus(_A)
class _ChSysSwCurrentBootImgStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),(_k,2)))
_ChSysSwCurrentBootImgStatus_Type.__name__=_E
_ChSysSwCurrentBootImgStatus_Object=MibTableColumn
chSysSwCurrentBootImgStatus=_ChSysSwCurrentBootImgStatus_Object((1,3,6,1,4,1,6027,3,10,1,2,8,1,5),_ChSysSwCurrentBootImgStatus_Type())
chSysSwCurrentBootImgStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwCurrentBootImgStatus.setStatus(_A)
_ChSysSwBackupBootImgVersion_Type=DisplayString
_ChSysSwBackupBootImgVersion_Object=MibTableColumn
chSysSwBackupBootImgVersion=_ChSysSwBackupBootImgVersion_Object((1,3,6,1,4,1,6027,3,10,1,2,8,1,6),_ChSysSwBackupBootImgVersion_Type())
chSysSwBackupBootImgVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwBackupBootImgVersion.setStatus(_A)
_ChSysSwBackupBootImgDate_Type=DateAndTime
_ChSysSwBackupBootImgDate_Object=MibTableColumn
chSysSwBackupBootImgDate=_ChSysSwBackupBootImgDate_Object((1,3,6,1,4,1,6027,3,10,1,2,8,1,7),_ChSysSwBackupBootImgDate_Type())
chSysSwBackupBootImgDate.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwBackupBootImgDate.setStatus(_A)
class _ChSysSwBackupBootImgStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),(_k,2)))
_ChSysSwBackupBootImgStatus_Type.__name__=_E
_ChSysSwBackupBootImgStatus_Object=MibTableColumn
chSysSwBackupBootImgStatus=_ChSysSwBackupBootImgStatus_Object((1,3,6,1,4,1,6027,3,10,1,2,8,1,8),_ChSysSwBackupBootImgStatus_Type())
chSysSwBackupBootImgStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwBackupBootImgStatus.setStatus(_A)
class _ChSysSwNextRebootImage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_ChSysSwNextRebootImage_Type.__name__=_E
_ChSysSwNextRebootImage_Object=MibTableColumn
chSysSwNextRebootImage=_ChSysSwNextRebootImage_Object((1,3,6,1,4,1,6027,3,10,1,2,8,1,9),_ChSysSwNextRebootImage_Type())
chSysSwNextRebootImage.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwNextRebootImage.setStatus(_A)
class _ChSysSwCurrentBootImage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_ChSysSwCurrentBootImage_Type.__name__=_E
_ChSysSwCurrentBootImage_Object=MibTableColumn
chSysSwCurrentBootImage=_ChSysSwCurrentBootImage_Object((1,3,6,1,4,1,6027,3,10,1,2,8,1,10),_ChSysSwCurrentBootImage_Type())
chSysSwCurrentBootImage.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwCurrentBootImage.setStatus(_A)
_ChSysSwInPartitionAImgVers_Type=DisplayString
_ChSysSwInPartitionAImgVers_Object=MibTableColumn
chSysSwInPartitionAImgVers=_ChSysSwInPartitionAImgVers_Object((1,3,6,1,4,1,6027,3,10,1,2,8,1,11),_ChSysSwInPartitionAImgVers_Type())
chSysSwInPartitionAImgVers.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwInPartitionAImgVers.setStatus(_A)
_ChSysSwInPartitionBImgVers_Type=DisplayString
_ChSysSwInPartitionBImgVers_Object=MibTableColumn
chSysSwInPartitionBImgVers=_ChSysSwInPartitionBImgVers_Object((1,3,6,1,4,1,6027,3,10,1,2,8,1,12),_ChSysSwInPartitionBImgVers_Type())
chSysSwInPartitionBImgVers.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwInPartitionBImgVers.setStatus(_A)
_ChStackUnitUtilTable_Object=MibTable
chStackUnitUtilTable=_ChStackUnitUtilTable_Object((1,3,6,1,4,1,6027,3,10,1,2,9))
if mibBuilder.loadTexts:chStackUnitUtilTable.setStatus(_A)
_ChStackUnitUtilEntry_Object=MibTableRow
chStackUnitUtilEntry=_ChStackUnitUtilEntry_Object((1,3,6,1,4,1,6027,3,10,1,2,9,1))
chStackUnitUtilEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:chStackUnitUtilEntry.setStatus(_A)
_ChStackUnitCpuType_Type=F10ProcessorModuleType
_ChStackUnitCpuType_Object=MibTableColumn
chStackUnitCpuType=_ChStackUnitCpuType_Object((1,3,6,1,4,1,6027,3,10,1,2,9,1,1),_ChStackUnitCpuType_Type())
chStackUnitCpuType.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitCpuType.setStatus(_A)
class _ChStackUnitCpuUtil5Sec_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ChStackUnitCpuUtil5Sec_Type.__name__=_M
_ChStackUnitCpuUtil5Sec_Object=MibTableColumn
chStackUnitCpuUtil5Sec=_ChStackUnitCpuUtil5Sec_Object((1,3,6,1,4,1,6027,3,10,1,2,9,1,2),_ChStackUnitCpuUtil5Sec_Type())
chStackUnitCpuUtil5Sec.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitCpuUtil5Sec.setStatus(_A)
if mibBuilder.loadTexts:chStackUnitCpuUtil5Sec.setUnits(_Q)
class _ChStackUnitCpuUtil1Min_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ChStackUnitCpuUtil1Min_Type.__name__=_M
_ChStackUnitCpuUtil1Min_Object=MibTableColumn
chStackUnitCpuUtil1Min=_ChStackUnitCpuUtil1Min_Object((1,3,6,1,4,1,6027,3,10,1,2,9,1,3),_ChStackUnitCpuUtil1Min_Type())
chStackUnitCpuUtil1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitCpuUtil1Min.setStatus(_A)
if mibBuilder.loadTexts:chStackUnitCpuUtil1Min.setUnits(_Q)
class _ChStackUnitCpuUtil5Min_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ChStackUnitCpuUtil5Min_Type.__name__=_M
_ChStackUnitCpuUtil5Min_Object=MibTableColumn
chStackUnitCpuUtil5Min=_ChStackUnitCpuUtil5Min_Object((1,3,6,1,4,1,6027,3,10,1,2,9,1,4),_ChStackUnitCpuUtil5Min_Type())
chStackUnitCpuUtil5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitCpuUtil5Min.setStatus(_A)
if mibBuilder.loadTexts:chStackUnitCpuUtil5Min.setUnits(_Q)
class _ChStackUnitMemUsageUtil_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ChStackUnitMemUsageUtil_Type.__name__=_M
_ChStackUnitMemUsageUtil_Object=MibTableColumn
chStackUnitMemUsageUtil=_ChStackUnitMemUsageUtil_Object((1,3,6,1,4,1,6027,3,10,1,2,9,1,5),_ChStackUnitMemUsageUtil_Type())
chStackUnitMemUsageUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitMemUsageUtil.setStatus(_A)
if mibBuilder.loadTexts:chStackUnitMemUsageUtil.setUnits(_Q)
class _ChStackUnitFlashUsageUtil_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ChStackUnitFlashUsageUtil_Type.__name__=_M
_ChStackUnitFlashUsageUtil_Object=MibTableColumn
chStackUnitFlashUsageUtil=_ChStackUnitFlashUsageUtil_Object((1,3,6,1,4,1,6027,3,10,1,2,9,1,6),_ChStackUnitFlashUsageUtil_Type())
chStackUnitFlashUsageUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitFlashUsageUtil.setStatus(_A)
if mibBuilder.loadTexts:chStackUnitFlashUsageUtil.setUnits(_Q)
_ChSysSwCoresTable_Object=MibTable
chSysSwCoresTable=_ChSysSwCoresTable_Object((1,3,6,1,4,1,6027,3,10,1,2,10))
if mibBuilder.loadTexts:chSysSwCoresTable.setStatus(_A)
_ChSysCoresEntry_Object=MibTableRow
chSysCoresEntry=_ChSysCoresEntry_Object((1,3,6,1,4,1,6027,3,10,1,2,10,1))
chSysCoresEntry.setIndexNames((0,_B,_G),(0,_B,_Y))
if mibBuilder.loadTexts:chSysCoresEntry.setStatus(_A)
_ChSysCoresInstance_Type=Integer32
_ChSysCoresInstance_Object=MibTableColumn
chSysCoresInstance=_ChSysCoresInstance_Object((1,3,6,1,4,1,6027,3,10,1,2,10,1,1),_ChSysCoresInstance_Type())
chSysCoresInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCoresInstance.setStatus(_A)
_ChSysCoresFileName_Type=DisplayString
_ChSysCoresFileName_Object=MibTableColumn
chSysCoresFileName=_ChSysCoresFileName_Object((1,3,6,1,4,1,6027,3,10,1,2,10,1,2),_ChSysCoresFileName_Type())
chSysCoresFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCoresFileName.setStatus(_A)
_ChSysCoresTimeCreated_Type=F10SwDate
_ChSysCoresTimeCreated_Object=MibTableColumn
chSysCoresTimeCreated=_ChSysCoresTimeCreated_Object((1,3,6,1,4,1,6027,3,10,1,2,10,1,3),_ChSysCoresTimeCreated_Type())
chSysCoresTimeCreated.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCoresTimeCreated.setStatus(_A)
class _ChSysCoresStackUnitNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_ChSysCoresStackUnitNumber_Type.__name__=_E
_ChSysCoresStackUnitNumber_Object=MibTableColumn
chSysCoresStackUnitNumber=_ChSysCoresStackUnitNumber_Object((1,3,6,1,4,1,6027,3,10,1,2,10,1,4),_ChSysCoresStackUnitNumber_Type())
chSysCoresStackUnitNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCoresStackUnitNumber.setStatus(_A)
_ChSysCoresProcess_Type=DisplayString
_ChSysCoresProcess_Object=MibTableColumn
chSysCoresProcess=_ChSysCoresProcess_Object((1,3,6,1,4,1,6027,3,10,1,2,10,1,5),_ChSysCoresProcess_Type())
chSysCoresProcess.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCoresProcess.setStatus(_A)
_ChSysIfTable_Object=MibTable
chSysIfTable=_ChSysIfTable_Object((1,3,6,1,4,1,6027,3,10,1,2,11))
if mibBuilder.loadTexts:chSysIfTable.setStatus(_A)
_ChSysIfEntry_Object=MibTableRow
chSysIfEntry=_ChSysIfEntry_Object((1,3,6,1,4,1,6027,3,10,1,2,11,1))
chSysIfEntry.setIndexNames((0,_a,_b))
if mibBuilder.loadTexts:chSysIfEntry.setStatus(_A)
_ChSysIfType_Type=F10SSeriesPortType
_ChSysIfType_Object=MibTableColumn
chSysIfType=_ChSysIfType_Object((1,3,6,1,4,1,6027,3,10,1,2,11,1,1),_ChSysIfType_Type())
chSysIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysIfType.setStatus(_A)
_ChSysIfName_Type=DisplayString
_ChSysIfName_Object=MibTableColumn
chSysIfName=_ChSysIfName_Object((1,3,6,1,4,1,6027,3,10,1,2,11,1,2),_ChSysIfName_Type())
chSysIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysIfName.setStatus(_A)
class _ChSysIfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_ChSysIfAdminStatus_Type.__name__=_E
_ChSysIfAdminStatus_Object=MibTableColumn
chSysIfAdminStatus=_ChSysIfAdminStatus_Object((1,3,6,1,4,1,6027,3,10,1,2,11,1,3),_ChSysIfAdminStatus_Type())
chSysIfAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysIfAdminStatus.setStatus(_A)
class _ChSysIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ready',1),(_e,2),(_f,3),(_g,4),(_h,5),(_T,6)))
_ChSysIfOperStatus_Type.__name__=_E
_ChSysIfOperStatus_Object=MibTableColumn
chSysIfOperStatus=_ChSysIfOperStatus_Object((1,3,6,1,4,1,6027,3,10,1,2,11,1,4),_ChSysIfOperStatus_Type())
chSysIfOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysIfOperStatus.setStatus(_A)
_ChSysIfXfpRecvPower_Type=F10HundredthdB
_ChSysIfXfpRecvPower_Object=MibTableColumn
chSysIfXfpRecvPower=_ChSysIfXfpRecvPower_Object((1,3,6,1,4,1,6027,3,10,1,2,11,1,5),_ChSysIfXfpRecvPower_Type())
chSysIfXfpRecvPower.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysIfXfpRecvPower.setStatus(_A)
if mibBuilder.loadTexts:chSysIfXfpRecvPower.setUnits(_R)
_ChSysIfXfpRecvTemp_Type=Integer32
_ChSysIfXfpRecvTemp_Object=MibTableColumn
chSysIfXfpRecvTemp=_ChSysIfXfpRecvTemp_Object((1,3,6,1,4,1,6027,3,10,1,2,11,1,6),_ChSysIfXfpRecvTemp_Type())
chSysIfXfpRecvTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysIfXfpRecvTemp.setStatus(_A)
_ChSysIfXfpTxPower_Type=F10HundredthdB
_ChSysIfXfpTxPower_Object=MibTableColumn
chSysIfXfpTxPower=_ChSysIfXfpTxPower_Object((1,3,6,1,4,1,6027,3,10,1,2,11,1,7),_ChSysIfXfpTxPower_Type())
chSysIfXfpTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysIfXfpTxPower.setStatus(_A)
if mibBuilder.loadTexts:chSysIfXfpTxPower.setUnits(_R)
_ChAlarmObjects_ObjectIdentity=ObjectIdentity
chAlarmObjects=_ChAlarmObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,10,1,4))
_ChAlarmMibNotifications_ObjectIdentity=ObjectIdentity
chAlarmMibNotifications=_ChAlarmMibNotifications_ObjectIdentity((1,3,6,1,4,1,6027,3,10,1,4,0))
_F10sSeriesMibConformance_ObjectIdentity=ObjectIdentity
f10sSeriesMibConformance=_F10sSeriesMibConformance_ObjectIdentity((1,3,6,1,4,1,6027,3,10,2))
_F10sSeriesMibCompliances_ObjectIdentity=ObjectIdentity
f10sSeriesMibCompliances=_F10sSeriesMibCompliances_ObjectIdentity((1,3,6,1,4,1,6027,3,10,2,1))
_F10sSeriesMibGroups_ObjectIdentity=ObjectIdentity
f10sSeriesMibGroups=_F10sSeriesMibGroups_ObjectIdentity((1,3,6,1,4,1,6027,3,10,2,2))
f10sSeriesComponentGroup=ObjectGroup((1,3,6,1,4,1,6027,3,10,2,2,1))
f10sSeriesComponentGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:f10sSeriesComponentGroup.setStatus(_A)
f10sSeriesSystemGroup=ObjectGroup((1,3,6,1,4,1,6027,3,10,2,2,2))
f10sSeriesSystemGroup.setObjects(*((_B,_S),(_B,_q),(_B,_r),(_B,_s),(_B,_G),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_U),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_V),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_W),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_X),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2),(_B,_B3),(_B,_B4),(_B,_B5),(_B,_B6),(_B,_B7),(_B,_B8),(_B,_B9),(_B,_BA),(_B,_BB),(_B,_Y),(_B,_BC),(_B,_BD),(_B,_BE),(_B,_BF),(_B,_BG),(_B,_BH),(_B,_BI),(_B,_BJ),(_B,_BK),(_B,_BL),(_B,_BM)))
if mibBuilder.loadTexts:f10sSeriesSystemGroup.setStatus(_A)
chAlarmStackUnitDown=NotificationType((1,3,6,1,4,1,6027,3,10,1,4,0,1))
chAlarmStackUnitDown.setObjects(*((_D,_H),(_D,_K),(_D,_J),(_D,_I)))
if mibBuilder.loadTexts:chAlarmStackUnitDown.setStatus(_A)
chAlarmStackUnitUp=NotificationType((1,3,6,1,4,1,6027,3,10,1,4,0,2))
chAlarmStackUnitUp.setObjects(*((_D,_H),(_D,_K),(_D,_J),(_D,_I)))
if mibBuilder.loadTexts:chAlarmStackUnitUp.setStatus(_A)
chAlarmStackUnitReset=NotificationType((1,3,6,1,4,1,6027,3,10,1,4,0,3))
chAlarmStackUnitReset.setObjects(*((_D,_H),(_D,_K),(_D,_J),(_D,_I)))
if mibBuilder.loadTexts:chAlarmStackUnitReset.setStatus(_A)
chAlarmStackUnitOffline=NotificationType((1,3,6,1,4,1,6027,3,10,1,4,0,4))
chAlarmStackUnitOffline.setObjects(*((_D,_H),(_D,_K),(_D,_J),(_D,_I)))
if mibBuilder.loadTexts:chAlarmStackUnitOffline.setStatus(_A)
chAlarmStackUnitCodeMismatch=NotificationType((1,3,6,1,4,1,6027,3,10,1,4,0,5))
chAlarmStackUnitCodeMismatch.setObjects(*((_D,_H),(_D,_K),(_D,_J),(_D,_I)))
if mibBuilder.loadTexts:chAlarmStackUnitCodeMismatch.setStatus(_A)
chAlarmStackPortLinkUp=NotificationType((1,3,6,1,4,1,6027,3,10,1,4,0,6))
chAlarmStackPortLinkUp.setObjects(*((_D,_H),(_D,_K),(_D,_J),(_D,_I)))
if mibBuilder.loadTexts:chAlarmStackPortLinkUp.setStatus(_A)
chAlarmStackPortLinkDown=NotificationType((1,3,6,1,4,1,6027,3,10,1,4,0,7))
chAlarmStackPortLinkDown.setObjects(*((_D,_H),(_D,_K),(_D,_J),(_D,_I)))
if mibBuilder.loadTexts:chAlarmStackPortLinkDown.setStatus(_A)
f10sSeriesNotificationGroup=NotificationGroup((1,3,6,1,4,1,6027,3,10,2,2,3))
f10sSeriesNotificationGroup.setObjects(*((_B,_BN),(_B,_BO),(_B,_BP),(_B,_BQ),(_B,_BR),(_B,_BS),(_B,_BT)))
if mibBuilder.loadTexts:f10sSeriesNotificationGroup.setStatus(_A)
f10sSeriesMibCompliance=ModuleCompliance((1,3,6,1,4,1,6027,3,10,2,1,1))
f10sSeriesMibCompliance.setObjects(*((_B,_BU),(_B,_BV),(_B,_BW)))
if mibBuilder.loadTexts:f10sSeriesMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CodeType':CodeType,'UnitType':UnitType,'f10SSerChassisMib':f10SSerChassisMib,'f10SSerChassisObject':f10SSerChassisObject,'chObjects':chObjects,_n:chNumStackUnits,_o:chNumMaxStackableUnits,_p:chStackUnitIndexNext,'chSysObjects':chSysObjects,'chSwitchTypeTable':chSwitchTypeTable,'chSwitchTypeEntry':chSwitchTypeEntry,_S:chSwitchTypeSID,_q:chSwitchTypeModelID,_r:chSwitchTypeCodeType,_s:chSwitchTypeMgmtPreference,'chStackUnitTable':chStackUnitTable,'chStackUnitEntry':chStackUnitEntry,_c:chStackUnitIndex,_G:chStackUnitNumber,_t:chStackUnitSID,_u:chStackUnitMgmtStatus,_v:chStackUnitHwMgmtPreference,_w:chStackUnitAdmMgmtPreference,_x:chStackUnitModelID,_y:chStackUnitStatus,_z:chStackUnitDescription,_A0:chStackUnitCodeVersion,_A1:chStackUnitCodeVersionInFlash,_A2:chStackUnitSerialNumber,_A3:chStackUnitUpTime,_A4:chStackUnitTemp,_A5:chStackUnitType,_A6:chStackUnitSysType,_A7:chStackUnitVendorId,_A8:chStackUnitMfgDate,_A9:chStackUnitMacAddress,_AA:chStackUnitPartNum,_AB:chStackUnitProductRev,_AC:chStackUnitProductOrder,_AD:chStackUnitCountryCode,_AE:chStackUnitNum10GigEtherPorts,_AF:chStackUnitNumGigEtherPorts,_AG:chStackUnitNumFastEtherPorts,_AH:chStackUnitNumFanTrays,_AI:chStackUnitNumPowerSupplies,_AJ:chStackUnitNumPluggableModules,'chStackUnitNum40GigEtherPorts':chStackUnitNum40GigEtherPorts,_AK:chStackUnitRowStatus,_AL:chStackUnitPiecePartID,_AM:chStackUnitPPIDRevision,_AN:chStackUnitServiceTag,_AO:chStackUnitExpressServiceCode,'chSysPowerSupplyTable':chSysPowerSupplyTable,'chSysPowerSupplyEntry':chSysPowerSupplyEntry,_U:chSysPowerSupplyIndex,_AP:chSysPowerSupplyOperStatus,_AQ:chSysPowerSupplyType,_AR:chSysPowerSupplyPiecePartID,_AS:chSysPowerSupplyPPIDRevision,_AT:chSysPowerSupplyServiceTag,_AU:chSysPowerSupplyExpressServiceCode,'chSysFanTrayTable':chSysFanTrayTable,'chSysFanTrayEntry':chSysFanTrayEntry,_V:chSysFanTrayIndex,_AV:chSysFanTrayOperStatus,_AW:chSysFanTrayPiecePartID,_AX:chSysFanTrayPPIDRevision,_AY:chSysFanTrayServiceTag,_AZ:chSysFanTrayExpressServiceCode,'chSysPortTable':chSysPortTable,'chSysPortEntry':chSysPortEntry,_W:chSysPortIndex,_Aa:chSysPortType,_Ab:chSysPortAdminStatus,_Ac:chSysPortOperStatus,_Ad:chSysPortIfIndex,_Ae:chSysPortXfpRecvPower,_Af:chSysPortXfpRecvTemp,_Ag:chSysPortXfpTxPower,'chSysStackPortTable':chSysStackPortTable,'chSysStackPortEntry':chSysStackPortEntry,_X:chSysStackPortIndex,_Ah:chSysStackPortConfiguredMode,_Ai:chSysStackPortRunningMode,_Aj:chSysStackPortLinkStatus,_Ak:chSysStackPortLinkSpeed,_Al:chSysStackPortRxDataRate,_Am:chSysStackPortRxErrorRate,_An:chSysStackPortRxTotalErrors,_Ao:chSysStackPortTxDataRate,_Ap:chSysStackPortTxErrorRate,_Aq:chSysStackPortTxTotalErrors,'chSysProcessorTable':chSysProcessorTable,'chSysProcessorEntry':chSysProcessorEntry,_Ar:chSysProcessorModule,_As:chSysProcessorUpTime,_At:chSysProcessorNvramSize,_Au:chSysProcessorMemSize,'chSysSwModuleTable':chSysSwModuleTable,'chSysSwModuleEntry':chSysSwModuleEntry,_Av:chSysSwRuntimeImgVersion,_Aw:chSysSwRuntimeImgDate,_Ax:chSysSwCurrentBootImgVersion,_Ay:chSysSwCurrentBootImgDate,_Az:chSysSwCurrentBootImgStatus,_A_:chSysSwBackupBootImgVersion,_B0:chSysSwBackupBootImgDate,_B1:chSysSwBackupBootImgStatus,_B2:chSysSwNextRebootImage,_B3:chSysSwCurrentBootImage,_B4:chSysSwInPartitionAImgVers,_B5:chSysSwInPartitionBImgVers,'chStackUnitUtilTable':chStackUnitUtilTable,'chStackUnitUtilEntry':chStackUnitUtilEntry,_B6:chStackUnitCpuType,_B7:chStackUnitCpuUtil5Sec,_B8:chStackUnitCpuUtil1Min,_B9:chStackUnitCpuUtil5Min,_BA:chStackUnitMemUsageUtil,_BB:chStackUnitFlashUsageUtil,'chSysSwCoresTable':chSysSwCoresTable,'chSysCoresEntry':chSysCoresEntry,_Y:chSysCoresInstance,_BC:chSysCoresFileName,_BD:chSysCoresTimeCreated,_BE:chSysCoresStackUnitNumber,_BF:chSysCoresProcess,'chSysIfTable':chSysIfTable,'chSysIfEntry':chSysIfEntry,_BG:chSysIfType,_BH:chSysIfName,_BI:chSysIfAdminStatus,_BJ:chSysIfOperStatus,_BK:chSysIfXfpRecvPower,_BL:chSysIfXfpRecvTemp,_BM:chSysIfXfpTxPower,'chAlarmObjects':chAlarmObjects,'chAlarmMibNotifications':chAlarmMibNotifications,_BN:chAlarmStackUnitDown,_BO:chAlarmStackUnitUp,_BP:chAlarmStackUnitReset,_BQ:chAlarmStackUnitOffline,_BR:chAlarmStackUnitCodeMismatch,_BS:chAlarmStackPortLinkUp,_BT:chAlarmStackPortLinkDown,'f10sSeriesMibConformance':f10sSeriesMibConformance,'f10sSeriesMibCompliances':f10sSeriesMibCompliances,'f10sSeriesMibCompliance':f10sSeriesMibCompliance,'f10sSeriesMibGroups':f10sSeriesMibGroups,_BU:f10sSeriesComponentGroup,_BV:f10sSeriesSystemGroup,_BW:f10sSeriesNotificationGroup})