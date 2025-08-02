_s='cpqIoDrvInfoPowerlossProtectDisabled'
_r='cpqIoDrvInfoState'
_q='cpqIoDrvInfoFlashbackIndicator'
_p='cpqIoDrvInfoNonWritableIndicator'
_o='cpqIoDrvInfoWearoutIndicator'
_n='cpqIoDrvProcIndex'
_m='cpqIoDrvTempIndex'
_l='cpqIoDrvTempInfoIndex'
_k='cpqIoDrvWriteIndex'
_j='cpqIoDrvWriteInfoIndex'
_i='cpqIoDrvCapacityIndex'
_h='cpqIoDrvCapacityInfoIndex'
_g='cpqIoDrvExtnIndex'
_f='optimal'
_e='suboptimal'
_d='incompatible'
_c='internal'
_b='failed'
_a='degraded'
_Z='NotificationType'
_Y='cpqIoDrvInfoCurrentTemp'
_X='heavy'
_W='moderate'
_V='light'
_U='unavailable'
_T='none'
_S='unknown'
_R='optional'
_Q='cpqIoDrvInfoPCISlot'
_P='cpqIoDrvInfoSerialNumber'
_O='cpqIoDrvInfoSparesPartNumber'
_N='cpqIoDrvInfoFirmwareVersion'
_M='cpqIoDrvInfoName'
_L='sysName'
_K='SNMPv2-MIB'
_J='cpqHoTrapFlags'
_I='CPQHOST-MIB'
_H='cpqIoDrvInfoIndex'
_G='read-write'
_F='DisplayString'
_E='obsolete'
_D='Integer32'
_C='CPQIODRV-MIB'
_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,cpqHoTrapFlags=mibBuilder.importSymbols(_I,'compaq',_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_K,_L)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_Z,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_Z,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
_CpqIoDrv_ObjectIdentity=ObjectIdentity
cpqIoDrv=_CpqIoDrv_ObjectIdentity((1,3,6,1,4,1,232,172))
_CpqIoDrvMibRev_ObjectIdentity=ObjectIdentity
cpqIoDrvMibRev=_CpqIoDrvMibRev_ObjectIdentity((1,3,6,1,4,1,232,172,1))
class _CpqIoDrvMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqIoDrvMibRevMajor_Type.__name__=_D
_CpqIoDrvMibRevMajor_Object=MibScalar
cpqIoDrvMibRevMajor=_CpqIoDrvMibRevMajor_Object((1,3,6,1,4,1,232,172,1,1),_CpqIoDrvMibRevMajor_Type())
cpqIoDrvMibRevMajor.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvMibRevMajor.setStatus(_B)
class _CpqIoDrvMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqIoDrvMibRevMinor_Type.__name__=_D
_CpqIoDrvMibRevMinor_Object=MibScalar
cpqIoDrvMibRevMinor=_CpqIoDrvMibRevMinor_Object((1,3,6,1,4,1,232,172,1,2),_CpqIoDrvMibRevMinor_Type())
cpqIoDrvMibRevMinor.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvMibRevMinor.setStatus(_B)
class _CpqIoDrvMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('ok',2),(_a,3),(_b,4)))
_CpqIoDrvMibCondition_Type.__name__=_D
_CpqIoDrvMibCondition_Object=MibScalar
cpqIoDrvMibCondition=_CpqIoDrvMibCondition_Object((1,3,6,1,4,1,232,172,1,3),_CpqIoDrvMibCondition_Type())
cpqIoDrvMibCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvMibCondition.setStatus(_B)
_CpqIoDrvComponent_ObjectIdentity=ObjectIdentity
cpqIoDrvComponent=_CpqIoDrvComponent_ObjectIdentity((1,3,6,1,4,1,232,172,2))
_CpqIoDrvInfo_ObjectIdentity=ObjectIdentity
cpqIoDrvInfo=_CpqIoDrvInfo_ObjectIdentity((1,3,6,1,4,1,232,172,2,1))
_CpqIoDrvInfoTable_Object=MibTable
cpqIoDrvInfoTable=_CpqIoDrvInfoTable_Object((1,3,6,1,4,1,232,172,2,1,1))
if mibBuilder.loadTexts:cpqIoDrvInfoTable.setStatus(_B)
_CpqIoDrvInfoEntry_Object=MibTableRow
cpqIoDrvInfoEntry=_CpqIoDrvInfoEntry_Object((1,3,6,1,4,1,232,172,2,1,1,1))
cpqIoDrvInfoEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cpqIoDrvInfoEntry.setStatus(_B)
class _CpqIoDrvInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_CpqIoDrvInfoIndex_Type.__name__=_D
_CpqIoDrvInfoIndex_Object=MibTableColumn
cpqIoDrvInfoIndex=_CpqIoDrvInfoIndex_Object((1,3,6,1,4,1,232,172,2,1,1,1,1),_CpqIoDrvInfoIndex_Type())
cpqIoDrvInfoIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoIndex.setStatus(_B)
class _CpqIoDrvInfoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('ok',2),(_a,3),(_b,4)))
_CpqIoDrvInfoStatus_Type.__name__=_D
_CpqIoDrvInfoStatus_Object=MibTableColumn
cpqIoDrvInfoStatus=_CpqIoDrvInfoStatus_Object((1,3,6,1,4,1,232,172,2,1,1,1,2),_CpqIoDrvInfoStatus_Type())
cpqIoDrvInfoStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoStatus.setStatus(_B)
class _CpqIoDrvInfoName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_CpqIoDrvInfoName_Type.__name__=_F
_CpqIoDrvInfoName_Object=MibTableColumn
cpqIoDrvInfoName=_CpqIoDrvInfoName_Object((1,3,6,1,4,1,232,172,2,1,1,1,3),_CpqIoDrvInfoName_Type())
cpqIoDrvInfoName.setMaxAccess(_G)
if mibBuilder.loadTexts:cpqIoDrvInfoName.setStatus(_B)
class _CpqIoDrvInfoSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_CpqIoDrvInfoSerialNumber_Type.__name__=_F
_CpqIoDrvInfoSerialNumber_Object=MibTableColumn
cpqIoDrvInfoSerialNumber=_CpqIoDrvInfoSerialNumber_Object((1,3,6,1,4,1,232,172,2,1,1,1,4),_CpqIoDrvInfoSerialNumber_Type())
cpqIoDrvInfoSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoSerialNumber.setStatus(_B)
class _CpqIoDrvInfoPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_CpqIoDrvInfoPartNumber_Type.__name__=_F
_CpqIoDrvInfoPartNumber_Object=MibTableColumn
cpqIoDrvInfoPartNumber=_CpqIoDrvInfoPartNumber_Object((1,3,6,1,4,1,232,172,2,1,1,1,5),_CpqIoDrvInfoPartNumber_Type())
cpqIoDrvInfoPartNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoPartNumber.setStatus(_B)
class _CpqIoDrvInfoSubVendorPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_CpqIoDrvInfoSubVendorPartNumber_Type.__name__=_F
_CpqIoDrvInfoSubVendorPartNumber_Object=MibTableColumn
cpqIoDrvInfoSubVendorPartNumber=_CpqIoDrvInfoSubVendorPartNumber_Object((1,3,6,1,4,1,232,172,2,1,1,1,6),_CpqIoDrvInfoSubVendorPartNumber_Type())
cpqIoDrvInfoSubVendorPartNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoSubVendorPartNumber.setStatus(_B)
class _CpqIoDrvInfoSparesPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_CpqIoDrvInfoSparesPartNumber_Type.__name__=_F
_CpqIoDrvInfoSparesPartNumber_Object=MibTableColumn
cpqIoDrvInfoSparesPartNumber=_CpqIoDrvInfoSparesPartNumber_Object((1,3,6,1,4,1,232,172,2,1,1,1,7),_CpqIoDrvInfoSparesPartNumber_Type())
cpqIoDrvInfoSparesPartNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoSparesPartNumber.setStatus(_B)
class _CpqIoDrvInfoAssemblyNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_CpqIoDrvInfoAssemblyNumber_Type.__name__=_F
_CpqIoDrvInfoAssemblyNumber_Object=MibTableColumn
cpqIoDrvInfoAssemblyNumber=_CpqIoDrvInfoAssemblyNumber_Object((1,3,6,1,4,1,232,172,2,1,1,1,8),_CpqIoDrvInfoAssemblyNumber_Type())
cpqIoDrvInfoAssemblyNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoAssemblyNumber.setStatus(_B)
class _CpqIoDrvInfoFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_CpqIoDrvInfoFirmwareVersion_Type.__name__=_F
_CpqIoDrvInfoFirmwareVersion_Object=MibTableColumn
cpqIoDrvInfoFirmwareVersion=_CpqIoDrvInfoFirmwareVersion_Object((1,3,6,1,4,1,232,172,2,1,1,1,9),_CpqIoDrvInfoFirmwareVersion_Type())
cpqIoDrvInfoFirmwareVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoFirmwareVersion.setStatus(_B)
class _CpqIoDrvInfoDriverVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_CpqIoDrvInfoDriverVersion_Type.__name__=_F
_CpqIoDrvInfoDriverVersion_Object=MibTableColumn
cpqIoDrvInfoDriverVersion=_CpqIoDrvInfoDriverVersion_Object((1,3,6,1,4,1,232,172,2,1,1,1,10),_CpqIoDrvInfoDriverVersion_Type())
cpqIoDrvInfoDriverVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoDriverVersion.setStatus(_B)
class _CpqIoDrvInfoUID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_CpqIoDrvInfoUID_Type.__name__=_F
_CpqIoDrvInfoUID_Object=MibTableColumn
cpqIoDrvInfoUID=_CpqIoDrvInfoUID_Object((1,3,6,1,4,1,232,172,2,1,1,1,11),_CpqIoDrvInfoUID_Type())
cpqIoDrvInfoUID.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoUID.setStatus(_B)
class _CpqIoDrvInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_S,0),('detached',1),('attached',2),('minimal',3),('error',4),('detaching',5),('attaching',6),('scanning',7),('formatting',8),('updating',9),('attach',10),('detach',11),('format',12),('update',13)))
_CpqIoDrvInfoState_Type.__name__=_D
_CpqIoDrvInfoState_Object=MibTableColumn
cpqIoDrvInfoState=_CpqIoDrvInfoState_Object((1,3,6,1,4,1,232,172,2,1,1,1,12),_CpqIoDrvInfoState_Type())
cpqIoDrvInfoState.setMaxAccess(_G)
if mibBuilder.loadTexts:cpqIoDrvInfoState.setStatus(_B)
class _CpqIoDrvInfoClientDeviceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_CpqIoDrvInfoClientDeviceName_Type.__name__=_F
_CpqIoDrvInfoClientDeviceName_Object=MibTableColumn
cpqIoDrvInfoClientDeviceName=_CpqIoDrvInfoClientDeviceName_Object((1,3,6,1,4,1,232,172,2,1,1,1,13),_CpqIoDrvInfoClientDeviceName_Type())
cpqIoDrvInfoClientDeviceName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoClientDeviceName.setStatus(_B)
_CpqIoDrvInfoBeacon_Type=Integer32
_CpqIoDrvInfoBeacon_Object=MibTableColumn
cpqIoDrvInfoBeacon=_CpqIoDrvInfoBeacon_Object((1,3,6,1,4,1,232,172,2,1,1,1,14),_CpqIoDrvInfoBeacon_Type())
cpqIoDrvInfoBeacon.setMaxAccess(_G)
if mibBuilder.loadTexts:cpqIoDrvInfoBeacon.setStatus(_B)
class _CpqIoDrvInfoPCIAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CpqIoDrvInfoPCIAddress_Type.__name__=_F
_CpqIoDrvInfoPCIAddress_Object=MibTableColumn
cpqIoDrvInfoPCIAddress=_CpqIoDrvInfoPCIAddress_Object((1,3,6,1,4,1,232,172,2,1,1,1,15),_CpqIoDrvInfoPCIAddress_Type())
cpqIoDrvInfoPCIAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoPCIAddress.setStatus(_B)
class _CpqIoDrvInfoPCIDeviceID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_CpqIoDrvInfoPCIDeviceID_Type.__name__=_F
_CpqIoDrvInfoPCIDeviceID_Object=MibTableColumn
cpqIoDrvInfoPCIDeviceID=_CpqIoDrvInfoPCIDeviceID_Object((1,3,6,1,4,1,232,172,2,1,1,1,16),_CpqIoDrvInfoPCIDeviceID_Type())
cpqIoDrvInfoPCIDeviceID.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoPCIDeviceID.setStatus(_B)
class _CpqIoDrvInfoPCISubdeviceID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_CpqIoDrvInfoPCISubdeviceID_Type.__name__=_F
_CpqIoDrvInfoPCISubdeviceID_Object=MibTableColumn
cpqIoDrvInfoPCISubdeviceID=_CpqIoDrvInfoPCISubdeviceID_Object((1,3,6,1,4,1,232,172,2,1,1,1,17),_CpqIoDrvInfoPCISubdeviceID_Type())
cpqIoDrvInfoPCISubdeviceID.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoPCISubdeviceID.setStatus(_B)
class _CpqIoDrvInfoPCIVendorID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_CpqIoDrvInfoPCIVendorID_Type.__name__=_F
_CpqIoDrvInfoPCIVendorID_Object=MibTableColumn
cpqIoDrvInfoPCIVendorID=_CpqIoDrvInfoPCIVendorID_Object((1,3,6,1,4,1,232,172,2,1,1,1,18),_CpqIoDrvInfoPCIVendorID_Type())
cpqIoDrvInfoPCIVendorID.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoPCIVendorID.setStatus(_B)
class _CpqIoDrvInfoPCISubvendorID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_CpqIoDrvInfoPCISubvendorID_Type.__name__=_F
_CpqIoDrvInfoPCISubvendorID_Object=MibTableColumn
cpqIoDrvInfoPCISubvendorID=_CpqIoDrvInfoPCISubvendorID_Object((1,3,6,1,4,1,232,172,2,1,1,1,19),_CpqIoDrvInfoPCISubvendorID_Type())
cpqIoDrvInfoPCISubvendorID.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoPCISubvendorID.setStatus(_B)
class _CpqIoDrvInfoPCISlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_CpqIoDrvInfoPCISlot_Type.__name__=_D
_CpqIoDrvInfoPCISlot_Object=MibTableColumn
cpqIoDrvInfoPCISlot=_CpqIoDrvInfoPCISlot_Object((1,3,6,1,4,1,232,172,2,1,1,1,20),_CpqIoDrvInfoPCISlot_Type())
cpqIoDrvInfoPCISlot.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoPCISlot.setStatus(_B)
_CpqIoDrvInfoWearoutIndicator_Type=Integer32
_CpqIoDrvInfoWearoutIndicator_Object=MibTableColumn
cpqIoDrvInfoWearoutIndicator=_CpqIoDrvInfoWearoutIndicator_Object((1,3,6,1,4,1,232,172,2,1,1,1,21),_CpqIoDrvInfoWearoutIndicator_Type())
cpqIoDrvInfoWearoutIndicator.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoWearoutIndicator.setStatus(_B)
_CpqIoDrvInfoFlashbackIndicator_Type=Integer32
_CpqIoDrvInfoFlashbackIndicator_Object=MibTableColumn
cpqIoDrvInfoFlashbackIndicator=_CpqIoDrvInfoFlashbackIndicator_Object((1,3,6,1,4,1,232,172,2,1,1,1,22),_CpqIoDrvInfoFlashbackIndicator_Type())
cpqIoDrvInfoFlashbackIndicator.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoFlashbackIndicator.setStatus(_B)
class _CpqIoDrvInfoNonWritableIndicator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('writeReduced',0),('nonWritable',1),('normal',2),(_S,3)))
_CpqIoDrvInfoNonWritableIndicator_Type.__name__=_D
_CpqIoDrvInfoNonWritableIndicator_Object=MibTableColumn
cpqIoDrvInfoNonWritableIndicator=_CpqIoDrvInfoNonWritableIndicator_Object((1,3,6,1,4,1,232,172,2,1,1,1,23),_CpqIoDrvInfoNonWritableIndicator_Type())
cpqIoDrvInfoNonWritableIndicator.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoNonWritableIndicator.setStatus(_B)
class _CpqIoDrvInfoCurrentTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_CpqIoDrvInfoCurrentTemp_Type.__name__=_D
_CpqIoDrvInfoCurrentTemp_Object=MibTableColumn
cpqIoDrvInfoCurrentTemp=_CpqIoDrvInfoCurrentTemp_Object((1,3,6,1,4,1,232,172,2,1,1,1,24),_CpqIoDrvInfoCurrentTemp_Type())
cpqIoDrvInfoCurrentTemp.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoCurrentTemp.setStatus(_B)
class _CpqIoDrvInfoPercentLifeRemaining_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_CpqIoDrvInfoPercentLifeRemaining_Type.__name__=_D
_CpqIoDrvInfoPercentLifeRemaining_Object=MibTableColumn
cpqIoDrvInfoPercentLifeRemaining=_CpqIoDrvInfoPercentLifeRemaining_Object((1,3,6,1,4,1,232,172,2,1,1,1,25),_CpqIoDrvInfoPercentLifeRemaining_Type())
cpqIoDrvInfoPercentLifeRemaining.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoPercentLifeRemaining.setStatus(_B)
_CpqIoDrvInfoShortTermWearoutDate_Type=DisplayString
_CpqIoDrvInfoShortTermWearoutDate_Object=MibTableColumn
cpqIoDrvInfoShortTermWearoutDate=_CpqIoDrvInfoShortTermWearoutDate_Object((1,3,6,1,4,1,232,172,2,1,1,1,26),_CpqIoDrvInfoShortTermWearoutDate_Type())
cpqIoDrvInfoShortTermWearoutDate.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoShortTermWearoutDate.setStatus(_E)
_CpqIoDrvInfoLongTermWearoutDate_Type=DisplayString
_CpqIoDrvInfoLongTermWearoutDate_Object=MibTableColumn
cpqIoDrvInfoLongTermWearoutDate=_CpqIoDrvInfoLongTermWearoutDate_Object((1,3,6,1,4,1,232,172,2,1,1,1,27),_CpqIoDrvInfoLongTermWearoutDate_Type())
cpqIoDrvInfoLongTermWearoutDate.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoLongTermWearoutDate.setStatus(_E)
_CpqIoDrvInfoShortTermNonWritableDate_Type=DisplayString
_CpqIoDrvInfoShortTermNonWritableDate_Object=MibTableColumn
cpqIoDrvInfoShortTermNonWritableDate=_CpqIoDrvInfoShortTermNonWritableDate_Object((1,3,6,1,4,1,232,172,2,1,1,1,28),_CpqIoDrvInfoShortTermNonWritableDate_Type())
cpqIoDrvInfoShortTermNonWritableDate.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoShortTermNonWritableDate.setStatus(_E)
_CpqIoDrvInfoLongTermNonWritableDate_Type=DisplayString
_CpqIoDrvInfoLongTermNonWritableDate_Object=MibTableColumn
cpqIoDrvInfoLongTermNonWritableDate=_CpqIoDrvInfoLongTermNonWritableDate_Object((1,3,6,1,4,1,232,172,2,1,1,1,29),_CpqIoDrvInfoLongTermNonWritableDate_Type())
cpqIoDrvInfoLongTermNonWritableDate.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoLongTermNonWritableDate.setStatus(_E)
class _CpqIoDrvInfoMinimalModeReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,5,6,7,8)));namedValues=NamedValues(*((_S,0),('fwOutOfDate',1),('lowPower',2),('dualPlaneFail',3),(_c,5),('cardLimitExceeded',6),('notInMinimalMode',7),('unsupportedOS',8)))
_CpqIoDrvInfoMinimalModeReason_Type.__name__=_D
_CpqIoDrvInfoMinimalModeReason_Object=MibTableColumn
cpqIoDrvInfoMinimalModeReason=_CpqIoDrvInfoMinimalModeReason_Object((1,3,6,1,4,1,232,172,2,1,1,1,30),_CpqIoDrvInfoMinimalModeReason_Type())
cpqIoDrvInfoMinimalModeReason.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoMinimalModeReason.setStatus(_B)
class _CpqIoDrvInfoReducedWriteReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_T,0),('userRequested',1),('noMdBlocks',2),('noMemory',3),('dieFailure',4),('wearout',5),('adapterPower',6),(_c,7),('powerLimiting',8),(_U,9),('groomFails',10)))
_CpqIoDrvInfoReducedWriteReason_Type.__name__=_D
_CpqIoDrvInfoReducedWriteReason_Object=MibTableColumn
cpqIoDrvInfoReducedWriteReason=_CpqIoDrvInfoReducedWriteReason_Object((1,3,6,1,4,1,232,172,2,1,1,1,31),_CpqIoDrvInfoReducedWriteReason_Type())
cpqIoDrvInfoReducedWriteReason.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoReducedWriteReason.setStatus(_B)
class _CpqIoDrvInfoMilliVolts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqIoDrvInfoMilliVolts_Type.__name__=_D
_CpqIoDrvInfoMilliVolts_Object=MibTableColumn
cpqIoDrvInfoMilliVolts=_CpqIoDrvInfoMilliVolts_Object((1,3,6,1,4,1,232,172,2,1,1,1,32),_CpqIoDrvInfoMilliVolts_Type())
cpqIoDrvInfoMilliVolts.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoMilliVolts.setStatus(_B)
class _CpqIoDrvInfoMilliVoltsPeak_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqIoDrvInfoMilliVoltsPeak_Type.__name__=_D
_CpqIoDrvInfoMilliVoltsPeak_Object=MibTableColumn
cpqIoDrvInfoMilliVoltsPeak=_CpqIoDrvInfoMilliVoltsPeak_Object((1,3,6,1,4,1,232,172,2,1,1,1,33),_CpqIoDrvInfoMilliVoltsPeak_Type())
cpqIoDrvInfoMilliVoltsPeak.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoMilliVoltsPeak.setStatus(_B)
class _CpqIoDrvInfoMilliVoltsMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqIoDrvInfoMilliVoltsMin_Type.__name__=_D
_CpqIoDrvInfoMilliVoltsMin_Object=MibTableColumn
cpqIoDrvInfoMilliVoltsMin=_CpqIoDrvInfoMilliVoltsMin_Object((1,3,6,1,4,1,232,172,2,1,1,1,34),_CpqIoDrvInfoMilliVoltsMin_Type())
cpqIoDrvInfoMilliVoltsMin.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoMilliVoltsMin.setStatus(_B)
class _CpqIoDrvInfoMilliWatts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqIoDrvInfoMilliWatts_Type.__name__=_D
_CpqIoDrvInfoMilliWatts_Object=MibTableColumn
cpqIoDrvInfoMilliWatts=_CpqIoDrvInfoMilliWatts_Object((1,3,6,1,4,1,232,172,2,1,1,1,35),_CpqIoDrvInfoMilliWatts_Type())
cpqIoDrvInfoMilliWatts.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoMilliWatts.setStatus(_B)
class _CpqIoDrvInfoMilliWattsPeak_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqIoDrvInfoMilliWattsPeak_Type.__name__=_D
_CpqIoDrvInfoMilliWattsPeak_Object=MibTableColumn
cpqIoDrvInfoMilliWattsPeak=_CpqIoDrvInfoMilliWattsPeak_Object((1,3,6,1,4,1,232,172,2,1,1,1,36),_CpqIoDrvInfoMilliWattsPeak_Type())
cpqIoDrvInfoMilliWattsPeak.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoMilliWattsPeak.setStatus(_B)
class _CpqIoDrvInfoMilliAmps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqIoDrvInfoMilliAmps_Type.__name__=_D
_CpqIoDrvInfoMilliAmps_Object=MibTableColumn
cpqIoDrvInfoMilliAmps=_CpqIoDrvInfoMilliAmps_Object((1,3,6,1,4,1,232,172,2,1,1,1,37),_CpqIoDrvInfoMilliAmps_Type())
cpqIoDrvInfoMilliAmps.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoMilliAmps.setStatus(_B)
class _CpqIoDrvInfoMilliAmpsPeak_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqIoDrvInfoMilliAmpsPeak_Type.__name__=_D
_CpqIoDrvInfoMilliAmpsPeak_Object=MibTableColumn
cpqIoDrvInfoMilliAmpsPeak=_CpqIoDrvInfoMilliAmpsPeak_Object((1,3,6,1,4,1,232,172,2,1,1,1,38),_CpqIoDrvInfoMilliAmpsPeak_Type())
cpqIoDrvInfoMilliAmpsPeak.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoMilliAmpsPeak.setStatus(_B)
class _CpqIoDrvInfoAdapterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('iodrive',0),('iodriveLowPro2',1),('iodriveDuo',2),('iosan',3),(_S,4),('ioOctal',5)))
_CpqIoDrvInfoAdapterType_Type.__name__=_D
_CpqIoDrvInfoAdapterType_Object=MibTableColumn
cpqIoDrvInfoAdapterType=_CpqIoDrvInfoAdapterType_Object((1,3,6,1,4,1,232,172,2,1,1,1,39),_CpqIoDrvInfoAdapterType_Type())
cpqIoDrvInfoAdapterType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoAdapterType.setStatus(_B)
class _CpqIoDrvInfoAdapterPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,65535))
_CpqIoDrvInfoAdapterPort_Type.__name__=_D
_CpqIoDrvInfoAdapterPort_Object=MibTableColumn
cpqIoDrvInfoAdapterPort=_CpqIoDrvInfoAdapterPort_Object((1,3,6,1,4,1,232,172,2,1,1,1,40),_CpqIoDrvInfoAdapterPort_Type())
cpqIoDrvInfoAdapterPort.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoAdapterPort.setStatus(_B)
class _CpqIoDrvInfoAdapterSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_CpqIoDrvInfoAdapterSerialNumber_Type.__name__=_F
_CpqIoDrvInfoAdapterSerialNumber_Object=MibTableColumn
cpqIoDrvInfoAdapterSerialNumber=_CpqIoDrvInfoAdapterSerialNumber_Object((1,3,6,1,4,1,232,172,2,1,1,1,41),_CpqIoDrvInfoAdapterSerialNumber_Type())
cpqIoDrvInfoAdapterSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoAdapterSerialNumber.setStatus(_B)
_CpqIoDrvInfoAdapterExtPowerPresent_Type=Integer32
_CpqIoDrvInfoAdapterExtPowerPresent_Object=MibTableColumn
cpqIoDrvInfoAdapterExtPowerPresent=_CpqIoDrvInfoAdapterExtPowerPresent_Object((1,3,6,1,4,1,232,172,2,1,1,1,42),_CpqIoDrvInfoAdapterExtPowerPresent_Type())
cpqIoDrvInfoAdapterExtPowerPresent.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoAdapterExtPowerPresent.setStatus(_B)
_CpqIoDrvInfoPowerlossProtectDisabled_Type=Integer32
_CpqIoDrvInfoPowerlossProtectDisabled_Object=MibTableColumn
cpqIoDrvInfoPowerlossProtectDisabled=_CpqIoDrvInfoPowerlossProtectDisabled_Object((1,3,6,1,4,1,232,172,2,1,1,1,43),_CpqIoDrvInfoPowerlossProtectDisabled_Type())
cpqIoDrvInfoPowerlossProtectDisabled.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoPowerlossProtectDisabled.setStatus(_B)
_CpqIoDrvInfoInternalTempHigh_Type=Integer32
_CpqIoDrvInfoInternalTempHigh_Object=MibTableColumn
cpqIoDrvInfoInternalTempHigh=_CpqIoDrvInfoInternalTempHigh_Object((1,3,6,1,4,1,232,172,2,1,1,1,44),_CpqIoDrvInfoInternalTempHigh_Type())
cpqIoDrvInfoInternalTempHigh.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoInternalTempHigh.setStatus(_B)
class _CpqIoDrvInfoAmbientTemp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,100))
_CpqIoDrvInfoAmbientTemp_Type.__name__=_D
_CpqIoDrvInfoAmbientTemp_Object=MibTableColumn
cpqIoDrvInfoAmbientTemp=_CpqIoDrvInfoAmbientTemp_Object((1,3,6,1,4,1,232,172,2,1,1,1,45),_CpqIoDrvInfoAmbientTemp_Type())
cpqIoDrvInfoAmbientTemp.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoAmbientTemp.setStatus(_E)
class _CpqIoDrvInfoPCIBandwidthCompatibility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,16,2048,32768)));namedValues=NamedValues(*((_d,0),(_e,16),(_f,2048),(_S,32768)))
_CpqIoDrvInfoPCIBandwidthCompatibility_Type.__name__=_D
_CpqIoDrvInfoPCIBandwidthCompatibility_Object=MibTableColumn
cpqIoDrvInfoPCIBandwidthCompatibility=_CpqIoDrvInfoPCIBandwidthCompatibility_Object((1,3,6,1,4,1,232,172,2,1,1,1,46),_CpqIoDrvInfoPCIBandwidthCompatibility_Type())
cpqIoDrvInfoPCIBandwidthCompatibility.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoPCIBandwidthCompatibility.setStatus(_B)
class _CpqIoDrvInfoPCIPowerCompatibility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,16,2048,32768)));namedValues=NamedValues(*((_d,0),(_e,16),(_f,2048),(_S,32768)))
_CpqIoDrvInfoPCIPowerCompatibility_Type.__name__=_D
_CpqIoDrvInfoPCIPowerCompatibility_Object=MibTableColumn
cpqIoDrvInfoPCIPowerCompatibility=_CpqIoDrvInfoPCIPowerCompatibility_Object((1,3,6,1,4,1,232,172,2,1,1,1,47),_CpqIoDrvInfoPCIPowerCompatibility_Type())
cpqIoDrvInfoPCIPowerCompatibility.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoPCIPowerCompatibility.setStatus(_B)
class _CpqIoDrvInfoActualGoverningLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_T,0),(_V,1),(_W,2),(_X,3),(_U,4)))
_CpqIoDrvInfoActualGoverningLevel_Type.__name__=_D
_CpqIoDrvInfoActualGoverningLevel_Object=MibTableColumn
cpqIoDrvInfoActualGoverningLevel=_CpqIoDrvInfoActualGoverningLevel_Object((1,3,6,1,4,1,232,172,2,1,1,1,48),_CpqIoDrvInfoActualGoverningLevel_Type())
cpqIoDrvInfoActualGoverningLevel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoActualGoverningLevel.setStatus(_B)
class _CpqIoDrvInfoLifespanGoverningLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_T,0),(_V,1),(_W,2),(_X,3),(_U,4)))
_CpqIoDrvInfoLifespanGoverningLevel_Type.__name__=_D
_CpqIoDrvInfoLifespanGoverningLevel_Object=MibTableColumn
cpqIoDrvInfoLifespanGoverningLevel=_CpqIoDrvInfoLifespanGoverningLevel_Object((1,3,6,1,4,1,232,172,2,1,1,1,49),_CpqIoDrvInfoLifespanGoverningLevel_Type())
cpqIoDrvInfoLifespanGoverningLevel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoLifespanGoverningLevel.setStatus(_B)
class _CpqIoDrvInfoPowerGoverningLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_T,0),(_V,1),(_W,2),(_X,3),(_U,4)))
_CpqIoDrvInfoPowerGoverningLevel_Type.__name__=_D
_CpqIoDrvInfoPowerGoverningLevel_Object=MibTableColumn
cpqIoDrvInfoPowerGoverningLevel=_CpqIoDrvInfoPowerGoverningLevel_Object((1,3,6,1,4,1,232,172,2,1,1,1,50),_CpqIoDrvInfoPowerGoverningLevel_Type())
cpqIoDrvInfoPowerGoverningLevel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoPowerGoverningLevel.setStatus(_B)
class _CpqIoDrvInfoThermalGoverningLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_T,0),(_V,1),(_W,2),(_X,3),(_U,4)))
_CpqIoDrvInfoThermalGoverningLevel_Type.__name__=_D
_CpqIoDrvInfoThermalGoverningLevel_Object=MibTableColumn
cpqIoDrvInfoThermalGoverningLevel=_CpqIoDrvInfoThermalGoverningLevel_Object((1,3,6,1,4,1,232,172,2,1,1,1,51),_CpqIoDrvInfoThermalGoverningLevel_Type())
cpqIoDrvInfoThermalGoverningLevel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoThermalGoverningLevel.setStatus(_B)
_CpqIoDrvInfoLifespanGoverningEnabled_Type=Integer32
_CpqIoDrvInfoLifespanGoverningEnabled_Object=MibTableColumn
cpqIoDrvInfoLifespanGoverningEnabled=_CpqIoDrvInfoLifespanGoverningEnabled_Object((1,3,6,1,4,1,232,172,2,1,1,1,52),_CpqIoDrvInfoLifespanGoverningEnabled_Type())
cpqIoDrvInfoLifespanGoverningEnabled.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoLifespanGoverningEnabled.setStatus(_B)
class _CpqIoDrvInfoLifespanGoverningTgtDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_CpqIoDrvInfoLifespanGoverningTgtDate_Type.__name__=_F
_CpqIoDrvInfoLifespanGoverningTgtDate_Object=MibTableColumn
cpqIoDrvInfoLifespanGoverningTgtDate=_CpqIoDrvInfoLifespanGoverningTgtDate_Object((1,3,6,1,4,1,232,172,2,1,1,1,53),_CpqIoDrvInfoLifespanGoverningTgtDate_Type())
cpqIoDrvInfoLifespanGoverningTgtDate.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvInfoLifespanGoverningTgtDate.setStatus(_B)
_CpqIoDrvExtn_ObjectIdentity=ObjectIdentity
cpqIoDrvExtn=_CpqIoDrvExtn_ObjectIdentity((1,3,6,1,4,1,232,172,2,2))
_CpqIoDrvExtnTable_Object=MibTable
cpqIoDrvExtnTable=_CpqIoDrvExtnTable_Object((1,3,6,1,4,1,232,172,2,2,1))
if mibBuilder.loadTexts:cpqIoDrvExtnTable.setStatus(_B)
_CpqIoDrvExtnEntry_Object=MibTableRow
cpqIoDrvExtnEntry=_CpqIoDrvExtnEntry_Object((1,3,6,1,4,1,232,172,2,2,1,1))
cpqIoDrvExtnEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:cpqIoDrvExtnEntry.setStatus(_B)
class _CpqIoDrvExtnIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_CpqIoDrvExtnIndex_Type.__name__=_D
_CpqIoDrvExtnIndex_Object=MibTableColumn
cpqIoDrvExtnIndex=_CpqIoDrvExtnIndex_Object((1,3,6,1,4,1,232,172,2,2,1,1,1),_CpqIoDrvExtnIndex_Type())
cpqIoDrvExtnIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvExtnIndex.setStatus(_B)
_CpqIoDrvExtnTotalPhysicalCapacityU_Type=Counter32
_CpqIoDrvExtnTotalPhysicalCapacityU_Object=MibTableColumn
cpqIoDrvExtnTotalPhysicalCapacityU=_CpqIoDrvExtnTotalPhysicalCapacityU_Object((1,3,6,1,4,1,232,172,2,2,1,1,2),_CpqIoDrvExtnTotalPhysicalCapacityU_Type())
cpqIoDrvExtnTotalPhysicalCapacityU.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvExtnTotalPhysicalCapacityU.setStatus(_B)
_CpqIoDrvExtnTotalPhysicalCapacityL_Type=Counter32
_CpqIoDrvExtnTotalPhysicalCapacityL_Object=MibTableColumn
cpqIoDrvExtnTotalPhysicalCapacityL=_CpqIoDrvExtnTotalPhysicalCapacityL_Object((1,3,6,1,4,1,232,172,2,2,1,1,3),_CpqIoDrvExtnTotalPhysicalCapacityL_Type())
cpqIoDrvExtnTotalPhysicalCapacityL.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvExtnTotalPhysicalCapacityL.setStatus(_B)
_CpqIoDrvExtnUsablePhysicalCapacityU_Type=Counter32
_CpqIoDrvExtnUsablePhysicalCapacityU_Object=MibTableColumn
cpqIoDrvExtnUsablePhysicalCapacityU=_CpqIoDrvExtnUsablePhysicalCapacityU_Object((1,3,6,1,4,1,232,172,2,2,1,1,4),_CpqIoDrvExtnUsablePhysicalCapacityU_Type())
cpqIoDrvExtnUsablePhysicalCapacityU.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvExtnUsablePhysicalCapacityU.setStatus(_E)
_CpqIoDrvExtnUsablePhysicalCapacityL_Type=Counter32
_CpqIoDrvExtnUsablePhysicalCapacityL_Object=MibTableColumn
cpqIoDrvExtnUsablePhysicalCapacityL=_CpqIoDrvExtnUsablePhysicalCapacityL_Object((1,3,6,1,4,1,232,172,2,2,1,1,5),_CpqIoDrvExtnUsablePhysicalCapacityL_Type())
cpqIoDrvExtnUsablePhysicalCapacityL.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvExtnUsablePhysicalCapacityL.setStatus(_E)
_CpqIoDrvExtnUsedPhysicalCapacityU_Type=Counter32
_CpqIoDrvExtnUsedPhysicalCapacityU_Object=MibTableColumn
cpqIoDrvExtnUsedPhysicalCapacityU=_CpqIoDrvExtnUsedPhysicalCapacityU_Object((1,3,6,1,4,1,232,172,2,2,1,1,6),_CpqIoDrvExtnUsedPhysicalCapacityU_Type())
cpqIoDrvExtnUsedPhysicalCapacityU.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvExtnUsedPhysicalCapacityU.setStatus(_E)
_CpqIoDrvExtnUsedPhysicalCapacityL_Type=Counter32
_CpqIoDrvExtnUsedPhysicalCapacityL_Object=MibTableColumn
cpqIoDrvExtnUsedPhysicalCapacityL=_CpqIoDrvExtnUsedPhysicalCapacityL_Object((1,3,6,1,4,1,232,172,2,2,1,1,7),_CpqIoDrvExtnUsedPhysicalCapacityL_Type())
cpqIoDrvExtnUsedPhysicalCapacityL.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvExtnUsedPhysicalCapacityL.setStatus(_E)
_CpqIoDrvExtnTotalLogicalCapacityU_Type=Counter32
_CpqIoDrvExtnTotalLogicalCapacityU_Object=MibTableColumn
cpqIoDrvExtnTotalLogicalCapacityU=_CpqIoDrvExtnTotalLogicalCapacityU_Object((1,3,6,1,4,1,232,172,2,2,1,1,8),_CpqIoDrvExtnTotalLogicalCapacityU_Type())
cpqIoDrvExtnTotalLogicalCapacityU.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvExtnTotalLogicalCapacityU.setStatus(_B)
_CpqIoDrvExtnTotalLogicalCapacityL_Type=Counter32
_CpqIoDrvExtnTotalLogicalCapacityL_Object=MibTableColumn
cpqIoDrvExtnTotalLogicalCapacityL=_CpqIoDrvExtnTotalLogicalCapacityL_Object((1,3,6,1,4,1,232,172,2,2,1,1,9),_CpqIoDrvExtnTotalLogicalCapacityL_Type())
cpqIoDrvExtnTotalLogicalCapacityL.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvExtnTotalLogicalCapacityL.setStatus(_B)
_CpqIoDrvExtnAvailableLogicalCapacityU_Type=Counter32
_CpqIoDrvExtnAvailableLogicalCapacityU_Object=MibTableColumn
cpqIoDrvExtnAvailableLogicalCapacityU=_CpqIoDrvExtnAvailableLogicalCapacityU_Object((1,3,6,1,4,1,232,172,2,2,1,1,10),_CpqIoDrvExtnAvailableLogicalCapacityU_Type())
cpqIoDrvExtnAvailableLogicalCapacityU.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvExtnAvailableLogicalCapacityU.setStatus(_E)
_CpqIoDrvExtnAvailableLogicalCapacityL_Type=Counter32
_CpqIoDrvExtnAvailableLogicalCapacityL_Object=MibTableColumn
cpqIoDrvExtnAvailableLogicalCapacityL=_CpqIoDrvExtnAvailableLogicalCapacityL_Object((1,3,6,1,4,1,232,172,2,2,1,1,11),_CpqIoDrvExtnAvailableLogicalCapacityL_Type())
cpqIoDrvExtnAvailableLogicalCapacityL.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvExtnAvailableLogicalCapacityL.setStatus(_E)
_CpqIoDrvExtnBytesReadU_Type=Counter32
_CpqIoDrvExtnBytesReadU_Object=MibTableColumn
cpqIoDrvExtnBytesReadU=_CpqIoDrvExtnBytesReadU_Object((1,3,6,1,4,1,232,172,2,2,1,1,12),_CpqIoDrvExtnBytesReadU_Type())
cpqIoDrvExtnBytesReadU.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvExtnBytesReadU.setStatus(_B)
_CpqIoDrvExtnBytesReadL_Type=Counter32
_CpqIoDrvExtnBytesReadL_Object=MibTableColumn
cpqIoDrvExtnBytesReadL=_CpqIoDrvExtnBytesReadL_Object((1,3,6,1,4,1,232,172,2,2,1,1,13),_CpqIoDrvExtnBytesReadL_Type())
cpqIoDrvExtnBytesReadL.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvExtnBytesReadL.setStatus(_B)
_CpqIoDrvExtnPhysicalBytesWrittenU_Type=Counter32
_CpqIoDrvExtnPhysicalBytesWrittenU_Object=MibTableColumn
cpqIoDrvExtnPhysicalBytesWrittenU=_CpqIoDrvExtnPhysicalBytesWrittenU_Object((1,3,6,1,4,1,232,172,2,2,1,1,14),_CpqIoDrvExtnPhysicalBytesWrittenU_Type())
cpqIoDrvExtnPhysicalBytesWrittenU.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvExtnPhysicalBytesWrittenU.setStatus(_B)
_CpqIoDrvExtnPhysicalBytesWrittenL_Type=Counter32
_CpqIoDrvExtnPhysicalBytesWrittenL_Object=MibTableColumn
cpqIoDrvExtnPhysicalBytesWrittenL=_CpqIoDrvExtnPhysicalBytesWrittenL_Object((1,3,6,1,4,1,232,172,2,2,1,1,15),_CpqIoDrvExtnPhysicalBytesWrittenL_Type())
cpqIoDrvExtnPhysicalBytesWrittenL.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvExtnPhysicalBytesWrittenL.setStatus(_B)
_CpqIoDrvExtnLogicalBytesWrittenU_Type=Counter32
_CpqIoDrvExtnLogicalBytesWrittenU_Object=MibTableColumn
cpqIoDrvExtnLogicalBytesWrittenU=_CpqIoDrvExtnLogicalBytesWrittenU_Object((1,3,6,1,4,1,232,172,2,2,1,1,16),_CpqIoDrvExtnLogicalBytesWrittenU_Type())
cpqIoDrvExtnLogicalBytesWrittenU.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvExtnLogicalBytesWrittenU.setStatus(_E)
_CpqIoDrvExtnLogicalBytesWrittenL_Type=Counter32
_CpqIoDrvExtnLogicalBytesWrittenL_Object=MibTableColumn
cpqIoDrvExtnLogicalBytesWrittenL=_CpqIoDrvExtnLogicalBytesWrittenL_Object((1,3,6,1,4,1,232,172,2,2,1,1,17),_CpqIoDrvExtnLogicalBytesWrittenL_Type())
cpqIoDrvExtnLogicalBytesWrittenL.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvExtnLogicalBytesWrittenL.setStatus(_E)
_CpqIoDrvExtnShortTermStartDate_Type=DisplayString
_CpqIoDrvExtnShortTermStartDate_Object=MibTableColumn
cpqIoDrvExtnShortTermStartDate=_CpqIoDrvExtnShortTermStartDate_Object((1,3,6,1,4,1,232,172,2,2,1,1,18),_CpqIoDrvExtnShortTermStartDate_Type())
cpqIoDrvExtnShortTermStartDate.setMaxAccess(_G)
if mibBuilder.loadTexts:cpqIoDrvExtnShortTermStartDate.setStatus(_E)
class _CpqIoDrvExtnShortTermWindow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_CpqIoDrvExtnShortTermWindow_Type.__name__=_D
_CpqIoDrvExtnShortTermWindow_Object=MibTableColumn
cpqIoDrvExtnShortTermWindow=_CpqIoDrvExtnShortTermWindow_Object((1,3,6,1,4,1,232,172,2,2,1,1,19),_CpqIoDrvExtnShortTermWindow_Type())
cpqIoDrvExtnShortTermWindow.setMaxAccess(_G)
if mibBuilder.loadTexts:cpqIoDrvExtnShortTermWindow.setStatus(_E)
_CpqIoDrvExtnShortTermEndDate_Type=DisplayString
_CpqIoDrvExtnShortTermEndDate_Object=MibTableColumn
cpqIoDrvExtnShortTermEndDate=_CpqIoDrvExtnShortTermEndDate_Object((1,3,6,1,4,1,232,172,2,2,1,1,20),_CpqIoDrvExtnShortTermEndDate_Type())
cpqIoDrvExtnShortTermEndDate.setMaxAccess(_G)
if mibBuilder.loadTexts:cpqIoDrvExtnShortTermEndDate.setStatus(_E)
_CpqIoDrvExtnShortTermEndDateFloat_Type=Integer32
_CpqIoDrvExtnShortTermEndDateFloat_Object=MibTableColumn
cpqIoDrvExtnShortTermEndDateFloat=_CpqIoDrvExtnShortTermEndDateFloat_Object((1,3,6,1,4,1,232,172,2,2,1,1,21),_CpqIoDrvExtnShortTermEndDateFloat_Type())
cpqIoDrvExtnShortTermEndDateFloat.setMaxAccess(_G)
if mibBuilder.loadTexts:cpqIoDrvExtnShortTermEndDateFloat.setStatus(_E)
_CpqIoDrvExtnLongTermStartDate_Type=DisplayString
_CpqIoDrvExtnLongTermStartDate_Object=MibTableColumn
cpqIoDrvExtnLongTermStartDate=_CpqIoDrvExtnLongTermStartDate_Object((1,3,6,1,4,1,232,172,2,2,1,1,22),_CpqIoDrvExtnLongTermStartDate_Type())
cpqIoDrvExtnLongTermStartDate.setMaxAccess(_G)
if mibBuilder.loadTexts:cpqIoDrvExtnLongTermStartDate.setStatus(_E)
class _CpqIoDrvExtnLongTermWindow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_CpqIoDrvExtnLongTermWindow_Type.__name__=_D
_CpqIoDrvExtnLongTermWindow_Object=MibTableColumn
cpqIoDrvExtnLongTermWindow=_CpqIoDrvExtnLongTermWindow_Object((1,3,6,1,4,1,232,172,2,2,1,1,23),_CpqIoDrvExtnLongTermWindow_Type())
cpqIoDrvExtnLongTermWindow.setMaxAccess(_G)
if mibBuilder.loadTexts:cpqIoDrvExtnLongTermWindow.setStatus(_E)
_CpqIoDrvExtnLongTermEndDate_Type=DisplayString
_CpqIoDrvExtnLongTermEndDate_Object=MibTableColumn
cpqIoDrvExtnLongTermEndDate=_CpqIoDrvExtnLongTermEndDate_Object((1,3,6,1,4,1,232,172,2,2,1,1,24),_CpqIoDrvExtnLongTermEndDate_Type())
cpqIoDrvExtnLongTermEndDate.setMaxAccess(_G)
if mibBuilder.loadTexts:cpqIoDrvExtnLongTermEndDate.setStatus(_E)
_CpqIoDrvExtnLongTermEndDateFloat_Type=Integer32
_CpqIoDrvExtnLongTermEndDateFloat_Object=MibTableColumn
cpqIoDrvExtnLongTermEndDateFloat=_CpqIoDrvExtnLongTermEndDateFloat_Object((1,3,6,1,4,1,232,172,2,2,1,1,25),_CpqIoDrvExtnLongTermEndDateFloat_Type())
cpqIoDrvExtnLongTermEndDateFloat.setMaxAccess(_G)
if mibBuilder.loadTexts:cpqIoDrvExtnLongTermEndDateFloat.setStatus(_E)
_CpqIoDrvExtnWriteRateAutoCalc_Type=Integer32
_CpqIoDrvExtnWriteRateAutoCalc_Object=MibTableColumn
cpqIoDrvExtnWriteRateAutoCalc=_CpqIoDrvExtnWriteRateAutoCalc_Object((1,3,6,1,4,1,232,172,2,2,1,1,26),_CpqIoDrvExtnWriteRateAutoCalc_Type())
cpqIoDrvExtnWriteRateAutoCalc.setMaxAccess(_G)
if mibBuilder.loadTexts:cpqIoDrvExtnWriteRateAutoCalc.setStatus(_E)
_CpqIoDrvExtnShortTermAvgU_Type=Counter32
_CpqIoDrvExtnShortTermAvgU_Object=MibTableColumn
cpqIoDrvExtnShortTermAvgU=_CpqIoDrvExtnShortTermAvgU_Object((1,3,6,1,4,1,232,172,2,2,1,1,27),_CpqIoDrvExtnShortTermAvgU_Type())
cpqIoDrvExtnShortTermAvgU.setMaxAccess(_G)
if mibBuilder.loadTexts:cpqIoDrvExtnShortTermAvgU.setStatus(_E)
_CpqIoDrvExtnShortTermAvgL_Type=Counter32
_CpqIoDrvExtnShortTermAvgL_Object=MibTableColumn
cpqIoDrvExtnShortTermAvgL=_CpqIoDrvExtnShortTermAvgL_Object((1,3,6,1,4,1,232,172,2,2,1,1,28),_CpqIoDrvExtnShortTermAvgL_Type())
cpqIoDrvExtnShortTermAvgL.setMaxAccess(_G)
if mibBuilder.loadTexts:cpqIoDrvExtnShortTermAvgL.setStatus(_E)
_CpqIoDrvExtnLongTermAvgU_Type=Counter32
_CpqIoDrvExtnLongTermAvgU_Object=MibTableColumn
cpqIoDrvExtnLongTermAvgU=_CpqIoDrvExtnLongTermAvgU_Object((1,3,6,1,4,1,232,172,2,2,1,1,29),_CpqIoDrvExtnLongTermAvgU_Type())
cpqIoDrvExtnLongTermAvgU.setMaxAccess(_G)
if mibBuilder.loadTexts:cpqIoDrvExtnLongTermAvgU.setStatus(_E)
_CpqIoDrvExtnLongTermAvgL_Type=Counter32
_CpqIoDrvExtnLongTermAvgL_Object=MibTableColumn
cpqIoDrvExtnLongTermAvgL=_CpqIoDrvExtnLongTermAvgL_Object((1,3,6,1,4,1,232,172,2,2,1,1,30),_CpqIoDrvExtnLongTermAvgL_Type())
cpqIoDrvExtnLongTermAvgL.setMaxAccess(_G)
if mibBuilder.loadTexts:cpqIoDrvExtnLongTermAvgL.setStatus(_E)
class _CpqIoDrvExtnConfidenceInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CpqIoDrvExtnConfidenceInterval_Type.__name__=_D
_CpqIoDrvExtnConfidenceInterval_Object=MibTableColumn
cpqIoDrvExtnConfidenceInterval=_CpqIoDrvExtnConfidenceInterval_Object((1,3,6,1,4,1,232,172,2,2,1,1,31),_CpqIoDrvExtnConfidenceInterval_Type())
cpqIoDrvExtnConfidenceInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:cpqIoDrvExtnConfidenceInterval.setStatus(_E)
class _CpqIoDrvExtnFormattedBlockSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,4096))
_CpqIoDrvExtnFormattedBlockSize_Type.__name__=_D
_CpqIoDrvExtnFormattedBlockSize_Object=MibTableColumn
cpqIoDrvExtnFormattedBlockSize=_CpqIoDrvExtnFormattedBlockSize_Object((1,3,6,1,4,1,232,172,2,2,1,1,32),_CpqIoDrvExtnFormattedBlockSize_Type())
cpqIoDrvExtnFormattedBlockSize.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvExtnFormattedBlockSize.setStatus(_B)
_CpqIoDrvExtnCurrentRAMUsageU_Type=Counter32
_CpqIoDrvExtnCurrentRAMUsageU_Object=MibTableColumn
cpqIoDrvExtnCurrentRAMUsageU=_CpqIoDrvExtnCurrentRAMUsageU_Object((1,3,6,1,4,1,232,172,2,2,1,1,33),_CpqIoDrvExtnCurrentRAMUsageU_Type())
cpqIoDrvExtnCurrentRAMUsageU.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvExtnCurrentRAMUsageU.setStatus(_B)
_CpqIoDrvExtnCurrentRAMUsageL_Type=Counter32
_CpqIoDrvExtnCurrentRAMUsageL_Object=MibTableColumn
cpqIoDrvExtnCurrentRAMUsageL=_CpqIoDrvExtnCurrentRAMUsageL_Object((1,3,6,1,4,1,232,172,2,2,1,1,34),_CpqIoDrvExtnCurrentRAMUsageL_Type())
cpqIoDrvExtnCurrentRAMUsageL.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvExtnCurrentRAMUsageL.setStatus(_B)
_CpqIoDrvExtnPeakRAMUsageU_Type=Counter32
_CpqIoDrvExtnPeakRAMUsageU_Object=MibTableColumn
cpqIoDrvExtnPeakRAMUsageU=_CpqIoDrvExtnPeakRAMUsageU_Object((1,3,6,1,4,1,232,172,2,2,1,1,35),_CpqIoDrvExtnPeakRAMUsageU_Type())
cpqIoDrvExtnPeakRAMUsageU.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvExtnPeakRAMUsageU.setStatus(_B)
_CpqIoDrvExtnPeakRAMUsageL_Type=Counter32
_CpqIoDrvExtnPeakRAMUsageL_Object=MibTableColumn
cpqIoDrvExtnPeakRAMUsageL=_CpqIoDrvExtnPeakRAMUsageL_Object((1,3,6,1,4,1,232,172,2,2,1,1,36),_CpqIoDrvExtnPeakRAMUsageL_Type())
cpqIoDrvExtnPeakRAMUsageL.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvExtnPeakRAMUsageL.setStatus(_B)
_CpqIoDrvCapacity_ObjectIdentity=ObjectIdentity
cpqIoDrvCapacity=_CpqIoDrvCapacity_ObjectIdentity((1,3,6,1,4,1,232,172,2,3))
_CpqIoDrvCapacityTable_Object=MibTable
cpqIoDrvCapacityTable=_CpqIoDrvCapacityTable_Object((1,3,6,1,4,1,232,172,2,3,1))
if mibBuilder.loadTexts:cpqIoDrvCapacityTable.setStatus(_B)
_CpqIoDrvCapacityEntry_Object=MibTableRow
cpqIoDrvCapacityEntry=_CpqIoDrvCapacityEntry_Object((1,3,6,1,4,1,232,172,2,3,1,1))
cpqIoDrvCapacityEntry.setIndexNames((0,_C,_h),(0,_C,_i))
if mibBuilder.loadTexts:cpqIoDrvCapacityEntry.setStatus(_B)
class _CpqIoDrvCapacityInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_CpqIoDrvCapacityInfoIndex_Type.__name__=_D
_CpqIoDrvCapacityInfoIndex_Object=MibTableColumn
cpqIoDrvCapacityInfoIndex=_CpqIoDrvCapacityInfoIndex_Object((1,3,6,1,4,1,232,172,2,3,1,1,1),_CpqIoDrvCapacityInfoIndex_Type())
cpqIoDrvCapacityInfoIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvCapacityInfoIndex.setStatus(_B)
class _CpqIoDrvCapacityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CpqIoDrvCapacityIndex_Type.__name__=_D
_CpqIoDrvCapacityIndex_Object=MibTableColumn
cpqIoDrvCapacityIndex=_CpqIoDrvCapacityIndex_Object((1,3,6,1,4,1,232,172,2,3,1,1,2),_CpqIoDrvCapacityIndex_Type())
cpqIoDrvCapacityIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvCapacityIndex.setStatus(_R)
_CpqIoDrvCapacityValueU_Type=Counter32
_CpqIoDrvCapacityValueU_Object=MibTableColumn
cpqIoDrvCapacityValueU=_CpqIoDrvCapacityValueU_Object((1,3,6,1,4,1,232,172,2,3,1,1,3),_CpqIoDrvCapacityValueU_Type())
cpqIoDrvCapacityValueU.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvCapacityValueU.setStatus(_B)
_CpqIoDrvCapacityValueL_Type=Counter32
_CpqIoDrvCapacityValueL_Object=MibTableColumn
cpqIoDrvCapacityValueL=_CpqIoDrvCapacityValueL_Object((1,3,6,1,4,1,232,172,2,3,1,1,4),_CpqIoDrvCapacityValueL_Type())
cpqIoDrvCapacityValueL.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvCapacityValueL.setStatus(_B)
_CpqIoDrvCapacityTimestamp_Type=DisplayString
_CpqIoDrvCapacityTimestamp_Object=MibTableColumn
cpqIoDrvCapacityTimestamp=_CpqIoDrvCapacityTimestamp_Object((1,3,6,1,4,1,232,172,2,3,1,1,5),_CpqIoDrvCapacityTimestamp_Type())
cpqIoDrvCapacityTimestamp.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvCapacityTimestamp.setStatus(_B)
_CpqIoDrvWrite_ObjectIdentity=ObjectIdentity
cpqIoDrvWrite=_CpqIoDrvWrite_ObjectIdentity((1,3,6,1,4,1,232,172,2,4))
_CpqIoDrvWriteTable_Object=MibTable
cpqIoDrvWriteTable=_CpqIoDrvWriteTable_Object((1,3,6,1,4,1,232,172,2,4,1))
if mibBuilder.loadTexts:cpqIoDrvWriteTable.setStatus(_R)
_CpqIoDrvWriteEntry_Object=MibTableRow
cpqIoDrvWriteEntry=_CpqIoDrvWriteEntry_Object((1,3,6,1,4,1,232,172,2,4,1,1))
cpqIoDrvWriteEntry.setIndexNames((0,_C,_j),(0,_C,_k))
if mibBuilder.loadTexts:cpqIoDrvWriteEntry.setStatus(_R)
class _CpqIoDrvWriteInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_CpqIoDrvWriteInfoIndex_Type.__name__=_D
_CpqIoDrvWriteInfoIndex_Object=MibTableColumn
cpqIoDrvWriteInfoIndex=_CpqIoDrvWriteInfoIndex_Object((1,3,6,1,4,1,232,172,2,4,1,1,1),_CpqIoDrvWriteInfoIndex_Type())
cpqIoDrvWriteInfoIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvWriteInfoIndex.setStatus(_B)
class _CpqIoDrvWriteIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CpqIoDrvWriteIndex_Type.__name__=_D
_CpqIoDrvWriteIndex_Object=MibTableColumn
cpqIoDrvWriteIndex=_CpqIoDrvWriteIndex_Object((1,3,6,1,4,1,232,172,2,4,1,1,2),_CpqIoDrvWriteIndex_Type())
cpqIoDrvWriteIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvWriteIndex.setStatus(_R)
_CpqIoDrvWriteValueU_Type=Counter32
_CpqIoDrvWriteValueU_Object=MibTableColumn
cpqIoDrvWriteValueU=_CpqIoDrvWriteValueU_Object((1,3,6,1,4,1,232,172,2,4,1,1,3),_CpqIoDrvWriteValueU_Type())
cpqIoDrvWriteValueU.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvWriteValueU.setStatus(_B)
_CpqIoDrvWriteValueL_Type=Counter32
_CpqIoDrvWriteValueL_Object=MibTableColumn
cpqIoDrvWriteValueL=_CpqIoDrvWriteValueL_Object((1,3,6,1,4,1,232,172,2,4,1,1,4),_CpqIoDrvWriteValueL_Type())
cpqIoDrvWriteValueL.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvWriteValueL.setStatus(_B)
_CpqIoDrvWriteTimestamp_Type=DisplayString
_CpqIoDrvWriteTimestamp_Object=MibTableColumn
cpqIoDrvWriteTimestamp=_CpqIoDrvWriteTimestamp_Object((1,3,6,1,4,1,232,172,2,4,1,1,5),_CpqIoDrvWriteTimestamp_Type())
cpqIoDrvWriteTimestamp.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvWriteTimestamp.setStatus(_B)
_CpqIoDrvTemp_ObjectIdentity=ObjectIdentity
cpqIoDrvTemp=_CpqIoDrvTemp_ObjectIdentity((1,3,6,1,4,1,232,172,2,5))
_CpqIoDrvTempTable_Object=MibTable
cpqIoDrvTempTable=_CpqIoDrvTempTable_Object((1,3,6,1,4,1,232,172,2,5,1))
if mibBuilder.loadTexts:cpqIoDrvTempTable.setStatus(_R)
_CpqIoDrvTempEntry_Object=MibTableRow
cpqIoDrvTempEntry=_CpqIoDrvTempEntry_Object((1,3,6,1,4,1,232,172,2,5,1,1))
cpqIoDrvTempEntry.setIndexNames((0,_C,_l),(0,_C,_m))
if mibBuilder.loadTexts:cpqIoDrvTempEntry.setStatus(_R)
class _CpqIoDrvTempInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_CpqIoDrvTempInfoIndex_Type.__name__=_D
_CpqIoDrvTempInfoIndex_Object=MibTableColumn
cpqIoDrvTempInfoIndex=_CpqIoDrvTempInfoIndex_Object((1,3,6,1,4,1,232,172,2,5,1,1,1),_CpqIoDrvTempInfoIndex_Type())
cpqIoDrvTempInfoIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvTempInfoIndex.setStatus(_B)
class _CpqIoDrvTempIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqIoDrvTempIndex_Type.__name__=_D
_CpqIoDrvTempIndex_Object=MibTableColumn
cpqIoDrvTempIndex=_CpqIoDrvTempIndex_Object((1,3,6,1,4,1,232,172,2,5,1,1,2),_CpqIoDrvTempIndex_Type())
cpqIoDrvTempIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvTempIndex.setStatus(_R)
class _CpqIoDrvTempValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_CpqIoDrvTempValue_Type.__name__=_D
_CpqIoDrvTempValue_Object=MibTableColumn
cpqIoDrvTempValue=_CpqIoDrvTempValue_Object((1,3,6,1,4,1,232,172,2,5,1,1,3),_CpqIoDrvTempValue_Type())
cpqIoDrvTempValue.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvTempValue.setStatus(_B)
_CpqIoDrvTempTimestamp_Type=Counter32
_CpqIoDrvTempTimestamp_Object=MibTableColumn
cpqIoDrvTempTimestamp=_CpqIoDrvTempTimestamp_Object((1,3,6,1,4,1,232,172,2,5,1,1,4),_CpqIoDrvTempTimestamp_Type())
cpqIoDrvTempTimestamp.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvTempTimestamp.setStatus(_B)
_CpqIoDrvProc_ObjectIdentity=ObjectIdentity
cpqIoDrvProc=_CpqIoDrvProc_ObjectIdentity((1,3,6,1,4,1,232,172,2,6))
_CpqIoDrvProcTable_Object=MibTable
cpqIoDrvProcTable=_CpqIoDrvProcTable_Object((1,3,6,1,4,1,232,172,2,6,1))
if mibBuilder.loadTexts:cpqIoDrvProcTable.setStatus(_E)
_CpqIoDrvProcEntry_Object=MibTableRow
cpqIoDrvProcEntry=_CpqIoDrvProcEntry_Object((1,3,6,1,4,1,232,172,2,6,1,1))
cpqIoDrvProcEntry.setIndexNames((0,_C,_n))
if mibBuilder.loadTexts:cpqIoDrvProcEntry.setStatus(_E)
class _CpqIoDrvProcIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_CpqIoDrvProcIndex_Type.__name__=_D
_CpqIoDrvProcIndex_Object=MibTableColumn
cpqIoDrvProcIndex=_CpqIoDrvProcIndex_Object((1,3,6,1,4,1,232,172,2,6,1,1,1),_CpqIoDrvProcIndex_Type())
cpqIoDrvProcIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvProcIndex.setStatus(_E)
class _CpqIoDrvProcName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_CpqIoDrvProcName_Type.__name__=_F
_CpqIoDrvProcName_Object=MibTableColumn
cpqIoDrvProcName=_CpqIoDrvProcName_Object((1,3,6,1,4,1,232,172,2,6,1,1,2),_CpqIoDrvProcName_Type())
cpqIoDrvProcName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvProcName.setStatus(_E)
class _CpqIoDrvProcState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_CpqIoDrvProcState_Type.__name__=_F
_CpqIoDrvProcState_Object=MibTableColumn
cpqIoDrvProcState=_CpqIoDrvProcState_Object((1,3,6,1,4,1,232,172,2,6,1,1,3),_CpqIoDrvProcState_Type())
cpqIoDrvProcState.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvProcState.setStatus(_E)
_CpqIoDrvProcRAM_Type=Counter32
_CpqIoDrvProcRAM_Object=MibTableColumn
cpqIoDrvProcRAM=_CpqIoDrvProcRAM_Object((1,3,6,1,4,1,232,172,2,6,1,1,4),_CpqIoDrvProcRAM_Type())
cpqIoDrvProcRAM.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvProcRAM.setStatus(_E)
class _CpqIoDrvProcCPU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CpqIoDrvProcCPU_Type.__name__=_D
_CpqIoDrvProcCPU_Object=MibTableColumn
cpqIoDrvProcCPU=_CpqIoDrvProcCPU_Object((1,3,6,1,4,1,232,172,2,6,1,1,5),_CpqIoDrvProcCPU_Type())
cpqIoDrvProcCPU.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqIoDrvProcCPU.setStatus(_E)
cpqIoDrvWearoutTrap=NotificationType((1,3,6,1,4,1,232,0,172001))
cpqIoDrvWearoutTrap.setObjects(*((_K,_L),(_I,_J),(_C,_o),(_C,_H),(_C,_M),(_C,_N),(_C,_O),(_C,_P),(_C,_Q)))
if mibBuilder.loadTexts:cpqIoDrvWearoutTrap.setStatus('')
cpqIoDrvNonWritableTrap=NotificationType((1,3,6,1,4,1,232,0,172002))
cpqIoDrvNonWritableTrap.setObjects(*((_K,_L),(_I,_J),(_C,_p),(_C,_H),(_C,_M),(_C,_N),(_C,_O),(_C,_P),(_C,_Q)))
if mibBuilder.loadTexts:cpqIoDrvNonWritableTrap.setStatus('')
cpqIoDrvFlashbackTrap=NotificationType((1,3,6,1,4,1,232,0,172003))
cpqIoDrvFlashbackTrap.setObjects(*((_K,_L),(_I,_J),(_C,_q),(_C,_H),(_C,_M),(_C,_N),(_C,_O),(_C,_P),(_C,_Q)))
if mibBuilder.loadTexts:cpqIoDrvFlashbackTrap.setStatus('')
cpqIoDrvTempHighTrap=NotificationType((1,3,6,1,4,1,232,0,172004))
cpqIoDrvTempHighTrap.setObjects(*((_K,_L),(_I,_J),(_C,_Y),(_C,_H),(_C,_M),(_C,_N),(_C,_O),(_C,_P),(_C,_Q)))
if mibBuilder.loadTexts:cpqIoDrvTempHighTrap.setStatus('')
cpqIoDrvTempOkTrap=NotificationType((1,3,6,1,4,1,232,0,172005))
cpqIoDrvTempOkTrap.setObjects(*((_K,_L),(_I,_J),(_C,_Y),(_C,_H),(_C,_M),(_C,_N),(_C,_O),(_C,_P),(_C,_Q)))
if mibBuilder.loadTexts:cpqIoDrvTempOkTrap.setStatus('')
cpqIoDrvErrorTrap=NotificationType((1,3,6,1,4,1,232,0,172006))
cpqIoDrvErrorTrap.setObjects(*((_K,_L),(_I,_J),(_C,_r),(_C,_H),(_C,_M),(_C,_N),(_C,_O),(_C,_P),(_C,_Q)))
if mibBuilder.loadTexts:cpqIoDrvErrorTrap.setStatus('')
cpqIoDrvPowerlossProtectTrap=NotificationType((1,3,6,1,4,1,232,0,172007))
cpqIoDrvPowerlossProtectTrap.setObjects(*((_K,_L),(_I,_J),(_C,_s),(_C,_H),(_C,_M),(_C,_N),(_C,_O),(_C,_P),(_C,_Q)))
if mibBuilder.loadTexts:cpqIoDrvPowerlossProtectTrap.setStatus('')
mibBuilder.exportSymbols(_C,**{'cpqIoDrvWearoutTrap':cpqIoDrvWearoutTrap,'cpqIoDrvNonWritableTrap':cpqIoDrvNonWritableTrap,'cpqIoDrvFlashbackTrap':cpqIoDrvFlashbackTrap,'cpqIoDrvTempHighTrap':cpqIoDrvTempHighTrap,'cpqIoDrvTempOkTrap':cpqIoDrvTempOkTrap,'cpqIoDrvErrorTrap':cpqIoDrvErrorTrap,'cpqIoDrvPowerlossProtectTrap':cpqIoDrvPowerlossProtectTrap,'cpqIoDrv':cpqIoDrv,'cpqIoDrvMibRev':cpqIoDrvMibRev,'cpqIoDrvMibRevMajor':cpqIoDrvMibRevMajor,'cpqIoDrvMibRevMinor':cpqIoDrvMibRevMinor,'cpqIoDrvMibCondition':cpqIoDrvMibCondition,'cpqIoDrvComponent':cpqIoDrvComponent,'cpqIoDrvInfo':cpqIoDrvInfo,'cpqIoDrvInfoTable':cpqIoDrvInfoTable,'cpqIoDrvInfoEntry':cpqIoDrvInfoEntry,_H:cpqIoDrvInfoIndex,'cpqIoDrvInfoStatus':cpqIoDrvInfoStatus,_M:cpqIoDrvInfoName,_P:cpqIoDrvInfoSerialNumber,'cpqIoDrvInfoPartNumber':cpqIoDrvInfoPartNumber,'cpqIoDrvInfoSubVendorPartNumber':cpqIoDrvInfoSubVendorPartNumber,_O:cpqIoDrvInfoSparesPartNumber,'cpqIoDrvInfoAssemblyNumber':cpqIoDrvInfoAssemblyNumber,_N:cpqIoDrvInfoFirmwareVersion,'cpqIoDrvInfoDriverVersion':cpqIoDrvInfoDriverVersion,'cpqIoDrvInfoUID':cpqIoDrvInfoUID,_r:cpqIoDrvInfoState,'cpqIoDrvInfoClientDeviceName':cpqIoDrvInfoClientDeviceName,'cpqIoDrvInfoBeacon':cpqIoDrvInfoBeacon,'cpqIoDrvInfoPCIAddress':cpqIoDrvInfoPCIAddress,'cpqIoDrvInfoPCIDeviceID':cpqIoDrvInfoPCIDeviceID,'cpqIoDrvInfoPCISubdeviceID':cpqIoDrvInfoPCISubdeviceID,'cpqIoDrvInfoPCIVendorID':cpqIoDrvInfoPCIVendorID,'cpqIoDrvInfoPCISubvendorID':cpqIoDrvInfoPCISubvendorID,_Q:cpqIoDrvInfoPCISlot,_o:cpqIoDrvInfoWearoutIndicator,_q:cpqIoDrvInfoFlashbackIndicator,_p:cpqIoDrvInfoNonWritableIndicator,_Y:cpqIoDrvInfoCurrentTemp,'cpqIoDrvInfoPercentLifeRemaining':cpqIoDrvInfoPercentLifeRemaining,'cpqIoDrvInfoShortTermWearoutDate':cpqIoDrvInfoShortTermWearoutDate,'cpqIoDrvInfoLongTermWearoutDate':cpqIoDrvInfoLongTermWearoutDate,'cpqIoDrvInfoShortTermNonWritableDate':cpqIoDrvInfoShortTermNonWritableDate,'cpqIoDrvInfoLongTermNonWritableDate':cpqIoDrvInfoLongTermNonWritableDate,'cpqIoDrvInfoMinimalModeReason':cpqIoDrvInfoMinimalModeReason,'cpqIoDrvInfoReducedWriteReason':cpqIoDrvInfoReducedWriteReason,'cpqIoDrvInfoMilliVolts':cpqIoDrvInfoMilliVolts,'cpqIoDrvInfoMilliVoltsPeak':cpqIoDrvInfoMilliVoltsPeak,'cpqIoDrvInfoMilliVoltsMin':cpqIoDrvInfoMilliVoltsMin,'cpqIoDrvInfoMilliWatts':cpqIoDrvInfoMilliWatts,'cpqIoDrvInfoMilliWattsPeak':cpqIoDrvInfoMilliWattsPeak,'cpqIoDrvInfoMilliAmps':cpqIoDrvInfoMilliAmps,'cpqIoDrvInfoMilliAmpsPeak':cpqIoDrvInfoMilliAmpsPeak,'cpqIoDrvInfoAdapterType':cpqIoDrvInfoAdapterType,'cpqIoDrvInfoAdapterPort':cpqIoDrvInfoAdapterPort,'cpqIoDrvInfoAdapterSerialNumber':cpqIoDrvInfoAdapterSerialNumber,'cpqIoDrvInfoAdapterExtPowerPresent':cpqIoDrvInfoAdapterExtPowerPresent,_s:cpqIoDrvInfoPowerlossProtectDisabled,'cpqIoDrvInfoInternalTempHigh':cpqIoDrvInfoInternalTempHigh,'cpqIoDrvInfoAmbientTemp':cpqIoDrvInfoAmbientTemp,'cpqIoDrvInfoPCIBandwidthCompatibility':cpqIoDrvInfoPCIBandwidthCompatibility,'cpqIoDrvInfoPCIPowerCompatibility':cpqIoDrvInfoPCIPowerCompatibility,'cpqIoDrvInfoActualGoverningLevel':cpqIoDrvInfoActualGoverningLevel,'cpqIoDrvInfoLifespanGoverningLevel':cpqIoDrvInfoLifespanGoverningLevel,'cpqIoDrvInfoPowerGoverningLevel':cpqIoDrvInfoPowerGoverningLevel,'cpqIoDrvInfoThermalGoverningLevel':cpqIoDrvInfoThermalGoverningLevel,'cpqIoDrvInfoLifespanGoverningEnabled':cpqIoDrvInfoLifespanGoverningEnabled,'cpqIoDrvInfoLifespanGoverningTgtDate':cpqIoDrvInfoLifespanGoverningTgtDate,'cpqIoDrvExtn':cpqIoDrvExtn,'cpqIoDrvExtnTable':cpqIoDrvExtnTable,'cpqIoDrvExtnEntry':cpqIoDrvExtnEntry,_g:cpqIoDrvExtnIndex,'cpqIoDrvExtnTotalPhysicalCapacityU':cpqIoDrvExtnTotalPhysicalCapacityU,'cpqIoDrvExtnTotalPhysicalCapacityL':cpqIoDrvExtnTotalPhysicalCapacityL,'cpqIoDrvExtnUsablePhysicalCapacityU':cpqIoDrvExtnUsablePhysicalCapacityU,'cpqIoDrvExtnUsablePhysicalCapacityL':cpqIoDrvExtnUsablePhysicalCapacityL,'cpqIoDrvExtnUsedPhysicalCapacityU':cpqIoDrvExtnUsedPhysicalCapacityU,'cpqIoDrvExtnUsedPhysicalCapacityL':cpqIoDrvExtnUsedPhysicalCapacityL,'cpqIoDrvExtnTotalLogicalCapacityU':cpqIoDrvExtnTotalLogicalCapacityU,'cpqIoDrvExtnTotalLogicalCapacityL':cpqIoDrvExtnTotalLogicalCapacityL,'cpqIoDrvExtnAvailableLogicalCapacityU':cpqIoDrvExtnAvailableLogicalCapacityU,'cpqIoDrvExtnAvailableLogicalCapacityL':cpqIoDrvExtnAvailableLogicalCapacityL,'cpqIoDrvExtnBytesReadU':cpqIoDrvExtnBytesReadU,'cpqIoDrvExtnBytesReadL':cpqIoDrvExtnBytesReadL,'cpqIoDrvExtnPhysicalBytesWrittenU':cpqIoDrvExtnPhysicalBytesWrittenU,'cpqIoDrvExtnPhysicalBytesWrittenL':cpqIoDrvExtnPhysicalBytesWrittenL,'cpqIoDrvExtnLogicalBytesWrittenU':cpqIoDrvExtnLogicalBytesWrittenU,'cpqIoDrvExtnLogicalBytesWrittenL':cpqIoDrvExtnLogicalBytesWrittenL,'cpqIoDrvExtnShortTermStartDate':cpqIoDrvExtnShortTermStartDate,'cpqIoDrvExtnShortTermWindow':cpqIoDrvExtnShortTermWindow,'cpqIoDrvExtnShortTermEndDate':cpqIoDrvExtnShortTermEndDate,'cpqIoDrvExtnShortTermEndDateFloat':cpqIoDrvExtnShortTermEndDateFloat,'cpqIoDrvExtnLongTermStartDate':cpqIoDrvExtnLongTermStartDate,'cpqIoDrvExtnLongTermWindow':cpqIoDrvExtnLongTermWindow,'cpqIoDrvExtnLongTermEndDate':cpqIoDrvExtnLongTermEndDate,'cpqIoDrvExtnLongTermEndDateFloat':cpqIoDrvExtnLongTermEndDateFloat,'cpqIoDrvExtnWriteRateAutoCalc':cpqIoDrvExtnWriteRateAutoCalc,'cpqIoDrvExtnShortTermAvgU':cpqIoDrvExtnShortTermAvgU,'cpqIoDrvExtnShortTermAvgL':cpqIoDrvExtnShortTermAvgL,'cpqIoDrvExtnLongTermAvgU':cpqIoDrvExtnLongTermAvgU,'cpqIoDrvExtnLongTermAvgL':cpqIoDrvExtnLongTermAvgL,'cpqIoDrvExtnConfidenceInterval':cpqIoDrvExtnConfidenceInterval,'cpqIoDrvExtnFormattedBlockSize':cpqIoDrvExtnFormattedBlockSize,'cpqIoDrvExtnCurrentRAMUsageU':cpqIoDrvExtnCurrentRAMUsageU,'cpqIoDrvExtnCurrentRAMUsageL':cpqIoDrvExtnCurrentRAMUsageL,'cpqIoDrvExtnPeakRAMUsageU':cpqIoDrvExtnPeakRAMUsageU,'cpqIoDrvExtnPeakRAMUsageL':cpqIoDrvExtnPeakRAMUsageL,'cpqIoDrvCapacity':cpqIoDrvCapacity,'cpqIoDrvCapacityTable':cpqIoDrvCapacityTable,'cpqIoDrvCapacityEntry':cpqIoDrvCapacityEntry,_h:cpqIoDrvCapacityInfoIndex,_i:cpqIoDrvCapacityIndex,'cpqIoDrvCapacityValueU':cpqIoDrvCapacityValueU,'cpqIoDrvCapacityValueL':cpqIoDrvCapacityValueL,'cpqIoDrvCapacityTimestamp':cpqIoDrvCapacityTimestamp,'cpqIoDrvWrite':cpqIoDrvWrite,'cpqIoDrvWriteTable':cpqIoDrvWriteTable,'cpqIoDrvWriteEntry':cpqIoDrvWriteEntry,_j:cpqIoDrvWriteInfoIndex,_k:cpqIoDrvWriteIndex,'cpqIoDrvWriteValueU':cpqIoDrvWriteValueU,'cpqIoDrvWriteValueL':cpqIoDrvWriteValueL,'cpqIoDrvWriteTimestamp':cpqIoDrvWriteTimestamp,'cpqIoDrvTemp':cpqIoDrvTemp,'cpqIoDrvTempTable':cpqIoDrvTempTable,'cpqIoDrvTempEntry':cpqIoDrvTempEntry,_l:cpqIoDrvTempInfoIndex,_m:cpqIoDrvTempIndex,'cpqIoDrvTempValue':cpqIoDrvTempValue,'cpqIoDrvTempTimestamp':cpqIoDrvTempTimestamp,'cpqIoDrvProc':cpqIoDrvProc,'cpqIoDrvProcTable':cpqIoDrvProcTable,'cpqIoDrvProcEntry':cpqIoDrvProcEntry,_n:cpqIoDrvProcIndex,'cpqIoDrvProcName':cpqIoDrvProcName,'cpqIoDrvProcState':cpqIoDrvProcState,'cpqIoDrvProcRAM':cpqIoDrvProcRAM,'cpqIoDrvProcCPU':cpqIoDrvProcCPU})