_B4='f10mSeriesNotificationGroup'
_B3='f10mSeriesSystemGroup'
_B2='f10mSeriesComponentGroup'
_B1='chAlarmStackUnitRoleChanged'
_B0='chAlarmStackPortLinkDown'
_A_='chAlarmStackPortLinkUp'
_Az='chAlarmStackUnitCodeMismatch'
_Ay='chAlarmStackUnitOffline'
_Ax='chAlarmStackUnitReset'
_Aw='chAlarmStackUnitUp'
_Av='chAlarmStackUnitDown'
_Au='chSysCoresProcess'
_At='chSysCoresStackUnitNumber'
_As='chSysCoresTimeCreated'
_Ar='chSysCoresFileName'
_Aq='chStackUnitFlashUsageUtil'
_Ap='chStackUnitMemUsageUtil'
_Ao='chStackUnitCpuUtil5Min'
_An='chStackUnitCpuUtil1Min'
_Am='chStackUnitCpuUtil5Sec'
_Al='chStackUnitCpuType'
_Ak='chSysSwInPartitionBImgVers'
_Aj='chSysSwInPartitionAImgVers'
_Ai='chSysSwCurrentBootImage'
_Ah='chSysSwNextRebootImage'
_Ag='chSysSwBackupBootImgStatus'
_Af='chSysSwBackupBootImgDate'
_Ae='chSysSwBackupBootImgVersion'
_Ad='chSysSwCurrentBootImgStatus'
_Ac='chSysSwCurrentBootImgDate'
_Ab='chSysSwCurrentBootImgVersion'
_Aa='chSysSwRuntimeImgDate'
_AZ='chSysSwRuntimeImgVersion'
_AY='chSysProcessorMemSize'
_AX='chSysProcessorNvramSize'
_AW='chSysProcessorUpTime'
_AV='chSysProcessorModule'
_AU='chSysStackPortTxTotalErrors'
_AT='chSysStackPortTxErrorRate'
_AS='chSysStackPortTxDataRate'
_AR='chSysStackPortRxTotalErrors'
_AQ='chSysStackPortRxErrorRate'
_AP='chSysStackPortRxDataRate'
_AO='chSysStackPortLinkSpeed'
_AN='chSysStackPortLinkStatus'
_AM='chSysStackPortRunningMode'
_AL='chSysStackPortConfiguredMode'
_AK='chSysPortXfpTxPower'
_AJ='chSysPortXfpRecvTemp'
_AI='chSysPortXfpRecvPower'
_AH='chSysPortIfIndex'
_AG='chSysPortOperStatus'
_AF='chSysPortAdminStatus'
_AE='chSysPortType'
_AD='chSysFanTrayOperStatus'
_AC='chSysPowerSupplyType'
_AB='chSysPowerSupplyOperStatus'
_AA='chStackUnitExpressServiceCode'
_A9='chStackUnitServiceTag'
_A8='chStackUnitPPIDRevision'
_A7='chStackUnitPiecePartID'
_A6='chStackUnitRowStatus'
_A5='chStackUnitNumPluggableModules'
_A4='chStackUnitNumPowerSupplies'
_A3='chStackUnitNumFanTrays'
_A2='chStackUnitNumFastEtherPorts'
_A1='chStackUnitNumGigEtherPorts'
_A0='chStackUnitNum10GigEtherPorts'
_z='chStackUnitCountryCode'
_y='chStackUnitProductOrder'
_x='chStackUnitProductRev'
_w='chStackUnitPartNum'
_v='chStackUnitMacAddress'
_u='chStackUnitMfgDate'
_t='chStackUnitVendorId'
_s='chStackUnitSysType'
_r='chStackUnitType'
_q='chStackUnitTemp'
_p='chStackUnitUpTime'
_o='chStackUnitSerialNumber'
_n='chStackUnitCodeVersionInFlash'
_m='chStackUnitCodeVersion'
_l='chStackUnitDescription'
_k='chStackUnitStatus'
_j='chStackUnitModelID'
_i='chStackUnitAdmMgmtPreference'
_h='chStackUnitHwMgmtPreference'
_g='chStackUnitSID'
_f='chStackUnitIndexNext'
_e='chNumMaxStackableUnits'
_d='chNumStackUnits'
_c='bootImage-B'
_b='bootImage-A'
_a='failed'
_Z='ethernet'
_Y='chStackUnitIndex'
_X='OctetString'
_W='chStackUnitMgmtStatus'
_V='chSysCoresInstance'
_U='chSysStackPortIndex'
_T='chSysPortIndex'
_S='down'
_R='chSysFanTrayIndex'
_Q='unknown'
_P='chSysPowerSupplyIndex'
_O='notPresent'
_N='percent'
_M='DisplayString'
_L='read-create'
_K='Gauge32'
_J='chAlarmVarSlot'
_I='chAlarmVarPort'
_H='chAlarmVarInteger'
_G='chAlarmVarString'
_F='chStackUnitNumber'
_E='Integer32'
_D='F10-CHASSIS-MIB'
_C='read-only'
_B='F10-M-SERIES-CHASSIS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_X,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
chAlarmVarInteger,chAlarmVarPort,chAlarmVarSlot,chAlarmVarString=mibBuilder.importSymbols(_D,_H,_I,_J,_G)
f10Mgmt,=mibBuilder.importSymbols('FORCE10-SMI','f10Mgmt')
F10ChassisType,F10HundredthdB,F10MSeriesPortType,F10MfgDate,F10ProcessorModuleType,F10SwDate=mibBuilder.importSymbols('FORCE10-TC','F10ChassisType','F10HundredthdB','F10MSeriesPortType','F10MfgDate','F10ProcessorModuleType','F10SwDate')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_K,_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_M,'MacAddress','PhysAddress','RowStatus','TextualConvention')
f10MSerChassisMib=ModuleIdentity((1,3,6,1,4,1,6027,3,19))
if mibBuilder.loadTexts:f10MSerChassisMib.setRevisions(('2012-11-02 12:00','2012-12-03 12:00','2012-03-27 12:00','2007-10-03 12:00'))
class CodeType(TextualConvention,Unsigned32):status=_A;displayHint='x'
class UnitType(TextualConvention,Unsigned32):status=_A;displayHint='x'
_F10MSerChassisObject_ObjectIdentity=ObjectIdentity
f10MSerChassisObject=_F10MSerChassisObject_ObjectIdentity((1,3,6,1,4,1,6027,3,19,1))
_ChObjects_ObjectIdentity=ObjectIdentity
chObjects=_ChObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,19,1,1))
_ChNumStackUnits_Type=Integer32
_ChNumStackUnits_Object=MibScalar
chNumStackUnits=_ChNumStackUnits_Object((1,3,6,1,4,1,6027,3,19,1,1,1),_ChNumStackUnits_Type())
chNumStackUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:chNumStackUnits.setStatus(_A)
_ChNumMaxStackableUnits_Type=Integer32
_ChNumMaxStackableUnits_Object=MibScalar
chNumMaxStackableUnits=_ChNumMaxStackableUnits_Object((1,3,6,1,4,1,6027,3,19,1,1,2),_ChNumMaxStackableUnits_Type())
chNumMaxStackableUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:chNumMaxStackableUnits.setStatus(_A)
class _ChStackUnitIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,6))
_ChStackUnitIndexNext_Type.__name__=_E
_ChStackUnitIndexNext_Object=MibScalar
chStackUnitIndexNext=_ChStackUnitIndexNext_Object((1,3,6,1,4,1,6027,3,19,1,1,3),_ChStackUnitIndexNext_Type())
chStackUnitIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitIndexNext.setStatus(_A)
_ChSysObjects_ObjectIdentity=ObjectIdentity
chSysObjects=_ChSysObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,19,1,2))
_ChStackUnitTable_Object=MibTable
chStackUnitTable=_ChStackUnitTable_Object((1,3,6,1,4,1,6027,3,19,1,2,1))
if mibBuilder.loadTexts:chStackUnitTable.setStatus(_A)
_ChStackUnitEntry_Object=MibTableRow
chStackUnitEntry=_ChStackUnitEntry_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1))
chStackUnitEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:chStackUnitEntry.setStatus(_A)
_ChStackUnitIndex_Type=Integer32
_ChStackUnitIndex_Object=MibTableColumn
chStackUnitIndex=_ChStackUnitIndex_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,1),_ChStackUnitIndex_Type())
chStackUnitIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:chStackUnitIndex.setStatus(_A)
class _ChStackUnitNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,6))
_ChStackUnitNumber_Type.__name__=_E
_ChStackUnitNumber_Object=MibTableColumn
chStackUnitNumber=_ChStackUnitNumber_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,2),_ChStackUnitNumber_Type())
chStackUnitNumber.setMaxAccess(_L)
if mibBuilder.loadTexts:chStackUnitNumber.setStatus(_A)
_ChStackUnitSID_Type=Integer32
_ChStackUnitSID_Object=MibTableColumn
chStackUnitSID=_ChStackUnitSID_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,3),_ChStackUnitSID_Type())
chStackUnitSID.setMaxAccess(_L)
if mibBuilder.loadTexts:chStackUnitSID.setStatus('deprecated')
class _ChStackUnitMgmtStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('mgmtUnit',1),('standbyUnit',2),('stackUnit',3),('unassigned',4)))
_ChStackUnitMgmtStatus_Type.__name__=_E
_ChStackUnitMgmtStatus_Object=MibTableColumn
chStackUnitMgmtStatus=_ChStackUnitMgmtStatus_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,4),_ChStackUnitMgmtStatus_Type())
chStackUnitMgmtStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:chStackUnitMgmtStatus.setStatus(_A)
class _ChStackUnitHwMgmtPreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disabled',0),('unsassigned',1),('assigned',2)))
_ChStackUnitHwMgmtPreference_Type.__name__=_E
_ChStackUnitHwMgmtPreference_Object=MibTableColumn
chStackUnitHwMgmtPreference=_ChStackUnitHwMgmtPreference_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,5),_ChStackUnitHwMgmtPreference_Type())
chStackUnitHwMgmtPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitHwMgmtPreference.setStatus(_A)
class _ChStackUnitAdmMgmtPreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,15))
_ChStackUnitAdmMgmtPreference_Type.__name__=_E
_ChStackUnitAdmMgmtPreference_Object=MibTableColumn
chStackUnitAdmMgmtPreference=_ChStackUnitAdmMgmtPreference_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,6),_ChStackUnitAdmMgmtPreference_Type())
chStackUnitAdmMgmtPreference.setMaxAccess(_L)
if mibBuilder.loadTexts:chStackUnitAdmMgmtPreference.setStatus(_A)
_ChStackUnitModelID_Type=DisplayString
_ChStackUnitModelID_Object=MibTableColumn
chStackUnitModelID=_ChStackUnitModelID_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,7),_ChStackUnitModelID_Type())
chStackUnitModelID.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitModelID.setStatus(_A)
class _ChStackUnitStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ok',1),('unsupported',2),('codeMismatch',3),('configMismatch',4),('unitDown',5),(_O,6)))
_ChStackUnitStatus_Type.__name__=_E
_ChStackUnitStatus_Object=MibTableColumn
chStackUnitStatus=_ChStackUnitStatus_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,8),_ChStackUnitStatus_Type())
chStackUnitStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitStatus.setStatus(_A)
_ChStackUnitDescription_Type=DisplayString
_ChStackUnitDescription_Object=MibTableColumn
chStackUnitDescription=_ChStackUnitDescription_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,9),_ChStackUnitDescription_Type())
chStackUnitDescription.setMaxAccess(_L)
if mibBuilder.loadTexts:chStackUnitDescription.setStatus(_A)
_ChStackUnitCodeVersion_Type=DisplayString
_ChStackUnitCodeVersion_Object=MibTableColumn
chStackUnitCodeVersion=_ChStackUnitCodeVersion_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,10),_ChStackUnitCodeVersion_Type())
chStackUnitCodeVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitCodeVersion.setStatus(_A)
_ChStackUnitCodeVersionInFlash_Type=DisplayString
_ChStackUnitCodeVersionInFlash_Object=MibTableColumn
chStackUnitCodeVersionInFlash=_ChStackUnitCodeVersionInFlash_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,11),_ChStackUnitCodeVersionInFlash_Type())
chStackUnitCodeVersionInFlash.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitCodeVersionInFlash.setStatus(_A)
_ChStackUnitSerialNumber_Type=DisplayString
_ChStackUnitSerialNumber_Object=MibTableColumn
chStackUnitSerialNumber=_ChStackUnitSerialNumber_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,12),_ChStackUnitSerialNumber_Type())
chStackUnitSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitSerialNumber.setStatus(_A)
_ChStackUnitUpTime_Type=TimeTicks
_ChStackUnitUpTime_Object=MibTableColumn
chStackUnitUpTime=_ChStackUnitUpTime_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,13),_ChStackUnitUpTime_Type())
chStackUnitUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitUpTime.setStatus(_A)
_ChStackUnitTemp_Type=Gauge32
_ChStackUnitTemp_Object=MibTableColumn
chStackUnitTemp=_ChStackUnitTemp_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,14),_ChStackUnitTemp_Type())
chStackUnitTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitTemp.setStatus(_A)
_ChStackUnitType_Type=UnitType
_ChStackUnitType_Object=MibTableColumn
chStackUnitType=_ChStackUnitType_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,15),_ChStackUnitType_Type())
chStackUnitType.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitType.setStatus(_A)
_ChStackUnitSysType_Type=F10ChassisType
_ChStackUnitSysType_Object=MibTableColumn
chStackUnitSysType=_ChStackUnitSysType_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,16),_ChStackUnitSysType_Type())
chStackUnitSysType.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitSysType.setStatus(_A)
_ChStackUnitVendorId_Type=DisplayString
_ChStackUnitVendorId_Object=MibTableColumn
chStackUnitVendorId=_ChStackUnitVendorId_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,17),_ChStackUnitVendorId_Type())
chStackUnitVendorId.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitVendorId.setStatus(_A)
_ChStackUnitMfgDate_Type=F10MfgDate
_ChStackUnitMfgDate_Object=MibTableColumn
chStackUnitMfgDate=_ChStackUnitMfgDate_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,18),_ChStackUnitMfgDate_Type())
chStackUnitMfgDate.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitMfgDate.setStatus(_A)
_ChStackUnitMacAddress_Type=MacAddress
_ChStackUnitMacAddress_Object=MibTableColumn
chStackUnitMacAddress=_ChStackUnitMacAddress_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,19),_ChStackUnitMacAddress_Type())
chStackUnitMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitMacAddress.setStatus(_A)
_ChStackUnitPartNum_Type=DisplayString
_ChStackUnitPartNum_Object=MibTableColumn
chStackUnitPartNum=_ChStackUnitPartNum_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,20),_ChStackUnitPartNum_Type())
chStackUnitPartNum.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitPartNum.setStatus(_A)
_ChStackUnitProductRev_Type=DisplayString
_ChStackUnitProductRev_Object=MibTableColumn
chStackUnitProductRev=_ChStackUnitProductRev_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,21),_ChStackUnitProductRev_Type())
chStackUnitProductRev.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitProductRev.setStatus(_A)
_ChStackUnitProductOrder_Type=DisplayString
_ChStackUnitProductOrder_Object=MibTableColumn
chStackUnitProductOrder=_ChStackUnitProductOrder_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,22),_ChStackUnitProductOrder_Type())
chStackUnitProductOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitProductOrder.setStatus(_A)
class _ChStackUnitCountryCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_ChStackUnitCountryCode_Type.__name__=_X
_ChStackUnitCountryCode_Object=MibTableColumn
chStackUnitCountryCode=_ChStackUnitCountryCode_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,23),_ChStackUnitCountryCode_Type())
chStackUnitCountryCode.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitCountryCode.setStatus(_A)
_ChStackUnitNum10GigEtherPorts_Type=Integer32
_ChStackUnitNum10GigEtherPorts_Object=MibTableColumn
chStackUnitNum10GigEtherPorts=_ChStackUnitNum10GigEtherPorts_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,24),_ChStackUnitNum10GigEtherPorts_Type())
chStackUnitNum10GigEtherPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitNum10GigEtherPorts.setStatus(_A)
_ChStackUnitNumGigEtherPorts_Type=Integer32
_ChStackUnitNumGigEtherPorts_Object=MibTableColumn
chStackUnitNumGigEtherPorts=_ChStackUnitNumGigEtherPorts_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,25),_ChStackUnitNumGigEtherPorts_Type())
chStackUnitNumGigEtherPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitNumGigEtherPorts.setStatus(_A)
_ChStackUnitNumFastEtherPorts_Type=Integer32
_ChStackUnitNumFastEtherPorts_Object=MibTableColumn
chStackUnitNumFastEtherPorts=_ChStackUnitNumFastEtherPorts_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,26),_ChStackUnitNumFastEtherPorts_Type())
chStackUnitNumFastEtherPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitNumFastEtherPorts.setStatus(_A)
_ChStackUnitNumFanTrays_Type=Integer32
_ChStackUnitNumFanTrays_Object=MibTableColumn
chStackUnitNumFanTrays=_ChStackUnitNumFanTrays_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,27),_ChStackUnitNumFanTrays_Type())
chStackUnitNumFanTrays.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitNumFanTrays.setStatus(_A)
_ChStackUnitNumPowerSupplies_Type=Integer32
_ChStackUnitNumPowerSupplies_Object=MibTableColumn
chStackUnitNumPowerSupplies=_ChStackUnitNumPowerSupplies_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,28),_ChStackUnitNumPowerSupplies_Type())
chStackUnitNumPowerSupplies.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitNumPowerSupplies.setStatus(_A)
_ChStackUnitNumPluggableModules_Type=Integer32
_ChStackUnitNumPluggableModules_Object=MibTableColumn
chStackUnitNumPluggableModules=_ChStackUnitNumPluggableModules_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,29),_ChStackUnitNumPluggableModules_Type())
chStackUnitNumPluggableModules.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitNumPluggableModules.setStatus(_A)
_ChStackUnitNum40GigEtherPorts_Type=Integer32
_ChStackUnitNum40GigEtherPorts_Object=MibTableColumn
chStackUnitNum40GigEtherPorts=_ChStackUnitNum40GigEtherPorts_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,30),_ChStackUnitNum40GigEtherPorts_Type())
chStackUnitNum40GigEtherPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitNum40GigEtherPorts.setStatus(_A)
_ChStackUnitRowStatus_Type=RowStatus
_ChStackUnitRowStatus_Object=MibTableColumn
chStackUnitRowStatus=_ChStackUnitRowStatus_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,31),_ChStackUnitRowStatus_Type())
chStackUnitRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:chStackUnitRowStatus.setStatus(_A)
class _ChStackUnitPiecePartID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_ChStackUnitPiecePartID_Type.__name__=_M
_ChStackUnitPiecePartID_Object=MibTableColumn
chStackUnitPiecePartID=_ChStackUnitPiecePartID_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,32),_ChStackUnitPiecePartID_Type())
chStackUnitPiecePartID.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitPiecePartID.setStatus(_A)
class _ChStackUnitPPIDRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_ChStackUnitPPIDRevision_Type.__name__=_M
_ChStackUnitPPIDRevision_Object=MibTableColumn
chStackUnitPPIDRevision=_ChStackUnitPPIDRevision_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,33),_ChStackUnitPPIDRevision_Type())
chStackUnitPPIDRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitPPIDRevision.setStatus(_A)
class _ChStackUnitServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_ChStackUnitServiceTag_Type.__name__=_M
_ChStackUnitServiceTag_Object=MibTableColumn
chStackUnitServiceTag=_ChStackUnitServiceTag_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,34),_ChStackUnitServiceTag_Type())
chStackUnitServiceTag.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitServiceTag.setStatus(_A)
class _ChStackUnitExpressServiceCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_ChStackUnitExpressServiceCode_Type.__name__=_M
_ChStackUnitExpressServiceCode_Object=MibTableColumn
chStackUnitExpressServiceCode=_ChStackUnitExpressServiceCode_Object((1,3,6,1,4,1,6027,3,19,1,2,1,1,35),_ChStackUnitExpressServiceCode_Type())
chStackUnitExpressServiceCode.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitExpressServiceCode.setStatus(_A)
_ChSysPowerSupplyTable_Object=MibTable
chSysPowerSupplyTable=_ChSysPowerSupplyTable_Object((1,3,6,1,4,1,6027,3,19,1,2,2))
if mibBuilder.loadTexts:chSysPowerSupplyTable.setStatus(_A)
_ChSysPowerSupplyEntry_Object=MibTableRow
chSysPowerSupplyEntry=_ChSysPowerSupplyEntry_Object((1,3,6,1,4,1,6027,3,19,1,2,2,1))
chSysPowerSupplyEntry.setIndexNames((0,_B,_F),(0,_B,_P))
if mibBuilder.loadTexts:chSysPowerSupplyEntry.setStatus(_A)
_ChSysPowerSupplyIndex_Type=Integer32
_ChSysPowerSupplyIndex_Object=MibTableColumn
chSysPowerSupplyIndex=_ChSysPowerSupplyIndex_Object((1,3,6,1,4,1,6027,3,19,1,2,2,1,1),_ChSysPowerSupplyIndex_Type())
chSysPowerSupplyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPowerSupplyIndex.setStatus(_A)
class _ChSysPowerSupplyOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('normal',1),('warning',2),('critical',3),('shutdown',4),(_O,5),('notFunctioning',6)))
_ChSysPowerSupplyOperStatus_Type.__name__=_E
_ChSysPowerSupplyOperStatus_Object=MibTableColumn
chSysPowerSupplyOperStatus=_ChSysPowerSupplyOperStatus_Object((1,3,6,1,4,1,6027,3,19,1,2,2,1,2),_ChSysPowerSupplyOperStatus_Type())
chSysPowerSupplyOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPowerSupplyOperStatus.setStatus(_A)
class _ChSysPowerSupplyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Q,1),('ac',2),('dc',3),('externalPowerSupply',4),('internalRedundant',5)))
_ChSysPowerSupplyType_Type.__name__=_E
_ChSysPowerSupplyType_Object=MibTableColumn
chSysPowerSupplyType=_ChSysPowerSupplyType_Object((1,3,6,1,4,1,6027,3,19,1,2,2,1,3),_ChSysPowerSupplyType_Type())
chSysPowerSupplyType.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPowerSupplyType.setStatus(_A)
_ChSysFanTrayTable_Object=MibTable
chSysFanTrayTable=_ChSysFanTrayTable_Object((1,3,6,1,4,1,6027,3,19,1,2,3))
if mibBuilder.loadTexts:chSysFanTrayTable.setStatus(_A)
_ChSysFanTrayEntry_Object=MibTableRow
chSysFanTrayEntry=_ChSysFanTrayEntry_Object((1,3,6,1,4,1,6027,3,19,1,2,3,1))
chSysFanTrayEntry.setIndexNames((0,_B,_F),(0,_B,_R))
if mibBuilder.loadTexts:chSysFanTrayEntry.setStatus(_A)
_ChSysFanTrayIndex_Type=Integer32
_ChSysFanTrayIndex_Object=MibTableColumn
chSysFanTrayIndex=_ChSysFanTrayIndex_Object((1,3,6,1,4,1,6027,3,19,1,2,3,1,1),_ChSysFanTrayIndex_Type())
chSysFanTrayIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysFanTrayIndex.setStatus(_A)
class _ChSysFanTrayOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_S,2)))
_ChSysFanTrayOperStatus_Type.__name__=_E
_ChSysFanTrayOperStatus_Object=MibTableColumn
chSysFanTrayOperStatus=_ChSysFanTrayOperStatus_Object((1,3,6,1,4,1,6027,3,19,1,2,3,1,2),_ChSysFanTrayOperStatus_Type())
chSysFanTrayOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysFanTrayOperStatus.setStatus(_A)
_ChSysPortTable_Object=MibTable
chSysPortTable=_ChSysPortTable_Object((1,3,6,1,4,1,6027,3,19,1,2,4))
if mibBuilder.loadTexts:chSysPortTable.setStatus(_A)
_ChSysPortEntry_Object=MibTableRow
chSysPortEntry=_ChSysPortEntry_Object((1,3,6,1,4,1,6027,3,19,1,2,4,1))
chSysPortEntry.setIndexNames((0,_B,_F),(0,_B,_T))
if mibBuilder.loadTexts:chSysPortEntry.setStatus(_A)
_ChSysPortIndex_Type=Integer32
_ChSysPortIndex_Object=MibTableColumn
chSysPortIndex=_ChSysPortIndex_Object((1,3,6,1,4,1,6027,3,19,1,2,4,1,1),_ChSysPortIndex_Type())
chSysPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPortIndex.setStatus(_A)
_ChSysPortType_Type=F10MSeriesPortType
_ChSysPortType_Object=MibTableColumn
chSysPortType=_ChSysPortType_Object((1,3,6,1,4,1,6027,3,19,1,2,4,1,2),_ChSysPortType_Type())
chSysPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPortType.setStatus(_A)
class _ChSysPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_S,2)))
_ChSysPortAdminStatus_Type.__name__=_E
_ChSysPortAdminStatus_Object=MibTableColumn
chSysPortAdminStatus=_ChSysPortAdminStatus_Object((1,3,6,1,4,1,6027,3,19,1,2,4,1,3),_ChSysPortAdminStatus_Type())
chSysPortAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPortAdminStatus.setStatus(_A)
class _ChSysPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ready',1),('portDown',2),('portProblem',3),('cardProblem',4),('cardDown',5),(_O,6)))
_ChSysPortOperStatus_Type.__name__=_E
_ChSysPortOperStatus_Object=MibTableColumn
chSysPortOperStatus=_ChSysPortOperStatus_Object((1,3,6,1,4,1,6027,3,19,1,2,4,1,4),_ChSysPortOperStatus_Type())
chSysPortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPortOperStatus.setStatus(_A)
_ChSysPortIfIndex_Type=Integer32
_ChSysPortIfIndex_Object=MibTableColumn
chSysPortIfIndex=_ChSysPortIfIndex_Object((1,3,6,1,4,1,6027,3,19,1,2,4,1,5),_ChSysPortIfIndex_Type())
chSysPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPortIfIndex.setStatus(_A)
_ChSysPortXfpRecvPower_Type=F10HundredthdB
_ChSysPortXfpRecvPower_Object=MibTableColumn
chSysPortXfpRecvPower=_ChSysPortXfpRecvPower_Object((1,3,6,1,4,1,6027,3,19,1,2,4,1,6),_ChSysPortXfpRecvPower_Type())
chSysPortXfpRecvPower.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPortXfpRecvPower.setStatus(_A)
if mibBuilder.loadTexts:chSysPortXfpRecvPower.setUnits('dB')
_ChSysPortXfpRecvTemp_Type=Integer32
_ChSysPortXfpRecvTemp_Object=MibTableColumn
chSysPortXfpRecvTemp=_ChSysPortXfpRecvTemp_Object((1,3,6,1,4,1,6027,3,19,1,2,4,1,7),_ChSysPortXfpRecvTemp_Type())
chSysPortXfpRecvTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPortXfpRecvTemp.setStatus(_A)
_ChSysPortXfpTxPower_Type=F10HundredthdB
_ChSysPortXfpTxPower_Object=MibTableColumn
chSysPortXfpTxPower=_ChSysPortXfpTxPower_Object((1,3,6,1,4,1,6027,3,19,1,2,4,1,8),_ChSysPortXfpTxPower_Type())
chSysPortXfpTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysPortXfpTxPower.setStatus(_A)
if mibBuilder.loadTexts:chSysPortXfpTxPower.setUnits('dB')
_ChSysStackPortTable_Object=MibTable
chSysStackPortTable=_ChSysStackPortTable_Object((1,3,6,1,4,1,6027,3,19,1,2,5))
if mibBuilder.loadTexts:chSysStackPortTable.setStatus(_A)
_ChSysStackPortEntry_Object=MibTableRow
chSysStackPortEntry=_ChSysStackPortEntry_Object((1,3,6,1,4,1,6027,3,19,1,2,5,1))
chSysStackPortEntry.setIndexNames((0,_B,_F),(0,_B,_U))
if mibBuilder.loadTexts:chSysStackPortEntry.setStatus(_A)
_ChSysStackPortIndex_Type=Integer32
_ChSysStackPortIndex_Object=MibTableColumn
chSysStackPortIndex=_ChSysStackPortIndex_Object((1,3,6,1,4,1,6027,3,19,1,2,5,1,1),_ChSysStackPortIndex_Type())
chSysStackPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysStackPortIndex.setStatus(_A)
class _ChSysStackPortConfiguredMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stack',1),(_Z,2),(_Q,3)))
_ChSysStackPortConfiguredMode_Type.__name__=_E
_ChSysStackPortConfiguredMode_Object=MibTableColumn
chSysStackPortConfiguredMode=_ChSysStackPortConfiguredMode_Object((1,3,6,1,4,1,6027,3,19,1,2,5,1,2),_ChSysStackPortConfiguredMode_Type())
chSysStackPortConfiguredMode.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysStackPortConfiguredMode.setStatus(_A)
class _ChSysStackPortRunningMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stack',1),(_Z,2),(_Q,3)))
_ChSysStackPortRunningMode_Type.__name__=_E
_ChSysStackPortRunningMode_Object=MibTableColumn
chSysStackPortRunningMode=_ChSysStackPortRunningMode_Object((1,3,6,1,4,1,6027,3,19,1,2,5,1,3),_ChSysStackPortRunningMode_Type())
chSysStackPortRunningMode.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysStackPortRunningMode.setStatus(_A)
class _ChSysStackPortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_S,2)))
_ChSysStackPortLinkStatus_Type.__name__=_E
_ChSysStackPortLinkStatus_Object=MibTableColumn
chSysStackPortLinkStatus=_ChSysStackPortLinkStatus_Object((1,3,6,1,4,1,6027,3,19,1,2,5,1,4),_ChSysStackPortLinkStatus_Type())
chSysStackPortLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysStackPortLinkStatus.setStatus(_A)
_ChSysStackPortLinkSpeed_Type=Gauge32
_ChSysStackPortLinkSpeed_Object=MibTableColumn
chSysStackPortLinkSpeed=_ChSysStackPortLinkSpeed_Object((1,3,6,1,4,1,6027,3,19,1,2,5,1,5),_ChSysStackPortLinkSpeed_Type())
chSysStackPortLinkSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysStackPortLinkSpeed.setStatus(_A)
_ChSysStackPortRxDataRate_Type=Counter32
_ChSysStackPortRxDataRate_Object=MibTableColumn
chSysStackPortRxDataRate=_ChSysStackPortRxDataRate_Object((1,3,6,1,4,1,6027,3,19,1,2,5,1,6),_ChSysStackPortRxDataRate_Type())
chSysStackPortRxDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysStackPortRxDataRate.setStatus(_A)
_ChSysStackPortRxErrorRate_Type=Counter32
_ChSysStackPortRxErrorRate_Object=MibTableColumn
chSysStackPortRxErrorRate=_ChSysStackPortRxErrorRate_Object((1,3,6,1,4,1,6027,3,19,1,2,5,1,7),_ChSysStackPortRxErrorRate_Type())
chSysStackPortRxErrorRate.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysStackPortRxErrorRate.setStatus(_A)
_ChSysStackPortRxTotalErrors_Type=Counter32
_ChSysStackPortRxTotalErrors_Object=MibTableColumn
chSysStackPortRxTotalErrors=_ChSysStackPortRxTotalErrors_Object((1,3,6,1,4,1,6027,3,19,1,2,5,1,8),_ChSysStackPortRxTotalErrors_Type())
chSysStackPortRxTotalErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysStackPortRxTotalErrors.setStatus(_A)
_ChSysStackPortTxDataRate_Type=Counter32
_ChSysStackPortTxDataRate_Object=MibTableColumn
chSysStackPortTxDataRate=_ChSysStackPortTxDataRate_Object((1,3,6,1,4,1,6027,3,19,1,2,5,1,9),_ChSysStackPortTxDataRate_Type())
chSysStackPortTxDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysStackPortTxDataRate.setStatus(_A)
_ChSysStackPortTxErrorRate_Type=Counter32
_ChSysStackPortTxErrorRate_Object=MibTableColumn
chSysStackPortTxErrorRate=_ChSysStackPortTxErrorRate_Object((1,3,6,1,4,1,6027,3,19,1,2,5,1,10),_ChSysStackPortTxErrorRate_Type())
chSysStackPortTxErrorRate.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysStackPortTxErrorRate.setStatus(_A)
_ChSysStackPortTxTotalErrors_Type=Counter32
_ChSysStackPortTxTotalErrors_Object=MibTableColumn
chSysStackPortTxTotalErrors=_ChSysStackPortTxTotalErrors_Object((1,3,6,1,4,1,6027,3,19,1,2,5,1,11),_ChSysStackPortTxTotalErrors_Type())
chSysStackPortTxTotalErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysStackPortTxTotalErrors.setStatus(_A)
_ChSysProcessorTable_Object=MibTable
chSysProcessorTable=_ChSysProcessorTable_Object((1,3,6,1,4,1,6027,3,19,1,2,6))
if mibBuilder.loadTexts:chSysProcessorTable.setStatus(_A)
_ChSysProcessorEntry_Object=MibTableRow
chSysProcessorEntry=_ChSysProcessorEntry_Object((1,3,6,1,4,1,6027,3,19,1,2,6,1))
chSysProcessorEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:chSysProcessorEntry.setStatus(_A)
_ChSysProcessorModule_Type=F10ProcessorModuleType
_ChSysProcessorModule_Object=MibTableColumn
chSysProcessorModule=_ChSysProcessorModule_Object((1,3,6,1,4,1,6027,3,19,1,2,6,1,1),_ChSysProcessorModule_Type())
chSysProcessorModule.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysProcessorModule.setStatus(_A)
_ChSysProcessorUpTime_Type=TimeTicks
_ChSysProcessorUpTime_Object=MibTableColumn
chSysProcessorUpTime=_ChSysProcessorUpTime_Object((1,3,6,1,4,1,6027,3,19,1,2,6,1,2),_ChSysProcessorUpTime_Type())
chSysProcessorUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysProcessorUpTime.setStatus(_A)
_ChSysProcessorNvramSize_Type=Integer32
_ChSysProcessorNvramSize_Object=MibTableColumn
chSysProcessorNvramSize=_ChSysProcessorNvramSize_Object((1,3,6,1,4,1,6027,3,19,1,2,6,1,3),_ChSysProcessorNvramSize_Type())
chSysProcessorNvramSize.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysProcessorNvramSize.setStatus(_A)
_ChSysProcessorMemSize_Type=Integer32
_ChSysProcessorMemSize_Object=MibTableColumn
chSysProcessorMemSize=_ChSysProcessorMemSize_Object((1,3,6,1,4,1,6027,3,19,1,2,6,1,4),_ChSysProcessorMemSize_Type())
chSysProcessorMemSize.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysProcessorMemSize.setStatus(_A)
_ChSysSwModuleTable_Object=MibTable
chSysSwModuleTable=_ChSysSwModuleTable_Object((1,3,6,1,4,1,6027,3,19,1,2,7))
if mibBuilder.loadTexts:chSysSwModuleTable.setStatus(_A)
_ChSysSwModuleEntry_Object=MibTableRow
chSysSwModuleEntry=_ChSysSwModuleEntry_Object((1,3,6,1,4,1,6027,3,19,1,2,7,1))
chSysSwModuleEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:chSysSwModuleEntry.setStatus(_A)
_ChSysSwRuntimeImgVersion_Type=DisplayString
_ChSysSwRuntimeImgVersion_Object=MibTableColumn
chSysSwRuntimeImgVersion=_ChSysSwRuntimeImgVersion_Object((1,3,6,1,4,1,6027,3,19,1,2,7,1,1),_ChSysSwRuntimeImgVersion_Type())
chSysSwRuntimeImgVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwRuntimeImgVersion.setStatus(_A)
_ChSysSwRuntimeImgDate_Type=F10SwDate
_ChSysSwRuntimeImgDate_Object=MibTableColumn
chSysSwRuntimeImgDate=_ChSysSwRuntimeImgDate_Object((1,3,6,1,4,1,6027,3,19,1,2,7,1,2),_ChSysSwRuntimeImgDate_Type())
chSysSwRuntimeImgDate.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwRuntimeImgDate.setStatus(_A)
_ChSysSwCurrentBootImgVersion_Type=DisplayString
_ChSysSwCurrentBootImgVersion_Object=MibTableColumn
chSysSwCurrentBootImgVersion=_ChSysSwCurrentBootImgVersion_Object((1,3,6,1,4,1,6027,3,19,1,2,7,1,3),_ChSysSwCurrentBootImgVersion_Type())
chSysSwCurrentBootImgVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwCurrentBootImgVersion.setStatus(_A)
_ChSysSwCurrentBootImgDate_Type=DateAndTime
_ChSysSwCurrentBootImgDate_Object=MibTableColumn
chSysSwCurrentBootImgDate=_ChSysSwCurrentBootImgDate_Object((1,3,6,1,4,1,6027,3,19,1,2,7,1,4),_ChSysSwCurrentBootImgDate_Type())
chSysSwCurrentBootImgDate.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwCurrentBootImgDate.setStatus(_A)
class _ChSysSwCurrentBootImgStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),(_a,2)))
_ChSysSwCurrentBootImgStatus_Type.__name__=_E
_ChSysSwCurrentBootImgStatus_Object=MibTableColumn
chSysSwCurrentBootImgStatus=_ChSysSwCurrentBootImgStatus_Object((1,3,6,1,4,1,6027,3,19,1,2,7,1,5),_ChSysSwCurrentBootImgStatus_Type())
chSysSwCurrentBootImgStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwCurrentBootImgStatus.setStatus(_A)
_ChSysSwBackupBootImgVersion_Type=DisplayString
_ChSysSwBackupBootImgVersion_Object=MibTableColumn
chSysSwBackupBootImgVersion=_ChSysSwBackupBootImgVersion_Object((1,3,6,1,4,1,6027,3,19,1,2,7,1,6),_ChSysSwBackupBootImgVersion_Type())
chSysSwBackupBootImgVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwBackupBootImgVersion.setStatus(_A)
_ChSysSwBackupBootImgDate_Type=DateAndTime
_ChSysSwBackupBootImgDate_Object=MibTableColumn
chSysSwBackupBootImgDate=_ChSysSwBackupBootImgDate_Object((1,3,6,1,4,1,6027,3,19,1,2,7,1,7),_ChSysSwBackupBootImgDate_Type())
chSysSwBackupBootImgDate.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwBackupBootImgDate.setStatus(_A)
class _ChSysSwBackupBootImgStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),(_a,2)))
_ChSysSwBackupBootImgStatus_Type.__name__=_E
_ChSysSwBackupBootImgStatus_Object=MibTableColumn
chSysSwBackupBootImgStatus=_ChSysSwBackupBootImgStatus_Object((1,3,6,1,4,1,6027,3,19,1,2,7,1,8),_ChSysSwBackupBootImgStatus_Type())
chSysSwBackupBootImgStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwBackupBootImgStatus.setStatus(_A)
class _ChSysSwNextRebootImage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_ChSysSwNextRebootImage_Type.__name__=_E
_ChSysSwNextRebootImage_Object=MibTableColumn
chSysSwNextRebootImage=_ChSysSwNextRebootImage_Object((1,3,6,1,4,1,6027,3,19,1,2,7,1,9),_ChSysSwNextRebootImage_Type())
chSysSwNextRebootImage.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwNextRebootImage.setStatus(_A)
class _ChSysSwCurrentBootImage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_c,2)))
_ChSysSwCurrentBootImage_Type.__name__=_E
_ChSysSwCurrentBootImage_Object=MibTableColumn
chSysSwCurrentBootImage=_ChSysSwCurrentBootImage_Object((1,3,6,1,4,1,6027,3,19,1,2,7,1,10),_ChSysSwCurrentBootImage_Type())
chSysSwCurrentBootImage.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwCurrentBootImage.setStatus(_A)
_ChSysSwInPartitionAImgVers_Type=DisplayString
_ChSysSwInPartitionAImgVers_Object=MibTableColumn
chSysSwInPartitionAImgVers=_ChSysSwInPartitionAImgVers_Object((1,3,6,1,4,1,6027,3,19,1,2,7,1,11),_ChSysSwInPartitionAImgVers_Type())
chSysSwInPartitionAImgVers.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwInPartitionAImgVers.setStatus(_A)
_ChSysSwInPartitionBImgVers_Type=DisplayString
_ChSysSwInPartitionBImgVers_Object=MibTableColumn
chSysSwInPartitionBImgVers=_ChSysSwInPartitionBImgVers_Object((1,3,6,1,4,1,6027,3,19,1,2,7,1,12),_ChSysSwInPartitionBImgVers_Type())
chSysSwInPartitionBImgVers.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysSwInPartitionBImgVers.setStatus(_A)
_ChStackUnitUtilTable_Object=MibTable
chStackUnitUtilTable=_ChStackUnitUtilTable_Object((1,3,6,1,4,1,6027,3,19,1,2,8))
if mibBuilder.loadTexts:chStackUnitUtilTable.setStatus(_A)
_ChStackUnitUtilEntry_Object=MibTableRow
chStackUnitUtilEntry=_ChStackUnitUtilEntry_Object((1,3,6,1,4,1,6027,3,19,1,2,8,1))
chStackUnitUtilEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:chStackUnitUtilEntry.setStatus(_A)
_ChStackUnitCpuType_Type=F10ProcessorModuleType
_ChStackUnitCpuType_Object=MibTableColumn
chStackUnitCpuType=_ChStackUnitCpuType_Object((1,3,6,1,4,1,6027,3,19,1,2,8,1,1),_ChStackUnitCpuType_Type())
chStackUnitCpuType.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitCpuType.setStatus(_A)
class _ChStackUnitCpuUtil5Sec_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ChStackUnitCpuUtil5Sec_Type.__name__=_K
_ChStackUnitCpuUtil5Sec_Object=MibTableColumn
chStackUnitCpuUtil5Sec=_ChStackUnitCpuUtil5Sec_Object((1,3,6,1,4,1,6027,3,19,1,2,8,1,2),_ChStackUnitCpuUtil5Sec_Type())
chStackUnitCpuUtil5Sec.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitCpuUtil5Sec.setStatus(_A)
if mibBuilder.loadTexts:chStackUnitCpuUtil5Sec.setUnits(_N)
class _ChStackUnitCpuUtil1Min_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ChStackUnitCpuUtil1Min_Type.__name__=_K
_ChStackUnitCpuUtil1Min_Object=MibTableColumn
chStackUnitCpuUtil1Min=_ChStackUnitCpuUtil1Min_Object((1,3,6,1,4,1,6027,3,19,1,2,8,1,3),_ChStackUnitCpuUtil1Min_Type())
chStackUnitCpuUtil1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitCpuUtil1Min.setStatus(_A)
if mibBuilder.loadTexts:chStackUnitCpuUtil1Min.setUnits(_N)
class _ChStackUnitCpuUtil5Min_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ChStackUnitCpuUtil5Min_Type.__name__=_K
_ChStackUnitCpuUtil5Min_Object=MibTableColumn
chStackUnitCpuUtil5Min=_ChStackUnitCpuUtil5Min_Object((1,3,6,1,4,1,6027,3,19,1,2,8,1,4),_ChStackUnitCpuUtil5Min_Type())
chStackUnitCpuUtil5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitCpuUtil5Min.setStatus(_A)
if mibBuilder.loadTexts:chStackUnitCpuUtil5Min.setUnits(_N)
class _ChStackUnitMemUsageUtil_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ChStackUnitMemUsageUtil_Type.__name__=_K
_ChStackUnitMemUsageUtil_Object=MibTableColumn
chStackUnitMemUsageUtil=_ChStackUnitMemUsageUtil_Object((1,3,6,1,4,1,6027,3,19,1,2,8,1,5),_ChStackUnitMemUsageUtil_Type())
chStackUnitMemUsageUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitMemUsageUtil.setStatus(_A)
if mibBuilder.loadTexts:chStackUnitMemUsageUtil.setUnits(_N)
class _ChStackUnitFlashUsageUtil_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ChStackUnitFlashUsageUtil_Type.__name__=_K
_ChStackUnitFlashUsageUtil_Object=MibTableColumn
chStackUnitFlashUsageUtil=_ChStackUnitFlashUsageUtil_Object((1,3,6,1,4,1,6027,3,19,1,2,8,1,6),_ChStackUnitFlashUsageUtil_Type())
chStackUnitFlashUsageUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:chStackUnitFlashUsageUtil.setStatus(_A)
if mibBuilder.loadTexts:chStackUnitFlashUsageUtil.setUnits(_N)
_ChSysSwCoresTable_Object=MibTable
chSysSwCoresTable=_ChSysSwCoresTable_Object((1,3,6,1,4,1,6027,3,19,1,2,9))
if mibBuilder.loadTexts:chSysSwCoresTable.setStatus(_A)
_ChSysCoresEntry_Object=MibTableRow
chSysCoresEntry=_ChSysCoresEntry_Object((1,3,6,1,4,1,6027,3,19,1,2,9,1))
chSysCoresEntry.setIndexNames((0,_B,_F),(0,_B,_V))
if mibBuilder.loadTexts:chSysCoresEntry.setStatus(_A)
_ChSysCoresInstance_Type=Integer32
_ChSysCoresInstance_Object=MibTableColumn
chSysCoresInstance=_ChSysCoresInstance_Object((1,3,6,1,4,1,6027,3,19,1,2,9,1,1),_ChSysCoresInstance_Type())
chSysCoresInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCoresInstance.setStatus(_A)
_ChSysCoresFileName_Type=DisplayString
_ChSysCoresFileName_Object=MibTableColumn
chSysCoresFileName=_ChSysCoresFileName_Object((1,3,6,1,4,1,6027,3,19,1,2,9,1,2),_ChSysCoresFileName_Type())
chSysCoresFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCoresFileName.setStatus(_A)
_ChSysCoresTimeCreated_Type=F10SwDate
_ChSysCoresTimeCreated_Object=MibTableColumn
chSysCoresTimeCreated=_ChSysCoresTimeCreated_Object((1,3,6,1,4,1,6027,3,19,1,2,9,1,3),_ChSysCoresTimeCreated_Type())
chSysCoresTimeCreated.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCoresTimeCreated.setStatus(_A)
class _ChSysCoresStackUnitNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_ChSysCoresStackUnitNumber_Type.__name__=_E
_ChSysCoresStackUnitNumber_Object=MibTableColumn
chSysCoresStackUnitNumber=_ChSysCoresStackUnitNumber_Object((1,3,6,1,4,1,6027,3,19,1,2,9,1,4),_ChSysCoresStackUnitNumber_Type())
chSysCoresStackUnitNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCoresStackUnitNumber.setStatus(_A)
_ChSysCoresProcess_Type=DisplayString
_ChSysCoresProcess_Object=MibTableColumn
chSysCoresProcess=_ChSysCoresProcess_Object((1,3,6,1,4,1,6027,3,19,1,2,9,1,5),_ChSysCoresProcess_Type())
chSysCoresProcess.setMaxAccess(_C)
if mibBuilder.loadTexts:chSysCoresProcess.setStatus(_A)
_ChAlarmObjects_ObjectIdentity=ObjectIdentity
chAlarmObjects=_ChAlarmObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,19,1,4))
_ChAlarmMibNotifications_ObjectIdentity=ObjectIdentity
chAlarmMibNotifications=_ChAlarmMibNotifications_ObjectIdentity((1,3,6,1,4,1,6027,3,19,1,4,0))
_F10mSeriesMibConformance_ObjectIdentity=ObjectIdentity
f10mSeriesMibConformance=_F10mSeriesMibConformance_ObjectIdentity((1,3,6,1,4,1,6027,3,19,2))
_F10mSeriesMibCompliances_ObjectIdentity=ObjectIdentity
f10mSeriesMibCompliances=_F10mSeriesMibCompliances_ObjectIdentity((1,3,6,1,4,1,6027,3,19,2,1))
_F10mSeriesMibGroups_ObjectIdentity=ObjectIdentity
f10mSeriesMibGroups=_F10mSeriesMibGroups_ObjectIdentity((1,3,6,1,4,1,6027,3,19,2,2))
f10mSeriesComponentGroup=ObjectGroup((1,3,6,1,4,1,6027,3,19,2,2,1))
f10mSeriesComponentGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:f10mSeriesComponentGroup.setStatus(_A)
f10mSeriesSystemGroup=ObjectGroup((1,3,6,1,4,1,6027,3,19,2,2,2))
f10mSeriesSystemGroup.setObjects(*((_B,_F),(_B,_g),(_B,_W),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_P),(_B,_AB),(_B,_AC),(_B,_R),(_B,_AD),(_B,_T),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_U),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_V),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au)))
if mibBuilder.loadTexts:f10mSeriesSystemGroup.setStatus(_A)
chAlarmStackUnitDown=NotificationType((1,3,6,1,4,1,6027,3,19,1,4,0,1))
chAlarmStackUnitDown.setObjects(*((_D,_H),(_D,_G),(_D,_J),(_D,_I)))
if mibBuilder.loadTexts:chAlarmStackUnitDown.setStatus(_A)
chAlarmStackUnitUp=NotificationType((1,3,6,1,4,1,6027,3,19,1,4,0,2))
chAlarmStackUnitUp.setObjects(*((_D,_H),(_D,_G),(_D,_J),(_D,_I)))
if mibBuilder.loadTexts:chAlarmStackUnitUp.setStatus(_A)
chAlarmStackUnitReset=NotificationType((1,3,6,1,4,1,6027,3,19,1,4,0,3))
chAlarmStackUnitReset.setObjects(*((_D,_H),(_D,_G),(_D,_J),(_D,_I)))
if mibBuilder.loadTexts:chAlarmStackUnitReset.setStatus(_A)
chAlarmStackUnitOffline=NotificationType((1,3,6,1,4,1,6027,3,19,1,4,0,4))
chAlarmStackUnitOffline.setObjects(*((_D,_H),(_D,_G),(_D,_J),(_D,_I)))
if mibBuilder.loadTexts:chAlarmStackUnitOffline.setStatus(_A)
chAlarmStackUnitCodeMismatch=NotificationType((1,3,6,1,4,1,6027,3,19,1,4,0,5))
chAlarmStackUnitCodeMismatch.setObjects(*((_D,_H),(_D,_G),(_D,_J),(_D,_I)))
if mibBuilder.loadTexts:chAlarmStackUnitCodeMismatch.setStatus(_A)
chAlarmStackPortLinkUp=NotificationType((1,3,6,1,4,1,6027,3,19,1,4,0,6))
chAlarmStackPortLinkUp.setObjects(*((_D,_H),(_D,_G),(_D,_J),(_D,_I)))
if mibBuilder.loadTexts:chAlarmStackPortLinkUp.setStatus(_A)
chAlarmStackPortLinkDown=NotificationType((1,3,6,1,4,1,6027,3,19,1,4,0,7))
chAlarmStackPortLinkDown.setObjects(*((_D,_H),(_D,_G),(_D,_J),(_D,_I)))
if mibBuilder.loadTexts:chAlarmStackPortLinkDown.setStatus(_A)
chAlarmStackUnitRoleChanged=NotificationType((1,3,6,1,4,1,6027,3,19,1,4,0,8))
chAlarmStackUnitRoleChanged.setObjects(*((_B,_W),(_D,_G)))
if mibBuilder.loadTexts:chAlarmStackUnitRoleChanged.setStatus(_A)
f10mSeriesNotificationGroup=NotificationGroup((1,3,6,1,4,1,6027,3,19,2,2,3))
f10mSeriesNotificationGroup.setObjects(*((_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1)))
if mibBuilder.loadTexts:f10mSeriesNotificationGroup.setStatus(_A)
f10mSeriesMibCompliance=ModuleCompliance((1,3,6,1,4,1,6027,3,19,2,1,1))
f10mSeriesMibCompliance.setObjects(*((_B,_B2),(_B,_B3),(_B,_B4)))
if mibBuilder.loadTexts:f10mSeriesMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CodeType':CodeType,'UnitType':UnitType,'f10MSerChassisMib':f10MSerChassisMib,'f10MSerChassisObject':f10MSerChassisObject,'chObjects':chObjects,_d:chNumStackUnits,_e:chNumMaxStackableUnits,_f:chStackUnitIndexNext,'chSysObjects':chSysObjects,'chStackUnitTable':chStackUnitTable,'chStackUnitEntry':chStackUnitEntry,_Y:chStackUnitIndex,_F:chStackUnitNumber,_g:chStackUnitSID,_W:chStackUnitMgmtStatus,_h:chStackUnitHwMgmtPreference,_i:chStackUnitAdmMgmtPreference,_j:chStackUnitModelID,_k:chStackUnitStatus,_l:chStackUnitDescription,_m:chStackUnitCodeVersion,_n:chStackUnitCodeVersionInFlash,_o:chStackUnitSerialNumber,_p:chStackUnitUpTime,_q:chStackUnitTemp,_r:chStackUnitType,_s:chStackUnitSysType,_t:chStackUnitVendorId,_u:chStackUnitMfgDate,_v:chStackUnitMacAddress,_w:chStackUnitPartNum,_x:chStackUnitProductRev,_y:chStackUnitProductOrder,_z:chStackUnitCountryCode,_A0:chStackUnitNum10GigEtherPorts,_A1:chStackUnitNumGigEtherPorts,_A2:chStackUnitNumFastEtherPorts,_A3:chStackUnitNumFanTrays,_A4:chStackUnitNumPowerSupplies,_A5:chStackUnitNumPluggableModules,'chStackUnitNum40GigEtherPorts':chStackUnitNum40GigEtherPorts,_A6:chStackUnitRowStatus,_A7:chStackUnitPiecePartID,_A8:chStackUnitPPIDRevision,_A9:chStackUnitServiceTag,_AA:chStackUnitExpressServiceCode,'chSysPowerSupplyTable':chSysPowerSupplyTable,'chSysPowerSupplyEntry':chSysPowerSupplyEntry,_P:chSysPowerSupplyIndex,_AB:chSysPowerSupplyOperStatus,_AC:chSysPowerSupplyType,'chSysFanTrayTable':chSysFanTrayTable,'chSysFanTrayEntry':chSysFanTrayEntry,_R:chSysFanTrayIndex,_AD:chSysFanTrayOperStatus,'chSysPortTable':chSysPortTable,'chSysPortEntry':chSysPortEntry,_T:chSysPortIndex,_AE:chSysPortType,_AF:chSysPortAdminStatus,_AG:chSysPortOperStatus,_AH:chSysPortIfIndex,_AI:chSysPortXfpRecvPower,_AJ:chSysPortXfpRecvTemp,_AK:chSysPortXfpTxPower,'chSysStackPortTable':chSysStackPortTable,'chSysStackPortEntry':chSysStackPortEntry,_U:chSysStackPortIndex,_AL:chSysStackPortConfiguredMode,_AM:chSysStackPortRunningMode,_AN:chSysStackPortLinkStatus,_AO:chSysStackPortLinkSpeed,_AP:chSysStackPortRxDataRate,_AQ:chSysStackPortRxErrorRate,_AR:chSysStackPortRxTotalErrors,_AS:chSysStackPortTxDataRate,_AT:chSysStackPortTxErrorRate,_AU:chSysStackPortTxTotalErrors,'chSysProcessorTable':chSysProcessorTable,'chSysProcessorEntry':chSysProcessorEntry,_AV:chSysProcessorModule,_AW:chSysProcessorUpTime,_AX:chSysProcessorNvramSize,_AY:chSysProcessorMemSize,'chSysSwModuleTable':chSysSwModuleTable,'chSysSwModuleEntry':chSysSwModuleEntry,_AZ:chSysSwRuntimeImgVersion,_Aa:chSysSwRuntimeImgDate,_Ab:chSysSwCurrentBootImgVersion,_Ac:chSysSwCurrentBootImgDate,_Ad:chSysSwCurrentBootImgStatus,_Ae:chSysSwBackupBootImgVersion,_Af:chSysSwBackupBootImgDate,_Ag:chSysSwBackupBootImgStatus,_Ah:chSysSwNextRebootImage,_Ai:chSysSwCurrentBootImage,_Aj:chSysSwInPartitionAImgVers,_Ak:chSysSwInPartitionBImgVers,'chStackUnitUtilTable':chStackUnitUtilTable,'chStackUnitUtilEntry':chStackUnitUtilEntry,_Al:chStackUnitCpuType,_Am:chStackUnitCpuUtil5Sec,_An:chStackUnitCpuUtil1Min,_Ao:chStackUnitCpuUtil5Min,_Ap:chStackUnitMemUsageUtil,_Aq:chStackUnitFlashUsageUtil,'chSysSwCoresTable':chSysSwCoresTable,'chSysCoresEntry':chSysCoresEntry,_V:chSysCoresInstance,_Ar:chSysCoresFileName,_As:chSysCoresTimeCreated,_At:chSysCoresStackUnitNumber,_Au:chSysCoresProcess,'chAlarmObjects':chAlarmObjects,'chAlarmMibNotifications':chAlarmMibNotifications,_Av:chAlarmStackUnitDown,_Aw:chAlarmStackUnitUp,_Ax:chAlarmStackUnitReset,_Ay:chAlarmStackUnitOffline,_Az:chAlarmStackUnitCodeMismatch,_A_:chAlarmStackPortLinkUp,_B0:chAlarmStackPortLinkDown,_B1:chAlarmStackUnitRoleChanged,'f10mSeriesMibConformance':f10mSeriesMibConformance,'f10mSeriesMibCompliances':f10mSeriesMibCompliances,'f10mSeriesMibCompliance':f10mSeriesMibCompliance,'f10mSeriesMibGroups':f10mSeriesMibGroups,_B2:f10mSeriesComponentGroup,_B3:f10mSeriesSystemGroup,_B4:f10mSeriesNotificationGroup})