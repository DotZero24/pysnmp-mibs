_Bm='mdlPsTestResult'
_Bl='mdlCConfigMismatchReason'
_Bk='mdlCHardwareFailureReason'
_Bj='sysCRdnOnline'
_Bi='sysDclOnline'
_Bh='sysDclRedundancyStatus'
_Bg='sysSAlrStatus'
_Bf='sysSAlrStatusAll'
_Be='mdlSActivity'
_Bd='mdlSCardType'
_Bc='sysDbaseDownloadCnfgIdxCmd'
_Bb='sysSSanityCheckStatus'
_Ba='alrGenCode'
_BZ='mapLinkIdx'
_BY='cmprPrtIdx'
_BX='cmprSltIdx'
_BW='cmprVersion'
_BV='cmprCnfgIdx'
_BU='cmprTypeIdx'
_BT='prtT3E3PrtIdx'
_BS='prtT3E3CnfgIdx'
_BR='prtHdslIdx'
_BQ='prtICnfgIdx'
_BP='prtDestIdx'
_BO='prtDestDimIdx'
_BN='prtDestCnfgIdx'
_BM='prtDimIdx'
_BL='prtDimCnfgIdx'
_BK='prtSpPrtIdx'
_BJ='prtSpCnfgIdx'
_BI='prtHSBertPrtIdx'
_BH='prtHSPrtIdx'
_BG='prtHSCnfgIdx'
_BF='prtT1E1FdlMsgFdlType'
_BE='prtT1E1FdlMsgPrtIdx'
_BD='dedicatedFr'
_BC='prtT1E1PrtIdx'
_BB='prtT1E1CnfgIdx'
_BA='prtT1E1SPrtIdx'
_B9='userConfig'
_B8='prtCfgParamIdx'
_B7='prtCfgParamCnfgIdx'
_B6='prtMonitoringIdx'
_B5='prtMonCnfgIdx'
_B4='prtBertPrtIdx'
_B3='prtAlrMaskPrtIdx'
_B2='prtSAlarmIdx'
_B1='prtSAlarmPrtIdx'
_B0='prtGenTsIdx'
_A_='prtGenTsPrtIdx'
_Az='prtGenTsCnfgIdx'
_Ay='prtGenTestIdx'
_Ax='prtGenTestPrtIdx'
_Aw='prtGenPrtIdx'
_Av='mdlAlrMaskSltIdx'
_Au='mdlAlrIdx'
_At='mdlAlrSltIdx'
_As='cardMismatch'
_Ar='notPresent'
_Aq='mdlCSlotIdx'
_Ap='mdlCConfigIdx'
_Ao='mdlSSltIdx'
_An='sysDbaseFlipIdx'
_Am='linkAggregation'
_Al='sysCRdnCnfgIdx'
_Ak='sysCnfgIdx'
_Aj='sysCClkSrcIdx'
_Ai='sysCClkCnfgIdx'
_Ah='sysBufferAlrIdx'
_Ag='sysSAlrIdx'
_Af='sysSBusPortIdx'
_Ae='sysSRdnFlipIdx'
_Ad='sysSErrIdx'
_Ac='sysSErrType'
_Ab='sysDclCopyDbIdx'
_Aa='sysDclCnfgIdx'
_AZ='e1T1orSerial'
_AY='SnmpAdminString'
_AX='entPhysicalSoftwareRev'
_AW='entPhysicalHardwareRev'
_AV='manual'
_AU='normal'
_AT='kmxOpt'
_AS='sysCRdnPrimePort'
_AR='sysCRdnPrimeSlot'
_AQ='secondary'
_AP='primary'
_AO='high'
_AN='enable'
_AM='disable'
_AL='rip2'
_AK='kmxIO12'
_AJ='kmxIO11'
_AI='kmxIO10'
_AH='kmxIO9'
_AG='kmxIO8'
_AF='kmxIO7'
_AE='kmxIO6'
_AD='kmxIO5'
_AC='kmxIO4'
_AB='kmxIO3'
_AA='kmxIO2'
_A9='kmxIO1'
_A8='kmxMlB'
_A7='kmxMlA'
_A6='dclB'
_A5='dclA'
_A4='Unsigned32'
_A3='mdlCProgCardType'
_A2='down'
_A1='proprietary'
_A0='enabled'
_z='internal'
_y='disabled'
_x='auto'
_w='clB'
_v='clA'
_u='unknown'
_t='standAlone'
_s='other'
_r='mdlCActualCardType'
_q='yes'
_p='no'
_o='critical'
_n='event'
_m='minor'
_l='OctetString'
_k='major'
_j='io15'
_i='io14'
_h='io13'
_g='io12'
_f='io11'
_e='io10'
_d='warning'
_c='none'
_b='io9'
_a='io8'
_Z='io7'
_Y='io6'
_X='io5'
_W='io4'
_V='io3'
_U='io2'
_T='io1'
_S='alarmEventReason'
_R='alarmEventLogSourceName'
_Q='alarmEventLogSeverity'
_P='alarmEventLogDescription'
_O='alarmEventLogDateAndTime'
_N='alarmEventLogAlarmOrEventId'
_M='entPhysicalAlias'
_L='ENTITY-MIB'
_K='read-create'
_J='DisplayString'
_I='on'
_H='off'
_G='RAD-GEN-MIB'
_F='RAD-Dacs-MIB'
_E='notApplicable'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_l,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PhysicalIndexOrZero,entPhysicalAlias,entPhysicalDescr,entPhysicalEntry,entPhysicalHardwareRev,entPhysicalSoftwareRev=mibBuilder.importSymbols(_L,'PhysicalIndexOrZero',_M,'entPhysicalDescr','entPhysicalEntry',_AW,_AX)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
agnLed,agnThresholdMax,agnThresholdMin,agnThresholdUom,alarmEventLogAlarmOrEventId,alarmEventLogDateAndTime,alarmEventLogDescription,alarmEventLogSeverity,alarmEventLogSourceName,alarmEventReason,systemsEvents=mibBuilder.importSymbols(_G,'agnLed','agnThresholdMax','agnThresholdMin','agnThresholdUom',_N,_O,_P,_Q,_R,_S,'systemsEvents')
protectGroupLastCmd,protectGroupLastSwitchReason=mibBuilder.importSymbols('RAD-Protection-MIB','protectGroupLastCmd','protectGroupLastSwitchReason')
radWan,=mibBuilder.importSymbols('RAD-SMI-MIB','radWan')
CardType,ProtectGroupCmdType,ProtectLastSwitchReasonType,SlotType=mibBuilder.importSymbols('RAD-TC','CardType','ProtectGroupCmdType','ProtectLastSwitchReasonType','SlotType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_AY)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols('SNMPv2-MIB','sysName')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_A4,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
dacsMux=ModuleIdentity((1,3,6,1,4,1,164,3,3))
_DacsMuxEvents_ObjectIdentity=ObjectIdentity
dacsMuxEvents=_DacsMuxEvents_ObjectIdentity((1,3,6,1,4,1,164,3,3,0))
if mibBuilder.loadTexts:dacsMuxEvents.setStatus(_A)
_SystemDacsMux_ObjectIdentity=ObjectIdentity
systemDacsMux=_SystemDacsMux_ObjectIdentity((1,3,6,1,4,1,164,3,3,1))
_SysSa_ObjectIdentity=ObjectIdentity
sysSa=_SysSa_ObjectIdentity((1,3,6,1,4,1,164,3,3,1,1))
_SysSaSwchStatus_Type=Integer32
_SysSaSwchStatus_Object=MibScalar
sysSaSwchStatus=_SysSaSwchStatus_Object((1,3,6,1,4,1,164,3,3,1,1,1),_SysSaSwchStatus_Type())
sysSaSwchStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSaSwchStatus.setStatus(_A)
class _SysSaSwRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysSaSwRevision_Type.__name__=_J
_SysSaSwRevision_Object=MibScalar
sysSaSwRevision=_SysSaSwRevision_Object((1,3,6,1,4,1,164,3,3,1,1,2),_SysSaSwRevision_Type())
sysSaSwRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSaSwRevision.setStatus(_A)
class _SysSaHwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysSaHwVersion_Type.__name__=_J
_SysSaHwVersion_Object=MibScalar
sysSaHwVersion=_SysSaHwVersion_Object((1,3,6,1,4,1,164,3,3,1,1,3),_SysSaHwVersion_Type())
sysSaHwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSaHwVersion.setStatus(_A)
_SysSaPorts_Type=Integer32
_SysSaPorts_Object=MibScalar
sysSaPorts=_SysSaPorts_Object((1,3,6,1,4,1,164,3,3,1,1,4),_SysSaPorts_Type())
sysSaPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSaPorts.setStatus(_A)
_SysSaReadSwch_Type=Integer32
_SysSaReadSwch_Object=MibScalar
sysSaReadSwch=_SysSaReadSwch_Object((1,3,6,1,4,1,164,3,3,1,1,5),_SysSaReadSwch_Type())
sysSaReadSwch.setMaxAccess(_D)
if mibBuilder.loadTexts:sysSaReadSwch.setStatus(_A)
class _SysSaBuActivePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),(_AZ,2),('eth',3),(_AP,4),(_AQ,5),('third',6),('fourth',7)))
_SysSaBuActivePort_Type.__name__=_B
_SysSaBuActivePort_Object=MibScalar
sysSaBuActivePort=_SysSaBuActivePort_Object((1,3,6,1,4,1,164,3,3,1,1,6),_SysSaBuActivePort_Type())
sysSaBuActivePort.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSaBuActivePort.setStatus(_A)
_SysHub_ObjectIdentity=ObjectIdentity
sysHub=_SysHub_ObjectIdentity((1,3,6,1,4,1,164,3,3,1,2))
_SysChas_ObjectIdentity=ObjectIdentity
sysChas=_SysChas_ObjectIdentity((1,3,6,1,4,1,164,3,3,1,2,1))
_ChassTotalNoOfSlt_Type=Integer32
_ChassTotalNoOfSlt_Object=MibScalar
chassTotalNoOfSlt=_ChassTotalNoOfSlt_Object((1,3,6,1,4,1,164,3,3,1,2,1,1),_ChassTotalNoOfSlt_Type())
chassTotalNoOfSlt.setMaxAccess(_C)
if mibBuilder.loadTexts:chassTotalNoOfSlt.setStatus(_A)
_ChassTotalNoOfIoSlt_Type=Integer32
_ChassTotalNoOfIoSlt_Object=MibScalar
chassTotalNoOfIoSlt=_ChassTotalNoOfIoSlt_Object((1,3,6,1,4,1,164,3,3,1,2,1,2),_ChassTotalNoOfIoSlt_Type())
chassTotalNoOfIoSlt.setMaxAccess(_C)
if mibBuilder.loadTexts:chassTotalNoOfIoSlt.setStatus(_A)
_ChassTotalNoOfPsSlt_Type=Integer32
_ChassTotalNoOfPsSlt_Object=MibScalar
chassTotalNoOfPsSlt=_ChassTotalNoOfPsSlt_Object((1,3,6,1,4,1,164,3,3,1,2,1,3),_ChassTotalNoOfPsSlt_Type())
chassTotalNoOfPsSlt.setMaxAccess(_C)
if mibBuilder.loadTexts:chassTotalNoOfPsSlt.setStatus(_A)
_ChassTotalNoOfClSlt_Type=Integer32
_ChassTotalNoOfClSlt_Object=MibScalar
chassTotalNoOfClSlt=_ChassTotalNoOfClSlt_Object((1,3,6,1,4,1,164,3,3,1,2,1,4),_ChassTotalNoOfClSlt_Type())
chassTotalNoOfClSlt.setMaxAccess(_C)
if mibBuilder.loadTexts:chassTotalNoOfClSlt.setStatus(_A)
_ChassTotalNoOfMlSlt_Type=Integer32
_ChassTotalNoOfMlSlt_Object=MibScalar
chassTotalNoOfMlSlt=_ChassTotalNoOfMlSlt_Object((1,3,6,1,4,1,164,3,3,1,2,1,5),_ChassTotalNoOfMlSlt_Type())
chassTotalNoOfMlSlt.setMaxAccess(_C)
if mibBuilder.loadTexts:chassTotalNoOfMlSlt.setStatus(_A)
_SysDcl_ObjectIdentity=ObjectIdentity
sysDcl=_SysDcl_ObjectIdentity((1,3,6,1,4,1,164,3,3,1,2,2))
_SysDclTable_Object=MibTable
sysDclTable=_SysDclTable_Object((1,3,6,1,4,1,164,3,3,1,2,2,1))
if mibBuilder.loadTexts:sysDclTable.setStatus(_A)
_SysDclEntry_Object=MibTableRow
sysDclEntry=_SysDclEntry_Object((1,3,6,1,4,1,164,3,3,1,2,2,1,1))
sysDclEntry.setIndexNames((0,_F,_Aa))
if mibBuilder.loadTexts:sysDclEntry.setStatus(_A)
class _SysDclCnfgIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SysDclCnfgIdx_Type.__name__=_B
_SysDclCnfgIdx_Object=MibTableColumn
sysDclCnfgIdx=_SysDclCnfgIdx_Object((1,3,6,1,4,1,164,3,3,1,2,2,1,1,1),_SysDclCnfgIdx_Type())
sysDclCnfgIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:sysDclCnfgIdx.setStatus(_A)
class _SysDclRedundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_SysDclRedundancy_Type.__name__=_B
_SysDclRedundancy_Object=MibTableColumn
sysDclRedundancy=_SysDclRedundancy_Object((1,3,6,1,4,1,164,3,3,1,2,2,1,1,2),_SysDclRedundancy_Type())
sysDclRedundancy.setMaxAccess(_D)
if mibBuilder.loadTexts:sysDclRedundancy.setStatus(_A)
class _SysDclActiveCl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_x,1),(_A5,2),(_A6,3)))
_SysDclActiveCl_Type.__name__=_B
_SysDclActiveCl_Object=MibTableColumn
sysDclActiveCl=_SysDclActiveCl_Object((1,3,6,1,4,1,164,3,3,1,2,2,1,1,3),_SysDclActiveCl_Type())
sysDclActiveCl.setMaxAccess(_D)
if mibBuilder.loadTexts:sysDclActiveCl.setStatus(_A)
_SysDclFlipDelay_Type=Integer32
_SysDclFlipDelay_Object=MibTableColumn
sysDclFlipDelay=_SysDclFlipDelay_Object((1,3,6,1,4,1,164,3,3,1,2,2,1,1,4),_SysDclFlipDelay_Type())
sysDclFlipDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:sysDclFlipDelay.setStatus(_A)
class _SysDclFlipUponStnClk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_p,2),(_q,3)))
_SysDclFlipUponStnClk_Type.__name__=_B
_SysDclFlipUponStnClk_Object=MibTableColumn
sysDclFlipUponStnClk=_SysDclFlipUponStnClk_Object((1,3,6,1,4,1,164,3,3,1,2,2,1,1,5),_SysDclFlipUponStnClk_Type())
sysDclFlipUponStnClk.setMaxAccess(_D)
if mibBuilder.loadTexts:sysDclFlipUponStnClk.setStatus(_A)
_SysDclChFailThreshold_Type=Integer32
_SysDclChFailThreshold_Object=MibTableColumn
sysDclChFailThreshold=_SysDclChFailThreshold_Object((1,3,6,1,4,1,164,3,3,1,2,2,1,1,6),_SysDclChFailThreshold_Type())
sysDclChFailThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sysDclChFailThreshold.setStatus(_A)
_SysDclChPriority_Type=OctetString
_SysDclChPriority_Object=MibTableColumn
sysDclChPriority=_SysDclChPriority_Object((1,3,6,1,4,1,164,3,3,1,2,2,1,1,7),_SysDclChPriority_Type())
sysDclChPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:sysDclChPriority.setStatus(_A)
class _SysDclConfigDownloadSrc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_A5,2),(_A6,3)))
_SysDclConfigDownloadSrc_Type.__name__=_B
_SysDclConfigDownloadSrc_Object=MibTableColumn
sysDclConfigDownloadSrc=_SysDclConfigDownloadSrc_Object((1,3,6,1,4,1,164,3,3,1,2,2,1,1,8),_SysDclConfigDownloadSrc_Type())
sysDclConfigDownloadSrc.setMaxAccess(_D)
if mibBuilder.loadTexts:sysDclConfigDownloadSrc.setStatus(_A)
class _SysDclSwDownloadSrc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_A5,2),(_A6,3)))
_SysDclSwDownloadSrc_Type.__name__=_B
_SysDclSwDownloadSrc_Object=MibTableColumn
sysDclSwDownloadSrc=_SysDclSwDownloadSrc_Object((1,3,6,1,4,1,164,3,3,1,2,2,1,1,9),_SysDclSwDownloadSrc_Type())
sysDclSwDownloadSrc.setMaxAccess(_D)
if mibBuilder.loadTexts:sysDclSwDownloadSrc.setStatus(_A)
class _SysDclRedundancyStatus_Type(Bits):namedValues=NamedValues(*(('cnfgMismatch',0),('swMismatch',1),('cardAAbsent',2),('cardBAbsent',3),('lossOfCommunication',4),('hwMismatch',5),('cnfgUpdate',6),('swUpdate',7)))
_SysDclRedundancyStatus_Type.__name__='Bits'
_SysDclRedundancyStatus_Object=MibTableColumn
sysDclRedundancyStatus=_SysDclRedundancyStatus_Object((1,3,6,1,4,1,164,3,3,1,2,2,1,1,10),_SysDclRedundancyStatus_Type())
sysDclRedundancyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sysDclRedundancyStatus.setStatus(_A)
class _SysDclOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_A5,1),(_A6,2)))
_SysDclOnline_Type.__name__=_B
_SysDclOnline_Object=MibScalar
sysDclOnline=_SysDclOnline_Object((1,3,6,1,4,1,164,3,3,1,2,2,2),_SysDclOnline_Type())
sysDclOnline.setMaxAccess(_C)
if mibBuilder.loadTexts:sysDclOnline.setStatus(_A)
_SysDclCopyDbTable_Object=MibTable
sysDclCopyDbTable=_SysDclCopyDbTable_Object((1,3,6,1,4,1,164,3,3,1,2,2,3))
if mibBuilder.loadTexts:sysDclCopyDbTable.setStatus(_A)
_SysDclCopyDbEntry_Object=MibTableRow
sysDclCopyDbEntry=_SysDclCopyDbEntry_Object((1,3,6,1,4,1,164,3,3,1,2,2,3,1))
sysDclCopyDbEntry.setIndexNames((0,_F,_Ab))
if mibBuilder.loadTexts:sysDclCopyDbEntry.setStatus(_A)
class _SysDclCopyDbIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SysDclCopyDbIdx_Type.__name__=_B
_SysDclCopyDbIdx_Object=MibTableColumn
sysDclCopyDbIdx=_SysDclCopyDbIdx_Object((1,3,6,1,4,1,164,3,3,1,2,2,3,1,1),_SysDclCopyDbIdx_Type())
sysDclCopyDbIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:sysDclCopyDbIdx.setStatus(_A)
class _SysDclCopyDbCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_SysDclCopyDbCmd_Type.__name__=_B
_SysDclCopyDbCmd_Object=MibTableColumn
sysDclCopyDbCmd=_SysDclCopyDbCmd_Object((1,3,6,1,4,1,164,3,3,1,2,2,3,1,2),_SysDclCopyDbCmd_Type())
sysDclCopyDbCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:sysDclCopyDbCmd.setStatus(_A)
class _SysDclFlipCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),('flip',3)))
_SysDclFlipCmd_Type.__name__=_B
_SysDclFlipCmd_Object=MibScalar
sysDclFlipCmd=_SysDclFlipCmd_Object((1,3,6,1,4,1,164,3,3,1,2,2,4),_SysDclFlipCmd_Type())
sysDclFlipCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:sysDclFlipCmd.setStatus(_A)
_SysStatus_ObjectIdentity=ObjectIdentity
sysStatus=_SysStatus_ObjectIdentity((1,3,6,1,4,1,164,3,3,1,3))
class _SysSDateFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ddMMYYYY',1),('mmDDYYYY',2),('yyyyDDMM',3),('yyyyMMDD',4)))
_SysSDateFormat_Type.__name__=_B
_SysSDateFormat_Object=MibScalar
sysSDateFormat=_SysSDateFormat_Object((1,3,6,1,4,1,164,3,3,1,3,1),_SysSDateFormat_Type())
sysSDateFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:sysSDateFormat.setStatus(_A)
class _SysSDateCmd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysSDateCmd_Type.__name__=_J
_SysSDateCmd_Object=MibScalar
sysSDateCmd=_SysSDateCmd_Object((1,3,6,1,4,1,164,3,3,1,3,2),_SysSDateCmd_Type())
sysSDateCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:sysSDateCmd.setStatus(_A)
class _SysSTimeCmd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysSTimeCmd_Type.__name__=_J
_SysSTimeCmd_Object=MibScalar
sysSTimeCmd=_SysSTimeCmd_Object((1,3,6,1,4,1,164,3,3,1,3,3),_SysSTimeCmd_Type())
sysSTimeCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:sysSTimeCmd.setStatus(_A)
_SysSActiveCnfg_Type=Integer32
_SysSActiveCnfg_Object=MibScalar
sysSActiveCnfg=_SysSActiveCnfg_Object((1,3,6,1,4,1,164,3,3,1,3,4),_SysSActiveCnfg_Type())
sysSActiveCnfg.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSActiveCnfg.setStatus(_A)
_SysSEditCnfg_Type=Integer32
_SysSEditCnfg_Object=MibScalar
sysSEditCnfg=_SysSEditCnfg_Object((1,3,6,1,4,1,164,3,3,1,3,5),_SysSEditCnfg_Type())
sysSEditCnfg.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSEditCnfg.setStatus(_A)
class _SysSEditBy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_c,1),('snmp',2),('terCon1',3),('terCon2',4),('terInbandCon1',5),('terInbandCon2',6),('lcd',7)))
_SysSEditBy_Type.__name__=_B
_SysSEditBy_Object=MibScalar
sysSEditBy=_SysSEditBy_Object((1,3,6,1,4,1,164,3,3,1,3,6),_SysSEditBy_Type())
sysSEditBy.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSEditBy.setStatus(_A)
class _SysSClkSrc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('master',1),('fallback',2),(_z,3),('ml',4)))
_SysSClkSrc_Type.__name__=_B
_SysSClkSrc_Object=MibScalar
sysSClkSrc=_SysSClkSrc_Object((1,3,6,1,4,1,164,3,3,1,3,7),_SysSClkSrc_Type())
sysSClkSrc.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSClkSrc.setStatus(_A)
class _SysSAlrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7)));namedValues=NamedValues(*((_H,2),(_k,3),(_m,4),(_n,5),(_d,6),(_o,7)))
_SysSAlrStatus_Type.__name__=_B
_SysSAlrStatus_Object=MibScalar
sysSAlrStatus=_SysSAlrStatus_Object((1,3,6,1,4,1,164,3,3,1,3,8),_SysSAlrStatus_Type())
sysSAlrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSAlrStatus.setStatus(_A)
class _SysSAlrStatusAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7)));namedValues=NamedValues(*((_H,2),(_k,3),(_m,4),(_n,5),(_d,6),(_o,7)))
_SysSAlrStatusAll_Type.__name__=_B
_SysSAlrStatusAll_Object=MibScalar
sysSAlrStatusAll=_SysSAlrStatusAll_Object((1,3,6,1,4,1,164,3,3,1,3,9),_SysSAlrStatusAll_Type())
sysSAlrStatusAll.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSAlrStatusAll.setStatus(_A)
class _SysSTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_SysSTestStatus_Type.__name__=_B
_SysSTestStatus_Object=MibScalar
sysSTestStatus=_SysSTestStatus_Object((1,3,6,1,4,1,164,3,3,1,3,10),_SysSTestStatus_Type())
sysSTestStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSTestStatus.setStatus(_A)
class _SysSSanityCheckStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_u,1),('fail',2),(_d,3),('ok',4)))
_SysSSanityCheckStatus_Type.__name__=_B
_SysSSanityCheckStatus_Object=MibScalar
sysSSanityCheckStatus=_SysSSanityCheckStatus_Object((1,3,6,1,4,1,164,3,3,1,3,11),_SysSSanityCheckStatus_Type())
sysSSanityCheckStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSSanityCheckStatus.setStatus(_A)
_SysSNoOfSanityCheckErr_Type=Integer32
_SysSNoOfSanityCheckErr_Object=MibScalar
sysSNoOfSanityCheckErr=_SysSNoOfSanityCheckErr_Object((1,3,6,1,4,1,164,3,3,1,3,12),_SysSNoOfSanityCheckErr_Type())
sysSNoOfSanityCheckErr.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSNoOfSanityCheckErr.setStatus(_A)
_SysSErrListTable_Object=MibTable
sysSErrListTable=_SysSErrListTable_Object((1,3,6,1,4,1,164,3,3,1,3,13))
if mibBuilder.loadTexts:sysSErrListTable.setStatus(_A)
_SysSErrListEntry_Object=MibTableRow
sysSErrListEntry=_SysSErrListEntry_Object((1,3,6,1,4,1,164,3,3,1,3,13,1))
sysSErrListEntry.setIndexNames((0,_F,_Ac),(0,_F,_Ad))
if mibBuilder.loadTexts:sysSErrListEntry.setStatus(_A)
class _SysSErrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('error',1),(_d,2)))
_SysSErrType_Type.__name__=_B
_SysSErrType_Object=MibTableColumn
sysSErrType=_SysSErrType_Object((1,3,6,1,4,1,164,3,3,1,3,13,1,1),_SysSErrType_Type())
sysSErrType.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSErrType.setStatus(_A)
_SysSErrIdx_Type=Integer32
_SysSErrIdx_Object=MibTableColumn
sysSErrIdx=_SysSErrIdx_Object((1,3,6,1,4,1,164,3,3,1,3,13,1,2),_SysSErrIdx_Type())
sysSErrIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSErrIdx.setStatus(_A)
class _SysSErrDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysSErrDescription_Type.__name__=_J
_SysSErrDescription_Object=MibTableColumn
sysSErrDescription=_SysSErrDescription_Object((1,3,6,1,4,1,164,3,3,1,3,13,1,3),_SysSErrDescription_Type())
sysSErrDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSErrDescription.setStatus(_A)
_SysSMaxNoOfCnfg_Type=Integer32
_SysSMaxNoOfCnfg_Object=MibScalar
sysSMaxNoOfCnfg=_SysSMaxNoOfCnfg_Object((1,3,6,1,4,1,164,3,3,1,3,14),_SysSMaxNoOfCnfg_Type())
sysSMaxNoOfCnfg.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSMaxNoOfCnfg.setStatus(_A)
_SysSSelfTestResult_Type=Integer32
_SysSSelfTestResult_Object=MibScalar
sysSSelfTestResult=_SysSSelfTestResult_Object((1,3,6,1,4,1,164,3,3,1,3,15),_SysSSelfTestResult_Type())
sysSSelfTestResult.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSSelfTestResult.setStatus(_A)
class _SysSRelayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_H,2),(_I,3)))
_SysSRelayState_Type.__name__=_B
_SysSRelayState_Object=MibScalar
sysSRelayState=_SysSRelayState_Object((1,3,6,1,4,1,164,3,3,1,3,16),_SysSRelayState_Type())
sysSRelayState.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSRelayState.setStatus(_A)
class _SysSInvertedAlr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_p,2),(_q,3)))
_SysSInvertedAlr_Type.__name__=_B
_SysSInvertedAlr_Object=MibScalar
sysSInvertedAlr=_SysSInvertedAlr_Object((1,3,6,1,4,1,164,3,3,1,3,17),_SysSInvertedAlr_Type())
sysSInvertedAlr.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSInvertedAlr.setStatus(_A)
_SysSRdnFlipTable_Object=MibTable
sysSRdnFlipTable=_SysSRdnFlipTable_Object((1,3,6,1,4,1,164,3,3,1,3,18))
if mibBuilder.loadTexts:sysSRdnFlipTable.setStatus(_A)
_SysSRdnFlipEntry_Object=MibTableRow
sysSRdnFlipEntry=_SysSRdnFlipEntry_Object((1,3,6,1,4,1,164,3,3,1,3,18,1))
sysSRdnFlipEntry.setIndexNames((0,_F,_Ae))
if mibBuilder.loadTexts:sysSRdnFlipEntry.setStatus(_A)
_SysSRdnFlipIdx_Type=Integer32
_SysSRdnFlipIdx_Object=MibTableColumn
sysSRdnFlipIdx=_SysSRdnFlipIdx_Object((1,3,6,1,4,1,164,3,3,1,3,18,1,1),_SysSRdnFlipIdx_Type())
sysSRdnFlipIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSRdnFlipIdx.setStatus(_A)
class _SysSRdnFlipSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,255)));namedValues=NamedValues(*((_T,5),(_U,6),(_V,7),(_W,8),(_X,9),(_Y,10),(_Z,11),(_a,12),(_b,13),(_e,14),(_f,15),(_g,16),(_h,17),(_i,18),(_j,19),(_E,255)))
_SysSRdnFlipSlot_Type.__name__=_B
_SysSRdnFlipSlot_Object=MibTableColumn
sysSRdnFlipSlot=_SysSRdnFlipSlot_Object((1,3,6,1,4,1,164,3,3,1,3,18,1,2),_SysSRdnFlipSlot_Type())
sysSRdnFlipSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSRdnFlipSlot.setStatus(_A)
_SysSRdnFlipPort_Type=Integer32
_SysSRdnFlipPort_Object=MibTableColumn
sysSRdnFlipPort=_SysSRdnFlipPort_Object((1,3,6,1,4,1,164,3,3,1,3,18,1,3),_SysSRdnFlipPort_Type())
sysSRdnFlipPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSRdnFlipPort.setStatus(_A)
_SysSRdnFlipCause_Type=DisplayString
_SysSRdnFlipCause_Object=MibTableColumn
sysSRdnFlipCause=_SysSRdnFlipCause_Object((1,3,6,1,4,1,164,3,3,1,3,18,1,4),_SysSRdnFlipCause_Type())
sysSRdnFlipCause.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSRdnFlipCause.setStatus(_A)
_SysSRdnFlipDate_Type=DisplayString
_SysSRdnFlipDate_Object=MibTableColumn
sysSRdnFlipDate=_SysSRdnFlipDate_Object((1,3,6,1,4,1,164,3,3,1,3,18,1,5),_SysSRdnFlipDate_Type())
sysSRdnFlipDate.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSRdnFlipDate.setStatus(_A)
_SysSRdnFlipTime_Type=DisplayString
_SysSRdnFlipTime_Object=MibTableColumn
sysSRdnFlipTime=_SysSRdnFlipTime_Object((1,3,6,1,4,1,164,3,3,1,3,18,1,6),_SysSRdnFlipTime_Type())
sysSRdnFlipTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSRdnFlipTime.setStatus(_A)
class _SysSRdnFlipTableClearCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_SysSRdnFlipTableClearCmd_Type.__name__=_B
_SysSRdnFlipTableClearCmd_Object=MibScalar
sysSRdnFlipTableClearCmd=_SysSRdnFlipTableClearCmd_Object((1,3,6,1,4,1,164,3,3,1,3,19),_SysSRdnFlipTableClearCmd_Type())
sysSRdnFlipTableClearCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:sysSRdnFlipTableClearCmd.setStatus(_A)
_SysSRdnFlipCmd_Type=ObjectIdentifier
_SysSRdnFlipCmd_Object=MibScalar
sysSRdnFlipCmd=_SysSRdnFlipCmd_Object((1,3,6,1,4,1,164,3,3,1,3,20),_SysSRdnFlipCmd_Type())
sysSRdnFlipCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:sysSRdnFlipCmd.setStatus(_A)
_SysSBusTable_Object=MibTable
sysSBusTable=_SysSBusTable_Object((1,3,6,1,4,1,164,3,3,1,3,21))
if mibBuilder.loadTexts:sysSBusTable.setStatus(_A)
_SysSBusEntry_Object=MibTableRow
sysSBusEntry=_SysSBusEntry_Object((1,3,6,1,4,1,164,3,3,1,3,21,1))
sysSBusEntry.setIndexNames((0,_F,_Af))
if mibBuilder.loadTexts:sysSBusEntry.setStatus(_A)
_SysSBusPortIdx_Type=Integer32
_SysSBusPortIdx_Object=MibTableColumn
sysSBusPortIdx=_SysSBusPortIdx_Object((1,3,6,1,4,1,164,3,3,1,3,21,1,1),_SysSBusPortIdx_Type())
sysSBusPortIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSBusPortIdx.setStatus(_A)
class _SysSBusStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('free',1),('physical',2),('virtual',3)))
_SysSBusStatus_Type.__name__=_B
_SysSBusStatus_Object=MibTableColumn
sysSBusStatus=_SysSBusStatus_Object((1,3,6,1,4,1,164,3,3,1,3,21,1,2),_SysSBusStatus_Type())
sysSBusStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSBusStatus.setStatus(_A)
_SysSBusCapturePort_Type=Integer32
_SysSBusCapturePort_Object=MibTableColumn
sysSBusCapturePort=_SysSBusCapturePort_Object((1,3,6,1,4,1,164,3,3,1,3,21,1,3),_SysSBusCapturePort_Type())
sysSBusCapturePort.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSBusCapturePort.setStatus(_A)
_SysSBusUtilization_Type=Integer32
_SysSBusUtilization_Object=MibTableColumn
sysSBusUtilization=_SysSBusUtilization_Object((1,3,6,1,4,1,164,3,3,1,3,21,1,4),_SysSBusUtilization_Type())
sysSBusUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSBusUtilization.setStatus(_A)
_SysSRdnCmdTable_Object=MibTable
sysSRdnCmdTable=_SysSRdnCmdTable_Object((1,3,6,1,4,1,164,3,3,1,3,22))
if mibBuilder.loadTexts:sysSRdnCmdTable.setStatus(_A)
_SysSRdnCmdEntry_Object=MibTableRow
sysSRdnCmdEntry=_SysSRdnCmdEntry_Object((1,3,6,1,4,1,164,3,3,1,3,22,1))
sysSRdnCmdEntry.setIndexNames((0,_F,_AR),(0,_F,_AS))
if mibBuilder.loadTexts:sysSRdnCmdEntry.setStatus(_A)
class _SysSRdnEnforcedChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('noEnforcement',2),(_AP,3),(_AQ,4)))
_SysSRdnEnforcedChannel_Type.__name__=_B
_SysSRdnEnforcedChannel_Object=MibTableColumn
sysSRdnEnforcedChannel=_SysSRdnEnforcedChannel_Object((1,3,6,1,4,1,164,3,3,1,3,22,1,1),_SysSRdnEnforcedChannel_Type())
sysSRdnEnforcedChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:sysSRdnEnforcedChannel.setStatus(_A)
class _SysSRdnLockFlip_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_H,2),(_I,3)))
_SysSRdnLockFlip_Type.__name__=_B
_SysSRdnLockFlip_Object=MibTableColumn
sysSRdnLockFlip=_SysSRdnLockFlip_Object((1,3,6,1,4,1,164,3,3,1,3,22,1,2),_SysSRdnLockFlip_Type())
sysSRdnLockFlip.setMaxAccess(_D)
if mibBuilder.loadTexts:sysSRdnLockFlip.setStatus(_A)
class _SysSRdnManualFlip_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_H,2),(_I,3)))
_SysSRdnManualFlip_Type.__name__=_B
_SysSRdnManualFlip_Object=MibTableColumn
sysSRdnManualFlip=_SysSRdnManualFlip_Object((1,3,6,1,4,1,164,3,3,1,3,22,1,3),_SysSRdnManualFlip_Type())
sysSRdnManualFlip.setMaxAccess(_D)
if mibBuilder.loadTexts:sysSRdnManualFlip.setStatus(_A)
_SysSAlrAttrIndication_Type=Integer32
_SysSAlrAttrIndication_Object=MibScalar
sysSAlrAttrIndication=_SysSAlrAttrIndication_Object((1,3,6,1,4,1,164,3,3,1,3,23),_SysSAlrAttrIndication_Type())
sysSAlrAttrIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSAlrAttrIndication.setStatus(_A)
_SysCurrentAlr_ObjectIdentity=ObjectIdentity
sysCurrentAlr=_SysCurrentAlr_ObjectIdentity((1,3,6,1,4,1,164,3,3,1,4))
_SysSAlrTable_Object=MibTable
sysSAlrTable=_SysSAlrTable_Object((1,3,6,1,4,1,164,3,3,1,4,1))
if mibBuilder.loadTexts:sysSAlrTable.setStatus(_A)
_SysSAlrEntry_Object=MibTableRow
sysSAlrEntry=_SysSAlrEntry_Object((1,3,6,1,4,1,164,3,3,1,4,1,1))
sysSAlrEntry.setIndexNames((0,_F,_Ag))
if mibBuilder.loadTexts:sysSAlrEntry.setStatus(_A)
_SysSAlrIdx_Type=Integer32
_SysSAlrIdx_Object=MibTableColumn
sysSAlrIdx=_SysSAlrIdx_Object((1,3,6,1,4,1,164,3,3,1,4,1,1,1),_SysSAlrIdx_Type())
sysSAlrIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSAlrIdx.setStatus(_A)
_SysSAlrCode_Type=Integer32
_SysSAlrCode_Object=MibTableColumn
sysSAlrCode=_SysSAlrCode_Object((1,3,6,1,4,1,164,3,3,1,4,1,1,2),_SysSAlrCode_Type())
sysSAlrCode.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSAlrCode.setStatus(_A)
class _SysSAlrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6,7)));namedValues=NamedValues(*((_n,3),(_m,4),(_k,5),(_d,6),(_o,7)))
_SysSAlrState_Type.__name__=_B
_SysSAlrState_Object=MibTableColumn
sysSAlrState=_SysSAlrState_Object((1,3,6,1,4,1,164,3,3,1,4,1,1,3),_SysSAlrState_Type())
sysSAlrState.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSAlrState.setStatus(_A)
class _SysSAlarmMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_SysSAlarmMask_Type.__name__=_B
_SysSAlarmMask_Object=MibTableColumn
sysSAlarmMask=_SysSAlarmMask_Object((1,3,6,1,4,1,164,3,3,1,4,1,1,4),_SysSAlarmMask_Type())
sysSAlarmMask.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSAlarmMask.setStatus(_A)
class _SysSAlarmInvert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_SysSAlarmInvert_Type.__name__=_B
_SysSAlarmInvert_Object=MibTableColumn
sysSAlarmInvert=_SysSAlarmInvert_Object((1,3,6,1,4,1,164,3,3,1,4,1,1,5),_SysSAlarmInvert_Type())
sysSAlarmInvert.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSAlarmInvert.setStatus(_A)
class _SysSAlarmOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_SysSAlarmOnOff_Type.__name__=_B
_SysSAlarmOnOff_Object=MibTableColumn
sysSAlarmOnOff=_SysSAlarmOnOff_Object((1,3,6,1,4,1,164,3,3,1,4,1,1,6),_SysSAlarmOnOff_Type())
sysSAlarmOnOff.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSAlarmOnOff.setStatus(_A)
_SysSAlarmCounter_Type=Integer32
_SysSAlarmCounter_Object=MibTableColumn
sysSAlarmCounter=_SysSAlarmCounter_Object((1,3,6,1,4,1,164,3,3,1,4,1,1,7),_SysSAlarmCounter_Type())
sysSAlarmCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:sysSAlarmCounter.setStatus(_A)
class _SysSAlrClearCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_SysSAlrClearCmd_Type.__name__=_B
_SysSAlrClearCmd_Object=MibScalar
sysSAlrClearCmd=_SysSAlrClearCmd_Object((1,3,6,1,4,1,164,3,3,1,4,2),_SysSAlrClearCmd_Type())
sysSAlrClearCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:sysSAlrClearCmd.setStatus(_A)
class _SysSAlrClearAllCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_SysSAlrClearAllCmd_Type.__name__=_B
_SysSAlrClearAllCmd_Object=MibScalar
sysSAlrClearAllCmd=_SysSAlrClearAllCmd_Object((1,3,6,1,4,1,164,3,3,1,4,3),_SysSAlrClearAllCmd_Type())
sysSAlrClearAllCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:sysSAlrClearAllCmd.setStatus(_A)
class _SysSAlrMaskAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_SysSAlrMaskAll_Type.__name__=_B
_SysSAlrMaskAll_Object=MibScalar
sysSAlrMaskAll=_SysSAlrMaskAll_Object((1,3,6,1,4,1,164,3,3,1,4,4),_SysSAlrMaskAll_Type())
sysSAlrMaskAll.setMaxAccess(_D)
if mibBuilder.loadTexts:sysSAlrMaskAll.setStatus(_A)
class _SysSAlrMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SysSAlrMask_Type.__name__=_l
_SysSAlrMask_Object=MibScalar
sysSAlrMask=_SysSAlrMask_Object((1,3,6,1,4,1,164,3,3,1,4,5),_SysSAlrMask_Type())
sysSAlrMask.setMaxAccess(_D)
if mibBuilder.loadTexts:sysSAlrMask.setStatus(_A)
class _SysSAlrDataUpdateCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_SysSAlrDataUpdateCmd_Type.__name__=_B
_SysSAlrDataUpdateCmd_Object=MibScalar
sysSAlrDataUpdateCmd=_SysSAlrDataUpdateCmd_Object((1,3,6,1,4,1,164,3,3,1,4,6),_SysSAlrDataUpdateCmd_Type())
sysSAlrDataUpdateCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:sysSAlrDataUpdateCmd.setStatus(_A)
_SysBufferAlr_ObjectIdentity=ObjectIdentity
sysBufferAlr=_SysBufferAlr_ObjectIdentity((1,3,6,1,4,1,164,3,3,1,5))
_SysBufferAlrTable_Object=MibTable
sysBufferAlrTable=_SysBufferAlrTable_Object((1,3,6,1,4,1,164,3,3,1,5,1))
if mibBuilder.loadTexts:sysBufferAlrTable.setStatus(_A)
_SysBufferAlrEntry_Object=MibTableRow
sysBufferAlrEntry=_SysBufferAlrEntry_Object((1,3,6,1,4,1,164,3,3,1,5,1,1))
sysBufferAlrEntry.setIndexNames((0,_F,_Ah))
if mibBuilder.loadTexts:sysBufferAlrEntry.setStatus(_A)
_SysBufferAlrIdx_Type=Integer32
_SysBufferAlrIdx_Object=MibTableColumn
sysBufferAlrIdx=_SysBufferAlrIdx_Object((1,3,6,1,4,1,164,3,3,1,5,1,1,1),_SysBufferAlrIdx_Type())
sysBufferAlrIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:sysBufferAlrIdx.setStatus(_A)
_SysBufferAlrCode_Type=Integer32
_SysBufferAlrCode_Object=MibTableColumn
sysBufferAlrCode=_SysBufferAlrCode_Object((1,3,6,1,4,1,164,3,3,1,5,1,1,2),_SysBufferAlrCode_Type())
sysBufferAlrCode.setMaxAccess(_C)
if mibBuilder.loadTexts:sysBufferAlrCode.setStatus(_A)
class _SysBufferAlrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7)));namedValues=NamedValues(*((_H,2),(_n,3),(_m,4),(_k,5),(_d,6),(_o,7)))
_SysBufferAlrState_Type.__name__=_B
_SysBufferAlrState_Object=MibTableColumn
sysBufferAlrState=_SysBufferAlrState_Object((1,3,6,1,4,1,164,3,3,1,5,1,1,3),_SysBufferAlrState_Type())
sysBufferAlrState.setMaxAccess(_C)
if mibBuilder.loadTexts:sysBufferAlrState.setStatus(_A)
class _SysBufferAlrSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,120,255)));namedValues=NamedValues(*(('psA',1),('psB',2),(_v,3),(_w,4),(_T,5),(_U,6),(_V,7),(_W,8),(_X,9),(_Y,10),(_Z,11),(_a,12),(_b,13),(_e,14),(_f,15),(_g,16),(_h,17),(_i,18),(_j,19),('local',20),('psC',21),('kmxPsA',101),('kmxPsB',102),(_A7,103),(_A8,104),('kmxCl',105),(_AT,106),(_A9,107),(_AA,108),(_AB,109),(_AC,110),(_AD,111),(_AE,112),(_AF,113),(_AG,114),(_AH,115),(_AI,116),(_AJ,117),(_AK,118),('remote',120),(_E,255)))
_SysBufferAlrSlot_Type.__name__=_B
_SysBufferAlrSlot_Object=MibTableColumn
sysBufferAlrSlot=_SysBufferAlrSlot_Object((1,3,6,1,4,1,164,3,3,1,5,1,1,4),_SysBufferAlrSlot_Type())
sysBufferAlrSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:sysBufferAlrSlot.setStatus(_A)
_SysBufferAlrPort_Type=Integer32
_SysBufferAlrPort_Object=MibTableColumn
sysBufferAlrPort=_SysBufferAlrPort_Object((1,3,6,1,4,1,164,3,3,1,5,1,1,5),_SysBufferAlrPort_Type())
sysBufferAlrPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sysBufferAlrPort.setStatus(_A)
class _SysBufferAlrDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysBufferAlrDate_Type.__name__=_J
_SysBufferAlrDate_Object=MibTableColumn
sysBufferAlrDate=_SysBufferAlrDate_Object((1,3,6,1,4,1,164,3,3,1,5,1,1,6),_SysBufferAlrDate_Type())
sysBufferAlrDate.setMaxAccess(_C)
if mibBuilder.loadTexts:sysBufferAlrDate.setStatus(_A)
class _SysBufferAlrTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysBufferAlrTime_Type.__name__=_J
_SysBufferAlrTime_Object=MibTableColumn
sysBufferAlrTime=_SysBufferAlrTime_Object((1,3,6,1,4,1,164,3,3,1,5,1,1,7),_SysBufferAlrTime_Type())
sysBufferAlrTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sysBufferAlrTime.setStatus(_A)
_SysBufferAlrUpTime_Type=TimeTicks
_SysBufferAlrUpTime_Object=MibTableColumn
sysBufferAlrUpTime=_SysBufferAlrUpTime_Object((1,3,6,1,4,1,164,3,3,1,5,1,1,8),_SysBufferAlrUpTime_Type())
sysBufferAlrUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sysBufferAlrUpTime.setStatus(_A)
_SysBufferAlrInfo_Type=SnmpAdminString
_SysBufferAlrInfo_Object=MibTableColumn
sysBufferAlrInfo=_SysBufferAlrInfo_Object((1,3,6,1,4,1,164,3,3,1,5,1,1,9),_SysBufferAlrInfo_Type())
sysBufferAlrInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:sysBufferAlrInfo.setStatus(_A)
class _SysBufferAlrClearCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_SysBufferAlrClearCmd_Type.__name__=_B
_SysBufferAlrClearCmd_Object=MibScalar
sysBufferAlrClearCmd=_SysBufferAlrClearCmd_Object((1,3,6,1,4,1,164,3,3,1,5,2),_SysBufferAlrClearCmd_Type())
sysBufferAlrClearCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:sysBufferAlrClearCmd.setStatus(_A)
_SysConfig_ObjectIdentity=ObjectIdentity
sysConfig=_SysConfig_ObjectIdentity((1,3,6,1,4,1,164,3,3,1,6))
_SysCClkSrcTable_Object=MibTable
sysCClkSrcTable=_SysCClkSrcTable_Object((1,3,6,1,4,1,164,3,3,1,6,1))
if mibBuilder.loadTexts:sysCClkSrcTable.setStatus(_A)
_SysCClkSrcEntry_Object=MibTableRow
sysCClkSrcEntry=_SysCClkSrcEntry_Object((1,3,6,1,4,1,164,3,3,1,6,1,1))
sysCClkSrcEntry.setIndexNames((0,_F,_Ai),(0,_F,_Aj))
if mibBuilder.loadTexts:sysCClkSrcEntry.setStatus(_A)
class _SysCClkCnfgIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SysCClkCnfgIdx_Type.__name__=_B
_SysCClkCnfgIdx_Object=MibTableColumn
sysCClkCnfgIdx=_SysCClkCnfgIdx_Object((1,3,6,1,4,1,164,3,3,1,6,1,1,1),_SysCClkCnfgIdx_Type())
sysCClkCnfgIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:sysCClkCnfgIdx.setStatus(_A)
class _SysCClkSrcIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('master',1),('fallback',2)))
_SysCClkSrcIdx_Type.__name__=_B
_SysCClkSrcIdx_Object=MibTableColumn
sysCClkSrcIdx=_SysCClkSrcIdx_Object((1,3,6,1,4,1,164,3,3,1,6,1,1,2),_SysCClkSrcIdx_Type())
sysCClkSrcIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:sysCClkSrcIdx.setStatus(_A)
class _SysCClkSrcMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,255)));namedValues=NamedValues(*((_c,1),(_z,2),('rxClk',3),('station',4),('lbt',5),('ntr',6),('adaptive',7),('stationB',8),('automatic',9),('system',10),('sSubSystem',11),('recovered',12),(_E,255)))
_SysCClkSrcMode_Type.__name__=_B
_SysCClkSrcMode_Object=MibTableColumn
sysCClkSrcMode=_SysCClkSrcMode_Object((1,3,6,1,4,1,164,3,3,1,6,1,1,3),_SysCClkSrcMode_Type())
sysCClkSrcMode.setMaxAccess(_D)
if mibBuilder.loadTexts:sysCClkSrcMode.setStatus(_A)
_SysCClkSrcPrt_Type=Integer32
_SysCClkSrcPrt_Object=MibTableColumn
sysCClkSrcPrt=_SysCClkSrcPrt_Object((1,3,6,1,4,1,164,3,3,1,6,1,1,4),_SysCClkSrcPrt_Type())
sysCClkSrcPrt.setMaxAccess(_D)
if mibBuilder.loadTexts:sysCClkSrcPrt.setStatus(_A)
class _SysCClkStationFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('f1544Khz',2),('f2048Khz',3)))
_SysCClkStationFreq_Type.__name__=_B
_SysCClkStationFreq_Object=MibTableColumn
sysCClkStationFreq=_SysCClkStationFreq_Object((1,3,6,1,4,1,164,3,3,1,6,1,1,5),_SysCClkStationFreq_Type())
sysCClkStationFreq.setMaxAccess(_D)
if mibBuilder.loadTexts:sysCClkStationFreq.setStatus(_A)
_SysCClkRevertiveTimeout_Type=Integer32
_SysCClkRevertiveTimeout_Object=MibTableColumn
sysCClkRevertiveTimeout=_SysCClkRevertiveTimeout_Object((1,3,6,1,4,1,164,3,3,1,6,1,1,6),_SysCClkRevertiveTimeout_Type())
sysCClkRevertiveTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:sysCClkRevertiveTimeout.setStatus(_A)
class _SysCClkStationIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),('g703',2),('rs422',3),('g703E1Unbalanced',4),('g703T1',5),('rs422T1',6)))
_SysCClkStationIf_Type.__name__=_B
_SysCClkStationIf_Object=MibTableColumn
sysCClkStationIf=_SysCClkStationIf_Object((1,3,6,1,4,1,164,3,3,1,6,1,1,7),_SysCClkStationIf_Type())
sysCClkStationIf.setMaxAccess(_D)
if mibBuilder.loadTexts:sysCClkStationIf.setStatus(_A)
class _SysCClkStationCableMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_AU,2),('yCable',3)))
_SysCClkStationCableMode_Type.__name__=_B
_SysCClkStationCableMode_Object=MibTableColumn
sysCClkStationCableMode=_SysCClkStationCableMode_Object((1,3,6,1,4,1,164,3,3,1,6,1,1,8),_SysCClkStationCableMode_Type())
sysCClkStationCableMode.setMaxAccess(_D)
if mibBuilder.loadTexts:sysCClkStationCableMode.setStatus(_A)
class _SysCClkStationOutState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_y,2),(_A0,3)))
_SysCClkStationOutState_Type.__name__=_B
_SysCClkStationOutState_Object=MibTableColumn
sysCClkStationOutState=_SysCClkStationOutState_Object((1,3,6,1,4,1,164,3,3,1,6,1,1,9),_SysCClkStationOutState_Type())
sysCClkStationOutState.setMaxAccess(_D)
if mibBuilder.loadTexts:sysCClkStationOutState.setStatus(_A)
class _SysCClkSsmBased_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_p,2),(_q,3)))
_SysCClkSsmBased_Type.__name__=_B
_SysCClkSsmBased_Object=MibTableColumn
sysCClkSsmBased=_SysCClkSsmBased_Object((1,3,6,1,4,1,164,3,3,1,6,1,1,10),_SysCClkSsmBased_Type())
sysCClkSsmBased.setMaxAccess(_D)
if mibBuilder.loadTexts:sysCClkSsmBased.setStatus(_A)
class _SysCClkSSubsystemSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4)));namedValues=NamedValues(*((_E,1),(_v,3),(_w,4)))
_SysCClkSSubsystemSlot_Type.__name__=_B
_SysCClkSSubsystemSlot_Object=MibTableColumn
sysCClkSSubsystemSlot=_SysCClkSSubsystemSlot_Object((1,3,6,1,4,1,164,3,3,1,6,1,1,11),_SysCClkSSubsystemSlot_Type())
sysCClkSSubsystemSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:sysCClkSSubsystemSlot.setStatus(_A)
_SysCClkRecoveredID_Type=Unsigned32
_SysCClkRecoveredID_Object=MibTableColumn
sysCClkRecoveredID=_SysCClkRecoveredID_Object((1,3,6,1,4,1,164,3,3,1,6,1,1,12),_SysCClkRecoveredID_Type())
sysCClkRecoveredID.setMaxAccess(_D)
if mibBuilder.loadTexts:sysCClkRecoveredID.setStatus(_A)
_SysCnfgTable_Object=MibTable
sysCnfgTable=_SysCnfgTable_Object((1,3,6,1,4,1,164,3,3,1,6,2))
if mibBuilder.loadTexts:sysCnfgTable.setStatus(_A)
_SysCnfgEntry_Object=MibTableRow
sysCnfgEntry=_SysCnfgEntry_Object((1,3,6,1,4,1,164,3,3,1,6,2,1))
sysCnfgEntry.setIndexNames((0,_F,_Ak))
if mibBuilder.loadTexts:sysCnfgEntry.setStatus(_A)
_SysCnfgIdx_Type=Integer32
_SysCnfgIdx_Object=MibTableColumn
sysCnfgIdx=_SysCnfgIdx_Object((1,3,6,1,4,1,164,3,3,1,6,2,1,1),_SysCnfgIdx_Type())
sysCnfgIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:sysCnfgIdx.setStatus(_A)
class _SysCMatrixMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('bidirectional',2),('unidirectional',3)))
_SysCMatrixMode_Type.__name__=_B
_SysCMatrixMode_Object=MibTableColumn
sysCMatrixMode=_SysCMatrixMode_Object((1,3,6,1,4,1,164,3,3,1,6,2,1,2),_SysCMatrixMode_Type())
sysCMatrixMode.setMaxAccess(_D)
if mibBuilder.loadTexts:sysCMatrixMode.setStatus(_A)
class _SysCIsdnFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('te',2),('nt',3)))
_SysCIsdnFormat_Type.__name__=_B
_SysCIsdnFormat_Object=MibTableColumn
sysCIsdnFormat=_SysCIsdnFormat_Object((1,3,6,1,4,1,164,3,3,1,6,2,1,3),_SysCIsdnFormat_Type())
sysCIsdnFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:sysCIsdnFormat.setStatus(_A)
class _SysCRoutingOnEth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_c,2),(_A1,3),(_AL,4),('rip1',5),('rip1and2',6)))
_SysCRoutingOnEth_Type.__name__=_B
_SysCRoutingOnEth_Object=MibTableColumn
sysCRoutingOnEth=_SysCRoutingOnEth_Object((1,3,6,1,4,1,164,3,3,1,6,2,1,4),_SysCRoutingOnEth_Type())
sysCRoutingOnEth.setMaxAccess(_D)
if mibBuilder.loadTexts:sysCRoutingOnEth.setStatus(_A)
class _SysCAutoConfigEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_AM,2),(_AN,3)))
_SysCAutoConfigEnable_Type.__name__=_B
_SysCAutoConfigEnable_Object=MibTableColumn
sysCAutoConfigEnable=_SysCAutoConfigEnable_Object((1,3,6,1,4,1,164,3,3,1,6,2,1,5),_SysCAutoConfigEnable_Type())
sysCAutoConfigEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:sysCAutoConfigEnable.setStatus(_A)
class _SysCIntTsAllocMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('static',2),('dynamic',3),('staticOneToOne',4)))
_SysCIntTsAllocMode_Type.__name__=_B
_SysCIntTsAllocMode_Object=MibTableColumn
sysCIntTsAllocMode=_SysCIntTsAllocMode_Object((1,3,6,1,4,1,164,3,3,1,6,2,1,6),_SysCIntTsAllocMode_Type())
sysCIntTsAllocMode.setMaxAccess(_D)
if mibBuilder.loadTexts:sysCIntTsAllocMode.setStatus(_A)
class _SysCBuPrimaryPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*(('noBackup',2),(_AZ,3),('eth',4)))
_SysCBuPrimaryPort_Type.__name__=_B
_SysCBuPrimaryPort_Object=MibTableColumn
sysCBuPrimaryPort=_SysCBuPrimaryPort_Object((1,3,6,1,4,1,164,3,3,1,6,2,1,7),_SysCBuPrimaryPort_Type())
sysCBuPrimaryPort.setMaxAccess(_D)
if mibBuilder.loadTexts:sysCBuPrimaryPort.setStatus(_A)
class _SysCEnableLanOverTdm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*(('enableAll',2),('enableVoiceOnly',3),('enableVoiceAndMng',4)))
_SysCEnableLanOverTdm_Type.__name__=_B
_SysCEnableLanOverTdm_Object=MibTableColumn
sysCEnableLanOverTdm=_SysCEnableLanOverTdm_Object((1,3,6,1,4,1,164,3,3,1,6,2,1,8),_SysCEnableLanOverTdm_Type())
sysCEnableLanOverTdm.setMaxAccess(_D)
if mibBuilder.loadTexts:sysCEnableLanOverTdm.setStatus(_A)
_SysCSs7FisuSuppression_Type=Integer32
_SysCSs7FisuSuppression_Object=MibTableColumn
sysCSs7FisuSuppression=_SysCSs7FisuSuppression_Object((1,3,6,1,4,1,164,3,3,1,6,2,1,9),_SysCSs7FisuSuppression_Type())
sysCSs7FisuSuppression.setMaxAccess(_D)
if mibBuilder.loadTexts:sysCSs7FisuSuppression.setStatus(_A)
class _SysCBuRecMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_x,2),(_AV,3)))
_SysCBuRecMode_Type.__name__=_B
_SysCBuRecMode_Object=MibTableColumn
sysCBuRecMode=_SysCBuRecMode_Object((1,3,6,1,4,1,164,3,3,1,6,2,1,10),_SysCBuRecMode_Type())
sysCBuRecMode.setMaxAccess(_D)
if mibBuilder.loadTexts:sysCBuRecMode.setStatus(_A)
_SysCRdnTable_Object=MibTable
sysCRdnTable=_SysCRdnTable_Object((1,3,6,1,4,1,164,3,3,1,6,3))
if mibBuilder.loadTexts:sysCRdnTable.setStatus(_A)
_SysCRdnEntry_Object=MibTableRow
sysCRdnEntry=_SysCRdnEntry_Object((1,3,6,1,4,1,164,3,3,1,6,3,1))
sysCRdnEntry.setIndexNames((0,_F,_Al),(0,_F,_AR),(0,_F,_AS))
if mibBuilder.loadTexts:sysCRdnEntry.setStatus(_A)
_SysCRdnCnfgIdx_Type=Integer32
_SysCRdnCnfgIdx_Object=MibTableColumn
sysCRdnCnfgIdx=_SysCRdnCnfgIdx_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,1),_SysCRdnCnfgIdx_Type())
sysCRdnCnfgIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:sysCRdnCnfgIdx.setStatus(_A)
class _SysCRdnPrimeSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,255)));namedValues=NamedValues(*((_T,5),(_U,6),(_V,7),(_W,8),(_X,9),(_Y,10),(_Z,11),(_a,12),(_b,13),(_e,14),(_f,15),(_g,16),(_h,17),(_i,18),(_j,19),(_E,255)))
_SysCRdnPrimeSlot_Type.__name__=_B
_SysCRdnPrimeSlot_Object=MibTableColumn
sysCRdnPrimeSlot=_SysCRdnPrimeSlot_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,2),_SysCRdnPrimeSlot_Type())
sysCRdnPrimeSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:sysCRdnPrimeSlot.setStatus(_A)
_SysCRdnPrimePort_Type=Integer32
_SysCRdnPrimePort_Object=MibTableColumn
sysCRdnPrimePort=_SysCRdnPrimePort_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,3),_SysCRdnPrimePort_Type())
sysCRdnPrimePort.setMaxAccess(_C)
if mibBuilder.loadTexts:sysCRdnPrimePort.setStatus(_A)
class _SysCRdnSecSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,255)));namedValues=NamedValues(*((_T,5),(_U,6),(_V,7),(_W,8),(_X,9),(_Y,10),(_Z,11),(_a,12),(_b,13),(_e,14),(_f,15),(_g,16),(_h,17),(_i,18),(_j,19),(_E,255)))
_SysCRdnSecSlot_Type.__name__=_B
_SysCRdnSecSlot_Object=MibTableColumn
sysCRdnSecSlot=_SysCRdnSecSlot_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,4),_SysCRdnSecSlot_Type())
sysCRdnSecSlot.setMaxAccess(_K)
if mibBuilder.loadTexts:sysCRdnSecSlot.setStatus(_A)
_SysCRdnSecPort_Type=Integer32
_SysCRdnSecPort_Object=MibTableColumn
sysCRdnSecPort=_SysCRdnSecPort_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,5),_SysCRdnSecPort_Type())
sysCRdnSecPort.setMaxAccess(_K)
if mibBuilder.loadTexts:sysCRdnSecPort.setStatus(_A)
class _SysCRdnMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('dualCableAIS',2),('yCable',3),('dualCableParallelTx',4),('backup',5),('singleSlotProtection',6),('onePlusOne',7),('oneToOne',8),(_Am,9),(_AV,10),('onePlusOneBid',11),('onePlusOneOpt',12),('ds0SncProtection',13)))
_SysCRdnMode_Type.__name__=_B
_SysCRdnMode_Object=MibTableColumn
sysCRdnMode=_SysCRdnMode_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,6),_SysCRdnMode_Type())
sysCRdnMode.setMaxAccess(_K)
if mibBuilder.loadTexts:sysCRdnMode.setStatus(_A)
class _SysCRdnRecMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_x,2),(_AV,3),('nonRevertive',4)))
_SysCRdnRecMode_Type.__name__=_B
_SysCRdnRecMode_Object=MibTableColumn
sysCRdnRecMode=_SysCRdnRecMode_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,7),_SysCRdnRecMode_Type())
sysCRdnRecMode.setMaxAccess(_K)
if mibBuilder.loadTexts:sysCRdnRecMode.setStatus(_A)
_SysCRdnRecTime_Type=Integer32
_SysCRdnRecTime_Object=MibTableColumn
sysCRdnRecTime=_SysCRdnRecTime_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,8),_SysCRdnRecTime_Type())
sysCRdnRecTime.setMaxAccess(_K)
if mibBuilder.loadTexts:sysCRdnRecTime.setStatus(_A)
class _SysCRdnHwSwFlip_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('hw',2),('sw',3)))
_SysCRdnHwSwFlip_Type.__name__=_B
_SysCRdnHwSwFlip_Object=MibTableColumn
sysCRdnHwSwFlip=_SysCRdnHwSwFlip_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,9),_SysCRdnHwSwFlip_Type())
sysCRdnHwSwFlip.setMaxAccess(_K)
if mibBuilder.loadTexts:sysCRdnHwSwFlip.setStatus(_A)
_SysCRdnRowStatus_Type=RowStatus
_SysCRdnRowStatus_Object=MibTableColumn
sysCRdnRowStatus=_SysCRdnRowStatus_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,10),_SysCRdnRowStatus_Type())
sysCRdnRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:sysCRdnRowStatus.setStatus(_A)
class _SysCRdnOnline_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_AP,2),(_AQ,3)))
_SysCRdnOnline_Type.__name__=_B
_SysCRdnOnline_Object=MibTableColumn
sysCRdnOnline=_SysCRdnOnline_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,11),_SysCRdnOnline_Type())
sysCRdnOnline.setMaxAccess(_C)
if mibBuilder.loadTexts:sysCRdnOnline.setStatus(_A)
class _SysCRdnSwitchingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('biDirectional',2),('uniDirectional',3),(_Am,4)))
_SysCRdnSwitchingMode_Type.__name__=_B
_SysCRdnSwitchingMode_Object=MibTableColumn
sysCRdnSwitchingMode=_SysCRdnSwitchingMode_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,12),_SysCRdnSwitchingMode_Type())
sysCRdnSwitchingMode.setMaxAccess(_K)
if mibBuilder.loadTexts:sysCRdnSwitchingMode.setStatus(_A)
_SysCRdnFlipUponEvent_Type=Integer32
_SysCRdnFlipUponEvent_Object=MibTableColumn
sysCRdnFlipUponEvent=_SysCRdnFlipUponEvent_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,13),_SysCRdnFlipUponEvent_Type())
sysCRdnFlipUponEvent.setMaxAccess(_K)
if mibBuilder.loadTexts:sysCRdnFlipUponEvent.setStatus(_A)
_SysCRdnLosOrLofTime_Type=Integer32
_SysCRdnLosOrLofTime_Object=MibTableColumn
sysCRdnLosOrLofTime=_SysCRdnLosOrLofTime_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,14),_SysCRdnLosOrLofTime_Type())
sysCRdnLosOrLofTime.setMaxAccess(_K)
if mibBuilder.loadTexts:sysCRdnLosOrLofTime.setStatus(_A)
_SysCRdnEventsTimeWindow_Type=Integer32
_SysCRdnEventsTimeWindow_Object=MibTableColumn
sysCRdnEventsTimeWindow=_SysCRdnEventsTimeWindow_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,15),_SysCRdnEventsTimeWindow_Type())
sysCRdnEventsTimeWindow.setMaxAccess(_K)
if mibBuilder.loadTexts:sysCRdnEventsTimeWindow.setStatus(_A)
_SysCRdnSequenceNumberThreshold_Type=Integer32
_SysCRdnSequenceNumberThreshold_Object=MibTableColumn
sysCRdnSequenceNumberThreshold=_SysCRdnSequenceNumberThreshold_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,16),_SysCRdnSequenceNumberThreshold_Type())
sysCRdnSequenceNumberThreshold.setMaxAccess(_K)
if mibBuilder.loadTexts:sysCRdnSequenceNumberThreshold.setStatus(_A)
_SysCRdnBufferErrorsThreshold_Type=Integer32
_SysCRdnBufferErrorsThreshold_Object=MibTableColumn
sysCRdnBufferErrorsThreshold=_SysCRdnBufferErrorsThreshold_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,17),_SysCRdnBufferErrorsThreshold_Type())
sysCRdnBufferErrorsThreshold.setMaxAccess(_K)
if mibBuilder.loadTexts:sysCRdnBufferErrorsThreshold.setStatus(_A)
_SysCRdnBuffUnderrunTime_Type=Integer32
_SysCRdnBuffUnderrunTime_Object=MibTableColumn
sysCRdnBuffUnderrunTime=_SysCRdnBuffUnderrunTime_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,18),_SysCRdnBuffUnderrunTime_Type())
sysCRdnBuffUnderrunTime.setMaxAccess(_K)
if mibBuilder.loadTexts:sysCRdnBuffUnderrunTime.setStatus(_A)
class _SysCRdnPrimePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('low',2),(_AO,3)))
_SysCRdnPrimePriority_Type.__name__=_B
_SysCRdnPrimePriority_Object=MibTableColumn
sysCRdnPrimePriority=_SysCRdnPrimePriority_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,19),_SysCRdnPrimePriority_Type())
sysCRdnPrimePriority.setMaxAccess(_K)
if mibBuilder.loadTexts:sysCRdnPrimePriority.setStatus(_A)
class _SysCRdnSecPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('low',2),(_AO,3)))
_SysCRdnSecPriority_Type.__name__=_B
_SysCRdnSecPriority_Object=MibTableColumn
sysCRdnSecPriority=_SysCRdnSecPriority_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,20),_SysCRdnSecPriority_Type())
sysCRdnSecPriority.setMaxAccess(_K)
if mibBuilder.loadTexts:sysCRdnSecPriority.setStatus(_A)
_SysCRdnWTR_Type=Unsigned32
_SysCRdnWTR_Object=MibTableColumn
sysCRdnWTR=_SysCRdnWTR_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,21),_SysCRdnWTR_Type())
sysCRdnWTR.setMaxAccess(_K)
if mibBuilder.loadTexts:sysCRdnWTR.setStatus(_A)
_SysCRdnName_Type=SnmpAdminString
_SysCRdnName_Object=MibTableColumn
sysCRdnName=_SysCRdnName_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,22),_SysCRdnName_Type())
sysCRdnName.setMaxAccess(_K)
if mibBuilder.loadTexts:sysCRdnName.setStatus(_A)
class _SysCRdnTxDownDurationUponFlip_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_SysCRdnTxDownDurationUponFlip_Type.__name__=_A4
_SysCRdnTxDownDurationUponFlip_Object=MibTableColumn
sysCRdnTxDownDurationUponFlip=_SysCRdnTxDownDurationUponFlip_Object((1,3,6,1,4,1,164,3,3,1,6,3,1,23),_SysCRdnTxDownDurationUponFlip_Type())
sysCRdnTxDownDurationUponFlip.setMaxAccess(_K)
if mibBuilder.loadTexts:sysCRdnTxDownDurationUponFlip.setStatus(_A)
_SysDbase_ObjectIdentity=ObjectIdentity
sysDbase=_SysDbase_ObjectIdentity((1,3,6,1,4,1,164,3,3,1,7))
class _SysDbaseSanityCheckCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_SysDbaseSanityCheckCmd_Type.__name__=_B
_SysDbaseSanityCheckCmd_Object=MibScalar
sysDbaseSanityCheckCmd=_SysDbaseSanityCheckCmd_Object((1,3,6,1,4,1,164,3,3,1,7,1),_SysDbaseSanityCheckCmd_Type())
sysDbaseSanityCheckCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:sysDbaseSanityCheckCmd.setStatus(_A)
class _SysDbaseDownloadCnfgIdxCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SysDbaseDownloadCnfgIdxCmd_Type.__name__=_B
_SysDbaseDownloadCnfgIdxCmd_Object=MibScalar
sysDbaseDownloadCnfgIdxCmd=_SysDbaseDownloadCnfgIdxCmd_Object((1,3,6,1,4,1,164,3,3,1,7,2),_SysDbaseDownloadCnfgIdxCmd_Type())
sysDbaseDownloadCnfgIdxCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:sysDbaseDownloadCnfgIdxCmd.setStatus(_A)
class _SysDbaseUploadCnfgIdxCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SysDbaseUploadCnfgIdxCmd_Type.__name__=_B
_SysDbaseUploadCnfgIdxCmd_Object=MibScalar
sysDbaseUploadCnfgIdxCmd=_SysDbaseUploadCnfgIdxCmd_Object((1,3,6,1,4,1,164,3,3,1,7,3),_SysDbaseUploadCnfgIdxCmd_Type())
sysDbaseUploadCnfgIdxCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:sysDbaseUploadCnfgIdxCmd.setStatus(_A)
_SysDbaseFlipTable_Object=MibTable
sysDbaseFlipTable=_SysDbaseFlipTable_Object((1,3,6,1,4,1,164,3,3,1,7,4))
if mibBuilder.loadTexts:sysDbaseFlipTable.setStatus(_A)
_SysDbaseFlipEntry_Object=MibTableRow
sysDbaseFlipEntry=_SysDbaseFlipEntry_Object((1,3,6,1,4,1,164,3,3,1,7,4,1))
sysDbaseFlipEntry.setIndexNames((0,_F,_An))
if mibBuilder.loadTexts:sysDbaseFlipEntry.setStatus(_A)
class _SysDbaseFlipIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SysDbaseFlipIdx_Type.__name__=_B
_SysDbaseFlipIdx_Object=MibTableColumn
sysDbaseFlipIdx=_SysDbaseFlipIdx_Object((1,3,6,1,4,1,164,3,3,1,7,4,1,1),_SysDbaseFlipIdx_Type())
sysDbaseFlipIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:sysDbaseFlipIdx.setStatus(_A)
class _SysDbaseFlipTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysDbaseFlipTime_Type.__name__=_J
_SysDbaseFlipTime_Object=MibTableColumn
sysDbaseFlipTime=_SysDbaseFlipTime_Object((1,3,6,1,4,1,164,3,3,1,7,4,1,2),_SysDbaseFlipTime_Type())
sysDbaseFlipTime.setMaxAccess(_D)
if mibBuilder.loadTexts:sysDbaseFlipTime.setStatus(_A)
class _SysDbaseFlipActivation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_AM,1),(_AN,2)))
_SysDbaseFlipActivation_Type.__name__=_B
_SysDbaseFlipActivation_Object=MibTableColumn
sysDbaseFlipActivation=_SysDbaseFlipActivation_Object((1,3,6,1,4,1,164,3,3,1,7,4,1,3),_SysDbaseFlipActivation_Type())
sysDbaseFlipActivation.setMaxAccess(_D)
if mibBuilder.loadTexts:sysDbaseFlipActivation.setStatus(_A)
_MdlDacsMux_ObjectIdentity=ObjectIdentity
mdlDacsMux=_MdlDacsMux_ObjectIdentity((1,3,6,1,4,1,164,3,3,2))
_MdlGen_ObjectIdentity=ObjectIdentity
mdlGen=_MdlGen_ObjectIdentity((1,3,6,1,4,1,164,3,3,2,1))
_CardEvents_ObjectIdentity=ObjectIdentity
cardEvents=_CardEvents_ObjectIdentity((1,3,6,1,4,1,164,3,3,2,1,0))
_MdlSTable_Object=MibTable
mdlSTable=_MdlSTable_Object((1,3,6,1,4,1,164,3,3,2,1,1))
if mibBuilder.loadTexts:mdlSTable.setStatus(_A)
_MdlSEntry_Object=MibTableRow
mdlSEntry=_MdlSEntry_Object((1,3,6,1,4,1,164,3,3,2,1,1,1))
mdlSEntry.setIndexNames((0,_F,_Ao))
if mibBuilder.loadTexts:mdlSEntry.setStatus(_A)
_MdlSSltIdx_Type=SlotType
_MdlSSltIdx_Object=MibTableColumn
mdlSSltIdx=_MdlSSltIdx_Object((1,3,6,1,4,1,164,3,3,2,1,1,1,1),_MdlSSltIdx_Type())
mdlSSltIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlSSltIdx.setStatus(_A)
_MdlSCardType_Type=CardType
_MdlSCardType_Object=MibTableColumn
mdlSCardType=_MdlSCardType_Object((1,3,6,1,4,1,164,3,3,2,1,1,1,2),_MdlSCardType_Type())
mdlSCardType.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlSCardType.setStatus(_A)
class _MdlSHwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MdlSHwVer_Type.__name__=_J
_MdlSHwVer_Object=MibTableColumn
mdlSHwVer=_MdlSHwVer_Object((1,3,6,1,4,1,164,3,3,2,1,1,1,3),_MdlSHwVer_Type())
mdlSHwVer.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlSHwVer.setStatus(_A)
class _MdlSSwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MdlSSwVer_Type.__name__=_J
_MdlSSwVer_Object=MibTableColumn
mdlSSwVer=_MdlSSwVer_Object((1,3,6,1,4,1,164,3,3,2,1,1,1,4),_MdlSSwVer_Type())
mdlSSwVer.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlSSwVer.setStatus(_A)
class _MdlSAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7)));namedValues=NamedValues(*((_H,2),(_k,3),(_m,4),(_n,5),(_d,6),(_o,7)))
_MdlSAlarmStatus_Type.__name__=_B
_MdlSAlarmStatus_Object=MibTableColumn
mdlSAlarmStatus=_MdlSAlarmStatus_Object((1,3,6,1,4,1,164,3,3,2,1,1,1,5),_MdlSAlarmStatus_Type())
mdlSAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlSAlarmStatus.setStatus(_A)
class _MdlSAlarmStatusAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7)));namedValues=NamedValues(*((_H,2),(_k,3),(_m,4),(_n,5),(_d,6),(_o,7)))
_MdlSAlarmStatusAll_Type.__name__=_B
_MdlSAlarmStatusAll_Object=MibTableColumn
mdlSAlarmStatusAll=_MdlSAlarmStatusAll_Object((1,3,6,1,4,1,164,3,3,2,1,1,1,6),_MdlSAlarmStatusAll_Type())
mdlSAlarmStatusAll.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlSAlarmStatusAll.setStatus(_A)
class _MdlSTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_MdlSTestStatus_Type.__name__=_B
_MdlSTestStatus_Object=MibTableColumn
mdlSTestStatus=_MdlSTestStatus_Object((1,3,6,1,4,1,164,3,3,2,1,1,1,7),_MdlSTestStatus_Type())
mdlSTestStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlSTestStatus.setStatus(_A)
class _MdlSHwStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('fail',2),('ok',3)))
_MdlSHwStatus_Type.__name__=_B
_MdlSHwStatus_Object=MibTableColumn
mdlSHwStatus=_MdlSHwStatus_Object((1,3,6,1,4,1,164,3,3,2,1,1,1,8),_MdlSHwStatus_Type())
mdlSHwStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlSHwStatus.setStatus(_A)
class _MdlSActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('offline',2),('online',3)))
_MdlSActivity_Type.__name__=_B
_MdlSActivity_Object=MibTableColumn
mdlSActivity=_MdlSActivity_Object((1,3,6,1,4,1,164,3,3,2,1,1,1,9),_MdlSActivity_Type())
mdlSActivity.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlSActivity.setStatus(_A)
class _MdlSAlrClearCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_MdlSAlrClearCmd_Type.__name__=_B
_MdlSAlrClearCmd_Object=MibTableColumn
mdlSAlrClearCmd=_MdlSAlrClearCmd_Object((1,3,6,1,4,1,164,3,3,2,1,1,1,10),_MdlSAlrClearCmd_Type())
mdlSAlrClearCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:mdlSAlrClearCmd.setStatus(_A)
class _MdlSAlrClearAllCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_MdlSAlrClearAllCmd_Type.__name__=_B
_MdlSAlrClearAllCmd_Object=MibTableColumn
mdlSAlrClearAllCmd=_MdlSAlrClearAllCmd_Object((1,3,6,1,4,1,164,3,3,2,1,1,1,11),_MdlSAlrClearAllCmd_Type())
mdlSAlrClearAllCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:mdlSAlrClearAllCmd.setStatus(_A)
class _MdlSAlrMaskAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_MdlSAlrMaskAll_Type.__name__=_B
_MdlSAlrMaskAll_Object=MibTableColumn
mdlSAlrMaskAll=_MdlSAlrMaskAll_Object((1,3,6,1,4,1,164,3,3,2,1,1,1,12),_MdlSAlrMaskAll_Type())
mdlSAlrMaskAll.setMaxAccess(_D)
if mibBuilder.loadTexts:mdlSAlrMaskAll.setStatus(_A)
_MdlSCmd_Type=Integer32
_MdlSCmd_Object=MibTableColumn
mdlSCmd=_MdlSCmd_Object((1,3,6,1,4,1,164,3,3,2,1,1,1,13),_MdlSCmd_Type())
mdlSCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:mdlSCmd.setStatus(_A)
class _MdlSReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_MdlSReset_Type.__name__=_B
_MdlSReset_Object=MibTableColumn
mdlSReset=_MdlSReset_Object((1,3,6,1,4,1,164,3,3,2,1,1,1,14),_MdlSReset_Type())
mdlSReset.setMaxAccess(_D)
if mibBuilder.loadTexts:mdlSReset.setStatus(_A)
class _MdlSRebuildFrame_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_H,2),(_I,3)))
_MdlSRebuildFrame_Type.__name__=_B
_MdlSRebuildFrame_Object=MibTableColumn
mdlSRebuildFrame=_MdlSRebuildFrame_Object((1,3,6,1,4,1,164,3,3,2,1,1,1,15),_MdlSRebuildFrame_Type())
mdlSRebuildFrame.setMaxAccess(_D)
if mibBuilder.loadTexts:mdlSRebuildFrame.setStatus(_A)
class _MdlSBackupSwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MdlSBackupSwVer_Type.__name__=_J
_MdlSBackupSwVer_Object=MibTableColumn
mdlSBackupSwVer=_MdlSBackupSwVer_Object((1,3,6,1,4,1,164,3,3,2,1,1,1,16),_MdlSBackupSwVer_Type())
mdlSBackupSwVer.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlSBackupSwVer.setStatus(_A)
class _MdlSSecondaryBackupSwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MdlSSecondaryBackupSwVer_Type.__name__=_J
_MdlSSecondaryBackupSwVer_Object=MibTableColumn
mdlSSecondaryBackupSwVer=_MdlSSecondaryBackupSwVer_Object((1,3,6,1,4,1,164,3,3,2,1,1,1,17),_MdlSSecondaryBackupSwVer_Type())
mdlSSecondaryBackupSwVer.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlSSecondaryBackupSwVer.setStatus(_A)
class _MdlSPiggybackVer_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MdlSPiggybackVer_Type.__name__=_AY
_MdlSPiggybackVer_Object=MibTableColumn
mdlSPiggybackVer=_MdlSPiggybackVer_Object((1,3,6,1,4,1,164,3,3,2,1,1,1,18),_MdlSPiggybackVer_Type())
mdlSPiggybackVer.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlSPiggybackVer.setStatus(_A)
_MdlCTable_Object=MibTable
mdlCTable=_MdlCTable_Object((1,3,6,1,4,1,164,3,3,2,1,2))
if mibBuilder.loadTexts:mdlCTable.setStatus(_A)
_MdlCEntry_Object=MibTableRow
mdlCEntry=_MdlCEntry_Object((1,3,6,1,4,1,164,3,3,2,1,2,1))
mdlCEntry.setIndexNames((0,_F,_Ap),(0,_F,_Aq))
if mibBuilder.loadTexts:mdlCEntry.setStatus(_A)
class _MdlCConfigIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_MdlCConfigIdx_Type.__name__=_B
_MdlCConfigIdx_Object=MibTableColumn
mdlCConfigIdx=_MdlCConfigIdx_Object((1,3,6,1,4,1,164,3,3,2,1,2,1,1),_MdlCConfigIdx_Type())
mdlCConfigIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlCConfigIdx.setStatus(_A)
_MdlCSlotIdx_Type=SlotType
_MdlCSlotIdx_Object=MibTableColumn
mdlCSlotIdx=_MdlCSlotIdx_Object((1,3,6,1,4,1,164,3,3,2,1,2,1,2),_MdlCSlotIdx_Type())
mdlCSlotIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlCSlotIdx.setStatus(_A)
_MdlCProgCardType_Type=CardType
_MdlCProgCardType_Object=MibTableColumn
mdlCProgCardType=_MdlCProgCardType_Object((1,3,6,1,4,1,164,3,3,2,1,2,1,3),_MdlCProgCardType_Type())
mdlCProgCardType.setMaxAccess(_D)
if mibBuilder.loadTexts:mdlCProgCardType.setStatus(_A)
_MdlCNoOfExtPrt_Type=Integer32
_MdlCNoOfExtPrt_Object=MibTableColumn
mdlCNoOfExtPrt=_MdlCNoOfExtPrt_Object((1,3,6,1,4,1,164,3,3,2,1,2,1,4),_MdlCNoOfExtPrt_Type())
mdlCNoOfExtPrt.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlCNoOfExtPrt.setStatus(_A)
_MdlCNoOfIntPrt_Type=Integer32
_MdlCNoOfIntPrt_Object=MibTableColumn
mdlCNoOfIntPrt=_MdlCNoOfIntPrt_Object((1,3,6,1,4,1,164,3,3,2,1,2,1,5),_MdlCNoOfIntPrt_Type())
mdlCNoOfIntPrt.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlCNoOfIntPrt.setStatus(_A)
_MdlCParam_Type=Integer32
_MdlCParam_Object=MibTableColumn
mdlCParam=_MdlCParam_Object((1,3,6,1,4,1,164,3,3,2,1,2,1,6),_MdlCParam_Type())
mdlCParam.setMaxAccess(_D)
if mibBuilder.loadTexts:mdlCParam.setStatus(_A)
class _MdlCAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_A2,2)))
_MdlCAdminStatus_Type.__name__=_B
_MdlCAdminStatus_Object=MibTableColumn
mdlCAdminStatus=_MdlCAdminStatus_Object((1,3,6,1,4,1,164,3,3,2,1,2,1,7),_MdlCAdminStatus_Type())
mdlCAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mdlCAdminStatus.setStatus(_A)
_MdlCActualCardType_Type=CardType
_MdlCActualCardType_Object=MibTableColumn
mdlCActualCardType=_MdlCActualCardType_Object((1,3,6,1,4,1,164,3,3,2,1,2,1,8),_MdlCActualCardType_Type())
mdlCActualCardType.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlCActualCardType.setStatus(_A)
class _MdlCOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),(_A2,2),(_Ar,3)))
_MdlCOperStatus_Type.__name__=_B
_MdlCOperStatus_Object=MibTableColumn
mdlCOperStatus=_MdlCOperStatus_Object((1,3,6,1,4,1,164,3,3,2,1,2,1,9),_MdlCOperStatus_Type())
mdlCOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlCOperStatus.setStatus(_A)
class _MdlCDetailedStatus_Type(Bits):namedValues=NamedValues(*(('initializing',0),(_As,1),('initFailed',2),('provisionFailed',3),('selfTestFailed',4),('commFailure',5),('bpInterfaceFailure',6),('configurationMismatch',7),('noInputPower',8)))
_MdlCDetailedStatus_Type.__name__='Bits'
_MdlCDetailedStatus_Object=MibTableColumn
mdlCDetailedStatus=_MdlCDetailedStatus_Object((1,3,6,1,4,1,164,3,3,2,1,2,1,10),_MdlCDetailedStatus_Type())
mdlCDetailedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlCDetailedStatus.setStatus(_A)
_MdlCEntPhysicalIndex_Type=PhysicalIndexOrZero
_MdlCEntPhysicalIndex_Object=MibTableColumn
mdlCEntPhysicalIndex=_MdlCEntPhysicalIndex_Object((1,3,6,1,4,1,164,3,3,2,1,2,1,11),_MdlCEntPhysicalIndex_Type())
mdlCEntPhysicalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlCEntPhysicalIndex.setStatus(_A)
class _MdlCReset_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_MdlCReset_Type.__name__=_B
_MdlCReset_Object=MibTableColumn
mdlCReset=_MdlCReset_Object((1,3,6,1,4,1,164,3,3,2,1,2,1,12),_MdlCReset_Type())
mdlCReset.setMaxAccess(_D)
if mibBuilder.loadTexts:mdlCReset.setStatus(_A)
class _MdlCConfigMismatchReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,2147483647)));namedValues=NamedValues(*(('s128KbpsInSynchronousMode',1),('s14k4KbpsConfiguration',2),('s28k8KbpsConfiguration',3),('s48KbpsConfiguration',4),('s56KbpsInSynchronousMode',5),('s7k2KbpsConfiguration',6),('adpcmConfiguration',7),('dceOnDteHwInSynchronousMode',8),('dteOnDceHwInSynchronousMode',9),('rlbLlbInV110RateAdaptation',10),('swNotSupportingAdvancedSignaling',11),('signalingConfiguration',12),('stratum1WithoutOcxo',13),('stratum2WithoutOcxo',14),('useOf4TdmBusesInChassis',15),('winkStartModeConfiguration',16),(_s,2147483647)))
_MdlCConfigMismatchReason_Type.__name__=_B
_MdlCConfigMismatchReason_Object=MibTableColumn
mdlCConfigMismatchReason=_MdlCConfigMismatchReason_Object((1,3,6,1,4,1,164,3,3,2,1,2,1,13),_MdlCConfigMismatchReason_Type())
mdlCConfigMismatchReason.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlCConfigMismatchReason.setStatus(_A)
_MdlCIpAddressType_Type=InetAddressType
_MdlCIpAddressType_Object=MibTableColumn
mdlCIpAddressType=_MdlCIpAddressType_Object((1,3,6,1,4,1,164,3,3,2,1,2,1,14),_MdlCIpAddressType_Type())
mdlCIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:mdlCIpAddressType.setStatus(_A)
_MdlCIpAddress_Type=InetAddress
_MdlCIpAddress_Object=MibTableColumn
mdlCIpAddress=_MdlCIpAddress_Object((1,3,6,1,4,1,164,3,3,2,1,2,1,15),_MdlCIpAddress_Type())
mdlCIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:mdlCIpAddress.setStatus(_A)
class _MdlCHardwareFailureReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_s,1),('ringerVoltageFailure',2),('fanFailure',3)))
_MdlCHardwareFailureReason_Type.__name__=_B
_MdlCHardwareFailureReason_Object=MibTableColumn
mdlCHardwareFailureReason=_MdlCHardwareFailureReason_Object((1,3,6,1,4,1,164,3,3,2,1,2,1,16),_MdlCHardwareFailureReason_Type())
mdlCHardwareFailureReason.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlCHardwareFailureReason.setStatus(_A)
class _MdlCFanControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_A2,2)))
_MdlCFanControl_Type.__name__=_B
_MdlCFanControl_Object=MibTableColumn
mdlCFanControl=_MdlCFanControl_Object((1,3,6,1,4,1,164,3,3,2,1,2,1,22),_MdlCFanControl_Type())
mdlCFanControl.setMaxAccess(_D)
if mibBuilder.loadTexts:mdlCFanControl.setStatus(_A)
class _MdlCFanOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),(_A2,2),(_Ar,3)))
_MdlCFanOperStatus_Type.__name__=_B
_MdlCFanOperStatus_Object=MibTableColumn
mdlCFanOperStatus=_MdlCFanOperStatus_Object((1,3,6,1,4,1,164,3,3,2,1,2,1,23),_MdlCFanOperStatus_Type())
mdlCFanOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlCFanOperStatus.setStatus(_A)
_MdlAlr_ObjectIdentity=ObjectIdentity
mdlAlr=_MdlAlr_ObjectIdentity((1,3,6,1,4,1,164,3,3,2,1,3))
_MdlAlrTable_Object=MibTable
mdlAlrTable=_MdlAlrTable_Object((1,3,6,1,4,1,164,3,3,2,1,3,1))
if mibBuilder.loadTexts:mdlAlrTable.setStatus(_A)
_MdlAlrEntry_Object=MibTableRow
mdlAlrEntry=_MdlAlrEntry_Object((1,3,6,1,4,1,164,3,3,2,1,3,1,1))
mdlAlrEntry.setIndexNames((0,_F,_At),(0,_F,_Au))
if mibBuilder.loadTexts:mdlAlrEntry.setStatus(_A)
_MdlAlrIdx_Type=Integer32
_MdlAlrIdx_Object=MibTableColumn
mdlAlrIdx=_MdlAlrIdx_Object((1,3,6,1,4,1,164,3,3,2,1,3,1,1,1),_MdlAlrIdx_Type())
mdlAlrIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlAlrIdx.setStatus(_A)
_MdlAlrSltIdx_Type=SlotType
_MdlAlrSltIdx_Object=MibTableColumn
mdlAlrSltIdx=_MdlAlrSltIdx_Object((1,3,6,1,4,1,164,3,3,2,1,3,1,1,2),_MdlAlrSltIdx_Type())
mdlAlrSltIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlAlrSltIdx.setStatus(_A)
_MdlAlrCode_Type=Integer32
_MdlAlrCode_Object=MibTableColumn
mdlAlrCode=_MdlAlrCode_Object((1,3,6,1,4,1,164,3,3,2,1,3,1,1,3),_MdlAlrCode_Type())
mdlAlrCode.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlAlrCode.setStatus(_A)
class _MdlAlrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6,7)));namedValues=NamedValues(*((_n,3),(_m,4),(_k,5),(_d,6),(_o,7)))
_MdlAlrState_Type.__name__=_B
_MdlAlrState_Object=MibTableColumn
mdlAlrState=_MdlAlrState_Object((1,3,6,1,4,1,164,3,3,2,1,3,1,1,4),_MdlAlrState_Type())
mdlAlrState.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlAlrState.setStatus(_A)
class _MdlAlarmMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_MdlAlarmMask_Type.__name__=_B
_MdlAlarmMask_Object=MibTableColumn
mdlAlarmMask=_MdlAlarmMask_Object((1,3,6,1,4,1,164,3,3,2,1,3,1,1,5),_MdlAlarmMask_Type())
mdlAlarmMask.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlAlarmMask.setStatus(_A)
class _MdlAlarmInvert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_MdlAlarmInvert_Type.__name__=_B
_MdlAlarmInvert_Object=MibTableColumn
mdlAlarmInvert=_MdlAlarmInvert_Object((1,3,6,1,4,1,164,3,3,2,1,3,1,1,6),_MdlAlarmInvert_Type())
mdlAlarmInvert.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlAlarmInvert.setStatus(_A)
class _MdlAlarmOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_MdlAlarmOnOff_Type.__name__=_B
_MdlAlarmOnOff_Object=MibTableColumn
mdlAlarmOnOff=_MdlAlarmOnOff_Object((1,3,6,1,4,1,164,3,3,2,1,3,1,1,7),_MdlAlarmOnOff_Type())
mdlAlarmOnOff.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlAlarmOnOff.setStatus(_A)
_MdlAlarmCounter_Type=Integer32
_MdlAlarmCounter_Object=MibTableColumn
mdlAlarmCounter=_MdlAlarmCounter_Object((1,3,6,1,4,1,164,3,3,2,1,3,1,1,8),_MdlAlarmCounter_Type())
mdlAlarmCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlAlarmCounter.setStatus(_A)
_MdlAlrMaskTable_Object=MibTable
mdlAlrMaskTable=_MdlAlrMaskTable_Object((1,3,6,1,4,1,164,3,3,2,1,3,2))
if mibBuilder.loadTexts:mdlAlrMaskTable.setStatus(_A)
_MdlAlrMaskEntry_Object=MibTableRow
mdlAlrMaskEntry=_MdlAlrMaskEntry_Object((1,3,6,1,4,1,164,3,3,2,1,3,2,1))
mdlAlrMaskEntry.setIndexNames((0,_F,_Av))
if mibBuilder.loadTexts:mdlAlrMaskEntry.setStatus(_A)
_MdlAlrMaskSltIdx_Type=SlotType
_MdlAlrMaskSltIdx_Object=MibTableColumn
mdlAlrMaskSltIdx=_MdlAlrMaskSltIdx_Object((1,3,6,1,4,1,164,3,3,2,1,3,2,1,1),_MdlAlrMaskSltIdx_Type())
mdlAlrMaskSltIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlAlrMaskSltIdx.setStatus(_A)
class _MdlAlrMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,10))
_MdlAlrMask_Type.__name__=_l
_MdlAlrMask_Object=MibTableColumn
mdlAlrMask=_MdlAlrMask_Object((1,3,6,1,4,1,164,3,3,2,1,3,2,1,2),_MdlAlrMask_Type())
mdlAlrMask.setMaxAccess(_D)
if mibBuilder.loadTexts:mdlAlrMask.setStatus(_A)
_MdlCl_ObjectIdentity=ObjectIdentity
mdlCl=_MdlCl_ObjectIdentity((1,3,6,1,4,1,164,3,3,2,2))
_MdlClTable_Object=MibTable
mdlClTable=_MdlClTable_Object((1,3,6,1,4,1,164,3,3,2,2,1))
if mibBuilder.loadTexts:mdlClTable.setStatus(_A)
_MdlClEntry_Object=MibTableRow
mdlClEntry=_MdlClEntry_Object((1,3,6,1,4,1,164,3,3,2,2,1,1))
mdlClEntry.setIndexNames((0,_F,'mdlClIdx'))
if mibBuilder.loadTexts:mdlClEntry.setStatus(_A)
class _MdlClIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*((_v,3),(_w,4)))
_MdlClIdx_Type.__name__=_B
_MdlClIdx_Object=MibTableColumn
mdlClIdx=_MdlClIdx_Object((1,3,6,1,4,1,164,3,3,2,2,1,1,1),_MdlClIdx_Type())
mdlClIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlClIdx.setStatus(_A)
_MdlClSwchStatus_Type=Integer32
_MdlClSwchStatus_Object=MibTableColumn
mdlClSwchStatus=_MdlClSwchStatus_Object((1,3,6,1,4,1,164,3,3,2,2,1,1,2),_MdlClSwchStatus_Type())
mdlClSwchStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlClSwchStatus.setStatus(_A)
class _MdlClLastFlipDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MdlClLastFlipDate_Type.__name__=_J
_MdlClLastFlipDate_Object=MibTableColumn
mdlClLastFlipDate=_MdlClLastFlipDate_Object((1,3,6,1,4,1,164,3,3,2,2,1,1,3),_MdlClLastFlipDate_Type())
mdlClLastFlipDate.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlClLastFlipDate.setStatus(_A)
class _MdlClLastFlipTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MdlClLastFlipTime_Type.__name__=_J
_MdlClLastFlipTime_Object=MibTableColumn
mdlClLastFlipTime=_MdlClLastFlipTime_Object((1,3,6,1,4,1,164,3,3,2,2,1,1,4),_MdlClLastFlipTime_Type())
mdlClLastFlipTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlClLastFlipTime.setStatus(_A)
class _MdlClLastFlipCause_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MdlClLastFlipCause_Type.__name__=_J
_MdlClLastFlipCause_Object=MibTableColumn
mdlClLastFlipCause=_MdlClLastFlipCause_Object((1,3,6,1,4,1,164,3,3,2,2,1,1,5),_MdlClLastFlipCause_Type())
mdlClLastFlipCause.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlClLastFlipCause.setStatus(_A)
_MdlPs_ObjectIdentity=ObjectIdentity
mdlPs=_MdlPs_ObjectIdentity((1,3,6,1,4,1,164,3,3,2,3))
_MdlPsTable_Object=MibTable
mdlPsTable=_MdlPsTable_Object((1,3,6,1,4,1,164,3,3,2,3,1))
if mibBuilder.loadTexts:mdlPsTable.setStatus(_A)
_MdlPsEntry_Object=MibTableRow
mdlPsEntry=_MdlPsEntry_Object((1,3,6,1,4,1,164,3,3,2,3,1,1))
mdlPsEntry.setIndexNames((0,_F,'mdlPsIdx'))
if mibBuilder.loadTexts:mdlPsEntry.setStatus(_A)
_MdlPsIdx_Type=SlotType
_MdlPsIdx_Object=MibTableColumn
mdlPsIdx=_MdlPsIdx_Object((1,3,6,1,4,1,164,3,3,2,3,1,1,1),_MdlPsIdx_Type())
mdlPsIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlPsIdx.setStatus(_A)
class _MdlPsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notActive',1),('active',2)))
_MdlPsStatus_Type.__name__=_B
_MdlPsStatus_Object=MibTableColumn
mdlPsStatus=_MdlPsStatus_Object((1,3,6,1,4,1,164,3,3,2,3,1,1,2),_MdlPsStatus_Type())
mdlPsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlPsStatus.setStatus(_A)
class _MdlPsTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ok',1),('f12V',2),('f5V',3),('fMinus5V',4),('fFanVoltage',5),('fMainVoltage',6)))
_MdlPsTestResult_Type.__name__=_B
_MdlPsTestResult_Object=MibTableColumn
mdlPsTestResult=_MdlPsTestResult_Object((1,3,6,1,4,1,164,3,3,2,3,1,1,3),_MdlPsTestResult_Type())
mdlPsTestResult.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlPsTestResult.setStatus(_A)
_MdlPsVoltageCurrent_Type=Integer32
_MdlPsVoltageCurrent_Object=MibTableColumn
mdlPsVoltageCurrent=_MdlPsVoltageCurrent_Object((1,3,6,1,4,1,164,3,3,2,3,1,1,4),_MdlPsVoltageCurrent_Type())
mdlPsVoltageCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlPsVoltageCurrent.setStatus(_A)
_MdlPsVoltageMin_Type=Integer32
_MdlPsVoltageMin_Object=MibTableColumn
mdlPsVoltageMin=_MdlPsVoltageMin_Object((1,3,6,1,4,1,164,3,3,2,3,1,1,5),_MdlPsVoltageMin_Type())
mdlPsVoltageMin.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlPsVoltageMin.setStatus(_A)
_MdlPsVoltageMax_Type=Integer32
_MdlPsVoltageMax_Object=MibTableColumn
mdlPsVoltageMax=_MdlPsVoltageMax_Object((1,3,6,1,4,1,164,3,3,2,3,1,1,6),_MdlPsVoltageMax_Type())
mdlPsVoltageMax.setMaxAccess(_C)
if mibBuilder.loadTexts:mdlPsVoltageMax.setStatus(_A)
_PrtDacsMux_ObjectIdentity=ObjectIdentity
prtDacsMux=_PrtDacsMux_ObjectIdentity((1,3,6,1,4,1,164,3,3,3))
_PrtGen_ObjectIdentity=ObjectIdentity
prtGen=_PrtGen_ObjectIdentity((1,3,6,1,4,1,164,3,3,3,1))
_PrtGenParamTable_Object=MibTable
prtGenParamTable=_PrtGenParamTable_Object((1,3,6,1,4,1,164,3,3,3,1,1))
if mibBuilder.loadTexts:prtGenParamTable.setStatus(_A)
_PrtGenEntry_Object=MibTableRow
prtGenEntry=_PrtGenEntry_Object((1,3,6,1,4,1,164,3,3,3,1,1,1))
prtGenEntry.setIndexNames((0,_F,_Aw))
if mibBuilder.loadTexts:prtGenEntry.setStatus(_A)
_PrtGenPrtIdx_Type=Integer32
_PrtGenPrtIdx_Object=MibTableColumn
prtGenPrtIdx=_PrtGenPrtIdx_Object((1,3,6,1,4,1,164,3,3,3,1,1,1,1),_PrtGenPrtIdx_Type())
prtGenPrtIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGenPrtIdx.setStatus(_A)
class _PrtGenSlt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,255)));namedValues=NamedValues(*((_T,5),(_U,6),(_V,7),(_W,8),(_X,9),(_Y,10),(_Z,11),(_a,12),(_b,13),(_e,14),(_f,15),(_g,16),(_h,17),(_i,18),(_j,19),(_A7,103),(_A8,104),('kmxCl',105),(_AT,106),(_A9,107),(_AA,108),(_AB,109),(_AC,110),(_AD,111),(_AE,112),(_AF,113),(_AG,114),(_AH,115),(_AI,116),(_AJ,117),(_AK,118),(_t,255)))
_PrtGenSlt_Type.__name__=_B
_PrtGenSlt_Object=MibTableColumn
prtGenSlt=_PrtGenSlt_Object((1,3,6,1,4,1,164,3,3,3,1,1,1,2),_PrtGenSlt_Type())
prtGenSlt.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGenSlt.setStatus(_A)
class _PrtGenExtInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('external',2),(_z,3)))
_PrtGenExtInt_Type.__name__=_B
_PrtGenExtInt_Object=MibTableColumn
prtGenExtInt=_PrtGenExtInt_Object((1,3,6,1,4,1,164,3,3,3,1,1,1,3),_PrtGenExtInt_Type())
prtGenExtInt.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGenExtInt.setStatus(_A)
_PrtGenIfIndex_Type=Integer32
_PrtGenIfIndex_Object=MibTableColumn
prtGenIfIndex=_PrtGenIfIndex_Object((1,3,6,1,4,1,164,3,3,3,1,1,1,4),_PrtGenIfIndex_Type())
prtGenIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGenIfIndex.setStatus(_A)
class _PrtGenActiveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_u,1),('notUsed',2),('offLine',3),('onLine',4),('offLineRedundancy',5),('onLineRedundancy',6)))
_PrtGenActiveStatus_Type.__name__=_B
_PrtGenActiveStatus_Object=MibTableColumn
prtGenActiveStatus=_PrtGenActiveStatus_Object((1,3,6,1,4,1,164,3,3,3,1,1,1,5),_PrtGenActiveStatus_Type())
prtGenActiveStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGenActiveStatus.setStatus(_A)
class _PrtGenAlrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7)));namedValues=NamedValues(*((_H,2),(_k,3),(_m,4),(_n,5),(_d,6),(_o,7)))
_PrtGenAlrStatus_Type.__name__=_B
_PrtGenAlrStatus_Object=MibTableColumn
prtGenAlrStatus=_PrtGenAlrStatus_Object((1,3,6,1,4,1,164,3,3,3,1,1,1,6),_PrtGenAlrStatus_Type())
prtGenAlrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGenAlrStatus.setStatus(_A)
class _PrtGenTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_PrtGenTestStatus_Type.__name__=_B
_PrtGenTestStatus_Object=MibTableColumn
prtGenTestStatus=_PrtGenTestStatus_Object((1,3,6,1,4,1,164,3,3,3,1,1,1,7),_PrtGenTestStatus_Type())
prtGenTestStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGenTestStatus.setStatus(_A)
_PrtGenTestMask_Type=Integer32
_PrtGenTestMask_Object=MibTableColumn
prtGenTestMask=_PrtGenTestMask_Object((1,3,6,1,4,1,164,3,3,3,1,1,1,8),_PrtGenTestMask_Type())
prtGenTestMask.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGenTestMask.setStatus(_A)
_PrtGenTestCmd_Type=Integer32
_PrtGenTestCmd_Object=MibTableColumn
prtGenTestCmd=_PrtGenTestCmd_Object((1,3,6,1,4,1,164,3,3,3,1,1,1,9),_PrtGenTestCmd_Type())
prtGenTestCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:prtGenTestCmd.setStatus(_A)
_PrtGenTestRunning_Type=Integer32
_PrtGenTestRunning_Object=MibTableColumn
prtGenTestRunning=_PrtGenTestRunning_Object((1,3,6,1,4,1,164,3,3,3,1,1,1,10),_PrtGenTestRunning_Type())
prtGenTestRunning.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGenTestRunning.setStatus(_A)
class _PrtGenType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,255)));namedValues=NamedValues(*((_u,1),('t1',2),('e1',3),('hs',4),('t1Csu',5),('t1Dsu',6),('e1Ltu',7),('e1Dsu',8),('hdsl',9),('sp',10),('t1F',11),('e1F',12),('dim',13),('isdn',14),('t3',15),('e3',16),('t3f',17),('e3f',18),('idsl',19),('stm1',20),('vc4',21),('vc12',22),('msdsl',23),('vc11',24),('vc3',25),('soh',26),('eth',27),('shdsl',28),(_s,255)))
_PrtGenType_Type.__name__=_B
_PrtGenType_Object=MibTableColumn
prtGenType=_PrtGenType_Object((1,3,6,1,4,1,164,3,3,3,1,1,1,11),_PrtGenType_Type())
prtGenType.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGenType.setStatus(_A)
class _PrtGenInterfaceType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PrtGenInterfaceType_Type.__name__=_J
_PrtGenInterfaceType_Object=MibTableColumn
prtGenInterfaceType=_PrtGenInterfaceType_Object((1,3,6,1,4,1,164,3,3,3,1,1,1,12),_PrtGenInterfaceType_Type())
prtGenInterfaceType.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGenInterfaceType.setStatus(_A)
class _PrtGenAlrClearCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noOp',1),(_H,2),(_I,3)))
_PrtGenAlrClearCmd_Type.__name__=_B
_PrtGenAlrClearCmd_Object=MibTableColumn
prtGenAlrClearCmd=_PrtGenAlrClearCmd_Object((1,3,6,1,4,1,164,3,3,3,1,1,1,13),_PrtGenAlrClearCmd_Type())
prtGenAlrClearCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:prtGenAlrClearCmd.setStatus(_A)
class _PrtGenAlrMaskAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noOp',1),(_H,2),(_I,3)))
_PrtGenAlrMaskAll_Type.__name__=_B
_PrtGenAlrMaskAll_Object=MibTableColumn
prtGenAlrMaskAll=_PrtGenAlrMaskAll_Object((1,3,6,1,4,1,164,3,3,3,1,1,1,14),_PrtGenAlrMaskAll_Type())
prtGenAlrMaskAll.setMaxAccess(_D)
if mibBuilder.loadTexts:prtGenAlrMaskAll.setStatus(_A)
_PrtGenParamStatus_Type=OctetString
_PrtGenParamStatus_Object=MibTableColumn
prtGenParamStatus=_PrtGenParamStatus_Object((1,3,6,1,4,1,164,3,3,3,1,1,1,15),_PrtGenParamStatus_Type())
prtGenParamStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGenParamStatus.setStatus(_A)
class _PrtGenRdnStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),(_H,2),(_I,3)))
_PrtGenRdnStatus_Type.__name__=_B
_PrtGenRdnStatus_Object=MibTableColumn
prtGenRdnStatus=_PrtGenRdnStatus_Object((1,3,6,1,4,1,164,3,3,3,1,1,1,16),_PrtGenRdnStatus_Type())
prtGenRdnStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGenRdnStatus.setStatus(_A)
_PrtGenTestMaskXP_Type=OctetString
_PrtGenTestMaskXP_Object=MibTableColumn
prtGenTestMaskXP=_PrtGenTestMaskXP_Object((1,3,6,1,4,1,164,3,3,3,1,1,1,17),_PrtGenTestMaskXP_Type())
prtGenTestMaskXP.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGenTestMaskXP.setStatus(_A)
_PrtGenTestCmdXP_Type=OctetString
_PrtGenTestCmdXP_Object=MibTableColumn
prtGenTestCmdXP=_PrtGenTestCmdXP_Object((1,3,6,1,4,1,164,3,3,3,1,1,1,18),_PrtGenTestCmdXP_Type())
prtGenTestCmdXP.setMaxAccess(_D)
if mibBuilder.loadTexts:prtGenTestCmdXP.setStatus(_A)
_PrtGenTestRunningXP_Type=OctetString
_PrtGenTestRunningXP_Object=MibTableColumn
prtGenTestRunningXP=_PrtGenTestRunningXP_Object((1,3,6,1,4,1,164,3,3,3,1,1,1,19),_PrtGenTestRunningXP_Type())
prtGenTestRunningXP.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGenTestRunningXP.setStatus(_A)
_PrtGenTestDurationTable_Object=MibTable
prtGenTestDurationTable=_PrtGenTestDurationTable_Object((1,3,6,1,4,1,164,3,3,3,1,2))
if mibBuilder.loadTexts:prtGenTestDurationTable.setStatus(_A)
_PrtGenTestDurationEntry_Object=MibTableRow
prtGenTestDurationEntry=_PrtGenTestDurationEntry_Object((1,3,6,1,4,1,164,3,3,3,1,2,1))
prtGenTestDurationEntry.setIndexNames((0,_F,_Ax),(0,_F,_Ay))
if mibBuilder.loadTexts:prtGenTestDurationEntry.setStatus(_A)
_PrtGenTestPrtIdx_Type=Integer32
_PrtGenTestPrtIdx_Object=MibTableColumn
prtGenTestPrtIdx=_PrtGenTestPrtIdx_Object((1,3,6,1,4,1,164,3,3,3,1,2,1,1),_PrtGenTestPrtIdx_Type())
prtGenTestPrtIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGenTestPrtIdx.setStatus(_A)
class _PrtGenTestIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,20,21,22,23,26,27,28,30,32,33,34)));namedValues=NamedValues(*(('localLoop',1),('remoteLoop',2),('bert',3),('plb',4),('rlb',5),('llb',6),('toneInjection',7),('txInband',8),('rxInband',9),('remLoopOnRemUnit',10),('bertOnRemUnit',11),('llbOnRemUnit',12),('txPlb',14),('txLlb',15),('dteLoop',16),('hdslTxInband',20),('hdslRxInband',21),('monitor',22),('userLineLoopback',23),('lbbd',26),('lb1',27),('lb2',28),('tsRemoteLoop',30),('downstreamAis',32),('upstreamAis',33),('sendRdi',34)))
_PrtGenTestIdx_Type.__name__=_B
_PrtGenTestIdx_Object=MibTableColumn
prtGenTestIdx=_PrtGenTestIdx_Object((1,3,6,1,4,1,164,3,3,3,1,2,1,2),_PrtGenTestIdx_Type())
prtGenTestIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGenTestIdx.setStatus(_A)
_PrtGenTestDuration_Type=Integer32
_PrtGenTestDuration_Object=MibTableColumn
prtGenTestDuration=_PrtGenTestDuration_Object((1,3,6,1,4,1,164,3,3,3,1,2,1,3),_PrtGenTestDuration_Type())
prtGenTestDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:prtGenTestDuration.setStatus(_A)
_PrtGenTsTable_Object=MibTable
prtGenTsTable=_PrtGenTsTable_Object((1,3,6,1,4,1,164,3,3,3,1,3))
if mibBuilder.loadTexts:prtGenTsTable.setStatus(_A)
_PrtGenTsEntry_Object=MibTableRow
prtGenTsEntry=_PrtGenTsEntry_Object((1,3,6,1,4,1,164,3,3,3,1,3,1))
prtGenTsEntry.setIndexNames((0,_F,_Az),(0,_F,_A_),(0,_F,_B0))
if mibBuilder.loadTexts:prtGenTsEntry.setStatus(_A)
class _PrtGenTsCnfgIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PrtGenTsCnfgIdx_Type.__name__=_B
_PrtGenTsCnfgIdx_Object=MibTableColumn
prtGenTsCnfgIdx=_PrtGenTsCnfgIdx_Object((1,3,6,1,4,1,164,3,3,3,1,3,1,1),_PrtGenTsCnfgIdx_Type())
prtGenTsCnfgIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGenTsCnfgIdx.setStatus(_A)
_PrtGenTsPrtIdx_Type=Integer32
_PrtGenTsPrtIdx_Object=MibTableColumn
prtGenTsPrtIdx=_PrtGenTsPrtIdx_Object((1,3,6,1,4,1,164,3,3,3,1,3,1,2),_PrtGenTsPrtIdx_Type())
prtGenTsPrtIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGenTsPrtIdx.setStatus(_A)
_PrtGenTsIdx_Type=Integer32
_PrtGenTsIdx_Object=MibTableColumn
prtGenTsIdx=_PrtGenTsIdx_Object((1,3,6,1,4,1,164,3,3,3,1,3,1,3),_PrtGenTsIdx_Type())
prtGenTsIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtGenTsIdx.setStatus(_A)
class _PrtGenTsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_u,1),('voice',2),('data',3),('vcMP',4),('nc',5),('mng',6)))
_PrtGenTsType_Type.__name__=_B
_PrtGenTsType_Object=MibTableColumn
prtGenTsType=_PrtGenTsType_Object((1,3,6,1,4,1,164,3,3,3,1,3,1,4),_PrtGenTsType_Type())
prtGenTsType.setMaxAccess(_D)
if mibBuilder.loadTexts:prtGenTsType.setStatus(_A)
_PrtGenTsIConPrt_Type=Integer32
_PrtGenTsIConPrt_Object=MibTableColumn
prtGenTsIConPrt=_PrtGenTsIConPrt_Object((1,3,6,1,4,1,164,3,3,3,1,3,1,5),_PrtGenTsIConPrt_Type())
prtGenTsIConPrt.setMaxAccess(_D)
if mibBuilder.loadTexts:prtGenTsIConPrt.setStatus(_A)
_PrtGenTsIConTs_Type=Integer32
_PrtGenTsIConTs_Object=MibTableColumn
prtGenTsIConTs=_PrtGenTsIConTs_Object((1,3,6,1,4,1,164,3,3,3,1,3,1,6),_PrtGenTsIConTs_Type())
prtGenTsIConTs.setMaxAccess(_D)
if mibBuilder.loadTexts:prtGenTsIConTs.setStatus(_A)
_PrtAlr_ObjectIdentity=ObjectIdentity
prtAlr=_PrtAlr_ObjectIdentity((1,3,6,1,4,1,164,3,3,3,1,4))
_PrtSAlarmTable_Object=MibTable
prtSAlarmTable=_PrtSAlarmTable_Object((1,3,6,1,4,1,164,3,3,3,1,4,1))
if mibBuilder.loadTexts:prtSAlarmTable.setStatus(_A)
_PrtSAlarmEntry_Object=MibTableRow
prtSAlarmEntry=_PrtSAlarmEntry_Object((1,3,6,1,4,1,164,3,3,3,1,4,1,1))
prtSAlarmEntry.setIndexNames((0,_F,_B1),(0,_F,_B2))
if mibBuilder.loadTexts:prtSAlarmEntry.setStatus(_A)
_PrtSAlarmIdx_Type=Integer32
_PrtSAlarmIdx_Object=MibTableColumn
prtSAlarmIdx=_PrtSAlarmIdx_Object((1,3,6,1,4,1,164,3,3,3,1,4,1,1,1),_PrtSAlarmIdx_Type())
prtSAlarmIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtSAlarmIdx.setStatus(_A)
_PrtSAlarmPrtIdx_Type=Integer32
_PrtSAlarmPrtIdx_Object=MibTableColumn
prtSAlarmPrtIdx=_PrtSAlarmPrtIdx_Object((1,3,6,1,4,1,164,3,3,3,1,4,1,1,2),_PrtSAlarmPrtIdx_Type())
prtSAlarmPrtIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtSAlarmPrtIdx.setStatus(_A)
_PrtSAlarmCode_Type=Integer32
_PrtSAlarmCode_Object=MibTableColumn
prtSAlarmCode=_PrtSAlarmCode_Object((1,3,6,1,4,1,164,3,3,3,1,4,1,1,3),_PrtSAlarmCode_Type())
prtSAlarmCode.setMaxAccess(_C)
if mibBuilder.loadTexts:prtSAlarmCode.setStatus(_A)
class _PrtSAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6,7)));namedValues=NamedValues(*((_n,3),(_m,4),(_k,5),(_d,6),(_o,7)))
_PrtSAlarmState_Type.__name__=_B
_PrtSAlarmState_Object=MibTableColumn
prtSAlarmState=_PrtSAlarmState_Object((1,3,6,1,4,1,164,3,3,3,1,4,1,1,4),_PrtSAlarmState_Type())
prtSAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:prtSAlarmState.setStatus(_A)
class _PrtSAlarmMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_PrtSAlarmMask_Type.__name__=_B
_PrtSAlarmMask_Object=MibTableColumn
prtSAlarmMask=_PrtSAlarmMask_Object((1,3,6,1,4,1,164,3,3,3,1,4,1,1,5),_PrtSAlarmMask_Type())
prtSAlarmMask.setMaxAccess(_C)
if mibBuilder.loadTexts:prtSAlarmMask.setStatus(_A)
class _PrtSAlarmInvert_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_PrtSAlarmInvert_Type.__name__=_B
_PrtSAlarmInvert_Object=MibTableColumn
prtSAlarmInvert=_PrtSAlarmInvert_Object((1,3,6,1,4,1,164,3,3,3,1,4,1,1,6),_PrtSAlarmInvert_Type())
prtSAlarmInvert.setMaxAccess(_C)
if mibBuilder.loadTexts:prtSAlarmInvert.setStatus(_A)
class _PrtSAlarmOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_PrtSAlarmOnOff_Type.__name__=_B
_PrtSAlarmOnOff_Object=MibTableColumn
prtSAlarmOnOff=_PrtSAlarmOnOff_Object((1,3,6,1,4,1,164,3,3,3,1,4,1,1,7),_PrtSAlarmOnOff_Type())
prtSAlarmOnOff.setMaxAccess(_C)
if mibBuilder.loadTexts:prtSAlarmOnOff.setStatus(_A)
_PrtSAlarmCounter_Type=Integer32
_PrtSAlarmCounter_Object=MibTableColumn
prtSAlarmCounter=_PrtSAlarmCounter_Object((1,3,6,1,4,1,164,3,3,3,1,4,1,1,8),_PrtSAlarmCounter_Type())
prtSAlarmCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:prtSAlarmCounter.setStatus(_A)
_PrtAlrMaskTable_Object=MibTable
prtAlrMaskTable=_PrtAlrMaskTable_Object((1,3,6,1,4,1,164,3,3,3,1,4,2))
if mibBuilder.loadTexts:prtAlrMaskTable.setStatus(_A)
_PrtAlrMaskEntry_Object=MibTableRow
prtAlrMaskEntry=_PrtAlrMaskEntry_Object((1,3,6,1,4,1,164,3,3,3,1,4,2,1))
prtAlrMaskEntry.setIndexNames((0,_F,_B3))
if mibBuilder.loadTexts:prtAlrMaskEntry.setStatus(_A)
_PrtAlrMaskPrtIdx_Type=Integer32
_PrtAlrMaskPrtIdx_Object=MibTableColumn
prtAlrMaskPrtIdx=_PrtAlrMaskPrtIdx_Object((1,3,6,1,4,1,164,3,3,3,1,4,2,1,1),_PrtAlrMaskPrtIdx_Type())
prtAlrMaskPrtIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtAlrMaskPrtIdx.setStatus(_A)
class _PrtAlrMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_PrtAlrMask_Type.__name__=_l
_PrtAlrMask_Object=MibTableColumn
prtAlrMask=_PrtAlrMask_Object((1,3,6,1,4,1,164,3,3,3,1,4,2,1,2),_PrtAlrMask_Type())
prtAlrMask.setMaxAccess(_D)
if mibBuilder.loadTexts:prtAlrMask.setStatus(_A)
_PrtBertTable_Object=MibTable
prtBertTable=_PrtBertTable_Object((1,3,6,1,4,1,164,3,3,3,1,5))
if mibBuilder.loadTexts:prtBertTable.setStatus(_A)
_PrtBertEntry_Object=MibTableRow
prtBertEntry=_PrtBertEntry_Object((1,3,6,1,4,1,164,3,3,3,1,5,1))
prtBertEntry.setIndexNames((0,_F,_B4))
if mibBuilder.loadTexts:prtBertEntry.setStatus(_A)
_PrtBertPrtIdx_Type=Integer32
_PrtBertPrtIdx_Object=MibTableColumn
prtBertPrtIdx=_PrtBertPrtIdx_Object((1,3,6,1,4,1,164,3,3,3,1,5,1,1),_PrtBertPrtIdx_Type())
prtBertPrtIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtBertPrtIdx.setStatus(_A)
class _PrtBertPattern_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,255)));namedValues=NamedValues(*(('p2E3m1',1),('p2E4m1',2),('p2E5m1',3),('p2E6m1',4),('p2E7m1',5),('p511',6),('p2E10m1',7),('p2047',8),('p2E15m1',9),('p2E17m1',10),('p2E18m1',11),('p2E20m1',12),('qrss',13),('p2E21m1',14),('p2E22m1',15),('p2E23m1',16),('p2E25m1',17),('p2E28m1',18),('p2E29m1',19),('p2E31m1',20),('p2E32m1',21),('rj011',22),('p63',23),('p1M7S',24),('p1S7M',25),('alternate',26),('mark',27),('space',28),('p2E11m1',29),(_E,255)))
_PrtBertPattern_Type.__name__=_B
_PrtBertPattern_Object=MibTableColumn
prtBertPattern=_PrtBertPattern_Object((1,3,6,1,4,1,164,3,3,3,1,5,1,2),_PrtBertPattern_Type())
prtBertPattern.setMaxAccess(_D)
if mibBuilder.loadTexts:prtBertPattern.setStatus(_A)
class _PrtBertInjectRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,255)));namedValues=NamedValues(*(('noError',1),('r10Em1',2),('r10Em2',3),('r10Em3',4),('r10Em4',5),('r10Em5',6),('r10Em6',7),('r10Em7',8),('single',9),(_E,255)))
_PrtBertInjectRate_Type.__name__=_B
_PrtBertInjectRate_Object=MibTableColumn
prtBertInjectRate=_PrtBertInjectRate_Object((1,3,6,1,4,1,164,3,3,3,1,5,1,3),_PrtBertInjectRate_Type())
prtBertInjectRate.setMaxAccess(_D)
if mibBuilder.loadTexts:prtBertInjectRate.setStatus(_A)
class _PrtBertInjectErrRateCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_PrtBertInjectErrRateCmd_Type.__name__=_B
_PrtBertInjectErrRateCmd_Object=MibTableColumn
prtBertInjectErrRateCmd=_PrtBertInjectErrRateCmd_Object((1,3,6,1,4,1,164,3,3,3,1,5,1,4),_PrtBertInjectErrRateCmd_Type())
prtBertInjectErrRateCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:prtBertInjectErrRateCmd.setStatus(_A)
class _PrtBertInjectSingleErrCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_PrtBertInjectSingleErrCmd_Type.__name__=_B
_PrtBertInjectSingleErrCmd_Object=MibTableColumn
prtBertInjectSingleErrCmd=_PrtBertInjectSingleErrCmd_Object((1,3,6,1,4,1,164,3,3,3,1,5,1,5),_PrtBertInjectSingleErrCmd_Type())
prtBertInjectSingleErrCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:prtBertInjectSingleErrCmd.setStatus(_A)
_PrtBertRunTime_Type=Integer32
_PrtBertRunTime_Object=MibTableColumn
prtBertRunTime=_PrtBertRunTime_Object((1,3,6,1,4,1,164,3,3,3,1,5,1,6),_PrtBertRunTime_Type())
prtBertRunTime.setMaxAccess(_C)
if mibBuilder.loadTexts:prtBertRunTime.setStatus(_A)
_PrtBertESs_Type=Integer32
_PrtBertESs_Object=MibTableColumn
prtBertESs=_PrtBertESs_Object((1,3,6,1,4,1,164,3,3,3,1,5,1,7),_PrtBertESs_Type())
prtBertESs.setMaxAccess(_C)
if mibBuilder.loadTexts:prtBertESs.setStatus(_A)
_PrtBertSyncLoss_Type=Integer32
_PrtBertSyncLoss_Object=MibTableColumn
prtBertSyncLoss=_PrtBertSyncLoss_Object((1,3,6,1,4,1,164,3,3,3,1,5,1,8),_PrtBertSyncLoss_Type())
prtBertSyncLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:prtBertSyncLoss.setStatus(_A)
_PrtBertErrorBits_Type=Integer32
_PrtBertErrorBits_Object=MibTableColumn
prtBertErrorBits=_PrtBertErrorBits_Object((1,3,6,1,4,1,164,3,3,3,1,5,1,9),_PrtBertErrorBits_Type())
prtBertErrorBits.setMaxAccess(_C)
if mibBuilder.loadTexts:prtBertErrorBits.setStatus(_A)
class _PrtBertClearCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_PrtBertClearCounters_Type.__name__=_B
_PrtBertClearCounters_Object=MibTableColumn
prtBertClearCounters=_PrtBertClearCounters_Object((1,3,6,1,4,1,164,3,3,3,1,5,1,10),_PrtBertClearCounters_Type())
prtBertClearCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:prtBertClearCounters.setStatus(_A)
class _PrtBertSyncStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('syncLoss',2),('sync',3)))
_PrtBertSyncStatus_Type.__name__=_B
_PrtBertSyncStatus_Object=MibTableColumn
prtBertSyncStatus=_PrtBertSyncStatus_Object((1,3,6,1,4,1,164,3,3,3,1,5,1,11),_PrtBertSyncStatus_Type())
prtBertSyncStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:prtBertSyncStatus.setStatus(_A)
class _PrtBertTs_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_PrtBertTs_Type.__name__=_l
_PrtBertTs_Object=MibTableColumn
prtBertTs=_PrtBertTs_Object((1,3,6,1,4,1,164,3,3,3,1,5,1,12),_PrtBertTs_Type())
prtBertTs.setMaxAccess(_D)
if mibBuilder.loadTexts:prtBertTs.setStatus(_A)
class _PrtBertResult_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PrtBertResult_Type.__name__=_J
_PrtBertResult_Object=MibTableColumn
prtBertResult=_PrtBertResult_Object((1,3,6,1,4,1,164,3,3,3,1,5,1,13),_PrtBertResult_Type())
prtBertResult.setMaxAccess(_C)
if mibBuilder.loadTexts:prtBertResult.setStatus(_A)
_PrtBertTxBits_Type=Integer32
_PrtBertTxBits_Object=MibTableColumn
prtBertTxBits=_PrtBertTxBits_Object((1,3,6,1,4,1,164,3,3,3,1,5,1,14),_PrtBertTxBits_Type())
prtBertTxBits.setMaxAccess(_C)
if mibBuilder.loadTexts:prtBertTxBits.setStatus(_A)
_PrtBertRxBits_Type=Integer32
_PrtBertRxBits_Object=MibTableColumn
prtBertRxBits=_PrtBertRxBits_Object((1,3,6,1,4,1,164,3,3,3,1,5,1,15),_PrtBertRxBits_Type())
prtBertRxBits.setMaxAccess(_C)
if mibBuilder.loadTexts:prtBertRxBits.setStatus(_A)
_PrtBertTxErrorBits_Type=Integer32
_PrtBertTxErrorBits_Object=MibTableColumn
prtBertTxErrorBits=_PrtBertTxErrorBits_Object((1,3,6,1,4,1,164,3,3,3,1,5,1,16),_PrtBertTxErrorBits_Type())
prtBertTxErrorBits.setMaxAccess(_C)
if mibBuilder.loadTexts:prtBertTxErrorBits.setStatus(_A)
_PrtMonTable_Object=MibTable
prtMonTable=_PrtMonTable_Object((1,3,6,1,4,1,164,3,3,3,1,6))
if mibBuilder.loadTexts:prtMonTable.setStatus(_A)
_PrtMonEntry_Object=MibTableRow
prtMonEntry=_PrtMonEntry_Object((1,3,6,1,4,1,164,3,3,3,1,6,1))
prtMonEntry.setIndexNames((0,_F,_B5),(0,_F,_B6))
if mibBuilder.loadTexts:prtMonEntry.setStatus(_A)
class _PrtMonCnfgIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PrtMonCnfgIdx_Type.__name__=_B
_PrtMonCnfgIdx_Object=MibTableColumn
prtMonCnfgIdx=_PrtMonCnfgIdx_Object((1,3,6,1,4,1,164,3,3,3,1,6,1,1),_PrtMonCnfgIdx_Type())
prtMonCnfgIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtMonCnfgIdx.setStatus(_A)
_PrtMonitoringIdx_Type=Integer32
_PrtMonitoringIdx_Object=MibTableColumn
prtMonitoringIdx=_PrtMonitoringIdx_Object((1,3,6,1,4,1,164,3,3,3,1,6,1,2),_PrtMonitoringIdx_Type())
prtMonitoringIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtMonitoringIdx.setStatus(_A)
class _PrtMonitoringEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_y,2),(_A0,3)))
_PrtMonitoringEnable_Type.__name__=_B
_PrtMonitoringEnable_Object=MibTableColumn
prtMonitoringEnable=_PrtMonitoringEnable_Object((1,3,6,1,4,1,164,3,3,3,1,6,1,3),_PrtMonitoringEnable_Type())
prtMonitoringEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:prtMonitoringEnable.setStatus(_A)
class _PrtMonitoringTSs_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_PrtMonitoringTSs_Type.__name__=_l
_PrtMonitoringTSs_Object=MibTableColumn
prtMonitoringTSs=_PrtMonitoringTSs_Object((1,3,6,1,4,1,164,3,3,3,1,6,1,4),_PrtMonitoringTSs_Type())
prtMonitoringTSs.setMaxAccess(_D)
if mibBuilder.loadTexts:prtMonitoringTSs.setStatus(_A)
_PrtMonitoredPort_Type=Integer32
_PrtMonitoredPort_Object=MibTableColumn
prtMonitoredPort=_PrtMonitoredPort_Object((1,3,6,1,4,1,164,3,3,3,1,6,1,5),_PrtMonitoredPort_Type())
prtMonitoredPort.setMaxAccess(_D)
if mibBuilder.loadTexts:prtMonitoredPort.setStatus(_A)
class _PrtMonitoredTSs_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_PrtMonitoredTSs_Type.__name__=_l
_PrtMonitoredTSs_Object=MibTableColumn
prtMonitoredTSs=_PrtMonitoredTSs_Object((1,3,6,1,4,1,164,3,3,3,1,6,1,6),_PrtMonitoredTSs_Type())
prtMonitoredTSs.setMaxAccess(_D)
if mibBuilder.loadTexts:prtMonitoredTSs.setStatus(_A)
_PrtCfgParam_ObjectIdentity=ObjectIdentity
prtCfgParam=_PrtCfgParam_ObjectIdentity((1,3,6,1,4,1,164,3,3,3,1,7))
_PrtCfgParamTable_Object=MibTable
prtCfgParamTable=_PrtCfgParamTable_Object((1,3,6,1,4,1,164,3,3,3,1,7,1))
if mibBuilder.loadTexts:prtCfgParamTable.setStatus(_A)
_PrtCfgParamEntry_Object=MibTableRow
prtCfgParamEntry=_PrtCfgParamEntry_Object((1,3,6,1,4,1,164,3,3,3,1,7,1,1))
prtCfgParamEntry.setIndexNames((0,_F,_B7),(0,_F,_B8))
if mibBuilder.loadTexts:prtCfgParamEntry.setStatus(_A)
class _PrtCfgParamCnfgIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PrtCfgParamCnfgIdx_Type.__name__=_B
_PrtCfgParamCnfgIdx_Object=MibTableColumn
prtCfgParamCnfgIdx=_PrtCfgParamCnfgIdx_Object((1,3,6,1,4,1,164,3,3,3,1,7,1,1,1),_PrtCfgParamCnfgIdx_Type())
prtCfgParamCnfgIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtCfgParamCnfgIdx.setStatus(_A)
_PrtCfgParamIdx_Type=Integer32
_PrtCfgParamIdx_Object=MibTableColumn
prtCfgParamIdx=_PrtCfgParamIdx_Object((1,3,6,1,4,1,164,3,3,3,1,7,1,1,2),_PrtCfgParamIdx_Type())
prtCfgParamIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtCfgParamIdx.setStatus(_A)
class _PrtCfgParamSlt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,6,7,8,9,10,11,12,13,107,108,109,110,111,112,113,114,115,116,117,118,255)));namedValues=NamedValues(*((_T,5),(_U,6),(_V,7),(_W,8),(_X,9),(_Y,10),(_Z,11),(_a,12),(_b,13),(_A9,107),(_AA,108),(_AB,109),(_AC,110),(_AD,111),(_AE,112),(_AF,113),(_AG,114),(_AH,115),(_AI,116),(_AJ,117),(_AK,118),(_E,255)))
_PrtCfgParamSlt_Type.__name__=_B
_PrtCfgParamSlt_Object=MibTableColumn
prtCfgParamSlt=_PrtCfgParamSlt_Object((1,3,6,1,4,1,164,3,3,3,1,7,1,1,3),_PrtCfgParamSlt_Type())
prtCfgParamSlt.setMaxAccess(_C)
if mibBuilder.loadTexts:prtCfgParamSlt.setStatus(_A)
class _PrtCfgParamOperatedMl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,103,104)));namedValues=NamedValues(*((_E,1),(_A7,103),(_A8,104)))
_PrtCfgParamOperatedMl_Type.__name__=_B
_PrtCfgParamOperatedMl_Object=MibTableColumn
prtCfgParamOperatedMl=_PrtCfgParamOperatedMl_Object((1,3,6,1,4,1,164,3,3,3,1,7,1,1,4),_PrtCfgParamOperatedMl_Type())
prtCfgParamOperatedMl.setMaxAccess(_D)
if mibBuilder.loadTexts:prtCfgParamOperatedMl.setStatus(_A)
class _PrtCfgParamMlAtoMlBPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('low',2),(_AO,3)))
_PrtCfgParamMlAtoMlBPrio_Type.__name__=_B
_PrtCfgParamMlAtoMlBPrio_Object=MibTableColumn
prtCfgParamMlAtoMlBPrio=_PrtCfgParamMlAtoMlBPrio_Object((1,3,6,1,4,1,164,3,3,3,1,7,1,1,5),_PrtCfgParamMlAtoMlBPrio_Type())
prtCfgParamMlAtoMlBPrio.setMaxAccess(_D)
if mibBuilder.loadTexts:prtCfgParamMlAtoMlBPrio.setStatus(_A)
class _PrtCfgParamMlBtoMlAPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('low',2),(_AO,3)))
_PrtCfgParamMlBtoMlAPrio_Type.__name__=_B
_PrtCfgParamMlBtoMlAPrio_Object=MibTableColumn
prtCfgParamMlBtoMlAPrio=_PrtCfgParamMlBtoMlAPrio_Object((1,3,6,1,4,1,164,3,3,3,1,7,1,1,6),_PrtCfgParamMlBtoMlAPrio_Type())
prtCfgParamMlBtoMlAPrio.setMaxAccess(_D)
if mibBuilder.loadTexts:prtCfgParamMlBtoMlAPrio.setStatus(_A)
class _PrtCfgParamInbandLoopDetection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_y,2),(_A0,3)))
_PrtCfgParamInbandLoopDetection_Type.__name__=_B
_PrtCfgParamInbandLoopDetection_Object=MibTableColumn
prtCfgParamInbandLoopDetection=_PrtCfgParamInbandLoopDetection_Object((1,3,6,1,4,1,164,3,3,3,1,7,1,1,7),_PrtCfgParamInbandLoopDetection_Type())
prtCfgParamInbandLoopDetection.setMaxAccess(_D)
if mibBuilder.loadTexts:prtCfgParamInbandLoopDetection.setStatus(_A)
class _PrtCfgParamInbandLoopPatternCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('rdlLoop',2),(_B9,3)))
_PrtCfgParamInbandLoopPatternCfg_Type.__name__=_B
_PrtCfgParamInbandLoopPatternCfg_Object=MibTableColumn
prtCfgParamInbandLoopPatternCfg=_PrtCfgParamInbandLoopPatternCfg_Object((1,3,6,1,4,1,164,3,3,3,1,7,1,1,8),_PrtCfgParamInbandLoopPatternCfg_Type())
prtCfgParamInbandLoopPatternCfg.setMaxAccess(_D)
if mibBuilder.loadTexts:prtCfgParamInbandLoopPatternCfg.setStatus(_A)
_PrtCfgParamInbandLoopActPattern_Type=DisplayString
_PrtCfgParamInbandLoopActPattern_Object=MibTableColumn
prtCfgParamInbandLoopActPattern=_PrtCfgParamInbandLoopActPattern_Object((1,3,6,1,4,1,164,3,3,3,1,7,1,1,9),_PrtCfgParamInbandLoopActPattern_Type())
prtCfgParamInbandLoopActPattern.setMaxAccess(_D)
if mibBuilder.loadTexts:prtCfgParamInbandLoopActPattern.setStatus(_A)
_PrtCfgParamInbandLoopDeactPattern_Type=DisplayString
_PrtCfgParamInbandLoopDeactPattern_Object=MibTableColumn
prtCfgParamInbandLoopDeactPattern=_PrtCfgParamInbandLoopDeactPattern_Object((1,3,6,1,4,1,164,3,3,3,1,7,1,1,10),_PrtCfgParamInbandLoopDeactPattern_Type())
prtCfgParamInbandLoopDeactPattern.setMaxAccess(_D)
if mibBuilder.loadTexts:prtCfgParamInbandLoopDeactPattern.setStatus(_A)
_PrtT1E1_ObjectIdentity=ObjectIdentity
prtT1E1=_PrtT1E1_ObjectIdentity((1,3,6,1,4,1,164,3,3,3,2))
_PrtT1E1StatTable_Object=MibTable
prtT1E1StatTable=_PrtT1E1StatTable_Object((1,3,6,1,4,1,164,3,3,3,2,1))
if mibBuilder.loadTexts:prtT1E1StatTable.setStatus(_A)
_PrtT1E1StatEntry_Object=MibTableRow
prtT1E1StatEntry=_PrtT1E1StatEntry_Object((1,3,6,1,4,1,164,3,3,3,2,1,1))
prtT1E1StatEntry.setIndexNames((0,_F,_BA))
if mibBuilder.loadTexts:prtT1E1StatEntry.setStatus(_A)
_PrtT1E1SPrtIdx_Type=Integer32
_PrtT1E1SPrtIdx_Object=MibTableColumn
prtT1E1SPrtIdx=_PrtT1E1SPrtIdx_Object((1,3,6,1,4,1,164,3,3,3,2,1,1,1),_PrtT1E1SPrtIdx_Type())
prtT1E1SPrtIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtT1E1SPrtIdx.setStatus(_A)
class _PrtT1E1SSlt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,255)));namedValues=NamedValues(*((_v,3),(_w,4),(_T,5),(_U,6),(_V,7),(_W,8),(_X,9),(_Y,10),(_Z,11),(_a,12),(_b,13),(_e,14),(_f,15),(_g,16),(_h,17),(_i,18),(_j,19),(_t,255)))
_PrtT1E1SSlt_Type.__name__=_B
_PrtT1E1SSlt_Object=MibTableColumn
prtT1E1SSlt=_PrtT1E1SSlt_Object((1,3,6,1,4,1,164,3,3,3,2,1,1,2),_PrtT1E1SSlt_Type())
prtT1E1SSlt.setMaxAccess(_C)
if mibBuilder.loadTexts:prtT1E1SSlt.setStatus(_A)
_PrtT1E1OosCount_Type=Gauge32
_PrtT1E1OosCount_Object=MibTableColumn
prtT1E1OosCount=_PrtT1E1OosCount_Object((1,3,6,1,4,1,164,3,3,3,2,1,1,3),_PrtT1E1OosCount_Type())
prtT1E1OosCount.setMaxAccess(_C)
if mibBuilder.loadTexts:prtT1E1OosCount.setStatus(_A)
_PrtT1E1BpvLastMin_Type=Gauge32
_PrtT1E1BpvLastMin_Object=MibTableColumn
prtT1E1BpvLastMin=_PrtT1E1BpvLastMin_Object((1,3,6,1,4,1,164,3,3,3,2,1,1,4),_PrtT1E1BpvLastMin_Type())
prtT1E1BpvLastMin.setMaxAccess(_C)
if mibBuilder.loadTexts:prtT1E1BpvLastMin.setStatus(_A)
_PrtT1E1BpvMax_Type=Gauge32
_PrtT1E1BpvMax_Object=MibTableColumn
prtT1E1BpvMax=_PrtT1E1BpvMax_Object((1,3,6,1,4,1,164,3,3,3,2,1,1,5),_PrtT1E1BpvMax_Type())
prtT1E1BpvMax.setMaxAccess(_C)
if mibBuilder.loadTexts:prtT1E1BpvMax.setStatus(_A)
_PrtT1E1CnfgTable_Object=MibTable
prtT1E1CnfgTable=_PrtT1E1CnfgTable_Object((1,3,6,1,4,1,164,3,3,3,2,2))
if mibBuilder.loadTexts:prtT1E1CnfgTable.setStatus(_A)
_PrtT1E1CnfgEntry_Object=MibTableRow
prtT1E1CnfgEntry=_PrtT1E1CnfgEntry_Object((1,3,6,1,4,1,164,3,3,3,2,2,1))
prtT1E1CnfgEntry.setIndexNames((0,_F,_BB),(0,_F,_BC))
if mibBuilder.loadTexts:prtT1E1CnfgEntry.setStatus(_A)
class _PrtT1E1CnfgIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PrtT1E1CnfgIdx_Type.__name__=_B
_PrtT1E1CnfgIdx_Object=MibTableColumn
prtT1E1CnfgIdx=_PrtT1E1CnfgIdx_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,1),_PrtT1E1CnfgIdx_Type())
prtT1E1CnfgIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtT1E1CnfgIdx.setStatus(_A)
_PrtT1E1PrtIdx_Type=Integer32
_PrtT1E1PrtIdx_Object=MibTableColumn
prtT1E1PrtIdx=_PrtT1E1PrtIdx_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,2),_PrtT1E1PrtIdx_Type())
prtT1E1PrtIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtT1E1PrtIdx.setStatus(_A)
class _PrtT1E1Slt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,103,104,106,107,108,109,110,111,112,113,114,115,116,117,118,255)));namedValues=NamedValues(*((_v,3),(_w,4),(_T,5),(_U,6),(_V,7),(_W,8),(_X,9),(_Y,10),(_Z,11),(_a,12),(_b,13),(_e,14),(_f,15),(_g,16),(_h,17),(_i,18),(_j,19),(_A7,103),(_A8,104),(_AT,106),(_A9,107),(_AA,108),(_AB,109),(_AC,110),(_AD,111),(_AE,112),(_AF,113),(_AG,114),(_AH,115),(_AI,116),(_AJ,117),(_AK,118),(_t,255)))
_PrtT1E1Slt_Type.__name__=_B
_PrtT1E1Slt_Object=MibTableColumn
prtT1E1Slt=_PrtT1E1Slt_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,3),_PrtT1E1Slt_Type())
prtT1E1Slt.setMaxAccess(_C)
if mibBuilder.loadTexts:prtT1E1Slt.setStatus(_A)
class _PrtT1E1LineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_s,1),('esf',2),('d4',3),('e1',4),('e1Crc',5),('e1MF',6),('e1CrcMF',7),('unframed',8)))
_PrtT1E1LineType_Type.__name__=_B
_PrtT1E1LineType_Object=MibTableColumn
prtT1E1LineType=_PrtT1E1LineType_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,4),_PrtT1E1LineType_Type())
prtT1E1LineType.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1LineType.setStatus(_A)
class _PrtT1E1LineCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('jbzs',1),('b8zs',2),('hdb3',3),('zbtsi',4),('ami',5),(_s,6)))
_PrtT1E1LineCode_Type.__name__=_B
_PrtT1E1LineCode_Object=MibTableColumn
prtT1E1LineCode=_PrtT1E1LineCode_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,5),_PrtT1E1LineCode_Type())
prtT1E1LineCode.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1LineCode.setStatus(_A)
class _PrtT1E1SignalMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_c,1),('robbedBit',2),('bitOriented',3),('messageOriented',4)))
_PrtT1E1SignalMode_Type.__name__=_B
_PrtT1E1SignalMode_Object=MibTableColumn
prtT1E1SignalMode=_PrtT1E1SignalMode_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,6),_PrtT1E1SignalMode_Type())
prtT1E1SignalMode.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1SignalMode.setStatus(_A)
class _PrtT1E1Fdl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16)));namedValues=NamedValues(*((_s,1),('ansi-T1-403',2),('att-54016',4),('fdl-none',8),('transFdl',16)))
_PrtT1E1Fdl_Type.__name__=_B
_PrtT1E1Fdl_Object=MibTableColumn
prtT1E1Fdl=_PrtT1E1Fdl_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,7),_PrtT1E1Fdl_Type())
prtT1E1Fdl.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1Fdl.setStatus(_A)
class _PrtT1E1FdlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*((_s,1),('user',2),('carrier',3),(_E,255)))
_PrtT1E1FdlMode_Type.__name__=_B
_PrtT1E1FdlMode_Object=MibTableColumn
prtT1E1FdlMode=_PrtT1E1FdlMode_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,8),_PrtT1E1FdlMode_Type())
prtT1E1FdlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1FdlMode.setStatus(_A)
class _PrtT1E1Sync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_s,1),('tr62411',2),('ccitt',3),('fast',4)))
_PrtT1E1Sync_Type.__name__=_B
_PrtT1E1Sync_Object=MibTableColumn
prtT1E1Sync=_PrtT1E1Sync_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,9),_PrtT1E1Sync_Type())
prtT1E1Sync.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1Sync.setStatus(_A)
class _PrtT1E1CGA_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),('trans',2),('full',3)))
_PrtT1E1CGA_Type.__name__=_B
_PrtT1E1CGA_Object=MibTableColumn
prtT1E1CGA=_PrtT1E1CGA_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,10),_PrtT1E1CGA_Type())
prtT1E1CGA.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1CGA.setStatus(_A)
class _PrtT1E1IdleCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_PrtT1E1IdleCode_Type.__name__=_l
_PrtT1E1IdleCode_Object=MibTableColumn
prtT1E1IdleCode=_PrtT1E1IdleCode_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,11),_PrtT1E1IdleCode_Type())
prtT1E1IdleCode.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1IdleCode.setStatus(_A)
class _PrtT1E1OosSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6)));namedValues=NamedValues(*(('notsupported',2),('forcedIdle',3),('forcedBusy',4),('busyIdle',5),('idleBusy',6)))
_PrtT1E1OosSignal_Type.__name__=_B
_PrtT1E1OosSignal_Object=MibTableColumn
prtT1E1OosSignal=_PrtT1E1OosSignal_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,12),_PrtT1E1OosSignal_Type())
prtT1E1OosSignal.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1OosSignal.setStatus(_A)
class _PrtT1E1VoiceOos_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_PrtT1E1VoiceOos_Type.__name__=_l
_PrtT1E1VoiceOos_Object=MibTableColumn
prtT1E1VoiceOos=_PrtT1E1VoiceOos_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,13),_PrtT1E1VoiceOos_Type())
prtT1E1VoiceOos.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1VoiceOos.setStatus(_A)
class _PrtT1E1DataOos_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_PrtT1E1DataOos_Type.__name__=_l
_PrtT1E1DataOos_Object=MibTableColumn
prtT1E1DataOos=_PrtT1E1DataOos_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,14),_PrtT1E1DataOos_Type())
prtT1E1DataOos.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1DataOos.setStatus(_A)
class _PrtT1E1LineLengthMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_u,1),('len0p133ft',2),('len134p266ft',3),('len267p399ft',4),('len400p533ft',5),('len534p655ft',6),('fcc68',7)))
_PrtT1E1LineLengthMask_Type.__name__=_B
_PrtT1E1LineLengthMask_Object=MibTableColumn
prtT1E1LineLengthMask=_PrtT1E1LineLengthMask_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,15),_PrtT1E1LineLengthMask_Type())
prtT1E1LineLengthMask.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1LineLengthMask.setStatus(_A)
class _PrtT1E1TxGainMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('txGain0db',2),('txGain7dot5db',3),('txGain15db',4),('txGain22dot5db',5)))
_PrtT1E1TxGainMask_Type.__name__=_B
_PrtT1E1TxGainMask_Object=MibTableColumn
prtT1E1TxGainMask=_PrtT1E1TxGainMask_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,16),_PrtT1E1TxGainMask_Type())
prtT1E1TxGainMask.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1TxGainMask.setStatus(_A)
class _PrtT1E1InbandMng_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7)));namedValues=NamedValues(*((_H,2),('fdlOrTs0',3),('dedicatedTs',4),('dedicatedPpp',5),(_BD,6),(_z,7)))
_PrtT1E1InbandMng_Type.__name__=_B
_PrtT1E1InbandMng_Object=MibTableColumn
prtT1E1InbandMng=_PrtT1E1InbandMng_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,17),_PrtT1E1InbandMng_Type())
prtT1E1InbandMng.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1InbandMng.setStatus(_A)
class _PrtT1E1InbandMngRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,1),('r4k',2),('r8k',3),('r12k',4),('r16k',5),('r32k',6),('r64k',7),('r20k',8)))
_PrtT1E1InbandMngRate_Type.__name__=_B
_PrtT1E1InbandMngRate_Object=MibTableColumn
prtT1E1InbandMngRate=_PrtT1E1InbandMngRate_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,18),_PrtT1E1InbandMngRate_Type())
prtT1E1InbandMngRate.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1InbandMngRate.setStatus(_A)
_PrtT1E1DedicatedTs_Type=Integer32
_PrtT1E1DedicatedTs_Object=MibTableColumn
prtT1E1DedicatedTs=_PrtT1E1DedicatedTs_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,19),_PrtT1E1DedicatedTs_Type())
prtT1E1DedicatedTs.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1DedicatedTs.setStatus(_A)
class _PrtT1E1InbandMngRoutProt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_c,2),(_A1,3),(_AL,4)))
_PrtT1E1InbandMngRoutProt_Type.__name__=_B
_PrtT1E1InbandMngRoutProt_Object=MibTableColumn
prtT1E1InbandMngRoutProt=_PrtT1E1InbandMngRoutProt_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,20),_PrtT1E1InbandMngRoutProt_Type())
prtT1E1InbandMngRoutProt.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1InbandMngRoutProt.setStatus(_A)
class _PrtT1E1LinkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('regular',2),('transparent',3)))
_PrtT1E1LinkMode_Type.__name__=_B
_PrtT1E1LinkMode_Object=MibTableColumn
prtT1E1LinkMode=_PrtT1E1LinkMode_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,21),_PrtT1E1LinkMode_Type())
prtT1E1LinkMode.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1LinkMode.setStatus(_A)
class _PrtT1E1Multiplier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('br56',2),('br64',3)))
_PrtT1E1Multiplier_Type.__name__=_B
_PrtT1E1Multiplier_Object=MibTableColumn
prtT1E1Multiplier=_PrtT1E1Multiplier_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,22),_PrtT1E1Multiplier_Type())
prtT1E1Multiplier.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1Multiplier.setStatus(_A)
class _PrtT1E1RxGain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),('rxGain12dB',2),('rxGain30dB',3),('rxGain36dB',4),('shortHaul',5),('longHaul',6),('rxGain20dB',7)))
_PrtT1E1RxGain_Type.__name__=_B
_PrtT1E1RxGain_Object=MibTableColumn
prtT1E1RxGain=_PrtT1E1RxGain_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,23),_PrtT1E1RxGain_Type())
prtT1E1RxGain.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1RxGain.setStatus(_A)
class _PrtT1E1RAI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_H,2),(_I,3)))
_PrtT1E1RAI_Type.__name__=_B
_PrtT1E1RAI_Object=MibTableColumn
prtT1E1RAI=_PrtT1E1RAI_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,24),_PrtT1E1RAI_Type())
prtT1E1RAI.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1RAI.setStatus(_A)
class _PrtT1E1LineMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('csu',2),('dsu',3),('ltu',4)))
_PrtT1E1LineMode_Type.__name__=_B
_PrtT1E1LineMode_Object=MibTableColumn
prtT1E1LineMode=_PrtT1E1LineMode_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,25),_PrtT1E1LineMode_Type())
prtT1E1LineMode.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1LineMode.setStatus(_A)
_PrtT1E1TS0SaBits_Type=OctetString
_PrtT1E1TS0SaBits_Object=MibTableColumn
prtT1E1TS0SaBits=_PrtT1E1TS0SaBits_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,26),_PrtT1E1TS0SaBits_Type())
prtT1E1TS0SaBits.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1TS0SaBits.setStatus(_A)
class _PrtT1E1ConnectedTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_p,2),(_q,3)))
_PrtT1E1ConnectedTS_Type.__name__=_B
_PrtT1E1ConnectedTS_Object=MibTableColumn
prtT1E1ConnectedTS=_PrtT1E1ConnectedTS_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,27),_PrtT1E1ConnectedTS_Type())
prtT1E1ConnectedTS.setMaxAccess(_C)
if mibBuilder.loadTexts:prtT1E1ConnectedTS.setStatus(_A)
class _PrtT1E1Ts0SaBit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('noMng',2),('mng',3)))
_PrtT1E1Ts0SaBit_Type.__name__=_B
_PrtT1E1Ts0SaBit_Object=MibTableColumn
prtT1E1Ts0SaBit=_PrtT1E1Ts0SaBit_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,28),_PrtT1E1Ts0SaBit_Type())
prtT1E1Ts0SaBit.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1Ts0SaBit.setStatus(_A)
class _PrtT1E1SameFeCnfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_p,2),(_q,3)))
_PrtT1E1SameFeCnfg_Type.__name__=_B
_PrtT1E1SameFeCnfg_Object=MibTableColumn
prtT1E1SameFeCnfg=_PrtT1E1SameFeCnfg_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,29),_PrtT1E1SameFeCnfg_Type())
prtT1E1SameFeCnfg.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1SameFeCnfg.setStatus(_A)
class _PrtT1E1RemCrc4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_p,2),(_q,3)))
_PrtT1E1RemCrc4_Type.__name__=_B
_PrtT1E1RemCrc4_Object=MibTableColumn
prtT1E1RemCrc4=_PrtT1E1RemCrc4_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,30),_PrtT1E1RemCrc4_Type())
prtT1E1RemCrc4.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1RemCrc4.setStatus(_A)
_PrtT1E1MaxTSs_Type=Integer32
_PrtT1E1MaxTSs_Object=MibTableColumn
prtT1E1MaxTSs=_PrtT1E1MaxTSs_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,31),_PrtT1E1MaxTSs_Type())
prtT1E1MaxTSs.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1MaxTSs.setStatus(_A)
class _PrtT1E1EocTsConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_y,2),(_A0,3)))
_PrtT1E1EocTsConfig_Type.__name__=_B
_PrtT1E1EocTsConfig_Object=MibTableColumn
prtT1E1EocTsConfig=_PrtT1E1EocTsConfig_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,32),_PrtT1E1EocTsConfig_Type())
prtT1E1EocTsConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1EocTsConfig.setStatus(_A)
class _PrtT1E1Role_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('sub',2),('main',3)))
_PrtT1E1Role_Type.__name__=_B
_PrtT1E1Role_Object=MibTableColumn
prtT1E1Role=_PrtT1E1Role_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,33),_PrtT1E1Role_Type())
prtT1E1Role.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1Role.setStatus(_A)
class _PrtT1E1PppEchoFailDetection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_AM,2),(_AN,3)))
_PrtT1E1PppEchoFailDetection_Type.__name__=_B
_PrtT1E1PppEchoFailDetection_Object=MibTableColumn
prtT1E1PppEchoFailDetection=_PrtT1E1PppEchoFailDetection_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,34),_PrtT1E1PppEchoFailDetection_Type())
prtT1E1PppEchoFailDetection.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1PppEchoFailDetection.setStatus(_A)
class _PrtT1E1CasOosPattern_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('space',1),('mark',2),('spaceMark',3)))
_PrtT1E1CasOosPattern_Type.__name__=_B
_PrtT1E1CasOosPattern_Object=MibTableColumn
prtT1E1CasOosPattern=_PrtT1E1CasOosPattern_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,36),_PrtT1E1CasOosPattern_Type())
prtT1E1CasOosPattern.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1CasOosPattern.setStatus(_A)
class _PrtT1E1CasOosSpaceCode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_PrtT1E1CasOosSpaceCode_Type.__name__=_A4
_PrtT1E1CasOosSpaceCode_Object=MibTableColumn
prtT1E1CasOosSpaceCode=_PrtT1E1CasOosSpaceCode_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,37),_PrtT1E1CasOosSpaceCode_Type())
prtT1E1CasOosSpaceCode.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1CasOosSpaceCode.setStatus(_A)
class _PrtT1E1CasOosMarkCode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_PrtT1E1CasOosMarkCode_Type.__name__=_A4
_PrtT1E1CasOosMarkCode_Object=MibTableColumn
prtT1E1CasOosMarkCode=_PrtT1E1CasOosMarkCode_Object((1,3,6,1,4,1,164,3,3,3,2,2,1,38),_PrtT1E1CasOosMarkCode_Type())
prtT1E1CasOosMarkCode.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT1E1CasOosMarkCode.setStatus(_A)
_PrtT1E1FdlMsgTable_Object=MibTable
prtT1E1FdlMsgTable=_PrtT1E1FdlMsgTable_Object((1,3,6,1,4,1,164,3,3,3,2,3))
if mibBuilder.loadTexts:prtT1E1FdlMsgTable.setStatus(_A)
_PrtT1E1FdlMsgEntry_Object=MibTableRow
prtT1E1FdlMsgEntry=_PrtT1E1FdlMsgEntry_Object((1,3,6,1,4,1,164,3,3,3,2,3,1))
prtT1E1FdlMsgEntry.setIndexNames((0,_F,_BE),(0,_F,_BF))
if mibBuilder.loadTexts:prtT1E1FdlMsgEntry.setStatus(_A)
_PrtT1E1FdlMsgPrtIdx_Type=Integer32
_PrtT1E1FdlMsgPrtIdx_Object=MibTableColumn
prtT1E1FdlMsgPrtIdx=_PrtT1E1FdlMsgPrtIdx_Object((1,3,6,1,4,1,164,3,3,3,2,3,1,1),_PrtT1E1FdlMsgPrtIdx_Type())
prtT1E1FdlMsgPrtIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtT1E1FdlMsgPrtIdx.setStatus(_A)
class _PrtT1E1FdlMsgFdlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('send',1),('receive',2)))
_PrtT1E1FdlMsgFdlType_Type.__name__=_B
_PrtT1E1FdlMsgFdlType_Object=MibTableColumn
prtT1E1FdlMsgFdlType=_PrtT1E1FdlMsgFdlType_Object((1,3,6,1,4,1,164,3,3,3,2,3,1,2),_PrtT1E1FdlMsgFdlType_Type())
prtT1E1FdlMsgFdlType.setMaxAccess(_C)
if mibBuilder.loadTexts:prtT1E1FdlMsgFdlType.setStatus(_A)
class _PrtT1E1FdlMsgSlt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,255)));namedValues=NamedValues(*((_T,5),(_U,6),(_V,7),(_W,8),(_X,9),(_Y,10),(_Z,11),(_a,12),(_b,13),(_e,14),(_f,15),(_g,16),(_h,17),(_i,18),(_j,19),(_t,255)))
_PrtT1E1FdlMsgSlt_Type.__name__=_B
_PrtT1E1FdlMsgSlt_Object=MibTableColumn
prtT1E1FdlMsgSlt=_PrtT1E1FdlMsgSlt_Object((1,3,6,1,4,1,164,3,3,3,2,3,1,3),_PrtT1E1FdlMsgSlt_Type())
prtT1E1FdlMsgSlt.setMaxAccess(_C)
if mibBuilder.loadTexts:prtT1E1FdlMsgSlt.setStatus(_A)
_PrtT1E1FdlMsg_Type=OctetString
_PrtT1E1FdlMsg_Object=MibTableColumn
prtT1E1FdlMsg=_PrtT1E1FdlMsg_Object((1,3,6,1,4,1,164,3,3,3,2,3,1,4),_PrtT1E1FdlMsg_Type())
prtT1E1FdlMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:prtT1E1FdlMsg.setStatus(_A)
_PrtHS_ObjectIdentity=ObjectIdentity
prtHS=_PrtHS_ObjectIdentity((1,3,6,1,4,1,164,3,3,3,3))
_PrtHSParamTable_Object=MibTable
prtHSParamTable=_PrtHSParamTable_Object((1,3,6,1,4,1,164,3,3,3,3,1))
if mibBuilder.loadTexts:prtHSParamTable.setStatus(_A)
_PrtHSParamEntry_Object=MibTableRow
prtHSParamEntry=_PrtHSParamEntry_Object((1,3,6,1,4,1,164,3,3,3,3,1,1))
prtHSParamEntry.setIndexNames((0,_F,_BG),(0,_F,_BH))
if mibBuilder.loadTexts:prtHSParamEntry.setStatus(_A)
class _PrtHSCnfgIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PrtHSCnfgIdx_Type.__name__=_B
_PrtHSCnfgIdx_Object=MibTableColumn
prtHSCnfgIdx=_PrtHSCnfgIdx_Object((1,3,6,1,4,1,164,3,3,3,3,1,1,1),_PrtHSCnfgIdx_Type())
prtHSCnfgIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtHSCnfgIdx.setStatus(_A)
_PrtHSPrtIdx_Type=Integer32
_PrtHSPrtIdx_Object=MibTableColumn
prtHSPrtIdx=_PrtHSPrtIdx_Object((1,3,6,1,4,1,164,3,3,3,3,1,1,2),_PrtHSPrtIdx_Type())
prtHSPrtIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtHSPrtIdx.setStatus(_A)
class _PrtHSSlt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,255)));namedValues=NamedValues(*((_T,5),(_U,6),(_V,7),(_W,8),(_X,9),(_Y,10),(_Z,11),(_a,12),(_b,13),(_e,14),(_f,15),(_g,16),(_h,17),(_i,18),(_j,19),(_t,255)))
_PrtHSSlt_Type.__name__=_B
_PrtHSSlt_Object=MibTableColumn
prtHSSlt=_PrtHSSlt_Object((1,3,6,1,4,1,164,3,3,3,3,1,1,3),_PrtHSSlt_Type())
prtHSSlt.setMaxAccess(_C)
if mibBuilder.loadTexts:prtHSSlt.setStatus(_A)
class _PrtHSRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,200)));namedValues=NamedValues(*(('r0x56eq0Kbps',1),('r1x56eq56Kbps',2),('r2x56eq112Kbps',3),('r3x56eq168Kbps',4),('r4x56eq224Kbps',5),('r5x56eq280Kbps',6),('r6x56eq336Kbps',7),('r7x56eq392Kbps',8),('r8x56eq448Kbps',9),('r9x56eq504Kbps',10),('r10x56eq560Kbps',11),('r11x56eq616Kbps',12),('r12x56eq672Kbps',13),('r13x56eq728Kbps',14),('r14x56eq784Kbps',15),('r15x56eq840Kbps',16),('r16x56eq896Kbps',17),('r17x56eq952Kbps',18),('r18x56eq1008Kbps',19),('r19x56eq1064Kbps',20),('r20x56eq1120Kbps',21),('r21x56eq1176Kbps',22),('r22x56eq1232Kbps',23),('r23x56eq1288Kbps',24),('r24x56eq1344Kbps',25),('r25x56eq1400Kbps',26),('r26x56eq1456Kbps',27),('r27x56eq1512Kbps',28),('r28x56eq1568Kbps',29),('r29x56eq1624Kbps',30),('r30x56eq1680Kbps',31),('r31x56eq1736Kbps',32),('r0x64eq0Kbps',33),('r1x64eq64Kbps',34),('r2x64eq128Kbps',35),('r3x64eq192Kbps',36),('r4x64eq256Kbps',37),('r5x64eq320Kbps',38),('r6x64eq384Kbps',39),('r7x64eq448Kbps',40),('r8x64eq512Kbps',41),('r9x64eq576Kbps',42),('r10x64eq640Kbps',43),('r11x64eq704Kbps',44),('r12x64eq768Kbps',45),('r13x64eq832Kbps',46),('r14x64eq896Kbps',47),('r15x64eq960Kbps',48),('r16x64eq1024Kbps',49),('r17x64eq1088Kbps',50),('r18x64eq1152Kbps',51),('r19x64eq1216Kbps',52),('r20x64eq1280Kbps',53),('r21x64eq1344Kbps',54),('r22x64eq1408Kbps',55),('r23x64eq1472Kbps',56),('r24x64eq1536Kbps',57),('r25x64eq1600Kbps',58),('r26x64eq1664Kbps',59),('r27x64eq1728Kbps',60),('r28x64eq1792Kbps',61),('r29x64eq1856Kbps',62),('r30x64eq1920Kbps',63),('r31x64eq1984Kbps',64),('r32x64eq2048Kbps',65),('r32x56eq1792Kbps',66),('r64x64eq4096Kbps',67),(_x,200)))
_PrtHSRate_Type.__name__=_B
_PrtHSRate_Object=MibTableColumn
prtHSRate=_PrtHSRate_Object((1,3,6,1,4,1,164,3,3,3,3,1,1,4),_PrtHSRate_Type())
prtHSRate.setMaxAccess(_D)
if mibBuilder.loadTexts:prtHSRate.setStatus(_A)
class _PrtHSFifoSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,255)));namedValues=NamedValues(*((_x,1),('b32bit',2),('b60bit',3),('b104bit',4),('b144bit',5),(_E,255)))
_PrtHSFifoSize_Type.__name__=_B
_PrtHSFifoSize_Object=MibTableColumn
prtHSFifoSize=_PrtHSFifoSize_Object((1,3,6,1,4,1,164,3,3,3,3,1,1,5),_PrtHSFifoSize_Type())
prtHSFifoSize.setMaxAccess(_D)
if mibBuilder.loadTexts:prtHSFifoSize.setStatus(_A)
class _PrtHSClkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*(('dce',1),('dte1',2),('dte2',3),(_E,255)))
_PrtHSClkMode_Type.__name__=_B
_PrtHSClkMode_Object=MibTableColumn
prtHSClkMode=_PrtHSClkMode_Object((1,3,6,1,4,1,164,3,3,3,3,1,1,6),_PrtHSClkMode_Type())
prtHSClkMode.setMaxAccess(_D)
if mibBuilder.loadTexts:prtHSClkMode.setStatus(_A)
class _PrtHSCTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_I,1),('rts',2),(_E,255)))
_PrtHSCTS_Type.__name__=_B
_PrtHSCTS_Object=MibTableColumn
prtHSCTS=_PrtHSCTS_Object((1,3,6,1,4,1,164,3,3,3,3,1,1,7),_PrtHSCTS_Type())
prtHSCTS.setMaxAccess(_D)
if mibBuilder.loadTexts:prtHSCTS.setStatus(_A)
class _PrtHSRtsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,255)));namedValues=NamedValues(*((_H,2),(_I,3),(_E,255)))
_PrtHSRtsState_Type.__name__=_B
_PrtHSRtsState_Object=MibTableColumn
prtHSRtsState=_PrtHSRtsState_Object((1,3,6,1,4,1,164,3,3,3,3,1,1,8),_PrtHSRtsState_Type())
prtHSRtsState.setMaxAccess(_C)
if mibBuilder.loadTexts:prtHSRtsState.setStatus(_A)
class _PrtHSInbandLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_y,2),(_A0,3)))
_PrtHSInbandLoopback_Type.__name__=_B
_PrtHSInbandLoopback_Object=MibTableColumn
prtHSInbandLoopback=_PrtHSInbandLoopback_Object((1,3,6,1,4,1,164,3,3,3,3,1,1,9),_PrtHSInbandLoopback_Type())
prtHSInbandLoopback.setMaxAccess(_D)
if mibBuilder.loadTexts:prtHSInbandLoopback.setStatus(_A)
class _PrtHSInbandLoopPatternCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('rdlLoop',2),(_B9,3)))
_PrtHSInbandLoopPatternCfg_Type.__name__=_B
_PrtHSInbandLoopPatternCfg_Object=MibTableColumn
prtHSInbandLoopPatternCfg=_PrtHSInbandLoopPatternCfg_Object((1,3,6,1,4,1,164,3,3,3,3,1,1,10),_PrtHSInbandLoopPatternCfg_Type())
prtHSInbandLoopPatternCfg.setMaxAccess(_D)
if mibBuilder.loadTexts:prtHSInbandLoopPatternCfg.setStatus(_A)
_PrtHSInbandLoopActPattern_Type=DisplayString
_PrtHSInbandLoopActPattern_Object=MibTableColumn
prtHSInbandLoopActPattern=_PrtHSInbandLoopActPattern_Object((1,3,6,1,4,1,164,3,3,3,3,1,1,11),_PrtHSInbandLoopActPattern_Type())
prtHSInbandLoopActPattern.setMaxAccess(_D)
if mibBuilder.loadTexts:prtHSInbandLoopActPattern.setStatus(_A)
_PrtHSInbandLoopDeactPattern_Type=DisplayString
_PrtHSInbandLoopDeactPattern_Object=MibTableColumn
prtHSInbandLoopDeactPattern=_PrtHSInbandLoopDeactPattern_Object((1,3,6,1,4,1,164,3,3,3,3,1,1,12),_PrtHSInbandLoopDeactPattern_Type())
prtHSInbandLoopDeactPattern.setMaxAccess(_D)
if mibBuilder.loadTexts:prtHSInbandLoopDeactPattern.setStatus(_A)
class _PrtHSDCD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('linkOK',2),(_I,3)))
_PrtHSDCD_Type.__name__=_B
_PrtHSDCD_Object=MibTableColumn
prtHSDCD=_PrtHSDCD_Object((1,3,6,1,4,1,164,3,3,3,3,1,1,13),_PrtHSDCD_Type())
prtHSDCD.setMaxAccess(_D)
if mibBuilder.loadTexts:prtHSDCD.setStatus(_A)
class _PrtHSClkPolarity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_AU,2),('invert',3)))
_PrtHSClkPolarity_Type.__name__=_B
_PrtHSClkPolarity_Object=MibTableColumn
prtHSClkPolarity=_PrtHSClkPolarity_Object((1,3,6,1,4,1,164,3,3,3,3,1,1,14),_PrtHSClkPolarity_Type())
prtHSClkPolarity.setMaxAccess(_D)
if mibBuilder.loadTexts:prtHSClkPolarity.setStatus(_A)
class _PrtHSInterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_E,1),('rs530',2),('v35',3),('rs422',4),('x21',5),('v24',6),('rs530a',7),('rs232',8),('rs449',9)))
_PrtHSInterfaceType_Type.__name__=_B
_PrtHSInterfaceType_Object=MibTableColumn
prtHSInterfaceType=_PrtHSInterfaceType_Object((1,3,6,1,4,1,164,3,3,3,3,1,1,15),_PrtHSInterfaceType_Type())
prtHSInterfaceType.setMaxAccess(_D)
if mibBuilder.loadTexts:prtHSInterfaceType.setStatus(_A)
class _PrtHSUnframed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_p,2),(_q,3)))
_PrtHSUnframed_Type.__name__=_B
_PrtHSUnframed_Object=MibTableColumn
prtHSUnframed=_PrtHSUnframed_Object((1,3,6,1,4,1,164,3,3,3,3,1,1,16),_PrtHSUnframed_Type())
prtHSUnframed.setMaxAccess(_D)
if mibBuilder.loadTexts:prtHSUnframed.setStatus(_A)
_PrtHSBertTable_Object=MibTable
prtHSBertTable=_PrtHSBertTable_Object((1,3,6,1,4,1,164,3,3,3,3,2))
if mibBuilder.loadTexts:prtHSBertTable.setStatus(_A)
_PrtHSBertEntry_Object=MibTableRow
prtHSBertEntry=_PrtHSBertEntry_Object((1,3,6,1,4,1,164,3,3,3,3,2,1))
prtHSBertEntry.setIndexNames((0,_F,_BI))
if mibBuilder.loadTexts:prtHSBertEntry.setStatus(_A)
_PrtHSBertPrtIdx_Type=Integer32
_PrtHSBertPrtIdx_Object=MibTableColumn
prtHSBertPrtIdx=_PrtHSBertPrtIdx_Object((1,3,6,1,4,1,164,3,3,3,3,2,1,1),_PrtHSBertPrtIdx_Type())
prtHSBertPrtIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtHSBertPrtIdx.setStatus(_A)
class _PrtHSBertSlt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,255)));namedValues=NamedValues(*((_T,5),(_U,6),(_V,7),(_W,8),(_X,9),(_Y,10),(_Z,11),(_a,12),(_b,13),(_e,14),(_f,15),(_g,16),(_h,17),(_i,18),(_j,19),(_t,255)))
_PrtHSBertSlt_Type.__name__=_B
_PrtHSBertSlt_Object=MibTableColumn
prtHSBertSlt=_PrtHSBertSlt_Object((1,3,6,1,4,1,164,3,3,3,3,2,1,2),_PrtHSBertSlt_Type())
prtHSBertSlt.setMaxAccess(_C)
if mibBuilder.loadTexts:prtHSBertSlt.setStatus(_A)
class _PrtHSBertCountClr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_H,2),(_I,3)))
_PrtHSBertCountClr_Type.__name__=_B
_PrtHSBertCountClr_Object=MibTableColumn
prtHSBertCountClr=_PrtHSBertCountClr_Object((1,3,6,1,4,1,164,3,3,3,3,2,1,3),_PrtHSBertCountClr_Type())
prtHSBertCountClr.setMaxAccess(_D)
if mibBuilder.loadTexts:prtHSBertCountClr.setStatus(_A)
_PrtHSBertTestResult_Type=Integer32
_PrtHSBertTestResult_Object=MibTableColumn
prtHSBertTestResult=_PrtHSBertTestResult_Object((1,3,6,1,4,1,164,3,3,3,3,2,1,4),_PrtHSBertTestResult_Type())
prtHSBertTestResult.setMaxAccess(_C)
if mibBuilder.loadTexts:prtHSBertTestResult.setStatus(_A)
_PrtSP_ObjectIdentity=ObjectIdentity
prtSP=_PrtSP_ObjectIdentity((1,3,6,1,4,1,164,3,3,3,4))
_PrtSpCnfgTable_Object=MibTable
prtSpCnfgTable=_PrtSpCnfgTable_Object((1,3,6,1,4,1,164,3,3,3,4,1))
if mibBuilder.loadTexts:prtSpCnfgTable.setStatus(_A)
_PrtSpCnfgEntry_Object=MibTableRow
prtSpCnfgEntry=_PrtSpCnfgEntry_Object((1,3,6,1,4,1,164,3,3,3,4,1,1))
prtSpCnfgEntry.setIndexNames((0,_F,_BJ),(0,_F,_BK))
if mibBuilder.loadTexts:prtSpCnfgEntry.setStatus(_A)
class _PrtSpCnfgIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PrtSpCnfgIdx_Type.__name__=_B
_PrtSpCnfgIdx_Object=MibTableColumn
prtSpCnfgIdx=_PrtSpCnfgIdx_Object((1,3,6,1,4,1,164,3,3,3,4,1,1,1),_PrtSpCnfgIdx_Type())
prtSpCnfgIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtSpCnfgIdx.setStatus(_A)
_PrtSpPrtIdx_Type=Integer32
_PrtSpPrtIdx_Object=MibTableColumn
prtSpPrtIdx=_PrtSpPrtIdx_Object((1,3,6,1,4,1,164,3,3,3,4,1,1,2),_PrtSpPrtIdx_Type())
prtSpPrtIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtSpPrtIdx.setStatus(_A)
class _PrtSpUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_u,1),('noUse',2),('nmsSlip',3),('nmsPpp',4),('muxSlip',5),('muxPpp',6),('terminal',7),('dialOut',8)))
_PrtSpUsage_Type.__name__=_B
_PrtSpUsage_Object=MibTableColumn
prtSpUsage=_PrtSpUsage_Object((1,3,6,1,4,1,164,3,3,3,4,1,1,3),_PrtSpUsage_Type())
prtSpUsage.setMaxAccess(_D)
if mibBuilder.loadTexts:prtSpUsage.setStatus(_A)
class _PrtSpRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_x,1),('s300bps',2),('s1200bps',3),('s2400bps',4),('s4800bps',5),('s9600bps',6),('s19200bps',7),('s38400bps',8),('s57600bps',9),('s115200bps',10)))
_PrtSpRate_Type.__name__=_B
_PrtSpRate_Object=MibTableColumn
prtSpRate=_PrtSpRate_Object((1,3,6,1,4,1,164,3,3,3,4,1,1,4),_PrtSpRate_Type())
prtSpRate.setMaxAccess(_D)
if mibBuilder.loadTexts:prtSpRate.setStatus(_A)
class _PrtSpDataBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dataBits7',1),('dataBits8',2)))
_PrtSpDataBits_Type.__name__=_B
_PrtSpDataBits_Object=MibTableColumn
prtSpDataBits=_PrtSpDataBits_Object((1,3,6,1,4,1,164,3,3,3,4,1,1,5),_PrtSpDataBits_Type())
prtSpDataBits.setMaxAccess(_D)
if mibBuilder.loadTexts:prtSpDataBits.setStatus(_A)
class _PrtSpParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),('odd',2),('even',3)))
_PrtSpParity_Type.__name__=_B
_PrtSpParity_Object=MibTableColumn
prtSpParity=_PrtSpParity_Object((1,3,6,1,4,1,164,3,3,3,4,1,1,6),_PrtSpParity_Type())
prtSpParity.setMaxAccess(_D)
if mibBuilder.loadTexts:prtSpParity.setStatus(_A)
class _PrtSpCallOutMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_c,2),('all',3),(_k,4)))
_PrtSpCallOutMode_Type.__name__=_B
_PrtSpCallOutMode_Object=MibTableColumn
prtSpCallOutMode=_PrtSpCallOutMode_Object((1,3,6,1,4,1,164,3,3,3,4,1,1,7),_PrtSpCallOutMode_Type())
prtSpCallOutMode.setMaxAccess(_D)
if mibBuilder.loadTexts:prtSpCallOutMode.setStatus(_A)
class _PrtSpInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dce',1),('dte',2)))
_PrtSpInterface_Type.__name__=_B
_PrtSpInterface_Object=MibTableColumn
prtSpInterface=_PrtSpInterface_Object((1,3,6,1,4,1,164,3,3,3,4,1,1,8),_PrtSpInterface_Type())
prtSpInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:prtSpInterface.setStatus(_A)
class _PrtSpCTS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_I,2),('rts',3)))
_PrtSpCTS_Type.__name__=_B
_PrtSpCTS_Object=MibTableColumn
prtSpCTS=_PrtSpCTS_Object((1,3,6,1,4,1,164,3,3,3,4,1,1,9),_PrtSpCTS_Type())
prtSpCTS.setMaxAccess(_D)
if mibBuilder.loadTexts:prtSpCTS.setStatus(_A)
class _PrtSpDcdDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),('d0',2),('d10',3),('d50',4),('d100',5),('d200',6),('d300',7)))
_PrtSpDcdDelay_Type.__name__=_B
_PrtSpDcdDelay_Object=MibTableColumn
prtSpDcdDelay=_PrtSpDcdDelay_Object((1,3,6,1,4,1,164,3,3,3,4,1,1,10),_PrtSpDcdDelay_Type())
prtSpDcdDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:prtSpDcdDelay.setStatus(_A)
class _PrtSpDsr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_I,2),('dtr',3)))
_PrtSpDsr_Type.__name__=_B
_PrtSpDsr_Object=MibTableColumn
prtSpDsr=_PrtSpDsr_Object((1,3,6,1,4,1,164,3,3,3,4,1,1,11),_PrtSpDsr_Type())
prtSpDsr.setMaxAccess(_D)
if mibBuilder.loadTexts:prtSpDsr.setStatus(_A)
class _PrtSpNoOfRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_PrtSpNoOfRetries_Type.__name__=_B
_PrtSpNoOfRetries_Object=MibTableColumn
prtSpNoOfRetries=_PrtSpNoOfRetries_Object((1,3,6,1,4,1,164,3,3,3,4,1,1,12),_PrtSpNoOfRetries_Type())
prtSpNoOfRetries.setMaxAccess(_D)
if mibBuilder.loadTexts:prtSpNoOfRetries.setStatus(_A)
class _PrtSpWaitForConnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('t30sec',2),('t45sec',3),('t60sec',4)))
_PrtSpWaitForConnect_Type.__name__=_B
_PrtSpWaitForConnect_Object=MibTableColumn
prtSpWaitForConnect=_PrtSpWaitForConnect_Object((1,3,6,1,4,1,164,3,3,3,4,1,1,13),_PrtSpWaitForConnect_Type())
prtSpWaitForConnect.setMaxAccess(_D)
if mibBuilder.loadTexts:prtSpWaitForConnect.setStatus(_A)
class _PrtSpDialMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('tone',2),('pulse',3)))
_PrtSpDialMode_Type.__name__=_B
_PrtSpDialMode_Object=MibTableColumn
prtSpDialMode=_PrtSpDialMode_Object((1,3,6,1,4,1,164,3,3,3,4,1,1,14),_PrtSpDialMode_Type())
prtSpDialMode.setMaxAccess(_D)
if mibBuilder.loadTexts:prtSpDialMode.setStatus(_A)
class _PrtSpAltNumMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_p,2),(_q,3)))
_PrtSpAltNumMode_Type.__name__=_B
_PrtSpAltNumMode_Object=MibTableColumn
prtSpAltNumMode=_PrtSpAltNumMode_Object((1,3,6,1,4,1,164,3,3,3,4,1,1,15),_PrtSpAltNumMode_Type())
prtSpAltNumMode.setMaxAccess(_D)
if mibBuilder.loadTexts:prtSpAltNumMode.setStatus(_A)
class _PrtSpPrimaryNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_PrtSpPrimaryNum_Type.__name__=_J
_PrtSpPrimaryNum_Object=MibTableColumn
prtSpPrimaryNum=_PrtSpPrimaryNum_Object((1,3,6,1,4,1,164,3,3,3,4,1,1,16),_PrtSpPrimaryNum_Type())
prtSpPrimaryNum.setMaxAccess(_D)
if mibBuilder.loadTexts:prtSpPrimaryNum.setStatus(_A)
class _PrtSpAltNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_PrtSpAltNum_Type.__name__=_J
_PrtSpAltNum_Object=MibTableColumn
prtSpAltNum=_PrtSpAltNum_Object((1,3,6,1,4,1,164,3,3,3,4,1,1,17),_PrtSpAltNum_Type())
prtSpAltNum.setMaxAccess(_D)
if mibBuilder.loadTexts:prtSpAltNum.setStatus(_A)
class _PrtSpRoutProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_c,2),(_A1,3),(_AL,4)))
_PrtSpRoutProtocol_Type.__name__=_B
_PrtSpRoutProtocol_Object=MibTableColumn
prtSpRoutProtocol=_PrtSpRoutProtocol_Object((1,3,6,1,4,1,164,3,3,3,4,1,1,18),_PrtSpRoutProtocol_Type())
prtSpRoutProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:prtSpRoutProtocol.setStatus(_A)
class _PrtSpCmd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_PrtSpCmd_Type.__name__=_l
_PrtSpCmd_Object=MibTableColumn
prtSpCmd=_PrtSpCmd_Object((1,3,6,1,4,1,164,3,3,3,4,1,1,19),_PrtSpCmd_Type())
prtSpCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:prtSpCmd.setStatus(_A)
class _PrtSpActCallOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('always',2),('linkFail',3)))
_PrtSpActCallOut_Type.__name__=_B
_PrtSpActCallOut_Object=MibTableColumn
prtSpActCallOut=_PrtSpActCallOut_Object((1,3,6,1,4,1,164,3,3,3,4,1,1,20),_PrtSpActCallOut_Type())
prtSpActCallOut.setMaxAccess(_D)
if mibBuilder.loadTexts:prtSpActCallOut.setStatus(_A)
class _PrtSpAlrRelayMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_AU,2),('invert',3)))
_PrtSpAlrRelayMode_Type.__name__=_B
_PrtSpAlrRelayMode_Object=MibTableColumn
prtSpAlrRelayMode=_PrtSpAlrRelayMode_Object((1,3,6,1,4,1,164,3,3,3,4,1,1,21),_PrtSpAlrRelayMode_Type())
prtSpAlrRelayMode.setMaxAccess(_D)
if mibBuilder.loadTexts:prtSpAlrRelayMode.setStatus(_A)
class _PrtSpStopBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('stopBits1',2),('stopBits1dot5',3),('stopBits2',4)))
_PrtSpStopBits_Type.__name__=_B
_PrtSpStopBits_Object=MibTableColumn
prtSpStopBits=_PrtSpStopBits_Object((1,3,6,1,4,1,164,3,3,3,4,1,1,22),_PrtSpStopBits_Type())
prtSpStopBits.setMaxAccess(_D)
if mibBuilder.loadTexts:prtSpStopBits.setStatus(_A)
_PrtDim_ObjectIdentity=ObjectIdentity
prtDim=_PrtDim_ObjectIdentity((1,3,6,1,4,1,164,3,3,3,5))
_PrtDimCnfgTable_Object=MibTable
prtDimCnfgTable=_PrtDimCnfgTable_Object((1,3,6,1,4,1,164,3,3,3,5,1))
if mibBuilder.loadTexts:prtDimCnfgTable.setStatus(_A)
_PrtDimCnfgEntry_Object=MibTableRow
prtDimCnfgEntry=_PrtDimCnfgEntry_Object((1,3,6,1,4,1,164,3,3,3,5,1,1))
prtDimCnfgEntry.setIndexNames((0,_F,_BL),(0,_F,_BM))
if mibBuilder.loadTexts:prtDimCnfgEntry.setStatus(_A)
class _PrtDimCnfgIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PrtDimCnfgIdx_Type.__name__=_B
_PrtDimCnfgIdx_Object=MibTableColumn
prtDimCnfgIdx=_PrtDimCnfgIdx_Object((1,3,6,1,4,1,164,3,3,3,5,1,1,1),_PrtDimCnfgIdx_Type())
prtDimCnfgIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtDimCnfgIdx.setStatus(_A)
_PrtDimIdx_Type=Integer32
_PrtDimIdx_Object=MibTableColumn
prtDimIdx=_PrtDimIdx_Object((1,3,6,1,4,1,164,3,3,3,5,1,1,2),_PrtDimIdx_Type())
prtDimIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtDimIdx.setStatus(_A)
class _PrtDimTxMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('regularTx',2),('broadcast',3)))
_PrtDimTxMode_Type.__name__=_B
_PrtDimTxMode_Object=MibTableColumn
prtDimTxMode=_PrtDimTxMode_Object((1,3,6,1,4,1,164,3,3,3,5,1,1,3),_PrtDimTxMode_Type())
prtDimTxMode.setMaxAccess(_D)
if mibBuilder.loadTexts:prtDimTxMode.setStatus(_A)
class _PrtDimPolarity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('normalClk',2),('inverted',3)))
_PrtDimPolarity_Type.__name__=_B
_PrtDimPolarity_Object=MibTableColumn
prtDimPolarity=_PrtDimPolarity_Object((1,3,6,1,4,1,164,3,3,3,5,1,1,4),_PrtDimPolarity_Type())
prtDimPolarity.setMaxAccess(_D)
if mibBuilder.loadTexts:prtDimPolarity.setStatus(_A)
class _PrtDimClkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5)));namedValues=NamedValues(*(('extDce',2),('dce',3),('smooth',4),('extSmooth',5)))
_PrtDimClkMode_Type.__name__=_B
_PrtDimClkMode_Object=MibTableColumn
prtDimClkMode=_PrtDimClkMode_Object((1,3,6,1,4,1,164,3,3,3,5,1,1,5),_PrtDimClkMode_Type())
prtDimClkMode.setMaxAccess(_D)
if mibBuilder.loadTexts:prtDimClkMode.setStatus(_A)
class _PrtDimMaxDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('t16msec',2),('t64msec',3)))
_PrtDimMaxDelay_Type.__name__=_B
_PrtDimMaxDelay_Object=MibTableColumn
prtDimMaxDelay=_PrtDimMaxDelay_Object((1,3,6,1,4,1,164,3,3,3,5,1,1,6),_PrtDimMaxDelay_Type())
prtDimMaxDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:prtDimMaxDelay.setStatus(_A)
class _PrtDimMng_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_y,2),('ts1',3),(_BD,4)))
_PrtDimMng_Type.__name__=_B
_PrtDimMng_Object=MibTableColumn
prtDimMng=_PrtDimMng_Object((1,3,6,1,4,1,164,3,3,3,5,1,1,7),_PrtDimMng_Type())
prtDimMng.setMaxAccess(_D)
if mibBuilder.loadTexts:prtDimMng.setStatus(_A)
class _PrtDimMngRoutProt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_c,2),(_A1,3)))
_PrtDimMngRoutProt_Type.__name__=_B
_PrtDimMngRoutProt_Object=MibTableColumn
prtDimMngRoutProt=_PrtDimMngRoutProt_Object((1,3,6,1,4,1,164,3,3,3,5,1,1,8),_PrtDimMngRoutProt_Type())
prtDimMngRoutProt.setMaxAccess(_D)
if mibBuilder.loadTexts:prtDimMngRoutProt.setStatus(_A)
_PrtDimDestTable_Object=MibTable
prtDimDestTable=_PrtDimDestTable_Object((1,3,6,1,4,1,164,3,3,3,5,2))
if mibBuilder.loadTexts:prtDimDestTable.setStatus(_A)
_PrtDimDestEntry_Object=MibTableRow
prtDimDestEntry=_PrtDimDestEntry_Object((1,3,6,1,4,1,164,3,3,3,5,2,1))
prtDimDestEntry.setIndexNames((0,_F,_BN),(0,_F,_BO),(0,_F,_BP))
if mibBuilder.loadTexts:prtDimDestEntry.setStatus(_A)
class _PrtDestCnfgIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PrtDestCnfgIdx_Type.__name__=_B
_PrtDestCnfgIdx_Object=MibTableColumn
prtDestCnfgIdx=_PrtDestCnfgIdx_Object((1,3,6,1,4,1,164,3,3,3,5,2,1,1),_PrtDestCnfgIdx_Type())
prtDestCnfgIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtDestCnfgIdx.setStatus(_A)
_PrtDestDimIdx_Type=Integer32
_PrtDestDimIdx_Object=MibTableColumn
prtDestDimIdx=_PrtDestDimIdx_Object((1,3,6,1,4,1,164,3,3,3,5,2,1,2),_PrtDestDimIdx_Type())
prtDestDimIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtDestDimIdx.setStatus(_A)
class _PrtDestIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_PrtDestIdx_Type.__name__=_B
_PrtDestIdx_Object=MibTableColumn
prtDestIdx=_PrtDestIdx_Object((1,3,6,1,4,1,164,3,3,3,5,2,1,3),_PrtDestIdx_Type())
prtDestIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtDestIdx.setStatus(_A)
_PrtDest_Type=Integer32
_PrtDest_Object=MibTableColumn
prtDest=_PrtDest_Object((1,3,6,1,4,1,164,3,3,3,5,2,1,4),_PrtDest_Type())
prtDest.setMaxAccess(_D)
if mibBuilder.loadTexts:prtDest.setStatus(_A)
class _PrtDestConnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_p,2),(_q,3)))
_PrtDestConnect_Type.__name__=_B
_PrtDestConnect_Object=MibTableColumn
prtDestConnect=_PrtDestConnect_Object((1,3,6,1,4,1,164,3,3,3,5,2,1,5),_PrtDestConnect_Type())
prtDestConnect.setMaxAccess(_C)
if mibBuilder.loadTexts:prtDestConnect.setStatus(_A)
_PrtI_ObjectIdentity=ObjectIdentity
prtI=_PrtI_ObjectIdentity((1,3,6,1,4,1,164,3,3,3,6))
_PrtICnfgTable_Object=MibTable
prtICnfgTable=_PrtICnfgTable_Object((1,3,6,1,4,1,164,3,3,3,6,1))
if mibBuilder.loadTexts:prtICnfgTable.setStatus(_A)
_PrtICnfgEntry_Object=MibTableRow
prtICnfgEntry=_PrtICnfgEntry_Object((1,3,6,1,4,1,164,3,3,3,6,1,1))
prtICnfgEntry.setIndexNames((0,_F,_BQ),(0,_F,'prtIIdx'))
if mibBuilder.loadTexts:prtICnfgEntry.setStatus(_A)
class _PrtICnfgIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PrtICnfgIdx_Type.__name__=_B
_PrtICnfgIdx_Object=MibTableColumn
prtICnfgIdx=_PrtICnfgIdx_Object((1,3,6,1,4,1,164,3,3,3,6,1,1,1),_PrtICnfgIdx_Type())
prtICnfgIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtICnfgIdx.setStatus(_A)
_PrtIIdx_Type=Integer32
_PrtIIdx_Object=MibTableColumn
prtIIdx=_PrtIIdx_Object((1,3,6,1,4,1,164,3,3,3,6,1,1,2),_PrtIIdx_Type())
prtIIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtIIdx.setStatus(_A)
class _PrtIRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('nc',2),('r2bit',3),('r4bit',4),('r8bit',5)))
_PrtIRate_Type.__name__=_B
_PrtIRate_Object=MibTableColumn
prtIRate=_PrtIRate_Object((1,3,6,1,4,1,164,3,3,3,6,1,1,3),_PrtIRate_Type())
prtIRate.setMaxAccess(_D)
if mibBuilder.loadTexts:prtIRate.setStatus(_A)
class _PrtIConnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_p,2),(_q,3)))
_PrtIConnect_Type.__name__=_B
_PrtIConnect_Object=MibTableColumn
prtIConnect=_PrtIConnect_Object((1,3,6,1,4,1,164,3,3,3,6,1,1,4),_PrtIConnect_Type())
prtIConnect.setMaxAccess(_D)
if mibBuilder.loadTexts:prtIConnect.setStatus(_A)
_PrtHdsl_ObjectIdentity=ObjectIdentity
prtHdsl=_PrtHdsl_ObjectIdentity((1,3,6,1,4,1,164,3,3,3,7))
_PrtHdslTable_Object=MibTable
prtHdslTable=_PrtHdslTable_Object((1,3,6,1,4,1,164,3,3,3,7,1))
if mibBuilder.loadTexts:prtHdslTable.setStatus(_A)
_PrtHdslEntry_Object=MibTableRow
prtHdslEntry=_PrtHdslEntry_Object((1,3,6,1,4,1,164,3,3,3,7,1,1))
prtHdslEntry.setIndexNames((0,_F,_BR))
if mibBuilder.loadTexts:prtHdslEntry.setStatus(_A)
_PrtHdslIdx_Type=Integer32
_PrtHdslIdx_Object=MibTableColumn
prtHdslIdx=_PrtHdslIdx_Object((1,3,6,1,4,1,164,3,3,3,7,1,1,1),_PrtHdslIdx_Type())
prtHdslIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtHdslIdx.setStatus(_A)
class _PrtHdslMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('central',2),('remote',3)))
_PrtHdslMode_Type.__name__=_B
_PrtHdslMode_Object=MibTableColumn
prtHdslMode=_PrtHdslMode_Object((1,3,6,1,4,1,164,3,3,3,7,1,1,2),_PrtHdslMode_Type())
prtHdslMode.setMaxAccess(_D)
if mibBuilder.loadTexts:prtHdslMode.setStatus(_A)
class _PrtHdslRptrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_c,2),('hrpt',3)))
_PrtHdslRptrType_Type.__name__=_B
_PrtHdslRptrType_Object=MibTableColumn
prtHdslRptrType=_PrtHdslRptrType_Object((1,3,6,1,4,1,164,3,3,3,7,1,1,3),_PrtHdslRptrType_Type())
prtHdslRptrType.setMaxAccess(_C)
if mibBuilder.loadTexts:prtHdslRptrType.setStatus(_A)
class _PrtHdslMaxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_E,1),('r192',2),('r256',3),('r320',4),('r384',5),('r448',6),('r512',7),('r576',8),('r640',9),('r768',10),('r896',11),('r1024',12),('r1152',13),('r1280',14),('r1536',15),('r1920',16),('r2048',17)))
_PrtHdslMaxRate_Type.__name__=_B
_PrtHdslMaxRate_Object=MibTableColumn
prtHdslMaxRate=_PrtHdslMaxRate_Object((1,3,6,1,4,1,164,3,3,3,7,1,1,4),_PrtHdslMaxRate_Type())
prtHdslMaxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:prtHdslMaxRate.setStatus(_A)
class _PrtHdslLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('msdsl2w',2),('hdsl2w',3),('hdsl4w',4),('gDsl',5)))
_PrtHdslLinkType_Type.__name__=_B
_PrtHdslLinkType_Object=MibTableColumn
prtHdslLinkType=_PrtHdslLinkType_Object((1,3,6,1,4,1,164,3,3,3,7,1,1,5),_PrtHdslLinkType_Type())
prtHdslLinkType.setMaxAccess(_C)
if mibBuilder.loadTexts:prtHdslLinkType.setStatus(_A)
class _PrtHdslCompSwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PrtHdslCompSwVer_Type.__name__=_J
_PrtHdslCompSwVer_Object=MibTableColumn
prtHdslCompSwVer=_PrtHdslCompSwVer_Object((1,3,6,1,4,1,164,3,3,3,7,1,1,6),_PrtHdslCompSwVer_Type())
prtHdslCompSwVer.setMaxAccess(_C)
if mibBuilder.loadTexts:prtHdslCompSwVer.setStatus(_A)
class _PrtHdslCompHwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PrtHdslCompHwVer_Type.__name__=_J
_PrtHdslCompHwVer_Object=MibTableColumn
prtHdslCompHwVer=_PrtHdslCompHwVer_Object((1,3,6,1,4,1,164,3,3,3,7,1,1,7),_PrtHdslCompHwVer_Type())
prtHdslCompHwVer.setMaxAccess(_C)
if mibBuilder.loadTexts:prtHdslCompHwVer.setStatus(_A)
_PrtT3E3_ObjectIdentity=ObjectIdentity
prtT3E3=_PrtT3E3_ObjectIdentity((1,3,6,1,4,1,164,3,3,3,8))
_PrtT3E3CnfgTable_Object=MibTable
prtT3E3CnfgTable=_PrtT3E3CnfgTable_Object((1,3,6,1,4,1,164,3,3,3,8,1))
if mibBuilder.loadTexts:prtT3E3CnfgTable.setStatus(_A)
_PrtT3E3CnfgEntry_Object=MibTableRow
prtT3E3CnfgEntry=_PrtT3E3CnfgEntry_Object((1,3,6,1,4,1,164,3,3,3,8,1,1))
prtT3E3CnfgEntry.setIndexNames((0,_F,_BS),(0,_F,_BT))
if mibBuilder.loadTexts:prtT3E3CnfgEntry.setStatus(_A)
class _PrtT3E3CnfgIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PrtT3E3CnfgIdx_Type.__name__=_B
_PrtT3E3CnfgIdx_Object=MibTableColumn
prtT3E3CnfgIdx=_PrtT3E3CnfgIdx_Object((1,3,6,1,4,1,164,3,3,3,8,1,1,1),_PrtT3E3CnfgIdx_Type())
prtT3E3CnfgIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtT3E3CnfgIdx.setStatus(_A)
_PrtT3E3PrtIdx_Type=Integer32
_PrtT3E3PrtIdx_Object=MibTableColumn
prtT3E3PrtIdx=_PrtT3E3PrtIdx_Object((1,3,6,1,4,1,164,3,3,3,8,1,1,2),_PrtT3E3PrtIdx_Type())
prtT3E3PrtIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:prtT3E3PrtIdx.setStatus(_A)
class _PrtT3E3Slt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,255)));namedValues=NamedValues(*((_v,3),(_w,4),(_T,5),(_U,6),(_V,7),(_W,8),(_X,9),(_Y,10),(_Z,11),(_a,12),(_b,13),(_e,14),(_f,15),(_g,16),(_h,17),(_i,18),(_j,19),(_t,255)))
_PrtT3E3Slt_Type.__name__=_B
_PrtT3E3Slt_Object=MibTableColumn
prtT3E3Slt=_PrtT3E3Slt_Object((1,3,6,1,4,1,164,3,3,3,8,1,1,3),_PrtT3E3Slt_Type())
prtT3E3Slt.setMaxAccess(_C)
if mibBuilder.loadTexts:prtT3E3Slt.setStatus(_A)
class _PrtT3E3LineLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('len0p450ft',2),('len451p900ft',3)))
_PrtT3E3LineLength_Type.__name__=_B
_PrtT3E3LineLength_Object=MibTableColumn
prtT3E3LineLength=_PrtT3E3LineLength_Object((1,3,6,1,4,1,164,3,3,3,8,1,1,4),_PrtT3E3LineLength_Type())
prtT3E3LineLength.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT3E3LineLength.setStatus(_A)
class _PrtT3E3InbandMng_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_E,1),(_H,2),('cBit',3),('cBitTxRxMng',4),('cBitTx',5),('cBitTxMng',6),('m13',7),('cdpv',8),('nationalBit',9)))
_PrtT3E3InbandMng_Type.__name__=_B
_PrtT3E3InbandMng_Object=MibTableColumn
prtT3E3InbandMng=_PrtT3E3InbandMng_Object((1,3,6,1,4,1,164,3,3,3,8,1,1,5),_PrtT3E3InbandMng_Type())
prtT3E3InbandMng.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT3E3InbandMng.setStatus(_A)
class _PrtT3E3AisFrame_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('unframed',2),('framed',3)))
_PrtT3E3AisFrame_Type.__name__=_B
_PrtT3E3AisFrame_Object=MibTableColumn
prtT3E3AisFrame=_PrtT3E3AisFrame_Object((1,3,6,1,4,1,164,3,3,3,8,1,1,6),_PrtT3E3AisFrame_Type())
prtT3E3AisFrame.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT3E3AisFrame.setStatus(_A)
class _PrtT3E3TxClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('external',1),(_z,2),(_E,255)))
_PrtT3E3TxClockSource_Type.__name__=_B
_PrtT3E3TxClockSource_Object=MibTableColumn
prtT3E3TxClockSource=_PrtT3E3TxClockSource_Object((1,3,6,1,4,1,164,3,3,3,8,1,1,7),_PrtT3E3TxClockSource_Type())
prtT3E3TxClockSource.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT3E3TxClockSource.setStatus(_A)
class _PrtT3E3RoutProt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_c,2),(_A1,3),(_AL,4)))
_PrtT3E3RoutProt_Type.__name__=_B
_PrtT3E3RoutProt_Object=MibTableColumn
prtT3E3RoutProt=_PrtT3E3RoutProt_Object((1,3,6,1,4,1,164,3,3,3,8,1,1,8),_PrtT3E3RoutProt_Type())
prtT3E3RoutProt.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT3E3RoutProt.setStatus(_A)
class _PrtT3E3AisTransmit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_AM,2),(_AN,3)))
_PrtT3E3AisTransmit_Type.__name__=_B
_PrtT3E3AisTransmit_Object=MibTableColumn
prtT3E3AisTransmit=_PrtT3E3AisTransmit_Object((1,3,6,1,4,1,164,3,3,3,8,1,1,9),_PrtT3E3AisTransmit_Type())
prtT3E3AisTransmit.setMaxAccess(_D)
if mibBuilder.loadTexts:prtT3E3AisTransmit.setStatus(_A)
_GenDacsMux_ObjectIdentity=ObjectIdentity
genDacsMux=_GenDacsMux_ObjectIdentity((1,3,6,1,4,1,164,3,3,4))
_CmprTable_Object=MibTable
cmprTable=_CmprTable_Object((1,3,6,1,4,1,164,3,3,4,1))
if mibBuilder.loadTexts:cmprTable.setStatus(_A)
_CmprEntry_Object=MibTableRow
cmprEntry=_CmprEntry_Object((1,3,6,1,4,1,164,3,3,4,1,1))
cmprEntry.setIndexNames((0,_F,_BU),(0,_F,_BV),(0,_F,_BW),(0,_F,_BX),(0,_F,_BY))
if mibBuilder.loadTexts:cmprEntry.setStatus(_A)
_CmprTypeIdx_Type=Integer32
_CmprTypeIdx_Object=MibTableColumn
cmprTypeIdx=_CmprTypeIdx_Object((1,3,6,1,4,1,164,3,3,4,1,1,1),_CmprTypeIdx_Type())
cmprTypeIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:cmprTypeIdx.setStatus(_A)
_CmprCnfgIdx_Type=Integer32
_CmprCnfgIdx_Object=MibTableColumn
cmprCnfgIdx=_CmprCnfgIdx_Object((1,3,6,1,4,1,164,3,3,4,1,1,2),_CmprCnfgIdx_Type())
cmprCnfgIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:cmprCnfgIdx.setStatus(_A)
_CmprVersion_Type=Integer32
_CmprVersion_Object=MibTableColumn
cmprVersion=_CmprVersion_Object((1,3,6,1,4,1,164,3,3,4,1,1,3),_CmprVersion_Type())
cmprVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cmprVersion.setStatus(_A)
class _CmprSltIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,255)));namedValues=NamedValues(*(('psA',1),('psB',2),(_v,3),(_w,4),(_T,5),(_U,6),(_V,7),(_W,8),(_X,9),(_Y,10),(_Z,11),(_a,12),(_b,13),(_e,14),(_f,15),(_g,16),(_h,17),(_i,18),(_j,19),(_E,255)))
_CmprSltIdx_Type.__name__=_B
_CmprSltIdx_Object=MibTableColumn
cmprSltIdx=_CmprSltIdx_Object((1,3,6,1,4,1,164,3,3,4,1,1,4),_CmprSltIdx_Type())
cmprSltIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:cmprSltIdx.setStatus(_A)
_CmprPrtIdx_Type=Integer32
_CmprPrtIdx_Object=MibTableColumn
cmprPrtIdx=_CmprPrtIdx_Object((1,3,6,1,4,1,164,3,3,4,1,1,5),_CmprPrtIdx_Type())
cmprPrtIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:cmprPrtIdx.setStatus(_A)
_CmprObj_Type=OctetString
_CmprObj_Object=MibTableColumn
cmprObj=_CmprObj_Object((1,3,6,1,4,1,164,3,3,4,1,1,6),_CmprObj_Type())
cmprObj.setMaxAccess(_D)
if mibBuilder.loadTexts:cmprObj.setStatus(_A)
_MapLinkTable_Object=MibTable
mapLinkTable=_MapLinkTable_Object((1,3,6,1,4,1,164,3,3,4,2))
if mibBuilder.loadTexts:mapLinkTable.setStatus(_A)
_MapLinkEntry_Object=MibTableRow
mapLinkEntry=_MapLinkEntry_Object((1,3,6,1,4,1,164,3,3,4,2,1))
mapLinkEntry.setIndexNames((0,_F,_BZ))
if mibBuilder.loadTexts:mapLinkEntry.setStatus(_A)
_MapLinkIdx_Type=Integer32
_MapLinkIdx_Object=MibTableColumn
mapLinkIdx=_MapLinkIdx_Object((1,3,6,1,4,1,164,3,3,4,2,1,1),_MapLinkIdx_Type())
mapLinkIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:mapLinkIdx.setStatus(_A)
class _MapLinkSlotIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,255)));namedValues=NamedValues(*((_T,5),(_U,6),(_V,7),(_W,8),(_X,9),(_Y,10),(_Z,11),(_a,12),(_b,13),(_e,14),(_f,15),(_g,16),(_h,17),(_i,18),(_j,19),(_t,255)))
_MapLinkSlotIdx_Type.__name__=_B
_MapLinkSlotIdx_Object=MibTableColumn
mapLinkSlotIdx=_MapLinkSlotIdx_Object((1,3,6,1,4,1,164,3,3,4,2,1,2),_MapLinkSlotIdx_Type())
mapLinkSlotIdx.setMaxAccess(_D)
if mibBuilder.loadTexts:mapLinkSlotIdx.setStatus(_A)
_MapLinkPortIdx_Type=Integer32
_MapLinkPortIdx_Object=MibTableColumn
mapLinkPortIdx=_MapLinkPortIdx_Object((1,3,6,1,4,1,164,3,3,4,2,1,3),_MapLinkPortIdx_Type())
mapLinkPortIdx.setMaxAccess(_D)
if mibBuilder.loadTexts:mapLinkPortIdx.setStatus(_A)
class _MapLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_u,1),(_A2,2),('up',3)))
_MapLinkState_Type.__name__=_B
_MapLinkState_Object=MibTableColumn
mapLinkState=_MapLinkState_Object((1,3,6,1,4,1,164,3,3,4,2,1,4),_MapLinkState_Type())
mapLinkState.setMaxAccess(_C)
if mibBuilder.loadTexts:mapLinkState.setStatus(_A)
_AlrGenTable_Object=MibTable
alrGenTable=_AlrGenTable_Object((1,3,6,1,4,1,164,3,3,4,3))
if mibBuilder.loadTexts:alrGenTable.setStatus(_A)
_AlrGenEntry_Object=MibTableRow
alrGenEntry=_AlrGenEntry_Object((1,3,6,1,4,1,164,3,3,4,3,1))
alrGenEntry.setIndexNames((0,_F,_Ba))
if mibBuilder.loadTexts:alrGenEntry.setStatus(_A)
_AlrGenCode_Type=Integer32
_AlrGenCode_Object=MibTableColumn
alrGenCode=_AlrGenCode_Object((1,3,6,1,4,1,164,3,3,4,3,1,1),_AlrGenCode_Type())
alrGenCode.setMaxAccess(_C)
if mibBuilder.loadTexts:alrGenCode.setStatus(_A)
class _AlrGenDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AlrGenDescription_Type.__name__=_J
_AlrGenDescription_Object=MibTableColumn
alrGenDescription=_AlrGenDescription_Object((1,3,6,1,4,1,164,3,3,4,3,1,2),_AlrGenDescription_Type())
alrGenDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:alrGenDescription.setStatus(_A)
class _AlrGenLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('system',2),('card',3),('port',4)))
_AlrGenLevel_Type.__name__=_B
_AlrGenLevel_Object=MibTableColumn
alrGenLevel=_AlrGenLevel_Object((1,3,6,1,4,1,164,3,3,4,3,1,3),_AlrGenLevel_Type())
alrGenLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:alrGenLevel.setStatus(_A)
class _AlrGenSlotType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('ps',2),('cl',3),('io',4),('clAndIo',5)))
_AlrGenSlotType_Type.__name__=_B
_AlrGenSlotType_Object=MibTableColumn
alrGenSlotType=_AlrGenSlotType_Object((1,3,6,1,4,1,164,3,3,4,3,1,4),_AlrGenSlotType_Type())
alrGenSlotType.setMaxAccess(_C)
if mibBuilder.loadTexts:alrGenSlotType.setStatus(_A)
class _AlrGenSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),(_n,3),(_m,4),(_k,5),(_d,6),(_o,7)))
_AlrGenSeverity_Type.__name__=_B
_AlrGenSeverity_Object=MibTableColumn
alrGenSeverity=_AlrGenSeverity_Object((1,3,6,1,4,1,164,3,3,4,3,1,5),_AlrGenSeverity_Type())
alrGenSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:alrGenSeverity.setStatus(_A)
class _AlrGenDebounce_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlrGenDebounce_Type.__name__=_B
_AlrGenDebounce_Object=MibTableColumn
alrGenDebounce=_AlrGenDebounce_Object((1,3,6,1,4,1,164,3,3,4,3,1,6),_AlrGenDebounce_Type())
alrGenDebounce.setMaxAccess(_D)
if mibBuilder.loadTexts:alrGenDebounce.setStatus(_A)
class _AlrGenDefSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),(_n,3),(_m,4),(_k,5),(_d,6),(_o,7)))
_AlrGenDefSeverity_Type.__name__=_B
_AlrGenDefSeverity_Object=MibTableColumn
alrGenDefSeverity=_AlrGenDefSeverity_Object((1,3,6,1,4,1,164,3,3,4,3,1,7),_AlrGenDefSeverity_Type())
alrGenDefSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:alrGenDefSeverity.setStatus(_A)
sanityCheckTrap=NotificationType((1,3,6,1,4,1,164,3,3,0,1))
sanityCheckTrap.setObjects(*((_F,_Bb),(_F,_Bc)))
if mibBuilder.loadTexts:sanityCheckTrap.setStatus(_A)
dacsMuxAlarmsTrap=NotificationType((1,3,6,1,4,1,164,3,3,0,2))
if mibBuilder.loadTexts:dacsMuxAlarmsTrap.setStatus(_A)
mdlConnectTrap=NotificationType((1,3,6,1,4,1,164,3,3,0,3))
mdlConnectTrap.setObjects(*((_F,_Bd),(_F,_Be)))
if mibBuilder.loadTexts:mdlConnectTrap.setStatus(_A)
sysAlrStatusTrap=NotificationType((1,3,6,1,4,1,164,3,3,0,4))
sysAlrStatusTrap.setObjects(*((_F,_Bf),(_F,_Bg)))
if mibBuilder.loadTexts:sysAlrStatusTrap.setStatus(_A)
sysStatusChangedTrap=NotificationType((1,3,6,1,4,1,164,3,3,0,5))
sysStatusChangedTrap.setObjects((_G,'agnLed'))
if mibBuilder.loadTexts:sysStatusChangedTrap.setStatus(_A)
cnfgUpdateTrap=NotificationType((1,3,6,1,4,1,164,3,3,0,6))
if mibBuilder.loadTexts:cnfgUpdateTrap.setStatus(_A)
sysRedundancyStatusTrap=NotificationType((1,3,6,1,4,1,164,3,3,0,7))
sysRedundancyStatusTrap.setObjects((_F,_Bh))
if mibBuilder.loadTexts:sysRedundancyStatusTrap.setStatus(_A)
sysRedundancyActiveCardTrap=NotificationType((1,3,6,1,4,1,164,3,3,0,8))
sysRedundancyActiveCardTrap.setObjects((_F,_Bi))
if mibBuilder.loadTexts:sysRedundancyActiveCardTrap.setStatus(_A)
sysRedundancyActivePortTrap=NotificationType((1,3,6,1,4,1,164,3,3,0,9))
sysRedundancyActivePortTrap.setObjects((_F,_Bj))
if mibBuilder.loadTexts:sysRedundancyActivePortTrap.setStatus(_A)
cardHwFailure=NotificationType((1,3,6,1,4,1,164,3,3,2,1,0,1))
cardHwFailure.setObjects(*((_G,_R),(_G,_N),(_G,_P),(_G,_Q),(_G,_O),(_G,_S),(_L,_M),(_F,_r),(_F,_Bk)))
if mibBuilder.loadTexts:cardHwFailure.setStatus(_A)
cardMismatch=NotificationType((1,3,6,1,4,1,164,3,3,2,1,0,2))
cardMismatch.setObjects(*((_G,_R),(_G,_N),(_G,_P),(_G,_Q),(_G,_O),(_G,_S),(_L,_M),(_F,_r),(_F,_A3)))
if mibBuilder.loadTexts:cardMismatch.setStatus(_A)
cardProvisionFailure=NotificationType((1,3,6,1,4,1,164,3,3,2,1,0,3))
cardProvisionFailure.setObjects(*((_G,_R),(_G,_N),(_G,_P),(_G,_Q),(_G,_O),(_G,_S),(_L,_M),(_F,_r)))
if mibBuilder.loadTexts:cardProvisionFailure.setStatus(_A)
cardUnsupportedSw=NotificationType((1,3,6,1,4,1,164,3,3,2,1,0,4))
cardUnsupportedSw.setObjects(*((_G,_R),(_G,_N),(_G,_P),(_G,_Q),(_G,_O),(_G,_S),(_L,_M),(_F,_r),(_L,_AX)))
if mibBuilder.loadTexts:cardUnsupportedSw.setStatus(_A)
cardUnsupportedHw=NotificationType((1,3,6,1,4,1,164,3,3,2,1,0,5))
cardUnsupportedHw.setObjects(*((_G,_R),(_G,_N),(_G,_P),(_G,_Q),(_G,_O),(_G,_S),(_L,_M),(_F,_r),(_L,_AW)))
if mibBuilder.loadTexts:cardUnsupportedHw.setStatus(_A)
cardImproperRemoval=NotificationType((1,3,6,1,4,1,164,3,3,2,1,0,6))
cardImproperRemoval.setObjects(*((_G,_R),(_G,_N),(_G,_P),(_G,_Q),(_G,_O),(_G,_S),(_L,_M),(_F,_A3)))
if mibBuilder.loadTexts:cardImproperRemoval.setStatus(_A)
cardNoResponse=NotificationType((1,3,6,1,4,1,164,3,3,2,1,0,8))
cardNoResponse.setObjects(*((_G,_R),(_G,_N),(_G,_P),(_G,_Q),(_G,_O),(_G,_S),(_L,_M),(_F,_A3)))
if mibBuilder.loadTexts:cardNoResponse.setStatus(_A)
cardInitFailure=NotificationType((1,3,6,1,4,1,164,3,3,2,1,0,9))
cardInitFailure.setObjects(*((_G,_R),(_G,_N),(_G,_P),(_G,_Q),(_G,_O),(_G,_S),(_L,_M),(_F,_r)))
if mibBuilder.loadTexts:cardInitFailure.setStatus(_A)
cardReset=NotificationType((1,3,6,1,4,1,164,3,3,2,1,0,10))
cardReset.setObjects(*((_G,_R),(_G,_N),(_G,_P),(_G,_Q),(_G,_O),(_G,_S),(_L,_M),(_F,_r)))
if mibBuilder.loadTexts:cardReset.setStatus(_A)
cardPluggedIn=NotificationType((1,3,6,1,4,1,164,3,3,2,1,0,11))
cardPluggedIn.setObjects(*((_G,_R),(_G,_N),(_G,_P),(_G,_Q),(_G,_O),(_G,_S),(_L,_M),(_F,_r)))
if mibBuilder.loadTexts:cardPluggedIn.setStatus(_A)
cardPluggedOut=NotificationType((1,3,6,1,4,1,164,3,3,2,1,0,12))
cardPluggedOut.setObjects(*((_G,_R),(_G,_N),(_G,_P),(_G,_Q),(_G,_O),(_G,_S),(_L,_M),(_F,_A3)))
if mibBuilder.loadTexts:cardPluggedOut.setStatus(_A)
cardConfigurationMismatch=NotificationType((1,3,6,1,4,1,164,3,3,2,1,0,14))
cardConfigurationMismatch.setObjects(*((_G,_R),(_G,_N),(_G,_P),(_G,_Q),(_G,_O),(_G,_S),(_L,_M),(_F,_r),(_F,_Bl)))
if mibBuilder.loadTexts:cardConfigurationMismatch.setStatus(_A)
powerDeliveryFailure=NotificationType((1,3,6,1,4,1,164,6,1,0,73))
powerDeliveryFailure.setObjects(*((_G,_R),(_G,_N),(_G,_P),(_G,_Q),(_G,_O),(_G,_S),(_L,_M),(_F,_Bm)))
if mibBuilder.loadTexts:powerDeliveryFailure.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'dacsMux':dacsMux,'dacsMuxEvents':dacsMuxEvents,'sanityCheckTrap':sanityCheckTrap,'dacsMuxAlarmsTrap':dacsMuxAlarmsTrap,'mdlConnectTrap':mdlConnectTrap,'sysAlrStatusTrap':sysAlrStatusTrap,'sysStatusChangedTrap':sysStatusChangedTrap,'cnfgUpdateTrap':cnfgUpdateTrap,'sysRedundancyStatusTrap':sysRedundancyStatusTrap,'sysRedundancyActiveCardTrap':sysRedundancyActiveCardTrap,'sysRedundancyActivePortTrap':sysRedundancyActivePortTrap,'systemDacsMux':systemDacsMux,'sysSa':sysSa,'sysSaSwchStatus':sysSaSwchStatus,'sysSaSwRevision':sysSaSwRevision,'sysSaHwVersion':sysSaHwVersion,'sysSaPorts':sysSaPorts,'sysSaReadSwch':sysSaReadSwch,'sysSaBuActivePort':sysSaBuActivePort,'sysHub':sysHub,'sysChas':sysChas,'chassTotalNoOfSlt':chassTotalNoOfSlt,'chassTotalNoOfIoSlt':chassTotalNoOfIoSlt,'chassTotalNoOfPsSlt':chassTotalNoOfPsSlt,'chassTotalNoOfClSlt':chassTotalNoOfClSlt,'chassTotalNoOfMlSlt':chassTotalNoOfMlSlt,'sysDcl':sysDcl,'sysDclTable':sysDclTable,'sysDclEntry':sysDclEntry,_Aa:sysDclCnfgIdx,'sysDclRedundancy':sysDclRedundancy,'sysDclActiveCl':sysDclActiveCl,'sysDclFlipDelay':sysDclFlipDelay,'sysDclFlipUponStnClk':sysDclFlipUponStnClk,'sysDclChFailThreshold':sysDclChFailThreshold,'sysDclChPriority':sysDclChPriority,'sysDclConfigDownloadSrc':sysDclConfigDownloadSrc,'sysDclSwDownloadSrc':sysDclSwDownloadSrc,_Bh:sysDclRedundancyStatus,_Bi:sysDclOnline,'sysDclCopyDbTable':sysDclCopyDbTable,'sysDclCopyDbEntry':sysDclCopyDbEntry,_Ab:sysDclCopyDbIdx,'sysDclCopyDbCmd':sysDclCopyDbCmd,'sysDclFlipCmd':sysDclFlipCmd,'sysStatus':sysStatus,'sysSDateFormat':sysSDateFormat,'sysSDateCmd':sysSDateCmd,'sysSTimeCmd':sysSTimeCmd,'sysSActiveCnfg':sysSActiveCnfg,'sysSEditCnfg':sysSEditCnfg,'sysSEditBy':sysSEditBy,'sysSClkSrc':sysSClkSrc,_Bg:sysSAlrStatus,_Bf:sysSAlrStatusAll,'sysSTestStatus':sysSTestStatus,_Bb:sysSSanityCheckStatus,'sysSNoOfSanityCheckErr':sysSNoOfSanityCheckErr,'sysSErrListTable':sysSErrListTable,'sysSErrListEntry':sysSErrListEntry,_Ac:sysSErrType,_Ad:sysSErrIdx,'sysSErrDescription':sysSErrDescription,'sysSMaxNoOfCnfg':sysSMaxNoOfCnfg,'sysSSelfTestResult':sysSSelfTestResult,'sysSRelayState':sysSRelayState,'sysSInvertedAlr':sysSInvertedAlr,'sysSRdnFlipTable':sysSRdnFlipTable,'sysSRdnFlipEntry':sysSRdnFlipEntry,_Ae:sysSRdnFlipIdx,'sysSRdnFlipSlot':sysSRdnFlipSlot,'sysSRdnFlipPort':sysSRdnFlipPort,'sysSRdnFlipCause':sysSRdnFlipCause,'sysSRdnFlipDate':sysSRdnFlipDate,'sysSRdnFlipTime':sysSRdnFlipTime,'sysSRdnFlipTableClearCmd':sysSRdnFlipTableClearCmd,'sysSRdnFlipCmd':sysSRdnFlipCmd,'sysSBusTable':sysSBusTable,'sysSBusEntry':sysSBusEntry,_Af:sysSBusPortIdx,'sysSBusStatus':sysSBusStatus,'sysSBusCapturePort':sysSBusCapturePort,'sysSBusUtilization':sysSBusUtilization,'sysSRdnCmdTable':sysSRdnCmdTable,'sysSRdnCmdEntry':sysSRdnCmdEntry,'sysSRdnEnforcedChannel':sysSRdnEnforcedChannel,'sysSRdnLockFlip':sysSRdnLockFlip,'sysSRdnManualFlip':sysSRdnManualFlip,'sysSAlrAttrIndication':sysSAlrAttrIndication,'sysCurrentAlr':sysCurrentAlr,'sysSAlrTable':sysSAlrTable,'sysSAlrEntry':sysSAlrEntry,_Ag:sysSAlrIdx,'sysSAlrCode':sysSAlrCode,'sysSAlrState':sysSAlrState,'sysSAlarmMask':sysSAlarmMask,'sysSAlarmInvert':sysSAlarmInvert,'sysSAlarmOnOff':sysSAlarmOnOff,'sysSAlarmCounter':sysSAlarmCounter,'sysSAlrClearCmd':sysSAlrClearCmd,'sysSAlrClearAllCmd':sysSAlrClearAllCmd,'sysSAlrMaskAll':sysSAlrMaskAll,'sysSAlrMask':sysSAlrMask,'sysSAlrDataUpdateCmd':sysSAlrDataUpdateCmd,'sysBufferAlr':sysBufferAlr,'sysBufferAlrTable':sysBufferAlrTable,'sysBufferAlrEntry':sysBufferAlrEntry,_Ah:sysBufferAlrIdx,'sysBufferAlrCode':sysBufferAlrCode,'sysBufferAlrState':sysBufferAlrState,'sysBufferAlrSlot':sysBufferAlrSlot,'sysBufferAlrPort':sysBufferAlrPort,'sysBufferAlrDate':sysBufferAlrDate,'sysBufferAlrTime':sysBufferAlrTime,'sysBufferAlrUpTime':sysBufferAlrUpTime,'sysBufferAlrInfo':sysBufferAlrInfo,'sysBufferAlrClearCmd':sysBufferAlrClearCmd,'sysConfig':sysConfig,'sysCClkSrcTable':sysCClkSrcTable,'sysCClkSrcEntry':sysCClkSrcEntry,_Ai:sysCClkCnfgIdx,_Aj:sysCClkSrcIdx,'sysCClkSrcMode':sysCClkSrcMode,'sysCClkSrcPrt':sysCClkSrcPrt,'sysCClkStationFreq':sysCClkStationFreq,'sysCClkRevertiveTimeout':sysCClkRevertiveTimeout,'sysCClkStationIf':sysCClkStationIf,'sysCClkStationCableMode':sysCClkStationCableMode,'sysCClkStationOutState':sysCClkStationOutState,'sysCClkSsmBased':sysCClkSsmBased,'sysCClkSSubsystemSlot':sysCClkSSubsystemSlot,'sysCClkRecoveredID':sysCClkRecoveredID,'sysCnfgTable':sysCnfgTable,'sysCnfgEntry':sysCnfgEntry,_Ak:sysCnfgIdx,'sysCMatrixMode':sysCMatrixMode,'sysCIsdnFormat':sysCIsdnFormat,'sysCRoutingOnEth':sysCRoutingOnEth,'sysCAutoConfigEnable':sysCAutoConfigEnable,'sysCIntTsAllocMode':sysCIntTsAllocMode,'sysCBuPrimaryPort':sysCBuPrimaryPort,'sysCEnableLanOverTdm':sysCEnableLanOverTdm,'sysCSs7FisuSuppression':sysCSs7FisuSuppression,'sysCBuRecMode':sysCBuRecMode,'sysCRdnTable':sysCRdnTable,'sysCRdnEntry':sysCRdnEntry,_Al:sysCRdnCnfgIdx,_AR:sysCRdnPrimeSlot,_AS:sysCRdnPrimePort,'sysCRdnSecSlot':sysCRdnSecSlot,'sysCRdnSecPort':sysCRdnSecPort,'sysCRdnMode':sysCRdnMode,'sysCRdnRecMode':sysCRdnRecMode,'sysCRdnRecTime':sysCRdnRecTime,'sysCRdnHwSwFlip':sysCRdnHwSwFlip,'sysCRdnRowStatus':sysCRdnRowStatus,_Bj:sysCRdnOnline,'sysCRdnSwitchingMode':sysCRdnSwitchingMode,'sysCRdnFlipUponEvent':sysCRdnFlipUponEvent,'sysCRdnLosOrLofTime':sysCRdnLosOrLofTime,'sysCRdnEventsTimeWindow':sysCRdnEventsTimeWindow,'sysCRdnSequenceNumberThreshold':sysCRdnSequenceNumberThreshold,'sysCRdnBufferErrorsThreshold':sysCRdnBufferErrorsThreshold,'sysCRdnBuffUnderrunTime':sysCRdnBuffUnderrunTime,'sysCRdnPrimePriority':sysCRdnPrimePriority,'sysCRdnSecPriority':sysCRdnSecPriority,'sysCRdnWTR':sysCRdnWTR,'sysCRdnName':sysCRdnName,'sysCRdnTxDownDurationUponFlip':sysCRdnTxDownDurationUponFlip,'sysDbase':sysDbase,'sysDbaseSanityCheckCmd':sysDbaseSanityCheckCmd,_Bc:sysDbaseDownloadCnfgIdxCmd,'sysDbaseUploadCnfgIdxCmd':sysDbaseUploadCnfgIdxCmd,'sysDbaseFlipTable':sysDbaseFlipTable,'sysDbaseFlipEntry':sysDbaseFlipEntry,_An:sysDbaseFlipIdx,'sysDbaseFlipTime':sysDbaseFlipTime,'sysDbaseFlipActivation':sysDbaseFlipActivation,'mdlDacsMux':mdlDacsMux,'mdlGen':mdlGen,'cardEvents':cardEvents,'cardHwFailure':cardHwFailure,_As:cardMismatch,'cardProvisionFailure':cardProvisionFailure,'cardUnsupportedSw':cardUnsupportedSw,'cardUnsupportedHw':cardUnsupportedHw,'cardImproperRemoval':cardImproperRemoval,'cardNoResponse':cardNoResponse,'cardInitFailure':cardInitFailure,'cardReset':cardReset,'cardPluggedIn':cardPluggedIn,'cardPluggedOut':cardPluggedOut,'cardConfigurationMismatch':cardConfigurationMismatch,'mdlSTable':mdlSTable,'mdlSEntry':mdlSEntry,_Ao:mdlSSltIdx,_Bd:mdlSCardType,'mdlSHwVer':mdlSHwVer,'mdlSSwVer':mdlSSwVer,'mdlSAlarmStatus':mdlSAlarmStatus,'mdlSAlarmStatusAll':mdlSAlarmStatusAll,'mdlSTestStatus':mdlSTestStatus,'mdlSHwStatus':mdlSHwStatus,_Be:mdlSActivity,'mdlSAlrClearCmd':mdlSAlrClearCmd,'mdlSAlrClearAllCmd':mdlSAlrClearAllCmd,'mdlSAlrMaskAll':mdlSAlrMaskAll,'mdlSCmd':mdlSCmd,'mdlSReset':mdlSReset,'mdlSRebuildFrame':mdlSRebuildFrame,'mdlSBackupSwVer':mdlSBackupSwVer,'mdlSSecondaryBackupSwVer':mdlSSecondaryBackupSwVer,'mdlSPiggybackVer':mdlSPiggybackVer,'mdlCTable':mdlCTable,'mdlCEntry':mdlCEntry,_Ap:mdlCConfigIdx,_Aq:mdlCSlotIdx,_A3:mdlCProgCardType,'mdlCNoOfExtPrt':mdlCNoOfExtPrt,'mdlCNoOfIntPrt':mdlCNoOfIntPrt,'mdlCParam':mdlCParam,'mdlCAdminStatus':mdlCAdminStatus,_r:mdlCActualCardType,'mdlCOperStatus':mdlCOperStatus,'mdlCDetailedStatus':mdlCDetailedStatus,'mdlCEntPhysicalIndex':mdlCEntPhysicalIndex,'mdlCReset':mdlCReset,_Bl:mdlCConfigMismatchReason,'mdlCIpAddressType':mdlCIpAddressType,'mdlCIpAddress':mdlCIpAddress,_Bk:mdlCHardwareFailureReason,'mdlCFanControl':mdlCFanControl,'mdlCFanOperStatus':mdlCFanOperStatus,'mdlAlr':mdlAlr,'mdlAlrTable':mdlAlrTable,'mdlAlrEntry':mdlAlrEntry,_Au:mdlAlrIdx,_At:mdlAlrSltIdx,'mdlAlrCode':mdlAlrCode,'mdlAlrState':mdlAlrState,'mdlAlarmMask':mdlAlarmMask,'mdlAlarmInvert':mdlAlarmInvert,'mdlAlarmOnOff':mdlAlarmOnOff,'mdlAlarmCounter':mdlAlarmCounter,'mdlAlrMaskTable':mdlAlrMaskTable,'mdlAlrMaskEntry':mdlAlrMaskEntry,_Av:mdlAlrMaskSltIdx,'mdlAlrMask':mdlAlrMask,'mdlCl':mdlCl,'mdlClTable':mdlClTable,'mdlClEntry':mdlClEntry,'mdlClIdx':mdlClIdx,'mdlClSwchStatus':mdlClSwchStatus,'mdlClLastFlipDate':mdlClLastFlipDate,'mdlClLastFlipTime':mdlClLastFlipTime,'mdlClLastFlipCause':mdlClLastFlipCause,'mdlPs':mdlPs,'mdlPsTable':mdlPsTable,'mdlPsEntry':mdlPsEntry,'mdlPsIdx':mdlPsIdx,'mdlPsStatus':mdlPsStatus,_Bm:mdlPsTestResult,'mdlPsVoltageCurrent':mdlPsVoltageCurrent,'mdlPsVoltageMin':mdlPsVoltageMin,'mdlPsVoltageMax':mdlPsVoltageMax,'prtDacsMux':prtDacsMux,'prtGen':prtGen,'prtGenParamTable':prtGenParamTable,'prtGenEntry':prtGenEntry,_Aw:prtGenPrtIdx,'prtGenSlt':prtGenSlt,'prtGenExtInt':prtGenExtInt,'prtGenIfIndex':prtGenIfIndex,'prtGenActiveStatus':prtGenActiveStatus,'prtGenAlrStatus':prtGenAlrStatus,'prtGenTestStatus':prtGenTestStatus,'prtGenTestMask':prtGenTestMask,'prtGenTestCmd':prtGenTestCmd,'prtGenTestRunning':prtGenTestRunning,'prtGenType':prtGenType,'prtGenInterfaceType':prtGenInterfaceType,'prtGenAlrClearCmd':prtGenAlrClearCmd,'prtGenAlrMaskAll':prtGenAlrMaskAll,'prtGenParamStatus':prtGenParamStatus,'prtGenRdnStatus':prtGenRdnStatus,'prtGenTestMaskXP':prtGenTestMaskXP,'prtGenTestCmdXP':prtGenTestCmdXP,'prtGenTestRunningXP':prtGenTestRunningXP,'prtGenTestDurationTable':prtGenTestDurationTable,'prtGenTestDurationEntry':prtGenTestDurationEntry,_Ax:prtGenTestPrtIdx,_Ay:prtGenTestIdx,'prtGenTestDuration':prtGenTestDuration,'prtGenTsTable':prtGenTsTable,'prtGenTsEntry':prtGenTsEntry,_Az:prtGenTsCnfgIdx,_A_:prtGenTsPrtIdx,_B0:prtGenTsIdx,'prtGenTsType':prtGenTsType,'prtGenTsIConPrt':prtGenTsIConPrt,'prtGenTsIConTs':prtGenTsIConTs,'prtAlr':prtAlr,'prtSAlarmTable':prtSAlarmTable,'prtSAlarmEntry':prtSAlarmEntry,_B2:prtSAlarmIdx,_B1:prtSAlarmPrtIdx,'prtSAlarmCode':prtSAlarmCode,'prtSAlarmState':prtSAlarmState,'prtSAlarmMask':prtSAlarmMask,'prtSAlarmInvert':prtSAlarmInvert,'prtSAlarmOnOff':prtSAlarmOnOff,'prtSAlarmCounter':prtSAlarmCounter,'prtAlrMaskTable':prtAlrMaskTable,'prtAlrMaskEntry':prtAlrMaskEntry,_B3:prtAlrMaskPrtIdx,'prtAlrMask':prtAlrMask,'prtBertTable':prtBertTable,'prtBertEntry':prtBertEntry,_B4:prtBertPrtIdx,'prtBertPattern':prtBertPattern,'prtBertInjectRate':prtBertInjectRate,'prtBertInjectErrRateCmd':prtBertInjectErrRateCmd,'prtBertInjectSingleErrCmd':prtBertInjectSingleErrCmd,'prtBertRunTime':prtBertRunTime,'prtBertESs':prtBertESs,'prtBertSyncLoss':prtBertSyncLoss,'prtBertErrorBits':prtBertErrorBits,'prtBertClearCounters':prtBertClearCounters,'prtBertSyncStatus':prtBertSyncStatus,'prtBertTs':prtBertTs,'prtBertResult':prtBertResult,'prtBertTxBits':prtBertTxBits,'prtBertRxBits':prtBertRxBits,'prtBertTxErrorBits':prtBertTxErrorBits,'prtMonTable':prtMonTable,'prtMonEntry':prtMonEntry,_B5:prtMonCnfgIdx,_B6:prtMonitoringIdx,'prtMonitoringEnable':prtMonitoringEnable,'prtMonitoringTSs':prtMonitoringTSs,'prtMonitoredPort':prtMonitoredPort,'prtMonitoredTSs':prtMonitoredTSs,'prtCfgParam':prtCfgParam,'prtCfgParamTable':prtCfgParamTable,'prtCfgParamEntry':prtCfgParamEntry,_B7:prtCfgParamCnfgIdx,_B8:prtCfgParamIdx,'prtCfgParamSlt':prtCfgParamSlt,'prtCfgParamOperatedMl':prtCfgParamOperatedMl,'prtCfgParamMlAtoMlBPrio':prtCfgParamMlAtoMlBPrio,'prtCfgParamMlBtoMlAPrio':prtCfgParamMlBtoMlAPrio,'prtCfgParamInbandLoopDetection':prtCfgParamInbandLoopDetection,'prtCfgParamInbandLoopPatternCfg':prtCfgParamInbandLoopPatternCfg,'prtCfgParamInbandLoopActPattern':prtCfgParamInbandLoopActPattern,'prtCfgParamInbandLoopDeactPattern':prtCfgParamInbandLoopDeactPattern,'prtT1E1':prtT1E1,'prtT1E1StatTable':prtT1E1StatTable,'prtT1E1StatEntry':prtT1E1StatEntry,_BA:prtT1E1SPrtIdx,'prtT1E1SSlt':prtT1E1SSlt,'prtT1E1OosCount':prtT1E1OosCount,'prtT1E1BpvLastMin':prtT1E1BpvLastMin,'prtT1E1BpvMax':prtT1E1BpvMax,'prtT1E1CnfgTable':prtT1E1CnfgTable,'prtT1E1CnfgEntry':prtT1E1CnfgEntry,_BB:prtT1E1CnfgIdx,_BC:prtT1E1PrtIdx,'prtT1E1Slt':prtT1E1Slt,'prtT1E1LineType':prtT1E1LineType,'prtT1E1LineCode':prtT1E1LineCode,'prtT1E1SignalMode':prtT1E1SignalMode,'prtT1E1Fdl':prtT1E1Fdl,'prtT1E1FdlMode':prtT1E1FdlMode,'prtT1E1Sync':prtT1E1Sync,'prtT1E1CGA':prtT1E1CGA,'prtT1E1IdleCode':prtT1E1IdleCode,'prtT1E1OosSignal':prtT1E1OosSignal,'prtT1E1VoiceOos':prtT1E1VoiceOos,'prtT1E1DataOos':prtT1E1DataOos,'prtT1E1LineLengthMask':prtT1E1LineLengthMask,'prtT1E1TxGainMask':prtT1E1TxGainMask,'prtT1E1InbandMng':prtT1E1InbandMng,'prtT1E1InbandMngRate':prtT1E1InbandMngRate,'prtT1E1DedicatedTs':prtT1E1DedicatedTs,'prtT1E1InbandMngRoutProt':prtT1E1InbandMngRoutProt,'prtT1E1LinkMode':prtT1E1LinkMode,'prtT1E1Multiplier':prtT1E1Multiplier,'prtT1E1RxGain':prtT1E1RxGain,'prtT1E1RAI':prtT1E1RAI,'prtT1E1LineMode':prtT1E1LineMode,'prtT1E1TS0SaBits':prtT1E1TS0SaBits,'prtT1E1ConnectedTS':prtT1E1ConnectedTS,'prtT1E1Ts0SaBit':prtT1E1Ts0SaBit,'prtT1E1SameFeCnfg':prtT1E1SameFeCnfg,'prtT1E1RemCrc4':prtT1E1RemCrc4,'prtT1E1MaxTSs':prtT1E1MaxTSs,'prtT1E1EocTsConfig':prtT1E1EocTsConfig,'prtT1E1Role':prtT1E1Role,'prtT1E1PppEchoFailDetection':prtT1E1PppEchoFailDetection,'prtT1E1CasOosPattern':prtT1E1CasOosPattern,'prtT1E1CasOosSpaceCode':prtT1E1CasOosSpaceCode,'prtT1E1CasOosMarkCode':prtT1E1CasOosMarkCode,'prtT1E1FdlMsgTable':prtT1E1FdlMsgTable,'prtT1E1FdlMsgEntry':prtT1E1FdlMsgEntry,_BE:prtT1E1FdlMsgPrtIdx,_BF:prtT1E1FdlMsgFdlType,'prtT1E1FdlMsgSlt':prtT1E1FdlMsgSlt,'prtT1E1FdlMsg':prtT1E1FdlMsg,'prtHS':prtHS,'prtHSParamTable':prtHSParamTable,'prtHSParamEntry':prtHSParamEntry,_BG:prtHSCnfgIdx,_BH:prtHSPrtIdx,'prtHSSlt':prtHSSlt,'prtHSRate':prtHSRate,'prtHSFifoSize':prtHSFifoSize,'prtHSClkMode':prtHSClkMode,'prtHSCTS':prtHSCTS,'prtHSRtsState':prtHSRtsState,'prtHSInbandLoopback':prtHSInbandLoopback,'prtHSInbandLoopPatternCfg':prtHSInbandLoopPatternCfg,'prtHSInbandLoopActPattern':prtHSInbandLoopActPattern,'prtHSInbandLoopDeactPattern':prtHSInbandLoopDeactPattern,'prtHSDCD':prtHSDCD,'prtHSClkPolarity':prtHSClkPolarity,'prtHSInterfaceType':prtHSInterfaceType,'prtHSUnframed':prtHSUnframed,'prtHSBertTable':prtHSBertTable,'prtHSBertEntry':prtHSBertEntry,_BI:prtHSBertPrtIdx,'prtHSBertSlt':prtHSBertSlt,'prtHSBertCountClr':prtHSBertCountClr,'prtHSBertTestResult':prtHSBertTestResult,'prtSP':prtSP,'prtSpCnfgTable':prtSpCnfgTable,'prtSpCnfgEntry':prtSpCnfgEntry,_BJ:prtSpCnfgIdx,_BK:prtSpPrtIdx,'prtSpUsage':prtSpUsage,'prtSpRate':prtSpRate,'prtSpDataBits':prtSpDataBits,'prtSpParity':prtSpParity,'prtSpCallOutMode':prtSpCallOutMode,'prtSpInterface':prtSpInterface,'prtSpCTS':prtSpCTS,'prtSpDcdDelay':prtSpDcdDelay,'prtSpDsr':prtSpDsr,'prtSpNoOfRetries':prtSpNoOfRetries,'prtSpWaitForConnect':prtSpWaitForConnect,'prtSpDialMode':prtSpDialMode,'prtSpAltNumMode':prtSpAltNumMode,'prtSpPrimaryNum':prtSpPrimaryNum,'prtSpAltNum':prtSpAltNum,'prtSpRoutProtocol':prtSpRoutProtocol,'prtSpCmd':prtSpCmd,'prtSpActCallOut':prtSpActCallOut,'prtSpAlrRelayMode':prtSpAlrRelayMode,'prtSpStopBits':prtSpStopBits,'prtDim':prtDim,'prtDimCnfgTable':prtDimCnfgTable,'prtDimCnfgEntry':prtDimCnfgEntry,_BL:prtDimCnfgIdx,_BM:prtDimIdx,'prtDimTxMode':prtDimTxMode,'prtDimPolarity':prtDimPolarity,'prtDimClkMode':prtDimClkMode,'prtDimMaxDelay':prtDimMaxDelay,'prtDimMng':prtDimMng,'prtDimMngRoutProt':prtDimMngRoutProt,'prtDimDestTable':prtDimDestTable,'prtDimDestEntry':prtDimDestEntry,_BN:prtDestCnfgIdx,_BO:prtDestDimIdx,_BP:prtDestIdx,'prtDest':prtDest,'prtDestConnect':prtDestConnect,'prtI':prtI,'prtICnfgTable':prtICnfgTable,'prtICnfgEntry':prtICnfgEntry,_BQ:prtICnfgIdx,'prtIIdx':prtIIdx,'prtIRate':prtIRate,'prtIConnect':prtIConnect,'prtHdsl':prtHdsl,'prtHdslTable':prtHdslTable,'prtHdslEntry':prtHdslEntry,_BR:prtHdslIdx,'prtHdslMode':prtHdslMode,'prtHdslRptrType':prtHdslRptrType,'prtHdslMaxRate':prtHdslMaxRate,'prtHdslLinkType':prtHdslLinkType,'prtHdslCompSwVer':prtHdslCompSwVer,'prtHdslCompHwVer':prtHdslCompHwVer,'prtT3E3':prtT3E3,'prtT3E3CnfgTable':prtT3E3CnfgTable,'prtT3E3CnfgEntry':prtT3E3CnfgEntry,_BS:prtT3E3CnfgIdx,_BT:prtT3E3PrtIdx,'prtT3E3Slt':prtT3E3Slt,'prtT3E3LineLength':prtT3E3LineLength,'prtT3E3InbandMng':prtT3E3InbandMng,'prtT3E3AisFrame':prtT3E3AisFrame,'prtT3E3TxClockSource':prtT3E3TxClockSource,'prtT3E3RoutProt':prtT3E3RoutProt,'prtT3E3AisTransmit':prtT3E3AisTransmit,'genDacsMux':genDacsMux,'cmprTable':cmprTable,'cmprEntry':cmprEntry,_BU:cmprTypeIdx,_BV:cmprCnfgIdx,_BW:cmprVersion,_BX:cmprSltIdx,_BY:cmprPrtIdx,'cmprObj':cmprObj,'mapLinkTable':mapLinkTable,'mapLinkEntry':mapLinkEntry,_BZ:mapLinkIdx,'mapLinkSlotIdx':mapLinkSlotIdx,'mapLinkPortIdx':mapLinkPortIdx,'mapLinkState':mapLinkState,'alrGenTable':alrGenTable,'alrGenEntry':alrGenEntry,_Ba:alrGenCode,'alrGenDescription':alrGenDescription,'alrGenLevel':alrGenLevel,'alrGenSlotType':alrGenSlotType,'alrGenSeverity':alrGenSeverity,'alrGenDebounce':alrGenDebounce,'alrGenDefSeverity':alrGenDefSeverity,'powerDeliveryFailure':powerDeliveryFailure})