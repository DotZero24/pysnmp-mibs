_A7='kcprtSubUnitIndex'
_A6='kcprtTrayJobIndex'
_A5='kcprtMediaIndex'
_A4='kcprtSJobIndex'
_A3='kcprtSJobStorageIndex'
_A2='kcprtFileIndex'
_A1='kcprtFileStorageIndex'
_A0='kcprtFontDataIndex'
_z='kcprtMessageDataIndex'
_y='kcprtProgramDataIndex'
_x='kcprtHostDataIndex'
_w='prescribe'
_v='kcprtMacroDataIndex'
_u='kcprtPartitionIndex'
_t='kcprtMemoryDeviceIndex'
_s='kcprtAlertEventCountIndex'
_r='kcprtAlertChangeLogIndex'
_q='kcprtAlertCallLogIndex'
_p='kcprtAlertJamLogIndex'
_o='kcprtAlertStateDisplayIndex'
_n='kcprtAlertIndex'
_m='kcprtBuzzerIndex'
_l='kcprtChannelIndex'
_k='medium'
_j='offOrNotSupport'
_i='kcprtPunchGroupIndex'
_h='kcprtOutputTrayIndex'
_g='kcprtTrayGroupIndex'
_f='kcprtInputGroupIndex'
_e='kcprtInputIndex'
_d='disabled'
_c='kcprtCpuIndex'
_b='enable'
_a='disable'
_Z='prtMarkerIndex'
_Y='Printer-MIB'
_X='kcprtMailBoxTrayIndex'
_W='light'
_V='none'
_U='enabled'
_T='kcprtMailBoxIndex'
_S='unknown'
_R='kcprtOutputIndex'
_Q='normal'
_P='registered'
_O='notRegistered'
_N='others'
_M='on'
_L='optional'
_K='OctetString'
_J='off'
_I='not-accessible'
_H='DisplayString'
_G='hrDeviceIndex'
_F='HOST-RESOURCES-MIB'
_E='KYOCERA-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hrDeviceIndex,=mibBuilder.importSymbols(_F,_G)
PresentOnOff,prtMarkerIndex=mibBuilder.importSymbols(_Y,'PresentOnOff',_Z)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
_Kyocera_ObjectIdentity=ObjectIdentity
kyocera=_Kyocera_ObjectIdentity((1,3,6,1,4,1,1347))
_KcPrinter_ObjectIdentity=ObjectIdentity
kcPrinter=_KcPrinter_ObjectIdentity((1,3,6,1,4,1,1347,43))
_KcprtGeneral_ObjectIdentity=ObjectIdentity
kcprtGeneral=_KcprtGeneral_ObjectIdentity((1,3,6,1,4,1,1347,43,5))
_KcprtGeneralTable_Object=MibTable
kcprtGeneralTable=_KcprtGeneralTable_Object((1,3,6,1,4,1,1347,43,5,1))
if mibBuilder.loadTexts:kcprtGeneralTable.setStatus(_A)
_KcprtGeneralEntry_Object=MibTableRow
kcprtGeneralEntry=_KcprtGeneralEntry_Object((1,3,6,1,4,1,1347,43,5,1,1))
kcprtGeneralEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:kcprtGeneralEntry.setStatus(_A)
class _KcprtGeneralModelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_KcprtGeneralModelName_Type.__name__=_H
_KcprtGeneralModelName_Object=MibTableColumn
kcprtGeneralModelName=_KcprtGeneralModelName_Object((1,3,6,1,4,1,1347,43,5,1,1,1),_KcprtGeneralModelName_Type())
kcprtGeneralModelName.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtGeneralModelName.setStatus(_A)
class _KcprtOptionVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_KcprtOptionVersion_Type.__name__=_H
_KcprtOptionVersion_Object=MibTableColumn
kcprtOptionVersion=_KcprtOptionVersion_Object((1,3,6,1,4,1,1347,43,5,1,1,2),_KcprtOptionVersion_Type())
kcprtOptionVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtOptionVersion.setStatus(_A)
class _KcprtKpdlLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_KcprtKpdlLevel_Type.__name__=_C
_KcprtKpdlLevel_Object=MibTableColumn
kcprtKpdlLevel=_KcprtKpdlLevel_Object((1,3,6,1,4,1,1347,43,5,1,1,3),_KcprtKpdlLevel_Type())
kcprtKpdlLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtKpdlLevel.setStatus(_A)
class _KcprtSystemUpTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtSystemUpTime_Type.__name__=_C
_KcprtSystemUpTime_Object=MibTableColumn
kcprtSystemUpTime=_KcprtSystemUpTime_Object((1,3,6,1,4,1,1347,43,5,1,1,4),_KcprtSystemUpTime_Type())
kcprtSystemUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSystemUpTime.setStatus(_A)
class _KcprtBinNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_KcprtBinNumber_Type.__name__=_C
_KcprtBinNumber_Object=MibTableColumn
kcprtBinNumber=_KcprtBinNumber_Object((1,3,6,1,4,1,1347,43,5,1,1,5),_KcprtBinNumber_Type())
kcprtBinNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtBinNumber.setStatus(_A)
class _KcprtCardSlotCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_KcprtCardSlotCapacity_Type.__name__=_C
_KcprtCardSlotCapacity_Object=MibTableColumn
kcprtCardSlotCapacity=_KcprtCardSlotCapacity_Object((1,3,6,1,4,1,1347,43,5,1,1,6),_KcprtCardSlotCapacity_Type())
kcprtCardSlotCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtCardSlotCapacity.setStatus(_A)
class _KcprtRomSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_KcprtRomSlotNumber_Type.__name__=_C
_KcprtRomSlotNumber_Object=MibTableColumn
kcprtRomSlotNumber=_KcprtRomSlotNumber_Object((1,3,6,1,4,1,1347,43,5,1,1,7),_KcprtRomSlotNumber_Type())
kcprtRomSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtRomSlotNumber.setStatus(_A)
class _KcprtSimmSlotCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_KcprtSimmSlotCapacity_Type.__name__=_C
_KcprtSimmSlotCapacity_Object=MibTableColumn
kcprtSimmSlotCapacity=_KcprtSimmSlotCapacity_Object((1,3,6,1,4,1,1347,43,5,1,1,8),_KcprtSimmSlotCapacity_Type())
kcprtSimmSlotCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSimmSlotCapacity.setStatus(_A)
class _KcprtSimmSlotUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_KcprtSimmSlotUsed_Type.__name__=_C
_KcprtSimmSlotUsed_Object=MibTableColumn
kcprtSimmSlotUsed=_KcprtSimmSlotUsed_Object((1,3,6,1,4,1,1347,43,5,1,1,9),_KcprtSimmSlotUsed_Type())
kcprtSimmSlotUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSimmSlotUsed.setStatus(_A)
class _KcprtOriginalMemorySize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtOriginalMemorySize_Type.__name__=_C
_KcprtOriginalMemorySize_Object=MibTableColumn
kcprtOriginalMemorySize=_KcprtOriginalMemorySize_Object((1,3,6,1,4,1,1347,43,5,1,1,10),_KcprtOriginalMemorySize_Type())
kcprtOriginalMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtOriginalMemorySize.setStatus(_A)
class _KcprtTotalMemorySize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtTotalMemorySize_Type.__name__=_C
_KcprtTotalMemorySize_Object=MibTableColumn
kcprtTotalMemorySize=_KcprtTotalMemorySize_Object((1,3,6,1,4,1,1347,43,5,1,1,11),_KcprtTotalMemorySize_Type())
kcprtTotalMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtTotalMemorySize.setStatus(_A)
class _KcprtUserMemorySize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtUserMemorySize_Type.__name__=_C
_KcprtUserMemorySize_Object=MibTableColumn
kcprtUserMemorySize=_KcprtUserMemorySize_Object((1,3,6,1,4,1,1347,43,5,1,1,12),_KcprtUserMemorySize_Type())
kcprtUserMemorySize.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtUserMemorySize.setStatus(_A)
class _KcprtVirtualMemory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notSupported',0),('support',1)))
_KcprtVirtualMemory_Type.__name__=_C
_KcprtVirtualMemory_Object=MibTableColumn
kcprtVirtualMemory=_KcprtVirtualMemory_Object((1,3,6,1,4,1,1347,43,5,1,1,13),_KcprtVirtualMemory_Type())
kcprtVirtualMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtVirtualMemory.setStatus(_A)
class _KcprtPageMemorySize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('mem128KB',1),('mem256KB',2),('mem512KB',3),('memA4orLetter',4),('memLegal',5),('memwLetter',6),('memwLegal',7)))
_KcprtPageMemorySize_Type.__name__=_C
_KcprtPageMemorySize_Object=MibTableColumn
kcprtPageMemorySize=_KcprtPageMemorySize_Object((1,3,6,1,4,1,1347,43,5,1,1,14),_KcprtPageMemorySize_Type())
kcprtPageMemorySize.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtPageMemorySize.setStatus(_A)
class _KcprtHostBufferSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_KcprtHostBufferSize_Type.__name__=_C
_KcprtHostBufferSize_Object=MibTableColumn
kcprtHostBufferSize=_KcprtHostBufferSize_Object((1,3,6,1,4,1,1347,43,5,1,1,15),_KcprtHostBufferSize_Type())
kcprtHostBufferSize.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtHostBufferSize.setStatus(_A)
class _KcprtHostBuffer1stRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_KcprtHostBuffer1stRate_Type.__name__=_C
_KcprtHostBuffer1stRate_Object=MibTableColumn
kcprtHostBuffer1stRate=_KcprtHostBuffer1stRate_Object((1,3,6,1,4,1,1347,43,5,1,1,16),_KcprtHostBuffer1stRate_Type())
kcprtHostBuffer1stRate.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtHostBuffer1stRate.setStatus(_A)
class _KcprtHostBuffer2ndRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_KcprtHostBuffer2ndRate_Type.__name__=_C
_KcprtHostBuffer2ndRate_Object=MibTableColumn
kcprtHostBuffer2ndRate=_KcprtHostBuffer2ndRate_Object((1,3,6,1,4,1,1347,43,5,1,1,17),_KcprtHostBuffer2ndRate_Type())
kcprtHostBuffer2ndRate.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtHostBuffer2ndRate.setStatus(_A)
class _KcprtHostBuffer3rdRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_KcprtHostBuffer3rdRate_Type.__name__=_C
_KcprtHostBuffer3rdRate_Object=MibTableColumn
kcprtHostBuffer3rdRate=_KcprtHostBuffer3rdRate_Object((1,3,6,1,4,1,1347,43,5,1,1,18),_KcprtHostBuffer3rdRate_Type())
kcprtHostBuffer3rdRate.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtHostBuffer3rdRate.setStatus(_A)
class _KcprtHostBufferOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('automatic',0),('fixed',1)))
_KcprtHostBufferOption_Type.__name__=_C
_KcprtHostBufferOption_Object=MibTableColumn
kcprtHostBufferOption=_KcprtHostBufferOption_Object((1,3,6,1,4,1,1347,43,5,1,1,19),_KcprtHostBufferOption_Type())
kcprtHostBufferOption.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtHostBufferOption.setStatus(_A)
class _KcprtBufferXoffLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_KcprtBufferXoffLevel_Type.__name__=_C
_KcprtBufferXoffLevel_Object=MibTableColumn
kcprtBufferXoffLevel=_KcprtBufferXoffLevel_Object((1,3,6,1,4,1,1347,43,5,1,1,20),_KcprtBufferXoffLevel_Type())
kcprtBufferXoffLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtBufferXoffLevel.setStatus(_A)
class _KcprtBufferXonLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_KcprtBufferXonLevel_Type.__name__=_C
_KcprtBufferXonLevel_Object=MibTableColumn
kcprtBufferXonLevel=_KcprtBufferXonLevel_Object((1,3,6,1,4,1,1347,43,5,1,1,21),_KcprtBufferXonLevel_Type())
kcprtBufferXonLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtBufferXonLevel.setStatus(_A)
class _KcprtFFTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_KcprtFFTimeout_Type.__name__=_C
_KcprtFFTimeout_Object=MibTableColumn
kcprtFFTimeout=_KcprtFFTimeout_Object((1,3,6,1,4,1,1347,43,5,1,1,22),_KcprtFFTimeout_Type())
kcprtFFTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtFFTimeout.setStatus(_A)
class _KcprtSleepTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_KcprtSleepTimer_Type.__name__=_C
_KcprtSleepTimer_Object=MibTableColumn
kcprtSleepTimer=_KcprtSleepTimer_Object((1,3,6,1,4,1,1347,43,5,1,1,23),_KcprtSleepTimer_Type())
kcprtSleepTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtSleepTimer.setStatus(_A)
class _KcprtWakeupStatusPage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_a,0),(_b,1)))
_KcprtWakeupStatusPage_Type.__name__=_C
_KcprtWakeupStatusPage_Object=MibTableColumn
kcprtWakeupStatusPage=_KcprtWakeupStatusPage_Object((1,3,6,1,4,1,1347,43,5,1,1,24),_KcprtWakeupStatusPage_Type())
kcprtWakeupStatusPage.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtWakeupStatusPage.setStatus(_A)
class _KcprtOnlineControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('offLine',0),('onLine',1)))
_KcprtOnlineControl_Type.__name__=_C
_KcprtOnlineControl_Object=MibTableColumn
kcprtOnlineControl=_KcprtOnlineControl_Object((1,3,6,1,4,1,1347,43,5,1,1,25),_KcprtOnlineControl_Type())
kcprtOnlineControl.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtOnlineControl.setStatus(_A)
class _KcprtCopyCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_KcprtCopyCount_Type.__name__=_C
_KcprtCopyCount_Object=MibTableColumn
kcprtCopyCount=_KcprtCopyCount_Object((1,3,6,1,4,1,1347,43,5,1,1,26),_KcprtCopyCount_Type())
kcprtCopyCount.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtCopyCount.setStatus(_A)
class _KcprtContinueKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),('continue',1)))
_KcprtContinueKey_Type.__name__=_C
_KcprtContinueKey_Object=MibTableColumn
kcprtContinueKey=_KcprtContinueKey_Object((1,3,6,1,4,1,1347,43,5,1,1,27),_KcprtContinueKey_Type())
kcprtContinueKey.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtContinueKey.setStatus(_A)
class _KcprtSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_KcprtSerialNumber_Type.__name__=_H
_KcprtSerialNumber_Object=MibTableColumn
kcprtSerialNumber=_KcprtSerialNumber_Object((1,3,6,1,4,1,1347,43,5,1,1,28),_KcprtSerialNumber_Type())
kcprtSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSerialNumber.setStatus(_A)
class _KcprtAssetNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_KcprtAssetNumber_Type.__name__=_H
_KcprtAssetNumber_Object=MibTableColumn
kcprtAssetNumber=_KcprtAssetNumber_Object((1,3,6,1,4,1,1347,43,5,1,1,29),_KcprtAssetNumber_Type())
kcprtAssetNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtAssetNumber.setStatus(_A)
class _KcprtSignature_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_KcprtSignature_Type.__name__=_K
_KcprtSignature_Object=MibTableColumn
kcprtSignature=_KcprtSignature_Object((1,3,6,1,4,1,1347,43,5,1,1,30),_KcprtSignature_Type())
kcprtSignature.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtSignature.setStatus(_A)
class _KcprtFirmParamCurrentRegister_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_KcprtFirmParamCurrentRegister_Type.__name__=_K
_KcprtFirmParamCurrentRegister_Object=MibTableColumn
kcprtFirmParamCurrentRegister=_KcprtFirmParamCurrentRegister_Object((1,3,6,1,4,1,1347,43,5,1,1,31),_KcprtFirmParamCurrentRegister_Type())
kcprtFirmParamCurrentRegister.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtFirmParamCurrentRegister.setStatus(_A)
class _KcprtFirmParamCurrentValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_KcprtFirmParamCurrentValue_Type.__name__=_K
_KcprtFirmParamCurrentValue_Object=MibTableColumn
kcprtFirmParamCurrentValue=_KcprtFirmParamCurrentValue_Object((1,3,6,1,4,1,1347,43,5,1,1,32),_KcprtFirmParamCurrentValue_Type())
kcprtFirmParamCurrentValue.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtFirmParamCurrentValue.setStatus(_A)
class _KcprtSleepMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_M,1)))
_KcprtSleepMode_Type.__name__=_C
_KcprtSleepMode_Object=MibTableColumn
kcprtSleepMode=_KcprtSleepMode_Object((1,3,6,1,4,1,1347,43,5,1,1,33),_KcprtSleepMode_Type())
kcprtSleepMode.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtSleepMode.setStatus(_A)
class _KcprtAutoContinueMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_M,1)))
_KcprtAutoContinueMode_Type.__name__=_C
_KcprtAutoContinueMode_Object=MibTableColumn
kcprtAutoContinueMode=_KcprtAutoContinueMode_Object((1,3,6,1,4,1,1347,43,5,1,1,34),_KcprtAutoContinueMode_Type())
kcprtAutoContinueMode.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtAutoContinueMode.setStatus(_A)
class _KcprtAutoContinueTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_KcprtAutoContinueTimer_Type.__name__=_C
_KcprtAutoContinueTimer_Object=MibTableColumn
kcprtAutoContinueTimer=_KcprtAutoContinueTimer_Object((1,3,6,1,4,1,1347,43,5,1,1,35),_KcprtAutoContinueTimer_Type())
kcprtAutoContinueTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtAutoContinueTimer.setStatus(_A)
class _KcprtAbsoluteModelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_KcprtAbsoluteModelName_Type.__name__=_H
_KcprtAbsoluteModelName_Object=MibTableColumn
kcprtAbsoluteModelName=_KcprtAbsoluteModelName_Object((1,3,6,1,4,1,1347,43,5,1,1,36),_KcprtAbsoluteModelName_Type())
kcprtAbsoluteModelName.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtAbsoluteModelName.setStatus(_A)
class _KcprtEquipmentID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_KcprtEquipmentID_Type.__name__=_H
_KcprtEquipmentID_Object=MibTableColumn
kcprtEquipmentID=_KcprtEquipmentID_Object((1,3,6,1,4,1,1347,43,5,1,1,37),_KcprtEquipmentID_Type())
kcprtEquipmentID.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtEquipmentID.setStatus(_A)
_KcprtMaxCopyCount_Type=Integer32
_KcprtMaxCopyCount_Object=MibTableColumn
kcprtMaxCopyCount=_KcprtMaxCopyCount_Object((1,3,6,1,4,1,1347,43,5,1,1,38),_KcprtMaxCopyCount_Type())
kcprtMaxCopyCount.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMaxCopyCount.setStatus(_A)
_KcprtCpuTable_Object=MibTable
kcprtCpuTable=_KcprtCpuTable_Object((1,3,6,1,4,1,1347,43,5,4))
if mibBuilder.loadTexts:kcprtCpuTable.setStatus(_A)
_KcprtCpuEntry_Object=MibTableRow
kcprtCpuEntry=_KcprtCpuEntry_Object((1,3,6,1,4,1,1347,43,5,4,1))
kcprtCpuEntry.setIndexNames((0,_F,_G),(0,_E,_c))
if mibBuilder.loadTexts:kcprtCpuEntry.setStatus(_A)
_KcprtCpuIndex_Type=Integer32
_KcprtCpuIndex_Object=MibTableColumn
kcprtCpuIndex=_KcprtCpuIndex_Object((1,3,6,1,4,1,1347,43,5,4,1,1),_KcprtCpuIndex_Type())
kcprtCpuIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtCpuIndex.setStatus(_A)
class _KcprtCpuName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_KcprtCpuName_Type.__name__=_H
_KcprtCpuName_Object=MibTableColumn
kcprtCpuName=_KcprtCpuName_Object((1,3,6,1,4,1,1347,43,5,4,1,2),_KcprtCpuName_Type())
kcprtCpuName.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtCpuName.setStatus(_A)
_KcprtCpuClock_Type=Integer32
_KcprtCpuClock_Object=MibTableColumn
kcprtCpuClock=_KcprtCpuClock_Object((1,3,6,1,4,1,1347,43,5,4,1,3),_KcprtCpuClock_Type())
kcprtCpuClock.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtCpuClock.setStatus(_A)
class _KcprtCpuRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('engine',0),('controller',1)))
_KcprtCpuRole_Type.__name__=_C
_KcprtCpuRole_Object=MibTableColumn
kcprtCpuRole=_KcprtCpuRole_Object((1,3,6,1,4,1,1347,43,5,4,1,4),_KcprtCpuRole_Type())
kcprtCpuRole.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtCpuRole.setStatus(_A)
class _KcprtFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_KcprtFirmwareVersion_Type.__name__=_H
_KcprtFirmwareVersion_Object=MibTableColumn
kcprtFirmwareVersion=_KcprtFirmwareVersion_Object((1,3,6,1,4,1,1347,43,5,4,1,5),_KcprtFirmwareVersion_Type())
kcprtFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtFirmwareVersion.setStatus(_A)
class _KcprtFirmwareUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*((_U,3),(_d,4)))
_KcprtFirmwareUpdate_Type.__name__=_C
_KcprtFirmwareUpdate_Object=MibTableColumn
kcprtFirmwareUpdate=_KcprtFirmwareUpdate_Object((1,3,6,1,4,1,1347,43,5,4,1,6),_KcprtFirmwareUpdate_Type())
kcprtFirmwareUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtFirmwareUpdate.setStatus(_A)
_KcprtInput_ObjectIdentity=ObjectIdentity
kcprtInput=_KcprtInput_ObjectIdentity((1,3,6,1,4,1,1347,43,8))
_KcprtInputTable_Object=MibTable
kcprtInputTable=_KcprtInputTable_Object((1,3,6,1,4,1,1347,43,8,1))
if mibBuilder.loadTexts:kcprtInputTable.setStatus(_A)
_KcprtInputEntry_Object=MibTableRow
kcprtInputEntry=_KcprtInputEntry_Object((1,3,6,1,4,1,1347,43,8,1,1))
kcprtInputEntry.setIndexNames((0,_F,_G),(0,_E,_e))
if mibBuilder.loadTexts:kcprtInputEntry.setStatus(_A)
_KcprtInputIndex_Type=Integer32
_KcprtInputIndex_Object=MibTableColumn
kcprtInputIndex=_KcprtInputIndex_Object((1,3,6,1,4,1,1347,43,8,1,1,1),_KcprtInputIndex_Type())
kcprtInputIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtInputIndex.setStatus(_A)
class _KcprtInputMPtrayMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,5)));namedValues=NamedValues(*(('cassette',0),('manual',1),('first',2),('notPresent',5)))
_KcprtInputMPtrayMode_Type.__name__=_C
_KcprtInputMPtrayMode_Object=MibTableColumn
kcprtInputMPtrayMode=_KcprtInputMPtrayMode_Object((1,3,6,1,4,1,1347,43,8,1,1,2),_KcprtInputMPtrayMode_Type())
kcprtInputMPtrayMode.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtInputMPtrayMode.setStatus(_A)
class _KcprtInputGroupMember_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5)));namedValues=NamedValues(*(('member',3),('notMember',4),('alone',5)))
_KcprtInputGroupMember_Type.__name__=_C
_KcprtInputGroupMember_Object=MibTableColumn
kcprtInputGroupMember=_KcprtInputGroupMember_Object((1,3,6,1,4,1,1347,43,8,1,1,3),_KcprtInputGroupMember_Type())
kcprtInputGroupMember.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtInputGroupMember.setStatus(_A)
_KcprtInputMediaListIndex_Type=Integer32
_KcprtInputMediaListIndex_Object=MibTableColumn
kcprtInputMediaListIndex=_KcprtInputMediaListIndex_Object((1,3,6,1,4,1,1347,43,8,1,1,4),_KcprtInputMediaListIndex_Type())
kcprtInputMediaListIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtInputMediaListIndex.setStatus(_A)
class _KcprtInputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ready',0),('down',1)))
_KcprtInputStatus_Type.__name__=_C
_KcprtInputStatus_Object=MibTableColumn
kcprtInputStatus=_KcprtInputStatus_Object((1,3,6,1,4,1,1347,43,8,1,1,5),_KcprtInputStatus_Type())
kcprtInputStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtInputStatus.setStatus(_A)
_KcprtInputDialPaperSize_Type=Integer32
_KcprtInputDialPaperSize_Object=MibTableColumn
kcprtInputDialPaperSize=_KcprtInputDialPaperSize_Object((1,3,6,1,4,1,1347,43,8,1,1,6),_KcprtInputDialPaperSize_Type())
kcprtInputDialPaperSize.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtInputDialPaperSize.setStatus(_A)
_KcprtInputOtherPaperSize_Type=Integer32
_KcprtInputOtherPaperSize_Object=MibTableColumn
kcprtInputOtherPaperSize=_KcprtInputOtherPaperSize_Object((1,3,6,1,4,1,1347,43,8,1,1,7),_KcprtInputOtherPaperSize_Type())
kcprtInputOtherPaperSize.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtInputOtherPaperSize.setStatus(_A)
class _PrtInputCustomDimFeedDirDeclared_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_PrtInputCustomDimFeedDirDeclared_Type.__name__=_C
_PrtInputCustomDimFeedDirDeclared_Object=MibTableColumn
prtInputCustomDimFeedDirDeclared=_PrtInputCustomDimFeedDirDeclared_Object((1,3,6,1,4,1,1347,43,8,1,1,8),_PrtInputCustomDimFeedDirDeclared_Type())
prtInputCustomDimFeedDirDeclared.setMaxAccess(_D)
if mibBuilder.loadTexts:prtInputCustomDimFeedDirDeclared.setStatus(_A)
class _PrtInputCustomDimXFeedDirDeclared_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_PrtInputCustomDimXFeedDirDeclared_Type.__name__=_C
_PrtInputCustomDimXFeedDirDeclared_Object=MibTableColumn
prtInputCustomDimXFeedDirDeclared=_PrtInputCustomDimXFeedDirDeclared_Object((1,3,6,1,4,1,1347,43,8,1,1,9),_PrtInputCustomDimXFeedDirDeclared_Type())
prtInputCustomDimXFeedDirDeclared.setMaxAccess(_D)
if mibBuilder.loadTexts:prtInputCustomDimXFeedDirDeclared.setStatus(_A)
_KcprnInputMediaMatrix_Type=DisplayString
_KcprnInputMediaMatrix_Object=MibTableColumn
kcprnInputMediaMatrix=_KcprnInputMediaMatrix_Object((1,3,6,1,4,1,1347,43,8,1,1,10),_KcprnInputMediaMatrix_Type())
kcprnInputMediaMatrix.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprnInputMediaMatrix.setStatus(_A)
_KcprnInputPaperSizeIndex_Type=Integer32
_KcprnInputPaperSizeIndex_Object=MibTableColumn
kcprnInputPaperSizeIndex=_KcprnInputPaperSizeIndex_Object((1,3,6,1,4,1,1347,43,8,1,1,11),_KcprnInputPaperSizeIndex_Type())
kcprnInputPaperSizeIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprnInputPaperSizeIndex.setStatus(_A)
_KcprtInputGroupTable_Object=MibTable
kcprtInputGroupTable=_KcprtInputGroupTable_Object((1,3,6,1,4,1,1347,43,8,2))
if mibBuilder.loadTexts:kcprtInputGroupTable.setStatus(_A)
_KcprtInputGroupEntry_Object=MibTableRow
kcprtInputGroupEntry=_KcprtInputGroupEntry_Object((1,3,6,1,4,1,1347,43,8,2,1))
kcprtInputGroupEntry.setIndexNames((0,_F,_G),(0,_E,_f))
if mibBuilder.loadTexts:kcprtInputGroupEntry.setStatus(_A)
_KcprtInputGroupIndex_Type=Integer32
_KcprtInputGroupIndex_Object=MibTableColumn
kcprtInputGroupIndex=_KcprtInputGroupIndex_Object((1,3,6,1,4,1,1347,43,8,2,1,1),_KcprtInputGroupIndex_Type())
kcprtInputGroupIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtInputGroupIndex.setStatus(_A)
class _KcprtInputGroupMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_J,0),('group',1),('size',2),('all',3)))
_KcprtInputGroupMode_Type.__name__=_C
_KcprtInputGroupMode_Object=MibTableColumn
kcprtInputGroupMode=_KcprtInputGroupMode_Object((1,3,6,1,4,1,1347,43,8,2,1,2),_KcprtInputGroupMode_Type())
kcprtInputGroupMode.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtInputGroupMode.setStatus(_A)
_KcprtOutput_ObjectIdentity=ObjectIdentity
kcprtOutput=_KcprtOutput_ObjectIdentity((1,3,6,1,4,1,1347,43,9))
_KcprtOutputTable_Object=MibTable
kcprtOutputTable=_KcprtOutputTable_Object((1,3,6,1,4,1,1347,43,9,1))
if mibBuilder.loadTexts:kcprtOutputTable.setStatus(_A)
_KcprtOutputEntry_Object=MibTableRow
kcprtOutputEntry=_KcprtOutputEntry_Object((1,3,6,1,4,1,1347,43,9,1,1))
kcprtOutputEntry.setIndexNames((0,_F,_G),(0,_E,_R))
if mibBuilder.loadTexts:kcprtOutputEntry.setStatus(_A)
_KcprtOutputIndex_Type=Integer32
_KcprtOutputIndex_Object=MibTableColumn
kcprtOutputIndex=_KcprtOutputIndex_Object((1,3,6,1,4,1,1347,43,9,1,1,1),_KcprtOutputIndex_Type())
kcprtOutputIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtOutputIndex.setStatus(_A)
class _KcprtOutputMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('sorter',0),('collator',1),('stacker',2),('mailbox',3)))
_KcprtOutputMode_Type.__name__=_C
_KcprtOutputMode_Object=MibTableColumn
kcprtOutputMode=_KcprtOutputMode_Object((1,3,6,1,4,1,1347,43,9,1,1,2),_KcprtOutputMode_Type())
kcprtOutputMode.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtOutputMode.setStatus(_A)
class _KcprtOutputMultiMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('id-specific',1),('if-specific',2)))
_KcprtOutputMultiMode_Type.__name__=_C
_KcprtOutputMultiMode_Object=MibTableColumn
kcprtOutputMultiMode=_KcprtOutputMultiMode_Object((1,3,6,1,4,1,1347,43,9,1,1,3),_KcprtOutputMultiMode_Type())
kcprtOutputMultiMode.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtOutputMultiMode.setStatus(_A)
_KcprtOutputGroupNumber_Type=Integer32
_KcprtOutputGroupNumber_Object=MibTableColumn
kcprtOutputGroupNumber=_KcprtOutputGroupNumber_Object((1,3,6,1,4,1,1347,43,9,1,1,4),_KcprtOutputGroupNumber_Type())
kcprtOutputGroupNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtOutputGroupNumber.setStatus(_A)
_KcprtOutputDefaultGroup_Type=Integer32
_KcprtOutputDefaultGroup_Object=MibTableColumn
kcprtOutputDefaultGroup=_KcprtOutputDefaultGroup_Object((1,3,6,1,4,1,1347,43,9,1,1,5),_KcprtOutputDefaultGroup_Type())
kcprtOutputDefaultGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtOutputDefaultGroup.setStatus(_A)
class _KcprtOutputBulkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notFull',0),('full',1)))
_KcprtOutputBulkStatus_Type.__name__=_C
_KcprtOutputBulkStatus_Object=MibTableColumn
kcprtOutputBulkStatus=_KcprtOutputBulkStatus_Object((1,3,6,1,4,1,1347,43,9,1,1,6),_KcprtOutputBulkStatus_Type())
kcprtOutputBulkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtOutputBulkStatus.setStatus(_A)
_KcprtOutputTrayMaxCapacity_Type=Integer32
_KcprtOutputTrayMaxCapacity_Object=MibTableColumn
kcprtOutputTrayMaxCapacity=_KcprtOutputTrayMaxCapacity_Object((1,3,6,1,4,1,1347,43,9,1,1,7),_KcprtOutputTrayMaxCapacity_Type())
kcprtOutputTrayMaxCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtOutputTrayMaxCapacity.setStatus(_A)
_KcprtStapler_Type=PresentOnOff
_KcprtStapler_Object=MibTableColumn
kcprtStapler=_KcprtStapler_Object((1,3,6,1,4,1,1347,43,9,1,1,8),_KcprtStapler_Type())
kcprtStapler.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtStapler.setStatus(_A)
_KcprtStaplerConsumableState_Type=Integer32
_KcprtStaplerConsumableState_Object=MibTableColumn
kcprtStaplerConsumableState=_KcprtStaplerConsumableState_Object((1,3,6,1,4,1,1347,43,9,1,1,9),_KcprtStaplerConsumableState_Type())
kcprtStaplerConsumableState.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtStaplerConsumableState.setStatus(_A)
class _KcprtOutputActionOnFull_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('printStoppedWithMessage',0),('printContinue',1)))
_KcprtOutputActionOnFull_Type.__name__=_C
_KcprtOutputActionOnFull_Object=MibTableColumn
kcprtOutputActionOnFull=_KcprtOutputActionOnFull_Object((1,3,6,1,4,1,1347,43,9,1,1,10),_KcprtOutputActionOnFull_Type())
kcprtOutputActionOnFull.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtOutputActionOnFull.setStatus(_A)
class _KcprtOutputPunchStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_V,0),(_U,1)))
_KcprtOutputPunchStatus_Type.__name__=_C
_KcprtOutputPunchStatus_Object=MibTableColumn
kcprtOutputPunchStatus=_KcprtOutputPunchStatus_Object((1,3,6,1,4,1,1347,43,9,1,1,11),_KcprtOutputPunchStatus_Type())
kcprtOutputPunchStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtOutputPunchStatus.setStatus(_A)
class _KcprtOutputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ready',0),('down',1)))
_KcprtOutputStatus_Type.__name__=_C
_KcprtOutputStatus_Object=MibTableColumn
kcprtOutputStatus=_KcprtOutputStatus_Object((1,3,6,1,4,1,1347,43,9,1,1,12),_KcprtOutputStatus_Type())
kcprtOutputStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtOutputStatus.setStatus(_A)
_KcprtTrayGroupTable_Object=MibTable
kcprtTrayGroupTable=_KcprtTrayGroupTable_Object((1,3,6,1,4,1,1347,43,9,2))
if mibBuilder.loadTexts:kcprtTrayGroupTable.setStatus(_A)
_KcprtTrayGroupEntry_Object=MibTableRow
kcprtTrayGroupEntry=_KcprtTrayGroupEntry_Object((1,3,6,1,4,1,1347,43,9,2,1))
kcprtTrayGroupEntry.setIndexNames((0,_F,_G),(0,_E,_R),(0,_E,_g))
if mibBuilder.loadTexts:kcprtTrayGroupEntry.setStatus(_A)
_KcprtTrayGroupIndex_Type=Integer32
_KcprtTrayGroupIndex_Object=MibTableColumn
kcprtTrayGroupIndex=_KcprtTrayGroupIndex_Object((1,3,6,1,4,1,1347,43,9,2,1,1),_KcprtTrayGroupIndex_Type())
kcprtTrayGroupIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtTrayGroupIndex.setStatus(_A)
_KcprtTrayGroupBeginIndex_Type=Integer32
_KcprtTrayGroupBeginIndex_Object=MibTableColumn
kcprtTrayGroupBeginIndex=_KcprtTrayGroupBeginIndex_Object((1,3,6,1,4,1,1347,43,9,2,1,2),_KcprtTrayGroupBeginIndex_Type())
kcprtTrayGroupBeginIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtTrayGroupBeginIndex.setStatus(_A)
_KcprtTrayGroupEndIndex_Type=Integer32
_KcprtTrayGroupEndIndex_Object=MibTableColumn
kcprtTrayGroupEndIndex=_KcprtTrayGroupEndIndex_Object((1,3,6,1,4,1,1347,43,9,2,1,3),_KcprtTrayGroupEndIndex_Type())
kcprtTrayGroupEndIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtTrayGroupEndIndex.setStatus(_A)
_KcprtOutputTrayTable_Object=MibTable
kcprtOutputTrayTable=_KcprtOutputTrayTable_Object((1,3,6,1,4,1,1347,43,9,3))
if mibBuilder.loadTexts:kcprtOutputTrayTable.setStatus(_A)
_KcprtOutputTrayEntry_Object=MibTableRow
kcprtOutputTrayEntry=_KcprtOutputTrayEntry_Object((1,3,6,1,4,1,1347,43,9,3,1))
kcprtOutputTrayEntry.setIndexNames((0,_F,_G),(0,_E,_R),(0,_E,_h))
if mibBuilder.loadTexts:kcprtOutputTrayEntry.setStatus(_A)
_KcprtOutputTrayIndex_Type=Integer32
_KcprtOutputTrayIndex_Object=MibTableColumn
kcprtOutputTrayIndex=_KcprtOutputTrayIndex_Object((1,3,6,1,4,1,1347,43,9,3,1,1),_KcprtOutputTrayIndex_Type())
kcprtOutputTrayIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtOutputTrayIndex.setStatus(_A)
_KcprtOutputTrayOrder_Type=Integer32
_KcprtOutputTrayOrder_Object=MibTableColumn
kcprtOutputTrayOrder=_KcprtOutputTrayOrder_Object((1,3,6,1,4,1,1347,43,9,3,1,2),_KcprtOutputTrayOrder_Type())
kcprtOutputTrayOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtOutputTrayOrder.setStatus(_A)
_KcprtOutputTrayGroup_Type=Integer32
_KcprtOutputTrayGroup_Object=MibTableColumn
kcprtOutputTrayGroup=_KcprtOutputTrayGroup_Object((1,3,6,1,4,1,1347,43,9,3,1,3),_KcprtOutputTrayGroup_Type())
kcprtOutputTrayGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtOutputTrayGroup.setStatus(_A)
_KcprtOutputTrayCount_Type=Integer32
_KcprtOutputTrayCount_Object=MibTableColumn
kcprtOutputTrayCount=_KcprtOutputTrayCount_Object((1,3,6,1,4,1,1347,43,9,3,1,4),_KcprtOutputTrayCount_Type())
kcprtOutputTrayCount.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtOutputTrayCount.setStatus(_A)
class _KcprtOutputTrayName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_KcprtOutputTrayName_Type.__name__=_H
_KcprtOutputTrayName_Object=MibTableColumn
kcprtOutputTrayName=_KcprtOutputTrayName_Object((1,3,6,1,4,1,1347,43,9,3,1,5),_KcprtOutputTrayName_Type())
kcprtOutputTrayName.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtOutputTrayName.setStatus(_A)
_KcprtPunchGroupTable_Object=MibTable
kcprtPunchGroupTable=_KcprtPunchGroupTable_Object((1,3,6,1,4,1,1347,43,9,4))
if mibBuilder.loadTexts:kcprtPunchGroupTable.setStatus(_A)
_KcprtPunchGroupEntry_Object=MibTableRow
kcprtPunchGroupEntry=_KcprtPunchGroupEntry_Object((1,3,6,1,4,1,1347,43,9,4,1))
kcprtPunchGroupEntry.setIndexNames((0,_F,_G),(0,_E,_i))
if mibBuilder.loadTexts:kcprtPunchGroupEntry.setStatus(_A)
_KcprtPunchGroupIndex_Type=Integer32
_KcprtPunchGroupIndex_Object=MibTableColumn
kcprtPunchGroupIndex=_KcprtPunchGroupIndex_Object((1,3,6,1,4,1,1347,43,9,4,1,1),_KcprtPunchGroupIndex_Type())
kcprtPunchGroupIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtPunchGroupIndex.setStatus(_A)
class _KcprtPunchGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_KcprtPunchGroupName_Type.__name__=_H
_KcprtPunchGroupName_Object=MibTableColumn
kcprtPunchGroupName=_KcprtPunchGroupName_Object((1,3,6,1,4,1,1347,43,9,4,1,2),_KcprtPunchGroupName_Type())
kcprtPunchGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtPunchGroupName.setStatus(_A)
_KcprtPunchGroupHoleNumber_Type=Integer32
_KcprtPunchGroupHoleNumber_Object=MibTableColumn
kcprtPunchGroupHoleNumber=_KcprtPunchGroupHoleNumber_Object((1,3,6,1,4,1,1347,43,9,4,1,3),_KcprtPunchGroupHoleNumber_Type())
kcprtPunchGroupHoleNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtPunchGroupHoleNumber.setStatus(_A)
class _KcprtPunchGroupType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_KcprtPunchGroupType_Type.__name__=_H
_KcprtPunchGroupType_Object=MibTableColumn
kcprtPunchGroupType=_KcprtPunchGroupType_Object((1,3,6,1,4,1,1347,43,9,4,1,4),_KcprtPunchGroupType_Type())
kcprtPunchGroupType.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtPunchGroupType.setStatus(_A)
_KcprtMarker_ObjectIdentity=ObjectIdentity
kcprtMarker=_KcprtMarker_ObjectIdentity((1,3,6,1,4,1,1347,43,10))
_KcprtMarkerTable_Object=MibTable
kcprtMarkerTable=_KcprtMarkerTable_Object((1,3,6,1,4,1,1347,43,10,1))
if mibBuilder.loadTexts:kcprtMarkerTable.setStatus(_A)
_KcprtMarkerEntry_Object=MibTableRow
kcprtMarkerEntry=_KcprtMarkerEntry_Object((1,3,6,1,4,1,1347,43,10,1,1))
kcprtMarkerEntry.setIndexNames((0,_F,_G),(0,_Y,_Z))
if mibBuilder.loadTexts:kcprtMarkerEntry.setStatus(_A)
_KcprtMarkerIndex_Type=Integer32
_KcprtMarkerIndex_Object=MibTableColumn
kcprtMarkerIndex=_KcprtMarkerIndex_Object((1,3,6,1,4,1,1347,43,10,1,1,1),_KcprtMarkerIndex_Type())
kcprtMarkerIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtMarkerIndex.setStatus(_A)
class _KcprtMarkerKirLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_j,0),(_W,1),(_k,2),('dark',3)))
_KcprtMarkerKirLevel_Type.__name__=_C
_KcprtMarkerKirLevel_Object=MibTableColumn
kcprtMarkerKirLevel=_KcprtMarkerKirLevel_Object((1,3,6,1,4,1,1347,43,10,1,1,2),_KcprtMarkerKirLevel_Type())
kcprtMarkerKirLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtMarkerKirLevel.setStatus(_A)
class _KcprtMarkerEcoprintLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_j,0),(_W,1),(_k,2),('dark',3)))
_KcprtMarkerEcoprintLevel_Type.__name__=_C
_KcprtMarkerEcoprintLevel_Object=MibTableColumn
kcprtMarkerEcoprintLevel=_KcprtMarkerEcoprintLevel_Object((1,3,6,1,4,1,1347,43,10,1,1,3),_KcprtMarkerEcoprintLevel_Type())
kcprtMarkerEcoprintLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtMarkerEcoprintLevel.setStatus(_A)
_KcprtMarkerAddressabilityFeedDirDeclared_Type=Integer32
_KcprtMarkerAddressabilityFeedDirDeclared_Object=MibTableColumn
kcprtMarkerAddressabilityFeedDirDeclared=_KcprtMarkerAddressabilityFeedDirDeclared_Object((1,3,6,1,4,1,1347,43,10,1,1,4),_KcprtMarkerAddressabilityFeedDirDeclared_Type())
kcprtMarkerAddressabilityFeedDirDeclared.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtMarkerAddressabilityFeedDirDeclared.setStatus(_A)
_KcprtMarkerAddressabilityXFeedDirDeclared_Type=Integer32
_KcprtMarkerAddressabilityXFeedDirDeclared_Object=MibTableColumn
kcprtMarkerAddressabilityXFeedDirDeclared=_KcprtMarkerAddressabilityXFeedDirDeclared_Object((1,3,6,1,4,1,1347,43,10,1,1,5),_KcprtMarkerAddressabilityXFeedDirDeclared_Type())
kcprtMarkerAddressabilityXFeedDirDeclared.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtMarkerAddressabilityXFeedDirDeclared.setStatus(_A)
_KcprtMarkerAddressabilityFeedDirChosen_Type=Integer32
_KcprtMarkerAddressabilityFeedDirChosen_Object=MibTableColumn
kcprtMarkerAddressabilityFeedDirChosen=_KcprtMarkerAddressabilityFeedDirChosen_Object((1,3,6,1,4,1,1347,43,10,1,1,6),_KcprtMarkerAddressabilityFeedDirChosen_Type())
kcprtMarkerAddressabilityFeedDirChosen.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMarkerAddressabilityFeedDirChosen.setStatus(_A)
_KcprtMarkerAddressabilityXFeedDirChosen_Type=Integer32
_KcprtMarkerAddressabilityXFeedDirChosen_Object=MibTableColumn
kcprtMarkerAddressabilityXFeedDirChosen=_KcprtMarkerAddressabilityXFeedDirChosen_Object((1,3,6,1,4,1,1347,43,10,1,1,7),_KcprtMarkerAddressabilityXFeedDirChosen_Type())
kcprtMarkerAddressabilityXFeedDirChosen.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMarkerAddressabilityXFeedDirChosen.setStatus(_A)
_KcprtMarkerDrumCounter_Type=Integer32
_KcprtMarkerDrumCounter_Object=MibTableColumn
kcprtMarkerDrumCounter=_KcprtMarkerDrumCounter_Object((1,3,6,1,4,1,1347,43,10,1,1,8),_KcprtMarkerDrumCounter_Type())
kcprtMarkerDrumCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMarkerDrumCounter.setStatus(_A)
class _KcprtMarkerColorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*(('monochrome',1),('color',4)))
_KcprtMarkerColorMode_Type.__name__=_C
_KcprtMarkerColorMode_Object=MibTableColumn
kcprtMarkerColorMode=_KcprtMarkerColorMode_Object((1,3,6,1,4,1,1347,43,10,1,1,9),_KcprtMarkerColorMode_Type())
kcprtMarkerColorMode.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtMarkerColorMode.setStatus(_A)
_KcprtMarkerBitsPerPixel_Type=Integer32
_KcprtMarkerBitsPerPixel_Object=MibTableColumn
kcprtMarkerBitsPerPixel=_KcprtMarkerBitsPerPixel_Object((1,3,6,1,4,1,1347,43,10,1,1,10),_KcprtMarkerBitsPerPixel_Type())
kcprtMarkerBitsPerPixel.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtMarkerBitsPerPixel.setStatus(_A)
class _KcprtMarkerGlossMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('low',0),('high',1)))
_KcprtMarkerGlossMode_Type.__name__=_C
_KcprtMarkerGlossMode_Object=MibTableColumn
kcprtMarkerGlossMode=_KcprtMarkerGlossMode_Object((1,3,6,1,4,1,1347,43,10,1,1,11),_KcprtMarkerGlossMode_Type())
kcprtMarkerGlossMode.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtMarkerGlossMode.setStatus(_A)
_KcprtMarkerServiceCount_Type=Integer32
_KcprtMarkerServiceCount_Object=MibTableColumn
kcprtMarkerServiceCount=_KcprtMarkerServiceCount_Object((1,3,6,1,4,1,1347,43,10,1,1,12),_KcprtMarkerServiceCount_Type())
kcprtMarkerServiceCount.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMarkerServiceCount.setStatus(_A)
_KcprtColorant_ObjectIdentity=ObjectIdentity
kcprtColorant=_KcprtColorant_ObjectIdentity((1,3,6,1,4,1,1347,43,12))
_KcprtColorantGeneralTable_Object=MibTable
kcprtColorantGeneralTable=_KcprtColorantGeneralTable_Object((1,3,6,1,4,1,1347,43,12,1))
if mibBuilder.loadTexts:kcprtColorantGeneralTable.setStatus(_A)
_KcprtColorantGeneralEntry_Object=MibTableRow
kcprtColorantGeneralEntry=_KcprtColorantGeneralEntry_Object((1,3,6,1,4,1,1347,43,12,1,1))
kcprtColorantGeneralEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:kcprtColorantGeneralEntry.setStatus(_A)
class _KcprtColorQuality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Q,0),('quick',1),('fine',2),('presentation',3)))
_KcprtColorQuality_Type.__name__=_C
_KcprtColorQuality_Object=MibTableColumn
kcprtColorQuality=_KcprtColorQuality_Object((1,3,6,1,4,1,1347,43,12,1,1,1),_KcprtColorQuality_Type())
kcprtColorQuality.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtColorQuality.setStatus(_L)
class _KcprtColorMatching_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_J,0),('auto',1),('vivid',2),('display',3)))
_KcprtColorMatching_Type.__name__=_C
_KcprtColorMatching_Object=MibTableColumn
kcprtColorMatching=_KcprtColorMatching_Object((1,3,6,1,4,1,1347,43,12,1,1,2),_KcprtColorMatching_Type())
kcprtColorMatching.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtColorMatching.setStatus(_L)
class _KcprtColorantIdentifier_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_KcprtColorantIdentifier_Type.__name__=_K
_KcprtColorantIdentifier_Object=MibTableColumn
kcprtColorantIdentifier=_KcprtColorantIdentifier_Object((1,3,6,1,4,1,1347,43,12,1,1,3),_KcprtColorantIdentifier_Type())
kcprtColorantIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtColorantIdentifier.setStatus(_L)
class _KcprtRGBSimulation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_V,0),('smtpe240m',1),('hdtv',2),('trinitron',3),('applergb',4),('ntsc',5),('kcrgb',6),('custom',7)))
_KcprtRGBSimulation_Type.__name__=_C
_KcprtRGBSimulation_Object=MibTableColumn
kcprtRGBSimulation=_KcprtRGBSimulation_Object((1,3,6,1,4,1,1347,43,12,1,1,4),_KcprtRGBSimulation_Type())
kcprtRGBSimulation.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtRGBSimulation.setStatus(_L)
class _KcprtCMYKSimulation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_Q,0),(_V,1),('swop',2),('euroscale',3),('toyo',4),('dic',5)))
_KcprtCMYKSimulation_Type.__name__=_C
_KcprtCMYKSimulation_Object=MibTableColumn
kcprtCMYKSimulation=_KcprtCMYKSimulation_Object((1,3,6,1,4,1,1347,43,12,1,1,5),_KcprtCMYKSimulation_Type())
kcprtCMYKSimulation.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtCMYKSimulation.setStatus(_L)
_KcprtChannel_ObjectIdentity=ObjectIdentity
kcprtChannel=_KcprtChannel_ObjectIdentity((1,3,6,1,4,1,1347,43,14))
_KcprtChannelTable_Object=MibTable
kcprtChannelTable=_KcprtChannelTable_Object((1,3,6,1,4,1,1347,43,14,1))
if mibBuilder.loadTexts:kcprtChannelTable.setStatus(_A)
_KcprtChannelEntry_Object=MibTableRow
kcprtChannelEntry=_KcprtChannelEntry_Object((1,3,6,1,4,1,1347,43,14,1,1))
kcprtChannelEntry.setIndexNames((0,_F,_G),(0,_E,_l))
if mibBuilder.loadTexts:kcprtChannelEntry.setStatus(_A)
_KcprtChannelIndex_Type=Integer32
_KcprtChannelIndex_Object=MibTableColumn
kcprtChannelIndex=_KcprtChannelIndex_Object((1,3,6,1,4,1,1347,43,14,1,1,1),_KcprtChannelIndex_Type())
kcprtChannelIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtChannelIndex.setStatus(_A)
class _KcprtChannelMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('through',0),('hexDump',1)))
_KcprtChannelMode_Type.__name__=_C
_KcprtChannelMode_Object=MibTableColumn
kcprtChannelMode=_KcprtChannelMode_Object((1,3,6,1,4,1,1347,43,14,1,1,2),_KcprtChannelMode_Type())
kcprtChannelMode.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtChannelMode.setStatus(_A)
class _KcprtChannelCopyCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_KcprtChannelCopyCount_Type.__name__=_C
_KcprtChannelCopyCount_Object=MibTableColumn
kcprtChannelCopyCount=_KcprtChannelCopyCount_Object((1,3,6,1,4,1,1347,43,14,1,1,3),_KcprtChannelCopyCount_Type())
kcprtChannelCopyCount.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtChannelCopyCount.setStatus(_A)
_KcprtChannelResolution_Type=Integer32
_KcprtChannelResolution_Object=MibTableColumn
kcprtChannelResolution=_KcprtChannelResolution_Object((1,3,6,1,4,1,1347,43,14,1,1,4),_KcprtChannelResolution_Type())
kcprtChannelResolution.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtChannelResolution.setStatus(_A)
_KcprtChannelPaperSize_Type=Integer32
_KcprtChannelPaperSize_Object=MibTableColumn
kcprtChannelPaperSize=_KcprtChannelPaperSize_Object((1,3,6,1,4,1,1347,43,14,1,1,5),_KcprtChannelPaperSize_Type())
kcprtChannelPaperSize.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtChannelPaperSize.setStatus(_A)
_KcprtHostBufferRatio_Type=Integer32
_KcprtHostBufferRatio_Object=MibTableColumn
kcprtHostBufferRatio=_KcprtHostBufferRatio_Object((1,3,6,1,4,1,1347,43,14,1,1,6),_KcprtHostBufferRatio_Type())
kcprtHostBufferRatio.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtHostBufferRatio.setStatus(_L)
class _KcprtChannelErrorCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtChannelErrorCounter_Type.__name__=_C
_KcprtChannelErrorCounter_Object=MibTableColumn
kcprtChannelErrorCounter=_KcprtChannelErrorCounter_Object((1,3,6,1,4,1,1347,43,14,1,1,7),_KcprtChannelErrorCounter_Type())
kcprtChannelErrorCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtChannelErrorCounter.setStatus(_L)
_KcprtBuzzer_ObjectIdentity=ObjectIdentity
kcprtBuzzer=_KcprtBuzzer_ObjectIdentity((1,3,6,1,4,1,1347,43,17))
_KcprtBuzzerTable_Object=MibTable
kcprtBuzzerTable=_KcprtBuzzerTable_Object((1,3,6,1,4,1,1347,43,17,1))
if mibBuilder.loadTexts:kcprtBuzzerTable.setStatus(_A)
_KcprtBuzzerEntry_Object=MibTableRow
kcprtBuzzerEntry=_KcprtBuzzerEntry_Object((1,3,6,1,4,1,1347,43,17,1,1))
kcprtBuzzerEntry.setIndexNames((0,_F,_G),(0,_E,_m))
if mibBuilder.loadTexts:kcprtBuzzerEntry.setStatus(_A)
_KcprtBuzzerIndex_Type=Integer32
_KcprtBuzzerIndex_Object=MibTableColumn
kcprtBuzzerIndex=_KcprtBuzzerIndex_Object((1,3,6,1,4,1,1347,43,17,1,1,1),_KcprtBuzzerIndex_Type())
kcprtBuzzerIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtBuzzerIndex.setStatus(_A)
class _KcprtBuzzerOnTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,400))
_KcprtBuzzerOnTime_Type.__name__=_C
_KcprtBuzzerOnTime_Object=MibTableColumn
kcprtBuzzerOnTime=_KcprtBuzzerOnTime_Object((1,3,6,1,4,1,1347,43,17,1,1,2),_KcprtBuzzerOnTime_Type())
kcprtBuzzerOnTime.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtBuzzerOnTime.setStatus(_A)
class _KcprtBuzzerOffTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,400))
_KcprtBuzzerOffTime_Type.__name__=_C
_KcprtBuzzerOffTime_Object=MibTableColumn
kcprtBuzzerOffTime=_KcprtBuzzerOffTime_Object((1,3,6,1,4,1,1347,43,17,1,1,3),_KcprtBuzzerOffTime_Type())
kcprtBuzzerOffTime.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtBuzzerOffTime.setStatus(_A)
class _KcprtBuzzerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_M,1)))
_KcprtBuzzerMode_Type.__name__=_C
_KcprtBuzzerMode_Object=MibTableColumn
kcprtBuzzerMode=_KcprtBuzzerMode_Object((1,3,6,1,4,1,1347,43,17,1,1,4),_KcprtBuzzerMode_Type())
kcprtBuzzerMode.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtBuzzerMode.setStatus(_A)
class _KcprtBuzzerTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_KcprtBuzzerTone_Type.__name__=_C
_KcprtBuzzerTone_Object=MibTableColumn
kcprtBuzzerTone=_KcprtBuzzerTone_Object((1,3,6,1,4,1,1347,43,17,1,1,5),_KcprtBuzzerTone_Type())
kcprtBuzzerTone.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtBuzzerTone.setStatus(_A)
_KcprtAlert_ObjectIdentity=ObjectIdentity
kcprtAlert=_KcprtAlert_ObjectIdentity((1,3,6,1,4,1,1347,43,18))
_KcprtAlertTable_Object=MibTable
kcprtAlertTable=_KcprtAlertTable_Object((1,3,6,1,4,1,1347,43,18,1))
if mibBuilder.loadTexts:kcprtAlertTable.setStatus(_A)
_KcprtAlertEntry_Object=MibTableRow
kcprtAlertEntry=_KcprtAlertEntry_Object((1,3,6,1,4,1,1347,43,18,1,1))
kcprtAlertEntry.setIndexNames((0,_F,_G),(0,_E,_n))
if mibBuilder.loadTexts:kcprtAlertEntry.setStatus(_A)
_KcprtAlertIndex_Type=Integer32
_KcprtAlertIndex_Object=MibTableColumn
kcprtAlertIndex=_KcprtAlertIndex_Object((1,3,6,1,4,1,1347,43,18,1,1,1),_KcprtAlertIndex_Type())
kcprtAlertIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtAlertIndex.setStatus(_A)
class _KcprtAlertInformation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_KcprtAlertInformation_Type.__name__=_K
_KcprtAlertInformation_Object=MibTableColumn
kcprtAlertInformation=_KcprtAlertInformation_Object((1,3,6,1,4,1,1347,43,18,1,1,2),_KcprtAlertInformation_Type())
kcprtAlertInformation.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtAlertInformation.setStatus(_A)
_KcprtAlertStateTable_Object=MibTable
kcprtAlertStateTable=_KcprtAlertStateTable_Object((1,3,6,1,4,1,1347,43,18,2))
if mibBuilder.loadTexts:kcprtAlertStateTable.setStatus(_A)
_KcprtAlertStateEntry_Object=MibTableRow
kcprtAlertStateEntry=_KcprtAlertStateEntry_Object((1,3,6,1,4,1,1347,43,18,2,1))
kcprtAlertStateEntry.setIndexNames((0,_F,_G),(0,_E,_o))
if mibBuilder.loadTexts:kcprtAlertStateEntry.setStatus(_A)
_KcprtAlertStateDisplayIndex_Type=Integer32
_KcprtAlertStateDisplayIndex_Object=MibTableColumn
kcprtAlertStateDisplayIndex=_KcprtAlertStateDisplayIndex_Object((1,3,6,1,4,1,1347,43,18,2,1,1),_KcprtAlertStateDisplayIndex_Type())
kcprtAlertStateDisplayIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtAlertStateDisplayIndex.setStatus(_A)
class _KcprtAlertStateDisplay_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_KcprtAlertStateDisplay_Type.__name__=_H
_KcprtAlertStateDisplay_Object=MibTableColumn
kcprtAlertStateDisplay=_KcprtAlertStateDisplay_Object((1,3,6,1,4,1,1347,43,18,2,1,2),_KcprtAlertStateDisplay_Type())
kcprtAlertStateDisplay.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtAlertStateDisplay.setStatus(_A)
_KcprtAlertStateCode_Type=Integer32
_KcprtAlertStateCode_Object=MibTableColumn
kcprtAlertStateCode=_KcprtAlertStateCode_Object((1,3,6,1,4,1,1347,43,18,2,1,3),_KcprtAlertStateCode_Type())
kcprtAlertStateCode.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtAlertStateCode.setStatus(_A)
_KcprtAlertJamLogTable_Object=MibTable
kcprtAlertJamLogTable=_KcprtAlertJamLogTable_Object((1,3,6,1,4,1,1347,43,18,3))
if mibBuilder.loadTexts:kcprtAlertJamLogTable.setStatus(_A)
_KcprtAlertJamLogEntry_Object=MibTableRow
kcprtAlertJamLogEntry=_KcprtAlertJamLogEntry_Object((1,3,6,1,4,1,1347,43,18,3,1))
kcprtAlertJamLogEntry.setIndexNames((0,_F,_G),(0,_E,_p))
if mibBuilder.loadTexts:kcprtAlertJamLogEntry.setStatus(_A)
_KcprtAlertJamLogIndex_Type=Integer32
_KcprtAlertJamLogIndex_Object=MibTableColumn
kcprtAlertJamLogIndex=_KcprtAlertJamLogIndex_Object((1,3,6,1,4,1,1347,43,18,3,1,1),_KcprtAlertJamLogIndex_Type())
kcprtAlertJamLogIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtAlertJamLogIndex.setStatus(_A)
_KcprtAlertJamLogStamp_Type=Integer32
_KcprtAlertJamLogStamp_Object=MibTableColumn
kcprtAlertJamLogStamp=_KcprtAlertJamLogStamp_Object((1,3,6,1,4,1,1347,43,18,3,1,2),_KcprtAlertJamLogStamp_Type())
kcprtAlertJamLogStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtAlertJamLogStamp.setStatus(_A)
_KcprtAlertJamLogFactor_Type=DisplayString
_KcprtAlertJamLogFactor_Object=MibTableColumn
kcprtAlertJamLogFactor=_KcprtAlertJamLogFactor_Object((1,3,6,1,4,1,1347,43,18,3,1,3),_KcprtAlertJamLogFactor_Type())
kcprtAlertJamLogFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtAlertJamLogFactor.setStatus(_A)
_KcprtAlertJamLogPosition_Type=DisplayString
_KcprtAlertJamLogPosition_Object=MibTableColumn
kcprtAlertJamLogPosition=_KcprtAlertJamLogPosition_Object((1,3,6,1,4,1,1347,43,18,3,1,4),_KcprtAlertJamLogPosition_Type())
kcprtAlertJamLogPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtAlertJamLogPosition.setStatus(_A)
_KcprtAlertJamLogInput_Type=Integer32
_KcprtAlertJamLogInput_Object=MibTableColumn
kcprtAlertJamLogInput=_KcprtAlertJamLogInput_Object((1,3,6,1,4,1,1347,43,18,3,1,5),_KcprtAlertJamLogInput_Type())
kcprtAlertJamLogInput.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtAlertJamLogInput.setStatus(_A)
_KcprtAlertJamLogPaper_Type=Integer32
_KcprtAlertJamLogPaper_Object=MibTableColumn
kcprtAlertJamLogPaper=_KcprtAlertJamLogPaper_Object((1,3,6,1,4,1,1347,43,18,3,1,6),_KcprtAlertJamLogPaper_Type())
kcprtAlertJamLogPaper.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtAlertJamLogPaper.setStatus(_A)
_KcprtAlertJamLogMedia_Type=Integer32
_KcprtAlertJamLogMedia_Object=MibTableColumn
kcprtAlertJamLogMedia=_KcprtAlertJamLogMedia_Object((1,3,6,1,4,1,1347,43,18,3,1,7),_KcprtAlertJamLogMedia_Type())
kcprtAlertJamLogMedia.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtAlertJamLogMedia.setStatus(_A)
_KcprtAlertJamLogOutput_Type=Integer32
_KcprtAlertJamLogOutput_Object=MibTableColumn
kcprtAlertJamLogOutput=_KcprtAlertJamLogOutput_Object((1,3,6,1,4,1,1347,43,18,3,1,8),_KcprtAlertJamLogOutput_Type())
kcprtAlertJamLogOutput.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtAlertJamLogOutput.setStatus(_A)
_KcprtAlertCallLogTable_Object=MibTable
kcprtAlertCallLogTable=_KcprtAlertCallLogTable_Object((1,3,6,1,4,1,1347,43,18,4))
if mibBuilder.loadTexts:kcprtAlertCallLogTable.setStatus(_A)
_KcprtAlertCallLogEntry_Object=MibTableRow
kcprtAlertCallLogEntry=_KcprtAlertCallLogEntry_Object((1,3,6,1,4,1,1347,43,18,4,1))
kcprtAlertCallLogEntry.setIndexNames((0,_F,_G),(0,_E,_q))
if mibBuilder.loadTexts:kcprtAlertCallLogEntry.setStatus(_A)
_KcprtAlertCallLogIndex_Type=Integer32
_KcprtAlertCallLogIndex_Object=MibTableColumn
kcprtAlertCallLogIndex=_KcprtAlertCallLogIndex_Object((1,3,6,1,4,1,1347,43,18,4,1,1),_KcprtAlertCallLogIndex_Type())
kcprtAlertCallLogIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtAlertCallLogIndex.setStatus(_A)
_KcprtAlertCallLogStamp_Type=Integer32
_KcprtAlertCallLogStamp_Object=MibTableColumn
kcprtAlertCallLogStamp=_KcprtAlertCallLogStamp_Object((1,3,6,1,4,1,1347,43,18,4,1,2),_KcprtAlertCallLogStamp_Type())
kcprtAlertCallLogStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtAlertCallLogStamp.setStatus(_A)
_KcprtAlertCallLogFactor_Type=DisplayString
_KcprtAlertCallLogFactor_Object=MibTableColumn
kcprtAlertCallLogFactor=_KcprtAlertCallLogFactor_Object((1,3,6,1,4,1,1347,43,18,4,1,3),_KcprtAlertCallLogFactor_Type())
kcprtAlertCallLogFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtAlertCallLogFactor.setStatus(_A)
_KcprtAlertChangeLogTable_Object=MibTable
kcprtAlertChangeLogTable=_KcprtAlertChangeLogTable_Object((1,3,6,1,4,1,1347,43,18,5))
if mibBuilder.loadTexts:kcprtAlertChangeLogTable.setStatus(_A)
_KcprtAlertChangeLogEntry_Object=MibTableRow
kcprtAlertChangeLogEntry=_KcprtAlertChangeLogEntry_Object((1,3,6,1,4,1,1347,43,18,5,1))
kcprtAlertChangeLogEntry.setIndexNames((0,_F,_G),(0,_E,_r))
if mibBuilder.loadTexts:kcprtAlertChangeLogEntry.setStatus(_A)
_KcprtAlertChangeLogIndex_Type=Integer32
_KcprtAlertChangeLogIndex_Object=MibTableColumn
kcprtAlertChangeLogIndex=_KcprtAlertChangeLogIndex_Object((1,3,6,1,4,1,1347,43,18,5,1,1),_KcprtAlertChangeLogIndex_Type())
kcprtAlertChangeLogIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtAlertChangeLogIndex.setStatus(_A)
_KcprtAlertChangeLogStamp_Type=Integer32
_KcprtAlertChangeLogStamp_Object=MibTableColumn
kcprtAlertChangeLogStamp=_KcprtAlertChangeLogStamp_Object((1,3,6,1,4,1,1347,43,18,5,1,2),_KcprtAlertChangeLogStamp_Type())
kcprtAlertChangeLogStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtAlertChangeLogStamp.setStatus(_A)
_KcprtAlertChangeLogKind_Type=DisplayString
_KcprtAlertChangeLogKind_Object=MibTableColumn
kcprtAlertChangeLogKind=_KcprtAlertChangeLogKind_Object((1,3,6,1,4,1,1347,43,18,5,1,3),_KcprtAlertChangeLogKind_Type())
kcprtAlertChangeLogKind.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtAlertChangeLogKind.setStatus(_A)
_KcprtAlertEventCountTable_Object=MibTable
kcprtAlertEventCountTable=_KcprtAlertEventCountTable_Object((1,3,6,1,4,1,1347,43,18,6))
if mibBuilder.loadTexts:kcprtAlertEventCountTable.setStatus(_A)
_KcprtAlertEventCountEntry_Object=MibTableRow
kcprtAlertEventCountEntry=_KcprtAlertEventCountEntry_Object((1,3,6,1,4,1,1347,43,18,6,1))
kcprtAlertEventCountEntry.setIndexNames((0,_F,_G),(0,_E,_s))
if mibBuilder.loadTexts:kcprtAlertEventCountEntry.setStatus(_A)
_KcprtAlertEventCountIndex_Type=Integer32
_KcprtAlertEventCountIndex_Object=MibTableColumn
kcprtAlertEventCountIndex=_KcprtAlertEventCountIndex_Object((1,3,6,1,4,1,1347,43,18,6,1,1),_KcprtAlertEventCountIndex_Type())
kcprtAlertEventCountIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtAlertEventCountIndex.setStatus(_A)
_KcprtAlertEventCountFactor_Type=DisplayString
_KcprtAlertEventCountFactor_Object=MibTableColumn
kcprtAlertEventCountFactor=_KcprtAlertEventCountFactor_Object((1,3,6,1,4,1,1347,43,18,6,1,2),_KcprtAlertEventCountFactor_Type())
kcprtAlertEventCountFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtAlertEventCountFactor.setStatus(_A)
_KcprtAlertEventCountValue_Type=Integer32
_KcprtAlertEventCountValue_Object=MibTableColumn
kcprtAlertEventCountValue=_KcprtAlertEventCountValue_Object((1,3,6,1,4,1,1347,43,18,6,1,3),_KcprtAlertEventCountValue_Type())
kcprtAlertEventCountValue.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtAlertEventCountValue.setStatus(_A)
_KcprtMemoryResource_ObjectIdentity=ObjectIdentity
kcprtMemoryResource=_KcprtMemoryResource_ObjectIdentity((1,3,6,1,4,1,1347,43,20))
_KcprtMemoryDeviceTable_Object=MibTable
kcprtMemoryDeviceTable=_KcprtMemoryDeviceTable_Object((1,3,6,1,4,1,1347,43,20,1))
if mibBuilder.loadTexts:kcprtMemoryDeviceTable.setStatus(_A)
_KcprtMemoryDeviceEntry_Object=MibTableRow
kcprtMemoryDeviceEntry=_KcprtMemoryDeviceEntry_Object((1,3,6,1,4,1,1347,43,20,1,1))
kcprtMemoryDeviceEntry.setIndexNames((0,_F,_G),(0,_E,_t))
if mibBuilder.loadTexts:kcprtMemoryDeviceEntry.setStatus(_A)
_KcprtMemoryDeviceIndex_Type=Integer32
_KcprtMemoryDeviceIndex_Object=MibTableColumn
kcprtMemoryDeviceIndex=_KcprtMemoryDeviceIndex_Object((1,3,6,1,4,1,1347,43,20,1,1,1),_KcprtMemoryDeviceIndex_Type())
kcprtMemoryDeviceIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtMemoryDeviceIndex.setStatus(_A)
class _KcprtMemoryDeviceLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,255)));namedValues=NamedValues(*(('pcCard-A',0),('pcCard-B',1),('optionROMsocket',2),('residentFont',3),('downloadArea',4),('hardDisk',5),('memoryCard',6),(_N,255)))
_KcprtMemoryDeviceLocation_Type.__name__=_C
_KcprtMemoryDeviceLocation_Object=MibTableColumn
kcprtMemoryDeviceLocation=_KcprtMemoryDeviceLocation_Object((1,3,6,1,4,1,1347,43,20,1,1,2),_KcprtMemoryDeviceLocation_Type())
kcprtMemoryDeviceLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMemoryDeviceLocation.setStatus(_A)
class _KcprtMemoryDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,255)));namedValues=NamedValues(*(('rom',0),('flash',1),('sram',2),('dram',3),('strage',4),(_N,255)))
_KcprtMemoryDeviceType_Type.__name__=_C
_KcprtMemoryDeviceType_Object=MibTableColumn
kcprtMemoryDeviceType=_KcprtMemoryDeviceType_Object((1,3,6,1,4,1,1347,43,20,1,1,3),_KcprtMemoryDeviceType_Type())
kcprtMemoryDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMemoryDeviceType.setStatus(_A)
_KcprtMemoryDeviceTotalSize_Type=Integer32
_KcprtMemoryDeviceTotalSize_Object=MibTableColumn
kcprtMemoryDeviceTotalSize=_KcprtMemoryDeviceTotalSize_Object((1,3,6,1,4,1,1347,43,20,1,1,4),_KcprtMemoryDeviceTotalSize_Type())
kcprtMemoryDeviceTotalSize.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtMemoryDeviceTotalSize.setStatus(_A)
_KcprtMemoryDeviceUsedSize_Type=Integer32
_KcprtMemoryDeviceUsedSize_Object=MibTableColumn
kcprtMemoryDeviceUsedSize=_KcprtMemoryDeviceUsedSize_Object((1,3,6,1,4,1,1347,43,20,1,1,5),_KcprtMemoryDeviceUsedSize_Type())
kcprtMemoryDeviceUsedSize.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMemoryDeviceUsedSize.setStatus(_A)
class _KcprtMemoryDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4)));namedValues=NamedValues(*(('readyReadWrite',0),('readyReadOnly',1),('notAccessible',2),('lowBattery',4)))
_KcprtMemoryDeviceStatus_Type.__name__=_C
_KcprtMemoryDeviceStatus_Object=MibTableColumn
kcprtMemoryDeviceStatus=_KcprtMemoryDeviceStatus_Object((1,3,6,1,4,1,1347,43,20,1,1,6),_KcprtMemoryDeviceStatus_Type())
kcprtMemoryDeviceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtMemoryDeviceStatus.setStatus(_A)
_KcprtMemoryDeviceUnit_Type=Integer32
_KcprtMemoryDeviceUnit_Object=MibTableColumn
kcprtMemoryDeviceUnit=_KcprtMemoryDeviceUnit_Object((1,3,6,1,4,1,1347,43,20,1,1,7),_KcprtMemoryDeviceUnit_Type())
kcprtMemoryDeviceUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMemoryDeviceUnit.setStatus(_A)
_KcprtPartitionTable_Object=MibTable
kcprtPartitionTable=_KcprtPartitionTable_Object((1,3,6,1,4,1,1347,43,20,2))
if mibBuilder.loadTexts:kcprtPartitionTable.setStatus(_A)
_KcprtPartitionEntry_Object=MibTableRow
kcprtPartitionEntry=_KcprtPartitionEntry_Object((1,3,6,1,4,1,1347,43,20,2,1))
kcprtPartitionEntry.setIndexNames((0,_F,_G),(0,_E,_u))
if mibBuilder.loadTexts:kcprtPartitionEntry.setStatus(_A)
_KcprtPartitionIndex_Type=Integer32
_KcprtPartitionIndex_Object=MibTableColumn
kcprtPartitionIndex=_KcprtPartitionIndex_Object((1,3,6,1,4,1,1347,43,20,2,1,1),_KcprtPartitionIndex_Type())
kcprtPartitionIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtPartitionIndex.setStatus(_A)
_KcprtPartitionSize_Type=Integer32
_KcprtPartitionSize_Object=MibTableColumn
kcprtPartitionSize=_KcprtPartitionSize_Object((1,3,6,1,4,1,1347,43,20,2,1,2),_KcprtPartitionSize_Type())
kcprtPartitionSize.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtPartitionSize.setStatus(_A)
_KcprtPartitionLocation_Type=Integer32
_KcprtPartitionLocation_Object=MibTableColumn
kcprtPartitionLocation=_KcprtPartitionLocation_Object((1,3,6,1,4,1,1347,43,20,2,1,3),_KcprtPartitionLocation_Type())
kcprtPartitionLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtPartitionLocation.setStatus(_A)
class _KcprtPartitionResourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,3,4,5,6,7)));namedValues=NamedValues(*(('void',0),('macro',3),('hostData',4),('programData',5),('messageData',6),('fontData',7)))
_KcprtPartitionResourceType_Type.__name__=_C
_KcprtPartitionResourceType_Object=MibTableColumn
kcprtPartitionResourceType=_KcprtPartitionResourceType_Object((1,3,6,1,4,1,1347,43,20,2,1,4),_KcprtPartitionResourceType_Type())
kcprtPartitionResourceType.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtPartitionResourceType.setStatus(_A)
class _KcprtPartitionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_KcprtPartitionName_Type.__name__=_H
_KcprtPartitionName_Object=MibTableColumn
kcprtPartitionName=_KcprtPartitionName_Object((1,3,6,1,4,1,1347,43,20,2,1,5),_KcprtPartitionName_Type())
kcprtPartitionName.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtPartitionName.setStatus(_A)
class _KcprtPartitionLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('notLoaded',0),('loaded',1)))
_KcprtPartitionLoad_Type.__name__=_C
_KcprtPartitionLoad_Object=MibTableColumn
kcprtPartitionLoad=_KcprtPartitionLoad_Object((1,3,6,1,4,1,1347,43,20,2,1,6),_KcprtPartitionLoad_Type())
kcprtPartitionLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtPartitionLoad.setStatus(_A)
_KcprtMacroDataTable_Object=MibTable
kcprtMacroDataTable=_KcprtMacroDataTable_Object((1,3,6,1,4,1,1347,43,20,3))
if mibBuilder.loadTexts:kcprtMacroDataTable.setStatus(_A)
_KcprtMacroDataEntry_Object=MibTableRow
kcprtMacroDataEntry=_KcprtMacroDataEntry_Object((1,3,6,1,4,1,1347,43,20,3,1))
kcprtMacroDataEntry.setIndexNames((0,_F,_G),(0,_E,_v))
if mibBuilder.loadTexts:kcprtMacroDataEntry.setStatus(_A)
_KcprtMacroDataIndex_Type=Integer32
_KcprtMacroDataIndex_Object=MibTableColumn
kcprtMacroDataIndex=_KcprtMacroDataIndex_Object((1,3,6,1,4,1,1347,43,20,3,1,1),_KcprtMacroDataIndex_Type())
kcprtMacroDataIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtMacroDataIndex.setStatus(_A)
class _KcprtMacroDataName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,4))
_KcprtMacroDataName_Type.__name__=_H
_KcprtMacroDataName_Object=MibTableColumn
kcprtMacroDataName=_KcprtMacroDataName_Object((1,3,6,1,4,1,1347,43,20,3,1,2),_KcprtMacroDataName_Type())
kcprtMacroDataName.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMacroDataName.setStatus(_A)
_KcprtMacroDataID_Type=Integer32
_KcprtMacroDataID_Object=MibTableColumn
kcprtMacroDataID=_KcprtMacroDataID_Object((1,3,6,1,4,1,1347,43,20,3,1,3),_KcprtMacroDataID_Type())
kcprtMacroDataID.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMacroDataID.setStatus(_A)
class _KcprtMacroDataType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_w,1),('pcl',2),(_N,255)))
_KcprtMacroDataType_Type.__name__=_C
_KcprtMacroDataType_Object=MibTableColumn
kcprtMacroDataType=_KcprtMacroDataType_Object((1,3,6,1,4,1,1347,43,20,3,1,4),_KcprtMacroDataType_Type())
kcprtMacroDataType.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMacroDataType.setStatus(_A)
class _KcprtMacroDataAutoLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('onWithInitialize',1),('onWithoutInitialize',2)))
_KcprtMacroDataAutoLoad_Type.__name__=_C
_KcprtMacroDataAutoLoad_Object=MibTableColumn
kcprtMacroDataAutoLoad=_KcprtMacroDataAutoLoad_Object((1,3,6,1,4,1,1347,43,20,3,1,5),_KcprtMacroDataAutoLoad_Type())
kcprtMacroDataAutoLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMacroDataAutoLoad.setStatus(_A)
_KcprtMacroDataLocation_Type=Integer32
_KcprtMacroDataLocation_Object=MibTableColumn
kcprtMacroDataLocation=_KcprtMacroDataLocation_Object((1,3,6,1,4,1,1347,43,20,3,1,6),_KcprtMacroDataLocation_Type())
kcprtMacroDataLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMacroDataLocation.setStatus(_A)
class _KcprtMacroDataAttribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_KcprtMacroDataAttribute_Type.__name__=_C
_KcprtMacroDataAttribute_Object=MibTableColumn
kcprtMacroDataAttribute=_KcprtMacroDataAttribute_Object((1,3,6,1,4,1,1347,43,20,3,1,7),_KcprtMacroDataAttribute_Type())
kcprtMacroDataAttribute.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMacroDataAttribute.setStatus(_A)
_KcprtHostDataTable_Object=MibTable
kcprtHostDataTable=_KcprtHostDataTable_Object((1,3,6,1,4,1,1347,43,20,4))
if mibBuilder.loadTexts:kcprtHostDataTable.setStatus(_A)
_KcprtHostDataEntry_Object=MibTableRow
kcprtHostDataEntry=_KcprtHostDataEntry_Object((1,3,6,1,4,1,1347,43,20,4,1))
kcprtHostDataEntry.setIndexNames((0,_F,_G),(0,_E,_x))
if mibBuilder.loadTexts:kcprtHostDataEntry.setStatus(_A)
_KcprtHostDataIndex_Type=Integer32
_KcprtHostDataIndex_Object=MibTableColumn
kcprtHostDataIndex=_KcprtHostDataIndex_Object((1,3,6,1,4,1,1347,43,20,4,1,1),_KcprtHostDataIndex_Type())
kcprtHostDataIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtHostDataIndex.setStatus(_A)
class _KcprtHostDataName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_KcprtHostDataName_Type.__name__=_H
_KcprtHostDataName_Object=MibTableColumn
kcprtHostDataName=_KcprtHostDataName_Object((1,3,6,1,4,1,1347,43,20,4,1,2),_KcprtHostDataName_Type())
kcprtHostDataName.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtHostDataName.setStatus(_A)
_KcprtHostDataLocation_Type=Integer32
_KcprtHostDataLocation_Object=MibTableColumn
kcprtHostDataLocation=_KcprtHostDataLocation_Object((1,3,6,1,4,1,1347,43,20,4,1,3),_KcprtHostDataLocation_Type())
kcprtHostDataLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtHostDataLocation.setStatus(_A)
class _KcprtHostDataAttribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_KcprtHostDataAttribute_Type.__name__=_C
_KcprtHostDataAttribute_Object=MibTableColumn
kcprtHostDataAttribute=_KcprtHostDataAttribute_Object((1,3,6,1,4,1,1347,43,20,4,1,4),_KcprtHostDataAttribute_Type())
kcprtHostDataAttribute.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtHostDataAttribute.setStatus(_A)
_KcprtProgramDataTable_Object=MibTable
kcprtProgramDataTable=_KcprtProgramDataTable_Object((1,3,6,1,4,1,1347,43,20,5))
if mibBuilder.loadTexts:kcprtProgramDataTable.setStatus(_A)
_KcprtProgramDataEntry_Object=MibTableRow
kcprtProgramDataEntry=_KcprtProgramDataEntry_Object((1,3,6,1,4,1,1347,43,20,5,1))
kcprtProgramDataEntry.setIndexNames((0,_F,_G),(0,_E,_y))
if mibBuilder.loadTexts:kcprtProgramDataEntry.setStatus(_A)
_KcprtProgramDataIndex_Type=Integer32
_KcprtProgramDataIndex_Object=MibTableColumn
kcprtProgramDataIndex=_KcprtProgramDataIndex_Object((1,3,6,1,4,1,1347,43,20,5,1,1),_KcprtProgramDataIndex_Type())
kcprtProgramDataIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtProgramDataIndex.setStatus(_A)
class _KcprtProgramDataName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_KcprtProgramDataName_Type.__name__=_H
_KcprtProgramDataName_Object=MibTableColumn
kcprtProgramDataName=_KcprtProgramDataName_Object((1,3,6,1,4,1,1347,43,20,5,1,2),_KcprtProgramDataName_Type())
kcprtProgramDataName.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtProgramDataName.setStatus(_A)
class _KcprtProgramDataType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,255)));namedValues=NamedValues(*(('emulation',0),(_w,1),('panel',2),(_N,255)))
_KcprtProgramDataType_Type.__name__=_C
_KcprtProgramDataType_Object=MibTableColumn
kcprtProgramDataType=_KcprtProgramDataType_Object((1,3,6,1,4,1,1347,43,20,5,1,3),_KcprtProgramDataType_Type())
kcprtProgramDataType.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtProgramDataType.setStatus(_A)
_KcprtProgramDataLocation_Type=Integer32
_KcprtProgramDataLocation_Object=MibTableColumn
kcprtProgramDataLocation=_KcprtProgramDataLocation_Object((1,3,6,1,4,1,1347,43,20,5,1,4),_KcprtProgramDataLocation_Type())
kcprtProgramDataLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtProgramDataLocation.setStatus(_A)
class _KcprtProgramDataAttribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_O,0),(_P,1),('running',2)))
_KcprtProgramDataAttribute_Type.__name__=_C
_KcprtProgramDataAttribute_Object=MibTableColumn
kcprtProgramDataAttribute=_KcprtProgramDataAttribute_Object((1,3,6,1,4,1,1347,43,20,5,1,5),_KcprtProgramDataAttribute_Type())
kcprtProgramDataAttribute.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtProgramDataAttribute.setStatus(_A)
_KcprtMessageDataTable_Object=MibTable
kcprtMessageDataTable=_KcprtMessageDataTable_Object((1,3,6,1,4,1,1347,43,20,6))
if mibBuilder.loadTexts:kcprtMessageDataTable.setStatus(_A)
_KcprtMessageDataEntry_Object=MibTableRow
kcprtMessageDataEntry=_KcprtMessageDataEntry_Object((1,3,6,1,4,1,1347,43,20,6,1))
kcprtMessageDataEntry.setIndexNames((0,_F,_G),(0,_E,_z))
if mibBuilder.loadTexts:kcprtMessageDataEntry.setStatus(_A)
_KcprtMessageDataIndex_Type=Integer32
_KcprtMessageDataIndex_Object=MibTableColumn
kcprtMessageDataIndex=_KcprtMessageDataIndex_Object((1,3,6,1,4,1,1347,43,20,6,1,1),_KcprtMessageDataIndex_Type())
kcprtMessageDataIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtMessageDataIndex.setStatus(_A)
class _KcprtMessageDataName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_KcprtMessageDataName_Type.__name__=_H
_KcprtMessageDataName_Object=MibTableColumn
kcprtMessageDataName=_KcprtMessageDataName_Object((1,3,6,1,4,1,1347,43,20,6,1,2),_KcprtMessageDataName_Type())
kcprtMessageDataName.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMessageDataName.setStatus(_A)
_KcprtMessageDataLocation_Type=Integer32
_KcprtMessageDataLocation_Object=MibTableColumn
kcprtMessageDataLocation=_KcprtMessageDataLocation_Object((1,3,6,1,4,1,1347,43,20,6,1,3),_KcprtMessageDataLocation_Type())
kcprtMessageDataLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMessageDataLocation.setStatus(_A)
class _KcprtMessageDataAttribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_KcprtMessageDataAttribute_Type.__name__=_C
_KcprtMessageDataAttribute_Object=MibTableColumn
kcprtMessageDataAttribute=_KcprtMessageDataAttribute_Object((1,3,6,1,4,1,1347,43,20,6,1,4),_KcprtMessageDataAttribute_Type())
kcprtMessageDataAttribute.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMessageDataAttribute.setStatus(_A)
_KcprtFontDataTable_Object=MibTable
kcprtFontDataTable=_KcprtFontDataTable_Object((1,3,6,1,4,1,1347,43,20,7))
if mibBuilder.loadTexts:kcprtFontDataTable.setStatus(_A)
_KcprtFontDataEntry_Object=MibTableRow
kcprtFontDataEntry=_KcprtFontDataEntry_Object((1,3,6,1,4,1,1347,43,20,7,1))
kcprtFontDataEntry.setIndexNames((0,_F,_G),(0,_E,_A0))
if mibBuilder.loadTexts:kcprtFontDataEntry.setStatus(_A)
_KcprtFontDataIndex_Type=Integer32
_KcprtFontDataIndex_Object=MibTableColumn
kcprtFontDataIndex=_KcprtFontDataIndex_Object((1,3,6,1,4,1,1347,43,20,7,1,1),_KcprtFontDataIndex_Type())
kcprtFontDataIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtFontDataIndex.setStatus(_A)
class _KcprtTypeFaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_KcprtTypeFaceName_Type.__name__=_H
_KcprtTypeFaceName_Object=MibTableColumn
kcprtTypeFaceName=_KcprtTypeFaceName_Object((1,3,6,1,4,1,1347,43,20,7,1,2),_KcprtTypeFaceName_Type())
kcprtTypeFaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtTypeFaceName.setStatus(_A)
_KcprtFontID_Type=Integer32
_KcprtFontID_Object=MibTableColumn
kcprtFontID=_KcprtFontID_Object((1,3,6,1,4,1,1347,43,20,7,1,3),_KcprtFontID_Type())
kcprtFontID.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtFontID.setStatus(_A)
class _KcprtFontType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,255)));namedValues=NamedValues(*(('bitmap',0),('scalable',1),(_N,255)))
_KcprtFontType_Type.__name__=_C
_KcprtFontType_Object=MibTableColumn
kcprtFontType=_KcprtFontType_Object((1,3,6,1,4,1,1347,43,20,7,1,4),_KcprtFontType_Type())
kcprtFontType.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtFontType.setStatus(_A)
_KcprtFontLocation_Type=Integer32
_KcprtFontLocation_Object=MibTableColumn
kcprtFontLocation=_KcprtFontLocation_Object((1,3,6,1,4,1,1347,43,20,7,1,5),_KcprtFontLocation_Type())
kcprtFontLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtFontLocation.setStatus(_A)
class _KcprtFontAttribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_O,0),(_P,1)))
_KcprtFontAttribute_Type.__name__=_C
_KcprtFontAttribute_Object=MibTableColumn
kcprtFontAttribute=_KcprtFontAttribute_Object((1,3,6,1,4,1,1347,43,20,7,1,6),_KcprtFontAttribute_Type())
kcprtFontAttribute.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtFontAttribute.setStatus(_A)
_KcprtFileStorageTable_Object=MibTable
kcprtFileStorageTable=_KcprtFileStorageTable_Object((1,3,6,1,4,1,1347,43,20,8))
if mibBuilder.loadTexts:kcprtFileStorageTable.setStatus(_A)
_KcprtFileStorageEntry_Object=MibTableRow
kcprtFileStorageEntry=_KcprtFileStorageEntry_Object((1,3,6,1,4,1,1347,43,20,8,1))
kcprtFileStorageEntry.setIndexNames((0,_F,_G),(0,_E,_A1))
if mibBuilder.loadTexts:kcprtFileStorageEntry.setStatus(_A)
_KcprtFileStorageIndex_Type=Integer32
_KcprtFileStorageIndex_Object=MibTableColumn
kcprtFileStorageIndex=_KcprtFileStorageIndex_Object((1,3,6,1,4,1,1347,43,20,8,1,1),_KcprtFileStorageIndex_Type())
kcprtFileStorageIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtFileStorageIndex.setStatus(_A)
_KcprtFileStorageLimitSize_Type=Integer32
_KcprtFileStorageLimitSize_Object=MibTableColumn
kcprtFileStorageLimitSize=_KcprtFileStorageLimitSize_Object((1,3,6,1,4,1,1347,43,20,8,1,2),_KcprtFileStorageLimitSize_Type())
kcprtFileStorageLimitSize.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtFileStorageLimitSize.setStatus(_A)
_KcprtFileStorageUsedSize_Type=Integer32
_KcprtFileStorageUsedSize_Object=MibTableColumn
kcprtFileStorageUsedSize=_KcprtFileStorageUsedSize_Object((1,3,6,1,4,1,1347,43,20,8,1,3),_KcprtFileStorageUsedSize_Type())
kcprtFileStorageUsedSize.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtFileStorageUsedSize.setStatus(_A)
_KcprtFileStorageUnit_Type=Integer32
_KcprtFileStorageUnit_Object=MibTableColumn
kcprtFileStorageUnit=_KcprtFileStorageUnit_Object((1,3,6,1,4,1,1347,43,20,8,1,4),_KcprtFileStorageUnit_Type())
kcprtFileStorageUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtFileStorageUnit.setStatus(_A)
class _KcprtFileStorageCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtFileStorageCounter_Type.__name__=_C
_KcprtFileStorageCounter_Object=MibTableColumn
kcprtFileStorageCounter=_KcprtFileStorageCounter_Object((1,3,6,1,4,1,1347,43,20,8,1,5),_KcprtFileStorageCounter_Type())
kcprtFileStorageCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtFileStorageCounter.setStatus(_A)
_KcprtFileTable_Object=MibTable
kcprtFileTable=_KcprtFileTable_Object((1,3,6,1,4,1,1347,43,20,9))
if mibBuilder.loadTexts:kcprtFileTable.setStatus(_A)
_KcprtFileEntry_Object=MibTableRow
kcprtFileEntry=_KcprtFileEntry_Object((1,3,6,1,4,1,1347,43,20,9,1))
kcprtFileEntry.setIndexNames((0,_F,_G),(0,_E,_A2))
if mibBuilder.loadTexts:kcprtFileEntry.setStatus(_A)
_KcprtFileIndex_Type=Integer32
_KcprtFileIndex_Object=MibTableColumn
kcprtFileIndex=_KcprtFileIndex_Object((1,3,6,1,4,1,1347,43,20,9,1,1),_KcprtFileIndex_Type())
kcprtFileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtFileIndex.setStatus(_A)
class _KcprtFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_KcprtFileName_Type.__name__=_K
_KcprtFileName_Object=MibTableColumn
kcprtFileName=_KcprtFileName_Object((1,3,6,1,4,1,1347,43,20,9,1,2),_KcprtFileName_Type())
kcprtFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtFileName.setStatus(_A)
_KcprtFileSize_Type=Integer32
_KcprtFileSize_Object=MibTableColumn
kcprtFileSize=_KcprtFileSize_Object((1,3,6,1,4,1,1347,43,20,9,1,3),_KcprtFileSize_Type())
kcprtFileSize.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtFileSize.setStatus(_A)
_KcprtSJobStorageTable_Object=MibTable
kcprtSJobStorageTable=_KcprtSJobStorageTable_Object((1,3,6,1,4,1,1347,43,20,10))
if mibBuilder.loadTexts:kcprtSJobStorageTable.setStatus(_A)
_KcprtSJobStorageEntry_Object=MibTableRow
kcprtSJobStorageEntry=_KcprtSJobStorageEntry_Object((1,3,6,1,4,1,1347,43,20,10,1))
kcprtSJobStorageEntry.setIndexNames((0,_F,_G),(0,_E,_A3))
if mibBuilder.loadTexts:kcprtSJobStorageEntry.setStatus(_A)
_KcprtSJobStorageIndex_Type=Integer32
_KcprtSJobStorageIndex_Object=MibTableColumn
kcprtSJobStorageIndex=_KcprtSJobStorageIndex_Object((1,3,6,1,4,1,1347,43,20,10,1,1),_KcprtSJobStorageIndex_Type())
kcprtSJobStorageIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtSJobStorageIndex.setStatus(_A)
_KcprtSJobStorageLimitSize_Type=Integer32
_KcprtSJobStorageLimitSize_Object=MibTableColumn
kcprtSJobStorageLimitSize=_KcprtSJobStorageLimitSize_Object((1,3,6,1,4,1,1347,43,20,10,1,2),_KcprtSJobStorageLimitSize_Type())
kcprtSJobStorageLimitSize.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobStorageLimitSize.setStatus(_A)
_KcprtSJobStorageUsedSize_Type=Integer32
_KcprtSJobStorageUsedSize_Object=MibTableColumn
kcprtSJobStorageUsedSize=_KcprtSJobStorageUsedSize_Object((1,3,6,1,4,1,1347,43,20,10,1,3),_KcprtSJobStorageUsedSize_Type())
kcprtSJobStorageUsedSize.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobStorageUsedSize.setStatus(_A)
_KcprtSJobStorageUnit_Type=Integer32
_KcprtSJobStorageUnit_Object=MibTableColumn
kcprtSJobStorageUnit=_KcprtSJobStorageUnit_Object((1,3,6,1,4,1,1347,43,20,10,1,4),_KcprtSJobStorageUnit_Type())
kcprtSJobStorageUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobStorageUnit.setStatus(_A)
class _KcprtSJobStorageStateCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtSJobStorageStateCounter_Type.__name__=_C
_KcprtSJobStorageStateCounter_Object=MibTableColumn
kcprtSJobStorageStateCounter=_KcprtSJobStorageStateCounter_Object((1,3,6,1,4,1,1347,43,20,10,1,5),_KcprtSJobStorageStateCounter_Type())
kcprtSJobStorageStateCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobStorageStateCounter.setStatus(_A)
class _KcprtSJobStorageAttribute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('volatile',1),('nonVolatile',2),(_S,255)))
_KcprtSJobStorageAttribute_Type.__name__=_C
_KcprtSJobStorageAttribute_Object=MibTableColumn
kcprtSJobStorageAttribute=_KcprtSJobStorageAttribute_Object((1,3,6,1,4,1,1347,43,20,10,1,6),_KcprtSJobStorageAttribute_Type())
kcprtSJobStorageAttribute.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobStorageAttribute.setStatus(_A)
_KcprtSJobTable_Object=MibTable
kcprtSJobTable=_KcprtSJobTable_Object((1,3,6,1,4,1,1347,43,20,11))
if mibBuilder.loadTexts:kcprtSJobTable.setStatus(_A)
_KcprtSJobEntry_Object=MibTableRow
kcprtSJobEntry=_KcprtSJobEntry_Object((1,3,6,1,4,1,1347,43,20,11,1))
kcprtSJobEntry.setIndexNames((0,_F,_G),(0,_E,_A4))
if mibBuilder.loadTexts:kcprtSJobEntry.setStatus(_A)
_KcprtSJobIndex_Type=Integer32
_KcprtSJobIndex_Object=MibTableColumn
kcprtSJobIndex=_KcprtSJobIndex_Object((1,3,6,1,4,1,1347,43,20,11,1,1),_KcprtSJobIndex_Type())
kcprtSJobIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtSJobIndex.setStatus(_A)
class _KcprtSjobID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_KcprtSjobID_Type.__name__=_H
_KcprtSjobID_Object=MibTableColumn
kcprtSjobID=_KcprtSjobID_Object((1,3,6,1,4,1,1347,43,20,11,1,2),_KcprtSjobID_Type())
kcprtSjobID.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSjobID.setStatus(_A)
class _KcprtSJobName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_KcprtSJobName_Type.__name__=_H
_KcprtSJobName_Object=MibTableColumn
kcprtSJobName=_KcprtSJobName_Object((1,3,6,1,4,1,1347,43,20,11,1,3),_KcprtSJobName_Type())
kcprtSJobName.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobName.setStatus(_A)
class _KcprtSJobOwner_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_KcprtSJobOwner_Type.__name__=_H
_KcprtSJobOwner_Object=MibTableColumn
kcprtSJobOwner=_KcprtSJobOwner_Object((1,3,6,1,4,1,1347,43,20,11,1,4),_KcprtSJobOwner_Type())
kcprtSJobOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobOwner.setStatus(_A)
class _KcprtSJobTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_KcprtSJobTime_Type.__name__=_H
_KcprtSJobTime_Object=MibTableColumn
kcprtSJobTime=_KcprtSJobTime_Object((1,3,6,1,4,1,1347,43,20,11,1,5),_KcprtSJobTime_Type())
kcprtSJobTime.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobTime.setStatus(_A)
_KcprtSJobPageNumber_Type=Integer32
_KcprtSJobPageNumber_Object=MibTableColumn
kcprtSJobPageNumber=_KcprtSJobPageNumber_Object((1,3,6,1,4,1,1347,43,20,11,1,6),_KcprtSJobPageNumber_Type())
kcprtSJobPageNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobPageNumber.setStatus(_A)
class _KcprtSJobSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtSJobSize_Type.__name__=_C
_KcprtSJobSize_Object=MibTableColumn
kcprtSJobSize=_KcprtSJobSize_Object((1,3,6,1,4,1,1347,43,20,11,1,7),_KcprtSJobSize_Type())
kcprtSJobSize.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobSize.setStatus(_A)
_KcprtSJobStorageRef_Type=Integer32
_KcprtSJobStorageRef_Object=MibTableColumn
kcprtSJobStorageRef=_KcprtSJobStorageRef_Object((1,3,6,1,4,1,1347,43,20,11,1,8),_KcprtSJobStorageRef_Type())
kcprtSJobStorageRef.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobStorageRef.setStatus(_A)
_KcprtSJobCopyCount_Type=Integer32
_KcprtSJobCopyCount_Object=MibTableColumn
kcprtSJobCopyCount=_KcprtSJobCopyCount_Object((1,3,6,1,4,1,1347,43,20,11,1,9),_KcprtSJobCopyCount_Type())
kcprtSJobCopyCount.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobCopyCount.setStatus(_A)
class _KcprtSJobBarcodePrintExistence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('notPrinting',0),('firstPagePrinting',1),('allPagePrinting',2)))
_KcprtSJobBarcodePrintExistence_Type.__name__=_C
_KcprtSJobBarcodePrintExistence_Object=MibTableColumn
kcprtSJobBarcodePrintExistence=_KcprtSJobBarcodePrintExistence_Object((1,3,6,1,4,1,1347,43,20,11,1,10),_KcprtSJobBarcodePrintExistence_Type())
kcprtSJobBarcodePrintExistence.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobBarcodePrintExistence.setStatus(_A)
class _KcprtSJobDuplexMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5)));namedValues=NamedValues(*(('shortEdgeBindingDuplex',3),('longEdgeBindingDuplex',4),('simplex',5)))
_KcprtSJobDuplexMode_Type.__name__=_C
_KcprtSJobDuplexMode_Object=MibTableColumn
kcprtSJobDuplexMode=_KcprtSJobDuplexMode_Object((1,3,6,1,4,1,1347,43,20,11,1,11),_KcprtSJobDuplexMode_Type())
kcprtSJobDuplexMode.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobDuplexMode.setStatus(_A)
_KcprtSJobOutputIndex_Type=Integer32
_KcprtSJobOutputIndex_Object=MibTableColumn
kcprtSJobOutputIndex=_KcprtSJobOutputIndex_Object((1,3,6,1,4,1,1347,43,20,11,1,12),_KcprtSJobOutputIndex_Type())
kcprtSJobOutputIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobOutputIndex.setStatus(_A)
class _KcprtSJobStaplePosition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_J,0),('oneFrontLocation',1),('oneRearLocation',2),('twoCentralLocation',3)))
_KcprtSJobStaplePosition_Type.__name__=_C
_KcprtSJobStaplePosition_Object=MibTableColumn
kcprtSJobStaplePosition=_KcprtSJobStaplePosition_Object((1,3,6,1,4,1,1347,43,20,11,1,13),_KcprtSJobStaplePosition_Type())
kcprtSJobStaplePosition.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobStaplePosition.setStatus(_A)
_KcprtSJobBarcodePosition_Type=Integer32
_KcprtSJobBarcodePosition_Object=MibTableColumn
kcprtSJobBarcodePosition=_KcprtSJobBarcodePosition_Object((1,3,6,1,4,1,1347,43,20,11,1,14),_KcprtSJobBarcodePosition_Type())
kcprtSJobBarcodePosition.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobBarcodePosition.setStatus(_A)
_KcprtSJobStapleAndFoldCount_Type=Integer32
_KcprtSJobStapleAndFoldCount_Object=MibTableColumn
kcprtSJobStapleAndFoldCount=_KcprtSJobStapleAndFoldCount_Object((1,3,6,1,4,1,1347,43,20,11,1,15),_KcprtSJobStapleAndFoldCount_Type())
kcprtSJobStapleAndFoldCount.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobStapleAndFoldCount.setStatus(_A)
class _KcprtSJobFoldMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),('foldandStaple',1)))
_KcprtSJobFoldMode_Type.__name__=_C
_KcprtSJobFoldMode_Object=MibTableColumn
kcprtSJobFoldMode=_KcprtSJobFoldMode_Object((1,3,6,1,4,1,1347,43,20,11,1,16),_KcprtSJobFoldMode_Type())
kcprtSJobFoldMode.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobFoldMode.setStatus(_A)
class _KcprtSJobPunchMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('main',1),('sub',2)))
_KcprtSJobPunchMode_Type.__name__=_C
_KcprtSJobPunchMode_Object=MibTableColumn
kcprtSJobPunchMode=_KcprtSJobPunchMode_Object((1,3,6,1,4,1,1347,43,20,11,1,17),_KcprtSJobPunchMode_Type())
kcprtSJobPunchMode.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobPunchMode.setStatus(_A)
class _KcprtSJobTransparencySeparationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('blankPaperIjnterReef',1),('copySheetInterReef',2)))
_KcprtSJobTransparencySeparationMode_Type.__name__=_C
_KcprtSJobTransparencySeparationMode_Object=MibTableColumn
kcprtSJobTransparencySeparationMode=_KcprtSJobTransparencySeparationMode_Object((1,3,6,1,4,1,1347,43,20,11,1,18),_KcprtSJobTransparencySeparationMode_Type())
kcprtSJobTransparencySeparationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobTransparencySeparationMode.setStatus(_A)
_KcprtSJobTransparencySeparationInputIndex_Type=Integer32
_KcprtSJobTransparencySeparationInputIndex_Object=MibTableColumn
kcprtSJobTransparencySeparationInputIndex=_KcprtSJobTransparencySeparationInputIndex_Object((1,3,6,1,4,1,1347,43,20,11,1,19),_KcprtSJobTransparencySeparationInputIndex_Type())
kcprtSJobTransparencySeparationInputIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobTransparencySeparationInputIndex.setStatus(_A)
class _KcprtSJobRotatedCollationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_M,1)))
_KcprtSJobRotatedCollationMode_Type.__name__=_C
_KcprtSJobRotatedCollationMode_Object=MibTableColumn
kcprtSJobRotatedCollationMode=_KcprtSJobRotatedCollationMode_Object((1,3,6,1,4,1,1347,43,20,11,1,20),_KcprtSJobRotatedCollationMode_Type())
kcprtSJobRotatedCollationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobRotatedCollationMode.setStatus(_A)
class _KcprtSJobBookletMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('leftBinding',1),('rightBinding',2)))
_KcprtSJobBookletMode_Type.__name__=_C
_KcprtSJobBookletMode_Object=MibTableColumn
kcprtSJobBookletMode=_KcprtSJobBookletMode_Object((1,3,6,1,4,1,1347,43,20,11,1,21),_KcprtSJobBookletMode_Type())
kcprtSJobBookletMode.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobBookletMode.setStatus(_A)
class _KcprtSJobJobOffsetMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_M,1)))
_KcprtSJobJobOffsetMode_Type.__name__=_C
_KcprtSJobJobOffsetMode_Object=MibTableColumn
kcprtSJobJobOffsetMode=_KcprtSJobJobOffsetMode_Object((1,3,6,1,4,1,1347,43,20,11,1,22),_KcprtSJobJobOffsetMode_Type())
kcprtSJobJobOffsetMode.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSJobJobOffsetMode.setStatus(_A)
_KcprtMediaList_ObjectIdentity=ObjectIdentity
kcprtMediaList=_KcprtMediaList_ObjectIdentity((1,3,6,1,4,1,1347,43,21))
_KcprtMediaTable_Object=MibTable
kcprtMediaTable=_KcprtMediaTable_Object((1,3,6,1,4,1,1347,43,21,1))
if mibBuilder.loadTexts:kcprtMediaTable.setStatus(_A)
_KcprtMediaEntry_Object=MibTableRow
kcprtMediaEntry=_KcprtMediaEntry_Object((1,3,6,1,4,1,1347,43,21,1,1))
kcprtMediaEntry.setIndexNames((0,_F,_G),(0,_E,_A5))
if mibBuilder.loadTexts:kcprtMediaEntry.setStatus(_A)
_KcprtMediaIndex_Type=Integer32
_KcprtMediaIndex_Object=MibTableColumn
kcprtMediaIndex=_KcprtMediaIndex_Object((1,3,6,1,4,1,1347,43,21,1,1,1),_KcprtMediaIndex_Type())
kcprtMediaIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtMediaIndex.setStatus(_A)
class _KcprtMediaName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_KcprtMediaName_Type.__name__=_H
_KcprtMediaName_Object=MibTableColumn
kcprtMediaName=_KcprtMediaName_Object((1,3,6,1,4,1,1347,43,21,1,1,2),_KcprtMediaName_Type())
kcprtMediaName.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtMediaName.setStatus(_A)
class _KcprtMediaWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Q,0),('heavy',1),(_W,2),('extraheavy',3)))
_KcprtMediaWeight_Type.__name__=_C
_KcprtMediaWeight_Object=MibTableColumn
kcprtMediaWeight=_KcprtMediaWeight_Object((1,3,6,1,4,1,1347,43,21,1,1,3),_KcprtMediaWeight_Type())
kcprtMediaWeight.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtMediaWeight.setStatus(_A)
class _KcprtMediaFuserMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('high',0),('middle',1),('low',2),('vellum',3)))
_KcprtMediaFuserMode_Type.__name__=_C
_KcprtMediaFuserMode_Object=MibTableColumn
kcprtMediaFuserMode=_KcprtMediaFuserMode_Object((1,3,6,1,4,1,1347,43,21,1,1,4),_KcprtMediaFuserMode_Type())
kcprtMediaFuserMode.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtMediaFuserMode.setStatus(_A)
class _KcprtMediaPathType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_b,0),(_a,1)))
_KcprtMediaPathType_Type.__name__=_C
_KcprtMediaPathType_Object=MibTableColumn
kcprtMediaPathType=_KcprtMediaPathType_Object((1,3,6,1,4,1,1347,43,21,1,1,5),_KcprtMediaPathType_Type())
kcprtMediaPathType.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtMediaPathType.setStatus(_A)
_KcprtMediaDensity_Type=Integer32
_KcprtMediaDensity_Object=MibTableColumn
kcprtMediaDensity=_KcprtMediaDensity_Object((1,3,6,1,4,1,1347,43,21,1,1,6),_KcprtMediaDensity_Type())
kcprtMediaDensity.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtMediaDensity.setStatus(_A)
class _KcprtMediaManageLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,15)));namedValues=NamedValues(*((_d,0),(_U,15)))
_KcprtMediaManageLevel_Type.__name__=_C
_KcprtMediaManageLevel_Object=MibTableColumn
kcprtMediaManageLevel=_KcprtMediaManageLevel_Object((1,3,6,1,4,1,1347,43,21,1,1,7),_KcprtMediaManageLevel_Type())
kcprtMediaManageLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMediaManageLevel.setStatus(_A)
_KcprtMailBox_ObjectIdentity=ObjectIdentity
kcprtMailBox=_KcprtMailBox_ObjectIdentity((1,3,6,1,4,1,1347,43,22))
_KcprtMailBoxTable_Object=MibTable
kcprtMailBoxTable=_KcprtMailBoxTable_Object((1,3,6,1,4,1,1347,43,22,1))
if mibBuilder.loadTexts:kcprtMailBoxTable.setStatus(_A)
_KcprtMailBoxEntry_Object=MibTableRow
kcprtMailBoxEntry=_KcprtMailBoxEntry_Object((1,3,6,1,4,1,1347,43,22,1,1))
kcprtMailBoxEntry.setIndexNames((0,_F,_G),(0,_E,_T))
if mibBuilder.loadTexts:kcprtMailBoxEntry.setStatus(_A)
_KcprtMailBoxIndex_Type=Integer32
_KcprtMailBoxIndex_Object=MibTableColumn
kcprtMailBoxIndex=_KcprtMailBoxIndex_Object((1,3,6,1,4,1,1347,43,22,1,1,1),_KcprtMailBoxIndex_Type())
kcprtMailBoxIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtMailBoxIndex.setStatus(_A)
_KcprtMailBoxDeviceIndex_Type=Integer32
_KcprtMailBoxDeviceIndex_Object=MibTableColumn
kcprtMailBoxDeviceIndex=_KcprtMailBoxDeviceIndex_Object((1,3,6,1,4,1,1347,43,22,1,1,2),_KcprtMailBoxDeviceIndex_Type())
kcprtMailBoxDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMailBoxDeviceIndex.setStatus(_A)
class _KcprtMailBoxStateCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtMailBoxStateCounter_Type.__name__=_C
_KcprtMailBoxStateCounter_Object=MibTableColumn
kcprtMailBoxStateCounter=_KcprtMailBoxStateCounter_Object((1,3,6,1,4,1,1347,43,22,1,1,3),_KcprtMailBoxStateCounter_Type())
kcprtMailBoxStateCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMailBoxStateCounter.setStatus(_A)
class _KcprtMailBoxUsedTrays_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_KcprtMailBoxUsedTrays_Type.__name__=_C
_KcprtMailBoxUsedTrays_Object=MibTableColumn
kcprtMailBoxUsedTrays=_KcprtMailBoxUsedTrays_Object((1,3,6,1,4,1,1347,43,22,1,1,4),_KcprtMailBoxUsedTrays_Type())
kcprtMailBoxUsedTrays.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMailBoxUsedTrays.setStatus(_A)
class _KcprtMailBoxDocumentsNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtMailBoxDocumentsNumber_Type.__name__=_C
_KcprtMailBoxDocumentsNumber_Object=MibTableColumn
kcprtMailBoxDocumentsNumber=_KcprtMailBoxDocumentsNumber_Object((1,3,6,1,4,1,1347,43,22,1,1,5),_KcprtMailBoxDocumentsNumber_Type())
kcprtMailBoxDocumentsNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMailBoxDocumentsNumber.setStatus(_A)
class _KcprtMailBoxPageNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtMailBoxPageNumber_Type.__name__=_C
_KcprtMailBoxPageNumber_Object=MibTableColumn
kcprtMailBoxPageNumber=_KcprtMailBoxPageNumber_Object((1,3,6,1,4,1,1347,43,22,1,1,6),_KcprtMailBoxPageNumber_Type())
kcprtMailBoxPageNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMailBoxPageNumber.setStatus(_A)
class _KcprtMailBoxUsedSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtMailBoxUsedSize_Type.__name__=_C
_KcprtMailBoxUsedSize_Object=MibTableColumn
kcprtMailBoxUsedSize=_KcprtMailBoxUsedSize_Object((1,3,6,1,4,1,1347,43,22,1,1,7),_KcprtMailBoxUsedSize_Type())
kcprtMailBoxUsedSize.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMailBoxUsedSize.setStatus(_A)
class _KcprtMailBoxLimitSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtMailBoxLimitSize_Type.__name__=_C
_KcprtMailBoxLimitSize_Object=MibTableColumn
kcprtMailBoxLimitSize=_KcprtMailBoxLimitSize_Object((1,3,6,1,4,1,1347,43,22,1,1,8),_KcprtMailBoxLimitSize_Type())
kcprtMailBoxLimitSize.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtMailBoxLimitSize.setStatus(_A)
class _KcprtMailBoxMaxLimitSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtMailBoxMaxLimitSize_Type.__name__=_C
_KcprtMailBoxMaxLimitSize_Object=MibTableColumn
kcprtMailBoxMaxLimitSize=_KcprtMailBoxMaxLimitSize_Object((1,3,6,1,4,1,1347,43,22,1,1,9),_KcprtMailBoxMaxLimitSize_Type())
kcprtMailBoxMaxLimitSize.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMailBoxMaxLimitSize.setStatus(_A)
_KcprtMailBoxUnit_Type=Integer32
_KcprtMailBoxUnit_Object=MibTableColumn
kcprtMailBoxUnit=_KcprtMailBoxUnit_Object((1,3,6,1,4,1,1347,43,22,1,1,10),_KcprtMailBoxUnit_Type())
kcprtMailBoxUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMailBoxUnit.setStatus(_A)
class _KcprtMailBoxAliasCheck_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_KcprtMailBoxAliasCheck_Type.__name__=_H
_KcprtMailBoxAliasCheck_Object=MibTableColumn
kcprtMailBoxAliasCheck=_KcprtMailBoxAliasCheck_Object((1,3,6,1,4,1,1347,43,22,1,1,11),_KcprtMailBoxAliasCheck_Type())
kcprtMailBoxAliasCheck.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtMailBoxAliasCheck.setStatus(_A)
_KcprtMailBoxTrayTable_Object=MibTable
kcprtMailBoxTrayTable=_KcprtMailBoxTrayTable_Object((1,3,6,1,4,1,1347,43,22,2))
if mibBuilder.loadTexts:kcprtMailBoxTrayTable.setStatus(_A)
_KcprtMailBoxTrayEntry_Object=MibTableRow
kcprtMailBoxTrayEntry=_KcprtMailBoxTrayEntry_Object((1,3,6,1,4,1,1347,43,22,2,1))
kcprtMailBoxTrayEntry.setIndexNames((0,_F,_G),(0,_E,_T),(0,_E,_X))
if mibBuilder.loadTexts:kcprtMailBoxTrayEntry.setStatus(_A)
_KcprtMailBoxTrayIndex_Type=Integer32
_KcprtMailBoxTrayIndex_Object=MibTableColumn
kcprtMailBoxTrayIndex=_KcprtMailBoxTrayIndex_Object((1,3,6,1,4,1,1347,43,22,2,1,1),_KcprtMailBoxTrayIndex_Type())
kcprtMailBoxTrayIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtMailBoxTrayIndex.setStatus(_A)
class _KcprtMailBoxTrayUsedFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,255)));namedValues=NamedValues(*(('notUsed',0),('used',1),(_S,255)))
_KcprtMailBoxTrayUsedFlag_Type.__name__=_C
_KcprtMailBoxTrayUsedFlag_Object=MibTableColumn
kcprtMailBoxTrayUsedFlag=_KcprtMailBoxTrayUsedFlag_Object((1,3,6,1,4,1,1347,43,22,2,1,2),_KcprtMailBoxTrayUsedFlag_Type())
kcprtMailBoxTrayUsedFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMailBoxTrayUsedFlag.setStatus(_A)
class _KcprtMailBoxTrayLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_KcprtMailBoxTrayLabel_Type.__name__=_H
_KcprtMailBoxTrayLabel_Object=MibTableColumn
kcprtMailBoxTrayLabel=_KcprtMailBoxTrayLabel_Object((1,3,6,1,4,1,1347,43,22,2,1,3),_KcprtMailBoxTrayLabel_Type())
kcprtMailBoxTrayLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtMailBoxTrayLabel.setStatus(_A)
class _KcprtMailBoxTrayLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,255)));namedValues=NamedValues(*(('unlock',0),('lock',1),(_S,255)))
_KcprtMailBoxTrayLock_Type.__name__=_C
_KcprtMailBoxTrayLock_Object=MibTableColumn
kcprtMailBoxTrayLock=_KcprtMailBoxTrayLock_Object((1,3,6,1,4,1,1347,43,22,2,1,4),_KcprtMailBoxTrayLock_Type())
kcprtMailBoxTrayLock.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMailBoxTrayLock.setStatus(_A)
class _KcprtMailBoxTrayDocumentsNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtMailBoxTrayDocumentsNumber_Type.__name__=_C
_KcprtMailBoxTrayDocumentsNumber_Object=MibTableColumn
kcprtMailBoxTrayDocumentsNumber=_KcprtMailBoxTrayDocumentsNumber_Object((1,3,6,1,4,1,1347,43,22,2,1,5),_KcprtMailBoxTrayDocumentsNumber_Type())
kcprtMailBoxTrayDocumentsNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMailBoxTrayDocumentsNumber.setStatus(_A)
class _KcprtMailBoxTrayPageNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtMailBoxTrayPageNumber_Type.__name__=_C
_KcprtMailBoxTrayPageNumber_Object=MibTableColumn
kcprtMailBoxTrayPageNumber=_KcprtMailBoxTrayPageNumber_Object((1,3,6,1,4,1,1347,43,22,2,1,6),_KcprtMailBoxTrayPageNumber_Type())
kcprtMailBoxTrayPageNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMailBoxTrayPageNumber.setStatus(_A)
class _KcprtMailBoxTrayOccupiedSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtMailBoxTrayOccupiedSize_Type.__name__=_C
_KcprtMailBoxTrayOccupiedSize_Object=MibTableColumn
kcprtMailBoxTrayOccupiedSize=_KcprtMailBoxTrayOccupiedSize_Object((1,3,6,1,4,1,1347,43,22,2,1,7),_KcprtMailBoxTrayOccupiedSize_Type())
kcprtMailBoxTrayOccupiedSize.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMailBoxTrayOccupiedSize.setStatus(_A)
class _KcprtMailBoxTraySharedSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtMailBoxTraySharedSize_Type.__name__=_C
_KcprtMailBoxTraySharedSize_Object=MibTableColumn
kcprtMailBoxTraySharedSize=_KcprtMailBoxTraySharedSize_Object((1,3,6,1,4,1,1347,43,22,2,1,8),_KcprtMailBoxTraySharedSize_Type())
kcprtMailBoxTraySharedSize.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMailBoxTraySharedSize.setStatus(_A)
class _KcprtMailBoxTrayErrorLogNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtMailBoxTrayErrorLogNumber_Type.__name__=_C
_KcprtMailBoxTrayErrorLogNumber_Object=MibTableColumn
kcprtMailBoxTrayErrorLogNumber=_KcprtMailBoxTrayErrorLogNumber_Object((1,3,6,1,4,1,1347,43,22,2,1,9),_KcprtMailBoxTrayErrorLogNumber_Type())
kcprtMailBoxTrayErrorLogNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtMailBoxTrayErrorLogNumber.setStatus(_A)
class _KcprtMailBoxTrayPurgeDocuments_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtMailBoxTrayPurgeDocuments_Type.__name__=_C
_KcprtMailBoxTrayPurgeDocuments_Object=MibTableColumn
kcprtMailBoxTrayPurgeDocuments=_KcprtMailBoxTrayPurgeDocuments_Object((1,3,6,1,4,1,1347,43,22,2,1,10),_KcprtMailBoxTrayPurgeDocuments_Type())
kcprtMailBoxTrayPurgeDocuments.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtMailBoxTrayPurgeDocuments.setStatus(_A)
class _KcprtMailBoxTrayReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtMailBoxTrayReset_Type.__name__=_C
_KcprtMailBoxTrayReset_Object=MibTableColumn
kcprtMailBoxTrayReset=_KcprtMailBoxTrayReset_Object((1,3,6,1,4,1,1347,43,22,2,1,11),_KcprtMailBoxTrayReset_Type())
kcprtMailBoxTrayReset.setMaxAccess(_D)
if mibBuilder.loadTexts:kcprtMailBoxTrayReset.setStatus(_A)
_KcprtTrayJobTable_Object=MibTable
kcprtTrayJobTable=_KcprtTrayJobTable_Object((1,3,6,1,4,1,1347,43,22,3))
if mibBuilder.loadTexts:kcprtTrayJobTable.setStatus(_A)
_KcprtTrayJobEntry_Object=MibTableRow
kcprtTrayJobEntry=_KcprtTrayJobEntry_Object((1,3,6,1,4,1,1347,43,22,3,1))
kcprtTrayJobEntry.setIndexNames((0,_F,_G),(0,_E,_T),(0,_E,_X),(0,_E,_A6))
if mibBuilder.loadTexts:kcprtTrayJobEntry.setStatus(_A)
_KcprtTrayJobIndex_Type=Integer32
_KcprtTrayJobIndex_Object=MibTableColumn
kcprtTrayJobIndex=_KcprtTrayJobIndex_Object((1,3,6,1,4,1,1347,43,22,3,1,1),_KcprtTrayJobIndex_Type())
kcprtTrayJobIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtTrayJobIndex.setStatus(_A)
class _KcprtTrayJobID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_KcprtTrayJobID_Type.__name__=_H
_KcprtTrayJobID_Object=MibTableColumn
kcprtTrayJobID=_KcprtTrayJobID_Object((1,3,6,1,4,1,1347,43,22,3,1,2),_KcprtTrayJobID_Type())
kcprtTrayJobID.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtTrayJobID.setStatus(_A)
class _KcprtTrayJobName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_KcprtTrayJobName_Type.__name__=_H
_KcprtTrayJobName_Object=MibTableColumn
kcprtTrayJobName=_KcprtTrayJobName_Object((1,3,6,1,4,1,1347,43,22,3,1,3),_KcprtTrayJobName_Type())
kcprtTrayJobName.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtTrayJobName.setStatus(_A)
class _KcprtTrayJobOwner_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_KcprtTrayJobOwner_Type.__name__=_H
_KcprtTrayJobOwner_Object=MibTableColumn
kcprtTrayJobOwner=_KcprtTrayJobOwner_Object((1,3,6,1,4,1,1347,43,22,3,1,4),_KcprtTrayJobOwner_Type())
kcprtTrayJobOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtTrayJobOwner.setStatus(_A)
class _KcprtTrayJobTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_KcprtTrayJobTime_Type.__name__=_H
_KcprtTrayJobTime_Object=MibTableColumn
kcprtTrayJobTime=_KcprtTrayJobTime_Object((1,3,6,1,4,1,1347,43,22,3,1,5),_KcprtTrayJobTime_Type())
kcprtTrayJobTime.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtTrayJobTime.setStatus(_A)
class _KcprtTrayJobPageNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtTrayJobPageNumber_Type.__name__=_C
_KcprtTrayJobPageNumber_Object=MibTableColumn
kcprtTrayJobPageNumber=_KcprtTrayJobPageNumber_Object((1,3,6,1,4,1,1347,43,22,3,1,6),_KcprtTrayJobPageNumber_Type())
kcprtTrayJobPageNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtTrayJobPageNumber.setStatus(_A)
class _KcprtTrayJobSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_KcprtTrayJobSize_Type.__name__=_C
_KcprtTrayJobSize_Object=MibTableColumn
kcprtTrayJobSize=_KcprtTrayJobSize_Object((1,3,6,1,4,1,1347,43,22,3,1,7),_KcprtTrayJobSize_Type())
kcprtTrayJobSize.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtTrayJobSize.setStatus(_A)
class _KcprtTrayJobStorageResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,255)));namedValues=NamedValues(*(('noError',0),('error',1),(_S,255)))
_KcprtTrayJobStorageResult_Type.__name__=_C
_KcprtTrayJobStorageResult_Object=MibTableColumn
kcprtTrayJobStorageResult=_KcprtTrayJobStorageResult_Object((1,3,6,1,4,1,1347,43,22,3,1,8),_KcprtTrayJobStorageResult_Type())
kcprtTrayJobStorageResult.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtTrayJobStorageResult.setStatus(_A)
_KcprtSubUnit_ObjectIdentity=ObjectIdentity
kcprtSubUnit=_KcprtSubUnit_ObjectIdentity((1,3,6,1,4,1,1347,43,23))
_KcprtSubUnitTable_Object=MibTable
kcprtSubUnitTable=_KcprtSubUnitTable_Object((1,3,6,1,4,1,1347,43,23,1))
if mibBuilder.loadTexts:kcprtSubUnitTable.setStatus(_A)
_KcprtSubUnitEntry_Object=MibTableRow
kcprtSubUnitEntry=_KcprtSubUnitEntry_Object((1,3,6,1,4,1,1347,43,23,1,1))
kcprtSubUnitEntry.setIndexNames((0,_F,_G),(0,_E,_A7))
if mibBuilder.loadTexts:kcprtSubUnitEntry.setStatus(_A)
_KcprtSubUnitIndex_Type=Integer32
_KcprtSubUnitIndex_Object=MibTableColumn
kcprtSubUnitIndex=_KcprtSubUnitIndex_Object((1,3,6,1,4,1,1347,43,23,1,1,1),_KcprtSubUnitIndex_Type())
kcprtSubUnitIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:kcprtSubUnitIndex.setStatus(_A)
class _KcprtSubUnitModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_KcprtSubUnitModel_Type.__name__=_H
_KcprtSubUnitModel_Object=MibTableColumn
kcprtSubUnitModel=_KcprtSubUnitModel_Object((1,3,6,1,4,1,1347,43,23,1,1,2),_KcprtSubUnitModel_Type())
kcprtSubUnitModel.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSubUnitModel.setStatus(_A)
class _KcprtSubUnitAbsoluteModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_KcprtSubUnitAbsoluteModel_Type.__name__=_H
_KcprtSubUnitAbsoluteModel_Object=MibTableColumn
kcprtSubUnitAbsoluteModel=_KcprtSubUnitAbsoluteModel_Object((1,3,6,1,4,1,1347,43,23,1,1,3),_KcprtSubUnitAbsoluteModel_Type())
kcprtSubUnitAbsoluteModel.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSubUnitAbsoluteModel.setStatus(_A)
_KcprtSubUnitTableIndex_Type=Integer32
_KcprtSubUnitTableIndex_Object=MibTableColumn
kcprtSubUnitTableIndex=_KcprtSubUnitTableIndex_Object((1,3,6,1,4,1,1347,43,23,1,1,4),_KcprtSubUnitTableIndex_Type())
kcprtSubUnitTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSubUnitTableIndex.setStatus(_A)
_KcprtSubUnitObjectIndex_Type=Integer32
_KcprtSubUnitObjectIndex_Object=MibTableColumn
kcprtSubUnitObjectIndex=_KcprtSubUnitObjectIndex_Object((1,3,6,1,4,1,1347,43,23,1,1,5),_KcprtSubUnitObjectIndex_Type())
kcprtSubUnitObjectIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtSubUnitObjectIndex.setStatus(_A)
_KcprtJob_ObjectIdentity=ObjectIdentity
kcprtJob=_KcprtJob_ObjectIdentity((1,3,6,1,4,1,1347,43,24))
_KcprtJobGeneralTable_Object=MibTable
kcprtJobGeneralTable=_KcprtJobGeneralTable_Object((1,3,6,1,4,1,1347,43,24,1))
if mibBuilder.loadTexts:kcprtJobGeneralTable.setStatus(_A)
_KcprtJobGeneralEntry_Object=MibTableRow
kcprtJobGeneralEntry=_KcprtJobGeneralEntry_Object((1,3,6,1,4,1,1347,43,24,1,1))
kcprtJobGeneralEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:kcprtJobGeneralEntry.setStatus(_A)
_KcprtJobMaxEntryNumber_Type=Integer32
_KcprtJobMaxEntryNumber_Object=MibTableColumn
kcprtJobMaxEntryNumber=_KcprtJobMaxEntryNumber_Object((1,3,6,1,4,1,1347,43,24,1,1,1),_KcprtJobMaxEntryNumber_Type())
kcprtJobMaxEntryNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtJobMaxEntryNumber.setStatus(_A)
_KcprtJobNewestJobIndex_Type=Integer32
_KcprtJobNewestJobIndex_Object=MibTableColumn
kcprtJobNewestJobIndex=_KcprtJobNewestJobIndex_Object((1,3,6,1,4,1,1347,43,24,1,1,2),_KcprtJobNewestJobIndex_Type())
kcprtJobNewestJobIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:kcprtJobNewestJobIndex.setStatus(_A)
class _KcprtJobCancelByJobOwner_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_KcprtJobCancelByJobOwner_Type.__name__=_H
_KcprtJobCancelByJobOwner_Object=MibTableColumn
kcprtJobCancelByJobOwner=_KcprtJobCancelByJobOwner_Object((1,3,6,1,4,1,1347,43,24,1,1,3),_KcprtJobCancelByJobOwner_Type())
kcprtJobCancelByJobOwner.setMaxAccess('write-only')
if mibBuilder.loadTexts:kcprtJobCancelByJobOwner.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'kyocera':kyocera,'kcPrinter':kcPrinter,'kcprtGeneral':kcprtGeneral,'kcprtGeneralTable':kcprtGeneralTable,'kcprtGeneralEntry':kcprtGeneralEntry,'kcprtGeneralModelName':kcprtGeneralModelName,'kcprtOptionVersion':kcprtOptionVersion,'kcprtKpdlLevel':kcprtKpdlLevel,'kcprtSystemUpTime':kcprtSystemUpTime,'kcprtBinNumber':kcprtBinNumber,'kcprtCardSlotCapacity':kcprtCardSlotCapacity,'kcprtRomSlotNumber':kcprtRomSlotNumber,'kcprtSimmSlotCapacity':kcprtSimmSlotCapacity,'kcprtSimmSlotUsed':kcprtSimmSlotUsed,'kcprtOriginalMemorySize':kcprtOriginalMemorySize,'kcprtTotalMemorySize':kcprtTotalMemorySize,'kcprtUserMemorySize':kcprtUserMemorySize,'kcprtVirtualMemory':kcprtVirtualMemory,'kcprtPageMemorySize':kcprtPageMemorySize,'kcprtHostBufferSize':kcprtHostBufferSize,'kcprtHostBuffer1stRate':kcprtHostBuffer1stRate,'kcprtHostBuffer2ndRate':kcprtHostBuffer2ndRate,'kcprtHostBuffer3rdRate':kcprtHostBuffer3rdRate,'kcprtHostBufferOption':kcprtHostBufferOption,'kcprtBufferXoffLevel':kcprtBufferXoffLevel,'kcprtBufferXonLevel':kcprtBufferXonLevel,'kcprtFFTimeout':kcprtFFTimeout,'kcprtSleepTimer':kcprtSleepTimer,'kcprtWakeupStatusPage':kcprtWakeupStatusPage,'kcprtOnlineControl':kcprtOnlineControl,'kcprtCopyCount':kcprtCopyCount,'kcprtContinueKey':kcprtContinueKey,'kcprtSerialNumber':kcprtSerialNumber,'kcprtAssetNumber':kcprtAssetNumber,'kcprtSignature':kcprtSignature,'kcprtFirmParamCurrentRegister':kcprtFirmParamCurrentRegister,'kcprtFirmParamCurrentValue':kcprtFirmParamCurrentValue,'kcprtSleepMode':kcprtSleepMode,'kcprtAutoContinueMode':kcprtAutoContinueMode,'kcprtAutoContinueTimer':kcprtAutoContinueTimer,'kcprtAbsoluteModelName':kcprtAbsoluteModelName,'kcprtEquipmentID':kcprtEquipmentID,'kcprtMaxCopyCount':kcprtMaxCopyCount,'kcprtCpuTable':kcprtCpuTable,'kcprtCpuEntry':kcprtCpuEntry,_c:kcprtCpuIndex,'kcprtCpuName':kcprtCpuName,'kcprtCpuClock':kcprtCpuClock,'kcprtCpuRole':kcprtCpuRole,'kcprtFirmwareVersion':kcprtFirmwareVersion,'kcprtFirmwareUpdate':kcprtFirmwareUpdate,'kcprtInput':kcprtInput,'kcprtInputTable':kcprtInputTable,'kcprtInputEntry':kcprtInputEntry,_e:kcprtInputIndex,'kcprtInputMPtrayMode':kcprtInputMPtrayMode,'kcprtInputGroupMember':kcprtInputGroupMember,'kcprtInputMediaListIndex':kcprtInputMediaListIndex,'kcprtInputStatus':kcprtInputStatus,'kcprtInputDialPaperSize':kcprtInputDialPaperSize,'kcprtInputOtherPaperSize':kcprtInputOtherPaperSize,'prtInputCustomDimFeedDirDeclared':prtInputCustomDimFeedDirDeclared,'prtInputCustomDimXFeedDirDeclared':prtInputCustomDimXFeedDirDeclared,'kcprnInputMediaMatrix':kcprnInputMediaMatrix,'kcprnInputPaperSizeIndex':kcprnInputPaperSizeIndex,'kcprtInputGroupTable':kcprtInputGroupTable,'kcprtInputGroupEntry':kcprtInputGroupEntry,_f:kcprtInputGroupIndex,'kcprtInputGroupMode':kcprtInputGroupMode,'kcprtOutput':kcprtOutput,'kcprtOutputTable':kcprtOutputTable,'kcprtOutputEntry':kcprtOutputEntry,_R:kcprtOutputIndex,'kcprtOutputMode':kcprtOutputMode,'kcprtOutputMultiMode':kcprtOutputMultiMode,'kcprtOutputGroupNumber':kcprtOutputGroupNumber,'kcprtOutputDefaultGroup':kcprtOutputDefaultGroup,'kcprtOutputBulkStatus':kcprtOutputBulkStatus,'kcprtOutputTrayMaxCapacity':kcprtOutputTrayMaxCapacity,'kcprtStapler':kcprtStapler,'kcprtStaplerConsumableState':kcprtStaplerConsumableState,'kcprtOutputActionOnFull':kcprtOutputActionOnFull,'kcprtOutputPunchStatus':kcprtOutputPunchStatus,'kcprtOutputStatus':kcprtOutputStatus,'kcprtTrayGroupTable':kcprtTrayGroupTable,'kcprtTrayGroupEntry':kcprtTrayGroupEntry,_g:kcprtTrayGroupIndex,'kcprtTrayGroupBeginIndex':kcprtTrayGroupBeginIndex,'kcprtTrayGroupEndIndex':kcprtTrayGroupEndIndex,'kcprtOutputTrayTable':kcprtOutputTrayTable,'kcprtOutputTrayEntry':kcprtOutputTrayEntry,_h:kcprtOutputTrayIndex,'kcprtOutputTrayOrder':kcprtOutputTrayOrder,'kcprtOutputTrayGroup':kcprtOutputTrayGroup,'kcprtOutputTrayCount':kcprtOutputTrayCount,'kcprtOutputTrayName':kcprtOutputTrayName,'kcprtPunchGroupTable':kcprtPunchGroupTable,'kcprtPunchGroupEntry':kcprtPunchGroupEntry,_i:kcprtPunchGroupIndex,'kcprtPunchGroupName':kcprtPunchGroupName,'kcprtPunchGroupHoleNumber':kcprtPunchGroupHoleNumber,'kcprtPunchGroupType':kcprtPunchGroupType,'kcprtMarker':kcprtMarker,'kcprtMarkerTable':kcprtMarkerTable,'kcprtMarkerEntry':kcprtMarkerEntry,'kcprtMarkerIndex':kcprtMarkerIndex,'kcprtMarkerKirLevel':kcprtMarkerKirLevel,'kcprtMarkerEcoprintLevel':kcprtMarkerEcoprintLevel,'kcprtMarkerAddressabilityFeedDirDeclared':kcprtMarkerAddressabilityFeedDirDeclared,'kcprtMarkerAddressabilityXFeedDirDeclared':kcprtMarkerAddressabilityXFeedDirDeclared,'kcprtMarkerAddressabilityFeedDirChosen':kcprtMarkerAddressabilityFeedDirChosen,'kcprtMarkerAddressabilityXFeedDirChosen':kcprtMarkerAddressabilityXFeedDirChosen,'kcprtMarkerDrumCounter':kcprtMarkerDrumCounter,'kcprtMarkerColorMode':kcprtMarkerColorMode,'kcprtMarkerBitsPerPixel':kcprtMarkerBitsPerPixel,'kcprtMarkerGlossMode':kcprtMarkerGlossMode,'kcprtMarkerServiceCount':kcprtMarkerServiceCount,'kcprtColorant':kcprtColorant,'kcprtColorantGeneralTable':kcprtColorantGeneralTable,'kcprtColorantGeneralEntry':kcprtColorantGeneralEntry,'kcprtColorQuality':kcprtColorQuality,'kcprtColorMatching':kcprtColorMatching,'kcprtColorantIdentifier':kcprtColorantIdentifier,'kcprtRGBSimulation':kcprtRGBSimulation,'kcprtCMYKSimulation':kcprtCMYKSimulation,'kcprtChannel':kcprtChannel,'kcprtChannelTable':kcprtChannelTable,'kcprtChannelEntry':kcprtChannelEntry,_l:kcprtChannelIndex,'kcprtChannelMode':kcprtChannelMode,'kcprtChannelCopyCount':kcprtChannelCopyCount,'kcprtChannelResolution':kcprtChannelResolution,'kcprtChannelPaperSize':kcprtChannelPaperSize,'kcprtHostBufferRatio':kcprtHostBufferRatio,'kcprtChannelErrorCounter':kcprtChannelErrorCounter,'kcprtBuzzer':kcprtBuzzer,'kcprtBuzzerTable':kcprtBuzzerTable,'kcprtBuzzerEntry':kcprtBuzzerEntry,_m:kcprtBuzzerIndex,'kcprtBuzzerOnTime':kcprtBuzzerOnTime,'kcprtBuzzerOffTime':kcprtBuzzerOffTime,'kcprtBuzzerMode':kcprtBuzzerMode,'kcprtBuzzerTone':kcprtBuzzerTone,'kcprtAlert':kcprtAlert,'kcprtAlertTable':kcprtAlertTable,'kcprtAlertEntry':kcprtAlertEntry,_n:kcprtAlertIndex,'kcprtAlertInformation':kcprtAlertInformation,'kcprtAlertStateTable':kcprtAlertStateTable,'kcprtAlertStateEntry':kcprtAlertStateEntry,_o:kcprtAlertStateDisplayIndex,'kcprtAlertStateDisplay':kcprtAlertStateDisplay,'kcprtAlertStateCode':kcprtAlertStateCode,'kcprtAlertJamLogTable':kcprtAlertJamLogTable,'kcprtAlertJamLogEntry':kcprtAlertJamLogEntry,_p:kcprtAlertJamLogIndex,'kcprtAlertJamLogStamp':kcprtAlertJamLogStamp,'kcprtAlertJamLogFactor':kcprtAlertJamLogFactor,'kcprtAlertJamLogPosition':kcprtAlertJamLogPosition,'kcprtAlertJamLogInput':kcprtAlertJamLogInput,'kcprtAlertJamLogPaper':kcprtAlertJamLogPaper,'kcprtAlertJamLogMedia':kcprtAlertJamLogMedia,'kcprtAlertJamLogOutput':kcprtAlertJamLogOutput,'kcprtAlertCallLogTable':kcprtAlertCallLogTable,'kcprtAlertCallLogEntry':kcprtAlertCallLogEntry,_q:kcprtAlertCallLogIndex,'kcprtAlertCallLogStamp':kcprtAlertCallLogStamp,'kcprtAlertCallLogFactor':kcprtAlertCallLogFactor,'kcprtAlertChangeLogTable':kcprtAlertChangeLogTable,'kcprtAlertChangeLogEntry':kcprtAlertChangeLogEntry,_r:kcprtAlertChangeLogIndex,'kcprtAlertChangeLogStamp':kcprtAlertChangeLogStamp,'kcprtAlertChangeLogKind':kcprtAlertChangeLogKind,'kcprtAlertEventCountTable':kcprtAlertEventCountTable,'kcprtAlertEventCountEntry':kcprtAlertEventCountEntry,_s:kcprtAlertEventCountIndex,'kcprtAlertEventCountFactor':kcprtAlertEventCountFactor,'kcprtAlertEventCountValue':kcprtAlertEventCountValue,'kcprtMemoryResource':kcprtMemoryResource,'kcprtMemoryDeviceTable':kcprtMemoryDeviceTable,'kcprtMemoryDeviceEntry':kcprtMemoryDeviceEntry,_t:kcprtMemoryDeviceIndex,'kcprtMemoryDeviceLocation':kcprtMemoryDeviceLocation,'kcprtMemoryDeviceType':kcprtMemoryDeviceType,'kcprtMemoryDeviceTotalSize':kcprtMemoryDeviceTotalSize,'kcprtMemoryDeviceUsedSize':kcprtMemoryDeviceUsedSize,'kcprtMemoryDeviceStatus':kcprtMemoryDeviceStatus,'kcprtMemoryDeviceUnit':kcprtMemoryDeviceUnit,'kcprtPartitionTable':kcprtPartitionTable,'kcprtPartitionEntry':kcprtPartitionEntry,_u:kcprtPartitionIndex,'kcprtPartitionSize':kcprtPartitionSize,'kcprtPartitionLocation':kcprtPartitionLocation,'kcprtPartitionResourceType':kcprtPartitionResourceType,'kcprtPartitionName':kcprtPartitionName,'kcprtPartitionLoad':kcprtPartitionLoad,'kcprtMacroDataTable':kcprtMacroDataTable,'kcprtMacroDataEntry':kcprtMacroDataEntry,_v:kcprtMacroDataIndex,'kcprtMacroDataName':kcprtMacroDataName,'kcprtMacroDataID':kcprtMacroDataID,'kcprtMacroDataType':kcprtMacroDataType,'kcprtMacroDataAutoLoad':kcprtMacroDataAutoLoad,'kcprtMacroDataLocation':kcprtMacroDataLocation,'kcprtMacroDataAttribute':kcprtMacroDataAttribute,'kcprtHostDataTable':kcprtHostDataTable,'kcprtHostDataEntry':kcprtHostDataEntry,_x:kcprtHostDataIndex,'kcprtHostDataName':kcprtHostDataName,'kcprtHostDataLocation':kcprtHostDataLocation,'kcprtHostDataAttribute':kcprtHostDataAttribute,'kcprtProgramDataTable':kcprtProgramDataTable,'kcprtProgramDataEntry':kcprtProgramDataEntry,_y:kcprtProgramDataIndex,'kcprtProgramDataName':kcprtProgramDataName,'kcprtProgramDataType':kcprtProgramDataType,'kcprtProgramDataLocation':kcprtProgramDataLocation,'kcprtProgramDataAttribute':kcprtProgramDataAttribute,'kcprtMessageDataTable':kcprtMessageDataTable,'kcprtMessageDataEntry':kcprtMessageDataEntry,_z:kcprtMessageDataIndex,'kcprtMessageDataName':kcprtMessageDataName,'kcprtMessageDataLocation':kcprtMessageDataLocation,'kcprtMessageDataAttribute':kcprtMessageDataAttribute,'kcprtFontDataTable':kcprtFontDataTable,'kcprtFontDataEntry':kcprtFontDataEntry,_A0:kcprtFontDataIndex,'kcprtTypeFaceName':kcprtTypeFaceName,'kcprtFontID':kcprtFontID,'kcprtFontType':kcprtFontType,'kcprtFontLocation':kcprtFontLocation,'kcprtFontAttribute':kcprtFontAttribute,'kcprtFileStorageTable':kcprtFileStorageTable,'kcprtFileStorageEntry':kcprtFileStorageEntry,_A1:kcprtFileStorageIndex,'kcprtFileStorageLimitSize':kcprtFileStorageLimitSize,'kcprtFileStorageUsedSize':kcprtFileStorageUsedSize,'kcprtFileStorageUnit':kcprtFileStorageUnit,'kcprtFileStorageCounter':kcprtFileStorageCounter,'kcprtFileTable':kcprtFileTable,'kcprtFileEntry':kcprtFileEntry,_A2:kcprtFileIndex,'kcprtFileName':kcprtFileName,'kcprtFileSize':kcprtFileSize,'kcprtSJobStorageTable':kcprtSJobStorageTable,'kcprtSJobStorageEntry':kcprtSJobStorageEntry,_A3:kcprtSJobStorageIndex,'kcprtSJobStorageLimitSize':kcprtSJobStorageLimitSize,'kcprtSJobStorageUsedSize':kcprtSJobStorageUsedSize,'kcprtSJobStorageUnit':kcprtSJobStorageUnit,'kcprtSJobStorageStateCounter':kcprtSJobStorageStateCounter,'kcprtSJobStorageAttribute':kcprtSJobStorageAttribute,'kcprtSJobTable':kcprtSJobTable,'kcprtSJobEntry':kcprtSJobEntry,_A4:kcprtSJobIndex,'kcprtSjobID':kcprtSjobID,'kcprtSJobName':kcprtSJobName,'kcprtSJobOwner':kcprtSJobOwner,'kcprtSJobTime':kcprtSJobTime,'kcprtSJobPageNumber':kcprtSJobPageNumber,'kcprtSJobSize':kcprtSJobSize,'kcprtSJobStorageRef':kcprtSJobStorageRef,'kcprtSJobCopyCount':kcprtSJobCopyCount,'kcprtSJobBarcodePrintExistence':kcprtSJobBarcodePrintExistence,'kcprtSJobDuplexMode':kcprtSJobDuplexMode,'kcprtSJobOutputIndex':kcprtSJobOutputIndex,'kcprtSJobStaplePosition':kcprtSJobStaplePosition,'kcprtSJobBarcodePosition':kcprtSJobBarcodePosition,'kcprtSJobStapleAndFoldCount':kcprtSJobStapleAndFoldCount,'kcprtSJobFoldMode':kcprtSJobFoldMode,'kcprtSJobPunchMode':kcprtSJobPunchMode,'kcprtSJobTransparencySeparationMode':kcprtSJobTransparencySeparationMode,'kcprtSJobTransparencySeparationInputIndex':kcprtSJobTransparencySeparationInputIndex,'kcprtSJobRotatedCollationMode':kcprtSJobRotatedCollationMode,'kcprtSJobBookletMode':kcprtSJobBookletMode,'kcprtSJobJobOffsetMode':kcprtSJobJobOffsetMode,'kcprtMediaList':kcprtMediaList,'kcprtMediaTable':kcprtMediaTable,'kcprtMediaEntry':kcprtMediaEntry,_A5:kcprtMediaIndex,'kcprtMediaName':kcprtMediaName,'kcprtMediaWeight':kcprtMediaWeight,'kcprtMediaFuserMode':kcprtMediaFuserMode,'kcprtMediaPathType':kcprtMediaPathType,'kcprtMediaDensity':kcprtMediaDensity,'kcprtMediaManageLevel':kcprtMediaManageLevel,'kcprtMailBox':kcprtMailBox,'kcprtMailBoxTable':kcprtMailBoxTable,'kcprtMailBoxEntry':kcprtMailBoxEntry,_T:kcprtMailBoxIndex,'kcprtMailBoxDeviceIndex':kcprtMailBoxDeviceIndex,'kcprtMailBoxStateCounter':kcprtMailBoxStateCounter,'kcprtMailBoxUsedTrays':kcprtMailBoxUsedTrays,'kcprtMailBoxDocumentsNumber':kcprtMailBoxDocumentsNumber,'kcprtMailBoxPageNumber':kcprtMailBoxPageNumber,'kcprtMailBoxUsedSize':kcprtMailBoxUsedSize,'kcprtMailBoxLimitSize':kcprtMailBoxLimitSize,'kcprtMailBoxMaxLimitSize':kcprtMailBoxMaxLimitSize,'kcprtMailBoxUnit':kcprtMailBoxUnit,'kcprtMailBoxAliasCheck':kcprtMailBoxAliasCheck,'kcprtMailBoxTrayTable':kcprtMailBoxTrayTable,'kcprtMailBoxTrayEntry':kcprtMailBoxTrayEntry,_X:kcprtMailBoxTrayIndex,'kcprtMailBoxTrayUsedFlag':kcprtMailBoxTrayUsedFlag,'kcprtMailBoxTrayLabel':kcprtMailBoxTrayLabel,'kcprtMailBoxTrayLock':kcprtMailBoxTrayLock,'kcprtMailBoxTrayDocumentsNumber':kcprtMailBoxTrayDocumentsNumber,'kcprtMailBoxTrayPageNumber':kcprtMailBoxTrayPageNumber,'kcprtMailBoxTrayOccupiedSize':kcprtMailBoxTrayOccupiedSize,'kcprtMailBoxTraySharedSize':kcprtMailBoxTraySharedSize,'kcprtMailBoxTrayErrorLogNumber':kcprtMailBoxTrayErrorLogNumber,'kcprtMailBoxTrayPurgeDocuments':kcprtMailBoxTrayPurgeDocuments,'kcprtMailBoxTrayReset':kcprtMailBoxTrayReset,'kcprtTrayJobTable':kcprtTrayJobTable,'kcprtTrayJobEntry':kcprtTrayJobEntry,_A6:kcprtTrayJobIndex,'kcprtTrayJobID':kcprtTrayJobID,'kcprtTrayJobName':kcprtTrayJobName,'kcprtTrayJobOwner':kcprtTrayJobOwner,'kcprtTrayJobTime':kcprtTrayJobTime,'kcprtTrayJobPageNumber':kcprtTrayJobPageNumber,'kcprtTrayJobSize':kcprtTrayJobSize,'kcprtTrayJobStorageResult':kcprtTrayJobStorageResult,'kcprtSubUnit':kcprtSubUnit,'kcprtSubUnitTable':kcprtSubUnitTable,'kcprtSubUnitEntry':kcprtSubUnitEntry,_A7:kcprtSubUnitIndex,'kcprtSubUnitModel':kcprtSubUnitModel,'kcprtSubUnitAbsoluteModel':kcprtSubUnitAbsoluteModel,'kcprtSubUnitTableIndex':kcprtSubUnitTableIndex,'kcprtSubUnitObjectIndex':kcprtSubUnitObjectIndex,'kcprtJob':kcprtJob,'kcprtJobGeneralTable':kcprtJobGeneralTable,'kcprtJobGeneralEntry':kcprtJobGeneralEntry,'kcprtJobMaxEntryNumber':kcprtJobMaxEntryNumber,'kcprtJobNewestJobIndex':kcprtJobNewestJobIndex,'kcprtJobCancelByJobOwner':kcprtJobCancelByJobOwner})