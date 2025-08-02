_X='nbsDeviceTrapAdminPasswdChangeDescripton'
_W='nbsTrapRCMredundancyState'
_V='nbsTrapLoginName'
_U='nbsTrapWrongAccessDateTime'
_T='nbsDevPSHostIndex'
_S='unknown'
_R='nbsDevCPUIndex'
_Q='nbsDevPSInputIndex'
_P='NotificationType'
_O='nbsDevSNMPAccessMode'
_N='nbsTrapHostIpAddress'
_M='nbsDevAuthenticationRejectReason'
_L='nbsDevSessionType'
_K='nbsDevFANIndex'
_J='DisplayString'
_I='nbsDevPSIndex'
_H='notActive'
_G='active'
_F='read-write'
_E='DEV-CFG-MIB'
_D='none'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nbSwitchG1Il,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','nbSwitchG1Il')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_P,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_P,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
_NbDeviceConfig_ObjectIdentity=ObjectIdentity
nbDeviceConfig=_NbDeviceConfig_ObjectIdentity((1,3,6,1,4,1,629,1,50,11))
_NbDevGen_ObjectIdentity=ObjectIdentity
nbDevGen=_NbDevGen_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1))
class _NbDevOperationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('accelerouter',1),('router',2),('switch',3)))
_NbDevOperationMode_Type.__name__=_C
_NbDevOperationMode_Object=MibScalar
nbDevOperationMode=_NbDevOperationMode_Object((1,3,6,1,4,1,629,1,50,11,1,1),_NbDevOperationMode_Type())
nbDevOperationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nbDevOperationMode.setStatus(_A)
_NbDevErrorText_Type=DisplayString
_NbDevErrorText_Object=MibScalar
nbDevErrorText=_NbDevErrorText_Object((1,3,6,1,4,1,629,1,50,11,1,2),_NbDevErrorText_Type())
nbDevErrorText.setMaxAccess(_B)
if mibBuilder.loadTexts:nbDevErrorText.setStatus(_A)
class _NbsDevTftpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('server',2),('client',3)))
_NbsDevTftpMode_Type.__name__=_C
_NbsDevTftpMode_Object=MibScalar
nbsDevTftpMode=_NbsDevTftpMode_Object((1,3,6,1,4,1,629,1,50,11,1,3),_NbsDevTftpMode_Type())
nbsDevTftpMode.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsDevTftpMode.setStatus(_A)
class _NbDevRouterSaveConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('saveConfig',1),('warmReset',2),('coldReset',3),('backupReset',4)))
_NbDevRouterSaveConfig_Type.__name__=_C
_NbDevRouterSaveConfig_Object=MibScalar
nbDevRouterSaveConfig=_NbDevRouterSaveConfig_Object((1,3,6,1,4,1,629,1,50,11,1,4),_NbDevRouterSaveConfig_Type())
nbDevRouterSaveConfig.setMaxAccess(_F)
if mibBuilder.loadTexts:nbDevRouterSaveConfig.setStatus(_A)
class _NbsDevProperties_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8,16,32,64,128,256,512)));namedValues=NamedValues(*((_D,0),('redundantPowerSupply',1),('highDensityFibrePorts',2),('dcPowerSupply',4),('optiSwitch100FX',8),('chipModification',16),('expensiveModification',32),('telcoSubType',64),('extendedTempRange',128),('extraExtendedTempRange',256),('ptpSlaveSync',512)))
_NbsDevProperties_Type.__name__=_C
_NbsDevProperties_Object=MibScalar
nbsDevProperties=_NbsDevProperties_Object((1,3,6,1,4,1,629,1,50,11,1,5),_NbsDevProperties_Type())
nbsDevProperties.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevProperties.setStatus(_A)
class _NbsDevTemperatureMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('normal',2),('high',3)))
_NbsDevTemperatureMode_Type.__name__=_C
_NbsDevTemperatureMode_Object=MibScalar
nbsDevTemperatureMode=_NbsDevTemperatureMode_Object((1,3,6,1,4,1,629,1,50,11,1,6),_NbsDevTemperatureMode_Type())
nbsDevTemperatureMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevTemperatureMode.setStatus(_A)
class _NbsDevResetAfterDnldMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('yes',2),('no',3)))
_NbsDevResetAfterDnldMode_Type.__name__=_C
_NbsDevResetAfterDnldMode_Object=MibScalar
nbsDevResetAfterDnldMode=_NbsDevResetAfterDnldMode_Object((1,3,6,1,4,1,629,1,50,11,1,7),_NbsDevResetAfterDnldMode_Type())
nbsDevResetAfterDnldMode.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsDevResetAfterDnldMode.setStatus(_A)
_NbsDevPS_ObjectIdentity=ObjectIdentity
nbsDevPS=_NbsDevPS_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,8))
_NbsDevPSNumber_Type=Integer32
_NbsDevPSNumber_Object=MibScalar
nbsDevPSNumber=_NbsDevPSNumber_Object((1,3,6,1,4,1,629,1,50,11,1,8,1),_NbsDevPSNumber_Type())
nbsDevPSNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPSNumber.setStatus(_A)
_NbsDevPSTable_Object=MibTable
nbsDevPSTable=_NbsDevPSTable_Object((1,3,6,1,4,1,629,1,50,11,1,8,2))
if mibBuilder.loadTexts:nbsDevPSTable.setStatus(_A)
_NbsDevPSEntry_Object=MibTableRow
nbsDevPSEntry=_NbsDevPSEntry_Object((1,3,6,1,4,1,629,1,50,11,1,8,2,1))
nbsDevPSEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:nbsDevPSEntry.setStatus(_A)
_NbsDevPSIndex_Type=Integer32
_NbsDevPSIndex_Object=MibTableColumn
nbsDevPSIndex=_NbsDevPSIndex_Object((1,3,6,1,4,1,629,1,50,11,1,8,2,1,1),_NbsDevPSIndex_Type())
nbsDevPSIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPSIndex.setStatus(_A)
class _NbsDevPSType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('acPS',2),('dcPS',3),('externalPS',4)))
_NbsDevPSType_Type.__name__=_C
_NbsDevPSType_Object=MibTableColumn
nbsDevPSType=_NbsDevPSType_Object((1,3,6,1,4,1,629,1,50,11,1,8,2,1,2),_NbsDevPSType_Type())
nbsDevPSType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPSType.setStatus(_A)
_NbsDevPSDescription_Type=DisplayString
_NbsDevPSDescription_Object=MibTableColumn
nbsDevPSDescription=_NbsDevPSDescription_Object((1,3,6,1,4,1,629,1,50,11,1,8,2,1,3),_NbsDevPSDescription_Type())
nbsDevPSDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPSDescription.setStatus(_A)
class _NbsDevPSRedundantMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('mainPS',2),('secondaryPS',3)))
_NbsDevPSRedundantMode_Type.__name__=_C
_NbsDevPSRedundantMode_Object=MibTableColumn
nbsDevPSRedundantMode=_NbsDevPSRedundantMode_Object((1,3,6,1,4,1,629,1,50,11,1,8,2,1,4),_NbsDevPSRedundantMode_Type())
nbsDevPSRedundantMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPSRedundantMode.setStatus(_A)
class _NbsDevPSOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_NbsDevPSOperStatus_Type.__name__=_C
_NbsDevPSOperStatus_Object=MibTableColumn
nbsDevPSOperStatus=_NbsDevPSOperStatus_Object((1,3,6,1,4,1,629,1,50,11,1,8,2,1,5),_NbsDevPSOperStatus_Type())
nbsDevPSOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPSOperStatus.setStatus(_A)
class _NbsDevPSAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_NbsDevPSAdminStatus_Type.__name__=_C
_NbsDevPSAdminStatus_Object=MibTableColumn
nbsDevPSAdminStatus=_NbsDevPSAdminStatus_Object((1,3,6,1,4,1,629,1,50,11,1,8,2,1,6),_NbsDevPSAdminStatus_Type())
nbsDevPSAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsDevPSAdminStatus.setStatus(_A)
_NbsDevPSInput_ObjectIdentity=ObjectIdentity
nbsDevPSInput=_NbsDevPSInput_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,9))
_NbsDevPSInputNumber_Type=Integer32
_NbsDevPSInputNumber_Object=MibScalar
nbsDevPSInputNumber=_NbsDevPSInputNumber_Object((1,3,6,1,4,1,629,1,50,11,1,9,1),_NbsDevPSInputNumber_Type())
nbsDevPSInputNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPSInputNumber.setStatus(_A)
_NbsDevPSInputTable_Object=MibTable
nbsDevPSInputTable=_NbsDevPSInputTable_Object((1,3,6,1,4,1,629,1,50,11,1,9,2))
if mibBuilder.loadTexts:nbsDevPSInputTable.setStatus(_A)
_NbsDevPSInputEntry_Object=MibTableRow
nbsDevPSInputEntry=_NbsDevPSInputEntry_Object((1,3,6,1,4,1,629,1,50,11,1,9,2,1))
nbsDevPSInputEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:nbsDevPSInputEntry.setStatus(_A)
_NbsDevPSInputIndex_Type=Integer32
_NbsDevPSInputIndex_Object=MibTableColumn
nbsDevPSInputIndex=_NbsDevPSInputIndex_Object((1,3,6,1,4,1,629,1,50,11,1,9,2,1,1),_NbsDevPSInputIndex_Type())
nbsDevPSInputIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPSInputIndex.setStatus(_A)
class _NbsDevPSInputType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('acInput',2),('dcInput',3),('dcRedundInput',4)))
_NbsDevPSInputType_Type.__name__=_C
_NbsDevPSInputType_Object=MibTableColumn
nbsDevPSInputType=_NbsDevPSInputType_Object((1,3,6,1,4,1,629,1,50,11,1,9,2,1,2),_NbsDevPSInputType_Type())
nbsDevPSInputType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPSInputType.setStatus(_A)
_NbsDevPSInputDescription_Type=DisplayString
_NbsDevPSInputDescription_Object=MibTableColumn
nbsDevPSInputDescription=_NbsDevPSInputDescription_Object((1,3,6,1,4,1,629,1,50,11,1,9,2,1,3),_NbsDevPSInputDescription_Type())
nbsDevPSInputDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPSInputDescription.setStatus(_A)
class _NbsDevPSInputRedundantMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('mainInput',2),('secondaryInput',3)))
_NbsDevPSInputRedundantMode_Type.__name__=_C
_NbsDevPSInputRedundantMode_Object=MibTableColumn
nbsDevPSInputRedundantMode=_NbsDevPSInputRedundantMode_Object((1,3,6,1,4,1,629,1,50,11,1,9,2,1,4),_NbsDevPSInputRedundantMode_Type())
nbsDevPSInputRedundantMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPSInputRedundantMode.setStatus(_A)
class _NbsDevPSInputOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_NbsDevPSInputOperStatus_Type.__name__=_C
_NbsDevPSInputOperStatus_Object=MibTableColumn
nbsDevPSInputOperStatus=_NbsDevPSInputOperStatus_Object((1,3,6,1,4,1,629,1,50,11,1,9,2,1,5),_NbsDevPSInputOperStatus_Type())
nbsDevPSInputOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPSInputOperStatus.setStatus(_A)
class _NbsDevPSInputAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_NbsDevPSInputAdminStatus_Type.__name__=_C
_NbsDevPSInputAdminStatus_Object=MibTableColumn
nbsDevPSInputAdminStatus=_NbsDevPSInputAdminStatus_Object((1,3,6,1,4,1,629,1,50,11,1,9,2,1,6),_NbsDevPSInputAdminStatus_Type())
nbsDevPSInputAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsDevPSInputAdminStatus.setStatus(_A)
_NbsDevCPU_ObjectIdentity=ObjectIdentity
nbsDevCPU=_NbsDevCPU_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,10))
_NbsDevCPUNumber_Type=Integer32
_NbsDevCPUNumber_Object=MibScalar
nbsDevCPUNumber=_NbsDevCPUNumber_Object((1,3,6,1,4,1,629,1,50,11,1,10,1),_NbsDevCPUNumber_Type())
nbsDevCPUNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevCPUNumber.setStatus(_A)
_NbsDevCPUTable_Object=MibTable
nbsDevCPUTable=_NbsDevCPUTable_Object((1,3,6,1,4,1,629,1,50,11,1,10,2))
if mibBuilder.loadTexts:nbsDevCPUTable.setStatus(_A)
_NbsDevCPUEntry_Object=MibTableRow
nbsDevCPUEntry=_NbsDevCPUEntry_Object((1,3,6,1,4,1,629,1,50,11,1,10,2,1))
nbsDevCPUEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:nbsDevCPUEntry.setStatus(_A)
_NbsDevCPUIndex_Type=Integer32
_NbsDevCPUIndex_Object=MibTableColumn
nbsDevCPUIndex=_NbsDevCPUIndex_Object((1,3,6,1,4,1,629,1,50,11,1,10,2,1,1),_NbsDevCPUIndex_Type())
nbsDevCPUIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevCPUIndex.setStatus(_A)
class _NbsDevCPUType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('cx33cpu2MBflash16MBdram',2),('cx33cpu4MBflash16MBdram',3),('cx33cpu4MBflash64MBdram',4)))
_NbsDevCPUType_Type.__name__=_C
_NbsDevCPUType_Object=MibTableColumn
nbsDevCPUType=_NbsDevCPUType_Object((1,3,6,1,4,1,629,1,50,11,1,10,2,1,2),_NbsDevCPUType_Type())
nbsDevCPUType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevCPUType.setStatus(_A)
_NbsDevCPUDescription_Type=DisplayString
_NbsDevCPUDescription_Object=MibTableColumn
nbsDevCPUDescription=_NbsDevCPUDescription_Object((1,3,6,1,4,1,629,1,50,11,1,10,2,1,3),_NbsDevCPUDescription_Type())
nbsDevCPUDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevCPUDescription.setStatus(_A)
class _NbsDevCPURedundantMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('mainCPU',2),('redundantCPU',3)))
_NbsDevCPURedundantMode_Type.__name__=_C
_NbsDevCPURedundantMode_Object=MibTableColumn
nbsDevCPURedundantMode=_NbsDevCPURedundantMode_Object((1,3,6,1,4,1,629,1,50,11,1,10,2,1,4),_NbsDevCPURedundantMode_Type())
nbsDevCPURedundantMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevCPURedundantMode.setStatus(_A)
class _NbsDevCPUOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('enabled',2),('disabled',3)))
_NbsDevCPUOperStatus_Type.__name__=_C
_NbsDevCPUOperStatus_Object=MibTableColumn
nbsDevCPUOperStatus=_NbsDevCPUOperStatus_Object((1,3,6,1,4,1,629,1,50,11,1,10,2,1,5),_NbsDevCPUOperStatus_Type())
nbsDevCPUOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevCPUOperStatus.setStatus(_A)
class _NbsDevCPUAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('enable',2),('disable',3)))
_NbsDevCPUAdminStatus_Type.__name__=_C
_NbsDevCPUAdminStatus_Object=MibTableColumn
nbsDevCPUAdminStatus=_NbsDevCPUAdminStatus_Object((1,3,6,1,4,1,629,1,50,11,1,10,2,1,6),_NbsDevCPUAdminStatus_Type())
nbsDevCPUAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsDevCPUAdminStatus.setStatus(_A)
_NbsDevCPUOrderNumber_Type=Integer32
_NbsDevCPUOrderNumber_Object=MibTableColumn
nbsDevCPUOrderNumber=_NbsDevCPUOrderNumber_Object((1,3,6,1,4,1,629,1,50,11,1,10,2,1,7),_NbsDevCPUOrderNumber_Type())
nbsDevCPUOrderNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevCPUOrderNumber.setStatus(_A)
_NbsDevFAN_ObjectIdentity=ObjectIdentity
nbsDevFAN=_NbsDevFAN_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,11))
_NbsDevFANsNumber_Type=Integer32
_NbsDevFANsNumber_Object=MibScalar
nbsDevFANsNumber=_NbsDevFANsNumber_Object((1,3,6,1,4,1,629,1,50,11,1,11,1),_NbsDevFANsNumber_Type())
nbsDevFANsNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevFANsNumber.setStatus(_A)
_NbsDevFANTable_Object=MibTable
nbsDevFANTable=_NbsDevFANTable_Object((1,3,6,1,4,1,629,1,50,11,1,11,2))
if mibBuilder.loadTexts:nbsDevFANTable.setStatus(_A)
_NbsDevFANEntry_Object=MibTableRow
nbsDevFANEntry=_NbsDevFANEntry_Object((1,3,6,1,4,1,629,1,50,11,1,11,2,1))
nbsDevFANEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:nbsDevFANEntry.setStatus(_A)
_NbsDevFANIndex_Type=Integer32
_NbsDevFANIndex_Object=MibTableColumn
nbsDevFANIndex=_NbsDevFANIndex_Object((1,3,6,1,4,1,629,1,50,11,1,11,2,1,1),_NbsDevFANIndex_Type())
nbsDevFANIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevFANIndex.setStatus(_A)
class _NbsDevFANType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('fixed',2),('pwm',3)))
_NbsDevFANType_Type.__name__=_C
_NbsDevFANType_Object=MibTableColumn
nbsDevFANType=_NbsDevFANType_Object((1,3,6,1,4,1,629,1,50,11,1,11,2,1,2),_NbsDevFANType_Type())
nbsDevFANType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevFANType.setStatus(_A)
_NbsDevFANDescription_Type=DisplayString
_NbsDevFANDescription_Object=MibTableColumn
nbsDevFANDescription=_NbsDevFANDescription_Object((1,3,6,1,4,1,629,1,50,11,1,11,2,1,3),_NbsDevFANDescription_Type())
nbsDevFANDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevFANDescription.setStatus(_A)
class _NbsDevFANOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_NbsDevFANOperStatus_Type.__name__=_C
_NbsDevFANOperStatus_Object=MibTableColumn
nbsDevFANOperStatus=_NbsDevFANOperStatus_Object((1,3,6,1,4,1,629,1,50,11,1,11,2,1,5),_NbsDevFANOperStatus_Type())
nbsDevFANOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevFANOperStatus.setStatus(_A)
class _NbsDevFANAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_NbsDevFANAdminStatus_Type.__name__=_C
_NbsDevFANAdminStatus_Object=MibTableColumn
nbsDevFANAdminStatus=_NbsDevFANAdminStatus_Object((1,3,6,1,4,1,629,1,50,11,1,11,2,1,6),_NbsDevFANAdminStatus_Type())
nbsDevFANAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsDevFANAdminStatus.setStatus(_A)
_NbsDevFANSpeed_Type=Integer32
_NbsDevFANSpeed_Object=MibTableColumn
nbsDevFANSpeed=_NbsDevFANSpeed_Object((1,3,6,1,4,1,629,1,50,11,1,11,2,1,7),_NbsDevFANSpeed_Type())
nbsDevFANSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevFANSpeed.setStatus(_A)
class _NbsDevHeaterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('on',2),('off',3)))
_NbsDevHeaterStatus_Type.__name__=_C
_NbsDevHeaterStatus_Object=MibScalar
nbsDevHeaterStatus=_NbsDevHeaterStatus_Object((1,3,6,1,4,1,629,1,50,11,1,12),_NbsDevHeaterStatus_Type())
nbsDevHeaterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevHeaterStatus.setStatus(_A)
_NbsDevPhysParams_ObjectIdentity=ObjectIdentity
nbsDevPhysParams=_NbsDevPhysParams_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,13))
_NbsDevPhParamDevAmbientTempC_Type=Unsigned32
_NbsDevPhParamDevAmbientTempC_Object=MibScalar
nbsDevPhParamDevAmbientTempC=_NbsDevPhParamDevAmbientTempC_Object((1,3,6,1,4,1,629,1,50,11,1,13,1),_NbsDevPhParamDevAmbientTempC_Type())
nbsDevPhParamDevAmbientTempC.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPhParamDevAmbientTempC.setStatus(_A)
_NbsDevPhParamPackProcTempC_Type=Unsigned32
_NbsDevPhParamPackProcTempC_Object=MibScalar
nbsDevPhParamPackProcTempC=_NbsDevPhParamPackProcTempC_Object((1,3,6,1,4,1,629,1,50,11,1,13,2),_NbsDevPhParamPackProcTempC_Type())
nbsDevPhParamPackProcTempC.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPhParamPackProcTempC.setStatus(_A)
_NbsDevPhParamCpuTempC_Type=Unsigned32
_NbsDevPhParamCpuTempC_Object=MibScalar
nbsDevPhParamCpuTempC=_NbsDevPhParamCpuTempC_Object((1,3,6,1,4,1,629,1,50,11,1,13,3),_NbsDevPhParamCpuTempC_Type())
nbsDevPhParamCpuTempC.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPhParamCpuTempC.setStatus(_A)
_NbsDevPhParamDevAmbientTempF_Type=Unsigned32
_NbsDevPhParamDevAmbientTempF_Object=MibScalar
nbsDevPhParamDevAmbientTempF=_NbsDevPhParamDevAmbientTempF_Object((1,3,6,1,4,1,629,1,50,11,1,13,7),_NbsDevPhParamDevAmbientTempF_Type())
nbsDevPhParamDevAmbientTempF.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPhParamDevAmbientTempF.setStatus(_A)
_NbsDevPhParamPackProcTempF_Type=Unsigned32
_NbsDevPhParamPackProcTempF_Object=MibScalar
nbsDevPhParamPackProcTempF=_NbsDevPhParamPackProcTempF_Object((1,3,6,1,4,1,629,1,50,11,1,13,8),_NbsDevPhParamPackProcTempF_Type())
nbsDevPhParamPackProcTempF.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPhParamPackProcTempF.setStatus(_A)
_NbsDevPhParamCpuTempF_Type=Unsigned32
_NbsDevPhParamCpuTempF_Object=MibScalar
nbsDevPhParamCpuTempF=_NbsDevPhParamCpuTempF_Object((1,3,6,1,4,1,629,1,50,11,1,13,9),_NbsDevPhParamCpuTempF_Type())
nbsDevPhParamCpuTempF.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPhParamCpuTempF.setStatus(_A)
_NbsDevPSHost_ObjectIdentity=ObjectIdentity
nbsDevPSHost=_NbsDevPSHost_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,14))
_NbsDevPSHostsNumber_Type=Integer32
_NbsDevPSHostsNumber_Object=MibScalar
nbsDevPSHostsNumber=_NbsDevPSHostsNumber_Object((1,3,6,1,4,1,629,1,50,11,1,14,1),_NbsDevPSHostsNumber_Type())
nbsDevPSHostsNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPSHostsNumber.setStatus(_A)
_NbsDevPSHostTable_Object=MibTable
nbsDevPSHostTable=_NbsDevPSHostTable_Object((1,3,6,1,4,1,629,1,50,11,1,14,2))
if mibBuilder.loadTexts:nbsDevPSHostTable.setStatus(_A)
_NbsDevPSHostEntry_Object=MibTableRow
nbsDevPSHostEntry=_NbsDevPSHostEntry_Object((1,3,6,1,4,1,629,1,50,11,1,14,2,1))
nbsDevPSHostEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:nbsDevPSHostEntry.setStatus(_A)
_NbsDevPSHostIndex_Type=Integer32
_NbsDevPSHostIndex_Object=MibTableColumn
nbsDevPSHostIndex=_NbsDevPSHostIndex_Object((1,3,6,1,4,1,629,1,50,11,1,14,2,1,1),_NbsDevPSHostIndex_Type())
nbsDevPSHostIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPSHostIndex.setStatus(_A)
class _NbsDevPSHostType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('acPSHost',2),('dcPSHost',3)))
_NbsDevPSHostType_Type.__name__=_C
_NbsDevPSHostType_Object=MibTableColumn
nbsDevPSHostType=_NbsDevPSHostType_Object((1,3,6,1,4,1,629,1,50,11,1,14,2,1,2),_NbsDevPSHostType_Type())
nbsDevPSHostType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPSHostType.setStatus(_A)
_NbsDevPSHostDescr_Type=DisplayString
_NbsDevPSHostDescr_Object=MibTableColumn
nbsDevPSHostDescr=_NbsDevPSHostDescr_Object((1,3,6,1,4,1,629,1,50,11,1,14,2,1,3),_NbsDevPSHostDescr_Type())
nbsDevPSHostDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPSHostDescr.setStatus(_A)
_NbsDevPSHostPSNumber_Type=Integer32
_NbsDevPSHostPSNumber_Object=MibTableColumn
nbsDevPSHostPSNumber=_NbsDevPSHostPSNumber_Object((1,3,6,1,4,1,629,1,50,11,1,14,2,1,4),_NbsDevPSHostPSNumber_Type())
nbsDevPSHostPSNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPSHostPSNumber.setStatus(_A)
_NbsDevPSHostFirstPS_Type=Integer32
_NbsDevPSHostFirstPS_Object=MibTableColumn
nbsDevPSHostFirstPS=_NbsDevPSHostFirstPS_Object((1,3,6,1,4,1,629,1,50,11,1,14,2,1,6),_NbsDevPSHostFirstPS_Type())
nbsDevPSHostFirstPS.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPSHostFirstPS.setStatus(_A)
class _NbsDevPSHostOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_NbsDevPSHostOperStatus_Type.__name__=_C
_NbsDevPSHostOperStatus_Object=MibTableColumn
nbsDevPSHostOperStatus=_NbsDevPSHostOperStatus_Object((1,3,6,1,4,1,629,1,50,11,1,14,2,1,8),_NbsDevPSHostOperStatus_Type())
nbsDevPSHostOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevPSHostOperStatus.setStatus(_A)
class _NbsDevPSHostAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_G,2),(_H,3)))
_NbsDevPSHostAdminStatus_Type.__name__=_C
_NbsDevPSHostAdminStatus_Object=MibTableColumn
nbsDevPSHostAdminStatus=_NbsDevPSHostAdminStatus_Object((1,3,6,1,4,1,629,1,50,11,1,14,2,1,10),_NbsDevPSHostAdminStatus_Type())
nbsDevPSHostAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:nbsDevPSHostAdminStatus.setStatus(_A)
class _NbsDevTemperatureProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_S,1),('commercial',2),('extreme',3),('industrial',4),('nebsF2B',5),('nebsS2S',6)))
_NbsDevTemperatureProfile_Type.__name__=_C
_NbsDevTemperatureProfile_Object=MibScalar
nbsDevTemperatureProfile=_NbsDevTemperatureProfile_Object((1,3,6,1,4,1,629,1,50,11,1,15),_NbsDevTemperatureProfile_Type())
nbsDevTemperatureProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevTemperatureProfile.setStatus(_A)
_NbsSysRomVers_Type=DisplayString
_NbsSysRomVers_Object=MibScalar
nbsSysRomVers=_NbsSysRomVers_Object((1,3,6,1,4,1,629,1,50,11,1,15),_NbsSysRomVers_Type())
nbsSysRomVers.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsSysRomVers.setStatus(_A)
_NbsDevTrapVars_ObjectIdentity=ObjectIdentity
nbsDevTrapVars=_NbsDevTrapVars_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,50))
class _NbsDevSessionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cliSession',1),('telnetSession',2),(_D,3)))
_NbsDevSessionType_Type.__name__=_C
_NbsDevSessionType_Object=MibScalar
nbsDevSessionType=_NbsDevSessionType_Object((1,3,6,1,4,1,629,1,50,11,1,50,1),_NbsDevSessionType_Type())
nbsDevSessionType.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevSessionType.setStatus(_A)
class _NbsDevAuthenticationRejectReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('localAgentReject',1),('radiusServerReject',2),('radiusServerNotFound',3),(_D,4)))
_NbsDevAuthenticationRejectReason_Type.__name__=_C
_NbsDevAuthenticationRejectReason_Object=MibScalar
nbsDevAuthenticationRejectReason=_NbsDevAuthenticationRejectReason_Object((1,3,6,1,4,1,629,1,50,11,1,50,2),_NbsDevAuthenticationRejectReason_Type())
nbsDevAuthenticationRejectReason.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevAuthenticationRejectReason.setStatus(_A)
class _NbsTrapLoginName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsTrapLoginName_Type.__name__=_J
_NbsTrapLoginName_Object=MibScalar
nbsTrapLoginName=_NbsTrapLoginName_Object((1,3,6,1,4,1,629,1,50,11,1,50,5),_NbsTrapLoginName_Type())
nbsTrapLoginName.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsTrapLoginName.setStatus(_A)
class _NbsTrapHostIpAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsTrapHostIpAddress_Type.__name__=_J
_NbsTrapHostIpAddress_Object=MibScalar
nbsTrapHostIpAddress=_NbsTrapHostIpAddress_Object((1,3,6,1,4,1,629,1,50,11,1,50,6),_NbsTrapHostIpAddress_Type())
nbsTrapHostIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsTrapHostIpAddress.setStatus(_A)
class _NbsTrapWrongAccessDateTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NbsTrapWrongAccessDateTime_Type.__name__=_J
_NbsTrapWrongAccessDateTime_Object=MibScalar
nbsTrapWrongAccessDateTime=_NbsTrapWrongAccessDateTime_Object((1,3,6,1,4,1,629,1,50,11,1,50,7),_NbsTrapWrongAccessDateTime_Type())
nbsTrapWrongAccessDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsTrapWrongAccessDateTime.setStatus(_A)
_NbsTrapRCMredundancyState_Type=DisplayString
_NbsTrapRCMredundancyState_Object=MibScalar
nbsTrapRCMredundancyState=_NbsTrapRCMredundancyState_Object((1,3,6,1,4,1,629,1,50,11,1,50,8),_NbsTrapRCMredundancyState_Type())
nbsTrapRCMredundancyState.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsTrapRCMredundancyState.setStatus(_A)
class _NbsDevSNMPAccessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('readOnWriteOn',1),('readOnWriteOff',2),('readOffWriteOff',3)))
_NbsDevSNMPAccessMode_Type.__name__=_C
_NbsDevSNMPAccessMode_Object=MibScalar
nbsDevSNMPAccessMode=_NbsDevSNMPAccessMode_Object((1,3,6,1,4,1,629,1,50,11,1,50,10),_NbsDevSNMPAccessMode_Type())
nbsDevSNMPAccessMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDevSNMPAccessMode.setStatus(_A)
_NbsDeviceTrapReason_Type=DisplayString
_NbsDeviceTrapReason_Object=MibScalar
nbsDeviceTrapReason=_NbsDeviceTrapReason_Object((1,3,6,1,4,1,629,1,50,11,1,50,11),_NbsDeviceTrapReason_Type())
nbsDeviceTrapReason.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDeviceTrapReason.setStatus(_A)
_NbsDeviceTrapAdminPasswdChangeDescripton_Type=DisplayString
_NbsDeviceTrapAdminPasswdChangeDescripton_Object=MibScalar
nbsDeviceTrapAdminPasswdChangeDescripton=_NbsDeviceTrapAdminPasswdChangeDescripton_Object((1,3,6,1,4,1,629,1,50,11,1,50,12),_NbsDeviceTrapAdminPasswdChangeDescripton_Type())
nbsDeviceTrapAdminPasswdChangeDescripton.setMaxAccess(_B)
if mibBuilder.loadTexts:nbsDeviceTrapAdminPasswdChangeDescripton.setStatus(_A)
invalidPassword=NotificationType((1,3,6,1,4,1,629,1,50,11,1,0,7))
invalidPassword.setObjects(*((_E,_L),(_E,_M),(_E,_N)))
if mibBuilder.loadTexts:invalidPassword.setStatus('')
wrongAccess=NotificationType((1,3,6,1,4,1,629,1,50,11,1,0,8))
wrongAccess.setObjects(*((_E,_U),(_E,_L),(_E,_M),(_E,_V),(_E,_N)))
if mibBuilder.loadTexts:wrongAccess.setStatus('')
deviceRCMredundancyState=NotificationType((1,3,6,1,4,1,629,1,50,11,1,0,12))
deviceRCMredundancyState.setObjects((_E,_W))
if mibBuilder.loadTexts:deviceRCMredundancyState.setStatus('')
snmpAccessMode=NotificationType((1,3,6,1,4,1,629,1,50,11,1,0,20))
snmpAccessMode.setObjects((_E,_O))
if mibBuilder.loadTexts:snmpAccessMode.setStatus('')
snmpRequestRejected=NotificationType((1,3,6,1,4,1,629,1,50,11,1,0,21))
snmpRequestRejected.setObjects((_E,_O))
if mibBuilder.loadTexts:snmpRequestRejected.setStatus('')
deviceTemperatureNormal=NotificationType((1,3,6,1,4,1,629,1,50,11,1,0,48))
if mibBuilder.loadTexts:deviceTemperatureNormal.setStatus('')
deviceTemperatureHigh=NotificationType((1,3,6,1,4,1,629,1,50,11,1,0,49))
if mibBuilder.loadTexts:deviceTemperatureHigh.setStatus('')
AdminPasswdChange=NotificationType((1,3,6,1,4,1,629,1,50,11,1,0,50))
AdminPasswdChange.setObjects((_E,_X))
if mibBuilder.loadTexts:AdminPasswdChange.setStatus('')
powerSupplyUp=NotificationType((1,3,6,1,4,1,629,1,50,11,1,8,0,2))
powerSupplyUp.setObjects((_E,_I))
if mibBuilder.loadTexts:powerSupplyUp.setStatus('')
powerSupplyDown=NotificationType((1,3,6,1,4,1,629,1,50,11,1,8,0,3))
powerSupplyDown.setObjects((_E,_I))
if mibBuilder.loadTexts:powerSupplyDown.setStatus('')
powerSupplyPresent=NotificationType((1,3,6,1,4,1,629,1,50,11,1,8,0,4))
powerSupplyPresent.setObjects((_E,_I))
if mibBuilder.loadTexts:powerSupplyPresent.setStatus('')
powerSupplyNotPresent=NotificationType((1,3,6,1,4,1,629,1,50,11,1,8,0,5))
powerSupplyNotPresent.setObjects((_E,_I))
if mibBuilder.loadTexts:powerSupplyNotPresent.setStatus('')
fanUnitUp=NotificationType((1,3,6,1,4,1,629,1,50,11,1,11,0,46))
fanUnitUp.setObjects((_E,_K))
if mibBuilder.loadTexts:fanUnitUp.setStatus('')
fanUnitDown=NotificationType((1,3,6,1,4,1,629,1,50,11,1,11,0,47))
fanUnitDown.setObjects((_E,_K))
if mibBuilder.loadTexts:fanUnitDown.setStatus('')
mibBuilder.exportSymbols(_E,**{'nbDeviceConfig':nbDeviceConfig,'nbDevGen':nbDevGen,'invalidPassword':invalidPassword,'wrongAccess':wrongAccess,'deviceRCMredundancyState':deviceRCMredundancyState,'snmpAccessMode':snmpAccessMode,'snmpRequestRejected':snmpRequestRejected,'deviceTemperatureNormal':deviceTemperatureNormal,'deviceTemperatureHigh':deviceTemperatureHigh,'AdminPasswdChange':AdminPasswdChange,'nbDevOperationMode':nbDevOperationMode,'nbDevErrorText':nbDevErrorText,'nbsDevTftpMode':nbsDevTftpMode,'nbDevRouterSaveConfig':nbDevRouterSaveConfig,'nbsDevProperties':nbsDevProperties,'nbsDevTemperatureMode':nbsDevTemperatureMode,'nbsDevResetAfterDnldMode':nbsDevResetAfterDnldMode,'nbsDevPS':nbsDevPS,'powerSupplyUp':powerSupplyUp,'powerSupplyDown':powerSupplyDown,'powerSupplyPresent':powerSupplyPresent,'powerSupplyNotPresent':powerSupplyNotPresent,'nbsDevPSNumber':nbsDevPSNumber,'nbsDevPSTable':nbsDevPSTable,'nbsDevPSEntry':nbsDevPSEntry,_I:nbsDevPSIndex,'nbsDevPSType':nbsDevPSType,'nbsDevPSDescription':nbsDevPSDescription,'nbsDevPSRedundantMode':nbsDevPSRedundantMode,'nbsDevPSOperStatus':nbsDevPSOperStatus,'nbsDevPSAdminStatus':nbsDevPSAdminStatus,'nbsDevPSInput':nbsDevPSInput,'nbsDevPSInputNumber':nbsDevPSInputNumber,'nbsDevPSInputTable':nbsDevPSInputTable,'nbsDevPSInputEntry':nbsDevPSInputEntry,_Q:nbsDevPSInputIndex,'nbsDevPSInputType':nbsDevPSInputType,'nbsDevPSInputDescription':nbsDevPSInputDescription,'nbsDevPSInputRedundantMode':nbsDevPSInputRedundantMode,'nbsDevPSInputOperStatus':nbsDevPSInputOperStatus,'nbsDevPSInputAdminStatus':nbsDevPSInputAdminStatus,'nbsDevCPU':nbsDevCPU,'nbsDevCPUNumber':nbsDevCPUNumber,'nbsDevCPUTable':nbsDevCPUTable,'nbsDevCPUEntry':nbsDevCPUEntry,_R:nbsDevCPUIndex,'nbsDevCPUType':nbsDevCPUType,'nbsDevCPUDescription':nbsDevCPUDescription,'nbsDevCPURedundantMode':nbsDevCPURedundantMode,'nbsDevCPUOperStatus':nbsDevCPUOperStatus,'nbsDevCPUAdminStatus':nbsDevCPUAdminStatus,'nbsDevCPUOrderNumber':nbsDevCPUOrderNumber,'nbsDevFAN':nbsDevFAN,'fanUnitUp':fanUnitUp,'fanUnitDown':fanUnitDown,'nbsDevFANsNumber':nbsDevFANsNumber,'nbsDevFANTable':nbsDevFANTable,'nbsDevFANEntry':nbsDevFANEntry,_K:nbsDevFANIndex,'nbsDevFANType':nbsDevFANType,'nbsDevFANDescription':nbsDevFANDescription,'nbsDevFANOperStatus':nbsDevFANOperStatus,'nbsDevFANAdminStatus':nbsDevFANAdminStatus,'nbsDevFANSpeed':nbsDevFANSpeed,'nbsDevHeaterStatus':nbsDevHeaterStatus,'nbsDevPhysParams':nbsDevPhysParams,'nbsDevPhParamDevAmbientTempC':nbsDevPhParamDevAmbientTempC,'nbsDevPhParamPackProcTempC':nbsDevPhParamPackProcTempC,'nbsDevPhParamCpuTempC':nbsDevPhParamCpuTempC,'nbsDevPhParamDevAmbientTempF':nbsDevPhParamDevAmbientTempF,'nbsDevPhParamPackProcTempF':nbsDevPhParamPackProcTempF,'nbsDevPhParamCpuTempF':nbsDevPhParamCpuTempF,'nbsDevPSHost':nbsDevPSHost,'nbsDevPSHostsNumber':nbsDevPSHostsNumber,'nbsDevPSHostTable':nbsDevPSHostTable,'nbsDevPSHostEntry':nbsDevPSHostEntry,_T:nbsDevPSHostIndex,'nbsDevPSHostType':nbsDevPSHostType,'nbsDevPSHostDescr':nbsDevPSHostDescr,'nbsDevPSHostPSNumber':nbsDevPSHostPSNumber,'nbsDevPSHostFirstPS':nbsDevPSHostFirstPS,'nbsDevPSHostOperStatus':nbsDevPSHostOperStatus,'nbsDevPSHostAdminStatus':nbsDevPSHostAdminStatus,'nbsDevTemperatureProfile':nbsDevTemperatureProfile,'nbsSysRomVers':nbsSysRomVers,'nbsDevTrapVars':nbsDevTrapVars,_L:nbsDevSessionType,_M:nbsDevAuthenticationRejectReason,_V:nbsTrapLoginName,_N:nbsTrapHostIpAddress,_U:nbsTrapWrongAccessDateTime,_W:nbsTrapRCMredundancyState,_O:nbsDevSNMPAccessMode,'nbsDeviceTrapReason':nbsDeviceTrapReason,_X:nbsDeviceTrapAdminPasswdChangeDescripton})